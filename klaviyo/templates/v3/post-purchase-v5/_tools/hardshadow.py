"""Harde schaduw onder een transparante productuitsnede (Floris 19 nov 2026: zoals de preset "Hard" in Photoroom AI Schaduwen).
De Photoroom MCP kan dit niet: generate_ai-shadows heeft alleen een beeldinvoer (geen stijl/preset) en levert een zachte schaduw op wit.
Daarom met PIL op de Photoroom remove-background-uitsneden:
  1. slagschaduw: silhouet uit het alfakanaal, zwart, verticaal platgedrukt (zichthoek van de packshots ~30 graden van boven),
     onderrand gelijk met de onderrand van het product, kleine verschuiving naar rechtsonder, blur ~2 px, dekking ~52%;
  2. contactschaduw: smalle donkere band (dekking ~70%, blur ~1 px) precies langs de onderste rand van het product.
Resultaat: PNG met transparante achtergrond (werkt op elke getinte kaart). hard(src, rot, out, scale) -> out.
"""
import os
import numpy as np
from scipy import ndimage
from PIL import Image, ImageFilter, ImageChops

def hard(src, rot=0, out=None, squash=0.26, shift=(0.035, 0.012), op=0.52, blur=2.0, contact=0.70):
    if out and os.path.exists(out) and os.path.getmtime(out) > max(os.path.getmtime(src), os.path.getmtime(__file__)):
        return out
    im = Image.open(src).convert('RGBA')
    if rot: im = im.rotate(-rot, resample=Image.BICUBIC, expand=True)
    a = im.split()[3].point(lambda v: 0 if v < 24 else v)
    im.putalpha(a); im = im.crop(a.getbbox()); a = im.split()[3]
    w, h = im.size
    # werk op ware grootte, blur in pixels van het eindbeeld: schaal mee (uitsneden zijn ~1000-2000 px, kaart toont ~500 px)
    k = max(1.0, w / 600)
    padx, padb = int(w * .06), int(h * .10)
    W, H = w + 2 * padx, h + padb
    # 1. slagschaduw, per los onderdeel (sets: elk stuk zijn eigen schaduw direct eronder)
    mask = np.array(a) > 90
    lab, n = ndimage.label(ndimage.binary_dilation(mask, iterations=max(2, int(4 * k))))
    cast = Image.new('L', (W, H), 0); con = Image.new('L', (W, H), 0)
    areas = ndimage.sum(mask, lab, range(1, n + 1))
    for i, sl in enumerate(ndimage.find_objects(lab)):
        if areas[i] < mask.sum() * .004: continue
        y0, y1, x0, x1 = sl[0].start, sl[0].stop, sl[1].start, sl[1].stop
        part = Image.fromarray(((lab[sl] == i + 1) & mask[sl]).astype('uint8') * 255)
        ph = y1 - y0; sh_h = max(4, int(ph * squash))
        flat = part.resize((x1 - x0, sh_h), Image.BILINEAR).point(lambda v: 255 if v > 90 else 0)
        cast.paste(255, (padx + x0 + int(w * shift[0]), y1 - sh_h + int(ph * shift[1] * 1.2) + int(h * .004)), flat)
        # 2. contactschaduw van dit onderdeel: onderste ~4% van zijn silhouet, een paar px omlaag, nauwelijks blur
        band = int(max(3, ph * .04))
        bot = part.crop((0, ph - band, x1 - x0, ph)).point(lambda v: 255 if v > 90 else 0)
        con.paste(255, (padx + x0 + int(w * .003), y1 - band + max(2, int(ph * .008))), bot)
    cast = cast.filter(ImageFilter.GaussianBlur(blur * k)).point(lambda v: int(v * op))
    con = con.filter(ImageFilter.GaussianBlur(0.8 * k)).point(lambda v: int(v * contact))
    m = ImageChops.lighter(cast, con)
    canvas = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    shadow = Image.new('RGBA', (W, H), (18, 14, 10, 0)); shadow.putalpha(m)
    canvas = Image.alpha_composite(canvas, shadow)
    canvas.alpha_composite(im, (padx, 0))
    canvas = canvas.crop(canvas.split()[3].getbbox())
    if out: canvas.save(out); return out
    return canvas
