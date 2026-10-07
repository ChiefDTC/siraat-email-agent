"""Beelden voor de vergelijkingstabel (research/ux-round2/blocks/compare.html).

Maakt in <uitmap>:
  icon-check.png   vinkje in brick (2x, 32 px voor 16 px weergave)
  icon-cross.png   kruisje in warm grijs
  icon-same.png    vinkje in grijs (voor rijen waar beide kolommen hetzelfde kunnen)
  compare-cap-<naam>.png   kopstuk van de tabel (1024 breed, 2x): bovenrand met afgeronde hoeken,
                           linkerkolom wit, rechterkolom grijs, productfoto die over de rand steekt.
Gebruik:
  python3 -I scripts/make_compare_assets.py <uitmap> [<productfoto> <naam>]
De productfoto (crème packshot) wordt via vermenigvuldigen ingezet: crème wordt transparant,
schaduw en metaal blijven, dus hij staat net zo goed op crème als op wit. Bron wordt alleen gelezen.
"""
import sys, os
from PIL import Image, ImageDraw, ImageChops

CREAM = (248, 247, 242); WHITE = (255, 255, 255); GREY = (236, 232, 225)
BRICK = (172, 59, 25); MUTED = (154, 148, 139); INK = (40, 40, 40)
S = 4


def icon(kind, col, out):
    n = 32 * S; im = Image.new('RGBA', (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    w = int(3.2 * S * 2)
    if kind == 'check':
        d.line([(n * .2, n * .53), (n * .42, n * .74), (n * .82, n * .3)], fill=col + (255,), width=w, joint='curve')
        for x, y in [(n * .2, n * .53), (n * .42, n * .74), (n * .82, n * .3)]:
            d.ellipse((x - w / 2, y - w / 2, x + w / 2, y + w / 2), fill=col + (255,))
    else:
        for a, b in [((n * .27, n * .27), (n * .73, n * .73)), ((n * .73, n * .27), (n * .27, n * .73))]:
            d.line([a, b], fill=col + (255,), width=w)
            for x, y in (a, b): d.ellipse((x - w / 2, y - w / 2, x + w / 2, y + w / 2), fill=col + (255,))
    im.resize((32, 32), Image.LANCZOS).save(out)


def cap(photo, out, overhang=200, inner=84, prod_w=340, crop=(0.13, 0.13, 0.93, 0.87), src_bg=(247, 242, 236)):
    W = 1024; H = overhang + inner
    base = Image.new('RGB', (W * S, H * S), CREAM); d = ImageDraw.Draw(base)
    r = 24 * S; top = overhang * S
    d.rounded_rectangle((0, top, W * S - 1, H * S + r * 2), radius=r, fill=GREY)
    # linkerkolom wit, met eigen afgeronde hoek linksboven
    d.rounded_rectangle((0, top, W * S // 2 + r, H * S + r * 2), radius=r, fill=WHITE)
    d.rectangle((W * S // 2, top, W * S // 2 + r + 2, H * S), fill=GREY)
    base = base.resize((W, H), Image.LANCZOS)
    if photo:
        p = Image.open(photo).convert('RGB')
        p = p.crop((int(p.width * crop[0]), int(p.height * crop[1]), int(p.width * crop[2]), int(p.height * crop[3])))
        p = p.resize((prod_w, int(p.height * prod_w / p.width)), Image.LANCZOS)
        # transmissiekaart: foto / achtergrondkleur
        # licht verloop in de achtergrond wegdrukken: alles boven 96 procent wordt volledig transparant
        t = Image.merge('RGB', [c.point(lambda v, k=1 / s: 255 if v * k >= 0.96 else int(255 * min(1, v * k / 0.96)))
                                for c, s in zip(p.split(), src_bg)])
        # randen van de uitsnede zacht laten uitlopen naar 'transparant' (wit in de transmissiekaart)
        m = Image.new('L', p.size, 0); md = ImageDraw.Draw(m); f = 28
        for i in range(f):
            md.rectangle((i, i, p.width - 1 - i, p.height - 1 - i), outline=int(255 * (1 - i / f)))
        t = Image.composite(Image.new('RGB', p.size, WHITE), t, m)
        x = W // 4 - prod_w // 2 - 24; y = H - p.height - 4
        region = base.crop((x, y, x + p.width, y + p.height))
        base.paste(ImageChops.multiply(region, t), (x, y))
    base.save(out, optimize=True)


def main():
    if len(sys.argv) not in (2, 4): sys.exit(__doc__)
    o = sys.argv[1]; os.makedirs(o, exist_ok=True)
    icon('check', BRICK, os.path.join(o, 'icon-check.png'))
    icon('cross', MUTED, os.path.join(o, 'icon-cross.png'))
    icon('check', MUTED, os.path.join(o, 'icon-same.png'))
    if len(sys.argv) == 4:
        cap(sys.argv[2], os.path.join(o, 'compare-cap-%s.png' % sys.argv[3]))
    else:
        cap(None, os.path.join(o, 'compare-cap-plain.png'))
    print('ok', o)


if __name__ == '__main__':
    main()
