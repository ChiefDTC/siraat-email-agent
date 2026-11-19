"""BF-W1 B · 12pcs top (US) · TEST (19 nov 2026), kopie van bf-w1-image-b. NIET LIVE. Bovenste aanbod per land: VS 12-Pcs (bf-top12), rest 6-Pcs (bf-top6);
lagere dubbele kaart per tak weg (VS zonder card-set12-wide, rest met card-standard-wide in plaats van de rij standard + set6). Landconditie als scripts/v5lib.py.
Origineel: BF-W1 image B (concept, 18 nov 2026). NIET LIVE. B-variant voor de A/B in flow Rn556d (A = template XXg4sn).
Zelfde aanbod en prijzen als A, geen nep-urgentie (geen 'ends at midnight', geen '92% claimed').
Header en footer uit klaviyo/templates/partials (zoals v6d build.py). Geen discount-redirect (geen code), wel UTM.
Gebruik: python3 -I _tools/build.py   -> bf-w1-image-b.html (Klaviyo, CDN-beelden) en bf-w1-image-b-preview.html
Zonder klaviyo-urls.txt wijzen de beelden naar de lokale bestanden (alleen voor previews).
"""
import re, os, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../../..'))
V6D = os.path.join(REPO, 'klaviyo/templates/v3/welcome/v6d-envelope-rich')
P = os.path.join(REPO, 'klaviyo/templates/partials')
def load(p): return dict(l.split() for l in open(p) if len(l.split()) == 2) if os.path.exists(p) else {}
urls = load(os.path.join(P, 'shared/klaviyo-urls.txt'))
urls.update(load(os.path.join(REPO, 'klaviyo/templates/v3/campaigns/thanksgiving-roast-1117/assets/klaviyo-urls.txt')))
V6U = load(os.path.join(V6D, 'klaviyo-urls.txt'))
OWN = load(os.path.join(ROOT, 'klaviyo-urls.txt'))
REUSE = ['gifts-flatlay.jpg', 'e1-reviews.jpg', 'torn-AC3B19-ECE7DD.jpg', 'torn-ECE7DD-282828.jpg', 'torn-282828-ECE7DD.jpg', 'torn-ECE7DD-F8F7F2.jpg']
def src(key, local):
    """CDN-url als die er is, anders lokaal pad (preview)."""
    if key in REUSE: return (V6U.get(key) if not local else None) or os.path.join(V6D, 'sections', key)
    return (OWN.get(key) if not local else None) or os.path.join(ROOT, 'sections', key)

CAMP = 'bfcm-welcome-b-12pcs-top'
H = {'duo': '2-pans-and-2-lids', 'standard': 'original-siraat-100-pure-titanium-pan-with-hammered-pattern',
     'set6': 'titanium-hammered-pan-set-with-lids-6-pcs', 'set12': 'titanium-hammered-cookware-set'}
F = "font-family:Inter,Arial,Helvetica,sans-serif;"
INK, BODY, BRICK, CREAM, SAND, DARK, W = '#272727', '#2E2E2E', '#AC3B19', '#F8F7F2', '#ECE7DD', '#282828', '#FFFFFF'
FR = 'Free shipping. 30-day returns. 100,000+ happy customers.'
SUBJECT = 'Black Friday is live. No code needed.'
PREVIEW = 'Up to 70% off pans and sets, plus 5 free gifts with every order.'

def U(c, path='/collections/black-friday-sale'):
    return f'https://siraatskitchen.com{path}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={c}'
def UP(c, k): return U(c, '/products/' + H[k])

class Mail:
    def __init__(s): s.rows = []  # (soort, data)
    def add(s, h): s.rows.append(('html', h)); return s
    def img(s, key, alt, href): s.rows.append(('img', (key, alt, href))); return s
    def pair(s, items): s.rows.append(('pair', items)); return s
    def torn(s, a, b): return s.img(f'torn-{a[1:]}-{b[1:]}.jpg', '', U('edge'))
    def live(s, bg, inner, pad='22px 40px 26px 40px'):
        return s.add(f'<tr><td align="center" bgcolor="{bg}" class="pad" style="background-color:{bg};padding:{pad};text-align:center;">{inner}</td></tr>\n')
    @staticmethod
    def btn(label, href, dark):
        bb, fc = (W, INK) if dark else (INK, W)
        return (f'<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="400" style="width:100%;max-width:400px;margin:0 auto;"><tr><td align="center" bgcolor="{bb}" style="background-color:{bb};border-radius:40px;">'
                f'<a href="{href}" style="display:block;padding:19px 16px;{F}font-size:15px;line-height:18px;font-weight:600;letter-spacing:1.2px;color:{fc};text-decoration:none;text-transform:uppercase;">{label} &rarr;</a></td></tr></table>')
    def cta(s, bg, label, href, dark=False, sub=None, lead=None, pad='6px 40px 32px 40px'):
        sc = '#F1D9CB' if bg == BRICK else ('#CFC8BC' if dark else '#727272')
        tc = W if bg in (BRICK, DARK) else BODY
        top = f'<div class="lead" style="{F}font-size:17px;line-height:27px;font-weight:400;color:{tc};padding-bottom:18px;">{lead}</div>' if lead else ''
        return s.live(bg, top + s.btn(label, href, dark) + (f'<div style="{F}font-size:12px;line-height:18px;color:{sc};padding-top:10px;">{sub}</div>' if sub else ''), pad)
    def render(s, local):
        out, imgs = '', []
        for kind, d in s.rows:
            if kind == 'html': out += d
            elif kind == 'img':
                key, alt, href = d; imgs.append(key)
                out += f'<tr><td style="padding:0;font-size:0;line-height:0;"><a href="{href}" style="display:block;border:0;"><img src="{src(key, local)}" width="600" alt="{alt}" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>\n'
            else:
                cells = ''
                for key, alt, href in d:
                    imgs.append(key)
                    cells += f'<td width="50%" valign="top" style="width:50%;padding:0;font-size:0;line-height:0;"><a href="{href}" style="display:block;"><img src="{src(key, local)}" width="300" alt="{alt}" style="display:block;width:100%;max-width:300px;height:auto;border:0;"></a></td>'
                out += f'<tr><td bgcolor="{SAND}" style="background-color:{SAND};padding:0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cells}</tr></table></td></tr>\n'
        return out, imgs

hdr = open(os.path.join(P, 'header.html')).read(); ftr = open(os.path.join(P, 'footer.html')).read()
for k, v in urls.items():
    hdr = hdr.replace('{{SHARED}}/' + k, v); ftr = ftr.replace('{{SHARED}}/' + k, v).replace('{{IMG}}/' + k, v)
hdr = re.sub(r'<!--.*?-->\n?', '', hdr, flags=re.S); ftr = re.sub(r'<!--.*?-->\n?', '', ftr, flags=re.S)
def utm_nav(h, tag):
    return re.sub(r'href="(https://(?:www\.)?siraatskitchen\.com[^"?]*)"', lambda m: f'href="{m.group(1)}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={tag}-{(m.group(1).rstrip("/").split("/")[-1] or "home").replace(".com", "home")}"', h)
HEAD = open(os.path.join(REPO, 'klaviyo/templates/v3/welcome/v6-envelope/e1.html')).read().split('<body')[0]

# ======================= mail
e = Mail()
e.add(f'<tr><td align="center" bgcolor="{INK}" style="background-color:{INK};padding:11px 16px;{F}font-size:11px;line-height:15px;letter-spacing:2px;font-weight:600;color:{CREAM};text-transform:uppercase;">'
      f'<a href="{U("codebar")}" style="color:{CREAM};text-decoration:none;">Free shipping &middot; 30-day returns &middot; 75-year warranty</a></td></tr>\n')
e.add('{{HEADER}}\n')
e.img('bf-hero.jpg', 'Black Friday sale is live: up to 70% off. No code needed, 5 free gifts with every order. Two hands hold up hammered titanium Pan Pro pans against a brick red background.', U('hero'))
e.cta(BRICK, 'See my Black Friday prices', U('cta1'), dark=True, sub=FR, pad='4px 40px 34px 40px',
      lead='Your Black Friday price is already on every pan and set. Nothing to copy, nothing to type at checkout.')
e.torn(BRICK, SAND)
e.add("<!--{% with mpc=person.Country mpcc=person|lookup:'country_code' %}{% if mpc == 'United States' or mpc == 'US' or not mpc and mpcc == 'US' %}-->\n")
e.img('bf-top12.jpg', 'Start here, the complete kitchen: Cookware Set, 12 pieces, 3 pans, 3 pots and 6 lids. 68% off: $649, was $2,047. Black Friday price, no code.', UP('top12', 'set12'))
e.cta(SAND, 'Get the 12-piece set for $649', UP('top12-cta', 'set12'), sub=FR, pad='0 40px 30px 40px')
e.add('<!--{% else %}-->\n')
e.img('bf-top6.jpg', 'Start here, three pans, three lids: Pan Set, 6 pieces, 3 pans and 3 fitted lids. 70% off: $299, was $997. Black Friday price, no code.', UP('top6', 'set6'))
e.cta(SAND, 'Get the 6-piece set for $299', UP('top6-cta', 'set6'), sub=FR, pad='0 40px 30px 40px')
e.add('<!--{% endif %}{% endwith %}-->\n')
e.img('bf-h-more.jpg', 'The rest of the sale: pick your pan or your whole kitchen.', U('h-more'))
e.add("<!--{% with mpc=person.Country mpcc=person|lookup:'country_code' %}{% if mpc == 'United States' or mpc == 'US' or not mpc and mpcc == 'US' %}-->\n")
e.pair([('card-standard.jpg', 'Pan Pro Standard, 11 inch, 28 cm. 69% off: $149, was $480.', UP('card-standard', 'standard')),
        ('card-set6.jpg', 'Pan Set, 6 pieces: 3 pans and 3 fitted lids. 70% off: $299, was $997.', UP('card-set6', 'set6'))])
e.add('<!--{% else %}-->\n')
e.img('card-standard-wide.jpg', 'Pan Pro Standard, our bestseller, 11 inch, 28 cm. 69% off: $149, was $480.', UP('card-standard', 'standard'))
e.img('card-set12-wide.jpg', 'Cookware Set, 12 pieces: 3 pans, 3 pots and 6 lids, the complete kitchen. 68% off: $649, was $2,047.', UP('card-set12', 'set12'))
e.add('<!--{% endif %}{% endwith %}-->\n')
e.torn(SAND, DARK)
e.img('bf-reasons.jpg', 'Why now, five honest reasons, no countdown. 1: Black Friday prices, up to 70% off pans and sets. 2: No code needed, the sale price is already on the product page. 3: 5 free gifts in the box with every order. 4: 30-day returns, unused within 30 days of delivery, full refund. 5: 75-year warranty against defects; a pure titanium cooking surface with no coatings, so nothing to wear off.', U('reasons'))
e.torn(DARK, SAND)
e.img('gifts-flatlay.jpg', '5 free gifts in the box with every order: free shipping, the Favorites Cookbook, the plastic-free e-book, a mystery gift and a chance to win a PFAS water filter.', U('gifts'))
e.torn(SAND, CREAM)
e.img('e1-reviews.jpg', 'Five stars from 100,000+ happy customers. Tammy: I am on my 4th pan from Siraat, I even gifted one to my son. Sunny C.: I ordered one pan to try it out, now I am ordering the set.', UP('reviews', 'standard'))
e.cta(CREAM, 'See my Black Friday prices', U('cta2'), sub=FR, pad='4px 40px 12px 40px')
e.live(CREAM, f'<div style="{F}font-size:16px;line-height:26px;color:{BODY};text-align:left;">Not sure where to start? The Pan Pro Standard is our bestseller, $149 this Black Friday. Reply and our team will help you pick.</div>'
       f'<div style="{F}font-size:16px;line-height:24px;color:{INK};text-align:left;font-weight:600;padding-top:14px;">Benjamin</div><div style="{F}font-size:14px;line-height:20px;color:#8A847A;text-align:left;">Founder, Siraat</div>', '18px 40px 30px 40px')
e.add('{{FOOTER}}\n')

def page(local):
    body, imgs = e.render(local)
    head = re.sub(r'<title>[^<]*</title>', f'<title>{SUBJECT}</title>', HEAD)
    body = body.replace('{{HEADER}}', utm_nav(hdr, 'nav')).replace('{{FOOTER}}', utm_nav(ftr, 'ft'))
    html = (head + '<body style="margin:0;padding:0;background:#FFFFFF;">\n'
            f'<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;">{PREVIEW}' + '&#847;&zwnj;&nbsp;' * 60 + '</div>\n'
            '<table bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;" width="100%">\n<tr><td align="center" style="padding:8px 0 32px 0;">\n'
            f'<table bgcolor="{CREAM}" border="0" cellpadding="0" cellspacing="0" class="w" role="presentation" style="width:100%;max-width:600px;background-color:{CREAM};" width="600">\n'
            + body + '</table>\n</td></tr>\n</table>\n</body>\n</html>\n')
    assert '—' not in html
    assert '{{SHARED}}' not in html and '{{IMG}}' not in html
    assert 'discount/' not in html
    return html, imgs

html, imgs = page(local=not OWN)
open(os.path.join(ROOT, 'bf-w1-b-12pcs-top.html'), 'w').write(html)
prev, _ = page(local=True)
prev = prev.replace("{{ first_name|default:'there' }}", 'Sarah').replace('{{ organization.name }}', "Siraat's Kitchen").replace('{{ organization.full_address }}', '(address)')
IFX = re.escape("<!--{% with mpc=person.Country mpcc=person|lookup:'country_code' %}{% if mpc == 'United States' or mpc == 'US' or not mpc and mpcc == 'US' %}-->")
for nm, us in (('us', True), ('int', False)):
    x = re.sub(IFX + r'(.*?)' + re.escape('<!--{% else %}-->') + r'(.*?)' + re.escape('<!--{% endif %}{% endwith %}-->'), lambda m: m.group(1 if us else 2), prev, flags=re.S)
    assert '{% if' not in x
    x = re.sub(r'\{%.*?%\}', '#', x); x = re.sub(r'\{\{.*?\}\}', '', x)
    open(os.path.join(ROOT, f'preview-{nm}.html'), 'w').write(x)
kb = sum(os.path.getsize(src(k, True)) for k in set(imgs)) // 1024
w = {'html_kb': len(html) // 1024, 'images': len(set(imgs)), 'images_kb': kb, 'total_kb_est': len(html) // 1024 + kb + 30}
json.dump(w, open(os.path.join(ROOT, 'sections/weights.json'), 'w'))
print('cdn' if OWN else 'local', w, sorted(set(imgs)))
