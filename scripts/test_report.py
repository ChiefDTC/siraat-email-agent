#!/usr/bin/env python3
"""Testrapport v4-flows: cijfers per arm, kans dat B beter is, stopregel en advies.

Draaien (vanuit /tmp, met `python3 -I`; Klaviyo alleen lezen: GET en report-POSTs, sleutel via de proxy):

  python3 -I /home/user/siraat-email-agent/scripts/test_report.py
      Live: alle v4-flows ("v4 · ..." in Klaviyo) sinds livegang (standaard 2026-10-08) tot nu.
      Schrijft exports/tests/results-YYYY-MM-DD.md en .csv.

  --dry-run            Proef op de OUDE flows (Y2TmNB, Tsg2tV, SwkMyn, TBWngE, TyEjuQ, Wj6x6V, SiaNLu):
                       bestaande splits in die flows spelen arm A en arm B. Standaard laatste 42 dagen.
                       Schrijft results-YYYY-MM-DD-dryrun.md/.csv.
  --cohort             Ook cohortconversie en cohortomzet per arm (Placed Order binnen 7 dagen na de
                       instapmail, welcome 14), los van Klaviyo-attributie. Leest Placed Order-events en
                       per koper de Received Email-events (GET). Cache: ~/.cache/siraat-test-report/.
  --cohort-max=N       Hoogstens N kopers ophalen (alleen om te proberen; uitkomst is dan onvolledig).
  --since=YYYY-MM-DD   Begin (UTC). --until=YYYY-MM-DD einde (exclusief, standaard nu).
  --plan               Volumes van de oude flows (laatste 8 volle weken) en steekproef/looptijd per test.
                       Schrijft exports/tests/plan-YYYY-MM-DD.md.
  --today=YYYY-MM-DD   Rapportdatum overschrijven (voor tests van de beslisregels).

Wat het doet:
  1. Eén flow-series-report (dagelijks, conversion metric Placed Order RSNxYV) per bericht voor alle
     testflows. Dagen in de BFCM-bevriezing (20 nov t/m 6 dec 2026) tellen niet mee en worden apart getoond.
  2. Berichten naar arm op naam (scripts/build_flows.py): "Old · ..." tegen v4 (T01), "CODE · X" tegen
     "X nocode · T02-B" (T02, cooldown telt niet mee), "W1 · T04-A/B" (T04), "B1 · T05a-A/B" (T05a).
  3. Per arm: RPR, conversie, klik, uitschrijving, spam, AOV. T01 per instromer (n = delivered van de
     eerste mail van het pad, omzet = alle mails van het pad).
  4. Kans dat B beter is: Beta-binomiaal voor ratio's; voor RPR conversie x orderwaarde (Gamma, CV 0,7).
     T02 gepoold over strata (gewicht = ontvangers per stratum) plus P(codelift > breakeven 20%).
  5. Advies volgens research/testing/05-beslisregels.md.
"""
import concurrent.futures as cf
import csv, datetime as dt, json, math, os, re, subprocess, sys, time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "exports/tests")
CACHE = os.path.join(os.path.expanduser("~"), ".cache", "siraat-test-report")
REV = "2025-10-15"
PLACED_ORDER, RECEIVED_EMAIL = "RSNxYV", "YkRM4Q"
ARGS = sys.argv[1:]
DRY = "--dry-run" in ARGS
COHORT = "--cohort" in ARGS
PLAN = "--plan" in ARGS
SIMS = 40000
CV_ORDER = 0.7          # variatiecoëfficiënt orderwaarde (01-meetkader §3.1), tot er orderdata is
BREAKEVEN = 0.20        # codelift die 10% korting terugverdient bij 60% marge (01 §1.4)
FREEZE = (dt.date(2026, 11, 20), dt.date(2026, 12, 6))  # BFCM, inclusief
GO_LIVE = dt.date(2026, 10, 8)
PHASE1_END = dt.date(2026, 11, 19)
OBSOLETE = {"Y6yj2z"}
RNG = np.random.default_rng(20261008)


def opt(name, default=None):
    for a in ARGS:
        if a.startswith(f"--{name}="):
            return a.split("=", 1)[1]
    return default


TODAY = dt.date.fromisoformat(opt("today")) if opt("today") else dt.datetime.now(dt.timezone.utc).date()


# ---------------------------------------------------------------- API (alleen lezen)
def api(method, path, body=None, tries=6):
    url = path if path.startswith("http") else f"https://a.klaviyo.com/api/{path}"
    cmd = ["curl", "-sS", "-g", "-X", method, url, "-H", f"revision: {REV}",
           "-H", "accept: application/vnd.api+json", "-H", "content-type: application/vnd.api+json",
           "-w", "\n%{http_code}"]
    if body is not None:
        cmd += ["--data-binary", "@-"]
    for i in range(tries):
        out = subprocess.run(cmd, input=json.dumps(body) if body is not None else None,
                             capture_output=True, text=True)
        txt, _, code = (out.stdout or "").rpartition("\n")
        if code == "429" or code.startswith("5"):
            wait = 31 if "report" in url else 2 * (i + 1)
            print(f"  {code} op {url.split('/api/')[-1][:40]}, {wait}s wachten", file=sys.stderr)
            time.sleep(wait)
            continue
        try:
            d = json.loads(txt or "{}")
        except json.JSONDecodeError:
            d = {"errors": [{"detail": (txt or out.stderr)[:300]}]}
        if "errors" in d:
            raise RuntimeError(f"Klaviyo {code} op {url}: {d['errors'][0].get('detail')}")
        return d
    raise RuntimeError(f"Klaviyo bleef 429/5xx geven op {url}")


def get_all(path, max_pages=500):
    rows, url = [], path
    for _ in range(max_pages):
        d = api("GET", url)
        rows += d.get("data", [])
        url = (d.get("links") or {}).get("next")
        if not url:
            break
    return rows


def series(flow_ids, start, end):
    """Dagelijkse cijfers per bericht. Eén report-call (limiet 2 per minuut, 225 per dag)."""
    stats = ["recipients", "delivered", "clicks_unique", "conversion_uniques", "conversions",
             "conversion_value", "unsubscribe_uniques", "spam_complaints", "bounced"]
    ids = ",".join(f'"{f}"' for f in flow_ids)
    body = {"data": {"type": "flow-series-report", "attributes": {
        "statistics": stats, "interval": "daily", "conversion_metric_id": PLACED_ORDER,
        "timeframe": {"start": f"{start}T00:00:00+00:00", "end": f"{end}T00:00:00+00:00"},
        "group_by": ["flow_id", "flow_name", "flow_message_id", "flow_message_name", "send_channel"],
        "filter": f"contains-any(flow_id,[{ids}])"}}}
    a = api("POST", "flow-series-reports/", body)["data"]["attributes"]
    days = [dt.date.fromisoformat(x[:10]) for x in a["date_times"]]
    msgs = []
    for r in a["results"]:
        g = r["groupings"]
        if g.get("send_channel") not in (None, "email"):
            continue
        msgs.append({"flow_id": g["flow_id"], "flow_name": g.get("flow_name", ""),
                     "msg_id": g["flow_message_id"], "name": (g.get("flow_message_name") or "").strip(),
                     "daily": {k: [float(v or 0) for v in r["statistics"][k]] for k in stats}})
    return days, msgs


# ---------------------------------------------------------------- testdefinities
# Elke test: strata; elk stratum kiest berichten voor arm A en B (regex op de berichtnaam) binnen een flow.
# unit "entrant": n = delivered van de instapmail(s) (entry_a/entry_b), omzet en klik over het hele pad.
# unit "message": n = delivered van de berichten zelf.
# Live namen komen uit scripts/build_flows.py (OVERZICHT.md).
WELCOME_W = 14
LIVE_TESTS = [
    {"id": "T01", "title": "Oud tegen nieuw (padsplit 50/50)", "unit": "entrant", "rule": "oldnew",
     "a": "Oud pad", "b": "v4", "primary": "rpr", "planned_end": PHASE1_END, "strata": [
         {"key": "checkout", "flow": "v4 · Checkout abandonment", "window": 7,
          "arm_a": r"^Old · ", "arm_b": r"^(?!Old · ).+", "entry_a": r"^Old · Checkout 1$", "entry_b": r"^C1$"},
         {"key": "cart", "flow": "v4 · Cart abandonment", "window": 7,
          "arm_a": r"^Old · ", "arm_b": r"^(?!Old · ).+", "entry_a": r"^Old · Cart 1$", "entry_b": r"^K1(-ACC)?$"},
         {"key": "browse", "flow": "v4 · Browse abandonment", "window": 7,
          "arm_a": r"^Old · ", "arm_b": r"^(?!Old · ).+", "entry_a": r"^Old · Browse 1$",
          "entry_b": r"^B1( · T05a-[AB])?$|^B1-ACC$"},
         {"key": "welcome", "flow": "v4 · Welcome", "window": WELCOME_W,
          "arm_a": r"^Old · ", "arm_b": r"^(?!Old · ).+", "entry_a": r"^Old · Welcome 1$",
          "entry_b": r"^W0$|^W1( · T04-[AB])?$"},
     ]},
    {"id": "T02", "title": "Unieke code tegen geen code in de laatste mail (gepoold)", "unit": "message",
     "rule": "code", "a": "CODE", "b": "geen code (T02-B)", "primary": "rpr", "planned_end": None,
     "dynamic": {"arm_a": r"^CODE · (?!V1$|N2$)(?P<s>.+)$", "arm_b": r"^(?P<s>.+) nocode · T02-B$"},
     "window": 7, "strata": []},
    {"id": "T04", "title": "W1: HI10 als code-blok (A) tegen gift card (B)", "unit": "message", "rule": "content_rpr",
     "a": "W1-A code-blok", "b": "W1-B gift card", "primary": "rpr", "planned_end": PHASE1_END, "strata": [
         {"key": "w1", "flow": "v4 · Welcome", "window": WELCOME_W,
          "arm_a": r"^W1 · T04-A$", "arm_b": r"^W1 · T04-B$", "main": r"^W1$"}]},
    {"id": "T05a", "title": "B1-onderwerp: authority (A) tegen social proof (B)", "unit": "message",
     "rule": "subject", "a": "authority", "b": "social proof", "primary": "click", "planned_end": PHASE1_END,
     "strata": [{"key": "b1", "flow": "v4 · Browse abandonment", "window": 7,
                 "arm_a": r"^B1 · T05a-A$", "arm_b": r"^B1 · T05a-B$", "main": r"^B1$"}]},
]

# Proef op de oude flows: bestaande splits spelen A en B (zelfde rekenwerk, andere namen).
DRY_TESTS = [
    {"id": "T01", "title": "Oud tegen nieuw (PROEF: interne splits oude flows)", "unit": "entrant", "rule": "oldnew",
     "a": "pad A", "b": "pad B", "primary": "rpr", "planned_end": None, "strata": [
         {"key": "checkout", "flow": "Y2TmNB", "window": 7, "arm_a": r"^(Copy of )?Email #\d$",
          "arm_b": r"^New AB Checkout \d$", "entry_a": r"^(Copy of )?Email #1$", "entry_b": r"^New AB Checkout 1$"},
         {"key": "cart", "flow": "SwkMyn", "window": 7, "arm_a": r"^Email #[13]$", "arm_b": r"^Copy of Email #[13]$",
          "entry_a": r"^Email #1$", "entry_b": r"^Copy of Email #1$"},
         {"key": "browse", "flow": "TyEjuQ", "window": 7, "arm_a": r"^Email #1$", "arm_b": r"^Copy of Email #1$",
          "entry_a": r"^Email #1$", "entry_b": r"^Copy of Email #1$"},
         {"key": "welcome", "flow": "SiaNLu", "window": WELCOME_W, "arm_a": r".", "arm_b": r"^GEEN-ARM-B$",
          "entry_a": r"Email #1", "entry_b": r"^GEEN-ARM-B$"},
     ]},
    {"id": "T02", "title": "Code tegen geen code (PROEF: laatste mails oude flows)", "unit": "message", "rule": "code",
     "a": "A", "b": "B", "primary": "rpr", "planned_end": None, "window": 7, "strata": [
         {"key": "checkout-4", "flow": "Y2TmNB", "window": 7, "arm_a": r"^Email #4$", "arm_b": r"^New AB Checkout 4$"},
         {"key": "cart-3", "flow": "SwkMyn", "window": 7, "arm_a": r"^Email #3$", "arm_b": r"^Copy of Email #3$"},
         {"key": "cart-3-tp", "flow": "TBWngE", "window": 7, "arm_a": r"^Email #3$", "arm_b": r"^Copy of Email #3$"}]},
    {"id": "T04", "title": "W1-A tegen W1-B (PROEF: Tsg2tV Email #1 tegen Copy of Email #1)", "unit": "message",
     "rule": "content_rpr", "a": "A", "b": "B", "primary": "rpr", "planned_end": None, "strata": [
         {"key": "w1", "flow": "Tsg2tV", "window": 7, "arm_a": r"^Email #1$", "arm_b": r"^Copy of Email #1$"}]},
    {"id": "T05a", "title": "Onderwerp B1 (PROEF: Wj6x6V Email #1 tegen Copy of Email #1)", "unit": "message",
     "rule": "subject", "a": "A", "b": "B", "primary": "click", "planned_end": None, "strata": [
         {"key": "b1", "flow": "Wj6x6V", "window": 7, "arm_a": r"^Email #1$", "arm_b": r"^Copy of Email #1$"}]},
]
DRY_FLOWS = ["Y2TmNB", "Tsg2tV", "SwkMyn", "TBWngE", "TyEjuQ", "Wj6x6V", "SiaNLu"]

# Geplande n per arm (uit --plan, 7 okt 2026; zie research/testing/06-meetplan-v4.md). Sleutel test of test/stratum.
PLANNED_N = {"T01/welcome": 7700, "T01/browse": 23500, "T01/checkout": 3550, "T01/cart": 8100,
             "T02": 19500, "T04": 8200, "T05a": 14400}


# ---------------------------------------------------------------- aggregatie
STATS = ["recipients", "delivered", "clicks_unique", "conversion_uniques", "conversions", "conversion_value",
         "unsubscribe_uniques", "spam_complaints", "bounced"]


def in_freeze(d):
    return FREEZE[0] <= d <= FREEZE[1]


def day_mask(days, since, until, freeze_only=False):
    return [(since <= d < until) and (in_freeze(d) if freeze_only else not in_freeze(d)) for d in days]


def total(msgs, mask):
    t = {k: 0.0 for k in STATS}
    for m in msgs:
        for k in STATS:
            t[k] += sum(v for v, ok in zip(m["daily"][k], mask) if ok)
    return t


def flow_match(m, sel):
    return m["flow_id"] == sel or m["flow_name"] == sel


def build_strata(test, msgs):
    """Vul strata voor tests met dynamische namen (T02) en koppel berichten per arm."""
    out = []
    if test.get("dynamic"):
        groups = {}
        for m in msgs:
            for arm in ("a", "b"):
                mm = re.match(test["dynamic"][f"arm_{arm}"], m["name"])
                if mm:
                    key = f"{m['flow_name'].replace('v4 · ', '')} · {mm.group('s')}"
                    groups.setdefault(key, {"a": [], "b": []})[arm].append(m)
        for key in sorted(groups):
            out.append({"key": key, "window": test.get("window", 7), "msgs": groups[key]})
        return out
    for s in test["strata"]:
        fm = [m for m in msgs if flow_match(m, s["flow"])]
        st = dict(s, msgs={"a": [m for m in fm if re.search(s["arm_a"], m["name"])],
                           "b": [m for m in fm if re.search(s["arm_b"], m["name"])]})
        if test["unit"] == "entrant":
            st["entry"] = {"a": [m for m in fm if re.search(s["entry_a"], m["name"])],
                           "b": [m for m in fm if re.search(s["entry_b"], m["name"])]}
        if s.get("main"):
            st["main_msgs"] = [m for m in fm if re.search(s["main"], m["name"])]
        out.append(st)
    return out


def arm_numbers(test, st, arm, mask):
    t = total(st["msgs"][arm], mask)
    n = total(st["entry"][arm], mask)["delivered"] if test["unit"] == "entrant" else t["delivered"]
    return {"n": n, **t}


# ---------------------------------------------------------------- statistiek
def beta_draws(x, n):
    x, n = max(0.0, x), max(0.0, n)
    return RNG.beta(1 + x, 1 + max(0.0, n - x), SIMS)


def aov_draws(value, orders, fallback):
    if orders <= 0:
        mean, orders_eff = fallback, 1.0
    else:
        mean, orders_eff = value / orders, orders
    k = max(orders_eff, 1.0) / CV_ORDER ** 2
    return RNG.gamma(k, mean / k, SIMS)


def draws_for(arm, fallback_aov):
    n = arm["n"]
    conv = beta_draws(min(arm["conversion_uniques"], n), n)
    click = beta_draws(min(arm["clicks_unique"], n), n)
    unsub = beta_draws(min(arm["unsubscribe_uniques"], n), n)
    rpr = conv * aov_draws(arm["conversion_value"], arm["conversions"], fallback_aov)
    d = {"conv": conv, "click": click, "unsub": unsub, "rpr": rpr}
    if "cohort_buyers" in arm and arm.get("cohort_n", 0) > 0:
        cn = arm["cohort_n"]
        d["cohort"] = beta_draws(min(arm["cohort_buyers"], cn), cn)
        d["cohort_rpe"] = d["cohort"] * aov_draws(arm["cohort_rev"], arm["cohort_orders"], fallback_aov)
    return d


def summarize(da, db):
    res = {}
    for k in da:
        if k not in db:
            continue
        a, b = da[k], db[k]
        lift = b / np.maximum(a, 1e-12) - 1
        res[k] = {"p_b": float(np.mean(b > a)), "lift": float(np.median(lift)),
                  "lo": float(np.percentile(lift, 5)), "hi": float(np.percentile(lift, 95))}
    return res


def srm_p(na, nb):
    tot = na + nb
    if tot <= 0:
        return None
    e = tot / 2
    chi = (na - e) ** 2 / e + (nb - e) ** 2 / e
    return math.erfc(math.sqrt(chi / 2))


# ---------------------------------------------------------------- cohort (optioneel)
def cohort(tests_strata, since, until):
    """Placed Order binnen W dagen na de instapmail, per arm. Alleen GET op events."""
    os.makedirs(CACHE, exist_ok=True)
    cap = int(opt("cohort-max", "0") or 0)
    maxw = max(st["window"] for _, st in tests_strata)
    entry_ids = {}
    for t, st in tests_strata:
        for arm in ("a", "b"):
            src = st["entry"][arm] if t["unit"] == "entrant" else st["msgs"][arm]
            for m in src:
                entry_ids.setdefault(m["msg_id"], []).append((t["id"], st["key"], arm))
    end_orders = min(until, TODAY + dt.timedelta(days=1))
    flt = (f'and(equals(metric_id,"{PLACED_ORDER}"),greater-or-equal(datetime,{since}T00:00:00Z),'
           f'less-than(datetime,{end_orders}T00:00:00Z))')
    print(f"cohort: Placed Order-events {since} tot {end_orders} ophalen", file=sys.stderr)
    orders = get_all(f"events?filter={flt}&fields[event]=datetime,event_properties&page[size]=200", 2000)
    by_prof = {}
    for e in orders:
        pid = ((e.get("relationships") or {}).get("profile") or {}).get("data", {}).get("id")
        if not pid:
            continue
        p = e["attributes"].get("event_properties") or {}
        by_prof.setdefault(pid, []).append((e["attributes"]["datetime"], float(p.get("$value") or 0)))
    pids = sorted(by_prof)
    if cap:
        pids = pids[:cap]
    print(f"cohort: {len(orders)} orders, {len(by_prof)} kopers, {len(pids)} ophalen", file=sys.stderr)
    r_since = since - dt.timedelta(days=maxw)

    def received(pid):
        f = os.path.join(CACHE, f"{pid}.json")
        try:
            c = json.load(open(f))
            if c["from"] <= str(r_since) and c["to"] >= str(end_orders):
                return c["ev"]
        except Exception:
            pass
        flt2 = (f'and(equals(profile_id,"{pid}"),equals(metric_id,"{RECEIVED_EMAIL}"),'
                f'greater-or-equal(datetime,{r_since}T00:00:00Z),less-than(datetime,{end_orders}T00:00:00Z))')
        rows = get_all(f"events?filter={flt2}&fields[event]=datetime,event_properties&page[size]=200", 50)
        ev = [[r["attributes"]["datetime"], (r["attributes"]["event_properties"] or {}).get("$message")]
              for r in rows if (r["attributes"]["event_properties"] or {}).get("$flow")]
        json.dump({"from": str(r_since), "to": str(end_orders), "ev": ev}, open(f, "w"))
        return ev

    got = {}
    with cf.ThreadPoolExecutor(8) as ex:
        for i, (pid, ev) in enumerate(zip(pids, ex.map(received, pids))):
            got[pid] = ev
            if i and i % 500 == 0:
                print(f"  {i}/{len(pids)}", file=sys.stderr)
    # per (test, stratum, arm): unieke kopers en hun omzet binnen het venster na een rijpe instap
    res = {}
    for pid, ev in got.items():
        ords = [(dt.datetime.fromisoformat(t), v) for t, v in by_prof[pid]]
        for t_ev, mid in ev:
            for tid, key, arm in entry_ids.get(mid, []):
                st = next(s for tt, s in tests_strata if tt["id"] == tid and s["key"] == key)
                w = st["window"]
                te = dt.datetime.fromisoformat(t_ev)
                if not (since <= te.date() <= until - dt.timedelta(days=w + 1)) or in_freeze(te.date()):
                    continue
                hit = [(t, v) for t, v in ords if te < t <= te + dt.timedelta(days=w)]
                if hit:
                    slot = res.setdefault((tid, key, arm), {})
                    prev = slot.get(pid)
                    if prev is None or prev[0] > te:
                        slot[pid] = (te, sum(v for _, v in hit), len(hit))
    return res, len(pids) < len(by_prof)


# ---------------------------------------------------------------- beslisregel (05-beslisregels.md)
def verdict(test, s, a, b, days_run, planned, weekly_b):
    rule, pr = test["rule"], s.get(test["primary"] if test["primary"] != "rpr" else "rpr", {})
    conv_key = "cohort" if "cohort" in s else "conv"
    na, nb = a["n"], b["n"]
    guard = []
    if min(na, nb) >= 1000:
        ua, ub = a["unsubscribe_uniques"] / na, b["unsubscribe_uniques"] / nb
        if ub > max(0.01, 1.5 * ua):
            guard.append(f"uitschrijving B {ub:.2%} (A {ua:.2%})")
        if ua > max(0.01, 1.5 * ub):
            guard.append(f"uitschrijving A {ua:.2%} (B {ub:.2%})")
        for lab, arm in (("A", a), ("B", b)):
            if arm["spam_complaints"] / arm["n"] > 0.001:
                guard.append(f"spam {lab} {arm['spam_complaints'] / arm['n']:.3%}")
    p_srm = srm_p(na, nb)
    if p_srm is not None and p_srm < 0.01 and min(na, nb) > 0:
        guard.append(f"SRM p={p_srm:.4f}")
    if min(na, nb) == 0:
        return "GEEN DATA", "Een arm heeft geen verzendingen: split, A/B-start of berichtnamen controleren."
    if guard:
        return "STOP / ONDERZOEK", "Guardrail: " + "; ".join(guard) + ". Arm met de overschrijding stoppen als dit na een week nog zo is."
    conv_min = min(a["conversion_uniques"], b["conversion_uniques"])
    reached = planned and min(na, nb) >= planned
    horizon = reached or (test.get("planned_end") and TODAY > test["planned_end"])
    p = pr.get("p_b", 0.5)
    pc = s.get(conv_key, {}).get("p_b", 0.5)
    prog = f"{min(na, nb) / planned:.0%} van n" if planned else "geen geplande n"
    eta = ""
    if planned and weekly_b > 0 and not reached:
        eta = f", n gehaald rond {TODAY + dt.timedelta(weeks=(planned - min(na, nb)) / weekly_b):%d %b}"
    if days_run < 14 or conv_min < 30:
        return "NIET KIJKEN", f"Minder dan 14 dagen of minder dan 30 conversies per arm ({prog}{eta})."
    if rule == "oldnew":
        if p >= 0.99 and pc >= 0.9:
            return "STOP: v4 WINT", "P(v4 beter) >= 99%: oud pad mag eruit, v4 naar 100%."
        if p <= 0.05 and pc <= 0.2:
            return "LET OP: OUD BETER", "P(oud beter) >= 95%: v4 niet uitrollen in deze flow, oorzaak zoeken."
        if horizon:
            return "BESLIS: v4", f"Horizon bereikt zonder bewijs dat oud beter is: v4 naar 100% (P(v4 beter) {p:.0%})."
        return "DOORLOPEN", f"{prog}{eta}. Tot 19 november, oud pad uiterlijk dan uit."
    if rule == "code":
        pl = s.get("p_breakeven", 0.0)
        if p >= 0.99 and days_run >= 28:
            return "STOP: GEEN CODE", "P(zonder code beter op RPR) >= 99% na 4 weken: code eruit, 10% holdout houden."
        if horizon:
            if pl >= 0.80:
                return "BESLIS: CODE BLIJFT", f"P(codelift > {BREAKEVEN:.0%}) = {pl:.0%} >= 80%."
            return "BESLIS: GEEN CODE", f"P(codelift > {BREAKEVEN:.0%}) = {pl:.0%} < 80%: geen code, 10% holdout met code."
        return "DOORLOPEN", f"{prog}{eta}. P(codelift > breakeven) nu {pl:.0%}; vaste horizon, niet vroeg beslissen."
    if rule == "content_rpr":
        if p >= 0.99 and pc >= 0.9:
            return "STOP: B WINT", "P(B beter op RPR) >= 99% en conversie wijst dezelfde kant op."
        if p <= 0.01 and pc <= 0.1:
            return "STOP: A WINT", "P(A beter op RPR) >= 99%."
        if horizon:
            if p >= 0.95:
                return "BESLIS: B", f"P(B beter op RPR) {p:.0%} >= 95%."
            return "BESLIS: A", f"P(B beter op RPR) {p:.0%} < 95%: A houden (één framing overal)."
        return "DOORLOPEN", f"{prog}{eta}."
    if rule == "subject":
        rp = s.get("rpr", {}).get("p_b", 0.5)
        if horizon or (p >= 0.99 or p <= 0.01):
            if p >= 0.95 and rp >= 0.2:
                return "BESLIS: B", f"P(B beter op klik) {p:.0%}, RPR niet duidelijk slechter (P {rp:.0%})."
            if p <= 0.05 and rp <= 0.8:
                return "BESLIS: A", f"P(A beter op klik) {1 - p:.0%}."
            if horizon:
                return "BESLIS: A", f"Geen duidelijk verschil (P(B beter op klik) {p:.0%}): A houden."
        return "DOORLOPEN", f"{prog}{eta}."
    return "?", ""


# ---------------------------------------------------------------- rapport
def fmt_pct(x, d=2):
    return "" if x is None else f"{x * 100:.{d}f}%"


def run_report():
    tests = DRY_TESTS if DRY else LIVE_TESTS
    until = dt.date.fromisoformat(opt("until")) if opt("until") else TODAY + dt.timedelta(days=1)
    if opt("since"):
        since = dt.date.fromisoformat(opt("since"))
    else:
        since = (TODAY - dt.timedelta(days=42)) if DRY else GO_LIVE
    if DRY:
        flow_ids = DRY_FLOWS
    else:
        flows = get_all("flows?fields[flow]=name,status,archived")
        flow_ids = [f["id"] for f in flows if f["attributes"]["name"].startswith("v4 ·")
                    and f["id"] not in OBSOLETE and not f["attributes"].get("archived")]
        if not flow_ids:
            raise SystemExit("Geen v4-flows gevonden in Klaviyo. Gebruik --dry-run om de oude flows te testen.")
    if until <= since:
        raise SystemExit(f"Nog geen data: --since {since} ligt niet voor --until {until}.")
    print(f"flow-series-report {since} tot {until} voor {len(flow_ids)} flows", file=sys.stderr)
    days, msgs = series(flow_ids, since, until)
    mask = day_mask(days, since, until)
    fmask = day_mask(days, since, until, freeze_only=True)
    days_run = sum(1 for d, ok in zip(days, mask) if ok and d <= TODAY)
    all_t = total(msgs, mask)
    fallback_aov = all_t["conversion_value"] / all_t["conversions"] if all_t["conversions"] else 230.0

    built = [(t, build_strata(t, msgs)) for t in tests]
    coh, partial = ({}, False)
    if COHORT:
        coh, partial = cohort([(t, s) for t, ss in built for s in ss], since, until)

    rows, md = [], []
    stamp = TODAY.isoformat()
    md.append(f"# Testrapport v4-flows · {stamp}{' · PROEF op oude flows' if DRY else ''}\n")
    md.append(f"Gegenereerd door `scripts/test_report.py`{' --dry-run' if DRY else ''}{' --cohort' if COHORT else ''}. "
              f"Venster {since} tot {until} (UTC, verzenddatum), {days_run} dagen data. "
              f"Klaviyo flow-series-report, conversion metric Placed Order (RSNxYV). "
              f"BFCM-bevriezing {FREEZE[0]:%d %b} t/m {FREEZE[1]:%d %b} telt niet mee. "
              f"Beslisregels: `research/testing/05-beslisregels.md`.\n")
    if DRY:
        md.append("**Proef.** De v4-flows staan nog niet live. Arm A en B zijn hier bestaande splits in de oude flows, "
                  "alleen om te laten zien dat ophalen, groeperen en rekenen werken. Geen beslissingen op baseren.\n")
    if COHORT and partial:
        md.append(f"**Cohort onvolledig** (--cohort-max): niet alle kopers opgehaald, cohortcijfers zijn een ondergrens.\n")
    md.append("Leeswijzer: n = instromers (T01, delivered van de eerste mail van het pad) of ontvangers (overige tests). "
              "RPR = Klaviyo-geattribueerde omzet / n. Conversie (attr.) = unieke converters / n (bij T01 opgeteld over "
              "het pad, dus een bovengrens). Cohort = kopers binnen 7 dagen (welcome 14) na de instapmail, los van "
              "attributie; alleen met `--cohort`. P(B>A) = kans dat B beter is (Bayesiaans). Lift = B t.o.v. A, mediaan "
              "met 90%-interval.\n")
    summary = []
    for test, strata in built:
        md.append(f"## {test['id']} · {test['title']}\n")
        md.append(f"A = {test['a']}, B = {test['b']}. Primair: "
                  f"{'unieke klik (RPR als rem)' if test['primary'] == 'click' else 'omzet per ' + ('instromer' if test['unit'] == 'entrant' else 'ontvanger') + ' en conversie'}.\n")
        if not strata:
            md.append("_Nog geen berichten met deze namen gevonden (flow niet live of nog geen verzendingen)._\n")
            summary.append((test["id"], "-", "GEEN DATA", "Geen berichten gevonden."))
            continue
        md.append("| Stratum | Arm | Berichten | n | Omzet | RPR | Conv. (attr.) | Cohort | Klik | Uitschr. | Spam | AOV |")
        md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
        pooled_d = {"a": None, "b": None}
        pool_n = {"a": {k: 0.0 for k in STATS + ["n"]}, "b": {k: 0.0 for k in STATS + ["n"]}}
        weights, per_stratum = [], []
        for st in strata:
            arms = {}
            for arm in ("a", "b"):
                x = arm_numbers(test, st, arm, mask)
                c = coh.get((test["id"], st["key"], arm))
                if COHORT:
                    w = st["window"]
                    mmask = day_mask(days, since, until - dt.timedelta(days=w + 1))
                    src = st["entry"][arm] if test["unit"] == "entrant" else st["msgs"][arm]
                    x["cohort_n"] = total(src, mmask)["delivered"]
                    x["cohort_buyers"] = len(c or {})
                    x["cohort_rev"] = sum(v[1] for v in (c or {}).values())
                    x["cohort_orders"] = sum(v[2] for v in (c or {}).values())
                arms[arm] = x
                for k in pool_n[arm]:
                    pool_n[arm][k] += x.get(k, 0)
            a, b = arms["a"], arms["b"]
            for arm, lab in (("a", "A"), ("b", "B")):
                x = arms[arm]
                n = x["n"]
                names = "; ".join(sorted({m["name"] for m in st["msgs"][arm]}))[:80] or "(geen)"
                coh_txt = (f"{x['cohort_buyers']}/{int(x['cohort_n'])} = {fmt_pct(x['cohort_buyers'] / x['cohort_n'])}"
                           if COHORT and x.get("cohort_n") else "")
                md.append(f"| {st['key']} | {lab} | {names} | {int(n)} | ${x['conversion_value']:,.0f} | "
                          f"{'' if not n else '$%.2f' % (x['conversion_value'] / n)} | "
                          f"{'' if not n else fmt_pct(min(1, x['conversion_uniques'] / n))} | {coh_txt} | "
                          f"{'' if not n else fmt_pct(x['clicks_unique'] / n)} | "
                          f"{'' if not n else fmt_pct(x['unsubscribe_uniques'] / n)} | "
                          f"{'' if not n else fmt_pct(x['spam_complaints'] / n, 3)} | "
                          f"{'' if not x['conversions'] else '$%.0f' % (x['conversion_value'] / x['conversions'])} |")
                rows.append({"date": stamp, "mode": "dryrun" if DRY else "live", "test_id": test["id"],
                             "stratum": st["key"], "arm": lab, "arm_label": test[arm], "messages": names,
                             "n": int(n), "delivered": int(x["delivered"]), "clicks_unique": int(x["clicks_unique"]),
                             "conversion_uniques": int(x["conversion_uniques"]), "conversions": int(x["conversions"]),
                             "revenue": round(x["conversion_value"], 2),
                             "rpr": round(x["conversion_value"] / n, 4) if n else "",
                             "conv_rate": round(min(1, x["conversion_uniques"] / n), 5) if n else "",
                             "click_rate": round(x["clicks_unique"] / n, 5) if n else "",
                             "unsub_rate": round(x["unsubscribe_uniques"] / n, 5) if n else "",
                             "spam_rate": round(x["spam_complaints"] / n, 6) if n else "",
                             "cohort_n": int(x.get("cohort_n", 0)) if COHORT else "",
                             "cohort_buyers": x.get("cohort_buyers", "") if COHORT else "",
                             "cohort_rev": round(x.get("cohort_rev", 0), 2) if COHORT else ""})
            if st.get("main_msgs"):
                mn = total(st["main_msgs"], mask)["delivered"]
                if mn > 0:
                    md.append(f"| {st['key']} | hoofdbericht | {st['main_msgs'][0]['name']} | {int(mn)} | | | | | | | | |")
                    summary.append((test["id"], st["key"], "LET OP",
                                    f"{int(mn)} verzendingen op het hoofdbericht zonder variant: A/B-test niet gestart?"))
            if a["n"] > 0 and b["n"] > 0:
                da, db = draws_for(a, fallback_aov), draws_for(b, fallback_aov)
                w = a["n"] + b["n"]
                weights.append(w)
                per_stratum.append((st["key"], da, db, a, b))
                for arm, d in (("a", da), ("b", db)):
                    if pooled_d[arm] is None:
                        pooled_d[arm] = {k: v * w for k, v in d.items()}
                    else:
                        pooled_d[arm] = {k: pooled_d[arm][k] + d[k] * w for k in pooled_d[arm] if k in d}
        md.append("")
        # kansen per stratum en gepoold
        md.append("| Stratum | P(B>A) RPR | Lift RPR (90%) | P(B>A) conv. | P(B>A) cohort | P(B>A) klik | P(B>A) uitschr. | SRM p | Advies | Toelichting |")
        md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
        evals = [(k, da, db, a, b) for k, da, db, a, b in per_stratum]
        if test["id"] == "T02" and len(per_stratum) > 1:
            W = sum(weights)
            pa = {k: v / W for k, v in pooled_d["a"].items()}
            pb = {k: v / W for k, v in pooled_d["b"].items()}
            evals.append(("gepoold", pa, pb, pool_n["a"], pool_n["b"]))
        for key, da, db, a, b in evals:
            s = summarize(da, db)
            if test["rule"] == "code":
                s["p_breakeven"] = float(np.mean(da["conv"] / np.maximum(db["conv"], 1e-12) - 1 > BREAKEVEN))
            planned = PLANNED_N.get(f"{test['id']}/{key}", PLANNED_N.get(test["id"]))
            if test["id"] == "T02" and key != "gepoold" and len(per_stratum) > 1:
                planned = None
            weekly_b = min(a["n"], b["n"]) / max(days_run / 7, 1e-9)
            status, why = verdict(test, s, a, b, days_run, planned, weekly_b)
            if test["id"] == "T02" and key != "gepoold" and len(per_stratum) > 1:
                status, why = "(stratum)", "Beslissing op de gepoolde regel; per stratum alleen bij eigen 80%-bewijs."
            g = lambda k, f="p_b": s.get(k, {}).get(f)
            lift = s.get("rpr", {})
            md.append(f"| {key} | {fmt_pct(g('rpr'), 0)} | "
                      f"{'' if not lift else f'{lift['lift']:+.0%} ({lift['lo']:+.0%} tot {lift['hi']:+.0%})'} | "
                      f"{fmt_pct(g('conv'), 0)} | {fmt_pct(g('cohort'), 0) if 'cohort' in s else ''} | "
                      f"{fmt_pct(g('click'), 0)} | {fmt_pct(g('unsub'), 0)} | "
                      f"{'' if srm_p(a['n'], b['n']) is None else f'{srm_p(a['n'], b['n']):.3f}'} | **{status}** | {why} |")
            if key == "gepoold" or len(evals) == 1 or test["id"] != "T02":
                if not (test["id"] == "T02" and key != "gepoold" and len(per_stratum) > 1):
                    summary.append((test["id"], key, status, why))
            for r in rows:
                if r["test_id"] == test["id"] and r["stratum"] == key:
                    r.update({"prob_b_better_rpr": round(g("rpr") or 0, 4), "prob_b_better_conv": round(g("conv") or 0, 4),
                              "prob_b_better_click": round(g("click") or 0, 4),
                              "prob_b_better_cohort": round(g("cohort") or 0, 4) if "cohort" in s else "",
                              "lift_rpr": round(lift.get("lift", 0), 4), "lift_rpr_lo90": round(lift.get("lo", 0), 4),
                              "lift_rpr_hi90": round(lift.get("hi", 0), 4),
                              "p_breakeven": round(s.get("p_breakeven", 0), 4) if "p_breakeven" in s else "",
                              "srm_p": round(srm_p(a["n"], b["n"]) or 0, 4), "planned_n_per_arm": planned or "",
                              "status": status, "advice": why})
            if key == "gepoold":
                rows.append({"date": stamp, "mode": "dryrun" if DRY else "live", "test_id": test["id"],
                             "stratum": "gepoold", "arm": "A-B", "n": f"{int(a['n'])}/{int(b['n'])}",
                             "prob_b_better_rpr": round(g("rpr") or 0, 4), "prob_b_better_conv": round(g("conv") or 0, 4),
                             "p_breakeven": round(s.get("p_breakeven", 0), 4), "status": status, "advice": why})
        md.append("")
    fz = total(msgs, fmask)
    if fz["delivered"]:
        md.append(f"## BFCM-bevriezing (apart, telt niet mee)\n\nDelivered {int(fz['delivered'])}, omzet ${fz['conversion_value']:,.0f}.\n")
    md.insert(4, "## Samenvatting\n\n| Test | Stratum | Advies | Toelichting |\n| --- | --- | --- | --- |\n" +
              "\n".join(f"| {a} | {b} | **{c}** | {d} |" for a, b, c, d in summary) + "\n")
    os.makedirs(OUT, exist_ok=True)
    base = os.path.join(OUT, f"results-{stamp}{'-dryrun' if DRY else ''}")
    open(base + ".md", "w").write("\n".join(md) + "\n")
    cols = []
    for r in rows:
        for k in r:
            if k not in cols:
                cols.append(k)
    with open(base + ".csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(f"Geschreven: {base}.md en .csv ({len(rows)} regels)")
    for s in summary:
        print("  ", " | ".join(s))


# ---------------------------------------------------------------- plan: steekproef en looptijd
def n_per_arm(p1, mde, z_a=1.96, z_b=0.84):
    p2 = p1 * (1 + mde)
    pb = (p1 + p2) / 2
    return math.ceil((z_a * math.sqrt(2 * pb * (1 - pb)) + z_b * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
                     / (p2 - p1) ** 2)


def run_plan():
    end = TODAY - dt.timedelta(days=TODAY.weekday())       # laatste maandag
    start = end - dt.timedelta(weeks=8)
    flows = DRY_FLOWS + ["UEfh4h", "RL3TU6"]
    print(f"plan: flow-series-report {start} tot {end}", file=sys.stderr)
    days, msgs = series(flows, start, end)
    mask = [True] * len(days)
    wk = 8.0

    def sel(flow, pat):
        return [m for m in msgs if m["flow_id"] == flow and re.search(pat, m["name"])]

    def agg(ms):
        return total(ms, mask)
    units = {
        "welcome": (sel("SiaNLu", r"Email #1"), sel("SiaNLu", r".")),
        "checkout": (sel("Y2TmNB", r"^(Copy of )?Email #1$|^New AB Checkout 1$") + sel("Tsg2tV", r"Email #1$"),
                     sel("Y2TmNB", r".") + sel("Tsg2tV", r".")),
        "cart": (sel("SwkMyn", r"Email #1$") + sel("TBWngE", r"Email #1$"), sel("SwkMyn", r".") + sel("TBWngE", r".")),
        "browse": (sel("TyEjuQ", r".") + sel("Wj6x6V", r"."), sel("TyEjuQ", r".") + sel("Wj6x6V", r".")),
    }
    lines = [f"# Plan: volumes, steekproef en looptijd v4-tests · {TODAY}\n",
             f"Gegenereerd door `scripts/test_report.py --plan`. Bron: Klaviyo flow-series-report, oude flows, "
             f"8 volle weken {start} tot {end} (UTC), conversion metric Placed Order RSNxYV. "
             f"n per arm: twee proporties, alpha 5% tweezijdig, power 80%, 50/50. RPR-n = conversie-n x "
             f"(1 + CV²) = x {1 + CV_ORDER ** 2:.2f} (CV orderwaarde {CV_ORDER}). Weken = n per arm / instroom per arm per week.\n",
             "## Volumes oude flows (per week, gemiddeld over 8 weken)\n",
             "| Eenheid | Instromers/wk | Mails/wk | Conversie per instromer (attr.) | Omzet per instromer | Klik eerste mail |",
             "| --- | --- | --- | --- | --- | --- |"]
    base = {}
    for k, (entry, path) in units.items():
        e, p = agg(entry), agg(path)
        ent = e["delivered"] / wk
        conv = min(1, p["conversion_uniques"] / e["delivered"]) if e["delivered"] else 0
        base[k] = {"ent": ent, "conv": conv, "rpe": p["conversion_value"] / e["delivered"],
                   "click": e["clicks_unique"] / e["delivered"]}
        lines.append(f"| {k} | {ent:,.0f} | {p['delivered'] / wk:,.0f} | {conv:.2%} | ${base[k]['rpe']:.2f} | {base[k]['click']:.2%} |")
    # T02-strata (laatste mails oud als schatting)
    t02 = {"checkout C4": sel("Y2TmNB", r"^Email #4$|^New AB Checkout 5$") + sel("Tsg2tV", r"^Email #4$"),
           "cart K3": sel("SwkMyn", r"Email #3$") + sel("TBWngE", r"Email #3$"),
           "winback R2": sel("UEfh4h", r"Email #2$"),
           "post-purchase P3": sel("RL3TU6", r"100 Day-Trial")}
    lines += ["", "T02-strata (oude laatste mails als schatting; B2-clicked = unieke klikkers op de oude browsemail):", "",
              "| Stratum | Ontvangers/wk (oud) | Conversie | In T02 per arm/wk |", "| --- | --- | --- | --- |"]
    t02_arm, t02_conv_num = 0.0, 0.0
    for k, ms in t02.items():
        t = agg(ms)
        r = t["delivered"] / wk
        share = 0.5 if k.split()[0] in ("checkout", "cart") else 1.0   # alleen in de v4-arm van T01
        per_arm = r * share * 0.5
        t02_arm += per_arm
        t02_conv_num += per_arm * (t["conversion_uniques"] / t["delivered"] if t["delivered"] else 0)
        lines.append(f"| {k} | {r:,.0f} | {t['conversion_uniques'] / max(t['delivered'], 1):.2%} | {per_arm:,.0f} |")
    b2 = base["browse"]["click"] * base["browse"]["ent"] * 0.5 * 0.85 * 0.5
    t02_arm += b2
    t02_conv_num += b2 * 0.008
    lines.append(f"| browse B2-clicked | {base['browse']['click'] * base['browse']['ent']:,.0f} (klikkers) | ~0,80% (aanname) | {b2:,.0f} |")
    t02_conv = t02_conv_num / t02_arm
    lines.append(f"\nT02 gepoold: ~{t02_arm:,.0f} per arm per week, conversie ~{t02_conv:.2%}. Cooldown (code in de laatste "
                 f"30 dagen) gaat buiten T02 om en verlaagt dit nog; na week 2 opnieuw rekenen.\n")
    # tests
    tests = [
        ("T01 welcome", base["welcome"]["ent"] / 2, base["welcome"]["conv"], "conversie per instromer (14 d)", 0.30),
        ("T01 browse", base["browse"]["ent"] / 2, base["browse"]["conv"], "conversie per instromer (7 d)", 0.30),
        ("T01 checkout", base["checkout"]["ent"] / 2, base["checkout"]["conv"], "conversie per instromer (7 d)", 0.50),
        ("T01 cart", base["cart"]["ent"] / 2, base["cart"]["conv"], "conversie per instromer (7 d)", 0.50),
        ("T02 gepoold", t02_arm, t02_conv, "conversie per ontvanger (7 d)", 0.50),
        ("T04 W1", base["welcome"]["ent"] * 0.5 * 0.95 * 0.5, 0.0071, "conversie W1 (14 d)", 0.50),
        ("T05a B1 (klik)", base["browse"]["ent"] * 0.5 * 0.85 * 0.5, base["browse"]["click"], "unieke klik B1", 0.20),
        ("T05a B1 (conv.)", base["browse"]["ent"] * 0.5 * 0.85 * 0.5, base["browse"]["conv"], "conversie B1 (7 d)", 0.30),
    ]
    lines += ["## Steekproef en looptijd per test\n",
              "Per arm per week = instroom in die arm. T04 en T05a lopen alleen in de v4-arm van T01 (50%), "
              "T05a alleen bij kookgerei (aanname 85% van de browse-instroom), W1 niet bij bestaande klanten "
              "(aanname 5%). Weken tot 19 november vanaf 8 oktober: 6.\n",
              "| Test | Per arm/wk | Basis | Metric | n/arm +20% | +30% | +50% | Weken bij gekozen MDE (conv. / RPR) | Gekozen MDE | Haalbaar voor 19 nov? |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for name, per_arm, p1, metric, mde in tests:
        ns = {m: n_per_arm(p1, m) for m in (0.2, 0.3, 0.5)}
        n_conv = ns[mde]
        wk_conv, wk_rpr = n_conv / per_arm, n_conv * (1 + CV_ORDER ** 2) / per_arm
        ok = "ja" if wk_conv <= 6 else ("alleen conv." if wk_conv <= 6 < wk_rpr else "nee")
        if "klik" in metric:
            wk_rpr = float("nan")
            ok = "ja" if wk_conv <= 6 else "nee"
        lines.append(f"| {name} | {per_arm:,.0f} | {p1:.2%} | {metric} | {ns[0.2]:,} | {ns[0.3]:,} | {ns[0.5]:,} | "
                     f"{wk_conv:.1f} / {'-' if math.isnan(wk_rpr) else f'{wk_rpr:.1f}'} | +{mde:.0%} | {ok} |")
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"plan-{TODAY}.md")
    open(path, "w").write("\n".join(lines) + "\n")
    print(f"Geschreven: {path}")
    print("\n".join(lines[-len(tests) - 1:]))


if __name__ == "__main__":
    if PLAN:
        run_plan()
    else:
        run_report()
