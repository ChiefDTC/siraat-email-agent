"""Maakte op 8 nov 2026 de DRAFT-flow Ubi9m5 'v4 · Tegoed ($12 in your account) · DRAFT' (trigger lijst TvEQxz 'Tegoed uitgegeven').
Templates: T1 VaRdvM, T2 V6dXap, T3 W6nhmt, T4 Xb9RTV (POST /api/templates, CODE, uit t*.klaviyo.html).
Niet opnieuw draaien zonder reden (maakt een tweede flow). Draaien vanuit de scratchpad golive-map (kl.py). Alles status draft."""
import json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api
I = {'t1': 'VaRdvM', 't2': 'V6dXap', 't3': 'W6nhmt', 't4': 'Xb9RTV', 'list': 'TvEQxz'}
EXP = "{{ person.siraat_credit_expires_at|format_date_string|date:'l, F j' }}"
def tf(op): return {'type': 'date', 'operator': op}
def pm(m, frame, mf=None): return {'type': 'profile-metric', 'metric_id': m, 'measurement': 'count', 'measurement_filter': {'type': 'numeric', 'operator': 'equals', 'value': 0}, 'timeframe_filter': tf(frame), 'metric_filters': mf}
def G(*c): return {'conditions': list(c)}
def msg(name, subj, pre, tpl, smart):
    return {'from_email': 'send@siraatskitchen.com', 'from_label': 'Benjamin from Siraat', 'reply_to_email': 'send@siraatskitchen.com', 'cc_email': None, 'bcc_email': None,
            'subject_line': subj, 'preview_text': pre, 'template_id': tpl, 'smart_sending_enabled': smart, 'transactional': False, 'add_tracking_params': False,
            'custom_tracking_params': None, 'additional_filters': None, 'name': name}
def email(t, m, nxt): return {'temporary_id': t, 'type': 'send-email', 'data': {'message': m, 'status': 'draft'}, 'links': {'next': nxt}}
def wait(t, d, nxt): return {'temporary_id': t, 'type': 'time-delay', 'data': {'unit': 'days', 'value': d, 'secondary_value': None, 'timezone': 'profile', 'delay_until_time': '09:00:00'}, 'links': {'next': nxt}}
def split(t, f, y, n): return {'temporary_id': t, 'type': 'conditional-split', 'data': {'profile_filter': f}, 'links': {'next_if_true': y, 'next_if_false': n}}
pf = {'condition_groups': [G(pm('RSNxYV', 'flow-start')),   # geen order sinds flowstart (uit bij order)
      G(pm('USRsNP', 'flow-start', [{'property': 'CouponKey', 'filter': {'type': 'string', 'operator': 'equals', 'value': 'SIRAAT_CREDIT_12'}}])),
      G({'type': 'profile-not-in-flow', 'timeframe_filter': tf('alltime')})]}
has = {'condition_groups': [G({'type': 'profile-property', 'property': "properties['siraat_credit_code']", 'filter': {'type': 'existence', 'operator': 'is-set'}})]}
acts = [split('hold', {'condition_groups': [G({'type': 'profile-sample', 'percentage': 10})]}, None, 'w0'),   # 10% holdout: geen code, geen mail
        wait('w0', 0, 'e1'),
        email('e1', msg('TEGOED T1 · uitgifte', 'You have $12 in your account', 'Benjamin here. A $12 code for your next order, good for 30 days.', I['t1'], True), 'w14'),
        wait('w14', 14, 's2'), split('s2', has, 'e2', None),
        email('e2', msg('TEGOED T2 · dag 14', 'Your $12 is still in your account', 'Unused, and good until ' + EXP + '. Same code as before.', I['t2'], True), 'w13'),
        wait('w13', 13, 'e3'),
        email('e3', msg('TEGOED T3 · nog 3 dagen', 'Your $12 expires in 3 days', 'It stops working on ' + EXP + '. After that it is gone.', I['t3'], False), 'w2'),
        wait('w2', 2, 'e4'),
        email('e4', msg('TEGOED T4 · laatste dag', 'Last day for your $12', 'Less than 24 hours left. This is the last email about it.', I['t4'], False), None)]
if __name__ == '__main__' and '--create' in sys.argv:
    d = api('POST', '/api/flows', {'data': {'type': 'flow', 'attributes': {'name': 'v4 · Tegoed ($12 in your account) · DRAFT',
            'definition': {'triggers': [{'type': 'list', 'id': I['list']}], 'profile_filter': pf, 'entry_action_id': 'hold', 'actions': acts}}}})
    print(json.dumps(d)[:400])
