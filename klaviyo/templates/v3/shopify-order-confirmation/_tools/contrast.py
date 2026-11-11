"""Contrast van de witte hero-tekst tegen het beeld eronder (previews/_bg-*.png, tekst onzichtbaar gerenderd).
WCAG: lichtste 5% van de pixels (worst case) tegenover wit. Grote tekst >= 3:1, bodytekst >= 4.5:1.
Gebruik: python3 -I _tools/contrast.py"""
import glob, os
from PIL import Image
D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'previews')
def lum(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
for f in sorted(glob.glob(os.path.join(D, '_bg-*.png'))):
    im = Image.open(f).convert('RGB')
    L = sorted(0.2126 * lum(r) + 0.7152 * lum(g) + 0.0722 * lum(b) for r, g, b in im.getdata())
    p95 = L[int(len(L) * 0.95)]; med = L[len(L) // 2]
    print(os.path.basename(f), 'median %.1f:1' % (1.05 / (med + 0.05)), 'worst5%% %.1f:1' % (1.05 / (p95 + 0.05)))
