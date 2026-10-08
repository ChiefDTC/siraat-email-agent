# 02 · Bottom-up omzetmodel: wat er echt te halen is, en waar het plafond ligt

Datum: 8 oktober 2026. Alleen gelezen: Klaviyo (metric aggregates en flow-values-report, revision 2025-10-15) en Shopify (ShopifyQL). Niets gewijzigd. Basisjaar: 8 oktober 2025 t/m 7 oktober 2026 (365 dagen, dus inclusief BFCM 2025). Data: `02-instroom.csv` (trechter) en `02-model.csv` (model per stroom, met formule-invoer en bron per regel). Vervangt `flow-potentie.md` niet, maar legt het ernaast.

## Kort

| | Nu (365 d) | Realistisch | Ambitieus | Plafond |
| --- | --- | --- | --- | --- |
| Omzet uit flows plus nieuwe stromen | **$1,94 mln** | $2,96 mln | $4,39 mln | $6,81 mln |
| **Extra per jaar (Klaviyo-geattribueerd)** | | **+$1,02 mln** | **+$2,45 mln** | **+$4,87 mln** |
| Waarvan waarschijnlijk echt extra (incrementeel) | | +$0,53 mln | +$1,30 mln | +$2,62 mln |
| Aandeel van de totale omzet ($18,34 mln) | 10,6% | 16,1% | 24,0% | 37,1% |

De eigenaar heeft gelijk dat $0,9 mln niet het plafond is. Maar het grote geld zit maar voor de helft in "betere flows". De andere helft komt uit dingen die nu helemaal ontbreken: SMS, meer inschrijvers uit de pop-up, BFCM goed doen en een paar kleine nieuwe flows. En ongeveer de helft van alle geattribueerde omzet zou ook zonder mail gekomen zijn. Eerlijk getal om op te sturen: **ambitieus +$2,4 mln geattribueerd, ongeveer +$1,3 mln echt extra per jaar.**

---

## 1. Instroom en trechters (eigen data)

### 1.1 Volumes per dag

| Stroom | 365 d per dag | 90 d per dag | Bron |
| --- | --- | --- | --- |
| Nieuwe inschrijvers Email List | **643** | **641** (laatste 30 d: 607) | SCvkku, List = Email List |
| waarvan koopt binnen 10 min (koopt al in de sessie) | ~130 (20,3%) | | timing 01 §6 |
| dus nieuwe prospects voor welcome | **~510** | ~510 | |
| Uitschrijvingen | 252 | 325 (september) | YcWddQ |
| Netto lijstgroei | ~390 | ~300 | inschrijvers min uitschrijvers |
| Extra BFCM-lijst (alleen nov/dec 2025) | 45.396 in totaal | 0 | List "EB [DG] BFCM 2025" |
| Checkout Started (uniek) | 326 | 289 | RfMvni |
| echte verlaters (geen order na 15 min, 26,1%) | ~85 | ~75 | timing 01 §1b |
| Added to Cart (uniek) | 351 | 283 | QXcV8K (47% van de events is een automatische gift) |
| Viewed Product onsite (uniek) | 1.186 | 1.116 | XNtYMB |
| Active on Site (uniek, herkend profiel) | 1.488 | 1.427 | UdCdLD |
| Bezoekers webshop | ~11.300 | | ShopifyQL sessions (4,13 mln bezoekers, 5,28 mln sessies) |
| Orders | 248 | 201 | Placed Order (Shopify: 90.134 per jaar) |
| Omzet | $50.246 | $42.705 | Placed Order |

**De 300 tot 400 van de eigenaar klopt, maar dan als netto groei.** Bruto komen er 640 per dag bij, waarvan ~510 die nog niet gekocht hebben. Tegelijk schrijven 250 tot 325 per dag zich uit. Netto groeit de lijst met 300 tot 390 per dag.

### 1.2 Bereik: wie komt nu in een flow (gemiddelde jul t/m sep 2026, per maand)

| Trigger | Mensen per maand | Unieke ontvangers flow | Bereik | Oordeel |
| --- | --- | --- | --- | --- |
| Welcome | 20.201 inschrijvers | 21.715 (SiaNLu) | ~100% | goed, behalve BFCM-lijst (zie §3.3) |
| Checkout | 2.336 verlaters | 2.987 (twee flows, dubbel) | ~100% | goed; dubbele trigger weg in v4 |
| Cart | 9.122 unieke ATC (incl. gifts) | 5.264 | ~100% van de echte verlaters | goed |
| Browse | 34.952 bekijkers | 22.394 (twee flows, overlap) | ~64% | redelijk; filters en herinstap 7 d |
| Active on Site zonder productview | ~9.000 | 0 | **0%** | gat: geen site-flow |
| Post-purchase | 6.213 kopers | 6.404 | ~100% | goed |
| Winback | ~6.800 kopers 2 mnd eerder | 5.675 | ~83% | redelijk |
| Bezoekers die Klaviyo herkent | 11.300 per dag | 1.488 Active on Site | **~13%** | het echte bereikplafond van browse/site |

Conclusie: **bereik is niet het probleem in de bestaande flows.** Iedereen die we kennen, krijgt al mail. Het bereik groeit alleen door meer mensen te herkennen (meer inschrijvers, SMS, klik-cookies) en door de gaten: BFCM-lijst, site abandonment.

### 1.3 Herstel en conversie per stroom (365 d, Klaviyo flow-report)

| Stroom | Delivered | Orders | Omzet | Per ontvanger | AOV | Herstel door flow | Totaal herstel 7 d (timing) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Welcome (+FTL) | 1.562.931 | 3.987 | $871.437 | $0,56 | $219 | 1,70% van inschrijvers | dag 1-30: 2,82% van niet-kopers |
| Checkout | 134.068 | 1.254 | $291.769 | $2,18 | $233 | 4,0% van verlaters | 12,3% |
| Cart | 168.728 | 1.049 | $253.885 | $1,50 | $242 | 2,0% van instromers | 8,5% |
| Browse | 261.543 | 1.420 | $299.378 | $1,14 | $211 | 0,44% van instromers | 6,3% (onsite) |
| Post-purchase | 389.903 | 870 | $144.899 | $0,37 | $167 | 1,2% van nieuwe klanten | |
| Winback | 103.896 | 122 | $21.779 | $0,21 | $179 | 0,17% van kopers | |
| Overig (review, lead magnets, BIS, sunset) | 218.650 | 333 | $61.287 | | | | |
| **Totaal flows** | **2.839.719** | **9.035** | **$1.944.434** | $0,68 | $215 | | |

- E-mail totaal: $3,13 mln (17,0%), flows $1,94 mln (10,6%), campagnes ~$1,18 mln. SMS: $15.855 sinds juli.
- **November 2025 (BFCM): flowaandeel 6,2%**, december 9,6%, de rest van het jaar 9,4 tot 15,1%. In de grootste maand van het jaar deden de flows het slechtst.
- AOV US tegen internationaal: 365 d $218 tegen $217 (45% US); laatste 90 d is US 66% van de orders, AOV $230.
- Herhaling: 9,2% van de kopers koopt ooit een tweede keer, 8,0% binnen 365 d, mediaan 35 dagen, AOV 2e order $177 (personalisatie 01 §2.2, timing 01 §7). Shopify: 7.487 terugkerende tegen 80.912 nieuwe klanten per jaar.

---

## 2. Per flow: volume × bereik × conversie × AOV

Formule per regel: **omzet = volume × bereik × conversie × AOV**. De conversie "nu" is teruggerekend uit de echte 365-dagenomzet, zodat het model op vandaag sluit. Per scenario krijgt elke hefboom een factor met een eigen bron. Alle getallen in `02-model.csv`.

| Stroom | Volume per jaar | Bereik | Conv. nu | AOV | Nu | Realistisch | Ambitieus | Plafond |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Welcome (+FTL) | 234.576 inschrijvers | 100% | 1,70% | $218 | $871k | $1.077k (conv ×1,2, AOV ×1,03) | $1.386k (×1,5, ×1,06) | $1.917k (×2,0, ×1,10) |
| Checkout | 31.008 verlaters | 100% | 4,04% | $233 | $292k | $376k (×1,25, ×1,03) | $479k (×1,55, ×1,06) | $642k (×2,0, ×1,10) |
| Cart | 51.792 instromers | 100% | 2,03% | $242 | $254k | $311k (×1,2, ×1,02) | $379k (×1,45, ×1,03) | $480k (×1,8, ×1,05) |
| Browse | 321.464 instromers | 100% (+10/25% herkenning) | 0,44% | $211 | $299k | $419k (×1,4) | $555k (bereik ×1,1, ×1,8, ×1,03) | $817k (×1,25, ×2,6, ×1,05) |
| Post-purchase | 80.912 nieuwe klanten | 90% | 1,19% | $167 | $145k | $207k (×1,35, AOV $177) | $269k (×1,75) | $361k (×2,35) |
| Winback | 89.189 kopers | 78% | 0,17% | $179 | $22k | $37k (0,30%) | $57k (0,45%) | $87k (0,70%) |
| Overige flows | | | | | $61k | $61k | $61k | $61k |
| VIP (nieuw) | 7.487 herhaalkopers | 85% | | $169 | $0 | $32k (3%) | $54k (5%) | $75k (7%) |
| Anniversary (nieuw) | 75.000 kopers kookgerei | 60% | | $177 | $0 | $24k (0,3%) | $40k (0,5%) | $64k (0,8%) |
| Site abandonment (nieuw) | ~55.000 | 100% | | $211 | $0 | $23k (0,20%) | $35k (0,30%) | $52k (0,45%) |
| **Subtotaal flows** | | | | | **$1,94 mln** | **$2,57 mln** | **$3,31 mln** | **$4,56 mln** |

### Onderbouwing per hefboom

**Welcome** (grootste post, $871k). Volume ligt vast (inschrijvers), bereik is al 100%, dus alles zit in conversie en AOV.
- Realistisch ×1,2: de beste maand van dit jaar haalde 3,51% conversie in dag 1 tot 30 bij niet-kopers tegen 2,82% gemiddeld (lijst 01 §1, maart). Dat is ×1,24, dus haalbaar met dezelfde lijst.
- Ambitieus ×1,5: welcome-mail 1 uit februari/maart deed $4,01 per ontvanger tegen $2,73 voor de huidige (history §1, ×1,47); Alia-cohort januari 4,44% (×1,57). Tailoring op `shopping_for` (personalisatie, lijst 03 §1) en de dag-7-split op intentie.
- Plafond ×2,0: dan halen we $2,30 per ontvanger, net onder het Klaviyo-gemiddelde voor welcome ($2,35 tot $2,65). Top 10% ($20,92) is voor een giveaway-lijst geen maatstaf.
- AOV: set-trede in W4 ($349) en deksel: +3/6/10%. Nu $218.
- Wat het nu kost: 1,97% uitschrijving per welcome-mail, 16,3% van de inschrijvers weg binnen 30 dagen.

**Checkout** ($292k). 26,1% van de starters koopt niet binnen 15 minuten: 31.000 verlaters per jaar. Flows herstellen er nu 4,0% van; in totaal komt 12,3% binnen 7 dagen terug.
- Ambitieus ×1,55 = het eigen beste pad (New AB Checkout, juli 2026): opgeteld 4,6% conversie per instromer tegen 2,96% gemiddeld (timing 01 §2, meetplan 06 §1).
- Plafond ×2,0 met AOV +10% (C3 set-upgrade "three for $349", deksel). Klaviyo top 10% cart ($28,89 per ontvanger) halen we niet; ons beste losse bericht ooit is $7,83.

**Cart** ($254k). Cart 1 "we saved these" deed 0,97% conversie tegen 0,86% nu; een code met deadline won van een kale code (cart 3 tegen cart 2, history §1). Klaviyo-gemiddelde $3,65 per ontvanger tegen ons $1,50: ruimte, maar onze verlaters kopen een pan van $242, geen T-shirt. Plafond ×1,8. AOV beperkt (+2 tot 5%): de deksel-regel in K2 (24% van de pan-orders heeft al een deksel).

**Browse** ($299k). Nu één mail. In checkout en cart voegen de vervolgmails samen 60 tot 70% van mail 1 toe; B2 is dus realistisch ×1,4. De browse-versie van april 2025 deed $2,90 per ontvanger (×3,1 op nu); plafond ×2,6. Bereik: Klaviyo herkent ongeveer 13% van de bezoekers. Elke extra herkende bezoeker is een extra browse-instromer: +10% (ambitieus) en +25% (plafond), alleen haalbaar via meer inschrijvers en SMS (zie 3.1 en 3.2). Dit is een aanname zonder eigen meting.

**Post-purchase en herhaling.** Nu 9,2% herhaalkopers. De bouwstenen met eigen bewijs:
- Deksel: 24% van de pan-orders neemt hem al mee; 22% van de herhalers zonder deksel koopt hem bij order 2 (mediaan 24 dagen). De campagne "Put a lid on it" aan pankopers: 0,74% conversie, index 6,9.
- Tweede maat: Standard naar Mini 19%, Small naar Mini 33% van de tweede orders.
- Realistisch 1,6%, ambitieus 2,1%, plafond 2,8% conversie op 73.000 bereikte nieuwe klanten, AOV $177.

**Controle via herhaalratio** (alle kanalen, eerste jaar): elke procentpunt extra herhaling = 80.912 × 1% × $177 × 1,15 (derde orders) = **~$165k**.

| Herhaling binnen 365 d | Extra omzet per jaar | Klopt met model? |
| --- | --- | --- |
| 8,0% (nu) | 0 | |
| 10% | +$330k | ≈ ambitieus: post-purchase + winback + VIP + anniversary + strips samen +$320k |
| 11,5% | +$580k | ≈ plafond van dezelfde flows (+$554k) |
| 15% | +$1,16 mln | niet onderbouwd |
| 20% | +$2,0 mln | niet onderbouwd |

15 tot 20% is voor een pan die 75 jaar garantie heeft niet realistisch op basis van onze data: zelfs bij eerdere kopers in checkout is de basis maar 26,9%, en de categorie verkoopt "één keer goed". Het eerlijke plafond ligt rond 11 tot 12%.

---

## 3. Wat ontbreekt en wat er blijft liggen

| Item | Formule | Realistisch | Ambitieus | Plafond | Bron en kanttekening |
| --- | --- | --- | --- | --- | --- |
| **SMS** | 234.576 inschrijvers × opt-in × $ per SMS-abonnee per jaar | $113k (12% × $4) | $310k (22% × $6) | $601k (32% × $8) | Nu 3,6% opt-in (8.538), laatste 90 d 7,6%. Eigen opbrengst: $15.855 op 15.373 SMS = $1,03 per SMS; 4 tot 8 SMS per abonnee per jaar. Mature DTC: SMS 10 tot 20% van de omzet, home goods aan de onderkant (eightx.co). Kosten per SMS en buitenland niet afgetrokken. |
| **Pop-up / inschrijfratio** | extra inschrijvers × waarde per extra inschrijver via e-mail | $94k (+10% × $4) | $281k (+20% × $6) | $657k (+35% × $8) | Nu 643 per dag = 4,4% van de sessies. Niet-koper levert $9,78 in dag 1 tot 90 (alle kanalen), ~50% via e-mail. Dit is Alia-werk (tweede stap, exit-intent), geen flowwerk. |
| **BFCM/Q4** | omzet nov+dec ($4,58 mln) × flowaandeel − nu ($333k) | $56k (8,5%) | $153k (10,6%) | $263k (13%) | Nov 2025 flowaandeel 6,2%. 45.396 BFCM-inschrijvers op een aparte lijst kregen vermoedelijk geen welcome (SiaNLu nov: 2.416 uniek). Cadeau-hoek en "order by"-datum in browse/cart/welcome horen hier. Deadline: vóór 20 november. |
| **Vaatwasstrips (replenishment)** | ~56.000 orders met strips als gift × conv naar abonnement × 6 mnd × $20 | $34k (0,5%) | $67k (1,0%) | $134k (2,0%) | Nu 0,16% (WvRupU: 31 orders op 19.190) en 25 Recharge-starts. Abonnement $25 met 20% korting. |
| **Review-to-referral** | 80.912 nieuwe klanten × aandeel via verwijzing × $200 | $40k (0,25%) | $121k (0,75%) | $324k (2%) | Geen eigen data (geen programma); zwakste schatting. Kost een beloning per verwijzing. |
| **Price drop** | 4 sales × 35.000 bekijkers × 40% mailbaar × conv × $211 | $18k | $35k | $53k | Conversie 0,15 tot 0,45%, onder browse. Campagnes vangen een deel al. |
| **Back in stock** | aanmeldingen × 4% × $204 | $8k | $20k | $33k | Nu 261 aanmeldingen in 3 maanden; flow 4% conversie ($8,15 per ontvanger). 12-pcs en 6-pcs zitten in backorder. |
| **Sunset + frequentieplafond** | vermeden verlies op e-mailomzet | $30k | $90k | $190k | Outlook/Yahoo = 31,6% van de mail, spam 0,31% en 0,11%. 20% minder inbox daar ≈ 6% van $3,13 mln = $190k. Eén maand 30% minder inbox kost $50k tot $70k (lijst 03 §5). |
| Post-purchase cross-sell op product | | in §2 | | | Zit in P3/R1/VIP (niet dubbel tellen). |
| Cadeau-flows | | in BFCM/Q4 | | | Data ziet 4,8 tot 8,5% cadeau, enquête 19%. |
| **Totaal ontbrekend** | | **+$392k** | **+$1,08 mln** | **+$2,25 mln** | |

---

## 4. Uitkomst

### 4.1 Tabel per stroom, drie scenario's (USD per jaar)

| Stroom | Nu | Realistisch | Ambitieus | Plafond | Extra ambitieus | Incrementeel deel (aanname) |
| --- | --- | --- | --- | --- | --- | --- |
| Welcome (+FTL) | 871.437 | 1.077.096 | 1.385.585 | 1.917.161 | +514.148 | 50% |
| Checkout | 291.769 | 375.653 | 479.376 | 641.892 | +187.607 | 40% |
| Cart | 253.885 | 310.755 | 379.177 | 479.843 | +125.292 | 50% |
| Browse | 299.378 | 419.129 | 555.047 | 817.302 | +255.669 | 50% |
| Post-purchase | 144.899 | 207.350 | 268.788 | 360.943 | +123.889 | 40% |
| Winback | 21.779 | 37.024 | 56.625 | 87.116 | +34.846 | 50% |
| Overige flows | 61.287 | 61.287 | 61.287 | 61.287 | 0 | |
| VIP | 0 | 32.265 | 53.775 | 75.286 | +53.775 | 30% |
| Anniversary | 0 | 23.895 | 39.825 | 63.720 | +39.825 | 50% |
| Site abandonment | 0 | 23.210 | 34.815 | 52.222 | +34.815 | 60% |
| SMS | 0 | 112.596 | 309.640 | 600.515 | +309.640 | 50% |
| Pop-up / inschrijfratio | 0 | 93.830 | 281.491 | 656.813 | +281.491 | 70% |
| BFCM/Q4 | 0 | 56.293 | 152.540 | 262.537 | +152.540 | 50% |
| Vaatwasstrips | 0 | 33.600 | 67.200 | 134.400 | +67.200 | 70% |
| Price drop | 0 | 17.724 | 35.448 | 53.172 | +35.448 | 50% |
| Back in stock | 0 | 8.160 | 20.400 | 32.640 | +20.400 | 50% |
| Review-to-referral | 0 | 40.456 | 121.368 | 323.648 | +121.368 | 50% |
| Sunset + plafond | 0 | 30.000 | 90.000 | 190.000 | +90.000 | 100% |
| **Totaal** | **1.944.434** | **2.960.323** | **4.392.387** | **6.810.497** | **+2.447.953** | |
| **Extra per jaar** | | **+$1,02 mln** | **+$2,45 mln** | **+$4,87 mln** | | |
| **Waarvan incrementeel** | | **+$0,53 mln** | **+$1,30 mln** | **+$2,62 mln** | | |

Per nieuwe prospect (510 per dag): nu $4,68 welcome-omzet per prospect, ambitieus $7,44. Dat is $2.400 per dag nu, $3.800 ambitieus.

### 4.2 Waarom het oude model lager uitkwam

Het oude model (`flow-potentie.md`) gaf +$0,48 / +$1,0 / +$1,9 mln. Het middelste getal ($1,0 mln, door de eigenaar onthouden als $0,9 mln) is ongeveer ons realistische scenario. Het verschil zit in vijf aannames:

1. **90 dagen × 4 in plaats van 365 dagen.** De oude basis was $416k × 4 = $1,66 mln; het echte jaar is $1,94 mln. Q4 (nov+dec = 25% van de omzet) zat er niet in.
2. **Alleen omzet per ontvanger opschalen, op hetzelfde volume.** Geen nieuwe stromen behalve $84k tot $196k per jaar voor nieuwe flows. SMS, pop-up, BFCM-lijst, strips, referral: nul.
3. **Geen trechter.** Het oude model rekende niet met inschrijvers × conversie × AOV, dus zag het niet dat bereik al 100% is (en dus niet de hefboom) en dat herkenning (13% van de bezoekers) en lijstgroei dat wel zijn.
4. **BFCM-gat niet gezien.** Flows deden 6,2% in november tegen 10,6% over het jaar.
5. **Te voorzichtig op de beste eigen mails, te ruim op welcome.** Oud basis gaf welcome ×1,6 en ambitieus ×2,2 zonder eigen bewijs; nieuw is ×1,5 ambitieus met twee eigen ankers. Checkout oud ×1,7 basis; nieuw ×1,55 ambitieus (eigen beste pad). De bestaande flows samen komen in beide modellen ongeveer op hetzelfde uit. **Het "veel meer" zit dus niet in betere flowmails, maar in nieuwe kanalen en bereik.**

### 4.3 Echte risico's

1. **Attributie tegen incrementaliteit.** Klaviyo geeft een order aan de laatste mail in 5 dagen. In checkout koopt 12,3% van de verlaters binnen 7 dagen, mail of niet; mail na 10 minuten gaf maar +7% kopers tegen 30 minuten (timing 1c). Daarom de kolom "incrementeel" (30 tot 70%, aanname). Meten met T01 (oud tegen nieuw) en een vaste holdout van 10% (meetplan 06).
2. **Marge van codes.** 50,9% van de orders gebruikt al een code. Bij 10% korting en 60% brutomarge moet een code +20% kopers opleveren om quitte te spelen (+33% bij 15%). T02 kan dat pas na ~12 weken onderscheiden; tot dan "geen code" als standaard.
3. **Frequentie en uitschrijvingen.** Welcome 1,97% uitschrijving per mail; 16,3% van de inschrijvers weg in 30 dagen; welcome plus browse in dezelfde week 7,24% tegen 5,14% uitschrijving. Van 3 naar 4 mails per week springt de uitschrijving van 0,98% naar 1,60%. Meer flows betekent meer mail per persoon: het plafond van 3 campagnes per week (v4 §1.3) moet aan.
4. **Deliverability.** Outlook 0,31% spam in Q3 (63% van alle klachten), Gmail onzichtbaar zonder Postmaster Tools, 46% van de ontvangers niet betrokken. Boven 0,3% gaat ook de checkoutmail naar spam: alles in deze tabel hangt hiervan af.
5. **SMS en pop-up zijn geen e-mailwerk.** Ze vragen Alia-toegang, SMS-kosten (buitenland duur), toestemming per land (TCPA in de US). De bedragen zijn de minst zekere van het model.
6. **Seizoen en mix.** Het basisjaar bevat BFCM 2025 en drie sales; internationaal zakte van 55% naar 34% van de orders. Bij minder verkeer schaalt alles evenredig mee.

---

## 5. Top 10 hefbomen (gerangschikt op extra omzet ambitieus, met moeite)

| # | Hefboom | Extra per jaar (ambitieus) | Realistisch tot plafond | Moeite | Waarom |
| --- | --- | --- | --- | --- | --- |
| 1 | Welcome v4 live, met tailoring op `shopping_for` en dag-7-split | +$514k | +$206k tot +$1,05 mln | laag (gebouwd) | Grootste volume; eigen beste maand en mail bewijzen ×1,2 tot ×1,5 |
| 2 | SMS opbouwen (tweede stap pop-up, SMS in welcome en abandonment) | +$310k | +$113k tot +$601k | hoog | Nu 3,6% opt-in, vrijwel geen omzet |
| 3 | Pop-up: inschrijfratio omhoog (Alia, exit-intent, tweede stap) | +$281k | +$94k tot +$657k | middel | Elke extra inschrijver voedt welcome, browse en campagnes |
| 4 | Browse v4 met B2 en paren-regel | +$256k | +$120k tot +$518k | laag (gebouwd) | Nu één mail; eigen versie 2025 deed ×3 |
| 5 | Checkout v4 (C1 zonder code, C3 set-upgrade, C4 code) | +$188k | +$84k tot +$350k | laag (gebouwd) | Eigen beste pad ×1,55 |
| 6 | BFCM/Q4: BFCM-lijst in welcome, flows niet stilleggen, "order by" | +$153k | +$56k tot +$263k | laag tot middel, vóór 20 nov | Flowaandeel nov 6,2% tegen 10,6% |
| 7 | Cart v4 (deadline-code, deksel-regel) | +$125k | +$57k tot +$226k | laag (gebouwd) | Cart 1 en cart 3 historisch beter |
| 8 | Post-purchase P3 deksel in jouw maat, R1 tweede maat | +$124k (+$35k winback) | +$62k tot +$216k | laag (gebouwd) | 22% van de herhalers koopt de deksel |
| 9 | Review-to-referral | +$121k | +$40k tot +$324k | hoog (programma, beloning) | Geen eigen data, zwakst onderbouwd |
| 10 | Sunset + frequentieplafond | +$90k (beschermd) | +$30k tot +$190k | laag | Beschermt de andere negen |

Daarna: vaatwasstrips (+$67k, middel), VIP (+$54k, laag), anniversary (+$40k, laag), price drop (+$35k, middel), site abandonment (+$35k, laag), back in stock (+$20k, laag).

**Volgorde om te doen:** 1, 4, 5, 7, 8 en 10 zijn gebouwd of bijna; samen +$1,33 mln ambitieus. Dan 6 (tijdkritisch). SMS en pop-up (2, 3) zijn een apart project met de grootste onzekerheid en het grootste plafond.

## Methode en beperkingen

- Volumes: Klaviyo metric aggregates (US/Eastern, dagelijks, "unique" = som van unieke profielen per dag). Omzet per flow: flow-values-report `last_365_days`, conversion metric RSNxYV. Shopify: ShopifyQL `sales` en `sessions`.
- Het veld `$value` van Checkout Started bevat onbruikbare bedragen (miljoenen per maand) en is niet gebruikt.
- Bezoekers per maand opgeteld (een bezoeker in twee maanden telt twee keer); herkenning 13% is dus een ondergrens.
- Benchmarks (Klaviyo-gemiddelde en top 10% per flow, SMS-aandeel) komen uit derde bronnen die Klaviyo-rapporten citeren; klaviyo.com was vanuit deze sessie niet bereikbaar: [inboxally.com](https://www.inboxally.com/blog/klaviyo-email-benchmarks), [eightx.co flows](https://eightx.co/blog/average-klaviyo-flow-revenue-contribution-benchmarks), [eightx.co SMS](https://eightx.co/blog/average-ecommerce-sms-revenue-share-by-vertical-2026), [1digitalagency.com](https://www.1digitalagency.com/blog/the-7-essential-klaviyo-flows-every-shopify-store-needs-with-revenue-benchmarks-70284/).
- Incrementeel aandeel per stroom is een aanname tot T01 en de holdout iets anders laten zien.
- BFCM-lijst zonder welcome: afgeleid uit de ontvangers van SiaNLu in november; even nakijken of er in november 2025 een aparte BFCM-welcome draaide.
