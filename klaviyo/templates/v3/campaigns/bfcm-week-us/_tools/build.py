"""BFCM-week US (27 nov t/m 4 dec 2026): bouwt de 4 campagnemails uit een vaste opmaak plus copy en beelden per map.

Gebruik:
    python3 -I klaviyo/templates/v3/campaigns/bfcm-week-us/_tools/build.py            # alle mappen
    python3 -I .../_tools/build.py m2-abandoners-sat                                   # een map
    node .../_tools/render.js                                                          # preview.png per map

Uitvoer per map: email.html (m3: email-a.html en email-b.html) = de Klaviyo-versie (met Klaviyo-tags).
Plus _tools/.preview/<map>[-a|-b].html (tags opgelost) voor render.js -> <map>/preview[-a|-b].png.

Bronnen per map (ontbreekt iets, dan een duidelijk gemarkeerde [PLACEHOLDER]):
  <map>/copy.md            copy-agent. Formaat zoals op 22 nov geleverd: '## Subject lines' (A/B-blok, A = gekozen),
                           '## Preview text', '## Red top banner', '## Hero' (- LABEL:, - Line1|Line2:, - Subline:,
                           - Offer bar:), '## Body' met '### Block N · Opener|Product|Proof|Gifts|What doesn't end|CTA',
                           '### P.S.'. Varianten in m3: regels met [A] of [B] (een vet [B]-kopje neemt de regels
                           eronder mee tot de volgende lege regel). '[VRAAG FLORIS...]' wordt nooit gerenderd.
  <map>/images/README.md   image-agent. Elke regel met een https-URL telt; de plek is het eerste trefwoord in die regel
                           (hero / deal|set|12-p / pizza|steel). Regels met 'variant a|b' of 'email-a|b' alleen voor die variant.
  shared/images/README.md  gedeelde textuur (achtergrond van het gifts-blok).
Opmaak (600 px, tabellen, donker, Homestead-stijl):
  1 rode aankondigingsbalk  2 vaste header (donkere variant van partials/header.html, witte lockup)
  3 hero: beeld, label, schreefkop (live tekst), subline, aanbodbalk, rode knop, friction
  4 opener van Benjamin  5 deal 12-Pcs (+ code-blok in m3-B)  6 pizza steel  7 5 gifts (rijen, M2 compact)
  8 bewijs: review, Light Labs, (M4: two promises), vier cijfers, '30-day returns. 100,000+ happy customers.'
  9 slot: knop, friction, slotregel, Benjamin, P.S.  10 vaste footer (partials/footer.html)
Controles (build stopt): geen em dash, nooit 'purifier', nooit '4 gifts', geen [VRAAG, elke siraatskitchen-link met
utm_source=klaviyo&utm_medium=email&utm_campaign=bfcm-week-us-<map> (+ utm_content per blok).
"""
import html, os, re, sys

T = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(T)
REPO = os.path.abspath(os.path.join(C, '..', '..', '..', '..', '..'))
P = os.path.join(REPO, 'klaviyo', 'templates', 'partials')
PREV = os.path.join(T, '.preview')
CAMPAIGN = 'bfcm-week-us'


def urls(path):
    d = {}
    for l in open(path):
        p = l.split()
        if len(p) == 2: d[p[0]] = p[1]
    return d


SHARED = urls(os.path.join(P, 'shared', 'klaviyo-urls.txt'))
ASSETS = urls(os.path.join(P, 'assets', 'klaviyo-urls.txt'))
# gifts5-cookbook (urgency-1108/_tools/shared-urls.txt); md5 gelijk aan partials/shared/gift-cookbook.jpg
SHARED['gift-cookbook.jpg'] = 'https://cdn.klaviyomail.com/company/TdtTzz/images/dabf0446-a5d7-49ae-87f8-672e5692bf5b.jpeg'

# ---------------------------------------------------------------- vaste feiten (BRIEF.md, DECISIONS.md, Shopify 22 nov)
SITE = 'https://siraatskitchen.com'
U_SET = SITE + '/products/titanium-hammered-cookware-set-12-pcs-free-pizza-steel-1'  # bundel met gratis Pizza Steel, $649 / $2,047 (Floris 22 nov)
U_STEEL = SITE + '/products/titanium-hammered-pizza-steel'
U_SALE = SITE + '/collections/black-friday-sale'
U_LAB = SITE + '/pages/third-party-testing'
U_WARRANTY = SITE + '/pages/warranty'
IMG_SET = 'https://cdn.klaviyomail.com/company/TdtTzz/images/0736e895-5f4b-42d5-b84b-2a6b9380f4ed.jpeg'  # BF-W1 a-top12.jpg, 1200x760, op zwart
IMG_STEEL = ('https://cdn.shopify.com/s/files/1/0907/0877/1156/files/SK_PIZZA_LIFE_05_2048_031126.jpg'
             '?v=1793715479&width=1200&height=640&crop=center')                                          # Shopify-productfoto, uitsnede 15:8
GIFTS = [  # beeld, waarde (US, BRIEF), naam. Cookbook zonder bedrag in de brief.
    ('gift-shipping.jpg', '$15 value', 'Free shipping'),
    ('gift-mystery.jpg', '$35 value', 'A mystery gift'),
    ('gift-ebook.jpg', '$30 value', 'The Plastic-Free Cooking e-book'),
    ('gift-cookbook.jpg', '$25 value', 'The Favorites Cookbook e-book'),
    ('gift-filter.jpg', '$450 value', 'A chance to win a PFAS water filter'),
]

# ---------------------------------------------------------------- kleuren en letters
BLACK = '#000000'; PANEL = '#302E2F'; RED = '#C9252C'; YEL = '#FFB800'; PINK = '#FF6B70'
WHITE = '#FFFFFF'; TXT = '#E8E5E0'; MUTED = '#A8A39B'; LINE = '#3A3838'; HEAD = '#282828'; TEX_BG = '#111110'
SERIF = "'Instrument Serif','Times New Roman',Times,serif"
SANS = 'Inter,Arial,Helvetica,sans-serif'

# ---------------------------------------------------------------- standaard (placeholders tot copy.md er is)
PH = '[PLACEHOLDER] '
BASE = dict(
    subject=PH + 'subject line', preview=PH + 'preview text, about 80 characters.',
    banner='5 FREE gifts with every order + a FREE Pizza Steel with the 12-piece set',
    label='BLACK FRIDAY', headline=PH.strip() + '|Up to 70% off', subline=PH + 'One short sentence under the headline.',
    offerbar='$2,047 \u2192 $649 \u00b7 FREE PIZZA STEEL \u00b7 5 FREE GIFTS',
    opener=[], desc=[PH + 'Product description from copy.md.'], steel_line='Only with the 12-piece set, only during the sale.',
    gifts_line='5 free gifts with every order ($555 value)', code=None,
    cta='Get the 12-piece set', cta_url=U_SET, friction='Free shipping from the US. 30-day returns. 100,000+ happy customers.',
    quote=None, lab='Tested free from PFAS by Light Labs, report no. 25895.', promises=None,
    gifts_head='5 free gifts with every order', gifts_style='rows', gifts_text='',
    close_pre=[], close_post=[], sign='Benjamin', sign_role='Founder, Siraat',
    pay='normal', scarcity='The current batch is almost gone.',
    ps=PH + 'P.S. One line that restates the deal. (link: %s)' % U_SALE, cta2=None,
)
MAILS = {
    'm1-buyers-bf': {'email.html': {}},
    'm2-abandoners-sat': {'email.html': dict(gifts_style='compact', pay='prominent')},
    'm3-buyers-cm': {'email-a.html': {}, 'email-b.html': {}},
    'm4-24h-left': {'email.html': {}},
}

# ---------------------------------------------------------------- copy.md
def variant_filter(txt, v):
    out, skip = [], False
    for l in txt.split('\n'):
        if skip:
            if not l.strip(): skip = False
            else: continue
        m = re.match(r'^(\s*(?:[-*]\s+)?)(\*\*)?\[(A|B)\](\*\*)?\s*', l)
        if m:
            if v is None or m.group(3).lower() != v:
                if m.group(2) and not m.group(4): skip = True  # vet kopje: regels eronder horen erbij
                continue
            l = m.group(1) + (m.group(2) or '') + l[m.end():]
        out.append(l)
    return '\n'.join(out)


def sections(txt, level):
    parts = re.split(r'(?m)^%s\s+(.*)$' % ('#' * level), txt)
    return [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts), 2)]


def nonempty(s): return [l for l in s.split('\n') if l.strip()]


def strip_bullet(l): return re.sub(r'^\s*(?:[-*+]|\d+\.)\s+', '', l).strip()


def kv(lines, key_rx):
    """'- Key: value' of 'Key: value'; lege waarde = eerste opsommingsregel eronder."""
    for i, l in enumerate(lines):
        m = re.match(r'^\s*(?:-\s+)?\**(%s)\**\s*:\s*(.*)$' % key_rx, l, re.I)
        if m:
            val = m.group(2).strip()
            if not val and i + 1 < len(lines) and re.match(r'^\s+-\s+', lines[i + 1]): val = strip_bullet(lines[i + 1])
            return val.strip('*').strip()
    return None


def paras(block):
    return [' '.join(x.strip() for x in p.split('\n')) for p in re.split(r'\n\s*\n', block.strip()) if p.strip()]


def parse_copy(path, v):
    if not os.path.exists(path): return {}
    txt = variant_filter(open(path).read(), v)
    out = {}
    sec = dict((k.lower(), b) for k, b in sections(txt, 2))
    g = lambda pre: next((b for k, b in sec.items() if k.startswith(pre)), None)
    s = g('subject')
    if s:
        ab = re.search(r'(?s)\*\*A/B%s.*?\*\*(.*?)(?=\*\*A/B|\Z)' % ((' variant ' + v.upper()) if v and 'A/B variant' in s else ''), s)
        m = re.search(r'(?m)^\s*-\s*A:\s*(.+)$', ab.group(1)) if ab else None
        if m: out['subject'] = m.group(1).strip()
    for key, pre in (('preview', 'preview'), ('banner', 'red top banner')):
        b = g(pre)
        if b and nonempty(b): out[key] = strip_bullet(nonempty(b)[0])
    h = g('hero')
    if h:
        L = h.split('\n')
        for key, rx in (('label', 'LABEL'), ('headline', r'Line1\|Line2'), ('subline', 'Subline'), ('offerbar', r'Offer bar[^:]*')):
            val = kv(L, rx)
            if val: out[key] = val
    body = g('body')
    if body:
        for name, b in sections(body, 3):
            n = name.lower()
            if 'opener' in n: out['opener'] = paras(b)
            elif 'product' in n: out.update(parse_product(b))
            elif 'proof' in n: out.update(parse_proof(b))
            elif 'gift' in n:
                ls = nonempty(b)
                if ls and all(re.match(r'^\s*\d+\.', x) for x in ls[1:]) and len(ls) > 1: out['gifts_head'] = ls[0].rstrip(':')
                elif ls: out['gifts_text'] = ' '.join(ls)
            elif "doesn't end" in n or 'promise' in n or 'risk' in n:
                ls = nonempty(b); out['promises'] = (ls[0].rstrip(':'), [strip_bullet(x) for x in ls[1:]])
            elif 'cta' in n or 'sign' in n: out.update(parse_close(b))
    ps = next((b for k, b in sections(txt, 3) if k.lower().startswith('p.s')), None)
    if ps and nonempty(ps): out['ps'] = strip_bullet(nonempty(ps)[0])
    return out


def parse_product(b):
    o, desc, plus, buf, code = {}, [], [], [], None
    lines = b.split('\n'); i = 0
    while i < len(lines):
        l = lines[i].rstrip(); s = l.strip()
        if not s or s.startswith('(If '):
            if buf: desc.append(' '.join(buf)); buf = []
        elif re.match(r'^\*\*Titanium Hammered Cookware Set', s) or s.startswith('~~'): pass
        elif re.match(r'^\*\*[^*]*code[^*]*\*\*$', s, re.I):      # code-blok (m3-B)
            if buf: desc.append(' '.join(buf)); buf = []
            items = []
            while i + 1 < len(lines) and lines[i + 1].strip():
                i += 1; items.append(strip_bullet(lines[i]))
            code = (s.strip('*'), items)
        elif s.startswith('+ '): plus.append(s[2:])
        elif re.match(r'^(Button|Friction reducer)\s*:', s, re.I):
            key = 'cta' if s.lower().startswith('button') else 'friction'
            val = kv([s], 'Button|Friction reducer') or ''
            if not val and i + 1 < len(lines) and re.match(r'^\s*-\s+', lines[i + 1]):
                i += 1; val = strip_bullet(lines[i]).strip('*').strip()
            if buf: desc.append(' '.join(buf)); buf = []
            o[key] = val
        else: buf.append(s)
        i += 1
    if buf: desc.append(' '.join(buf))
    o['desc'] = desc; o['code'] = code
    for p in plus:
        if re.search(r'pizza steel', p, re.I): o['steel_line'] = p
        elif re.search(r'gift', p, re.I): o['gifts_line'] = p
    return o


def parse_proof(b):
    o, rest = {}, []
    for l in nonempty(b):
        m = re.match(r'^\s*-\s*q\d\s*\(R\d+\s+([^)]+)\)\s*:\s*["\u201c](.+?)["\u201d]\s*$', l)
        if m: o['quote'] = (m.group(2), m.group(1)); continue
        rest.append(l.strip())
    if rest: o['lab'] = ' '.join(rest)
    return o


def parse_close(b):
    o, pre, post, seen, buf = {}, [], [], False, []
    def flush():
        if buf: (post if seen else pre).append(' '.join(buf)); buf.clear()
    for l in b.split('\n'):
        x = l.strip()
        if not x: flush(); continue
        if re.match(r'^Button\s*:', x, re.I):
            flush(); v = kv([x], 'Button') or ''
            if not v.lower().startswith('same'): o['cta2'] = v
            seen = True
        elif re.match(r'^Friction reducer\s*:', x, re.I): flush(); seen = True
        elif re.match(r'^(Benjamin|Founder, Siraat)$', x): flush()
        else: buf.append(x)
    flush()
    o['close_pre'], o['close_post'] = pre, post
    return o


# ---------------------------------------------------------------- images/README.md
SLOTS = [('hero', r'\bhero\b'), ('deal', r'\b(deal|12.?p(c|ie)\w*|set12|product block)\b'), ('steel', r'\b(pizza|steel)\b')]


def parse_images(path, v):
    if not os.path.exists(path): return {}
    out = {}
    for l in open(path):
        u = re.search(r'https://[^\s)|>"\'`]+', l)
        if not u or 'invalid' in u.group(0): continue
        low = l.lower()
        tag = re.search(r'\b(?:variant|var\.?)\s*([ab])\b|email-([ab])', low)
        if v and tag and v not in tag.groups(): continue
        for slot, rx in SLOTS:
            if slot not in out and re.search(rx, low): out[slot] = u.group(0); break
    return out


def shared_texture():
    p = os.path.join(C, 'shared', 'images', 'README.md')
    if not os.path.exists(p): return None
    for l in open(p):
        if 'texture' in l.lower():
            u = re.search(r'https://cdn\.klaviyomail\.com[^\s)|]+', l)
            if u: return u.group(0)
    return None


# ---------------------------------------------------------------- tekst naar html
def esc(s): return html.escape(s, quote=False)


def utm(url, mp, block):
    if not url.startswith(SITE) or 'utm_' in url: return url
    return url + ('&' if '?' in url else '?') + 'utm_source=klaviyo&utm_medium=email&utm_campaign=%s-%s&utm_content=%s' % (CAMPAIGN, mp, block)


def link(text, url, color=WHITE):
    return '<a href="%s" style="color:%s;text-decoration:underline;">%s</a>' % (url, color, text)


def md(s, mp, block, strong=WHITE):
    """Markdown-inline naar html. '(link: URL)' maakt van de zin ervoor een link; 'report no. 25895' linkt naar het labrapport."""
    s = re.sub(r'\s*\[VRAAG FLORIS[^\]]*\]', '', s)
    url = None
    m = re.search(r'\s*\(link:\s*(\S+?)\)\s*$', s)
    if m: url, s = m.group(1), s[:m.start()]
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<span style="font-weight:600;color:%s;">\1</span>' % strong, s)
    s = re.sub(r'~~(.+?)~~', r'<span style="text-decoration:line-through;">\1</span>', s)
    s = s.replace('\u2192', '&rarr;')
    if url:
        u = utm(url, mp, block)
        ends = [m.end() for m in re.finditer(r'(?<!\bno)[.?!]\s+(?=[A-Z])', s[:-2])]
        s = s[:ends[-1]] + link(s[ends[-1]:], u, strong) if ends else link(s, u, strong)
    elif 'third-party-testing' not in s:
        s = re.sub(r'(?i)(report no\. 25895)', lambda x: link(x.group(1), utm(U_LAB, mp, block + '-report'), strong), s)
    return s


# ---------------------------------------------------------------- bouwstenen
def row(inner, bg=BLACK, pad='0', cls='', align=''):
    c = ' class="%s"' % cls if cls else ''
    a = ' align="%s"' % align if align else ''
    return '<tr><td%s%s bgcolor="%s" style="background-color:%s;padding:%s;">%s</td></tr>\n' % (c, a, bg, bg, pad, inner)


def gap(n): return '<div style="height:%dpx;line-height:%dpx;font-size:0;">&nbsp;</div>' % (n, n)


def button(label, url, w=360):
    return ('<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" class="btnw" style="margin:0 auto;width:%dpx;">'
            '<tr><td align="center" bgcolor="%s" style="background-color:%s;border-radius:4px;">'
            '<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="%s" style="height:54px;v-text-anchor:middle;width:%dpx;" arcsize="8%%" stroke="f" fillcolor="%s"><center style="color:#FFFFFF;font-family:Arial,sans-serif;font-size:15px;font-weight:bold;letter-spacing:1px;">%s</center></v:roundrect><![endif]-->'
            '<!--[if !mso]><!--><a href="%s" class="tw" style="display:block;padding:18px 18px;font-family:%s;font-size:15px;line-height:20px;font-weight:600;letter-spacing:1.2px;color:#FFFFFF;text-decoration:none;text-transform:uppercase;border-radius:4px;">%s</a><!--<![endif]-->'
            '</td></tr></table>') % (w, RED, RED, url, w, RED, esc(label.upper()), url, SANS, esc(label))


def img(url, href, alt, w=600):
    return ('<a href="%s" style="display:block;border:0;"><img src="%s" width="%d" alt="%s" style="display:block;width:100%%;max-width:%dpx;height:auto;border:0;"></a>'
            % (href, url, w, html.escape(alt), w))


def eyebrow(t, color=MUTED):
    return '<div style="font-family:%s;font-size:12px;line-height:18px;font-weight:600;letter-spacing:2px;color:%s;text-transform:uppercase;">%s</div>' % (SANS, color, esc(t))


def serif(t, size=50, lh=54, color=WHITE, cls='h1'):
    t = '<br>'.join(esc(x.strip()) for x in t.split('|'))
    return ('<div class="%s tw" style="font-family:%s;font-style:italic;font-weight:400;font-size:%dpx;line-height:%dpx;letter-spacing:-0.3px;color:%s;">%s</div>'
            % (cls, SERIF, size, lh, color, t))


def sub(t, color=MUTED):
    return '<div class="fr" style="font-family:%s;font-size:12px;line-height:18px;color:%s;">%s</div>' % (SANS, color, esc(t))


def para(html_text, color=TXT, size=16, lh=26, mb=16, align='left'):
    return '<p class="bp" style="margin:0 0 %dpx 0;font-family:%s;font-size:%dpx;line-height:%dpx;color:%s;text-align:%s;">%s</p>' % (mb, SANS, size, lh, color, align, html_text)


PAYLINE = 'Pay over time with Affirm or Shop Pay.'  # Floris 22 nov, US


def payline(big=False):
    if big:
        return ('<div style="font-family:%s;font-size:15px;line-height:22px;font-weight:600;color:%s;">%s</div>' % (SANS, WHITE, PAYLINE))
    return '<div style="font-family:%s;font-size:13px;line-height:19px;color:%s;">%s</div>' % (SANS, TXT, PAYLINE)


def rule(): return '<div style="border-top:1px solid %s;font-size:0;line-height:0;height:1px;">&nbsp;</div>' % LINE


# ---------------------------------------------------------------- secties
def s_banner(c, mp):
    return row('<a href="%s" class="tw" style="font-family:%s;font-size:13px;line-height:19px;font-weight:600;letter-spacing:0.6px;color:#FFFFFF;text-decoration:none;text-transform:uppercase;">%s&nbsp;&rarr;</a>'
               % (utm(U_SET, mp, 'banner'), SANS, re.sub(r'(?i)(12-PIECE SET|\$\d+ OFF \$\d+\+|5 FREE GIFTS)', lambda m: '<span style="white-space:nowrap;">%s</span>' % m.group(1), esc(c['banner']))), RED, '11px 20px', 'ban', 'center')


def s_header(mp):
    """Vaste header uit partials/header.html, donkere variant: zelfde opbouw en navigatie, vlak #282828 en de witte lockup
    (logo-white-dark.png = brand/logo/lockup/siraat-lockup-white-email-on-dark.png, gehost; zelfde beeld als de footer)."""
    h = open(os.path.join(P, 'header.html')).read()
    h = h.replace('style="color:#282828;', 'style="color:#F2F2F2;')
    h = h.replace('#F8F7F2', HEAD).replace('border-bottom:1px solid #ECE7DD;', 'border-bottom:1px solid %s;' % LINE)
    h = h.replace('{{SHARED}}/logo-black-cream.png', SHARED['logo-white-dark.png'])
    assert '{{' not in h and 'logo-black' not in h
    h = re.sub(r'href="(https://siraatskitchen\.com[^"]*)"', lambda m: 'href="%s"' % utm(m.group(1), mp, 'header'), h)
    return h + '\n'


def offerbar(t):
    t = esc(t).replace('\u2192', '&rarr;')
    t = re.sub(r'(\$2,047)(\s*&rarr;)', r'<span style="text-decoration:line-through;color:%s;">\1</span>\2' % MUTED, t)
    t = re.sub(r'(WAS \$2,047)', r'<span style="text-decoration:line-through;color:%s;">\1</span>' % MUTED, t)
    return ('<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" style="margin:0 auto;"><tr>'
            '<td class="ob" align="center" bgcolor="#141414" style="background-color:#141414;border:1px solid #4A4747;padding:10px 16px;font-family:%s;font-size:12px;line-height:18px;font-weight:600;letter-spacing:1.4px;color:%s;text-transform:uppercase;">%s</td></tr></table>'
            % (SANS, WHITE, t))


def s_hero(c, im, mp, tex):
    """Geen AI-beeld (Higgsfield zonder tegoed): kop als live tekst op de donkere hamerslag-textuur (shared/images), daaronder
    de echte productfoto van de 12-Pcs set op zwart (BF-W1 a-top12.jpg). Levert de image-agent later een 'hero' in
    images/README.md, dan komt die foto op de plek van de setfoto."""
    u = utm(c['cta_url'], mp, 'hero')
    txt = (eyebrow(c['label'], WHITE) + gap(14) + serif(c['headline']) + gap(14) +
           '<div class="lead" style="font-family:%s;font-size:18px;line-height:27px;color:%s;">%s</div>' % (SANS, TXT, md(c['subline'], mp, 'hero')))
    top = bg_cell('<div style="text-align:center;">%s</div>' % txt, tex, '44px 40px 40px 40px', 'pad')
    alt = 'Titanium Hammered Cookware Set, 12 pieces: 3 pans, 2 saucepans, a stock pot and 6 lids'
    pic = row(img(im.get('hero') or IMG_SET, u, alt), BLACK, '0')
    act = offerbar(c['offerbar']) + gap(26) + button(c['cta'], u) + gap(12) + sub(c['friction'])
    if c['pay'] == 'prominent': act += gap(10) + payline(True)
    return top + pic + row('<div style="text-align:center;">%s</div>' % act, BLACK, '8px 40px 40px 40px', 'pad', 'center')


def s_opener(c, mp):
    if not c['opener']: return ''
    return row(rule() + gap(32) + ''.join(para(md(p, mp, 'opener')) for p in c['opener']), BLACK, '0 40px 18px 40px', 'pad')


def s_code(c, mp):
    if not c['code']: return ''
    title, items = c['code']
    code = re.search(r'\[CODE\]|\b[A-Z0-9]{5,}\b$', title)
    head = re.sub(r':\s*\[CODE\]\s*$', '', title)
    lis = ''.join('<tr><td valign="top" style="padding:0 10px 10px 0;font-family:%s;font-size:15px;line-height:23px;color:%s;">&bull;</td>'
                  '<td style="padding:0 0 10px 0;font-family:%s;font-size:15px;line-height:23px;color:%s;">%s</td></tr>'
                  % (SANS, YEL, SANS, TXT, md(x, mp, 'code')) for x in items)
    box = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#272727" style="background-color:#272727;border:1px dashed #6A6662;">'
           '<tr><td align="center" bgcolor="#272727" style="background-color:#272727;padding:20px 20px 6px 20px;">%s%s'
           '<div class="cd" style="font-family:%s;font-size:30px;line-height:36px;font-weight:800;letter-spacing:4px;color:%s;">%s</div></td></tr>'
           '<tr><td bgcolor="#272727" style="background-color:#272727;padding:14px 22px 8px 22px;text-align:left;"><table role="presentation" cellpadding="0" cellspacing="0" border="0" style="text-align:left;">%s</table></td></tr></table>'
           % (eyebrow(head, MUTED), gap(6), SANS, WHITE, esc(code.group(0) if code else '[CODE]'), lis))
    return gap(22) + box


def s_deal(c, im, mp):
    u = utm(c['cta_url'], mp, 'deal')
    desc = ''.join(para(md(p, mp, 'deal'), TXT, 16, 25, 12, 'center') for p in c['desc'])
    steel = re.sub(r'\*\*|\s*\(.*?\)|\..*$', '', c['steel_line']).strip()
    steel = steel if 'Pizza Steel' in steel else 'FREE Titanium Hammered Pizza Steel'
    steel = esc(steel).replace('FREE', '<span style="color:%s;">FREE</span>' % PINK, 1)
    gl = md(c['gifts_line'], mp, 'deal')
    body = ('<div style="text-align:center;">'
            '<span style="display:inline-block;background-color:%s;color:#111111;font-family:%s;font-size:12px;line-height:16px;font-weight:800;letter-spacing:1.5px;padding:5px 12px;border-radius:12px;">68%% OFF</span>'
            '&nbsp;&nbsp;<span style="display:inline-block;border:1px solid %s;color:%s;font-family:%s;font-size:12px;line-height:14px;font-weight:600;letter-spacing:1.5px;padding:4px 11px;border-radius:12px;">ALMOST SOLD OUT</span>'
            '%s<div class="tw" style="font-family:%s;font-size:20px;line-height:26px;font-weight:600;color:%s;">Titanium Hammered Cookware Set, 12&nbsp;Pcs</div>'
            '<div style="padding-top:6px;font-family:%s;font-size:16px;line-height:32px;color:%s;">Regular price <span style="text-decoration:line-through;">$2,047</span>'
            '&nbsp;&nbsp;<span class="pr" style="font-size:32px;line-height:32px;font-weight:800;color:%s;vertical-align:-4px;">$649</span></div>%s%s'
            '<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" style="margin:0 auto;"><tr>'
            '<td bgcolor="%s" style="background-color:%s;border:1px solid %s;border-radius:4px;padding:10px 16px;font-family:%s;font-size:15px;line-height:21px;font-weight:600;color:%s;">+ %s</td></tr></table>'
            '%s<div style="font-family:%s;font-size:14px;line-height:20px;color:%s;">%s</div>%s</div>'
            % (YEL, SANS, PINK, PINK, SANS, gap(14), SANS, WHITE, SANS, MUTED, WHITE, gap(6) + payline(c['pay'] == 'prominent') + gap(4) + '<div style="font-family:%s;font-size:13px;line-height:19px;color:%s;">%s</div>' % (SANS, PINK, esc(c['scarcity'])) + gap(16), desc, BLACK, BLACK, RED, SANS, WHITE, steel,
               gap(10), SANS, TXT, gl, s_code(c, mp)))
    body += gap(26) + button(c['cta'], u) + gap(12) + '<div style="text-align:center;">%s</div>' % sub(c['friction'])
    pic = row(img(im['deal'], u, 'Titanium Hammered Cookware Set, 12 pieces with the Pizza Steel'), BLACK, '0') if im.get('deal') else ''
    head = row(rule() + gap(30) + '<div style="text-align:center;">%s</div>' % eyebrow('THE CYBER MONDAY DEAL' if 'CYBER' in c['label'].upper() else 'THE BLACK FRIDAY DEAL', MUTED),
               BLACK, '0 40px 10px 40px', 'pad')
    return head + pic + row(body, BLACK, '8px 40px 44px 40px', 'pad')


def s_steel(c, im, mp):
    u = utm(U_SET, mp, 'pizza-steel')
    line = c['steel_line']
    if 'Pizza Steel' not in line: line = '**FREE Titanium Hammered Pizza Steel**, a $129 value. ' + line
    if not line.rstrip().endswith('.'): line = line.rstrip() + '.'
    pic = row(img(im.get('steel') or IMG_STEEL, u, 'Titanium Hammered Pizza Steel with a fresh pizza on the dinner table'), BLACK, '0')
    txt = ('<div style="text-align:center;">%s%s<div class="lead" style="font-family:%s;font-size:17px;line-height:26px;color:%s;">%s</div></div>'
           % (eyebrow('FREE WITH THE 12-PIECE SET', PINK), gap(10), SANS, TXT, md(line, mp, 'pizza-steel')))
    return pic + row(txt, BLACK, '22px 44px 44px 44px', 'pad')


def bg_cell(inner, tex, pad, cls):
    if not tex: return row(inner, BLACK, pad, cls)
    return ('<tr><td class="%s" background="%s" bgcolor="%s" style="background-color:%s;background-image:url(\'%s\');background-size:600px auto;background-repeat:repeat;background-position:center top;padding:%s;">'
            '<!--[if gte mso 9]><v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width:600px;"><v:fill type="tile" src="%s" color="%s"/><v:textbox style="mso-fit-shape-to-text:true" inset="0,0,0,0"><![endif]-->'
            '%s<!--[if gte mso 9]></v:textbox></v:rect><![endif]--></td></tr>\n' % (cls, tex, TEX_BG, TEX_BG, tex, pad, tex, TEX_BG, inner))


def s_gifts(c, mp, tex):
    u = utm(U_SALE, mp, 'gifts')
    head = ('<div style="text-align:center;">%s%s%s</div>%s'
            % (eyebrow('$555 VALUE', MUTED), gap(10), serif(c['gifts_head'].replace('5 free gifts', '5 FREE gifts', 1).replace(' ship with', '|ship with', 1) if ' ship with' in c['gifts_head'] else c['gifts_head'].replace('5 free gifts', '5 FREE gifts', 1).replace(' with every', '|with every', 1), 40, 44, WHITE, 'h2'), gap(24)))
    if c['gifts_style'] == 'compact':
        cells = ''.join('<td class="gc" width="20%%" align="center" valign="top" style="padding:0 4px;"><a href="%s" style="text-decoration:none;">'
                        '<img src="%s" width="96" alt="%s" style="display:block;width:96px;max-width:100%%;height:auto;border:0;margin:0 auto;border-radius:4px;"></a></td>'
                        % (u, SHARED[f], html.escape(n), ) for f, v, n in GIFTS)
        inner = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>%s</tr></table>%s%s'
                 % (cells, gap(18), para(md(c['gifts_text'] or c['gifts_line'], mp, 'gifts'), TXT, 16, 25, 0, 'center')))
        return bg_cell(head + inner, tex, '40px 32px 40px 32px', 'pad')
    rows = ''
    for i, (f, val, name) in enumerate(GIFTS, 1):
        rows += ('<tr><td style="padding:0 0 8px 0;"><a href="%s" style="text-decoration:none;display:block;">'
                 '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%s" style="background-color:%s;"><tr>'
                 '<td class="gi" width="112" valign="middle" bgcolor="#FFFFFF" style="width:112px;background-color:#FFFFFF;font-size:0;line-height:0;">'
                 '<img src="%s" width="112" height="112" alt="%s" style="display:block;width:112px;height:112px;border:0;"></td>'
                 '<td class="gt" valign="middle" bgcolor="%s" style="background-color:%s;padding:14px 24px;">'
                 '<div class="gv" style="font-family:%s;font-size:12px;line-height:17px;font-weight:600;letter-spacing:1.6px;color:%s;text-transform:uppercase;">Gift %d &middot; %s</div>'
                 '<div class="gn tw" style="font-family:%s;font-size:18px;line-height:24px;font-weight:600;color:%s;padding-top:4px;">%s</div></td>'
                 '</tr></table></a></td></tr>'
                 % (u, PANEL, PANEL, SHARED[f], html.escape(name), PANEL, PANEL, SANS, MUTED, i, esc(val), SANS, WHITE, esc(name)))
    return bg_cell(head + '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % rows, tex, '40px 24px 34px 24px', 'gp')


def s_proof(c, mp):
    out = ''
    if c['quote']:
        q, name = c['quote']
        out += ('<div style="text-align:center;"><div style="font-family:Arial,Helvetica,sans-serif;font-size:18px;line-height:20px;letter-spacing:3px;color:%s;">&#9733;&#9733;&#9733;&#9733;&#9733;</div>%s%s%s'
                '<div style="font-family:%s;font-size:12px;line-height:18px;font-weight:600;letter-spacing:1.6px;color:%s;text-transform:uppercase;">%s &middot; Verified buyer</div></div>'
                % (WHITE, gap(14), serif('\u201c' + q + '\u201d', 28, 36, WHITE, 'h3'), gap(14), SANS, MUTED, esc(name)))
    if c['lab']:
        out += gap(22) + para(md(c['lab'], mp, 'proof'), TXT, 15, 24, 0, 'center')
    if c['promises']:
        title, items = c['promises']
        lis = ''.join('<tr><td valign="top" width="34" style="padding:0 0 14px 0;"><div style="width:24px;height:24px;line-height:24px;border-radius:12px;background-color:%s;text-align:center;font-family:%s;font-size:13px;font-weight:600;color:#111111;">%d</div></td>'
                      '<td style="padding:0 0 14px 0;font-family:%s;font-size:15px;line-height:23px;color:%s;">%s</td></tr>' % (WHITE, SANS, i, SANS, TXT, md(x, mp, 'promises')) for i, x in enumerate(items, 1))
        out += (gap(32) + '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%s" style="background-color:%s;"><tr><td style="padding:24px 24px 10px 24px;">'
                '%s%s<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table></td></tr></table>'
                % (PANEL, PANEL, serif(title, 28, 34, WHITE, 'h3'), gap(16), lis))
    stats = [('No. 25895', 'Light Labs report', utm(U_LAB, mp, 'proof-lab')), ('75-year', 'Warranty', utm(U_WARRANTY, mp, 'proof-warranty')),
             ]

    def cell(a, b, u, first):
        return ('<td width="50%%" align="center" valign="top" style="padding:18px 4px;border-left:%s;">'
                '<a href="%s" style="text-decoration:none;"><div class="pv tw" style="font-family:%s;font-size:22px;line-height:26px;font-weight:800;color:%s;">%s</div>'
                '<div style="font-family:%s;font-size:11px;line-height:16px;font-weight:600;letter-spacing:1.6px;color:%s;text-transform:uppercase;padding-top:4px;">%s</div></a></td>'
                % ('0' if first else '1px solid %s' % LINE, u, SANS, WHITE, a, SANS, MUTED, esc(b)))

    def half(a, b, k):
        return ('<!--[if mso]><td width="520" valign="top"><![endif]--><div class="%s" style="display:inline-block;width:100%%;max-width:520px;vertical-align:top;">'
                '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>%s%s</tr></table></div><!--[if mso]></td><![endif]-->'
                % (k, cell(*a, True), cell(*b, False)))
    grid = ('<div style="font-size:0;text-align:center;border-top:1px solid %s;border-bottom:1px solid %s;">'
            '<!--[if mso]><table role="presentation" width="520" cellpadding="0" cellspacing="0" border="0"><tr><![endif]-->%s%s<!--[if mso]></tr></table><![endif]--></div>'
            % (LINE, LINE, half(stats[0], stats[1], 'hf'), ''))
    out += gap(36) + grid + gap(36) + '<div style="text-align:center;">%s</div>' % serif('30-day returns.|100,000+ happy customers.', 40, 46, WHITE, 'h2')
    return row(out, BLACK, '44px 40px 40px 40px', 'pad')


def s_close(c, mp):
    u = utm(c['cta_url'], mp, 'cta2')
    out = ''.join(para(md(p, mp, 'close')) for p in c['close_pre'])
    out += gap(8) + button(c['cta2'] or c['cta'], u) + gap(12) + '<div style="text-align:center;">%s</div>' % sub(c['friction'])
    if c['pay'] == 'prominent': out += gap(8) + '<div style="text-align:center;">%s</div>' % payline()
    out += gap(32)
    out += ''.join(para(md(p, mp, 'close')) for p in c['close_post'])
    out += ('<p style="margin:4px 0 0 0;font-family:%s;font-size:16px;line-height:24px;color:%s;"><span style="font-weight:600;color:%s;">%s</span><br>'
            '<span style="color:%s;font-size:14px;">%s</span></p>' % (SANS, TXT, WHITE, esc(c['sign']), MUTED, esc(c['sign_role'])))
    if c.get('ps'):
        out += gap(22) + para(md(c['ps'], mp, 'ps', TXT), MUTED, 15, 24, 0)
    return row(rule() + gap(34) + out, BLACK, '0 40px 50px 40px', 'pad')


def s_footer(mp):
    f = open(os.path.join(P, 'footer.html')).read()
    f = f.replace('{{SHARED}}/logo-white-dark.png', SHARED['logo-white-dark.png'])
    f = f.replace('{{IMG}}/fb.png', ASSETS['fb.png']).replace('{{IMG}}/ig.png', ASSETS['ig.png'])
    # contrast: in de partial staan afmelden/voorkeuren/webweergave op #111111 op #282828 (onleesbaar); hier #BDB8B0
    f = f.replace('style="color:#111111;"', 'style="color:#BDB8B0;"')
    assert '{{SHARED}}' not in f and '{{IMG}}' not in f
    f = re.sub(r'href="(https://siraatskitchen\.com[^"]*)"', lambda m: 'href="%s"' % utm(m.group(1), mp, 'footer'), f)
    return f + '\n'


HEADCSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Instrument+Serif:ital@0;1&display=swap');
:root{color-scheme:light only;supported-color-schemes:light only;}
body{margin:0;padding:0;background:#000000;-webkit-text-size-adjust:100%;}
table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}
img{border:0;display:block;line-height:100%;outline:none;text-decoration:none;}
@media only screen and (max-width:599px){
  .w{width:100%!important;}
  .pad{padding-left:20px!important;padding-right:20px!important;}
  .gp{padding-left:12px!important;padding-right:12px!important;}
  .navhide{display:none!important;}
  .h1{font-size:42px!important;line-height:46px!important;}
  .h2{font-size:32px!important;line-height:37px!important;}
  .h3{font-size:24px!important;line-height:31px!important;}
  .lead{font-size:16px!important;line-height:25px!important;}
  .btnw{width:100%!important;}
  .ban a{font-size:12px!important;line-height:18px!important;letter-spacing:0.3px!important;}
  .ob{font-size:11px!important;letter-spacing:0.8px!important;padding:9px 10px!important;}
  .gi,.gi img{width:88px!important;height:88px!important;}
  .gt{padding:10px 14px!important;}
  .gv{font-size:11px!important;letter-spacing:1.2px!important;}
  .gn{font-size:16px!important;line-height:21px!important;}
  .gc{padding:0 2px!important;}
  .hf{max-width:100%!important;}
  .hf2{border-top:1px solid #3A3838!important;}
  .pv{font-size:20px!important;line-height:24px!important;}
  .cd{font-size:26px!important;}
}
[data-ogsc] .tw,[data-ogsb] .tw{color:#FFFFFF!important;}
</style>"""


def page(c, im, mp, tex):
    pre = esc(c['preview']) + '&#847;&zwnj;&nbsp;' * 60
    body = (s_banner(c, mp) + s_header(mp) + s_hero(c, im, mp, tex) + s_opener(c, mp) + s_deal(c, im, mp) + s_steel(c, im, mp) +
            s_gifts(c, mp, tex) + s_proof(c, mp) + s_close(c, mp) + s_footer(mp))
    return ('<!DOCTYPE html>\n<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">\n'
            '<head>\n<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="X-UA-Compatible" content="IE=edge">\n'
            '<meta name="color-scheme" content="light only"><meta name="supported-color-schemes" content="light only">\n'
            '<title>%s</title>\n<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->\n'
            '<!--[if mso]><style>body,table,td,div,p,a,span{font-family:Arial,Helvetica,sans-serif!important;}</style><![endif]-->\n%s\n</head>\n'
            '<body bgcolor="#000000" style="margin:0;padding:0;background-color:#000000;">\n'
            '<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:#000000;">%s</div>\n'
            '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#000000" style="background-color:#000000;"><tr><td align="center" bgcolor="#000000" style="background-color:#000000;">\n'
            '<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="#000000" style="width:600px;max-width:600px;background-color:#000000;">\n'
            '%s</table>\n</td></tr></table>\n</body>\n</html>\n') % (esc(c['subject']), HEADCSS, pre, body)


def check(h, name):
    vis = re.sub(r'(?s)<style.*?</style>|<!--.*?-->', '', h)
    txt = re.sub(r'<[^>]+>', ' ', vis)
    bad = []
    if '\u2014' in h or '&mdash;' in h: bad.append('em dash')
    if re.search(r'(?i)purifier', h): bad.append('purifier')
    if re.search(r'(?i)\b(4|four) (free )?gifts', txt): bad.append('4 gifts')
    if 'VRAAG' in h: bad.append('[VRAAG] in mail')
    if re.search(r'/products/titanium-hammered-cookware-set[?"]', h): bad.append('12-Pcs link zonder Pizza Steel-bundel')
    if re.search(r'(?i)\b(wok|deep pan)\b', re.sub(r'<[^>]+>', ' ', h)): bad.append('wok/deep pan in de set')
    for u in re.findall(r'href="(https://siraatskitchen\.com[^"]*)"', h):
        if 'utm_source=klaviyo&utm_medium=email&utm_campaign=%s-' % CAMPAIGN not in u: bad.append('no utm: ' + u)
    for u in re.findall(r'href="(https?://[^"]*)"', h):
        if not re.match(r'https://(siraatskitchen\.com|www\.facebook\.com|www\.instagram\.com)', u): bad.append('foreign link: ' + u)
    if bad: raise SystemExit('%s: %s' % (name, '; '.join(sorted(set(bad)))))


def preview(h):
    h = h.replace('{% unsubscribe_link %}', '#').replace('{% manage_preferences_link %}', '#').replace('{% web_view_link %}', '#')
    h = h.replace('{{ organization.name }}', "Siraat's Kitchen").replace('{{ organization.full_address }}', '[address]')
    h = re.sub(r"\{\{\s*first_name\|default:'([^']*)'\s*\}\}", r'\1', h)
    h = re.sub(r'\{%.*?%\}', '', h); h = re.sub(r'\{\{.*?\}\}', '', h)
    return h


def main(only):
    os.makedirs(PREV, exist_ok=True)
    tex = shared_texture()
    report = []
    for mp, variants in MAILS.items():
        if only and mp not in only: continue
        for fn, over in variants.items():
            v = re.search(r'email-([ab])\.html', fn); v = v.group(1) if v else None
            cp = parse_copy(os.path.join(C, mp, 'copy.md'), v)
            im = parse_images(os.path.join(C, mp, 'images', 'README.md'), v)
            c = dict(BASE); c.update(over); c.update(cp)
            h = page(c, im, mp, tex)
            check(h, mp + '/' + fn)
            open(os.path.join(C, mp, fn), 'w').write(h)
            open(os.path.join(PREV, mp + ('-' + v if v else '') + '.html'), 'w').write(preview(h))
            report.append('%-20s %-13s copy:%-3s images:%-16s %d KB  subject: %s' % (mp, fn, 'yes' if cp else 'no', ','.join(sorted(im)) or '-', len(h) // 1024, c['subject']))
    print('\n'.join(report))


if __name__ == '__main__':
    main(sys.argv[1:])
