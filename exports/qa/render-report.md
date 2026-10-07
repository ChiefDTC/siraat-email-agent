# QA-render rapport

Gegenereerd door `scripts/qa_render.py`. 61 mails: **61 groen**, 0 met FOUT, 24 met waarschuwing.

Tag-allowlist: Django `autoescape, comment, cycle, elif, else, empty, endautoescape, endcomment, endfilter, endfor, endif, endifchanged, endspaceless, endverbatim, endwith, filter, firstof, for, if, ifchanged, lorem, now, regroup, resetcycle, spaceless, templatetag, verbatim, widthratio, with` plus Klaviyo `coupon_code, manage_preferences, manage_preferences_link, unsubscribe, unsubscribe_link, web_view, web_view_link`.

## Gebruikte filters

| filter | status | mails |
|---|---|---|
| `cut` | TWIJFEL | 5 |
| `default` | Django | 57 |
| `floatformat` | Django | 18 |
| `join` | Django | 20 |
| `lookup` | Klaviyo | 7 |
| `slice` | TWIJFEL | 5 |

## Per mail

| mail | status | varianten | hoogte 390 px | zichtbare `{%`/`{{` in ruwe weergave |
|---|---|---|---|---|
| anniversary/n1 | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3268 | 4 |
| anniversary/n2-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3395 | 4 |
| anniversary/n2 | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3102 | 6 |
| browse/b1-acc | let op | vp_pan, vp_set6, vp_apron | 3160 | 6 |
| browse/b1 | let op | vp_pan, vp_set6, vp_apron | 3580 | 6 |
| browse/b2-clicked-nocode | let op | vp_pan, vp_set6, vp_apron | 2980 | 6 |
| browse/b2-clicked | let op | vp_pan, vp_set6, vp_apron | 3435 | 8 |
| browse/b2-notclicked | let op | vp_pan, vp_set6, vp_apron | 3343 | 5 |
| cart/k1-acc | let op | atc_pan, atc_apron, atc_lid_eur | 3121 | 6 |
| cart/k1 | groen | atc_pan, atc_apron, atc_lid_eur | 3578 | 6 |
| cart/k2-new | groen | atc_pan, atc_apron, atc_lid_eur | 3288 | 6 |
| cart/k2-returning | groen | atc_pan, atc_apron, atc_lid_eur | 3492 | 6 |
| cart/k3-nocode | groen | atc_pan, atc_apron, atc_lid_eur | 3385 | 6 |
| cart/k3 | groen | atc_pan, atc_apron, atc_lid_eur | 3598 | 8 |
| checkout/c1 | let op | co_pan, co_set6, co_apron, co_pan_eur | 3639 | 7 |
| checkout/c2-acc | let op | co_pan, co_set6, co_apron, co_pan_eur | 3276 | 7 |
| checkout/c2 | let op | co_pan, co_set6, co_apron, co_pan_eur | 3578 | 7 |
| checkout/c3-acc | let op | co_pan, co_set6, co_apron, co_pan_eur | 3440 | 7 |
| checkout/c3-p | let op | co_pan, co_set6, co_apron, co_pan_eur | 3527 | 7 |
| checkout/c3-s | let op | co_pan, co_set6, co_apron, co_pan_eur | 3589 | 7 |
| checkout/c4-int-nocode | let op | co_pan, co_set6, co_apron, co_pan_eur | 3321 | 7 |
| checkout/c4-int | let op | co_pan, co_set6, co_apron, co_pan_eur | 3489 | 9 |
| checkout/c4-us-nocode | let op | co_pan, co_set6, co_apron, co_pan_eur | 3473 | 7 |
| checkout/c4-us | let op | co_pan, co_set6, co_apron, co_pan_eur | 3576 | 9 |
| post-purchase/p1-first | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3835 | 8 |
| post-purchase/p1-repeat | let op | po_pan_us, po_set6, po_apron_us, po_deep | 2827 | 8 |
| post-purchase/p2-safe | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3496 | 4 |
| post-purchase/p2 | let op | po_pan_us, po_set6, po_apron_us, po_deep | 4024 | 4 |
| post-purchase/p3-accessory-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3527 | 4 |
| post-purchase/p3-accessory | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3286 | 6 |
| post-purchase/p3-apron-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3154 | 4 |
| post-purchase/p3-apron | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3432 | 6 |
| post-purchase/p3-next-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3370 | 4 |
| post-purchase/p3-next | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3558 | 6 |
| post-purchase/p3-pan-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3226 | 4 |
| post-purchase/p3-pan | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3522 | 6 |
| post-purchase/p3-set-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3290 | 4 |
| post-purchase/p3-set | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3586 | 6 |
| site/a1 | groen | none | 3509 | 4 |
| site/a2 | groen | none | 3568 | 4 |
| sunset/s1 | groen | none | 1816 | 4 |
| sunset/s2 | groen | none | 1499 | 4 |
| ugc/u1 | groen | none | 2942 | 4 |
| vip/v1-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep, po_pan_us+pool | 3517 | 4 |
| vip/v1 | groen | po_pan_us, po_set6, po_apron_us, po_deep, po_pan_us+pool | 3099 | 6 |
| vip/v2 | groen | po_pan_us, po_set6, po_apron_us, po_deep, po_pan_us+pool | 1371 | 4 |
| welcome/w0 | groen | none | 2932 | 4 |
| welcome/w1-a | groen | none | 3412 | 4 |
| welcome/w1-b | groen | none | 3425 | 4 |
| welcome/w2 | groen | none | 2335 | 4 |
| welcome/w3 | groen | none | 3247 | 3 |
| welcome/w4-int | groen | none | 3345 | 3 |
| welcome/w4-us | groen | none | 3534 | 3 |
| welcome/w5 | groen | none | 3507 | 3 |
| winback/r1-acc | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3543 | 4 |
| winback/r1-pan | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3516 | 4 |
| winback/r1-set | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3426 | 4 |
| winback/r2-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3427 | 4 |
| winback/r2-vip-nocode | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3476 | 4 |
| winback/r2-vip | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3156 | 6 |
| winback/r2 | groen | po_pan_us, po_set6, po_apron_us, po_deep | 3113 | 6 |

## Fouten en waarschuwingen

- let op browse/b1-acc: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b1-acc: filter |slice: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.Price|slice). Controleer één keer met Preview in Klaviyo.
- let op browse/b1-acc: ruw 390 px (code-editor mobiel): tabel 464 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b1: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b1: filter |slice: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.Price|slice). Controleer één keer met Preview in Klaviyo.
- let op browse/b1: ruw 390 px (code-editor mobiel): tabel 494 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b2-clicked-nocode: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-clicked-nocode: filter |slice: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.Price|slice). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-clicked-nocode: ruw 390 px (code-editor mobiel): tabel 494 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b2-clicked: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-clicked: filter |slice: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.Price|slice). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-clicked: ruw 390 px (code-editor mobiel): tabel 494 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b2-notclicked: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-notclicked: filter |slice: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.Price|slice). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-notclicked: ruw 390 px (code-editor mobiel): tabel 494 px breed door lange Django-expressies; gerenderd in orde
- let op cart/k1-acc: ruw 390 px (code-editor mobiel): tabel 468 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c1: hoogte 3639 px op 390 px (max ~3600) bij co_set6
- let op checkout/c1: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c2-acc: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c2: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c3-acc: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c3-p: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c3-s: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c4-int-nocode: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c4-int: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c4-us-nocode: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c4-us: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p1-first: hoogte 3835 px op 390 px bij po_set6 (geen verkoopmail of P2: langer toegestaan)
- let op post-purchase/p1-first: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p1-repeat: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p2: hoogte 4024 px op 390 px bij po_pan_us (geen verkoopmail of P2: langer toegestaan)
- let op post-purchase/p3-accessory: ruw 390 px (code-editor mobiel): tabel 495 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p3-apron: ruw 390 px (code-editor mobiel): tabel 495 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p3-next: ruw 390 px (code-editor mobiel): tabel 495 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p3-pan: ruw 390 px (code-editor mobiel): tabel 495 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p3-set: ruw 390 px (code-editor mobiel): tabel 495 px breed door lange Django-expressies; gerenderd in orde

Screenshots: `exports/qa/shots/<flow>-<id>-<desktop|mobile>-<rendered|raw>.jpg` (gerenderd = eerste variant).
