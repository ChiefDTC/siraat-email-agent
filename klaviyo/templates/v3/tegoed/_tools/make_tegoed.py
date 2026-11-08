"""Tegoed-flow '$15 in your account' (plan research/plannen/2026-11-tegoed/systeem.md, 8 nov 2026). Concept, flow staat als DRAFT in Klaviyo.
Schrijft de vier bron-templates t1..t4.html in klaviyo/templates/v3/tegoed/. Vaste header en footer via {{HEADER}}/{{FOOTER}} (build_template.py).
T1 geeft de code uit met {% coupon_code 'SIRAAT_CREDIT_15' %} (placeholder, coupon maakt Floris aan).
T2 t/m T4 lezen dezelfde code en de echte einddatum van het profiel (siraat_credit_code, siraat_credit_expires_at): een tweede
coupon_code-tag zou per mail een NIEUWE code met een nieuwe einddatum maken. Gebruik: python3 -I make_tegoed.py"""
import os
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COUPON = "{% coupon_code 'SIRAAT_CREDIT_15' %}"
F = "font-family:Inter,Arial,Helvetica,sans-serif;"
SITE = 'https://siraatskitchen.com'
EXP_T1 = "{{DATE:29:l, F j}}"      # build_template: vandaag + 29 dagen; de echte code loopt minimaal tot het eind van die dag (zie systeem.md 3.3)
EXP_P = "{{ person.siraat_credit_expires_at|format_date_string|date:'l, F j' }}"
CODE_P = "{{ person.siraat_credit_code }}"


def utm(mid, part):
    return 'utm_source=klaviyo&utm_medium=email&utm_campaign=tegoed-%s&utm_content=%s' % (mid, part)


def link(code, mid, part):
    return '%s/discount/%s?redirect=%%2F&%s' % (SITE, code, utm(mid, part))


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


def P(t, pad='0 40px 16px 40px', size=17, color='#2E2E2E', weight=400):
    return ('<tr><td class="pad lead" align="left" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:%s;text-align:left;">'
            '<div style="%sfont-size:%dpx;line-height:27px;color:%s;font-weight:%d;">%s</div></td></tr>\n') % (pad, F, size, color, weight, t)


def H1(t, eyebrow):
    return ('<tr><td class="pad" align="left" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:34px 40px 18px 40px;text-align:left;">'
            '<div style="%sfont-size:11px;line-height:14px;color:#8A847A;font-weight:700;letter-spacing:2px;text-transform:uppercase;padding-bottom:10px;">%s</div>'
            '<div class="h1" style="font-family:\'Instrument Serif\',\'Times New Roman\',Times,serif;font-size:40px;line-height:44px;font-weight:400;font-style:italic;color:#272727;letter-spacing:-0.5px;">%s</div>'
            '</td></tr>\n') % (F, eyebrow, t)


def summary(code, exp, status=''):
    """Kaart 'Account / Credit / Expires / Code' (Smooche-achtig accountformaat, maar met echte waarden)."""
    row = ('<tr><td class="kv" style="%sfont-size:16px;line-height:24px;color:#8A847A;font-weight:500;padding:5px 0;width:96px;" width="96" valign="top">%s</td>'
           '<td class="kv" style="%sfont-size:16px;line-height:24px;color:#272727;font-weight:600;padding:5px 0;" valign="top">%s</td></tr>')
    rows = ''.join(row % (F, k, F, v) for k, v in (('Account', '{{ email }}'), ('Credit', '$15'), ('Expires', exp)))
    rows += row % (F, 'Code', F, '<span style="font-family:Menlo,Consolas,monospace;font-size:17px;letter-spacing:1px;color:#272727;">%s</span>' % code)
    st = ('<div style="%sfont-size:12px;line-height:16px;color:#B8862B;font-weight:700;letter-spacing:1.6px;text-transform:uppercase;padding-bottom:8px;">%s</div>' % (F, status)) if status else ''
    return ('<tr><td class="pad" align="left" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:0 40px 20px 40px;">'
            '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0" bgcolor="#F8F7F2" style="background-color:#F8F7F2;border:1px solid #ECE7DD;border-radius:10px;">'
            '<tr><td style="padding:18px 22px 14px 22px;">%s<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0">%s</table></td></tr></table></td></tr>\n') % (st, rows)


def btn(label, url, fr='One use, already applied. 30-day returns. 100,000+ happy customers.'):
    return ('<tr><td class="pad" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:6px 30px 24px 30px;text-align:center;">'
            '<table role="presentation" width="360" cellpadding="0" cellspacing="0" border="0" style="width:100%%;max-width:360px;margin:0 auto;"><tr>'
            '<td align="center" bgcolor="#272727" style="background-color:#272727;border-radius:30px;">'
            '<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="%s" style="height:56px;v-text-anchor:middle;width:360px;" arcsize="50%%" stroke="f" fillcolor="#272727"><center style="color:#FFFFFF;font-family:Arial,sans-serif;font-size:15px;font-weight:bold;">%s</center></v:roundrect><![endif]-->'
            '<!--[if !mso]><!--><a href="%s" style="display:block;padding:19px 18px;%sfont-size:15px;line-height:18px;font-weight:700;letter-spacing:1.2px;color:#FFFFFF;text-decoration:none;text-transform:uppercase;">%s &rarr;</a><!--<![endif]-->'
            '</td></tr></table><div style="%sfont-size:13px;line-height:19px;color:#5E5A54;font-weight:500;padding-top:12px;">%s</div></td></tr>\n') % (url, label, url, F, label, F, fr)


def quote(q, who):
    return ('<tr><td class="pad" align="left" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:2px 40px 20px 40px;text-align:left;">'
            '<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-left:3px solid #B8862B;padding:2px 0 2px 16px;">'
            '<div style="%sfont-size:17px;line-height:26px;color:#272727;font-weight:500;">&ldquo;%s&rdquo;</div>'
            '<div style="%sfont-size:13px;line-height:18px;color:#8A847A;font-weight:500;padding-top:6px;">%s</div></td></tr></table></td></tr>\n') % (F, q, F, who)


def sign():
    return ('<tr><td class="pad" align="left" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:4px 40px 10px 40px;text-align:left;">'
            '<div style="%sfont-size:17px;line-height:24px;color:#272727;font-weight:700;">Benjamin</div>'
            '<div style="%sfont-size:14px;line-height:20px;color:#8A847A;font-weight:400;">Founder, Siraat</div></td></tr>\n') % (F, F)


def small(t):
    return ('<tr><td class="pad" align="left" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:14px 40px 8px 40px;text-align:left;">'
            '<div style="%sfont-size:12px;line-height:18px;color:#8A847A;font-weight:400;">%s</div></td></tr>\n') % (F, t)


HI = P("Hi {{ first_name|default:'there' }},", '0 40px 12px 40px')
TERMS = ('One $15 code per customer, for one order of $75 or more. It cannot be exchanged for cash and stops working after the expiry date shown above. '
         'You get this because you ordered from Siraat before.')
TAMMY = ("I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns.", 'Tammy, verified buyer')


def meta(mid, subj, alts, pre, when, extra):
    return ('TEGOED · v4 · Tegoed ($15 in your account) · DRAFT (concept 8 nov 2026, flow als DRAFT in Klaviyo, niets live).\n'
            'ID: %s\nSENDER: Benjamin from Siraat\nSUBJECT A: %s\nSUBJECT B: %s\nANDERE ONDERWERPEN: %s\nPREVIEW: %s\nWANNEER: %s\n'
            'WIE: lijst "Tegoed uitgegeven" (placeholder-trigger), aanbevolen cohort: kopers zonder order in 120 dagen, US; flowfilter geen order sinds flowstart.\n%s'
            % (mid, subj[0], subj[1], ' · '.join(alts), pre, when, extra))


files = {}

# ---------------- T1 · uitgifte: de code wordt hier gemaakt (coupon-tag) ----------------
m = 't1'
subj = ('You have $15 in your account', '$15 for your next order, from Benjamin')
alts = ('What would you cook next?', '$15, yours for 30 days', '"I am on my 4th pan from Siraat"')
pre = 'Benjamin here. A $15 code for your next order, good for 30 days.'
b = head(meta(m, subj, alts, pre, 'dag 0, 09:00 lokale tijd',
              'CODE: coupon_code SIRAAT_CREDIT_15 (placeholder; Klaviyo-coupon gekoppeld aan Shopify, $15 vast, 1x per klant, vervalt 29 dagen na aanmaak + 24 u Klaviyo-marge).\n'
              'EXPIRES: vandaag + 29 dagen (conservatief: de code werkt minimaal tot het eind van die dag). Coupon Assigned schrijft code en echte einddatum naar het profiel.'),
         subj[0], pre)
b += H1('You have $15<br>in your account.', 'A thank-you from Benjamin')
b += HI
b += P("Benjamin here. You ordered from Siraat before, so I made you a $15 code for your next order. That&#39;s it. A thank-you for being a customer.")
b += summary(COUPON, EXP_T1)
b += P("It&#39;s one code, made for you. It works once, on any order of $75 or more, and the button below applies it for you.")
b += P("It has a real end date: %s. A thank-you shouldn&#39;t hang around forever, so after that day the code stops working and the regular price applies." % EXP_T1)
b += btn('Use my $15', link(COUPON, m, 'cta1'))
b += P("Not sure what to get? Most people add a second size, so there&#39;s one pan for the eggs and one big enough for everyone. Reply and our team will help you pick.", '0 40px 16px 40px')
b += sign() + small(TERMS) + TAIL
files[m] = b

# ---------------- T2 · herinnering dag 14 (code en datum van het profiel) ----------------
m = 't2'
subj = ('Your $15 is still in your account', 'Still yours: $15 until ' + EXP_P)
alts = ('Two weeks left on your $15', 'Where your $15 goes furthest', '"I am on my 4th pan from Siraat"')
pre = 'Unused, and good until ' + EXP_P + '. Same code as before.'
b = head(meta(m, subj, alts, pre, 'dag 14, 09:00 lokale tijd',
              'CODE: person.siraat_credit_code en person.siraat_credit_expires_at (geschreven vanuit Coupon Assigned). Split vooraf: alleen als siraat_credit_code gezet is.'),
         subj[0], pre)
b += H1('Your $15 is<br>still here.', 'Your credit')
b += HI
b += P("Quick note. The $15 I sent you two weeks ago hasn&#39;t been used yet, so it&#39;s still in your account. Same code, same end date.")
b += summary(CODE_P, EXP_P, 'Unused')
b += btn('Use my $15', link(CODE_P, m, 'cta1'))
b += P("If you&#39;re wondering where it goes furthest: on a second pan. Every one has the same pure titanium cooking surface and no coatings, so there&#39;s nothing on it to wear off. One of our regulars put it like this:", '4px 40px 16px 40px')
b += quote(*TAMMY)
b += P("Questions about a size? Reply and our team will help.", '0 40px 14px 40px')
b += sign() + small(TERMS) + TAIL
files[m] = b

# ---------------- T3 · 3 dagen voor einddatum ----------------
m = 't3'
subj = ('Your $15 expires in 3 days', 'Three days left on your $15')
alts = ('Your $15 ends ' + EXP_P, 'Before your $15 runs out', 'Still thinking about that second pan?')
pre = 'It stops working on ' + EXP_P + '. After that it is gone.'
b = head(meta(m, subj, alts, pre, 'dag 27, 09:00 lokale tijd (resterend 2,6 tot 3 dagen, zie systeem.md 3.3)', 'Smart Sending uit (echte deadline).'),
         subj[0], pre)
b += H1('Your $15 expires<br>in 3 days.', 'Your credit')
b += HI
b += P("Your $15 code ends on %s. After that it stops working and I can&#39;t bring it back, because it was made for a set period from the start." % EXP_P)
b += summary(CODE_P, EXP_P, '3 days left')
b += btn('Use my $15', link(CODE_P, m, 'cta1'))
b += P("If something has been on your list, a lid, a second size, a gift for someone who cooks, this is a good week for it. Every pan is covered for 75 years against defects.", '4px 40px 16px 40px')
b += sign() + small(TERMS) + TAIL
files[m] = b

# ---------------- T4 · laatste dag ----------------
m = 't4'
subj = ('Last day for your $15', 'Your $15 expires in less than 24 hours')
alts = ('Your $15 ends ' + EXP_P, 'The last email about your $15', 'Today is the last day')
pre = 'Less than 24 hours left. This is the last email about it.'
b = head(meta(m, subj, alts, pre, 'dag 29, 09:00 lokale tijd (resterend 14 tot 24 uur)',
              'Geen "tonight" in onderwerp: de echte eindtijd ligt tussen 23:00 en 09:00 (Klaviyo-batch + 24 u marge). "tonight" pas als de einddatum vast op 23:59 ET staat (optie B, systeem.md).\nSmart Sending uit (echte deadline).'),
         subj[0], pre)
b += H1('Last day for<br>your $15.', 'Your credit')
b += HI
b += P("This is the last email about your $15. The code stops working in less than 24 hours, and I won&#39;t send another one.")
b += summary(CODE_P, EXP_P, 'Less than 24 hours left')
b += btn('Use my $15 today', link(CODE_P, m, 'cta1'))
b += P("Two promises if you use it. Changed your mind? Send it back unused within 30 days for a full refund. Something wrong? If it arrives damaged or defective within 30 days, we refund or replace it and pay the shipping. After that, the 75-year warranty covers defects.", '4px 40px 16px 40px')
b += P("And if now isn&#39;t the moment, that&#39;s fine. Thank you for cooking with us.", '0 40px 14px 40px')
b += sign() + small(TERMS) + TAIL
files[m] = b

for k, v in files.items():
    assert '\u2014' not in v and '\u2013' not in v, k
    open(os.path.join(N, k + '.html'), 'w').write(v)
    print('geschreven', k)
