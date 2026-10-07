#!/usr/bin/env python3
"""Refresh the Siraat's Kitchen asset register (content/assets/index.csv).

Runs with `python3 -I scripts/refresh_assets.py [options]`. Standard library
only (PIL is optional, used only as a fallback to read image dimensions).
No secrets: Shopify data comes from JSON dumps you made with the Shopify MCP
tool (or the Admin API), Drive data comes from the public embed view.

What it does
------------
1. Shopify part (only when --dumps DIR is given): rebuilds every row with
   source shopify-product and shopify-file from the JSON dumps in DIR and
   merges them into index.csv. Rows whose image no longer exists in the dump
   are dropped. For rows that already existed, the manual columns
   (category, use, text_in_image, product_handle) are kept.
2. Shoot part (unless --no-drive): reads the two public Drive folders of the
   high production shoot through https://drive.google.com/embeddedfolderview
   and writes them as source=drive-shoot. Width and height are read from the
   first bytes of each file via drive.usercontent.google.com. Falls back to
   content/media/hp-shoot/index.csv when Drive cannot be reached.
3. Derived columns for every row:
   product_handle  Shopify handle (product images: from the product; files and
                   shoot: inferred from the title, empty when unknown)
   use             hero | product-card | detail | lifestyle | packshot |
                   not-for-email
   text_in_image   yes | no | unknown
   used_in         email ids from content/mapping/mapping.csv that use this id
   Precedence for use and text_in_image: content/assets/visual-checks.csv
   (rows that a person or Claude actually looked at) > existing value in
   index.csv > rules on category and title.

Expected input shape (--dumps DIR)
----------------------------------
DIR holds any number of *.json files. Each file is one GraphQL result page, a
list of pages, or the bare connection object. Files are recognised by content:

products (query `products`), each node:
    {"id": "gid://shopify/Product/1", "title": "...", "handle": "...",
     "status": "ACTIVE",
     "images": {"nodes": [{"id": "gid://shopify/ProductImage/2",
                           "url": "https://cdn.shopify.com/...",
                           "altText": "...", "width": 2048, "height": 2048}]}}
    Accepted wrappers: {"data": {"products": {"nodes": [...]}}},
    {"products": {"nodes"|"edges": ...}}, {"nodes": [...]}, or a list of
    those. `edges: [{node: {...}}]` works wherever `nodes` does. `media` with
    MediaImage nodes ({"id", "alt", "image": {"url","width","height"}}) is
    accepted in place of `images`.

files (query `files`, MediaImage nodes), each node:
    {"id": "gid://shopify/MediaImage/3", "alt": "...",
     "createdAt": "2025-10-15T10:00:00Z",
     "image": {"url": "https://cdn.shopify.com/...", "width": 1920,
               "height": 1280},
     "originalSource": {"fileSize": 123456}}
    Same wrappers with key "files". Non-image nodes are skipped.

The GraphQL queries that produce these dumps are in content/assets/README.md.

Options
-------
  --dumps DIR      folder with Shopify JSON dumps (omit to keep Shopify rows)
  --no-drive       skip the Drive shoot fetch, keep existing drive-shoot rows
  --index PATH     register to update (default content/assets/index.csv)
  --dry-run        print counts, do not write
"""
import argparse
import csv
import html
import io
import json
import os
import re
import sys
import urllib.request
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, 'content', 'assets', 'index.csv')
CHECKS = os.path.join(ROOT, 'content', 'assets', 'visual-checks.csv')
PRODUCTS = os.path.join(ROOT, 'content', 'facts', 'products.csv')
MAPPING = os.path.join(ROOT, 'content', 'mapping', 'mapping.csv')
SHOOT_INDEX = os.path.join(ROOT, 'content', 'media', 'hp-shoot', 'index.csv')

SHOOT_FOLDERS = {
    'images': '1eGJRW_AeQvbuYPHqnLuqBhy-VQd1SApd',
    'square': '1bvJPfwpE70CMgDKMsUo9uiDTWIxQfRph',
}
EMBED = 'https://drive.google.com/embeddedfolderview?id={}'
DOWNLOAD = 'https://drive.usercontent.google.com/download?id={}&export=download'

BASE_COLS = ['source', 'id', 'title', 'folder_or_product', 'url_or_viewurl',
             'width', 'height', 'bytes', 'category', 'notes']
NEW_COLS = ['product_handle', 'use', 'text_in_image', 'used_in']
USES = {'hero', 'product-card', 'detail', 'lifestyle', 'packshot', 'not-for-email'}


# ---------------------------------------------------------------- helpers
def num_id(gid):
    m = re.search(r'(\d+)$', gid or '')
    return m.group(1) if m else ''


def url_key(url):
    return (url or '').split('?')[0]


def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def fetch(url, limit=None, timeout=30):
    req = urllib.request.Request(url, headers={'User-Agent': 'siraat-asset-refresh/1.0'})
    if limit:
        req.add_header('Range', f'bytes=0-{limit - 1}')
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read(limit) if limit else r.read()
        size = r.headers.get('Content-Range', '').split('/')[-1] or r.headers.get('Content-Length', '')
        return data, size


# ---------------------------------------------------------------- Shopify dumps
def iter_nodes(conn):
    if not isinstance(conn, dict):
        return
    for n in conn.get('nodes') or []:
        yield n
    for e in conn.get('edges') or []:
        if isinstance(e, dict) and e.get('node'):
            yield e['node']


def find_connections(obj, key):
    """Yield every connection object stored under `key` anywhere in obj."""
    if isinstance(obj, list):
        for o in obj:
            yield from find_connections(o, key)
    elif isinstance(obj, dict):
        if key in obj and isinstance(obj[key], dict):
            yield obj[key]
        for k in ('data', 'result', 'response'):
            if k in obj:
                yield from find_connections(obj[k], key)


def load_dumps(folder):
    products, files = [], []
    for name in sorted(os.listdir(folder)):
        if not name.endswith('.json'):
            continue
        with open(os.path.join(folder, name), encoding='utf-8') as f:
            obj = json.load(f)
        got = False
        for conn in find_connections(obj, 'products'):
            products.extend(iter_nodes(conn)); got = True
        for conn in find_connections(obj, 'files'):
            files.extend(iter_nodes(conn)); got = True
        if not got:  # bare connection or list of nodes: sniff by id prefix
            nodes = list(iter_nodes(obj)) if isinstance(obj, dict) else obj if isinstance(obj, list) else []
            for n in nodes:
                gid = (n or {}).get('id', '')
                if '/Product/' in gid:
                    products.append(n)
                elif '/MediaImage/' in gid:
                    files.append(n)
    return products, files


def guess_category(title, alt=''):
    t = f'{title} {alt}'.lower()
    if re.search(r'static|_ad_|sale|%|off_|promo|banner|bundle_deal|bfcm|black_?friday', t):
        return 'ad-static'
    if re.search(r'screenshot|screen_shot|screen shot|ui_|checkout|cart', t):
        return 'ui-screenshot'
    if re.search(r'logo|emblem|icon|badge|forbes|wired|kickstarter', t):
        return 'logo'
    if re.search(r'lifestyle|kitchen|cooking|stove|chef|egg|steak|apron|_p\d', t):
        return 'lifestyle'
    if title.lower().endswith('.svg'):
        return 'other'
    return 'packshot'


def shopify_rows(products, files):
    rows = []
    for p in products:
        imgs = list(iter_nodes(p.get('images') or {}))
        for m in iter_nodes(p.get('media') or {}):
            if m.get('image'):
                imgs.append({'id': m.get('id'), 'url': m['image'].get('url'),
                             'altText': m.get('alt'), 'width': m['image'].get('width'),
                             'height': m['image'].get('height')})
        for im in imgs:
            url = im.get('url') or im.get('src') or ''
            rows.append({
                'source': 'shopify-product', 'id': im.get('id', ''),
                'title': url_key(url).rsplit('/', 1)[-1],
                'folder_or_product': p.get('title', ''), 'url_or_viewurl': url,
                'width': str(im.get('width') or ''), 'height': str(im.get('height') or ''),
                'bytes': '', 'category': '',
                'notes': f"status {p.get('status', '')}; handle {p.get('handle', '')}; alt: {im.get('altText') or ''}",
                'product_handle': p.get('handle', ''),
            })
    for fnode in files:
        img = fnode.get('image') or {}
        url = img.get('url') or ''
        if not url:
            continue
        size = ((fnode.get('originalSource') or {}).get('fileSize')) or ''
        rows.append({
            'source': 'shopify-file', 'id': fnode.get('id', ''),
            'title': url_key(url).rsplit('/', 1)[-1],
            'folder_or_product': 'Shopify Files (Content > Files)', 'url_or_viewurl': url,
            'width': str(img.get('width') or ''), 'height': str(img.get('height') or ''),
            'bytes': str(size), 'category': '',
            'notes': f"created {(fnode.get('createdAt') or '')[:10]}; alt: {fnode.get('alt') or ''}",
        })
    return rows


# ---------------------------------------------------------------- Drive shoot
ENTRY = re.compile(r'<div class="flip-entry" id="entry-([\w-]+)".*?flip-entry-title">([^<]+)<', re.S)


def image_size(data):
    """(width, height) from the first bytes of a WebP, PNG or JPEG file."""
    import struct
    if data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        chunk = data[12:16]
        if chunk == b'VP8 ':
            w, h = struct.unpack('<HH', data[26:30])
            return w & 0x3FFF, h & 0x3FFF
        if chunk == b'VP8L':
            b = data[21:25]
            return 1 + (((b[1] & 0x3F) << 8) | b[0]), 1 + (((b[3] & 0xF) << 10) | (b[2] << 2) | ((b[1] & 0xC0) >> 6))
        if chunk == b'VP8X':
            return 1 + int.from_bytes(data[24:27], 'little'), 1 + int.from_bytes(data[27:30], 'little')
    if data[:8] == b'\x89PNG\r\n\x1a\n':
        return struct.unpack('>II', data[16:24])
    if data[:2] == b'\xff\xd8':
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker, length = data[i + 1], struct.unpack('>H', data[i + 2:i + 4])[0]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, w = struct.unpack('>HH', data[i + 5:i + 9])
                return w, h
            i += 2 + length
    try:  # anything else: let PIL try, if installed
        from PIL import Image
        return Image.open(io.BytesIO(data)).size
    except Exception:
        return None


def drive_dims(file_id):
    for _ in range(3):
        try:
            data, size = fetch(DOWNLOAD.format(file_id), limit=65536)
            wh = image_size(data)
            if wh:
                return str(wh[0]), str(wh[1]), size
        except Exception:
            pass
    return '', '', ''


def shoot_rows(old_by_id):
    rows = []
    try:
        for folder, fid in SHOOT_FOLDERS.items():
            page, _ = fetch(EMBED.format(fid))
            for did, title in ENTRY.findall(page.decode('utf-8', 'replace')):
                rows.append((folder, html.unescape(title).strip(), did))
        print(f'drive: {len(rows)} shoot images read from the embed view')
    except Exception as e:  # network blocked: use the local copy of the listing
        print(f'drive: embed view not reachable ({e}); using {SHOOT_INDEX}')
        rows = [(r['folder'], r['title'], r['drive_id']) for r in read_csv(SHOOT_INDEX)]
    out = []
    for folder, title, did in rows:
        old = old_by_id.get(did, {})
        w, h, b = old.get('width', ''), old.get('height', ''), old.get('bytes', '')
        if not w:
            w, h, b = drive_dims(did)
        shot = title.split('_')[0]
        out.append({
            'source': 'drive-shoot', 'id': did, 'title': title,
            'folder_or_product': f'HP shoot / {folder}',
            'url_or_viewurl': f'https://drive.google.com/file/d/{did}/view',
            'width': w, 'height': h, 'bytes': b,
            'category': 'packshot' if shot.startswith('P11') else 'lifestyle',
            'notes': f'high production shoot, shot {shot}; folder id {SHOOT_FOLDERS.get(folder, "")}',
        })
    return out


# ---------------------------------------------------------------- derived columns
SHOOT_HANDLE = {
    'P02': 'titanium-hammered-cookware-set', 'P022': 'titanium-hammered-cookware-set',
    'P03': 'titanium-hammered-cookware-set', 'P05': 'titanium-hammered-cookware-set',
    'P06': 'titanium-hammered-pan-pro-incl-lid',
}
PAN_PRO = 'original-siraat-100-pure-titanium-pan-with-hammered-pattern'
TITLE_RULES = [  # (regex on normalised title, handle); first match wins
    (r'just everything|34 ?pcs', 'the-just-everything-bundle-34-pcs'),
    (r'full hammered pro', 'full-hammered-pro-edition'),
    (r'cookware ?set ?pro|cookwaresetpro|pro ?set\b', 'titanium-hammered-cookware-set-pro'),
    (r'12 ?pcs?\b|12 ?piece|12pc|cookware ?set', 'titanium-hammered-cookware-set'),
    (r'6 ?pcs?\b|6 ?piece|6pcs', 'titanium-hammered-pan-set-with-lids-6-pcs'),
    (r'complete edition|hammered collection|4 ?pcs', 'the-hammered-collection'),
    (r'roast', 'titanium-hammered-roasting-pan'),
    (r'pizza ?wheel|pizza ?cutter', 'pizza-wheel'),
    (r'pizza', 'titanium-hammered-pizza-steel'),
    (r'crepe|crêpe', 'titanium-hammered-crepe-pan-pro'),
    (r'wok', 'titanium-hammered-wok-pan-pro'),
    (r'deep ?pan', 'titanium-hammered-deep-pan-pro'),
    (r'7[,.]?5 ?l', '7-5-litre-titanium-hammered-pot-with-lid'),
    (r'\b3 ?l(itre)?\b', '3-litre-titanium-hammered-pot-with-lid'),
    (r'\b2 ?l(itre)?\b', '2-litre-titanium-hammered-pot-with-lid'),
    (r'\bpots?\b|stock ?pot|sauce ?pan', 'titanium-hammered-cookware-set'),
    (r'gold', 'titanium-cutting-board-v2-gold-edition'),
    (r'non ?slip|mat for', 'siraat-non-slip-mat-for-board-premium-silicone'),
    (r'diatomite', 'diatomite-mat-anthracite-ultra-hygienic-fast-drying-mold-resistant'),
    (r'cutting ?board|titanboard|prep ?board|\bboard', 'titanium-cutting-board-v2'),
    (r'utensil|spatula|turner|flipper|ladle|skimmer', 'siraat-pure-titanium-utensils-bundle'),
    (r'\bsalt\b|pepper|\bmills?\b|hex ?mills?|grinder', 'salt-pepper-mill-set'),
    (r'apron.*azure|azure', 'siraat-signature-apron-azure'),
    (r'apron.*moss|moss', 'siraat-signature-apron-moss'),
    (r'apron.*ember|ember', 'siraat-signature-apron-ember'),
    (r'apron.*oak|\boak', 'siraat-signature-apron-oak'),
    (r'trivet', 'magnetic-cherry-wood-trivet'),
    (r'ice ?cube', 'siraat-titanium-ice-cubes'),
    (r'bottle', 'titanium-water-bottle'),
    (r'chopstick', 'titanium-chopsticks'),
    (r'straw', 'titanium-straws'),
    (r'grill ?press|smash', 'grill-press'),
    (r'sharpener', 'rolling-knife-sharpener-diamond-ceramic'),
    (r'tote', 'tote-bag'),
    (r'tea ?filter', 'titanium-tea-filter'),
    (r'dishwasher ?sheet|detergent', 'dishwashing-detergent-sheets-fresh-lemon'),
    (r'gift ?card', 'e-gift-card'),
    (r'pan ?pro ?mini|\bmini\b', 'titanium-hammered-pan-pro-mini'),
    (r'pan ?pro ?small|\bsmall\b', 'titanium-hammered-pan-pro-small'),
    (r'pan ?pro ?large|\blarge\b', 'titanium-hammered-pan-pro-large'),
    (r'\blid\b', None),  # handled below: pan + lid = Pan Pro, lid alone = lid
    (r'hammered ?pan|pan ?pro|panpro|frying ?pan|hammeredpan|titanium ?pan|\bpan\b', PAN_PRO),
]


NOT_OURS = r'taima|our ?place|hexclad|caraway|greenpan|made ?in cookware|always ?pan|teflon|cast ?iron|competitor'


def norm_title(t):
    t = re.sub(r'\.(webp|jpe?g|png|gif|svg|heic|avif)$', '', t.lower())
    t = re.sub(r'([a-z])([0-9])', r'\1 \2', t)
    t = re.sub(r'[_\-]+', ' ', t)
    t = re.sub(r'([a-z])(pan|board|set|lid)\b', r'\1 \2', t)
    return t


def infer_handle(row, valid):
    title = row['title']
    m = re.match(r'(P\d{2,3})-', title)
    if m and (row['source'] == 'drive-shoot' or row['source'] == 'shopify-file'):
        return SHOOT_HANDLE.get(m.group(1), PAN_PRO)
    t = norm_title(title + ' ' + (row.get('notes', '').split('alt:', 1)[-1] if 'alt:' in row.get('notes', '') else ''))
    if re.search(NOT_OURS, t):
        return ''
    for rx, handle in TITLE_RULES:
        if re.search(rx, t):
            if handle is None:
                return PAN_PRO if re.search(r'\bpan\b', t) else 'stainless-steel-lid'
            return handle if handle in valid else ''
    return ''


def rule_use(row):
    cat, title = row['category'], row['title'].lower()
    if cat in ('ad-static', 'ui-screenshot', 'logo', 'other') or title.endswith('.svg'):
        return 'not-for-email'
    if cat == 'product-cutout':
        return 'product-card'
    if cat == 'lifestyle':
        return 'lifestyle'
    return 'packshot'


def rule_text(row):
    cat = row['category']
    if cat in ('ad-static', 'ui-screenshot', 'logo'):
        return 'yes'
    return 'unknown'


def mapping_index():
    """numeric Shopify id or Drive id -> set of email ids."""
    used = defaultdict(set)
    if not os.path.exists(MAPPING):
        return used
    for r in read_csv(MAPPING):
        email = r.get('email', '')
        blob = ' '.join(v for v in r.values() if v)
        for n in re.findall(r'\b\d{11,15}\b', blob):
            used[n].add(email)
        for d in re.findall(r'\b1[\w-]{32}\b', blob):
            used[d].add(email)
    return used


def email_sort(e):
    order = 'WCKBPR'
    return (order.index(e[0]) if e and e[0] in order else 9, e)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--dumps')
    ap.add_argument('--no-drive', action='store_true')
    ap.add_argument('--index', default=INDEX)
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()

    old = read_csv(a.index)
    print(f'read {len(old)} rows from {a.index}')
    for r in old:
        for c in NEW_COLS:
            r.setdefault(c, '')
    keep = {(r['source'], r['id'], r['folder_or_product']): r for r in old}

    rows = []
    if a.dumps:
        products, files = load_dumps(a.dumps)
        print(f'dumps: {len(products)} products, {len(files)} files')
        fresh = shopify_rows(products, files)
        if not fresh:
            sys.exit('dumps contained no Shopify images; nothing changed')
        seen = set()
        for r in fresh:
            k = (r['source'], r['id'], r['folder_or_product'])
            prev = keep.get(k)
            if prev:
                for c in ('category', 'use', 'text_in_image', 'product_handle'):
                    if prev.get(c):
                        r[c] = prev[c]
            if not r['category']:
                r['category'] = guess_category(r['title'], r['notes'])
                r['notes'] += '; category guessed by refresh_assets.py'
            seen.add(k)
            rows.append(r)
        dropped = sum(1 for r in old if r['source'].startswith('shopify') and
                      (r['source'], r['id'], r['folder_or_product']) not in seen)
        print(f'shopify: {len(fresh)} rows from dumps, {dropped} old rows no longer in Shopify')
    else:
        rows += [r for r in old if r['source'].startswith('shopify')]

    rows += [r for r in old if not r['source'].startswith('shopify') and r['source'] != 'drive-shoot']

    old_shoot = {r['id']: r for r in old if r['source'] == 'drive-shoot'}
    if a.no_drive:
        rows += list(old_shoot.values())
    else:
        for r in shoot_rows(old_shoot):
            prev = old_shoot.get(r['id'], {})
            for c in NEW_COLS:
                r[c] = prev.get(c, '')
            rows.append(r)

    # visual checks: by Drive id / numeric Shopify id, and by CDN url path
    checks_by_key, checks_by_url = {}, {}
    if os.path.exists(CHECKS):
        for c in read_csv(CHECKS):
            checks_by_key[c['key']] = c
            if c.get('url_path'):
                checks_by_url[c['url_path']] = c
    valid = {r['handle'] for r in read_csv(PRODUCTS)}
    used = mapping_index()

    # shoot <-> Shopify copies (same shot name, same aspect) share used_in
    def shot_key(r):
        if r['source'] == 'drive-shoot':
            shape = 'square' if r['folder_or_product'].endswith('square') else 'wide'
        else:
            shape = 'square' if r['width'] == r['height'] else 'wide'
        return re.match(r'(P\d{2,3}-[A-Z])', r['title']).group(1), shape
    shopify_copies = defaultdict(set)
    for r in rows:
        if r['source'] == 'shopify-file' and re.match(r'P\d{2,3}-[A-Z]', r['title']) and r['width']:
            shopify_copies[shot_key(r)].add(num_id(r['id']))

    for r in rows:
        nid = num_id(r['id']) if r['source'].startswith('shopify') else r['id']
        chk = checks_by_key.get(nid) or checks_by_url.get(url_key(r['url_or_viewurl']))
        if r['source'] == 'shopify-product':
            m = re.search(r'handle ([^;]+)', r['notes'])
            r['product_handle'] = m.group(1).strip() if m else r.get('product_handle', '')
        elif not r.get('product_handle'):
            r['product_handle'] = infer_handle(r, valid)
        if r['source'] in ('figma',):
            r['product_handle'] = r['product_handle'] if r['product_handle'] in valid else ''
        if chk and chk['use'] in USES:
            r['use'], r['text_in_image'] = chk['use'], chk['text_in_image']
        else:
            if r.get('use') not in USES:
                r['use'] = rule_use(r)
            if r.get('text_in_image') not in ('yes', 'no', 'unknown'):
                r['text_in_image'] = rule_text(r)
        if r['category'] == 'ad-static':  # baked-in text always wins
            r['use'], r['text_in_image'] = 'not-for-email', 'yes'
        emails = set(used.get(nid, ()))
        if r['source'] == 'drive-shoot' and re.match(r'P\d{2,3}-[A-Z]', r['title']):
            for sid in shopify_copies.get(shot_key(r), ()):
                emails |= used.get(sid, set())
        r['used_in'] = ','.join(sorted(emails, key=email_sort))

    cols = BASE_COLS + NEW_COLS
    print(f'writing {len(rows)} rows')
    print('use:', dict(Counter(r['use'] for r in rows).most_common()))
    print('text_in_image:', dict(Counter(r['text_in_image'] for r in rows).most_common()))
    print('hero without text:', sum(1 for r in rows if r['use'] == 'hero' and r['text_in_image'] == 'no'))
    print('rows with used_in:', sum(1 for r in rows if r['used_in']))
    if a.dry_run:
        return
    with open(a.index, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)


if __name__ == '__main__':
    main()
