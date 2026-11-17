"""Welcome v6b 'Sealed envelope, direct response' (concept, 17 nov 2026). NIET LIVE, niet in Klaviyo als template of flow.
Feedback Floris op v6: veel meer direct response, upsells, verkopen eerst; envelop alleen als lichte draad.
Bouwt e1..e5.html (Klaviyo) en e1..e5-preview.html in de map erboven. Gebruik: python3 -I _tools/build.py
Spec: klaviyo/flows/welcome-v6b-envelope-dr.md

Prijzen: Shopify Admin API, 17 nov 2026 (US, USD). Geen doorgestreepte compare-at (zie spec). Besparing alleen als echte som
van losse Shopify-prijzen. HI10: Shopify DiscountCodeNode 1737555870036, 10% op alles, 1x per klant, geen einddatum.
"""
import re, os
from urllib.parse import quote
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../../..'))
P = os.path.join(REPO, 'klaviyo/templates/partials')
def load_urls(path): return dict(l.split() for l in open(path) if len(l.split()) == 2)
urls = load_urls(os.path.join(P, 'shared/klaviyo-urls.txt'))
urls.update(load_urls(os.path.join(REPO, 'klaviyo/templates/v3/campaigns/thanksgiving-roast-1117/assets/klaviyo-urls.txt')))
urls.update(load_urls(os.path.join(ROOT, 'assets/klaviyo-urls.txt')))
urls['gift-cookbook.jpg'] = 'https://cdn.klaviyomail.com/company/TdtTzz/images/dabf0446-a5d7-49ae-87f8-672e5692bf5b.jpeg'

CAMP, CODE = 'v6b-welcome-dr', 'HI10'
GIFTS = '5 free gifts with every order'  # [VRAAG FLORIS] als de gifts na BF stoppen: hier aanpassen, staat overal via deze constante
REPORT = 'https://siraatskitchen.com/pages/third-party-testing'

# ---- Shopify, 17 nov 2026 (variants.price), US
PR = {  # sleutel: (titel, korte naam, handle, prijs, beeld, maat)
    'mini':     ('Titanium Hammered Pan Pro Mini', 'Pan Pro Mini', 'titanium-hammered-pan-pro-mini', 129, 'v6b-mini.jpg', '8&Prime; (20 cm)'),
    'small':    ('Titanium Hammered Pan Pro Small', 'Pan Pro Small', 'titanium-hammered-pan-pro-small', 137, 'v6b-small.jpg', '10&Prime; (26 cm)'),
    'standard': ('Titanium Hammered Pan Pro Standard', 'Pan Pro Standard', 'original-siraat-100-pure-titanium-pan-with-hammered-pattern', 144, 'v6b-standard.jpg', '11&Prime; (28 cm)'),
    'large':    ('Titanium Hammered Pan Pro Large', 'Pan Pro Large', 'titanium-hammered-pan-pro-large', 149, 'v6b-large.jpg', '12&Prime; (30 cm)'),
    'set6':     ('Titanium Hammered Pan Set With Lids, 6-Pcs', '6-Piece Set', 'titanium-hammered-pan-set-with-lids-6-pcs', 299, 'v6b-set6.jpg', 'Mini, Small, Large + 3 lids'),
    'set12':    ('Titanium Hammered Cookware Set, 12-Pcs', '12-Piece Set', 'titanium-hammered-cookware-set', 649, 'v6b-set12.jpg', '3 pans, 3 pots, 6 lids'),
    'duo':      ('2 Pans + 2 Lids', '2 Pans + 2 Lids', '2-pans-and-2-lids', 199, 'v6b-duo.jpg', '2 hammered pans + 2 lids'),
    'roast':    ('Titanium Hammered Roasting Pan', 'Roasting Pan', 'titanium-hammered-roasting-pan', 199, 'v6b-roast.jpg', 'V-rack included'),
    'lid':      ('Stainless Steel Lid', 'Fitted lid', 'stainless-steel-lid', 59, 'v6b-lid.jpg', 'Mini, Small, Standard, Large'),
}
def d(n): return f'${n:,.0f}' if n == int(n) else f'${n:,.2f}'
def hi(n): return d(round(n * 0.9, 2))
SEP6 = PR['mini'][3] + PR['small'][3] + PR['large'][3] + 3 * PR['lid'][3]   # 592
SAVE6 = SEP6 - PR['set6'][3]                                                # 293

F = "font-family:Inter,Arial,Helvetica,sans-serif;"
S = "font-family:'Instrument Serif','Times New Roman',Times,serif;font-style:italic;font-weight:400;"
INK, BRICK, CREAM, SAND, GREY, GOLD, W, ESP = '#272727', '#AC3B19', '#F8F7F2', '#ECE7DD', '#5E5A54', '#B8862B', '#FFFFFF', '#321E1D'
FR = 'Free shipping. 30-day returns. 100,000+ happy customers.'
STARS = f'<span style="color:{BRICK};letter-spacing:2px;">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'

class Mail:
    def __init__(s, mid): s.mid, s.b = mid, ''
    def U(s, c, path='/collections/all'):
        return f'https://siraatskitchen.com/discount/{CODE}?redirect=' + quote(f'{path}?utm_source=klaviyo&utm_medium=email&utm_campaign={CAMP}&utm_content={s.mid}-{c}', safe='')
    def UP(s, c, k): return s.U(c, '/products/' + PR[k][2])
    def plain(s, c, url): return f'{url}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={s.mid}-{c}'
    def add(s, h): s.b += h; return s
    def row(s, inner, pad='0 40px', bg=CREAM, cls='pad', al='left'):
        return s.add(f'<tr><td align="{al}" bgcolor="{bg}" class="{cls}" style="background-color:{bg};padding:{pad};text-align:{al};">{inner}</td></tr>\n')
    def codebar(s, t):
        return s.add(f'<tr><td align="center" bgcolor="{INK}" style="background-color:{INK};padding:11px 16px;{F}font-size:11px;line-height:15px;letter-spacing:1.6px;font-weight:700;color:{CREAM};text-transform:uppercase;"><a href="{s.U("codebar")}" style="color:{CREAM};text-decoration:none;">{t}</a></td></tr>\n')
    def p(s, t, pad='12px 40px 0 40px', size=16, col='#2E2E2E', al='left', w=400):
        return s.row(f'<div class="lead" style="{F}font-size:{size}px;line-height:{round(size*1.5)}px;color:{col};font-weight:{w};">{t}</div>', pad, al=al)
    def h(s, eyebrow, title, pad='30px 40px 0 40px', al='center', size=36):
        e = f'<div style="{F}font-size:12px;line-height:16px;letter-spacing:2.2px;font-weight:700;color:{BRICK};padding-bottom:6px;">{eyebrow}</div>' if eyebrow else ''
        return s.row(f'{e}<div class="h2" style="{F}font-size:{size}px;line-height:{round(size*1.12)}px;font-weight:800;color:{INK};letter-spacing:-0.6px;">{title}</div>', pad, al=al)
    def btn(s, label, href, pad='18px 40px 0 40px', sub=FR, big=True):
        s.row(f'<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="440" style="width:100%;max-width:440px;margin:0 auto;"><tr><td align="center" bgcolor="{BRICK}" style="background-color:{BRICK};border-radius:6px;"><a href="{href}" style="display:block;padding:{"21px" if big else "16px"} 16px;{F}font-size:{"17px" if big else "15px"};line-height:20px;font-weight:800;letter-spacing:0.6px;color:{W};text-decoration:none;text-transform:uppercase;">{label} &rarr;</a></td></tr></table>', pad, al='center')
        if sub: s.row(f'<div style="{F}font-size:12px;line-height:18px;color:#727272;">{sub}</div>', '8px 40px 0 40px', al='center')
        return s
    def offertop(s, eyebrow, title, sub, label, href):
        """Boven de vouw: harde aanbodregel, code (envelopkaartje als lichte draad), grote knop, sterren + 100,000+."""
        s.h(eyebrow, title, '26px 34px 0 34px', size=38)
        s.p(sub, '10px 40px 0 40px', size=17, al='center')
        s.row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{W}" style="background-color:{W};border:2px dashed {INK};border-radius:8px;"><tr>'
              f'<td width="96" valign="middle" class="envthumb" style="width:96px;padding:10px 0 10px 10px;"><a href="{href}" style="display:block;"><img src="{urls["v6e-m2-seal.jpg"]}" width="86" height="86" alt="Your welcome envelope, sealed with the Siraat seal" style="display:block;width:86px;height:86px;border:0;border-radius:6px;"></a></td>'
              f'<td valign="middle" align="center" style="padding:12px 10px;text-align:center;"><div style="{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:700;color:{GOLD};">YOUR WELCOME CODE</div>'
              f'<div class="code" style="{F}font-size:34px;line-height:40px;letter-spacing:7px;font-weight:800;color:{INK};padding-top:2px;">{CODE}</div>'
              f'<div style="{F}font-size:13px;line-height:18px;color:#2E2E2E;"><b>10% off everything</b> + {GIFTS}</div></td></tr></table>', '18px 40px 0 40px')
        s.btn(label, href)
        s.row(f'<div style="{F}font-size:13px;line-height:18px;color:{INK};">{STARS}&nbsp; <b>100,000+ happy customers</b> &middot; 75-year warranty</div>', '10px 30px 0 30px', al='center')
        return s
    def cards2(s, keys, title=None, eyebrow=None, tags=None):
        """Productkaarten 2 per rij: beeld, naam, maat, prijs en prijs met HI10, eigen knop met code."""
        if title: s.h(eyebrow, title, '32px 40px 0 40px', size=28)
        tags = tags or {}
        def card(k):
            t, n, hd, pr, im, sz = PR[k]
            tag = f'<div style="{F}font-size:10px;line-height:13px;letter-spacing:1.4px;font-weight:800;color:{W};background-color:{INK};display:inline-block;padding:4px 7px;border-radius:3px;">{tags[k]}</div>' if k in tags else '<div style="font-size:0;line-height:21px;">&nbsp;</div>'
            return (f'<td width="50%" valign="top" class="c2" style="width:50%;padding:0 6px 12px 6px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{W}" style="background-color:{W};border:1px solid {SAND};border-radius:8px;"><tr><td align="center" bgcolor="{W}" style="background-color:{W};padding:12px 12px 14px 12px;text-align:center;">'
                    f'{tag}<a href="{s.UP("card-" + k + "-img", k)}" style="display:block;"><img src="{urls[im]}" width="220" alt="{t}" style="display:block;width:100%;max-width:220px;height:auto;border:0;margin:6px auto 0 auto;"></a>'
                    f'<div style="{F}font-size:15px;line-height:19px;font-weight:800;color:{INK};padding-top:8px;"><a href="{s.UP("card-" + k + "-name", k)}" style="color:{INK};text-decoration:none;">{n}</a></div>'
                    f'<div style="{F}font-size:12px;line-height:16px;color:#8A847A;padding-top:2px;">{sz}</div>'
                    f'<div style="{F}font-size:14px;line-height:20px;color:#5E5A54;padding-top:8px;">{d(pr)}</div>'
                    f'<div class="np" style="{F}font-size:24px;line-height:28px;font-weight:800;color:{INK};">{hi(pr)}</div><div style="{F}font-size:10px;line-height:13px;letter-spacing:1.2px;font-weight:700;color:{BRICK};">WITH HI10</div>'
                    f'<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="margin-top:10px;"><tr><td align="center" bgcolor="{INK}" style="background-color:{INK};border-radius:5px;"><a href="{s.UP("card-" + k, k)}" style="display:block;padding:11px 6px;{F}font-size:12px;line-height:15px;font-weight:800;letter-spacing:0.6px;color:{W};text-decoration:none;">GET 10% OFF &rarr;</a></td></tr></table>'
                    '</td></tr></table></td>')
        rows = ''
        for i in range(0, len(keys), 2):
            pair = keys[i:i + 2]
            rows += '<tr>' + ''.join(card(k) for k in pair) + ('<td width="50%"></td>' if len(pair) == 1 else '') + '</tr>'
        return s.row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>', '14px 34px 0 34px', cls='padx')
    def bundle6(s, title='Most people pick the 6-piece set'):
        """Bundelblok: echte losse prijzen opgeteld tegen de setprijs. Geen compare-at."""
        items = [('Pan Pro Mini 8&Prime;', PR['mini'][3]), ('Pan Pro Small 10&Prime;', PR['small'][3]), ('Pan Pro Large 12&Prime;', PR['large'][3]), ('3 fitted lids (3 &times; $59)', 3 * PR['lid'][3])]
        li = ''.join(f'<tr><td style="padding:5px 0;{F}font-size:14px;line-height:19px;color:#2E2E2E;border-bottom:1px solid {SAND};">{n}</td><td align="right" style="padding:5px 0;{F}font-size:14px;line-height:19px;color:#2E2E2E;border-bottom:1px solid {SAND};">{d(p)}</td></tr>' for n, p in items)
        li += f'<tr><td style="padding:7px 0 0 0;{F}font-size:14px;line-height:19px;color:#5E5A54;">Bought one by one</td><td align="right" style="padding:7px 0 0 0;{F}font-size:14px;line-height:19px;color:#5E5A54;">{d(SEP6)}</td></tr>'
        li += f'<tr><td style="padding:3px 0 0 0;{F}font-size:16px;line-height:21px;font-weight:800;color:{INK};">The set</td><td align="right" style="padding:3px 0 0 0;{F}font-size:16px;line-height:21px;font-weight:800;color:{INK};">{d(PR["set6"][3])}</td></tr>'
        s.row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{W}" style="background-color:{W};border:2px solid {INK};border-radius:10px;"><tr><td bgcolor="{W}" style="background-color:{W};padding:18px 18px 16px 18px;">'
              f'<div style="{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:800;color:{BRICK};">MOST POPULAR UPGRADE</div><div class="h3" style="{F}font-size:24px;line-height:28px;font-weight:800;color:{INK};padding-top:4px;">{title}</div>'
              f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:12px;"><tr><td width="38%" valign="top" class="bimg" style="width:38%;padding-right:12px;"><a href="{s.UP("bundle-img", "set6")}" style="display:block;"><img src="{urls["v6b-set6.jpg"]}" width="190" alt="Titanium Hammered Pan Set With Lids, 6 pieces" style="display:block;width:100%;max-width:190px;height:auto;border:0;border-radius:6px;"></a></td>'
              f'<td valign="top"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{li}</table></td></tr></table>'
              f'<div style="{F}font-size:17px;line-height:24px;color:{INK};padding-top:12px;text-align:center;"><b style="color:{BRICK};">You save {d(SAVE6)}.</b> With HI10: <b>{hi(PR["set6"][3])}</b>, about {d(round(PR["set6"][3] * 0.9 / 3))} a pan, lid included.</div>'
              '</td></tr></table>', '26px 40px 0 40px')
        return s.btn(f'Get the set for {hi(PR["set6"][3])}', s.UP('bundle', 'set6'), '14px 40px 0 40px', sub=None)
    def addrow(s, k, head, line, label):
        """'Add the lid' / 'complete the set': smalle rij met prijs en eigen knop."""
        t, n, hd, pr, im, sz = PR[k]
        return s.row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#F1ECE2" style="background-color:#F1ECE2;border-radius:8px;"><tr>'
                     f'<td width="84" valign="middle" style="width:84px;padding:10px 0 10px 10px;"><a href="{s.UP("add-" + k + "-img", k)}" style="display:block;"><img src="{urls[im]}" width="74" height="74" alt="{t}" style="display:block;width:74px;height:74px;border:0;border-radius:6px;"></a></td>'
                     f'<td valign="middle" style="padding:10px 12px;"><div style="{F}font-size:11px;line-height:14px;letter-spacing:1.6px;font-weight:800;color:{BRICK};">{head}</div><div style="{F}font-size:14px;line-height:19px;color:{INK};padding-top:3px;">{line} <b>{d(pr)}, {hi(pr)} with HI10.</b></div>'
                     f'<div style="padding-top:5px;"><a href="{s.UP("add-" + k, k)}" style="{F}font-size:13px;line-height:17px;font-weight:800;color:{BRICK};">{label} &rarr;</a></div></td></tr></table>', '16px 40px 0 40px')
    def sizes(s):
        """Maatkiezer met prijs en prijs met HI10 per maat, elke tegel klikbaar met code."""
        def tile(k, label, who):
            t, n, hd, pr, im, sz = PR[k]
            pop = f'<div style="{F}font-size:9px;line-height:12px;letter-spacing:1px;font-weight:800;color:{W};background-color:{BRICK};padding:3px 0;border-radius:3px 3px 0 0;">MOST PICKED</div>' if k == 'standard' else f'<div style="font-size:9px;line-height:18px;">&nbsp;</div>'
            bd = BRICK if k == 'standard' else SAND
            return (f'<td width="25%" valign="top" class="sz" style="width:25%;padding:0 4px;">{pop}<a href="{s.UP("size-" + k, k)}" style="display:block;text-decoration:none;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{W}" style="background-color:{W};border:2px solid {bd};"><tr><td align="center" bgcolor="{W}" style="background-color:{W};padding:10px 3px 12px 3px;text-align:center;">'
                    f'<img src="{urls[im]}" width="90" alt="{t}" style="display:block;width:100%;max-width:90px;height:auto;border:0;margin:0 auto;">'
                    f'<div style="{F}font-size:14px;line-height:17px;font-weight:800;color:{INK};padding-top:6px;">{label}</div><div style="{F}font-size:12px;line-height:15px;color:#8A847A;">{sz.split(" ")[0]}</div>'
                    f'<div style="{F}font-size:11px;line-height:14px;color:#5E5A54;padding-top:4px;">{who}</div>'
                    f'<div style="{F}font-size:13px;line-height:17px;color:#5E5A54;padding-top:6px;">{d(pr)}</div><div style="{F}font-size:17px;line-height:21px;font-weight:800;color:{INK};">{hi(pr)}</div>'
                    f'<div style="{F}font-size:11px;line-height:14px;font-weight:800;color:{BRICK};padding-top:6px;">PICK &rarr;</div></td></tr></table></a></td>')
        s.h('SIZE CHOOSER', 'Which size is yours?', '32px 40px 0 40px', size=28)
        return s.row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{tile("mini", "Mini", "eggs for one")}{tile("small", "Small", "sides for two")}{tile("standard", "Standard", "everyday, 2 to 4")}{tile("large", "Large", "a family")}</tr></table>'
                     f'<div style="{F}font-size:12px;line-height:17px;color:#8A847A;padding-top:8px;text-align:center;">Price with HI10 in bold. Same titanium surface on every size.</div>', '14px 30px 0 30px', cls='padx')
    def stack(s, k='standard'):
        """Value stack: pan + 5 gifts ($555 value) + garantie + retour + verzending, dan de prijs met HI10."""
        t, n, hd, pr, im, sz = PR[k]
        rows = [(f'{n} {sz.split(" ")[0]}', d(pr)), ('5 free gifts: free shipping, e-book, mystery gift, cookbook, chance to win a PFAS water filter', '$555 value'),
                ('75-year warranty against defects', 'Included'), ('30-day returns', 'Included')]
        li = ''.join(f'<tr><td valign="top" style="padding:8px 0;border-bottom:1px solid {SAND};{F}font-size:14px;line-height:19px;color:#2E2E2E;"><span style="color:{BRICK};font-weight:800;">&#10003;</span>&nbsp; {a}</td><td valign="top" align="right" style="padding:8px 0 8px 10px;border-bottom:1px solid {SAND};{F}font-size:14px;line-height:19px;font-weight:700;color:{INK};white-space:nowrap;">{b}</td></tr>' for a, b in rows)
        s.row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{W}" style="background-color:{W};border:1px solid {SAND};border-radius:10px;"><tr><td bgcolor="{W}" style="background-color:{W};padding:16px 18px;">'
              f'<div style="{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:800;color:{BRICK};">EVERYTHING YOU GET</div><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:6px;">{li}</table>'
              f'<div style="{F}font-size:20px;line-height:26px;color:{INK};padding-top:12px;text-align:center;">Your price: <b>{hi(pr)}</b> <span style="{F}font-size:14px;color:#8A847A;">with HI10</span></div></td></tr></table>', '24px 40px 0 40px')
        return s.btn(f'Get my pan for {hi(pr)}', s.UP('stack', k), '14px 40px 0 40px', sub=None)
    def reviews(s, items, title=None):
        cells = ''.join(f'<tr><td style="padding:0 0 10px 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{W}" style="background-color:{W};border:1px solid {SAND};border-radius:8px;"><tr><td bgcolor="{W}" style="background-color:{W};padding:12px 16px;">'
                        f'<div style="{F}font-size:13px;line-height:15px;">{STARS}</div><div style="{F}font-size:15px;line-height:21px;color:{INK};padding-top:5px;font-weight:600;">&ldquo;{q}&rdquo;</div><div style="{F}font-size:12px;line-height:16px;color:#8A847A;padding-top:4px;">{w} &middot; Verified buyer</div></td></tr></table></td></tr>' for q, w in items)
        if title: s.h(None, title, '28px 40px 0 40px', size=24)
        return s.row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{cells}</table>', '12px 40px 0 40px')
    def faq(s, items):
        cells = ''.join(f'<tr><td style="padding:0 0 8px 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{W}" style="background-color:{W};border-left:4px solid {BRICK};"><tr><td bgcolor="{W}" style="background-color:{W};padding:11px 14px;">'
                        f'<div style="{F}font-size:16px;line-height:21px;font-weight:800;color:{INK};">{q}</div><div style="{F}font-size:14px;line-height:20px;color:#2E2E2E;padding-top:3px;">{a}</div></td></tr></table></td></tr>' for q, a in items)
        return s.row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{cells}</table>', '14px 40px 0 40px')
    def compare(s, rows):
        def cell(t, ok, bg):
            return f'<td width="50%" valign="middle" bgcolor="{bg}" style="width:50%;background-color:{bg};padding:10px 10px;border-top:1px solid {SAND};{F}font-size:14px;line-height:18px;color:{INK};"><span style="color:{BRICK if ok else "#9A948B"};font-weight:800;">{"&#10003;" if ok else "&#10005;"}</span>&nbsp; {t}</td>'
        r = ''.join(f'<tr>{cell(a, True, W)}{cell(b, False, "#F3F0EA")}</tr>' for a, b in rows)
        head = (f'<tr><td width="50%" bgcolor="{INK}" style="width:50%;background-color:{INK};padding:10px;{F}font-size:12px;line-height:16px;letter-spacing:1.4px;font-weight:800;color:{W};">SIRAAT</td>'
                f'<td width="50%" bgcolor="#E4DED3" style="width:50%;background-color:#E4DED3;padding:10px;{F}font-size:12px;line-height:16px;letter-spacing:1.4px;font-weight:800;color:{INK};">A PFAS-COATED PAN</td></tr>')
        return s.row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid {SAND};">{head}{r}</table>', '16px 40px 0 40px')
    def img(s, key, alt, href, w=600, pad='0', cls='pad'):
        return s.row(f'<a href="{href}" style="display:block;"><img src="{urls[key]}" width="{w}" alt="{alt}" style="display:block;width:100%;max-width:{w}px;height:auto;border:0;margin:0 auto;"></a>', pad, al='center', cls=cls)
    def sign(s, ps=None):
        s.p('<b>Benjamin</b><br><span style="color:#8A847A;font-size:14px;">Founder, Siraat</span>', '20px 40px 0 40px')
        if ps: s.p(ps, '12px 40px 0 40px', size=14, col=GREY)
        return s.add(f'<tr><td bgcolor="{CREAM}" style="background-color:{CREAM};padding:0 0 28px 0;font-size:0;line-height:0;">&nbsp;</td></tr>\n')

# ---------- vaste header en footer
hdr = open(os.path.join(P, 'header.html')).read(); ftr = open(os.path.join(P, 'footer.html')).read()
for k, v in urls.items():
    hdr = hdr.replace('{{SHARED}}/' + k, v); ftr = ftr.replace('{{SHARED}}/' + k, v).replace('{{IMG}}/' + k, v)
hdr = re.sub(r'<!--.*?-->\n?', '', hdr, flags=re.S); ftr = re.sub(r'<!--.*?-->\n?', '', ftr, flags=re.S)
assert '{{SHARED}}' not in hdr + ftr and '{{IMG}}' not in hdr + ftr
def utm_nav(h, tag, mid):
    return re.sub(r'href="(https://(?:www\.)?siraatskitchen\.com[^"?]*)"', lambda m: f'href="{m.group(1)}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={mid}-{tag}-{(m.group(1).rstrip("/").split("/")[-1] or "home").replace(".com", "home")}"', h)

HEAD = open(os.path.join(ROOT, '../v6-envelope/e1.html')).read().split('<body')[0]
HEAD = HEAD.replace('.cimg{width:36%!important;}', '.cimg{width:36%!important;} .c2{padding:0 4px 10px 4px!important;} .np{font-size:21px!important;} .sz{padding:0 2px!important;} .code{font-size:28px!important;letter-spacing:5px!important;} .envthumb{width:72px!important;} .envthumb img{width:64px!important;height:64px!important;} .bimg{width:34%!important;} .h3{font-size:21px!important;line-height:25px!important;}')
HEAD = HEAD.replace('.h2{font-size:32px!important;line-height:36px!important;}', '.h2{font-size:28px!important;line-height:32px!important;}')

def page(m, title, preview):
    head = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', HEAD)
    body = m.b.replace('{{HEADER}}', utm_nav(hdr, 'nav', m.mid)).replace('{{FOOTER}}', utm_nav(ftr, 'ft', m.mid))
    html = (head + '<body style="margin:0;padding:0;background:#FFFFFF;">\n'
            f'<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;">{preview}' + '&#847;&zwnj;&nbsp;' * 60 + '</div>\n'
            '<table bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;" width="100%">\n<tr><td align="center" style="padding:8px 0 32px 0;">\n'
            f'<table bgcolor="{CREAM}" border="0" cellpadding="0" cellspacing="0" class="w" role="presentation" style="width:100%;max-width:600px;background-color:{CREAM};" width="600">\n'
            + body + '</table>\n</td></tr>\n</table>\n</body>\n</html>\n')
    assert '—' not in html, m.mid
    assert '{{SHARED}}' not in html and '{{IMG}}' not in html and '{{HEADER}}' not in html
    open(os.path.join(ROOT, m.mid + '.html'), 'w').write(html)
    prev = html.replace("{{ first_name|default:'there' }}", 'Sarah').replace('{{ organization.name }}', "Siraat's Kitchen").replace('{{ organization.full_address }}', '(address)')
    prev = re.sub(r'\{%.*?%\}', '#', prev); prev = re.sub(r'\{\{.*?\}\}', '', prev)
    open(os.path.join(ROOT, m.mid + '-preview.html'), 'w').write(prev)
    print(m.mid, 'ok', len(html), 'bytes')

HI = "Hi {{ first_name|default:'there' }},"
R = {  # letterlijk uit content/reviews/reviews.csv (Trustpilot, 5 sterren), alleen ingekort met '...'
    'tammy': ('I am on my 4th pan from Siraat... I even gifted one to my son, and he says it&rsquo;s the best pan he owns.', 'Tammy, Pan Pro'),
    'sunny': ('I ordered one pan to try it out. I&rsquo;m so glad I did. I am so happy with this pan that I&rsquo;m ordering the set.', 'Sunny C.'),
    'michael': ('The real test was my egg the next morning... the egg released completely and slid around the pan like it was non-stick.', 'Michael G., Pan Pro'),
    'fatima': ('...I thought it was just marketing hype... I ended up buying the whole collection.', 'Fatima, Set'),
    'carole': ('I&rsquo;ve been cooking for well over 60 years... This Siraat pan has been the absolute best I&rsquo;ve ever used.', 'Carole, Pan Pro'),
    'thomas': ('This pan is fantastic. Makes all of our others &ldquo;non stick&rdquo; seem really sticky.', 'Thomas D., Pan Pro'),
    'brandon': ('Siraat replaced a pan free of charge... I just sent them the picture and they honored the warranty.', 'Brandon W., Pan Pro'),
    'graham': ('We cooked the best omelette we have ever eaten when we used the pan for the first time.', 'Graham C., Pan Pro'),
}
OBJ = [('Will food stick?', 'Not when the pan is hot. <b>Medium heat for 2 to 3 minutes</b>, a teaspoon of oil, and eggs slide. Skip the heat, and it sticks.'),
       ('Does it work on induction?', '<b>Yes.</b> Induction, gas, electric and ceramic. Oven safe, dishwasher safe, metal utensils welcome.'),
       ('What if I don&rsquo;t like it?', '<b>30-day returns.</b> Send it back unused within 30 days of delivery for a full refund.')]

# ================================================================ E1 · offer + bestsellers + bundel (5 min)
e = Mail('e1')
e.codebar(f'Welcome &middot; 10% off with HI10 &middot; {GIFTS}').add('{{HEADER}}\n')
e.offertop('YOUR WELCOME ENVELOPE IS OPEN', 'Take 10% off your first pan.', f'<b>Code HI10 works on everything</b>, sets included. Plus {GIFTS}.', 'Claim my 10% + gifts', e.U('cta1'))
e.p(f'Already something in your cart? <a href="{e.U("cart", "/cart")}" style="color:{BRICK};font-weight:800;">Apply my 10% to my cart &rarr;</a>', '10px 40px 0 40px', size=14, al='center')
e.cards2(['standard', 'set6', 'duo', 'roast'], 'Our bestsellers, with your 10%', 'START HERE', tags={'standard': 'BESTSELLER', 'set6': 'BEST VALUE'})
e.bundle6()
e.addrow('lid', 'ADD THE LID', 'Fits your pan, keeps the heat in.', 'Add a lid')
e.reviews([R['tammy'], R['sunny']], '100,000+ happy customers')
e.btn('Claim my 10% + gifts', e.U('cta2'), '18px 40px 0 40px')
e.p('<b>Pure titanium cooking surface. No coatings.</b> Tested for 31 PFAS compounds by Light Labs, every one below the detection limit. ' + f'<a href="{e.plain("report", REPORT)}" style="color:{BRICK};">Report no. 25895 &rarr;</a>', '18px 40px 0 40px', size=14, col=GREY, al='center')
e.sign()
e.add('{{FOOTER}}\n')
page(e, 'Your 10% is inside', f'HI10 takes 10% off everything, sets included. Plus {GIFTS}.')

# ================================================================ E2 · verhaal kort, eindigt in kaarten + maatkiezer (+1 d 10:00)
e = Mail('e2')
e.codebar(f'10% off with HI10 &middot; {GIFTS}').add('{{HEADER}}\n')
e.offertop('THE PAN NOBODY ELSE WAS MAKING', 'The original hammered titanium pan.', '<b>First orders shipped December 20, 2024.</b> Look-alikes came after. Yours is 10% off.', 'Get 10% off the original', e.UP('cta1', 'standard'))
e.img('v6e-m2-path.jpg', 'A line of gold sand leading to the Siraat seal', e.UP('story-img', 'standard'), pad='26px 0 0 0', cls='')
e.p('<b>Siraat is named after sirat, the Arabic word for path.</b> The path to a non-toxic life, one step at a time.', '18px 40px 0 40px')
e.p('We started with titanium cutting boards. Then we made the pan: <b>a pure titanium cooking surface, no coatings</b>. Nothing on it to wear off. That is why it is covered for 75 years.', '10px 40px 0 40px')
e.p('<b>Your first step is one pan.</b> Pick your size:', '10px 40px 0 40px')
e.sizes()
e.btn('Get 10% off my size', e.UP('cta2', 'standard'), '18px 40px 0 40px')
e.stack('standard')
e.addrow('lid', 'ADD THE LID', 'The fitted lid for your size.', 'Add a lid')
e.reviews([R['carole'], R['graham']])
e.sign('P.S. HI10 has no end date. One use, 10% off everything.')
e.add('{{FOOTER}}\n')
page(e, 'The pan nobody else was making', 'First orders shipped December 20, 2024. Pick your size, 10% off with HI10.')

# ================================================================ E3 · bewijs + tabel + bundel (+2 d 09:00)
e = Mail('e3')
e.codebar(f'10% off with HI10 &middot; {GIFTS}').add('{{HEADER}}\n')
e.offertop('REPORT NO. 25895', 'Tested for 31 PFAS. All below detection.', '<b>Every pan says non-toxic. We show the paper.</b> And your 10% is still here.', 'Get 10% off the tested pan', e.UP('cta1', 'standard'))
e.row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
      + ''.join(f'<td width="33%" valign="top" align="center" style="width:33%;padding:0 4px;text-align:center;"><div class="big3" style="{F}font-size:34px;line-height:38px;font-weight:800;color:{BRICK};">{a}</div><div style="{F}font-size:12px;line-height:16px;color:#2E2E2E;padding-top:4px;">{b}</div></td>'
                for a, b in [('31', 'PFAS compounds tested'), ('0', 'detected above the limit'), ('75', 'year warranty')]) + '</tr></table>', '28px 30px 0 30px', cls='padx')
e.p(f'Light Labs, an <b>ISO/IEC 17025-accredited lab</b>, tested our cooking surface. <a href="{e.plain("report", REPORT)}" style="color:{BRICK};font-weight:700;">Read report no. 25895 &rarr;</a>', '14px 40px 0 40px', size=15, al='center')
e.h('SIDE BY SIDE', 'Siraat vs a PFAS-coated pan', '30px 40px 0 40px', size=26)
e.compare([('Pure titanium surface', 'A coating on top'), ('No coating to wear off', 'Coating wears with use'), ('Metal utensils welcome', 'Wood or silicone advised'), ('Dishwasher safe', 'Hand wash advised'), ('Lab report no. 25895', 'Testing varies by brand')])
e.reviews([R['michael'], R['thomas']])
e.cards2(['standard', 'large'], 'Start with one tested pan', None, tags={'standard': 'BESTSELLER'})
e.bundle6('Or the whole stove: 3 pans + 3 lids')
e.sign('P.S. Same titanium cooking surface on every pan in the set.')
e.add('{{FOOTER}}\n')
page(e, 'Report no. 25895', '31 PFAS compounds tested, every one below detection. Your 10% is still here.')

# ================================================================ E4 · still sealed + top 3 + bezwaren (+3 d 09:00)
e = Mail('e4')
e.codebar(f'Still unused &middot; 10% off with HI10 &middot; {GIFTS}').add('{{HEADER}}\n')
e.offertop('YOUR ENVELOPE IS STILL SEALED', 'Your 10% hasn&rsquo;t been used yet.', f'<b>HI10 takes 10% off everything.</b> {GIFTS[0].upper() + GIFTS[1:]}. Pick yours below.', 'Use my 10% now', e.U('cta1'))
e.cards2(['standard', 'set6'], 'Where most people start', 'MOST PICKED', tags={'standard': '#1 BESTSELLER', 'set6': 'BEST VALUE'})
e.cards2(['set12', 'large'], tags={'set12': 'WHOLE KITCHEN'})
e.p('12-piece set: 3 pans, 2-qt and 3-qt saucepans, an 8-qt stockpot, and a lid for each. US only.', '0 40px 0 40px', size=12, col='#8A847A', al='center')
e.h('QUICK ANSWERS', 'Before you open it', '28px 40px 0 40px', size=26)
e.faq(OBJ)
e.addrow('set6', 'COMPLETE THE SET', f'Three pans and three lids instead of one pan. {d(SAVE6)} less than one by one:', 'Upgrade to the 6-piece set')
e.reviews([R['fatima'], R['brandon']])
e.btn('Use my 10% now', e.U('cta2'), '16px 40px 0 40px')
e.sign()
e.add('{{FOOTER}}\n')
page(e, 'Still sealed', f'Your 10% is unused. Where most people start, with your price, plus {GIFTS}.')

# ================================================================ E5 · korte brief Benjamin + harde recap (+4 d 09:00)
e = Mail('e5')
e.add('{{HEADER}}\n')
e.p(HI, '30px 40px 0 40px')
e.p('Last note from me about your welcome code.', '12px 40px 0 40px')
e.p(f'<b>HI10 takes 10% off everything</b>, and {GIFTS}. It has no end date, so no pressure. But if you were waiting for a sign, this is it.', '12px 40px 0 40px')
e.p('<b>Two promises.</b> Changed your mind? Unused within 30 days of delivery, full refund. Something wrong? Damaged or defective in the first 30 days, we refund or replace it and pay the shipping. After that, the 75-year warranty.', '12px 40px 0 40px')
e.p('Not sure which pan? Reply and tell me what you cook most. Our team will help.', '12px 40px 0 40px')
e.sign()
# harde recap
rec = ''.join(f'<tr><td width="70" valign="middle" style="width:70px;padding:8px 0;border-top:1px solid {SAND};"><a href="{e.UP("recap-" + k + "-img", k)}" style="display:block;"><img src="{urls[PR[k][4]]}" width="60" height="60" alt="{PR[k][0]}" style="display:block;width:60px;height:60px;border:0;border-radius:6px;"></a></td>'
              f'<td valign="middle" style="padding:8px 8px;border-top:1px solid {SAND};{F}font-size:14px;line-height:18px;color:{INK};"><b>{PR[k][1]}</b><br><span style="color:#8A847A;">{d(PR[k][3])}</span> &rarr; <b>{hi(PR[k][3])}</b></td>'
              f'<td valign="middle" align="right" style="padding:8px 0;border-top:1px solid {SAND};"><a href="{e.UP("recap-" + k, k)}" style="display:inline-block;background-color:{INK};color:{W};{F}font-size:12px;line-height:15px;font-weight:800;padding:10px 12px;border-radius:5px;text-decoration:none;">GET 10% OFF</a></td></tr>' for k in ['standard', 'set6', 'set12'])
e.row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{W}" style="background-color:{W};border:2px solid {INK};border-radius:10px;"><tr><td bgcolor="{W}" style="background-color:{W};padding:18px 18px 8px 18px;">'
      f'<div style="{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:800;color:{BRICK};text-align:center;">YOUR OFFER, IN ONE PLACE</div>'
      f'<div style="{F}font-size:30px;line-height:36px;font-weight:800;color:{INK};text-align:center;padding-top:4px;">10% off with <span style="border:2px dashed {INK};padding:0 8px;letter-spacing:4px;">HI10</span></div>'
      f'<div style="{F}font-size:14px;line-height:20px;color:#2E2E2E;text-align:center;padding:8px 0 10px 0;">+ {GIFTS} &middot; 75-year warranty &middot; 30-day returns</div>'
      f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rec}</table></td></tr></table>', '6px 40px 0 40px')
e.btn('Claim my 10% + gifts', e.U('cta'), '16px 40px 0 40px')
e.add(f'<tr><td bgcolor="{CREAM}" style="background-color:{CREAM};padding:0 0 28px 0;font-size:0;line-height:0;">&nbsp;</td></tr>\n')
e.add('{{FOOTER}}\n')
page(e, 'Last note about your 10%', 'No end date, no pressure. Two promises, and your 10% in one place.')
