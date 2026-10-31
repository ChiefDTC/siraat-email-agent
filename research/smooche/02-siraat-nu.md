# Smooche-vergelijking · 02 · Wat Siraat nu doet na een inschrijving (31 okt 2026)

Vraag Floris: "we hebben geen mail direct na de inschrijving". Dit document controleert dat met data.

Alleen gelezen. Klaviyo (account TdtTzz, revision 2025-10-15): `GET /api/forms`, `GET /api/metrics`, flowdefinitie `T4a5Mk`, templates van W1 (Sq2bvX, XMAs8s), W2 (VjPTKM), W3 (VCjUYQ), events van Subscribed to Email Marketing `UqVdQX` (28 tot 30 okt: 2.814 events; cohort 9 tot 23 okt: 11.353 events), Received Email `YkRM4Q`, Bounced Email `XDdu6P`, Placed Order `RSNxYV` (1 tot 31 okt: 6.821 orders), `POST /api/flow-values-reports` (1 tot 31 okt) en `POST /api/metric-aggregates`. Niets gewijzigd in Klaviyo of Shopify, niets verstuurd. Rekenwerk in de scratchpad (`golive/smoo/`); hier alleen aggregaten, geen e-mailadressen.

---

## 0. Kort antwoord

**De bewering klopt niet.** Wie zich inschrijft via de pop-up krijgt W1 gemiddeld **6,5 minuten** later (mediaan; p90 9,9 minuten; maximaal 16 minuten). W1 maakt het meeste geld van de hele welcome-flow ($2,83 per ontvanger, 80% van de omzet van de nieuwe arm).

Wat wél klopt: **60% van de kopers uit de pop-up koopt binnen 10 minuten na de inschrijving**, ongeveer 80% van hen nog vóór W1 binnen is, en vrijwel allemaal zonder code. W1 is een ontworpen mail met 22 beelden en 22 links, geen korte brief. Het eerste persoonlijke woord van Benjamin komt pas de volgende ochtend (W2).

---

## 1. Inschrijfformulieren en aanbod

| Bron | Status | Inschrijvingen | Aanbod |
|---|---|---|---|
| Klaviyo-formulieren (35 stuks) | **alle 35 op draft** (laatste wijziging 14 mei 2026) | 0 (Viewed Form 3 en Form submitted 0 in oktober) | niet actief |
| **Alia-pop-up** ("Card Game") | live | 721, 752 en 997 per dag op 28, 29 en 30 okt (88% van alle inschrijvingen) | giveaway: een lot op "je order terugbetaald" ("Win your order for free"). Geen code bij de inschrijving |
| Shopify-checkout (opt-in) | live | ~110 per dag (12% sinds 20 okt; daarvoor 450 tot 780 per dag) | geen; inschrijving tijdens het afrekenen |
| Back in stock-wachtlijst (Klaviyo onsite) | live | ~3 per dag | geen |

- Alle bronnen schrijven in op dezelfde lijst **Uw8eZG (Email List)**, `double_opt_in: false`. Alia schrijft in via de API (`method API_V3_SUBSCRIBE`, `custom_method_detail "Alia sign-up"`).
- **Alia Reward Claimed (TBeZmH)**: laatste event 12 sep 2026 (rad met SIRAAT5, SIRAAT10, SIRAAT15). Sindsdien 0, ook in oktober. Het kortingsrad is dus vervangen door de Card Game-giveaway.
- **De korting komt alleen per mail.** De pop-up geeft geen code (PLAYBOOK: "opt-in geeft een lot ... geen kortingscode"). Bevestigd door de orders: van 243 orders binnen 10 minuten na een Alia-inschrijving (cohort 9 tot 23 okt) hadden er **240 geen kortingscode**, 1 HI10.
- **Levering van HI10:** in W1 via een link met de code al toegepast: `https://siraatskitchen.com/discount/HI10?redirect=/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern...` (7 van de 22 links in W1). Daarnaast staat de code als tekst in de balk bovenaan ("YOUR WELCOME 10% · CODE HI10").

---

## 2. Welcome-flow T4a5Mk: hoe hij nu staat

**Trigger:** toegevoegd aan lijst Uw8eZG. **Flowfilter:** e-mail bevat geen `test@` EN **nooit eerder in deze flow** (alltime; wie zich opnieuw inschrijft, krijgt de welcome niet nog eens). Smart sending staat **uit** op elke mail. Klaviyo kent voor e-mailflows geen quiet hours; de enige "stille uren" zijn de vaste verzendtijden van W2 tot W5.

| Stap | Actie | Instelling | Wat dat betekent |
|---|---|---|---|
| Split T01 | 119850648 | random sample **100% nieuw pad** | oude arm krijgt niemand meer |
| Wacht | 119850649 | **5 minuten**, geen "tot"-tijd | ook 's nachts |
| Exit | 119850651 | Placed Order > 0 sinds flowstart: stop | kopers binnen 5 min krijgen niets |
| Split al klant | 119850653 | Placed Order > 0 alltime | ja: W0 (eind), nee: W1 |
| **W1** (A/B Q1) | 119850659 | A "No PFAS. Here's the paper. And 10%." / B "Your 10% works on top of the sale" (sinds 28 okt 23:13 UTC), 50/50, handmatige winnaar | ~5 min na inschrijving |
| Wacht | 119850661 | 1 dag, tot 10:00 (tijdzone profiel) | volgende kalenderdag 10:00: 10 tot 34 uur na inschrijving |
| W2 | 119850663 | "The pan nobody else was making", van "Benjamin at Siraat's Kitchen" | dag 1, 10:00 |
| Wacht | 119850665 | 2 dagen, tot 09:00 | |
| W3 | 119850667 | "Has your cookware been tested?" | dag 3, 09:00 |
| Wacht + split land | 119850669, 119850671 | 3 dagen, tot 09:00; land = US | |
| W4-US / W4-INT | 119850673 / 119850674 | "Who are you cooking for?" | dag 6, 09:00 |
| Wacht | 119850676 / 119850677 | 4 dagen, tot 09:00 | |
| W5-US / W5-INT | 119850679 / 119850680 | "Tammy is on her fourth pan" | dag 10, 09:00 |

**Filters op elke mail van het nieuwe pad (W0 tot W5):** Placed Order = 0 sinds flowstart, en **geen mail uit checkout (QUBUQV) of cart (TZG9Mx) in de laatste dag**. Dan wordt de mail overgeslagen, niet beëindigd.

### Gemeten vertraging inschrijving tot W1

Steekproef: 160 willekeurige inschrijvingen van 28 okt 00:00 tot 30 okt 12:00 UTC (minstens 26 uur om W1 te krijgen). Per profiel de eerste Received Email uit T4a5Mk na de inschrijving.

| | Minuten na inschrijving |
|---|---|
| Ingesteld | 5 |
| p10 | 5,8 |
| **Mediaan** | **6,5** |
| **p90** | **9,9** |
| Maximum | 16,4 |

n = 135 (134 keer W1, 1 keer W0). Geen enkele W1 kwam later dan 17 minuten; er is geen nachtelijke vertraging. De eerste mail die iemand na de inschrijving krijgt, is in 133 van de 160 gevallen W1/W0. In 18 gevallen is dat "Your E-Guide Is Ready" (flow YyaMjx, 3 min na een order): dat zijn de kopers.

### Wie krijgt geen W1 (25 van 160, 16%)

| Reden | Aantal | Toelichting |
|---|---|---|
| Kocht binnen 5 minuten (exit-split) | 19 | 12 via de Shopify-checkout (inschrijving tijdens het afrekenen), 7 via Alia |
| W1 verstuurd maar **hard bounce** | 4 | Alia; W1 heeft daardoor 2,4% bounce, W2 1,0% (giveaway trekt nep-adressen) |
| Al eerder in de welcome (opnieuw ingeschreven) | 1 | flowfilter "nooit eerder in deze flow" |
| Onverklaard | 1 | geen Received, geen Bounce; consent SUBSCRIBED; alleen een Skipped Send van een campagne |
| Al klant | 0 | (1 klant kreeg W0) |
| Niet ingeschreven / geen consent | 0 | alle inschrijvingen zijn `SUBSCRIBED`, single opt-in |

Alleen Alia (141 in de steekproef): **W1 afgeleverd bij 128 (91%)**, verstuurd bij 132 (94%).

---

## 3. Prestaties per mail, oktober (1 tot 31 okt, flow-values-report)

Toeschrijving Klaviyo-standaard (Placed Order). De flow bestaat sinds 8 okt; de oude arm loopt sinds 19 okt leeg.

| Mail | Bericht | Ontvangers | Open | Klik | Orders | Omzet | Per ontv. | Afmelding | Bounce |
|---|---|---|---|---|---|---|---|---|---|
| **W1** | RN7Yy6 | 11.913 | 45,1% | **3,79%** | **116** | **$32.946** | **$2,83** | 1,90% | 2,42% |
| W0 (al klant) | VZYNbF | 101 | 69,3% | 7,92% | 2 | $1.177 | $11,65 | 0,99% | 0% |
| W2 | RHuJcG | 8.247 | 41,1% | 1,89% | 17 | $4.492 | $0,55 | 1,67% | 0,99% |
| W3 | SSTz6y | 7.216 | 38,0% | 1,09% | 11 | $1.839 | $0,26 | 1,27% | 0,98% |
| W4-US | XDaaZn | 3.024 | 36,6% | 0,63% | 3 | $979 | $0,33 | 0,57% | 0,89% |
| W4-INT | TrhmmM | 2.650 | 36,9% | 1,26% | 0 | $0 | $0,00 | 0,80% | 0,94% |
| W5-US | Wp85L8 | 1.778 | 35,9% | 0,74% | 0 | $0 | $0,00 | 0,96% | 0,68% |
| W5-INT | TXF9D2 | 1.794 | 34,6% | 0,62% | 0 | $0 | $0,00 | 0,73% | 0,56% |
| **Nieuwe arm** | | **36.723** | | | **149** | **$41.433** | **$1,13** | 1,41% | |
| Oude arm (Old 1 tot 8) | | 15.235 | | | 47 | $15.710 | $1,03 | 2,02% | |
| Old · Welcome 1 | WCZQNi | 3.265 | 47,5% | 2,66% | 31 | $10.794 | $3,41 | 4,27% | 3,09% |

- **W1 maakt het geld:** 80% van de omzet van de nieuwe arm, 77% van alle welcome-omzet als je de oude W1 meetelt. Na W2 valt het weg; W4-INT en W5 leverden in oktober samen 0 orders op 8.200 mails.
- **Q1 (onderwerp W1), eerste 2,5 dag** (28 okt 23:13 tot 31 okt 14:00 UTC): B 1.124 ontvangers, 9 orders, $2.041; A 1.101 ontvangers, 8 orders, $2.461. Te vroeg; geen conclusie.

### Wanneer kopen nieuwe inschrijvers?

Cohort: Alia-inschrijvingen 19 okt 12:00 tot 23 okt (pop-up op vol volume), n = 2.759, eerste order binnen 7 dagen (alle orders, niet alleen toegeschreven).

| Eerste order na inschrijving | Kopers | % van inschrijvers | % van kopers | Omzet (7 d) |
|---|---|---|---|---|
| **binnen 10 minuten** | 169 | 6,13% | **60%** | $37.133 |
| 10 min tot 1 uur | 53 | 1,92% | 19% | $15.005 |
| 1 tot 24 uur | 32 | 1,16% | 11% | $6.911 |
| 1 tot 3 dagen | 15 | 0,54% | 5% | $3.007 |
| 3 tot 7 dagen | 13 | 0,47% | 5% | $3.691 |
| **Totaal 7 dagen** | **282** | **10,2%** | 100% | $65.747 |

- **90% van de kopers koopt binnen 24 uur, 79% binnen het eerste uur.** Wat na dag 1 komt (W2 tot W5), raakt 10% van de kopers.
- De kopers binnen 10 minuten kopen in een mediaan van ~4 minuten na de inschrijving, dus meestal vóór W1 (6,5 min; ongeveer 80% van deze orders valt vóór de 6,5 minuten). Ze gebruiken geen code: ze zaten al in de winkel en de pop-up gaf hun niets om te gebruiken.
- HI10 in het eerste uur tot dag 1: van de 132 orders van 10 minuten tot 24 uur na een Alia-inschrijving (cohort 9 tot 23 okt) hadden er 25 HI10 en 100 geen code.
- Shopify-checkout-inschrijvers (ter vergelijking): 87% van hun kopers koopt binnen 10 minuten, want ze schrijven zich in tijdens het afrekenen.

---

## 4. Hoe de welcome-mails er nu uitzien

| Mail | Vorm | Afzender | Aanbod | Primaire link | Korting automatisch? |
|---|---|---|---|---|---|
| W1 (A en B zelfde template) | **ontworpen**: vaste header met logo, navigatie (Cookware, Sets, About), codebalk, hero, vergelijkingstabel "Your future pan vs a PFAS pan", 22 beelden, 22 links, 43 KB | Siraat's Kitchen | 10% met HI10 "on top of the sale" + gifts; Card Game-bevestiging ("Your Card Game entry is in, with a chance to get your order refunded") staat onder de knop | knop "Claim my 10% + gifts" naar **één productpagina** (Original Siraat titanium pan) | **ja**, via `/discount/HI10?redirect=...` (7 links); nav-links zonder code |
| W2 | brief van Benjamin ("It's Benjamin. I wanted to write to you myself."), maar mét header, logo en navigatie; 8 beelden, 17 links | Benjamin at Siraat's Kitchen | 10% in de P.S. | P.S.-link naar dezelfde productpagina | ja (2 links) |
| W3 | ontworpen ("Don't take our word for it", zes bewijzen), 17 beelden, 22 links | Siraat's Kitchen | 10% + gifts | zelfde productpagina | ja (5 links) |

Geen enkele welcome-mail heeft een deadline. HI10 vervalt niet (PLAYBOOK: "geen nep-urgentie, HI10 heeft geen deadline").

---

## 5. Verschil met een Smooche-opzet

Smooche-opzet = (a) direct een platte brief van de oprichter, (b) met het aanbod al toegepast, (c) één knop naar een collectie, (d) vervolgmails met korte tussenpozen en (e) een echte deadline.

| Onderdeel | Smooche | Siraat nu | Gat |
|---|---|---|---|
| Moment eerste mail | direct | 6,5 min mediaan (instelling 5 min + verwerking) | klein. Maar 60% van de kopers koopt binnen 10 min, een deel vóór W1. Een vertraging van 0 tot 1 min haalt een deel daarvan in |
| Vorm eerste mail | platte brief van de oprichter | ontworpen verkoopmail, 22 beelden, 22 links; de brief van Benjamin komt pas als W2 (dag 1, 10:00) | **groot** |
| Aanbod al toegepast | ja | ja: HI10 via `/discount/HI10?redirect=` | geen |
| Aanbod zichtbaar in de pop-up | aanbod meteen | pop-up belooft alleen de giveaway, geen code. 240 van 243 snelle kopers kopen zonder code | middel: de 10% bereikt de snelle kopers niet |
| Eén knop | één CTA | 1 primaire knop (3 keer), plus navigatie, testlinks, socials: 22 links | middel |
| Doel van de knop | collectie | één productpagina (de Original pan) | middel: sets en andere maten zijn een klik extra |
| Vervolg met korte tussenpozen | uren tot 1 dag | W2 de volgende ochtend 10:00 (10 tot 34 uur), daarna dag 3, 6 en 10 | **groot**: niets tussen minuut 6 en de volgende ochtend, terwijl 30% van de kopers in uur 0 tot 24 koopt |
| Deadline | ja, echte deadline | geen; HI10 vervalt nooit | **groot** (vraagt een besluit: een echte deadline kan alleen met een unieke code of een vervaldatum, zie T09) |
| Giveaway-bevestiging | n.v.t. | één zin onder de knop in W1 | klein; mogelijk deels de reden van 1,9% afmelding en 2,4% bounce op W1 |

**Conclusie.** Er is wél een mail direct na de inschrijving, en het is de beste mail van de flow. Het gat zit niet in het moment maar in (1) de vorm van die eerste mail (ontworpen catalogusmail in plaats van een korte brief met één knop), (2) het ontbreken van een tweede contact binnen de eerste uren, (3) het ontbreken van een deadline, en (4) een pop-up die geen aanbod meegeeft, waardoor de 60% snelle kopers de 10% nooit ziet.

Open punten om te bevestigen:
- Of Alia na het invullen nog een eigen scherm of code toont. Dat is vanuit Klaviyo niet te zien; de orders wijzen op nee.
- De terugval in Shopify-checkout-inschrijvingen van ~600 per dag (9 tot 19 okt) naar ~110 per dag (sinds 20 okt). Niet onderzocht; mogelijk een wijziging in de checkout-opt-in.
