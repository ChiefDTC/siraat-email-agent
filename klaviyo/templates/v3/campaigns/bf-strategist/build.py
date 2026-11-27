"""Creative strategists BF-mails (2 docs, 27 nov), elk als eigen mail, claim-proof. US only, 12-delige set $499 (code SET499, $150 = 23%).
A = doc 1 (gestructureerd), B = doc 2 (verhaal). Helpers uit ../bf-1127/_tools/build.py. Gebruik: python3 -I build.py"""
import os, re
H = os.path.dirname(os.path.abspath(__file__))
BT = os.path.join(os.path.dirname(H), 'bf-1127', '_tools')
src = open(os.path.join(BT, 'build.py')).read().split("os.makedirs(os.path.join(T, '.preview')")[0]
g = {'__file__': os.path.join(BT, 'build.py')}; exec(src, g)
p, a, btn, row, shell, FIRST, MUTED, SANS, SERIF, INK, RED, IMG12, LINE, PANEL = (g[k] for k in
 ('p','a','btn','row','shell','FIRST','MUTED','SANS','SERIF','INK','RED','IMG12','LINE','PANEL'))
SITE = 'https://siraatskitchen.com'; SET = '/products/titanium-hammered-cookware-set'; LAB = '/pages/third-party-testing'; GOLD = '#F2C14E'
def L(camp, path, c):
    pre = f'{SITE}/discount/SET499?redirect={path}&' if path == SET else f'{SITE}{path}?'
    return f'{pre}utm_source=klaviyo&utm_medium=email&utm_campaign={camp}&utm_content={c}'
def H2(t): return f'<div style="font-family:{SERIF};font-size:30px;line-height:36px;color:{INK};padding-bottom:8px;">{t}</div>'
def hero(camp, label, big, btn_label):
    return (f'<tr><td bgcolor="#111111" style="background-color:#111111;padding:34px 30px 10px 30px;text-align:center;font-family:{SANS};">'
        f'<div style="font-size:13px;line-height:18px;letter-spacing:2.5px;font-weight:800;color:{GOLD};">{label}</div>'
        f'<div style="font-size:84px;line-height:88px;font-weight:900;color:#FFFFFF;padding-top:10px;">{big}</div>'
        f'<div style="font-size:18px;line-height:26px;color:#BDB8B0;padding-top:4px;"><s>$649</s> &middot; an extra 23% off</div>'
        f'<div style="font-family:{SERIF};font-size:30px;line-height:36px;color:#FFFFFF;padding-top:8px;">The 12-Piece Titanium Hammered Set</div>'
        f'<div style="font-size:18px;line-height:26px;font-weight:700;color:{GOLD};padding-top:12px;">+ 5 FREE gifts, including a mystery gift</div></td></tr>\n'
        f'<tr><td bgcolor="#111111" style="background-color:#111111;padding:16px 30px 0 30px;"><a href="{L(camp,SET,"hero-img")}"><img src="{IMG12}" width="540" alt="The 12-Piece Titanium Hammered Set" style="display:block;width:100%;max-width:540px;height:auto;border:0;border-radius:6px;"></a></td></tr>\n'
        f'<tr><td bgcolor="#111111" style="background-color:#111111;padding:24px 40px 36px 40px;">' + btn(btn_label, L(camp,SET,'hero-btn')) +
        f'<div style="font-family:{SANS};font-size:13px;line-height:19px;color:#BDB8B0;text-align:center;padding-top:12px;">$499 already applied. Free shipping. 30-day returns. 100,000+ happy customers.</div></td></tr>\n')
ITEMS = [('8" Pan + Lid','Eggs, single portions, quick sauces. The one you’ll reach for first.'),('10" Pan + Lid','Everyday sautéing, veggies and weeknight dinners.'),
         ('12" Pan + Lid','Steaks, family meals and big one-pan dishes.'),('2-Qt Saucepan + Lid','Sauces, grains and reheating.'),
         ('3-Qt Saucepan + Lid','Pasta, soups and sides.'),('Stockpot + Lid','Stocks, stews, chili and batch cooking.')]
def inside(camp, title, sub):
    lst = ''.join(f'<tr><td style="padding:10px 0;border-bottom:1px solid {LINE};font-family:{SANS};font-size:16px;line-height:24px;color:{INK};"><b>{n}</b><br><span style="color:{MUTED};font-size:15px;">{d}</span></td></tr>' for n, d in ITEMS)
    return row(H2(title) + p(sub, 16, 24, MUTED) + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{lst}</table>' +
               p('Every piece: pure titanium cooking surface, no coatings, 75-year warranty. About $83 a piece, lids included.', 15, 23, INK, '16px 0 18px 0') +
               btn('Shop the 12-piece set for $499', L(camp,SET,'inside-btn')), '26px 40px 30px 40px')
def compare(title, rows, right):
    tb = (f'<tr><td style="padding:10px 8px;font-family:{SANS};font-size:12px;letter-spacing:1px;font-weight:800;color:#FFFFFF;background:{INK};">FEATURE</td>'
          f'<td align="center" style="padding:10px 8px;font-family:{SANS};font-size:12px;letter-spacing:1px;font-weight:800;color:#FFFFFF;background:{RED};">SIRAAT</td>'
          f'<td align="center" style="padding:10px 8px;font-family:{SANS};font-size:12px;letter-spacing:1px;font-weight:800;color:#FFFFFF;background:{INK};">{right}</td></tr>')
    for i, (f, s, c) in enumerate(rows):
        bg = '#FFFFFF' if i % 2 == 0 else PANEL
        tb += (f'<tr><td style="padding:11px 8px;font-family:{SANS};font-size:14px;line-height:20px;color:{INK};background:{bg};">{f}</td>'
               f'<td align="center" style="padding:11px 8px;font-family:{SANS};font-size:14px;line-height:20px;font-weight:700;color:#2E7D32;background:{bg};">{s}</td>'
               f'<td align="center" style="padding:11px 8px;font-family:{SANS};font-size:14px;line-height:20px;color:{RED};background:{bg};">{c}</td></tr>')
    return row(H2(title) + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid {LINE};">{tb}</table>', '20px 40px 30px 40px')
def deal(camp, label, paras, btn_label):
    body = ''.join(f'<div style="font-size:17px;line-height:27px;color:#FFFFFF;padding-top:12px;">{x}</div>' for x in paras)
    return (f'<tr><td bgcolor="#111111" style="background-color:#111111;padding:34px 40px 36px 40px;font-family:{SANS};">'
        f'<div style="font-size:13px;letter-spacing:2.5px;font-weight:800;color:{GOLD};text-align:center;">{label}</div>{body}'
        f'<div style="padding-top:22px;">' + btn(btn_label, L(camp,SET,'deal-btn')) + '</div>'
        f'<div style="font-size:13px;line-height:20px;color:#BDB8B0;text-align:center;padding-top:14px;">&#10003; Tested PFAS-free (report no. 25895) &middot; &#10003; 75-year warranty &middot; &#10003; 30-day returns &middot; &#10003; Free shipping</div></td></tr>\n')
END = 'This price ends Cyber Monday at midnight ET. After that, it’s back to $649.'
LABP = lambda camp: f'We had our Pan Pro tested by Light Labs, an ISO/IEC 17025-accredited lab. Report no. 25895: 31 PFAS compounds tested, every one below the detection limit. Every piece in this set has the same titanium cooking surface. {a("Read the report yourself", L(camp,LAB,"lab"))}.'

# ---------- A: doc 1 ----------
CA = 'bf-strategist-a'
A = (hero(CA, 'BLACK FRIDAY JUST WENT LIVE', '$499', 'Grab my set') +
     inside(CA, 'Everything inside our 12-piece titanium set', '3 pans, 3 pots, 6 fitted lids. A complete kitchen in one decision.') +
     row(p(LABP(CA), 15, 23), '0 40px 20px 40px') +
     compare('Siraat vs. coated cookware', [('No coating to scratch or flake','&#10003;','&#10007;'),('No PFAS, PFOA or BPA','&#10003; Lab tested','Varies'),
        ('Safe with metal utensils','&#10003;','&#10007;'),('Oven safe','&#10003;','Limited'),('Induction compatible','&#10003;','Varies'),
        ('Dishwasher safe','&#10003;','Not advised'),('Warranty','75 years','Short')], 'COATED PANS') +
     deal(CA, 'WARNING: THIS DEAL WON’T LAST', ['This is the lowest price we’ve ever put on the full 12-piece set, and we can’t keep it there.', f'$499 instead of $649, plus 5 free gifts. Already applied when you tap a button. {END}'], 'Claim my set for $499 + 5 free gifts'))
# ---------- B: doc 2 ----------
CB = 'bf-strategist-b'
B = (hero(CB, 'BLACK FRIDAY &middot; THE BIGGEST SALE IN SIRAAT HISTORY', '$499', 'Grab my set, Black Friday price') +
     row(H2('Your kitchen has a secret.') +
         p(f'Hey {FIRST},') +
         p('Go to your kitchen right now. Pull out your frying pan. The one you use every morning. The one you cook the kids’ eggs on. The one you’ve had for three, five, maybe eight years.') +
         p('Hold it under the light. Run your thumb across the surface. Slowly.') +
         p('Feel the scratches? The rough patches where the smooth black used to be? The bare metal underneath?') +
         p('That’s the coating leaving your pan. Every coated pan does it eventually. That’s why you keep replacing them.'), '34px 40px 6px 40px') +
     row(H2('We built the set that ends the cycle.') +
         p('The Siraat 12-Piece Titanium Hammered Set is not coated. Not sprayed. Not “titanium-reinforced.” Not “titanium-ceramic.”') +
         p('Every piece has a pure titanium cooking surface with no coatings. There is nothing on top of it. Nothing to scratch, flake or chip.') +
         p(LABP(CB)) + p('We show you the paper. Most brands only show you the label.'), '20px 40px 6px 40px') +
     inside(CB, '12 pieces. One titanium cooking surface.', 'Every piece has the same pure titanium surface, no coatings and a 75-year warranty.') +
     compare('Siraat vs. your “non-toxic” pans', [('Coating','&#10003; None. Nothing to scratch.','Wears off over time'),
        ('PFAS, PFOA, BPA','&#10003; None. Report published.','Often only a label'),('Metal utensils','&#10003; Use whatever you want.','“Wooden only”'),
        ('Dishwasher','&#10003; Safe','“Hand wash only”'),('Warranty','&#10003; 75 years','Short'),('What you pay for','&#10003; A set built to last','Another pan next year')], 'COATED PANS') +
     deal(CB, 'LET’S BE HONEST', ['The 12-piece set for $499 instead of $649. Plus 5 free gifts. Plus free shipping.',
        'This is the lowest price we’ve ever put on the full 12-piece set.', f'Already applied when you tap the button. {END}', 'Benjamin, Founder'], 'Claim the Black Friday deal') +
     row(p('<b>P.S.</b> Tonight, after dinner, do one thing. Pick up your frying pan and look at the surface under the kitchen light. Scratches, rough patches, bare metal? Then you already know.', 15, 23) +
         p(f'{a("Get the 12-piece set for $499", L(CB,SET,"ps"))}. Covered for 75 years.', 15, 23), '26px 40px 30px 40px'))
for name, body, title, pre in [('mail-a-doc1', A, 'Black Friday Is Live', 'Upgrade your whole kitchen: 12 titanium pieces for $499 + 5 free gifts.'),
                               ('mail-b-doc2', B, 'Black Friday: $499 for all 12 pieces + 5 free gifts', 'The only cookware set with zero coating. Already applied.')]:
    h = shell(title, pre, body); assert '—' not in h
    open(os.path.join(H, name + '.html'), 'w').write(h)
    pv = h.replace(FIRST, 'Sarah')
    for t in ['{% unsubscribe_link %}', '{% manage_preferences_link %}', '{% web_view_link %}']: pv = pv.replace(t, '#')
    pv = re.sub(r'\{%.*?%\}', '', pv).replace('{{ organization.name }}', 'Siraats Kitchen').replace('{{ organization.full_address }}', 'Address').replace('{{ sk_ref }}', '')
    open(os.path.join(H, name + '.preview.html'), 'w').write(pv); print(name, len(h))
