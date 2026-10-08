# 01 · Segmenten-audit vóór livegang (13 v4-flows)

Datum: 8 oktober 2026, avond. Segment-auditor. Klaviyo account TdtTzz, alleen GET (revision 2025-10-15). Niets gewijzigd in Klaviyo, niets gecommit.

Bronnen: `GET /api/flows/{id}/?additional-fields[flow]=definition` voor alle 13 Draft-flows en alle 24 live flows, `GET /api/metrics`, `GET /api/segments/{id}` met `profile_count`, `GET /api/lists/Uw8eZG`, en steekproeven van events (Placed Order, Checkout Started, Added to Cart, Viewed Product, Delivered Shipment, Received Email, Clicked Email) om de logica op echte data te toetsen. De lokale JSON in `exports/live/flows/*.json` is vergeleken met wat live in Klaviyo staat: trigger, filters en mails zijn gelijk, behalve de A/B-variatienamen (zie bevinding 1).

Leeswijzer: "sinds start" = since starting this flow. "CODE-cooldown" = split "Received Email waarvan Campaign Name bevat `CODE ·`, minstens 1 keer in 30 dagen". Klaviyo zet bij flowmails de berichtnaam in `Campaign Name` en de flow-ID in `$flow` (gecontroleerd op live Clicked/Received Email-events, bijvoorbeeld `$flow: SiaNLu, Campaign Name: "EB [DG] | Email #3"`). Flowfilters worden bij elke stap opnieuw gecontroleerd.

---

## Samenvatting in één tabel

| # | Ernst | Bevinding | Flow |
|---|---|---|---|
| 1 | BLOKKEREND | Klik-split na B1 matcht nooit: Klaviyo hernoemde de A/B-variaties | Browse WdRz5k |
| 2 | BLOKKEREND | T2SmtR (Failure to launch) mist nog de T01-voorwaarde, en de voorwaarde uit GO-LIVE stap 8 zou alle huidige inschrijvers uitsluiten | Welcome T4a5Mk + T2SmtR |
| 3 | BLOKKEREND | Oude naflows (Pan Education, FREE E-GUIDE, E-Book) blijven volgens GO-LIVE live, volgens OVERZICHT-V5 uit; nu dubbele inhoud | Post-purchase, levering, UGC |
| 4 | BELANGRIJK | Browse en cart hebben geen post-purchase-uitsluiting: kopers krijgen dagen na hun order "Get this pan with 10% off" | Browse, Cart |
| 5 | BELANGRIJK | Delivered Shipment vuurt per zending, ook voor een gift-zending: P2, P2-SAFE en U1 op het verkeerde moment | Levering, UGC, Post-purchase |
| 6 | BELANGRIJK | 14% van de checkouts krijgt geen C3 (Deep Pan, Wok, Crêpe, Pizza Steel, Roasting, Pan Pro vanaf $300 zonder set) | Checkout |
| 7 | BELANGRIJK | Sunset start alleen voor nieuwe segmentleden: de 75.425 huidige leden komen er nooit in | Sunset |
| 8 | BELANGRIJK | Segmenten ontbreken: Sunset · suppressed, Welcome-bescherming, Campagne-cap | Sunset, campagnes |
| 9 | BELANGRIJK | Triple Pixel-flows uit = bereik weg (36% van de TP-cartprofielen heeft geen Shopify Added to Cart) | Cart, Checkout, Browse |
| 10 | BELANGRIJK | Wisselgat: wie vóór livegang bestelde krijgt geen winback meer (oude flow uit, nieuwe start alleen bij nieuwe orders) | Winback, Post-purchase |
| 11 | KLEIN | Welcome W4-landsplit: 15% van de inschrijvers na een week zonder land, valt in W4-INT | Welcome |
| 12 | KLEIN | Klik-splits tellen botklikken | Browse |
| 13 | KLEIN | Sunset S1 heeft geen verzendfilter | Sunset |
| 14 | KLEIN | Cooldown telt ontvangst, niet gebruik; oude-arm-codes tellen niet; VIP-cooldown telt ook HI10 | alle codeflows |
| 15 | KLEIN | Tweede order binnen 30 dagen: geen P1 en geen P3 | Post-purchase |
| 16 | KLEIN | Terugkerende klant met kookgerei in checkout krijgt geen C2 | Checkout |
| 17 | KLEIN | A/B-experimenten staan op draft; T04-rapportage op naam werkt niet meer | Welcome, Browse |
| 18 | KLEIN | Voorrang welcome boven browse, terwijl OVERZICHT-V5 browse boven welcome noemt | Browse, documentatie |
| 19 | KLEIN | Welcome-filter `email not-contains test@` sluit ook echte adressen uit | Welcome |

Details, bewijs en fix staan in sectie C.

---

## A. Per flow: zo werkt het (live definitie)

Alle 13 flows: status draft, alle mails draft, smart sending uit, niet transactioneel, tijdzone profiel, afzender "Siraat's Kitchen" (W2, S2, V2, S3, S4: "Benjamin at Siraat's Kitchen"), reply-to support@.

Gebruikte metrics (alle actief, laatste event 8 okt): Placed Order RSNxYV, Checkout Started RfMvni, Added to Cart QXcV8K (Shopify), Viewed Product XNtYMB, Active on Site UdCdLD, Delivered Shipment VcUF33, Fulfilled Order VtEiZT, Refunded Order Xg6cwn, Received Email YkRM4Q, Clicked Email W247h8, Opened Email WyrTym, Opened Ticket YzvjGf (Gorgias), Checkout Started - Triple Pixel RtgBgs (alleen in het oude cart-pad). Let op: er bestaan ook een tweede "Added to Cart" (SRYm9S, API, nooit een event) en een tweede "Active on Site" (TF6iAL, laatste event maart 2026). De flows gebruiken de juiste, actieve varianten.

Titellijsten (KOOK 54, SET 19, P2 48, PANPRO+STARTER 26, GROOT_SET 15, DEKSEL 7, SCHORT 4) gecontroleerd tegen de Items van 1.600 orders sinds 20 september: elke verkochte pan, set en schort valt in de juiste lijst; accessoires (plank, utensils, molens, deksel) vallen er terecht buiten.

### 1. Post-purchase X3ySuU
- **Trigger**: Placed Order (geen triggerfilter).
- **Flowfilter**: niet in deze flow in 30 dagen. Herinstap 30 dagen.
- **Mails**:
  - +1 uur: **P1-FIRST** (Placed Order = 1 all time) of **P1-REPEAT** (> 1).
  - dag 17, 09:00: **P2-SAFE** alleen als de order een pan of set bevat (P2-lijst, 17 dagen), er sinds start geen Delivered Shipment was en geen refund in 30 dagen.
  - dag 21, 09:00: split "Placed Order = 2 all time": JA = einde (VIP neemt het over). NEE: CODE-cooldown-split.
    - cooldown JA: P3-versie zonder code.
    - cooldown NEE: random 50% (T02): JA = `CODE · P3-*` (eigen 10%, 14 dagen), NEE = P3-versie zonder code (T02-B).
    - Binnen elke tak kiest een verzendfilter precies één P3: SET (set of order vanaf $300) > NEXT·deksel > PAN > ACCESSORY·kook; zonder kookgerei in de order: NEXT·eigenaar (had al kookgerei) > APRON > ACCESSORY·acc. Gift-card-only krijgt geen P3. Alle P3's: Placed Order 0 sinds start, geen refund in 30 dagen.

### 2. Post-purchase · levering VQ93sx
- **Trigger**: Delivered Shipment (Shopify), geen triggerfilter.
- **Flowfilter**: Placed Order met een P2-titel in 30 dagen · niet in deze flow in 30 dagen · geen mail "P2-SAFE" ontvangen in 30 dagen. Herinstap 30 dagen.
- **Mail**: de dag erna 09:00 **P2** "The mistake that makes titanium stick" (geen refund in 30 dagen).

### 3. Checkout abandonment QUBUQV
- **Trigger**: Checkout Started met `$value > 0`.
- **Flowfilter**: Placed Order 0 sinds start · niet in deze flow in 14 dagen · geen post-purchase-mail (X3ySuU) in 7 dagen. Herinstap 14 dagen.
- **Split T01**: random 50%.
  - **JA (v4)**: +30 min **C1** · +1 dag **C2** (kookgerei in checkout én nooit besteld) of **C2-ACC** (geen kookgerei) · +2 dagen 09:00 **C3-S** (grote set) / **C3-P** (Pan Pro of starterbundel, checkout < $300, geen grote set) / **C3-ACC** (geen kookgerei én nooit besteld) · +2 dagen 09:00 CODE-cooldown: JA = C4 nocode · NEE = random 50% (T02): **CODE · C4** (eigen 10%, 48 uur) of C4 nocode.
  - **NEE (oud pad)**: Old · Checkout 1 t/m 5 (10 min, 1 d 08:30, 1 d, 2 d, 1 d).
  - Elke mail: Placed Order 0 sinds start.

### 4. Cart abandonment TZG9Mx
- **Trigger**: Added to Cart met Price > 0 en Product Name bevat niet Mystery Gift, E-Book, Free Shipping, Giveaway (de vier gratis gifts, 1.418 van 1.600 orders hebben ze).
- **Flowfilter**: Checkout Started 0 sinds start · Placed Order 0 sinds start · geen checkout-mail (QUBUQV) in 7 dagen · niet in deze flow in 14 dagen. Herinstap 14 dagen.
- **Split T01**: random 50%.
  - **JA**: +30 min split "Added to Cart in 1 dag met Product Name bevat Hammer/Pan/Pot/ookware/Everything/fanne/Prep Bundle".
    - kookgerei: **K1** · +1 dag **K2-RETURNING** (ooit besteld) of **K2-NEW** · +2 dagen 09:00 CODE-cooldown: JA = K3 nocode · NEE = random 50%: **CODE · K3 · pan** of nocode.
    - anders: **K1-ACC** · +3 dagen 09:00 dezelfde K3-router (acc).
  - **NEE**: Old · Cart 1 t/m 3.
  - Elke v4-mail: Checkout Started 0 en Placed Order 0 sinds start. Getoetst op ATC-events sinds 4 okt: elke pan, set, wok, deep, crêpe, pizza steel valt in "kookgerei"; deksel, plank, utensils, molens in ACC. Gratis gifts starten de flow niet.

### 5. Welcome T4a5Mk
- **Trigger**: toegevoegd aan lijst Uw8eZG "Email List" (215.028 profielen).
- **Flowfilter**: email bevat niet `test@` · nooit eerder in deze flow.
- **Split T01**: random 50%.
  - **JA**: +20 min: besteld sinds start? JA = einde. NEE: ooit besteld? JA = **W0** (bestaande klant), NEE = **W1** A/B (T04, twee variaties 50/50, geen automatische winnaar) · +1 d 09:00 **W2** (Benjamin) · +2 d **W3** · +3 d split land (location.country = "United States" of "US"): **W4-US** of **W4-INT** · +4 d **W5**.
  - Elke v4-mail: Placed Order 0 sinds start · geen checkout-mail en geen cart-mail in de laatste 1 dag (mail wordt overgeslagen, de flow loopt door).
  - **NEE**: Old · Welcome 1 t/m 8 (zoals SiaNLu).

### 6. Browse abandonment WdRz5k
- **Trigger**: Viewed Product.
- **Flowfilter**: Added to Cart, Checkout Started, Placed Order elk 0 sinds start · geen cart-, checkout- of welcome-mail in 7 dagen · niet in deze flow in 7 dagen. Herinstap 7 dagen.
- **Split T01**: random 50%.
  - **JA**: +1 uur split "Viewed Product in 1 dag met Name bevat kookwoord".
    - kookgerei: **B1** A/B (T05a, onderwerp A/B) · +2 d 09:00 split "Clicked Email met Campaign Name bevat `B1 · T05a` sinds start" (**kapot, bevinding 1**): JA = CODE-cooldown en T02 naar **CODE · B2-CLICKED · pan** of nocode; NEE = **B2-NOTCLICKED**.
    - anders: **B1-ACC** · +2 d 09:00 split "geklikt op B1-ACC": JA = cooldown/T02 naar B2-CLICKED · acc; NEE = einde.
  - **NEE**: Old · Browse 1 (+10 min).
  - Elke mail: Placed Order 0 sinds start; B2: ook Added to Cart 0 sinds start.

### 7. VIP VTkxFL
- **Trigger**: Placed Order. **Flowfilter**: Placed Order = 2 all time (dus de tweede order; een derde order haalt iemand eruit) · nooit eerder in deze flow.
- dag 30, 09:00: split "CODE-mail in 30 d **en** Placed Order met `Discount Codes` niet leeg in 45 d": JA = **V1 nocode**, NEE = **CODE · V1** (15%, 14 dagen). Geen T02. Filter: geen refund sinds start, geen order in 14 dagen.
- +10 d 09:00: **V2** (Benjamin), Placed Order en refund 0 sinds start.

### 8. Winback UyFc78
- **Trigger**: Placed Order. Geen flowfilter, geen herinstapgrens: elke order start een nieuwe run, de oude stopt via "Placed Order 0 sinds start".
- dag 45, 09:00: één R1 via verzendfilters (alle met: geen post-purchase- of VIP-mail in 7 d): **R1-SET** (set of $300+) / **R1-PAN · kook** / **R1-PAN · eigenaar** (geen kookgerei in 46 d maar wel ooit) / **R1-ACC** (nooit kookgerei).
- dag 75, 09:00: Placed Order >= 2 all time? JA = R2-VIP-router (cooldown, T02, **CODE · R2-VIP** 15%) · NEE = R2-router (**CODE · R2** 10%).

### 9. Anniversary XbYT7T
- **Trigger**: Placed Order. **Flowfilter**: Placed Order = 1 all time · kookgerei ooit besteld (samen: eerste order met kookgerei) · nooit eerder in deze flow. Elke stap opnieuw: wie een tweede order plaatst valt eruit.
- dag 182, 09:00: **N1** (geen refund, geen VIP- of winback-mail in 14 d, geen Gorgias-ticket in 14 d).
- dag 365, 09:00: CODE-cooldown: JA = N2 nocode, NEE = **CODE · N2** (15%). Geen T02.

### 10. Site abandonment VLGhbR
- **Trigger**: Active on Site (UdCdLD).
- **Flowfilter**: Viewed Product, Added to Cart, Checkout Started, Placed Order elk 0 sinds start · geen order in 30 d · geen browse-, cart-, checkout- of post-purchase-mail in 7 d · geen welcome-mail in 10 d · niet in deze flow in 14 d. Herinstap 14 dagen.
- +2 uur **A1**, +2 d 09:00 **A2**; beide met dezelfde "niets gedaan sinds start"-filter.

### 11. Sunset TbYQmX
- **Trigger**: toegevoegd aan segment WuHSm6 (75.425 leden, zie B).
- **Flowfilter**: niet in deze flow in 180 d · geen welcome- of post-purchase-mail in 30 d. Herinstap 180 dagen.
- +1 d 09:00 **SUNSET · S1** (geen verzendfilter) · +4 d 09:00 **SUNSET · S2** (Benjamin): alleen als sinds start geen menselijke klik, geen site-bezoek en geen order.
- Geen stap 3 (suppressie): het segment "v4 · Sunset · suppressed" bestaat niet.

### 12. Sunset · kept Wzz6xC
- **Trigger**: toegevoegd aan segment YxfuJT "v4 · Sunset · kept (klik 7d)" = Clicked Email met `$flow = TbYQmX` en Bot Click = false in 7 dagen (nu 0 leden, klopt: sunset is nog niet live).
- **Flowfilter**: niet in deze flow in 365 d.
- +30 min **S3** (Benjamin, Placed Order 0 sinds start) · +4 d 09:00 **S4** (ook geen checkout- of cart-mail in 3 d).

### 13. UGC first egg VPixnJ
- **Trigger**: Delivered Shipment. **Flowfilter**: Placed Order = 1 all time · kookgerei ooit · nooit eerder in deze flow · nooit de 12-delige set (backorder).
- +4 d 09:00 **U1** (geen ticket sinds start, geen refund in 30 d, Fulfilled Order in 60 d).

### Wie krijgt wat na één order (nieuwe klant, pan)
Na livegang van groep B, als de oude naflows blijven zoals GO-LIVE zegt: P1 (+1 u) · FREE E-GUIDE (+3 min) · E-Book-flow (3 mails, vuurt op Mystery Gift) · Pan Education (6 mails vanaf "in transit") · P2 (levering +1 d) · U1 (levering +4 d) · reviewverzoek XzHrez (levering +14 d) · P3 (dag 21) · R1 (dag 45) · R2 (dag 75) · N1 (dag 182) · N2 (dag 365). Zie bevinding 3.

---

## B. Segmenten en lijsten

| ID | Naam | Leden (8 okt) | Definitie in gewone taal | Gebruikt door |
|---|---|---|---|---|
| WuHSm6 | v4 · Sunset · unengaged 120d | **75.425** | Mag marketingmail ontvangen · meer dan 7 mails ontvangen in 120 dagen · 0 keer actief op de site in 120 dagen · 0 orders in 180 dagen · 0 menselijke klikken (Bot Click = false) in 120 dagen · profiel minstens 120 dagen oud. Botfilter en leeftijd zijn nu wel aanwezig (in 06-sunset-kept nog niet). | Trigger Sunset |
| YxfuJT | v4 · Sunset · kept (klik 7d) | **0** (plausibel: sunset niet live) | Minstens 1 menselijke klik (Bot Click = false) op een mail uit flow TbYQmX in de laatste 7 dagen | Trigger Sunset · kept |
| Uw8eZG | Email List (lijst) | 215.028 | Alle inschrijvingen (Alia, enz.) | Trigger Welcome, oude SiaNLu en T2SmtR |
| XY4NVp | Sunset Segment (oud) | 17.394 | Marketing toegestaan · ooit menselijk geklikt of geopend · ooit actief op site · 0 klikken in 100 dagen · 0 opens ... (oude definitie) | Trigger oude sunset S7V4a7 (live) |
| (geen) | v4 · Sunset · suppressed | **ontbreekt** | Plan: in WuHSm6 en S2 ontvangen 3 tot 60 dagen geleden | Wekelijkse suppressie (bevinding 8) |
| (geen) | v4 · Welcome protection | **ontbreekt** | Plan: lid van Uw8eZG minder dan 14 dagen en 0 orders in 14 dagen | Uitsluiting campagnes |
| (geen) | v4 · Campagne-cap | **ontbreekt** | Plan: minstens 3 campagnemails in 7 dagen | Uitsluiting campagnes |
| (geen) | v4 · Heeft kookgerei, v4 · VIP, v4 · US | ontbreken | Rapportage | Geen flow hangt ervan af |

Er zijn 59 segmenten; alleen WuHSm6 en YxfuJT hebben "v4" in de naam, geen enkel segment heeft "v5" in de naam. Geen enkele v4-flow gebruikt een segment of lijst in een filter of split; alle uitsluitingen lopen via "Received Email waarvan `$flow` = flow-ID". Alle zeven gebruikte flow-ID's (X3ySuU, QUBUQV, TZG9Mx, T4a5Mk, WdRz5k, VTkxFL, UyFc78) bestaan en horen bij de juiste flow.

Plausibiliteit: WuHSm6 75.425 tegen 78.682 in 06-sunset-kept (voor de botfilter en leeftijdsgrens). Botfilter maakt het segment groter, leeftijdsgrens kleiner; netto -3.257 is aannemelijk. 35% van de lijst is ongeëngageerd, in lijn met HS-segmenten (Engaged 90 Days VKxqyA ongeveer 89.600). YxfuJT = 0 is juist. Geen segment staat onterecht op 0.

---

## C. Bevindingen

### 1. BLOKKEREND · Browse: de klik-split na B1 matcht nooit
**Wat**: de split na B1 (pan-tak) zoekt Clicked Email met `Campaign Name` bevat `B1 · T05a`. Bij het aanmaken van het A/B-experiment heeft Klaviyo de variaties hernoemd naar "B1 Test #1 October 08, 2026 Variation A/B"; de hoofdmail heet "B1". Geen van die namen bevat `B1 · T05a`.
**Bewijs**: split-actie `119850697` in WdRz5k: `"metric_filters":[{"property":"Campaign Name","filter":{"type":"string","operator":"contains","value":"B1 · T05a"}}]`. A/B-actie `119850693`: variaties `YyFeR4` "B1 Test #1 October 08, 2026 Variation A" en `UkNrdt` "... Variation B", hoofdmail `UXPtQ6` "B1". Lokale JSON had nog "B1 · T05a-A/-B".
**Gevolg**: iedereen in de pan-tak krijgt B2-NOTCLICKED, ook wie in B1 klikte. `CODE · B2-CLICKED · pan` en de T02-meting in browse vuren nooit. (Welcome W1 heeft hetzelfde hernoemen, maar daar hangt geen split van af.)
**Fix (UI, 2 minuten)**: Flows > v4 · Browse abandonment > de split direct na "wacht 2 dagen" in de kookgerei-tak > voorwaarde vervangen door: *What someone has done* · Clicked Email · **where Flow equals "v4 · Browse abandonment"** · **and Bot Click is false** · at least once · since starting this flow. B1 is de enige mail vóór die split, dus elke klik uit deze flow is een B1-klik. Doe hetzelfde bij de B1-ACC-split (`119850698`, werkt nu wel, maar telt botklikken).
Via API kan het niet zonder de flow opnieuw te bouwen (flowacties zijn niet te PATCHen); pas dan in `scripts/build_flows.py` de klik-split aan naar `$flow = WdRz5k` plus `Bot Click = false`.

### 2. BLOKKEREND · T2SmtR (Failure to launch) is nog niet aangepast, en de geplande voorwaarde is te streng
**Wat**: T2SmtR (live, trigger lijst Uw8eZG, 10 mails vanaf dag 30, smart sending aan) stuurt na livegang ook het nieuwe welcome-pad zijn mails. GO-LIVE stap 8 wil daarom in de split na 30 dagen eisen: "Received Email waarvan Campaign Name `Old · Welcome` bevat, minstens 1 keer in 60 dagen". Dat sluit ook iedereen uit die zich de laatste 30 dagen inschreef en SiaNLu-mails kreeg (die heten "EB [DG] | Email #2" enz., niet "Old · Welcome"): zij staan nu in de wachtstap en zouden hun FTL-mails verliezen.
**Bewijs**: split `90675572` in T2SmtR bevat alleen `Placed Order equals 0 in-the-last 30 day`. Live Received Email-events van SiaNLu hebben `Campaign Name: "EB [DG] | Email #3"`.
**Fix (UI)**: T2SmtR > split na "wacht 30 dagen" > voorwaarde toevoegen (EN): *What someone has done* · Received Email · **where Flow equals "v4 · Welcome"** **and Campaign Name doesn't contain "Old ·"** · **zero times** · in the last 60 days. Zo gaan het oude v4-pad en alle huidige inschrijvers door, en valt alleen het nieuwe v4-pad (W0 t/m W5) eruit. Doen vóór groep A live gaat.

### 3. BLOKKEREND (groep B) · Oude naflows: tegenstrijdig plan en dubbele inhoud
**Wat**: `exports/GO-LIVE.md` stap 9 laat Pan Education (YcXbHx), FREE E-GUIDE (YyaMjx), E-Book (TSUnLs) en Mystery Gift Reveal (WvRupU) "ongewijzigd live". `OVERZICHT-V5.md` sectie 8 zegt: deze vier uit vóór post-purchase live gaat. Beide kunnen niet.
**Bewijs**:
- YcXbHx (trigger Postflows "Shipment In Transit") stuurt 6 mails, waaronder "The #1 mistake that makes titanium stick" na levering. De nieuwe P2 (levering VQ93sx) heet "The mistake that makes titanium stick", en P2-SAFE en U1 behandelen dezelfde eerste-ei-boodschap.
- YyaMjx stuurt elke order na 3 minuten "Your E-Guide Is Ready"; P1 bevat dezelfde e-booklink (`/products/e`, 3 keer in p1-first.html).
- TSUnLs vuurt op Mystery Gift/E-Guide in de order: dat zit in 1.418 van de 1.600 orders sinds 20 sept, dus vrijwel elke koper krijgt 3 extra mails.
**Fix (besluit eigenaar, vóór groep B)**: advies: YcXbHx en YyaMjx in dezelfde minuut als RL3TU6 naar Draft (inhoud zit in P1, P2, P2-SAFE, U1). TSUnLs: uit als P1 de mystery gift en het e-book volledig dekt, anders laten. WvRupU (sheets-verkoop) mag blijven. Daarna GO-LIVE.md en OVERZICHT-V5.md gelijk trekken.

### 4. BELANGRIJK · Browse en cart sluiten recente kopers niet uit
**Wat**: checkout weert wie in 7 dagen een post-purchase-mail kreeg; browse en cart niet. Hun filters "Placed Order 0 sinds start" stoppen alleen een order ná de instap. Een koper die twee dagen na zijn order productpagina's bekijkt (heel gewoon) krijgt B1 "Get this pan with 10% off" of B1-ACC.
**Bewijs**: van 605 profielen met Viewed Product op 8 okt (07:00 tot 19:20 UTC) hadden er 24 (4%) een order in de 7 dagen ervoor; bij Added to Cart 2 van 128. Ruwweg 50 kopers per dag in browse. Flowfilter browse WdRz5k bevat geen YkRM4Q-voorwaarde met `$flow = X3ySuU` en geen Placed Order-venster.
**Fix (UI)**: in WdRz5k en TZG9Mx een flowfilter toevoegen: *What someone has done* · Placed Order · zero times · in the last 14 days. (Cart: dit laat K2-RETURNING intact voor wie langer geleden kocht.) Zelfde regel in `build_flows.py` opnemen.

### 5. BELANGRIJK · Delivered Shipment vuurt ook voor gift- en accessoirezendingen
**Wat**: Shopify maakt per fulfillment een Delivered Shipment. Gifts (Mystery Gift, $value 0) en planken gaan soms los. Levering en UGC hebben geen triggerfilter op Items, dus de eerste aankomst (bijvoorbeeld alleen de Mystery Gift) start P2 de dag erna en U1 na 4 dagen, terwijl de pan nog onderweg is. De herinstap (30 dagen) en "nooit eerder in deze flow" blokkeren daarna de echte pan-levering. Ook P2-SAFE wordt overgeslagen, want die eist "Delivered Shipment = 0 sinds start" zonder Items-filter.
**Bewijs**: 453 Delivered Shipment-events sinds 1 okt: 306 met pan of set, 25 alleen gifts, 122 overig (plank, deksel e.d.). 5 van 402 profielen kregen eerst een levering zonder pan en later een met pan (venster van één week, in werkelijkheid meer). Triggers VQ93sx en VPixnJ: `"trigger_filter": null`.
**Fix (UI)**: in VQ93sx en VPixnJ een triggerfilter: Items contains any of (de P2-lijst: Pan Pro's, sets, wok, deep, crêpe, roasting). In X3ySuU bij P2-SAFE de voorwaarde "Delivered Shipment zero times since starting this flow" aanvullen met "where Items contains any of P2-lijst". Bij een herbouw via `build_flows.py`: `trigger_filter` met `metric-property` op `Items`, `contains-any`.

### 6. BELANGRIJK · 14% van de checkouts krijgt geen C3
**Wat**: C3-S eist een grote set, C3-P een Pan Pro of starterbundel én checkout < $300, C3-ACC geen kookgerei én nooit besteld. Wie alleen een Deep Pan, Wok, Crêpe Pan, Pizza Steel of Roasting Pan afrekent, of een Pan Pro-checkout vanaf $300 zonder grote set heeft (2 pannen, pan + deksel + plank), valt overal buiten. Bij hen zit er 4 dagen stilte tussen C2 en C4.
**Bewijs**: 2.897 Checkout Started-events sinds 1 okt nagespeeld met de live filters: C3-P 1.413, C3-ACC 622, C3-S 458, **geen C3 404**. Grootste groepen: alleen Deep Pan Pro 118, Wok 54, Pan Pro Standard >= $300 36, Crêpe 29, Pizza Steel 26, Large >= $300 18, Roasting 13. `$value` is altijd USD (123 van 123 gecontroleerd), dus geen valutafout.
**Fix**: kies één: (a) in de C3-P-filter de lijst uitbreiden met Deep, Wok, Crêpe, Pizza Steel, Roasting en de $300-grens laten vallen (als de C3-P-template "One pan, or three?" generiek genoeg is); of (b) een vierde mail C3-K (vangnet) met filter "kookgerei in 4 dagen EN niet C3-S EN niet C3-P". In de UI: C3-P-mail > Edit filter.

### 7. BELANGRIJK · Sunset: de huidige 75.425 leden starten nooit
**Wat**: een segment-getriggerde flow neemt alleen profielen op die na het live zetten tot het segment toetreden. De 75.425 profielen die er nu al in zitten, komen er pas in als ze eruit vallen en terugkomen (dat gebeurt bij ongeëngageerden bijna nooit). Effect: de sunset doet de eerste maanden vrijwel niets aan de bestaande dode staart. Plan (06-sunset-kept 1.1) wilde juist een inhaalslag in delen van 10.000 per week.
**Bewijs**: trigger `{"type":"segment","id":"WuHSm6"}`, profile_count 75.425.
**Fix (besluit)**: of na livegang in de flow "Add past profiles" gebruiken (dan alles in één keer: S1 naar circa 75.000 profielen, let op klachtenpiek), of de inhaalslag als campagnes S1/S2 in delen van 10.000 (eigen segmenten met een willekeurige verdeling), en de flow alleen voor nieuwe instroom. Oude S7V4a7 (17.394 in XY4NVp) in dezelfde minuut naar Draft, anders krijgen overlappende profielen vier afscheidsmails.

### 8. BELANGRIJK · Ontbrekende segmenten
**Wat en bewijs**: in de lijst van 59 segmenten staan alleen WuHSm6 en YxfuJT met "v4". Ontbreken:
- **v4 · Sunset · suppressed**: zonder dit segment heeft S2 ("Last email from me (unless you tap)") geen gevolg; er wordt niemand onderdrukt.
- **v4 · Welcome protection** en **v4 · Campagne-cap**: GO-LIVE stap 3 zegt "vóór de eerste campagne na livegang". Zonder deze krijgen nieuwe inschrijvers naast W1 t/m W5 ook alle Homestead-campagnes.
**Fix (UI, Lists & Segments > Create segment)**:
- Suppressed: *If someone is in segment* "v4 · Sunset · unengaged 120d" AND *What someone has done* Received Email where Campaign Name contains "SUNSET · S2" at least once in the last 60 days AND Received Email where Campaign Name contains "SUNSET · S2" zero times in the last 3 days. Wekelijks: segment openen > Manage > Suppress all.
- Welcome-bescherming: *If someone is in list* Email List, added in the last 14 days AND Placed Order zero times in the last 14 days. Bij elke campagne uitsluiten.
- Campagne-cap: Received Email where Flow is not set at least 3 times in the last 7 days. Bij elke campagne uitsluiten.

### 9. BELANGRIJK · Triple Pixel-flows uit = bereik weg
**Wat**: GO-LIVE groep A zet ook TBWngE (cart), Tsg2tV (checkout) en TyEjuQ (browse) op Draft. Die vangen bezoekers die wel een Triple Pixel-event hebben maar geen Shopify-event. De v4-flows triggeren alleen op Shopify/klaviyo.js-events.
**Bewijs** (profielen, 7 okt 07:00 tot 8 okt 19:20 UTC): Added to Cart TP 500 profielen, waarvan **182 zonder** Shopify Added to Cart; Checkout Started TP 155, waarvan 32 zonder Shopify Checkout Started. Viewed Product TP (8 okt): 140 van 555 zonder Viewed Product. TBWngE filtert zelf al op "Added to Cart (QXcV8K) 0 sinds start": het is bewust het complement.
**Fix (besluit eigenaar)**: of de drie TP-flows laten draaien en in elk een flowfilter toevoegen "Received Email where Flow equals v4 · Cart abandonment (resp. Checkout, Browse) zero times since starting this flow" (en voor TBWngE de bestaande SwkMyn-filter vervangen door TZG9Mx); de T01-meting blijft zuiver, want beide armen zijn Shopify-getriggerd. Of accepteren dat circa 120 cart-profielen per dag geen mail meer krijgen. Hun oude inhoud wel eerst nalopen (oude claims).

### 10. BELANGRIJK · Wisselgat bij winback en post-purchase
**Wat**: v4 Winback, VIP en Anniversary starten alleen bij orders na livegang. Wie in de 75 dagen vóór livegang bestelde, zit nu in oude winback UEfh4h; die gaat in groep B naar Draft, dus R1/R2 vallen weg voor circa twee maanden aan klanten. Hetzelfde voor recente kopers in RL3TU6 (hun lopende reeks stopt).
**Bewijs**: UEfh4h trigger Placed Order, geen flowfilter; v4 UyFc78 trigger Placed Order zonder backfill.
**Fix (UI)**: UEfh4h niet naar Draft maar live laten met een extra flowfilter: Placed Order zero times **after** <datum en tijd van livegang>. Nieuwe orders vallen dan direct af (die doet v4), lopende runs maken hun reeks af. Na 75 dagen op Draft. Voor RL3TU6 hetzelfde kan, maar de oude inhoud noemt "100 Days to Try Us Out" (in strijd met DECISIONS, 30-day returns): daar liever wel uitzetten.

### 11. KLEIN · Welcome W4: land vaak onbekend
**Bewijs**: 100 inschrijvers van 1 okt: 15 zonder `location.country`; 100 nieuwste: 28 zonder. Van wie het land bekend is, is 61% US. Gevolg: circa 9% van de inschrijvers is waarschijnlijk US maar krijgt W4-INT (geen dollars, geen US-only producten).
**Fix**: split uitbreiden met OF `properties.country_code equals US` (nu 13% gevuld bij nieuwe profielen). Of accepteren; W4-INT is niet fout, alleen minder scherp.

### 12. KLEIN · Klik-splits tellen botklikken
Splits `119850697` en `119850698` (browse) gebruiken Clicked Email zonder `Bot Click = false`. Een Outlook-scanner kan zo een eigen code (CODE · B2-CLICKED) uitlokken. Fix: zie bevinding 1.

### 13. KLEIN · Sunset S1 zonder verzendfilter
S1 (`119850754`) heeft `additional_filters: null`. Wie in de dag tussen instap en S1 klikt of koopt, krijgt toch "Should we keep writing to you?". Fix: S1 filter Placed Order 0 sinds start EN Clicked Email (Bot Click false) 0 sinds start EN Active on Site 0 sinds start.

### 14. KLEIN · Cooldown-logica en uitleg lopen uiteen
OVERZICHT-V5 zegt "wie een eigen code kreeg (en die gebruikte)"; de split telt alleen ontvangst van een `CODE ·`-mail. Codes uit de oude T01-armen ("Old · Cart 2 ... 10% off", "Old · Welcome 8") tellen niet. De VIP-cooldown kijkt naar `Discount Codes` niet leeg, dus ook HI10 of een lekcode telt als "gebruikt". Geen fix nodig vóór livegang; wel de uitleg in OVERZICHT-V5 corrigeren.

### 15. KLEIN · Tweede order binnen 30 dagen
Post-purchase heeft "niet in deze flow in 30 dagen" plus herinstap 30. Een tweede order binnen 30 dagen krijgt geen P1-REPEAT, en de P3 van de eerste order vervalt (Placed Order sinds start). Bij order 2 neemt VIP het over; bij order 3+ binnen 30 dagen krijgt de klant niets. Acceptabel, wel bewust kiezen.

### 16. KLEIN · Geen C2 voor terugkerende klant met kookgerei
C2 eist "Placed Order = 0 all time", C2-ACC "geen kookgerei". Een bestaande klant met een pan in de checkout krijgt op dag 1 niets. Mogelijk bewust (C2 gaat over "is it tested?"); anders C2-ACC-filter verruimen.

### 17. KLEIN · A/B-experimenten
W1 (`01M4E3EWS7W4DCBYCZ8VSB2WP4`) en B1 (`01M4E3FN7PHBNKSZ10BNFMMB4P`) staan op `experiment_status: draft`, allocatie 50/50, winnaar handmatig. Bij livegang controleren dat het experiment echt start. Rapportage die op de naam "W1 · T04-A/B" of "B1 · T05a" zoekt (`scripts/test_report.py`) vindt niets meer: gebruik `$message` (VnXKz4/SXwPrW, YyFeR4/UkNrdt) of de A/B-rapportage van Klaviyo.

### 18. KLEIN · Voorrang welcome en browse
Browse start niet bij een welcome-mail in 7 dagen; welcome wijkt alleen voor checkout en cart (1 dag). In de praktijk gaat welcome dus boven browse. Dat volgt plan 1.2 (uitschrijving bij overlap), maar OVERZICHT-V5 sectie 3 zegt "post-purchase > checkout > cart > browse > welcome". Alleen de tekst aanpassen.

### 19. KLEIN · Testadres-filter
Welcome-flowfilter `email not-contains "test@"` sluit ook echte adressen als contest@, latest@ uit. Fix: `not-contains "test@example.com"` zoals SiaNLu, of `does not end with "@example.com"`.

---

## D. Overlap met de oude live flows bij livegang

24 flows live. Overlap per v4-flow, en wat er moet gebeuren:

| v4-flow | Oude live flow met dezelfde trigger | Risico als beide live | Actie |
|---|---|---|---|
| Checkout QUBUQV | Y2TmNB (Checkout Started), Tsg2tV (TP-variant) | dubbele C-mails | groep A: zelfde minuut Draft; Tsg2tV zie bevinding 9 |
| Cart TZG9Mx | SwkMyn (Added to Cart), TBWngE (TP) | dubbel | idem |
| Browse WdRz5k | Wj6x6V (Viewed Product), TyEjuQ (TP) | dubbel | idem |
| Welcome T4a5Mk | SiaNLu (lijst Uw8eZG), T2SmtR (lijst Uw8eZG) | dubbele welcome; FTL in het nieuwe pad | SiaNLu Draft; T2SmtR fix uit bevinding 2 |
| Post-purchase X3ySuU | RL3TU6, YyaMjx, TSUnLs, YcXbHx, SxN86d, UYALJ8 | P1 plus 3 tot 10 oude mails | bevinding 3 |
| Levering VQ93sx, UGC VPixnJ | YcXbHx (in transit), XzHrez (delivered +14 d) | P2 dubbel met Pan Education | bevinding 3; XzHrez mag blijven |
| Winback UyFc78 | UEfh4h | dubbele winback | bevinding 10 |
| Sunset TbYQmX | S7V4a7 (segment XY4NVp) | vier afscheidsmails | zelfde minuut Draft |
| VIP, Anniversary, Site, Sunset · kept | geen | geen | geen |

Geen v4-flow overlapt met de CS-flows (TLHht3, UcGzaL, Y4a7fJ), BIS (WsQDYu), Middle East (SxN86d, alleen splits op land), Trustpilot (Vixr6X, 12 okt uit) of Pan Flash (Wn2tsq, mail draft).

## E. Wat klopt (gecontroleerd, geen actie)

- Stop-bij-bestelling: elke verkoopmail heeft "Placed Order 0 sinds start" (checkout, cart, browse, welcome, site, winback, P3, S2, S3, S4).
- Voorrang checkout boven cart boven browse/site, en welcome wijkt voor checkout/cart: correct met de juiste flow-ID's.
- Cooldown-split staat vóór elke T02-split, berichtnamen `CODE · ...` kloppen in alle 13 codemails; VIP en N2 zonder T02 zoals gepland.
- T01: random 50% bovenaan in checkout, cart, welcome, browse; oud pad heet overal "Old · ...".
- VIP: Placed Order = 2 all time; de API accepteerde `Discount Codes length-greater-than 0`.
- Anniversary: Placed Order = 1 all time plus kookgerei; wachttijden 182 en 183 dagen zijn geaccepteerd.
- Sunset-segment: consent, meer dan 7 mails, 0 menselijke klikken, 0 site, 0 orders in 180 d, profiel minstens 120 dagen: allemaal aanwezig.
- Sunset · kept: `$flow = TbYQmX` en Bot Click = false in YxfuJT; S2 slaat klikkers over.
- Cart-triggerfilter weert de vier gratis gifts; categorie-split klopt op alle ATC-producten sinds 4 okt.
- Titellijsten dekken elke verkochte pan, set en schort (1.600 orders).
