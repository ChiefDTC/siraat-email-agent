"""Roasting Pan INT-lancering (Floris, 1 nov 2026): campagne "NEW IN STOCK" + "BLACK FRIDAY SPECIAL", 3 varianten.
Visuele referentie: de productpagina https://siraatskitchen.com/products/titanium-hammered-roasting-pan ("gewoon als die"):
Inter (koppen 600, tekst 400/500), ink #272727, crème #F6F4F0 / #F7F2EC (packshot), haarlijn #E9E9E9, gouden ruitjes,
zwarte BF-pil, rode SAVE-pil, gele topbalk. De serif uit de PDP-galerijbeelden (gebakken in de beelden, niet in de CSS)
is live tekst in Instrument Serif met 'Times New Roman' als terugval.
Vaste header (lockup) en footer via build_template.py. Prijzen per markt via {{PRICE:roast}} / {{WAS:roast}} (catalogus 1 nov bijgewerkt).
Gebruik (vanuit /tmp): python3 -I make_roast.py. Daarna render_roast.py en shot_roast.js."""
import os, re
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INK, CREAM, PACK, ESP, HAIR, GOLD, RED, Y, GREY = '#272727', '#F6F4F0', '#F7F2EC', '#3A2D25', '#E9E9E9', '#B8862B', '#C8202A', '#FFB800', '#5E5A54'
FF = "Inter,Arial,Helvetica,sans-serif"
SERIF = "'Instrument Serif','Times New Roman',Times,serif"
CDN = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/'
IMG = lambda n, w=1200: CDN + n + '.webp?width=%d&format=pjpg' % w
CROP = lambda n, w=1200, h=780: CDN + n + '.webp?width=%d&height=%d&crop=center&format=pjpg' % (w, h)
PK = 'Roastingpanwithrack'
TURKEY = 'siraat-titanium-hammered-roasting-pan-01-thanksgiving-turkey'
GALLERY = 'siraat-titanium-hammered-roasting-pan-02-titanium-hammered-roasting-pan'
GRAVY = 'siraat-titanium-hammered-roasting-pan-03-stovetop-gravy'
LABS = 'siraat-titanium-hammered-roasting-pan-04-light-labs-pfas-free'
CARVE = 'siraat-titanium-hammered-roasting-pan-07-carving-at-the-table'
RACK = 'siraat-titanium-hammered-roasting-pan-08-v-rack-included-international-cm'
PDP = 'https://siraatskitchen.com/products/titanium-hammered-roasting-pan'
FR = 'Free shipping &middot; 100,000+ customers'
ORANGE = '#D96200'  # niet meer in gebruik: Floris koos daarna voor de BF-badgekleur #FFB800 met ink #272727 tekst (contrast 10,4:1)

def utm(content):
    return PDP + '?utm_source=klaviyo&utm_medium=email&utm_campaign=roasting-int&utm_content=' + content

CSS = '''
    .w{width:100%!important;}
    .pad{padding-left:22px!important;padding-right:22px!important;}
    .padx{padding-left:16px!important;padding-right:16px!important;}
    .navhide{display:none!important;}
    .h1{font-size:40px!important;line-height:42px!important;}
    .h1b{font-size:34px!important;line-height:37px!important;}
    .h2{font-size:30px!important;line-height:34px!important;}
    .now{font-size:40px!important;line-height:42px!important;}
    .lead{font-size:16px!important;line-height:25px!important;}
    .col{display:block!important;width:100%!important;padding-left:0!important;padding-right:0!important;}
    .colgap{padding-bottom:10px!important;}
    .bf{font-size:24px!important;line-height:28px!important;}
    .big{font-size:76px!important;line-height:76px!important;letter-spacing:-3px!important;}
    .big2{font-size:64px!important;line-height:64px!important;letter-spacing:-2px!important;}
'''
def head(meta, title, pre):
    return '''<!--
ROASTING PAN INT · NEW IN STOCK + BLACK FRIDAY SPECIAL (concept 1 nov 2026, niet in Klaviyo, niets live).
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
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap');
  body{margin:0;padding:0;background:#FFFFFF;-webkit-text-size-adjust:100%%;}
  table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}
  img{border:0;display:block;line-height:100%%;outline:none;text-decoration:none;}
  a{color:#272727;}
  @media only screen and (max-width:620px){%s  }
</style>
</head>
<body style="margin:0;padding:0;background:#FFFFFF;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">%s</div>
<!-- MARKET-SIGNAL: profile -->
<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF">
<tr><td align="center" style="padding:8px 0 32px 0;">
''' % (meta.strip(), title, CSS, pre)
TAIL = '\n{{FOOTER}}\n\n</table>\n</td></tr>\n</table>\n</body>\n</html>\n'
def OPEN(bg='#FFFFFF'):
    return ('<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:%s;" bgcolor="%s">\n\n' % (bg, bg)
            + '{{BLOCK:bf-topbar text="BLACK FRIDAY SALE IS LIVE" bg="#FFB800" color="#272727"}}\n{{HEADER}}\n')

def row(bg, pad, inner, align='left', cls='pad'):
    return '<tr><td class="%s" align="%s" bgcolor="%s" style="background-color:%s;padding:%s;text-align:%s;">%s</td></tr>\n' % (cls, align, bg, bg, pad, align, inner)
def txt(t, size=16, lh=25, color=INK, weight=400, extra=''):
    return '<div style="font-family:%s;font-size:%dpx;line-height:%dpx;color:%s;font-weight:%d;%s">%s</div>' % (FF, size, lh, color, weight, extra, t)
def serif(t, size=46, lh=50, color=INK, cls='h1', italic=False, extra=''):
    return '<div class="%s" style="font-family:%s;font-size:%dpx;line-height:%dpx;font-weight:400;%scolor:%s;letter-spacing:-0.5px;%s">%s</div>' % (cls, SERIF, size, lh, 'font-style:italic;' if italic else '', color, extra, t)
def pill(t, bg=INK, fg='#FFFFFF', center=True, size=11):
    al = 'align="center" style="margin:0 auto;"' if center else ''
    return '<table role="presentation" %s cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="%s" style="background-color:%s;border-radius:3px;padding:7px 11px;font-family:%s;font-size:%dpx;line-height:12px;letter-spacing:1.4px;font-weight:600;color:%s;white-space:nowrap;text-transform:uppercase;">%s</td></tr></table>' % (al, bg, bg, FF, size, fg, t)
def img(src, alt, url=None, w=600, radius=0):
    i = '<img src="%s" width="%d" alt="%s" style="display:block;width:100%%;max-width:%dpx;height:auto;border:0;%s">' % (src, w, alt, w, ('border-radius:%dpx;' % radius) if radius else '')
    return '<a href="%s" style="text-decoration:none;">%s</a>' % (url, i) if url else i
def gap(bg, h=24):
    return '<tr><td bgcolor="%s" style="background-color:%s;height:%dpx;line-height:%dpx;font-size:0;">&nbsp;</td></tr>\n' % (bg, bg, h, h)

def button(label, url, bg, pad='22px 40px 28px 40px', sub=FR, frame=False, dark=False, fill=None, fg='#FFFFFF'):
    """PDP-knop: ink, witte tekst, hoofdletters, pilvorm. frame=True: geel kader zoals het 'Early access'-blok op de PDP."""
    a = ('<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="%s" style="height:58px;v-text-anchor:middle;width:380px;" arcsize="50%%" stroke="f" fillcolor="%s"><center style="color:%s;font-family:Arial,sans-serif;font-size:15px;font-weight:bold;">%s</center></v:roundrect><![endif]-->'
         '<!--[if !mso]><!--><a href="%s" style="display:block;padding:20px 18px;font-family:%s;font-size:15px;line-height:18px;font-weight:700;letter-spacing:1.2px;color:%s;text-decoration:none;text-transform:uppercase;">%s &rarr;</a><!--<![endif]-->') % (
        url, fill or ('#FFFFFF' if dark else INK), (fg if fill else '#FFFFFF'), label, url, FF, fg if fill else (INK if dark else '#FFFFFF'), label)
    b = '<table role="presentation" width="380" cellpadding="0" cellspacing="0" border="0" style="width:100%%;max-width:380px;margin:0 auto;"><tr><td align="center" bgcolor="%s" style="background-color:%s;border-radius:30px;">%s</td></tr></table>' % (
        fill or ('#FFFFFF' if dark else INK), fill or ('#FFFFFF' if dark else INK), a)
    if frame:
        b = '<table role="presentation" width="420" cellpadding="0" cellspacing="0" border="0" style="width:100%%;max-width:420px;margin:0 auto;"><tr><td bgcolor="%s" style="background-color:%s;border:2px solid %s;border-radius:36px;padding:4px;">%s</td></tr></table>' % (INK, INK, Y, b)
    s = txt(sub, 13, 19, '#C9C2B6' if dark else GREY, 500, 'padding-top:12px;') if sub else ''
    return row(bg, pad, b + s, 'center')

# Prijs per markt. Markten zonder vaste prijslijst (HK, Midden-Oosten, CH, SE, JP, NO) krijgen alleen "70% OFF".
def price(size=46, center=True, dark=False):
    nc = '#FFFFFF' if dark else INK; wc = '#9E978C' if dark else '#B5B5B5'
    al = 'align="center" style="margin:0 auto;"' if center else ''
    priced = ('<table role="presentation" %s cellpadding="0" cellspacing="0" border="0"><tr>'
              '<td valign="middle" class="now" style="padding-right:12px;font-family:%s;font-size:%dpx;line-height:%dpx;font-weight:600;letter-spacing:-1px;color:%s;white-space:nowrap;">{{PRICE:roast}}</td>'
              '<td valign="middle" style="padding-right:12px;font-family:%s;font-size:20px;line-height:22px;font-weight:600;color:%s;text-decoration:line-through;white-space:nowrap;">{{WAS:roast}}</td>'
              '<td valign="middle"><span style="display:inline-block;background-color:%s;color:#FFFFFF;font-family:%s;font-size:12px;line-height:14px;font-weight:700;letter-spacing:0.6px;padding:6px 9px;border-radius:3px;white-space:nowrap;">70%% OFF</span></td>'
              '</tr></table>') % (al, FF, size, size + 2, nc, FF, wc, RED, FF)
    unpriced = '<div class="now" style="font-family:%s;font-size:%dpx;line-height:%dpx;font-weight:600;letter-spacing:-1px;color:%s;">70%% off</div>' % (FF, size, size + 2, nc)
    return '{{IF:PRICED}}' + priced + '{{ELSE}}' + unpriced + '{{ENDIF}}'

def diamonds(items, bg='#FFFFFF', title='', boxed=True, pad='0 20px 20px 20px'):
    """PDP-blok 'Why a titanium roaster': ink kader 1px, radius 10, gouden ruitjes."""
    r = ''.join(('<tr><td width="24" valign="top" style="padding:5px 0 0 0;"><div style="width:9px;height:9px;background-color:%s;transform:rotate(45deg);-webkit-transform:rotate(45deg);font-size:0;line-height:0;">&nbsp;</div></td>'
                 '<td valign="top" style="padding:0 0 14px 0;">%s%s</td></tr>') % (GOLD, txt(t, 16, 22, INK, 600), txt(d, 15, 22, '#4A4A4A', 400, 'padding-top:2px;')) for t, d in items)
    t = txt(title, 16, 22, INK, 600, 'padding-bottom:14px;') if title else ''
    inner = t + '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % r
    if boxed:
        inner = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid %s;border-radius:10px;"><tr><td style="padding:20px 20px 8px 20px;">%s</td></tr></table>' % (INK, inner)
    return row(bg, pad, inner, 'left', 'padx')

def trust(bg='#FFFFFF', pad='0 20px 24px 20px'):
    """PDP-raster 2x2 met haarlijn-kaartjes. Alleen toegestane claims (geen 'free returns', geen levertijd)."""
    cell = lambda a, b: '<td width="50%%" valign="top" style="padding:0 5px 10px 5px;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid #E4DED3;border-radius:6px;"><tr><td align="center" style="padding:14px 10px;">%s%s</td></tr></table></td>' % (
        txt(a, 14, 19, INK, 500, 'text-align:center;'), txt(b, 12, 17, '#8A847A', 400, 'text-align:center;padding-top:3px;'))
    t = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>%s%s</tr><tr>%s%s</tr></table>' % (
        cell('Tested PFAS-free', 'Light Labs report 25895'), cell('75-year warranty', 'Covered for 75 years'),
        cell('Free shipping', 'Duties paid'), cell('30-day returns', 'Unused, within 30 days')))
    return row(bg, pad, t, 'center', 'padx')

# Echte Trustpilot-reviews, letterlijk uit content/reviews/sets.json (5 sterren, gecontroleerd in top.md). Geen roasting-pan-reviews
# beschikbaar, dus de kop zegt eerlijk dat het over Siraat-titanium gaat.
REV = {'R399': ('My deliveries were prompt and I live in Melbourne, Australia... I love their titanium cookware', 'Anthony'),
       'R011': ('We have purchased twice from Siraat... Expensive but definitely Value for money. Quality cookware!', 'Lorraine'),
       'R014': ('I purchased their titanium wok a few months ago and it performs exactly as expected.', 'Caliann')}
def reviews(ids, bg=CREAM, title='In their words', pad='30px 20px 26px 20px'):
    h = txt('<span style="color:%s;letter-spacing:3px;">&#9733;&#9733;&#9733;&#9733;&#9733;</span>' % GOLD, 18, 22, INK, 400, 'text-align:center;')
    h += txt(title, 15, 22, INK, 600, 'text-align:center;padding-top:4px;')
    cards = ''
    for k in ids:
        q, n = REV[k]
        cards += '<tr><td style="padding:12px 0 0 0;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border-radius:10px;"><tr><td style="padding:18px 20px;">%s%s%s</td></tr></table></td></tr>' % (
            txt('&#9733;&#9733;&#9733;&#9733;&#9733;', 13, 15, GOLD, 400, 'letter-spacing:2px;'), txt('&ldquo;%s&rdquo;' % q, 16, 24, INK, 500, 'padding-top:8px;'),
            txt('%s &middot; Verified buyer' % n, 13, 18, '#8A847A', 500, 'padding-top:8px;'))
    h += '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % cards
    h += txt('100,000+ happy customers, on the same titanium cooking surface', 13, 19, '#8A847A', 500, 'text-align:center;padding-top:14px;')
    return row(bg, pad, h, 'left', 'padx')

def included(bg='#FFFFFF', pad='0 20px 24px 20px', gifts='{{GIFTS:total}}'):
    li = lambda a, b: '<tr><td valign="top" style="padding:12px 0;border-bottom:1px solid %s;">%s</td><td align="right" valign="top" style="padding:12px 0 12px 10px;border-bottom:1px solid %s;">%s</td></tr>' % (
        HAIR, txt(a, 15, 21, INK, 500), HAIR, txt(b, 13, 21, '#8A847A', 600, 'white-space:nowrap;'))
    t = txt("WHAT&rsquo;S INCLUDED", 13, 18, INK, 600, 'letter-spacing:1.2px;padding-bottom:4px;')
    t += '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid %s;">%s%s%s%s</table>' % (
        HAIR, li('Titanium Hammered Roasting Pan', 'In its protective box'), li('Fitted V-rack', '33.5 &times; 23.5 &times; 10 cm'),
        li('5 essential guides', 'Care and cooking'), li('With every order', gifts))
    return row(bg, pad, t, 'left', 'padx')

def P(t, bg='#FFFFFF', pad='0 40px 18px 40px', size=17, lh=27, color='#2E2E2E'):
    return row(bg, pad, txt(t, size, lh, color), 'left', 'pad lead')
def sign(bg='#FFFFFF'):
    return row(bg, '4px 40px 30px 40px', txt('Benjamin', 17, 24, INK, 700) + txt('Founder, Siraat', 14, 20, '#8A847A'), 'left', 'pad')
def meta(id_, sender, subj, pre, when, who, why):
    return 'ID: %s\nSENDER: %s\nSUBJECT A: %s\nSUBJECT B: %s\nPREVIEW A: %s\nPREVIEW B: %s\nWANNEER: %s\nWIE/FILTERS: %s\nWAAROM: %s' % (id_, sender, subj[0], subj[1], pre[0], pre[1], when, who, why)

WHO = ('Campagne-segment INT: e-mailabonnees met profielland bekend en niet US (Klaviyo: Country is set, not United States), '
       'engaged 90 dagen; uitsluiten: Placed Order laatste 7 dagen, ooit een order met de Titanium Hammered Roasting Pan (Items contains Roasting), suppressed. Smart sending aan.')
files = {}

# =====================================================================
# A · Bold BF launch
m = meta('roast-int-a · Bold BF launch', 'Siraat',
         ('NEW IN STOCK: the titanium roasting pan', 'Black Friday special: 70% off the roaster'),
         ('Just arrived, with its Black Friday price on day one.', 'Pure titanium, no coatings. Rack included.'),
         'wo 4 nov, 08:15 lokale tijd (lege dag; v2-letter schuift voor INT naar 13 nov)', WHO,
         'Nieuws plus aanbod in één beeld: wat het is, wat het kost, waarom het blijft. PDP-stijl, BF-prijs zoals op de PDP.')
c = 'roasting-int'
b = head(m, 'NEW IN STOCK: the titanium roasting pan', 'Just arrived, with its Black Friday price on day one.') + OPEN()
b += row(PACK, '30px 24px 0 24px', '<table role="presentation" align="center" style="margin:0 auto;" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right:6px;">%s</td><td>%s</td></tr></table>' % (pill('New in stock'), pill('Black Friday &nbsp;|&nbsp; 70% off', Y, INK)), 'center')
b += row(PACK, '18px 24px 0 24px', serif('The Titanium Hammered<br>Roasting Pan', 48, 50, INK, 'h1', True), 'center')
b += row(PACK, '12px 40px 0 40px', txt('Just arrived outside the US. A pure titanium roasting surface, hand-hammered, no coatings.', 17, 26, '#4A4A4A', 400, 'text-align:center;'), 'center')
b += row(PACK, '10px 0 0 0', img(CROP(PK), 'The Titanium Hammered Roasting Pan with its fitted V-rack', utm('a-hero')), 'center', '')
b += row(INK, '16px 20px', txt('BLACK FRIDAY SPECIAL', 13, 16, Y, 700, 'letter-spacing:2.4px;text-align:center;'), 'center', 'padx')
b += row('#FFFFFF', '24px 20px 0 20px', price(52), 'center', 'padx')
b += row('#FFFFFF', '10px 30px 0 30px', txt('Black Friday price from day one. No code needed. Plus {{GIFTS:total}} with every order.', 15, 23, GREY, 500, 'text-align:center;'), 'center')
b += button('Get my roasting pan', utm('a-cta1'), '#FFFFFF', '22px 30px 30px 30px')
b += diamonds([('No coatings, no PFAS', 'A pure titanium roasting surface. The same titanium surface as our pans, tested PFAS-free by Light Labs, report no. 25895.'),
               ('Roast it, then make the gravy in it', 'Works on the stovetop too, induction included. Deglaze while it is warm and the drippings lift right off.'),
               ('Covered for 75 years', 'Dents, a warped base, a loose handle or rivet. Nothing on it to wear off, so we can promise that.')],
              '#FFFFFF', 'Why a titanium roaster')
b += row('#FFFFFF', '0 20px 24px 20px', img(IMG(TURKEY), 'A golden roast on the V-rack in the Siraat roasting pan on a holiday table', utm('a-turkey'), 560, 10), 'center', 'padx')
b += included()
b += reviews(['R399', 'R011'], CREAM, 'What customers say about Siraat titanium')
b += gap('#FFFFFF', 24) + trust()
b += row('#FFFFFF', '0 20px 0 20px', price(40), 'center', 'padx')
b += button('Get my roasting pan', utm('a-cta2'), '#FFFFFF', '20px 30px 34px 30px')
files['roast-int-a'] = b + TAIL

# A2 · variant A zonder bedragen (Floris, 1 nov avond): geen {{PRICE}}/{{WAS}}/{{GIFTS:total}}, één grote "70% OFF" in BF-geel.
def bigoff(size=104, cls='big', sub='Black Friday price from day one. No code needed.', pad='26px 20px 30px 20px', label=True):
    h = txt('BLACK FRIDAY SPECIAL', 13, 16, Y, 700, 'letter-spacing:2.4px;text-align:center;padding-bottom:10px;') if label else ''
    h += '<div class="%s" style="font-family:%s;font-size:%dpx;line-height:%dpx;font-weight:900;letter-spacing:-4px;color:%s;text-align:center;">70%% OFF</div>' % (cls, FF, size, size - 2, Y)
    h += txt(sub, 16, 24, '#E6E3DC', 500, 'text-align:center;padding-top:12px;')
    return row(INK, pad, h, 'center', 'padx')
m = meta('roast-int-a2 · Bold BF launch zonder bedragen (vervangt A)', 'Siraat',
         ('NEW IN STOCK: the titanium roasting pan', 'Black Friday special: 70% off the roaster'),
         ('Just arrived, with its Black Friday price on day one.', 'Pure titanium, no coatings. Rack included.'),
         'wo 4 nov, 08:15 lokale tijd', WHO,
         'Keuze Floris: variant A, zonder valuta-bedragen (overal gelijk), grote 70% OFF in BF-geel.')
b = head(m, 'NEW IN STOCK: the titanium roasting pan', 'Just arrived, with its Black Friday price on day one.') + OPEN()
b += row(PACK, '30px 24px 0 24px', '<table role="presentation" align="center" style="margin:0 auto;" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right:6px;">%s</td><td>%s</td></tr></table>' % (pill('New in stock'), pill('Black Friday &nbsp;|&nbsp; 70% off', Y, INK)), 'center')
b += row(PACK, '18px 24px 0 24px', serif('The Titanium Hammered<br>Roasting Pan', 48, 50, INK, 'h1', True), 'center')
b += row(PACK, '12px 40px 0 40px', txt('Just arrived in our warehouse. A pure titanium roasting surface, hand-hammered, no coatings.', 17, 26, '#4A4A4A', 400, 'text-align:center;'), 'center')
b += row(PACK, '10px 0 0 0', img(CROP(PK), 'The Titanium Hammered Roasting Pan with its fitted V-rack', utm('a2-hero')), 'center', '')
b += bigoff(sub='Black Friday price from day one. No code needed.<br>Plus free gifts with every order.')
b += button('Get my roasting pan', utm('a2-cta1'), '#FFFFFF', '26px 30px 30px 30px', fill=Y, fg=INK)
b += diamonds([('No coatings, no PFAS', 'A pure titanium roasting surface. The same titanium surface as our pans, tested PFAS-free by Light Labs, report no. 25895.'),
               ('Roast it, then make the gravy in it', 'Works on the stovetop too, induction included. Deglaze while it is warm and the drippings lift right off.'),
               ('Covered for 75 years', 'Dents, a warped base, a loose handle or rivet. Nothing on it to wear off, so we can promise that.')],
              '#FFFFFF', 'Why a titanium roaster')
b += row('#FFFFFF', '0 20px 24px 20px', img(IMG(TURKEY), 'A golden roast on the V-rack in the Siraat roasting pan on a holiday table', utm('a2-turkey'), 560, 10), 'center', 'padx')
b += included(gifts='Free gifts')
b += reviews(['R399', 'R011'], CREAM, 'What customers say about Siraat titanium')
b += gap('#FFFFFF', 24) + trust()
b += bigoff(80, 'big2', 'Black Friday price. No code needed.', '24px 20px 26px 20px', False)
b += button('Get my roasting pan', utm('a2-cta2'), '#FFFFFF', '24px 30px 34px 30px', fill=Y, fg=INK)
files['roast-int-a2'] = b + TAIL
assert not re.search(r'\{\{(PRICE|WAS|GIFTS)', files['roast-int-a2'])

# =====================================================================
# B · Editorial PDP style
m = meta('roast-int-b · Editorial PDP-stijl', 'Siraat',
         ('Roast it. Then make the gravy in it.', 'The roasting pan, rebuilt in titanium'),
         ('New in stock, and 70% off for Black Friday.', 'No coating to flake at roasting heat. Now in stock.'),
         'vr 6 nov, 08:15 lokale tijd (alternatief voor A, of als tweede verzending naar INT-niet-openers van A)', WHO,
         'Verhaal eerst (probleem met gecoate en stalen braadsledes, het mechanisme), dan hard aanbod. Galerijstijl van de PDP: espresso, serif.')
b = head(m, 'Roast it. Then make the gravy in it.', 'New in stock, and 70% off for Black Friday.') + OPEN()
b += row('#FFFFFF', '0', img(IMG(CARVE), 'Carving the holiday roast right in the Siraat titanium roasting pan at the table', utm('b-hero')), 'center', '')
b += row(ESP, '34px 24px 0 24px', pill('New in stock', '#FFFFFF', INK), 'center')
b += row(ESP, '18px 24px 0 24px', serif('Roast it.<br><i>Then make the<br>gravy in it.</i>', 46, 50, '#FFFFFF'), 'center')
b += row(ESP, '14px 40px 30px 40px', txt('The roasting pan, rebuilt in titanium. Just arrived outside the US, and 70% off for Black Friday.', 17, 26, '#E6DED3', 400, 'text-align:center;'), 'center')
b += P('Most roasters ask you to pick a problem. A coated one scratches and flakes, and a roast is the hottest job you give it. A plain steel one is safe, but the drippings burn on and you spend the evening soaking it.', '#FFFFFF', '32px 40px 16px 40px')
b += P('So we built one without either problem. A pure titanium roasting surface with no coatings, hand-hammered. A fitted V-rack that lifts the roast so the heat gets all the way round. And a base that goes straight onto the stovetop, induction included, so the gravy starts in the same pan.')
b += P('It is the same titanium surface as our pans, tested PFAS-free by Light Labs (report no. 25895). Dishwasher safe, rack and all.', '#FFFFFF', '0 40px 24px 40px')
b += row('#FFFFFF', '0 20px 24px 20px', img(IMG(LABS), 'Third-party tested by Light Labs: the Siraat Titanium Hammered Roasting Pan is PFAS-free', utm('b-labs'), 560, 10), 'center', 'padx')
# hard offer block (crème, zoals het prijsblok op de PDP)
ob = pill('Black Friday special', INK, '#FFFFFF')
ob += serif('Titanium Hammered<br>Roasting Pan', 34, 38, INK, 'h1b', False, 'padding-top:16px;')
ob += '<div style="padding-top:14px;">%s</div>' % price(44)
ob += txt('No code needed. Rack, guides and {{GIFTS:total}} included.', 15, 23, GREY, 500, 'text-align:center;padding-top:10px;')
b += row(CREAM, '34px 24px 0 24px', ob, 'center')
b += button('Get mine at 70% off', utm('b-cta1'), CREAM, '22px 30px 32px 30px')
b += gap('#FFFFFF', 24)
b += diamonds([('Nothing on it to wear off', 'Pure titanium cooking surface, no coatings. No PFAS, PFOA, or BPA.'),
               ('Fitted V-rack included', '33.5 &times; 23.5 &times; 10 cm. Lifts the roast for even browning.'),
               ('75-year warranty, 30-day returns', 'Send it back unused within 30 days, or keep it and we cover it for 75 years.')], '#FFFFFF', 'Inside every roaster')
b += reviews(['R014', 'R399'], CREAM, 'In their words')
b += row('#FFFFFF', '30px 24px 0 24px', serif('Roast it this year.', 34, 38, INK, 'h1b'), 'center')
b += button('Get mine at 70% off', utm('b-cta2'), '#FFFFFF', '20px 30px 34px 30px')
files['roast-int-b'] = b + TAIL

# =====================================================================
# C · Brief van Benjamin
m = meta('roast-int-c · Brief van Benjamin', 'Benjamin from Siraat',
         ('It finally arrived outside the US', 'Now in stock: the titanium roaster'),
         ('The titanium roasting pan, with its Black Friday price.', 'One pan for the whole holiday dinner.'),
         'vr 13 nov, 08:15 lokale tijd (lege dag), of di 4 nov als C de enige variant wordt', WHO,
         'Founder-brieven halen 1,3% klik tegenover 0,3 tot 0,6% voor beeldmails (PLAYBOOK 1). Eén beeld, één knop.')
b = head(m, 'It finally arrived outside the US', 'The titanium roasting pan, with its Black Friday price.') + OPEN()
b += P("Hi {{ first_name|default:'there' }},", '#FFFFFF', '34px 40px 14px 40px')
b += P('Benjamin here. Until now, the roasting pan was one of the few pieces we only sold in the US. This week it finally arrived outside the US, and it is in stock now.')
b += P('It is a simple idea: a pure titanium roasting surface with no coatings, hand-hammered, with a fitted V-rack. When the roast comes out, it goes straight onto the stovetop for the gravy. Induction too.')
b += row('#FFFFFF', '6px 40px 0 40px', '<a href="%s" style="text-decoration:none;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%s" style="background-color:%s;border-radius:10px;"><tr><td style="padding:0;">%s</td></tr><tr><td align="center" style="padding:4px 20px 22px 20px;">%s<div style="padding-top:10px;">%s</div></td></tr></table></a>' % (
    utm('c-card'), PACK, PACK, img(CROP(PK, 1040, 676), 'The Titanium Hammered Roasting Pan with its fitted V-rack', None, 520, 10),
    pill('Black Friday special', INK, '#FFFFFF') + txt('Titanium Hammered Roasting Pan', 17, 22, INK, 600, 'text-align:center;padding-top:12px;'), price(34)), 'center', 'pad')
b += P('It launched straight into Black Friday, so you get the sale price from day one, {{GIFTS:total}} with your order, 30 days to send it back unused, and a 75-year warranty.', '#FFFFFF', '24px 40px 6px 40px')
b += button('Get my roasting pan', utm('c-cta'), '#FFFFFF', '16px 40px 24px 40px')
b += P('Not sure it fits your oven? It is 35.5 &times; 27 cm, 43.5 cm with the handles. Reply and our team will help.', '#FFFFFF', '0 40px 12px 40px', 15, 23, GREY) + sign()
files['roast-int-c'] = b + TAIL

for k, v in files.items():
    assert '—' not in v, k
    body = v.split('-->', 1)[1]
    for bad in ('from the US', 'next batch', 'reserve', 'lifetime', 'risk-free', 'free returns', '750', '400&deg;', 'Shop now'):
        assert bad.lower() not in body.lower(), (k, bad)
    open(os.path.join(N, k + '.html'), 'w').write(v)
    print('geschreven', k, len(v))
