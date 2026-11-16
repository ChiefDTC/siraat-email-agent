"""Thanksgiving Roast 17 nov 2026 (US). Bouwt tg-us.html (Klaviyo) en tg-us-preview.html (Django-tags vervangen).
Gebruik: python3 -I _tools/build.py   (vanuit de campagnemap)"""
import re, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../../..'))
P = os.path.join(REPO, 'klaviyo/templates/partials')
urls = dict(l.split() for l in open(os.path.join(P, 'shared/klaviyo-urls.txt')) if len(l.split()) == 2)
urls.update(dict(l.split() for l in open(os.path.join(ROOT, 'assets/klaviyo-urls.txt')) if len(l.split()) == 2))
f13 = open(os.path.join(REPO, 'klaviyo/templates/v3/campaigns/friday13-1113/f13-us.html')).read()

CAMP = 'thanksgiving-roast-1117-us'
PDP = 'https://siraatskitchen.com/products/titanium-hammered-roasting-pan'
def U(c): return f'{PDP}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={c}'
F = "font-family:Inter,Arial,Helvetica,sans-serif;"
S = "font-family:'Instrument Serif','Times New Roman',Times,serif;font-style:italic;font-weight:400;"
INK, BRICK, ESP, CREAM, SAND, GREY = '#272727', '#AC3B19', '#321E1D', '#F8F7F2', '#ECE7DD', '#5E5A54'

def p(t, pad="14px 40px 0 40px", size=17, col="#2E2E2E", al="left", w=400):
    return f'<tr><td align="{al}" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:{pad};text-align:{al};"><div style="{F}font-size:{size}px;line-height:{round(size*1.55)}px;color:{col};font-weight:{w};">{t}</div></td></tr>\n'
def eyebrow(label, title, pad="38px 40px 6px 40px"):
    return f'<tr><td align="left" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:{pad};"><div style="{F}font-size:12px;line-height:16px;letter-spacing:2.4px;font-weight:700;color:{BRICK};">{label}</div><div class="h2" style="{S}font-size:34px;line-height:38px;color:{INK};padding-top:8px;">{title}</div></td></tr>\n'
def btn(label, c, pad="26px 40px 0 40px"):
    return (f'<tr><td align="center" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:{pad};"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="400" style="width:100%;max-width:400px;margin:0 auto;"><tr><td align="center" bgcolor="{INK}" style="background-color:{INK};border-radius:30px;"><a href="{U(c)}" style="display:block;padding:20px 18px;{F}font-size:15px;line-height:18px;font-weight:700;letter-spacing:1.2px;color:#FFFFFF;text-decoration:none;text-transform:uppercase;">{label}</a></td></tr></table></td></tr>\n'
            f'<tr><td align="center" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:10px 40px 0 40px;text-align:center;"><div style="{F}font-size:12px;line-height:18px;color:#727272;">Free shipping. 30-day returns. 100,000+ happy customers.</div></td></tr>\n')
def img(src, alt, c, w=600, pad="0", radius=0):
    return f'<tr><td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:{pad};"><a href="{U(c)}" style="display:block;border:0;text-decoration:none;"><img src="{src}" width="{w}" alt="{alt}" style="display:block;width:100%;max-width:{w}px;height:auto;border:0;border-radius:{radius}px;"></a></td></tr>\n'

# ---------- thaw calendar (USDA: fridge, about 24 h per 4 to 5 lb; upper bound counted back from Thursday 26 Nov)
THAW = [('12 lb', '3 days', 'Mon, Nov 23'), ('16 lb', '4 days', 'Sun, Nov 22'), ('20 lb', '5 days', 'Sat, Nov 21'), ('24 lb', '6 days', 'Fri, Nov 20')]
def tile(w, d, date):
    return (f'<td width="50%" valign="top" style="padding:0 5px 10px 5px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{CREAM}" style="background-color:{CREAM};border:1px solid {SAND};border-radius:8px;"><tr><td align="center" bgcolor="{CREAM}" style="background-color:{CREAM};padding:16px 8px 16px 8px;text-align:center;">'
            f'<div style="{S}font-size:34px;line-height:38px;color:{INK};">{w}</div>'
            f'<div style="{F}font-size:12px;line-height:17px;color:#8A847A;padding-top:2px;">about {d} in the fridge</div>'
            f'<div style="{F}font-size:11px;line-height:16px;letter-spacing:1.6px;font-weight:700;color:{BRICK};padding-top:10px;">FRIDGE BY</div>'
            f'<div style="{F}font-size:17px;line-height:22px;font-weight:700;color:{INK};padding-top:2px;">{date}</div></td></tr></table></td>')
cal = (f'<tr><td bgcolor="#FFFFFF" class="padx" style="background-color:#FFFFFF;padding:16px 35px 0 35px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">'
       f'<tr>{tile(*THAW[0])}{tile(*THAW[1])}</tr><tr>{tile(*THAW[2])}{tile(*THAW[3])}</tr></table></td></tr>\n')

def fix(n, title, body):
    return (f'<tr><td bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:16px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {SAND};"><tr>'
            f'<td width="52" valign="top" style="width:52px;padding:18px 0 0 0;"><div style="{S}font-size:44px;line-height:44px;color:{BRICK};">{n}</div></td>'
            f'<td valign="top" style="padding:18px 0 0 0;"><div style="{F}font-size:18px;line-height:24px;font-weight:700;color:{INK};">{title}</div><div style="{F}font-size:16px;line-height:25px;color:#2E2E2E;padding-top:6px;">{body}</div></td></tr></table></td></tr>\n')

def why(t):
    return f'<tr><td valign="top" width="24" style="width:24px;padding:0 0 10px 0;"><img src="{urls["icon-check.png"]}" width="16" alt="" style="display:block;width:16px;height:auto;margin-top:4px;"></td><td valign="top" style="padding:0 0 10px 6px;{F}font-size:16px;line-height:24px;color:#2E2E2E;">{t}</td></tr>'

# ---------- page
head = f13[:f13.index('<body')]
head = re.sub(r'<title>[^<]*</title>', '<title>Your Thanksgiving roast, sorted</title>', head)
PREVIEW = 'Order by Friday, Nov 20. V-rack included, $199, plus 5 free gifts.'
hdr = open(os.path.join(P, 'header.html')).read().replace('{{SHARED}}/', '')
ftr = open(os.path.join(P, 'footer.html')).read()
for k, v in urls.items():
    hdr = hdr.replace(k, v) if k.startswith('logo') else hdr
    ftr = ftr.replace('{{SHARED}}/' + k, v).replace('{{IMG}}/' + k, v)
hdr = re.sub(r'<!--.*?-->\n?', '', hdr, flags=re.S); ftr = re.sub(r'<!--.*?-->\n?', '', ftr, flags=re.S)
def utm_nav(h, tag):  # UTM op header/footer-links (zoals build_template.py doet)
    return re.sub(r'href="(https://(?:www\.)?siraatskitchen\.com[^"?]*)"', lambda m: f'href="{m.group(1)}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={tag}-{(m.group(1).rstrip("/").split("/")[-1] or "home").replace(".com","home")}"', h)
hdr, ftr = utm_nav(hdr, 'nav'), utm_nav(ftr, 'ft')

# gifts: vast 5-gifts-blok uit F13 (zelfde opmaak), links naar de PDP
g0 = f13.index('5 free gifts with every order'); g0 = f13.rfind('<tr>', 0, g0)
g1 = f13.index('Happy Lucky Friday'); g1 = f13.rfind('<tr>', 0, g1)
G = [('gift-shipping.jpg','Free shipping','Included'),('gift-ebook.jpg','Plastic-free e-book','Included'),('gift-mystery.jpg','Mystery gift','Included'),('cookbook','Favorites Cookbook','Included'),('gift-filter.jpg','Chance to win a PFAS water filter','Weekly draw')]
gsrc = dict(re.findall(r'alt="([^"]+)" src="([^"]+)"', f13[g0:g1]))
def gt(k, n, v):
    src = gsrc.get({'Plastic-free e-book':'Plastic-Free Home e book'}.get(n,n)) or urls[k]
    return (f'<td width="20%" valign="top" align="center" class="gm" style="padding:8px 3px 12px 3px;"><a href="{U("gifts")}" style="display:block;text-decoration:none;"><img src="{src}" width="64" height="64" alt="{n}" style="display:block;width:64px;height:64px;border:0;border-radius:6px;margin:0 auto;object-fit:cover;"></a>'
            f'<div style="{F}font-size:11px;line-height:14px;font-weight:600;color:{INK};padding-top:8px;text-align:center;">{n}</div><div style="{F}font-size:10px;line-height:13px;color:#8A847A;padding-top:2px;text-align:center;">{v}</div></td>')
gifts = (f'<tr><td align="center" bgcolor="#FFFFFF" class="padx" style="background-color:#FFFFFF;padding:34px 24px 0 24px;"><div class="h1s" style="{S}font-size:28px;line-height:32px;color:{INK};text-align:center;padding-bottom:10px;">5 free gifts with every order ($555&nbsp;value)</div>'
         f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{CREAM}" style="background-color:{CREAM};border-radius:8px;"><tr>' + ''.join(gt(*x) for x in G) + '</tr></table></td></tr>\n')

# ---------- v2 (Floris 16 nov): levering voor Thanksgiving is de kern, veel meer beeld
def tile4(w, d, day, date):
    return (f'<td width="25%" valign="top" style="width:25%;padding:0 3px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{CREAM}" style="background-color:{CREAM};border:1px solid {SAND};border-radius:8px;"><tr><td align="center" bgcolor="{CREAM}" style="background-color:{CREAM};padding:14px 2px 14px 2px;text-align:center;">'
            f'<div class="tw" style="{S}font-size:30px;line-height:32px;color:{INK};">{w}</div>'
            f'<div style="{F}font-size:11px;line-height:15px;color:#8A847A;padding-top:3px;">{d}</div>'
            f'<div style="{F}font-size:9px;line-height:12px;letter-spacing:1.4px;font-weight:700;color:{BRICK};padding-top:9px;">IN THE FRIDGE</div>'
            f'<div style="{F}font-size:14px;line-height:18px;font-weight:700;color:{INK};padding-top:3px;">{day}<br>{date}</div></td></tr></table></td>')
T4 = [('12 lb', '3 days', 'Mon', 'Nov 23'), ('16 lb', '4 days', 'Sun', 'Nov 22'), ('20 lb', '5 days', 'Sat', 'Nov 21'), ('24 lb', '6 days', 'Fri', 'Nov 20')]
cal4 = (f'<tr><td bgcolor="#FFFFFF" class="padx" style="background-color:#FFFFFF;padding:18px 33px 0 33px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
        + ''.join(tile4(*t) for t in T4) + '</tr></table></td></tr>\n')
def benefit(src, alt, title, body, c):
    return (f'<tr><td bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:16px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td width="120" valign="top" style="width:120px;"><a href="{U(c)}" style="display:block;text-decoration:none;"><img src="{src}" width="120" height="120" alt="{alt}" style="display:block;width:120px;height:120px;border:0;border-radius:8px;"></a></td>'
            f'<td valign="middle" style="padding:0 0 0 16px;"><div style="{F}font-size:17px;line-height:22px;font-weight:700;color:{INK};">{title}</div><div style="{F}font-size:14px;line-height:21px;color:#4A4640;padding-top:5px;">{body}</div></td></tr></table></td></tr>\n')
def darkbtn(label, c, sub):
    return (f'<tr><td align="center" bgcolor="{ESP}" class="pad" style="background-color:{ESP};padding:6px 40px 0 40px;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="400" style="width:100%;max-width:400px;margin:0 auto;"><tr><td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border-radius:30px;"><a href="{U(c)}" style="display:block;padding:20px 18px;{F}font-size:15px;line-height:18px;font-weight:700;letter-spacing:1.2px;color:{INK};text-decoration:none;text-transform:uppercase;">{label}</a></td></tr></table></td></tr>\n'
            f'<tr><td align="center" bgcolor="{ESP}" class="pad" style="background-color:{ESP};padding:12px 40px 34px 40px;text-align:center;"><div style="{F}font-size:12px;line-height:18px;color:#D9C6BC;">{sub}</div></td></tr>\n')
FR = 'Free shipping. 30-day returns. 100,000+ happy customers.'

b = ''
b += f'<tr><td align="center" bgcolor="{INK}" style="background-color:{INK};padding:11px 20px;{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:800;color:{CREAM};text-transform:uppercase;"><a href="https://siraatskitchen.com/collections/black-friday-sale?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content=topbar" style="color:{CREAM};text-decoration:none;">VIP BLACK FRIDAY SALE IS LIVE</a></td></tr>\n'
b += hdr + '\n'
b += img(urls['tg2-hero.jpg'], 'Order by Fri, Nov 20. Your Thanksgiving roast, sorted. Order now, it arrives before Thanksgiving. A golden turkey on the V-rack in the Siraat Titanium Hammered Roasting Pan.', 'hero')
b += darkbtn('Get my roasting pan', 'cta1', FR)
b += p("Hi {{ first_name|default:'there' }}, Benjamin here.", "32px 40px 0 40px")
b += p("Order this week and the pan is on your counter before Thursday, V&#8209;rack in the box. Here is the rest of the plan.")
b += eyebrow('THE TURKEY TIMELINE', 'When your bird goes in the fridge', "36px 40px 4px 40px")
b += p("About one day for every 4 to 5 lb (USDA), counted back from Thursday, Nov&nbsp;26.", "8px 40px 0 40px", size=15, col=GREY)
b += cal4
b += p("Then roast it on the rack and pull it when the breast and thigh read 165&deg;F. Rest 20 minutes before you carve.", "14px 40px 0 40px", size=15, col=GREY)
b += eyebrow('WHY THIS PAN', 'Built around the rack', "38px 40px 2px 40px")
b += benefit(urls['tg2-rack.jpg'], 'The fitted V-rack in the Siraat roasting pan', 'The V&#8209;rack is in the box.', 'It lifts the bird off the pan floor, so the underside browns instead of steaming in its juices.', 'why-rack')
b += benefit(urls['tg2-gravy.jpg'], 'Whisking gravy in the roasting pan on an induction cooktop', 'Make the gravy right in it.', 'Fully clad with an induction base. From the oven straight to gas, electric or induction.', 'why-gravy')
b += benefit(urls['tg2-carve.jpg'], 'Carving a turkey in the Siraat roasting pan', 'Nothing on it to wear off.', 'A pure titanium cooking surface, no coatings. No PFAS, PFOA, or BPA. Dishwasher safe.', 'why-surface')
# product card, 2 kolommen
b += (f'<tr><td bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:30px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{CREAM}" style="background-color:{CREAM};border:1px solid {SAND};border-radius:10px;"><tr>'
      f'<td width="50%" valign="middle" style="width:50%;padding:12px 0 12px 12px;"><a href="{U("card-img")}" style="display:block;text-decoration:none;"><img src="{urls["tg2-pan.jpg"]}" width="248" alt="Siraat Titanium Hammered Roasting Pan with V-rack" style="display:block;width:100%;max-width:248px;height:auto;border:0;border-radius:6px;"></a></td>'
      f'<td valign="middle" style="padding:12px 14px 12px 14px;"><div style="{F}font-size:16px;line-height:21px;font-weight:700;color:{INK};"><a href="{U("card-name")}" style="color:{INK};text-decoration:none;">Titanium Hammered Roasting Pan</a></div>'
      f'<div style="{F}font-size:12px;line-height:17px;color:#8A847A;padding-top:4px;">V&#8209;rack included &middot; 14 x 10.6 in</div>'
      f'<div class="now" style="{F}font-size:32px;line-height:36px;font-weight:800;color:{INK};padding-top:10px;">$199</div>'
      f'<div style="{F}font-size:10px;line-height:14px;letter-spacing:1.4px;font-weight:700;color:{BRICK};padding-top:2px;">BLACK FRIDAY PRICE</div></td></tr></table></td></tr>\n')
b += btn('Get my roasting pan', 'cta2', "20px 40px 0 40px")
b += p("<b>Order by Friday, Nov 20</b> and it arrives before Thanksgiving.", "10px 40px 0 40px", size=14, col=INK, al="center")
b += img(urls['tg2-life.jpg'], 'Friends laughing while carving a turkey in the Siraat roasting pan at a Thanksgiving table', 'lifestyle', pad="32px 0 0 0")
b += gifts
# twee beloftes
def prom(t, s):
    return f'<td width="50%" valign="top" align="center" style="width:50%;padding:16px 8px;text-align:center;"><div style="{S}font-size:26px;line-height:30px;color:{INK};">{t}</div><div style="{F}font-size:12px;line-height:17px;color:#8A847A;padding-top:4px;">{s}</div></td>'
b += (f'<tr><td bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:26px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {SAND};border-bottom:1px solid {SAND};"><tr>'
      + prom('75-year warranty', 'Covered against defects.') + prom('30-day returns', 'Unused, within 30 days of delivery.') + '</tr></table></td></tr>\n')
b += p("Happy roasting,", "26px 40px 4px 40px")
b += f'<tr><td align="left" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:4px 40px 14px 40px;text-align:left;"><div style="{F}font-size:17px;line-height:24px;color:{INK};font-weight:700;">Benjamin</div><div style="{F}font-size:14px;line-height:20px;color:#8A847A;">Founder, Siraat</div></td></tr>\n'
b += p("P.S. Order by Friday, Nov 20. The pan beats the bird to the table.", "4px 40px 32px 40px", size=15, col=GREY)
b += ftr

html = (head + '<body style="margin:0;padding:0;background:#FFFFFF;">\n'
        f'<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;">{PREVIEW}' + '&#847;&zwnj;&nbsp;' * 60 + '</div>\n'
        '<table bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;" width="100%">\n<tr><td align="center" style="padding:8px 0 32px 0;">\n'
        '<table bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" class="w" role="presentation" style="width:100%;max-width:600px;background:#FFFFFF;" width="600">\n'
        + b + '</table>\n</td></tr>\n</table>\n</body>\n</html>\n')
assert '—' not in html and '{{SHARED}}' not in html and '{{IMG}}' not in html
open(os.path.join(ROOT, 'tg-us.html'), 'w').write(html)
prev = html.replace("{{ first_name|default:'there' }}", 'Floris').replace('{{ organization.name }}', "Siraat's Kitchen").replace('{{ organization.full_address }}', '(address)')
prev = re.sub(r'\{%.*?%\}', '#', prev); prev = re.sub(r'\{\{.*?\}\}', '', prev)
open(os.path.join(ROOT, 'tg-us-preview.html'), 'w').write(prev)
print('ok', len(html), 'bytes; em dash', html.count('—'))
