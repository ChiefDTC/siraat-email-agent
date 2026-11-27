"""Creative strategists BF-mail (2 docs, 27 nov), samengevoegd en claim-proof gemaakt. US only (12-delige set).
Gebruikt helpers uit ../bf-1127/_tools/build.py (vaste header/footer). Gebruik: python3 -I build.py"""
import os, re
H = os.path.dirname(os.path.abspath(__file__))
BT = os.path.join(os.path.dirname(H), 'bf-1127', '_tools')
src = open(os.path.join(BT, 'build.py')).read().split("os.makedirs(os.path.join(T, '.preview')")[0]
g = {'__file__': os.path.join(BT, 'build.py')}; exec(src, g)
p, a, btn, row, signoff, shell, FIRST, MUTED, SANS, SERIF, INK, RED, IMG12, LINE, PANEL = (g[k] for k in
 ('p','a','btn','row','signoff','shell','FIRST','MUTED','SANS','SERIF','INK','RED','IMG12','LINE','PANEL'))
SITE = 'https://siraatskitchen.com'
def L(path, c): return f'{SITE}{path}?utm_source=klaviyo&utm_medium=email&utm_campaign=bf-strategist-12pc&utm_content={c}'
SET = '/products/titanium-hammered-cookware-set'
LAB = '/pages/third-party-testing'
GOLD = '#F2C14E'
hero = (f'<tr><td bgcolor="#111111" style="background-color:#111111;padding:34px 30px 10px 30px;text-align:center;font-family:{SANS};">'
        f'<div style="font-size:13px;line-height:18px;letter-spacing:2.5px;font-weight:800;color:{GOLD};">BLACK FRIDAY JUST WENT LIVE</div>'
        f'<div style="font-size:84px;line-height:88px;font-weight:900;color:#FFFFFF;padding-top:10px;">30% OFF</div>'
        f'<div style="font-family:{SERIF};font-size:30px;line-height:36px;color:#FFFFFF;padding-top:6px;">The 12-Piece Titanium Hammered Set</div>'
        f'<div style="font-size:18px;line-height:26px;font-weight:700;color:{GOLD};padding-top:14px;">+ 5 FREE gifts, including a mystery gift</div>'
        f'</td></tr>\n'
        f'<tr><td bgcolor="#111111" style="background-color:#111111;padding:16px 30px 0 30px;"><a href="{L(SET,"hero-img")}"><img src="{IMG12}" width="540" alt="The 12-Piece Titanium Hammered Set" style="display:block;width:100%;max-width:540px;height:auto;border:0;border-radius:6px;"></a></td></tr>\n'
        f'<tr><td bgcolor="#111111" style="background-color:#111111;padding:24px 40px 36px 40px;">' + btn('Grab my set', L(SET,'hero-btn')) +
        f'<div style="font-family:{SANS};font-size:13px;line-height:19px;color:#BDB8B0;text-align:center;padding-top:12px;">Free shipping. 30-day returns. 100,000+ happy customers.</div></td></tr>\n')
story = row(
    p(f'Hey {FIRST},') +
    p('Go to your kitchen. Pull out the frying pan you use every morning. The one you’ve had for three, five, maybe eight years.') +
    p('Hold it under the light. Run your thumb across the surface. Slowly.') +
    p('Feel the scratches? The rough patches where the smooth black used to be?') +
    p('That’s the coating wearing off. Every coated pan does it eventually. That’s why you keep buying new ones.') +
    p('<b>We built the set that ends that cycle.</b> Every piece has a pure titanium cooking surface with no coatings. Nothing sprayed on, nothing to scratch off, nothing to flake.') +
    p(f'We had our Pan Pro tested by Light Labs, an ISO/IEC 17025-accredited lab. Report no. 25895: 31 PFAS compounds tested, every one below the detection limit. Every piece in this set has the same titanium cooking surface. {a("Read the report yourself", L(LAB,"lab"))}.'),
    '34px 40px 10px 40px')
items = [('8" Pan + Lid','Eggs, single portions, quick sauces. The one you’ll reach for first.'),
         ('10" Pan + Lid','Everyday sautéing, veggies and weeknight dinners.'),
         ('12" Pan + Lid','Steaks, family meals and big one-pan dishes.'),
         ('2-Qt Saucepan + Lid','Sauces, grains and reheating.'),
         ('3-Qt Saucepan + Lid','Pasta, soups and sides.'),
         ('Stockpot + Lid','Stocks, stews, chili and batch cooking.')]
lst = ''.join(f'<tr><td style="padding:10px 0;border-bottom:1px solid {LINE};font-family:{SANS};font-size:16px;line-height:24px;color:{INK};"><b>{n}</b><br><span style="color:{MUTED};font-size:15px;">{d}</span></td></tr>' for n, d in items)
inside = row(
    f'<div style="font-family:{SERIF};font-size:30px;line-height:36px;color:{INK};padding-bottom:6px;">Everything inside the 12-piece set</div>' +
    p('3 pans, 3 pots, 6 fitted lids. A complete kitchen in one decision.', 16, 24, MUTED) +
    f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{lst}</table>' +
    p('Every piece: pure titanium cooking surface, no coatings, 75-year warranty.', 15, 23, INK, '16px 0 18px 0') +
    btn('Shop the 12-piece set', L(SET,'inside-btn')), '26px 40px 30px 40px')
rows = [('No coating to scratch or flake','&#10003;','&#10007;'),('No PFAS, PFOA or BPA','&#10003; Lab tested','Varies'),
        ('Safe with metal utensils','&#10003;','&#10007;'),('Oven safe','&#10003;','Limited'),('Induction, gas, electric, ceramic','&#10003;','Varies'),
        ('Dishwasher safe','&#10003;','Not advised'),('Warranty','75 years','Short')]
tb = (f'<tr><td style="padding:10px 8px;font-family:{SANS};font-size:12px;letter-spacing:1px;font-weight:800;color:#FFFFFF;background:{INK};">FEATURE</td>'
      f'<td align="center" style="padding:10px 8px;font-family:{SANS};font-size:12px;letter-spacing:1px;font-weight:800;color:#FFFFFF;background:{RED};">SIRAAT</td>'
      f'<td align="center" style="padding:10px 8px;font-family:{SANS};font-size:12px;letter-spacing:1px;font-weight:800;color:#FFFFFF;background:{INK};">COATED PANS</td></tr>')
for i, (f, s, c) in enumerate(rows):
    bg = '#FFFFFF' if i % 2 == 0 else PANEL
    tb += (f'<tr><td style="padding:11px 8px;font-family:{SANS};font-size:14px;line-height:20px;color:{INK};background:{bg};">{f}</td>'
           f'<td align="center" style="padding:11px 8px;font-family:{SANS};font-size:14px;font-weight:700;color:#2E7D32;background:{bg};">{s}</td>'
           f'<td align="center" style="padding:11px 8px;font-family:{SANS};font-size:14px;color:{RED};background:{bg};">{c}</td></tr>')
compare = row(f'<div style="font-family:{SERIF};font-size:30px;line-height:36px;color:{INK};padding-bottom:14px;">Siraat vs. coated cookware</div>'
              f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid {LINE};">{tb}</table>', '20px 40px 30px 40px')
deal = (f'<tr><td bgcolor="#111111" style="background-color:#111111;padding:34px 40px 36px 40px;font-family:{SANS};">'
        f'<div style="font-size:13px;letter-spacing:2.5px;font-weight:800;color:{GOLD};text-align:center;">THIS DEAL WON’T LAST</div>'
        f'<div style="font-size:17px;line-height:27px;color:#FFFFFF;padding-top:14px;">Black Friday isn’t about margin for me. It’s about getting pure titanium into as many kitchens as possible before another year of coated pans goes by.</div>'
        f'<div style="font-size:17px;line-height:27px;color:#FFFFFF;padding-top:12px;">So the 12-piece set is 30% off, with 5 free gifts. This price ends [END DATE]. After that, it’s back to the regular sale price.</div>'
        f'<div style="font-size:16px;line-height:24px;color:#BDB8B0;padding-top:12px;">Benjamin, Founder</div>'
        f'<div style="padding-top:22px;">' + btn('Claim 30% off + 5 free gifts', L(SET,'deal-btn')) + '</div>'
        f'<div style="font-size:13px;line-height:20px;color:#BDB8B0;text-align:center;padding-top:14px;">&#10003; Tested PFAS-free (report no. 25895) &middot; &#10003; 75-year warranty &middot; &#10003; 30-day returns &middot; &#10003; Free shipping</div>'
        f'</td></tr>\n')
body = hero + story + inside + compare + deal
h = shell('Black Friday is live', 'Upgrade your whole kitchen for 30% off. 5 free gifts included.', body)
assert '—' not in h
open(os.path.join(H, 'bf-strategist-12pc.html'), 'w').write(h)
pv = h.replace(FIRST, 'Sarah')
for t in ['{% unsubscribe_link %}', '{% manage_preferences_link %}', '{% web_view_link %}']: pv = pv.replace(t, '#')
pv = re.sub(r'\{%.*?%\}', '', pv).replace('{{ organization.name }}', 'Siraats Kitchen').replace('{{ organization.full_address }}', 'Address').replace('{{ sk_ref }}', '')
open(os.path.join(H, 'preview.html'), 'w').write(pv); print('ok', len(h))
