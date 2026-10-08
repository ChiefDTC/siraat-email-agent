"""v5-bouwstenen (8 okt 2026): markt-helper, macro's en generator-blokken voor scripts/build_template.py.

Eén plek voor alle landlogica (research/v5/01-markten.md). build_template.py roept aan:
  v5lib.block(naam, params, flow)   voor {{BLOCK:gifts5|reviews3|bundle|xsell|vs ...}}
  v5lib.expand(html, flow)          voor de inline macro's ({{IF:..}}, {{SIZE:..}}, {{PRICE:..}}, {{SHIP}}, {{GIFTS:..}} ...)
  v5lib.us_cond(flow)               voor productcard us="1" (vervangt de oude USCOND-tabel)
Documentatie met voorbeelden: PLAYBOOK.md h12, sectie "v5-bouwstenen".

Markten: US, CA, UK, EU (EURO-prijslijst), AU, NZ, SG, HK, ME (Midden-Oosten), REST (bekend land, geen eigen prijslijst), onbekend.
Signaal per flowtype (01-markten.md sectie 4):
  order    (post-purchase, winback, vip, anniversary)  event.extra.shipping_address.country_code
  cart     (Added to Cart)                             event|lookup:'_ip_country_code'
  checkout (Checkout Started)                          event.extra.presentment_currency, bij USD of geen valuta ook het profielland
  browse   (Viewed Product)                            profielland, terugval prijsnotatie in event.Price ('£', '€', '$x' zonder decimalen = US)
  profile  (welcome, site, sunset, ugc)                profielland
Profielland = person.Country (Klaviyo-tag uit de help-pagina "Template tags and variable syntax"), terugval eigen veld
person.country_code (ISO). Waarde is een naam ("United States") of ISO ("US"); elke vergelijking kent beide.
[CONTROLEREN in Klaviyo-preview op een echt profiel voor livegang.]
Elke voorwaarde staat binnen één {% with %} met korte variabelen (mc, mcur, mpc, mpr), zodat de HTML klein blijft.
"""
import os, re, json, html as _html

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
PARTIALS = os.path.join(ROOT, 'klaviyo', 'templates', 'partials')
CATALOG = os.path.join(ROOT, 'content', 'catalog', 'products.json')
REVSETS = os.path.join(ROOT, 'content', 'reviews', 'sets.json')

# ------------------------------------------------------------------ markten
EU_ISO = 'AT|BE|BG|HR|CZ|EE|FI|FR|DE|GR|HU|IE|IT|LV|LU|NL|SK|SI|ES'          # Shopify-markt EURO (prijslijst EUR)
EU_NAMES = ('Austria|Belgium|Bulgaria|Croatia|Czechia|Czech Republic|Estonia|Finland|France|Germany|Greece|Hungary|'
            'Ireland|Italy|Latvia|Luxembourg|Netherlands|Slovakia|Slovenia|Spain')
ME_ISO = 'AE|SA|KW|BH|OM|QA'
ME_NAMES = 'United Arab Emirates|Saudi Arabia|Kuwait|Bahrain|Oman|Qatar'
ME_CUR = 'AED|SAR|KWD|BHD|OMR|QAR'
NAMED = ['US', 'CA', 'UK', 'EU', 'AU', 'NZ', 'SG', 'HK', 'ME']
PRICED = ['US', 'CA', 'UK', 'EU', 'AU', 'NZ', 'SG']          # vaste prijslijst in Shopify: bedragen mogen
ISO = {'US': 'US', 'CA': 'CA', 'UK': 'GB', 'AU': 'AU', 'NZ': 'NZ', 'SG': 'SG', 'HK': 'HK'}
PNAMES = {'US': ['United States', 'US'], 'CA': ['Canada', 'CA'],
          'UK': ['United Kingdom', 'GB', 'UK'], 'AU': ['Australia', 'AU'], 'NZ': ['New Zealand', 'NZ'],
          'SG': ['Singapore', 'SG'], 'HK': ['Hong Kong', 'HK']}
CUR = {'US': 'USD', 'CA': 'CAD', 'UK': 'GBP', 'EU': 'EUR', 'AU': 'AUD', 'NZ': 'NZD', 'SG': 'SGD', 'HK': 'HKD'}
CAT_COUNTRY = {'US': 'US', 'CA': 'CA', 'UK': 'GB', 'EU': 'DE', 'AU': 'AU', 'NZ': 'NZ', 'SG': 'SG'}   # land in products.json
SYM = {'US': '$', 'CA': 'C$', 'UK': '\u00a3', 'EU': '\u20ac', 'AU': 'A$', 'NZ': 'NZ$', 'SG': 'S$'}

FLOWSIG = {'post-purchase': 'order', 'winback': 'order', 'vip': 'order', 'anniversary': 'order',
           'checkout': 'checkout', 'cart': 'cart', 'browse': 'browse',
           'welcome': 'profile', 'site': 'profile', 'sunset': 'profile', 'ugc': 'profile'}
PC = "person.Country"          # Klaviyo-tag voor het profielland; tweede bron person.country_code (mpcc) bij profiel en browse
PCC = "person|lookup:'country_code'"   # eigen ISO-veld (47 tot 72% gevuld, 01-markten.md sectie 4); gebonden als mpcc (integratie 8 okt)
# EU- en ME-lijsten één keer per {% with %} gebonden (meu, mme), zodat elke voorwaarde kort blijft
_L = {'order': (EU_ISO, ME_ISO), 'cart': (EU_ISO, ME_ISO), 'checkout': (None, ME_CUR),
      'profile': (EU_ISO + '|' + EU_NAMES, ME_ISO + '|' + ME_NAMES), 'browse': (EU_ISO + '|' + EU_NAMES, ME_ISO + '|' + ME_NAMES)}
def _lists(sig):
    eu, me = _L[sig]
    return (" meu='%s'" % eu if eu else '') + " mme='%s'" % me
BIND = {'order': "mc=event.extra.shipping_address.country_code" + _lists('order'),
        'cart': "mc=event|lookup:'_ip_country_code'" + _lists('cart'),
        'checkout': "mcur=event.extra.presentment_currency mpc=" + PC + "|default:'US'" + _lists('checkout'),
        'profile': "mpc=" + PC + " mpcc=" + PCC + _lists('profile'),
        'browse': "mpc=" + PC + " mpcc=" + PCC + " mpr=event.Price" + _lists('browse')}

def sig_of(flow):
    if flow in BIND: return flow
    return FLOWSIG.get(flow, 'profile')

def _prof(m, cc=True):
    """Profielland-voorwaarde voor markt m als lijst disjuncten (zonder haakjes: Django kent geen haakjes).
    cc=True: ook het eigen ISO-veld person.country_code (mpcc) als het land leeg is."""
    if m in PNAMES: d = ["mpc == '%s'" % n for n in PNAMES[m]] + (["not mpc and mpcc == '%s'" % (ISO[m])] if cc else [])
    elif m == 'EU': d = ["mpc and mpc in meu"] + (["not mpc and mpcc and mpcc in meu"] if cc else [])
    elif m == 'ME': d = ["mpc and mpc in mme"] + (["not mpc and mpcc and mpcc in mme"] if cc else [])
    else: raise KeyError(m)
    return d

def disj(m, sig):
    """Voorwaarde voor markt m als lijst disjuncten (elk een and-reeks), met de variabelen uit BIND[sig]."""
    if sig in ('order', 'cart'):
        if m in ISO: return ["mc == '%s'" % ISO[m]]
        if m == 'EU': return ["mc and mc in meu"]
        if m == 'ME': return ["mc and mc in mme"]
    if sig == 'profile':
        return _prof(m)
    if sig == 'browse':
        d = _prof(m)
        if m == 'US': d = d + ["not mpc and not mpcc and '$' in mpr and '.' not in mpr"]
        if m == 'UK': d = d + ["not mpc and not mpcc and '£' in mpr"]
        if m == 'EU': d = d + ["not mpc and not mpcc and '€' in mpr"]
        return d
    if sig == 'checkout':
        # presentment_currency is er altijd (01-markten: 100%); USD telt alleen als US bij een US- of leeg profielland
        # (mpc is in de checkout-binding standaard 'US', zie BIND)
        if m == 'US': return ["mcur == 'USD' and " + x for x in _prof('US', cc=False)]
        if m == 'ME': return ["mcur and mcur in mme"]
        return ["mcur == '%s'" % CUR[m]]
    raise KeyError((m, sig))

def known(sig):
    return {'order': 'mc', 'cart': 'mc', 'checkout': 'mcur', 'profile': 'mpc or mpcc', 'browse': 'mpc or mpcc or mpr'}[sig]

def cond(m, sig):
    if m == 'KNOWN': return known(sig)
    if m == 'PRICED': return ' or '.join(x for mm in PRICED for x in disj(mm, sig))
    return ' or '.join(disj(m, sig))

def wopen(sig): return '{%% with %s %%}' % BIND[sig]
WCLOSE = '{% endwith %}'

def chain(sig, vals, dflt='', bare=False, known_val=None):
    """Keten over markten. vals = [(markt of lijst markten, tekst)], known_val = tekst voor elk ander bekend land, dflt = onbekend.
    Gelijke opeenvolgende teksten worden samengevoegd. bare=True: geen eigen {% with %} (de omgeving bindt al)."""
    parts = []
    for m, v in vals:
        ms = m if isinstance(m, (list, tuple)) else [m]
        c = ' or '.join(cond(x, sig) for x in ms)
        if parts and parts[-1][1] == v: parts[-1][0] += ' or ' + c
        else: parts.append([c, v])
    if known_val is not None:
        if parts and parts[-1][1] == known_val: parts[-1][0] += ' or ' + known(sig)
        else: parts.append([known(sig), known_val])
    parts = [p for p in parts]
    if not parts: return dflt
    # staart met dezelfde tekst als de default mag weg
    while parts and parts[-1][1] == dflt: parts.pop()
    if not parts: return dflt
    out = ''.join(('{%% if %s %%}' if i == 0 else '{%% elif %s %%}') % c + v for i, (c, v) in enumerate(parts))
    out += ('{%% else %%}%s{%% endif %%}' % dflt) if dflt else '{% endif %}'
    return out if bare else wopen(sig) + out + WCLOSE

def us_cond(flow):
    """Voor productcard us="1": volledige voorwaarde zonder with is niet mogelijk; geeft (open, voorwaarde, sluit)."""
    sig = sig_of(flow)
    return wopen(sig), cond('US', sig), WCLOSE

# ------------------------------------------------------------------ catalogus
_CAT = None
def catalog():
    global _CAT
    if _CAT is None:
        d = json.load(open(CATALOG))
        _CAT = {p['handle']: p for p in d['products']}
    return _CAT

# sleutel -> (handle, variant-filter op titel of None = goedkoopste beschikbare variant ("vanaf"))
PKEY = {
 'mini': ('titanium-hammered-pan-pro-mini', None), 'small': ('titanium-hammered-pan-pro-small', None),
 'standard': ('original-siraat-100-pure-titanium-pan-with-hammered-pattern', None), 'large': ('titanium-hammered-pan-pro-large', None),
 'deep': ('titanium-hammered-deep-pan-pro', None), 'wok': ('titanium-hammered-wok-pan-pro', None),
 'crepe': ('titanium-hammered-crepe-pan-pro', None), 'pizza': ('titanium-hammered-pizza-steel', None),
 'roast': ('titanium-hammered-roasting-pan', None), 'lid': ('stainless-steel-lid', None),
 'lid20': ('stainless-steel-lid', '20CM'), 'lid26': ('stainless-steel-lid', '10"'), 'lid28': ('stainless-steel-lid', '11"'), 'lid30': ('stainless-steel-lid', '12"'),
 'board': ('titanium-cutting-board-v2', None), 'boardbundle': ('titanium-cutting-board-v2-bundle', None),
 'utset': ('siraat-pure-titanium-utensils-bundle', None), 'utensil': ('siraat-pure-titanium-utensils', None),
 'apron': ('siraat-signature-apron-moss', None), 'mill': ('salt-pepper-mill-set', None), 'sheets': ('dishwashing-detergent-sheets-fresh-lemon', None),
 'set6': ('titanium-hammered-pan-set-with-lids-6-pcs', None), 'set12': ('titanium-hammered-cookware-set', None),
 'setpro': ('titanium-hammered-cookware-set-pro', None), 'complete': ('the-hammered-collection', None),
 'full': ('full-hammered-pro-edition', None), 'everything': ('the-just-everything-bundle-34-pcs', None),
 'duo2': ('2-pans-and-2-lids', None), 'panproduo': ('titanium-hammered-pan-pro-duo', None), 'produo': ('titanium-pro-duo', None),
 'kit': ('titanium-hammered-pan-pro-kit', None), 'cookprep': ('titanium-hammered-pro-prep-cook-set', None),
 'panutensil': ('titanium-hammered-pan-pro-utensil-set', None), 'withlid': ('titanium-hammered-pan-pro-incl-lid', None),
}

def _variants(key):
    h, vf = PKEY[key] if key in PKEY else (key, None)
    p = catalog().get(h)
    if not p: raise KeyError('catalogus kent %s niet' % key)
    vs = p['variants']
    if vf: vs = [v for v in vs if vf in v['title']]
    if not vs: raise KeyError('variant %s niet gevonden in %s' % (vf, h))
    return p, vs

def us_only(key): return bool(_variants(key)[0].get('us_only'))
def handle(key): return PKEY[key][0] if key in PKEY else key

def amount(key, m, field='price'):
    """Bedrag (float) in markt m, of None (geen prijslijst, niet te koop, geen compare-at). Meerdere varianten: laagste."""
    if m not in CAT_COUNTRY: return None
    p, vs = _variants(key)
    if p.get('us_only') and m != 'US': return None
    c = CAT_COUNTRY[m]; xs = []
    for v in vs:
        pr = (v.get('prices') or {}).get(c)
        if pr and pr.get(field) is not None and (v.get('available') or {}).get(c, True): xs.append(float(pr[field]))
    return min(xs) if xs else None

def money(x, m):
    if x is None: return ''
    s = ('{:,.0f}'.format(x) if abs(x - round(x)) < 0.005 else '{:,.2f}'.format(x))
    return SYM[m] + s

def multi_variant(key):
    p, vs = _variants(key)
    return len({(v.get('prices') or {}).get('US', {}) and v['prices']['US'].get('price') for v in vs}) > 1

def price_vals(key, mult=1.0, field='price', frm=False):
    out = []
    for m in PRICED:
        a = amount(key, m, field)
        if a is not None: out.append((m, (('from ' if frm and multi_variant(key) else '') + money(a * mult, m))))
    return out

# ------------------------------------------------------------------ teksten per markt
SIZE_IN = {6: '2.4', 9: '3.5', 20: '8', 24: '9.5', 26: '10', 28: '11', 30: '12'}   # 6 en 9: zijhoogte deep pan en wok (about-blok)
def size_txt(cm, mode=''):
    i = SIZE_IN.get(int(cm), '%g' % (int(cm) / 2.54))
    us = '%s&Prime; (%s cm)' % (i, cm) if mode == 'both' else '%s&Prime;' % i
    return us, '%s cm' % cm, '%s cm (%s&Prime;)' % (cm, i)

def size_chain(sig, cm, mode='', bare=False):
    us, intl, unk = size_txt(cm, mode)
    return chain(sig, [('US', us)], unk, bare=bare, known_val=intl)

SHIP_US, SHIP_INT, SHIP_UNK = 'Free shipping from the US', 'Free shipping, duties paid', 'Free shipping, duties paid'
FR_TAIL = '30-day returns. 100,000+ happy customers.'
GIFT = {  # (verzending, e-book, mystery, filter, totaal) per markt; 01-markten.md sectie 6, DECISIONS 8 okt
 'US': (15, 30, 25, 450, 70), 'CA': (20, 40, 35, 620, 95), 'UK': (10, 25, 20, 350, 55), 'EU': (15, 30, 25, 410, 70),
 'AU': (20, 45, 35, 660, 100), 'NZ': (25, 50, 45, 820, 120), 'SG': (20, 40, 35, 590, 95)}
GIDX = {'ship': 0, 'ebook': 1, 'mystery': 2, 'filter': 3, 'total': 4}

def gifts_text(kind, sig, bare=False):
    up = kind.isupper(); k = kind.lower()
    def u(x): return x.upper() if up else x
    if k == 'total':
        vals = [(m, u('%s in gifts' % money(GIFT[m][4], m))) for m in GIFT]; dflt = u('4 free gifts')
    elif k == 'headline':
        vals = [(m, '%s in gifts, on us' % money(GIFT[m][4], m)) for m in GIFT]; dflt = '4 free gifts, on us'
    elif k == 'filterline':
        vals = [(m, 'a %s PFAS water filter' % money(GIFT[m][3], m)) for m in GIFT]; dflt = 'a PFAS water filter'
    elif k in GIDX:
        vals = [(m, money(GIFT[m][GIDX[k]], m)) for m in GIFT]; dflt = ''
    else:
        raise ValueError('onbekende GIFTS-macro: %s' % kind)
    return chain(sig, vals, dflt, bare=bare)

# ------------------------------------------------------------------ inline macro's
MACRO = re.compile(r'\{\{(IF|ELIF):([A-Z,]+)\}\}|\{\{(ELSE|ENDIF|USONLY|ELSEUS|/USONLY|SHIP|FRICTION|FRICTION:code)\}\}'
                   r'|\{\{SIZE:(\d+)(?::(both))?\}\}|\{\{(PRICE|WAS|FROM):([a-z0-9-]+)(?:\*([\d.]+))?(?:\|([^}]*))?\}\}|\{\{GIFTS:(\w+)\}\}')
SPECIAL = {'INT', 'NOTUS', 'UNKNOWN'}

def expand(h, flow):
    """Klapt de v5-macro's uit tot Klaviyo/Django. Fout bij een onbekende markt of een niet-gesloten IF/USONLY."""
    sig = sig_of(flow); stack = []
    def mlist(s):
        ms = s.split(',')
        for m in ms:
            if m not in NAMED + ['PRICED', 'KNOWN'] + list(SPECIAL): raise ValueError('onbekende markt in macro: %s' % m)
        return ms
    def rep(mo):
        g = mo.groups()
        if g[0] == 'IF':
            ms = mlist(g[1])
            if len(ms) > 1 and SPECIAL & set(ms): raise ValueError('INT/NOTUS/UNKNOWN niet combineren: %s' % g[1])
            stack.append(('IF', ms[0] if ms[0] in SPECIAL else ''))
            if ms[0] == 'INT': return wopen(sig) + '{%% if %s %%}{%% elif %s %%}' % (cond('US', sig), known(sig))
            if ms[0] == 'NOTUS': return wopen(sig) + '{%% if %s %%}{%% else %%}' % cond('US', sig)
            if ms[0] == 'UNKNOWN': return wopen(sig) + '{%% if %s %%}{%% else %%}' % known(sig)
            return wopen(sig) + '{%% if %s %%}' % ' or '.join(cond(m, sig) for m in ms)
        if g[0] == 'ELIF':
            if not stack or stack[-1][0] != 'IF' or stack[-1][1]: raise ValueError('ELIF zonder gewone IF (niet na INT/NOTUS/UNKNOWN)')
            ms = mlist(g[1])
            if SPECIAL & set(ms): raise ValueError('ELIF:%s kan niet' % g[1])
            return '{%% elif %s %%}' % ' or '.join(cond(m, sig) for m in ms)
        t = g[2]
        if t == 'ELSE':
            if not stack or stack[-1][0] != 'IF' or stack[-1][1] in ('INT', 'NOTUS', 'UNKNOWN'): raise ValueError('ELSE kan hier niet')
            return '{% else %}'
        if t == 'ENDIF':
            if not stack or stack[-1][0] != 'IF': raise ValueError('ENDIF zonder IF')
            stack.pop(); return '{% endif %}' + WCLOSE
        if t == 'USONLY':
            stack.append(('US', '')); return wopen(sig) + '{%% if %s %%}' % cond('US', sig)
        if t == 'ELSEUS':
            if not stack or stack[-1][0] != 'US': raise ValueError('ELSEUS buiten USONLY')
            return '{% else %}'
        if t == '/USONLY':
            if not stack or stack[-1][0] != 'US': raise ValueError('/USONLY zonder USONLY')
            stack.pop(); return '{% endif %}' + WCLOSE
        if t == 'SHIP':
            return chain(sig, [('US', SHIP_US)], SHIP_UNK, known_val=SHIP_INT)
        if t == 'FRICTION':
            return chain(sig, [('US', SHIP_US + '. ' + FR_TAIL)], SHIP_UNK + '. ' + FR_TAIL, known_val=SHIP_INT + '. ' + FR_TAIL)
        if t == 'FRICTION:code':
            return chain(sig, [('US', 'One use, already applied. ' + FR_TAIL)], 'One use, already applied. Duties paid. 30-day returns.')
        if g[3]:
            return size_chain(sig, int(g[3]), g[4] or '')
        if g[5]:
            kind, key, mult, fb = g[5], g[6], float(g[7] or 1), g[8] or ''
            if kind == 'WAS': return chain(sig, price_vals(key, mult, 'compare_at'), fb)
            return chain(sig, price_vals(key, mult, frm=(kind == 'FROM')), fb)
        if g[9]:
            return gifts_text(g[9], sig)
        return mo.group(0)
    out = MACRO.sub(rep, h)
    if stack: raise ValueError('niet gesloten: %s' % stack)
    left = re.findall(r'\{\{(?:IF|ELIF|SIZE|PRICE|WAS|FROM|GIFTS):[^}]*\}\}|\{\{(?:ELSE|ENDIF|USONLY|ELSEUS|/USONLY|SHIP|FRICTION)\}\}', out)
    if left: raise ValueError('onbekende macro: %s' % left[:3])
    return out

# ------------------------------------------------------------------ blokken
F = "font-family:Inter,Arial,Helvetica,sans-serif;"
SERIF = "font-family:'Instrument Serif','Times New Roman',serif;font-style:italic;"
def esc(x): return _html.escape(x, quote=False)
def tpl(name): return open(os.path.join(PARTIALS, 'blocks', name)).read()

def fill(t, kv, name):
    for k, v in kv.items(): t = t.replace('[[' + k + ']]', v)
    left = re.findall(r'\[\[\w+\]\]', t)
    if left: raise ValueError('blok %s mist %s' % (name, left))
    return t

# ---- gifts5
GIFT_TILES = [('ship', 'gift-shipping.jpg', 'Free shipping', 'Free<br>shipping', 'Included'),
              ('ebook', 'gift-ebook.jpg', 'The Green Clean E-Guide', 'The Green Clean<br>E-Guide', 'Included'),
              ('mystery', 'gift-mystery.jpg', 'Mystery gift', 'Mystery gift<br>in the box', 'Included'),
              ('filter', 'gift-filter.jpg', 'Chance to win a PFAS water filter', 'Win a PFAS<br>water filter', 'Chance to win')]
URGENCY = 'Your 4 gifts end when the fall sale ends.'

def gifts5(kv, sig):
    style = kv.get('style', 'grid')
    def val(k, dflt):
        return chain(sig, [(m, '%s value' % money(GIFT[m][GIDX[k]], m)) for m in GIFT], dflt, bare=True)
    tile = tpl('gifts5-tile.html') if style == 'grid' else tpl('gifts5-mini.html')
    tiles = {}
    for i, (k, img, alt, label, dflt) in enumerate(GIFT_TILES, 1):
        tiles['t%d' % i] = tile.replace('[[img]]', img).replace('[[alt]]', alt).replace('[[label]]', label).replace('[[value]]', val(k, dflt))
    urg = ('<div data-gifts-urgency="1" style="%sfont-size:13px;line-height:19px;font-weight:600;color:#AC3B19;text-align:center;padding-top:10px;">%s</div>' % (F, URGENCY)) if kv.get('urgency') == '1' else ''
    d = {'pad': kv.get('pad', '30px 44px 6px 44px' if style == 'grid' else '18px 44px 6px 44px'),
         'eyebrow': kv.get('eyebrow', 'WITH EVERY ORDER'),
         'headline': kv.get('headline') or gifts_text('headline', sig, bare=True),
         'line': kv.get('line') or ('Your %s ship with this order.' % gifts_text('total', sig, bare=True)),
         'note': kv.get('note', 'The filter is a chance to win. The rest comes with every order.'),
         'urgency': urg}
    d.update(tiles)
    return wopen(sig) + fill(tpl('gifts5.html' if style == 'grid' else 'gifts5-row.html'), d, 'gifts5') + WCLOSE

# ---- reviews3
PILLAR = {'K': 'On quality', 'L': 'On delivery', 'S': 'On service'}
_REV = None
def revsets():
    global _REV
    if _REV is None:
        if not os.path.exists(REVSETS): raise ValueError('content/reviews/sets.json ontbreekt: draai scripts/make_review_blocks.py')
        _REV = json.load(open(REVSETS))
    return _REV

def assign_pillars(refs, R):
    """Kies per review een pijler zodat de set zo veel mogelijk verschillende pijlers toont (K, L, S)."""
    import itertools
    opts = [R[r]['pillars'] for r in refs]; best = None
    for combo in itertools.product(*opts):
        score = (len(set(combo)), sum(1 for c, o in zip(combo, opts) if c == o[0]))
        if best is None or score > best[0]: best = (score, combo)
    return list(best[1])

def reviews3(kv, sig):
    R = revsets()
    if kv.get('ids'): refs = [x.strip() for x in kv['ids'].split(',') if x.strip()]
    else:
        s = kv.get('set', '')
        if s not in R['sets']: raise ValueError('reviews3: onbekende set %r (zie content/reviews/sets.json)' % s)
        refs = R['sets'][s]
    n = int(kv.get('n', '3')); refs = refs[:n]
    for r in refs:
        if r not in R['reviews']: raise ValueError('reviews3: review %s staat niet in de bruikbare lijst' % r)
        if r.split('-')[0] in R['banned']: raise ValueError('reviews3: %s mag niet (%s)' % (r, R['banned'][r.split('-')[0]]))
    if len(refs) < 2: raise ValueError('reviews3: minimaal 2 reviews')
    pil = [p.upper() for p in kv['pillars'].split(',')] if kv.get('pillars') else assign_pillars(refs, R['reviews'])
    card = tpl('reviews3-card.html'); cards = []
    w = '%d%%' % (100 // len(refs) - 2)
    for i, (r, p) in enumerate(zip(refs, pil)):
        rv = R['reviews'][r]
        c = card.replace('[[w]]', w).replace('[[ref]]', r).replace('[[pillar]]', PILLAR[p]).replace('[[quote]]', esc(rv['snippet'])).replace('[[name]]', esc(rv['name']))
        if i: cards.append('<td class="rvsp" width="12" style="font-size:0;line-height:0;">&nbsp;</td>')
        cards.append(c)
    d = {'pad': kv.get('pad', '28px 44px 6px 44px'), 'cards': ''.join(cards),
         'eyebrow': ('<div style="%sfont-size:12px;line-height:16px;letter-spacing:2px;font-weight:600;color:#AC3B19;text-align:center;padding-bottom:14px;">%s</div>' % (F, kv['eyebrow'])) if kv.get('eyebrow') else ''}
    return fill(tpl('reviews3.html'), d, 'reviews3')

# ---- vergelijking
VS = {  # rijen uit research/ux-round2/comparisons.md (A/B/C), PFAS-tabel volgens besluit 8 okt (direct "PFAS pan", geen gezondheidsclaim, geen merknamen)
 'pfas': ('Your future pan vs a PFAS pan', 'A PFAS pan',
          [('Pure titanium surface', 'PFAS coating on top', 'cross'), ('No coating to wear off', 'Coating wears with use', 'cross'),
           ('Metal utensils welcome', 'Wood or silicone advised', 'cross'), ('Lab tested PFAS-free', 'PFAS in the coating', 'cross'),
           ('Dishwasher safe', 'Hand wash advised', 'cross')],
          'Light Labs report no. 25895: 31 PFAS compounds tested, all below detection.'),
 'steel': ('Your future pan vs stainless steel', 'Stainless steel',
           [('Hammered for natural release', 'Food tends to stick', 'cross'), ('Cleanup in 30 seconds', 'Often needs a soak', 'cross'),
            ('75-year warranty', 'Varies by brand', 'cross'), ('Lab tested PFAS-free', 'PFAS-free too', 'same'),
            ('Induction ready', 'Induction ready too', 'same')],
           'Cleanup in 30 seconds: verified review, Thomas H. Light Labs report no. 25895.'),
 'castiron': ('Your future pan vs cast iron', 'Cast iron',
              [('No seasoning needed', 'Needs seasoning', 'cross'), ('Dishwasher safe', 'Hand wash, dry, oil', 'cross'),
               ('Hot in 2 to 3 minutes', 'Slow to heat up', 'cross'), ('Non-reactive titanium', 'Acids strip seasoning', 'cross'),
               ('Induction ready', 'Induction ready too', 'same')],
              'Preheat on medium for 2 to 3 minutes. Never on high.'),
}
def vs(kv):
    kind = kv.get('kind', 'pfas')
    if kind not in VS: raise ValueError('vs: kind moet pfas, steel of castiron zijn')
    head, colB, rows, note = VS[kind]
    p = {'pad': kv.get('pad', '34px 44px 6px 44px'), 'eyebrow': kv.get('eyebrow', 'SIDE BY SIDE'), 'headline': kv.get('headline', head),
         'cap': kv.get('cap', 'compare-cap-panpro.png'), 'colA': kv.get('colA', 'Your future pan'), 'colB': kv.get('colB', colB),
         'note': kv.get('note', note)}
    for i, (a, b, ib) in enumerate(rows, 1): p['a%d' % i], p['b%d' % i], p['ib%d' % i] = a, b, ib
    return p   # build_template rendert met het bestaande compare-blok

# ---- bundel: "what's in the box" + rekensom
# (sleutel, titel-substrings (lowercase, OR), naam, inhoud [(cm of None, tekst)], onderdelen voor de som (sleutels), kop, setregel-sjabloon, compare-at tonen)
BUNDLES = [
 ('everything', ['34-pcs', 'just everything'], 'The Just Everything Bundle', [(None, 'the 12-piece set, the roasting pan, wok, deep pan, cr&ecirc;pe pan and pizza steel'), (None, '4 cutting boards, the utensil set, mills and 4 aprons')], None, 'Everything we make, in one box.', '34 pieces for {p}', True),
 ('set12', ['12-pcs', '12 pcs'], '12-piece set', [(None, 'Pan Pro Mini {20}, Small {26} and Large {30}'), (None, '2-quart and 3-quart saucepans and an 8-quart stockpot'), (None, 'a fitted lid for every pan and pot')], None, 'A whole kitchen, one decision.', '12 pieces for {p}', True),
 ('set6', ['pan set with lids', '6-teilig'], '6-piece set', [(None, 'Pan Pro Mini {20}, Small {26} and Large {30}'), (None, 'a fitted stainless steel lid for each pan')], ['mini', 'small', 'large', 'lid20', 'lid26', 'lid30'], 'Buy 2, get 4 free.', 'Six pieces for {p}', True),
 ('full', ['full hammered pro'], 'Full Hammered Pro Edition', [(None, 'Pan Pro Mini {20}, Small {26}, Pan Pro {28} and Large {30}'), (None, 'a lid for each pan'), (None, 'titanium flipper, spatula, scooper and ladle')], ['mini', 'small', 'standard', 'large', 'lid20', 'lid26', 'lid28', 'lid30', 'utset'], 'Every size, every lid, every tool.', 'All of it for {p}', False),
 ('complete', ['complete edition'], 'Complete Edition', [(None, 'Pan Pro {28}'), (None, 'Deep Pan Pro, Wok Pan Pro and Cr&ecirc;pe Pan Pro')], None, 'Four shapes, one surface.', 'Four pans for {p}', False),
 ('setpro', ['cookware set pro'], 'Cookware Set Pro', [(None, 'Pan Pro {28}, Wok Pan Pro and Deep Pan Pro'), (None, 'a titanium flipper and ladle')], None, 'Three shapes, one surface.', 'The set for {p}', False),
 ('panproduo', ['pan pro duo'], 'Pan Pro Duo', [(None, 'Pan Pro Mini {20} and Pan Pro {28}')], ['mini', 'standard'], 'Two sizes, one surface.', 'Both pans for {p}', False),
 ('duo2', ['2 pans + 2 lids', '2 pans'], 'Pro Duo: 2 pans + 2 lids', [(None, 'Pan Pro Mini {20} and Pan Pro {28}'), (None, 'a fitted lid for each')], ['mini', 'standard', 'lid20', 'lid28'], 'Two pans, two lids.', 'Four pieces for {p}', False),
 ('produo', ['pro duo'], 'Pro Duo', [(None, 'Pan Pro {28}'), (None, 'a titanium flipper')], None, 'The pan and the flipper.', 'Both for {p}', False),
 ('kit', ['pan pro kit'], 'Pan Pro Kit', [(None, 'Pan Pro Small {26}'), (None, 'a fitted lid and a titanium flipper')], ['small', 'lid26', 'utensil'], 'Pan, lid and flipper.', 'The kit for {p}', False),
 ('cookprep', ['cook & prep'], 'Cook &amp; Prep Bundle', [(None, 'Pan Pro {28}'), (None, 'the Titanium Cutting Board, size L')], None, 'Cook and prep, both titanium.', 'Both for {p}', False),
 ('panutensil', ['pan pro & utensil'], 'Pan Pro &amp; Utensil Set', [(None, 'Pan Pro {28}'), (None, 'flipper, spatula, scooper and ladle')], None, 'The pan and every tool.', 'All of it for {p}', False),
]
US_ONLY_BUNDLES = {'everything', 'set12', 'duo2'}

def bundle_sum(parts, m):
    t = 0.0
    for k in parts:
        a = amount(k, m)
        if a is None: return None
        t += a
    return t

def bundle(kv, sig, src):
    lines = []
    for key, toks, name, items, parts, head, setline, cmp in BUNDLES:
        cnd = ' or '.join("'%s' in bs" % t for t in toks)
        def items_html(mode):
            out = []
            for _, txt in items:
                txt = re.sub(r'\{(\d+)\}', lambda mo: size_txt(int(mo.group(1)))[mode], txt)
                out.append('<span style="color:#AC3B19;font-weight:600;">&#10003;</span>&nbsp; ' + txt)
            return '<br>'.join(out)
        content = chain(sig, [('US', items_html(0))], items_html(2), bare=True, known_val=items_html(1))
        # prijsregel per markt: setprijs, compare-at doorgestreept (alleen waar Floris het anker bevestigde) en de losse som
        pv = []
        for m in PRICED:
            a = amount(key, m)
            if a is None: continue
            w = amount(key, m, 'compare_at') if cmp else None
            s = bundle_sum(parts, m) if parts else None
            line = setline.replace('{p}', '<b style="color:#AC3B19;font-weight:600;">%s</b>' % money(a, m))
            if w and w > a: line += ' <span style="color:#9A948B;text-decoration:line-through;">%s</span>' % money(w, m)
            if s and s > a + 0.5: line += '<br><span style="color:#727272;font-size:13px;">Bought one by one: %s.</span>' % money(s, m)
            pv.append((m, line))
        price = chain(sig, pv, '', bare=True)
        body = fill(tpl('bundle-body.html'), {'key': key, 'name': name, 'head': head, 'items': content, 'price': price}, 'bundle')
        if key in US_ONLY_BUNDLES:   # buiten de US nooit tonen: dan het algemene blok
            body = '{%% if %s %%}%s{%% else %%}%s{%% endif %%}' % (cond('US', sig), body, '[[generic]]')
        lines.append((cnd, body))
    generic = fill(tpl('bundle-body.html'), {'key': 'generic', 'name': 'Your set', 'head': kv.get('fallback', 'Every piece, the same titanium surface.'),
                                            'items': '<span style="color:#AC3B19;font-weight:600;">&#10003;</span>&nbsp; One tested titanium cooking surface on every piece<br><span style="color:#AC3B19;font-weight:600;">&#10003;</span>&nbsp; One 75-year warranty for all of it', 'price': ''}, 'bundle')
    ch = ''.join(('{%% if %s %%}' if i == 0 else '{%% elif %s %%}') % c + b for i, (c, b) in enumerate(lines)) + '{% else %}' + generic + '{% endif %}'
    ch = ch.replace('[[generic]]', generic)
    d = {'pad': kv.get('pad', '28px 44px 6px 44px'), 'eyebrow': kv.get('eyebrow', "WHAT'S IN THE BOX"), 'chain': ch}
    return '{%% with bs=%s|lower %%}' % src + wopen(sig) + fill(tpl('bundle.html'), d, 'bundle') + WCLOSE + '{% endwith %}'

# ---- cross-sell
# token: (naam, regel, sleutel voor prijs en link, beeld, cm voor de maat in de naam of None)
XITEM = {
 'mini': ('Pan Pro Mini', 'The breakfast pan: eggs and small portions.', 'mini', 'pc-mini.jpg', 20),
 'small': ('Pan Pro Small', 'Dinner for two.', 'small', 'pc-small.jpg', 26),
 'standard': ('Pan Pro', 'The size most kitchens start with.', 'standard', 'pc-standard.jpg', 28),
 'large': ('Pan Pro Large', 'Room for the whole family.', 'large', 'pc-large.jpg', 30),
 'deep': ('Deep Pan Pro', 'Higher sides for sauces, pasta and one-pan dinners.', 'deep', 'pc-deep.jpg', None),
 'wok': ('Wok Pan Pro', 'Deep and wide, to toss without spilling.', 'wok', 'pc-wok.jpg', None),
 'crepe': ('Cr&ecirc;pe Pan Pro', 'Flat and wide: cr&ecirc;pes, pancakes, tortillas.', 'crepe', 'pc-crepe.jpg', None),
 'lid20': ('Stainless Steel Lid,', 'Fits the Mini.', 'lid20', 'pc-lid.jpg', 20),
 'lid26': ('Stainless Steel Lid,', 'Fits the Small.', 'lid26', 'pc-lid.jpg', 26),
 'lid28': ('Stainless Steel Lid,', 'Fits the Pan Pro.', 'lid28', 'pc-lid.jpg', 28),
 'lid30': ('Stainless Steel Lid,', 'Fits the Large.', 'lid30', 'pc-lid.jpg', 30),
 'board': ('Titanium Cutting Board', 'Non-porous titanium, anti-microbial. Four sizes.', 'board', 'pc-board.jpg', None),
 'utset': ('Titanium Utensil Set', 'Titanium tools, made for your pans.', 'utset', 'pc-utensil.jpg', None),
 'apron': ('Siraat Signature Apron', 'Heavy canvas, adjustable, four colors.', 'apron', 'pc-apron.jpg', None),
 'mill': ('Salt &amp; Pepper Mill Set', 'All-metal, 12 grind settings. A matching pair.', 'mill', 'pc-mill.jpg', None),
 'set6': ('The 6-piece set', 'Mini, Small and Large, each with its own lid.', 'set6', 'pc-set6.jpg', None),
}
LIDVAR = {'lid20': '53294486421844', 'lid26': '52401107206484', 'lid28': '52401107239252', 'lid30': '52401107272020'}
# Bezit: titel in de huidige order (xs = event-titels, lowercase) of sleutel in person.siraat_owned (xo, lijst uit
# (xo krijgt |default:'' : zonder sync ontbreekt de property en dan is 'x' not in xo in Klaviyo onwaar, 09-monitor-rapport H2)
# scripts/sync_owned.py, die bundels uitpakt). Sets in de huidige order tellen mee via hun inhoud (SETS_ALL enz.).
SETS_ALL = ['pan set', 'teilig', '12-pcs', '12 pcs', 'full hammered', 'everyth']
XOWN = {'mini': (['pan pro mini', '2 pans', 'pan pro duo'] + SETS_ALL, ['panpro_mini']),
        'small': (['pan pro small', 'pan pro kit'] + SETS_ALL, ['panpro_small']),
        'standard': (['pan pro standard', 'cookware set pro', 'complete edition', 'full hammered', '2 pans', 'pro duo', 'cook & prep', 'pan pro & utensil', 'everyth'], ['panpro_standard']),
        'large': (['pan pro large'] + SETS_ALL, ['panpro_large']),
        'deep': (['deep pan', 'cookware set pro', 'complete edition', 'everyth'], ['deep']),
        'wok': (['wok', 'cookware set pro', 'complete edition', 'everyth'], ['wok']),
        'crepe': (['crêpe', 'crepe', 'complete edition', 'everyth'], ['crepe']),
        'lid20': (['lid', '2 pans'] + SETS_ALL, ['lid_20']), 'lid26': (['lid', 'pan pro kit'] + SETS_ALL, ['lid_26']),
        'lid28': (['lid', 'full hammered', '2 pans'], ['lid_28']), 'lid30': (['lid'] + SETS_ALL, ['lid_30']),
        'board': (['cutting board', 'cook & prep', 'everyth'], ['board']),
        'utset': (['utensil', 'full hammered', 'everyth'], ['utensils']),
        'apron': (['apron', 'everyth'], ['apron']), 'mill': (['mill', 'everyth'], ['mill']),
        'set6': (SETS_ALL, ['set6', 'set12', 'everything'])}
# Categorieën van de huidige order en hun kandidaten (04-cross-sell.md 6.1). Een kandidaat verschijnt als hij niet in bezit is en
# hoort bij een categorie die in de order zit. Eén rij per product (geen dubbele rijen bij meer producten in de order).
XCAT = [
 ('set12', ['12-pcs', '12 pcs'], ['standard', 'utset', 'board']),
 ('set6', ['pan set', 'teilig'], ['standard', 'utset', 'board']),
 ('pot', ['saucepan', 'pot with lid', 'pot set'], ['set6', 'standard', 'board']),
 ('setmix', ['cookware set pro', 'complete edition', 'full hammered', 'pan pro duo', '2 pans', 'pro duo', 'pan pro kit', 'cook & prep', 'pan pro & utensil'], ['lid28', 'board', 'crepe']),
 ('standard', ['pan pro standard'], ['lid28', 'mini', 'board']),
 ('large', ['pan pro large'], ['lid30', 'small', 'board']),
 ('small', ['pan pro small'], ['mini', 'lid26', 'board']),
 ('mini', ['pan pro mini'], ['standard', 'lid20', 'board']),
 ('deep', ['deep pan'], ['wok', 'mini', 'board']),
 ('wok', ['wok'], ['deep', 'mini', 'board']),
 ('crepe', ['crêpe', 'crepe'], ['standard', 'board', 'utset']),
 ('pizza', ['pizza steel'], ['board', 'standard', 'crepe']),
 ('roast', ['roasting'], ['board', 'large', 'utset']),
 ('board', ['cutting board'], ['standard', 'mini', 'utset']),
 ('lid', ['steel lid'], ['mini', 'small', 'board']),
 ('utset', ['utensil'], ['board', 'mini', 'deep']),
 ('mill', ['mill'], ['board', 'apron', 'standard']),
 ('apron', ['apron'], ['mill', 'board', 'standard']),
 ('other', ['sheets', 'detergent', 'gift card', 'bottle', 'straw', 'ice cube', 'trivet', 'chopstick', 'mat', 'sharpener', 'tote', 'wheel', 'grill'], ['standard', 'mini', 'board']),
]
XORDER = ['lid28', 'lid30', 'lid26', 'lid20', 'standard', 'mini', 'small', 'large', 'set6', 'deep', 'wok', 'crepe', 'board', 'utset', 'mill', 'apron']
XHEAD = {'set12': 'Goes with your set', 'set6': 'Goes with your set', 'pot': 'Now the pans', 'setmix': 'Goes with your set',
         'standard': 'What Pan Pro owners add next', 'large': 'What Large owners add next', 'small': 'What Small owners add next',
         'mini': 'What Mini owners add next', 'deep': 'Goes with your deep pan', 'wok': 'Goes with your wok', 'crepe': 'Goes with your cr&ecirc;pe pan',
         'pizza': 'Goes with your pizza steel', 'roast': 'Goes with your roasting pan', 'board': 'Goes with your board', 'lid': 'Goes with your lid',
         'utset': 'Goes with your utensils', 'mill': 'Goes with your mills', 'apron': 'Goes with your apron', 'other': 'Picked for your kitchen', '': 'Picked for your kitchen'}

def owned(tok):
    subs, keys = XOWN[tok]
    return ' or '.join(["'%s' in xs" % x for x in subs] + ["'%s' in xo" % k for k in keys])

def owned_short(tok):
    """Korte bezitstoets voor de terugvalregel (eigen titel of sleutel; sets via hun sleutels in siraat_owned)."""
    subs, keys = XOWN[tok]
    return ' or '.join(["'%s' in xs" % subs[0]] + ["'%s' in xo" % k for k in keys])

def free(tok):
    subs, keys = XOWN[tok]
    return ' and '.join(["'%s' not in xs" % x for x in subs] + ["'%s' not in xo" % k for k in keys])

def xrow(tok, kv, sig, prices):
    name, sub, key, img, cm = XITEM[tok]
    pre, post = kv.get('pre', 'https://siraatskitchen.com/products/'), kv.get('post', '')
    h = handle(key)
    if tok in LIDVAR:
        h += ('%3Fvariant%3D' if 'redirect' in pre else '?variant=') + LIDVAR[tok]
        # de link heeft nu al een query: de UTM-staart sluit aan met & (gecodeerd %26), nooit een tweede ? (%3F)
        if post.upper().startswith('%3F'): post = '%26' + post[3:]
        elif post.startswith('?'): post = '&' + post[1:]
    if cm: name = name + ' ' + size_chain(sig, cm, bare=True)
    pr = ''
    if prices != 'none':
        vals = price_vals(key, frm=True)
        if prices != 'local': vals = [x for x in vals if x[0] == 'US']
        pr = chain(sig, [(m, ' &middot; <b style="color:#282828;">%s</b>' % v) for m, v in vals], '', bare=True)
    row = fill(tpl('xsell-row.html'), {'tok': tok, 'img': img, 'url': pre + h + post, 'name': name, 'sub': sub, 'price': pr}, 'xsell')
    if us_only(key): row = '{%% if %s %%}%s{%% endif %%}' % (cond('US', sig), row)
    return row

def xsell(kv, sig, src):
    prices = kv.get('prices', 'local')
    fb = ('<tr><td colspan="2" data-xs="none" style="padding:14px 16px;border-top:1px solid #ECE7DD;%sfont-size:14px;line-height:21px;color:#727272;text-align:center;">%s</td></tr>' %
          (F, kv.get('fallback', 'Already have the full line-up? Reply and tell us what you cook most. We will point you to the right next piece.')))
    rel = {}
    for cat, toks, cands in XCAT:
        for t in cands: rel.setdefault(t, []).extend(toks)
    rows = ''
    for t in XORDER:
        r = ' or '.join("'%s' in xs" % x for x in dict.fromkeys(rel.get(t, [])))
        if t in ('standard', 'mini', 'board'): r = 'not xs or ' + r          # geen titels (bv. alleen een gift): de standaardrij
        row = xrow(t, kv, sig, prices)
        if t == 'set6' and kv.get('fall') == '1':   # fall-sale-set ook als Mini, Small en Large alle drie niet in bezit zijn
            g = '{%% if %s %%}{%% if %s %%}%s{%% elif %s and %s and %s %%}%s{%% endif %%}{%% endif %%}' % (free(t), r, row, free('mini'), free('small'), free('large'), row)
        elif r: g = '{%% if %s %%}{%% if %s %%}%s{%% endif %%}{%% endif %%}' % (free(t), r, row)
        else: continue
        rows += g
    # terugval: alle kandidaten van de eerste categorie in bezit (of het 34-delige bundel): één regel in plaats van rijen
    nb = ''
    for i, (cat, toks, cands) in enumerate(XCAT):
        c = ' or '.join("'%s' in xs" % t for t in toks)
        inner = fb
        for t in reversed(cands): inner = '{%% if %s %%}%s{%% endif %%}' % (owned_short(t), inner)
        nb += ('{%% if %s %%}' if i == 0 else '{%% elif %s %%}') % c + inner
    nb += '{% endif %}'
    body = "{%% if 'everyth' in xs or '34-pcs' in xs %%}%s{%% else %%}%s%s{%% endif %%}" % (fb, rows, nb)
    hb, hv = [], []
    for cat, toks, cands in XCAT:
        c = ' or '.join("'%s' in xs" % x for x in toks); t = XHEAD.get(cat, XHEAD[''])
        if hb and hv[-1] == t: hb[-1] += ' or ' + c
        else: hb.append(c); hv.append(t)
    head = ''.join(('{%% if %s %%}' if i == 0 else '{%% elif %s %%}') % c + t for i, (c, t) in enumerate(zip(hb, hv))) + '{% else %}' + XHEAD[''] + '{% endif %}'
    d = {'pad': kv.get('pad', '28px 44px 4px 44px'), 'eyebrow': kv.get('eyebrow', 'OFTEN ADDED NEXT'), 'headline': kv.get('headline') or head,
         'rows': body, 'note': kv.get('note', '')}
    return ("{%% with xs=%s|lower xo=person|lookup:'siraat_owned'|default:'' %%}" % src) + wopen(sig) + fill(tpl('xsell.html'), d, 'xsell') + WCLOSE + '{% endwith %}'

def _amp(subs):
    """Titels met & komen via |join als &amp; binnen (autoescape): test beide vormen."""
    out = []
    for x in subs:
        out.append(x)
        if '&' in x and '&amp;' not in x: out.append(x.replace('&', '&amp;'))
    return out

for _k, (_s, _keys) in list(XOWN.items()): XOWN[_k] = (_amp(_s), _keys)
XCAT = [(c, _amp(t), cands) for c, t, cands in XCAT]
BUNDLES = [(b[0], _amp(b[1])) + tuple(b[2:]) for b in BUNDLES]

# ------------------------------------------------------------------ registratie
SRC = {'checkout': "event.Items|join:','", 'order': "event.Items|join:','", 'cart': "event|lookup:'Product Name'", 'browse': 'event.Name',
       'profile': "''"}
BLOCKS = {'gifts5', 'reviews3', 'bundle', 'xsell', 'vs'}

def block(name, kv, flow):
    sig = kv.pop('sig', None) or sig_of(flow)
    src = kv.get('src') or SRC[sig]
    if name == 'gifts5': return gifts5(kv, sig)
    if name == 'reviews3': return reviews3(kv, sig)
    if name == 'bundle': return bundle(kv, sig, src)
    if name == 'xsell': return xsell(kv, sig, src)
    raise ValueError(name)
