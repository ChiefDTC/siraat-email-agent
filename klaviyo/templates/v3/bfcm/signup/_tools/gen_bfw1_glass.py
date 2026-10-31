"""Genereert bf-w1-c/d/e.html (Smooche-achtige productkaarten met glaseffect) in klaviyo/templates/v3/bfcm/signup.
Basis: bf-w1-b (dark minimal). Kaarten blijven naast elkaar op mobiel (beeldkaart + glaspaneel, om en om gespiegeld)."""
import os
S = '/home/user/siraat-email-agent/klaviyo/templates/v3/bfcm/signup'
CDN = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/'
F = "Inter,Arial,Helvetica,sans-serif"
SALE = 'https://siraatskitchen.com/collections/black-friday-sale'

P = {
 'pan': dict(url='https://siraatskitchen.com/cart/add?id=51034913571156&quantity=1', page='https://siraatskitchen.com/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern',
   img=CDN+'Titanium_hammered_pan_pro_standard_b69d1fc5-43d8-40a5-9ad7-523bdddc54d4.webp?v=1781682831&width=600&format=pjpg',
   alt='Titanium Hammered Pan Pro Standard', name='Pan Pro Standard',
   b=['Pure titanium cooking surface', 'No coating, 75-year warranty'], now='$144', was='$480', btn='Add to cart'),
 'set6': dict(url='https://siraatskitchen.com/cart/add?id=55805001498964&quantity=1', page='https://siraatskitchen.com/products/titanium-hammered-pan-set-with-lids-6-pcs',
   img=CDN+'6pcscookwareset.webp?width=600&format=pjpg', alt='Titanium Hammered Pan Set with Lids, 6 pieces',
   name='Pan Set, 6&nbsp;Pcs', b=['3 pans and 3 fitted lids', 'Works on every stovetop'], now='$299', was='$997', btn='Add to cart'),
 'set12': dict(url='https://siraatskitchen.com/cart/add?id=55995692843348&quantity=1', page='https://siraatskitchen.com/products/titanium-hammered-cookware-set',
   img=CDN+'12pcsset.webp?width=600&format=pjpg', alt='Titanium Hammered Cookware Set, 12 pieces',
   name='Cookware Set, 12&nbsp;Pcs', b=['3 pans, 3 pots, 6 lids', 'The complete kitchen'], now='$599', was='$1,997', btn='Add to cart'),
 'wok': dict(url='https://siraatskitchen.com/products/titanium-hammered-wok-pan-pro', page='https://siraatskitchen.com/products/titanium-hammered-wok-pan-pro',
   img=CDN+'WokHammedPan_3.webp?v=1780301994&width=600&format=pjpg', alt='Titanium Hammered Wok Pan Pro',
   name='Wok Pan Pro', b=['Deep sides for stir-fries', 'Oven safe, 75-year warranty'], now='$119', was='$397', btn='Choose size'),
}

BASE = dict(page='#0E0E0E', ink='#FFFFFF', sub='#C9C5BD', mute='#8A867E', line='#2A2927', tile='#F5F2EC')
TH = {
 'c': dict(BASE, name='glass over vault, white pills', secbg='#0E0E0E', secimg=CDN+'siraat-collection-exclusive-08-vault-desktop.jpg?width=1200',
           hero=CDN+'siraat-collection-exclusive-01-plinths-desktop.jpg?width=1200', heroalt='Siraat hammered titanium pans on dark plinths',
           glass='rgba(24,24,24,0.72)', edge='rgba(255,255,255,0.20)', pill_bg='#FFFFFF', pill_fg='#272727',
           btn_bg='#FFFFFF', btn_fg='#272727', nm=22, nmm=16),
 'd': dict(BASE, name='glass over plinths, yellow pills', secbg='#0E0E0E', secimg=CDN+'siraat-collection-exclusive-01-plinths-desktop.jpg?width=1200',
           hero=CDN+'siraat-collection-exclusive-08-vault-desktop.jpg?width=1200', heroalt='Siraat hammered titanium pans in a dark vault',
           glass='rgba(24,24,24,0.72)', edge='rgba(255,255,255,0.20)', pill_bg='#FFB800', pill_fg='#272727',
           btn_bg='#FFFFFF', btn_fg='#272727', nm=25, nmm=18),
 'e': dict(BASE, name='clean solid #141414, subtle glass', secbg='#141414', secimg=None,
           hero=CDN+'siraat-collection-exclusive-01-plinths-desktop.jpg?width=1200', heroalt='Siraat hammered titanium pans on dark plinths',
           glass='rgba(255,255,255,0.05)', edge='rgba(255,255,255,0.12)', pill_bg='#FFFFFF', pill_fg='#272727',
           btn_bg='#FFFFFF', btn_fg='#272727', nm=22, nmm=16),
}


def row(t, html, pad, cls='pad', align='left', extra='', bg=None):
    bg = bg or t['page']
    return '<tr><td class="%s" align="%s" bgcolor="%s" style="background-color:%s;padding:%s;%s">%s</td></tr>\n' % (cls, align, bg, bg, pad, extra, html)


def button(t, label, url):
    return ('<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" bgcolor="#FFB800" style="background-color:#FFB800;">'
            '<!--[if mso]><v:rect xmlns:v="urn:schemas-microsoft-com:vml" href="%s" style="height:54px;v-text-anchor:middle;width:280px;" stroke="f" fillcolor="#FFB800"><center style="color:#272727;font-family:Arial,sans-serif;font-size:14px;font-weight:bold;letter-spacing:2px;">%s</center></v:rect><![endif]-->'
            '<!--[if !mso]><!--><a href="%s" style="display:block;padding:18px 34px;font-family:%s;font-size:14px;line-height:18px;font-weight:800;letter-spacing:2px;color:#272727;text-decoration:none;text-transform:uppercase;white-space:nowrap;">%s &rarr;</a><!--<![endif]-->'
            '</td></tr></table>') % (url, label.upper(), url, F, label)


def pill(t):
    return ('<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td class="pl" bgcolor="%s" style="background-color:%s;border-radius:999px;padding:6px 11px;'
            'font-family:%s;font-size:10px;line-height:12px;font-weight:800;letter-spacing:1.2px;color:%s;text-transform:uppercase;white-space:nowrap;">Up to 70%% off</td></tr></table>') % (t['pill_bg'], t['pill_bg'], F, t['pill_fg'])


def panel(t, p):
    bl = ''.join(('<tr><td class="bd" valign="top" width="12" style="width:12px;font-family:%s;font-size:14px;line-height:20px;color:%s;">&bull;</td>'
                  '<td class="bt" valign="top" style="font-family:%s;font-size:14px;line-height:20px;color:%s;padding-bottom:4px;">%s</td></tr>') % (F, t['mute'], F, t['sub'], b) for b in p['b'])
    price = ('{{IF:US}}<div style="padding-top:12px;"><span class="pr" style="font-family:%s;font-size:26px;line-height:30px;font-weight:900;letter-spacing:-0.6px;color:%s;">%s</span>'
             '&nbsp;<span class="pw" style="font-family:%s;font-size:14px;line-height:30px;color:%s;text-decoration:line-through;">%s</span></div>{{ELSE}}{{ENDIF}}') % (F, t['ink'], p['now'], F, t['mute'], p['was'])
    btn = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" bgcolor="%s" style="background-color:%s;border-radius:8px;">'
           '<a class="cb" href="%s" style="display:block;padding:13px 8px;font-family:%s;font-size:12px;line-height:16px;font-weight:800;letter-spacing:1.6px;color:%s;text-decoration:none;text-transform:uppercase;white-space:nowrap;border-radius:8px;">%s</a>'
           '</td></tr></table>') % (t['btn_bg'], t['btn_bg'], p['url'], F, t['btn_fg'], p['btn'])
    return ('<div class="pn" style="font-family:%s;font-size:%dpx;line-height:%dpx;font-weight:900;letter-spacing:-0.6px;color:%s;">'
            '<a href="%s" style="color:%s;text-decoration:none;">%s</a></div>'
            '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="margin-top:10px;">%s</table>'
            '%s<div class="bw" style="padding-top:16px;">%s</div>') % (F, t['nm'], t['nm'] + 4, t['ink'], p['page'], t['ink'], p['name'], bl, price, btn)


def card(t, p, img_left):
    """Beeldkaart en glaspaneel naast elkaar, ook op 375 px. Rowspan zorgt voor gelijke hoogte: pilrij + beeldrij links, paneel over twee rijen rechts."""
    pill_td = ('<td class="ip" width="47%%" valign="top" bgcolor="%s" style="width:47%%;background-color:%s;border-radius:12px 12px 0 0;padding:12px 12px 0 12px;">%s</td>') % (t['tile'], t['tile'], pill(t))
    img_td = ('<td class="ii" width="47%%" valign="middle" align="center" bgcolor="%s" style="width:47%%;background-color:%s;border-radius:0 0 12px 12px;padding:4px 8px 12px 8px;">'
              '<a href="%s" style="text-decoration:none;"><img src="%s" width="250" alt="%s" style="display:block;width:100%%;max-width:250px;height:auto;border:0;"></a></td>') % (t['tile'], t['tile'], p['page'], p['img'], p['alt'])
    gap = '<td class="cg" rowspan="2" width="12" style="width:12px;font-size:0;line-height:0;">&nbsp;</td>'
    pan = ('<td class="gp" rowspan="2" width="51%%" valign="middle" bgcolor="#1C1C1C" style="width:51%%;background-color:#1C1C1C;background-color:%s;border:1px solid #333333;border:1px solid %s;border-top-color:rgba(255,255,255,0.32);border-radius:12px;padding:20px 18px;">%s</td>') % (t['glass'], t['edge'], panel(t, p))
    if img_left:
        r1 = pill_td + gap + pan
    else:
        r1 = pan + gap + pill_td
    tb = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;"><tr>%s</tr><tr>%s</tr></table>' % (r1, img_td)
    return '<tr><td class="cp" style="padding:0 20px 14px 20px;">%s</td></tr>\n' % tb


def proof(t):
    cells = [('100,000+', 'customers'), ('75-year', 'warranty'), ('30-day', 'returns')]
    tds = ''.join(('<td width="33%%" align="center" valign="top" style="width:33%%;padding:18px 4px;%s">'
                   '<div class="pv" style="font-family:%s;font-size:22px;line-height:26px;font-weight:900;letter-spacing:-0.6px;color:%s;">%s</div>'
                   '<div style="font-family:%s;font-size:10px;line-height:14px;font-weight:800;letter-spacing:1.6px;color:%s;text-transform:uppercase;padding-top:4px;">%s</div></td>') % (
        '' if i == 0 else 'border-left:1px solid %s;' % t['line'], F, t['ink'], v, F, t['mute'], l) for i, (v, l) in enumerate(cells))
    tb = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid %s;border-bottom:1px solid %s;"><tr>%s</tr></table>' % (t['line'], t['line'], tds)
    return row(t, tb, '32px 40px 0 40px')


def signoff(t):
    body = ('<div style="font-family:%s;font-size:16px;line-height:25px;color:%s;">Not sure where to start? The Pan Pro Standard, our #1 seller. Reply if you get stuck, I read them.</div>'
            '<div style="font-family:%s;font-size:15px;line-height:22px;font-weight:800;color:%s;padding-top:12px;">Benjamin <span style="font-weight:400;color:%s;">&middot; Founder, Siraat</span></div>') % (F, t['sub'], F, t['ink'], t['mute'])
    return row(t, body, '28px 40px 40px 40px')


def section(t, opt):
    title = ('<tr><td class="st" align="center" style="padding:44px 20px 24px 20px;font-family:%s;font-size:34px;line-height:38px;font-weight:900;letter-spacing:-1px;color:#FFFFFF;">Discover the collection</td></tr>\n') % F
    cards = card(t, P['pan'], True) + card(t, P['set6'], False)
    cards += '{{USONLY}}\n' + card(t, P['set12'], True) + '{{ELSEUS}}\n' + card(t, P['wok'], True) + '{{/USONLY}}\n'
    inner = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">\n%s%s<tr><td style="height:26px;line-height:26px;font-size:0;">&nbsp;</td></tr>\n</table>' % (title, cards)
    if t['secimg']:
        return ('<tr><td background="%s" bgcolor="%s" valign="top" style="background-color:%s;background-image:url(\'%s\');background-position:center center;background-size:cover;background-repeat:no-repeat;">\n'
                '<!--[if gte mso 9]><v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width:600px;"><v:fill type="frame" src="%s" color="%s" /><v:textbox style="mso-fit-shape-to-text:true" inset="0,0,0,0"><![endif]-->\n'
                '%s\n<!--[if gte mso 9]></v:textbox></v:rect><![endif]-->\n</td></tr>\n') % (t['secimg'], t['secbg'], t['secbg'], t['secimg'], t['secimg'], t['secbg'], inner)
    return '<tr><td bgcolor="%s" style="background-color:%s;border-top:1px solid #222222;">\n%s\n</td></tr>\n' % (t['secbg'], t['secbg'], inner)


HEAD = '''<!--
BF SIGNUP FLOW · W1 OPTIE %(OPT)s "%(name)s" (31 okt 2026). Variant op bf-w1-b (dark minimal) na feedback Floris op zijn iPhone (Gmail):
  regel "Free shipping. 30-day returns." onder de heroknop en de witruimte eronder weg; producten als Smooche "Discover The Collection":
  beeldkaart (#F5F2EC, pil UP TO 70%% OFF) en glaspaneel (naam, 2 bullets, ADD TO CART) naast elkaar, ook op mobiel, om en om gespiegeld.
  Glas is nagebootst (geen backdrop-filter): rgba-paneel met 1px rgba-rand, vaste terugval #1C1C1C. Sectie: %(secline)s.
  Volgorde: Pan Pro Standard, 6-delige set, US: 12-delige set / niet-US: Wok Pan Pro (CHOOSE SIZE naar productpagina, heeft maten).
  ADD TO CART-knoppen gaan naar /cart/add?id=...&quantity=1. Generator: scratchpad bfw1tools/gen_bfw1_glass.py.
SUBJECT: You're just in time 🧡
PREVIEW: Up to 70%% off is live, no code needed. Here's where I'd start.
MARKET-SIGNAL: profile (person.Country). Onbekend land telt als niet-US.
  Prijzen alleen in de US via de IF:US-macro; buiten de US geen bedragen. 12-delige set alleen via de USONLY-macro.
  Ankerprijzen gecontroleerd in Shopify 31 okt: Pan Pro 144/480, 6 Pcs 299/997, 12 Pcs 599/1997 (alle 70%%). Vóór livegang controleren op de site.
-->
<!-- MARKET-SIGNAL: profile -->
'''

CSS = '''<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800;900&display=swap');
  body{margin:0;padding:0;background:#0E0E0E;-webkit-text-size-adjust:100%%;}
  table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}
  img{border:0;display:block;line-height:100%%;outline:none;text-decoration:none;}
  @media only screen and (max-width:620px){
    .w{width:100%%!important;}
    .pad{padding-left:20px!important;padding-right:20px!important;}
    .navhide{display:none!important;}
    .h1{font-size:39px!important;line-height:42px!important;letter-spacing:-1.4px!important;}
    .lead{font-size:16px!important;line-height:24px!important;}
    .st{font-size:26px!important;line-height:30px!important;padding:34px 16px 18px 16px!important;}
    .cp{padding:0 12px 10px 12px!important;}
    .cg{width:8px!important;}
    .ip{padding:9px 8px 0 8px!important;}
    .pl{font-size:8.5px!important;line-height:10px!important;letter-spacing:0.8px!important;padding:5px 8px!important;}
    .ii{padding:4px 4px 8px 4px!important;}
    .gp{padding:14px 11px!important;}
    .pn{font-size:%(nmm)dpx!important;line-height:%(nmml)dpx!important;letter-spacing:-0.3px!important;}
    .bd{width:9px!important;font-size:12px!important;line-height:16px!important;}
    .bt{font-size:12px!important;line-height:16px!important;padding-bottom:3px!important;}
    .pr{font-size:19px!important;line-height:22px!important;}
    .pw{font-size:12px!important;line-height:22px!important;}
    .bw{padding-top:12px!important;}
    .cb{font-size:10.5px!important;letter-spacing:1.1px!important;padding:11px 4px!important;}
    .pv{font-size:19px!important;line-height:22px!important;}
  }
</style>'''


def build(opt):
    t = TH[opt]
    out = [HEAD % dict(OPT=opt.upper(), name=t['name'], secline=('achtergrondbeeld %s via background-attribuut + CSS, VML voor Outlook, bgcolor %s als terugval' % (t['secimg'].split('/')[-1].split('?')[0], t['secbg'])) if t['secimg'] else 'geen beeld, effen #141414')]
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
''' + CSS % dict(nmm=t['nmm'], nmml=t['nmm'] + 3) + '''
</head>
<body style="margin:0;padding:0;background:#0E0E0E;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;">Up to 70% off is live, no code needed. Here's where I'd start.&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#0E0E0E" style="background-color:#0E0E0E;">
<tr><td align="center" style="padding:0;">
<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background-color:#0E0E0E;" bgcolor="#0E0E0E">
''')
    out.append('<tr><td align="center" bgcolor="#0E0E0E" style="background-color:#0E0E0E;padding:11px 20px;font-family:%s;font-size:11px;line-height:14px;letter-spacing:2.4px;font-weight:800;color:#FFFFFF;text-transform:uppercase;border-bottom:1px solid %s;">Black Friday Sale is live</td></tr>\n' % (F, t['line']))
    out.append('{{HEADER}}\n')
    out.append('<tr><td bgcolor="#0E0E0E" style="background-color:#0E0E0E;padding:0;"><a href="%s" style="text-decoration:none;"><img src="%s" width="600" alt="%s" style="display:block;width:100%%;max-width:600px;height:auto;border:0;"></a></td></tr>\n' % (SALE, t['hero'], t['heroalt']))
    out.append(row(t, '<div style="font-family:%s;font-size:12px;line-height:16px;font-weight:800;letter-spacing:2.4px;color:%s;text-transform:uppercase;">You\'re just in time</div>' % (F, t['mute']), '40px 40px 0 40px'))
    out.append(row(t, 'Up to 70% off.<br>No code needed.', '16px 40px 0 40px', cls='pad h1',
                   extra='font-family:%s;font-size:54px;line-height:56px;font-weight:900;letter-spacing:-2px;color:%s;' % (F, t['ink'])))
    out.append(row(t, 'The sale is live on the pans and sets people buy most. Here\'s where I\'d start.', '20px 40px 0 40px', cls='pad lead',
                   extra='font-family:%s;font-size:18px;line-height:27px;color:%s;' % (F, t['sub'])))
    out.append(row(t, button(t, 'Shop the sale', SALE), '28px 40px 36px 40px'))
    out.append(section(t, opt))
    out.append(proof(t))
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


for o in 'cde':
    build(o)
print('ok')
