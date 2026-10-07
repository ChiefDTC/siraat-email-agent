# 00 · Data: wat zit er in de carts, en wie zijn het

Stand 7 oktober 2026. Bron: Klaviyo API (GET /api/events, revision 2025-10-15, alleen lezen) en metric-aggregates. Steekproef: de 800 meest recente events per metric, 3.200 in totaal. Per profiel is met een aparte GET opgezocht of er vóór het event al een Placed Order was en of daarin kookgerei zat. Profiel-ID's alleen gehasht en alleen in het geheugen gebruikt; hier staan uitsluitend aggregaten. Scripts: scratch (fetch.py, classify.py, analyze2.py), niet in de repo.

## Steekproef en weekvolume

| Metric | ID | Steekproef | Periode steekproef | Unieke profielen per week (aggregaat, 14 sep tot 4 okt) | Instroom in de flow per week (schatting) |
| --- | --- | --- | --- | --- | --- |
| Checkout Started | RfMvni | 800 events, 638 profielen | 5 tot 7 okt (2,1 dagen) | 1.620 tot 1.920 | ~630 (mail 1 van Y2TmNB + Tsg2tV, 90 d / 13) |
| Added to Cart | QXcV8K | 800 events, 288 profielen | 6 tot 7 okt (21 uur) | 1.450 tot 1.840 | ~990 (mail 1 van SwkMyn + TBWngE) |
| Viewed Product | XNtYMB | 800 events, 452 profielen | 7 okt (8 uur, alleen ochtend US/EU) | 5.360 tot 6.880 | ~3.000 (aanname: de twee browse-flows sturen deels naar dezelfde mensen; som mail 1 is 6.000) |
| Placed Order | RSNxYV | 800 orders | 4 tot 7 okt | 980 tot 1.320 | ~1.150 (post-purchase); winback R1 ~1.230 |

Beperkingen: Viewed Product dekt maar 8 uur, dus tijdzone-scheef. Added to Cart dekt een dag. Categorieaandelen zijn goed bruikbaar, absolute weekaantallen in de rest van deze map zijn schattingen (aandeel x instroom per week).

## Verdeling per trigger (eerste event per profiel, dus het event dat de flow start)

Categorie-indeling op betaalde regels (gratis gift-regels genegeerd). "Kookgerei" = Pan Pro, wok, deep, crêpe, pizza steel, roasting pan, pots. "Set" = set, bundel, Duo, Kit, Edition, 2 Pans + 2 Lids, of twee of meer kookgerei-stuks.

### Checkout Started (638 profielen)

| Categorie | Aandeel | Mediaan $ | Al eerder gekocht | Waarvan had al kookgerei |
| --- | --- | --- | --- | --- |
| Alleen Pan Pro (1 stuk) | 44,0% | 139 | 8% | 7% |
| Set of bundel | 17,7% | 516 | 13% | 13% |
| Kookgerei + accessoire (vooral pan + deksel of plank) | 10,3% | 245 | 11% | 11% |
| Meerdere losse pannen | 3,1% | 292 | 15% | 15% |
| Set + accessoire | 1,9% | 681 | 27% | 27% |
| 1 deep pan | 1,9% | 136 | 25% | 25% |
| 1 wok | 1,6% | 143 | 40% | 40% |
| 1 pizza steel | 1,1% | 129 | 14% | 14% |
| 1 crêpe pan | 0,9% | 152 | 0% | 0% |
| 1 roasting pan | 0,5% | 199 | 33% | 33% |
| **Alleen accessoires, samen** | **15,0%** | | | |
| · meerdere accessoires (trivet, bottle, utensils, molens) | 6,4% | 19 | 0% | 0% |
| · alleen snijplank | 4,1% | 149 | 44% | 40% |
| · alleen schort | 2,0% | 56 | 0% | 0% |
| · alleen molen(s) | 1,6% | 124 | 10% | 10% |
| · alleen utensils | 0,6% | 62 | 0% | 0% |
| · alleen deksel | 0,2% | 63 | 0% | 0% |
| Alleen gratis gift-regels ($0 cart) | 2,0% | 0 | 8% | 8% |
| E-gift card | 0 in de steekproef | | | |

Groepen: kookgerei 60%, set 23%, accessoire 15%, leeg 2%. Al klant: 11%. Cart van $300 of meer: 23,6%; daarvan 6,4% van alle carts losse pannen zonder set. Twee of meer pannen onder $300 (krijgt "Keep my one pan"): 1,5%.

### Added to Cart (288 profielen, eerste event)

| Categorie | Aandeel | Mediaan $ | Al klant |
| --- | --- | --- | --- |
| Pan Pro | 62,2% | 134 | 12% |
| Set of bundel | 17,4% | 599 | 12% |
| Snijplank | 4,9% | 89 | 71% |
| Deep pan | 3,8% | 142 | 9% |
| Gratis gift ($0, automatisch toegevoegd) als eerste event | 3,8% | 0 | 36% |
| Wok | 3,1% | 139 | 56% |
| Crêpe | 1,7% | 129 | 20% |
| Overige accessoires (molens, deksel, utensils) | 2,7% | | |
| Pizza steel | 0,3% | 129 | 0% |

Alle events (niet per profiel): **47% van de Added to Cart-events is een automatisch toegevoegde gratis gift** (Mystery Gift, e-book, Free Shipping, filterloting, prijs $0). Valuta: 69% USD, 31% lokaal (SGD 11%, AUD 8%, GBP, EUR, AED, CAD, HKD, NZD). 61 van 288 profielen voegden in één dag producten uit meer dan één categorie toe. Al klant: 18%.

### Viewed Product (452 profielen, eerste event)

Pan Pro 82,3% · set 7,7% · snijplank 2,4% · overige accessoires 2,6% · crêpe, wok, deep, pizza, roasting samen 4,8%. Al klant: 16% (snijplank en strips: 27 tot 100%).

### Placed Order (800 orders)

| Categorie | Aandeel | Mediaan $ | Al klant |
| --- | --- | --- | --- |
| Alleen Pan Pro | 46,6% | 136 | 10% |
| Set of bundel | 17,0% | 396 | 12% |
| Kookgerei + accessoire | 13,6% | 198 | 16% |
| · waarvan **pan + deksel in dezelfde order** | **11,6% van alle orders** | | |
| Alleen snijplank | 5,2% | 97 | 43% |
| Meerdere losse pannen | 3,2% | 279 | 23% |
| Set + accessoire | 3,1% | 678 | 28% |
| Wok / deep / crêpe / pizza / roasting (1 stuk) | 2,1 / 2,1 / 1,8 / 0,6 / 0,1% | ~130 tot 216 | 20 tot 100% |
| Molens / utensils / deksel / strips / overig | 1,8 / 1,2 / 0,4 / 0,2 / 0,6% | | |
| Schort | 1 van 800 orders (in een gemengde order) | | |

- Alleen accessoires: 9,5% van de orders; 6,0% eerste order, 3,1% van iemand die al kookgerei had.
- Enkel overig kookgerei (wok, deep, crêpe, pizza, roasting): 8,4%.
- Ordernummer: 1e order 83,4%, 2e 12,1%, 3e of later 4,4%.
- Verzendland: 62,8% US, **37,0% buiten de US**. `$currency_code` is altijd USD (shop money), dus valuta zegt bij orders en checkouts niets over het land.
- Gifts: Mystery Gift zit in 87,5% van de orders.
- E-gift card: 0 in 800 orders. Pot Set 6-Pcs en losse pots: 0 in de steekproef (wel $196k in 90 dagen volgens Shopify, dus de titel verschilt of het loopt via een andere listing; nakijken in Items van een echte order).

## Eventvelden die bruikbaar zijn voor splits (met voorbeelden)

| Metric | Veld | Voorbeeld | Bruikbaar voor | Niet bruikbaar |
| --- | --- | --- | --- | --- |
| Checkout Started | `Items` (lijst producttitels, inclusief de 4 gift-titels) | `["Mystery Gift","Plastic-Free Home E-Book","PFAS Water Purifier Giveaway (Weekly Draw Entry)","Free Shipping","Titanium Cutting Board (Anti-Microbial)"]` | Trigger split `Items contains-any [...]`, template `{% if 'Apron' in event.Items\|join:',' %}` | |
| | `$value` | `93.98` | Split set/pan (>= 300) | Uitschieters (1 event > $100k) |
| | `Item Count` | `5` (telt gifts mee) | | Niet voor "1 product" (gifts tellen mee) |
| | `$extra.line_items[]` → `title`, `variant_title`, `price`, `line_price`, `quantity`, `product.handle`, `product.images[].thumb_src`, `gift_card` | `title "Titanium Cutting Board (Anti-Microbial)"`, `variant_title "Versatile (15\" x 11\")"`, `price 89`, `handle titanium-cutting-board-v2` | Cart-weergave, maat in de template | `product.product_type` is **leeg** bij alle producten; `product.tags` alleen `bogos-gift, gorgias_do_not_recommend` bij gifts; `vendor` altijd SIRAATSKITCHEN |
| | `Collections` | 20 collecties incl. alle sale-collecties | | Te ruis (elk product zit in "Cookware" en in sales) |
| | `Customer Locale`, `presentment_currency` | `en-US`, `USD` | | Geen land; INT-checkouts staan ook op USD |
| Placed Order | `Items`, `$value`, `Item Count`, `Discount Codes`, `Source Name` | idem | P3, winback, U1, N1-splits | |
| | `$extra.line_items[].title/name/sku/price` | `name "Titanium Hammered Pan Set With Lids \| 6-Pcs"`, `price 349` | | product_type leeg |
| | `$extra.shipping_address.country_code` | `US` | Template: prijzen alleen bij US | |
| Added to Cart | `Product Name`, `Variant Name`, `Price` (lokale valuta), `$currency`, `Quantity`, `ProductID`, `URL` (myshopify-domein), `ImageURL`, `CompareAtPrice`, `_ip_country_code` | `Product Name "Stainless Steel Lid"`, `Variant Name "Chrome / Standard 28CM"`, `Price 39.0`, `$currency "EUR"` | Split op `Product Name`; trigger filter `Price > 0` | Bevat **alleen het toegevoegde product**, niet de hele cart. `Product Type` leeg. |
| Viewed Product | `Name`, `Price` (tekst: `"$69"` of `"119,00"`), `ProductID`, `URL`, `ImageURL`, `Categories` | `Name "Titanium Cutting Board (Anti-Microbial)"` | Split op `Name` | Geen valuta, geen type |

Titels (exact, zoals ze in `Items` en `Product Name` staan) voor de filters in 03-routing.md:
- Pan Pro: `Titanium Hammered Pan Pro Standard`, `... Large`, `... Small`, `... Mini`, `Titanium Pan Pro`
- Overig kookgerei: `Titanium Hammered Deep Pan Pro`, `Titanium Hammered Wok Pan Pro`, `Titanium Hammered Crêpe Pan Pro`, `Titanium Hammered Pizza Steel`, `Titanium Hammered Roasting Pan`
- Sets: `Titanium Hammered Pan Set With Lids | 6-Pcs`, `Titanium Hammered Cookware Set | 12-Pcs`, `Titanium Hammered Cookware Set Pro`, `Titanium Hammered Complete Edition`, `Titanium Hammered – Complete Edition`, `Full Hammered Pro Edition`, `The Just Everything Bundle | 34-Pcs`, `2 Pans + 2 Lids`, `12 pcs cookware set`, `Titanium-Hammerpfannenset mit Deckel | 6-teilig`
- Accessoires: `Stainless Steel Lid`, `Titanium Cutting Board (Anti-Microbial)`, `Titanium Cutting Board Bundle`, `Siraat Signature Apron (Azure|Moss|Ember|Oak)`, `Salt Mill`, `Pepper Mill`, `Salt & Pepper Mill Set`, `Titanium Utensil`, `Titanium Utensil Set Bundle`, `Titanium Chopsticks`, `Titanium Water Bottle`, `Cherry Wood Mini Trivet`, `Grill Press`, `Titanium Straws`, `Pizza Wheel`, `Rolling Knife Sharpener`, `Plastic-Free Dishwasher Sheets`, `E-Gift Card`
- Gift-regels (altijd negeren): `Mystery Gift`, `Plastic-Free Home E-Book`, `Free Shipping`, `PFAS Water Purifier Giveaway (Weekly Draw Entry)`, `Shipping Protection`
- In Added to Cart komt soms de variant mee in de naam: `Stainless Steel Lid - Chrome / Standard (11")`, `Titanium Hammered Wok Pan Pro - Large 12"`. Daarom in templates `in` (substring) gebruiken, en in Klaviyo-filters `contains` op de string.

Regel voor templates (één woordtest, getest op alle titels hierboven): **kookgerei = de tekst bevat `Pan`, `Pot`, `Pizza Steel`, `ookware`, `Everything` of `Pfanne`**. Geen enkele accessoiretitel bevat die woorden ("Pizza Wheel" niet, want de test is "Pizza Steel"; "Stainless Steel Lid" niet). Gift-regels ook niet.
