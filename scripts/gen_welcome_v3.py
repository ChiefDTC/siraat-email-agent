"""Generates klaviyo/templates/v3/welcome/*.html (source templates with {{IMG}}, {{HEADER}}, {{FOOTER}})."""
import os
OUT = '/home/user/siraat-email-agent/klaviyo/templates/v3/welcome/'
SITE = 'https://siraatskitchen.com'
PAN = SITE + '/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern'
PAN_HI10 = SITE + '/discount/HI10?redirect=/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern'
ALL_HI10 = SITE + '/discount/HI10?redirect=/collections/all'
F = "font-family:Inter,Arial,Helvetica,sans-serif;"
SERIF = "font-family:'Instrument Serif','Times New Roman',serif;font-style:italic;"

HEAD = """<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>%(title)s</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>
  @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&family=Inter:wght@400;500;600&display=swap');
  body{margin:0;padding:0;background:#FFFFFF;-webkit-text-size-adjust:100%%;}
  table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}
  img{border:0;display:block;line-height:100%%;outline:none;text-decoration:none;}
  a{color:#AC3B19;}
  @media only screen and (max-width:620px){
    .w{width:100%%!important;}
    .pad{padding-left:22px!important;padding-right:22px!important;}
    .stack{display:block!important;width:100%%!important;}
    .stackpad{padding:0 0 14px 0!important;}
    .h2{font-size:30px!important;line-height:34px!important;}
    .navhide{display:none!important;}
    .desk{display:none!important;max-height:0!important;overflow:hidden!important;}
    .mob{display:block!important;max-height:none!important;overflow:visible!important;}
    .code{font-size:26px!important;letter-spacing:4px!important;}
    .btn{padding:16px 20px!important;letter-spacing:1px!important;font-size:13px!important;}
  }
</style>
</head>
<body style="margin:0;padding:0;background:#FFFFFF;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;">%(preview)s&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;</div>
<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF">
<tr><td align="center" style="padding:8px 0 32px 0;">
<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:#F8F7F2;" bgcolor="#F8F7F2">

{{HEADER}}
"""
TAIL = """
{{FOOTER}}

</table>
</td></tr>
</table>
</body>
</html>
"""


def meta(sa, sb, pv, send, filt):
    return f"<!-- SUBJECT_A: {sa} | SUBJECT_B: {sb} | PREVIEW: {pv} | SEND: {send} | FILTERS: {filt} -->\n"


def hero(img, alt, href):
    return f"""
<!-- HERO: shoot photo + TT Ramillas headline baked in (scripts/make_hero.py) -->
<tr><td style="padding:0;">
  <a href="{href}"><img src="{{{{IMG}}}}/{img}" width="600" alt="{alt}" style="width:100%;max-width:600px;height:auto;"></a>
</td></tr>
"""


def button(text, href, pad="24px 44px 4px 44px", comment="CTA"):
    return f"""
<!-- {comment} -->
<tr><td align="center" style="padding:{pad};">
  <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
    <td align="center" bgcolor="#AC3B19" style="background:#AC3B19;border-radius:2px;">
      <a class="btn" href="{href}" style="display:inline-block;padding:16px 40px;{F}font-size:14px;line-height:16px;font-weight:600;letter-spacing:1.5px;color:#FFFFFF;text-decoration:none;">{text}</a>
    </td>
  </tr></table>
</td></tr>
"""


def text(paras, pad="30px 44px 6px 44px", comment="INTRO", size=16, lh=26, color="#282828"):
    ps = ''.join(f'  <p style="margin:0 0 14px 0;">{p}</p>\n' for p in paras[:-1]) + f'  <p style="margin:0;">{paras[-1]}</p>\n'
    return f"""
<!-- {comment} -->
<tr><td class="pad" style="padding:{pad};{F}font-size:{size}px;line-height:{lh}px;color:{color};">
{ps}</td></tr>
"""


def h2(title, sub=None, pad="34px 44px 6px 44px"):
    s = f'\n  <div style="{F}font-size:15px;line-height:23px;color:#727272;text-align:center;padding-top:8px;">{sub}</div>' if sub else ''
    return f"""
<tr><td class="pad" style="padding:{pad};">
  <div class="h2" style="{SERIF}font-size:34px;line-height:38px;color:#282828;text-align:center;">{title}</div>{s}
</td></tr>
"""


def offer_block(eyebrow, title, body, btn_text, btn_href):
    return f"""
<!-- OFFER: HI10 as live code block (espresso, dashed code) -->
<tr><td class="pad" style="padding:26px 44px 8px 44px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#321E1D" style="background:#321E1D;border-radius:4px;">
    <tr><td align="center" style="padding:30px 26px 6px 26px;{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:600;color:#C9C6C0;">{eyebrow}</td></tr>
    <tr><td align="center" class="h2" style="padding:8px 26px 0 26px;{SERIF}font-size:36px;line-height:40px;color:#FFFFFF;">{title}</td></tr>
    <tr><td align="center" style="padding:20px 26px 0 26px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
        <td align="center" style="border:2px dashed #C9C6C0;padding:12px 30px;{F}">
          <span style="font-size:11px;letter-spacing:2px;font-weight:600;color:#C9C6C0;vertical-align:middle;">CODE&nbsp;&nbsp;</span>
          <span class="code" style="font-size:30px;line-height:36px;letter-spacing:6px;font-weight:600;color:#FFFFFF;vertical-align:middle;">HI10</span>
        </td>
      </tr></table>
    </td></tr>
    <tr><td align="center" style="padding:16px 34px 0 34px;{F}font-size:14px;line-height:22px;color:#E4DED3;">{body}</td></tr>
    <tr><td align="center" style="padding:20px 26px 30px 26px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
        <td align="center" bgcolor="#FFFFFF" style="background:#FFFFFF;border-radius:2px;">
          <a href="{btn_href}" style="display:inline-block;padding:14px 32px;{F}font-size:13px;line-height:16px;font-weight:600;letter-spacing:1.5px;color:#321E1D;text-decoration:none;">{btn_text}</a>
        </td>
      </tr></table>
    </td></tr>
  </table>
</td></tr>
"""


def stars():
    return '<div style="font-family:Arial,Helvetica,sans-serif;font-size:14px;letter-spacing:2px;color:#AC3B19;">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'


def review_card(quote, name, extra=""):
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #ECE7DD;">
          <tr><td style="padding:18px 18px 16px 18px;{F}">
            {stars()}
            <div style="font-size:14px;line-height:21px;color:#282828;padding:8px 0 10px 0;">&ldquo;{quote}&rdquo;</div>
            <div style="font-size:12px;line-height:16px;font-weight:600;color:#727272;">{name}{extra}</div>
          </td></tr>
        </table>"""


def reviews2(a, b, foot="Join 100,000+ happy customers.", pad="24px 44px 6px 44px"):
    f = f'\n  <div style="{F}font-size:13px;line-height:20px;color:#727272;text-align:center;padding-top:14px;">{foot}</div>' if foot else ''
    return f"""
<!-- REVIEWS -->
<tr><td class="pad" style="padding:{pad};">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
      <td class="stack stackpad" width="50%" valign="top" style="padding:0 7px 0 0;">
        {review_card(*a)}
      </td>
      <td class="stack stackpad" width="50%" valign="top" style="padding:0 0 0 7px;">
        {review_card(*b)}
      </td>
    </tr>
  </table>{f}
</td></tr>
"""


def trust(items=("30-DAY<br>RETURNS", "75-YEAR<br>WARRANTY", "FREE<br>SHIPPING")):
    a, b, c = items
    td = f"padding:16px 4px;{F}font-size:11px;line-height:15px;letter-spacing:1px;font-weight:600;color:#282828;"
    return f"""
<!-- TRUST ROW -->
<tr><td class="pad" style="padding:22px 44px 6px 44px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid #ECE7DD;border-bottom:1px solid #ECE7DD;">
    <tr>
      <td width="33%" align="center" style="{td}">{a}</td>
      <td width="34%" align="center" style="{td}border-left:1px solid #ECE7DD;border-right:1px solid #ECE7DD;">{b}</td>
      <td width="33%" align="center" style="{td}">{c}</td>
    </tr>
  </table>
</td></tr>
"""


def signoff(line="Questions about sizes, induction or how to cook on titanium? Just reply. A real person reads every email."):
    return f"""
<!-- SIGN-OFF -->
<tr><td class="pad" style="padding:22px 44px 26px 44px;{F}font-size:15px;line-height:24px;color:#282828;">
  {line}<br><br>
  Benjamin<br><span style="color:#727272;">Founder, Siraat's Kitchen</span>
</td></tr>
"""


def product_row(img, alt, name, price_html, desc, href, link_text):
    p = f'<div style="font-size:15px;line-height:21px;color:#282828;padding-top:4px;">{price_html}</div>' if price_html else ''
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #ECE7DD;">
    <tr>
      <td class="stack" width="200" valign="middle" style="padding:0;">
        <a href="{href}"><img src="{{{{IMG}}}}/{img}" width="200" alt="{alt}" style="width:100%;max-width:200px;height:auto;margin:0 auto;"></a>
      </td>
      <td class="stack" valign="middle" style="padding:18px 20px;{F}">
        <div style="font-size:16px;line-height:22px;font-weight:600;color:#282828;">{name}</div>
        {p}
        <div style="font-size:14px;line-height:21px;color:#727272;padding-top:6px;">{desc}</div>
        <div style="font-size:13px;line-height:20px;padding-top:10px;"><a href="{href}" style="color:#AC3B19;font-weight:600;text-decoration:none;">{link_text} &rarr;</a></div>
      </td>
    </tr>
  </table>"""


def tier(num, eyebrow, title, intro, rows):
    body = '\n  <div style="height:12px;line-height:12px;font-size:12px;">&nbsp;</div>\n  '.join(rows)
    return f"""
<!-- TIER {num} -->
<tr><td class="pad" style="padding:30px 44px 6px 44px;">
  <div style="{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:600;color:#AC3B19;text-align:center;">{eyebrow}</div>
  <div class="h2" style="{SERIF}font-size:34px;line-height:38px;color:#282828;text-align:center;padding-top:6px;">{title}</div>
  <div style="{F}font-size:15px;line-height:23px;color:#727272;text-align:center;padding:8px 0 16px 0;">{intro}</div>
  {body}
</td></tr>
"""


def price(now, was=None):
    w = f' &nbsp;<span style="color:#9A948B;text-decoration:line-through;">${was}</span>' if was else ''
    return f'<span style="font-weight:600;">${now}</span>{w}'


def write(name, head_meta, title, preview, body):
    html = head_meta + HEAD % {'title': title, 'preview': preview} + body + TAIL
    assert '—' not in html, name + ' contains an em dash'
    open(OUT + name, 'w').write(html)
    print('wrote', name)


SEND_FILTER = "Flow: list Uw8eZG (Alia Card Game), email not contains test@, never in this flow, re-entry never. Split A: Placed Order = 0 ever (prospect path). Send filter: Placed Order = 0 since flow start"

# ---------------------------------------------------------------- W0
w0 = hero('hero-w0.jpg', 'First heat, then oil. Your first egg in three steps. An egg in a Siraat hammered titanium pan.', SITE + '/pages/care-use')
w0 += button('WATCH THE COOK GUIDE', SITE + '/pages/care-use')
w0 += text([
    "Hi {{ first_name|default:'there' }},",
    "Thank you. You already cook with us, or your pan is on its way, so this email is not here to sell you anything.",
    "One line about the card game: your entry is in, with a chance to have your order refunded.",
    "Now the part that matters. A pure titanium cooking surface has no coating, so it does not behave like the pan you are used to. Our chef teaches every new owner the same three steps. Give it two minutes and the first egg slides."])
w0 += h2('Three steps, one egg', 'Cold metal grabs your food. Hot metal lets it go.')
steps = [
    ('1', 'Heat first', 'Medium heat, about two minutes, before anything goes in. Medium on titanium works like high on a normal pan.', None),
    ('2', 'Do the water test', 'Flick in a drop of water. If it dances and rolls around, the pan is ready. If it just sits and sizzles, wait a little longer.', 'gif-water-test.gif'),
    ('3', 'Then oil, then the egg', 'A thin layer of oil, let it shimmer, then the egg. Leave it alone until it lets go by itself. Then it slides.', 'gif-egg-slide.gif'),
]
for n, t, d, g in steps:
    w0 += f"""
<!-- STEP {n} -->
<tr><td class="pad" style="padding:22px 44px 0 44px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #ECE7DD;">
    <tr><td style="padding:20px 22px {'14px' if g else '20px'} 22px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
        <td width="44" valign="top" style="{SERIF}font-size:34px;line-height:34px;color:#AC3B19;">{n}</td>
        <td valign="top" style="{F}">
          <div style="font-size:16px;line-height:22px;font-weight:600;color:#282828;">{t}</div>
          <div style="font-size:14px;line-height:21px;color:#727272;padding-top:4px;">{d}</div>
        </td>
      </tr></table>
    </td></tr>""" + (f"""
    <tr><td style="padding:0 22px 22px 22px;"><img src="{{{{IMG}}}}/{g}" width="512" alt="{'A drop of water dancing in a hot Siraat titanium pan' if n == '2' else 'An egg sliding freely in a Siraat titanium pan'}" style="width:100%;max-width:512px;height:auto;"></td></tr>""" if g else '') + """
  </table>
</td></tr>
"""
w0 += text(["If you can do an egg, you can do anything. Steak, fish and pancakes follow the same rule: heat first, then oil, then patience."],
           pad="22px 44px 6px 44px", comment="CHEF LINE", size=15, lh=24, color="#727272")
w0 += f"""
<!-- REVIEW -->
<tr><td class="pad" style="padding:20px 44px 6px 44px;">
  {review_card("I followed the instructions; let the pan heat up and did the water test. Then fried an egg which didn&rsquo;t stick to the pan. Easy clean up.", "Aggie M., verified buyer")}
</td></tr>
"""
w0 += h2('Good to know', None, pad="30px 44px 0 44px")
w0 += f"""
<!-- CARE FACTS -->
<tr><td class="pad" style="padding:14px 44px 6px 44px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #ECE7DD;">
    <tr><td style="padding:14px 20px;border-bottom:1px solid #ECE7DD;{F}font-size:14px;line-height:21px;color:#727272;"><span style="font-weight:600;color:#282828;">No seasoning required.</span> Wash it once and cook.</td></tr>
    <tr><td style="padding:14px 20px;border-bottom:1px solid #ECE7DD;{F}font-size:14px;line-height:21px;color:#727272;"><span style="font-weight:600;color:#282828;">Metal utensils are fine.</span> There is no coating to scratch off.</td></tr>
    <tr><td style="padding:14px 20px;border-bottom:1px solid #ECE7DD;{F}font-size:14px;line-height:21px;color:#727272;"><span style="font-weight:600;color:#282828;">Dishwasher safe.</span> A soft sponge by hand works just as well.</td></tr>
    <tr><td style="padding:14px 20px;{F}font-size:14px;line-height:21px;color:#727272;"><span style="font-weight:600;color:#282828;">Covered for 75 years.</span> Against defects, for as long as you own it.</td></tr>
  </table>
</td></tr>
"""
w0 += button('WATCH THE COOK GUIDE', SITE + '/pages/care-use', pad="26px 44px 8px 44px")
w0 += trust(("NO<br>SEASONING", "75-YEAR<br>WARRANTY", "DISHWASHER<br>SAFE"))
w0 += signoff("Stuck on something, literally or not? Just reply. A real person reads every email.")
write('w0.html', meta("Thank you. Now the first egg.", "Before your pan arrives: three steps",
                      "Cold metal grabs your food, hot metal lets it go.",
                      "10 min after signup, buyers path (Split A: Placed Order > 0 ever). Then end of flow; post-purchase takes over",
                      "Flow: list Uw8eZG, email not contains test@, never in this flow. No offer, no HI10"),
      'Thank you. Now the first egg.', 'Cold metal grabs your food, hot metal lets it go.', w0)

# ---------------------------------------------------------------- W1 (A and B)
W1_PREVIEW = "Your giveaway entry is in. Plus 10% on top of the sale with HI10."


def w1(variant):
    b = hero('hero-w1.jpg', 'The original hammered pan. Pure titanium cooking surface, no coatings. Since December 20, 2024.', PAN_HI10)
    b += button('SHOP THE PAN PRO WITH HI10', PAN_HI10)
    b += text([
        "Hi {{ first_name|default:'there' }},",
        "Your entry is in: a chance to win your order refunded. Good luck.",
        "Now, why you signed up. Siraat makes the original hammered titanium pan. Our first orders shipped on December 20, 2024. At that point nobody else was making a pan like this. Look-alikes have appeared since. We are still the original.",
        "A welcome from us, so you do not have to wait for the draw:"])
    if variant == 'A':
        b += offer_block('YOUR WELCOME OFFER', '10% on top of the sale',
                         'Enter HI10 at checkout and it comes off the sale price, not the full price. One code per order, on everything except subscriptions.',
                         'APPLY HI10 AND SHOP', ALL_HI10)
    else:
        b += f"""
<!-- OFFER: HI10 as welcome gift card (rendered card image + live text) -->
<tr><td class="pad" style="padding:22px 34px 0 34px;">
  <a href="{ALL_HI10}"><img src="{{{{IMG}}}}/gift-card.jpg" width="532" alt="Siraat welcome gift card: 10% on top of the sale with code HI10" style="width:100%;max-width:532px;height:auto;"></a>
</td></tr>
<tr><td class="pad" align="center" style="padding:14px 44px 0 44px;{F}font-size:15px;line-height:23px;color:#282828;text-align:center;">
  Your welcome gift card is <span style="font-weight:600;letter-spacing:1px;">HI10</span>: 10% on top of the sale price.<br><span style="color:#727272;font-size:14px;">Enter it at checkout, or tap below and we apply it for you. One code per order, on everything except subscriptions.</span>
</td></tr>
"""
        b += button('USE MY GIFT CARD', ALL_HI10, pad="18px 44px 4px 44px", comment="GIFT CARD CTA")
    b += h2('What makes it the original')
    pts = [
        ('Pure titanium cooking surface', 'No coatings anywhere. Nothing to peel, flake or wear through.'),
        ('The hammered pattern', 'Tiny points of contact between food and metal, so less of your food touches the pan.'),
        ('Tested, not claimed', 'Light Labs, an ISO/IEC 17025-accredited lab, tested it for PFAS. Report no. 25895, every compound below the detection limit.'),
        ('Covered for 75 years', 'A 75-year warranty against defects. There is no coating to fail.'),
    ]
    rows = ''
    for i, (t, d) in enumerate(pts):
        bb = '' if i == len(pts) - 1 else 'border-bottom:1px solid #ECE7DD;'
        rows += f"""
    <tr><td style="padding:14px 20px;{bb}{F}">
      <div style="font-size:15px;line-height:21px;font-weight:600;color:#282828;">{t}</div>
      <div style="font-size:14px;line-height:21px;color:#727272;padding-top:3px;">{d}</div>
    </td></tr>"""
    b += f"""
<!-- PROOF POINTS -->
<tr><td class="pad" style="padding:16px 44px 6px 44px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #ECE7DD;">{rows}
  </table>
</td></tr>
"""
    b += h2('Where most people start', 'One pan. Pick it by how many you cook for.', pad="34px 44px 14px 44px")
    b += f"""
<!-- PRODUCT -->
<tr><td class="pad" style="padding:0 44px 6px 44px;">
  {product_row('prod-panpro.jpg', 'Titanium Hammered Pan Pro', 'Titanium Hammered Pan Pro', price('134', '439') + ' &nbsp;<span style="font-size:13px;color:#727272;">Standard 11&Prime;</span>', 'The Standard 11&Prime; is right for one or two people. Cooking for a family? The Large 12&Prime; is $139. HI10 takes another 10% off at checkout.', PAN_HI10, 'Shop the Pan Pro')}
</td></tr>
"""
    b += reviews2(("This pan is fantastic. Makes all of our others &lsquo;non stick&rsquo; seem really sticky.", "Thomas D., verified buyer"),
                  ("I am so happy to throw away my old Teflon pans and replace with the new titanium ones. They disperse the heat very well and are easy to clean.", "Fran G., verified buyer"))
    b += button('SHOP THE PAN PRO WITH HI10', PAN_HI10, pad="22px 44px 8px 44px")
    b += trust()
    b += signoff()
    return b


w1_send = "10 min after signup, prospect path. A/B test 50/50: w1-a (HI10 as code block) vs w1-b (HI10 as welcome gift card), winner on placed order rate, then unique clicks"
write('w1-a.html', meta("Welcome. 10% on top of the sale, no catch.", "The original hammered titanium pan, plus 10%", W1_PREVIEW, w1_send, SEND_FILTER),
      'Welcome to Siraat', W1_PREVIEW, w1('A'))
write('w1-b.html', meta("Welcome. 10% on top of the sale, no catch.", "The original hammered titanium pan, plus 10%", W1_PREVIEW,
                        w1_send + ". Same subjects as w1-a so the offer framing is the only variable", SEND_FILTER),
      'Welcome to Siraat', W1_PREVIEW, w1('B'))

# ---------------------------------------------------------------- W2 founder note (plain-text style)
W2_PREVIEW = "First orders shipped December 20, 2024. Here is why."
P = f"margin:0 0 18px 0;"
w2paras = [
    "Hi {{ first_name|default:'there' }},",
    "It&rsquo;s Benjamin, the founder of Siraat. You joined us yesterday, so I wanted to write to you myself. Just a short note.",
    "The hammered titanium pan started with us. Our first orders shipped on December 20, 2024, and at that point nobody else was making a pan like this: a pure titanium cooking surface, a hammered pattern, and no coating of any kind. We developed it ourselves, and I&rsquo;m proud of it.",
    "The idea was simple. Most of us have thrown out a pan because the coating wore through, then bought the same kind again. I believed a pan with nothing added to it could cook just as well. The hammered pattern creates tiny points of contact between the food and the surface, so less of your food touches the metal. Heat it first, add a little oil, and an egg slides. And because there is nothing on the surface, there is nothing to scratch, wear or wonder about years from now.",
    "Since then, look-alikes have appeared. Same shape, similar claims. We&rsquo;re still the original, and more than 100,000 happy customers cook on it today.",
    "We don&rsquo;t ask you to take our word for it. Light Labs, an ISO/IEC 17025-accredited lab, tested our pan for PFAS. Report no. 25895: every compound came back below the detection limit. Every Siraat pan has the same titanium cooking surface, and every one comes with a 75-year warranty. Designed in the Netherlands, made in certified facilities.",
    f'If you want to see it: <a href="{PAN_HI10}" style="color:#AC3B19;">the pan that started it</a>. Your welcome code HI10 still takes 10% off on top of the sale.',
    "If you have a question, just hit reply. A real person reads every email.",
    "Benjamin<br>Founder, Siraat&rsquo;s Kitchen",
    "P.S. 30-day returns from the day the box arrives. If it&rsquo;s not for you, send it back unused.",
]
w2body = ''.join(f'  <p style="{P}">{p}</p>\n' for p in w2paras[:-1]) + f'  <p style="margin:0;">{w2paras[-1]}</p>\n'
w2 = f"""
<!-- FOUNDER NOTE: plain-text style. No hero, no images in the body, left aligned, one text link -->
<tr><td class="pad" style="padding:34px 44px 34px 44px;background:#FFFFFF;{F}font-size:16px;line-height:26px;color:#282828;" bgcolor="#FFFFFF">
{w2body}</td></tr>
"""
write('w2.html', meta("Why I started Siraat's Kitchen", "The pan nobody else was making", W2_PREVIEW,
                      "Day 1, 10:00 local time (wait until day 1 at 10:00 after W1). From name 'Benjamin at Siraat's Kitchen', reply-to a read inbox",
                      SEND_FILTER),
      "Why I started Siraat's Kitchen", W2_PREVIEW, w2)

# ---------------------------------------------------------------- W3 proof
W3_PREVIEW = "Report no. 25895. An ISO/IEC 17025-accredited lab. Here is what it says."
LAB = SITE + '/pages/third-party-testing'
w3 = hero('hero-w3.jpg', 'Tested. Not claimed. Light Labs report no. 25895. Read the lab report yourself.', LAB)
w3 += button('READ THE LAB REPORT', LAB)
w3 += text([
    "Hi {{ first_name|default:'there' }},",
    "Every pan on the shelf says non-toxic. Very few can show you the paper. Since our first orders shipped on December 20, 2024, a lot of titanium pans have appeared, so here is what our chef tells everyone.",
    "Ask any brand these three questions. If the answer to one of them is no, keep looking."])
qs = [
    ('1', 'Is there an independent lab report?', 'Yes. Light Labs, an ISO/IEC 17025-accredited lab, tested our pan for 31 PFAS compounds. Every one came back below the detection limit.'),
    ('2', 'Is there a certificate with a report number?', 'Yes. Report no. 25895, released October 30, 2025, signed by the lab director. Every Siraat pan has the same titanium cooking surface, so it covers all of them.'),
    ('3', 'Does the warranty outlast you?', 'Yes. A 75-year warranty against defects, for as long as you own it. There is no coating to fail.'),
]
qrows = ''
for i, (n, t, d) in enumerate(qs):
    last = i == 2
    pd = '14px 0 18px 0' if last else '14px 0'
    bb = '' if last else 'border-bottom:1px solid #ECE7DD;'
    qrows += f"""
        <tr>
          <td width="44" valign="top" style="padding:{pd};{SERIF}font-size:34px;line-height:34px;color:#AC3B19;">{n}</td>
          <td valign="top" style="padding:{pd};{bb}{F}">
            <div style="font-size:16px;line-height:22px;font-weight:600;color:#282828;">{t}</div>
            <div style="font-size:14px;line-height:21px;color:#727272;padding-top:4px;">{d}</div>
          </td>
        </tr>"""
w3 += f"""
<!-- PROOF CARD: the three questions + certificate -->
<tr><td class="pad" style="padding:22px 44px 8px 44px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #ECE7DD;">
    <tr><td style="padding:20px 22px 6px 22px;{F}font-size:11px;line-height:14px;letter-spacing:1.5px;font-weight:600;color:#AC3B19;">THE THREE QUESTIONS</td></tr>
    <tr><td style="padding:0 22px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{qrows}
      </table>
    </td></tr>
    <tr><td style="padding:4px 22px 22px 22px;">
      <a href="{LAB}"><img src="{{{{IMG}}}}/certificate.jpg" width="514" alt="Light Labs Certificate of Analysis for Siraat's Kitchen, Titanium Hammered Pan Pro, test 25895" style="width:100%;max-width:514px;height:auto;border:1px solid #ECE7DD;"></a>
      <div style="{F}font-size:13px;line-height:20px;padding-top:10px;"><a href="{LAB}" style="color:#AC3B19;font-weight:600;text-decoration:none;">See the full lab report &rarr;</a></div>
    </td></tr>
  </table>
</td></tr>
"""
w3 += h2('Only titanium touches your food', 'Three layers of metal, bonded together. No coating anywhere in the pan.')
w3 += """
<!-- ANATOMY: desktop labelled image, mobile unlabelled image + live text -->
<tr><td style="padding:14px 0 0 0;">
  <!--[if !mso]><!--><div class="mob" style="display:none;max-height:0;overflow:hidden;mso-hide:all;">
    <img src="{{IMG}}/anatomy-mobile.jpg" width="600" alt="Cutaway of the Siraat pan showing three bonded layers" style="width:100%;max-width:600px;height:auto;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:6px;">
      <tr><td style="padding:12px 22px;border-bottom:1px solid #ECE7DD;font-family:Inter,Arial,Helvetica,sans-serif;"><span style="font-size:15px;font-weight:600;color:#282828;">Pure titanium</span><br><span style="font-size:14px;line-height:20px;color:#727272;">The surface you cook on. The only layer your food touches.</span></td></tr>
      <tr><td style="padding:12px 22px;border-bottom:1px solid #ECE7DD;font-family:Inter,Arial,Helvetica,sans-serif;"><span style="font-size:15px;font-weight:600;color:#282828;">Aluminium core</span><br><span style="font-size:14px;line-height:20px;color:#727272;">Even heat, edge to edge.</span></td></tr>
      <tr><td style="padding:12px 22px;font-family:Inter,Arial,Helvetica,sans-serif;"><span style="font-size:15px;font-weight:600;color:#282828;">Stainless steel base</span><br><span style="font-size:14px;line-height:20px;color:#727272;">Gas, electric, induction.</span></td></tr>
    </table>
  </div><!--<![endif]-->
  <div class="desk"><img src="{{IMG}}/anatomy.jpg" width="600" alt="Cutaway of the Siraat pan: pure titanium cooking surface, aluminium core for even heat, stainless steel base for gas, electric and induction." style="width:100%;max-width:600px;height:auto;"></div>
</td></tr>
"""
w3 += h2('How it compares', 'What you cook on, side by side.')
cols = ['Coated pan', 'Stainless', 'Cast iron', 'Siraat']
rows = [
    ('Coating that can wear off', ['Yes', 'No', 'No', 'No']),
    ('Needs seasoning', ['No', 'No', 'Yes', 'No']),
    ('Metal utensils', ['Avoid', 'Yes', 'Yes', 'Yes']),
    ('Dishwasher', ['Often not', 'Yes', 'No', 'Yes']),
    ('Lab report you can read', ['Ask', 'Ask', 'Ask', 'No. 25895']),
]
th = f"padding:10px 4px;{F}font-size:11px;line-height:14px;letter-spacing:0.5px;font-weight:600;color:#727272;text-align:center;border-bottom:1px solid #ECE7DD;"
thS = th.replace('color:#727272', 'color:#FFFFFF') + 'background:#AC3B19;'
trows = f'<tr><td style="{th}text-align:left;padding-left:14px;">&nbsp;</td>' + ''.join(
    f'<td width="16%" style="{thS if c == "Siraat" else th}">{c.upper()}</td>' for c in cols) + '</tr>'
for i, (label, vals) in enumerate(rows):
    bb = '' if i == len(rows) - 1 else 'border-bottom:1px solid #ECE7DD;'
    trows += f'\n      <tr><td style="padding:11px 4px 11px 14px;{bb}{F}font-size:13px;line-height:18px;font-weight:600;color:#282828;">{label}</td>'
    for c, v in zip(cols, vals):
        s = f"padding:11px 4px;{bb}{F}font-size:13px;line-height:18px;text-align:center;"
        s += 'color:#282828;font-weight:600;background:#FBF3EF;' if c == 'Siraat' else 'color:#727272;'
        trows += f'<td style="{s}">{v}</td>'
    trows += '</tr>'
w3 += f"""
<!-- COMPARISON TABLE (live text) -->
<tr><td class="pad" style="padding:16px 44px 6px 44px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #ECE7DD;">
      {trows}
  </table>
</td></tr>
"""
w3 += reviews2(("Fantastic product which has no coating that could eventually flake off. Dishwasher friendly and will also cope with the oven temperatures if required. This is definitely a life long pan.", "Jonathan D., verified buyer"),
               ("Awesome pan and peace of mind that I am not ingesting bits of toxins when I cook. Nice looking pan too.", "Gwen, verified buyer"))
w3 += text(["Read the report, then see the pan. Your welcome code HI10 still takes 10% off on top of the sale."],
           pad="26px 44px 0 44px", comment="BRIDGE", size=15, lh=24)
w3 += button('SEE THE PAN PRO WITH HI10', PAN_HI10, pad="18px 44px 8px 44px")
w3 += trust()
w3 += signoff("Want the full report as a PDF, or have a question about materials? Just reply. A real person reads every email.")
write('w3.html', meta("Has your cookware actually been tested?", "Three questions to ask any titanium pan brand", W3_PREVIEW,
                      "Day 3, 10:00 local time", SEND_FILTER),
      'Tested. Not claimed.', W3_PREVIEW, w3)

# ---------------------------------------------------------------- W4 US / INT
SHEETS = SITE + '/products/dishwashing-detergent-sheets-fresh-lemon'
BOARD = SITE + '/products/titanium-cutting-board-v2'
SET6 = SITE + '/products/titanium-hammered-pan-set-with-lids-6-pcs-bday-sale'
SET6_INT = SITE + '/products/titanium-hammered-pan-set-with-lids-6-pcs'
SETPRO = SITE + '/products/titanium-hammered-cookware-set-pro'
SET12 = SITE + '/products/titanium-hammered-cookware-set'
ALL = SITE + '/collections/all'


def small_pair(a, b):
    def cell(img, alt, name, pr, desc, href, side):
        p = f'<div style="font-size:14px;line-height:20px;color:#282828;padding-top:2px;">{pr}</div>' if pr else ''
        pad = '0 7px 0 0' if side == 'l' else '0 0 0 7px'
        return f"""<td class="stack stackpad" width="50%" valign="top" style="padding:{pad};">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #ECE7DD;">
          <tr><td style="padding:0;"><a href="{href}"><img src="{{{{IMG}}}}/{img}" width="248" alt="{alt}" style="width:100%;max-width:248px;height:auto;margin:0 auto;"></a></td></tr>
          <tr><td style="padding:4px 16px 16px 16px;{F}">
            <div style="font-size:15px;line-height:21px;font-weight:600;color:#282828;">{name}</div>
            {p}
            <div style="font-size:13px;line-height:19px;color:#727272;padding-top:4px;">{desc}</div>
            <div style="font-size:13px;line-height:20px;padding-top:8px;"><a href="{href}" style="color:#AC3B19;font-weight:600;text-decoration:none;">Shop &rarr;</a></div>
          </td></tr>
        </table>
      </td>"""
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
      {cell(*a, 'l')}
      {cell(*b, 'r')}
    </tr></table>"""


def w4(us):
    b = hero('hero-w4-us.jpg' if us else 'hero-w4-int.jpg',
             'Three ways to start. ' + ('Under $80, one pan, or the whole kitchen. US prices, free shipping.' if us else 'A first piece, one pan, or a full set. Ships worldwide, duties paid.'),
             ALL)
    b += button('CHOOSE YOUR START', ALL)
    if us:
        intro = ["Hi {{ first_name|default:'there' }},",
                 "Not everyone starts with a full kitchen. Most people start with one pan, some with something smaller, a few go all in on day one. Here are the three ways in, with today&rsquo;s US prices.",
                 "Whichever you pick: free shipping, free 30-day returns on unused products, and a 75-year warranty on every pan."]
    else:
        intro = ["Hi {{ first_name|default:'there' }},",
                 "Not everyone starts with a full kitchen. Most people start with one pan, some with something smaller, a few go all in on day one. Here are the three ways in.",
                 "Whichever you pick: free shipping worldwide with duties paid, so there is nothing extra to pay at the door. Prices show in your own currency at checkout. Free 30-day returns on unused products, and a 75-year warranty on every pan."]
    b += text(intro)
    # tier 1
    b += tier(1, 'START SMALL', 'A first piece' + (' under $80' if us else ''),
              'Try the Siraat way of doing things before you change your pans.',
              [small_pair(('prod-sheets.jpg', 'Plastic-Free Dishwasher Sheets, Fresh Lemon', 'Dishwasher Sheets', price('25', '60') if us else '', 'Plastic-free, pre-measured, fresh lemon. One sheet per load.', SHEETS),
                          ('prod-board.jpg', 'Titanium Cutting Board V2', 'Titanium Cutting Board', ('<span style="font-weight:600;">From $69</span>' if us else ''), 'Anti-microbial titanium. Four sizes, from Mini to Large.', BOARD))])
    # tier 2
    b += tier(2, 'THE ONE MOST PEOPLE PICK', 'One pan',
              'The original hammered titanium pan. If you buy one thing, buy this.',
              [product_row('prod-panpro.jpg', 'Titanium Hammered Pan Pro', 'Titanium Hammered Pan Pro',
                           (price('134', '439') + ' &nbsp;<span style="font-size:13px;color:#727272;">Standard 11&Prime;</span>') if us else '',
                           ('Four sizes from $127 to $139. ' if us else 'Four sizes, from the 8&Prime; Mini to the 12&Prime; Large. ') + 'Pure titanium cooking surface, no coatings, works on gas, electric and induction.',
                           PAN, 'Shop the Pan Pro')])
    # tier 3
    if us:
        rows3 = [product_row('prod-set6.jpg', 'Titanium Hammered Pan Set With Lids, 6 pieces', 'The 6-piece set', price('349'),
                             'Three hammered pans in three sizes, plus three stainless steel lids. The pans you reach for every day.', SET6, 'Shop the 6-piece set'),
                 product_row('prod-setpro.jpg', 'Titanium Hammered Cookware Set Pro', 'Cookware Set Pro', price('479', '870'),
                             'Pan Pro, Wok Pan Pro and Deep Pan Pro, plus titanium utensils. Sear, stir-fry and simmer.', SETPRO, 'Shop the Set Pro'),
                 product_row('prod-set12.jpg', 'Titanium Hammered Cookware Set, 12 pieces', 'The 12-piece set', price('599', '1,186') + ' &nbsp;<span style="font-size:12px;font-weight:600;letter-spacing:1px;color:#AC3B19;">US ONLY</span>',
                             'Three pans, three pots and six lids. A complete PFAS-free kitchen in one decision.', SET12, 'Shop the 12-piece set')]
        t3 = tier(3, 'THE WHOLE KITCHEN', 'A set, from $349', 'Every pan in every set has the same titanium cooking surface as the one Light Labs tested.', rows3)
    else:
        rows3 = [product_row('prod-setpro.jpg', 'Titanium Hammered Cookware Set Pro', 'Cookware Set Pro', '',
                             'Pan Pro, Wok Pan Pro and Deep Pan Pro, plus titanium utensils. Sear, stir-fry and simmer. Our first pick outside the US.', SETPRO, 'Shop the Set Pro'),
                 product_row('prod-set6.jpg', 'Titanium Hammered Pan Set With Lids, 6 pieces', 'The 6-piece set', '',
                             'Three hammered pans in three sizes, plus three stainless steel lids. The pans you reach for every day.', SET6_INT, 'Shop the 6-piece set')]
        t3 = tier(3, 'THE WHOLE KITCHEN', 'A full set', 'Every pan in every set has the same titanium cooking surface as the one Light Labs tested.', rows3)
    b += t3
    if us:
        b += text(["Why a $134 pan? Because it is built to be the last frying pan you buy. The coated pan you replace every time the surface wears is the expensive one. This one has no coating to wear, and a 75-year warranty behind it."],
                  pad="28px 44px 0 44px", comment="PRICE MATH", size=15, lh=24, color="#727272")
        b += reviews2(("I purchased the hammered pro pan standard. It is beautiful and lightweight. I cooked perfect over easy eggs for the first time in a non coated pan.", "Deb, verified buyer"),
                      ("Bought the wok pan and the experience was amazing. I am considering buying more kitchenware from Siraat.", "David, verified buyer"))
    else:
        b += reviews2(("The pan is great, heats up very quickly on a low heat on my induction hob, does not stick, easy to clean, light weight. Also can use metal on it.", "Mrs J., verified buyer, UK"),
                      ("We cooked the best omelette we have ever eaten when we used the pan for the first time. Cleaning the pan afterwards was so easy.", "Graham C., verified buyer"))
    b += text(['Your welcome code still works on all three: <span style="font-weight:600;letter-spacing:1px;">HI10</span> takes 10% off on top of the sale.'],
              pad="24px 44px 0 44px", comment="HI10 LINE", size=15, lh=24)
    b += button('CHOOSE YOUR START', ALL_HI10, pad="18px 44px 8px 44px")
    b += trust(("30-DAY<br>RETURNS", "75-YEAR<br>WARRANTY", "FREE<br>SHIPPING") if us else ("30-DAY<br>RETURNS", "75-YEAR<br>WARRANTY", "DUTIES<br>PAID"))
    b += signoff("Not sure which size or set fits your kitchen? Reply with what you cook most. A real person reads every email.")
    return b


write('w4-us.html', meta("Three ways to start", "Under $80, one pan, or the whole kitchen",
                         "A first piece under $80, the Pan Pro at $134, or a set from $349.",
                         "Day 6, 10:00 local time. Split B: Location country = United States (yes branch)", SEND_FILTER),
      'Three ways to start', "A first piece under $80, the Pan Pro at $134, or a set from $349.", w4(True))
write('w4-int.html', meta("Three ways to start", "One pan, or the whole kitchen",
                          "A first piece, the Pan Pro, or a full set. Free shipping, duties paid.",
                          "Day 6, 10:00 local time. Split B: Location country = United States (no branch, all other countries)", SEND_FILTER),
      'Three ways to start', "A first piece, the Pan Pro, or a full set. Free shipping, duties paid.", w4(False))

# ---------------------------------------------------------------- W5
W5_PREVIEW = "Tammy is on her fourth pan. Marilyn gave her nonstick pans away."
w5 = hero('hero-w5.jpg', 'In their words. What 100,000+ happy customers found out. Your 10% is still here.', PAN_HI10)
w5 += button('USE HI10 AT CHECKOUT', PAN_HI10)
w5 += text([
    "Hi {{ first_name|default:'there' }},",
    "We have told you about the lab report, the warranty and where the pan came from. This is the last email in our welcome series, so we will let the people who cook on it every day do the talking."])
w5 += f"""
<!-- FEATURED QUOTE -->
<tr><td class="pad" style="padding:26px 44px 6px 44px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #ECE7DD;">
    <tr><td align="center" style="padding:30px 30px 26px 30px;">
      {stars()}
      <div class="h2" style="{SERIF}font-size:30px;line-height:36px;color:#282828;padding:14px 0 14px 0;">&ldquo;I am on my 4th pan from Siraat. I even gifted one to my son, and he says it&rsquo;s the best pan he owns.&rdquo;</div>
      <div style="{F}font-size:12px;line-height:16px;font-weight:600;color:#727272;letter-spacing:0.5px;">TAMMY, VERIFIED BUYER</div>
    </td></tr>
  </table>
</td></tr>
"""
w5 += reviews2(("I followed your directions, made scrambled eggs and they came out of the pan perfectly. I am getting rid of (or giving away) my non stick pans. I only need the new one.", "Marilyn B., verified buyer"),
               ("Cooked eggs in the skillet and it definitely needed just a thin covering of oil, and it cleaned up beautifully. I am very impressed.", "Sandi R., verified buyer"),
               foot=None, pad="14px 44px 0 44px")
w5 += reviews2(("Siraat replaced a pan free of charge that had the handle started to become loose on my favorite pan. I just sent them the picture and they honored the warranty.", "Brandon W., verified buyer"),
               ("Very happy with the product. An excellent non toxic pan that&rsquo;s easy to clean.", "D. C., verified buyer"),
               foot="Join 100,000+ happy customers.", pad="14px 44px 6px 44px")
w5 += offer_block('STILL YOURS', '10% on top of the sale',
                  'This is the last time we mention it in this series. HI10 comes off the sale price at checkout. One code per order, on everything except subscriptions.',
                  'APPLY HI10 AND SHOP', PAN_HI10)
w5 += h2('Comes with every Hammered Pan', 'Four extras with your order, on top of your 10%.', pad="30px 44px 0 44px")
gifts = [('Free shipping', 'To your door, no minimum.'), ('Plastic-Free Home e-book', 'Our guide to a cleaner kitchen.'),
         ('A mystery gift', 'We will not spoil it.'), ('A chance to win', 'A PFAS water purifier, drawn weekly.')]
gcells = ''
for i, (t, d) in enumerate(gifts):
    side = 'padding:0 7px 14px 0;' if i % 2 == 0 else 'padding:0 0 14px 7px;'
    cell = f"""<td class="stack stackpad" width="50%" valign="top" style="{side}">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFFFFF;border:1px solid #ECE7DD;"><tr><td style="padding:16px 18px;{F}">
          <div style="{SERIF}font-size:26px;line-height:26px;color:#AC3B19;">{i + 1}</div>
          <div style="font-size:15px;line-height:21px;font-weight:600;color:#282828;padding-top:8px;">{t}</div>
          <div style="font-size:13px;line-height:19px;color:#727272;padding-top:2px;">{d}</div>
        </td></tr></table>
      </td>"""
    gcells += ('<tr>' if i % 2 == 0 else '') + cell + ('</tr>' if i % 2 == 1 else '')
w5 += f"""
<!-- GIFT STACK -->
<tr><td class="pad" style="padding:16px 44px 0 44px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{gcells}</table>
</td></tr>
"""
w5 += f"""
<!-- PRODUCTS -->
<tr><td class="pad" style="padding:16px 44px 6px 44px;">
  {product_row('prod-panpro.jpg', 'Titanium Hammered Pan Pro', 'Titanium Hammered Pan Pro', '', 'The one Tammy is on her fourth of. Four sizes, pure titanium cooking surface, no coatings.', PAN_HI10, 'Shop the Pan Pro')}
  <div style="height:12px;line-height:12px;font-size:12px;">&nbsp;</div>
  {product_row('prod-duo.jpg', 'Titanium Hammered Pan Pro Duo', 'Pan Pro Duo', '', 'The Small and the Standard together. One for eggs, one for everything else.', SITE + '/discount/HI10?redirect=/products/titanium-hammered-pan-pro-duo', 'Shop the Duo')}
</td></tr>
"""
w5 += text(["Changed your mind after it arrives? Free 30-day returns on unused products, from the day the box arrives. A defect later on is covered by the 75-year warranty, as Brandon found out."],
           pad="24px 44px 0 44px", comment="RISK REVERSAL", size=15, lh=24, color="#727272")
w5 += button('USE HI10 AT CHECKOUT', PAN_HI10, pad="22px 44px 8px 44px")
w5 += trust()
w5 += signoff("Thank you for reading along this week. If anything is still holding you back, reply and tell us. A real person reads every email.")
write('w5.html', meta("In their words (and your 10% is still here)", "What 100,000+ happy customers found out", W5_PREVIEW,
                      "Day 9, 10:00 local time. Last mail of the flow; day 10 end, non-buyers go to campaigns", SEND_FILTER),
      'In their words', W5_PREVIEW, w5)
