#!/usr/bin/env python3
"""Bouwt de affiliate-flows (klaviyo/flows/affiliate-system-v1.md) als DRAFT via POST /api/flows.
Draaien vanuit de scratchpad golive-map (kl.py): python3 build_aff_flows.py [--dry]
Alle mails status draft, flows status draft. Raakt geen bestaande flows aan.

S1 (vanaf 22 okt middag) start op bezorging: Postflows - 4. Shipment Delivered (UabgWz), alleen affiliates
(profiel heeft Referral Link - SocialSnowball). 10% holdout, 3 dagen (10:00), 2 dagen extra als er net een
reviewmail was, A1 announce, 3 dagen, A2 nudge-1 alleen voor openers zonder klik. Geen samenkomende takken
(PLAYBOOK/v4 2.1), dus de A1-staart staat dubbel. De oude lineaire slotversie (VX4gA3) is verwijderd.
Optie --only s1 bouwt alleen S1.
"""
import json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api

T = json.load(open('/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/aff/templates.json'))
DRY = '--dry' in sys.argv
SALE, PAYOUT = 'Xqbr4d', 'WManrA'   # XzrVJZ (inschrijving) is niet meer de S1-trigger
RECEIVED, OPENED, CLICKED = 'YkRM4Q', 'WyrTym', 'W247h8'
REFUND, CANCEL, TICKET = 'Xg6cwn', 'TFervq', 'YzvjGf'
POSTFLOWS = 'UabgWz'                # Postflows - 4. Shipment Delivered
REVIEW_FLOWS = ['XzHrez', 'TvfJYU']
A1, A2 = 'AFF S1 · A1', 'AFF S1 · A2'
REF_LINK = 'Referral Link - SocialSnowball'
S1_NAME = 'AFF S1 · Activatie na bezorging'
SEND_AT = '10:00:00'                       # profieltijdzone


def tf(op, **k):
    d = {'type': 'date', 'operator': op}
    if op == 'in-the-last':
        d.update(unit='day', quantity=k['days'])
    return d


def pm(metric, op, val, frame, mf=None):
    return {'type': 'profile-metric', 'metric_id': metric, 'measurement': 'count',
            'measurement_filter': {'type': 'numeric', 'operator': op, 'value': val},
            'timeframe_filter': frame, 'metric_filters': mf}


def name_is(s, op='contains'):
    return [{'property': 'Campaign Name', 'filter': {'type': 'string', 'operator': op, 'value': s}}]


def flow_is(fid):
    return [{'property': '$flow', 'filter': {'type': 'string', 'operator': 'equals', 'value': fid}}]


def G(*conds):  # één conditiegroep: condities binnen een groep = OF
    return {'conditions': list(conds)}


def msg(name, subject, preview, tpl, utm, smart):
    return {'from_email': 'send@siraatskitchen.com', 'from_label': 'Benjamin from Siraat',
            'reply_to_email': 'send@siraatskitchen.com', 'cc_email': None, 'bcc_email': None,
            'subject_line': subject, 'preview_text': preview, 'template_id': tpl,
            'smart_sending_enabled': smart, 'transactional': False, 'add_tracking_params': True,
            'custom_tracking_params': [{'param': 'utm_source', 'value': 'klaviyo'}, {'param': 'utm_medium', 'value': 'email'},
                                       {'param': 'utm_campaign', 'value': utm}],
            'additional_filters': None, 'name': name}


def email(tid, m, filters, nxt):
    m = dict(m)
    m['additional_filters'] = {'condition_groups': filters} if filters else None
    return {'temporary_id': tid, 'type': 'send-email', 'data': {'message': m, 'status': 'draft'}, 'links': {'next': nxt}}


def wait(tid, days, nxt):
    return {'temporary_id': tid, 'type': 'time-delay',
            'data': {'unit': 'days', 'value': days, 'secondary_value': None, 'timezone': 'profile', 'delay_until_time': SEND_AT},
            'links': {'next': nxt}}


# ------------------------------------------------------------------ S1 (22 okt middag: bezorg-trigger)
def s1():
    """S1 op bezorging (Postflows UabgWz). Geen slots meer: de trigger is zelf het bezorgbewijs.
    Takken lopen niet samen (editorregel v4 2.1): A1 en de A2-staart staan dubbel, een keer direct
    en een keer na 2 extra dagen wachten als er net een reviewmail was."""
    pf = {'condition_groups': [
        G({'type': 'profile-property', 'property': "properties['%s']" % REF_LINK, 'filter': {'type': 'existence', 'operator': 'is-set'}}),
        G({'type': 'profile-not-in-flow', 'timeframe_filter': tf('alltime')}),
        G(pm(REFUND, 'equals', 0, tf('in-the-last', days=60))),
        G(pm(CANCEL, 'equals', 0, tf('in-the-last', days=60))),
        G(pm(TICKET, 'equals', 0, tf('in-the-last', days=21))),
        G(pm(SALE, 'equals', 0, tf('alltime'))),
    ]}
    review_2d = {'condition_groups': [G(*[pm(RECEIVED, 'greater-than', 0, tf('in-the-last', days=2), flow_is(f)) for f in REVIEW_FLOWS])]}
    opened_not_clicked = {'condition_groups': [G(pm(OPENED, 'greater-than', 0, tf('flow-start'), name_is(A1))),
                                               G(pm(CLICKED, 'equals', 0, tf('flow-start'), name_is(A1)))]}
    m1 = msg(A1 + ' · announce', 'Your order can pay for itself', 'Friends get 15% off their first order. You get 15% of what they pay.',
             T['AFF · announce'], 'aff-announce', True)
    m2 = msg(A2 + ' · nudge-1', 'Has anyone asked about your pan?', 'That is the moment your link pays. Give 15%, get 15%.',
             T['AFF · nudge-1'], 'aff-nudge-1', True)

    def split(tid, flt, yes, no):
        return {'temporary_id': tid, 'type': 'conditional-split', 'data': {'profile_filter': flt},
                'links': {'next_if_true': yes, 'next_if_false': no}}

    def tail(sfx, label):  # A1, 3 dagen, opened-niet-geklikt, A2
        return [email('a1' + sfx, dict(m1, name=f'{A1} · announce{label}'), None, 'w3' + sfx),
                wait('w3' + sfx, 3, 'c' + sfx),
                split('c' + sfx, opened_not_clicked, 'a2' + sfx, None),
                email('a2' + sfx, dict(m2, name=f'{A2} · nudge-1{label}'), None, None)]

    acts = [split('hold', {'condition_groups': [G({'type': 'profile-sample', 'percentage': 10})]}, None, 'w1'),
            wait('w1', 3, 'rv'),
            split('rv', review_2d, 'w2', 'a1'),
            wait('w2', 2, 'a1r')]
    acts += tail('', '') + tail('r', ' · na review')
    return S1_NAME, {'triggers': [{'type': 'metric', 'id': POSTFLOWS}], 'profile_filter': pf,
                     'entry_action_id': 'hold', 'actions': acts}


def single(name, trig, days_not_in_flow, m):
    pf = {'condition_groups': [G({'type': 'profile-not-in-flow', 'timeframe_filter': tf('in-the-last', days=days_not_in_flow)})]}
    return name, {'triggers': [{'type': 'metric', 'id': trig}], 'profile_filter': pf, 'entry_action_id': 'e',
                  'actions': [email('e', m, None, None)]}


def s5():
    return [single('AFF S5a · Verkoopmelding', SALE, 3,
                   msg('AFF S5 · SALE · aff-sale', 'A friend just ordered with your link', 'Here is your commission, and how your order can pay for itself.',
                       T['AFF · sale'], 'aff-sale', False)),
            single('AFF S5b · Uitbetaling', PAYOUT, 14,
                   msg('AFF S5 · PAY · aff-payout', 'Your payout is on its way', 'Look for an email from Tremendous to choose PayPal, bank, Visa or a gift card.',
                       T['AFF · payout'], 'aff-payout', False))]


if __name__ == '__main__':
    out = {}
    flows = [s1()] if '--only' in sys.argv and 's1' in sys.argv else [s1()] + s5()
    for name, d in flows:
        print(name, len(d['actions']), 'acties')
        if DRY:
            continue
        ex = api('GET', '/api/flows?filter=equals(name,"%s")&fields[flow]=name' % name)
        if ex.get('data'):
            print('  bestaat al', ex['data'][0]['id']); out[name] = ex['data'][0]['id']; continue
        r = api('POST', '/api/flows', {'data': {'type': 'flow', 'attributes': {'name': name, 'definition': d}}})
        if 'errors' in r:
            print('  FOUT', json.dumps(r['errors'])[:1500]); continue
        out[name] = r['data']['id']; print('  ', r['data']['id'], r['data']['attributes']['status'])
    if out:
        fj = '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/aff/flows.json'
        try:
            prev = json.load(open(fj))
        except Exception:
            prev = {}
        prev.update(out)
        json.dump(prev, open(fj, 'w'), ensure_ascii=False, indent=1)
