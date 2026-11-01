# Smooche · 06 · Volumeplan november v2 (1 nov 2026)

Opdracht Floris (1 nov, na afwijzing van de november-concepten in `05-designs-november.md`): zelfde mailvolume als Smooche (ongeveer 13 mails in 41 uur voor iemand die zich aanmeldt, kijkt, in de winkelwagen legt en afrekent), pure direct response ("dit is echt THE sale"), harde push aan het einde van de sale (maandag 30 november) en nooit meer "next batch" of "reserve": de nieuwe 6-Pcs en 12-Pcs voorraad is net binnen, dus "Just arrived and selling fast" (DECISIONS, "Voorraad-copy").

**Status: concept. Niets in Klaviyo of Shopify gewijzigd, niets live.** Designs: `klaviyo/templates/v3/bfcm/november-v2/` (15 nieuwe mails). Figma: rij "November v2: Smooche-volume (1 nov)" op de pagina "BFCM 2026 · Flows (Black Friday-stijl)": https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=213-2 (titelkaart 213:5, tijdlijn 213:14, previews per scenario A tot E). Oude rij 210:2 heet nu "VERVANGEN DOOR V2".

Vervalt: het hele stock-concept "Our sets sold out. Here's what that means." (`nov-stock`, verwijderd) en elke regel "next batch", "reserved", "arriving mid-November" (ook uit blok `bf-stock`). De oude `november/`-concepten blijven alleen als archief.

---

## 0. Kort

| | Smooche (gemeten) | Siraat nu | Siraat v2 |
|---|---|---|---|
| Mails in 41 uur, reis aanmelden + kijken + cart + checkout | **13** | 3 à 4 | **13** |
| Mails in de eerste 2 uur | 3 | 1 | 3 |
| Cart/checkout dag 0 | 3 in 90 min | 1 (C1) | 4 (K1, C1, C1b +1 u, C1c +3 u) |
| Cart/checkout dag 1 (24 uur later) | 3 in 75 min | 1 (C2 08:30) | 3 (C2 +24 u, C2b +25 u, C2c +26 u) |
| Persoonlijke brief ("Chloe" / Benjamin) | 7 van 13 | 0 | 3 van 13 (C1b, C2c, plus W1b/letter-campagne) |
| Campagnes per dag in november | n.v.t. | 0 à 3, 9 lege dagen | minimaal 1 per dag, 3 à 5 op 28 tot 30 nov |

Vangrail (Floris accepteert extra afmeldingen en spam, "wie spam klikt, koopt toch niet"): **stop een nieuwe verzending of flowstap zodra de spamklachten boven 0,3% komen** (de harde grens van Gmail). Zie sectie 6.

## 1. Uitgangspunt: de Smooche-reis

Uit `04-meer-output-november.md` sectie 1 (13 .eml's, Gmail-thread van Floris). Aanmelding 30 okt 23:27 UTC, cart en checkout gestart ~31 okt 14:30 UTC (+15 u).

| # | Uur | Smooche | Type |
|---|---|---|---|
| 1 | 0,0 | You joined at the right time | welkom, beeld |
| 2 | 0,5 | Found your new make-up? (Chloe) | browse, brief |
| 3 | 2,0 | No tricks, just a treat (Chloe) | welkom 2, brief |
| 4 | 13,5 | Happy Halloween | campagne / krediet |
| 5 | 15,2 | Still want your foundation? (Chloe) | cart, brief |
| 6 | 16,3 | Foundation that adapts to you | product, 3 redenen |
| 7 | 16,5 | Your order is pending (Chloe) | checkout |
| 8 | 26,0 | What the right foundation actually does | welkom 3, educatie + reviews |
| 9 | 38,5 | Your store credit is updated (Chloe) | campagne / krediet |
| 10 | 39,2 | Your foundation order is pending (Chloe) | checkout 2 |
| 11 | 40,3 | A photo of me went viral... | verhaal |
| 12 | 40,5 | #1 Korean Foundation is waiting | checkout 3, beeld |
| 13 | 41,3 | Your [bedrag] is about to disappear | campagne, aftelklok |

Wat we overnemen: het ritme (0, +0,5, +2 uur; cart/checkout drie keer binnen 90 minuten en precies 24 uur later nog eens drie), de mix beeldmail / brief, de dagelijkse campagne. Wat we niet overnemen: nep-tegoed, "your order is pending", nep-aftelklokken en "expires today" zonder echte deadline.

## 2. De gecombineerde reis (13 mails in 40,5 uur)

Scenario zoals Floris het testte, in lokale tijd van de klant: aanmelding dag 0 om 20:00, bekijkt meteen een product (20:10), legt de volgende ochtend om 10:00 in de winkelwagen en start om 10:20 de checkout, koopt niet.

| # | Moment | Uur | Flow | Mail | Status | Onderwerp (A) |
|---|---|---|---|---|---|---|
| 1 | d0 20:05 | 0,1 | Welcome T4a5Mk (W1-a-bf) of BF-groep Rn556d (BF-W1) | W1 | hergebruik, live | (bestaand) |
| 2 | d0 20:40 | 0,7 | Browse WdRz5k / QNZyEb | B1 (b1-bf) | hergebruik, **wachttijd 1 u naar 30 min** | (bestaand) |
| 3 | d0 22:00 | 2,0 | Welcome T4a5Mk + Rn556d | **v2-w1b** | nieuw | Your Black Friday price list |
| 4 | d1 08:15 | 12,3 | Campagne (Homestead of extra slot, sectie 4) | dagcampagne | kalender | (per dag) |
| 5 | d1 10:15 | 14,3 | Cart TZG9Mx | K1 (k1-v2-bf) | hergebruik, live, +15 min | (bestaand) |
| 6 | d1 10:30 | 14,5 | Checkout QUBUQV | C1 (c1-bf) | hergebruik, live, +10 min | (bestaand) |
| 7 | d1 11:20 | 15,3 | Checkout QUBUQV | **v2-c1b** | nieuw, +1 u | I saved your cart |
| 8 | d1 13:20 | 17,3 | Checkout QUBUQV | **v2-c1c** | nieuw, +3 u | 3 reasons 100,000+ people switched |
| 9 | d1 20:00 | 24,0 | Welcome T4a5Mk + Rn556d | **v2-w2** | nieuw, +24 u na aanmelding | Just arrived: the 6 and 12-piece sets |
| 10 | d2 08:15 | 36,3 | Campagne | dagcampagne | kalender | (per dag) |
| 11 | d2 10:20 | 38,5 | Checkout QUBUQV | C2 (c2-bf) | hergebruik, **wachttijd "volgende dag 08:30" naar precies +24 u** | (bestaand) |
| 12 | d2 11:20 | 39,5 | Checkout QUBUQV | **v2-c2b** | nieuw, +25 u | Everything you get, added up |
| 13 | d2 12:20 | 40,5 | Checkout QUBUQV | **v2-c2c** | nieuw, +26 u | Two promises before Monday |

Totaal: **13 mails in 40,5 uur** (Smooche 13 in 41,3 uur). Verdeling: 0-6 uur 3 (Smooche 3), 6-24 uur 6 (Smooche 4), 24-41 uur 4 (Smooche 6). Hergebruikt: 6 (W1, B1, K1, C1, C2 plus de campagnes); nieuw: 7 flowmails.

Waarom K1 (#5) nog verstuurd wordt: de cart-flow filtert op "Started Checkout = 0 sinds flowstart" op het moment van versturen; bij checkout na 20 minuten is K1 (+15 min) al weg. Start de checkout binnen 15 minuten, dan vervalt K1 en komt de reis op 12. Wil Floris altijd 13: K1 voor checkout-starters niet overslaan (filter weg), dan dubbelt K1 met C1 inhoudelijk.

## 3. Per scenario: elke mail met wachttijd

Alle tijden na de trigger van die flow. "Overslaan" = de stap valt weg als er in het genoemde venster al een mail uit een andere flow kwam (filter op Received Email, flow-string). Nieuwe stappen krijgen geen "max 3 mails per dag"-filter meer (vervalt op verzoek van Floris); wel "Placed Order = 0 sinds flowstart".

### 3.1 Alleen aanmelden (Welcome T4a5Mk, gewone groep; BF-groep Rn556d gelijk getrokken)

| Stap | Wachttijd | Mail | Hergebruik / nieuw | Overslaan als |
|---|---|---|---|---|
| W1 / BF-W1 | +5 min (Rn556d direct) | w1-a-bf / bf-w1 | hergebruik | |
| W1b | +2 uur | v2-w1b (prijslijst) | **nieuw** | Started Checkout in laatste 1 uur |
| W2 | +24 uur (nu: volgende dag 10:00) | v2-w2 (just arrived, selling fast) | **nieuw**, vervangt w2-bf tijdens de sale | cart/checkout-mail in laatste 1 uur (nu 1 dag) |
| W3 | +2 dagen 09:00 | w3-bf / bf-w3 | hergebruik | idem |
| W4, W5 | zoals nu | w4-us-bf / w4-int-bf, w5-bf | hergebruik | idem |
| Last call | 28, 29 en 30 nov via de eindcampagnes (sectie 5) | | | |

Plus de dagcampagne (nieuwe aanmelders zitten in E30). Alleen-aanmelden in 41 uur: W1, W1b, W2 + 2 campagnes = 5 (Smooche 5 in hetzelfde scenario: mails 1, 3, 4, 8, 9).

BF-groep Rn556d: krijgt na BF-W1 nu niets meer uit de welcome (exit-split 119850651). In v2: W1b, W2, W3 als stappen in Rn556d (of de exit-split laten alleen W1 overslaan). Beslissing nodig.

### 3.2 Alleen kijken (Browse WdRz5k, Triple Pixel QNZyEb draft)

| Stap | Wachttijd | Mail | Hergebruik / nieuw |
|---|---|---|---|
| B1 | **30 min** (nu 1 uur) | b1-bf / b1-acc-bf (tp-b1-bf in QNZyEb) | hergebruik |
| B2 | **+24 uur** (nu 2 dagen 09:00) | b2-clicked-bf / b2-clicked-nocode-bf / b2-notclicked-bf | hergebruik |
| B3 | +48 uur | v2-proof (100,000+, als flowmail) | **nieuw** (zelfde ontwerp als de campagne) |

### 3.3 Winkelwagen (Cart TZG9Mx)

| Stap | Wachttijd | Mail | Hergebruik / nieuw |
|---|---|---|---|
| K1 | +15 min | k1-v2-bf / k1-acc-bf | hergebruik |
| K1b | **+1 uur** | v2-k1b (extra 10% ticket, BFCODE) | **nieuw** |
| K2 | **+24 uur** (nu 2 dagen 08:00) | k2-new-bf / k2-returning-bf | hergebruik |
| K2b | +25 uur | v2-c2b-ontwerp met cart-event (value stack) | **nieuw** (variant van v2-c2b op het Added to Cart-event; bouwen na akkoord) |
| K3 | +3 dagen 09:00 | k3-bf / k3-nocode-bf | hergebruik |

Filter op elke stap: Started Checkout = 0 sinds flowstart (checkout neemt over).

### 3.4 Checkout (QUBUQV)

| Stap | Wachttijd | Mail | Hergebruik / nieuw |
|---|---|---|---|
| C1 | +10 min | c1-bf | hergebruik |
| C1b | **+1 uur** | v2-c1b (brief Benjamin, "I saved your cart") | **nieuw** |
| C1c | **+3 uur** | v2-c1c (3 redenen + review + cart) | **nieuw** |
| C2 | **+24 uur** (nu volgende dag 08:30) | c2-bf / c2-acc-bf | hergebruik |
| C2b | **+25 uur** | v2-c2b (value stack) | **nieuw** |
| C2c | **+26 uur** | v2-c2c (donkere brief, "Two promises") | **nieuw** |
| C3 | +3 dagen 09:00 | c3-s-bf / c3-p-bf / c3-acc-bf | hergebruik |
| C4 | +5 dagen 09:00 | c4-bf / c4-nocode-bf | hergebruik |

Checkout alleen in 41 uur: 6 mails (Smooche-ritme: 3 + 3).

### 3.5 Site (VLGhbR)

A1 van 2 uur naar **1 uur**, A2 van 2 dagen naar **+24 uur** (a1-bf, a2-bf, hergebruik). Geen nieuwe mails.

### 3.6 Wat in Klaviyo moet veranderen (na akkoord, niet gedaan)

| Flow | Wijziging |
|---|---|
| T4a5Mk welcome | stap W1b +2 u (v2-w1b); W2-template tijdens de sale v2-w2 op +24 u; overslaanvenster van 1 dag naar 1 uur |
| Rn556d BF-groep | W1b, W2, W3 toevoegen (of exit-split 119850651 aanpassen) |
| WdRz5k / QNZyEb | B1 30 min, B2 +24 u, B3 +48 u (v2-proof) |
| TZG9Mx cart | K1b +1 u (v2-k1b), K2 +24 u, K2b +25 u |
| QUBUQV checkout | C1b +1 u, C1c +3 u, C2 +24 u, C2b +25 u, C2c +26 u |
| VLGhbR site | A1 1 u, A2 +24 u |
| Alle nieuwe stappen | Smart Sending uit (zoals C1), filter Placed Order = 0 sinds flowstart, UTM `bf-v2-*` |
| 1 december | alle BF-templates terug naar de normale versies (PLAN.md punt 4) |

## 4. Dagelijkse campagnes op de 9 lege dagen

Homestead-kalender (`research/homestead/kalender-november-2026.md`) laat 2, 4, 6, 9, 12, 13, 16, 20 en 22 november leeg. Elke dag een verzending, zodat ook de dagcampagne in de reis (sectie 2, #4 en #10) er echt is. Tijden lokaal; uitsluitingen steeds: Basis, kopers laatste 3 dagen, wie in de laatste 1 uur een flowmail uit checkout of cart kreeg.

| Dag | Tijd | Segment | Mail | Doel |
|---|---|---|---|---|
| ma 2 nov | 08:15 | E90 | v2-w2 als campagne ("Just arrived: the 6 and 12-piece sets") | nieuwe voorraad melden de dag na de launch |
| wo 4 nov | 08:00 | E30 | v2-letter ("What I would buy at 70% off") | Benjamin-brief week 1 (gat in Homestead-ritme) |
| vr 6 nov | 08:15 | E90 + kopers 365 d | v2-pricelist ("The Black Friday price list") | prijzen als hoofdzaak, lege vrijdag |
| ma 9 nov | 08:15 | E90 | v2-proof ("100,000+ kitchens, no coatings") | sociaal bewijs, maandag leeg |
| do 12 nov | 10:00 | Product Viewers + ATC L14 zonder order | v2-pricelist (onderwerp "Still deciding? Here is every price") | abandoners, vorig jaar beste RPR ($0,770) |
| vr 13 nov | 08:00 | E30 | v2-letter (onderwerp "If I were starting from zero") | tweede brief, andere opener |
| ma 16 nov | 08:15 | E30 | v2-proof (onderwerp "\"The last pans we ever have to purchase\"") | bewijs naar de warmste lezers |
| vr 20 nov | 08:15 | E90 | v2-w2 ("The sets are selling fast") | alleen als de sets die ochtend nog op voorraad zijn (check backend) |
| zo 22 nov | 10:00 | E30 + abandoners L30 | v2-pricelist (onderwerp "8 days left: the price list") | stille dag voor de BF-week, met echte deadline |

Plus optioneel do 19 nov (alleen sms bij Homestead): v2-letter of v2-proof naar E30.

Daarmee krijgt een E30-lezer in november ~28 mails (Homestead 19 + 9), een E90-lezer ~21.

## 5. Einde sale: 27 tot en met 30 november

Bovenop de Homestead-kalender. Smart Sending uit voor alle mails op 27 tot 30 nov. Uitsluiting overal: order sinds 27 nov 00:00.

| Dag | Tijd | Segment | Mail | Doel | Bron |
|---|---|---|---|---|---|
| vr 27 nov | 08:00 | Lijst | E15 Black Friday: Up to 70% Off Plus Free Gifts | BF-start | Homestead |
| vr 27 nov | 13:00 | E90 | E16 Black Friday Bestsellers | | Homestead |
| vr 27 nov | 18:00 | E90 | E17 A Note Before Black Friday Ends | let op: sale loopt tot 30 nov, titel aanpassen | Homestead |
| vr 27 nov | 21:00 | abandoners L30 | **v2-pricelist** (onderwerp "Black Friday price list, before bed") | extra, abandoners | v2 |
| za 28 nov | 08:15 | E90 + kopers 365 d | **v2-sat28** "The last weekend of Black Friday" | extra, start eindpush | v2 |
| za 28 nov | 10:00 | E180 | E18 Small Business Saturday | | Homestead |
| za 28 nov | 19:00 | abandoners L30 + E30 | **v2-proof** (onderwerp "3 days left. Here is what they say.") | extra | v2 |
| zo 29 nov | 09:00 | Lijst | **v2-sun29** "Black Friday ends tomorrow" | extra, deadline | v2 |
| zo 29 nov | 10:00 | niet-openers E16 | Resend 3 | | Homestead |
| zo 29 nov | 19:00 | niet-openers v2-sun29 + abandoners L30 | **v2-sun29** resend (onderwerp "Tomorrow it is over") | extra | v2 |
| ma 30 nov | 07:00 | E90 + abandoners L30 | **v2-mon-am** "Last day: up to 70% off" | extra, eerste mail van de dag | v2 |
| ma 30 nov | 10:00 | Lijst | E19 Cyber Monday: Final Day of the Sale | | Homestead |
| ma 30 nov | 13:00 | E30 + abandoners L14 | **v2-mon-pm** "Final hours" (brief Benjamin) | extra | v2 |
| ma 30 nov | 17:00 | E90 | E20 Final Hours | | Homestead |
| ma 30 nov | 20:00 | klikkers 30 d + abandoners L14 | **v2-mon-late** "Last email: Black Friday ends tonight" | extra, laatste mail | v2 |

Aantal voor een E30-lezer: vr 3 à 4, za 3, zo 2 à 3, ma 5. Afstemmen met Homestead: zij kunnen E19 en E20 ook met de v2-ontwerpen sturen.

Flow-aanpassingen 27 tot 30 nov:
- Alle BF-flowmails hebben al de vaste band "Sale ends Monday, Nov 30"; geen datumlogica nodig.
- Rn556d en T4a5Mk: aanmelders van 28 tot 30 nov krijgen W1b al na **1 uur** (in plaats van 2) en v2-w2 na **12 uur**, zodat ze vóór het einde nog contact hebben. Kan met een conditional split op datum (Klaviyo: profiel-eigenschap "aangemeld na 28 nov") of door de wachttijden op 28 nov om te zetten.
- QUBUQV en TZG9Mx: wie op 29 of 30 nov afhaakt, mist C2 (+24 u valt na de sale). Op 29 nov de C2-stap tijdelijk naar **+6 uur** zetten, op 1 dec terug.
- 1 december: alle BF-templates terug, campagnes stoppen, geen "ends" meer.

## 6. Vangrails (monitoring, op verzoek Floris minimaal)

- **Harde stopregel: spamklachten boven 0,3%** (de grens van Gmail) op een nieuwe verzending of flowstap, gemeten vanaf 1.000 ontvangers: die stap of campagne stopt (flowstap op Draft, campagne niet opnieuw sturen) tot we weten waarom. Dit is de enige stopregel; de strengere regels uit `04` (0,15% spam, 1,5% afmelding, max 3 per dag) vervallen op verzoek van Floris.
- Dagelijks kijken (flowbewaking #claude-mail): spam en afmeldingen per nieuwe stap en per campagne, en Google Postmaster Tools voor het domein (Klaviyo ziet niet elke Gmail-klacht). Afmeldingen alleen rapporteren.
- Voorraadregel: "Just arrived" en "Selling fast" alleen zolang de sets op voorraad zijn. Elke maandag en op de ochtend van 2, 20 en 27 tot 30 nov controleren in de backend; zijn ze uitverkocht, dan de regels weghalen (niet vervangen door "next batch").
- BFCODE: alleen in cart en checkout (v2-k1b, v2-c1b, v2-c1c, v2-c2b, v2-c2c). Werkt de code niet samen met de automatische kortingen (LOG 1 nov), dan eerst in Shopify fixen.

## 7. De nieuwe mails (verzendvolgorde)

| Mail | Flow / dag | Wachttijd | Afzender | Onderwerp A / B | Preview |
|---|---|---|---|---|---|
| v2-w1b | T4a5Mk, Rn556d | +2 u | Siraat | Your Black Friday price list / Up to 70% off. Every price inside. | Every price, side by side. Free gifts. Ends Monday, Nov 30. |
| v2-k1b | TZG9Mx | +1 u | Siraat | Extra 10% off your cart (already applied) / You left this at up to 70% off | On top of Black Friday prices. Ends Monday, Nov 30. |
| v2-c1b | QUBUQV | +1 u | Benjamin from Siraat | I saved your cart / Benjamin here, about your order | Plus an extra 10%, already applied. Sale ends Monday. |
| v2-c1c | QUBUQV | +3 u | Siraat | 3 reasons 100,000+ people switched / Why it is covered for 75 years | Then your extra 10%, still applied. Ends Monday. |
| v2-w2 | T4a5Mk, Rn556d; campagne 2 en 20 nov | +24 u | Siraat | Just arrived: the 6 and 12-piece sets / Restocked, and going fast | New stock just landed. At up to 70% off, it is selling fast. |
| v2-c2b | QUBUQV | +25 u | Siraat | Everything you get, added up / Your cart + 4 gifts + extra 10% | It is all still on your cart. Black Friday ends Monday, Nov 30. |
| v2-c2c | QUBUQV | +26 u | Benjamin from Siraat | Two promises before Monday / What if it is not for you? | Your extra 10% is still on your cart. The sale ends Monday, Nov 30. |
| v2-letter | campagne 4, 13 nov | | Benjamin from Siraat | What I would buy at 70% off / If I were starting from zero | Three picks, depending on your kitchen. Ends Monday, Nov 30. |
| v2-pricelist | campagne 6, 12, 22, 27 nov | | Siraat | The Black Friday price list / Every price, one email | Up to 70% off, side by side. Ends Monday, Nov 30. |
| v2-proof | campagne 9, 16, 28 nov; browse B3 | | Siraat | 100,000+ kitchens, no coatings / "The last pans we ever have to purchase" | What they say after the first egg. Up to 70% off until Monday, Nov 30. |
| v2-sat28 | campagne za 28 nov 08:15 | | Siraat | The last weekend of Black Friday / 3 days left: up to 70% off | Ends Monday, Nov 30. The sets are selling fast. |
| v2-sun29 | campagne zo 29 nov 09:00 + 19:00 | | Siraat | Black Friday ends tomorrow / Tomorrow it is over | Up to 70% off ends Monday, Nov 30. Here is every price. |
| v2-mon-am | campagne ma 30 nov 07:00 | | Siraat | Last day: up to 70% off / Today is the last day | Black Friday ends today. Free gifts end with it. |
| v2-mon-pm | campagne ma 30 nov 13:00 | | Benjamin from Siraat | Final hours / Benjamin here, before it ends | The Black Friday Sale ends today. A short note first. |
| v2-mon-late | campagne ma 30 nov 20:00 | | Siraat | Last email: Black Friday ends tonight / This is the last one | After today the Black Friday Sale is over. |

Alternatieve onderwerpen staan in de kopcommentaar van elke bron.

## 8. Ontwerpsysteem v2 (één systeem, elke mail anders)

Bron: `klaviyo/templates/v3/bfcm/november-v2/_tools/make_v2.py` (componenten), build en checks `render_v2.py`, screenshots `shot_v2.js` (375 en 600 px, 2x). Alles vanuit /tmp.

- Kleuren: Signal Yellow #FFB800 (vlakken, knoppen, tickets, %), Ink #272727, Night #0E0E0E, Cream #F8F7F2, Stock red #C8202A alleen voor "SELLING FAST". Inter Black koppen in caps, Inter Extra Bold tags. Geen gele tekst op cream.
- Vaste topbar (`bf-topbar`) boven de vaste header met lockup en de vaste footer in elke mail (merkregel).
- Componenten: donkere hero met "BLACK FRIDAY / SALE IS LIVE" en een reuzen-"70% OFF"; gele hero (just arrived, ends tomorrow, value stack); dealkaart met was/nu/% en bonusregel (12-Pcs + gratis Pizza Steel in de US, 6-Pcs elders); productraster 2 x 2 met doorgestreepte compare-at uit `content/catalog/products.json` per markt (`{{WAS}}`/`{{PRICE}}`); deadlineband; 30 / 75 / 100K+-strook; reviewkaarten (letterlijk uit `content/reviews/top.md`); value stack; brief van Benjamin (cream of Night).
- Gewijzigde blokken: `bf-cta` breder en zwaarder (360 px, 16 px, Inter Black), `bf-stock` zonder NEXT BATCH (alleen JUST ARRIVED, SELLING FAST, IN STOCK).
- Nieuw beeld: `assets/deal-set12-pizza.jpg` (12-Pcs + Pizza Steel-inzet), `deal-set6.jpg`, `deal-set12.jpg` uit Shopify-productbeelden (nog naar de Klaviyo-bibliotheek bij export).

Prijzen (US, products.json 31 okt): 12-Pcs $649 (was $2,047, -68%), 6-Pcs $299 (was $997), Pan Pro Standard $144 (was $480), Large $149 (was $497), Mini $99 (was $330), Deep vanaf $119 (was $397), Wok vanaf $119, Pizza Steel $199 (gratis bij de 12-Pcs via `/products/titanium-hammered-cookware-set-12-pcs-free-pizza-steel-1`). Andere markten via de macro's; overal 70%.

## 9. Open vragen voor Floris

1. Eindtijd en tijdzone van de sale op maandag 30 nov (nodig voor "ends tonight" in v2-mon-late; nu staat er "until the end of today").
2. Wat zijn de prijzen na 30 nov? We schrijven bewust niet "prices go back up" zolang dat niet vaststaat.
3. Akkoord op afzender "Benjamin from Siraat" voor v2-c1b, v2-c2c, v2-letter, v2-mon-pm?
4. BF-groep Rn556d: W1b/W2/W3 als stappen in Rn556d of exit-split aanpassen?
5. Wie verstuurt de 9 dagslots en de extra eindcampagnes: wij of Homestead? E17 "A Note Before Black Friday Ends" op 27 nov moet anders heten (sale loopt tot 30 nov).
6. Mag K1 ook naar wie al een checkout startte (dan altijd 13 in de reis)?
7. "Just arrived": klopt het ook voor de INT-voorraad (6-Pcs buiten de US)?
8. Mag de extra 10% (BFCODE) ook in de cart-value-stack K2b, en werkt de code naast de automatische kortingen?
