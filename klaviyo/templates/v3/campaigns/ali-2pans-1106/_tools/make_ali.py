"""Platte tekstbrief (US only) op basis van Ali's tekst, 3 varianten. Prijzen uit Shopify 6 nov 2026:
Hammered Pan Pro Standard $144 (MSRP $480), 2 Pans + 2 Lids $199 (MSRP $664). Gebruik: python3 -I make_ali.py"""
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SET = 'https://siraatskitchen.com/products/2-pans-and-2-lids'
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
HI = "Hi {{ first_name|default:'there' }},"
V = {}
# A: Ali's tekst, zo dicht mogelijk bij het origineel, prijzen gecorrigeerd
r = p(HI, 20) + p('I need to show you something.')
r += p('Right now, one of our bestselling Titanium Hammered Pans is already down to <b>$144</b>.') + p('But here&rsquo;s where it gets crazy.')
r += p('For just <b>$55 more</b>, you get:', 16) + p('&bull; 2 Titanium Hammered Pans<br>&bull; 2 matching stainless steel lids', 6, extra='padding-left:58px;')
r += p('All four pieces for <b>$199</b>. A set with an MSRP of $664. That&rsquo;s $465 in savings.')
r += p('And here&rsquo;s why we&rsquo;re doing this.')
r += p('We believe what you cook with matters just as much as what you cook. Your family deserves cookware without a coating. Cookware that doesn&rsquo;t need replacing every few years. Cookware made to last for decades, and maybe even be passed down.')
r += p('That&rsquo;s why we started Siraat. And that&rsquo;s why our VIP Black Friday prices are this low. We&rsquo;re not trying to sell you another pan next year. We want to make the pan you reach for, year after year.')
r += p('No PFAS, PFOA, or BPA. No coatings. Backed by our 75-year warranty, with 30 days to decide.')
r += p('If you&rsquo;ve been thinking about upgrading your cookware, this is your moment.')
r += p('<b>' + a(u(SET, 'a', 'main-link'), 'Get your 2 Pans + 2 Lids for $199 here') + '</b>')
r += p('Your family deserves better cookware.') + p('Benjamin<br><span style="color:#7A746B;font-size:15px;">Founder, Siraat</span>', 22)
r += p('P.S. Want to upgrade your whole kitchen? The full VIP Black Friday collection is live ' + a(u(COL, 'a', 'ps-link'), 'here') + '. It ends Monday, November 30.', 22, 15, 24, '#444444')
V['ali-a'] = ('Ali, gecorrigeerd', 'I need to show you something', 'One pan is $144. For $55 more you get four pieces.', r)
# B: zelfde brief, rekensom als nette tekstregels, serif-briefgevoel
r = p(HI, 20, fam=F) + p('I need to show you something.', fam=F)
r += p('One of our bestselling Titanium Hammered Pans is already down to $144. Here&rsquo;s the part that surprised even me.', fam=F)
r += ('<tr><td class="pad" style="padding:20px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid #E6E2DA;border-bottom:1px solid #E6E2DA;">'
      + ''.join('<tr><td style="padding:9px 0;%sfont-size:16px;line-height:22px;color:#222222;">%s</td><td align="right" style="padding:9px 0;%sfont-size:16px;line-height:22px;color:#222222;white-space:nowrap;">%s</td></tr>' % (S, l, S, rr)
                for l, rr in [('1 Titanium Hammered Pan', '$144'), ('2 pans + 2 stainless steel lids', '<b>$199</b>'), ('MSRP of the set', '<s style="color:#8A847B;">$664</s>'), ('You save', '<b>$465</b>')])
      + '</table></td></tr>\n')
r += p('That&rsquo;s $55 more for a second pan and both lids.', 16, fam=F)
r += p('Why so low? Because we&rsquo;re not trying to sell you another pan next year. We want to make the pan you reach for, year after year. No coating to wear off. No PFAS, PFOA, or BPA. A 75-year warranty, and 30 days to decide.', fam=F)
r += p('<b>' + a(u(SET, 'b', 'main-link'), 'Get 2 Pans + 2 Lids for $199 &rarr;') + '</b>', 20, 18, 28)
r += p('Your family deserves better cookware.', fam=F) + p('Benjamin<br><span style="color:#7A746B;font-size:15px;">Founder, Siraat</span>', 22, fam=F)
r += p('P.S. Upgrading the whole kitchen? Everything is up to 70% off in ' + a(u(COL, 'b', 'ps-link'), 'the VIP Black Friday sale') + ', until Monday, November 30.', 22, 15, 24, '#444444', F)
V['ali-b'] = ('Brief met rekensom', '$144 for one, or $199 for four', 'Two pans and two lids. MSRP $664. Here is why it is this low.', r)
# C: kort, direct response
r = p(HI, 20) + p('Quick one.') + p('One Titanium Hammered Pan: $144.<br>Two pans + two lids: <b>$199</b>.')
r += p('That&rsquo;s $55 for a second pan and both lids. MSRP $664, so you save $465.')
r += p('No coating to wear off, a 75-year warranty, and 30 days to decide if it&rsquo;s right for you.')
r += p('<b>' + a(u(SET, 'c', 'main-link'), 'Get the 4-piece set for $199') + '</b>', 18)
r += p('Benjamin<br><span style="color:#7A746B;font-size:15px;">Founder, Siraat</span>', 22)
r += p('P.S. VIP Black Friday ends Monday, November 30. ' + a(u(COL, 'c', 'ps-link'), 'See everything that&rsquo;s on sale') + '.', 22, 15, 24, '#444444')
V['ali-c'] = ('Kort, direct response', 'Two pans, two lids, $199', 'That is $55 more than one pan. MSRP $664.', r)
for k, (desc, sub, pre, rows) in V.items():
    h = wrap(pre, rows)
    assert '—' not in h and '–' not in h and 'CVX79' not in h
    open(os.path.join(OUT, k + '.klaviyo.html'), 'w').write(h)
    open(os.path.join(OUT, k + '.meta.txt'), 'w').write('ID: %s · %s\nMARKT: US only\nSENDER: Benjamin from Siraat\nSUBJECT: %s\nPREVIEW: %s\n' % (k, desc, sub, pre))
    print('ok', k, len(h))
