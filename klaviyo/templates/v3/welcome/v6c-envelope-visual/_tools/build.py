"""Welcome v6c 'Sealed envelope, visual DR' (concept, 17 nov 2026). NIET LIVE.
Copy, aanbod, prijzen en links uit v6b; ontworpen beeldsecties uit _tools/sections.py (Klaviyo-URL's in klaviyo-urls.txt).
Live HTML blijft: preheader, codebalk, header, regel onder de hero, codebox, hoofdknoppen, ondertekening, footer.
Gebruik: python3 -I _tools/build.py   Spec: klaviyo/flows/welcome-v6c-envelope-visual.md
"""
import re, os
from urllib.parse import quote
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../../..'))
P = os.path.join(REPO, 'klaviyo/templates/partials')
def load(p): return dict(l.split() for l in open(p) if len(l.split()) == 2)
urls = load(os.path.join(P, 'shared/klaviyo-urls.txt'))
urls.update(load(os.path.join(REPO, 'klaviyo/templates/v3/campaigns/thanksgiving-roast-1117/assets/klaviyo-urls.txt')))
S = load(os.path.join(ROOT, 'klaviyo-urls.txt'))  # secties

CAMP, CODE = 'v6c-welcome-visual', 'HI10'
GIFTS = '5 free gifts with every order'  # [VRAAG FLORIS] na BF
REPORT = 'https://siraatskitchen.com/pages/third-party-testing'
H = {'standard': 'original-siraat-100-pure-titanium-pan-with-hammered-pattern', 'mini': 'titanium-hammered-pan-pro-mini', 'small': 'titanium-hammered-pan-pro-small',
     'large': 'titanium-hammered-pan-pro-large', 'set6': 'titanium-hammered-pan-set-with-lids-6-pcs', 'set12': 'titanium-hammered-cookware-set',
     'duo': '2-pans-and-2-lids', 'roast': 'titanium-hammered-roasting-pan', 'lid': 'stainless-steel-lid'}
NAME = {'standard': 'Titanium Hammered Pan Pro Standard 11 inch, $144, $129.60 with HI10', 'mini': 'Pan Pro Mini 8 inch, $129, $116.10 with HI10',
        'small': 'Pan Pro Small 10 inch, $137, $123.30 with HI10', 'large': 'Pan Pro Large 12 inch, $149, $134.10 with HI10',
        'set6': '6-Piece Set, Mini, Small and Large with 3 lids, $299, $269.10 with HI10', 'set12': '12-Piece Set, 3 pans, 3 pots and 6 lids, $649, $584.10 with HI10',
        'duo': '2 Pans + 2 Lids, $199, $179.10 with HI10', 'roast': 'Titanium Hammered Roasting Pan with V-rack, $199, $179.10 with HI10'}
F = "font-family:Inter,Arial,Helvetica,sans-serif;"
INK, BRICK, CREAM, SAND, DARK, ORANGE, GOLD, W = '#272727', '#AC3B19', '#F8F7F2', '#ECE7DD', '#282828', '#C4642C', '#B8862B', '#FFFFFF'
FR = 'Free shipping. 30-day returns. 100,000+ happy customers.'

class Mail:
    def __init__(s, mid): s.mid, s.b, s.imgs = mid, '', []
    def U(s, c, path='/collections/all'):
        return f'https://siraatskitchen.com/discount/{CODE}?redirect=' + quote(f'{path}?utm_source=klaviyo&utm_medium=email&utm_campaign={CAMP}&utm_content={s.mid}-{c}', safe='')
    def UP(s, c, k): return s.U(c, '/products/' + H[k])
    def add(s, h): s.b += h; return s
    def img(s, key, alt, href, w=600):
        s.imgs.append(key)
        return s.add(f'<tr><td style="padding:0;font-size:0;line-height:0;"><a href="{href}" style="display:block;border:0;"><img src="{S[key + ".jpg"]}" width="{w}" alt="{alt}" style="display:block;width:100%;max-width:{w}px;height:auto;border:0;"></a></td></tr>\n')
    def torn(s, a, b): return s.img(f'torn-{a[1:]}-{b[1:]}', '', s.U('edge'))
    def codebar(s, t):
        return s.add(f'<tr><td align="center" bgcolor="{INK}" style="background-color:{INK};padding:11px 16px;{F}font-size:11px;line-height:15px;letter-spacing:1.6px;font-weight:700;color:{CREAM};text-transform:uppercase;"><a href="{s.U("codebar")}" style="color:{CREAM};text-decoration:none;">{t}</a></td></tr>\n')
    def live(s, bg, inner, pad='22px 40px 26px 40px'):
        return s.add(f'<tr><td align="center" bgcolor="{bg}" class="pad" style="background-color:{bg};padding:{pad};text-align:center;">{inner}</td></tr>\n')
    def btn(s, label, href, bg, dark):
        bb, fc = (W, INK) if dark else (BRICK, W)
        return (f'<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="440" style="width:100%;max-width:440px;margin:0 auto;"><tr><td align="center" bgcolor="{bb}" style="background-color:{bb};border-radius:40px;">'
                f'<a href="{href}" style="display:block;padding:21px 16px;{F}font-size:17px;line-height:20px;font-weight:800;letter-spacing:0.8px;color:{fc};text-decoration:none;text-transform:uppercase;">{label} &rarr;</a></td></tr></table>')
    def offer(s, bg, line, label, href, dark=False, extra=''):
        """Live: korte regel onder de hero, codebox (gestippeld), grote knop, friction reducer."""
        tc, sc, box = (W, '#CFC8BC', '#353332') if dark else (INK, '#727272', W)
        bd = '#E7C988' if dark else INK
        inner = (f'<div class="lead" style="{F}font-size:17px;line-height:25px;color:{tc};">{line}</div>'
                 f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" style="margin:16px auto 0 auto;"><tr><td align="center" bgcolor="{box}" style="background-color:{box};border:3px dashed {bd};border-radius:10px;padding:10px 34px;">'
                 f'<div style="{F}font-size:11px;line-height:14px;letter-spacing:2.4px;font-weight:800;color:{GOLD};">YOUR WELCOME CODE</div><div style="{F}font-size:34px;line-height:40px;letter-spacing:8px;font-weight:900;color:{tc};">{CODE}</div></td></tr></table>'
                 f'<div style="padding-top:16px;">{s.btn(label, href, bg, dark)}</div><div style="{F}font-size:12px;line-height:18px;color:{sc};padding-top:10px;">{FR}</div>{extra}')
        return s.live(bg, inner)
    def cta(s, bg, label, href, dark=False, sub=None, pad='6px 40px 34px 40px'):
        sc = '#E9CBB9' if bg in (BRICK, ORANGE) else ('#CFC8BC' if dark else '#727272')
        return s.live(bg, s.btn(label, href, bg, dark) + (f'<div style="{F}font-size:12px;line-height:18px;color:{sc};padding-top:10px;">{sub}</div>' if sub else ''), pad)
    def cards(s, rows):
        """Productkaarten als beelden, 2 per rij op zandpaneel, elk met eigen link (code toegepast)."""
        for r in rows:
            cells = ''.join(f'<td width="50%" valign="top" style="width:50%;padding:0;font-size:0;line-height:0;"><a href="{s.UP("card-" + k, k)}" style="display:block;"><img src="{S[pre + k + ".jpg"]}" width="300" alt="{NAME[k]}" style="display:block;width:100%;max-width:300px;height:auto;border:0;"></a></td>' for pre, k in r)
            for pre, k in r: s.imgs.append(pre + k)
            s.add(f'<tr><td bgcolor="{SAND}" style="background-color:{SAND};padding:0 0 0 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cells}</tr></table></td></tr>\n')
        return s
    def sign(s, bg=CREAM, ps=None):
        t = f'<div style="{F}font-size:16px;line-height:24px;color:{INK};text-align:left;"><b>Benjamin</b><br><span style="color:#8A847A;font-size:14px;">Founder, Siraat</span></div>'
        if ps: t += f'<div style="{F}font-size:14px;line-height:21px;color:#5E5A54;text-align:left;padding-top:10px;">{ps}</div>'
        return s.live(bg, t, '18px 40px 30px 40px')


RV = {'tammy': ('I am on my 4th pan from Siraat... I even gifted one to my son, and he says it&rsquo;s the best pan he owns.', 'Tammy, Pan Pro'),
      'sunny': ('I ordered one pan to try it out. I&rsquo;m so glad I did. I am so happy with this pan that I&rsquo;m ordering the set.', 'Sunny C.'),
      'michael': ('The real test was my egg the next morning... the egg released completely and slid around the pan like it was non-stick.', 'Michael G., Pan Pro'),
      'thomas': ('This pan is fantastic. Makes all of our others &ldquo;non stick&rdquo; seem really sticky.', 'Thomas D., Pan Pro'),
      'carole': ('I&rsquo;ve been cooking for well over 60 years... This Siraat pan has been the absolute best I&rsquo;ve ever used.', 'Carole, Pan Pro'),
      'graham': ('We cooked the best omelette we have ever eaten when we used the pan for the first time.', 'Graham C., Pan Pro'),
      'fatima': ('...I thought it was just marketing hype... I ended up buying the whole collection.', 'Fatima, Set'),
      'brandon': ('Siraat replaced a pan free of charge... I just sent them the picture and they honored the warranty.', 'Brandon W., Pan Pro')}
def reviews(m, keys, title, bg=CREAM, dark=False):
    """Reviews als live tekst (toegankelijk, telt als live aandeel), letterlijk uit content/reviews/reviews.csv."""
    cb, qc, st = ('#353332', W, '#E7C988') if dark else (W, INK, BRICK)
    cards = ''.join(f'<tr><td style="padding:0 0 12px 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{cb}" style="background-color:{cb};border-radius:14px;"><tr><td bgcolor="{cb}" style="background-color:{cb};padding:16px 20px;text-align:left;border-radius:14px;">'
                    f'<div style="{F}font-size:15px;line-height:16px;letter-spacing:3px;color:{st};">&#9733;&#9733;&#9733;&#9733;&#9733;</div><div style="{F}font-size:16px;line-height:23px;font-weight:600;color:{qc};padding-top:6px;">&ldquo;{RV[k][0]}&rdquo;</div>'
                    f'<div style="{F}font-size:12px;line-height:16px;color:#8A847A;padding-top:6px;">{RV[k][1]} &middot; Verified buyer</div></td></tr></table></td></tr>' for k in keys)
    return m.live(bg, f'<div style="{F}font-size:24px;line-height:26px;letter-spacing:5px;color:{st};">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
                  f'<div style="font-family:\'Instrument Serif\',\'Times New Roman\',serif;font-style:italic;font-size:34px;line-height:38px;color:{qc if dark else INK};padding:4px 0 14px 0;">{title}</div>'
                  f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{cards}</table>', '26px 30px 10px 30px')

hdr = open(os.path.join(P, 'header.html')).read(); ftr = open(os.path.join(P, 'footer.html')).read()
for k, v in urls.items():
    hdr = hdr.replace('{{SHARED}}/' + k, v); ftr = ftr.replace('{{SHARED}}/' + k, v).replace('{{IMG}}/' + k, v)
hdr = re.sub(r'<!--.*?-->\n?', '', hdr, flags=re.S); ftr = re.sub(r'<!--.*?-->\n?', '', ftr, flags=re.S)
def utm_nav(h, tag, mid):
    return re.sub(r'href="(https://(?:www\.)?siraatskitchen\.com[^"?]*)"', lambda m: f'href="{m.group(1)}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={mid}-{tag}-{(m.group(1).rstrip("/").split("/")[-1] or "home").replace(".com", "home")}"', h)
HEAD = open(os.path.join(ROOT, '../v6-envelope/e1.html')).read().split('<body')[0]

REPORT_SIZES = {}
def page(m, title, preview):
    head = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', HEAD)
    body = m.b.replace('{{HEADER}}', utm_nav(hdr, 'nav', m.mid)).replace('{{FOOTER}}', utm_nav(ftr, 'ft', m.mid))
    html = (head + '<body style="margin:0;padding:0;background:#FFFFFF;">\n'
            f'<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;">{preview}' + '&#847;&zwnj;&nbsp;' * 60 + '</div>\n'
            '<table bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;" width="100%">\n<tr><td align="center" style="padding:8px 0 32px 0;">\n'
            f'<table bgcolor="{CREAM}" border="0" cellpadding="0" cellspacing="0" class="w" role="presentation" style="width:100%;max-width:600px;background-color:{CREAM};" width="600">\n'
            + body + '</table>\n</td></tr>\n</table>\n</body>\n</html>\n')
    assert '—' not in html, m.mid
    assert '{{SHARED}}' not in html and '{{IMG}}' not in html
    open(os.path.join(ROOT, m.mid + '.html'), 'w').write(html)
    prev = html.replace("{{ first_name|default:'there' }}", 'Sarah').replace('{{ organization.name }}', "Siraat's Kitchen").replace('{{ organization.full_address }}', '(address)')
    prev = re.sub(r'\{%.*?%\}', '#', prev); prev = re.sub(r'\{\{.*?\}\}', '', prev)
    open(os.path.join(ROOT, m.mid + '-preview.html'), 'w').write(prev)
    kb = sum(os.path.getsize(os.path.join(ROOT, 'sections', k + '.jpg')) for k in m.imgs) // 1024
    REPORT_SIZES[m.mid] = (len(html) // 1024, kb)
    print(m.mid, 'html', len(html) // 1024, 'KB, section images', len(m.imgs), kb, 'KB')

# ======================= E1 · offer + bestsellers + bundel
e = Mail('e1')
e.codebar(f'Welcome &middot; 10% off with HI10 &middot; {GIFTS}').add('{{HEADER}}\n')
e.img('e1-hero', 'Your welcome envelope is open. Take 10% off your first pan. Code HI10 works on everything, sets included. 10% off plus 5 free gifts.', e.U('hero'))
e.offer(CREAM, f'<b>HI10 takes 10% off everything</b>, sets included. Plus {GIFTS}.', 'Claim my 10% + gifts', e.U('cta1'),
        extra=f'<div style="{F}font-size:14px;line-height:20px;color:{INK};padding-top:10px;">Already something in your cart? <a href="{e.U("cart", "/cart")}" style="color:{BRICK};font-weight:800;">Apply my 10% to my cart &rarr;</a></div>')
e.torn(CREAM, DARK)
e.img('e1-steps', 'How it works, three steps. 1: pick your pan or set. 2: HI10 is applied by the button, or type it at checkout. 3: the 5 free gifts ship in the same box.', e.U('steps'))
e.torn(DARK, SAND)
e.img('h-bestsellers', 'Start here: our bestsellers, with your 10%', e.U('h-best'))
e.cards([[('card-', 'standard'), ('card-', 'set6')], [('card-', 'duo'), ('card-', 'roast')]])
e.torn(SAND, BRICK)
e.img('e1-bundle', 'Most people pick the 6-piece set. $293 saved: Mini $129, Small $137, Large $149 and 3 lids $177 cost $592 one by one, the set is $299. With HI10 $269.10, about $90 a pan, lid included.', e.UP('bundle', 'set6'))
e.cta(BRICK, 'Get the set for $269.10', e.UP('bundle-cta', 'set6'), dark=True, sub='One use of HI10, applied by the button. 30-day returns.')
e.torn(BRICK, CREAM)
reviews(e, ['tammy', 'sunny'], '100,000+ happy customers')
e.cta(CREAM, 'Claim my 10% + gifts', e.U('cta2'), sub=FR, pad='4px 40px 10px 40px')
e.live(CREAM, f'<div style="{F}font-size:13px;line-height:19px;color:#5E5A54;">Pure titanium cooking surface, no coatings. Tested for 31 PFAS by Light Labs. <a href="{REPORT}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content=e1-report" style="color:{BRICK};">Report no. 25895 &rarr;</a></div>', '6px 40px 0 40px')
e.sign()
e.add('{{FOOTER}}\n')
page(e, 'Your 10% is inside', f'HI10 takes 10% off everything, sets included. Plus {GIFTS}.')

# ======================= E2 · verhaal kort, maatkiezer, value stack
e = Mail('e2')
e.codebar(f'10% off with HI10 &middot; {GIFTS}').add('{{HEADER}}\n')
e.img('e2-hero', 'The pan nobody else was making. The original hammered pan. First orders shipped December 20, 2024. Look-alikes came after.', e.UP('hero', 'standard'))
e.offer(DARK, '<b>Yours is 10% off</b>, on every size and set.', 'Get 10% off the original', e.UP('cta1', 'standard'), dark=True)
e.torn(DARK, CREAM)
e.img('e2-story', 'Siraat: from sirat, the Arabic word for path. The path to a non-toxic life, one step at a time. We started with titanium cutting boards, then made the pan with a pure titanium cooking surface and no coatings. Nothing on it to wear off, covered for 75 years.', e.UP('story', 'standard'))
e.torn(CREAM, SAND)
e.img('h-sizes', 'Size chooser: which size is yours?', e.UP('h-sizes', 'standard'))
e.cards([[('size-', 'mini'), ('size-', 'small')], [('size-', 'standard'), ('size-', 'large')]])
e.cta(SAND, 'Get 10% off my size', e.UP('sizes-cta', 'standard'), sub='Same titanium surface on every size.', pad='16px 40px 30px 40px')
e.torn(SAND, DARK)
e.img('e2-stack', 'Everything you get: Pan Pro Standard 11 inch $144, 5 free gifts worth $555, 75-year warranty and 30-day returns included. Your price $129.60 with HI10.', e.UP('stack', 'standard'))
e.cta(DARK, 'Get my pan for $129.60', e.UP('stack-cta', 'standard'), dark=True, sub=FR)
e.torn(DARK, CREAM)
reviews(e, ['carole', 'graham'], '100,000+ happy customers')
e.sign(ps='P.S. HI10 has no end date. One use, 10% off everything.')
e.add('{{FOOTER}}\n')
page(e, 'The pan nobody else was making', 'First orders shipped December 20, 2024. Pick your size, 10% off with HI10.')

# ======================= E3 · bewijs + tabel + bundel
e = Mail('e3')
e.codebar(f'10% off with HI10 &middot; {GIFTS}').add('{{HEADER}}\n')
e.img('e3-hero', 'Report no. 25895. Tested for 31 PFAS. Every one below the detection limit. Read the paper, not the label.', e.UP('hero', 'standard'))
e.offer(DARK, '<b>Every pan says non-toxic. We show the paper.</b> Your 10% is still here.', 'Get 10% off the tested pan', e.UP('cta1', 'standard'), dark=True)
e.torn(DARK, CREAM)
e.img('e3-stats', '31 PFAS compounds tested, 0 above the detection limit, 75-year warranty. Light Labs, ISO/IEC 17025-accredited, report no. 25895.', f'{REPORT}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content=e3-stats')
e.torn(CREAM, SAND)
e.img('e3-compare', 'Siraat vs a PFAS-coated pan: pure titanium surface vs a coating on top; no coating to wear off vs coating wears with use; metal utensils welcome vs wood or silicone advised; dishwasher safe vs hand wash advised; lab report 25895 vs testing varies by brand.', e.UP('compare', 'standard'))
e.torn(SAND, DARK)
reviews(e, ['michael', 'thomas'], 'The egg test', bg=DARK, dark=True)
e.torn(DARK, SAND)
e.img('h-tested', 'Start with one pan', e.UP('h-tested', 'standard'))
e.cards([[('card-', 'standard'), ('card-', 'large')]])
e.live(SAND, '', '10px 0 0 0')
e.torn(SAND, BRICK)
e.img('e3-bundle', 'Or the whole stove: 3 pans and 3 lids. $293 saved versus $592 one by one. The set is $299, $269.10 with HI10.', e.UP('bundle', 'set6'))
e.cta(BRICK, 'Get the set for $269.10', e.UP('bundle-cta', 'set6'), dark=True, sub='Same titanium cooking surface on every pan in the set.')
e.torn(BRICK, CREAM)
e.sign()
e.add('{{FOOTER}}\n')
page(e, 'Report no. 25895', '31 PFAS compounds tested, every one below detection. Your 10% is still here.')

# ======================= E4 · still sealed + top + bezwaren
e = Mail('e4')
e.codebar(f'Still unused &middot; 10% off with HI10 &middot; {GIFTS}').add('{{HEADER}}\n')
e.img('e4-hero', 'Your envelope: still sealed? Your 10% hasn&rsquo;t been used yet.', e.U('hero'))
e.offer(DARK, f'<b>HI10 takes 10% off everything.</b> No end date. Plus {GIFTS}.', 'Use my 10% now', e.U('cta1'), dark=True)
e.torn(DARK, SAND)
e.img('h-start', 'Most picked: where most people start', e.U('h-start'))
e.cards([[('card-', 'standard'), ('card-', 'set6')], [('card-', 'set12'), ('card-', 'large')]])
e.live(SAND, f'<div style="{F}font-size:12px;line-height:17px;color:#8A847A;">12-piece set: 3 pans, 2-qt and 3-qt saucepans, an 8-qt stockpot, a lid for each. US only.</div>', '10px 40px 24px 40px')
e.torn(SAND, DARK)
e.img('e4-objections', 'Quick answers. Will food stick? Not when the pan is hot: medium heat 2 to 3 minutes and a teaspoon of oil. Induction? Yes, also gas, electric and ceramic. Don&rsquo;t like it? 30-day returns, unused, full refund.', e.U('objections'))
e.torn(DARK, ORANGE)
e.img('e4-complete', 'Complete the set: 3 pans and 3 lids instead of one pan. $293 saved versus one by one. $299, or $269.10 with HI10.', e.UP('complete', 'set6'))
e.cta(ORANGE, 'Upgrade to the 6-piece set', e.UP('complete-cta', 'set6'), dark=True, sub='One use of HI10, applied by the button.')
e.torn(ORANGE, CREAM)
reviews(e, ['fatima', 'brandon'], 'In their words')
e.cta(CREAM, 'Use my 10% now', e.U('cta2'), sub=FR, pad='4px 40px 10px 40px')
e.sign()
e.add('{{FOOTER}}\n')
page(e, 'Still sealed', f'Your 10% is unused. Where most people start, with your price, plus {GIFTS}.')

# ======================= E5 · korte brief + harde recap
e = Mail('e5')
e.add('{{HEADER}}\n')
L = lambda t: f'<div class="lead" style="{F}font-size:16px;line-height:24px;color:#2E2E2E;text-align:left;padding-top:12px;">{t}</div>'
e.live(CREAM, L("Hi {{ first_name|default:'there' }},") + L('Last note from me about your welcome code.') +
       L(f'<b>HI10 takes 10% off everything</b>, and {GIFTS}. It has no end date, so no pressure. But if you were waiting for a sign, this is it.') +
       L('<b>Two promises.</b> Changed your mind? Unused within 30 days of delivery, full refund. Something wrong? Damaged or defective in the first 30 days, we refund or replace it and pay the shipping. After that, the 75-year warranty.') +
       L('Not sure which pan? Reply and tell me what you cook most. Our team will help.'), '18px 40px 0 40px')
e.sign()
e.torn(CREAM, DARK)
e.img('e5-recap', 'Your offer in one place: 10% off with HI10, plus 5 free gifts, 75-year warranty, 30-day returns. Pan Pro Standard $144, $129.60 with HI10. 6-Piece Set $299, $269.10. 12-Piece Set $649, $584.10.', e.U('recap'))
sm = lambda k, t: f'<td width="33%" align="center" style="width:33%;padding:0 4px;"><a href="{e.UP("recap-" + k, k)}" style="display:block;background-color:{W};color:{INK};{F}font-size:12px;line-height:15px;font-weight:800;padding:11px 4px;border-radius:30px;text-decoration:none;">{t}</a></td>'
e.live(DARK, f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{sm("standard", "PAN &rarr;")}{sm("set6", "6-PIECE &rarr;")}{sm("set12", "12-PIECE &rarr;")}</tr></table>', '0 30px 6px 30px')
e.offer(DARK, '<b>Your code, one more time.</b>', 'Claim my 10% + gifts', e.U('cta'), dark=True)
e.add('{{FOOTER}}\n')
page(e, 'Last note about your 10%', 'No end date, no pressure. Two promises, and your 10% in one place.')

import json; json.dump(REPORT_SIZES, open(os.path.join(ROOT, 'sections/weights.json'), 'w'))
