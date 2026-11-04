"""Prijslijst-campagne wo 4 nov 2026 (concept, niets live). US apart (focus 12-Pcs set) en INT apart (geen bedragen, alleen procenten).
Hergebruikt de bouwstenen van bfcm/november-v2/_tools/make_v2.py (alleen het helper-deel, de v2-bestanden worden niet overschreven).
Gebruik: python3 -I make_pl.py  (vanuit /tmp). Daarna render_pl.py en shot_pl.js."""
import os
V2 = '/home/user/siraat-email-agent/klaviyo/templates/v3/bfcm/november-v2/_tools/make_v2.py'
src = open(V2).read().split('# =====================================================================\n# FLOWS')[0]
g = {'__file__': V2, '__name__': 'v2helpers'}; exec(compile(src, V2, 'exec'), g); globals().update({k: v for k, v in g.items() if not k.startswith('__')})
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOP = 'VIP BLACK FRIDAY SALE IS LIVE'; VIP = 'VIP BLACK FRIDAY'
FREE = 'Free shipping &middot; 100,000+ customers'
files = {}
TILE['large'] = dict(TILE['large'], img=TILE['standard']['img'])  # oude afbeelding had nog een los BLACK FRIDAY-label

def meta2(id_, mkt, subj, pre, why):
    return 'ID: %s\nMARKT: %s\nSENDER: %s\nSUBJECT A: %s\nSUBJECT B: %s\nPREVIEW: %s\nWANNEER: wo 4 nov 2026 08:15 lokale tijd\nWIE: %s\nWAAROM: %s' % (
        id_, mkt, 'Benjamin from Siraat' if 'letter' in id_ else 'Siraat', subj[0], subj[1], pre,
        'Engaged 90D US v2 (VMjhb2) + No Country 90D (R5rFrC); excl. kopers sinds 1 nov en aanmelders laatste 3 dagen' if mkt == 'US' else 'Engaged 90D INT v2 (XrFa5r); excl. kopers sinds 1 nov en aanmelders laatste 3 dagen', why)
def set12_card(bg, c, ct, label='Get the 12-piece deal'):
    return deal(bg, '{{IMG}}/deal-set12-pizza.jpg', 'Titanium Hammered Cookware Set, 12 Pcs, with a free Pizza Steel', utm(U['set12p'], c, ct + '-set12'), [JA, SF],
                'Cookware Set, 12&nbsp;Pcs', '3 pans, 2 saucepans, a stockpot and 6 fitted lids. A whole kitchen with a pure titanium cooking surface, no coatings.',
                '{{WAS:set12}}', '{{PRICE:set12}}', '-68%', '+ FREE Pizza Steel ($664 value) with this set', label, FREE, 'THE COMPLETE SET')
def us_tiles(c, ct, keys):
    return grid(CREAM if True else None, [dict(TILE[k], url=utm(TILE[k]['url'], c, ct + '-' + k)) for k in keys])

# ---------------- US-A: alles om de 12-Pcs (gele hero + waardestapel) ----------------
c = 'pl-1104-us'
m = meta2('pl-us-a · De 12-Pcs als enige hoofddeal', 'US', ('Replace the whole kitchen. 68% off.', 'The 12-piece set + a free Pizza Steel'),
          'The full titanium set, plus a free Pizza Steel ($664 value). Just arrived and selling fast.',
          'US koopt vooral de 12-Pcs (Floris 4 nov). Eén deal, waardestapel met de gratis Pizza Steel, daarna bewijs en pas onderaan kleinere opties.')
b = head(m, 'Replace the whole kitchen. 68% off.', 'The full titanium set, plus a free Pizza Steel ($664 value). Just arrived and selling fast.', 'US') + OPEN(Y, TOP)
b += hero_yellow(VIP, 'Replace the', 'whole kitchen.', 'The 12-piece titanium set, 68% off. Plus a free Pizza Steel worth $664.',
                 'Get the 12-piece deal', utm(U['set12p'], c, 'a-hero'), 'No code needed. ' + FREE, '{{IMG}}/deal-set12-pizza.jpg', 'Titanium Hammered Cookware Set, 12 Pcs, with a free Pizza Steel')
b += band('JUST ARRIVED &nbsp;&middot;&nbsp; SELLING FAST', INK, Y)
b += gap(CREAM, 26)
b += stack(CREAM, [('Cookware Set, 12 Pcs (3 pans, 2 saucepans, stockpot, 6 lids)', '-68%'), ('Titanium Pizza Steel', 'FREE ($664 VALUE)'),
                   ('{{GIFTS:total}} with every order', 'FREE'), ('Shipping', 'FREE'), ('75-year warranty, 30-day returns', 'INCLUDED')],
           'Your VIP Black Friday price', '{{PRICE:set12}}')
b += cta_ink('Get the 12-piece deal', utm(U['set12p'], c, 'a-stack'), CREAM, '0 30px 30px 30px', FREE)
b += row(CREAM, '6px 24px 6px 24px', '<div class="hl" style="font-family:%s;font-size:30px;line-height:34px;font-weight:900;letter-spacing:-1px;color:%s;text-align:center;">What&#39;s in the box</div>' % (FF, INK), 'center', 'padx')
b += bullets(CREAM, ['Pan Pro Mini {{SIZE:20}}, Small {{SIZE:26}} and Large {{SIZE:30}}', '2-quart and 3-quart saucepans and an 8-quart stockpot', 'A fitted lid for every pan and pot',
                     'Pure titanium cooking surface. No coating to scratch or wear off.'])
b += proof(NIGHT, ['R398', 'R583', 'R169'], 'Why people buy the whole set')
b += stats(NIGHT) + cta('Get the 12-piece deal', utm(U['set12p'], c, 'a-proof'), NIGHT, '0 30px 34px 30px', FREE)
b += row(CREAM, '30px 24px 14px 24px', txt('Rather start smaller?', 22, 28, INK, 900, 'text-align:center;'), 'center', 'padx')
b += grid(CREAM, [dict(TILE[k], url=utm(TILE[k]['url'], c, 'a-' + k)) for k in ('set6', 'standard', 'wok', 'deep')])
b += cta('Shop the sale', utm(SALE, c, 'a-cta-end'), CREAM, '12px 30px 34px 30px', FREE)
files['pl-us-a'] = b + TAIL

# ---------------- US-B: prijslijst, 12-Pcs bovenaan ----------------
m = meta2('pl-us-b · Prijslijst, 12-Pcs bovenaan', 'US', ('The VIP Black Friday price list', 'Every price, one email'),
          'Up to 70% off, side by side. The 12-piece set comes with a free Pizza Steel.',
          'Smooche-stijl prijsmail: de prijs verkoopt. 12-Pcs groot bovenaan, daaronder alle andere deals naast elkaar.')
b = head(m, 'The VIP Black Friday price list', 'Up to 70% off, side by side. The 12-piece set comes with a free Pizza Steel.', 'US') + OPEN(CREAM, TOP)
b += row(CREAM, '36px 16px 0 16px', pill(VIP, center=True), 'center')
b += row(CREAM, '18px 16px 0 16px', '<div class="hx" style="font-family:%s;font-size:58px;line-height:56px;font-weight:900;letter-spacing:-2.2px;color:%s;text-transform:uppercase;">The price<br><span style="background-color:%s;padding:0 8px;">list.</span></div>' % (FF, INK, Y), 'center', 'padx')
b += row(CREAM, '18px 30px 26px 30px', txt('Up to 70% off. Free gifts with every order. No code needed.', 17, 26, '#3E3B37', 500, 'text-align:center;'), 'center')
b += row(CREAM, '0 20px 10px 20px', txt('#1 THIS WEEK', 12, 16, '#727272', 900, 'letter-spacing:2px;text-align:center;'), 'center', 'padx')
b += set12_card(CREAM, c, 'b')
b += band('EVERYTHING ELSE, UP TO 70% OFF') + gap(CREAM, 20)
b += grid(CREAM, [dict(TILE[k], url=utm(TILE[k]['url'], c, 'b-' + k)) for k in ('set6', 'standard', 'large', 'wok', 'deep', 'pizza')])
b += stats(CREAM)
b += cta_ink('Get the 12-piece deal', utm(U['set12p'], c, 'b-cta-end'), CREAM, '0 30px 34px 30px', FREE)
files['pl-us-b'] = b + TAIL

# ---------------- US-C: brief van Benjamin over de 12-Pcs ----------------
m = meta2('pl-us-c-letter · Brief van Benjamin over de 12-Pcs', 'US', ('If I were starting from zero', 'The one I would buy at 68% off'),
          'Benjamin here. One set, one decision, and a free Pizza Steel.',
          'Founder-brieven halen 1,3% klik tegenover 0,3 tot 0,6% voor beeldmails (PLAYBOOK 1). Zelfde aanbod, persoonlijke vorm.')
b = head(m, 'If I were starting from zero', 'Benjamin here. One set, one decision, and a free Pizza Steel.', 'US') + OPEN(CREAM, TOP)
b += P("Hi {{ first_name|default:'there' }},", '34px 40px 14px 40px')
b += P('Benjamin here. If I had to start my kitchen from zero this month, I would not buy pans one by one. I would buy the 12-piece set.')
b += P('Three pans, two saucepans, a stockpot and a lid for every one of them. All with a pure titanium cooking surface, so there is no coating to scratch or wear off. Ever.')
b += row(CREAM, '4px 20px 18px 20px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border-radius:10px;"><tr><td style="padding:0;">%s</td></tr><tr><td style="padding:18px 20px;">%s%s<div style="padding-top:10px;">%s</div>%s</td></tr></table>' % (
    img('{{IMG}}/deal-set12-pizza.jpg', 'Titanium Hammered Cookware Set, 12 Pcs, with a free Pizza Steel', utm(U['set12p'], c, 'c-img'), 0, 560),
    pills([JA, SF]), '<div style="font-family:%s;font-size:22px;line-height:28px;font-weight:900;color:%s;padding-top:8px;"><a href="%s" style="color:%s;text-decoration:none;">Cookware Set, 12&nbsp;Pcs &rarr;</a></div>' % (FF, INK, utm(U['set12p'], c, 'c-name'), INK),
    price_line('{{WAS:set12}}', '{{PRICE:set12}}', '-68%', False, False), txt('+ a free Pizza Steel ($664 value) and {{GIFTS:total}}', 15, 22, INK, 800, 'padding-top:10px;')), 'left', 'padx')
b += P('It just arrived in our warehouse, and it is selling fast. That is the honest reason I am writing today.')
b += cta_ink('Get the 12-piece deal', utm(U['set12p'], c, 'c-cta'), CREAM, '6px 40px 26px 40px', 'No code needed. ' + FREE)
b += P('You have 30 days to send it back unused, and it is covered for 75 years. Questions about sizes? Just reply.', '0 40px 12px 40px', CREAM, '#5E5A54', 15, 23) + sign()
files['pl-us-c-letter'] = b + TAIL

# ---------------- INT: geen bedragen, alleen procenten ----------------
ci = 'pl-1104-int'
def pct_tile(k, ct):
    t = dict(TILE[k]); t['url'] = utm(t['url'], ci, ct + '-' + k); t['was'] = '&nbsp;'; t['img'] = TILE['standard']['img'] if k == 'large' else t['img']; t['now'] = '70% OFF'; t['off'] = 'NOW'
    return t
m = meta2('pl-int-a · Prijslijst zonder bedragen', 'INT', ('The VIP Black Friday deals, side by side', '70% off. Here is all of it.'),
          '70% off, side by side. 4 free gifts with every order. No code needed.',
          'INT: gemengde markten, dus geen valuta (DECISIONS). De 6-Pcs is hier de grootste set; procenten in het oranje.')
b = head(m, 'The VIP Black Friday deals, side by side', '70% off, side by side. 4 free gifts with every order. No code needed.', 'INT') + OPEN(NIGHT, TOP)
b += hero_dark(VIP, 'Every deal,', 'one email.', '70% OFF', 'UP TO', 'Pure titanium pans and sets. 4 free gifts with every order. No code needed.',
               'Shop the sale', utm(SALE, ci, 'a-hero'), FREE)
b += band('JUST ARRIVED &nbsp;&middot;&nbsp; SELLING FAST') + gap(CREAM, 24)
b += deal(CREAM, '{{IMG}}/deal-set6.jpg', 'Titanium Hammered Pan Set with Lids, 6 Pcs', utm(U['set6'], ci, 'a-set6'), [JA, SF], 'Pan Set with Lids, 6&nbsp;Pcs',
          'Pan Pro Mini, Small and Large, each with its own fitted lid. Pure titanium cooking surface, no coatings.', '', '70% OFF', 'VIP', '+ 4 free gifts with every order',
          'Get the 6-piece deal', FREE, 'THE STARTER SET')
b += grid(CREAM, [pct_tile(k, 'a') for k in ('standard', 'large', 'wok', 'deep', 'small', 'pizza')])
b += stats(CREAM)
b += cta('Shop the sale', utm(SALE, ci, 'a-cta-end'), CREAM, '0 30px 34px 30px', FREE)
files['pl-int-a'] = b + TAIL

m = meta2('pl-int-b-letter · Brief van Benjamin, drie keuzes', 'INT', ('What I would buy at 70% off', 'Three picks, depending on your kitchen'),
          'Benjamin here. Three picks, all 70% off, no code needed.', 'Brief-vorm voor betrokken lezers, zonder bedragen.')
b = head(m, 'What I would buy at 70% off', 'Benjamin here. Three picks, all 70% off, no code needed.', 'INT') + OPEN(CREAM, TOP)
b += P("Hi {{ first_name|default:'there' }},", '34px 40px 14px 40px')
b += P('Benjamin here. People keep asking me the same question this month: with everything 70% off, what should I actually buy? Here is my honest answer.')
pick = lambda n, t, d, url: row(CREAM, '0 20px 12px 20px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border-radius:10px;"><tr><td style="padding:18px 20px;">%s%s%s<div style="padding-top:10px;">%s</div></td></tr></table>' % (
    txt(n, 12, 14, '#727272', 900, 'letter-spacing:2px;'), '<div style="font-family:%s;font-size:21px;line-height:27px;font-weight:900;color:%s;padding-top:6px;"><a href="%s" style="color:%s;text-decoration:none;">%s &rarr;</a></div>' % (FF, INK, url, INK, t),
    txt(d, 16, 24, '#3E3B37', 400, 'padding-top:6px;'), '<span style="display:inline-block;background-color:%s;color:%s;font-family:%s;font-size:14px;line-height:16px;font-weight:900;padding:7px 10px;border-radius:3px;">70%% OFF</span>' % (Y, INK, FF)), 'left', 'padx')
b += pick('IF YOU WANT ONE PAN', 'Pan Pro Standard {{SIZE:28}}', 'The size most people cook with every day. If you are not sure, start here.', utm(U['standard'], ci, 'b-standard'))
b += pick('IF YOU COOK FOR TWO OR MORE', 'Pan Set with Lids, 6&nbsp;Pcs', 'Mini, Small and Large, each with a lid. Just arrived, and selling fast.', utm(U['set6'], ci, 'b-set6'))
b += pick('IF YOU STIR-FRY OR SEAR A LOT', 'Wok Pan Pro', 'High sides, a flat base, and nothing on the surface to wear off.', utm(U['wok'], ci, 'b-wok'))
b += P('Whatever you pick: it ships with 4 free gifts, you have 30 days to send it back unused, and it is covered for 75 years.', '14px 40px 6px 40px')
b += cta('Shop the sale', utm(SALE, ci, 'b-cta'), CREAM, '16px 40px 24px 40px', 'No code needed. ' + FREE)
b += P('Not sure about a size? Reply and our team will help.', '0 40px 12px 40px', CREAM, '#5E5A54', 15, 23) + sign()
files['pl-int-b-letter'] = b + TAIL

for k, v in files.items():
    assert '—' not in v, k
    body = v.split('-->', 1)[1]
    for bad in ('next batch', 'NEXT BATCH', 'reserve', 'arriving', 'next shipment', 'Ends Monday'):
        assert bad not in body, (k, bad)
    if '-int-' in k: assert '$' not in body and '{{PRICE' not in body and '{{WAS' not in body and '{{GIFTS' not in body, k
    open(os.path.join(N, k + '.html'), 'w').write(v); print('geschreven', k, len(v))
