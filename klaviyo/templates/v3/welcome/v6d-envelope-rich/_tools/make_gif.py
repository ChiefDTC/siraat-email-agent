"""E1 hero: geanimeerde envelop (600 px breed). Verzegeld -> handen breken het zegel -> open, kaart toont 10% OFF + 5 FREE GIFTS.
Het eerste frame is al betekenisvol: onderschrift met aanbod staat in elk frame (Outlook toont alleen frame 1).
Gebruik: python3 -I _tools/make_gif.py   -> sections/e1-envelope.gif (< 1 MB)
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../../..'))
ENV = '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/envelope-assets/'
RAM = os.path.join(REPO, 'klaviyo/fonts/TTRamillas-LightItalic.ttf')
INTER = '/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
INTER_B = '/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'
W, PH, CAP = 600, 330, 150
CREAM, INK, BRICK, GOLD = (248, 247, 242), (39, 39, 39), (172, 59, 25), (184, 134, 43)

def fit(path, box=None):
    im = Image.open(path).convert('RGB')
    if box: im = im.crop(box)
    w, h = im.size; r = W / PH
    if w / h > r: nw = int(h * r); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else: nh = int(w / r); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    return im.resize((W, PH), Image.LANCZOS)

a = fit(ENV + 'siraat-01-front-cream.jpg')
b = fit(ENV + 'siraat-06-hands-breaking-seal.jpg', (0, 250, 1289, 1217))
# geopende envelop: 'Your first step' van de kaart weghalen (papier eroverheen kopieren), dan het aanbod erop
src = Image.open(ENV + 'siraat-15-opened-front-card.jpg').convert('RGB')
patch = src.crop((600, 470, 1005, 555)).resize((405, 95)).filter(ImageFilter.GaussianBlur(3))
src.paste(patch, (600, 552))
d = ImageDraw.Draw(src)
f1 = ImageFont.truetype(INTER_B, 118); f2 = ImageFont.truetype(INTER, 44)
for txt, f, y, col in [('10% OFF', f1, 520, INK), ('+ 5 FREE GIFTS', f2, 660, BRICK)]:
    tw = d.textlength(txt, font=f); d.text((800 - tw / 2, y), txt, font=f, fill=col)
w, h = src.size; r = W / PH; nh = int(w / r); top = (h - nh) // 2
c = src.crop((0, top, w, top + nh)).resize((W, PH), Image.LANCZOS)

def caption(img):
    fr = Image.new('RGB', (W, PH + CAP), CREAM); fr.paste(img, (0, 0)); dd = ImageDraw.Draw(fr)
    fr_ = ImageFont.truetype(RAM, 46); fs = ImageFont.truetype(INTER, 17)
    t1 = 'Your welcome envelope'; t2 = '10% OFF EVERYTHING + 5 FREE GIFTS  ·  CODE HI10'
    dd.text(((W - dd.textlength(t1, font=fr_)) / 2, PH + 26), t1, font=fr_, fill=INK)
    dd.text(((W - dd.textlength(t2, font=fs)) / 2, PH + 92), t2, font=fs, fill=BRICK)
    return fr

seq = []  # (frame, ms)
A, B, C = caption(a), caption(b), caption(c)
seq.append((A, 1400))
seq.append((Image.blend(A, B, 0.5), 110))
seq.append((B, 1100))
for t in (0.33, 0.66): seq.append((Image.blend(B, C, t), 100))
seq.append((C, 3200))
out = os.path.join(ROOT, 'sections/e1-envelope.gif'); os.makedirs(os.path.dirname(out), exist_ok=True)
pal = [f.quantize(colors=80, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG) for f, _ in seq]
pal[0].save(out, save_all=True, append_images=pal[1:], duration=[ms for _, ms in seq], loop=0, optimize=True, disposal=1)
A.save(os.path.join(ROOT, 'sections/e1-envelope-first.jpg'), quality=85)
C.save(os.path.join(ROOT, 'sections/e1-envelope-last.jpg'), quality=85)
print(out, os.path.getsize(out) // 1024, 'KB', len(seq), 'frames')
