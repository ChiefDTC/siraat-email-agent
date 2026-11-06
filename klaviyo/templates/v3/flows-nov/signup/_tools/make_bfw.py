"""Flow Rn556d (aanmelding), na BF-W1 "You're just in time": BF-W2 (dag 1 10:00, brief van Benjamin + sets) en
BF-W3 (dag 2 09:00, twijfels wegnemen, visueel zoals E5). Elk US en INT. Geen bedragen, alleen de gele sale-tag 70% OFF.
Hergebruikt de helpers uit homestead-e5-e6/_tools/make_final.py (die laadt make_e56.py en make_pl2.py). Concept, niets live.
Gebruik (vanuit /tmp): python3 -I make_bfw.py, daarna python3 -I render_bfw.py <uitmap> en node shot_bfw.js <uitmap> <previewmap>."""
import os, re, csv
F = '/home/user/siraat-email-agent/klaviyo/templates/v3/campaigns/homestead-e5-e6/_tools/make_final.py'
src = open(F).read().split('\nfiles = {}\n')[0]
g = {'__file__': F, '__name__': 'finalhelpers'}; exec(compile(src, F, 'exec'), g)
globals().update({k: v for k, v in g.items() if not k.startswith('__')})
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = '/home/user/siraat-email-agent'

# ---------------------------------------------------------------- beelden
# Nieuw (Higgsfield, Nano Banana 2.1 met packshot Pan Pro Standard als referentie, 6 nov 2026), in Klaviyo geüpload:
IM_EGGS = 'https://cdn.klaviyomail.com/company/TdtTzz/images/9425c219-f68a-48b0-944f-ecd163aebd80.jpeg'   # bfw2-eggs.jpg
IM_DROP = 'https://cdn.klaviyomail.com/company/TdtTzz/images/280d948c-0332-4e43-8b68-c27b82251184.jpeg'   # bfw3-waterdrop.jpg
IM_SPAT = 'https://cdn.klaviyomail.com/company/TdtTzz/images/7e09867e-b934-42f6-a08b-3ee984f6c8ee.jpeg'   # bfw3-spatula.jpg
LABS_PAGE = 'https://siraatskitchen.com/pages/third-party-testing'

# ---------------------------------------------------------------- reviews (letterlijk, gecontroleerd tegen reviews.csv hieronder)
HG['REVS'].update({
    'R025': ("I ordered one pan to try it out. I'm so glad I did. I am so happy with this pan that I'm ordering the set.", 'Sunny C.'),
    'R555': ('Awesome pan and peace of mind that I am not ingesting bits of toxins when I cook. Nice looking pan too!', 'Gwen'),
})
def check_reviews(ids):
    rev = {r['id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'content/reviews/reviews.csv')))}
    for k in ids:
        q = HG['REVS'][k][0]; o = rev[k]['quote']; pos = 0
        assert rev[k]['stars'] == '5', (k, 'sterren')
        for p in [p.strip() for p in q.split('...') if p.strip()]:
            j = o.find(p, pos); assert j >= 0, (k, 'niet letterlijk', p); pos = j + len(p)
        assert len(q) <= 120, (k, len(q))
check_reviews(['R025', 'R240', 'R555', 'R583'])

# ---------------------------------------------------------------- extra bouwstenen
def note_head(t, bg='#FFFFFF', pad='8px 40px 10px 40px'):
    return row(bg, pad, serif(t, 28, 32, INK, 'ptitle', True), 'left', 'pad')
def proof4(items, bg='#FFFFFF', pad='4px 20px 22px 20px'):
    """2x2 bewijsraster met de gedeelde iconen (icoon, kop, regel)."""
    cell = lambda ic, a, b: ('<td width="50%%" valign="top" style="padding:0 5px 10px 5px;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid %s;border-radius:10px;">'
                             '<tr><td align="center" style="padding:16px 10px 16px 10px;"><img src="{{SHARED}}/%s" width="44" alt="" style="display:block;margin:0 auto;width:44px;height:auto;border:0;">%s%s</td></tr></table></td>') % (
        HAIR, ic, txt(a, 15, 20, INK, 700, 'text-align:center;padding-top:10px;'), txt(b, 13, 18, '#6E6A64', 500, 'text-align:center;padding-top:3px;'))
    c = [cell(*x) for x in items]
    t = '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>%s%s</tr><tr>%s%s</tr></table>' % tuple(c)
    return row(bg, pad, t, 'center', 'padx')
def stars_row(bg=CREAM, pad='24px 20px 22px 20px'):
    return row(bg, pad, txt('&#9733;&#9733;&#9733;&#9733;&#9733;', 16, 18, GOLD, 400, 'letter-spacing:3px;text-align:center;') + txt('100,000+ HAPPY CUSTOMERS', 12, 16, INK, 700, 'letter-spacing:2px;text-align:center;padding-top:4px;'), 'center', 'padx')
def labs_card(us, camp):
    h = txt('The paper, not the label', 12, 16, '#D9C9A8', 700, 'letter-spacing:2.2px;text-transform:uppercase;text-align:center;padding-bottom:10px;')
    h += serif('Report no. 25895', 40, 44, '#FFFFFF', 'h1b', True, 'text-align:center;')
    h += txt('Light Labs, an ISO/IEC 17025-accredited lab, tested our titanium cooking surface for 31 PFAS compounds. Every one came back below the detection limit.', 16, 25, '#E6E3DC', 400, 'text-align:center;padding-top:14px;')
    h += txt('Released %s.' % ('October 30, 2025' if us else '30 October 2025'), 13, 19, '#C9C2B6', 500, 'text-align:center;padding-top:8px;')
    return row(ESP, '30px 28px 0 28px', h, 'center', 'pad') + dark_button('Read the report myself', utm(LABS_PAGE, camp, 'labs'), '')
def promise_boxes(us):
    it = [('icon-warranty-75-year.png', '75-year warranty', 'A dent, a warped base, a loose handle or rivet, a lid that no longer fits. All covered, for 75 years.'),
          ('icon-returns-30-day.png', '30-day returns', 'Changed your mind? Send it back unused within 30 days of delivery.')]
    i = serif('Two promises', 30, 34, INK, 'h1s', True, 'text-align:center;padding-bottom:6px;')
    for ic, a, b in it:
        inner = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td width="56" valign="top" style="padding:0 12px 0 0;"><img src="{{SHARED}}/%s" width="44" alt="" style="display:block;width:44px;height:auto;border:0;"></td>'
                 '<td valign="top">%s%s</td></tr></table>') % (ic, txt(a, 16, 22, INK, 700), txt(b, 15, 23, '#4A4A4A', 400, 'padding-top:4px;'))
        i += '<div style="height:10px;line-height:10px;font-size:0;">&nbsp;</div>' + boxed(inner, HAIR, '#FFFFFF', '16px 18px')
    return row(CREAM, '28px 20px 26px 20px', i, 'left', 'padx')
def big_quote(q, who, bg='#FFFFFF'):
    return row(bg, '30px 34px 24px 34px', txt('&#9733;&#9733;&#9733;&#9733;&#9733;', 15, 18, GOLD, 400, 'letter-spacing:3px;text-align:center;padding-bottom:10px;')
               + serif('&ldquo;%s&rdquo;' % q, 26, 33, INK, 'h1s', True, 'text-align:center;') + txt(who, 13, 18, '#8A847A', 600, 'text-align:center;padding-top:10px;letter-spacing:0.4px;'), 'center')
def meta_bf(id_, mkt, sender, subj, alts, pre, when, who, why):
    return ('ID: %s\nMARKT: %s\nSENDER: %s\nSUBJECT A: %s\nSUBJECT B: %s\nANDERE ONDERWERPEN: %s\nPREVIEW: %s\nWANNEER: %s\nWIE: %s\nWAAROM: %s' % (id_, mkt, sender, subj[0], subj[1], ' · '.join(alts), pre, when, who, why))
def HEADBF(meta_, subj, pre):
    return head(meta_, subj, pre).replace('HOMESTEAD E5/E6 · NOVEMBER 2026 (concept 5 nov 2026, niet in Klaviyo, niets live).',
                                          'FLOW Rn556d AANMELDING · BF-W2/BF-W3 (concept 6 nov 2026, niet in Klaviyo, niets live).').replace(
        'ROASTING PAN INT · NEW IN STOCK + BLACK FRIDAY SPECIAL (concept 1 nov 2026, niet in Klaviyo, niets live).',
        'FLOW Rn556d AANMELDING · BF-W2/BF-W3 (concept 6 nov 2026, niet in Klaviyo, niets live).')
WHO = 'Flow Rn556d (lijst Uw8eZG), groep B van de test BF-W1 tegen BF-W1+W2+W3; %s; filter Placed Order = 0 sinds flowstart; smart sending aan'
BAD = ('next batch', 'reserve', 'arriving', 'next shipment', 'purifier', 'lifetime', 'for life', 'free filter', 'scratch-proof', 'while supplies last',
       'vraag floris', 'risk-free', 'money-back', 'free returns', '100-day', 'shop now', 'learn more', 'buy now', 'delve', 'unlock', 'elevate', 'journey', 'seamless', "don't miss")

files = {}
for mkt in ('us', 'int'):
    US = mkt == 'us'; M = mkt.upper(); c2 = 'bfw2-' + mkt; c3 = 'bfw3-' + mkt
    who = WHO % ('US + geen land (person.Country)' if US else 'INT (land bekend, niet US)')
    END = 'Monday, November 30' if US else 'Monday 30 November'
    SMALL = ('Offer valid November 1 to 30. Gifts while the sale runs; the water filter is a weekly draw.' if US else 'Offer valid 1 to 30 November. The water filter is a weekly draw.')

    # ======================= BF-W2 · kort, direct response (Floris 6 nov: korter en meer sale) =======================
    subj = ('Your 70% off is still here', 'A note from Benjamin (and the sets)')
    alts = ('Where I would start at 70% off', 'Still deciding? Here is the short version', 'Up to 70% off the sets')
    pre = 'Up to 70% off, 4 free gifts, no code needed. Here is where I would start.'
    b = HEADBF(meta_bf('bfw2-%s · Kort, direct response, sale voorop' % mkt, M, 'Benjamin from Siraat', subj, alts, pre, 'dag 1, 10:00 lokale tijd (na BF-W1)', who,
                       'Floris 6 nov: korter en meer sale. Aanbod en knop bovenaan, één keuze tussen twee sets, deadline.'), subj[0], pre) + OPEN3()
    b += P("Hi, Benjamin here. Quick one: your VIP Black Friday prices are still live. <b>Up to 70% off</b>, 4 gifts with every order, no code needed.", '#FFFFFF', '34px 40px 16px 40px')
    b += pbtn('Shop VIP Black Friday', utm(SALE, c2, 'cta-top'), US, '4px 30px 22px 30px')
    b += row('#FFFFFF', '0 20px 22px 20px', img(IM_EGGS, 'Two friends laughing as fried eggs slide out of a Siraat hammered titanium pan onto toast', utm(SALE, c2, 'img'), 560, 10), 'center', 'padx')
    b += note_head('Where I&#39;d start')
    if US:
        b += wide_card('set12', 'The whole stove in one box, plus a free Pizza Steel. Just arrived and selling fast.', US, '70% OFF', 'Get the 12-piece set', utm(URL['set12'], c2, 'card-set12'))
        b += wide_card('set6', 'Mini, Small and Large, each with its own lid. Just arrived and selling fast.', US, '70% OFF', 'Get the 6-piece set', utm(URL['set6'], c2, 'card-set6'))
    else:
        b += wide_card('set6', 'Mini, Small and Large, each with its own lid. Just arrived and selling fast.', US, '70% OFF', 'Get the 6-piece set', utm(URL['set6'], c2, 'card-set6'))
        b += wide_card('standard', 'Only need one? The pan Siraat started with.', US, '70% OFF', 'Get the Pan Pro', utm(URL['standard'], c2, 'card-standard'))
    b += P('Pure titanium, no coating, nothing to wear off. Covered for 75 years, and 30 days to send it back unused.', '#FFFFFF', '10px 40px 12px 40px')
    b += P('<b>The sale ends %s.</b> After that, prices go back to normal.' % END, '#FFFFFF', '0 40px 8px 40px') + sign()
    files['bfw2-%s' % mkt] = b + small(SMALL) + TAIL

    # ======================= BF-W3 · Built to last. Priced for Black Friday. =======================
    subj = ('Built to last. Priced for Black Friday.', 'Report no. 25895')
    alts = ('Why ours is covered for 75 years', 'Has your pan ever been tested?', '"The last pans we ever have to purchase"')
    pre = '75 years of cover, no coating, 30 days to decide. Up to 70%% off until %s.' % ('Nov 30' if US else '30 Nov')
    b = HEADBF(meta_bf('bfw3-%s · Twijfels weg: garantie, geen coating, retour, Light Labs, reviews' % mkt, M, 'Siraat', subj, alts, pre, 'dag 2, 09:00 lokale tijd', who,
                       'Plan 2026-11: twijfels wegnemen, visueel zoals E5. A/B: belofte (specifiek) tegen autoriteit (rapportnummer).'), subj[0], pre) + OPEN3()
    b += glass_img(IM_DROP, utm(SALE, c3, 'hero'), 'VIP Black Friday', 'Built to last.<br>Priced for Black Friday.', 'Up to 70%% off. Ends %s.' % END, 460, 290, 34)
    b += hero_btn('Get my Black Friday price', utm(SALE, c3, 'cta1'), US, '#FFFFFF', '20px 30px 22px 30px')
    b += P("Benjamin here. 70% off is only a good deal if the pan is still in your kitchen in twenty years. So before you pick one, here's what stands behind it.", '#FFFFFF', '4px 40px 18px 40px')
    b += proof4([('icon-warranty-75-year.png', '75-year warranty', 'Against defects'), ('icon-no-coating.png', 'No coatings', 'Pure titanium surface'),
                 ('icon-returns-30-day.png', '30-day returns', 'Unused, from delivery'), ('icon-pfas-tested.png', 'Light Labs tested', 'Report no. 25895')])
    b += pull('Nothing on it to wear off. That&#39;s why we can cover it for 75 years.')
    b += gap('#FFFFFF', 20) + glass_img(IM_SPAT, utm(URL['standard'], c3, 'img-spatula'), 'No coatings', 'Metal spatula? Go ahead.', 'A pure titanium cooking surface')
    b += P('A coated pan is a pan with a layer on it, and layers wear. Ours has a pure titanium cooking surface and no coatings, so there is no layer to wear thin or flake into your food. Metal utensils are fine. So is the dishwasher.', '#FFFFFF', '22px 40px 26px 40px')
    b += labs_card(US, c3)
    b += promise_boxes(US)
    b += big_quote("Buy it because it's safe, it's the only pan you will need in your kitchen, life long.", 'A Siraat customer')
    b += revblock(['R240', 'R555', 'R583'], CREAM, 'In their words')
    b += heading('Where to start', '#FFFFFF', '30px 24px 16px 24px')
    b += wide_card('standard', 'The everyday size. The pan Siraat started with.', US, '70% OFF', 'Get the Pan Pro', utm(URL['standard'], c3, 'card-standard'))
    b += wide_card('set6', 'Mini, Small and Large, each with its own lid. Selling fast.', US, '70% OFF', 'Get the 6-piece set', utm(URL['set6'], c3, 'card-set6'))
    if US: b += wide_card('set12', '3 pans, 3 pots, 6 lids, plus a free Pizza Steel. Selling fast.', US, '70% OFF', 'Get the 12-piece set', utm(URL['set12'], c3, 'card-set12'))
    b += row('#FFFFFF', '2px 30px 24px 30px', txt(FRIC(US), 13, 19, GREY, 500, 'text-align:center;'), 'center')
    b += bf_short(US, c3, 'band').replace('Free shipping, from the US.', 'Free shipping from the US.').replace('Shop VIP Black Friday', 'Claim my Black Friday price')
    b += closing('Happy cooking,').replace('6px 40px 4px 40px', '28px 40px 4px 40px') + sign()
    files['bfw3-%s' % mkt] = b + small(SMALL) + TAIL

for k, v in files.items():
    assert '—' not in v and '–' not in v, (k, 'streepje')
    body = v.split('-->', 1)[1]
    assert '$' not in body and not re.search(r'\{\{(PRICE|WAS|FROM)', body), (k, 'prijs')
    plain = re.sub(r'<[^>]+>', ' ', body).lower()
    for bad in BAD: assert bad not in plain, (k, bad)
    if '-int' in k: assert 'thanksgiving' not in plain and 'veterans' not in plain and not re.search(r'\{\{(GIFTS|FRICTION)', body) and 'set12' not in body and '12-piece' not in plain, k
    open(os.path.join(N, k + '.html'), 'w').write(v); print('geschreven', k, len(v))
