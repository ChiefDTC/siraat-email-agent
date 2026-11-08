"""Urgentie-sprint 8 nov 2026: de 6 deadline-mails (FLASH, VIP-WEEKEND, CREDIT, LAST-HOURS, GIFTS, DRAW), elk US en INT.
Bronnen: research/plannen/2026-11-urgentie-sprint/BRIEF.md, copy/copy.json (alle tekst komt daaruit) en ux/ux-spec.md (opbouw, maten,
kleuren, eerste scherm <= 560 px op 375, knop 1 uiterlijk op 520 px, alles gelinkt met eigen utm_content). Concept, niets in Klaviyo, geen testmails.

Bouw (vanuit /tmp):  python3 -I make_urg.py            -> urg-<mail>-<us|int>.html, .klaviyo.html, -preview.html in urgency-1108/
QA en screenshots:   python3 -I render_urg.py <uitmap>  en  node shot_urg.js <previewmap>

Placeholders. In de bron en in .klaviyo.html staan deadline, prijs en tegoed als duidelijke tokens [[DEADLINE]] enz., NIET als Django-variabele
(een lege {{ DEADLINE }} zou in Klaviyo stil leeg renderen; UX-spec 2.3). Vul VALUES hieronder in zodra de backend-deadline echt bestaat en bouw
opnieuw; zolang er nog een [[...]] in .klaviyo.html staat, is die mail niet verzendklaar (render_urg.py meldt dat als BLOKKEREND).
De VIP-code is wel Klaviyo-klaar: {% coupon_code 'VIPWEEKEND' %} (couponnaam in Klaviyo nog aanmaken, BRIEF: unieke code per profiel).
Beelden: alle hero's in HERO (bestandsnaam) en KLAVIYO_URL (na upload invullen); -preview.html gebruikt de lokale bestanden in assets/."""
import os, re, json, html, csv, subprocess, sys, shutil

ROOT = '/home/user/siraat-email-agent'
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # .../campaigns/urgency-1108
A = os.path.join(N, 'assets')
T = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'scripts')); import v5lib as V
COPY = json.load(open(os.path.join(ROOT, 'research/plannen/2026-11-urgentie-sprint/copy/copy.json')))['mails']

# ---------------------------------------------------------------- placeholders
# None = token blijft staan in .klaviyo.html (niet verzendklaar). Voorstel Klaviyo-tags staan erachter als commentaar.
VALUES = {
    'DEADLINE': None,          # bv. 'tonight at 11:59 PM ET' (UX-spec 2.4: met tijdzone, gelijk aan de backend)
    'DEADLINE_SHORT': None,    # bv. 'tonight'
    'DEADLINE_DATE': None,     # bv. 'November 15, 2026 at 11:59 PM ET' (juridische regel CREDIT en DRAW)
    'FLASH_PRICE': None,       # US, bv. '$199' (Floris zet de prijs in Shopify)
    'FLASH_PERCENT': None,     # INT, bv. '20%'
    'CREDIT': None,            # {{ person|lookup:'rise_wallet_balance'|floatformat:"-2" }} pas na Klaviyo-preview en segment saldo > 0
    'POINTS': None,            # {{ person|lookup:'siraat_points'|floatformat:0 }}
    'PAN_AFTER_CREDIT': None,  # 144 min CREDIT, in Klaviyo te berekenen
    'DRAW_RULES_URL': None,    # officiele regels; mail 6 mag niet live zonder
}
# Voorbeeldwaarden voor -preview.html en de QA-render (opdracht: DEADLINE "tonight at 11:59 PM", DEADLINE_SHORT "tonight", CREDIT 12).
SAMPLE = {'DEADLINE': 'tonight at 11:59 PM', 'DEADLINE_SHORT': 'tonight', 'DEADLINE_DATE': 'November 8, 2026 at 11:59 PM ET',
          'FLASH_PRICE': '$199', 'FLASH_PERCENT': '20%', 'CREDIT': '12', 'POINTS': '1,200', 'PAN_AFTER_CREDIT': '132',
          'DRAW_RULES_URL': 'https://siraatskitchen.com/pages/filter-draw-rules'}
def caps(d):
    d = dict(d)
    for k in ('DEADLINE', 'DEADLINE_SHORT'):
        if d.get(k): d[k + '_CAPS'] = d[k].upper()
    return d
TOKENS = ['DEADLINE_SHORT_CAPS', 'DEADLINE_CAPS', 'DEADLINE_SHORT', 'DEADLINE_DATE', 'DEADLINE', 'FLASH_PRICE', 'FLASH_PERCENT',
          'CREDIT', 'POINTS', 'PAN_AFTER_CREDIT', 'DRAW_RULES_URL']
def fill(h, vals):
    for k in TOKENS:
        if vals.get(k): h = h.replace('[[%s]]' % k, vals[k])
    return h

# ---------------------------------------------------------------- beelden (één plek; KLAVIYO_URL na upload invullen)
HERO = {'flash': 'urg-flash-hero.jpg', 'vip': 'urg-vip-weekend-hero.jpg', 'credit': 'urg-credit-hero.jpg',
        'gifts': 'urg-gifts-hero.jpg', 'draw': 'urg-draw-hero.jpg', 'last': 'urg-last-hours-hero.jpg'}
KLAVIYO_URL = {f: None for f in HERO.values()}   # bv. 'urg-flash-hero.jpg': 'https://cdn.klaviyomail.com/company/TdtTzz/images/....jpeg'
COOKBOOK = 'https://cdn.klaviyomail.com/company/TdtTzz/images/dabf0446-a5d7-49ae-87f8-672e5692bf5b.jpeg'
SOCIAL = {'fb.png': 'https://cdn.klaviyomail.com/company/TdtTzz/images/17c00632-f9db-4dcd-a27e-bf0adc4987da.png',
          'ig.png': 'https://cdn.klaviyomail.com/company/TdtTzz/images/6b905e47-7bf9-4aec-a63b-0538ecc6bd60.png'}
CDN = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/'
SQ = lambda n: CDN + n + '?width=600&height=420&crop=center&format=pjpg'
PROD = {  # key: (naam, beeld)
    'standard': ('Pan Pro Standard', 'Titanium_hammered_pan_pro_standard_b69d1fc5-43d8-40a5-9ad7-523bdddc54d4.webp'),
    'set6': ('Pan Set with Lids, 6 Pcs', '6pcscookwareset.webp'),
    'crepe': ('Cr&ecirc;pe Pan Pro', 'Crepepan01.jpg'),
    'deep': ('Deep Pan Pro', 'DeepHammeredPan.webp'),
}
GRID = ['standard', 'set6', 'crepe', 'deep']

# ---------------------------------------------------------------- stijl
INK, ESP, CREAM, WHITE, BRICK, GOLD, Y, GREY, HAIR, SOFT = '#272727', '#321E1D', '#F8F7F2', '#FFFFFF', '#AC3B19', '#B8862B', '#FFB800', '#727272', '#ECE7DD', '#C9C6C0'
FF = 'Inter,Arial,Helvetica,sans-serif'
SYS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
SITE = 'https://siraatskitchen.com'
SALE = SITE + '/collections/black-friday-sale'
DUO = SITE + '/products/2-pans-and-2-lids'
VIPTAG = "{% coupon_code 'VIPWEEKEND' %}"

def utm(url, camp, ct):
    return url + ('&' if '?' in url else '?') + 'utm_source=klaviyo&utm_medium=email&utm_campaign=%s&utm_content=%s' % (camp, ct)
def vip(path, camp, ct):  # /discount/CODE?redirect=pad met URL-gecodeerde UTM (UX-spec 4)
    return SITE + '/discount/' + VIPTAG + '?redirect=' + path + '%3Futm_source%3Dklaviyo%26utm_medium%3Demail%26utm_campaign%3D' + camp + '%26utm_content%3D' + ct

CSS = '''
    .w{width:100%!important;}
    .pad{padding-left:24px!important;padding-right:24px!important;}
    .navhide{display:none!important;}
    .h1u{font-size:36px!important;line-height:40px!important;}
    .bigc{font-size:56px!important;line-height:60px!important;}
    .lt{padding-left:24px!important;padding-right:24px!important;}
    .tb{font-size:11px!important;letter-spacing:0.8px!important;padding:12px 12px!important;}
    .btn{font-size:15px!important;letter-spacing:0.5px!important;padding:19px 12px!important;}
'''
def head(meta, title, pre):
    return '''<!--
URGENTIE-SPRINT 8 NOV 2026 · urgency-1108 (concept, niet in Klaviyo, niets live, geen testmails).
%s
-->
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>%s</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
  body{margin:0;padding:0;background:#FFFFFF;-webkit-text-size-adjust:100%%;}
  table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}
  img{border:0;display:block;line-height:100%%;outline:none;text-decoration:none;}
  h1{margin:0;padding:0;}
  a{color:#272727;}
  @media only screen and (max-width:620px){%s  }
</style>
</head>
<body style="margin:0;padding:0;background:#FFFFFF;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">%s</div>
<!-- MARKET-SIGNAL: profile -->
<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF">
<tr><td align="center" style="padding:0 0 32px 0;">
<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:#FFFFFF;" bgcolor="#FFFFFF">
''' % (meta.strip(), html.escape(title), CSS, pre)
TAIL = '\n{{FOOTER}}\n\n</table>\n</td></tr>\n</table>\n</td></tr>\n</table>\n</body>\n</html>\n'

def row(bg, pad, inner, align='left', cls='pad'):
    return '<tr><td class="%s" align="%s" bgcolor="%s" style="background-color:%s;padding:%s;text-align:%s;">%s</td></tr>\n' % (cls, align, bg, bg, pad, align, inner)
def gap(bg, h=24):
    return '<tr><td bgcolor="%s" style="background-color:%s;height:%dpx;line-height:%dpx;font-size:0;">&nbsp;</td></tr>\n' % (bg, bg, h, h)
def txt(t, size=16, lh=24, color=INK, weight=400, extra=''):
    return '<div style="font-family:%s;font-size:%dpx;line-height:%dpx;color:%s;font-weight:%d;%s">%s</div>' % (FF, size, lh, color, weight, extra, t)
def al(t, href, size=16, lh=24, color=INK, weight=400, extra='', ur=''):
    """Tekst als blok-link (UX-spec 1.4: eigen <a display:block> per vlak, geen onderstreping, kleur zoals de tekst)."""
    return '<a href="%s" data-urg="%s" style="display:block;text-decoration:none;font-family:%s;font-size:%dpx;line-height:%dpx;color:%s;font-weight:%d;%s">%s</a>' % (
        href, ur, FF, size, lh, color, weight, extra, t)
def h1(t, href, color, align='left'):
    return ('<h1 class="h1u" style="margin:0;padding:0;font-family:%s;font-size:40px;line-height:44px;font-weight:800;letter-spacing:-0.8px;color:%s;text-align:%s;">'
            '<a href="%s" data-urg="h1" style="display:block;text-decoration:none;color:%s;">%s</a></h1>') % (FF, color, align, href, color, t)
def topbar(t, href):
    return ('<tr><td align="center" bgcolor="%s" style="background-color:%s;padding:0;text-align:center;">'
            '<a href="%s" data-urg="topbar" class="tb" style="display:block;padding:12px 20px;font-family:%s;font-size:12px;line-height:16px;letter-spacing:1.6px;font-weight:800;color:#FFFFFF;text-decoration:none;text-transform:uppercase;">%s</a></td></tr>\n{{HEADER}}\n') % (INK, INK, href, FF, t)
def button(label, url, bg, dark=False, pad='0 40px 0 40px', ur='cta'):
    fill_, fg = ('#FFFFFF', INK) if dark else (INK, '#FFFFFF')
    vml = ('<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="%s" style="height:56px;v-text-anchor:middle;width:360px;" arcsize="50%%" stroke="f" fillcolor="%s">'
           '<center style="color:%s;font-family:Arial,sans-serif;font-size:16px;font-weight:bold;letter-spacing:1px;">%s</center></v:roundrect><![endif]-->') % (url, fill_, fg, label.upper())
    a = ('<!--[if !mso]><!--><a href="%s" data-urg="%s" class="btn" style="display:block;padding:19px 16px;font-family:%s;font-size:16px;line-height:18px;font-weight:800;letter-spacing:1px;color:%s;text-decoration:none;text-transform:uppercase;">%s&nbsp;&rarr;</a><!--<![endif]-->') % (url, ur, FF, fg, label)
    b = ('<table role="presentation" width="360" cellpadding="0" cellspacing="0" border="0" style="width:100%%;max-width:360px;margin:0 auto;"><tr>'
         '<td align="center" bgcolor="%s" style="background-color:%s;border-radius:28px;">%s%s</td></tr></table>') % (fill_, fill_, vml, a)
    return row(bg, pad, b, 'center')
def friction(t, bg, dark=False, pad='10px 40px 0 40px'):
    return row(bg, pad, txt(t, 13, 18, SOFT if dark else GREY, 500, 'text-align:center;'), 'center')
def heroimg(key, alt, href, bg, pad='0'):
    i = '<img src="{{IMG}}/%s" width="600" alt="%s" style="display:block;width:100%%;max-width:600px;height:auto;border:0;">' % (HERO[key], html.escape(alt, quote=True))
    return row(bg, pad, '<a href="%s" data-urg="hero-img" style="display:block;text-decoration:none;">%s</a>' % (href, i), 'center', '')
def para(t, bg=WHITE, pad='0 40px 16px 40px', size=16, lh=25, color=INK):
    return row(bg, pad, txt(t, size, lh, color, 400), 'left')
def quote(q, who, href, bg=CREAM):
    h = txt('&#9733;&#9733;&#9733;&#9733;&#9733;', 15, 18, GOLD, 400, 'letter-spacing:3px;text-align:center;padding-bottom:10px;')
    h += al('&ldquo;%s&rdquo;' % q, href, 20, 28, INK, 600, 'text-align:center;', 'review')
    h += txt('%s, verified buyer' % who, 13, 18, GREY, 600, 'text-align:center;padding-top:10px;')
    return row(bg, '26px 40px 24px 40px', h, 'center')
def eyebrow(t, href, dark):
    return al(t, href, 12, 16, GOLD if dark else BRICK, 700, 'letter-spacing:2px;text-transform:uppercase;padding-bottom:10px;', 'eyebrow')

# ---------------------------------------------------------------- 5 gifts (stijl scripts/gifts5.py: 2x2 raster, filter gecentreerd eronder)
def gift_list(us, int_ship=False):
    return [('gift-mystery.jpg', 'Mystery gift', 'Mystery<br>gift', '$35 value' if us else 'Included'),
            ('gift-shipping.jpg', 'Free shipping', 'Free shipping' + ('<br>duties paid' if int_ship else '') if not us else 'Free<br>shipping', '$15 value' if us else 'Included'),
            ('gift-ebook.jpg', 'Plastic-free ebook', 'Plastic-free<br>ebook', '$30 value' if us else 'Included'),
            ('gift-cookbook.jpg', 'Favorites cookbook', 'Favorites<br>cookbook', '$25 value' if us else 'Included'),
            ('gift-filter.jpg', 'Chance to win a PFAS water filter', 'Chance to win a<br>PFAS water filter', '$450 value, weekly draw' if us else 'Weekly draw')]
def gifts_grid(us, href, bg=WHITE, eyebrow_t='WITH EVERY ORDER', title=None, note='The filter is a chance to win in our weekly draw. The rest comes with every order.', compact=True):
    def tile(g, w='50%'):
        im, alt, lab, val = g
        if compact:  # zelfde 2x2 + filter gecentreerd, tegel liggend (beeld links) zodat het blok op 375 px ~260 px hoog blijft
            return ('<td width="%s" valign="middle" bgcolor="#FFFFFF" data-gift="%s" style="background-color:#FFFFFF;border:1px solid %s;padding:8px;">'
                    '<a href="%s" data-urg="gift" style="display:block;text-decoration:none;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>'
                    '<td width="56" valign="middle"><img src="{{SHARED}}/%s" width="56" alt="%s" style="display:block;width:56px;height:56px;border:0;"></td>'
                    '<td valign="middle" style="padding-left:8px;text-align:left;"><span style="display:block;font-family:%s;font-size:12px;line-height:15px;font-weight:600;color:%s;">%s</span>'
                    '<span style="display:block;font-family:%s;font-size:11px;line-height:15px;font-weight:600;color:%s;padding-top:2px;">%s</span></td></tr></table></a></td>') % (
                w, im, HAIR, href, im, alt, FF, INK, lab, FF, BRICK, val)
        return ('<td width="%s" valign="top" align="center" bgcolor="#FFFFFF" data-gift="%s" style="background-color:#FFFFFF;border:1px solid %s;padding:8px 6px 10px 6px;">'
                '<a href="%s" data-urg="gift" style="display:block;text-decoration:none;"><img src="{{SHARED}}/%s" width="72" alt="%s" style="display:block;width:72px;height:72px;margin:0 auto;border:0;">'
                '<span style="display:block;font-family:%s;font-size:13px;line-height:17px;font-weight:600;color:%s;padding-top:6px;">%s</span>'
                '<span style="display:block;font-family:%s;font-size:12px;line-height:16px;font-weight:600;color:%s;padding-top:2px;">%s</span></a></td>') % (
            w, im, HAIR, href, im, alt, FF, INK, lab, FF, BRICK, val)
    g = gift_list(us, int_ship=not us)
    sp = '<td width="10" style="font-size:0;line-height:0;">&nbsp;</td>'
    t = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>%s%s%s</tr><tr><td colspan="3" style="height:10px;line-height:10px;font-size:0;">&nbsp;</td></tr><tr>%s%s%s</tr></table>' % (
        tile(g[0]), sp, tile(g[1]), tile(g[2]), sp, tile(g[3]))
    t += '<table role="presentation" align="center" width="50%%" cellpadding="0" cellspacing="0" border="0" data-gift5row="1" style="margin:10px auto 0 auto;width:50%%;"><tr>%s</tr></table>' % tile(g[4], '100%')
    title = title or ('5 free gifts with every order' + (' <span style="white-space:nowrap;">($555 value)</span>' if us else ''))
    h = txt(eyebrow_t, 12, 16, BRICK, 700, 'letter-spacing:2px;text-align:center;')
    h += al(title, href, 26, 31, INK, 800, 'text-align:center;letter-spacing:-0.4px;padding:6px 0 18px 0;', 'gifts-title') + t
    h += txt(note, 13, 19, GREY, 400, 'text-align:center;padding-top:14px;')
    return row(bg, '30px 40px 26px 40px', h, 'center')
def gifts_strip(us, href):
    """Compacte strook voor het eerste scherm (GIFTS, donker): 5 kleine echte gift-beelden op één rij, labels wit."""
    cells = ''
    for im, alt, lab, val in gift_list(us):
        lab2 = {'gift-filter.jpg': 'Chance to win<br>a filter'}.get(im, lab)
        cells += ('<td width="20%%" valign="top" align="center" style="padding:0 3px;"><img src="{{SHARED}}/%s" width="56" alt="%s" style="display:block;width:56px;height:56px;margin:0 auto;border-radius:6px;border:0;">'
                  '<span style="display:block;font-family:%s;font-size:11px;line-height:14px;font-weight:600;color:#FFFFFF;padding-top:6px;">%s</span></td>') % (im, alt, FF, lab2)
    return '<a href="%s" data-urg="hero-gifts" style="display:block;text-decoration:none;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>%s</tr></table></a>' % (href, cells)

# ---------------------------------------------------------------- producten 2x2 (alleen waar de UX-spec ze vraagt: VIP, CREDIT, GIFTS, DRAW)
def money(x): return ('$%.2f' % x).replace('.00', '')
def card(k, us, href, note=''):
    n, im = PROD[k]
    tag = '<span style="display:inline-block;background-color:%s;color:%s;font-family:%s;font-size:11px;line-height:13px;font-weight:800;letter-spacing:0.6px;padding:4px 7px;border-radius:3px;white-space:nowrap;">70%% OFF</span>' % (Y, INK, FF)
    if us:
        p, w = V.amount(k, 'US'), V.amount(k, 'US', 'compare_at')
        price = ('<span style="font-family:%s;font-size:18px;line-height:24px;font-weight:700;color:%s;">%s</span> <span style="font-family:%s;font-size:13px;line-height:24px;color:%s;text-decoration:line-through;">%s</span> ' % (FF, INK, money(p), FF, GREY, money(w))) + tag
        if note: price += txt(note % money(p * 0.9), 13, 18, BRICK, 600, 'padding-top:4px;')
    else:
        price = tag + (txt(note, 13, 18, BRICK, 600, 'padding-top:6px;') if note else '')
    return ('<a href="%s" data-urg="card" style="display:block;text-decoration:none;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid %s;border-radius:10px;">'
            '<tr><td style="padding:0;"><img src="%s" width="260" alt="%s" style="display:block;width:100%%;max-width:260px;height:auto;border:0;border-radius:10px 10px 0 0;"></td></tr>'
            '<tr><td style="padding:12px 12px 14px 12px;"><span style="display:block;font-family:%s;font-size:15px;line-height:20px;font-weight:700;color:%s;padding-bottom:6px;">%s &rarr;</span>%s</td></tr></table></a>') % (
        href, HAIR, SQ(im), n, FF, INK, n, price)
def grid(us, hrefs, title, bg=CREAM, note=''):
    c = [card(k, us, hrefs[k], note) for k in GRID]
    t = ''
    for i in (0, 2):
        t += '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td width="50%%" valign="top" style="padding:0 5px 10px 0;">%s</td><td width="50%%" valign="top" style="padding:0 0 10px 5px;">%s</td></tr></table>' % (c[i], c[i + 1])
    return row(bg, '28px 40px 20px 40px', txt(title, 22, 28, INK, 800, 'text-align:center;padding-bottom:16px;letter-spacing:-0.3px;') + t, 'center')

def legal(t, bg=WHITE, pad='14px 40px 0 40px'):
    return row(bg, pad, txt(t, 12, 17, GREY, 400, 'text-align:center;'), 'center')
def ps(t, href, bg=WHITE):
    return row(bg, '6px 40px 26px 40px', al(t, href, 15, 23, INK, 400, 'font-style:italic;', 'ps'), 'left')

# ---------------------------------------------------------------- copy-hulp
REPL = {'{{VIP_CODE}}': VIPTAG}
def tk(s):
    """copy.json-placeholder {{X}} -> [[X]] (token) of Klaviyo-tag; first_name blijft Klaviyo."""
    if s is None: return ''
    for a, b in REPL.items(): s = s.replace(a, b)
    s = re.sub(r'\{\{(DEADLINE_SHORT|DEADLINE_DATE|DEADLINE|FLASH_PRICE|FLASH_PERCENT|CREDIT|POINTS|PAN_AFTER_CREDIT|DRAW_RULES_URL)\}\}', r'[[\1]]', s)
    return s
def check_reviews(proofs):
    rev = {r['id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'content/reviews/reviews.csv')))}
    for p in proofs:
        o = rev[p['id']]['quote']; pos = 0
        assert rev[p['id']]['stars'] == '5', p['id']
        for part in [x.strip() for x in p['quote'].split('...') if x.strip()]:
            j = o.find(part, pos); assert j >= 0, (p['id'], 'niet letterlijk', part); pos = j + len(part)
def meta(mid, mkt, m, c, extra=''):
    notes = ' | '.join(m.get('notes_nl', [])).replace('{{BLOCK:', 'BLOCK ').replace('{{', '[[').replace('}}', ']]')
    return ('ID: %s\nMARKT: %s\nSENDER: %s\nSUBJECT A: %s\nSUBJECT B: %s\nSUBJECT C: %s\nSUBJECT KEUZE: %s (deadline in %s)\nPREVIEW: %s\nRESEND: %s / %s\nWIE: %s\n'
            'TOKENS: [[...]] = placeholder, pas verzendklaar als VALUES in _tools/make_urg.py gevuld is (UX-spec 2.3).\nNOTITIES COPY: %s\n%s') % (
        mid, mkt, m['sender'], tk(c['subject_a']), tk(c['subject_b']), tk(c['subject_c']), c['subject_pick'], c['subject_deadline'], tk(c['preview']),
        tk(c.get('resend_subject')), tk(c.get('resend_preview')), m['audience'], notes, extra)
def subj(c): return tk(c['subject_' + c['subject_pick'].lower()])

files = {}
# ======================================================================= 1 FLASH (donker eerste scherm)
def flash(mkt):
    m = COPY['1-flash']; c = m[mkt.upper()]; us = mkt == 'us'; camp = 'urgency-1108-flash-' + mkt
    L = lambda ct: utm(DUO, camp, ct)
    check_reviews(c['proof'])
    x = '' if us else 'LET OP: 2 Pans + 2 Lids staat in de catalogus als US-only (content/catalog, duo2 us_only). UX-spec 3 wil INT op Pan Pro Standard; copy houdt de set. Beslissing Floris voor INT live gaat.'
    b = head(meta('urg-flash-' + mkt, mkt.upper(), m, c, x), subj(c), tk(c['preview']))
    b += topbar('Flash deal ends [[DEADLINE_CAPS]]', L('topbar'))
    inner = eyebrow(c['eyebrow'], L('hero-eyebrow'), True)
    inner += h1('%s<br>%s' % (c['hero_line1'], c['hero_line2']), L('hero-kop'), '#FFFFFF')
    if us:
        offer = ('<span style="font-size:30px;line-height:36px;font-weight:800;color:#FFFFFF;">[[FLASH_PRICE]]</span>&nbsp; '
                 '<span style="font-size:18px;line-height:36px;font-weight:600;color:%s;text-decoration:line-through;">$249</span>&nbsp; '
                 '<span style="font-size:15px;line-height:36px;font-weight:600;color:%s;">for 2 pans + 2 lids</span>') % (SOFT, SOFT)
    else:
        offer = ('<span style="display:inline-block;background-color:%s;color:%s;font-size:15px;line-height:18px;font-weight:800;letter-spacing:0.6px;padding:6px 10px;border-radius:3px;">EXTRA [[FLASH_PERCENT]] OFF</span>&nbsp; '
                 '<span style="font-size:15px;line-height:36px;font-weight:600;color:%s;">on 2 pans + 2 lids</span>') % (Y, INK, SOFT)
    inner += al(offer, L('hero-offer'), 16, 36, '#FFFFFF', 600, 'padding-top:14px;', 'offer')
    inner += al(tk(c['countdown']), L('hero-deadline'), 16, 22, '#FFFFFF', 700, 'padding-top:8px;', 'deadline')
    b += row(INK, '26px 40px 20px 40px', inner, 'left')
    b += button(tk(c['cta']), L('cta1'), INK, True, ur='cta1') + friction(c['friction'], INK, True, '10px 40px 22px 40px')
    b += heroimg('flash', 'Two friends laughing as shrimp sizzle in a Siraat hammered titanium pan. Flash deal ends [[DEADLINE]]', L('hero-img'), INK)
    b += gap(WHITE, 26)
    for p in c['body']: b += para(tk(p))
    b += quote(c['proof'][0]['quote'], c['proof'][0]['name'], L('review'))
    b += gap(WHITE, 24) + para(c['authority'], WHITE, '0 40px 6px 40px', 15, 23, '#4A4A4A')
    b += button(tk(c['cta']), L('cta2'), WHITE, pad='14px 40px 0 40px', ur='cta2') + friction(c['friction'], WHITE, pad='10px 40px 4px 40px')
    b += gifts_grid(us, L('gifts'), WHITE, 'WITH THIS ORDER', None)
    b += row(CREAM, '26px 40px 16px 40px', al(tk(c['final_cta_line']), L('final-line'), 17, 24, BRICK, 700, 'text-align:center;', 'final'), 'center')
    b += button(tk(c['cta']), L('cta3'), CREAM, pad='0 40px 26px 40px', ur='cta3')
    b += gap(WHITE, 22) + ps(tk(c['ps']), L('ps'))
    return b + TAIL

# ======================================================================= 2 VIP-WEEKEND (donker, codevak)
def vipmail(mkt):
    m = COPY['2-vip-weekend']; c = m[mkt.upper()]; us = mkt == 'us'; camp = 'urgency-1108-vip-' + mkt
    L = lambda ct, path='/collections/black-friday-sale': vip(path, camp, ct)
    check_reviews(c['proof'])
    x = "VIP-code: {% coupon_code 'VIPWEEKEND' %} in codevak en in elke link (Klaviyo wijst per ontvanger per bericht één code toe). Couponnaam is een voorstel; 'on top' alleen als de code in Shopify op de saleprijs stapelt (UX-spec 3, open vraag 3)."
    b = head(meta('urg-vip-' + mkt, mkt.upper(), m, c, x), subj(c), tk(c['preview']))
    b += topbar('VIP extra 10% ends [[DEADLINE_CAPS]]', L('topbar'))
    inner = eyebrow(c['eyebrow'], L('hero-eyebrow'), True)
    inner += h1('%s<br>%s' % (c['hero_line1'], c['hero_line2']), L('hero-kop'), '#FFFFFF')
    code = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:2px dashed %s;border-radius:8px;"><tr><td align="center" style="padding:10px 10px;">'
            '<span class="offer-code" style="display:block;font-family:%s;font-size:24px;line-height:30px;font-weight:800;letter-spacing:3px;color:%s;white-space:nowrap;">%s</span>'
            '<span style="display:block;font-family:%s;font-size:12px;line-height:16px;color:%s;padding-top:2px;">Your personal code &middot; already applied when you tap below</span></td></tr></table>') % (GOLD, FF, INK, VIPTAG, FF, GREY)
    inner += '<div style="padding-top:16px;"><a href="%s" data-urg="offer" style="display:block;text-decoration:none;">%s</a></div>' % (L('hero-code'), code)
    inner += al('Your code works until [[DEADLINE]].', L('hero-deadline'), 16, 22, '#FFFFFF', 700, 'padding-top:14px;', 'deadline')
    b += row(INK, '20px 40px 18px 40px', inner, 'left')
    b += button(c['cta'], L('cta1'), INK, True, ur='cta1') + friction(c['friction'], INK, True, '10px 40px 22px 40px')
    b += heroimg('vip', 'A couple laughing over a steak in a Siraat hammered titanium pan. Your extra 10% ends [[DEADLINE]]', L('hero-img'), INK)
    b += gap(WHITE, 26)
    for p in c['body']: b += para(tk(p))
    hrefs = {k: L('card-' + k, '/products/' + V.handle(k)) for k in GRID}
    b += grid(us, hrefs, 'What your 10% looks like' if us else 'Where your 10% goes', CREAM, '%s with your code' if us else 'Extra 10% with your code')
    b += quote(c['proof'][0]['quote'], c['proof'][0]['name'], L('review'), WHITE)
    b += para(c['authority'], WHITE, '0 40px 6px 40px', 15, 23, '#4A4A4A')
    b += gifts_grid(us, L('gifts'), WHITE, 'COMES WITH YOUR ORDER', None)
    b += row(WHITE, '4px 40px 16px 40px', al(tk(c['final_cta_line']), L('final-line'), 17, 24, BRICK, 700, 'text-align:center;', 'final'), 'center')
    b += button(c['cta'], L('cta2'), WHITE, ur='cta2') + friction(c['friction'], WHITE, pad='10px 40px 4px 40px')
    b += gap(WHITE, 18) + ps(tk(c['ps']), L('ps'))
    return b + TAIL

# ======================================================================= 3 CREDIT (licht, persoonlijk)
def credit(mkt):
    m = COPY['3-credit']; c = m[mkt.upper()]; us = mkt == 'us'; camp = 'urgency-1108-credit-' + mkt
    L = lambda ct: utm(SALE, camp, ct)
    check_reviews(c['proof'])
    x = 'Tegoed: [[CREDIT]] en [[POINTS]] uit Rise.ai (rise_wallet_balance / siraat_points). Alleen naar segment saldo > 0, nooit $0 of een default (UX-spec 3). Mag pas live als Rise echt tegoed met vervaldatum zet.'
    b = head(meta('urg-credit-' + mkt, mkt.upper(), m, c, x), subj(c), tk(c['preview']))
    b += topbar('Your credit expires [[DEADLINE_CAPS]]', L('topbar'))
    b += row(WHITE, '24px 40px 12px 40px', al(tk(c['body'][0]), L('hero-hi'), 16, 22, INK, 500, '', 'hi'), 'left')
    card_ = txt(c['eyebrow'], 12, 16, BRICK, 700, 'letter-spacing:2px;')
    if us:
        card_ += ('<h1 style="margin:0;padding:0;"><a href="%s" data-urg="h1" style="display:block;text-decoration:none;font-family:%s;color:%s;">'
                  '<span class="bigc" style="display:block;font-size:64px;line-height:68px;font-weight:800;letter-spacing:-2px;padding-top:6px;">$[[CREDIT]]</span>'
                  '<span class="h1u" style="display:block;font-size:30px;line-height:36px;font-weight:800;letter-spacing:-0.5px;">%s</span></a></h1>') % (L('hero-kop'), FF, INK, (lambda z: z[:1].upper() + z[1:])(tk(c['hero_line2'])))
    else:
        card_ += h1('%s<br>%s' % (c['hero_line1'], tk(c['hero_line2'])), L('hero-kop'), INK).replace('padding:0;', 'padding:6px 0 0 0;', 1)
    card_ += al(tk(c['subline']), L('hero-points'), 14, 20, GREY, 500, 'padding-top:6px;', 'points')
    card_ += al(tk(c['countdown']), L('hero-deadline'), 16, 22, BRICK, 700, 'padding-top:10px;', 'deadline')
    box = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid %s;border-radius:8px;"><tr><td style="padding:18px 20px 18px 20px;">%s</td></tr></table>' % (HAIR, card_)
    b += row(WHITE, '0 40px 18px 40px', box, 'left')
    b += button(tk(c['cta']), L('cta1'), WHITE, ur='cta1') + friction(c['friction'], WHITE, pad='10px 40px 24px 40px')
    b += heroimg('credit', 'A woman tasting pasta straight from a Siraat hammered titanium pan. Your store credit expires [[DEADLINE]]', L('hero-img'), WHITE)
    b += gap(WHITE, 28)
    for p in c['body'][1:]: b += para(tk(p))
    b += quote(c['proof'][0]['quote'], c['proof'][0]['name'], L('review'))
    b += row(WHITE, '22px 40px 0 40px', txt(c['authority'], 16, 25, INK, 600, 'text-align:center;'), 'center')
    b += gifts_grid(us, L('gifts'), WHITE, 'WITH THIS ORDER', None)
    b += grid(us, {k: L('card-' + k) for k in GRID}, 'Use it on anything', CREAM)
    b += row(WHITE, '26px 40px 16px 40px', al(tk(c['final_cta_line']), L('final-line'), 17, 24, BRICK, 700, 'text-align:center;', 'final'), 'center')
    b += button(tk(c['cta']), L('cta2'), WHITE, ur='cta2') + friction(c['friction'], WHITE, pad='10px 40px 4px 40px')
    b += gap(WHITE, 18) + ps(tk(c['ps']), L('ps'))
    b += legal(tk(c['legal']), WHITE, '0 40px 26px 40px')
    return b + TAIL

# ======================================================================= 4 LAST-HOURS (platte brief van Benjamin, uitzondering BRIEF: geen header, minimale footer)
LAST_SOURCE = '1-flash'   # bronmail waarop dit de resend is; ander bron: wijzig en bouw opnieuw (what_ends in copy.json)
LAST_LINK = {'1-flash': DUO, '2-vip-weekend': SALE, '3-credit': SALE, '5-gifts': SALE, '6-draw': SALE}
MINFOOT = ('<tr><td class="lt" style="padding:30px 40px 0 40px;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-top:1px solid %s;font-size:1px;line-height:1px;">&nbsp;</td></tr></table></td></tr>\n'
           '<tr><td class="lt" align="left" style="padding:16px 40px 8px 40px;font-family:%s;font-size:12px;line-height:18px;color:%s;text-align:left;">'
           '<a href="{%% unsubscribe_link %%}" style="color:%s;">Unsubscribe</a> &nbsp;|&nbsp; <a href="{%% manage_preferences_link %%}" style="color:%s;">Manage preferences</a><br>'
           '{{ organization.name }} &middot; {{ organization.full_address }}</td></tr>\n') % (HAIR, SYS, GREY, GREY, GREY)
def last(mkt):
    m = COPY['4-last-hours']; c = m[mkt.upper()]; camp = 'urgency-1108-last-' + mkt
    we = m['what_ends'][LAST_SOURCE][mkt.upper()]
    href = lambda ct: utm(LAST_LINK[LAST_SOURCE], camp, ct)
    check_reviews(c['proof'])
    t = c['plain_text'].replace('{{WHAT_ENDS}}', we[0]).replace('{{WHAT_ENDS_SHORT}}', we[1]).replace('{{AFTER}}', we[2])
    x = ('Bron: %s (LAST_SOURCE in make_urg.py). Platte brief, geen header en geen logo, minimale footer (BRIEF; CLAUDE.md noemt deze uitzondering nog alleen voor affiliate en Mystery Gift: '
         'Floris laten bevestigen en in DECISIONS zetten). Antwoordadres moet een gelezen inbox zijn. Hero urg-last-hours-hero.jpg bewust niet gebruikt (UX-spec 3: geen beeld in de brief).') % LAST_SOURCE
    pre = tk(c['preview'])
    b = head(meta('urg-last-' + mkt, mkt.upper(), m, c, x), tk(c['subject_a']), pre).replace('<table role="presentation" class="w" width="600"', '<table role="presentation" class="w" width="560"').replace('width:600px;max-width:600px;background:#FFFFFF;', 'width:560px;max-width:560px;background:#FFFFFF;')
    b = b.replace("@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');", '')
    paras = [p.strip() for p in t.split('\n\n')]
    S = 'font-family:%s;font-size:17px;line-height:26px;color:%s;' % (SYS, INK)
    linkline = lambda txt_, ct: ('<tr><td class="lt" style="padding:0 40px 14px 40px;%s"><a href="%s" data-urg="%s" style="display:inline-block;padding:12px 0;font-family:%s;font-size:18px;line-height:22px;font-weight:700;color:%s;text-decoration:underline;">%s</a></td></tr>\n') % (S, href(ct), ct, SYS, BRICK, txt_)
    out = ''
    for i, p in enumerate(paras):
        p = tk(p)
        if p.startswith('Here&#39;s the link') or p.startswith("Here's the link"):
            first, _ = p.split('\n', 1)
            out += '<tr><td class="lt" style="padding:0 40px 0 40px;%s">%s</td></tr>\n' % (S, first)
            out += linkline('&rarr; Take me to the sale', 'link2')
            continue
        p = p.replace('\n', '<br>')
        if p.startswith(tk(we[0])[:12]):  # de deadline-zin: mag vet (UX-spec 3)
            p = '<b data-urg="deadline">%s</b>' % p
        pad = '24px 40px 14px 40px' if i == 0 else '0 40px 14px 40px'
        out += '<tr><td class="lt" style="padding:%s;%s">%s</td></tr>\n' % (pad, S, p)
        if 'That&#39;s the whole change' in p or "That's the whole change" in p:
            out += linkline('&rarr; See it before it ends', 'link1')   # link 1 in het eerste scherm (UX-spec 3, regel 4)
    b += out + MINFOOT + '\n</table>\n</td></tr>\n</table>\n</body>\n</html>\n'
    return b

# ======================================================================= 5 GIFTS (donker, giftstrook in het eerste scherm)
def gifts(mkt):
    m = COPY['5-gifts']; c = m[mkt.upper()]; us = mkt == 'us'; camp = 'urgency-1108-gifts-' + mkt
    L = lambda ct: utm(SALE, camp, ct)
    check_reviews(c['proof'])
    b = head(meta('urg-gifts-' + mkt, mkt.upper(), m, c), subj(c), tk(c['preview']))
    b += topbar('Your free gifts end [[DEADLINE_CAPS]]', L('topbar'))
    inner = eyebrow(c['eyebrow'], L('hero-eyebrow'), True)
    inner += h1('%s<br>%s' % (c['hero_line1'], tk(c['hero_line2'])), L('hero-kop'), '#FFFFFF')
    inner += al(c['subline'], L('hero-offer'), 17, 24, SOFT, 600, 'padding:8px 0 16px 0;', 'offer')
    inner += gifts_strip(us, L('hero-gifts'))
    inner += al(tk(c['countdown']), L('hero-deadline'), 16, 22, '#FFFFFF', 700, 'padding-top:14px;', 'deadline')
    b += row(INK, '26px 40px 20px 40px', inner, 'left')
    b += button(c['cta'], L('cta1'), INK, True, ur='cta1') + friction(c['friction'], INK, True, '10px 40px 22px 40px')
    b += heroimg('gifts', 'A woman opening a gift box next to a PFAS water filter and a Siraat hammered titanium pan. Gifts end [[DEADLINE]]', L('hero-img'), INK)
    b += gap(WHITE, 26) + para(tk(c['body'][0]))
    b += gifts_grid(us, L('gifts'), WHITE, 'WHAT SHIPS WITH YOUR ORDER', None, 'Mystery gift stays a surprise. The filter is a chance to win in our weekly draw.')
    for p in c['body'][2:]: b += para(tk(p))
    b += button(c['cta'], L('cta2'), WHITE, pad='6px 40px 0 40px', ur='cta2') + friction(c['friction'], WHITE, pad='10px 40px 26px 40px')
    b += quote(c['proof'][0]['quote'], c['proof'][0]['name'], L('review'))
    b += grid(us, {k: L('card-' + k) for k in GRID}, 'Pick anything, the gifts come with it', WHITE)
    b += para(c['authority'], WHITE, '6px 40px 6px 40px', 15, 23, '#4A4A4A')
    b += row(CREAM, '26px 40px 16px 40px', al(tk(c['final_cta_line']), L('final-line'), 17, 24, BRICK, 700, 'text-align:center;', 'final'), 'center')
    b += button(c['cta'], L('cta3'), CREAM, pad='0 40px 26px 40px', ur='cta3')
    b += gap(WHITE, 22) + ps(tk(c['ps']), L('ps'))
    return b + TAIL

# ======================================================================= 6 DRAW (licht, juridische regel bij de knop)
def draw(mkt):
    m = COPY['6-draw']; c = m[mkt.upper()]; us = mkt == 'us'; camp = 'urgency-1108-draw-' + mkt
    L = lambda ct: utm(SALE, camp, ct)
    check_reviews(c['proof'])
    x = 'BLOKKEREND: niet verzenden zonder officiele regels online ([[DRAW_RULES_URL]]). "Full rules" is de enige tweede bestemming (UX-spec 1.3).'
    b = head(meta('urg-draw-' + mkt, mkt.upper(), m, c, x), subj(c), tk(c['preview']))
    b += topbar('Filter draw closes [[DEADLINE_CAPS]]', L('topbar'))
    inner = eyebrow(c['eyebrow'], L('hero-eyebrow'), False)
    inner += h1('%s<br>%s' % (c['hero_line1'], tk(c['hero_line2'])), L('hero-kop'), INK)
    inner += al(c['subline'], L('hero-offer'), 17, 24, '#4A4A4A', 500, 'padding-top:10px;', 'offer')
    inner += al(tk(c['countdown']), L('hero-deadline'), 16, 22, BRICK, 700, 'padding-top:12px;', 'deadline')
    b += row(WHITE, '28px 40px 20px 40px', inner, 'left')
    b += button(c['cta'], L('cta1'), WHITE, ur='cta1')
    rules = 'No purchase necessary. <a href="[[DRAW_RULES_URL]]" data-urg="rules" style="color:%s;text-decoration:underline;font-weight:600;display:inline-block;padding:4px 0;">Official rules</a>' % GREY
    b += row(WHITE, '10px 40px 24px 40px', txt(c['friction'], 13, 18, GREY, 500, 'text-align:center;') + txt(rules, 12, 17, GREY, 400, 'text-align:center;padding-top:6px;'), 'center')
    b += heroimg('draw', 'A man filling a glass from a PFAS water filter while his friend holds up a Siraat pan. This week\'s draw closes [[DEADLINE]]', L('hero-img'), WHITE)
    b += gap(WHITE, 28)
    for p in c['body']: b += para(tk(p))
    b += quote(c['proof'][0]['quote'], c['proof'][0]['name'], L('review'))
    b += gifts_grid(us, L('gifts'), WHITE, 'WITH EVERY ORDER', c['gifts_line'] if not us else 'Plus 4 more gifts with every order <span style="white-space:nowrap;">($555 value in total)</span>')
    b += grid(us, {k: L('card-' + k) for k in GRID}, 'One pan, one entry', CREAM)
    b += row(WHITE, '26px 40px 16px 40px', al(tk(c['final_cta_line']), L('final-line'), 17, 24, BRICK, 700, 'text-align:center;', 'final'), 'center')
    b += button(c['cta'], L('cta2'), WHITE, ur='cta2') + friction(c['friction'], WHITE, pad='10px 40px 4px 40px')
    b += gap(WHITE, 18) + ps(tk(c['ps']), L('ps'))
    lg = tk(c['legal']).replace('Full rules: [[DRAW_RULES_URL]]', 'Full rules: <a href="[[DRAW_RULES_URL]]" style="color:%s;">official rules</a>.' % GREY)
    b += legal(lg, WHITE, '0 40px 26px 40px')
    return b + TAIL

BUILD = {'flash': flash, 'vip': vipmail, 'credit': credit, 'last': last, 'gifts': gifts, 'draw': draw}
BAD = ('next batch', 'reserve', 'coming', 'price held', 'pending order', 'no extensions', 'purifier', 'free filter', 'lifetime', 'for life',
       'risk-free', 'money-back', 'free returns', 'shop now', 'learn more', 'buy now', 'delve', 'unlock', 'elevate', 'journey', 'seamless', "don't miss",
       'while supplies last', 'a real person reads', 'scratch-proof')

def build_all():
    # urls voor build_template: sociale iconen + hero's (na upload KLAVIYO_URL, anders duidelijk token UPLOAD-PENDING)
    urls = os.path.join(T, 'klaviyo-urls.txt')
    open(urls, 'w').write(''.join('%s %s\n' % kv for kv in SOCIAL.items()) + ''.join('%s %s\n' % (f, KLAVIYO_URL[f] or 'UPLOAD-PENDING:' + f) for f in HERO.values()))
    shared = os.path.join(T, 'shared-urls.txt'); open(shared, 'w').write('gift-cookbook.jpg %s\n' % COOKBOOK)
    for f in SOCIAL:  # preview: footer-iconen lokaal naast de hero's
        s = os.path.join(ROOT, 'klaviyo/templates/v3/bfcm/november-v2/assets', f)
        if not os.path.exists(os.path.join(A, f)): shutil.copy(s, A)
    BT = os.path.join(ROOT, 'scripts/build_template.py')
    for key, fn in BUILD.items():
        for mkt in ('us', 'int'):
            mid = 'urg-%s-%s' % (key, mkt); v = fn(mkt)
            body = v.split('-->', 1)[1]
            assert '—' not in v and '–' not in v, (mid, 'streepje')
            plain = html.unescape(re.sub(r'<[^>]+>', ' ', body)).lower()
            for bad in BAD: assert not re.search(r'\b%s\b' % re.escape(bad), plain), (mid, bad)
            if mkt == 'int': assert '$' not in re.sub(r'\{%.*?%\}', '', body), (mid, 'valuta in INT')
            assert '{{DEADLINE' not in body and '{{CREDIT' not in body, (mid, 'ruwe copy-placeholder')
            src = os.path.join(N, mid + '.html'); open(src, 'w').write(v)
            r = subprocess.run([sys.executable, '-I', BT, src, A, urls, '--shared-urls=' + shared], capture_output=True, text=True, cwd='/tmp')
            if r.returncode: sys.exit('%s BUILD %s %s' % (mid, r.stderr[-800:], r.stdout[-300:]))
            k = os.path.join(N, mid + '.klaviyo.html'); kh = fill(open(k).read(), caps(VALUES)); open(k, 'w').write(kh)
            p = os.path.join(N, mid + '-preview.html'); ph = fill(open(p).read(), caps(SAMPLE)); open(p, 'w').write(ph)
            left = sorted(set(re.findall(r'\[\[(\w+)\]\]', open(k).read())))
            print('geschreven', mid, '%.0f KB' % (os.path.getsize(k) / 1024), '| tokens nog open:', ','.join(left) or 'geen')

if __name__ == '__main__':
    build_all()
