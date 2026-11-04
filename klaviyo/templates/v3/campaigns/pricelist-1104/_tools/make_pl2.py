"""Prijslijst wo 4 nov 2026, ronde 2 (Floris 4 nov): normale productfoto's, stijl van de Roasting Pan-mail (Instrument Serif italic,
Inter, crème packshots, gele BF-knoppen met ink tekst), Black Friday zichtbaar maar niet schreeuwerig. Producten: Crêpe Pan, Roasting Pan,
Wok Pan, Deep Pan. US: 12-Pcs voorop. INT: geen bedragen, alleen 70% OFF. Concept, niets live.
Gebruik (vanuit /tmp): python3 -I make_pl2.py. Daarna render_pl.py en shot_pl.js."""
import os, re
R = '/home/user/siraat-email-agent/klaviyo/templates/v3/campaigns/roasting-int/_tools/make_roast.py'
src = open(R).read().split('\nfiles = {}\n')[0]
g = {'__file__': R, '__name__': 'roasthelpers'}; exec(compile(src, R, 'exec'), g); globals().update({k: v for k, v in g.items() if not k.startswith('__')})
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOP = '{{BLOCK:bf-topbar text="VIP BLACK FRIDAY SALE IS LIVE" bg="#FFB800" color="#272727"}}\n{{HEADER}}\n'
def OPEN2(bg='#FFFFFF'):
    return '<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:%s;" bgcolor="%s">\n\n' % (bg, bg) + TOP
SQ = lambda n: CDN + n + '?width=600&height=600&crop=center&format=pjpg'
WIDE = lambda n: CDN + n + '?width=1200&height=780&crop=center&format=pjpg'
P_ = {  # key: (naam, beeld, url, korte regel)
 'crepe': ('Cr&ecirc;pe Pan Pro', 'Crepepan01.jpg', 'https://siraatskitchen.com/products/titanium-hammered-crepe-pan-pro', 'Flat and wide: cr&ecirc;pes, pancakes, tortillas.'),
 'roast': ('Roasting Pan', 'Roastingpanwithrack.webp', 'https://siraatskitchen.com/products/titanium-hammered-roasting-pan', 'With its fitted V-rack. New in stock.'),
 'wok': ('Wok Pan Pro', 'siraat-wok-real-side.jpg', 'https://siraatskitchen.com/products/titanium-hammered-wok-pan-pro', 'Deep and wide, to toss without spilling.'),
 'deep': ('Deep Pan Pro', 'DeepHammeredPan.webp', 'https://siraatskitchen.com/products/titanium-hammered-deep-pan-pro', 'Higher sides for sauces and one-pan dinners.'),
 'set6': ('Pan Set with Lids, 6&nbsp;Pcs', '6pcscookwareset.webp', 'https://siraatskitchen.com/products/titanium-hammered-pan-set-with-lids-6-pcs', 'Mini, Small and Large, each with its own lid.'),
 'standard': ('Pan Pro Standard', 'Titanium_hammered_pan_pro_standard_b69d1fc5-43d8-40a5-9ad7-523bdddc54d4.webp', 'https://siraatskitchen.com/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern', 'The everyday size. Start here.'),
}
SET12 = 'https://siraatskitchen.com/products/titanium-hammered-cookware-set-12-pcs-free-pizza-steel-1'
FRM = {'wok', 'deep'}
def u(url, camp, ct): return url + '?utm_source=klaviyo&utm_medium=email&utm_campaign=%s&utm_content=%s' % (camp, ct)
def off(size=12): return '<span style="display:inline-block;background-color:%s;color:%s;font-family:%s;font-size:%dpx;line-height:14px;font-weight:800;letter-spacing:0.6px;padding:5px 8px;border-radius:3px;white-space:nowrap;">70%% OFF</span>' % (Y, INK, FF, size)
def money_line(k, us):
    if not us: return off(13)
    f = '<span style="font-size:12px;font-weight:500;">from </span>' if k in FRM else ''
    return ('<span style="font-family:%s;font-size:20px;line-height:28px;font-weight:600;color:%s;white-space:nowrap;">%s{{PRICE:%s}}</span> '
            '<span style="font-family:%s;font-size:13px;line-height:28px;font-weight:600;color:#B5B5B5;text-decoration:line-through;">{{WAS:%s}}</span> %s') % (FF, INK, f, k, FF, k, off(11))
def card(k, us, camp, ct):
    n, im, url, line = P_[k]; link = u(url, camp, ct + '-' + k)
    return ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid %s;border-radius:10px;">'
            '<tr><td style="padding:0;border-radius:10px 10px 0 0;overflow:hidden;">%s</td></tr><tr><td style="padding:14px 14px 16px 14px;">%s%s<div style="padding-top:10px;">%s</div></td></tr></table>') % (
        HAIR, img(SQ(im), n.replace('&nbsp;', ' '), link, 270, 0),
        '<div style="font-family:%s;font-size:16px;line-height:20px;font-weight:600;color:%s;"><a href="%s" style="color:%s;text-decoration:none;">%s</a></div>' % (FF, INK, link, INK, n),
        txt(line, 13, 18, '#6E6A64', 400, 'padding-top:4px;'), money_line(k, us))
def grid4(keys, us, camp, ct, bg='#FFFFFF'):
    out = ''
    for i in range(0, len(keys), 2):
        out += row(bg, '0 20px 12px 20px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td width="50%%" valign="top" style="padding-right:6px;">%s</td><td width="50%%" valign="top" style="padding-left:6px;">%s</td></tr></table>' % (
            card(keys[i], us, camp, ct), card(keys[i + 1], us, camp, ct)), 'left', 'padx')
    return out
def listrow(k, us, camp, ct, last=False):
    n, im, url, line = P_[k]; link = u(url, camp, ct + '-' + k)
    return ('<tr><td width="96" valign="middle" style="padding:14px 0;%s"><a href="%s"><img src="%s" width="84" alt="%s" style="display:block;width:84px;height:84px;border-radius:8px;border:0;"></a></td>'
            '<td valign="middle" style="padding:14px 0 14px 12px;%s"><div style="font-family:%s;font-size:17px;line-height:22px;font-weight:600;color:%s;"><a href="%s" style="color:%s;text-decoration:none;">%s &rarr;</a></div>%s<div style="padding-top:8px;">%s</div></td></tr>') % (
        '' if last else 'border-bottom:1px solid %s;' % HAIR, link, SQ(im), n.replace('&nbsp;', ' '), '' if last else 'border-bottom:1px solid %s;' % HAIR,
        FF, INK, link, INK, n, txt(line, 13, 18, '#6E6A64', 400, 'padding-top:3px;'), money_line(k, us))
def bfband(t='VIP BLACK FRIDAY &nbsp;&middot;&nbsp; UP TO 70% OFF'):
    return row(INK, '15px 20px', txt(t, 13, 16, Y, 700, 'letter-spacing:2.4px;text-align:center;'), 'center', 'padx')
def pills2(a, b):
    return pill(a) + '<div style="height:6px;line-height:6px;font-size:0;">&nbsp;</div>' + pill(b, Y, INK)
WHY = [('No coatings, no PFAS', 'A pure titanium cooking surface, tested PFAS-free by Light Labs. Nothing to scratch, flake or wear off.'),
       ('One surface for everything', 'Sear, simmer, roast, flip. Stovetop and oven, induction included.'),
       ('Covered for 75 years', 'Because there is nothing on it to wear off, we can promise that. 30-day returns.')]
def meta2(id_, mkt, sender, subj, pre, why):
    who = ('Engaged 90D US v2 (VMjhb2) + No Country 90D (R5rFrC)' if mkt == 'US' else 'Engaged 90D INT v2 (XrFa5r)') + '; excl. kopers sinds 1 nov en aanmelders laatste 3 dagen; smart sending aan'
    return 'ID: %s\nMARKT: %s\nSENDER: %s\nSUBJECT A: %s\nSUBJECT B: %s\nPREVIEW: %s\nWANNEER: wo 4 nov 2026 08:15 lokale tijd\nWIE: %s\nWAAROM: %s' % (id_, mkt, sender, subj[0], subj[1], pre, who, why)
def bigoff(size=104, cls='big', sub='', pad='26px 20px 30px 20px', label=True):
    h = txt('VIP BLACK FRIDAY', 13, 16, Y, 700, 'letter-spacing:2.4px;text-align:center;padding-bottom:10px;') if label else ''
    h += '<div class="%s" style="font-family:%s;font-size:%dpx;line-height:%dpx;font-weight:900;letter-spacing:-4px;color:%s;text-align:center;">70%% OFF</div>' % (cls, FF, size, size - 2, Y)
    h += txt(sub, 16, 24, '#E6E3DC', 500, 'text-align:center;padding-top:12px;')
    return row(INK, pad, h, 'center', 'padx')
files = {}

# ---------- US-D: 12-Pcs als held in roasting-stijl, daaronder crepe/roast/wok/deep ----------
c = 'pl-1104-us'
m = meta2('pl-us-d · 12-Pcs in roasting-stijl', 'US', 'Siraat', ('The whole kitchen, 68% off', 'Our 12-piece set, at its VIP Black Friday price'),
          'The 12-piece titanium set with a free Pizza Steel. Just arrived and selling fast.', 'Ronde 2 Floris: normale foto&#39;s, eigen stijl, BF zichtbaar. 12-Pcs voorop voor de US.')
b = head(m, 'The whole kitchen, 68% off', 'The 12-piece titanium set with a free Pizza Steel. Just arrived and selling fast.') + OPEN2()
b += row(PACK, '30px 24px 0 24px', pills2('Just arrived', 'VIP Black Friday &nbsp;|&nbsp; 68% off'), 'center')
b += row(PACK, '18px 24px 0 24px', serif('The Titanium Hammered<br>Cookware Set, 12 Pcs', 46, 50, INK, 'h1', True), 'center')
b += row(PACK, '12px 40px 0 40px', txt('Three pans, two saucepans, a stockpot and a lid for every one. Pure titanium, hand-hammered, no coatings.', 17, 26, '#4A4A4A', 400, 'text-align:center;'), 'center')
b += row(PACK, '12px 0 0 0', img(WIDE('12pcsset.webp'), 'The Titanium Hammered Cookware Set, 12 Pcs', u(SET12, c, 'd-hero')), 'center', '')
b += bfband('VIP BLACK FRIDAY &nbsp;&middot;&nbsp; SELLING FAST')
b += row('#FFFFFF', '24px 20px 0 20px', '<table role="presentation" align="center" style="margin:0 auto;" cellpadding="0" cellspacing="0" border="0"><tr><td valign="middle" class="now" style="padding-right:12px;font-family:%s;font-size:52px;line-height:54px;font-weight:600;letter-spacing:-1px;color:%s;">{{PRICE:set12}}</td><td valign="middle" style="padding-right:12px;font-family:%s;font-size:20px;line-height:22px;font-weight:600;color:#B5B5B5;text-decoration:line-through;">{{WAS:set12}}</td><td valign="middle">%s</td></tr></table>' % (FF, INK, FF, off(13).replace('70%', '68%')), 'center', 'padx')
b += row('#FFFFFF', '12px 30px 0 30px', txt('<b style="color:%s;">+ a free Pizza Steel ($664 value)</b> and {{GIFTS:total}}. No code needed.' % INK, 15, 23, GREY, 500, 'text-align:center;'), 'center')
b += button('Get the 12-piece set', u(SET12, c, 'd-cta1'), '#FFFFFF', '22px 30px 30px 30px', fill=Y, fg=INK)
b += diamonds(WHY, '#FFFFFF', 'Why people replace everything at once')
b += row(CREAM, '30px 24px 6px 24px', serif('Or pick the pan you&#39;re missing', 34, 38, INK, 'h1b', True) + txt('Every pan below is 70% off for VIP Black Friday.', 15, 22, GREY, 500, 'padding-top:8px;'), 'center')
b += gap(CREAM, 14) + grid4(['crepe', 'roast', 'wok', 'deep'], True, c, 'd', CREAM) + gap(CREAM, 12)
b += gap('#FFFFFF', 24) + trust()
b += button('Shop VIP Black Friday', u('https://siraatskitchen.com/collections/black-friday-sale', c, 'd-cta-end'), '#FFFFFF', '4px 30px 34px 30px', fill=Y, fg=INK)
files['pl-us-d'] = b + TAIL

# ---------- US-E: rustige prijslijst (menukaart) ----------
m = meta2('pl-us-e · Prijslijst als menukaart', 'US', 'Siraat', ('The VIP Black Friday price list', 'Every price in one place'),
          'The 12-piece set first, then every pan. Up to 70% off, no code needed.', 'Prijzen verkopen, maar in onze eigen rustige stijl: lijst met foto, naam en prijs.')
b = head(m, 'The VIP Black Friday price list', 'The 12-piece set first, then every pan. Up to 70% off, no code needed.') + OPEN2()
b += row(PACK, '32px 24px 0 24px', pill('VIP Black Friday', Y, INK), 'center')
b += row(PACK, '16px 24px 0 24px', serif('The price list', 54, 56, INK, 'h1', True), 'center')
b += row(PACK, '10px 40px 26px 40px', txt('Up to 70% off. Free gifts with every order. No code needed.', 17, 26, '#4A4A4A', 400, 'text-align:center;'), 'center')
b += row('#FFFFFF', '24px 20px 0 20px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid %s;border-radius:10px;"><tr><td style="padding:0;border-radius:10px 10px 0 0;overflow:hidden;">%s</td></tr><tr><td style="padding:18px 20px 20px 20px;">%s%s%s<div style="padding-top:12px;">%s</div>%s</td></tr></table>' % (
    INK, img(WIDE('12pcsset.webp'), 'The Titanium Hammered Cookware Set, 12 Pcs', u(SET12, c, 'e-img'), 560),
    pill('#1 this week', INK, '#FFFFFF', False) + '<div style="height:6px;line-height:6px;font-size:0;">&nbsp;</div>' + pill('Just arrived &middot; selling fast', Y, INK, False),
    serif('Cookware Set, 12 Pcs', 32, 36, INK, 'h2', True, 'padding-top:10px;'), txt('3 pans, 2 saucepans, a stockpot and 6 fitted lids.', 15, 22, '#6E6A64', 400, 'padding-top:4px;'),
    '<span style="font-family:%s;font-size:34px;line-height:40px;font-weight:600;color:%s;">{{PRICE:set12}}</span> <span style="font-family:%s;font-size:16px;font-weight:600;color:#B5B5B5;text-decoration:line-through;">{{WAS:set12}}</span> %s' % (FF, INK, FF, off(12).replace('70%', '68%')),
    txt('+ FREE Pizza Steel ($664 value)', 15, 22, INK, 700, 'padding-top:10px;')), 'left', 'padx')
b += button('Get the 12-piece set', u(SET12, c, 'e-cta1'), '#FFFFFF', '18px 30px 26px 30px', fill=Y, fg=INK)
b += bfband('EVERY PAN &nbsp;&middot;&nbsp; 70% OFF')
rows_ = ''.join(listrow(k, True, c, 'e', i == 5) for i, k in enumerate(['crepe', 'roast', 'wok', 'deep', 'set6', 'standard']))
b += row('#FFFFFF', '8px 20px 6px 20px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % rows_, 'left', 'padx')
b += gap('#FFFFFF', 10) + trust()
b += button('Shop VIP Black Friday', u('https://siraatskitchen.com/collections/black-friday-sale', c, 'e-cta-end'), '#FFFFFF', '4px 30px 34px 30px', fill=Y, fg=INK)
files['pl-us-e'] = b + TAIL

# ---------- INT-C: zelfde stijl, 6-Pcs voorop, geen bedragen ----------
ci = 'pl-1104-int'
m = meta2('pl-int-c · Roasting-stijl, 6-Pcs voorop, zonder bedragen', 'INT', 'Siraat', ('VIP Black Friday: 70% off every pan', 'The pans you have been eyeing, 70% off'),
          'Cr&ecirc;pe, roasting, wok and deep pan. All 70% off, no code needed.', 'INT gemengde markten: geen valuta. Zelfde stijl als de Roasting Pan-mail van 2 nov.')
b = head(m, 'VIP Black Friday: 70% off every pan', 'Crêpe, roasting, wok and deep pan. All 70% off, no code needed.') + OPEN2()
b += row(PACK, '30px 24px 0 24px', pills2('Just arrived', 'VIP Black Friday &nbsp;|&nbsp; 70% off'), 'center')
b += row(PACK, '18px 24px 0 24px', serif('Every pan you&#39;ve<br>been eyeing', 48, 50, INK, 'h1', True), 'center')
b += row(PACK, '12px 40px 0 40px', txt('Pure titanium, hand-hammered, no coatings. For VIP Black Friday, all of it is 70% off.', 17, 26, '#4A4A4A', 400, 'text-align:center;'), 'center')
b += row(PACK, '12px 0 0 0', img(WIDE('6pcscookwareset.webp'), 'The Titanium Hammered Pan Set with Lids, 6 Pcs', u(P_['set6'][2], ci, 'c-hero')), 'center', '')
b += bigoff(96, 'big', 'No code needed. Plus 4 free gifts with every order.', '26px 20px 30px 20px', True)
b += button('Get the 6-piece set', u(P_['set6'][2], ci, 'c-cta1'), '#FFFFFF', '20px 30px 30px 30px', fill=Y, fg=INK)
b += row(CREAM, '30px 24px 6px 24px', serif('Pick your pan', 36, 40, INK, 'h1b', True) + txt('Every one of these is 70% off.', 15, 22, GREY, 500, 'padding-top:8px;'), 'center')
b += gap(CREAM, 14) + grid4(['crepe', 'roast', 'wok', 'deep'], False, ci, 'c', CREAM) + gap(CREAM, 12)
b += diamonds(WHY, '#FFFFFF', 'Why titanium', pad='24px 20px 20px 20px')
b += trust()
b += button('Shop VIP Black Friday', u('https://siraatskitchen.com/collections/black-friday-sale', ci, 'c-cta-end'), '#FFFFFF', '4px 30px 34px 30px', fill=Y, fg=INK)
files['pl-int-c'] = b + TAIL

# ---------- INT-D: menukaart zonder bedragen ----------
m = meta2('pl-int-d · Lijst zonder bedragen', 'INT', 'Siraat', ('The VIP Black Friday list', 'Every pan, 70% off'),
          'Six pans and sets, all 70% off. No code needed.', 'Rustige lijstvorm zonder valuta.')
b = head(m, 'The VIP Black Friday list', 'Six pans and sets, all 70% off. No code needed.') + OPEN2()
b += row(PACK, '32px 24px 0 24px', pill('VIP Black Friday', Y, INK), 'center')
b += row(PACK, '16px 24px 0 24px', serif('Everything is<br>70% off', 54, 56, INK, 'h1', True), 'center')
b += row(PACK, '10px 40px 26px 40px', txt('Pure titanium, no coatings. 4 free gifts with every order. No code needed.', 17, 26, '#4A4A4A', 400, 'text-align:center;'), 'center')
rows_ = ''.join(listrow(k, False, ci, 'd', i == 5) for i, k in enumerate(['set6', 'crepe', 'roast', 'wok', 'deep', 'standard']))
b += row('#FFFFFF', '12px 20px 6px 20px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % rows_, 'left', 'padx')
b += bfband('JUST ARRIVED &nbsp;&middot;&nbsp; SELLING FAST')
b += gap('#FFFFFF', 24) + trust()
b += button('Shop VIP Black Friday', u('https://siraatskitchen.com/collections/black-friday-sale', ci, 'd-cta-end'), '#FFFFFF', '4px 30px 34px 30px', fill=Y, fg=INK)
files['pl-int-d'] = b + TAIL

for k, v in files.items():
    assert '—' not in v, k
    body = v.split('-->', 1)[1]
    for bad in ('next batch', 'reserve', 'arriving', 'next shipment', 'Ends Monday'):
        assert bad not in body, (k, bad)
    if '-int-' in k: assert '$' not in body and not re.search(r'\{\{(PRICE|WAS|GIFTS)', body), k
    open(os.path.join(N, k + '.html'), 'w').write(v); print('geschreven', k, len(v))
