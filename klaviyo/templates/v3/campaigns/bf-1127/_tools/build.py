"""Black Friday 27 nov 2026 (plan Floris 26 nov): extra 20% already applied.
US: 12-delige set (+ Damascus messenset, Just Everything als tekstregels). INTL: 6-delige set.
Bouwt ../us-0800.html, ../intl-0800.html (hybride: korte brief + 1 productblok) en
../us-1800.html, ../intl-1800.html (korte tekstbrief), plus .preview/*.html met opgeloste tags.
Codes (nog aan te maken): BENJAMIN20 (US) en BENJAMIN20INTL. Aanname: alleen vrijdag geldig, tot middernacht ET.
Gebruik: python3 -I build.py"""
import os, re

T = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(T)
REPO = os.path.abspath(os.path.join(C, *['..'] * 5)); P = os.path.join(REPO, 'klaviyo', 'templates', 'partials')
def urls(p): return {a: b for a, b in (l.split() for l in open(p) if len(l.split()) == 2)}
SH = urls(os.path.join(P, 'shared', 'klaviyo-urls.txt')); AS = urls(os.path.join(P, 'assets', 'klaviyo-urls.txt'))

def partial(n):
    h = open(os.path.join(P, n)).read()
    h = re.sub(r'\{\{SHARED\}\}/([\w.-]+)', lambda m: SH[m.group(1)], h)
    return re.sub(r'\{\{IMG\}\}/([\w.-]+)', lambda m: AS[m.group(1)], h)

SITE = 'https://siraatskitchen.com'
SET12 = '/products/titanium-hammered-cookware-set-12-pcs-free-pizza-steel-1'
SET6 = '/products/titanium-hammered-pan-set-with-lids-6-pcs'
KNIFE = '/products/damascus-67-layer-knife-set-8-piece'
JE = '/products/the-just-everything-bundle-34-pcs'
def link(path, code, camp, content):
    return (f'{SITE}/discount/{code}?redirect={path}&utm_source=klaviyo&utm_medium=email'
            f'&utm_campaign=bf-1127-{camp}&utm_content={content}')
IMG12 = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/12pcsset.webp?v=1781591412&width=1100&height=1100&crop=center&format=pjpg'
IMG6 = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/6pcscookwareset.webp?v=1783062518&width=1100&height=1100&crop=center&format=pjpg'

PAGE = '#F8F7F2'; INK = '#282828'; MUTED = '#6B6660'; LINE = '#E5E0D6'; RED = '#B3262C'; PANEL = '#F1EEE7'
SERIF = "'Instrument Serif','Times New Roman',Times,serif"; SANS = 'Inter,Arial,Helvetica,sans-serif'
FIRST = "{{ first_name|default:'there' }}"

def p(t, size=17, lh=27, color=INK, pad='0 0 14px 0', align='left'):
    return f'<div style="font-family:{SANS};font-size:{size}px;line-height:{lh}px;color:{color};text-align:{align};padding:{pad};">{t}</div>'
def a(t, href):
    return f'<a href="{href}" style="color:{RED};font-weight:700;text-decoration:underline;">{t}</a>'
def btn(label, href):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" bgcolor="{RED}" '
            f'style="background-color:{RED};border-radius:4px;"><a href="{href}" style="display:block;padding:18px 20px;font-family:{SANS};'
            f'font-size:15px;line-height:20px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;color:#FFFFFF;text-decoration:none;">{label}</a></td></tr></table>')
def row(inner, pad='0 40px', bg='#FFFFFF'):
    return f'<tr><td class="pad" bgcolor="{bg}" style="padding:{pad};background-color:{bg};">{inner}</td></tr>\n'
def topbar(t):
    return (f'<tr><td bgcolor="{RED}" style="background-color:{RED};padding:11px 20px;text-align:center;font-family:{SANS};font-size:12px;'
            f'line-height:17px;letter-spacing:1.5px;font-weight:700;color:#FFFFFF;">{t}</td></tr>\n')
def signoff():
    return p('Benjamin<br><span style="color:#6B6660;font-size:14px;">Founder, Siraat</span>', pad='4px 0 0 0')

def shell(title, preheader, body):
    pre = preheader + '&#847;&zwnj;&nbsp;' * 60
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<style>@media only screen and (max-width:620px){{.wrap{{width:100%!important}}.pad{{padding-left:20px!important;padding-right:20px!important}}.h2{{font-size:28px!important;line-height:32px!important}}.navhide{{display:none!important}}}}</style></head>
<body style="margin:0;padding:0;background:{PAGE};">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;">{pre}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{PAGE}" style="background-color:{PAGE};"><tr><td align="center" style="padding:0;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;background:#FFFFFF;">
{partial('header.html')}
{body}
{partial('footer.html')}
</table></td></tr></table></body></html>'''

def product_block(img, href, alt, badge, title, price_html, lines, button):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid {LINE};border-radius:8px;">'
            f'<tr><td style="padding:0;"><a href="{href}"><img src="{img}" width="558" alt="{alt}" style="display:block;width:100%;max-width:558px;height:auto;border:0;border-radius:8px 8px 0 0;"></a></td></tr>'
            f'<tr><td style="padding:20px 22px 22px 22px;">'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="{RED}" style="background-color:{RED};border-radius:3px;padding:6px 10px;font-family:{SANS};font-size:12px;font-weight:800;letter-spacing:1.5px;color:#FFFFFF;">{badge}</td></tr></table>'
            f'<div class="h2" style="font-family:{SERIF};font-size:30px;line-height:34px;color:{INK};padding:12px 0 8px 0;">{title}</div>'
            + (p(price_html, 18, 28, pad='0 0 10px 0') if price_html else '')
            + ''.join(p(l, 15, 23, pad='0 0 8px 0') for l in lines)
            + '<div style="height:8px;">&nbsp;</div>' + btn(button, href)
            + p('Already applied, no code needed &middot; 30-day returns &middot; 75-year warranty', 13, 19, MUTED, '10px 0 0 0', 'center')
            + '</td></tr></table>')

# ------------------------------------------------------------ 08:00 US (hybride)
def us_0800():
    C_, K = 'BENJAMIN20', 'us-0800'
    L = lambda path, c: link(path, C_, K, c)
    b = topbar('EXTRA 20% OFF THE 12-PIECE SET &middot; ALREADY APPLIED &middot; TODAY ONLY')
    letter = (p(f'Hey {FIRST},') +
              p('It&rsquo;s Black Friday, and I&rsquo;ve gone a little crazy.') +
              p('Yesterday I added 10% for Thanksgiving. Today I&rsquo;m going further, but only on the set I&rsquo;m proudest of: our 12-piece Titanium Hammered Cookware Set.') +
              p(f'{a("EXTRA 20% OFF, on top of the Black Friday sale", L(SET12, "letter-link"))}. No code. It&rsquo;s already applied when you tap the button below.') +
              p('That&rsquo;s <b>$519.20</b> for the full kitchen, plus a FREE Titanium Hammered Pizza Steel. It ends tonight at midnight.') +
              signoff())
    b += row(letter, '32px 40px 24px 40px')
    prod = product_block(IMG12, L(SET12, 'set12-img'), 'Siraat Titanium Hammered Cookware Set, 12 pieces', '75% OFF &middot; EXTRA 20% ALREADY APPLIED',
        'The 12-piece Titanium Hammered Cookware Set',
        f'<span style="text-decoration:line-through;color:{MUTED};">$2,047</span> &nbsp;<span style="text-decoration:line-through;color:{MUTED};">$649</span> &nbsp;<b style="color:{RED};font-size:24px;">$519.20</b>',
        ['<b>+ FREE Titanium Hammered Pizza Steel</b> (still $149 on its own) <b>+ 5 free gifts</b>.',
         'Three hammered pans (8, 10, 12 inch), 2-qt and 3-qt saucepans, an 8-qt stock pot and six lids. Ships from our US warehouses.'],
        'Get the 12-piece set for $519.20 &rarr;')
    b += row(prod, '6px 20px 24px 20px', PANEL)
    extra = (p('<b>Also an extra 20% today, already applied:</b>', 15, 23, pad='0 0 6px 0') +
             p(f'&rarr; {a("Damascus 67-layer knife set (8 pcs)", L(KNIFE, "knife-link"))}: <span style="text-decoration:line-through;color:{MUTED};">$1,599</span> $399.20', 15, 23, pad='0 0 4px 0') +
             p(f'&rarr; {a("The Just Everything Bundle (34 pcs)", L(JE, "je-link"))}: <span style="text-decoration:line-through;color:{MUTED};">$4,997</span> $1,199.20', 15, 23, pad='0 0 0 0'))
    b += row(extra, '24px 40px 36px 40px')
    return shell('Extra 20% off the 12-piece set', 'Today only. $519.20 + a free Pizza Steel. Ends midnight.', b)

# ------------------------------------------------------------ 08:00 INTL (hybride, geen bedragen)
def intl_0800():
    C_, K = 'BENJAMIN20INTL', 'intl-0800'
    L = lambda path, c: link(path, C_, K, c)
    b = topbar('EXTRA 20% OFF THE 6-PIECE SET &middot; ALREADY APPLIED &middot; TODAY ONLY')
    letter = (p(f'Hey {FIRST},') +
              p('It&rsquo;s Black Friday, and I&rsquo;ve gone a little crazy.') +
              p('This week Bon App&eacute;tit put our cookware in their holiday issue. To celebrate, I&rsquo;m going further today, on the set most of you start with: our 6-piece Titanium Hammered Pan Set with Lids.') +
              p(f'{a("EXTRA 20% OFF, on top of the Black Friday sale", L(SET6, "letter-link"))}. No code. It&rsquo;s already applied when you tap the button below.') +
              p('Plus 5 free gifts with your order. It ends tonight at midnight.') +
              signoff())
    b += row(letter, '32px 40px 24px 40px')
    prod = product_block(IMG6, L(SET6, 'set6-img'), 'Siraat Titanium Hammered Pan Set with Lids, 6 pieces', 'UP TO 70% OFF &middot; EXTRA 20% ALREADY APPLIED',
        'The 6-piece Titanium Hammered Pan Set with Lids', '',
        ['Three hammered pans and a lid for each. A pure titanium cooking surface, no coatings, nothing to peel or flake.',
         '<b>+ 5 free gifts</b> with every order.'],
        'Get the 6-piece set with extra 20% &rarr;')
    b += row(prod, '6px 20px 36px 20px', PANEL)
    return shell('Extra 20% off the 6-piece set', 'Today only, on top of the Black Friday sale. Ends midnight.', b)

# ------------------------------------------------------------ 18:00 tekstbrieven
def us_1800():
    L = lambda c: link(SET12, 'BENJAMIN20', 'us-1800', c)
    body = (p(f'Hey {FIRST},') +
            p('Quick one. At midnight I switch off the extra 20% on the 12-piece set. My team was not thrilled I turned it on in the first place.') +
            p(f'Until then it&rsquo;s <b>$519.20</b> for the full hammered titanium kitchen, with a FREE Pizza Steel and 5 free gifts. Already applied, no code: {a("get the 12-piece set before midnight", L("letter-link"))}.') +
            p('If it&rsquo;s been sitting in your cart all week, tonight is the night.') +
            signoff() +
            p(f'P.S. 30-day returns and a 75-year warranty. {a("The extra 20% ends at midnight", L("ps-link"))}.', 15, 23, MUTED, '18px 0 0 0'))
    return shell('Before midnight', 'I have to switch it off tonight.', row(body, '32px 40px 36px 40px'))

def intl_1800():
    L = lambda c: link(SET6, 'BENJAMIN20INTL', 'intl-1800', c)
    body = (p(f'Hey {FIRST},') +
            p('Quick one. At midnight I switch off the extra 20% on the 6-piece set. My team was not thrilled I turned it on in the first place.') +
            p(f'Until then it&rsquo;s on top of the Black Friday sale, with 5 free gifts. Already applied, no code: {a("get the 6-piece set before midnight", L("letter-link"))}.') +
            p('If it&rsquo;s been sitting in your cart all week, tonight is the night.') +
            signoff() +
            p(f'P.S. 30-day returns and a 75-year warranty. {a("The extra 20% ends at midnight", L("ps-link"))}.', 15, 23, MUTED, '18px 0 0 0'))
    return shell('Before midnight', 'I have to switch it off tonight.', row(body, '32px 40px 36px 40px'))

os.makedirs(os.path.join(T, '.preview'), exist_ok=True)
for name, h in (('us-0800', us_0800()), ('intl-0800', intl_0800()), ('us-1800', us_1800()), ('intl-1800', intl_1800())):
    assert '—' not in h and 'purifier' not in h.lower() and '80%' not in h, name
    if name.startswith('intl'):
        assert 'Pizza' not in h and '$' not in re.sub(r'\{\{.*?\}\}|\{%.*?%\}', '', h), name
    open(os.path.join(C, name + '.html'), 'w').write(h)
    pv = h.replace(FIRST, 'Sarah').replace('{% unsubscribe_link %}', '#').replace('{% manage_preferences_link %}', '#').replace('{% web_view_link %}', '#')
    pv = re.sub(r"\{% today .*?%\}", '', pv).replace('{{ organization.name }}', 'Siraats Kitchen').replace('{{ organization.full_address }}', 'Address').replace('{{ sk_ref }}', '')
    open(os.path.join(T, '.preview', name + '.html'), 'w').write(pv)
    print(name, len(h))
