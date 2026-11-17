"""Welcome v6 'The sealed envelope' (concept, 17 nov 2026). NIET LIVE, niet in Klaviyo als template of flow.
Bouwt e1..e5.html (Klaviyo-HTML) en e1..e5-preview.html (Django-tags vervangen) in de map erboven.
Gebruik: python3 -I _tools/build.py   (vanuit klaviyo/templates/v3/welcome/v6-envelope)
Spec: klaviyo/flows/welcome-v6-envelope.md

Eerlijkheidsregels (zie spec):
- Iedereen krijgt hetzelfde envelopje: HI10 (10%, 1x per klant, verloopt niet) + 5 free gifts. Geen 'handpicked', geen VIP,
  geen variabel bedrag, geen deadline of countdown (HI10 heeft geen einddatum).
- Reviews letterlijk uit content/reviews (Trustpilot, 5 sterren), alleen ingekort met '...'.
"""
import re, os
from urllib.parse import quote
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../../..'))
P = os.path.join(REPO, 'klaviyo/templates/partials')
def load_urls(path):
    return dict(l.split() for l in open(path) if len(l.split()) == 2)
urls = load_urls(os.path.join(P, 'shared/klaviyo-urls.txt'))
urls.update(load_urls(os.path.join(REPO, 'klaviyo/templates/v3/campaigns/thanksgiving-roast-1117/assets/klaviyo-urls.txt')))  # fb.png, ig.png
urls.update(load_urls(os.path.join(ROOT, 'assets/klaviyo-urls.txt')))
urls['gift-cookbook.jpg'] = 'https://cdn.klaviyomail.com/company/TdtTzz/images/dabf0446-a5d7-49ae-87f8-672e5692bf5b.jpeg'  # zelfde beeld als F13 (cookbook-tegel)

CAMP = 'v6-welcome-envelope'
CODE = 'HI10'  # welkomstcode: 10%, appliesOncePerCustomer (DECISIONS 8 okt), geen einddatum
H_PAN = '/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern'
H_SET6 = '/products/titanium-hammered-pan-set-with-lids-6-pcs'
H_WOK = '/products/titanium-hammered-wok-pan-pro'
H_ALL = '/collections/all'
REPORT = 'https://siraatskitchen.com/pages/third-party-testing'

F = "font-family:Inter,Arial,Helvetica,sans-serif;"
S = "font-family:'Instrument Serif','Times New Roman',Times,serif;font-style:italic;font-weight:400;"
INK, BRICK, ESP, CREAM, SAND, GREY, GOLD, WHITE = '#272727', '#AC3B19', '#321E1D', '#F8F7F2', '#ECE7DD', '#5E5A54', '#B8862B', '#FFFFFF'
FR = 'Free shipping. 30-day returns. 100,000+ happy customers.'

def utm(c, mail):
    return f'utm_source=klaviyo&utm_medium=email&utm_campaign={CAMP}&utm_content={mail}-{c}'

class Mail:
    def __init__(s, mid): s.mid, s.b = mid, ''
    def U(s, c, path=H_ALL):  # code via /discount/ met URL-encoded redirect inclusief UTM (patroon F13/ROAST15, getest)
        return f'https://siraatskitchen.com/discount/{CODE}?redirect=' + quote(f'{path}?{utm(c, s.mid)}', safe='')
    def plain(s, c, url):
        return f'{url}?{utm(c, s.mid)}'.replace('&', '&amp;')
    # ---- blokken
    def add(s, h): s.b += h; return s
    def codebar(s, text):
        return s.add(f'<tr><td align="center" bgcolor="{INK}" style="background-color:{INK};padding:11px 20px;{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:700;color:{CREAM};text-transform:uppercase;"><a href="{s.U("codebar")}" style="color:{CREAM};text-decoration:none;">{text}</a></td></tr>\n')
    def img(s, key, alt, c, path=H_ALL, w=600, pad='0', radius=0, cls='', link=None):
        href = link or s.U(c, path)
        return s.add(f'<tr><td align="center" bgcolor="{CREAM}"{cls} style="background-color:{CREAM};padding:{pad};"><a href="{href}" style="display:block;border:0;text-decoration:none;"><img src="{urls[key]}" width="{w}" alt="{alt}" style="display:block;width:100%;max-width:{w}px;height:auto;border:0;border-radius:{radius}px;"></a></td></tr>\n')
    def eyebrow(s, label, title, pad='34px 40px 0 40px', al='center'):
        return s.add(f'<tr><td align="{al}" bgcolor="{CREAM}" class="pad" style="background-color:{CREAM};padding:{pad};text-align:{al};"><div style="{F}font-size:12px;line-height:16px;letter-spacing:2.4px;font-weight:700;color:{BRICK};">{label}</div><div class="h2" style="{S}font-size:38px;line-height:42px;color:{INK};padding-top:8px;">{title}</div></td></tr>\n')
    def p(s, t, pad='14px 40px 0 40px', size=17, col='#2E2E2E', al='left', w=400):
        return s.add(f'<tr><td align="{al}" bgcolor="{CREAM}" class="pad" style="background-color:{CREAM};padding:{pad};text-align:{al};"><div class="lead" style="{F}font-size:{size}px;line-height:{round(size*1.55)}px;color:{col};font-weight:{w};">{t}</div></td></tr>\n')
    def btn(s, label, c, path=H_ALL, pad='24px 40px 0 40px', sub=FR):
        s.add(f'<tr><td align="center" bgcolor="{CREAM}" class="pad" style="background-color:{CREAM};padding:{pad};"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="400" style="width:100%;max-width:400px;margin:0 auto;"><tr><td align="center" bgcolor="{INK}" style="background-color:{INK};border-radius:30px;"><a href="{s.U(c, path)}" style="display:block;padding:19px 18px;{F}font-size:15px;line-height:18px;font-weight:700;letter-spacing:1.2px;color:{WHITE};text-decoration:none;text-transform:uppercase;">{label}</a></td></tr></table></td></tr>\n')
        if sub:
            s.add(f'<tr><td align="center" bgcolor="{CREAM}" class="pad" style="background-color:{CREAM};padding:10px 40px 0 40px;text-align:center;"><div style="{F}font-size:12px;line-height:18px;color:#727272;">{sub}</div></td></tr>\n')
        return s
    def sandline(s, pad='30px 40px 0 40px'):  # de zandlijn als detail: goud, kort, leidt naar wat eronder komt
        return s.add(f'<tr><td align="center" bgcolor="{CREAM}" style="background-color:{CREAM};padding:{pad};"><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="140" style="width:140px;"><tr><td height="2" bgcolor="#D2B25C" style="background-color:#D2B25C;height:2px;font-size:0;line-height:0;">&nbsp;</td></tr></table></td></tr>\n')
    def reveal(s, intro):
        """Het 'geopende envelopje': witte kaart met 10%, de code als live tekst en de 5 gifts in een regel."""
        return s.add(f'<tr><td bgcolor="{CREAM}" class="pad" style="background-color:{CREAM};padding:22px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{WHITE}" style="background-color:{WHITE};border:1px solid {SAND};border-radius:10px;"><tr><td align="center" bgcolor="{WHITE}" style="background-color:{WHITE};padding:26px 20px 24px 20px;text-align:center;">'
            f'<div style="{F}font-size:11px;line-height:14px;letter-spacing:2.4px;font-weight:700;color:{GOLD};">{intro}</div>'
            f'<div class="big" style="{S}font-size:64px;line-height:66px;color:{INK};padding-top:10px;">10% off</div>'
            f'<div style="{F}font-size:16px;line-height:24px;color:#2E2E2E;padding-top:4px;">plus <b>5 free gifts</b> with every order</div>'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" style="margin:18px auto 0 auto;"><tr><td align="center" style="border:2px dashed {INK};padding:9px 26px;{F}font-size:26px;line-height:30px;letter-spacing:6px;font-weight:700;color:{INK};">{CODE}</td></tr></table>'
            f'<div style="{F}font-size:12px;line-height:18px;color:#8A847A;padding-top:10px;">Already applied when you use the button. No expiry date.</div>'
            '</td></tr></table></td></tr>\n')
    def steps(s, items):
        cells = ''.join(f'<td width="33%" valign="top" class="st" style="width:33%;padding:0 6px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{WHITE}" style="background-color:{WHITE};border:1px solid {SAND};border-radius:8px;"><tr><td align="center" bgcolor="{WHITE}" style="background-color:{WHITE};padding:16px 8px 16px 8px;text-align:center;height:118px;" valign="top">'
                        f'<div style="{S}font-size:40px;line-height:40px;color:{GOLD};">{i+1}</div><div style="{F}font-size:14px;line-height:19px;font-weight:700;color:{INK};padding-top:8px;">{t}</div><div style="{F}font-size:12px;line-height:17px;color:#6F6A62;padding-top:4px;">{d}</div></td></tr></table></td>' for i, (t, d) in enumerate(items))
        return s.add(f'<tr><td bgcolor="{CREAM}" class="padx" style="background-color:{CREAM};padding:18px 34px 0 34px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cells}</tr></table></td></tr>\n')
    def gifts(s, title='Also in the box: 5 free gifts'):
        G = [('gift-shipping.jpg', 'Free shipping', 'Every order'), ('gift-ebook.jpg', 'Plastic-free e-book', 'Included'), ('gift-mystery.jpg', 'Mystery gift', 'Included'),
             ('gift-cookbook.jpg', 'Favorites Cookbook', 'Included'), ('gift-filter.jpg', 'Chance to win a PFAS water filter', 'Weekly draw')]
        t = ''.join(f'<td width="20%" valign="top" align="center" style="width:20%;padding:8px 3px 12px 3px;"><a href="{s.U("gifts")}" style="display:block;text-decoration:none;"><img src="{urls[k]}" width="60" height="60" alt="{n}" style="display:block;width:60px;height:60px;border:0;border-radius:6px;margin:0 auto;object-fit:cover;"></a>'
                    f'<div style="{F}font-size:11px;line-height:14px;font-weight:600;color:{INK};padding-top:8px;text-align:center;">{n}</div><div style="{F}font-size:10px;line-height:13px;color:#8A847A;padding-top:2px;text-align:center;">{v}</div></td>' for k, n, v in G)
        return s.add(f'<tr><td align="center" bgcolor="{CREAM}" class="padx" style="background-color:{CREAM};padding:28px 24px 0 24px;"><div style="{S}font-size:28px;line-height:32px;color:{INK};text-align:center;padding-bottom:10px;">{title}</div>'
                     f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{WHITE}" style="background-color:{WHITE};border:1px solid {SAND};border-radius:8px;"><tr>{t}</tr></table></td></tr>\n')
    def quote(s, q, who, pad='22px 40px 0 40px'):
        return s.add(f'<tr><td bgcolor="{CREAM}" class="pad" style="background-color:{CREAM};padding:{pad};"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{WHITE}" style="background-color:{WHITE};border:1px solid {SAND};border-radius:8px;"><tr><td bgcolor="{WHITE}" style="background-color:{WHITE};padding:18px 22px;">'
                     f'<div style="{F}font-size:14px;line-height:16px;letter-spacing:2px;color:{BRICK};">&#9733;&#9733;&#9733;&#9733;&#9733;</div><div style="{S}font-size:22px;line-height:29px;color:{INK};padding-top:8px;">&ldquo;{q}&rdquo;</div>'
                     f'<div style="{F}font-size:12px;line-height:17px;color:#8A847A;padding-top:8px;">{who} &middot; Verified buyer</div></td></tr></table></td></tr>\n')
    def compare(s, rows):
        def cell(t, ok, bg):
            ic = f'<span style="color:{BRICK if ok else "#9A948B"};font-weight:700;">{"&#10003;" if ok else "&#10005;"}</span>&nbsp; '
            return f'<td width="50%" valign="middle" bgcolor="{bg}" style="width:50%;background-color:{bg};padding:12px 12px;border-top:1px solid {SAND};{F}font-size:14px;line-height:19px;color:{INK};">{ic}{t}</td>'
        r = ''.join(f'<tr>{cell(a, True, WHITE)}{cell(b, False, "#F3F0EA")}</tr>' for a, b in rows)
        head = (f'<tr><td width="50%" bgcolor="{INK}" style="width:50%;background-color:{INK};padding:12px;{F}font-size:12px;line-height:16px;letter-spacing:1.6px;font-weight:700;color:{WHITE};">SIRAAT</td>'
                f'<td width="50%" bgcolor="#E4DED3" style="width:50%;background-color:#E4DED3;padding:12px;{F}font-size:12px;line-height:16px;letter-spacing:1.6px;font-weight:700;color:{INK};">A PFAS-COATED PAN</td></tr>')
        return s.add(f'<tr><td bgcolor="{CREAM}" class="pad" style="background-color:{CREAM};padding:20px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid {SAND};border-radius:8px;border-collapse:separate;overflow:hidden;">{head}{r}</table></td></tr>\n')
    def card(s, key, alt, q, who, name, line, path, c, label):
        """Productkaart: kop is een letterlijke klantquote (eerste persoon), code in de kaart, eigen knop."""
        return s.add(f'<tr><td bgcolor="{CREAM}" class="pad" style="background-color:{CREAM};padding:20px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{WHITE}" style="background-color:{WHITE};border:1px solid {SAND};border-radius:10px;"><tr>'
            f'<td width="42%" valign="top" class="cimg" style="width:42%;padding:14px 0 14px 14px;"><a href="{s.U(c + "-img", path)}" style="display:block;text-decoration:none;"><img src="{urls[key]}" width="200" alt="{alt}" style="display:block;width:100%;max-width:200px;height:auto;border:0;border-radius:6px;"></a></td>'
            f'<td valign="top" style="padding:14px 16px 14px 14px;"><div style="{F}font-size:13px;line-height:15px;letter-spacing:2px;color:{BRICK};">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
            f'<div class="cq" style="{S}font-size:21px;line-height:26px;color:{INK};padding-top:6px;">&ldquo;{q}&rdquo;</div><div style="{F}font-size:11px;line-height:15px;color:#8A847A;padding-top:5px;">{who} &middot; Verified buyer</div>'
            f'<div style="{F}font-size:15px;line-height:20px;font-weight:700;color:{INK};padding-top:10px;"><a href="{s.U(c + "-name", path)}" style="color:{INK};text-decoration:none;">{name}</a></div>'
            f'<div style="{F}font-size:13px;line-height:19px;color:#4A4640;padding-top:3px;">{line}</div>'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin-top:10px;"><tr><td style="border:1px dashed {INK};padding:4px 10px;{F}font-size:11px;line-height:14px;letter-spacing:1.6px;font-weight:700;color:{INK};">CODE {CODE} &middot; 10% OFF</td></tr></table>'
            f'<div style="padding-top:12px;"><a href="{s.U(c, path)}" style="{F}font-size:14px;line-height:18px;font-weight:700;color:{BRICK};text-decoration:underline;">{label} &rarr;</a></div></td></tr></table></td></tr>\n')
    def sign(s, ps=None):
        s.p('Benjamin', '22px 40px 0 40px', w=700, col=INK)
        s.p('Founder, Siraat', '2px 40px 0 40px', size=14, col='#8A847A')
        if ps: s.p(ps, '16px 40px 0 40px', size=15, col=GREY)
        return s.add(f'<tr><td bgcolor="{CREAM}" style="background-color:{CREAM};padding:0 0 30px 0;font-size:0;line-height:0;">&nbsp;</td></tr>\n')

# ---------- header en footer uit de vaste partials (CLAUDE.md: elke mail met vaste header en footer)
hdr = open(os.path.join(P, 'header.html')).read()
ftr = open(os.path.join(P, 'footer.html')).read()
for k, v in urls.items():
    hdr = hdr.replace('{{SHARED}}/' + k, v)
    ftr = ftr.replace('{{SHARED}}/' + k, v).replace('{{IMG}}/' + k, v)
hdr = re.sub(r'<!--.*?-->\n?', '', hdr, flags=re.S); ftr = re.sub(r'<!--.*?-->\n?', '', ftr, flags=re.S)
assert '{{SHARED}}' not in hdr + ftr and '{{IMG}}' not in hdr + ftr
def utm_nav(h, tag, mid):
    return re.sub(r'href="(https://(?:www\.)?siraatskitchen\.com[^"?]*)"', lambda m: f'href="{m.group(1)}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={mid}-{tag}-{(m.group(1).rstrip("/").split("/")[-1] or "home").replace(".com", "home")}"', h)

HEAD = '''<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>__TITLE__</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>
  @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&family=Inter:wght@400;500;600;700&display=swap');
  body{margin:0;padding:0;background:#FFFFFF;-webkit-text-size-adjust:100%;}
  table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}
  img{border:0;display:block;line-height:100%;outline:none;text-decoration:none;}
  a{color:#AC3B19;}
  @media only screen and (max-width:620px){
    .w{width:100%!important;}
    .pad{padding-left:22px!important;padding-right:22px!important;}
    .padx{padding-left:14px!important;padding-right:14px!important;}
    .h2{font-size:32px!important;line-height:36px!important;}
    .big{font-size:54px!important;line-height:58px!important;}
    .navhide{display:none!important;}
    .lead{font-size:16px!important;line-height:25px!important;}
    .st{padding:0 3px!important;}
    .cq{font-size:18px!important;line-height:23px!important;}
    .cimg{width:36%!important;}
  }
</style>
</head>
'''

def page(m, title, preview):
    head = HEAD.replace('__TITLE__', title)
    body = m.b.replace('{{HEADER}}', utm_nav(hdr, 'nav', m.mid)).replace('{{FOOTER}}', utm_nav(ftr, 'ft', m.mid))
    html = (head + '<body style="margin:0;padding:0;background:#FFFFFF;">\n'
            f'<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;">{preview}' + '&#847;&zwnj;&nbsp;' * 60 + '</div>\n'
            '<table bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;" width="100%">\n<tr><td align="center" style="padding:8px 0 32px 0;">\n'
            f'<table bgcolor="{CREAM}" border="0" cellpadding="0" cellspacing="0" class="w" role="presentation" style="width:100%;max-width:600px;background-color:{CREAM};" width="600">\n'
            + body + '</table>\n</td></tr>\n</table>\n</body>\n</html>\n')
    assert '—' not in html, m.mid + ': em dash'
    assert '{{SHARED}}' not in html and '{{IMG}}' not in html and '{{HEADER}}' not in html
    open(os.path.join(ROOT, m.mid + '.html'), 'w').write(html)
    prev = (html.replace("{{ first_name|default:'there' }}", 'Sarah').replace('{{ organization.name }}', "Siraat's Kitchen")
                .replace('{{ organization.full_address }}', '(address)'))
    prev = re.sub(r'\{%.*?%\}', '#', prev); prev = re.sub(r'\{\{.*?\}\}', '', prev)
    open(os.path.join(ROOT, m.mid + '-preview.html'), 'w').write(prev)
    words = len(re.sub(r'<[^>]+>', ' ', body.split('{{FOOTER}}')[0]).split())
    print(m.mid, 'ok', len(html), 'bytes')

HI = "Hi {{ first_name|default:'there' }},"

# =====================================================================================================
# E1 · The sealed envelope arrives (5 min na inschrijving). Rol: geld (vervangt W1), code boven de vouw, cartlink.
e = Mail('e1')
e.codebar('Your welcome envelope &middot; 10% off with HI10 &middot; 5 free gifts').add('{{HEADER}}\n')
e.img('v6e-m1-hero.jpg', 'A cream envelope closed with a gold Siraat seal, a line of gold sand leading to it. Inside: 10% off with HI10 and 5 free gifts.', 'hero')
e.eyebrow('YOUR WELCOME ENVELOPE', 'Here is what&rsquo;s inside.', '30px 40px 0 40px')
e.reveal('OPENED FOR YOU, SAME AS FOR EVERYONE WHO JOINS')
e.btn('Claim my 10% + gifts', 'cta1')
e.p(f'Already something in your cart? <a href="{e.U("cart", "/cart")}" style="color:{BRICK};font-weight:700;">Apply my 10% to my cart &rarr;</a>', '12px 40px 0 40px', size=15, al='center')
e.eyebrow('HOW IT WORKS', 'Three steps.', '36px 40px 0 40px')
e.steps([('Pick your pan or set', 'Start with the one you cook with most.'), ('Your 10% is applied', 'The button adds HI10. Or type it at checkout.'), ('The gifts ship with it', '5 free gifts go in the same box.')])
e.gifts()
e.sandline()
e.p(HI, '26px 40px 0 40px')
e.p('Benjamin here, I started Siraat. A quick word about the envelope, because I know how these usually go.', '10px 40px 0 40px')
e.p('There is no lottery in it and no secret amount. Everyone who joins gets the same thing: 10% off and 5 free gifts. The code does not expire, so there is no clock on it either.', '12px 40px 0 40px')
e.p(f'What I do want you to know before you pick: our pans have a pure titanium cooking surface with no coatings, so there is nothing on it to wear off. Light Labs tested that surface for 31 PFAS compounds and every one came back below the detection limit. <a href="{e.plain("report", REPORT)}" style="color:{BRICK};">Report no. 25895, read it yourself &rarr;</a>', '12px 40px 0 40px')
e.btn('Claim my 10% + gifts', 'cta2', pad='22px 40px 0 40px')
e.sign('P.S. Tomorrow I will tell you what the seal on the envelope says. It is our name, and it is a word with a meaning.')
e.add('{{FOOTER}}\n')
page(e, 'Your welcome envelope', 'Open it: 10% off with HI10, plus 5 free gifts with every order. Same for everyone, no expiry.')

# =====================================================================================================
# E2 · What's inside: the path and the name (+1 dag 10:00). Rol: merkverhaal, aanbod in de P.S.
e = Mail('e2')
e.codebar('Your envelope &middot; 10% off with HI10 &middot; 5 free gifts').add('{{HEADER}}\n')
e.img('v6e-m2-hero.jpg', 'An opened cream envelope with the gold seal, a card inside that reads Your first step', 'hero')
e.eyebrow('THE SECOND THING IN YOUR ENVELOPE', 'Your first step.', '30px 40px 0 40px')
e.p(HI, '18px 40px 0 40px')
e.p('Yesterday&rsquo;s envelope held your welcome gift. Today, the story behind the seal.', '10px 40px 0 40px')
e.p('<b>Siraat is named after sirat, the Arabic word for path.</b> Our promise is in the name: the path to a non-toxic life.', '12px 40px 0 40px')
e.p('A path is not a leap. Nobody throws out a whole kitchen in one weekend. You start with the pan you use most, and the next step comes when you are ready.', '12px 40px 0 40px')
e.img('v6e-m2-path.jpg', 'A line of gold sand winding across a sandstone surface to the Siraat seal', 'path', pad='26px 0 0 0')
e.eyebrow('THE MARK ON THE SEAL', 'Six letters in one square.', '30px 40px 0 40px')
e.p('Look at the square in our logo at the top of this email. It spells S, I, R, A, A, T in Latin letters, drawn in the style of square Kufic: only straight lines and right angles, like bricks set into a wall.', '14px 40px 0 40px')
e.p('The gold line you keep seeing is the path, made of sand. Every grain is one small choice: one pan, one swap, one habit.', '12px 40px 0 40px')
e.sandline()
e.eyebrow('WHERE OUR PATH STARTED', 'Before the pan, a cutting board.', '26px 40px 0 40px')
e.p('We started with titanium cutting boards. Then we made the pan nobody else was making: the original hammered titanium pan, with a pure titanium cooking surface and no coatings. The first orders shipped on December 20, 2024. Look-alikes came after.', '14px 40px 0 40px')
e.p('Since then, more than 100,000 people have taken that first step with us.', '12px 40px 0 40px')
e.btn('Start with one pan, 10% off', 'cta1', H_PAN)
e.sign('P.S. Your envelope is still open on our side: HI10 takes 10% off, and the 5 free gifts ship with every order. No expiry date.')
e.add('{{FOOTER}}\n')
page(e, 'From sirat, the Arabic word for path', 'The second thing in your envelope: what our name means. (Your 10% is in the P.S.)')

# =====================================================================================================
# E3 · The proof (+2 dagen 09:00). Rol: autoriteit, rapport 25895, vergelijking met een PFAS-pan.
e = Mail('e3')
e.codebar('Your envelope &middot; 10% off with HI10 &middot; 5 free gifts').add('{{HEADER}}\n')
e.img('v6e-m3-hero.jpg', 'A black envelope sealed with the gold Siraat seal', 'hero', H_PAN)
e.eyebrow('WHAT WE PUT IN WRITING', 'Don&rsquo;t take the label&rsquo;s word for it.', '30px 40px 0 40px')
e.p(HI, '18px 40px 0 40px')
e.p('Every pan on the shelf says non-toxic. Few can hand you the paper. So here is ours, and three things you can check before you spend a dollar.', '10px 40px 0 40px')
for n, (t, d) in enumerate([
        ('The lab report.', f'Light Labs, an ISO/IEC 17025-accredited lab, tested our cooking surface for 31 PFAS compounds. Every one came back below the detection limit. <a href="{e.plain("report", REPORT)}" style="color:{BRICK};">Report no. 25895 &rarr;</a>'),
        ('The surface.', 'A pure titanium cooking surface, no coatings. No PFAS, PFOA, or BPA. There is nothing on it to peel, flake or wear off.'),
        ('The warranty.', 'Because there is no coating to wear out, every pan is covered for 75 years against defects. And unused pans can go back within 30 days.')]):
    e.add(f'<tr><td bgcolor="{CREAM}" class="pad" style="background-color:{CREAM};padding:16px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {SAND};"><tr>'
          f'<td width="48" valign="top" style="width:48px;padding:16px 0 0 0;"><div style="{S}font-size:42px;line-height:42px;color:{GOLD};">{n+1}</div></td>'
          f'<td valign="top" style="padding:16px 0 0 0;"><div style="{F}font-size:17px;line-height:23px;font-weight:700;color:{INK};">{t}</div><div style="{F}font-size:15px;line-height:23px;color:#2E2E2E;padding-top:4px;">{d}</div></td></tr></table></td></tr>\n')
e.eyebrow('SIDE BY SIDE', 'Siraat or a PFAS-coated pan', '34px 40px 0 40px')
e.compare([('Pure titanium surface', 'A coating on top'), ('No coating to wear off', 'Coating wears with use'), ('Metal utensils welcome', 'Wood or silicone advised'), ('Dishwasher safe', 'Hand wash advised')])
e.p('One honest thing: no coating cooks a little differently. Heat it on medium for 2 to 3 minutes, add a teaspoon of oil, and the egg lets go. Skip the heat, and it sticks.', '18px 40px 0 40px', size=15, col=GREY)
e.quote('The real test was my egg the next morning... the egg released completely and slid around the pan like it was non-stick.', 'Michael G., Pan Pro')
e.btn('Get 10% off the tested pan', 'cta1', H_PAN)
e.sign('P.S. HI10 still takes 10% off, the 5 free gifts still ship with every order. Same envelope, no expiry.')
e.add('{{FOOTER}}\n')
page(e, 'Report no. 25895', '31 PFAS compounds tested. Every one below the detection limit. Read it yourself.')

# =====================================================================================================
# E4 · Still sealed? (+3 dagen 09:00). Rol: productkaarten met quote-kop en code op elke kaart. Geen deadline.
e = Mail('e4')
e.codebar('Still unopened &middot; 10% off with HI10 &middot; 5 free gifts').add('{{HEADER}}\n')
e.img('v6e-m4-hero.jpg', 'A sealed Siraat envelope leaning on a kitchen counter next to a bowl of lemons', 'hero')
e.eyebrow('YOUR ENVELOPE', 'Still sealed?', '30px 40px 0 40px')
e.p(HI, '18px 40px 0 40px')
e.p('Your 10% has not been used yet. That is fine, there is no clock on it. If you are still choosing, here is where most people start, in the words of the people who did.', '10px 40px 0 40px')
e.card('pc-standard.jpg', 'Titanium Hammered Pan Pro Standard, 11 inch', 'We cooked the best omelette we have ever eaten when we used the pan for the first time.', 'Graham C.',
       'Titanium Hammered Pan Pro Standard', 'The pan Siraat started with. 11&Prime;, the size most people pick first.', H_PAN, 'card-pan', 'Get 10% off this pan')
e.card('pc-set6.jpg', 'Titanium Hammered Pan Set With Lids, 6 pieces', '...I thought it was just marketing hype... I ended up buying the whole collection.', 'Fatima',
       'Pan Set With Lids, 6 pieces', 'Three pans, three lids. The everyday kitchen in one step.', H_SET6, 'card-set6', 'Get 10% off the set')
e.card('pc-wok.jpg', 'Titanium Hammered Wok Pan Pro', '...I honestly thought this might be another scam. But it&rsquo;s real titanium.', 'James',
       'Titanium Hammered Wok Pan Pro', 'Deep sides for stir-fry, sauces and anything that tosses.', H_WOK, 'card-wok', 'Get 10% off the wok')
e.btn('Open my envelope', 'cta1', pad='28px 40px 0 40px')
e.gifts('With any of them: 5 free gifts')
e.sign('P.S. Not sure which size? Reply and tell me who you cook for. Our team will help you pick.')
e.add('{{FOOTER}}\n')
page(e, 'Still sealed?', 'Your 10% is still unused. Three places people start, in their own words.')

# =====================================================================================================
# E5 · A plain letter from Benjamin (+4 dagen 09:00). Rol: laatste mail, liking + volledige risk reversal. Header en footer blijven (CLAUDE.md).
e = Mail('e5')
e.add('{{HEADER}}\n')
e.p(HI, '34px 40px 0 40px')
e.p('This is my last note about the envelope.', '14px 40px 0 40px')
e.p('I did not send it to rush you. A path only works at your own pace, and the pan will be here when you are ready. Your code HI10 has no end date. It takes 10% off once, and the 5 free gifts ship with every order.', '14px 40px 0 40px')
e.p('If something is holding you back, it is usually one of two worries. So here are two promises:', '14px 40px 0 40px')
e.p('<b>If you change your mind.</b> Send it back unused within 30 days of delivery for a full refund.', '12px 40px 0 60px')
e.p('<b>If something is wrong.</b> Damaged or defective in the first 30 days? We refund or replace it, and we pay the shipping. After that, the 75-year warranty covers defects: a dent, a warped base, a loose handle or rivet.', '12px 40px 0 60px')
e.p(f'If you want to start small, <a href="{e.U("letter-pan", H_PAN)}" style="color:{BRICK};text-decoration:underline;">this is the pan I would start with</a>. If you cook for more people, <a href="{e.U("letter-set", H_SET6)}" style="color:{BRICK};text-decoration:underline;">the 6-piece set</a> does the whole stove in one step. Your 10% is already in both links.', '14px 40px 0 40px')
e.p('And if you are not sure yet, reply and tell me what you cook most. Our team will help.', '14px 40px 0 40px')
e.p('Thank you for opening it with us.', '14px 40px 0 40px')
e.sign()
e.add('{{FOOTER}}\n')
page(e, 'Last note about the envelope', 'No clock on it. Just two promises, and the pan I would start with.')
