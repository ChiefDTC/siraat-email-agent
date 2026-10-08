"""Productblokken voor de flows (productmatrix, research/tailoring/10-productmatrix.md).

Schrijft drie blokken in klaviyo/templates/partials/blocks/ en de productbeelden in partials/shared/:
  about.html   {{BLOCK:about src="<expr>" lead="YOUR" pad="..."}}
               "About your <product>": beeld, kop, 3 feiten, het meest gestelde bezwaar met antwoord, 1 echte review.
  goes.html    {{BLOCK:goes src="<expr>" lead="YOUR" pad="..." pre="<url tot /products/>" post="<rest van de url>" note="..."}}
               "Goes with your <product>": 2 rijen op basis van de echte kooppatronen (research/personalisatie/01-voorstel.md 2.1-2.2).
               Link per rij = pre + handle + post (zo kan een mail HI10 of een eigen code in de link zetten).
  noun.html    {{BLOCK:noun src="<expr>" dflt="pan"}}  inline: pan / wok / pizza steel / pot / set / apron ...
  label.html   {{BLOCK:label src="<expr>" dflt="PAN"}}  inline, hoofdletters: PAN PRO 11&Prime; / PIZZA STEEL / 12-PIECE SET ...
  pick.html    {{BLOCK:pick src="<expr>" set="..." pot="..." pizza="..." apron="..." dflt="..."}}  inline keuze per groep
               (zelfde volgorde als about), bijvoorbeeld een productspecifieke hero: src="{{BLOCK:pick ... set="{{IMG}}/c1-hero-set.jpg" ...}}".
<expr> is de string waarin gezocht wordt: event.Items|join:',' (Checkout Started, Placed Order), event|lookup:'Product Name'
(Added to Cart), event.Name (Viewed Product). Volgorde van de keten = prioriteit bij meer producten in de cart: set, pot,
Pan Pro per maat, vorm, overig kookgerei, accessoires. Elk blok heeft data-about / data-goes = categorie (voor de tests).
Geen prijzen in deze blokken (55% van de orders is internationaal; prijzen alleen waar de template dat al per land regelt).
Reviews: letterlijk uit content/reviews/reviews.csv (Trustpilot), het script controleert dat elke quote echt in die review staat.
Beelden: kopieën van content/products/*/img (en enkele Shopify-CDN-kopieën in scratch), originelen nooit gewijzigd.
Gebruik: python3 -I scripts/make_product_blocks.py [--dl=<map met gedownloade CDN-beelden>]"""
import os, sys, csv, re
from PIL import Image, ImageChops
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
B = os.path.join(ROOT, 'klaviyo', 'templates', 'partials', 'blocks'); SH = os.path.join(ROOT, 'klaviyo', 'templates', 'partials', 'shared')
P = os.path.join(ROOT, 'content', 'products')
OPT = {a.split('=', 1)[0]: a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--') and '=' in a}

# ---------- categorieën: (key, voorwaarde-tokens, noun, label, beeld) ----------
# tokens: lijst substrings, OR. Volgorde = prioriteit.
CATS = [
 ('set12',    ['12-Pcs', '12 pcs'], 'set', '12-PIECE SET'),
 ('setall',   ['Everything'], 'set', 'JUST EVERYTHING BUNDLE'),
 ('setbig',   ['Cookware Set Pro', 'Complete Edition', 'Full Hammered', '2 Pans', 'Pro Duo', 'Pan Pro Kit', 'Wok & Deep'], 'set', 'SET'),
 ('pot',      ['Pot'], 'pot', 'POT'),
 ('set6',     ['6-Pcs', '6-teilig'], 'set', '6-PIECE SET'),
 ('standard', ['Pan Pro Standard', 'Titanium Pan Pro', 'Frying Pan'], 'pan', 'PAN PRO {{IF:US}}11&Prime;{{ELSE}}STANDARD{{ENDIF}}'),
 ('large',    ['Pan Pro Large'], 'pan', 'PAN PRO {{IF:US}}12&Prime;{{ELSE}}LARGE{{ENDIF}}'),
 ('small',    ['Pan Pro Small'], 'pan', 'PAN PRO {{IF:US}}10&Prime;{{ELSE}}SMALL{{ENDIF}}'),
 ('mini',     ['Pan Pro Mini'], 'pan', 'PAN PRO MINI'),
 ('deep',     ['Deep Pan'], 'deep pan', 'DEEP PAN'),
 ('wok',      ['Wok'], 'wok', 'WOK'),
 ('crepe',    ['pe Pan'], 'cr&ecirc;pe pan', 'CR&Ecirc;PE PAN'),
 ('pizza',    ['Pizza Steel'], 'pizza steel', 'PIZZA STEEL'),
 ('roast',    ['Roasting'], 'roasting pan', 'ROASTING PAN'),
 ('panpro',   ['Hammered Pan Pro', 'Cook & Prep'], 'pan', 'PAN PRO'),
 ('board',    ['Titanium Cutting Board'], 'board', 'CUTTING BOARD'),
 ('lid',      ['Lid'], 'lid', 'LID'),
 ('mill',     ['Mill'], 'mills', 'MILLS'),
 ('utensil',  ['Utensil', 'Chopsticks'], 'utensils', 'UTENSILS'),
 ('apron',    ['Apron'], 'apron', 'APRON'),
 ('sheets',   ['Dishwasher Sheets', 'Detergent'], 'sheets', 'DISHWASHER SHEETS'),
 ('giftcard', ['Gift Card'], 'gift card', 'GIFT CARD'),
]
KEY = {c[0]: c for c in CATS}

# ---------- beelden (240x240, getoond op 96 of 64 px) ----------
DL = OPT.get('--dl', '')
IMG = {
 'standard': P + '/titanium-hammered-pan-pro/img/packshot-1.jpg', 'large': P + '/titanium-hammered-pan-pro/img/packshot-2.jpg',
 'small': P + '/titanium-hammered-pan-pro/img/packshot-3.jpg', 'mini': P + '/titanium-hammered-pan-pro/img/packshot-3.jpg',
 'panpro': P + '/titanium-hammered-pan-pro/img/packshot-1.jpg',
 'deep': P + '/titanium-hammered-deep-pan-pro/img/packshot-3.jpg', 'wok': P + '/titanium-hammered-wok-pan-pro/img/packshot-3.jpg',
 'crepe': P + '/titanium-hammered-crepe-pan-pro/img/packshot-2.jpg', 'pizza': P + '/titanium-hammered-pizza-steel/img/packshot-1.jpg',
 'roast': P + '/titanium-hammered-roasting-pan/img/packshot-1.jpg', 'lid': P + '/stainless-steel-lid/img/packshot-1.jpg',
 'board': P + '/titanium-cutting-board-v2/img/packshot-2.jpg', 'mill': P + '/salt-pepper-mill-set/img/packshot-1.jpg',
 'apron': P + '/siraat-signature-apron/img/packshot-1.jpg', 'sheets': P + '/dishwashing-detergent-sheets-fresh-lemon/img/packshot-1.jpg',
 'giftcard': P + '/e-gift-card/img/image-1.jpg', 'set6': P + '/titanium-hammered-pan-set-with-lids-6-pcs/img/packshot-1.jpg',
 'set12': P + '/titanium-hammered-cookware-set/img/packshot-1.jpg', 'setbig': P + '/titanium-hammered-cookware-set-pro/img/packshot-1.jpg',
 'setall': DL + '/TitaniumHammeredPanPro_18.webp', 'pot': DL + '/6PCSSet08_1_3.webp', 'utensil': DL + '/Utensils05-V2_1.webp',
}
CROP = {'giftcard': (0.26, 0.17, 0.74, 0.65)}   # alleen het monogram van de kaart, zonder kersttekst

# ---------- inhoud per categorie ----------
# v5 (8 okt 2026, integratie): about en label zijn marktveilig. Maten via {{SIZE:cm}} / {{SIZE:cm:both}} en bedragen of US-teksten
# via {{IF:US}}..{{ELSE}}..{{ENDIF}} (scripts/v5lib.py, uitgeklapt door build_template.py na de blokexpansie, signaal per flow).
# Nooit meer een inch of $ los in about/label: buiten de US cm en geen dollar. goes/goes1 zijn vervangen door xsell (v5lib) en niet herzien.
# head, 3 feiten, bezwaar (vraag, antwoord), review-id + quote (letterlijk, mag op een hele zin of met ... ingekort), productlabel
A = {
 'standard': ("The size most kitchens start with.",
   ["{{SIZE:28:both}}: everyday cooking for 2 to 4.", "Gas, electric, ceramic and induction.", "No coating. Tested free from PFAS by Light Labs, report no. 25895."],
   ("Will eggs stick?", "Not once it is hot. Medium heat for 2 to 3 minutes, the water drop test, then a thin layer of oil."),
   ('R411', "I purchased the hammered pro pan standard. It is beautiful and lightweight.", 'Pan Pro Standard')),
 'large': ("Room for the whole family.",
   ["{{SIZE:30:both}}: family dinners, batch cooking, several steaks at once.", "Gas, electric, ceramic and induction.", "No coating. Tested free from PFAS by Light Labs, report no. 25895."],
   ("Which lid fits?", "The 30 cm Stainless Steel Lid. One in five Large owners adds it next."),
   ('R473', "I saved up and bought the large fry pan. It's a whole new way to cook.", 'Pan Pro Large')),
 'small': ("Dinner for two, done right.",
   ["{{SIZE:26:both}}: the right size for two.", "Gas, electric, ceramic and induction.", "No coating. Tested free from PFAS by Light Labs, report no. 25895."],
   ("Is {{SIZE:26}} big enough?", "For two, yes. Cooking for 3 or more most nights? The {{SIZE:28}} is the better pick."),
   ('R401', "Now I can cook knowing I have the top of the line cookware...", 'Pan Pro Small')),
 'mini': ("The one you grab for breakfast.",
   ["{{SIZE:20:both}}: eggs, an omelette, a portion for one.", "The same titanium cooking surface as the bigger sizes.", "Gas, electric, ceramic and induction."],
   ("Too small to be useful?", "It is the pan owners buy most as their second one, for the quick jobs."),
   ('R324', "I ordered a 2nd smaller pan because of this experience.", 'Pan Pro Mini')),
 'panpro': ("The original hammered titanium pan.",
   ["Four sizes, from {{SIZE:20}} to {{SIZE:30}}.", "Gas, electric, ceramic and induction.", "No coating. Tested free from PFAS by Light Labs, report no. 25895."],
   ("Will eggs stick?", "Not once it is hot. Medium heat for 2 to 3 minutes, the water drop test, then a thin layer of oil."),
   ('R473', "I saved up and bought the large fry pan. It's a whole new way to cook.", 'Pan Pro')),
 'deep': ("Sears like a skillet, holds like a saut&eacute; pan.",
   ["Higher sides, about {{SIZE:6:both}}, for sauces, pasta and one-pan dinners.", "The same titanium cooking surface as the Pan Pro.", "Gas, electric, ceramic and induction."],
   ("Is there a lid for it?", "Match the diameter: the 20, 26, 28 and 30 cm lids fit. There is no lid for the 24 cm yet."),
   ('R562', "The Deep Pan Pro is my 'go to' favourite because I like to cook big meals", 'Deep Pan Pro')),
 'wok': ("Toss it. Nothing spills.",
   ["Deep, flared walls, up to {{SIZE:9:both}}.", "The same titanium cooking surface as the Pan Pro.", "Gas, electric, ceramic and induction."],
   ("Metal spatula?", "Yes. There is no coating on it to scratch."),
   ('R014', "Also, I purchased their titanium wok a few months ago and it performs exactly as expected.", 'Wok Pan Pro')),
 'crepe': ("A low rim, so the spatula slides under.",
   ["Flat and wide: cr&ecirc;pes, pancakes, eggs and tortillas.", "The same titanium cooking surface as the Pan Pro.", "Gas, electric, ceramic and induction."],
   ("Will cr&ecirc;pes stick?", "Heat it first on medium, then a few drops of oil. The first one is the test."),
   ('R088', "This is the best crepe pan that I have used that works like a non-stick but gives crispy output like a cast iron pan.", 'Cr&ecirc;pe Pan Pro')),
 'pizza': ("Lift it in, bake, lift it out.",
   ["Hammered surface: air gets under the dough, so it releases.", "No coating and no seasoning: nothing to burn off or keep up.", "Two side handles. Home oven, pizza oven or grill."],
   ("Dishwasher?", "Yes. Let it cool first, or use warm water and a little soap."),
   ('R048', "Have used my pizza stone a couple of times and it has made an excellent crust.", 'Pizza Steel')),
 'roast': ("Sear, roast and make the gravy in one pan.",
   ["Fitted rack included, for crisp skin all the way round.", "Stovetop to oven, induction too.", "{{IF:US}}14 x 10.6&Prime;, 2.8&Prime; deep.{{ELSE}}36 x 27 cm, 7 cm deep.{{ENDIF}} Pan and rack go in the dishwasher."],
   ("Will a turkey fit?", "Check the size above against your bird. Unused, it can go back within 30 days of delivery."),
   None),
 'pot': ("Soups, sauces and pasta, on titanium.",
   ["Comes with its own stainless steel lid.", "The same hammered titanium cooking surface as the pans, no coating.", "Gas, electric, ceramic and induction. Oven and dishwasher safe."],
   ("Same warranty as the pans?", "Yes. Every pot is covered for 75 years."),
   ('R018', "Our pots and pans are beautiful. They clean up very well and look brand new after every cleaning.", 'pots and pans')),
 'set6': ("Three pans, three lids, one decision.",
   ["Pan Pro {{SIZE:20}}, {{SIZE:26}} and {{SIZE:30}}, each with its own lid.", "Every pan: tested free from PFAS by Light Labs.", "One 75-year warranty covers every piece."],
   ("Pans and lids in one box?", "They can travel in separate parcels, each with its own tracking."),
   ('R025', "I ordered one pan to try it out. I'm so glad I did. I am so happy with this pan that I'm ordering the set.", 'set')),
 'set12': ("A complete PFAS-free kitchen.",
   ["Three pans and three pots, six lids.", "Every piece: induction ready, oven and dishwasher safe.", "One 75-year warranty for the whole set."],
   ("Why two parcels?", "Pans and pots can travel separately, each with its own tracking. Nothing is missing."),
   ('R530', "I ordered a full set of the titanium cookware. It arrived in phases. All of it works as stated.", 'full set')),
 'setbig': ("Every pan you need, one surface.",
   ["The same titanium cooking surface on every piece.", "Gas, electric, ceramic and induction.", "One 75-year warranty covers the set."],
   ("What if I do not use every piece?", "Unused pieces can go back within 30 days of delivery."),
   ('R398', "I ended up buying the whole collection. The food turned out much better cooked and juicier.", 'collection')),
 'setall': ("The whole kitchen, in one order.",
   ["Pans, pots, a roasting pan and the tools, one titanium cooking surface.", "Pieces travel in separate parcels, each tracked.", "One 75-year warranty covers it all."],
   ("What if I do not use every piece?", "Unused pieces can go back within 30 days of delivery."),
   ('R398', "I ended up buying the whole collection. The food turned out much better cooked and juicier.", 'collection')),
 'board': ("Nothing soaks in.",
   ["Pure titanium, non-porous: no juices or smells soak in.", "Anti-microbial, with a juice groove.", "Kind to knives: knife steel is harder than titanium."],
   ("Knife marks?", "Every board shows them. On titanium they are surface lines, not grooves that hold bacteria."),
   ('R490', "The cutting board itself is awesome and exceeded my expectations.", 'Cutting Board')),
 'lid': ("Sized to your pan.",
   ["304 stainless steel, with three steam vents.", "20, 26, 28 or 30 cm.", "One lid fits every Siraat pan of that diameter."],
   ("Which size?", "Match the diameter: Mini 20 cm, Small 26 cm, Standard 28 cm, Large 30 cm."),
   ('R157', "Pans and lids arrived promptly and in good condition. Excellent quality and we look forward to using them for a long time.", 'pans and lids')),
 'mill': ("Heavy, metal, and easy to fill.",
   ["All-metal body with a knurled grip.", "12 numbered settings, from fine to coarse.", "A wide opening, so refilling is quick."],
   ("Which salt?", "Sea salt, Himalayan or rock salt."),
   ('R256', "Really well made, plastic free, salt and pepper grinders.", 'Mill Set')),
 'utensil': ("Made for your pans.",
   ["Titanium tools, light in the hand.", "Safe on every Siraat pan.", "Metal on titanium is fine: there is no coating to damage."],
   ("Will they mark my pan?", "Any marks are cosmetic. There is no coating to scrape off."),
   ('R018', "I received a free metal spatula as a gift. It works great and does not scratch the pans.", 'spatula')),
 'apron': ("Made for the cook who stays at the stove.",
   ["Heavy 16-oz canvas with a water-repellent finish.", "Adjustable neck and waist straps, one size fits most.", "A real front pocket. Four colors: Azure, Moss, Ember, Oak."],
   ("Machine washable?", "Wipe it down, or hand wash cold and let it air dry."),
   ('R200', "It comes beautifully boxed, and the apron, bottle and spatula are such lovely gifts.", 'gift box')),
 'sheets': ("One sheet, one load.",
   ["Pre-dosed: no measuring, no plastic pod.", "Phosphate-free and bleach-free.", "Tear one in half for a light load, or for washing up by hand."],
   ("How many washes?", "30 sheets, up to 60 washes when you tear them in half."),
   None),
 'giftcard': ("They pick the pan and the size.",
   ["Sent by email, so it cannot get stuck in the mail.", "{{IF:US}}$25 to $200.{{ELSE}}Several amounts to choose from.{{ENDIF}}", "Spend it on anything in the shop."],
   ("Can it be combined with a code?", "Yes. It works as payment, and one discount code still applies."),
   None),
}

# ---------- cross-sell: wat erbij hoort ----------
# item: (naam, regel, handle, beeld)
ITEM = {
 'mini': ("Pan Pro Mini 8&Prime;", "The breakfast pan: eggs and small portions.", 'titanium-hammered-pan-pro-mini', 'mini'),
 'small': ("Pan Pro Small 10&Prime;", "Dinner for two.", 'titanium-hammered-pan-pro-small', 'small'),
 'standard': ("Pan Pro 11&Prime;", "The size most kitchens start with.", 'original-siraat-100-pure-titanium-pan-with-hammered-pattern', 'standard'),
 'deep': ("Deep Pan Pro", "Higher sides for sauces, pasta and one-pan dinners.", 'titanium-hammered-deep-pan-pro', 'deep'),
 'wok': ("Wok Pan Pro", "Up to 3.5&Prime; deep, to toss without spilling.", 'titanium-hammered-wok-pan-pro', 'wok'),
 'crepe': ("Cr&ecirc;pe Pan Pro", "Flat and wide: cr&ecirc;pes, pancakes, tortillas.", 'titanium-hammered-crepe-pan-pro', 'crepe'),
 'lid20': ("Stainless Steel Lid, 20 cm", "Fits your 8&Prime; Mini.", 'stainless-steel-lid', 'lid'),
 'lid26': ("Stainless Steel Lid, 26 cm", "Fits your 10&Prime; Small.", 'stainless-steel-lid', 'lid'),
 'lid28': ("Stainless Steel Lid, 28 cm", "Fits your 11&Prime; Pan Pro.", 'stainless-steel-lid', 'lid'),
 'lid30': ("Stainless Steel Lid, 30 cm", "Fits your 12&Prime; Large.", 'stainless-steel-lid', 'lid'),
 'lid': ("Stainless Steel Lid", "Match the diameter of your pan.", 'stainless-steel-lid', 'lid'),
 'board': ("Titanium Cutting Board", "Non-porous titanium, anti-microbial. Four sizes.", 'titanium-cutting-board-v2', 'board'),
 'boardL': ("Titanium Cutting Board", "The Large takes a whole pizza or a roast.", 'titanium-cutting-board-v2', 'board'),
 'apron': ("Siraat Signature Apron", "16-oz canvas, adjustable, four colors.", 'siraat-signature-apron-moss', 'apron'),
 'mill': ("Salt &amp; Pepper Mill Set", "All-metal, 12 grind settings. A matching pair.", 'salt-pepper-mill-set', 'mill'),
 'utensil': ("Titanium Utensil Set", "Titanium tools, made for your pans.", 'siraat-pure-titanium-utensils-bundle', 'utensil'),
 'sheets': ("Dishwasher Sheets", "One pre-dosed sheet per load, no plastic pod.", 'dishwashing-detergent-sheets-fresh-lemon', 'sheets'),
}
# per categorie: (kop, datazin of '', [items]); bron kooppatronen: personalisatie 2.1 en 2.2, cross-sell.md per product
G = {
 'mini':     ("What Mini owners add next", "One in five Mini owners comes back for the 11&Prime;.", ['standard', 'lid20']),
 'small':    ("What Small owners add next", "One in three Small owners comes back for the Mini.", ['mini', 'lid26']),
 'standard': ("What 11&Prime; owners add next", "One in five 11&Prime; owners comes back for the Mini.", ['mini', 'lid28']),
 'large':    ("What Large owners add next", "One in five Large owners adds the lid, one in seven the 10&Prime;.", ['small', 'lid30']),
 'panpro':   ("What Pan Pro owners add next", "The second order is most often a smaller size or a lid.", ['mini', 'lid']),
 'deep':     ("Goes with your deep pan", "The deep pan and the wok are the pair most often bought together.", ['wok', 'lid']),
 'wok':      ("Goes with your wok", "The wok and the deep pan are the pair most often bought together.", ['deep', 'crepe']),
 'crepe':    ("Goes with your cr&ecirc;pe pan", "", ['standard', 'wok']),
 'pizza':    ("Goes with your pizza steel", "", ['boardL', 'standard']),
 'roast':    ("Goes with your roasting pan", "", ['boardL', 'standard']),
 'pot':      ("Goes with your pot", "", ['standard', 'deep']),
 'set6':     ("Goes with your set", "Three in ten set owners add a board next.", ['board', 'apron']),
 'set12':    ("Goes with your set", "Three in ten set owners add a board next.", ['board', 'apron']),
 'setbig':   ("Goes with your set", "Three in ten set owners add a board next.", ['board', 'apron']),
 'setall':   ("Goes with your bundle", "", ['mill', 'sheets']),
 'board':    ("Goes with your board", "One in five board owners adds the 11&Prime; pan.", ['standard', 'utensil']),
 'lid':      ("Goes with your lid", "", ['mini', 'board']),
 'mill':     ("Goes with your mills", "", ['apron', 'board']),
 'utensil':  ("Goes with your utensils", "", ['standard', 'board']),
 'apron':    ("Goes with your apron", "", ['mill', 'standard']),
 'sheets':   ("Goes with your sheets", "", ['standard', 'board']),
}

F = "font-family:Inter,Arial,Helvetica,sans-serif;"
SERIF = "font-family:'Instrument Serif','Times New Roman',serif;font-style:italic;"

def cond(tokens):
    """Voorwaarde op de variabele s ({% with s=[[src]] %} staat om elk blok, zodat de expressie maar één keer in de HTML staat).
    Token 'A&B' = beide moeten erin staan."""
    one = lambda t: ' and '.join("'%s' in s" % x.replace("'", "\\'") for x in t.split('&'))
    return ' or '.join(one(t) for t in tokens)

# Alleen voor goes: Pan Pro met een deksel in dezelfde order krijgt geen deksel aangeboden (vooraan in de keten).
GEXTRA = [('standard', ['Pan Pro Standard&Lid'], ['mini', 'board']), ('large', ['Pan Pro Large&Lid'], ['small', 'board']),
          ('small', ['Pan Pro Small&Lid'], ['mini', 'board']), ('mini', ['Pan Pro Mini&Lid'], ['standard', 'board']),
          ('panpro', ['Pan Pro With Lid'], ['mini', 'board'])]

def fchain(val, keys=None, dflt='', extra=()):
    """Eén {% if %}/{% elif %}-keten voor één veld; opeenvolgende categorieën met dezelfde waarde delen één voorwaarde.
    Bouwt alleen de tekst die verschilt; de opmaak staat één keer om de keten heen (Gmail-clipping, export_klaviyo MAXKB)."""
    parts = []
    for k, toks, noun, label in list(extra) + CATS:
        if keys is not None and k not in keys: continue
        v = val(k)
        if v is None: continue
        if parts and parts[-1][1] == v: parts[-1][0].extend(toks)
        else: parts.append([list(toks), v])
    out = ''.join(('{%% if %s %%}' if i == 0 else '{%% elif %s %%}') % cond(t) + v for i, (t, v) in enumerate(parts))
    return out + ('{%% else %%}%s{%% endif %%}' % dflt if dflt else '{% endif %}')

def anycond(keys):
    return cond([t for k, toks, n, l in CATS if k in keys for t in toks])

def about_block():
    K = [k for k in KEY if k in A]
    R = [k for k in K if A[k][3]]
    tick = '<span style="color:#AC3B19;font-weight:600;">&#10003;</span>&nbsp; '
    rev = lambda k: ('&ldquo;%s&rdquo;' % A[k][3][1]) if A[k][3] else None
    who = lambda k: ('<b style="color:#282828;font-weight:600;">%s</b> &middot; Verified buyer &middot; %s' % (REV[A[k][3][0]]['name'], A[k][3][2])) if A[k][3] else None
    return ('{%% with s=[[src]] %%}{%% if %s %%}\n' % anycond(K) +
      '<tr><td class="pad" data-about="' + fchain(lambda k: k, K) + '" style="padding:[[pad]];">'
      '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="width:100%;background:#FFFFFF;border:1px solid #ECE7DD;">'
      '<tr><td style="padding:18px 18px 0 18px;' + F + 'font-size:11px;line-height:14px;letter-spacing:2px;font-weight:600;color:#AC3B19;">ABOUT [[lead]] ' + fchain(lambda k: KEY[k][3], K) + '</td></tr>'
      '<tr><td style="padding:6px 18px 0 18px;' + SERIF + 'font-size:26px;line-height:29px;color:#282828;">' + fchain(lambda k: A[k][0], K) + '</td></tr>'
      '<tr><td style="padding:12px 18px 8px 18px;' + F + 'font-size:14px;line-height:21px;color:#282828;">' + tick + fchain(lambda k: A[k][1][0], K) + '<br>' + tick + fchain(lambda k: A[k][1][1], K) + '<br>' + tick + fchain(lambda k: A[k][1][2], K) + '</td></tr>'
      '<tr><td style="padding:6px 18px 16px 18px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="#F8F7F2" style="background:#F8F7F2;padding:11px 14px;' + F + 'font-size:14px;line-height:20px;color:#282828;"><b>' + fchain(lambda k: A[k][2][0], K) + '</b> ' + fchain(lambda k: A[k][2][1], K) + '</td></tr></table></td></tr>'
      '{%% if %s %%}' % anycond(R) +
      '<tr><td style="padding:0 18px 18px 18px;' + F + '"><div style="border-top:1px solid #ECE7DD;padding-top:14px;"><div style="font-family:Arial,Helvetica,sans-serif;font-size:13px;letter-spacing:2px;color:#AC3B19;">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
      '<div style="font-size:15px;line-height:22px;color:#282828;padding:6px 0 6px 0;">' + fchain(rev, R) + '</div>'
      '<div style="font-size:12px;line-height:16px;color:#727272;">' + fchain(who, R) + '</div></div></td></tr>{% endif %}'
      '</table></td></tr>\n{% endif %}{% endwith %}\n')

def goes_block(n=2):
    K = [k for k in KEY if k in G]
    X = [(k + '+lid', t, None, None) for k, t, items in GEXTRA]
    GI = dict(((k + '+lid'), items) for k, t, items in GEXTRA)
    base = lambda k: k.split('+')[0]
    def fc(val, keys, **kw): return fchain(val, keys + list(GI), extra=X, **kw)
    def row(i):
        it = lambda k: ITEM[(GI[k] if k in GI else G[k][2])[i]]
        href = '[[pre]]' + fc(lambda k: it(k)[2], K) + '[[post]]'
        return ('<tr><td width="76" valign="middle" style="width:76px;padding:12px 0 12px 14px;%s"><img src="%s" width="64" height="64" alt="" style="width:64px;height:64px;"></td>'
                '<td valign="middle" style="padding:12px 12px 12px 12px;%s%s"><a href="%s" style="text-decoration:none;color:#282828;"><span style="font-size:15px;line-height:20px;font-weight:600;color:#282828;">%s</span><br>'
                '<span style="font-size:13px;line-height:18px;color:#727272;">%s</span> <span style="font-size:13px;font-weight:600;color:#AC3B19;white-space:nowrap;">See it&nbsp;&rarr;</span></a></td></tr>') % (
            'border-top:1px solid #ECE7DD;' if i else '', fc(lambda k: '{{SHARED}}/pc-%s.jpg' % it(k)[3], K), F, 'border-top:1px solid #ECE7DD;' if i else '',
            href, fc(lambda k: it(k)[0], K), fc(lambda k: it(k)[1], K))
    S = [k for k in K if G[k][1]]
    return ('{%% with s=[[src]] %%}{%% if %s %%}\n' % anycond(K) +
      '<tr><td class="pad" data-goes="' + fc(lambda k: base(k), K) + '" style="padding:[[pad]];">'
      '<div style="' + F + 'font-size:11px;line-height:14px;letter-spacing:2px;font-weight:600;color:#AC3B19;text-align:center;">OFTEN ADDED NEXT</div>'
      '<div class="h2" style="' + SERIF + 'font-size:32px;line-height:36px;color:#282828;text-align:center;padding:6px 0 4px 0;">' + fc(lambda k: G[base(k)][0], K) + '</div>'
      '{%% if %s %%}<div style="%sfont-size:13px;line-height:19px;color:#727272;text-align:center;">' % (anycond(S), F) + fc(lambda k: G[base(k)][1], S) + '</div>{% endif %}'
      '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="width:100%;background:#FFFFFF;border:1px solid #ECE7DD;margin-top:10px;">' + row(0) + (row(1) if n == 2 else '') + '</table>'
      '<div style="' + F + 'font-size:12px;line-height:18px;color:#727272;text-align:center;padding-top:8px;">[[note]]</div></td></tr>\n{% endif %}{% endwith %}\n')

def write_blocks():
    hdr = lambda n, u: '<!-- BLOCK %s (gegenereerd door scripts/make_product_blocks.py, niet met de hand wijzigen). %s -->\n' % (n, u)
    open(os.path.join(B, 'about.html'), 'w').write(hdr('about', 'Params: src (Django-expressie), lead (YOUR/THE), pad.') + about_block())
    open(os.path.join(B, 'goes.html'), 'w').write(hdr('goes', 'Params: src, pad, pre, post (link = pre + handle + post), note (regel onder de rijen, mag leeg). Geen gift card.') + goes_block())
    open(os.path.join(B, 'goes1.html'), 'w').write(hdr('goes1', 'Zoals goes, alleen de eerste rij (voor mails waar de tweede rij, vaak het deksel, al als hoofdkaart staat).') + goes_block(1))
    # inline blokken (midden in een zin of attribuut): geen commentaarregel
    open(os.path.join(B, 'noun.html'), 'w').write('{% with s=[[src]] %}' + fchain(lambda k: KEY[k][2], dflt='[[dflt]]') + '{% endwith %}')
    open(os.path.join(B, 'label.html'), 'w').write('{% with s=[[src]] %}' + fchain(lambda k: KEY[k][3], dflt='[[dflt]]') + '{% endwith %}')
    grp = lambda k: '[[set]]' if k.startswith('set') else ('[[%s]]' % k if k in ('pot', 'pizza', 'apron') else '[[dflt]]')
    open(os.path.join(B, 'pick.html'), 'w').write('{% with s=[[src]] %}' + fchain(grp, dflt='[[dflt]]') + '{% endwith %}')

def bg(im):
    px = [im.getpixel(p) for p in ((2, 2), (im.width - 3, 2), (2, im.height - 3), (im.width - 3, im.height - 3))]
    return tuple(sum(c[i] for c in px) // 4 for i in range(3))

# v5 (8 okt 2026): extra kaartbeelden voor het cross-sell-blok xsell (scripts/v5lib.py), gemaakt door scripts/make_v5_images.py.
# Deze nooit weggooien bij het opruimen hieronder.
V5_KEEP = {'large', 'set6', 'set12', 'pizza', 'roast'}

def make_pc(k, src, out_dir=SH):
    """Eén kaartbeeld pc-<k>.jpg (240x240) uit een kopie van de bronfoto; het origineel wordt nooit gewijzigd."""
    im = Image.open(src).convert('RGB')
    if k in CROP:
        x0, y0, x1, y1 = CROP[k]; im = im.crop((int(im.width * x0), int(im.height * y0), int(im.width * x1), int(im.height * y1)))
    else:   # inzoomen op het product: bounding box van alles wat afwijkt van de achtergrond, 8% marge, vierkant
        b = bg(im); diff = ImageChops.difference(im, Image.new('RGB', im.size, b)).convert('L').point(lambda v: 255 if v > 24 else 0)
        box = diff.getbbox() or (0, 0, im.width, im.height)
        cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2; s = max(box[2] - box[0], box[3] - box[1]) * 1.08
        s = max(s, min(im.size) * 0.35)
        canvas = Image.new('RGB', (int(s), int(s)), b); canvas.paste(im, (int(s / 2 - cx), int(s / 2 - cy))); im = canvas
    if min(im.size) < 240: sys.exit('beeld te klein voor 2x: %s %s' % (k, im.size))
    im.resize((240, 240), Image.LANCZOS).save(os.path.join(out_dir, 'pc-%s.jpg' % k), quality=84, optimize=True, progressive=True)

def write_images():
    used = {v[3] for v in ITEM.values()}   # alleen beelden die het goes-blok toont (about heeft geen beeld: de cart toont het product al)
    for f in os.listdir(SH):
        if f.startswith('pc-') and f[3:-4] not in used and f[3:-4] not in V5_KEEP: os.remove(os.path.join(SH, f))
    for k, src in IMG.items():
        if k not in used: continue
        if not os.path.exists(src): sys.exit('beeld ontbreekt: %s (geef --dl=<map> met de CDN-kopieën)' % src)
        make_pc(k, src)

def load_reviews():
    return {r['id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'content', 'reviews', 'reviews.csv')))}

def check_quotes():
    bad = []
    for k, v in A.items():
        if not v[3]: continue
        rid, q, _ = v[3]; r = REV.get(rid)
        if not r: bad.append('%s: review %s bestaat niet' % (k, rid)); continue
        if r['stars'] != '5': bad.append('%s: %s heeft %s sterren' % (k, rid, r['stars']))
        core = q[:-3] if q.endswith('...') else q
        if core not in r['quote']: bad.append('%s: quote niet letterlijk in %s' % (k, rid))
        if len(q) > 125: bad.append('%s: quote %d tekens (max ~120)' % (k, len(q)))
    for k, v in list(A.items()) + list(G.items()):
        if '—' in repr(v): bad.append('%s: gedachtestreepje' % k)
    if bad: sys.exit('\n'.join(bad))

REV = load_reviews()
if __name__ == '__main__':
    check_quotes(); write_blocks(); write_images()
    print('ok: about.html, goes.html, noun.html, pick.html en %d beelden pc-*.jpg' % len({v[3] for v in ITEM.values()}))
