"""Homestead E5 (di 10 nov, Weekly Recipe: Thanksgiving sides) en E6 (wo 11 nov, founder-brief Pan Pro Standard), elk 3 varianten
(A, B, C) in US en INT: 12 mails. Copy letterlijk uit research/homestead/2026-11-e5-e6/copy.md, UX uit ux.md (knop en beeld in het
eerste scherm op 375 px, echte knoppen, BF-aanbod niet alleen in de P.S.). Stijl: helpers uit pricelist-1104/_tools/make_pl2.py
(Floris 4 nov). US: prijzen via {{PRICE:x|$..}} / {{WAS:x|$..}} met vaste US-terugval; INT: geen bedragen, geen valuta.
Beelden: alleen echte Shopify-CDN-beelden van Siraat (packshots en PDP-lifestyle), geen AI-beelden. Concept, niets live.
Gebruik (vanuit /tmp): python3 -I make_e56.py, daarna render_e56.py en shot_e56.js."""
import os, re, sys
S = '/home/user/siraat-email-agent/klaviyo/templates/v3/campaigns/pricelist-1104/_tools/make_pl2.py'
src = open(S).read().split('\nfiles = {}\n')[0]
g = {'__file__': S, '__name__': 'pl2helpers'}; exec(compile(src, S, 'exec'), g); globals().update({k: v for k, v in g.items() if not k.startswith('__')})
sys.path.insert(0, '/home/user/siraat-email-agent/scripts'); import v5lib as V
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- vaste waarden
TOPBAR = 'VIP BLACK FRIDAY SALE IS LIVE'   # VIP-label in alle mails (Floris 2 nov)
SALE = 'https://siraatskitchen.com/collections/black-friday-sale'
PRD = 'https://siraatskitchen.com/products/'
URL = {'large': PRD + 'titanium-hammered-pan-pro-large', 'deep': PRD + 'titanium-hammered-deep-pan-pro',
       'standard': PRD + 'original-siraat-100-pure-titanium-pan-with-hammered-pattern',
       'set6': PRD + 'titanium-hammered-pan-set-with-lids-6-pcs', 'set12': PRD + 'titanium-hammered-cookware-set-12-pcs-free-pizza-steel-1'}
PK = {'large': 'Titanium_hammered_pan_pro_large_6d4ce352-c4ff-48c9-b4d1-170232007e4f.webp', 'deep': 'DeepHammeredPan.webp',
      'standard': 'Titanium_hammered_pan_pro_standard_b69d1fc5-43d8-40a5-9ad7-523bdddc54d4.webp',
      'set6': '6pcscookwareset.webp', 'set12': '12pcsset.webp'}
NAME = {'large': 'Pan Pro Large', 'deep': 'Deep Pan Pro', 'standard': 'Pan Pro Standard', 'set6': '6-piece set', 'set12': '12-piece set'}
FAMILY = 'siraat-titanium-hammered-deep-pan-10-family-dinner.webp'
RAGU = 'siraat-titanium-hammered-deep-pan-01-ragu-on-the-stove.webp'
BRAISE = 'siraat-titanium-hammered-deep-pan-05-chicken-braise.webp'
C43 = lambda n: n if n.startswith('http') else CDN + n + '?width=1200&height=900&crop=center&format=pjpg'
C32 = lambda n: n if n.startswith('http') else CDN + n + '?width=1200&height=800&crop=center&format=pjpg'
# Nieuwe beelden (Higgsfield, 5 nov; Floris: betere beelden)
IM_TABLE = 'https://cdn.klaviyomail.com/company/TdtTzz/images/96090f37-154b-4105-9419-fd63b5cbbc72.jpeg'
IM_SWEET = 'https://cdn.klaviyomail.com/company/TdtTzz/images/b9d86771-f8e2-4154-97ee-10e620db8b96.jpeg'
IM_BEANS = 'https://cdn.klaviyomail.com/company/TdtTzz/images/2383c27e-e535-41f0-90bf-2f922c8b7219.jpeg'
IM_EGG = 'https://cdn.klaviyomail.com/company/TdtTzz/images/2a5217ee-dceb-4c59-86f4-de5456855eab.jpeg'
IM_VET = 'https://cdn.klaviyomail.com/company/TdtTzz/images/0b4b0787-1355-4d98-b8bb-479c9659c3df.jpeg'

C11 = lambda n: CDN + n + '?width=1200&height=1200&crop=center&format=pjpg'
SQ2 = lambda n: CDN + n + '?width=1200&height=1200&crop=center&format=pjpg'
FR_INT = 'Free shipping, duties paid. 30-day returns. 100,000+ happy customers.'
def FRIC(us): return '{{FRICTION}}' if us else FR_INT

# US-bedragen uit de catalogus (scripts/v5lib.py), als terugval in de macro's en voor de berekende placeholders
def usd(x): return V.money(x, 'US')
AMT = {k: (V.amount(k, 'US', 'price'), V.amount(k, 'US', 'compare_at')) for k in ('standard', 'large', 'deep', 'set6', 'set12')}
SAVE_STD = usd(AMT['standard'][1] - AMT['standard'][0])                                   # {{SAVE:standard}} = $336
STACK_STD = usd(AMT['standard'][1] + sum(V.GIFT['US'][i] for i in (0, 1, 2)))             # {{STACK:standard}} = $550 (filter telt niet mee)
def PRICE(k): return ('{{FROM:%s|from %s}}' % (k, usd(AMT[k][0]))) if k == 'deep' else '{{PRICE:%s|%s}}' % (k, usd(AMT[k][0]))
def WAS(k): return '{{WAS:%s|%s}}' % (k, usd(AMT[k][1]))
def PCT(k): return round(100 - 100 * AMT[k][0] / AMT[k][1])
def gv(k): return '{{IF:US}} ({{GIFTS:%s}}){{ENDIF}}' % k   # gift-waarde US tussen haakjes, leeg bij onbekend land

head.__globals__['CSS'] += ('    .h1s{font-size:30px!important;line-height:34px!important;}\n    .rpad{padding-left:16px!important;padding-right:16px!important;}\n'
                            '    .ptitle{font-size:26px!important;line-height:30px!important;}\n    .thumb{width:96px!important;}\n')

def utm(url, camp, ct): return u(url, camp, ct)
def topbar(): return '{{BLOCK:bf-topbar text="<a href=\'%s\' style=\'color:#F8F7F2;text-decoration:none;\'>%s</a>" bg="#272727" color="#F8F7F2"}}\n{{HEADER}}\n' % (SALE, TOPBAR)
def OPEN3(bg='#FFFFFF'):
    return '<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:%s;" bgcolor="%s">\n\n' % (bg, bg) + topbar()
def HEAD(meta_, subj, pre):
    return head(meta_, subj, pre).replace('ROASTING PAN INT · NEW IN STOCK + BLACK FRIDAY SPECIAL (concept 1 nov 2026, niet in Klaviyo, niets live).',
                                          'HOMESTEAD E5/E6 · NOVEMBER 2026 (concept 5 nov 2026, niet in Klaviyo, niets live).')
def meta4(id_, mkt, sender, subj, pre, when, who, why):
    return 'ID: %s\nMARKT: %s\nSENDER: %s\nSUBJECT A: %s\nSUBJECT B: %s\nPREVIEW: %s\nWANNEER: %s\nWIE: %s\nWAAROM: %s' % (id_, mkt, sender, subj[0], subj[1], pre, when, who, why)

# ---------------------------------------------------------------- bouwstenen
def badge(t, size=11): return off(size).replace('>70% OFF<', '>%s<' % t)
def price_line(k, us, int_label='70% OFF', big=20):
    if not us: return badge(int_label.upper(), 12)
    return ('<span style="font-family:%s;font-size:%dpx;line-height:28px;font-weight:600;color:%s;white-space:nowrap;">%s</span> '
            '<span style="font-family:%s;font-size:13px;line-height:28px;font-weight:600;color:#B5B5B5;text-decoration:line-through;white-space:nowrap;">%s</span> %s') % (
        FF, big, INK, PRICE(k), FF, WAS(k), badge('%d%% OFF' % PCT(k)))
def sbtn(label, url, full=False):
    if full:
        return ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="margin-top:12px;"><tr><td align="center" bgcolor="%s" style="background-color:%s;border-radius:20px;">'
                '<a href="%s" style="display:block;padding:11px 8px;font-family:%s;font-size:12px;line-height:15px;font-weight:700;letter-spacing:0.6px;color:%s;text-decoration:none;text-transform:uppercase;text-align:center;">%s &rarr;</a></td></tr></table>') % (INK, INK, url, FF, '#FFFFFF', label)
    return ('<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin-top:12px;"><tr><td bgcolor="%s" style="background-color:%s;border-radius:20px;">'
            '<a href="%s" style="display:block;padding:11px 14px;font-family:%s;font-size:12px;line-height:14px;font-weight:700;letter-spacing:0.8px;color:%s;text-decoration:none;text-transform:uppercase;white-space:nowrap;">%s &rarr;</a></td></tr></table>') % (INK, INK, url, FF, '#FFFFFF', label)
def hero(label, title, sub, image, alt, link, ratio=C32, pad_title='12px 24px 0 24px'):
    h = row(PACK, '22px 24px 0 24px', pill(label, INK, '#FFFFFF'), 'center')
    h += row(PACK, pad_title, serif(title, 46, 50, INK, 'h1', True), 'center')
    h += row(PACK, '8px 36px 14px 36px', txt(sub, 17, 25, '#4A4A4A', 400, 'text-align:center;'), 'center')
    h += row(PACK, '0', img(ratio(image), alt, link), 'center', '')
    return h
def offerbar(t): return row(INK, '12px 16px', txt(t, 12, 17, '#F8F7F2', 700, 'letter-spacing:1.4px;text-align:center;'), 'center', 'padx')
def heading(t, bg='#FFFFFF', pad='30px 24px 6px 24px', sub=''):
    return row(bg, pad, serif(t, 34, 38, INK, 'h1b', True) + (txt(sub, 15, 22, GREY, 500, 'padding-top:8px;') if sub else ''), 'center')
def closing(t, bg='#FFFFFF'): return P(t, bg, '6px 40px 4px 40px')
def ps(t, bg='#FFFFFF'): return P('<b>P.S.</b> ' + t, bg, '8px 40px 14px 40px')
def small(t, bg='#FFFFFF'): return row(bg, '10px 30px 26px 30px', txt(t, 12, 18, '#8A847A', 400, 'text-align:center;'), 'center')
def numbered(steps, start=1):
    r = ''.join('<tr><td width="38" valign="top" style="padding:0 0 12px 0;"><div style="width:26px;height:26px;border-radius:13px;background-color:%s;font-family:%s;font-size:13px;line-height:26px;font-weight:800;color:%s;text-align:center;">%d</div></td><td valign="top" style="padding:2px 0 12px 0;">%s</td></tr>' % (
        INK, FF, '#FFFFFF', i, txt(s, 16, 24, '#2E2E2E')) for i, s in enumerate(steps, start))
    return '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % r
def bullets(items, color='#2E2E2E', dot=GOLD, size=16, lh=24):
    r = ''.join('<tr><td width="20" valign="top" style="padding:%dpx 0 0 2px;"><div style="width:7px;height:7px;background-color:%s;transform:rotate(45deg);-webkit-transform:rotate(45deg);font-size:0;line-height:0;">&nbsp;</div></td><td valign="top" style="padding:0 0 8px 0;">%s</td></tr>' % (
        (lh - 7) // 2, dot, txt(t, size, lh, color)) for t in items)
    return '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % r
def eyebrow(t, color=INK, extra=''): return txt(t, 12, 16, color, 700, 'letter-spacing:1.6px;text-transform:uppercase;' + extra)
def boxed(inner, border=HAIR, bg='#FFFFFF', pad='20px'):
    return '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%s" style="background-color:%s;border:1px solid %s;border-radius:10px;"><tr><td style="padding:%s;">%s</td></tr></table>' % (bg, bg, border, pad, inner)
def prodhead(k, title, meta_, link):
    """Kop van een receptkaart: kleine packshot links, titel en meta-regel rechts."""
    return ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td width="80" valign="middle" style="padding:0 14px 0 0;"><a href="%s"><img src="%s" width="72" alt="%s" style="display:block;width:72px;height:72px;border-radius:8px;border:0;"></a></td>'
            '<td valign="middle">%s%s</td></tr></table>') % (link, SQ(PK[k]), 'Siraat ' + NAME[k], serif(title, 28, 31, INK, 'ptitle', True), txt(meta_, 14, 20, GREY, 500, 'padding-top:4px;'))
def recipe(k, title, meta_, need, steps, ahead, note, link):
    i = prodhead(k, title, meta_, link)
    i += eyebrow('You need', INK, 'padding:18px 0 8px 0;') + bullets([x.strip() for x in need])
    i += eyebrow('Method', INK, 'padding:10px 0 10px 0;') + numbered(steps)
    i += '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%s" style="background-color:%s;border-radius:8px;margin-top:4px;"><tr><td style="padding:14px 16px;">%s</td></tr></table>' % (CREAM, CREAM, txt('<b>Make ahead:</b> ' + ahead, 15, 23, INK))
    i += txt(note, 15, 23, '#4A4A4A', 400, 'padding-top:14px;')
    return row('#FFFFFF', '6px 20px 0 20px', boxed(i, HAIR, '#FFFFFF', '20px 18px 18px 18px'), 'left', 'padx')
def daycard(day, title, meta_, body, bullets_=None):
    i = pill(day, INK, '#FFFFFF', False) + serif(title, 28, 31, INK, 'ptitle', True, 'padding-top:12px;') + txt(meta_, 14, 20, GREY, 500, 'padding-top:4px;')
    i += (txt(body, 16, 25, '#2E2E2E', 400, 'padding-top:12px;') if body else '') + ('<div style="padding-top:12px;">%s</div>' % bullets(bullets_) if bullets_ else '')
    return row('#FFFFFF', '0 20px 12px 20px', boxed(i, HAIR, '#FFFFFF', '20px 18px 18px 18px'), 'left', 'padx')
def wide_card(k, line, us, int_label, label, link):
    """Productkaart over de volle breedte: packshot links, naam, regel, prijs en knop rechts. Werkt op 375 en 600 px."""
    i = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td width="132" class="thumb" valign="top" style="padding:0 14px 0 0;"><a href="%s"><img src="%s" width="118" alt="Siraat %s" style="display:block;width:100%%;max-width:118px;height:auto;border-radius:8px;border:0;"></a></td>'
         '<td valign="top">%s%s<div style="padding-top:8px;">%s</div>%s</td></tr></table>') % (
        link, SQ(PK[k]), NAME[k], '<div style="font-family:%s;font-size:17px;line-height:22px;font-weight:600;color:%s;"><a href="%s" style="color:%s;text-decoration:none;">%s</a></div>' % (FF, INK, link, INK, NAME[k]),
        txt(line, 14, 20, '#6E6A64', 400, 'padding-top:4px;'), price_line(k, us, int_label, 20), sbtn(label, link))
    return row('#FFFFFF', '0 20px 12px 20px', boxed(i, HAIR, '#FFFFFF', '14px'), 'left', 'padx')
def gcard(k, line, us, int_label, label, link, sticker=''):
    st = ('<div style="padding-bottom:8px;">%s</div>' % pill(sticker, INK, '#FFFFFF', False, 10)) if sticker else ''
    return ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid %s;border-radius:10px;">'
            '<tr><td style="padding:0;border-radius:10px 10px 0 0;overflow:hidden;">%s</td></tr><tr><td style="padding:12px 12px 14px 12px;">%s%s%s<div style="padding-top:8px;">%s</div>%s</td></tr></table>') % (
        HAIR, img(SQ(PK[k]), 'Siraat ' + NAME[k], link, 270, 0), st,
        '<div style="font-family:%s;font-size:16px;line-height:20px;font-weight:600;color:%s;"><a href="%s" style="color:%s;text-decoration:none;">%s</a></div>' % (FF, INK, link, INK, NAME[k]),
        txt(line, 13, 18, '#6E6A64', 400, 'padding-top:4px;'), price_line(k, us, int_label, 18), sbtn(label, link, True))
def grid(cards, bg=CREAM):
    out = ''
    for i in range(0, len(cards), 2):
        out += row(bg, '0 20px 12px 20px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td width="50%%" valign="top" style="padding-right:6px;">%s</td><td width="50%%" valign="top" style="padding-left:6px;">%s</td></tr></table>' % (cards[i], cards[i + 1]), 'left', 'padx')
    return out
REVS = {'R562': ("The Deep Pan Pro is my 'go to' favourite because I like to cook big meals", 'M. K.'),
        'R518': ('We cooked the best omelette we have ever eaten when we used the pan for the first time.', 'Graham C.'),
        'R411': ('I purchased the hammered pro pan standard. It is beautiful and lightweight.', 'Deb'),
        'R138': ("I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns.", 'Tammy'),
        'R583': ('These hammered Titanium pans from Siraat have been the best we have owned yet... the last pans we ever have to purchase.', 'Scott Y.'),
        'R240': ('Siraat replaced a pan free of charge... I just sent them the picture and they honored the warranty.', 'Brandon W.'),
        'R169': ('The real test was my egg the next morning... the egg released completely and slid around the pan like it was non-stick.', 'Michael G.'),
        'R011': ('We have purchased twice from Siraat... Expensive but definitely Value for money. Quality cookware!', 'Lorraine'),
        'R399': ('My deliveries were prompt and I live in Melbourne, Australia... I love their titanium cookware', 'Anthony')}
def revblock(ids, bg=CREAM, title='From their kitchens', pad='28px 20px 26px 20px'):
    h = txt('<span style="color:%s;letter-spacing:3px;">&#9733;&#9733;&#9733;&#9733;&#9733;</span>' % GOLD, 18, 22, INK, 400, 'text-align:center;') + txt(title, 15, 22, INK, 600, 'text-align:center;padding-top:4px;')
    for k in ids:
        q, n = REVS[k]
        h += '<div style="height:12px;line-height:12px;font-size:0;">&nbsp;</div>' + boxed(txt('&#9733;&#9733;&#9733;&#9733;&#9733;', 13, 15, GOLD, 400, 'letter-spacing:2px;') + txt('&ldquo;%s&rdquo;' % q, 16, 24, INK, 500, 'padding-top:8px;') + txt('%s &middot; Verified buyer' % n, 13, 18, '#8A847A', 500, 'padding-top:8px;'), '#FFFFFF', '#FFFFFF', '18px 20px')
    return row(bg, pad, h, 'left', 'padx')
def quote(k, bg='#FFFFFF'):
    q, n = REVS[k]
    i = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-left:3px solid %s;padding:2px 0 2px 16px;">%s%s</td></tr></table>' % (
        GOLD, txt('&ldquo;%s&rdquo;' % q, 17, 26, INK, 500), txt('%s, verified buyer' % n, 13, 18, '#8A847A', 500, 'padding-top:6px;'))
    return row(bg, '0 40px 18px 40px', i, 'left', 'pad')
def dark_button(label, url, sub): return button(label, url, ESP, '22px 30px 30px 30px', sub=sub, fill='#FFFFFF', fg=INK, dark=True)
def bfband_full(us, camp, ct):
    """BF-band uit copy.md sectie 1 (espresso-blok in offer-stijl)."""
    h = txt('VIP BLACK FRIDAY', 13, 16, '#D9C9A8', 700, 'letter-spacing:2.4px;text-align:center;padding-bottom:12px;')
    h += serif('Up to 70% off, plus 4 gifts<br>with every order.', 36, 40, '#FFFFFF', 'h1b', True, 'text-align:center;')
    gl = (['Free shipping%s' % gv('ship'), 'The Plastic-Free Home e-book%s' % gv('ebook'), 'A mystery gift%s' % gv('mystery'), 'A weekly chance to win {{GIFTS:filterline}}'] if us else
          ['Free shipping, duties paid', 'The Plastic-Free Home e-book', 'A mystery gift', 'A weekly chance to win a PFAS water filter'])
    h += '<div style="padding:18px 6px 0 6px;">%s</div>' % bullets(gl, '#E6E3DC', GOLD, 15, 22)
    if us: h += txt('With the 12-piece set: a Titanium Hammered Pizza Steel, free.', 15, 22, '#FFFFFF', 600, 'padding:6px 6px 0 6px;')
    h += txt('Ends Monday, November 30.' if us else 'Ends Monday 30 November.', 14, 20, '#E6E3DC', 600, 'padding-top:14px;text-align:center;')
    out = row(ESP, '30px 26px 0 26px', h, 'left', 'pad')
    return out + dark_button('Get my Black Friday price', utm(SALE, camp, ct + '-band'), FRIC(us))
def gifts_tiles(us, bg='#FFFFFF'):
    it = ([('Free shipping', '{{GIFTS:ship}} value'), ('Plastic-Free Home e&#8209;book', '{{GIFTS:ebook}} value'), ('Mystery gift', '{{GIFTS:mystery}} value'), ('Chance to win {{GIFTS:filterline}}', 'Weekly draw')] if us else
          [('Free shipping, duties paid', 'Included'), ('Plastic-Free Home e&#8209;book', 'Included'), ('Mystery gift', 'Included'), ('Chance to win a PFAS water filter', 'Weekly draw')])
    GI = ['gift-shipping.jpg', 'gift-ebook.jpg', 'gift-mystery.jpg', 'gift-filter.jpg']
    cell = lambda a, b, n: '<td width="50%%" valign="top" style="padding:0 5px 10px 5px;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid #E9E4DA;border-radius:8px;"><tr><td style="padding:0;border-radius:8px 8px 0 0;overflow:hidden;"><img src="{{SHARED}}/%s" width="270" alt="%s" style="display:block;width:100%%;max-width:270px;height:auto;border:0;border-radius:8px 8px 0 0;"></td></tr><tr><td align="center" style="padding:12px 10px 14px 10px;">%s%s</td></tr></table></td>' % (
        GI[n - 1], re.sub('<[^>]+>|&[^;]+;', ' ', a), txt(a, 14, 19, INK, 600, 'text-align:center;'), txt(b, 12, 17, '#8A847A', 500, 'text-align:center;padding-top:3px;'))
    t = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>%s%s</tr><tr>%s%s</tr></table>' % tuple(cell(a, b, i + 1) for i, (a, b) in enumerate(it))
    return row(bg, '26px 20px 14px 20px', serif('4 gifts with every order', 30, 34, INK, 'h1s', True, 'text-align:center;padding-bottom:16px;') + t, 'center', 'padx')
def pricebar(k, us, int_label='70% OFF', bg='#FFFFFF', pad='22px 20px 0 20px'):
    if not us: return row(bg, pad, '<div style="text-align:center;">%s</div>' % badge(int_label, 14), 'center', 'padx')
    t = ('<table role="presentation" align="center" style="margin:0 auto;" cellpadding="0" cellspacing="0" border="0"><tr><td valign="middle" class="now" style="padding-right:12px;font-family:%s;font-size:48px;line-height:50px;font-weight:600;letter-spacing:-1px;color:%s;white-space:nowrap;">%s</td>'
         '<td valign="middle" style="padding-right:12px;font-family:%s;font-size:20px;line-height:22px;font-weight:600;color:#B5B5B5;text-decoration:line-through;white-space:nowrap;">%s</td><td valign="middle">%s</td></tr></table>') % (FF, INK, PRICE(k), FF, WAS(k), badge('%d%% OFF' % PCT(k), 13))
    return row(bg, pad, t, 'center', 'padx')
def mini_offer(us, camp, ct, label='Get my Pan Pro at 70% off'):
    """Compacte productkaart in de brief (UX: beeld, prijs en knop binnen het eerste scherm)."""
    link = utm(URL['standard'], camp, ct)
    i = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td width="96" valign="top" style="padding:0 14px 0 0;"><a href="%s"><img src="%s" width="84" alt="Siraat Pan Pro Standard" style="display:block;width:84px;height:84px;border-radius:8px;border:0;"></a></td>'
         '<td valign="top"><div style="font-family:%s;font-size:17px;line-height:22px;font-weight:600;color:%s;"><a href="%s" style="color:%s;text-decoration:none;">Pan Pro Standard</a></div><div style="padding-top:4px;">%s</div></td></tr></table>%s') % (
        link, SQ(PK['standard']), FF, INK, link, INK, price_line('standard', us, '70% OFF', 20), sbtn(label, link, True))
    return row('#FFFFFF', '0 20px 20px 20px', boxed(i, HAIR, PACK, '14px'), 'left', 'padx')
VS_ROWS = [('Pure titanium surface', 'A PTFE or ceramic coating'), ('No coating to wear off', 'Coating wears with use'), ('Metal utensils welcome', 'Wood or silicone advised'),
           ('Third-party tested by Light Labs', 'Testing varies by brand'), ('Dishwasher safe', 'Hand wash advised')]
def compare(bg=CREAM):
    r = '<tr><td width="50%%" bgcolor="%s" style="background-color:%s;padding:12px 12px;border-radius:10px 0 0 0;">%s</td><td width="50%%" bgcolor="#EFEAE1" style="background-color:#EFEAE1;padding:12px 12px;border-radius:0 10px 0 0;">%s</td></tr>' % (
        INK, INK, txt('Siraat Titanium', 14, 18, '#FFFFFF', 700), txt('Coated nonstick', 14, 18, '#6E6A64', 700))
    for i, (a, b) in enumerate(VS_ROWS):
        last = i == len(VS_ROWS) - 1; bb = '' if last else 'border-bottom:1px solid %s;' % HAIR
        r += '<tr><td valign="top" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:12px;%s%s">%s</td><td valign="top" bgcolor="#F9F7F3" style="background-color:#F9F7F3;padding:12px;%s%s">%s</td></tr>' % (
            bb, 'border-radius:0 0 0 10px;' if last else '', txt('<span style="color:%s;font-weight:800;">&#10003;</span>&nbsp; %s' % (GOLD, a), 15, 21, INK, 600), bb, 'border-radius:0 0 10px 0;' if last else '', txt(b, 15, 21, '#6E6A64', 400))
    t = serif('Your next pan vs a coated pan', 32, 36, INK, 'h1s', True, 'text-align:center;padding-bottom:16px;')
    t += '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid %s;border-radius:10px;border-collapse:separate;">%s</table>' % (HAIR, r)
    t += txt('Light Labs report no. 25895: 31 PFAS compounds tested, all below detection.', 12, 18, '#8A847A', 400, 'text-align:center;padding-top:12px;')
    return row(bg, '30px 20px 26px 20px', t, 'left', 'padx')
def stack_receipt(us):
    li = lambda a, b, strong=False: '<tr><td valign="top" style="padding:11px 0;border-bottom:1px dashed #D8D1C4;">%s</td><td align="right" width="40%%" valign="top" style="padding:11px 0 11px 10px;border-bottom:1px dashed #D8D1C4;">%s</td></tr>' % (
        txt(a, 15, 21, INK, 700 if strong else 500), txt(b, 15, 21, INK if strong else '#6E6A64', 700 if strong else 500, 'text-align:right;'))
    if us:
        rows_ = [('Titanium Hammered Pan Pro Standard', '<span style="text-decoration:line-through;color:#B5B5B5;">%s</span> %s' % (WAS('standard'), PRICE('standard'))),
                 ('Free shipping', '{{IF:US}}{{GIFTS:ship}} {{ENDIF}}included'), ('Plastic-Free Home e-book', '{{IF:US}}{{GIFTS:ebook}} {{ENDIF}}included'),
                 ('Mystery gift', '{{IF:US}}{{GIFTS:mystery}} {{ENDIF}}included'), ('Weekly chance to win {{GIFTS:filterline}}', 'entered with your order'),
                 ('75-year warranty', 'included'), ('30-day returns', 'included')]
        tot = li('Value', STACK_STD, True) + li('Your price', PRICE('standard'), True)
    else:
        rows_ = [('Titanium Hammered Pan Pro Standard', '70% off'), ('Free shipping, duties paid', 'included'), ('Plastic-Free Home e-book', 'included'), ('Mystery gift', 'included'),
                 ('Weekly chance to win a PFAS water filter', 'entered with your order'), ('75-year warranty', 'included'), ('30-day returns', 'included')]
        tot = ''
    t = eyebrow("What you get", INK, 'padding-bottom:6px;text-align:center;') + '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px dashed #D8D1C4;">%s%s</table>' % (''.join(li(a, b) for a, b in rows_), tot)
    return row('#FFFFFF', '8px 20px 22px 20px', boxed(t, '#E4DED3', '#FFFDF8', '18px 18px 8px 18px'), 'left', 'padx')
def promises():
    it = [('Changed your mind?', 'Send it back unused within 30 days of delivery for a full refund.'),
          ('Something wrong?', 'Damaged or defective in the first 30 days, we refund or replace it and pay the shipping. After that, the 75-year warranty takes over.')]
    i = serif('Two promises', 30, 34, INK, 'h1s', True, 'text-align:center;padding-bottom:14px;')
    for a, b in it:
        i += '<div style="height:10px;line-height:10px;font-size:0;">&nbsp;</div>' + boxed(txt(a, 16, 22, INK, 700) + txt(b, 15, 23, '#4A4A4A', 400, 'padding-top:4px;'), HAIR, '#FFFFFF', '16px 18px')
    return row(CREAM, '28px 20px 26px 20px', i, 'left', 'padx')
def hero_btn(label, url, us, bg='#FFFFFF', pad='16px 30px 26px 30px'): return button(label, url, bg, pad, sub=FRIC(us), fill=INK, fg='#FFFFFF')
def pbtn(label, url, us, pad='4px 30px 28px 30px', bg='#FFFFFF'): return button(label, url, bg, pad, sub=FRIC(us), fill=INK, fg='#FFFFFF')

files = {}
WHO5 = 'E30 (Homestead-segment, engaged 30 dagen), %s; smart sending aan'
WHO6 = 'E90 (Homestead-segment, engaged 90 dagen), %s, minus Pan Pro Standard-kopers (segment bestaat nog niet); smart sending aan'

for mkt in ('us', 'int'):
    US = mkt == 'us'; M = mkt.upper(); c5 = 'e5-1110-' + mkt; c6 = 'e6-1111-' + mkt
    WHEN5 = 'di 10 nov 2026, ochtend lokale tijd'; WHEN6 = 'wo 11 nov 2026, ochtend lokale tijd'
    who = 'US + geen land' if US else 'INT (land bekend, niet US)'
    SMALL = ('Offer valid November 1 to 30. Gifts while the sale runs; the water filter is a weekly draw.' if US else 'Offer valid 1 to 30 November. The water filter is a weekly draw.')
    lg, dp = utm(URL['large'], c5, 'recipe1'), utm(URL['deep'], c5, 'recipe2')
    # recepten (copy.md E5 A)
    SP = dict(k='large', title='Maple sweet potato rounds', meta_='Pan Pro Large &middot; 20 minutes &middot; make ahead up to 2 days',
              need=['2 large sweet potatoes', 'olive oil', '2 tablespoons maple syrup', 'flaky salt'],
              steps=['Slice the sweet potatoes into rounds about %s thick.' % ('3/8 inch (1 cm)' if US else '1 cm'),
                     'Heat the Pan Pro Large on medium for 2 to 3 minutes. Flick in a drop of water. When it balls up and glides, add a thin layer of olive oil.',
                     'Lay the rounds flat and leave them alone for 4 minutes. Cold metal grabs your food, hot metal lets it go.',
                     "Flip. Another 4 minutes, until they're golden on both sides and soft in the middle.", 'Drizzle with maple syrup. Salt. Done.'],
              ahead='into the fridge in a covered dish. On %s, 8 minutes in a low oven.' % ('Thursday' if US else 'the day'),
              note="One honest note: if a round sticks, the pan wasn't hot yet. Give the next rounds another minute.")
    GB = dict(k='deep', title='Green beans with shallots and almonds', meta_='Deep Pan Pro &middot; 10 minutes &middot; make ahead up to 2 days',
              need=['1 lb green beans' if US else '500 g green beans', '2 shallots', 'a knob of butter', 'half a lemon', 'a handful of toasted almond slivers'],
              steps=['Blanch the beans for 3 minutes in salted boiling water. Drain and leave them in the colander.',
                     'Slice the shallots and soften them in a little butter in the Deep Pan Pro over medium-low.', 'Beans back in. Toss.', 'Squeeze of lemon, almonds on top.'],
              ahead="fridge. On %s, back into the Deep Pan Pro on the lowest heat while everything else rests. They'll hold there for 30 minutes." % ('Thursday' if US else 'the day'),
              note='Why the Deep Pan: the higher sides mean you can toss a full batch without beans going over the edge.')

    # ================= E5 A · recept eerst, rijk opgemaakt =================
    subj = ('Make it Tuesday, serve it Thursday', "The Thanksgiving side that's better reheated") if US else ('Make it ahead, serve it hot', "The side dish that's better reheated")
    pre = 'Two sides, two pans, done before the big %s.' % ('day' if US else 'dinner')
    b = HEAD(meta4('e5-%s-a · Recept eerst, rijk opgemaakt' % mkt, M, 'Siraat', subj, pre, WHEN5, WHO5 % who, 'copy.md E5 A: twee receptkaarten, dan de BF-band. UX: beeld en knop in het eerste scherm.'), subj[0], pre) + OPEN3()
    b += hero('Weekly recipe', 'Make it Tuesday.<br>Serve it Thursday.' if US else 'Make it ahead.<br>Serve it hot.', 'Two sides that get better overnight.',
              IM_TABLE, 'A holiday table from above with sweet potatoes and green beans in two Siraat pans', utm(SALE, c5, 'a-hero'))
    b += hero_btn('Get my Black Friday price', utm(SALE, c5, 'a-cta1'), US)
    b += P('Benjamin here.', '#FFFFFF', '4px 40px 14px 40px')
    b += P(('Thanksgiving Thursday has one stove and five dishes that all want it at 4 pm. So I take two sides off the list early. Both get made the Tuesday before. Both reheat while the turkey rests. And the sweet potatoes, honestly, come out better the second day.') if US else
           ('A big dinner has one stove and five dishes that all want it at the same moment. So I take two sides off the list early. Both get made two days ahead. Both reheat while the main course rests. And the sweet potatoes, honestly, come out better the second day. (Cooking for Thanksgiving this month? These are the two I&#39;d make.)'),
           '#FFFFFF', '0 40px 10px 40px')
    b += row('#FFFFFF', '4px 20px 18px 20px', img(IM_SWEET, 'Maple sweet potato rounds in a Siraat Pan Pro', lg, 560, 10), 'center', 'padx')
    b += recipe(link=lg, **SP) + pbtn('Shop the Pan Pro Large', lg, US, '18px 30px 26px 30px')
    b += row('#FFFFFF', '4px 20px 18px 20px', img(IM_BEANS, 'Green beans with shallots and almonds in a Siraat Deep Pan Pro', dp, 560, 10), 'center', 'padx')
    b += recipe(link=dp, **GB) + pbtn('Shop the Deep Pan Pro', dp, US, '18px 30px 26px 30px')
    b += diamonds([('A pure titanium cooking surface, no coatings.', ''), ('Tested free from PFAS by Light Labs, report no. 25895.', ''), ('Dishwasher safe. Thursday night, that matters.' if US else 'Dishwasher safe. On the day, that matters.', '')],
                  '#FFFFFF', 'Why these two pans', pad='4px 20px 24px 20px')
    b += revblock(['R562', 'R518'])
    b += bfband_full(US, c5, 'a')
    b += closing('Happy cooking,', '#FFFFFF').replace('6px 40px 4px 40px', '30px 40px 4px 40px') + sign()
    if US:
        b += ps('The Black Friday sale is live: up to 70% off and 4 gifts with every order. Doing the whole kitchen? The 12-piece set comes with a free Titanium Hammered Pizza Steel. Just arrived and selling fast. Ends Monday, November 30.')
        b += pbtn('Shop the 12-piece set', utm(URL['set12'], c5, 'a-ps'), US, '4px 30px 18px 30px')
    else:
        b += ps('The Black Friday sale is live: up to 70% off and 4 gifts with every order. Doing the whole kitchen? The 6-piece set gives you three pans and three lids. Just arrived and selling fast. Ends Monday 30 November.')
        b += pbtn('Shop the 6-piece set', utm(URL['set6'], c5, 'a-ps'), US, '4px 30px 18px 30px')
    files['e5-%s-a' % mkt] = b + small(SMALL) + TAIL

    # ================= E5 B · prep plan =================
    subj = ('Your Thanksgiving, in 3 days and 2 pans', 'What can you cook before Thursday?') if US else ('A big dinner, in 3 days and 2 pans', 'What can you cook two days early?')
    pre = 'Tuesday, Wednesday, Thursday. The plan that frees up your stove.' if US else 'Day one, day two, the big day. The plan that frees up your stove.'
    b = HEAD(meta4('e5-%s-b · Prep plan in drie dagen' % mkt, M, 'Siraat', subj, pre, WHEN5, WHO5 % who, 'copy.md E5 B: draaiboek met drie dagkaarten en twee productkaarten.'), subj[0], pre) + OPEN3()
    b += hero('Thanksgiving prep plan' if US else 'Big dinner prep plan', 'Three days.<br>Two pans.', 'One free stove on Thursday.' if US else 'One free stove on the day.',
              IM_SWEET, 'Golden maple sweet potato rounds in a Siraat Pan Pro', utm(SALE, c5, 'b-hero'))
    b += hero_btn('Get my Black Friday price', utm(SALE, c5, 'b-cta1'), US)
    b += P('Benjamin here.', '#FFFFFF', '4px 40px 14px 40px')
    b += P(("Here's the problem with Thanksgiving: everything wants the stove at the same time. Here's my fix: two sides get done before Thursday, in two pans, and on the day they only need warming up.") if US else
           ("Here's the problem with a big dinner: everything wants the stove at the same time. Here's my fix: two sides get done in the two days before, in two pans, and on the day they only need warming up. (Thanksgiving, a birthday, the whole family on a Sunday. Same plan.)"),
           '#FFFFFF', '0 40px 18px 40px')
    d1, d2, d3 = ('TUESDAY', 'WEDNESDAY', 'THURSDAY') if US else ('DAY ONE', 'DAY TWO', 'THE BIG DAY')
    b += daycard(d1, 'Maple sweet potato rounds', 'Pan Pro Large, 20 minutes',
                 'Slice 2 large sweet potatoes into %s rounds. Heat the Pan Pro Large on medium for 2 to 3 minutes, until a drop of water balls up and glides, then add a thin layer of olive oil. Lay the rounds flat. Don&#39;t move them for 4 minutes. Flip, 4 more. Maple syrup, salt. Into the fridge.' % ('3/8 inch (1 cm)' if US else '1 cm'))
    b += daycard(d2, 'Green beans with shallots and almonds', 'Deep Pan Pro, 10 minutes',
                 'Blanch the beans 3 minutes, drain. Soften 2 sliced shallots in butter in the Deep Pan Pro. Beans back in, a squeeze of lemon, toasted almond slivers. Into the fridge. Both pans go in the dishwasher. That&#39;s %s.' % ('Wednesday' if US else 'day two'))
    b += daycard(d3, 'The warm-up', '', '', ['30 minutes before dinner: green beans into the Deep Pan Pro, lowest heat. They hold there.', '10 minutes before: sweet potatoes into a low oven for 8 minutes.',
                                            ('Turkey' if US else 'Main course') + ' out to rest. Your sides are already hot.'])
    b += P('Why it works in these pans: the cooking surface is pure titanium with no coatings, so the only trick is heat. Cold metal grabs your food, hot metal lets it go. Tested free from PFAS by Light Labs, report no. 25895.', '#FFFFFF', '12px 40px 20px 40px')
    b += gap('#FFFFFF', 6)
    b += wide_card('large', 'Room for a whole batch of rounds.', US, '70% OFF', 'Shop the Pan Pro Large', utm(URL['large'], c5, 'b-card-large'))
    b += wide_card('deep', 'Higher sides for sauces, pasta and one-pan dinners.', US, 'UP TO 70% OFF', 'Shop the Deep Pan Pro', utm(URL['deep'], c5, 'b-card-deep'))
    b += row('#FFFFFF', '2px 30px 24px 30px', txt(FRIC(US), 13, 19, GREY, 500, 'text-align:center;'), 'center')
    b += revblock(['R562', 'R518'])
    b += bfband_full(US, c5, 'b')
    b += closing('Have a good Thanksgiving,' if US else 'Happy cooking,').replace('6px 40px 4px 40px', '30px 40px 4px 40px') + sign()
    if US:
        b += ps('Cooking for a crowd every year? The 12-piece set is the whole kitchen in one box, and right now it comes with a free Titanium Hammered Pizza Steel. Just arrived and selling fast. The sale ends Monday, November 30.')
        b += pbtn('Shop the 12-piece set', utm(URL['set12'], c5, 'b-ps'), US, '4px 30px 18px 30px')
    else:
        b += ps('Cooking for a crowd every year? The 6-piece set gives you three pans and a lid for each. Just arrived and selling fast. The sale ends Monday 30 November.')
        b += pbtn('Shop the 6-piece set', utm(URL['set6'], c5, 'b-ps'), US, '4px 30px 18px 30px')
    files['e5-%s-b' % mkt] = b + small(SMALL) + TAIL

    # ================= E5 C · kort, één recept, sterke BF-sectie =================
    subj = ('10-minute green beans, made Tuesday', 'A Thanksgiving side + up to 70% off') if US else ('10-minute green beans, made ahead', 'A make-ahead side + up to 70% off')
    pre = 'One side dish, one pan, and the Black Friday prices.'
    b = HEAD(meta4('e5-%s-c · Kort: één recept, sterke BF-sectie' % mkt, M, 'Siraat', subj, pre, WHEN5, WHO5 % who, 'copy.md E5 C: snelste recept als haak, daarna vier producten en de gifts.'), subj[0], pre) + OPEN3()
    b += hero('Weekly recipe', 'Ten minutes.<br>Made Tuesday.' if US else 'Ten minutes.<br>Made ahead.', 'Reheats while the turkey rests.' if US else 'Reheats while dinner rests.',
              IM_BEANS, 'Green beans with shallots and almonds in a Siraat Deep Pan Pro', utm(URL['deep'], c5, 'c-hero'))
    b += hero_btn('Get my Black Friday price', utm(SALE, c5, 'c-cta1'), US, pad='16px 30px 22px 30px')
    b += offerbar('UP TO 70%% OFF &nbsp;&middot;&nbsp; %s' % ('{{GIFTS:TOTAL}}' if US else '4 GIFTS WITH EVERY ORDER')) + gap('#FFFFFF', 22)
    b += P('Benjamin here. One side dish this week, because %s is busy enough.' % ('Thanksgiving' if US else 'a big dinner'), '#FFFFFF', '4px 40px 16px 40px')
    i = serif('Green beans with shallots and almonds', 28, 31, INK, 'ptitle', True) + txt('Deep Pan Pro &middot; 10 minutes', 14, 20, GREY, 500, 'padding:4px 0 14px 0;')
    i += numbered(['Blanch %s green beans for 3 minutes. Drain.' % ('1 lb' if US else '500 g'), 'Soften 2 sliced shallots in a little butter in the Deep Pan Pro.',
                   'Beans back in, a squeeze of lemon, a handful of toasted almond slivers.',
                   ('Fridge. On Thursday, lowest heat in the same pan while the turkey rests. It holds for 30 minutes.') if US else ('Fridge. On the day, lowest heat in the same pan while everything else rests. It holds for 30 minutes.')])
    i += txt('Pure titanium cooking surface, no coatings, straight into the dishwasher after.', 15, 23, '#4A4A4A', 400, 'padding-top:4px;')
    b += row('#FFFFFF', '0 20px 0 20px', boxed(i, HAIR, '#FFFFFF', '20px 18px 16px 18px'), 'left', 'padx')
    b += pbtn('Shop the Deep Pan Pro', utm(URL['deep'], c5, 'c-recipe'), US, '18px 30px 28px 30px')
    b += heading("This week's Black Friday prices", CREAM, '30px 24px 18px 24px')
    if US:
        cards = [gcard('deep', 'Higher sides for sauces, pasta and one-pan dinners.', US, '', 'Shop the pan', utm(URL['deep'], c5, 'c-grid-deep')),
                 gcard('large', 'Room for the whole family.', US, '', 'Shop the pan', utm(URL['large'], c5, 'c-grid-large')),
                 gcard('set6', 'Mini, Small and Large, each with its own lid.', US, '', 'Shop the set', utm(URL['set6'], c5, 'c-grid-set6'), 'Just arrived'),
                 gcard('set12', 'The whole kitchen. Plus a free Pizza Steel.', US, '', 'Shop the set', utm(URL['set12'], c5, 'c-grid-set12'), 'Just arrived')]
        under = "The sets just arrived and they're selling fast."
    else:
        cards = [gcard('deep', 'Higher sides for sauces, pasta and one-pan dinners.', US, 'UP TO 70% OFF', 'Shop the pan', utm(URL['deep'], c5, 'c-grid-deep')),
                 gcard('large', 'Room for the whole family.', US, '70% OFF', 'Shop the pan', utm(URL['large'], c5, 'c-grid-large')),
                 gcard('standard', 'The size most kitchens start with.', US, '70% OFF', 'Shop the pan', utm(URL['standard'], c5, 'c-grid-standard')),
                 gcard('set6', 'Mini, Small and Large, each with its own lid.', US, 'UP TO 70% OFF', 'Shop the set', utm(URL['set6'], c5, 'c-grid-set6'), 'Just arrived')]
        under = "The 6-piece set just arrived and it's selling fast."
    b += grid(cards) + row(CREAM, '4px 30px 26px 30px', txt(under, 14, 20, INK, 600, 'text-align:center;'), 'center')
    b += gifts_tiles(US)
    b += revblock(['R562'] if US else ['R399'], CREAM, 'From their kitchens', '26px 20px 26px 20px')
    b += pbtn('Get my Black Friday price', utm(SALE, c5, 'c-cta-end'), US, '28px 30px 0 30px')
    b += row('#FFFFFF', '10px 30px 20px 30px', txt('Up to 70% off. Ends Monday, November 30.' if US else 'Up to 70% off. Ends Monday 30 November.', 14, 20, INK, 600, 'text-align:center;'), 'center')
    b += sign()
    files['e5-%s-c' % mkt] = b + small(SMALL) + TAIL

    # ================= E6 A · founder-brief =================
    subj = ('December 20, 2024', 'Why this pan came first'); pre = "The original hammered titanium pan, and why it's 70% off this week."
    b = HEAD(meta4('e6-%s-a · Founder-brief, persoonlijk' % mkt, M, 'Benjamin from Siraat', subj, pre, WHEN6, WHO6 % who, 'copy.md E6 A: waarom Benjamin deze pan maakte. UX: compacte productkaart en knop binnen het eerste scherm.'), subj[0], pre) + OPEN3()
    top = '34px 40px 16px 40px'
    if US: b += P('First, for Veterans Day: thank you to everyone who serves and has served.', '#FFFFFF', top); top = '0 40px 16px 40px'
    if US: b += row('#FFFFFF', '0 20px 20px 20px', img(IM_VET, 'A folded American flag on a kitchen shelf above a Siraat pan on the stove', None, 560, 10), 'center', 'padx')
    b += P('Benjamin here. I want to tell you how the Pan Pro Standard happened.', '#FFFFFF', top)
    b += mini_offer(US, c6, 'a-card')
    b += P("Siraat didn't start with pans. We started with titanium cutting boards. And the question that came after was obvious: could you cook on titanium too, with nothing coated on top of it?")
    b += P('The Pan Pro was the answer. A pure titanium cooking surface, a hammered pattern, no coatings of any kind. We shipped the first orders on %s. Since then, more than 100,000 people have bought from us, in a little over a year. Others started hammering titanium after that. This was the first one.' % ('December 20, 2024' if US else '20 December 2024'))
    b += row('#FFFFFF', '4px 20px 22px 20px', img(IM_EGG, 'An egg sliding out of a Siraat Pan Pro Standard onto toast', utm(URL['standard'], c6, 'a-img'), 560, 10), 'center', 'padx')
    b += P("Here's what I like most about it. There's no coating on it, so there's nothing to wear thin and nothing to peel. It goes in the dishwasher. Metal spatulas are fine. And we had it tested: Light Labs, an ISO/IEC 17025-accredited lab, checked it for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895, and you can read it yourself.")
    b += P('The one thing it asks of you is heat. Medium for 2 to 3 minutes, until a drop of water balls up and glides, then a teaspoon of oil. Cold metal grabs your food, hot metal lets it go.')
    if US: b += P('This week the Pan Pro Standard is <b>%s</b>, down from %s. That&#39;s 70%% off, and every order comes with 4 gifts: free shipping, the Plastic-Free Home e-book, a mystery gift, and a weekly chance to win {{GIFTS:filterline}}.' % (PRICE('standard'), WAS('standard')))
    else: b += P('This week the Pan Pro Standard is <b>70% off</b>, and every order comes with 4 gifts: free shipping with duties paid, the Plastic-Free Home e-book, a mystery gift, and a weekly chance to win a PFAS water filter.')
    b += pbtn('Get my Pan Pro at 70% off', utm(URL['standard'], c6, 'a-cta1'), US, '6px 30px 28px 30px')
    b += P('Two people who said it better than I can:')
    for k in (['R411', 'R138'] if US else ['R138', 'R399']): b += quote(k)
    b += P("And it's covered for 75 years.") + sign()
    b += ps('30-day returns, counted from the day the box arrives. The sale ends %s.' % ('Monday, November 30' if US else 'Monday 30 November'))
    files['e6-%s-a' % mkt] = b + small(SMALL) + TAIL

    # ================= E6 B · the last pan =================
    subj = ('"The last pans we ever have to purchase"', 'How many pans have you thrown out?'); pre = 'Why a coated pan has an end date, and this one has a 75-year warranty.'
    b = HEAD(meta4('e6-%s-b · The last pan: coating tegen puur titanium' % mkt, M, 'Benjamin from Siraat', subj, pre, WHEN6, WHO6 % who, 'copy.md E6 B: coating heeft een einddatum, garantie en klantcitaat als bewijs.'), subj[0], pre) + OPEN3()
    b += hero("Benjamin's note", 'A pan with<br>no end date.', 'Covered for 75 years.', PK['standard'], 'The Siraat Titanium Hammered Pan Pro Standard', utm(URL['standard'], c6, 'b-hero'))
    b += hero_btn('Get my Pan Pro at 70% off', utm(URL['standard'], c6, 'b-cta1'), US, pad='16px 30px 22px 30px')
    b += offerbar('70%% OFF &nbsp;&middot;&nbsp; %s' % ('{{GIFTS:TOTAL}}' if US else '4 GIFTS WITH EVERY ORDER')) + gap('#FFFFFF', 22)
    top = '4px 40px 16px 40px'
    if US: b += P('First, for Veterans Day: thank you to everyone who serves and has served.', '#FFFFFF', top); top = '0 40px 16px 40px'
    if US: b += row('#FFFFFF', '0 20px 20px 20px', img(IM_VET, 'A folded American flag on a kitchen shelf above a Siraat pan on the stove', None, 560, 10), 'center', 'padx')
    b += P('Benjamin here. A quick question before the sale stuff: how many frying pans have you thrown out?', '#FFFFFF', top)
    b += P("Most people I talk to can count a few. Not because they cooked wrong. Because a coated pan wears with use, and once the coating starts to go, the pan is done. That's the deal with coatings. They come with an end date nobody prints on the box.")
    b += P("The Pan Pro Standard doesn't have that problem, because there's nothing on it to lose. The cooking surface is pure titanium, with no coatings of any kind. No coating means nothing to wear thin, nothing to peel, nothing to baby. Metal spatula, dishwasher, %s, all fine." % ('Tuesday night' if US else 'a busy weeknight'))
    b += pbtn('Get my Pan Pro at 70% off', utm(URL['standard'], c6, 'b-cta2'), US, '6px 30px 28px 30px')
    b += compare()
    b += P("I'm not going to tell you how many years it lasts. I'll tell you what we put in writing instead: a 75-year warranty. If it dents, if the base warps, if a handle or rivet comes loose, or if the lid stops fitting, we take care of it.", '#FFFFFF', '28px 40px 18px 40px')
    b += P('One customer sent us a photo and that was it:') + quote('R240')
    b += P("And another said the thing I'd never write myself:") + quote('R583')
    i = eyebrow('Black Friday', INK, 'text-align:center;') + serif('Pan Pro Standard', 34, 38, INK, 'h1b', True, 'text-align:center;padding-top:6px;')
    if US:
        i += ('<table role="presentation" align="center" style="margin:10px auto 0 auto;" cellpadding="0" cellspacing="0" border="0"><tr><td valign="middle" style="padding-right:10px;font-family:%s;font-size:18px;font-weight:600;color:#B5B5B5;text-decoration:line-through;white-space:nowrap;">%s</td>'
              '<td valign="middle" class="now" style="padding-right:10px;font-family:%s;font-size:44px;line-height:48px;font-weight:600;color:%s;white-space:nowrap;">%s</td><td valign="middle">%s</td></tr></table>') % (FF, WAS('standard'), FF, INK, PRICE('standard'), badge('70% OFF', 12))
        i += txt('You save %s' % SAVE_STD, 15, 22, INK, 700, 'text-align:center;padding-top:6px;')
        i += txt('Plus 4 gifts with every order: free shipping, the Plastic-Free Home e-book, a mystery gift, and a weekly chance to win {{GIFTS:filterline}}.', 15, 23, '#4A4A4A', 400, 'text-align:center;padding-top:10px;')
    else:
        i += '<div style="text-align:center;padding-top:10px;">%s</div>' % badge('70% OFF', 14)
        i += txt('Plus 4 gifts with every order: free shipping with duties paid, the Plastic-Free Home e-book, a mystery gift, and a weekly chance to win a PFAS water filter.', 15, 23, '#4A4A4A', 400, 'text-align:center;padding-top:10px;')
    i += txt('Tested free from PFAS by Light Labs, report no. 25895.', 13, 19, '#8A847A', 500, 'text-align:center;padding-top:8px;')
    b += row('#FFFFFF', '10px 20px 0 20px', boxed(img(C43(PK['standard']), 'The Siraat Titanium Hammered Pan Pro Standard', utm(URL['standard'], c6, 'b-offer-img'), 520, 8) + '<div style="height:14px;line-height:14px;font-size:0;">&nbsp;</div>' + i, INK, PACK, '16px 16px 20px 16px'), 'left', 'padx')
    b += pbtn('Get my Pan Pro at 70% off', utm(URL['standard'], c6, 'b-cta3'), US, '20px 30px 26px 30px')
    b += sign()
    b += ps('Changed your mind after it arrives? Unused, within 30 days of delivery, you get a full refund. The sale ends %s.' % ('Monday, November 30' if US else 'Monday 30 November'))
    files['e6-%s-b' % mkt] = b + small(SMALL) + TAIL

    # ================= E6 C · kort en hard met waardestapel =================
    subj = ('The original pan, 70% off', '1 pan, 4 gifts, 75-year warranty')
    pre = '$144 for the Pan Pro Standard. Ends November 30.' if US else '70% off the Pan Pro Standard, plus 4 gifts. Ends 30 November.'
    b = HEAD(meta4('e6-%s-c · Kort en hard, waardestapel' % mkt, M, 'Benjamin from Siraat', subj, pre, WHEN6, WHO6 % who, 'copy.md E6 C: most aware, aanbod voorop, waardestapel als bonnetje.'), subj[0], pre) + OPEN3()
    b += hero('Black Friday', 'The original pan.<br>70% off.', 'Plus 4 gifts. Ends Nov 30.' if US else 'Plus 4 gifts. Ends 30 Nov.', PK['standard'], 'The Siraat Titanium Hammered Pan Pro Standard', utm(URL['standard'], c6, 'c-hero'))
    if US: b += pricebar('standard', US, pad='16px 20px 0 20px')
    b += hero_btn('Get my Pan Pro at 70% off', utm(URL['standard'], c6, 'c-cta1'), US, pad='14px 30px 22px 30px')
    b += offerbar('70% OFF &nbsp;&middot;&nbsp; 4 GIFTS WITH EVERY ORDER') + gap('#FFFFFF', 22)
    top = '4px 40px 16px 40px'
    if US: b += P('First, for Veterans Day: thank you to everyone who serves and has served.', '#FFFFFF', top); top = '0 40px 16px 40px'
    if US: b += row('#FFFFFF', '0 20px 20px 20px', img(IM_VET, 'A folded American flag on a kitchen shelf above a Siraat pan on the stove', None, 560, 10), 'center', 'padx')
    b += P('Benjamin here. Short one today.', '#FFFFFF', top)
    if US:
        b += P('The Pan Pro Standard is the original hammered titanium pan. Pure titanium cooking surface, no coatings. Right now it&#39;s %s instead of %s. That&#39;s 70%% off.' % (PRICE('standard'), WAS('standard')))
        b += P("If it's been on your list for a while, this is the week.")
    else:
        b += P('The Pan Pro Standard is the original hammered titanium pan. Pure titanium cooking surface, no coatings. Right now it&#39;s 70% off.')
        b += P("If you've had it in your cart for a while, this is the week.")
    b += stack_receipt(US)
    b += diamonds([('A pure titanium cooking surface, no coatings', ''), ('Tested free from PFAS by Light Labs, report no. 25895', ''), ('Covered for 75 years', '')], '#FFFFFF', '', pad='0 20px 24px 20px')
    b += revblock(['R169', 'R011'])
    b += promises()
    b += pbtn('Get my Pan Pro at 70% off', utm(URL['standard'], c6, 'c-cta-end'), US, '28px 30px 0 30px')
    b += row('#FFFFFF', '10px 30px 18px 30px', txt('The sale ends %s.' % ('Monday, November 30' if US else 'Monday 30 November'), 14, 20, INK, 600, 'text-align:center;'), 'center')
    b += sign()
    files['e6-%s-c' % mkt] = b + small(SMALL) + TAIL

BAD = ('next batch', 'reserve', 'arriving', 'next shipment', 'purifier', 'lifetime', 'for life', 'free filter', 'scratch-proof', 'while supplies last', 'VRAAG FLORIS')
for k, v in files.items():
    assert '—' not in v and '–' not in v, k
    body = v.split('-->', 1)[1]
    low = re.sub(r'<[^>]+>', ' ', body).lower()
    for bad in BAD: assert bad.lower() not in low, (k, bad)
    if '-int-' in k:
        assert '$' not in body and not re.search(r'\{\{(PRICE|WAS|FROM|GIFTS|FRICTION)', body), k
        assert 'Veterans' not in body and 'inch' not in body and ' lb ' not in body, k
    else:
        assert 'Benjamin' in body
    open(os.path.join(N, k + '.html'), 'w').write(v); print('geschreven', k, len(v))
print('SAVE:standard', SAVE_STD, '| STACK:standard', STACK_STD)
