"""Maakt de DRAFT-flow 'v5 · Post-purchase + delivery (draft)' via POST /api/flows/ (revision 2025-10-15). Alle mails status draft,
flow status draft. Raakt X3ySuU, VQ93sx, UUZr3e en R9dcdY niet aan. python3 -I _tools/flow.py [--dry]"""
import os, sys, json, copy
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../..'))
IDS = json.load(open(os.path.join(ROOT, 'klaviyo-template-ids.json')))
META = json.load(open(os.path.join(ROOT, 'out/meta.json')))
LIVE = json.load(open('/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/ppv5/flow-X3ySuU.json'))['data']['attributes']['definition']
UUZ = json.load(open(os.path.join(REPO, 'klaviyo/templates/v3/post-purchase-viewed/tailored/flow-definition.json')))
UUZ = UUZ.get('data', UUZ); UUZ = UUZ.get('attributes', UUZ).get('definition', UUZ)
PO, RECV, REFUND, DELIV, ORDP = 'RSNxYV', 'YkRM4Q', 'Xg6cwn', 'VcUF33', 'XT7f8Z'
def pm(mid, op, val, tf, mf=None):
    return {'type': 'profile-metric', 'metric_id': mid, 'measurement': 'count', 'measurement_filter': {'type': 'numeric', 'operator': op, 'value': val}, 'timeframe_filter': tf, 'metric_filters': mf}
last = lambda d: {'type': 'date', 'operator': 'in-the-last', 'unit': 'day', 'quantity': d}
ALLT, START = {'type': 'date', 'operator': 'alltime'}, {'type': 'date', 'operator': 'flow-start'}
paid = lambda d: [pm(PO, 'greater-than', 0, last(d), [{'property': '$value', 'filter': {'type': 'numeric', 'operator': 'greater-than', 'value': 0.0}}])]
# pankopers: dezelfde Items-lijst als live P2-SAFE (X3ySuU 119850554)
p2safe = next(a for a in LIVE['actions'] if a['type'] == 'send-email' and a['data']['message']['name'] == 'P2-SAFE')['data']['message']['additional_filters']
PAN_ITEMS = p2safe['condition_groups'][0]['conditions'][0]['metric_filters']
pan = lambda d: [pm(PO, 'greater-than', 0, last(d), PAN_ITEMS)]
VIEWED = next(a for a in UUZ['actions'] if a.get('temporary_id', a.get('id')) == 's-viewed')['data']['profile_filter']['condition_groups'][0]['conditions']
own = lambda frag: pm(ORDP, 'equals', 0, ALLT, [{'property': 'Name', 'filter': {'type': 'string', 'operator': 'contains', 'value': frag}}])
nomail = lambda flow: pm(RECV, 'equals', 0, last(30), [{'property': '$flow', 'filter': {'type': 'string', 'operator': 'equals', 'value': flow}}])
name_has = lambda s, d=30: pm(RECV, 'equals', 0, last(d), [{'property': 'Campaign Name', 'filter': {'type': 'string', 'operator': 'contains', 'value': s}}])
G = lambda *conds: {'conditions': list(conds)}

def email(tid, key, name, groups):
    return {'temporary_id': tid, 'type': 'send-email', 'data': {'status': 'draft', 'message': {
        'name': name, 'from_email': 'send@siraatskitchen.com', 'from_label': "Siraat's Kitchen", 'reply_to_email': 'support@siraatskitchen.com',
        'cc_email': None, 'bcc_email': None, 'subject_line': META[key]['subject'], 'preview_text': META[key]['preview'], 'template_id': IDS[key],
        'smart_sending_enabled': False, 'transactional': False, 'add_tracking_params': False, 'additional_filters': {'condition_groups': groups}}}}
def delay(tid, val, unit='days', at='09:00:00'):
    d = {'unit': unit, 'value': val, 'secondary_value': None, 'timezone': 'profile'}
    if at: d['delay_until_time'] = at
    return {'temporary_id': tid, 'type': 'time-delay', 'data': d}

A = [
 delay('d0', 1, 'hours', None),
 email('pp1f', 'pp1-first', 'PP v5 · PP1-FIRST', [G(pm(PO, 'equals', 1, ALLT)), G(*paid(4))]),
 email('pp1r', 'pp1-repeat', 'PP v5 · PP1-REPEAT', [G(pm(PO, 'greater-than', 1, ALLT)), G(*paid(4))]),
 delay('d2', 2),
 # PP2: bekeek iets aanbiedbaars, of heeft de 12-Pcs/34-Pcs nooit gehad (template kiest hero per land en valt terug op een bedankregel)
 email('pp2', 'pp2-upsell', 'PP v5 · PP2-UPSELL · VIP15', [G(*VIEWED, own('12-Pcs')), G(*VIEWED, own('34-Pcs')), G(pm(REFUND, 'equals', 0, last(30))), G(*paid(6))]),
 delay('d8', 6),
 email('pp3d', 'pp3-delivered', 'PP v5 · PP3-DELIVERED', [G(pm(DELIV, 'greater-than', 0, START)), G(*pan(10)), G(nomail('VQ93sx')), G(nomail('R9dcdY')),
                                                          G(name_has('P2-SAFE')), G(pm(REFUND, 'equals', 0, last(30))), G(*paid(10))]),
 delay('d11', 3),
 email('pp3s', 'pp3-safe', 'PP v5 · PP3-SAFE', [G(name_has('PP v5 · PP3')), G(*pan(13)), G(nomail('VQ93sx')), G(nomail('R9dcdY')),
                                                G(name_has('P2-SAFE')), G(pm(REFUND, 'equals', 0, last(30))), G(*paid(13))]),
 delay('d21', 10),
 {'temporary_id': 'cool', 'type': 'conditional-split', 'data': {'profile_filter': {'condition_groups': [G(pm(RECV, 'greater-than', 0, last(30), [{'property': 'Campaign Name', 'filter': {'type': 'string', 'operator': 'contains', 'value': 'CODE ·'}}]))]}}},
 email('pp4n', 'pp4-nocode', 'PP v5 · PP4 nocode · cooldown', [G(pm(PO, 'equals', 0, START)), G(pm(REFUND, 'equals', 0, last(30))), G(*paid(24))]),
 email('pp4c', 'pp4-code', 'CODE · PP v5 · PP4', [G(pm(PO, 'equals', 0, START)), G(pm(REFUND, 'equals', 0, last(30))), G(*paid(24))]),
]
nxt = ['pp1f', 'pp1r', 'd2', 'pp2', 'd8', 'pp3d', 'd11', 'pp3s', 'd21', 'cool']
for i, a in enumerate(A):
    if a['temporary_id'] == 'cool': a['links'] = {'next_if_true': 'pp4n', 'next_if_false': 'pp4c'}
    elif a['temporary_id'] in ('pp4n', 'pp4c'): a['links'] = {'next': None}
    else: a['links'] = {'next': nxt[i]}
definition = {'triggers': [{'type': 'metric', 'id': PO, 'trigger_filter': None}],
              'profile_filter': {'condition_groups': [G({'type': 'profile-not-in-flow', 'timeframe_filter': last(30)})]},
              'entry_action_id': 'd0', 'actions': A, 'reentry_criteria': {'duration': 30, 'unit': 'day'}}
body = {'data': {'type': 'flow', 'attributes': {'name': 'v5 · Post-purchase + delivery (draft)', 'definition': definition}}}
json.dump(body, open(os.path.join(ROOT, 'flow-definition.json'), 'w'), indent=1, ensure_ascii=False)
if '--dry' in sys.argv: print('dry', len(A), 'acties'); sys.exit()
idf = os.path.join(ROOT, 'flow-id.txt')
assert not os.path.exists(idf), 'flow bestaat al: ' + open(idf).read()
r = api('POST', '/api/flows/', body)
if 'data' not in r: print(json.dumps(r)[:1500]); sys.exit(1)
fid = r['data']['id']; open(idf, 'w').write(fid + '\n')
print('flow', fid, r['data']['attributes'].get('status'))
