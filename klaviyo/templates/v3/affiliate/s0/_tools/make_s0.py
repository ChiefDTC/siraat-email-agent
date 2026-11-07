"""AFF S0 'deel je link' (7 nov 2026), 3 varianten met CTA op het beeld en deelknoppen.
Platte brief van Benjamin zonder header/logo, minimale footer (uitzondering affiliate, CLAUDE.md).
Gebruik: python3 -I make_s0.py  -> schrijft <id>.klaviyo.html en <id>-preview.html (met voorbeelddata)."""
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
IMG = 'https://cdn.klaviyomail.com/company/TdtTzz/images/bc9df2cb-fb28-4f38-ba4a-2e31f7a3929d.jpeg'
LINK = "{{ person|lookup:'Referral Link - SocialSnowball'|default:'https://siraatskitchen.com' }}"
FO = "{{ person|lookup:'Referral Friend Offer - SocialSnowball'|default:'15%' }}"
RW = "{{ person|lookup:'Referral Reward - SocialSnowball'|default:'15%' }}"
DASH = 'https://affiliates.socialsnowball.io/auth/affiliate/login?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign=aff-s0-%s&amp;utm_content=dashboard'
S = "font-family:Inter,Arial,Helvetica,sans-serif;"
SER = "font-family:'Instrument Serif',Georgia,'Times New Roman',serif;"
INK = '#272727'
def p(t, top=14, size=16, lh=25, col='#282828', extra=''):
    return '<tr><td class="pad" style="padding:%dpx 40px 0 40px;%sfont-size:%dpx;line-height:%dpx;color:%s;%s">%s</td></tr>\n' % (top, S, size, lh, col, extra, t)
def hero(v, eyebrow, title, btn):
    btn_html = ('<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="#FFFFFF" style="border-radius:6px;">'
                '<a href="%s" style="display:inline-block;padding:14px 26px;%sfont-size:15px;font-weight:700;letter-spacing:1px;color:%s;text-decoration:none;text-transform:uppercase;">%s &rarr;</a></td></tr></table>') % (LINK, S, INK, btn)
    panel = ('<div style="%sfont-size:11px;line-height:14px;letter-spacing:2px;color:#E9DFC8;font-weight:700;text-transform:uppercase;">%s</div>'
             '<div class="htitle" style="%sfont-size:36px;line-height:39px;color:#FFFFFF;padding:6px 0 16px 0;">%s</div>%s') % (S, eyebrow, SER, title, btn_html)
    return ('<tr><td align="left" valign="bottom" bgcolor="#2A2622" background="%s" style="background-color:#2A2622;background-image:url(%s);background-size:cover;background-position:center 30%%;">'
            '<!--[if gte mso 9]><v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width:600px;height:430px;"><v:fill type="frame" src="%s" color="#2A2622" /><v:textbox inset="0,0,0,0"><![endif]-->'
            '<a class="hpad" href="%s" style="display:block;text-decoration:none;padding:250px 28px 26px 28px;background:linear-gradient(180deg,rgba(0,0,0,0) 0%%,rgba(0,0,0,0.15) 40%%,rgba(0,0,0,0.72) 100%%);">'
            '<span style="display:block;">%s</span></a><!--[if gte mso 9]></v:textbox></v:rect><![endif]--></td></tr>\n') % (IMG, IMG, IMG, LINK, panel)
def share_row(v):
    msg = 'I%20love%20my%20Siraat%20titanium%20pan.%20Here%20is%20' + 'my%20link%20for%20' + 'a%20discount%20on%20your%20first%20order%3A%20'
    items = [('WhatsApp', 'https://wa.me/?text=' + msg + LINK), ('Text', 'sms:?&amp;body=' + msg + LINK), ('Email', 'mailto:?subject=A%20pan%20I%20think%20you%27ll%20love&amp;body=' + msg + LINK)]
    cells = ''.join('<td class="sh" width="33%%" align="center" style="padding:0 4px;"><a href="%s" style="display:block;border:1px solid #D9D3C7;border-radius:6px;padding:12px 4px;%sfont-size:14px;font-weight:600;color:%s;text-decoration:none;">%s</a></td>' % (u, S, INK, n) for n, u in items)
    return ('<tr><td class="pad" style="padding:18px 36px 0 36px;"><div style="%sfont-size:12px;letter-spacing:1.5px;color:#7A746B;font-weight:700;text-transform:uppercase;padding:0 4px 8px 4px;">Send it in one tap</div>'
            '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr>%s</tr></table></td></tr>\n') % (S, cells)
def copybox():
    return ('<tr><td class="pad" style="padding:14px 40px 0 40px;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="#F4F1EA" style="border-radius:6px;padding:12px 14px;%sfont-size:13px;line-height:19px;color:#5A554D;word-break:break-all;">'
            'Your link: <a href="%s" style="color:%s;font-weight:600;">%s</a></td></tr></table></td></tr>\n') % (S, LINK, INK, LINK)
def steps():
    rows = [('1', 'Send your link to a friend.'), ('2', 'They get %s off their first order.' % FO), ('3', 'You get %s of what they pay, paid to you by PayPal, bank or gift card.' % RW)]
    h = ''.join('<tr><td width="34" valign="top" style="padding:8px 0;"><div style="width:26px;height:26px;border-radius:13px;background:%s;color:#FFFFFF;%sfont-size:13px;font-weight:700;line-height:26px;text-align:center;">%s</div></td><td style="padding:8px 0;%sfont-size:16px;line-height:24px;color:#282828;">%s</td></tr>' % (INK, S, n, S, t) for n, t in rows)
    return '<tr><td class="pad" style="padding:16px 40px 0 40px;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table></td></tr>\n' % h
def sign(v):
    return (p('Benjamin, founder of Siraat', 22) +
            p('Your sales and payouts are in <a href="%s" style="color:#9A948B;">your dashboard</a>.' % (DASH % v), 10, 12, 18, '#9A948B'))
FOOT = ('<tr><td class="pad" style="padding:30px 40px 0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-top:1px solid #ECE7DD;font-size:1px;line-height:1px;">&nbsp;</td></tr></table></td></tr>\n'
        '<tr><td class="pad" align="center" style="padding:16px 40px 24px 40px;' + S + 'font-size:11px;line-height:17px;color:#9A948B;text-align:center;">You get this email because your Siraat order came with a referral link.<br>'
        '<a href="{% unsubscribe_link %}" style="color:#111111;">Unsubscribe</a> &nbsp;|&nbsp; <a href="{% manage_preferences_link %}" style="color:#111111;">Manage preferences</a><br>{{ organization.name }} &middot; {{ organization.full_address }}</td></tr>\n')
def wrap(pre, rows):
    return ('<!doctype html><html lang="en" xmlns:v="urn:schemas-microsoft-com:vml"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="x-apple-disable-message-reformatting"><title>Siraat</title>'
            '<style>body{margin:0;padding:0;background:#FFFFFF;}@media only screen and (max-width:620px){.pad{padding-left:22px!important;padding-right:22px!important;}.hpad{padding:190px 20px 22px 20px!important;}.htitle{font-size:29px!important;line-height:32px!important;}.w{width:100%!important;}.sh a{font-size:13px!important;}}</style></head>'
            '<body style="margin:0;padding:0;background:#FFFFFF;"><div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">' + pre + '&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;</div>'
            '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF"><tr><td align="center">'
            '<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;">\n' + rows + FOOT + '</table></td></tr></table></body></html>')
HI = "Hi {{ first_name|default:'there' }},"
V = {}
# A: kort, CTA op beeld, deelknoppen
r = hero('a', 'Your own Siraat link', 'Give %s.<br>Get %s.' % (FO, RW), 'Share my link')
r += p(HI, 26) + p('Your order came with your own link. Friends get %s off their first order. You get %s of what they pay.' % (FO, RW))
r += p('Most people send it to one friend who asked about the pan. That one message is usually all it takes.')
r += share_row('a') + copybox() + sign('a')
V['s0-a'] = ('Kort, CTA op beeld, deelknoppen', 'Your order can pay for itself', 'Give your friends %s off. You get %s of what they pay.' % ('15%', '15%'), r)
# B: hoe het werkt in 3 stappen + rekenvoorbeeld
r = hero('b', 'Thank you for your order', 'Your order can<br>pay for itself', 'Get my link')
r += p(HI, 26) + p('Thank you for choosing Siraat. Your order came with something extra: your own link.')
r += steps()
r += p('<b>One example:</b> a friend orders the Pan Pro Standard at $144 with your link. They pay about $122, and you get about $18. Eight friends and a whole Pan Pro is paid back.', 16)
r += share_row('b') + copybox() + sign('b')
V['s0-b'] = ('Uitleg in 3 stappen + rekenvoorbeeld', 'Your order can pay for itself', 'How your link works, in three steps.', r)
# C: Black Friday-timing, persoonlijk van Benjamin
r = hero('c', 'Black Friday, from Benjamin', 'Your friends are<br>shopping this week', 'Send my link')
r += p(HI, 26) + p('Quick one from me. This is the week your friends are buying pans anyway, so it is the best week to send them your link.')
r += p('They get %s off their first order. You get %s of what they pay. No code to remember, the link does it.' % (FO, RW))
r += share_row('c') + copybox() + sign('c')
V['s0-c'] = ('Black Friday-timing, persoonlijk', 'Your friends are shopping this week', 'Send them your link: %s off for them, %s for you.' % ('15%', '15%'), r)
SAMPLE = {"{{ person|lookup:'Referral Link - SocialSnowball'|default:'https://siraatskitchen.com' }}": 'https://www.siraatskitchen.com/LOLA12345',
          "{{ person|lookup:'Referral Friend Offer - SocialSnowball'|default:'15%' }}": '15%', "{{ person|lookup:'Referral Reward - SocialSnowball'|default:'15%' }}": '15%',
          "{{ first_name|default:'there' }}": 'Sarah', '{{ organization.name }}': 'SIRAATSKITCHEN', '{{ organization.full_address }}': '2803 Philadelphia Pike Suite B #1567 Claymont, Delaware 19703',
          '{% unsubscribe_link %}': '#', '{% manage_preferences_link %}': '#'}
for k, (desc, sub, pre, rows) in V.items():
    h = wrap(pre, rows)
    assert not any(c in h for c in '—–') and 'CVX79' not in h
    open(os.path.join(OUT, k + '.klaviyo.html'), 'w').write(h)
    pv = h
    for a, b in SAMPLE.items(): pv = pv.replace(a, b)
    open(os.path.join(OUT, k + '-preview.html'), 'w').write(pv)
    open(os.path.join(OUT, k + '.meta.txt'), 'w').write('ID: %s · %s\nSENDER: Benjamin from Siraat\nSUBJECT: %s\nPREVIEW: %s\n' % (k, desc, sub, pre))
    print('ok', k, len(h))
