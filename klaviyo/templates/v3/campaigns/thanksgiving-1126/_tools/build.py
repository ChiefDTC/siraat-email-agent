"""Thanksgiving 26 nov 2026: bouwt us.html (Thanksgiving x Black Friday) en intl.html (As seen in Bon Appetit).
Copy: ../copy.md (copy-agent, 26 nov). Beelden: ../upload/klaviyo-urls.txt. Vaste header/footer uit partials.
Gebruik: python3 -I build.py   (schrijft ../us.html, ../intl.html en .preview/*.html met opgeloste tags)"""
import os, re

T = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(T)
REPO = os.path.abspath(os.path.join(C, *['..'] * 5)); P = os.path.join(REPO, 'klaviyo', 'templates', 'partials')
def urls(p): return {a: b for a, b in (l.split() for l in open(p) if len(l.split()) == 2)}
SH = urls(os.path.join(P, 'shared', 'klaviyo-urls.txt')); AS = urls(os.path.join(P, 'assets', 'klaviyo-urls.txt'))
UP = urls(os.path.join(C, 'upload', 'klaviyo-urls.txt'))
SH['gift-cookbook.jpg'] = 'https://cdn.klaviyomail.com/company/TdtTzz/images/dabf0446-a5d7-49ae-87f8-672e5692bf5b.jpeg'

def partial(n):
    h = open(os.path.join(P, n)).read()
    h = re.sub(r'\{\{SHARED\}\}/([\w.-]+)', lambda m: SH[m.group(1)], h)
    return re.sub(r'\{\{IMG\}\}/([\w.-]+)', lambda m: AS[m.group(1)], h)

SITE = 'https://siraatskitchen.com'
def link(path, market, content, code='THANKSGIVING10'):
    return (f'{SITE}/discount/{code}?redirect={path}&utm_source=klaviyo&utm_medium=email'
            f'&utm_campaign=thanksgiving-1126-{market}&utm_content={content}')
SET12 = '/products/titanium-hammered-cookware-set-12-pcs-free-pizza-steel-1'
SET6 = '/products/titanium-hammered-pan-set-with-lids-6-pcs'
SALE = '/collections/black-friday-sale'
PAN = '/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern'
IMGPAN = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/Titanium_hammered_pan_pro_standard_b69d1fc5-43d8-40a5-9ad7-523bdddc54d4.webp?v=1781682831&width=400&height=400&crop=center&format=pjpg'
IMG12 = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/12pcsset.webp?v=1781591412&width=1100&height=900&crop=bottom&format=pjpg'
IMG6 = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/6pcscookwareset.webp?v=1783062518&width=1100&height=900&crop=center&format=pjpg'

PAGE = '#F8F7F2'; INK = '#282828'; MUTED = '#6B6660'; LINE = '#E5E0D6'; RED = '#B3262C'; NAVY = '#1F2A44'; PANEL = '#F1EEE7'
SERIF = "'Instrument Serif','Times New Roman',Times,serif"; SANS = 'Inter,Arial,Helvetica,sans-serif'

def p(t, size=17, lh=27, color=INK, pad='0 0 14px 0', align='left', extra=''):
    return f'<div style="font-family:{SANS};font-size:{size}px;line-height:{lh}px;color:{color};text-align:{align};padding:{pad};{extra}">{t}</div>'
def btn(label, href, bg=RED):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" bgcolor="{bg}" '
            f'style="background-color:{bg};border-radius:4px;"><a href="{href}" style="display:block;padding:18px 20px;font-family:{SANS};'
            f'font-size:15px;line-height:20px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;color:#FFFFFF;text-decoration:none;">{label}</a></td></tr></table>')
def row(inner, pad='0 40px', bg='#FFFFFF'):
    return f'<tr><td class="pad" bgcolor="{bg}" style="padding:{pad};background-color:{bg};">{inner}</td></tr>\n'
def eyebrow(t, color=RED):
    return f'<div style="font-family:{SANS};font-size:12px;line-height:16px;letter-spacing:2.5px;font-weight:700;color:{color};text-transform:uppercase;padding-bottom:8px;">{t}</div>'
def h2(t, size=34):
    return f'<div class="h2" style="font-family:{SERIF};font-size:{size}px;line-height:{size+4}px;color:{INK};padding-bottom:14px;">{t}</div>'
def bullets(items):
    li = ''.join(f'<tr><td width="22" valign="top" style="font-family:{SANS};font-size:16px;line-height:25px;color:{RED};font-weight:700;">&#10003;</td>'
                 f'<td style="font-family:{SANS};font-size:16px;line-height:25px;color:{INK};padding-bottom:6px;">{i}</td></tr>' for i in items)
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{li}</table>'
def codebar(note, code='THANKSGIVING10'):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" bgcolor="{PANEL}" '
            f'style="background-color:{PANEL};border:1px dashed #BFB7A8;border-radius:4px;padding:14px 12px;">'
            f'<div style="font-family:{SANS};font-size:12px;letter-spacing:2px;font-weight:600;color:{MUTED};">YOUR CODE</div>'
            f'<div style="font-family:{SANS};font-size:24px;line-height:32px;letter-spacing:3px;font-weight:800;color:{INK};">{code}</div>'
            f'<div style="font-family:{SANS};font-size:13px;line-height:19px;color:{MUTED};">{note}</div></td></tr></table>')
def img(src, href, alt, w=520):
    return f'<a href="{href}"><img src="{src}" width="{w}" alt="{alt}" style="display:block;width:100%;max-width:{w}px;height:auto;border:0;border-radius:6px;"></a>'
def signoff():
    return p('Benjamin<br><span style="color:#6B6660;font-size:14px;">Founder, Siraat</span>', pad='4px 0 0 0')

def shell(title, preheader, body):
    pre = preheader + '&#847;&zwnj;&nbsp;' * 60
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<style>@media only screen and (max-width:620px){{.wrap{{width:100%!important}}.pad{{padding-left:20px!important;padding-right:20px!important}}.h2{{font-size:30px!important;line-height:34px!important}}.navhide{{display:none!important}}}}</style></head>
<body style="margin:0;padding:0;background:{PAGE};">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;">{pre}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{PAGE}" style="background-color:{PAGE};"><tr><td align="center" style="padding:0;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;background:#FFFFFF;">
{partial('header.html')}
{body}
{partial('footer.html')}
</table></td></tr></table></body></html>'''

def topbar(t):
    return (f'<tr><td bgcolor="{NAVY}" style="background-color:{NAVY};padding:11px 20px;text-align:center;font-family:{SANS};font-size:12px;'
            f'line-height:17px;letter-spacing:1.5px;font-weight:700;color:#FFFFFF;">{t}</td></tr>\n')

GIFTS_US = [('gift-shipping.jpg', 'Free shipping'), ('gift-mystery.jpg', 'A mystery gift'), ('gift-ebook.jpg', 'The Plastic-Free Cooking e-book'),
            ('gift-cookbook.jpg', 'The Favorites Cookbook e-book'), ('gift-filter.jpg', 'A chance to win a PFAS water filter ($450 value)')]
def gifts(items, title):
    cells = ''.join(f'<tr><td width="64" style="padding:6px 12px 6px 0;"><img src="{SH[f]}" width="56" alt="" style="display:block;width:56px;height:56px;border-radius:6px;"></td>'
                    f'<td style="font-family:{SANS};font-size:15px;line-height:21px;color:{INK};">{t}</td></tr>' for f, t in items)
    return eyebrow(title) + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{cells}</table>'

# ------------------------------------------------------------------ US (Floris 26 nov: CTA direct onder hero, sale laten zien, vierkante setfoto; nooit 80%)
IMG12SQ = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/12pcsset.webp?v=1781591412&width=1100&height=1100&crop=center&format=pjpg'
def us():
    m = 'us'
    b = topbar('EXTRA 10% OFF ENDS TONIGHT AT MIDNIGHT ET')
    b += f'<tr><td style="padding:0;"><a href="{link(SALE, m, "hero")}"><img src="{UP["us-hero-thanksgiving-btn.jpg"]}" width="600" alt="Happy Thanksgiving. Thanksgiving x Black Friday, extra 10% off. Claim 70% + extra 10% off." style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>\n'
    story = (p('<b>Happy Thanksgiving 2026.</b>', 19, 28, pad='0 0 12px 0') +
             p('This morning I was at the office going through the Black Friday orders, and I kept thinking about this year. More than 100,000 of you now cook on our pans. That still doesn&rsquo;t feel real to me.') +
             p('So I did something without running it by the team first: I put an <b>extra 10% off everything</b>, on top of the Black Friday sale. No meeting, no approval. Just a thank you for a year we never expected.') +
             p('It&rsquo;s already applied when you tap any button in this email. But I can only keep it on for today, so <b style="color:#B3262C;">the extra 10% ends tonight at midnight ET.</b>') +
             p('Here&rsquo;s to a full table today, and a healthy end of the year for you and yours.') + signoff())
    b += row(story, '30px 40px 28px 40px')
    offer = (f'<div style="font-family:{SANS};font-size:13px;line-height:18px;letter-spacing:3px;font-weight:700;color:#CDB27A;text-align:center;">BLACK FRIDAY SALE &middot; THANKSGIVING EXTRA</div>'
             f'<div style="font-family:{SANS};font-size:60px;line-height:62px;font-weight:800;color:#FFFFFF;text-align:center;padding:12px 0 2px 0;letter-spacing:-1px;">UP TO 70% OFF</div>'
             f'<div style="font-family:{SANS};font-size:30px;line-height:36px;font-weight:800;color:#F2C14E;text-align:center;padding-bottom:16px;">+ AN EXTRA 10% OFF</div>'
             f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="border:2px dashed #CDB27A;border-radius:6px;padding:12px;">'
             f'<div style="font-family:{SANS};font-size:12px;letter-spacing:2px;font-weight:600;color:#BDB8B0;">USE CODE</div>'
             f'<div style="font-family:{SANS};font-size:30px;line-height:38px;letter-spacing:4px;font-weight:800;color:#FFFFFF;">THANKSGIVING10</div>'
             f'<div style="font-family:{SANS};font-size:13px;line-height:19px;color:#BDB8B0;">Already applied when you tap any button &middot; <b style="color:#F2C14E;">ends tonight at midnight ET</b></div></td></tr></table>'
             f'<div style="height:20px;">&nbsp;</div>' + btn('Shop the Black Friday sale &rarr;', link(SALE, m, 'offer-btn')) +
             p('+ 5 FREE gifts with every order ($555 value) &middot; Extra 10% ends tonight', 14, 20, '#BDB8B0', '12px 0 0 0', 'center'))
    b += row(offer, '34px 40px 34px 40px', '#1E1D1B')
    prod = (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid {LINE};border-radius:8px;"><tr><td style="padding:0;">'
            f'<a href="{link(SET12, m, "set12-img")}"><img src="{IMG12SQ}" width="558" alt="Siraat Titanium Hammered Cookware Set, 12 pieces" style="display:block;width:100%;max-width:558px;height:auto;border:0;border-radius:8px 8px 0 0;"></a></td></tr>'
            f'<tr><td style="padding:20px 22px 22px 22px;">'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="{RED}" style="background-color:{RED};border-radius:3px;padding:6px 10px;font-family:{SANS};font-size:12px;font-weight:800;letter-spacing:1.5px;color:#FFFFFF;">68% OFF + EXTRA 10%</td>'
            f'<td style="padding-left:10px;font-family:{SANS};font-size:12px;font-weight:700;letter-spacing:1.5px;color:{MUTED};">+ FREE PIZZA STEEL</td></tr></table>'
            f'<div class="h2" style="font-family:{SERIF};font-size:30px;line-height:34px;color:{INK};padding:12px 0 8px 0;">The 12-piece Titanium Hammered Cookware Set</div>' +
            p(f'<span style="text-decoration:line-through;color:{MUTED};">$2,047</span> &nbsp;$649 &nbsp;&rarr;&nbsp; <b style="color:{RED};font-size:22px;">$584.10</b> <span style="color:{MUTED};font-size:14px;">with THANKSGIVING10</span>', 18, 28, pad='0 0 10px 0') +
            p('<b>Plus a FREE Titanium Hammered Pizza Steel</b> (still $149 on its own). Three hammered pans (8, 10, 12 inch), 2-qt and 3-qt saucepans, an 8-qt stock pot and six lids. Ships from our US warehouses. 93% sold.', 15, 23, pad='0 0 16px 0') +
            btn('Claim my 12-piece set &rarr;', link(SET12, m, 'set12-btn')) +
            p('Code already applied &middot; 30-day returns &middot; 75-year warranty', 13, 19, MUTED, '10px 0 0 0', 'center') +
            '</td></tr></table>')
    b += row(prod, '30px 20px 16px 20px', PANEL)
    six = (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid {LINE};border-radius:8px;"><tr>'
           f'<td width="150" valign="middle" style="padding:14px;"><a href="{link(SET6, m, "set6-img")}"><img src="{IMG6}" width="130" alt="Siraat 6-piece hammered pan set with lids" style="display:block;width:130px;height:auto;border-radius:6px;border:0;"></a></td>'
           f'<td valign="middle" style="padding:14px 14px 14px 0;">{p("<b>Starting smaller? The 6-piece set</b>", 16, 22, pad="0 0 4px 0")}'
           f'{p(f"<span style=text-decoration:line-through;color:{MUTED};>$1,163</span> $349 &rarr; <b style=color:{RED};>$314.10</b> with the code", 15, 22, pad="0 0 8px 0")}'
           f'<a href="{link(SET6, m, "set6-btn")}" style="font-family:{SANS};font-size:13px;font-weight:800;letter-spacing:1px;color:{RED};">CLAIM THE 6-PIECE SET &rarr;</a></td></tr></table>')
    pan = (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid {LINE};border-radius:8px;"><tr>'
           f'<td width="150" valign="middle" style="padding:14px;"><a href="{link(PAN, m, "pan-img")}"><img src="{IMGPAN}" width="130" alt="Siraat Titanium Hammered Pan Pro Standard" style="display:block;width:130px;height:auto;border-radius:6px;border:0;"></a></td>'
           f'<td valign="middle" style="padding:14px 14px 14px 0;">{p("<b>Just one pan? The Titanium Hammered Pan Pro</b>", 16, 22, pad="0 0 4px 0")}'
           f'{p(f"<span style=text-decoration:line-through;color:{MUTED};>$480</span> $144 &rarr; <b style=color:{RED};>$129.60</b> with the code", 15, 22, pad="0 0 8px 0")}'
           f'<a href="{link(PAN, m, "pan-btn")}" style="font-family:{SANS};font-size:13px;font-weight:800;letter-spacing:1px;color:{RED};">CLAIM THE PAN PRO &rarr;</a></td></tr></table>')
    b += row(six, '0 20px 12px 20px', PANEL)
    b += row(pan, '0 20px 30px 20px', PANEL)
    b += row(gifts(GIFTS_US, 'Your 5 free gifts with every order'), '30px 40px 18px 40px')
    trust = ''.join(f'<td width="25%" align="center" valign="top" style="padding:0 4px;font-family:{SANS};font-size:12px;line-height:17px;color:{INK};">'
                    f'<div style="font-family:{SERIF};font-size:24px;line-height:28px;">{x}</div>{y}</td>'
                    for x, y in [('75 yrs', 'warranty'), ('30 days', 'returns'), ('PFAS', 'lab tested'), ('100K+', 'customers')])
    b += row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {LINE};border-bottom:1px solid {LINE};"><tr><td style="padding:18px 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{trust}</tr></table></td></tr></table>', '10px 40px 6px 40px')
    close = (p('<b>Your extra 10% ends tonight at midnight ET.</b> Tomorrow it&rsquo;s gone. The Black Friday sale itself runs until Dec 5.', 16, 25, pad='18px 0 18px 0', align='center') +
             btn('Claim 70% + extra 10% off &rarr;', link(SALE, m, 'close-btn')) +
             p('P.S. The free Pizza Steel only comes with the 12-piece set, and the set is 93% sold. If it&rsquo;s on your list, get it before midnight while the extra 10% still applies.', 15, 23, MUTED, '22px 0 0 0'))
    b += row(close, '0 40px 40px 40px')
    return shell('Happy Thanksgiving', 'Benjamin added an extra 10% off. It ends tonight at midnight.', b)

# ------------------------------------------------------------------ INTL (Floris 26 nov: duidelijker, direct response, sale laten zien, code BONAPPETIT10)
def intl():
    m = 'intl'; CODE = 'BONAPPETIT10'
    L = lambda path, c: link(path, m, c, CODE)
    b = topbar('AS SEEN IN BON APP&Eacute;TIT &middot; EXTRA 10% OFF WITH CODE BONAPPETIT10')
    b += f'<tr><td style="padding:0;"><a href="{L(SALE, "hero")}"><img src="{UP["intl-hero-bon-appetit.jpg"]}" width="600" alt="As seen in Bon Appétit, the Holiday 2026 issue: This holiday, cook with the best." style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>\n'
    # groot aanbodblok, donker, direct onder de hero
    offer = (f'<div style="font-family:{SANS};font-size:13px;line-height:18px;letter-spacing:3px;font-weight:700;color:#CDB27A;text-align:center;">BLACK FRIDAY SALE &middot; AS SEEN IN BON APP&Eacute;TIT</div>'
             f'<div style="font-family:{SANS};font-size:60px;line-height:62px;font-weight:800;color:#FFFFFF;text-align:center;padding:12px 0 2px 0;letter-spacing:-1px;">UP TO 70% OFF</div>'
             f'<div style="font-family:{SANS};font-size:30px;line-height:36px;font-weight:800;color:#F2C14E;text-align:center;padding-bottom:16px;">+ AN EXTRA 10% OFF</div>'
             f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="border:2px dashed #CDB27A;border-radius:6px;padding:12px;">'
             f'<div style="font-family:{SANS};font-size:12px;letter-spacing:2px;font-weight:600;color:#BDB8B0;">USE CODE</div>'
             f'<div style="font-family:{SANS};font-size:30px;line-height:38px;letter-spacing:4px;font-weight:800;color:#FFFFFF;">{CODE}</div>'
             f'<div style="font-family:{SANS};font-size:13px;line-height:19px;color:#BDB8B0;">Already applied when you tap any button below</div></td></tr></table>'
             f'<div style="height:20px;">&nbsp;</div>' + btn('Shop the sale now &rarr;', L(SALE, 'offer-btn')) +
             p('+ 5 FREE gifts with every order &middot; Ends Sunday, Nov 30', 14, 20, '#BDB8B0', '12px 0 0 0', 'center'))
    b += row(offer, '34px 40px 34px 40px', '#1E1D1B')
    # waarom: het citaat + uitleg
    why = (eyebrow('What Bon App&eacute;tit wrote') + h2('&ldquo;This holiday, cook with the best.&rdquo;', 32) +
           f'<div style="border-left:3px solid {RED};padding:2px 0 2px 16px;margin:0 0 18px 0;font-family:{SERIF};font-style:italic;font-size:20px;line-height:28px;color:{INK};">&ldquo;No better gift for the home chef than a stellar, non-toxic cooking surface. Siraat&rsquo;s Hammered Titanium Cookware serves up zero coatings, impeccable quality &amp; trusted by 100K+ customers.&rdquo;</div>' +
           p('Here&rsquo;s what that means in your kitchen:', 16, 25) +
           bullets(['<b>Zero coatings.</b> A pure titanium cooking surface, nothing to peel or flake into your food.',
                    '<b>Tested free from PFAS</b> by Light Labs, report no. 25895.',
                    '<b>Built to last.</b> Covered by a 75-year warranty.',
                    '<b>No risk.</b> 30 days to change your mind.']))
    b += row(why, '36px 40px 26px 40px')
    # productkaart 6-delig met kortingsbadge
    prod = (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid {LINE};border-radius:8px;"><tr><td style="padding:0;position:relative;">'
            f'<a href="{L(SET6, "set6-img")}"><img src="{IMG6}" width="558" alt="Siraat Titanium Hammered Pan Set with Lids, 6 pieces" style="display:block;width:100%;max-width:558px;height:auto;border:0;border-radius:8px 8px 0 0;"></a></td></tr>'
            f'<tr><td style="padding:20px 22px 22px 22px;">'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="{RED}" style="background-color:{RED};border-radius:3px;padding:6px 10px;font-family:{SANS};font-size:12px;font-weight:800;letter-spacing:1.5px;color:#FFFFFF;">70% OFF + EXTRA 10%</td>'
            f'</tr></table>'
            f'<div class="h2" style="font-family:{SERIF};font-size:30px;line-height:34px;color:{INK};padding:12px 0 8px 0;">The 6-piece Titanium Hammered Pan Set with Lids</div>' +
            p('Three hammered pans and a lid for each. The easiest way to start cooking without coatings. For yourself, or as the gift this year.', 16, 24, pad='0 0 16px 0') +
            btn('Get the 6-piece set &rarr;', L(SET6, 'set6-btn')) +
            p(f'Code {CODE} already applied &middot; 5 free gifts included', 13, 19, MUTED, '10px 0 0 0', 'center') +
            '</td></tr></table>')
    b += row(prod, '30px 20px 30px 20px', PANEL)
    # stappen: hoe werkt het
    steps = (eyebrow('How it works') +
             bullets(['Tap any button in this email. Your extra 10% is applied automatically.',
                      'Pick your set or pan. Black Friday prices are already up to 70% off.',
                      'Check out. 5 free gifts are added to every order. (No discount showing? Enter BONAPPETIT10 at checkout.)']))
    b += row(steps, '30px 40px 10px 40px')
    trust = ''.join(f'<td width="25%" align="center" valign="top" style="padding:0 4px;font-family:{SANS};font-size:12px;line-height:17px;color:{INK};">'
                    f'<div style="font-family:{SERIF};font-size:24px;line-height:28px;">{a}</div>{b2}</td>'
                    for a, b2 in [('75 yrs', 'warranty'), ('30 days', 'returns'), ('PFAS', 'lab tested'), ('100K+', 'customers')])
    b += row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {LINE};border-bottom:1px solid {LINE};"><tr><td style="padding:18px 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{trust}</tr></table></td></tr></table>', '18px 40px 6px 40px')
    close = (p('<b>Your extra 10% ends Sunday, Nov 30 at 11:59 PM ET.</b> After that it&rsquo;s gone, and the sale ends Dec 5.', 16, 25, pad='22px 0 18px 0', align='center') +
             btn('Shop the sale with BONAPPETIT10 &rarr;', L(SALE, 'close-btn')) +
             p('Being in Bon App&eacute;tit is a big moment for a small team. Thank you for cooking with us first.<br>Benjamin, Founder', 15, 23, MUTED, '24px 0 0 0', 'center'))
    b += row(close, '0 40px 40px 40px')
    return shell('As seen in Bon Appétit', 'Up to 70% off + an extra 10% with BONAPPETIT10. Already applied, ends Sunday.', b)

os.makedirs(os.path.join(T, '.preview'), exist_ok=True)
for name, h in (('us', us()), ('intl', intl())):
    assert '—' not in h and 'purifier' not in h.lower() and '4 gifts' not in h.lower() and '80%' not in h, name
    if name == 'intl': assert 'Pizza' not in h and '$' not in re.sub(r'\{\{.*?\}\}|\{%.*?%\}', '', h), 'intl bevat $ of Pizza'
    open(os.path.join(C, name + '.html'), 'w').write(h)
    pv = h.replace("{{ first_name|default:'there' }}", 'there').replace('{% unsubscribe_link %}', '#').replace('{% manage_preferences_link %}', '#').replace('{% web_view_link %}', '#')
    pv = re.sub(r"\{% today .*?%\}", '', pv).replace('{{ organization.name }}', 'Siraats Kitchen').replace('{{ organization.full_address }}', 'Address').replace('{{ sk_ref }}', '')
    open(os.path.join(T, '.preview', name + '.html'), 'w').write(pv)
    print(name, len(h))
