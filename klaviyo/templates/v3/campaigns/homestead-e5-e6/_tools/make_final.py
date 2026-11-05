"""E5 en E6 definitief (Floris 5 nov): per mail één versie (E5 = prep-plan, E6 = brief van Benjamin), US en INT,
zonder prijzen (ook US alleen 70% OFF), korter. Hergebruikt helpers en dagkaarten uit make_e56.py. Concept, niets live.
Gebruik (vanuit /tmp): python3 -I make_final.py, daarna render_e56.py <out> e5-us-final,e5-int-final,e6-us-final,e6-int-final."""
import os, re
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_e56.py')
E56SRC = open(SRC).read()
helpers = E56SRC.split('\nfor mkt in (')[0]
HG0 = {'__file__': SRC, '__name__': 'e56helpers'}; exec(compile(helpers, SRC, 'exec'), HG0)
globals().update({k: v for k, v in HG0.items() if not k.startswith('__')})
HG = wide_card.__globals__
# geen prijzen: prijsregels tonen alleen het percentage-label, ook in US
_pl, _pb = price_line, pricebar
HG['price_line'] = lambda k, us, int_label='70% OFF', big=20: _pl(k, False, int_label, big)
HG['pricebar'] = lambda k, us, int_label='70% OFF', bg='#FFFFFF', pad='22px 20px 0 20px': _pb(k, False, int_label, bg, pad)
HG['gv'] = lambda k: ''
E56LINES = E56SRC.split('\n')
def grab(start, stop):
    i = next(n for n, l in enumerate(E56LINES) if l.strip().startswith(start))
    j = next(n for n in range(i, len(E56LINES)) if E56LINES[n].strip().startswith(stop))
    return '\n'.join(l[4:] for l in E56LINES[i:j])
DAYS = grab('d1, d2, d3 =', "b += P('Why it works")
def bf_short(us, camp, ct):
    h = txt('VIP BLACK FRIDAY', 13, 16, '#D9C9A8', 700, 'letter-spacing:2.4px;text-align:center;padding-bottom:12px;')
    h += serif('Up to 70% off, plus 4 gifts<br>with every order.', 34, 38, '#FFFFFF', 'h1b', True, 'text-align:center;')
    h += txt('Ends Monday, November 30.' if us else 'Ends Monday 30 November.', 14, 20, '#E6E3DC', 600, 'padding-top:12px;text-align:center;')
    return row(ESP, '28px 26px 0 26px', h, 'left', 'pad') + dark_button('Shop VIP Black Friday', utm(SALE, camp, ct + '-band'), FRIC(us) if not us else FR_INT.replace('duties paid', 'from the US') if 'duties paid' in FR_INT else FR_INT)
def gifts(us):
    h = gifts_tiles(False)
    return h.replace('Free shipping, duties paid', 'Free shipping') if us else h
BAD = ('next batch', 'reserve', 'arriving', 'next shipment', 'purifier', 'lifetime', 'for life', 'free filter', 'scratch-proof', 'while supplies last', 'VRAAG FLORIS')
files = {}
for mkt in ('us', 'int'):
    US = mkt == 'us'; M = mkt.upper(); c5 = 'e5-1110-' + mkt; c6 = 'e6-1111-' + mkt
    who = 'US Engaged 30D' if US else 'INT Engaged 30D'
    WHEN5 = 'di 10 nov 2026, ochtend lokale tijd'; WHEN6 = 'wo 11 nov 2026, ochtend lokale tijd'
    SMALL = ('Offer valid November 1 to 30. Gifts while the sale runs; the water filter is a weekly draw.' if US else 'Offer valid 1 to 30 November. The water filter is a weekly draw.')
    # ---------- E5 definitief: prep-plan, kort, zonder prijzen ----------
    subj = ('Your Thanksgiving, in 3 days and 2 pans', 'What can you cook before Thursday?') if US else ('A big dinner, in 3 days and 2 pans', 'What can you cook two days early?')
    pre = 'Tuesday, Wednesday, Thursday. The plan that frees up your stove.' if US else 'Day one, day two, the big day. The plan that frees up your stove.'
    b = HEAD(meta4('e5-%s-final · Prep-plan, kort, zonder prijzen' % mkt, M, 'Siraat', subj, pre, WHEN5, WHO5 % who, 'Floris 5 nov: één versie, zonder prijs, korter.'), subj[0], pre) + OPEN3()
    b += hero('Thanksgiving prep plan' if US else 'Big dinner prep plan', 'Three days.<br>Two pans.', 'One free stove on Thursday.' if US else 'One free stove on the day.',
              IM_SWEET, 'Golden maple sweet potato rounds in a Siraat Pan Pro', utm(SALE, c5, 'f-hero'))
    b += hero_btn('Shop VIP Black Friday', utm(SALE, c5, 'f-cta1'), US)
    b += P(("Benjamin here. Everything wants the stove at the same time on Thanksgiving. So two sides get done before Thursday, and on the day they only need warming up.") if US else
           ("Benjamin here. At a big dinner everything wants the stove at the same time. So two sides get done in the days before, and on the day they only need warming up."), '#FFFFFF', '6px 40px 18px 40px')
    loc = dict(HG); loc.update(b='', US=US, c5=c5); exec(DAYS, loc); b += loc['b']
    b += gap('#FFFFFF', 6)
    b += wide_card('large', 'Room for a whole batch of rounds.', US, '70% OFF', 'Shop the Pan Pro Large', utm(URL['large'], c5, 'f-card-large'))
    b += wide_card('deep', 'Higher sides for sauces, pasta and one-pan dinners.', US, 'UP TO 70% OFF', 'Shop the Deep Pan Pro', utm(URL['deep'], c5, 'f-card-deep'))
    b += gap('#FFFFFF', 10) + bf_short(US, c5, 'f') + gifts(US)
    b += closing('Have a good Thanksgiving,' if US else 'Happy cooking,').replace('6px 40px 4px 40px', '18px 40px 4px 40px') + sign()
    files['e5-%s-final' % mkt] = b + small(SMALL) + TAIL
    # ---------- E6 definitief: brief van Benjamin, kort, zonder prijzen ----------
    subj = ('December 20, 2024', 'Why this pan came first'); pre = "The original hammered titanium pan, and why it's 70% off this week."
    b = HEAD(meta4('e6-%s-final · Brief van Benjamin, kort, zonder prijzen' % mkt, M, 'Benjamin from Siraat', subj, pre, WHEN6, WHO6 % who, 'Floris 5 nov: één versie, zonder prijs, korter.'), subj[0], pre) + OPEN3()
    top = '34px 40px 16px 40px'
    if US:
        b += P('First, for Veterans Day: thank you to everyone who serves and has served.', '#FFFFFF', top); top = '0 40px 16px 40px'
        b += row('#FFFFFF', '0 20px 20px 20px', img(IM_VET, 'A folded American flag on a kitchen shelf above a Siraat pan on the stove', None, 560, 10), 'center', 'padx')
    b += P('Benjamin here. I want to tell you how the Pan Pro Standard happened.', '#FFFFFF', top)
    b += mini_offer(US, c6, 'f-card')
    b += P("Siraat didn't start with pans. We started with titanium cutting boards, and the next question was obvious: could you cook on titanium too, with nothing coated on top of it? The Pan Pro was the answer. A pure titanium cooking surface, a hammered pattern, no coatings of any kind. Since then, more than 100,000 people have bought from us.")
    b += row('#FFFFFF', '4px 20px 22px 20px', img(IM_EGG, 'An egg sliding out of a Siraat Pan Pro Standard onto toast', utm(URL['standard'], c6, 'f-img'), 560, 10), 'center', 'padx')
    b += P("No coating means nothing to wear thin and nothing to peel. It goes in the dishwasher, metal spatulas are fine, and Light Labs tested it for 31 PFAS compounds: every one came back below the detection limit.")
    b += P('This week it&#39;s <b>70% off</b>, with 4 gifts on every order.')
    b += pbtn('Get my Pan Pro at 70% off', utm(URL['standard'], c6, 'f-cta1'), US, '6px 30px 24px 30px')
    b += quote('R411' if US else 'R138')
    b += P("And it's covered for 75 years.") + sign()
    b += ps('30-day returns, counted from the day the box arrives. The sale ends %s.' % ('Monday, November 30' if US else 'Monday 30 November'))
    files['e6-%s-final' % mkt] = b + small(SMALL) + TAIL
for k, v in files.items():
    assert '—' not in v and '–' not in v, k
    body = v.split('-->', 1)[1]
    assert '$' not in body and not re.search(r'\{\{(PRICE|WAS|FROM)', body), (k, 'prijs')
    for bad in BAD: assert bad.lower() not in re.sub(r'<[^>]+>', ' ', body).lower(), (k, bad)
    if '-int-' in k: assert 'Veterans' not in body and not re.search(r'\{\{(GIFTS|FRICTION)', body), k
    open(os.path.join(N, k + '.html'), 'w').write(v); print('geschreven', k, len(v))
