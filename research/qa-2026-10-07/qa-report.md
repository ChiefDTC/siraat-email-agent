# QA- en deliverability-rapport · Flow System v3 (31 mails)

Datum: 7 oktober 2026 · Account TdtTzz · Bron: `klaviyo/templates/v3/*` (bron + preview), `partials/`, `scripts/build_template.py`.
Methode: metingen met Python/PIL en ImageMagick, rendering met Playwright (Chromium, 390 px, met en zonder media queries), Klaviyo API (alleen GET: metrics, events, coupons, accounts), Shopify Admin API (alleen lezen: producten, collecties, pagina's, kortingscode HI10).
Niets gewijzigd in `klaviyo/templates` of `scripts`; voorstellen staan als patch in `patches/`.

Beperking: siraatskitchen.com is in deze container geblokkeerd door de proxy (CONNECT 403). Links zijn daarom gecontroleerd via de Shopify Admin API (bestaat het product, de collectie of de pagina, en is het gepubliceerd). De redirect van `/discount/CODE?redirect=` zelf is niet live getest.

---

## 1. Samenvatting

De HTML is klein genoeg (geen Gmail-clipping), alle mails hebben lang-attribuut, role=presentation op elke tabel, alt-teksten, preheader gelijk aan PREVIEW, footer met uitschrijven, voorkeuren en adres, en geen em dash. De grote risico's zitten in de **dynamische data** en in **ontbrekende Klaviyo-objecten**:

1. **Geen enkele coupon bestaat in Klaviyo** (`GET /api/coupons` geeft 0). Zeven codes worden gebruikt in 10 mails. Zonder coupon rendert de mail niet en slaat Klaviyo de verzending over.
2. **W5 bevat `{% coupon_code 'W5_10_72H' %}` in de HTML-comment bovenaan.** Klaviyo rendert tags ook in comments: elke W5 faalt (coupon bestaat niet) of deelt ongemerkt een code uit.
3. **Cart-blok toont gratis gifts in plaats van de pan.** In 100 echte Checkout Started-events staan in 60 gevallen gift-regels van $0 in de eerste drie plekken, en in **40 van de 100 valt het betaalde product helemaal buiten de getoonde drie**. De klant ziet dan "Mystery Gift $0.00 · Plastic-Free Home E-Book $0.00 · PFAS Water **Purifier** Giveaway $0.00" (verboden woord). Geldt voor C1 t/m C4 en P1 (Placed Order heeft dezelfde volgorde).
4. **`/collections/cookware` bestaat niet** (geen collectie, geen redirect). Zit in header en footer: 2 dode links in alle 31 mails.
5. **$349 voor de 6-delige set linkt in P3-accessory, R2 en R2-VIP naar het product van $399** (`...-6-pcs`). Alleen `...-6-pcs-bday-sale` (unlisted) kost $349.

---

## 2. Bevindingen per controlegebied

### 2.1 Grootte (Gmail-clip, beeldgewicht)

- **HTML**: preview 10,5 tot 27,5 KB. Geschat met CDN-URL's van 90 tekens: max 28,5 KB (W4-US). Proefbouw van de Klaviyo-versie met nep-CDN-URL's: C1 24,4 KB, K1 25,1 KB, P1-first 26,5 KB. Klaviyo's klik-tracking voegt circa 3 KB toe (20 tot 34 links). **Ruim onder 102 KB, geen clipping-risico.**
- Besparing HTML: interne comments circa 1,1 tot 1,5 KB per mail (waaronder de metadata-comment voor de DOCTYPE met couponnamen en segmentlogica, zichtbaar in de bron voor ontvangers). CSS is 1,7 KB, dedupliceren levert vrijwel niets op. Patch 06 stript comments in de Klaviyo-versie.
- **Beeldgewicht** (statische beelden, zonder dynamische productfoto's):
  - Boven 1 MB: **P2 1824 KB** (twee GIF's 887 + 762 KB), **W0 1474 KB** (GIF's 576 + 762 KB), **C2 1437 KB** (GIF 765 KB, plus anatomy desktop 191 KB en mobiel 194 KB die allebei laden).
  - Hero boven 250 KB: **W3 317 KB**. Grens: W5 241, R1-pan 242, W4-US 229 KB.
  - Losse GIF's allemaal onder 1 MB (grootste oil-shimmer 887 KB).
- **Dynamische beelden (groot probleem)**: het cart-blok gebruikt `item.product.images.0.src`, het origineel van Shopify: 2048 tot 3000 px, gemeten **321 KB (Pan Pro) en 460 KB (12-delige set)** per stuk, getoond op 88 px. Met drie regels kan dat 1 MB extra zijn. Het event bevat ook `thumb_src` (240 px, 3 tot 11 KB). Added to Cart `ImageURL` (K1 t/m K3) is ook het origineel; met `&width=200` wordt het circa 10 KB (getest op cdn.shopify.com). Shopify levert aan clients zonder WebP-ondersteuning automatisch JPEG (getest), dus de .webp-extensie is geen Outlook-probleem.

**Compressietest (PIL, SSIM op luminantie):**

| Ingreep | Resultaat |
| --- | --- |
| Hero's naar JPEG q82 progressive | -7 % (7532 naar 6956 KB totaal), SSIM >= 0,996: visueel identiek |
| Hero's naar q78 progressive | -14 % (naar 6479 KB), SSIM 0,985 tot 0,995: op foto's niet te zien, controleer de kopregel in de hero op randjes |
| W3-hero | 317 naar 291 KB (q82) of 270 KB (q78). Onder 250 KB alleen met q74 of een iets kleinere uitsnede |
| GIF elke tweede frame weg (vertraging x2), 128 kleuren | egg-slide 764 naar 355 KB, water-test 575 naar 287 KB, oil-shimmer 887 naar 435 KB (circa -50 %). Beeld per frame gelijk, beweging iets schokkeriger (3,5 in plaats van 7 fps) |
| GIF alleen minder kleuren (64, fuzz 5 %) | slechts -20 %, met zichtbare banding: niet aanbevolen |

Na GIF-halvering en hero q80: P2 circa 990 KB, W0 circa 800 KB, C2 circa 1030 KB (C2 onder 1 MB als de anatomy-beelden ook naar q78 gaan, -65 KB). Kleinigheid: in C2 staat egg-slide (480 px breed) op `max-width:512px` en wordt dus licht opgeschaald.

### 2.2 Klaviyo-syntax en event-velden

Alle `{% if %}`/`{% for %}` zijn in balans in alle 31 bronnen. Filters `default`, `lookup:'Product Name'`, `cut`, `floatformat` zijn geldige Klaviyo-filters. Gecontroleerd tegen echte events (7 oktober 2026):

| Trigger (metric) | Veld in template | Echte data | Oordeel |
| --- | --- | --- | --- |
| Checkout Started (RfMvni, Shopify) | `event.extra.responsive_checkout_url` + `&discount=` | `https://siraatskitchen.com/90708771156/checkouts/ac/.../recover?key=...&locale=en-US` | OK, heeft al `?`, dus `&discount=` klopt |
| idem | `event.extra.line_items`, `item.title`, `item.quantity` (1.0), `item.line_price` (69.0) | aanwezig, getallen | OK met floatformat |
| idem | `item.product.images.0.src` | origineel 2048 tot 3000 px | **te zwaar**, gebruik `thumb_src` |
| idem | volgorde regels | gifts van $0 vaak eerst; 55 % heeft meer dan 3 regels | **probleem A3** |
| idem | `$` voor prijzen | `line_price` is shopvaluta (USD); 13 van 100 checkouts in SGD, CAD, GBP, LBP | klant ziet USD terwijl hij in eigen valuta afrekende |
| Added to Cart (QXcV8K, Shopify) | `event|lookup:'Product Name'`, `ImageURL`, `Price` (134.0), `Quantity` (1.0) | aanwezig; Price is getal | OK. `URL` wijst naar `2d0add-d6.myshopify.com`, maar de K-mails gebruiken `/cart`, dus geen effect |
| Viewed Product (XNtYMB, API) | `event.Name`, `ImageURL` (`_grande.webp`, 600 px), `Price`, `URL` | Price is tekst incl. valuta: "$134", maar ook "Dhs. 500.00" | OK (template zet geen extra $), buiten de VS staat een vreemde valuta naast $-prijzen elders in de mail |
| idem | `event.URL|cut:'https://siraatskitchen.com'` | URL op siraatskitchen.com | OK. Let op: er bestaan ook Viewed Product-metrics van Elevar, TrackBee en Triple Whale; bouw de browse-flow op XNtYMB |
| Placed Order (RSNxYV) | `event.extra.order_number` | 107762, terwijl Shopify het order "#SIRAAT107762" noemt (`event.extra.name`) | klant ziet een ander ordernummer dan in de Shopify-bevestiging |
| idem | line items in P1 | zelfde gift-regels eerst als bij checkout | **probleem A3** |
| Coupons | `{% coupon_code 'C4_10_48H' %}` enz. | `GET /api/coupons`: **0 coupons** | **kritiek A1** |
| Account | `organization.full_address`, `organization.name` | adres gevuld (2803 Philadelphia Pike, Claymont DE); naam "SIRAATSKITCHEN" | adres OK, naam lelijk in footer |

Render-endpoint: niet gebruikt. De v3-templates bestaan nog niet in Klaviyo; renderen zou eerst een template aanmaken.

Onzeker, controleren in Klaviyo-preview: of een coupon_code-tag die 4 tot 11 keer in één mail staat (P3: 11 keer per mail, in links en tekst) overal dezelfde code toont. Volgens de Klaviyo-documentatie wel; even verifiëren met een testprofiel zodra de coupons bestaan.

### 2.3 Links

Alle 49 unieke hrefs verzameld. Via Shopify Admin API gecontroleerd:

| Link | Status |
| --- | --- |
| `/collections/cookware` (header + footer, alle 31) | **bestaat niet, geen redirect: 404** |
| `/collections/bundles`, `/collections/accessories`, `/collections/all` | OK |
| `/pages/faq`, `/pages/care-use`, `/pages/warranty`, `/pages/third-party-testing` | OK, gepubliceerd |
| `/products/e` | OK, maar dit is "The Green Clean E-Guide" **voor $50** (compare-at $80). P1 zegt "Download your e-book": klant komt op een betaalpagina. Gratis variant bestaat: `/products/the-green-e-guide-free` ($0) |
| 16 productpaden (pan pro standard/mini/small/large, duo, wok, crepe, lid, board, utensils, set 12, set pro, 2 pans + 2 lids, sheets, 6-pcs) | ACTIVE |
| `/products/titanium-hammered-pan-set-with-lids-6-pcs-bday-sale` (C3-P, W4-INT, W4-US) | UNLISTED, werkt via URL, $349. Prima zolang die actie loopt |
| `/products/titanium-hammered-pan-set-with-lids-6-pcs` (P3-accessory, R2, R2-VIP) | ACTIVE maar **$399**, terwijl de mail $349 noemt |
| Kortingscode HI10 | ACTIVE, geen einddatum |
| Checkout-fallback `https://siraatskitchen.com/checkout?utm_source=klaviyo&discount=...` (C4) | leeg winkelmandje leidt naar /cart; acceptabel als noodval |
| Domeinen | alle links op siraatskitchen.com, facebook.com, instagram.com. Geen myshopify-links in de templates |

### 2.4 Outlook, Gmail, Apple Mail

| Onderdeel | Oordeel |
| --- | --- |
| Tabellen, role=presentation, 600 px container, bgcolor op td | OK in alle 31 |
| VML-knoppen (`{{BLOCK:cta}}`) | OK: v:roundrect met fillcolor en href. Label in Outlook zonder pijl en zonder hoofdletters (verschilt van de HTML-knop, cosmetisch) |
| Knop in `{{BLOCK:offer}}` (16 mails) | **geen VML**: in Outlook alleen de tekst klikbaar, padding op `<a>` wordt genegeerd |
| Lettertypen | Inter en Instrument Serif via `@import`, fallback Arial en Times New Roman staat er. **Geen mso-override**: Outlook 2016 tot 2021 valt bij een webfont in de stack vaak terug op Times New Roman voor álle tekst. Patch 06 voegt `<!--[if mso]>` Arial-regel toe en zet `@import` in een eigen, voor Outlook verborgen style-blok (dan overleven de media queries ook als een client het @import-blok weggooit) |
| `div` met padding (veel tussenruimte) | Outlook negeert padding op div deels: ruimtes iets krapper. Laag |
| `max-width` op beelden | Outlook gebruikt het width-attribuut; alle hero's en GIF's hebben width. OK |
| `object-fit:cover` op productthumbs | niet in Gmail/Outlook; Shopify-beelden zijn vierkant, dus geen vervorming in de praktijk |
| Achtergrondbeelden op td | geen, dus geen VML-achtergronden nodig. OK |
| Dark mode | `color-scheme: light` meta aanwezig, Apple Mail houdt licht. **Gmail iOS/Android en Outlook.com/app keren kleuren om**: het logo `logo-black.png` (juiste lockup, md5 gelijk aan `brand/logo/lockup/siraat-lockup-black-email.png`) is zwart op transparant en wordt dan zwart op donkergrijs, bijna onzichtbaar. Iconen (brick op transparant) blijven zichtbaar. Footer (wit logo op #282828) OK |
| **Zonder media queries (390 px)** | Getest in alle 31. Alles blijft 600 px breed (scrollWidth 600 op 390 viewport): horizontaal scrollen of uitzoomen tot circa 65 %, waardoor 15 px bodytekst als circa 10 px oogt. Gifts (4 naast elkaar), reviews (2 naast elkaar) en iconen stapelen niet. Nav in de header blijft zichtbaar. Niets valt weg of overlapt, dus bruikbaar maar klein. Raakt Gmail-app met niet-Google-accounts (IMAP/Outlook-adressen) en sommige Android-clients |
| Met media queries (390 px) | Geen overflow in alle 31. Gifts 2x2, reviews gestapeld, knop volle breedte |

### 2.5 Toegankelijkheid

| Check | Resultaat |
| --- | --- |
| lang="en" | OK, alle 31 |
| role=presentation | OK, 0 tabellen zonder |
| alt-teksten | Geen enkel img zonder alt. Decoratieve iconen hebben alt="" (correct, want het label staat ernaast als tekst). Hero-alt noemt het aanbod in alle verkoopmails (W0, P2, P1 zonder aanbod, terecht) |
| Contrast wit op brick #AC3B19 | 6,19:1, OK |
| Grijs #727272 op cream #F8F7F2 | **4,48:1, net onder AA 4,5** voor 13 tot 14 px tekst. Op wit 4,81 OK. Voorstel: #6B6B6B (4,97:1) |
| Brick op cream (eyebrows) | 5,77:1 OK. Footer #BDB8B0 op #282828: 7,47 OK |
| Lettergrootte mobiel | Bodytekst 14 tot 15 px OK. Onder 13 px: icoonlabels 10 px (via mobiele CSS van 11 naar 10 px), eyebrows en codebalk 11 px, reviewnamen, giftwaarde en footer-legal 12 px. Hoofdletterlabels, dus geen bodytekst, maar 10 px is te klein: maak het minimaal 11 px |
| Tap targets (met MQ, 390 px) | Hoofdknoppen 56 px OK. **Footer-navigatie 17 px hoog** (padding zit op de td, niet op de link), tekstlinks als "See the set →" 16 tot 17 px, logo 34 px. Gemiddeld 10 tot 17 links per mail onder 44 px |

### 2.6 Content-consistentie

| Check | Resultaat |
| --- | --- |
| Em dash | geen, in alle bronnen en previews |
| "lifetime", "100-day", "purifier", "reserved", "final call", "30,000", Floris/Ali | niet in de vaste tekst. **Wel via data**: Shopify-regel "PFAS Water Purifier Giveaway (Weekly Draw Entry)" verschijnt in het cart-blok (A3) |
| "independent" | in C2 en W3 ("An independent lab report?"). DECISIONS zegt "nooit independent" (bij Trustpilot); bevestigen of dat ook voor het lab geldt |
| Levertijden | geen. Alleen "within 30 days of delivery" (retourregel, OK) en een reviewquote "Quick delivery" in P3-accessory (geen termijn, OK) |
| Prijzen | $134 Pan Pro, $439 compare-at, $599 12-set, $1,186 compare-at 12-set, $127/$129/$139 maten, $229 duo, $479 set pro, $199 2+2, $139 crepe, $119 wok mini, $59 deksel, $149 utensils, $69 board, $25 sheets: kloppen met Shopify. **$349 6-set klopt alleen op het bday-sale-product** (A5) |
| Gifts | "WITH EVERY ORDER", "$70 in gifts" ($15 + $30 + $25), "chance to win" bij de filter: OK. Naamverschil e-book: blok zegt "Plastic-Free Home e-book", het giftbeeld toont "The Green Clean Guide", de downloadlink is "The Green Clean E-Guide" van $50 |
| Benjamin als afzender | OK waar ondertekend |
| Subject <= 50 tekens | **Te lang**: K3-B 55, W5-B 54, P3-pan-B 51, P3-set-B 51. Rest OK |
| Preview 40 tot 90 | **Te lang**: R2 107, P3-pan 100. Rest 49 tot 88, OK |

### 2.7 Spam-signalen

| Signaal | Oordeel |
| --- | --- |
| Hoofdletters in onderwerp | geen. In body 21 tot 39 woorden in caps (eyebrows, labels), normaal voor dit design |
| Uitroeptekens | 0 in onderwerpen; in body alleen in reviewquotes (max 8 in C3-P, vooral CSS-tekens; echte tekst max 2) |
| "Free" in onderwerp | nergens |
| Beeld/tekst | 250 tot 430 woorden live tekst per mail, 12 tot 20 beelden; W2 is tekstmail. Gezonde verhouding |
| Linkdomeinen | alleen siraatskitchen.com plus social. Klaviyo-tracking wikkelt links in de Klaviyo-trackingdomein; overweeg een branded click-tracking-domein als dat nog niet staat |
| Afzender | default send@siraatskitchen.com. Meerdere mails zeggen "Just reply. A real person reads every email": zet reply-to op een gelezen inbox |
| SPF/DKIM/DMARC | niet te testen (DNS geblokkeerd in container) |

### 2.8 Footer-compliance

Alle 31: `{% unsubscribe %}`, `{% manage_preferences_url %}`, `{% web_view %}`, `{{ organization.full_address }}` (adres gevuld in account). OK. Naam in de footer wordt "SIRAATSKITCHEN" (accountnaam); liever "Siraat's Kitchen" hardcoden of de organisatienaam aanpassen.

Juridisch aandachtspunt (geen e-mailtechniek): de mails koppelen "a chance to win a $450 PFAS water filter" aan "it all comes with your order". In de VS is een prijsvraag die aan aankoop gekoppeld is zonder "No purchase necessary" en officiële regels een risico (illegal lottery). Er is geen regels-pagina in Shopify. Laten checken.

---

## 3. Tabel per mail

Kolommen: HTML = geschatte Klaviyo-HTML; Beeld = statische beelden (exclusief dynamische productfoto's). Codes verwijzen naar de fixlijst (paragraaf 4). Voor elke mail gelden daarnaast de algemene punten **A4, A9, A10, A11, A12, A13, A19, A20** (header/footer en design-system).

| Mail | HTML | Beeld | Grootte | Syntax/data | Links | Content | Status | Ernst |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| checkout/c1 | 23,4 KB | 269 KB | OK | A3, A6, A18 | OK | OK | probleem | Kritiek |
| checkout/c2 | 23,0 KB | 1437 KB | A7, A24 | A3, A6, A18 | OK | A15 | probleem | Kritiek |
| checkout/c3-p | 24,8 KB | 320 KB | OK | A3, A6, A18 | OK (bday-sale) | OK | probleem | Kritiek |
| checkout/c3-s | 24,4 KB | 252 KB | OK | A3, A6, A18 | OK | OK | probleem | Kritiek |
| checkout/c4-int | 23,4 KB | 240 KB | OK | A1, A3, A6, A18 | OK | OK | probleem | Kritiek |
| checkout/c4-us | 25,2 KB | 379 KB | OK | A1, A3, A6, A18 | OK | OK | probleem | Kritiek |
| cart/k1 | 24,9 KB | 325 KB | OK | A6 | OK | OK | probleem | Hoog |
| cart/k2-new | 24,6 KB | 258 KB | OK | A6 | OK | OK | probleem | Hoog |
| cart/k2-returning | 23,2 KB | 285 KB | OK | A6 | OK | OK | probleem | Hoog |
| cart/k3 | 24,0 KB | 241 KB | OK | A1, A6 | OK | A14 (subject B 55) | probleem | Kritiek |
| browse/b1 | 25,2 KB | 316 KB | OK | A18 (valuta) | OK | OK | algemeen | Midden |
| browse/b2-clicked | 26,0 KB | 235 KB | OK | A1, A18 | OK | OK | probleem | Kritiek |
| browse/b2-notclicked | 24,8 KB | 231 KB | OK | A18 | OK | OK | algemeen | Midden |
| post-purchase/p1-first | 26,0 KB | 270 KB | OK | A3, A6, A17 | A16 | A16 | probleem | Kritiek |
| post-purchase/p1-repeat | 19,3 KB | 272 KB | OK | A3, A6, A17 | A16 | OK | probleem | Kritiek |
| post-purchase/p2 | 23,6 KB | 1824 KB | A7 | OK | OK | OK | probleem | Midden |
| post-purchase/p3-accessory | 24,7 KB | 247 KB | OK | A1 | A5 | A5 | probleem | Kritiek |
| post-purchase/p3-pan | 23,1 KB | 238 KB | OK | A1 | OK | A14 (subject B 51, preview 100) | probleem | Kritiek |
| post-purchase/p3-set | 23,4 KB | 287 KB | OK | A1 | OK | A14 (subject B 51) | probleem | Kritiek |
| welcome/w0 | 18,2 KB | 1474 KB | A7 | OK | OK | OK | probleem | Midden |
| welcome/w1-a | 25,2 KB | 305 KB | OK | OK | OK | OK | algemeen | Midden |
| welcome/w1-b | 25,2 KB | 370 KB | OK | OK | OK | OK | algemeen | Midden |
| welcome/w2 | 10,7 KB | 24 KB | OK | OK | OK | OK | algemeen | Midden |
| welcome/w3 | 24,8 KB | 388 KB | A8 (hero 317 KB) | OK | OK | A15 | probleem | Midden |
| welcome/w4-int | 27,8 KB | 271 KB | OK | OK | OK (bday-sale) | OK | algemeen | Midden |
| welcome/w4-us | 28,5 KB | 386 KB | OK | OK | OK (bday-sale) | OK | algemeen | Midden |
| welcome/w5 | 25,5 KB | 388 KB | OK | A2 | OK | A14 (subject B 54) | probleem | Kritiek |
| winback/r1-pan | 26,9 KB | 410 KB | OK | OK | OK | OK | algemeen | Midden |
| winback/r1-set | 26,8 KB | 345 KB | OK | OK | OK | OK | algemeen | Midden |
| winback/r2 | 26,9 KB | 373 KB | OK | A1 | A5 | A5, A14 (preview 107) | probleem | Kritiek |
| winback/r2-vip | 26,7 KB | 360 KB | OK | A1 | A5 | A5 | probleem | Kritiek |

"Algemeen" = alleen de punten die voor alle 31 gelden (hoogste daarvan: A4 hoog, de collectie-link; na patch 01 zakt dat naar midden).

---

## 4. Geprioriteerde fixlijst

| # | Ernst | Probleem | Mails | Fix |
| --- | --- | --- | --- | --- |
| A1 | Kritiek | Coupons bestaan niet in Klaviyo (0 coupons). Mail met onbekende coupon wordt niet verstuurd | C4-INT, C4-US, K3, B2-clicked, P3 x3, R2, R2-VIP | In Klaviyo aanmaken als Shopify-coupon (unieke codes, 1 keer per klant, vervaltermijn per code): C4_10_48H, K3_10_48H, B2_10_48H, P3_THANKYOU_10_14D, R2_10_72H, R2_VIP_15_72H. Daarna test-preview met een profiel |
| A2 | Kritiek | `{% coupon_code 'W5_10_72H' %}` staat in de metadata-comment van W5 en wordt gerenderd | W5 | Patch 03 (tag onschadelijk maken) en patch 06 (comments uit de Klaviyo-versie) |
| A3 | Kritiek | Cart-blok toont gift-regels van $0 (incl. "Purifier") en verbergt in 40 % van de checkouts het betaalde product | C1, C2, C3-P, C3-S, C4-INT, C4-US, P1-first, P1-repeat | Patch 02: `{% if item.line_price > 0 %}` in plaats van `forloop.counter <= 3` (toont alle betaalde regels) |
| A4 | Hoog | `/collections/cookware` bestaat niet: 2 dode links per mail | alle 31 | Patch 01: naar `/collections/pans` ("Titanium Pan Collection"), ook in de kopie `v3/checkout/partials/` |
| A5 | Hoog | "$349" voor de 6-set linkt naar het $399-product | P3-accessory, R2, R2-VIP | Patch 04: link naar `...-6-pcs-bday-sale`. Let op: als de bday-sale stopt, moeten C3-P, W4 en deze drie mee naar $399 |
| A6 | Hoog | Productfoto's op volle resolutie (321 tot 460 KB per stuk op 88 px) | C1 t/m C4, P1 x2, K1 t/m K3 | Patch 02 (`thumb_src`, 240 px) en patch 05 (`ImageURL` + `&width=200`) |
| A7 | Midden | Beeldgewicht boven 1 MB door GIF's | P2 (1,8 MB), W0 (1,5 MB), C2 (1,4 MB) | Elke tweede frame weg + 128 kleuren: -50 % per GIF (zie 2.1). C2: anatomy desktop en mobiel naar q78 |
| A8 | Midden | Hero boven 250 KB; hero's op circa q85 | W3 (317 KB), alle hero's | Alle hero's q80 progressive (circa -10 %, SSIM > 0,99); W3 q74 of iets kleinere uitsnede |
| A9 | Midden | Dark mode: zwart logo op transparant verdwijnt in Gmail-app en Outlook.com dark | alle 31 | Logo-PNG met dunne lichte rand (1 tot 2 px #F8F7F2 glow) of met ingebakken cream-achtergrond; plus `[data-ogsc]`-regel die naar `logo-white` wisselt voor Outlook.com |
| A10 | Midden | Geen Outlook-fontfallback bij webfonts: risico Times New Roman | alle 31 | Patch 06 (mso Arial-regel, `@import` in eigen niet-mso style-blok) |
| A11 | Midden | Zonder media queries 600 px vast, klein op mobiel | alle 31 | Hoofdcontainer fluid-hybrid: `width="100%" style="max-width:600px"` met een mso-ghosttabel van 600; gifts/reviews als inline-block kolommen |
| A12 | Midden | Tap targets onder 44 px (footer-nav 17 px, tekstlinks 16 px) | alle 31 | Footer: padding van td naar `<a style="display:block;padding:15px 4px">`. Secundaire tekstlinks: `display:inline-block;padding:12px 0` |
| A13 | Laag | Grijs #727272 op cream 4,48:1; icoonlabels 10 px op mobiel | alle 31 | #727272 overal naar #6B6B6B (4,97:1); `.ic div` mobiel 11 px in `_style.css` |
| A14 | Midden | Subject boven 50 of preview boven 90 tekens | K3, W5, P3-pan, P3-set, R2 | Inkorten, bv. K3-B "75-year warranty, 30-day returns, 10% less" (42); W5-B "What 100,000+ customers found out (+10%)" (40); R2-preview "Your own 10% code, one tap. Plus $70 in gifts. Ends in 72 hours." (66) |
| A15 | Laag | "independent" ondanks regel in DECISIONS | C2, W3 | Bevestigen of het lab-gebruik mag; anders "An accredited lab report?" |
| A16 | Midden | "Download your e-book" gaat naar /products/e van $50; naam e-book verschilt (blok, beeld, product) | P1-first, P1-repeat, gift-blok | Link naar `/products/the-green-e-guide-free` of de echte download (PDF); één naam kiezen. Besluit van 7 okt (DECISIONS) noemt /products/e, dus eerst met Floris checken |
| A17 | Laag | Ordernummer 107762 in plaats van "#SIRAAT107762" | P1 x2 | Patch 02: `{{ event.extra.name }}` |
| A18 | Laag | Valuta: USD-bedragen bij niet-USD checkouts (13 %); browse toont "Dhs. 500.00" naast $-prijzen | C1 t/m C4, B1, B2 | Patch 02 verbergt de regelprijs als `presentment_currency` niet USD is |
| A19 | Laag | Interne metadata-comment voor DOCTYPE en andere comments gaan mee naar ontvangers (couponnamen, segmentlogica, circa 1,2 KB) | alle 31 | Patch 06 |
| A20 | Laag | Footer toont "SIRAATSKITCHEN" (organization.name) | alle 31 | In footer.html "Siraat's Kitchen" vast zetten of naam in Klaviyo-account aanpassen |
| A21 | Midden (juridisch) | Prijsvraag gekoppeld aan bestelling zonder regels of "No purchase necessary" | alle mails met gift-blok | Regels-pagina plus één regel kleine tekst onder het gift-blok |
| A22 | Laag | "Just reply" terwijl afzender send@ is | C1, W2 e.a. | Reply-to op support-inbox in flow-instellingen |
| A23 | Laag | Offer-blok-knop zonder VML; VML-label wijkt af | 16 mails met offer-blok | VML-roundrect zoals in cta.html toevoegen aan offer.html (fill #FFFFFF, tekst #321E1D) |
| A24 | Laag | C2 laadt anatomy desktop en mobiel (beide circa 190 KB) | C2 | Compressie q78, of mobiel-uitsnede als enige beeld met live labels eronder |
| A25 | Laag | `v3/checkout/partials` is een kopie, geen symlink (post-purchase en winback zijn symlinks) | checkout | Vervangen door symlink naar `../../partials` om drift te voorkomen |

Geen actie nodig: Gmail-clipping, lang, role=presentation, alt-teksten, em dash, levertijden, spam-woorden in onderwerpen, footer-compliance, HI10 actief, alle productlinks behalve de twee hierboven.

---

## 5. Patches (`research/qa-2026-10-07/patches/`)

Alle zes getest met `git apply --check -p1` vanuit de repo-root; patch 06 plus 02 en 05 zijn proefgebouwd in een kopie (C1, P1-first, K1, W5): if/for in balans, geen comments of coupon-tags meer in de Klaviyo-versie, VML-knoppen intact, preview werkt.

| Patch | Inhoud |
| --- | --- |
| 01-collections-cookware-404.patch | header.html en footer.html (globaal en checkout-kopie): `/collections/cookware` naar `/collections/pans` |
| 02-cart-block-gifts-thumbs-currency.patch | blocks/cart.html, p1-first, p1-repeat: alleen regels met prijs > 0, `thumb_src`, prijs alleen bij USD, ordernaam |
| 03-w5-coupon-tag-in-comment.patch | w5.html: coupon-tag in metadata-comment onschadelijk |
| 04-six-piece-set-349-handle.patch | p3-accessory, r2, r2-vip: 6-set-link naar het $349-product |
| 05-added-to-cart-image-width.patch | k1 t/m k3: `ImageURL` met `&width=200` |
| 06-build-strip-comments-mso-font.patch | build_template.py: comments uit de Klaviyo-versie, mso-fontfallback, @import apart; preview-regex bijgewerkt voor patch 02 |

Toepassen: `cd /home/user/siraat-email-agent && git apply -p1 research/qa-2026-10-07/patches/0X-*.patch`, daarna alle templates opnieuw bouwen. Volgorde: 06 eerst (anders matcht de preview-regex niet meer na 02).
