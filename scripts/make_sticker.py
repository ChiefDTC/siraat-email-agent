"""Maakt een sticker als transparante PNG (2x) in de Siraat-huisstijl.

Twee vormen:
  scallop  ronde getande sticker (zoals de NEW-referentie), standaard brick met witte tekst
  pill     kleine afgeronde label-pil (bijv. BEST SELLER, NEW, US ONLY)

Gebruik:
  python3 -I scripts/make_sticker.py "NEW" uit.png
  python3 -I scripts/make_sticker.py "SAVE|$305" uit.png            (| = nieuwe regel, eerste regel klein)
  python3 -I scripts/make_sticker.py "BEST|SELLER" uit.png --size=120
  python3 -I scripts/make_sticker.py "BEST SELLER" uit.png --shape=pill
  opties: --size=<css px, standaard 112 (scallop) of 22 hoog (pill)>  --bg=#AC3B19  --fg=#FFFFFF
          --teeth=28  --rotate=<graden>  --outline  (dunne witte binnenring)
Uitvoer is 2x: --size=112 geeft een PNG van 224 px breed; in HTML zet je width=112.
"""
import sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_B = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
FONT_SB = '/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
SS = 4  # supersampling bovenop 2x


def hexrgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def tracked(draw, text, font, spacing):
    """breedte van tekst met letterafstand"""
    return sum(draw.textlength(c, font=font) for c in text) + spacing * (len(text) - 1)


def draw_tracked(draw, xy, text, font, spacing, fill):
    x, y = xy
    for c in text:
        draw.text((x, y), c, font=font, fill=fill)
        x += draw.textlength(c, font=font) + spacing


def fit_font(draw, text, path, max_w, start, spacing_em):
    s = start
    while s > 6:
        f = ImageFont.truetype(path, s)
        if tracked(draw, text, f, s * spacing_em) <= max_w: return f
        s -= 1
    return ImageFont.truetype(path, s)


def scallop(text, size, bg, fg, teeth, outline):
    px = size * 2 * SS  # eindgrootte 2x, getekend op SS
    im = Image.new('RGBA', (px, px), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c = px / 2; R = px * 0.44; b = px * 0.04  # basisstraal en tandstraal
    d.ellipse((c - R, c - R, c + R, c + R), fill=bg)
    for i in range(teeth):
        a = 2 * math.pi * i / teeth
        x = c + (R + b * 0.1) * math.cos(a); y = c + (R + b * 0.1) * math.sin(a)
        d.ellipse((x - b, y - b, x + b, y + b), fill=bg)
    if outline:
        r2 = R - px * 0.045
        d.ellipse((c - r2, c - r2, c + r2, c + r2), outline=fg + (150,), width=max(2, int(px * 0.008)))
    lines = text.split('|')
    inner = R * 1.5  # beschikbare breedte voor tekst
    if len(lines) == 1:
        f = fit_font(d, lines[0], FONT_B, inner * (0.82 if len(lines[0]) <= 4 else 0.92), int(px * 0.2), 0.04)
        sp = f.size * 0.04; w = tracked(d, lines[0], f, sp)
        bb = f.getbbox('NEW0$')
        y = c - (bb[1] + bb[3]) / 2
        draw_tracked(d, (c - w / 2, y), lines[0], f, sp, fg)
    else:
        small, big = lines[0], lines[1]
        fs = fit_font(d, small, FONT_SB, inner * 0.62, int(px * 0.095), 0.14)
        fb = fit_font(d, big, FONT_B, inner * 0.9, int(px * 0.22), 0.0)
        sps = fs.size * 0.14
        hs = fs.getbbox('SAVE')[3] - fs.getbbox('SAVE')[1]
        hb = fb.getbbox('$305')[3] - fb.getbbox('$305')[1]
        gap = px * 0.035; tot = hs + gap + hb; top = c - tot / 2
        ws = tracked(d, small, fs, sps)
        draw_tracked(d, (c - ws / 2, top - fs.getbbox('SAVE')[1]), small, fs, sps, fg)
        wb = tracked(d, big, fb, 0)
        draw_tracked(d, (c - wb / 2, top + hs + gap - fb.getbbox('$305')[1]), big, fb, 0, fg)
    return im


def pill(text, height, bg, fg):
    h = height * 2 * SS
    tmp = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    f = ImageFont.truetype(FONT_SB, int(h * 0.42)); sp = f.size * 0.12
    w = int(tracked(tmp, text, f, sp) + h * 1.1)
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=h // 2, fill=bg)
    bb = f.getbbox('BEST')
    draw_tracked(d, ((w - tracked(d, text, f, sp)) / 2, (h - (bb[1] + bb[3])) / 2), text, f, sp, fg)
    return im


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    opt = dict(a[2:].split('=', 1) if '=' in a else (a[2:], '1') for a in sys.argv[1:] if a.startswith('--'))
    if len(args) != 2: sys.exit(__doc__)
    text, out = args
    shape = opt.get('shape', 'scallop')
    bg = hexrgb(opt.get('bg', '#AC3B19')) + (255,); fg = hexrgb(opt.get('fg', '#FFFFFF'))
    if shape == 'pill':
        im = pill(text.replace('|', ' '), int(opt.get('size', 22)), bg, fg + (255,))
    else:
        im = scallop(text, int(opt.get('size', 112)), bg, fg + (255,), int(opt.get('teeth', 28)), 'outline' in opt)
    im = im.resize((im.width // SS, im.height // SS), Image.LANCZOS)
    rot = float(opt.get('rotate', 0))
    if rot: im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    im.save(out, optimize=True)
    print('ok', out, im.size)


if __name__ == '__main__':
    main()
