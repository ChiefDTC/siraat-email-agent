"""December-reeks (flowplan nov 2026, sectie "Na 30 nov"): drie mails voor wie zich in november inschreef en niet kocht.
1 dec: How to cook on titanium (uitleg in stappen), 3 dec: Why Benjamin made the Pan Pro (brief), 6 dec: 100,000 kitchens later (bewijs).
Geen Black Friday, geen sale-druk, geen bedragen, geen geel. Elk in US en INT (INT: geen valuta). Concept, niets live.
Hergebruikt helpers uit homestead-e5-e6/_tools/make_final.py (die laadt make_e56.py en make_pl2.py).
Gebruik (vanuit /tmp): python3 -I make_dec.py, daarna render_dec.py <uitmap> en shot_dec.js <uitmap> <previewmap>."""
import os, re
F = '/home/user/siraat-email-agent/klaviyo/templates/v3/campaigns/homestead-e5-e6/_tools/make_final.py'
src = open(F).read().split('\nBAD = ')[0]
g = {'__file__': F, '__name__': 'finalhelpers'}; exec(compile(src, F, 'exec'), g); globals().update({k: v for k, v in g.items() if not k.startswith('__')})
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HG = wide_card.__globals__  # namespace van make_e56/make_pl2: daar leven OPEN3/topbar

# ---------------------------------------------------------------- neutrale topbalk (geen VIP Black Friday)
TOPTXT = 'Pure titanium. No coatings. 75-year warranty.'
def topbar_dec():
    return ('{{BLOCK:bf-topbar text="<a href=\'https://siraatskitchen.com/pages/third-party-testing?utm_source=klaviyo&utm_medium=email&utm_campaign=dec-topbar\' '
            'style=\'color:#F8F7F2;text-decoration:none;\'>%s</a>" bg="#272727" color="#F8F7F2"}}\n{{HEADER}}\n') % TOPTXT
HG['topbar'] = topbar_dec

# ---------------------------------------------------------------- beelden
IM = {l.split()[0]: l.split()[1] for l in open(os.path.join(N, 'assets', 'klaviyo-urls.txt')) if l.strip()}
IM_DROP, IM_OIL, IM_KITCHEN, IM_SPAT = IM['dec-waterdrop'], IM['dec-oil'], IM['dec-kitchen'], IM['dec-spatula']
IM_FAMILY = C11(FAMILY)
IM_RANGE = CDN + 'P022-A_GasRange_2560w_q76.webp?width=1200&height=800&crop=center&format=pjpg'
PANS = 'https://siraatskitchen.com/collections/pans'
TEST = 'https://siraatskitchen.com/pages/third-party-testing'
WARR = 'https://siraatskitchen.com/pages/warranty'

REVS['R112'] = ('The food does not stick, cooks perfectly and evenly... Excellent product and excellent service.', 'Fabio P.')
REVS['HS1'] = ("Buy it because it's safe, it's the only pan you will need in your kitchen, life long.", 'Siraat customer')  # Floris 5 nov
REVS['R220'] = ("I've been cooking for well over 60 years... This Siraat pan has been the absolute best I've ever used.", 'Carole')

def meta5(id_, mkt, sender, subj, pre, when, why):
    who = ('Nieuw segment: aangemeld 1 t/m 30 nov 2026, nooit besteld (Placed Order alltime = 0), %s, engaged 30 dagen; '
           'uitsluiten: in een afhaakflow (checkout, cart, browse) in de laatste 24 uur; smart sending aan. Stap uit bij Placed Order.') % (
        'US + geen land' if mkt == 'US' else 'INT (land bekend, niet US)')
    return ('ID: %s\nMARKT: %s\nSENDER: %s\nSUBJECT A: %s\nSUBJECT B: %s\nSUBJECT (overige 3): %s\nPREVIEW: %s\nWANNEER: %s\nWIE: %s\nWAAROM: %s') % (
        id_, mkt, sender, subj[0], subj[1], ' | '.join(subj[2:]), pre, when, who, why)
def HEADD(meta_, subj, pre):
    return head(meta_, subj, pre).replace('ROASTING PAN INT · NEW IN STOCK + BLACK FRIDAY SPECIAL (concept 1 nov 2026, niet in Klaviyo, niets live).',
                                          'DECEMBER-REEKS · NIET-KOPERS NOVEMBER (concept 6 nov 2026, niet in Klaviyo, niets live).')

# ---------------------------------------------------------------- bouwstenen zonder prijs en zonder geel
def stepcard(n, title, body, image, alt, link, note=''):
    """Stap: beeld bovenaan, nummer en kop, korte tekst. Volle breedte op 375 en 600 px."""
    num = '<div style="width:30px;height:30px;border-radius:15px;background-color:%s;font-family:%s;font-size:14px;line-height:30px;font-weight:800;color:#FFFFFF;text-align:center;">%d</div>' % (INK, FF, n)
    hd = '<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td valign="middle" style="padding-right:12px;">%s</td><td valign="middle">%s</td></tr></table>' % (num, serif(title, 28, 32, INK, 'ptitle', True))
    i = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid %s;border-radius:10px;">' % HAIR
    if image: i += '<tr><td style="padding:0;border-radius:10px 10px 0 0;overflow:hidden;">%s</td></tr>' % img(image, alt, link, 558, 0).replace('style="display:block;', 'style="display:block;border-radius:10px 10px 0 0;')
    i += '<tr><td style="padding:18px 18px 18px 18px;">%s%s%s</td></tr></table>' % (hd, txt(body, 16, 25, '#2E2E2E', 400, 'padding-top:10px;'),
                                                                                txt(note, 14, 21, GREY, 500, 'padding-top:10px;') if note else '')
    return row('#FFFFFF', '0 20px 14px 20px', i, 'left', 'padx')
def pcard(k, line, label, link):
    """Productkaart zonder prijs (geen sale): packshot, naam, regel, knop."""
    return ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid %s;border-radius:10px;">'
            '<tr><td style="padding:0;border-radius:10px 10px 0 0;overflow:hidden;">%s</td></tr><tr><td style="padding:12px 12px 14px 12px;">%s%s%s</td></tr></table>') % (
        HAIR, img(SQ(PK[k]), 'Siraat ' + NAME[k], link, 270, 0),
        '<div style="font-family:%s;font-size:16px;line-height:20px;font-weight:600;color:%s;"><a href="%s" style="color:%s;text-decoration:none;">%s</a></div>' % (FF, INK, link, INK, NAME[k]),
        txt(line, 13, 18, '#6E6A64', 400, 'padding-top:4px;'), sbtn(label, link, True))
def wcard(k, line, label, link, bg='#FFFFFF', boxbg='#FFFFFF'):
    """Brede productkaart zonder prijs (packshot links)."""
    i = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td width="132" class="thumb" valign="top" style="padding:0 14px 0 0;"><a href="%s"><img src="%s" width="118" alt="Siraat %s" style="display:block;width:100%%;max-width:118px;height:auto;border-radius:8px;border:0;"></a></td>'
         '<td valign="top">%s%s%s</td></tr></table>') % (
        link, SQ(PK[k]), NAME[k], '<div style="font-family:%s;font-size:17px;line-height:22px;font-weight:600;color:%s;"><a href="%s" style="color:%s;text-decoration:none;">%s</a></div>' % (FF, INK, link, INK, NAME[k]),
        txt(line, 14, 20, '#6E6A64', 400, 'padding-top:4px;'), sbtn(label, link))
    return row(bg, '0 20px 14px 20px', boxed(i, HAIR, boxbg, '14px'), 'left', 'padx')
def proofbox(icon, title, body, link=None, linktxt=''):
    lk = ('<div style="padding-top:8px;"><a href="%s" style="font-family:%s;font-size:14px;line-height:20px;font-weight:700;color:%s;text-decoration:underline;">%s</a></div>' % (link, FF, INK, linktxt)) if link else ''
    i = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td width="58" valign="top" style="padding:2px 14px 0 0;"><img src="{{SHARED}}/%s" width="44" alt="" style="display:block;width:44px;height:auto;border:0;"></td>'
         '<td valign="top">%s%s%s</td></tr></table>') % (icon, txt(title, 17, 23, INK, 700), txt(body, 15, 23, '#4A4A4A', 400, 'padding-top:4px;'), lk)
    return '<div style="height:10px;line-height:10px;font-size:0;">&nbsp;</div>' + boxed(i, HAIR, '#FFFFFF', '16px 16px')
def bigquote(k, bg=CREAM):
    q, n = REVS[k]
    h = txt('&#9733;&#9733;&#9733;&#9733;&#9733;', 16, 18, GOLD, 400, 'letter-spacing:3px;text-align:center;')
    h += serif('&ldquo;%s&rdquo;' % q, 28, 36, INK, 'h1s', True, 'text-align:center;padding-top:12px;')
    h += txt(n, 13, 18, '#8A847A', 600, 'text-align:center;padding-top:12px;letter-spacing:1px;text-transform:uppercase;')
    return row(bg, '30px 30px 28px 30px', h, 'center', 'pad')
def btn(label, url, us, pad='6px 30px 28px 30px', bg='#FFFFFF'): return pbtn(label, url, us, pad, bg)
def line_center(t, bg='#FFFFFF', pad='0 30px 22px 30px', size=14): return row(bg, pad, txt(t, size, 21, GREY, 500, 'text-align:center;'), 'center')

files = {}
for mkt in ('us', 'int'):
    US = mkt == 'us'; M = mkt.upper()
    D24 = 'December 20, 2024' if US else '20 December 2024'

    # =============================== DEC 1 · How to cook on titanium ===============================
    c = 'dec1-' + mkt; std = utm(URL['standard'], c, 'card'); pans = utm(PANS, c, 'cta1')
    subj = ('How to cook on titanium', 'The one mistake that makes titanium stick', '2 to 3 minutes on medium',
            'Ever seen a drop of water dance?', '"The egg released completely"')
    pre = 'Medium heat, one drop of water, then oil. Nothing sticks when the heat is right.'
    b = HEADD(meta5('dec1-%s · Uitleg titanium in vier stappen' % mkt, M, 'Siraat', subj, pre, 'di 1 dec 2026, 09:00 lokale tijd',
                    'Flowplan "Na 30 nov" mail 1. Grootste twijfel na prijs: werkt titanium echt (15%). Uitleg plus bewijs, geen aanbod. Test A/B = onderwerp (uitleg tegen nieuwsgierigheid).'),
              subj[0], pre) + OPEN3()
    b += glass_img(IM_DROP, utm(PANS, c, 'hero'), 'How to cook on titanium', 'Watch the water dance.', 'Nothing sticks when the heat is right.', 440, 290, 36)
    b += P("Benjamin here. The question I get most from people who haven't bought yet: does titanium really work, or does everything stick?", '#FFFFFF', '26px 40px 14px 40px')
    b += P("It works. It just asks for one thing a coated pan never did. Heat first, food second. Four steps, and the first time takes about three minutes longer than you're used to.", '#FFFFFF', '0 40px 22px 40px')
    b += btn('Find my first titanium pan', pans, US, '0 30px 26px 30px')
    b += stepcard(1, 'Heat it on medium', 'Put the empty pan on medium heat and give it 2 to 3 minutes. Not high. Titanium spreads the heat, it just needs a moment to get there.', None, '', None)
    b += stepcard(2, 'The water drop test', 'Flick in a few drops of water, like the photo at the top. If they hiss and vanish, wait a little longer. When they pull into round beads and glide across the surface, the pan is ready.', None, '', None)
    b += stepcard(3, 'Then the oil', 'About a teaspoon of oil or a knob of butter. Tilt the pan so it runs into the hammered pattern.',
                  IM_OIL, 'A teaspoon of olive oil poured into a hot Siraat hammered titanium pan', utm(PANS, c, 'step3'))
    b += stepcard(4, "Lay it down. Don't move it.", "Put the food in and leave it alone. Cold metal grabs your food, hot metal lets it go. When it's ready to turn, it lets go by itself.",
                  IM_EGG, 'A fried egg sliding out of a Siraat Pan Pro Standard onto toast', utm(URL['standard'], c, 'step4'),
                  "One honest note: if something sticks, the pan wasn't hot yet. Give the next one another minute.")
    b += pull('Nothing sticks when<br>the heat is right.')
    b += heading('After dinner', '#FFFFFF', '26px 24px 14px 24px')
    b += row('#FFFFFF', '0 20px 18px 20px', img(IM_SPAT, 'A metal spatula lifting a seared salmon fillet out of a Siraat hammered titanium pan', utm(PANS, c, 'clean-img'), 560, 10), 'center', 'padx')
    b += P("There's no coating on it, so there's nothing to protect. Metal spatulas are fine. Warm water and a sponge, and you clean up in under a minute. Or put it straight in the dishwasher.", '#FFFFFF', '0 40px 16px 40px')
    b += icons_row([('icon-metal-utensil-safe.png', 'Metal utensil safe'), ('icon-dishwasher-safe.png', 'Dishwasher safe'), ('icon-no-coating.png', 'No coatings')], '#FFFFFF')
    b += revblock(['R169', 'R112'], CREAM, 'From their kitchens')
    b += gap('#FFFFFF', 24)
    b += wcard('standard', 'The pan Siraat started with. The everyday size for eggs, steak and weeknights.', 'Shop the Pan Pro', std)
    b += btn('Find my first titanium pan', utm(PANS, c, 'cta-end'), US, '10px 30px 26px 30px')
    b += closing('Happy cooking,') + sign()
    b += ps('Tested free from PFAS by Light Labs, report no. 25895. 31 compounds, every one below the detection limit. <a href="%s" style="color:#272727;">Read the report</a>.' % utm(TEST, c, 'ps'))
    files['dec1-' + mkt] = b + TAIL

    # =============================== DEC 3 · Why Benjamin made the Pan Pro ===============================
    c = 'dec3-' + mkt; std = utm(URL['standard'], c, 'card')
    subj = ('Why I made the Pan Pro', D24, 'Why the first pan had no coating', 'Why would anyone make a pan with nothing on it?', '"I am on my 4th pan from Siraat"')
    pre = 'The pan Siraat started with, and the one thing I refused to put on it.'
    b = HEADD(meta5('dec3-%s · Brief van Benjamin: het verhaal van de Pan Pro' % mkt, M, 'Benjamin from Siraat', subj, pre, 'do 3 dec 2026, 09:00 lokale tijd',
                    'Flowplan "Na 30 nov" mail 2. Founder-notes klikken het best (PLAYBOOK 1). Verhaal en waarom, geen aanbod. Test A/B = onderwerp (ik-vorm tegen datum).'),
              subj[0], pre) + OPEN3()
    b += P("Hi, it's Benjamin.", '#FFFFFF', '34px 40px 14px 40px')
    b += P("You joined us in November, and there's no sale in this email. Just the story of the pan we started with, because it explains everything else we make.")
    b += P("The Pan Pro is the pan Siraat started with. The question behind it was simple: could you cook on pure titanium, with nothing coated on top of it?")
    b += row('#FFFFFF', '4px 20px 22px 20px', img(IM_KITCHEN, 'A quiet home kitchen at night with two eggs frying in a Siraat hammered titanium pan on the stove', utm(URL['standard'], c, 'img'), 560, 10), 'center', 'padx')
    b += P('The Pan Pro was the answer. A pure titanium cooking surface, a hammered pattern, no coatings of any kind. We shipped the first orders on %s. Others started hammering titanium after that. This was the first one.' % D24)
    b += P("Why no coating? Because the coating is the part that wears. Once it starts to go, the pan is done. Take it away and there's nothing on the pan to wear off. That's also why we can put a 75-year warranty on it.")
    b += P('And because people ask: Light Labs, an ISO/IEC 17025-accredited lab, tested the Pan Pro for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895, and <a href="%s" style="color:#272727;">you can read it yourself</a>.' % utm(TEST, c, 'report'))
    b += P('Since then, more than 100,000 people have bought from us, in a little over a year. Some came back for more. Like Tammy:')
    b += quote('R138')
    b += P("If you're still deciding, start where we did. The Standard is the everyday size, the one for eggs, a steak or a weeknight pasta.", '#FFFFFF', '4px 40px 18px 40px')
    b += wcard('standard', 'The original hammered titanium pan. Pure titanium cooking surface, no coatings.', 'See the Pan Pro', std)
    b += btn('Start with the original pan', utm(URL['standard'], c, 'cta1'), US, '8px 30px 26px 30px')
    b += P('Questions about sizes, induction or anything else? Reply and our team will help.')
    b += sign()
    b += ps("30-day returns, counted from the day it arrives. And after that, it's covered for 75 years.")
    files['dec3-' + mkt] = b + TAIL

    # =============================== DEC 6 · 100,000 kitchens later ===============================
    c = 'dec6-' + mkt
    subj = ('100,000 kitchens later', '"The only pan you will need"', 'What 100,000 kitchens found out', 'Still deciding on titanium?', 'Report no. 25895')
    pre = 'In their words. Plus the lab report, the 75-year warranty and 30 days to decide.'
    b = HEADD(meta5('dec6-%s · Bewijs: reviews, labrapport, garantie, retour' % mkt, M, 'Siraat', subj, pre, 'zo 6 dec 2026, 09:00 lokale tijd',
                    'Flowplan "Na 30 nov" mail 3. Sociaal bewijs plus autoriteit en risico-omkering, geen aanbod. Test A/B = onderwerp (getal tegen klantcitaat).'),
              subj[0], pre) + OPEN3()
    b += glass_img(IM_FAMILY, utm(PANS, c, 'hero'), 'In their words', '100,000 kitchens later.', 'What people say once the pan is theirs.', 440, 290, 36)
    b += P("Benjamin here. You've heard enough from me. This one is what other people say, and the three things we put in writing.", '#FFFFFF', '26px 40px 6px 40px')
    b += bigquote('HS1', '#FFFFFF')
    b += revblock(['R138', 'R583', 'R220'], CREAM, 'From their kitchens')
    b += btn('Find my pan', utm(PANS, c, 'cta1'), US, '24px 30px 26px 30px')
    h = serif('Three things in writing', 32, 36, INK, 'h1s', True, 'text-align:center;padding-bottom:6px;')
    h += proofbox('icon-pfas-tested.png', 'The lab report', 'Light Labs, an ISO/IEC 17025-accredited lab, tested for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895.', utm(TEST, c, 'proof-report'), 'Read it yourself')
    h += proofbox('icon-warranty-75-year.png', 'A 75-year warranty', 'A dent, a warped base, a loose handle or rivet, a lid that no longer fits: we take care of it. There is no coating on it to wear off, so we can promise that.', utm(WARR, c, 'proof-warranty'), 'How the warranty works')
    h += proofbox('icon-returns-30-day.png', '30 days to decide', 'Changed your mind? Send it back unused within 30 days of delivery for a full refund.')
    b += row('#FFFFFF', '10px 20px 10px 20px', h, 'left', 'padx')
    b += P('One customer sent us a photo, and that was it:', '#FFFFFF', '18px 40px 14px 40px') + quote('R240')
    b += heading('Where to start', CREAM, '30px 24px 18px 24px')
    cards = [pcard('standard', 'The original. The everyday size.', 'Shop the pan', utm(URL['standard'], c, 'grid-standard')),
             pcard('large', 'Room for the whole family.', 'Shop the pan', utm(URL['large'], c, 'grid-large')),
             pcard('deep', 'Higher sides for sauces and one-pan dinners.', 'Shop the pan', utm(URL['deep'], c, 'grid-deep')),
             pcard('set6', 'Three pans, each with its own lid.', 'Shop the set', utm(URL['set6'], c, 'grid-set6'))]
    b += grid(cards) + gap(CREAM, 14)
    b += btn('Find my pan', utm(PANS, c, 'cta-end'), US, '28px 30px 26px 30px')
    b += closing('Happy cooking,') + sign()
    files['dec6-' + mkt] = b + TAIL

BAD = ('next batch', 'reserve', 'arriving', 'next shipment', 'purifier', 'lifetime', 'for life', 'free filter', 'scratch-proof', 'while supplies last',
       'VRAAG FLORIS', 'black friday', '% off', 'sale ends', 'hurry', 'last chance', 'risk-free', 'money-back', 'free returns')
for k, v in files.items():
    assert '—' not in v and '–' not in v, (k, 'dash')
    body = v.split('-->', 1)[1]
    low = re.sub(r'<[^>]+>', ' ', body).lower()
    for bad in BAD: assert bad.lower() not in low, (k, bad)
    assert '$' not in body and not re.search(r'\{\{(PRICE|WAS|FROM|GIFTS)', body), (k, 'prijs')
    assert 'FFB800' not in body.upper(), (k, 'geel')
    if k.endswith('-int'): assert '{{FRICTION' not in body, k
    open(os.path.join(N, k + '.html'), 'w').write(v); print('geschreven', k, len(v))
