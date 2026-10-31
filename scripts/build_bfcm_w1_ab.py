#!/usr/bin/env python3
"""BF-W1 direct, stijl B (dark), als A/B-test op de hoofdlijst (31 okt 2026, Floris: "meteen die mail, geen delay, dan A/B testen").
1. Template "v4 · BFCM · W1 direct · B dark" uit klaviyo/templates/v3/bfcm/signup/bf-w1-b.klaviyo.html.
2. Flow WjAc2q (lijst BFCM2026) krijgt deze template.
3. Nieuwe flow "v4 · BFCM Welcome · direct A/B (hoofdlijst)": trigger hoofdlijst Uw8eZG, geen wachttijd,
   random 50%: JA krijgt BF-W1 direct, NEE krijgt niets uit deze flow (alleen de gewone welcome W1 na 5 min).
Alles draft. Bij livegang moet de gewone welcome-W1 een extra filter krijgen ("geen mail uit deze flow in de laatste dag"),
anders krijgt de JA-groep ook nog de gewone W1. Dat filter staat NIET in dit script (live flow, pas bij livegang)."""
import json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api

SRC = '/home/user/siraat-email-agent/klaviyo/templates/v3/bfcm/signup/bf-w1-b.klaviyo.html'
TNAME = 'v4 · BFCM · W1 direct · B dark'
MAIN, BFCM_FLOW = 'Uw8eZG', 'WjAc2q'
NAME = 'v4 · BFCM Welcome · direct A/B (hoofdlijst)'
SUBJECT = "You're just in time 🧡"
PREVIEW = "Up to 70% off is live, no code needed. Here's where I'd start."


def msg(tid, name):
    return {'from_email': 'send@siraatskitchen.com', 'from_label': 'Benjamin from Siraat', 'reply_to_email': 'send@siraatskitchen.com',
            'cc_email': None, 'bcc_email': None, 'subject_line': SUBJECT, 'preview_text': PREVIEW, 'template_id': tid,
            'smart_sending_enabled': False, 'transactional': False, 'add_tracking_params': True,
            'custom_tracking_params': [{'param': 'utm_source', 'value': 'klaviyo'}, {'param': 'utm_medium', 'value': 'email'},
                                       {'param': 'utm_campaign', 'value': 'bfcm-welcome'}],
            'additional_filters': None, 'name': name}


if __name__ == '__main__':
    ex = api('GET', '/api/templates?filter=equals(name,"%s")' % TNAME)
    tid = ex['data'][0]['id'] if ex.get('data') else api('POST', '/api/templates', {'data': {'type': 'template', 'attributes': {'name': TNAME, 'editor_type': 'CODE', 'html': open(SRC).read()}}})['data']['id']
    print('template', tid)
    # flow BFCM2026 naar stijl B
    d = api('GET', f'/api/flows/{BFCM_FLOW}?additional-fields[flow]=definition')['data']['attributes']['definition']
    aid = d['actions'][0]['id']
    a = api('GET', f'/api/flow-actions/{aid}')['data']['attributes']['definition']
    a['data']['message'].update(template_id=tid, subject_line=SUBJECT, preview_text=PREVIEW)
    r = api('PATCH', f'/api/flow-actions/{aid}', {'data': {'type': 'flow-action', 'id': aid, 'attributes': {'definition': a}}})
    print('WjAc2q', 'FOUT ' + json.dumps(r['errors'])[:300] if 'errors' in r else 'ok')
    # nieuwe A/B-flow op hoofdlijst
    ex = api('GET', '/api/flows?filter=equals(name,"%s")' % NAME)
    if ex.get('data'):
        print('flow bestaat al', ex['data'][0]['id']); sys.exit()
    df = {'triggers': [{'type': 'list', 'id': MAIN}],
          'profile_filter': {'condition_groups': [{'conditions': [{'type': 'profile-not-in-flow', 'timeframe_filter': {'type': 'date', 'operator': 'alltime'}}]}]},
          'entry_action_id': 'split',
          'actions': [{'temporary_id': 'split', 'type': 'conditional-split',
                       'data': {'profile_filter': {'condition_groups': [{'conditions': [{'type': 'profile-sample', 'percentage': 50}]}]}},
                       'links': {'next_if_true': 'w1', 'next_if_false': None}},
                      {'temporary_id': 'w1', 'type': 'send-email', 'data': {'message': msg(tid, 'BF-W1 direct · B dark'), 'status': 'draft'}, 'links': {'next': None}}]}
    r = api('POST', '/api/flows', {'data': {'type': 'flow', 'attributes': {'name': NAME, 'definition': df}}})
    print('nieuwe flow', 'FOUT ' + json.dumps(r['errors'])[:800] if 'errors' in r else (r['data']['id'], r['data']['attributes']['status']))
