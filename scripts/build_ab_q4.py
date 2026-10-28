#!/usr/bin/env python3
"""A/B Q4 (28 okt 2026): B-varianten en nieuwe mails als library-templates in Klaviyo.

Varianten van een bestaande mail worden afgeleid van de LIVE flow-template (niet van de repo-build, die wijkt af),
met een vaste lijst vervangingen. Zo verschilt B van A alleen in de testvariabele. Bron en resultaat staan in
klaviyo/templates/v3/ab-q4/ (<key>.a.html = live A op het moment van bouwen, <key>.klaviyo.html = B).
Nieuwe mails (K4, C5) komen uit de repo-bron via build_template.py (cart/k4-installments, checkout/c5-installments).

Draaien: python3 scripts/build_ab_q4.py [--dry]   (maakt of werkt library-templates bij, raakt geen flow aan)
"""
import os, sys, json, re
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api

DRY = '--dry' in sys.argv
ROOT = '/home/user/siraat-email-agent/klaviyo/templates/v3/'
OUT = ROOT + 'ab-q4/'
os.makedirs(OUT, exist_ok=True)

BR1_HERO_A = 'https://cdn.klaviyomail.com/company/TdtTzz/images/a0d7c845-62a3-4e24-ba4c-c849d79df87d.jpeg'
BR1_HERO_B = 'https://cdn.klaviyomail.com/company/TdtTzz/images/5c05c48c-d26a-4d0a-9b66-c26ffd44d4f2.jpeg'  # browse/assets/b1-hero-br1.jpg
BR1_LINE_A = '<b>HI10</b> takes an extra 10% off this price. Already applied with the button.'
BR1_LINE_B = 'That&rsquo;s the sale price. <b>HI10</b> takes an extra 10% off it, already applied with the button.'
BR1_PREVIEW = 'The sale price, plus an extra 10% with HI10. The lab report is inside.'
BR1_BAR_A = 'EXTRA 10% OFF YOUR ORDER · CODE\xa0'
BR1_BAR_B = 'SALE PRICE + EXTRA 10% · CODE\xa0'


def lid_card(size_us, size_cm, variant):
    mc = ("<!--{% with mc=event.extra.shipping_address.country_code %}-->")
    label = (mc + "<!--{% if mc == 'US' %}-->" + size_us + "″<!--{% elif mc %}-->" + size_cm + " cm<!--{% else %}-->" + size_cm + " cm ("
             + size_us + "″)<!--{% endif %}--><!--{% endwith %}-->")
    url = ('https://siraatskitchen.com/products/stainless-steel-lid?variant=%s&amp;utm_source=klaviyo&amp;utm_medium=email'
           '&amp;utm_campaign=v4-postpurchase&amp;utm_content=p1first-lidcard' % variant)
    friction = (mc + "<!--{% if mc == 'US' %}-->Free shipping from the US. 30-day returns. 100,000+ happy customers."
                "<!--{% else %}-->Free shipping, duties paid. 30-day returns. 100,000+ happy customers.<!--{% endif %}--><!--{% endwith %}-->")
    return ('<tr><td class="pad" style="padding:18px 44px 4px 44px;"><table bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" role="presentation" '
            'style="background-color:#FFFFFF;border:1px solid #ECE7DD;" width="100%"><tr>'
            '<td bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:16px 0 16px 16px;" valign="middle" width="112"><a href="' + url + '">'
            '<img alt="Stainless steel lid" src="https://cdn.klaviyomail.com/company/TdtTzz/images/fef2213b-f218-4f6e-b70a-d858ea6728d4.jpeg" '
            'style="display:block;width:96px;height:96px;object-fit:cover;background:#F8F7F2;border:0;" width="96"/></a></td>'
            '<td bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:14px 16px;font-family:Inter,Arial,Helvetica,sans-serif;" valign="middle">'
            '<div style="font-size:11px;line-height:14px;letter-spacing:1.5px;font-weight:600;color:#AC3B19;padding-bottom:5px;">MADE FOR YOUR PAN</div>'
            '<div style="font-size:16px;line-height:22px;font-weight:600;color:#282828;">The ' + label + ' lid</div>'
            '<div style="font-size:14px;line-height:20px;color:#727272;padding-top:3px;">Same diameter as your pan. Steams, melts, stops the splatter.</div>'
            '</td></tr><tr><td colspan="2" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:0 16px 16px 16px;" align="center">'
            '<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tr><td align="center" bgcolor="#AC3B19" '
            'style="background-color:#AC3B19;border-radius:4px;"><a href="' + url + '" style="display:block;padding:13px 18px;font-family:Inter,Arial,'
            'Helvetica,sans-serif;font-size:14px;line-height:18px;font-weight:600;letter-spacing:1px;color:#FFFFFF;text-decoration:none;">'
            'ADD THE LID THAT FITS MY PAN &rarr;</a></td></tr></table>'
            '<div style="font-family:Inter,Arial,Helvetica,sans-serif;font-size:12px;line-height:18px;color:#727272;padding-top:10px;">' + friction + '</div>'
            '</td></tr></table></td></tr>')


def t15(h):
    """P1-FIRST: elke ONE SIZE NOTE-regel (tekst + link) wordt een productkaart. Voorwaarden (welke pan, al in bezit) blijven gelijk.
    Geen prijs op de kaart: de dekselprijs wisselt met de sale en de catalogus is van 8 okt."""
    sizes = {'52401107239252': ('11', '28'), '52401107272020': ('12', '30'), '52401107206484': ('10', '26'), '53294486421844': ('8', '20')}
    n = 0
    for var, (us, cm) in sizes.items():
        seg_end = h.index('variant=' + var)
        start = h.rindex('<tr><td class="pad" style="padding:16px 44px 4px 44px;">', 0, seg_end)
        end = h.index('</td></tr></table></td></tr>', seg_end) + len('</td></tr></table></td></tr>')
        assert 'ONE SIZE NOTE' in h[start:end] and h[start:end].count('ONE SIZE NOTE') == 1
        h = h[:start] + lid_card(us, cm, var) + h[end:]
        n += 1
    assert n == 4 and 'ONE SIZE NOTE' not in h
    return h


def t21(h):
    """K1: HI10 al toegepast. Codebalk, regel onder de cart en alle cartlinks met de code. Hero, onderwerp, blokken en friction reducer gelijk (HI10 houdt de US-regel, PLAYBOOK 12)."""
    a = h.index('STILL PENDING ON YOUR CART ·'); b = h.index('</td></tr>', a)
    h = h[:a] + ('EXTRA 10% ALREADY APPLIED · CODE  <span class="cb-code" style="display:inline-block;border:1px dashed #FFFFFF;'
                 'padding:1px 8px;letter-spacing:2px;word-break:break-all;">HI10</span>\n') + h[b:]
    old = 'Saved as you left it, plus anything else in your cart.'
    assert h.count(old) == 1
    h = h.replace(old, 'Saved as you left it. Your extra 10% is already applied with the button below.')
    n = h.count('https://siraatskitchen.com/cart?utm_source=klaviyo')
    assert n == 7, n
    h = re.sub(r'https://siraatskitchen\.com/cart\?(utm_source=klaviyo(?:&amp;|&)utm_medium=email(?:&amp;|&)utm_campaign=v4-cart(?:&amp;|&)utm_content=k1-[a-z0-9]+)',
               lambda m: 'https://siraatskitchen.com/discount/HI10?redirect=/cart%3F' + m.group(1).replace('&amp;', '%26').replace('&', '%26'), h)
    h = h.replace('?storefront=true&amp;utm_source=klaviyo', '?storefront=true&amp;discount=HI10&amp;utm_source=klaviyo')
    return h


def br1(h, hero=True):
    assert h.count(BR1_BAR_A) == 1 and h.count(BR1_LINE_A) >= 1
    h = h.replace(BR1_BAR_A, BR1_BAR_B).replace(BR1_LINE_A, BR1_LINE_B)
    for pre in ('Two years ago I read about PFAS. This pan is what came out of it.',
                'Here it is again, with the lab report, the 75-year warranty and 10% off.'):
        h = h.replace(pre, BR1_PREVIEW)
    if hero:
        assert h.count(BR1_HERO_A) == 1
        h = h.replace(BR1_HERO_A, BR1_HERO_B)
        h = h.replace('Extra 10% off with code HI10, plus 4 free gifts.', 'The sale price, plus an extra 10% off with code HI10, plus 4 free gifts.')
    return h


VARIANTS = [  # key, naam in Klaviyo, live template-id van A, functie
    ('br1-b1', 'AB Q4 · BR1-B · B1 sale-prijs (WdRz5k)', 'R6E5Zv', lambda h: br1(h, True)),
    ('br1-tp-b1', 'AB Q4 · BR1-B · TP B1 sale-prijs (QNZyEb)', 'TY9hCH', lambda h: br1(h, False)),
    ('t21-k1-hi10', 'AB Q4 · T21-B · K1 met HI10 toegepast', 'Rp3mf6', t21),
    ('t15-p1-lidcard', 'AB Q4 · T15-B · P1-FIRST dekselkaart', 'XhZ3Xr', t15),
]
NEW = [
    ('t23-k4', 'AB Q4 · T23 · K4 termijnen (cart dag 7, US)', ROOT + 'cart/k4-installments.klaviyo.html'),
    ('t24-c5', 'AB Q4 · T24 · C5 termijnen (checkout dag 14, US)', ROOT + 'checkout/c5-installments.klaviyo.html'),
]


def upsert(name, html):
    # naamfilter met een middot werkt niet in de API: bestaande ID's uit template-ids.json
    known = json.load(open(OUT + 'template-ids.json')) if os.path.exists(OUT + 'template-ids.json') else {}
    tid = known.get(name)
    ex = [{'id': tid}] if tid and 'data' in api('GET', '/api/templates/' + tid) else []
    if DRY:
        return 'DRY'
    if ex:
        tid = ex[0]['id']
        r = api('PATCH', '/api/templates/' + tid, {'data': {'type': 'template', 'id': tid, 'attributes': {'html': html}}})
    else:
        r = api('POST', '/api/templates', {'data': {'type': 'template', 'attributes': {'name': name, 'editor_type': 'CODE', 'html': html}}})
    if 'errors' in r:
        raise SystemExit('FOUT %s %s' % (name, json.dumps(r['errors'])[:400]))
    return r['data']['id']


if __name__ == '__main__':
    ids = {}
    for key, name, src, fn in VARIANTS:
        a = api('GET', '/api/templates/' + src)['data']['attributes']['html']
        open(OUT + key + '.a.html', 'w').write(a)
        b = fn(a)
        assert '—' not in b
        open(OUT + key + '.klaviyo.html', 'w').write(b)
        ids[name] = upsert(name, b); print(key, name, ids[name], len(a), len(b))
    for key, name, path in NEW:
        b = open(path).read(); assert '—' not in b
        open(OUT + key + '.klaviyo.html', 'w').write(b)
        ids[name] = upsert(name, b); print(key, name, ids[name], len(b))
    if not DRY:
        json.dump(ids, open(OUT + 'template-ids.json', 'w'), indent=1)
