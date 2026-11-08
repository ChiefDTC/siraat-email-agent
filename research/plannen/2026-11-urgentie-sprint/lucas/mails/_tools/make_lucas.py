"""Voorbeeldmails voor Lucas (urgentie-sprint, 8 nov 2026). Bron: ../../BRIEF-copy-per-flow.md.
Hergebruikt de helpers en de look van klaviyo/templates/v3/campaigns/urgency-1108/_tools/make_urg.py en de vaste
header/footer uit klaviyo/templates/partials/. Alleen browser-voorbeelden: niets naar Klaviyo, Rise.ai of Shopify.
Bouw:  python3 -I make_lucas.py   (daarna node shot_lucas.js voor de PNG's)"""
import os, re, html, shutil

ROOT = '/home/user/siraat-email-agent'
T = os.path.dirname(os.path.abspath(__file__)); M = os.path.dirname(T); AS = os.path.join(M, 'assets')
URG = os.path.join(ROOT, 'klaviyo/templates/v3/campaigns/urgency-1108/_tools/make_urg.py')
G = {'__file__': URG, '__name__': 'x'}; exec(open(URG).read(), G)
row, txt, al, h1, button, friction, para, quote, eyebrow, gifts_grid, gap = (G[k] for k in
    'row txt al h1 button friction para quote eyebrow gifts_grid gap'.split())
INK, CREAM, WHITE, BRICK, GOLD, GREY, HAIR, SOFT, FF, SYS = (G[k] for k in 'INK CREAM WHITE BRICK GOLD GREY HAIR SOFT FF SYS'.split())
SITE = 'https://siraatskitchen.com'; SALE = SITE + '/collections/black-friday-sale'; DUO = SITE + '/products/2-pans-and-2-lids'
CDN = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/'
IMG_DUO = CDN + 'Titanium_Hammered_Pan_Pro_15.webp?width=400&format=pjpg'
IMG_STD = CDN + 'Titanium_hammered_pan_pro_standard_b69d1fc5-43d8-40a5-9ad7-523bdddc54d4.webp?width=400&format=pjpg'
PART = os.path.join(ROOT, 'klaviyo/templates/partials')

# ------------------------------------------------------------------ assets lokaal (map is los te versturen)
os.makedirs(AS, exist_ok=True)
for f in ['gift-mystery.jpg', 'gift-shipping.jpg', 'gift-ebook.jpg', 'gift-cookbook.jpg', 'gift-filter.jpg', 'logo-black-cream.png', 'logo-white-dark.png']:
    shutil.copy(os.path.join(PART, 'shared', f), AS)
for f in ['fb.png', 'ig.png']:
    shutil.copy(os.path.join(ROOT, 'klaviyo/templates/v3/campaigns/urgency-1108/assets', f), AS)

# ------------------------------------------------------------------ bouwstenen
def ann(rows):
    """Grijze strook BOVEN de mail: hoort niet bij de mail."""
    tr = ''.join('<tr><td valign="top" style="padding:3px 12px 3px 0;font-weight:700;white-space:nowrap;color:#333;">%s</td><td valign="top" style="padding:3px 0;color:#444;">%s</td></tr>' % (k, v) for k, v in rows)
    return ('<div class="ann" style="background:#E6E6E6;border-bottom:2px solid #BDBDBD;padding:16px 16px 18px 16px;font-family:Menlo,Consolas,monospace;font-size:12px;line-height:18px;">'
            '<div style="max-width:600px;margin:0 auto;"><div style="font-size:11px;letter-spacing:1px;color:#777;padding-bottom:8px;">NOTE FOR LUCAS &middot; NOT PART OF THE EMAIL &middot; EXAMPLE BUILD 8 NOV 2026</div>'
            '<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="width:100%%;">%s</table></div></div>\n') % tr
def refs(items): return '<br>'.join('&ldquo;%s&rdquo;' % i for i in items)
def ul(items): return '<br>'.join('&middot; ' + i for i in items)
def pill(t): return ('<span style="display:inline-block;font-family:Menlo,Consolas,monospace;font-size:10px;line-height:14px;font-weight:400;letter-spacing:0;'
                     'color:#555;background:#E6E6E6;border:1px dashed #999;padding:2px 6px;vertical-align:middle;text-transform:none;">%s</span>' % t)

CSS = G['CSS'] + '    .bb{display:block!important;width:100%!important;}\n'
def page(title, pre, annotation, body, prefix='assets', letter=False):
    w = 560 if letter else 600
    font = '' if letter else "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');"
    h = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
         '<meta name="color-scheme" content="light">\n<title>%s</title>\n<style>\n  %s\n  body{margin:0;padding:0;background:#FFFFFF;-webkit-text-size-adjust:100%%;}\n'
         '  table{border-collapse:collapse;}\n  img{border:0;display:block;line-height:100%%;outline:none;text-decoration:none;}\n  h1{margin:0;padding:0;}\n  a{color:#272727;}\n'
         '  @media only screen and (max-width:620px){%s  }\n</style>\n</head>\n<body style="margin:0;padding:0;background:#FFFFFF;">\n%s'
         '<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;">%s</div>\n'
         '<!-- ======== EMAIL START ======== -->\n<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF">\n<tr><td align="center" style="padding:%s;">\n'
         '<table role="presentation" class="w" width="%d" cellpadding="0" cellspacing="0" border="0" style="width:%dpx;max-width:%dpx;background:#FFFFFF;" bgcolor="#FFFFFF">\n'
         '%s\n</table>\n</td></tr>\n</table>\n<!-- ======== EMAIL END ======== -->\n</body>\n</html>\n') % (
        html.escape(title), font, CSS, annotation, pre, '0 0 32px 0' if not letter else '0 0 32px 0', w, w, w, body)
    h = h.replace('{{SHARED}}', prefix).replace('{{IMG}}', prefix)
    # Klaviyo-tags van de vaste footer leesbaar maken voor de browser
    h = re.sub(r"\{% today '[^']*' as sk_ref %\}<span[^>]*>ref \{\{ sk_ref \}\}</span>", '', h)
    for a, b in [('{% unsubscribe_link %}', '#unsubscribe'), ('{% manage_preferences_link %}', '#preferences'), ('{% web_view_link %}', '#webview'),
                 ('{{ organization.name }}', "Siraat&#39;s Kitchen"), ('{{ organization.full_address }}', '[company address]')]:
        h = h.replace(a, b)
    return h

HEADER = open(os.path.join(PART, 'header.html')).read()
FOOTER = open(os.path.join(PART, 'footer.html')).read()
def topbar(t, href):
    return ('<tr><td align="center" bgcolor="%s" style="background-color:%s;padding:0;text-align:center;"><a href="%s" class="tb" style="display:block;padding:12px 20px;'
            'font-family:%s;font-size:12px;line-height:16px;letter-spacing:1.6px;font-weight:800;color:#FFFFFF;text-decoration:none;text-transform:uppercase;">%s</a></td></tr>\n%s\n') % (INK, INK, href, FF, t, HEADER)

def stockline(bg=WHITE, dark=False, pad='12px 40px 0 40px'):
    c = '#FFFFFF' if dark else INK
    t = '<span style="color:#2E7D32;font-size:14px;">&#9679;</span>&nbsp; <b>In stock.</b> Free shipping, duties paid.'
    return row(bg, pad, txt(t, 14, 20, c, 500, 'text-align:center;'), 'center')

def counter(bg=WHITE, dark=False, pad='12px 40px 0 40px'):
    c = '#FFFFFF' if dark else INK
    t = '<b>2,140 orders</b> since Nov 1 &nbsp;' + pill('EXAMPLE NUMBER, live from Shopify')
    return row(bg, pad, txt(t, 14, 22, c, 500, 'text-align:center;'), 'center')

def countdown(bg=INK, pad='18px 40px 4px 40px'):
    box = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#1B1B1B" style="background-color:#1B1B1B;border:2px dashed %s;border-radius:8px;">'
           '<tr><td align="center" style="padding:22px 16px;height:86px;">'
           '<div style="font-family:%s;font-size:30px;line-height:36px;font-weight:800;letter-spacing:4px;color:#FFFFFF;">07 : 42 : 10</div>'
           '<div style="font-family:%s;font-size:10px;line-height:14px;letter-spacing:3px;color:%s;padding-top:2px;">HRS &nbsp;&nbsp;&nbsp;&nbsp; MIN &nbsp;&nbsp;&nbsp;&nbsp; SEC</div>'
           '<div style="padding-top:10px;">%s</div></td></tr></table>') % (GOLD, FF, FF, SOFT, pill('IMAGE: Live countdown GIF (Sendtric) to the real end time, 600 x 150'))
    return row(bg, pad, box, 'center')

def cartcard(lines, total_label, total, href, bg=WHITE, pad='0 40px 0 40px', note=''):
    """Cart/productblok. lines = [(img, naam, detail, prijs)]."""
    r = ''
    for img, name, det, price in lines:
        r += ('<tr><td width="96" valign="middle" style="padding:14px 0 14px 14px;"><img src="%s" width="96" alt="%s" style="display:block;width:96px;height:96px;object-fit:cover;border-radius:6px;border:0;"></td>'
              '<td valign="middle" style="padding:14px 14px 14px 14px;text-align:left;"><div style="font-family:%s;font-size:16px;line-height:21px;font-weight:700;color:%s;">%s</div>'
              '<div style="font-family:%s;font-size:13px;line-height:19px;color:%s;padding-top:3px;">%s</div></td>'
              '<td valign="middle" align="right" style="padding:14px 14px 14px 0;font-family:%s;font-size:16px;line-height:21px;font-weight:700;color:%s;white-space:nowrap;">%s</td></tr>') % (
            img, name, FF, INK, name, FF, GREY, det, FF, INK, price)
    r += ('<tr><td colspan="3" style="border-top:1px solid %s;padding:12px 14px;font-family:%s;font-size:15px;line-height:21px;color:%s;">'
          '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td style="font-family:%s;font-size:15px;color:%s;">%s</td>'
          '<td align="right" style="font-family:%s;font-size:17px;font-weight:800;color:%s;white-space:nowrap;">%s</td></tr></table></td></tr>') % (
        HAIR, FF, INK, FF, INK, total_label, FF, INK, total)
    t = ('<a href="%s" style="display:block;text-decoration:none;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" '
         'style="background-color:#FFFFFF;border:1px solid %s;border-radius:10px;">%s</table></a>') % (href, HAIR, r)
    if note: t += '<div style="padding-top:8px;text-align:left;">%s</div>' % pill(note)
    return row(bg, pad, t, 'left')

def anchor(bg=CREAM, href=DUO, title='The honest math'):
    h = txt(title.upper(), 12, 16, BRICK, 700, 'letter-spacing:2px;text-align:center;padding-bottom:12px;')
    cells = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>'
             '<td width="50%%" valign="top" style="padding:0 5px 0 0;"><a href="%s" style="display:block;text-decoration:none;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background:#FFFFFF;border:1px solid %s;border-radius:10px;">'
             '<tr><td><img src="%s" width="255" alt="Pan Pro Standard" style="display:block;width:100%%;height:auto;border-radius:10px 10px 0 0;"></td></tr>'
             '<tr><td style="padding:12px;"><div style="font-family:%s;font-size:15px;font-weight:700;color:%s;">Pan Pro Standard</div><div style="font-family:%s;font-size:14px;color:%s;padding-top:4px;">One pan: <b>$144</b></div></td></tr></table></a></td>'
             '<td width="50%%" valign="top" style="padding:0 0 0 5px;"><a href="%s" style="display:block;text-decoration:none;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background:#FFFFFF;border:2px solid %s;border-radius:10px;">'
             '<tr><td><img src="%s" width="255" alt="2 Pans + 2 Lids" style="display:block;width:100%%;height:auto;border-radius:10px 10px 0 0;"></td></tr>'
             '<tr><td style="padding:12px;"><div style="font-family:%s;font-size:15px;font-weight:700;color:%s;">2 Pans + 2 Lids</div><div style="font-family:%s;font-size:14px;color:%s;padding-top:4px;">Four pieces: <b>$199</b></div></td></tr></table></a></td>'
             '</tr></table>') % (SITE + '/products/titanium-hammered-pan-pro-standard', HAIR, IMG_STD, FF, INK, FF, INK, href, INK, IMG_DUO, FF, INK, FF, INK)
    h += cells + txt('One pan is $144. Four pieces: $199.', 17, 24, INK, 700, 'text-align:center;padding-top:16px;')
    return row(bg, '28px 40px 26px 40px', h, 'center')

def deadline_box(t, sub, bg=WHITE, note='', pad='22px 40px 0 40px'):
    inner = ''
    if note: inner += '<div style="padding-bottom:10px;">%s</div>' % pill(note)
    inner += txt(t, 18, 24, BRICK, 800, 'text-align:center;') + (txt(sub, 14, 21, GREY, 500, 'text-align:center;padding-top:4px;') if sub else '')
    box = ('<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="%s" style="background-color:%s;border:1px dashed #999;border-radius:8px;">'
           '<tr><td style="padding:16px 18px;">%s</td></tr></table>') % (CREAM, CREAM, inner)
    return row(bg, pad, box, 'center')

SCOTT = ('These hammered Titanium pans from Siraat have been the best we have owned yet... the last pans we ever have to purchase.', 'Scott Y.')
TAMMY = ("I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns.", 'Tammy')
STEVEN = ('I returned my pans, unused, and received a refund, no questions asked.', 'Steven T.')
GWEN = ('Awesome pan and peace of mind that I am not ingesting bits of toxins when I cook.', 'Gwen')
LOUISE = ("A gift for my daughter who loves to cook... I can't wait to finish work, and go home to cook.", 'Louise T.')
REVNOTE = 'Review: verbatim from content/reviews/reviews.csv (Trustpilot, 5 stars, %s). Universal Content block "%s".'

def hero(bg, eb, title, sub, href, dark):
    inner = eyebrow(eb, href, dark) + h1(title, href, '#FFFFFF' if dark else INK)
    if sub: inner += txt(sub, 17, 24, SOFT if dark else '#4A4A4A', 500, 'padding-top:10px;')
    return row(bg, '26px 40px 20px 40px', inner, 'left')

def ps_(t, href, bg=WHITE):
    return row(bg, '6px 40px 26px 40px', al(t, href, 15, 23, INK, 400, 'font-style:italic;'), 'left')

# ------------------------------------------------------------------ platte brief (Benjamin)
LS = 'font-family:%s;font-size:17px;line-height:26px;color:%s;' % (SYS, INK)
MINFOOT = G['MINFOOT']
def letter(paras):
    out = ''
    for i, p in enumerate(paras):
        pad = '28px 40px 14px 40px' if i == 0 else '0 40px 14px 40px'
        if p.startswith('LINK:'):
            label, href = p[5:].split('|')
            out += ('<tr><td class="lt" style="padding:0 40px 16px 40px;%s"><a href="%s" style="font-family:%s;font-size:18px;line-height:24px;font-weight:700;color:%s;text-decoration:underline;">%s</a></td></tr>\n') % (LS, href, SYS, BRICK, label)
        else:
            out += '<tr><td class="lt" style="padding:%s;%s">%s</td></tr>\n' % (pad, LS, p)
    return out + MINFOOT

def letter_ann(flow, fid, pos, subj, pre, ref, notes, sender='Benjamin from Siraat'):
    return ann([('Flow', '%s &middot; Klaviyo flow <b>%s</b>' % (flow, fid)), ('Position', pos), ('From', sender), ('Subject', subj), ('Preview', pre),
                ('Replaces reference:', ref), ('Implementation', ul(notes))])

def mail_ann(flow, fid, pos, subj, pre, ref, notes):
    return ann([('Flow', '%s &middot; Klaviyo flow <b>%s</b>' % (flow, fid)), ('Position', pos), ('Subject', subj), ('Preview', pre),
                ('Replaces reference:', ref), ('Implementation', ul(notes))])

FILES = {}
GIFTS_NOTE = 'The filter is a chance to win in our weekly draw. The rest comes with every order.'

# ================================================================== 1 checkout e1
def checkout_e1():
    L = SITE + '/cart'
    a = mail_ann('v4 &middot; Checkout abandonment', 'QUBUQV', 'Email 1 (first send after Started Checkout, current flow timing unchanged)',
                 'Your checkout is still open: extra 10% applied', 'Finish in one click.',
                 refs(['Your order is pending.', "pricing is tied to today's flash sale and will expire SOON", 'pending orders not completed within 24 hours will be marked as canceled',
                       'Your foundation order is pending.', 'running pretty low on stock', "selling out fast, but the deal's still live", 'only available while current stock lasts',
                       'This exclusive sale is set to end very soon']),
                 ['Cart block: dynamic from <code>event.extra.line_items</code> (image, title, price); example shows 2 Pans + 2 Lids at the current site price $199.',
                  'Button link: <code>{{ event.extra.responsive_checkout_url }}&amp;discount=BFCODE</code> (BFCODE = placeholder, real code never in the repo).',
                  'Stock line: fixed text "In stock. Free shipping, duties paid." Show a low-stock line only if Shopify inventory is really low.',
                  'Deadline block: conditional, <code>{% if today == 2026-11-30 %}</code> (show block only on the real last day). Universal Content block "BF last-day line".',
                  REVNOTE % ('R583', 'Review Scott Y.'), '5 gifts: Universal Content block "5 gifts (US)"; $555 only in USD mails.'])
    b = topbar('Your extra 10% is applied at checkout', L)
    b += hero(INK, 'YOUR CHECKOUT', 'Still open.<br>Extra 10% applied.', 'Finish in one click. Everything is saved the way you left it.', L, True)
    b += cartcard([(IMG_DUO, '2 Pans + 2 Lids', 'Pan Pro Standard + Mini, 2 lids &middot; Qty 1', '$199')], 'Extra 10% (BFCODE), applied', '$179.10', L, INK, '0 40px 0 40px',
                  'Dynamic: line items from the checkout event')
    b += stockline(INK, True, '14px 40px 0 40px')
    b += button('Complete my order', L, INK, True, '18px 40px 0 40px') + friction('Free shipping. 30-day returns. 100,000+ happy customers.', INK, True, '10px 40px 24px 40px')
    b += deadline_box('VIP Sale ends tonight at 11:59 PM ET.', 'After that, your extra 10% and the sale price are gone. Free shipping and 30-day returns stay.', WHITE,
                      'CONDITIONAL: only on Nov 30, the real last day', '26px 40px 4px 40px')
    b += gap(WHITE, 18)
    b += para('You picked the two pans most people cook with every day, and both lids. Same pure titanium cooking surface, no coatings, nothing to wear off.')
    b += quote(*SCOTT, L)
    b += gifts_grid(True, L, WHITE, 'SHIPS WITH THIS ORDER', None, GIFTS_NOTE)
    b += button('Complete my order', L, WHITE, pad='4px 40px 0 40px') + friction('Free shipping. 30-day returns. 100,000+ happy customers.', WHITE, pad='10px 40px 28px 40px')
    b += FOOTER
    return page('Your checkout is still open: extra 10% applied', 'Finish in one click.', a, b)

# ================================================================== 2 checkout last (Benjamin)
def checkout_last():
    L = SITE + '/cart'
    a = letter_ann('v4 &middot; Checkout abandonment', 'QUBUQV', 'Last email of the flow (replaces the current last checkout mail)',
                   'Benjamin here: a quick note before it ends', 'Reply and tell me what you cook. I read these.',
                   refs(['Your order is pending.', 'pending orders not completed within 24 hours will be marked as canceled', 'This exclusive sale is set to end very soon']),
                   ['Plain text letter: no header, no logo, no images, minimal footer (unsubscribe, preferences, address). Same format as the affiliate letters; Floris to confirm this exception in DECISIONS.md.',
                    'No "Re:" or "Fwd:" in the subject. Reply-to must be an inbox that is really read.',
                    'Deadline sentence: conditional on the real last day (Nov 30). On other days use the version without "tonight": "The VIP Sale runs until Nov 30, 11:59 PM ET."',
                    'Product name: <code>{{ event.extra.line_items.0.product.title }}</code>; example 2 Pans + 2 Lids. Link: checkout URL + <code>&amp;discount=BFCODE</code>.',
                    'Universal Content block "Benjamin signature".'])
    body = letter(['Hi there,',
                   'Benjamin here, the founder of Siraat. You left the 2 Pans + 2 Lids in your checkout, and I wanted to send one quick note before the VIP Sale ends tonight at 11:59 PM ET.',
                   'Your extra 10% is still applied. One pan on its own is $144. The four pieces are $199, and the 10% comes off that at checkout.',
                   'LINK:&rarr; Finish my checkout|' + L,
                   'After 11:59 PM ET the sale price is over. Free shipping and 30-day returns stay, so if the pans are not for you, you send them back.',
                   'If something held you back, a question about sizes, induction or anything else, just hit reply. Reply and tell me what you cook. I read these.',
                   'Benjamin<br>Founder, Siraat'])
    return page('Benjamin here: a quick note before it ends', 'Reply and tell me what you cook. I read these.', a, body, letter=True)

# ================================================================== 3 cart last day
def cart_lastday():
    L = SITE + '/cart'
    a = mail_ann('v4 &middot; Cart abandonment', 'TZG9Mx', 'Last-day version of cart email 1 (same position, swapped in by date)',
                 'VIP Sale ends tonight at 11:59 PM ET', 'Ends tonight 11:59 PM ET. 2 Pans + 2 Lids $199.',
                 refs(['Found your new make-up?', "the sale we're running right now ends tonight at midnight", 'No extensions this time.', 'running pretty low on stock',
                       "selling out fast, but the deal's still live", 'Final hours', 'ends tonight', 'use it or lose it']) + '<br>+ countdownmail.com timer',
                 ['Date condition: send this version only on Nov 30 (conditional split on today, or two message variants). Before Nov 30 the normal v4 cart mail goes out.',
                  'Countdown: Sendtric (or NiftyImages) GIF to Nov 30 2026, 11:59 PM ET. After the end it shows "SALE ENDED". Universal Content block "BF countdown".',
                  'Cart block: dynamic from <code>event</code> Added to Cart items; example 2 Pans + 2 Lids $199. Link: cart URL with <code>?discount=BFCODE</code>.',
                  'Stock line fixed; low-stock only if Shopify inventory is really low.', REVNOTE % ('R138', 'Review Tammy')])
    b = topbar('VIP Sale ends tonight at 11:59 PM ET', L)
    b += hero(INK, 'LAST DAY', 'VIP Sale ends tonight at 11:59 PM ET', 'Your cart is saved. The sale price is not, after tonight.', L, True)
    b += countdown(INK, '4px 40px 18px 40px')
    b += cartcard([(IMG_DUO, '2 Pans + 2 Lids', 'Pan Pro Standard + Mini, 2 lids &middot; Qty 1', '$199')], 'Your cart', '$199', L, INK, '0 40px 0 40px', 'Dynamic: items from the cart event')
    b += stockline(INK, True, '14px 40px 0 40px')
    b += button('Return to my cart', L, INK, True, '18px 40px 0 40px') + friction('Free shipping. 30-day returns. 100,000+ happy customers.', INK, True, '10px 40px 24px 40px')
    b += gap(WHITE, 8) + anchor(WHITE)
    b += quote(*TAMMY, L)
    b += gifts_grid(True, L, WHITE, 'SHIPS WITH THIS ORDER', None, GIFTS_NOTE)
    b += button('Return to my cart', L, WHITE, pad='4px 40px 0 40px') + friction('Free shipping. 30-day returns. 100,000+ happy customers.', WHITE, pad='10px 40px 28px 40px')
    b += FOOTER
    return page('VIP Sale ends tonight at 11:59 PM ET', 'Ends tonight 11:59 PM ET. 2 Pans + 2 Lids $199.', a, b)

# ================================================================== 4 BFCM welcome last day
def bfcm_lastday():
    L = SALE
    a = mail_ann('BFCM Welcome (Rn556d) + BF follow-up (YqKCmH)', 'Rn556d / YqKCmH', 'Last-day version of the next email in each flow (swapped in by date)',
                 'VIP Sale ends tonight at 11:59 PM ET', 'Ends tonight 11:59 PM ET. 2 Pans + 2 Lids $199.',
                 refs(['Found your new make-up?', "the sale we're running right now ends tonight at midnight", 'No extensions this time.', '(1) Your store credit is updated.',
                       'Your [amount] is about to disappear', 'Final hours']) + '<br>+ countdownmail.com timer',
                 ['Date condition: only on Nov 30, the real last day.',
                  'Countdown: Sendtric GIF to Nov 30 2026 11:59 PM ET, then "SALE ENDED". Universal Content block "BF countdown".',
                  'Order counter: real number from Shopify (orders since Nov 1), refreshed before send or via a profile/feed property. <b>2,140 is an example number.</b> No counter if the data is not live.',
                  'Prices: current site prices only ($144 Pan Pro Standard, $199 2 Pans + 2 Lids). No compare-at in this mail.',
                  '5 gifts: Universal Content block "5 gifts (US)".', REVNOTE % ('R583', 'Review Scott Y.')])
    b = topbar('VIP Sale ends tonight at 11:59 PM ET', L)
    b += hero(INK, 'BLACK FRIDAY &middot; LAST DAY', 'Ends tonight.<br>11:59 PM ET.', 'Up to 70% off, plus 5 free gifts with every order.', L, True)
    b += countdown(INK, '4px 40px 6px 40px')
    b += counter(INK, True, '10px 40px 0 40px')
    b += button('Shop the VIP Sale', L, INK, True, '18px 40px 0 40px') + friction('Free shipping. 30-day returns. 100,000+ happy customers.', INK, True, '10px 40px 24px 40px')
    b += anchor(CREAM, DUO, 'Most picked this week')
    b += gifts_grid(True, L, WHITE, 'WITH EVERY ORDER, UNTIL TONIGHT', None, GIFTS_NOTE)
    b += quote(*SCOTT, L)
    b += row(WHITE, '24px 40px 16px 40px', txt('Order before 11:59 PM ET tonight and all five gifts ship with it.', 17, 24, BRICK, 700, 'text-align:center;'), 'center')
    b += button('Shop the VIP Sale', L, WHITE, pad='0 40px 0 40px') + friction('Free shipping. 30-day returns. 100,000+ happy customers.', WHITE, pad='10px 40px 28px 40px')
    b += FOOTER
    return page('VIP Sale ends tonight at 11:59 PM ET', 'Ends tonight 11:59 PM ET. 2 Pans + 2 Lids $199.', a, b)

# ================================================================== 5 ended
def ended():
    L = SITE + '/collections/cookware'
    a = mail_ann('Checkout (QUBUQV), Cart (TZG9Mx), BFCM Welcome (Rn556d), BF follow-up (YqKCmH), BF campaigns', 'QUBUQV / TZG9Mx / Rn556d / YqKCmH',
                 'Auto-switch: replaces any sale mail that would send after Nov 30, 11:59 PM ET (and the day-after campaign)',
                 "It ended. Here's what's still on.", 'The flash price is over. Free shipping and 30-day returns stay.',
                 refs(['(1) Your store credit is updated.', 'I extended your credit with just 24 hours (until tonight)... cannot be extended again']),
                 ['Date condition: <code>{% if today &gt; 2026-11-30 %}</code> show this version instead of the sale version (or a split on date in each flow).',
                  'Nothing is extended. No code, no countdown, no gifts (they ended with the sale).',
                  'Prices shown live from the site, no compare-at.', 'Universal Content block "BF ended".', REVNOTE % ('R273', 'Review Steven T.')])
    b = topbar('The VIP Sale has ended', L)
    b += hero(WHITE, 'THE SALE IS OVER', "It ended.<br>Here's what's still on.", 'The flash price is over. Free shipping and 30-day returns stay.', L, False)
    items = [('Free shipping', 'On every order, duties paid.'), ('30-day returns', 'Cook with it. Not for you? Send it back.'),
             ('75-year warranty', 'On every pan, from the day it arrives.'), ('In stock', 'Ships now, no waiting list.')]
    t = ''.join('<tr><td style="border-top:1px solid %s;padding:14px 4px;"><div style="font-family:%s;font-size:16px;line-height:22px;font-weight:700;color:%s;">&#10003;&nbsp; %s</div>'
                '<div style="font-family:%s;font-size:14px;line-height:20px;color:%s;padding:2px 0 0 22px;">%s</div></td></tr>' % (HAIR, FF, INK, k, FF, GREY, v) for k, v in items)
    b += row(WHITE, '0 40px 6px 40px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="border-bottom:1px solid %s;">%s</table>' % (HAIR, t))
    b += button('See the cookware', L, WHITE, pad='18px 40px 0 40px') + friction('Free shipping. 30-day returns. 100,000+ happy customers.', WHITE, pad='10px 40px 26px 40px')
    b += para('We will not pretend the sale is still running. If you were waiting for it, it is done, and the next one is not planned yet. What you get with every pan stays the same: a pure titanium cooking surface, no coatings, lab tested for PFAS.')
    b += quote(*STEVEN, L)
    b += gap(WHITE, 10) + FOOTER
    return page("It ended. Here's what's still on.", 'The flash price is over. Free shipping and 30-day returns stay.', a, b)

# ================================================================== 6 welcome w1
def welcome_w1():
    L = SALE
    a = mail_ann('v4 &middot; Welcome', 'T4a5Mk', 'Email 1 (also used as subject line in BFCM Welcome Rn556d and BF follow-up YqKCmH)',
                 '5 free gifts with every order, until tonight', 'Mystery gift, two books and a draw entry. $555 value.',
                 refs(['(1) Your store credit is updated.']),
                 ['"until tonight" only on the real last day (Nov 30). Other days: subject "5 free gifts with every order, until Nov 30".',
                  'Gifts: Universal Content block "5 gifts (US)" (4 tiles + PFAS filter tile centred). "$555 value" only in USD mails; INT without amount.',
                  'Filter is always "chance to win", never free.', REVNOTE % ('R563', 'Review Louise T.')])
    b = topbar('5 free gifts with every order', L)
    b += hero(INK, 'WELCOME TO SIRAAT', '5 free gifts with every order', 'Mystery gift, two books, free shipping and a draw entry for a PFAS water filter. $555 value, until tonight.', L, True)
    b += button('Claim my 5 gifts', L, INK, True, '6px 40px 0 40px') + friction('Free shipping. 30-day returns. 100,000+ happy customers.', INK, True, '10px 40px 24px 40px')
    b += gifts_grid(True, L, WHITE, 'WITH EVERY ORDER', None, GIFTS_NOTE)
    b += para('Siraat makes the original hammered titanium pan: a pure titanium cooking surface, no coatings, nothing to flake into your food. Light Labs tested it for PFAS. Report no. 25895.')
    b += anchor(CREAM)
    b += quote(*LOUISE, L, WHITE)
    b += button('Claim my 5 gifts', L, WHITE, pad='4px 40px 0 40px') + friction('Free shipping. 30-day returns. 100,000+ happy customers.', WHITE, pad='10px 40px 28px 40px')
    b += FOOTER
    return page('5 free gifts with every order, until tonight', 'Mystery gift, two books and a draw entry. $555 value.', a, b)

# ================================================================== 7 welcome founder
def welcome_founder():
    a = letter_ann('v4 &middot; Welcome', 'T4a5Mk', 'Founder email (plain text, after W1)', 'Benjamin here: a quick note before it ends', 'Reply and tell me what you cook. I read these.',
                   refs(['(1) Your store credit is updated.']) + ' (no "Re:"/"Fwd:" tricks)',
                   ['Plain text letter: no header, no logo, minimal footer. Floris to confirm the exception in DECISIONS.md.',
                    'Sale sentence conditional on the real last day; other days: "The VIP Sale runs until Nov 30, 11:59 PM ET."',
                    'Reply-to must be an inbox that is really read (otherwise drop "I read these").', 'Universal Content block "Benjamin signature".'])
    body = letter(['Hi there,',
                   'Benjamin here, the founder of Siraat. Thanks for joining.',
                   'We shipped our first hammered titanium pans on 20 December 2024. The idea was simple: a pure titanium cooking surface, no coating that can wear off. Since then more than 100,000 people cook with one.',
                   'The VIP Sale ends tonight at 11:59 PM ET. One pan is $144. Two pans and two lids are $199. Every order ships free with 5 gifts, and you have 30 days to send it back.',
                   'LINK:&rarr; See the VIP Sale|' + SALE,
                   'One question before you go: what do you cook most? Reply and tell me what you cook. I read these.',
                   'Benjamin<br>Founder, Siraat'])
    return page('Benjamin here: a quick note before it ends', 'Reply and tell me what you cook. I read these.', a, body, letter=True)

# ================================================================== 9 sunset
def sunset():
    a = letter_ann('v4 &middot; Sunset', 'TbYQmX', 'Sunset email (plain text, to profiles without opens or clicks in the sunset window)',
                   'Benjamin here: a quick note before it ends', 'Reply and tell me what you cook. I read these.', '(no reference copy for Sunset in the brief; tone follows the founder letter)',
                   ['Plain text letter, no header, minimal footer. Floris to confirm.', 'Link "Keep me on the list" = tracked click; profiles that click stay, the rest is suppressed after the current wait step.',
                    'Sale sentence conditional on the real last day; outside the sale drop that paragraph.', 'Universal Content block "Benjamin signature".'])
    body = letter(['Hi there,',
                   'Benjamin here, from Siraat. You have not opened our emails in a while, and that is fine. I would rather send fewer emails than ones nobody wants.',
                   'So this is a quick note before it ends. If you still want to hear from us, one click keeps you on the list:',
                   'LINK:&rarr; Keep me on the list|' + SITE,
                   'If not, you do not have to do anything. We will stop emailing you in a few days.',
                   'One more thing, in case it helps: the VIP Sale ends tonight at 11:59 PM ET. Free shipping, 30-day returns and a 75-year warranty on every pan.',
                   'And if you cook with one of our pans already, reply and tell me what you cook. I read these.',
                   'Benjamin<br>Founder, Siraat'])
    return page('Benjamin here: a quick note before it ends', 'Reply and tell me what you cook. I read these.', a, body, letter=True)

# ================================================================== 8 redeem (4 varianten, mails/redeem/)
SMOOCHE = refs(['(1) Your store credit is updated.', 'This is a little bit urgent. I saw your store credit expired yesterday.',
                'I really did not want to just have you lose $12.24, it was already yours.',
                'I know Halloween weekends can get busy, so I extended your credit with just 24 hours (until tonight).',
                'Please note: your credit cannot be extended again. After tonight it will disappear.']) + ' (subject of the Smooche letter: "(1) Your store credit is updated.")'
CODE = 'SIR-7K2Q9'
CODEPILL = pill('EXAMPLE CODE, real one = {% coupon_code \'SIRAAT12\' %}')
RED_IMPL = ['Code: unique Klaviyo coupon <code>{% coupon_code \'SIRAAT12\' %}</code> (one code per profile), backed by a Shopify discount: fixed $12 off, one use per customer, ends Nov 30 2026 11:59 PM ET. "SIR-7K2Q9" is an example, never a real code. Not Rise.ai.',
            'Expiry in the mail must equal the real end date of the Shopify discount. Nothing is extended, ever.',
            'Flow trigger and audience: to be decided by Floris (new flow, e.g. past buyers; optionally v4 &middot; Winback UyFc78).',
            'Redeem link: <code>https://siraatskitchen.com/discount/{% coupon_code \'SIRAAT12\' %}?redirect=/collections/black-friday-sale</code> (Klaviyo reuses the same code within one message).',
            '"Account:" line = <code>{{ email }}</code>; example shows you@example.com.']
def redeem_letter(reminder):
    subj = 'Your $12 code expires tonight at 11:59 PM ET' if reminder else 'You have $12 to spend at Siraat'
    pre = 'Code inside. Works until 11:59 PM ET tonight.' if reminder else 'Your code is inside. It works until Sunday 30 November, 11:59 PM ET.'
    a = letter_ann('NEW &middot; Redeem ($12 code)', 'new flow, ID after creation', 'Email 2 (last day, Nov 30)' if reminder else 'Email 1',
                   subj, pre, SMOOCHE,
                   RED_IMPL + ['Plain letter, no header and no logo at the top (approved for this letter), fixed minimal footer.'] +
                   (['Send on Nov 30 only, to profiles that did not use the code (filter: code not redeemed / Placed Order with discount since flow start = 0).'] if reminder else []))
    info = ('<b>Account:</b> you@example.com<br><b>Credit:</b> $12<br><b>Expiry date:</b> Sunday 30 November, 11:59 PM ET')
    L = SALE
    if reminder:
        ps = ['Hi there,', info,
              'Benjamin here. A short reminder: your $12 code expires tonight at 11:59 PM ET.',
              'You got it because you have ordered from us before. It works on anything on the site, and it comes off at checkout.',
              'Your code: <b style="font-size:19px;letter-spacing:1px;">%s</b> %s' % (CODE, CODEPILL),
              'LINK:Click here to redeem your $12.|' + L,
              'After 11:59 PM ET tonight the code stops working. That is the real end date, it will not be moved.',
              'Benjamin<br>Founder, Siraat']
    else:
        ps = ['Hi there,', info,
              'Benjamin here. You have ordered from Siraat before, so I made you a $12 code to use on your next order.',
              'It works on anything on the site and comes off at checkout. It is yours until Sunday 30 November, 11:59 PM ET. After that it expires.',
              'Your code: <b style="font-size:19px;letter-spacing:1px;">%s</b> %s' % (CODE, CODEPILL),
              'LINK:Click here to redeem your $12.|' + L,
              'If you have a question about a pan or a size, just reply.',
              'Benjamin<br>Founder, Siraat']
    return page(subj, pre, a, letter(ps), '../assets', letter=True)

def credit_card(sub):
    c = txt('YOUR CODE', 12, 16, BRICK, 700, 'letter-spacing:2px;')
    c += '<div class="bigc" style="font-family:%s;font-size:64px;line-height:68px;font-weight:800;letter-spacing:-2px;color:%s;padding-top:6px;">$12</div>' % (FF, INK)
    c += txt('off your next order', 20, 26, INK, 700)
    c += ('<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin-top:14px;border:2px dashed %s;border-radius:8px;"><tr><td style="padding:10px 18px;font-family:%s;font-size:22px;line-height:28px;font-weight:800;letter-spacing:3px;color:%s;">%s</td></tr></table>') % (GOLD, FF, INK, CODE)
    c += '<div style="padding-top:8px;">%s</div>' % CODEPILL
    c += txt(sub, 14, 20, GREY, 500, 'padding-top:10px;')
    c += txt('Expires Sunday 30 November, 11:59 PM ET.', 16, 22, BRICK, 700, 'padding-top:8px;')
    return row(WHITE, '0 40px 18px 40px', '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="border:1px solid %s;border-radius:8px;"><tr><td style="padding:20px;">%s</td></tr></table>' % (HAIR, c))

def steps():
    s = [('1', 'Tap "Use my $12". The code is applied for you.'), ('2', 'Pick anything on the site.'), ('3', 'The $12 comes off at checkout.')]
    t = ''.join('<tr><td width="36" valign="top" style="padding:8px 0;"><div style="width:28px;height:28px;border-radius:14px;background:%s;color:#FFFFFF;font-family:%s;font-size:14px;line-height:28px;font-weight:800;text-align:center;">%s</div></td>'
                '<td valign="middle" style="padding:8px 0;font-family:%s;font-size:16px;line-height:22px;color:%s;">%s</td></tr>' % (INK, FF, n, FF, INK, v) for n, v in s)
    return row(CREAM, '24px 40px 22px 40px', txt('HOW IT WORKS', 12, 16, BRICK, 700, 'letter-spacing:2px;padding-bottom:8px;') + '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table>' % t)

def redeem_designed(stack):
    L = SALE
    subj = 'Your $12 works on top of the sale' if stack else 'You have $12 to spend at Siraat'
    pre = 'Plus 5 free gifts and free shipping. Until Nov 30, 11:59 PM ET.' if stack else 'A thank-you for your past orders. Works until Nov 30, 11:59 PM ET.'
    extra = (['Stacking: DECISIONS 19 okt says unique flow codes may stack on the sale (50 and 70% off), and gifts and free shipping come with every order. '
              '<b>Check with Floris whether SIRAAT12 stacks</b> and set "Combines with: product discounts" on the Shopify discount before this goes live.'] if stack else [])
    a = mail_ann('NEW &middot; Redeem ($12 code)', 'new flow, ID after creation', 'Designed variant (A/B against the plain letter)' + (', stack version' if stack else ''),
                 subj, pre, SMOOCHE, RED_IMPL + ['Fixed header and footer.', '5 gifts: Universal Content block "5 gifts (US)".'] + extra + [REVNOTE % ('R138', 'Review Tammy')])
    b = topbar('Your $12 code expires Nov 30, 11:59 PM ET', L)
    b += hero(WHITE, 'FOR PAST CUSTOMERS', 'Your $12 to spend' if not stack else '$12 on top of<br>the VIP Sale', 'A thank-you for your past orders. Applied at checkout.', L, False)
    b += credit_card('Works on top of the 5 free gifts and free shipping.' if stack else 'One use, on anything on the site.')
    b += button('Use my $12', L, WHITE, pad='0 40px 0 40px') + friction('One use, already applied. 30-day returns. 100,000+ happy customers.', WHITE, pad='10px 40px 26px 40px')
    if stack:
        st = [('Sale price', 'Up to 70% off, already on the site'), ('Your $12 code', 'Off at checkout, on top'), ('5 free gifts', '$555 value, with every order'), ('Free shipping', 'Duties paid')]
        t = ''.join('<tr><td style="border-top:1px solid %s;padding:12px 4px;font-family:%s;font-size:16px;font-weight:700;color:%s;">+ %s</td><td align="right" style="border-top:1px solid %s;padding:12px 4px;font-family:%s;font-size:14px;color:%s;">%s</td></tr>' % (HAIR, FF, INK, k, HAIR, FF, GREY, v) for k, v in st)
        b += row(WHITE, '0 40px 22px 40px', txt('HOW IT ADDS UP', 12, 16, BRICK, 700, 'letter-spacing:2px;padding-bottom:6px;') + '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" style="border-bottom:1px solid %s;">%s</table>' % (HAIR, t)
                 + '<div style="padding-top:10px;">%s</div>' % pill('CHECK WITH FLORIS: does the code stack on sale prices?'))
        b += anchor(CREAM, DUO, 'With your $12')
        b += row(CREAM, '0 40px 22px 40px', txt('With your code: one pan $132, four pieces $187.', 15, 22, INK, 600, 'text-align:center;'), 'center')
    else:
        b += steps()
    b += gifts_grid(True, L, WHITE, 'ALSO WITH THIS ORDER', None, GIFTS_NOTE)
    b += quote(*TAMMY, L)
    b += button('Use my $12', L, WHITE, pad='22px 40px 0 40px') + friction('Code expires Sunday 30 November, 11:59 PM ET.', WHITE, pad='10px 40px 28px 40px')
    b += FOOTER
    return page(subj, pre, a, b, '../assets')

# ================================================================== 10 site buy box
def buybox():
    a = ann([('What', 'PDP buy box mock (website, not an email) &middot; 2 Pans + 2 Lids'), ('Where', 'Product page buy box, announcement bar and cart drawer use the same lines'),
             ('Replaces reference:', refs(['2h 43m', '7:55:46', '93% sold', 'High demand, few units left', 'Due to high demand, quantities are limited', 'Selling fast',
                                           'Refunding 10 random orders today &middot; Today only', 'Delivery from your local warehouse']) + '<br>(timers reset per visitor)'),
             ('Implementation', ul(['Deadline: one fixed time for everyone, "VIP Sale ends Nov 30, 11:59 PM ET". After that the line reads "Ended". No per-visitor timer.',
                                    'Stock line fixed "In stock. Free shipping, duties paid." Low stock only from real Shopify inventory.',
                                    'Order counter: real Shopify count of orders since Nov 1 (metafield refreshed by a job, or no bar at all). <b>2,140 is an example.</b>',
                                    'Prices: current site prices ($199, one pan $144). No invented compare-at.', 'Reviews: verbatim Trustpilot, 5 stars.']))])
    gifts = ''.join('<div style="text-align:center;width:19%%;display:inline-block;vertical-align:top;"><img src="assets/%s" alt="" style="width:52px;height:52px;margin:0 auto;border-radius:6px;"><div style="font-size:11px;line-height:14px;padding-top:4px;color:#272727;font-weight:600;">%s</div></div>' % (i, l)
                    for i, l in [('gift-mystery.jpg', 'Mystery gift'), ('gift-shipping.jpg', 'Free shipping'), ('gift-ebook.jpg', 'Plastic-free ebook'), ('gift-cookbook.jpg', 'Favorites cookbook'), ('gift-filter.jpg', 'Chance to win a PFAS filter')])
    rev = ''.join('<div style="border-top:1px solid #ECE7DD;padding:12px 0;"><div style="color:#B8862B;letter-spacing:2px;font-size:13px;">&#9733;&#9733;&#9733;&#9733;&#9733;</div><div style="font-size:14px;line-height:21px;padding-top:4px;">&ldquo;%s&rdquo;</div><div style="font-size:12px;color:#727272;padding-top:4px;font-weight:600;">%s, verified buyer</div></div>' % r for r in (SCOTT, GWEN))
    return ('''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>PDP buy box mock</title>
<style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
body{margin:0;background:#FFFFFF;font-family:Inter,Arial,sans-serif;color:#272727;}
.wrap{max-width:1000px;margin:0 auto;padding:24px 16px;display:flex;gap:32px;flex-wrap:wrap;}
.img{flex:1 1 380px;}.img img{width:100%%;border-radius:10px;display:block;background:#F8F7F2;}
.box{flex:1 1 380px;}
.bar{background:#272727;color:#fff;text-align:center;font-size:12px;letter-spacing:1.6px;font-weight:800;padding:11px;}
.btn{display:block;background:#272727;color:#fff;text-align:center;padding:18px;border-radius:28px;font-weight:800;letter-spacing:1px;text-decoration:none;margin-top:16px;}
.tag{display:inline-block;background:#FFB800;color:#272727;font-size:12px;font-weight:800;padding:4px 8px;border-radius:3px;vertical-align:middle;}
</style></head><body>
%s<div class="bar">BLACK FRIDAY SALE IS LIVE &middot; VIP SALE ENDS NOV 30, 11:59 PM ET</div>
<div style="background:#F8F7F2;border-bottom:1px solid #ECE7DD;padding:16px;text-align:center;"><img src="assets/logo-black-cream.png" alt="Siraat" style="width:150px;margin:0 auto;display:block;"></div>
<div class="wrap">
 <div class="img"><img src="%s" alt="2 Pans + 2 Lids"></div>
 <div class="box">
  <div style="font-size:12px;letter-spacing:2px;color:#AC3B19;font-weight:700;">THE ORIGINAL HAMMERED TITANIUM PAN</div>
  <h1 style="font-size:32px;line-height:38px;margin:8px 0 6px 0;font-weight:800;letter-spacing:-0.5px;">2 Pans + 2 Lids</h1>
  <div style="font-size:14px;color:#727272;">Pan Pro Standard + Mini, 2 lids &middot; pure titanium cooking surface, no coatings</div>
  <div style="padding:16px 0 4px 0;"><span style="font-size:30px;font-weight:800;">$199</span> &nbsp;<span class="tag">BLACK FRIDAY</span></div>
  <div style="font-size:15px;font-weight:600;">One pan is $144. Four pieces: $199.</div>
  <div style="margin-top:16px;border:1px solid #ECE7DD;border-radius:8px;padding:12px 14px;background:#F8F7F2;">
    <div style="font-size:15px;font-weight:800;color:#AC3B19;">VIP Sale ends Nov 30, 11:59 PM ET</div>
    <div style="font-size:12px;color:#727272;padding-top:2px;">Same time for everyone. After that this line says &ldquo;Ended&rdquo;.</div>
  </div>
  <div style="font-size:14px;padding-top:12px;"><span style="color:#2E7D32;">&#9679;</span> <b>In stock.</b> Free shipping, duties paid.</div>
  <div style="font-size:14px;padding-top:6px;"><b>2,140 orders</b> since Nov 1 %s</div>
  <a class="btn" href="#">ADD TO CART &rarr;</a>
  <div style="font-size:12px;color:#727272;text-align:center;padding-top:8px;">Free shipping. 30-day returns. 75-year warranty. 100,000+ happy customers.</div>
  <div style="margin-top:20px;border:1px solid #ECE7DD;border-radius:8px;padding:14px;">
    <div style="font-size:15px;font-weight:800;padding-bottom:10px;">5 free gifts with every order <span style="font-weight:600;color:#727272;">($555 value)</span></div>%s
    <div style="font-size:11px;color:#727272;padding-top:8px;">The filter is a chance to win in our weekly draw. The rest comes with every order.</div>
  </div>
  <div style="margin-top:18px;"><div style="font-size:15px;font-weight:800;padding-bottom:4px;">What owners say</div>%s</div>
 </div>
</div></body></html>''') % (a, IMG_DUO.replace('width=400', 'width=900'), pill('EXAMPLE NUMBER, live from Shopify'), gifts, rev)

# ------------------------------------------------------------------ schrijven + checks
OUT = {'checkout-e1.html': checkout_e1, 'checkout-last-benjamin.html': checkout_last, 'cart-lastday.html': cart_lastday,
       'bfcm-welcome-lastday.html': bfcm_lastday, 'ended.html': ended, 'welcome-w1.html': welcome_w1, 'welcome-founder-benjamin.html': welcome_founder,
       'redeem/redeem-letter-benjamin.html': lambda: redeem_letter(False), 'redeem/redeem-letter-reminder.html': lambda: redeem_letter(True),
       'redeem/redeem-designed.html': lambda: redeem_designed(False), 'redeem/redeem-stack.html': lambda: redeem_designed(True),
       'sunset-benjamin.html': sunset, 'site-buybox.html': buybox}
if __name__ == '__main__':
    os.makedirs(os.path.join(M, 'redeem'), exist_ok=True)
    for f in ('redeem-credit.html', 'redeem-credit-reminder.html'):
        if os.path.exists(os.path.join(M, f)): os.remove(os.path.join(M, f))
    for f, fn in OUT.items():
        h = fn()
        assert not re.search('[\u2013\u2014]', h), (f, 'streepje')
        assert not re.search(r'\{\{\s*(SHARED|IMG|HEADER|FOOTER)', h), (f, 'open placeholder')
        open(os.path.join(M, f), 'w').write(h); print('geschreven', f, '%.0f KB' % (len(h) / 1024))

# ------------------------------------------------------------------ index.html (kaart per mail, thumbnail = screenshot)
CARDS = [('checkout-e1.html', 'v4 &middot; Checkout abandonment (QUBUQV), email 1', 'Your checkout is still open: extra 10% applied'),
         ('checkout-last-benjamin.html', 'v4 &middot; Checkout abandonment (QUBUQV), last email, Benjamin letter', 'Benjamin here: a quick note before it ends'),
         ('cart-lastday.html', 'v4 &middot; Cart abandonment (TZG9Mx), last day', 'VIP Sale ends tonight at 11:59 PM ET'),
         ('bfcm-welcome-lastday.html', 'BFCM Welcome (Rn556d) / BF follow-up (YqKCmH), last day', 'VIP Sale ends tonight at 11:59 PM ET'),
         ('ended.html', 'Auto-switch after the end (QUBUQV, TZG9Mx, Rn556d, YqKCmH)', "It ended. Here's what's still on."),
         ('welcome-w1.html', 'v4 &middot; Welcome (T4a5Mk), email 1', '5 free gifts with every order, until tonight'),
         ('welcome-founder-benjamin.html', 'v4 &middot; Welcome (T4a5Mk), founder letter', 'Benjamin here: a quick note before it ends'),
         ('redeem/redeem-letter-benjamin.html', 'NEW &middot; Redeem $12 code, email 1, Benjamin letter', 'You have $12 to spend at Siraat'),
         ('redeem/redeem-letter-reminder.html', 'NEW &middot; Redeem $12 code, last day, Benjamin letter', 'Your $12 code expires tonight at 11:59 PM ET'),
         ('redeem/redeem-designed.html', 'NEW &middot; Redeem $12 code, designed version', 'You have $12 to spend at Siraat'),
         ('redeem/redeem-stack.html', 'NEW &middot; Redeem $12 code on top of the sale (check stacking with Floris)', 'Your $12 works on top of the sale'),
         ('sunset-benjamin.html', 'v4 &middot; Sunset (TbYQmX), Benjamin letter', 'Benjamin here: a quick note before it ends'),
         ('site-buybox.html', 'Site &middot; PDP buy box mock (not an email)', 'VIP Sale ends Nov 30, 11:59 PM ET')]
def index():
    c = ''
    for f, flow, subj in CARDS:
        png = 'screenshots/' + f.replace('/', '-').replace('.html', '.png')
        c += ('<a class="card" href="%s"><div class="thumb"><img src="%s" alt="" loading="lazy"></div><div class="meta"><div class="flow">%s</div>'
              '<div class="subj">%s</div><div class="file">%s &middot; <span>full screenshot</span></div></div></a>\n') % (f, png, flow, subj, f)
    return ('''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Urgency examples for Lucas</title>
<style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
body{margin:0;background:#F8F7F2;font-family:Inter,Arial,sans-serif;color:#272727;}
.top{max-width:1180px;margin:0 auto;padding:32px 16px 8px 16px;}
h1{font-size:28px;margin:0 0 8px 0;letter-spacing:-0.4px;} p{color:#555;font-size:15px;line-height:23px;max-width:760px;margin:0 0 6px 0;}
.grid{max-width:1180px;margin:0 auto;padding:16px;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px;}
.card{display:block;background:#fff;border:1px solid #ECE7DD;border-radius:10px;overflow:hidden;text-decoration:none;color:#272727;}
.card:hover{border-color:#272727;}
.thumb{height:360px;overflow:hidden;background:#eee;border-bottom:1px solid #ECE7DD;}
.thumb img{width:100%;display:block;}
.meta{padding:12px 14px 14px 14px;} .flow{font-size:12px;color:#AC3B19;font-weight:600;line-height:17px;}
.subj{font-size:16px;font-weight:800;line-height:21px;padding-top:6px;} .file{font-size:12px;color:#727272;padding-top:8px;font-family:Menlo,monospace;}
</style></head><body>
<div class="top"><h1>Urgency sprint: example emails per flow</h1>
<p>One card per email. Each file opens in the browser with a grey note strip on top (not part of the email) that lists the Klaviyo flow, position, subject and preview, the reference copy we replace, and the implementation notes.</p>
<p>Source: BRIEF-copy-per-flow.md (8 Nov 2026). Prices are current site prices. "2,140 orders" and "SIR-7K2Q9" are examples. BFCODE is a placeholder for the real code.</p></div>
<div class="grid">
@@CARDS@@</div></body></html>
''').replace('@@CARDS@@', c)
if __name__ == '__main__':
    open(os.path.join(M, 'index.html'), 'w').write(index()); print('geschreven index.html')
