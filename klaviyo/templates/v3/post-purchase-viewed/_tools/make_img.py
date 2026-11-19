"""Productbeelden PP viewed upsell (19 nov 2026): uitsnede met grondschaduw (v6d ground.py) op crème #F3EEE6, 1200x760 (weergave 600).
python3 -I _tools/make_img.py   (vanuit de map post-purchase-viewed)"""
import os, sys
from PIL import Image
D = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
V6 = os.path.join(D, '../welcome/v6d-envelope-rich')
sys.path.insert(0, os.path.join(V6, '_tools'))
from ground import ground
BG = (243, 238, 230)
def make(cut, out, maxw, maxh, rot=0, H=760):
    g = ground(cut, rot, os.path.join(D, 'gen', 'g-' + os.path.basename(cut)))
    im = Image.open(g).convert('RGBA')
    s = min(maxw / im.width, maxh / im.height, 1.0)
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    W = 1200
    c = Image.new('RGBA', (W, H), BG + (255,))
    c.alpha_composite(im, ((W - im.width) // 2, H - 60 - im.height))
    c.convert('RGB').save(os.path.join(D, 'assets', out), quality=84, optimize=True, progressive=True)
    print(out, os.path.getsize(os.path.join(D, 'assets', out)) // 1024, 'KB', im.size)
make(os.path.join(V6, 'gen/cut-set12.png'), 'ppv-set12.jpg', 1000, 640)
make(os.path.join(V6, 'gen/cut-set6.png'), 'ppv-set6.jpg', 980, 620, -4)
