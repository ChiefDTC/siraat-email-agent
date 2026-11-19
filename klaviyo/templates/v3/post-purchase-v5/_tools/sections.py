"""PP v5 · Post-purchase + delivery (draft, 19 nov 2026). Ontworpen beeldsecties (1200 breed), stijl van BF-W1 B en welcome v6d:
sfeerbeelden, getinte productkaarten met echte Photoroom-uitsneden en grondschaduw (v6d ground.py), gescheurde randen
(hergebruikt uit v6d), reviewkaarten, stappen met gouden cijfers. Typografie PLAYBOOK 13: koppen TT Ramillas Light Italic,
tekst Inter 400, labels Inter 600, vet alleen voor prijzen en heldencijfers; tekst in beeld minimaal 30 px (koppen 48+).
Geel #FFB800 alleen voor de kortingstag (DECISIONS 5 nov).
Gebruik: python3 -I _tools/cuts.py && python3 -I _tools/sections.py && node _tools/render.js
"""
import os, re, sys, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../..'))
V6D = os.path.join(REPO, 'klaviyo/templates/v3/welcome/v6d-envelope-rich')
PP = os.path.join(REPO, 'klaviyo/templates/v3/post-purchase')
sys.path.insert(0, os.path.join(V6D, '_tools')); sys.path.insert(0, os.path.dirname(__file__))
from hardshadow import hard  # noqa: E402  (harde schaduw, Floris 19 nov; ground.py niet meer gebruikt)
from catalog import CARDS, TINT  # noqa: E402
CUT = os.path.join(ROOT, 'gen/clean/')
SH = os.path.join(ROOT, 'gen/hard'); os.makedirs(SH, exist_ok=True)
FONT = os.path.join(REPO, 'klaviyo/fonts/TTRamillas-LightItalic.ttf')
OUT = os.path.join(ROOT, 'sections/src'); os.makedirs(OUT, exist_ok=True)
CREAM, SAND, DARK, BRICK, GOLD, W, INK, BODY, YEL, ESP = '#F8F7F2', '#ECE7DD', '#282828', '#AC3B19', '#B8862B', '#FFFFFF', '#272727', '#2E2E2E', '#FFB800', '#321E1D'
f = lambda p: 'file://' + p
c = lambda k: f(CUT + f'cut-{k}.png')
# 19 nov laat: Floris leverde zelf productfoto's met harde schaduw (brand/product-photos/2026-11-19-prio6). Die gaan voor op eigen uitsneden.
FL = os.path.join(REPO, 'brand/product-photos/2026-11-19-prio6/')
FLORIS = {'s12': '12-delige-set', 's06': '6-delige-set', 'std': 'pan-pro-standard', 'lrg': 'pan-pro-large', 'dep': 'deep-pan', 'wok': 'wok'}
FL2 = os.path.join(REPO, 'brand/product-photos/2026-11-19-prio-extra/')  # tweede levering Floris: Crepe, Pizza Steel, Roasting Pan (wit, multiply)
FLORIS2 = {'crp': ('crepe-pan_leeg_hard.png', ''), 'piz': ('pizza-steel_leeg_hard.png', ''), 'rst': ('roasting-pan_wit_hard.jpg', 'mix-blend-mode:multiply;'), 'brd': ('cutting-board_leeg_hard.png', ''), 'kn8': ('damascus-knives_leeg_hard.png', ''), 'lid': ('lid_leeg_hard.png', ''), 'ute': ('utensils_leeg_hard.png', ''), 'p22': ('2-pans-2-lids_leeg_hard.png', ''), 'e34': ('34-pcs_leeg_hard.png', ''), 'csp': ('cookware-set-pro_leeg_hard.png', ''), 'fhp': ('full-hammered-pro_leeg_hard.png', '')}
# Small en Mini: de foto van de Standard, kleiner afgebeeld (Floris 19 nov)
SMALLER = {'sml': .82, 'min': .68}
FLORIS.update({'sml': 'pan-pro-standard', 'min': 'pan-pro-standard'})
FLORIS.update({k: None for k in FLORIS2})
def pimg(key, cut, rot, mw, mh):
    if key in FLORIS2:
        fn, bl = FLORIS2[key]
        return f'<img src="{f(FL2 + fn)}" style="max-width:{mw}px;max-height:{mh}px;{bl}">'
    if key in FLORIS:
        sc = SMALLER.get(key, 1)
        return f'<img src="{f(FL + FLORIS[key] + "_leeg_hard.png")}" style="max-width:{int(mw*sc)}px;max-height:{int(mh*sc)}px">'
    return f'<img class="shadow" src="{c(cut)}" style="max-width:{mw}px;max-height:{mh}px;transform:rotate({rot}deg)">'

BASE = f'''<!doctype html><html><head><meta charset="utf-8">
<style>
@font-face{{font-family:Ramillas;src:url("{f(FONT)}");font-style:italic;font-weight:300;}}
*{{box-sizing:border-box;margin:0;padding:0}} body{{width:1200px;font-family:Inter,sans-serif;font-weight:400;-webkit-font-smoothing:antialiased;color:{BODY}}}
#s{{width:1200px;position:relative;overflow:hidden}}
.ram{{font-family:Ramillas,serif;font-style:italic;font-weight:300}}
.eb{{font-weight:600;letter-spacing:6px;font-size:30px;text-transform:uppercase}}
.num{{font-weight:800;letter-spacing:-2px}}
.tag{{display:inline-block;background:{YEL};color:{INK};font-weight:800;letter-spacing:2px;border-radius:14px;text-transform:uppercase}}
.was{{text-decoration:line-through;text-decoration-thickness:3px;color:#8A847A}}
</style></head><body><div id="s" style="__S__">__C__</div></body></html>'''
SECS = []
def _ground(m):
    src, st = m.group(1), m.group(2)
    r = re.search(r'transform:rotate\((-?[\d.]+)deg\);?', st); rot = float(r.group(1)) if r else 0
    st = re.sub(r'transform:rotate\([^)]*\);?', '', st)
    path = src.replace('file://', '')
    out = os.path.join(SH, os.path.basename(path)[:-4] + f'_{rot:g}.png')
    return f'<img src="file://{hard(path, rot, out)}" style="{st}">'
def sec(name, style, content):
    content = re.sub(r'<img class="shadow" src="([^"]+)" style="([^"]*)">', _ground, content)
    open(os.path.join(OUT, name + '.html'), 'w').write(BASE.replace('__S__', style).replace('__C__', content)); SECS.append(name)
def head(eb, title, col=INK, ebc=BRICK, size=100):
    return (f'<div class="eb" style="color:{ebc};text-align:center">{eb}</div>' if eb else '') + \
           f'<div class="ram" style="color:{col};font-size:{size}px;line-height:{int(size*1.06)}px;text-align:center;margin-top:16px">{title}</div>'

# ================= PP1 · bevestiging: armen met pannen op brick (zelfde beeld als BF-W1 B, andere boodschap)
for k, eb, t1, sub in (('first', 'Order confirmed', 'Good call.', 'Here is what happens next.'),
                       ('repeat', 'Order confirmed', 'Good to see you again.', 'Here is what happens next.')):
    sec(f'pp1-hero-{k}', f'background:{BRICK}', f'<div style="position:relative;height:1380px;background:url({f(V6D + "/gen/arms.png")}) center bottom/cover">'
        f'<div style="position:absolute;left:0;right:0;top:78px;text-align:center;color:{W}">'
        f'<div class="eb" style="color:#F3D2BF">{eb}</div>'
        f'<div class="ram" style="font-size:{150 if k == "first" else 118}px;line-height:1.02;margin-top:22px">{t1}</div>'
        f'<div style="font-size:46px;line-height:60px;margin-top:20px;color:#FBE9DF">{sub}</div></div></div>')

# PP1 · de ene tip (flash-foto ei) op crème
sec('pp1-tip', f'background:{CREAM};padding:70px 60px 64px', head('Before it arrives', 'Heat first.<br>Then oil. Then the egg.', size=92) +
    f'<div style="margin-top:44px;border-radius:40px;overflow:hidden;height:700px;background:url({f(V6D + "/gen/flash-egg.png")}) center/cover"></div>'
    f'<div style="display:flex;gap:26px;margin-top:44px">' + ''.join(
        f'<div style="flex:1;background:{W};border-radius:30px;padding:34px 26px;text-align:center"><div class="ram" style="font-size:88px;line-height:80px;color:{GOLD}">{n}</div>'
        f'<div style="font-weight:600;font-size:34px;line-height:44px;color:{INK};margin-top:14px">{t}</div><div style="font-size:30px;line-height:42px;color:#6F6A62;margin-top:8px">{s}</div></div>'
        for n, t, s in (('1', 'Medium heat', '2 to 3 minutes. Never higher.'), ('2', 'Water test', 'Drops bead up and glide.'), ('3', 'Then oil', 'A thin layer, then the egg.'))) + '</div>')

# PP1 · wat er nu gebeurt (zand, gouden cijfers)
NEXT = [('Packed with your 5 free gifts', 'Free shipping, the plastic-free e-book, the Favorites Cookbook, a mystery gift and your chance to win a PFAS water filter.'),
        ('Tracking by email', 'The link lands in your inbox the moment your order ships.'),
        ('The day it lands', 'We send the chef&rsquo;s first cook, five short steps. Keep it for your first morning.')]
sec('pp1-next', f'background:{SAND};padding:76px 70px 60px', head('What happens next', 'From order to first egg', size=92) +
    '<div style="margin-top:40px">' + ''.join(
        f'<div style="display:flex;gap:34px;align-items:flex-start;padding:30px 0;border-top:2px solid #D8D0C2">'
        f'<div class="ram" style="flex:none;width:90px;color:{GOLD};font-size:110px;line-height:96px;text-align:center">{i+1}</div>'
        f'<div style="flex:1"><div style="font-weight:600;font-size:42px;line-height:52px;color:{INK}">{t}</div><div style="font-size:34px;line-height:50px;color:#6F6A62;margin-top:6px">{s}</div></div></div>'
        for i, (t, s) in enumerate(NEXT)) + '</div>')

# ================= PP2 · getailorde upsell: bovenste aanbod (VS 12-Pcs, rest 6-Pcs), zelfde kaart als BF-W1 B
def top(name, title, cut, rot, maxw, pname, sub, price_html):
    sec(name, f'background:{SAND};padding:76px 50px 44px', head('A thank-you for your order', title) +
        f'<div style="position:relative;margin-top:44px;background:#FBF7F0;border-radius:44px;box-shadow:0 10px 30px rgba(60,40,20,.07);padding:56px 50px 60px;text-align:center">'
        f'<div class="tag" style="position:absolute;left:44px;top:40px;font-size:40px;padding:14px 26px">15% OFF</div>'
        f'<div style="height:560px;display:flex;align-items:center;justify-content:center;padding-top:40px">' + pimg(cut, cut, rot, maxw, 520) + '</div>'
        f'<div style="font-weight:600;font-size:52px;line-height:60px;color:{INK};margin-top:26px">{pname}</div>'
        f'<div style="font-size:36px;line-height:50px;color:#6F6A62;margin-top:10px">{sub}</div>' + price_html + '</div>')
top('pp2-top12', 'The rest of the kitchen', 's12', -3, 900, 'Cookware Set, 12 Pcs', '3 pans, 3 pots and 6 lids',
    f'<div style="margin-top:30px;display:flex;align-items:baseline;justify-content:center;gap:26px"><span class="was" style="font-size:46px">$2,047</span><span style="font-size:52px;color:#6F6A62">$649</span>'
    f'<span class="num" style="font-size:150px;line-height:150px;color:{INK};letter-spacing:-5px">$551.65</span></div>'
    f'<div style="font-weight:600;font-size:30px;letter-spacing:5px;color:{BRICK};margin-top:8px">WITH YOUR CODE VIP15-PICKS</div>')
top('pp2-top6', 'Three pans, three lids', 's06', -4, 860, 'Pan Set, 6 Pcs', 'Mini, Small and Large, each with a fitted lid',
    f'<div class="num" style="font-size:150px;line-height:160px;color:{INK};letter-spacing:-5px;margin-top:24px">15% OFF</div>'
    f'<div style="font-weight:600;font-size:30px;letter-spacing:5px;color:{BRICK};margin-top:4px">WITH YOUR CODE VIP15-PICKS</div>')
sec('pp2-h-viewed', f'background:{CREAM};padding:70px 70px 34px', head('You had a look at these', 'Same code, 15% off each', size=88))
sec('pp4-h-next', f'background:{CREAM};padding:70px 70px 34px', head('Picked for your kitchen', 'What owners add next', size=88))

# ================= productkaart-bovenkant (gedeeld door PP2 en PP4): getinte kaart met afgeronde bovenhoeken, uitsnede met grondschaduw.
# Naam, prijs en knop staan live eronder in dezelfde tint (build.py), dus dynamisch per markt en per code.
for k, (cut, rot, mw, mh) in CARDS.items():
    bundle = os.path.exists(CUT + f'bundle-{k}.png')  # samengestelde bundel: schaduw zit al per onderdeel in het beeld
    img = (pimg(k, cut, rot, mw, mh) if k in FLORIS else f'<img src="{f(CUT + f"bundle-{k}.png")}" style="max-width:{mw}px;max-height:{mh}px">' if bundle else
           pimg(k, cut, rot, mw, mh))
    sec(f'card-{k}', f'background:{CREAM};padding:20px 40px 0', f'<div style="background:{TINT[k]};border-radius:40px 40px 0 0;height:680px;display:flex;align-items:center;justify-content:center;padding:46px 40px 18px">'
        + img + '</div>')

# ================= reviewkaarten (letterlijk uit content/reviews/reviews.csv, gecontroleerd in build.py)
def review(name, quotes, bg=CREAM, eb='In their words', title='100,000+ happy customers'):
    cards = ''.join(f'<div style="background:{W};border-radius:36px;padding:44px 50px;margin-top:30px;display:flex;gap:34px;align-items:flex-start">'
                    f'<div class="ram" style="flex:none;width:96px;height:96px;border-radius:50%;background:#F3E3D3;color:{BRICK};font-size:62px;line-height:96px;text-align:center">{n[0]}</div>'
                    f'<div><div style="color:{BRICK};font-size:34px;letter-spacing:6px">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
                    f'<div style="font-size:38px;line-height:54px;color:{INK};margin-top:12px">&ldquo;{q}&rdquo;</div>'
                    f'<div style="font-size:30px;line-height:40px;color:#8A847A;margin-top:14px">{n} &middot; Verified buyer</div></div></div>' for n, q in quotes)
    sec(name, f'background:{bg};padding:70px 60px 60px', f'<div style="color:{BRICK};font-size:44px;letter-spacing:10px;text-align:center">&#9733;&#9733;&#9733;&#9733;&#9733;</div>' + head('', title, size=84) + cards)
REV = json.load(open(os.path.join(os.path.dirname(__file__), 'reviews.json')))
for k, v in REV.items():
    review(f'rev-{k}', [(x['name'], x['quote']) for x in v['quotes']], title=v['title'])

# ================= PP3 · eerste gebruik: hero ei-foto, vijf stappen donker, deksel
for k, eb, t in (('delivered', 'It&rsquo;s here', 'Your first egg,<br>step by step'), ('safe', 'For your first cook', 'Your first egg,<br>step by step')):
    sec(f'pp3-hero-{k}', f'background:{CREAM}', f'<div style="height:805px;background:url({f(V6D + "/gen/egg.jpg")}) center/cover"></div>'
        f'<div style="padding:64px 60px 30px">' + head(eb, t, size=104) + '</div>')
STEPS = [('Preheat on medium, 2 to 3 minutes', 'Medium on titanium works like high on a normal pan. You never need to go higher.'),
         ('Do the water test', 'Flick in a few drops. When they bead up and glide, the pan is ready.'),
         ('Add a thin layer of oil', 'First heat, then oil. Always into a hot pan, never a cold one.'),
         ('Eggs: turn the heat down to low', 'Once the white sets, it lets go by itself. Then it slides.'),
         ('Meat and fish: lay it down, then leave it', 'It holds on at first, then forms a crust and lets go on its own.')]
sec('pp3-steps', f'background:{DARK};padding:76px 70px 60px;color:{W}', head('The chef&rsquo;s first cook', 'Cold metal grabs.<br>Hot metal lets go.', W, '#E7C988', 96) +
    '<div style="margin-top:40px">' + ''.join(
        f'<div style="display:flex;gap:34px;align-items:flex-start;padding:28px 0;border-top:2px solid #44403C">'
        f'<div class="ram" style="flex:none;width:90px;color:{GOLD};font-size:110px;line-height:96px;text-align:center">{i+1}</div>'
        f'<div style="flex:1"><div style="font-weight:600;font-size:40px;line-height:50px">{t}</div><div style="font-size:34px;line-height:50px;color:#CFC8BC;margin-top:6px">{s}</div></div></div>'
        for i, (t, s) in enumerate(STEPS)) + '</div>')

# ================= PP4 · sfeerbeeld (shoot-foto, flash-stijl) met kop
sec('pp4-hero', f'background:{CREAM}', f'<div style="height:1000px;background:url({f(PP + "/assets/src/friends-greeting-v5-crop-no-saucepan.jpg")}) center 30%/cover"></div>'
    f'<div style="padding:64px 60px 24px">' + head('Three weeks in', 'The pieces owners<br>add next', size=104) + '</div>')

json.dump(SECS, open(os.path.join(OUT, 'list.json'), 'w'))
print(len(SECS), 'sections')
