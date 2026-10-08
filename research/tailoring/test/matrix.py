"""Productmatrix: rendert per productcategorie de mails die die klant in elke flow krijgt (routing uit 03-routing.md en
klaviyo/flows/v4-flow-system.md, nieuwe klant, US) en controleert per categorie welke blokken wel en niet mogen verschijnen.
Gebruik: python3 matrix.py [--dump=<map>] [--only=apron,pizza]
  --dump: schrijft per cel de platte tekst (<map>/<cat>/<flow>-<mail>.txt) om te lezen.
Exitcode 1 bij een FOUT. Samples: python3 mksamples.py (samples/<trig>_x_<cat>.json)."""
import sys, os, re, json, subprocess, html as H
T = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(T, '..', '..', '..'))
V = os.path.join(ROOT, 'klaviyo', 'templates', 'v3'); SH = os.path.join(ROOT, 'klaviyo', 'templates', 'partials', 'shared')
sys.path.insert(0, os.path.join(T, 'pylib')); sys.path.insert(0, T)
import django
from django.conf import settings
settings.configure(TEMPLATES=[{'BACKEND': 'django.template.backends.django.DjangoTemplates', 'OPTIONS': {'libraries': {'kl': 'kltags'}, 'builtins': ['kltags']}}])
django.setup()
from django.template import engines
from mksamples import CATS
OPT = {a.split('=', 1)[0]: (a.split('=', 1)[1] if '=' in a else '1') for a in sys.argv[1:] if a.startswith('--')}

SET = {'set6', 'set12', 'setbig', 'setall'}; PANPRO = {'mini', 'small', 'standard', 'large'}; FORM = {'deep', 'wok', 'crepe'}
KOOK = PANPRO | FORM | {'pizza', 'roast', 'pot'}
ACC = {'lid', 'apron', 'board', 'utensil', 'mill', 'sheets', 'giftcard'}

def route(c):
    """Mails per flow voor een nieuwe klant met alleen dit product (US). Geeft {flow: [mail, ...]}."""
    t, price, _ = CATS[c]; kook = c in KOOK or c in SET
    r = {}
    if kook:
        c3 = 'c3-s' if (c in SET or price >= 300) else ('c3-p' if c in PANPRO and price < 250 else None)
        r['checkout'] = ['c1', 'c2'] + ([c3] if c3 else []) + ['c4', 'c4-nocode']
    else:
        r['checkout'] = ['c1', 'c2-acc', 'c3-acc', 'c4', 'c4-nocode']
    words = ('Hammer', 'Pan', 'Pot', 'ookware', 'Everything', 'fanne', 'Prep Bundle')
    kw = any(w in t for w in words)
    r['cart'] = ['k1', 'k2-new', 'k3', 'k3-nocode'] if kw else ['k1-acc', 'k3', 'k3-nocode']
    r['browse'] = ['b1', 'b2-clicked', 'b2-notclicked'] if kw else ['b1-acc', 'b2-clicked']
    if c in SET or price >= 300: p3 = 'p3-set'
    elif c in PANPRO | FORM: p3 = 'p3-pan'
    elif c in KOOK: p3 = 'p3-accessory'
    elif c == 'giftcard': p3 = None
    elif c == 'apron': p3 = 'p3-apron'
    else: p3 = 'p3-accessory'
    p2 = c in PANPRO | FORM | SET          # build_flows.py P2_TITELS: geen eerste-ei-gids bij alleen pizza steel, roasting pan of pot
    r['post-purchase'] = ['p1-first'] + (['p2'] if p2 else []) + ([p3, p3 + '-nocode'] if p3 else [])
    r['winback'] = (['r1-set'] if (c in SET or price >= 300) else ['r1-pan']) if kook else ['r1-acc']
    r['winback'] += ['r2', 'r2-nocode']
    r['vip'] = ['v1', 'v1-nocode', 'v2']
    r['anniversary'] = ['n1', 'n2', 'n2-nocode'] if kook else []
    return r

TRIG = {'checkout': 'co', 'cart': 'atc', 'browse': 'vp', 'post-purchase': 'po', 'winback': 'po', 'vip': 'po', 'anniversary': 'po'}
FLOWDIR = {'checkout': 'checkout', 'cart': 'cart', 'browse': 'browse', 'post-purchase': 'post-purchase', 'winback': 'winback', 'vip': 'vip', 'anniversary': 'anniversary'}
_exp = {}
def expanded(flow, mail):
    k = (flow, mail)
    if k not in _exp:
        src = os.path.join(V, FLOWDIR[flow], mail + '.html')
        if not os.path.exists(src): _exp[k] = None; return None
        out = os.path.join(T, 'out', 'mx-%s.exp.html' % mail)
        r = subprocess.run([sys.executable, os.path.join(T, 'expand.py'), src, os.path.join(V, FLOWDIR[flow], 'assets'), '/dev/null', out], capture_output=True, text=True)
        if r.returncode: raise RuntimeError('expand %s: %s' % (mail, r.stderr[-300:]))
        _exp[k] = engines['django'].from_string(open(out).read().replace('{{IMG}}', 'assets').replace('{{SHARED}}', 'shared'))
    return _exp[k]

def render(flow, mail, c):
    tpl = expanded(flow, mail)
    if tpl is None: return None
    ev = json.load(open(os.path.join(T, 'samples', '%s_x_%s.json' % (TRIG[flow], c))))
    return tpl.render({'event': ev, 'first_name': 'Sarah', 'person': {}, 'organization': {'name': "Siraat's Kitchen", 'full_address': '[address]'}})

def text(h):
    h = re.sub(r'<style.*?</style>|<!--.*?-->', '', h, flags=re.S)
    h = re.sub(r'<div class="ug-mob".*?<!--<!\[endif\]-->', '', h, flags=re.S)   # mobiele kopie van blokken niet dubbel tellen
    t = H.unescape(re.sub(r'<[^>]+>', '\n', h))
    return '\n'.join(x.strip() for x in t.split('\n') if x.strip())

def imgs(h): return re.findall(r'<img[^>]+src="([^"]+)"', h)

# ---------- verwachtingen per categorie ----------
# PAN_TALK: uitleg over de pan als hoofdzaak; mag niet in een mail aan iemand die alleen een accessoire koos.
PAN_TALK = ['No PFAS. No coating', 'The 11-inch is our best seller', 'first egg', 'Titanium vs. coated', 'One pan.']
NAME = {'mini': 'Mini', 'small': 'Small', 'standard': 'Standard', 'large': 'Large', 'deep': 'deep pan', 'wok': 'wok', 'crepe': 'crêpe',
        'pizza': 'pizza steel', 'roast': 'roasting pan', 'pot': 'pot', 'set6': '6-piece', 'set12': '12-piece', 'setbig': 'set',
        'lid': 'lid', 'apron': 'apron', 'board': 'board', 'utensil': 'utensil', 'mill': 'mill', 'sheets': 'sheets', 'giftcard': 'gift card'}
ABOUT_FLOWS = {'checkout': 'c1', 'cart': None, 'browse': None, 'post-purchase': None, 'winback': None}

def checks(c, flow, mail, h, tx):
    """Fouten voor deze cel (productmatrix 10-productmatrix.md, sectie Na)."""
    F = []; low = tx.lower()
    if c in ACC:
        for p in PAN_TALK:
            if p.lower() in low: F.append('panuitleg "%s" bij %s' % (p, c))
    if c == 'apron':   # claims.md schort: PVC-coating, nooit naast "no coating(s)"
        for m in __import__('re').finditer('no coating', low):
            if 'apron' in low[max(0, m.start() - 300):m.start() + 300]: F.append('"no coating" vlak bij de schort'); break
    if c in KOOK | SET and 'you started with an accessory' in low: F.append('kookgerei aangesproken als accessoire')
    if c in ('pot', 'pizza', 'roast') and flow in ('winback', 'anniversary', 'post-purchase') and 'your pan ' in low.split('\n', 1)[-1].replace('your pan pro', '').replace('?', ' ') + ' ':
        F.append('"your pan" bij een %s' % c)
    need_about = {'c1'} | ({'k1', 'k2-new'} if c in KOOK | SET and c not in PANPRO else set()) | ({'k1-acc', 'b1-acc'} if c in ACC else set())
    need_goes = ({'c1', 'r1-pan', 'v1', 'v1-nocode'} | ({'k2-new'} if c not in PANPRO else set())) if c != 'giftcard' else set()
    need_goes1 = {'p3-pan', 'p3-pan-nocode', 'p3-set', 'p3-set-nocode'}
    if mail in need_about and 'data-about="%s"' % ('standard' if c == 'panpro' else c) not in h: F.append('geen productblok data-about="%s"' % c)
    if (mail in need_goes or mail in need_goes1) and 'data-goes="%s"' % c not in h: F.append('geen goes-blok data-goes="%s"' % c)
    return F

# eigen productregels per categorie: wat moet de klant zien (tekst) in de eerste mail van de flow
MUST = {
 ('apron', 'c1'): ['16-oz canvas', 'Adjustable', 'ABOUT YOUR APRON', 'Machine washable?', 'Deborah G.', 'Salt & Pepper Mill Set'],
 ('pizza', 'c1'): ['ABOUT YOUR PIZZA STEEL', 'Sergio C.', 'Goes with your pizza steel'],
 ('set12', 'c1'): ['ABOUT YOUR 12-PIECE SET', 'Why two parcels?', 'Lauren W.', 'Siraat Signature Apron'],
 ('pot', 'c1'): ['ABOUT YOUR POT'], ('standard', 'c1'): ['Pan Pro Mini', 'Stainless Steel Lid, 28 cm', 'Shop Pay Installments'],
 ('small', 'p3-pan'): ['One in three Small owners comes back for the Mini'], ('mini', 'p3-pan'): ['Pan Pro 11'],
 ('board', 'k1-acc'): ['ABOUT YOUR CUTTING BOARD', 'Knife marks?'], ('pot', 'r1-pan'): ['your pot'], ('wok', 'r1-pan'): ['Deep Pan Pro'],
 ('pizza', 'p3-accessory'): ['your pizza steel'], ('apron', 'b1-acc'): ['ABOUT THE APRON'],
}
# en wat er niet mag staan
MUSTNOT = {('apron', 'c1'): ['Titanium vs. coated'], ('wok', 'r1-pan'): ['Wok Pan Pro'], ('standard', 'p3-pan'): ['Titanium Cutting Board'],
 ('pizza', 'k1'): ['Why one pass is enough'], ('pot', 'k2-new'): ['15 coated pans']}

def main():
    only = OPT.get('--only'); cats = only.split(',') if only else list(CATS)
    dump = OPT.get('--dump'); fail = 0; rows = []
    for c in cats:
        for flow, mails in route(c).items():
            for m in mails:
                h = render(flow, m, c)
                if h is None: rows.append((c, flow, m, 'ontbreekt', [])); continue
                tx = text(h)
                F = checks(c, flow, m, h, tx)
                for w in MUST.get((c, m), []):
                    if w.lower() not in tx.lower(): F.append('mist "%s"' % w)
                for w in MUSTNOT.get((c, m), []):
                    if w.lower() in tx.lower(): F.append('bevat "%s"' % w)
                rows.append((c, flow, m, 'ok' if not F else 'FOUT', F))
                if dump:
                    d = os.path.join(dump, c); os.makedirs(d, exist_ok=True)
                    open(os.path.join(d, '%s-%s.txt' % (flow, m)), 'w').write(tx + '\n\n[IMG] ' + '\n[IMG] '.join(imgs(h)))
                    open(os.path.join(d, '%s-%s.html' % (flow, m)), 'w').write(h)
    for c, flow, m, st, F in rows:
        if st == 'FOUT' or OPT.get('--verbose'):
            for x in (F or ['']): print('%-4s %-9s %-13s %-14s %s' % ('FOUT' if F else 'ok', c, flow, m, x))
    nf = sum(1 for r in rows if r[3] == 'FOUT')
    print('matrix: %d cellen-mails, %d FOUT' % (len(rows), nf))
    sys.exit(1 if nf else 0)

if __name__ == '__main__': main()
