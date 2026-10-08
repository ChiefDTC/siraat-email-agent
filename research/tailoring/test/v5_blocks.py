"""Test van alle v5-bouwstenen (scripts/v5lib.py) per signaal en per markt. Gebruik: python3 -I v5_blocks.py [--dump=<map>]
Bouwt research/tailoring/test/v5/demo.html voor elk signaal (order, checkout, cart, browse, profile) met expand.py,
rendert met Django op US, UK, AU, CA, SG, EU en onbekend, en controleert:
 - macro's: maat, prijs, verzendregel, gifts-tekst en markt-takken geven per markt precies de verwachte tekst
 - geen USD en geen inch buiten de US, US-only producten nooit buiten de US (v5checks.market_problems)
 - gifts5 heeft altijd de vier gift-beelden (ook de free shipping-afbeelding), reviews3 nooit R017
 - bundel: juiste bundel per titel, US-only bundels buiten de US het algemene blok
 - cross-sell: nooit een product uit de order of uit person.siraat_owned (lijst), op een matrix van orders en bezit
Exitcode 1 bij een FOUT."""
import sys, os, re, json, subprocess
T = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(T, '..', '..', '..'))
sys.path.insert(0, os.path.join(T, 'pylib')); sys.path.insert(0, T); sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import django
from django.conf import settings
settings.configure(TEMPLATES=[{'BACKEND': 'django.template.backends.django.DjangoTemplates', 'OPTIONS': {'libraries': {'kl': 'kltags'}, 'builtins': ['kltags']}}])
django.setup()
from django.template import engines
import v5checks as C
OPT = {a.split('=', 1)[0]: (a.split('=', 1)[1] if '=' in a else '1') for a in sys.argv[1:] if a.startswith('--')}
OUT = os.path.join(T, 'out'); os.makedirs(OUT, exist_ok=True)
SIGS = ['order', 'checkout', 'cart', 'browse', 'profile']
FAIL = []; OK = [0]
def ok(c, msg):
    if c: OK[0] += 1
    else: FAIL.append(msg)

def build(sig):
    src = os.path.join(T, 'v5', 'demo-%s.html' % sig)
    open(src, 'w').write('<!-- MARKET-SIGNAL: %s -->\n' % sig + open(os.path.join(T, 'v5', 'demo.html')).read())
    out = os.path.join(OUT, 'v5-demo-%s.exp.html' % sig)
    r = subprocess.run([sys.executable, os.path.join(T, 'expand.py'), src, os.path.join(T, 'v5', 'assets'), '/dev/null', out], capture_output=True, text=True)
    if r.returncode: sys.exit('expand %s: %s' % (sig, (r.stderr or r.stdout)[-500:]))
    return engines['django'].from_string(open(out).read().replace('{{IMG}}', 'assets').replace('{{SHARED}}', 'shared'))

def items_ev(sig, titles):
    """Basis-event met deze producttitels voor het signaal."""
    if sig in ('order', 'checkout'): return {'Items': titles, 'extra': {}}
    if sig == 'cart': return {'Product Name': titles[0] if titles else '', 'Price': 144}
    if sig == 'browse': return {'Name': titles[0] if titles else '', 'Price': '$144'}
    return {}

def render(tpl, sig, m, titles=(), owned=None):
    ev, p = C.market_ctx(sig, m, items_ev(sig, list(titles)))
    if owned is not None: p['siraat_owned'] = owned
    return tpl.render({'event': ev, 'person': p, 'first_name': 'Sarah', 'organization': {'name': "Siraat's Kitchen", 'full_address': '[address]'}})

def span(h, k):
    mo = re.search(r'<span data-t="%s">(.*?)</span>' % k, h, re.S)
    return re.sub(r'\s+', ' ', C.text(mo.group(1))).strip() if mo else None

# verwachte macro-uitkomst per markt (XX = onbekend)
EXP = {
 'size':  {'US': 'Pan Pro 11″', 'XX': 'Pan Pro 28 cm (11″)', '*': 'Pan Pro 28 cm'},
 'price': {'US': 'Pan Pro $144', 'UK': 'Pan Pro £124', 'AU': 'Pan Pro A$224', 'CA': 'Pan Pro C$224', 'SG': 'Pan Pro S$204', 'EU': 'Pan Pro €139', 'XX': 'Pan Pro'},
 'code':  {'US': '$129.60', 'UK': '£111.60', 'AU': 'A$201.60', 'CA': 'C$201.60', 'SG': 'S$183.60', 'EU': '€125.10', 'XX': ''},
 'ship':  {'US': 'Free shipping from the US', '*': 'Free shipping, duties paid'},
 'gifts': {'US': '$70 in gifts', 'UK': '£55 in gifts', 'AU': 'A$100 in gifts', 'CA': 'C$95 in gifts', 'SG': 'S$95 in gifts', 'EU': '€70 in gifts', 'XX': '4 free gifts'},
 'filter': {'US': 'Win a $450 PFAS water filter', 'UK': 'Win a £350 PFAS water filter', 'AU': 'Win a A$660 PFAS water filter', 'CA': 'Win a C$620 PFAS water filter', 'SG': 'Win a S$590 PFAS water filter', 'EU': 'Win a €410 PFAS water filter', 'XX': 'Win a PFAS water filter'},
 'if':    {'US': 'MARKET-US', 'UK': 'MARKET-UK', 'AU': 'MARKET-AUNZ', 'CA': 'MARKET-CA', 'SG': 'MARKET-SG', '*': 'MARKET-OTHER'},
 'int':   {'US': '', 'XX': '', '*': 'KNOWN-INT'},
 'unknown': {'XX': 'MARKET-UNKNOWN', '*': ''},
 'usonly': {'US': 'The 12-piece set, $599', '*': 'The 6-piece set'},
}

def main():
    dump = OPT.get('--dump')
    for sig in SIGS:
        tpl = build(sig)
        for m in C.MARKETS:
            if sig == 'browse' and m in ('AU', 'CA', 'SG', 'EU', 'UK'): pass
            h = render(tpl, sig, m, ['Titanium Hammered Pan Pro Standard'])
            if dump: open(os.path.join(dump, 'v5-%s-%s.html' % (sig, m)), 'w').write(h)
            for k, e in EXP.items():
                want = e.get(m, e.get('*'))
                got = span(h, k)
                ok(got == want, '%s/%s macro %s: kreeg %r, verwacht %r' % (sig, m, k, got, want))
            # regels op de hele demo (alle blokken staan erin)
            for x in C.market_problems(h, m): FAIL.append('%s/%s: %s' % (sig, m, x))
            for x in C.gifts_problems(h): FAIL.append('%s/%s: %s' % (sig, m, x))
            for x in C.review_problems(h): FAIL.append('%s/%s: %s' % (sig, m, x))
            ok(h.count('data-gift="') == 8, '%s/%s: niet 2x4 gift-beelden (%d)' % (sig, m, h.count('data-gift="')))
            ok(h.count('data-gifts-urgency') == 1, '%s/%s: urgentieregel ontbreekt' % (sig, m))
            ok(len(re.findall(r'data-rev="', h)) == 5, '%s/%s: reviews3 niet 3+2 kaarten' % (sig, m))
            ok(all(p in h for p in ('On quality', 'On delivery', 'On service', 'Verified buyer')), '%s/%s: pijlerlabels' % (sig, m))
            ok('Your future pan vs a PFAS pan' in h and 'Your future pan vs stainless steel' in h and 'Your future pan vs cast iron' in h, '%s/%s: vergelijkingen' % (sig, m))
            ok(not re.search(r'\{[%{]|\}\}|%\}', C.text(h)), '%s/%s: Django-restant' % (sig, m))
        # bundel per titel (order/checkout: event.Items)
        if sig in ('order', 'checkout'):
            B = [('Titanium Hammered Pan Set With Lids | 6-Pcs', 'set6', {'US': ['Buy 2, get 4 free.', 'Six pieces for $299', '$598'], 'UK': ['Six pieces for £249'], 'XX': ['Buy 2, get 4 free.']}),
                 ('Titanium Hammered Cookware Set | 12-Pcs', 'set12', {'US': ['12 pieces for $599', '$1,186']}),
                 ('Titanium Hammered Complete Edition', 'complete', {'US': ['Four pans for $399']}),
                 ('Titanium Hammered Cookware Set Pro', 'setpro', {}), ('Full Hammered Pro Edition', 'full', {}),
                 ('2 Pans + 2 Lids', 'duo2', {'US': ['Four pieces for $199', 'Bought one by one: $361.']}), ('Titanium Hammered Pan Pro Duo', 'panproduo', {}),
                 ('Titanium Hammered Pro Duo', 'produo', {}), ('Titanium Hammered Pan Pro Kit', 'kit', {}), ('Titanium Cook & Prep Bundle', 'cookprep', {}),
                 ('The Just Everything Bundle | 34-Pcs', 'everything', {}), ('Titanium Hammered Pan Pro Standard', 'generic', {})]
            for title, key, must in B:
                for m in C.MARKETS:
                    h = render(tpl, sig, m, [title])
                    got = re.findall(r'data-bundle="(\w+)"', h)
                    want = 'generic' if (key in ('set12', 'everything', 'duo2') and m != 'US') else key
                    ok(got == [want], '%s/%s bundel %s: kreeg %s, verwacht %s' % (sig, m, title, got, want))
                    for w in must.get(m, []): ok(w in re.sub(r'\s+', ' ', C.text(h)), '%s/%s bundel %s mist %r' % (sig, m, key, w))
        # cross-sell: nooit iets uit de order of uit siraat_owned
        if sig in ('order', 'checkout'):
            X = [(['Titanium Hammered Pan Pro Standard'], None), (['Titanium Hammered Pan Pro Standard', 'Titanium Hammered Pan Pro Mini'], None),
                 (['Titanium Hammered Pan Pro Small', 'Titanium Hammered Pan Pro Mini'], None), (['Titanium Hammered Pan Pro Large', 'Titanium Hammered Pan Pro Small'], None),
                 (['Titanium Hammered Pan Set With Lids | 6-Pcs'], None), (['Titanium Hammered Pan Set With Lids | 6-Pcs', 'Titanium Cutting Board (Anti-Microbial)'], None),
                 (['Titanium Hammered Deep Pan Pro', 'Titanium Hammered Wok Pan Pro'], None), (['Siraat Signature Apron (Moss)', 'Salt & Pepper Mill Set'], None),
                 (['Titanium Hammered Pan Pro Standard', 'Stainless Steel Lid', 'Titanium Cutting Board (Anti-Microbial)'], None),
                 (['Stainless Steel Lid'], ['panpro', 'panpro_standard', 'panpro_mini', 'lid', 'lid_28', 'board']),
                 (['Titanium Hammered Pan Pro Mini'], ['panpro', 'panpro_small', 'lid', 'lid_26']),
                 (['Titanium Hammered Cookware Set | 12-Pcs'], None), (['3 Litre Titanium Hammered Pot With Lid'], None),
                 (['The Just Everything Bundle | 34-Pcs'], None), (['Titanium Hammered Pan Pro Standard'], ['panpro_mini', 'lid_28', 'board', 'utensils', 'deep', 'wok', 'panpro_small', 'panpro_large']),
                 (['Plastic-Free Dishwasher Sheets'], None)]
            OWNS = {'mini': ['pan pro mini', 'pan set', '12-pcs', 'full hammered', 'everyth'], 'small': ['pan pro small', 'pan set', '12-pcs', 'everyth'],
                    'standard': ['pan pro standard', 'cookware set pro', 'complete edition', 'everyth'], 'large': ['pan pro large', 'pan set', '12-pcs', 'everyth'],
                    'deep': ['deep pan'], 'wok': ['wok'], 'crepe': ['crêpe'], 'board': ['cutting board'], 'utset': ['utensil'],
                    'apron': ['apron'], 'mill': ['mill'], 'set6': ['pan set', '12-pcs'], 'lid20': ['lid'], 'lid26': ['lid'], 'lid28': ['lid'], 'lid30': ['lid']}
            KEYS = {'mini': 'panpro_mini', 'small': 'panpro_small', 'standard': 'panpro_standard', 'large': 'panpro_large', 'deep': 'deep', 'wok': 'wok', 'crepe': 'crepe',
                    'board': 'board', 'utset': 'utensils', 'apron': 'apron', 'mill': 'mill', 'set6': 'set6', 'lid20': 'lid_20', 'lid26': 'lid_26', 'lid28': 'lid_28', 'lid30': 'lid_30'}
            for titles, own in X:
                for m in ('US', 'UK', 'XX'):
                    h = render(tpl, sig, m, titles, own)
                    sh = C.xsell_shown(h); low = ','.join(titles).lower()
                    for t in sh:
                        if t == 'none': continue
                        ok(not any(x in low for x in OWNS[t]), '%s/%s xsell %s toont %s uit de order' % (sig, m, titles, t))
                        ok(not own or KEYS[t] not in own, '%s/%s xsell %s toont %s uit siraat_owned' % (sig, m, titles, t))
                    ok(len(sh) >= 1, '%s/%s xsell %s: leeg blok' % (sig, m, titles))
                    if '34-Pcs' in titles[0]: ok(sh == ['none'], '%s xsell 34-delig moet de terugval tonen: %s' % (sig, sh))
                    if m == 'US' and titles == ['Titanium Hammered Pan Pro Standard'] and own is None:
                        ok(sh[:3] == ['lid28', 'mini', 'set6'] or sh[:2] == ['lid28', 'mini'], '%s xsell Standard: %s' % (sig, sh))
                        ok('$99' in re.sub(r'\s+', ' ', C.text(h)) and '$59' in C.text(h), '%s xsell Standard: prijzen Mini $99 en deksel $59' % sig)
                    if m == 'UK' and titles == ['Titanium Hammered Pan Pro Standard'] and own is None:
                        ok('£109' in C.text(h), '%s xsell UK: Mini £109' % sig)
                    # links (integratie 8 okt): een deksel-variant met code-link mag nooit twee keer ? of %3F krijgen
                    for href in re.findall(r'href="([^"]*)"', h):
                        q = href.split('redirect=', 1)[-1] if 'redirect=' in href else href
                        ok(q.upper().count('%3F') + q.count('?') <= 1, '%s/%s xsell link met dubbele query: %s' % (sig, m, href[:140]))
        # mpcc (integratie 8 okt): profielland alleen in het eigen veld country_code (zonder person.Country) telt ook
        if sig in ('browse', 'profile'):
            for m in C.MARKETS:
                if m == 'XX': continue
                ev, p = C.market_ctx(sig, m, items_ev(sig, ['Titanium Hammered Pan Pro Standard']))
                p.pop('Country', None); p['country_code'] = C.ISO[m]
                if sig == 'browse': ev.pop('Price', None)
                h = tpl.render({'event': ev, 'person': p, 'first_name': 'Sarah', 'organization': {'name': "Siraat's Kitchen", 'full_address': '[address]'}})
                for k in ('size', 'ship', 'gifts'):
                    want = EXP[k].get(m, EXP[k].get('*')); got = span(h, k)
                    ok(got == want, '%s/%s alleen country_code: macro %s kreeg %r, verwacht %r' % (sig, m, k, got, want))
    # xsell-links zonder code (pre = /products/, post = ?utm...): deksel-variant sluit met & aan
    import v5lib
    for pre, post in (('https://siraatskitchen.com/products/', '?utm_source=klaviyo&utm_medium=email'),
                      ('https://siraatskitchen.com/discount/HI10?redirect=/products/', '%3Futm_source%3Dklaviyo%26utm_medium%3Demail')):
        row = v5lib.xrow('lid28', {'pre': pre, 'post': post}, 'order', 'none')
        href = re.search(r'href="([^"]*)"', row).group(1); q = href.split('redirect=', 1)[-1]
        ok(q.upper().count('%3F') + q.count('?') == 1 and ('variant' in q) and ('utm_source' in q), 'xsell deksel-link %s' % href)
    print('v5-bouwstenen: %d ok, %d FOUT' % (OK[0], len(FAIL)))
    for f in FAIL[:60]: print('FOUT', f)
    sys.exit(1 if FAIL else 0)

if __name__ == '__main__': main()
