"""Sunset en winback in Black Friday-stijl (plan research/plannen/2026-11-sunset-winback.md, 7 nov 2026). Concept, niets in Klaviyo.
- sbf-us / sbf-int: Sunset TbYQmX, nieuwe mail tussen S1 en S2 ("one last look at 70% off"), afzender Benjamin. Markt via profielland.
- wbf-us / wbf-int: BF-winback voor eerdere kopers (nieuwe flow 'v4 · Winback BF', segment-trigger zonder event, zie plan), markt via profielland.
Geen bedragen (alleen de gele sale-tag 70% OFF), geen code (BFCODE hoort alleen in abandonment), geen einddatum van de sale.
Hergebruikt de helpers van flows-nov/signup/_tools/make_bfw.py (die laadt homestead-e5-e6 make_final/make_e56/make_pl2).
Gebruik (vanuit /tmp): python3 -I make_sw.py, daarna python3 -I render_sw.py <uitmap> en node shot_sw.js <uitmap> <previewmap>."""
import os, re
B = '/home/user/siraat-email-agent/klaviyo/templates/v3/flows-nov/signup/_tools/make_bfw.py'
src = open(B).read().split('\nfiles = {}\n')[0]
g = {'__file__': B, '__name__': 'bfwhelpers'}; exec(compile(src, B, 'exec'), g)
globals().update({k: v for k, v in g.items() if not k.startswith('__')})
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IM_EGG_SLIDE = IM_EGG     # ei glijdt uit de Pan Pro op toast (Higgsfield 5 nov, Klaviyo-CDN)
IM_FEAST = IM_TABLE       # tafel met twee Siraat-pannen (Higgsfield 5 nov, Klaviyo-CDN)
check_reviews(['R583', 'R138'])

def HEADSW(meta_, subj, pre, signal):
    h = HEADBF(meta_, subj, pre).replace('FLOW Rn556d AANMELDING · BF-W2/BF-W3 (concept 6 nov 2026, niet in Klaviyo, niets live).',
                                        'SUNSET TbYQmX / WINBACK BF · VIP BLACK FRIDAY (concept 7 nov 2026, niet in Klaviyo, niets live).')
    # build_template.py leest de marktbron uit deze losse comment (de map heet niet sunset of winback); de export stript alle comments
    return h.replace('-->', '-->\n<!-- MARKET-SIGNAL: %s -->' % signal, 1)

files = {}
for mkt in ('us', 'int'):
    US = mkt == 'us'; M = mkt.upper(); cs = 'sunset-bf-' + mkt; cw = 'winback-bf-' + mkt
    SMALL = 'The water filter is a weekly draw.'

    # ======================= SBF · Sunset, laatste verkoopmail vóór S2 en de onderdrukking =======================
    subj = ('Before I stop writing: your 70% off', 'Still cooking on a coated pan?')
    alts = ('Your VIP Black Friday price, one last time', 'Up to 70% off, and 4 gifts. Last one from me.', '"The last pans we ever have to purchase"')
    pre = 'Up to 70% off, 4 gifts with every order, no code needed. The last sale email you will get from me.'
    who = ('Flow TbYQmX (segment WuHSm6, 120 d niet actief), %s; filter: geen klik (Bot Click = false) en geen order sinds flowstart; smart sending aan' %
           ('person.Country US of leeg' if US else 'person.Country bekend en niet US'))
    b = HEADSW(meta_bf('sbf-%s · Sunset: one last look at 70%% off' % mkt, M, 'Benjamin from Siraat', subj, alts, pre,
                       'S1 + 2 dagen, 09:00 lokale tijd (vóór S2, die schuift naar S1 + 4 dagen)', who,
                       'Sunset S1/S2 brengen $0,01 per ontvanger op. Eén verkoopmail met echte, ware schaarste: de laatste verkoopmail vóór onderdrukking. '
                       'Elke klik houdt de lezer op de lijst (kept-flow Wzz6xC). Voorwaarde: onderdrukkingsstap na S2 (zie plan), anders klopt "last sale email" niet.'),
               subj[0], pre, 'profile') + OPEN3()
    b += P("Hi, Benjamin here. It&#39;s been a while since you opened one of our emails, so I&#39;ll keep this one short.", '#FFFFFF', '34px 40px 14px 40px')
    b += glass_img(IM_EGG_SLIDE, utm(SALE, cs, 'hero'), 'VIP Black Friday', 'One last look<br>at 70% off.', 'Plus 4 gifts with every order. No code needed.', 400, 290, 34)
    b += hero_btn('Get my Black Friday price', utm(SALE, cs, 'cta1'), US, '#FFFFFF', '20px 30px 22px 30px')
    b += P('Our VIP Black Friday sale is live. Up to 70% off, 4 gifts in every box, nothing to type at checkout. '
           'If a pan with nothing on it to wear off was ever on your list, this is the moment I&#39;d pick it up.', '#FFFFFF', '4px 40px 14px 40px')
    b += P('Every pan has a pure titanium cooking surface and no coatings. Light Labs tested it for 31 PFAS compounds, and every one came back below the detection limit (report no. 25895).', '#FFFFFF', '0 40px 18px 40px')
    b += note_head('Where I&#39;d start')
    b += wide_card('standard', 'The everyday size. The pan Siraat started with.', US, '70% OFF', 'Get the Pan Pro', utm(URL['standard'], cs, 'card-standard'))
    b += wide_card('set6', 'Mini, Small and Large, each with its own lid. Just arrived and selling fast.', US, '70% OFF', 'Get the 6-piece set', utm(URL['set6'], cs, 'card-set6'))
    b += gap('#FFFFFF', 8) + quote('R583')
    b += P('This is the last sale email you&#39;ll get from me. One more short note after this, and then I&#39;ll stop writing. '
           'Unless you tap anything in this email: then you stay on the list and I&#39;ll only send what&#39;s worth opening.', '#FFFFFF', '6px 40px 10px 40px')
    b += P('Questions before you order? Reply and our team will help.', '#FFFFFF', '0 40px 8px 40px') + sign()
    b += gap('#FFFFFF', 18) + bf_short(US, cs, 'band').replace('Free shipping, from the US.', 'Free shipping from the US.').replace('Shop VIP Black Friday', 'Get my Black Friday price')
    files['sbf-%s' % mkt] = b + small(SMALL) + TAIL

    # ======================= WBF · Winback voor eerdere kopers =======================
    subj = ('Up to 70% off your second pan', '"I am on my 4th pan from Siraat"')
    alts = ('Your VIP Black Friday price is live', 'Ready for a second pan?', 'What I would add to your kitchen at 70% off')
    pre = '4 gifts with every order, no code needed. Here is where I would go next.'
    who = ('Nieuwe flow v4 · Winback BF (segment eerdere kopers, laatste order 45+ dagen geleden), %s; filters: geen order sinds flowstart, '
           'geen mail uit UyFc78/UEfh4h/X3ySuU in 7 dagen; smart sending aan' % ('person.Country US of leeg' if US else 'person.Country bekend en niet US'))
    b = HEADSW(meta_bf('wbf-%s · Winback BF: je volgende pan, tot 70%% off' % mkt, M, 'Benjamin from Siraat', subj, alts, pre,
                       'instap + 0 dagen, 10:00 lokale tijd (eenmalig in de BF-periode)', who,
                       'UyFc78 stuurt pas vanaf 23 nov (45 dagen wachttijd sinds livegang 8 okt), UEfh4h alleen voor orders van vóór 9 okt op dag 60. '
                       'Kopers van nov 2025 tot aug 2026 krijgen nu geen winback in de sale. A/B: aanbod (specifiek) tegen sociaal bewijs (letterlijke review).'),
               subj[0], pre, 'profile') + OPEN3()
    b += glass_img(IM_FEAST, utm(SALE, cw, 'hero'), 'VIP Black Friday', 'Your next pan,<br>up to 70% off.', 'Plus 4 gifts with every order.', 440, 290, 34)
    b += hero_btn('Get my VIP price', utm(SALE, cw, 'cta1'), US, '#FFFFFF', '20px 30px 22px 30px')
    b += P("Benjamin here. You&#39;ve had a Siraat box on your doorstep before, so I&#39;ll skip the pitch. "
           "Our VIP Black Friday sale is live: up to 70% off, 4 gifts in every box, no code needed.", '#FFFFFF', '4px 40px 14px 40px')
    b += P('Most kitchens need more than one pan. One for the eggs, one for the sauce, one that&#39;s big enough for everyone. '
           'Up to 70% off is a good moment for the second one.', '#FFFFFF', '0 40px 18px 40px')
    b += quote('R138')
    b += note_head('Where I&#39;d go next')
    b += wide_card('standard', 'The everyday size. The pan Siraat started with.', US, '70% OFF', 'Get the Pan Pro', utm(URL['standard'], cw, 'card-standard'))
    b += wide_card('deep', 'Higher sides for sauces, braises and one-pan dinners.', US, '70% OFF', 'Get the Deep Pan Pro', utm(URL['deep'], cw, 'card-deep'))
    b += wide_card('set6', 'Mini, Small and Large, each with its own lid. Just arrived and selling fast.', US, '70% OFF', 'Get the 6-piece set', utm(URL['set6'], cw, 'card-set6'))
    if US: b += wide_card('set12', 'The whole stove in one box, plus a free Pizza Steel.', US, '70% OFF', 'Get the 12-piece set', utm(URL['set12'], cw, 'card-set12'))
    b += P('A second pan also makes a good gift. Same 4 gifts in the box, whoever it&#39;s for. '
           'Every pan is covered for 75 years against defects, and you have 30 days to send it back unused.', '#FFFFFF', '14px 40px 10px 40px')
    b += P('Questions before you order? Reply and our team will help.', '#FFFFFF', '0 40px 8px 40px') + sign()
    b += gap('#FFFFFF', 18) + bf_short(US, cw, 'band').replace('Free shipping, from the US.', 'Free shipping from the US.').replace('Shop VIP Black Friday', 'Get my VIP price')
    files['wbf-%s' % mkt] = b + small(SMALL) + TAIL

for k, v in files.items():
    assert '\u2014' not in v and '\u2013' not in v, (k, 'streepje')
    body = v.split('-->', 1)[1]
    m = NODATE.search(re.sub(r'<[^>]+>', ' ', v.replace('&nbsp;', ' '))); assert not m, (k, 'einddatum', m and m.group(0))
    assert 'BFCODE' not in v and 'discount/' not in v, (k, 'code hoort niet in sunset/winback')
    assert '$' not in body and not re.search(r'\{\{(PRICE|WAS|FROM)', body), (k, 'prijs')
    assert 'VIP Black Friday' in body, (k, 'sale-label')
    plain = re.sub(r'<[^>]+>', ' ', body).lower()
    for bad in BAD + ('last chance', 'hurry', 'only a few'): assert bad not in plain, (k, bad)
    if '-int' in k: assert 'thanksgiving' not in plain and 'veterans' not in plain and not re.search(r'\{\{(GIFTS|FRICTION)', body) and 'set12' not in body and '12-piece' not in plain, k
    v = link_all(v)
    open(os.path.join(N, k + '.html'), 'w').write(v); print('geschreven', k, len(v))
