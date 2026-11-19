"""Hero-beelden PP viewed upsell, versie 19 nov avond (Floris: harde schaduw). Photoroom-uitsnede (post-purchase-v5/gen/clean)
met harde schaduw (post-purchase-v5/_tools/hardshadow.py) op crème #F3EEE6, 1200x760 (weergave 600). Vervangt ppv-set12.jpg/ppv-set6.jpg
(oude bestanden blijven staan). python3 -I _tools/make_img_hard.py   (vanuit de map post-purchase-viewed)"""
import os, sys
from PIL import Image
D = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
V5 = os.path.join(D, '../post-purchase-v5')
sys.path.insert(0, os.path.join(V5, '_tools'))
from hardshadow import hard
BG = (243, 238, 230)
def make(key, out, maxw, maxh, rot=0, H=760):
    g = hard(os.path.join(V5, f'gen/clean/cut-{key}.png'), rot, os.path.join(V5, 'gen/hard', f'ppv-{key}_{rot}.png'))
    im = Image.open(g).convert('RGBA')
    s = min(maxw / im.width, maxh / im.height, 1.0)
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    c = Image.new('RGBA', (1200, H), BG + (255,))
    c.alpha_composite(im, ((1200 - im.width) // 2, H - 40 - im.height))
    c.convert('RGB').save(os.path.join(D, 'assets', out), quality=84, optimize=True, progressive=True)
    print(out, os.path.getsize(os.path.join(D, 'assets', out)) // 1024, 'KB', im.size)
make('s12', 'ppv-set12-hard.jpg', 1000, 680, -3)
make('s06', 'ppv-set6-hard.jpg', 980, 670, -4)
