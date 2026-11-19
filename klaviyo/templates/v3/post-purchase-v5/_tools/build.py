"""PP v5 · Post-purchase + delivery (DRAFT, 19 nov 2026). NIET LIVE. Bouwt 7 code-templates in ../out/:
  pp1-first, pp1-repeat   bevestiging en verwachting (Placed Order + 1 uur)
  pp2-upsell              getailorde upsell VIP15-PICKS (dag 2, 09:00), logica uit post-purchase-viewed (YyGsj3, ppv_vr_*)
  pp3-delivered, pp3-safe eerste gebruik: het ei, de chef-stappen, het deksel (bezorgd rond dag 8, anders dag 11)
  pp4-code, pp4-nocode    cross-sell rond dag 21 (P3_THANKYOU_10_14D, 10% 14 dagen; nocode bij cooldown)
Vaste header en footer uit klaviyo/templates/partials. Beeldsecties uit sections/ (CDN-url via sections/klaviyo-urls.txt,
anders lokaal pad voor previews). Land = verzendland van de order (PLAYBOOK v5lib: event.extra.shipping_address.country_code).
Gebruik: python3 -I _tools/build.py
"""
import re, os, sys, json
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../..'))
sys.path.insert(0, os.path.join(REPO, 'klaviyo/templates/v3/post-purchase-viewed/_tools'))
import build_tailored as bt  # noqa: E402  (ppv-logica: owned_cond, CHAIN, HERO_OK)
from catalog import ALL, P, BYKEY, TINT  # noqa: E402
V6D = os.path.join(REPO, 'klaviyo/templates/v3/welcome/v6d-envelope-rich')
PART = os.path.join(REPO, 'klaviyo/templates/partials')
OUTD = os.path.join(ROOT, 'out'); os.makedirs(OUTD, exist_ok=True)
def load(p): return dict(l.split() for l in open(p) if len(l.split()) == 2) if os.path.exists(p) else {}
urls = load(os.path.join(PART, 'shared/klaviyo-urls.txt'))
urls.update({k: v for k, v in load(os.path.join(REPO, 'klaviyo/templates/v3/post-purchase/assets/klaviyo-urls.txt')).items() if k in ('fb.png', 'ig.png')})
V6U = load(os.path.join(V6D, 'klaviyo-urls.txt'))
PPU = load(os.path.join(REPO, 'klaviyo/templates/v3/post-purchase/assets/klaviyo-urls.txt'))
OWN = load(os.path.join(ROOT, 'sections/klaviyo-urls.txt'))
LOCAL = '--local' in sys.argv
def src(key):
    if key.startswith('torn-') or key == 'gifts-flatlay.jpg':
        return (None if LOCAL else V6U.get(key)) or os.path.join(V6D, 'sections', key)
    if key == 'egg-slide-lite.gif':
        return (None if LOCAL else PPU.get(key)) or os.path.join(REPO, 'klaviyo/templates/v3/post-purchase/assets', key)
    return (None if LOCAL else OWN.get(key)) or os.path.join(ROOT, 'sections', key)

CAMP = 'pp-v5'
F = "font-family:Inter,Arial,Helvetica,sans-serif;"
INK, BODY, BRICK, CREAM, SAND, DARK, W, ESP, GREY = '#272727', '#2E2E2E', '#AC3B19', '#F8F7F2', '#ECE7DD', '#282828', '#FFFFFF', '#321E1D', '#727272'
US = "event.extra.shipping_address.country_code == 'US'"
FR_US, FR_INT = 'Free shipping. 30-day returns. 100,000+ happy customers.', 'Free shipping, duties paid. 30-day returns. 100,000+ happy customers.'
FRC_US, FRC_INT = 'One use, already applied. 30-day returns. 100,000+ happy customers.', 'One use, already applied. Duties paid. 30-day returns.'
def fr(code=False):
    a, b = (FRC_US, FRC_INT) if code else (FR_US, FR_INT)
    return f'{{% if {US} %}}{a}{{% else %}}{b}{{% endif %}}'
# De Shopify Digital Downloads-link uit DECISIONS 8 okt (delivery.shopifyapps.com/-/b3a2...) geeft op 19 nov 404, ook in de live P1. Daarom de e-bookpagina (DECISIONS 7 okt).
EBOOK = 'https://siraatskitchen.com/products/e?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign=pp-v5&amp;utm_content=ebook'
def U(c, path='/collections/all'):
    return f'https://siraatskitchen.com{path}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={c}'
def UP(c, handle): return U(c, '/products/' + handle)
P3CODE = "{% coupon_code 'P3_THANKYOU_10_14D' %}"
def UC(c, handle, code):
    """Link met de code al toegepast (Shopify /discount/<code>?redirect=), UTM's URL-gecodeerd in de redirect."""
    return ('https://siraatskitchen.com/discount/' + code + '?redirect=' +
            quote(f'/products/{handle}?utm_source=klaviyo&utm_medium=email&utm_campaign={CAMP}&utm_content={c}', safe=''))
DATE14 = "{% today '%Y-%m-%d' as today %}{{ today|days_later:14|format_date_string|date:'M j' }}"

def money(x): return ('$%s' % format(x, ',.2f')).replace('.00', '')
def disc(x, pct): return '$%s' % format(round(x * (1 - pct / 100) + 1e-9, 2), ',.2f')

class Mail:
    def __init__(s, name, subject, preview): s.rows, s.name, s.subject, s.preview = [], name, subject, preview
    def add(s, h): s.rows.append(h); return s
    def img(s, key, alt, href, bg=CREAM):
        return s.add(f'<tr><td bgcolor="{bg}" style="background-color:{bg};padding:0;font-size:0;line-height:0;"><a href="{href}" style="display:block;border:0;"><img src="{src(key)}" width="600" alt="{alt}" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>\n')
    def torn(s, a, b): return s.img(f'torn-{a[1:]}-{b[1:]}.jpg', '', U('edge'), bg=a)
    def live(s, bg, inner, pad='22px 40px 26px 40px', align='center'):
        return s.add(f'<tr><td align="{align}" bgcolor="{bg}" class="pad" style="background-color:{bg};padding:{pad};text-align:{align};">{inner}</td></tr>\n')
    @staticmethod
    def btn(label, href, dark=False, w=400):
        bb, fc = (W, INK) if dark else (INK, W)
        return (f'<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="{w}" style="width:100%;max-width:{w}px;margin:0 auto;"><tr><td align="center" bgcolor="{bb}" style="background-color:{bb};border-radius:40px;">'
                f'<a href="{href}" style="display:block;padding:19px 16px;{F}font-size:15px;line-height:18px;font-weight:600;letter-spacing:1.2px;color:{fc};text-decoration:none;text-transform:uppercase;">{label} &rarr;</a></td></tr></table>')
    def cta(s, bg, label, href, sub=None, lead=None, pad='6px 40px 32px 40px', dark=False):
        sc = '#F1D9CB' if bg in (BRICK, ESP) else ('#CFC8BC' if bg == DARK else GREY)
        tc = W if bg in (BRICK, DARK, ESP) else BODY
        top = f'<div class="lead" style="{F}font-size:17px;line-height:27px;color:{tc};padding-bottom:20px;text-align:left;">{lead}</div>' if lead else ''
        return s.live(bg, top + s.btn(label, href, dark) + (f'<div style="{F}font-size:12px;line-height:18px;color:{sc};padding-top:10px;">{sub}</div>' if sub else ''), pad)
    def text(s, bg, t, pad='18px 40px 0 40px', size=17, col=BODY, w=400, align='left'):
        return s.live(bg, f'<div style="{F}font-size:{size}px;line-height:{round(size * 1.6)}px;color:{col};font-weight:{w};">{t}</div>', pad, align)
    def eyebrow(s, bg, eb, pad='30px 40px 0 40px'):
        return s.live(bg, f'<div style="{F}font-size:12px;line-height:16px;letter-spacing:2px;font-weight:600;color:{BRICK};text-transform:uppercase;">{eb}</div>', pad)
    def promises(s, bg=CREAM):
        def cell(t, s_): return f'<td width="50%" valign="top" align="center" style="width:50%;padding:16px 6px;text-align:center;"><div style="font-family:\'Instrument Serif\',\'Times New Roman\',Times,serif;font-style:italic;font-size:24px;line-height:28px;color:{INK};">{t}</div><div style="{F}font-size:12px;line-height:17px;color:#8A847A;padding-top:4px;">{s_}</div></td>'
        return s.live(bg, f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {SAND};border-bottom:1px solid {SAND};"><tr>'
                      + cell('75-year warranty', 'On our cookware, against defects.') + cell('30-day returns', 'Unused, within 30 days of delivery.') + '</tr></table>', '22px 40px 0 40px')
    def sign(s, ps=None, bg=CREAM):
        s.live(bg, f'<div style="{F}font-size:17px;line-height:27px;color:{BODY};">Thank you for cooking with us,</div><div style="{F}font-size:17px;line-height:24px;color:{INK};font-weight:600;padding-top:12px;">Benjamin</div><div style="{F}font-size:14px;line-height:20px;color:#8A847A;">Founder, Siraat</div>', '22px 40px 14px 40px', 'left')
        if ps: s.text(bg, ps, '4px 40px 28px 40px', size=15, col='#5E5A54')
        return s
    def topbar(s, t, href):
        return s.add(f'<tr><td align="center" bgcolor="{INK}" style="background-color:{INK};padding:11px 16px;{F}font-size:11px;line-height:15px;letter-spacing:2px;font-weight:600;color:{CREAM};text-transform:uppercase;"><a href="{href}" style="color:{CREAM};text-decoration:none;">{t}</a></td></tr>\n')

    def html(s, pre='', post=''):
        hdr = open(os.path.join(PART, 'header.html')).read(); ftr = open(os.path.join(PART, 'footer.html')).read()
        for k, v in urls.items():
            hdr = hdr.replace('{{SHARED}}/' + k, v); ftr = ftr.replace('{{SHARED}}/' + k, v).replace('{{IMG}}/' + k, v)
        hdr = re.sub(r'<!--.*?-->\n?', '', hdr, flags=re.S); ftr = re.sub(r'<!--.*?-->\n?', '', ftr, flags=re.S)
        def utm_nav(h, tag):
            return re.sub(r'href="(https://(?:www\.)?siraatskitchen\.com[^"?]*)"', lambda m: f'href="{m.group(1)}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={tag}-{(m.group(1).rstrip("/").split("/")[-1] or "home").replace(".com", "home")}"', h)
        body = ''.join(s.rows).replace('{{HEADER}}', utm_nav(hdr, 'nav')).replace('{{FOOTER}}', utm_nav(ftr, 'ft'))
        head = open(os.path.join(REPO, 'klaviyo/templates/v3/welcome/v6-envelope/e1.html')).read().split('<body')[0]
        i = head.rindex('</style>')
        head = head[:i] + '@media only screen and (max-width: 480px) { .h1x { font-size:34px !important; line-height:38px !important; } }\n' + head[i:]
        head = re.sub(r'<title>[^<]*</title>', f'<title>{s.subject}</title>', head)
        html = (head + '<body style="margin:0;padding:0;background:#FFFFFF;">\n'
                f'<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;">{s.preview}' + '&#847;&zwnj;&nbsp;' * 60 + '</div>\n'
                '<table bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;" width="100%">\n<tr><td align="center" style="padding:8px 0 32px 0;">\n'
                f'<table bgcolor="{CREAM}" border="0" cellpadding="0" cellspacing="0" class="w" role="presentation" style="width:100%;max-width:600px;background-color:{CREAM};" width="600">\n'
                + pre + body + post + '</table>\n</td></tr>\n</table>\n</body>\n</html>\n')
        assert '—' not in html, s.name
        assert '{{SHARED}}' not in html and '{{IMG}}' not in html
        # besturingstags tussen tabelrijen in commentaar (PLAYBOOK 12), uitvoertags laten staan
        html = re.sub(r'(?<!<!--)(\{%\s*(?:if|elif|else|endif|for|endfor|with|endwith)\b[^%]*%\})', r'<!--\1-->', html)
        # ... maar niet binnen attributen of binnen een <div>-tekst: daar mag het commentaar ook staan (HTML-commentaar in tekst is onschadelijk)
        return html

def card_live(prod, pct, code, content, us_only=None):
    """Live onderkant van een productkaart in dezelfde tint als het kaartbeeld (card-<key>.jpg)."""
    k, h, tint = prod['key'], prod['handle'], TINT[prod['key']]
    url = UC(content, h, code) if code else UP(content, h)
    pre = 'from ' if prod['frm'] else ''
    was = f'<span style="text-decoration:line-through;color:#8A847A;">{money(prod["was"])}</span>&nbsp; ' if prod.get('was') else ''
    if code:
        pr_us = (f'<div style="{F}font-size:14px;line-height:20px;color:#5E5A54;padding-top:10px;">{was}{pre}{money(prod["price"])}</div>'
                 f'<div style="{F}font-size:24px;line-height:30px;font-weight:800;color:{INK};">{pre}{disc(prod["price"], pct)} <span style="font-size:13px;font-weight:400;color:#5E5A54;">with your code</span></div>')
        pr_int = f'<div style="{F}font-size:24px;line-height:30px;font-weight:800;color:{INK};padding-top:10px;">{pct}% off <span style="font-size:13px;font-weight:400;color:#5E5A54;">with your code</span></div>'
        label = f'Get {pct}% off'
    else:
        pr_us = f'<div style="{F}font-size:24px;line-height:30px;font-weight:800;color:{INK};padding-top:10px;">{was}{pre}{money(prod["price"])}</div>'
        pr_int = ''
        label = 'Add it to my kitchen'
    usonly = prod['us'] if us_only is None else us_only
    prices = pr_us if usonly else f'{{% if {US} %}}{pr_us}{{% else %}}{pr_int}{{% endif %}}'
    alt = re.sub('&[a-zA-Z]+;', '', prod['name'])
    return (f'<tr><td bgcolor="{CREAM}" style="background-color:{CREAM};padding:0;font-size:0;line-height:0;"><a href="{url}" style="display:block;border:0;"><img src="{src("card-" + k + ".jpg")}" width="600" alt="{alt}" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>\n'
            f'<tr><td align="center" bgcolor="{CREAM}" style="background-color:{CREAM};padding:0 0 18px 0;">'
            f'<table role="presentation" width="93.4%" cellpadding="0" cellspacing="0" border="0" bgcolor="{tint}" style="width:93.4%;background-color:{tint};border-radius:0 0 20px 20px;"><tr><td align="center" bgcolor="{tint}" style="background-color:{tint};padding:4px 22px 24px 22px;text-align:center;border-radius:0 0 20px 20px;">'
            f'<div style="{F}font-size:18px;line-height:24px;font-weight:600;color:{INK};"><a href="{url}" style="color:{INK};text-decoration:none;">{prod["name"]}</a></div>'
            f'<div style="{F}font-size:14px;line-height:21px;color:#5E5A54;padding-top:4px;">{prod["line"]}</div>' + prices +
            f'<div style="padding-top:14px;"><a href="{url}" style="display:inline-block;background-color:{INK};border-radius:24px;padding:13px 22px;{F}font-size:13px;line-height:14px;font-weight:600;letter-spacing:1.2px;color:#FFFFFF;text-decoration:none;text-transform:uppercase;">{label} &rarr;</a></div>'
            '</td></tr></table></td></tr>\n')

def codebox(code_html, note, bg=CREAM):
    return (f'<tr><td bgcolor="{bg}" class="pad" style="background-color:{bg};padding:10px 40px 6px 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{ESP}" style="background-color:{ESP};border-radius:16px;"><tr><td align="center" bgcolor="{ESP}" style="background-color:{ESP};padding:24px 24px;text-align:center;border-radius:16px;">'
            f'<div style="{F}font-size:12px;line-height:16px;letter-spacing:2px;font-weight:600;color:#D9C6BC;">YOUR CODE</div>'
            f'<div style="padding-top:10px;"><span style="display:inline-block;border:1px dashed #D9C6BC;border-radius:6px;padding:8px 16px;{F}font-size:20px;line-height:24px;font-weight:800;letter-spacing:2px;color:#FFFFFF;white-space:nowrap;">{code_html}</span></div>'
            f'<div style="{F}font-size:13px;line-height:20px;color:#D9C6BC;padding-top:10px;">{note}</div></td></tr></table></td></tr>\n')

REV = json.load(open(os.path.join(os.path.dirname(__file__), 'reviews.json')))
def revalt(k): return 'Five stars from 100,000+ happy customers. ' + ' '.join(f'{q["name"]}: {re.sub("&[a-z]+;", "", q["quote"])}' for q in REV[k]['quotes'])

MAILS = {}
# =====================================================================================  PP1 · bevestiging
for kind in ('first', 'repeat'):
    m = Mail(f'pp1-{kind}', "Good call. Here's what happens next." if kind == 'first' else 'Good to see you again',
             'Order confirmed. Your 5 free gifts, your e-book and the one tip that matters.')
    m.topbar('Free shipping &middot; 30-day returns &middot; 75-year warranty', U('topbar'))
    m.add('{{HEADER}}\n')
    m.img(f'pp1-hero-{kind}.jpg', ('Order confirmed. Good call. ' if kind == 'first' else 'Order confirmed. Good to see you again. ') + 'Here is what happens next. Two hands hold up hammered titanium pans against a brick red background.', U('hero', '/pages/care-use'), bg=BRICK)
    intro = ("Hi {{ first_name|default:'there' }}, your order is in. You chose a pure titanium cooking surface with no coatings, so there is nothing on it to wear off, and it is covered for 75 years. You may be wondering whether it keeps its promises. The first egg will tell you."
             if kind == 'first' else
             "Hi {{ first_name|default:'there' }}, thank you for ordering again. The same pure titanium cooking surface, no coatings, the same 75-year warranty. And your 5 free gifts come with this order too.")
    m.text(CREAM, intro, '30px 40px 0 40px')
    # orderblok (live, Placed Order line_items)
    m.add(f'<tr><td bgcolor="{CREAM}" class="pad" style="background-color:{CREAM};padding:22px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{W}" style="background-color:{W};border-radius:16px;"><tr><td bgcolor="{W}" style="background-color:{W};padding:20px 22px 12px 22px;border-radius:16px;">'
          f'<div style="{F}font-size:12px;line-height:16px;letter-spacing:2px;font-weight:600;color:{BRICK};">ORDER {{{{ event.extra.name|default:\'\' }}}}</div>'
          '{% for item in event.extra.line_items %}'
          f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:10px 0;border-bottom:1px solid {SAND};{F}font-size:15px;line-height:21px;color:{INK};">{{{{ item.title }}}}</td>'
          f'<td align="right" style="padding:10px 0 10px 10px;border-bottom:1px solid {SAND};{F}font-size:14px;line-height:21px;color:#8A847A;white-space:nowrap;">Qty {{{{ item.quantity|floatformat:0 }}}}</td></tr></table>'
          '{% endfor %}'
          f'<div style="{F}font-size:13px;line-height:20px;color:#8A847A;padding-top:12px;">Tracking link by email as soon as it ships.</div></td></tr></table></td></tr>\n')
    m.cta(CREAM, 'Download my free e-book', EBOOK, sub='One of your 5 free gifts. Questions? Reply and our team will help.', pad='26px 40px 32px 40px')
    m.torn(CREAM, SAND)
    m.img('gifts-flatlay.jpg', '5 free gifts in the box with every order: free shipping, the Favorites Cookbook, the plastic-free e-book, a mystery gift and a chance to win a PFAS water filter.', EBOOK, bg=SAND)
    m.torn(SAND, CREAM)
    m.img('pp1-tip.jpg', 'Before it arrives: heat first, then oil, then the egg. 1 medium heat for 2 to 3 minutes, never higher. 2 the water test: drops bead up and glide. 3 then oil, a thin layer, then the egg.', U('tip', '/pages/care-use'))
    m.cta(CREAM, "Watch the chef's first cook", U('tip-cta', '/pages/care-use'), sub='Two to three minutes of heat. Then breakfast.', pad='4px 40px 34px 40px')
    m.torn(CREAM, SAND)
    m.img('pp1-next.jpg', "What happens next, from order to first egg. 1 packed with your 5 free gifts. 2 tracking by email the moment your order ships. 3 the day it lands we send the chef's first cook, five short steps.", U('next', '/pages/care-use'), bg=SAND)
    m.torn(SAND, CREAM)
    m.img('rev-pp1.jpg', revalt('pp1'), UP('reviews', 'original-siraat-100-pure-titanium-pan-with-hammered-pattern'))
    m.promises()
    m.sign('P.S. Something not right with your order, the address or the size? Reply to this email and our team will help.')
    m.add('{{FOOTER}}\n')
    MAILS[m.name] = (m, '', '')

# =====================================================================================  PP2 · getailorde upsell (VIP15-PICKS)
bt.CAMP = CAMP + '-upsell'
CODE = bt.CODE
END = bt.END_LINE
m = Mail('pp2-upsell', 'A thank-you: 15% off, picked for you', 'Your order is on its way. Here is 15% off, once, until Monday, Nov 30.')
m.add('{% if h or s %}')
m.topbar(f'Your 15% thank&#8209;you &middot; <span style="white-space:nowrap;">code {CODE}</span> &middot; <span style="white-space:nowrap;">ends Nov 30</span>', U('topbar'))
m.add('{% endif %}')
m.add('{{HEADER}}\n')
m.add('{% if h or s %}')
m.text(CREAM, "Hi {{ first_name|default:'there' }}, your order is on its way. As a thank&#8209;you, here is 15% off, once, " +
       "{% if h %}{% if s %}on the set that rounds out your kitchen and on the pieces you had a look at.{% else %}on the set that rounds out your kitchen.{% endif %}{% else %}on the pieces you had a look at.{% endif %} The code is already in every button.",
       '30px 40px 26px 40px')
m.add('{% if h %}')
m.add(f'{{% if {US} %}}')
m.img('pp2-top12.jpg', 'A thank-you for your order, the rest of the kitchen: Cookware Set, 12 pieces, 3 pans, 3 pots and 6 lids. 15% off: $551.65 with your code VIP15-PICKS, was $649, compare at $2,047.', bt.U(bt.SET12['handle'], 'set12-img'), bg=SAND)
m.cta(SAND, 'Get 15% off the set', bt.U(bt.SET12['handle'], 'set12-cta'), sub=FRC_US, pad='0 40px 34px 40px')
m.add('{% else %}')
m.img('pp2-top6.jpg', 'A thank-you for your order, three pans, three lids: Pan Set, 6 pieces, Mini, Small and Large, each with a fitted lid. 15% off with your code VIP15-PICKS.', bt.U(BYKEY['s06']['handle'], 'set6-img'), bg=SAND)
m.cta(SAND, 'Get 15% off the set', bt.U(BYKEY['s06']['handle'], 'set6-cta'), sub=FRC_INT, pad='0 40px 34px 40px')
m.add('{% endif %}')
m.torn(SAND, CREAM)
m.add('{% endif %}')
cards = ''.join(('{% if t == "' + prod['t'] + '" %}{% if ' + bt.owned_cond(prod['key']) + ' %}{% else %}' + card_live(prod, 15, CODE, prod['key']) + '{% endif %}{% endif %}') for prod in P)
m.add('{% if s %}')
m.img('pp2-h-viewed.jpg', 'You had a look at these. Same code, 15% off each.', U('h-viewed'))
m.add('{% for t in s|slice:":3" %}' + cards + '{% endfor %}')
m.add('{% endif %}')
m.add(codebox(CODE, f'15% off, one use, on any of the pieces in this email. Already applied through every button. Ends {END}, when our Black Friday sale ends. After that the regular price applies.'))
m.add('{% if h %}')
m.img('rev-pp2.jpg', revalt('pp2'), UP('reviews', 'original-siraat-100-pure-titanium-pan-with-hammered-pattern'))
m.add('{% endif %}')
m.promises()
m.sign(f'P.S. {CODE} works once and ends {END}. Reply and our team will help with anything about your order.')
m.add('{% else %}')
m.text(CREAM, "Hi {{ first_name|default:'there' }}, your order is on its way. Thank you for cooking with us. If anything about your order is not right, reply and our team will help.", '34px 40px 0 40px')
m.sign()
m.add('{% endif %}')
m.add('{{FOOTER}}\n')
def _pp2_fix(html):
    return html.replace('{% if h or s %}', '{% if s or ' + bt.HERO_OK + ' %}').replace('{% if h %}', '{% if ' + bt.HERO_OK + ' %}')
PRE2 = ('{% with cc=event.extra.shipping_address.country_code|default:"XX" %}{% with io=cc|cut:"US"|length %}{% with off=io|add:io|add:io|add:io|add:io|add:io|add:io|add:io %}'
        '{% with items0=event.Items|join:"|" so0=person|lookup:\'siraat_owned\'|join:"|" %}{% with items="|"|add:items0|add:"|" so="|"|add:so0|add:"|" %}' + bt.CHAIN)
POST2 = bt.CHAIN_END + '{% endwith %}{% endwith %}{% endwith %}{% endwith %}{% endwith %}'
MAILS['pp2-upsell'] = (m, PRE2, POST2)

# =====================================================================================  PP3 · eerste gebruik
LIDSIZE = [('Pan Pro Large', '12&Prime;', '30 cm'), ('Pan Pro Standard', '11&Prime;', '28 cm'), ('Pan Pro Small', '10&Prime;', '26 cm'), ('Pan Pro Mini', '8&Prime;', '20 cm')]
def lid_line():
    out = ''
    for i, (frag, inch, cm) in enumerate(LIDSIZE):
        out += ('{% if ' if i == 0 else '{% elif ') + f"'{frag}' in items %}}{{% if {US} %}}Your {inch} Pan Pro takes the {inch} lid.{{% else %}}Your Pan Pro takes the {cm} lid, same diameter.{{% endif %}}"
    return out + '{% else %}Pick the same diameter as your pan: 8, 10, 11 or 12 inch (20, 26, 28 or 30 cm).{% endif %}'
LIDOK = "'Pan Pro' in items and not 'Lid' in items and not 'Pcs' in items and not 'Edition' in items and not 'Duo' in items and not 'Set' in items"
for kind in ('delivered', 'safe'):
    m = Mail(f'pp3-{kind}', 'Your first egg, step by step' if kind == 'delivered' else 'Before your first cook: the egg',
             "Medium on titanium works like high on a normal pan. The chef's five steps." if kind == 'delivered' else 'Heat first, then oil, then the egg. Keep this for your first cook.')
    m.add('{{HEADER}}\n')
    m.img(f'pp3-hero-{kind}.jpg', ("It's here. " if kind == 'delivered' else 'For your first cook. ') + 'Your first egg, step by step. A fried egg slides out of a hammered titanium pan onto toast.', U('hero', '/pages/care-use'))
    intro = ("Hi {{ first_name|default:'there' }}, your order has arrived. You may be wondering whether it keeps its promises. The first egg will tell you, and before it, one thing to know: there is no coating on it, so the release comes from heat and timing, not chemicals."
             if kind == 'delivered' else
             "Hi {{ first_name|default:'there' }}, your order is either on your stove already or on its way to you. We cannot see which, so here is the chef's first cook now. Keep it for the morning you unbox it. There is no coating on it, so the release comes from heat and timing, not chemicals.")
    m.text(CREAM, intro, '8px 40px 0 40px')
    m.cta(CREAM, "Watch the chef's first cook", U('cta1', '/pages/care-use'), sub='Two to three minutes of heat. Then breakfast.', pad='24px 40px 34px 40px')
    m.torn(CREAM, DARK)
    m.img('pp3-steps.jpg', "The chef's first cook. Cold metal grabs, hot metal lets go. 1 preheat on medium, 2 to 3 minutes. 2 do the water test: drops bead up and glide. 3 add a thin layer of oil. 4 eggs: turn the heat down to low, once the white sets it lets go. 5 meat and fish: lay it down, then leave it.", U('steps', '/pages/care-use'), bg=DARK)
    m.torn(DARK, CREAM)
    m.img('egg-slide-lite.gif', 'An egg slides across a hammered titanium pan', U('gif', '/pages/care-use'))
    m.live(CREAM, f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{SAND}" style="background-color:{SAND};border-radius:16px;"><tr><td bgcolor="{SAND}" style="background-color:{SAND};padding:22px 24px;border-radius:16px;text-align:left;">'
           f'<div style="{F}font-size:12px;line-height:16px;letter-spacing:2px;font-weight:600;color:{BRICK};">IF SOMETHING STICKS</div>'
           f'<div style="font-family:\'Instrument Serif\',\'Times New Roman\',Times,serif;font-style:italic;font-size:26px;line-height:31px;color:{INK};padding-top:8px;">A sticky pan is not a ruined pan.</div>'
           f'<div style="{F}font-size:16px;line-height:25px;color:{BODY};padding-top:10px;">Usually the pan was not hot enough yet, or the food moved too early. Mix baking soda with a little water, rub it over the surface with a soft sponge and rinse. Back to day one. A blue or gold shimmer is harmless heat tint.</div></td></tr></table>', '26px 40px 10px 40px')
    m.add(f'{{% if {LIDOK} %}}')
    m.eyebrow(CREAM, 'For a set yolk on top', '26px 40px 4px 40px')
    m.text(CREAM, 'Cover the pan for the last minute. No lid yet? ' + lid_line(), '6px 40px 16px 40px', size=16, align='center')
    m.add(card_live(ALL['lid'], 0, None, 'lid'))
    m.add('{% endif %}')
    m.img('rev-pp3.jpg', revalt('pp3'), UP('reviews', 'original-siraat-100-pure-titanium-pan-with-hammered-pattern'))
    m.sign('P.S. Still sticking after the water test? Reply and tell us what you cooked. Our team will work it out with you.')
    m.add('{{FOOTER}}\n')
    MAILS[m.name] = (m, '{% with items0=event.Items|join:"|" %}{% with items="|"|add:items0|add:"|" %}', '{% endwith %}{% endwith %}')

# =====================================================================================  PP4 · cross-sell dag 21
SLOTS = {  # categorie -> 3 plaatsen, elk (voorkeur, alternatief als de voorkeur al in huis is)
    'set': [('std', 'dep'), ('brd', 'wok'), ('ute', 'crp')],
    'pan': [('lid', 'ute'), ('s06', 'dep'), ('brd', 'wok')],
    'acc': [('std', 'lrg'), ('s06', 'dep'), ('brd', 'ute')],
}
ISSET = "'Pcs' in items or 'Edition' in items or 'Cookware Set' in items or 'Bundle' in items or 'Duo' in items or 'Pan Pro Kit' in items or 'Cook & Prep' in items"
ISPAN = "'Pan' in items or 'Wok' in items"
def owned(k):
    if k == 'lid': return "'Lid' in items or person|lookup:'ppv_vr_lid' == 9"
    return bt.owned_cond(k)
def slots(cat, pct, code):
    out = ''
    for a, b in SLOTS[cat]:
        ca = card_live(ALL[a], pct, code, a, us_only=False if a == 's06' else None)
        cb = card_live(ALL[b], pct, code, b, us_only=False if b == 's06' else None)
        out += f'{{% if {owned(a)} %}}{{% if {owned(b)} %}}{{% else %}}{cb}{{% endif %}}{{% else %}}{ca}{{% endif %}}'
    return out
for kind in ('code', 'nocode'):
    code = P3CODE if kind == 'code' else None
    m = Mail(f'pp4-{kind}', 'How is the pan treating you?', ('What owners add next, with your own 10% for 14 days.' if code else 'What owners add next. 5 free gifts with every order.'))
    if code:
        m.topbar(f'Your 10% thank&#8209;you &middot; <span style="white-space:nowrap;">ends {DATE14}</span>', U('topbar'))
    m.add('{{HEADER}}\n')
    m.img('pp4-hero.jpg', 'Three weeks in: the pieces owners add next. A cook laughs in a warm kitchen at night.', U('hero'))
    m.text(CREAM, "Hi {{ first_name|default:'there' }}, a few weeks of cooking by now. This is the point where owners come back for the same few things: a lid, a second size, the board. Here they are, matched to your order, so nothing repeats what is already in your kitchen."
           + (' Your own code takes 10% off, for 14 days.' if code else ' Every order comes with 5 free gifts.'), '8px 40px 0 40px')
    m.cta(CREAM, 'Use my 10% code' if code else 'See what fits my kitchen', ('https://siraatskitchen.com/discount/' + P3CODE + '?redirect=' + quote(f'/collections/all?utm_source=klaviyo&utm_medium=email&utm_campaign={CAMP}&utm_content=pp4-cta1', safe='')) if code else U('pp4-cta1'),
          sub=fr(bool(code)), pad='24px 40px 30px 40px')
    m.img('pp4-h-next.jpg', 'Picked for your kitchen: what owners add next.', U('h-next'))
    m.add(f'{{% if {ISSET} %}}' + slots('set', 10, code) + f'{{% elif {ISPAN} %}}' + slots('pan', 10, code) + '{% else %}' + slots('acc', 10, code) + '{% endif %}')
    if code:
        m.add(codebox(P3CODE, f'10% off, one use, already applied through every button. Made for you, so it has an end date: {DATE14}. After that the regular price applies.'))
    m.img('rev-pp4.jpg', revalt('pp4'), UP('reviews', 'original-siraat-100-pure-titanium-pan-with-hammered-pattern'))
    m.promises()
    m.sign('P.S. Your next order comes with 5 free gifts too. Reply and our team will help you pick the right size.')
    m.add('{{FOOTER}}\n')
    MAILS[m.name] = (m, '{% with items0=event.Items|join:"|" so0=person|lookup:\'siraat_owned\'|join:"|" %}{% with items="|"|add:items0|add:"|" so="|"|add:so0|add:"|" %}', '{% endwith %}{% endwith %}')

META = {}
for name, (m, pre, post) in MAILS.items():
    html = m.html(pre, post)
    if name == 'pp2-upsell': html = _pp2_fix(html)
    open(os.path.join(OUTD, name + '.html'), 'w').write(html)
    META[name] = {'subject': m.subject, 'preview': m.preview, 'bytes': len(html)}
    print(name, len(html) // 1024, 'KB')
json.dump(META, open(os.path.join(OUTD, 'meta.json'), 'w'), indent=1)
