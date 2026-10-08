# 05 · Links in alle 61 v5-mails

Stand: 8 oktober 2026, link-agent. Aanleiding (Floris): "als ik in een e-mail op 'About' klik, ga ik naar een FAQ."

## Methode

1. Elke mail uit de v4-inventaris (61) gebouwd zoals `qa_render.py` dat doet (`build_template.py --out --no-preview`, dus header, footer, blokken en v5-macro's uitgeklapt) en met de Django-engine van de QA-poort gerenderd per markt (US, UK, AU, CA, SG, EU, onbekend) en per voorbeeldevent: alle `co_*`, `atc_*`, `vp_*` en `po_*` samples (zo komen ook de cross-sell- en bundeltakken langs), profielmails zonder event. Per anker: href, ankertekst of alt-tekst, markten waarin hij zichtbaar is. Daarnaast alle hrefs uit de ongerenderde Klaviyo-HTML (alle takken) als controle: geen pad gevonden dat niet ook gerenderd voorkwam.
2. Elke unieke bestemming gevolgd met `curl -sSIL --max-redirs 10` (Chrome-UA, Accept-Language en-US) en de HTML opgehaald voor `<title>` en `<h1>`. Kortingslinks getest als `/discount/HI10?redirect=<pad>` (de unieke coupons `{% coupon_code %}` bestaan pas bij verzending; de route is dezelfde). Belangrijke links ook met cookie `localization=US|GB|AU|CA|DE|SG|NZ`: geen landredirect, de site heeft geen submappen (`/en-gb` enz. bestaan niet), alles blijft op siraatskitchen.com met 200.
3. Facebook en Instagram: de proxy van deze omgeving weigert beide hosts (403 op CONNECT), dus niet live te volgen. Vergeleken met de links die de site zelf in header en footer gebruikt.
4. Echte Klaviyo-events bekeken (Added to Cart QXcV8K, Viewed Product XNtYMB) voor de velden achter `event.URL`.

Scripts en ruwe uitvoer (niet in git): scratchpad `links/inv.py`, `links/check.py`, `links/res.json`.

## Tabel per unieke bestemming

Status = eindstatus na redirects (302 -> 200 = kortingsroute). Titel | h1 van de eindpagina. Mails = aantal mails waarin de link voorkomt.

| Bestemming | Tekst in de mail (voorbeelden) | Mails | Markten | Status | Titel / h1 | Oordeel |
|---|---|---|---|---|---|---|
| `/pages/faq` (header) | ABOUT | 61 | alle | 200 | FAQs – Find Your Answers Quickly / Frequently Asked Questions | **FOUT**, aangepast naar `/pages/about-us` |
| `/pages/about-us` (nieuw) | ABOUT | 61 | alle | 200 | Learn More About Siraats Kitchen – Our Story & Values | Goed: de site noemt dit zelf "ABOUT US" en "Our Story"; Benjamin, 30-day returns, 75-year guarantee |
| `https://siraatskitchen.com/` | logo (alt "Siraat"), "Keep me on the list" (sunset) | 61 | alle | 200 | Titanium Cookware Set ... | Goed |
| `/collections/pans` | COOKWARE, TITANIUM COOKWARE, My first titanium pan, Show me the pans | 61 | alle | 200 | Titanium Pan Collection | Goed |
| `/collections/bundles` | SETS, BUNDLES & SETS, A full set, pans and lids | 61 | alle | 200 | Bundles | Goed |
| `/collections/accessories` | ACCESSORIES | 61 | alle | 200 | Accessories | Goed |
| `/collections/all` | Shop with my 4 gifts, See what fits my pan/set | 7 (+ via korting 9) | alle | 200 | All Products | Goed |
| `/pages/third-party-testing` | LAB RESULTS, Read report no. 25895, beeld "Light Labs Certificate of Analysis" | 61 | alle | 200 | Third Party Testing | Goed (pagina laadt de Light Labs-widget `company-id=415 product-id=2231`); rapportnummer 25895 niet in de HTML te zien, zie vragen |
| `/pages/care-use` | Watch the chef video, Watch the cook guide, Read the care guide | 5 (p1-repeat, p2, p2-safe, u1, w0) | alle | 200 | Care & Use / Care for your Siraat | Goed: bevat de video "how to make an egg slide straight off" (2:33) |
| `/pages/warranty` | What the warranty covers (k2-new) | 1 | alle | 200 | Warranty | Link klopt, **inhoud van de pagina niet**: "lifetime warranty" i.p.v. 75 jaar (zie vragen) |
| `/products/e` | Download your e-book | 2 (p1-first, p1-repeat) | alle | 200 | The Green Clean E-Guide | Goed volgens DECISIONS (7 okt); het is een productpagina, geen download |
| `/products/e-gift-card` | A gift for someone who cooks (s3-kept) | 1 | alle | 200 | Siraats Kitchen Gift Card / E-Gift Card | Goed |
| `/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern` | Pan Pro 28 cm / 11″, Claim my 10% + gifts | 36 | alle | 200 | Titanium Hammered Pan Pro Standard | Goed (28 cm = Standard) |
| `/products/titanium-hammered-pan-pro-mini` | Pan Pro Mini 20 cm / 8″ | 25 | alle | 200 | Titanium Hammered Pan Pro Mini | Goed |
| `/products/titanium-hammered-pan-pro-small` | Pan Pro Small 26 cm / 10″ | 25 | alle | 200 | Titanium Hammered Pan Pro Small | Goed |
| `/products/titanium-hammered-pan-pro-large` | Pan Pro Large 30 cm / 12″ | 25 | alle | 200 | Titanium Hammered Pan Pro Large | Goed |
| `/products/titanium-hammered-deep-pan-pro` | Deep Pan Pro | 23 | alle | 200 | Titanium Hammered Deep Pan Pro | Goed |
| `/products/titanium-hammered-wok-pan-pro` | Wok Pan Pro | 22 | alle | 200 | Titanium Hammered Wok Pan Pro | Goed |
| `/products/titanium-hammered-crepe-pan-pro` | Crêpe Pan Pro | 22 | alle | 200 | Titanium Hammered Crêpe Pan Pro | Goed |
| `/products/titanium-hammered-pan-set-with-lids-6-pcs` | The 6-piece set, Buy 2, get 4 free, FALL SALE | 27 | alle | 200 | Titanium Hammered Pan Set With Lids \| 6-Pcs | Goed: de $299-hoofdlisting (Viewed Product-event toont $299, compare-at $598). De $349-listing komt in geen enkele tak meer voor |
| `/products/titanium-hammered-cookware-set` | The 12-piece set (w4-us) | 1 | alleen US | 200 | Titanium Hammered Cookware Set \| 12-Pcs | Goed: US-only product alleen in de US-tak |
| `/products/stainless-steel-lid?variant=53294486421844` | Stainless Steel Lid, 20 cm / Add the 20 cm lid | 12+ | alle | 200 | Stainless Steel Lid | Goed: variant = "Mini 20CM" |
| `...?variant=52401107206484` | 26 cm lid | 12+ | alle | 200 | Stainless Steel Lid | Goed: "Small (10")" |
| `...?variant=52401107239252` | 28 cm lid | 12+ | alle | 200 | Stainless Steel Lid | Goed: "Standard (11")" |
| `...?variant=52401107272020` | 30 cm lid | 12+ | alle | 200 | Stainless Steel Lid | Goed: "Large (12")" |
| `/products/stainless-steel-lid` (zonder variant) | "Sized to your pan: 20, 26, 28 or 30 cm" (k2-returning), "The lid that fits: match it to your pan's diameter" (p3-pan), "The stainless steel lid for your pan" (w0) | 3 | alle | 200 | Stainless Steel Lid | Goed: de tekst noemt geen maat, dus geen variant nodig (zie suggestie) |
| `/products/titanium-cutting-board-v2` | Titanium Cutting Board | 22 | alle | 200 | Titanium Cutting Board (Anti-Microbial) | Goed |
| `/products/siraat-pure-titanium-utensils-bundle` | Titanium Utensil Set | 22 | alle | 200 | Titanium Utensil Set Bundle | Goed |
| `/products/siraat-signature-apron-moss` | Siraat Signature Apron | 22 | alle | 200 | Siraat Signature Apron (Moss) | Goed (één kleur als landingsvariant) |
| `/products/salt-pepper-mill-set` | Salt & Pepper Mill Set | 22 | alle | 200 | Salt & Pepper Mill Set | Goed |
| `/discount/HI10?redirect=<pad>` | Claim my 10% + gifts, Get 10% off my pan, Shop with my 10%, cross-sell-rijen | 14 (a1, a2, b1, b1-acc, b2-notclicked, c3-acc, c3-p, n1, r1-*, w4-*) | alle | 302 -> 200 | zelfde als het pad | Goed: elke redirect naar /products, /collections/all, /collections/pans landt op 200 met UTM erachter |
| `/discount/{% coupon_code 'X' %}?redirect=<pad>` | Use my 10% now, Get my 15% now, Add the lid, 10% off | 17 (b2-clicked, k3, n2, p3-*, r2, r2-vip, v1) | alle | 302 -> 200 | zelfde als het pad | Goed (route getest met HI10) |
| `{{ event.extra.responsive_checkout_url }}&discount=HI10` | Complete my order, Keep my one pan and check out | 6 (c1, c2, c2-acc, c3-acc, c3-p, c3-s) | alle | n.v.t. (per klant) | Shopify recover-URL | Goed: Klaviyo-variabele, niet hardcoded |
| `{{ event.extra.responsive_checkout_url }}&discount={% coupon_code 'C4_10_48H' %}` | Use my 10% now (c4) | 1 | alle | n.v.t. | idem | Goed |
| `{{ event.extra.responsive_checkout_url }}` | Complete my order (c4-nocode) | 1 | alle | n.v.t. | idem | Goed |
| `https://siraatskitchen.com{{ event.URL|cut:... }}` | Finish my order, productregel, hero (k1, k1-acc, k2-*, k3-nocode, b1, b2-*) | 11 | alle | n.v.t. | PDP van het product uit het event | Goed: event-variabele; Added to Cart-URL is het myshopify-domein en wordt eraf geknipt, Viewed Product gebruikt siraatskitchen.com |
| `/cart` | alleen als terugval als `event.URL` leeg is | (5) | alle | 200 | Your Shopping Cart | Terugval, zie suggestie cart-permalink |
| `https://www.facebook.com/siraatskitchen` | Facebook-icoon (footer) | 61 | alle | proxy 403 | niet te volgen | **Aangepast** naar de URL die de site zelf gebruikt |
| `https://www.facebook.com/people/SiraatsKitchen/61567176126958/` (nieuw) | Facebook-icoon | 61 | alle | proxy 403 | niet te volgen | Gelijk aan header en footer van siraatskitchen.com |
| `https://www.instagram.com/siraatskitchen` | Instagram-icoon | 61 | alle | proxy 403 | niet te volgen | Goed: zelfde account als op de site (`instagram.com/siraatskitchen`) |
| `mailto:support@siraatskitchen.com` | support@siraatskitchen.com (s2) | 1 | alle | n.v.t. | | Goed (adres aanwezig) |
| `mailto:support@siraatskitchen.com?subject=My first egg` | Send my photo (u1) | 1 | alle | n.v.t. | | Goed |
| `{% unsubscribe 'Unsubscribe' %}`, `{% unsubscribe_link %}` | Unsubscribe, Unsubscribe in one tap (s1, s2, s3-kept) | 61 | alle | Klaviyo | | Goed: Klaviyo-tags |
| `{% manage_preferences_link %}` | Manage preferences, Choose fewer emails | 61 | alle | Klaviyo | | Goed |
| `{% web_view 'View in browser' %}` | View in browser | 61 | alle | Klaviyo | | Goed |

Overige controles over alle 61 mails en alle takken:
- Geen `http://`, geen lege href, geen `href="#"`, geen `mailto:` zonder adres in de Klaviyo-HTML (lege hrefs in de testrender zijn de stub van de testengine voor Klaviyo's unsubscribe/web_view-tags).
- Geen 404 en geen redirectketen langer dan 1 stap (alleen de bedoelde 302 van `/discount/`). Eén 503 bij een herhaalde test was tijdelijk (3 x opnieuw 200).
- UTM: elke siraatskitchen.com-link heeft utm_source, utm_medium, utm_campaign en utm_content, bij kortingslinks binnen de `redirect`. utm_campaign per flow (v4-checkout, v4-cart ...), utm_content-prefix per mail uniek, behalve de A/B-paren k3/k3-nocode en b2-clicked/b2-clicked-nocode: die delen bewust het prefix en verschillen in utm_term (t02-a/t02-b). Header en footer kregen die utm_term niet (zie aanpassing 3).
- US-only producten (12-delige set, potten, 2 pans + 2 lids, 34-delig) komen in geen enkele niet-US-tak als link voor.
- Lid-varianten passen bij de genoemde maat in alle mails (automatisch vergeleken: 0 afwijkingen).

## Gevonden fouten

1. **Header ABOUT -> /pages/faq** (alle 61 mails, alle markten). Bron: `klaviyo/templates/partials/header.html`. De site zelf heeft "ABOUT US" en "Our Story" op `/pages/about-us`; de FAQ heeft een eigen menupunt.
2. **Facebook-icoon naar `facebook.com/siraatskitchen`**, terwijl de site naar `facebook.com/people/SiraatsKitchen/61567176126958/` linkt. Niet te controleren of de korte naam van Siraat is; de site is leidend.
3. **utm_term ontbrak op header/footer** in k3-nocode en b2-clicked-nocode (en de codevarianten): de clicks op logo, nav en footer van de A/B-takken waren in de analytics niet te onderscheiden.
4. Geen fout in de mail, wel in de bestemming: `/pages/warranty` zegt "lifetime warranty". De mail (k2-new, "What the warranty covers") en DECISIONS zeggen 75 jaar.

## Aanpassingen (bron)

| Bestand | Oud | Nieuw |
|---|---|---|
| `klaviyo/templates/partials/header.html` | `<a href="https://siraatskitchen.com/pages/faq" ...>ABOUT</a>` | `<a href="https://siraatskitchen.com/pages/about-us" ...>ABOUT</a>` (UTM wordt `utm_content=<mail>-nav-about-us`) |
| `klaviyo/templates/partials/footer.html` | `https://www.facebook.com/siraatskitchen` | `https://www.facebook.com/people/SiraatsKitchen/61567176126958/` |
| `scripts/build_template.py` (`add_utm`) | header/footer-UTM zonder utm_term | als de mail precies één utm_term gebruikt, krijgen header en footer dezelfde `&utm_term=` (k3: t02-a, k3-nocode: t02-b, idem b2-clicked) |

Daarna `python3 -I scripts/qa_render.py` (alle mails, alle markten, met browser): **61 mails, 61 groen, 0 met FOUT** (`exports/qa/render-report.md`). Opnieuw geïnventariseerd: ABOUT -> /pages/about-us en het nieuwe Facebook-adres in alle 61 mails. Niets geëxporteerd naar Klaviyo, niets gecommit. De lokale `*.klaviyo.html` en previews zijn niet opnieuw gebouwd; `export_klaviyo.py` bouwt ze bij de export opnieuw uit de bron.

## Wat ik niet zeker weet (vragen aan Floris)

1. **About-pagina**: ik heb `/pages/about-us` gekozen (site-menu "ABOUT US" en footer "Our Story", met Benjamin als Founder). Alternatieven op de site: `/pages/our-production` en `/pages/benjamin-lander` (dat laatste is een advertorial "10 Shocking Reasons...", niet geschikt). Akkoord?
2. **Warranty-pagina** zegt "lifetime warranty against manufacturing defects"; alle mails zeggen 75 jaar. Pagina aanpassen, of k2-new laten linken naar `/policies/refund-policy` (die noemt de 75 jaar wel)? Ook `/pages/about-us` zegt nog "made to last a lifetime".
3. **Facebook**: is `facebook.com/people/SiraatsKitchen/61567176126958/` de juiste pagina (dat is wat de site gebruikt)? Bestaat er een korte gebruikersnaam (bv. facebook.com/siraatskitchen) die van Siraat is? Instagram `siraatskitchen` klopt met de site.
4. **Light Labs**: `/pages/third-party-testing` toont een Light Labs-widget (product-id 2231). Ik kon niet zien of dat rapport 25895 is (widget laadt via JavaScript). Graag één keer in de browser bevestigen, of een directe link naar rapport 25895 geven.
5. **E-book**: "Download your e-book" gaat naar `/products/e` (productpagina, DECISIONS 7 okt). Is er een echte downloadlink (of komt de download via de orderbevestiging)? Anders de knoptekst "Get your e-book" overwegen.

## Suggesties (niet aangepast)

- **Cart-knop over apparaten heen**: K-mails sturen "Finish my order" naar de PDP uit `event.URL` (werkt op elk apparaat, maar is geen winkelwagen). Het echte Added to Cart-event bevat `VariantID` en `Quantity`; `https://siraatskitchen.com/cart/{{ event.VariantID }}:{{ event.Quantity }}?storefront=true` getest: opent de cart met het product (302 -> /cart). Nadeel: een permalink vervangt de bestaande cart door dat ene product. Keuze voor Floris.
- **p3-pan "Add the lid, 10% off"**: nu de algemene dekselpagina; kan per pan uit de order naar de juiste variant (Mini/Small/Standard/Large), zoals de cross-sell al doet.
- **Terugval in checkoutmails**: als `responsive_checkout_url` ooit leeg is, wordt de link `/discount/HI10?redirect=/cart&discount=HI10&utm_...` (UTM buiten de redirect). Werkt, maar de UTM gaat verloren; zeldzaam (01-markten: checkout-URL 100 procent gevuld).
- `scripts/mail_checks.py` (inbox-QA) kent de regel "about -> /pages/about" al; die slaagt nu.
