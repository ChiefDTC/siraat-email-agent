"""Bouwt op 8 nov 2026 de twee DRAFT-flows 'v4 · Checkout abandonment · REDEEM 13.78 A/B · DRAFT' en 'v4 · Cart abandonment · REDEEM 13.78 A/B · DRAFT'.
Leest de live definities van QUBUQV (checkout) en TZG9Mx (cart) alleen (GET), wijzigt ze nooit.
Opbouw (beide flows): trigger, flowfilters, reentry en eerste mail (C1 na 10 min, K1/K1-ACC na 15 min) zoals live, dan profile-sample 50/50:
  arm A (true)  = exacte kopie van het live v4-pad na de eerste mail (templates gekloond via /api/template-clone);
  arm B (false) = wacht tot ~4 uur na de trigger, R1 (code), 20 uur, R2 (verwijzing), dan de educatieve mails C2/C3 of K2 zonder 10%-code
                  (code-vrije kopie van de live HTML: BF-CVX79-blok, -zinnen en -links eruit); C4/K3 vervallen.
Het oude 0%-pad uit de live flows (Old · ...) wordt niet meegenomen. Alle mails status draft, flow status draft. Nooit live zetten.
ID's in ids.json naast dit script (cache: opnieuw draaien maakt geen dubbele templates). Flows maken alleen met --create.
Draaien vanuit de scratchpad golive-map (kl.py)."""
import json, os, re, sys, time
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api
T = os.path.dirname(os.path.abspath(__file__)); N = os.path.dirname(T)
IDS_F = os.path.join(T, 'ids.json')
IDS = json.load(open(IDS_F)) if os.path.exists(IDS_F) else {}
def save(): json.dump(IDS, open(IDS_F, 'w'), indent=1, sort_keys=True)
TAG = 'REDEEM A/B DRAFT'


def ok(r, what):
    if 'data' not in r: raise SystemExit('%s mislukt: %s' % (what, json.dumps(r)[:800]))
    return r['data']


def live(fid):
    return ok(api('GET', '/api/flows/%s?additional-fields[flow]=definition' % fid), 'GET ' + fid)['attributes']['definition']


def clone(key, tid, label):
    if key not in IDS:
        IDS[key] = ok(api('POST', '/api/template-clone', {'data': {'type': 'template', 'id': tid, 'attributes': {'name': '%s · %s (kopie %s)' % (TAG, label, tid)}}}), 'clone ' + tid)['id']
        save(); time.sleep(1)
    return IDS[key]


def create_tpl(key, name, html):
    if key not in IDS:
        IDS[key] = ok(api('POST', '/api/templates', {'data': {'type': 'template', 'attributes': {'name': name, 'editor_type': 'CODE', 'html': html}}}), 'template ' + key)['id']
        save(); time.sleep(1)
    return IDS[key]


# ---------- code-vrije kopie (arm B): BF-CVX79 / extra 10% eruit ----------
SENT = {'BF-CVX79 is already applied, and your 5 gifts are still pending on this cart.': 'Your 5 gifts are still pending on this cart.',
        'BF-CVX79 takes an extra 10% off, already applied with the button below.': 'Saved exactly as you left it.',
        'BF-CVX79 is already applied to your set.': 'Your set is saved exactly as you left it.',
        'BF-CVX79 is already applied, on your pan or on the set.': 'Your cart is saved exactly as you left it.',
        'BF-CVX79 is already applied, on your cart or on the pan.': 'Your cart is saved exactly as you left it.',
        'Your cart is saved, BF-CVX79 is applied, and the 5 gifts ship with it.': 'Your cart is saved, and the 5 gifts ship with it.'}


def nocode(h, old_pre, new_pre):
    h, n = re.subn(r'<tr><td class="pad"[^>]*>\s*<table bgcolor="#FFB800"[^>]*>(?:(?!</table>).)*?VIP BLACK FRIDAY DEAL.*?</table>\s*</td></tr>', '', h, flags=re.S)
    assert n == 1, 'deal-blok niet gevonden'
    for a, b in SENT.items(): h = h.replace(a, b)
    # checkout-knoppen: responsive_checkout_url zonder discount
    h = h.replace("|default:'https://siraatskitchen.com/discount/BF-CVX79?redirect=/cart' }}", "|default:'https://siraatskitchen.com/cart?' }}")
    h = h.replace('&amp;discount=BF-CVX79', '').replace('&discount=BF-CVX79', '')
    # /discount/BF-CVX79?redirect=<pad>%3F<utm> -> <pad>?<utm>
    def dec(m):
        p = m.group(1).replace('%3F', '?').replace('%26', '&amp;').replace('%3D', '=')
        return 'href="https://siraatskitchen.com' + p + '"'
    h = re.sub(r'href="https://siraatskitchen\.com/discount/BF-CVX79\?redirect=([^"]*)"', dec, h)
    assert old_pre in h, 'previewtekst niet gevonden'
    h = h.replace(old_pre, new_pre)
    left = [x for x in ('BF-CVX79', '10%', 'discount/', 'discount=') if x in h]
    assert not left, left
    return h


NEWPRE = {'C2': 'Why I had our pan lab-tested.', 'C2-ACC': 'Still in your cart. 5 gifts ship with it, either way.',
          'C3-S': 'Every piece, the same tested titanium surface.', 'C3-P': 'Most of our 100,000+ customers start with one.',
          'C3-ACC': 'We started with cutting boards too.', 'K2-RETURNING': 'You know how it works. Your cart is saved.',
          'K2-NEW': 'Our warranty runs 75 years. Here is the math.'}


def strip_meta(h):
    return re.sub(r'\A\s*<!--.*?-->\s*', '', h, count=1, flags=re.S)


R = {}
for mid in ('r1-checkout', 'r2-checkout', 'r1-cart', 'r2-cart'):
    R[mid] = create_tpl('tpl_' + mid, '%s · %s · $13.78 %s' % (TAG, mid.upper(), 'in your account' if mid.startswith('r1') else 'expires in 4 hours'),
                        strip_meta(open(os.path.join(N, mid + '.klaviyo.html')).read()))


def acts_by_id(d): return {a['id']: a for a in d['actions']}


def msg_copy(a, tpl, name=None, pre=None):
    m = {k: v for k, v in a['data']['message'].items() if k != 'id'}
    m['template_id'] = tpl
    if name: m['name'] = name
    if pre is not None: m['preview_text'] = pre
    return m


def email(t, m, nxt): return {'temporary_id': t, 'type': 'send-email', 'data': {'message': m, 'status': 'draft'}, 'links': {'next': nxt}}
def wait(t, data, nxt): return {'temporary_id': t, 'type': 'time-delay', 'data': data, 'links': {'next': nxt}}
def split(t, pf, y, n): return {'temporary_id': t, 'type': 'conditional-split', 'data': {'profile_filter': pf}, 'links': {'next_if_true': y, 'next_if_false': n}}
def W(unit, v): return {'unit': unit, 'value': v, 'secondary_value': None, 'timezone': 'profile'}
AB = {'condition_groups': [{'conditions': [{'type': 'profile-sample', 'percentage': 50}]}]}


def copy_path(flow, A, start, prefix, out, nocode_mode=False):
    """Kopieert het live pad vanaf actie-id start; geeft de temporary_id terug. nocode_mode: alleen tot en met de C3/K2-mails, codevrij, zonder C4/K3."""
    if start is None: return None
    a = A[start]; t = prefix + start
    if any(x['temporary_id'] == t for x in out): return t
    if a['type'] == 'send-email':
        name = a['data']['message']['name']
        if nocode_mode:
            if name.startswith(('C4', 'CODE', 'K3')): return None
            src = a['data']['message']['template_id']
            key = 'nocode_%s_%s' % (flow, src)
            if key not in IDS:
                h = ok(api('GET', '/api/templates/%s' % src), 'GET tpl ' + src)['attributes']['html']
                create_tpl(key, '%s · %s · %s zonder 10%% (uit %s)' % (TAG, flow, name, src), nocode(h, a['data']['message']['preview_text'], NEWPRE[name]))
            m = msg_copy(a, IDS[key], 'B · %s · no code' % name, NEWPRE[name])
        else:
            m = msg_copy(a, clone('clone_%s_%s' % (flow, a['data']['message']['template_id']), a['data']['message']['template_id'], '%s · %s' % (flow, name)),
                         'A · %s' % name)
        e = email(t, m, None); out.append(e)
        e['links']['next'] = copy_path(flow, A, a['links']['next'], prefix, out, nocode_mode)
    elif a['type'] == 'time-delay':
        nxt = copy_path(flow, A, a['links']['next'], prefix, out, nocode_mode)
        if nxt is None: return None
        out.append(wait(t, a['data'], nxt))
    elif a['type'] == 'conditional-split':
        if nocode_mode: return None   # de enige splits na C3/K2 zijn de C4/K3-code-splits
        out.append(split(t, a['data']['profile_filter'], None, None)); s = out[-1]
        s['links']['next_if_true'] = copy_path(flow, A, a['links']['next_if_true'], prefix, out)
        s['links']['next_if_false'] = copy_path(flow, A, a['links']['next_if_false'], prefix, out)
    else:
        raise SystemExit('onbekend actietype ' + a['type'])
    return t


def arm_b(flow, A, first_mail_id, first_wait_min, after_r2_live_wait, prefix, out):
    """R1 op ~4 uur na de trigger, R2 20 uur later, dan de educatieve mails zonder code."""
    filt = A[first_mail_id]['data']['message']
    base = {k: v for k, v in filt.items() if k != 'id'}
    def rmsg(mid, name, subj, pre):
        m = dict(base); m.update({'name': name, 'subject_line': subj, 'preview_text': pre, 'template_id': R[mid], 'from_label': 'Benjamin from Siraat',
                                  'smart_sending_enabled': False, 'custom_tracking_params': None, 'add_tracking_params': False}); return m
    edu = None
    if after_r2_live_wait:
        wa = A[after_r2_live_wait]
        nxt = copy_path(flow, A, wa['links']['next'], prefix + 'e', out, nocode_mode=True)
        out.append(wait(prefix + 'w-edu', wa['data'], nxt)); edu = prefix + 'w-edu'
    out.append(email(prefix + 'r2', rmsg('r2-' + flow, 'B · R2 · $13.78 expires in 4 hours', 'Your $13.78 expires in 4 hours',
                                         'The code in my last email stops working in about 4 hours. This is the last email about it.'), edu))
    out.append(wait(prefix + 'w20h', W('hours', 20), prefix + 'r2'))
    out.append(email(prefix + 'r1', rmsg('r1-' + flow, 'B · R1 · You have $13.78 in your account', 'You have $13.78 in your account',
                                         'Benjamin here. A $13.78 code for the order you started, good for 24 hours.'), prefix + 'w20h'))
    out.append(wait(prefix + 'w4h', W('minutes', 240 - first_wait_min), prefix + 'r1'))
    return prefix + 'w4h'


def first_mail(flow, A, mid, nxt):
    a = A[mid]; tpl = clone('clone_%s_%s' % (flow, a['data']['message']['template_id']), a['data']['message']['template_id'], '%s · %s' % (flow, a['data']['message']['name']))
    return email('f' + mid, msg_copy(a, tpl, a['data']['message']['name']), nxt)


def build_checkout():
    d = live('QUBUQV'); A = acts_by_id(d); out = []
    # live v4-pad: entry split (100%) -> true -> wacht 10 min -> C1 -> wacht 1d 08:30 -> C2 ...
    entry = A[d['entry_action_id']]; w10 = A[entry['links']['next_if_true']]; c1 = w10['links']['next']
    after_c1 = A[c1]['links']['next']          # wacht 1 dag 08:30 (naar C2)
    a_start = copy_path('checkout', A, after_c1, 'a', out)
    b_start = arm_b('checkout', A, c1, w10['data']['value'], after_c1, 'b', out)
    out.append(split('ab', AB, a_start, b_start))
    out.append(first_mail('checkout', A, c1, 'ab'))
    out.append(wait('w10', w10['data'], 'f' + c1))
    return {'triggers': d['triggers'], 'profile_filter': d['profile_filter'], 'reentry_criteria': d.get('reentry_criteria'),
            'entry_action_id': 'w10', 'actions': out}


def build_cart(checkout_draft_id):
    d = live('TZG9Mx'); A = acts_by_id(d); out = []
    entry = A[d['entry_action_id']]; w15 = A[entry['links']['next_if_true']]; ps = A[w15['links']['next']]   # productsplit pan/acc
    branches = {}
    for side, mid in (('pan', ps['links']['next_if_true']), ('acc', ps['links']['next_if_false'])):
        after = A[mid]['links']['next']          # pan: wacht 2d 08:00 naar K2; acc: wacht 3d 09:00 naar K3-split
        a_start = copy_path('cart', A, after, 'a' + side, out)
        b_start = arm_b('cart', A, mid, w15['data']['value'], after if side == 'pan' else None, 'b' + side, out)
        out.append(split('ab' + side, AB, a_start, b_start))
        out.append(first_mail('cart', A, mid, 'ab' + side)); branches[side] = 'f' + mid
    out.append(split('ps', ps['data']['profile_filter'], branches['pan'], branches['acc']))
    out.append(wait('w15', w15['data'], 'ps'))
    pf = json.loads(json.dumps(d['profile_filter']))
    if checkout_draft_id:   # ook geen mail uit de nieuwe checkout-draft in 7 dagen (naast QUBUQV), voor als die de live checkout vervangt
        pf['condition_groups'].append({'conditions': [{'type': 'profile-metric', 'metric_id': 'YkRM4Q', 'measurement': 'count',
            'measurement_filter': {'type': 'numeric', 'operator': 'equals', 'value': 0}, 'timeframe_filter': {'type': 'date', 'operator': 'in-the-last', 'unit': 'day', 'quantity': 7},
            'metric_filters': [{'property': '$flow', 'filter': {'type': 'string', 'operator': 'equals', 'value': checkout_draft_id}}]}]})
    return {'triggers': d['triggers'], 'profile_filter': pf, 'reentry_criteria': d.get('reentry_criteria'), 'entry_action_id': 'w15', 'actions': out}


def create(key, name, definition):
    if key in IDS: print(key, 'bestaat al', IDS[key]); return IDS[key]
    json.dump(definition, open(os.path.join('/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/redeem', key + '.def.json'), 'w'), indent=1)
    r = api('POST', '/api/flows', {'data': {'type': 'flow', 'attributes': {'name': name, 'definition': definition}}})
    f = ok(r, 'flow ' + key); IDS[key] = f['id']; save()
    print(key, f['id'], f['attributes'].get('status')); return f['id']


if __name__ == '__main__':
    dc = build_checkout(); print('checkout acties', len(dc['actions']))
    if '--create' in sys.argv:
        cid = create('flow_checkout', 'v4 · Checkout abandonment · REDEEM 13.78 A/B · DRAFT', dc)
        dk = build_cart(cid); print('cart acties', len(dk['actions']))
        create('flow_cart', 'v4 · Cart abandonment · REDEEM 13.78 A/B · DRAFT', dk)
    print(json.dumps(IDS, indent=1))
