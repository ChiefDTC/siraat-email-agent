#!/usr/bin/env python3
"""Bouwt alle v4-flows (plan klaviyo/flows/v4-flow-system.md, hoofdstuk 2) als Klaviyo-flowdefinities.

Draaien (vanuit /tmp, met `python3 -I`):

  python3 -I /home/user/siraat-email-agent/scripts/build_flows.py
      Dry-run voor alle flows. Leest (alleen GET) de oude flows voor de T01-paden en controleert
      metrics, lijst, segmenten, coupons en templates. Schrijft exports/live/flows/<slug>.json en
      exports/live/flows/OVERZICHT.md. Ontbrekende templates en flow-ID's worden placeholders.

  python3 -I .../build_flows.py --live --only=<slug>
      Maakt één flow aan via POST /api/flows (Klaviyo maakt hem als Draft, alle mails status draft).
      Weigert als: een template ontbreekt, een flow waar deze flow naar verwijst nog geen ID heeft
      in exports/live/flows.csv, het sunset-segment ontbreekt, of de flownaam al bestaat.
      Logt "naam,id" in exports/live/flows.csv. Volgorde: zie --order.

  --order              toon de bouwvolgorde (afhankelijkheden via "Received Email where $flow = ...").
  --w4=split|template  Welcome W4: landsplit met w4-us/w4-int (standaard) of één template `w4`.
  --ab=action|split    A/B-tests (T04 W1, T05a B1) als Klaviyo ab-test-actie (standaard, zelfde vorm als
                       XzHrez) of als 50/50 random-split met gedupliceerd vervolg (terugval).
  --t02-new            ook V1 en N2 in T02 (na de eerste 4 weken). Standaard 100% code bij geen cooldown.
  --max-delay=N        lange wachttijden (anniversary 182/183 dagen) opknippen in stukken van max N dagen.
  --offline            geen API-calls; gebruikt de cache in exports/live/flows/_bron/ (sunset-segment: bekend ID WuHSm6).
  --vip-cooldown=codes|discounts|none|old
                       VIP V1 (besluit 8 okt): cooldown alleen als er ook een order MET code was (standaard `codes`:
                       Placed Order waarvan "Discount Codes" niet leeg is). `discounts`: Total Discounts > 0.
                       `none`: altijd V1 (15%). `old`: oude cooldown (alleen Received CODE-mail in 30 dagen).

Lessen uit de checkout-bouw (Bouwnotitie 2.1): geen samenkomende takken (strikt een boom), categorie
als verzendfilter op de mail, geen update-profile (cooldown via berichtnaam "CODE · ..."), geen
existence/is-not-set-filters, `not-equals` sluit profielen zonder waarde uit.
"""
import csv, json, os, re, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "exports/live/flows")
CACHE = os.path.join(OUT_DIR, "_bron")
REV = "2025-10-15"
ARGS = sys.argv[1:]
LIVE = "--live" in ARGS
OFFLINE = "--offline" in ARGS


def opt(name, default=None):
    for a in ARGS:
        if a.startswith(f"--{name}="):
            return a.split("=", 1)[1]
    return default


W4_MODE = opt("w4", "split")
AB_MODE = opt("ab", "action")
T02_NEW = "--t02-new" in ARGS
MAX_DELAY = int(opt("max-delay", "0") or 0)
VIP_COOLDOWN = opt("vip-cooldown", "codes")  # codes | discounts | none | old (zie build_vip)
ONLY = opt("only")

# ---------------------------------------------------------------- ID's (plan 1.1)
CHECKOUT_STARTED, ADDED_TO_CART, VIEWED_PRODUCT = "RfMvni", "QXcV8K", "XNtYMB"
PLACED_ORDER, DELIVERED, ACTIVE_ON_SITE = "RSNxYV", "VcUF33", "UdCdLD"
RECEIVED_EMAIL, CLICKED_EMAIL, OPENED_EMAIL = "YkRM4Q", "W247h8", "WyrTym"
REFUNDED, OPENED_TICKET, FULFILLED = "Xg6cwn", "YzvjGf", "VtEiZT"
WELCOME_LIST = "Uw8eZG"
SUNSET_SEGMENT = "v4 · Sunset · unengaged 120d"
KNOWN_SEGMENT_IDS = {SUNSET_SEGMENT: "WuHSm6"}  # terugval voor --offline (aangemaakt 8 okt, LOG)
OLD_POSTPURCHASE = "RL3TU6"
OBSOLETE_FLOW_IDS = {"Y6yj2z"}  # eerste checkout-draft (landsplit), wordt vervangen; nooit naar verwijzen

METRICS = {
    CHECKOUT_STARTED: "Checkout Started", ADDED_TO_CART: "Added to Cart", VIEWED_PRODUCT: "Viewed Product",
    PLACED_ORDER: "Placed Order", DELIVERED: "Delivered Shipment", ACTIVE_ON_SITE: "Active on Site",
    RECEIVED_EMAIL: "Received Email", CLICKED_EMAIL: "Clicked Email", OPENED_EMAIL: "Opened Email",
    REFUNDED: "Refunded Order", OPENED_TICKET: "Opened Ticket", FULFILLED: "Fulfilled Order",
    "RtgBgs": "Checkout Started (Triple Pixel)",
}

FROM_EMAIL = "send@siraatskitchen.com"
FROM_LABEL = "Siraat's Kitchen"
FROM_BENJAMIN = "Benjamin at Siraat's Kitchen"
REPLY_TO = "support@siraatskitchen.com"
CODE = "CODE ·"  # cooldown-terugval plan 1.4: alle codemails heten "CODE · ..."

# ---------------------------------------------------------------- producttitels (plan 1.7)
# Exacte Shopify-producttitels (Admin API products, alle statussen incl. UNLISTED/ARCHIVED, opgehaald 8 okt 2026;
# lijst in content/facts/shopify-titles.csv). Items in Checkout Started en Placed Order = deze producttitels.
# Audit 01 S2: schorten heten "(Azure)", niet " - Azure"; BDAY-, SB- en FREE PIZZA STEEL-listings ontbraken.
PANPRO_TITELS = [
    "Titanium Hammered Pan Pro Standard", "Titanium Hammered Pan Pro Large", "Titanium Hammered Pan Pro Small",
    "Titanium Hammered Pan Pro Mini", "Titanium Pan Pro", "Titanium Hammered Pan Pro With Lid",
    "Titanium Hammered Pan Pro Small (BDAY SALE)", "Titanium Hammered Pan Pro Standard (BDAY SALE)",
    "Titanium Hammered Pan Pro Large (BDAY SALE)", "Titanium Hammered Pan Pro - Reader Exclusive Deal",
    "Titanium Hammered Pan Pro", "Titanium Hammered Pan", "Titanium Hammered Pan Pro Standrd",
    "Titanium Hammered Pan Pro-Standard", "Titanium Hammered Pan Pro-Large", "Titanium Hammered Pan Pro-Small",
    "Titanium Hammered Pan Pro Mini With Lid", "Titanium Hammered Pan Pro Small With Lid",
    "Titanium Hammered Pan Pro Standard With Lid", "Titanium Hammered Pan Pro Large With Lid",
    "Holiday Sale Exclusive | Titanium Hammered Pan Pro", 'Titanium Hammered Frying Pan, 11"',
]
VORM_TITELS = ["Titanium Hammered Deep Pan Pro", "Titanium Hammered Wok Pan Pro", "Titanium Hammered Crêpe Pan Pro",
               "Titanium Hammered Wok Pan Pro Medium", "Titanium Hammered Deep Pan Pro Mini"]
POT_TITELS = ["2 Litre Titanium Hammered Pot With Lid", "3 Litre Titanium Hammered Pot With Lid",
              "7,5 Litre Titanium Hammered Pot With Lid", "Titanium Hammered Pot Set With Lids | 6-Pcs"]
KOOK_TITELS = PANPRO_TITELS + VORM_TITELS + POT_TITELS + [
    "Titanium Hammered Pizza Steel", "Titanium Hammered Roasting Pan",
    "Titanium Hammered Pan Pro & Utensil Set", "Titanium Cook & Prep Bundle",
]
SET_TITELS = [
    "Titanium Hammered Pan Set With Lids | 6-Pcs", "Titanium Hammered Pan Set With Lids | 6-Pcs (BDAY SALE)",
    "Titanium Hammered Pan Set With Lids | 6-Pcs SB", "Titanium Hammered Cookware Set | 12-Pcs",
    "Titanium Hammered Cookware Set | 12-Pcs | + FREE PIZZA STEEL", "Titanium Hammered Cookware Set | 12-Pcs | + FREE PIZZA STEEL (EXCLUSIVE)",
    "Titanium Hammered Cookware Set Pro", "Titanium Hammered Complete Edition", "Titanium Hammered – Complete Edition",
    "Full Hammered Pro Edition", "The Just Everything Bundle | 34-Pcs", "2 Pans + 2 Lids",
    "Titanium Hammered Pan Pro Duo", "Titanium Hammered Pro Duo", "Titanium Hammered Pan Pro Kit",
    "Titanium Hammered Wok & Deep Pan Pro", "Titanium Hammered Wok & Deep Pan Set",
    "12 pcs cookware set", "Titanium-Hammerpfannenset mit Deckel | 6-teilig",
]
# v5 (8 okt, research/v5/02 1.3): starterbundels gaan in checkout naar C3-P (upgrade naar de $299-set), niet naar C3-S.
STARTER_TITELS = ["Titanium Hammered Pan Pro Duo", "Titanium Hammered Pro Duo", "Titanium Hammered Pan Pro Kit", "2 Pans + 2 Lids"]
GROOT_SET_TITELS = [t for t in SET_TITELS if t not in STARTER_TITELS]
DEKSEL_TITELS = ["Stainless Steel Lid", "Stainless Steel Lid (S)", "Titanium Hammered Pan Pro With Lid",
                 "Titanium Hammered Pan Pro Mini With Lid", "Titanium Hammered Pan Pro Small With Lid",
                 "Titanium Hammered Pan Pro Standard With Lid", "Titanium Hammered Pan Pro Large With Lid"]
# P2 (eerste ei, voorverwarmen) alleen voor pannen en sets: niet voor wie alleen een pizza steel, roasting pan of pot kocht (productmatrix 8 okt).
P2_TITELS = PANPRO_TITELS + VORM_TITELS + SET_TITELS + ["Titanium Hammered Pan Pro & Utensil Set", "Titanium Cook & Prep Bundle"]
SCHORT_TITELS = ["Siraat Signature Apron (Azure)", "Siraat Signature Apron (Moss)",
                 "Siraat Signature Apron (Ember)", "Siraat Signature Apron (Oak)"]
EGIFT_TITELS = ["E-Gift Card"]
KOOK_WOORDEN = ["Hammer", "Pan", "Pot", "ookware", "Everything", "fanne", "Prep Bundle"]
KOOK = KOOK_TITELS + SET_TITELS
BACKORDER_FALLBACK = ["Titanium Hammered Cookware Set | 12-Pcs",
                      "Titanium Hammered Cookware Set | 12-Pcs | + FREE PIZZA STEEL",
                      "Titanium Hammered Cookware Set | 12-Pcs | + FREE PIZZA STEEL (EXCLUSIVE)"]
TITLE_SETS = {tuple(KOOK): "KOOK_TITELS+SET_TITELS", tuple(SET_TITELS): "SET_TITELS",
              tuple(PANPRO_TITELS + VORM_TITELS): "PANPRO+VORM_TITELS", tuple(PANPRO_TITELS): "PANPRO_TITELS",
              tuple(DEKSEL_TITELS): "DEKSEL_TITELS", tuple(GROOT_SET_TITELS): "GROOT_SET_TITELS (sets zonder starterbundels)",
              tuple(PANPRO_TITELS + STARTER_TITELS): "PANPRO_TITELS+STARTER_TITELS", tuple(SCHORT_TITELS): "SCHORT_TITELS",
              tuple(EGIFT_TITELS): "E-Gift Card", tuple(P2_TITELS): "P2_TITELS", tuple(BACKORDER_FALLBACK): "12-pcs (backorder)"}


# ---------------------------------------------------------------- API (alleen GET, behalve POST bij --live)
def api(method, path, body=None):
    url = path if path.startswith("http") else f"https://a.klaviyo.com/api/{path}"
    cmd = ["curl", "-sS", "-g", "-X", method, url, "-H", f"revision: {REV}",
           "-H", "accept: application/vnd.api+json", "-H", "content-type: application/vnd.api+json"]
    if body is not None:
        cmd += ["--data-binary", "@-"]
    out = subprocess.run(cmd, input=json.dumps(body) if body is not None else None, capture_output=True, text=True)
    try:
        return json.loads(out.stdout or "{}")
    except json.JSONDecodeError:
        return {"errors": [{"detail": (out.stdout or out.stderr)[:300]}]}


def get_all(path):
    rows, url = [], path
    for _ in range(60):
        d = api("GET", url)
        if "errors" in d:
            return rows, d["errors"]
        rows += d.get("data", [])
        url = (d.get("links") or {}).get("next")
        if not url:
            break
    return rows, None


def get_flow(fid):
    """Bestaande flow met definitie (GET), met cache voor --offline."""
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, f"flow-{fid}.json")
    if not OFFLINE:
        d = api("GET", f"flows/{fid}?additional-fields[flow]=definition")
        if "data" in d:
            with open(p, "w") as fh:
                json.dump(d, fh, ensure_ascii=False)
            return d["data"]["attributes"]
    if os.path.exists(p):
        return json.load(open(p))["data"]["attributes"]
    sys.exit(f"Flow {fid} niet op te halen en geen cache in {p}")


# ---------------------------------------------------------------- bronnen in de repo
def load_templates():
    t = {}
    p = os.path.join(ROOT, "exports/live/templates.csv")
    if os.path.exists(p):
        for row in csv.reader(open(p)):
            if len(row) >= 3:
                t[row[1].strip()] = row[2].strip()  # laatste regel wint
    return t


def load_manifest():
    return {r["id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "exports/manifest.csv")))}


def load_flows_csv():
    m = {}
    p = os.path.join(ROOT, "exports/live/flows.csv")
    if os.path.exists(p):
        for row in csv.reader(open(p)):
            if len(row) >= 2 and row[1].strip() not in OBSOLETE_FLOW_IDS:
                m[row[0].strip()] = row[1].strip()
    return m


UNIT_NL = {"minutes": "minuten", "hours": "uur", "days": "dagen"}
SUBJECT_FALLBACK = {"c4": "c4-us", "c4-nocode": "c4-us-nocode", "w4": "w4-us"}

FLOWMAP = {"checkout": "checkout", "cart": "cart", "browse": "browse", "welcome": "welcome",
           "postpurchase": "post-purchase", "levering": "post-purchase", "winback": "winback", "site": "site",
           "sunset": "sunset", "vip": "vip", "anniversary": "anniversary", "ugc": "ugc", "sunsetkept": "sunset"}


def topcomment(folder, mid):
    """SUBJECT_A en PREVIEW uit de topcomment van de bron-HTML (als de manifestregel ontbreekt)."""
    p = os.path.join(ROOT, "klaviyo/templates/v3", folder, f"{mid}.html")
    if not os.path.exists(p):
        return None
    head = open(p, encoding="utf-8").read(6000)
    m = re.search(r"<!--(.*?)-->", head, re.S)
    if not m:
        return None
    parts = {}
    for seg in m.group(1).split(" | "):
        if ":" in seg:
            k, v = seg.split(":", 1)
            parts[k.strip()] = v.strip()
    return {"onderwerp_a": parts.get("SUBJECT_A", ""), "onderwerp_b": parts.get("SUBJECT_B", ""),
            "preview": parts.get("PREVIEW", "")}


# ---------------------------------------------------------------- condities
FLOW_START = {"type": "date", "operator": "flow-start"}
ALLTIME = {"type": "date", "operator": "alltime"}


def last_days(n):
    return {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": n}


def mc(metric, op, value, tf, filters=None):
    return {"type": "profile-metric", "metric_id": metric, "measurement": "count",
            "measurement_filter": {"type": "numeric", "operator": op, "value": value},
            "timeframe_filter": tf, "metric_filters": filters}


def zero(metric, tf, filters=None):
    return mc(metric, "equals", 0, tf, filters)


def some(metric, tf, filters=None):
    return mc(metric, "greater-than", 0, tf, filters)


def f_items(titles):
    return [{"property": "Items", "filter": {"type": "list", "operator": "contains-any", "value": list(titles)}}]


def f_value(op, v):
    return [{"property": "$value", "filter": {"type": "numeric", "operator": op, "value": v}}]


def f_str(prop, op, v):
    return [{"property": prop, "filter": {"type": "string", "operator": op, "value": v}}]


def not_in_flow(tf):
    return {"type": "profile-not-in-flow", "timeframe_filter": tf}


def sample(pct):
    return {"type": "profile-sample", "percentage": pct}


def groups(*gs):
    """Groepen zijn EN, condities binnen een groep zijn OF."""
    return {"condition_groups": [{"conditions": list(g)} for g in gs]}


NO_ORDER_SINCE_START = zero(PLACED_ORDER, FLOW_START)
HEEFT_GEKOCHT = some(PLACED_ORDER, ALLTIME)
NIEUWE_KLANT = zero(PLACED_ORDER, ALLTIME)
NOT_BOT = [{"property": "Bot Click", "filter": {"type": "boolean", "operator": "equals", "value": False}}]
COOLDOWN = some(RECEIVED_EMAIL, last_days(30), f_str("Campaign Name", "contains", CODE))
COUNTRY_US_ANY = [  # "US" en "United States" komen allebei voor (country-split-review)
    {"type": "profile-property", "property": "location['country']",
     "filter": {"type": "string", "operator": "equals", "value": "United States"}},
    {"type": "profile-property", "property": "location['country']",
     "filter": {"type": "string", "operator": "equals", "value": "US"}},
]


# ---------------------------------------------------------------- flowbouwer
class Ctx:
    """Gedeelde bronnen en registratie van wat elke flow nodig heeft."""

    def __init__(self):
        self.templates = load_templates()
        self.manifest = load_manifest()
        self.flow_ids = load_flows_csv()
        self.segment_ids = {}


class Flow:
    def __init__(self, ctx, slug, name, utm):
        self.ctx, self.slug, self.name, self.utm = ctx, slug, name, utm
        self.actions, self.n = [], 0
        self.missing_templates, self.deps, self.notes, self.warnings = set(), set(), [], []
        self.base_filters = []  # groepen die op elke v4-mail komen

    # -- referenties
    def tpl(self, mid):
        r = self.ctx.manifest.get(mid)
        folder = FLOWMAP[self.slug]
        tname = r["templatenaam"] if r else f"v4 · {self.name[5:]} · {mid}"
        tid = self.ctx.templates.get(tname)
        if not tid:
            self.missing_templates.add(tname)
            tid = f"TPL?{tname}"
        info = r or topcomment(folder, mid) or {}
        subj, prev = info.get("onderwerp_a", ""), info.get("preview", "")
        if not r:
            src = "onderwerp/preview uit de topcomment van de bron-HTML"
            if not subj and mid in SUBJECT_FALLBACK:  # samengevoegde template nog niet gebouwd
                info = self.ctx.manifest.get(SUBJECT_FALLBACK[mid], {})
                subj, prev = info.get("onderwerp_a", ""), info.get("preview", "")
                src = f"nog geen bron-HTML: onderwerp/preview voorlopig van {SUBJECT_FALLBACK[mid]}, opnieuw draaien zodra {mid}.html er is"
            self.warnings.append(f"{mid}: geen manifestregel, {src}")
        return tid, subj, prev, (info.get("onderwerp_b") or "")

    def flow_ref(self, slug, fallback=None):
        """ID van een andere v4-flow (uit flows.csv). Placeholder in de dry-run."""
        self.deps.add(slug)
        name = FLOW_NAMES[slug]
        fid = self.ctx.flow_ids.get(name)
        if fid:
            return fid
        if fallback and LIVE:
            self.warnings.append(f"{name} heeft nog geen ID: terugval op {fallback}")
            return fallback
        return f"FLOW?{slug}" + (f"|{fallback}" if fallback else "")

    def received_from(self, slug, op_zero=True, days=7, extra=None, fallback=None):
        filt = f_str("$flow", "equals", self.flow_ref(slug, fallback)) + (extra or [])
        return (zero if op_zero else some)(RECEIVED_EMAIL, last_days(days), filt)

    # -- acties
    def add(self, type_, data, links):
        self.n += 1
        aid = f"a{self.n:03d}"
        self.actions.append({"temporary_id": aid, "type": type_, "data": data, "links": links})
        return aid

    def delay(self, unit, value, until=None, nxt=None):
        if unit == "days" and MAX_DELAY and value > MAX_DELAY:  # opknippen (anniversary)
            rest = value - MAX_DELAY
            nxt = self.delay("days", rest, until, nxt)
            return self.delay("days", MAX_DELAY, None, nxt)
        d = {"unit": unit, "value": value, "secondary_value": None, "timezone": "profile"}
        if until:
            d["delay_until_time"] = until
        return self.add("time-delay", d, {"next": nxt})

    def message(self, name, template_id, subject, preview, utm=None, filter_groups=(), label=None, base=True,
                reply_to=REPLY_TO):
        gs = (list(self.base_filters) if base else []) + [list(g) for g in filter_groups]
        return {"from_email": FROM_EMAIL, "from_label": label or FROM_LABEL, "reply_to_email": reply_to,
                "cc_email": None, "bcc_email": None, "subject_line": subject, "preview_text": preview,
                "template_id": template_id, "smart_sending_enabled": False, "transactional": False,
                "add_tracking_params": True,
                "custom_tracking_params": [{"param": "utm_source", "value": "klaviyo"},
                                           {"param": "utm_medium", "value": "email"},
                                           {"param": "utm_campaign", "value": utm or self.utm}],
                "additional_filters": {"condition_groups": [{"conditions": g} for g in gs]} if gs else None,
                "name": name}

    def mail(self, mid, name, nxt=None, filter_groups=(), label=None, base=True, subject=None):
        tid, subj, prev, _ = self.tpl(mid)
        msg = self.message(name, tid, subject or subj, prev, filter_groups=filter_groups, label=label, base=base)
        return self.add("send-email", {"message": msg, "status": "draft"}, {"next": nxt})

    def raw_mail(self, msg, nxt=None):
        return self.add("send-email", {"message": msg, "status": "draft"}, {"next": nxt})

    def cs(self, filt, yes=None, no=None):
        return self.add("conditional-split", {"profile_filter": filt}, {"next_if_true": yes, "next_if_false": no})

    def ab(self, exp_name, variants, nxt_factory, winner="unique-clicks"):
        """A/B-test (plan 1.6, geen automatische winnaar). variants: lijst (naam, mid, onderwerp, opties).
        action: Klaviyo ab-test-actie (vorm van XzHrez / klaviyo/flows/review-request-flow.json).
        split : 50/50 random split met per tak een eigen kopie van het vervolg (geen samenkomende takken)."""
        if AB_MODE == "split":
            ids = []
            for vname, mid, subj, kw in variants:
                ids.append(self.mail(mid, vname, nxt_factory(), subject=subj, **kw))
            return self.cs(groups([sample(50)]), yes=ids[0], no=ids[1])
        nxt = nxt_factory()
        msgs = []
        for vname, mid, subj, kw in variants:
            tid, s, prev, _ = self.tpl(mid)
            fg = kw.get("filter_groups", ())
            msgs.append(self.message(vname, tid, subj or s, prev, filter_groups=fg, label=kw.get("label")))
        self.n += 1
        aid = f"a{self.n:03d}"
        var_ids = [f"{aid}v{i}" for i in range(len(msgs))]
        main = dict(msgs[0], name=msgs[0]["name"].rsplit(" · ", 1)[0])
        data = {
            "main_action": {"temporary_id": f"{aid}m", "type": "send-email",
                            "data": {"message": main, "status": "draft"}, "links": {"next": None}},
            "current_experiment": {
                "name": exp_name,
                "variations": [{"temporary_id": vid, "type": "send-email",
                                "data": {"message": m, "status": "draft"}, "links": {"next": None}}
                               for vid, m in zip(var_ids, msgs)],
                "allocations": {vid: round(1 / len(msgs), 4) for vid in var_ids},
                "winner_metric": winner,
                "automatic_winner_selection_settings": {"enabled": False, "automatic_end_date": None,
                                                        "automatic_end_statistical_certainty": False},
            },
        }
        self.actions.append({"temporary_id": aid, "type": "ab-test", "data": data, "links": {"next": nxt}})
        return aid

    def router(self, code_mid, nocode_mid, label, filter_groups=(), nxt_factory=lambda: None, t02=True, cooldown=None, **kw):
        """Code-router (plan 1.4, vereenvoudigd volgens country-split-review): cooldown-split, dan T02 50/50.
        Codemail heet "CODE · <label>". Elke tak krijgt een eigen kopie van het vervolg."""
        code = self.mail(code_mid, f"{CODE} {label}", nxt_factory(), filter_groups, **kw)
        if cooldown is False:  # geen cooldown-tak (VIP --vip-cooldown=none)
            if t02:
                b = self.mail(nocode_mid, f"{label} nocode · T02-B", nxt_factory(), filter_groups, **kw)
                return self.cs(groups([sample(50)]), yes=code, no=b)
            return code
        cd = self.mail(nocode_mid, f"{label} nocode · cooldown", nxt_factory(), filter_groups, **kw)
        if t02:
            b = self.mail(nocode_mid, f"{label} nocode · T02-B", nxt_factory(), filter_groups, **kw)
            code = self.cs(groups([sample(50)]), yes=code, no=b)
        return self.cs(cooldown or groups([COOLDOWN]), yes=cd, no=code)

    def chain(self, steps, nxt=None):
        """steps: lijst van functies nxt -> action_id, van boven naar beneden."""
        for step in reversed(steps):
            nxt = step(nxt)
        return nxt

    def old_path(self, flow_id, choices, utm, label_prefix):
        """T01 oud pad: wachttijden en templates uit de echte bestaande flow (GET). choices = keuzes bij
        elke split (True = JA). Stopt bij een split zonder keuze. Draft-mails worden overgeslagen."""
        src = get_flow(flow_id)["definition"]
        A = {str(a["id"]): a for a in src["actions"]}
        cur, ch, steps, i = str(src["entry_action_id"]), list(choices), [], 0
        while cur and cur != "None":
            a = A[cur]
            if a["type"] == "time-delay":
                d = a["data"]
                steps.append(("delay", (d["unit"], d["value"], d.get("delay_until_time"))))
                cur = str(a["links"].get("next"))
            elif a["type"] == "send-email":
                if a["data"].get("status") == "live":
                    i += 1
                    m = a["data"]["message"]
                    steps.append(("mail", (m, i)))
                cur = str(a["links"].get("next"))
            elif a["type"] in ("conditional-split", "trigger-split"):
                if not ch:
                    break
                cur = str(a["links"]["next_if_true" if ch.pop(0) else "next_if_false"])
            else:
                cur = str(a["links"].get("next"))
        nxt, summary = None, []
        for kind, val in reversed(steps):
            if kind == "delay":
                unit, value, until = val
                nxt = self.delay(unit, value, until, nxt)
            else:
                m, i = val
                old = m.get("additional_filters") or {"condition_groups": []}
                gs = [g["conditions"] for g in old["condition_groups"]] + [[NO_ORDER_SINCE_START]]
                msg = self.message(f"Old · {label_prefix} {i}", m["template_id"], m["subject_line"],
                                   (m.get("preview_text") or "").strip(), utm=utm, filter_groups=gs, base=False)
                nxt = self.raw_mail(msg, nxt)
        for kind, val in steps:
            summary.append(f"wacht {val[1]} {UNIT_NL[val[0]]}" + (f" tot {val[2][:5]}" if val[2] else "") if kind == "delay"
                           else f"{val[0]['template_id']} \"{val[0]['subject_line']}\"")
        self.notes.append(f"Oud pad uit {flow_id} (GET): " + " → ".join(summary))
        return nxt

    def definition(self, triggers, profile_filter, entry, reentry=None):
        d = {"triggers": triggers, "profile_filter": profile_filter, "actions": self.actions,
             "entry_action_id": entry}
        if reentry:
            d["reentry_criteria"] = {"duration": reentry, "unit": "day"}
        return {"data": {"type": "flow", "attributes": {"name": self.name, "definition": d}}}


def mtrig(metric, filt=None):
    return {"type": "metric", "id": metric, "trigger_filter": filt}


def t01(f, new_arm, old_arm):
    return f.cs(groups([sample(50)]), yes=new_arm, no=old_arm)


# ================================================================ flows (plan hoofdstuk 2)
FLOW_NAMES = {
    "postpurchase": "v4 · Post-purchase", "levering": "v4 · Post-purchase · levering",
    "checkout": "v4 · Checkout abandonment", "cart": "v4 · Cart abandonment",
    "browse": "v4 · Browse abandonment", "welcome": "v4 · Welcome", "winback": "v4 · Winback",
    "site": "v4 · Site abandonment", "sunset": "v4 · Sunset", "vip": "v4 · VIP",
    "anniversary": "v4 · Anniversary", "ugc": "v4 · UGC first egg", "sunsetkept": "v4 · Sunset · kept",
}
UTM = {"postpurchase": "v4-postpurchase", "levering": "v4-postpurchase", "checkout": "v4-checkout",
       "cart": "v4-cart", "browse": "v4-browse", "welcome": "v4-welcome", "winback": "v4-winback",
       "site": "v4-site", "sunset": "v4-sunset", "vip": "v4-vip", "anniversary": "v4-anniversary", "ugc": "v4-ugc",
       "sunsetkept": "v4-sunset-kept"}


def po(op, v, tf, filt=None):
    return mc(PLACED_ORDER, op, v, tf, filt)


# ---------------------------------------------------------------- 2.1 Checkout
def build_checkout(f):
    f.base_filters = [[NO_ORDER_SINCE_START]]

    def csm(op, v, days, filt):  # Checkout Started in de laatste N dagen (vangt het trigger-event)
        return mc(CHECKOUT_STARTED, op, v, last_days(days), filt)

    # dag 5: cooldown-split en T02, één template c4 / c4-nocode (land in de template)
    c4 = lambda nxt: f.router("c4", "c4-nocode", "C4")
    d5 = lambda nxt: f.delay("days", 2, "09:00:00", nxt)
    # dag 3: C3-S, C3-P of C3-ACC als verzendfilter (hoogstens één komt door)
    c3acc = lambda nxt: f.mail("c3-acc", "C3-ACC", nxt, [[csm("equals", 0, 4, f_items(KOOK))], [NIEUWE_KLANT]])
    # v5 (8 okt, integratie): C3-S alleen op set-titels (de $value >= 300-route vervalt); C3-P: Pan Pro of starterbundel,
    # waarde onder $300 (drempel 250 -> 300) en geen grote set. Wok/deep/pizza/roast/pot alleen of >= $300 zonder set: geen C3.
    c3p = lambda nxt: f.mail("c3-p", "C3-P", nxt, [
        [csm("greater-than", 0, 4, f_items(PANPRO_TITELS + STARTER_TITELS))], [csm("greater-than", 0, 4, f_value("less-than", 300))],
        [csm("equals", 0, 4, f_items(GROOT_SET_TITELS))]])
    c3s = lambda nxt: f.mail("c3-s", "C3-S", nxt, [[csm("greater-than", 0, 4, f_items(GROOT_SET_TITELS))]])
    d3 = lambda nxt: f.delay("days", 2, "09:00:00", nxt)
    c2acc = lambda nxt: f.mail("c2-acc", "C2-ACC", nxt, [[csm("equals", 0, 2, f_items(KOOK))]])
    c2 = lambda nxt: f.mail("c2", "C2", nxt, [[csm("greater-than", 0, 2, f_items(KOOK))], [NIEUWE_KLANT]])
    d2 = lambda nxt: f.delay("days", 1, None, nxt)  # 24 uur na C1 (besluit 3.5)
    c1 = lambda nxt: f.mail("c1", "C1", nxt)
    d1 = lambda nxt: f.delay("minutes", 30, None, nxt)
    new = f.chain([d1, c1, d2, c2, c2acc, d3, c3s, c3p, c3acc, d5, c4])
    old = f.old_path("Y2TmNB", [False], "old-checkout", "Checkout")
    entry = t01(f, new, old)
    f.notes += ["Landsplit vervallen (country-split-review): C4 is één template `c4` / `c4-nocode`, land via {% if %} in de template.",
                "Categorie (C2/C2-ACC, C3-S/C3-P/C3-ACC) als verzendfilter op Checkout Started in de laatste 2/4 dagen (Bouwnotitie 2.1).",
                "v5: C3-S = grote set in de checkout (GROOT_SET_TITELS); C3-P = Pan Pro of starterbundel (Pro Duo, Kit, 2 Pans + 2 Lids) onder $300 zonder grote set. Geen $value-route naar C3-S meer."]
    return f.definition(
        [mtrig(CHECKOUT_STARTED, groups([{"type": "metric-property", "metric_id": CHECKOUT_STARTED, "field": "$value",
                                          "filter": {"type": "numeric", "operator": "greater-than", "value": 0}}]))],
        groups([NO_ORDER_SINCE_START], [not_in_flow(last_days(14))],
               [f.received_from("postpurchase", days=7, fallback=OLD_POSTPURCHASE)]),
        entry, reentry=14)


# ---------------------------------------------------------------- 2.2 Cart
def build_cart(f):
    f.base_filters = [[zero(CHECKOUT_STARTED, FLOW_START)], [NO_ORDER_SINCE_START]]
    kook_conds = [some(ADDED_TO_CART, last_days(1), f_str("Product Name", "contains", w)) for w in KOOK_WOORDEN]

    pan = f.chain([
        lambda n: f.mail("k1", "K1", n),
        lambda n: f.delay("days", 1, None, n),  # 24 uur na K1
        lambda n: f.mail("k2-returning", "K2-RETURNING", n, [[HEEFT_GEKOCHT]]),
        lambda n: f.mail("k2-new", "K2-NEW", n, [[NIEUWE_KLANT]]),
        lambda n: f.delay("days", 2, "09:00:00", n),  # dag 3, 09:00
        lambda n: f.router("k3", "k3-nocode", "K3 · pan"),
    ])
    acc = f.chain([
        lambda n: f.mail("k1-acc", "K1-ACC", n),
        lambda n: f.delay("days", 3, "09:00:00", n),  # dag 3, 09:00
        lambda n: f.router("k3", "k3-nocode", "K3 · acc"),
    ])
    split_k = f.cs({"condition_groups": [{"conditions": kook_conds}]}, yes=pan, no=acc)
    new = f.delay("minutes", 30, None, split_k)
    old = f.old_path("SwkMyn", [True, True], "old-cart", "Cart")
    entry = t01(f, new, old)
    f.notes.append("CS K: Added to Cart waarvan Product Name een kookwoord bevat, in de laatste 1 dag (OF tussen de woorden).")
    trig = groups(
        [{"type": "metric-property", "metric_id": ADDED_TO_CART, "field": "Price",
          "filter": {"type": "numeric", "operator": "greater-than", "value": 0}}],
        *[[{"type": "metric-property", "metric_id": ADDED_TO_CART, "field": "Product Name",
            "filter": {"type": "string", "operator": "not-contains", "value": w}}]
          for w in ["Mystery Gift", "E-Book", "Free Shipping", "Giveaway"]])
    return f.definition(
        [mtrig(ADDED_TO_CART, trig)],
        groups([zero(CHECKOUT_STARTED, FLOW_START)], [NO_ORDER_SINCE_START],
               [f.received_from("checkout", days=7)], [not_in_flow(last_days(14))]),
        entry, reentry=14)


# ---------------------------------------------------------------- 2.3 Browse
def build_browse(f):
    f.base_filters = [[NO_ORDER_SINCE_START]]
    b2_extra = [[zero(ADDED_TO_CART, FLOW_START)]]
    kook_conds = [some(VIEWED_PRODUCT, last_days(1), f_str("Name", "contains", w)) for w in KOOK_WOORDEN]

    def clicked(name_part):
        return groups([some(CLICKED_EMAIL, FLOW_START, f_str("Campaign Name", "contains", name_part))])

    def pan_rest():
        b2c = f.router("b2-clicked", "b2-clicked-nocode", "B2-CLICKED · pan", b2_extra)
        b2n = f.mail("b2-notclicked", "B2-NOTCLICKED", None, b2_extra)
        # 12-fixes (8 okt): Klaviyo hernoemt A/B-variaties ("B1 Test #1 ..."), dus niet op de berichtnaam maar op $flow = deze flow
        # (B1 is de enige mail voor deze split). De API accepteert maar één metric_filter: Bot Click = false in de UI zetten.
        split = f.cs(groups([some(CLICKED_EMAIL, FLOW_START, f_str("$flow", "equals", f.flow_ref("browse", "WdRz5k")))]), yes=b2c, no=b2n)
        return f.delay("days", 2, "09:00:00", split)

    _, sa, _, sb = f.tpl("b1")
    pan = f.ab("T05a · B1-onderwerp (authority tegen social proof)",
               [("B1 · T05a-A", "b1", sa, {}), ("B1 · T05a-B", "b1", sb, {})], pan_rest)
    acc_split = f.cs(clicked("B1-ACC"), yes=f.router("b2-clicked", "b2-clicked-nocode", "B2-CLICKED · acc", b2_extra),
                     no=None)
    acc = f.mail("b1-acc", "B1-ACC", f.delay("days", 2, "09:00:00", acc_split))
    split_k = f.cs({"condition_groups": [{"conditions": kook_conds}]}, yes=pan, no=acc)
    new = f.delay("hours", 1, None, split_k)
    old = f.old_path("TyEjuQ", [True], "old-browse", "Browse")
    entry = t01(f, new, old)
    f.notes += ["Kookgerei-split: Viewed Product waarvan Name een kookwoord bevat in de laatste 1 dag (plan: trigger split; nu CS met dezelfde uitkomst).",
                "Klik-split na B1: Clicked Email waarvan $flow = deze flow sinds flowstart (Klaviyo hernoemt de A/B-variaties); na B1-ACC: Campaign Name bevat 'B1-ACC'. Bot Click = false in de UI toevoegen (API: maar één metric_filter).",
                "Oud pad: TyEjuQ 10-minutenarm ($1,31 tegen $1,18 per ontvanger, research/timing/01-data.md)."]
    return f.definition(
        [mtrig(VIEWED_PRODUCT)],
        groups([zero(ADDED_TO_CART, FLOW_START)], [zero(CHECKOUT_STARTED, FLOW_START)], [NO_ORDER_SINCE_START],
               [f.received_from("cart", days=7)], [f.received_from("checkout", days=7)],
               [f.received_from("welcome", days=7)], [not_in_flow(last_days(7))]),
        entry, reentry=7)


# ---------------------------------------------------------------- 2.4 Welcome
def build_welcome(f):
    f.base_filters = [[NO_ORDER_SINCE_START], [f.received_from("checkout", days=1)], [f.received_from("cart", days=1)]]

    def w4_and_rest():
        w5 = lambda: f.mail("w5", "W5", None)
        if W4_MODE == "template":
            return f.mail("w4", "W4", f.delay("days", 4, "09:00:00", w5()))
        us = f.mail("w4-us", "W4-US", f.delay("days", 4, "09:00:00", w5()))
        intl = f.mail("w4-int", "W4-INT", f.delay("days", 4, "09:00:00", w5()))
        return f.cs({"condition_groups": [{"conditions": COUNTRY_US_ANY}]}, yes=us, no=intl)

    def after_w1():
        return f.chain([
            lambda n: f.delay("days", 1, "09:00:00", n),
            lambda n: f.mail("w2", "W2", n, label=FROM_BENJAMIN),
            lambda n: f.delay("days", 2, "09:00:00", n),
            lambda n: f.mail("w3", "W3", n),
            lambda n: f.delay("days", 3, "09:00:00", n),
            lambda n: w4_and_rest(),
        ])

    w1 = f.ab("T04 · W1-A code-blok tegen W1-B gift card",
              [("W1 · T04-A", "w1-a", None, {}), ("W1 · T04-B", "w1-b", None, {})], after_w1)
    a2 = f.cs(groups([HEEFT_GEKOCHT]), yes=f.mail("w0", "W0", None), no=w1)
    a1 = f.cs(groups([some(PLACED_ORDER, FLOW_START)]), yes=None, no=a2)
    new = f.delay("minutes", 20, None, a1)
    old = f.old_path("SiaNLu", [False, True], "old-welcome", "Welcome")
    entry = t01(f, new, old)
    f.notes += [f"W4-modus: {W4_MODE} ({'landsplit w4-us/w4-int, US = United States of US' if W4_MODE == 'split' else 'één template w4'}).",
                "T2SmtR (Failure to launch) kan geen filter v3_arm krijgen (update-profile kan niet via API): zie GO-LIVE.md."]
    return f.definition(
        [{"type": "list", "id": WELCOME_LIST}],
        groups([{"type": "profile-property", "property": "email",
                 "filter": {"type": "string", "operator": "not-contains", "value": "test@"}}],
               [not_in_flow(ALLTIME)]),
        entry)


# ---------------------------------------------------------------- 2.5 Post-purchase
def build_postpurchase(f):
    def pol(days, op, titles=None, value=None):
        filt = f_items(titles) if titles else f_value(*value)
        return mc(PLACED_ORDER, "greater-than" if op else "equals", 0, last_days(days), filt)

    D = 21  # de trigger-order valt op dag 20 binnen 21 dagen
    has = lambda t: pol(D, True, t)
    hasnot = lambda t: pol(D, False, t)
    big, notbig = pol(D, True, value=("greater-than-or-equal", 300)), pol(D, False, value=("greater-than-or-equal", 300))
    owner = some(PLACED_ORDER, ALLTIME, f_items(KOOK))
    not_owner = zero(PLACED_ORDER, ALLTIME, f_items(KOOK))
    p3_base = [[NO_ORDER_SINCE_START], [zero(REFUNDED, last_days(30))]]
    # P3-router (2.5 stap 3K/3A) als verzendfilters; per profiel komt hoogstens één mail door.
    P3 = [
        ("p3-set", "P3-SET", [[has(KOOK)], [has(SET_TITELS), big]]),
        ("p3-next", "P3-NEXT · deksel", [[has(KOOK)], [hasnot(SET_TITELS)], [notbig], [has(DEKSEL_TITELS)]]),
        ("p3-pan", "P3-PAN", [[has(KOOK)], [hasnot(SET_TITELS)], [notbig], [hasnot(DEKSEL_TITELS)],
                              [has(PANPRO_TITELS + VORM_TITELS)]]),
        ("p3-accessory", "P3-ACCESSORY · kook", [[has(KOOK)], [hasnot(SET_TITELS)], [notbig], [hasnot(DEKSEL_TITELS)],
                                                 [hasnot(PANPRO_TITELS + VORM_TITELS)]]),
        ("p3-next", "P3-NEXT · eigenaar", [[hasnot(KOOK)], [hasnot(EGIFT_TITELS)], [owner]]),
        ("p3-apron", "P3-APRON", [[hasnot(KOOK)], [hasnot(EGIFT_TITELS)], [not_owner], [has(SCHORT_TITELS)]]),
        ("p3-accessory", "P3-ACCESSORY · acc", [[hasnot(KOOK)], [hasnot(EGIFT_TITELS)], [not_owner],
                                                [hasnot(SCHORT_TITELS)]]),
    ]

    def p3_chain(arm):
        nxt = None
        for mid, label, fg in reversed(P3):
            if arm == "A":
                nxt = f.mail(mid, f"{CODE} {label}", nxt, p3_base + fg)
            else:
                nxt = f.mail(f"{mid}-nocode", f"{label} nocode · {arm}", nxt, p3_base + fg)
        return nxt

    t02 = f.cs(groups([sample(50)]), yes=p3_chain("A"), no=p3_chain("T02-B"))
    router = f.cs(groups([COOLDOWN]), yes=p3_chain("cooldown"), no=t02)
    r0 = f.cs(groups([po("equals", 2, ALLTIME)]), yes=None, no=router)
    entry = f.chain([
        lambda n: f.delay("hours", 1, None, n),
        lambda n: f.mail("p1-first", "P1-FIRST", n, [[po("equals", 1, ALLTIME)]]),
        lambda n: f.mail("p1-repeat", "P1-REPEAT", n, [[po("greater-than", 1, ALLTIME)]]),
        lambda n: f.delay("days", 16, "09:00:00", n),
        lambda n: f.mail("p2-safe", "P2-SAFE", n, [[pol(17, True, P2_TITELS)], [zero(DELIVERED, FLOW_START)],
                                                    [zero(REFUNDED, last_days(30))]]),
        lambda n: f.delay("days", 4, "09:00:00", n),
        lambda n: r0,
    ])
    f.notes += ["P1-FIRST/P1-REPEAT en de P3-router als verzendfilters (geen samenkomende takken). Categorie op Placed Order in de laatste 21 dagen.",
                "P3-NEXT staat twee keer (deksel in order; of eigenaar die nu een accessoire kocht), want OF tussen twee EN-blokken kan niet in één filter.",
                "Titellijsten = exacte Shopify-producttitels (8 okt 2026, alle statussen); P2 en P2-SAFE alleen bij pannen en sets (P2_TITELS).",
                "T02 in P3: één split, alle vijf P3-mails in beide armen (strata P3-pan, P3-set, P3-accessory, P3-next, P3-apron)."]
    return f.definition([mtrig(PLACED_ORDER)], groups([not_in_flow(last_days(30))]), entry, reentry=30)


def build_levering(f):
    p2 = f.mail("p2", "P2", None, [[zero(REFUNDED, last_days(30))]])
    entry = f.delay("days", 1, "09:00:00", p2)
    return f.definition(
        [mtrig(DELIVERED)],
        groups([some(PLACED_ORDER, last_days(30), f_items(P2_TITELS))], [not_in_flow(last_days(30))],
               [zero(RECEIVED_EMAIL, last_days(30),
                     f_str("Campaign Name", "contains", "P2-SAFE"))]),
        entry, reentry=30)


# ---------------------------------------------------------------- 2.6 Winback
def build_winback(f):
    f.base_filters = [[NO_ORDER_SINCE_START]]
    D = 46
    has = lambda t: some(PLACED_ORDER, last_days(D), f_items(t))
    hasnot = lambda t: zero(PLACED_ORDER, last_days(D), f_items(t))
    big = some(PLACED_ORDER, last_days(D), f_value("greater-than-or-equal", 300))
    notbig = zero(PLACED_ORDER, last_days(D), f_value("greater-than-or-equal", 300))
    r1x = [[f.received_from("postpurchase", days=7)], [f.received_from("vip", days=7)]]

    def r2():
        vip = f.router("r2-vip", "r2-vip-nocode", "R2-VIP")
        reg = f.router("r2", "r2-nocode", "R2")
        return f.cs(groups([po("greater-than-or-equal", 2, ALLTIME)]), yes=vip, no=reg)

    entry = f.chain([
        lambda n: f.delay("days", 45, "09:00:00", n),
        lambda n: f.mail("r1-set", "R1-SET", n, r1x + [[has(KOOK)], [has(SET_TITELS), big]]),
        lambda n: f.mail("r1-pan", "R1-PAN · kook", n, r1x + [[has(KOOK)], [hasnot(SET_TITELS)], [notbig]]),
        lambda n: f.mail("r1-pan", "R1-PAN · eigenaar", n, r1x + [[hasnot(KOOK)], [some(PLACED_ORDER, ALLTIME, f_items(KOOK))]]),
        lambda n: f.mail("r1-acc", "R1-ACC", n, r1x + [[zero(PLACED_ORDER, ALLTIME, f_items(KOOK))]]),
        lambda n: f.delay("days", 30, "09:00:00", n),
        lambda n: r2(),
    ])
    f.notes += ["Geen herinstapgrens (3.11): elke order start een nieuwe run; de oude stopt via de verzendfilter Placed Order = 0 sinds start.",
                "R1-router als verzendfilters op Placed Order in de laatste 46 dagen. R2 alleen zolang 'up to 50% off' live is."]
    return f.definition([mtrig(PLACED_ORDER)], None, entry)


# ---------------------------------------------------------------- 2.7 Site abandonment
def build_site(f):
    f.base_filters = [[zero(VIEWED_PRODUCT, FLOW_START)], [zero(ADDED_TO_CART, FLOW_START)],
                      [zero(CHECKOUT_STARTED, FLOW_START)], [NO_ORDER_SINCE_START]]
    entry = f.chain([
        lambda n: f.delay("hours", 2, None, n),
        lambda n: f.mail("a1", "A1", n),
        lambda n: f.delay("days", 2, "09:00:00", n),
        lambda n: f.mail("a2", "A2", n),
    ])
    f.notes.append("'Can receive email marketing' niet als filter: marketingmails gaan in Klaviyo nooit naar uitgeschreven profielen.")
    return f.definition(
        [mtrig(ACTIVE_ON_SITE)],
        groups([zero(VIEWED_PRODUCT, FLOW_START)], [zero(ADDED_TO_CART, FLOW_START)], [zero(CHECKOUT_STARTED, FLOW_START)],
               [NO_ORDER_SINCE_START], [zero(PLACED_ORDER, last_days(30))],
               [f.received_from("browse", days=7)], [f.received_from("cart", days=7)],
               [f.received_from("checkout", days=7)], [f.received_from("postpurchase", days=7)],
               [f.received_from("welcome", days=10)], [not_in_flow(last_days(14))]),
        entry, reentry=14)


# ---------------------------------------------------------------- 2.8 Sunset
def build_sunset(f):
    seg = f.ctx.segment_ids.get(SUNSET_SEGMENT) or (KNOWN_SEGMENT_IDS[SUNSET_SEGMENT] if OFFLINE else None)
    if not seg:
        f.missing_templates.add(f"SEGMENT {SUNSET_SEGMENT}")
        seg = f"SEG?{SUNSET_SEGMENT}"
    entry = f.chain([
        lambda n: f.delay("days", 1, "09:00:00", n),
        lambda n: f.mail("s1", "SUNSET · S1", n),
        lambda n: f.delay("days", 4, "09:00:00", n),
        lambda n: f.mail("s2", "SUNSET · S2", n, [[zero(CLICKED_EMAIL, FLOW_START, NOT_BOT)], [zero(ACTIVE_ON_SITE, FLOW_START)],
                                                  [NO_ORDER_SINCE_START]], label=FROM_BENJAMIN),
    ])
    f.notes += ["Stap 3 (update profile sunset_status) kan niet via de API. Vervanging: segment 'v4 · Sunset · suppressed' = "
                "in 'v4 · Sunset · unengaged 120d' EN Received Email waarvan Campaign Name 'SUNSET · S2' bevat, minstens 1 keer in 60 dagen "
                "EN 0 keer in de laatste 3 dagen. Wie klikt, de site bezoekt of koopt valt vanzelf uit het unengaged-segment.",
                "Geen Opened Email-filter (3.16).",
                "S2-filter telt alleen menselijke klikken (Clicked Email waarvan Bot Click = false, research/v5/06 fix 3); een scannerklik "
                "slaat S2 niet meer over. Segment WuHSm6 zelf wordt in de hoofdsessie bijgewerkt (research/v5/08-integratie.md).",
                "Vervolg voor wie klikt: aparte flow 'v4 · Sunset · kept' (sunsetkept)."]
    return f.definition(
        [{"type": "segment", "id": seg}],
        groups([not_in_flow(last_days(180))], [f.received_from("welcome", days=30)],
               [f.received_from("postpurchase", days=30)]),
        entry, reentry=180)


# ---------------------------------------------------------------- 2.8b Sunset · kept (research/v5/06-sunset-kept.md sectie 6)
KEPT = "SUNSET-KEPT ·"  # berichtnamen: bevat bewust niet "SUNSET · S" (suppressed-segment) en niet "CODE ·" (cooldown)


def kept_prop(field, ftype, op, value):
    return {"type": "metric-property", "metric_id": CLICKED_EMAIL, "field": field,
            "filter": {"type": ftype, "operator": op, "value": value}}


def build_sunset_kept(f):
    """Instap: menselijke klik (Bot Click false) op S1 of S2 van v4 · Sunset. 30 minuten later S3, dag 4 09:00 S4.
    Geen samenkomende takken (lineair), geen update-profile, geen coupon."""
    trig = groups([kept_prop("$flow", "string", "equals", f.flow_ref("sunset"))],
                  [kept_prop("Bot Click", "boolean", "equals", False)])
    s4f = [[NO_ORDER_SINCE_START], [f.received_from("checkout", days=3)], [f.received_from("cart", days=3)]]
    entry = f.chain([
        lambda n: f.delay("minutes", 30, None, n),
        lambda n: f.mail("s3-kept", f"{KEPT} S3", n, [[NO_ORDER_SINCE_START]], label=FROM_BENJAMIN),
        lambda n: f.delay("days", 4, "09:00:00", n),
        lambda n: f.mail("s4-kept", f"{KEPT} S4", n, s4f, label=FROM_BENJAMIN),
    ])
    f.notes += ["'Kept' zonder update-profile: segment 'v4 · Sunset · kept' = Clicked Email (Bot Click false) where $flow = "
                "v4 · Sunset, minstens 1 keer in de laatste 180 dagen. Keuze in S3: Clicked Email waarvan URL het pad bevat.",
                "Geen korting en geen coupon (06-sunset-kept, 4). Klik op S1 en S2 geeft één instap (flowfilter 365 dagen).",
                "Terugval als de triggerfilter $flow weigert: Campaign Name contains 'SUNSET · S'."]
    return f.definition([mtrig(CLICKED_EMAIL, trig)], groups([not_in_flow(last_days(365))]), entry)


# ---------------------------------------------------------------- 2.9 VIP
def build_vip(f):
    v1f = [[zero(REFUNDED, FLOW_START)], [zero(PLACED_ORDER, last_days(14))]]

    def v2():
        return f.delay("days", 10, "09:00:00",
                       f.mail("v2", "V2", None, [[NO_ORDER_SINCE_START], [zero(REFUNDED, FLOW_START)]], label=FROM_BENJAMIN))

    # Besluit 8 okt: VIP krijgt 15%, ook vlak na een eerdere code als die NIET gebruikt is. De cooldown-tak (v1-nocode)
    # alleen als er een CODE-mail in 30 dagen was EN de order (de 2e order, de trigger, 30 dagen geleden) een kortingscode had.
    # De flowfilter Placed Order = 2 all time + de verzendfilter Placed Order 0 in 14 dagen maken "laatste 45 dagen" = de trigger-order.
    used = {"codes": [{"property": "Discount Codes", "filter": {"type": "list", "operator": "length-greater-than", "value": 0}}],
            "discounts": [{"property": "Total Discounts", "filter": {"type": "numeric", "operator": "greater-than", "value": 0}}]}
    if VIP_COOLDOWN in used:
        cd, cdtxt = groups([COOLDOWN], [some(PLACED_ORDER, last_days(45), used[VIP_COOLDOWN])]), (
            f"cooldown = CODE-mail in 30 dagen EN Placed Order in 45 dagen met {'Discount Codes niet leeg' if VIP_COOLDOWN == 'codes' else 'Total Discounts > 0'}")
    elif VIP_COOLDOWN == "none":
        cd, cdtxt = False, "geen cooldown: iedereen V1 (15%)"
    else:
        cd, cdtxt = None, "oude cooldown (alleen CODE-mail in 30 dagen)"
    entry = f.delay("days", 30, "09:00:00", f.router("v1", "v1-nocode", "V1", v1f, nxt_factory=v2, t02=T02_NEW, cooldown=cd))
    f.notes += [f"V1-cooldown (--vip-cooldown={VIP_COOLDOWN}): {cdtxt}. Onbevestigd in de API: de list-operator 'length-greater-than' op "
                "'Discount Codes'. Weigert Klaviyo de POST, dan opnieuw met --vip-cooldown=discounts, en anders --vip-cooldown=none.",
                f"T02 op V1: {'aan' if T02_NEW else 'uit (eerste 4 weken 100% code zonder cooldown; daarna --t02-new)'}.",
                "siraat_regular = true (update profile) kan niet via de API; segment 'v4 · VIP' = Placed Order minstens 2 keer.",
                "Flowfilter Placed Order = 2 over all time geldt bij elke stap: een 3e order vóór dag 30 haalt iemand uit de flow."]
    return f.definition([mtrig(PLACED_ORDER)],
                        groups([po("equals", 2, ALLTIME)], [not_in_flow(ALLTIME)]), entry)


# ---------------------------------------------------------------- 2.10 Anniversary
def build_anniversary(f):
    n1f = [[zero(REFUNDED, FLOW_START)], [f.received_from("vip", days=14)], [f.received_from("winback", days=14)],
           [zero(OPENED_TICKET, last_days(14))]]
    n2f = [[zero(REFUNDED, FLOW_START)], [zero(PLACED_ORDER, last_days(14))]]
    entry = f.chain([
        lambda n: f.delay("days", 182, "09:00:00", n),
        lambda n: f.mail("n1", "N1", n, n1f),
        lambda n: f.delay("days", 183, "09:00:00", n),
        lambda n: f.router("n2", "n2-nocode", "N2", n2f, t02=T02_NEW),
    ])
    f.notes += ["Triggerfilter 'Items bevat kookgerei' als flowfilter: Placed Order met KOOK+SET minstens 1 keer over all time "
                "(samen met Placed Order = 1 over all time is dat de eerste order). Een filter 'in de laatste dag' zou bij de "
                "herbeoordeling op dag 182 iedereen eruit halen.",
                "Placed Order = 1 over all time wordt bij elke stap opnieuw gecontroleerd: wie binnen het jaar opnieuw koopt, krijgt geen N1/N2.",
                f"182 en 183 dagen in één wachttijd{'; opgeknipt in stukken van ' + str(MAX_DELAY) + ' dagen' if MAX_DELAY else ' (als Klaviyo weigert: --max-delay=91)'}."]
    return f.definition([mtrig(PLACED_ORDER)],
                        groups([po("equals", 1, ALLTIME)], [some(PLACED_ORDER, ALLTIME, f_items(KOOK))],
                               [not_in_flow(ALLTIME)]), entry)


# ---------------------------------------------------------------- 2.11 UGC first egg
def build_ugc(f):
    backorder = BACKORDER_FALLBACK
    try:
        pf = get_flow("XzHrez")["definition"]["profile_filter"]["condition_groups"]
        for g in pf:
            for c in g["conditions"]:
                for mf in c.get("metric_filters") or []:
                    if mf["property"] == "Items":
                        backorder = mf["filter"]["value"]
    except Exception:
        pass
    u1 = f.mail("u1", "U1", None, [[zero(OPENED_TICKET, FLOW_START)], [zero(REFUNDED, last_days(30))],
                                   [some(FULFILLED, last_days(60))]])
    entry = f.delay("days", 4, "09:00:00", u1)
    f.notes.append("Backorder-uitsluiting gelezen uit XzHrez (12-delige set). Reply-to support@ (Gorgias-macro UGC15).")
    return f.definition([mtrig(DELIVERED)],
                        groups([po("equals", 1, ALLTIME)], [some(PLACED_ORDER, ALLTIME, f_items(KOOK))],
                               [not_in_flow(ALLTIME)], [zero(PLACED_ORDER, ALLTIME, f_items(backorder))]), entry)


BUILDERS = {"postpurchase": build_postpurchase, "levering": build_levering, "checkout": build_checkout,
            "cart": build_cart, "browse": build_browse, "welcome": build_welcome, "winback": build_winback,
            "site": build_site, "sunset": build_sunset, "vip": build_vip, "anniversary": build_anniversary,
            "ugc": build_ugc, "sunsetkept": build_sunset_kept}
PREFERRED = ["postpurchase", "levering", "checkout", "cart", "browse", "welcome", "vip", "winback",
             "anniversary", "site", "sunset", "sunsetkept", "ugc"]


# ================================================================ controles
def iter_actions(actions):
    for a in actions:
        yield a
        if a["type"] == "ab-test":
            yield a["data"]["main_action"]
            yield from a["data"]["current_experiment"]["variations"]


def validate(body):
    d = body["data"]["attributes"]["definition"]
    acts = {a["temporary_id"]: a for a in d["actions"]}
    errs, refs = [], {}
    for a in d["actions"]:
        for k, v in a["links"].items():
            if v is None:
                continue
            if v not in acts:
                errs.append(f"{a['temporary_id']}.{k} verwijst naar onbekende actie {v}")
            refs.setdefault(v, []).append(a["temporary_id"])
    if d["entry_action_id"] not in acts:
        errs.append("entry_action_id onbekend")
    refs.setdefault(d["entry_action_id"], []).append("ENTRY")
    for v, src in refs.items():
        if len(src) > 1:
            errs.append(f"samenkomende takken: {v} wordt bereikt vanuit {src}")
    seen, stack = set(), [d["entry_action_id"]]
    while stack:
        x = stack.pop()
        if x in seen or x not in acts:
            continue
        seen.add(x)
        stack += [v for v in acts[x]["links"].values() if v]
    for x in acts:
        if x not in seen:
            errs.append(f"actie {x} is niet bereikbaar")
    for a in iter_actions(d["actions"]):
        if a["type"] == "send-email":
            m = a["data"]["message"]
            if not m.get("template_id"):
                errs.append(f"{m['name']}: geen template")
            if not m.get("subject_line"):
                errs.append(f"{m['name']}: geen onderwerp")
            if a["data"].get("status") != "draft":
                errs.append(f"{m['name']}: status niet draft")
            if m.get("smart_sending_enabled"):
                errs.append(f"{m['name']}: smart sending aan")
        if a["type"] == "update-profile":
            errs.append("update-profile wordt door de API geweigerd")
    blob = json.dumps(d)
    for bad in ('"is-not-set"', '"existence"'):
        if bad in blob:
            errs.append(f"ongeldige filter-operator {bad}")
    return errs, None


# ---------------------------------------------------------------- leesbare boom
def tf_txt(tf):
    if not tf:
        return ""
    o = tf["operator"]
    return {"flow-start": "sinds flowstart", "alltime": "over all time"}.get(o, f"in de laatste {tf.get('quantity')} dagen")


def mf_txt(mfs):
    out = []
    for m in mfs or []:
        fl = m["filter"]
        v = fl.get("value")
        if isinstance(v, list):
            v = TITLE_SETS.get(tuple(v), f"{len(v)} titels")
        out.append(f"{m['property']} {fl['operator']} {v}")
    return " en ".join(out)


def cond_txt(c, flowname):
    t = c["type"]
    if t == "profile-metric":
        op, v = c["measurement_filter"]["operator"], c["measurement_filter"]["value"]
        ops = {"equals": "=", "greater-than": ">", "greater-than-or-equal": "≥", "less-than": "<"}
        name = METRICS.get(c["metric_id"], c["metric_id"])
        mf = mf_txt(c.get("metric_filters")).replace("$flow equals ", "$flow = ")
        mf = mf.replace(f"FLOW?postpurchase|{OLD_POSTPURCHASE}", f"v4 · Post-purchase (zolang die geen ID heeft: {OLD_POSTPURCHASE})")
        for slug, n in FLOW_NAMES.items():
            mf = mf.replace(f"FLOW?{slug}", n)
        for n, i in flowname.items():
            mf = mf.replace(f"$flow = {i}", f"$flow = {n} ({i})")
        return f"{name}{' (' + mf + ')' if mf else ''} {ops.get(op, op)} {v} {tf_txt(c['timeframe_filter'])}"
    if t == "profile-not-in-flow":
        return f"niet in deze flow {tf_txt(c['timeframe_filter'])}"
    if t == "profile-sample":
        return f"random {c['percentage']}%"
    if t == "profile-property":
        return f"{c['property']} {c['filter']['operator']} {c['filter'].get('value', '')}"
    if t == "metric-property":
        return f"event.{c['field']} {c['filter']['operator']} {c['filter'].get('value')}"
    return json.dumps(c)[:120]


def filt_txt(f, flowname):
    if not f:
        return ""
    return " EN ".join("(" + " OF ".join(cond_txt(c, flowname) for c in g["conditions"]) + ")"
                       if len(g["conditions"]) > 1 else cond_txt(g["conditions"][0], flowname)
                       for g in f["condition_groups"])


def render_tree(body, flowname, base_txt):
    d = body["data"]["attributes"]["definition"]
    A = {a["temporary_id"]: a for a in d["actions"]}
    lines = []

    def mail_line(m, ind):
        ft = filt_txt(m.get("additional_filters"), flowname)
        if base_txt and ft.startswith(base_txt):
            ft = "standaard" + ft[len(base_txt):]
        tpl = m["template_id"]
        tpl = f"**ONTBREEKT** `{tpl[4:]}`" if tpl.startswith("TPL?") else f"`{tpl}`"
        lab = "" if m["from_label"] == FROM_LABEL else f" · afzender {m['from_label']}"
        lines.append(f"{ind}- ✉ **{m['name']}** · {tpl} · \"{m['subject_line']}\"{lab}")
        if ft:
            lines.append(f"{ind}  - filter: {ft}")

    def walk(i, ind):
        while i:
            a = A[i]
            t = a["type"]
            if t == "time-delay":
                x = a["data"]
                u = {"minutes": "minuten", "hours": "uur", "days": "dagen"}[x["unit"]]
                lines.append(f"{ind}- ⏱ wacht {x['value']} {u}" + (f", tot {x['delay_until_time'][:5]}" if x.get("delay_until_time") else ""))
            elif t == "send-email":
                mail_line(a["data"]["message"], ind)
            elif t == "ab-test":
                ce = a["data"]["current_experiment"]
                lines.append(f"{ind}- 🔀 A/B-actie **{ce['name']}** (50/50, geen automatische winnaar, winnaar op {ce['winner_metric']})")
                for v in ce["variations"]:
                    mail_line(v["data"]["message"], ind + "  ")
            elif t == "conditional-split":
                lines.append(f"{ind}- ◆ split: {filt_txt(a['data']['profile_filter'], flowname)}")
                lines.append(f"{ind}  - JA:")
                walk(a["links"]["next_if_true"], ind + "    ")
                if not a["links"]["next_if_true"]:
                    lines.append(f"{ind}    - (einde)")
                lines.append(f"{ind}  - NEE:")
                walk(a["links"]["next_if_false"], ind + "    ")
                if not a["links"]["next_if_false"]:
                    lines.append(f"{ind}    - (einde)")
                return
            i = a["links"].get("next")

    walk(d["entry_action_id"], "")
    return lines


# ---------------------------------------------------------------- Klaviyo-controle (alleen GET)
def klaviyo_check(ctx):
    rep = {"metrics": [], "list": None, "segments": {}, "coupons": None, "v4_flows": [], "errors": []}
    if OFFLINE:
        rep["errors"].append("offline: geen controle")
        return rep
    for mid, name in METRICS.items():
        if mid == "RtgBgs":
            continue
        d = api("GET", f"metrics/{mid}")
        got = d.get("data", {}).get("attributes", {}).get("name")
        rep["metrics"].append((mid, name, got))
    d = api("GET", f"lists/{WELCOME_LIST}")
    rep["list"] = d.get("data", {}).get("attributes", {}).get("name")
    segs, err = get_all("segments?fields[segment]=name")
    names = {s["attributes"]["name"]: s["id"] for s in segs}
    for want in [SUNSET_SEGMENT, "v4 · Sunset · suppressed", "v4 · Welcome-bescherming", "v4 · Campagne-cap",
                 "v4 · Heeft kookgerei", "v4 · VIP", "v4 · US"]:
        rep["segments"][want] = names.get(want)
        if names.get(want):
            ctx.segment_ids[want] = names[want]
    d = api("GET", "coupons")
    rep["coupons"] = [c["attributes"].get("external_id") for c in d.get("data", [])] if "data" in d else None
    fl, _ = get_all("flows?fields[flow]=name,status&filter=contains(name,%22v4%20%C2%B7%22)")
    rep["v4_flows"] = [(x["id"], x["attributes"]["name"], x["attributes"]["status"]) for x in fl]
    return rep


COUPONS = [("C4_10_48H", "10%", "48 uur", "c4 (checkout)"), ("K3_10_48H", "10%", "48 uur", "k3 (cart)"),
           ("B2_10_48H", "10%", "48 uur", "b2-clicked (browse)"), ("P3_THANKYOU_10_14D", "10%", "14 dagen", "p3-* (post-purchase)"),
           ("R2_10_72H", "10%", "72 uur", "r2 (winback)"), ("R2_VIP_15_72H", "15%", "72 uur", "r2-vip (winback)"),
           ("SK_REGULARS15_14D", "15%", "14 dagen", "v1 (VIP)"), ("SK_ANNIV15_7D", "15%", "7 dagen", "n2 (anniversary, besluit 8 okt)")]


def order(deps):
    done, out = set(), []
    while len(out) < len(PREFERRED):
        for s in PREFERRED:
            if s not in done and deps.get(s, set()) - {s} <= done:
                out.append(s)
                done.add(s)
                break
        else:
            sys.exit(f"Cyclische afhankelijkheid: {deps}")
    return out


# ================================================================ main
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    ctx = Ctx()
    rep = klaviyo_check(ctx)
    built = {}
    for slug in PREFERRED:
        f = Flow(ctx, slug, FLOW_NAMES[slug], UTM[slug])
        body = BUILDERS[slug](f)
        errs, _ = validate(body)
        built[slug] = (f, body, errs)
    deps = {s: v[0].deps for s, v in built.items()}
    seq = order(deps)

    if "--order" in ARGS:
        for i, s in enumerate(seq, 1):
            print(f"{i:2d}. {s:13s} {FLOW_NAMES[s]:32s} hangt af van: {', '.join(sorted(deps[s] - {s})) or '-'}")
        return

    # ---- schrijven
    flowname = {n: i for n, i in ctx.flow_ids.items()}
    all_missing, summary = set(), []
    for s in seq:
        f, body, errs = built[s]
        with open(os.path.join(OUT_DIR, f"{s}.json"), "w") as fh:
            json.dump(body, fh, indent=1, ensure_ascii=False)
        acts = body["data"]["attributes"]["definition"]["actions"]
        mails = [a for a in iter_actions(acts) if a["type"] == "send-email" and not a["temporary_id"].endswith("m")]
        splits = sum(a["type"] == "conditional-split" for a in acts)
        abt = sum(a["type"] == "ab-test" for a in acts)
        all_missing |= f.missing_templates
        summary.append((s, len(acts), len(mails), splits, abt, len(errs), sorted(f.missing_templates)))

    # ---- OVERZICHT.md
    L = ["# v4-flows · overzicht voor controle", "",
         f"Gegenereerd door `scripts/build_flows.py` op {time.strftime('%Y-%m-%d %H:%M')} (dry-run). "
         f"Modus: W4 `{W4_MODE}`, A/B `{AB_MODE}`, T02 op V1/N2 `{'aan' if T02_NEW else 'uit'}`"
         f"{', max-delay ' + str(MAX_DELAY) if MAX_DELAY else ''}. De JSON per flow staat ernaast (`<slug>.json`).", "",
         "Leeswijzer: ⏱ wachttijd · ◆ split (JA/NEE) · 🔀 A/B-actie · ✉ mail (berichtnaam · template-ID · onderwerp). "
         "\"standaard\" = de verzendfilter die op elke mail van die flow staat (zie kop). Takken komen nooit samen: "
         "waar het plan een gedeeld vervolg heeft, staat het vervolg per tak apart.", "",
         "## Samenvatting", "",
         "| # | Flow | Acties | Mails | Splits | A/B | Controle | Ontbrekend |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for i, (s, na, nm, ns, nab, ne, miss) in enumerate(summary, 1):
        L.append(f"| {i} | {FLOW_NAMES[s]} (`{s}`) | {na} | {nm} | {ns} | {nab} | {'OK' if not ne else str(ne) + ' fouten'} | {len(miss)} |")
    L += ["", "Volgorde = bouwvolgorde voor `--live` (een flow verwijst via \"Received Email where $flow = ...\" naar flows "
          "die eerder in de lijst staan). Welcome staat vóór browse, omdat browse filtert op welcome-mails.", ""]

    L += ["## Klaviyo-controle (GET)", ""]
    if rep["metrics"]:
        L += ["| Metric | Verwacht | In Klaviyo |", "| --- | --- | --- |"]
        L += [f"| {m} | {n} | {g or '**ONTBREEKT**'} |" for m, n, g in rep["metrics"]]
        L += ["", f"- Lijst {WELCOME_LIST}: {rep['list'] or '**ONTBREEKT**'}"]
        for sname, sid in rep["segments"].items():
            L.append(f"- Segment \"{sname}\": {sid or '**ONTBREEKT**'}")
        L.append(f"- Coupons in Klaviyo: {', '.join(rep['coupons']) if rep['coupons'] else '**geen** (alle 8 pools ontbreken)'}")
        L.append("- Bestaande v4-flows: " + (", ".join(f"{i} {n} ({st})" for i, n, st in rep["v4_flows"]) or "geen"))
    L += ["", "### Templates die nog geëxporteerd moeten worden", ""]
    tm = sorted(x for x in all_missing if not x.startswith("SEGMENT"))
    L += [f"{len(tm)} templates ontbreken in `exports/live/templates.csv`:", ""] + [f"- `{x}`" for x in tm] + [""]
    L += ["### Coupons (plan 1.4 en 4.4)", "", "| Pool | Korting | Vervalt na | Mail | In Klaviyo |", "| --- | --- | --- | --- | --- |"]
    have = set(rep["coupons"] or [])
    L += [f"| {p} | {k} | {v} | {m} | {'ja' if p in have else 'nee'} |" for p, k, v, m in COUPONS]
    L.append("")

    for s in seq:
        f, body, errs = built[s]
        d = body["data"]["attributes"]["definition"]
        L += [f"## {FLOW_NAMES[s]} (`{s}`, utm_campaign `{UTM[s]}`)", ""]
        trig = d["triggers"][0]
        ttxt = {"list": f"lijst {trig['id']}", "segment": f"segment {trig['id']}"}.get(trig["type"], METRICS.get(trig["id"], trig["id"]))
        L.append(f"- **Trigger**: {ttxt}" + (f" · triggerfilter: {filt_txt(trig.get('trigger_filter'), flowname)}" if trig.get("trigger_filter") else ""))
        L.append(f"- **Flowfilters**: {filt_txt(d.get('profile_filter'), flowname) or 'geen'}")
        L.append(f"- **Herinstap**: {str(d['reentry_criteria']['duration']) + ' dagen' if d.get('reentry_criteria') else 'geen grens (alleen via flowfilter)'}")
        base_txt = filt_txt({"condition_groups": [{"conditions": g} for g in f.base_filters]}, flowname) if f.base_filters else ""
        if base_txt:
            L.append(f"- **Standaard verzendfilter op elke v4-mail**: {base_txt}")
        if f.deps - {s}:
            L.append(f"- **Verwijst naar**: {', '.join(FLOW_NAMES[x] for x in sorted(f.deps - {s}))}")
        for n in f.notes:
            L.append(f"- {n}")
        for w in sorted(set(f.warnings)):
            L.append(f"- Let op: {w}")
        if errs:
            L.append("- **FOUTEN**: " + "; ".join(errs))
        L += ["", *render_tree(body, flowname, base_txt), ""]
    L = [ln.replace("FLOW?postpurchase|RL3TU6", "v4 · Post-purchase (anders RL3TU6)") for ln in L]
    for sl, n in FLOW_NAMES.items():
        L = [ln.replace(f"FLOW?{sl}", n) for ln in L]
    with open(os.path.join(OUT_DIR, "OVERZICHT.md"), "w") as fh:
        fh.write("\n".join(L) + "\n")

    # ---- console
    print(f"{'flow':13s} acties mails splits ab fouten ontbrekend")
    for s, na, nm, ns, nab, ne, miss in summary:
        print(f"{s:13s} {na:6d} {nm:5d} {ns:6d} {nab:2d} {ne:6d} {len(miss)}")
        for e in built[s][2]:
            print("   FOUT:", e)
    print(f"\n{len(tm)} templates nog te exporteren; volgorde: {' > '.join(seq)}")
    print(f"-> {OUT_DIR}/<slug>.json en OVERZICHT.md")

    if not LIVE:
        return
    # ---- live: één flow
    if not ONLY or ONLY not in BUILDERS:
        sys.exit("--live vraagt --only=<slug>: " + ", ".join(seq))
    f, body, errs = built[ONLY]
    name = FLOW_NAMES[ONLY]
    if errs:
        sys.exit(f"Controle faalt voor {ONLY}: {errs}")
    if f.missing_templates:
        sys.exit(f"Niet aangemaakt: ontbrekend {sorted(f.missing_templates)}. Eerst exporteren (export_klaviyo.py).")
    blob = json.dumps(body)
    if "FLOW?" in blob:
        todo = sorted(set(re.findall(r"FLOW\?([a-z]+)", blob)))
        sys.exit(f"Niet aangemaakt: {name} verwijst naar flows zonder ID in exports/live/flows.csv: {todo}. "
                 f"Bouwvolgorde: {' > '.join(seq)}")
    for dep in f.deps - {ONLY}:
        fid = ctx.flow_ids.get(FLOW_NAMES[dep])
        got = None
        for _ in range(3) if fid else []:
            got = api("GET", f"flows/{fid}?fields%5Bflow%5D=name").get("data", {}).get("attributes", {}).get("name")
            if got: break
            time.sleep(3)
        if fid and got != FLOW_NAMES[dep]:
            sys.exit(f"flows.csv: {fid} heet in Klaviyo '{got}', verwacht '{FLOW_NAMES[dep]}'.")
    existing, _ = get_all("flows?fields[flow]=name,status&filter=contains(name,%22v4%20%C2%B7%22)")
    for fl in existing:
        if fl["attributes"]["name"] == name:
            extra = (" Dit is de oude checkout-draft met landsplit: verwijder of hernoem Y6yj2z eerst."
                     if fl["id"] in OBSOLETE_FLOW_IDS else "")
            sys.exit(f"Flow '{name}' bestaat al: {fl['id']} ({fl['attributes']['status']}). Niets aangemaakt.{extra}")
    res = api("POST", "flows", body)
    if "errors" in res:
        seen = set()
        for e in res["errors"]:
            k = (e.get("detail"), re.sub(r"/\d+", "/N", (e.get("source") or {}).get("pointer", "")))
            if k not in seen:
                seen.add(k)
                print(e.get("detail"), "@", (e.get("source") or {}).get("pointer"))
        sys.exit(1)
    fid = res["data"]["id"]
    print("aangemaakt:", name, fid, res["data"]["attributes"].get("status"))
    with open(os.path.join(ROOT, "exports/live/flows.csv"), "a") as fh:
        fh.write(f"{name},{fid}\n")


if __name__ == "__main__":
    main()
