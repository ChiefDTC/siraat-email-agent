"""Win Your Order Back, wo 4 nov 2026 (Floris 4 nov): vandaag wordt één willekeurige order volledig terugbetaald (staat ook op de PDP:
"REFUNDING 1 RANDOM ORDER TODAY · Today only"). Mail focust op die actie, toont de hele BF-collectie (set is één van de producten).
Stijl: eigen stijl (Roasting Pan-mail / prijslijst ronde 2). US met prijzen, INT zonder bedragen. Concept, niets live.
Gebruik (vanuit /tmp): python3 -I make_win.py, daarna render_win.py en shot_win.js."""
import os, re
S = '/home/user/siraat-email-agent/klaviyo/templates/v3/campaigns/pricelist-1104/_tools/make_pl2.py'
src = open(S).read().split('\nfiles = {}\n')[0]
g = {'__file__': S, '__name__': 'pl2helpers'}; exec(compile(src, S, 'exec'), g); globals().update({k: v for k, v in g.items() if not k.startswith('__')})
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P_['set12'] = ('Cookware Set, 12&nbsp;Pcs', '12pcsset.webp', SET12, 'The whole kitchen + a free Pizza Steel.')
SALE = 'https://siraatskitchen.com/collections/black-friday-sale'
G2 = card.__globals__; _ml = G2['money_line']
def money_line(k, us):  # 12-Pcs is 68%, niet 70%
    h = _ml(k, us)
    return h.replace('>70% OFF<', '>68% OFF<') if k == 'set12' else h
G2['money_line'] = money_line
US_KEYS = ['set12', 'crepe', 'roast', 'wok', 'deep', 'standard']
INT_KEYS = ['set6', 'crepe', 'roast', 'wok', 'deep', 'standard']
SMALL = 'One order placed today, Wednesday, November 4, is picked at random and refunded in full. Your sale price and free gifts still apply.'
def steps(bg='#FFFFFF', pad='0 20px 24px 20px'):
    it = [('1', 'Order anything today', 'Any pan, any set. Everything is already up to 70% off for VIP Black Friday.'),
          ('2', 'We pick one order at random', 'From every order placed today.'),
          ('3', 'That order is refunded in full', 'You keep everything. We pay it all back.')]
    r = ''.join('<tr><td width="46" valign="top" style="padding:0 0 16px 0;"><div style="width:34px;height:34px;border-radius:17px;background-color:%s;font-family:%s;font-size:16px;line-height:34px;font-weight:800;color:%s;text-align:center;">%s</div></td><td valign="top" style="padding:4px 0 16px 0;">%s%s</td></tr>' % (
        Y, FF, INK, n, txt(t, 17, 22, INK, 600), txt(d, 15, 22, '#4A4A4A', 400, 'padding-top:3px;')) for n, t, d in it)
    t = txt('HOW IT WORKS', 13, 18, INK, 600, 'letter-spacing:1.2px;padding-bottom:16px;') + '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % r
    card = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid %s;border-radius:10px;"><tr><td style="padding:20px 20px 6px 20px;">%s</td></tr></table>' % (INK, t)
    return row(bg, pad, card, 'left', 'padx')
def refund_block(sub):
    h = txt('TODAY ONLY', 13, 16, Y, 700, 'letter-spacing:2.4px;text-align:center;padding-bottom:10px;')
    h += '<div class="big2" style="font-family:%s;font-size:70px;line-height:70px;font-weight:900;letter-spacing:-3px;color:%s;text-align:center;">1 ORDER<br>ON US</div>' % (FF, Y)
    h += txt(sub, 16, 24, '#E6E3DC', 500, 'text-align:center;padding-top:14px;')
    return row(INK, '28px 20px 30px 20px', h, 'center', 'padx')
def hero(camp, ct, sub):
    h = row(PACK, '30px 24px 0 24px', pills2('VIP Black Friday', 'Today only'), 'center')
    h += row(PACK, '18px 24px 0 24px', serif('Win your<br>order back', 58, 60, INK, 'h1', True), 'center')
    h += row(PACK, '14px 36px 26px 36px', txt(sub, 17, 26, '#4A4A4A', 400, 'text-align:center;'), 'center')
    return h
def small(bg='#FFFFFF'):
    return row(bg, '0 30px 26px 30px', txt(SMALL, 12, 18, '#8A847A', 400, 'text-align:center;'), 'center')
def meta3(id_, mkt, sender, subj, pre, why):
    who = ('Engaged 90D US v2 (VMjhb2) + No Country 90D (R5rFrC)' if mkt == 'US' else 'Engaged 90D INT v2 (XrFa5r)') + '; excl. kopers vandaag; smart sending aan'
    return 'ID: %s\nMARKT: %s\nSENDER: %s\nSUBJECT A: %s\nSUBJECT B: %s\nPREVIEW: %s\nWANNEER: wo 4 nov 2026, zo vroeg mogelijk (actie geldt alleen vandaag)\nWIE: %s\nWAAROM: %s' % (id_, mkt, sender, subj[0], subj[1], pre, who, why)
files = {}
HERO = 'https://cdn.klaviyomail.com/company/TdtTzz/images/1ff5f3b8-908c-4343-be27-05dff0aa6c2f.jpeg'  # hero-1 (Higgsfield, Floris koos 4 nov)
SUBJ = ('Win your order back (today only)', "We're refunding one order today")
PRE = 'Order anything today and it could be on us. Everything is already up to 70% off.'

for mkt in ('us', 'int'):
    US = mkt == 'us'; c = 'win-1104-' + mkt; keys = US_KEYS if US else INT_KEYS
    # ---------- A: actie voorop, dan hele collectie ----------
    m = meta3('wb-%s-a · Actie voorop + hele collectie' % mkt, mkt.upper(), 'Siraat', SUBJ, PRE, 'Floris 4 nov: offer is Win Your Order Back, collectie breed tonen, set niet de hoofdzaak.')
    b = head(m, SUBJ[0], PRE) + OPEN2()
    b += hero(c, 'a', 'Order anything today, and one random order gets refunded in full. That could be yours.')
    b += refund_block('Everything is already up to 70% off. One order placed today gets refunded in full.')
    b += button('Win your order back', u(SALE, c, 'a-cta1'), '#FFFFFF', '26px 30px 26px 30px', fill=Y, fg=INK)
    b += steps()
    b += row(CREAM, '30px 24px 6px 24px', serif('Our VIP Black Friday picks', 34, 38, INK, 'h1b', True) + txt('Pick anything. Every order today is in the draw.', 15, 22, GREY, 500, 'padding-top:8px;'), 'center')
    b += gap(CREAM, 14) + grid4(keys, US, c, 'a', CREAM) + gap(CREAM, 12)
    b += gap('#FFFFFF', 24) + trust()
    b += button('Shop VIP Black Friday', u(SALE, c, 'a-cta-end'), '#FFFFFF', '4px 30px 20px 30px', fill=Y, fg=INK) + small()
    files['wb-%s-a' % mkt] = b + TAIL

    # ---------- B: brief van Benjamin ----------
    m = meta3('wb-%s-b-letter · Brief van Benjamin' % mkt, mkt.upper(), 'Benjamin from Siraat', ("Today, one of you gets their order for free", 'Win your order back (today only)'),
              'Benjamin here. One order placed today is on us.', 'Founder-brief: klikt het best bij betrokken lezers. Zelfde actie, persoonlijk.')
    b = head(m, 'Today, one of you gets their order for free', 'Benjamin here. One order placed today is on us.') + OPEN2()
    b += P("Hi {{ first_name|default:'there' }},", '#FFFFFF', '34px 40px 14px 40px')
    b += P('Benjamin here. Something different today.')
    b += P('<b>One order placed today gets refunded in full.</b> We pick it at random from every order that comes in today, and we pay the whole thing back. You keep the pans.')
    b += P('And everything is already up to 70% off for VIP Black Friday, so whatever you pick is a good deal before the draw even happens.')
    b += button('Win your order back', u(SALE, c, 'b-cta1'), '#FFFFFF', '6px 40px 26px 40px', fill=Y, fg=INK)
    b += row('#FFFFFF', '0 20px 8px 20px', txt('A few of the pans people are ordering today:', 15, 22, GREY, 500, 'text-align:center;'), 'center')
    rows_ = ''.join(listrow(k, US, c, 'b', i == 3) for i, k in enumerate(keys[:4]))
    b += row('#FFFFFF', '0 20px 10px 20px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % rows_, 'left', 'padx')
    b += P('Good luck. And if it is not you this time, you still have pans that will outlast all of us.', '#FFFFFF', '10px 40px 12px 40px') + sign()
    b += small()
    files['wb-%s-b-letter' % mkt] = b + TAIL

    # ---------- C: korte, harde beeldmail ----------
    m = meta3('wb-%s-c · Kort en hard' % mkt, mkt.upper(), 'Siraat', ('1 order. Refunded. Today.', 'Win your order back (today only)'), PRE, 'Smooche-stijl: één boodschap, één knop, producten eronder.')
    b = head(m, '1 order. Refunded. Today.', PRE) + OPEN2(INK)
    b += refund_block('Order anything today and it could be on us. One random order gets refunded in full.')
    b += button('Win your order back', u(SALE, c, 'c-cta1'), INK, '0 30px 30px 30px', fill=Y, fg=INK, sub='Everything up to 70% off &middot; Free shipping &middot; 100,000+ customers', dark=True)
    b += row(INK, '0 20px 26px 20px', img(HERO, 'A hammered titanium pan in an open black gift box with a yellow ribbon', u(SALE, c, 'c-hero'), 560, 10), 'center', 'padx')
    b += bfband('VIP BLACK FRIDAY &nbsp;&middot;&nbsp; TODAY ONLY')
    b += gap(CREAM, 20) + grid4(keys, US, c, 'c', CREAM) + gap(CREAM, 12)
    b += button('Shop VIP Black Friday', u(SALE, c, 'c-cta-end'), '#FFFFFF', '24px 30px 20px 30px', fill=Y, fg=INK) + small()
    files['wb-%s-c' % mkt] = b + TAIL

for k, v in files.items():
    assert '—' not in v, k
    body = v.split('-->', 1)[1]
    for bad in ('next batch', 'reserve', 'arriving', 'Ends Monday', 'guaranteed'):
        assert bad not in body, (k, bad)
    if '-int-' in k: assert '$' not in body and not re.search(r'\{\{(PRICE|WAS|GIFTS)', body), k
    open(os.path.join(N, k + '.html'), 'w').write(v); print('geschreven', k, len(v))
