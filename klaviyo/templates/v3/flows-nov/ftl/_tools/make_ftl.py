"""Failure to launch T2SmtR in Black Friday-stijl (plan research/plannen/2026-11-ftl-bf.md, 7 nov 2026). Concept, niets in Klaviyo.
Drie verkoopmails tot 30 nov, elk US en INT, markt via profielland (lijsttrigger, geen event):
- ftl1 (dag 30, slot 90675582): brief van Benjamin, VIP-prijs en 4 gifts voorop.
- ftl2 (dag 32, slot 90675586): titanium tegen coating (het enige oude FTL-onderwerp dat verkocht), Light Labs, reviews.
- ftl3 (dag 35, slot 108678769): welke pan eerst, twee beloftes, laatste mail van de reeks.
Geen bedragen (alleen de gele sale-tag 70% OFF), geen code (BFCODE hoort alleen in abandonment), geen einddatum van de sale.
Hergebruikt de helpers van flows-nov/signup/_tools/make_bfw.py (BF-topbalk, lockup-header en vaste footer via {{HEADER}}/{{FOOTER}}).
Gebruik (vanuit /tmp): python3 -I make_ftl.py, daarna python3 -I render_ftl.py <uitmap> en node shot_ftl.js <uitmap> <previewmap>."""
import os, re
B = '/home/user/siraat-email-agent/klaviyo/templates/v3/flows-nov/signup/_tools/make_bfw.py'
src = open(B).read().split('\nfiles = {}\n')[0]
g = {'__file__': B, '__name__': 'bfwhelpers'}; exec(compile(src, B, 'exec'), g)
globals().update({k: v for k, v in g.items() if not k.startswith('__')})
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Echte Shopify-lifestylebeelden (PDP Deep Pan Pro), niet eerder in FTL of Rn556d gebruikt
IM_FAMILY, IM_RAGU, IM_BRAISE = C43(FAMILY), C43(RAGU), C43(BRAISE)
HG['REVS'].update({'R169': ('The real test was my egg the next morning... the egg released completely and slid around the pan like it was non-stick.', 'Michael G.')})
check_reviews(['R583', 'R138', 'R169', 'R240'])

def HEADFTL(meta_, subj, pre):
    h = HEADBF(meta_, subj, pre).replace('FLOW Rn556d AANMELDING · BF-W2/BF-W3 (concept 6 nov 2026, niet in Klaviyo, niets live).',
                                        'FLOW T2SmtR FAILURE TO LAUNCH · VIP BLACK FRIDAY (concept 7 nov 2026, niet in Klaviyo, niets live).')
    return h.replace('-->', '-->\n<!-- MARKET-SIGNAL: profile -->', 1)
def band(us, camp, label):
    return gap('#FFFFFF', 18) + bf_short(us, camp, 'band').replace('Free shipping, from the US.', 'Free shipping from the US.').replace('Shop VIP Black Friday', label)

WHO = ('Flow T2SmtR (lijst Uw8eZG, 30 dagen na aanmelding, geen order sinds flowstart, geen W2 in 60 d), %s; '
       'smart sending UIT, 19:00 lokale tijd (na de campagne van 08:15, zie plan)')
files = {}
for mkt in ('us', 'int'):
    US = mkt == 'us'; M = mkt.upper(); c1, c2, c3 = 'ftl-bf1-' + mkt, 'ftl-bf2-' + mkt, 'ftl-bf3-' + mkt
    who = WHO % ('person.Country US of leeg' if US else 'person.Country bekend en niet US')
    SMALL = 'The water filter is a weekly draw.'

    # ======================= FTL-BF1 · dag 30 · brief van Benjamin, aanbod voorop =======================
    subj = ('Up to 70% off, a month after you signed up', '"The last pans we ever have to purchase"')
    alts = ('Your VIP Black Friday price is live', '15 coated pans, or one', 'Where I would start at 70% off')
    pre = 'Up to 70% off and 4 gifts with every order. No code needed.'
    b = HEADFTL(meta_bf('ftl1-%s · Dag 30: je VIP-prijs, brief van Benjamin' % mkt, M, 'Benjamin from Siraat', subj, alts, pre,
                        'dag 30 na aanmelding, 19:00 lokale tijd (slot 90675582, was Bestsellers, draft)', who,
                        'Oude FTL-mails waren beeldmails met 56%-banner en 100-day: $0,01 tot $0,04 per ontvanger. Aanbod en knop boven de vouw, '
                        'prijsbezwaar (27%) beantwoorden met waarde over tijd. A/B: aanbod (specifiek) tegen verhaal (letterlijke review).'), subj[0], pre) + OPEN3()
    b += P("Hi, Benjamin here. You signed up about a month ago and haven&#39;t picked a pan yet. Fair enough, a pan is a real decision. "
           "So here&#39;s the best moment I can give you: our VIP Black Friday sale is live.", '#FFFFFF', '34px 40px 16px 40px')
    b += glass_img(IM_FAMILY, utm(SALE, c1, 'hero'), 'VIP Black Friday', 'Up to 70% off.<br>4 gifts in every box.', 'No code needed.', 420, 290, 34)
    b += hero_btn('Get my VIP price', utm(SALE, c1, 'cta1'), US, '#FFFFFF', '20px 30px 22px 30px')
    b += P('A pure titanium cooking surface, no coatings. Light Labs tested it for 31 PFAS compounds (report no. 25895), and every one came back below the detection limit.', '#FFFFFF', '4px 40px 18px 40px')
    b += note_head('Where I&#39;d start')
    b += wide_card('standard', 'The everyday size. The pan Siraat started with.', US, '70% OFF', 'Get the Pan Pro', utm(URL['standard'], c1, 'card-standard'))
    b += wide_card('set6', 'Mini, Small and Large, each with its own lid. Just arrived and selling fast.', US, '70% OFF', 'Get the 6-piece set', utm(URL['set6'], c1, 'card-set6'))
    if US: b += wide_card('set12', 'The whole stove in one box, plus a free Pizza Steel.', US, '70% OFF', 'Get the 12-piece set', utm(URL['set12'], c1, 'card-set12'))
    b += gifts(US)
    b += P('Is it worth it? A coated pan is a pan you end up buying again. Ours is covered for 75 years against defects, '
           'and you have 30 days to send it back unused.', '#FFFFFF', '18px 40px 16px 40px')
    b += quote('R583')
    b += P('Questions before you order? Reply and our team will help.', '#FFFFFF', '0 40px 8px 40px') + sign()
    b += band(US, c1, 'Get my VIP price')
    files['ftl1-%s' % mkt] = b + small(SMALL) + TAIL

    # ======================= FTL-BF2 · dag 32 · titanium tegen coating =======================
    subj = ('Your pan vs ours, now up to 70% off', 'Report no. 25895')
    alts = ('Has your pan ever been tested?', 'Coated, stainless or titanium?', 'Why ours is covered for 75 years')
    pre = 'What a coating does over time, and what we put on paper instead. Up to 70% off, plus 4 gifts.'
    b = HEADFTL(meta_bf('ftl2-%s · Dag 32: titanium tegen coating, bewijs' % mkt, M, 'Siraat', subj, alts, pre,
                        'dag 32, 19:00 lokale tijd (slot 90675586, was FAQ&#39;s, draft)', who,
                        'Titanium vs Non-Stick was de enige oude FTL-mail met omzet ($0,13 per ontvanger in 14 d). Zelfde idee, nu met aanbod, vergelijking, '
                        'Light Labs en reviews. A/B: specifiek (aanbod) tegen autoriteit (rapportnummer).'), subj[0], pre) + OPEN3()
    b += glass_img(IM_RAGU, utm(SALE, c2, 'hero'), 'VIP Black Friday', 'Nothing on it<br>to wear off.', 'Up to 70% off, plus 4 gifts.', 440, 290, 34)
    b += hero_btn('Get my Black Friday price', utm(SALE, c2, 'cta1'), US, '#FFFFFF', '20px 30px 22px 30px')
    b += P('A coated pan is a pan with a layer on it, and layers wear. That&#39;s the whole difference. '
           'Ours has a pure titanium cooking surface and no coatings, so there is nothing to wear thin or flake into your food.', '#FFFFFF', '4px 40px 18px 40px')
    b += compare()
    b += labs_card(US, c2)
    b += revblock(['R169', 'R240'], CREAM, 'In their words')
    b += heading('Where to start', '#FFFFFF', '30px 24px 16px 24px')
    b += wide_card('standard', 'The everyday size. The pan Siraat started with.', US, '70% OFF', 'Get the Pan Pro', utm(URL['standard'], c2, 'card-standard'))
    b += wide_card('set6', 'Mini, Small and Large, each with its own lid. Selling fast.', US, '70% OFF', 'Get the 6-piece set', utm(URL['set6'], c2, 'card-set6'))
    if US: b += wide_card('set12', '3 pans, 3 pots, 6 lids, plus a free Pizza Steel.', US, '70% OFF', 'Get the 12-piece set', utm(URL['set12'], c2, 'card-set12'))
    b += row('#FFFFFF', '2px 30px 10px 30px', txt(FRIC(US), 13, 19, GREY, 500, 'text-align:center;'), 'center')
    b += band(US, c2, 'Get my Black Friday price')
    files['ftl2-%s' % mkt] = b + small(SMALL) + TAIL

    # ======================= FTL-BF3 · dag 35 · welke pan eerst, twee beloftes =======================
    subj = ('Still deciding? Here is the short version', '"I am on my 4th pan from Siraat"')
    alts = ('Which pan first? Here is how I would choose', 'Two promises before you pick a pan', 'Up to 70% off the sets')
    pre = 'Which pan to start with, and what happens if it is not right. Up to 70% off, plus 4 gifts.'
    b = HEADFTL(meta_bf('ftl3-%s · Dag 35: welke pan eerst, twee beloftes' % mkt, M, 'Benjamin from Siraat', subj, alts, pre,
                        'dag 35, 19:00 lokale tijd (slot 108678769, was How to Store + Care, live)', who,
                        'Twijfels na prijs: maat (15%) en werkt titanium echt (15%). Laatste mail van de reeks, dus volledige risico-omkering. '
                        'A/B: specifiek (korte versie) tegen verhaal (letterlijke review).'), subj[0], pre) + OPEN3()
    b += P("Benjamin here, with the last note in this series. If a pan has been on your list since you signed up, here&#39;s the short version.", '#FFFFFF', '34px 40px 16px 40px')
    b += glass_img(IM_BRAISE, utm(SALE, c3, 'hero'), 'VIP Black Friday', 'Which pan first?', 'Up to 70% off, plus 4 gifts.', 420, 290, 34)
    b += hero_btn('Find my pan', utm(SALE, c3, 'cta1'), US, '#FFFFFF', '20px 30px 22px 30px')
    b += note_head('How I&#39;d choose')
    b += wide_card('standard', 'Cooking for one or two. Eggs, steak, the everyday pan.', US, '70% OFF', 'Get the Pan Pro', utm(URL['standard'], c3, 'card-standard'))
    b += wide_card('deep', 'Higher sides for sauces, braises and one-pan dinners.', US, '70% OFF', 'Get the Deep Pan Pro', utm(URL['deep'], c3, 'card-deep'))
    b += wide_card('set6', 'Cooking for a family. Three sizes, each with its own lid.', US, '70% OFF', 'Get the 6-piece set', utm(URL['set6'], c3, 'card-set6'))
    if US: b += wide_card('set12', 'Replacing everything at once. Plus a free Pizza Steel.', US, '70% OFF', 'Get the 12-piece set', utm(URL['set12'], c3, 'card-set12'))
    b += P('Does titanium really work? It does, with one habit: heat it first. Medium heat for 2 to 3 minutes, until a drop of water forms a ball and glides. '
           'Then a teaspoon of oil. Cold metal grabs your food, hot metal lets it go.', '#FFFFFF', '18px 40px 18px 40px')
    b += quote('R138')
    b += promises()
    b += P('Questions before you order? Reply and our team will help.', '#FFFFFF', '24px 40px 8px 40px') + sign()
    b += band(US, c3, 'Find my pan')
    files['ftl3-%s' % mkt] = b + small(SMALL) + TAIL

for k, v in files.items():
    assert '—' not in v and '–' not in v, (k, 'streepje')
    body = v.split('-->', 1)[1]
    m = NODATE.search(re.sub(r'<[^>]+>', ' ', v.replace('&nbsp;', ' '))); assert not m, (k, 'einddatum', m and m.group(0))
    assert 'BFCODE' not in v and 'discount/' not in v, (k, 'code hoort niet in FTL')
    assert '$' not in body and not re.search(r'\{\{(PRICE|WAS|FROM)', body), (k, 'prijs')
    assert 'VIP Black Friday' in body and '{{HEADER}}' in body and '{{FOOTER}}' in v, (k, 'label/header/footer')
    plain = re.sub(r'<[^>]+>', ' ', body).lower()
    for bad in BAD + ('last chance', 'hurry', 'only a few', '100-day', 'prime time', '56%'): assert bad not in plain, (k, bad)
    if '-int' in k: assert 'thanksgiving' not in plain and not re.search(r'\{\{(GIFTS|FRICTION)', body) and 'set12' not in body and '12-piece' not in plain, k
    v = link_all(v)
    open(os.path.join(N, k + '.html'), 'w').write(v); print('geschreven', k, len(v))
