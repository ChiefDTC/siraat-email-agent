"""BF-W1 B · 12pcs top (19 nov 2026, kopie van bf-w1-image-b): bf-duo vervangen door bf-top12 (VS) en bf-top6 (rest), plus card-standard-wide voor de niet-VS-tak.
Origineel: BF-W1 image B (18 nov 2026): beeldgedreven B-variant van de BFCM Welcome-mail BF-W1 (A = template XXg4sn).
Zelfde aanbod en prijzen als A, geen nep-urgentie. Aanpak en beelden uit welcome v6d (v3/welcome/v6d-envelope-rich):
uitsneden met grondschaduw (ground.py), getinte productkaarten, gescheurde randen, armen-beeld, gifts flat-lay, reviewkaarten.
Typografie PLAYBOOK §13: koppen TT Ramillas Light Italic, tekst Inter 400, labels en knoppen Inter 600, vet alleen voor prijzen
en heldencijfers. Geel #FFB800 alleen voor sale-tags (DECISIONS 5 nov).
Gebruik: python3 -I _tools/sections.py && node _tools/render.js
"""
import os, re, sys, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../../..'))
V6D = os.path.join(REPO, 'klaviyo/templates/v3/welcome/v6d-envelope-rich')
sys.path.insert(0, os.path.join(V6D, '_tools'))
from ground import ground  # noqa: E402
GEN = os.path.join(V6D, 'gen/')
SH = os.path.join(ROOT, 'gen/sh'); os.makedirs(SH, exist_ok=True)
FONT = os.path.join(REPO, 'klaviyo/fonts/TTRamillas-LightItalic.ttf')
OUT = os.path.join(ROOT, 'sections/src'); os.makedirs(OUT, exist_ok=True)
CREAM, SAND, DARK, BRICK, GOLD, W, INK, BODY, YEL = '#F8F7F2', '#ECE7DD', '#282828', '#AC3B19', '#B8862B', '#FFFFFF', '#272727', '#2E2E2E', '#FFB800'
f = lambda p: 'file://' + p
g = lambda n: f(GEN + n)

BASE = f'''<!doctype html><html><head><meta charset="utf-8">
<style>
@font-face{{font-family:Ramillas;src:url("{f(FONT)}");font-style:italic;font-weight:300;}}
*{{box-sizing:border-box;margin:0;padding:0}} body{{width:1200px;font-family:Inter,sans-serif;font-weight:400;-webkit-font-smoothing:antialiased;color:{BODY}}}
#s{{width:1200px;position:relative;overflow:hidden}}
.ram{{font-family:Ramillas,serif;font-style:italic;font-weight:300}}
.eb{{font-weight:600;letter-spacing:6px;font-size:30px;text-transform:uppercase}}
.btn{{display:inline-block;border-radius:999px;font-weight:600;letter-spacing:3px;text-transform:uppercase}}
.num{{font-weight:800;letter-spacing:-2px}}
.tag{{display:inline-block;background:{YEL};color:{INK};font-weight:800;letter-spacing:2px;border-radius:14px;text-transform:uppercase}}
.was{{text-decoration:line-through;text-decoration-thickness:3px;color:#8A847A}}
</style></head><body><div id="s" style="__S__">__C__</div></body></html>'''
SECS = []
def _ground(m):
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

# ---------- hero: armen met pannen op brick, aanbod bovenin (geen deadline)
sec('bf-hero', f'background:{BRICK}', f'<div style="position:relative;height:1500px;background:url({g("arms.png")}) center bottom/cover">'
    f'<div style="position:absolute;left:0;right:0;top:64px;text-align:center;color:{W}">'
    f'<div class="eb" style="color:#F3D2BF">Black Friday sale is live</div>'
    f'<div style="font-weight:600;font-size:48px;letter-spacing:10px;margin-top:26px">UP TO</div>'
    f'<div class="num" style="font-size:250px;line-height:220px;letter-spacing:-8px;margin-top:6px">70% OFF</div>'
    f'<div style="font-size:46px;line-height:62px;margin-top:18px">No code needed.<br>5 free gifts with every order.</div></div></div>')

# ---------- uitgelicht bovenaan (19 nov): VS = 12-Pcs set, rest = 6-Pcs set (zelfde kaart als de oude bf-duo)
def top(name, title, cut, rot, maxw, tag, pname, sub, was, now):
    sec(name, f'background:{SAND};padding:76px 50px 40px', head('Start here', title) +
        f'<div style="position:relative;margin-top:44px;background:#FBF7F0;border-radius:44px;box-shadow:0 10px 30px rgba(60,40,20,.07);padding:56px 50px 60px;text-align:center">'
        f'<div class="tag" style="position:absolute;left:44px;top:40px;font-size:40px;padding:14px 26px">{tag}</div>'
        f'<div style="height:560px;display:flex;align-items:center;justify-content:center;padding-top:40px"><img class="shadow" src="{g(cut)}" style="max-width:{maxw}px;max-height:520px;transform:rotate({rot}deg)"></div>'
        f'<div style="font-weight:600;font-size:52px;line-height:60px;color:{INK};margin-top:26px">{pname}</div>'
        f'<div style="font-size:36px;line-height:50px;color:#6F6A62;margin-top:10px">{sub}</div>'
        f'<div style="margin-top:30px;display:flex;align-items:baseline;justify-content:center;gap:30px"><span class="was" style="font-size:52px">{was}</span><span class="num" style="font-size:150px;line-height:150px;color:{INK};letter-spacing:-5px">{now}</span></div>'
        f'<div style="font-weight:600;font-size:30px;letter-spacing:5px;color:{BRICK};margin-top:6px">BLACK FRIDAY PRICE &middot; NO CODE</div></div>')
top('bf-top12', 'The complete kitchen', 'cut-set12.png', -3, 900, '68% OFF', 'Cookware Set, 12 Pcs', '3 pans, 3 pots and 6 lids', '$2,047', '$649')
top('bf-top6', 'Three pans, three lids', 'cut-set6.png', -4, 860, '70% OFF', 'Pan Set, 6 Pcs', '3 pans and 3 fitted lids', '$997', '$299')

# ---------- kop boven de kaarten
sec('bf-h-more', f'background:{SAND};padding:56px 70px 20px', head('The rest of the sale', 'Pick your pan<br>or your whole kitchen', size=92))

# ---------- productkaarten (zelfde stramien als v6d card(), maar BF-prijs zonder code)
PR = {'standard': ('Pan Pro Standard', '11&Prime; &middot; 28 cm', 480, 149, '#F3E3D3', 'cut-standard.png', -12),
      'set6': ('Pan Set, 6 Pcs', '3 pans + 3 fitted lids', 997, 299, '#E4E7DF', 'cut-set6.png', -4),
      'set12': ('Cookware Set, 12 Pcs', '3 pans, 3 pots, 6 lids', 2047, 649, '#E8E1EA', 'cut-set12.png', -3)}
pct = lambda was, now: round(100 * (1 - now / was))  # 68,96 -> 69; 62,5 -> 62
def card(k, cta):
    n, sz, was, now, tint, cut, rot = PR[k]
    sec('card-' + k, f'width:600px;height:900px;background:{SAND};padding:12px', f'<div style="position:relative;width:576px;height:876px;background:{tint};border-radius:40px;text-align:center;overflow:hidden">'
        f'<div class="tag" style="position:absolute;left:30px;top:30px;font-size:30px;padding:10px 20px">{pct(was, now)}% OFF</div>'
        f'<div style="height:480px;display:flex;align-items:center;justify-content:center;padding:80px 30px 0"><img class="shadow" src="{g(cut)}" style="max-width:480px;max-height:370px;transform:rotate({rot}deg)"></div>'
        f'<div style="font-weight:600;font-size:42px;line-height:50px;color:{INK};margin-top:6px">{n}</div><div style="font-size:30px;color:#7A746B;margin-top:4px">{sz}</div>'
        f'<div style="margin-top:18px;display:flex;align-items:baseline;justify-content:center;gap:18px"><span class="was" style="font-size:34px">${was:,}</span><span class="num" style="font-size:80px;line-height:84px;color:{INK}">${now:,}</span></div>'
        f'<div class="btn" style="margin-top:24px;background:{INK};color:{W};font-size:28px;padding:20px 40px">{cta} &rarr;</div></div>')
card('standard', 'See the pan')
card('set6', 'See the set')
# 12-delig breed (1200), zodat de rij niet scheef loopt
n, sz, was, now, tint, cut, rot = PR['set12']
sec('card-set12-wide', f'background:{SAND};padding:12px 12px 50px', f'<div style="position:relative;background:{tint};border-radius:40px;display:flex;align-items:center;padding:44px 40px 44px 30px;gap:20px">'
    f'<div style="flex:1.15;text-align:center"><img class="shadow" src="{g(cut)}" style="width:600px;transform:rotate({rot}deg)"></div>'
    f'<div style="flex:1;text-align:center"><div class="tag" style="font-size:34px;padding:12px 22px;margin-bottom:26px">{pct(was, now)}% OFF</div><div class="eb" style="color:{BRICK};font-size:28px">The complete kitchen</div><div style="font-weight:600;font-size:46px;line-height:54px;color:{INK};margin-top:16px">{n}</div>'
    f'<div style="font-size:32px;color:#7A746B;margin-top:6px">{sz}</div><div class="was" style="font-size:40px;margin-top:22px">${was:,}</div><div class="num" style="font-size:120px;line-height:120px;color:{INK};letter-spacing:-4px">${now:,}</div>'
    f'<div class="btn" style="margin-top:22px;background:{INK};color:{W};font-size:28px;padding:20px 40px">See the set &rarr;</div></div></div>')

n, sz, was, now, tint, cut, rot = PR['standard']
sec('card-standard-wide', f'background:{SAND};padding:12px 12px 24px', f'<div style="position:relative;background:{tint};border-radius:40px;display:flex;align-items:center;padding:44px 40px 44px 30px;gap:20px">'
    f'<div style="flex:1.15;text-align:center"><img class="shadow" src="{g(cut)}" style="width:540px;transform:rotate({rot}deg)"></div>'
    f'<div style="flex:1;text-align:center"><div class="tag" style="font-size:34px;padding:12px 22px;margin-bottom:26px">{pct(was, now)}% OFF</div><div class="eb" style="color:{BRICK};font-size:28px">Our bestseller</div><div style="font-weight:600;font-size:46px;line-height:54px;color:{INK};margin-top:16px">{n}</div>'
    f'<div style="font-size:32px;color:#7A746B;margin-top:6px">{sz}</div><div class="was" style="font-size:40px;margin-top:22px">${was:,}</div><div class="num" style="font-size:120px;line-height:120px;color:{INK};letter-spacing:-4px">${now:,}</div>'
    f'<div class="btn" style="margin-top:22px;background:{INK};color:{W};font-size:28px;padding:20px 40px">See the pan &rarr;</div></div></div>')

# ---------- echte redenen in plaats van een countdown (donker)
RS = [('Black Friday prices', 'Up to 70% off pans and sets.'),
      ('No code needed', 'Nothing to copy or type. The sale price is already on the product page.'),
      ('5 free gifts', 'In the box with every order, sets and single pans alike.'),
      ('30-day returns', 'Unused within 30 days of delivery? Full refund.'),
      ('75-year warranty', 'Covered against defects. A pure titanium cooking surface, no coatings, so nothing to wear off.')]
sec('bf-reasons', f'background:{DARK};padding:76px 70px 70px;color:{W}', head('Why now', 'Five honest reasons.<br>No countdown.', W, '#E7C988', 96) +
    '<div style="margin-top:40px">' + ''.join(
        f'<div style="display:flex;gap:34px;align-items:flex-start;padding:30px 0;border-top:2px solid #44403C">'
        f'<div class="ram" style="flex:none;width:90px;color:{GOLD};font-size:110px;line-height:96px;text-align:center">{i+1}</div>'
        f'<div style="flex:1"><div style="font-weight:600;font-size:42px;line-height:52px">{t}</div><div style="font-size:36px;line-height:52px;color:#CFC8BC;margin-top:6px">{s}</div></div></div>'
        for i, (t, s) in enumerate(RS)) + '</div>')

json.dump(SECS, open(os.path.join(OUT, 'list.json'), 'w'))
print(len(SECS), 'sections')
