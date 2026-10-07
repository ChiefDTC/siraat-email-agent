# 03 · Routing-ontwerp: categorie-router per flow

Doel: elke koper krijgt een mail over wat hij echt koos, met zo weinig varianten als kan. Ontwerp: **vier paden** overal hetzelfde, plus dynamische blokken binnen één template waar alleen een alinea of een productkaart verschilt.

| Pad | Wie (aandeel checkout / orders) | Waar het verschil zit |
| --- | --- | --- |
| **KOOKGEREI** | Pan Pro, deep, wok, crêpe, pizza steel, roasting, pots, en kookgerei + accessoire (60% / 76%) | Bestaande v3-mails |
| **SET** | Set of bundel, of cart >= $300 (23% / 20%) | Bestaande S-varianten |
| **ACCESSOIRE** | Alles zonder kookgerei: schort, plank, deksel, molens, utensils, strips, gift card, overig (15% / 9,5%) | Nieuwe *-acc mails; schort en gift card via `{% if %}` binnen dezelfde template |
| **BESTAANDE KLANT** | Placed Order >= 1 vóór de trigger (11 tot 18%) | Overslaan van merkuitleg (C2) en brug-mails (C3-acc); P3 bij order 2 overslaan |

Internationaal is geen eigen pad maar een regel: prijzen alleen tonen als de valuta USD is (cart) of het verzendland US is (post-purchase, winback); C4 blijft gesplitst op land.

## Bouwstenen (exact zoals in Klaviyo in te stellen)

Titellijsten: zie 00-data.md, sectie "Titels". Afkortingen hieronder:

- `KOOK_TITELS` (lijst, exact): Titanium Hammered Pan Pro Standard, Titanium Hammered Pan Pro Large, Titanium Hammered Pan Pro Small, Titanium Hammered Pan Pro Mini, Titanium Pan Pro, Titanium Hammered Deep Pan Pro, Titanium Hammered Wok Pan Pro, Titanium Hammered Crêpe Pan Pro, Titanium Hammered Pizza Steel, Titanium Hammered Roasting Pan, 2 Litre Titanium Hammered Pot With Lid, 3 Litre Titanium Hammered Pot With Lid, 7,5 Litre Titanium Hammered Pot With Lid, Pot Set With Lids 6-Pcs (titel nakijken), Titanium Hammered Pan Pro With Lid, Titanium Hammered Pan Pro & Utensil Set, Titanium Cook & Prep Bundle
- `SET_TITELS` (lijst, exact): Titanium Hammered Pan Set With Lids | 6-Pcs, Titanium Hammered Cookware Set | 12-Pcs, Titanium Hammered Cookware Set Pro, Titanium Hammered Complete Edition, Titanium Hammered – Complete Edition, Full Hammered Pro Edition, The Just Everything Bundle | 34-Pcs, 2 Pans + 2 Lids, Titanium Hammered Pan Pro Duo, Titanium Hammered Pro Duo, Titanium Hammered Pan Pro Kit, 12 pcs cookware set, Titanium-Hammerpfannenset mit Deckel | 6-teilig
- `PANPRO_TITELS`: de vijf Pan Pro-titels plus Titanium Hammered Pan Pro With Lid
- `VORM_TITELS` (wok, deep, crêpe): Titanium Hammered Deep Pan Pro, Titanium Hammered Wok Pan Pro, Titanium Hammered Crêpe Pan Pro
- `KOOK_WOORDEN` (substring, voor velden die één string zijn: Product Name, Name): `Hammer`, `Pan`, `Pot`, `ookware`, `Everything`, `fanne`, `Prep Bundle`. Getest op 115 titels (alle producttitels in products.csv en in de 3.200 events): geen enkel accessoire matcht, elk kookgerei wel.

Waarom twee vormen: `Items` (Checkout Started, Placed Order) is een **lijst** van titels; in Klaviyo-filters betekent "contains" daar "bevat dit element exact", dus exacte titels met `contains-any`. `Product Name` (Added to Cart) en `Name` (Viewed Product) zijn **strings**, soms met variant erachter ("Stainless Steel Lid - Chrome / Standard (11")"), dus substring met `contains` per woord, OR-gekoppeld.

Bewezen filtervorm (PLAYBOOK 4): `metric_filters` met `Items list contains-any`. In de UI: Trigger split → property `Items` → "contains any of" → titels plakken.

Profielvoorwaarden:
- `HEEFT_GEKOCHT` = What someone has done: Placed Order, at least once, over all time (in een trigger-flow op Checkout/Cart/Viewed Product telt het trigger-event niet mee).
- `HEEFT_KOOKGEREI` = Placed Order where `Items` contains-any (`KOOK_TITELS` + `SET_TITELS`), at least once, over all time.
- `ORDER_2` = Placed Order count over all time equals 2 (in post-purchase telt de huidige order mee).

## 1. Checkout abandonment

```
Trigger: Checkout Started
  Trigger filter (nieuw): $value is greater than 0          (sluit $0-carts met alleen gifts uit, 2%)
  Flow filters: ongewijzigd
→ wacht 1 uur → C1 (één template, pan-uitleg alleen bij kookgerei via {% if %})
→ TRIGGER SPLIT T1: Items contains-any KOOK_TITELS + SET_TITELS
   JA (kookgerei/set)
     → wacht tot dag 2, 09:00
     → CONDITIONAL SPLIT S1: HEEFT_GEKOCHT
          JA  → (geen C2) 
          NEE → C2
     → wacht 1 dag
     → TRIGGER SPLIT T2: $value >= 300 OR Items contains-any SET_TITELS
          JA  → C3-S
          NEE → TRIGGER SPLIT T3: Items contains-any PANPRO_TITELS AND $value < 250
                  JA  → C3-P
                  NEE → (geen C3: pizza steel, roasting, pot, wok/deep/crêpe alleen, of 2 pannen onder $300)
     → wacht 1 dag → CONDITIONAL SPLIT land = US → C4-US / C4-INT
   NEE (accessoire)
     → wacht tot dag 2, 09:00 → C2-acc
     → wacht 1 dag
     → CONDITIONAL SPLIT S1: HEEFT_GEKOCHT
          JA  → (geen C3)
          NEE → C3-acc
     → wacht 1 dag → land = US → C4-US / C4-INT   (12-pcs-blok verbergt zich zonder kookgerei)
```

Waarom T3 met `$value < 250`: één Pan Pro is $127 tot $139, met deksel $186 tot $198, met plank tot ~$240. Twee pannen zijn minstens $254. Zo krijgt een cart met twee pannen geen "Keep my one pan".

Variantaantal: 2 nieuwe mails (C2-acc, C3-acc). C1 en C4 zijn één template met `{% if %}`.

## 2. Cart abandonment

```
Trigger: Added to Cart
  Trigger filters (nieuw): Price is greater than 0
                           Product Name doesn't contain "Mystery Gift" / "E-Book" / "Free Shipping" / "Giveaway"
→ wacht 1 uur
→ CONDITIONAL SPLIT K: Added to Cart where Product Name contains "Hammer" OR "Pan" OR "Pot" OR "ookware"
                       OR "Everything" OR "fanne" OR "Prep Bundle", at least once in the last 1 day
   JA (kookgerei, ook als eerst een accessoire en daarna een pan is toegevoegd)
     → K1 → wacht 1 dag → split HEEFT_GEKOCHT → K2-returning / K2-new → wacht 1 dag → K3
   NEE (accessoire)
     → K1-acc → wacht 2 dagen → K3   (geen K2: de rekensom per jaar gaat over een pan)
```

Waarom een conditional split en geen trigger split: Added to Cart bevat alleen het toegevoegde product. Een conditional split over "de laatste dag" ziet ook een pan die na het accessoire is toegevoegd (21% van de profielen voegt meer dan één categorie toe).

Prijs: K1, K2-new, K2-returning, K3 en K1-acc tonen de prijs alleen bij `event|lookup:'$currency' == 'USD'` (gebouwd).

## 3. Browse abandonment

```
Trigger: Viewed Product (filters ongewijzigd)
→ wacht 4 uur
→ TRIGGER SPLIT: Name contains "Hammer" OR "Pan" OR "Pot" OR "ookware" OR "Everything" OR "fanne" OR "Prep Bundle"
   JA  → B1 (knop en eyebrow "set" of "pan" via {% if %}) → wacht 2 dagen → split klikte B1 → B2-clicked / B2-notclicked
   NEE → B1-acc → wacht 2 dagen → split klikte B1-acc → JA: B2-clicked (dynamisch) / NEE: einde
```

Optioneel: bestaande klanten (`HEEFT_KOOKGEREI`) die een pan bekijken krijgen nu de basisuitleg "coated vs Siraat". Volume ~480 per week. Voorstel voor een volgende ronde: B1 voor eigenaren = B2-clicked direct (code, geen uitleg). Nu niet gebouwd: het bekeken product is vaak een tweede maat, en de uitleg schaadt niet.

## 4. Welcome

Geen wijziging. W0 (koper-pad) zou dezelfde intro-logica als P1-first kunnen krijgen; volume klein.

## 5. Post-purchase

```
Trigger: Placed Order (ongewijzigd)
→ P1-first / P1-repeat (P1-first: intro, tijdlijnregel "first cook" en chef-tip alleen bij kookgerei, via {% if %})
→ TRIGGER SPLIT P2: Items contains-any KOOK_TITELS + SET_TITELS
     JA  → (conditional wait Delivered Shipment) → P2
     NEE → geen P2
→ wacht tot dag 14, 10:00
→ CONDITIONAL SPLIT: ORDER_2 → JA: geen P3 (VIP V1 op dag 30 neemt het over)
→ TRIGGER SPLIT A: Items contains-any KOOK_TITELS + SET_TITELS
   JA (kookgerei of set)
     → TRIGGER SPLIT A1: $value >= 300 OR Items contains-any SET_TITELS     → P3-set
     → TRIGGER SPLIT A2: Items contains-any "Stainless Steel Lid", "Titanium Hammered Pan Pro With Lid" → P3-next (hoofdkaart snijplank)
     → TRIGGER SPLIT A3: Items contains-any PANPRO_TITELS + VORM_TITELS     → P3-pan (dekseltekst "pick the same diameter")
     → anders (pizza steel, roasting pan, pots)                             → P3-accessory ("Now meet the pan")
   NEE (alleen accessoires)
     → TRIGGER SPLIT B1: Items contains "E-Gift Card"                       → geen P3 (UYALJ8 bestaat)
     → CONDITIONAL SPLIT B2: HEEFT_KOOKGEREI                                → P3-next (hoofdkaart deksel, of snijplank als er een deksel in de order zat)
     → TRIGGER SPLIT B3: Items contains-any de vier schorttitels            → P3-apron
     → anders                                                                → P3-accessory
→ P4 review (XzHrez, ongewijzigd)
```

Deep pan 24 cm (Standard) heeft geen deksel. P3-pan zegt nu "Pick the same diameter as your pan" en de lid-PDP toont de maten; een aparte uitsluiting op variant kan alleen via `$extra.line_items[].variant_title`, wat in een flow-split niet kan. Acceptabel risico, wel in Gorgias bekend.

Prijzen in P3-next en P3-apron alleen bij `event.extra.shipping_address.country_code == 'US'` (gebouwd). P3-pan, P3-set en P3-accessory tonen nog USD aan iedereen: zelfde regel toevoegen (zie 04).

## 6. Winback

```
Trigger: Placed Order → wacht 60 dagen (ongewijzigd)
→ TRIGGER SPLIT: Items contains-any KOOK_TITELS + SET_TITELS
   JA  → bestaande split pan/set → R1-pan (deksel-rij verborgen als de order al een deksel had) / R1-set
   NEE → CONDITIONAL SPLIT HEEFT_KOOKGEREI → JA: R1-pan · NEE: R1-acc
→ wacht 30 dagen → R2 / R2-VIP (ongewijzigd)
```

## 7. Nieuwe flows

| Flow | Wijziging |
| --- | --- |
| UGC first egg (U1) | Flow filter erbij: `HEEFT_KOOKGEREI` (de trigger Delivered Shipment heeft geen Items) |
| Anniversary (N1, N2) | Trigger filter: Placed Order `Items` contains-any KOOK_TITELS + SET_TITELS. Eerste orders zonder kookgerei krijgen N1 niet ("six months on titanium") |
| VIP (V1, V2) | Geen wijziging; P3 wijkt bij order 2 (zie 5) |
| Site (A1, A2), Sunset (S1, S2) | Geen wijziging |

## 8. Dynamische content: wat binnen één template blijft

Alle condities gebruiken alleen velden die in de echte events bestaan (00-data.md) en zijn getest met Django, dezelfde templatetaal als Klaviyo, op geanonimiseerde voorbeeld-events: `research/tailoring/test/run_tests.sh` (44 controles, alle groen).

| Template | Conditie (letterlijk) | Effect |
| --- | --- | --- |
| C1, C4-US, P1-first | `{% if 'Hammer' in event.Items\|join:',' or 'Pan' in event.Items\|join:',' or 'Pot' in event.Items\|join:',' or 'ookware' in event.Items\|join:',' or 'Everything' in event.Items\|join:',' or 'fanne' in event.Items\|join:',' or 'Prep Bundle' in event.Items\|join:',' %}` | Pan-uitleg, 12-pcs-alternatief, eerste-ei-tijdlijn en chef-tip alleen bij kookgerei |
| C2-acc | `{% if 'Apron' in event.Items\|join:',' %}` (en idem Cutting Board, Lid, Mill, Utensil/Chopsticks, Gift Card, Dishwasher Sheets) | Eén feitregel per accessoiretype in de cart |
| C3-acc | `{% if 'Apron' in event.Items\|join:',' %}` | Zin "An apron does want something to cook in" |
| K1-acc | `{% if 'Apron' in event\|lookup:'Product Name' %}...{% elif ... %}` en `{% if event.Price and event\|lookup:'$currency' == 'USD' %}` | Subregel en feitregel per product; prijs alleen in USD |
| K1, K2-new, K2-returning, K3 | `{% if event.Price and event\|lookup:'$currency' == 'USD' %}` | Geen "$" voor SGD/AUD/EUR-bedragen |
| B1, B2-notclicked | `{% if 'Set' in event.Name or 'Edition' in event.Name or 'Bundle' in event.Name or 'Duo' in event.Name or 'Kit' in event.Name %}set{% else %}pan{% endif %}` | "Get 10% off this set" |
| B1-acc, B2-clicked | kookwoorden op `event.Name`; accessoirewoorden met `{% elif %}` | Subregel klopt (geen "pure titanium cooking surface" onder een stalen deksel) |
| P3-next | `{% if 'Lid' in event.Items\|join:',' %}` (hoofdkaart plank, anders deksel), `{% if 'Wok' not in ... %}`, `{% if event.extra.shipping_address.country_code == 'US' %}` | Geen deksel aan wie hem net kocht; geen wok aan wie een wok heeft; prijzen alleen US |
| R1-pan | `{% if 'Lid' not in event.Items\|join:',' %}` | Deksel-rij weg bij pan + deksel |

Eén keer controleren in Klaviyo zelf (preview met een echt profiel) vóór livegang: `join` op `event.Items` en `in` in een `{% if %}` zijn standaard Django en worden door Klaviyo ondersteund, maar Klaviyo is geen volledige Django-kopie.

## 9. Varianten: totaal

Nieuw: 7 templates (C2-acc, C3-acc, K1-acc, B1-acc, P3-next, P3-apron, R1-acc). Gewijzigd: 12 (C1, C4-US, K1, K2-new, K2-returning, K3, B1, B2-clicked, B2-notclicked, P1-first, P3-pan, R1-pan). Geen aparte schort-, gift-card-, deksel- of plankvarianten in checkout, cart of browse: die zitten als feitregels in de -acc templates.
