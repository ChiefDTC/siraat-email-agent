"""Platte tekstbrief (US only) op basis van Ali's tekst, 3 varianten. Prijzen uit Shopify 6 nov 2026:
Hammered Pan Pro Standard $144 (MSRP $480), 2 Pans + 2 Lids $249 (MSRP $664). Gebruik: python3 -I make_ali.py"""
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SET = 'https://siraatskitchen.com/products/2-pans-and-2-lids'
PAN = 'https://siraatskitchen.com/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern'
COL = 'https://siraatskitchen.com/collections/black-friday-sale'
def u(url, v, ct): return '%s?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign=2pans-1106-%s&amp;utm_content=%s' % (url, v, ct)
F = "font-family:Georgia,'Times New Roman',serif;" 
S = "font-family:Inter,Arial,Helvetica,sans-serif;"
def p(t, top=16, size=17, lh=27, col='#222222', fam=None, extra=''):
    return '<tr><td class="pad" style="padding:%dpx 40px 0 40px;%sfont-size:%dpx;line-height:%dpx;color:%s;text-align:left;%s">%s</td></tr>\n' % (top, fam or S, size, lh, col, extra, t)
def a(href, t): return '<a href="%s" style="color:#1A4FB3;text-decoration:underline;">%s</a>' % (href, t)
FOOT = ('<tr><td class="pad" style="padding:34px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-top:1px solid #E6E2DA;font-size:1px;line-height:1px;">&nbsp;</td></tr></table></td></tr>\n'
 '<tr><td class="pad" align="center" style="padding:16px 40px 24px 40px;' + S + 'font-size:11px;line-height:17px;color:#9A948B;text-align:center;">'
 'You get this email because you signed up at Siraats Kitchen.<br>'
 '<a href="{% unsubscribe_link %}" style="color:#111111;">Unsubscribe</a> &nbsp;|&nbsp; <a href="{% manage_preferences_link %}" style="color:#111111;">Manage preferences</a><br>'
 '{{ organization.name }} &middot; {{ organization.full_address }}</td></tr>\n')
def wrap(pre, rows):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="x-apple-disable-message-reformatting">'
      '<title>Siraat</title><style>body{margin:0;padding:0;background:#FFFFFF;}a{color:#1A4FB3;}@media only screen and (max-width:620px){.pad{padding-left:22px!important;padding-right:22px!important;}.w{width:100%%!important;}}</style>'
      '<!--[if mso]><style>body,table,td,a{font-family:Arial,Helvetica,sans-serif!important;}</style><![endif]--></head>'
      '<body style="margin:0;padding:0;background:#FFFFFF;">'
      '<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">%s&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;</div>'
      '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF"><tr><td align="center">'
      '<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%%;max-width:600px;">\n'
      '<tr><td style="height:12px;font-size:1px;line-height:1px;">&nbsp;</td></tr>\n%s%s</table></td></tr></table></body></html>') % (pre, rows, FOOT)

def full(v, table=False):
    L = lambda t, top=14: p(t, top)
    r = p('Hey {{ first_name|default:\'\' }},'.replace(" {{ first_name|default:'' }}", "{% if first_name %} {{ first_name }}{% endif %}"), 20)
    r += L('I need to show you something.')
    r += L('Right now, one of our ' + a(u(PAN, v, 'single-pan'), 'bestselling Titanium Hammered Pans') + ' is already discounted to <b>$144</b>.')
    r += L('But here&rsquo;s where things get crazy.')
    r += L('For just <b>$105 MORE</b>, you can get:')
    r += p(a(u(SET, v, 'items-pans'), '2 Titanium Hammered Pans.') + '<br>' + a(u(SET, v, 'items-lids'), '2 Matching Stainless Steel Lids.'), 6)
    r += L('<b>' + a(u(SET, v, 'four-pieces'), 'All FOUR pieces for just $249.') + '</b>')
    r += L('A set with an MSRP of $664. ' + a(u(SET, v, 'yours-199'), 'Yours for $249 this Black Friday.'))
    r += L('That&rsquo;s <b>$415 in savings</b>.')
    if table:
        r += ('<tr><td class="pad" style="padding:18px 40px 4px 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid #E6E2DA;border-bottom:1px solid #E6E2DA;">'
          + ''.join('<tr><td style="padding:9px 0;%sfont-size:16px;line-height:22px;color:#222222;">%s</td><td align="right" style="padding:9px 0;%sfont-size:16px;line-height:22px;color:#222222;white-space:nowrap;">%s</td></tr>' % (S, l, S, rr)
                    for l, rr in [('1 Titanium Hammered Pan', '$144'), (a(u(SET, v, 'table-set'), '2 pans + 2 stainless steel lids'), '<b>' + a(u(SET, v, 'table-price'), '$249') + '</b>'), ('MSRP of the set', '<s style="color:#8A847B;">$664</s>'), ('You save', '<b>$415</b>')])
          + '</table></td></tr>\n')
    r += L('And here&rsquo;s why we&rsquo;re doing this.')
    r += L('We genuinely believe that what you cook with matters just as much as what you cook.')
    r += L('Your family deserves cookware without chemical nonstick coatings. Cookware that doesn&rsquo;t need replacing every few years. Cookware that&rsquo;s made to last for decades, and maybe even be passed down to the next generation.')
    r += L('That&rsquo;s why we created Siraat.')
    r += L('And that&rsquo;s why our VIP Black Friday prices are so aggressive.')
    r += L('We&rsquo;re not trying to sell you another pan next year.')
    r += L('We want to make the pan you reach for year after year.')
    r += L('100% pure titanium cooking surface. No PFAS, PFOA, or BPA. Backed by our 75-year warranty.')
    r += L('And right now, ' + a(u(COL, v, 'prices'), 'at prices we don&rsquo;t normally offer') + '.')
    r += L('If you&rsquo;ve been thinking about upgrading your cookware, ' + a(u(SET, v, 'your-moment'), 'this is your moment') + '.')
    r += L('<b>' + a(u(SET, v, 'get-yours'), 'Get your 2 Pans + 2 Lids for $249 here:') + '</b>')
    r += p(a(u(SET, v, 'main-link'), 'siraatskitchen.com/products/2-pans-and-2-lids'), 6)
    r += L(a(u(SET, v, 'better-cookware'), 'Your family deserves better cookware.'))
    r += p('Benjamin<br>Siraat', 20)
    r += p('P.S. Want to upgrade your entire kitchen? Our full VIP Black Friday collection is live here:<br>' + a(u(COL, v, 'ps-link'), 'siraatskitchen.com/collections/black-friday-sale'), 20)
    return r
V = {'ali-a': ('Volledige tekst Ali, prijzen gecorrigeerd', 'I need to show you something', 'One pan is $144. For $105 more you get all four pieces.', full('a')),
     'ali-b': ('Volledige tekst Ali + prijsoverzicht', 'I need to show you something', 'One pan is $144. For $105 more you get all four pieces.', full('b', True))}
for k, (desc, sub, pre, rows) in V.items():
    h = wrap(pre, rows)
    assert '—' not in h and '–' not in h and 'CVX79' not in h
    open(os.path.join(OUT, k + '.klaviyo.html'), 'w').write(h)
    open(os.path.join(OUT, k + '.meta.txt'), 'w').write('ID: %s · %s\nMARKT: US only\nSENDER: Benjamin from Siraat\nSUBJECT: %s\nPREVIEW: %s\n' % (k, desc, sub, pre))
    print('ok', k, len(h))
