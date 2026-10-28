# A/B-tests Q4 · Checkout en cart (28 okt 2026)

Vraag Floris: zoveel mogelijk optimaliseren vóór Black Friday. Dit deel gaat over **v4 · Checkout abandonment `QUBUQV`** en **v4 · Cart abandonment `TZG9Mx`** (beide live), met de oude armen in dezelfde flows (achter de oud/nieuw-splits `119850583` en `119850622`, beide sinds 19 okt op 100% nieuw). De oude losse flows (`Y2TmNB`, `Tsg2tV`, `SwkMyn`, `TBWngE` en ouder) staan op Draft en versturen niets.

Alleen gelezen. Klaviyo (account TdtTzz, revision 2025-10-15): flowdefinities, flow-messages en live templates van C1, C2, K1 en K2-NEW; `POST /api/flow-values-reports` per bericht over **14 okt 00:00 tot 28 okt 00:00 UTC** (conversie Placed Order `RSNxYV`), gecontroleerd tegen `metric-aggregates` op Placed Order per `$attributed_flow` en `$attributed_message` (zelfde orders, verschil hooguit 1 order per mail); Clicked Email `W247h8` per `$message` met `Bot Click` = 0; Unsubscribed `YcWddQ` als losse events per `message_id`; `flow-series-reports` per dag vanaf 8 okt; Checkout Started `RfMvni` en Added to Cart `QXcV8K` (Shopify; `SRYm9S` is de API-variant, niet gebruikt). Voor de afmeldanalyse: de 47 afmelders uit checkout en een willekeurige steekproef van 91 checkout-ontvangers, met hun mails in de dagen eromheen. Niets gewijzigd in Klaviyo, niets verstuurd. Profiel-ID's en ruwe events staan alleen in de scratchpad (`abq4/`); hier alleen aggregaten.

Regels (PLAYBOOK 6, plan van 19 okt): één variabele per test, winnaar op unieke kliks met omzet per ontvanger als controle, geen automatische winnaar, minstens vier weken, maximaal 2 tests per flow, bij twijfel wint A. Copy volgens de skill siraat-direct-response en DECISIONS (Benjamin, 30-day returns, 75-year warranty, 100,000+ happy customers).

---

## 1. Samenvatting

1. **Checkout maakte in 14 dagen $11.664 op 3.417 mails: $3,41 per ontvanger** ($3,99 per afgeleverde mail), 14,3 orders per 1.000 mails. Cart: **$10.314 op 5.336 mails, $1,93 per ontvanger**. De briefingcijfers ($4,53 en $2,26) komen uit een ander venster; het verschil in checkout zit vooral in de bouncegolf van C1 (punt 5).
2. **De afmeldpieken in checkout komen van C2** (`RZpvpp`, "Has the pan in your cart been tested?", 24 uur na C1): 2,38% per mail, 14 van de 43 afmeldingen, het dubbele van C1 (1,52%) en vier keer de latere mails. Wie zich afmeldt is meestal (77%) een **aanmelder van 0 tot 3 dagen oud** die in 26 uur W1, C1 en C2 kreeg (de checkoutflow mailt vooral zulke nieuwe aanmelders: 68% van de ontvangers); 11 van de 16 afmeld-events op C2 komen via de afmeldknop van de mailbox. De twee "dagen boven 2%" zijn toeval rond een structureel te hoog niveau: bij gemiddeld 3 afmeldingen per dag verwacht je 2 tot 3 dagen met 5 of meer in twee weken. Details in sectie 3.
3. **T02 (code tegen geen code) in checkout en cart:** code 1.165 ontvangers, 2,6% klik, 4 orders, $939 ($0,81 per ontvanger); geen code 1.123, 1,1% klik, 1 order, $156 ($0,14). Klik significant (p = 0,008), orders niet (p = 0,38). Afmelding gelijk (1,21 tegen 1,25%). Codes stapelen op de sale (DECISIONS 19 okt), dus **advies: T02 in checkout en cart van 1 nov tot 6 dec op 100% code**, hervatten in december.
4. **T14 (C1-onderwerp) is nooit gestart** en **T18 (K1-onderwerp) nog niet**: in beide flows staat geen enkele A/B-actie. Er zijn dus ook geen variaties die via de API te patchen zijn: elke onderwerp- of inhoudstest hier is een nieuwe A/B in de UI, elke timing- of extra-mailtest een nieuwe split in de UI. Alleen de bestaande random splits (T02 en oud/nieuw) zijn via de API aan te passen.
5. **Bijvangst:** C1 had van 12 tot 21 okt een bouncegolf (456 van 1.314 in het venster, op 19 okt 117 van 177), sinds 22 okt onder 5%. Daardoor kreeg C2 tot 22 okt weinig volume en lijkt het afmeldprobleem "nieuw". Verder: smart sending staat uit in beide flows, en C1, C2 en de cartmails zeggen "Your 4 gifts end when the fall sale ends" terwijl de gifts in november doorlopen [VRAAG FLORIS: blijft die regel kloppen na 31 okt?].
6. **Top van de nieuwe tests** (sectie 5, gesorteerd op verwachte extra omzet per week): HI10 al in K1 ($200 tot $1.100), een cartmail op dag 7 over betalen in termijnen naar het HexClad-patroon ($200 tot $600), een checkoutmail op dag 14 met hetzelfde bezwaar ($120 tot $300), het C1-onderwerp ($0 tot $330), C2 naar 48 uur tegen de afmeldingen. Geen enkele test haalt vóór BFCM een harde uitslag op orders; vóór 20 nov zie je hooguit de richting bij een groot effect. Besluiten vallen in december.

---

## 2. Cijfers per mail en per arm, 14 dagen (14 tot 28 okt)

Klik = unieke menselijke klik (`Bot Click` = 0) per afgeleverde mail. Orders en omzet = Klaviyo-toeschrijving (Placed Order). Omzet per ontvanger = omzet gedeeld door ontvangers inclusief bounces (zoals Klaviyo). Afmelding per afgeleverde mail. Bounce per ontvanger.

### Checkout `QUBUQV`

| Mail | Bericht | Arm | Ontvangers | Klik | Orders | Omzet | Per ontv. | Afmelding | Spam | Bounce |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | WhTznn | nieuw | 1.314 | 72 (8,4%) | 30 | $6.577 | $5,01 | 13 (1,52%) | 0 | 456 (34,7%) |
| C2 | RZpvpp | nieuw | 592 | 23 (3,9%) | 9 | $2.294 | $3,87 | **14 (2,38%)** | 0 | 4 (0,7%) |
| C3-P | WF2QWP | nieuw | 305 | 4 (1,3%) | 0 | $0 | $0,00 | 4 (1,32%) | 0 | 1 (0,3%) |
| CODE · C4 (T02-A) | RKvJmd | nieuw | 293 | 7 (2,4%) | 2 | $691 | $2,36 | 3 (1,03%) | 1 | 2 (0,7%) |
| C4 nocode · T02-B | SUUzf5 | nieuw | 258 | 4 (1,6%) | 0 | $0 | $0,00 | 1 (0,39%) | 0 | 1 (0,4%) |
| C3-S | VvC24X | nieuw | 163 | 3 (1,9%) | 2 | $1.090 | $6,69 | 2 (1,23%) | 0 | 1 (0,6%) |
| C3-ACC | Rd7W5Y | nieuw | 87 | 1 (1,2%) | 0 | $0 | $0,00 | 0 | 0 | 1 (1,1%) |
| C2-ACC | UXedMJ | nieuw | 85 | 2 (2,4%) | 1 | $79 | $0,93 | 1 (1,18%) | 0 | 0 |
| C4 nocode · cooldown | UaWEuj | nieuw | 2 | 0 | 0 | $0 | $0,00 | 0 | 0 | 0 |
| Old · Checkout 1 | VESwKK | oud | 59 | 3 (9,4%) | 2 | $295 | $4,99 | 2 (6,25%) | 0 | 27 (45,8%) |
| Old · Checkout 2 | VAfgqm | oud | 32 | 1 (3,1%) | 1 | $150 | $4,69 | 0 | 0 | 0 |
| Old · Checkout 3 | SxMhEC | oud | 39 | 3 (7,7%) | 1 | $285 | $7,31 | 0 | 0 | 0 |
| Old · Checkout 4 | W3ZNkc | oud | 91 | 2 (2,2%) | 0 | $0 | $0,00 | 2 (2,22%) | 0 | 1 (1,1%) |
| Old · Checkout 5 | YnPu7U | oud | 97 | 3 (3,1%) | 1 | $203 | $2,09 | 1 (1,04%) | 0 | 1 (1,0%) |
| **Totaal** | | | **3.417** | **127 (4,3%)** | **49** | **$11.664** | **$3,41** | **43 (1,47%)** | **1** | **495 (14,5%)** |

De oude arm is een staart van wie vóór 19 okt instroomde; de laatste oude mail ging op 24 okt.

### Cart `TZG9Mx`

| Mail | Bericht | Arm | Ontvangers | Klik | Orders | Omzet | Per ontv. | Afmelding | Spam | Bounce |
|---|---|---|---|---|---|---|---|---|---|---|
| K1 | Vb6YFp | nieuw | 1.848 | 72 (3,9%) | 17 | $5.692 | $3,08 | 12 (0,66%) | 2 | 16 (0,9%) |
| K2-NEW | Ti3QPw | nieuw | 1.471 | 31 (2,1%) | 5 | $1.178 | $0,80 | 12 (0,82%) | 2 | 12 (0,8%) |
| CODE · K3 · pan (T02-A) | SApxRv | nieuw | 656 | 15 (2,3%) | 1 | $160 | $0,24 | 8 (1,23%) | 0 | 8 (1,2%) |
| K3 · pan nocode · T02-B | WbfiSt | nieuw | 643 | 7 (1,1%) | 1 | $156 | $0,24 | 10 (1,56%) | 0 | 3 (0,5%) |
| K1-ACC | SKE4yh | nieuw | 174 | 8 (4,6%) | 5 | $412 | $2,37 | 5 (2,89%) | 0 | 1 (0,6%) |
| K2-RETURNING | TV4Ts9 | nieuw | 135 | 7 (5,2%) | 1 | $797 | $5,90 | 0 | 0 | 0 |
| K3 · acc nocode · T02-B | Xrhq7H | nieuw | 77 | 0 | 0 | $0 | $0,00 | 2 (2,63%) | 0 | 1 (1,3%) |
| CODE · K3 · acc (T02-A) | TQrD6K | nieuw | 66 | 5 (7,6%) | 1 | $88 | $1,33 | 2 (3,03%) | 0 | 0 |
| K3 cooldown (pan en acc) | UZQtYB, WSTBQu | nieuw | 2 | 1 | 0 | $0 | $0,00 | 0 | 0 | 0 |
| Old · Cart 1 | VN83i2 | oud | 84 | 5 (6,0%) | 3 | $834 | $9,93 | 1 (1,19%) | 0 | 0 |
| Old · Cart 2 | WkvPzf | oud | 96 | 5 (5,2%) | 1 | $789 | $8,22 | 5 (5,21%) | 0 | 0 |
| Old · Cart 3 | UtsFHn | oud | 84 | 1 (1,2%) | 1 | $209 | $2,48 | 0 | 0 | 0 |
| **Totaal** | | | **5.336** | **157 (3,0%)** | **36** | **$10.314** | **$1,93** | **57 (1,08%)** | **4** | **41 (0,8%)** |

Lezing:

- **Checkout leunt op C1 en C2** (75% van de omzet). C3-P, C3-ACC, C2-ACC en de nocode-C4 maken samen 1 order op 735 mails.
- **Cart leunt op K1** (55%). K3 maakt in beide T02-armen $0,24 per ontvanger; de hele derde stap is zwak.
- **Oude cart-arm tegen nieuw** (oud/nieuw-test T01, gesloten op 19 okt): sinds 12 okt maakte de oude arm 5 orders en $1.832 op ongeveer 190 instromers (~$9,40 per instromer), de nieuwe arm met hetzelfde instapvenster 14 orders en $3.890 op 979 instromers ($3,97). Klein en niet significant (p ≈ 0,2), maar wel dezelfde kant op als eerder (19 okt: oud voor op orders). Het verschil tussen de armen zit vooral in het aanbod: de oude cart gaf 10% in mail 2, de nieuwe pas in K3 op dag 3. Dat is test T21.

### Volume per dag (basis voor alle schattingen)

| Mail | Per dag | Per arm bij 50/50 | Opmerking |
|---|---|---|---|
| C1 | ~70 echt afgeleverd (94 inclusief de bouncegolf) | 35 | sinds 22 okt bounce onder 5% |
| C2 | ~50 (was ~35 tijdens de bouncegolf) | 25 | |
| C3-P / C3-S / C3-ACC | 22 / 12 / 6 | | te klein voor een eigen test |
| C4 (beide T02-armen) | ~40 | 20 | |
| K1 / K1-ACC | 132 / 12 | 66 | |
| K2-NEW / K2-RETURNING | 105 / 10 | 52 | |
| K3 (alle armen) | ~103 | 51 | |

---

## 3. Waarom checkout boven 2% afmelding uitkwam

### Wat de dagrapporten zagen

Op 25 okt (24 uur tot 08:50 UTC) 5 afmeldingen op 203 mails (2,53%), op 28 okt 5 op 236 (2,17%). Per kalenderdag (UTC): 24 okt 8 afmeldingen (C1 4, C2 2, CODE · C4 2), 28 okt tot 16:00 al 6 (C2 4).

### Welke mail

Over 14 dagen, alleen de nieuwe arm:

| Mail | Afgeleverd | Afmeldingen | Per mail | Via mailboxknop |
|---|---|---|---|---|
| **C2** | 588 | **14** | **2,38%** | 11 |
| C1 | 858 | 13 | 1,52% | 13 van 14 events |
| C3-P | 304 | 4 | 1,32% | 2 |
| C4 (code en nocode) | 548 | 4 | 0,73% | 3 |
| C3-S, C2-ACC, C3-ACC | 333 | 3 | 0,90% | 0 |

C2 en C1 samen leveren 63% van de afmeldingen. C2 is de enige mail die structureel boven 2% zit. Dat past bij de geschiedenis: de oude "EB / DEC 25 / Checkout Abandonment / Triple Pixel · Email #2" zat in september en oktober ook op 2,26% (afmeldingen/01-data.md). De tweede checkoutmail is al langer het zwakke punt.

### Wie zich afmeldt (47 afmelders, inclusief de oude-armstaart, tegen een steekproef van 91 checkout-ontvangers)

| Kenmerk | Afmelders | Ontvangers (steekproef) |
|---|---|---|
| 0 tot 3 dagen op de lijst | 77% | 68% |
| Bron Alia (giveaway-pop-up) | 60% | 59% |
| Welkomstmail in dezelfde 48 uur | 60% | ~51% |
| US-profiel | 47% | 46% |
| Campagnemail in de 48 uur ervoor | 15% | |

- **De checkoutflow mailt vooral gloednieuwe aanmelders.** Van de afgeleverde C1's in de steekproef kreeg 84% binnen 2 uur ook een welkomstmail (vrijwel altijd W1): pop-up, dan checkout, dan W1 en C1 vlak na elkaar, de volgende dag C2. Voor die groep is C2 de derde mail in ongeveer 26 uur.
- **Het is niet de markt en niet de campagnedruk.** US en niet-US zijn even vertegenwoordigd als in de ontvangers, en 40 van de 47 kregen in de 48 uur ervoor geen campagne.
- **Het is geen inhoudswijziging.** De templates van C1 en C2 zijn sinds 19 okt 17:29 UTC niet aangeraakt.
- **De afmeldknop van de mailbox domineert** (30 van 47). Wie zo afhaakt ziet alleen afzender, onderwerp en preview. Bij C2 is dat "Siraat's Kitchen", "Has the pan in your cart been tested?" en "Two years ago I started reading about PFAS. Report no. 25895 is the answer.": een derde mail met een vraag over giftigheid, de dag na de vorige twee.

### Toeval of probleem

Gemiddeld 3 afmeldingen per dag op ~210 mails. Bij een Poisson-verdeling is de kans op 5 of meer op één dag 17 tot 20%: in 14 dagen verwacht je 2 tot 3 zulke dagen. **De twee pieken zijn dus geen incident.** Het probleem is het niveau: 1,47% over de hele flow (PLAYBOOK 6: boven 1% is een probleem), gedragen door C2. Dat werd zichtbaarder na 22 okt: toen stopte de bouncegolf op C1 en kreeg C2 40% meer volume (van ~35 naar ~50 per dag).

### Conclusie en wat eraan te doen

**Oorzaak: C2 (`RZpvpp`) als derde mail in 26 uur voor aanmelders van 0 tot 3 dagen oud, die tegelijk W1 en C1 kregen.** Twee knoppen, allebei te toetsen in plaats van blind te wijzigen:

1. Timing: C2 naar 48 uur (test T22, sectie 5). Raakt de stapeling direct.
2. Onderwerp en preview van C2: van giftigheid naar hun cart en het bewijs (test T26, na BFCM; C2 kan maar één test tegelijk dragen).

Snelle maatregel zonder test, alleen na akkoord Floris: smart sending aanzetten op C2 (staat uit in beide flows). Nadeel: wie binnen 16 uur een welkomstmail kreeg, mist C2, en C2 maakt $3,87 per ontvanger. Daarom liever T22.

---

## 4. Lopende tests

| Test | Waar | Stand 28 okt | Advies |
|---|---|---|---|
| **T01 checkout** (oud/nieuw) | split `119850583` op 100% nieuw | gesloten 19 okt, staart oude arm tot 24 okt | klaar. Oude mails blijven staan als rollback |
| **T01 cart** (oud/nieuw) | split `119850622` op 100% nieuw | gesloten 19 okt (DECISIONS), niet 31 okt zoals het plan van 19 okt zei. Oud ~$9,40 per instromer tegen nieuw $3,97, 5 tegen 14 orders, p ≈ 0,2 | niet heropenen; de vraag erachter (korting eerder) toetsen in T21 |
| **T02 checkout** (C4) | split `119850619` 50/50 | code 311 ontv. sinds 8 okt, 2,3% klik, 2 orders, $691; geen code 285, 1,4%, 0 orders | zie hieronder |
| **T02 cart** (K3 pan en acc) | splits `119850645` en `119850638` 50/50 | pan: code 776, 2,3% klik, 1 order $160; geen code 757, 1,1%, 1 order $156. Acc: code 78, 6,4%, 1 order; geen code 81, 0 kliks | zie hieronder |
| **T02 checkout + cart samen** | | code 1.165 ontv., 2,6% klik, 4 orders, $939, $0,81 per ontv., afmelding 1,21%; geen code 1.123, 1,1%, 1 order, $156, $0,14, 1,25%. Klik p = 0,008, orders p = 0,38 | **1 nov tot 6 dec op 100% code** (splits op 100 naar de code-tak; kan via de API door de percentage van de splitactie te patchen). Codes stapelen op 50 en 70% (DECISIONS 19 okt), de code-arm wint op klik en kost geen extra afmeldingen. Hervatten 7 dec, eindbesluit 31 jan zoals gepland. Waarde: ~$260 per week (nocode-ontvangers x verschil per ontvanger) |
| **T14** C1-onderwerp | C1 `119850587` | **niet gestart**, C1 is een gewone send-email | starten (test T14 hieronder) |
| **T18** K1-onderwerp | K1 `119850627` | gepland 1 nov, niet gestart | na T21, want K1 kan één test dragen |

---

## 5. Voorstel: zeven tests, gesorteerd op verwachte extra omzet per week

Rekenbasis. Omzet per week = de helft van de 14 dagen: checkout $5.832 (C1 $3.289, C2 $1.147), cart $5.157 (K1 $2.846). "Extra per week" = bij uitrol van de winnaar op het huidige volume, zonder BFCM-opslag; in november 2 tot 3 keer zoveel. Power: tweezijdig 5%, 80% power, 50/50.

**Wat haalbaar is.** Omzet per ontvanger heeft per mail een standaardafwijking van ~$40 (2,3% koopt, gemiddelde order ~$240). Een verschil van 30% in omzet per ontvanger zien vraagt ~11.000 ontvangers per arm: geen enkele mail hier haalt dat in Q4. Daarom per test drie lagen: (1) klik als snelle maat, (2) omzet per ontvanger als besluitmaat met een vooraf vastgelegde regel (uitrol als P(B beter) ≥ 80% op omzet per ontvanger en klik dezelfde kant op wijst, anders blijft A), (3) afmelding en spam als harde bewakers (stop bij afmelding +50% relatief of meer dan 1 spamklacht per 1.000 in de B-arm).

Kleinste zichtbare verschil (MDE) per maat:

| Maat | Per arm per dag | 21 dagen (tot 20 nov) | 28 dagen | 28 dagen met BFCM-volume (x2,5) |
|---|---|---|---|---|
| C1 klik (8,4%) | 35 | 48% | 42% | 26% |
| C1 orders (2,3%) | 35 | 95% | 82% | 52% |
| K1 klik (3,9%) | 66 | 52% | 45% | 29% |
| K1 orders (0,9%) | 66 | 112% | 97% | 61% |
| Hele cartpad, orders per instromer (1,5%) | 75 | 81% | 70% | 44% |
| C2 klik (3,9%) / afmelding (2,4%) | 25 | 84% / 110% | 73% / 95% | 46% / 60% |
| Extra mail tegen geen mail, orders (1%) | 50 (cart) / 20 (checkout) | 127% / 190% | 110% / 166% | 69% / 105% |

Klaviyo-uitvoerbaarheid in het kort: er staan **geen A/B-acties** in `QUBUQV` en `TZG9Mx`, dus "variaties patchen via de API" kan hier nergens. Elke onderwerp- of inhoudstest = **UI: mail aanklikken > Create A/B test** (winnaar op unieke kliks, automatische winnaar uit, 50/50, variaties `<mail> · T<nr>-A/-B`, Start test). Timing en extra mails = **UI: random split (profile sample 50%) plus nieuwe acties**; de API kan in een bestaande flow geen acties toevoegen (PATCH op `/api/flows/` neemt geen definition). Via de API kan wel: percentages van bestaande splits en de template van een bestaande send-email patchen (`PATCH /api/flow-actions/{id}`). Een cloudsessie in Auto-modus mag dat bij live flows niet (PLAYBOOK 9).

### 1. T21 · K1 met HI10 al toegepast (aanbod)

| | |
|---|---|
| Flow / mail | Cart `TZG9Mx`, K1 (actie `119850627`, bericht `Vb6YFp`). K1-ACC niet (te klein) |
| Hypothese | De cart laat de korting liggen tot K3 op dag 3, terwijl C1 met HI10 al toegepast $5,01 per ontvanger maakt en K1 $3,08. De oude cart (10% in mail 2) deed ~$9,40 per instromer tegen $3,97 nieuw. In een sale waarin HI10 stapelt op 50 en 70%, is een korting die al in de cart staat het sterkste duwtje voor iemand die nog niet aan checkout begon |
| Variabele | Aanbod. A = huidige K1 (geen code). B = zelfde K1, alleen de codebalk "EXTRA 10% ALREADY APPLIED · CODE HI10", de regel onder de cart "Your extra 10% is already applied with the button below." (letterlijk uit C1) en de knoplinks met `https://siraatskitchen.com/discount/HI10?redirect=/cart`. Onderwerp, preview, hero en blokken gelijk |
| Maat | Omzet per K1-ontvanger over de hele cartpad (alle aan TZG9Mx toegeschreven orders per arm, via `$attributed_variation` en profielen per arm), na korting. Bewakers: afmelding K1, spam, en K3-codegebruik (B krijgt in K3 nog steeds een code) |
| Looptijd en power | K1 66 per arm per dag. Op orders in 21 dagen alleen +112% zichtbaar, met BFCM-volume in 28 dagen +61%. Het verwachte effect (oud tegen nieuw) is van die orde, dus een richting vóór BFCM is mogelijk; besluit in december op de Bayes-regel |
| Verwachte extra omzet | Cartomzet $5.157 per week. Orders +15 tot 35%, min 10% op de orders die toch al kwamen: **+$200 tot +$1.100 per week**, midden ~$650. In november x2 tot x3 |
| Risico | Middel. Marge: 10% extra korting op cartorders bovenop 50 tot 70%. Kan K3 (unieke code) uithollen; K3 is nu al zwak ($0,24). HI10 is eenmalig per klant (Shopify), dus geen dubbele korting. Strijdig met DECISIONS 8 okt ("geen HI10 in K1 en K2"): **[VRAAG FLORIS: akkoord om dit te toetsen?]** |
| Klaviyo | UI: A/B op K1, variatie B kiest een nieuwe template. Claude bouwt `klaviyo/templates/v3/cart/k1-hi10.html` als kopie van `k1.html` (vaste header en footer, codebalk-blok, QA-scripts), na akkoord |
| Klaar vóór BFCM | Start 1 nov. Richting rond 20 nov als het effect groot is, besluit 7 dec of later. Blokkeert T18 tot het besluit |

### 2. T23 · Cart: extra mail op dag 7 over betalen in termijnen (HexClad, idee 30)

| | |
|---|---|
| Flow / mail | Cart `TZG9Mx`, nieuwe stap K4 na K3 (pan- en acc-pad), alleen US |
| Hypothese | Prijs is het grootste bezwaar (27% twijfelde, survey). HexClad beantwoordt dat aan het eind van de cartflow, 7 dagen na de vorige mail, met Affirm en zonder korting ("Price holding you back? We got you.", concurrenten/overzicht idee 8 en 30). Wij hebben Shop Pay Installments en Affirm (DECISIONS 7 okt; Affirm-app $6.300 per maand, AOV $333, payments/02-advies-bnpl.md), en de cartmails noemen het nergens. Een rustige mail na een lange pauze haalt kopers terug zonder extra korting en met weinig afmeldrisico |
| Variabele | Extra mail tegen geen mail (holdout). Random split 50% na K3, wacht tot dag 7 na de cart, 09:00 lokaal. Beide takken zetten een profieleigenschap (`ab_k4 = mail` of `control`) voor de meting |
| Maat | Alle orders (niet alleen toegeschreven) per profiel in de split binnen 14 dagen na het splitmoment, omzet per profiel. Bewakers: afmelding en spam van K4 |
| Looptijd en power | ~50 per arm per dag. Bij 1% kopers in die fase in 28 dagen pas +110% zichtbaar, met BFCM-volume +69%. Dit is een waardetest: rol uit bij P(mail beter) ≥ 80% en afmelding onder 1% |
| Verwachte extra omzet | ~700 profielen per week bereiken dag 7. K3 zelf converteert 0,15%; een mail met een nieuw argument 0,1 tot 0,3% erbij x AOV cart $287 = **+$200 tot +$600 per week** |
| Risico | Laag tot middel: een vijfde mail. Alleen US (de termijnregel mag in US-mails, DECISIONS 7 okt). Geen bedragen per maand noemen zonder Shopify-bevestiging |
| Klaviyo | UI: na K3 een conditional split "random sample 50%", in de mailtak een delay en de nieuwe mail. Claude bouwt `cart/k4-installments.html` |
| Klaar vóór BFCM | Bouw 29 tot 31 okt, start 1 nov. Eerste mails vanaf 8 nov, dus vóór BFCM alleen ~12 dagen data: geen besluit vóór december. Wel direct waarde in de sale als het werkt |

Copy K4 (US, kalm register, 60 tot 180 woorden, Benjamin):

- Vijf onderwerpen: curiosity + benefit "The pan in your cart, paid over time" / specificity "Covered for 75 years, paid over a few months" / question "Is the price what stopped you?" / story `"The last pans we ever have to purchase"` (bestaande reviewquote uit K2-NEW, opnieuw controleren met check_reviews.py) / offer "Pay over time at checkout". **Kies: "Is the price what stopped you?"** (vraag, sluit aan op HexClad; alleen deze, het is een holdout).
- Preview: "Shop Pay Installments and Affirm are at checkout. Your cart is still saved."
- Hero: label "STILL IN YOUR CART" / "Same pan.|Paid over time." / subline "Covered for 75 years, not 5."
- Opener: "Say a good coated pan lasts 5 years. Ours is covered for 75. That's the math, and it's still a lot to pay at once." Dan: "So you don't have to. Pick Shop Pay Installments or Affirm at checkout and spread it out." Dan bewijs: "No coatings, a pure titanium cooking surface, tested by Light Labs, report no. 25895."
- Knop "Return to my cart", eronder "Free shipping. 30-day returns. 100,000+ happy customers." Ondertekening "Benjamin / Founder, Siraat's Kitchen", "Reply and our team will help."
- Vaste header en footer, cart-blok en productkaart via de blokken (PLAYBOOK 11 en 12).

### 3. T24 · Checkout: extra mail op dag 14 over prijs en garantie

| | |
|---|---|
| Flow / mail | Checkout `QUBUQV`, nieuwe stap C5 na C4 (alle takken), alleen US |
| Hypothese | Zelfde als T23, nu bij wie al aan checkout begon. HexClad stuurt de prijsmail op dag 14 (7 dagen na de vorige). Wie na C4 niet koopt, struikelt meestal over het bedrag, niet over het bewijs |
| Variabele | Extra mail tegen geen mail, random 50% na C4, mail op dag 14 na de checkout, 09:00 lokaal. Profieleigenschap `ab_c5` per tak |
| Maat | Alle orders per profiel in de split binnen 14 dagen na het splitmoment. Bewakers: afmelding en spam |
| Looptijd en power | ~20 per arm per dag: in 28 dagen alleen +166%, met BFCM-volume +105%. Beslissen samen met T23 (zelfde idee, gepoold als één hypothese "termijnmail aan het eind") |
| Verwachte extra omzet | ~250 per week op dag 14 zonder order x 0,2 tot 0,5% extra kopers x AOV checkout $238 = **+$120 tot +$300 per week** |
| Risico | Laag. Lange pauze na C4. De copy mag niet terugverwijzen naar de C4-code (die is dan verlopen) |
| Klaviyo | UI: split, delay, mail. Template `checkout/c5-installments.html` = K4-copy met "checkout" in plaats van "cart" en het blok `{{BLOCK:cart}}` van checkout |
| Klaar vóór BFCM | Start 1 nov, eerste mails vanaf 15 nov. Geen besluit vóór december |

### 4. T14 · C1-onderwerp "Don't leave these hanging"

| | |
|---|---|
| Flow / mail | Checkout `QUBUQV`, C1 (actie `119850587`, bericht `WhTznn`) |
| Hypothese | Ongewijzigd uit het plan van 19 okt: "Don't leave these hanging" stond op alle zeven historische checkout-1-varianten met samen $194.000 omzet. Eerder gepland voor 22 okt, nooit gestart |
| Variabele | Onderwerp. A "Your cart + 4 gifts are still pending", B "Don't leave these hanging". Preview gelijk ("They ship the moment you place the order. One tap left.") |
| Maat | Unieke klik, controle omzet per ontvanger, bewaker afmelding (C1 nu 1,52%) |
| Looptijd en power | 35 per arm per dag: klik +48% in 21 dagen, +42% in 28, met BFCM-volume +26%. Realistisch 6 weken |
| Verwachte extra omzet | C1 $3.289 per week, winnaar +0 tot 10%: **$0 tot $330 per week** (A is al sterk) |
| Risico | Laag. Beide onderwerpen noemen geen korting, dus sale-neutraal. A noemt "4 gifts": die blijven in november (DECISIONS 19 okt) |
| Klaviyo | UI: Create A/B test op C1 |
| Klaar vóór BFCM | Start 30 okt. Geen besluit vóór BFCM, beslissen in december met sale-dagen apart |

### 5. T18 · K1-onderwerp "we saved these for you" (na T21)

| | |
|---|---|
| Flow / mail | Cart `TZG9Mx`, K1 |
| Hypothese | Old · Cart 1 "Hi {{ first_name }}, we saved these for you" klikt nu 6,0% tegen K1 3,9% (klein volume) en haalde historisch $2,43 tot $2,66 op 71.417 ontvangers |
| Variabele | Onderwerp. A "The hammered pattern: an easy wipe", B "{{ first_name\|default:'Hi' }}, we saved these for you" |
| Maat | Unieke klik, controle omzet per ontvanger |
| Looptijd en power | Klik +45% in 28 dagen, met BFCM-volume +29% |
| Verwachte extra omzet | K1 $2.846 per week x 0 tot 8% = **$0 tot $230 per week** |
| Risico | Laag |
| Klaviyo | UI: A/B op K1. Kan pas na het T21-besluit, want K1 draagt één test. Als Floris T21 niet wil: T18 start 1 nov |
| Klaar vóór BFCM | Nee, tenzij T21 niet doorgaat |

### 6. T26 · C2-onderwerp: bewijs over hun cart in plaats van een vraag over giftigheid

| | |
|---|---|
| Flow / mail | Checkout `QUBUQV`, C2 (actie `119850597`, bericht `RZpvpp`) |
| Hypothese | Wie C2 wegklikt, ziet alleen de inbox. "Has the pan in your cart been tested?" plus de preview over PFAS leest voor een nieuwe aanmelder als de zoveelste angstmail. Een onderwerp over hun eigen cart en het rapportnummer houdt het bewijs maar zet de cart voorop: minder afmeldingen, minstens even veel klik |
| Variabele | Onderwerp en preview als één inbox-variabele (de afmeldknop reageert op allebei). Vijf onderwerpen: curiosity + benefit "The paper behind the pan in your cart" / specificity "Report no. 25895, for the pan in your cart" / question "Has the pan in your cart been tested?" (A) / story "Why I had our pan lab-tested" / offer "Your cart, the lab report, and 10% applied". **B: "Report no. 25895, for the pan in your cart"**, preview "Read the lab report yourself. Your cart and 4 gifts are still saved." |
| Maat | Omzet per ontvanger en klik; **afmelding hier als co-hoofdmaat** |
| Looptijd en power | 25 per arm per dag: afmelding pas bij -95% zichtbaar in 28 dagen. Alleen een groot effect wordt zichtbaar; anders telt het als richting |
| Verwachte extra omzet | C2 $1.147 per week x -5 tot +20% = **-$60 tot +$230 per week**, plus 2 tot 4 afmeldingen minder per week |
| Risico | Laag |
| Klaviyo | UI: A/B op C2 |
| Klaar vóór BFCM | Nee: C2 draagt eerst T22. Start 7 dec of na het T22-besluit |

### 7. T22 · C2 op 48 uur in plaats van 24 uur (timing, tegen de afmeldingen)

| | |
|---|---|
| Flow / mail | Checkout `QUBUQV`, wachttijd `119850595` vóór C2 |
| Hypothese | C2 is de derde mail in 26 uur voor aanmelders die W1 en C1 vlak na elkaar kregen (sectie 3). Een dag later valt hij niet meer in die golf, terwijl 86% van de checkoutorders na een mail binnen 48 uur valt (timing/02-advies.md): C1 heeft zijn werk dan gedaan |
| Variabele | Timing van C2: A 24 uur na C1 (nu), B 2 dagen na C1 tot 09:00 lokaal. Gevolg voor C3 en C4: in B schuiven ze een dag mee, dus de vergelijking is het hele pad vanaf C2 |
| Maat | Omzet per C1-ontvanger over C2 tot C4 en afmeldingen per C1-ontvanger over het pad. Doel: afmelding op C2 van 2,4% naar ~1,2% zonder omzetverlies |
| Looptijd en power | 25 per arm per dag. Een halvering van de afmelding is in 28 dagen niet hard te zien (MDE ~95%); met BFCM-volume ~60%. Besluit op de Bayes-regel; omzet per ontvanger mag niet meer dan 10% dalen |
| Verwachte extra omzet | **-$100 tot +$150 per week** (C2 $1.147 per week); het doel is ~3 afmeldingen per week minder op de checkoutflow (een derde van het probleem uit sectie 3) |
| Risico | Middel: later mailen kan C2-omzet kosten. De oude "mail 2 op dag 2" deed $0,41 tot $0,73 per ontvanger (timing/02-advies.md), al was dat een andere mail |
| Klaviyo | UI: vóór de wachttijd een conditional split "random sample 50%" met in de B-tak een eigen delay en kopieën van C2, C2-ACC en de rest van het pad (bestaande templates). Kan niet via de API. Alternatief zonder kopieën: smart sending op C2 (één vinkje, maar dan zonder meting) |
| Klaar vóór BFCM | Start 30 okt. In 3 weken alleen richting op afmelding; besluit begin december |

### Samenvattende tabel

| # | Test | Variabele | Extra per week | Flow-slot | UI of API | Start | Besluit |
|---|---|---|---|---|---|---|---|
| 1 | T21 K1 met HI10 | aanbod | +$200 tot +$1.100 | cart 1 | UI (A/B), template door Claude | 1 nov, na akkoord | dec |
| 2 | T23 K4 dag 7, termijnen | extra mail, bezwaar prijs | +$200 tot +$600 | cart 2 | UI (split + mail) | 1 nov | dec |
| 3 | T24 C5 dag 14, termijnen | extra mail, bezwaar prijs | +$120 tot +$300 | checkout 1 | UI (split + mail) | 1 nov | dec, gepoold met T23 |
| 4 | T14 C1-onderwerp | onderwerp | $0 tot +$330 | checkout 2 | UI (A/B) | 30 okt | dec |
| 5 | T18 K1-onderwerp | onderwerp | $0 tot +$230 | cart (na T21) | UI (A/B) | na T21 | jan |
| 6 | T26 C2-onderwerp | onderwerp + preview | -$60 tot +$230 | checkout (na T22) | UI (A/B) | 7 dec | jan |
| 7 | T22 C2 op 48 uur | timing | -$100 tot +$150, minder afmeldingen | checkout | UI (split) | 30 okt | dec |
| | T02 op 100% code (besluit, geen nieuwe test) | aanbod | ~+$260 | bestaand | API (split-percentage) of UI | 1 nov | hervatten 7 dec |

Let op de regel "maximaal 2 tests per flow". Checkout kan vóór BFCM T14 en één van T22 of T24 dragen, naast T02 (die op 100% staat en dus even niet telt). **Advies checkout: T14 en T22 vóór BFCM** (T22 is de afmeldfix), **T24 op 7 dec**. Cart: T21 en T23, T02 op 100%.

Niet voorgesteld:

- **Urgentie in de sale.** Halloween 70% en november 70% hebben geen bevestigde einddatum (DECISIONS 7 en 19 okt), en "70% ends" klopt niet als november ook 70% is. De enige echte deadline is de unieke code in C4 en K3 (48 uur); die zit al in T02.
- **Timing van C1** (10 tegen 30 minuten). De flow staat op 10 minuten (de template-notitie zegt 30). Het timingonderzoek zag bij 10 minuten +7% kopers, niet significant: weinig te winnen, veel te verliezen op de beste mail.
- **Productkaart.** De K1-v2-kaart (`cart/k1-v2.html`, knop naar de cartpagina) is klaar als voorstel, maar K1 draagt eerst T21. C3-P (0 orders op 305) is te klein voor een test: vaste wissel na akkoord, voor/na meten.

---

## 6. Kalender

| Wanneer | Actie | Wie |
|---|---|---|
| 29 okt | Floris: akkoord T21 (HI10 in K1, wijkt af van DECISIONS 8 okt), T02 op 100% code tijdens de sale, regel "gifts end when the fall sale ends" na 31 okt | Floris |
| 29 tot 31 okt | Claude bouwt `k1-hi10.html`, `k4-installments.html`, `c5-installments.html` (vaste header en footer, QA groen), als Draft-templates | Claude |
| 30 okt | Start T14 (C1-onderwerp) en T22 (C2 op 48 uur) | Floris in UI |
| 1 nov | T02-splits `119850619`, `119850638`, `119850645` op 100% code. Start T21, T23, T24 (T24 alleen als T22 niet start) | Floris in UI, Claude controleert via API |
| elke ochtend | Dagbewaking: afmelding per mail met 7-dagengemiddelde in plaats van 24 uur (minder vals alarm), bounce C1 | Claude |
| 20 nov tot 6 dec | Bevriezing: niets nieuws, lopende tests door, BFCM-dagen apart rapporteren | |
| 7 dec | Rapport alle tests (vóór, sale, na). T02 hervatten 50/50. T22 beslissen, daarna T26. T24 starten als die nog niet liep | Claude, Floris |
| januari | T21, T23 en T24 beslissen; T18 na T21 | |

## 7. Open punten voor Floris

1. Mag T21 (HI10 al in K1) als test, tegen het besluit van 8 okt in?
2. T02 in checkout en cart op 100% code van 1 nov tot 6 dec?
3. Blijft "Your 4 gifts end when the fall sale ends" na 31 okt waar, nu de gifts in november doorlopen? Zo niet, dan moet die regel in C1, C2 en de cartmails vóór 1 nov aangepast worden (raakt T14 niet: het onderwerp blijft gelijk).
4. Mag de termijnmail (T23, T24) een bedrag per maand noemen, of alleen "Shop Pay Installments and Affirm are at checkout" zoals in C1?
5. C1 bouncegolf 12 tot 21 okt: weet iemand wat er toen in de checkout gebeurde (bots, test-checkouts, een app)? Sinds 22 okt is het weg.
