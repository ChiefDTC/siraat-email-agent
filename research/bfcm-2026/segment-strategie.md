# BFCM 2026 · Segmentstrategie voor de resterende verzendingen (27 nov t/m 5 dec)

Stand: donderdag 26 nov 2026, 14:50 UTC. Alleen gelezen in Klaviyo (campagnes, campaign-values-reports met conversiemetric Placed Order RSNxYV, segmenten, billing-usage, metric-aggregates). Niets gewijzigd. Bedragen in USD, Klaviyo-attributie. Ruwe data: scratchpad `golive/bfcm26/` (campaigns_*.json, reports.json, segments.json, billing.json).

## Samenvatting

1. **Ga niet naar de hele lijst (RNuYDm/VdfJTJ), maar naar 90D (VMjhb2 / XrFa5r) voor alle golven behalve de Black Friday-aankondiging zelf (Email 15, 08:00): die mag één keer naar 180D (TntB6g / S9BZVJ).** De staart tussen 90D en 180D (~24k US-profielen) leverde maandag in Email 11 ongeveer 3 procent opens, 0 kliks en dus ongeveer $0 omzet, maar kostte 24.000 mails. De staart tussen 180D en "alles" is al weg zodra Ur6Ehr wordt uitgesloten (RNuYDm min Ur6Ehr is in de praktijk hetzelfde publiek als TntB6g, verschil ~2k).
2. **Deliverability is geen reden om krap te gaan, budget wel.** Alle US-sends deze week: spam 0,029 tot 0,042 procent (grens 0,3), uitschrijf 0,33 tot 0,56 procent. INT: spam 0,002 tot 0,055 procent. Email 11 naar de hele lijst (min Ur6Ehr) deed het niet slechter dan de 90D-sends (spam 0,035, uitschrijf 0,47).
3. **Het e-mailplafond is het echte probleem.** 2.022.321 van 2.900.000 gebruikt (teller loopt bijna live mee, vandaag al grotendeels verwerkt). Over tot 7 dec: ~845k na vandaag. Het Homestead-plan zoals het nu staat (Fri 3 golven naar hele lijst + za resend + ma Cyber Monday + flows ~18k/dag) kost ~1,1 miljoen. Zelfs het zuinige plan hieronder kost ~1,0 miljoen. **Verhoog het plan vandaag nog naar minstens 3,5M voor deze cyclus** (of controleer dat Klaviyo automatisch upgradet in plaats van blokkeert).
4. **Smart Sending staat AAN op Email 15, 16 en 17 en op SMS 6.** Met het venster van 16 uur krijgt bijna niemand Email 16 (13:00) en Email 17 (18:00), omdat ze 5 of 10 uur eerder Email 15 kregen. Vandaag kostte Smart Sending al ~22k ontvangers op onze Thanksgiving-mail (72.842 van ~94.600). Op 27 en 30 nov Smart Sending uit op alle campagnes (dat was ook de afspraak uit het INT-plan van 1 nov).
5. **Verwachte omzet vrijdag (e-mail US+INT, 3 golven naar 90D/180D, ~450k mails): $100k tot $150k** bij $0,28 tot $0,38 per ontvanger (1,5 tot 2 keer het weekgemiddelde van $0,19, zoals vorig jaar: $0,31 op 26 nov naar $0,59 tot $0,65 op BF). Plus SMS 6 US ~37k ontvangers x $0,64 tot $0,80 = $24k tot $30k.
6. **SMS: VJdd3C (37.4k) en Xrxk9P (36.4k, engaged 180D) zijn vrijwel hetzelfde publiek; neem VJdd3C.** Maar: elke SMS kost ~2 procent uitschrijvers (SMS 4: 1,97, SMS 5: 2,08 procent) en er is nog $825 SMS-krediet voor 4 geplande SMS-golven. Maximaal 2: SMS 6 (BF) en de laatste-dag-SMS.
7. Zaterdag-resend (E4) niet naar de hele lijst maar naar niet-openers van Email 15/16 binnen 90D (segment nog te maken) of anders naar VMjhb2 met Smart Sending aan; plus onze M2 naar afhakers (vorig jaar de beste send van het weekend, $0,77 per ontvanger; dit jaar Email 13 naar kijkers en afhakers $0,257, beste e-mail van de week).
8. Cyber Monday was vorig jaar zwak ($0,15 tot $0,25 tegen $0,59 tot $0,65 op BF). Eén golf naar 90D plus SMS plus onze M3 naar kopers is genoeg; geen "Final Day" zolang de einddatum (30 nov of 5 dec) niet vaststaat.
9. Fout gevonden: Email 11 INTL (23 nov) ging naar R5LmyU (INT SMS-abonnees, 3.634 ontvangers) in plaats van VdfJTJ (~65k). De INT-lijst heeft de BF-week-aankondiging dus niet gehad.
10. Als het plan niet wordt verhoogd: schrap in deze volgorde: de 180D-staart overal (bespaart ~35k per golf), de zondag-send, de resend naar iedereen (alleen niet-openers), Email 17 INTL, M1 beperken tot engaged kopers.

## 1. Vorig jaar: BFCM 24 nov t/m 2 dec 2025 (e-mail; er waren nog geen SMS-campagnes, de eerste SMS was juli 2026)

Segmenten toen: TNdhKc = EB Engaged 30 Days (nu 100.964), TSVhx9 = EB Engaged 180 Days (nu leeg), TMaWCL = EB Engaged 90 Days (leeg), XYRq7Q = iedereen met e-mailtoestemming, S6kBRe = lijst "BFCM 2025" (41.970), Tgt2x2/UuABDJ = abandoned cart/checkout 30d. Vaste uitsluitingen: W3q7Zy bounces, XTpfNG spam, VSnBnJ afmelders, soms UfyDPs kopers 30d.

| Datum (UTC) | Mail | Publiek | Ontv. | Open | Klik | Orders | Omzet | $/ontv. | Uitschr. | Spam |
|---|---|---|---|---|---|---|---|---|---|---|
| ma 24 nov 08:12 | 48 Hours Left (tekst, James) | E180 excl UfyDPs | 12.920 | 52,4% | 1,51% | 34 | $6.876 | 0,53 | 1,24% | 0,016% |
| di 25 nov 17:00 | 10 Days 10% Off Ends Tonight | E30 + BFCM-lijst | 35.768 | 32,7% | 1,72% | 53 | $14.488 | 0,41 | 0,78% | 0,036% |
| wo 26 nov 08:11 | Staff Picks | iedereen (XYRq7Q) | 37.584 | 50,8% | 1,42% | 53 | $11.828 | 0,31 | 1,50% | 0,021% |
| do 27 nov 08:07 | Happy Thanksgiving | E30 | 27.378 | 61,8% | 0,99% | 33 | $6.509 | 0,24 | 1,31% | 0,048% |
| **vr 28 nov 08:03** | BF + 62% Off Sitewide | E180 + lijst | 30.704 | 40,0% | 2,84% | 86 | $18.059 | **0,59** | 0,73% | 0,124% |
| **vr 28 nov 13:03** | Highlight Bestsellers | E30 + lijst | 27.011 | 57,1% | 2,34% | 74 | $17.222 | **0,64** | 0,95% | 0,119% |
| **vr 28 nov 18:06** | Plain text reminder "Don't let this burn" | E90 + lijst | 28.491 | 60,9% | 1,83% | 84 | $18.507 | **0,65** | 1,09% | 0,060% |
| za 29 nov 10:02 | Sale Extension "Black Weekends" | E30 + lijst | 26.325 | 59,6% | 1,80% | 62 | $13.376 | 0,51 | 1,04% | 0,034% |
| za 29 nov 13:56 | Last Push Abandoned Orders | afhakers 30d | 12.069 | 57,1% | 1,53% | 60 | $9.286 | **0,77** | 1,21% | 0,050% |
| za 29 nov 17:02 | Bestsellers Top Trio | E30 + lijst | 28.479 | 56,7% | 1,79% | 63 | $12.321 | 0,43 | 1,09% | 0,049% |
| zo 30 nov 21:17 | 8 Hours Left (tekst) | E30 | 25.526 | 61,0% | 1,50% | 42 | $10.191 | 0,40 | 1,82% | 0,051% |
| ma 1 dec 08:15 | Cyber Monday AM 42% + 5% | E30 | 27.899 | 54,0% | 0,90% | 23 | $4.195 | 0,15 | 1,55% | 0,151% |
| ma 1 dec 17:02 | Cyber Monday PM | E30 | 20.799 | 58,2% | 0,99% | 28 | $5.284 | 0,25 | 0,91% | 0,029% |
| di 2 dec 10:14 | CM Resend "Ending Soon" | E30 | 29.591 | 54,6% | 1,13% | 51 | $10.506 | 0,36 | 1,25% | 0,085% |
| **Totaal** | 14 mails | | 370.544 | | | 746 | **$158.648** | 0,43 | | |

Lessen: (a) drie golven op BF-dag zelf hielden alle drie hun omzet per ontvanger ($0,59, $0,64, $0,65); de tekstmail 's avonds was de beste. (b) Zaterdag was bijna even goed als vrijdag, met de afhakers-push als uitschieter. (c) Cyber Monday leverde een kwart tot een derde van BF per ontvanger; de resend op dinsdag deed het beter dan de maandag zelf. (d) De bredere segmenten (180D, iedereen) scoorden niet slechter per ontvanger dan 30D, maar de lijst was toen 30 tot 40k; uitschrijvingen lagen op 1 tot 1,8 procent per send, veel hoger dan nu (0,3 tot 0,6). (e) Spam bleef overal onder 0,16 procent; de hoogste waarden zaten op de drukste dagen (BF 0,12, CM 0,15).

## 2. Deze BFCM-week tot nu toe (18 t/m 26 nov 2026)

Segmenten: VMjhb2 US Engaged 90D (115.118), TntB6g US Engaged 180D (131.248), RNuYDm US alle abonnees (148.922), XrFa5r INT Engaged 90D (57.761), S9BZVJ INT Engaged 180D (64.809), VdfJTJ INT alle (81.916), T3EWq6 US productkijkers 30d (47.649), VprSf5 US cart/checkout 30d (21.995), Xrxk9P US SMS engaged 180D (36.372), VJdd3C US SMS alle (37.400). Standaarduitsluitingen: UJY6LA wacht op order (8.636), Ur6Ehr onbetrokken 180 niet-kopers (31.004, US+INT), suppressies VSnBnJ W3q7Zy W4vNzF XTpfNG.

| Datum (lokaal) | Mail | Publiek | Ontv. | Open | Klik | Orders | Omzet | $/ontv. | Uitschr. | Spam |
|---|---|---|---|---|---|---|---|---|---|---|
| wo 18 nov 08:15 | HS Email 9 Before the Rush (Benjamin) | US VMjhb2 | 88.240 | 46,1% | 0,64% | 56 | $14.875 | 0,169 | 0,56% | 0,040% |
| wo 18 nov 08:15 | HS Email 9 INTL | INT XrFa5r | 48.820 | 50,3% | 0,79% | 25 | $5.667 | 0,116 | 0,51% | 0,002% |
| do 19 nov 12:00 | HS SMS 4 US | Xrxk9P | 23.148 | | 4,62% | 49 | $18.460 | **0,80** | 1,97% | |
| do 19 nov 12:00 | HS SMS 4 INTL | Y7wCYe | 3.850 | | 4,44% | 7 | $1.442 | 0,37 | 1,46% | |
| vr 20 nov 09:00 | Wij: Selling out before BF (A/B) | US VMjhb2 excl kopers 30d | 86.509 | 44,0% | 0,63% | 51 | $15.843 | 0,183 | 0,33% | 0,042% |
| za 21 nov 08:15 | HS Email 10 Gift Guide | US VMjhb2 | 96.653 | 43,4% | 0,75% | 77 | $18.744 | 0,194 | 0,51% | 0,032% |
| za 21 nov 08:15 | HS Email 10 INTL | INT XrFa5r | 53.651 | 51,3% | 0,73% | 41 | $10.060 | 0,188 | 0,49% | 0,011% |
| ma 23 nov 08:15 | HS Email 11 BF Week Is Here | **US RNuYDm** excl Ur6Ehr, TriYPe | 111.736 | 35,4% | 0,39% | 64 | $22.846 | 0,204 | 0,47% | 0,035% |
| ma 23 nov 08:15 | HS Email 11 INTL | **R5LmyU (INT SMS-abonnees, fout)** | 3.634 | 41,0% | 1,65% | 5 | $1.318 | 0,363 | 1,07% | 0,055% |
| ma 23 nov 11:00 | HS SMS 5 US | Xrxk9P | 23.283 | | 3,98% | 31 | $14.929 | 0,64 | 2,08% | |
| di 24 nov 17:00 ET | Wij: Most unique product (tekst) | US VMjhb2 excl kopers 30d, 12-pcs | 86.429 | 41,4% | 0,52% | 30 | $14.388 | 0,166 | 0,47% | 0,029% |
| wo 25 nov 10:00 | HS Email 13 Still Deciding | US T3EWq6 + VprSf5 | 37.332 | 30,6% | 0,81% | 27 | $9.582 | **0,257** | 0,44% | 0,029% |
| wo 25 nov 10:00 | HS Email 13 INTL | INT TvUeki + XrwgLh | 10.098 | 38,7% | 1,57% | 8 | $1.373 | 0,136 | 0,83% | 0,040% |
| do 26 nov 08:15 | Wij: Thanksgiving x BF (loopt nog, 1 tot 6 uur oud) | US VMjhb2 excl kopers 30d | 72.842 | 14,2% | 0,18% | 8 | $1.476 | 0,020 | 0,09% | 0,007% |
| do 26 nov 08:15 | Wij: As seen in Bon Appétit (loopt nog) | INT VdfJTJ excl kopers 30d, Ur6Ehr | 57.615 | 23,8% | 0,34% | 8 | $2.199 | 0,038 | 0,25% | 0,007% |
| **E-mail 18 t/m 25 nov** | 10 mails | | 623.102 | | | 384 | **$114.696** | 0,184 | | |
| **SMS 18 t/m 25 nov** | 3 sms | | 50.281 | | | 87 | **$34.831** | 0,69 | ~2% | |

Vaststellingen:
- De lijst is 3,5 keer zo groot als vorig jaar, de omzet per ontvanger is ongeveer een derde ($0,18 tegen $0,45 in dezelfde week vorig jaar). In totaal doet e-mail wel meer: $115k in 8 dagen tegen $56k vorig jaar (24 t/m 27 nov plus de dagen ervoor).
- De omzet per ontvanger van US 90D-sends ligt stabiel op $0,17 tot $0,19, ongeacht afzender of vorm (HS beeldmail, onze tekstmail, A/B). Kijkers plus afhakers (Email 13) doen $0,26.
- SMS doet $0,64 tot $0,80 per ontvanger, 3,5 keer e-mail, maar kost 2 procent van de SMS-lijst per send.
- Onze Thanksgiving-mail van vanochtend had 72.842 ontvangers op een publiek van ~94.600: Smart Sending (16 uur) sloeg ~22k mensen over die in de voorgaande 16 uur een flowmail kregen.

## 3. Tiers: 90D tegenover 180D tegenover alles

Definities (uit de segmenten): "Engaged 90D/180D" = toestemming e-mail, US-land, en in de laatste 90/180 dagen minstens één Active on Site, Opened Email (inclusief Apple-proxy-opens) of Clicked Email. Ur6Ehr = ingeschreven, 0 Active on Site, 0 menselijke opens, 0 kliks en 0 orders in 180 dagen. RNuYDm min Ur6Ehr is dus bijna exact TntB6g plus een paar duizend onbetrokken kopers.

| Tier (US) | Omvang | Bewijs deze week | Open | Klik | $/ontv. | Uitschr. | Spam |
|---|---|---|---|---|---|---|---|
| 90D (VMjhb2) na uitsluitingen | 86k tot 97k | 5 sends 18 t/m 24 nov | 41 tot 46% | 0,52 tot 0,75% | 0,166 tot 0,194 | 0,33 tot 0,56% | 0,029 tot 0,042% |
| Staart 90D naar 180D (~24k) | ~24k | afgeleid uit Email 11 (111.736) min een 90D-send van ~88k op 44% open, 0,64% klik | **~3%** | **~0%** | **~$0** | onbekend, lijkt niet hoger | niet hoger |
| 180D (TntB6g) na uitsluitingen = Email 11-publiek | ~112k | Email 11 (23 nov) | 35,4% | 0,39% | 0,204 (launch-dag van de $649-deal) | 0,47% | 0,035% |
| Alles (RNuYDm) zonder Ur6Ehr-uitsluiting | ~128k | geen send deze maand; 1 nov hele US-lijst (dag 1): $0,027, spam 0,011% | | | | | |

Interpretatie: de 24k mensen die wel in 180D maar niet in 90D zitten openden Email 11 nauwelijks en klikten vrijwel niet; de hoge omzet per ontvanger van Email 11 kwam uit de kern en uit de deal. Eén observatie, met inhoudsverschil, dus geen hard bewijs, maar vorig jaar zagen we hetzelfde patroon in de resend-data (INT-onderzoek 1 nov: $/ontvanger daalt sterk buiten E90). Deliverability-verschil tussen 90D en 180D: geen. De staart kost dus alleen mails, en mails zijn nu het schaarse goed. INT: XrFa5r (90D, 49 tot 54k ontvangers) deed $0,12 tot $0,19; de hele INT-lijst vandaag $0,04 (zachte mail, loopt nog); S9BZVJ 180D is 7k groter dan XrFa5r.

**Advies:** TntB6g/S9BZVJ alleen voor Email 15 (de BF-aankondiging met de sterkste deal, één kans om de staart te wekken, zoals de 180D-ochtendmail vorig jaar). Alle andere golven VMjhb2/XrFa5r. RNuYDm/VdfJTJ nergens; het voegt niets toe boven TntB6g zodra Ur6Ehr is uitgesloten, en zonder Ur6Ehr-uitsluiting voeg je 16k US-profielen toe die in 180 dagen niets deden (op 1 nov: $0,03 per ontvanger).

## 4. Deliverability

- Spam deze week: US 0,029 tot 0,042 procent, INT 0,002 tot 0,055 procent. Grens Gmail 0,3 procent, onze stopregel (Floris, INT-plan) 0,3 procent vanaf 1.000 ontvangers. Hoogste ooit in BFCM vorig jaar: 0,15 procent (CM-ochtend). Geen enkele send komt in de buurt.
- Uitschrijf: US 0,33 tot 0,56 procent per e-mail, INT 0,25 tot 0,83 procent. Bij 3 e-mails op vrijdag naar ~90k verlies je ~0,5 procent x 3 = ~1.300 US-abonnees op één dag (vorig jaar 2,8 procent op BF). Acceptabel voor BF, maar niet drie dagen op rij.
- Hele lijst op vrijdag: niet riskant voor spam (Email 11 bewijst het), wel zinloos qua omzet en duur qua volume. Als Ur6Ehr wél meegaat (16k US die 180 dagen niets deden, veel Alia-giveaway-instroom) stijgt het risico wel: dat zijn precies de adressen die bounces en klachten geven.
- Koude staart in de sends van deze week: nul. Alle US-campagnes gingen naar VMjhb2, behalve Email 11 (RNuYDm min Ur6Ehr, waarvan ~24k buiten VMjhb2) en Email 13 (gedragssegment). De uitsluiting Ur6Ehr stond op alle HS-sends van deze week behalve Email 10 en 13.
- SMS: 2 procent uitschrijf per send is hoog; 4 SMS in 4 dagen zou ~8 procent van de SMS-lijst kosten. SMS-smart-sending staat ook aan op SMS 6 (geen probleem voor SMS 6 zelf, wel als SMS 7 binnen 16 uur volgt).

## 5. Budget (e-mailplafond)

- Teller: 2.022.321 van 2.900.000 (as of 26 nov 14:46 UTC), periode 7 nov 22:06 tot 7 dec 22:06 UTC. Controle: Received Email 8 nov t/m 26 nov 14:30 UTC telt ~2,01M, dus de teller loopt bijna live mee en bevat de sends van vanochtend al grotendeels. Rest van vandaag (staart US-send, flows): ~30k. **Beschikbaar 27 nov t/m 7 dec: ~845k.**
- Flows: 17 t/m 25 nov gemiddeld 17.400 mails per dag zonder campagnes (dagen zonder campagne: 19 nov 18.043, 22 nov 20.773). 27 nov t/m 7 dec = 11 dagen x ~18k = **~200k**. Blijft over voor campagnes: **~645k.**
- SMS-krediet: $1.785 van $2.610 gebruikt; ~$825 over, dat is ongeveer 1 tot 1,5 US-golf van 37k (3 US-golven plus INT kostten ~$1.700 sinds 7 nov).

Geschatte ontvangers per golf (na standaarduitsluitingen): RNuYDm min Ur6Ehr ~118k, TntB6g ~115k, VMjhb2 ~88k; VdfJTJ min Ur6Ehr ~65k, S9BZVJ ~62k, XrFa5r ~52k. US kopers all-time in VMjhb2 ~40k (schatting), afhakers+kijkers 30d (T3EWq6+VprSf5) ~37k.

| Scenario | Vr 27 | Za 28 | Zo 29 | Ma 30 | 1 t/m 7 dec | Flows | Totaal | Tegen 845k |
|---|---|---|---|---|---|---|---|---|
| HS-plan zoals het staat (E15 hele lijst, E16/E17 180D, resend E4 hele lijst, E19 hele lijst) | 183+177+177 = 537k | 183k | 0 | 183k | 0 | 200k | **1.103k** | +258k |
| Idem maar alles 180D | 531k | 177k | 0 | 177k | 0 | 200k | 1.085k | +240k |
| Alles 90D (HS-plan, 3 golven vr) | 420k | 140k | 0 | 140k | 0 | 200k | 900k | +55k |
| Advies hieronder (E15 180D, rest 90D, resend alleen niet-openers, plus M1 t/m M4, zo optioneel) | 177+140+140+40 = 497k | 95+37 = 132k | 0 (optie 88k) | 140+40 = 180k | 70+88 = 158k | 200k | **1.167k** | +322k |
| Minimum dat past zonder upgrade | 3 x 90D = 420k | niet-openers 95k | 0 | 90D 140k | niets | 200k | 855k | +10k |

Conclusie: zonder planverhoging kan alleen "3 golven 90D op vrijdag, een niet-openers-resend zaterdag en één golf Cyber Monday" en verder niets (geen M1 t/m M4, geen laatste-dag-push, en de flows komen in de laatste dagen in gevaar). **Verhoog het plan vóór vrijdagochtend naar 3,5M (advies) of minstens 3,2M.** Klaviyo rekent anders overage of, als "automatically upgrade" uitstaat, stopt het met verzenden zodra de 2,9M bereikt is; dat zou midden in het BF-weekend zijn (rond zaterdagmiddag bij het HS-plan). Verhoog ook het SMS-krediet als SMS 6 en 8 beide moeten doorgaan.

## 6. Advies per resterende verzending

Alle sends: Smart Sending UIT op 27 en 30 nov; uitsluiten altijd UJY6LA, Ur6Ehr, VSnBnJ, W3q7Zy, W4vNzF, XTpfNG en de andere markt (VdfJTJ bij US, RNuYDm bij INT). Verwachte omzet = ontvangers x waargenomen $/ontvanger met BF-opslag (1,5 tot 2x op vrijdag, 1,2 tot 1,5x op zaterdag, 1x op maandag, zoals vorig jaar).

| Send | Advies publiek (include) | Extra uitsluitingen | Tijd (lokaal) | Ontv. | Verwacht $/ontv. | Verwachte omzet | Waarom |
|---|---|---|---|---|---|---|---|
| **Vr 27 · Email 15** BF Up to 70% Off | US **TntB6g** (niet RNuYDm); INT **S9BZVJ** (niet VdfJTJ) | TriYPe (kopers 14d), TCQLcv (12-pcs-kopers; de deal is de set) | 08:00 | 115k + 62k | US 0,30 tot 0,40; INT 0,15 tot 0,25 | $35k tot $46k US, $9k tot $16k INT | Eén brede golf met de sterkste deal is de enige kans om de 90-180D-staart te wekken (vorig jaar 180D-ochtendmail $0,59). RNuYDm voegt boven TntB6g niets toe als Ur6Ehr is uitgesloten. HS sluit nu geen enkele koper uit: kopers van 14 dagen krijgen anders een "koop de set" op een set die ze net kochten. |
| **Vr 27 · SMS 6 US** | **VJdd3C** (zoals gepland) | W92553 (3d), UJY6LA, SLVWps, TCQLcv | 09:00 | ~34k | 0,65 tot 0,85 | $22k tot $29k | VJdd3C en Xrxk9P overlappen voor 97 procent; SMS 4 en 5 deden $0,64 en $0,80. Houd SMS 7 (zaterdag) achterwege: 2 procent uitschrijf per SMS en $825 krediet. |
| **Vr 27 · SMS 6 INTL** | R5LmyU | zoals gepland | 13:00 | ~5k | 0,35 | $1,5k tot $2k | SMS 4 INTL deed $0,37. |
| **Vr 27 · Onze M1** kopers BF (12-Pcs + Pizza Steel) | US kopers all-time **binnen VMjhb2** (engaged kopers) | TCQLcv, 6-Pcs-bezitters, UfyDPs/WFqvwp (30d), UJY6LA | 10:00 ET | ~40k | 0,25 tot 0,40 | $10k tot $16k | Kopers converteren beter op de set, maar krijgen dan 4 mails op één dag: daarom alleen engaged kopers en liefst als vervanging van Email 16 voor deze groep (sluit all-time kopers uit van E16 US). |
| **Vr 27 · Email 16** Bestsellers | US **VMjhb2**; INT **XrFa5r** | W92553, UJY6LA, kopers all-time als M1 doorgaat | 13:00 | 88k + 52k | US 0,30 tot 0,40; INT 0,15 tot 0,25 | $26k tot $35k US, $8k tot $13k INT | Tweede golf vorig jaar $0,64 op 30D. De 90-180D-staart heeft om 08:00 al zijn kans gehad; 24k+10k mails besparen. Smart Sending UIT, anders gaat deze mail naar bijna niemand. |
| **Vr 27 · Email 17** A Note Before BF (tekst, Benjamin) | US **VMjhb2**; INT **XrFa5r** | W92553, UJY6LA | 18:00 | 88k + 52k | US 0,30 tot 0,40 | $26k tot $35k US, $8k tot $13k INT | Vorig jaar was de avondtekstmail de beste golf van BF ($0,65, 60,9 procent open). Smart Sending UIT. |
| **Za 28 · Resend E4** (HS, nu RNuYDm/VdfJTJ) | **Niet-openers van Email 15 en 16 binnen VMjhb2 / XrFa5r** (nieuw segment: Received Email 15, 0 menselijke opens, 0 kliks, geen order sinds 27 nov). Geen segment mogelijk: VMjhb2/XrFa5r met Smart Sending AAN | TriYPe, UJY6LA | 10:00 | ~55k + 35k (zonder segment 88k + 52k) | 0,20 tot 0,30 | $11k tot $17k US | Een resend naar de hele lijst kost 183k mails; vorig jaar deed de zaterdag-extension $0,51 op 30D. Niet-openers geven dezelfde incrementele omzet voor de helft van de mails. |
| **Za 28 · Onze M2** afhakers (Benjamin, kort) | US **VprSf5 + T3EWq6** (zoals Email 13) | UfyDPs/WFqvwp, UJY6LA, TCQLcv | 14:00 ET | ~37k | 0,35 tot 0,50 | $13k tot $18k | Vorig jaar de beste send van het weekend ($0,77, afhakers 30d); dit jaar deed Email 13 naar hetzelfde publiek $0,257 op een woensdag. |
| **Zo 29 · optioneel** "Last 36 hours of Black Friday prices" | US **VMjhb2** | TriYPe, UJY6LA | 17:00 | 88k | 0,20 tot 0,30 | $18k tot $26k | Vorig jaar zondag $0,40. Alleen doen als het plan is verhoogd en als de sale echt op 30 nov eindigt; anders overslaan en de mails bewaren voor 5 dec. |
| **Ma 30 · Email 19** Cyber Monday (HS, nu RNuYDm/VdfJTJ) | US **VMjhb2**; INT **XrFa5r** | TriYPe, UJY6LA | 08:00 | 88k + 52k | US 0,18 tot 0,25; INT 0,10 tot 0,18 | $16k tot $22k US, $5k tot $9k INT | Cyber Monday was vorig jaar $0,15 tot $0,25; de hele lijst (183k) kost 43k extra mails voor ~$0. "Final Day of the Sale" alleen als 30 nov echt de einddatum is. |
| **Ma 30 · SMS 8 US** Last Day for These Prices | **VJdd3C** | W92553, UJY6LA, SLVWps | 12:00 | ~34k | 0,50 tot 0,70 | $17k tot $24k | Tweede en laatste SMS van het weekend; krediet controleren. SMS 7 en 9 schrappen. |
| **Ma 30 · Onze M3** kopers CM | US kopers all-time binnen VMjhb2 | TCQLcv, 6-Pcs, UfyDPs/WFqvwp, UJY6LA | 10:00 ET | ~40k | 0,20 tot 0,30 | $8k tot $12k | Variant A/B volgens brief; kopers alleen als M1 niet al op vrijdag ging, anders alleen niet-openers van M1. |
| **Di 1 t/m do 3 dec** | geen campagnes, alleen flows | | | ~18k/dag | | | Lijst laten rusten na 7 sends in 4 dagen; mails sparen voor de echte einddatum. |
| **Vr 4 dec · Onze M4** "24 hours left" | US **Engaged 30D** (bestaand EB TNdhKc gefilterd op US, of VMjhb2 met Active on Site 30d) + **VprSf5 + T3EWq6** | TriYPe, UJY6LA | 18:00 ET | ~70k | 0,25 tot 0,35 | $17k tot $25k | Alleen als de sale tot 5 dec loopt. Vorig jaar "8 Hours Left" (tekst) $0,40 op 30D. |
| **Za 5 dec · laatste dag** tekstmail Benjamin "ends tonight" | US **VMjhb2**; INT **XrFa5r** | TriYPe, UJY6LA | 10:00 lokaal, SMS 9 om 17:00 als krediet er is | 88k + 52k | 0,20 tot 0,30 | $18k tot $26k US | Laatste-dag-mails hielden vorig jaar $0,36 tot $0,40. |

Totaal advies (zonder zondag): ~1,05M mails, verwachte e-mailomzet 27 nov t/m 5 dec $230k tot $330k plus SMS $40k tot $55k. Ter vergelijking: vorig jaar 24 nov t/m 2 dec $159k e-mail.

## 7. Wat te veranderen in Klaviyo (checklist, niets door mij gedaan)

1. Settings > Billing: e-mailplan voor deze cyclus verhogen naar 3,5M (of controleren dat auto-upgrade aanstaat); SMS-krediet verhogen als SMS 6 en 8 beide doorgaan.
2. Email 15 US: include RNuYDm vervangen door TntB6g; exclude TriYPe en TCQLcv toevoegen. Email 15 INTL: VdfJTJ vervangen door S9BZVJ; TriYPe toevoegen.
3. Email 16 en 17 US: include TntB6g vervangen door VMjhb2; INTL: S9BZVJ door XrFa5r.
4. Email 15, 16, 17, SMS 6 (en op 30 nov Email 19, SMS 8): Smart Sending uit.
5. Resend E4: include vervangen door niet-openers-segment (of VMjhb2/XrFa5r met Smart Sending aan). Email 19: RNuYDm/VdfJTJ vervangen door VMjhb2/XrFa5r.
6. SMS 7 (za) en SMS 9 (ma avond) niet inplannen.

## 8. Open vragen voor Floris (max 5)

1. **Einddatum**: eindigt de sale 30 nov (HS Email 19 "Final Day", SMS 8/9, codes) of 5 dec (Email 11-footer, M4 in de brief)? Dit bepaalt de copy van maandag en of er een 4/5 dec-push komt.
2. **Plan verhogen**: mag ik Homestead vragen (of doe jij het) het Klaviyo-e-mailplan vandaag naar 3,5M te zetten en SMS-krediet bij te kopen? Zonder dat past alleen het minimumscenario.
3. **Smart Sending uit** op Email 15/16/17 en SMS 6: doet Homestead dat of mogen wij de campagnes aanpassen? Nu krijgt bijna niemand Email 16 en 17.
4. **Email 11 INTL** ging op 23 nov naar R5LmyU (INT SMS-abonnees, 3.634) in plaats van VdfJTJ. Bewust? Zo nee: moet Email 15 INTL de 12-Pcs/BF-week-inhoud alsnog meenemen?
5. **Niet-openers-segmenten** voor de zaterdag-resend (2 segmenten, US en INT, via de API): akkoord dat wij die aanmaken (verder geen wijzigingen)?
