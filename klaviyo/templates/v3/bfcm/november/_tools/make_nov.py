"""November meer output (1 nov 2026): maakt de bronmails in bfcm/november uit de bestaande BF-templates (signup, lifecycle) plus nieuwe brieven.
Gebruik: python3 -I make_nov.py   (schrijft alleen in bfcm/november). Daarna render_nov.py voor build, Django-render en checks.
Voorraadregels: Shopify 1 nov ~15:00 UTC (zie research/smooche/05-designs-november.md). Wekelijks controleren."""
import os, re
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BF = os.path.dirname(N)
rd = lambda p: open(os.path.join(BF, p)).read()

SALE_END = 'Monday, November 30'
END_TIME = 'midnight PT'          # [VRAAG FLORIS] exacte tijd en tijdzone
HL = lambda t: '<span style="background-color:#FFE38A;color:#272727;padding:0 3px;">%s</span>' % t  # open punt zichtbaar in concept

# Voorraadblok: US en niet-US (12-delige set alleen US). Drempels kloppen op 1 nov; geen exacte aantallen.
def stock(pad, bg, eyebrow='STOCK CHECK', note=None):
    note = note or 'Stock moves daily during the sale. Up to 70%% off until %s.' % SALE_END
    common = ('t2="SELLING FAST" c2="#C8202A" f2="#FFFFFF" d2="<b>Wok Pan Pro {{SIZE:24}} and {{SIZE:28}}:</b> fewer than 100 left of each. <b>Pan Pro Mini:</b> fewer than 200 left." '
              't3="IN STOCK" c3="#3A3A3A" f3="#FFFFFF" d3="<b>Pan Pro Standard, Small and Large:</b> plenty in stock." note="%s"' % note)
    b = '{{BLOCK:bf-stock pad="%s" bg="%s" eyebrow="%s" t1="NEXT BATCH" c1="#FFB800" f1="#272727" d1="%s" %s}}'
    us = b % (pad, bg, eyebrow, '<b>Pan Set, 6 Pcs, Cookware Set, 12 Pcs and Pan Pro Duo:</b> the current batch is sold out. Orders now reserve yours from the next shipment, expected {{NEXT_BATCH_DATE}}.', common)
    intl = b % (pad, bg, eyebrow, '<b>Pan Set, 6 Pcs and Pan Pro Duo:</b> the current batch is sold out. Orders now reserve yours from the next shipment, expected {{NEXT_BATCH_DATE}}.', common)
    return '{{USONLY}}\n%s\n{{ELSEUS}}\n%s\n{{/USONLY}}' % (us, intl)

def head(meta, title, preheader, signal, extra_css=''):
    return '''<!--
NOVEMBER MEER OUTPUT (concept 1 nov 2026, niet in Klaviyo). Plan: research/smooche/04-meer-output-november.md. Designs: research/smooche/05-designs-november.md.
%s
-->
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>%s</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>
  @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&family=Inter:wght@400;500;600;800;900&display=swap');
  body{margin:0;padding:0;background:#FFFFFF;-webkit-text-size-adjust:100%%;}
  table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}
  img{border:0;display:block;line-height:100%%;outline:none;text-decoration:none;}
  a{color:#272727;}
  @media only screen and (max-width:620px){
    .w{width:100%%!important;}
    .pad{padding-left:22px!important;padding-right:22px!important;}
    .h1{font-size:34px!important;line-height:37px!important;}
    .navhide{display:none!important;}
    .lead{font-size:16px!important;line-height:25px!important;}
    .bfh{font-size:38px!important;line-height:44px!important;padding-left:16px!important;padding-right:16px!important;}%s
  }
</style>
</head>
<body style="margin:0;padding:0;background:#FFFFFF;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">%s</div>
<!-- MARKET-SIGNAL: %s -->
<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF">
<tr><td align="center" style="padding:8px 0 32px 0;">
''' % (meta.strip(), title, extra_css, preheader, signal)

TAIL = '''
{{FOOTER}}

</table>
</td></tr>
</table>
</body>
</html>
'''
OPEN = lambda bg: '<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:%s;" bgcolor="%s">\n\n' % (bg, bg)
P = lambda txt, pad='0 44px 18px 44px', color='#282828', size='16px;line-height:26px': '<tr><td class="pad lead" style="padding:%s;font-family:Inter,Arial,Helvetica,sans-serif;font-size:%s;color:%s;">%s</td></tr>\n' % (pad, size, color, txt)
SIGN_CREAM = '<tr><td class="pad" style="padding:6px 44px 30px 44px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#282828;">Benjamin<br><span style="color:#727272;font-size:14px;">Founder, Siraat</span></td></tr>\n'
SIGN_DARK = '<tr><td class="pad lead" align="left" bgcolor="#0E0E0E" style="background-color:#0E0E0E;padding:6px 40px 34px 40px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#E6E3DC;text-align:left;"><b style="font-weight:800;color:#FFFFFF;">Benjamin</b><br><span style="font-size:13px;color:#9E998F;">Founder, Siraat</span></td></tr>\n'
DARKP = lambda txt, pad='0 40px 22px 40px', color='#E6E3DC', extra='': '<tr><td class="pad lead" align="left" bgcolor="#0E0E0E" style="background-color:#0E0E0E;padding:%s;font-family:Inter,Arial,Helvetica,sans-serif;font-size:16px;line-height:25px;color:%s;text-align:left;%s">%s</td></tr>\n' % (pad, color, extra, txt)
SUB = lambda t, c='#BDB8AE': "<div style='font-family:Inter,Arial,Helvetica,sans-serif;font-size:12px;line-height:18px;color:%s;padding-top:14px;'>%s</div>" % (c, t)
SALE = 'https://siraatskitchen.com/collections/black-friday-sale'
def utm(url, camp, content):
    return url + ('&' if '?' in url else '?') + 'utm_source=klaviyo&utm_medium=email&utm_campaign=%s&utm_content=%s' % (camp, content)

files = {}

# Sold-beyond-stock items, zoals ze in de eventtitels heten (catalogus): 6-Pcs set, 12-Pcs set, Pan Pro Duo, Pan Pro & Utensil Set
SETCHK = lambda src: "{%% if '6-Pcs' in %s or '12-Pcs' in %s or 'Pan Pro Duo' in %s or 'Utensil Set' in %s %%}" % (src, src, src, src)
BATCH_NOTE = '''<tr><td class="pad" style="padding:4px 44px 18px 44px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="#FFB800" style="background-color:#FFB800;padding:12px 14px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:#272727;"><b style="font-weight:800;">NEXT BATCH.</b> The current batch of your set is sold out. Ordering now reserves yours from the next shipment, expected {{NEXT_BATCH_DATE}}.</td></tr></table></td></tr>
'''

# ---------- 1. C1b checkout +1 uur ----------
CO = "{{ event.extra.responsive_checkout_url|default:'https://siraatskitchen.com/discount/BFCODE?redirect=/cart' }}&discount=BFCODE&utm_source=klaviyo&utm_medium=email&utm_campaign=v4-checkout&utm_content=c1b-%s"
items = "event.Items|join:','"
meta = '''ID: nov-c1b · C1b checkout, tweede contact dag 0
SENDER: Benjamin from Siraat (reply-to gelezen inbox)
SUBJECT A: Your Black Friday cart is saved
SUBJECT B: Benjamin here, about your cart
  Alternatieven: "Something stop you at checkout?" · "Your extra 10% is still on it" · "One tap left, at Black Friday prices"
PREVIEW: Your extra 10% is still on it, and so are your 4 gifts.
TRIGGER/TIMING: v4 · Checkout abandonment QUBUQV, nieuwe stap na C1: wacht 1 uur na de trigger (50 min na C1). Smart Sending uit (zoals C1).
FILTERS: Placed Order = 0 sinds flowstart; minder dan 3 Received Email in de laatste 1 dag; niet geklikt op C1 in de laatste 50 min (optioneel, test); geen BFCODE-mail uit de cart-flow in de laatste 1 uur.
WAAROM: plan 04 punt 2 (C1 $7,96 per ontvanger; Smooche 3 mails in 90 min). Schatting $4.000 a $5.000 in november.
AANBOD: up to 70% off + extra 10% met BFCODE (placeholder), 4 gifts. Geen nep-order of nep-deadline.
PLACEHOLDER: {{NEXT_BATCH_DATE}} alleen zichtbaar als er een uitverkochte set in de checkout zit (6-Pcs, 12-Pcs, Pan Pro Duo, Pan Pro & Utensil Set).'''
b = head(meta, 'Your Black Friday cart is saved', 'Your extra 10% is still on it, and so are your 4 gifts.', 'checkout')
b += OPEN('#F8F7F2') + '{{BLOCK:bf-topbar text="BLACK FRIDAY SALE IS LIVE"}}\n{{HEADER}}\n'
b += P("Hi {{ first_name|default:'there' }},", '34px 44px 14px 44px')
b += P("Benjamin here. You got to the last step about an hour ago, so I kept your cart for you, at Black Friday prices.", '0 44px 4px 44px')
b += '{{BLOCK:cart pad="18px 44px 4px 44px" title="YOUR CART, SAVED" line="Your extra 10% is applied with the button. Or use code BFCODE at checkout."}}\n'
b += SETCHK(items) + '\n' + BATCH_NOTE + '{% endif %}\n'
b += '{{BLOCK:bf-cta bg="#F8F7F2" label="Complete my order" url="%s" pad="14px 44px 26px 44px" sub="%s"}}\n' % (CO % 'cta1', SUB('{{FRICTION}}', '#727272'))
b += P("Every order ships with {{GIFTS:total}}. Changed your mind later? Send it back unused within 30 days. Something wrong with it? It's covered for 75 years.")
b += P("If something stopped you, a size question, the price, anything at all, just reply. Our team will help.", '0 44px 18px 44px')
b += SIGN_CREAM + TAIL
files['nov-c1b'] = b

# ---------- 2. K1b cart +3 uur ----------
CART = 'https://siraatskitchen.com/discount/BFCODE?redirect=/cart%%3Futm_source%%3Dklaviyo%%26utm_medium%%3Demail%%26utm_campaign%%3Dv4-cart%%26utm_content%%3Dk1b-%s'
pn = "event|lookup:'Product Name'"
meta = '''ID: nov-k1b · K1b cart, tweede contact dag 0
SENDER: Benjamin from Siraat (reply-to gelezen inbox)
SUBJECT A: Your cart, still at Black Friday prices
SUBJECT B: Still thinking it over?
  Alternatieven: "Benjamin here. Your cart is still open." · "Which pan did you pick?" · "An extra 10% on the cart you left"
PREVIEW: Benjamin here. An extra 10% is applied with the button, on top of up to 70% off.
TRIGGER/TIMING: v4 · Cart abandonment TZG9Mx, nieuwe stap na K1: wacht 3 uur na de trigger. Smart Sending aan.
FILTERS: Placed Order = 0 sinds flowstart; Started Checkout = 0 sinds flowstart (checkout-flow neemt over); minder dan 3 Received Email in de laatste 1 dag.
WAAROM: plan 04 punt 4 (K1 $3,59 per ontvanger, tweede dag-0-contact ontbreekt). Schatting $2.000 a $3.000.
EVENT: Added to Cart: Product Name, ImageURL, Quantity (zoals k1-v2-bf). Prijs bewust weggelaten (BF-prijs en code in de cart).'''
b = head(meta, 'Your cart, still at Black Friday prices', 'Benjamin here. An extra 10% is applied with the button, on top of up to 70% off.', 'cart')
b += OPEN('#F8F7F2') + '{{BLOCK:bf-topbar text="BLACK FRIDAY SALE IS LIVE"}}\n{{HEADER}}\n'
b += P("Hi {{ first_name|default:'there' }},", '34px 44px 14px 44px')
b += P("Benjamin here. You left this in your cart earlier today. It's still there, at Black Friday prices, and the button below takes an extra 10% off on top.", '0 44px 4px 44px')
b += '''<tr><td class="pad" style="padding:18px 44px 4px 44px;">
  <table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid #ECE7DD;">
    <tr><td bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:16px 16px 12px 16px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:11px;line-height:14px;letter-spacing:2px;font-weight:800;color:#272727;">STILL IN YOUR CART</td></tr>
    <tr><td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:0 16px;"><a href="%s"><img src="{%% if event.ImageURL %%}{{ event.ImageURL }}&width=1000{%% else %%}{{IMG}}/cart-fallback.jpg{%% endif %%}" width="478" alt="{{ event|lookup:'Product Name'|default:'Your item' }}" style="display:block;width:100%%;max-width:{%% if event.ImageURL %%}478{%% else %%}264{%% endif %%}px;height:auto;border:0;background-color:#F8F7F2;"></a></td></tr>
    <tr><td bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:16px 16px 4px 16px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:18px;line-height:24px;font-weight:600;color:#282828;word-break:break-word;">{{ event|lookup:'Product Name'|default:'Your item' }}</td></tr>
    <tr><td bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:0 16px 16px 16px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:#727272;">Qty {{ event.Quantity|default:1|floatformat:0 }} &middot; Extra 10%% off with the button</td></tr>
  </table>
</td></tr>
''' % (CART % 'product')
b += SETCHK(pn) + '\n' + BATCH_NOTE + '{% endif %}\n'
b += '{{BLOCK:bf-cta bg="#F8F7F2" label="Return to my cart" url="%s" pad="14px 44px 26px 44px" sub="%s"}}\n' % (CART % 'cta1', SUB('{{FRICTION}}', '#727272'))
b += P("One thing people ask me: does titanium really work without a coating? It does, with heat. Medium heat for 2 to 3 minutes, then a teaspoon of oil. Cold metal grabs your food. Hot metal lets it go.")
b += P("Every order ships with {{GIFTS:total}}, and you have 30 days to send it back unused. Questions about size? Reply and our team will help.", '0 44px 18px 44px')
b += SIGN_CREAM + TAIL
files['nov-k1b'] = b

# ---------- 3. W1b welcome +3 uur (hergebruik signup/bf-w1b) ----------
w = rd('signup/bf-w1b.html')
body = w[w.index('<table role="presentation" class="w"'):w.index('{{FOOTER}}')]
body = body.replace('{{BLOCK:bf-cta label="See the whole sale"', stock('6px 20px 26px 20px', '#0E0E0E') + '\n{{BLOCK:bf-cta label="See the whole sale"')
body = body.replace('Quick note from Benjamin.', 'Quick note from me, Benjamin.')
meta = '''ID: nov-w1b · W1b welcome, tweede contact dag 0 (bron: signup/bf-w1b.html, ongewijzigd behalve het voorraadblok)
SENDER: Benjamin from Siraat
SUBJECT A: Up to 70% off is still waiting
SUBJECT B: The short version
  Alternatieven: "Pans or sets?" · "Still deciding? Start here." · "Three picks, no code needed"
PREVIEW: The short version: three picks, up to 70% off, no code needed.
TRIGGER/TIMING: v4 · Welcome T4a5Mk (gewone groep, na W1) en Rn556d (BF-groep, na BF-W1): wacht 3 uur na W1. Smart Sending aan.
FILTERS: Placed Order = 0 sinds flowstart; Started Checkout = 0 in de laatste 3 uur; geen mail uit checkout- of cart-flow in de laatste 1 dag; minder dan 3 Received Email in de laatste 1 dag; holdout 20% (random sample split).
WAAROM: plan 04 punt 3 (W1 $2,74, daarna niets tot de volgende ochtend). Schatting $5.000 a $12.000.'''
files['nov-w1b'] = head(meta, 'Up to 70% off is still waiting', 'The short version: three picks, up to 70% off, no code needed.', 'profile') + body + TAIL.lstrip('\n')

# ---------- 4. BF-W2 dag 1 (BF-groep Rn556d; brief van 54 woorden uit lifecycle/w2-bf + voorraad) ----------
meta = '''ID: nov-bf-w2 · BF-groep (Rn556d) dag 1. Bron: lifecycle/w2-bf.html (W2 ingekort tot 54 woorden, 31 okt). Zelfde verhaal, plus een eerlijke voorraadregel.
SENDER: Benjamin from Siraat (reply-to gelezen inbox)
SUBJECT A: The pan nobody else was making
SUBJECT B: A note from Benjamin (and the sets)
  Alternatieven: "December 20, 2024" · "Why I made a pan with no coating" · "Our sets are going faster than planned"
PREVIEW: It's Benjamin. A short note, and a heads-up about the sets.
TRIGGER/TIMING: flow Rn556d (BF-groep 25%), stap na BF-W1: wacht 1 dag tot 10:00 (profieltijdzone), zoals W2 in T4a5Mk. Alternatief: exit-split 119850651 in T4a5Mk zo aanpassen dat de BF-groep alleen W1 overslaat (dan lifecycle/w2-bf zelf). Smart Sending uit (zoals W2).
FILTERS: Placed Order = 0 sinds flowstart; geen Received Email uit checkout- of cart-flow in de laatste 1 dag (overslaan, niet uitstappen); minder dan 3 Received Email in de laatste 1 dag.
WAAROM: plan 04 punt 1 (BF-groep krijgt na BF-W1 niets meer; W2 $0,54 per ontvanger).'''
b = head(meta, 'The pan nobody else was making', 'It&rsquo;s Benjamin. A short note, and a heads-up about the sets.', 'profile')
b += OPEN('#F8F7F2') + '{{BLOCK:bf-topbar text="BLACK FRIDAY SALE IS LIVE"}}\n{{HEADER}}\n'
b += P("Hi {{ first_name|default:'there' }},", '34px 44px 18px 44px')
b += P("It&rsquo;s Benjamin, founder of Siraat. Thanks for joining yesterday.")
b += P('I made our pan because I didn&rsquo;t want PFAS coatings in my kitchen. Pure titanium, nothing to wear off, covered for 75 years. Lab tested: <a href="https://siraatskitchen.com/pages/third-party-testing?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign=bf-nov&amp;utm_content=bfw2-report" style="color:#272727;">Light Labs report no. 25895</a>.')
b += P("One heads-up. Our sets are going faster than we planned. The current batch is gone, so a set ordered today is reserved from the next shipment. The pans themselves are in stock.")
b += P("Our Black Friday Sale is live: up to 70% off, no code needed.", '0 44px 6px 44px')
b += SIGN_CREAM
b += stock('6px 44px 6px 44px', '#F8F7F2')
b += '{{BLOCK:bf-cta label="Shop the sale" url="%s" pad="22px 44px 4px 44px" bg="#F8F7F2" sub="%s"}}\n' % (utm(SALE, 'bf-nov', 'bfw2-cta'), SUB('{{FRICTION}}', '#727272'))
b += '{{BLOCK:gifts5 style="row" pad="14px 44px 34px 44px" line="Every order comes with {{GIFTS:total}}."}}\n' + TAIL
files['nov-bf-w2'] = b

# ---------- 5. BF-W3 dag 3 (hergebruik signup/bf-w3 + voorraad voor de sets) ----------
w = rd('signup/bf-w3.html')
body = w[w.index('<table role="presentation" class="w"'):w.index('{{FOOTER}}')]
body = body.replace('{{BLOCK:bf-sectionbar text="OR GET IT IN A SET"}}', stock('0 20px 30px 20px', '#0E0E0E', 'BEFORE YOU PICK A SET') + '\n{{BLOCK:bf-sectionbar text="OR GET IT IN A SET"}}')
meta = '''ID: nov-bf-w3 · BF-groep (Rn556d) dag 3. Bron: signup/bf-w3.html (Pan Pro Standard uitgediept, dan de sets), plus voorraadblok voor de sets.
SENDER: Siraat
SUBJECT A: Built to last. Priced for Black Friday.
SUBJECT B: Why there's nothing to wear off
  Alternatieven: "Cold metal grabs. Hot metal lets go." · "75 years of cover, Black Friday price" · "The pan is in stock. The sets are not."
PREVIEW: Nothing on it to wear off. That's why it's covered for 75 years.
TRIGGER/TIMING: flow Rn556d, na BF-W2: wacht 2 dagen tot 09:00. Smart Sending aan.
FILTERS: Placed Order = 0 sinds flowstart; geen mail uit checkout- of cart-flow in de laatste 1 dag; minder dan 3 Received Email in de laatste 1 dag.
WAAROM: plan 04 punt 1 (W3 $0,24 per ontvanger, bewijs plus sets).'''
files['nov-bf-w3'] = head(meta, 'Built to last. Priced for Black Friday.', 'Nothing on it to wear off. That&rsquo;s why it&rsquo;s covered for 75 years.', 'profile') + body + TAIL.lstrip('\n')

# ---------- 6. Stock alert (campagne, betrokken 90 dagen) ----------
CARD = lambda side, img, url, kicker, name, b1, b2, pad='0 20px 12px 20px', pill='UP TO 70% OFF': '{{BLOCK:bf-product side="%s" img="%s" url="%s" kicker="%s" name="%s" b1="%s" b2="%s" pad="%s" pill="%s" btn="SHOP IT"}}\n' % (side, img, url, kicker, name, b1, b2, pad, pill)
IMG = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/'
U_STD = 'https://siraatskitchen.com/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern'
U_SET6 = 'https://siraatskitchen.com/products/titanium-hammered-pan-set-with-lids-6-pcs'
U_WOK = 'https://siraatskitchen.com/products/titanium-hammered-wok-pan-pro'
meta = '''ID: nov-stock · Stock alert, campagne (nieuw concept, verzoek Floris 1 nov: meer urgentie rond voorraad, eerlijk)
SENDER: Benjamin from Siraat
SUBJECT A: Our sets sold out. Here's what that means.
SUBJECT B: A stock update from Benjamin
  Alternatieven: "The 6-piece set: first batch gone" · "What's left, and what's next" · "Wok Pan Pro: fewer than 100 left"
PREVIEW: The current batch of sets is gone. The pans are in stock. Up to 70% off until Monday, November 30.
TRIGGER/TIMING: campagne, voorstel di 17 of wo 18 nov 08:15 lokale tijd (Homestead-ritme), en alleen als de voorraadregels die ochtend nog kloppen.
DOELGROEP: Engaged 90 dagen (geopend of geklikt), uitgesloten: kopers laatste 14 dagen, BF-signupreeks dag 0 tot 3, ontvangers van een andere campagne in de laatste 16 uur. Smart Sending aan.
WAAROM: verzoek Floris 1 nov (voorraadurgentie). Voorraad Shopify 1 nov: 6-Pcs -627, Pan Pro Duo -452, 12-Pcs -8, Pan Pro & Utensil Set -96; Wok 24/26/28 cm 84/126/78; Mini 166; Standard 935, Large 518, Small 454.
REGEL: geen exacte aantallen, alleen drempels die op de verzenddag waar zijn. Opnieuw tellen op de ochtend van verzending.'''
b = head(meta, 'Our sets sold out', 'The current batch of sets is gone. The pans are in stock. Up to 70% off until Monday, November 30.', 'profile')
b += OPEN('#0E0E0E') + '{{BLOCK:bf-topbar text="STOCK UPDATE &middot; BLACK FRIDAY SALE" bg="#FFB800" color="#272727"}}\n{{HEADER}}\n'
b += '<tr><td bgcolor="#0E0E0E" style="background-color:#0E0E0E;padding:0;"><img src="%ssiraat-collection-exclusive-05-gallery-rail-desktop.jpg?width=1200" width="600" alt="Siraat titanium pans on a gallery rail" style="display:block;width:100%%;max-width:600px;height:auto;border:0;"></td></tr>\n' % IMG
b += '<tr><td align="center" class="pad" bgcolor="#0E0E0E" style="background-color:#0E0E0E;padding:30px 30px 0 30px;"><table role="presentation" align="center" cellpadding="0" cellspacing="0" border="0" style="margin:0 auto;"><tr><td bgcolor="#FFB800" style="background-color:#FFB800;padding:6px 10px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:11px;line-height:12px;letter-spacing:1.8px;font-weight:800;color:#272727;">STOCK UPDATE</td></tr></table></td></tr>\n'
b += '<tr><td align="center" class="pad bfh" bgcolor="#0E0E0E" style="background-color:#0E0E0E;padding:18px 24px 0 24px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:46px;line-height:52px;font-weight:900;letter-spacing:-1.4px;color:#FFFFFF;text-align:center;">Our sets<br><span style="background-color:#FFB800;color:#272727;padding:0 8px;">sold out.</span></td></tr>\n'
b += '<tr><td class="pad lead" align="center" bgcolor="#0E0E0E" style="background-color:#0E0E0E;padding:18px 36px 26px 36px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:17px;line-height:26px;color:#E6E3DC;text-align:center;">The current batch, that is. Here&rsquo;s what&rsquo;s left, and what&rsquo;s next.</td></tr>\n'
b += DARKP('Benjamin here, with an honest stock update. More of you picked a set this month than we planned for. The current batch is gone. You can still order one at the sale price: it&rsquo;s reserved for you from the next shipment, expected {{NEXT_BATCH_DATE}}.', '0 40px 16px 40px')
b += DARKP('The single pans are a different story. Most are in stock. Two are getting low, and I&rsquo;d rather tell you now than after.', '0 40px 22px 40px')
b += stock('0 20px 26px 20px', '#0E0E0E', 'WHERE THINGS STAND')
b += '{{BLOCK:bf-cta label="Shop the sale" url="%s" pad="4px 40px 30px 40px" sub="%s"}}\n' % (utm(SALE, 'bf-nov', 'stock-cta1'), SUB('No code needed. 30-day returns. 75-year warranty.'))
b += '{{BLOCK:bf-sectionbar text="IN STOCK, LOW, AND NEXT BATCH"}}\n<tr><td bgcolor="#0E0E0E" style="background-color:#0E0E0E;height:20px;line-height:20px;font-size:0;">&nbsp;</td></tr>\n'
b += CARD('left', IMG + 'siraat-bf-product-hammered-pan-pro-yellow.webp?width=800&format=pjpg', U_STD, 'IN STOCK', 'Pan Pro Standard', 'Pure titanium cooking surface. Zero coating.', 'Plenty in stock. The pan most people start with.')
b += CARD('right', IMG + 'siraat-bf-product-hammered-wok-pan-pro-yellow.webp?width=800&format=pjpg', U_WOK, 'SELLING FAST', 'Wok Pan Pro', 'Made for stir-fries, searing and tossing.', '{{SIZE:24}} and {{SIZE:28}}: fewer than 100 left of each.')
b += CARD('left', IMG + '6pcscookwareset.webp?width=600', U_SET6, 'NEXT BATCH', 'Pan Set with Lids, 6&nbsp;Pcs', '3 pans and 3 fitted lids.', 'Current batch sold out. Order now to reserve one from the next shipment.', '0 20px 30px 20px')
b += DARKP('Two promises, either way. Change your mind? Send it back unused within 30 days. Something wrong with it? It&rsquo;s covered for 75 years.', '0 40px 4px 40px')
b += '{{BLOCK:bf-cta label="Shop the sale" url="%s" pad="20px 40px 20px 40px"}}\n' % utm(SALE, 'bf-nov', 'stock-cta2')
b += SIGN_DARK + TAIL
files['nov-stock'] = b

# ---------- 7. Laatste dag (24 uur voor het einde) ----------
w = rd('signup/bf-last.html')
body = w[w.index('<table role="presentation" class="w"'):w.index('{{FOOTER}}')]
body = body.replace('LAST CALL &middot; ENDS [END DATE]', 'ENDS TOMORROW &middot; MONDAY, NOVEMBER 30')
body = body.replace('>LAST CALL</td>', '>ENDS TOMORROW</td>')
body = body.replace('Last call.<br><span style="background-color:#FFB800;color:#272727;padding:0 8px;">Ends [END DATE].</span>', 'One day<br><span style="background-color:#FFB800;color:#272727;padding:0 8px;">left.</span>')
body = body.replace('Then prices go back to normal.', 'The Black Friday Sale ends tomorrow, %s. Then prices go back to normal.' % SALE_END)
body = body.replace('Benjamin here, one last time this sale.', 'Benjamin here. One day left.')
body = re.sub(r'Black Friday prices end on <span[^>]*>\[END DATE\]</span> at <span[^>]*>\[END TIME \+ TIMEZONE\]</span>\.', 'Black Friday prices end tomorrow, %s, at %s. Two things to know before you decide: our sets are now ordered from the next batch, and the Wok Pan Pro is running low.' % (SALE_END, HL(END_TIME)), body)
body = body.replace("If you've been deciding between a pan and a set, these are the three I'd look at.", '')
body = body.replace('{{BLOCK:bf-sectionbar text="LAST CALL: MY 3 PICKS"}}', stock('0 20px 30px 20px', '#0E0E0E') + '\n{{BLOCK:bf-sectionbar text="ONE DAY LEFT: MY 3 PICKS"}}')
meta = '''ID: nov-last-day · Deadline 1, 24 uur voor het einde (bron: signup/bf-last.html, placeholders ingevuld)
SENDER: Siraat
SUBJECT A: Black Friday ends tomorrow
SUBJECT B: One day left: up to 70% off
  Alternatieven: "Ends Monday, November 30" · "Before prices go back" · "Pan or set? One day to decide."
PREVIEW: Up to 70% off until Monday, November 30 at midnight PT. Then prices go back to normal.
TRIGGER/TIMING: campagne zo 29 nov 18:00 lokale tijd (ca. 30 uur voor het einde voor US-oost, 24 uur voor PT), plus dezelfde mail als laatste stap in de BF-reeks (Rn556d) voor niet-kopers.
DOELGROEP: Engaged 60 dagen + abandoners 30 dagen (Started Checkout of Added to Cart, geen order), uitgesloten kopers laatste 7 dagen. Smart Sending aan (8 uur in BF-week).
WAAROM: plan 04 punt 6 (echte deadline-mails, $10.000 a $20.000 netto voor beide). Einde: Monday, November 30 (Floris 1 nov). [VRAAG FLORIS] klok en tijdzone, nu "midnight PT".'''
files['nov-last-day'] = head(meta, 'Black Friday ends tomorrow', 'Up to 70% off until Monday, November 30 at midnight PT. Then prices go back to normal.', 'profile') + body + TAIL.lstrip('\n')

# ---------- 8. Final hours (laatste dag, brief) ----------
meta = '''ID: nov-final-hours · Deadline 2, laatste uren (korte brief van Benjamin in BF-stijl, geen hero)
SENDER: Benjamin from Siraat
SUBJECT A: Final hours
SUBJECT B: Tonight at midnight PT, prices go back
  Alternatieven: "The sale ends tonight" · "Last email about Black Friday" · "Benjamin here, one last time"
PREVIEW: The Black Friday Sale ends tonight at midnight PT. This is my last email about it.
TRIGGER/TIMING: campagne ma 30 nov 14:00 PT op een vaste tijd voor iedereen (niet lokale tijd, het einde is overal hetzelfde moment), US-lijst. INT apart: ma 30 nov 09:00 lokale tijd met dezelfde mail (einde = di ochtend in Europa, de copy noemt "Monday at midnight PT" zonder "tonight" voor INT via IF:US).
DOELGROEP: klikkers 30 dagen + abandoners 14 dagen zonder order, uitgesloten kopers sinds 27 nov. Smart Sending aan (8 uur).
WAAROM: plan 04 punt 6. Echte deadline: alleen als Floris het einde bevestigt. Geen afteller (kan later met echte eindtijd).'''
b = head(meta, 'Final hours', 'The Black Friday Sale ends tonight at midnight PT. This is my last email about it.', 'profile')
b += OPEN('#0E0E0E') + '{{BLOCK:bf-topbar text="FINAL HOURS &middot; ENDS MONDAY, NOVEMBER 30" bg="#FFB800" color="#272727"}}\n{{HEADER}}\n'
b += '<tr><td class="pad h1" bgcolor="#0E0E0E" style="background-color:#0E0E0E;padding:38px 40px 14px 40px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:46px;line-height:50px;font-weight:900;letter-spacing:-1.4px;color:#FFFFFF;">Final<br><span style="background-color:#FFB800;color:#272727;padding:0 6px;">hours.</span></td></tr>\n'
b += DARKP("Hi {{ first_name|default:'there' }}, Benjamin here.", '10px 40px 16px 40px', '#FFFFFF', 'font-weight:800;')
b += DARKP('The Black Friday Sale ends {{IF:US}}tonight{{ELSE}}Monday, November 30{{ENDIF}} at %s. After that, prices go back to normal and this is my last email about it.' % HL(END_TIME), '0 40px 16px 40px')
b += DARKP('If you were waiting for the last moment: this is it. Up to 70% off, no code needed. A set ordered now is reserved from the next shipment, the single pans ship from stock.', '0 40px 6px 40px')
b += '{{BLOCK:bf-cta label="Shop before it ends" url="%s" pad="22px 40px 28px 40px" sub="%s"}}\n' % (utm(SALE, 'bf-nov', 'final-cta1'), SUB('No code needed. 30-day returns. 75-year warranty.'))
b += stock('0 20px 26px 20px', '#0E0E0E', 'LAST STOCK CHECK', 'Checked this morning. Up to 70% off until midnight PT.')
b += DARKP('Thank you for cooking with us this year. 100,000+ happy customers now cook without a coating.', '0 40px 10px 40px')
b += SIGN_DARK + TAIL
files['nov-final-hours'] = b

for k, v in files.items():
    assert '—' not in v, k
    open(os.path.join(N, k + '.html'), 'w').write(v)
    print('geschreven', k, len(v))
