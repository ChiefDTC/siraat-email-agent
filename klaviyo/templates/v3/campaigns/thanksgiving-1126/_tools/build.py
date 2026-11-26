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
    b = topbar('EXTRA 10% OFF ENDS TONIGHT AT MIDNIGHT')
    b += f'<tr><td style="padding:0;"><a href="{link(SALE, m, "hero")}"><img src="{UP["us-hero-thanksgiving-v7.jpg"]}" width="600" alt="Happy Thanksgiving. Thanksgiving x Black Friday, extra 10% off. Claim 70% off." style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>\n'
    story = (p('<b>Happy Thanksgiving 2026.</b>', 19, 28, pad='0 0 12px 0') +
             p('This morning I was at the office going through the Black Friday orders, and I kept thinking about this year. More than 100,000 of you now cook on our pans. That still doesn&rsquo;t feel real to me.') +
             p('So I did something without running it by the team first: I put an <b>extra 10% off everything</b>, on top of the Black Friday sale. No meeting, no approval. Just a thank you for a year we never expected.') +
             p(f'It&rsquo;s already applied when you tap the button or any image in this email. But I can only keep it on for today, so <a href="{link(SALE, m, "story-link")}" style="color:#B3262C;font-weight:700;text-decoration:underline;">the extra 10% ends tonight at midnight.</a>') +
             p('Here&rsquo;s to a full table today, and a healthy end of the year for you and yours.') + signoff())
    b += row(story, '30px 40px 28px 40px')
    b += row(btn('Shop the Black Friday sale &rarr;', link(SALE, m, 'offer-btn')), '6px 40px 40px 40px')
    return shell('Happy Thanksgiving', 'Benjamin added an extra 10% off. It ends tonight at midnight.', b)

# ------------------------------------------------------------------ INTL (Floris 26 nov: duidelijker, direct response, sale laten zien, code BONAPPETIT10)
def intl():
    m = 'intl'; CODE = 'BONAPPETIT10'
    L = lambda path, c: link(path, m, c, CODE)
    b = topbar('AS SEEN IN BON APP&Eacute;TIT &middot; EXTRA 10% OFF WITH CODE BONAPPETIT10')
    b += f'<tr><td style="padding:0;"><a href="{L(SALE, "hero")}"><img src="{UP["intl-hero-bon-appetit.jpg"]}" width="600" alt="As seen in Bon Appétit, the Holiday 2026 issue: This holiday, cook with the best." style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>\n'
    story = (p('<b>A note from Benjamin</b>', 19, 28, pad='0 0 12px 0') +
             p('When I started Siraat, the idea was simple: cookware with no coatings, so nothing from your pan ends up in your food. A lot of people told me nobody would care what their pan is made of.') +
             p('This holiday season, our hammered titanium cookware is in the <b>Holiday 2026 issue of Bon App&eacute;tit</b>, one of the most iconic food magazines in the world. Right in the season when people decide what to cook with, and what to give.') +
             p('I&rsquo;m honestly proud of that. Not for the name, but because it shows the mission is landing: more and more people want to know what they cook on.') +
             p(f'To celebrate, I added an <b>extra 10% off everything</b> with code BONAPPETIT10, on top of the Black Friday sale. <a href="{L(SALE, "story-link")}" style="color:#B3262C;font-weight:700;text-decoration:underline;">It&rsquo;s already applied when you tap here.</a>') +
             p('Thank you for being part of this from the start.') + signoff())
    b += row(story, '30px 40px 28px 40px')
    # groot aanbodblok, donker, direct onder de hero
    b += row(btn('Shop the sale now &rarr;', L(SALE, 'offer-btn')), '6px 40px 40px 40px')
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
