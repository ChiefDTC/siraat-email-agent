"""Mailblok-demo's voor de drie gift-card-varianten (research/giftcard/01-presentatie.md).
Gebruik: python3 -I research/giftcard/make_demo.py  (daarna node scripts/qa_mail_shots.js demo/jobs.json demo/res.json)
Vaste header en footer uit klaviyo/templates/partials/. Bedrag, naam en afzender zijn live tekst (in Klaviyo een
profiel- of eventveld), geen code in de mail: XXXXXXXX."""
import os, re
from PIL import Image
R = '/home/user/siraat-email-agent/'
G = R + 'research/giftcard/'
D = G + 'demo/'
os.makedirs(D, exist_ok=True)
P = R + 'klaviyo/templates/partials/'
SHARED = os.path.relpath(P + 'shared', D)
IMG = os.path.relpath(R + 'klaviyo/templates/v3/welcome/assets', D)
CREAM = (248, 247, 242)

def flat(src, out, w=1100):
    im = Image.open(G + src).convert('RGBA')
    bb = im.getchannel('A').getbbox(); im = im.crop(bb)
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    bg = Image.new('RGB', im.size, CREAM); bg.paste(im, (0, 0), im)
    bg.save(D + out, quality=80, optimize=True, progressive=True)
    print(out, bg.size, os.path.getsize(D + out) // 1024, 'KB')

flat('v1-goud-echt-lockup.png', 'card-v1.jpg')
flat('v2-titanium.png', 'card-v2.jpg')
Image.open(G + 'v3-titanium-plat.jpg').resize((1100, 678), Image.LANCZOS).save(D + 'card-v3-bg.jpg', quality=80, optimize=True)
Image.open(G + 'v3-titanium-50.jpg').resize((1100, 678), Image.LANCZOS).save(D + 'card-v3-50.jpg', quality=80, optimize=True)

def part(name):
    s = open(P + name).read().replace('{{SHARED}}', SHARED).replace('{{IMG}}', IMG)
    return s
STYLE = open(P + 'blocks/_style.css').read()
CTA = open(P + 'blocks/cta.html').read()
def cta(label, url, sub):
    return CTA.replace('[[pad]]', '22px 44px 6px 44px').replace('[[label]]', label).replace('[[url]]', url).replace('[[sub]]', sub)
SUB = "<div style='font-family:Inter,Arial,Helvetica,sans-serif;font-size:12px;line-height:18px;color:#727272;padding-top:10px;'>Delivered by email. Spend it on anything in the shop.</div>"
URL = 'https://siraatskitchen.com/products/e-gift-card'

def live_strip(amount, name, note):
    # Live tekst onder het beeld: werkt in elke client en in dark mode (eigen bgcolor op de tabel).
    return f'''<tr><td class="pad" style="padding:0 44px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid #ECE7DD;">
<tr><td align="center" style="padding:18px 20px 4px 20px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:11px;line-height:14px;letter-spacing:2px;font-weight:600;color:#AC3B19;">FOR {name.upper()}</td></tr>
<tr><td align="center" style="padding:0 20px 2px 20px;font-family:'Instrument Serif','Times New Roman',serif;font-style:italic;font-size:44px;line-height:48px;color:#282828;">{amount}</td></tr>
<tr><td align="center" style="padding:0 20px 18px 20px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:14px;line-height:21px;color:#727272;">{note}</td></tr>
</table></td></tr>'''

def img_row(src, alt, pad='26px 28px 14px 28px'):
    return f'<tr><td class="pad" align="center" style="padding:{pad};"><a href="{URL}"><img src="{src}" width="544" alt="{alt}" style="display:block;width:100%;max-width:544px;height:auto;border:0;margin:0 auto;"></a></td></tr>'

def bg_card(name, amount):
    # Variant C: titanium kaart als achtergrond, bedrag en naam live erover (bulletproof background + VML).
    return f'''<tr><td class="pad" align="center" style="padding:26px 28px 14px 28px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:544px;"><tr>
<td background="card-v3-bg.jpg" bgcolor="#C9C6C0" valign="top" style="background-color:#C9C6C0;background-image:url('card-v3-bg.jpg');background-size:cover;background-position:center;border-radius:14px;">
<!--[if gte mso 9]><v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width:544px;height:335px;"><v:fill type="frame" src="card-v3-bg.jpg" color="#C9C6C0"/><v:textbox inset="0,0,0,0"><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
<tr><td height="150" style="height:150px;font-size:0;line-height:0;">&nbsp;</td></tr>
<tr><td align="center" style="padding:0 16px 0 70px;font-family:'Instrument Serif','Times New Roman',serif;font-style:italic;font-size:56px;line-height:60px;color:#282828;">{amount}</td></tr>
<tr><td align="center" style="padding:6px 16px 34px 70px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:13px;line-height:18px;letter-spacing:1.5px;font-weight:600;color:#282828;">FOR {name.upper()} &middot; FROM BENJAMIN</td></tr>
</table>
<!--[if gte mso 9]></v:textbox></v:rect><![endif]-->
</td></tr></table></td></tr>'''

def intro(h, p):
    return f'''<tr><td class="pad" align="center" style="padding:30px 44px 0 44px;font-family:'Instrument Serif','Times New Roman',serif;font-style:italic;font-size:34px;line-height:38px;color:#282828;">{h}</td></tr>
<tr><td class="pad" align="center" style="padding:12px 44px 0 44px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:16px;line-height:25px;color:#282828;">{p}</td></tr>'''

def mail(title, body):
    return f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light only"><meta name="supported-color-schemes" content="light only"><title>{title}</title>
<style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Instrument+Serif:ital@1&display=swap');
:root{{color-scheme:light only;}} body{{margin:0;padding:0;background:#FFFFFF;}} img{{border:0;display:block;}}
{STYLE}
@media only screen and (max-width:620px){{.pad{{padding-left:20px!important;padding-right:20px!important;}}}}</style></head>
<body style="margin:0;padding:0;background-color:#FFFFFF;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF"><tr><td align="center" style="padding-top:8px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="#F8F7F2" style="width:100%;max-width:600px;background-color:#F8F7F2;">
{part('header.html')}
{body}
{part('footer.html')}
</table></td></tr></table></body></html>'''

INTRO = intro('A gift for Anna.', 'Every Siraat pan has a pure titanium cooking surface and no coatings. Anna picks the pan and the size.')
NOTE = 'From Benjamin. Delivered by email, spend it on anything in the shop.'
V = {
 'v1': INTRO + img_row('card-v1.jpg', 'Siraat gift card') + live_strip('$50', 'Anna', NOTE) + cta('Send a gift card', URL, SUB),
 'v2': INTRO + img_row('card-v2.jpg', 'Siraat gift card') + live_strip('$50', 'Anna', NOTE) + cta('Send a gift card', URL, SUB),
 'v3': INTRO + bg_card('Anna', '$50') + cta('Send a gift card', URL, SUB),
 'v3s': INTRO + img_row('card-v3-50.jpg', 'Siraat gift card, $50') + cta('Send a gift card', URL, SUB),
}
jobs = []
for k, b in V.items():
    open(D + f'{k}.html', 'w').write(mail('Siraat gift card ' + k, b))
    for mode in ('light', 'forced'):
        jobs.append({'key': f'{k}-{mode}', 'html': D + f'{k}.html', 'width': 375, 'mode': mode, 'shot': D + f'{k}-375-{mode}.png', 'net': False})
import json; json.dump(jobs, open(D + 'jobs.json', 'w'), indent=1)
print('ok', len(jobs), 'jobs')
