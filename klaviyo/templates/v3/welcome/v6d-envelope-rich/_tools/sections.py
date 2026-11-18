"""v6d 'Rich detail': ontworpen beeldsecties (1200 px) met echte productfoto's, Higgsfield-beelden en uitsneden.
Typografie-baseline (PLAYBOOK, 17 nov): koppen TT Ramillas Light Italic (nooit vet), tekst Inter 400, labels Inter 600,
knoppen Inter 600; vet/zwaar alleen voor prijzen, de code en grote heldencijfers.
Gebruik: python3 -I _tools/sections.py && node _tools/render.js   (GIF: _tools/make_gif.py)
Beelden in gen/: Higgsfield gpt_image_2_6 (arms, coated, flash-egg, flatlay, egg) en remove_background (cut-*), gift-* uit de gift-blokken.
"""
import os, json, random
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../../..'))
ENV = '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/envelope-assets/'
GEN = os.path.join(ROOT, 'gen/')
FONT = os.path.join(REPO, 'klaviyo/fonts/TTRamillas-LightItalic.ttf')
OUT = os.path.join(ROOT, 'sections/src'); os.makedirs(OUT, exist_ok=True)
CREAM, SAND, DARK, BRICK, ORANGE, GOLD, W, INK, BODY = '#F8F7F2', '#ECE7DD', '#282828', '#AC3B19', '#C4642C', '#B8862B', '#FFFFFF', '#272727', '#2E2E2E'
GIFTS = '5 free gifts with every order'
PR = {'mini': ('Pan Pro Mini', '8&Prime; &middot; 20 cm', 129), 'small': ('Pan Pro Small', '10&Prime; &middot; 26 cm', 144),
      'standard': ('Pan Pro Standard', '11&Prime; &middot; 28 cm', 149), 'large': ('Pan Pro Large', '12&Prime; &middot; 30 cm', 154),
      'set6': ('6-Piece Set', 'Mini, Small, Large + 3 lids', 299), 'set12': ('12-Piece Set', '3 pans, 3 pots, 6 lids', 699),
      'duo': ('2 Pans + 2 Lids', '2 hammered pans + 2 lids', 199), 'roast': ('Roasting Pan', 'V-rack included', 199)}
CUT = {'standard': 'cut-standard', 'large': 'cut-standard', 'small': 'cut-standard', 'mini': 'cut-mini', 'set6': 'cut-set6', 'set12': 'cut-set12', 'duo': 'cut-duo', 'roast': 'cut-roast'}
def d(n): return f'${n:,.0f}' if n == int(n) else f'${n:,.2f}'
def hi(n): return d(round(n * 0.9, 2))
f = lambda p: 'file://' + p
g = lambda n: f(GEN + n)

BASE = f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Homemade+Apple&display=block" rel="stylesheet">
<style>
@font-face{{font-family:Ramillas;src:url("{f(FONT)}");font-style:italic;font-weight:300;}}
*{{box-sizing:border-box;margin:0;padding:0}} body{{width:1200px;font-family:Inter,sans-serif;font-weight:400;-webkit-font-smoothing:antialiased;color:{BODY}}}
#s{{width:1200px;position:relative;overflow:hidden}}
.ram{{font-family:Ramillas,serif;font-style:italic;font-weight:300}}
.eb{{font-weight:600;letter-spacing:6px;font-size:30px;text-transform:uppercase}}
.btn{{display:inline-block;border-radius:999px;font-weight:600;letter-spacing:3px;text-transform:uppercase}}
.num{{font-weight:800;letter-spacing:-2px}}
</style></head><body><div id="s" style="__S__">__C__</div></body></html>'''
SECS = []
import re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ground import ground
SH = os.path.join(GEN, 'sh'); os.makedirs(SH, exist_ok=True)
def _ground(m):
    # schaduw op de ondergrond onder elke productuitsnede (Floris 18 nov: anders lijkt het te zweven); draaiing zit in de PNG
    src, st = m.group(1), m.group(2)
    r = re.search(r'transform:rotate\((-?[\d.]+)deg\);?', st); rot = float(r.group(1)) if r else 0
    st = re.sub(r'transform:rotate\([^)]*\);?|transform-origin:[^;"]*;?', '', st)
    path = src.replace('file://', '')
    out = os.path.join(SH, os.path.basename(path)[:-4] + f'_{rot:g}.png')
    return f'<img src="file://{ground(path, rot, out)}" style="{st}">'
def sec(name, style, content):
    content = re.sub(r'<img class="shadow" src="([^"]+)" style="([^"]*)">', _ground, content)
    open(os.path.join(OUT, name + '.html'), 'w').write(BASE.replace('__S__', style).replace('__C__', content)); SECS.append(name)
def head(eb, title, col=INK, ebc=BRICK, size=100):
    return f'<div class="eb" style="color:{ebc};text-align:center">{eb}</div><div class="ram" style="color:{col};font-size:{size}px;line-height:{int(size*1.04)}px;text-align:center;margin-top:14px">{title}</div>'

# ---------- torn-paper strips
def torn(top, bot, seed, h=56):
    random.seed(seed); pts = []; x = 0
    while x < 1200: pts.append((x, random.randint(18, h - 16))); x += random.randint(7, 19)
    pts.append((1200, random.randint(18, h - 16)))
    P = lambda dy: 'M0,0 L' + ' L'.join(f'{a},{b + dy}' for a, b in pts) + ' L1200,0 Z'
    sec(f'torn-{top[1:]}-{bot[1:]}', f'height:{h}px;background:{bot}', f'<svg width="1200" height="{h}" style="display:block"><path d="{P(5)}" fill="#000" opacity="0.10"/><path d="{P(0)}" fill="{top}"/></svg>')
for i, (a, b) in enumerate([(CREAM, DARK), (DARK, SAND), (SAND, BRICK), (BRICK, CREAM), (CREAM, SAND), (SAND, DARK), (DARK, CREAM), (CREAM, BRICK), (SAND, CREAM), (DARK, BRICK), (BRICK, SAND), (DARK, ORANGE), (ORANGE, CREAM), (BRICK, DARK)]):
    torn(a, b, i + 3)

# ---------- hero's E2-E4 (tekst op effen vlak, foto eronder), sub Inter 400
def hero(name, img, eb, l1, l2, sub, pos='center', imgh=600, badge=None):
    bd = (f'<div style="position:absolute;right:60px;bottom:56px;background:{BRICK};color:{W};padding:28px 40px;border-radius:24px;box-shadow:0 18px 40px rgba(0,0,0,.3);text-align:center">'
          f'<div class="num" style="font-size:120px;line-height:110px">{badge[0]}</div><div style="font-weight:600;font-size:30px;letter-spacing:4px;margin-top:10px">{badge[1]}</div></div>') if badge else ''
    sec(name, f'background:{DARK}', f'<div style="padding:80px 70px 40px;color:{W};text-align:center"><div class="eb" style="color:#E7C988">{eb}</div>'
        f'<div class="ram" style="font-size:150px;line-height:146px;margin-top:26px;letter-spacing:-2px">{l1}<br>{l2}</div>'
        f'<div style="font-size:42px;line-height:60px;margin:28px auto 0;max-width:960px;color:#E8E2D8">{sub}</div></div>'
        f'<div style="position:relative;height:{imgh}px;background:url({f(img)}) {pos}/cover"><div style="position:absolute;left:0;right:0;top:0;height:200px;background:linear-gradient(180deg,rgba(40,40,40,1),rgba(40,40,40,0))"></div>{bd}</div>')
hero('e2-hero', ENV + 'siraat-05-sand-path-dark.jpg', 'The pan nobody else was making', 'The original', 'hammered pan.', 'First orders shipped December 20, 2024. Look-alikes came after.')
hero('e3-hero', ENV + 'siraat-02-front-dark.jpg', 'Report no. 25895', 'Tested for', '31 PFAS.', 'Every one below the detection limit. Read the paper, not the label.', pos='center 60%', badge=('31', 'PFAS COMPOUNDS TESTED'))
hero('e4-hero', GEN + 'kitchen-counter-seal-fixed.jpg', 'Your envelope', 'Still', 'sealed?', 'Your 10% hasn&rsquo;t been used yet.', pos='center 62%', imgh=640)

# ---------- E1 stappen (donker)
steps = [('Pick your pan or set', 'Start with the one you cook with most.'), ('HI10 is applied', 'The button adds your 10%, or type HI10 at checkout.'), ('Gifts ship with it', '5 free gifts go in the same box.')]
sec('e1-steps', f'background:{DARK};padding:70px 60px 76px', head('How it works', 'Three steps.', W, '#E7C988', 104) + '<div style="display:flex;gap:26px;margin-top:44px">' + ''.join(
    f'<div style="flex:1;background:#353332;border-radius:28px;padding:40px 30px 46px;text-align:center"><div class="ram" style="color:{GOLD};font-size:180px;line-height:160px">{i+1}</div>'
    f'<div style="color:{W};font-weight:600;font-size:38px;line-height:46px;margin-top:18px">{t}</div><div style="color:#CFC8BC;font-size:32px;line-height:44px;margin-top:12px">{s}</div></div>' for i, (t, s) in enumerate(steps)) + '</div>')

# ---------- paneelkoppen
for n, eb, t, bg in [('h-bestsellers', 'Start here', 'Our bestsellers,<br>with your 10%', SAND), ('h-start', 'Most picked', 'Where most<br>people start', SAND)]:
    sec(n, f'background:{bg};padding:70px 70px 26px', head(eb, t))

# ---------- productkaarten: uitsnede schuin met schaduw op getint paneel
TINT = {'standard': '#F3E3D3', 'set6': '#E4E7DF', 'duo': '#EFE6DA', 'roast': '#E8E1EA', 'set12': '#E4E7DF', 'large': '#F3E3D3'}
def card(k, tag=None):
    n, sz, p = PR[k]; rot = {'set6': -4, 'set12': -3, 'roast': -6}.get(k, -12)
    t = f'<div class="btn" style="position:absolute;left:34px;top:34px;background:{INK};color:{W};font-size:28px;padding:12px 22px;letter-spacing:3px">{tag}</div>' if tag else ''
    sec('card-' + k, f'width:600px;height:900px;background:{SAND};padding:12px', f'<div style="position:relative;width:576px;height:876px;background:{TINT[k]};border-radius:40px;text-align:center;overflow:hidden">{t}'
        f'<div style="height:470px;display:flex;align-items:center;justify-content:center;padding:60px 30px 0"><img class="shadow" src="{g(CUT[k] + ".png")}" style="max-width:470px;max-height:380px;transform:rotate({rot}deg)"></div>'
        f'<div style="font-weight:600;font-size:42px;line-height:50px;color:{INK};margin-top:6px">{n}</div><div style="font-size:30px;color:#7A746B;margin-top:4px">{sz}</div>'
        f'<div style="margin-top:18px;font-size:32px;color:#6F6A62">{d(p)} &nbsp;&rarr;&nbsp; <span class="num" style="font-size:64px;color:{INK}">{hi(p)}</span></div>'
        f'<div style="font-weight:600;font-size:28px;letter-spacing:4px;color:{BRICK};margin-top:2px">WITH HI10</div>'
        f'<div class="btn" style="margin-top:20px;background:{INK};color:{W};font-size:30px;padding:20px 44px">Get 10% off &rarr;</div></div>')
for k, tag in [('standard', 'BESTSELLER'), ('set6', 'BEST VALUE'), ('duo', None), ('roast', None), ('set12', 'WHOLE KITCHEN'), ('large', None)]:
    card(k, tag)

# ---------- bundel (brick) met uitsnede set
items = [('Pan Pro Mini 8&Prime;', 129), ('Pan Pro Small 10&Prime;', 144), ('Pan Pro Large 12&Prime;', 154), ('3 fitted lids', 177)]
def bundle(name, eb, title):
    li = ''.join(f'<div style="display:flex;justify-content:space-between;font-size:36px;line-height:46px;padding:12px 0;border-bottom:2px solid rgba(255,255,255,.22)"><span>{a}</span><span>{d(b)}</span></div>' for a, b in items)
    sec(name, f'background:{BRICK};padding:70px 70px 56px;color:{W}', head(eb, title, W, '#F3D2BF', 96) +
        f'<div style="display:flex;align-items:center;gap:30px;margin-top:30px"><div style="flex:1.1;text-align:center"><img class="shadow" src="{g("cut-set6.png")}" style="width:560px;transform:rotate(-5deg)"></div>'
        f'<div style="flex:1;text-align:center"><div class="num" style="font-size:210px;line-height:190px;letter-spacing:-6px">$305</div><div style="font-weight:600;font-size:52px;letter-spacing:12px;margin-top:6px">SAVED</div></div></div>'
        f'<div style="margin-top:34px">{li}<div style="display:flex;justify-content:space-between;font-size:36px;margin-top:14px;opacity:.85"><span>Bought one by one</span><span>$604</span></div>'
        f'<div style="display:flex;justify-content:space-between;font-size:46px;margin-top:8px"><span>The set</span><span class="num" style="letter-spacing:0">$299</span></div></div>'
        f'<div style="margin-top:40px;background:{W};color:{INK};border-radius:28px;padding:30px;text-align:center;font-size:40px;line-height:54px">With HI10: <span class="num" style="font-size:60px;letter-spacing:0">$269.10</span><br><span style="font-size:32px;color:#6F6A62">about $90 a pan, lid included</span></div>')
bundle('e1-bundle', 'Most popular upgrade', 'Most people pick<br>the 6-piece set')
bundle('e3-bundle', 'Or the whole stove', '3 pans + 3 lids')

# ---------- gifts flat-lay (Higgsfield-achtergrond + echte gift-beelden)
gp = [('gift-cookbook-cut.png', 'Favorites Cookbook', 560, 40, -5, 250), ('gift-ebook-cut.png', 'Plastic-free e-book', 880, 50, 5, 250), ('gift-mystery-cut.png', 'Mystery gift', 560, 470, 3, 250),
      ('gift-filter-cut.png', 'Chance to win a PFAS water filter', 870, 460, -2, 240)]
items_html = ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w+40}px;text-align:center"><img class="shadow" src="{g(fn)}" style="width:{w}px;max-height:290px;object-fit:contain;transform:rotate({r}deg)"><div style="margin-top:14px;font-weight:600;font-size:30px;line-height:34px;color:{INK};background:rgba(248,247,242,.92);display:inline-block;padding:8px 16px;border-radius:12px">{lab}</div></div>' for fn, lab, x, y, r, w in gp)
sec('gifts-flatlay', f'background:{SAND}', f'<div style="padding:70px 70px 30px">{head("In the box with every order", "5 free gifts")}</div>'
    f'<div style="position:relative;height:870px;background:url({g("flatlay.png")}) center/cover">{items_html}'
    f'<div style="position:absolute;left:70px;top:520px;font-weight:600;font-size:30px;color:{INK};background:rgba(248,247,242,.92);padding:8px 16px;border-radius:12px">Free shipping</div></div>')

# ---------- reviewkaarten als beeld
R = {'tammy': ('I am on my 4th pan from Siraat... I even gifted one to my son, and he says it&rsquo;s the best pan he owns.', 'Tammy', 'Pan Pro'),
     'sunny': ('I ordered one pan to try it out. I&rsquo;m so glad I did. I am so happy with this pan that I&rsquo;m ordering the set.', 'Sunny C.', 'Verified order'),
     'michael': ('The real test was my egg the next morning... the egg released completely and slid around the pan like it was non-stick.', 'Michael G.', 'Pan Pro'),
     'thomas': ('This pan is fantastic. Makes all of our others &ldquo;non stick&rdquo; seem really sticky.', 'Thomas D.', 'Pan Pro'),
     'carole': ('I&rsquo;ve been cooking for well over 60 years... This Siraat pan has been the absolute best I&rsquo;ve ever used.', 'Carole', 'Pan Pro'),
     'graham': ('We cooked the best omelette we have ever eaten when we used the pan for the first time.', 'Graham C.', 'Pan Pro'),
     'fatima': ('...I thought it was just marketing hype... I ended up buying the whole collection.', 'Fatima', 'Set'),
     'brandon': ('Siraat replaced a pan free of charge... I just sent them the picture and they honored the warranty.', 'Brandon W.', 'Pan Pro')}
def reviews(name, keys, title, bg=CREAM, dark=False, prod='standard'):
    cb, qc, st, tc = ('#353332', '#F1ECE4', '#E7C988', W) if dark else (W, BODY, BRICK, INK)
    cards = ''.join(f'<div style="display:flex;gap:30px;align-items:center;background:{cb};border-radius:32px;padding:40px 44px;margin-top:30px;box-shadow:0 8px 22px rgba(0,0,0,.06)">'
                    f'<div style="flex:none;width:150px;height:150px;border-radius:50%;background:{"#46423E" if dark else "#F3EEE6"};display:flex;align-items:center;justify-content:center;font-family:Ramillas,serif;font-style:italic;font-size:80px;color:{st}">{R[k][1][0]}</div>'
                    f'<div style="flex:1"><div style="color:{st};font-size:36px;letter-spacing:6px">&#9733;&#9733;&#9733;&#9733;&#9733;</div><div style="color:{qc};font-size:38px;line-height:54px;margin-top:10px">&ldquo;{R[k][0]}&rdquo;</div>'
                    f'<div style="font-size:30px;color:#8A847A;margin-top:12px"><span style="font-weight:600;color:{tc}">{R[k][1]}</span>{(" &middot; " + R[k][2]) if R[k][2] != "Verified order" else ""} &middot; <span style="color:{"#7FB08A" if dark else "#3F7A4E"}">&#10003; Verified buyer</span></div></div></div>' for k in keys)
    sec(name, f'background:{bg};padding:70px 60px 70px', f'<div style="text-align:center;color:{st};font-size:56px;letter-spacing:10px">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
        f'<div class="ram" style="color:{tc};font-size:92px;line-height:98px;text-align:center;margin-top:8px">{title}</div>{cards}')
reviews('e1-reviews', ['tammy', 'sunny'], '100,000+ happy customers')
reviews('e2-reviews', ['carole', 'graham'], '100,000+ happy customers')
reviews('e3-reviews', ['michael', 'thomas'], 'The egg test', bg=DARK, dark=True)
reviews('e4-reviews', ['fatima', 'brandon'], 'In their words')

# ---------- E2 verhaal met flash-foto
sec('e2-story', f'background:{CREAM}', f'<img src="{g("flash-egg.png")}" style="display:block;width:1200px;height:760px;object-fit:cover;object-position:center 40%">'
    f'<div style="padding:60px 80px 70px">{head("The name on the seal", "Siraat: from sirat,<br>the Arabic word for path.", size=88)}'
    + ''.join(f'<div style="display:flex;gap:26px;align-items:flex-start;margin-top:36px"><div style="width:20px;height:20px;border-radius:50%;background:{GOLD};margin-top:18px;flex:none"></div><div style="font-size:38px;line-height:58px">{t}</div></div>'
              for t in ['The path to a non-toxic life, one step at a time.', 'We started with titanium cutting boards. Then we made the pan: <b style="font-weight:600">a pure titanium cooking surface, no coatings.</b>', 'Nothing on it to wear off. That is why every pan is covered for 75 years.']) + '</div>')

# ---------- E2 maatlijn op schaal (diameter 20/26/28/30 cm; ei ~5,7 cm) met prijs
SC = 9.0  # px per cm: kombreedte in de uitsnede ~ beeldbreedte; ei ~5,7 cm
def lineup():
    cols = ''
    for k, lab, cm, who in [('mini', 'Mini', 20, 'eggs for one'), ('small', 'Small', 26, 'sides for two'), ('standard', 'Standard', 28, 'everyday, 2 to 4'), ('large', 'Large', 30, 'a family')]:
        n, sz, p = PR[k]; w = int(cm * SC)
        mark = f'<div class="btn" style="background:{BRICK};color:{W};font-size:28px;padding:8px 16px;letter-spacing:2px;margin-top:10px">MOST PICKED</div>' if k == 'standard' else '<div style="height:44px;margin-top:10px"></div>'
        cols += (f'<div style="width:{w + 20}px;text-align:center;display:flex;flex-direction:column;align-items:center"><div style="height:420px;display:flex;align-items:flex-end;justify-content:center">'
                 f'<img class="shadow" src="{g(CUT[k] + ".png")}" style="width:{w}px;transform:rotate(-33deg);transform-origin:50% 75%"></div>'
                 f'<div style="font-weight:600;font-size:38px;color:{INK};margin-top:26px">{lab}</div><div style="font-size:30px;color:#7A746B;margin-top:2px;white-space:nowrap">{sz}</div><div style="font-size:30px;color:#7A746B;white-space:nowrap">{who}</div>'
                 f'<div style="font-size:30px;color:#6F6A62;margin-top:10px">{d(p)}</div><div class="num" style="font-size:48px;color:{INK};letter-spacing:-1px">{hi(p)}</div>{mark}</div>')
    egg = f'<div style="width:90px;text-align:center;display:flex;flex-direction:column;align-items:center"><div style="height:420px;display:flex;align-items:flex-end"><img class="shadow" src="{g("cut-egg.png")}" style="width:{int(5.7 * SC)}px"></div><div style="font-size:28px;line-height:28px;color:#8A847A;margin-top:26px">egg,<br>to scale</div></div>'
    sec('e2-sizes', f'background:{SAND};padding:70px 30px 60px', head('Size chooser, to scale', 'Which size is yours?') +
        f'<div style="display:flex;justify-content:center;align-items:flex-start;gap:34px;margin-top:20px">{egg}{cols}</div>'
        f'<div style="text-align:center;font-size:30px;color:#7A746B;margin-top:26px">Price with HI10 in bold. Same titanium cooking surface on every size.</div>')
lineup()

# ---------- E3 anatomie: grote heldenfoto met dunne lijnen
PX, PY, PW = 250, 110, 700; PH = int(PW * 1336 / 1402)
pt = lambda fx, fy: (int(PX + fx * PW), int(PY + fy * PH))
labels = [('No coating to wear off', 40, 500, (300, 522), pt(0.08, 0.62)), ('Pure titanium cooking surface', 40, 700, (300, 722), pt(0.45, 0.75)),
          ('Hammered texture', 920, 450, (910, 472), pt(0.66, 0.62)), ('Works on induction, gas and electric', 920, 760, (910, 782), pt(0.55, 0.96))]
lines = ''.join(f'<line x1="{a[0]}" y1="{a[1]}" x2="{p[0]}" y2="{p[1]}" stroke="{INK}" stroke-width="2"/><circle cx="{p[0]}" cy="{p[1]}" r="10" fill="{W}" stroke="{BRICK}" stroke-width="5"/>' for t, lx, ly, a, p in labels)
labs = ''.join(f'<div style="position:absolute;left:{lx}px;top:{ly}px;width:250px;font-size:32px;line-height:42px;color:{INK}">{t}</div>' for t, lx, ly, a, p in labels)
sec('e3-anatomy', f'background:{CREAM};padding:70px 0 30px', f'<div style="padding:0 70px">{head("Up close", "What you&rsquo;re paying for")}</div>'
    f'<div style="position:relative;height:{PY + PH + 110}px"><img class="shadow" src="{g("cut-standard.png")}" style="position:absolute;left:{PX - int(PW * 112 / 1402)}px;top:{PY}px;width:{int(PW * 1626 / 1402)}px">'
    f'<svg width="1200" height="{PY + PH + 110}" style="position:absolute;left:0;top:0">{lines}</svg>{labs}</div>')

# ---------- E3 vergelijking met foto's
rows = [('Pure titanium surface', 'A coating on top'), ('No coating to wear off', 'Coating wears with use'), ('Metal utensils welcome', 'Wood or silicone advised'), ('Dishwasher safe', 'Hand wash advised'), ('Lab report no. 25895', 'Testing varies by brand')]
sec('e3-compare', f'background:{SAND};padding:70px 60px 70px', head('Side by side', 'Siraat vs a<br>PFAS-coated pan') +
    f'<div style="margin-top:44px;border-radius:30px;overflow:hidden;background:{W}"><div style="display:flex">'
    f'<div style="flex:1;background:{W};padding:30px 20px 20px;text-align:center"><div style="height:330px;display:flex;align-items:center;justify-content:center"><img class="shadow" src="{g("cut-standard.png")}" style="max-width:360px;max-height:300px"></div><div style="font-weight:600;font-size:30px;letter-spacing:4px;color:{INK};margin-top:10px">SIRAAT PAN PRO</div></div>'
    f'<div style="flex:1;background:#E4DED3;padding:30px 20px 20px;text-align:center"><div style="height:330px;display:flex;align-items:center;justify-content:center;overflow:hidden"><img src="{g("coated.png")}" style="width:380px;height:330px;object-fit:cover;border-radius:20px;mix-blend-mode:multiply"></div><div style="font-weight:600;font-size:30px;letter-spacing:4px;color:{INK};margin-top:10px">A PFAS-COATED PAN</div></div></div>'
    + ''.join(f'<div style="display:flex;font-size:34px;line-height:44px;border-top:2px solid {SAND}"><div style="flex:1;padding:26px 34px;color:{INK}"><span style="color:{BRICK};font-weight:600">&#10003;</span>&nbsp; {a}</div><div style="flex:1;padding:26px 34px;background:#F3F0EA;color:#5E5A54"><span style="color:#9A948B">&#10005;</span>&nbsp; {b}</div></div>' for a, b in rows) + '</div>'
    f'<div style="text-align:center;font-size:30px;color:#7A746B;margin-top:22px">Illustration of a typical worn coated pan. No brand shown.</div>')

# ---------- E2 value stack (donker)
vs = [('Pan Pro Standard 11&Prime;', '$149'), ('5 free gifts', '$555 value'), ('75-year warranty', 'Included'), ('30-day returns', 'Included')]
sec('e2-stack', f'background:{DARK};padding:70px 70px 56px;color:{W}', head('Everything you get', 'One pan. A lot more.', W, '#E7C988') +
    f'<div style="display:flex;gap:40px;align-items:center;margin-top:30px"><img class="shadow" src="{g("cut-standard.png")}" style="width:380px;transform:rotate(-14deg)"><div style="flex:1">'
    + ''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;font-size:36px;padding:22px 0;border-bottom:2px solid #44403C"><span><span style="color:#E7C988">&#10003;</span>&nbsp; {a}</span><span style="font-weight:600">{b}</span></div>' for a, b in vs) + '</div></div>'
    + f'<div style="font-size:30px;line-height:40px;color:#BDB5A8;margin-top:18px">Gifts: free shipping, e-book, mystery gift, cookbook and a weekly chance to win a PFAS water filter.</div>'
    + f'<div style="text-align:center;margin-top:40px;font-size:40px;color:#E8E2D8">Your price</div><div class="num" style="text-align:center;font-size:160px;line-height:160px;letter-spacing:-4px">$134.10</div><div style="text-align:center;font-weight:600;font-size:30px;letter-spacing:6px;color:#E7C988">WITH HI10</div>')

# ---------- E4 bezwaren (donker), oranje rand
OBJ = [('Will food stick?', 'Not when the pan is hot. Medium heat for 2 to 3 minutes, a teaspoon of oil, and eggs slide. Skip the heat, and it sticks.'),
       ('Does it work on induction?', 'Yes. Induction, gas, electric and ceramic. Dishwasher safe, metal utensils welcome.'),
       ('What if I don&rsquo;t like it?', '30-day returns. Send it back unused within 30 days of delivery for a full refund.')]
sec('e4-objections', f'background:{DARK};padding:70px 70px 76px;color:{W}', head('Quick answers', 'Before you open it', W, '#E7C988') + ''.join(
    f'<div style="background:#353332;border-radius:30px;padding:40px 46px;margin-top:30px;border-left:12px solid {ORANGE}"><div class="ram" style="font-size:62px;line-height:68px">{q}</div><div style="font-size:36px;line-height:52px;color:#DDD6CB;margin-top:12px">{a}</div></div>' for q, a in OBJ))

# ---------- E4 complete the set (oranje)
sec('e4-complete', f'background:{ORANGE};padding:70px 70px 56px;color:{W}', head('Complete the set', '3 pans + 3 lids<br>instead of one pan', W, '#FBE3D2', 92) +
    f'<div style="display:flex;align-items:center;gap:20px;margin-top:20px"><div style="flex:1.2;text-align:center"><img class="shadow" src="{g("cut-set6.png")}" style="width:600px;transform:rotate(-4deg)"></div>'
    f'<div style="flex:1;text-align:center"><div class="num" style="font-size:190px;line-height:180px;letter-spacing:-5px">$305</div><div style="font-weight:600;font-size:48px;letter-spacing:10px">SAVED</div></div></div>'
    f'<div style="text-align:center;font-size:38px;line-height:54px;margin-top:20px">versus buying them one by one. $299, or <span class="num" style="letter-spacing:0">$269.10</span> with HI10.</div>')

# ---------- E5 brief op papier (boven en onder als beeld, tekst live) + armen + recap
PAPER = '#FBF8F1'
sec('e5-paper-top', f'background:{CREAM};padding:60px 50px 0', f'<div style="background:{PAPER};height:250px;border-radius:6px 6px 0 0;box-shadow:0 -2px 18px rgba(0,0,0,.06);padding:70px 80px 0;position:relative">'
    f'<div class="eb" style="color:{GOLD}">A note from Benjamin</div><div style="height:2px;width:160px;background:#D2B25C;margin-top:30px"></div>'
    f'<img src="{f(os.path.join(ROOT, "../v6-envelope/assets/v6e-m2-seal.jpg"))}" style="position:absolute;right:80px;top:50px;width:150px;height:150px;border-radius:50%;object-fit:cover"></div>')
sec('e5-paper-sign', f'background:{CREAM};padding:0 50px 60px', f'<div style="background:{PAPER};height:300px;border-radius:0 0 6px 6px;box-shadow:0 14px 22px rgba(0,0,0,.07);padding:20px 80px 0">'
    f'<div style="font-family:\'Homemade Apple\',cursive;font-size:84px;line-height:130px;color:#2B3A55;transform:rotate(-4deg);transform-origin:left">Benjamin</div>'
    f'<div style="font-size:32px;color:#6F6A62;margin-top:10px">Founder, Siraat</div></div>')
sec('e5-arms', f'background:{BRICK}', f'<div style="position:relative;height:1500px;background:url({g("arms.png")}) center bottom/cover">'
    f'<div style="position:absolute;left:0;right:0;top:80px;text-align:center;color:{W}"><div class="eb" style="color:#F3D2BF">Your offer, in one place</div>'
    f'<div class="num" style="font-size:240px;line-height:220px;letter-spacing:-8px;margin-top:20px">10% OFF</div><div style="font-size:44px;line-height:60px;margin-top:10px">every pan and every set, with HI10<br>+ {GIFTS}</div></div></div>')
def mini(k):  # losse kaart per product, zodat elke kaart naar zijn eigen productpagina linkt
    return (f'<div style="background:{TINT[k]};border-radius:30px;padding:30px 14px 34px;text-align:center"><div style="height:240px;display:flex;align-items:center;justify-content:center"><img class="shadow" src="{g(CUT[k] + ".png")}" style="max-width:300px;max-height:220px;transform:rotate(-8deg)"></div>'
            f'<div style="font-weight:600;font-size:36px;line-height:42px;color:{INK};margin-top:14px">{PR[k][0]}</div><div style="font-size:30px;color:#7A746B;margin-top:6px">{d(PR[k][2])}</div><div class="num" style="font-size:52px;color:{INK};letter-spacing:-1px">{hi(PR[k][2])}</div></div>')
sec('e5-recap-top', f'width:1200px;background:{DARK};padding:60px 20px 36px', f'<div style="font-size:36px;color:#E8E2D8;text-align:center">75-year warranty &middot; 30-day returns &middot; free shipping</div>')
for i, k in enumerate(['standard', 'set6', 'set12']):
    sec('e5-recap-' + k, f'width:400px;background:{DARK};padding:0 20px 50px', mini(k))
json.dump(SECS, open(os.path.join(OUT, 'list.json'), 'w'))
print(len(SECS), 'sections')
