# A/B Q4 · 07 · Uitgevoerd op 28 oktober 2026

Op akkoord van Floris (28 okt): "graag alles implementeren jij, dus ook die filter tegen orders van 0$, maar alle andere dingen, en die C2 even testen naar 48 uur, graag alle testen starten". Uitgevoerd via de Klaviyo-API (account TdtTzz), tussen 23:05 en 23:56 UTC.

Elke actie is vóór de wijziging teruggelezen en erna gecontroleerd: status ongewijzigd, template ongewijzigd, filter aanwezig. De oude definities staan in `exports/rollback/2026-10-28-abq4/` (`voor0` = vóór alles, `voor1` = na het $0-filter).

Geen enkele wijziging is door een classifier tegengehouden.

## Overzicht

| # | Item | Status | ID's | Terugdraaien |
|---|---|---|---|---|
| 1 | $0-filter op order- en bezorgflows | **live** op 58 verzendacties | zie 1 | PATCH met `voor0/<id>.json` |
| 2 | P2-SAFE niet dubbel | **live** | actie 119850554 | PATCH met `voor1/119850554.json` |
| 3 | TP · B2-NOTCLICKED op Manual | **gedaan** | actie 121177242 (QNZyEb) | status terug op live |
| 4 | Vangnetflows bezorging | **live** | R9dcdY (P2), YhQJdb (affiliate S1) | flow op draft of manual |
| 4b | Dedupe in de originelen | **live** | 119850581, 121654816/17/22/23, 119577632/35 | PATCH met `voor1/<id>.json` |
| 5 | Q1 W1-onderwerp, T04 dicht met A | **loopt** sinds 23:13 UTC | variatie 119850658 | `voor0/119850658.json` |
| 5b | BR1 op B1 (WdRz5k), T05a dicht met A | **loopt** sinds 23:41 UTC | variatie 119850692 | `voor0/119850692.json` |
| 6 | UI-tests voorbereid | templates klaar, start in UI | zie 6 en `06-ui-stappen.md` | niets live |
| 7 | BFCM-kopersreeks | segment en 3 concepten (Draft) | SpBxrC, XN5G3M, 3 campagnes | verwijderen |
| 8 | Testmails naar Floris | 13 verstuurd | lijst R8FUy5 | n.v.t. |

---

## 1. $0-filter (TikTok-samples)

**Hoe een sample eruitziet.** Gezien in de Placed Order-events (RSNxYV):
- `$value` 0, `Source Name` "tiktok".
- Tags "Free sample", "Shipped by Seller" en "TikTokOrderID:...".
- Kortingscode "Free sample" voor 100%.

Sinds 1 okt zijn er 365 orders van $0:
- 285 TikTok-samples;
- 41 draft orders met "Custom discount": vooral "#FOC Replacement" (vervanging bij een defect) en "Influencer seeding";
- 4 overige web-orders.

**Filter.** Op elke send-email komt een eigen conditiegroep:
- Placed Order met `$value` > 0;
- minstens 1 keer;
- in de laatste N dagen.

N = de wachttijd tot die mail + een buffer:
- order-flows +3 dagen;
- bezorg-flows +60 dagen;
- de review +75 dagen.

Zo telt de order die de flow startte altijd mee als hij betaald is. **Een betalende klant wordt dus nooit tegengehouden voor de mails van zijn eigen betaalde order.** Een sample of vervanging start nog wel de flow, maar de mails gaan er niet uit, tenzij die persoon in hetzelfde venster ook een betaalde order had.

Waarom niet "ooit een betaalde order":
- Een vroegere klant die nu een TikTok-sample of een gratis vervanging krijgt, zou dan opnieuw P1 krijgen ("Good call"), daarna een reviewverzoek voor de vervanging en 60 dagen later een winback.
- Met het venster gebeurt dat niet.
- Wil Floris toch "ooit": één PATCH per actie (timeframe naar alltime).

**Toegepast op 58 verzendacties.** UYALJ8 (e-gift card) is overgeslagen: de trigger vraagt een gift card, dus een sample komt daar niet binnen.

| Flow | Acties | N (dagen) |
|---|---|---|
| X3ySuU post-purchase | P1-FIRST, P1-REPEAT (4), P2-SAFE (20), 21 P3-varianten (24) | 4 tot 24 |
| VQ93sx P2 | 119850581 | 61 |
| XzHrez review (A/B-variaties) | 119577632, 119577635 | 75 |
| TvfJYU review-vangnet | 121192022 | 80 |
| YwsKcf Mystery Gift | M1 tot M3 en M4 (draft) | 6 tot 33 |
| R22pzb affiliate S1 | 4 mails | 65 tot 70 |
| UEfh4h oude winback | 4 mails | 63 tot 66 |
| UyFc78 v4-winback | 10 mails | 48 tot 78 |
| VTkxFL VIP | 4 mails | 33 tot 43 |
| XbYT7T anniversary | 3 mails | 185 tot 368 |
| YyaMjx FREE E-GUIDE (trigger Placed Order) | 1 mail | 3 |
| VPixnJ UGC first egg | 1 mail | 64 |

**Telling over de afgelopen 14 dagen (14 tot 28 okt).** Bekeken zijn alle 563 profielen met een $0-order sinds 15 juli en hun ontvangen mails. Het filter had **791 mails aan 339 profielen** tegengehouden:

| Type $0-order | Mails tegengehouden |
|---|---|
| TikTok-sample | 644 |
| Gratis vervanging (FOC replacement) | 73 |
| Influencer seeding | 46 |
| Overig | 28 |

Per flow:
- X3ySuU 253
- FREE E-GUIDE 236
- VQ93sx 130
- UGC 86
- oude winback 70
- review 16

Mails die bij deze profielen wél bij een betaalde order hoorden, gaan gewoon door: 74 mails in 14 dagen.

Wat Floris zelf in de UI regelt (06-ui-stappen, stap 0):
- de triggerfilter `$value > 0` op X3ySuU;
- herinstap en profielfilter naar 7 dagen.

## 2. P2-SAFE niet dubbel (actie 119850554)

Drie verzendfilters zijn erbij gekomen:
- Received Email waar Campaign Name "P2-SAFE" bevat: 0 keer in 30 dagen;
- Received Email `$flow` = VQ93sx: 0 keer in 30 dagen;
- Received Email `$flow` = R9dcdY (het nieuwe P2-vangnet): 0 keer in 30 dagen.

## 3. TP · B2-NOTCLICKED op Manual

Actie 121177242 in QNZyEb staat van live op **manual**. De rest van de flow blijft live. Reden: 0,50% spam, boven de Gmail-grens.

## 4. Vangnet voor bezorgevents

**Levertijd.** Fulfilled naar Delivered in Klaviyo (1.323 orders, 20 sep tot 11 okt):
- mediaan 7,1 dagen;
- p75 9,7 dagen;
- p90 12,5 dagen.

Per land: US mediaan 7,3 en p90 13,6; AU 6,5 en 10,8; UK 8,9 en 11,1.

Ecomflow (`shipping_times`, 30 dagen): US gemiddeld 9,1 dagen (6 tot 13), UK 7,5, AU 8,0, CA 8,8. De doorlooptijd tot de vervoerder is nu weer 1 tot 3 dagen. Die liep 9 tot 22 okt op tot 4 tot 14 dagen.

| Vangnet | Flow | Trigger en wachttijd | Mails | Instroom |
|---|---|---|---|---|
| P2 | **R9dcdY** "v4 · P2 vangnet · Fulfilled +12d (geen Delivered)", live | Fulfilled Order (VtEiZT), 12 dagen tot 13:00 profieltijd | P2 · vangnet (122742976), template UJ4XeW = byte-kopie van de live P2 (UKxRjv) | pankopers (zelfde productlijst als VQ93sx, 45 dagen), niet in deze flow in 30 dagen, herinstap 30 dagen |
| Affiliate S1 | **YhQJdb** "AFF S1 vangnet · Fulfilled +12d (geen Postflows)", live | Fulfilled Order, 10% holdout, 12 dagen tot 10:00, dan dezelfde opbouw als R22pzb | A1 (122742393, 122742394), A2 (122742399, 122742400); templates byte-kopie van de originelen | profielfilter van R22pzb (referral link, geen refund of cancel 60 dagen, geen ticket 21 dagen, nooit een referral-sale), eenmalig |

Waarom P2 pas op dag 12:
- P2 zegt "your pan has arrived".
- Op dag 12 is ongeveer 90% bezorgd.
- Het origineel gaat 1 dag na bezorging om 09:00.
- Het vangnet gaat om 13:00, zodat een origineel van dezelfde ochtend al als ontvangen telt.

**Dedupe.** Niemand krijgt beide versies.

Het vangnet slaat over bij:
- **P2**: een Delivered Shipment sinds de start; een mail uit VQ93sx in 30 dagen; P2-SAFE in 30 dagen.
- **AFF**: een Postflows-bezorgevent sinds de start; ooit een mail uit R22pzb.

De originelen slaan over bij een mail uit het vangnet:
- VQ93sx P2: geen R9dcdY-mail in 30 dagen;
- R22pzb A1 en A2: nooit een YhQJdb-mail.

Beide vangnetten hebben het $0-filter.

Restpunt: wie in de 10%-holdout van R22pzb zat, kreeg geen mail en is niet als "in R22pzb" te herkennen. Een klein deel van die holdout kan dus een vangnetmail krijgen.

**QA.**
- De templates zijn byte-gelijk aan de live originelen.
- Server-render van P2 en de vier AFF-mails op echte Fulfilled-events (US, AU en GB): geen restanten, geen em dash.
- P2 leest `event.Items` en `event.extra.shipping_address`. Die staan in Fulfilled Order net zo als in Delivered Shipment.
- Een vangnetflow start alleen voor nieuwe Fulfilled-events vanaf het moment van livegang. Er wordt niets ingehaald.
- De eerste P2-vangnetmails gaan rond 9 nov, de eerste AFF-vangnetmails rond 9 tot 11 nov.

**Review-vangnet TvfJYU (alleen gecontroleerd).**
- De flow is live en de mail is live.
- Profielfilter "geen Delivered sinds de start" (wordt bij elke stap opnieuw getoetst), "nooit een XzHrez-mail", geen set van 12.
- De eerste mails gaan vanaf ongeveer 9 nov (Fulfilled + 21 dagen).

Gat gevonden: XzHrez sloot TvfJYU niet uit. Wie op dag 21 de vangnetmail kreeg en daarna toch een Delivered-event kreeg, zou op bezorging + 14 dagen een tweede reviewverzoek krijgen. Dat is opgelost: beide XzHrez-variaties (119577632, 119577635) hebben nu het verzendfilter "nooit een TvfJYU-mail".

Terugdraaien:
- vangnetflows op draft;
- dedupe-filters terugzetten met `voor1/<id>.json`.

## 5. Tests via de API (gestart)

| Test | Wat | Sinds | Meten |
|---|---|---|---|
| **T04 dicht met A** | Geen winnaar: P(B beter) ≈ 69%, de regel vraagt 95% (01-welcome) | 28 okt | regel in `research/testing/results.csv` |
| **Q1 · W1-onderwerp** | Variatie 119850658 (B) heeft nu onderwerp **"Your 10% works on top of the sale"**, de preview van A en de template van A (kopie XMAs8s, HTML gelijk aan Sq2bvX). A blijft "No PFAS. Here's the paper. And 10%." Verdeling 50/50, automatische winnaar uit | 28 okt 23:13 UTC | `$variation` SXwPrW (B), alleen data na 23:13 UTC. Beslissen op 19 nov bij ≥ +20% klik, anders door tot december |
| **T05a dicht met A** | Geen verschil op klik of orders (03-browse) | 28 okt | results.csv |
| **BR1 · B1 met de saleprijs (WdRz5k)** | Variatie 119850692 (B) heeft nu onderwerp **"Your pan, at the sale price"**, preview "The sale price, plus an extra 10% with HI10. The lab report is inside." en template Ye4tQy (= library RDeehg). Anders dan A: codebalk, aanbodbalk in de hero (b1-hero-br1.jpg, alleen de balk opnieuw geschilderd, foto en kop gelijk), de prijsregel en de preheader | 28 okt 23:41 UTC | `$variation` van 119850692. TP-helft in de UI (06, stap 2). Beslissen op 7 dec |

De review-A/B (XzHrez) had geen geplande variatiewissel.

## 6. UI-tests: voorbereid

Library-templates (CODE), gebouwd met `scripts/build_ab_q4.py`. Bronnen en kopieën staan in `klaviyo/templates/v3/ab-q4/`. Een B-variant van een bestaande mail is afgeleid van de **live** template van A, met een vaste lijst vervangingen. Zo verschilt B alleen in de testvariabele. De repo-build wijkt namelijk af van wat live staat.

| Test | Template | ID | Basis |
|---|---|---|---|
| T15 · P1-FIRST dekselkaart | AB Q4 · T15-B · P1-FIRST dekselkaart | TW2TUt | live XhZ3Xr, dekselregel wordt kaart (geen prijs) |
| BR1 · TP B1 | AB Q4 · BR1-B · TP B1 sale-prijs (QNZyEb) | TgpB6X | live TY9hCH |
| BR1 · B1 | AB Q4 · BR1-B · B1 sale-prijs (WdRz5k) | RDeehg | live R6E5Zv (al in gebruik via de API) |
| T21 · K1 met HI10 | AB Q4 · T21-B · K1 met HI10 toegepast | W4XNNw | live Rp3mf6 |
| T23 · K4 termijnen | AB Q4 · T23 · K4 termijnen (cart dag 7, US) | WJB7C2 | nieuw: `v3/cart/k4-installments.html`, hero k4-hero.jpg (P04-A) |
| T24 · C5 termijnen | AB Q4 · T24 · C5 termijnen (checkout dag 14, US) | VeFfkA | nieuw: `v3/checkout/c5-installments.html`, hero c5-hero.jpg (P11-D) |
| T22 · C2 48 uur | geen nieuwe template (klonen in de UI) | | |
| T14 · C1-onderwerp | geen nieuwe template | | |
| T18 · K1-onderwerp | geen nieuwe template, start pas na T21 | | |

**QA.**
- K4 en C5: `qa_render.py` met statische controle in V5-STRICT, Django-render, browser op 600 en 390 px, markten en Gmail-simulatie.
- Enige FOUT: de bekende footerregel (zwarte links op #282828 in de Gmail-iOS-simulatie, "variant E"). Die staat ook bij de live mails, zoals K2-NEW. Het is geen nieuw probleem.
- B-varianten:
  - server-render op echte events (B1 en TP: Viewed Product; K1: Added to Cart US en EUR; P1: Placed Order US en niet-US);
  - tekstdiff A tegen B laat alleen de bedoelde regels zien;
  - geen restanten, geen None, geen $0, geen em dash;
  - Chromium 390 en 600 px zonder horizontale scroll, alle beelden laden;
  - `mail_checks`: preview en achtergrond zonder problemen.
- Copy: skill siraat-direct-response, 5 onderwerpen per nieuwe mail staan in de bron-comment.

## 7. BFCM-reeks naar eerdere kopers (voorbereiding)

- Segment **SpBxrC** "BFCM · Kopers · mailbaar · geen order 30 d":
  - minstens 1 betaalde order ooit ($value > 0);
  - geen order in 30 dagen;
  - e-mail marketing toegestaan.
  - Het telde direct na aanmaken nog (0, processing).
- Lijst **XN5G3M** "BFCM · Kopers · holdout 15% (vullen op 12 nov)". Nog leeg, staat als uitsluiting op de drie concepten. Vullen op 12 nov met een random 15% uit SpBxrC.
- Drie campagnes als **Draft** (niet ingepland). De datum in de concepten is alleen een richtdatum.

| Campagne | ID | Template | Onderwerp |
|---|---|---|---|
| CONCEPT · BFCM kopers 1 · aanloop (13 nov) | 01M62ECAG50BTTQGG82JYEY541 | TAcSqc | The lid your pan is missing |
| CONCEPT · BFCM kopers 2 · Black Friday (27 nov) | 01M62ECEGWRPHFA2HQPAM6WE22 | VhZvzh | Black Friday, for the kitchen you started |
| CONCEPT · BFCM kopers 3 · Cyber Monday (30 nov) | 01M62ECJ5ER9F0GNV8GJMKJPCV | UAmcBg | Cyber Monday, one more look |

- Bronnen: `klaviyo/templates/campaigns/bfcm-kopers-1..3.html`. Elk concept is een korte brief van Benjamin met:
  - cross-sell op `siraat_owned`, zonder prijzen (de novemberprijzen zijn niet bekend);
  - de gifts-strook en een knop.
- Ontbreekt nog (wacht op Floris):
  - reikwijdte en startdatum van de novembersale (nu "up to 70% off");
  - setprijs in november;
  - Black Friday-aanbod of vroege toegang;
  - einddatum. Daarom staat er geen "last chance" in.

## 8. Testmails naar Floris

Er zijn 13 campagnes "TEST2 · AB Q4 · ..." naar lijst R8FUy5 ("TEST · Floris", 1 profiel) verstuurd tussen 23:53 en 23:55 UTC, met "[TEST]" voor het onderwerp. De verzending liep via campagnes, niet via de Gmail-koppeling.

Mails met eventdata zijn vooraf gerenderd op een echt event (US, Pan Pro Standard), zodat Floris de echte inhoud ziet.

Verstuurd:
- Q1 W1-B;
- BR1 B1-B en BR1 TP-B1-B;
- T21 K1-B;
- T15 P1-FIRST-B;
- T23 K4 en T24 C5;
- P2-vangnet, AFF-vangnet A1 en A2;
- BFCM-concepten 1 tot 3.

Fout en herstel: de eerste ronde (campagnes "TEST · AB Q4 · ...") had een vaste verzenddatum 31 dec in plaats van "direct". Ze zijn allemaal geannuleerd vóór verzending (status Cancelled). Er is niets twee keer verstuurd.

## Geblokkeerd of bewust niet gedaan

- **Classifier**: niets tegengehouden.
- **API-grenzen**:
  - Flownaam wijzigen kan niet. Het P2-vangnet is daarom als draft opnieuw gemaakt met de juiste naam (oude draft Yfeu2i verwijderd, nooit live).
  - Een naamfilter met "·" werkt niet in de API. Daardoor ontstonden een dubbele draft-flow (WbXPmR) en 4 dubbele templates. Die zijn direct verwijderd.
  - De wegwerp-flow YuaK3J is verwijderd.
- **Alleen UI**: zie 06-ui-stappen.md (X3ySuU trigger, herinstap en profielfilter; T15, BR1-TP, T14, T21, T23, T24, T22, later T18).
- **Wacht op Floris**: Q2/W5, BR3, winback met de sale, P3-salerij, de regel over de gifts na 31 okt, het affiliate-blok in BFCM, de inhoud van de BFCM-concepten.
- **Niet uitgevoerd zonder akkoord**: oude banners en claims in winback en FTL.
