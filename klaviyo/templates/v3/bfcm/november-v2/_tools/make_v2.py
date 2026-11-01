"""November v2 (1 nov 2026, na afwijzing v1 door Floris): pure direct response in Black Friday-stijl, Smooche-volume.
Maakt de bronmails in bfcm/november-v2. Gebruik: python3 -I make_v2.py  (vanuit /tmp). Daarna render_v2.py en shot_v2.js.
Plan en tijdlijn: research/smooche/06-volume-plan-smooche.md. Merkregels: vaste header en footer, lockup, Benjamin, 30 dagen retour,
75 jaar garantie, 100,000+ klanten. Voorraad-copy (DECISIONS 1 nov): alleen "Just arrived" en "Selling fast" voor de 6-Pcs en 12-Pcs sets,
nooit "next batch", "reserved" of iets wat nog moet komen. BF-code alleen als placeholder BFCODE en alleen in cart/checkout."""
import os, re
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INK, NIGHT, CREAM, Y, RED = '#272727', '#0E0E0E', '#F8F7F2', '#FFB800', '#C8202A'
FF = 'Inter,Arial,Helvetica,sans-serif'
CDN = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/'
SALE = 'https://siraatskitchen.com/collections/black-friday-sale'
U = {'set12p': 'https://siraatskitchen.com/products/titanium-hammered-cookware-set-12-pcs-free-pizza-steel-1',
     'set6': 'https://siraatskitchen.com/products/titanium-hammered-pan-set-with-lids-6-pcs',
     'standard': 'https://siraatskitchen.com/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern',
     'large': 'https://siraatskitchen.com/products/titanium-hammered-pan-pro-large',
     'mini': 'https://siraatskitchen.com/products/titanium-hammered-pan-pro-mini',
     'deep': 'https://siraatskitchen.com/products/titanium-hammered-deep-pan-pro',
     'wok': 'https://siraatskitchen.com/products/titanium-hammered-wok-pan-pro',
     'report': 'https://siraatskitchen.com/pages/third-party-testing'}
YS = lambda n: CDN + 'siraat-bf-product-%s-yellow.webp?width=600&format=pjpg' % n
EX = lambda n: CDN + 'siraat-collection-exclusive-%s-desktop.jpg?width=1200' % n

def utm(url, camp, content):
    return url + ('&' if '?' in url else '?') + 'utm_source=klaviyo&utm_medium=email&utm_campaign=%s&utm_content=%s' % (camp, content)
def T(s, **kw):
    for k, v in kw.items(): s = s.replace('[[%s]]' % k, v)
    assert '[[' not in s, re.findall(r'\[\[\w+\]\]', s)
    return s

# ---------- skelet ----------
CSS = '''
    .w{width:100%!important;}
    .pad{padding-left:22px!important;padding-right:22px!important;}
    .padx{padding-left:16px!important;padding-right:16px!important;}
    .navhide{display:none!important;}
    .hx{font-size:44px!important;line-height:44px!important;letter-spacing:-1.6px!important;}
    .hxx{font-size:60px!important;line-height:58px!important;letter-spacing:-2.5px!important;}
    .hl{font-size:34px!important;line-height:36px!important;}
    .now{font-size:40px!important;line-height:42px!important;}
    .lead{font-size:16px!important;line-height:25px!important;}
    .tn{font-size:13px!important;line-height:17px!important;}
    .tp{font-size:17px!important;line-height:20px!important;}
    .st{font-size:30px!important;line-height:32px!important;}
'''
def head(meta, title, pre, signal):
    return '''<!--
NOVEMBER V2 · SMOOCHE-VOLUME (concept 1 nov 2026, niet in Klaviyo, niets live). Plan: research/smooche/06-volume-plan-smooche.md.
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
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800;900&display=swap');
  body{margin:0;padding:0;background:#FFFFFF;-webkit-text-size-adjust:100%%;}
  table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}
  img{border:0;display:block;line-height:100%%;outline:none;text-decoration:none;}
  a{color:#272727;}
  @media only screen and (max-width:620px){%s  }
</style>
</head>
<body style="margin:0;padding:0;background:#FFFFFF;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">%s</div>
<!-- MARKET-SIGNAL: %s -->
<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF">
<tr><td align="center" style="padding:8px 0 32px 0;">
''' % (meta.strip(), title, CSS, pre, signal)
TAIL = '\n{{FOOTER}}\n\n</table>\n</td></tr>\n</table>\n</body>\n</html>\n'
def OPEN(bg, top='BLACK FRIDAY SALE IS LIVE', tbg=INK, tfg=Y):
    return ('<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:%s;" bgcolor="%s">\n\n' % (bg, bg)
            + '{{BLOCK:bf-topbar text="%s" bg="%s" color="%s"}}\n{{HEADER}}\n' % (top, tbg, tfg))

def row(bg, pad, inner, align='left', cls='pad', extra=''):
    return '<tr><td class="%s" align="%s" bgcolor="%s" style="background-color:%s;padding:%s;text-align:%s;%s">%s</td></tr>\n' % (cls, align, bg, bg, pad, align, extra, inner)
def txt(t, size=16, lh=25, color=INK, weight=400, extra=''):
    return '<div style="font-family:%s;font-size:%dpx;line-height:%dpx;color:%s;font-weight:%d;%s">%s</div>' % (FF, size, lh, color, weight, extra, t)
def pill(t, bg=Y, fg=INK, center=False):
    al = 'align="center" style="margin:0 auto;"' if center else ''
    return '<table role="presentation" %s cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="%s" style="background-color:%s;border-radius:3px;padding:7px 11px;font-family:%s;font-size:11px;line-height:12px;letter-spacing:1.8px;font-weight:900;color:%s;white-space:nowrap;">%s</td></tr></table>' % (al, bg, bg, FF, fg, t)
def pills(lst, center=False):
    cells = ''.join('<td style="padding:0 6px 6px 0;">%s</td>' % pill(t, b, f) for t, b, f in lst)
    al = 'align="center" style="margin:0 auto;"' if center else ''
    return '<table role="presentation" %s cellpadding="0" cellspacing="0" border="0"><tr>%s</tr></table>' % (al, cells)
def img(src, alt, url=None, radius=0, w=600):
    i = '<img src="%s" width="%d" alt="%s" style="display:block;width:100%%;max-width:%dpx;height:auto;border:0;%s">' % (src, w, alt, w, 'border-radius:%dpx;' % radius if radius else '')
    return '<a href="%s" style="text-decoration:none;">%s</a>' % (url, i) if url else i
def cta(label, url, bg, pad='22px 40px 30px 40px', sub=''):
    s = "<div style='font-family:%s;font-size:12px;line-height:18px;color:%s;padding-top:12px;'>%s</div>" % (FF, '#BDB8AE' if bg in (NIGHT, '#1C1C1C') else '#5E5A54', sub) if sub else ''
    return '{{BLOCK:bf-cta label="%s" url="%s" bg="%s" pad="%s" sub="%s"}}\n' % (label, url, bg, pad, s)
def cta_ink(label, url, bg=Y, pad='22px 40px 30px 40px', sub=''):
    s = txt(sub, 12, 18, INK, 600, 'padding-top:12px;') if sub else ''
    b = ('<table role="presentation" width="360" cellpadding="0" cellspacing="0" border="0" style="width:100%%;max-width:360px;margin:0 auto;"><tr><td align="center" bgcolor="%s" style="background-color:%s;border-radius:30px;">'
         '<a href="%s" style="display:block;padding:20px 20px;font-family:%s;font-size:16px;line-height:18px;font-weight:900;letter-spacing:1.5px;color:%s;text-decoration:none;text-transform:uppercase;">%s &rarr;</a></td></tr></table>') % (INK, INK, url, FF, Y, label)
    return row(bg, pad, b + s, 'center')
def band(t, bg=Y, fg=INK):
    return row(bg, '14px 16px', txt(t, 13, 18, fg, 900, 'letter-spacing:1.6px;text-transform:uppercase;'), 'center', 'padx')
def gap(bg, h=24):
    return '<tr><td bgcolor="%s" style="background-color:%s;height:%dpx;line-height:%dpx;font-size:0;">&nbsp;</td></tr>\n' % (bg, bg, h, h)

# ---------- hero's ----------
def hero_dark(tag, l1, l2, big='70% OFF', pre='UP TO', sub='', label='Shop the sale', url=SALE, fr='', image=None, alt='', hl2=False):
    h = row(NIGHT, '34px 24px 0 24px', pill(tag, center=True), 'center')
    l2h = '<span style="background-color:%s;color:%s;padding:0 8px;">%s</span>' % (Y, INK, l2) if hl2 else l2
    h += row(NIGHT, '20px 16px 0 16px', '<div class="hx" style="font-family:%s;font-size:58px;line-height:58px;font-weight:900;letter-spacing:-2px;color:#FFFFFF;text-transform:uppercase;">%s<br>%s</div>' % (FF, l1, l2h), 'center', 'padx')
    if big:
        h += row(NIGHT, '22px 16px 0 16px', txt(pre, 15, 18, Y, 900, 'letter-spacing:4px;') + '<div class="hxx" style="font-family:%s;font-size:96px;line-height:90px;font-weight:900;letter-spacing:-4px;color:%s;padding-top:2px;">%s</div>' % (FF, Y, big), 'center', 'padx')
    if sub: h += row(NIGHT, '18px 30px 0 30px', txt(sub, 17, 26, '#E6E3DC', 500, 'text-align:center;'), 'center')
    h += cta(label, url, NIGHT, '24px 30px 28px 30px', fr)
    if image: h += row(NIGHT, '0', img(image, alt, url), 'center', '')
    return h
def hero_yellow(tag, l1, l2, sub, label, url, fr='', image=None, alt=''):
    h = row(Y, '34px 24px 0 24px', pill(tag, INK, Y, True), 'center')
    h += row(Y, '18px 16px 0 16px', '<div class="hx" style="font-family:%s;font-size:60px;line-height:58px;font-weight:900;letter-spacing:-2.2px;color:%s;text-transform:uppercase;">%s<br>%s</div>' % (FF, INK, l1, l2), 'center', 'padx')
    if sub: h += row(Y, '18px 30px 0 30px', txt(sub, 17, 26, INK, 600, 'text-align:center;'), 'center')
    h += cta_ink(label, url, Y, '24px 30px %s 30px' % ('24px' if image else '32px'), fr)
    if image: h += row(Y, '0 20px 24px 20px', img(image, alt, url, 10, 560), 'center', 'padx')
    return h

# ---------- productblokken ----------
def price_line(was, now, off, dark=False, big=True):
    wc = '#8C877F' if dark else '#9A948B'; nc = '#FFFFFF' if dark else INK
    ns = 'font-size:48px;line-height:48px;' if big else 'font-size:22px;line-height:24px;'
    return ('<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>'
            '<td valign="middle" style="padding-right:10px;font-family:%s;font-size:%s;line-height:20px;color:%s;text-decoration:line-through;font-weight:600;">%s</td>'
            '<td valign="middle" class="%s" style="padding-right:10px;font-family:%s;%sfont-weight:900;letter-spacing:-1.5px;color:%s;">%s</td>'
            '<td valign="middle"><span style="display:inline-block;background-color:%s;color:%s;font-family:%s;font-size:%s;line-height:14px;font-weight:900;padding:6px 8px;border-radius:3px;white-space:nowrap;">%s</span></td>'
            '</tr></table>') % (FF, '20px' if big else '14px', wc, was, 'now' if big else '', FF, ns, nc, now, Y, INK, FF, '13px' if big else '11px', off)
def deal(bg, image, alt, url, tags, name, desc, was, now, off, bonus='', label='Get this deal', fr='', kicker=''):
    """Grote dealkaart: wit op Night of cream. tags = [(tekst, bg, fg)]"""
    card = '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border-radius:12px;">'
    card += '<tr><td style="padding:0;border-radius:12px 12px 0 0;overflow:hidden;">%s</td></tr>' % img(image, alt, url, 0, 560)
    inner = pills(tags)
    if kicker: inner += txt(kicker, 11, 14, '#727272', 800, 'letter-spacing:1.8px;padding-top:8px;')
    inner += '<div class="hl" style="font-family:%s;font-size:32px;line-height:34px;font-weight:900;letter-spacing:-1px;color:%s;padding-top:6px;"><a href="%s" style="color:%s;text-decoration:none;">%s</a></div>' % (FF, INK, url, INK, name)
    inner += txt(desc, 15, 22, '#5E5A54', 400, 'padding:8px 0 14px 0;')
    inner += price_line(was, now, off)
    card += '<tr><td style="padding:20px 22px 6px 22px;">%s</td></tr>' % inner
    if bonus:
        card += '<tr><td style="padding:12px 22px 4px 22px;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="#FFF3CC" style="background-color:#FFF3CC;border-left:4px solid %s;padding:12px 14px;font-family:%s;font-size:15px;line-height:21px;color:%s;font-weight:800;">%s</td></tr></table></td></tr>' % (Y, FF, INK, bonus)
    s = txt(fr, 12, 18, '#5E5A54', 400, 'padding-top:10px;text-align:center;') if fr else ''
    card += ('<tr><td align="center" style="padding:16px 22px 22px 22px;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" bgcolor="%s" style="background-color:%s;border-radius:30px;">'
             '<a href="%s" style="display:block;padding:18px 16px;font-family:%s;font-size:16px;line-height:18px;font-weight:900;letter-spacing:1.4px;color:%s;text-decoration:none;text-transform:uppercase;">%s &rarr;</a></td></tr></table>%s</td></tr>') % (Y, Y, url, FF, INK, label, s)
    card += '</table>'
    return row(bg, '0 20px 24px 20px', card, 'left', 'padx')
def tile(t, dark):
    tb = '#1C1C1C' if dark else '#FFFFFF'; nc = '#FFFFFF' if dark else INK; wc = '#8C877F' if dark else '#9A948B'
    h = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%s" style="background-color:%s;border-radius:10px;">' % (tb, tb)
    h += '<tr><td style="padding:0;">%s</td></tr>' % img(t['img'], t['name'], t['url'], 10, 270)
    h += '<tr><td style="padding:12px 12px 14px 12px;">'
    h += '<div class="tn" style="font-family:%s;font-size:15px;line-height:19px;font-weight:900;color:%s;"><a href="%s" style="color:%s;text-decoration:none;">%s</a></div>' % (FF, nc, t['url'], nc, t['name'])
    h += '<div style="font-family:%s;font-size:13px;line-height:16px;color:%s;text-decoration:line-through;font-weight:600;padding-top:8px;">%s</div>' % (FF, wc, t['was'])
    h += '<div style="padding-top:2px;"><span class="tp" style="font-family:%s;font-size:22px;line-height:26px;font-weight:900;letter-spacing:-0.6px;color:%s;">%s</span>&nbsp;&nbsp;<span style="display:inline-block;vertical-align:3px;background-color:%s;color:%s;font-family:%s;font-size:11px;line-height:13px;font-weight:900;padding:4px 6px;border-radius:3px;">%s</span></div>' % (FF, nc, t['now'], Y, INK, FF, t['off'])
    h += '</td></tr></table>'
    return h
def grid(bg, tiles, pad='0 20px 12px 20px'):
    dark = bg in (NIGHT,)
    out = ''
    for i in range(0, len(tiles), 2):
        a, b = tiles[i], tiles[i + 1]
        out += row(bg, pad, '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td width="50%%" valign="top" style="padding-right:6px;">%s</td><td width="50%%" valign="top" style="padding-left:6px;">%s</td></tr></table>' % (tile(a, dark), tile(b, dark)), 'left', 'padx')
    return out
TILE = {
 'standard': dict(img=YS('hammered-pan-pro'), name='Pan Pro Standard {{SIZE:28}}', was='{{WAS:standard}}', now='{{PRICE:standard}}', off='-70%', url=U['standard']),
 'large': dict(img=CDN + 'siraat-bf-product-hammered-pan-pro-yellow-tag.webp?width=600&format=pjpg', name='Pan Pro Large {{SIZE:30}}', was='{{WAS:large}}', now='{{PRICE:large}}', off='-70%', url=U['large']),
 'mini': dict(img=YS('hammered-pan-pro-mini'), name='Pan Pro Mini {{SIZE:20}}', was='{{WAS:mini}}', now='{{PRICE:mini}}', off='-70%', url=U['mini']),
 'deep': dict(img=YS('hammered-deep-pan-pro'), name='Deep Pan Pro', was='{{WAS:deep}}', now='<span style="font-size:13px;font-weight:700;letter-spacing:0;">from</span> {{PRICE:deep}}', off='-70%', url=U['deep']),
 'wok': dict(img=YS('hammered-wok-pan-pro'), name='Wok Pan Pro', was='{{WAS:wok}}', now='<span style="font-size:13px;font-weight:700;letter-spacing:0;">from</span> {{PRICE:wok}}', off='-70%', url=U['wok']),
 'small': dict(img=YS('hammered-pan-pro'), name='Pan Pro Small {{SIZE:26}}', was='{{WAS:small}}', now='{{PRICE:small}}', off='-70%', url='https://siraatskitchen.com/products/titanium-hammered-pan-pro-small'),
 'pizza': dict(img=CDN + 'TitaniumHammeredPizzaSteel.webp?width=600&format=pjpg', name='Pizza Steel', was='{{WAS:pizza}}', now='{{PRICE:pizza}}', off='-70%', url='https://siraatskitchen.com/products/titanium-hammered-pizza-steel'),
 'set6': dict(img='{{IMG}}/deal-set6.jpg', name='Pan Set with Lids, 6&nbsp;Pcs', was='{{WAS:set6}}', now='{{PRICE:set6}}', off='-70%', url=U['set6']),
}
JA = ('JUST ARRIVED', Y, INK); SF = ('SELLING FAST', RED, '#FFFFFF')
def deal_main(bg, camp, content, label='Get the 12-piece deal', fr='Free shipping &middot; 100,000+ customers'):
    """US: 12-Pcs met gratis Pizza Steel. Elders: 6-Pcs (12-Pcs is US-only)."""
    us = deal(bg, '{{IMG}}/deal-set12-pizza.jpg', 'Titanium Hammered Cookware Set, 12 Pcs, with a free Pizza Steel', utm(U['set12p'], camp, content + '-set12'), [JA, SF],
              'Cookware Set, 12&nbsp;Pcs', '3 pans, 2 saucepans, a stockpot and 6 fitted lids. A whole kitchen with a pure titanium cooking surface, no coatings.',
              '{{WAS:set12}}', '{{PRICE:set12}}', '-68%', '+ FREE Pizza Steel ($664 value) with this set', label, fr, 'THE COMPLETE SET')
    intl = deal(bg, '{{IMG}}/deal-set6.jpg', 'Titanium Hammered Pan Set with Lids, 6 Pcs', utm(U['set6'], camp, content + '-set6'), [JA, SF],
                'Pan Set with Lids, 6&nbsp;Pcs', 'Pan Pro Mini, Small and Large, each with its own fitted lid. Pure titanium cooking surface, no coatings.',
                '{{WAS:set6}}', '{{PRICE:set6}}', '-70%', '+ {{GIFTS:total}} with every order', label.replace('12-piece', '6-piece'), fr, 'THE STARTER SET')
    return '{{USONLY}}\n%s{{ELSEUS}}\n%s{{/USONLY}}\n' % (us, intl)
def tiles_for(camp, content, keys_us, keys_int):
    def mk(keys):
        return [dict(TILE[k], url=utm(TILE[k]['url'], camp, content + '-' + k)) for k in keys]
    return mk(keys_us), mk(keys_int)
def grid_mkt(bg, camp, content, keys_us=('set6', 'standard', 'wok', 'deep'), keys_int=('standard', 'wok', 'deep', 'small')):
    a, b = tiles_for(camp, content, keys_us, keys_int)
    return '{{USONLY}}\n%s{{ELSEUS}}\n%s{{/USONLY}}\n' % (grid(bg, a), grid(bg, b))

# ---------- bewijs, garantie, stack ----------
REV = {  # letterlijk uit content/reviews/top.md (Trustpilot, 5 sterren, gecontroleerd)
 'R169': ('The real test was my egg the next morning... the egg released completely and slid around the pan like it was non-stick.', 'Michael G.'),
 'R138': ("I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns.", 'Tammy'),
 'R583': ('These hammered Titanium pans from Siraat have been the best we have owned yet... the last pans we ever have to purchase.', 'Scott Y.'),
 'R398': ('...I thought it was just marketing hype... I ended up buying the whole collection.', 'Fatima'),
 'R220': ("I've been cooking for well over 60 years... This Siraat pan has been the absolute best I've ever used.", 'Carole'),
 'R240': ('Siraat replaced a pan free of charge... I just sent them the picture and they honored the warranty.', 'Brandon W.'),
 'R466': ('...I honestly thought this might be another scam. But it&#39;s real titanium.', 'James'),
 'R577': ('This pan is fantastic. Makes all of our others "non stick" seem really sticky.', 'Thomas D.'),
}
def proof(bg, ids, title='100,000+ happy customers', pad='30px 20px 10px 20px'):
    dark = bg == NIGHT
    sc = Y if dark else INK; tc = '#FFFFFF' if dark else INK; cb = '#1C1C1C' if dark else '#FFFFFF'
    h = row(bg, pad, txt('&#9733;&#9733;&#9733;&#9733;&#9733;', 24, 26, sc, 400, 'letter-spacing:4px;') + '<div class="st" style="font-family:%s;font-size:34px;line-height:38px;font-weight:900;letter-spacing:-1px;color:%s;padding-top:6px;">%s</div>' % (FF, tc, title), 'center', 'padx')
    for i in ids:
        q, n = REV[i]
        c = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%s" style="background-color:%s;border-radius:10px;"><tr><td style="padding:18px 20px;">%s%s%s</td></tr></table>' % (
            cb, cb, txt('&#9733;&#9733;&#9733;&#9733;&#9733;', 14, 16, Y if dark else '#272727', 400, 'letter-spacing:2px;'),
            txt('&ldquo;%s&rdquo;' % q, 17, 25, tc, 600, 'padding-top:8px;'), txt('%s &middot; Verified buyer' % n, 13, 18, '#9E998F' if dark else '#727272', 600, 'padding-top:10px;'))
        h += row(bg, '12px 20px 0 20px', c, 'left', 'padx')
    return h + gap(bg, 18)
def stats(bg):
    dark = bg == NIGHT
    nc = Y if dark else INK; lc = '#BDB8AE' if dark else '#5E5A54'; br = '#2E2E2E' if dark else '#E4DED3'
    cell = lambda n, l, last=False: '<td width="33%%" align="center" valign="top" style="padding:16px 4px;%s"><div class="st" style="font-family:%s;font-size:34px;line-height:36px;font-weight:900;letter-spacing:-1px;color:%s;">%s</div>%s</td>' % (
        '' if last else 'border-right:1px solid %s;' % br, FF, nc, n, txt(l, 11, 15, lc, 800, 'letter-spacing:1.4px;padding-top:4px;'))
    t = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid %s;border-bottom:1px solid %s;"><tr>%s%s%s</tr></table>' % (
        br, br, cell('30', 'DAY<br>RETURNS'), cell('75', 'YEAR<br>WARRANTY'), cell('100K+', 'HAPPY<br>CUSTOMERS', True))
    return row(bg, '10px 20px 24px 20px', t, 'center', 'padx')
def stack(bg, rows, total_l, total_r, title='EVERYTHING YOU GET'):
    r = ''.join('<tr><td style="padding:13px 0;border-bottom:1px solid #ECE7DD;font-family:%s;font-size:16px;line-height:22px;color:%s;font-weight:600;">%s</td><td align="right" style="padding:13px 0 13px 10px;border-bottom:1px solid #ECE7DD;font-family:%s;font-size:14px;line-height:20px;color:%s;font-weight:900;white-space:nowrap;letter-spacing:0.6px;">%s</td></tr>' % (FF, INK, a, FF, INK, b) for a, b in rows)
    r += '<tr><td style="padding:16px 0 4px 0;font-family:%s;font-size:18px;line-height:24px;color:%s;font-weight:900;">%s</td><td align="right" style="padding:16px 0 4px 10px;"><span style="display:inline-block;background-color:%s;font-family:%s;font-size:16px;line-height:20px;font-weight:900;color:%s;padding:6px 10px;border-radius:3px;white-space:nowrap;">%s</span></td></tr>' % (FF, INK, total_l, Y, FF, INK, total_r)
    card = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border-radius:12px;"><tr><td style="padding:20px 22px 18px 22px;">%s<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="margin-top:6px;">%s</table></td></tr></table>' % (txt(title, 12, 16, '#727272', 900, 'letter-spacing:2px;'), r)
    return row(bg, '0 20px 24px 20px', card, 'left', 'padx')
def reasons(bg, items):
    dark = bg == NIGHT
    out = ''
    for n, t, d in items:
        c = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td width="70" valign="top"><div style="font-family:%s;font-size:44px;line-height:44px;font-weight:900;color:%s;letter-spacing:-2px;">%s</div></td><td valign="top" style="padding-left:6px;">%s%s</td></tr></table>' % (
            FF, Y if dark else INK, n, txt(t, 20, 25, '#FFFFFF' if dark else INK, 900, 'letter-spacing:-0.3px;'), txt(d, 16, 24, '#E6E3DC' if dark else '#3E3B37', 400, 'padding-top:6px;'))
        out += row(bg, '0 24px 24px 24px', c)
    return out

# ---------- brief (Benjamin) ----------
P = lambda t, pad='0 40px 18px 40px', bg=CREAM, color='#282828', size=17, lh=27: row(bg, pad, txt(t, size, lh, color), 'left', 'pad lead')
def sign(bg=CREAM):
    dark = bg == NIGHT
    return row(bg, '4px 40px 30px 40px', txt('Benjamin', 17, 24, '#FFFFFF' if dark else INK, 800) + txt('Founder, Siraat', 14, 20, '#9E998F' if dark else '#727272'), 'left', 'pad')
def bullets(bg, items, color='#282828'):
    r = ''.join('<tr><td width="22" valign="top" style="padding:8px 0 0 0;"><div style="width:9px;height:9px;background-color:%s;font-size:0;line-height:0;">&nbsp;</div></td><td valign="top" style="padding:0 0 10px 0;font-family:%s;font-size:17px;line-height:25px;color:%s;">%s</td></tr>' % (Y if bg == NIGHT else INK, FF, color, i) for i in items)
    return row(bg, '0 40px 12px 40px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % r, 'left', 'pad')

files = {}
FR_CODE = 'Extra 10% applied at checkout. 30-day returns. 75-year warranty.'
FR_SALE = 'No code needed. Free shipping &middot; 100,000+ customers'
CO = lambda c: "{{ event.extra.responsive_checkout_url|default:'https://siraatskitchen.com/cart' }}&discount=BFCODE&utm_source=klaviyo&utm_medium=email&utm_campaign=bf-v2-checkout&utm_content=%s" % c
CARTL = lambda c: 'https://siraatskitchen.com/discount/BFCODE?redirect=/cart%%3Futm_source%%3Dklaviyo%%26utm_medium%%3Demail%%26utm_campaign%%3Dbf-v2-cart%%26utm_content%%3D' + c
def meta(id_, sender, subj, pre, when, who, why, alts=''):
    return 'ID: %s\nSENDER: %s\nSUBJECT A: %s\nSUBJECT B: %s\n%sPREVIEW: %s\nWANNEER: %s\nWIE/FILTERS: %s\nWAAROM: %s' % (id_, sender, subj[0], subj[1], ('  Alternatieven: %s\n' % alts) if alts else '', pre, when, who, why)

# =====================================================================
# FLOWS
# =====================================================================
# --- F1 W1b: welcome +2 uur, de prijslijst ---
c = 'bf-v2-welcome'
m = meta('v2-w1b · Welcome tweede contact, +2 uur (T4a5Mk na W1 en Rn556d na BF-W1)', 'Siraat',
         ('Your Black Friday price list', 'Up to 70% off. Every price inside.'), 'Every price, side by side. Free gifts with every order.',
         'flow-stap +2 uur na aanmelding', 'Placed Order 0 sinds flowstart; geen Started Checkout in de laatste 1 uur (dan neemt checkout over)',
         'Smooche mail 3 (+2 u). W1 haalt $2,74 per ontvanger, daarna was er tot de volgende ochtend niets.', '"70% off: the full price list" · "Your prices are in" · "$649 for a whole kitchen"')
b = head(m, 'Your Black Friday price list', 'Every price, side by side. Free gifts with every order.', 'profile') + OPEN(NIGHT)
b += hero_dark('THE PRICE LIST', 'Black Friday', 'sale is live', sub='No code needed. Free gifts with every order.', url=utm(SALE, c, 'w1b-hero'), fr='Free shipping &middot; 100,000+ customers')
b += band('THE BIGGEST DEAL IN THE SALE')
b += gap(NIGHT, 24) + deal_main(NIGHT, c, 'w1b')
b += band('EVERY PRICE, SIDE BY SIDE', INK, Y) + gap(NIGHT, 20) + grid_mkt(NIGHT, c, 'w1b')
b += proof(NIGHT, ['R169'], 'Eggs slide. No coating.')
b += stats(NIGHT)
b += cta('Shop the sale', utm(SALE, c, 'w1b-cta2'), NIGHT, '4px 30px 34px 30px')
files['v2-w1b'] = b + TAIL

# --- F2 W2: welcome +24 uur (ook campagne): just arrived, selling fast ---
c = 'bf-v2-welcome'
m = meta('v2-w2 · Welcome +24 uur (T4a5Mk, vervangt W2 tijdens de sale; Rn556d na W1b). Ook te gebruiken als campagne (2 en 20 nov).', 'Siraat',
         ('Just arrived: the 6 and 12-piece sets', 'Restocked, and going fast'), 'New stock just landed. At up to 70% off, it is selling fast.',
         'flow-stap +24 uur na aanmelding (Smooche mail 8 op +26 u)', 'Placed Order 0; overslaan als checkout- of cart-mail in de laatste 1 uur (niet 1 dag zoals nu)',
         'Floris 1 nov: nieuwe voorraad 6-Pcs en 12-Pcs is binnen ("just arrived and selling fast").', '"The sets are back" · "Just landed: 12 pieces for $649" · "New stock. Same 70% off."')
b = head(m, 'Just arrived: the sets', 'New stock just landed. At up to 70% off, it is selling fast.', 'profile') + OPEN(Y, 'JUST ARRIVED &middot; SELLING FAST')
b += hero_yellow('NEW STOCK IS IN', 'Just', 'arrived.', 'The 6 and 12-piece sets just landed in our warehouse. At up to 70% off, they are selling fast.', 'Shop the sets', utm(SALE, c, 'w2-hero'), 'Up to 70% off. Free gifts with every order.')
b += band('SELLING FAST', INK, Y) + gap(NIGHT, 24)
b += '{{USONLY}}\n' + deal(NIGHT, '{{IMG}}/deal-set12-pizza.jpg', 'Cookware Set, 12 Pcs, with a free Pizza Steel', utm(U['set12p'], c, 'w2-set12'), [JA, SF], 'Cookware Set, 12&nbsp;Pcs',
        '3 pans, 2 saucepans, a stockpot and 6 fitted lids. The whole kitchen, done in one order.', '{{WAS:set12}}', '{{PRICE:set12}}', '-68%', '+ FREE Pizza Steel ($664 value) with this set', 'Get the 12-piece set', '', 'THE COMPLETE SET') + '{{/USONLY}}\n'
b += deal(NIGHT, '{{IMG}}/deal-set6.jpg', 'Pan Set with Lids, 6 Pcs', utm(U['set6'], c, 'w2-set6'), [JA, SF], 'Pan Set with Lids, 6&nbsp;Pcs',
          'Pan Pro Mini, Small and Large, each with its own fitted lid. The three sizes you reach for every day.', '{{WAS:set6}}', '{{PRICE:set6}}', '-70%', '+ {{GIFTS:total}} with every order', 'Get the 6-piece set', 'Free shipping &middot; 100,000+ customers', 'THE STARTER SET')
b += proof(NIGHT, ['R398'], 'Started with one. Bought the set.', '14px 20px 10px 20px')
b += stats(NIGHT)
b += P('Quick note from me. Both sets sold faster this fall than we expected, and the new stock just arrived this week. At these prices it is going quickly. If a set has been on your list, now is the time.', '6px 40px 14px 40px', NIGHT, '#E6E3DC') + sign(NIGHT)
files['v2-w2'] = b + TAIL

# --- F3 K1b: cart +1 uur, extra 10% ticket ---
pn = "event|lookup:'Product Name'"
m = meta('v2-k1b · Cart tweede contact, +1 uur (TZG9Mx na K1)', 'Siraat',
         ('Extra 10% off your cart (already applied)', 'You left this at up to 70% off'), 'On top of Black Friday prices of up to 70% off.',
         'flow-stap +1 uur na Added to Cart (Smooche mail 6 op +1 u)', 'Placed Order 0; Started Checkout 0 sinds flowstart (checkout-flow neemt over)',
         'K1 haalt $3,59 per ontvanger; extra 10% met BFCODE alleen in abandonment (DECISIONS 31 okt).', '"Your cart just got 10% cheaper" · "Still yours, now 10% less" · "An extra 10%, on us"')
b = head(m, 'Extra 10% off your cart', 'On top of Black Friday prices of up to 70% off.', 'cart') + OPEN(NIGHT)
b += row(NIGHT, '34px 24px 0 24px', pill('YOUR CART', center=True), 'center')
b += row(NIGHT, '18px 16px 0 16px', '<div class="hx" style="font-family:%s;font-size:56px;line-height:56px;font-weight:900;letter-spacing:-2px;color:#FFFFFF;text-transform:uppercase;">Extra 10%% off.<br><span style="color:%s;">Already applied.</span></div>' % (FF, Y), 'center', 'padx')
b += row(NIGHT, '16px 30px 22px 30px', txt('On top of Black Friday prices of up to 70% off. One tap and it is in your cart.', 17, 26, '#E6E3DC', 500, 'text-align:center;'), 'center')
ticket = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%s" style="background-color:%s;border:2px dashed %s;border-radius:6px;"><tr><td align="center" style="padding:16px 14px;">%s<div class="hl" style="font-family:%s;font-size:40px;line-height:42px;font-weight:900;letter-spacing:-1px;color:%s;padding-top:4px;">BFCODE</div>%s</td></tr></table>') % (
    Y, Y, INK, txt('YOUR EXTRA 10% CODE', 11, 14, INK, 900, 'letter-spacing:2px;'), FF, INK, txt('Applied automatically with the button below.', 13, 18, INK, 600, 'padding-top:6px;'))
b += row(NIGHT, '0 20px 18px 20px', ticket, 'center', 'padx')
cartcard = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border-radius:12px;">'
            '<tr><td align="center" style="padding:18px 18px 0 18px;"><a href="%s"><img src="{%% if event.ImageURL %%}{{ event.ImageURL }}&width=1000{%% else %%}{{IMG}}/cart-fallback.jpg{%% endif %%}" width="300" alt="{{ %s|default:\'Your item\' }}" style="display:block;width:100%%;max-width:{%% if event.ImageURL %%}300{%% else %%}240{%% endif %%}px;height:auto;border:0;border-radius:8px;"></a></td></tr>'
            '<tr><td style="padding:16px 20px 4px 20px;">%s<div style="font-family:%s;font-size:20px;line-height:26px;font-weight:900;color:%s;padding-top:8px;word-break:break-word;">{{ %s|default:\'Your item\' }}</div>%s</td></tr>'
            '<tr><td style="padding:12px 20px 20px 20px;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="#FFF3CC" style="background-color:#FFF3CC;border-left:4px solid %s;padding:11px 13px;font-family:%s;font-size:14px;line-height:20px;color:%s;font-weight:700;">Black Friday price + extra 10%% + {{GIFTS:total}}</td></tr></table></td></tr></table>') % (
    CARTL('k1b-product'), pn, pill('STILL IN YOUR CART'), FF, INK, pn, txt('Qty {{ event.Quantity|default:1|floatformat:0 }}', 14, 20, '#727272', 600, 'padding-top:2px;'), Y, FF, INK)
b += row(NIGHT, '0 20px 4px 20px', cartcard, 'left', 'padx')
b += cta('Return to my cart', CARTL('k1b-cta1'), NIGHT, '22px 30px 26px 30px', FR_CODE)
b += band('UP TO 70% OFF &nbsp;&middot;&nbsp; FREE GIFTS')
b += proof(NIGHT, ['R577'], 'Makes the others feel sticky.')
b += stats(NIGHT)
b += cta('Use my extra 10%', CARTL('k1b-cta2'), NIGHT, '0 30px 34px 30px')
files['v2-k1b'] = b + TAIL

# --- F4 C1b: checkout +1 uur, brief van Benjamin (Smooche "Chloe") ---
m = meta('v2-c1b · Checkout tweede contact, +1 uur (QUBUQV na C1). Platte brief binnen vaste header/footer.', 'Benjamin from Siraat (reply-to gelezen inbox)',
         ('I saved your cart', 'Benjamin here, about your order'), 'Plus an extra 10%, already applied with one tap.',
         'flow-stap +1 uur na Started Checkout (Smooche mail 7 op +1 u 15)', 'Placed Order 0 sinds flowstart',
         'C1 haalt $7,96 per ontvanger, het rijkste moment van de reis. Brief-vorm werkt bij Smooche (7 van 13 mails).', '"Your cart is still open" · "One step left" · "Something stop you?"')
b = head(m, 'I saved your cart', 'Plus an extra 10%, already applied with one tap.', 'checkout') + OPEN(CREAM)
b += P("Hi {{ first_name|default:'there' }},", '34px 40px 14px 40px')
b += P('Benjamin here. You were one step from finishing your order an hour ago, so I saved your cart.')
b += P('<b>Here is what is on it right now:</b>', '0 40px 10px 40px')
b += bullets(CREAM, ['Black Friday prices, up to 70% off', '<b>An extra 10% off</b> with code BFCODE, already applied with the button', '{{GIFTS:total}}, included', 'Free shipping, 30-day returns and a 75-year warranty'])
b += '{{BLOCK:cart pad="8px 40px 4px 40px" title="YOUR CART, SAVED" line="Extra 10% with code <b>BFCODE</b>, already applied with the button."}}\n'
b += cta('Complete my order', CO('c1b-cta1'), CREAM, '20px 40px 26px 40px', FR_CODE)
b += P('If something stopped you, the size, the price, anything, just reply. Our team will help.')
b += sign()
files['v2-c1b'] = b + TAIL

# --- F5 C1c: checkout +3 uur, drie redenen ---
m = meta('v2-c1c · Checkout derde contact, +3 uur (QUBUQV). Product en bewijs (Smooche mail 6 "3 reasons").', 'Siraat',
         ('3 reasons 100,000+ people switched', 'Why it is covered for 75 years'), 'Then your extra 10%, still applied.',
         'flow-stap +3 uur na Started Checkout', 'Placed Order 0 sinds flowstart',
         'Bezwaren wegnemen (werkt titanium echt, is het getest) vlak voor de beslissing; bewijs = rapport + review.', '"Report no. 25895" · "Cold metal grabs. Hot metal lets go." · "What makes it different"')
b = head(m, '3 reasons 100,000+ people switched', 'Then your extra 10%, still applied.', 'checkout') + OPEN(NIGHT)
b += row(NIGHT, '0', img(EX('04-pan-tower'), 'A tower of Siraat titanium pans'), 'center', '')
b += row(NIGHT, '30px 24px 0 24px', pill('BEFORE YOU DECIDE', center=True), 'center')
b += row(NIGHT, '18px 16px 26px 16px', '<div class="hx" style="font-family:%s;font-size:56px;line-height:56px;font-weight:900;letter-spacing:-2px;color:#FFFFFF;text-transform:uppercase;">3 reasons<br><span style="color:%s;">they switched.</span></div>' % (FF, Y), 'center', 'padx')
b += reasons(NIGHT, [('01', 'Nothing to wear off.', 'A pure titanium cooking surface with no coatings. Nothing to peel or flake. That is why it is covered for 75 years.'),
                     ('02', 'Tested, not just labeled.', 'Light Labs report no. 25895: 31 PFAS compounds tested, every one below the detection limit. <a href="%s" style="color:%s;">Read it yourself</a>.' % (utm(U['report'], 'bf-v2-checkout', 'c1c-report'), Y)),
                     ('03', 'Eggs slide. With heat.', 'Medium heat for 2 to 3 minutes, then a teaspoon of oil. Cold metal grabs your food. Hot metal lets it go.')])
b += proof(NIGHT, ['R169'], 'In their words', '6px 20px 10px 20px')
b += band('YOUR CART &nbsp;&middot;&nbsp; EXTRA 10% APPLIED')
b += '{{BLOCK:cart pad="20px 20px 4px 20px" title="STILL IN YOUR CART" line="Extra 10% with code <b>BFCODE</b>, already applied with the button."}}\n'
b += cta('Complete my order', CO('c1c-cta1'), NIGHT, '20px 30px 34px 30px', FR_CODE)
files['v2-c1c'] = b + TAIL

# --- F6 C2b: checkout +25 uur, value stack ---
m = meta('v2-c2b · Checkout, +25 uur (QUBUQV, na C2 op +24 u). Value stack.', 'Siraat',
         ('Everything you get, added up', 'Your cart + 4 gifts + extra 10%'), 'It is all still on your cart, with your extra 10%.',
         'flow-stap +25 uur (Smooche herhaalt de cart-reeks precies 24 uur later)', 'Placed Order 0 sinds flowstart',
         'Prijs is het grootste bezwaar (27% twijfelde): waarde optellen, niet alleen korting.', '"Here is the math" · "What $70 in gifts looks like" · "The deal, line by line"')
b = head(m, 'Everything you get, added up', 'It is all still on your cart, with your extra 10%.', 'checkout') + OPEN(Y, 'EXTRA 10% APPLIED')
b += hero_yellow('YOUR ORDER', 'Everything', 'you get.', 'Added up, line by line. It is all still on your cart.', 'Complete my order', CO('c2b-hero'), FR_CODE)
b += gap(Y, 4)
b += stack(Y, [('Your cart at Black Friday prices', 'UP TO 70% OFF'), ('Extra 10% with code BFCODE', 'APPLIED'), ('Free shipping', '{{IF:PRICED}}{{GIFTS:ship}} VALUE{{ELSE}}INCLUDED{{ENDIF}}'),
               ('Chef&#39;s e-book', '{{IF:PRICED}}{{GIFTS:ebook}} VALUE{{ELSE}}INCLUDED{{ENDIF}}'), ('Mystery gift', '{{IF:PRICED}}{{GIFTS:mystery}} VALUE{{ELSE}}INCLUDED{{ENDIF}}'), ('A chance to win a PFAS water filter', 'INCLUDED'),
               ('30-day returns', 'INCLUDED'), ('75-year warranty', 'INCLUDED')], 'Gifts with your order', '{{GIFTS:TOTAL}}')
b += '{{BLOCK:cart pad="0 20px 4px 20px" title="YOUR CART" line="Extra 10% with code <b>BFCODE</b>, already applied with the button."}}\n'
b += cta_ink('Complete my order', CO('c2b-cta2'), Y, '20px 30px 32px 30px', '{{GIFTS:total}} included.')
b += band('100,000+ HAPPY CUSTOMERS', INK, Y)
b += proof(NIGHT, ['R240'], 'Covered for 75 years.', '24px 20px 10px 20px')
files['v2-c2b'] = b + TAIL

# --- F7 C2c: checkout +26 uur, donkere brief "Two promises" ---
m = meta('v2-c2c · Checkout, +26 uur (QUBUQV). Donkere brief van Benjamin, volledige risicoomkering.', 'Benjamin from Siraat',
         ('Two promises, then it is your call', 'What if it is not for you?'), 'Your extra 10% is still on your cart. Two promises first.',
         'flow-stap +26 uur (Smooche mail 12 op +40,5 u, laatste van de reeks)', 'Placed Order 0 sinds flowstart',
         'Laatste mail van de dag-1-reeks: risico wegnemen (skill sectie 8, "Two promises").', '"Benjamin, one more time" · "The honest answer" · "If it is wrong, we fix it"')
b = head(m, 'Two promises, then it is your call', 'Your extra 10% is still on your cart. Two promises first.', 'checkout') + OPEN(NIGHT)
b += row(NIGHT, '36px 40px 6px 40px', '<div class="hl" style="font-family:%s;font-size:40px;line-height:42px;font-weight:900;letter-spacing:-1.4px;color:#FFFFFF;">Two promises.<br><span style="color:%s;">Then it is your call.</span></div>' % (FF, Y), 'left', 'pad')
b += P("Hi {{ first_name|default:'there' }}, Benjamin again.", '20px 40px 14px 40px', NIGHT, '#FFFFFF')
b += P('Your cart is still open. If one thing is holding you back, it is usually this: what if it is not for you? So here are my two promises.', '0 40px 18px 40px', NIGHT, '#E6E3DC')
prom = lambda n, t, d: row(NIGHT, '0 20px 12px 20px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#1C1C1C" style="background-color:#1C1C1C;border-radius:10px;border-left:5px solid %s;"><tr><td style="padding:18px 20px;">%s%s%s</td></tr></table>' % (Y, txt(n, 12, 14, Y, 900, 'letter-spacing:2px;'), txt(t, 20, 26, '#FFFFFF', 900, 'padding-top:6px;'), txt(d, 16, 24, '#E6E3DC', 400, 'padding-top:6px;')), 'left', 'padx')
b += prom('PROMISE 1', 'Changed your mind?', 'Send it back unused within 30 days for a full refund.')
b += prom('PROMISE 2', 'Something wrong with it?', 'Damaged or defective in the first 30 days: refund or replacement, and we pay the shipping. After that, it is covered for 75 years.')
b += P('Your extra 10% (code BFCODE) is still on your cart, together with {{GIFTS:total}}.', '14px 40px 6px 40px', NIGHT, '#E6E3DC')
b += cta('Complete my order', CO('c2c-cta1'), NIGHT, '18px 30px 24px 30px', FR_CODE)
b += P('Reply if you have a question. Our team will help.', '0 40px 12px 40px', NIGHT, '#BDB8AE', 15, 23) + sign(NIGHT)
files['v2-c2c'] = b + TAIL

# =====================================================================
# EINDE SALE (campagnes 28 tot 30 nov)
# =====================================================================
c = 'bf-v2-end'
m = meta('v2-sat28 · Campagne za 28 nov 08:15 lokaal', 'Siraat', ('The last weekend of Black Friday', '3 days left: up to 70% off'),
         'Up to 70% off and free gifts, for three more days.', 'za 28 nov 08:15 lokaal (US/INT)', 'E90 + kopers 365 d, uitgesloten: order sinds 27 nov. Smart sending uit.',
         'Harde push einde sale (Floris 1 nov).', '"Last weekend at these prices" · "The final weekend" · "Black Friday, last 3 days"')
b = head(m, 'The last weekend of Black Friday', 'Up to 70% off and free gifts, for three more days.', 'profile') + OPEN(NIGHT, 'LAST WEEKEND &middot; UP TO 70% OFF', Y, INK)
b += hero_dark('3 DAYS LEFT', 'The last', 'weekend.', sub='Up to 70% off and free gifts, for three more days. Then the Black Friday Sale is over.', url=utm(SALE, c, 'sat-hero'), fr='Free shipping &middot; 100,000+ customers', image=EX('07-stage-reveal'), alt='Siraat titanium pans on a stage')
b += band('3 DAYS LEFT &nbsp;&middot;&nbsp; SAT &nbsp;&middot;&nbsp; SUN &nbsp;&middot;&nbsp; MON')
b += gap(NIGHT, 24) + deal_main(NIGHT, c, 'sat')
b += grid_mkt(NIGHT, c, 'sat')
b += proof(NIGHT, ['R138'], 'Her 4th pan. Your first?')
b += cta('Shop the sale', utm(SALE, c, 'sat-cta2'), NIGHT, '4px 30px 34px 30px')
files['v2-sat28'] = b + TAIL

m = meta('v2-sun29 · Campagne zo 29 nov 09:00 lokaal (+ resend 19:00 aan niet-openers en abandoners 30 d)', 'Siraat', ('Black Friday ends tomorrow', 'Tomorrow it is over'),
         'Up to 70% off ends tomorrow. Here is every price.', 'zo 29 nov 09:00; resend 19:00', 'Lijst (min unengaged 180 non-buyers), uitgesloten order sinds 27 nov. Smart sending uit.',
         'Echte deadline: einde maandag 30 nov.', '"One day left" · "Ends tomorrow: the full price list" · "Last day tomorrow"')
b = head(m, 'Black Friday ends tomorrow', 'Up to 70% off ends tomorrow. Here is every price.', 'profile') + OPEN(Y, 'ENDS TOMORROW', INK, Y)
b += hero_yellow('ONE DAY LEFT', 'Ends', 'tomorrow.', 'Up to 70% off and free gifts end tomorrow.', 'Shop before it ends', utm(SALE, c, 'sun-hero'), 'No code needed. Free gifts with every order.')
b += band('THE FULL PRICE LIST', INK, Y) + gap(NIGHT, 24)
b += deal_main(NIGHT, c, 'sun', 'Get the 12-piece deal')
b += grid_mkt(NIGHT, c, 'sun', ('set6', 'standard', 'wok', 'deep', 'small', 'pizza'), ('standard', 'wok', 'deep', 'small', 'pizza', 'set6'))
b += stats(NIGHT)
b += cta('Shop before it ends', utm(SALE, c, 'sun-cta2'), NIGHT, '0 30px 34px 30px')
files['v2-sun29'] = b + TAIL

m = meta('v2-mon-am · Campagne ma 30 nov 07:00 lokaal', 'Siraat', ('Last day: up to 70% off', 'Today is the last day'), 'Black Friday ends today. Free gifts end with it.',
         'ma 30 nov 07:00 lokaal (voor Homestead E19 10:00)', 'E90 + abandoners 30 d, uitgesloten order sinds 27 nov. Smart sending uit.', 'Harde push laatste dag.', '"It ends today" · "Last day for these prices" · "Today only: the 12-piece for $649"')
b = head(m, 'Last day: up to 70% off', 'Black Friday ends today. Free gifts end with it.', 'profile') + OPEN(NIGHT, 'LAST DAY &middot; ENDS TODAY', Y, INK)
b += row(NIGHT, '0', img(EX('10-levitating-pan'), 'A Siraat titanium pan, lifted over the stove'), 'center', '')
b += row(NIGHT, '30px 16px 0 16px', '<div style="font-family:%s;font-size:15px;line-height:18px;font-weight:900;letter-spacing:4px;color:%s;">BLACK FRIDAY</div><div class="hxx" style="font-family:%s;font-size:110px;line-height:100px;font-weight:900;letter-spacing:-5px;color:#FFFFFF;padding-top:8px;">LAST<br><span style="background-color:%s;color:%s;padding:0 10px;">DAY.</span></div>' % (FF, Y, FF, Y, INK), 'center', 'padx')
b += row(NIGHT, '22px 30px 0 30px', txt('Up to 70% off and free gifts end today.', 18, 27, '#E6E3DC', 600, 'text-align:center;'), 'center')
b += cta('Shop before it ends', utm(SALE, c, 'monam-hero'), NIGHT, '24px 30px 30px 30px', 'Free shipping &middot; 100,000+ customers')
b += band('ENDS TODAY')
b += gap(NIGHT, 24) + deal_main(NIGHT, c, 'monam', 'Get it before it ends')
b += grid_mkt(NIGHT, c, 'monam')
b += cta('Shop before it ends', utm(SALE, c, 'monam-cta2'), NIGHT, '10px 30px 34px 30px', 'Ends today.')
files['v2-mon-am'] = b + TAIL

m = meta('v2-mon-pm · Campagne ma 30 nov 13:00 lokaal, brief van Benjamin', 'Benjamin from Siraat', ('Final hours', 'Benjamin here, before it ends'), 'The Black Friday Sale ends today. A short note first.',
         'ma 30 nov 13:00 lokaal', 'E30 + abandoners 14 d, uitgesloten order sinds 27 nov. Smart sending uit.', 'Persoonlijke brief tussen de beeldmails (Smooche "Chloe").', '"A note before it ends" · "Last day, honestly" · "If you were waiting"')
b = head(m, 'Final hours', 'The Black Friday Sale ends today. A short note first.', 'profile') + OPEN(CREAM, 'FINAL HOURS &middot; ENDS TODAY', Y, INK)
b += row(CREAM, '36px 40px 4px 40px', '<div class="hl" style="font-family:%s;font-size:44px;line-height:46px;font-weight:900;letter-spacing:-1.6px;color:%s;">Final hours.</div>' % (FF, INK), 'left', 'pad')
b += P("Hi {{ first_name|default:'there' }},", '18px 40px 14px 40px')
b += P('Benjamin here. Our Black Friday Sale ends today. A short note before it does.')
b += P('If you were waiting for the right moment, this is it. Here is what still holds until the end of today:')
b += bullets(CREAM, ['<b>Up to 70% off</b>, no code needed', '{{USONLY}}<b>The 12-piece set for {{PRICE:set12}}</b> (was {{WAS:set12}}), with a free Pizza Steel{{ELSEUS}}<b>The 6-piece set for {{PRICE:set6}}</b> (was {{WAS:set6}}){{/USONLY}}', '{{GIFTS:total}} with every order', '30-day returns and a 75-year warranty'])
b += cta('Shop before it ends', utm(SALE, c, 'monpm-cta1'), CREAM, '14px 40px 26px 40px', 'Ends today.')
b += P('Thank you for cooking with us this year. 100,000+ people now cook without a coating, and I hope you will be one of them.')
b += sign()
files['v2-mon-pm'] = b + TAIL

m = meta('v2-mon-late · Campagne ma 30 nov 20:00 lokaal, laatste mail', 'Siraat', ('Last email: Black Friday ends tonight', 'This is the last one'), 'After today the Black Friday Sale is over.',
         'ma 30 nov 20:00 lokaal [VRAAG FLORIS: eindtijd en tijdzone, "tonight" alleen als de sale om middernacht lokaal sluit]', 'klikkers 30 d + abandoners 14 d, uitgesloten order sinds 27 nov.',
         'Laatste duw (Smooche "final hours" met aftelklok; wij zonder klok).', '"Closing tonight" · "Last call" · "The end of Black Friday"')
b = head(m, 'Last email: Black Friday ends tonight', 'After today the Black Friday Sale is over.', 'profile') + OPEN(NIGHT, 'LAST CALL &middot; ENDS TODAY', Y, INK)
b += row(NIGHT, '44px 24px 0 24px', pill('LAST CALL', center=True), 'center')
b += row(NIGHT, '20px 16px 0 16px', '<div class="hx" style="font-family:%s;font-size:58px;line-height:58px;font-weight:900;letter-spacing:-2px;color:#FFFFFF;text-transform:uppercase;">This is<br>the last email.</div>' % FF, 'center', 'padx')
b += row(NIGHT, '22px 16px 0 16px', txt('BLACK FRIDAY ENDS', 15, 18, Y, 900, 'letter-spacing:4px;') + '<div class="hxx" style="font-family:%s;font-size:96px;line-height:90px;font-weight:900;letter-spacing:-4px;color:%s;padding-top:4px;">TONIGHT</div>' % (FF, Y), 'center', 'padx')
b += row(NIGHT, '20px 30px 0 30px', txt('Up to 70% off and free gifts, until the end of today. After that, the sale is over.', 17, 26, '#E6E3DC', 500, 'text-align:center;'), 'center')
b += cta('Shop before it ends', utm(SALE, c, 'monlate-cta1'), NIGHT, '26px 30px 30px 30px', 'Free shipping &middot; 100,000+ customers')
b += row(NIGHT, '0', img(EX('09-chefs-table'), 'Siraat titanium pans on a chef&#39;s table with steak'), 'center', '')
b += stats(NIGHT).replace('10px 20px 24px 20px', '24px 20px 24px 20px')
files['v2-mon-late'] = b + TAIL

# =====================================================================
# DAGELIJKSE CAMPAGNES (lege dagen)
# =====================================================================
c = 'bf-v2-daily'
m = meta('v2-pricelist · Campagne lege dagen (6, 12, 22 nov)', 'Siraat', ('The Black Friday price list', 'Every price, one email'), 'Up to 70% off, side by side. Free gifts with every order.',
         'zie research/smooche/06 sectie 4', 'zie tabel', 'Prijzen als hoofdzaak: de prijs verkoopt (Smooche-beeldmails met %).', '"$144 for the pan" · "What 70% off looks like" · "Price list inside"')
b = head(m, 'The Black Friday price list', 'Up to 70% off, side by side. Free gifts with every order.', 'profile') + OPEN(CREAM)
b += row(CREAM, '36px 16px 0 16px', pill('BLACK FRIDAY SALE IS LIVE', center=True), 'center')
b += row(CREAM, '18px 16px 0 16px', '<div class="hx" style="font-family:%s;font-size:58px;line-height:56px;font-weight:900;letter-spacing:-2.2px;color:%s;text-transform:uppercase;">The price<br><span style="background-color:%s;padding:0 8px;">list.</span></div>' % (FF, INK, Y), 'center', 'padx')
b += row(CREAM, '18px 30px 26px 30px', txt('Up to 70% off. Free gifts with every order. No code needed.', 17, 26, '#3E3B37', 500, 'text-align:center;'), 'center')
b += deal_main(CREAM, c, 'pl', 'Get the 12-piece deal')
b += grid_mkt(CREAM, c, 'pl', ('set6', 'standard', 'wok', 'deep', 'small', 'pizza'), ('standard', 'wok', 'deep', 'small', 'pizza', 'set6'))
b += stats(CREAM)
b += cta('Shop the sale', utm(SALE, c, 'pl-cta2'), CREAM, '0 30px 34px 30px', 'Free shipping &middot; 100,000+ customers')
files['v2-pricelist'] = b + TAIL

m = meta('v2-proof · Campagne lege dagen (9, 16 nov)', 'Siraat', ('100,000+ kitchens, no coatings', '"The last pans we ever have to purchase"'), 'What they say after the first egg. And this month, up to 70% off.',
         'zie tabel', 'zie tabel', 'Sociaal bewijs als hoofdzaak (Smooche mail 8, educatie + reviews).', '"Carole has cooked for 60 years" · "In their words" · "Why they kept buying"')
b = head(m, '100,000+ kitchens, no coatings', 'What they say after the first egg. And this month, up to 70% off.', 'profile') + OPEN(NIGHT)
b += row(NIGHT, '40px 16px 0 16px', txt('&#9733;&#9733;&#9733;&#9733;&#9733;', 26, 28, Y, 400, 'letter-spacing:5px;') + '<div class="hxx" style="font-family:%s;font-size:110px;line-height:104px;font-weight:900;letter-spacing:-5px;color:%s;padding-top:10px;">100,000+</div>' % (FF, Y), 'center', 'padx')
b += row(NIGHT, '6px 16px 0 16px', '<div class="hx" style="font-family:%s;font-size:44px;line-height:46px;font-weight:900;letter-spacing:-1.6px;color:#FFFFFF;text-transform:uppercase;">happy customers.</div>' % FF, 'center', 'padx')
b += row(NIGHT, '16px 30px 0 30px', txt('Here is what they say, in their own words. And this month, it is up to 70% off.', 17, 26, '#E6E3DC', 500, 'text-align:center;'), 'center')
b += cta('Shop the sale', utm(SALE, c, 'proof-hero'), NIGHT, '24px 30px 10px 30px', 'Free shipping &middot; 100,000+ customers')
b += proof(NIGHT, ['R583', 'R220', 'R466'], 'In their words')
b += band('UP TO 70% OFF &nbsp;&middot;&nbsp; FREE GIFTS') + gap(NIGHT, 24)
b += grid_mkt(NIGHT, c, 'proof')
b += cta('Shop the sale', utm(SALE, c, 'proof-cta2'), NIGHT, '10px 30px 34px 30px')
files['v2-proof'] = b + TAIL

m = meta('v2-letter · Campagne lege dagen (4, 13 nov), brief van Benjamin', 'Benjamin from Siraat', ('What I would buy at 70% off', 'If I were starting from zero'), 'Three picks, depending on your kitchen.',
         'zie tabel', 'E30 (brieven werken het best bij betrokken lezers)', 'Founder-brieven halen 1,3% klik tegenover 0,3 tot 0,6% voor beeldmails (PLAYBOOK 1).', '"Three picks" · "Where I would start" · "Pan or set?"')
b = head(m, 'What I would buy at 70% off', 'Three picks, depending on your kitchen.', 'profile') + OPEN(CREAM)
b += P("Hi {{ first_name|default:'there' }},", '34px 40px 14px 40px')
b += P('Benjamin here. People keep asking me the same question this month: with everything up to 70% off, what should I actually buy? Here is my honest answer.')
pick = lambda n, t, d, price, url: row(CREAM, '0 20px 12px 20px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border-radius:10px;"><tr><td style="padding:18px 20px;">%s%s%s%s</td></tr></table>' % (
    txt(n, 12, 14, '#727272', 900, 'letter-spacing:2px;'), '<div style="font-family:%s;font-size:21px;line-height:27px;font-weight:900;color:%s;padding-top:6px;"><a href="%s" style="color:%s;text-decoration:none;">%s &rarr;</a></div>' % (FF, INK, url, INK, t), txt(d, 16, 24, '#3E3B37', 400, 'padding-top:6px;'), '<div style="padding-top:10px;">%s</div>' % price), 'left', 'padx')
b += pick('IF YOU WANT ONE PAN', 'Pan Pro Standard {{SIZE:28}}', 'The size most people cook with every day. If you are not sure, start here.', price_line('{{WAS:standard}}', '{{PRICE:standard}}', '-70%', False, False), utm(U['standard'], c, 'letter-standard'))
b += pick('IF YOU COOK FOR TWO OR MORE', 'Pan Set with Lids, 6&nbsp;Pcs', 'Mini, Small and Large, each with a lid. Just arrived, and selling fast.', price_line('{{WAS:set6}}', '{{PRICE:set6}}', '-70%', False, False), utm(U['set6'], c, 'letter-set6'))
b += '{{USONLY}}\n' + pick('IF YOU ARE REPLACING EVERYTHING', 'Cookware Set, 12&nbsp;Pcs + free Pizza Steel', 'Pans, saucepans, a stockpot and 6 lids. Just arrived, and selling fast.', price_line('{{WAS:set12}}', '{{PRICE:set12}}', '-68%', False, False), utm(U['set12p'], c, 'letter-set12')) + '{{/USONLY}}\n'
b += P('Whatever you pick: it ships with {{GIFTS:total}}, you have 30 days to send it back unused, and it is covered for 75 years.', '14px 40px 6px 40px')
b += cta('Shop the sale', utm(SALE, c, 'letter-cta1'), CREAM, '16px 40px 24px 40px', 'No code needed.')
b += P('Not sure about a size? Reply and our team will help.', '0 40px 12px 40px', CREAM, '#5E5A54', 15, 23) + sign()
files['v2-letter'] = b + TAIL

for k, v in files.items():
    assert '\u2014' not in v, k
    for bad in ('next batch', 'NEXT BATCH', 'reserve', 'arriving', 'next shipment'):
        assert bad not in v.split('-->', 1)[1], (k, bad)
    open(os.path.join(N, k + '.html'), 'w').write(v)
    print('geschreven', k, len(v))
