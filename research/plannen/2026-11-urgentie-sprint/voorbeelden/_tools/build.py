"""Bouwt voorbeelden/index.html: visuele galerij van de urgentie-sprint (nu vs agressief, campagnes,
herbouwde mails, black-hat referentie, site). Alleen lokaal; leest de repo-bestanden en de gerenderde
huidige templates (voorbeelden/huidig/*.jpg, zie render_current.py en shot_current.js).
Geen echte BF-code (BFCODE is placeholder). Geen gedachtestreepjes.
python3 build.py <map met gerenderde huidige templates (html)>"""
import json, re, os, sys, html, glob

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)                     # .../voorbeelden
SPRINT = os.path.dirname(OUT)                   # .../2026-11-urgentie-sprint
ROOT = os.path.abspath(os.path.join(SPRINT, '..', '..', '..'))
REL = '../../../../'                            # van voorbeelden/ naar repo-root
RENDER = sys.argv[1] if len(sys.argv) > 1 else ''

FA = json.load(open(os.path.join(SPRINT, 'flows-agressief', 'flows-agressief.json')))
CA = json.load(open(os.path.join(SPRINT, 'copy-agressief', 'copy-agressief.json')))
CN = json.load(open(os.path.join(SPRINT, 'copy', 'copy.json')))

E = lambda s: html.escape(str(s), quote=True)
LOCKUP = REL + 'brand/logo/lockup/siraat-lockup-black-email-on-cream.png'
PAN_IMG = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/Titanium_hammered_pan_pro_standard_b69d1fc5-43d8-40a5-9ad7-523bdddc54d4.webp?v=1781682831&width=600'
DEFAULT_HERO = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/siraat-collection-exclusive-01-plinths-desktop.jpg?width=1200'

SAMPLE = {
    'DEADLINE': 'tonight at 11:59 PM ET', 'DEADLINE_SHORT': 'tonight', 'HOURS_LEFT': '6',
    'MINUTES_LEFT': '60', 'CREDIT': '$12', 'NEXT_CHARGE': 'Dec 2', 'UNITS': '14',
    'FLASH_PRICE': '$199', 'FLASH_PERCENT': '20%', 'VIP_CODE': 'VIP-7KQ2', 'POINTS': '1,200',
    'PAN_AFTER_CREDIT': '132', 'WHAT_ENDS': 'The flash price on 2 pans + 2 lids',
    'WHAT_ENDS_SHORT': 'the flash price', 'AFTER': 'Then the set goes back to $249.',
    'AFTER_SHORT': 'then $249', 'DEADLINE_PAST': 'last night at 11:59 PM ET', 'N': '3',
    'LINK': 'siraatskitchen.com/r/you', 'DRAW_RULES_URL': 'official rules',
}

def fill(s):
    """Placeholder vullen met voorbeeldwaarde, zichtbaar gemarkeerd."""
    s = E(s)
    s = s.replace('${{CREDIT}}', '{{CREDIT}}')
    def rep(m):
        k = m.group(1)
        v = SAMPLE.get(k)
        if v is None:
            return '<span class="ph" title="placeholder">{{%s}}</span>' % k
        return '<span class="ph" title="{{%s}}">%s</span>' % (k, E(v))
    s = re.sub(r'\{\{\s*([A-Z_]+)\s*\}\}', rep, s)
    s = re.sub(r'\bBFCODE\b', '<span class="ph" title="placeholder, echte code nooit in de repo">BFCODE</span>', s)
    return s

RANK = {'groen': 0, 'oranje': 1, 'rood': 2}
NL_RISK = {'groen': 'groen', 'oranje': 'oranje', 'rood': 'rood'}

def dot(r):
    return '<i class="dot %s" title="risico %s"></i>' % (r, r)

def hardest(items, key='risico'):
    """Hoogste risico; bij gelijk de laatste (meestal de hardste formulering)."""
    best = None
    for it in items:
        if best is None or RANK.get(it[key], 0) >= RANK.get(best[key], 0):
            best = it
    return best

def inbox(sender, subj, prev, risk=None, time='9:41 AM', fake=False, note=''):
    av = (sender or 'S')[0].upper()
    r = ('<span class="rk %s">%s</span>' % (risk, risk)) if risk else ''
    return ('<div class="inbox%s"><div class="av">%s</div><div class="ib"><div class="from"><b>%s</b>'
            '<span class="tm">%s</span></div><div class="subj">%s %s</div><div class="prev">%s</div>%s</div></div>') % (
        ' fake' if fake else '', E(av), E(sender), E(time), fill(subj), r, fill(prev),
        ('<div class="inote">%s</div>' % note) if note else '')

def hero_split(t):
    a, _, b = t.partition('|')
    return a.strip(), b.strip()

def topbar_text(dl):
    if '{{DEADLINE' in dl:
        return 'ENDS ' + SAMPLE['DEADLINE'].upper()
    if '{{NEXT_CHARGE}}' in dl:
        return 'NEXT DELIVERY ' + SAMPLE['NEXT_CHARGE'].upper()
    if '{{HOURS_LEFT}}' in dl:
        return SAMPLE['HOURS_LEFT'] + ' HOURS LEFT'
    return 'BLACK FRIDAY: UP TO 70% OFF'

def phone(hero_img, hero, dl, cta, ps, logo=True, top=None, body=None):
    k, sub = hero_split(hero or '')
    t = top or topbar_text(dl or '')
    out = ['<div class="phone"><div class="mtop">%s</div>' % E(t)]
    if logo:
        out.append('<div class="mhead"><img src="%s" alt="Siraat" width="150" loading="lazy"></div>' % LOCKUP)
    out.append('<div class="mhero" style="background-image:url(\'%s\')"><div class="glass"><div class="hk">%s</div>%s</div></div>' % (
        E(hero_img), fill(k), ('<div class="hs">%s</div>' % fill(sub)) if sub else ''))
    out.append('<div class="mbody">')
    if body:
        out.append('<p class="bt">%s</p>' % fill(body))
    if dl:
        out.append('<p class="dl">%s</p>' % fill(dl))
    if cta:
        out.append('<div class="btn">%s</div>' % fill(cta))
    out.append('<p class="fr">Free shipping, duties paid. 30-day returns. 75-year warranty.</p>')
    if ps:
        out.append('<p class="ps">%s</p>' % fill(ps))
    out.append('</div></div>')
    return ''.join(out)

# ---------- huidige templates: hero en logo uit de render ----------
def tpl_info(tid):
    info = {'hero': DEFAULT_HERO, 'logo': True, 'shot': None}
    p = os.path.join(OUT, 'huidig', tid + '.jpg')
    if os.path.exists(p):
        info['shot'] = 'huidig/%s.jpg' % tid
    f = os.path.join(RENDER, tid + '.html') if RENDER else ''
    if f and os.path.exists(f):
        h = open(f).read()
        bg = re.findall(r'background(?:-image)?\s*[:=]\s*["\']?(?:url\()?["\']?(https://[^"\')\s]+)', h)
        big = [m.group(1) for m in re.finditer(r'<img[^>]*?src="(https://[^"]+)"[^>]*?width="(\d+)"', h) if int(m.group(2)) >= 400]
        if bg:
            info['hero'] = bg[0]
        elif big:
            info['hero'] = big[0]
        info['hero'] = info['hero'].replace('&amp;', '&')
        first = h[:12000]
        info['logo'] = bool(re.search(r'<img[^>]*alt="Siraat"', first))
    return info

# ---------- sectie 1: flows ----------
def regel(m, veld):
    for r in m['regels']:
        if r['veld'] == veld:
            return r
    return None

def flow_mail_card(f, m):
    subs = [r for r in m['regels'] if r['veld'].startswith('Subject')]
    prevs = [r for r in m['regels'] if r['veld'].startswith('Preview')]
    s = hardest(subs) if subs else {'copy': '', 'risico': 'groen'}
    p = prevs[0] if prevs else {'copy': '', 'risico': 'groen'}
    if prevs:
        p = hardest(prevs)
    hero = regel(m, 'Hero') or {'copy': ''}
    cta = regel(m, 'CTA') or {'copy': ''}
    dl = regel(m, 'Deadline-regel') or {'copy': ''}
    ps = regel(m, 'PS') or {'copy': ''}
    sender = 'Benjamin from Siraat' if 'Benjamin' in m['sleutel'] or f['id'] in ('R22pzb', 'YhQJdb') else 'Siraat'
    mx = max((r['risico'] for r in m['regels']), key=lambda r: RANK.get(r, 0)) if m['regels'] else 'groen'
    # links: nu
    if m['berichten']:
        b = m['berichten'][0]
        info = tpl_info(b['template'])
        more = ''
        if len(m['berichten']) > 1:
            more = '<details class="var"><summary>+%d varianten</summary><ul>%s</ul></details>' % (
                len(m['berichten']) - 1, ''.join('<li><b>%s</b>: %s</li>' % (E(x['naam']), E(x['huidig_onderwerp'] or '')) for x in m['berichten'][1:]))
        st = m.get('stats_14d') or {}
        meta = '%s · template %s · %s ontvangers 14 d · RPR $%.2f' % (E(b['positie']), E(b['template']), '{:,.0f}'.format(st.get('ontvangers', 0)), st.get('rpr', 0) or 0)
        shot = ('<a class="shot" href="%s" target="_blank"><img src="%s" alt="Huidige template %s, bovenkant" loading="lazy"></a>'
                '<p class="cap">Huidige template, gerenderd met voorbeeldprofiel (US), bovenste deel. Klik voor groot.</p>') % (info['shot'], info['shot'], E(b['template'])) if info['shot'] else '<p class="cap">Geen render beschikbaar.</p>'
        left = ('<div class="col nu"><div class="lab">Nu (live)</div>%s<p class="meta">%s</p>%s'
                '<p class="cur"><b>Hero nu:</b> %s<br><b>Knop nu:</b> %s</p>%s</div>') % (
            inbox(sender, b['huidig_onderwerp'] or '(geen onderwerp)', b['huidige_preview'] or ''), meta, more,
            E(m['huidige_hero']), E(m['huidige_cta']), shot)
    else:
        info = {'hero': DEFAULT_HERO, 'logo': True}
        left = ('<div class="col nu"><div class="lab">Nu</div><div class="empty">Deze stap bestaat nog niet in Klaviyo.<br>%s</div></div>') % E(m['noot'] or 'Nieuwe stap (voorstel).')
    logo = info['logo'] and f['id'] != 'YwsKcf'
    # rechts: agressief
    lines = []
    for r in m['regels']:
        codes = ''.join('<span class="code" title="%s">%s</span>' % (E(FA['voorwaarden'].get(c, '')), E(c)) for c in r.get('waar_als_codes', []))
        lines.append('<li>%s<span class="veld">%s</span><span class="cp">%s</span><span class="codes">%s</span>%s</li>' % (
            dot(r['risico']), E(r['veld']), fill(r['copy'].replace('|', ' / ')), codes,
            ('<span class="nt">%s</span>' % E(r['noot'])) if r.get('noot') else ''))
    allc = []
    for r in m['regels']:
        for c in r.get('waar_als_codes', []):
            if c not in allc:
                allc.append(c)
    vw = ''.join('<li><b>[%s]</b> %s</li>' % (E(c), fill(FA['voorwaarden'].get(c, ''))) for c in allc)
    right = ('<div class="col agr"><div class="lab">Te agressief (maximale stand) <span class="rk %s">hoogste risico: %s</span></div>%s%s'
             '<ul class="lines">%s</ul><details class="vw"><summary>Waar als: voorwaarden voluit (%d)</summary><ul>%s</ul></details></div>') % (
        mx, mx, inbox(sender, s['copy'], p['copy'], s['risico']),
        phone(info['hero'], hero['copy'], dl['copy'], cta['copy'], ps['copy'], logo=logo),
        ''.join(lines), len(allc), vw)
    title = E(m['sleutel'])
    badge = '<span class="new">nieuw</span>' if m['nieuw'] else ''
    return '<article class="mcard"><h4>%s %s</h4><div class="pair">%s%s</div></article>' % (title, badge, left, right)

def sec_flows():
    flows = sorted(FA['flows'], key=lambda f: (f['prioriteit'], -(f['stats_14d'].get('omzet') or 0)))
    nav = ''.join('<a href="#f-%s">%s</a>' % (f['id'], E(re.sub(r'^(v4 · |EB \| )', '', f['naam']))) for f in flows)
    parts = []
    n = 0
    for f in flows:
        st = f['stats_14d']
        nw = ''.join('<li><s>%s</s> %s</li>' % (E(x['regel']), E(x['waarom'])) for x in f['nooit_waar'])
        cards = ''.join(flow_mail_card(f, m) for m in f['mails'])
        n += len(f['mails'])
        parts.append(('<section class="flow" id="f-%s"><header class="fh"><div><span class="eyebrow">Prioriteit %s · %s</span>'
                      '<h3>%s</h3></div><p class="fstat">%s per week · RPR $%.2f · klik %.1f%% · <a href="../flows-agressief/%s">bronbestand</a></p>'
                      '<p class="echt"><b>Echte deadlines:</b> %s</p><details class="nooit"><summary>Nooit waar in deze flow (%d)</summary><ul>%s</ul></details></header>%s</section>') % (
            f['id'], f['prioriteit'], f['id'], E(f['naam']), '{:,.0f}'.format(st.get('per_week') or 0), st.get('rpr') or 0,
            st.get('klik_pct') or 0, E(f['bestand']), E(f['echte_deadlines']), len(f['nooit_waar']), nw, cards))
    return n, len(flows), nav, ''.join(parts)

# ---------- sectie 2: campagnes ----------
CAMP = [('1-flash', 'urg-flash', 'urg-flash-hero.jpg'), ('2-vip-weekend', 'urg-vip', 'urg-vip-weekend-hero.jpg'),
        ('3-credit', 'urg-credit', 'urg-credit-hero.jpg'), ('4-last-hours', 'urg-last', 'urg-last-hours-hero.jpg'),
        ('5-gifts', 'urg-gifts', 'urg-gifts-hero.jpg'), ('6-draw', 'urg-draw', 'urg-draw-hero.jpg')]
CPATH = REL + 'klaviyo/templates/v3/campaigns/urgency-1108/'

def sec_campaigns():
    out = []
    for key, slug, heroimg in CAMP:
        a = CA['mails'][key]; n = CN['mails'][key]
        cards = []
        for reg in ('US', 'INT'):
            nu = n[reg]; ag = a[reg]
            subj = nu.get('subject_' + nu.get('subject_pick', 'a').lower()) or nu.get('subject_a')
            png = CPATH + 'previews/%s-%s-375.png' % (slug, reg.lower())
            left = ('<div class="col nu"><div class="lab">Normaal (gebouwd, %s)</div>%s'
                    '<a class="shot tall" href="%s" target="_blank"><img src="%s" alt="Preview %s %s" loading="lazy"></a>'
                    '<p class="cap"><a href="%s" target="_blank">375 px</a> · <a href="%s" target="_blank">600 px</a></p></div>') % (
                reg, inbox(n['sender'], subj, nu.get('preview', '')), png, png, slug, reg,
                png, CPATH + 'previews/%s-%s-600.png' % (slug, reg.lower()))
            sb = hardest(ag['subjects']); pv = hardest(ag['previews'])
            rows = ''.join(inbox(a['sender'], x['text'], pv['text'] if x is sb else ag['previews'][0]['text'], x['risico'], time=t)
                           for x, t in zip(ag['subjects'], ['9:00 AM', '1:00 PM', '6:00 PM', '10:59 PM', '11:15 PM']))
            hero = hardest(ag['heroes']); btn = hardest(ag['buttons'])
            cd = ag['countdown'].get('T-1h') or {}
            body = ag['body']['text'] if isinstance(ag['body'], dict) else ''
            ps = ''
            mx = max([x['risico'] for x in ag['subjects'] + ag['previews'] + ag['heroes'] + ag['buttons']], key=lambda r: RANK[r])
            heroes = ''.join('<li>%s<span class="cp">%s</span></li>' % (dot(x['risico']), fill(x['text'].replace('|', ' / '))) for x in ag['heroes'])
            btns = ''.join('<li>%s<span class="cp">%s</span></li>' % (dot(x['risico']), fill(x['text'])) for x in ag['buttons'])
            cds = ''.join('<li>%s<span class="veld">%s</span><span class="cp">%s</span></li>' % (dot(v['risico']), E(k), fill(v['text'])) for k, v in ag['countdown'].items())
            rs = ag['resend'] if isinstance(ag['resend'], list) else [ag['resend']]
            rsh = ''.join(inbox(a['sender'], x['text'], 'Resend naar niet-openers', x.get('risico')) for x in rs if isinstance(x, dict) and x.get('text'))
            vw = ''.join('<li>%s %s: %s</li>' % (dot(x['risico']), fill(x['text']), fill(x['waar_als'])) for x in ag['subjects'])
            right = ('<div class="col agr"><div class="lab">Agressief (%s) <span class="rk %s">hoogste risico: %s</span></div>'
                     '<div class="stack">%s</div>%s<h5>Hero-opties</h5><ul class="lines">%s</ul><h5>Knoppen</h5><ul class="lines">%s</ul>'
                     '<h5>Aftellen per verzendmoment</h5><ul class="lines">%s</ul>%s'
                     '<details class="vw"><summary>Waar als (onderwerpen)</summary><ul>%s</ul></details></div>') % (
                reg, mx, mx, rows,
                phone(CPATH + 'assets/' + heroimg, hero['text'], cd.get('text', ''), btn['text'], ps, body=body),
                heroes, btns, cds, ('<h5>Resend</h5><div class="stack">%s</div>' % rsh) if rsh else '', vw)
            cards.append('<article class="mcard"><h4>%s · %s</h4><div class="pair">%s%s</div></article>' % (E(a['name']), reg, left, right))
        out.append('<section class="flow" id="c-%s"><header class="fh"><span class="eyebrow">Campagne %s</span><h3>%s</h3><p class="fstat">%s</p></header>%s</section>' % (
            key, key[0], E(a['name']), fill(a['base']), ''.join(cards)))
    # extra mails uit copy-agressief zonder gebouwde template
    ex = []
    for key in ('7-final-hour', '8-missed-last-call'):
        a = CA['mails'][key]
        rows = ''.join(inbox(a['sender'].split(' (')[0], x['text'], a['US']['previews'][0]['text'], x['risico']) for x in a['US']['subjects'])
        ex.append('<div class="col agr"><div class="lab">%s</div><div class="stack">%s</div></div>' % (E(a['name']), rows))
    sm = ''.join('<li><s>%s</s><span>%s</span></li>' % (E(x['smooche']), E(x['waarom_niet'])) for x in CA['smooche_doet_dit_wij_niet'])
    out.append('<section class="flow" id="c-extra"><header class="fh"><h3>Extra uit copy-agressief (nog geen gebouwde mail)</h3></header><div class="pair">%s</div>'
               '<details class="nooit" open><summary>Smooche doet dit, wij niet (%d)</summary><ul>%s</ul></details></section>' % (''.join(ex), len(CA['smooche_doet_dit_wij_niet']), sm))
    return ''.join(out)

# ---------- sectie 3: herbouwde mails ----------
def meta_of(path):
    t = open(path).read()
    g = lambda k: (re.search(k + r':\s*([^\n<]*)', t) or [None, ''])[1].strip()
    return g('SENDER'), g('SUBJECT A'), g('PREVIEW')

def sec_rebuilt():
    base = REL + 'klaviyo/templates/v3/'
    items = []
    groups = [('Welcome (herbouw W2 tot W5)', 'flows-nov/welcome', [('wn2', 'us-us'), ('wn2', 'int-int'), ('wn3', 'us-us'), ('wn3', 'int-int'), ('wn4', 'us-us'), ('wn4', 'int-int'), ('wn5', 'us-us'), ('wn5', 'int-int')]),
              ('Failure to launch BF1 tot BF3', 'flows-nov/ftl', [('ftl1', 'us-us'), ('ftl1', 'int-int'), ('ftl1', 'int-au'), ('ftl2', 'us-us'), ('ftl2', 'int-int'), ('ftl3', 'us-us'), ('ftl3', 'int-int')]),
              ('Sunset en winback', 'flows-nov/sunset-winback', [('sbf', 'us-us'), ('sbf', 'int-int'), ('wbf', 'us-us'), ('wbf', 'int-int')])]
    out = []
    count = 0
    for title, folder, lst in groups:
        cards = []
        for slug, var in lst:
            src = os.path.join(ROOT, 'klaviyo/templates/v3', folder, '%s-%s.html' % (slug, var.split('-')[0]))
            snd, sa, pv = meta_of(src)
            p375 = base + folder + '/previews/%s-%s-375.png' % (slug, var)
            p600 = base + folder + '/previews/%s-%s-600.png' % (slug, var)
            cards.append('<figure class="thumb"><a href="%s" target="_blank"><img src="%s" alt="%s %s" loading="lazy"></a><figcaption><b>%s · %s</b>%s'
                         '<span class="lk"><a href="%s" target="_blank">375</a> · <a href="%s" target="_blank">600</a></span></figcaption></figure>' % (
                             p375, p375, slug, var, slug.upper(), var.upper(), inbox(snd or 'Siraat', sa, pv), p375, p600))
            count += 1
        out.append('<h3 class="gh">%s</h3><div class="grid">%s</div>' % (E(title), ''.join(cards)))
    # affiliate s0-b
    src = os.path.join(ROOT, 'klaviyo/templates/v3/affiliate/s0/s0-b.meta.txt')
    t = open(src).read()
    g = lambda k: (re.search(k + r':\s*([^\n]*)', t) or [None, ''])[1].strip()
    out.append('<h3 class="gh">Affiliate share-link (s0-b)</h3><div class="grid"><figure class="thumb"><a href="img/s0-b-375.jpg" target="_blank"><img src="img/s0-b-375.jpg" alt="s0-b" loading="lazy"></a>'
               '<figcaption><b>S0-B · platte brief van Benjamin</b>%s<span class="lk"><a href="%sklaviyo/templates/v3/affiliate/s0/s0-b-preview.html" target="_blank">preview-html</a></span></figcaption></figure></div>' % (
                   inbox(g('SENDER'), g('SUBJECT'), g('PREVIEW')), REL))
    return count + 1, ''.join(out)

# ---------- sectie 4: black-hat ----------
def site(inner, cls=''):
    return '<div class="site %s">%s</div>' % (cls, inner)

def mail(inner):
    return '<div class="snip">%s</div>' % inner

def pdp_mini(extra):
    return site('<div class="pm"><img src="%s" alt="pan" loading="lazy"><div><div class="pt">Titanium Hammered Pan Pro</div>%s</div></div>' % (PAN_IMG, extra))

BH = [
 ('A1', 'Tijd', 'Evergreen of resettende timer', 'Hoog: FTC-rapport 2022, UCPD bijlage I punt 7, CMA Emma Sleep',
  'Princeton-crawl (Mathur e.a. 2019): 157 van 393 timers misleidend. Siraat nu: balk en koopbox (zie Site).',
  site('<div class="bar">VIP BLACK FRIDAY SALE · 70% OFF + 5 GIFTS <span class="tmr">00:59:36</span></div><div class="frames"><div><small>Bezoek 1</small><span class="tmr dark">00:59:36</span></div><div><small>Bezoek 2, volgende dag</small><span class="tmr dark">00:59:59</span></div></div><p class="sm">Na nul begint hij gewoon opnieuw.</p>'),
  site('<div class="bar">BLACK FRIDAY ENDS NOV 30 · 11:59 PM ET</div><p class="sm">Eén eindtijd voor iedereen, uit dezelfde bron als de Shopify-korting (<code>data-siraat-end</code>). Daarna "Ended" en de prijs verandert echt.</p>')),
 ('A2', 'Tijd', '"Ends tonight" terwijl de sale doorloopt', 'Hoog: FTC sectie 5, UCPD punt 7',
  'Smooche, letterlijk: "the sale ends tonight at midnight. No extensions this time." De sale liep door.',
  inbox('Merk X', 'The sale ends tonight at midnight', 'No extensions this time.', fake=True),
  inbox('Siraat', 'Black Friday ends Nov 30', 'Up to 70% off until Nov 30 at 11:59 PM ET. Then regular prices.') + '<p class="sm">Op 30 nov zelf mag "ends tonight" wel ([BF30]). Daarvoor een ketting van echte kleine deadlines: flash 24 u, VIP-weekend, trekking per week.</p>'),
 ('A3', 'Tijd', 'Verlengen na "kan niet verlengd worden"', 'Hoog: maakt de eerste deadline achteraf vals',
  'Smooche: "I extended your credit by 24 hours... It cannot be extended again."',
  inbox('Chloe from Merk X', 'I extended your credit by 24 hours', 'It cannot be extended again.', fake=True),
  inbox('Siraat', "It ended. Here's what's still on.", 'The flash price ended last night at 11:59 PM ET. Black Friday is still up to 70% off.') + '<p class="sm">Na-deadline-mail (copy-agressief 8B): geen verlenging, wel wat nog echt loopt.</p>'),
 ('A4', 'Tijd', 'Nep-countdown-GIF in de mail', 'Midden tot hoog: eindtijd die niet bestaat of per open opnieuw begint',
  'Smooche via countdownmail.com; "Expires Today"-zegel op een code die morgen weer werkt.',
  mail('<div class="cd"><span>00</span>:<span>59</span>:<span>36</span></div><div class="stamp">EXPIRES TODAY</div><p class="sm">Telt bij elke open opnieuw vanaf 01:00:00.</p>'),
  mail('<div class="cd"><span>00</span>:<span>59</span>:<span>36</span></div><p class="dl">Ends tonight at 11:59 PM ET.</p><p class="sm">Live GIF (Sendtric/NiftyImages) die naar de echte backend-tijd telt en daarna ENDED toont. Alleen als A/B in FLASH en GIFTS.</p>')),
 ('B1', 'Schaarste', 'Nep "only 3 left"', 'Hoog: UCPD punt 7, FTC; VK boetes tot 10% omzet',
  'Smooche: "running pretty low on stock". Siraat eerder: "High demand, few units left" bij 1.098 stuks (nu verborgen, staat nog in de HTML).',
  pdp_mini('<div class="red">Only 3 left in stock!</div><div class="sm">Running pretty low on stock</div>'),
  pdp_mini('<div class="ok">In stock</div><div class="sm">Een getal alleen live uit Shopify/ShipBob (variabele UNITS), bv. "14 left in this batch". Anders geen voorraadregel.</div>')),
 ('B2', 'Schaarste', 'Nep "93% sold"-balk', 'Hoog: vast getal zonder noemer is een onware feitelijke claim',
  'Flash-sale-templates; Siraat PDP nu: <code>data-bf-count="93"</code> hardgecodeerd met "breathing"-animatie.',
  site('<div class="sold"><i style="width:93%"></i></div><div class="sm"><b>93% sold</b> · Hurry, almost gone</div>'),
  site('<div class="sm"><b>2,140 orders since Nov 1</b> (voorbeeldgetal; alleen als het live uit Shopify komt)</div><div class="sm">Of: geen balk.</div>')),
 ('B3', 'Schaarste', '"High demand" / "selling fast"', 'Midden tot hoog: Emma Sleep ("High Demand" bij 7 stuks per dag)',
  'Smooche, Emma Sleep. Siraat PDP: "Selling fast", "Due to high demand, quantities are limited."',
  pdp_mini('<div class="red">Selling fast</div><div class="sm">Due to high demand, quantities are limited.</div>'),
  pdp_mini('<div class="ok">100,000+ customers</div><div class="sm">75-year warranty · 30-day returns</div>')),
 ('B4', 'Schaarste', 'Nep-exclusiviteit: vaste "VIP password"', 'Midden: "only for you" is onwaar zodra de code op couponsites staat',
  'Smooche: "VIP ONLY... YOUR PASSWORD: [vaste code]".',
  mail('<div class="eb">VIP ONLY</div><div class="big">YOUR PASSWORD:<br><span class="code2">MERKVIP</span></div><p class="sm">Zelfde code voor de hele lijst.</p>'),
  mail('<div class="eb">YOUR OWN CODE</div><div class="big"><span class="code2">VIP-7KQ2</span></div><p class="dl">One use. Stops working Sunday at 11:59 PM ET.</p><p class="sm">Unieke <code>{% coupon_code %}</code> per profiel.</p>')),
 ('C1', 'Social proof', 'Nep "12 people viewing" / "Jane just bought"', 'Hoog: FTC-reviewregel (nep-sociale indicatoren), UCPD; CMA 2019',
  'Mathur e.a.: activiteitsmeldingen, deels willekeurig gegenereerd door apps.',
  pdp_mini('<div class="sm">👀 <b>12 people</b> are viewing this right now</div><div class="toast">Jane from Ohio just bought this · 2 min ago</div>'),
  pdp_mini('<div class="sm"><b>1,240 orders this week</b> (voorbeeldgetal, alleen uit Shopify)</div><div class="sm">Of een letterlijke review met naam.</div>')),
 ('C2', 'Social proof', 'Nepreviews, gekochte of gefilterde reviews', 'Zeer hoog: 16 CFR 465, tot $53.088 per overtreding',
  'Smooche: sterren zonder bron. FTC v. Fashion Nova (onderdrukte negatieve reviews).',
  site('<div class="stars">★★★★★</div><div class="sm">"Best pan ever!!!"</div><div class="sm">Geen naam, geen bron, alleen 5 sterren zichtbaar.</div>'),
  site('<div class="stars">★★★★★</div><div class="sm">"I ordered one pan to try it out." Sunny C., verified buyer</div><div class="sm">Letterlijk, met naam; 3-sterrenreviews blijven zichtbaar.</div>')),
 ('D1', 'Mail', 'Nep "Re:" / "Fwd:"', 'Hoog: CAN-SPAM 7704(a)(2), FTC v. Jumpstart ($900.000)',
  'Veel DTC- en infoproductlijsten. Open-lift, geen klik-lift, wel spammeldingen.',
  inbox('Merk X', 'Re: your question', 'Following up on this, did you see it?', fake=True),
  inbox('Benjamin from Siraat', 'Last hours', "A short note from me, then I'll leave you alone.") + '<p class="sm">Echte brief van Benjamin, geen voorvoegsel; antwoorden op de reply-to worden gelezen.</p>'),
 ('D2', 'Mail', 'Nep-orderstatus ("Your order is pending")', 'Zeer hoog: CAN-SPAM, FTC sectie 5, chargebacks',
  'Smooche, letterlijk: "Your order is pending... will be marked as canceled within 24 hours" terwijl er geen order is.',
  inbox('Merk X', 'Your order is pending.', 'Pending orders not completed within 24 hours will be marked as canceled.', fake=True),
  inbox('Siraat', 'Your checkout is still open: extra 10% applied', 'An extra 10% on top of the sale, applied with the button.') + '<p class="sm">Alleen naar een echte Started Checkout zonder order.</p>'),
 ('D3', 'Mail', 'Nep-persoonlijk tegoed', 'Hoog: verzonnen saldo en verzonnen handeling (UCPD art. 6)',
  'Smooche, letterlijk: "Yesterday we added $12.24 to your account... support team just checked" (eigenlijk een code met $30 minimum).',
  inbox('Merk X', 'Yesterday we added $12.24 to your account', "Our customer support team just checked and noticed you haven't used it.", fake=True),
  inbox('Benjamin from Siraat', 'Your ${{CREDIT}} expires at midnight ET', 'Earned by your past orders. Applied at checkout, after the sale price.') + '<p class="sm">Echt Rise.ai-tegoed op het profiel met echte vervaldatum.</p>'),
 ('D4', 'Mail', '"(1)" of 🔔 als nep-notificatie', 'Midden tot hoog: misleidend onderwerp',
  'Smooche, letterlijk: "(1) Your store credit is updated."',
  inbox('Merk X', '(1) Your store credit is updated.', 'Tap to view your balance.', fake=True),
  inbox('Siraat', 'Your own 10% expires in 48 hours', 'One use, already applied with the button.') + '<p class="sm">Getallen die echte informatie zijn: 5 gifts, $X tegoed, 48 uur.</p>'),
 ('D5', 'Mail', 'Persona die verzonnen dingen doet', 'Midden: de verzonnen handeling, niet de persona; CAN-SPAM 7704(a)(1)',
  'Smooche: "Chloe from Smooche: I extended your credit".',
  inbox('Chloe from Merk X', 'Chloe here: I set this aside for you', 'I asked the team to hold it until tonight.', fake=True),
  inbox('Benjamin from Siraat', 'Benjamin here: it ends in {{HOURS_LEFT}} hours', "One short note from me, then I'll leave you alone.") + '<p class="sm">Benjamin bestaat en zegt alleen wat echt gebeurd is.</p>'),
 ('D6', 'Mail', 'Preheader-lokaas', 'Midden: onderwerp plus preview samen misleidend, klachten',
  'Veel BF-lijsten: de preview belooft iets wat de mail niet geeft.',
  inbox('Merk X', 'Black Friday is here', 'Your free pan is inside 🎁', fake=True),
  inbox('Siraat', '24-hour flash: 2 pans + 2 lids', 'Ends tonight 11:59 PM ET. 2 Pans + 2 Lids $199.')),
 ('D7', 'Mail', 'Verstopte of moeilijke afmelding', 'Hoog: CAN-SPAM, Gmail/Yahoo (RFC 8058, 2 dagen)',
  'Lichtgrijs 8 px, login vereist, "manage preferences" zonder uitschrijfknop.',
  mail('<div class="foot tiny">To stop receiving these emails, log in to your account and update your communication settings.</div>'),
  mail('<div class="foot"><u>Unsubscribe</u> · <u>Preferences</u> · <u>Fewer emails until Nov 30</u><br>Vaste footer-partial, one-click unsubscribe.</div>')),
 ('D8', 'Mail', 'Volume zonder nieuwe reden (13 mails in 41 uur)', 'Laag juridisch, midden deliverability',
  'Smooche. Eigen data 7 nov: opens zakken naar 26,5% bij de vijfde campagne zonder nieuwe reden.',
  '<div class="stack">' + ''.join(inbox('Merk X', s, 'Last chance.', time=t, fake=True) for s, t in [('FINAL HOURS', '8:02 AM'), ('Re: your cart', '10:30 AM'), ('LAST CHANCE ⏰', '1:15 PM'), ('Ends tonight!!', '4:40 PM'), ('(1) Your store credit is updated.', '7:05 PM'), ('Final hour', '11:00 PM')]) + '</div>',
  '<div class="stack">' + inbox('Siraat', '24-hour flash: 2 pans + 2 lids', 'Flash price until tonight at 11:59 PM ET.', time='9:00 AM') + inbox('Benjamin from Siraat', 'Last hours', 'Only to openers without a click.', time='8:00 PM') + '</div><p class="sm">Max 3 per dag (4 vanaf 27 nov), elke mail een nieuwe echte reden.</p>'),
 ('E1', 'Prijs', 'Opgeblazen ankerprijs', 'Hoog in EU (Omnibus art. 6a), VS 16 CFR 233',
  'Overal in DTC; Emma Sleep. Siraat: "Regular price $664" voor 2 Pans + 2 Lids nu $199.',
  site('<div class="price">$199 <s>$664</s> <span class="tag">70% OFF</span></div><div class="sm">Regular price $664</div>'),
  site('<div class="price">$199 <span class="tag">BLACK FRIDAY</span></div><div class="sm">One pan is $144. Four pieces: $199.</div><div class="sm">EU: korting tegen de laagste prijs van de laatste 30 dagen.</div>')),
 ('E2', 'Prijs', 'Drip pricing / verborgen kosten', 'Midden tot hoog; Baymard: 48% haakt af op extra kosten',
  'Mathur e.a. (hidden costs).',
  site('<table class="co"><tr><td>Subtotal</td><td>$199.00</td></tr><tr><td>Handling fee</td><td>$9.95</td></tr><tr><td>Priority processing</td><td>$4.99</td></tr><tr><th>Total</th><th>$213.94</th></tr></table><p class="sm">Pas zichtbaar in de laatste stap.</p>'),
  site('<table class="co"><tr><td>Subtotal</td><td>$199.00</td></tr><tr><td>Shipping, duties</td><td>Free</td></tr><tr><th>Total</th><th>$199.00</th></tr></table><p class="sm">"Free shipping, duties paid" boven de vouw.</p>')),
 ('E3', 'Prijs', '"Free" dat niet free is / "activated for you"', 'Midden',
  'Smooche, letterlijk: "Free shipping has been activated for you" (geldt voor iedereen).',
  inbox('Merk X', 'Free shipping has been activated for you', 'Only on your account, today.', fake=True),
  inbox('Siraat', 'Free shipping on every order, duties paid', 'Plus 5 free gifts until Nov 30.')),
 ('F1', 'Checkout', 'Voorgevinkte upsell', 'Hoog: EU art. 22 Consumentenrechtenrichtlijn, FTC',
  'Shipping-protection-apps standaard aan; Mathur e.a. (sneak into basket).',
  site('<label class="cb on">☑ Shipping protection $3.99</label><label class="cb on">☑ Priority processing $4.99</label>'),
  site('<label class="cb">☐ Add a steel lid for $39</label><div class="sm">Niets standaard aan; post-purchase met duidelijke "No thanks".</div>')),
 ('F2', 'Pop-up', 'Confirmshaming', 'Laag juridisch, midden reputatie (PFAS-boodschap leest snel als angst)',
  'Mathur e.a.; veel pop-ups.',
  site('<div class="pop"><b>Get 10% off</b><div class="btn sm2">Yes please</div><u class="no">No thanks, I like toxic pans</u></div>'),
  site('<div class="pop"><b>Get 10% off</b><div class="btn sm2">Yes please</div><u class="no">No thanks</u></div>')),
 ('F3', 'Pop-up', 'Nep spin-to-win (iedereen wint hetzelfde)', 'Hoog in EU (UCPD punt 31); VS sweepstakes-regels',
  'Smooche: "Try your luck... see what you win".',
  site('<div class="pop"><div class="wheel"></div><b>You won 10% off!</b><div class="sm">Try your luck, see what you win.</div></div>'),
  site('<div class="pop"><b>Order by Sunday 11:59 PM ET</b><div class="sm">One entry in this week\'s PFAS water filter draw. No purchase necessary, <u>official rules</u>.</div></div>')),
 ('F4', 'Abonnement', 'Negative option / moeilijk opzeggen', 'Zeer hoog: ROSCA, FTC v. Amazon ($2,5 mld)',
  'Amazon Prime (FTC, sept 2025).',
  site('<label class="cb on">◉ Subscribe and save 20%</label><label class="cb">○ One-time purchase</label><div class="sm tiny">Cancel by calling customer service.</div>'),
  site('<label class="cb on">◉ One-time purchase</label><label class="cb">○ Subscribe: 20% off every delivery</label><div class="sm">Skip or cancel in 2 clicks, reminder before each charge.</div>')),
 ('S1', 'Siraat nu', 'K1-ACC: "4 gifts pending"', 'Licht: echte cart, maar "pending" is het woord van de nep-order-tactiek',
  'Live cartflow K1-ACC (template WrMYnX) en <code>klaviyo/templates/v3/cart/k1-acc.html</code>.',
  mail('<div class="strip">4 GIFTS STILL PENDING ON YOUR CART</div><p class="sm">Preview: "4 gifts are pending with it".</p>'),
  mail('<div class="strip">YOUR 5 GIFTS ARE IN THE CART WITH IT</div><p class="sm">Zelfde feit, zonder orderstatus-woord; en 5 gifts in plaats van 4 ([GIFTS5]).</p>')),
 ('S2', 'Siraat nu', '"48-hour code" die in Shopify een jaar geldt', 'Hoog: de deadline is onwaar, ook al is het aanbod goed',
  'flows-ontwerp 2.3: Coupon Assigned toont CouponExpirationDate een jaar na aanmaak bij pools B2, K3, C4.',
  mail('<div class="eb">YOUR OWN CODE</div><p class="dl">Your 10% expires in 48 hours.</p><div class="be">Shopify: vervalt 8 nov 2027</div>'),
  mail('<div class="eb">YOUR OWN CODE</div><p class="dl">Your 10% expires Tuesday at 9:00 AM ET.</p><div class="be ok2">Shopify: vervalt echt 48 uur na uitgifte; mail toont de tijd uit het event</div>')),
]

def sec_blackhat():
    cards = []
    for code, cat, name, risk, src, black, white in BH:
        wm = 'NU LIVE, VERVANGEN' if code.startswith('S') else 'REFERENTIE, NIET VERSTUREN'
        cards.append(('<article class="bh-card" id="bh-%s"><header><span class="eyebrow">%s · %s</span><h4>%s</h4><p class="risk">%s</p><p class="src">%s</p></header>'
                      '<div class="pair"><div class="col"><div class="lab red">Black-hat</div><div class="bh" data-wm="%s">%s</div></div>'
                      '<div class="col"><div class="lab green">White-hat Siraat</div><div class="wh">%s</div></div></div></article>') % (
            code, code, E(cat), E(name), E(risk), src, wm, black, white))
    return len(BH), ''.join(cards)

# ---------- sectie 5: site ----------
def sec_site():
    before = ('<div class="pdp bh" data-wm="NU LIVE, VERVANGEN"><div class="bar">VIP BLACK FRIDAY SALE · 70% OFF + 5 GIFTS <span class="tmr">02h 43m 00</span><i class="mk">1</i></div>'
              '<div class="pdpb"><img src="PANIMG" alt="Pan Pro" loading="lazy"><div class="bb"><div class="pt">Titanium Hammered Pan Pro</div>'
              '<div class="price">$144 <s>$480</s> <span class="tag">70% OFF</span><i class="mk">6</i></div>'
              '<div class="flash"><b>Our biggest sale of the year · Selling fast</b><i class="mk">3</i><div>Ends in <span class="tmr dark">07:55:46</span><i class="mk">1</i></div>'
              '<div class="sold"><i style="width:93%"></i></div><div class="sm"><b>93% sold</b><i class="mk">2</i></div>'
              '<div class="sm">Due to high demand, quantities are limited.<i class="mk">3</i></div>'
              '<div class="sm">✦ Refunding 10 random orders today ✦ · Today only<i class="mk">4</i></div></div>'
              '<div class="sm">Delivery from your local warehouse · Express shipping <s>$15</s> FREE<i class="mk">5</i></div>'
              '<div class="btn">Add to cart</div></div></div></div>').replace('PANIMG', PAN_IMG)
    after = ('<div class="pdp"><div class="bar">BLACK FRIDAY · UP TO 70% OFF + 5 GIFTS · ENDS NOV 30, 11:59 PM ET</div>'
             '<div class="pdpb"><img src="PANIMG" alt="Pan Pro" loading="lazy"><div class="bb"><div class="pt">Titanium Hammered Pan Pro</div>'
             '<div class="price">$144 <s>$480</s> <span class="tag">70% OFF</span></div>'
             '<div class="flash"><b>Our biggest sale of the year</b><div>Black Friday ends <b>Nov 30 at 11:59 PM ET</b></div>'
             '<div class="sm">Same end time for everyone (<code>data-siraat-end</code>). After that: "Ended", and the price really changes.</div>'
             '<div class="sm">A chance to win your order back: weekly draw, <u>official rules</u>.</div></div>'
             '<div class="sm">Free shipping, duties paid. 5 free gifts with every order.</div>'
             '<div class="btn">Add to cart</div><div class="sm">30-day returns · 75-year warranty · 100,000+ customers</div></div></div></div>').replace('PANIMG', PAN_IMG)
    legend = [('1', 'Timer per bezoeker die zichzelf reset: balk 2 u 43 m, koopbox "7:55:46" (localStorage, <code>siraat-sale-countdown.js</code>). Vervangen door vaste <code>data-siraat-end</code> of de datumregel.'),
              ('2', 'Hardgecodeerde "93% sold"-balk met "breathing"-animatie (<code>data-bf-count="93"</code>). Weg, of een echte teller met noemer uit Shopify.'),
              ('3', '"Selling fast" en "Due to high demand, quantities are limited." bij ruime voorraad. Weg tenzij echte data; verborgen "few units left" ook uit de HTML.'),
              ('4', '"Refunding 10 random orders today · Today only" zonder regels en elke dag. Alleen op trekkingsdagen, met link naar officiële regels en AMOE.'),
              ('5', '"Delivery from your local warehouse": misleidende leverclaim (chargebacks). "Free shipping, duties paid" met echte levertijd.'),
              ('6', 'Ankerprijs: houdbaar in de VS alleen als $480 echt de normale prijs was; EU: laagste prijs van 30 dagen (Omnibus).')]
    lg = ''.join('<li><i class="mk">%s</i> %s</li>' % (a, b) for a, b in legend)
    return ('<div class="pair site-pair"><div class="col"><div class="lab red">Nu op siraatskitchen.com (8 nov, als bezoeker opgehaald)</div>%s</div>'
            '<div class="col"><div class="lab green">Voorstel: één echte eindtijd, geen nep-balken</div>%s</div></div><ol class="legend">%s</ol>') % (before, after, lg)

CSS = r"""
:root{--bg:#F5F4EF;--surface:#fff;--ink:#272727;--muted:#66625C;--line:#E2DED5;--cream:#F8F7F2;--yellow:#FFB800;
--groen:#2F7A52;--oranje:#C46A12;--rood:#B3261E;--sans:Inter,system-ui,-apple-system,'Segoe UI',Arial,sans-serif;--serif:'Newsreader',Georgia,'Times New Roman',serif;color-scheme:light}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.5;overflow-x:hidden}
a{color:inherit}
code{font-size:12px;background:#EEEBE3;padding:1px 4px;border-radius:3px;overflow-wrap:anywhere}
.wrap{max-width:1180px;margin:0 auto;padding:24px 16px 80px}
h1,h2,h3{font-family:var(--serif);font-weight:600;margin:0;line-height:1.15;text-wrap:balance}
h1{font-size:clamp(30px,5vw,46px)}h2{font-size:clamp(24px,3.6vw,34px)}h3{font-size:22px}
h4{margin:0 0 12px;font-size:16px;font-weight:700}
h5{margin:14px 0 6px;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
p{margin:0}
.eyebrow{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:600}
.intro{display:flex;flex-direction:column;gap:12px;margin-bottom:20px}
.intro p{max-width:75ch;color:var(--muted)}
.legendbox{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:13px;background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:12px 14px}
.legendbox span{display:inline-flex;align-items:center;gap:6px}
nav.top{position:sticky;top:0;z-index:20;background:rgba(245,244,239,.96);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);margin:0 -16px 24px;padding:10px 16px;display:flex;gap:6px;overflow-x:auto;scrollbar-width:none}
nav.top a{flex:0 0 auto;text-decoration:none;font-size:13px;font-weight:600;padding:6px 10px;border-radius:999px;background:var(--surface);border:1px solid var(--line)}
nav.top a.warn{background:#FBE7E5;border-color:#E9B4AE;color:var(--rood)}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 18px}
.chips a{font-size:12px;text-decoration:none;padding:4px 9px;border-radius:999px;border:1px solid var(--line);background:var(--surface)}
section.top{margin-top:40px;scroll-margin-top:60px}
section.top>header{display:flex;flex-direction:column;gap:8px;margin-bottom:12px}
section.top>header p{max-width:80ch;color:var(--muted)}
.flow{margin:26px 0 10px;scroll-margin-top:60px}
.fh{display:flex;flex-direction:column;gap:6px;padding:14px 0;border-top:2px solid var(--ink);margin-bottom:12px}
.fh p{font-size:13px;color:var(--muted);max-width:90ch}
.fstat{font-variant-numeric:tabular-nums}
details{font-size:13px}
details summary{cursor:pointer;font-weight:600;color:var(--ink)}
details ul{margin:6px 0 0;padding-left:18px;color:var(--muted)}
details li{margin:3px 0;overflow-wrap:anywhere}
.nooit li s{color:var(--rood);margin-right:6px}
.mcard{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:16px;margin:14px 0}
.new{font-size:10px;letter-spacing:.08em;text-transform:uppercase;background:var(--ink);color:#fff;border-radius:4px;padding:2px 6px;vertical-align:2px}
.pair{display:grid;grid-template-columns:1fr;gap:18px}
@media (min-width:900px){.pair{grid-template-columns:1fr 1fr}}
.col{min-width:0;display:flex;flex-direction:column;gap:10px}
.lab{font-size:11px;letter-spacing:.1em;text-transform:uppercase;font-weight:700;color:var(--muted);display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.lab.red{color:var(--rood)}.lab.green{color:var(--groen)}
.meta,.cap,.cur{font-size:12px;color:var(--muted)}
.cur{background:var(--cream);border-radius:6px;padding:8px 10px}
.empty{border:1px dashed var(--line);border-radius:8px;padding:28px 16px;text-align:center;color:var(--muted);font-size:13px}
.shot{display:block;max-height:560px;overflow:hidden;border:1px solid var(--line);border-radius:8px;background:#fff;align-self:flex-start;width:min(300px,100%)}
.shot img{display:block;width:100%;height:auto}
.shot.tall{max-height:640px}
/* inbox */
.inbox{display:flex;gap:10px;background:#fff;border:1px solid var(--line);border-radius:8px;padding:10px 12px;font-family:Roboto,Arial,var(--sans)}
.inbox .av{flex:0 0 34px;height:34px;border-radius:50%;background:var(--ink);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px}
.inbox.fake .av{background:#7A2E2A}
.ib{min-width:0;flex:1}
.from{display:flex;justify-content:space-between;gap:8px;font-size:14px}
.tm{font-size:12px;color:var(--muted);white-space:nowrap}
.subj{font-weight:700;font-size:14px;overflow-wrap:anywhere}
.prev{font-size:13px;color:#5f6368;overflow-wrap:anywhere}
.inote{font-size:11px;color:var(--muted);margin-top:4px}
.stack{display:flex;flex-direction:column;gap:0}
.stack .inbox{border-radius:0;margin-top:-1px}
.stack .inbox:first-child{border-radius:8px 8px 0 0}.stack .inbox:last-child{border-radius:0 0 8px 8px}
.rk{font-size:10px;letter-spacing:.06em;text-transform:uppercase;font-weight:700;padding:1px 6px;border-radius:4px;color:#fff;vertical-align:1px;font-family:var(--sans)}
.rk.groen{background:var(--groen)}.rk.oranje{background:var(--oranje)}.rk.rood{background:var(--rood)}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%;flex:0 0 10px;margin-top:4px}
.dot.groen{background:var(--groen)}.dot.oranje{background:var(--oranje)}.dot.rood{background:var(--rood)}
.ph{border-bottom:1.5px dotted currentColor;background:rgba(255,184,0,.18)}
/* phone mock */
.phone{width:min(340px,100%);border:1px solid #D5D1C8;border-radius:22px;overflow:hidden;background:#fff;box-shadow:0 6px 18px rgba(0,0,0,.06);align-self:flex-start}
.mtop{background:var(--ink);color:#fff;text-align:center;font-size:10.5px;letter-spacing:.14em;font-weight:700;padding:8px 10px}
.mhead{background:var(--cream);border-bottom:1px solid #ECE7DD;padding:12px 18px}
.mhead img{display:block;width:120px;height:auto}
.mhero{position:relative;height:250px;background-size:cover;background-position:center;display:flex;align-items:flex-end;padding:12px}
.glass{background:rgba(39,39,39,.78);color:#fff;border-radius:8px;padding:12px 14px;width:100%}
.hk{font-family:var(--serif);font-size:24px;line-height:1.12;font-weight:600}
.hs{font-size:13px;margin-top:4px;opacity:.92}
.mbody{padding:14px 18px 18px;display:flex;flex-direction:column;gap:10px}
.mbody .bt{font-size:13px;color:#3a3a3a}
.dl{font-size:13px;font-weight:700}
.btn{background:var(--ink);color:#fff;text-align:center;font-weight:700;font-size:13px;letter-spacing:.06em;text-transform:uppercase;padding:13px 14px;border-radius:4px}
.fr{font-size:11px;color:var(--muted);text-align:center}
.ps{font-size:13px;font-style:italic;border-top:1px solid var(--line);padding-top:10px}
/* lines */
.lines{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px;font-size:13px}
.lines li{display:flex;flex-wrap:wrap;gap:4px 8px;align-items:flex-start;border-bottom:1px solid #F0EDE6;padding-bottom:6px}
.veld{font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:700;min-width:86px;margin-top:2px}
.cp{flex:1 1 200px;min-width:0;overflow-wrap:anywhere}
.codes{display:flex;flex-wrap:wrap;gap:3px;width:100%;padding-left:18px}
.code{font-size:10px;font-weight:600;background:#EEEBE3;border-radius:3px;padding:1px 5px;cursor:help}
.nt{width:100%;padding-left:18px;font-size:11px;color:var(--oranje)}
.var summary{font-weight:500}
/* thumbs */
.gh{margin:22px 0 10px;font-size:19px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}
.thumb{margin:0;background:var(--surface);border:1px solid var(--line);border-radius:10px;overflow:hidden;display:flex;flex-direction:column}
.thumb>a{display:block;height:380px;overflow:hidden;background:#fff;border-bottom:1px solid var(--line)}
.thumb img{display:block;width:100%;height:auto}
.thumb figcaption{padding:10px;display:flex;flex-direction:column;gap:8px;font-size:13px}
.lk{font-size:12px;color:var(--muted)}
/* black-hat */
.bh-warn{background:#FBE7E5;border:2px solid var(--rood);color:#5c1612;border-radius:10px;padding:14px 16px;font-size:14px}
.bh-card{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:16px;margin:14px 0;scroll-margin-top:60px}
.bh-card header{display:flex;flex-direction:column;gap:4px;margin-bottom:12px}
.bh-card .risk{font-size:13px;color:var(--rood);font-weight:600}
.bh-card .src{font-size:12px;color:var(--muted)}
.bh{position:relative;overflow:hidden;border-radius:8px;min-height:120px;outline:2px solid rgba(179,38,30,.35);outline-offset:2px}
.bh::after{content:attr(data-wm);position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-22deg);font:800 15px/1 var(--sans);letter-spacing:.06em;color:rgba(179,38,30,.42);white-space:nowrap;background:rgba(255,255,255,.35);pointer-events:none;border:3px solid rgba(179,38,30,.30);padding:6px 10px;border-radius:6px}
.wh{border-radius:8px}
.sm{font-size:12px;color:var(--muted);margin-top:4px}
.tiny{font-size:8px!important;color:#bbb!important}
.site{background:#fff;border:1px solid var(--line);border-radius:8px;padding:12px;font-size:13px}
.bar{background:var(--ink);color:#fff;font-size:11px;letter-spacing:.08em;font-weight:700;padding:8px 10px;text-align:center;border-radius:4px;position:relative}
.tmr{font-family:ui-monospace,Menlo,monospace;background:#fff;color:var(--ink);padding:1px 6px;border-radius:3px;margin-left:6px;font-weight:700;letter-spacing:.02em}
.tmr.dark{background:var(--ink);color:#fff}
.frames{display:flex;gap:10px;margin-top:10px;flex-wrap:wrap}
.frames div{display:flex;flex-direction:column;gap:4px;font-size:12px}
.pm{display:flex;gap:10px;align-items:flex-start}
.pm img{width:72px;height:72px;object-fit:cover;border-radius:6px;background:#f2f2f2}
.pt{font-weight:700;font-size:14px}
.red{color:var(--rood);font-weight:700}.ok{color:var(--groen);font-weight:700}
.toast{margin-top:8px;background:var(--ink);color:#fff;font-size:11px;border-radius:6px;padding:6px 8px;display:inline-block}
.sold{height:8px;background:#EEE;border-radius:4px;overflow:hidden;margin-top:8px}.sold i{display:block;height:100%;background:var(--rood)}
.stars{color:#C99A00;letter-spacing:2px}
.snip{background:#fff;border:1px solid var(--line);border-radius:8px;padding:14px;text-align:center;display:flex;flex-direction:column;gap:8px;align-items:center}
.cd{display:flex;gap:4px;align-items:center;font:700 22px ui-monospace,Menlo,monospace}
.cd span{background:var(--ink);color:#fff;border-radius:4px;padding:6px 8px}
.stamp{border:2px solid var(--rood);color:var(--rood);font-weight:800;font-size:12px;letter-spacing:.1em;padding:3px 8px;transform:rotate(-6deg)}
.eb{font-size:11px;letter-spacing:.14em;font-weight:700;color:var(--muted)}
.big{font-family:var(--serif);font-size:20px;font-weight:600}
.code2{font-family:ui-monospace,Menlo,monospace;border:2px dashed var(--ink);padding:2px 8px;display:inline-block;margin-top:4px;font-size:18px}
.foot{font-size:12px;color:var(--muted)}
.price{font-size:20px;font-weight:700;display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:4px}
.price s{font-size:14px;color:var(--muted);font-weight:400}
.tag{background:var(--yellow);color:var(--ink);font-size:11px;font-weight:800;letter-spacing:.06em;padding:3px 7px;border-radius:3px}
table.co{width:100%;border-collapse:collapse;font-size:13px}
table.co td,table.co th{padding:4px 0;border-bottom:1px solid #F0EDE6;text-align:left}
table.co td:last-child,table.co th:last-child{text-align:right}
.cb{display:block;padding:6px 8px;border:1px solid var(--line);border-radius:6px;margin-bottom:6px}
.cb.on{border-color:var(--ink);font-weight:600}
.pop{border:1px solid var(--line);border-radius:10px;padding:14px;display:flex;flex-direction:column;gap:8px;align-items:center;text-align:center}
.btn.sm2{padding:9px 14px;width:100%}
.no{font-size:12px;color:var(--muted)}
.wheel{width:70px;height:70px;border-radius:50%;background:conic-gradient(var(--yellow) 0 25%,#272727 0 50%,#E2DED5 0 75%,#B3261E 0)}
.strip{background:#B8442C;color:#fff;font-size:11px;letter-spacing:.1em;font-weight:700;padding:8px 10px;width:100%}
.be{font-size:11px;font-weight:700;color:#fff;background:var(--rood);border-radius:4px;padding:3px 8px}
.be.ok2{background:var(--groen)}
/* site */
.pdp{background:#fff;border:1px solid var(--line);border-radius:10px;overflow:hidden;font-size:13px}
.pdp .bar{border-radius:0}
.pdpb{display:grid;grid-template-columns:1fr;gap:12px;padding:14px}
@media (min-width:560px){.pdpb{grid-template-columns:150px 1fr}}
.pdpb>img{width:100%;max-width:220px;aspect-ratio:1;object-fit:cover;border-radius:8px;background:#f2f2f2}
.bb{display:flex;flex-direction:column;gap:8px;min-width:0}
.flash{border:1px solid var(--line);border-radius:8px;padding:10px;display:flex;flex-direction:column;gap:6px;background:var(--cream)}
.mk{display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:50%;background:var(--rood);color:#fff;font-size:11px;font-style:normal;font-weight:800;margin-left:6px;vertical-align:1px}
.legend{list-style:none;padding:0;margin:16px 0 0;display:flex;flex-direction:column;gap:8px;font-size:13px;max-width:90ch}
.legend .mk{margin:0 6px 0 0}
.site-pair .bh::after{font-size:clamp(20px,4vw,34px)}
footer.end{margin-top:50px;font-size:12px;color:var(--muted);border-top:1px solid var(--line);padding-top:14px}
"""

def main():
    nmails, nflows, fnav, flows_html = sec_flows()
    camps = sec_campaigns()
    nreb, reb = sec_rebuilt()
    nbh, bh = sec_blackhat()
    sitehtml = sec_site()
    samples = ' · '.join('<span><b>{{%s}}</b> = %s</span>' % (k, E(SAMPLE[k])) for k in ('DEADLINE', 'DEADLINE_SHORT', 'MINUTES_LEFT', 'HOURS_LEFT', 'CREDIT', 'NEXT_CHARGE', 'UNITS', 'FLASH_PRICE'))
    doc = f"""<!doctype html>
<html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Urgentie-voorbeelden</title>
<meta name="description" content="Visuele galerij urgentie-sprint november 2026: flows nu tegen te agressief, campagnes, herbouwde mails, black-hat referentie en site.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Newsreader:opsz,wght@6..72,600&display=swap">
<style>{CSS}</style></head><body><div class="wrap">
<div class="intro"><span class="eyebrow">Urgentie-sprint · 8 nov 2026 · alleen lezen, niets verstuurd</span>
<h1>Urgentie-voorbeelden</h1>
<p>Alles wat we voorstellen, zichtbaar gemaakt. Links steeds wat nu live staat, rechts de bewust te harde baseline uit flows-agressief en copy-agressief, die Floris per mail afzwakt. Onderaan de black-hat-kant als referentie (nooit versturen) en de koopbox op de site. Mocks zijn illustraties, geen Klaviyo-templates.</p>
<div class="legendbox"><span>{dot('groen')} groen: waar zodra de backend-voorwaarde klopt</span><span>{dot('oranje')} oranje: strikte extra voorwaarde, caps, emoji of verliesframing</span><span>{dot('rood')} rood: alleen met extra techniek; standaard niet versturen</span></div>
<div class="legendbox"><span>Voorbeeldwaarden, <span class="ph">zo gemarkeerd</span>:</span> {samples} <span><b>BFCODE</b> = placeholder (echte code nooit in de repo)</span></div>
</div>
<nav class="top"><a href="#flows">1. Flows: nu vs agressief</a><a href="#campagnes">2. Campagnes</a><a href="#herbouwd">3. Herbouwde mails</a><a class="warn" href="#blackhat">4. Black-hat (niet versturen)</a><a href="#site">5. Site</a></nav>

<section class="top" id="flows"><header><span class="eyebrow">Sectie 1 · {nflows} flows · {nmails} mails</span><h2>Flows: nu vs agressief</h2>
<p>Per mail: links het huidige onderwerp, de preview en de bovenkant van de live template (lokaal gerenderd met een US-voorbeeldprofiel). Rechts de hardste stand: het onderwerp en de preview met het hoogste risico in de inbox, en de bovenkant van de mail met topbalk, kop over het bestaande hero-beeld, deadline-regel, knop en P.S. Daaronder alle regels met risico en de "waar als"-codes (beweeg over een code voor de voorwaarde, of open "voorwaarden voluit"). Volgorde: prioriteit, dan omzet.</p></header>
<div class="chips">{fnav}</div>
{flows_html}</section>

<section class="top" id="campagnes"><header><span class="eyebrow">Sectie 2 · 6 campagnes</span><h2>Campagnes: normaal vs agressief</h2>
<p>Links de gebouwde campagne (preview uit klaviyo/templates/v3/campaigns/urgency-1108), rechts de vijf agressieve onderwerpen als inbox, de hardste hero, knop en aftelregel over hetzelfde hero-beeld, en alle opties met risico.</p></header>
{camps}</section>

<section class="top" id="herbouwd"><header><span class="eyebrow">Sectie 3 · {nreb} mails</span><h2>Herbouwde mails</h2>
<p>Klaar in de repo, nog niet live. Klik op een beeld voor de volle preview.</p></header>
{reb}</section>

<section class="top" id="blackhat"><header><span class="eyebrow">Sectie 4 · {nbh} tactieken</span><h2>Black-hat referentie (NIET VERSTUREN)</h2>
<div class="bh-warn"><b>Alleen referentie.</b> De linkerkant toont hoe de agressieve kant het doet, op basis van gedocumenteerde openbare voorbeelden (Smooche-regels letterlijk, afzender geanonimiseerd als "Merk X") en wat de livesite van Siraat nu doet. Dit zijn visuele mocks in deze galerij, geen templates. Rechts de eerlijke Siraat-versie die het meeste effect houdt. Bron: black-hat/black-hat-referentie.md.</div></header>
{bh}</section>

<section class="top" id="site"><header><span class="eyebrow">Sectie 5 · koopbox PDP</span><h2>Site: koopbox nu vs voorstel</h2>
<p>De mail met een echte deadline landt nu op een pagina met een tweede, nep-deadline. Links de koopbox zoals op 8 nov opgehaald, rechts één echte eindtijd en geen nep-balken.</p></header>
{sitehtml}</section>

<footer class="end">Gebouwd met voorbeelden/_tools/build.py uit flows-agressief.json, copy-agressief.json, copy.json, black-hat-referentie.md en de lokaal gerenderde live templates (Klaviyo alleen GET). Niets in Klaviyo of Shopify gewijzigd, niets verstuurd.</footer>
</div></body></html>"""
    assert not re.search('[–—]', doc), 'gedachtestreepje in uitvoer'
    assert not re.search(r'BF-[A-Z0-9]{4,}', doc), 'echte code in uitvoer'
    open(os.path.join(OUT, 'index.html'), 'w').write(doc)
    print('flows', nflows, 'mails', nmails, 'rebuilt', nreb, 'blackhat', nbh, 'bytes', len(doc))

main()
