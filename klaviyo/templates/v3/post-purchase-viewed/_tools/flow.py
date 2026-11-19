"""Maakt de DRAFT-flow 'PP viewed upsell VIP15' (19 nov 2026). Niets live, alle mails status draft.
python3 -I _tools/flow.py [--dry]   (vanuit de map post-purchase-viewed). Schrijft flow-definition.json en flow-id.txt."""
import sys, json, os
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api
D = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ids = json.load(open(os.path.join(D, 'klaviyo-template-ids.json')))
VIEWED, ORDERED, RECEIVED = 'XNtYMB', 'XT7f8Z', 'YkRM4Q'
US_COND = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {"type": "profile-region", "in_region": True, "region": "united_states"}
# (sleutel, onderwerp, preview, Name-filter viewed, Name-filter ordered)
P = [('set12', 'Still thinking about the 12-piece set?', 'Your order is on its way. Here is 15% off the set you looked at, once.', ('contains', 'Cookware Set | 12-Pcs')),
     ('set6', 'Still thinking about the 6-piece set?', 'Your order is on its way. Here is 15% off the set you looked at, once.', ('contains', 'Pan Set With Lids | 6-Pcs')),
     ('deep', 'Still thinking about the Deep Pan?', 'Your order is on its way. Here is 15% off the Deep Pan, once.', ('equals', 'Titanium Hammered Deep Pan Pro')),
     ('large', 'Still thinking about the 12-inch pan?', 'Your order is on its way. Here is 15% off the Pan Pro Large, once.', ('equals', 'Titanium Hammered Pan Pro Large'))]
def metric(mid, op, val, tf, name=None, prop='Name'):
    return {"type": "profile-metric", "metric_id": mid, "measurement": "count",
            "measurement_filter": {"type": "numeric", "operator": op, "value": val}, "timeframe_filter": tf,
            "metric_filters": None if name is None else [{"property": prop, "filter": {"type": "string", "operator": name[0], "value": name[1]}}]}
ALL = {"type": "date", "operator": "alltime"}
L30 = {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 30}
L1 = {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 1}
actions = [{"temporary_id": "delay", "type": "time-delay", "data": {"unit": "days", "value": 2, "secondary_value": None, "timezone": "profile", "delay_until_time": "09:00:00"}, "links": {"next": "split-set12"}}]
for i, (k, subj, prev, nm) in enumerate(P):
    groups = [{"conditions": [metric(VIEWED, 'greater-than', 0, L30, nm)]}, {"conditions": [metric(ORDERED, 'equals', 0, ALL, nm)]}]
    if k == 'set12': groups.append({"conditions": [US_COND]})
    nxt = P[i + 1][0] if i + 1 < len(P) else None
    actions.append({"temporary_id": f"split-{k}", "type": "conditional-split", "data": {"profile_filter": {"condition_groups": groups}},
                    "links": {"next_if_true": f"mail-{k}", "next_if_false": f"split-{nxt}" if nxt else None}})
    actions.append({"temporary_id": f"mail-{k}", "type": "send-email", "links": {"next": None}, "data": {"status": "draft", "message": {
        "name": f"PPV-{k.upper()} VIP15", "from_email": "send@siraatskitchen.com", "from_label": "Siraat's Kitchen", "reply_to_email": "support@siraatskitchen.com",
        "cc_email": None, "bcc_email": None, "subject_line": subj, "preview_text": prev, "template_id": ids[k],
        "smart_sending_enabled": False, "transactional": False, "add_tracking_params": False,
        "additional_filters": {"condition_groups": [{"conditions": [metric(ORDERED, 'equals', 0, ALL, nm)]},
                                                    {"conditions": [metric(RECEIVED, 'equals', 0, L1, ('equals', 'X3ySuU'), prop='$flow')]}]}}}})
defn = {"triggers": [{"type": "metric", "id": "RSNxYV", "trigger_filter": None}],
        "profile_filter": {"condition_groups": [{"conditions": [{"type": "profile-not-in-flow", "timeframe_filter": L30}]}]},
        "actions": actions, "entry_action_id": "delay", "reentry_criteria": {"duration": 30, "unit": "day"}}
body = {"data": {"type": "flow", "attributes": {"name": "PP viewed upsell · VIP15 (draft, 19 nov)", "definition": defn}}}
json.dump(body, open(os.path.join(D, 'flow-definition.json'), 'w'), indent=1, ensure_ascii=False)
if '--dry' in sys.argv: print('dry'); sys.exit()
d = api('POST', '/api/flows/', body)
if 'data' in d:
    fid = d['data']['id']; open(os.path.join(D, 'flow-id.txt'), 'w').write(fid + '\n'); print('flow', fid, d['data']['attributes'].get('status'))
else:
    print(json.dumps(d)[:1500])
