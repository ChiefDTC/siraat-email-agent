#!/usr/bin/env python3
"""Reviewverzoek via meerdere bezorgtriggers (1 nov 2026, Floris: "meerdere triggers, maar niet dubbel").
Klaviyo staat maar 1 trigger per flow toe, dus per trigger een kopie van XzHrez (14 d tot 09:30, mail variant A):
- Postflows "4. Shipment Delivered" (UabgWz)
- ShipBob "Delivered" (SMpL9v)
Dedupe: elke reviewmail in alle reviewflows (XzHrez, TvfJYU en de kopieen) krijgt per andere reviewflow een filter
"Received Email met $flow = X, ooit, aantal 0". Nieuwe flows als draft; de dedupe-filters op XzHrez (A/B-variaties)
en TvfJYU sluiten alleen extra uit. Draaien: python3 scripts/build_review_multi_trigger.py"""
import json, sys, copy
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api

SRC, FALLBACK = 'XzHrez', 'TvfJYU'
NEW = [('UabgWz', 'Review request · Delivered +14d (Postflows)'), ('SMpL9v', 'Review request · Delivered +14d (ShipBob)')]


def nodup(fid):
    return {'conditions': [{'type': 'profile-metric', 'metric_id': 'YkRM4Q', 'measurement': 'count',
                            'measurement_filter': {'type': 'numeric', 'operator': 'equals', 'value': 0},
                            'timeframe_filter': {'type': 'date', 'operator': 'alltime'},
                            'metric_filters': [{'property': '$flow', 'filter': {'type': 'string', 'operator': 'equals', 'value': fid}}]}]}


def add_dedupe(filters, others):
    f = copy.deepcopy(filters) or {'condition_groups': []}
    have = json.dumps(f)
    for o in others:
        if f'"value": "{o}"' not in have:
            f['condition_groups'].append(nodup(o))
    return f


src = api('GET', f'/api/flows/{SRC}?additional-fields[flow]=definition')['data']['attributes']['definition']
ab = [a for a in src['actions'] if a['type'] == 'ab-test'][0]['data']
varA = [v for v in ab['current_experiment']['variations'] if v['data']['message']['subject_line'].startswith('Win')][0]
delay = [a for a in src['actions'] if a['type'] == 'time-delay'][0]['data']

ids = {}
for metric, name in NEW:
    ex = api('GET', '/api/flows?filter=equals(name,"%s")' % name)
    if ex.get('data'):
        ids[metric] = ex['data'][0]['id']; print('bestaat', name, ids[metric]); continue
    msg = copy.deepcopy(varA['data']['message']); msg.pop('id', None); msg['name'] = 'Review request · Win your purchase back'
    d = {'triggers': [{'type': 'metric', 'id': metric}], 'profile_filter': src['profile_filter'], 'entry_action_id': 'wait',
         'actions': [{'temporary_id': 'wait', 'type': 'time-delay', 'data': delay, 'links': {'next': 'mail'}},
                     {'temporary_id': 'mail', 'type': 'send-email', 'data': {'message': msg, 'status': 'draft'}, 'links': {'next': None}}]}
    r = api('POST', '/api/flows', {'data': {'type': 'flow', 'attributes': {'name': name, 'definition': d}}})
    if 'errors' in r:
        print('FOUT', json.dumps(r['errors'])[:800]); sys.exit(1)
    ids[metric] = r['data']['id']; print('nieuw', name, ids[metric], r['data']['attributes']['status'])

allflows = [SRC, FALLBACK] + list(ids.values())


def patch(aid, fid):
    a = api('GET', f'/api/flow-actions/{aid}')['data']['attributes']['definition']
    m = a['data']['message']
    m['additional_filters'] = add_dedupe(m.get('additional_filters'), [o for o in allflows if o != fid])
    r = api('PATCH', f'/api/flow-actions/{aid}', {'data': {'type': 'flow-action', 'id': aid, 'attributes': {'definition': a}}})
    print(' ', fid, aid, 'FOUT ' + json.dumps(r['errors'])[:300] if 'errors' in r else 'dedupe ok')


for v in ab['current_experiment']['variations']:
    patch(v['id'], SRC)
fb = api('GET', f'/api/flows/{FALLBACK}?additional-fields[flow]=definition')['data']['attributes']['definition']
patch([a for a in fb['actions'] if a['type'] == 'send-email'][0]['id'], FALLBACK)
for fid in ids.values():
    d = api('GET', f'/api/flows/{fid}?additional-fields[flow]=definition')['data']['attributes']['definition']
    patch([a for a in d['actions'] if a['type'] == 'send-email'][0]['id'], fid)
