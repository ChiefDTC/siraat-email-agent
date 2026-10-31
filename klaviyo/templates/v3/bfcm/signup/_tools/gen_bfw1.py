"""Genereert bf-w1-a.html (editorial light) en bf-w1-b.html (dark minimal) in klaviyo/templates/v3/bfcm/signup."""
import os
S = '/home/user/siraat-email-agent/klaviyo/templates/v3/bfcm/signup'
CDN = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/'
F = "Inter,Arial,Helvetica,sans-serif"
SALE = 'https://siraatskitchen.com/collections/black-friday-sale'

P = {
 'pan': dict(url='https://siraatskitchen.com/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern',
   img=CDN+'Titanium_hammered_pan_pro_standard_b69d1fc5-43d8-40a5-9ad7-523bdddc54d4.webp?v=1781682831&width=1200&format=pjpg',
   alt='Titanium Hammered Pan Pro Standard', kicker='OUR #1 SELLER', name='Pan Pro Standard',
   ben='Pure titanium cooking surface, no coatings. Nothing on it to wear off, so it&rsquo;s covered for 75 years.',
   now='$144', was='$480', save='Save $336', btn='Shop the Pan Pro'),
 'set6': dict(url='https://siraatskitchen.com/products/titanium-hammered-pan-set-with-lids-6-pcs',
   img=CDN+'6pcscookwareset.webp?width=700&format=pjpg', alt='Titanium Hammered Pan Set with Lids, 6 pieces',
   kicker='3 PANS + 3 LIDS', name='Pan Set, 6&nbsp;Pcs', ben='Three sizes and fitted lids. Every frying job covered.',
   now='$299', was='$997', save='Save $698', btn='Shop the 6-Pcs set'),
 'set12': dict(url='https://siraatskitchen.com/products/titanium-hammered-cookware-set',
   img=CDN+'12pcsset.webp?width=700&format=pjpg', alt='Titanium Hammered Cookware Set, 12 pieces',
   kicker='THE COMPLETE SET', name='Cookware Set, 12&nbsp;Pcs', ben='3 pans, 3 pots and 6 fitted lids. Works on every stovetop, induction too.',
   now='$599', was='$1,997', save='Save $1,398', btn='Shop the 12-Pcs set'),
 'wok': dict(url='https://siraatskitchen.com/products/titanium-hammered-wok-pan-pro',
   img=CDN+'WokHammedPan_3.webp?v=1780301994&width=700&format=pjpg', alt='Titanium Hammered Wok Pan Pro',
   kicker='TITANIUM HAMMERED', name='Wok Pan Pro', ben='Deep sides for stir-fries, searing and tossing. Oven safe.',
   now='$119', was='$397', save='Save $278', btn='Shop the Wok Pan Pro'),
}

TH = {
 'a': dict(bg='#FFFFFF', outer='#F8F7F2', ink='#272727', sub='#5C5953', mute='#8C877E', line='#E6E2D9', save='#272727',
           btn_bg='#272727', btn_fg='#FFFFFF', tile='#F6F1EB', bar_bg='#FFB800', bar_fg='#272727', link='#272727'),
 'b': dict(bg='#0E0E0E', outer='#0E0E0E', ink='#FFFFFF', sub='#C9C5BD', mute='#8A867E', line='#2A2927', save='#FFB800',
           btn_bg='#FFB800', btn_fg='#272727', tile='#F6F1EB', bar_bg='#0E0E0E', bar_fg='#FFFFFF', link='#FFFFFF'),
}


def td(t, style, cls='', align='left'):
    c = ' class="%s"' % cls if cls else ''
    return '<tr><td%s align="%s" bgcolor="%s" style="background-color:%s;%s">%s</td></tr>\n' % (c, align, t['bg'], t['bg'], style, '%s')


def row(t, html, pad, cls='pad', align='left', extra=''):
    return '<tr><td class="%s" align="%s" bgcolor="%s" style="background-color:%s;padding:%s;%s">%s</td></tr>\n' % (cls, align, t['bg'], t['bg'], pad, extra, html)


def hair(t, pad='0 40px'):
    return ('<tr><td class="pad" bgcolor="%s" style="background-color:%s;padding:%s;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">'
            '<tr><td height="1" bgcolor="%s" style="background-color:%s;height:1px;line-height:1px;font-size:0;">&nbsp;</td></tr></table></td></tr>\n') % (t['bg'], t['bg'], pad, t['line'], t['line'])


def space(t, h):
    return '<tr><td bgcolor="%s" style="background-color:%s;height:%dpx;line-height:%dpx;font-size:0;">&nbsp;</td></tr>\n' % (t['bg'], t['bg'], h, h)


def button(t, label, url, full=False):
    w = ' width="100%"' if full else ''
    return ('<table role="presentation"%s cellpadding="0" cellspacing="0" border="0"><tr><td align="center" bgcolor="%s" style="background-color:%s;">'
            '<!--[if mso]><v:rect xmlns:v="urn:schemas-microsoft-com:vml" href="%s" style="height:54px;v-text-anchor:middle;width:280px;" stroke="f" fillcolor="%s"><center style="color:%s;font-family:Arial,sans-serif;font-size:14px;font-weight:bold;letter-spacing:2px;">%s</center></v:rect><![endif]-->'
            '<!--[if !mso]><!--><a href="%s" style="display:block;padding:18px 34px;font-family:%s;font-size:14px;line-height:18px;font-weight:800;letter-spacing:2px;color:%s;text-decoration:none;text-transform:uppercase;white-space:nowrap;">%s &rarr;</a><!--<![endif]-->'
            '</td></tr></table>') % (w, t['btn_bg'], t['btn_bg'], url, t['btn_bg'], t['btn_fg'], label.upper(), url, F, t['btn_fg'], label)


def outline(t, label, url):
    return ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="border:2px solid %s;">'
            '<a href="%s" style="display:block;padding:16px 20px;font-family:%s;font-size:14px;line-height:18px;font-weight:800;letter-spacing:2px;color:%s;text-decoration:none;text-transform:uppercase;white-space:nowrap;">%s &rarr;</a>'
            '</td></tr></table>') % (t['ink'], url, F, t['ink'], label)


def textlink(t, label, url, size=12):
    return ('<a href="%s" style="font-family:%s;font-size:%dpx;line-height:16px;font-weight:800;letter-spacing:1.6px;color:%s;text-decoration:none;text-transform:uppercase;border-bottom:1px solid %s;padding-bottom:3px;white-space:nowrap;">%s &rarr;</a>') % (url, F, size, t['link'], t['link'], label)


def price(t, p, big):
    sz = 30 if big else 22
    us = ('<span class="pr%s" style="font-family:%s;font-size:%dpx;line-height:%dpx;font-weight:900;letter-spacing:-0.6px;color:%s;">%s</span>'
          '&nbsp;&nbsp;<span style="font-family:%s;font-size:%dpx;line-height:%dpx;color:%s;text-decoration:line-through;">%s</span>'
          '<div style="font-family:%s;font-size:12px;line-height:16px;font-weight:800;letter-spacing:1.4px;color:%s;text-transform:uppercase;padding-top:6px;">%s</div>') % (
        '' if big else 's', F, sz, sz + 4, t['ink'], p['now'], F, 15 if big else 14, sz, t['mute'], p['was'], F, t['save'], p['save'])
    if big:
        intl = ('<div class="pr" style="font-family:%s;font-size:26px;line-height:30px;font-weight:900;letter-spacing:-0.6px;color:%s;">Up to 70%% off</div>'
                '<div style="font-family:%s;font-size:12px;line-height:16px;font-weight:800;letter-spacing:1.4px;color:%s;text-transform:uppercase;padding-top:6px;">See your price on the site</div>') % (F, t['ink'], F, t['save'])
    else:
        intl = ('<div style="font-family:%s;font-size:12px;line-height:16px;font-weight:800;letter-spacing:1.4px;color:%s;text-transform:uppercase;">In the sale</div>'
                '<div style="font-family:%s;font-size:13px;line-height:18px;color:%s;padding-top:4px;">Your price shows on the site.</div>') % (F, t['save'], F, t['mute'])
    return '{{IF:US}}' + us + '{{ELSE}}' + intl + '{{ENDIF}}'


def kicker(t, k):
    return '<div style="font-family:%s;font-size:11px;line-height:14px;font-weight:800;letter-spacing:2px;color:%s;text-transform:uppercase;">%s</div>' % (F, t['mute'], k)


def hero_product(t, p):
    img = ('<a href="%s" style="text-decoration:none;"><img src="%s" width="520" alt="%s" style="display:block;width:100%%;max-width:520px;height:auto;border:0;"></a>') % (p['url'], p['img'], p['alt'])
    out = row(t, img, '0 40px 0 40px', cls='pad', align='center')
    body = (kicker(t, p['kicker']) +
            '<div class="pn" style="font-family:%s;font-size:34px;line-height:38px;font-weight:900;letter-spacing:-1px;color:%s;padding-top:10px;"><a href="%s" style="color:%s;text-decoration:none;">%s</a></div>' % (F, t['ink'], p['url'], t['ink'], p['name']) +
            '<div style="font-family:%s;font-size:16px;line-height:24px;color:%s;padding-top:10px;">%s</div>' % (F, t['sub'], p['ben']))
    out += row(t, body, '26px 40px 0 40px')
    out += row(t, price(t, p, True), '18px 40px 0 40px')
    out += row(t, outline(t, p['btn'], p['url']), '22px 40px 40px 40px', cls='pad')
    return out


def side_product(t, p):
    inner = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>'
             '<td class="si" width="240" valign="middle" bgcolor="%s" style="background-color:%s;width:240px;"><a href="%s" style="text-decoration:none;"><img src="%s" width="240" alt="%s" style="display:block;width:100%%;max-width:240px;height:auto;border:0;"></a></td>'
             '<td class="sg" width="28" style="width:28px;font-size:0;line-height:0;">&nbsp;</td>'
             '<td valign="middle" style="text-align:left;">%s'
             '<div class="sn" style="font-family:%s;font-size:22px;line-height:26px;font-weight:900;letter-spacing:-0.6px;color:%s;padding-top:8px;"><a href="%s" style="color:%s;text-decoration:none;">%s</a></div>'
             '<div class="sb" style="font-family:%s;font-size:14px;line-height:20px;color:%s;padding-top:8px;">%s</div>'
             '<div style="padding-top:14px;">%s</div>'
             '<div style="padding-top:16px;">%s</div>'
             '</td></tr></table>') % (t['tile'], t['tile'], p['url'], p['img'], p['alt'], kicker(t, p['kicker']), F, t['ink'], p['url'], t['ink'], p['name'],
                                      F, t['sub'], p['ben'], price(t, p, False), textlink(t, p['btn'], p['url']))
    return row(t, inner, '32px 40px 32px 40px')


def proof(t):
    cells = [('100,000+', 'customers'), ('75-year', 'warranty'), ('30-day', 'returns'), ('Free', 'shipping{{IF:US}}{{ELSE}}, duties paid{{ENDIF}}')]
    def c(v, l, bl, bt):
        b = ''
        if bl: b += 'border-left:1px solid %s;' % t['line']
        if bt: b += 'border-top:1px solid %s;' % t['line']
        return ('<td width="50%%" align="center" valign="top" style="width:50%%;padding:20px 8px;%s">'
                '<div style="font-family:%s;font-size:24px;line-height:28px;font-weight:900;letter-spacing:-0.6px;color:%s;">%s</div>'
                '<div style="font-family:%s;font-size:11px;line-height:15px;font-weight:800;letter-spacing:1.8px;color:%s;text-transform:uppercase;padding-top:6px;">%s</div></td>') % (b, F, t['ink'], v, F, t['mute'], l)
    tb = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid %s;border-bottom:1px solid %s;">'
          '<tr>%s%s</tr><tr>%s%s</tr></table>') % (t['line'], t['line'], c(*cells[0], False, False), c(*cells[1], True, False), c(*cells[2], False, True), c(*cells[3], True, True))
    return row(t, tb, '8px 40px 0 40px')


def signoff(t):
    body = ('<div style="font-family:%s;font-size:16px;line-height:25px;color:%s;">Not sure where to start? Start with the Pan Pro Standard, it&rsquo;s our #1 seller. '
            'Reply if you get stuck. I read them.</div>'
            '<div style="font-family:%s;font-size:16px;line-height:24px;font-weight:800;color:%s;padding-top:16px;">Benjamin</div>'
            '<div style="font-family:%s;font-size:13px;line-height:18px;color:%s;">Founder, Siraat</div>') % (F, t['sub'], F, t['ink'], F, t['mute'])
    return row(t, body, '36px 40px 44px 40px')


HEAD = '''<!--
BF SIGNUP FLOW · W1 OPTIE %(opt)s "%(optname)s" (31 okt 2026). Herontwerp na feedback Floris ("looks a bit cheap ... more minimalist, more direct response").
  Twee opties naast elkaar: bf-w1-a.html (editorial light) en bf-w1-b.html (dark minimal). Zelfde copy en structuur, alleen de stijl verschilt.
  Structuur: topbar BLACK FRIDAY SALE IS LIVE, vaste header, %(heroline)skop met aanbod + één regel + SHOP THE SALE, productlijst (Pan Pro Standard groot,
  6-delige set, US: 12-delige set / niet-US: Wok Pan Pro), bewijsstrook (2x2), afsluiting Benjamin, vaste footer. Rechte hoeken, geen pillen.
SUBJECT: You're just in time 🧡
PREVIEW: Up to 70% off is live, no code needed. Here's where I'd start.
MARKET-SIGNAL: profile (person.Country). Onbekend land telt als niet-US.
  Prijzen alleen in de US via de IF:US-macro; buiten de US "Up to 70% off" zonder bedrag. 12-delige set alleen via de USONLY-macro.
  Ankerprijzen gecontroleerd in Shopify 31 okt: Pan Pro 144/480, 6 Pcs 299/997, 12 Pcs 599/1997, Wok 24cm 119/397 (alle 70%). products.json is verouderd.
  (Standard $288). Vóór livegang controleren op de site; alleen tonen als de site exact dezelfde doorgestreepte prijs toont.
  Controleer vóór livegang dat de sale-prijzen zonder code gelden ("no code needed").
-->
<!-- MARKET-SIGNAL: profile -->
'''


def fmt(x, d):
    for k, v in d.items(): x = x.replace('%%(%s)s' % k, v)
    return x


def build(opt):
    t = TH[opt]
    out = []
    out.append(fmt(HEAD, dict(opt=opt.upper(), optname='editorial light' if opt == 'a' else 'dark minimal',
                           heroline='' if opt == 'a' else 'donker hero-beeld (exclusive 01 plinths), ')))
    out.append('''<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>You're just in time</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800;900&display=swap');
  body{margin:0;padding:0;background:%(outer)s;-webkit-text-size-adjust:100%%;}
  table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}
  img{border:0;display:block;line-height:100%%;outline:none;text-decoration:none;}
  @media only screen and (max-width:620px){
    .w{width:100%%!important;}
    .pad{padding-left:20px!important;padding-right:20px!important;}
    .navhide{display:none!important;}
    .h1{font-size:39px!important;line-height:42px!important;letter-spacing:-1.4px!important;}
    .lead{font-size:16px!important;line-height:24px!important;}
    .pn{font-size:28px!important;line-height:32px!important;}
    .si{width:140px!important;}
    .sg{width:16px!important;}
    .sn{font-size:18px!important;line-height:22px!important;}
    .sb{font-size:13px!important;line-height:18px!important;}
    .prs{font-size:20px!important;}
  }
</style>
</head>
<body style="margin:0;padding:0;background:%(outer)s;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;">Up to 70%% off is live, no code needed. Here's where I'd start.&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;</div>
<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%(outer)s" style="background-color:%(outer)s;">
<tr><td align="center" style="padding:0;">
<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background-color:%(bg)s;" bgcolor="%(bg)s">
''' % t)
    # 1 topbar
    bb = '' if opt == 'a' else 'border-bottom:1px solid %s;' % t['line']
    out.append('<tr><td align="center" bgcolor="%s" style="background-color:%s;padding:11px 20px;font-family:%s;font-size:11px;line-height:14px;letter-spacing:2.4px;font-weight:800;color:%s;text-transform:uppercase;%s">Black Friday Sale is live</td></tr>\n' % (t['bar_bg'], t['bar_bg'], F, t['bar_fg'], bb))
    # 2 header
    out.append('{{HEADER}}\n')
    # 3 hero
    if opt == 'b':
        out.append('<tr><td bgcolor="#0E0E0E" style="background-color:#0E0E0E;padding:0;"><a href="%s" style="text-decoration:none;"><img src="%ssiraat-collection-exclusive-01-plinths-desktop.jpg?width=1200" width="600" alt="Siraat hammered titanium pans on dark plinths" style="display:block;width:100%%;max-width:600px;height:auto;border:0;"></a></td></tr>\n' % (SALE, CDN))
    top = '52px' if opt == 'a' else '40px'
    out.append(row(t, '<div style="font-family:%s;font-size:12px;line-height:16px;font-weight:800;letter-spacing:2.4px;color:%s;text-transform:uppercase;">You\'re just in time</div>' % (F, t['mute']), '%s 40px 0 40px' % top))
    out.append(row(t, 'Up to 70% off.<br>No code needed.', '16px 40px 0 40px', cls='pad h1',
                   extra='font-family:%s;font-size:54px;line-height:56px;font-weight:900;letter-spacing:-2px;color:%s;' % (F, t['ink'])))
    out.append(row(t, 'The sale is live on the pans and sets people buy most. Here\'s where I\'d start.', '20px 40px 0 40px', cls='pad lead',
                   extra='font-family:%s;font-size:18px;line-height:27px;color:%s;' % (F, t['sub'])))
    out.append(row(t, button(t, 'Shop the sale', SALE), '28px 40px 0 40px'))
    out.append(row(t, '<div style="font-family:%s;font-size:12px;line-height:18px;color:%s;">Free shipping{{IF:US}}{{ELSE}}, duties paid{{ENDIF}}. 30-day returns.</div>' % (F, t['mute']), '14px 40px 48px 40px'))
    out.append(hair(t))
    # 4 products
    out.append(space(t, 40))
    out.append(hero_product(t, P['pan']))
    out.append(hair(t))
    out.append(side_product(t, P['set6']))
    out.append(hair(t))
    out.append('{{USONLY}}\n' + side_product(t, P['set12']) + '{{ELSEUS}}\n' + side_product(t, P['wok']) + '{{/USONLY}}\n')
    # 5 proof
    out.append(proof(t))
    # 6 sign-off
    out.append(signoff(t))
    out.append('''{{FOOTER}}
</table>
</td></tr>
</table>
</body>
</html>
''')
    h = ''.join(out)
    assert '—' not in h
    open(os.path.join(S, 'bf-w1-%s.html' % opt), 'w').write(h)


for o in 'ab':
    build(o)
print('ok')
