"""v6c: ontworpen beeldsecties (1200 px breed) als HTML/CSS, gerenderd met Playwright (_tools/render.js) naar JPG q80.
Gebruik: python3 -I _tools/sections.py && node _tools/render.js
Copy, prijzen en aanbod komen uit v6b (klaviyo/flows/welcome-v6b-envelope-dr.md). Shopify-prijzen 17 nov 2026, US.
Leesbaarheid op 390 px (factor 0.325): koppen >= 48 px, lopende tekst in beeld >= 32 px op het 1200-canvas.
"""
import os, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../../..'))
SCR = '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad'
ENV = SCR + '/envelope-assets/'
PROD = os.path.join(ROOT, '../v6b-envelope-dr/assets/')
SEAL = os.path.join(ROOT, '../v6-envelope/assets/v6e-m2-seal.jpg')
FONT = os.path.join(REPO, 'klaviyo/fonts/TTRamillas-LightItalic.ttf')
OUT = os.path.join(ROOT, 'sections/src'); os.makedirs(OUT, exist_ok=True)

CREAM, SAND, DARK, BRICK, ORANGE, GOLD, W, INK = '#F8F7F2', '#ECE7DD', '#282828', '#AC3B19', '#C4642C', '#B8862B', '#FFFFFF', '#272727'
GIFTS = '5 free gifts with every order'
PR = {'mini': ('Pan Pro Mini', '8&Prime; &middot; 20 cm', 129), 'small': ('Pan Pro Small', '10&Prime; &middot; 26 cm', 137),
      'standard': ('Pan Pro Standard', '11&Prime; &middot; 28 cm', 144), 'large': ('Pan Pro Large', '12&Prime; &middot; 30 cm', 149),
      'set6': ('6-Piece Set', 'Mini, Small, Large + 3 lids', 299), 'set12': ('12-Piece Set', '3 pans, 3 pots, 6 lids', 649),
      'duo': ('2 Pans + 2 Lids', '2 hammered pans + 2 lids', 199), 'roast': ('Roasting Pan', 'V-rack included', 199), 'lid': ('Fitted Lid', 'Mini to Large', 59)}
def d(n): return f'${n:,.0f}' if n == int(n) else f'${n:,.2f}'
def hi(n): return d(round(n * 0.9, 2))
f = lambda p: 'file://' + p

BASE = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Ramillas;src:url("{f(FONT)}");font-style:italic;font-weight:300;}}
*{{box-sizing:border-box;margin:0;padding:0}} body{{width:1200px;font-family:Inter,sans-serif;-webkit-font-smoothing:antialiased}}
#s{{width:1200px;position:relative;overflow:hidden}}
.ram{{font-family:Ramillas,serif;font-style:italic;font-weight:300}}
.eyebrow{{font-weight:800;letter-spacing:7px;font-size:30px;text-transform:uppercase}}
.pill{{display:inline-block;border-radius:999px;font-weight:800;letter-spacing:2px}}
</style></head><body><div id="s" style="__S__">__C__</div></body></html>'''
SECS = []
def sec(name, style, content):
    open(os.path.join(OUT, name + '.html'), 'w').write(BASE.replace('__S__', style).replace('__C__', content)); SECS.append(name)

# ---------- torn-paper strips (kleur boven -> kleur onder), SVG met grillig pad
import random
def torn(top, bot, seed=1, h=56):
    random.seed(seed); pts = []; x = 0
    while x < 1200:
        pts.append(f'{x},{random.randint(18, h - 16)}'); x += random.randint(7, 19)
    pts.append(f'1200,{random.randint(18, h - 16)}')
    path = 'M0,0 L' + ' L'.join(pts) + f' L1200,0 Z'
    shadow = 'M0,0 L' + ' L'.join(p.split(',')[0] + ',' + str(int(p.split(',')[1]) + 5) for p in pts) + ' L1200,0 Z'
    name = f'torn-{top[1:]}-{bot[1:]}'
    sec(name, f'height:{h}px;background:{bot}', f'<svg width="1200" height="{h}" viewBox="0 0 1200 {h}" style="display:block"><path d="{shadow}" fill="#000" opacity="0.10"/><path d="{path}" fill="{top}"/></svg>')
    return name
for i, (a, b) in enumerate([(CREAM, DARK), (DARK, SAND), (SAND, BRICK), (BRICK, CREAM), (CREAM, SAND), (SAND, DARK), (DARK, CREAM), (CREAM, BRICK), (SAND, CREAM), (DARK, BRICK), (BRICK, SAND), (DARK, ORANGE), (ORANGE, CREAM)]):
    torn(a, b, seed=i + 3)

# ---------- hero's: foto full-bleed, grote kop ingebakken
def hero(name, img, eyebrow, l1, l2, sub, dark=True, pos='center', h=1250, badge=None, align='flex-start', imgh=600):
    """Tekstblok op effen kleur boven, foto full-bleed eronder met zachte overgang; badge rechtsonder op de foto."""
    bg = DARK if dark else CREAM; col = W if dark else INK
    rgb = '40,40,40' if dark else '248,247,242'
    b = (f'<div style="position:absolute;right:60px;bottom:60px;background:{BRICK};color:{W};padding:30px 44px;border-radius:24px;box-shadow:0 18px 40px rgba(0,0,0,.3);text-align:center">'
         f'<div style="font-weight:900;font-size:120px;line-height:110px;letter-spacing:-3px">{badge[0]}</div><div style="font-weight:800;font-size:34px;letter-spacing:3px;margin-top:10px">{badge[1]}</div></div>') if badge else ''
    sec(name, f'background:{bg}', f'<div style="padding:80px 70px 40px;color:{col};text-align:center"><div class="eyebrow" style="color:{GOLD if not dark else "#E7C988"}">{eyebrow}</div>'
        f'<div class="ram" style="font-size:150px;line-height:146px;margin-top:26px;letter-spacing:-2px">{l1}<br>{l2}</div>'
        f'<div style="font-size:44px;line-height:58px;font-weight:600;margin:30px auto 0;max-width:960px">{sub}</div></div>'
        f'<div style="position:relative;height:{imgh}px;background:url({f(img)}) {pos}/cover"><div style="position:absolute;left:0;right:0;top:0;height:200px;background:linear-gradient(180deg,rgba({rgb},1),rgba({rgb},0))"></div>{b}</div>')

hero('e1-hero', ENV + 'siraat-03-front-sand-line.jpg', 'Your welcome envelope is open', 'Take 10% off', 'your first pan.', 'Code HI10 works on everything, sets included.', dark=False, pos='center 55%', badge=('10% OFF', '+ 5 FREE GIFTS'))
hero('e2-hero', ENV + 'siraat-05-sand-path-dark.jpg', 'The pan nobody else was making', 'The original', 'hammered pan.', 'First orders shipped December 20, 2024. Look-alikes came after.', pos='center', h=1150)
hero('e3-hero', ENV + 'siraat-02-front-dark.jpg', 'Report no. 25895', 'Tested for', '31 PFAS.', 'Every one below the detection limit. Read the paper, not the label.', pos='center 60%', h=1200, badge=('31', 'PFAS COMPOUNDS TESTED'))
hero('e4-hero', ENV + 'siraat-07-kitchen-counter.jpg', 'Your envelope', 'Still', 'sealed?', 'Your 10% hasn&rsquo;t been used yet.', pos='center 62%', h=1300)

# ---------- stappen (donker), grote cijfers
steps = [('Pick your pan or set', 'Start with the one you cook with most.'), ('HI10 is applied', 'The button adds your 10%. Or type HI10 at checkout.'), ('Gifts ship with it', '5 free gifts go in the same box.')]
sec('e1-steps', f'background:{DARK};padding:70px 70px 76px', f'<div class="eyebrow" style="color:#E7C988;text-align:center">How it works</div><div class="ram" style="color:{W};font-size:110px;line-height:110px;text-align:center;margin-top:14px">Three steps.</div>'
    '<div style="display:flex;gap:30px;margin-top:44px">' + ''.join(
        f'<div style="flex:1;background:#353332;border-radius:28px;padding:44px 34px 50px;text-align:center"><div class="ram" style="color:{GOLD};font-size:190px;line-height:170px">{i+1}</div>'
        f'<div style="color:{W};font-weight:800;font-size:40px;line-height:48px;margin-top:20px">{t}</div><div style="color:#CFC8BC;font-size:32px;line-height:42px;margin-top:14px">{s}</div></div>' for i, (t, s) in enumerate(steps)) + '</div>')

# ---------- paneelkoppen
def head(name, bg, eyebrow, title, col=INK, ebcol=BRICK, pad='70px 70px 30px'):
    sec(name, f'background:{bg};padding:{pad};text-align:center', f'<div class="eyebrow" style="color:{ebcol}">{eyebrow}</div><div class="ram" style="color:{col};font-size:104px;line-height:108px;margin-top:16px">{title}</div>')
head('h-bestsellers', SAND, 'Start here', 'Our bestsellers,<br>with your 10%')
head('h-start', SAND, 'Most picked', 'Where most<br>people start')
head('h-tested', SAND, 'One tested pan', 'Start with one pan')
head('h-sizes', SAND, 'Size chooser', 'Which size is yours?')

# ---------- productkaarten (580 breed, ronde witte kaart op zandpaneel), 2 per rij in de mail
def card(k, tag=None, bg=SAND):
    n, sz, p = PR[k]
    t = f'<div class="pill" style="position:absolute;left:34px;top:34px;background:{INK};color:{W};font-size:26px;padding:12px 22px">{tag}</div>' if tag else ''
    sec('card-' + k, f'width:600px;height:880px;background:{bg};padding:10px', f'<div style="position:relative;width:580px;height:860px;background:{W};border-radius:36px;box-shadow:0 10px 24px rgba(0,0,0,.06);text-align:center;overflow:hidden">{t}'
        f'<img src="{f(PROD + "v6b-" + k + ".jpg")}" style="width:430px;height:430px;object-fit:cover;margin-top:50px;border-radius:20px">'
        f'<div style="font-weight:800;font-size:46px;line-height:52px;color:{INK};margin-top:20px">{n}</div><div style="font-size:30px;color:#8A847A;margin-top:6px">{sz}</div>'
        f'<div style="margin-top:20px;font-size:34px;color:#6F6A62">{d(p)} &nbsp;&rarr;&nbsp; <span style="font-weight:900;font-size:66px;color:{INK};letter-spacing:-1px">{hi(p)}</span></div><div style="font-weight:800;font-size:26px;letter-spacing:4px;color:{BRICK};margin-top:2px">WITH HI10</div>'
        f'<div class="pill" style="margin-top:16px;background:{BRICK};color:{W};font-size:30px;padding:20px 44px">GET 10% OFF &rarr;</div></div>')
    SECS[-1] = 'card-' + k
for k, tag in [('standard', 'BESTSELLER'), ('set6', 'BEST VALUE'), ('duo', None), ('roast', None), ('set12', 'WHOLE KITCHEN'), ('large', None)]:
    card(k, tag)

# ---------- maatkiezer: 4 tegels 2x2 (580 breed), Standard gemarkeerd
def size(k, label, who, top=False):
    n, sz, p = PR[k]; bd = BRICK if top else W
    t = f'<div class="pill" style="position:absolute;left:50%;transform:translateX(-50%);top:26px;background:{BRICK};color:{W};font-size:26px;padding:10px 24px;white-space:nowrap">MOST PICKED</div>' if top else ''
    sec('size-' + k, f'width:600px;height:760px;background:{SAND};padding:10px', f'<div style="position:relative;width:580px;height:740px;background:{W};border-radius:36px;border:6px solid {bd};text-align:center">{t}'
        f'<img src="{f(PROD + "v6b-" + k + ".jpg")}" style="width:330px;height:330px;object-fit:cover;margin-top:70px;border-radius:16px">'
        f'<div style="font-weight:900;font-size:58px;color:{INK};margin-top:8px">{label}</div><div style="font-size:32px;color:#8A847A">{sz} &middot; {who}</div>'
        f'<div style="margin-top:14px;font-size:32px;color:#6F6A62">{d(p)} &rarr; <span style="font-weight:900;font-size:56px;color:{INK}">{hi(p)}</span></div></div>')
for k, l, w, t in [('mini', 'Mini', 'eggs for one', False), ('small', 'Small', 'sides for two', False), ('standard', 'Standard', '2 to 4', True), ('large', 'Large', 'a family', False)]:
    size(k, l, w, t)

# ---------- bundel op brick: $293 SAVED
items = [('Pan Pro Mini 8&Prime;', 129), ('Pan Pro Small 10&Prime;', 137), ('Pan Pro Large 12&Prime;', 149), ('3 fitted lids', 177)]
def bundle(name, eyebrow, title):
    li = ''.join(f'<div style="display:flex;justify-content:space-between;font-size:36px;line-height:46px;padding:12px 0;border-bottom:2px solid rgba(255,255,255,.22)"><span>{a}</span><span>{d(b)}</span></div>' for a, b in items)
    sec(name, f'background:{BRICK};padding:70px 70px 50px;color:{W}', f'<div class="eyebrow" style="color:#F3D2BF;text-align:center">{eyebrow}</div><div class="ram" style="font-size:96px;line-height:100px;text-align:center;margin-top:14px">{title}</div>'
        f'<div style="text-align:center;margin-top:30px"><span style="font-weight:900;font-size:220px;line-height:200px;letter-spacing:-6px">$293</span><div style="font-weight:900;font-size:64px;letter-spacing:10px;margin-top:8px">SAVED</div></div>'
        f'<div style="display:flex;gap:44px;margin-top:56px;align-items:center"><img src="{f(PROD + "v6b-set6.jpg")}" style="width:420px;height:420px;border-radius:30px;object-fit:cover">'
        f'<div style="flex:1">{li}<div style="display:flex;justify-content:space-between;font-size:36px;margin-top:16px;opacity:.85"><span>Bought one by one</span><span>$592</span></div>'
        f'<div style="display:flex;justify-content:space-between;font-size:50px;font-weight:900;margin-top:10px"><span>The set</span><span>$299</span></div></div></div>'
        f'<div style="margin-top:50px;background:{W};color:{INK};border-radius:28px;padding:34px;text-align:center;font-size:42px;line-height:54px">With HI10: <b style="font-size:60px">$269.10</b><br><span style="font-size:34px;color:#6F6A62">about $90 a pan, lid included</span></div>')
bundle('e1-bundle', 'Most popular upgrade', 'Most people pick<br>the 6-piece set')
bundle('e3-bundle', 'Or the whole stove', '3 pans + 3 lids')

# ---------- reviews (crème), 2 kaarten, quote >= 34 px
R = {'tammy': ('I am on my 4th pan from Siraat... I even gifted one to my son, and he says it&rsquo;s the best pan he owns.', 'Tammy'),
     'sunny': ('I ordered one pan to try it out. I&rsquo;m so glad I did. I am so happy with this pan that I&rsquo;m ordering the set.', 'Sunny C.'),
     'michael': ('The real test was my egg the next morning... the egg released completely and slid around the pan like it was non-stick.', 'Michael G.'),
     'thomas': ('This pan is fantastic. Makes all of our others &ldquo;non stick&rdquo; seem really sticky.', 'Thomas D.'),
     'carole': ('I&rsquo;ve been cooking for well over 60 years... This Siraat pan has been the absolute best I&rsquo;ve ever used.', 'Carole'),
     'graham': ('We cooked the best omelette we have ever eaten when we used the pan for the first time.', 'Graham C.'),
     'fatima': ('...I thought it was just marketing hype... I ended up buying the whole collection.', 'Fatima'),
     'brandon': ('Siraat replaced a pan free of charge... I just sent them the picture and they honored the warranty.', 'Brandon W.')}
def reviews(name, keys, bg=CREAM, title='100,000+ happy customers', dark=False):
    c = W if dark else INK; cb = '#353332' if dark else W; qc = W if dark else INK
    sec(name, f'background:{bg};padding:80px 70px 80px', f'<div style="text-align:center;color:{BRICK if not dark else "#E7C988"};font-size:64px;letter-spacing:10px">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
        f'<div class="ram" style="color:{c};font-size:96px;line-height:100px;text-align:center;margin-top:10px">{title}</div>' + ''.join(
        f'<div style="background:{cb};border-radius:30px;padding:44px 50px;margin-top:36px;box-shadow:0 8px 20px rgba(0,0,0,.05)"><div style="color:{BRICK if not dark else "#E7C988"};font-size:40px;letter-spacing:6px">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
        f'<div style="color:{qc};font-size:42px;line-height:56px;font-weight:600;margin-top:14px">&ldquo;{R[k][0]}&rdquo;</div><div style="color:#8A847A;font-size:32px;margin-top:16px">{R[k][1]} &middot; Verified buyer</div></div>' for k in keys))
reviews('e1-reviews', ['tammy', 'sunny'])
reviews('e2-reviews', ['carole', 'graham'])
reviews('e3-reviews', ['michael', 'thomas'], bg=DARK, title='The egg test', dark=True)
reviews('e4-reviews', ['fatima', 'brandon'], title='In their words')

# ---------- verhaal (crème) met zegel
sec('e2-story', f'background:{CREAM};padding:90px 70px 90px', f'<div style="display:flex;gap:56px;align-items:center"><img src="{f(SEAL)}" style="width:400px;height:400px;border-radius:50%;object-fit:cover;box-shadow:0 20px 40px rgba(0,0,0,.15)">'
    f'<div style="flex:1"><div class="eyebrow" style="color:{BRICK}">The name on the seal</div><div class="ram" style="font-size:92px;line-height:96px;color:{INK};margin-top:14px">Siraat: from sirat, the Arabic word for path.</div></div></div>'
    + ''.join(f'<div style="display:flex;gap:28px;align-items:flex-start;margin-top:44px"><div style="width:22px;height:22px;border-radius:50%;background:{GOLD};margin-top:16px;flex:none"></div><div style="font-size:40px;line-height:54px;color:{INK}">{t}</div></div>'
              for t in ['<b>The path to a non-toxic life,</b> one step at a time.', 'We started with titanium cutting boards. Then we made the pan: <b>a pure titanium cooking surface, no coatings.</b>', '<b>Nothing on it to wear off.</b> That is why every pan is covered for 75 years.']))

# ---------- value stack (donker)
vs = [('Pan Pro Standard 11&Prime;', '$144'), ('5 free gifts', '$555 value'), ('75-year warranty', 'Included'), ('30-day returns', 'Included')]
sec('e2-stack', f'background:{DARK};padding:90px 70px 60px;color:{W}', f'<div class="eyebrow" style="color:#E7C988;text-align:center">Everything you get</div><div class="ram" style="font-size:100px;line-height:104px;text-align:center;margin-top:14px">One pan. A lot more.</div>'
    + ''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;font-size:44px;padding:30px 0;border-bottom:2px solid #44403C"><span><span style="color:#E7C988;font-weight:900">&#10003;</span>&nbsp; {a}</span><span style="font-weight:800">{b}</span></div>' for a, b in vs)
    + f'<div style="font-size:32px;line-height:44px;color:#BDB5A8;margin-top:20px">Gifts: free shipping, e-book, mystery gift, cookbook and a weekly chance to win a PFAS water filter.</div>'
    + f'<div style="text-align:center;margin-top:50px;font-size:46px">Your price</div><div style="text-align:center;font-weight:900;font-size:170px;line-height:170px;letter-spacing:-4px">$129.60</div><div style="text-align:center;font-weight:800;font-size:34px;letter-spacing:6px;color:#E7C988">WITH HI10</div>')

# ---------- bewijs: 31 / 0 / 75 + vergelijking
sec('e3-stats', f'background:{CREAM};padding:90px 50px 70px', '<div style="display:flex;text-align:center">' + ''.join(
    f'<div style="flex:1"><div style="font-weight:900;font-size:200px;line-height:190px;color:{BRICK};letter-spacing:-6px">{a}</div><div style="font-size:36px;line-height:46px;color:{INK};margin-top:10px;font-weight:600">{b}</div></div>'
    for a, b in [('31', 'PFAS compounds<br>tested'), ('0', 'above the<br>detection limit'), ('75', 'year<br>warranty')]) + '</div>'
    f'<div style="text-align:center;font-size:36px;line-height:50px;color:#5E5A54;margin-top:50px">Light Labs, an ISO/IEC 17025-accredited lab.<br><b style="color:{INK}">Report no. 25895, read it yourself.</b></div>')
rows = [('Pure titanium surface', 'A coating on top'), ('No coating to wear off', 'Coating wears with use'), ('Metal utensils welcome', 'Wood or silicone advised'), ('Dishwasher safe', 'Hand wash advised'), ('Lab report no. 25895', 'Testing varies by brand')]
sec('e3-compare', f'background:{SAND};padding:90px 60px 90px', f'<div class="eyebrow" style="color:{BRICK};text-align:center">Side by side</div><div class="ram" style="font-size:100px;line-height:104px;color:{INK};text-align:center;margin-top:14px">Siraat vs a<br>PFAS-coated pan</div>'
    f'<div style="margin-top:50px;border-radius:30px;overflow:hidden;background:{W}"><div style="display:flex;font-weight:800;font-size:34px;letter-spacing:3px"><div style="flex:1;background:{INK};color:{W};padding:30px 34px">SIRAAT</div><div style="flex:1;background:#DCD4C6;color:{INK};padding:30px 34px">A PFAS-COATED PAN</div></div>'
    + ''.join(f'<div style="display:flex;font-size:36px;line-height:46px;border-top:2px solid {SAND}"><div style="flex:1;padding:28px 34px;color:{INK}"><b style="color:{BRICK}">&#10003;</b>&nbsp; {a}</div><div style="flex:1;padding:28px 34px;background:#F3F0EA;color:#5E5A54"><b style="color:#9A948B">&#10005;</b>&nbsp; {b}</div></div>' for a, b in rows) + '</div>')

# ---------- bezwaren (donker)
OBJ = [('Will food stick?', 'Not when the pan is hot. <b>Medium heat for 2 to 3 minutes</b>, a teaspoon of oil, and eggs slide. Skip the heat, and it sticks.'),
       ('Does it work on induction?', '<b>Yes.</b> Induction, gas, electric and ceramic. Dishwasher safe, metal utensils welcome.'),
       ('What if I don&rsquo;t like it?', '<b>30-day returns.</b> Send it back unused within 30 days of delivery for a full refund.')]
sec('e4-objections', f'background:{DARK};padding:90px 70px 90px;color:{W}', f'<div class="eyebrow" style="color:#E7C988;text-align:center">Quick answers</div><div class="ram" style="font-size:100px;line-height:104px;text-align:center;margin-top:14px">Before you open it</div>'
    + ''.join(f'<div style="background:#353332;border-radius:30px;padding:44px 50px;margin-top:34px;border-left:14px solid {ORANGE}"><div style="font-weight:900;font-size:50px;line-height:58px">{q}</div><div style="font-size:38px;line-height:52px;color:#DDD6CB;margin-top:14px">{a}</div></div>' for q, a in OBJ))

# ---------- E4 complete the set (oranje accent)
sec('e4-complete', f'background:{ORANGE};padding:80px 70px 60px;color:{W}', f'<div style="display:flex;gap:50px;align-items:center"><img src="{f(PROD + "v6b-set6.jpg")}" style="width:430px;height:430px;border-radius:30px;object-fit:cover">'
    f'<div style="flex:1"><div class="eyebrow" style="color:#FBE3D2">Complete the set</div><div class="ram" style="font-size:92px;line-height:96px;margin-top:14px">3 pans + 3 lids instead of one pan.</div></div></div>'
    f'<div style="display:flex;justify-content:center;align-items:baseline;gap:30px;margin-top:50px"><span style="font-weight:900;font-size:180px;line-height:170px;letter-spacing:-5px">$293</span><span style="font-weight:900;font-size:60px;letter-spacing:8px">SAVED</span></div>'
    f'<div style="text-align:center;font-size:40px;line-height:54px;margin-top:10px">versus buying them one by one. <b>$299, or $269.10 with HI10.</b></div>')

# ---------- E5 recap (donker): groot 10% OFF + 3 mini-kaarten
mini = ''.join(f'<div style="flex:1;background:{W};border-radius:30px;padding:26px 16px 34px;text-align:center"><img src="{f(PROD + "v6b-" + k + ".jpg")}" style="width:300px;height:300px;object-fit:cover;border-radius:16px">'
               f'<div style="font-weight:800;font-size:38px;line-height:44px;color:{INK};margin-top:12px">{PR[k][0]}</div><div style="font-size:32px;color:#8A847A;margin-top:6px">{d(PR[k][2])}</div><div style="font-weight:900;font-size:54px;color:{INK}">{hi(PR[k][2])}</div></div>'
               for k in ['standard', 'set6', 'set12'])
sec('e5-recap', f'background:{DARK};padding:90px 50px 70px;color:{W};text-align:center', f'<div class="eyebrow" style="color:#E7C988">Your offer, in one place</div>'
    f'<div style="font-weight:900;font-size:230px;line-height:220px;letter-spacing:-7px;margin-top:20px">10% OFF</div><div style="font-size:46px;line-height:60px;margin-top:6px">+ {GIFTS}<br><span style="color:#BDB5A8">75-year warranty &middot; 30-day returns</span></div>'
    f'<div style="display:flex;gap:24px;margin-top:60px">{mini}</div>')

json.dump(SECS, open(os.path.join(OUT, 'list.json'), 'w'))
print(len(SECS), 'sections')
