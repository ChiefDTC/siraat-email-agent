# Urgentie-sprint · verzendkalender 8 tot 30 november 2026 (rol: scheduler)

Alleen gelezen. Niets in Klaviyo of Shopify gewijzigd, niets ingepland, geen testmails. Bronnen: Klaviyo `GET /api/campaigns` (alle e-mailcampagnes sinds 20 sep, status en verzendinstellingen), `POST /api/campaign-values-reports` (laatste 30 dagen, conversie RSNxYV), `POST /api/metric-aggregates` (RSNxYV, toeschrijving per campagne per uur) en `GET /api/events` op Placed Order (8.731 orders, 9 okt tot 8 nov; alleen tijdstip, land en provincie gebruikt, niets opgeslagen in de repo). Daarnaast `research/homestead/kalender-november-2026.md`, `research/smooche/06-volume-plan-smooche.md` sectie 5, `research/plannen/2026-11-urgentie.md`, `2026-11-ftl-bf.md`, `2026-11-welcome-audit.md`, `2026-11-punten-store-credit.md` en `copy/copy.md` van deze sprint. Machineleesbare versie: `kalender.csv` (zelfde map).

Lokale tijd = tijd van de ontvanger (Klaviyo "Send in recipient's local time", zoals Homestead nu doet). US = lijst VMjhb2, INT = lijst XrFa5r. APAC = AU, NZ, SG, HK (de helft van de INT-orders).

---

## 0. Kort

- **Kopers kopen 's ochtends.** US: 35% van de orders tussen 06:00 en 12:00 lokaal, piek 09:00 tot 12:00 (7,4 tot 7,7% per uur). INT: piek 08:00 tot 11:00 (8,4 tot 8,5% per uur). De avond (18:00 tot 24:00) is nog 23 à 24%, met een klein bultje rond 20:00 tot 21:00 bij INT; na 22:00 zakt het hard (US 4,9% in de laatste twee uur).
- **Weekend is het sterkst.** US: zaterdag 123 (index, gemiddelde dag = 100), zondag 101, maandag 84. INT: zaterdag 143, zondag 129, woensdag 75.
- **Een deadline trekt de koop naar dezelfde dag.** 31 okt (ENDS TONIGHT): 74% van de toegeschreven orders binnen 24 uur na verzending; 4 nov US (today only): 62%. Alle campagnes samen: 51%. Kleine aantallen (20 tot 60 toegeschreven orders per campagne), dus richting, geen wet.
- **Er staat bijna niets ingepland.** Enige campagne met status Scheduled/Sending: Resend 1 (E1) op zo 8 nov 10:00 lokaal. Alles daarna (Homestead E5 tot E20, resends 2 en 3) bestaat nog niet of als Draft. Botsingen zitten dus in plannen en drafts, niet in ingeplande verzendingen; ze zijn nu nog gratis op te lossen.
- **Voorstel:** 6 mails in 9 verzendmomenten, steeds op dagen zonder Homestead-campagne: FLASH do 12 en (optioneel) do 19, VIP-WEEKEND vr 13 en (optioneel) do 26, DRAW zo 22, CREDIT en GIFTS op ma 30, LAST-HOURS als avondbrief bij elke deadline. Hoofdmail 08:30 lokaal (zondag 09:00), resend niet-openers 13:00 of 14:00 dezelfde dag, LAST-HOURS 17:00 lokaal (op 30 nov 20:00).
- **Grootste regel voor Floris:** "tonight at 11:59 PM ontvangerstijd" bestaat in Shopify niet als één korting; een korting heeft één eindmoment. Daarom drie regio's met elk een eigen eindmoment en de tijdzone in de copy (sectie 3). Zonder die drie backend-deadlines per mechaniek gaat de mail niet live.

---

## 1. Wat de data zegt

### 1.1 Orders per uur van de dag (lokale tijd van de koper, 9 okt tot 8 nov)

Tijdzone per order uit het verzendadres (US per staat, CA en AU per provincie, overige landen hoofdtijdzone). 6.627 US-orders, 2.104 INT.

| Uur lokaal | US % | INT % | | Uur lokaal | US % | INT % |
|---|---|---|---|---|---|---|
| 00 | 1,4 | 1,7 | | 12 | 6,5 | 7,0 |
| 01 | 0,8 | 1,0 | | 13 | 6,6 | 6,3 |
| 02 | 0,5 | 0,7 | | 14 | 5,3 | 5,3 |
| 03 | 0,7 | 0,4 | | 15 | 5,9 | 5,2 |
| 04 | 1,0 | 0,5 | | 16 | 5,6 | 5,4 |
| 05 | 1,3 | 1,1 | | 17 | 5,9 | 5,2 |
| 06 | 2,3 | 2,0 | | 18 | 5,4 | 4,2 |
| 07 | 4,0 | 4,1 | | 19 | 4,7 | 4,2 |
| 08 | 6,1 | 7,2 | | 20 | 4,2 | **4,8** |
| 09 | **7,7** | **8,4** | | 21 | 4,2 | 4,5 |
| 10 | 7,4 | **8,5** | | 22 | 2,7 | 3,4 |
| 11 | 7,6 | 6,3 | | 23 | 2,2 | 2,8 |

Dagdelen: US 00 tot 06 6%, 06 tot 12 35%, 12 tot 18 36%, 18 tot 24 23%. INT 5 / 37 / 34 / 24%. Op de deadlinedagen schuift het niet naar de avond (31 okt US 24% na 18:00, 4 nov 22%): de deadline maakt de dag drukker, niet de laatste uren. Lezing: de hoofdmail moet 's ochtends binnen zijn; de avondmail is een vangnet voor wie al keek, geen hoofdmoment.

### 1.2 Orders per weekdag (lokaal)

| | ma | di | wo | do | vr | za | zo |
|---|---|---|---|---|---|---|---|
| US orders | 797 | 906 | 898 | 886 | 1.017 | **1.165** | 958 |
| US omzet ($k) | 184 | 183 | 191 | 228 | 261 | **315** | 246 |
| INT orders | 272 | 262 | 225 | 251 | 276 | **429** | 389 |

Een deadline die op zondag 23:59 eindigt, pakt de twee sterkste dagen (VIP-weekend, trekking). Maandag is de zwakste dag en is de dag na elke weekenddeadline.

### 1.3 Campagnes laatste 30 dagen (verzending, RPR, verdeling van toegeschreven orders)

Bijna alles gaat om 08:15 lokaal (Homestead), dus het effect van het uur is niet te meten; wel het effect van de deadline.

| Verzonden (lokaal) | Campagne | Ontv. | Open | Klik | RPR | Orders binnen 24 u |
|---|---|---|---|---|---|---|
| 27 okt 08:15 | Oct E11 "ends this week" | 83.306 | 41,4% | 0,69% | $0,155 | 40% |
| 31 okt 08:15 | Oct E12 "ENDS TONIGHT" | 84.564 | 40,9% | 0,80% | $0,165 | **74%** |
| 1 nov 08:15 | Nov E1 US | 74.434 | 35,9% | 0,58% | $0,102 | 29% |
| 1 nov 08:15 | Nov E1 INT | 75.034 | 38,1% | 0,88% | $0,097 | n.v.t. |
| 2 nov 09:00 | Roasting Pan INT | 73.390 | 38,6% | 0,78% | $0,088 | n.v.t. |
| 3 nov 08:15 | Nov E2 recept US / INT | 67.688 / 52.831 | 41,2 / 45,6% | 0,24 / 0,34% | $0,087 / $0,093 | 36% (US) |
| 4 nov 09:00 | Win your order back US "(today only)" | 74.697 | 42,5% | 0,78% | **$0,171** | **62%** |
| 4 nov 09:00 | idem INT | 52.047 | 49,4% | 1,13% | $0,077 | n.v.t. |
| 5 nov 08:15 | Nov E3 US / INT | 72.533 / 49.206 | 44,0 / 48,7% | 0,50 / 0,57% | $0,109 / $0,103 | 65% (US) |
| 6 nov 13:07 ET (niet lokaal) | Benjamin-brief 2 Pans + 2 Lids US | 76.794 | 44,1% | 0,56% | $0,126 | 85% (40% binnen 6 u) |
| 7 nov 08:15 | Nov E4 US / INT | 73.288 / 51.371 | 30,9 / 41,4% | 0,43 / 0,53% | $0,072 / $0,034 | 100% (US, 16 orders) |

"Orders binnen 24 u" = aandeel van de aan die campagne toegeschreven orders dat binnen 24 uur na het verzendmoment viel (uurdata `$attributed_message`). Voor INT niet berekend omdat lokale verzending in APAC vóór het UTC-verzendmoment valt. Alle campagnes samen: 51%.

Lezing: RPR $0,15 tot $0,17 alleen bij een echte einddatum; zonder deadline $0,03 tot $0,13. De middagbrief van Benjamin (13:07 ET, niet lokaal) verkocht snel: een tweede contact op een andere tijd dan 08:15 werkt.

---

## 2. Wat al staat of gepland is (stand 8 nov 2026)

### 2.1 In Klaviyo

| Status | Wanneer | Campagne | Smart sending |
|---|---|---|---|
| Sending/Scheduled | zo 8 nov 10:00 lokaal | HS Resend 1 (E1) US en INT, "Still cooking on coated pans?" | aan |
| Draft | di 10 nov 09:00 lokaal | E5 Thanksgiving prep plan US en INT | uit |
| Draft | wo 11 nov 09:00 lokaal | E6 Founder letter US en INT | uit |
| Draft | vr 13 nov 15:00 UTC | CONCEPT BFCM kopers 1 "The lid your pan is missing" (segment SpBxrC, kopers) | aan |
| Draft | vr 27 nov 15:00 UTC | CONCEPT BFCM kopers 2 | aan |
| Draft | ma 30 nov 15:00 UTC | CONCEPT BFCM kopers 3 | aan |
| Draft | (8 nov 09:00) | AFF inhaal "Your order can pay for itself" | uit |

Geen andere campagne met status Scheduled tot en met 30 nov.

### 2.2 Homestead-kalender (nog niet ingepland), plus weekend

di 10 E5 · wo 11 E6 · **za 14 E7 08:15 (all buyers + E90)** · **zo 15 Resend 2 10:00** · di 17 E8 · wo 18 E9 08:00 · **za 21 E10 08:15** · ma 23 E11 · di 24 E12 · wo 25 E13 10:00 (abandoners) · do 26 E14 08:00 (E30) · vr 27 E15 08:00, E16 13:00, E17 18:00 · **za 28 E18 10:00** · **zo 29 Resend 3 10:00** · ma 30 E19 10:00, E20 17:00. SMS: za 14 12:00, do 19 12:00, ma 23 11:00, vr 27 09:00, za 28 12:00, ma 30 12:00 en 19:00.

Lege maildagen bij Homestead: ma 9, **do 12, vr 13**, ma 16, **do 19**, vr 20, **zo 22**. Daar landen de sprintmails.

### 2.3 Flows die op dezelfde dag mailen

| Flow | Tijd | Botsing en oplossing |
|---|---|---|
| Failure to launch T2SmtR (plan FTL-BF1 tot BF3, dag 30, 32, 35) | 19:00 lokaal, smart sending uit (plan, wacht op akkoord) | LAST-HOURS staat op 17:00, dus 2 uur ervoor. Kleine groep (~3 mails per persoon). Uitsluiting "Received Email ≥ 3 keer in de laatste dag" vangt de rest. |
| Welcome T4a5Mk W2 10:00, W3 tot W5 09:00; BFCM Welcome Rn556d | ochtend | Nieuwe aanmelders zitten in E30. Op een sprintdag krijgen ze hooguit W + hoofdmail + avondmail = 3. Welcome niet uitsluiten (W1 is $3,09 per ontvanger, de flow wint). |
| Cart TZG9Mx, Checkout QUBUQV, Browse WdRz5k/QNZyEb | op gedrag, C1 binnen 1 u | Sprintmails sluiten uit wie in het laatste uur een mail uit deze flows kreeg (zoals in het urgentieplan). Flow is meer waard (C1 $7,96, K1 $3,59). |
| BF-flowmails (v2, BFCODE in cart en checkout) | flowtijden | Geen sale-einddatum in flows (besluit 1 nov); sprintmails zijn campagnes, dus geen conflict. |
| Rise-datumflow X1 tot X4 (plan, nog niet live) | 23 nov 09:00, 28 nov, 29 nov, 30 nov 12:00 | X4 (30 nov 12:00) is dezelfde mail als CREDIT. Kies één: CREDIT als campagne en X4 uit, of X4 als flow en CREDIT vervalt. Voorstel: X4 = CREDIT (flow loopt per profiel op de echte vervaldatum). |

---

## 3. Het deadline-moment: drie regio's, tijdzone in de copy

Baseline van de brief: "tonight 23:59 ontvangerstijd". Een Shopify-korting, -prijs of Klaviyo-couponpool heeft één eindmoment voor iedereen. Eén eindmoment voor de hele wereld maakt de deadline voor een deel van de lezers onwaar (te vroeg of te laat; te laat is precies het Smooche-patroon "ends tonight" terwijl het doorloopt). Daarom per mechaniek **drie backend-deadlines**, en `{{DEADLINE}}` per regio met tijdzone:

| Regio | Wie | Eindmoment | `{{DEADLINE}}` (voorbeeld) | Echt voor de lezer |
|---|---|---|---|---|
| **US/AM** | US, CA, MX, rest Amerika | 23:59 PT (= 07:59 UTC volgende dag) | "tonight at 11:59 PM PT" | ET-lezer heeft tot 02:59 ET; in de copy staat het moment exact |
| **EU** | EU, UK, IE, CH, Midden-Oosten, Afrika | 23:59 CET (= 22:59 UTC) | "tonight at 11:59 PM CET" | UK tot 22:59, Dubai tot 02:59 lokaal; exact genoemd |
| **APAC** | AU, NZ, SG, HK, rest Azië | 23:59 AEDT (= 12:59 UTC) | "tonight at 11:59 PM Sydney time" | SG/HK tot 20:59 lokaal, NZ tot 01:59; exact genoemd |

Uitvoering: per regio een eigen Shopify-korting (FLASH, einde sale, gifts) of een eigen Klaviyo-coupon gekoppeld aan een eigen Shopify-kortingsregel (VIP), plus per regio een Klaviyo-campagne (US-campagne = US/AM, INT gesplitst in INT-EU en INT-APAC op profiel-land). Kan Floris voor FLASH de prijs per market zetten (Shopify Markets-prijslijst), dan is dat hetzelfde in één stap. De trekking heeft juridisch één sluitmoment (één set regels): **zondag 23:59 PT** voor iedereen, met de omrekening in de copy ("Monday at 6:59 PM Sydney time").

Lukt drie regio's niet: dan alleen US/AM met deadline, INT dezelfde dag zonder deadline-onderwerp (gewone BF-mail). Nooit één wereldtijd met "tonight" erin.

**Inplannen:** lokale verzending moet minstens 24 uur van tevoren gepland staan (APAC krijgt het eerst, 08:30 AEDT = 21:30 UTC de dag ervoor). Dus elke sprintmail uiterlijk **de dag ervoor om 12:00 CET** op Scheduled, met `send_past_recipients_immediately` uit.

---

## 4. Kalender

Tijden lokaal (ontvanger). Smart sending **uit** op alle sprintmails (anders verdringt de 08:15-campagne of een flowmail van de laatste 16 uur de avondmail en is de deadline voorbij). In plaats daarvan vaste uitsluitingen op elke sprintmail:

- Basis (Base exclusions), Unengaged 180 non-buyers, P7 (vanaf 23 nov P3, vanaf 27 nov order sinds 27 nov 00:00).
- Order geplaatst sinds de hoofdmail (voor resend en LAST-HOURS).
- Mail ontvangen uit Cart, Checkout of Browse in het laatste uur.
- Received Email ≥ 3 keer in de laatste dag (tot 26 nov), ≥ 4 keer (27 tot 30 nov).

### Week 2 · 8 tot 15 november

| Dag | Tijd lokaal | Mail | Doelgroep | Deadline (backend) | Wat er nog meer is die dag |
|---|---|---|---|---|---|
| zo 8 | 10:00 | (Homestead Resend 1, al bezig) | niet-openers E1 | geen | |
| ma 9 | | geen sprintmail | | | **Floris kiest FLASH-product en prijs** |
| di 10 | 09:00 | (E5 Homestead) | E30 | | |
| wo 11 | 09:00 | (E6 Homestead) | E90 | | **FLASH-kortingen staan en zijn getest, campagne Scheduled vóór 12:00 CET** |
| **do 12** | **08:30** | **1 FLASH** US: 2 Pans + 2 Lids flash-prijs; INT: extra % op sets | US: E90 + Product Viewers L30; INT-EU en INT-APAC: idem | do 12 nov 23:59 PT / CET / AEDT | geen Homestead-mail, geen SMS |
| do 12 | 14:00 | FLASH resend niet-openers, nieuw onderwerp ("Last hours: ..." uit copy.md) | ontving FLASH, niet geopend, geen order | zelfde | +5,5 u in plaats van +24 u: daarna is de deadline voorbij |
| do 12 | 17:00 | **4 LAST-HOURS** (Benjamin, platte tekst) op FLASH | FLASH geopend, niet geklikt, geen order | zelfde, ~7 u over | FTL-BF 19:00 (kleine groep) |
| **vr 13** | **08:30** | **2 VIP-WEEKEND** extra 10% met eigen code | alle kopers + E30 (US, INT-EU, INT-APAC) | code vervalt zo 15 nov 23:59 PT / CET / AEDT | **botst met Draft "BFCM kopers 1" (vr 13, 15:00 UTC, zelfde kopers)**: VIP vervangt die mail, of kopers 1 schuift naar ma 16 |
| za 14 | 08:15 | (E7 Free Gifts, Homestead) | All buyers + E90 | | SMS3 12:00. Geen sprintmail: zaterdag heeft al de VIP-code lopen |
| **zo 15** | **12:00** | VIP resend niet-openers, onderwerp "Your extra 10% ends tonight" | ontving VIP, niet geopend, geen order | zelfde | Homestead Resend 2 om 10:00: Homestead sluit ontvangers van de VIP-resend uit, of de VIP-resend sluit "ontving Resend 2" uit. Niet allebei aan dezelfde persoon |
| zo 15 | 17:00 | **4 LAST-HOURS** op VIP | VIP geopend, niet geklikt, geen order | ~7 u over | |

### Week 3 · 16 tot 22 november

| Dag | Tijd lokaal | Mail | Doelgroep | Deadline (backend) | Wat er nog meer is die dag |
|---|---|---|---|---|---|
| ma 16 | | geen sprintmail | | | Floris: ja/nee FLASH 2 en product; ja/nee VIP-weekend 2 |
| di 17 | 08:15 | (E8 Homestead) | E30 | | Rise L1 "You have $X waiting" staat in het tegoedplan op 19:00: zelfde uur als FTL. Voorstel L1 17:00 |
| wo 18 | 08:00 | (E9 Homestead) | E90 | | **Trekkingsregels gepubliceerd** (anders vervalt DRAW); FLASH 2 Scheduled vóór 12:00 CET |
| **do 19** | **08:30** | **1 FLASH 2** (optioneel, ander product) | E90 + Product Viewers L30 | do 19 nov 23:59 PT / CET / AEDT | Homestead SMS4 12:00 "No need to wait": laat de SMS de flash noemen of schuif hem naar vr 20 |
| do 19 | 14:00 / 17:00 | FLASH 2 resend niet-openers / **4 LAST-HOURS** | als do 12 | zelfde | |
| vr 20 | | geen sprintmail | | | **Floris bevestigt eindmoment sale 30 nov** (nodig voor GIFTS, CREDIT, aftelklok, E19/E20) |
| za 21 | 08:15 | (E10 Gift Guide, Homestead) | E90 | | |
| **zo 22** | **09:00** | **6 DRAW** "Order by Sunday midnight to enter this week's filter draw" | E90 + kopers (US, INT-EU, INT-APAC) | trekking sluit zo 22 nov 23:59 PT (één moment, omgerekend in de copy) | **botst met urgentieplan "v2-pricelist + R-a op E10" zo 22 10:00**: DRAW vervangt v2-pricelist; R-a op E10 schuift naar 13:00 en sluit DRAW-ontvangers uit |
| zo 22 | 13:00 | DRAW resend niet-openers | ontving DRAW, niet geopend, geen order | zelfde | |
| zo 22 | 17:00 | **4 LAST-HOURS** op DRAW | DRAW geopend, niet geklikt, geen order | zelfde | |

### Week 4 · 23 tot 30 november

| Dag | Tijd lokaal | Mail | Doelgroep | Deadline (backend) | Wat er nog meer is die dag |
|---|---|---|---|---|---|
| ma 23 tot wo 25 | | geen sprintmail | | | E11, E12, E13 (Homestead). Rise X1 23 nov |
| **do 26** | **17:00** | **2 VIP-WEEKEND 2** (optioneel, Thanksgiving-weekend) | alle kopers + E30 | code vervalt zo 29 nov 23:59 PT / CET / AEDT | E14 om 08:00 naar E30: dit wordt het tweede contact. 17:00 omdat Thanksgiving-ochtend in de US niet koopt; ruim voor FTL 19:00 |
| vr 27 tot za 28 | | geen sprintmail | | | E15 tot E18, v2-pricelist, v2-sat28, v2-proof. Al 3 à 4 per dag |
| zo 29 | 17:00 | **4 LAST-HOURS** op VIP 2 | VIP 2 geopend, niet geklikt, geen order | ~7 u over | Vervangt "VIP weekend 2 laatste uren 18:00" uit het urgentieplan. DRAW deze week alleen als blok in v2-sun29, geen eigen mail |
| **ma 30** | **07:00** | **5 GIFTS** "Your 5 free gifts end tonight" | E90 + abandoners L30 | einde sale en gifts ma 30 nov 23:59 PT / CET / AEDT | Vervangt v2-mon-am "Last day" (zelfde doelgroep, zelfde boodschap) |
| ma 30 | 10:00 | (E19 Cyber Monday, Homestead) | Lijst | | |
| **ma 30** | **12:00** | **3 CREDIT** "Your $X store credit expires tonight" | profielen met tegoed > 0 (Rise) | tegoed vervalt ma 30 nov 23:59, zelfde moment als de sale | Is Rise X4 (zelfde slot in het tegoedplan). Ontvangers van CREDIT worden uitgesloten van v2-mon-pm 13:00 |
| ma 30 | 13:00 / 17:00 | (v2-mon-pm Benjamin / E20 Final Hours) | | | |
| **ma 30** | **20:00** | **4 LAST-HOURS** op GIFTS, E19 en CREDIT | geopend, niet geklikt, geen order sinds 30 nov 00:00 | ~4 u over | v2-mon-late 20:00 gaat naar klikkers: de twee groepen sluiten elkaar uit |

---

## 5. Resend-regels

| | Gewone sale-mail (Homestead) | Sprintmail met deadline vandaag | VIP (deadline over 2 à 3 dagen) |
|---|---|---|---|
| Niet-openers (R-a) | +24 u in het weekend, anders +48 u, nieuw onderwerp | **zelfde dag +5,5 u** (13:00 of 14:00), nieuw onderwerp met de deadline | **+48 u** (zo 12:00), onderwerp "ends tonight" |
| Openers zonder klik (R-b) | +24 u, Benjamin-brief | **zelfde avond 17:00** = LAST-HOURS (op 30 nov 20:00) | **laatste avond 17:00** = LAST-HOURS |
| Altijd | geen order sinds hoofdmail; nooit twee resends naar dezelfde persoon op één dag | idem | idem |

Niet-openers en openers zonder klik zijn twee groepen die elkaar uitsluiten, dus elke lezer krijgt op een sprintdag hooguit één vervolgmail. Apple MPP telt veel automatische opens: LAST-HOURS kan daardoor ook naar mensen gaan die de hoofdmail nooit zagen. Dat is acceptabel omdat LAST-HOURS de deadline zelf herhaalt. Resend-onderwerpen komen uit `copy/copy.md`.

---

## 6. Maximaal aantal mails per persoon per dag

| Periode | Campagnes max | Alle mails (incl. flows) max | Hoe afgedwongen |
|---|---|---|---|
| 8 tot 26 nov | 2 | 3 | Uitsluiting "Received Email ≥ 3 keer in de laatste dag" op elke sprintmail; sprintmails alleen op dagen zonder Homestead-campagne (uitzondering do 26 met E14 en zo 15 en 22 met resends, steeds max 2 campagnes) |
| 27 tot 30 nov | 4 | 4 à 5 | Uitsluiting "≥ 4 keer in de laatste dag". Let op: het v2-plan geeft een E30-lezer op ma 30 vijf mails (07:00, 10:00, 13:00, 17:00, 20:00). Met GIFTS in plaats van v2-mon-am en de uitsluiting blijft het 4 |

Voorbeeld E30-lezer op do 12: hoofdmail FLASH 08:30, eventueel W3 09:00 (alleen nieuwe aanmelders), dan of de resend 14:00 (niet geopend) of LAST-HOURS 17:00 (geopend, niet geklikt). Maximaal 3.

---

## 7. Wat Floris in de backend moet zetten, en wanneer

Zonder deze stappen gaat de mail niet live; het slot wordt dan een gewone mail zonder deadline.

| # | Wat | Waar | Eindmoment(en) | Besluit uiterlijk | Klaar en getest uiterlijk |
|---|---|---|---|---|---|
| D1 | FLASH 1: US 2 Pans + 2 Lids flash-prijs, INT extra % op sets | Shopify: 3 kortingen of 3 market-prijzen | do 12 nov 23:59 PT, 23:59 CET, 23:59 AEDT; start uiterlijk wo 11 nov 13:00 UTC (do 00:00 AEDT) | **ma 9 nov 18:00 CET** | **wo 11 nov 12:00 CET** |
| D2 | VIP-weekend 1: extra 10%, one use, stapelt op de sale | Klaviyo: 3 unieke-codepools, elk aan een eigen Shopify-kortingsregel | zo 15 nov 23:59 PT / CET / AEDT | **di 10 nov** (percentage, doelgroep, stapelen met BFCODE/HI10) | **do 12 nov 12:00 CET** |
| D3 | Trekking: officiële regels met sluitmoment en "no purchase necessary" | Shopify-pagina + link in footer | zo 22 nov 23:59 PT | ma 16 nov | **wo 18 nov** |
| D4 | FLASH 2 (optioneel) | als D1 | do 19 nov 23:59 PT / CET / AEDT | ma 16 nov | **wo 18 nov 12:00 CET** |
| D5 | Eindmoment sale + einde gifts (automatische gift-regel stopt) | Shopify (sale, gift-automatisering) | ma 30 nov 23:59 PT / CET / AEDT (voorstel; DECISIONS zegt nog "geen harde datum tot Floris die geeft") | **vr 20 nov** | wo 25 nov |
| D6 | VIP-weekend 2 (optioneel) | als D2 | zo 29 nov 23:59 PT / CET / AEDT | ma 23 nov | **wo 25 nov 12:00 CET** |
| D7 | Rise-tegoed met vervaldatum, saldo en vervaldatum gesynchroniseerd naar Klaviyo | Rise.ai + Klaviyo-profielen | ma 30 nov 23:59, gelijk aan D5 (het tegoedplan zegt 23:59 ET: kiezen) | ma 16 nov (L1 staat op 17 nov) | **vr 20 nov**; niet live op 27 nov = CREDIT vervalt |

---

## 8. Botsingen en open punten

1. **Draft "BFCM kopers 1" (vr 13 nov 15:00 UTC, kopers)** valt op dezelfde dag en doelgroep als VIP-WEEKEND. Eén van de twee: voorstel VIP vervangt kopers 1, of kopers 1 naar ma 16.
2. **Zo 15 nov**: Homestead Resend 2 (10:00) en VIP-resend (12:00) raken grotendeels dezelfde niet-openers. Wederzijds uitsluiten.
3. **Zo 22 nov**: het urgentieplan zet daar v2-pricelist + R-a op E10 (10:00). DRAW neemt het slot; R-a naar 13:00 met uitsluiting van DRAW-ontvangers.
4. **Do 19 nov**: Homestead SMS4 12:00 op een FLASH-dag. Laten aansluiten of schuiven.
5. **Ma 30 nov**: v2-plan heeft 5 mails voor E30, plus Rise X4 12:00 en CREDIT. GIFTS vervangt v2-mon-am, CREDIT = X4, cap 4 per persoon.
6. **Tijdzone eind sale en tegoed**: tegoedplan zegt 23:59 ET, deze kalender 23:59 per regio. Eén keuze voor alles (D5 = D7), anders zegt de ene mail iets anders dan de andere.
7. **Rise L1 di 17 nov 19:00** valt op het FTL-uur. 17:00 voorgesteld.
8. **E5/E6 drafts staan op 09:00**, de Homestead-kalender zegt 08:15/08:00. Geen probleem voor de sprint, wel afstemmen.
9. **Smart sending uit** op sprintmails betekent dat de bescherming van 16 uur weg is; de uitsluitingen in sectie 4 vervangen hem. Vangrail per verzending vanaf 1.000 ontvangers: spam boven 0,15% of afmelding boven 1,5% = volgende sprintmail stoppen.
10. **"24-hour"** in de FLASH-copy: met drie regio's loopt de korting per regio één kalenderdag, niet precies 24 uur na ontvangst. Copy houdt "ends tonight" en "today only", geen "24 hours" als exacte duur tenzij de regio-korting precies 00:00 tot 23:59 loopt (dan klopt het).
