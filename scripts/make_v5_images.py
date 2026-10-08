"""v5-beelden (8 okt 2026).
1. Kaartbeelden voor het cross-sell-blok: pc-large, pc-set6, pc-set12, pc-pizza, pc-roast (240x240) in klaviyo/templates/partials/shared,
   met dezelfde uitsnede-logica als scripts/make_product_blocks.py (make_pc), uit kopieën van content/products/*/img.
2. Hero's van de mails uit research/v5/05-beeld-vervangingen.csv opnieuw met scripts/make_hero.py: de 13 goedgekeurde v5-AI-beelden
   (de -2k-versie, zodat er nooit wordt opgeschaald) en echte foto's voor de 3 afgekeurde (egg-plate, pan-microphone, three-pans).
   Kop, subregel, label en aanbodbalk zijn dezelfde als in de hero van v4 (de flow-bouwers kunnen ze later aanpassen: alleen HERO hieronder
   wijzigen en dit script opnieuw draaien).
Originelen worden nooit gewijzigd. Gebruik: python3 -I scripts/make_v5_images.py [--cards] [--heroes] [--only=p2,k2-new]"""
import os, sys, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
OPT = {a.split('=', 1)[0]: (a.split('=', 1)[1] if '=' in a else '1') for a in sys.argv[1:] if a.startswith('--')}
P = os.path.join(ROOT, 'content', 'products'); AI = os.path.join(ROOT, 'content', 'media', 'ai-flash'); HP = os.path.join(ROOT, 'content', 'media', 'hp-shoot')
V = os.path.join(ROOT, 'klaviyo', 'templates', 'v3')
CARDS = {'large': P + '/titanium-hammered-pan-pro/img/packshot-2.jpg', 'set6': P + '/titanium-hammered-pan-set-with-lids-6-pcs/img/packshot-1.jpg',
         'set12': P + '/titanium-hammered-cookware-set/img/packshot-1.jpg', 'pizza': P + '/titanium-hammered-pizza-steel/img/packshot-1.jpg',
         'roast': P + '/titanium-hammered-roasting-pan/img/packshot-1.jpg'}
SEP = '  ·  '
# mail: (bron, hero-bestand(en), kop, subregel, label, aanbodbalk, ratio)
HERO = {
 'p1-first': ('ai:pan-trophy-1x1', ['post-purchase/assets/p1-first-hero.jpg'], "Good call.|Here's what's next.", 'Your order, 4 gifts and one tip.', 'ORDER CONFIRMED', 'YOUR 4 GIFTS ARE ON THE WAY', ''),
 'p1-repeat': ('ai:friends-greeting-1x1', ['post-purchase/assets/p1-repeat-hero.jpg'], 'Good to see|you again.', 'Same packing, same 4 gifts.', 'ORDER CONFIRMED', 'SAME 4 GIFTS, ON THE WAY', ''),
 'p2': ('hp-shoot/square/P09-A_Pan_Lid_1920w_q82.jpg', ['post-purchase/assets/p2-hero.jpg'], 'If you can|do an egg,', 'you can do anything', 'CHEF GUIDE', 'HEAT FIRST' + SEP + 'THEN OIL' + SEP + 'THEN EGG', ''),
 'p3-pan': ('ai:lid-steam-1x1', ['post-purchase/assets/p3-pan-hero.jpg'], 'The lid|that fits.', "Match it to your pan's diameter.", 'FITS YOUR PAN', 'YOUR 10% THANK-YOU CODE' + SEP + '14 DAYS', ''),
 'p3-pan-nocode': ('ai:lid-steam-1x1', ['post-purchase/assets/p3-pan-nocode-hero.jpg'], 'The lid|that fits.', "Match it to your pan's diameter.", 'FITS YOUR PAN', 'FREE SHIPPING' + SEP + '4 GIFTS WITH EVERY ORDER', ''),
 'p3-accessory': ('ai:pan-reflection-1x1', ['post-purchase/assets/p3-accessory-hero.jpg'], 'Now meet|the pan.', 'The original hammered titanium pan.', 'FOR SIRAAT OWNERS', 'YOUR 10% THANK-YOU CODE' + SEP + '14 DAYS', ''),
 'p3-accessory-nocode': ('ai:pan-reflection-1x1', ['post-purchase/assets/p3-accessory-nocode-hero.jpg'], 'Now meet|the pan.', 'The original hammered titanium pan.', 'FOR SIRAAT OWNERS', 'FREE SHIPPING' + SEP + '4 GIFTS WITH EVERY ORDER', ''),
 'p3-set': ('ai:crepe-flip-1x1', ['post-purchase/assets/p3-set-hero.jpg'], 'The pan your|set is missing.', 'Flat for crepes. Deep for stir-fry.', 'FOR SET OWNERS', 'YOUR 10% THANK-YOU CODE' + SEP + '14 DAYS', ''),
 'p3-set-nocode': ('ai:crepe-flip-1x1', ['post-purchase/assets/p3-set-nocode-hero.jpg'], 'The pan your|set is missing.', 'Flat for crepes. Deep for stir-fry.', 'FOR SET OWNERS', 'FREE SHIPPING' + SEP + '4 GIFTS WITH EVERY ORDER', ''),
 'r1-set': ('ai:full-stove-1x1', ['winback/assets/r1-set-hero.jpg'], 'The shapes|a set leaves out.', 'Crepe, wok, board and tools.', 'FOR SET OWNERS', 'EXTRA 10% OFF WITH HI10' + SEP + '$70 IN GIFTS', ''),
 'b2-clicked': ('ai:egg-slide-4x3', ['browse/assets/b2-clicked-hero.jpg'], 'Your own 10%,|for 48 hours.', 'Then the regular sale price again.', 'YOUR CODE · 48 HOURS', 'YOUR OWN 10% CODE' + SEP + '$70 IN GIFTS', '4:3'),
 'b2-clicked-nocode': ('ai:egg-slide-4x3', ['browse/assets/b2-clicked-nocode-hero.jpg'], '“I ordered one pan|to try it out.”', 'Sunny C., verified buyer', 'IN THEIR WORDS', '$70 IN GIFTS WITH EVERY ORDER' + SEP + 'FREE SHIPPING', '4:3'),
 'b2-notclicked': ('ai:sauce-taste-4x3', ['browse/assets/b2-notclicked-hero.jpg'], 'In their|words.', 'From skeptics to fourth-pan owners.', '100,000+ HAPPY CUSTOMERS', 'EXTRA 10% OFF WITH HI10' + SEP + '$70 IN GIFTS', '4:3'),
 'k2-new': ('hp-shoot/images/P11-A_Hammered_1920w_q82.jpg', ['cart/assets/k2-new-hero.jpg'], '15 pans,|or one.', 'The math on the pan in your cart.', 'THE REAL PRICE', 'EXTRA 10% OFF WITH HI10' + SEP + '$70 IN GIFTS', '4:3'),
 'c2': ('ai:olive-oil-4x3', ['checkout/assets/c2-hero-pfas.jpg'], 'Non-toxic is easy|to say.', "Here's the report: no. 25895.", 'STILL COMPARING? GOOD.', 'EXTRA 10% OFF WITH HI10' + SEP + '$70 IN GIFTS', '4:3'),
 'c3-p': ('products/titanium-hammered-pan-set-with-lids-6-pcs/img/packshot-1.jpg', ['checkout/assets/c3p-hero.jpg'], 'One pan,|or three?', '3 pans + 3 lids, about $116 a pan.', 'ONE PAN OR THREE', 'EXTRA 10% OFF WITH HI10' + SEP + '$70 IN GIFTS', '4:3'),
 'k3': ('ai:steak-sear-4x3', ['cart/assets/k3-hero.jpg'], 'The last email|about your cart.', 'Your own 10% code, good for 48 hours.', 'YOUR CODE · 48 HOURS', 'YOUR OWN 10% CODE' + SEP + '$70 IN GIFTS', '4:3'),
 'k3-nocode': ('ai:steak-sear-4x3', ['cart/assets/k3-nocode-hero.jpg'], 'The last email|about your cart.', 'Two promises, and $70 in gifts.', 'STILL IN YOUR CART', '$70 IN GIFTS WITH EVERY ORDER' + SEP + '30-DAY RETURNS', '4:3'),
 'w0': ('ai:egg-crack-1x1', ['welcome/assets/w0-hero.jpg'], 'First heat,|then oil.', 'Your first egg, in three steps.', 'CARE AND USE', '', ''),
 'w4-int': ('ai:two-sizes-1x1', ['welcome/assets/w4-int-hero.jpg'], 'Who are you|cooking for?', 'Pick your size. Duties paid.', 'THE ONE MOST PEOPLE PICK', '10% OFF WITH HI10' + SEP + '4 GIFTS', ''),
 'w4-us': ('ai:pasta-lift-1x1', ['welcome/assets/w4-us-hero.jpg'], 'Who are you|cooking for?', 'Pick your size. Your 10% is applied.', 'THE ONE MOST PEOPLE PICK', '10% OFF WITH HI10' + SEP + '$70 IN GIFTS', ''),
}

def src_path(s):
    if s.startswith('ai:'): return os.path.join(AI, s[3:] + '-v5-2k.jpg')
    if s.startswith('hp-shoot/'): return os.path.join(ROOT, 'content', 'media', s)
    if s.startswith('products/'): return os.path.join(ROOT, 'content', s)
    raise ValueError(s)

def cards():
    import make_product_blocks as M
    for k, src in CARDS.items():
        M.make_pc(k, src); print('pc-%s.jpg' % k)

def heroes():
    only = set(OPT['--only'].split(',')) if OPT.get('--only') else None
    for mail, (s, outs, head, sub, label, offer, ratio) in HERO.items():
        if only and mail not in only: continue
        src = src_path(s)
        if not os.path.exists(src): sys.exit('bron ontbreekt: %s' % src)
        for o in outs:
            cmd = [sys.executable, '-I', os.path.join(ROOT, 'scripts', 'make_hero.py'), src, os.path.join(V, o), head, sub, label]
            if offer: cmd.append('--offer=' + offer)
            if ratio: cmd.append('--ratio=' + ratio)
            r = subprocess.run(cmd, capture_output=True, text=True)
            if r.returncode: sys.exit('make_hero %s: %s' % (mail, r.stderr[-300:]))
            print(mail, '->', o, '(%d KB)' % (os.path.getsize(os.path.join(V, o)) // 1024))

if __name__ == '__main__':
    if '--cards' in OPT or '--heroes' not in OPT: cards()
    if '--heroes' in OPT or '--cards' not in OPT: heroes()
