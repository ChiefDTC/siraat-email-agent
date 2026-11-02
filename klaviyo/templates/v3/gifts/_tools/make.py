import os, sys, io
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops

S = os.path.dirname(os.path.abspath(__file__))
HI = os.path.join(S, 'hi')
OUT = '/home/user/siraat-email-agent/klaviyo/templates/v3/gifts/assets'
os.makedirs(OUT, exist_ok=True)

NIGHT = (14, 14, 14)
CREAM = (248, 247, 242)
INK = (39, 39, 39)


def page(n):
    return Image.open(os.path.join(HI, f'p{n}.png')).convert('RGB')


def save_jpg(im, name, q=84):
    p = os.path.join(OUT, name)
    im.convert('RGB').save(p, 'JPEG', quality=q, optimize=True, progressive=True, subsampling='4:2:0')
    print(name, im.size, os.path.getsize(p) // 1024, 'KB')


def save_png(im, name, colors=256):
    p = os.path.join(OUT, name)
    im.convert('RGB').save(p, 'PNG', optimize=True)
    if os.path.getsize(p) <= 300 * 1024:
        print(name, im.size, os.path.getsize(p) // 1024, 'KB (truecolor)')
        return
    q = im.convert('RGB').quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)
    q.save(p, 'PNG', optimize=True)
    print(name, im.size, os.path.getsize(p) // 1024, 'KB')


def persp_coeffs(dst, src):
    # coefficients mapping output (dst) points to input (src) points
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); B.append(v)
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()


def warp(img, quad, size):
    """Place img (RGBA) into quad (TL,TR,BR,BL) on a canvas of size."""
    w, h = img.size
    src = [(0, 0), (w, 0), (w, h), (0, h)]
    c = persp_coeffs(quad, src)
    return img.transform(size, Image.PERSPECTIVE, c, Image.BICUBIC)


def lin_grad(w, h, stops, horizontal=True):
    """stops: list of (pos, (r,g,b,a))."""
    n = w if horizontal else h
    xs = np.linspace(0, 1, n)
    arr = np.zeros((n, 4))
    for ch in range(4):
        arr[:, ch] = np.interp(xs, [s[0] for s in stops], [s[1][ch] for s in stops])
    if horizontal:
        a = np.tile(arr[None, :, :], (h, 1, 1))
    else:
        a = np.tile(arr[:, None, :], (1, w, 1))
    return Image.fromarray(a.astype(np.uint8), 'RGBA')


def dress_cover(cover):
    """Add hinge groove, spine shading and soft sheen to the flat front cover."""
    cover = cover.convert('RGBA')
    w, h = cover.size
    g = lin_grad(w, h, [
        (0.0, (0, 0, 0, 120)), (0.012, (0, 0, 0, 40)), (0.022, (255, 255, 255, 38)),
        (0.032, (0, 0, 0, 70)), (0.05, (0, 0, 0, 10)), (0.5, (0, 0, 0, 0)),
        (0.985, (0, 0, 0, 0)), (1.0, (0, 0, 0, 40))])
    cover = Image.alpha_composite(cover, g)
    sheen = lin_grad(w, h, [(0, (255, 255, 255, 0)), (0.35, (255, 255, 255, 22)),
                            (0.55, (255, 255, 255, 0)), (1, (255, 255, 255, 0))])
    cover = Image.alpha_composite(cover, sheen)
    return cover


def spine_strip(cover, sw):
    """Spine colour sampled from the cover's left edge, with cylinder shading."""
    a = np.asarray(cover.convert('RGB'))
    col = a[:, 8:40].reshape(-1, 3).mean(0)
    h = cover.size[1]
    base = Image.new('RGBA', (sw, h), tuple(int(c * 0.78) for c in col) + (255,))
    shade = lin_grad(sw, h, [(0, (0, 0, 0, 150)), (0.45, (255, 255, 255, 30)), (1, (0, 0, 0, 90))])
    return Image.alpha_composite(base, shade)


def book(cover, height, turn=0.16, depth=0.045, canvas_pad=0.25):
    """Render a standing hardcover. Returns RGBA image and the base points for shadows."""
    cover = cover.convert('RGBA')
    cw, ch = cover.size
    scale = height / ch
    W = int(cw * scale); H = height
    cov = dress_cover(cover.resize((W, H), Image.LANCZOS))
    sp = spine_strip(cov, max(8, int(W * 0.12)))
    pad = int(H * canvas_pad)
    size = (W + 2 * pad, H + 2 * pad)
    ox, oy = pad, pad
    sw = int(W * depth)          # visible spine width
    fw = int(W * (1 - turn * 0.35))  # foreshortened front width
    shrink = H * turn * 0.22     # far edge vertical shrink (perspective)
    # front face quad: left edge (near) full height, right edge (far) shorter
    x0 = ox + sw
    front = [(x0, oy), (x0 + fw, oy + shrink), (x0 + fw, oy + H - shrink * 0.55), (x0, oy + H)]
    spine = [(ox, oy + shrink * 0.35), (x0, oy), (x0, oy + H), (ox, oy + H - shrink * 0.25)]
    layer = Image.new('RGBA', size, (0, 0, 0, 0))
    layer = Image.alpha_composite(layer, warp(sp, spine, size))
    layer = Image.alpha_composite(layer, warp(cov, front, size))
    # thin board edge highlight on top of front
    d = ImageDraw.Draw(layer)
    d.line([front[0], front[1]], fill=(255, 255, 255, 40), width=2)
    base = (ox, oy + H - shrink * 0.25, x0 + fw, oy + H - shrink * 0.55, x0, oy + H)
    return layer, front, spine


def shadowed(layer, front, spine, bg_dark=False, light_dir=1):
    size = layer.size
    H = front[3][1] - front[0][1]
    out = Image.new('RGBA', size, (0, 0, 0, 0))
    black = Image.new('RGBA', size, (0, 0, 0, 255))
    # 1) wide ambient shadow cast back-right onto the wall
    sh = Image.new('L', size, 0)
    off = H * 0.035
    poly = [(p[0] + off * light_dir, p[1] + off * 0.5) for p in [spine[0], front[1], front[2], front[3], spine[3]]]
    ImageDraw.Draw(sh).polygon(poly, fill=95 if not bg_dark else 200)
    sh = sh.filter(ImageFilter.GaussianBlur(H * 0.05))
    # 2) floor shadow: flattened blurred ellipse under the base, pushed right
    fl = Image.new('L', size, 0)
    by = front[3][1]
    x0 = spine[3][0]; x1 = front[2][0]
    ImageDraw.Draw(fl).ellipse([x0 - H * 0.02, by - H * 0.018, x1 + H * 0.10, by + H * 0.028], fill=150 if not bg_dark else 230)
    fl = fl.filter(ImageFilter.GaussianBlur(H * 0.022))
    # 3) tight contact line
    ct = Image.new('L', size, 0)
    ImageDraw.Draw(ct).polygon([(x0, by - 3), (x1, front[2][1] - 3), (x1 + 4, front[2][1] + 3), (x0, by + 4)], fill=200)
    ct = ct.filter(ImageFilter.GaussianBlur(3))
    m = ImageChops.lighter(ImageChops.lighter(sh, fl), ct)
    out.paste(black, (0, 0), m)
    return Image.alpha_composite(out, layer)


def bg_cream(w, h):
    a = np.zeros((h, w, 3), float)
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx - w * 0.5) / w) ** 2 + ((yy - h * 0.42) / h) ** 2)
    top = np.array(CREAM, float); edge = np.array((233, 229, 219), float)
    t = np.clip(r / 0.75, 0, 1)[..., None]
    a = top * (1 - t) + edge * t
    # floor line: slightly darker lower part
    fy = h * 0.80
    ft = np.clip((yy - fy) / (h * 0.02), 0, 1)[..., None]
    a = a * (1 - 0.03 * ft)
    return Image.fromarray(a.clip(0, 255).astype(np.uint8), 'RGB').filter(ImageFilter.GaussianBlur(1.2)).convert('RGBA')


def bg_night(w, h, glow_y=0.62, glow_x=0.5, strength=1.0):
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx - w * glow_x) / (w * 0.55)) ** 2 + ((yy - h * glow_y) / (h * 0.55)) ** 2)
    base = np.array(NIGHT, float)
    warm = np.array((118, 76, 16), float)
    t = (np.exp(-(r ** 2) * 2.6) * 0.85)[..., None] * strength
    a = base * (1 - t) + warm * t
    # soft floor pool of light under the books
    rf = np.sqrt(((xx - w * glow_x) / (w * 0.42)) ** 2 + ((yy - h * 0.93) / (h * 0.07)) ** 2)
    tf = (np.exp(-(rf ** 2) * 1.6) * 0.35)[..., None]
    a = a * (1 - tf) + np.array((150, 104, 36), float) * tf
    return Image.fromarray(a.clip(0, 255).astype(np.uint8), 'RGB').convert('RGBA')


def floor_reflection(canvas, layer, pos, front, alpha=0.18, fade=0.22):
    """Faint mirrored reflection below a book on dark backgrounds."""
    x, y = pos
    H = front[3][1] - front[0][1]
    refl = layer.transpose(Image.FLIP_TOP_BOTTOM)
    rh = int(H * fade)
    bottom = int(front[3][1])
    # reflected region starts at the base line: in the flipped image the base is at size-bottom
    top_in_flip = layer.size[1] - bottom
    crop = refl.crop((0, top_in_flip, layer.size[0], top_in_flip + rh))
    m = lin_grad(crop.size[0], rh, [(0, (0, 0, 0, int(255 * alpha))), (1, (0, 0, 0, 0))], horizontal=False).split()[3]
    ca = crop.split()[3]
    crop.putalpha(ImageChops.multiply(ca, m))
    canvas.alpha_composite(crop, (x, y + bottom))


# ---------- sources ----------
cook = page(1)
ebook_src = Image.open(os.path.join(S, 'dl', 'e1.png')).convert('RGB')
ebook = ebook_src.crop((287, 227, 751, 851))  # flat front face from the Shopify product image
alt = Image.open(os.path.join(HI, 'ebook-alt.png')).convert('RGB')  # placeholder design (altcover.py)


def main(which):
    if 'cover' in which:
        c = cook.resize((1200, int(1200 * cook.size[1] / cook.size[0])), Image.LANCZOS)
        save_jpg(c, 'cookbook-cover.jpg', 80)
        e = ebook.resize((600, int(600 * ebook.size[1] / ebook.size[0])), Image.LANCZOS)
        e = e.filter(ImageFilter.UnsharpMask(1.2, 60, 2))
        save_jpg(e, 'ebook-cover.jpg', 88)
        a = alt.resize((600, int(600 * alt.size[1] / alt.size[0])), Image.LANCZOS)
        save_jpg(a, 'ebook-cover-alt.jpg', 88)

    if 'mockup' in which:
        for name, src in (('cookbook-mockup.png', cook), ('ebook-mockup.png', ebook), ('ebook-mockup-alt.png', alt)):
            W, H = 1200, 1000
            bg = bg_cream(W, H)
            lay, fr, sp = book(src, 720)
            img = shadowed(lay, fr, sp)
            bx = (W - img.size[0]) // 2 + 20
            by = int(H * 0.84 - fr[3][1])
            bg.alpha_composite(img, (bx, by))
            save_png(bg, name)

    if 'spread' in which:
        W, H = 1200, 860
        bg = bg_cream(W, H)
        pages = [page(2), page(16), page(29)]
        ph = 590
        imgs = []
        for p in pages:
            p = p.resize((int(ph * p.size[0] / p.size[1]), ph), Image.LANCZOS)
            imgs.append(p)
        pw = imgs[0].size[0]
        angles = [6, 0, -6]
        xs = [W / 2 - pw * 0.74, W / 2, W / 2 + pw * 0.74]
        ys = [H / 2 + 22, H / 2 - 8, H / 2 + 22]
        order = [0, 2, 1]
        for i in order:
            p = imgs[i].convert('RGBA')
            pad = 80
            cv = Image.new('RGBA', (p.size[0] + 2 * pad, p.size[1] + 2 * pad), (0, 0, 0, 0))
            # shadow
            sh = Image.new('L', cv.size, 0)
            ImageDraw.Draw(sh).rectangle([pad + 6, pad + 14, pad + p.size[0] + 6, pad + p.size[1] + 14], fill=120)
            sh = sh.filter(ImageFilter.GaussianBlur(22))
            cv.paste(Image.new('RGBA', cv.size, (40, 30, 15, 255)), (0, 0), sh)
            cv.alpha_composite(p, (pad, pad))
            ImageDraw.Draw(cv).rectangle([pad, pad, pad + p.size[0] - 1, pad + p.size[1] - 1], outline=(0, 0, 0, 22))
            cv = cv.rotate(angles[i], Image.BICUBIC, expand=True)
            bg.alpha_composite(cv, (int(xs[i] - cv.size[0] / 2), int(ys[i] - cv.size[1] / 2)))
        save_jpg(bg, 'cookbook-spread.jpg', 82)

    if 'crops' in which:
        for n, name, cx in ((16, 'recipe-garlic-butter-ribeye.jpg', 0.52), (22, 'recipe-garlic-butter-shrimp.jpg', 0.44),
                            (29, 'recipe-crispy-pizza-night.jpg', 0.50)):
            p = page(n)
            w, h = p.size
            photo_h = int(h * 0.405) - 4
            side = photo_h - 150  # start below the chapter pill
            x0 = int(w * cx - side / 2)
            y0 = photo_h - side
            # keep the chapter pill out: pill sits in the top-left, y < ~0.055h, x < ~0.29w
            c = p.crop((x0, y0, x0 + side, y0 + side)).resize((600, 600), Image.LANCZOS)
            c = c.filter(ImageFilter.UnsharpMask(1.0, 40, 2))
            save_jpg(c, name, 84)

    if 'duo' in which:
      for eb, dname in ((ebook, 'duo-hero.png'), (alt, 'duo-hero-alt.png')):
        W, H = 1200, 900
        bg = bg_night(W, H, glow_y=0.64, glow_x=0.5)
        lay2, fr2, sp2 = book(eb, 500, turn=0.16)
        img2 = shadowed(lay2, fr2, sp2, bg_dark=True)
        lay1, fr1, sp1 = book(cook, 560, turn=0.16)
        img1 = shadowed(lay1, fr1, sp1, bg_dark=True)
        base_y = int(H * 0.93)
        # cookbook front-left, e-book behind-right; overlap only covers the e-book spine edge
        total = (fr1[1][0] - sp1[0][0]) + (fr2[1][0] - fr2[0][0]) - 6
        x1 = int((W - total) / 2 - sp1[0][0])
        y1 = base_y - int(fr1[3][1])
        x2 = int(x1 + fr1[1][0] - fr2[0][0] - 6)
        y2 = base_y - 14 - int(fr2[3][1])
        bg.alpha_composite(img2, (x2, y2))
        bg.alpha_composite(img1, (x1, y1))
        save_png(bg, dname)


if __name__ == '__main__':
    main(sys.argv[1:] or ['cover', 'mockup', 'spread', 'crops', 'duo'])
