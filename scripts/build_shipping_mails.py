#!/usr/bin/env python3
"""Genereert de verzendupdate-mails (klaviyo/templates/v3/shipping/z1..z6) voor de ParcelWILL-flow.
Draaien: python3 scripts/build_shipping_mails.py  (schrijft <naam>.html en <naam>.sample.html met voorbeelddata).
Daarna per mail build_template.py op de .html (--no-preview) en op de .sample.html (preview)."""
import os

D = '/home/user/siraat-email-agent/klaviyo/templates/v3/shipping/'
F = "font-family:Inter,Arial,Helvetica,sans-serif;"
SERIF = "font-family:'Instrument Serif','Times New Roman',serif;font-style:italic;"
src = open(D + '../subscription/s1b.html').read()
head = src[src.index('<!DOCTYPE'):src.index('<!-- HERO -->')]
tail = src[src.index('<!-- SIGN-OFF -->'):]
STEPS = ['Packed', 'On its way', 'Out for delivery', 'Delivered']


def tracker(cur):
    cells = ''
    for i, s in enumerate(STEPS):
        if i < cur:
            dot, col, w = '#282828', '#282828', '500'
        elif i == cur:
            dot, col, w = '#AC3B19', '#AC3B19', '600'
        else:
            dot, col, w = '#D9D4CA', '#9A948B', '400'
        bar_l = 'transparent' if i == 0 else ('#282828' if i <= cur else '#D9D4CA')
        bar_r = 'transparent' if i == 3 else ('#282828' if i < cur else '#D9D4CA')
        cells += (f'<td width="25%" valign="top" align="center" style="padding:0;">'
                  f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
                  f'<td width="50%" style="padding:0;"><div style="height:2px;line-height:2px;font-size:2px;background:{bar_l};">&nbsp;</div></td>'
                  f'<td width="14" style="padding:0;"><div style="width:14px;height:14px;border-radius:7px;background:{dot};font-size:1px;line-height:14px;">&nbsp;</div></td>'
                  f'<td width="50%" style="padding:0;"><div style="height:2px;line-height:2px;font-size:2px;background:{bar_r};">&nbsp;</div></td>'
                  f'</tr></table><div style="{F}font-size:11px;line-height:14px;color:{col};font-weight:{w};padding-top:8px;">{s}</div></td>')
    return f'<tr><td class="pad" style="padding:26px 30px 0 30px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cells}</tr></table></td></tr>\n'


def hero(h, sub):
    return (f'<!-- HERO -->\n<tr><td class="pad h1" align="center" style="padding:30px 44px 0 44px;{SERIF}font-size:44px;line-height:48px;color:#282828;text-align:center;">{h}</td></tr>\n'
            f'<tr><td class="pad" align="center" style="padding:10px 44px 0 44px;{F}font-size:16px;line-height:24px;color:#727272;text-align:center;">{sub}</td></tr>\n')


def text(*ps):
    inner = ''.join(f'<p style="margin:0 0 14px 0;">{p}</p>' for p in ps)
    return (f'<tr><td class="pad lead" style="padding:26px 44px 0 44px;{F}font-size:16px;line-height:25px;color:#282828;">'
            f'<p style="margin:0 0 14px 0;">Hi {{{{ first_name|default:\'there\' }}}},</p>{inner}</td></tr>\n')


def box(title, rows):
    r = ''
    for i, (l, v) in enumerate(rows):
        b = '' if i == len(rows) - 1 else 'border-bottom:1px solid #ECE7DD;'
        r += (f'  <tr><td valign="top" width="110" style="padding:11px 0 11px 16px;{F}font-size:14px;line-height:21px;color:#727272;{b}">{l}</td>'
              f'<td valign="top" style="padding:11px 16px 11px 8px;{F}font-size:15px;line-height:22px;color:#282828;{b}">{v}</td></tr>\n')
    return (f'<tr><td class="pad" style="padding:8px 44px 0 44px;">\n  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:1px solid #ECE7DD;">\n'
            f'  <tr><td colspan="2" style="padding:14px 16px 2px 16px;{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:600;color:#AC3B19;">{title}</td></tr>\n{r}  </table>\n</td></tr>\n')


def dark(eyebrow, h, t):
    return (f'<tr><td class="pad" style="padding:22px 44px 0 44px;">\n  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#321E1D" style="background-color:#321E1D;">\n'
            f'  <tr><td bgcolor="#321E1D" style="padding:20px 22px 4px 22px;{F}font-size:11px;line-height:14px;letter-spacing:2px;font-weight:600;color:#C9C6C0;">{eyebrow}</td></tr>\n'
            f'  <tr><td bgcolor="#321E1D" style="padding:6px 22px 0 22px;{SERIF}font-size:28px;line-height:32px;color:#FFFFFF;">{h}</td></tr>\n'
            f'  <tr><td bgcolor="#321E1D" style="padding:10px 22px 20px 22px;{F}font-size:15px;line-height:23px;color:#ECE7DD;">{t}</td></tr>\n  </table>\n</td></tr>\n')


def cta(label, sub=''):
    s = f' sub="<div style=\'{F}font-size:12px;line-height:18px;color:#727272;padding-top:10px;\'>{sub}</div>"' if sub else ''
    return '{{BLOCK:cta label="%s" url="{{ event.tracking_link|default:\'https://siraatskitchen.com/apps/parcelpanel\' }}" pad="24px 44px 0 44px"%s}}\n\n' % (label, s)


ORDER = "{{ event.order_number|default:'' }}"
CAR = "{{ event.carrier_name|default:'Your local carrier' }}"
LAST = "{{ event.last_check_point|default:'Label created' }}"
LOC = "{{ event.location|default:'' }}"
PICK = "{{ event.pickup_location|default:'See the carrier page' }}"

M = {
    'z1-packed': (0, 'Your order is packed', 'Your order is packed and has a tracking number. The link may stay quiet for a few days, here is why.',
                  hero('Your order is packed.', 'Here is what happens next, so nothing is a surprise.'),
                  text('Good news: your order has left our warehouse and has a tracking number.')
                  + box('YOUR SHIPMENT', [('Order', ORDER), ('Carrier', CAR), ('Status', LAST)])
                  + dark('GOOD TO KNOW', 'The quiet days are normal.', 'Your parcel first travels to your country and clears customs. During that time, usually 5 to 7 days, your tracking link can still say &ldquo;label created&rdquo; or &ldquo;not yet received&rdquo;. Nothing is lost. As soon as your local carrier scans it, I&rsquo;ll let you know.')
                  + cta('Track my order', 'Updates can take a few days to show.'), 'Label created'),
    'z2-in-transit': (1, 'Your order is on its way', 'Your parcel has been scanned by the carrier and is moving.',
                      hero('Your parcel is on the&nbsp;move.', 'The carrier has it, and it is heading your way.'),
                      text('Your parcel has been scanned and is on its way to you. Here is the latest update.')
                      + box('LATEST UPDATE', [('Order', ORDER), ('Carrier', CAR), ('Last scan', LAST), ('Where', LOC)])
                      + cta('Track my order'), 'Arrived at sorting facility'),
    'z3-out-for-delivery': (2, 'It arrives today', 'Your Siraat order is out for delivery today.',
                            hero('It arrives today.', 'Your parcel is out for delivery.'),
                            text('Your order is with the driver and should arrive today. If you won&rsquo;t be home, you can usually choose a safe place or a pickup point on the carrier&rsquo;s page.')
                            + box('TODAY', [('Order', ORDER), ('Carrier', CAR), ('Last scan', LAST)])
                            + cta('See delivery details'), 'Out for delivery'),
    'z4-pickup': (2, 'Your parcel is waiting for you', 'Your order is ready to pick up. Here is where.',
                  hero('Your parcel is waiting for&nbsp;you.', 'It is ready to pick up. Please collect it soon.'),
                  text('Your order couldn&rsquo;t be left at your door, so the carrier has it ready for you to pick up. Most pickup points keep parcels for a limited time, often 7 to 14 days, after which it goes back to us.')
                  + box('PICK UP HERE', [('Order', ORDER), ('Carrier', CAR), ('Location', PICK)])
                  + cta('See pickup details', 'Bring an ID and your order number.'), 'Ready for pickup'),
    'z5-failed-attempt': (2, 'We missed you', 'The carrier tried to deliver your order. Here is how to get it.',
                          hero('We missed you.', 'The carrier tried to deliver your parcel.'),
                          text('The driver couldn&rsquo;t deliver your order this time. On the carrier&rsquo;s page you can usually pick a new day, a safe place or a pickup point. If the address looks wrong, just reply to this email and our team will help right away.')
                          + box('DELIVERY ATTEMPT', [('Order', ORDER), ('Carrier', CAR), ('Last scan', LAST)])
                          + cta('Choose a new delivery'), 'Delivery attempt failed'),
    'z6-delivered': (3, 'Your order has arrived', 'Your Siraat order was delivered. Didn&rsquo;t get it? Just reply.',
                     hero('It&rsquo;s there.', 'Your order has been delivered. Enjoy cooking.'),
                     text('Your order was delivered. I hope it brings a lot of good meals.',
                          'Didn&rsquo;t find it? Check your porch, mailbox and neighbours first. Still nothing? Just reply to this email and our team will sort it out with you.')
                     + box('DELIVERED', [('Order', ORDER), ('Carrier', CAR), ('Last scan', LAST)])
                     + cta('See delivery details'), 'Delivered'),
}

if __name__ == '__main__':
    for k, (cur, subj, pv, h, body, sample_last) in M.items():
        html = (f'<!-- {k.upper()} VERZENDUPDATE (VOORBEELD 30 okt 2026, NIET LIVE) | Trigger: ParcelWILL - Shipment status update (WYXGCn), split op event.shipment_status | SUBJECT: {subj} | PREVIEW: {pv} | Transactional aanvragen | UTM utm_campaign=v4-shipping -->\n'
                + head.replace('<title>Your first pack is on us</title>', f'<title>{subj}</title>').replace('Your free dishwasher sheet pack is on us.', pv)
                + h + tracker(cur) + body + tail)
        open(D + k + '.html', 'w').write(html)
        sample = (html.replace("{{ event.order_number|default:'' }}", '#SIRAAT113021').replace(CAR, 'GOFO').replace(LAST, sample_last)
                  .replace(LOC, 'Chicago, IL').replace(PICK, 'Walgreens, 1200 N State St, Chicago'))
        open(D + k + '.sample.html', 'w').write(sample)
        print(k, '—' in html)
