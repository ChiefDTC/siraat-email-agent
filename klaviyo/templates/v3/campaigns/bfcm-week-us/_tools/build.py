"""BFCM-week US (27 nov t/m 4 dec 2026): bouwt de 4 campagnemails uit een vaste opmaak plus copy en beelden per map.

Gebruik (vanuit de repo of waar dan ook):
    python3 -I klaviyo/templates/v3/campaigns/bfcm-week-us/_tools/build.py            # alle mappen
    python3 -I .../_tools/build.py m2-abandoners-sat                                   # een map

Uitvoer per map: email.html (m3: email-a.html en email-b.html), de Klaviyo-versie met Klaviyo-tags.
Daarnaast _tools/.preview/<map>-<variant>.html (tags opgelost) voor render.js -> <map>/preview.png.

Bronnen per map (als ze er zijn, anders duidelijk gemarkeerde placeholders):
  <map>/copy.md           copy-agent: label, kop (regel1|regel2), subline, knop, friction, body, P.S., preview.
  <map>/images/README.md  image-agent: gehoste URL per plek (hero, deal, pizza). Elke regel met een https-URL telt;
                          de plek is het eerste trefwoord in die regel (hero / deal|set / pizza|steel).
Opmaak (600 px, tabellen, donker):
  1 rode HS-aankondigingsbalk  2 vaste header (donkere variant van partials/header.html, lockup wit)
  3 hero (beeld + live tekst)  [m3-B: extra korting-blok]  4 deal 12-Pcs  5 pizza steel  6 5 gifts (rijen)
  7 bewijs  8 body/P.S. + tweede knop  9 vaste footer (partials/footer.html)
Regels: geen em dash, nooit "purifier", nooit "4 gifts"; elke link krijgt utm_source/medium/campaign (+ utm_content).
"""
import html, os, re, sys

T = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(T)                                   # .../bfcm-week-us
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
SHARED['gift-cookbook.jpg'] = 'https://cdn.klaviyomail.com/company/TdtTzz/images/dabf0446-a5d7-49ae-87f8-672e5692bf5b.jpeg'  # gifts5 (urgency-1108/_tools/shared-urls.txt), md5 gelijk aan partials/shared/gift-cookbook.jpg

# ---------------------------------------------------------------- vaste feiten (BRIEF.md, DECISIONS.md)
SITE = 'https://siraatskitchen.com'
U_SET = SITE + '/products/titanium-hammered-cookware-set'
U_STEEL = SITE + '/products/titanium-hammered-pizza-steel'
U_SALE = SITE + '/collections/black-friday-sale'
U_LAB = SITE + '/pages/third-party-testing'
U_WARRANTY = SITE + '/pages/warranty'
# 12-Pcs productbeeld op zwart (BF-W1 a-top12.jpg, 1200x760, al in Klaviyo)
IMG_SET = 'https://cdn.klaviyomail.com/company/TdtTzz/images/0736e895-5f4b-42d5-b84b-2a6b9380f4ed.jpeg'
# Pizza Steel: officiele Shopify-productfoto (diner met pizza op de steel), uitsnede 2:1 via de Shopify-CDN
IMG_STEEL = ('https://cdn.shopify.com/s/files/1/0907/0877/1156/files/SK_PIZZA_LIFE_05_2048_031126.jpg'
             '?v=1793715479&width=1200&height=640&crop=center')
GIFTS = [  # (beeld, waardelabel, naam)  waarden US volgens BRIEF; cookbook zonder bedrag (zie open punten)
    ('gift-shipping.jpg', '$15 value', 'Free shipping'),
    ('gift-mystery.jpg', '$25 value', 'A mystery gift'),
    ('gift-ebook.jpg', '$30 value', 'The Plastic-Free Cooking e-book'),
    ('gift-cookbook.jpg', 'Included', 'The Favorites Cookbook e-book'),
    ('gift-filter.jpg', '$450 value', 'A chance to win a PFAS water filter'),
]

# ---------------------------------------------------------------- kleuren
BLACK = '#000000'; PANEL = '#302E2F'; RED = '#C9252C'; RED_DK = '#A81E24'; YEL = '#FFB800'
WHITE = '#FFFFFF'; TXT = '#E8E5E0'; MUTED = '#A8A39B'; LINE = '#3A3838'; HEAD = '#282828'
SERIF = "'Instrument Serif','Times New Roman',Times,serif"
SANS = 'Inter,Arial,Helvetica,sans-serif'

# ---------------------------------------------------------------- placeholders per mail (tot copy.md er is)
PH = '[PLACEHOLDER] '
BASE = dict(
    subject=PH + 'subject line', preview=PH + 'preview text, about 80 characters, completes the subject line.',
    banner='5 FREE gifts with every order + a FREE Pizza Steel with the 12-piece set',
    label='BLACK FRIDAY', headline='Up to 70% off', subline=PH + 'One or two sentences that carry the idea of this mail, about twenty words long.',
    cta='Get the 12-piece set', cta_url=U_SET, friction='Free shipping. 30-day returns. 100,000+ happy customers.',
    deal_label='THE BLACK FRIDAY DEAL', deal_cta='Get the 12-piece set',
    steel_line='The Titanium Hammered Pizza Steel ships free with the 12-piece set. Only during the sale.',
    gifts_head='5 FREE gifts with every order', gifts_eyebrow='$555 VALUE',
    proof_line='30-day returns.|100,000+ happy customers.',
    body=[PH + 'Body from Benjamin. Short paragraphs, plain text, no more than three. This slot holds the personal note.',
          PH + 'Second paragraph. One idea per paragraph, one bold piece at most.'],
    sign='Benjamin', sign_role='Founder, Siraat',
    ps=PH + 'P.S. One line that restates the deal or the gifts.',
    cta2='Shop the Black Friday sale', cta2_url=U_SALE, extra=None,
)
MAILS = {
    'm1-buyers-bf': {'email.html': dict(label='BLACK FRIDAY · FOR OUR CUSTOMERS', headline=PH.strip() + '|For the kitchen you started')},
    'm2-abandoners-sat': {'email.html': dict(label='A NOTE FROM BENJAMIN', headline=PH.strip() + '|Something stopped you?')},
    'm3-buyers-cm': {
        'email-a.html': dict(label='CYBER MONDAY · FOR OUR CUSTOMERS', headline=PH.strip() + '|Cyber Monday'),
        'email-b.html': dict(label='CYBER MONDAY · FOR OUR CUSTOMERS', headline=PH.strip() + '|Cyber Monday, a little extra',
                             extra=dict(eyebrow='CYBER MONDAY EXTRA', tiers=[('$50 OFF', 'orders $400+'), ('$100 OFF', 'orders $700+')],
                                        code='[CODE]', note='Use code [CODE] at checkout. On top of the sale prices.')),
    },
    'm4-24h-left': {'email.html': dict(label='24 HOURS LEFT · ENDS [END: Sat, Dec 5]', headline='24 hours left', cta2='Shop before it ends')},
}

# ---------------------------------------------------------------- copy.md en images/README.md
KEYS = [  # (sleutel, regex op het label in copy.md)
    ('subject', r'(chosen|gekozen|final|keuze)?\s*subject( line)?( \(chosen\)| \(keuze\))?'), ('preview', r'preview( text)?|preheader'),
    ('label', r'(hero )?label|eyebrow'), ('headline', r'(hero )?(headline|kop)|regel ?1 ?\| ?regel ?2'),
    ('subline', r'(hero )?sub ?line|subregel'), ('cta', r'(primary )?(button|cta|knop)( 1)?'), ('cta2', r'(second(ary)? )?(button|cta|knop) 2'),
    ('friction', r'friction( reducer)?'), ('ps', r'p\.?s\.?'), ('banner', r'banner'), ('steel_line', r'pizza steel( line)?'),
]


def md_clean(s):
    s = s.strip().strip('`').strip()
    s = re.sub(r'^\*\*(.*)\*\*$', r'\1', s); s = re.sub(r'^"(.*)"$', r'\1', s)
    return s.strip()


def parse_copy(path, variant):
    """Lenient: 'Key: value' regels (ook **Key:**, - Key:, | Key | value |) en een sectie '## Body'. Bij m3 splitst
    een kop met 'Variant A' / 'Variant B' het document; gedeelde delen gelden voor beide. Wordt in fase 2 bijgesteld
    op het echte formaat van de copy-agent."""
    if not os.path.exists(path): return {}
    txt = open(path).read()
    if variant:
        parts = re.split(r'(?im)^#{1,4}.*\bvariant\s+([ab])\b.*$', txt)
        if len(parts) > 1:
            keep = parts[0]
            for i in range(1, len(parts), 2):
                if parts[i].lower() == variant: keep += parts[i + 1]
            txt = keep
    out = {}
    lines = txt.split('\n')
    for l in lines:
        m = re.match(r'^\s*(?:[-*]\s*)?(?:\|\s*)?\**([A-Za-z .()|0-9/]+?)\**\s*(?::\**|\|)\s*(.+?)\s*\|?\s*$', l)
        if not m: continue
        k, v = m.group(1).strip().lower(), md_clean(m.group(2))
        for key, rx in KEYS:
            if key not in out and re.fullmatch(rx, k) and v: out[key] = v; break
    m = re.search(r'(?ims)^#{1,4}\s*(body|tekst|text)\b.*?$(.*?)(?=^#{1,4}\s|\Z)', txt)
    if m:
        paras = [md_clean(p.replace('\n', ' ')) for p in re.split(r'\n\s*\n', m.group(2)) if p.strip()]
        paras = [p for p in paras if not re.match(r'(?i)^(p\.?s\.?|benjamin\b)', p)]
        if paras: out['body'] = paras
    return out


SLOTS = [('hero', r'\bhero\b'), ('deal', r'\b(deal|12.?p(c|ie)|set)\b'), ('steel', r'\b(pizza|steel)\b')]


def parse_images(path, variant):
    if not os.path.exists(path): return {}
    out = {}
    for l in open(path):
        u = re.search(r'https://[^\s)|>"\']+', l)
        if not u or 'invalid' in u.group(0): continue
        low = l.lower()
        if variant and re.search(r'\b(variant|var\.?)\s*[ab]\b|email-[ab]', low) and not re.search(r'\b(variant|var\.?)\s*%s\b|email-%s' % (variant, variant), low): continue
        for slot, rx in SLOTS:
            if slot not in out and re.search(rx, low): out[slot] = u.group(0); break
    return out


# ---------------------------------------------------------------- bouwstenen
def esc(s): return html.escape(s, quote=False).replace('’', '&rsquo;')


def utm(url, mp, block):
    if not url.startswith(SITE) or 'utm_' in url: return url
    return url + ('&' if '?' in url else '?') + 'utm_source=klaviyo&utm_medium=email&utm_campaign=%s-%s&utm_content=%s' % (CAMPAIGN, mp, block)


def row(inner, bg=BLACK, pad='0', cls=''):
    c = ' class="%s"' % cls if cls else ''
    return '<tr><td%s bgcolor="%s" style="background-color:%s;padding:%s;">%s</td></tr>\n' % (c, bg, bg, pad, inner)


def button(label, url, w=340, color=RED):
    return ('<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" class="btnw" style="margin:0 auto;width:%dpx;">'
            '<tr><td align="center" bgcolor="%s" style="background-color:%s;border-radius:4px;">'
            '<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="%s" style="height:54px;v-text-anchor:middle;width:%dpx;" arcsize="8%%" stroke="f" fillcolor="%s"><center style="color:#FFFFFF;font-family:Arial,sans-serif;font-size:15px;font-weight:bold;letter-spacing:1px;">%s</center></v:roundrect><![endif]-->'
            '<!--[if !mso]><!--><a href="%s" class="tw" style="display:block;padding:18px 20px;font-family:%s;font-size:15px;line-height:18px;font-weight:600;letter-spacing:1.2px;color:#FFFFFF;text-decoration:none;text-transform:uppercase;border-radius:4px;">%s</a><!--<![endif]-->'
            '</td></tr></table>') % (w, color, color, url, w, color, esc(label.upper()), url, SANS, esc(label))


def img(url, link, alt, w=600):
    return ('<a href="%s" style="display:block;border:0;"><img src="%s" width="%d" alt="%s" style="display:block;width:100%%;max-width:%dpx;height:auto;border:0;"></a>'
            % (link, url, w, html.escape(alt), w))


def eyebrow(t, color=MUTED):
    return '<div style="font-family:%s;font-size:12px;line-height:18px;font-weight:600;letter-spacing:2px;color:%s;text-transform:uppercase;">%s</div>' % (SANS, color, esc(t))


def serif(t, size=50, lh=54, color=WHITE, cls='h1'):
    t = '<br>'.join(esc(x.strip()) for x in t.split('|'))
    return ('<div class="%s tw" style="font-family:%s;font-style:italic;font-weight:400;font-size:%dpx;line-height:%dpx;letter-spacing:-0.5px;color:%s;">%s</div>'
            % (cls, SERIF, size, lh, color, t))


def sub(t, color=MUTED, size=12, lh=18):
    return '<div style="font-family:%s;font-size:%dpx;line-height:%dpx;color:%s;">%s</div>' % (SANS, size, lh, color, esc(t))


# ---------------------------------------------------------------- secties
def s_banner(c, mp):
    u = utm(U_SET, mp, 'banner')
    return row('<a href="%s" class="tw" style="font-family:%s;font-size:14px;line-height:20px;font-weight:600;color:#FFFFFF;text-decoration:none;">%s&nbsp;&rarr;</a>'
               % (u, SANS, esc(c['banner'])), RED, '11px 20px', 'ban').replace('<td class="ban"', '<td class="ban" align="center"')


def s_header(mp):
    """Vaste header uit partials/header.html, donkere variant: zelfde opbouw en links, vlak #282828 en de witte lockup
    (logo-white-dark.png = brand/logo/lockup/siraat-lockup-white-email-on-dark.png, gehost; zelfde beeld als in de footer)."""
    h = open(os.path.join(P, 'header.html')).read()
    h = h.replace('#F8F7F2', HEAD).replace('border-bottom:1px solid #ECE7DD;', 'border-bottom:1px solid %s;' % LINE)
    h = h.replace('{{SHARED}}/logo-black-cream.png', SHARED['logo-white-dark.png']).replace('color:#282828;', 'color:#F2F2F2;')
    assert '{{' not in h and 'logo-black' not in h
    h = re.sub(r'href="(https://siraatskitchen\.com[^"]*)"', lambda m: 'href="%s"' % utm(m.group(1), mp, 'header'), h)
    return h + '\n'


def s_hero(c, im, mp):
    u = utm(c['cta_url'], mp, 'hero')
    if im.get('hero'):
        pic = row(img(im['hero'], u, re.sub(r'\[.*?\]\s*', '', c['headline'].replace('|', ' '))), BLACK, '0', 'fz')
    else:
        pic = row('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>'
                  '<td align="center" valign="middle" height="400" bgcolor="#161616" style="height:400px;background-color:#161616;border:2px dashed #4A4747;'
                  'font-family:%s;font-size:13px;line-height:20px;letter-spacing:2px;font-weight:600;color:#7A7570;">[PLACEHOLDER] HERO IMAGE<br>'
                  '1200 x 800, dark Black Friday photo, no text in the image<br>from images/README.md (image agent)</td></tr></table>' % SANS, BLACK, '0')
    txt = (eyebrow(c['label'], WHITE) + '<div style="height:14px;line-height:14px;font-size:0;">&nbsp;</div>' + serif(c['headline']) +
           '<div style="height:16px;line-height:16px;font-size:0;">&nbsp;</div>' +
           '<div class="lead" style="font-family:%s;font-size:17px;line-height:27px;color:%s;">%s</div>' % (SANS, TXT, esc(c['subline'])) +
           '<div style="height:28px;line-height:28px;font-size:0;">&nbsp;</div>' + button(c['cta'], u) +
           '<div style="height:12px;line-height:12px;font-size:0;">&nbsp;</div>' + sub(c['friction']))
    return pic + row('<div style="text-align:center;">%s</div>' % txt, BLACK, '36px 40px 44px 40px', 'pad').replace('<td class="pad"', '<td class="pad" align="center"')


def s_extra(c, mp):
    e = c.get('extra')
    if not e: return ''
    cells = ''.join('<td class="ex" width="50%%" align="center" bgcolor="%s" style="background-color:%s;padding:16px 8px;border-left:%s;">'
                    '<div style="font-family:%s;font-size:28px;line-height:32px;font-weight:800;color:%s;">%s</div>'
                    '<div style="font-family:%s;font-size:13px;line-height:18px;color:%s;padding-top:4px;">%s</div></td>'
                    % (BLACK, BLACK, ('1px solid %s' % LINE) if i else '0', SANS, YEL, esc(a), SANS, TXT, esc(b)) for i, (a, b) in enumerate(e['tiers']))
    box = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%s" style="background-color:%s;border:1px dashed %s;">'
           '<tr><td colspan="2" align="center" bgcolor="%s" style="background-color:%s;padding:18px 16px 4px 16px;">%s</td></tr><tr>%s</tr>'
           '<tr><td colspan="2" align="center" bgcolor="%s" style="background-color:%s;padding:4px 16px 18px 16px;">'
           '<div style="font-family:%s;font-size:14px;line-height:20px;color:%s;">%s</div></td></tr></table>'
           % (BLACK, BLACK, MUTED, BLACK, BLACK, eyebrow(e['eyebrow'], WHITE), cells, BLACK, BLACK, SANS, TXT, esc(e['note'])))
    return row(box, BLACK, '0 40px 40px 40px', 'pad')


def s_deal(c, im, mp):
    u = utm(U_SET, mp, 'deal')
    top = row('<div style="border-top:1px solid %s;font-size:0;line-height:0;height:1px;">&nbsp;</div>' % LINE, BLACK, '0 40px', 'pad')
    head = row('<div style="text-align:center;">%s<div style="height:10px;line-height:10px;font-size:0;">&nbsp;</div>%s</div>'
               % (eyebrow(c['deal_label'], MUTED), serif('The 12-piece set|at 68% off', 40, 44, WHITE, 'h2')), BLACK, '40px 40px 8px 40px', 'pad')
    pic = row(img(im.get('deal') or IMG_SET, u, 'Titanium Hammered Cookware Set, 12 pieces: 3 pans, 3 pots and 6 lids'), BLACK, '0', 'fz')
    price = ('<div style="text-align:center;">'
             '<span style="display:inline-block;background-color:%s;color:#111111;font-family:%s;font-size:12px;line-height:16px;font-weight:800;letter-spacing:1.5px;padding:5px 12px;border-radius:12px;">68%% OFF</span>'
             '<div style="height:14px;line-height:14px;font-size:0;">&nbsp;</div>'
             '<div class="tw" style="font-family:%s;font-size:20px;line-height:26px;font-weight:600;color:%s;">Titanium Hammered Cookware Set, 12&nbsp;Pcs</div>'
             '<div style="padding-top:8px;font-family:%s;font-size:17px;line-height:30px;color:%s;">Regular price <span style="text-decoration:line-through;">$2,047</span>'
             '&nbsp;&nbsp;<span class="pr" style="font-size:30px;line-height:30px;font-weight:800;color:%s;vertical-align:-3px;">$649</span></div>'
             '<div style="padding-top:6px;font-family:%s;font-size:14px;line-height:20px;color:%s;">3 pans, 3 pots, 6 lids</div>'
             '<div style="height:16px;line-height:16px;font-size:0;">&nbsp;</div>'
             '<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" style="margin:0 auto;"><tr>'
             '<td bgcolor="%s" style="background-color:%s;border:1px solid %s;border-radius:4px;padding:10px 16px;font-family:%s;font-size:15px;line-height:21px;font-weight:600;color:%s;">'
             '+ <span style="color:#FF5A60;">FREE</span> Titanium Hammered Pizza Steel</td></tr></table>'
             '<div style="height:26px;line-height:26px;font-size:0;">&nbsp;</div>%s'
             '<div style="height:12px;line-height:12px;font-size:0;">&nbsp;</div>%s</div>'
             % (YEL, SANS, SANS, WHITE, SANS, MUTED, WHITE, SANS, MUTED, BLACK, BLACK, RED, SANS, WHITE,
                button(c['deal_cta'], u), sub(c['friction'])))
    return top + head + pic + row(price, BLACK, '20px 40px 44px 40px', 'pad')


def s_steel(c, im, mp):
    u = utm(U_SET, mp, 'pizza-steel')
    pic = row(img(im.get('steel') or IMG_STEEL, u, 'Titanium Hammered Pizza Steel with a pizza on the dinner table'), BLACK, '0 0 0 0', 'fz')
    txt = ('<div style="text-align:center;">%s<div style="height:10px;line-height:10px;font-size:0;">&nbsp;</div>'
           '<div class="lead" style="font-family:%s;font-size:17px;line-height:27px;color:%s;">%s</div></div>'
           % (eyebrow('FREE WITH THE 12-PIECE SET', '#FF5A60'), SANS, TXT, esc(c['steel_line'])))
    return pic + row(txt, BLACK, '22px 48px 44px 48px', 'pad')


def s_gifts(c, mp):
    u = utm(U_SALE, mp, 'gifts')
    head = row('<div style="text-align:center;">%s<div style="height:10px;line-height:10px;font-size:0;">&nbsp;</div>%s</div>'
               % (eyebrow(c['gifts_eyebrow'], MUTED), serif(c['gifts_head'], 40, 44, WHITE, 'h2')), BLACK, '0 40px 24px 40px', 'pad')
    rows = ''
    for i, (f, val, name) in enumerate(GIFTS, 1):
        rows += ('<tr><td style="padding:0 0 8px 0;"><a href="%s" style="text-decoration:none;display:block;">'
                 '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%s" style="background-color:%s;"><tr>'
                 '<td class="gi" width="120" valign="middle" bgcolor="#FFFFFF" style="width:120px;background-color:#FFFFFF;font-size:0;line-height:0;">'
                 '<img src="%s" width="120" height="120" alt="%s" style="display:block;width:120px;height:120px;border:0;"></td>'
                 '<td class="gt" valign="middle" bgcolor="%s" style="background-color:%s;padding:14px 24px;">'
                 '<div style="font-family:%s;font-size:13px;line-height:18px;font-weight:600;letter-spacing:1.6px;color:%s;text-transform:uppercase;">Gift %d &middot; %s</div>'
                 '<div class="gn tw" style="font-family:%s;font-size:18px;line-height:24px;font-weight:600;color:%s;padding-top:4px;">%s</div></td>'
                 '</tr></table></a></td></tr>'
                 % (u, PANEL, PANEL, SHARED[f], html.escape(name), PANEL, PANEL, SANS, MUTED, i, esc(val), SANS, WHITE, esc(name)))
    box = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % rows
    return head + row(box, BLACK, '0 24px 36px 24px', 'gp')


def s_proof(c, mp):
    stats = [('No. 25895', 'Light Labs report', utm(U_LAB, mp, 'proof-lab')), ('75-year', 'Warranty', utm(U_WARRANTY, mp, 'proof-warranty')),
             ('30-day', 'Returns', utm(U_SALE, mp, 'proof-returns')), ('100,000+', 'Happy customers', utm(U_SALE, mp, 'proof-customers'))]

    def cell(a, b, u, first):
        return ('<td width="50%%" align="center" valign="top" bgcolor="%s" style="background-color:%s;padding:18px 4px;border-left:%s;">'
                '<a href="%s" style="text-decoration:none;"><div class="pv tw" style="font-family:%s;font-size:22px;line-height:26px;font-weight:800;color:%s;">%s</div>'
                '<div style="font-family:%s;font-size:11px;line-height:16px;font-weight:600;letter-spacing:1.6px;color:%s;text-transform:uppercase;padding-top:4px;">%s</div></a></td>'
                % (BLACK, BLACK, '0' if first else '1px solid %s' % LINE, u, SANS, WHITE, a, SANS, MUTED, esc(b)))
    half = lambda a, b, k='hf': ('<!--[if mso]><td width="260" valign="top"><![endif]--><div class="%s" style="display:inline-block;width:100%%;max-width:260px;vertical-align:top;">'
                         '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>%s%s</tr></table></div><!--[if mso]></td><![endif]-->'
                         % (k, cell(*a, True), cell(*b, False)))
    grid = ('<div style="font-size:0;text-align:center;border-top:1px solid %s;border-bottom:1px solid %s;">'
            '<!--[if mso]><table role="presentation" width="520" cellpadding="0" cellspacing="0" border="0"><tr><![endif]-->%s%s<!--[if mso]></tr></table><![endif]--></div>'
            % (LINE, LINE, half(stats[0], stats[1]), half(stats[2], stats[3], 'hf hf2')))
    big = '<div style="text-align:center;padding-top:40px;">%s</div>' % serif(c['proof_line'], 40, 46, WHITE, 'h2')
    return row(grid + big, BLACK, '0 40px 40px 40px', 'pad')


def s_body(c, mp):
    ps = ''.join('<p style="margin:0 0 16px 0;font-family:%s;font-size:16px;line-height:26px;color:%s;">%s</p>' % (SANS, TXT, esc(p)) for p in c['body'])
    sig = ('<p style="margin:4px 0 0 0;font-family:%s;font-size:16px;line-height:24px;color:%s;"><span style="font-weight:600;color:%s;">%s</span>'
           '<span style="color:%s;"> &middot; %s</span></p>' % (SANS, TXT, WHITE, esc(c['sign']), MUTED, esc(c['sign_role'])))
    psl = '<p style="margin:22px 0 0 0;font-family:%s;font-size:15px;line-height:24px;color:%s;">%s</p>' % (SANS, MUTED, esc(c['ps'])) if c.get('ps') else ''
    u = utm(c['cta2_url'], mp, 'cta2')
    cta = ('<div style="height:34px;line-height:34px;font-size:0;">&nbsp;</div>%s<div style="height:12px;line-height:12px;font-size:0;">&nbsp;</div>'
           '<div style="text-align:center;">%s</div>' % (button(c['cta2'], u), sub(c['friction'])))
    line = '<div style="border-top:1px solid %s;font-size:0;line-height:0;height:1px;margin-bottom:34px;">&nbsp;</div>' % LINE
    return row(line + ps + sig + psl + cta, BLACK, '0 40px 52px 40px', 'pad')


def s_footer(mp):
    f = open(os.path.join(P, 'footer.html')).read()
    f = f.replace('{{SHARED}}/logo-white-dark.png', SHARED['logo-white-dark.png'])
    f = f.replace('{{IMG}}/fb.png', ASSETS['fb.png']).replace('{{IMG}}/ig.png', ASSETS['ig.png'])
    # contrast: in de partial staan de afmeld-/voorkeur-/webview-links op #111111 op #282828 (onleesbaar); hier #BDB8B0
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
a{text-decoration:none;}
@media only screen and (max-width:620px){
  .w{width:100%!important;}
  .pad{padding-left:20px!important;padding-right:20px!important;}
  .gp{padding-left:12px!important;padding-right:12px!important;}
  .navhide{display:none!important;}
  .h1{font-size:40px!important;line-height:44px!important;}
  .h2{font-size:32px!important;line-height:37px!important;}
  .lead{font-size:16px!important;line-height:25px!important;}
  .btnw{width:100%!important;}
  .ban a{font-size:13px!important;line-height:19px!important;}
  .gi,.gi img{width:96px!important;height:96px!important;}
  .gt{padding:10px 14px!important;}
  .gn{font-size:16px!important;line-height:21px!important;}
  .hf{max-width:100%!important;}
  .hf2{border-top:1px solid #3A3838!important;}
  .pv{font-size:20px!important;line-height:24px!important;}
  .ex div{font-size:24px!important;}
}
/* Outlook.com / Gmail-app dark mode: wit blijft wit */
[data-ogsc] .tw,[data-ogsb] .tw{color:#FFFFFF!important;}
</style>"""


def page(c, im, mp):
    pre = esc(c['preview']) + '&#847;&zwnj;&nbsp;' * 60
    body = (s_banner(c, mp) + s_header(mp) + s_hero(c, im, mp) + s_extra(c, mp) + s_deal(c, im, mp) + s_steel(c, im, mp) +
            s_gifts(c, mp) + s_proof(c, mp) + s_body(c, mp) + s_footer(mp))
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
    vis_txt = re.sub(r'<[^>]+>', ' ', vis)
    bad = []
    if '—' in h or '&mdash;' in h: bad.append('em dash')
    if re.search(r'(?i)purifier', h): bad.append('purifier')
    if re.search(r'(?i)\b(4|four) (free )?gifts', vis_txt): bad.append('4 gifts')
    for u in re.findall(r'href="(https://siraatskitchen\.com[^"]*)"', h):
        if 'utm_campaign=%s-' % CAMPAIGN not in u: bad.append('no utm: ' + u)
    for u in re.findall(r'href="(https?://[^"]*)"', h):
        if 'siraatskitchen.com' not in u and 'facebook.com' not in u and 'instagram.com' not in u: bad.append('foreign link: ' + u)
    if bad: raise SystemExit('%s: %s' % (name, '; '.join(sorted(set(bad)))))


def preview(h):
    h = h.replace('{% unsubscribe_link %}', '#').replace('{% manage_preferences_link %}', '#').replace('{% web_view_link %}', '#')
    h = h.replace('{{ organization.name }}', "Siraat's Kitchen").replace('{{ organization.full_address }}', '[address]')
    h = re.sub(r'\{%.*?%\}', '', h); h = re.sub(r'\{\{.*?\}\}', '', h)
    return h


def main(only):
    os.makedirs(PREV, exist_ok=True)
    report = []
    for mp, variants in MAILS.items():
        if only and mp not in only: continue
        os.makedirs(os.path.join(C, mp), exist_ok=True)
        for fn, over in variants.items():
            v = re.search(r'email-([ab])\.html', fn); v = v.group(1) if v else None
            cp = parse_copy(os.path.join(C, mp, 'copy.md'), v)
            im = parse_images(os.path.join(C, mp, 'images', 'README.md'), v)
            c = dict(BASE); c.update(over); c.update(cp)
            if c['cta_url'] == U_SET and 'cta' in cp and re.search(r'(?i)sale|shop black friday', cp['cta']): c['cta_url'] = U_SALE
            h = page(c, im, mp)
            check(h, mp + '/' + fn)
            open(os.path.join(C, mp, fn), 'w').write(h)
            tag = mp + ('-' + v if v else '')
            open(os.path.join(PREV, tag + '.html'), 'w').write(preview(h))
            report.append('%-26s %-13s copy:%-3s images:%s  %d KB' % (mp, fn, 'yes' if cp else 'no', ','.join(sorted(im)) or '-', len(h) // 1024))
    print('\n'.join(report))


if __name__ == '__main__':
    main(sys.argv[1:])
