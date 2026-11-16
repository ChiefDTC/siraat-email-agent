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
head = re.sub(r'<title>[^<]*</title>', '<title>Your turkey timeline</title>', head)
PREVIEW = 'Fridge dates for a 12 to 24 lb bird, two fixes that matter, and the pan with the rack built in.'
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

b = ''
b += f'<tr><td align="center" bgcolor="{INK}" style="background-color:{INK};padding:11px 20px;{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:800;color:{CREAM};text-transform:uppercase;"><a href="https://siraatskitchen.com/collections/black-friday-sale?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content=topbar" style="color:{CREAM};text-decoration:none;">VIP BLACK FRIDAY SALE IS LIVE</a></td></tr>\n'
b += hdr + '\n'
b += img(urls['tg-hero-turkey-43.jpg'], 'A roast turkey on the V-rack in the Siraat Titanium Hammered Roasting Pan on a Thanksgiving table', 'hero')
b += (f'<tr><td align="center" bgcolor="{ESP}" class="pad" style="background-color:{ESP};padding:38px 36px 36px 36px;text-align:center;">'
      f'<div style="{F}font-size:12px;line-height:16px;letter-spacing:3px;font-weight:700;color:#E2B8A4;">THE TURKEY TIMELINE</div>'
      f'<div class="h1b" style="{S}font-size:44px;line-height:48px;color:#FFFFFF;padding-top:12px;">Thaw it on time.<br>Lift it. Pull it at 165&deg;F.</div>'
      f'<div style="{F}font-size:16px;line-height:24px;color:#EADBD3;padding-top:14px;">The three things that decide the bird.</div></td></tr>\n')
b += p("Hi {{ first_name|default:'there' }}, Benjamin here.", "32px 40px 0 40px")
b += p("Most turkey trouble starts days before Thursday. The bird is still frozen on Wednesday night, or it sits in its own juices and the bottom steams, or it gets cooked by the clock instead of by the thermometer.")
b += p("So here is the short version. Save it, screenshot it, stick it on the fridge.")
b += eyebrow('STEP 1 &middot; THE FRIDGE', 'When your bird goes in')
b += p("Thawing in the fridge takes about a day for every 4 to 5 pounds (that is the USDA rule). Counting back from Thursday, November 26:", "10px 40px 0 40px", size=16)
b += cal
b += p("Bought it fresh? Skip this step. Running late? The USDA also allows a cold-water thaw, about 30 minutes per pound, changing the water every 30 minutes.", "8px 40px 0 40px", size=14, col=GREY)
b += eyebrow('STEP 2 &middot; THE OVEN', 'Two fixes that matter most')
b += fix('1', 'Lift it off the pan floor.', "A bird that sits flat in the pan cooks in its own juices, so the underside steams and stays pale. Set it on a rack: hot air reaches the bottom and the skin browns all the way round. The drippings collect underneath for the gravy.")
b += fix('2', 'Cook to 165&deg;F, not to the clock.', "Check the thickest part of the breast and the innermost part of the thigh, without touching bone. Every spot needs to read 165&deg;F. Then let it rest at least 20 minutes before you carve, so the juices settle back into the meat instead of onto the board.")
b += eyebrow('STEP 3 &middot; THE PAN', 'Built around the rack', "38px 40px 14px 40px")
b += img(urls['tg-pan-rack.jpg'], 'Siraat Titanium Hammered Roasting Pan with the fitted V-rack', 'pan-img', w=520, pad="0 40px", radius=8)
b += (f'<tr><td align="left" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:18px 40px 0 40px;"><div style="{F}font-size:20px;line-height:26px;font-weight:700;color:{INK};"><a href="{U("pan-name")}" style="color:{INK};text-decoration:none;">Titanium Hammered Roasting Pan</a></div>'
      f'<div style="{F}font-size:14px;line-height:20px;color:#8A847A;padding-top:4px;">With fitted V-rack &middot; 14 x 10.6 in</div>'
      f'<div style="padding-top:10px;"><span class="now" style="{F}font-size:34px;line-height:38px;font-weight:800;color:{INK};">$199</span><span style="{F}font-size:13px;line-height:18px;letter-spacing:1.4px;font-weight:700;color:{BRICK};padding-left:10px;">BLACK FRIDAY PRICE</span></div></td></tr>\n')
b += (f'<tr><td bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:16px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">'
      + why('<b>The rack is in the box.</b> A fitted V-rack that lifts the bird, so step 2 is already handled.')
      + why('<b>A pure titanium cooking surface, no coatings.</b> No PFAS, PFOA, or BPA. The same titanium surface as our Pan Pro, which Light Labs tested free from PFAS (report no. 25895).')
      + why('<b>From oven to stovetop.</b> Fully clad with an induction base, so the gravy gets whisked right in the pan, on gas, electric or induction.')
      + why('<b>Covered for 75 years.</b> Dishwasher safe, metal utensil safe, nothing on it to wear off.')
      + '</table></td></tr>\n')
b += btn('Get my roasting pan', 'cta1')
b += eyebrow('A STRAIGHT ANSWER', 'Will it arrive by Thursday?', "40px 40px 4px 40px")
b += p("I can't promise that, so I won't. With Thanksgiving next week, a pan ordered today may or may not make it to your table in time.", "10px 40px 0 40px")
b += p("Everything above works in the pan you already own. This one is for the roasts after it: Christmas dinner, the Sunday chicken, next year's bird. And it is covered for 75 years against defects.")
b += (f'<tr><td bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:28px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{CREAM}" style="background-color:{CREAM};border-left:3px solid {BRICK};"><tr><td bgcolor="{CREAM}" style="background-color:{CREAM};padding:18px 20px;">'
      f'<div style="{F}font-size:13px;line-height:16px;letter-spacing:2px;color:{BRICK};">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
      f'<div style="{S}font-size:22px;line-height:28px;color:{INK};padding-top:8px;">&ldquo;Siraat replaced a pan free of charge... I just sent them the picture and they honored the warranty.&rdquo;</div>'
      f'<div style="{F}font-size:13px;line-height:18px;color:#8A847A;padding-top:8px;">Brandon W. &middot; Verified buyer</div></td></tr></table></td></tr>\n')
b += btn('Get my roasting pan', 'cta2', "28px 40px 0 40px")
b += gifts
b += p("Happy roasting,", "28px 40px 4px 40px")
b += f'<tr><td align="left" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:4px 40px 18px 40px;text-align:left;"><div style="{F}font-size:17px;line-height:24px;color:{INK};font-weight:700;">Benjamin</div><div style="{F}font-size:14px;line-height:20px;color:#8A847A;">Founder, Siraat</div></td></tr>\n'
b += p("P.S. Write your fridge date on the turkey bag tonight. It is the one step you cannot catch up on later.", "4px 40px 32px 40px", size=15, col=GREY)
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
