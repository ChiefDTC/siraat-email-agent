# Productcatalogus (content/catalog)

Alle actieve producten van siraatskitchen.com als gestructureerde data, met prijzen en compare-at per land, beschikbaarheid per markt, maten in cm en inch, gewicht, beelden, PDP-teksten en FAQ. Stand: 8 oktober 2026 (fall sale actief). Gemaakt door de markten-agent (fase 1), zie `research/v5/01-markten.md` voor de tailoring per markt.

## Bestanden

| Bestand | Inhoud |
|---|---|
| `products.json` | 64 producten (alle 66 actieve min 2 niet-gepubliceerde Shipbob-kopieën), elk met varianten, prijzen per land, beschikbaarheid, beelden, PDP-secties en FAQ |
| `README.md` | Deze uitleg plus een leesbare index |
| `../../scripts/refresh_catalog.py` | Vernieuwt `products.json` (alleen lezen op de site; ruwe pagina's in `/tmp`, nooit in git) |

## Bronnen

1. **Storefront per land**: `https://siraatskitchen.com/products/<handle>.js` met de cookie `localization=<LAND>`. Zo rekent Shopify de prijs van die markt (prijslijst of omrekening). Gecontroleerd tegen Admin `contextualPricing`: zelfde bedragen (bv. Pan Pro Standard CA 224, AU 224, HK 1.147).
   Let op: de site heeft **geen** submappen per markt. `/en-au/`, `/en-gb/` enz. geven voor elk product 404; dat is dus geen bewijs voor "US only".
2. **PDP-HTML (US)** voor secties (OVERVIEW, DETAILS, WHAT'S INCLUDED, CARE & USE, DIMENSIONS) en de FAQ.
3. **Shopify Admin GraphQL** (alleen lezen): `products(query:"status:active")` voor de lijst van 66 actieve producten en `publishedInContext(country)` voor de beschikbaarheid per markt.

Landen in de data: US, CA, GB, DE, NL, FR, AU, NZ, SG, HK, AE, CH, NO, SE, JP. Valuta per land staat in `currency_by_country` (NO rekent in USD).

## Structuur van een product

```
handle, title, url, tags
role                  "verkoop" | "gift (gratis, auto-add)" | "duplicaat-listing van <handle>" (nooit linken)
us_only               true = alleen in de US-markt gepubliceerd (Admin publishedInContext)
published_storefront  {land: true/false}  (.js gaf 200 of 404 met die cookie)
variants[]            id, title, options, sku, weight_g,
                      size_cm, size_in_exact (cm/2,54), size_in_nominal (zoals de site het noemt: 8/9.5/10/11/12),
                      available {land: bool}, prices {land: {price, compare_at, currency}}
images[]              eerste 10 beeld-URL's (images_total = totaal)
pdp                   tagline, rating, reviews, badge (label boven de galerij), important_notice,
                      sections {OVERVIEW: [...], DETAILS: [...], ...}, whats_in_the_box[], whats_in_the_box_faq[],
                      dimensions [{cm, in}], faq [{q, a}], site_shipping_line
```

`compare_at: null` betekent: in dat land geen doorgestreepte prijs (veel in NZ). Bedragen zijn in de valuta van dat land.

## Gebruik in mails

- Prijzen en compare-at in mails komen voortaan **uit dit bestand**, per markt, niet uit de copy. De helper in `build_template.py` (voorstel in `research/v5/01-markten.md`, sectie 8) leest het bij het bouwen.
- **PDP-tekst is geen goedgekeurde claim.** De site zegt o.a. "548°C / 1000°F", "built to last a lifetime", "scratch-proof", "Free Express Shipping from the US" en "Medium" (bestaat niet). Claims alleen uit `content/facts/claims.csv` en DECISIONS.md.
- Gift-producten (`role` gift) staan erin voor hun waarde per markt (compare-at van free shipping en e-book). Nooit als product tonen.
- Duplicaat-listings (`-copy`, `-copy-1`) nooit linken; gebruik de hoofdhandle.

## Vernieuwen

```
cd /tmp && python3 -I /home/user/siraat-email-agent/scripts/refresh_catalog.py /home/user/siraat-email-agent/content/catalog/products.json
```

Duurt circa 45 minuten (66 producten x 15 landen, met pauze tussen verzoeken). Komt er een product of markt bij: eerst in Shopify Admin `products(query:"status:active")` en `publishedInContext` lezen en `HANDLES` en `US_ONLY` in het script bijwerken. Met `--no-fetch` alleen opnieuw parsen uit de ruwe map.

## Index (US-prijzen; andere landen in products.json)

| Product | Handle | Rol | Markten | Prijs USD | Compare-at USD | Maten | Gewicht | In de doos (PDP) |
|---|---|---|---|---|---|---|---|---|
| 2 Pans + 2 Lids | `2-pans-and-2-lids` | verkoop | alleen US | 199 | 844 |  | 4100 g | An 8" Mini pan for eggs, sauces and sides, and an 11" Standard pan, our best-seller, for everyday meals and a solo batch cook. Each pan comes with its own fitte |
| Cherry Wood Mini Trivet | `cherrywood-mini-trivet` | verkoop | alle 15 gemeten landen | 19 | geen |  | 160 g |  |
| Diatomite Mat Anthracite | `diatomite-mat-anthracite-ultra-hygienic-fast-drying-mold-resistant` | verkoop | alle 15 gemeten landen | 47 | 100 |  | 200 g |  |
| E-Gift Card | `e-gift-card` | verkoop | alle 15 gemeten landen | 100/200/25/50 | geen |  |  |  |
| Full Hammered Pro Edition | `full-hammered-pro-edition` | verkoop | alle 15 gemeten landen | 779 | 1760 |  | 8600 g | 1 Hammered Pan Pro Mini including lid / 1 Hammered Pan Pro Medium including lid / 1 Hammered Pan Pro Standard including lid / 1 Hammered Pan Pro Large including |
| Grill Press | `grill-press` | verkoop | alle 15 gemeten landen | 69 | 115 |  | 850 g |  |
| Magnetic Cherry Wood Trivet | `magnetic-cherry-wood-trivet` | verkoop | alle 15 gemeten landen | 29 | geen | 20 cm (8″) | 245 g |  |
| Non Slip Mat For Cutting Board | `siraat-non-slip-mat-for-board-premium-silicone` | verkoop | alle 15 gemeten landen | 49 | geen |  | 90 g |  |
| Pepper Mill | `pepper-mill` | verkoop | alle 15 gemeten landen | 79 | 119 |  | 752 g | 1× Siraat® Pepper Mill (matte black) / Cleaning kit for long-term performance / Instruction & care card / Premium recyclable packaging |
| Pizza Wheel | `pizza-wheel` | verkoop | alle 15 gemeten landen | 24 | 35 |  | 175 g |  |
| Plastic-Free Dishwasher Sheets | `dishwashing-detergent-sheets-fresh-lemon` | verkoop | alle 15 gemeten landen | 25 | geen |  |  | Per pack: 30 sheets, up to 60 washes, in a zip-tear paper envelope, with the dosing guide printed on the back. |
| Rolling Knife Sharpener | `rolling-knife-sharpener-diamond-ceramic` | verkoop | alle 15 gemeten landen | 63 | 105 |  |  |  |
| Salt & Pepper Mill Set | `salt-pepper-mill-set` | verkoop | alle 15 gemeten landen | 149 | 199 |  | 650 g | 1× Siraat® Salt Mill (gunmetal silver) / 1× Siraat® Pepper Mill (matte black) / 2× Cleaning kit for long-term performance / Instruction & care cards / Premium r |
| Salt Mill | `salt-mill` | verkoop | alle 15 gemeten landen | 79 | 119 |  | 650 g | 1× Siraat® Salt Mill (gunmetal silver) / Cleaning kit for long-term performance / Instruction & care card / Premium recyclable packaging |
| Siraat Signature Apron (Azure) | `siraat-signature-apron-azure` | verkoop | alle 15 gemeten landen | 54 | 100 |  | 513 g | 1 × Siraat Signature Apron |
| Siraat Signature Apron (Ember) | `siraat-signature-apron-ember` | verkoop | alle 15 gemeten landen | 54 | 100 |  | 513 g | 1 × Siraat Signature Apron |
| Siraat Signature Apron (Moss) | `siraat-signature-apron-moss` | verkoop | alle 15 gemeten landen | 54 | 100 |  | 513 g | 1 × Siraat Signature Apron |
| Siraat Signature Apron (Oak) | `siraat-signature-apron-oak` | verkoop | alle 15 gemeten landen | 54 | 100 |  | 550 g | 1 × Siraat Signature Apron |
| Stainless Steel Lid | `stainless-steel-lid` | verkoop | alle 15 gemeten landen | 59 | 110 | 20 cm (8″), 26 cm (10″), 28 cm (11″), 30 cm (12″) | 750/825/971 g |  |
| The Green Clean E-Guide | `e` | verkoop | alle 15 gemeten landen | 50 | 80 |  |  |  |
| The Just Everything Bundle / 34-Pcs | `the-just-everything-bundle-34-pcs` | verkoop | alleen US | 1499 | 4342 |  | 12000 g | WHAT'S INCLUDED (34 pieces) / The 12-Piece Titanium Hammered Cookware Set / 3 hammered frying pans 8" + 10" + 12" / 2L (2.1 qt) saucepan / 3L (3.2 qt) saucepan  |
| Titanium Chopsticks | `titanium-chopsticks` | verkoop | alle 15 gemeten landen | 49 | geen |  | 203 g |  |
| Titanium Cook & Prep Bundle | `titanium-hammered-pro-prep-cook-set` | verkoop | alle 15 gemeten landen | 199 | 270 | 28 cm (11″) | 2220 g | Titanium Hammered Pan Pro (28cm / 11,0") / Titanium Cutting Board V2 - Size L (39×28 cm / 15″×11″), / Titanium Cook & Prep Bundle L (39x28cm / 15″ x 11") / 28CM |
| Titanium Cutting Board (Anti-Microbial) | `titanium-cutting-board-v2` | verkoop | alle 15 gemeten landen | 69/79/89/99 | 140/160/180/200 |  | 390/520/750/900 g |  |
| Titanium Cutting Board Bundle | `titanium-cutting-board-v2-bundle` | verkoop | alle 15 gemeten landen | 149 | 680 |  | 1200 g | What's inside the bundle? / Size S (29×20 cm / 12″×8″) / Size M (34×23 cm / 14″×10″) / Size L (39×28 cm / 15″×11″) / Size XL (46×30 cm / 18″×12″) |
| Titanium Cutting Board V2 Gold Edition (Anodized) | `titanium-cutting-board-v2-gold-edition` | verkoop | alle 15 gemeten landen | 99 | geen |  | 390 g |  |
| Titanium Hammered Complete Edition | `the-hammered-collection` | verkoop | alle 15 gemeten landen | 399 | 1330 |  | 5392 g | Hammered Pan Pro 28 cm / 11.0″ – Height: 6.3 cm / 2.5″ / Hammered Wok Pan Pro 26 cm / 10.2″ – Height: 9 cm / 3.5″ / Hammered Deep Pan Pro 26 cm / 10.2″ – Height |
| Titanium Hammered Cookware Set Pro | `titanium-hammered-cookware-set-pro` | verkoop | alle 15 gemeten landen | 379 | 1263 |  | 4000 g | Hammered Pan Pro 28 cm / 11.0″ – Height: 6.3 cm / 2.5″ / Hammered Wok Pan Pro 28 cm / 10.2″ – Height: 9 cm / 3.5″ / Hammered Deep Pan Pro 26 cm / 10.2″ – Height |
| Titanium Hammered Cookware Set / 12-Pcs | `titanium-hammered-cookware-set` | verkoop | alleen US | 599 | 1186 |  |  | Three pans (Pan Pro Mini 8", Small 10", Large 12"), three pots (2-Qt and 3-Qt Saucepans and an 8-Qt Stock Pot), and six fitted lids, one for every pan and pot. |
| Titanium Hammered Crêpe Pan Pro | `titanium-hammered-crepe-pan-pro` | verkoop | alle 15 gemeten landen | 129 | 210 | 28 cm (11″) | 970 g | Titanium Crêpe Pan – securely packaged in a special protective box / 5 Essential Guides – including care tips, first-time seasoning, and pro cooking techniques |
| Titanium Hammered Deep Pan Pro | `titanium-hammered-deep-pan-pro` | verkoop | alle 15 gemeten landen | 119/134/139/144/149 | 389/439/455/475/489 | 20 cm (8″), 24 cm (9.5″), 26 cm (10″), 28 cm (11″), 30 cm (12″) | 1100/1250/1400 g | Titanium Hammered Pan – securely packaged in a custom protective box / 5 Essential Guides – including care tips, first-time seasoning, and pro cooking technique |
| Titanium Hammered Pan Pro & Utensil Set | `titanium-hammered-pan-pro-utensil-set` | verkoop | alle 15 gemeten landen | 249 | geen |  | 2530 g | Titanium Hammered Pan Pro 28 cm / 11.0″ / Flipper, Spatula, Scooper & Laddle (complete utensil set) |
| Titanium Hammered Pan Pro Duo | `titanium-hammered-pan-pro-duo` | verkoop | alle 15 gemeten landen | 249 | 570 |  |  | Hammered Pan Pro Mini : 20cm / 7.8" - Height: 6cm / 2.3" / Hammered Pan Pro Standard : 28 cm / 11″ – Height: 6.3 cm / 2.5″ |
| Titanium Hammered Pan Pro Kit | `titanium-hammered-pan-pro-kit` | verkoop | alle 15 gemeten landen | 199 | 470 |  | 2400 g | What's included: / Titanium Hammered Pans (26 cm / 10.2″) – securely packaged in a special protective box / Pure stainless steel lid with three precision steam  |
| Titanium Hammered Pan Pro Large | `titanium-hammered-pan-pro-large` | verkoop | alle 15 gemeten landen | 149 | 298 | 30 cm (12″) | 1990 g | Titanium Hammered Pan – securely packaged in a special protective box / 5 Essential Guides – including care tips, first-time seasoning, and pro cooking techniqu |
| Titanium Hammered Pan Pro Mini | `titanium-hammered-pan-pro-mini` | verkoop | alle 15 gemeten landen | 99 | 330 | 20 cm (8″) | 1000 g | Titanium Hammered Pan, securely packaged in a special protective box / 5 Essential Guides – including care tips, first-time seasoning, and pro cooking technique |
| Titanium Hammered Pan Pro Small | `titanium-hammered-pan-pro-small` | verkoop | alle 15 gemeten landen | 137 | 274 | 26 cm (10″) | 1470 g | Titanium Hammered Pan – securely packaged in a special protective box / 5 Essential Guides – including care tips, first-time seasoning, and pro cooking techniqu |
| Titanium Hammered Pan Pro Standard | `original-siraat-100-pure-titanium-pan-with-hammered-pattern` | verkoop | alle 15 gemeten landen | 144 | 288 | 28 cm (11″) | 1470 g | Titanium Hammered Pan, securely packaged in a special protective box / 5 Essential Guides – including care tips, first-time seasoning, and pro cooking technique |
| Titanium Hammered Pan Pro With Lid | `titanium-hammered-pan-pro-incl-lid` | verkoop | alle 15 gemeten landen | 174/189/199 | 265/305/340 | 26 cm (10″), 28 cm (11″), 30 cm (12″) | 2066/2233/2509 g | Titanium Hammered Pan – securely packaged in a special protective box / Premium 304 Stainless Steel Lid / 5 Essential Guides – including care tips, first-time s |
| Titanium Hammered Pan Set With Lids / 6-Pcs | `titanium-hammered-pan-set-with-lids-6-pcs` | verkoop | alle 15 gemeten landen | 299 | 598 |  | 5870 g | Three hammered pans (Pan Pro Mini 8", Small 10", Large 12"), each with a matching fitted stainless steel lid. Care and use guides are included in the box. Utens |
| Titanium Hammered Pizza Steel | `titanium-hammered-pizza-steel` | verkoop | alle 15 gemeten landen | 129 | 200 |  | 400 g |  |
| Titanium Hammered Pot With Lid / 3-Qt | `3-litre-titanium-hammered-pot-with-lid` | verkoop | alleen US | 179 | geen |  |  |  |
| Titanium Hammered Pro Duo | `titanium-pro-duo` | verkoop | alle 15 gemeten landen | 199 | 275 | 28 cm (11″) | 1570 g | Hammered Pan Pro 28 cm / 11.0″ / Titanium Flipper |
| Titanium Hammered Roasting Pan | `titanium-hammered-roasting-pan` | verkoop | alleen US | 199 | 250 |  | 3000 g | Yes. A fitted roasting rack (33.5 × 23.5 × 10 cm / 13.2″ × 9.3″ × 3.9″) is included. It lifts your roast off the base so hot air circulates and the skin crisps  |
| Titanium Hammered Saucepan With Lid / 2-Qt | `2-litre-titanium-hammered-pot-with-lid` | verkoop | alleen US | 149 | geen |  |  |  |
| Titanium Hammered Saucepan With Lid / 8-Qt | `7-5-litre-titanium-hammered-pot-with-lid` | verkoop | alleen US | 219 | geen |  |  |  |
| Titanium Hammered Wok Pan Pro | `titanium-hammered-wok-pan-pro` | verkoop | alle 15 gemeten landen | 119/127/134/139 | 389/419/439/455 | 24 cm (9.5″), 26 cm (10″), 28 cm (11″), 30 cm (12″) | 1385/1520/1620 g | Titanium Hammered Pan – securely packaged in a custom protective box / 5 Essential Guides – including care tips, first-time seasoning, and pro cooking technique |
| Titanium Ice Cubes | `siraat-titanium-ice-cubes` | verkoop | alle 15 gemeten landen | 49/59 | 69/79 |  | 178/286 g |  |
| Titanium Pan Pro | `original-siraat-100-pure-titanium-pan` | verkoop | alle 15 gemeten landen | 119 | 245 | 26 cm (10″) | 1500 g |  |
| Titanium Straws | `titanium-straws` | verkoop | alle 15 gemeten landen | 49/59 | geen |  |  |  |
| Titanium Utensil | `siraat-pure-titanium-utensils` | verkoop | alle 15 gemeten landen | 30 | 79 |  | 100 g |  |
| Titanium Utensil Set Bundle | `siraat-pure-titanium-utensils-bundle` | verkoop | alle 15 gemeten landen | 79 | 320 |  | 1061 g |  |
| Titanium Water Bottle | `titanium-water-bottle` | verkoop | alle 15 gemeten landen | 49 | 80 |  | 300 g |  |
| Tote Bag | `tote-bag` | verkoop | alle 15 gemeten landen | 34 | geen |  |  | 1 × Siraat Signature Apron |
| Titanium Hammered Pan Pro Large | `titanium-hammered-pan-pro-large-copy` | duplicaat-listing van titanium-hammered-pan-pro-large | alleen US | 169 | geen | 30 cm (12″) |  | Titanium Hammered Pan – securely packaged in a special protective box / 5 Essential Guides – including care tips, first-time seasoning, and pro cooking techniqu |
| Titanium Hammered Pan Pro Standard | `titanium-hammered-pan-pro-standard-copy` | duplicaat-listing van original-siraat-100-pure-titanium-pan-with-hammered-pattern | alleen US | 157 | geen | 28 cm (11″) | 1470 g | Titanium Hammered Pan, securely packaged in a special protective box / 5 Essential Guides – including care tips, first-time seasoning, and pro cooking technique |
| Titanium Hammered Pan Pro Standard | `titanium-hammered-pan-pro-standard-copy-1` | duplicaat-listing van original-siraat-100-pure-titanium-pan-with-hammered-pattern | alle 15 gemeten landen | 144 | geen | 28 cm (11″) | 1755 g | Titanium Hammered Pan, securely packaged in a special protective box / 5 Essential Guides – including care tips, first-time seasoning, and pro cooking technique |
| Free Shipping | `free-shipping-sca_clone_freegift` | gift (gratis, auto-add) | alle 15 gemeten landen | 0 | 15 |  |  |  |
| Mystery Gift | `dishwashing-detergent-sheets-fresh-lemon-sca_clone_freegift` | gift (gratis, auto-add) | alle 15 gemeten landen | 0 | geen |  |  |  |
| PFAS Water Purifier Giveaway (Weekly Draw Entry) | `entry-to-win-your-order-sca_clone_freegift` | gift (gratis, auto-add) | alle 15 gemeten landen | 0 | geen |  |  |  |
| Plastic-Free Home E-Book | `the-green-clean-e-guide-sca_clone_freegift` | gift (gratis, auto-add) | alle 15 gemeten landen | 0 | 30 |  |  |  |
| The Green Clean E-Guide | `e-sca_clone_freegift` | gift (gratis, auto-add) | alle 15 gemeten landen | 0 | 50 |  |  |  |
| The Green E-Guide - FREE | `the-green-e-guide-free` | gift (gratis, auto-add) | alle 15 gemeten landen | 0 | geen |  |  |  |
| 🎁 Non Slip Mat For Cutting Board (100% off) | `siraat-non-slip-mat-for-board-premium-silicone-sca_clone_freegift` | gift (gratis, auto-add) | alle 15 gemeten landen | 0 | geen |  | 90 g |  |

Ontbreken in `products.json` (actief maar niet gepubliceerd in de winkel, `.js` overal 404): `stainless-steel-lid-copy` (Stainless Steel Lid (S), US-only Shipbob-listing) en `titanium-hammered-pan-pro-mini-copy`. Beide nooit gebruiken.

## Bekende fouten op de site (niet in mails overnemen)

- Wok- en Deep Pan-varianten heten op de site in inch ("Mini 9″", "Standard 9.4″"), in Shopify in cm ("Mini 24CM"). De Deep Pan "Standard" is 24 cm, de koekenpan "Standard" 28 cm.
- Complete Edition noemt de crêpepan 30 cm, de eigen PDP 28 cm. Cookware Set Pro noemt de wok "28 cm / 10.2″" (28 cm is 11″).
- Full Hammered Pro Edition noemt een "Medium" Pan Pro, die bestaat niet.
- E-Gift Card heeft optielabels in euro ("€25,00") en een vaste CAD-prijs van C$50 voor de $25-kaart.
- Pan Pro Mini kost in de US $99 (veel goedkoper dan de Small, $137), maar in de UK £109 en in AU A$194, bijna gelijk aan de Small (£119, A$219). De verhouding tussen de maten verschilt dus per markt.
