# QA-render rapport

Gegenereerd door `scripts/qa_render.py`. 59 mails: **59 groen**, 0 met FOUT, 59 met waarschuwing.

Tag-allowlist: Django `autoescape, comment, cycle, elif, else, empty, endautoescape, endcomment, endfilter, endfor, endif, endifchanged, endspaceless, endverbatim, endwith, filter, firstof, for, if, ifchanged, lorem, now, regroup, resetcycle, spaceless, templatetag, verbatim, widthratio, with` plus Klaviyo `coupon_code, manage_preferences, manage_preferences_link, today, unsubscribe, unsubscribe_link, web_view, web_view_link`.

## Gebruikte filters

| filter | status | mails |
|---|---|---|
| `cut` | TWIJFEL | 11 |
| `date` | Django | 12 |
| `days_later` | Klaviyo | 12 |
| `default` | Django | 55 |
| `floatformat` | Django | 16 |
| `format_date_string` | Klaviyo | 12 |
| `join` | Django | 22 |
| `lookup` | Klaviyo | 7 |
| `slice` | TWIJFEL | 5 |
| `upper` | Django | 12 |

## Per mail

| mail | status | varianten | hoogte 390 px | zichtbare `{%`/`{{` in ruwe weergave |
|---|---|---|---|---|
| anniversary/n1 | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3292 | 4 |
| anniversary/n2-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3395 | 4 |
| anniversary/n2 | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3248 | 11 |
| browse/b1-acc | let op | vp_pan, vp_set6, vp_apron | 3458 | 6 |
| browse/b1 | let op | vp_pan, vp_set6, vp_apron | 3605 | 6 |
| browse/b2-clicked-nocode | let op | vp_pan, vp_set6, vp_apron | 2980 | 6 |
| browse/b2-clicked | let op | vp_pan, vp_set6, vp_apron | 3581 | 13 |
| browse/b2-notclicked | let op | vp_pan, vp_set6, vp_apron | 3343 | 5 |
| cart/k1-acc | let op | atc_pan, atc_apron, atc_lid_eur | 3398 | 6 |
| cart/k1 | let op | atc_pan, atc_apron, atc_lid_eur | 3578 | 6 |
| cart/k2-new | let op | atc_pan, atc_apron, atc_lid_eur | 3330 | 6 |
| cart/k2-returning | let op | atc_pan, atc_apron, atc_lid_eur | 3492 | 6 |
| cart/k3-nocode | let op | atc_pan, atc_apron, atc_lid_eur | 3385 | 6 |
| cart/k3 | let op | atc_pan, atc_apron, atc_lid_eur | 3523 | 13 |
| checkout/c1 | let op | co_pan, co_set6, co_apron, co_pan_eur | 3684 | 7 |
| checkout/c2-acc | let op | co_pan, co_set6, co_apron, co_pan_eur | 3276 | 7 |
| checkout/c2 | let op | co_pan, co_set6, co_apron, co_pan_eur | 3578 | 7 |
| checkout/c3-acc | let op | co_pan, co_set6, co_apron, co_pan_eur | 3440 | 7 |
| checkout/c3-p | let op | co_pan, co_set6, co_apron, co_pan_eur | 3575 | 7 |
| checkout/c3-s | let op | co_pan, co_set6, co_apron, co_pan_eur | 3589 | 7 |
| checkout/c4-nocode | let op | co_pan, co_set6, co_apron, co_pan_eur | 3438 | 7 |
| checkout/c4 | let op | co_pan, co_set6, co_apron, co_pan_eur | 3552 | 14 |
| post-purchase/p1-first | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3885 | 8 |
| post-purchase/p1-repeat | let op | po_pan_us, po_set6, po_apron_us, po_deep | 2827 | 8 |
| post-purchase/p2-safe | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3546 | 4 |
| post-purchase/p2 | let op | po_pan_us, po_set6, po_apron_us, po_deep | 4170 | 4 |
| post-purchase/p3-accessory-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3552 | 4 |
| post-purchase/p3-accessory | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3507 | 11 |
| post-purchase/p3-apron-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3154 | 4 |
| post-purchase/p3-apron | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3603 | 11 |
| post-purchase/p3-next-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3370 | 4 |
| post-purchase/p3-next | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3180 | 11 |
| post-purchase/p3-pan-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3243 | 4 |
| post-purchase/p3-pan | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3144 | 11 |
| post-purchase/p3-set-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3523 | 4 |
| post-purchase/p3-set | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3602 | 11 |
| site/a1 | let op | none | 3509 | 4 |
| site/a2 | let op | none | 3568 | 4 |
| sunset/s1 | let op | none | 1816 | 4 |
| sunset/s2 | let op | none | 1499 | 4 |
| ugc/u1 | let op | none | 2942 | 4 |
| vip/v1-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep, po_pan_us+pool | 3403 | 4 |
| vip/v1 | let op | po_pan_us, po_set6, po_apron_us, po_deep, po_pan_us+pool | 3121 | 11 |
| vip/v2 | let op | po_pan_us, po_set6, po_apron_us, po_deep, po_pan_us+pool | 1371 | 4 |
| welcome/w0 | let op | none | 2932 | 4 |
| welcome/w1-a | let op | none | 3490 | 4 |
| welcome/w1-b | let op | none | 3503 | 4 |
| welcome/w2 | let op | none | 2335 | 4 |
| welcome/w3 | let op | none | 3247 | 3 |
| welcome/w4-int | let op | none | 3345 | 3 |
| welcome/w4-us | let op | none | 3534 | 3 |
| welcome/w5 | let op | none | 3507 | 3 |
| winback/r1-acc | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3543 | 4 |
| winback/r1-pan | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3352 | 4 |
| winback/r1-set | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3426 | 4 |
| winback/r2-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3427 | 4 |
| winback/r2-vip-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3476 | 4 |
| winback/r2-vip | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3302 | 11 |
| winback/r2 | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3404 | 11 |

## Fouten en waarschuwingen

- let op anniversary/n1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op anniversary/n1: inbox: spamsignalen in de body: "FREE"
- let op anniversary/n1: outlook: preheader zonder mso-hide:all
- let op anniversary/n2-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op anniversary/n2-nocode: inbox: spamsignalen in de body: "FREE" x2
- let op anniversary/n2-nocode: outlook: preheader zonder mso-hide:all
- let op anniversary/n2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op anniversary/n2: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Claim my 10% →"
- let op anniversary/n2: outlook: preheader zonder mso-hide:all
- let op browse/b1-acc: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op browse/b1-acc: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b1-acc: filter |slice: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.Price|slice). Controleer één keer met Preview in Klaviyo.
- let op browse/b1-acc: inbox: spamsignalen in de body: "FREE"
- let op browse/b1-acc: outlook: preheader zonder mso-hide:all
- let op browse/b1-acc: ruw 390 px (code-editor mobiel): tabel 464 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op browse/b1: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b1: filter |slice: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.Price|slice). Controleer één keer met Preview in Klaviyo.
- let op browse/b1: hoogte 3605 px op 390 px (max ~3600) bij vp_pan
- let op browse/b1: outlook: preheader zonder mso-hide:all
- let op browse/b1: ruw 390 px (code-editor mobiel): tabel 575 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b2-clicked-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op browse/b2-clicked-nocode: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-clicked-nocode: filter |slice: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.Price|slice). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-clicked-nocode: inbox: spamsignalen in de body: "FREE"
- let op browse/b2-clicked-nocode: outlook: preheader zonder mso-hide:all
- let op browse/b2-clicked-nocode: ruw 390 px (code-editor mobiel): tabel 575 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b2-clicked: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op browse/b2-clicked: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-clicked: filter |slice: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.Price|slice). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-clicked: inbox: spamsignalen in de body: "FREE"
- let op browse/b2-clicked: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% now →"
- let op browse/b2-clicked: outlook: preheader zonder mso-hide:all
- let op browse/b2-clicked: ruw 390 px (code-editor mobiel): tabel 570 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b2-notclicked: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op browse/b2-notclicked: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-notclicked: filter |slice: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.Price|slice). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-notclicked: inbox: spamsignalen in de body: "FREE"
- let op browse/b2-notclicked: outlook: preheader zonder mso-hide:all
- let op browse/b2-notclicked: ruw 390 px (code-editor mobiel): tabel 575 px breed door lange Django-expressies; gerenderd in orde
- let op cart/k1-acc: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op cart/k1-acc: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k1-acc: inbox: spamsignalen in de body: "FREE"
- let op cart/k1-acc: outlook: preheader zonder mso-hide:all
- let op cart/k1-acc: ruw 390 px (code-editor mobiel): tabel 468 px breed door lange Django-expressies; gerenderd in orde
- let op cart/k1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op cart/k1: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k1: outlook: preheader zonder mso-hide:all
- let op cart/k1: plain-text: 4 regel(s) dubbel in Klaviyo's automatische tekstversie (verborgen desk/mob-varianten), bijv. "No coating, so nothing to scrub around."
- let op cart/k1: ruw 390 px (code-editor mobiel): tabel 409 px breed door lange Django-expressies; gerenderd in orde
- let op cart/k2-new: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op cart/k2-new: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k2-new: outlook: preheader zonder mso-hide:all
- let op cart/k2-new: ruw 390 px (code-editor mobiel): tabel 409 px breed door lange Django-expressies; gerenderd in orde
- let op cart/k2-returning: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op cart/k2-returning: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k2-returning: inbox: spamsignalen in de body: "FREE"
- let op cart/k2-returning: outlook: preheader zonder mso-hide:all
- let op cart/k3-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op cart/k3-nocode: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k3-nocode: inbox: spamsignalen in de body: "FREE"
- let op cart/k3-nocode: outlook: preheader zonder mso-hide:all
- let op cart/k3: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op cart/k3: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k3: inbox: spamsignaal in onderwerp A: "Last chance"
- let op cart/k3: inbox: spamsignalen in de body: "Last chance"
- let op cart/k3: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% now →"
- let op cart/k3: outlook: preheader zonder mso-hide:all
- let op checkout/c1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c1: hoogte 3684 px op 390 px (max ~3600) bij co_pan
- let op checkout/c1: outlook: preheader zonder mso-hide:all
- let op checkout/c1: plain-text: 3 regel(s) dubbel in Klaviyo's automatische tekstversie (verborgen desk/mob-varianten), bijv. "“Great to know no chemicals are being released into our food"
- let op checkout/c1: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c2-acc: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c2-acc: inbox: spamsignalen in de body: "FREE"
- let op checkout/c2-acc: outlook: preheader zonder mso-hide:all
- let op checkout/c2-acc: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c2: outlook: preheader zonder mso-hide:all
- let op checkout/c2: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c3-acc: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c3-acc: inbox: spamsignalen in de body: "FREE"
- let op checkout/c3-acc: outlook: preheader zonder mso-hide:all
- let op checkout/c3-acc: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c3-p: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c3-p: inbox: spamsignalen in de body: "FREE"
- let op checkout/c3-p: outlook: preheader zonder mso-hide:all
- let op checkout/c3-p: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c3-s: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c3-s: outlook: preheader zonder mso-hide:all
- let op checkout/c3-s: plain-text: 3 regel(s) dubbel in Klaviyo's automatische tekstversie (verborgen desk/mob-varianten), bijv. "Every pan goes stovetop to oven."
- let op checkout/c3-s: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c4-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c4-nocode: inbox: spamsignalen in de body: "FREE"
- let op checkout/c4-nocode: outlook: preheader zonder mso-hide:all
- let op checkout/c4-nocode: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c4: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c4: inbox: spamsignalen in de body: "Last chance"
- let op checkout/c4: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% now →"
- let op checkout/c4: outlook: preheader zonder mso-hide:all
- let op checkout/c4: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p1-first: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p1-first: hoogte 3885 px op 390 px bij po_set6 (geen verkoopmail of P2: langer toegestaan)
- let op post-purchase/p1-first: outlook: preheader zonder mso-hide:all
- let op post-purchase/p1-first: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p1-repeat: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p1-repeat: outlook: preheader zonder mso-hide:all
- let op post-purchase/p1-repeat: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p2-safe: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p2-safe: outlook: preheader zonder mso-hide:all
- let op post-purchase/p2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p2: hoogte 4170 px op 390 px bij po_pan_us (geen verkoopmail of P2: langer toegestaan)
- let op post-purchase/p2: outlook: preheader zonder mso-hide:all
- let op post-purchase/p3-accessory-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-accessory-nocode: inbox: spamsignalen in de body: "FREE"
- let op post-purchase/p3-accessory-nocode: outlook: preheader zonder mso-hide:all
- let op post-purchase/p3-accessory-nocode: plain-text: 4 regel(s) dubbel in Klaviyo's automatische tekstversie (verborgen desk/mob-varianten), bijv. "No coating to scratch, flake or wear off."
- let op post-purchase/p3-accessory: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-accessory: outlook: preheader zonder mso-hide:all
- let op post-purchase/p3-accessory: plain-text: 4 regel(s) dubbel in Klaviyo's automatische tekstversie (verborgen desk/mob-varianten), bijv. "No coating to scratch, flake or wear off."
- let op post-purchase/p3-accessory: ruw 390 px (code-editor mobiel): tabel 495 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p3-apron-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-apron-nocode: inbox: spamsignalen in de body: "FREE" x2
- let op post-purchase/p3-apron-nocode: outlook: preheader zonder mso-hide:all
- let op post-purchase/p3-apron: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-apron: hoogte 3603 px op 390 px (max ~3600) bij po_pan_us
- let op post-purchase/p3-apron: inbox: spamsignalen in de body: "FREE"
- let op post-purchase/p3-apron: outlook: preheader zonder mso-hide:all
- let op post-purchase/p3-apron: ruw 390 px (code-editor mobiel): tabel 495 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p3-next-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-next-nocode: inbox: spamsignalen in de body: "FREE" x2
- let op post-purchase/p3-next-nocode: outlook: preheader zonder mso-hide:all
- let op post-purchase/p3-next: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-next: outlook: preheader zonder mso-hide:all
- let op post-purchase/p3-next: ruw 390 px (code-editor mobiel): tabel 495 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p3-pan-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-pan-nocode: inbox: spamsignalen in de body: "FREE" x2
- let op post-purchase/p3-pan-nocode: outlook: preheader zonder mso-hide:all
- let op post-purchase/p3-pan: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-pan: inbox: spamsignalen in de body: "FREE"
- let op post-purchase/p3-pan: outlook: preheader zonder mso-hide:all
- let op post-purchase/p3-pan: ruw 390 px (code-editor mobiel): tabel 495 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p3-set-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-set-nocode: inbox: spamsignalen in de body: "FREE" x2
- let op post-purchase/p3-set-nocode: outlook: preheader zonder mso-hide:all
- let op post-purchase/p3-set: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-set: hoogte 3602 px op 390 px (max ~3600) bij po_pan_us
- let op post-purchase/p3-set: inbox: 6 uitroeptekens in de body
- let op post-purchase/p3-set: inbox: spamsignalen in de body: "!!!" x2, "FREE"
- let op post-purchase/p3-set: outlook: preheader zonder mso-hide:all
- let op post-purchase/p3-set: plain-text: 3 regel(s) dubbel in Klaviyo's automatische tekstversie (verborgen desk/mob-varianten), bijv. "“This is the best crepe pan that I have used that works like"
- let op post-purchase/p3-set: ruw 390 px (code-editor mobiel): tabel 495 px breed door lange Django-expressies; gerenderd in orde
- let op site/a1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op site/a1: inbox: spamsignalen in de body: "FREE"
- let op site/a1: outlook: preheader zonder mso-hide:all
- let op site/a2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op site/a2: outlook: preheader zonder mso-hide:all
- let op sunset/s1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op sunset/s1: outlook: preheader zonder mso-hide:all
- let op sunset/s2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op sunset/s2: outlook: preheader zonder mso-hide:all
- let op ugc/u1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op ugc/u1: outlook: preheader zonder mso-hide:all
- let op vip/v1-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op vip/v1-nocode: inbox: spamsignalen in de body: "no cost"
- let op vip/v1-nocode: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Shop with my 10% →"
- let op vip/v1-nocode: outlook: preheader zonder mso-hide:all
- let op vip/v1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op vip/v1: inbox: spamsignalen in de body: "no cost"
- let op vip/v1: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Claim my 15% →"
- let op vip/v1: outlook: preheader zonder mso-hide:all
- let op vip/v2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op vip/v2: outlook: preheader zonder mso-hide:all
- let op welcome/w0: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w0: outlook: preheader zonder mso-hide:all
- let op welcome/w1-a: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w1-a: inbox: spamsignalen in de body: "FREE"
- let op welcome/w1-a: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Claim my 10% + gifts →"
- let op welcome/w1-a: outlook: preheader zonder mso-hide:all
- let op welcome/w1-b: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w1-b: inbox: spamsignalen in de body: "FREE", "cash"
- let op welcome/w1-b: outlook: preheader zonder mso-hide:all
- let op welcome/w2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w2: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Claim my 10% + gifts →"
- let op welcome/w2: outlook: preheader zonder mso-hide:all
- let op welcome/w3: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w3: inbox: spamsignalen in de body: "FREE"
- let op welcome/w3: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Claim my 10% + gifts →"
- let op welcome/w3: outlook: preheader zonder mso-hide:all
- let op welcome/w4-int: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w4-int: inbox: spamsignalen in de body: "FREE"
- let op welcome/w4-int: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Claim my 10% + gifts →"
- let op welcome/w4-int: outlook: preheader zonder mso-hide:all
- let op welcome/w4-us: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w4-us: inbox: spamsignalen in de body: "FREE"
- let op welcome/w4-us: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Claim my 10% + gifts →"
- let op welcome/w4-us: outlook: preheader zonder mso-hide:all
- let op welcome/w5: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w5: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Claim my 10% + gifts →"
- let op welcome/w5: outlook: preheader zonder mso-hide:all
- let op winback/r1-acc: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r1-acc: outlook: preheader zonder mso-hide:all
- let op winback/r1-acc: plain-text: 4 regel(s) dubbel in Klaviyo's automatische tekstversie (verborgen desk/mob-varianten), bijv. "Nothing to flake or wear off."
- let op winback/r1-pan: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r1-pan: inbox: spamsignalen in de body: "FREE"
- let op winback/r1-pan: outlook: preheader zonder mso-hide:all
- let op winback/r1-set: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r1-set: inbox: spamsignalen in de body: "FREE"
- let op winback/r1-set: outlook: preheader zonder mso-hide:all
- let op winback/r2-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r2-nocode: inbox: spamsignalen in de body: "FREE" x2
- let op winback/r2-nocode: outlook: preheader zonder mso-hide:all
- let op winback/r2-vip-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r2-vip-nocode: inbox: spamsignalen in de body: "FREE"
- let op winback/r2-vip-nocode: outlook: preheader zonder mso-hide:all
- let op winback/r2-vip: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r2-vip: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Claim my 15% →"
- let op winback/r2-vip: outlook: preheader zonder mso-hide:all
- let op winback/r2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r2: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% now →"
- let op winback/r2: outlook: preheader zonder mso-hide:all
- let op winback/r2: plain-text: 3 regel(s) dubbel in Klaviyo's automatische tekstversie (verborgen desk/mob-varianten), bijv. "“This is my second purchase of Siraat frying pans in just a "

Screenshots: `exports/qa/shots/<flow>-<id>-<desktop|mobile>-<rendered|raw>.jpg` (gerenderd = eerste variant).
