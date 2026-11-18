"""Grondschaduw onder productuitsneden (Floris 18 nov 2026: altijd schaduw, anders zweeft het).
Draait de uitsnede (zoals eerder in CSS), en legt onder het laagste punt een platgedrukte, vervaagde silhouetschaduw plus een korte contactschaduw."""
import os
from PIL import Image, ImageFilter, ImageChops
def ground(src, rot, out):
    if os.path.exists(out) and os.path.getmtime(out) > os.path.getmtime(src) and os.path.getmtime(out) > os.path.getmtime(__file__):
        return out
    im = Image.open(src).convert('RGBA')
    if rot: im = im.rotate(-rot, resample=Image.BICUBIC, expand=True)  # CSS rotate(+) = klok mee
    im = im.crop(im.getbbox())
    w, h = im.size
    a = im.split()[3]
    pad_x, pad_b = int(w * .08), int(h * .14)
    W, H = w + 2 * pad_x, h + pad_b
    canvas = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    # 1. brede zachte schaduw: silhouet platgedrukt tot ~18% hoogte op de bodem
    sh_h = max(8, int(h * .18))
    flat = a.resize((int(w * 1.04), sh_h), Image.BILINEAR)
    sh = Image.new('L', (W, H), 0)
    sh.paste(flat, (pad_x - int(w * .02), h - int(sh_h * .78)))
    sh = sh.filter(ImageFilter.GaussianBlur(max(6, w * .03))).point(lambda v: int(v * .42))
    # 2. contactschaduw: smal en donker, direct onder de onderrand
    c_h = max(4, int(h * .05))
    cflat = a.resize((int(w * .9), c_h), Image.BILINEAR)
    cs = Image.new('L', (W, H), 0)
    cs.paste(cflat, (pad_x + int(w * .05), h - int(c_h * .95)))
    cs = cs.filter(ImageFilter.GaussianBlur(max(3, w * .012))).point(lambda v: int(v * .55))
    m = ImageChops.lighter(sh, cs)
    shadow = Image.new('RGBA', (W, H), (38, 28, 18, 0)); shadow.putalpha(m)
    canvas = Image.alpha_composite(canvas, shadow)
    canvas.alpha_composite(im, (pad_x, 0))
    canvas.save(out)
    return out
