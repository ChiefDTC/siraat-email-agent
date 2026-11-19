"""PP v5 (19 nov 2026): schone uitsneden uit de Photoroom remove-background-resultaten (gen/pr/cut-<key>.png, 2000 px, zie
gen/photoroom-generations.txt) plus samengestelde bundelbeelden uit dezelfde echte uitsneden.
- Alfa opschonen: < 24 wordt 0 (geen grijze waas of halo), > 232 wordt 255 (harde, schone rand), daarna bijsnijden.
- Bundels (geen eigen Photoroom-generatie, bespaart credits): Complete Edition, Cookware Set Pro, Full Hammered Pro,
  2 Pans + 2 Lids en Just Everything worden gelegd uit de losse uitsneden van precies de stukken die erin zitten.
Gebruik: python3 -I _tools/cuts.py   -> gen/clean/cut-<key>.png
"""
import os, sys
from PIL import Image
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../welcome/v6d-envelope-rich/_tools')))
from ground import ground  # noqa: E402
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC, OUT = os.path.join(ROOT, 'gen/pr'), os.path.join(ROOT, 'gen/clean')
os.makedirs(OUT, exist_ok=True)

def clean(im):
    im = im.convert('RGBA')
    r, g, b, a = im.split()
    a = a.point(lambda v: 0 if v < 24 else (255 if v > 232 else v))
    im = Image.merge('RGBA', (r, g, b, a))
    # volledig transparante pixels echt leeg maken, zodat getbbox klopt
    px = Image.new('RGBA', im.size, (0, 0, 0, 0))
    im = Image.composite(im, px, a)
    return im.crop(a.getbbox())

def load(k):
    # elk onderdeel krijgt zijn eigen grondschaduw, zodat ook de achterste stukken op de ondergrond staan
    src = os.path.join(OUT, f'cut-{k}.png'); tmp = os.path.join(ROOT, 'gen/sh', f'part-{k}.png')
    os.makedirs(os.path.dirname(tmp), exist_ok=True)
    return Image.open(ground(src, 0, tmp))

def compose(parts, w=1800, h=1300):
    """parts: (key, x, y, breedte) in canvaspixels; eerste staat achteraan."""
    c = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    for k, x, y, bw in parts:
        im = load(k)
        im = im.resize((bw, int(im.height * bw / im.width)), Image.LANCZOS)
        c.alpha_composite(im, (x, y))
    return c.crop(c.split()[3].getbbox())

if __name__ == '__main__':
    for f in sorted(os.listdir(SRC)):
        if f.startswith('cut-') and f.endswith('.png'):
            clean(Image.open(os.path.join(SRC, f))).save(os.path.join(OUT, f))
    B = {
        'cmp': [('wok', 0, 0, 1150), ('dep', 60, 300, 1150), ('crp', 0, 640, 1200), ('std', 820, 260, 1150)],
        'csp': [('wok', 0, 0, 1150), ('dep', 60, 330, 1150), ('std', 820, 200, 1150), ('ute', 1850, 280, 560)],
        'fhp': [('lid', 60, 0, 520), ('lid', 520, 0, 560), ('lid', 1020, 0, 600), ('lid', 1520, 10, 640),
                ('min', 0, 380, 560), ('sml', 470, 360, 640), ('std', 1000, 340, 720), ('lrg', 1600, 330, 780), ('ute', 2300, 300, 500)],
        'p22': [('lid', 0, 0, 640), ('lid', 560, 0, 760), ('min', 40, 330, 720), ('std', 640, 300, 980)],
        'e34': [('s12', 0, 0, 1500), ('rst', 1300, 150, 900), ('piz', 1450, 760, 760), ('wok', 300, 1300, 800), ('crp', 1050, 1350, 800),
                ('ute', 2050, 300, 600), ('brd', 2100, 900, 600)],
    }
    for k, parts in B.items():
        w = max(x + bw for _, x, _, bw in parts) + 40
        compose(parts, w=w, h=2400).save(os.path.join(OUT, f'bundle-{k}.png'))
    print(sorted(os.listdir(OUT)))
