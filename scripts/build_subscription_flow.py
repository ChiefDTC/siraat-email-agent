#!/usr/bin/env python3
"""Bouwt v4 · Abonnement S1 (Loop) via de API als draft. Draaien: python3 scripts/build_subscription_flow.py [--dry]
Trigger: Ordered Product, Dishwasher Sheets (ProductID 15483020443988) voor $0 = eerste gratis pack van een Loop-abonnement.
Losse kopers ($35) en herhaalorders ($20) vallen erbuiten. 15 minuten wachten, dan een split, S1 (variant b) in de JA-tak.
Random sample via de API: conditie {'type': 'profile-sample', 'percentage': 20}."""
import json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api

DRY = '--dry' in sys.argv
D = '/home/user/siraat-email-agent/klaviyo/templates/v3/subscription/'
ORDERED = 'XT7f8Z'
SHEETS = 15483020443988
NAME = 'v4 · Abonnement S1 (Loop, test 20%)'
TNAME = 'v4 · Abonnement · S1 skip-tip (b)'
SUBJECT = 'Your first pack of sheets is on us'
PREVIEW = 'Your free dishwasher sheet pack is on us.'


def template():
    ex = api('GET', '/api/templates?filter=equals(name,"%s")' % TNAME)
    if ex.get('data'):
        print('template bestaat', ex['data'][0]['id']); return ex['data'][0]['id']
    if DRY:
        return 'DRY'
    html = open(D + 's1b.klaviyo.html').read()
    r = api('POST', '/api/templates', {'data': {'type': 'template', 'attributes': {'name': TNAME, 'editor_type': 'CODE', 'html': html}}})
    print('template', r['data']['id']); return r['data']['id']


def definition(tid):
    prop = lambda field, op, val: {'type': 'metric-property', 'metric_id': ORDERED, 'field': field,
                                   'filter': {'type': 'numeric', 'operator': op, 'value': val}}
    trig = {'type': 'metric', 'id': ORDERED, 'trigger_filter': {'condition_groups': [
        {'conditions': [prop('ProductID', 'equals', SHEETS)]},
        {'conditions': [prop('$value', 'equals', 0)]}]}}
    pf = {'condition_groups': [{'conditions': [{'type': 'profile-not-in-flow', 'timeframe_filter': {'type': 'date', 'operator': 'alltime'}}]}]}
    placeholder = {'condition_groups': [{'conditions': [{'type': 'profile-sample', 'percentage': 20}]}]}  # random sample 20%
    msg = {'from_email': 'send@siraatskitchen.com', 'from_label': 'Benjamin from Siraat', 'reply_to_email': 'send@siraatskitchen.com',
           'cc_email': None, 'bcc_email': None, 'subject_line': SUBJECT, 'preview_text': PREVIEW, 'template_id': tid,
           'smart_sending_enabled': False, 'transactional': False, 'add_tracking_params': True,
           'custom_tracking_params': [{'param': 'utm_source', 'value': 'klaviyo'}, {'param': 'utm_medium', 'value': 'email'},
                                      {'param': 'utm_campaign', 'value': 'v4-subscription'}],
           'additional_filters': None, 'name': 'S1 skip-tip (b)'}
    acts = [
        {'temporary_id': 'wait', 'type': 'time-delay', 'data': {'unit': 'minutes', 'value': 15, 'secondary_value': None,
                                                                 'timezone': 'profile', 'delay_until_time': None}, 'links': {'next': 'split'}},
        {'temporary_id': 'split', 'type': 'conditional-split', 'data': {'profile_filter': placeholder},
         'links': {'next_if_true': 's1', 'next_if_false': None}},
        {'temporary_id': 's1', 'type': 'send-email', 'data': {'message': msg, 'status': 'draft'}, 'links': {'next': None}},
    ]
    return {'triggers': [trig], 'profile_filter': pf, 'entry_action_id': 'wait', 'actions': acts}


if __name__ == '__main__':
    tid = template()
    d = definition(tid)
    if DRY:
        print(json.dumps(d)[:1500]); sys.exit()
    ex = api('GET', '/api/flows?filter=equals(name,"%s")' % NAME)
    if ex.get('data'):
        print('flow bestaat al', ex['data'][0]['id']); sys.exit()
    r = api('POST', '/api/flows', {'data': {'type': 'flow', 'attributes': {'name': NAME, 'definition': d}}})
    if 'errors' in r:
        print('FOUT', json.dumps(r['errors'])[:2000]); sys.exit(1)
    print('flow', r['data']['id'], r['data']['attributes']['status'])
