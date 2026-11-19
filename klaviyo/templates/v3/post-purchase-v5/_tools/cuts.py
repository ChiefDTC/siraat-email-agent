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
sys.path.insert(0, os.path.dirname(__file__))
from ground import ground  # noqa: E402,F401
from hardshadow import hard  # noqa: E402
import numpy as np
from scipy import ndimage
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC, OUT = os.path.join(ROOT, 'gen/pr'), os.path.join(ROOT, 'gen/clean')
os.makedirs(OUT, exist_ok=True)

def largest(im):
    """Alleen het grootste losse onderdeel houden (bv. de titaniumplaat naast de wok in de bronfoto)."""
    a = np.array(im.split()[3]) > 40
    lab, n = ndimage.label(ndimage.binary_dilation(a, iterations=3))
    if n < 2: return im
    big = 1 + int(np.argmax(ndimage.sum(a, lab, range(1, n + 1))))
    keep = Image.fromarray(((lab == big) * 255).astype('uint8'))
    out = Image.new('RGBA', im.size, (0, 0, 0, 0)); out.paste(im, (0, 0), keep)
    return out.crop(out.split()[3].getbbox())

def neutral(im, thr=95):
    """Staal neutraal grijs zoals de packshots: alleen weinig verzadigde pixels (metaal) ontkleuren, eten en hout houden kleur."""
    a = im.split()[3]
    hsv = np.array(im.convert('RGB').convert('HSV')).astype(float)
    s_, v = hsv[..., 1], hsv[..., 2]
    edge = (np.array(a) > 0) & ~ndimage.binary_erosion(np.array(a) > 200, iterations=10)  # rand: bruine zweem van het decor
    metal = (s_ < thr) | edge
    hsv[..., 1] = np.where(metal, s_ * 0.18, s_)
    hsv[..., 2] = np.where(metal, np.clip(v * 1.06 + 6, 0, 255), v)
    out = Image.fromarray(hsv.astype('uint8'), 'HSV').convert('RGB').convert('RGBA'); out.putalpha(a)
    return out

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
    src = os.path.join(OUT, f'cut-{k}.png'); tmp = os.path.join(ROOT, 'gen/hard', f'part-{k}.png')
    os.makedirs(os.path.dirname(tmp), exist_ok=True)
    return Image.open(hard(src, 0, tmp))

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
            im = clean(Image.open(os.path.join(SRC, f)))
            if f.endswith('34.png'): im = neutral(largest(im), 40 if 'crp' in f else 95)  # 3/4-uitsneden uit sfeerbeelden: plaat weg, warme kleurzweem van het bruine decor eruit
            im.save(os.path.join(OUT, f))
    B = {
        'cmp': [('wok34', 0, 0, 1000), ('dep34', 1000, 40, 1000), ('crp34', 0, 600, 1050), ('std', 1050, 420, 900)],
        'csp': [('wok34', 0, 0, 1000), ('dep34', 1000, 40, 1000), ('std', 450, 470, 950), ('ute', 1500, 600, 520)],
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
