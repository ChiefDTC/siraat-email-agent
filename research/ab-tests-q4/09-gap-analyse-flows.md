# 09 · Gap-analyse flows vóór Black Friday (28 okt 2026)

Vraag Floris: 100% zeker weten dat we vóór Black Friday geen flow missen. Dit stuk zoekt (1) lifecycle-flows en triggers die ontbreken en (2) bestaande flows die er wel zijn maar niet doen wat ze moeten.

Alles alleen gelezen. Klaviyo (account TdtTzz, revision 2025-10-15): `GET /api/flows` over alle pagina's (110 flows, 29 live, 81 draft, 0 gearchiveerd) met definitie per flow, `GET /api/metrics` (184 metrics) met `metric-aggregates` per metric over 14 dagen, Received Email `YkRM4Q` per `$flow` (totaal en per dag), Placed Order `RSNxYV` als events met attributie (`include=attributions`) zodat orders van $0 (TikTok-samples, besluit Floris 28 okt) eruit konden, segmentdefinities en de HTML van de live oude mails. Daarnaast Recharge (actieve abonnementen, opzeggingen), Aftersell (upsellomzet), Email Love en WebSearch. Niets gewijzigd in Klaviyo of elders. In dit stuk staan alleen aggregaten, geen klantdata. Scripts en ruwe data in de scratchpad (`gap/`).

**Venster:** 14 okt 00:00 tot 28 okt 00:00 UTC (14 dagen), tenzij anders vermeld. Omzet = Klaviyo-attributie op Placed Order, zonder orders van $0. Per week = 14 dagen gedeeld door 2.

**Kader winkel in dit venster:** 3.286 orders, waarvan 245 van $0 (7,5%). Betaald: 3.041 orders, $750.851 (gem. $247). Flows: $70.125 (9,3%), dus ongeveer **$35.000 per week**.

---

## 0. Samenvatting voor Floris

1. **Geen enkele flow is "vergeten" in de zin dat er een groot event zonder flow ligt dat we nog niet kenden.** Wel zijn er acht dingen die vóór 1 november kapot, dubbel of verouderd zijn, en negen best-practice-flows die nog ontbreken. Van de top 10 van 19 oktober is twee keer iets volledig gedaan (Mystery Gift live, review-vangnet live) en één keer half (browse-split op 100%). De rest staat nog open.
2. **Grootste risico vóór de sale: 9 live oude mails tonen nog "SIRAAT PRIME TIME SALE | UP TO 56% OFF"**, 3 daarvan "100-DAY TRIAL", 1 "Lifetime". Dat zijn de 4 overgebleven Failure-to-launch-mails, de 4 mails van de oude winback en de e-guide. Samen ongeveer **26.000 mails per week**, straks naast "70% off". In strijd met DECISIONS (30 dagen retour, 75 jaar garantie). Stond al als nummer 3 op de lijst van 19 okt.
3. **$0-orders (TikTok-samples) lopen zes Placed Order-flows in**, ook VIP, winback, anniversary en de oude winback. Er staat alleen in checkout een filter `$value > 0`. 245 samples in 14 dagen: die krijgen straks een winbackcode op dag 45, een VIP-code en een jubileummail, en een sample telt in VIP mee als "tweede order".
4. **Abonnementen zijn ineens echt:** Recharge ging van 0 naar 124 actieve abonnementen sinds Mystery Gift live ging (23 okt), met 26 opzeggingen in negen dagen. Er is geen welkom-, mislukte-betaling- of opzegflow. Er staat wel een nieuwe draft "DW Sub Flow" (YuejJ9) op Placed Order zonder triggerfilter, die naar dezelfde mensen zou gaan als Mystery Gift.
5. **Ontbrekende flows met het meeste geld vóór BFCM:** vangnet checkout en cart via Triple Pixel en Elevar ($750 tot $1.200 per week), SMS-flows ($1.200 tot $2.100 per week, 1.760 nieuwe SMS-inschrijvers per week en 0 SMS-flows), een BFCM-vroegetoegang plus "sale ended"-flow ($1.000 tot $3.000 per week in de BFCM-weken) en jubileum en VIP voor bestaande klanten ($700 tot $1.500 per week in november).
6. **Affiliate S1 bereikt bijna niemand** (36 mails in 14 dagen), omdat hij op de kapotte Postflows-bezorgtrigger staat. Er komt een veel beter signaal binnen zonder flow: "Enrolled in SocialSnowball through purchase", ongeveer 1.250 per week.
7. **Opgeteld kan de top 10 tussen ongeveer $4.000 en $9.000 extra per week opleveren in november**, plus minder risico (claims, codes naar samples) en minder tickets. Alles is een schatting; sectie 4 geeft per punt de aanname.

De geprioriteerde lijst staat in sectie 5.

---

## 1. Inventaris van alle flows

### 1.1 Live flows (29), 14 dagen

RPR = omzet per verstuurde mail, zonder $0-orders.

| ID | Flow | Trigger | Mails 14 d | Betaalde orders | Omzet | RPR | Markering |
|---|---|---|---|---|---|---|---|
| T4a5Mk | v4 · Welcome | lijst Uw8eZG | 35.686 | 125 | $34.794 | $0,97 | ok; volume stijgt (1.388 naar 3.400 per dag) |
| QUBUQV | v4 · Checkout abandonment | Checkout Started (RfMvni), `$value > 0` | 2.931 | 50 | $12.106 | $4,13 | ok |
| TZG9Mx | v4 · Cart abandonment | Added to Cart (QXcV8K), filters gifts | 5.305 | 35 | $10.114 | $1,91 | geen waardesplit (zie 4.13) |
| WdRz5k | v4 · Browse abandonment | Viewed Product (XNtYMB) | 5.105 | 22 (+2 van $0) | $3.855 | $0,76 | filters 19 okt (A, B) niet aangepast |
| X3ySuU | v4 · Post-purchase | Placed Order, **geen** `$value`-filter | 3.511 | 20 | $3.720 | $1,06 | **samples erin**; herinstap nog 30 d |
| VQ93sx | v4 · Post-purchase · levering | Delivered Shipment (VcUF33) | 849 | 8 (+1) | $1.316 | $1,55 | **bezorgtrigger valt weg** (154 naar ~35 per dag) |
| YyaMjx | FREE E-GUIDE (oud) | Placed Order, geen filter | 2.841 | 6 (+1) | $975 | $0,34 | **dubbel met P1**; 56%-banner; uitschrijving 1,63% op 27 okt |
| QNZyEb | v4 · Browse · Triple Pixel | Viewed Product TP (V48nhq) | 1.024 | 4 (+1) | $679 | $0,66 | ok |
| T2SmtR | EB · Failure to launch (oud) | lijst Uw8eZG + 30 d | 39.766 | 5 | $657 | $0,02 | **oud, lekt nog ~3.000 per dag**; 4 live mails met 56%-banner |
| TbYQmX | v4 · Sunset | segment WuHSm6 | 16.396 | 2 | $597 | $0,04 | onderdrukt niemand (afmeldingen/01) |
| UEfh4h | EB · Customer Winback (oud) | Placed Order + 60 d | 6.588 | 4 (+1) | $586 | $0,09 | **oud, naast v4** tot 14 dec; 56%-banner; samples erin |
| WsQDYu | BIS · Back in Stock | Subscribed to Back in Stock (T4dnSM) | 147 | 3 | $444 | $3,02 | werkt; oude template |
| Wzz6xC | v4 · Sunset · kept | segment YxfuJT | 72 | 1 | $155 | $2,15 | ok |
| VLGhbR | v4 · Site abandonment | Active on Site (UdCdLD) | 1.503 | 1 | $128 | $0,09 | **bereik ingestort**: 329 naar ~60 per dag sinds 14 okt |
| YwsKcf | v4 · Mystery Gift | Ordered Product 15785445622100 of naam | 179 | 0 | $0 | $0 | live sinds 23 okt, M1 vanaf 26 okt; trigger klopt |
| XzHrez | Review request · Delivered +14d | Delivered Shipment | 462 | 0 | $0 | | bezorgtrigger valt weg |
| VPixnJ | v4 · UGC first egg | Delivered Shipment | 661 | 0 | $0 | | bezorgtrigger valt weg |
| R22pzb | AFF S1 · Activatie na bezorging | Postflows Delivered (UabgWz) | 36 | 0 | $0 | | **bijna dood**, zie K2 |
| TvfJYU | Review · fallback Fulfilled +21d | Fulfilled Order (VtEiZT) | 0 | | | | eerste mails vanaf 9 nov (ok) |
| VTkxFL | v4 · VIP | Placed Order, precies 2 orders, +30 d | 0 | | | | eerste mail ~8 nov; **samples tellen als order** |
| UyFc78 | v4 · Winback | Placed Order + 45 d | 0 | | | | eerste mail ~23 nov; samples erin |
| XbYT7T | v4 · Anniversary | Placed Order, + 182 d | 0 | | | | eerste mail april 2027; bestaande klanten nooit |
| Yp6sKv | AFF S5a · Verkoopmelding | Snowball New referral sale (Xqbr4d) | 0 | | | | 1 event in 14 d, ok |
| TkV5DY | AFF S5b · Uitbetaling | Snowball Payout sent (WManrA) | 0 | | | | 1 event, ok (eerste uitbetalingen na 45 d) |
| UYALJ8 | EB · E-Gift Card | Placed Order met "E-Gift Card" | 0 | | | | **geen instroom**: 0 orders met dat item in 14 d |
| Wn2tsq | EB · Pan Flash Buyers | segment YbCB68 (juli, vaste datum) | 0 | | | | **dode trigger**: statisch segment van 41, mail 1 op Draft |
| TLHht3, UcGzaL | CS-meldingen exception, attempt failed | Postflows 6 en 7 | intern | | | | interne alert, ok |
| Y4a7fJ | Ready for Pickup (CS) | Postflows 8 | intern | | | | e-mail op Draft, alleen interne alert, ok |

### 1.2 Markeringen

**Live zonder instroom (en dat is niet de bedoeling):**
- UYALJ8 E-Gift Card: 0 orders met "E-Gift Card" in 14 dagen. Of het product heet anders, of het wordt niet verkocht. In Q4 is dit de cadeauflow die wel moet werken (zie 4.14).
- Wn2tsq Pan Flash Buyers: segment op een vaste periode in juli, 41 profielen, groeit nooit meer. Kan op Draft.
- R22pzb (affiliate S1): 36 mails in 14 dagen bij ~1.500 orders per week.

**Live zonder instroom, wel zo bedoeld:** VIP (8 nov), Winback v4 (23 nov), Anniversary (april 2027), review-fallback TvfJYU (9 nov), AFF S5a/S5b.

**Dode of zieke triggers:**
- Delivered Shipment (VcUF33) en Postflows Delivered (UabgWz) zakten vanaf ~21 okt van 100 tot 430 naar 35 tot 70 per dag (Shopify "Marked Out for Delivery" zakte mee). Raakt VQ93sx, XzHrez, VPixnJ en R22pzb. Wordt al aangepakt (plan R1). Bijvangst: **ShipBob Delivered (SMpL9v) bleef stabiel op 35 tot 87 per dag** en is een derde bezorgsignaal dat geen flow gebruikt.
- Wn2tsq (statisch segment), UYALJ8 (productnaam).
- Geen enkele live flow wijst nog naar een verwijderd product. Mystery Gift-trigger (product 15785445622100 of naam "Mystery Gift") klopt: 2.521 van de 3.041 betaalde orders hebben het item.

**Dubbele flows naar dezelfde mensen:**
- **YyaMjx FREE E-GUIDE en v4 · Post-purchase P1-FIRST** starten allebei op Placed Order en geven allebei de e-guide. Elke koper krijgt dus twee mails rond dezelfde download. 2.841 e-guide-mails in 14 dagen, $0,34 per mail, en op 27 okt een uitschrijfpiek van 1,63%.
- **Draft YuejJ9 "DW Sub Flow | Buyers zonder sheets-abonnement"** (6 mails, aangemaakt 27 okt, niet door ons) zou op elke Placed Order starten. Vrijwel elke order heeft de Mystery Gift (de strips), dus dit gaat naar dezelfde mensen als YwsKcf M1 tot M3. Niet live zetten zonder afstemming.
- Browse: WdRz5k en QNZyEb dedupen elkaar goed (03-browse-site).

**Oude flows die nog lekken naast v4:**
- T2SmtR Failure to launch: ~2.800 tot 3.500 mails per dag, $0,02 per mail. Krijgt geen nieuwe instroom meer en loopt vanzelf leeg rond eind november. 6 mails staan sinds 28 okt op Draft, 4 lopen nog.
- UEfh4h oude winback: ~490 per dag, bewust tot 14 dec (DECISIONS 8 okt).
- YyaMjx: zie dubbel.
- Alle drie dragen de 56%-banner (sectie 1.3).

### 1.3 Verouderde claims in live mails (nog niet opgelost sinds 19 okt)

| Flow | Live mail | Gevonden in beeld-alt | Mails per week (ca.) |
|---|---|---|---|
| T2SmtR | Titanium vs Non-Stick | PRIME TIME SALE / UP TO 56% OFF, 100-DAY TRIAL | ~5.000 per mail, ~20.000 samen |
| T2SmtR | How to Store + Care | idem, plus "Get a Lifetime of Use Out of Us" | |
| T2SmtR | Titanium Vs Stainless Steel | PRIME TIME / 56%, 100-DAY TRIAL | |
| T2SmtR | Micro-Plastic Free | PRIME TIME / 56% | |
| UEfh4h | mail 1, 2, kopie 2, 3 | PRIME TIME / 56% | ~3.400 |
| YyaMjx | E-Guide Flow | PRIME TIME / 56% | ~1.400 |

### 1.4 Status van de lijst van 19 oktober

| # (19 okt) | Wat | Stand 28 okt |
|---|---|---|
| 1 | Browse-bereik | QNZyEb live, 90/10 naar 100%. Welcome-filter (7 d) en herinstap (7 d) niet aangepast |
| 2 | Vangnet checkout en cart via TP en Elevar | niet gedaan |
| 3 | 56%-banners en claims | niet gedaan (6 FTL-mails op Draft, de 4 overige en winback/e-guide dragen het nog) |
| 4 | BFCM early access | niet gebouwd (W5-variant voorgesteld in 00-plan, Q2) |
| 5 | Price drop en low inventory | niet gedaan |
| 6 | SMS-flows | niet gedaan, 0 SMS-acties in alle flows |
| 7 | Bestaande klanten: anniversary, VIP, reactivatie | niet gedaan (kopersreeks als campagne staat in 00-plan, test 1) |
| 8 | Mystery Gift v3 | **live 23 okt** |
| 9 | Proactieve deelzending en vertraging | niet gedaan (WjhwUa nog Draft) |
| 10 | Dekselmail en Cutting Board-tak | niet gedaan (T15 dekselkaart in P1 gepland 1 nov) |
| uitbr. F | Review-vangnet op Fulfilled Order | **live (TvfJYU)** |
| uitbr. E, G, H | Herinstap PP 7 d, VIP ≥ 2, W4 onbekend land | niet gedaan (E gepland 29 okt) |

---

## 2. Controle per metric (14 dagen)

Alle 184 metrics langsgelopen. Hieronder alles met volume dat niet triggert of waar de dekking twijfelachtig is. Metrics met 0 events (Wonderment, TrackBee, Zendesk, Alia, Meta lead ads, de meeste ShipBob-statussen, Klaviyo-forms) zijn dode koppelingen of niet in gebruik.

| Metric (ID) | Bron | Events | Uniek | Flow | Oordeel |
|---|---|---|---|---|---|
| Added to Cart - Triple Pixel (SZNHJK) | Triple Whale | 39.017 | 4.754 | geen (TBWngE draft) | **gat**, vangnet cart (4.1) |
| Viewed Product - Elevar SS (VPgSUk) | Elevar | 32.687 | 12.125 | geen | gat, vangnet browse (klein na QNZyEb) |
| Active on Site - Triple Pixel (TfGuLV) | Triple Whale | 29.696 | 13.361 | geen | tweede trigger voor site, laag |
| Added to Cart - Elevar SS (U2QZpR) | Elevar | 25.236 | 4.752 | geen | **gat**, vangnet cart |
| Received Text Message (Y6Y22E) | Klaviyo SMS | 22.539 | 13.917 | geen flow, alleen campagnes | SMS draait alleen op campagnes |
| Viewed Collection (XkJTYh) | Shopify | 7.303 | 3.389 | geen | **gat**, tak in site (4.10) |
| ParcelPanel / ParcelWILL (RN4Tk4, WYXGCn) | ParcelWILL | 5.508 elk | | geen | tracking loopt via de app, niet nodig |
| Fulfilled Partial Order (UHUr2m) | Shopify | 3.896 | 2.899 | geen | **gat**, deelzending heads-up (4.16) |
| Subscribed to Text Messaging Marketing (WQVUMq) | Klaviyo | 3.528 | 3.513 | **geen** | **gat**, SMS-welkom (4.2) |
| Checkout Started - Triple Pixel (RtgBgs) | Triple Whale | 2.638 | 1.841 | geen (Tsg2tV draft) | **gat**, vangnet checkout (4.1) |
| Enrolled in SocialSnowball through purchase (XzrVJZ) | Snowball | 2.276 | 2.275 | geen (Xszb66 draft, zonder trigger) | **betere trigger voor affiliate S1** (K2) |
| ShipBob LabeledCreated, Processing, Packed, Picked, InTransit | ShipBob | 870 tot 2.050 elk | | geen | interne stappen, niet nodig |
| Opened Ticket (YzvjGf) / Resolved Ticket (SzcCyb) | Gorgias | 2.022 / 1.652 | 1.600 / 1.334 | alleen als filter (5 flows) | goed; zie 4.15 |
| Begin Checkout - Elevar SS (WshVwX) | Elevar | 2.016 | 1.956 | geen | gat, vangnet checkout |
| Postflows 4. Shipment Delivered (UabgWz) | Postflows | 1.614 | 1.434 | R22pzb | **valt weg sinds ~21 okt** (R1) |
| Postflows 2. In Transit (VjA7Qr) | Postflows | 1.461 | | geen live (YcXbHx draft) | niet nodig |
| Fulfilled Order (VtEiZT) | Shopify | 1.396 | 1.372 | TvfJYU | komt in golven (822 op 24 okt) |
| Postflows 3. Out for Delivery (SmKps6) | Postflows | 1.175 | 1.057 | geen (SNcVfe draft) | transactioneel, niet nodig |
| Delivered Shipment (VcUF33) | Shopify | 1.070 | 1.013 | VQ93sx, XzHrez, VPixnJ | **valt weg** (R1) |
| Coupon Assigned (XUMYt7) | Klaviyo | 1.045 | | n.v.t. | codes uit flows, goed |
| ShipBob Shipped (UEsTZn) | ShipBob | 868 | 823 | geen (WjhwUa draft) | trigger deelzending (4.16) |
| Marked Out for Delivery (WQJZZS) / ShipBob OutForDelivery (VcQGgB) | Shopify / ShipBob | 862 / 840 | | geen | "out for delivery" is transactioneel; geen marketingflow nodig |
| ShipBob Delivered (SMpL9v) | ShipBob | 781 | 732 | **geen** | stabiel signaal, kandidaat-vangnet bij R1 |
| MissingPackagePreference (TKCvvQ) | ShipBob | 313 | 304 | geen | operationeel; ShipBob/Floris |
| Submitted Search (YeVVus) | Shopify | 305 | 190 | geen | klein, tak in site |
| ShipBob OutOfStock (TKx6c4) | ShipBob | 274 | 265 | geen | **gat**, proactieve vertragingsmail (4.16) |
| Completed Survey (Wa4pz9) | Gorgias | 158 | 156 | geen | CSAT, zie 4.15 |
| Order placed on Recharge (R5YMXn) | Recharge | 119 | | geen | abonnementsorders |
| Subscription started (WPwuMk) | Recharge | 114 | 113 | **geen** | **gat**, sinds 23 okt van 0 naar 63 op één dag (4.18) |
| Subscribed to Back in Stock (T4dnSM) | Klaviyo | 93 | 81 | WsQDYu | gedekt |
| Refunded Order (Xg6cwn) / Cancelled Order (TFervq) | Shopify | 62 / 43 | | alleen als filter (9 en 1 flows) | feedbackmail laag (4.15) |
| Ticket Created (S2Aax7) | Klaviyo | 40 | | geen | klein |
| Subscription cancelled (YksUBL) | Recharge | 26 | 26 | **geen** | **gat** (4.18) |
| Postflows 6, 7, 8 (exception, attempt failed, pickup) | Postflows | 26 / 25 / 97 | | CS-alerts | goed |
| Order upcoming (WYakYM) | Recharge | 9 | | geen | Recharge mailt zelf |
| Charge processing failed (Sdc247) | Recharge | 6 | 2 | **geen** | **gat**, klein (4.18) |
| Snowball overige (13 metrics) | Snowball | 1 tot 2 elk | | S5a, S5b | ok |
| Price Drop | Klaviyo-catalogus | bestaat niet | | | **niet aangezet** (4.4) |
| Aftersell | | geen metric in Klaviyo | | | upsells ~$36.000 in 14 d, zitten in de order zelf; geen flow nodig |
| Okendo, Loox, Trustpilot | | geen metric | | | reviews niet in Klaviyo; negatieve-reviewflow kan nu niet (4.15) |

**Bezorgevents:** de daling sinds ~21 okt wordt al aangepakt (plan R1). Daarom hier geen nieuwe actie, wel de notitie dat ShipBob Delivered (SMpL9v) in dezelfde periode niet daalde.

---

## 3. Wat ontbreekt ten opzichte van best practice (Q4, DTC-kookgerei)

Getoetst aan de data van Siraat. Concurrenten uit de eigen inbox-tijdlijn (research/concurrenten/overzicht.md, 16 dagen), Email Love en WebSearch. Email Love heeft van de kookgerei-merken alleen 4 HexClad-mails (welkom, reviews, Gordon Ramsay, oprichtersbrief) en geen journey; wel veel Black Friday early access-mails van andere DTC-merken in de laatste week (Lola Blankets "VIP early access starts soon", Kitsch, Inside Weather "Consider this your Black Friday invite", DUSK "Extra 25% off early access") en "price drop"-flows bij OFFICE en LOFT ("An item you've viewed just dropped in price").

| Best practice | Siraat nu | Data | Gat? |
|---|---|---|---|
| Replenishment vaatwasstrips | YwsKcf (M1 tot M3) voor elke Mystery Gift-ontvanger | 2.521 orders met de gift in 14 d; 122 betaalde strip-orders; 124 actieve abonnementen | klein: herhaalherinnering voor losse kopers zonder abonnement ontbreekt (4.17) |
| Abonnement (welkom, mislukte betaling, opzeggen) | niets | 114 starts, 26 opzeggingen (Recharge zegt 26 in 9 dagen), 6 mislukte betalingen | **ja** (4.18) |
| Cross-sell per product (deksel, set, accessoires) | P3 dag 21 met xsell; T15 dekselkaart gepland | deksel in 420 van 3.041 orders; ~2.000 orders met een pan | deels; dekselmail dag 30 tot 35 ontbreekt (4.8) |
| VIP en tweede aankoop | VTkxFL, alleen bij precies 2 orders, alleen nieuwe kopers | eerste mail 8 nov | deels (4.6) |
| Verjaardag / anniversary | Anniversary alleen voor kopers na 8 okt; geen verjaardagsveld | cohort nov 2025: 14.045 kopers | **ja** voor bestaande klanten (4.6); verjaardag n.v.t. zonder veld |
| Garantieregistratie | geen | 75-year warranty, geen registratiepagina bekend; HexClad heeft "Register for your warranty" | ja, maar na BFCM (4.11) |
| Zorg- en gebruikseducatie | P1, P2 (levering), P2-SAFE; Pan Education YcXbHx draft | P2 krijgt door R1 weinig volume; Cutting Board-tak weg (195 plankorders in 14 d) | klein (4.12) |
| Prijsdaling | geen | sale gaat via echte prijzen (Deep Pan Pro $305 naar $119), dus de catalogus ziet de daling | **ja** (4.4) |
| Back in stock | WsQDYu | 93 aanmeldingen, $3,02 per mail | gedekt |
| Verlaten winkelwagen met hoge waarde | checkout heeft $300-split (C3-S); cart niet | sets vanaf $299; 12-delige set in 257 orders | klein (4.13) |
| Cadeau-flow Q4 | gift card-flow zonder instroom; geen cadeaukoper-tak | 0 gift card-orders | **ja** (4.14) |
| BFCM-specifiek (vroege toegang, "sale ended") | geen lijst, geen flow; W5-variant voorgesteld | concurrenten en DTC-merken sturen nu al invites | **ja** (4.3) |
| Post-BFCM-heractivatie | winback v4 vanaf 45 d, oude winback tot 14 dec | BFCM-kopers en BFCM-klikkers zonder order | **ja** (4.5) |
| SMS | 0 SMS-flows, wel SMS-campagnes (22.539 SMS ontvangen) | 3.528 nieuwe SMS-inschrijvers | **ja** (4.2) |
| Na negatieve review of ticket | tickets alleen als filter; reviews niet in Klaviyo | 2.022 tickets, 158 surveys | laag (4.15) |
| Leveringsvertraging proactief | WjhwUa en Fulfillment Delayed op Draft | 3.896 deelzendingen, 274 OutOfStock | **ja** (4.16) |

---

## 4. Per ontbrekende of kapotte flow: volume, omzet, moeite, BFCM, API

Aannames: eigen RPR in dit venster (checkout $4,13, cart $1,91, browse $0,76, welcome $0,97, post-purchase $1,06, BIS $3,02). Externe benchmarks: Klaviyo 2024 abandoned cart $3,65 per ontvanger, welkom $2,35 tot $2,65, top 10% SMS-flows boven $5, replenishment $2 tot $5 (agency), back in stock $9,14 (Eightx). Voor flows die ook campagnes overlappen reken ik 50% incrementeel. Moeite: S = een dag of minder, M = 2 tot 5 dagen, L = langer of een nieuwe koppeling.

API: een nieuwe flow kan als Draft met `POST /api/flows` (definitie met triggers, filters, acties). Bestaande flows: alleen status en naam via PATCH, en acties via `PATCH /api/flow-actions`. **Triggerfilters en herinstap van een bestaande flow kunnen alleen in de UI** (05-herinstap). Een A/B-test starten is altijd een klik in de UI.

### Kapot of niet zoals bedoeld

**K1. Bezorgtrigger valt weg** (VQ93sx, XzHrez, VPixnJ, R22pzb). Wordt aangepakt (R1). Volume terug: ~700 P2 en ~700 reviewverzoeken per week. Toevoeging: ShipBob Delivered (SMpL9v, ~50 per dag, stabiel) als extra vangnet. BFCM: ja. API: kloon als Draft met andere trigger kan.

**K2. Affiliate S1 op de verkeerde trigger.** 36 mails in 14 dagen. "Enrolled in SocialSnowball through purchase" (XzrVJZ) komt ~1.250 keer per week binnen, bij elke order. Advies: kloon van R22pzb als Draft met trigger XzrVJZ en dezelfde wachttijd als de bezorging (bijvoorbeeld 10 dagen), filter "Delivered Shipment of Postflows Delivered 0 sinds start" tegen dubbel. Volume: ~1.000 per week (na filters). Omzet: indirect (vriendenorders); voorzichtig $100 tot $300 per week. Moeite S. BFCM: ja, maar Floris beslist of de affiliate-uitnodiging in BFCM mag (concurreert met 70% off). API: ja.

**K3. 56%-banners, "100-DAY TRIAL" en "Lifetime" in 9 live oude mails** (1.3). ~26.000 mails per week. Omzet: geen directe winst, wel risico (claim in strijd met DECISIONS, verwarring met 70% off). Moeite S. Vóór 1 nov: ja. API: de flowkopie van de template aanpassen kan met `update_email_template` als de key templates mag schrijven (PLAYBOOK 9 noemde alleen lezen); anders in de UI het bannerblok weghalen. Alternatief: UEfh4h en YyaMjx op Draft, FTL de 4 resterende op Draft.

**K4. $0-orders lopen Placed Order-flows in.** Geen `$value > 0`-triggerfilter in X3ySuU, UyFc78, VTkxFL, XbYT7T, YyaMjx, UEfh4h. ~120 samples per week. Gevolg: P3-code, winbackcode op dag 45, VIP (een sample telt als tweede order) en een jubileummail naar TikTok-creators. Omzet: geen winst, wel minder kortinglek en schonere cijfers. Moeite S (6 keer hetzelfde filter). Vóór BFCM: ja, liefst vóór 8 nov (eerste VIP). API: **nee, triggerfilter alleen in de UI**. Bij VIP ook het profielfilter "Placed Order equals 2" uitbreiden met `$value > 0`.

**K5. FREE E-GUIDE dubbel met P1.** 1.420 mails per week, $490 per week toegeschreven, maar P1-FIRST levert dezelfde e-guide. Advies: na een check dat de P1-link werkt YyaMjx op Draft (spaart ~1.400 mails en een deel van de uitschrijvingen). Verwacht omzetverlies klein (toeschrijving op dezelfde order als P1). Moeite S. API: ja (status). Floris beslist.

**K6. Dode flows: Wn2tsq (statisch julisegment) en UYALJ8 (gift card zonder instroom).** Wn2tsq op Draft (API, S). UYALJ8: productnaam in Shopify nakijken en triggerfilter aanpassen (UI), want in december is dit de cadeauflow (4.14).

**K7. Site abandonment ingestort.** VLGhbR van 329 naar ~60 mails per dag sinds 14 okt bij gelijk Active on Site-volume (25.221 events, 17.673 uniek). Al gesignaleerd in 03-browse-site; oorzaak nog niet gevonden. Terug naar ~150 per dag = ~600 extra mails per week x $0,33 (19 okt) = ~$200 per week. Moeite S (filters nalopen). API: lezen ja, filter wijzigen alleen in de UI.

**K8. Draft YuejJ9 overlapt Mystery Gift.** Niet live zetten zonder triggerfilter "geen Mystery Gift in de order" of zonder koppeling aan M3. Geen kosten, wel een besluit.

### Ontbrekend

**4.1 Vangnet checkout en cart via Triple Pixel en Elevar.** Volume (19 okt, één meetdag): 48 checkout-verlaters en 65 cart-verlaters per dag die Klaviyo niet ziet. Per week na filters: ~170 checkout en ~230 cart. Omzet: 170 x $4,13 x 50% + 230 x $1,91 x 50% = **$570 tot $1.200 per week** (bovenkant met het BFCM-verkeer). Moeite S (checkout, kloon QUBUQV met trigger RtgBgs en dedupe zoals QNZyEb), M (cart, andere eventvorm, filter tegen gifts). BFCM: ja, vóór 10 nov. API: ja (`POST /api/flows` als Draft). Let op: v4-regel "geen Triple Pixel-triggers" is met QNZyEb al losgelaten; dezelfde dedupe gebruiken.

**4.2 SMS-flows (welkom, checkout, cart).** 1.760 nieuwe SMS-inschrijvers per week, 0 flows. Welkom-SMS: 1.760 x $0,50 tot $1,00 = $880 tot $1.760. Checkout- en cart-SMS: aanname 8% van ~2.800 checkout-starters per week heeft SMS-toestemming, 220 x $3 x 50% = ~$330. **$1.200 tot $2.100 per week**, min SMS-kosten. Moeite M (copy, compliance, quiet hours, afstemming met wie de SMS-campagnes doet). BFCM: ja als het vóór ~10 nov live is; SMS is het snelste kanaal voor early access en Cyber Monday. API: flow als Draft met `send-sms`-acties waarschijnlijk via `POST /api/flows`; eerst met één testflow bevestigen, anders UI. Floris: SMS in flows ja/nee, wie beheert SMS.

**4.3 BFCM vroege toegang en "sale ended".** (a) Lijst "BFCM early access" plus 3 mails (bevestiging, 24 uur vooraf, start). (b) "Sale ended / last chance" voor wie een BFCM-campagne klikte en niet kocht: segmenttrigger "Clicked Email met campagnenaam BFCM in 3 dagen, Placed Order 0 in 3 dagen". Volume: bij ~5.000 opgaven en ~8.000 BFCM-klikkers zonder order. Omzet: **$1.000 tot $3.000 per week** in de twee BFCM-weken (aanname 3% koopt x $250 x 20 tot 40% incrementeel). Moeite S voor de flows, M met opgavepagina of Alia-kaart. BFCM: kern, start uiterlijk 5 nov. API: ja (lijst- of segmenttrigger). Overlap met W5-test Q2 in 00-plan: kies één. Floris: datum vroege toegang en wat de lijst krijgt.

**4.4 Price drop.** De sale verlaagt echte Shopify-prijzen (zie 03-browse-site: Deep Pan Pro $305 naar $119), dus een catalogus-prijsdaling werkt. Volume: ~8.000 unieke Klaviyo-bekijkers per week, na filters ~30% = 2.400 bij een daling (1 nov naar 70%, en Black Friday). Omzet: 2.400 x $0,60 x 50% = **$500 tot $1.500 per week in de weken met een prijsdaling**, verder ~0. Moeite S tot M. BFCM: ja, alleen als de trigger vóór de daling van 1 nov of uiterlijk die van Black Friday aanstaat. API: **nee**, de Price Drop-trigger bestaat nog niet als metric en moet in de UI aangezet worden (catalogus-instelling); daarna kan de flow in de UI.

**4.5 Post-BFCM-heractivatie.** Twee groepen: BFCM-klikkers zonder order (na 1 dec) en BFCM-kopers. De kopers zitten al in post-purchase; voor de klikkers is er niets tot de campagnes. Een flow "1 dec: wie klikte maar niet kocht, één mail na 5 dagen met een eerlijk vervolg (gifts, garantie, geen nep-verlenging)". Omzet: $300 tot $800 per week in december. Moeite S. BFCM: bouw vóór 20 nov, start 2 dec. API: ja.

**4.6 Bestaande klanten: anniversary en VIP terugwerkend.** XbYT7T en VTkxFL starten alleen op orders na 8 okt. Het cohort november 2025 (14.045 kopers) wordt in november één jaar klant, midden in BFCM. VIP mist iedereen die een tweede order had vóór 9 okt. Volume: ~3.500 per week in november (jubileum), ~100 per week VIP-backfill. Omzet: 3.500 x 60% bereikbaar x $0,50 = **~$1.000 per week**, plus VIP ~$100 tot $250; samen **$700 tot $1.500 per week** in november. Moeite M (veld `first_order_date` in `sync_owned.py`, datumtrigger). BFCM: ja als het vóór ~12 nov staat; anders als campagne (kopersreeks, 00-plan test 1). API: ja voor een nieuwe flow op een datumeigenschap of segment.

**4.7 Cross-sell deksel dag 30 tot 35.** ~1.000 pankopers per week, ongeveer de helft zonder deksel. Omzet: 500 x $0,50 = **$200 tot $450 per week**. Moeite S. BFCM: laag tot middel. T15 (dekselkaart in P1) dekt een deel; eerst T15 meten. API: ja (nieuwe flow) of tak in X3ySuU via UI.

**4.8 Collectie-browse en zoeken.** 1.700 unieke collectiebekijkers per week, waarvan een deel geen product bekijkt; 150 zoekers. Omzet: **$80 tot $150 per week**. Moeite S. API: ja als losse flow, of als extra trigger in VLGhbR (UI). BFCM: middel.

**4.9 Back in stock opfrissen.** Werkt ($3,02, 147 mails). Alleen de template is oud. **$50 tot $150 per week** extra. Moeite S. API: template.

**4.10 Hoge-waarde cart.** In TZG9Mx geen split op waarde. Carts boven $300 (sets) krijgen dezelfde K-mails als een losse pan. Tak met termijnen (Affirm, Shop Pay Installments, bevestigd 7 okt) of een notitie van Benjamin. Omzet: **$100 tot $300 per week**. Moeite S. API: nee voor een split in de live flow (UI); T23 (00-plan) is dezelfde gedachte voor alle carts.

**4.11 Garantieregistratie.** Geen. Waarde zit vooral in data (kookstijl, verjaardag) en vertrouwen. Omzet direct ~$0. Moeite M (pagina of form). Na BFCM.

**4.12 Zorg en educatie.** P1, P2 en P2-SAFE dekken het, maar P2 hangt aan de bezorgtrigger (K1). Cutting Board-tak is weg (~100 plankorders per week). **$30 tot $80 per week**. Moeite S. Na BFCM.

**4.13 Cadeau-flow Q4.** UYALJ8 krijgt niemand; er is geen tak voor cadeaukopers (verzendadres anders dan factuuradres) en geen "laatste besteldag voor de feestdagen" voor browse en cart. Omzet: **$200 tot $600 per week** in december. Moeite M. BFCM: na Cyber Monday, start 2 dec. API: ja (nieuwe flow), split op adres in de UI controleren.

**4.14 Na een negatieve ervaring of ticket.** 2.022 tickets en 158 CSAT-surveys in 14 dagen; reviews komen niet in Klaviyo. Een "we zijn er nog"-mail na een opgelost ticket met lage CSAT, en uitsluiting van marketing tot het ticket dicht is. Omzet ~$0, minder uitschrijvingen en betere reviews. Moeite M. Na BFCM. API: ja.

**4.15 Proactieve vertraging en deelzending.** 1.950 deelzendingen en ~140 OutOfStock-meldingen per week. Twee transactionele mails (deelzending heads-up op ShipBob Shipped plus Fulfilled Partial Order, "we wachten op voorraad" op OutOfStock). Omzet ~$0, wel minder "waar is de rest"-tickets en refunds in de BFCM-drukte. Moeite S tot M (eventvorm ShipBob nalopen, WjhwUa bestaat als Draft). BFCM: ja, vóór 20 nov. API: ja. Floris: tekst over levertijd.

**4.16 Replenishment strips voor losse kopers.** ~60 betaalde strip-orders per week buiten de abonnementen. Herinnering na ~25 dagen ("pak van 10 vellen"). **$50 tot $150 per week**. Moeite S. Afstemmen met YwsKcf M3 en draft YuejJ9. API: ja.

**4.17 Recharge-lifecycle.** ~57 starts en ~13 tot 18 opzeggingen per week, 3 mislukte betalingen. Drie mails: welkom abonnee (hoe beheren, eerste levering), mislukte betaling (Recharge stuurt mogelijk zelf; nagaan), opzegging (één mail met vraag waarom en een eerlijke "pauzeer in plaats van stoppen"). Omzet: **$50 tot $150 per week** nu, groeit met elke Mystery Gift-cohort; de opzegratio (~20% van de starts in negen dagen) is het signaal. Moeite S. BFCM: middel. API: ja (Recharge-metrics bestaan).

---

## 5. Geprioriteerde lijst

Volgorde = impact x haalbaarheid vóór BFCM. Per week = extra omzet in november, schatting.

| # | Wat | Type | Volume per week | Extra per week | Moeite | Vóór BFCM | API of UI |
|---|---|---|---|---|---|---|---|
| 1 | **56%-banners, 100-day en lifetime uit 9 live oude mails** (K3) | kapot | ~26.000 mails | risico, geen omzet | S | ja, vóór 1 nov | UI, of API als templates:write |
| 2 | **Triggerfilter `$value > 0` in 6 Placed Order-flows**, ook VIP-telling (K4) | kapot | ~120 samples | kortinglek eruit | S | ja, vóór 8 nov | alleen UI |
| 3 | **Vangnet checkout en cart via Triple Pixel en Elevar** (4.1) | ontbreekt | ~400 verlaters | $570 tot $1.200 | S/M | ja, vóór 10 nov | API (Draft) |
| 4 | **SMS-welkom en checkout/cart-SMS** (4.2) | ontbreekt | 1.760 inschrijvers | $1.200 tot $2.100 | M | ja, als besluit vóór 3 nov | API waarschijnlijk, anders UI |
| 5 | **BFCM vroege toegang en "sale ended"** (4.3) | ontbreekt | ~5.000 opgaven, ~8.000 klikkers | $1.000 tot $3.000 (BFCM-weken) | S/M | ja, start uiterlijk 5 nov | API |
| 6 | **Anniversary en VIP voor bestaande klanten** (4.6) | ontbreekt | ~3.600 | $700 tot $1.500 (nov) | M | ja, vóór 12 nov, anders campagne | API (nieuwe flow) |
| 7 | **Affiliate S1 naar trigger "Enrolled through purchase"** (K2) | kapot | 36 per 14 d naar ~1.000 | $100 tot $300 | S | ja | API (kloon als Draft) |
| 8 | **Price drop aanzetten** (4.4) | ontbreekt | ~2.400 per daling | $500 tot $1.500 (dalingsweken) | S/M | ja, vóór 1 nov of vóór Black Friday | alleen UI |
| 9 | **Proactieve deelzending en vertraging** (4.15) | ontbreekt | ~2.000 | minder tickets | S/M | ja, vóór 20 nov | API |
| 10 | **Recharge-lifecycle, en YuejJ9 niet los live** (4.17, K8) | ontbreekt | ~75 | $50 tot $150, groeit | S | ja | API |
| 11 | Site abandonment-bereik terug (K7) | kapot | +600 mails | ~$200 | S | ja | UI |
| 12 | FREE E-GUIDE op Draft (K5) | dubbel | -1.400 mails | ~$0 netto | S | ja | API (status) |
| 13 | Post-BFCM-heractivatie klikkers (4.5) | ontbreekt | ~5.000 | $300 tot $800 (dec) | S | bouwen vóór 20 nov | API |
| 14 | Hoge-waarde cart-tak (4.10) | ontbreekt | ~150 | $100 tot $300 | S | ja | UI |
| 15 | Wn2tsq op Draft, UYALJ8-trigger repareren (K6) | dood | 0 | (dec) | S | ja | API / UI |
| 16 | Dekselmail dag 32 (4.7) | ontbreekt | ~500 | $200 tot $450 | S | na T15 | API |
| 17 | Cadeau-flow en laatste besteldag (4.13) | ontbreekt | | $200 tot $600 (dec) | M | start 2 dec | API |
| 18 | Collectie- en zoektak (4.8), BIS-template (4.9), strips-herinnering (4.16) | ontbreekt | | $180 tot $450 samen | S | ja | API / UI |
| 19 | Na negatief ticket (4.14), garantieregistratie (4.11), zorg/planktak (4.12) | ontbreekt | | ~$0 tot $80 | M | na BFCM | API |

**Optelsom 3 tot en met 10:** ongeveer $4.100 tot $9.800 per week in de BFCM-weken, buiten november $2.500 tot $5.000. Nummers 1 en 2 leveren geen omzet maar halen risico weg en moeten eerst.

**Volgorde voor de komende dagen.** 29 tot 31 okt: 1, 2 en 8 (UI, samen ongeveer een uur; 8 moet vóór de daling van 1 nov). 1 tot 5 nov: 3, 5, 7 en 10 als Draft via de API, live na akkoord; besluit over 4. 5 tot 12 nov: 4, 6 en 9. Vanaf 20 nov bevriezing (00-plan): 13 en 17 klaarzetten voor 2 dec.

**Floris beslist:** SMS in flows (ja/nee, wie beheert); datum vroege toegang en wat de lijst krijgt; mag de affiliate-uitnodiging in BFCM doorlopen; FREE E-GUIDE uit; welke tekst over levertijd in de vertragingsmail; wie heeft YuejJ9 gebouwd en hoe verhoudt hij zich tot Mystery Gift.

---

## 6. Bronnen en beperkingen

- Klaviyo-API, account TdtTzz, 28 okt 2026: 110 flows met definitie, 184 metrics met aantallen over 14 dagen, Received Email per flow per dag, 3.286 Placed Order-events met attributie, segmenten YbCB68, WuHSm6, YxfuJT, HTML van 13 live oude mails.
- Recharge: 124 actieve abonnementen op 27 okt, opzeggingen per week. Aftersell: upsellomzet 14 tot 27 okt ~$36.000.
- Repo: research/flows-audit/2026-10-19-ontbrekende-flows.md en -uitbreiden.md, research/ab-tests-q4/00 tot 05, research/afmeldingen/01 en 02, research/lijstkwaliteit/01, research/concurrenten/overzicht.md, klaviyo/flows/v4-flow-system.md en mystery-gift-v3.md, LOG.md.
- Externe benchmarks: [Klaviyo 2024 Benchmark Report](https://resources.klaviyo.com/2024-benchmark-report), [Darkroom: flow-level benchmarks 2026 (replenishment $2 tot $5)](https://www.darkroomagency.com/observatory/email-marketing-benchmarks-ecommerce-2026), [Eightx: flow revenue benchmarks](https://eightx.co/blog/average-klaviyo-flow-revenue-contribution-benchmarks), [ClickMinded: SMS benchmarks 2026](https://www.clickminded.com/sms-marketing-benchmarks/), [InboxAlly: Klaviyo benchmarks](https://www.inboxally.com/blog/klaviyo-email-benchmarks), [HexClad warranty (registratie)](https://hexclad.com/warranty). Email Love: [HexClad](https://emaillove.com/authors/hexclad-cookware), BFCM early access-voorbeelden van oktober 2026 (Lola Blankets, Kitsch, Inside Weather, DUSK), price drop-voorbeelden (OFFICE, LOFT).
- Beperkingen: attributie is last touch in het Klaviyo-venster en overschat incrementele omzet. Unieke ontvangers per week zijn opgeteld, dus licht te hoog. Vangnetvolumes rusten op één meetdag (17 okt). Klaviyo logt geen overgeslagen flowstappen, dus waar staat "na filters" is het een schatting. Of `send-sms` in `POST /api/flows` werkt, is niet getest.
