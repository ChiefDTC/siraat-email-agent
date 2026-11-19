"""Productbeeld boven het aanbodblok van A (19 nov, Floris): vrijstaande uitsnede op #0E0E0E, 1200 px breed (weergave 600),
lichte vloerglow plus donkere contactschaduw zodat het product staat. Geen tekst. python3 -I make_top_img.py"""
import os
from PIL import Image, ImageFilter, ImageChops, ImageDraw
D = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(D, '../../welcome/v6d-envelope-rich/gen')
BG = (14, 14, 14)
def make(cut, out, maxw, maxh, rot=0):
    W, H = 1200, 760
    im = Image.open(os.path.join(GEN, cut)).convert('RGBA')
    if rot: im = im.rotate(-rot, resample=Image.BICUBIC, expand=True)
    im = im.crop(im.getbbox())
    s = min(maxw / im.width, maxh / im.height, 1.0)
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    w, h = im.size; x = (W - w) // 2; base = H - 90; y = base - h
    c = Image.new('RGB', (W, H), BG)
    # 1. vloerglow: brede, zachte lichte ellips onder het product
    g = Image.new('L', (W, H), 0); dr = ImageDraw.Draw(g)
    gw, gh = int(w * 1.15), int(h * .26)
    dr.ellipse((W // 2 - gw // 2, base - gh // 2, W // 2 + gw // 2, base + gh // 2), fill=255)
    g = g.filter(ImageFilter.GaussianBlur(46)).point(lambda v: int(v * .62))
    c = Image.composite(Image.new('RGB', (W, H), (96, 92, 86)), c, g)
    # 2. contactschaduw: platgedrukt silhouet, donker, direct onder de onderrand
    a = im.split()[3]
    sh = Image.new('L', (W, H), 0)
    ch = max(8, int(h * .09))
    sh.paste(a.resize((int(w * .92), ch)), (x + int(w * .04), base - int(ch * .85)))
    sh = sh.filter(ImageFilter.GaussianBlur(12)).point(lambda v: int(v * .95))
    c = Image.composite(Image.new('RGB', (W, H), (0, 0, 0)), c, sh)
    c.paste(im, (x, y), im)
    c.save(os.path.join(D, 'gen', out), quality=84, optimize=True, progressive=True)
    print(out, c.size, os.path.getsize(os.path.join(D, 'gen', out)) // 1024, 'KB', 'uitsnede', w, h)
make('cut-set12.png', 'a-top12.jpg', 900, 620)
make('cut-set6.png', 'a-top6.jpg', 880, 600, -4)
