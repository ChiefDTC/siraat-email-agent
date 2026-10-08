# QA-render rapport

Gegenereerd door `scripts/qa_render.py`. 61 mails: **61 groen**, 0 met FOUT, 61 met waarschuwing.

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
| `lookup` | Klaviyo | 35 |
| `lower` | Django | 29 |
| `upper` | Django | 12 |

## Per mail

| mail | status | varianten | hoogte 390 px | zichtbare `{%`/`{{` in ruwe weergave | v5-marktpunten (US, UK, AU, CA, SG, EU, onbekend) |
|---|---|---|---|---|---|
| anniversary/n1 | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3076 | 4 | 0 |
| anniversary/n2-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3010 | 4 | 0 |
| anniversary/n2 | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3505 | 11 | 0 |
| browse/b1-acc | let op | vp_pan, vp_set6, vp_apron | 2915 | 6 | 0 |
| browse/b1 | let op | vp_pan, vp_set6, vp_apron | 2879 | 7 | 0 |
| browse/b2-clicked-nocode | let op | vp_pan, vp_set6, vp_apron | 2942 | 8 | 0 |
| browse/b2-clicked | let op | vp_pan, vp_set6, vp_apron | 3443 | 15 | 0 |
| browse/b2-notclicked | let op | vp_pan, vp_set6, vp_apron | 3321 | 6 | 0 |
| cart/k1-acc | let op | atc_pan, atc_apron, atc_lid_eur | 3129 | 6 | 0 |
| cart/k1 | let op | atc_pan, atc_apron, atc_lid_eur | 3420 | 6 | 0 |
| cart/k2-new | let op | atc_pan, atc_apron, atc_lid_eur | 3035 | 6 | 0 |
| cart/k2-returning | let op | atc_pan, atc_apron, atc_lid_eur | 3085 | 7 | 0 |
| cart/k3-nocode | let op | atc_pan, atc_apron, atc_lid_eur | 3011 | 6 | 0 |
| cart/k3 | let op | atc_pan, atc_apron, atc_lid_eur | 3565 | 14 | 0 |
| checkout/c1 | let op | co_pan, co_set6, co_apron, co_pan_eur | 3494 | 7 | 0 |
| checkout/c2-acc | let op | co_pan, co_set6, co_apron, co_pan_eur | 3313 | 7 | 0 |
| checkout/c2 | let op | co_pan, co_set6, co_apron, co_pan_eur | 3193 | 7 | 0 |
| checkout/c3-acc | let op | co_pan, co_set6, co_apron, co_pan_eur | 2948 | 7 | 0 |
| checkout/c3-p | let op | co_pan, co_set6, co_apron, co_pan_eur | 3138 | 7 | 0 |
| checkout/c3-s | let op | co_pan, co_set6, co_apron, co_pan_eur | 2918 | 7 | 0 |
| checkout/c4-nocode | let op | co_pan, co_set6, co_apron, co_pan_eur | 3126 | 7 | 0 |
| checkout/c4 | let op | co_pan, co_set6, co_apron, co_pan_eur | 3552 | 15 | 0 |
| post-purchase/p1-first | let op | po_pan_us, po_set6, po_apron_us, po_deep | 4014 | 8 | 0 |
| post-purchase/p1-repeat | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3077 | 8 | 0 |
| post-purchase/p2-safe | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3854 | 4 | 0 |
| post-purchase/p2 | let op | po_pan_us, po_set6, po_apron_us, po_deep | 4186 | 4 | 0 |
| post-purchase/p3-accessory-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 2977 | 4 | 0 |
| post-purchase/p3-accessory | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3473 | 11 | 0 |
| post-purchase/p3-apron-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 2903 | 4 | 0 |
| post-purchase/p3-apron | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3472 | 11 | 0 |
| post-purchase/p3-next-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3024 | 4 | 0 |
| post-purchase/p3-next | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3520 | 11 | 0 |
| post-purchase/p3-pan-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3003 | 4 | 0 |
| post-purchase/p3-pan | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3548 | 11 | 0 |
| post-purchase/p3-set-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3024 | 4 | 0 |
| post-purchase/p3-set | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3545 | 11 | 0 |
| site/a1 | let op | none | 3094 | 4 | 0 |
| site/a2 | let op | none | 2915 | 4 | 0 |
| sunset/s1 | let op | none | 1816 | 4 | 0 |
| sunset/s2 | let op | none | 1499 | 4 | 0 |
| sunset/s3-kept | let op | none | 1790 | 4 | 0 |
| sunset/s4-kept | let op | none | 1657 | 4 | 0 |
| ugc/u1 | let op | none | 3088 | 4 | 0 |
| vip/v1-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep, po_pan_us+pool | 3061 | 4 | 0 |
| vip/v1 | let op | po_pan_us, po_set6, po_apron_us, po_deep, po_pan_us+pool | 3581 | 11 | 0 |
| vip/v2 | let op | po_pan_us, po_set6, po_apron_us, po_deep, po_pan_us+pool | 1389 | 4 | 0 |
| welcome/w0 | let op | none | 3332 | 4 | 0 |
| welcome/w1-a | let op | none | 3484 | 3 | 0 |
| welcome/w1-b | let op | none | 3406 | 3 | 0 |
| welcome/w2 | let op | none | 2597 | 4 | 0 |
| welcome/w3 | let op | none | 3533 | 4 | 0 |
| welcome/w4-int | let op | none | 3103 | 4 | 0 |
| welcome/w4-us | let op | none | 3082 | 4 | 0 |
| welcome/w5 | let op | none | 3531 | 3 | 0 |
| winback/r1-acc | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3460 | 4 | 0 |
| winback/r1-pan | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3021 | 4 | 0 |
| winback/r1-set | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3046 | 4 | 0 |
| winback/r2-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3186 | 4 | 0 |
| winback/r2-vip-nocode | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3207 | 4 | 0 |
| winback/r2-vip | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3577 | 13 | 0 |
| winback/r2 | let op | po_pan_us, po_set6, po_apron_us, po_deep | 3526 | 13 | 0 |

## Fouten en waarschuwingen

- let op anniversary/n1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op anniversary/n2-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op anniversary/n2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op anniversary/n2: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Get my 15% now →"
- let op browse/b1-acc: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op browse/b1-acc: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b1-acc: outlook: preheader zonder mso-hide:all
- let op browse/b1-acc: ruw 390 px (code-editor mobiel): tabel 464 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op browse/b1: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b1: outlook: preheader zonder mso-hide:all
- let op browse/b1: ruw 390 px (code-editor mobiel): tabel 575 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b2-clicked-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op browse/b2-clicked-nocode: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-clicked-nocode: outlook: preheader zonder mso-hide:all
- let op browse/b2-clicked-nocode: ruw 390 px (code-editor mobiel): tabel 575 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b2-clicked: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op browse/b2-clicked: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-clicked: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% now →"
- let op browse/b2-clicked: outlook: preheader zonder mso-hide:all
- let op browse/b2-clicked: ruw 390 px (code-editor mobiel): tabel 494 px breed door lange Django-expressies; gerenderd in orde
- let op browse/b2-notclicked: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op browse/b2-notclicked: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op browse/b2-notclicked: outlook: preheader zonder mso-hide:all
- let op browse/b2-notclicked: ruw 390 px (code-editor mobiel): tabel 575 px breed door lange Django-expressies; gerenderd in orde
- let op cart/k1-acc: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op cart/k1-acc: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k1-acc: ruw 390 px (code-editor mobiel): tabel 409 px breed door lange Django-expressies; gerenderd in orde
- let op cart/k1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op cart/k1: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k1: plain-text: 4 regel(s) dubbel in Klaviyo's automatische tekstversie (verborgen desk/mob-varianten), bijv. "No coating, so nothing to scrub around."
- let op cart/k2-new: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op cart/k2-new: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k2-returning: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op cart/k2-returning: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k2-returning: ruw 390 px (code-editor mobiel): tabel 484 px breed door lange Django-expressies; gerenderd in orde
- let op cart/k3-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op cart/k3-nocode: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k3: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op cart/k3: filter |cut: Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.
- let op cart/k3: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% now →"
- let op cart/k3: ruw 390 px (code-editor mobiel): tabel 395 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c1: inbox: 3 uitroeptekens in de body
- let op checkout/c1: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c2-acc: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c2-acc: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c2: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c3-acc: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c3-acc: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c3-p: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c3-p: inbox: spamsignalen in de body: "FREE"
- let op checkout/c3-p: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c3-s: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c3-s: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c4-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c4-nocode: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op checkout/c4: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op checkout/c4: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% now →"
- let op checkout/c4: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p1-first: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p1-first: hoogte 4014 px op 390 px bij po_pan_us (geen verkoopmail of P2: langer toegestaan)
- let op post-purchase/p1-first: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p1-repeat: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p1-repeat: inbox: 3 uitroeptekens in de body
- let op post-purchase/p1-repeat: ruw 390 px (code-editor mobiel): tabel 564 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p2-safe: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p2-safe: hoogte 3854 px op 390 px bij po_pan_us (geen verkoopmail of P2: langer toegestaan)
- let op post-purchase/p2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p2: hoogte 4186 px op 390 px bij po_pan_us (geen verkoopmail of P2: langer toegestaan)
- let op post-purchase/p3-accessory-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-accessory: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-accessory: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% code →"
- let op post-purchase/p3-accessory: ruw 390 px (code-editor mobiel): tabel 515 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p3-apron-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-apron: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-apron: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% code →"
- let op post-purchase/p3-apron: ruw 390 px (code-editor mobiel): tabel 515 px breed door lange Django-expressies; gerenderd in orde
- let op post-purchase/p3-next-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-next: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-next: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% code →"
- let op post-purchase/p3-pan-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-pan: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-pan: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% code →"
- let op post-purchase/p3-set-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-set: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op post-purchase/p3-set: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% code →"
- let op site/a1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op site/a1: outlook: preheader zonder mso-hide:all
- let op site/a2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op site/a2: outlook: preheader zonder mso-hide:all
- let op site/a2: ruw 390 px (code-editor mobiel): tabel 557 px breed door lange Django-expressies; gerenderd in orde
- let op sunset/s1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op sunset/s2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op sunset/s3-kept: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op sunset/s4-kept: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op ugc/u1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op vip/v1-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op vip/v1: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op vip/v1: inbox: spamsignalen in de body: "Get it now"
- let op vip/v1: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Get my 15% now →"
- let op vip/v2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w0: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w0: outlook: preheader zonder mso-hide:all
- let op welcome/w1-a: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w1-a: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Claim my 10% + gifts →"
- let op welcome/w1-a: outlook: preheader zonder mso-hide:all
- let op welcome/w1-a: ruw 390 px (code-editor mobiel): tabel 508 px breed door lange Django-expressies; gerenderd in orde
- let op welcome/w1-b: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w1-b: outlook: preheader zonder mso-hide:all
- let op welcome/w1-b: ruw 390 px (code-editor mobiel): tabel 456 px breed door lange Django-expressies; gerenderd in orde
- let op welcome/w2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w2: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Claim my 10% + gifts →"
- let op welcome/w2: outlook: preheader zonder mso-hide:all
- let op welcome/w3: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w3: outlook: preheader zonder mso-hide:all
- let op welcome/w4-int: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w4-int: outlook: preheader zonder mso-hide:all
- let op welcome/w4-int: ruw 390 px (code-editor mobiel): tabel 551 px breed door lange Django-expressies; gerenderd in orde
- let op welcome/w4-us: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w4-us: outlook: preheader zonder mso-hide:all
- let op welcome/w4-us: ruw 390 px (code-editor mobiel): tabel 551 px breed door lange Django-expressies; gerenderd in orde
- let op welcome/w5: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op welcome/w5: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Claim my 10% + gifts →"
- let op welcome/w5: outlook: preheader zonder mso-hide:all
- let op welcome/w5: ruw 390 px (code-editor mobiel): tabel 508 px breed door lange Django-expressies; gerenderd in orde
- let op winback/r1-acc: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r1-acc: ruw 390 px (code-editor mobiel): tabel 515 px breed door lange Django-expressies; gerenderd in orde
- let op winback/r1-pan: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r1-set: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r2-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r2-vip-nocode: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r2-vip: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r2-vip: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Get my 15% now →"
- let op winback/r2-vip: ruw 390 px (code-editor mobiel): tabel 395 px breed door lange Django-expressies; gerenderd in orde
- let op winback/r2: dark mode: logo-black.png is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)
- let op winback/r2: outlook: 1 knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar): "Use my 10% now →"
- let op winback/r2: ruw 390 px (code-editor mobiel): tabel 395 px breed door lange Django-expressies; gerenderd in orde

Screenshots: `exports/qa/shots/<flow>-<id>-<desktop|mobile>-<rendered|raw>.jpg` (gerenderd = eerste variant).
