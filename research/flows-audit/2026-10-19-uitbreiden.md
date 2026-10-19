# Audit: bestaande flows uitbreiden en filters verbreden (19 okt 2026)

Vraag Floris: welke bestaande flows kunnen we uitbreiden, of welke segmenten en filters kunnen ruimer, zodat er meer omzet uit komt? Ontbrekende flows staan in `2026-10-19-ontbrekende-flows.md` (andere agent) en worden hier niet herhaald; waar dat stuk iets al dekt, verwijs ik ernaar.

Alleen gelezen. Klaviyo-API (account TdtTzz, revision 2025-10-15): definities van alle 19 live flows plus concept QNZyEb, flow-values-reports per bericht, metric-aggregates per trigger, en per profiel alle events van 15 sep tot 19 okt voor een steekproef van 1.945 profielen (instap op 13 en 14 okt). Niets gewijzigd in Klaviyo, Shopify of andere tools. Ruwe data en scripts staan in de scratchpad van deze sessie (`uitbr/`), niet in de repo.

**Meetvenster.** De v4-flows staan live sinds 8 okt 22:29 UTC. Van de gevraagde 14 dagen hebben er dus maar 10 v4-data: alle cijfers hieronder zijn **9 okt 00:00 tot 19 okt 00:00 UTC (10 dagen)**, per maand = x3. Omzet = Klaviyo-toeschrijving op Placed Order (5 dagen klik, 1 dag open). Aantallen per bericht zijn klein: alles onder ~10 orders is een richting, geen bewijs.

---

## 0. Samenvatting voor Floris

1. **De meeste flows halen al bijna iedereen die ze kunnen halen.** Checkout (99% van de echte, niet-kopende verlaters met e-mail krijgt C1), cart, welcome (82%, de rest kocht al), post-purchase (96%) en levering (79%, de rest had geen pan in de zending). Daar valt met filters weinig te winnen.
2. **Browse is de uitzondering, maar anders dan gedacht.** v4 Browse bereikt 27% van de bekijkers (257 eerste mails per dag van 940). De grootste snijder is het filter "geen welcome-mail in 7 dagen": **30% van alle bekijkers**. Maar 91% daarvan schreef zich dezelfde dag in via de Alia-pop-up en kreeg W1 net binnen. Het bereikverschil met de oude browseflow (520 per dag) is dus bijna helemaal "geen tweede mail op inschrijfdag", en dat is bewust. Wel te winnen: het filter van 7 naar 1 dag, herinstap van 7 naar 4 dagen, de 10%-controle-arm uit, en een tweede mail voor accessoirekijkers.
3. **Delivered Shipment vuurt maar voor 40% van de orders** (US 39%, CA 5%, SG en AE 0%, AU 75%, UK 100%). Daardoor krijgt 60% van de kopers nooit een reviewverzoek (XzHrez) en nooit U1, en het buitenland bijna niemand. Een vangnet op Fulfilled Order verdubbelt het bereik van het reviewverzoek.
4. **Herhaalkopers binnen 30 dagen missen P1-REPEAT** (de sterkste naflowmail, $4.16 per ontvanger) door de herinstap van 30 dagen in post-purchase. Nu nog weinig (de eerste order lag vaak vóór de livegang), vanaf begin november ~12% van alle orders, en in BFCM meer.
5. **Failure to launch: 6 van de 10 mails leveren $0 op** (31.467 mails in 10 dagen, alle omzet zit in 4 mails). Inkorten scheelt ~60% volume en ~230 uitschrijvingen per maand vóór BFCM, zonder omzetverlies.
6. **Markten**: geen enkele flow sluit buitenland uit. Wel: W4 stuurt 57% van de W4-INT-ontvangers die versie omdat hun land onbekend is (Alia-inschrijvingen hebben geen locatie), en de leveringsflows missen het buitenland door punt 3.
7. **Uitgesloten en ongeëngageerd**: flows sluiten niemand uit op betrokkenheid. De sunset (TbYQmX) heeft geen onderdrukkingsstap (segment bestaat niet), dus er wordt niemand onderdrukt. Homestead-campagnes gebruiken "Engaged 180 days" (128.092) en sluiten "Welcome protection" niet uit. Niet te streng; advies: geen extra onderdrukking vóór Cyber Monday.
8. **SMS**: er zijn SMS-events (19.960 verzonden SMS in 10 dagen, 4 campagnes, 953 nieuwe SMS-inschrijvers), maar geen enkele flow stuurt SMS. Zie de andere audit (4.2).

**Top 10 samen: ongeveer $5.000 tot $8.300 extra per maand**, de meeste stappen zijn één getal of één filter in de UI. Sectie 4.

---

## 1. Per flow: huidig bereik tegenover mogelijk bereik

### 1.1 Overzicht

Trigger = unieke profielen met het triggerevent per dag (metric-aggregates). Eerste mail = ontvangers van de eerste mail per dag (flow-values-report, alle armen). Snijders = steekproef van echte instappers op 13 en 14 okt, waarbij per profiel de eerste reden telt waarom er geen mail kwam.

| Flow | Trigger per dag | Eerste mail per dag | Bereik | Grootste snijders (steekproef) | Ruimte |
|---|---|---|---|---|---|
| Checkout QUBUQV | 316 | 103 (C1 84, Old 19) | 33% | 52% kocht binnen 10 min; 16% hard bounce (bots, onderdrukt); 7% checkout van $0 (gratis e-book, triggerfilter); 2% storebot; 2% geen e-mailadres; herinstap 0,3% | geen: 99% van de echte verlaters met e-mail krijgt C1 |
| Cart TZG9Mx | 259 | 138 (K1 94, K1-ACC 11, Old 32) | 53% | 25% kocht binnen 15 min; 14% ging door naar checkout (checkoutflow neemt over); 3,5% herinstap 14 d; 3% gratis gift | klein: herinstap naar 7 d geeft maar +0,4% |
| Browse WdRz5k | 940 | 257 (B1 156, B1-ACC 35, Old 67) | 27% | **30% welcome-mail in 7 d**; **16% herinstap 7 d**; 15% cart of checkout binnen 1 uur; 8% kocht binnen 1 uur; 5% uitgeschreven | **ja**, zie 1.2 |
| Site VLGhbR | 1.100 | 117 (A1) | 11% | 64% bekeek binnen 2 uur een product (browse neemt over); 9% klant in 30 d; 6% kocht; 5% welcome-mail in 10 d | geen: de filters doen wat ze moeten |
| Welcome T4a5Mk | 738 (lijst Uw8eZG) | 602 (W1 304, Old W1 296, W0 3) | 82% | 14% kocht binnen 5 min; 2% bounce; 1% cart/checkoutmail | geen. Alia-inschrijvers: 92% bereik |
| Post-purchase X3ySuU | 200 (orders) | 191 (P1-FIRST 166, P1-REPEAT 25) | 96% | herinstap 30 d (nu 3%, straks ~12%) | **ja**, zie 1.4 |
| Levering VQ93sx | 104 (Delivered Shipment) | 82 (P2) | 79% van leveringen, **~32% van orders** | 10% zending zonder pan; 4% uitgeschreven; 3% al P2-SAFE | via P2-SAFE al gedekt |
| UGC VPixnJ | 104 | ~60 (U1) | 55% van leveringen | 19% meer dan 1 order ooit; 7% ticket of niet volledig fulfilled; 6% geen kookgerei | geen omzet ($0), laten |
| Review XzHrez | 104 | start 20 okt (14 d wachten) | ~40% van orders | geen Delivered Shipment bij 60% van de orders | **ja**, zie 1.5 |
| Failure to launch T2SmtR | lijst + 30 d (alleen oude welcome-arm) | 3.147 mails per dag (10 mails) | | split na 30 d sluit nieuwe welcome-arm uit (W2 ontvangen in 60 d) | **inkorten**, zie 2 |
| Sunset TbYQmX | segment WuHSm6, 79.928 | 528 (S1) | | alleen nieuwe segmentleden starten | laten tot na BFCM |
| Winback UEfh4h (oud) | orders van vóór 9 okt + 60 d | 155 (mail 1) | | filters "order na 9 okt" en "geen v4-winback" | loopt tot 14 dec, laten |
| E-guide YyaMjx | 200 | 175 | 87% | geen | laten tot P1-link bevestigd |
| BIS WsQDYu | 5 | 6 | | | klein |
| VIP VTkxFL, Winback UyFc78, Anniversary XbYT7T | | 0 (eerste mails 8 nov, 23 nov, april) | | VIP: precies 2 orders ooit | VIP verbreden, zie 1.6 |
| Browse TP QNZyEb (concept) | 157 TP-only bekijkers | 0 | | | andere audit G2: van de steekproef zou 52% alle filters halen, ~80 per dag |

### 1.2 Browse WdRz5k: welke filters snijden

Flowfilters nu: Added to Cart, Checkout Started, Placed Order 0 sinds start; Received Email uit TZG9Mx, QUBUQV en **T4a5Mk 0 keer in 7 dagen**; niet in deze flow in 7 dagen (herinstap 7 d); 90/10-split, wacht 1 uur.

Steekproef 300 bekijkers. Na aftrek van kopers, doorstromers naar cart/checkout en wie geen toestemming heeft blijven er 209 over (70% van alle bekijkers = het **mogelijke bereik, ~660 per dag**). Daarvan kregen er 63 een mail (~200 per dag).

| Reden geen mail (van 146) | Aantal | Detail |
|---|---|---|
| Welcome-mail in 7 d | 107 | 97 kregen hun laatste welcome-mail dezelfde dag; 91 schreven zich dezelfde dag in. Arm: 58 oud, 49 nieuw. Maar **10** hadden hun laatste welcome-mail 1 tot 3 dagen eerder |
| Herinstap 7 d (vorige bekijking) | 32 (16% van alle bekijkers, inclusief overlap) | eerste bekijking in het venster: 1 d 11, 2 d 8, 3 d 11, 4 d 6, 5 d 6, 6 d 5 |
| Cart- of checkoutmail in 7 d | 2 | |
| Onverklaard | 5 | |

Conclusie: de oude Wj6x6V stuurde ~520 per dag omdat hij geen welcome-filter had (wel herinstap 30 d). Het hele verschil met v4 (~260 per dag) zit in mensen die op hun inschrijfdag W1 krijgen. Dat terugdraaien betekent twee mails op dag 0 bij de groep met de hoogste uitschrijving (W1 2,4%, data 02-advies: overlap welcome en browse 7,24% tegen 5,14% uitschrijving per week). **Niet doen.** Wel:

| Verbreding | Klaviyo-wijziging | Extra eerste mails | Extra $ per maand | Aanname |
|---|---|---|---|---|
| A. Welcome-filter 7 d naar 1 d | flowfilter "Received Email where Flow = v4 · Welcome zero times in the last **1** day" (was 7) | 10/300 x 950 = ~31 per dag | **~$600** | $1,28 per instromer (nieuwe arm sinds 12 okt) x 50% overlap-korting |
| B. Herinstap 7 d naar 4 d | Trigger-instellingen: re-entry 4 dagen; flowfilter "Has not been in this flow in the last **4** days" | 17/300 x 950 = ~54 per dag | **~$1.000** | idem $0,64. De flow is na 3 dagen klaar (B1 1 uur, B2 dag 2 om 09:00) |
| C. 90/10 naar 100% nieuw | split 119850685: Random sample **100%** | ~24 per dag naar de nieuwe arm | **~$490** | nieuw $1,28 tegen oud $0 (155 ontvangers, 0 orders) of historisch ~$0,60; verschil $0,68 |
| D. B2 voor B1-ACC-niet-klikkers | split 119850698, NEE-tak: nu einde; nieuwe mail "B2-NOTCLICKED · acc" (template B2-NOTCLICKED of een accessoireversie) na de bestaande wachttijd | ~33 per dag (B1-ACC 346 in 10 d, 4,4% klik) | **$400 tot $550** | B2-NOTCLICKED doet $0,56 per ontvanger, 75% incrementeel |

Het B1-moment (1 uur) laten staan: 15% gaat in dat uur naar cart of checkout en krijgt daar een sterkere mail.

### 1.3 Checkout QUBUQV en Cart TZG9Mx

Geen filter om te verbreden. De drop-off is gezond: kopers (52% en 25%), bots (16% hard bounce plus 2% storebot in checkout, sinds 10 okt grotendeels gefilterd) en doorstroom van cart naar checkout (14%). Herinstap cart 14 naar 7 dagen haalt 2 van 480 (0,4%): niet de moeite.

Wat wel speelt (sectie 2): C3 en K3 leveren in 10 dagen niets op. En de 90/10-armen: checkout oud $9,10 tegen nieuw $6,49 per instromer, cart oud $5,82 tegen nieuw $2,83, maar op 4 en 2 orders in de oude arm. Niet op 100% zetten zonder significante cijfers; checkout en cart houden hun 10% controle tot het testrapport.

### 1.4 Post-purchase X3ySuU: herhaalkopers binnen 30 dagen

Flowfilter "niet in deze flow in 30 dagen" plus herinstap 30 dagen. Wie binnen 30 dagen opnieuw bestelt, krijgt geen P1-REPEAT (en de P3 van de eerste order valt weg door "Placed Order 0 sinds start"). Steekproef orders 12 tot 18 okt: 48 van 378 (12,7%) hadden een eerdere order in de 30 dagen ervoor; nu kregen 38 van die 48 toch P1, omdat hun eerste order vóór de livegang lag. Vanaf ~8 november valt die buffer weg.

| Verbreding | Klaviyo-wijziging | Extra | Extra $ per maand | Aanname |
|---|---|---|---|---|
| E. Herinstap 30 naar 7 dagen | Trigger-instellingen re-entry **7 dagen**; flowfilter "Has not been in this flow in the last **7** days"; P2-SAFE (actie 119850554) extra verzendfilter "Received Email where Campaign Name contains P2 zero times in the last 30 days" | ~24 P1-REPEAT per dag | **$1.000 tot $3.000** (BFCM hoger) | P1-REPEAT meet $4,16 per ontvanger (245 ontvangers, 3 orders); gerekend met $1,50 tot $4,00 |

### 1.5 Review request XzHrez en de leveringsflows: Delivered Shipment ontbreekt bij 60%

Orders van 28 tot 30 sep, Delivered Shipment ontvangen tot 19 okt (19 tot 21 dagen later):

| Land | Met Delivered Shipment |
|---|---|
| US | 123 van 318 (39%) |
| AU | 42 van 56 (75%) |
| GB | 19 van 19 (100%) |
| CA | 1 van 21 (5%) |
| SG | 0 van 16 |
| AE | 0 van 10 |
| overig | 2 van 30 |
| **totaal** | **187 van 470 (40%)** |

P2 heeft een vangnet (P2-SAFE op dag 17 in X3ySuU). Het reviewverzoek en U1 hebben er geen. Fulfilled Order komt wel bij 63% van de orders (3.557 tegen 5.663 in 30 dagen).

| Verbreding | Klaviyo-wijziging | Extra | Extra $ per maand | Aanname |
|---|---|---|---|---|
| F. Vangnet reviewverzoek | Kloon van XzHrez als Draft: trigger **Fulfilled Order** (VtEiZT), wacht 21 dagen tot 09:30; flowfilters: Delivered Shipment zero times since starting this flow; Received Email where Flow = XzHrez zero times over all time; zelfde verzendfilters (geen ticket sinds start, geen refund 30 d). Zelfde A/B-templates | ~54 verzoeken per dag, ~1.600 per maand, vooral US en buitenland | **~$420** plus naar schatting 50 tot 80 extra reviews per maand | oude reviewflow $0,26 per ontvanger ($712 op 2.725) |

Het filter "nooit de 12-delige set" in XzHrez en VPixnJ komt uit de backorderperiode; DECISIONS (7 okt) zegt dat de set weer binnen een paar dagen levert. Weghalen kan, maar het gaat om weinig kopers en U1 doet $0. Klein, wel een besluit.

### 1.6 VIP VTkxFL: alleen precies de tweede order

Flowfilter "Placed Order equals 2 over all time" plus "nooit eerder in deze flow". Wie een derde of latere order plaatst en nooit VIP kreeg (iedereen met een tweede order vóór 9 okt), komt er nooit in. Steekproef kopers 9 tot 19 okt: 1 order 328, 2 orders 58, 3 of meer 24 (6%).

| Verbreding | Klaviyo-wijziging | Extra | Extra $ per maand | Aanname |
|---|---|---|---|---|
| G. VIP ook bij 3e+ order | flowfilter "Placed Order **is at least 2** over all time" (was equals 2); "has not been in this flow" blijft ooit | ~12 per dag | **~$360**, vanaf 8 nov | geen VIP-cijfers nog; $1,00 per ontvanger (tussen R2-VIP en P1-REPEAT, voorzichtig) |

### 1.7 Welcome T4a5Mk: W4-landsplit

Split 119850671: location.country is "United States" of "US", anders W4-INT. Van de W4-INT-ontvangers in de steekproef had **57% geen land** (33 van 58); geen van de bekeken profielen zonder land had een tijdzone. Van W4-ontvangers met een bekend land is 77% US. W4-INT stuurde 535 mails in 10 dagen (0 orders), W4-US 474 (1 order, $315).

| Verbreding | Klaviyo-wijziging | Extra $ per maand | Aanname |
|---|---|---|---|
| H. Onbekend land naar W4-US | split: OR "location.country is not set" in de JA-tak. W4-US is marktveilig gebouwd (prijzen en maten via de profielhelper, onbekend = geen bedragen); alleen de 12-delige kaart is US-only. Eerst een template-render op een profiel zonder land | **$250 tot $400** | ~300 per maand naar W4-US; verschil $0,30 tot $0,45 per ontvanger; lage zekerheid (1 order) |

### 1.8 Lijstgroei, onderdrukking en ongeëngageerden vóór BFCM

- **Instroom welcome**: lijst Uw8eZG kreeg 13.115 nieuwe profielen in oktober tot nu (690 per dag; september ~610). 88% via Alia ($source "Alia sign-up"), 12% via de Shopify-checkout (die kochten al en krijgen P1). Alia-inschrijvers halen 92% bereik. Geen lek.
- **Alia-profielen hebben geen locatie** bij inschrijving (77 van 77 bekeken zonder land en tijdzone). Dat raakt W4 (1.7) en elk marktblok in welcome: zonder land toont de mail geen prijzen.
- **Onderdrukking**: geen flow sluit uit op betrokkenheid. Sunset S2 heeft geen gevolg, want het segment "v4 · Sunset · suppressed" bestaat niet (audit 01, bevinding 8). WuHSm6 groeide van 75.425 naar 79.928. Steekproef 600 leden: 0 kopers, dus geen klanten in de sunset.
- **Campagnes** (Homestead): Engaged 180 days (128.092) of Engaged 90 (90.269), uitsluitingen Unsubscribe, Bounced, For Suppression (5.895), Spam, soms "Purchased in the last 14 days". "Welcome protection" (XdK77b, 7.777) wordt alleen in Floris' eigen campagnes uitgesloten. Dat is niet te streng.
- **Advies**: tot en met Cyber Monday geen extra onderdrukking en de suppressiestap niet bouwen; daarna (vanaf 7 dec) S2 plus suppressie aanzetten. Voor BFCM eventueel één campagne naar Engaged 180 tot 365 dagen zonder spamklacht, gedoseerd: dat is campagnewerk voor Homestead, geen flow.

---

## 2. Reeksen verlengen of inkorten (per bericht, 9 tot 19 okt)

RPR = omzet per ontvanger. Klik = unieke klik / afgeleverd.

| Flow | Bericht | Ontv. | Klik | Orders | Omzet | RPR | Uitschr. | Oordeel |
|---|---|---|---|---|---|---|---|---|
| Checkout | C1 | 840 | 8,3% | 17 | $3.826 | $4,55 | 1,0% | sterk (41% bounce vóór de botfilter van 10 okt) |
| | C2 | 285 | 5,6% | 7 | $1.670 | $5,86 | 1,4% | sterkst |
| | C2-ACC | 66 | 3,0% | 1 | $79 | $1,20 | 1,5% | |
| | C3-S / C3-P / C3-ACC | 67 / 114 / 48 | 1,5% / 1,8% / 0% | 0 | $0 | $0 | 0 tot 1,8% | **zwak**: 229 ontvangers, 0 orders |
| | CODE · C4 / C4 nocode | 93 / 82 | 3,3% / 0% | 2 / 0 | $691 / $0 | $7,42 / $0 | 0% / 1,2% | code wint (klein) |
| | Old · Checkout 3 (oude bonusmail) | 96 | 6,3% | 4 | $995 | $10,37 | 1,0% | sterkste oude mail |
| Cart | K1 | 942 | 3,3% | 9 | $2.663 | $2,83 | 0,8% | sterk |
| | K2-NEW / K2-RETURNING | 586 / 79 | 2,6% / 7,6% | 2 / 0 | $360 / $0 | $0,61 / $0 | 1,2% / 0% | |
| | CODE · K3 / K3 nocode (pan en acc) | 256 / 252 | 1,5% / 1,2% | 0 / 0 | $0 | $0 | 2,0% / 3,2% | **zwak**: 508 ontvangers, 0 orders, hoge uitschrijving |
| Browse | B1 (A/B) | 1.561 | 2,9% | 5 | $1.082 | $0,69 | 0,5% | |
| | B1-ACC | 346 | 4,4% | 4 | $337 | $0,97 | 1,2% | NEE-tak eindigt zonder mail |
| | B2-NOTCLICKED | 1.225 | 1,7% | 4 | $684 | $0,56 | 0,2% | laatste mail doet 80% van B1 |
| | B2-CLICKED (alle) | 29 | | 1 | $599 | | | te klein |
| | Old · Browse 1 | 667 | 2,0% | 0 | $0 | $0 | 1,7% | controle-arm |
| Welcome | W1 (A/B) | 3.041 | 3,6% | 29 | $8.614 | $2,83 | 2,4% | |
| | W2 | 2.108 | 1,7% | 6 | $1.243 | $0,59 | 2,2% | |
| | W3 | 1.561 | 1,0% | 1 | $96 | $0,06 | 1,4% | **zwak** |
| | W4-US / W4-INT | 474 / 535 | 0,4% / 1,7% | 1 / 0 | $315 / $0 | $0,66 / $0 | 1,1% / 0,8% | zie 1.7 |
| | W5 | 75 | | 0 | | | | te vroeg |
| | Old · Welcome 1 | 2.955 | 2,7% | 30 | $10.195 | $3,45 | 4,1% | |
| Site | A1 / A2 | 1.169 / 959 | 3,6% / 1,3% | 3 / 1 | $593 / $128 | $0,51 / $0,13 | 0,6% | A2 houden (lage uitschrijving) |
| Post-purchase | P1-FIRST / P1-REPEAT | 1.664 / 245 | 7,5% / 5,3% | 8 / 3 | $1.172 / $1.019 | $0,70 / $4,16 | 0,3% / 0% | P1-REPEAT sterk |
| Levering | P2 | 822 | 5,0% | 5 | $522 | $0,64 | 0,5% | |
| UGC | U1 | 381 | 0,8% | 0 | $0 | $0 | 0% | geen verkoopdoel |
| FTL | 10 mails | 31.467 | 0,15 tot 0,46% | 6 | $1.274 | $0,04 | 0,46% | **inkorten** |
| Winback oud | mail 1 t/m 3 | 4.938 | 0,2 tot 0,6% | 5 | $673 | $0,14 | 0,5% | tot 14 dec |
| BIS | 1 / 2 | 56 / 44 | 7,3% / 20,5% | 2 / 1 | $364 / $80 | | 2% | klein |

**Verlengen**

- **Browse, accessoiretak (D)**: B1-ACC-niet-klikkers krijgen nu niets meer; B2-NOTCLICKED haalt in de pantak $0,56. Zelfde wachttijd, één mail.
- **Browse, pantak**: B2-NOTCLICKED is met $0,56 bijna zo goed als B1. Een B3 is denkbaar, maar de andere audit stelt al een B1b voor (24 uur, niet-openers). Eerst die; niet beide.
- **Post-purchase**: ruimte zit in bereik (E), niet in een extra mail. P3 (dag 21) start pas rond 30 okt; de andere audit (4.8) stelt een dekselmail op dag 32 voor.
- **Welcome**: niet verlengen. W3 tot en met W5 zijn zwak of nog niet te meten; de data van timing/02 zeggen dat dag 10 tot 30 campagnewerk is, en nieuwe inschrijvers krijgen de Homestead-campagnes al.

**Inkorten of vervangen**

- **Failure to launch T2SmtR**: alle omzet in 10 dagen zat in 4 mails: Titanium vs Stainless Steel ($498), Titanium vs Non-Stick ($455), Micro-Plastic Free ($161), How to Store + Care ($160). De andere 6 (Bestsellers + Product Reviews, Healthy Habits Start Here, FAQ's, Titanium Care, Ceramic VS Titanium, Review Focus) deden $0 op ~18.500 mails en ~78 uitschrijvingen. Die 6 op Draft (profielen slaan ze over) scheelt ~55.000 mails en ~230 uitschrijvingen per maand. Let op: vanaf ~8 nov halveert FTL vanzelf (de nieuwe welcome-arm valt eruit). De claimbanners in de overgebleven 4 moeten er hoe dan ook uit (andere audit 4.14).
- **Checkout C3**: 0 orders op 229. De oude bonusmail op dag 3 deed $10,37 (4 orders op 96). Test: C3-P en C3-S vervangen door een gift- of bonusinhoud (zelfde moment), of C3 helemaal laten vallen en C4 een dag naar voren. Het gat uit audit 01 bevinding 6 (14% krijgt geen C3) is er nog; dat maakt pas uit als C3 iets oplevert.
- **Cart K3**: 0 orders op 508, uitschrijving 2 tot 3%. Na de BFCM-bevriezing herzien (K2 een dag later en K3 eruit, of K3 alleen voor K1-klikkers). Nu laten: de T02-meting loopt nog.
- **Welcome W3**: $0,06 en 1,4% uitschrijving. Kandidaat om te vervangen in fase 2 (7 dec), niet nu: W1-test loopt tot ~29 okt.

---

## 3. Risico's per wijziging

| # | Wijziging | Dubbele mail | Deliverability | Marge en kortinglek | BFCM-moeheid | Terugdraaien |
|---|---|---|---|---|---|---|
| A | Browse welcome-filter 7 naar 1 d | browse na dag 1 naast W2 tot W5; welcome slaat zelf geen browse over | +31 mails per dag, verwaarloosbaar | B1 noemt 10%; geen nieuwe code (cooldown) | in november krijgen nieuwe inschrijvers ook dagelijks campagnes: in BFCM terug naar 3 d overwegen | getal terug naar 7 |
| B | Browse herinstap 4 d | zelfde B1 ("10% off") opnieuw na 4 dagen | +54 per dag | CODE-cooldown 30 d voorkomt een tweede eigen code; wel vaker de welkomstcode | hoger: frequente kijkers krijgen elke 4 dagen B1 | getal terug naar 7 |
| C | Browse 100% nieuw | geen | geen | geen | geen | 90 terugzetten; T01-meting browse eindigt |
| D | B2 voor B1-ACC | geen (zelfde flow) | +33 per dag | template zonder code houden | laag | mail op Draft |
| E | Post-purchase herinstap 7 d | P2-SAFE kan twee keer komen zonder extra filter (staat in de wijziging); VIP start bij order 2 naast P1-REPEAT (bewust) | geen | P3 heeft een eigen code; cooldown geldt | in BFCM veel herhaalorders: meer P1-REPEAT, dat is gewenst | getallen terug naar 30 |
| F | Review-vangnet | filter "nooit XzHrez" voorkomt dubbel verzoek; check Trustpilot eigen uitnodigingen (PLAYBOOK 5, open punt) | +54 per dag | incentive "win your purchase back" kost geld per winnaar | laag (service) | kloon op Draft |
| G | VIP 3e+ order | VIP en winback R2-VIP kunnen in dezelfde maand vallen (V1 heeft filter "geen order 14 d") | +12 per dag | 15% eigen code voor trouwe klanten; in BFCM stapelt dat op 70% off als de code op de saleprijs werkt | V1 valt rond BFCM | filter terug naar equals 2 |
| H | W4 onbekend naar US | geen | geen | geen | geen | split terug |
| I | C3 vervangen (test) | geen | geen | een bonus- of giftmail mag geen nieuwe korting zijn | laag | template terug |
| J | FTL 6 mails op Draft | minder | **beter** (−55.000 mails per maand) | geen | **beter** | mails weer Live |

Algemeen voor BFCM (vanaf 1 nov, 70% off): alle codemails in flows (C4, K3, B2, P3, R2, V1, N2) stapelen mogelijk op de BFCM-prijs. Het plan (homestead/02) zet T02 in de bevriezing op 100% code; met 70% korting is "0% code" (alleen gifts) waarschijnlijk beter voor de marge. Dat is een apart besluit. Homestead wil tot 22 okt geen grote flowwijzigingen; A tot en met H zijn klein en kunnen 22 tot 24 okt, zodat er vóór 1 nov een week data is.

---

## 4. Top 10 (extra $ per maand x gemak)

Gemak: S = één getal of filter in de UI, M = extra mail, kloon of template. Alle bedragen zijn schattingen op 10 dagen data, met de aannames uit sectie 1.

| # | Wat | Exacte wijziging in Klaviyo | Extra $ per maand | Gemak | Floris keurt goed |
|---|---|---|---|---|---|
| 1 | **Post-purchase: herhaalkopers binnen 30 dagen krijgen P1-REPEAT** | X3ySuU: Trigger > Re-entry van 30 naar **7 dagen**; flowfilter "Has not been in this flow in the last 30 days" naar **7 days**; P2-SAFE (119850554) verzendfilter erbij: Received Email where Campaign Name contains "P2" zero times in the last 30 days | $1.000 tot $3.000 | S | herinstap 7 dagen; extra P2-SAFE-filter |
| 2 | **Browse: herinstap 7 naar 4 dagen** | WdRz5k: Trigger > Re-entry **4 dagen**; flowfilter "Has not been in this flow in the last **4** days" | ~$1.000 | S | B1 mag na 4 dagen opnieuw |
| 3 | **Browse: welcome-filter 7 naar 1 dag** | WdRz5k flowfilter: Received Email where Flow = v4 · Welcome zero times in the last **1** day (was 7). Zelfde in QNZyEb bij livegang | ~$600 | S | browse vanaf dag 1 naast de welcome |
| 4 | **Browse: 10%-controle-arm uit** | split 119850685: Random sample **100%** | ~$490 | S | einde T01 in browse (checkout, cart en welcome blijven) |
| 5 | **Browse: tweede mail voor accessoirekijkers** | WdRz5k, split 119850698 (B1-ACC geklikt?): in de NEE-tak een mail "B2-NOTCLICKED · acc" (kopie van template B2-NOTCLICKED, verzendfilter Placed Order en Added to Cart 0 sinds start) | $400 tot $550 | M | extra mail; welke inhoud (pan-reviews of accessoire) |
| 6 | **Reviewverzoek ook zonder Delivered Shipment** | kloon XzHrez als Draft: trigger Fulfilled Order (VtEiZT), wacht 21 dagen tot 09:30, flowfilters Delivered Shipment zero times since starting this flow en Received Email where Flow = XzHrez zero times over all time; verzendfilters zoals XzHrez | ~$420 + 50 tot 80 reviews | M | kloon bouwen (Claude via API als Draft), daarna live; Trustpilot-eigen uitnodigingen gecontroleerd |
| 7 | **VIP ook bij derde en latere order** | VTkxFL flowfilter: Placed Order **is at least 2** over all time (was equals 2) | ~$360 vanaf 8 nov | S | 15% VIP-code ook voor bestaande trouwe klanten |
| 8 | **W4: onbekend land naar W4-US** | T4a5Mk split 119850671: OR "location country is not set" toevoegen aan de US-voorwaarde; eerst template-render W4-US op een profiel zonder land (Claude, alleen lezen) | $250 tot $400 (lage zekerheid) | S | US-versie (met 12-delige kaart) voor onbekend land |
| 9 | **Checkout C3 vervangen door een bonus- of giftmail** | QUBUQV: C3-P en C3-S (acties 119850606, 119850603) template wisselen naar een nieuwe C3-bonus (inhoud zoals de oude dag-3-mail, zonder nieuwe korting) | $500 tot $1.500 (onzeker, 4 orders op 96 in de oude arm) | M | inhoud C3; past in fase 2 of nu als test |
| 10 | **Failure to launch: 6 nulmails op Draft** | T2SmtR: mails Bestsellers + Product Reviews, Healthy Habits, FAQ's, Titanium Care, Ceramic VS Titanium, Review Focus: Status **Draft** (flow blijft Live) | ~$0 omzet, −55.000 mails en −230 uitschrijvingen per maand | S | welke 4 blijven; samen met de banneropschoning (andere audit 4.14) |

**Optelsom 1 tot 9: ongeveer $5.000 tot $8.300 per maand** (zonder de indirecte waarde van reviews en minder uitschrijvingen). Voorzichtige ondergrens met alleen de S-stappen 1 tot 4, 7, 8 en 10: ~$3.700.

**Volgorde.** Week van 22 okt: 1, 2, 3, 4, 8 en 10 (alle S, samen ~10 minuten in de UI). Daarna 5 en 6 (Claude kan de kloon en het template als Draft klaarzetten na "ga"). 7 vóór 8 nov. 9 als test, of in fase 2 na BFCM. Na elke wijziging volgt Claude bereik, uitschrijving en bounce in de dagelijkse 90/10-bewaking; terugdraaien is overal hetzelfde getal of dezelfde status terug.

**Niet in deze lijst, wel gecontroleerd**: checkout- en cartfilters (al maximaal), site abandonment (filters doen wat ze moeten), cart-herinstap (+0,4%), welcome-bereik (82%, rest kocht al), UGC (geen omzet), 90/10 in checkout en cart (oude arm niet aantoonbaar slechter, laten tot het testrapport). Triple Pixel- en Elevar-vangnetten, SMS-flows, backfill voor VIP, anniversary en winback staan in de andere audit.

---

## 5. Werkwijze

- Flowdefinities: `GET /api/flows/{id}?additional-fields[flow]=definition` voor 19 live flows, QNZyEb en de oude Wj6x6V, TyEjuQ, SwkMyn ter vergelijking.
- Prestaties per bericht: `POST /api/flow-values-reports` (9 tot 19 okt, en 12 okt 10:00 tot 19 okt voor de 90/10-armen), conversion metric Placed Order.
- Triggers: `POST /api/metric-aggregates` (count en uniek, 9 tot 19 okt) voor alle triggermetrics, Received Email per $flow, Subscribed to List per lijst, SMS-metrics.
- Snijders: alle triggerevents van 13 en 14 okt (checkout 583, cart 480 profielen; browse, site, welcome elk 300 en browse-TP 200 steekproef; leveringen 348), per profiel alle events van 15 sep tot 19 okt (1.945 profielen) plus toestemming en orderhistorie. Per profiel getoetst tegen de live filters in de volgorde van de flow; de eerste reden telt.
- Delivered-dekking: alle orders van 28 tot 30 sep (470) tegen alle Delivered Shipment-events tot 19 okt, per verzendland.
- Beperkingen: Klaviyo logt geen overgeslagen flowstappen als event (Skipped Send is alleen campagnes), dus de snijders zijn nagespeeld, niet uitgelezen. Toestemming is de stand van 19 okt. Omzet is Klaviyo-toeschrijving; de welcome-analyse (v6-golive/20) laat zien dat toeschrijving de snelste mail bevoordeelt.
