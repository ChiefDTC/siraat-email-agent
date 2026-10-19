# Audit: ontbrekende flows en gemiste omzet (19 okt 2026)

Opgesteld 19 oktober 2026, 18:00 UTC. Alles is alleen gelezen: Klaviyo-API (`GET /api/flows` met definities voor alle 97 flows, `GET /api/metrics` met metric-aggregates over 30 dagen, flow- en campaign-values-reports, events van één volle dag voor de overlap per signaalbron) en de repo. Niets gewijzigd in Klaviyo, Shopify of andere tools. Geen kortingscodes of sleutels in dit stuk.

Periodes: **voor** = 28 sep 00:00 tot 8 okt 22:29 UTC (10,94 dagen), **na** = 8 okt 22:29 tot 19 okt 18:03 UTC (10,82 dagen). Omzet = Klaviyo-attributie op Placed Order (RSNxYV), standaardvenster. Bedragen per dag = periode-omzet gedeeld door het aantal dagen.

---

## 0. Samenvatting voor Floris

1. **Flows leveren na de livegang minder per dag op terwijl de winkel groeit.** Flows: $4.687 per dag voor, $4.478 na (-4,5%). Winkelomzet (Placed Order): $43.481 per dag (28 sep tot 8 okt) tegen $46.948 (9 tot 18 okt, +8%). Flow-aandeel zakt van 10,8% naar 9,5%. Bij een gelijk aandeel had het $5.060 per dag moeten zijn: **ongeveer $580 per dag, $17.000 per maand achter.**
2. **Welcome en checkout zijn beter** (welcome +$664 per dag, checkout +$64). **Browse (-$573), cart (-$146) en de oude naflows (-$182) trekken het omlaag.**
3. **Belangrijkste nuance bij browse:** de nieuwe Triple Pixel-arm QNZyEb (vandaag gebouwd door een andere agent) haalt naar verwachting 40 tot 70 mails per dag. De oude TyEjuQ stuurde er 522 per dag, maar 75% daarvan ging naar mensen die ook al de Shopify-browsemail kregen. Het grootste deel van de $549 per dag was dus een **tweede browse-aanraking**, geen extra publiek. QNZyEb herstelt ongeveer $40 tot $80 per dag. Het gat van $400 tot $500 per dag zit in het **bereik van v4 Browse** (379 ontvangers per dag tegen 1.044 voor beide oude flows samen) en in het ontbreken van een tweede mail voor wie B1 niet opent.
4. **Een derde signaalbron staat ongebruikt: Elevar** (server-side). Op 17 okt zagen Triple Pixel en Elevar samen 380 productbekijkers, 65 cart-verlaters en 48 checkout-verlaters die Klaviyo zelf niet zag en die niet kochten. Daar hangt geen enkele flow aan.
5. **SMS heeft geen enkele flow.** SMS-campagnes doen $0,28 per ontvanger (e-mailcampagnes $0,066), er komen 1.200 tot 1.900 SMS-inschrijvers per maand bij, en toch geen welkom-SMS en geen checkout-SMS.
6. **Bestaande klanten vallen buiten VIP, Anniversary en (straks) Winback.** Die drie v4-flows starten op Placed Order na 8 okt. De 14.045 kopers van november 2025 worden in november 2026 één jaar klant, midden in BFCM, en krijgen niets.
7. **Live oude flows dragen nog verkeerde claims**: alle 10 Failure-to-launch-mails "PRIME TIME SALE / UP TO 56% OFF", 5 ervan "100-DAY TRIAL", 1 "lifetime"; ook de 4 winback-mails UEfh4h en de e-guide YyaMjx. Dat is in strijd met DECISIONS (30 dagen retour, 75 jaar garantie) en botst vanaf 1 november met "70% off".

Top 10 met eerste stap en besluit: sectie 5.

---

## 1. Inventaris

### 1.1 Live flows (23)

Omzet per dag in de periode voor / na. "n.v.t." = had nog geen ontvangers (lange wachttijd of nieuw).

| ID | Naam | Status | Trigger | Ontv. voor | Omzet voor ($/dag) | Ontv. na | Omzet na ($/dag) |
|---|---|---|---|---|---|---|---|
| T4a5Mk | v4 · Welcome | live | lijst Uw8eZG | 150 | 0 | 17.578 | **2.326** |
| QUBUQV | v4 · Checkout abandonment | live | Checkout Started (Shopify, RfMvni) | 37 | 0 | 2.381 | **839** |
| TZG9Mx | v4 · Cart abandonment | live | Added to Cart (Shopify, QXcV8K) | 24 | 25 | 3.235 | **409** |
| WdRz5k | v4 · Browse abandonment | live | Viewed Product (Klaviyo onsite, XNtYMB) | 132 | 0 | 4.098 | **258** |
| X3ySuU | v4 · Post-purchase | live | Placed Order | 15 | 0 | 2.014 | 203 |
| VQ93sx | v4 · Post-purchase · levering | live | Delivered Shipment (VcUF33) | 0 | 0 | 850 | 48 |
| VLGhbR | v4 · Site abandonment | live | Active on Site (UdCdLD) | 48 | 0 | 2.194 | 67 |
| TbYQmX | v4 · Sunset | live | segment WuHSm6 | 0 | 0 | 9.180 | 41 |
| Wzz6xC | v4 · Sunset · kept | live | segment YxfuJT | 0 | 0 | 25 | 14 |
| VPixnJ | v4 · UGC first egg | live | Delivered Shipment + 4 d | 0 | 0 | 451 | 0 |
| UyFc78 | v4 · Winback | live | Placed Order + 45 d | 0 | 0 | 0 | n.v.t. (eerste mail rond 23 nov) |
| VTkxFL | v4 · VIP | live | Placed Order, precies 2 orders, + 30 d | 0 | 0 | 0 | n.v.t. (eerste mail rond 8 nov) |
| XbYT7T | v4 · Anniversary | live | Placed Order, 1e order cookware, + 182 d | 0 | 0 | 0 | n.v.t. (eerste mail april 2027) |
| XzHrez | Review request · Delivered +14d | live | Delivered Shipment + 14 d | 0 | 0 | 0 | n.v.t. (eerste mail 20 okt) |
| T2SmtR | EB · Failure to launch | live | lijst Uw8eZG + 30 d | 41.739 | 163 | 34.195 | 118 |
| UEfh4h | EB · Customer Winback (oud, tot 14 dec) | live | Placed Order + 60 d | 6.409 | 103 | 5.253 | 62 |
| YyaMjx | FREE E-GUIDE | live | Placed Order | 1.837 | 25 | 1.846 | 53 |
| WsQDYu | BIS · Back in Stock | live | Subscribed to Back in Stock (T4dnSM) | 27 | 20 | 109 | 41 |
| UYALJ8 | EB · E-Gift Card | live | Placed Order met E-Gift Card | 0 | 0 | 0 | 0 |
| Wn2tsq | EB · Pan Flash Buyers | live | segment YbCB68 | 0 | 0 | 0 | 0 |
| TLHht3, UcGzaL, Y4a7fJ | CS-meldingen (exception, attempt failed, pickup) | live | Postflows 6, 7, 8 | intern | | intern | |

### 1.2 Bij de livegang (8 okt 22:29) op Draft gezet

| ID | Naam | Trigger | Ontv. voor | Omzet voor ($/dag) | Vervanger | Omzet vervanger na ($/dag) |
|---|---|---|---|---|---|---|
| SiaNLu | EB Welcome | lijst Uw8eZG | 24.814 | 1.662 | T4a5Mk | 2.326 |
| Y2TmNB | EB Checkout | Checkout Started | 2.129 | 619 | QUBUQV | 839 (samen met Tsg2tV) |
| Tsg2tV | EB Checkout · Triple Pixel | Checkout Started - TP (RtgBgs) | 1.233 | 156 | **geen** | |
| SwkMyn | EB Cart | Added to Cart | 3.710 | 555 | TZG9Mx | 409 |
| TBWngE | EB Cart · Triple Pixel | Added to Cart - TP (SZNHJK) | 471 | 0 | **geen** | |
| Wj6x6V | EB Browse | Viewed Product | 5.708 | 349 | WdRz5k | 258 (samen met TyEjuQ) |
| TyEjuQ | EB Browse · Triple Pixel | Viewed Product - TP (V48nhq) | 5.711 | 549 | QNZyEb (concept, 19 okt) | 0 |
| RL3TU6 | EB Post Purchase | Placed Order | 7.286 | 137 | X3ySuU + VQ93sx | 251 (samen) |
| TSUnLs | EB E-Book | Placed Order | 2.585 | 171 | YyaMjx (blijft) + P1 | zie boven |
| YcXbHx | EB Pan Education (incl. Cutting Board-tak) | Postflows In Transit | 2.608 | 153 | P1, P2, P2-SAFE, U1; **board-tak zonder vervanger** | |
| WvRupU | Mystery Gift Reveal | Ordered Product (dood product-ID) | 492 | 0 (dood sinds 21 sep) | Mystery Gift v3 (concept) | |
| S7V4a7 | EB Sunset | segment XY4NVp | 2.403 | 0 | TbYQmX + Wzz6xC | 55 |
| SxN86d | Middle East delay | Placed Order | 11 | 0 | bewust geen | |
| Vixr6X | Trustpilot 4 emojis (uit 12 okt) | segment Yx4ain | 473 | 0 | XzHrez (eerste mail 20 okt) | |

### 1.3 Overige drafts (60)

13 TEST v5-klonen, 10 oude EB-versies (Browse/Cart/Checkout 2025, Post Purchase 5/5/25, Welcome Ramadan, FREE E-GUIDE FLOW), 7 Postflows-flows, 7 Wonderment/ParcelPanel-varianten (Carrier Picked Up, Attempted Delivery, Shipment Created, Fulfillment Delayed, Out for Delivery, Shipment Delivered, Shipment Out for Delivery met 1 SMS), 5 HKT-flows, 7 "X Farooq"-flows (o.a. Active on site en Product Review / Cross Sell), 6 FLORIS-orderupdates, Split Shipment heads-up (WjhwUa, ShipBob Shipped), Review Email (trustpilot), Trustpilot Email Updated FL, 2 lege flows. Geen ervan heeft een trigger die nu nergens anders gedekt is, behalve **Split Shipment heads-up** en **Fulfillment Delayed** (zie 4.12).

### 1.4 Totaal

| | Voor | Na |
|---|---|---|
| Flowomzet per dag | $4.687 | $4.478 |
| Winkelomzet per dag (Placed Order) | $43.481 | $46.948 |
| Flow-aandeel | 10,8% | 9,5% |
| Ter vergelijking, 30 dagen campagnes | e-mail $117.499 op 1,79 mln ontvangers ($0,066) | SMS $11.347 op 40.178 ontvangers ($0,28) |

---

## 2. Gaten door de livegang

Per gat: wat er wegviel, wat het nu kost per dag, en hoeveel daarvan echt terug te halen is. Echt extra publiek is gemeten op zaterdag 17 oktober (alle events van die dag, unieke profielen, zonder order die dag).

| # | Gat | Wat voor de livegang | Nu | Verlies $/dag (gemeten) | Terug te halen $/dag (schatting) | Hoe |
|---|---|---|---|---|---|---|
| G1 | **Browse-bereik v4** | Wj6x6V + TyEjuQ: 1.044 ontvangers per dag, $898 | WdRz5k + site: 379 + 203 per dag, $325 | **-573** | **300 tot 450** | QNZyEb (TP-arm) dekt maar 40 tot 70 per dag. De rest: profielfilters van WdRz5k naast Wj6x6V leggen (Homestead zag 267 tegen 833 per dag), en een tweede mail (B1b, 24 uur later, alleen niet-openers) |
| G2 | Browse Triple Pixel TyEjuQ | 522 ontvangers per dag, $549 (laatste aanraking) | 0 (QNZyEb nog Draft) | deel van G1 | 40 tot 80 | QNZyEb live na de UI-stap aan de kliksplit; 250 TP-only bekijkers per dag, waarvan ~40 tot 70 alle filters halen |
| G3 | **Elevar-signalen (nooit gebruikt)** | geen | geen | 0 (was er nooit) | 60 tot 120 | 130 extra bekijkers, 20 extra checkout-verlaters per dag bovenop TP. Vangnet-armen met trigger Elevar (zie 3) |
| G4 | Checkout Triple Pixel Tsg2tV | 113 ontvangers per dag, $156 | 0 | -156 (maar checkout totaal +64) | 70 tot 110 | 48 checkout-verlaters per dag zonder Shopify-event (TP 28, Elevar 20 extra). x 50% bereikbaar x $3,81 (QUBUQV na) |
| G5 | Cart | SwkMyn 339 per dag, $555 | TZG9Mx 300 per dag, $409 | **-146** | 40 tot 100 | 65 extra cart-verlaters per dag via TP/Elevar (x 50% x $1,37 = $45); plus het lagere bereik van TZG9Mx onderzoeken (90/10-split zit erin) |
| G6 | Naflows (E-Book, Pan Education, Post Purchase) | $461 per dag | X3ySuU + VQ93sx + YyaMjx $304 | **-182** (deels toeval: TSUnLs $1.874 uit 3 orders) | 30 tot 60 | Deels attributie op herhaalorders. Echte gaten: de Cutting Board-tak (~170 mails per maand, moest volgens plan 11 blijven, staat nu op Draft) en de mystery-gift-onthulling (G8) |
| G7 | Reviewverzoeken | Vixr6X tot 12 okt | XzHrez stuurt pas vanaf 20 okt | 0 directe omzet | | 8 dagen zonder verzoek; backfill (lijst UXBmYd, 253) loopt via een andere agent |
| G8 | Mystery Gift Reveal WvRupU | dood sinds 21 sep (90 d tot dan: $4.293) | 0 | ~-48 sinds 21 sep | 50 tot 100 | Mystery Gift v3 (concept klaar, klaviyo/flows/mystery-gift-v3.md) |
| G9 | Winback bestaande klanten | UEfh4h, 60 d, $103 per dag | $62, stopt 14 dec; v4 pas vanaf ~23 nov voor nieuwe kopers | -41 nu, na 14 dec ~-60 | zie 4.6 | Geen winback voor klanten van vóór 9 okt na 14 dec, en geen 90/180-dagen-stap |

**Optelsom echt terug te halen: ongeveer $590 tot $1.020 per dag (zonder G9), dus $18.000 tot $30.000 per maand.** Dat is ruim het gemeten tekort van $580 per dag; het verschil komt van Elevar en checkout-TP, die er voor de livegang ook al niet (of half) waren.

---

## 3. Events zonder flow

30 dagen (19 sep tot 19 okt), aantallen events. Vetgedrukt = kansrijk.

| Metric (ID) | Bron | 30 d | Flow nu | Oordeel |
|---|---|---|---|---|
| **Added to Cart - Triple Pixel** (SZNHJK) | Triple Whale | 68.521 | geen (TBWngE uit) | vuurt ook op de automatische gifts; 17 okt: 148 profielen zonder Shopify-ATC, 45 zonder order of checkout. Vangnet met triggerfilter tegen gifts |
| **Viewed Product - Triple Pixel** (V48nhq) | Triple Whale | 61.657 | QNZyEb (Draft) | 250 extra bekijkers per dag |
| **Viewed Product - Elevar SS** (VPgSUk) | Elevar | 58.082 | **geen** | 248 bekijkers per dag zonder Klaviyo-event; met TP samen 380 |
| **Active on Site - Triple Pixel** (TfGuLV) | Triple Whale | 57.671 | geen | 301 actieve profielen per dag zonder Klaviyo-Active on Site; als tweede trigger in VLGhbR |
| **Added to Cart - Elevar SS** (U2QZpR) | Elevar | 44.866 | **geen** | 61 per dag zonder Shopify-ATC en zonder order |
| **Viewed Collection** (XkJTYh) | Shopify | 17.746 | geen | 95 profielen per dag bekeken een collectie maar geen product; tak in site abandonment |
| ParcelPanel / ParcelWILL status (RN4Tk4, WYXGCn) | ParcelWILL | 17.874 elk | geen | 3PL stuurt tracking al; niet nodig |
| Fulfilled Partial Order (UHUr2m) | Shopify | 8.805 | geen | deelzendingen; tickets "waar is de rest" (4.12) |
| **Begin Checkout - Elevar SS** (WshVwX) | Elevar | 3.402 | **geen** | 39 per dag zonder Shopify-Checkout Started |
| **Checkout Started - Triple Pixel** (RtgBgs) | Triple Whale | 4.296 | geen (Tsg2tV uit) | 28 per dag zonder Shopify-event |
| Opened Ticket / Resolved Ticket (YzvjGf, SzcCyb) | Gorgias | 3.735 / 3.201 | alleen als filter | goed zo |
| **Subscribed to Text Messaging Marketing** (WQVUMq) | Klaviyo | 2.500 (okt tot nu 1.864) | **geen SMS-flow** | 4.2 |
| ShipBob OutOfStock (TKx6c4) | ShipBob | 808 | geen | orders die niet kunnen vertrekken; proactieve vertragingsmail (4.12) |
| Submitted Search (YeVVus) | Shopify | 441 | geen | klein; meenemen in site abandonment |
| Coupon Assigned (XUMYt7) / Coupon Used (USRsNP) | Klaviyo | 362 / 1 | n.v.t. | Coupon Used vuurt niet meer sinds juli; niet op bouwen |
| Gorgias Completed Survey (Wa4pz9) | Gorgias | 265 | geen | tevreden klanten (CSAT 4 tot 5) naar review/referral, laag volume |
| Refunded Order (Xg6cwn) / Cancelled (TFervq) | Shopify | 111 / 66 | alleen als filter | feedbackmail, laag |
| Subscribed to Back in Stock (T4dnSM) | Klaviyo | 104 | WsQDYu | gedekt (oude template) |
| Recharge: Subscription started 9, upcoming 17, cancelled 5, charge failed 4 | Recharge | | geen | klein; groeit pas als Mystery Gift v3 werkt |
| Alia Reward Claimed, Meta Filled Out Lead Ad, alle Klaviyo-form-events | Alia, Meta, Klaviyo | 0 | | Alia stuurt geen events; pop-upvarianten zijn niet meetbaar in Klaviyo |
| Wonderment-, TrackBee-, Zendesk-metrics | | 0 | | dode koppelingen |
| Okendo, Loox, Trustpilot | | geen metric | | reviews komen niet in Klaviyo; geen review-gebaseerde flows mogelijk zonder koppeling |

---

## 4. Ontbrekende flows ten opzichte van best practice

Uitgangspunten voor de schattingen: AOV na livegang ~$229 (winkelomzet / orders 9 tot 18 okt), RPR uit onze eigen v4-flows na de livegang (browse $0,68, cart $1,37, checkout $3,81, site $0,33, welcome $1,43), een "incrementeel"-factor van 50% waar een flow mensen raakt die ook campagnes krijgen. Benchmarks Klaviyo: abandoned cart gemiddeld $6,77 per ontvanger in e-mail en $4,48 in SMS (Klaviyo 2026); back in stock gemiddeld $9,14 (Eightx); browse $0,95 gemiddeld, top 10% $7,05. Alles is een orde van grootte, geen belofte.

Effort: S = een dag of minder (kloon of tak, bestaande templates), M = 2 tot 5 dagen (nieuwe mails of data), L = meer dan een week of een nieuwe app.

### 4.1 Signaal-vangnet per bron (browse, cart, checkout, site)
- **Waarom**: Klaviyo's eigen onsite-script mist een kwart van de bekijkers (adblock, Safari ITP). Triple Pixel en Elevar zien ze wel. Zie sectie 2 en 3.
- **Trigger**: per flow een extra arm (of kloon) met trigger V48nhq/VPgSUk (browse), SZNHJK/U2QZpR (cart, triggerfilter tegen gifts), RtgBgs/WshVwX (checkout), TfGuLV (site). Dedupe: geen Shopify/Klaviyo-event van hetzelfde type in 1 dag, geen mail uit de hoofdflow in 7 dagen (zoals QNZyEb).
- **Mails**: dezelfde als de hoofdflow (2 browse, 3 cart, 4 checkout, 2 site).
- **Impact**: browse TP 40 tot 80, browse Elevar 30 tot 60, checkout 70 tot 110, cart 40 tot 60, site 20 tot 40 $/dag. **Samen $6.000 tot $10.000 per maand.** Eerst de vorm van de Elevar-events controleren (eigenschapnamen voor productblok).
- **Effort**: S per arm (QNZyEb is het sjabloon), M voor cart (andere eventvorm).
- **BFCM**: hoog. Verkeer verdubbelt in november; elk gemist profiel kost dan twee keer zoveel.

### 4.2 SMS-flows (welkom, checkout, cart)
- **Waarom**: SMS-campagnes doen per ontvanger 4x meer dan e-mail ($0,28 tegen $0,066). 1.200 tot 1.900 nieuwe SMS-inschrijvers per maand krijgen geen welkom. Afmeldingen SMS zijn hoog (2.242 in 30 dagen): een welkom-SMS die de verwachting zet helpt ook.
- **Trigger**: Subscribed to Text Messaging Marketing (welkom); in QUBUQV en TZG9Mx een SMS-tak na C1/K1 voor wie SMS-toestemming heeft.
- **Berichten**: welkom 2 SMS (direct, dag 2), checkout 1 SMS (na 1 uur), cart 1 SMS (na 4 uur), alle binnen quiet hours.
- **Impact**: welkom 1.500 x $1,00 = $1.500; checkout/cart: aanname 8% van de 11.900 checkout-starters per maand heeft SMS-toestemming = 950 x $4,48 x 50% = $2.100. **$3.000 tot $4.500 per maand**, min SMS-kosten (orde $100 tot $200).
- **Effort**: M (copy, TCPA-tekst, quiet hours, afstemming met wie de SMS-campagnes doet).
- **BFCM**: hoog; SMS is het snelste kanaal voor early access en Cyber Monday.

### 4.3 Price drop (catalogus)
- **Waarom**: in BFCM gaan de prijzen naar 70% off. Wie in de 30 dagen ervoor een product bekeek, krijgt automatisch "the pan you looked at is now $X". Klaviyo heeft hier een kant-en-klare trigger voor op de Shopify-catalogus.
- **Trigger**: Price Drop (catalogus), alleen als de prijs in Shopify echt daalt (compare-at plus lagere prijs). Werkt niet als BFCM alleen via een code of automatische korting loopt.
- **Mails**: 1 (eventueel 2: dag 0 en dag 3).
- **Impact**: ~25.000 unieke bekijkers per 30 dagen, 40% bereikbaar na filters = 10.000 x $0,60 x 50% incrementeel = **$3.000 eenmalig in november**, hoger als de daling groot is. Daarna klein.
- **Effort**: S tot M (catalogusvoorwaarde controleren, 1 template).
- **BFCM**: hoog, maar alleen bruikbaar als Floris de BFCM-prijzen als echte prijswijziging zet.

### 4.4 BFCM early access / wachtlijst
- **Waarom**: concurrenten bouwen nu al aanloop (Our Place drempelcadeau, HexClad winactie met deadline). Wie zich vóór 1 nov opgeeft, krijgt de deal een paar uur eerder. Bouwt een warme lijst die we zonder campagne-cap kunnen bereiken.
- **Trigger**: toegevoegd aan een nieuwe lijst "BFCM early access" (Alia-kaart of Klaviyo-form; Klaviyo-forms staan nu allemaal op draft).
- **Mails**: 3 (bevestiging, 24 uur voor start, start early access) plus 1 SMS bij toestemming.
- **Impact**: aanname 5.000 opgaven x 3% koopt x $250 = $37.500 omzet, waarvan 20 tot 40% incrementeel = **$7.500 tot $15.000 over BFCM**.
- **Effort**: S voor de flow, M met form en landingspagina.
- **BFCM**: kern.

### 4.5 Low inventory / "almost gone" (tak in browse en cart)
- **Waarom**: eerlijke schaarste werkt (skill direct response: alleen als het waar is). De 12-delige en 6-delige set hadden negatieve voorraad; in BFCM lopen maten op.
- **Trigger**: conditional split in WdRz5k en TZG9Mx op catalogusvoorraad onder een drempel (Klaviyo-catalogus heeft voorraad, BIS werkt al).
- **Mails**: 1 variant van B1/K2 per flow.
- **Impact**: +5 tot 10% op browse en cart = $35 tot $65 per dag, **$1.000 tot $2.000 per maand**.
- **Effort**: S.
- **BFCM**: hoog.

### 4.6 Bestaande klanten: anniversary, VIP en reactivatie met terugwerkende kracht
- **Waarom**: XbYT7T, VTkxFL en UyFc78 triggeren op Placed Order na de livegang. Van de 98.538 kopers krijgt niemand van vóór 9 okt ooit een jubileum- of VIP-mail, en na 14 dec ook geen winback meer. Cohort november 2025: 14.045 kopers ($3,05 mln) worden in november 2026 een jaar klant; mei 2026 (7.674) wordt zes maanden.
- **Trigger**: datumtrigger op profieleigenschap `first_order_date` (toe te voegen aan het nachtelijke script `sync_owned.py`), of segmenttrigger "1 order, 90 tot 365 dagen geleden, geen order sinds" voor reactivatie; VIP-backfill via segment "precies 2 orders, laatste 30 tot 120 dagen geleden".
- **Mails**: dezelfde als v4 (N1/N2, V1/V2, R1/R2).
- **Impact**: anniversary ~5.000 per maand x 60% bereikbaar x $0,50 = $1.500, in november met het grote cohort ~$4.000; reactivatie ~5.000 per maand x $0,30 = $1.500. **$3.000 tot $5.000 per maand**, piek in nov/dec.
- **Effort**: M (veld in sync_owned, kloon met datumtrigger, overlap met campagnes regelen).
- **BFCM**: hoog voor het november-cohort ("one year with your pan" plus de BFCM-deal).

### 4.7 Replenishment vaatwasstrips (Mystery Gift v3)
- **Waarom**: elke order krijgt de strips; het pak is na ~30 wasbeurten op. De oude onthulling deed $1.430 per maand en is sinds 21 sep dood.
- **Trigger**: Ordered Product 15785445622100 (plus OF op naam "Mystery Gift").
- **Mails**: 4 (dag 3, 12, 23, 30), spec klaar.
- **Impact**: **$1.500 tot $3.000 per maand** plus abonnement-LTV ($20 per maand per abonnee).
- **Effort**: S (alles gebouwd, alleen beelden en klikstappen).
- **BFCM**: middel; BFCM-orders leveren in december een grote groep strip-ontvangers op.

### 4.8 Cross-sell per bezit (deksel, tweede pan)
- **Waarom**: de tweede order is vooral een deksel (1.610) of tweede pan; mediaan 35 dagen. P3 (dag 20) heeft al `xsell`, Winback R1 komt op dag 45. Wat mist: een korte "fit the lid"-mail voor pankopers zonder deksel rond dag 30 tot 35, en accessoires (Our Place doet dit als losse campagne).
- **Trigger**: Placed Order met pan, geen deksel in `siraat_owned`, + 32 dagen.
- **Mails**: 1.
- **Impact**: ~3.500 pankopers per maand x 50% zonder deksel x $0,50 = **~$900 per maand**.
- **Effort**: S (productcard en xsell bestaan).
- **BFCM**: laag tot middel (sets in BFCM hebben al deksels).

### 4.9 Referral
- **Waarom**: geen programma; ontwerp en mails liggen klaar (research/referral).
- **Trigger**: Placed Order + na review 5 sterren; wekelijkse batch.
- **Mails**: 2 (ref1, ref1-review) plus bedankmail.
- **Impact**: ~200 vriendenorders per jaar x $224 = **~$3.700 per maand** (research/potentie).
- **Effort**: M.
- **BFCM**: laag; "give $25" valt weg naast 70% off. Advies: januari.

### 4.10 Collectie-browse en zoekverlating
- **Waarom**: 95 profielen per dag bekijken een collectie zonder product; 441 zoekopdrachten per maand.
- **Trigger**: Viewed Collection en Submitted Search als extra triggertak in VLGhbR (zelfde filters).
- **Mails**: 1 tot 2 (collectie bovenaan, bestsellers).
- **Impact**: 95 x 40% x $0,33 = $13 per dag, **~$400 tot $600 per maand**.
- **Effort**: S.
- **BFCM**: middel (mensen kijken in november per categorie: sets, deals).

### 4.11 Back in stock opfrissen en uitbreiden
- **Waarom**: WsQDYu werkt ($444 op 109 ontvangers, $4 per ontvanger) maar draait op een oude template. Sets met backorder: BIS-knop bij elk uitverkocht product.
- **Trigger**: bestaand.
- **Mails**: 2 (bevestiging, terug) plus 1 herinnering na 48 uur.
- **Impact**: **$300 tot $600 per maand**, in BFCM hoger bij uitverkochte maten.
- **Effort**: S.
- **BFCM**: middel.

### 4.12 Proactieve vertragings- en deelzendingsmail (service)
- **Waarom**: 8.805 deelzendingen en 808 OutOfStock-meldingen per maand, 3.735 tickets. Er liggen draftflows (Split Shipment heads-up, Fulfillment Delayed). In BFCM verdubbelen tickets.
- **Trigger**: ShipBob Shipped met deelzending, ShipBob OutOfStock (na controle van de eventvorm).
- **Mails**: 1 per trigger, transactioneel en kalm.
- **Impact**: geen directe omzet; minder tickets en refunds (111 per maand) en betere reviews.
- **Effort**: S tot M.
- **BFCM**: hoog voor de service.

### 4.13 Kleinere of nu niet mogelijke flows
| Flow | Status | Oordeel |
|---|---|---|
| Gift card: G2-herinnering (14 d) en kerstcampagnes | spec in 09-gift-card.md, flow UYALJ8 alleen bedankmail, 0 verzonden in 30 d | december-campagnes inplannen, flow laag |
| Cadeaukoper-tak (verzendadres anders dan factuuradres) | ontbreekt | in december P2 "is it unwrapped yet?" in plaats van "how's your pan", S, laag $ |
| Refund/annulering feedback | ontbreekt | 111 per maand, laag $ |
| Recharge: start, mislukte betaling, opzegging | ontbreekt | volumes 4 tot 17 per maand; pas na Mystery Gift v3 |
| CSAT-tevreden naar review/referral | ontbreekt | 265 surveys per maand, later |
| Productreviews (Okendo/Loox) en UGC-verzoek met foto | VPixnJ live, $0 | geen reviewevents in Klaviyo; eerst koppeling |
| Verjaardag, wishlist, quiz | geen databron | n.v.t. tot er een veld of app is |
| Cutting Board-tak (YcXbHx) | per ongeluk mee uit | 170 mails per maand, terug als losse flow of tak in X3ySuU, S |
| Pop-upvarianten (exit intent, SMS-stap) | Alia, geen events in Klaviyo | buiten Klaviyo-flows; wel nodig voor 4.4 |

### 4.14 Hygiëne vóór BFCM (geen nieuwe flow, wel geld)
Live oude mails met claims die niet meer mogen of met BFCM botsen:

| Flow | Mails live | Gevonden | Mails per dag |
|---|---|---|---|
| T2SmtR Failure to launch | 10 | "PRIME TIME SALE / UP TO 56% OFF" in alle 10, "100-day" in 5, "lifetime" in 1 | ~3.160 |
| UEfh4h Winback (tot 14 dec) | 4 | "PRIME TIME / 56%" in alle 4 | ~485 |
| YyaMjx FREE E-GUIDE | 1 | "PRIME TIME / 56%" | ~170 |

Ook: T2SmtR doet $118 per dag op 3.160 mails ($0,04 per ontvanger). Advies: banners en claims eruit vóór 1 nov, en daarna besluiten of FTL in BFCM pauzeert (campagnes bereiken dezelfde mensen).

---

## 5. Top 10 prioriteiten (impact x snelheid)

| # | Wat | Impact | Effort | BFCM | Eerste concrete stap | Floris beslist |
|---|---|---|---|---|---|---|
| 1 | **Bereik v4 Browse herstellen** (G1): filters WdRz5k naast Wj6x6V, tweede mail voor niet-openers, QNZyEb live | $300 tot $450 per dag, **$9.000 tot $13.500 per maand** | S | hoog | Claude: per filter van WdRz5k tellen hoeveel bekijkers van 1 dag eruit vallen (read-only), voorstel met de 2 of 3 strengste filters | welke filters soepeler mogen; "ga" voor QNZyEb (kliksplit in de UI) |
| 2 | **Vangnet checkout en cart via Triple Pixel en Elevar** (4.1) | $110 tot $170 per dag, **$3.300 tot $5.000 per maand** | S (checkout), M (cart) | hoog | Claude: QUBUQV-kloon als Draft met trigger RtgBgs, zelfde dedupe als QNZyEb; daarna Elevar-eventvorm controleren | akkoord op Draft-bouw via API; Elevar als derde bron ja/nee |
| 3 | **Claims en 56%-banners uit live oude mails** (4.14) | risico en verwarring met 70% off; ~3.800 mails per dag | S | kern | Claude: lijst per mail met exact blok; Floris haalt de blokken weg (UI, zoals plan 11 sectie 8) of zet FTL op pauze | weghalen of FTL in november pauzeren |
| 4 | **BFCM early access-lijst en flow** (4.4) | **$7.500 tot $15.000** over BFCM | S tot M | kern | Claude: 3 mails en lijst-spec in de repo; Homestead/Alia: kaart of form | start early access (uren), Alia of Klaviyo-form, wat de lijst krijgt |
| 5 | **Price drop en low inventory** (4.3, 4.5) | $3.000 eenmalig nov plus $1.000 tot $2.000 per maand | S tot M | hoog | Claude: catalogus (prijs, compare-at, voorraad) read-only controleren op 5 producten | gaan BFCM-prijzen als echte prijs in Shopify of via code? Drempel voor "almost gone" |
| 6 | **SMS-flows** (4.2) | **$3.000 tot $4.500 per maand** | M | hoog | Claude: SMS-toestemmingen per markt tellen en 4 SMS-teksten schrijven | SMS in flows ja/nee, wie beheert SMS (Homestead?), budget |
| 7 | **Bestaande klanten: anniversary/VIP/reactivatie** (4.6) | **$3.000 tot $5.000 per maand**, piek nov | M | hoog | Claude: `first_order_date` en `order_count` toevoegen aan `sync_owned.py` (alleen code, geen run) | akkoord op het extra profielveld en op een datumtrigger naast XbYT7T |
| 8 | **Mystery Gift v3 live** (4.7) | **$1.500 tot $3.000 per maand** | S | middel | beelden naar de Klaviyo-bibliotheek, flow als Draft | copy, M4 aan/uit, Recharge-portaalclaim (open vragen in de spec) |
| 9 | **Proactieve deelzending/vertraging** (4.12) | minder tickets en refunds | S tot M | hoog (service) | Claude: eventvorm ShipBob Shipped en OutOfStock lezen, draft WjhwUa nalopen | tekst over levertijd (3 tot 6 werkdagen of beleid) |
| 10 | **Cross-sell deksel dag 32 en Cutting Board-tak terug** (4.8, G6) | ~$900 per maand plus service | S | laag tot middel | Claude: segmentgrootte pankopers zonder deksel uit siraat_owned | ja/nee op extra post-purchase-mail |

Daarna: referral (januari), collectie/zoek-tak in site abandonment, BIS-template, gift card G2, Recharge-flows.

**Volgorde voor de komende 12 dagen (tot 1 nov):** 3 en 1 deze week (Homestead wil tot 22 okt geen grote wijzigingen; 1 en 3 zijn herstel), dan 2, 4 en 5 vóór 28 okt, 6 en 7 als het lukt vóór 1 nov, anders direct na Cyber Monday. 8 tot 10 kunnen parallel omdat ze los van BFCM staan.

---

## 6. Bronnen en werkwijze

- Klaviyo-API, account TdtTzz, 19 okt 2026: 97 flows met definitie, 177 metrics met aantallen over 30 dagen, flow-values-reports voor/na, campaign-values-report 30 dagen per kanaal, Placed Order per dag en per maand (okt 2025 tot sep 2026), alle events van 17 okt 2026 voor 13 metrics (unieke profielen per bron, overlap en zonder order). Scripts en ruwe data in de scratchpad van deze sessie, niet in de repo.
- Repo: research/v6-golive/11-overstapplan-oude-flows.md, 03-golive-draaiboek.md, research/homestead/2026-10-15-call-harmony.md, research/timing/01-data.md (herhaalaankoop, levertijd), research/referral/01-ontwerp.md, klaviyo/flows/mystery-gift-v3.md, research/concurrenten/overzicht.md, LOG.md (QNZyEb, 19 okt).
- Benchmarks: [Klaviyo abandoned cart benchmarks (2026, e-mail $6,77 en SMS $4,48 per ontvanger)](https://www.klaviyo.com/marketing-resources/abandoned-cart-benchmarks), [Klaviyo 2024 Benchmark Report](https://resources.klaviyo.com/2024-benchmark-report), [Eightx: flow revenue benchmarks (back in stock $9,14)](https://eightx.co/blog/average-klaviyo-flow-revenue-contribution-benchmarks), [InboxAlly: Klaviyo benchmarks (browse $0,95, top 10% $7,05)](https://www.inboxally.com/blog/klaviyo-email-benchmarks). Voor price drop is geen betrouwbare benchmark gevonden; de schatting rust op onze eigen browse-RPR.
- Beperkingen: één meetdag (zaterdag, drukker dan gemiddeld) voor de overlap; attributie is last touch met het Klaviyo-venster en overschat incrementele omzet; de periode na is 10,8 dagen en valt deels in een 90/10-test.
