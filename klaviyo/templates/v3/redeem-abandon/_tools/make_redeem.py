"""Redeem-stap $13.78 in checkout- en cart-abandonment (Floris, 8 nov 2026). Concept: alleen in de DRAFT-flows, live flows QUBUQV en TZG9Mx blijven ongemoeid.
Schrijft vier bron-templates in klaviyo/templates/v3/redeem-abandon/: r1-checkout, r1-cart, r2-checkout, r2-cart.
Vaste header en footer via {{HEADER}}/{{FOOTER}} (build_template.py), look van tegoed/t1.
R1 (ongeveer 4 uur na de trigger) geeft de code uit met {% coupon_code 'SIRAAT_CREDIT_1378' %} (twee keer in dezelfde mail = dezelfde code).
R2 (20 uur na R1, dus ongeveer 4 uur voor het einde) heeft GEEN tweede coupon-tag (die zou een nieuwe code maken): hij verwijst naar
de vorige mail en gebruikt person.siraat_redeem_code alleen als die property gezet is (iets moet hem schrijven, zie LOG).
Eerlijk: de code verloopt echt 24 uur na R1 (coupon in Klaviyo op 24 uur zetten). Geen 'added yesterday', 'extended' of 'support checked'.
Gebruik: python3 -I make_redeem.py"""
import os
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COUPON = "{% coupon_code 'SIRAAT_CREDIT_1378' %}"
PCODE = 'person.siraat_redeem_code'
F = "font-family:Inter,Arial,Helvetica,sans-serif;"
SITE = 'https://siraatskitchen.com'
FR_CODE = 'One use, already applied. 30-day returns. 100,000+ happy customers.'
FR_NOCODE = 'One use, on orders of $75 or more. 30-day returns. 100,000+ happy customers.'


def utm(flow, mid, part, enc=False):
    q = 'utm_source=klaviyo&utm_medium=email&utm_campaign=v4-%s-redeem&utm_content=%s-%s' % (flow, mid, part)
    return q.replace('=', '%3D').replace('&', '%26') if enc else q


def url_r1(flow, mid, part):
    if flow == 'checkout':
        return ("{%% if event.extra.responsive_checkout_url %%}{{ event.extra.responsive_checkout_url }}&discount=%s&%s"
                "{%% else %%}%s/discount/%s?redirect=/checkout%%3F%s{%% endif %%}") % (COUPON, utm(flow, mid, part), SITE, COUPON, utm(flow, mid, part, True))
    return '%s/discount/%s?redirect=/cart%%3F%s' % (SITE, COUPON, utm(flow, mid, part, True))


def url_r2(flow, mid, part):
    code = '{{ %s }}' % PCODE
    if flow == 'checkout':
        return ("{%% if %s and event.extra.responsive_checkout_url %%}{{ event.extra.responsive_checkout_url }}&discount=%s&%s"
                "{%% elif %s %%}%s/discount/%s?redirect=/checkout%%3F%s"
                "{%% elif event.extra.responsive_checkout_url %%}{{ event.extra.responsive_checkout_url }}&%s"
                "{%% else %%}%s/cart?%s{%% endif %%}") % (PCODE, code, utm(flow, mid, part), PCODE, SITE, code, utm(flow, mid, part, True),
                                                       utm(flow, mid, part), SITE, utm(flow, mid, part))
    return ("{%% if %s %%}%s/discount/%s?redirect=/cart%%3F%s{%% else %%}%s/cart?%s{%% endif %%}"
            % (PCODE, SITE, code, utm(flow, mid, part, True), SITE, utm(flow, mid, part)))


def head(meta, title, pre):
    return """<!--
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
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap');
  body{margin:0;padding:0;background:#FFFFFF;-webkit-text-size-adjust:100%%;}
  table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}
  img{border:0;display:block;line-height:100%%;outline:none;text-decoration:none;}
  a{color:#272727;}
  @media only screen and (max-width:620px){
    .w{width:100%%!important;}
    .pad{padding-left:22px!important;padding-right:22px!important;}
    .navhide{display:none!important;}
    .lead{font-size:16px!important;line-height:25px!important;}
    .h1{font-size:34px!important;line-height:38px!important;}
    .kv{font-size:15px!important;}
  }
</style>
</head>
<body style="margin:0;padding:0;background:#FFFFFF;">
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">%s</div>
<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF">
<tr><td align="center" style="padding:8px 0 32px 0;">
<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:#FFFFFF;" bgcolor="#FFFFFF">
{{HEADER}}
""" % (meta, title, pre)


TAIL = """<tr><td bgcolor="#FFFFFF" style="background-color:#FFFFFF;height:18px;line-height:18px;font-size:0;">&nbsp;</td></tr>
{{FOOTER}}
</table>
</td></tr>
</table>
</body>
</html>
"""


def P(t, pad='0 40px 16px 40px'):
    return ('<tr><td class="pad lead" align="left" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:%s;text-align:left;">'
            '<div style="%sfont-size:17px;line-height:27px;color:#2E2E2E;font-weight:400;">%s</div></td></tr>\n') % (pad, F, t)


def H1(t, eyebrow):
    return ('<tr><td class="pad" align="left" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:34px 40px 18px 40px;text-align:left;">'
            '<div style="%sfont-size:11px;line-height:14px;color:#8A847A;font-weight:700;letter-spacing:2px;text-transform:uppercase;padding-bottom:10px;">%s</div>'
            '<div class="h1" style="font-family:\'Instrument Serif\',\'Times New Roman\',Times,serif;font-size:40px;line-height:44px;font-weight:400;font-style:italic;color:#272727;letter-spacing:-0.5px;">%s</div>'
            '</td></tr>\n') % (F, eyebrow, t)


def summary(code, exp, status=''):
    """Kaart in accountformaat: Account / Credit / Expires / Code (echte waarden)."""
    row = ('<tr><td class="kv" style="%sfont-size:16px;line-height:24px;color:#8A847A;font-weight:500;padding:5px 0;width:96px;" width="96" valign="top">%s</td>'
           '<td class="kv" style="%sfont-size:16px;line-height:24px;color:#272727;font-weight:600;padding:5px 0;" valign="top">%s</td></tr>')
    rows = ''.join(row % (F, k, F, v) for k, v in (('Account', '{{ email }}'), ('Credit', '$13.78'), ('Expires', exp)))
    rows += row % (F, 'Code', F, '<span style="font-family:Menlo,Consolas,monospace;font-size:17px;letter-spacing:1px;color:#272727;">%s</span>' % code)
    st = ('<div style="%sfont-size:12px;line-height:16px;color:#B8862B;font-weight:700;letter-spacing:1.6px;text-transform:uppercase;padding-bottom:8px;">%s</div>' % (F, status)) if status else ''
    return ('<tr><td class="pad" align="left" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:0 40px 20px 40px;">'
            '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#F8F7F2" style="background-color:#F8F7F2;border:1px solid #ECE7DD;border-radius:10px;">'
            '<tr><td style="padding:18px 22px 14px 22px;">%s<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table></td></tr></table></td></tr>\n') % (st, rows)


def btn(label, url, fr):
    return ('<tr><td class="pad" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:6px 30px 24px 30px;text-align:center;">'
            '<table role="presentation" width="360" cellpadding="0" cellspacing="0" border="0" style="width:100%%;max-width:360px;margin:0 auto;"><tr>'
            '<td align="center" bgcolor="#272727" style="background-color:#272727;border-radius:30px;">'
            '<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="%s" style="height:56px;v-text-anchor:middle;width:360px;" arcsize="50%%" stroke="f" fillcolor="#272727"><center style="color:#FFFFFF;font-family:Arial,sans-serif;font-size:15px;font-weight:bold;">%s</center></v:roundrect><![endif]-->'
            '<!--[if !mso]><!--><a href="%s" style="display:block;padding:19px 18px;%sfont-size:15px;line-height:18px;font-weight:700;letter-spacing:1.2px;color:#FFFFFF;text-decoration:none;text-transform:uppercase;">%s &rarr;</a><!--<![endif]-->'
            '</td></tr></table><div style="%sfont-size:13px;line-height:19px;color:#5E5A54;font-weight:500;padding-top:12px;">%s</div></td></tr>\n') % (url, label, url, F, label, F, fr)


def sign():
    return ('<tr><td class="pad" align="left" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:4px 40px 10px 40px;text-align:left;">'
            '<div style="%sfont-size:17px;line-height:24px;color:#272727;font-weight:700;">Benjamin</div>'
            '<div style="%sfont-size:14px;line-height:20px;color:#8A847A;font-weight:400;">Founder, Siraat&#39;s Kitchen</div></td></tr>\n') % (F, F)


def small(t):
    return ('<tr><td class="pad" align="left" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:14px 40px 8px 40px;text-align:left;">'
            '<div style="%sfont-size:12px;line-height:18px;color:#8A847A;font-weight:400;">%s</div></td></tr>\n') % (F, t)


HI = P("Hi {{ first_name|default:'there' }},", '0 40px 12px 40px')
TERMS = ('One $13.78 code per customer, for one order of $75 or more. It cannot be exchanged for cash and stops working '
         '24 hours after the first email about it was sent.')
WHERE = {'checkout': 'checkout', 'cart': 'cart'}


def meta(mid, flow, subj, pre, when, extra):
    return ('REDEEM 13.78 · v4 · %s abandonment · REDEEM 13.78 A/B · DRAFT (concept 8 nov 2026, alleen arm B van de draft-flow, niets live).\n'
            'ID: %s-%s\nSENDER: Benjamin from Siraat\nSUBJECT: %s\nPREVIEW: %s\nWANNEER: %s\n'
            'FILTER: zoals de live %s-mails (geen order sinds flowstart%s).\n%s'
            % (flow.capitalize(), mid, flow, subj, pre, when, flow, ', geen checkout sinds flowstart' if flow == 'cart' else ', geen storebot-adres', extra))


SUBJ = {'r1': 'You have $13.78 in your account', 'r2': 'Your $13.78 expires in 4 hours'}
PRE = {'r1': 'Benjamin here. A $13.78 code for the order you started, good for 24 hours.',
       'r2': 'The code in my last email stops working in about 4 hours. This is the last email about it.'}
files = {}
for flow in ('checkout', 'cart'):
    w = WHERE[flow]
    # ---------------- R1 · uitgifte (coupon-tag) ----------------
    m = 'r1'
    b = head(meta(m, flow, SUBJ[m], PRE[m], 'ongeveer 4 uur na de trigger (na C1/K1 en de 50/50-split, arm B)',
                  'CODE: coupon_code SIRAAT_CREDIT_1378 (placeholder; coupon bestaat nog niet; in Klaviyo op 24 uur na toewijzing zetten).'),
             SUBJ[m], PRE[m])
    b += H1('You have $13.78<br>in your account.', 'From Benjamin')
    b += HI
    b += P("Benjamin here. You were close to finishing your order, so I made you a $13.78 code to use on it. It&#39;s one code, made for you, and it works once on an order of $75 or more.")
    b += summary(COUPON, 'in 24 hours')
    b += P("The button below takes you back to your %s with the code already applied, so there&#39;s nothing to copy." % w)
    b += btn('Use my $13.78', url_r1(flow, m, 'cta1'), FR_CODE)
    b += P("It&#39;s made for this order, so it really does end in 24 hours. After that the code stops working and the regular price applies. Questions about a size or a lid? Reply and our team will help.", '0 40px 16px 40px')
    b += sign() + small(TERMS) + TAIL
    files['%s-%s' % (m, flow)] = b

    # ---------------- R2 · ongeveer 4 uur voor het einde (geen coupon-tag) ----------------
    m = 'r2'
    b = head(meta(m, flow, SUBJ[m], PRE[m], '20 uur na R1 (code verloopt 24 uur na R1, dus nog ongeveer 4 uur)',
                  'CODE: GEEN coupon-tag. Knop met code alleen als %s gezet is; anders naar de %s en verwijzing naar de vorige mail. Smart Sending uit (echte deadline).' % (PCODE, w)),
             SUBJ[m], PRE[m])
    b += H1('Your $13.78 expires<br>in 4 hours.', 'Your credit')
    b += HI
    b += P("A short one. The $13.78 code in my last email hasn&#39;t been used yet, and it stops working in about 4 hours.")
    b += summary(('{%% if %s %%}{{ %s }}{%% else %%}<span style="%sfont-size:16px;letter-spacing:0;font-weight:600;">In my last email</span>{%% endif %%}' % (PCODE, PCODE, F)), 'in about 4 hours', 'Unused')
    b += P(("{%% if %s %%}The button below takes you back to your %s with the code already applied.{%% else %%}"
            "The button below takes you back to your %s. Paste the code from my last email at checkout. It works once, on an order of $75 or more.{%% endif %%}") % (PCODE, w, w))
    label = '{%% if %s %%}Use my $13.78{%% else %%}Back to my %s{%% endif %%}' % (PCODE, w)
    b += btn(label, url_r2(flow, m, 'cta1'), '{%% if %s %%}%s{%% else %%}%s{%% endif %%}' % (PCODE, FR_CODE, FR_NOCODE))
    b += P("This is the last email about the code. After that the regular price applies. If now isn&#39;t the moment, that&#39;s fine.", '0 40px 16px 40px')
    b += sign() + small(TERMS) + TAIL
    files['%s-%s' % (m, flow)] = b

for k, v in files.items():
    assert '—' not in v and '–' not in v, k
    open(os.path.join(N, k + '.html'), 'w').write(v)
    print('geschreven', k)
