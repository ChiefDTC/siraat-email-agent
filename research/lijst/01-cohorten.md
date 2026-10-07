# 01 · Cohorten per inschrijfbron en maand

Datum: 7 oktober 2026. Alleen gelezen uit Klaviyo (Events API GET, revision 2025-10-15, plus metric aggregates via MCP). Profiel-ID's zijn alleen gehasht in een tijdelijke scratchpad verwerkt; in de repo staan uitsluitend aggregaten. Volledige tabel: `cohorten.csv` (36 kolommen, per bron en maand, plus Alia-varianten).

## Kern in vijf punten

1. **De pop-up verkoopt, de mail daarna nauwelijks.** Van alle aanmelders koopt 21 procent binnen 24 uur (Alia 11 procent). Van wie dan nog niet kocht, koopt maar 2,8 procent in dag 1 tot 30 en 4,2 procent in dag 1 tot 90 (alle kanalen samen). Daar moet e-mail het verschil maken, en daar ligt het laag.
2. **Alia-aanmelders zijn sinds mei het grootste en zwakste cohort.** Conversie in 30 dagen 13 tot 15 procent (tegenover 17 tot 19 procent voor de Klaviyo sale-pop-ups in januari tot april), omzet per abonnee in 90 dagen $32 tot $34 (tegenover $37 tot $41), en 55 tot 60 procent van hen is na 45 dagen nog nooit betrokken maar wel mailbaar.
3. **Eén op zes aanmelders schrijft zich binnen 30 dagen uit** (16,3 procent), één op vier binnen 90 dagen (25,3 procent). 7 van elke 1.000 aanmelders klagen binnen 30 dagen over spam, en dat zijn alleen de providers die klachten terugmelden. In het septembercohort ligt de uitschrijving (18,6 procent) voor het eerst boven de klikratio (17,6 procent).
4. **De giveaway is nog te jong om te beoordelen, maar de eerste week is zwakker.** Card Game (sinds september): 9,5 procent koopt in 7 dagen, 11,8 procent schrijft zich uit, 4,9 spamklachten per 1.000. Dat is de laagste conversie en de hoogste uitschrijving en klacht van alle Alia-varianten. Ook binnen september zelf (tegenover Smart Offers: 10,9 procent conversie, 11,0 procent uitschrijving, 4,2 per 1.000) scoort hij slechter. Het 30-dagenbeeld komt rond 7 november.
5. **Wie in week 1 klikt, is 2,3 keer zo waardevol, maar de niet-klikkers maken de massa.** Slechts 8,5 procent van de niet-kopers klikt in de eerste 7 dagen; zij kopen daarna in 5,7 procent van de gevallen (dag 7 tot 90), de rest in 2,5 procent. Omdat de niet-klikkers 91,5 procent zijn, leveren zij nog steeds ongeveer 80 procent van de latere orders. Conclusie voor het voorstel: niet-klikkers niet afsnijden in week 1, wel minder vaak mailen, en pas na 45 tot 60 dagen zonder enig signaal laten gaan.

## Methode

| Onderdeel | Keuze |
|---|---|
| Cohort | Eerste "Subscribed to List"-event (`SCvkku`) voor Email List `Uw8eZG` per profiel, 1 januari tot en met 6 oktober 2026: 205.485 profielen. Maand in US/Eastern. |
| Bron | Profieleigenschap `$source` op 7 oktober. Groepen: **Alia sign-up** (95.636), **Klaviyo-formulier (sale-pop-up)** (63.333: New Year Sale, Pan Pop Up, Valentines, St Patricks, Easter, Mother's Day, Women's Day, Ramadan; alleen januari tot april actief), **Shopify (-50)** (46.128), overig (388). |
| Alia-variant | Eigenschappen `alia_campaign` en `alia_popup_name`. Alia overschrijft die bij elke nieuwe interactie, dus een variant is alleen toegekend in de maanden dat hij live was (anders "overig of niet toe te wijzen"). |
| Conversie | Placed Order (`RSNxYV`, alle kanalen, niet alleen e-mailgeattribueerd) van hetzelfde profiel vanaf 2 uur vóór aanmelding tot 30 of 90 dagen erna. Alleen cohorten waarvan het venster volledig verstreken is (90 dagen: januari tot juni volledig, juli deels). Cijfers onder 300 complete profielen zijn weggelaten. |
| Omzet per abonnee | Som orderwaarde (USD) in het venster gedeeld door alle aanmelders in het complete deel van het cohort. |
| Klikratio | Aandeel aanmelders met minstens één menselijke klik (`W247h8`, Bot Click niet waar) in het venster. Opens tellen niet (Apple Mail Privacy). |
| Uitschrijving, spam | Aandeel aanmelders met een Unsubscribed from Email Marketing-event (`YcWddQ`) respectievelijk Marked Email as Spam (`VQMAAk`) in het venster. Spam per 1.000 aanmelders. |
| Nooit betrokken, nog mailbaar | Cohortleden van minstens 45 dagen oud zonder klik en zonder order sinds aanmelding, die zich niet uitschreven en niet klaagden. |

**Kanttekeningen.** (1) Shopify (-50) is geen zuivere checkout-opt-in: januari tot april koopt 73 tot 83 procent binnen 24 uur, vanaf mei nog maar 32 tot 52 procent. Vermoedelijk komen er vanaf mei ook Shop- of accountaanmeldingen binnen met dezelfde code. (2) Order binnen 24 uur komt vaak uit dezelfde sessie als de pop-up; dat is geen e-mailprestatie. (3) Spamklachten zijn onderteld: Gmail en Apple melden ze niet terug (zie 02-deliverability). (4) Augustus en september bevatten de jubileumsale, Labor Day en Warehouse Clearance; mei Memorial Day.

## 1. Alle bronnen samen

| Maand | Abonnees | Koopt binnen 24 u | Conv. 30 d | Conv. dag 1 tot 30 (zonder aankoop 24 u) | Omzet/abonnee 30 d | Klik 30 d | Uitschrijf 30 d | Spam 30 d per 1.000 | Conv. 90 d | Omzet/abonnee 90 d | Nooit betrokken, nog mailbaar (45 d+) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01 | 28.427 | 24,2% | 26,40% | 2,89% | $52,16 | 18,1% | 19,2% | 8,83 | 27,67% | $56,59 | 38,4% |
| 2026-02 | 17.830 | 27,3% | 29,59% | 3,20% | $57,18 | 17,4% | 16,3% | 6,45 | 30,73% | $61,72 | 38,4% |
| 2026-03 | 18.987 | 26,7% | 29,27% | 3,51% | $61,45 | 17,4% | 16,0% | 5,95 | 30,28% | $65,48 | 38,0% |
| 2026-04 | 20.216 | 25,0% | 27,17% | 2,95% | $60,09 | 19,3% | 16,4% | 6,28 | 27,90% | $63,19 | 41,8% |
| 2026-05 | 31.512 | 16,3% | 18,55% | 2,63% | $43,41 | 18,4% | 16,2% | 7,27 | 19,37% | $46,37 | 50,9% |
| 2026-06 | 24.975 | 15,9% | 18,13% | 2,67% | $39,68 | 16,2% | 14,4% | 6,65 | 19,18% | $43,29 | 53,3% |
| 2026-07 | 18.217 | 20,7% | 22,98% | 2,94% | $51,88 | 18,2% | 14,5% | 5,98 | 21,53% (deels) | $46,35 (deels) | 50,9% |
| 2026-08 | 22.414 | 21,6% | 23,43% | 2,32% | $51,48 | 18,0% | 16,1% | 6,42 | n.v.t. | n.v.t. | 53,1% |
| 2026-09 | 18.435 | 17,4% | 18,87% (1 tot 6 sep) | 2,03% | $40,00 | 17,6% | 18,6% | 7,35 | n.v.t. | n.v.t. | n.v.t. |
| 2026-10 (t/m 6 okt) | 4.308 | 18,9% | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. |
| **Totaal** | **205.485** | **21,2%** | **23,78%** | **2,82%** | **$50,87** | **17,9%** | **16,3%** | **6,88** | **24,94%** | **$54,36** | **45,6%** |

De knik in mei valt samen met de overstap van Klaviyo sale-pop-ups naar Alia (Mystery Discount, Scratch Off). Het aandeel nooit-betrokken stijgt sindsdien van 38 tot 42 procent naar 51 tot 53 procent.

## 2. Alia sign-up

| Maand | Abonnees | Koopt binnen 24 u | Conv. 30 d | Conv. dag 1 tot 30 (zonder aankoop 24 u) | Omzet/abonnee 30 d | Klik 30 d | Uitschrijf 30 d | Spam 30 d per 1.000 | Conv. 90 d | Omzet/abonnee 90 d | Nooit betrokken, nog mailbaar (45 d+) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01 | 804 | 13,2% | 17,04% | 4,44% | $32,18 | 21,3% | 10,3% | 6,22 | 19,53% | $42,09 | 36,6% |
| 2026-02 | 590 | 13,9% | 15,76% | 2,17% | $29,43 | 15,9% | 7,3% | 0,00 | 22,03% | $52,88 | 38,1% |
| 2026-03 | 1.571 | 11,8% | 14,51% | 3,10% | $31,02 | 17,3% | 11,9% | 4,46 | 19,41% | $50,63 | 45,3% |
| 2026-04 | 5.120 | 14,2% | 17,52% | 3,87% | $40,13 | 18,5% | 14,8% | 7,03 | 19,43% | $46,65 | 49,0% |
| 2026-05 | 24.849 | 10,7% | 13,04% | 2,62% | $31,47 | 16,6% | 16,1% | 7,81 | 13,96% | $34,33 | 54,7% |
| 2026-06 | 20.425 | 10,5% | 12,96% | 2,75% | $28,65 | 14,9% | 14,4% | 6,61 | 14,05% | $31,90 | 56,8% |
| 2026-07 | 14.001 | 11,1% | 13,78% | 2,99% | $31,40 | 15,8% | 14,9% | 7,00 | 15,34% (deels) | $33,33 (deels) | 57,4% |
| 2026-08 | 11.829 | 12,4% | 14,60% | 2,50% | $31,95 | 15,3% | 16,1% | 6,68 | n.v.t. | n.v.t. | 60,1% |
| 2026-09 | 12.670 | 9,0% | 12,10% (1 tot 6 sep) | 2,37% | $25,35 | 16,7% | 18,1% | 6,43 | n.v.t. | n.v.t. | n.v.t. |
| 2026-10 | 3.773 | 9,2% | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. |
| **Totaal** | **95.636** | **10,9%** | **13,72%** | **2,79%** | **$31,16** | **16,0%** | **15,2%** | **6,98** | **14,90%** | **$35,20** | **55,4%** |

Alia-instroom: 12 tot 25 duizend per maand sinds mei, circa 2.900 per week in september.

## 3. Klaviyo sale-pop-ups (januari tot april) en Shopify (-50)

| Bron | Abonnees | Koopt binnen 24 u | Conv. 30 d | Conv. dag 1 tot 30 | Omzet/abonnee 30 d | Klik 30 d | Uitschrijf 30 d | Spam 30 d per 1.000 | Conv. 90 d | Omzet/abonnee 90 d | Nooit betrokken (45 d+) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Klaviyo-formulier, januari | 23.504 | 14,5% | 16,82% | 2,71% | $32,37 | 17,5% | 19,8% | 9,10 | 18,18% | $36,55 | 43,5% |
| Klaviyo-formulier, februari | 14.118 | 15,6% | 18,18% | 3,10% | $34,19 | 16,7% | 17,4% | 7,37 | 19,27% | $37,97 | 44,7% |
| Klaviyo-formulier, maart | 14.081 | 16,0% | 18,96% | 3,51% | $39,06 | 16,8% | 17,5% | 6,68 | 19,68% | $41,43 | 43,5% |
| Klaviyo-formulier, april | 11.480 | 14,8% | 16,87% | 2,38% | $37,18 | 16,4% | 18,5% | 6,62 | 17,22% | $38,58 | 46,8% |
| **Klaviyo-formulier, totaal** | **63.333** | **15,1%** | **17,61%** | **2,91%** | **$35,12** | **16,9%** | **18,5%** | **7,72** | **18,58%** | **$38,30** | **44,4%** |
| **Shopify (-50), totaal** | **46.128** | **51,1%** | **52,54%** | **2,57%** | **$112,59** | **22,8%** | **15,1%** | **5,36** | **62,23%** | **$134,63** | **27,7%** |

Per maand voor Shopify (-50) staat in `cohorten.csv`. Opvallend: ook kopers schrijven zich in 30 dagen voor 15 procent uit. Na een aankoop krijgen ze dezelfde campagnestroom als leads.

## 4. Alia-varianten: eerste 7 dagen (enige eerlijke vergelijking met de giveaway)

| Variant | Live | Abonnees (7 d compleet) | Conv. 7 d | Klik 7 d | Uitschrijf 7 d | Spam 7 d per 1.000 | Conv. 30 d | Uitschrijf 30 d |
|---|---|---|---|---|---|---|---|---|
| 10% welkomstkorting (BAU) | apr tot mei | 4.584 | 15,4% | 12,8% | 9,3% | 3,71 | 16,56% | 16,2% |
| Mystery Discount / Scratch Off | mei tot jul | 54.201 | 11,8% | 11,2% | 9,8% | 4,39 | 12,85% | 15,4% |
| Evergreen Control | jul tot aug | 9.592 | 14,3% | 10,7% | 9,3% | 3,34 | 15,35% | 15,8% |
| Smart Offers | aug tot sep | 6.217 | 12,4% | 10,9% | 10,2% | 3,22 | 13,56% | 17,4% |
| Smart Offers, alleen september | sep | 1.930 | 10,9% | 11,7% | 11,0% | 4,15 | n.v.t. | n.v.t. |
| Order Refund (giveaway) | sep | 3.210 | 10,4% | 10,3% | 10,5% | 3,12 | 11,77% (vroeg sep) | 18,7% |
| US Evergreen Card Game (giveaway, incl. timingvarianten 0 s, 8 s, Scratch Off) | sep tot okt | 6.935 | **9,5%** | 11,3% | **11,8%** | **4,90** | n.v.t. | n.v.t. |

Lezing: de giveaway trekt aanmelders die minder snel kopen en sneller afhaken in week 1. Dat past bij het mechanisme ("kans op terugbetaling" trekt winnaars, geen kopers). De verschillen zijn klein genoeg om deels seizoen te kunnen zijn; herhalen op 30 dagen begin november. Besluit van Floris (pop-up blijft de giveaway) staat; dit pleit voor betere selectie en behandeling ná de pop-up, niet voor het schrappen ervan.

## 5. Intentie en sunset: wat zeggen de eerste weken over later?

Cohorten januari tot en met juli met een volledig 90-dagenvenster, alleen profielen die in de eerste 7 dagen niet kochten.

| Bron | Aandeel dat in dag 0 tot 7 klikt | Conv. dag 7 tot 90: wel klik in week 1 | Conv. dag 7 tot 90: geen klik in week 1 | Geen klik en geen order in 45 d: conv. dag 45 tot 90 | Omzet dag 45 tot 90 per zo'n profiel | Geen klik en geen order in 60 d: conv. dag 60 tot 90 | Omzet dag 60 tot 90 per zo'n profiel |
|---|---|---|---|---|---|---|---|
| Alle bronnen | 8,5% | 5,71% | 2,48% | 0,64% | $1,47 | 0,36% | $0,85 |
| Alia sign-up | 7,5% | 6,13% | 2,57% | 0,76% | $1,65 | 0,45% | $1,01 |
| Klaviyo-formulier | 9,2% | 5,07% | 2,40% | 0,54% | $1,34 | 0,29% | $0,76 |
| Shopify (-50) | 9,0% | 7,02% | 2,32% | 0,54% | $1,15 | 0,29% | $0,52 |

- 75 procent van de Alia-aanmelders (44.289 van 58.766 in januari tot juli) klikt in 45 dagen niet en koopt niet.
- Van die groep koopt 0,76 procent alsnog in dag 45 tot 90, voor $1,65 per profiel, via alle kanalen. Het deel daarvan dat aan e-mail te danken is, is onbekend; het is in elk geval veel kleiner (geen klik betekent geen klik-attributie).
- Na 60 dagen zonder signaal halveert dat nog eens: 0,36 procent en $0,85 per profiel in de 30 dagen daarna.

## 6. Welke vragen dit openlaat

- Is "kans op order refund" (Card Game) de oorzaak van de zwakkere eerste week, of het seizoen? Herhaal de 7- en 30-dagenvergelijking op 7 november, en vraag Alia om de conversie per variant inclusief niet-aanmelders (wie de pop-up sluit en toch koopt).
- Wat is Shopify (-50) precies sinds mei? Uitzoeken in Shopify of Klaviyo-integratie-instellingen.
- Wat Alia doet met dubbele aanmeldingen, wegwerpadressen en bots: geen Alia-toegang in deze sessie.
