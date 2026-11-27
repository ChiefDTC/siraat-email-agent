"""US vr 27 nov 08:00 (vervangt HS Email 15 US): tekstbrief Benjamin, copy v4 uit ../us-0800-text-copy.md.
Links zonder code (aanname: automatische kortingen per product, US, tot middernacht ET). Op verzoek Floris 27 nov: platte tekst, geen header/logo/footer, alleen minimale afmeldregel.
Gebruik: python3 -I build_us_text.py"""
import os, re
T = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(T)
src = open(os.path.join(T, 'build.py')).read().split("os.makedirs(os.path.join(T, '.preview')")[0]
g = {'__file__': os.path.join(T, 'build.py')}; exec(src, g)
p, a, btn, row, signoff, shell, FIRST, MUTED, SANS, INK = (g[k] for k in ('p','p','btn','row','signoff','shell','FIRST','MUTED','SANS','INK'))
SITE = 'https://siraatskitchen.com'
def a(t, href): return f'<a href="{href}" style="color:#1155CC;text-decoration:underline;">{t}</a>'
def L(path, c): return f'{SITE}{path}?utm_source=klaviyo&utm_medium=email&utm_campaign=bf-1127-us-0800-text&utm_content={c}'
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
    p('It&rsquo;s Black Friday, and our store is going crazy. Orders keep coming in, and I should be the happiest guy in the world.') +
    p('But honestly? I&rsquo;m not happy yet.') +
    p('I read your messages, and one keeps coming back: &ldquo;I want one, but it&rsquo;s still too expensive.&rdquo; That one stays with me. It means someone is still cooking on a coating that&rsquo;s peeling, only because of the price.') +
    p('So today I&rsquo;m giving the biggest discount we have ever given. Not a little extra. The lowest prices Siraat has ever had, on top of Black Friday:') +
    head(f'{a("THE 12-PIECE SET", L(SET,"set-title"))}: an extra 23% off. <s>$649</s>, now $499.') +
    p('That&rsquo;s 76% off the regular price of $2,047. Here&rsquo;s what&rsquo;s inside:', pad='0 0 6px 0') + ul +
    p('About $83 a piece, lids included.') +
    head(f'{a("THE HAMMERED PAN PRO STANDARD (11&quot;)", L(STD,"std-title"))}: an extra 15% off. <s>$144</s>, now $122.40.') +
    head(f'{a("THE WOK PAN PRO", L(WOK,"wok-title"))} and {a("THE DEEP PAN PRO", L(DEEP,"deep-title"))}: an extra 10% off. From $107.10.') +
    p('Every discount is already applied when you tap a link in this email. No code needed.', pad='10px 0 14px 0') +
    p('If you ask me, take the set. It&rsquo;s the only way to get our hammered titanium pots. The pattern goes all the way into the pots, not just the pans.') +
    p(f'&#128073; {a("Get my 12-piece set for $499", L(SET, "button"))}', pad='4px 0 4px 0') +
    p('Already applied. Free shipping. 30-day returns. 100,000+ happy customers.', 14, 21, MUTED, '0 0 18px 0') +
    p(f'Or pick one pan: {a("Pan Pro Standard, $122.40", L(STD,"pick"))} &middot; {a("Wok Pan Pro", L(WOK,"pick"))} &middot; {a("Deep Pan Pro", L(DEEP,"pick"))}') +
    p('These prices end at midnight ET. After that I switch them off, because I can&rsquo;t keep them this low.') +
    signoff() +
    p(f'P.S. Every pan and pot has a pure titanium cooking surface with no coatings. Nothing to wear off, which is why it&rsquo;s covered for 75 years. {a("Get the set for $499", L(SET,"ps"))}.', 15, 23, MUTED, '18px 0 0 0'))
PRE = 'An extra 23% off the 12-piece set, on top of Black Friday. Ends at midnight.' + '&#847;&zwnj;&nbsp;' * 60
foot = p('Siraats Kitchen &middot; {{ organization.full_address }}<br><a href="{% unsubscribe_link %}" style="color:#6B6660;">Unsubscribe</a> &middot; <a href="{% manage_preferences_link %}" style="color:#6B6660;">Preferences</a>', 12, 18, MUTED, '28px 0 0 0')
h = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The biggest discount we&rsquo;ve ever given</title></head>
<body style="margin:0;padding:0;background:#FFFFFF;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;">{PRE}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF"><tr><td align="center" style="padding:0;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;"><tr><td style="padding:24px 20px 32px 20px;">
{body}{foot}
</td></tr></table></td></tr></table></body></html>'''
assert '—' not in h and '80%' not in h
open(os.path.join(C, 'us-0800-text.html'), 'w').write(h)
pv = h.replace(FIRST, 'Sarah')
for t in ['{% unsubscribe_link %}', '{% manage_preferences_link %}', '{% web_view_link %}']: pv = pv.replace(t, '#')
pv = re.sub(r'\{%.*?%\}', '', pv).replace('{{ organization.name }}', 'Siraats Kitchen').replace('{{ organization.full_address }}', 'Address').replace('{{ sk_ref }}', '')
os.makedirs(os.path.join(T, '.preview'), exist_ok=True)
open(os.path.join(T, '.preview', 'us-0800-text.html'), 'w').write(pv)
print('ok', len(h))
