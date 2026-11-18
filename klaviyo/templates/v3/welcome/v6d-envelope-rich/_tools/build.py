"""Welcome v6d 'Rich detail' (concept, 17 nov 2026). NIET LIVE. Copy, prijzen, links en eerlijkheid uit v6b/v6c.
Nieuw: echte productfoto's en Higgsfield-beelden in elke sectie, typografie-baseline (PLAYBOOK 17 nov).
Live HTML: preheader, codebalk, header, regel onder de hero, codebox, hoofdknoppen, brieftekst E5, footer.
Gebruik: python3 -I _tools/build.py   Spec: klaviyo/flows/welcome-v6d-envelope-rich.md
"""
import re, os, json
from urllib.parse import quote
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPO = os.path.abspath(os.path.join(ROOT, '../../../../..'))
P = os.path.join(REPO, 'klaviyo/templates/partials')
def load(p): return dict(l.split() for l in open(p) if len(l.split()) == 2)
urls = load(os.path.join(P, 'shared/klaviyo-urls.txt'))
urls.update(load(os.path.join(REPO, 'klaviyo/templates/v3/campaigns/thanksgiving-roast-1117/assets/klaviyo-urls.txt')))
S = load(os.path.join(ROOT, 'klaviyo-urls.txt'))

CAMP, CODE = 'v6d-welcome-rich', 'HI10'
GIFTS = '5 free gifts with every order'  # [VRAAG FLORIS] na BF
REPORT = 'https://siraatskitchen.com/pages/third-party-testing'
H = {'standard': 'original-siraat-100-pure-titanium-pan-with-hammered-pattern', 'mini': 'titanium-hammered-pan-pro-mini', 'small': 'titanium-hammered-pan-pro-small',
     'large': 'titanium-hammered-pan-pro-large', 'set6': 'titanium-hammered-pan-set-with-lids-6-pcs', 'set12': 'titanium-hammered-cookware-set',
     'duo': '2-pans-and-2-lids', 'roast': 'titanium-hammered-roasting-pan'}
NAME = {'standard': 'Titanium Hammered Pan Pro Standard 11 inch, $144, $129.60 with HI10', 'large': 'Pan Pro Large 12 inch, $149, $134.10 with HI10',
        'set6': '6-Piece Set, Mini, Small and Large with 3 lids, $299, $269.10 with HI10', 'set12': '12-Piece Set, 3 pans, 3 pots and 6 lids, $649, $584.10 with HI10',
        'duo': '2 Pans + 2 Lids, $199, $179.10 with HI10', 'roast': 'Titanium Hammered Roasting Pan with V-rack, $199, $179.10 with HI10'}
F = "font-family:Inter,Arial,Helvetica,sans-serif;"
INK, BODY, BRICK, CREAM, SAND, DARK, ORANGE, GOLD, W, PAPER = '#272727', '#2E2E2E', '#AC3B19', '#F8F7F2', '#ECE7DD', '#282828', '#C4642C', '#B8862B', '#FFFFFF', '#FBF8F1'
FR = 'Free shipping. 30-day returns. 100,000+ happy customers.'

class Mail:
    def __init__(s, mid): s.mid, s.b, s.imgs = mid, '', []
    def U(s, c, path='/collections/cookware'):
        return f'https://siraatskitchen.com/discount/{CODE}?redirect=' + quote(f'{path}?utm_source=klaviyo&utm_medium=email&utm_campaign={CAMP}&utm_content={s.mid}-{c}', safe='')
    def UP(s, c, k): return s.U(c, '/products/' + H[k])
    def add(s, h): s.b += h; return s
    def img(s, key, alt, href, ext='jpg'):
        s.imgs.append(key + '.' + ext)
        return s.add(f'<tr><td style="padding:0;font-size:0;line-height:0;"><a href="{href}" style="display:block;border:0;"><img src="{S[key + "." + ext]}" width="600" alt="{alt}" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>\n')
    def torn(s, a, b): return s.img(f'torn-{a[1:]}-{b[1:]}', '', s.U('edge'))
    def codebar(s, t):
        return s.add(f'<tr><td align="center" bgcolor="{INK}" style="background-color:{INK};padding:11px 16px;{F}font-size:11px;line-height:15px;letter-spacing:2px;font-weight:600;color:{CREAM};text-transform:uppercase;"><a href="{s.U("codebar")}" style="color:{CREAM};text-decoration:none;">{t}</a></td></tr>\n')
    def live(s, bg, inner, pad='22px 40px 26px 40px', al='center'):
        return s.add(f'<tr><td align="{al}" bgcolor="{bg}" class="pad" style="background-color:{bg};padding:{pad};text-align:{al};">{inner}</td></tr>\n')
    def btn(s, label, href, dark):
        bb, fc = (W, INK) if dark else (INK, W)
        return (f'<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="400" style="width:100%;max-width:400px;margin:0 auto;"><tr><td align="center" bgcolor="{bb}" style="background-color:{bb};border-radius:40px;">'
                f'<a href="{href}" style="display:block;padding:19px 16px;{F}font-size:15px;line-height:18px;font-weight:600;letter-spacing:1.2px;color:{fc};text-decoration:none;text-transform:uppercase;">{label} &rarr;</a></td></tr></table>')
    def offer(s, bg, line, label, href, dark=False, extra=''):
        tc, sc, box, bd = (W, '#CFC8BC', '#353332', '#E7C988') if dark else (BODY, '#727272', W, INK)
        inner = (f'<div class="lead" style="{F}font-size:17px;line-height:27px;font-weight:400;color:{tc};">{line}</div>'
                 f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" style="margin:16px auto 0 auto;"><tr><td align="center" bgcolor="{box}" style="background-color:{box};border:2px dashed {bd};border-radius:10px;padding:10px 34px;">'
                 f'<div style="{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:600;color:{GOLD};">YOUR WELCOME CODE</div><div style="{F}font-size:32px;line-height:40px;letter-spacing:8px;font-weight:800;color:{W if dark else INK};">{CODE}</div></td></tr></table>'
                 f'<div style="padding-top:16px;">{s.btn(label, href, dark)}</div><div style="{F}font-size:12px;line-height:18px;color:{sc};padding-top:10px;">{FR}</div>{extra}')
        return s.live(bg, inner)
    def cta(s, bg, label, href, dark=False, sub=None, pad='6px 40px 32px 40px'):
        sc = '#F1D9CB' if bg in (BRICK, ORANGE) else ('#CFC8BC' if dark else '#727272')
        return s.live(bg, s.btn(label, href, dark) + (f'<div style="{F}font-size:12px;line-height:18px;color:{sc};padding-top:10px;">{sub}</div>' if sub else ''), pad)
    def cards(s, rows):
        for r in rows:
            cells = ''.join(f'<td width="50%" valign="top" style="width:50%;padding:0;font-size:0;line-height:0;"><a href="{s.UP("card-" + k, k)}" style="display:block;"><img src="{S["card-" + k + ".jpg"]}" width="300" alt="{NAME[k]}" style="display:block;width:100%;max-width:300px;height:auto;border:0;"></a></td>' for k in r)
            s.imgs += ['card-' + k + '.jpg' for k in r]
            s.add(f'<tr><td bgcolor="{SAND}" style="background-color:{SAND};padding:0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cells}</tr></table></td></tr>\n')
        return s.live(SAND, '', '8px 0 0 0')
    def sign(s, bg=CREAM, ps=None):
        t = f'<div style="{F}font-size:16px;line-height:24px;color:{INK};text-align:left;font-weight:600;">Benjamin</div><div style="{F}font-size:14px;line-height:20px;color:#8A847A;text-align:left;">Founder, Siraat</div>'
        if ps: t += f'<div style="{F}font-size:14px;line-height:22px;color:#5E5A54;text-align:left;padding-top:10px;">{ps}</div>'
        return s.live(bg, t, '18px 40px 28px 40px')

hdr = open(os.path.join(P, 'header.html')).read(); ftr = open(os.path.join(P, 'footer.html')).read()
for k, v in urls.items():
    hdr = hdr.replace('{{SHARED}}/' + k, v); ftr = ftr.replace('{{SHARED}}/' + k, v).replace('{{IMG}}/' + k, v)
hdr = re.sub(r'<!--.*?-->\n?', '', hdr, flags=re.S); ftr = re.sub(r'<!--.*?-->\n?', '', ftr, flags=re.S)
def utm_nav(h, tag, mid):
    return re.sub(r'href="(https://(?:www\.)?siraatskitchen\.com[^"?]*)"', lambda m: f'href="{m.group(1)}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content={mid}-{tag}-{(m.group(1).rstrip("/").split("/")[-1] or "home").replace(".com", "home")}"', h)
HEAD = open(os.path.join(ROOT, '../v6-envelope/e1.html')).read().split('<body')[0]
WEIGHTS = {}
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
    kb = sum(os.path.getsize(os.path.join(ROOT, 'sections', k)) for k in set(m.imgs)) // 1024
    WEIGHTS[m.mid] = len(html) // 1024 + kb + 30  # +30 KB header, footer en iconen
    print(m.mid, 'html', len(html) // 1024, 'KB, images', len(m.imgs), kb, 'KB, total ~', WEIGHTS[m.mid], 'KB')

# ======================= E1
e = Mail('e1')
e.codebar(f'Welcome &middot; 10% off with HI10 &middot; {GIFTS}').add('{{HEADER}}\n')
e.img('e1-envelope', 'Your welcome envelope: the gold seal breaks and the card inside reads 10% off plus 5 free gifts. 10% off everything with code HI10.', e.U('hero'), ext='gif')
e.offer(CREAM, f'HI10 takes <b>10% off everything</b>, sets included. Plus {GIFTS}.', 'Claim my 10% + gifts', e.U('cta1'),
        extra=f'<div style="{F}font-size:14px;line-height:22px;color:{BODY};padding-top:10px;">Already something in your cart? <a href="{e.U("cart", "/cart")}" style="color:{BRICK};">Apply my 10% to my cart &rarr;</a></div>')
e.torn(CREAM, DARK)
e.img('e1-steps', 'How it works, three steps. 1: pick your pan or set. 2: HI10 is applied by the button, or type it at checkout. 3: the 5 free gifts ship in the same box.', e.U('steps'))
e.torn(DARK, SAND)
e.img('h-bestsellers', 'Start here: our bestsellers, with your 10%', e.U('h-best'))
e.cards([['standard', 'set6']])
e.torn(SAND, BRICK)
e.img('e1-bundle', 'Most people pick the 6-piece set. $293 saved: Mini $129, Small $137, Large $149 and 3 lids $177 cost $592 one by one, the set is $299. With HI10 $269.10, about $90 a pan, lid included.', e.UP('bundle', 'set6'))
e.cta(BRICK, 'Get the set for $269.10', e.UP('bundle-cta', 'set6'), dark=True, sub='One use of HI10, applied by the button. 30-day returns.')
e.torn(BRICK, SAND)
e.img('gifts-flatlay', '5 free gifts in the box with every order: free shipping, the Favorites Cookbook, the plastic-free e-book, a mystery gift and a weekly chance to win a PFAS water filter.', e.U('gifts'))
e.torn(SAND, CREAM)
e.img('e1-reviews', 'Five stars from 100,000+ happy customers. Tammy: I am on my 4th pan from Siraat. Sunny C.: I ordered one pan to try it out, now I am ordering the set.', e.UP('reviews', 'standard'))
e.cta(CREAM, 'Claim my 10% + gifts', e.U('cta2'), sub=FR, pad='4px 40px 10px 40px')
e.sign()
e.add('{{FOOTER}}\n')
page(e, 'Your 10% is inside', f'HI10 takes 10% off everything, sets included. Plus {GIFTS}.')

# ======================= E2
e = Mail('e2')
e.codebar(f'10% off with HI10 &middot; {GIFTS}').add('{{HEADER}}\n')
e.img('e2-hero', 'The pan nobody else was making. The original hammered pan. First orders shipped December 20, 2024. Look-alikes came after.', e.UP('hero', 'standard'))
e.offer(DARK, 'Yours is <b>10% off</b>, on every size and set.', 'Get 10% off the original', e.UP('cta1', 'standard'), dark=True)
e.torn(DARK, CREAM)
e.img('e2-story', 'A woman laughing as she slides a fried egg out of a hammered titanium pan. Siraat: from sirat, the Arabic word for path. We started with titanium cutting boards, then made the pan with a pure titanium cooking surface and no coatings, covered for 75 years.', e.UP('story', 'standard'))
e.torn(CREAM, SAND)
e.img('e2-sizes', 'Which size is yours, to scale with an egg: Mini 8 inch $129, $116.10 with HI10. Small 10 inch $137, $123.30. Standard 11 inch $144, $129.60, most picked. Large 12 inch $149, $134.10.', e.UP('sizes', 'standard'))
sz = lambda k, t: f'<td width="25%" align="center" style="width:25%;padding:0 3px;"><a href="{e.UP("size-" + k, k)}" style="display:block;background-color:{INK if k == "standard" else W};color:{W if k == "standard" else INK};{F}font-size:12px;line-height:15px;font-weight:600;letter-spacing:1px;padding:12px 2px;border-radius:30px;text-decoration:none;">{t}</a></td>'
e.live(SAND, f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{sz("mini", "MINI")}{sz("small", "SMALL")}{sz("standard", "STANDARD")}{sz("large", "LARGE")}</tr></table>', '0 30px 30px 30px')
e.torn(SAND, DARK)
e.img('e2-stack', 'Everything you get: Pan Pro Standard 11 inch $144, 5 free gifts worth $555, 75-year warranty and 30-day returns included. Your price $129.60 with HI10.', e.UP('stack', 'standard'))
e.cta(DARK, 'Get my pan for $129.60', e.UP('stack-cta', 'standard'), dark=True, sub=FR)
e.torn(DARK, CREAM)
e.img('e2-reviews', 'Five stars. Carole: cooking for over 60 years, the best pan she has used. Graham C.: the best omelette we have ever eaten.', e.UP('reviews', 'standard'))
e.sign(ps='P.S. HI10 has no end date. One use, 10% off everything.')
e.add('{{FOOTER}}\n')
page(e, 'The pan nobody else was making', 'First orders shipped December 20, 2024. Pick your size, 10% off with HI10.')

# ======================= E3
e = Mail('e3')
e.codebar(f'10% off with HI10 &middot; {GIFTS}').add('{{HEADER}}\n')
e.img('e3-hero', 'Report no. 25895. Tested for 31 PFAS. Every one below the detection limit. Read the paper, not the label.', e.UP('hero', 'standard'))
e.offer(DARK, f'Every pan says non-toxic. We show the paper. <a href="{REPORT}?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={CAMP}&amp;utm_content=e3-report" style="color:#E7C988;">Read report no. 25895 &rarr;</a>', 'Get 10% off the tested pan', e.UP('cta1', 'standard'), dark=True)
e.torn(DARK, SAND)
e.img('e3-compare', 'Photo comparison, Siraat Pan Pro vs a worn PFAS-coated pan: pure titanium surface vs a coating on top; no coating to wear off vs coating wears with use; metal utensils welcome vs wood or silicone advised; dishwasher safe vs hand wash advised; lab report 25895 vs testing varies by brand.', e.UP('compare', 'standard'))
e.torn(SAND, CREAM)
e.img('e3-anatomy', 'Up close, the Pan Pro: pure titanium cooking surface, no coating to wear off, hammered texture, works on induction, gas and electric.', e.UP('anatomy', 'standard'))
e.torn(CREAM, DARK)
e.img('e3-reviews', 'The egg test, five stars. Michael G.: the egg released completely. Thomas D.: makes our other non stick pans seem really sticky.', e.UP('reviews', 'standard'))
e.torn(DARK, BRICK)
e.img('e3-bundle', 'Or the whole stove: 3 pans and 3 lids. $293 saved versus $592 one by one. The set is $299, $269.10 with HI10.', e.UP('bundle', 'set6'))
e.cta(BRICK, 'Get the set for $269.10', e.UP('bundle-cta', 'set6'), dark=True, sub='Same titanium cooking surface on every pan in the set.')
e.torn(BRICK, CREAM)
e.sign()
e.add('{{FOOTER}}\n')
page(e, 'Report no. 25895', '31 PFAS compounds tested, every one below detection. Your 10% is still here.')

# ======================= E4
e = Mail('e4')
e.codebar(f'Still unused &middot; 10% off with HI10 &middot; {GIFTS}').add('{{HEADER}}\n')
e.img('e4-hero', 'Your envelope: still sealed? Your 10% hasn&rsquo;t been used yet.', e.U('hero'))
e.offer(DARK, f'HI10 takes <b>10% off everything</b>. No end date. Plus {GIFTS}.', 'Use my 10% now', e.U('cta1'), dark=True)
e.torn(DARK, SAND)
e.img('h-start', 'Most picked: where most people start', e.U('h-start'))
e.cards([['standard', 'set6'], ['set12', 'large']])
e.live(SAND, f'<div style="{F}font-size:12px;line-height:18px;color:#8A847A;">12-piece set: 3 pans, 2-qt and 3-qt saucepans, an 8-qt stockpot, a lid for each. US only.</div>', '0 40px 22px 40px')
e.torn(SAND, DARK)
e.img('e4-objections', 'Quick answers. Will food stick? Not when the pan is hot: medium heat 2 to 3 minutes and a teaspoon of oil. Induction? Yes, also gas, electric and ceramic. Don&rsquo;t like it? 30-day returns, unused, full refund.', e.U('objections'))
e.torn(DARK, ORANGE)
e.img('e4-complete', 'Complete the set: 3 pans and 3 lids instead of one pan. $293 saved versus one by one. $299, or $269.10 with HI10.', e.UP('complete', 'set6'))
e.cta(ORANGE, 'Upgrade to the 6-piece set', e.UP('complete-cta', 'set6'), dark=True, sub='One use of HI10, applied by the button.')
e.torn(ORANGE, CREAM)
e.img('e4-reviews', 'In their words, five stars. Fatima: I thought it was marketing hype, I ended up buying the whole collection. Brandon W.: they honored the warranty.', e.UP('reviews', 'set12'))
e.cta(CREAM, 'Use my 10% now', e.U('cta2'), sub=FR, pad='4px 40px 10px 40px')
e.sign()
e.add('{{FOOTER}}\n')
page(e, 'Still sealed', f'Your 10% is unused. Where most people start, with your price, plus {GIFTS}.')

# ======================= E5: brief op papier + armen + recap
e = Mail('e5')
e.add('{{HEADER}}\n')
e.img('e5-paper-top', 'A note from Benjamin', e.U('letter'))
L = lambda t: f'<div class="lead" style="{F}font-size:16px;line-height:26px;font-weight:400;color:{BODY};text-align:left;padding-top:12px;">{t}</div>'
letter = (L("Hi {{ first_name|default:'there' }},") + L('Last note from me about your welcome code.') +
          L(f'HI10 takes <b>10% off everything</b>, and {GIFTS}. It has no end date, so no pressure. But if you were waiting for a sign, this is it.') +
          L('Two promises. Changed your mind? Unused within 30 days of delivery, full refund. Something wrong? Damaged or defective in the first 30 days, we refund or replace it and pay the shipping. After that, the 75-year warranty.') +
          L('Not sure which pan? Reply and tell me what you cook most. Our team will help.'))
e.add(f'<tr><td bgcolor="{CREAM}" style="background-color:{CREAM};padding:0 25px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="{PAPER}" class="pad" style="background-color:{PAPER};padding:0 40px 6px 40px;">{letter}</td></tr></table></td></tr>\n')
e.img('e5-paper-sign', 'Signed, Benjamin, founder of Siraat', e.U('signature'))
e.torn(CREAM, BRICK)
e.img('e5-arms', 'Two hands hold up hammered titanium pans against a brick red background. Your offer in one place: 10% off every pan and every set with HI10, plus 5 free gifts with every order.', e.UP('arms', 'standard'))
e.torn(BRICK, DARK)
e.img('e5-recap-top', '75-year warranty, 30-day returns, free shipping.', e.U('recap-top'))
RC = {'standard': 'Pan Pro Standard $144, $129.60 with HI10', 'set6': '6-Piece Set $299, $269.10 with HI10', 'set12': '12-Piece Set $649, $584.10 with HI10'}
for k in RC: e.imgs.append('e5-recap-' + k + '.jpg')
e.add(f'<tr><td bgcolor="{DARK}" style="background-color:{DARK};padding:0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>' + ''.join(
    f'<td width="200" valign="top" style="width:33.33%;padding:0;font-size:0;line-height:0;"><a href="{e.UP("recap-card-" + k, k)}" style="display:block;"><img src="{S["e5-recap-" + k + ".jpg"]}" width="200" alt="{RC[k]}" style="display:block;width:100%;max-width:200px;height:auto;border:0;"></a></td>' for k in RC) + '</tr></table></td></tr>\n')
sm = lambda k, t: f'<td width="33%" align="center" style="width:33%;padding:0 4px;"><a href="{e.UP("recap-" + k, k)}" style="display:block;background-color:{W};color:{INK};{F}font-size:12px;line-height:15px;font-weight:600;letter-spacing:1px;padding:11px 4px;border-radius:30px;text-decoration:none;">{t}</a></td>'
e.live(DARK, f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{sm("standard", "PAN &rarr;")}{sm("set6", "6-PIECE &rarr;")}{sm("set12", "12-PIECE &rarr;")}</tr></table>', '0 30px 6px 30px')
e.offer(DARK, 'Your code, one more time.', 'Claim my 10% + gifts', e.U('cta'), dark=True)
e.add('{{FOOTER}}\n')
page(e, 'Last note about your 10%', 'No end date, no pressure. Two promises, and your 10% in one place.')
json.dump(WEIGHTS, open(os.path.join(ROOT, 'sections/weights.json'), 'w'))
