"""Callout-anatomie ("Take a closer look"): productfoto van bovenaf met dunne lijnen of nummers ingebakken.
De teksten blijven live HTML (blok research/ux-round2/blocks/closerlook.html); dit script maakt alleen de beelden.

Gebruik:
  python3 -I scripts/make_callout.py <spec.json> <naam> <uitmap>
Schrijft <uitmap>/<naam>-desk.jpg (lijnen naar de vier hoeken, voor desktop: tekst erboven en eronder)
     en <uitmap>/<naam>-mob.jpg  (genummerde punten, voor mobiel: tekst als genummerde lijst eronder).
Beelden zijn 2x (1024 breed voor 512 px weergave). Het bronbestand wordt alleen gelezen.

spec.json: {"<naam>": {
   "src": "pad/naar/foto",            bronfoto (kopie), crème achtergrond
   "rotate": 0,                        graden tegen de klok in
   "zoom": 0.3,                        uitvoer-px per bron-px (na draaien)
   "center": [512, 330],               waar het midden van de gedraaide foto in de uitvoer komt
   "h": 660,                           hoogte desktopbeeld (2x)
   "mob_h": 760, "mob_center": [512, 380], "mob_zoom": 0.3,   (optioneel, anders gelijk aan desktop)
   "points": [ {"pos":"TL","a":[x,y],"ex":40}, {"pos":"TR",...}, {"pos":"BL",...}, {"pos":"BR",...} ]
        a  = ankerpunt op het product (desktop-px); ex = x van de verticale lijn bij de tekst
        mob = optioneel ander ankerpunt voor mobiel
}}
"""
import sys, json, os
from PIL import Image, ImageDraw, ImageFont

W = 1024
CREAM = (248, 247, 242); INK = (40, 40, 40); BRICK = (172, 59, 25)
FONT = '/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'


def bgmatch(im, src=(247, 242, 236), dst=CREAM):
    ch = [c.point(lambda v, k=d / s: min(255, int(round(v * k)))) for c, s, d in zip(im.split()[:3], src, dst)]
    return Image.merge('RGB', ch)


def place(spec, h, zoom, center):
    src = Image.open(spec['src']).convert('RGB')
    src = bgmatch(src)
    if spec.get('rotate'):
        src = src.rotate(spec['rotate'], resample=Image.BICUBIC, expand=True, fillcolor=CREAM)
    src = src.resize((int(src.width * zoom), int(src.height * zoom)), Image.LANCZOS)
    can = Image.new('RGB', (W, h), CREAM)
    can.paste(src, (int(center[0] - src.width / 2), int(center[1] - src.height / 2)))
    return can


def main():
    if len(sys.argv) != 4: sys.exit(__doc__)
    spec = json.load(open(sys.argv[1]))[sys.argv[2]]; name = sys.argv[2]; out = sys.argv[3]
    os.makedirs(out, exist_ok=True)
    h = spec['h']
    # desktop: lijnen
    im = place(spec, h, spec['zoom'], spec['center']); d = ImageDraw.Draw(im)
    S = 4; big = Image.new('RGBA', (W * S, h * S), (0, 0, 0, 0)); bd = ImageDraw.Draw(big)
    for p in spec['points']:
        ax, ay = p['a']; ex = p['ex']; ey = 0 if p['pos'][0] == 'T' else h
        lw = 2 * S
        bd.line((ex * S, ey * S, ex * S, ay * S), fill=INK + (255,), width=lw)
        if abs(ex - ax) > 1: bd.line((ex * S - lw / 2, ay * S, ax * S, ay * S), fill=INK + (255,), width=lw)
        r = 7 * S; ring = 4 * S
        bd.ellipse(((ax * S) - r - ring, (ay * S) - r - ring, (ax * S) + r + ring, (ay * S) + r + ring), fill=CREAM + (255,))
        bd.ellipse(((ax * S) - r, (ay * S) - r, (ax * S) + r, (ay * S) + r), fill=BRICK + (255,))
    im.paste(big.resize((W, h), Image.LANCZOS), (0, 0), big.resize((W, h), Image.LANCZOS))
    im.save(os.path.join(out, name + '-desk.jpg'), quality=86, optimize=True, progressive=True)
    # mobiel: nummers
    mh = spec.get('mob_h', h); mz = spec.get('mob_zoom', spec['zoom']); mc = spec.get('mob_center', spec['center'])
    dy = mc[1] - spec['center'][1]; dx = mc[0] - spec['center'][0]; k = mz / spec['zoom']
    im = place(spec, mh, mz, mc)
    big = Image.new('RGBA', (W * S, mh * S), (0, 0, 0, 0)); bd = ImageDraw.Draw(big)
    f = ImageFont.truetype(FONT, 40 * S)
    for i, p in enumerate(spec['points'], 1):
        if 'mob' in p: ax, ay = p['mob']
        else:
            ax = mc[0] + (p['a'][0] - spec['center'][0]) * k; ay = mc[1] + (p['a'][1] - spec['center'][1]) * k
        r = 32 * S; ring = 6 * S
        bd.ellipse((ax * S - r - ring, ay * S - r - ring, ax * S + r + ring, ay * S + r + ring), fill=CREAM + (235,))
        bd.ellipse((ax * S - r, ay * S - r, ax * S + r, ay * S + r), fill=BRICK + (255,))
        t = str(i); bb = f.getbbox(t)
        bd.text((ax * S - (bb[0] + bb[2]) / 2, ay * S - (bb[1] + bb[3]) / 2), t, font=f, fill=(255, 255, 255, 255))
    sm = big.resize((W, mh), Image.LANCZOS); im.paste(sm, (0, 0), sm)
    im.save(os.path.join(out, name + '-mob.jpg'), quality=84, optimize=True, progressive=True)
    print('ok', name)


if __name__ == '__main__':
    main()
