"""US za 28 nov 10:00 (vervangt HS Resend 3 E16 US, niet-openers), afgeleid van US vr 27 nov 08:00 (vervangt HS Email 15 US): tekstbrief Benjamin, copy v4 uit ../us-0800-text-copy.md.
Links met code per product (BF499, PANPRO15, WOKDEEP10), alleen via de mail. Op verzoek Floris 27 nov: platte tekst, geen header/logo/footer, alleen minimale afmeldregel.
Gebruik: python3 -I build_us_text.py"""
import os, re
T = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(T)
src = open(os.path.join(T, 'build.py')).read().split("os.makedirs(os.path.join(T, '.preview')")[0]
g = {'__file__': os.path.join(T, 'build.py')}; exec(src, g)
p, a, btn, row, signoff, shell, FIRST, MUTED, SANS, INK = (g[k] for k in ('p','p','btn','row','signoff','shell','FIRST','MUTED','SANS','INK'))
SITE = 'https://siraatskitchen.com'
def a(t, href): return f'<a href="{href}" style="color:#1155CC;text-decoration:underline;">{t}</a>'
CODE = {'/products/titanium-hammered-cookware-set': 'BF499', '/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern': 'PANPRO15',
        '/products/titanium-hammered-wok-pan-pro': 'WOKDEEP10', '/products/titanium-hammered-deep-pan-pro': 'WOKDEEP10'}
def L(path, c): return f'{SITE}/discount/{CODE[path]}?redirect={path}&utm_source=klaviyo&utm_medium=email&utm_campaign=bf-1128-us-text-nonopeners&utm_content={c}'
SET = '/products/titanium-hammered-cookware-set'
STD = '/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern'
WOK = '/products/titanium-hammered-wok-pan-pro'
DEEP = '/products/titanium-hammered-deep-pan-pro'
def head(t): return p(f'<b>{t}</b>', pad='10px 0 6px 0')
items = ['8&quot; frying pan with lid', '10&quot; frying pan with lid', '12&quot; frying pan with lid',
         '2-quart saucepan with lid', '3-quart saucepan with lid', 'Stockpot with lid']
ul = ''.join(f'<tr><td valign="top" style="font-family:{SANS};font-size:17px;line-height:26px;color:{INK};padding:0 8px 0 4px;">&bull;</td>'
             f'<td style="font-family:{SANS};font-size:17px;line-height:26px;color:{INK};">{i}</td></tr>' for i in items)
ul = f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 10px 0;">{ul}</table>'
body = (p(f'Hey {FIRST},') +
    p('Quick one. On Black Friday I dropped our 12-piece set to $499. The biggest discount we&rsquo;ve ever given, and a lot of you grabbed it.') +
    p('So I kept it on for one more day. It ends today at midnight ET, then it goes back to $649.') +
    head(f'{a("THE 12-PIECE SET", L(SET,"set-title"))}: <s>$649</s>, now $499.') +
    p('That&rsquo;s an extra 23% off, and 76% off the regular price of $2,047. Here&rsquo;s what&rsquo;s inside:', pad='0 0 6px 0') + ul +
    p('About $83 a piece, lids included. And it&rsquo;s the only way to get our hammered titanium pots.') +
    p(f'&#128073; {a("Get my 12-piece set for $499", L(SET, "button"))}', pad='4px 0 4px 0') +
    p('Already applied. Not showing? Use code BF499 at checkout. Free shipping. 30-day returns. 100,000+ happy customers.', 14, 21, MUTED, '0 0 18px 0') +
    signoff() +
    p(f'P.S. Every pan and pot has a pure titanium cooking surface with no coatings. Nothing to wear off, which is why it&rsquo;s covered for 75 years. {a("The $499 ends today at midnight ET", L(SET,"ps"))}.', 15, 23, MUTED, '18px 0 0 0'))
PRE = 'It ends today.' + '&#847;&zwnj;&nbsp;' * 60
foot = p('Siraats Kitchen &middot; {{ organization.full_address }}<br><a href="{% unsubscribe_link %}" style="color:#6B6660;">Unsubscribe</a> &middot; <a href="{% manage_preferences_link %}" style="color:#6B6660;">Preferences</a>', 12, 18, MUTED, '28px 0 0 0')
h = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The 12-piece set is still $499</title></head>
<body style="margin:0;padding:0;background:#FFFFFF;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;">{PRE}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF"><tr><td align="center" style="padding:0;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;"><tr><td style="padding:24px 20px 32px 20px;">
{body}{foot}
</td></tr></table></td></tr></table></body></html>'''
assert '—' not in h and '80%' not in h
open(os.path.join(C, 'us-1128-text.html'), 'w').write(h)
pv = h.replace(FIRST, 'Sarah')
for t in ['{% unsubscribe_link %}', '{% manage_preferences_link %}', '{% web_view_link %}']: pv = pv.replace(t, '#')
pv = re.sub(r'\{%.*?%\}', '', pv).replace('{{ organization.name }}', 'Siraats Kitchen').replace('{{ organization.full_address }}', 'Address').replace('{{ sk_ref }}', '')
os.makedirs(os.path.join(T, '.preview'), exist_ok=True)
open(os.path.join(T, '.preview', 'us-1128-text.html'), 'w').write(pv)
print('ok', len(h))
