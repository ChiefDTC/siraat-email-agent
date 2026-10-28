#!/usr/bin/env python3
"""Vangnetflows voor de bezorgflows (28 okt 2026, akkoord Floris).

Sinds ~22 okt komen Delivered Shipment (VcUF33) en Postflows (UabgWz) maar voor een deel van de
orders binnen. Deze twee flows starten op Fulfilled Order (VtEiZT) plus een vaste wachttijd en
nemen alleen wie geen bezorgevent kreeg sinds de start (zelfde opzet als review-vangnet TvfJYU).

  P2-vangnet   : Fulfilled + 12 dagen 13:00  -> zelfde mail als VQ93sx P2 (template UKxRjv)
  AFF-vangnet  : Fulfilled + 12 dagen 10:00 -> zelfde opbouw als R22pzb (10% holdout, A1, A2)

Wachttijd uit de data: Fulfilled -> Delivered (Klaviyo, 1.323 orders 20 sep tot 11 okt) mediaan
7,1 dagen, p75 9,7, p90 12,5; Ecomflow US 9,1 dagen gemiddeld (30 d). P2 gaat in het origineel
1 dag na bezorging om 09:00. P2 zegt "your pan has arrived", dus vangnet pas op dag 12 om 13:00
(p90 van de levertijd; andere tijd dan 09:00, zodat een origineel van dezelfde ochtend al als ontvangen telt). AFF origineel = bezorging + 3 dagen.

Dedupe: vangnet slaat over als er sinds de start een bezorgevent kwam, of als de originele mail
(of P2-SAFE) al ontvangen is. De originele mails krijgen apart (patch_dedupe) het filter
"geen mail uit het vangnet". $0-filter (TikTok-samples) op elke mail.

Draaien vanuit elke map: python3 scripts/build_fallback_flows.py [--dry]
Alles wordt als draft gemaakt. Livezetten gebeurt los na QA.
"""
import json, sys, copy
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api

DRY = '--dry' in sys.argv
FULFILLED, DELIVERED, POSTFLOWS = 'VtEiZT', 'VcUF33', 'UabgWz'
PLACED, RECEIVED, REFUND = 'RSNxYV', 'YkRM4Q', 'Xg6cwn'
NAME_P2 = 'v4 · P2 vangnet · Fulfilled +12d (geen Delivered)'
NAME_AFF = 'AFF S1 vangnet · Fulfilled +12d (geen Postflows)'


def tf(op, days=None):
    d = {'type': 'date', 'operator': op}
    if days:
        d.update(unit='day', quantity=days)
    return d


def pm(metric, op, val, frame, mf=None):
    return {'type': 'profile-metric', 'metric_id': metric, 'measurement': 'count',
            'measurement_filter': {'type': 'numeric', 'operator': op, 'value': val},
            'timeframe_filter': frame, 'metric_filters': mf}


def G(*c):
    return {'conditions': list(c)}


def recv_flow(fid, frame):
    return pm(RECEIVED, 'equals', 0, frame, [{'property': '$flow', 'filter': {'type': 'string', 'operator': 'equals', 'value': fid}}])


def paid(days):
    return pm(PLACED, 'greater-than', 0, tf('in-the-last', days),
              [{'property': '$value', 'filter': {'type': 'numeric', 'operator': 'greater-than', 'value': 0}}])


def flowdef(fid):
    return api('GET', f'/api/flows/{fid}?additional-fields[flow]=definition')['data']['attributes']['definition']


def p2_definition():
    src = flowdef('VQ93sx')
    pan = copy.deepcopy(src['profile_filter']['condition_groups'][0])
    pan['conditions'][0]['timeframe_filter'] = tf('in-the-last', 45)
    p2safe = copy.deepcopy(src['profile_filter']['condition_groups'][2])  # Campaign Name contains P2-SAFE, 0 in 30 d
    pf = {'condition_groups': [
        pan,
        G({'type': 'profile-not-in-flow', 'timeframe_filter': tf('in-the-last', 30)}),
        p2safe,
        G(recv_flow('VQ93sx', tf('in-the-last', 30))),
        G(pm(DELIVERED, 'equals', 0, tf('flow-start'))),
    ]}
    send = [a for a in src['actions'] if a['type'] == 'send-email'][0]
    m = copy.deepcopy(send['data']['message'])
    m.pop('id', None)
    m['name'] = 'P2 · vangnet'
    af = copy.deepcopy(m['additional_filters'])
    af['condition_groups'] += [G(paid(45)), G(recv_flow('VQ93sx', tf('in-the-last', 30))), copy.deepcopy(p2safe)]
    m['additional_filters'] = af
    acts = [
        {'temporary_id': 'w1', 'type': 'time-delay',
         'data': {'unit': 'days', 'value': 12, 'secondary_value': None, 'timezone': 'profile', 'delay_until_time': '13:00:00'},
         'links': {'next': 'e1'}},
        {'temporary_id': 'e1', 'type': 'send-email', 'data': {'message': m, 'status': 'draft'}, 'links': {'next': None}},
    ]
    return {'triggers': [{'type': 'metric', 'id': FULFILLED, 'trigger_filter': None}], 'profile_filter': pf,
            'entry_action_id': 'w1', 'actions': acts, 'reentry_criteria': {'duration': 30, 'unit': 'day'}}


def aff_definition():
    src = flowdef('R22pzb')
    pf = copy.deepcopy(src['profile_filter'])
    pf['condition_groups'] += [G(recv_flow('R22pzb', tf('alltime'))), G(pm(POSTFLOWS, 'equals', 0, tf('flow-start')))]
    A = {a['id']: a for a in src['actions']}
    tid = {i: 'a' + i[-3:] for i in A}
    acts = []
    for i, a in A.items():
        b = {'temporary_id': tid[i], 'type': a['type'], 'data': copy.deepcopy(a['data']),
             'links': {k: (tid[v] if v else None) for k, v in a.get('links', {}).items()}}
        if a['type'] == 'time-delay' and i == '121654813':  # eerste wachttijd: bezorging + 3 d -> fulfilled + 12 d
            b['data']['value'] = 12
        if a['type'] == 'send-email':
            m = b['data']['message']
            m.pop('id', None)
            m['name'] = m['name'] + ' · vangnet'  # blijft "AFF S1 · A1" bevatten voor de open/klik-split
            m['additional_filters'] = {'condition_groups': [G(paid(70)), G(recv_flow('R22pzb', tf('alltime')))]}
            b['data']['status'] = 'draft'
        acts.append(b)
    return {'triggers': [{'type': 'metric', 'id': FULFILLED, 'trigger_filter': None}], 'profile_filter': pf,
            'entry_action_id': tid[src['entry_action_id']], 'actions': acts}


def create(name, d):
    url = '/api/flows?page[size]=50&fields[flow]=name'
    while url:  # filter op naam met een middot werkt niet betrouwbaar, dus zelf vergelijken
        ex = api('GET', url)
        hit = [f['id'] for f in ex.get('data', []) if f['attributes']['name'] == name]
        if hit:
            print('flow bestaat al', name, hit[0]); return hit[0]
        nxt = ex.get('links', {}).get('next')
        url = nxt.replace('https://a.klaviyo.com', '') if nxt else None
    if DRY:
        print('DRY', name, json.dumps(d)[:400]); return None
    r = api('POST', '/api/flows', {'data': {'type': 'flow', 'attributes': {'name': name, 'definition': d}}})
    if 'errors' in r:
        print('FOUT', name, json.dumps(r['errors'])[:1500]); return None
    print('flow', name, r['data']['id'], r['data']['attributes']['status'])
    return r['data']['id']


if __name__ == '__main__':
    create(NAME_P2, p2_definition())
    create(NAME_AFF, aff_definition())
