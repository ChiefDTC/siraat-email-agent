"""Maakt de DRAFT-flow 'PP set upsell VIP15' (19 nov 2026, v2 na wijziging Floris: alleen sets). Niets live, alle mails status draft.
python3 -I _tools/flow.py [--dry]   (vanuit de map post-purchase-viewed). Schrijft flow-definition.json en flow-id.txt.
Logica na 2 dagen (09:00):
  heeft 12-Pcs ooit besteld -> einde
  VS (location['country'] = United States/US, zoals split 119850671 in T4a5Mk):
     heeft 6-Pcs ooit besteld -> 12-Pcs (pad A)
     bekeek 6-Pcs (30 d) EN niet 12-Pcs (30 d) -> 6-Pcs (pad B)
     anders -> 12-Pcs (pad C, ook zonder bekeken product)
  niet-VS: heeft 6-Pcs -> einde, anders -> 6-Pcs (pad D)
Elk pad: mail 1, 2 dagen wachten (09:00), mail 2 (herinnering)."""
import sys, json, os
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api
D = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ids = json.load(open(os.path.join(D, 'klaviyo-template-ids.json')))
PLACED, VIEWED, ORDERED, RECEIVED = 'RSNxYV', 'XNtYMB', 'XT7f8Z', 'YkRM4Q'
N12, N6 = ('contains', 'Cookware Set | 12-Pcs'), ('contains', 'Pan Set With Lids | 6-Pcs')
ITEMS = {'set12': ['Titanium Hammered Cookware Set | 12-Pcs', 'Titanium Hammered Cookware Set | 12-Pcs | + FREE PIZZA STEEL', 'Titanium Hammered Cookware Set | 12-Pcs | + FREE PIZZA STEEL (EXCLUSIVE)'],
         'set6': ['Titanium Hammered Pan Set With Lids | 6-Pcs']}
NAME = {'set12': N12, 'set6': N6}
ALL = {"type": "date", "operator": "alltime"}
L30 = {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 30}
L1 = {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 1}
FS = {"type": "date", "operator": "flow-start"}
def metric(mid, op, val, tf, mf=None):
    return {"type": "profile-metric", "metric_id": mid, "measurement": "count", "measurement_filter": {"type": "numeric", "operator": op, "value": val}, "timeframe_filter": tf, "metric_filters": mf}
def nm(n, prop='Name'): return [{"property": prop, "filter": {"type": "string", "operator": n[0], "value": n[1]}}]
US = {"conditions": [{"type": "profile-property", "property": "location['country']", "filter": {"type": "string", "operator": "equals", "value": v}} for v in ("United States", "US")]}
G = lambda *c: {"condition_groups": [{"conditions": [x]} if not isinstance(x, dict) or 'conditions' not in x else x for x in c]}
NO_PP = metric(RECEIVED, 'equals', 0, L1, nm(('equals', 'X3ySuU'), '$flow'))
SUBJ = {'set12-m1': ("Here's the rest of the kitchen", 'Your order is on its way. 15% off the 12-piece set, once, until Nov 30.'),
        'set12-m2': ('Your VIP15 code ends Monday, Nov 30', '15% off the 12-piece set, one use. At 11:59 PM ET it stops working.'),
        'set6-m1': ('Three pans, three lids, 15% off', 'Your order is on its way. 15% off the 6-piece set, once, until Nov 30.'),
        'set6-m2': ('Your VIP15 code ends Monday, Nov 30', '15% off the 6-piece set, one use. At 11:59 PM ET it stops working.')}
def mail(tid, key, path, nxt):
    s, pv = SUBJ[key]; prod = key.split('-')[0]
    filt = [{"conditions": [metric(ORDERED, 'equals', 0, ALL, nm(NAME[prod]))]}, {"conditions": [NO_PP]}]
    if key.endswith('m2'):
        filt.insert(1, {"conditions": [metric(PLACED, 'equals', 0, FS, [{"property": "Items", "filter": {"type": "list", "operator": "contains-any", "value": ITEMS[prod]}}])]})
    return {"temporary_id": tid, "type": "send-email", "links": {"next": nxt}, "data": {"status": "draft", "message": {
        "name": f"PPS {path} {key.upper()}", "from_email": "send@siraatskitchen.com", "from_label": "Siraat's Kitchen", "reply_to_email": "support@siraatskitchen.com",
        "cc_email": None, "bcc_email": None, "subject_line": s, "preview_text": pv, "template_id": ids[key],
        "smart_sending_enabled": False, "transactional": False, "add_tracking_params": False, "additional_filters": {"condition_groups": filt}}}}
def path(p, prod):
    return [mail(f"{p}-m1", f"{prod}-m1", p, f"{p}-wait"),
            {"temporary_id": f"{p}-wait", "type": "time-delay", "data": {"unit": "days", "value": 2, "secondary_value": None, "timezone": "profile", "delay_until_time": "09:00:00"}, "links": {"next": f"{p}-m2"}},
            mail(f"{p}-m2", f"{prod}-m2", p, None)]
def split(tid, groups, t, f):
    return {"temporary_id": tid, "type": "conditional-split", "data": {"profile_filter": {"condition_groups": groups}}, "links": {"next_if_true": t, "next_if_false": f}}
actions = [
    {"temporary_id": "delay", "type": "time-delay", "data": {"unit": "days", "value": 2, "secondary_value": None, "timezone": "profile", "delay_until_time": "09:00:00"}, "links": {"next": "s-has12"}},
    split("s-has12", [{"conditions": [metric(ORDERED, 'greater-than', 0, ALL, nm(N12))]}], None, "s-us"),
    split("s-us", [US], "s-us-has6", "s-int-has6"),
    split("s-us-has6", [{"conditions": [metric(ORDERED, 'greater-than', 0, ALL, nm(N6))]}], "A-m1", "s-viewed6"),
    split("s-viewed6", [{"conditions": [metric(VIEWED, 'greater-than', 0, L30, nm(N6))]}, {"conditions": [metric(VIEWED, 'equals', 0, L30, nm(N12))]}], "B-m1", "C-m1"),
    split("s-int-has6", [{"conditions": [metric(ORDERED, 'greater-than', 0, ALL, nm(N6))]}], None, "D-m1"),
] + path('A', 'set12') + path('B', 'set6') + path('C', 'set12') + path('D', 'set6')
defn = {"triggers": [{"type": "metric", "id": PLACED, "trigger_filter": None}],
        "profile_filter": {"condition_groups": [{"conditions": [{"type": "profile-not-in-flow", "timeframe_filter": L30}]}]},
        "actions": actions, "entry_action_id": "delay", "reentry_criteria": {"duration": 30, "unit": "day"}}
body = {"data": {"type": "flow", "attributes": {"name": "PP set upsell · VIP15 (draft, 19 nov)", "definition": defn}}}
json.dump(body, open(os.path.join(D, 'flow-definition.json'), 'w'), indent=1, ensure_ascii=False)
if '--dry' in sys.argv: print('dry'); sys.exit()
d = api('POST', '/api/flows/', body)
if 'data' in d:
    fid = d['data']['id']; open(os.path.join(D, 'flow-id.txt'), 'w').write(fid + '\n'); print('flow', fid, d['data']['attributes'].get('status'))
else:
    print(json.dumps(d)[:1500])
