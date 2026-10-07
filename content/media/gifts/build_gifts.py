"""Builds clean single-gift images from the downloaded sources.
Run: python3 -I build_gifts.py  (from this folder). Outputs go to final/."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "sources")
OUT = os.path.join(HERE, "final")
CREAM = (248, 247, 242, 255)
os.makedirs(OUT, exist_ok=True)

def on_bg(img, color=CREAM):
    bg = Image.new("RGBA", img.size, color)
    bg.alpha_composite(img)
    return bg.convert("RGB")

def soft_shadow(size, box, blur=40, opacity=90):
    sh = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse(box, fill=(40, 30, 20, opacity))
    return sh.filter(ImageFilter.GaussianBlur(blur))

# 1. E-book mockup from the existing cover art (front face only; AI spine text is dropped)
def ebook():
    src = Image.open(os.path.join(SRC, "shopify-ebook-cover-ChatGPT.png")).convert("RGBA")
    face = src.crop((310, 228, 751, 851))
    H = 880
    W = round(face.width * H / face.height)
    face = face.resize((W, H), Image.LANCZOS)
    # light falloff: brighter near spine hinge, slightly darker to the right edge
    grad = Image.linear_gradient("L").rotate(90).resize((W, H))
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shade.putalpha(grad.point(lambda v: int(v * 0.10)))
    face = Image.alpha_composite(face, shade)
    hinge = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(hinge)
    for i in range(14):  # hinge groove
        d.line([(10 + i, 0), (10 + i, H)], fill=(0, 0, 0, int(38 * (1 - i / 14))))
    d.line([(4, 0), (4, H)], fill=(255, 255, 255, 70), width=2)
    face = Image.alpha_composite(face, hinge)
    # rounded corners on the open edge
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, W - 1, H - 1], radius=8, fill=255)
    mask.paste(255, (0, 0, 12, H))
    face.putalpha(mask)

    spine_w = 46
    spine_col = np.array(src.crop((292, 400, 300, 700)).convert("RGB")).reshape(-1, 3).mean(0).astype(int)
    spine = Image.new("RGBA", (spine_w, H), tuple(spine_col) + (255,))
    sg = Image.linear_gradient("L").rotate(90).resize((spine_w, H))
    dark = Image.new("RGBA", (spine_w, H), (0, 0, 0, 0)); dark.putalpha(sg.point(lambda v: int(70 - v * 0.2)))
    spine = Image.alpha_composite(spine, dark)
    ImageDraw.Draw(spine).line([(6, 0), (6, H)], fill=(255, 255, 255, 60), width=2)

    S = 1200
    canvas = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    total = spine_w + W
    x0 = (S - total) // 2 + 10
    y0 = (S - H) // 2 - 10
    canvas.alpha_composite(soft_shadow((S, S), (x0 - 30, y0 + H - 40, x0 + total + 60, y0 + H + 50), blur=30, opacity=110))
    sh2 = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(sh2).rectangle((x0 + 24, y0 + 24, x0 + total + 22, y0 + H + 14), fill=(40, 30, 20, 70))
    canvas.alpha_composite(sh2.filter(ImageFilter.GaussianBlur(26)))
    canvas.alpha_composite(spine, (x0, y0))
    canvas.alpha_composite(face, (x0 + spine_w, y0))
    canvas.save(os.path.join(OUT, "gift-ebook-mockup.png"))
    on_bg(canvas).save(os.path.join(OUT, "gift-ebook-mockup-cream.jpg"), quality=90)

# 2. Mystery gift: Shopify product photo (kraft box, red ribbon, on black). Square crop + cut-out attempt.
def mystery():
    src = Image.open(os.path.join(SRC, "shopify-GiftSiraat.jpg")).convert("RGB")
    src.resize((1200, 1200), Image.LANCZOS).save(os.path.join(OUT, "gift-mystery-photo-dark.jpg"), quality=90)
    # The box is an axis-aligned rectangle; find it from kraft and ribbon colours, then mask that rectangle.
    a = np.array(src).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    m = ((r > 90) & (r > g) & (g > b) & (r - b > 25) & (r - b < 110)) | ((r > 110) & (r > g * 1.8))
    cols = np.where(m.mean(0) > 0.2)[0]; rows = np.where(m.mean(1) > 0.2)[0]
    bbox = (int(cols.min()) + 1, int(rows.min()) + 1, int(cols.max()), int(rows.max()))
    cut = src.crop(bbox).convert("RGBA")
    mask = Image.new("L", cut.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, cut.width - 1, cut.height - 1], radius=3, fill=255)
    cut.putalpha(mask.filter(ImageFilter.GaussianBlur(0.6)))
    S = 1200; sc = 820 / max(cut.size)
    cut = cut.resize((round(cut.width * sc), round(cut.height * sc)), Image.LANCZOS)
    canvas = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    x0, y0 = (S - cut.width) // 2, (S - cut.height) // 2 - 20
    canvas.alpha_composite(soft_shadow((S, S), (x0 + 20, y0 + cut.height - 50, x0 + cut.width - 20, y0 + cut.height + 50), blur=34, opacity=100))
    canvas.alpha_composite(cut, (x0, y0))
    canvas.save(os.path.join(OUT, "gift-mystery-cutout.png"))
    on_bg(canvas).save(os.path.join(OUT, "gift-mystery-cutout-cream.jpg"), quality=90)

# 3. PFAS water purifier: Shopify product image is already a transparent cut-out. Trim, centre, square.
def purifier():
    src = Image.open(os.path.join(SRC, "shopify-Water_filter_free.png")).convert("RGBA")
    cut = src.crop(src.getchannel("A").getbbox())
    S = 1200; sc = 900 / max(cut.size)
    cut = cut.resize((round(cut.width * sc), round(cut.height * sc)), Image.LANCZOS)
    canvas = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    x0, y0 = (S - cut.width) // 2, (S - cut.height) // 2
    canvas.alpha_composite(soft_shadow((S, S), (x0 + 40, y0 + cut.height - 30, x0 + cut.width - 40, y0 + cut.height + 30), blur=24, opacity=80))
    canvas.alpha_composite(cut, (x0, y0))
    canvas.save(os.path.join(OUT, "gift-purifier.png"))
    on_bg(canvas).save(os.path.join(OUT, "gift-purifier-cream.jpg"), quality=90)

if __name__ == "__main__":
    ebook(); mystery(); purifier()
    print(sorted(os.listdir(OUT)))
