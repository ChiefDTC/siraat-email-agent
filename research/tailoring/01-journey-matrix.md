# 01 · Journey-simulator: wie krijgt welke mail, en past die?

Stand 7 oktober 2026, flowsysteem v3 zoals ontworpen (klaviyo/flows/v3-flow-system.md en v3-new-flows.md), vóór de tailoring-wijzigingen. Per trigger: welke mails in welke volgorde, en per mail of kop, uitleg, producten, aanbod en cross-sell passen.

Markering: **[ROOD]** = mismatch die de lezer merkt (verkeerd product, verkeerde uitleg, onjuiste claim of prijs). **[ORANJE]** = past matig (generiek, onnodig lang, gemiste kans). Zonder markering = past.
Weekaantallen = aandeel uit 00-data.md x instroom per week; schattingen.
"Na tailoring" verwijst naar de paden in 03-routing.md en de gebouwde mails.

## Kort: waar het het meest misgaat

| # | Mismatch | Trigger | Getroffen per week (schatting) |
| --- | --- | --- | --- |
| 1 | Browse: knop "Get 10% off this pan" en "Pure titanium cooking surface" onder elke bekeken set, plank, deksel, molen of schort; B2 "One pan. Nothing to wear off." | Viewed Product | ~360 (set 8% + accessoire 4% van ~3.000) |
| 2 | Cart: prijs in lokale valuta met een $ ervoor (S$199 wordt "$199.00", €39 wordt "$39.00") | Added to Cart | ~260 (26% niet-USD van ~990) |
| 3 | P3-pan "The lid, 10% off" aan wie de deksel net in dezelfde order kocht | Placed Order | ~135 (pan + deksel 11,6% van ~1.150) |
| 4 | Winback R1-pan "Fits the Pan Pro you already own" aan wie nooit een pan kocht (alleen plank, molen, schort) | Placed Order +60 d | ~115 (9,5% van ~1.230) |
| 5 | P1 "From order to first egg" + P2 chef-eierles aan accessoire-kopers | Placed Order | ~110 (9,5% van ~1.150) |
| 6 | Checkout C1 tot C3 praten over "the pan" en "upgrade to the 6-piece set" bij een cart met alleen schort, plank, molen of utensils | Checkout Started | ~95 (15% van ~630), waarvan ~13 schort, ~26 plank |
| 7 | P3-split kent pizza steel, roasting pan en pots niet; wok/deep/crêpe krijgen "Made for your Pan Pro" (deep 24 cm heeft geen deksel) | Placed Order | ~95 (8,4% van ~1.150) |
| 8 | Cart K1 "One wipe" (pan schoonmaken) en K2 "$1.79 a year" (som op de Pan Pro) bij een plank, molen of deksel | Added to Cart | ~80 (8% van ~990) |
| 9 | Checkout C2 "Need a second opinion on that pan?" (merkbewijs) aan bestaande klanten | Checkout Started | ~70 (11% van ~630) |
| 10 | U1 "Show us your first egg" en N1 "Six months on titanium" aan eerste-orders zonder kookgerei | Delivered / Placed Order +182 d | ~60 per mijlpaal (6% van ~1.000 eerste orders) |
| 11 | C4-US: 12-delige set ($599) als alternatief voor een schort- of plank-cart | Checkout Started | ~60 (US-deel van de accessoire-carts) |
| 12 | Cart K1 met "Mystery Gift $0.00" als product, omdat het eerste Added to Cart-event een automatisch toegevoegde gift is | Added to Cart | ~38 (3,8% van ~990) |
| 13 | C3-P "Make it three / Keep my one pan" bij een pizza steel, roasting pan, deep pan of meerdere pannen onder $300 | Checkout Started | ~48 (6% + 1,5% van ~630) |
| 14 | P3 bij een 2e order overlapt met VIP V1 (dag 30, 15%): twee codes binnen drie weken | Placed Order | ~140 (12% van ~1.150) |
| 15 | P3, R1, R2 tonen USD-prijzen aan buitenlandse kopers | Placed Order | ~425 P3 + ~455 R1 (37% buiten US) |

---

## 1. Checkout abandonment (Checkout Started, ~630 per week)

Huidige route: C1 (1 uur) → C2 (dag 2) → C3-P (< $300) of C3-S (>= $300) → C4-US of C4-INT. Geen split op product of klanttype.

| Wie (voorbeeld) | Aandeel | C1 "Your cart is still here" | C2 "Why Siraat / three questions" | C3 | C4 |
| --- | --- | --- | --- | --- | --- |
| Nieuw, 1 Pan Pro | 44% | Past | Past (bewijs voor de pan) | C3-P: past (één pan of drie) | Past |
| Nieuw, set ($349 tot $599) | 18% | Past | Past | C3-S: past | Past |
| Nieuw, pan + deksel ($193) | ~8% | Past | Past | C3-P "Keep my one pan": **[ORANJE]** deksel genegeerd | Past |
| Nieuw, 1 deep pan / wok / crêpe | 4,4% | Past | Past (zelfde titanium) | C3-P "Make it three: 3 pans + 3 lids": **[ORANJE]** andere vorm dan de set | Past |
| Nieuw, 1 pizza steel of roasting pan | 1,6% | Features "One pan. Nothing to wear off." **[ORANJE]** | "Need a second opinion on that pan?" **[ORANJE]** | C3-P "the pan in your cart", "Upgrade to the 6-piece set" **[ROOD]**: dit is geen pan | 12-pcs als alternatief **[ORANJE]** |
| Nieuw, 2 pannen < $300 | 1,5% | Past | Past | C3-P "Keep my one pan and check out" **[ROOD]** | Past |
| Nieuw, alleen schort ($49) | 2% | Cart klopt, maar features "One pan. Nothing to wear off. Metal utensils, high heat, dishwasher" **[ROOD]** | Onderwerp B "Need a second opinion on that pan?", lab-rapport, anatomie van de pan **[ROOD]** | C3-P: "Make it three. 3 pans + 3 lids for $349", knop "Upgrade to the 6-piece set", "Keep my one pan" **[ROOD]**: $49 cadeau-koper krijgt een $349-upsell | C4-US: "Cooking for a full house? The 12-piece set $599" **[ROOD]**, reviews over de koekenpan |
| Nieuw, alleen snijplank | 4% | idem **[ROOD]** | idem **[ROOD]** (rapport gaat over de pan) | C3-P **[ROOD]** | 12-pcs **[ROOD]** |
| Bestaande klant, alleen snijplank | (44% van de plank-carts) | **[ROOD]** pan-uitleg aan iemand die de pan heeft | **[ROOD]** merkbewijs aan een klant | **[ROOD]** | 12-pcs **[ORANJE]** |
| Nieuw, alleen deksel | 0,2% | **[ROOD]** | **[ROOD]** | **[ROOD]** | **[ROOD]** |
| Nieuw, molen(s) / utensils / trivet / bottle | 8,6% | **[ROOD]** | **[ROOD]** | **[ROOD]** ($19 trivet-cart krijgt de $349-rekensom) | **[ROOD]** |
| E-gift card (koper) | <1% | Cart klopt, features over de pan **[ROOD]** | **[ROOD]** | **[ROOD]** | Code geldt niet op een gift card **[ROOD]** (nakijken) |
| Nieuw, pan + schort ($183) | <1% | Past (pan zit erin) | Past | C3-P: past, schort genegeerd **[ORANJE]** | Past |
| Bestaande klant (elke categorie) | 11% | Past | "Why Siraat?" aan wie al kookt op Siraat **[ROOD]** (~70/week) | C3-P/S: past | Past, maar tweede code naast eventuele P3/VIP-code **[ORANJE]** |
| Internationaal | onbekend (checkout heeft geen land) | Prijzen in USD in de cart-regel **[ORANJE]** | Past | Rekensom in USD ($349, $116 per pan) **[ORANJE]** | C4-INT: past (split op profiel-land) |
| Cart met alleen gratis gifts ($0) | 2% | Lege cart-tabel, knop naar lege checkout **[ROOD]** | **[ROOD]** | **[ROOD]** | **[ROOD]** |

Na tailoring: accessoire-pad C1 (features verborgen) → C2-acc → C3-acc (alleen nieuw) → C4 (12-pcs verborgen). Bestaande klanten slaan C2 over. Pizza/roasting/deep/wok/crêpe en meerdere pannen slaan C3 over. Lege carts uitsluiten met trigger filter.

## 2. Cart abandonment (Added to Cart, ~990 per week)

Huidige route: K1 (1 uur) → K2-new of K2-returning (dag 2) → K3 (dag 3). Productkaart toont alleen het product van het trigger-event.

| Wie | Aandeel | K1 "One wipe. No scrubbing." | K2 | K3 "Your cart, now 10% less" |
| --- | --- | --- | --- | --- |
| Nieuw, Pan Pro | 62% | Past | K2-new "$1.79 a year" (som op de Pan Pro): past | Past |
| Nieuw, set | 17% | Productkaart klopt; schoonmaakuitleg "pan" **[ORANJE]** | Som op één pan van $134 **[ORANJE]** (voetnoot noemt de Pan Pro) | Past |
| Nieuw, deep / wok / crêpe | 8,6% | Past | Som op $134 **[ORANJE]** | Past |
| Nieuw, pizza steel | 0,3% | "One wipe" bij een pizzaplaat **[ORANJE]** | **[ORANJE]** | Past |
| Nieuw, snijplank | 4,9% (71% al klant) | "Nothing to scrub off, no coating on the cooking surface" **[ROOD]** | K2-new "The cheap pan is the expensive one", $134-som **[ROOD]** | Warranty-regel "Dents, a warped base, loose handles" **[ORANJE]** |
| Nieuw, deksel / molen / utensils / schort | 2,7% | **[ROOD]** | **[ROOD]** | **[ORANJE]** |
| Bestaande klant, plank of wok | 71% / 56% van die groep | K1 pan-uitleg aan eigenaar **[ORANJE]** | K2-returning: past | Past |
| Trigger = gratis gift ($0) | 3,8% | Productkaart "Mystery Gift", geen prijs, "HI10 takes 10% off" op een gratis item **[ROOD]** | **[ROOD]** | **[ROOD]** |
| Profiel voegde eerst accessoire, later pan toe | ~2% | Mail gaat over het accessoire, de pan ontbreekt **[ORANJE]** | | |
| Internationaal (31% niet-USD) | ~260 per week | "$199.00" terwijl het S$199 is **[ROOD]** | idem **[ROOD]**; K2-new USD-som **[ORANJE]** | idem **[ROOD]** |

Na tailoring: trigger filter Price > 0; split op Product Name (kookgerei of accessoire, laatste dag); accessoire-pad K1-acc → K3. Prijs alleen bij USD (K1, K2-new, K2-returning, K3 aangepast).

## 3. Browse abandonment (Viewed Product, ~3.000 per week)

Huidige route: B1 (4 uur) → B2-clicked of B2-notclicked (dag 2).

| Wie | Aandeel | B1 "No coating to scratch off" | B2-clicked (code) | B2-notclicked (reviews) |
| --- | --- | --- | --- | --- |
| Nieuw, Pan Pro | 82% | Past | Past | Past |
| Set bekeken (12-pcs, 6-pcs, Complete Edition) | 7,7% | Eyebrow "THE PAN YOU VIEWED", knop "Get 10% off this pan" **[ORANJE]** | "One pan. Nothing to wear off." **[ORANJE]** | Knop "this pan" **[ORANJE]** |
| Deep / wok / crêpe / pizza / roasting | 4,8% | Past (zelfde oppervlak) | Past | Past |
| Snijplank | 2,4% | "Pure titanium cooking surface", vergelijking "coated pan vs Siraat", "Get 10% off this pan" **[ROOD]** | **[ROOD]** | Reviews over eieren **[ROOD]** |
| Deksel (304 stainless) / molen (aluminium) / schort / strips | ~2% | "Pure titanium cooking surface" onder een stalen deksel of een schort: **onjuiste claim** **[ROOD]** | **[ROOD]** | **[ROOD]** |
| Bestaande klant | 16% | Basisuitleg "coated vs Siraat" aan een eigenaar **[ORANJE]** | Past | **[ORANJE]** |
| Internationaal | onbekend | Prijs als tekst "119,00" zonder valuta **[ORANJE]** | | |

Na tailoring: split op Name; accessoire-pad B1-acc → B2-clicked (dynamisch) of einde. B1 en B2-notclicked: "set" of "pan" in knop en eyebrow.

## 4. Welcome (lijst Uw8eZG, ~16.800 per week)

Geen productcontext bij instap. Prospect-pad W1 tot W5 gaat over de pan: past, dat is de bedoeling.
- Koper-pad W0 "Thank you. Now the first egg.": **[ORANJE]** bij wie alleen een accessoire kocht (~10% van kopers). Klein volume in welcome; laten zoals het is, of W0 de P1-logica geven.
- Internationaal: W4-INT bestaat. Past.

## 5. Post-purchase (Placed Order, ~1.150 per week)

Huidige route: P1-first of P1-repeat (1 uur) → P2 (levering + 1 dag) → P3 (dag 14, split pan / set / accessoire) → P4 review.

| Wie | Aandeel | P1 | P2 "If you can do an egg" | P3 (dag 14) |
| --- | --- | --- | --- | --- |
| 1e order, 1 Pan Pro | ~42% | Past | Past | P3-pan "The lid, 10% off": past |
| 1e order, pan + deksel | 11,6% | Past | Past | P3-pan: hero "The lid, 10% off" voor de deksel die al onderweg is **[ROOD]** (~135/week) |
| 1e order, set | ~15% | Past | Past | P3-set "Crepe or wok": past; bij Complete Edition / Set Pro zit crêpe of wok er al in **[ORANJE]** |
| 1e order, wok / deep / crêpe | 6% | Past | Past | Volgens split "single pan": P3-pan "Made for your Pan Pro" **[ORANJE]**; deep 24 cm heeft geen deksel **[ROOD]** |
| 1e order, pizza steel / roasting / pot | 0,7% + pots | Past | Eierles bij een pizzaplaat **[ORANJE]** | Valt buiten de split (geen pan, geen set, geen accessoire) **[ROOD]**: onbepaald pad |
| 1e order, alleen snijplank / molen / utensils | ~5% | "Thank you for choosing a pan", "From order to first egg", chef-tip voorverwarmen **[ROOD]** | Chef-eierles **[ROOD]** | P3-accessory "Now meet the pan": past |
| 1e order, alleen schort | zeldzaam (1 op 800) | **[ROOD]** idem | **[ROOD]** | P3-accessory: "Now meet the pan" past half; cadeau-hoek ontbreekt **[ORANJE]** |
| 1e order, e-gift card | 0 op 800 | **[ROOD]** "pan", gifts in de doos (er is geen doos) | **[ROOD]** | P3-accessory **[ROOD]**: de koper is de gever, de ontvanger is onbekend |
| 1e order, vaatwasstrips | 0,2% | **[ROOD]** | **[ROOD]** | P3-accessory: past half (abonnement is de logische stap, WvRupU) **[ORANJE]** |
| 2e order (12%) | | P1-repeat: past | Past | P3 met THX-code, en op dag 30 VIP V1 met 15%-code **[ROOD]**: twee codes in 16 dagen |
| Accessoire-order van bestaande pan-eigenaar | 3,1% | P1-repeat: past | Eierles opnieuw **[ORANJE]** | P3-accessory "Now meet the pan" aan iemand met een pan **[ROOD]** |
| Internationaal | 37% | Past | Past | Prijzen in USD ("$120.60 $134") **[ROOD]** |

Na tailoring: P1-first dynamisch (intro, tijdlijn, chef-tip alleen bij kookgerei). P2 alleen bij kookgerei. P3-router met zes paden: set, pan zonder deksel (P3-pan), kookgerei + deksel of eigenaar-met-accessoire (P3-next), pizza/roasting/pot of accessoire zonder kookgerei (P3-accessory), schort (P3-apron), gift card en 2e orders (geen P3).

## 6. Winback (Placed Order + 60 en 90 dagen, ~1.230 per week)

| Wie | Aandeel | R1 (dag 60) | R2 (dag 90) |
| --- | --- | --- | --- |
| Pan-koper | ~55% | R1-pan: deksel, 2 Pans + 2 Lids, wok, crêpe: past | Past |
| Pan + deksel | 11,6% | R1-pan biedt de deksel opnieuw aan **[ROOD]** | Past |
| Set-koper | ~20% | R1-set: past | Past |
| Alleen accessoire, nooit kookgerei | ~6% | R1-pan "Two months with your pan", "Fits the Pan Pro you already own" **[ROOD]** | R2 "Where most people go next: Hammered Pan Pro 11", a second pan" **[ORANJE]** |
| Wok / deep / crêpe / pizza | 8,4% | R1-pan: "Fits the Pan Pro you already own" **[ORANJE]** | Past |
| VIP | 16% | Past | R2-VIP: past |
| Internationaal | 37% | USD-prijzen "from $107.10 with HI10" **[ROOD]** | idem **[ORANJE]** |

Na tailoring: R1-acc voor wie nooit kookgerei kocht; R1-pan toont de deksel niet meer aan wie hem al heeft; tekst neutraal.

## 7. De vijf nieuwe flows

| Flow | Wie gaat mis | Wat | Getroffen |
| --- | --- | --- | --- |
| Site abandonment (A1, A2) | Niemand: geen productcontext, gaat over de maatkeuze van de pan | Past. Wel: bestaande klanten zijn al uitgesloten (Placed Order 30 d), maar niet wie langer geleden kocht **[ORANJE]** | |
| Sunset (S1, S2) | Niemand | Product-neutraal, past | |
| VIP (V1, V2) | 2e order, ongeacht product | V1 hero schort, producten deksel/set: past breed. Overlap met P3 bij order 2 **[ROOD]** (zie 5) | ~140/week |
| Anniversary (N1, N2) | Eerste order zonder kookgerei | N1 "Six months on titanium: patina, sticking" bij een plank of molen **[ROOD]** | ~60 per mijlpaal |
| UGC first egg (U1) | Eerste order zonder kookgerei | "Show us your first egg" na een schort of plank **[ROOD]** | ~60/week |

Na tailoring: U1 en N1 krijgen een flow-filter "eerste order bevat kookgerei" (Placed Order Items contains-any kookgerei-titels).

## 8. Vijf echte voorbeelden, mail voor mail

**A. Alleen schort (Oak, $49), nieuw, checkout afgebroken.**
Nu: C1 "Your cart is still here" met de schort in de cart, daaronder "One pan. Nothing to wear off. Metal utensils, high heat, dishwasher." → C2 "Need a second opinion on that pan?" met het lab-rapport en een doorsnede van de pan → C3-P "Make it three: 3 pans + 3 lids for $349", knop "Upgrade to the 6-piece set" → C4-US "Cooking for a full house? The 12-piece set, $599". Vier mails, nul over de schort.
Na: C1 zonder pan-blok → C2-acc "Yours, or a gift? Both work." (canvas, maat, wassen, cadeau-hoek, 30 dagen ruilen) → C3-acc "Most kitchens start with the pan" (zachte brug, cart blijft de knop) → C4 zonder 12-pcs.

**B. Alleen deksel (Stainless Steel Lid, $59), bestaande klant, cart.**
Nu: K1 "Nothing to scrub off, no coating on the cooking surface" onder een stalen deksel → K2-returning "Adding to your Siraat kitchen?": past → K3: past. Prijs: bij een EUR-klant "$39.00".
Na: K1-acc met "304 stainless steel. Match it to your pan's diameter" → K3. Prijs alleen in USD.

**C. E-gift card ($50), checkout.**
Nu: C1 tot C4 over de pan, C4 een kortingscode die op een gift card vermoedelijk niet werkt.
Na: accessoire-pad; C2-acc toont "Sent by email, so it cannot get stuck in the mail. They choose the pan and the size." In post-purchase: geen P3 (UYALJ8 bestaat voor gift cards).

**D. Vaatwasstrips ($25), order.**
Nu: P1 "Thank you for choosing a pan", P2 eierles, P3-accessory "Now meet the pan".
Na: P1 neutraal ("Thank you for ordering from us"), geen P2, P3-accessory (bij een eerste order) of P3-next (als er al een pan is). Abonnement blijft bij WvRupU.

**E. Roasting pan ($199), order.**
Nu: P3-split pan / set / accessoire kent hem niet → geen of een willekeurige P3. Winback R1-pan "Fits the Pan Pro you already own".
Na: P3-accessory ("Now meet the pan": de koekenpan, die heeft hij nog niet) en R1-pan met neutrale dekseltekst.

**F. Pan Pro + schort ($183), checkout.**
Nu en na: kookgerei-pad, C3-P. Past, schort wordt genegeerd. Bewust zo gelaten: de pan is de beslissing.
