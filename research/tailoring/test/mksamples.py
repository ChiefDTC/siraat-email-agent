"""Maakt per productcategorie een voorbeeld-event per trigger (productmatrix, research/tailoring/10-productmatrix.md).
Gebruik: python3 mksamples.py   (schrijft samples/<trig>_x_<cat>.json; bestaande samples blijven ongemoeid)
Triggers: co = Checkout Started, atc = Added to Cart, vp = Viewed Product, po = Placed Order (US-verzendadres).
Titels exact zoals in de echte events (research/tailoring/00-data.md, sectie Titels). Prijzen = USD-shopprijs (content/products/README.md)."""
import json, os, copy
H = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(H, 'samples')
P = '/home/user/siraat-email-agent/content/products/'
# cat: (titel, prijs, beeld)
CATS = {
 'mini':     ('Titanium Hammered Pan Pro Mini', 129, 'titanium-hammered-pan-pro'),
 'small':    ('Titanium Hammered Pan Pro Small', 127, 'titanium-hammered-pan-pro'),
 'standard': ('Titanium Hammered Pan Pro Standard', 134, 'titanium-hammered-pan-pro'),
 'large':    ('Titanium Hammered Pan Pro Large', 139, 'titanium-hammered-pan-pro'),
 'deep':     ('Titanium Hammered Deep Pan Pro', 139, 'titanium-hammered-deep-pan-pro'),
 'wok':      ('Titanium Hammered Wok Pan Pro', 139, 'titanium-hammered-wok-pan-pro'),
 'crepe':    ('Titanium Hammered Crêpe Pan Pro', 139, 'titanium-hammered-crepe-pan-pro'),
 'pizza':    ('Titanium Hammered Pizza Steel', 129, 'titanium-hammered-pizza-steel'),
 'roast':    ('Titanium Hammered Roasting Pan', 199, 'titanium-hammered-roasting-pan'),
 'pot':      ('3 Litre Titanium Hammered Pot With Lid', 179, 'titanium-hammered-cookware-set'),
 'set6':     ('Titanium Hammered Pan Set With Lids | 6-Pcs', 349, 'titanium-hammered-pan-set-with-lids-6-pcs'),
 'set12':    ('Titanium Hammered Cookware Set | 12-Pcs', 599, 'titanium-hammered-cookware-set'),
 'setbig':   ('Titanium Hammered Cookware Set Pro', 479, 'titanium-hammered-cookware-set-pro'),
 'setall':   ('The Just Everything Bundle | 34-Pcs', 1499, 'full-hammered-pro-edition'),
 'lid':      ('Stainless Steel Lid', 59, 'stainless-steel-lid'),
 'apron':    ('Siraat Signature Apron (Moss)', 49, 'siraat-signature-apron'),
 'board':    ('Titanium Cutting Board (Anti-Microbial)', 89, 'titanium-cutting-board-v2'),
 'utensil':  ('Titanium Utensil Set Bundle', 149, 'titanium-cutting-board-v2'),
 'mill':     ('Salt & Pepper Mill Set', 124, 'salt-pepper-mill-set'),
 'sheets':   ('Plastic-Free Dishwasher Sheets', 25, 'dishwashing-detergent-sheets-fresh-lemon'),
 'giftcard': ('E-Gift Card', 100, 'e-gift-card'),
}
# Echte afwijkende Shopify-titels (audit 01 S2): moeten in dezelfde categorie vallen
EXTRA = {'set6bday': ('Titanium Hammered Pan Set With Lids | 6-Pcs (BDAY SALE)', 349, 'titanium-hammered-pan-set-with-lids-6-pcs'),
         'set12pizza': ('Titanium Hammered Cookware Set | 12-Pcs | + FREE PIZZA STEEL', 699, 'titanium-hammered-cookware-set'),
         'stdbday': ('Titanium Hammered Pan Pro Standard (BDAY SALE)', 119, 'titanium-hammered-pan-pro'),
         'panlidstd': ('Titanium Hammered Pan Pro Standard With Lid', 186, 'titanium-hammered-pan-pro')}
def img(h):
    d = P + h + '/img/'
    f = sorted(x for x in os.listdir(d) if x.endswith('.jpg'))
    return d + f[0]
def order_like(base, title, price, im, us):
    d = json.load(open(os.path.join(S, base)))
    d['Items'] = [title] + d['Items'][1:]
    d['$value'] = price
    for k in ('$extra', 'extra'):
        li = d[k]['line_items'][0]
        li.update({'title': title, 'price': price, 'line_price': price})
        li['product']['images'] = [{'thumb_src': im, 'src': im}]
        if us is not None: d[k]['shipping_address'] = {'country_code': us}
    return d
def main():
    n = 0
    for c, (t, p, h) in list(CATS.items()) + list(EXTRA.items()):
        im = img(h)
        json.dump(order_like('co_pan.json', t, p, im, None), open(os.path.join(S, 'co_x_%s.json' % c), 'w'), ensure_ascii=False)
        json.dump(order_like('po_pan_us.json', t, p, im, 'US'), open(os.path.join(S, 'po_x_%s.json' % c), 'w'), ensure_ascii=False)
        if c in EXTRA: n += 2; continue
        json.dump({'Product Name': t, 'Price': p, 'Quantity': 1, 'ImageURL': im + '?v=1', 'URL': 'https://2d0add-d6.myshopify.com/products/x', '$currency': 'USD', '_ip_country_code': 'US', '$value': p},
                  open(os.path.join(S, 'atc_x_%s.json' % c), 'w'), ensure_ascii=False)
        json.dump({'Name': t, 'Price': '$%d' % p, 'ImageURL': im + '?v=1', 'URL': 'https://siraatskitchen.com/products/x'},
                  open(os.path.join(S, 'vp_x_%s.json' % c), 'w'), ensure_ascii=False)
        n += 4
    print('ok', n, 'samples')
if __name__ == '__main__': main()
