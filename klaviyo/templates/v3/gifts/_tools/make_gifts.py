"""Gift-leveringsmail (Favorites Cookbook + Plastic-Free Home E-Book), 3 varianten plus A-alt (placeholder e-book cover).
Copy: ../COPY.md. Stijl volgt het cookbook: Night #0E0E0E, Cream #F8F7F2, Signal Yellow #FFB800, Inter + serif-kop (DM Serif Display,
terugval Instrument Serif / Times New Roman), cursieve gele accentwoorden. Knoppen geel #FFB800 met tekst #272727 (Floris).
Vaste header (lockup) en footer via build_template.py. Transactioneel: geen korting, geen prijzen, geen productpromo, geen gift-waarden.
Gebruik (vanuit /tmp): python3 -I make_gifts.py. Daarna render_gifts.py en shot_gifts.js."""
import os, re
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NIGHT, CREAM, Y, INK, BODY, GREY, HAIR, SOFT = '#0E0E0E', '#F8F7F2', '#FFB800', '#272727', '#3A3A3A', '#727272', '#E4DED3', '#C9C4BA'
FF = "Inter,Arial,Helvetica,sans-serif"
SERIF = "'DM Serif Display','Instrument Serif','Times New Roman',Times,serif"
# Links. E-book: zoals in de live flow YyaMjx (template S2EMYW, gelezen 2 nov 2026). Cookbook: hosting nog niet gekozen.
EBOOK = 'https://delivery.shopifyapps.com/-/396da74b7735ff7f/6d8678add81ad2ad'
COOK = '{{COOKBOOK_URL}}'   # PLACEHOLDER: cookbook-downloadlink nog niet bekend (VRAAG FLORIS 1). Niet versturen zolang dit hier staat.
USE = 'PDF &middot; opens on phone, tablet or computer &middot; yours to keep'

CSS = '''
    .w{width:100%!important;}
    .pad{padding-left:24px!important;padding-right:24px!important;}
    .padx{padding-left:16px!important;padding-right:16px!important;}
    .navhide{display:none!important;}
    .h1{font-size:44px!important;line-height:46px!important;}
    .h2{font-size:30px!important;line-height:33px!important;}
    .lead{font-size:16px!important;line-height:25px!important;}
    .col{display:block!important;width:100%!important;padding-left:0!important;padding-right:0!important;}
    .colgap{padding-bottom:10px!important;}
    .cover{width:50%!important;}
    .thumb{width:84px!important;}
    .thtd{width:84px!important;padding:16px 0 16px 14px!important;}
    .cardtx{padding:16px 14px 16px 14px!important;}
    .rimg{width:88px!important;}
'''

def head(meta, title, pre):
    return '''<!--
GIFTS · bezorgmail Favorites Cookbook + Plastic-Free Home E-Book (concept 2 nov 2026, niet in Klaviyo, niets live).
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
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap');
  body{margin:0;padding:0;background:#FFFFFF;-webkit-text-size-adjust:100%%;}
  table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}
  img{border:0;display:block;line-height:100%%;outline:none;text-decoration:none;}
  a{color:#272727;}
  @media only screen and (max-width:620px){%s  }
</style>
</head>
<body style="margin:0;padding:0;background:#FFFFFF;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">%s</div>
<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF">
<tr><td align="center" style="padding:8px 0 32px 0;">
<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:%s;" bgcolor="%s">

{{HEADER}}
''' % (meta.strip(), title, CSS, pre, CREAM, CREAM)
TAIL = '\n{{FOOTER}}\n\n</table>\n</td></tr>\n</table>\n</body>\n</html>\n'

def row(bg, pad, inner, align='left', cls='pad'):
    return '<tr><td class="%s" align="%s" bgcolor="%s" style="background-color:%s;padding:%s;text-align:%s;">%s</td></tr>\n' % (cls, align, bg, bg, pad, align, inner)
def txt(t, size=16, lh=25, color=BODY, weight=400, extra=''):
    return '<div style="font-family:%s;font-size:%dpx;line-height:%dpx;color:%s;font-weight:%d;%s">%s</div>' % (FF, size, lh, color, weight, extra, t)
def eyebrow(t, color=Y, align='center', extra=''):
    return txt(t, 12, 16, color, 700, 'letter-spacing:2.4px;text-transform:uppercase;text-align:%s;%s' % (align, extra))
def serif(a, b='', size=54, lh=56, color='#FFFFFF', cls='h1', align='center', extra=''):
    """Kop zoals de cookbook-titel: rechte serif, accentwoord cursief in Signal Yellow."""
    acc = '<br><i style="font-style:italic;color:%s;">%s</i>' % (Y, b) if b else ''
    return '<div class="%s" style="font-family:%s;font-size:%dpx;line-height:%dpx;font-weight:400;color:%s;letter-spacing:-0.5px;text-align:%s;%s">%s%s</div>' % (cls, SERIF, size, lh, color, align, extra, a, acc)
def img(src, alt, url=None, w=600, cls='', radius=0, shadow=False):
    st = 'display:block;margin:0 auto;width:100%%;max-width:%dpx;height:auto;border:0;%s%s' % (w, ('border-radius:%dpx;' % radius) if radius else '', 'box-shadow:0 10px 30px rgba(0,0,0,.45);' if shadow else '')
    i = '<img src="%s" width="%d" alt="%s"%s style="%s">' % (src, w, alt, (' class="%s"' % cls) if cls else '', st)
    return '<a href="%s" style="text-decoration:none;">%s</a>' % (url, i) if url else i
def gap(bg, h=24):
    return '<tr><td bgcolor="%s" style="background-color:%s;height:%dpx;line-height:%dpx;font-size:0;">&nbsp;</td></tr>\n' % (bg, bg, h, h)

def btn(label, url, w=260, fill=Y, fg=INK, border=None):
    """Pilknop geel met donkere tekst. VML-terugval voor Outlook."""
    bd = 'border:1.5px solid %s;' % border if border else ''
    return ('<table role="presentation" width="%d" cellpadding="0" cellspacing="0" border="0" style="width:100%%;max-width:%dpx;margin:0 auto;"><tr><td align="center" bgcolor="%s" style="background-color:%s;border-radius:30px;%s">'
            '<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="%s" style="height:54px;v-text-anchor:middle;width:%dpx;" arcsize="50%%" stroke="f" fillcolor="%s"><center style="color:%s;font-family:Arial,sans-serif;font-size:15px;font-weight:bold;">%s</center></v:roundrect><![endif]-->'
            '<!--[if !mso]><!--><a href="%s" style="display:block;padding:17px 14px;font-family:%s;font-size:15px;line-height:20px;font-weight:700;color:%s;text-decoration:none;white-space:nowrap;">%s&nbsp;&nbsp;&darr;</a><!--<![endif]-->'
            '</td></tr></table>') % (w, w, fill, fill, bd, url, w, fill, fg, label, url, FF, fg, label)

def two_buttons(bg, pad='22px 32px 0 32px', sub=True, subcolor='#9C978E'):
    """De twee gelijkwaardige downloadknoppen: naast elkaar op desktop, onder elkaar op mobiel."""
    t = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>'
         '<td class="col colgap" width="50%%" valign="top" style="padding-right:6px;">%s</td>'
         '<td class="col" width="50%%" valign="top" style="padding-left:6px;">%s</td></tr></table>') % (btn('Download my cookbook', COOK), btn('Download my e-book', EBOOK))
    if sub: t += txt(USE, 12, 18, subcolor, 500, 'text-align:center;padding-top:12px;')
    return row(bg, pad, t, 'center')

def P(t, bg=CREAM, pad='0 44px 16px 44px', size=17, lh=27, color=BODY, weight=400):
    return row(bg, pad, txt(t, size, lh, color, weight), 'left', 'pad lead')

def textlink(label, url, color=INK):
    return '<a href="%s" style="font-family:%s;font-size:15px;line-height:22px;font-weight:700;color:%s;text-decoration:none;border-bottom:2px solid %s;padding-bottom:2px;white-space:nowrap;">%s&nbsp;&darr;</a>' % (url, FF, color, Y, label)

def bookcard(cover, alt, eb, title, body, label, url, bg=CREAM):
    """Kaart: cover links, tekst rechts (blijft naast elkaar op mobiel, cover smaller)."""
    t = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid %s;border-radius:12px;"><tr>'
         '<td class="thtd" width="132" valign="top" style="padding:18px 0 18px 18px;">%s</td>'
         '<td class="cardtx" valign="top" style="padding:18px 18px 18px 16px;">%s%s%s<div style="padding-top:12px;">%s</div></td></tr></table>') % (
        HAIR, img(cover, alt, url, 114, 'thumb', 4), eyebrow(eb, '#A87A00', 'left'),
        '<div style="font-family:%s;font-size:23px;line-height:27px;color:%s;padding-top:6px;">%s</div>' % (SERIF, INK, title),
        txt(body, 14, 21, '#55524C', 400, 'padding-top:6px;'), textlink(label, url))
    return row(bg, '0 24px 12px 24px', t, 'left', 'padx')

def gifts(title, bg='#FFFFFF', pad='28px 44px 24px 44px', note=True):
    items = [('Mystery gift', 'Packed with your order. We&rsquo;ll keep what&rsquo;s inside a surprise.'),
             ('Giveaway', 'You&rsquo;re entered in this week&rsquo;s draw for a PFAS water filter.'),
             ('Free shipping', 'Already applied to this order.')]
    r = ''.join(('<tr><td width="22" valign="top" style="padding:8px 0 0 0;"><div style="width:8px;height:8px;border-radius:4px;background-color:%s;font-size:0;line-height:0;">&nbsp;</div></td>'
                 '<td valign="top" style="padding:0 0 12px 0;">%s</td></tr>') % (Y, txt('<b style="color:%s;font-weight:600;">%s.</b> %s' % (INK, a, b), 15, 23, '#55524C')) for a, b in items)
    h = eyebrow(title, INK, 'left', 'padding-bottom:14px;')
    h += '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % r
    if note: h += txt('When your order ships, you&rsquo;ll get a separate email with tracking.', 14, 21, GREY, 400, 'padding-top:4px;')
    return row(bg, pad, '<div style="border-top:1px solid %s;padding-top:22px;">%s</div>' % (HAIR, h), 'left', 'pad')

def ps(t, bg=CREAM, pad='4px 44px 34px 44px'):
    return row(bg, pad, txt('<b style="color:%s;">P.S.</b> %s' % (INK, t), 15, 23, '#55524C'), 'left', 'pad')

def meta(id_, sender, subj, pre, note):
    return 'ID: %s\nSENDER: %s\nSUBJECT (aanbevolen): %s\nPREVIEW (aanbevolen): %s\nLINKS: e-book = live YyaMjx/S2EMYW-link; cookbook = PLACEHOLDER {{COOKBOOK_URL}} (render: #)\nNOTITIE: %s' % (id_, sender, subj, pre, note)

def hero_duo(hero, alt, eb='Included with your order', a='Your books', b='are ready', sub='Two downloads, yours to keep.'):
    h = row(NIGHT, '34px 24px 0 24px', eyebrow(eb), 'center')
    h += row(NIGHT, '14px 24px 0 24px', serif(a, b), 'center')
    h += row(NIGHT, '12px 40px 0 40px', txt(sub, 17, 25, '#D8D3CA', 400, 'text-align:center;'), 'center')
    h += row(NIGHT, '6px 0 0 0', img(hero, alt), 'center', '')
    h += two_buttons(NIGHT, '0 32px 30px 32px')
    return h

ALT = {'cook': 'The Favorites Cookbook by Siraat: 25 recipes built from the answers of 21,000+ home cooks',
       'ebook': 'The Plastic-Free Home E-Book (The Green Clean Guide): DIY cleaning recipes and eco tips',
       'duo': 'Your two Siraat books: The Favorites Cookbook and the Plastic-Free Home E-Book, ready to download'}
files = {}

# =====================================================================
# A · Clean delivery card (twee keer: echte e-book cover en de -alt placeholder-cover)
def variant_a(altcover):
    sfx = '-alt' if altcover else ''
    m = meta('gifts-a%s · Clean delivery card%s' % (sfx, ' (placeholder-cover The Plastic-Free Home)' if altcover else ' (echte e-book cover)'),
             'Siraat', 'Your two books are ready', '25 recipes and a 90-page home guide. Yours to keep.',
             'Advies uit COPY.md. Beide knoppen boven de vouw in de hero; kaarten herhalen de downloads als tekstlink.'
             + (' Alt-cover: werkt alleen als de e-book PDF zelf ook deze cover krijgt (assets/README.md).' if altcover else ''))
    b = head(m, 'Your two books are ready', '25 recipes and a 90-page home guide. Yours to keep.')
    b += hero_duo('{{IMG}}/duo-hero%s-email.jpg' % sfx, ALT['duo'])
    b += P('Thanks for your order. Two of your gifts don&rsquo;t need a box, so here they are now.', CREAM, '30px 44px 20px 44px')
    b += bookcard('{{IMG}}/cookbook-cover.jpg', ALT['cook'], 'Book one', 'The Favorites Cookbook',
                  '25 recipes in 6 chapters, built from the answers of 21,000+ Siraat home cooks. From the perfect fried egg to a Sunday roast, with a five-step pan school, a heat guide and a fix list for when something sticks. US and metric in every recipe.',
                  'Download my cookbook', COOK)
    eb_body = '90 pages of DIY cleaning recipes, ingredient guides and eco tips for the rest of your kitchen and home.'
    eb_body += ' The cover also says The Green Clean Guide.' if altcover else ' (The cover says The Green Clean Guide. Same book.)'
    b += bookcard('{{IMG}}/ebook-cover%s.jpg' % sfx, ALT['ebook'], 'Book two', 'The Plastic-Free Home E&#8209;Book', eb_body, 'Download my e-book', EBOOK)
    b += row(CREAM, '6px 44px 0 44px', txt(USE, 12, 18, GREY, 500, 'text-align:center;'), 'center')
    b += gap(CREAM, 14)
    b += gifts('The rest of your gifts', CREAM, '14px 44px 18px 44px')
    b += ps('Start on pages 6 and 7 of the cookbook. Two minutes of pan school makes every recipe after it better.')
    return b + TAIL
files['gifts-a'] = variant_a(False)
files['gifts-a-alt'] = variant_a(True)

# =====================================================================
# B · Brief van Benjamin
m = meta('gifts-b · Warm letter from Benjamin', 'Benjamin from Siraat', 'Start with an egg',
         'Your cookbook and e-book are inside. A note from Benjamin.',
         'Afwijking van COPY.md: "Reply and tell me what you cook first. I read these." wordt "Reply and tell us what you cook first." (PLAYBOOK h12 reply-regels).')
b = head(m, 'Start with an egg', 'Your cookbook and e-book are inside. A note from Benjamin.')
b += row(NIGHT, '34px 24px 0 24px', eyebrow('A note from Benjamin'), 'center')
b += row(NIGHT, '14px 24px 0 24px', serif('Start with', 'an egg'), 'center')
b += row(NIGHT, '12px 40px 0 40px', txt('Your cookbook and e-book are inside.', 17, 25, '#D8D3CA', 400, 'text-align:center;'), 'center')
b += two_buttons(NIGHT, '24px 32px 30px 32px')
b += P("Hi {{ first_name|default:'there' }},", CREAM, '34px 44px 14px 44px')
b += P('Thank you for your order. Before your box gets to you, I wanted you to have something to cook from.')
b += P('After every order we ask a few short questions. What do you love to eat? What will you cook first? More than 21,000 of you answered. Steak won the favorite-meal question by a long way. And nearly one in three said the first thing they&rsquo;d cook was an egg, the classic &ldquo;will it stick?&rdquo; test.')
b += P('So we built a cookbook around those answers. The Favorites Cookbook has 25 recipes in 6 chapters, and it opens with the egg.')
b += row(CREAM, '0 44px 22px 44px', textlink('Download my cookbook', COOK), 'left', 'pad')
b += P('Your second book is the Plastic-Free Home E-Book (the cover says The Green Clean Guide). It&rsquo;s 90 pages of DIY cleaning recipes and ingredient guides for the rest of your home.')
b += row(CREAM, '0 44px 26px 44px', textlink('Download my e-book', EBOOK), 'left', 'pad')
tip = (eyebrow('First cook, honest tip', '#A87A00', 'left', 'padding-bottom:8px;')
       + txt('There&rsquo;s no coating on your pan, so release comes from heat and timing. Medium heat for 2 to 3 minutes, flick in a drop of water, and wait until it forms one bead that glides. Then a teaspoon of butter or oil. Skip the preheat, and the egg sticks.', 16, 25, INK))
b += row(CREAM, '0 24px 24px 24px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border-left:3px solid %s;border-radius:0 10px 10px 0;"><tr><td style="padding:18px 20px;">%s</td></tr></table>' % (Y, tip), 'left', 'padx')
b += P('Reply and tell us what you cook first.', CREAM, '0 44px 20px 44px')
b += row(CREAM, '0 44px 8px 44px', '<div style="font-family:%s;font-size:30px;line-height:32px;font-style:italic;color:%s;">Benjamin</div>' % (SERIF, INK) + txt('Founder, Siraat', 14, 20, GREY, 500, 'padding-top:4px;'), 'left', 'pad')
b += gifts('Also on your order', CREAM, '24px 44px 14px 44px')
b += ps('If an egg does stick, it&rsquo;s almost always the heat, not you. The fix list is on page 44.')
files['gifts-b'] = b + TAIL

# =====================================================================
# C · What's inside showcase
m = meta('gifts-c · What&rsquo;s inside showcase', 'Siraat', '25 recipes, 6 chapters, yours',
         'Your Favorites Cookbook and e-book are ready to download.',
         'Receptteasers aangepast aan de beschikbare uitsneden (ribeye, shrimp, pizza) in plaats van egg/shakshuka uit COPY.md; teksten uit het boek (spread p. 16 en 29) of beschrijvend zonder tijden die niet zijn gecontroleerd.')
b = head(m, '25 recipes, 6 chapters, yours', 'Your Favorites Cookbook and e-book are ready to download.')
b += row(NIGHT, '34px 24px 0 24px', eyebrow('The Favorites Cookbook'), 'center')
b += row(NIGHT, '14px 24px 0 24px', serif('Steak won.', 'Eggs came first.', 50, 53), 'center')
b += row(NIGHT, '12px 40px 0 40px', txt('25 recipes from 21,000+ home cooks.', 17, 25, '#D8D3CA', 400, 'text-align:center;'), 'center')
b += row(NIGHT, '26px 24px 0 24px', img('{{IMG}}/cookbook-cover.jpg', ALT['cook'], COOK, 280, 'cover', 6, True), 'center')
b += two_buttons(NIGHT, '28px 32px 30px 32px')
b += P('Your order came with two books. Both are ready now.', CREAM, '32px 44px 16px 44px')
b += P('We asked Siraat home cooks what they love to eat and what they&rsquo;d cook first. Steak and red meat topped the favorite-meal list at 28%. One in three said their first cook would be an egg. The Favorites Cookbook is built around those answers.', CREAM, '0 44px 24px 44px')
chips = ['Eggs &amp; Breakfast', 'Steak &amp; Red Meat', 'Fish &amp; Seafood', 'Pasta &amp; Pizza Night', 'Stir-Fries &amp; Curries', 'Chicken, Roasts &amp; Comfort']
ch = ''.join('<span style="display:inline-block;margin:0 6px 8px 0;padding:7px 12px;border:1px solid %s;border-radius:20px;font-family:%s;font-size:13px;line-height:16px;font-weight:500;color:%s;background-color:#FFFFFF;white-space:nowrap;">%s</span>' % (SOFT, FF, INK, c) for c in chips)
b += row(CREAM, '0 44px 6px 44px', eyebrow('Inside: 6 chapters', INK, 'left', 'padding-bottom:12px;') + '<div>%s</div>' % ch, 'left', 'pad')
b += P('<b style="color:%s;font-weight:600;">Plus</b> five-step pan school &middot; heat guide &middot; five pan sauces in five minutes &middot; the &ldquo;if it sticks&rdquo; fix list &middot; a weekly dinner planner' % INK, CREAM, '8px 44px 26px 44px', 15, 23, '#55524C')
recipes = [('recipe-garlic-butter-ribeye.jpg', 'Garlic-Butter Ribeye', '25 min + rest &middot; A deep brown crust, a pink middle and a butter you spoon over the top.', 'Garlic-Butter Ribeye: a seared ribeye with herb butter, garlic and thyme in a hammered titanium pan'),
           ('recipe-garlic-butter-shrimp.jpg', 'Garlic-Butter Shrimp', 'The dish on the cover. Shrimp, garlic, butter and blistered tomatoes, all in one pan.', 'Garlic-Butter Shrimp: shrimp with cherry tomatoes, garlic and basil in a hammered titanium pan'),
           ('recipe-crispy-pizza-night.jpg', 'Crispy Pizza Night', 'A crisp base and no delivery fee. A hot steel does the heavy lifting.', 'Crispy Pizza Night: a blistered margherita pizza on a steel, sliced into eight')]
rr = ''
for i, (f, n, l, a) in enumerate(recipes):
    bd = 'border-top:1px solid %s;' % HAIR if i else ''
    rr += ('<tr><td width="112" valign="middle" style="padding:14px 0;%s">%s</td><td valign="middle" style="padding:14px 0 14px 16px;%s">'
           '<div style="font-family:%s;font-size:21px;line-height:25px;color:%s;">%s</div>%s</td></tr>') % (
        bd, img('{{IMG}}/' + f, a, COOK, 100, 'rimg', 8), bd, SERIF, INK, n, txt(l, 14, 21, '#55524C', 400, 'padding-top:4px;'))
b += row(CREAM, '0 24px 4px 24px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid %s;border-radius:12px;"><tr><td style="padding:16px 18px 6px 18px;">%s<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table></td></tr></table>' % (
    HAIR, eyebrow('Three to start with', '#A87A00', 'left', 'padding-bottom:2px;'), rr), 'left', 'padx')
b += row(CREAM, '18px 44px 26px 44px', '<div style="text-align:center;">%s</div>' % textlink('Download my cookbook', COOK), 'center', 'pad')
b += bookcard('{{IMG}}/ebook-cover.jpg', ALT['ebook'], 'Book two', 'The Plastic-Free Home E&#8209;Book',
              '90 pages of DIY cleaning recipes, ingredient guides and eco tips. (The cover says The Green Clean Guide.)', 'Download my e-book', EBOOK)
b += row(CREAM, '6px 44px 0 44px', txt(USE, 12, 18, GREY, 500, 'text-align:center;'), 'center')
b += gap(CREAM, 14)
b += gifts('The rest of your gifts', CREAM, '14px 44px 18px 44px')
b += ps('Print the planner on page 47. It&rsquo;s a full week of dinners from the book, with room for your own.')
files['gifts-c'] = b + TAIL

for k, v in files.items():
    assert '—' not in v and '&mdash;' not in v, k
    body = v.split('-->', 1)[1]
    for bad in ('$', '% off', 'HI10', 'code', 'Shop', 'sale', 'I read'):
        assert bad not in re.sub(r'<[^>]+>|\{\{[^}]*\}\}', '', body).replace('28%', ''), (k, bad)
    assert 'COOKBOOK_URL' in v and EBOOK in v and '{{HEADER}}' in v and '{{FOOTER}}' in v
    open(os.path.join(N, k + '.html'), 'w').write(v)
    print('geschreven', k, len(v))
