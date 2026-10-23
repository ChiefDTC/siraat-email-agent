#!/usr/bin/env python3
"""Bouwt v4 · Mystery Gift (klaviyo/flows/mystery-gift-v3.md) via de API. Draaien: python3 scripts/build_mystery_flow.py [--dry]
Stap 1 templates (CODE) uit m1-m4.klaviyo.html, stap 2 flow als draft met M1-M3 draft en M4 draft (blijft uit).
Livezetten gebeurt los, na controle. A/B-onderwerpen kunnen niet via de API: onderwerp A (oude controle) staat erin."""
import json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api

DRY = '--dry' in sys.argv
D = '/home/user/siraat-email-agent/klaviyo/templates/v3/mystery/'
ORDERED, PLACED, RECEIVED, REFUND = 'XT7f8Z', 'RSNxYV', 'YkRM4Q', 'Xg6cwn'
POST_PURCHASE, OLD = 'X3ySuU', 'WvRupU'
NAME = 'v4 · Mystery Gift'
MAILS = [  # (key, templatenaam, onderwerp, preview, wacht dagen, utm, status)
    ('m1', 'v4 · Mystery · M1 reveal', "Let's reveal your mystery gift", "It's not overstock. It's the other half of a no-coating kitchen.", 3),
    ('m2', 'v4 · Mystery · M2 how to use', 'The ten-second way to use your gift', 'One sheet where the pod goes. Half a sheet for a light load.', 9),
    ('m3', 'v4 · Mystery · M3 offer', "Alright, here's the offer", 'Including the part most brands would leave out.', 11),
    ('m4', 'v4 · Mystery · M4 last one', 'Last one from me about the dishwasher sheets', "The price isn't going anywhere. These emails are.", 7),
]


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


def templates():
    ids = {}
    for key, tname, *_ in MAILS:
        ex = api('GET', '/api/templates?filter=equals(name,"%s")' % tname)
        if ex.get('data'):
            ids[key] = ex['data'][0]['id']; print('template bestaat', tname, ids[key]); continue
        html = open(D + key + '.klaviyo.html').read()
        if DRY:
            ids[key] = 'DRY'; continue
        r = api('POST', '/api/templates', {'data': {'type': 'template', 'attributes': {'name': tname, 'editor_type': 'CODE', 'html': html}}})
        ids[key] = r['data']['id']; print('template', tname, ids[key])
    return ids


def definition(ids):
    trig = {'type': 'metric', 'id': ORDERED, 'trigger_filter': {'condition_groups': [G(
        {'type': 'metric-property', 'metric_id': ORDERED, 'field': 'ProductID', 'filter': {'type': 'numeric', 'operator': 'equals', 'value': 15785445622100}},
        {'type': 'metric-property', 'metric_id': ORDERED, 'field': 'Name', 'filter': {'type': 'string', 'operator': 'equals', 'value': 'Mystery Gift'}})]}}
    items = lambda name: [{'property': 'Items', 'filter': {'type': 'string', 'operator': 'contains', 'value': name}}]
    pf = {'condition_groups': [
        G({'type': 'profile-property', 'property': "properties['rc_active_subscriber']", 'filter': {'type': 'boolean', 'operator': 'equals', 'value': False}},
          {'type': 'profile-property', 'property': "properties['rc_active_subscriber']", 'filter': {'type': 'existence', 'operator': 'not-set'}}),
        G(pm(PLACED, 'equals', 0, tf('flow-start'), items('Plastic-Free Dishwasher Sheets'))),
        G(pm(PLACED, 'equals', 0, tf('flow-start'), items('Non-Toxic Dishwasher Sheets'))),
        G({'type': 'profile-not-in-flow', 'timeframe_filter': tf('alltime')}),
        G(pm(RECEIVED, 'equals', 0, tf('alltime'), [{'property': '$flow', 'filter': {'type': 'string', 'operator': 'equals', 'value': OLD}}])),
        G(pm(REFUND, 'equals', 0, tf('in-the-last', 30))),
    ]}
    skip_pp = {'condition_groups': [G(pm(RECEIVED, 'equals', 0, tf('in-the-last', 2),
                                         [{'property': '$flow', 'filter': {'type': 'string', 'operator': 'equals', 'value': POST_PURCHASE}}]))]}
    acts = []
    for i, (key, tname, subj, prev, days) in enumerate(MAILS):
        nxt = 'w' + MAILS[i + 1][0] if i + 1 < len(MAILS) else None
        acts.append({'temporary_id': 'w' + key, 'type': 'time-delay',
                     'data': {'unit': 'days', 'value': days, 'secondary_value': None, 'timezone': 'profile', 'delay_until_time': '10:00:00'},
                     'links': {'next': 'e' + key}})
        msg = {'from_email': 'send@siraatskitchen.com', 'from_label': 'Benjamin from Siraat', 'reply_to_email': 'send@siraatskitchen.com',
               'cc_email': None, 'bcc_email': None, 'subject_line': subj, 'preview_text': prev, 'template_id': ids[key],
               'smart_sending_enabled': True, 'transactional': False, 'add_tracking_params': True,
               'custom_tracking_params': [{'param': 'utm_source', 'value': 'klaviyo'}, {'param': 'utm_medium', 'value': 'email'},
                                          {'param': 'utm_campaign', 'value': 'v4-mystery'}],
               'additional_filters': skip_pp, 'name': tname}
        acts.append({'temporary_id': 'e' + key, 'type': 'send-email', 'data': {'message': msg, 'status': 'draft'}, 'links': {'next': nxt}})
    return {'triggers': [trig], 'profile_filter': pf, 'entry_action_id': 'wm1', 'actions': acts}


if __name__ == '__main__':
    ids = templates()
    d = definition(ids)
    if DRY:
        print(json.dumps(d)[:600]); sys.exit()
    ex = api('GET', '/api/flows?filter=equals(name,"%s")' % NAME)
    if ex.get('data'):
        print('flow bestaat al', ex['data'][0]['id']); sys.exit()
    r = api('POST', '/api/flows', {'data': {'type': 'flow', 'attributes': {'name': NAME, 'definition': d}}})
    if 'errors' in r:
        print('FOUT', json.dumps(r['errors'])[:2000]); sys.exit(1)
    print('flow', r['data']['id'], r['data']['attributes']['status'])
