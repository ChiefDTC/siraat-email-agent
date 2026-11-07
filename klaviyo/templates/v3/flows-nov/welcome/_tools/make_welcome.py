"""Welcome T4a5Mk (v4 · Welcome), herschreven staart W2 t/m W5 voor Black Friday (audit 7 nov 2026, research/plannen/2026-11-welcome-audit.md).
Waarom: W1 haalt $3.09 per ontvanger, W2 t/m W5 maar $0.07 tot $0.50. Patroon van de benchmark BF-W1 (Rn556d, $3.58): aanbod in onderwerp,
preview en eerste scherm, producten met prijs (US) en 70% OFF-tag, veel productlinks, kort. Per mail één idee en één primaire knop (boven en onder),
productkaarten als route. Geen einddatum van de sale (Floris 7 nov). Geel alleen op de sale-tag, topbalk en knoppen ink (DECISIONS 5 nov).
Mails: wn2 (Pan Pro Standard, brief Benjamin), wn3 (bon: wat 70% off oplevert, 6-delige set), wn4 (maat kiezen, alle maten met prijs),
wn5 (laatste welkomstmail: waar ik zou beginnen, twee beloftes). Elk US en INT. US: prijzen via {{PRICE}}/{{WAS}} met US-terugval (zoals BF-W1);
INT: geen bedragen, alleen de tag. Schakelaar PRICES_US=False geeft de prijsloze variant (zoals BF-W2/BF-W3).
Hergebruikt de helpers uit homestead-e5-e6/_tools/make_final.py (laadt make_e56.py en make_pl2.py). Concept, niets in Klaviyo.
Gebruik (vanuit /tmp): python3 -I make_welcome.py, daarna python3 -I render_welcome.py <uitmap> en node shot_welcome.js <uitmap> <previewmap>."""
import os, re, csv
F = '/home/user/siraat-email-agent/klaviyo/templates/v3/campaigns/homestead-e5-e6/_tools/make_final.py'
src = open(F).read().split('\nfiles = {}\n')[0]
g = {'__file__': F, '__name__': 'finalhelpers'}; exec(compile(src, F, 'exec'), g)
globals().update({k: v for k, v in g.items() if not k.startswith('__')})
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = '/home/user/siraat-email-agent'

PRICES_US = True   # True = US-prijzen zoals BF-W1 (benchmark); False = alleen de 70% OFF-tag zoals BF-W2/BF-W3
if PRICES_US:      # make_final zet prijzen uit; hier terug aan voor US (INT blijft tag-only via us=False)
    HG['price_line'], HG['pricebar'] = _pl, _pb

# ---------------------------------------------------------------- producten erbij (Mini, Small), bedragen uit de catalogus
PK.update({'mini': 'Titanium_hammered_pan_pro_mini_65b75fe4-5d77-49af-80a0-eb0b3a78e303.webp',
           'small': 'Titanium_hammered_pan_pro_small_76f7b49e-60cd-4e03-a90e-e72411c244d4.webp'})
URL.update({'mini': PRD + 'titanium-hammered-pan-pro-mini', 'small': PRD + 'titanium-hammered-pan-pro-small'})
NAME.update({'mini': 'Pan Pro Mini &middot; {{SIZE:20}}', 'small': 'Pan Pro Small &middot; {{SIZE:26}}'})
for k in ('mini', 'small'): AMT[k] = (V.amount(k, 'US', 'price'), V.amount(k, 'US', 'compare_at'))
NAME_SIZED = {'standard': 'Pan Pro Standard &middot; {{SIZE:28}}', 'large': 'Pan Pro Large &middot; {{SIZE:30}}'}

# ---------------------------------------------------------------- beelden (Klaviyo- en Shopify-CDN; niet dezelfde als BF-W1/W2/W3 in dezelfde reis)
IM_TABLE_ = IM_TABLE                                   # tafel met twee Siraat-pannen (Higgsfield 5 nov)
IM_EGG_ = IM_EGG                                       # ei glijdt uit de Pan Pro Standard op toast (Higgsfield 5 nov)
IM_RANGE = CDN + 'P022-A_GasRange_2560w_q76.webp?width=1200&height=800&crop=center&format=pjpg'   # shootfoto gasfornuis
IM_FAM = C11(FAMILY)                                   # Deep Pan Pro, familiediner (PDP-lifestyle)

# ---------------------------------------------------------------- reviews (letterlijk, gecontroleerd tegen reviews.csv)
HG['REVS'].update({
    'R555': ('Awesome pan and peace of mind that I am not ingesting bits of toxins when I cook. Nice looking pan too!', 'Gwen'),
    'R138': ("I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns.", 'Tammy'),
})
def check_reviews(ids):
    rev = {r['id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'content/reviews/reviews.csv')))}
    for k in ids:
        q = HG['REVS'][k][0]; o = rev[k]['quote']; pos = 0
        assert rev[k]['stars'] == '5', (k, 'sterren')
        for p in [p.strip() for p in q.split('...') if p.strip()]:
            j = o.find(p, pos); assert j >= 0, (k, 'niet letterlijk', p); pos = j + len(p)
        assert len(q) <= 120, (k, len(q))
check_reviews(['R555', 'R138', 'R169', 'R011'])

# ---------------------------------------------------------------- bouwstenen
def big_quote(q, who, bg='#FFFFFF'):
    return row(bg, '30px 34px 24px 34px', txt('&#9733;&#9733;&#9733;&#9733;&#9733;', 15, 18, GOLD, 400, 'letter-spacing:3px;text-align:center;padding-bottom:10px;')
               + serif('&ldquo;%s&rdquo;' % q, 26, 33, INK, 'h1s', True, 'text-align:center;') + txt(who, 13, 18, '#8A847A', 600, 'text-align:center;padding-top:10px;letter-spacing:0.4px;'), 'center')
def bullet_row(items, bg='#FFFFFF', pad='0 40px 16px 40px'):
    return row(bg, pad, bullets(items, '#2E2E2E', GOLD, 16, 24), 'left', 'pad')
def small_head(t, bg='#FFFFFF', pad='22px 24px 14px 24px'):
    return row(bg, pad, serif(t, 28, 32, INK, 'ptitle', True, 'text-align:center;'), 'center')
def card(k, line, us, label, link, name=None):
    """wide_card met optionele naam (maat in de naam)."""
    if name:
        old = NAME[k]; NAME[k] = name
        try: return wide_card(k, line, us, '70% OFF', label, link)
        finally: NAME[k] = old
    return wide_card(k, line, us, '70% OFF', label, link)
def receipt_set6(us):
    """Bon voor de 6-delige set: product, 3 gifts, de filter-kans, garantie en retour. US met bedragen (filter telt niet mee), INT zonder."""
    li = lambda a, b, strong=False: '<tr><td valign="top" style="padding:11px 0;border-bottom:1px dashed #D8D1C4;">%s</td><td align="right" width="40%%" valign="top" style="padding:11px 0 11px 10px;border-bottom:1px dashed #D8D1C4;">%s</td></tr>' % (
        txt(a, 15, 21, INK, 700 if strong else 500), txt(b, 15, 21, INK if strong else '#6E6A64', 700 if strong else 500, 'text-align:right;'))
    if us and PRICES_US:
        rows_ = [('Pan Set with Lids, 6 pieces', '<span style="text-decoration:line-through;color:#B5B5B5;">%s</span> %s' % (WAS('set6'), PRICE('set6'))),
                 ('Free shipping', '{{IF:US}}{{GIFTS:ship}} {{ENDIF}}included'), ('E-book', '{{IF:US}}{{GIFTS:ebook}} {{ENDIF}}included'),
                 ('Mystery gift in the box', '{{IF:US}}{{GIFTS:mystery}} {{ENDIF}}included'), ('Weekly chance to win {{GIFTS:filterline}}', 'entered with your order'),
                 ('75-year warranty', 'included'), ('30-day returns', 'included')]
        value = usd(AMT['set6'][1] + sum(V.GIFT['US'][i] for i in (0, 1, 2)))
        tot = li('Value', value, True) + li('Your price', PRICE('set6'), True)
    else:
        rows_ = [('Pan Set with Lids, 6 pieces', '70% off'), ('Free shipping' + ('' if us else ', duties paid'), 'included'), ('E-book', 'included'),
                 ('Mystery gift in the box', 'included'), ('Weekly chance to win a PFAS water filter', 'entered with your order'), ('75-year warranty', 'included'), ('30-day returns', 'included')]
        tot = ''
    t = eyebrow('Your receipt', INK, 'padding-bottom:6px;text-align:center;') + '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px dashed #D8D1C4;">%s%s</table>' % (''.join(li(a, b) for a, b in rows_), tot)
    return row('#FFFFFF', '8px 20px 22px 20px', boxed(t, '#E4DED3', '#FFFDF8', '18px 18px 8px 18px'), 'left', 'padx')
GIFTLINE = '4 gifts with every order: free shipping, an e-book, a mystery gift and a weekly chance to win a PFAS water filter.'
def giftline(bg=CREAM, pad='16px 30px 16px 30px'):
    return row(bg, pad, txt(GIFTLINE, 14, 21, INK, 600, 'text-align:center;'), 'center', 'padx')
def meta_w(id_, mkt, sender, subj, alts, pre, when, who, why):
    return ('ID: %s\nMARKT: %s\nSENDER: %s\nSUBJECT A: %s\nSUBJECT B: %s\nANDERE ONDERWERPEN: %s\nPREVIEW: %s\nWANNEER: %s\nWIE: %s\nWAAROM: %s' % (id_, mkt, sender, subj[0], subj[1], ' · '.join(alts), pre, when, who, why))
def HEADW(meta_, subj, pre):
    h = head(meta_, subj, pre)
    for s in ('HOMESTEAD E5/E6 · NOVEMBER 2026 (concept 5 nov 2026, niet in Klaviyo, niets live).',
              'ROASTING PAN INT · NEW IN STOCK + BLACK FRIDAY SPECIAL (concept 1 nov 2026, niet in Klaviyo, niets live).'):
        h = h.replace(s, 'WELCOME T4a5Mk · NIEUWE W2-W5 VOOR BLACK FRIDAY (concept 7 nov 2026, niet in Klaviyo, niets live).')
    return h

NODATE = re.compile(r'(?i)(30 nov|nov 30|november 30|30 november|1 to 30|sale ends|ends monday|until nov|until 30|until it ends|while the sale runs|through nov|after that, (prices|regular))')
BAD = ('next batch', 'reserve', 'arriving', 'next shipment', 'purifier', 'lifetime', 'for life', 'free filter', 'scratch-proof', 'while supplies last',
       'vraag floris', 'risk-free', 'money-back', 'free returns', '100-day', 'shop now', 'learn more', 'buy now', 'delve', 'unlock', 'elevate', 'journey', 'seamless',
       "don't miss", 'hurry', 'only a few left', 'last chance', 'expires')
WHO = 'Flow T4a5Mk (lijst Uw8eZG), slot %s, arm B (nieuw) van de test nieuw tegen huidig; %s; filter Placed Order = 0 sinds flowstart'
SMALL = 'Up to 70% off and 4 gifts with every order, no code needed. The water filter is a weekly draw.'

files = {}
for mkt in ('us', 'int'):
    US = mkt == 'us'; M = mkt.upper()
    who_m = 'US (land US of United States)' if US else 'INT (alle andere profielen, ook zonder land)'

    # ======================= WN2 · De pan waarmee Siraat begon (brief Benjamin, Pan Pro Standard) =======================
    c = 'wn2-' + mkt
    subj = ("The one pan I'd buy at 70% off", 'December 20, 2024')
    alts = ('The pan we started with is 70% off', 'If you only buy one pan this Black Friday?', '"The only pan you will need in your kitchen"')
    pre = 'Pan Pro Standard: 70% off, 4 gifts with it, no code needed.'
    b = HEADW(meta_w('wn2-%s · Brief van Benjamin, één product (Pan Pro Standard), aanbod in het eerste scherm' % mkt, M, 'Benjamin from Siraat', subj, alts, pre,
                     'slot W2 (dag 1 10:00 in de huidige flow; dag 3 als vervolg op BF-W3)', WHO % ('W2', who_m),
                     'W2 nu $0.47/ontvanger: sale alleen in de P.S., geen product, geen prijs. Nieuw: product, prijs en knop boven de vouw, verhaal in 3 zinnen.'), subj[0], pre) + OPEN3()
    std = utm(URL['standard'], c, 'hero')
    b += glass_img(IM_EGG_, std, 'VIP Black Friday', 'The pan Siraat<br>started with.', 'Pan Pro Standard &middot; 70% off, plus 4 gifts', 460, 290, 34)
    b += pricebar('standard', US, '70% OFF', '#FFFFFF', '22px 20px 0 20px')
    b += hero_btn('Get my Pan Pro at 70% off', utm(URL['standard'], c, 'cta1'), US, '#FFFFFF', '16px 30px 22px 30px')
    b += P("Benjamin here. If you buy one thing from us this Black Friday, I&#39;d make it this pan.", '#FFFFFF', '6px 40px 16px 40px')
    b += P("It&#39;s the first pan we ever shipped, on December 20, 2024. A pure titanium cooking surface, a hammered pattern, no coatings. Since then, more than 100,000 people have bought from us.")
    b += bullet_row(['No coating, so nothing to wear thin or flake into your food.', 'Metal spatulas, the dishwasher and the oven are all fine.',
                     'Light Labs tested it for 31 PFAS compounds. Every one came back below the detection limit.', 'Covered for 75 years against defects.'])
    b += P("One honest thing: give it 2 to 3 minutes on medium heat before the food goes in. Cold metal grabs your food, hot metal lets it go.", '#FFFFFF', '0 40px 6px 40px')
    b += quote('R555', '#FFFFFF').replace('0 40px 18px 40px', '10px 40px 22px 40px')
    b += small_head('Cooking for more than two?', '#FFFFFF', '8px 24px 14px 24px')
    b += card('set6', 'Mini, Small and Large, each with its own lid.', US, 'Get the 6-piece set', utm(URL['set6'], c, 'card-set6'))
    if US: b += card('set12', '3 pans, 3 pots, 6 lids, plus a free Pizza Steel.', US, 'Get the 12-piece set', utm(URL['set12'], c, 'card-set12'))
    b += pbtn('Get my Pan Pro at 70% off', utm(URL['standard'], c, 'cta-end'), US, '14px 30px 24px 30px')
    b += P('Questions about size or your stovetop? Reply and our team will help.', '#FFFFFF', '0 40px 8px 40px') + sign()
    b += ps('The Standard is %s, the right size for 2 to 4 people.' % ('11 inches (28 cm)' if US else '28 cm'))
    files['wn2-' + mkt] = b + small(SMALL) + TAIL

    # ======================= WN3 · Wat 70% off oplevert (bon, 6-delige set; bezwaar prijs) =======================
    c = 'wn3-' + mkt
    subj = ('What 70% off actually gets you', '"Expensive but definitely Value for money"')
    alts = (('Under $100 a pan, lid included',) if US else ('Three pans, three lids, 70% off',)) + ('Is titanium worth the price?', 'Your receipt, line by line')
    pre = ('The 6-piece set: under $100 a pan, lids and 4 gifts included.' if US else 'Three pans, three lids, 4 gifts, covered for 75 years. 70% off.')
    b = HEADW(meta_w('wn3-%s · Bezwaar prijs: de hele bon, 6-delige set' % mkt, M, 'Siraat', subj, alts, pre,
                     'slot W3 (dag 3 09:00 in de huidige flow; dag 5 als vervolg)', WHO % ('W3', who_m),
                     'W3 nu $0.50: zes bewijzen, labrapport krijgt meer links dan de sale, geen product. Bewijs zit al in BF-W3. Nieuw: prijs is het grootste bezwaar (enquête), dus de bon.'), subj[0], pre) + OPEN3()
    s6 = utm(URL['set6'], c, 'hero')
    b += glass_img(IM_TABLE_, s6, 'VIP Black Friday', 'What 70% off<br>actually gets you.', 'The 6-piece set, 4 gifts, 75 years of cover.', 460, 290, 34)
    b += pricebar('set6', US, '70% OFF', '#FFFFFF', '22px 20px 0 20px')
    b += hero_btn('Get my set at 70% off', utm(URL['set6'], c, 'cta1'), US, '#FFFFFF', '16px 30px 22px 30px')
    b += P("Benjamin here. Ask our customers what almost stopped them, and the most common answer is the price. Fair enough. So here is the whole receipt.", '#FFFFFF', '6px 40px 10px 40px')
    b += receipt_set6(US)
    b += P(("Three pans and three fitted lids, so under $100 a pan with its lid. And every piece is covered for 75 years." if US and PRICES_US else
            "Three pans and three fitted lids, 70% off. And every piece is covered for 75 years."), '#FFFFFF', '0 40px 14px 40px')
    b += P("Why can we cover it that long? There is no coating on it to wear off. A pure titanium cooking surface, tested by Light Labs for 31 PFAS compounds, every one below the detection limit.", '#FFFFFF', '0 40px 6px 40px')
    b += quote('R011', '#FFFFFF').replace('0 40px 18px 40px', '10px 40px 22px 40px')
    b += small_head('One pan, or the whole stove?', '#FFFFFF', '8px 24px 14px 24px')
    b += card('standard', 'The pan Siraat started with. Right for 2 to 4.', US, 'Get the Pan Pro', utm(URL['standard'], c, 'card-standard'))
    if US: b += card('set12', '3 pans, 3 pots, 6 lids, plus a free Pizza Steel.', US, 'Get the 12-piece set', utm(URL['set12'], c, 'card-set12'))
    b += pbtn('Get my set at 70% off', utm(URL['set6'], c, 'cta-end'), US, '14px 30px 24px 30px')
    b += P('Not sure which set fits your kitchen? Reply and our team will help.', '#FFFFFF', '0 40px 8px 40px') + sign()
    files['wn3-' + mkt] = b + small(SMALL) + TAIL

    # ======================= WN4 · Elke maat, 70% off (maat kiezen op wie je kookt) =======================
    c = 'wn4-' + mkt
    subj = ('Who are you cooking for?', 'Every size is 70% off')
    alts = (('8, 10, 11 or 12 inches?',) if US else ('20, 26, 28 or 30 cm?',)) + ('Pick your pan in 10 seconds', 'One, two, or a family?')
    pre = 'One, two, or a family? Pick your pan by that. Every size is 70% off, plus 4 gifts.'
    b = HEADW(meta_w('wn4-%s · Maat kiezen, alle maten met prijs en tag' % mkt, M, 'Siraat', subj, alts, pre,
                     'slot W4 (dag 6 09:00 in de huidige flow; dag 7 als vervolg)', WHO % ('W4', who_m),
                     'W4 nu $0.19 (US) en $0.10 (INT): goede maatkiezer, maar sale en prijs onzichtbaar ("In the Black Friday Sale"). Nieuw: prijs en 70% OFF per maat, aanbod boven de vouw.'), subj[0], pre) + OPEN3()
    b += glass_img(IM_RANGE, utm(SALE, c, 'hero'), 'VIP Black Friday', 'Every size,<br>70% off.', 'Pick it by who you cook for.', 460, 290, 34)
    b += hero_btn('Find my size at 70% off', utm(SALE, c, 'cta1'), US, '#FFFFFF', '20px 30px 22px 30px')
    b += P("Benjamin here. The easiest way to pick a pan is by who eats with you, not by what looks biggest.", '#FFFFFF', '4px 40px 18px 40px')
    b += card('mini', 'For one. Eggs, omelettes, a quick sauce.', US, 'Get the Mini', utm(URL['mini'], c, 'card-mini'))
    b += card('small', 'For two. Breakfast and sides.', US, 'Get the Small', utm(URL['small'], c, 'card-small'))
    b += card('standard', 'For 2 to 4. Our best seller, and the pan we started with.', US, 'Get the Standard', utm(URL['standard'], c, 'card-standard'), NAME_SIZED['standard'])
    b += card('large', 'For a family, or two steaks at once.', US, 'Get the Large', utm(URL['large'], c, 'card-large'), NAME_SIZED['large'])
    b += small_head('Or get three at once', '#FFFFFF', '14px 24px 14px 24px')
    b += card('set6', 'Mini, Small and Large, each with its own lid.', US, 'Get the 6-piece set', utm(URL['set6'], c, 'card-set6'))
    if US: b += card('set12', '3 pans, 3 pots, 6 lids, plus a free Pizza Steel.', US, 'Get the 12-piece set', utm(URL['set12'], c, 'card-set12'))
    b += giftline()
    b += revblock(['R169', 'R138'], CREAM, 'In their words', '6px 20px 24px 20px')
    b += pbtn('Find my size at 70% off', utm(SALE, c, 'cta-end'), US, '24px 30px 24px 30px')
    b += P('Still not sure? Reply with what you cook most and who for. Our team will tell you which size.', '#FFFFFF', '0 40px 8px 40px') + sign()
    files['wn4-' + mkt] = b + small(SMALL) + TAIL

    # ======================= WN5 · Laatste welkomstmail: waar ik zou beginnen, twee beloftes =======================
    c = 'wn5-' + mkt
    subj = ('My last welcome email (and 70% off)', 'Tammy is on her fourth pan')
    alts = ("Where I'd start, at 70% off", 'Ready to cook without coatings?', 'Three pans, two promises')
    pre = "Where I'd start, two promises, and up to 70% off with 4 gifts."
    b = HEADW(meta_w('wn5-%s · Laatste welkomstmail: drie startpunten, klantverhaal, twee beloftes' % mkt, M, 'Benjamin from Siraat', subj, alts, pre,
                     'slot W5 (dag 10 09:00 in de huidige flow; dag 9 als vervolg)', WHO % ('W5', who_m),
                     'W5 nu $0.07 (US) en $0.09 (INT): drie klantverhalen, geen product, sale onderaan. Nieuw: producten met prijs bovenaan, één verhaal, beloftes, echte laatste mail.'), subj[0], pre) + OPEN3()
    b += glass_img(IM_FAM, utm(SALE, c, 'hero'), 'VIP Black Friday', 'Where I&#39;d start.', 'Up to 70% off, plus 4 gifts with every order.', 460, 290, 34)
    b += hero_btn('Get my Black Friday price', utm(SALE, c, 'cta1'), US, '#FFFFFF', '20px 30px 22px 30px')
    b += P("Benjamin here. This is the last email in our welcome series, so I&#39;ll keep it to where I&#39;d start.", '#FFFFFF', '4px 40px 18px 40px')
    b += card('standard', 'Our best seller. The pan Siraat started with.', US, 'Get the Pan Pro', utm(URL['standard'], c, 'card-standard'))
    b += card('set6', 'Mini, Small and Large, each with its own lid.', US, 'Get the 6-piece set', utm(URL['set6'], c, 'card-set6'))
    b += card('deep', 'Higher sides for sauces and one-pan dinners.', US, 'Get the Deep Pan', utm(URL['deep'], c, 'card-deep'))
    if US: b += card('set12', '3 pans, 3 pots, 6 lids, plus a free Pizza Steel.', US, 'Get the 12-piece set', utm(URL['set12'], c, 'card-set12'))
    b += big_quote(HG['REVS']['R138'][0], 'Tammy &middot; Pan Pro &middot; Verified buyer', CREAM)
    b += promises()
    b += pbtn('Get my Black Friday price', utm(SALE, c, 'cta-end'), US, '24px 30px 24px 30px')
    b += P('Thanks for reading along. Reply any time and our team will help.', '#FFFFFF', '0 40px 8px 40px') + sign()
    b += ps('The Black Friday prices are for everyone, so you don&#39;t need a code.')
    files['wn5-' + mkt] = b + small(SMALL) + TAIL

# Floris 6 nov (regel: elk beeld klikbaar)
for k, v in files.items():
    assert '—' not in v and '–' not in v, (k, 'streepje')
    body = v.split('-->', 1)[1]
    plain = re.sub(r'<[^>]+>', ' ', body.replace('&nbsp;', ' ')).lower()
    m = NODATE.search(plain); assert not m, (k, 'einddatum', m and m.group(0))
    for bad in BAD: assert bad not in plain, (k, bad)
    assert 'BFCODE' not in body and 'HI10' not in body, (k, 'code')
    assert '#FFB800' not in body.split('{{HEADER}}')[0], (k, 'geel alleen op sale-tags')
    if '-int' in k:
        assert '$' not in body and not re.search(r'\{\{(PRICE|WAS|FROM|GIFTS|FRICTION)', body), (k, 'bedrag of US-macro in INT')
        assert 'set12' not in body and '12-piece' not in plain and 'thanksgiving' not in plain, (k, 'US-only')
    elif not PRICES_US:
        assert '$' not in body and not re.search(r'\{\{(PRICE|WAS|FROM)', body), (k, 'prijs')
    v = link_all(v)
    open(os.path.join(N, k + '.html'), 'w').write(v); print('geschreven', k, len(v))
