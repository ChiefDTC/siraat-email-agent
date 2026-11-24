# Personable (SMS-agent Sam) en de abandoned flows, 24 nov 2026

Bronnen: Klaviyo flow-series (Placed Order RSNxYV), Started Checkout RfMvni, Added to Cart QXcV8K, 15.271 Placed Order-events met codes; Shopify ShopifyQL. Alleen gelezen. Let op: checkout = QUBUQV, cart = TZG9Mx (niet andersom); browse = WdRz5k + QNZyEb. Splits staan sinds 19 okt al op 100% nieuw, dus geen splitwissel in de vergelijking.

**Startdatum.** Personable-codes (Floris): SAM5, SAM10, SAM15. SAM15 is nieuw: eerste orders 9 nov, nooit eerder gebruikt. Volume vanaf 14 nov (16 tot 23 orders per dag). Op 22 nov schakelt Sam van SAM15 naar SAM10. SAM10 bestond al: 31 orders tussen 17 okt en 8 nov (1 tot 3 per dag, pilot of oude code). SAM5 is nooit gebruikt.

| Periode | Checkout ontv / orders / omzet / $ per ontv | Cart | Browse | SAM-orders / omzet |
|---|---|---|---|---|
| Voor 26 okt t/m 8 nov (14 d) | 5.161 / 91 / $28.498 / $5,52 | 10.646 / 122 / $33.909 / $3,19 | 16.542 / 60 / $13.977 / $0,84 | 15 / $5.744 (SAM10) |
| Na 9 t/m 22 nov (14 d) | 7.667 / 147 / $43.948 / $5,73 | 17.792 / 205 / $61.677 / $3,47 | 44.111 / 178 / $44.202 / $1,00 | 190 / $57.067 |
| Sale zonder Sam 1 t/m 8 nov (8 d) | 3.681 / 60 / $17.398 / $4,73 | 7.580 / 91 / $26.648 / $3,52 | 13.596 / 47 / $11.358 / $0,84 | 12 / $5.222 |
| Sam op volume 14 t/m 21 nov (8 d) | 4.566 / 95 / $27.715 / $6,07 | 10.775 / 127 / $36.349 / $3,37 | 28.129 / 118 / $27.886 / $0,99 | 157 / $49.376 |

**Overlap.** Van de 190 SAM-orders (9 t/m 22 nov) kregen er 151 (79%) in de 3 dagen ervoor een abandoned-flowmail (vooral checkout en cart), 39 ($11.442) geen. 55 orders ($15.688) openden of klikten die mail ook, dus die telt Klaviyo als flowomzet en Personable als eigen omzet: dubbel geteld (checkout 31 / $9.297, cart 22 / $5.716, browse 2). Maar 24 SAM-kopers klikten de mail echt; de mediaan tussen eerste flowmail en order is 3,9 uur, 41 orders kwamen binnen 1 uur na de eerste mail.

**Korting.** Gemiddelde korting per order in de hele winkel daalde: $13,00 voor naar $5,90 na (orders met een code: $86 naar $47). SAM-orders: gemiddeld $49 korting op AOV $302, samen $9.484 aan korting in 14 dagen. Flowcodes werden niet minder gebruikt: BF-CVX79 157 naar 126, SIR-7K2Q9 (nieuw in de flows rond 10 nov) 0 naar 307.

**Per abandoner (alle kanalen).** Unieke Started Checkout 7.761 naar 11.178. Omzet uit checkout+cart+browse-flows per unieke checkout-starter: $9,84 naar $13,40 (+36%); met SAM-omzet erbij (zonder de 55 dubbele): $10,58 naar $17,11. Per unieke Added to Cart: $7,23 naar $8,87 (alleen mail). Ter vergelijking: winkelomzet per unieke checkout-starter steeg $177 naar $220 (+24%), dus de mailflows groeiden sneller dan de Black Week-golf zelf.

**Confounders.** Black Week-verkeer en intentie (orders per dag ~400 naar ~630), sale-intensiteit oplopend na 14 nov, SIR-7K2Q9 en nieuwe browse-varianten rond dezelfde datum, A/B browse B2 sinds 18 nov. Geen controlegroep zonder Sam, dus incrementaliteit van Personable is niet hard te bewijzen.

**Conclusie.** Geen schade aan de flows te zien: omzet per ontvanger van checkout (+4%, op volume +28% t.o.v. sale-week), cart (+9% / -4%) en browse (+19%) hield stand of steeg, en het aantal flowconversies groeide mee met het verkeer. Wel overlap: 4 op de 5 SAM-kopers zaten al in een abandoned flow, en ongeveer $15,7k van de SAM-omzet staat ook in Klaviyo. Het echte risico is marge (15% extra korting aan mensen die de mail al hadden), niet flowomzet. Personable's "$32k in 7 dagen" is dus deels mailomzet.

**Aanbevelingen.**
1. Laat Sam pas na de eerste mail sturen (checkout C1 op 10 min, cart K1 op 15 min): start Sam op 2 tot 4 uur, of sla Sam over als de eerste flowmail geopend of geklikt is. Dat raakt de 41 orders binnen 1 uur.
2. Houd de code op SAM10 (sinds 22 nov) of lager en laat SAM15 verlopen; laat Sam niet stapelen boven de flowcode (BF-CVX79/SIR-7K2Q9).
3. Meet incrementaliteit: vraag Personable om een holdout van 10 tot 20% van de cart-recovery-gesprekken en vergelijk omzet per abandoner (mail + SMS) tussen beide groepen.
