"""Tracker-flows (DRAFT) voor PP viewed tailored. Zetten profieleigenschappen ppv_vr_<key> (getal) die de mail leest.
  python3 -I _tools/trackers.py [--dry]   -> tailored/tracker-viewed.json, tailored/tracker-owned.json, tailored/tracker-ids.json
Viewed (trigger Viewed Product XNtYMB, elk event):  per product: is ppv_vr == 9 (in bezit)? dan niets. Anders 1;
  na 73 uur 2 (als er sindsdien geen nieuwere view is en het nog niet in bezit is), na nog 169 uur 3, na nog 481 uur 0.
  Een nieuwere view start een eigen pad, dus het oudere pad stopt bij de controle.
Owned (trigger Ordered Product XT7f8Z, elke orderregel, ook Aftersell-regels): zet 9 op het product en alles wat in die bundel zit.
Klaviyo staat in Update Profile alleen vaste waarden toe (geen datum uit het event) en alleen bestaande eigenschappen;
daarom emmers in plaats van datums, en het schema-profiel zz-ppv-schema-20261119 (geen e-mail) dat de eigenschappen aanmaakt."""
import sys, os, json
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive'); sys.path.insert(0, os.path.dirname(__file__))
from kl import api
from ppv_catalog import VIEW_MATCH, OWN_MATCH
D = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tailored'))
VIEWED, ORDERED = 'XNtYMB', 'XT7f8Z'
def L(n): return {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": n}
def nmf(m): return [{"property": "Name", "filter": {"type": "string", "operator": m[0], "value": m[1]}}]
def upd(tid, key, val, nxt=None):
    return {"temporary_id": tid, "type": "update-profile", "data": {"status": "draft", "profile_operations": [
        {"operator": "update", "property_type": "numeric", "property_key": f"properties['ppv_vr_{k}']", "property_value": val} for k in ([key] if isinstance(key, str) else key)]}, "links": {"next": nxt}}
def prop(key, op, v): return {"type": "profile-property", "property": f"properties['ppv_vr_{key}']", "filter": {"type": "numeric", "operator": op, "value": v}}
def split(tid, groups, t, f): return {"temporary_id": tid, "type": "conditional-split", "data": {"profile_filter": {"condition_groups": groups}}, "links": {"next_if_true": t, "next_if_false": f}}
def tsplit(tid, metric, m, t, f):
    return {"temporary_id": tid, "type": "trigger-split", "data": {"trigger_filter": {"condition_groups": [{"conditions": [
        {"type": "metric-property", "metric_id": metric, "field": "Name", "filter": {"type": "string", "operator": m[0], "value": m[1]}}]}]},
        "trigger_id": metric, "trigger_type": "metric", "trigger_subtype": None}, "links": {"next_if_true": t, "next_if_false": f}}
def delay(tid, h, nxt): return {"temporary_id": tid, "type": "time-delay", "data": {"unit": "hours", "value": h, "secondary_value": None, "timezone": "profile", "delay_until_time": None, "delay_until_weekdays": None}, "links": {"next": nxt}}
def noview(m, days): return {"type": "profile-metric", "metric_id": VIEWED, "measurement": "count", "measurement_filter": {"type": "numeric", "operator": "equals", "value": 0}, "timeframe_filter": L(days), "metric_filters": nmf(m)}

def viewed_flow():
    acts = []; vm = [(k, ms[0]) for k, ms in VIEW_MATCH if k != 's12']
    for i, (k, m) in enumerate(vm):
        nxt = f"t{i+1}" if i + 1 < len(vm) else None
        acts.append(tsplit(f"t{i}", VIEWED, m, f"{k}-own", nxt))
        acts.append(split(f"{k}-own", [{"conditions": [prop(k, 'equals', 9)]}], None, f"{k}-u1"))
        acts.append(upd(f"{k}-u1", k, 1, f"{k}-d1"))
        for st, (h, days, val) in enumerate([(73, 3, 2), (169, 10, 3), (481, 30, 0)], 1):
            acts.append(delay(f"{k}-d{st}", h, f"{k}-c{st}"))
            acts.append(split(f"{k}-c{st}", [{"conditions": [noview(m, days)]}, {"conditions": [prop(k, 'not-equals', 9)]}], f"{k}-u{st+1}", None))
            acts.append(upd(f"{k}-u{st+1}", k, val, f"{k}-d{st+1}" if st < 3 else None))
    return {"data": {"type": "flow", "attributes": {"name": "PPV tracker · Viewed Product > ppv_vr (draft, 19 nov)", "definition": {
        "triggers": [{"type": "metric", "id": VIEWED, "trigger_filter": None}], "profile_filter": None, "actions": acts, "entry_action_id": "t0"}}}}

def owned_flow():
    acts = []
    for i, (frag, keys) in enumerate(OWN_MATCH):
        nxt = f"t{i+1}" if i + 1 < len(OWN_MATCH) else None
        acts.append(tsplit(f"t{i}", ORDERED, ('contains', frag), f"u{i}", nxt))
        acts.append(upd(f"u{i}", sorted(set(keys)), 9))
    return {"data": {"type": "flow", "attributes": {"name": "PPV tracker · Ordered Product > ppv_vr = 9 (draft, 19 nov)", "definition": {
        "triggers": [{"type": "metric", "id": ORDERED, "trigger_filter": None}], "profile_filter": None, "actions": acts, "entry_action_id": "t0"}}}}

if __name__ == '__main__':
    out = {}
    for name, body in (('viewed', viewed_flow()), ('owned', owned_flow())):
        json.dump(body, open(os.path.join(D, f'tracker-{name}.json'), 'w'), indent=1, ensure_ascii=False)
        print(name, len(body['data']['attributes']['definition']['actions']), 'acties')
        if '--dry' in sys.argv: continue
        d = api('POST', '/api/flows/', body)
        if 'data' in d: out[name] = d['data']['id']; print(name, d['data']['id'], d['data']['attributes'].get('status'))
        else: print(name, json.dumps(d)[:800])
    if out: json.dump(out, open(os.path.join(D, 'tracker-ids.json'), 'w'), indent=1)
