"""Hoofdflow (DRAFT) 'PP viewed tailored · VIP15 (draft, 19 nov)'. python3 -I _tools/flow_tailored.py [--dry]
Trigger Placed Order; niet in deze flow in 30 dagen; wacht 2 dagen tot 09:00 (profieltijd);
VS (profiel-locatie, zoals split 119850671 in T4a5Mk): geen 12-Pcs/34-Pcs ooit besteld -> mail (12-Pcs hero);
niet-VS: geen 6-Pcs/12-Pcs/34-Pcs/Full Hammered Pro ooit -> mail (6-Pcs hero);
anders alleen mailen als er in 30 dagen een aanbiedbaar product bekeken is. Mailfilter: geen mail uit X3ySuU in 1 dag.
De mail zelf kiest hero en kaarten (ppv-tailored.html)."""
import sys, os, json
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive'); sys.path.insert(0, os.path.dirname(__file__))
from kl import api
from ppv_catalog import VIEW_MATCH
D = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tailored'))
PLACED, VIEWED, ORDERED, RECEIVED = 'RSNxYV', 'XNtYMB', 'XT7f8Z', 'YkRM4Q'
TID = open(os.path.join(D, 'template-id.txt')).read().strip()
ALL = {"type": "date", "operator": "alltime"}; L30 = {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 30}
L1 = {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 1}
def metric(mid, op, val, tf, mf): return {"type": "profile-metric", "metric_id": mid, "measurement": "count", "measurement_filter": {"type": "numeric", "operator": op, "value": val}, "timeframe_filter": tf, "metric_filters": mf}
def nm(op, v, prop='Name'): return [{"property": prop, "filter": {"type": "string", "operator": op, "value": v}}]
US = {"conditions": [{"type": "profile-property", "property": "location['country']", "filter": {"type": "string", "operator": "equals", "value": v}} for v in ("United States", "US")]}
def never(frag): return {"conditions": [metric(ORDERED, 'equals', 0, ALL, nm('contains', frag))]}
def split(tid, groups, t, f): return {"temporary_id": tid, "type": "conditional-split", "data": {"profile_filter": {"condition_groups": groups}}, "links": {"next_if_true": t, "next_if_false": f}}
VM = [ms[0] for k, ms in VIEW_MATCH if k != 's12']
VCH = [VM[i:i + 6] for i in range(0, len(VM), 6)]
def mail(tid, label):
    return {"temporary_id": tid, "type": "send-email", "links": {"next": None}, "data": {"status": "draft", "message": {
    "name": "PPV tailored · VIP15 · " + label, "from_email": "send@siraatskitchen.com", "from_label": "Siraat's Kitchen", "reply_to_email": "support@siraatskitchen.com",
    "cc_email": None, "bcc_email": None, "subject_line": "15% off, once, as a thank-you", "preview_text": "Your order is on its way. Here is 15% off, once, until Monday, Nov 30.",
    "template_id": TID, "smart_sending_enabled": False, "transactional": False, "add_tracking_params": False,
    "additional_filters": {"condition_groups": [{"conditions": [metric(RECEIVED, 'equals', 0, L1, nm('equals', 'X3ySuU', '$flow'))]}]}}}}
VIEWED_ANY = {"conditions": [metric(VIEWED, 'greater-than', 0, L30, nm(*ms[0])) for k, ms in VIEW_MATCH if k != 's12']}
# Klaviyo-flows zijn bomen (een actie heeft één ouder), daarom drie keer dezelfde mail (zelfde template) op drie paden.
actions = [
    {"temporary_id": "delay", "type": "time-delay", "data": {"unit": "days", "value": 2, "secondary_value": None, "timezone": "profile", "delay_until_time": "09:00:00"}, "links": {"next": "s-viewed"}},
    split("s-viewed", [VIEWED_ANY], "mail-v", "s-us"),
    mail("mail-v", "bekeek iets"),
    split("s-us", [US], "s-us-hero", "s-int-hero"),
    split("s-us-hero", [never('12-Pcs'), never('34-Pcs')], "mail-us", None),
    mail("mail-us", "VS, alleen 12-Pcs"),
    split("s-int-hero", [never('6-Pcs'), never('12-Pcs'), never('34-Pcs'), never('Full Hammered Pro')], "mail-int", None),
    mail("mail-int", "niet-VS, alleen 6-Pcs")]
body = {"data": {"type": "flow", "attributes": {"name": "PP viewed tailored · VIP15 (draft, 19 nov)", "definition": {
    "triggers": [{"type": "metric", "id": PLACED, "trigger_filter": None}],
    "profile_filter": {"condition_groups": [{"conditions": [{"type": "profile-not-in-flow", "timeframe_filter": L30}]}]},
    "actions": actions, "entry_action_id": "delay", "reentry_criteria": {"duration": 30, "unit": "day"}}}}}
json.dump(body, open(os.path.join(D, 'flow-definition.json'), 'w'), indent=1, ensure_ascii=False)
if '--dry' in sys.argv: sys.exit()
d = api('POST', '/api/flows/', body)
if 'data' in d:
    fid = d['data']['id']; open(os.path.join(D, 'flow-id.txt'), 'w').write(fid + '\n'); print('flow', fid, d['data']['attributes'].get('status'))
else: print(json.dumps(d)[:1500])
