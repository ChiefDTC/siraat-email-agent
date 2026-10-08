# QA-render rapport

Gegenereerd door `scripts/qa_render.py`. 61 mails: **44 groen**, 17 met FOUT, 43 met waarschuwing.

Tag-allowlist: Django `autoescape, comment, cycle, elif, else, empty, endautoescape, endcomment, endfilter, endfor, endif, endifchanged, endspaceless, endverbatim, endwith, filter, firstof, for, if, ifchanged, lorem, now, regroup, resetcycle, spaceless, templatetag, verbatim, widthratio, with` plus Klaviyo `coupon_code, manage_preferences, manage_preferences_link, today, unsubscribe, unsubscribe_link, web_view, web_view_link`.

## Gebruikte filters

| filter | status | mails |
|---|---|---|
| `cut` | TWIJFEL | 11 |
| `date` | Django | 12 |
| `days_later` | Klaviyo | 12 |
| `default` | Django | 58 |
| `floatformat` | Django | 16 |
| `format_date_string` | Klaviyo | 12 |
| `join` | Django | 32 |
| `lookup` | Klaviyo | 50 |
| `lower` | Django | 29 |
| `upper` | Django | 12 |

## Per mail

| mail | status | varianten | hoogte 390 px | zichtbare `{%`/`{{` in ruwe weergave | V5-STRICT | v5-marktpunten (US, UK, AU, CA, SG, EU, onbekend) |
|---|---|---|---|---|---|---|
| anniversary/n1 | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3076 | 2 | ja | 0 |
| anniversary/n2-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3010 | 2 | ja | 0 |
| anniversary/n2 | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3505 | 9 | ja | 0 |
| browse/b1-acc | let op | vp_pan, vp_set6, vp_apron | 2915 | 4 | ja | 0 |
| browse/b1 | let op | vp_pan, vp_set6, vp_apron | 2879 | 5 | ja | 0 |
| browse/b2-clicked-nocode | FOUT | vp_pan, vp_set6, vp_apron | 2942 | 6 | ja | 0 |
| browse/b2-clicked | let op | vp_pan, vp_set6, vp_apron | 3443 | 13 | ja | 0 |
| browse/b2-notclicked | let op | vp_pan, vp_set6, vp_apron | 3321 | 4 | ja | 0 |
| cart/k1-acc | FOUT | atc_pan, atc_apron, atc_lid_eur | 3129 | 4 | ja | 0 |
| cart/k1 | FOUT | atc_pan, atc_apron, atc_lid_eur | 3420 | 4 | ja | 0 |
| cart/k2-new | FOUT | atc_pan, atc_apron, atc_lid_eur | 3035 | 4 | ja | 0 |
| cart/k2-returning | FOUT | atc_pan, atc_apron, atc_lid_eur | 3085 | 5 | ja | 0 |
| cart/k3-nocode | FOUT | atc_pan, atc_apron, atc_lid_eur | 3011 | 4 | ja | 0 |
| cart/k3 | let op | atc_pan, atc_apron, atc_lid_eur | 3565 | 12 | ja | 0 |
| checkout/c1 | FOUT | co_pan, co_set6, co_apron, co_pan_eur | 3494 | 5 | ja | 0 |
| checkout/c2-acc | FOUT | co_pan, co_set6, co_apron, co_pan_eur | 3313 | 5 | ja | 0 |
| checkout/c2 | let op | co_pan, co_set6, co_apron, co_pan_eur | 3193 | 5 | ja | 0 |
| checkout/c3-acc | FOUT | co_pan, co_set6, co_apron, co_pan_eur | 2948 | 5 | ja | 0 |
| checkout/c3-p | let op | co_pan, co_set6, co_apron, co_pan_eur | 3138 | 5 | ja | 0 |
| checkout/c3-s | FOUT | co_pan, co_set6, co_apron, co_pan_eur | 2918 | 5 | ja | 0 |
| checkout/c4-nocode | FOUT | co_pan, co_set6, co_apron, co_pan_eur | 3126 | 5 | ja | 0 |
| checkout/c4 | let op | co_pan, co_set6, co_apron, co_pan_eur | 3552 | 13 | ja | 0 |
| post-purchase/p1-first | let op | po_pan_us, po_set6, po_apron_us, po_deep | 4077 | 6 | ja | 0 |
| post-purchase/p1-repeat | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3117 | 6 | ja | 0 |
| post-purchase/p2-safe | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3854 | 2 | ja | 0 |
| post-purchase/p2 | let op | po_pan_us, po_set6, po_apron_us, po_deep | 4186 | 2 | ja | 0 |
| post-purchase/p3-accessory-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 2977 | 2 | ja | 0 |
| post-purchase/p3-accessory | FOUT | po_pan_us, po_set6, po_apron_us, po_deep | 3473 | 9 | ja | 0 |
| post-purchase/p3-apron-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 2903 | 2 | ja | 0 |
| post-purchase/p3-apron | FOUT | po_pan_us, po_set6, po_apron_us, po_deep | 3472 | 9 | ja | 0 |
| post-purchase/p3-next-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3024 | 2 | ja | 0 |
| post-purchase/p3-next | FOUT | po_pan_us, po_set6, po_apron_us, po_deep | 3520 | 9 | ja | 0 |
| post-purchase/p3-pan-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3003 | 2 | ja | 0 |
| post-purchase/p3-pan | FOUT | po_pan_us, po_set6, po_apron_us, po_deep | 3548 | 9 | ja | 0 |
| post-purchase/p3-set-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3024 | 2 | ja | 0 |
| post-purchase/p3-set | FOUT | po_pan_us, po_set6, po_apron_us, po_deep | 3545 | 9 | ja | 0 |
| site/a1 | let op | none | 3094 | 2 | ja | 0 |
| site/a2 | let op | none | 2915 | 2 | ja | 0 |
| sunset/s1 | groen | none | 1816 | 2 | ja | 0 |
| sunset/s2 | groen | none | 1499 | 2 | ja | 0 |
| sunset/s3-kept | groen | none | 1790 | 2 | ja | 0 |
| sunset/s4-kept | groen | none | 1657 | 2 | ja | 0 |
| ugc/u1 | groen | none | 3088 | 2 | ja | 0 |
| vip/v1-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep, po_pan_us+pool | 3061 | 2 | ja | 0 |
| vip/v1 | FOUT | po_pan_us, po_set6, po_apron_us, po_deep, po_pan_us+pool | 3581 | 9 | ja | 0 |
| vip/v2 | groen | po_pan_us, po_set6, po_apron_us, po_deep, po_pan_us+pool | 1389 | 2 | ja | 0 |
| welcome/w0 | let op | none | 3332 | 2 | ja | 0 |
| welcome/w1-a | let op | none | 3484 | 1 | ja | 0 |
| welcome/w1-b | let op | none | 3406 | 1 | ja | 0 |
| welcome/w2 | let op | none | 2597 | 2 | ja | 0 |
| welcome/w3 | let op | none | 3533 | 2 | ja | 0 |
| welcome/w4-int | let op | none | 3103 | 2 | ja | 0 |
| welcome/w4-us | let op | none | 3082 | 2 | ja | 0 |
| welcome/w5 | let op | none | 3531 | 1 | ja | 0 |
| winback/r1-acc | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3460 | 2 | ja | 0 |
| winback/r1-pan | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3021 | 2 | ja | 0 |
| winback/r1-set | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3046 | 2 | ja | 0 |
| winback/r2-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3186 | 2 | ja | 0 |
| winback/r2-vip-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3207 | 2 | ja | 0 |
| winback/r2-vip | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3577 | 11 | ja | 0 |
| winback/r2 | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3526 | 11 | ja | 0 |

## Fouten en waarschuwingen

- let op anniversary/n2: ruw 390 px (code-editor mobiel): tabel 570 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b1-acc: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b1-acc: outlook: preheader zonder mso-hide:all
- let op browse/b1-acc: ruw 390 px (code-editor mobiel): tabel 464 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b1: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b1: outlook: preheader zonder mso-hide:all
- let op browse/b1: ruw 390 px (code-editor mobiel): tabel 575 px breed door lange Django-expressies; gerenderd in orde
- FOUT browse/b2-clicked-nocode: raw 600 px: horizontale overflow (867 > 600)
- FOUT browse/b2-clicked-nocode: raw 600 px: hoofdtabel 867 px (moet 600)
- FOUT browse/b2-clicked-nocode: raw 600 px: breed beeld niet op volle breedte: b2-clicked-nocode-hero-v5.jpg 600/867 px
- let op browse/b2-clicked-nocode: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-clicked-nocode: outlook: preheader zonder mso-hide:all
- let op browse/b2-clicked-nocode: ruw 390 px (code-editor mobiel): tabel 867 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b2-clicked: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-clicked: outlook: preheader zonder mso-hide:all
- let op browse/b2-clicked: ruw 390 px (code-editor mobiel): tabel 502 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b2-notclicked: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-notclicked: outlook: preheader zonder mso-hide:all
- let op browse/b2-notclicked: ruw 390 px (code-editor mobiel): tabel 575 px breed door lange Django-expressies; gerenderd in orde
- FOUT cart/k1-acc: raw 600 px: horizontale overflow (867 > 600)
- FOUT cart/k1-acc: raw 600 px: hoofdtabel 867 px (moet 600)
- FOUT cart/k1-acc: raw 600 px: breed beeld niet op volle breedte: k1acc-hero-v5.jpg 600/867 px
- let op cart/k1-acc: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k1-acc: ruw 390 px (code-editor mobiel): tabel 867 px breed door lange Django-expressies; gerenderd in orde
- FOUT cart/k1: raw 600 px: horizontale overflow (867 > 600)
- FOUT cart/k1: raw 600 px: hoofdtabel 867 px (moet 600)
- FOUT cart/k1: raw 600 px: breed beeld niet op volle breedte: k1-hero-v5.jpg 600/867 px
- let op cart/k1: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k1: plain-text: 4 regel(s) dubbel in Klaviyo's automatische tekstversie (verborgen desk/mob-varianten), bijv. "No coating, so nothing to scrub around."
- let op cart/k1: ruw 390 px (code-editor mobiel): tabel 867 px breed door lange Django-expressies; gerenderd in orde
- FOUT cart/k2-new: raw 600 px: horizontale overflow (867 > 600)
- FOUT cart/k2-new: raw 600 px: hoofdtabel 867 px (moet 600)
- FOUT cart/k2-new: raw 600 px: breed beeld niet op volle breedte: k2-new-hero-v5.jpg 600/867 px
- let op cart/k2-new: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k2-new: ruw 390 px (code-editor mobiel): tabel 867 px breed door lange Django-expressies; gerenderd in orde
- FOUT cart/k2-returning: raw 600 px: horizontale overflow (867 > 600)
- FOUT cart/k2-returning: raw 600 px: hoofdtabel 867 px (moet 600)
- FOUT cart/k2-returning: raw 600 px: breed beeld niet op volle breedte: k2-returning-hero-v5.jpg 600/867 px
- let op cart/k2-returning: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k2-returning: ruw 390 px (code-editor mobiel): tabel 867 px breed door lange Django-expressies; gerenderd in orde
- FOUT cart/k3-nocode: raw 600 px: horizontale overflow (867 > 600)
- FOUT cart/k3-nocode: raw 600 px: hoofdtabel 867 px (moet 600)
- FOUT cart/k3-nocode: raw 600 px: breed beeld niet op volle breedte: k3-nocode-hero-v5.jpg 600/867 px
- let op cart/k3-nocode: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k3-nocode: ruw 390 px (code-editor mobiel): tabel 867 px breed door lange Django-expressies; gerenderd in orde
- let op cart/k3: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k3: ruw 390 px (code-editor mobiel): tabel 503 px breed door lange Django-expressies; gerenderd in orde
- FOUT checkout/c1: raw 600 px: horizontale overflow (867 > 600)
- FOUT checkout/c1: raw 600 px: hoofdtabel 867 px (moet 600)
- let op checkout/c1: inbox: 3 uitroeptekens in de body
- let op checkout/c1: ruw 390 px (code-editor mobiel): tabel 867 px breed door lange Django-expressies; gerenderd in orde
- FOUT checkout/c2-acc: raw 600 px: horizontale overflow (867 > 600)
- FOUT checkout/c2-acc: raw 600 px: hoofdtabel 867 px (moet 600)
- FOUT checkout/c2-acc: raw 600 px: breed beeld niet op volle breedte: c2acc-hero-v5.jpg 600/867 px
- let op checkout/c2-acc: ruw 390 px (code-editor mobiel): tabel 867 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c2: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- FOUT checkout/c3-acc: raw 600 px: horizontale overflow (867 > 600)
- FOUT checkout/c3-acc: raw 600 px: hoofdtabel 867 px (moet 600)
- FOUT checkout/c3-acc: raw 600 px: breed beeld niet op volle breedte: c3acc-hero-v5.jpg 600/867 px
- let op checkout/c3-acc: ruw 390 px (code-editor mobiel): tabel 867 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c3-p: inbox: spamsignalen in de body: "FREE"
- let op checkout/c3-p: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- FOUT checkout/c3-s: raw 600 px: horizontale overflow (867 > 600)
- FOUT checkout/c3-s: raw 600 px: hoofdtabel 867 px (moet 600)
- FOUT checkout/c3-s: raw 600 px: breed beeld niet op volle breedte: c3s-hero-v5.jpg 600/867 px
- let op checkout/c3-s: ruw 390 px (code-editor mobiel): tabel 867 px breed door lange Django-expressies; gerenderd in orde
- FOUT checkout/c4-nocode: raw 600 px: horizontale overflow (867 > 600)
- FOUT checkout/c4-nocode: raw 600 px: hoofdtabel 867 px (moet 600)
- FOUT checkout/c4-nocode: raw 600 px: breed beeld niet op volle breedte: c4-nocode-hero-v5.jpg 600/867 px
- let op checkout/c4-nocode: ruw 390 px (code-editor mobiel): tabel 867 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c4: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p1-first: hoogte 4077 px op 390 px bij po_pan_us (geen verkoopmail of P2: langer toegestaan)
- let op post-purchase/p1-first: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p1-repeat: inbox: 3 uitroeptekens in de body
- let op post-purchase/p1-repeat: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p2-safe: hoogte 3854 px op 390 px bij po_pan_us (geen verkoopmail of P2: langer toegestaan)
- let op post-purchase/p2: hoogte 4186 px op 390 px bij po_pan_us (geen verkoopmail of P2: langer toegestaan)
- FOUT post-purchase/p3-accessory: raw 600 px: horizontale overflow (648 > 600)
- FOUT post-purchase/p3-accessory: raw 600 px: hoofdtabel 648 px (moet 600)
- FOUT post-purchase/p3-accessory: raw 600 px: breed beeld niet op volle breedte: p3-accessory-hero.jpg 600/648 px
- let op post-purchase/p3-accessory: ruw 390 px (code-editor mobiel): tabel 648 px breed door lange Django-expressies; gerenderd in orde
- FOUT post-purchase/p3-apron: raw 600 px: horizontale overflow (648 > 600)
- FOUT post-purchase/p3-apron: raw 600 px: hoofdtabel 648 px (moet 600)
- FOUT post-purchase/p3-apron: raw 600 px: breed beeld niet op volle breedte: p3-apron-hero.jpg 600/648 px
- let op post-purchase/p3-apron: ruw 390 px (code-editor mobiel): tabel 648 px breed door lange Django-expressies; gerenderd in orde
- FOUT post-purchase/p3-next: raw 600 px: horizontale overflow (648 > 600)
- FOUT post-purchase/p3-next: raw 600 px: hoofdtabel 648 px (moet 600)
- FOUT post-purchase/p3-next: raw 600 px: breed beeld niet op volle breedte: p3-next-hero.jpg 600/648 px
- let op post-purchase/p3-next: ruw 390 px (code-editor mobiel): tabel 648 px breed door lange Django-expressies; gerenderd in orde
- FOUT post-purchase/p3-pan: raw 600 px: horizontale overflow (648 > 600)
- FOUT post-purchase/p3-pan: raw 600 px: hoofdtabel 648 px (moet 600)
- FOUT post-purchase/p3-pan: raw 600 px: breed beeld niet op volle breedte: p3-pan-hero.jpg 600/648 px
- let op post-purchase/p3-pan: ruw 390 px (code-editor mobiel): tabel 648 px breed door lange Django-expressies; gerenderd in orde
- FOUT post-purchase/p3-set: raw 600 px: horizontale overflow (648 > 600)
- FOUT post-purchase/p3-set: raw 600 px: hoofdtabel 648 px (moet 600)
- FOUT post-purchase/p3-set: raw 600 px: breed beeld niet op volle breedte: p3-set-hero.jpg 600/648 px
- let op post-purchase/p3-set: ruw 390 px (code-editor mobiel): tabel 648 px breed door lange Django-expressies; gerenderd in orde
- let op site/a1: outlook: preheader zonder mso-hide:all
- let op site/a2: outlook: preheader zonder mso-hide:all
- let op site/a2: ruw 390 px (code-editor mobiel): tabel 557 px breed door lange Django-expressies; gerenderd in orde
- FOUT vip/v1: raw 600 px: horizontale overflow (634 > 600)
- FOUT vip/v1: raw 600 px: hoofdtabel 634 px (moet 600)
- FOUT vip/v1: raw 600 px: breed beeld niet op volle breedte: v1-hero.jpg 600/634 px
- let op vip/v1: inbox: spamsignalen in de body: "Get it now"
- let op vip/v1: ruw 390 px (code-editor mobiel): tabel 634 px breed door lange Django-expressies; gerenderd in orde
- let op welcome/w0: outlook: preheader zonder mso-hide:all
- let op welcome/w1-a: outlook: preheader zonder mso-hide:all
- let op welcome/w1-a: ruw 390 px (code-editor mobiel): tabel 508 px breed door lange Django-expressies; gerenderd in orde
- let op welcome/w1-b: outlook: preheader zonder mso-hide:all
- let op welcome/w1-b: ruw 390 px (code-editor mobiel): tabel 456 px breed door lange Django-expressies; gerenderd in orde
- let op welcome/w2: outlook: preheader zonder mso-hide:all
- let op welcome/w3: outlook: preheader zonder mso-hide:all
- let op welcome/w4-int: outlook: preheader zonder mso-hide:all
- let op welcome/w4-int: ruw 390 px (code-editor mobiel): tabel 551 px breed door lange Django-expressies; gerenderd in orde
- let op welcome/w4-us: outlook: preheader zonder mso-hide:all
- let op welcome/w4-us: ruw 390 px (code-editor mobiel): tabel 551 px breed door lange Django-expressies; gerenderd in orde
- let op welcome/w5: outlook: preheader zonder mso-hide:all
- let op welcome/w5: ruw 390 px (code-editor mobiel): tabel 508 px breed door lange Django-expressies; gerenderd in orde
- let op winback/r1-acc: ruw 390 px (code-editor mobiel): tabel 515 px breed door lange Django-expressies; gerenderd in orde
- let op winback/r2-vip: ruw 390 px (code-editor mobiel): tabel 554 px breed door lange Django-expressies; gerenderd in orde
- let op winback/r2: ruw 390 px (code-editor mobiel): tabel 501 px breed door lange Django-expressies; gerenderd in orde

Screenshots: `exports/qa/shots/<flow>-<id>-<desktop|mobile>-<rendered|raw>.jpg` (gerenderd = eerste variant).
