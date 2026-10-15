"""Gift card mockups (research/giftcard/01-presentatie.md).
Gebruik: python3 -I research/giftcard/make_mockups.py
Logo komt altijd uit brand/logo/lockup/, nooit nagetekend.
v1  Floris' gouden kaart, AI-logo weggepoetst, echt lockup gegraveerd erop
v2  dezelfde kaart in titanium-tint (zilver), echt lockup
v3  vlakke titanium kaart uit PIL (geen AI), echt lockup, brick lint, ruimte voor live tekst eronder
Plus: logo-vergelijking (overlay Floris tegen officieel)."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps, ImageChops
R = '/home/user/siraat-email-agent/'
G = R + 'research/giftcard/'
LOCK = R + 'brand/logo/lockup/siraat-lockup-black.png'
IS = '/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
ANG = 4.3                      # kanteling van de kaart (graden), gemeten op tekst en onderrand
C = (768, 512)

src = Image.open(G + 'floris-giftcard-goud.webp').convert('RGBA')

# ---------- 0. vergelijking monogram ----------
def mono_compare():
    lvl = src.rotate(ANG, resample=Image.BICUBIC, center=C)
    a = np.array(lvl.convert('RGB')).astype(float).mean(2)
    fm = lvl.crop((493, 468, 657, 628))                      # monogram Floris (rechtgezet)
    lk = Image.open(LOCK).convert('RGBA')
    off = Image.new('RGBA', lk.size, 'white'); off.alpha_composite(lk)
    om = off.crop((0, 0, 160, 160)).convert('L')             # monogram officieel
    S = 480
    f = ImageOps.autocontrast(fm.convert('L')).resize((S, S), Image.LANCZOS)
    o = om.resize((S, S), Image.LANCZOS)
    fd = np.array(f) < 110; od = np.array(o) < 128
    ov = np.full((S, S, 3), 255, np.uint8)
    ov[od & ~fd] = (172, 59, 25)     # alleen officieel (brick)
    ov[fd & ~od] = (70, 120, 200)    # alleen Floris (blauw)
    ov[fd & od] = (40, 40, 40)       # beide
    can = Image.new('RGB', (S * 3 + 80, S + 70), 'white'); d = ImageDraw.Draw(can)
    fnt = ImageFont.truetype(IS, 22)
    for i, (im, t) in enumerate([(f.convert('RGB'), 'Floris (AI)'), (o.convert('RGB'), 'Officieel lockup'), (Image.fromarray(ov), 'Overlay: blauw = alleen AI, rood = alleen officieel')]):
        can.paste(im, (20 + i * (S + 20), 50)); d.text((20 + i * (S + 20), 14), t, font=fnt, fill=(40, 40, 40))
    can.save(G + 'logo-vergelijking.png')
    agree = (fd & od).sum() / max(1, (fd | od).sum())
    print('overlap (IoU) monogram:', round(float(agree), 2))

# ---------- 1. Floris' kaart met echt lockup ----------
def engraved_lockup(width, ink=(74, 46, 20)):
    lk = Image.open(LOCK).convert('RGBA')
    h = round(lk.height * width / lk.width)
    lk = lk.resize((width, h), Image.LANCZOS)
    a = lk.getchannel('A')
    pad = 8
    W, H = width + 2 * pad, h + 2 * pad
    out = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    A = Image.new('L', (W, H), 0); A.paste(a, (pad, pad))
    hi = ImageChops.offset(A, 0, 2).filter(ImageFilter.GaussianBlur(0.8))      # lichte rand onder (gegraveerd)
    out.alpha_composite(Image.merge('RGBA', [Image.new('L', (W, H), v) for v in (255, 236, 190)] + [hi.point(lambda p: p * 0.55)]))
    body = Image.new('RGBA', (W, H), ink + (0,)); body.putalpha(A)
    out.alpha_composite(body)
    sh = ImageChops.multiply(A, ImageChops.offset(A, 0, 3).point(lambda p: 255 - p))  # binnenschaduw boven
    out.alpha_composite(Image.merge('RGBA', [Image.new('L', (W, H), 20)] * 3 + [sh.filter(ImageFilter.GaussianBlur(1)).point(lambda p: p * 0.6)]))
    return out

def spaced(d, xy, text, font, fill, sp):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill); x += d.textlength(ch, font=font) + sp

def spaced_w(d, text, font, sp):
    return sum(d.textlength(c, font=font) + sp for c in text) - sp

def v1():
    lvl = src.rotate(ANG, resample=Image.BICUBIC, center=C)
    arr = np.array(lvl).copy()
    x0, x1, y0, y1 = 470, 1385, 455, 728
    band = arr[740:860, x0:x1].copy()                          # schone geborstelde strook onder de tekst
    need = y1 - y0
    fill = np.concatenate([band[::-1], band, band[::-1]], 0)[:need].astype(float)
    # helderheid per kolom laten aansluiten op de rand boven en onder het gat (lineair over de hoogte)
    top = arr[y0 - 8:y0 - 2, x0:x1, :3].astype(float).mean(0) - fill[:6, :, :3].mean(0)
    bot = arr[y1 + 2:y1 + 8, x0:x1, :3].astype(float).mean(0) - fill[-6:, :, :3].mean(0)
    k = 41; ker = np.ones(k) / k
    top = np.stack([np.convolve(np.pad(top[:, c], k // 2, mode='edge'), ker, 'valid') for c in range(3)], 1)
    bot = np.stack([np.convolve(np.pad(bot[:, c], k // 2, mode='edge'), ker, 'valid') for c in range(3)], 1)
    t = np.linspace(0, 1, need)[:, None, None]
    fill[..., :3] += top[None] * (1 - t) + bot[None] * t
    patch = arr.copy(); patch[y0:y1, x0:x1] = np.clip(fill, 0, 255).astype(np.uint8)
    m = Image.new('L', lvl.size, 0); ImageDraw.Draw(m).rectangle((x0 + 10, y0 + 6, x1 - 10, y1 - 6), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(6))
    clean = Image.composite(Image.fromarray(patch), lvl, m)
    lw = 780
    lk = engraved_lockup(lw)
    clean.alpha_composite(lk, (int(925 - lk.width / 2), 478))
    d = ImageDraw.Draw(clean); f = ImageFont.truetype(IS, 30)
    t = 'GIFT CARD'; w = spaced_w(d, t, f, 12)
    spaced(d, (int(925 - w / 2), 672), t, f, (74, 46, 20, 255), 12)
    back = clean.rotate(-ANG, resample=Image.BICUBIC, center=C)
    mm = Image.new('L', lvl.size, 0); ImageDraw.Draw(mm).rectangle((x0, y0 - 4, x1, y1 + 4), fill=255)
    mm = mm.filter(ImageFilter.GaussianBlur(3)).rotate(-ANG, resample=Image.BICUBIC, center=C)
    res = src.copy(); res.paste(back, (0, 0), ImageChops.multiply(mm, back.getchannel('A')))
    res.putalpha(src.getchannel('A'))
    res.save(G + 'v1-goud-echt-lockup.png', optimize=True)
    return res

# ---------- 2. titanium-tint ----------
def v2(base):
    a = base.getchannel('A')
    g = ImageOps.autocontrast(base.convert('L'), cutoff=1)
    t = ImageOps.colorize(g, black=(38, 38, 40), mid=(150, 150, 152), white=(246, 246, 244), midpoint=110)
    t.putalpha(a); t.save(G + 'v2-titanium.png', optimize=True)
    return t

# ---------- 3. vlakke titanium kaart, geen AI ----------
def v3(amount=None, name='v3-titanium-plat'):
    W, H, r = 1200, 740, 44
    rng = np.random.default_rng(7)
    n = rng.normal(0, 1, (H, W // 8)).astype(np.float32)
    n = np.array(Image.fromarray(((n - n.min()) / (n.max() - n.min()) * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)).astype(float)
    n = np.array(Image.fromarray(n.astype(np.uint8)).filter(ImageFilter.BoxBlur(0)).resize((W // 40, H), Image.BILINEAR).resize((W, H), Image.BICUBIC)).astype(float)
    y = np.linspace(0, 1, H)[:, None]; x = np.linspace(0, 1, W)[None, :]
    sheen = 18 * np.exp(-((x - 0.62) ** 2) / 0.02) + 10 * np.exp(-((x - 0.18) ** 2) / 0.01) - 10 * y
    base = np.array([201, 198, 192], float)                     # titanium #C9C6C0
    img = np.clip(base[None, None, :] + (n[..., None] - 128) * 0.10 + sheen[..., None], 0, 255).astype(np.uint8)
    card = Image.fromarray(img).convert('RGBA'); d = ImageDraw.Draw(card)
    d.rounded_rectangle((18, 18, W - 18, H - 18), radius=r - 16, outline=(232, 230, 226), width=2)
    d.rectangle((150, 0, 210, H), fill=(172, 59, 25))           # brick lint, plat
    d.rectangle((150, 0, 154, H), fill=(140, 46, 18)); d.rectangle((206, 0, 210, H), fill=(196, 88, 52))
    lk = Image.open(LOCK).convert('RGBA'); lw = 560
    lk = lk.resize((lw, round(lk.height * lw / lk.width)), Image.LANCZOS)
    cx = 210 + (W - 210) // 2
    card.alpha_composite(lk, (cx - lw // 2, 150))
    f = ImageFont.truetype(IS, 26); t = 'GIFT CARD'; w = spaced_w(d, t, f, 11)
    spaced(d, (cx - w / 2, 318), t, f, (40, 40, 40, 255), 11)
    if amount:
        fa = ImageFont.truetype(R + 'klaviyo/fonts/TTRamillas-LightItalic.ttf', 190)
        d.text((cx - d.textlength(amount, font=fa) / 2, 392), amount, font=fa, fill=(40, 40, 40, 255))
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, W - 1, H - 1), radius=r, fill=255)
    card.putalpha(m)
    can = Image.new('RGB', (W + 0, H + 0), (248, 247, 242)); can.paste(card, (0, 0), card)
    can.save(G + name + '.jpg', quality=86)

if __name__ == '__main__':
    mono_compare()
    b = v1(); v2(b); v3(); v3('$50', 'v3-titanium-50')
    for p in ['v1-goud-echt-lockup.png', 'v2-titanium.png', 'v3-titanium-plat.jpg']:
        im = Image.open(G + p); print(p, im.size)
