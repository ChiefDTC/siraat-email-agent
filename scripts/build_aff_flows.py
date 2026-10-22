#!/usr/bin/env python3
"""Bouwt de affiliate-flows (klaviyo/flows/affiliate-system-v1.md) als DRAFT via POST /api/flows.
Draaien vanuit de scratchpad golive-map (kl.py): python3 build_aff_flows.py [--dry]
Alle mails status draft, flows status draft. Raakt geen bestaande flows aan.

S1 is lineair (Klaviyo kent geen samenkomende takken, PLAYBOOK/v4 2.1): slots om de 3 dagen, per slot
eerst een A2-kopie (nudge-1 voor openers van A1 zonder klik, 3 dagen na A1) en dan een A1-kopie (announce)
met verzendfilters die bepalen of het profiel nu aan de beurt is. Een overgeslagen profiel komt in het
volgende slot terug; zo werkt ook de 3-dagenafstand tot de reviewmail zonder extra takken.
"""
import json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api

T = json.load(open('/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/aff/templates.json'))
DRY = '--dry' in sys.argv
ENROLLED, SALE, PAYOUT = 'XzrVJZ', 'Xqbr4d', 'WManrA'
RECEIVED, OPENED, CLICKED = 'YkRM4Q', 'WyrTym', 'W247h8'
REFUND, CANCEL, TICKET = 'Xg6cwn', 'TFervq', 'YzvjGf'
DELIV, POSTFLOWS = 'VcUF33', 'UabgWz'
REVIEW_FLOWS = ['XzHrez', 'TvfJYU']
A1, A2 = 'AFF S1 · A1', 'AFF S1 · A2'
SLOTS = [6, 9, 12, 15, 18, 21, 24, 27]   # dagen na inschrijving waarop A1 kan vallen
CAP = 21                                   # vanaf dag 21 ook zonder bezorgbewijs


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
            'data': {'unit': 'days', 'value': days, 'secondary_value': None, 'timezone': 'profile', 'delay_until_time': '09:00:00'},
            'links': {'next': nxt}}


# ------------------------------------------------------------------ S1
def s1():
    pf = {'condition_groups': [
        G({'type': 'profile-not-in-flow', 'timeframe_filter': tf('alltime')}),
        G(pm(REFUND, 'equals', 0, tf('flow-start'))),
        G(pm(CANCEL, 'equals', 0, tf('flow-start'))),
        G(pm(TICKET, 'equals', 0, tf('in-the-last', days=21))),
        G(pm(SALE, 'equals', 0, tf('flow-start'))),
    ]}
    no_review_3d = [G(pm(RECEIVED, 'equals', 0, tf('in-the-last', days=3), flow_is(f))) for f in REVIEW_FLOWS]
    not_yet_a1 = G(pm(RECEIVED, 'equals', 0, tf('flow-start'), name_is(A1)))
    settled = [G(pm(DELIV, 'equals', 0, tf('in-the-last', days=3))), G(pm(POSTFLOWS, 'equals', 0, tf('in-the-last', days=3)))]
    has_proof = G(pm(DELIV, 'greater-than', 0, tf('flow-start')), pm(POSTFLOWS, 'greater-than', 0, tf('flow-start')))
    a2_filters = [G(pm(RECEIVED, 'greater-than', 0, tf('in-the-last', days=4), name_is(A1))),
                  G(pm(OPENED, 'greater-than', 0, tf('flow-start'), name_is(A1))),
                  G(pm(CLICKED, 'equals', 0, tf('flow-start'), name_is(A1))),
                  G(pm(RECEIVED, 'equals', 0, tf('flow-start'), name_is(A2)))]
    m1 = msg(A1 + ' · announce', 'Your order can pay for itself', 'Friends get 15% off their first order. You get 15% of what they pay.',
             T['AFF · announce'], 'aff-announce', True)
    m2 = msg(A2 + ' · nudge-1', 'Has anyone asked about your pan?', 'That is the moment your link pays. Give 15%, get 15%.',
             T['AFF · nudge-1'], 'aff-nudge-1', True)
    acts = [{'temporary_id': 'hold', 'type': 'conditional-split',
             'data': {'profile_filter': {'condition_groups': [G({'type': 'profile-sample', 'percentage': 10})]}},
             'links': {'next_if_true': None, 'next_if_false': 'w0'}}]
    prev = None
    for i, d in enumerate(SLOTS):
        gap = d if i == 0 else d - SLOTS[i - 1]
        acts.append(wait(f'w{i}', gap, f'b{i}'))
        # A2 (3 dagen na A1 in het vorige slot) en daarna A1
        acts.append(email(f'b{i}', dict(m2, name=f'{A2} · nudge-1 · d{d}'), a2_filters, f'a{i}'))
        f1 = [not_yet_a1] + settled + no_review_3d + ([] if d >= CAP else [has_proof])
        acts.append(email(f'a{i}', dict(m1, name=f'{A1} · announce · d{d}'), f1, f'w{i+1}'))
    last = SLOTS[-1] + 3
    acts.append(wait(f'w{len(SLOTS)}', 3, 'bz'))
    acts.append(email('bz', dict(m2, name=f'{A2} · nudge-1 · d{last}'), a2_filters, None))
    acts[0]['links']['next_if_false'] = 'w0'
    # eerste A2-kopie (dag 6) kan nooit vuren (geen eerdere A1); weglaten houdt de flow kleiner
    acts = [a for a in acts if a['temporary_id'] != 'b0']
    for a in acts:
        if a['links'].get('next') == 'b0':
            a['links']['next'] = 'a0'
    return 'AFF S1 · Activatie nieuwe kopers', {'triggers': [{'type': 'metric', 'id': ENROLLED}], 'profile_filter': pf,
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
    for name, d in [s1()] + s5():
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
        json.dump(out, open('/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/aff/flows.json', 'w'), ensure_ascii=False, indent=1)
