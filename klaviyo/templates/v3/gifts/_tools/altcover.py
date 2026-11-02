"""Placeholder cover for the Plastic-Free Home / Green Clean e-guide in the cookbook style. No logo, no wordmark."""
import math, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

F = '/mnt/skills/examples/canvas-design/canvas-fonts/'
INTER = '/usr/share/fonts/opentype/inter/'
W, H = 1870, 2420  # same as rendered cookbook pages (letter, 220 dpi)
CREAM = (245, 242, 235)
INK = (39, 39, 39)
GREEN = (46, 98, 72)
SAGE = (214, 226, 210)
YELLOW = (255, 184, 0)

im = Image.new('RGB', (W, H), CREAM)
d = ImageDraw.Draw(im)
serif = ImageFont.truetype(F + 'InstrumentSerif-Regular.ttf', 330)
serif_i = ImageFont.truetype(F + 'InstrumentSerif-Italic.ttf', 330)
eyebrow = ImageFont.truetype(INTER + 'Inter-SemiBold.otf', 44)
pill_f = ImageFont.truetype(INTER + 'Inter-Bold.otf', 40)
body = ImageFont.truetype(INTER + 'Inter-Regular.otf', 64)


def tracked(xy, text, font, fill, track):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + track
    return x


M = 150
# pill top right (yellow surface, ink text: allowed)
pt = 'A FREE E-GUIDE'
tw = sum(d.textlength(c, font=pill_f) + 6 for c in pt) - 6
px1 = W - M; px0 = px1 - tw - 90
d.rounded_rectangle([px0, 130, px1, 222], radius=46, fill=YELLOW)
tracked((px0 + 45, 150), pt, pill_f, INK, 6)

tracked((M, 330), 'THE GREEN CLEAN GUIDE', eyebrow, GREEN, 7)

y = 420
d.text((M - 8, y), 'The', font=serif, fill=INK)
d.text((M - 8, y + 290), 'Plastic-Free', font=serif, fill=INK)
d.text((M - 8, y + 580), 'Home', font=serif_i, fill=GREEN)

d.text((M, y + 960), 'Natural, easy ways to clean your kitchen', font=body, fill=(70, 70, 66))
d.text((M, y + 1045), 'and cut the plastic, one swap at a time.', font=body, fill=(70, 70, 66))

# arch panel bottom right (echoes the cookbook chapter pages)
ax0, ax1 = 1080, W - M
ay1 = H - 200
ar = (ax1 - ax0) // 2
ay0 = ay1 - 640
arch = Image.new('L', (W, H), 0)
ad = ImageDraw.Draw(arch)
ad.rectangle([ax0, ay0 + ar, ax1, ay1], fill=255)
ad.ellipse([ax0, ay0, ax1, ay0 + 2 * ar], fill=255)
im.paste(SAGE, (0, 0), arch)

# leaf sprig inside the arch
cx = (ax0 + ax1) // 2
stem_top, stem_bot = ay0 + 130, ay1 - 90
d.line([(cx, stem_bot), (cx, stem_top)], fill=GREEN, width=12)
leaf = Image.new('RGBA', (180, 80), (0, 0, 0, 0))
ImageDraw.Draw(leaf).ellipse([0, 14, 179, 66], fill=GREEN + (255,))
n = 7
for i in range(n):
    t = i / (n - 1)
    yy = stem_bot - 90 - t * (stem_bot - stem_top - 120)
    sc = 0.85 - 0.35 * t
    lf = leaf.resize((int(180 * sc), int(80 * sc)), Image.LANCZOS)
    for side in (-1, 1):
        r = lf.rotate(35 if side > 0 else 145, expand=True, resample=Image.BICUBIC)
        ox = cx + (6 if side > 0 else -r.size[0] - 6)
        im.paste(r, (int(ox), int(yy - r.size[1] / 2 - 30 * side * 0 - (34 if side > 0 else 0))), r)
top = leaf.resize((110, 50), Image.LANCZOS).rotate(90, expand=True, resample=Image.BICUBIC)
im.paste(top, (cx - top.size[0] // 2, stem_top - top.size[1] + 20), top)

# colour dots left of the arch (the cookbook chapter colours)
dots = [(255, 184, 0), (200, 74, 58), (46, 86, 140), (46, 98, 72), (176, 110, 50)]
for i, c in enumerate(dots):
    x = M + i * 92
    d.ellipse([x, ay1 - 64, x + 56, ay1 - 8], fill=c)

d.line([(M, H - 120), (W - M, H - 120)], fill=(222, 217, 206), width=3)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hi', 'ebook-alt.png')
im.save(out)
print(out)
