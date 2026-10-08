# 01 · Markten, valuta en productdata: tailoring per land

Stand 8 oktober 2026, fase 1 (alleen data en ontwerp). Alleen gelezen: Shopify Admin GraphQL (`markets`, `publishedInContext`, `contextualPricing`), ShopifyQL (365 dagen), siraatskitchen.com (`/products/<handle>.js` en PDP-HTML per land via de cookie `localization=<land>`) en Klaviyo (GET, steekproeven van 8 oktober). Geen template, flow of instelling gewijzigd. Productdata staat in `content/catalog/products.json` (uitleg in `content/catalog/README.md`).

Opdracht: `research/v5/00-feedback-floris.md`, sectie Checkout, punt "Internationaal".

## Kort

1. **De helft van de orders is niet-US.** US 45,3% van de orders (12 maanden), daarna UK 14,0%, AU 12,2%, SG 3,8%, CA 3,4%, AE 2,4%, HK 2,4%, NZ 2,1%, CH 1,8%, EU samen circa 8%. Een buitenlandse klant betaalt (bijna) altijd in de eigen valuta: in 200 recente orders klopt `presentment_currency` in 99% met het verzendland.
2. **US-only is nu hard bewezen** met `publishedInContext`: 12-delige set, de drie potten, Roasting Pan, "2 Pans + 2 Lids", "Just Everything Bundle 34-Pcs" en vier Shipbob-kopieën (Pan Pro Standard, Large, Mini, Lid (S)). Alle andere 55 actieve producten staan in elke markt.
3. **Let op: de oude bewijsvoering klopte niet.** `/en-au/` en `/en-gb/` bestaan niet: geen enkele markt heeft een eigen submap (ook de Pan Pro geeft daar 404). De markt volgt uit geolocatie of de cookie. Het bewijs komt nu uit Shopify zelf en uit `.js` met `localization=AU` (12-delige set: 404, Pan Pro: 200).
4. **Canada rekent duties in de checkout** (`ADD_DUTIES_AT_CHECKOUT`), alle andere markten niet. In 11 recente CA-orders stond wel 0 aan duties. "Duties paid" mag voor Canada pas na akkoord van Floris; tot dan alleen "Free shipping".
5. **Gift-waarden in lokale valuta** zijn hieronder per valuta uitgerekend uit de echte Shopify-prijzen (de gift-producten hebben eigen compare-at per markt). De drie gifts samen ($70) zijn: C$95, £55, €70, A$100, NZ$120, S$95, HK$560, AED 260. De filter ($450): C$620, £350, €410, A$660, NZ$820, S$590.
6. **Het browse-signaal in `build_template.py` is fout.** `'$' in event.Price` is ook waar voor AUD, CAD, SGD, NZD en HKD (de site toont die als "$194.00"). Viewed Product heeft geen valuta- of IP-veld; het profielland moet hier leidend zijn.
7. **`person.Country` bestaat waarschijnlijk niet.** In ruim 800 bekeken profielen staat geen eigenschap `Country`; het land staat in de locatie (`$country`, met "United States" en "US" door elkaar) en in een eigen veld `country_code` (ISO). C1 tot C4 vallen nu dus altijd terug op de valuta.
8. **Ontwerp:** één set macro's in `build_template.py` (`{{IF:AU}}`, `{{GIFTS:...}}`, `{{SIZE:28}}`, `{{PRICE:...}}`, `{{USONLY}}`) met per flowtype het betrouwbaarste signaal en een neutrale terugval (geen bedrag, maat "28 cm (11″)").

---

## 1. Shopify Markets (Admin GraphQL, 8 okt)

| Markt (handle) | Landen | Valuta | Prijzen | Duties | Eigen catalogus / publicatie | Opmerking |
|---|---|---|---|---|---|---|
| USA (`europa`) | US | USD (shopvaluta) | Prijslijst USD, 141 vaste prijzen, compare-at uit prijslijst | n.v.t. | Ja, publicatie USA | Handle heet "europa" (historisch), het is de US-markt |
| Canada | CA | CAD, afronding aan | Prijslijst CAD, 115 vaste prijzen | **ADD_DUTIES_AT_CHECKOUT**, belasting in de prijs | Twee catalogi: "Wereldwijd" en "Canada" | CA staat ook in de RoW-lijst |
| United Kingdom | GB | GBP | Prijslijst GBP, 119 vast | geen instelling | Ja | |
| EURO (`eu`) | AT, BE, BG, HR, CZ, EE, FI, FR, DE, GR, HU, IE, IT, LV, LU, NL, SK, SI, ES | EUR | Prijslijst "Italy", 113 vast | geen | Ja ("EU PRICING A-240726") | PT, DK, SE, PL, RO staan in RoW, niet in EURO |
| Germany | DE | EUR, afronding uit | (via EURO-prijslijst) | geen | Nee | Dubbel met EURO |
| Netherlands | NL | EUR | (via EURO) | geen | Nee | Dubbel met EURO |
| Australia | AU | AUD | Prijslijst AUD, 125 vast, compare-at NULLIFY | geen | Ja | |
| New Zealand | NZ | NZD | Prijslijst NZD, slechts 27 vast; compare-at NULLIFY | geen | Ja | Veel producten **zonder compare-at** in NZ (geen doorgestreepte prijs) |
| Singapore | SG | basis USD, lokale valuta aan | Prijslijst SGD, 104 vast | geen | Ja | |
| MIDDLE EAST | AE, KW, SA, BH, OM | basis USD, lokale valuta aan | Omgerekend (geen prijslijst) | geen | Nee | Klant ziet AED/SAR enz. |
| RoW (`wereldwijd`) | o.a. HK, MO, TW, TH, JP, KR, MY, ID, PH, MX, TR, CH, SE, DK, PL, PT, RO, NO, CN | basis USD, lokale valuta aan | Omgerekend | geen | Catalogus "Wereldwijd" | **Hongkong valt hier**: HKD, omgerekend en afgerond |
| Norway | NO | geen valuta-instelling: **USD** | | geen | Nee | |
| Shipping Costs To High | ZA, IN, EG en circa 150 kleinere landen | basis USD, lokale valuta aan | Omgerekend | geen | Nee | |

Taal: alle markten delen één web presence op `siraatskitchen.com` (Engels standaard, plus `/fr`, `/de`, `/it`, `/pl`, `/ar` als taal, niet als markt). Er bestaan **geen** submappen per markt (`/en-au/` enzovoort geeft voor elk product 404). `Customer Locale` in events is daardoor vooral `en-US` of `en-<land>` (geolocatie), geen echte taalkeuze. Mails blijven Engels.

Prijsaanpassing: alle prijslijsten staan op 0% aanpassing met vaste prijzen per product; landen zonder prijslijst (HK, AE, CH, SE, JP, NO) krijgen de USD-prijs omgerekend met Shopify-afronding (bv. Pan Pro Standard $144 = HK$1,147, AED 537, CHF 122).

## 2. US-only producten (bevestigd met data)

Bron: Admin `publishedInContext(country: X)` voor US, CA, GB, DE, NL, FR, AU, NZ, SG, HK, AE, CH, en storefront `.js` per land. "Alleen US" = `true` voor US en `false` voor alle elf andere landen.

| Product | Handle | Status | Bewijs |
|---|---|---|---|
| Titanium Hammered Cookware Set, 12-Pcs | `titanium-hammered-cookware-set` | US only | publishedInContext alleen US; `.js` 404 met AU, GB, CA enz. |
| 2 L pot (titel "Titanium Hammered Saucepan With Lid, 2-Qt") | `2-litre-titanium-hammered-pot-with-lid` | US only, voorraad 0 | idem |
| 3 L pot ("Pot With Lid, 3-Qt") | `3-litre-titanium-hammered-pot-with-lid` | US only | idem |
| 7,5 L pot ("Saucepan With Lid, 8-Qt") | `7-5-litre-titanium-hammered-pot-with-lid` | US only, voorraad 0 | idem |
| Titanium Hammered Roasting Pan | `titanium-hammered-roasting-pan` | US only | idem (eigenaar: "zeker weten" bevestigd) |
| 2 Pans + 2 Lids | `2-pans-and-2-lids` | US only, sinds 4 okt | idem |
| The Just Everything Bundle, 34-Pcs | `the-just-everything-bundle-34-pcs` | US only, sinds 5 okt | idem |
| Pan Pro Standard / Large / Mini (Shipbob-kopie) | `titanium-hammered-pan-pro-standard-copy`, `-large-copy`, `-mini-copy` | US only, tag `gorgias_do_not_recommend` | idem; nooit linken |
| Stainless Steel Lid (S) | `stainless-steel-lid-copy` | US only, niet gepubliceerd in de winkel | idem; nooit linken |

Gevolg voor mails: de 12-delige set, potten, roasting pan, 2+2 en 34-Pcs alleen binnen `{{USONLY}}`. Op de 6-Pcs-PDP staat de 12-delige set als keuze "12-piece set MOST VALUE"; buiten de US is die keuze er niet (PDP-tekst alleen in de US-versie gecontroleerd).

## 3. Klanten en orders per land en valuta

ShopifyQL, `FROM sales`, 365 dagen tot 8 okt 2026: **90.164 orders, $19,40 mln netto**.

| Land | Orders | % orders | Netto omzet (USD) | % omzet | AOV | Shopify-markt | Valuta klant |
|---|---|---|---|---|---|---|---|
| United States | 40.862 | 45.3% | $8.711.005 | 44.9% | $218 | USA | USD |
| United Kingdom | 12.639 | 14.0% | $2.489.042 | 12.8% | $206 | United Kingdom | GBP |
| Australia | 10.967 | 12.2% | $2.227.489 | 11.5% | $208 | Australia | AUD |
| Singapore | 3.424 | 3.8% | $738.728 | 3.8% | $220 | Singapore | SGD |
| Canada | 3.061 | 3.4% | $613.582 | 3.2% | $210 | Canada | CAD |
| United Arab Emirates | 2.189 | 2.4% | $605.143 | 3.1% | $282 | Middle East | AED |
| Hong Kong | 2.119 | 2.4% | $480.713 | 2.5% | $230 | RoW | HKD |
| New Zealand | 1.880 | 2.1% | $338.807 | 1.7% | $183 | New Zealand | NZD |
| Switzerland | 1.629 | 1.8% | $417.487 | 2.2% | $259 | RoW | CHF |
| Italy | 1.473 | 1.6% | $369.078 | 1.9% | $260 | EURO | EUR |
| Germany | 1.300 | 1.4% | $296.837 | 1.5% | $240 | Germany / EURO | EUR |
| France | 859 | 1.0% | $196.357 | 1.0% | $237 | EURO | EUR |
| Ireland | 727 | 0.8% | $152.672 | 0.8% | $213 | EURO | EUR |
| Sweden | 507 | 0.6% | $114.070 | 0.6% | $239 | RoW | SEK |
| Spain | 457 | 0.5% | $116.382 | 0.6% | $269 | EURO | EUR |
| Portugal | 457 | 0.5% | $111.017 | 0.6% | $254 | RoW | EUR |
| Austria | 452 | 0.5% | $105.593 | 0.5% | $241 | EURO | EUR |
| Belgium | 380 | 0.4% | $90.029 | 0.5% | $241 | EURO | EUR |
| Taiwan | 365 | 0.4% | $92.951 | 0.5% | $267 | RoW | TWD |
| Netherlands | 356 | 0.4% | $75.170 | 0.4% | $220 | Netherlands / EURO | EUR |
| Saudi Arabia | 348 | 0.4% | $129.580 | 0.7% | $379 | Middle East | SAR |
| Romania | 291 | 0.3% | $70.473 | 0.4% | $261 | RoW | RON |
| Japan | 285 | 0.3% | $66.511 | 0.3% | $242 | RoW | JPY |
| Mexico | 270 | 0.3% | $77.874 | 0.4% | $301 | RoW | USD/MXN |
| Greece | 251 | 0.3% | $64.352 | 0.3% | $263 | EURO | EUR |
| Slovenia | 247 | 0.3% | $61.145 | 0.3% | $254 | EURO | EUR |
| Denmark | 242 | 0.3% | $56.574 | 0.3% | $246 | RoW | DKK |
| Finland | 231 | 0.3% | $48.303 | 0.2% | $217 | EURO | EUR |
| Poland | 197 | 0.2% | $47.593 | 0.2% | $248 | RoW | PLN |
| Norway | 173 | 0.2% | $39.327 | 0.2% | $234 | Norway | USD |
| overige landen | 1.526 | 1.7% | | | | | |

Groepen: US 45.3%, niet-US 54.7%. EURO-landen in de top 30 samen 6.733 orders (7.5%). De niet-US-landen hebben een gelijke of hogere AOV dan de US (behalve NZ).

Valuta: ShopifyQL kent geen valuta-dimensie en Klaviyo rekent alles om naar USD (`$currency_code` altijd USD). Steekproef 200 Placed Orders (7 en 8 okt): `presentment_currency` USD 53%, AUD 17,5%, SGD 9,5%, CAD 5,5%, GBP 4,5%, EUR 3,5%, AED 2,5%, NZD 1,5%, HKD 1%, CHF, SAR, MYR. In 198 van 200 orders hoort de valuta bij het verzendland (uitzonderingen: CH en MX in USD). Over 12 maanden is de verdeling dus ongeveer gelijk aan de landentabel: circa 47% USD (US plus NO en een deel RoW), 14% GBP, 12% AUD, 8% EUR, 4% SGD, 3% CAD, 2 tot 3% AED, 2% HKD, 2% NZD, 2% CHF.

## 4. Welk Klaviyo-veld geeft land en valuta het best, per flowtype

Steekproeven 8 okt: 200 Placed Order, 300 Checkout Started, 400 Added to Cart (QXcV8K), 400 Viewed Product (XNtYMB), 100 nieuwste profielen; telkens met het profiel erbij.

| Flowtype (trigger) | Beste signaal | Dekking | Tweede signaal | Wat niet werkt |
|---|---|---|---|---|
| Post-purchase, winback, VIP, anniversary, UGC (Placed Order) | `event.extra.shipping_address.country_code` (ISO) | 100% | `event.extra.presentment_currency` (100%, 99% consistent met land) | `$currency_code` (altijd USD), profiel-`locale` |
| Checkout (Checkout Started) | `event.extra.presentment_currency` | 100% | `event|lookup:'Customer Locale'` (100%, maar 11 van 30 AUD-checkouts hebben `en-US`); profielland (57%) | `shipping_address` (2%), `$currency_code` |
| Cart (Added to Cart) | `event|lookup:'_ip_country_code'` | 100%, 93% gelijk aan profielland | profielland (96%); `$currency` alleen als bevestiging | `$currency` alleen: 18 van 32 AU-adds staan op USD; `Price` = 0 bij gift-adds (55% van de events) |
| Browse (Viewed Product) | profielland `person|lookup:'$country'` | 88% | prijsnotatie in `event.Price`: "£", "€", "Dhs.", "CHF" = zeker niet-US; "$x.xx" met decimalen = AUD/CAD/SGD/HKD/NZD; "$x" zonder decimalen = USD-markt | `'$' in event.Price` (huidige US-regel): ook waar voor AUD, CAD, SGD, NZD, HKD |
| Welcome, sunset, site, campagnes (alleen profiel) | profielland `person|lookup:'$country'` | 68% van nieuwe aanmeldingen | eigen veld `person.country_code` (ISO, 47 tot 72%), `$phone_number_region` (58%) | `locale` (65% "en", zegt niets) |

Profielland: de waarde is soms de naam ("United States", "Australia") en soms de ISO-code ("US", "AU", "CA", "AE"). Elke vergelijking moet beide vormen kennen. `person.Country` (zoals in c1, c3-p, c4, c4-nocode, k2-new) is een eigen eigenschap die in geen enkel bekeken profiel voorkomt: die tak valt nu altijd terug op de valuta. **[CONTROLEREN in Klaviyo-preview]** de exacte syntaxis `person|lookup:'$country'` op een echt profiel voordat de helper live gaat.

## 5. Wat de mail per markt toont

| Markt | Herkenning (zie 4) | Bedragen | Maten | Nooit tonen | Verzending en duties | Spelling |
|---|---|---|---|---|---|---|
| **US** | land US / "United States", valuta USD | USD met "$" | inch: `11″` (cm mag tussen haakjes in specs) | | "Free shipping", levertijd 6 tot 10 dagen; Shop Pay Installments en Affirm mogen | US |
| **CA** | CA / "Canada", CAD | `C$` (Shopify toont "$", in mail altijd C$ om verwarring te voorkomen) | `28 cm` | US-only | "Free shipping". **Geen "duties paid"** tot Floris het bevestigt: de markt staat op duties in de checkout. Levertijd: niet apart in het beleid (Rest of World, 6 tot 10 dagen) | US-spelling is gangbaar, woorden zonder variant kiezen |
| **UK** | GB, GBP | `£` | `28 cm` | US-only | "Free shipping, no import duties" (besluit 7 okt), 6 tot 10 dagen | UK |
| **EU** (EURO-lijst) | ISO in EU-lijst, EUR | `€` | `28 cm` | US-only | "Free shipping, no import duties", 6 tot 10 dagen (IE en DK 8 tot 14) | UK |
| **AU** | AU, AUD | `A$` | `28 cm` | US-only | "Free shipping, no import duties", 6 tot 10 dagen | UK/AU |
| **NZ** | NZ, NZD | `NZ$` | `28 cm` | US-only | idem; let op: veel NZ-producten hebben **geen compare-at**, dus geen doorgestreepte prijs tonen | UK |
| **SG** | SG, SGD | `S$` | `28 cm` | US-only | idem, 6 tot 8 dagen | UK |
| **HK** | HK, HKD | `HK$` (omgerekend, Shopify rondt af) | `28 cm` | US-only | idem | UK |
| **Midden-Oosten** | AE, SA, KW, BH, OM, QA; AED/SAR | geen bedragen, of AED als we het per stuk controleren (omgerekend) | `28 cm` | US-only | "Free shipping"; duties-belofte volgt het besluit voor INT | UK |
| **Rest** (o.a. CH, SE, JP, TW, TH, MX, NO, PT, DK, PL) | alles wat overblijft | **geen bedragen** (USD, CHF, SEK, JPY, gemengd) | `28 cm` | US-only | "Free shipping" | UK |
| **Onbekend** (geen enkel signaal) | | geen bedragen | `28 cm (11″)` | US-only | "Free worldwide shipping" | woorden zonder variant |

Regels die overal gelden:
- **Bedrag of geen bedrag.** Een bedrag staat alleen in de valuta van de markt, uit `content/catalog/products.json`. Weet de mail de markt niet zeker: zin zonder bedrag ("4 free gifts with every order", "Pan Pro, 11″ (28 cm)").
- **Kortingsbedragen** ("$120.60 with HI10") alleen waar de prijs vast staat in de prijslijst (US, CA, UK, EU, AU, NZ, SG). Voor HK, ME en Rest alleen "10% off".
- **Compare-at** alleen als die in die markt bestaat (NZ en een deel van AU/SG hebben er geen).
- **Spelling:** de mails kiezen bij voorkeur woorden zonder US/UK-variant. Waar het niet anders kan (colour/color, favourite/favorite, flavour/flavor, personalised/personalized): US-vorm voor US, UK-vorm voor de rest. Geen eigen spellingtakken in de flows bouwen; dit is een schrijfregel voor de copy-agent.
- **"Free Express Shipping from the US"** staat op elke PDP, ook voor bezoekers buiten de US, naast "Delivery from your local warehouse". Mails nemen "from the US" niet over buiten de US. **[VRAAG FLORIS]** of de PDP-regel per markt moet.

## 6. Gift-waarden per valuta

Bron: de gift-producten in Shopify (`free-shipping-sca_clone_freegift`, `the-green-clean-e-guide-sca_clone_freegift`, `dishwashing-detergent-sheets-fresh-lemon-sca_clone_freegift`, `entry-to-win-your-order-sca_clone_freegift`) hebben per markt een eigen compare-at. Waar die ontbreekt: USD-waarde maal de wisselkoers die Shopify zelf gebruikt (afgeleid uit de onafgeronde E-Gift Card-prijzen), afgerond op 5 (op 10 voor HKD/AED, op 50 voor SEK, op 100 voor JPY). De mail toont het afgeronde getal.

| Valuta | Markt | Free shipping | E-book | Mystery gift | Gifts samen (afgerond) | PFAS-filter (kans) | Bron |
|---|---|---|---|---|---|---|---|
| USD | US (ook NO, RoW-USD) | $15 | $30 | $25 | **$70** | $450 | ship en e-book: Shopify compare-at; mystery en filter: koers |
| CAD | CA | C$20 | C$40 | C$35 | **C$95** | C$620 | ship en e-book: Shopify compare-at; mystery en filter: koers |
| GBP | UK | £10 | £25 | £20 | **£55** | £350 | ship en e-book: Shopify compare-at; mystery en filter: koers |
| EUR | EU | €15 | €30 | €25 | **€70** | €410 | ship en e-book: Shopify compare-at; mystery en filter: koers |
| AUD | AU | A$20 | A$45 | A$35 | **A$100** | A$660 | ship en e-book: Shopify compare-at; mystery en filter: koers |
| NZD | NZ | NZ$25 | NZ$50 | NZ$45 | **NZ$120** | NZ$820 | ship en e-book: Shopify compare-at; mystery en filter: koers |
| SGD | SG | S$20 | S$40 | S$35 | **S$95** | S$590 | ship en e-book: Shopify compare-at; mystery en filter: koers |
| HKD | HK | HK$120 | HK$239 | HK$200 | **HK$560** | HK$3,600 | ship en e-book: Shopify compare-at; mystery en filter: koers |
| AED | AE (ME) | AED 56 | AED 112 | AED 90 | **AED 260** | AED 1,680 | ship en e-book: Shopify compare-at; mystery en filter: koers |
| CHF | CH | CHF 13 | CHF 26 | CHF 20 | **CHF 60** | CHF 380 | ship en e-book: Shopify compare-at; mystery en filter: koers |

Koersen die Shopify vandaag gebruikt (uit de E-Gift Card $25): GBP 0,773 · EUR 0,912 · AUD 1,469 · NZD 1,816 · SGD 1,301 · HKD 7,965 · AED 3,728 · CHF 0,846; CAD 1,374 is de mediaan van de vaste CAD-prijzen. Shopify zelf is niet consequent: free shipping is £10 maar $15 (koers zou £12 geven), e-book £25 tegen $30. De mail volgt de Shopify-compare-at, zodat de klant in de checkout hetzelfde bedrag ziet.

Advies per markt: **bedrag tonen** voor US, CA, UK, EU, AU, NZ, SG (vaste prijslijst, en het gift-blok in de checkout toont dezelfde valuta). **HK en AE**: bedrag mag (Shopify rekent om), maar de afronding kan per dag een paar HK$ of AED schuiven; toon daarom liever "4 free gifts". **CH, SE, JP, NO en Rest**: geen bedrag.

## 7. Prijzen kernproducten per markt (8 okt, fall sale)

Prijs / compare-at zoals Shopify ze in die markt toont. "geen" = geen compare-at in die markt.

| Product | US (USD) | CA (CAD) | GB (GBP) | EU (EUR) | AU (AUD) | NZ (NZD) | SG (SGD) | HK (HKD) | AE (AED) |
|---|---|---|---|---|---|---|---|---|---|
| Pan Pro Mini 8″ / 20 cm | 99 / 330 | 177 / 354 | 109 / 218 | 129 / 258 | 194 / 388 | 235 / 470 | 179 / 358 | 1028 / 2056 | 481 / 962 |
| Pan Pro Small 10″ / 26 cm | 137 / 274 | 219 / 438 | 119 / 238 | 134 / 268 | 219 / 438 | 269 / 538 | 199 / 398 | 1092 / 2183 | 511 / 1022 |
| Pan Pro Standard 11″ / 28 cm | 144 / 288 | 224 / 448 | 124 / 248 | 139 / 278 | 224 / 448 | 274 / 548 | 204 / 408 | 1147 / 2294 | 537 / 1074 |
| Pan Pro Large 12″ / 30 cm | 149 / 298 | 234 / 468 | 129 / 258 | 144 / 288 | 234 / 468 | 284 / 568 | 214 / 428 | 1187 / 2374 | 556 / 1111 |
| 6-Pcs set (fall sale, 3 pannen + 3 deksels) | 299 / 598 | 449 / 898 | 249 / 498 | 279 / 558 | 449 / 898 | 549 / 1098 | 409 / 818 | 2382 / 4764 | 1115 / 2230 |
| Stainless Steel Lid (elke maat) | 59 / 110 | 69 / 140 | 29 / 55 | 39 / 80 | 54 / 100 | 108 / geen | 39 / 80 | 470 / 877 | 220 / 411 |
| Wok Pan Pro Standard 28 cm | 134 / 439 | 194 / 639 | 104 / 339 | 119 / 389 | 194 / 639 | 239 / 779 | 174 / 569 | 1068 / 3497 | 500 / 1637 |
| Deep Pan Pro Standard 24 cm | 134 / 439 | 194 / 639 | 104 / 339 | 119 / 389 | 194 / 639 | 239 / 779 | 174 / 569 | 1068 / 3497 | 500 / 1637 |
| Crêpe Pan Pro 28 cm | 129 / 210 | 179 / 250 | 99 / 145 | 139 / 185 | 199 / 285 | 253 / geen | 164 / 235 | 1108 / 1434 | 519 / 671 |
| Complete Edition | 399 / 1330 | 649 / 1250 | 387 / 700 | 469 / 790 | 734 / 1500 | 900 / geen | 699 / 1200 | 3943 / 7169 | 1846 / 3355 |
| Cookware Set Pro | 379 / 1263 | 665 / 1200 | 449 / 750 | 449 / 765 | 699 / 1270 | 870 / geen | 699 / 1300 | 3816 / 6930 | 1786 / 3244 |
| Full Hammered Pro Edition | 779 / 1760 | 1099 / 2000 | 649 / 1250 | 699 / 1300 | 1145 / 2400 | 1452 / geen | 1099 / 2150 | 6365 / 11940 | 2979 / 5588 |
| Pan Pro Duo | 249 / 570 | 314 / 790 | 177 / 441 | 199 / 300 | 337 / geen | 416 / geen | 298 / geen | 1825 / 4541 | 854 / 2125 |
| Cutting Board Medium | 79 / 160 | 107 / 215 | 59 / 120 | 84 / 125 | 114 / 228 | 144 / geen | 103 / geen | 630 / 1116 | 295 / 522 |
| Utensil Set Bundle | 79 / 320 | 210 / 280 | 67 / 150 | 70 / 199.95 | 120 / 305 | 271 / geen | 190 / 260 | 1187 / 1593 | 556 / 746 |
| Signature Apron | 54 / 100 | 69 / 110 | 44 / 70 | 49 / 80 | 79 / 135 | 89 / geen | 74 / 120 | 391 / 638 | 183 / 299 |
| 12-Pcs set (US only) | 599 / 1186 | niet te koop | niet te koop | niet te koop | niet te koop | niet te koop | niet te koop | niet te koop | niet te koop |
| Roasting Pan (US only) | 199 / 250 | niet te koop | niet te koop | niet te koop | niet te koop | niet te koop | niet te koop | niet te koop | niet te koop |
| Just Everything 34-Pcs (US only) | 1499 / 4342 | niet te koop | niet te koop | niet te koop | niet te koop | niet te koop | niet te koop | niet te koop | niet te koop |

Valt op: US-prijzen op 8 okt zijn Mini $99, Small $137, Standard $144, Large $149 (compare-at steeds het dubbele, behalve Mini $330). De mails rekenen nog met $129 / $127 / $134 / $139 en de 6-Pcs voor $349. De fall sale-set (6-Pcs $299, compare-at $598) is Mini 8″ + Small 10″ + Large 12″ met drie deksels; de PDP noemt het "Buy 2 get 4 free": Small en Large betaald, Mini en drie deksels gratis. De Wok- en Deep-varianten heten op de site "Mini 9″" en "Standard 9.4″", in Shopify "Mini 24CM" en "Standard 24CM".

## 8. Logica: één helperblok in `build_template.py`

Voorstel (nog niet gebouwd; templates niet gewijzigd). Het script kent de flow al uit de map (`USCOND`). Daar komt één tabel `SIG` met per flowtype de signalen, en een paar macro's die bij het bouwen uitklappen tot gewone Django-`if`s. Zo staat de landlogica op één plek en blijft de bron leesbaar.

```python
# --- Markten (01-markten.md, 8 okt 2026) -------------------------------------------
EU='AT|BE|BG|HR|CZ|EE|FI|FR|DE|GR|HU|IE|IT|LV|LU|NL|SK|SI|ES|CY|MT|PT'   # ISO met | als scheiding: 'cc in EU' is veilig
ME='AE|SA|KW|BH|OM|QA'
PC="person|lookup:'$country'"            # [CONTROLEREN in preview]; waarden 'United States' of 'US'
PCC="person.country_code"                  # eigen ISO-veld, 47 tot 72% gevuld
NAMES={'US':('United States','US'),'CA':('Canada','CA'),'GB':('United Kingdom','GB'),'AU':('Australia','AU'),
       'NZ':('New Zealand','NZ'),'SG':('Singapore','SG'),'HK':('Hong Kong','HK')}
def pc_is(m): return '('+' or '.join("%s == '%s'"%(PC,n) for n in NAMES[m])+" or %s == '%s')"%(PCC,m)
CUR={'US':'USD','CA':'CAD','GB':'GBP','EU':'EUR','AU':'AUD','NZ':'NZD','SG':'SGD','HK':'HKD'}
SIG={  # per flowmap: hoe herken je markt m
 'order':   lambda m: ("event.extra.shipping_address.country_code in '%s'"%EU if m=='EU' else
                       "event.extra.shipping_address.country_code in '%s'"%ME if m=='ME' else
                       "event.extra.shipping_address.country_code == '%s'"%m),
 'checkout':lambda m: ("event.extra.presentment_currency in 'AED|SAR|KWD|BHD|OMR|QAR'" if m=='ME' else
                       "(event.extra.presentment_currency == 'USD' and (not %s or %s))"%(PC,pc_is('US')) if m=='US' else
                       "event.extra.presentment_currency == '%s'"%CUR[m]),
 'cart':    lambda m: ("event|lookup:'_ip_country_code' in '%s'"%(EU if m=='EU' else ME) if m in ('EU','ME') else
                       "event|lookup:'_ip_country_code' == '%s'"%m),
 'profile': lambda m: ("%s in '%s'"%(PCC,EU if m=='EU' else ME) if m in ('EU','ME') else pc_is(m)),
}
FLOWSIG={'post-purchase':'order','winback':'order','vip':'order','anniversary':'order','ugc':'order',
         'checkout':'checkout','cart':'cart','browse':'profile','welcome':'profile','sunset':'profile','site':'profile'}
# Browse-extra: prijsnotatie als terugval wanneer er geen profielland is
BROWSE_INT="('£' in event.Price or '€' in event.Price or 'Dhs' in event.Price or 'CHF' in event.Price or ('$' in event.Price and '.' in event.Price))"

def mcond(m,flow):
    s=SIG[FLOWSIG[flow]]
    if m=='KNOWN':   # markt met zekerheid bekend (anders neutrale tekst)
        return '('+' or '.join(s(x) for x in ('US','CA','GB','EU','AU','NZ','SG','HK'))+')'
    if m=='NOTUS':
        return 'not '+s('US') if FLOWSIG[flow]!='profile' else '(%s and not %s)'%(PC,pc_is('US'))
    return s(m)
# {{IF:AU}} {{ELIF:EU}} {{ELSE}} {{ENDIF}}   {{USONLY}}...{{/USONLY}}
# {{SIZE:28}}      -> US: 11″ | bekende niet-US markt: 28 cm | onbekend: 28 cm (11″)
# {{GIFTS:total}}  -> "$70" / "A$100" / ... ; onbekende markt: de tekst na de |, bv. {{GIFTS:total|4 free gifts}}
# {{PRICE:<handle>[/<variant-id>]}} -> lokale prijs uit content/catalog/products.json, alleen markten met vaste prijslijst
```

Uitklappen (voorbeeld voor de map `checkout`):

```django
{{SIZE:28}}
=> {% if event.extra.presentment_currency == 'USD' and (not person|lookup:'$country' or ...) %}11″{% elif event.extra.presentment_currency == 'CAD' or ... %}28 cm{% else %}28 cm (11″){% endif %}

{{GIFTS:total|4 free gifts}}
=> {% if <US> %}$70 in gifts{% elif <CA> %}C$95 in gifts{% elif <GB> %}£55 in gifts{% elif <EU> %}€70 in gifts{% elif <AU> %}A$100 in gifts{% elif <NZ> %}NZ$120 in gifts{% elif <SG> %}S$95 in gifts{% else %}4 free gifts{% endif %}
```

Afspraken voor de bouw:
1. `USCOND` blijft bestaan maar wordt `mcond('US', flow)`; `productcard us="1"` gebruikt dezelfde functie. De browse-regel `'$' in event.Price` vervalt (fout, zie 4).
2. Een `{{GIFTS}}`-macro heeft altijd een tekst-terugval; een mail mag nooit "$70" tonen aan een onbekende markt.
3. `{{USONLY}}` wikkelt elke kaart, link en zin over de 12-delige set, potten, Roasting Pan, 2+2 en 34-Pcs. Binnen `{% else %}` komt het INT-alternatief (meestal de 6-Pcs-set).
4. De gift-blokken (`partials/blocks/gifts.html`, `cart.html` default, `DEF['gifts']`) krijgen `{{GIFTS:ship}}`, `{{GIFTS:ebook}}`, `{{GIFTS:mystery}}`, `{{GIFTS:filter}}` en `{{GIFTS:total}}` in plaats van vaste bedragen.
5. Testen: de bestaande `research/tailoring/test` uitbreiden met één testprofiel per markt (US, AU, CA, GB, EU, onbekend) en per flowtype één event; Klaviyo-preview bevestigt de `$country`-syntaxis.
6. Het script leest `content/catalog/products.json`; na elke prijswijziging in Shopify eerst de catalogus vernieuwen (`content/catalog/README.md`), dan bouwen.

## 9. Waar USD, inches en US-only producten nu hard in de templates staan

Grep over `klaviyo/templates/v3/**` en `klaviyo/templates/partials/**` (bronbestanden, geen `.klaviyo.html` of previews) en `scripts/build_template.py`. "US-guard" = staat al binnen een US-voorwaarde, "INT-tak" = in de `else` daarvan, "ongeguard" = ziet iedereen, "routeringslogica" = alleen een `if` op de producttitel (bv. het woord "set" of "pot" voor een product dat de klant zelf bekeek; mag blijven). Totaal 295 regels.

| Soort | ongeguard | US-guard | INT-tak | routeringslogica |
|---|---|---|---|---|
| USD-bedrag | 120 | 66 | 0 | 0 |
| Maat in inch | 44 | 5 | 2 | 0 |
| US-only product | 13 | 2 | 0 | 19 |
| Verzend-/duties-/betaalbelofte | 13 | 11 | 0 | 0 |

Grootste brokken (ongeguard, ziet iedereen):
- **Gift-bedragen** "$70 in gifts", "$15 / $25 / $30 / $450 value": `partials/blocks/gifts.html` (vier waarden), `DEF['gifts']`, `DEF['cart']` en `codebar`-aanroepen in vrijwel elke flow. Eén macro `{{GIFTS:...}}` lost het grootste deel op.
- **6-Pcs $349 en "About $116 a pan"**: c3-p, a1, a2, w4-us, n2, n2-nocode, r2, r2-nocode, r2-vip, r2-vip-nocode; prijs is nu $299 (fall sale).
- **Pan Pro-prijzen** "$134", "$439", "$120.60 with HI10" in 28 bronbestanden (alle browse- en cart-mails, w1-a/b, w4-us, w5, a1, a2, c3-acc, p3-accessory/apron, n2, r1-acc, r1-set, r2), deels al achter een US-voorwaarde; de prijs is nu $144.
- **Inch-maten** (11″, 8″, 10″, 12″, "11-inch") in a1, a2, w4-int (de INT-variant!), w1-a/b, c3-p, p3-pan, p3-set, p3-accessory, n2, r2, en de blokken `about`, `goes`, `goes1`, `label`. w4-int en a1 zetten wel cm tussen haakjes.
- **US-only** ongeguard: de set-kaart in `c4-us` en `c4-us-nocode` (oude US-tak, vervalt met de samenvoeging), "pots" in de review-quote van c3-s, en de woorden "pot", "Roasting" in `about`/`goes`/`label`/`noun`-blokken (alleen zichtbaar als de klant dat product zelf had, dus US).
- **Duties** in `c4-int` en `c4-int-nocode` zonder voorwaarde (ok voor INT, maar fout voor Canada zolang dat niet bevestigd is).

Volledige lijst per bestand (regelnummer, wat, status, tekst):

- `partials/blocks/about.html`: r.2 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting; r.3 USD-bedrag (ongeguard): $200, $25; r.3 Maat in inch (ongeguard): 10.6″, 10″, 11″, 12″, 2.4″, 2.8″; r.3 US-only product (routeringslogica): 12 pcs, 12-PIECE, 12-Pcs, JUST EVERYTHING, Roasting, pot
- `partials/blocks/gifts.html`: r.11 USD-bedrag (ongeguard): $15 value; r.17 USD-bedrag (ongeguard): $30 value; r.26 USD-bedrag (ongeguard): $25 value; r.32 USD-bedrag (ongeguard): $450 value
- `partials/blocks/goes.html`: r.2 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting; r.3 Maat in inch (ongeguard): 10″, 11″, 12″, 3.5″, 8″; r.3 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot
- `partials/blocks/goes1.html`: r.2 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting; r.3 Maat in inch (ongeguard): 10″, 11″, 3.5″, 8″; r.3 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot
- `partials/blocks/label.html`: r.1 Maat in inch (ongeguard): 10″, 11″, 12″; r.1 US-only product (routeringslogica): 12 pcs, 12-PIECE, 12-Pcs, JUST EVERYTHING, Roasting
- `partials/blocks/noun.html`: r.1 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot
- `partials/blocks/pick.html`: r.1 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot
- `v3/anniversary/n1.html`: r.48 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot; r.68 USD-bedrag (US-guard): $53.10, $59; r.78 USD-bedrag (US-guard): $62.10, $69; r.87 USD-bedrag (US-guard): $107.10, $119; r.92 USD-bedrag (ongeguard): $70 in gifts
- `v3/anniversary/n2-nocode.html`: r.42 USD-bedrag (ongeguard): $70 IN GIFTS; r.70 USD-bedrag (US-guard): $59; r.78 Maat in inch (ongeguard): 11″; r.80 USD-bedrag (US-guard): $134; r.88 USD-bedrag (ongeguard): $116; r.89 USD-bedrag (US-guard): $349; r.98 USD-bedrag (ongeguard): $70 in gifts
- `v3/anniversary/n2.html`: r.58 USD-bedrag (ongeguard): $70 in gifts; r.71 USD-bedrag (US-guard): $53.10, $59; r.79 Maat in inch (ongeguard): 11″; r.81 USD-bedrag (US-guard): $120.60, $134; r.89 USD-bedrag (ongeguard): $116; r.90 USD-bedrag (US-guard): $314.10, $349
- `v3/browse/b1-acc.html`: r.60 USD-bedrag (US-guard): $439; r.80 USD-bedrag (ongeguard): $450, $70 in gifts
- `v3/browse/b1.html`: r.60 USD-bedrag (US-guard): $439; r.64 USD-bedrag (US-guard): $120.60; r.70 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot; r.81 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot; r.85 USD-bedrag (ongeguard): $450, $70 in gifts; r.87 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot
- `v3/browse/b2-clicked-nocode.html`: r.39 USD-bedrag (ongeguard): $70 IN GIFTS; r.60 USD-bedrag (US-guard): $439; r.64 USD-bedrag (ongeguard): $70 in gifts; r.70 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot; r.81 USD-bedrag (US-guard): $134, $439; r.81 Maat in inch (US-guard): 11″; r.82 USD-bedrag (ongeguard): $15 value; r.83 USD-bedrag (ongeguard): $30 value; r.84 USD-bedrag (ongeguard): $25 value; r.87 USD-bedrag (US-guard): $134, $509; r.89 USD-bedrag (ongeguard): $450; r.92 USD-bedrag (ongeguard): $450, $70 in gifts; r.95 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot; r.99 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot
- `v3/browse/b2-clicked.html`: r.60 USD-bedrag (US-guard): $439; r.64 USD-bedrag (US-guard): $120.60; r.83 USD-bedrag (US-guard): $134, $439; r.83 Maat in inch (US-guard): 11″; r.84 USD-bedrag (ongeguard): $15 value; r.85 USD-bedrag (ongeguard): $30 value; r.86 USD-bedrag (ongeguard): $25 value; r.89 USD-bedrag (US-guard): $13.40; r.90 USD-bedrag (US-guard): $120.60, $509; r.92 USD-bedrag (ongeguard): $450; r.95 USD-bedrag (ongeguard): $450, $70 in gifts
- `v3/browse/b2-notclicked.html`: r.60 USD-bedrag (US-guard): $439; r.64 USD-bedrag (US-guard): $120.60; r.70 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot; r.105 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot; r.108 USD-bedrag (ongeguard): $450, $70 in gifts; r.110 US-only product (routeringslogica): 12 pcs, 12-Pcs, Roasting, pot
- `v3/cart/k1-acc.html`: r.60 USD-bedrag (US-guard): $439; r.80 USD-bedrag (ongeguard): $450, $70 in gifts
- `v3/cart/k1.html`: r.60 USD-bedrag (US-guard): $439; r.64 USD-bedrag (US-guard): $120.60; r.75 USD-bedrag (ongeguard): $450, $70 in gifts
- `v3/cart/k2-new.html`: r.60 USD-bedrag (US-guard): $439; r.64 USD-bedrag (US-guard): $120.60; r.78 USD-bedrag (US-guard): $30; r.79 USD-bedrag (US-guard): $450; r.80 Maat in inch (US-guard): 11″; r.81 USD-bedrag (US-guard): $134; r.85 Verzend-/duties-/betaalbelofte (US-guard): Affirm, Shop Pay; r.87 USD-bedrag (ongeguard): $134, $30; r.87 Maat in inch (ongeguard): 11″; r.111 USD-bedrag (ongeguard): $450, $70 in gifts
- `v3/cart/k2-returning.html`: r.60 USD-bedrag (US-guard): $439; r.64 USD-bedrag (US-guard): $120.60; r.85 USD-bedrag (ongeguard): $53.10, $59; r.86 USD-bedrag (ongeguard): $119; r.88 USD-bedrag (ongeguard): $450, $70 in gifts
- `v3/cart/k3-nocode.html`: r.39 USD-bedrag (ongeguard): $70 IN GIFTS; r.60 USD-bedrag (US-guard): $439; r.64 USD-bedrag (ongeguard): $70 in gifts; r.92 USD-bedrag (ongeguard): $450, $70 in gifts
- `v3/cart/k3.html`: r.60 USD-bedrag (US-guard): $439; r.64 USD-bedrag (US-guard): $120.60; r.87 USD-bedrag (ongeguard): $450, $70 in gifts
- `v3/checkout/c1.html`: r.47 USD-bedrag (ongeguard): $70 in gifts; r.56 Verzend-/duties-/betaalbelofte (US-guard): Affirm, Shop Pay; r.59 USD-bedrag (ongeguard): $70 in gifts
- `v3/checkout/c2-acc.html`: r.77 USD-bedrag (ongeguard): $70 in gifts
- `v3/checkout/c2.html`: r.74 USD-bedrag (ongeguard): $70 in gifts
- `v3/checkout/c3-acc.html`: r.59 USD-bedrag (US-guard): $120.60, $134, $439; r.59 Maat in inch (US-guard): 11″; r.61 Maat in inch (INT-tak): 11″; r.68 USD-bedrag (ongeguard): $70 in gifts
- `v3/checkout/c3-p.html`: r.33 USD-bedrag (ongeguard): $116; r.60 USD-bedrag (ongeguard): $154; r.66 USD-bedrag (ongeguard): $116; r.67 USD-bedrag (ongeguard): $349; r.72 Verzend-/duties-/betaalbelofte (US-guard): Affirm, Shop Pay; r.74 USD-bedrag (ongeguard): $104.70, $314.10, $349; r.74 Maat in inch (ongeguard): 10″, 12″, 8″; r.81 USD-bedrag (US-guard): $15, $25, $30, $34.90, $349; r.82 USD-bedrag (US-guard): $314.10; r.83 USD-bedrag (US-guard): $104.70; r.85 USD-bedrag (US-guard): $450; r.102 Maat in inch (ongeguard): 11-inch
- `v3/checkout/c3-s.html`: r.62 USD-bedrag (ongeguard): $70 in gifts; r.64 US-only product (ongeguard): pots
- `v3/checkout/c4-int-nocode.html`: r.38 USD-bedrag (ongeguard): $70 IN GIFTS; r.47 USD-bedrag (ongeguard): $70 in gifts; r.47 Verzend-/duties-/betaalbelofte (ongeguard): duties; r.49 Verzend-/duties-/betaalbelofte (ongeguard): duties; r.51 Verzend-/duties-/betaalbelofte (ongeguard): duties; r.65 Verzend-/duties-/betaalbelofte (ongeguard): duties; r.67 USD-bedrag (ongeguard): $70 in gifts; r.69 Verzend-/duties-/betaalbelofte (ongeguard): duties
- `v3/checkout/c4-int.html`: r.49 Verzend-/duties-/betaalbelofte (ongeguard): Duties; r.51 Verzend-/duties-/betaalbelofte (ongeguard): duties; r.65 USD-bedrag (ongeguard): $70 in gifts; r.67 Verzend-/duties-/betaalbelofte (ongeguard): Duties
- `v3/checkout/c4-nocode.html`: r.10 USD-bedrag (ongeguard): $70 in gifts; r.33 USD-bedrag (ongeguard): $70 in gifts; r.38 USD-bedrag (ongeguard): $70 IN GIFTS; r.47 USD-bedrag (US-guard): $70 in gifts; r.47 Verzend-/duties-/betaalbelofte (US-guard): duties; r.49 Verzend-/duties-/betaalbelofte (US-guard): duties; r.51 Verzend-/duties-/betaalbelofte (US-guard): duties; r.65 Verzend-/duties-/betaalbelofte (US-guard): duties; r.67 USD-bedrag (ongeguard): $70 in gifts; r.71 USD-bedrag (US-guard): $1,186, $599; r.71 US-only product (US-guard): 12-piece, US ONLY, pots; r.76 Verzend-/duties-/betaalbelofte (US-guard): duties
- `v3/checkout/c4-us-nocode.html`: r.38 USD-bedrag (ongeguard): $70 IN GIFTS; r.47 USD-bedrag (ongeguard): $70 in gifts; r.67 USD-bedrag (ongeguard): $70 in gifts; r.71 USD-bedrag (ongeguard): $1,186, $599; r.71 US-only product (ongeguard): 12-piece, US ONLY, pots
- `v3/checkout/c4-us.html`: r.65 USD-bedrag (ongeguard): $70 in gifts; r.71 USD-bedrag (ongeguard): $1,186, $599; r.71 US-only product (ongeguard): 12-piece, US ONLY, pots
- `v3/checkout/c4.html`: r.33 USD-bedrag (ongeguard): $70 in gifts; r.47 USD-bedrag (ongeguard): $70 in gifts; r.49 Verzend-/duties-/betaalbelofte (US-guard): Duties; r.51 Verzend-/duties-/betaalbelofte (US-guard): duties; r.65 USD-bedrag (ongeguard): $70 in gifts; r.67 Verzend-/duties-/betaalbelofte (US-guard): Duties
- `v3/post-purchase/p1-first.html`: r.94 USD-bedrag (ongeguard): $450
- `v3/post-purchase/p3-accessory-nocode.html`: r.41 USD-bedrag (ongeguard): $134, $439; r.41 Maat in inch (ongeguard): 11″
- `v3/post-purchase/p3-accessory.html`: r.40 USD-bedrag (ongeguard): $120.60, $134, $439; r.40 Maat in inch (ongeguard): 11″
- `v3/post-purchase/p3-apron-nocode.html`: r.41 USD-bedrag (ongeguard): $134, $439; r.41 Maat in inch (ongeguard): 11″
- `v3/post-purchase/p3-apron.html`: r.40 USD-bedrag (ongeguard): $120.60, $134, $439; r.40 Maat in inch (ongeguard): 11″
- `v3/post-purchase/p3-next-nocode.html`: r.42 USD-bedrag (ongeguard): $69; r.44 USD-bedrag (ongeguard): $59; r.61 USD-bedrag (US-guard): $119; r.71 USD-bedrag (US-guard): $127; r.81 USD-bedrag (US-guard): $69
- `v3/post-purchase/p3-next.html`: r.41 USD-bedrag (ongeguard): $62.10, $69; r.43 USD-bedrag (ongeguard): $53.10, $59; r.76 USD-bedrag (US-guard): $107.10, $119; r.86 USD-bedrag (US-guard): $114.30, $127; r.96 USD-bedrag (US-guard): $62.10, $69
- `v3/post-purchase/p3-pan-nocode.html`: r.41 USD-bedrag (ongeguard): $59; r.41 Maat in inch (ongeguard): 10″, 11″, 12″, 8″
- `v3/post-purchase/p3-pan.html`: r.40 USD-bedrag (ongeguard): $53.10, $59; r.40 Maat in inch (ongeguard): 10″, 11″, 12″, 8″
- `v3/post-purchase/p3-set-nocode.html`: r.41 USD-bedrag (ongeguard): $139; r.41 Maat in inch (ongeguard): 11″; r.47 USD-bedrag (ongeguard): $119; r.47 Maat in inch (ongeguard): 3.5″
- `v3/post-purchase/p3-set.html`: r.40 USD-bedrag (ongeguard): $125.10, $139; r.40 Maat in inch (ongeguard): 11″; r.61 USD-bedrag (ongeguard): $107.10, $119; r.61 Maat in inch (ongeguard): 3.5″
- `v3/site/a1.html`: r.53 Maat in inch (ongeguard): 11″; r.64 Maat in inch (ongeguard): 8″; r.66 USD-bedrag (ongeguard): $116.10, $129; r.73 Maat in inch (ongeguard): 10″; r.75 USD-bedrag (ongeguard): $114.30, $127; r.83 Maat in inch (ongeguard): 11″; r.85 USD-bedrag (ongeguard): $120.60, $134, $439; r.92 Maat in inch (ongeguard): 12″; r.94 USD-bedrag (ongeguard): $125.10, $139; r.104 USD-bedrag (ongeguard): $70 in gifts; r.106 Maat in inch (ongeguard): 11″, 12″
- `v3/site/a2.html`: r.36 Maat in inch (ongeguard): 11-inch; r.52 USD-bedrag (ongeguard): $120.60, $134, $439; r.52 Maat in inch (ongeguard): 11″; r.57 Maat in inch (ongeguard): 11″; r.60 USD-bedrag (ongeguard): $116, $349; r.60 Maat in inch (ongeguard): 10″, 12″, 8″; r.68 USD-bedrag (ongeguard): $70 in gifts
- `v3/vip/v1-nocode.html`: r.63 USD-bedrag (ongeguard): $70 in gifts
- `v3/vip/v1.html`: r.58 USD-bedrag (ongeguard): $70 in gifts
- `v3/vip/v2.html`: r.47 US-only product (ongeguard): pot
- `v3/welcome/w0.html`: r.108 USD-bedrag (ongeguard): $59
- `v3/welcome/w1-a.html`: r.63 USD-bedrag (ongeguard): $120.60, $134,, $439; r.63 Maat in inch (ongeguard): 11″; r.65 USD-bedrag (ongeguard): $70 in gifts
- `v3/welcome/w1-b.html`: r.66 USD-bedrag (ongeguard): $120.60, $134,, $439; r.66 Maat in inch (ongeguard): 11″; r.68 USD-bedrag (ongeguard): $70 in gifts
- `v3/welcome/w3.html`: r.63 USD-bedrag (ongeguard): $70 in gifts
- `v3/welcome/w4-int.html`: r.33 Verzend-/duties-/betaalbelofte (ongeguard): duties; r.47 Verzend-/duties-/betaalbelofte (ongeguard): duties; r.58 Maat in inch (ongeguard): 8″; r.60 Maat in inch (ongeguard): 10″; r.62 Maat in inch (ongeguard): 11″; r.64 Maat in inch (ongeguard): 12″; r.71 Verzend-/duties-/betaalbelofte (ongeguard): duties; r.76 Maat in inch (ongeguard): 11″; r.76 Verzend-/duties-/betaalbelofte (ongeguard): duties; r.79 US-only product (ongeguard): pots; r.81 Verzend-/duties-/betaalbelofte (ongeguard): duties
- `v3/welcome/w4-us.html`: r.58 Maat in inch (ongeguard): 8″; r.59 USD-bedrag (ongeguard): $116.10, $129; r.60 Maat in inch (ongeguard): 10″; r.61 USD-bedrag (ongeguard): $114.30, $127; r.62 Maat in inch (ongeguard): 11″; r.63 USD-bedrag (ongeguard): $120.60, $134; r.64 Maat in inch (ongeguard): 12″; r.65 USD-bedrag (ongeguard): $125.10, $139; r.71 USD-bedrag (ongeguard): $70 in gifts; r.76 USD-bedrag (ongeguard): $120.60, $134, $439; r.76 Maat in inch (ongeguard): 11″; r.77 USD-bedrag (ongeguard): $105, $314.10, $349; r.78 USD-bedrag (ongeguard): $1,186, $539.10, $599; r.78 US-only product (ongeguard): 12-piece, US only, pots; r.80 US-only product (ongeguard): pots
- `v3/welcome/w5.html`: r.79 USD-bedrag (ongeguard): $70 in gifts; r.81 USD-bedrag (ongeguard): $120.60, $134, $439; r.81 Maat in inch (ongeguard): 11″
- `v3/winback/r1-acc.html`: r.59 USD-bedrag (US-guard): $120.60, $134, $439; r.59 Maat in inch (US-guard): 11″; r.61 Maat in inch (INT-tak): 11″; r.66 USD-bedrag (ongeguard): $70 in gifts
- `v3/winback/r1-pan.html`: r.60 USD-bedrag (US-guard): $179.10, $199, $250; r.60 US-only product (US-guard): Roasting; r.65 USD-bedrag (ongeguard): $70 in gifts
- `v3/winback/r1-set.html`: r.68 USD-bedrag (US-guard): $125.10, $139; r.79 USD-bedrag (US-guard): $107.10, $119; r.90 USD-bedrag (US-guard): $134.10, $149; r.100 USD-bedrag (US-guard): $62.10, $69; r.109 USD-bedrag (ongeguard): $70 in gifts
- `v3/winback/r2-nocode.html`: r.42 USD-bedrag (ongeguard): $70 IN GIFTS; r.65 Maat in inch (ongeguard): 11″; r.67 USD-bedrag (US-guard): $134; r.74 US-only product (ongeguard): 2 Pans + 2 Lids; r.76 USD-bedrag (US-guard): $199; r.84 USD-bedrag (ongeguard): $116; r.85 USD-bedrag (US-guard): $349; r.94 USD-bedrag (ongeguard): $70 in gifts
- `v3/winback/r2-vip-nocode.html`: r.42 USD-bedrag (ongeguard): $70 IN GIFTS; r.66 USD-bedrag (ongeguard): $116; r.67 USD-bedrag (US-guard): $349; r.76 USD-bedrag (US-guard): $479; r.83 US-only product (ongeguard): 2 Pans + 2 Lids; r.85 USD-bedrag (US-guard): $199; r.94 USD-bedrag (ongeguard): $70 in gifts; r.104 US-only product (ongeguard): pots
- `v3/winback/r2-vip.html`: r.56 USD-bedrag (ongeguard): $70 in gifts; r.67 USD-bedrag (ongeguard): $116; r.68 USD-bedrag (US-guard): $296.65, $349; r.77 USD-bedrag (US-guard): $407.15, $479; r.84 US-only product (ongeguard): 2 Pans + 2 Lids; r.86 USD-bedrag (US-guard): $169.15, $199; r.102 US-only product (ongeguard): pots
- `v3/winback/r2.html`: r.56 USD-bedrag (ongeguard): $70 in gifts; r.66 Maat in inch (ongeguard): 11″; r.68 USD-bedrag (US-guard): $120.60, $134; r.75 US-only product (ongeguard): 2 Pans + 2 Lids; r.77 USD-bedrag (US-guard): $179.10, $199; r.85 USD-bedrag (ongeguard): $116; r.86 USD-bedrag (US-guard): $314.10, $349; r.111 USD-bedrag (ongeguard): $70 in gifts

## 10. Open punten voor Floris

1. **Canada en duties.** Shopify zet duties in de CA-checkout, 11 recente CA-orders hadden 0 duties. Mogen CA-mails "no import duties" zeggen? Tot dan alleen "Free shipping".
2. **"Free Express Shipping from the US"** op elke PDP, ook voor AU/UK. Klopt dat voor alle markten (en wat is "local warehouse")?
3. **Noorwegen** rekent in USD (geen valuta-instelling) en valt dubbel in RoW; **Germany/Netherlands** zijn aparte markten zonder catalogus naast EURO. Bewust?
4. **Fall sale 6-Pcs $299**: in de mails staat nog $349 en "About $116 a pan" (zie lijst). DECISIONS zegt $349; de site zegt nu $299 / compare-at $598 ("Buy 2 get 4 free"). Welke prijs geldt tot wanneer?
5. **Pan Pro-prijzen zijn veranderd** (US, 8 okt): Mini $99, Small $137, Standard $144, Large $149; de mails noemen $129/$127/$134/$139. Prijzen in mails moeten voortaan uit `content/catalog/products.json` komen, niet uit de copy.
6. **Gift-waarden in Shopify** zijn per markt niet consequent omgerekend (free shipping £10 tegenover $15, e-book £25 tegenover $30) en de mystery gift en filter hebben geen compare-at. Mogen we de tabel in sectie 6 gebruiken, of zet Floris eigen waarden per markt?
