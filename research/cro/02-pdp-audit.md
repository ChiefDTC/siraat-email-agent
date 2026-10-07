# 02 · PDP-audit van de toppers

Stand: 7 oktober 2026. Bronnen: Shopify Admin API (prijzen, compare-at, voorraad, status, metafields via content/products), content/products/README.md (31 inconsistenties), Intelligems omzet per product (30 dagen), Triple Whale landingspagina's (bounce, ATC, CR per PDP), Gorgias (369 pre-sale tickets in 60 dagen: Product Details 191, Usage 82, Availability 44, Promotion 30, Warranty 10; plus 400 tickets en 154 lage reviews in content/reviews/objections.csv), Aftersell.
Update 7 oktober, 17:00: siraatskitchen.com werd later op de dag bereikbaar. Alle PDP's, collecties, home en de lege winkelwagen zijn met Playwright (Chromium) bekeken op iPhone 390x844, desktop 1440, Android Chrome (Pixel 7), en de Facebook- en Instagram-in-app-browser. Screenshots staan in `research/cro/screens/` (`<profiel>-<pagina>-fold.jpg` en `-full.jpg`), de volledige paginatekst in `research/cro/screens-text/`. Live prijzen via `/products/<handle>.js`. Toevoegen aan winkelwagen en de checkout openen is **niet** gedaan: die stap werd door de permissieregels van deze omgeving geblokkeerd (geldt als handeling in een gekoppelde winkel). Wat daarvoor nog moet staat in 05.

### 0a. Wat de live site vandaag laat zien (en wat afwijkt van content/products)

Prijzen live (US, 7 okt): Pan Pro Standard $134/$439, Large $139/$455, Small $127/$419, **Mini $99/$330** (was $129/$180), **6-set hoofdlisting nu $349/$749** (gelijk aan BDAY-listing; inconsistentie 1 is voor de prijs opgelost, er zijn nog wel twee listings), 12-set $599/$1,186, Deep $119 tot $149, Pizza $129/$200, Roasting $199/$250, **Apron $54/$100** (was $49/$80), deksel $59/$110. Pot Set 6-Pcs: **404**.

Bevindingen op elke pannen-PDP (Standard, Large, Small, Mini, Deep, 6-set, 12-set), letterlijk van de pagina:

| Wat staat er | Waarom het kost | Oordeel |
|---|---|---|
| Countdown "PRIME SALE · ends in 02 HRS 42 MIN 5x SEC" in de balk en in de koopbox; home: "Discounts already applied, for a few hours only" | Elke nieuwe sessie, minuten na elkaar, op elk profiel, startte op 02:42:5x. Het is een timer die per bezoeker opnieuw begint. Een terugkerende bezoeker (2,7 keer zoveel waard, zie 01) ziet de "laatste uren" elke dag opnieuw. FTC-risico (nep-urgentie) en vertrouwensverlies bij precies de koper die twijfelt | Weg, of een echte einddatum die voor iedereen gelijk is |
| "High demand — few units left" | Standard heeft 1.098 op voorraad, Large 624 | Nep-schaarste, weg |
| "Delivery From Your Local Warehouse · Fast & free shipping" en "Free Express Shipping · from the US" (Pan Pro, sets), "from local warehouse" (Deep, Pizza, Roasting, Apron) | Tickets: "goods are shipped directly from Ningbo China, inconsistent with" (93501949), "I have also discovered that you ship these products from China ... merchant misrepresentation. I have contacted my bank" (85587094). Dit is de directe bron van annuleringen en chargebacks | Vervangen door wat waar is per markt ("Free shipping, duties included, tracked") |
| "RISK-FREE PURCHASE: Cook on your pan at home for 30 days, and if it isn't the best pan you've owned, return it for a full refund" | Refund policy: "Products that have been used cannot be returned for a refund ... Return shipping for unused products is the customer's responsibility". Badge eronder: "30-Day Returns · free returns". Klanten citeren dit: "your advertisement says 30 day return hassle free" (87109409), "On the website, it says free returns" (88045707) | De PDP belooft een gebruikstest met gratis retour, het beleid niet. Eén van de twee aanpassen (zie 03) |
| Overview: "This pan is crafted to be indestructible, built to last a lifetime" | Verboden (DECISIONS: 75-year warranty, nooit lifetime) | Weg |
| Vergelijkingsblok: "Oven safe to 548°C / 1000°F"; Pizza "even at 1000°F", "Heat-safe to 1000°F"; Roasting "Heat safe to 400°C / 750°F" | Getal zonder bron, twee verschillende getallen in één winkel | "Oven safe" |
| Feature-iconen "Stay Cool Handle" met uitleg "shaped to stay cool on the stovetop" | Staat in claims "niet zeggen" (één review, geen spec); metalen greep op een pan van 548°C | Weg of meten |
| "Naturally nonstick" (Why titanium), FAQ "How do the pans stay nonstick without any coating?" | Het grootste retourbezwaar is plakken. De zichtbare review onderaan de PDP: "Siraat advertises it as naturally nonstick. Nothing could be further from the truth ... Satan's cookware" | Kop wordt "Natural release, with the right heat" plus de 3 stappen die al onderaan staan ("How to get the perfect release") naar boven |
| "Plus: win a PFAS water purifier · Weekly draw. Every order enters automatically · Worth $450" | "Purifier" is verboden (PLAYBOOK 11); een loterij gekoppeld aan aankoop zonder "No purchase necessary" en zonder regels-pagina is in de VS een juridisch risico (QA-rapport) | Regels-pagina plus "No purchase necessary", woord "filter" |
| 12-set: badge "SAVE $587" en verderop "You save $487" | Twee bedragen op één pagina | Eén bedrag uit compare-at |
| 6-set BDAY: "45% off for our birthday. The biggest discount we've ever done, and it won't get better than this." | Badge zegt 53 procent, en de hoofdlisting kost exact hetzelfde ($349/$749) zonder verjaardag | Tekst weg of gelijk aan de echte prijs |
| Mini (andere template, Upgrade & Save-blok): "2 Pans + 2 Lids $199 · $844 · Save $645 · extra 43% off" | Compare-at $844 voor 2 pannen en 2 deksels (los: circa $310) | Anker eerlijk maken |
| Reviewscore "4.8 · 3,281 reviews" bij elke PDP, ook de 12-set; Apron "4.8 · 23 reviews" | Goed zichtbaar boven de titel. Het is een gedeelde score over de hele lijn; de 12-set heeft geen eigen reviews | Prima; aanvullen met set-reviews |
| Shop Pay Installments-regel ("4 interest-free installments, or from $12.09/mo with Shop") staat direct boven de koopknop op de PDP | Goed. Afterpay/Klarna voor AU en UK ontbreekt | Zie 03 |
| Maatkeuze Pan Pro: Small, Standard ("BEST SELLER"), Large met "Meals for two / Our #1 seller / Family & batch" en prijzen in de kaart | Maathulp bestaat al (eerdere aanname in dit document klopt dus niet meer). Mini zit niet in de kaartjes, alleen via "Size guide"; op 390 breed overlapt de chatknop de Large-kaart | Mini als vierde kaart; chatknop hoger of kleiner op PDP |
| Desktop: de koopknop en hoofdprijs staan onder de vouw bij 1440x900; de sticky balk onderin dekt de gift-strip af | Op desktop ziet de bezoeker eerst timer en gifts, niet de prijs | Prijs en knop direct onder de maatkaarten |

Snelheid (lab, Chromium zonder netwerkvertraging, dus beter dan echt): PDP's laden in 2,6 tot 4,7 seconden tot `load`, LCP 0,7 tot 1,9 s, CLS 0 tot 0,02 (Android op de sets 0,055 tot 0,062, door het blok `product-info__block-item` en `siraat-fg` dat na laden verschuift). Pagina's wegen 2,3 tot 3,0 MB (PDP) en 5,4 MB (home mobiel, clearance-collectie 4,8 MB), met 280 tot 324 requests en **174 scripts van 22 externe domeinen** op de Pan Pro (onder andere Okendo én Loox, Kiwi Sizing, Recharge, Rise.ai, OptiMonk, Alia, Bogos, Intelligems, Clarity, GTM, Playbook, Avada, archive-digger-pixel). Echte p75 uit Triple Whale: LCP 2.492 ms, net onder de grens. Elke extra app duwt mobiel over de grens; Loox naast Okendo en OptiMonk naast Alia zijn dubbel.

In-app-browsers (Facebook en Instagram user agent) en Android: geen afwijkende layout, geen horizontale scroll, zelfde timer en blokken. Apple Pay is in Chromium niet te testen. Bij een tweede bezoek op iPhone stuurde Shopify de pagina via `shop.app/accounts/sur` (Shop-herkenning) door; in deze omgeving faalde die stap, in het echt is het een extra redirect bij terugkerende mobiele bezoekers. Controleren met een echte iPhone.

## 0. Wat voor alle PDP's geldt

Dit zijn de bezwaren die in tickets en lage reviews steeds terugkomen en die de PDP niet boven de vouw beantwoordt:

| Bezwaar | Hoe vaak | Wat de PDP nu doet | Wat moet |
|---|---|---|---|
| "Blijft eten plakken zonder coating?" | 60 van 400 tickets, 81 van 154 lage reviews | Beschrijving zegt "non-stick" niet, maar belooft wel "effortless"; uitleg over voorverwarmen zit diep in care_use | Direct onder de koopknop een regel "No coating, so release comes from heat: preheat 2 to 3 min, water test, 1 tsp oil" met link naar de 20-seconden-video. Dit is het bezwaar dat de meeste retouren en lage reviews veroorzaakt; het eerlijk vooraf zeggen verlaagt retour en verhoogt vertrouwen |
| "Welke maat heb ik nodig?" | 29 van 400, 21 pre-sale | Live: kaartjes Small/Standard/Large met "Meals for two / Our #1 seller / Family & batch". Mini ontbreekt in de kaartjes | Mini als vierde kaart ("1 person, eggs"); in de Size guide ook de hoogte en het passende deksel |
| "Is het echt titanium, wat zit eronder?" | 43 van 400, 28 pre-sale | Specificaties 0.5 / 1 / 0.6 mm staan diep; Gorgias, PDP en chef-video gebruiken drie verschillende formuleringen voor de buitenlaag | Eén doorsnede-beeld "3 layers, only titanium touches your food" met Light Labs-rapportnummer 25895 en een link naar /pages/third-party-testing |
| "Zit er een deksel bij?" | 41 van 400, 16 pre-sale; geregeld verkeerde deksels | Niet zichtbaar bij de koopknop | "Lid sold separately" plus een vinkje "Add the matching 28 cm lid, $59" (bundel). Verhoogt AOV en voorkomt verkeerde maat |
| "Waar komt het vandaan, betaal ik invoerrechten?" | 152 tickets over customs/duties, 91 over herkomst (60 dagen) | "Free worldwide shipping" zonder uitleg; orderbevestiging in Europa noemt wel mogelijke VAT en invoerrechten | Eén eerlijke regel per markt: "Designed in the Netherlands, made in certified facilities in Asia. Free shipping, duties included (US, AU, UK, CA)". Zie 03 |
| "Waarom is het goedkoper bij Amazon / was het vorig jaar goedkoper?" | tickets 86030773, 90337642, 89741682 | Doorgestreepte prijs $439 bij $134 | Zie prijsanker hieronder |
| "Retour gratis?" | tickets over retourkosten $12 tot $30 | Site en mails zeggen "free 30-day returns", refund policy zegt "return shipping for unused products is the customer's responsibility" | Kiezen en overal gelijk zetten (zie 03) |

Bewijs en reviews: Okendo staat op de pannen (4.8, 2.226 reviews, 98 procent recommended, gedeeld over de pannenlijn). Wat ontbreekt op elke PDP: reviews gefilterd op de bekeken maat of set, foto-reviews van "first egg"-momenten, een zichtbaar aantal reviews direct naast de titel, en een paar reviews die het plak-bezwaar eerlijk benoemen ("took me two tries, now eggs slide"). Gebruik de echte reviews uit content/products/*/reviews.md (R069, R017, R169 voor plakken; R407 voor maat; R053, R530 voor splitzendingen).

Prijsanker: de compare-at van de Pan Pro is $439 bij een prijs van $134 (69 procent). De badge zegt "50% OFF + FREE GIFTS". Klanten vergelijken met Amazon en met hun eigen eerdere aankoop. Een anker dat drie keer de prijs is en tegelijk niet klopt met de eigen badge ondermijnt vertrouwen en is in de VS een FTC-risico (former price die nooit gold). Advies: badge rekent automatisch uit compare-at (geen handmatige percentages), en een eerlijker anker testen in Intelligems (bijvoorbeeld de mei-prijs als compare-at). De prijstest van september had de "eerlijke mei-compare-at" juist geparkeerd.

## 1. Titanium Hammered Pan Pro (Standard, Large, Small, Mini)

Belang: $520.688 netto in 30 dagen (Standard $242.047, Large $184.988, Small $71.722, Mini $21.932), 49 procent van de omzet. De Standard-PDP is de landing van 155.268 sessies per maand: 76 procent bounce, ATC 5,3 procent, CR 1,44 procent. Small (0,92 procent) en Deep (0,72 procent) converteren als landing duidelijk slechter dan Mini (2,41 procent).

| Probleem | Detail | Fix |
|---|---|---|
| Badge | Live 7 okt: "70% OFF + FREE GIFTS" op Standard, Large, Small en Mini: klopt nu met compare-at (69 tot 70 procent). De eerdere "50% OFF" uit content/products is verouderd | Zo laten, maar het anker zelf is het probleem (zie prijsanker) |
| Mini-prijs | Opgelost: live $99 / $330 (was $129 / $180, duurder dan Small) | content/products en mails bijwerken naar $99 |
| Verboden claims live | "Scientifically proven to retain more nutrients", "Ultra-Durable & Scratch-Resistant", "a lifetime of reliable use"; beeld-alt "Light Labs tested with 30 of 30 tests passed" (certificaat toont 31 stoffen) | Eraf. Vervangen door "No coatings · PFAS-free titanium cooking surface · Tested by Light Labs, report 25895 · 75-year warranty" |
| Oventemperatuur | "Heat safe up to 548°C / 1000°F" terwijl de Roasting Pan 400°C zegt en claims.csv het getal op needs-proof heeft | "Oven safe" zonder getal tot er een bron is |
| Laagdikte | 0.5 / 1 / 0.6 mm live, needs-proof in claims.csv | Laten staan als specificatie (niet als kop) zodra Floris bevestigt |
| Maat "Medium" | Light Labs testte "Pan Pro, Medium", die maat bestaat niet | Op /pages/third-party-testing uitleggen welke maat getest is |
| Kopie-listings actief | Standard $157 en $144, Large $169, Mini $129 met eigen compare-at | Op draft of redirect naar de hoofdlisting; anders landen advertenties of oude mails op een andere prijs |
| Mini hoogte | "4.5 cm / 2.3 inch" (4.5 cm is 1.8 inch) | Corrigeren |
| Hoogte en deksel | Geen "lid not included" bij de knop | Deksel-bundel als vinkje (zie 0) |

Test (Intelligems, content): A = huidige PDP, B = maathulp in de knoppen + bezwaarregel "release comes from heat" + deksel-vinkje + reviewscore naast de titel. Beslis op omzet per bezoeker, minimaal 14 dagen en 300 orders per arm.

## 2. Titanium Hammered Pan Set With Lids, 6-Pcs ($349 BDAY en $399 listing)

Belang: $103.612 (hoofdlisting) plus $30.592 (SB-listing $449) in 30 dagen, 381 orders. Als landing: 2.774 sessies, 81 procent bounce, CR 1,84 procent, $6,94 per sessie (hoogste van alle PDP's).

| Probleem | Detail | Fix |
|---|---|---|
| Twee listings, sinds vandaag één prijs | Live 7 okt: hoofdlisting én BDAY beide $349 / $749 ("PRIME SALE · 53% OFF", "SAVE $400"). SB-listing $449 bestaat nog. content/products noemde nog $399 / $1,384 | Mails mogen naar de hoofdlisting linken (QA-punt A5 vervalt zolang de prijs zo blijft). BDAY-listing op redirect zetten naar de hoofdlisting, zodat er één URL, één reviewteller en één voorraad is |
| Badges en tekst | Badge nu "53% OFF" (klopt), maar de BDAY-tekst zegt "45% off for our birthday. The biggest discount we've ever done, and it won't get better than this." terwijl de gewone listing hetzelfde kost | BDAY-tekst weg |
| Compare-at $749 | De set bevat Mini, Small, Large (geen Standard) + 3 deksels; los kost dat $99 + $127 + $139 + 3 x $59 = $542 | Compare-at = som van de losse prijzen ($542): "Save $193 vs buying separately" is eerlijk en controleerbaar. Testen tegen het huidige anker |
| Voorraad -325 | Oververkocht; Gorgias mag hem alleen "when in stock" noemen | Levertijd eerlijk op de PDP zetten of doorverkopen stoppen; anders komen er annuleringen en chargebacks |
| Inhoud | Standard 11 inch zit er niet in (whats_included) | Expliciet tonen: "Mini 8 inch, Small 10 inch, Large 12 inch + 3 matching lids". Wie de bestseller wil, mist hem anders pas bij levering |
| Splitzending | Sets komen in meerdere pakketten | Eén regel "may arrive in 2 parcels, each tracked" |
| Beelden | Maar één echt packshot; beelden met "6PCSSet" in de naam tonen de pottenset | Juiste packshot van de 3 pannen + 3 deksels |

Test: Upgrade & Save-blok buiten de VS ("6 pcs upgrade excl usa") loopt sinds 2 okt: CR +6 procent, omzet per bezoeker +8 procent, kans beter dan controle 69 procent. Laten lopen tot 14 dagen.

## 3. Titanium Hammered Cookware Set, 12-Pcs ($599)

Belang: $147.304 direct in 30 dagen plus $49.176 als post-purchase upsell (88 keer, Aftersell). Als landing: 5.407 sessies, **89 procent bounce** (hoogste van alle PDP's), CR 0,89 procent, $4,64 per sessie.

| Probleem | Detail | Fix |
|---|---|---|
| Badge | Live: "PRIME SALE · 49% OFF" en "SAVE $587" (klopt), maar lager op dezelfde pagina "You save $487" | Eén bedrag |
| Potmaten | PDP "2-Qt, 3-Qt, 8-Qt", losse listings "2 L (2.1 qt), 3 L (3.2 qt), 7.5 L (7.9 qt)" | Eén set maten |
| Levering | DECISIONS: "een aantal dagen"; voorraad -2; komt in twee delen (pannen eerst, potten 24 tot 48 uur later) | "Ships in 2 parcels within X days" bij de knop |
| Amazon goedkoper met deksel | Ticket 86030773 | Uitleggen wat in de set zit tegenover een Amazon-listing (kopie of andere set?) of de Amazon-prijs gelijktrekken |
| Buiten de VS | Niet in de catalogus buiten US (behalve SG); de PPU biedt hem wel aan | Zie Aftersell in 03 |
| Hoge refund op $700+ | 12,4 procent van de omzet boven $700 wordt terugbetaald | Bezwaar "plakken" en splitzending vooraf benoemen; set-specifieke reviews |
| Bounce 89 procent | Waarschijnlijk zware hero of verkeerde advertentiebelofte (zie 05) | Visueel controleren; set-PDP een eigen "wat zit erin"-beeld boven de vouw |

Test: "12-pcs + gratis pizza steel" bestaat als unlisted variant ($699). Het is beter om de gratis pizza steel als gift-regel te testen dan als duurdere variant.

## 4. Titanium Hammered Pot Set With Lids, 6-Pcs

Belang: $32.474 in 30 dagen (135 orders) via Intelligems, terwijl het product in Shopify op **DRAFT** staat, voorraad -4, prijs $399 (compare $547), **lege beschrijving** en geen online-URL. Het verkoopt dus via een bundel, een app of een upsell, maar wie erop zoekt of er een link naar krijgt, landt nergens.

Fix: beslissen of het een zelfstandig product is. Zo ja: publiceren met beschrijving (maten in quart en liter gelijk aan de 12-set), inhoud, deksels, levering. Zo nee: in content/facts/products.csv en de mails nooit los aanbieden. Gorgias zegt nu "pots are not sold separately anywhere" terwijl losse potten (2 L, 3 L, 7,5 L) wel ACTIVE zijn.

## 5. Titanium Hammered Deep Pan Pro ($119 tot $149)

Belang: $58.749 direct (421 orders) plus $15.253 als PPU-downsell (215 keer). Als landing: 5.586 sessies, 79 procent bounce, CR 0,72 procent (half van de Pan Pro).

| Probleem | Detail | Fix |
|---|---|---|
| Maten zonder specs | Varianten 20, 24, 26, 28, 30 cm; specs alleen voor 20, 24, 26 | Specs voor alle maten |
| "Standard" betekent iets anders | Hier 24 cm, bij de koekenpan 28 cm | Maten op diameter noemen, niet op Standard/Large |
| Geen 24 cm-deksel | Wie Standard koopt, kan geen passend deksel kopen | Deksel 24 cm toevoegen of melden "fits our 26 cm lid snugly" als dat klopt |
| Badge | Live "PRIME SALE · 70% OFF" (klopt met compare-at); collectie "warehouse-clearance" zegt erboven "Everything left in the warehouse goes" | Clearance-framing van een kernproduct testen tegen geen clearance |
| Waarom een deep pan | PDP verkoopt geen gebruiksmoment | "Sauté, braise, shallow-fry" met een beeld per toepassing |

## 6. Titanium Hammered Pizza Steel ($129)

Belang: $19.845 (140 orders). Als landing: 4.741 sessies, 84 procent bounce, CR 1,86 procent.

| Probleem | Detail | Fix |
|---|---|---|
| Diameter ontbreekt | "Will it fit my oven?" is de eerste vraag; nergens een maat | Diameter, dikte en gewicht toevoegen |
| Badge en hitte | Live "PRIME SALE · 36% OFF" (klopt); tekst "No coatings, no chemicals, nothing to chip, peel or degrade, even at 1000°F" en "Heat-safe to 1000°F" | Getal weg |
| Hittegetal | PDP noemt pizza-oven-hitte zonder bron | "Safe in home ovens and pizza ovens" zonder getal |
| Cross-sell | Wordt vaak met de 12-set gekocht | Op de set-PDP aanbieden als gift of bundel |

## 7. Titanium Hammered Roasting Pan ($199)

Belang: $4.109 (21 orders). Als landing: 1.557 sessies, CR 0,77 procent. Lanceerproduct dat nog oude beloftes draagt.

| Probleem | Detail | Fix |
|---|---|---|
| Oude beloftes | Live 7 okt: "100-day trial" en "Lifetime warranty" zijn weg (75-Year Warranty, 30-Day Returns). Wel nog "Free Express Shipping", "for a lifetime, not a season", "High demand — few units left" bij 270 op voorraad | Express en lifetime weg |
| Oventemperatuur | 400°C / 750°F, terwijl de pannen 548°C zeggen | Eén lijn voor alles: "oven safe" |
| Gorgias zegt "not available yet, do not recommend" | Terwijl hij ACTIVE is en verkoopt | Gorgias-guidance 8566447 bijwerken, anders zegt support "niet leverbaar" tegen kopers met twijfel |
| Badge "LAUNCH SALE · SAVE $51" | Klopt ($250 naar $199) | Laten staan; dit is het voorbeeld voor alle andere badges |

## 8. Siraat Signature Apron ($49, vier kleuren)

Belang: verkoopt vooral als gift (Oak 272 orders en Ember 265 in 90 dagen voor gemiddeld $12). Rating 4.8 uit 23.

| Probleem | Detail | Fix |
|---|---|---|
| Badge | Live $54 / $100 met "PRIME SALE · 46% OFF" (klopt), maar onderaan "Built to last a lifetime" en "Wear it in your kitchen for 30 days ... return it for a full refund" | Lifetime weg; retourtekst gelijk aan beleid |
| PVC-coating en PU-leer | Botst met "no coatings / plastic-free" als hij naast de pannen staat | Niet in de gift-stack noemen met "plastic-free"; op de PDP eerlijk "water-repellent coated canvas" |
| Maattabel | Afmetingen staan er (84 x 74 cm, banden 102 cm) | Ook in inches, en "one size, adjustable" boven de vouw |
| Rol | Verkoopt bijna alleen als toevoeging | Als checkout-upsell of cart-add-on tonen, niet als landing |

## 9. Wat er per PDP moet veranderen, samengevat

| Prioriteit | Actie | Producten | Eigenaar | Test? |
|---|---|---|---|---|
| 1 | Verboden claims en oude beloftes eraf (nutrients, scratch-resistant, lifetime, 100-day trial, express shipping, 548°C, 30 of 30) | Pan Pro, Roasting Pan, Cookware Set Pro, Complete Edition, alle overviewteksten | dev (metafields), Claude levert teksten | Nee, compliance |
| 2 | Badges automatisch uit compare-at | Alle | dev | Nee |
| 3 | Eén prijs voor de 6-set, kopie-listings op draft | 6-set, Pan Pro | Floris | Nee |
| 4 | Maathulp in de knoppen, deksel-vinkje, bezwaarregel "release comes from heat", reviewscore bij titel | Pan Pro, Deep, Wok, Crêpe | dev, Claude copy | Ja, Intelligems content-test |
| 5 | Set-PDP's: "wat zit erin"-beeld, compare-at = som losse prijzen, levering in pakketten | 6-set, 12-set | dev, Floris (prijs) | Ja, anker-test |
| 6 | Specs aanvullen (Deep 28/30, Pizza diameter, Mini hoogte, potmaten) | Deep, Pizza, 12-set, Mini | Claude (teksten), dev | Nee |
| 7 | Pot Set: publiceren of overal weghalen | Pot Set | Floris | Nee |
| 8 | Herkomst en invoerrechten eerlijk per markt | Alle | Floris | Nee |
