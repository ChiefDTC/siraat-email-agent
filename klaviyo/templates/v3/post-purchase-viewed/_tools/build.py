"""PP set upsell VIP15 (19 nov 2026, draft; v2 na wijziging Floris: alleen sets, AOV omhoog). Vier mails: 12-Pcs mail 1 en 2 (herinnering), 6-Pcs mail 1 en 2.
Bouwt ppv-<id>.html (Klaviyo, Django-tags), ppv-<id>-preview.html (US-voorbeeld) en ppv-<id>-preview-int.html (niet-US, alleen 6-Pcs).
Gebruik: python3 -I _tools/build.py   (vanuit de map post-purchase-viewed)
Codes (Shopify, 19 nov, status SCHEDULED met start 2027-01-01, dus NIET actief): VIP15-SET12 2371721789780, VIP15-SET6 2371721822548.
15%, alleen dat product, 1x per klant, combineert met productkortingen (FREE GIFT) en verzending.
Bij livegang in Shopify: start = nu, eind = 2026-12-01T04:59Z (ma 30 nov 23:59 ET). Dat is de einddatum die de mails noemen."""
import re, os
from urllib.parse import quote
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../..'))
P = os.path.join(REPO, 'klaviyo/templates/partials')
urls = dict(l.split() for l in open(os.path.join(P, 'shared/klaviyo-urls.txt')) if len(l.split()) == 2)
urls.update(dict(l.split() for l in open(os.path.join(ROOT, 'assets/klaviyo-urls.txt')) if len(l.split()) == 2))
tg = open(os.path.join(REPO, 'klaviyo/templates/v3/campaigns/thanksgiving-roast-1117/tg-us.html')).read()
f13 = open(os.path.join(REPO, 'klaviyo/templates/v3/campaigns/friday13-1113/f13-us.html')).read()
reviews = {l.split(',')[0]: l for l in open(os.path.join(REPO, 'content/reviews/reviews.csv'))}

F = "font-family:Inter,Arial,Helvetica,sans-serif;"
S = "font-family:'Instrument Serif','Times New Roman',Times,serif;font-style:italic;font-weight:400;"
INK, BRICK, ESP, CREAM, SAND, GREY = '#272727', '#AC3B19', '#321E1D', '#F8F7F2', '#ECE7DD', '#5E5A54'
US = "{% if event.extra.shipping_address.country_code == 'US' %}"
ELSE, END = '{% else %}', '{% endif %}'
END_LINE = 'Monday, Nov 30 at 11:59&nbsp;PM&nbsp;ET'
FR_US = 'One use, already applied. 30-day returns. 100,000+ happy customers.'
FR_INT = 'One use, already applied. Duties paid. 30-day returns.'

# Wat ze kochten, kort genoemd (Placed Order Items, volgorde wisselt; gifts staan er ook in). Eerste treffer wint.
BOUGHT = [('Titanium Hammered Pan Pro Standard', 'Pan Pro'), ('Titanium Hammered Pan Pro Large', 'Pan Pro'), ('Titanium Hammered Pan Pro Small', 'Pan Pro'),
          ('Titanium Hammered Pan Pro Mini', 'Pan Pro'), ('Titanium Hammered Pan Set With Lids | 6-Pcs', '6-piece set'),
          ('Titanium Hammered Deep Pan Pro', 'Deep Pan'), ('Titanium Hammered Wok Pan Pro', 'wok'), ('Titanium Hammered Crêpe Pan Pro', 'crêpe pan'),
          ('Titanium Hammered Pro Duo', 'Pro Duo'), ('2 Pans + 2 Lids', 'pans'), ('Titanium Hammered Roasting Pan', 'roasting pan'),
          ('Titanium Cutting Board', 'cutting board')]
def bought(skip):
    out = ''
    for i, (t, n) in enumerate(B for B in BOUGHT if B[0] != skip):
        out += ('{%% if %s in event.Items %%}' if i == 0 else '{%% elif %s in event.Items %%}') % ("'" + t.replace("'", "\\'") + "'") + 'Your ' + n + ' is'
    return out + '{% else %}Your order is{% endif %}'

def p(t, pad="14px 40px 0 40px", size=17, col="#2E2E2E", al="left", w=400):
    return f'<tr><td align="{al}" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:{pad};text-align:{al};"><div style="{F}font-size:{size}px;line-height:{round(size*1.55)}px;color:{col};font-weight:{w};">{t}</div></td></tr>\n'

def quote_ok(rid, ex):
    orig = reviews[rid].split(',', 4)[4]
    pos = 0
    for part in [x.strip() for x in ex.split('...') if x.strip()]:
        j = orig.find(part, pos); assert j >= 0, (rid, part); pos = j + len(part)
    assert len(ex) <= 120 and ',5,' in reviews[rid], (rid, len(ex))
    return ex

SET12_BODY = ["Whatever is on its way to you now, the 12&#8209;piece set is the rest of the kitchen around it: three pans, a 2 qt and a 3 qt saucepan and an 8 qt stockpot, each with its lid. It is the only way to get our titanium hammered pots.",
         "Every piece has the same pure titanium cooking surface, no coatings. Nothing on it to wear off, so every piece is covered by the 75-year warranty.",
         "<b>VIP15-SET12 takes $97.35 off the set.</b> It is a thank-you for your order: one use, the 12&#8209;piece set only, and it ends " + END_LINE + ", when our Black Friday sale ends. After that the code stops working."]
SET6_BODY = ["Three pans and three lids mean the eggs, the sauce and the vegetables can all go at once, each with a lid that fits.",
         "Same pure titanium cooking surface as the rest of our cookware, no coatings. Nothing on it to wear off, so every piece is covered by the 75-year warranty.",
         "<b>VIP15-SET6 takes 15% off the set.</b> It is a thank-you for your order: one use, the 6&#8209;piece set only, and it ends " + END_LINE + ", when our Black Friday sale ends. After that the code stops working."]
B12 = dict(code='VIP15-SET12', handle='titanium-hammered-cookware-set', title='Titanium Hammered Cookware Set | 12-Pcs', short='12-piece set', us_only=True,
   img='ppv-set12.jpg', alt='The Siraat 12-piece set: three pans, two saucepans and an 8 qt stockpot, each with its lid',
   was='$2,047', now='$649', code_price='$551.65', name='Titanium Hammered Cookware Set', spec='12 pieces &middot; 3 pans, 3 pots, 6 lids &middot; US only', btn='Get 15% off the set')
B6 = dict(code='VIP15-SET6', handle='titanium-hammered-pan-set-with-lids-6-pcs', title='Titanium Hammered Pan Set With Lids | 6-Pcs', short='6-piece set', us_only=False,
   img='ppv-set6.jpg', alt='The Siraat 6-piece set: three titanium hammered pans and three lids',
   was='$997', now='$299', code_price='$254.15', name='Titanium Hammered Pan Set With Lids', spec='6 pieces &middot; 3 pans, 3 lids', btn='Get 15% off the set')
REV = ('R025', 'Sunny C.', "I ordered one pan to try it out. I'm so glad I did. I am so happy with this pan that I'm ordering the set.")
M = {
 'set12-m1': dict(B12, reminder=False, eyebrow='A THANK&#8209;YOU FOR YOUR ORDER',
   subject="Here's the rest of the kitchen", preview='Your order is on its way. 15% off the 12-piece set, once, until Nov 30.',
   h="Here&rsquo;s the rest of the kitchen.", intro="on its way. Here&rsquo;s the rest of the kitchen, 15% off, once.", body=SET12_BODY, rev=REV),
 'set12-m2': dict(B12, reminder=True, eyebrow='ENDS MONDAY, NOV 30',
   subject='Your VIP15 code ends Monday, Nov 30', preview='15% off the 12-piece set, one use. At 11:59 PM ET it stops working.',
   h='Your VIP15 code ends Monday night.', intro=None,
   body=["A short note, so it does not slip by. Your code VIP15-SET12 takes $97.35 off the 12&#8209;piece set: three pans, two saucepans and an 8 qt stockpot, each with its lid.",
         "It works once and ends " + END_LINE + ". After that it stops working. If the set is not for you, no need to do anything."], rev=None),
 'set6-m1': dict(B6, reminder=False, eyebrow='A THANK&#8209;YOU FOR YOUR ORDER',
   subject='Three pans, three lids, 15% off', preview='Your order is on its way. 15% off the 6-piece set, once, until Nov 30.',
   h='Three pans, three lids. 15% off, once.', intro="on its way. Here is the full pan set to go with it, 15% off, once.", body=SET6_BODY, rev=REV),
 'set6-m2': dict(B6, reminder=True, eyebrow='ENDS MONDAY, NOV 30',
   subject='Your VIP15 code ends Monday, Nov 30', preview='15% off the 6-piece set, one use. At 11:59 PM ET it stops working.',
   h='Your VIP15 code ends Monday night.', intro=None,
   body=["A short note, so it does not slip by. Your code VIP15-SET6 takes 15% off the 6&#8209;piece set: three pans and three lids.",
         "It works once and ends " + END_LINE + ". After that it stops working. If the set is not for you, no need to do anything."], rev=None),
}

head = tg[:tg.index('<body')]
_i = head.rindex('</style>'); head = head[:_i] + '@media only screen and (max-width: 480px) { .pr { font-size:21px !important; line-height:25px !important; } .h1x { font-size:34px !important; line-height:38px !important; } }\n' + head[_i:]
hdr0 = open(os.path.join(P, 'header.html')).read()
ftr0 = open(os.path.join(P, 'footer.html')).read()
for k, v in urls.items():
    hdr0 = hdr0.replace('{{SHARED}}/' + k, v)
    ftr0 = ftr0.replace('{{SHARED}}/' + k, v).replace('{{IMG}}/' + k, v)
hdr0 = re.sub(r'<!--.*?-->\n?', '', hdr0, flags=re.S); ftr0 = re.sub(r'<!--.*?-->\n?', '', ftr0, flags=re.S)
gsrc = dict(re.findall(r'alt="([^"]+)" src="([^"]+)"', f13))
CAMP = 'pp-viewed-upsell'

def build(key, m):
    U = lambda c: 'https://siraatskitchen.com/discount/' + m['code'] + '?redirect=' + quote(f'/products/{m["handle"]}?utm_source=klaviyo&utm_medium=email&utm_campaign={CAMP}&utm_content={key}-{c}', safe='')
    def utm_nav(h, tag):
        return re.sub(r'href="(https://(?:www\.)?siraatskitchen\.com[^"?]*)"', lambda x: f'href="{x.group(1)}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={key}-{tag}-{(x.group(1).rstrip("/").split("/")[-1] or "home").replace(".com","home")}"', h)
    hdr, ftr = utm_nav(hdr0, 'nav'), utm_nav(ftr0, 'ft')
    usx = (lambda a, b: a) if m['us_only'] else (lambda a, b: US + a + ELSE + b + END)
    FRX = FR_US if m['us_only'] else US + FR_US + ELSE + FR_INT + END
    def btn(c, pad="22px 40px 0 40px"):
        return (f'<tr><td align="center" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:{pad};"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="400" style="width:100%;max-width:400px;margin:0 auto;"><tr><td align="center" bgcolor="{INK}" style="background-color:{INK};border-radius:30px;"><a href="{U(c)}" style="display:block;padding:20px 18px;{F}font-size:15px;line-height:18px;font-weight:600;letter-spacing:1.2px;color:#FFFFFF;text-decoration:none;text-transform:uppercase;">{m["btn"]}</a></td></tr></table></td></tr>\n'
                f'<tr><td align="center" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:10px 40px 0 40px;text-align:center;"><div style="{F}font-size:12px;line-height:18px;color:#727272;">{FRX}</div></td></tr>\n')
    b = f'<tr><td align="center" bgcolor="{INK}" style="background-color:{INK};padding:11px 20px;{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:600;color:{CREAM};text-transform:uppercase;"><a href="{U("topbar")}" style="color:{CREAM};text-decoration:none;">YOUR 15% OFF THE {m["short"].upper().replace("-", "&#8209;")} &middot; <span style="white-space:nowrap;">CODE {m["code"]}</span></a></td></tr>\n'
    b += hdr + '\n'
    b += (f'<tr><td align="center" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:34px 40px 0 40px;text-align:center;"><div style="{F}font-size:12px;line-height:16px;letter-spacing:2px;font-weight:600;color:{BRICK};">{m["eyebrow"]}</div>'
          f'<div class="h1x" style="{S}font-size:42px;line-height:46px;color:{INK};padding-top:10px;">{m["h"]}</div></td></tr>\n')
    if m['intro']: b += p(bought(m['title']) + ' ' + m['intro'], "14px 40px 0 40px", al="center")
    b += f'<tr><td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:22px 0 0 0;"><a href="{U("img")}" style="display:block;border:0;text-decoration:none;"><img src="{urls[m["img"]]}" width="600" alt="{m["alt"]}" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>\n'
    # prijsblok (espresso), prijzen alleen US; INT zonder bedrag
    was = f'<span style="text-decoration:line-through;">{m["was"]}</span>&nbsp;&nbsp;' if m['was'] else ''
    price_us = (f'<div style="{F}font-size:15px;line-height:22px;color:#D9C6BC;">{was}{m["now"]}</div>'
                f'<div class="now" style="{F}font-size:40px;line-height:46px;font-weight:800;color:#FFFFFF;padding-top:2px;">{m["code_price"]}</div>'
                f'<div style="{F}font-size:13px;line-height:19px;color:#D9C6BC;padding-top:4px;">with your code</div>')
    price_int = f'<div class="now" style="{F}font-size:40px;line-height:46px;font-weight:800;color:#FFFFFF;">15% OFF</div><div style="{F}font-size:13px;line-height:19px;color:#D9C6BC;padding-top:4px;">the {m["short"]}, with your code</div>'
    b += (f'<tr><td align="center" bgcolor="{ESP}" class="pad" style="background-color:{ESP};padding:22px 40px 20px 40px;text-align:center;">'
          f'<div style="{F}font-size:16px;line-height:22px;font-weight:600;color:#FFFFFF;">{m["name"]}</div><div style="{F}font-size:12px;line-height:18px;color:#D9C6BC;padding-bottom:12px;">{m["spec"]}</div>'
          + usx(price_us, price_int) +
          f'<div style="padding-top:14px;"><span style="display:inline-block;border:1px dashed #D9C6BC;border-radius:6px;padding:8px 16px;{F}font-size:18px;line-height:22px;font-weight:800;letter-spacing:2px;color:#FFFFFF;white-space:nowrap;">{m["code"]}</span></div>'
          f'<div style="{F}font-size:12px;line-height:18px;color:#D9C6BC;padding-top:8px;">Applied through the button. Ends {END_LINE}.</div></td></tr>\n')
    b += btn('cta1')
    b += p("Hi {{ first_name|default:'there' }}, Benjamin here.", "32px 40px 0 40px")
    for t in m['body']:
        b += p(t)
    if m['rev']:
      rid, rn, rq = m['rev']; quote_ok(rid, rq)
      b += (f'<tr><td bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:26px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{CREAM}" style="background-color:{CREAM};border:1px solid {SAND};border-radius:10px;"><tr><td align="center" bgcolor="{CREAM}" style="background-color:{CREAM};padding:20px 24px;text-align:center;">'
          f'<div style="{F}font-size:15px;line-height:18px;letter-spacing:3px;color:{BRICK};">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
          f'<div style="{S}font-size:22px;line-height:29px;color:{INK};padding-top:8px;">&ldquo;{rq}&rdquo;</div>'
          f'<div style="{F}font-size:12px;line-height:17px;color:#8A847A;padding-top:8px;">{rn} &middot; Verified buyer</div></td></tr></table></td></tr>\n')
    if not m['reminder']: b += btn('cta2', "24px 40px 0 40px")
    # 5 gifts, compact
    G = [('Free shipping', 'Included'), ('Plastic-Free Home e book', 'Included'), ('Mystery gift', 'Included'), ('Favorites Cookbook', 'Included'), ('Chance to win a PFAS water filter', 'Weekly draw')]
    def gt(n, v):
        lab = {'Plastic-Free Home e book': 'Plastic-free e-book', 'Chance to win a PFAS water filter': 'Chance to win a PFAS water filter'}.get(n, n)
        return (f'<td width="20%" valign="top" align="center" class="gm" style="padding:8px 3px 12px 3px;"><a href="{U("gifts")}" style="display:block;text-decoration:none;"><img src="{gsrc[n]}" width="64" height="64" alt="{lab}" style="display:block;width:64px;height:64px;border:0;border-radius:6px;margin:0 auto;object-fit:cover;"></a>'
                f'<div style="{F}font-size:11px;line-height:14px;font-weight:600;color:{INK};padding-top:8px;text-align:center;">{lab}</div><div style="{F}font-size:10px;line-height:13px;color:#8A847A;padding-top:2px;text-align:center;">{v}</div></td>')
    gv = ' ($555&nbsp;value)' if m['us_only'] else US + ' ($555&nbsp;value)' + END
    if not m['reminder']: b += (f'<tr><td align="center" bgcolor="#FFFFFF" class="padx" style="background-color:#FFFFFF;padding:30px 24px 0 24px;"><div class="h1s" style="{S}font-size:26px;line-height:30px;color:{INK};text-align:center;padding-bottom:10px;">5 free gifts with every order, this one too{gv}</div>'
          f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{CREAM}" style="background-color:{CREAM};border-radius:8px;"><tr>' + ''.join(gt(*x) for x in G) + '</tr></table></td></tr>\n')
    def prom(t, s):
        return f'<td width="50%" valign="top" align="center" style="width:50%;padding:16px 6px;text-align:center;"><div class="pr" style="{S}font-size:26px;line-height:30px;color:{INK};">{t}</div><div style="{F}font-size:12px;line-height:17px;color:#8A847A;padding-top:4px;">{s}</div></td>'
    b += (f'<tr><td bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:22px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {SAND};border-bottom:1px solid {SAND};"><tr>'
          + prom('75-year warranty', 'Covered against defects.') + prom('30-day returns', 'Unused, within 30 days of delivery.') + '</tr></table></td></tr>\n')
    b += p("Thank you for cooking with us,", "22px 40px 4px 40px")
    b += f'<tr><td align="left" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:4px 40px 14px 40px;text-align:left;"><div style="{F}font-size:17px;line-height:24px;color:{INK};font-weight:600;">Benjamin</div><div style="{F}font-size:14px;line-height:20px;color:#8A847A;">Founder, Siraat</div></td></tr>\n'
    b += p(f"P.S. {m['code']} works once, on the {m['short']} only, until {END_LINE}. Reply and our team will help with anything about your order.", "4px 40px 26px 40px", size=15, col=GREY)
    b += ftr
    h0 = re.sub(r'<title>[^<]*</title>', f'<title>{m["subject"]}</title>', head)
    html = (h0 + '<body style="margin:0;padding:0;background:#FFFFFF;">\n'
            f'<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;">{m["preview"]}' + '&#847;&zwnj;&nbsp;' * 60 + '</div>\n'
            '<table bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;" width="100%">\n<tr><td align="center" style="padding:8px 0 32px 0;">\n'
            '<table bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" class="w" role="presentation" style="width:100%;max-width:600px;background:#FFFFFF;" width="600">\n'
            + b + '</table>\n</td></tr>\n</table>\n</body>\n</html>\n')
    assert '—' not in html and '{{SHARED}}' not in html and '{{IMG}}' not in html
    open(os.path.join(ROOT, f'ppv-{key}.html'), 'w').write(html)
    def prev(h, us):
        h = h.replace("{{ first_name|default:'there' }}", 'Floris').replace('{{ organization.name }}', "Siraat's Kitchen").replace('{{ organization.full_address }}', '(address)')
        # if-ketens oplossen: kies voor de preview Pan Pro (kocht Standard) en het gekozen land
        h = h.replace(bought(m['title']), 'Your Pan Pro is')
        h = re.sub(re.escape(US) + r'(.*?)' + re.escape(ELSE) + r'(.*?)' + re.escape(END), lambda x: x.group(1) if us else x.group(2), h, flags=re.S)
        h = re.sub(r'\{%.*?%\}', '#', h); h = re.sub(r'\{\{.*?\}\}', '', h)
        return h
    open(os.path.join(ROOT, f'ppv-{key}-preview.html'), 'w').write(prev(html, True))
    if not m['us_only']:
        open(os.path.join(ROOT, f'ppv-{key}-preview-int.html'), 'w').write(prev(html, False))
    print(key, len(html), 'bytes; em dash', html.count('—'))

for k, m in M.items():
    build(k, m)
