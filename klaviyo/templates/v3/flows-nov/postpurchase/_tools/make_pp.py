"""Post-purchase X3ySuU, drie nieuwe stappen (flowplan november, research/plannen/2026-11-flowplan.md), elk US en INT:
  pp-addon     +2 u na Placed Order   "Forgot the lid?"         upsell deksel, utensils, tweede maat (70% OFF-tag, geen bedragen)
  pp-complete  dag 3, 09:00           "Complete your kitchen"   cross-sell per aankoop: pannenkoper vs setkoper (Django op event.Items)
  pp-twopans   dag 21                 "Two pans, one dinner"    recept met Pan Pro + Deep Pan Pro, altijd geldig; sale-blok los weg te halen
Stijl en helpers: homestead-e5-e6/_tools/make_final.py (laadt make_e56.py en make_pl2.py). Geen bedragen, geen valuta, geel alleen op de tag.
Eerlijk: wat je nu toevoegt is een aparte order (zelfde doos beloven we niet). Concept 6 nov 2026, niets in Klaviyo.
Gebruik (vanuit /tmp): python3 -I make_pp.py, daarna render_pp.py <uitmap> en shot_pp.js <uitmap> <previewmap>."""
import os, re, csv
F = '/home/user/siraat-email-agent/klaviyo/templates/v3/campaigns/homestead-e5-e6/_tools/make_final.py'
src = open(F).read().split('\nfiles = {}\n')[0]
g = {'__file__': F, '__name__': 'finalhelpers'}; exec(compile(src, F, 'exec'), g); globals().update({k: v for k, v in g.items() if not k.startswith('__')})
HG = wide_card.__globals__
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = '/home/user/siraat-email-agent'

# ---------------------------------------------------------------- producten (catalogus 6 nov: alle hieronder ~70% off in US en EU)
PK.update({'lid': 'Regular_Hammered_Panttern_Pan_with_lid_02_e1b2d9bb-75a9-41ee-ae7a-f88f008157e1.jpg', 'utensils': 'Utensils05-V2_1.webp',
           'wok': 'WokHammedPan_3.webp', 'pizza': 'TitaniumHammeredPizzaSteel.webp', 'roast': 'Roastingpanwithrack.webp', 'crepe': 'Crepepan01.jpg'})
NAME.update({'lid': 'Stainless Steel Lid', 'utensils': 'Titanium Utensil Set', 'wok': 'Wok Pan Pro', 'pizza': 'Titanium Hammered Pizza Steel',
             'roast': 'Roasting Pan', 'crepe': 'Cr&ecirc;pe Pan Pro'})
URL.update({'lid': PRD + 'stainless-steel-lid', 'utensils': PRD + 'siraat-pure-titanium-utensils-bundle', 'wok': PRD + 'titanium-hammered-wok-pan-pro',
            'pizza': PRD + 'titanium-hammered-pizza-steel', 'roast': PRD + 'titanium-hammered-roasting-pan', 'crepe': PRD + 'titanium-hammered-crepe-pan-pro'})
# Nieuwe beelden (Higgsfield Nano Banana 2.1, 6 nov 2026, referentie: echte packshots Pan Pro Standard, Deep Pan, lid, utensils)
IM_FLAT = 'https://cdn.klaviyomail.com/company/TdtTzz/images/e9c89f6f-5deb-4fa0-a78d-a086028e6177.jpeg'
IM_STOVE = 'https://cdn.klaviyomail.com/company/TdtTzz/images/7c283dac-1ece-4826-b7d8-fa75413f4688.jpeg'
IM_TWO = 'https://cdn.klaviyomail.com/company/TdtTzz/images/d8be6234-2812-44cf-b381-e49dd0dbaf46.jpeg'
IM_CHICK = 'https://cdn.klaviyomail.com/company/TdtTzz/images/a18c1d4c-2e08-4207-a87c-b6791a01b779.jpeg'

# echte reviews, letterlijk (ingekort met ...), gecontroleerd tegen content/reviews/reviews.csv hieronder
REVS['R014'] = ("I purchased their titanium wok a few months ago and it performs exactly as expected.", 'Caliann')
_rv = {r['id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'content/reviews/reviews.csv')))}
for rid in ('R014', 'R138', 'R011', 'R562'):
    q = REVS[rid][0]; o = _rv[rid]['quote']; pos = 0
    assert _rv[rid]['stars'] == '5' and len(q) <= 120, rid
    for part in [p.strip() for p in q.split('...') if p.strip()]:
        j = o.find(part, pos); assert j >= 0, (rid, part); pos = j + len(part)

# ---------------------------------------------------------------- Django op de bestelling (event.Items van Placed Order)
SETQ = "'pan set' in s or 'cookware set' in s or 'lids' in s or 'everything' in s or 'edition' in s or 'duo' in s"
def W(inner): return "{% with s=event.Items|join:','|lower %}" + inner + "{% endwith %}"
def IF(cond, a, b): return '{%% if %s %%}%s{%% else %%}%s{%% endif %%}' % (cond, a, b)

def OPEN_PLAIN(bg='#FFFFFF'):  # zonder BF-topbalk (mail 3 moet na 30 nov ook kloppen), wel de vaste header
    return '<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:%s;" bgcolor="%s">\n\n{{HEADER}}\n' % (bg, bg)
def HEADP(meta_, subj, pre):
    return head(meta_, subj, pre).replace('ROASTING PAN INT · NEW IN STOCK + BLACK FRIDAY SPECIAL (concept 1 nov 2026, niet in Klaviyo, niets live).',
                                          'POST-PURCHASE X3ySuU · NIEUWE STAPPEN NOVEMBER 2026 (concept 6 nov 2026, niet in Klaviyo, niets live).')
def plain_card(k, line, label, link):
    """Productkaart zonder prijs of tag (mail 3, altijd geldig)."""
    i = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td width="106" valign="top" style="padding:0 14px 0 0;"><a href="%s"><img src="%s" width="92" alt="Siraat %s" style="display:block;width:92px;height:92px;border-radius:8px;border:0;"></a></td>'
         '<td valign="top"><div style="font-family:%s;font-size:17px;line-height:22px;font-weight:600;color:%s;"><a href="%s" style="color:%s;text-decoration:none;">%s</a></div>%s%s</td></tr></table>') % (
        link, SQ(PK[k]), re.sub('&[^;]+;', 'e', NAME[k]), FF, INK, link, INK, NAME[k], txt(line, 14, 20, '#6E6A64', 400, 'padding-top:4px;'), sbtn(label, link))
    return row('#FFFFFF', '0 20px 12px 20px', boxed(i, HAIR, '#FFFFFF', '14px'), 'left', 'padx')
def thanks(us):
    h = '<table role="presentation" align="center" style="margin:0 auto;" cellpadding="0" cellspacing="0" border="0"><tr><td valign="middle" style="padding-right:8px;"><img src="{{SHARED}}/icon-check.png" width="22" alt="" style="display:block;width:22px;height:auto;border:0;"></td><td valign="middle">%s</td></tr></table>' % txt('ORDER CONFIRMED', 12, 16, INK, 700, 'letter-spacing:2px;')
    h += serif("Thanks for your order, {{ first_name|default:'there' }}.", 34, 38, INK, 'h1b', True, 'text-align:center;padding-top:10px;')
    h += txt('The confirmation with every detail is already in your inbox.', 15, 22, GREY, 500, 'text-align:center;padding-top:8px;')
    return row(PACK, '24px 24px 22px 24px', h, 'center')
def rule_line(t, bg='#FFFFFF'): return row(bg, '2px 30px 24px 30px', txt(t, 13, 19, GREY, 500, 'text-align:center;'), 'center')
def sub(t, bg='#FFFFFF', pad='26px 24px 14px 24px'): return row(bg, pad, serif(t, 30, 34, INK, 'h1s', True, 'text-align:center;'), 'center')

def recipe2(us):
    """Receptkaart in E5-stijl: ingrediënten per pan, genummerde stappen in volgorde van de klok, timingblok, eerlijke noot."""
    cm = (lambda a, b: a) if us else (lambda a, b: b)
    chick = ['6 boneless, skin-on chicken thighs', 'salt and black pepper', '1 teaspoon olive oil', '1 lemon, halved']
    orzo = ['1 tablespoon butter', '2 garlic cloves, sliced', cm('1 1/2 cups orzo', '300 g orzo'), cm('4 cups hot chicken stock', '1 litre hot chicken stock'),
            '2 big handfuls of baby spinach', cm('1/2 cup grated parmesan', '40 g grated parmesan'), 'zest and juice of 1 lemon']
    steps = ['Pat the thighs dry and salt both sides. Dry skin is crisp skin.',
             '<b>Pan Pro</b> on medium for 2 to 3 minutes. Flick in a drop of water. When it balls up and glides, add the oil.',
             'Thighs in, skin side down. Leave them alone for 12 minutes. Cold metal grabs your food, hot metal lets it go.',
             '<b>Deep Pan Pro</b> on medium, 5 minutes after the chicken went in: butter and garlic for a minute, then the orzo. Stir until it smells toasty.',
             'Pour in all the hot stock. Simmer 10 minutes, stirring every minute or so, until the orzo is tender and creamy.',
             'Flip the chicken. Lemon halves in next to it, cut side down. 6 more minutes, until cooked through (%s inside).' % cm('165&deg;F', '74&deg;C'),
             'Spinach, parmesan, zest and lemon juice into the orzo. Stir until the spinach wilts. Chicken on top, seared lemon squeezed over.']
    i = txt('Serves 4 &middot; 40 minutes', 14, 20, GREY, 600)
    i += eyebrow('For the chicken &middot; Pan Pro', INK, 'padding:16px 0 8px 0;') + bullets(chick)
    i += eyebrow('For the orzo &middot; Deep Pan Pro', INK, 'padding:10px 0 8px 0;') + bullets(orzo)
    i += eyebrow('Method', INK, 'padding:10px 0 10px 0;') + numbered(steps)
    i += '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%s" style="background-color:%s;border-radius:8px;margin-top:4px;"><tr><td style="padding:14px 16px;">%s</td></tr></table>' % (
        CREAM, CREAM, txt('<b>The timing:</b> chicken first, orzo 5 minutes later. Both finish within a minute of each other, and both pans go in the dishwasher.', 15, 23, INK))
    i += txt("One honest note: if the skin sticks when you try to lift it, it isn't ready. Give it two more minutes and it lets go on its own.", 15, 23, '#4A4A4A', 400, 'padding-top:14px;')
    return row('#FFFFFF', '6px 20px 0 20px', boxed(i, HAIR, '#FFFFFF', '20px 18px 18px 18px'), 'left', 'padx')

BAD = ('next batch', 'reserve', 'arriving', 'next shipment', 'purifier', 'lifetime', 'for life', 'free filter', 'scratch-proof', 'while supplies last',
       'same box', 'same package', 'same shipment', 'together with your order', 'combined', 'risk-free', 'money-back', 'free returns', 'VRAAG FLORIS')
files = {}
for mkt in ('us', 'int'):
    US = mkt == 'us'; M = mkt.upper()
    FLOW = 'Flow X3ySuU (Placed Order RSNxYV), %s; filters zoals de bestaande stappen ($value > 0); smart sending aan' % ('US-tak' if US else 'INT-tak')
    END = 'Monday, November 30' if US else 'Monday 30 November'
    SEP = ('Ships free from the US as its own order. 30-day returns. 100,000+ happy customers.' if US else
           'Ships free, duties paid, as its own order. 30-day returns. 100,000+ happy customers.')
    size = (lambda a, b: a) if US else (lambda a, b: b)

    # ================= 1 · +2 uur: upsell =================
    c = 'pp-addon-' + mkt
    subj = ('Forgot the lid?', 'Thanks for your order. One quick thing.')
    pre = 'The lid, the tools, a second size. Still 70% off, and it ships free.'
    b = HEADP(meta4('pp-addon-%s · +2 u na bestelling, upsell (deksel, utensils, tweede maat)' % mkt, M, 'Siraat', subj, pre, 'Placed Order + 2 uur (flowstap 2 in X3ySuU)', FLOW,
                    'Flowplan nov: upsell vlak na de order tegen de Black Friday-prijs. Eerlijk: toevoegen = aparte order, gratis verzonden; geen belofte over dezelfde doos.'), subj[0], pre) + OPEN3()
    b += thanks(US)
    b += glass_img(IM_FLAT, utm(SALE, c, 'hero'), 'Forgot something?', 'The lid, the tools, a second size.', 'Same 70% off. Ships free on its own.', 440, 290, 32)
    b += P("Benjamin here. If you meant to add something, this is the easy moment. The Black Friday price still applies, and anything you add ships free as its own order. The order you just placed doesn't change.",
           '#FFFFFF', '24px 40px 14px 40px')
    lid = wide_card('lid', 'Pick the size of your pan. Keeps the heat in to steam, simmer or melt the cheese.', US, '70% OFF', 'Add the lid', utm(URL['lid'], c, 'card-lid'))
    deep = wide_card('deep', 'Higher sides for sauces, pasta and one-pan dinners.', US, '70% OFF', 'Add the Deep Pan Pro', utm(URL['deep'], c, 'card-deep'))
    wok = wide_card('wok', 'Deep and wide, to toss without spilling.', US, '70% OFF', 'Add the Wok Pan Pro', utm(URL['wok'], c, 'card-wok'))
    ute = wide_card('utensils', 'Spatula, turner, ladle, skimmer. All titanium, and safe on your pan.', US, '70% OFF', 'Add the utensils', utm(URL['utensils'], c, 'card-utensils'))
    roast = wide_card('roast', 'With its fitted V-rack, for the big roast.', US, '70% OFF', 'Add the Roasting Pan', utm(URL['roast'], c, 'card-roast'))
    large = wide_card('large', size('12 inch. One size up, for family portions.', '30 cm. One size up, for family portions.'), US, '70% OFF', 'Add the Pan Pro Large', utm(URL['large'], c, 'card-large'))
    std = wide_card('standard', size('11 inch. The everyday size, for eggs and two portions.', '28 cm. The everyday size, for eggs and two portions.'), US, '70% OFF', 'Add the Pan Pro Standard', utm(URL['standard'], c, 'card-standard'))
    b += W(IF("'lid' in s or " + SETQ, IF("'deep' in s", wok, deep), lid) + IF("'utensil' in s", roast, ute) + IF("'large' in s or " + SETQ, std, large))
    b += rule_line(SEP)
    b += quote('R138')
    b += P('The sale ends %s. After that, regular prices apply.' % END, '#FFFFFF', '0 40px 6px 40px') + sign()
    b += small('Added items ship as a separate order. Black Friday prices until %s.' % ('November 30' if US else '30 November'))
    files['pp-addon-' + mkt] = b + TAIL

    # ================= 2 · dag 3: complete your kitchen =================
    c = 'pp-complete-' + mkt
    subj = ('Complete your kitchen', "What's missing from your stove?")
    pre = 'Picked for what you just ordered. 70%% off until %s.' % ('November 30' if US else '30 November')
    b = HEADP(meta4('pp-complete-%s · dag 3 09:00, cross-sell per aankoop' % mkt, M, 'Siraat', subj, pre, 'Placed Order + 3 dagen, 09:00 lokale tijd (stap na de upsell)', FLOW + '; alleen tot 30 nov 23:59 (daarna stap overslaan of uitzetten)',
                    'Flowplan nov: cross-sell op wat ze kochten. Pannenkoper: Deep Pan, Wok, deksel. Setkoper: utensils, Pizza Steel, Roasting Pan. Nooit iets wat al in de order zit.'), subj[0], pre) + OPEN3()
    b += glass_img(IM_STOVE, utm(SALE, c, 'hero'), 'Day three', 'Complete your kitchen.', 'Picked for what you ordered.', 440, 290, 34)
    b += P(W(IF(SETQ, "Benjamin here. Your set covers the stove. These three cover the rest: the tools, the oven and pizza night.",
                "Benjamin here. Your pan does the everyday work. These three handle what it can't: one-pan dinners, a fast stir-fry, and anything that needs a lid.")),
           '#FFFFFF', '24px 40px 10px 40px')
    b += row('#FFFFFF', '0 20px 16px 20px', '<div style="text-align:center;">%s</div>' % badge('70%% OFF UNTIL %s' % ('NOV 30' if US else '30 NOV'), 12), 'center', 'padx')
    deep = wide_card('deep', 'Higher sides for sauces, pasta and one-pan dinners.', US, '70% OFF', 'Get the Deep Pan Pro', utm(URL['deep'], c, 'card-deep'))
    large = wide_card('large', size('12 inch. One size up, for family portions.', '30 cm. One size up, for family portions.'), US, '70% OFF', 'Get the Pan Pro Large', utm(URL['large'], c, 'card-large'))
    wok = wide_card('wok', 'Deep and wide, to toss a stir-fry without spilling.', US, '70% OFF', 'Get the Wok Pan Pro', utm(URL['wok'], c, 'card-wok'))
    crepe = wide_card('crepe', 'Flat and wide: cr&ecirc;pes, pancakes, tortillas.', US, '70% OFF', 'Get the Cr&ecirc;pe Pan', utm(URL['crepe'], c, 'card-crepe'))
    lid = wide_card('lid', 'Keeps the heat in. Steam, simmer, melt the cheese.', US, '70% OFF', 'Get the lid', utm(URL['lid'], c, 'card-lid'))
    ute = wide_card('utensils', 'Spatula, turner, ladle, skimmer. All titanium.', US, '70% OFF', 'Get the utensils', utm(URL['utensils'], c, 'card-utensils'))
    pizza = wide_card('pizza', 'Hammered titanium for the oven. Crisp base, pizza night at home.', US, '70% OFF', 'Get the Pizza Steel', utm(URL['pizza'], c, 'card-pizza'))
    roast = wide_card('roast', 'With its fitted V-rack, for the roast your stove has no room for.', US, '70% OFF', 'Get the Roasting Pan', utm(URL['roast'], c, 'card-roast'))
    setb = IF("'utensil' in s", wok, ute) + IF("'pizza' in s or '12-pcs' in s", crepe, pizza) + IF("'roast' in s", deep, roast)
    panb = IF("'deep' in s", large, deep) + IF("'wok' in s", crepe, wok) + IF("'lid' in s", ute, lid)
    b += W(IF(SETQ, setb, panb))
    b += rule_line(FRIC(US))
    b += W(IF(SETQ, quote('R011'), quote('R014')))
    b += icons_row([('icon-no-coating.png', 'No coatings'), ('icon-pfas-tested.png', 'Tested PFAS-free'), ('icon-dishwasher-safe.png', 'Dishwasher safe')], '#FFFFFF')
    b += bf_short(US, c, 'band') + gifts(US)
    b += closing('Happy cooking,').replace('6px 40px 4px 40px', '22px 40px 4px 40px') + sign()
    b += small('Every new order is its own shipment, shipped free. Black Friday prices until %s, then regular prices.' % ('November 30' if US else '30 November'))
    files['pp-complete-' + mkt] = b + TAIL

    # ================= 3 · dag 21: two pans, one dinner =================
    c = 'pp-twopans-' + mkt
    subj = ('Two pans, one dinner', 'Crispy chicken and lemon orzo, done together')
    pre = 'The Pan Pro crisps, the Deep Pan Pro simmers. 40 minutes.'
    b = HEADP(meta4('pp-twopans-%s · dag 21, recept met twee pannen' % mkt, M, 'Siraat', subj, pre, 'Placed Order + 21 dagen, 09:00 lokale tijd', FLOW,
                    'Flowplan nov: recept dat twee Siraat-producten nodig heeft. Werkt altijd; het blok tussen SALE-BLOK START en EIND gaat eruit na 30 nov.'), subj[0], pre) + OPEN_PLAIN()
    b += glass_img(IM_TWO, utm(URL['deep'], c, 'hero'), 'Two pans, one dinner', 'Crispy chicken, lemon orzo.', 'Pan Pro + Deep Pan Pro &middot; 40 minutes', 460, 290, 34)
    b += P("Benjamin here. By now you've probably done eggs, maybe a steak. This one uses two pans at once. The Pan Pro crisps the chicken while the Deep Pan Pro turns orzo creamy, and they finish within a minute of each other.",
           '#FFFFFF', '24px 40px 18px 40px')
    b += pull('Leave the chicken alone. When the skin is ready, it lets go on its own.')
    b += gap('#FFFFFF', 20) + glass_img(IM_CHICK, utm(URL['standard'], c, 'img-chicken'), 'The recipe', 'Chicken thighs, skin side down', 'Then the orzo goes on next to it')
    b += recipe2(US)
    b += P('Why the Deep Pan Pro for the orzo: the higher sides let the stock simmer without spitting over the edge, and there is room to stir in the spinach.', '#FFFFFF', '20px 40px 16px 40px')
    b += pbtn('Shop the Deep Pan Pro', utm(URL['deep'], c, 'cta-deep'), US, '0 30px 24px 30px')
    b += sub('Missing one of the two?')
    b += plain_card('standard', size('11 inch. The everyday size, room for 6 thighs.', '28 cm. The everyday size, room for 6 thighs.'), 'Shop the Pan Pro', utm(URL['standard'], c, 'card-standard'))
    b += plain_card('deep', 'Higher sides for orzo, sauces and one-pan dinners.', 'Shop the Deep Pan', utm(URL['deep'], c, 'card-deep'))
    b += quote('R562')
    b += icons_row([('icon-no-coating.png', 'No coatings'), ('icon-pfas-tested.png', 'Tested PFAS-free'), ('icon-dishwasher-safe.png', 'Dishwasher safe')])
    b += '<!-- SALE-BLOK START (weg na 30 nov 2026) -->\n' + bf_short(US, c, 'band') + '<!-- SALE-BLOK EIND -->\n'
    b += closing('Happy cooking,').replace('6px 40px 4px 40px', '22px 40px 4px 40px') + sign()
    b += ps('Made it? Reply with a photo of your two pans. A real person reads every email.')
    files['pp-twopans-' + mkt] = b + small('Both pans have the same pure titanium cooking surface, no coatings. Tested free from PFAS by Light Labs, report no. 25895.') + TAIL

for k, v in files.items():
    assert '—' not in v and '–' not in v, (k, 'streepje')
    body = v.split('-->', 1)[1]
    assert '$' not in body and not re.search(r'\{\{(PRICE|WAS|FROM|GIFTS)', body), (k, 'prijs')
    assert 'FFB800' not in re.sub(r'<span style="display:inline-block;background-color:#FFB800[^>]*>[^<]*</span>', '', body), (k, 'geel buiten tag')
    plain = re.sub(r'<[^>]+>', ' ', body).lower()
    for bad in BAD: assert bad.lower() not in plain, (k, bad)
    if 'twopans' in k: assert '70%' not in body.split('SALE-BLOK START')[0] and 'bf-topbar' not in body, (k, 'sale buiten blok')
    v = v.replace('Free shipping, from the US.', 'Free shipping from the US.')  # bf_short (make_final) zet een komma in de US-regel
    open(os.path.join(N, k + '.html'), 'w').write(v); print('geschreven', k, len(v))
