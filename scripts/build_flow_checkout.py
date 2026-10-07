#!/usr/bin/env python3
"""Bouwt de flow 'v4 · Checkout abandonment' (plan v4 hoofdstuk 2.1) als Klaviyo-flowdefinitie.

Standaard: alleen de JSON schrijven naar exports/live/flow-checkout.json.
--live: de flow aanmaken via POST /api/flows. Klaviyo maakt hem aan als Draft; alle mails staan op draft.
Er gaat niets live en er wordt niets verstuurd.

Templates komen uit exports/live/templates.csv (export_klaviyo.py).
"""
import csv, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLOW_NAME = "v4 · Checkout abandonment"
REV = "2025-10-15"

# Metrics en flows (v4-flow-system.md 1.1)
CHECKOUT_STARTED = "RfMvni"
PLACED_ORDER = "RSNxYV"
RECEIVED_EMAIL = "YkRM4Q"
POSTPURCHASE_FLOW = "RL3TU6"  # huidige post-purchase; vervangen door v4 · Post-purchase zodra die bestaat

KOOK_TITELS = [
    "Titanium Hammered Pan Pro Standard", "Titanium Hammered Pan Pro Large", "Titanium Hammered Pan Pro Small",
    "Titanium Hammered Pan Pro Mini", "Titanium Pan Pro", "Titanium Hammered Deep Pan Pro",
    "Titanium Hammered Wok Pan Pro", "Titanium Hammered Crêpe Pan Pro", "Titanium Hammered Pizza Steel",
    "Titanium Hammered Roasting Pan", "2 Litre Titanium Hammered Pot With Lid", "3 Litre Titanium Hammered Pot With Lid",
    "7,5 Litre Titanium Hammered Pot With Lid", "Pot Set With Lids 6-Pcs", "Titanium Hammered Pan Pro With Lid",
    "Titanium Hammered Pan Pro & Utensil Set", "Titanium Cook & Prep Bundle",
]
SET_TITELS = [
    "Titanium Hammered Pan Set With Lids | 6-Pcs", "Titanium Hammered Cookware Set | 12-Pcs",
    "Titanium Hammered Cookware Set Pro", "Titanium Hammered Complete Edition", "Titanium Hammered – Complete Edition",
    "Full Hammered Pro Edition", "The Just Everything Bundle | 34-Pcs", "2 Pans + 2 Lids",
    "Titanium Hammered Pan Pro Duo", "Titanium Hammered Pro Duo", "Titanium Hammered Pan Pro Kit",
    "12 pcs cookware set", "Titanium-Hammerpfannenset mit Deckel | 6-teilig",
]
PANPRO_TITELS = [
    "Titanium Hammered Pan Pro Standard", "Titanium Hammered Pan Pro Large", "Titanium Hammered Pan Pro Small",
    "Titanium Hammered Pan Pro Mini", "Titanium Pan Pro", "Titanium Hammered Pan Pro With Lid",
]

FROM_EMAIL = "send@siraatskitchen.com"
FROM_LABEL = "Siraat's Kitchen"
REPLY_TO = "support@siraatskitchen.com"
CODE_PREFIX = "CODE ·"  # cooldown-terugval uit plan 1.4: codemails heten "CODE · ..."

# Oud pad T01 = "New AB Checkout"-pad uit Y2TmNB (templates en wachttijden overgenomen)
OLD_PATH = [
    (("minutes", 10, None), "UD7QXp", "Old · Checkout 1", "Don’t leave these hanging", "You’re a click away from better kitchen tools"),
    (("days", 1, "08:30:00"), "TK3h6j", "Old · Checkout 2", "Join the Happy Chef Club", "Plus Your Questions Answered"),
    (("days", 1, None), "VPBrLr", "Old · Checkout 3", "We’ve cooked something for you!", "See Inside for Details"),
    (("days", 2, None), "UMURrd", "Old · Checkout 4", "One Click to Cooking Better for Life", "Checkout Your Cart"),
    (("days", 1, None), "RbaQfc", "Old · Checkout 5", "We Can’t Keep these Forever", "Your Cart & Discount Expires Tonight"),
]


def templates():
    t = {}
    with open(os.path.join(ROOT, "exports/live/templates.csv")) as f:
        for row in csv.reader(f):
            if len(row) >= 3 and row[1].startswith("v4 · Checkout abandonment · "):
                t[row[1].rsplit(" · ", 1)[1]] = row[2]
    return t


def manifest():
    m = {}
    with open(os.path.join(ROOT, "exports/manifest.csv")) as f:
        for r in csv.DictReader(f):
            if r["flow"] == "checkout":
                m[r["id"]] = r
    return m


# ---------- bouwstenen ----------
def metric_count(metric, op, value, timeframe, filters=None):
    return {"type": "profile-metric", "metric_id": metric, "measurement": "count",
            "measurement_filter": {"type": "numeric", "operator": op, "value": value},
            "timeframe_filter": timeframe, "metric_filters": filters}

FLOW_START = {"type": "date", "operator": "flow-start"}
ALLTIME = {"type": "date", "operator": "alltime"}
def last_days(n):
    return {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": n}

NO_ORDER_SINCE_START = metric_count(PLACED_ORDER, "equals", 0, FLOW_START)
HEEFT_GEKOCHT = metric_count(PLACED_ORDER, "greater-than", 0, ALLTIME)

def groups(*groups_):
    return {"condition_groups": [{"conditions": list(g)} for g in groups_]}

def items_any(titles):
    # één groep: condities binnen een groep zijn OF
    return [{"type": "metric-property", "metric_id": CHECKOUT_STARTED, "field": "Items",
             "filter": {"type": "list", "operator": "contains", "value": t}} for t in titles]

def value_cond(op, v):
    return {"type": "metric-property", "metric_id": CHECKOUT_STARTED, "field": "$value",
            "filter": {"type": "numeric", "operator": op, "value": v}}


class Flow:
    def __init__(self):
        self.actions = []
        self.n = 0

    def add(self, type_, data, links):
        self.n += 1
        aid = f"a{self.n:02d}"
        self.actions.append({"temporary_id": aid, "type": type_, "data": data, "links": links})
        return aid

    def link(self, aid, **links):
        for a in self.actions:
            if a["temporary_id"] == aid:
                a["links"].update(links)

    def delay(self, unit, value, until=None, nxt=None):
        d = {"unit": unit, "value": value, "secondary_value": None, "timezone": "profile"}
        if until:
            d["delay_until_time"] = until
        return self.add("time-delay", d, {"next": nxt})

    def email(self, name, template_id, subject, preview, utm_campaign, nxt=None, filters=True):
        msg = {"from_email": FROM_EMAIL, "from_label": FROM_LABEL, "reply_to_email": REPLY_TO,
               "cc_email": None, "bcc_email": None, "subject_line": subject, "preview_text": preview,
               "template_id": template_id, "smart_sending_enabled": False, "transactional": False,
               "add_tracking_params": True,
               "custom_tracking_params": [
                   {"param": "utm_source", "value": "klaviyo"},
                   {"param": "utm_medium", "value": "email"},
                   {"param": "utm_campaign", "value": utm_campaign}],
               "additional_filters": groups([NO_ORDER_SINCE_START]) if filters else None,
               "name": name}
        return self.add("send-email", {"message": msg, "status": "draft"}, {"next": nxt})

    def cs(self, filt, yes=None, no=None):
        return self.add("conditional-split", {"profile_filter": filt}, {"next_if_true": yes, "next_if_false": no})

    def ts(self, filt, yes=None, no=None):
        return self.add("trigger-split", {"trigger_filter": filt, "trigger_id": CHECKOUT_STARTED,
                                          "trigger_type": "metric", "trigger_subtype": None},
                        {"next_if_true": yes, "next_if_false": no})

    def update(self, props, nxt=None):
        ops = [{"operator": "update", "property_type": "string", "property_key": f"properties['{k}']",
                "property_value": v} for k, v in props.items()]
        return self.add("update-profile", {"profile_operations": ops, "status": "draft"}, {"next": nxt})


def cs_metric(op, v, days, filt=None):
    """Checkout Started-telling in de laatste N dagen (vangt het trigger-event)."""
    return metric_count(CHECKOUT_STARTED, op, v, last_days(days), filt)

def f_items(titles):
    return [{"property": "Items", "filter": {"type": "list", "operator": "contains-any", "value": titles}}]

def f_value(op, v):
    return [{"property": "$value", "filter": {"type": "numeric", "operator": op, "value": v}}]

COUNTRY_US = {"type": "profile-property", "property": "location['country']",
              "filter": {"type": "string", "operator": "equals", "value": "United States"}}
COUNTRY_NOT_US = {"type": "profile-property", "property": "location['country']",
                  "filter": {"type": "string", "operator": "not-equals", "value": "United States"}}
COUNTRY_SET = {"type": "profile-property", "property": "location['country']",
               "filter": {"type": "existence", "operator": "is-set"}}
COUNTRY_NOT_SET = {"type": "profile-property", "property": "location['country']",
                   "filter": {"type": "existence", "operator": "is-not-set"}}
LOCALE_US = [{"property": "Customer Locale", "filter": {"type": "string", "operator": "equals", "value": "en-US"}}]


def build():
    """Eén rechte lijn zonder samenkomende takken (Klaviyo staat dat niet toe).
    Categorie en land zitten als verzendfilter op de mail zelf; per profiel komt er
    precies één mail per stap door. Echte splits alleen voor T01, cooldown en T02."""
    T, M = templates(), manifest()
    missing = [k for k in ["c1", "c2", "c2-acc", "c3-acc", "c3-p", "c3-s", "c4-us", "c4-us-nocode", "c4-int", "c4-int-nocode"] if k not in T]
    if missing:
        sys.exit(f"Templates ontbreken in exports/live/templates.csv: {missing}")

    f = Flow()
    KOOK = KOOK_TITELS + SET_TITELS
    NEW_CUSTOMER = metric_count(PLACED_ORDER, "equals", 0, ALLTIME)

    def mail(mid, name, nxt, *extra_groups):
        r = M[mid]
        a = f.email(name, T[mid], r["onderwerp_a"], r["preview"], "v4-checkout", nxt)
        msg = f.actions[-1]["data"]["message"]
        msg["additional_filters"]["condition_groups"] += [{"conditions": list(g)} for g in extra_groups]
        return a

    # Land (plan 2.1 stap 5K): US = land US, of geen land en Customer Locale en-US. Anders INT.
    # Met splits, want "land is niet US" sluit profielen zonder land uit. Geen samenkomende takken,
    # dus de code-router staat er vier keer (US, INT, en twee keer voor profielen zonder land).
    cooldown = metric_count(RECEIVED_EMAIL, "greater-than", 0, last_days(30),
                            [{"property": "Campaign Name", "filter": {"type": "string", "operator": "contains", "value": CODE_PREFIX}}])

    def router(land, tag=""):
        L = land.upper()
        code = mail(f"c4-{land}", f"{CODE_PREFIX} C4-{L}{tag}", None)
        b_ = mail(f"c4-{land}-nocode", f"C4-{L}{tag} nocode · T02-B", None)
        cd = mail(f"c4-{land}-nocode", f"C4-{L}{tag} nocode · cooldown", None)
        t02 = f.cs(groups([{"type": "profile-sample", "percentage": 50}]), yes=code, no=b_)
        return f.cs(groups([cooldown]), yes=cd, no=t02)

    locale = f.ts(groups([{"type": "metric-property", "metric_id": CHECKOUT_STARTED, "field": "Customer Locale",
                           "filter": {"type": "string", "operator": "equals", "value": "en-US"}}]),
                  yes=router("us", " (geen land)"), no=router("int", " (geen land)"))
    has_country = f.cs(groups([COUNTRY_SET]), yes=router("int"), no=locale)
    land = f.cs(groups([COUNTRY_US]), yes=router("us"), no=has_country)
    d5 = f.delay("days", 2, "09:00:00", nxt=land)  # dag 5, 09:00

    # Dag 3: C3-S, C3-P of C3-ACC (hoogstens één komt door)
    c3acc = mail("c3-acc", "C3-ACC", d5, [cs_metric("equals", 0, 4, f_items(KOOK))], [NEW_CUSTOMER])
    c3p = mail("c3-p", "C3-P", c3acc,
               [cs_metric("greater-than", 0, 4, f_items(PANPRO_TITELS))],
               [cs_metric("greater-than", 0, 4, f_value("less-than", 250))],
               [cs_metric("equals", 0, 4, f_items(SET_TITELS))],
               [cs_metric("equals", 0, 4, f_value("greater-than-or-equal", 300))])
    c3s = mail("c3-s", "C3-S", c3p,
               [cs_metric("greater-than", 0, 4, f_items(SET_TITELS)),
                cs_metric("greater-than", 0, 4, f_value("greater-than-or-equal", 300))])
    d3 = f.delay("days", 2, "09:00:00", nxt=c3s)  # dag 3, 09:00

    # Dag 1: C2 (kookgerei, nieuwe klant) of C2-ACC (accessoire)
    c2acc = mail("c2-acc", "C2-ACC", d3, [cs_metric("equals", 0, 2, f_items(KOOK))])
    c2 = mail("c2", "C2", c2acc, [cs_metric("greater-than", 0, 2, f_items(KOOK))], [NEW_CUSTOMER])
    d2 = f.delay("days", 1, nxt=c2)  # 24 uur na C1

    c1 = mail("c1", "C1", d2)
    arm_new = f.delay("minutes", 30, nxt=c1)

    # Oud pad (T01 arm old)
    nxt = None
    for (unit, val, until), tid, name, subj, prev in reversed(OLD_PATH):
        e = f.email(name, tid, subj, prev, "old-checkout", nxt=nxt)
        nxt = f.delay(unit, val, until, nxt=e)
    arm_old = nxt

    t01 = f.cs(groups([{"type": "profile-sample", "percentage": 50}]), yes=arm_new, no=arm_old)

    definition = {
        "triggers": [{"type": "metric", "id": CHECKOUT_STARTED,
                      "trigger_filter": groups([value_cond("greater-than", 0)])}],
        "profile_filter": groups(
            [NO_ORDER_SINCE_START],
            [{"type": "profile-not-in-flow", "timeframe_filter": last_days(14)}],
            [metric_count(RECEIVED_EMAIL, "equals", 0, last_days(7),
                          [{"property": "$flow", "filter": {"type": "string", "operator": "equals", "value": POSTPURCHASE_FLOW}}])],
        ),
        "actions": f.actions,
        "entry_action_id": t01,
        "reentry_criteria": {"duration": 14, "unit": "day"},
    }
    return {"data": {"type": "flow", "attributes": {"name": FLOW_NAME, "definition": definition}}}



def api(method, path, body=None):
    cmd = ["curl", "-sS", "-g", "-X", method, f"https://a.klaviyo.com/api/{path}", "-H", f"revision: {REV}",
           "-H", "accept: application/vnd.api+json", "-H", "content-type: application/vnd.api+json"]
    if body is not None:
        cmd += ["--data-binary", "@-"]
    out = subprocess.run(cmd, input=json.dumps(body) if body is not None else None, capture_output=True, text=True)
    return json.loads(out.stdout or "{}")


def main():
    body = build()
    out = os.path.join(ROOT, "exports/live/flow-checkout.json")
    with open(out, "w") as fh:
        json.dump(body, fh, indent=1, ensure_ascii=False)
    acts = body["data"]["attributes"]["definition"]["actions"]
    print(f"{len(acts)} acties, {sum(a['type'] == 'send-email' for a in acts)} mails -> {out}")
    if "--live" not in sys.argv:
        return
    existing = api("GET", "flows?fields[flow]=name&sort=-created&page[size]=50")
    for fl in existing.get("data", []):
        if fl["attributes"]["name"] == FLOW_NAME:
            sys.exit(f"Flow bestaat al: {fl['id']}. Niets aangemaakt.")
    res = api("POST", "flows", body)
    if "errors" in res:
        seen = set()
        for e in res["errors"]:
            k = (e.get("detail"), __import__("re").sub(r"/\d+", "/N", e.get("source", {}).get("pointer", "")))
            if k not in seen:
                seen.add(k)
                print(e.get("detail"), "@", e.get("source", {}).get("pointer"))
        sys.exit(1)
    fid = res["data"]["id"]
    print("aangemaakt:", fid, res["data"]["attributes"].get("status"))
    with open(os.path.join(ROOT, "exports/live/flows.csv"), "a") as fh:
        fh.write(f"{FLOW_NAME},{fid}\n")


if __name__ == "__main__":
    main()
