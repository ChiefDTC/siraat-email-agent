#!/usr/bin/env python3
"""Affiliate-blok voor P1-FIRST en P1-REPEAT (Floris 22 okt 2026: link binnen ~1 uur na aankoop).

Maakt uit klaviyo/templates/v3/affiliate/aff-block.klaviyo.html de P1-variant
(klaviyo/templates/v3/affiliate/aff-block-p1.klaviyo.html):
- kop "Give 15%, get 15%" (uit de profielvariabelen, dus nooit een ander percentage dan Snowball zegt),
- rekensom op de waarde van DEZE order (event $value, alleen bij USD; anders het Pan Pro Duo-marktvoorbeeld),
- Inter in plaats van Instrument Serif (P1 laadt die font niet).
Met --insert <live.html> <out.html> zet het blok direct onder de eerste alinea ("Hi {{ first_name ...").
Raakt niets in Klaviyo aan.
"""
import re, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "klaviyo/templates/v3/affiliate/aff-block.klaviyo.html")
OUT = os.path.join(ROOT, "klaviyo/templates/v3/affiliate/aff-block-p1.klaviyo.html")


def build():
    h = open(SRC).read()
    h = h.split("\n", 1)[1]  # topcomment weg
    h = h.replace("ov=person|lookup:'Siraat Last Order Value'|default:''", "ov=event|lookup:'$value'|default:''")
    h = h.replace("oc=person|lookup:'Siraat Last Order Currency'|default:''", "oc=event.extra.presentment_currency|default:'USD'")
    # $value is in winkelvaluta (USD): niet-USD-takken weg, die vallen terug op het marktvoorbeeld
    h = re.sub(r"\{% elif rw == '15%' and fo == '15%' and ov and oc == '(GBP|EUR|CAD|AUD|NZD|SGD)' and ov <= [\d.]+ %\}.*?</b>", "", h)
    h = h.replace("Your last order was", "Your order was")
    h = re.sub(r'<div style="font-size:11px;line-height:14px;letter-spacing:2px;font-weight:600;color:#AC3B19;">GIVE (.*?), GET (.*?)</div>',
               r'<div style="font-size:11px;line-height:14px;letter-spacing:2px;font-weight:600;color:#AC3B19;">YOUR OWN SIRAAT LINK</div>', h)
    h = h.replace(
        """<div style="padding-top:8px;font-family:'Instrument Serif','Times New Roman',serif;font-style:italic;font-size:28px;line-height:32px;color:#282828;">Your order can pay for itself.</div>""",
        """<div style="padding-top:8px;font-family:Inter,Arial,Helvetica,sans-serif;font-size:24px;line-height:30px;font-weight:600;color:#282828;">Give {{ person|lookup:'Referral Friend Offer - SocialSnowball'|default:'15%' }}, get {{ person|lookup:'Referral Reward - SocialSnowball'|default:'15%' }}</div>""")
    assert "Give {{" in h and "event|lookup:'$value'" in h and "oc == 'GBP'" not in h
    head = "<!-- AFF-BLOCK P1 (gegenereerd door scripts/aff_p1_block.py uit aff-block.klaviyo.html): onder de eerste alinea van P1-FIRST/P1-REPEAT. Toont alleen met Referral Link en snow_pilot != out. -->\n"
    open(OUT, "w").write(head + h)
    return h


def insert(live, out):
    blk = build()
    h = open(live).read()
    i = h.find("Hi {{ first_name")
    assert i > 0, "eerste alinea niet gevonden"
    j = h.find("</td></tr>", i) + len("</td></tr>")
    open(out, "w").write(h[:j] + "\n" + blk + h[j:])


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "--insert":
        insert(sys.argv[2], sys.argv[3])
    else:
        build()
    print("ok")
