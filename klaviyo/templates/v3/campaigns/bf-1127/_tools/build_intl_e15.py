"""INTL vr 27 nov 08:00 (vervangt HS Email 15 INTL): schone eigen template, BFEXTRA10 already applied.
Hero + 6 productblokken als beeld (zelfde stijl als HS), elke CTA 'SHOP 70% OFF + 10% OFF'.
Vaste header/footer uit partials. Gebruik: python3 -I build_intl_e15.py"""
import os, re
T = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(T)
src = open(os.path.join(T, 'build.py')).read().split("os.makedirs(os.path.join(T, '.preview')")[0]
g = {'__file__': os.path.join(T, 'build.py')}; exec(src, g)
U = dict(l.split() for l in open('/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive/intl_bf/up4/klaviyo-urls.txt'))
SITE = 'https://siraatskitchen.com'
def L(path, c): return f'{SITE}/discount/BFEXTRA10?redirect={path}&utm_source=klaviyo&utm_medium=email&utm_campaign=bf-1127-intl-0800&utm_content={c}'
SALE = '/collections/black-friday-sale'
BLOCKS = [('b2-6pc.jpg', '/products/titanium-hammered-pan-set-with-lids-6-pcs', 'For the one who cooks every night: the 6-Piece Set. SHOP 70% OFF + 10% OFF'),
          ('b2-std.jpg', '/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern', 'For the new home: Pan Pro Standard. SHOP 70% OFF + 10% OFF'),
          ('b2-roast.jpg', '/products/titanium-hammered-roasting-pan', 'For the holiday table: Roasting Pan, rack included. SHOP 70% OFF + 10% OFF'),
          ('b2-wok.jpg', '/products/titanium-hammered-wok-pan-pro', 'For the stir-fry lover: Wok Pan Pro. SHOP 70% OFF + 10% OFF'),
          ('b2-deep.jpg', '/products/titanium-hammered-deep-pan-pro', 'For sauces and Sunday ragu: Deep Pan Pro. SHOP 70% OFF + 10% OFF'),
          ('b2-board.jpg', '/products/titanium-cutting-board-v2', 'For the plastic-free kitchen: Titanium Cutting Board. SHOP 70% OFF + 10% OFF')]
def imgrow(src, href, alt, bg='#000000'):
    return (f'<tr><td bgcolor="{bg}" style="padding:0;background-color:{bg};font-size:0;line-height:0;"><a href="{href}">'
            f'<img src="{src}" width="600" alt="{alt}" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></a></td></tr>\n')
bar = (f'<tr><td bgcolor="#B3262C" style="background-color:#B3262C;padding:12px 10px;text-align:center;font-family:Inter,Arial,Helvetica,sans-serif;">'
       f'<a href="{L(SALE, "bar")}" style="text-decoration:none;color:#FFFFFF;"><span style="display:block;font-size:16px;line-height:22px;font-weight:800;letter-spacing:1.5px;color:#FFFFFF;">EXTRA 10% OFF EVERYTHING &middot; 10% ALREADY APPLIED</span>'
       f'<span style="display:block;font-size:13px;line-height:19px;font-weight:600;letter-spacing:1px;color:#FFFFFF;">+ 5 FREE gifts with every order &middot; Today only &rarr;</span></a></td></tr>\n')
body = bar + imgrow(U['hero15-v4-nologo.jpg'], L(SALE, 'hero'), 'Up to 70% off. The craziest Black Friday ever: an extra 10% off on top of up to 70% off. SHOP 70% OFF + 10% OFF')
codebox = (f'<tr><td bgcolor="#000000" style="background-color:#000000;padding:6px 40px 30px 40px;">'
           f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="border:2px dashed #F2C14E;border-radius:6px;padding:16px 12px;">'
           f'<div style="font-family:Inter,Arial,Helvetica,sans-serif;font-size:22px;line-height:28px;font-weight:900;letter-spacing:1px;color:#FFFFFF;">YOUR EXTRA <span style="color:#F2C14E;">10% IS ALREADY APPLIED</span></div>'
           f'<div style="font-family:Inter,Arial,Helvetica,sans-serif;font-size:14px;line-height:21px;color:#BDB8B0;padding-top:6px;">No code needed when you tap any button. Not showing at checkout? Use code</div>'
           f'<div style="font-family:Inter,Arial,Helvetica,sans-serif;font-size:26px;line-height:34px;font-weight:900;letter-spacing:4px;color:#FFFFFF;padding-top:4px;">BFEXTRA10</div>'
           f'</td></tr></table></td></tr>\n')
body += codebox
for f, path, alt in BLOCKS:
    body += imgrow(U[f], L(path, f.split('.')[0]), alt)
body += (f'<tr><td bgcolor="#000000" style="background-color:#000000;padding:10px 40px 40px 40px;">'
         + g['btn']('SHOP 70% OFF + 10% OFF', L(SALE, 'bottom-btn'))
         + '<div style="font-family:Inter,Arial,Helvetica,sans-serif;font-size:13px;line-height:19px;color:#BDB8B0;text-align:center;padding-top:12px;">Extra 10% already applied (code BFEXTRA10) &middot; 30-day returns &middot; 75-year warranty &middot; 100,000+ customers</div></td></tr>\n')
h = g['shell']('Extra 10% off everything', 'On top of up to 70% off. Today only.', body)
# header/footer-links ook via de code
h = re.sub(r'href="(https://siraatskitchen\.com)(/[^"?]*)?(\?[^"]*)?"',
           lambda m: m.group(0) if 'discount/' in m.group(0) else f'href="{SITE}/discount/BFEXTRA10?redirect={m.group(2) or SALE}&utm_source=klaviyo&utm_medium=email&utm_campaign=bf-1127-intl-0800&utm_content=nav"', h)
assert '—' not in h and '$' not in re.sub(r'\{\{.*?\}\}|\{%.*?%\}', '', h)
open(os.path.join(C, 'intl-0800-bfextra10.html'), 'w').write(h)
pv = h
for t in ['{% unsubscribe_link %}', '{% manage_preferences_link %}', '{% web_view_link %}']: pv = pv.replace(t, '#')
pv = re.sub(r'\{%.*?%\}', '', pv).replace('{{ organization.name }}', 'Siraats Kitchen').replace('{{ organization.full_address }}', 'Address').replace('{{ sk_ref }}', '')
open(os.path.join(T, '.preview', 'intl-0800-bfextra10.html'), 'w').write(pv)
print('ok', len(h))
