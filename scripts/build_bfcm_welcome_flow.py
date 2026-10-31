#!/usr/bin/env python3
"""Bouwt "v4 · BFCM Welcome · direct" via de API als draft (31 okt 2026, Floris: aparte flow, direct een mail, zoals Smooche).
Trigger: lijst BFCM2026 (SWsGdg), waar beide Black Friday-pop-ups naartoe sturen. Geen wachttijd: BF-W1 gaat direct uit.
BF-W1 = klaviyo/templates/v3/bfcm/signup/bf-w1.klaviyo.html (bestsellers per markt: VS Pan Pro, 6 Pcs, 12 Pcs; anders Pan Pro, 6 Pcs, Deep, Wok).
Smart Sending uit (het is de eerste mail, mag nooit wegvallen). Status mail en flow: draft. Draaien: python3 scripts/build_bfcm_welcome_flow.py"""
import json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api

LIST = 'SWsGdg'
NAME = 'v4 · BFCM Welcome · direct (BFCM2026)'
TNAME = 'v4 · BFCM · W1 direct (bestsellers)'
SRC = '/home/user/siraat-email-agent/klaviyo/templates/v3/bfcm/signup/bf-w1.klaviyo.html'
SUBJECT = "You're just in time 🧡"
PREVIEW = "You're in. Up to 70% off, no code needed. Here's where I'd start."


def template():
    ex = api('GET', '/api/templates?filter=equals(name,"%s")' % TNAME)
    if ex.get('data'):
        return ex['data'][0]['id']
    r = api('POST', '/api/templates', {'data': {'type': 'template', 'attributes': {'name': TNAME, 'editor_type': 'CODE', 'html': open(SRC).read()}}})
    return r['data']['id']


if __name__ == '__main__':
    ex = api('GET', '/api/flows?filter=equals(name,"%s")' % NAME)
    if ex.get('data'):
        print('flow bestaat al', ex['data'][0]['id']); sys.exit()
    tid = template(); print('template', tid)
    msg = {'from_email': 'send@siraatskitchen.com', 'from_label': 'Benjamin from Siraat', 'reply_to_email': 'send@siraatskitchen.com',
           'cc_email': None, 'bcc_email': None, 'subject_line': SUBJECT, 'preview_text': PREVIEW, 'template_id': tid,
           'smart_sending_enabled': False, 'transactional': False, 'add_tracking_params': True,
           'custom_tracking_params': [{'param': 'utm_source', 'value': 'klaviyo'}, {'param': 'utm_medium', 'value': 'email'},
                                      {'param': 'utm_campaign', 'value': 'bfcm-welcome'}],
           'additional_filters': None, 'name': 'BF-W1 direct'}
    d = {'triggers': [{'type': 'list', 'id': LIST}],
         'profile_filter': {'condition_groups': [{'conditions': [{'type': 'profile-not-in-flow', 'timeframe_filter': {'type': 'date', 'operator': 'alltime'}}]}]},
         'entry_action_id': 'w1',
         'actions': [{'temporary_id': 'w1', 'type': 'send-email', 'data': {'message': msg, 'status': 'draft'}, 'links': {'next': None}}]}
    r = api('POST', '/api/flows', {'data': {'type': 'flow', 'attributes': {'name': NAME, 'definition': d}}})
    if 'errors' in r:
        print('FOUT', json.dumps(r['errors'])[:1500]); sys.exit(1)
    print('flow', r['data']['id'], r['data']['attributes']['status'])
