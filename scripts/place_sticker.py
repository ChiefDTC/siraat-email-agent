"""Zet een sticker (PNG van make_sticker.py) op een KOPIE van een productfoto.
Het origineel wordt nooit overschreven: uitvoerpad moet anders zijn dan de bron.

Gebruik:
  python3 -I scripts/place_sticker.py <foto> <sticker.png> <uit.jpg> [opties]
  --x=0.80 --y=0.20      middelpunt van de sticker als fractie van breedte en hoogte (standaard rechtsboven)
  --scale=0.26           stickerbreedte als fractie van de fotobreedte
  --rotate=-12           draaiing in graden (positief = tegen de klok in)
  --width=600            uitvoerbreedte in px (standaard: bronbreedte, max 1200)
  --square               centraal vierkant uitsnijden voor productkaarten
  --bgmatch              crème van Shopify-packshots (#F7F2EC) gelijktrekken naar mail-crème #F8F7F2
  --shadow               zachte schaduw onder de sticker
  --white                crème achtergrond van het packshot naar wit (voor witte productkaarten); schaduw blijft
"""
import sys, os
from PIL import Image, ImageFilter


def bgmatch(im, src=(247, 242, 236), dst=(248, 247, 242)):
    r, g, b = im.split()[:3]
    ch = [c.point(lambda v, k=d / s: min(255, int(round(v * k)))) for c, s, d in zip((r, g, b), src, dst)]
    return Image.merge('RGB', ch)


def towhite(im, src=(247, 242, 236)):
    # foto / achtergrondkleur: crème wordt wit, metaal en schaduw blijven; licht verloop boven 96 procent valt weg
    return Image.merge('RGB', [c.point(lambda v, k=1 / s: 255 if v * k >= 0.96 else int(255 * v * k / 0.96))
                               for c, s in zip(im.split()[:3], src)])


def main():
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    o = dict(x[2:].split('=', 1) if '=' in x else (x[2:], '1') for x in sys.argv[1:] if x.startswith('--'))
    if len(a) != 3: sys.exit(__doc__)
    src, stk, out = a
    if os.path.abspath(src) == os.path.abspath(out): sys.exit('uitvoer mag het origineel niet overschrijven')
    im = Image.open(src).convert('RGB')
    if 'square' in o:
        s = min(im.size); l = (im.width - s) // 2; t = (im.height - s) // 2; im = im.crop((l, t, l + s, t + s))
    W = min(int(o.get('width', im.width)), 1200)
    if W != im.width: im = im.resize((W, int(im.height * W / im.width)), Image.LANCZOS)
    if 'bgmatch' in o: im = bgmatch(im)
    if 'white' in o: im = towhite(im)
    st = Image.open(stk).convert('RGBA')
    sw = int(W * float(o.get('scale', 0.26)))
    if sw < 8: base = im; base.save(out, quality=88, optimize=True); print('ok (zonder sticker)', out); return
    st = st.resize((sw, int(st.height * sw / st.width)), Image.LANCZOS)
    rot = float(o.get('rotate', -12))
    if rot: st = st.rotate(rot, resample=Image.BICUBIC, expand=True)
    cx = int(im.width * float(o.get('x', 0.8))); cy = int(im.height * float(o.get('y', 0.2)))
    pos = (cx - st.width // 2, cy - st.height // 2)
    base = im.convert('RGBA')
    if 'shadow' in o:
        sh = Image.new('RGBA', st.size, (40, 30, 25, 0)); sh.putalpha(st.split()[3].point(lambda v: int(v * 0.22)))
        sh = sh.filter(ImageFilter.GaussianBlur(max(2, sw // 40)))
        base.alpha_composite(sh, (pos[0] + sw // 60, pos[1] + sw // 30))
    base.alpha_composite(st, pos)
    base.convert('RGB').save(out, quality=88, optimize=True)
    print('ok', out, base.size)


if __name__ == '__main__':
    main()
