"""PP viewed tailored · VIP (19 nov 2026, DRAFT). Eén mail, tailored op Viewed Product.
Bouwt ../ppv-tailored.html (Klaviyo code-template met Django-tags).
  python3 -I _tools/build_tailored.py          (vanuit de map post-purchase-viewed)

Logica in de mail (zie SCENARIOS.md):
  - Land = verzendland van de order (event.extra.shipping_address.country_code); onbekend telt als niet-VS.
  - Hero: VS = 12-Pcs set, niet-VS = 6-Pcs set; weg als de klant die set (of een bundel die hem bevat) al heeft.
  - Daaronder max 5 kaarten (Floris 20 nov, was 3) uit ppv_vr_<key> (profieleigenschap, gezet door de tracker-flows):
    1 = bekeken laatste ~3 dagen, 2 = 3 tot 10 dagen, 3 = 10 tot 30 dagen, 9 = in bezit. Volgorde: emmer 1, 2, 3,
    binnen een emmer de prioriteit uit ppv_catalog.P. Alleen-VS-producten nooit buiten de VS; 6-Pcs buiten de VS alleen als hero.
  - Vangnet: kaart en hero vallen ook weg als het product (of een bundel ermee) in deze order (event.Items) of in siraat_owned staat.
Code: VIP15-PICKS (Shopify, 15%, alleen de aanbiedbare producten, 1x per klant, combineert met productkortingen en verzending),
status SCHEDULED (start 2027-01-01), dus niet actief. Bij livegang: start = nu, eind 2026-12-01T04:59Z (ma 30 nov 23:59 ET)."""
import re, os, sys
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(__file__))
from ppv_catalog import P, SET12, OWN_MATCH, SO, BYKEY
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../..'))
PART = os.path.join(REPO, 'klaviyo/templates/partials')
urls = dict(l.split() for l in open(os.path.join(PART, 'shared/klaviyo-urls.txt')) if len(l.split()) == 2)
urls.update(dict(l.split() for l in open(os.path.join(ROOT, 'assets/klaviyo-urls.txt')) if len(l.split()) == 2))
tg = open(os.path.join(REPO, 'klaviyo/templates/v3/campaigns/thanksgiving-roast-1117/tg-us.html')).read()
f13 = open(os.path.join(REPO, 'klaviyo/templates/v3/campaigns/friday13-1113/f13-us.html')).read()
reviews = {l.split(',')[0]: l for l in open(os.path.join(REPO, 'content/reviews/reviews.csv'))}

CODE = 'VIP15-PICKS'
CAMP = 'pp-viewed-tailored'
END_LINE = 'Monday, Nov 30 at 11:59&nbsp;PM&nbsp;ET'
F = "font-family:Inter,Arial,Helvetica,sans-serif;"
S = "font-family:'Instrument Serif','Times New Roman',Times,serif;font-style:italic;font-weight:400;"
INK, BRICK, ESP, CREAM, SAND, GREY = '#272727', '#AC3B19', '#321E1D', '#F8F7F2', '#ECE7DD', '#5E5A54'
FR_US = 'One use, already applied. 30-day returns. 100,000+ happy customers.'
FR_INT = 'One use, already applied. Duties paid. 30-day returns.'
IS_US = '{% if io == 0 %}'
def money(x): return ('$%s' % format(x, ',.2f')).replace('.00', '') if float(x).is_integer() else '$%s' % format(x, ',.2f')
def cp(x): return '$%s' % format(round(x * 0.85 + 1e-9, 2), ',.2f')

def U(handle, content):
    return ('https://siraatskitchen.com/discount/' + CODE + '?redirect=' +
            quote(f'/products/{handle}?utm_source=klaviyo&utm_medium=email&utm_campaign={CAMP}&utm_content={content}', safe=''))

def owned_frags(key):
    return [frag for frag, keys in OWN_MATCH if key in keys]
def so_keys(key):
    return [s for s, ks in SO.items() if key in ks]
def owned_cond(key, extra=()):
    """Django-voorwaarde 'in bezit' (vangnet naast ppv_vr == 9). items = event.Items als '|'-string, so = '|siraat_owned|'."""
    c = [f"'{f}' in items" for f in owned_frags(key)] + [f"'|{s}|' in so" for s in so_keys(key)]
    c += [f"person|lookup:'ppv_vr_{k}' == 9" for k in (key,) + tuple(extra)]
    return ' or '.join(c)

def p(t, pad="14px 40px 0 40px", size=17, col="#2E2E2E", al="left", w=400):
    return f'<tr><td align="{al}" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:{pad};text-align:{al};"><div style="{F}font-size:{size}px;line-height:{round(size*1.55)}px;color:{col};font-weight:{w};">{t}</div></td></tr>\n'

def btn(label, url, pad="20px 40px 0 40px", fr=True):
    out = (f'<tr><td align="center" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:{pad};"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="400" style="width:100%;max-width:400px;margin:0 auto;"><tr><td align="center" bgcolor="{INK}" style="background-color:{INK};border-radius:30px;"><a href="{url}" style="display:block;padding:19px 18px;{F}font-size:15px;line-height:18px;font-weight:600;letter-spacing:1.2px;color:#FFFFFF;text-decoration:none;text-transform:uppercase;">{label}</a></td></tr></table></td></tr>\n')
    if fr:
        out += f'<tr><td align="center" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:10px 40px 0 40px;text-align:center;"><div style="{F}font-size:12px;line-height:18px;color:#727272;">{IS_US}{FR_US}{{% else %}}{FR_INT}{{% endif %}}</div></td></tr>\n'
    return out

def hero(kind):
    """kind 'set12' (VS) of 'set6' (niet-VS)."""
    if kind == 'set12':
        h, im, name, spec, alt = SET12['handle'], urls['ppv-set12-hard.jpg'], SET12['name'], '12 pieces &middot; 3 pans, 3 pots, 6 lids', 'The Siraat 12-piece set: three pans, two saucepans and an 8 qt stockpot, each with its lid'
        price = (f'<div style="{F}font-size:15px;line-height:22px;color:#D9C6BC;"><span style="text-decoration:line-through;">{money(SET12["was"])}</span>&nbsp;&nbsp;{money(SET12["price"])}</div>'
                 f'<div style="{F}font-size:40px;line-height:46px;font-weight:800;color:#FFFFFF;padding-top:2px;">{cp(SET12["price"])}</div>'
                 f'<div style="{F}font-size:13px;line-height:19px;color:#D9C6BC;padding-top:4px;">with your code</div>')
        lab = 'Get 15% off the set'
        body = "Three pans, a 2&nbsp;qt and a 3&nbsp;qt saucepan and an 8&nbsp;qt stockpot, each with its lid. It is the only way to get our titanium hammered pots."
    else:
        s6 = BYKEY['s06']
        h, im, name, spec, alt = s6['handle'], urls['ppv-set6-hard.jpg'], s6['name'], '6 pieces &middot; 3 pans, 3 lids', 'The Siraat 6-piece set: three titanium hammered pans and three lids'
        price = (f'<div style="{F}font-size:40px;line-height:46px;font-weight:800;color:#FFFFFF;">15% OFF</div>'
                 f'<div style="{F}font-size:13px;line-height:19px;color:#D9C6BC;padding-top:4px;">the 6&#8209;piece set, with your code</div>')
        lab = 'Get 15% off the set'
        body = "Mini 8&Prime;, Small 10&Prime; and Large 12&Prime;, each with a fitted lid. The eggs, the sauce and the vegetables can all go at once."
    k = 'set12' if kind == 'set12' else 'set6'
    out = f'<tr><td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:22px 0 0 0;"><a href="{U(h, k + "-img")}" style="display:block;border:0;text-decoration:none;"><img src="{im}" width="600" alt="{alt}" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>\n'
    out += (f'<tr><td align="center" bgcolor="{ESP}" class="pad" style="background-color:{ESP};padding:22px 40px 20px 40px;text-align:center;">'
            f'<div style="{F}font-size:16px;line-height:22px;font-weight:600;color:#FFFFFF;">{name}</div><div style="{F}font-size:12px;line-height:18px;color:#D9C6BC;padding-bottom:12px;">{spec}</div>'
            + price + '</td></tr>\n')
    out += p(body, "18px 40px 0 40px", size=16, al="center")
    out += btn(lab, U(h, k + '-cta'))
    return out

def card(prod):
    k, h = prod['key'], prod['handle']
    url = U(h, k)
    pre = 'from ' if prod['frm'] else ''
    was = f'<span style="text-decoration:line-through;color:#8A847A;">{money(prod["was"])}</span>&nbsp; ' if prod.get('was') else ''
    pr_us = (f'<div style="{F}font-size:14px;line-height:20px;color:#5E5A54;padding-top:8px;">{was}{pre}{money(prod["price"])}</div>'
             f'<div style="{F}font-size:20px;line-height:26px;font-weight:800;color:{INK};">{pre}{cp(prod["price"])} <span style="{F}font-size:13px;font-weight:400;color:#5E5A54;">with your code</span></div>')
    pr_int = f'<div style="{F}font-size:20px;line-height:26px;font-weight:800;color:{INK};padding-top:8px;">15% off <span style="{F}font-size:13px;font-weight:400;color:#5E5A54;">with your code</span></div>'
    prices = pr_us if prod['us'] else IS_US + pr_us + '{% else %}' + pr_int + '{% endif %}'
    return (f'<tr><td bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:14px 40px 0 40px;">'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{CREAM}" style="background-color:{CREAM};border:1px solid {SAND};border-radius:10px;"><tr>'
            f'<td width="150" valign="middle" class="cimg" style="width:150px;padding:14px 0 14px 14px;"><a href="{url}" style="display:block;border:0;"><img src="{prod["img"]}" width="136" alt="{re.sub("&[a-z]+;", "", prod["name"])}" style="display:block;width:136px;height:136px;object-fit:cover;border:0;border-radius:8px;"></a></td>'
            f'<td valign="middle" style="padding:14px 16px 14px 16px;">'
            f'<div style="{F}font-size:15px;line-height:20px;font-weight:600;color:{INK};"><a href="{url}" style="color:{INK};text-decoration:none;">{prod["name"]}</a></div>'
            f'<div style="{F}font-size:13px;line-height:19px;color:#5E5A54;padding-top:4px;">{prod["line"]}</div>'
            + prices +
            f'<div style="padding-top:10px;"><a href="{url}" style="display:inline-block;background-color:{INK};border-radius:20px;padding:10px 16px;{F}font-size:12px;line-height:14px;font-weight:600;letter-spacing:1.2px;color:#FFFFFF;text-decoration:none;text-transform:uppercase;">Get 15% off</a></div>'
            '</td></tr></table></td></tr>\n')

def quote_ok(rid, ex):
    orig = reviews[rid].split(',', 4)[4]
    pos = 0
    for part in [x.strip() for x in ex.split('...') if x.strip()]:
        j = orig.find(part, pos); assert j >= 0, (rid, part); pos = j + len(part)
    assert len(ex) <= 120 and ',5,' in reviews[rid]
    return ex

# ---------- de keten: s = tokens van bekeken, niet-bezeten producten, emmer 1 dan 2 dan 3, binnen emmer op prioriteit
CARD_P = [x for x in P]
xs, names = [], []
for b in (1, 2, 3):
    for prod in CARD_P:
        n = f"x{b}{prod['key']}"
        off = '|add:off' if prod['us'] else ''
        xs.append(f"{n}=person|lookup:'ppv_vr_{prod['key']}'|default:0|add:-{b}{off}|yesno:\",{prod['t']}\"")
        names.append(n)
CHAIN = '{% with ' + ' '.join(xs) + ' %}{% with s=' + '|add:'.join(names) + ' %}'
CHAIN_END = '{% endwith %}{% endwith %}'

def _neg(cond): return ' and '.join('not ' + c for c in cond.split(' or '))
HERO_OK = ('io == 0 and ' + _neg(owned_cond('s12', extra=('e34',))) + ' or io != 0 and ' + _neg(owned_cond('s06', extra=('s12', 'e34', 'fhp'))))

def build():
    head = tg[:tg.index('<body')]
    i = head.rindex('</style>')
    head = head[:i] + ('@media only screen and (max-width: 480px) { .h1x { font-size:34px !important; line-height:38px !important; } '
                       '.cimg { width:112px !important; } .cimg img { width:100px !important; height:100px !important; } }\n') + head[i:]
    hdr = open(os.path.join(PART, 'header.html')).read(); ftr = open(os.path.join(PART, 'footer.html')).read()
    for k, v in urls.items():
        hdr = hdr.replace('{{SHARED}}/' + k, v); ftr = ftr.replace('{{SHARED}}/' + k, v).replace('{{IMG}}/' + k, v)
    hdr = re.sub(r'<!--.*?-->\n?', '', hdr, flags=re.S); ftr = re.sub(r'<!--.*?-->\n?', '', ftr, flags=re.S)
    def utm_nav(h, tag):
        return re.sub(r'href="(https://(?:www\.)?siraatskitchen\.com[^"?]*)"', lambda x: f'href="{x.group(1)}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={tag}-{(x.group(1).rstrip("/").split("/")[-1] or "home").replace(".com","home")}"', h)
    hdr, ftr = utm_nav(hdr, 'nav'), utm_nav(ftr, 'ft')

    # hero-aanwezigheid als variabele (h=1 hero, h=0 geen)
    b = ''
    # topbalk (alleen als er een aanbod is)
    b += ('{% if h or s %}' + f'<tr><td align="center" bgcolor="{INK}" style="background-color:{INK};padding:11px 20px;{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:600;color:{CREAM};text-transform:uppercase;">'
          f'YOUR 15% THANK&#8209;YOU &middot; <span style="white-space:nowrap;">CODE {CODE}</span> &middot; <span style="white-space:nowrap;">ENDS NOV 30</span></td></tr>\n' + '{% endif %}')
    b += hdr + '\n'
    b += ('{% if h or s %}' + f'<tr><td align="center" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:34px 40px 0 40px;text-align:center;"><div style="{F}font-size:12px;line-height:16px;letter-spacing:2px;font-weight:600;color:{BRICK};">A THANK&#8209;YOU FOR YOUR ORDER</div>'
          f'<div class="h1x" style="{S}font-size:42px;line-height:46px;color:{INK};padding-top:10px;">' + '{% if h %}{% if io == 0 %}The rest of the kitchen, 15% off.{% else %}Three pans, three lids. 15% off.{% endif %}{% else %}Picked from what you looked at.{% endif %}</div></td></tr>\n')
    b += p("Hi {{ first_name|default:'there' }}, thanks for your order. As a thank&#8209;you, here is 15% off, once, " +
           "{% if h %}{% if s %}on the set that rounds out your kitchen and on the pieces you had a look at.{% else %}on the set that rounds out your kitchen.{% endif %}{% else %}on the pieces you had a look at.{% endif %}",
           "14px 40px 0 40px", al="center")
    b += '{% if h %}{% if io == 0 %}' + hero('set12') + '{% else %}' + hero('set6') + '{% endif %}{% endif %}'
    # kaarten
    cards = ''.join(('{% if t == "' + prod['t'] + '" %}{% if ' + owned_cond(prod['key']) + ' %}{% else %}' + card(prod) + '{% endif %}{% endif %}') for prod in CARD_P)
    b += ('{% if s %}' + f'<tr><td align="center" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:34px 40px 2px 40px;text-align:center;"><div style="{F}font-size:12px;line-height:16px;letter-spacing:2px;font-weight:600;color:{BRICK};">YOU HAD A LOOK AT THESE</div>'
          f'<div style="{S}font-size:28px;line-height:32px;color:{INK};padding-top:8px;">Same code, 15% off each.</div></td></tr>\n'
          '{% for t in s|slice:":5" %}' + cards + '{% endfor %}{% endif %}')
    # code-blok
    b += (
          f'<tr><td bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:28px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{ESP}" style="background-color:{ESP};border-radius:10px;"><tr><td align="center" bgcolor="{ESP}" style="background-color:{ESP};padding:22px 24px;text-align:center;">'
          f'<div style="{F}font-size:12px;line-height:16px;letter-spacing:2px;font-weight:600;color:#D9C6BC;">YOUR CODE</div>'
          f'<div style="padding-top:10px;"><span style="display:inline-block;border:1px dashed #D9C6BC;border-radius:6px;padding:8px 16px;{F}font-size:20px;line-height:24px;font-weight:800;letter-spacing:2px;color:#FFFFFF;white-space:nowrap;">{CODE}</span></div>'
          f'<div style="{F}font-size:13px;line-height:20px;color:#D9C6BC;padding-top:10px;">15% off, one use, on any of the pieces in this email. Already applied through every button. Ends {END_LINE}, when our Black Friday sale ends.</div></td></tr></table></td></tr>\n')
    # Benjamin
    b += p("{% if h %}Every pan and pot we make has the same pure titanium cooking surface as the one you just ordered, no coatings. Nothing on it to wear off, so our cookware is covered by the 75-year warranty.{% else %}Thank you for cooking with us. If anything about your order is not right, reply and our team will help.{% endif %}", "26px 40px 0 40px")
    rq = quote_ok('R025', "I ordered one pan to try it out. I'm so glad I did. I am so happy with this pan that I'm ordering the set.")
    b += ('{% if h %}' + f'<tr><td bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:22px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{CREAM}" style="background-color:{CREAM};border:1px solid {SAND};border-radius:10px;"><tr><td align="center" bgcolor="{CREAM}" style="background-color:{CREAM};padding:20px 24px;text-align:center;">'
          f'<div style="{F}font-size:15px;line-height:18px;letter-spacing:3px;color:{BRICK};">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
          f'<div style="{S}font-size:22px;line-height:29px;color:{INK};padding-top:8px;">&ldquo;{rq}&rdquo;</div>'
          f'<div style="{F}font-size:12px;line-height:17px;color:#8A847A;padding-top:8px;">Sunny C. &middot; Verified buyer</div></td></tr></table></td></tr>\n' + '{% endif %}')
    def prom(t, s_):
        return f'<td width="50%" valign="top" align="center" style="width:50%;padding:16px 6px;text-align:center;"><div style="{S}font-size:24px;line-height:28px;color:{INK};">{t}</div><div style="{F}font-size:12px;line-height:17px;color:#8A847A;padding-top:4px;">{s_}</div></td>'
    b += (f'<tr><td bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:22px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {SAND};border-bottom:1px solid {SAND};"><tr>'
          + prom('75-year warranty', 'On our cookware, against defects.') + prom('30-day returns', 'Unused, within 30 days of delivery.') + '</tr></table></td></tr>\n')
    b += p("Thank you for cooking with us,", "22px 40px 4px 40px")
    b += f'<tr><td align="left" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:4px 40px 14px 40px;text-align:left;"><div style="{F}font-size:17px;line-height:24px;color:{INK};font-weight:600;">Benjamin</div><div style="{F}font-size:14px;line-height:20px;color:#8A847A;">Founder, Siraat</div></td></tr>\n'
    b += p(f"P.S. {CODE} works once and ends {END_LINE}. After that it stops working. Reply and our team will help with anything about your order.", "4px 40px 26px 40px", size=15, col=GREY)
    b += ('{% else %}' + p("Hi {{ first_name|default:'there' }}, thanks for your order. We will email your tracking link as soon as it ships. If anything about your order is not right, reply and our team will help.", "34px 40px 0 40px")
          + f'<tr><td align="left" bgcolor="#FFFFFF" class="pad" style="background-color:#FFFFFF;padding:14px 40px 30px 40px;text-align:left;"><div style="{F}font-size:17px;line-height:24px;color:{INK};font-weight:600;">Benjamin</div><div style="{F}font-size:14px;line-height:20px;color:#8A847A;">Founder, Siraat</div></td></tr>\n'
          + '{% endif %}')
    b += ftr
    body = b.replace('{% if h or s %}', '{% if s or ' + HERO_OK + ' %}').replace('{% if h %}', '{% if ' + HERO_OK + ' %}')
    pre = ('{% with cc=event.extra.shipping_address.country_code|default:"XX" %}{% with io=cc|cut:"US"|length %}{% with off=io|add:io|add:io|add:io|add:io|add:io|add:io|add:io %}'
           '{% with items0=event.Items|join:"|" so0=person|lookup:\'siraat_owned\'|join:"|" %}{% with items="|"|add:items0|add:"|" so="|"|add:so0|add:"|" %}'
           + CHAIN)
    post = CHAIN_END + '{% endwith %}{% endwith %}{% endwith %}{% endwith %}{% endwith %}'
    preview = 'Thanks for your order. Here is 15% off, once, until Monday, Nov 30.'
    html = (head.replace(re.search(r'<title>[^<]*</title>', head).group(0), '<title>15% off, once, as a thank-you</title>') + '<body style="margin:0;padding:0;background:#FFFFFF;">\n'
            f'<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;">{preview}' + '&#847;&zwnj;&nbsp;' * 60 + '</div>\n'
            '<table bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;" width="100%">\n<tr><td align="center" style="padding:8px 0 32px 0;">\n'
            '<table bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" class="w" role="presentation" style="width:100%;max-width:600px;background:#FFFFFF;" width="600">\n'
            + pre + body + post + '</table>\n</td></tr>\n</table>\n</body>\n</html>\n')
    assert '—' not in html and '{{SHARED}}' not in html and '{{IMG}}' not in html
    # besturingstags in tabelcontext in commentaar (PLAYBOOK 12): {% if %} tussen <tr>'s
    html = re.sub(r'(\{%[^%]*%\})', lambda m: '<!--' + m.group(1) + '-->' if not m.group(1).startswith('{% with x1') else '<!--' + m.group(1) + '-->', html)
    open(os.path.join(ROOT, 'ppv-tailored.html'), 'w').write(html)
    print('ppv-tailored.html', len(html), 'bytes')

if __name__ == '__main__':
    build()
