# 04 · Offer- en urgentie-architectuur voor de v3-flows

Datum: 7 oktober 2026. Rol: direct-response strateeg. Alleen gelezen, niets gewijzigd in Klaviyo of Shopify.
Bronnen: DECISIONS.md, klaviyo/flows/v3-flow-system.md, baselines/ (90 dagen), content/hooks/angles.md en hooks.csv, content/reviews/summary.md, content/facts/ (products.csv, facts.csv, policies), research/2026-10-07-checkout-abandonment.md, v3-templates (onderwerpen uit de topcomment), Shopify-kortingscodes via Replo (75 actieve codes bekeken, er zijn er meer), Gethookd (7 zoekopdrachten: HexClad, Caraway, Our Place, Made In, Taima, Okura), Email Love (6 zoekopdrachten).

Taal: analyse in het Nederlands, alle mailcopy in het Engels. Geen gedachtestreepjes.

---

## 0. Samenvatting in vijf zinnen

1. De v3-flows verkopen nu bijna zonder aanbod: checkout C1 tot C4 heeft geen code, cart K1 tot K3 ook niet, en C3 belooft "reserved at today's price" terwijl er geen mechanisme is dat een prijs vasthoudt. Dat laatste moet eruit.
2. Het sterkste aanbod dat we hebben is al gratis: de altijd-aan sale plus de gift-stack (free shipping $15, e-book $30, mystery gift $25, kans op een $450 PFAS-filter, 5 winnaars per week). Dat moet bovenaan elke mail staan, in dollars, niet onderin als strip.
3. Echte urgentie bestaat op drie plekken: (a) unieke Klaviyo-codes per profiel met een echte vervaldatum, (b) de wekelijkse trekking van de PFAS-filter (deadline elke week, mits de actievoorwaarden dat vastleggen), (c) de maand-gift-stack zodra Floris een einddatum geeft. Alles daarbuiten (countdown zonder einde, "low stock", "price held") is niet waar en gaat niet in de mails.
4. Codes horen pas in de laatste mail van een verlatingsflow, met een cooldown van 30 dagen per profiel, zodat niemand leert dat afhaken loont. De data steunt dat: de eerste checkoutmail zonder code doet $4,28 tot $7,86 per ontvanger, de cartmail met "10% off" op dag 2 maar $0,79.
5. Voordat unieke codes enige urgentie hebben, moeten de lekkende publieke codes dicht: BFEXTRA10 (7.626 keer gebruikt, geen einddatum), NYEXTRA10 (3.366), NTWDHPKL5C (5.072), COOK10, COOKHAPPY, EXTRA30 (30 procent, onbeperkt) en drie 100-procent-codes zonder gebruikslimiet. Zolang die werken is "your code expires in 48 hours" technisch waar maar commercieel zwak.

---

## 1. Wat de data zegt over aanbod (baselines, 90 dagen)

| Mail (oud) | Aanbod | Omzet per ontvanger | Les |
| --- | --- | --- | --- |
| Checkout "New AB Checkout 1" / "Don't leave these hanging" | geen code | $7,86 / $5,62 / $4,86 | De beste mail van het account heeft geen korting nodig. Mail 1 = herinnering plus cart. |
| Checkout #3 "Your Order with a Special Extra Bonus" | gift/bonus | $1,34 en $0,80 | Bonus-framing op stap 3 verslaat de merkmail op stap 2 ($0,41 tot $0,73). |
| Checkout #4 "We Can't Keep these Forever" | geen code, urgentiewoorden | $0,68 en $2,11 | Urgentie werkt ook zonder code, maar moet waar zijn. |
| Cart #1 "we saved these for you" | geen code | $2,27 tot $2,90 | idem |
| Cart #2 "getting cooking with 10% off" (COOKHAPPY) | 10%, publiek, geen einde | $0,79 | Code op dag 2 trekt de omzet niet omhoog. |
| Cart #3 "Last Call for 10% Off!" | 10% | $0,97 tot $1,09 | Iets beter dan #2: "last call" helpt, maar het was geen echte last call. |
| Welcome #1 "Thanks For Joining Us" | welkomstcode | $1,78 | Hoogste welcome-RPR. |
| Welcome "Last Call for an Extra 10% Off" | 10%, deadline-framing | $0,26 | Twee keer de bewijsmail ervoor ($0,13). Deadline-framing werkt in welcome. |
| Winback "10% Off Expires Tonight" | 10%, "tonight" | $0,20 | Gelijk aan de nieuwe-productenmail ($0,24). Korting voegt in winback weinig toe. |
| BIS "It's Back!" | echte schaarste | $5,80 tot $9,36 | Echte voorraad-urgentie is de sterkste hefboom in het account. |

Conclusie: korting is geen motor in deze flows, zekerheid en gifts zijn het. Codes horen aan het eind, met een echte deadline, en alleen waar een holdout bewijst dat ze extra omzet maken.

Breakeven-regel voor elke code (aanname brutomarge m, door Floris te bevestigen): een 10%-code is alleen winstgevend als de conversie relatief stijgt met meer dan m / (m - 0,10) minus 1. Bij 60 procent marge betekent dat: de groep met code moet minstens 20 procent vaker converteren dan de groep zonder code. Bij 15 procent korting: 33 procent meer. Daarom bij elke code-test een holdout zonder code.

---

## 2. Wat er in Shopify staat (kortingscodes, gelezen via Replo)

| Code | Wat | Gebruik | Probleem |
| --- | --- | --- | --- |
| HI10 | 10%, onbeperkt, geen einddatum | 1.722 | Bindend (DECISIONS). Publiek, dus geen echte deadline mogelijk. |
| BFEXTRA10 | 10%, onbeperkt, sinds BF 2025 | 7.626 | Meest gebruikte code van de winkel, staat waarschijnlijk op couponsites. |
| NTWDHPKL5C | 10%, één keer per klant, geen limiet | 5.072 | Vermoedelijk oude pop-up-code, nog open. |
| Shopify Collabs default tier | 15% | 5.066 | Creator-codes, buiten scope, wel marge-lek. |
| NYEXTRA10 | 10%, onbeperkt | 3.366 | idem BFEXTRA10 |
| COOK10 / COOKHAPPY / GOODFOOD | 10%, onbeperkt | 236 / 187 / 33 | COOKHAPPY zat in de oude cartflow. |
| EXTRA30 | 30%, onbeperkt | 140 | Te diep om open te laten staan. |
| SRJACEP6YNN1, "Copy of SRJACEP6YNN1", SJHNDFJNSAD934 | 100% off, geen gebruikslimiet | 1 / 0 / 3 | Risico: gratis bestellingen. Direct naar Floris. |
| 9MJ85MRZDE17 | 100% off, limiet 3 | 1 | idem |
| SAVE10, VIP15, THANKS15, SAVE15, CHECKOUT10, THANKYOU10 (pools van 20) | uniek, één gebruik | 0 tot 5 | Bewijs dat unieke pools technisch al werken (Homestead, dec 2024 en mrt 2025), nooit ingezet. |
| THANKYOU{NAAM} (tientallen) | 20%, 1 klant | 0 tot 1 | Service-codes, prima. |

Regels uit facts.csv: één kortingscode per order; free shipping combineert wel. Dus een unieke flowcode vervangt HI10, ze stapelen niet. Dat is goed voor de marge en moet in de copy staan ("One code per order").

Actie voor Floris (niet door mij uitgevoerd): BFEXTRA10, NYEXTRA10, NTWDHPKL5C, EXTRA30, COOK10, COOKHAPPY, GOODFOOD, FLASH10, PAYDAY10, WINBACK10, CHECKOUT10 en de drie 100-procent-codes deactiveren of een einddatum geven. HI10 blijft (besluit), maar krijgt bij voorkeur een eind in de tijd zodra Floris dat wil (zie besluit B hieronder).

---

## 3. Concurrenten: hoe zij aanbod en urgentie bouwen

| Merk | Mechaniek (Gethookd, actief oktober 2026) | Wat we overnemen |
| --- | --- | --- |
| HexClad | "$1,118 OFF + FREE GIFT", "$735 OFF + FREE GIFT" op bundels, gekoppeld aan de Prime Time Sale (echte eventnaam). | Korting in dollars, niet in procenten, en altijd "+ FREE GIFT" erachter. |
| Caraway | "10% off. Everything. Yes, really. ... this never happens." en "Up to 25% off". | Lage procenten, maar zeldzaamheid als argument. Werkt alleen als het echt zelden is: precies het tegenovergestelde van onze altijd-open codes. |
| Our Place | "First Time Ever On Sale: $778 → $485 Titanium Pro Cookware Set", "New Customers Get 10% Off". | Let op: Our Place verkoopt nu een titanium set. "First time ever" en "new customers only" zijn echte grenzen. |
| Made In (Email Love) | "Final Hours to Save", "The best prices of the season end today", "Personalized Sale Picks for You": alleen deadlines bij echte sale-einden. | Deadline-onderwerpen alleen aan het eind van een echt venster. |
| Taima | "up to $200 OFF + FREE GIFT", gratis deksel ($49 doorgestreept), "30 days risk free", maar ook "Stock is running out fast" zonder bewijs. | Gratis add-on als waarde (deksel) wel; neppe schaarste niet. Hun "Did I just get scammed? ... now it's $200 off" toont het risico van eeuwige kortingen: kopers voelen zich bedrogen. |
| Okura | "RESTOCK SALE up to 70% OFF (Ends Today)", Halloween "70% off, bestseller now $89.95", 25-year warranty. | Prijsdruk in de categorie is hoog. Onze verdediging is niet een diepere korting, maar 75 jaar garantie, Light Labs 25895 en de gift-stack. |
| Email Love (Estée Lauder, L.L.Bean, Universal Standard, Hanks Belts) | "Free 8-Piece Gift with your purchase: Ends Tonight", "$15 off $75, ends 9/28", "Your VIP code expires Sunday night PT", "[6 Hour Alert] TWO new customer codes are expiring". | Gift-with-purchase als hoofdaanbod, datum in het onderwerp, persoonlijke code met vervaltijd. |
| Ninja, NEST, Astley Clarke (abandoned cart) | Code meerdere keren in de mail, "Last chance: 15% off your cart", korting en free shipping bovenaan. | Code één keer groot in de hero, één keer bij de CTA, verder niet. |

Patroon: de winnaars zetten het aanbod in de eerste regel, in dollars, met een gift erbij, en geven een deadline die bij een echt event of een persoonlijke code hoort.

---

## 4. De discount ladder

Vier treden. Elke profiel klimt hooguit één trede per 30 dagen.

| Trede | Wat | Wie | Waar |
| --- | --- | --- | --- |
| 0 · Altijd | Sale-prijs + 4 gifts ($70 aan gifts plus de kans op een $450 filter), getoond in dollars per cart of product. 30-day returns, 75-year warranty. | Iedereen, elke mail | Hero van C1, K1, B1, P1-cross-sell, R1 |
| 1 · Gift-upgrade (geen marge-lek op prijs) | Zelfde 4 gifts, maar nu als deadline: "this week's draw closes Sunday". Bij sets: upgrade naar 6-delige set ($349) in plaats van korting. | Iedereen in stap 2 en 3 | C2, C3, K2, B2-not-clicked |
| 2 · 10% | HI10 voor welcome-inschrijvers; unieke 10%-code (48 of 72 uur) voor iedereen die HI10 niet heeft gekregen. | Laatste mail van checkout, cart, browse-clickers, winback R2, post-purchase P3 | C4, K3, B2-clicked, R2, P3, W1/W5 |
| 3 · 15% | Unieke 15%-code, 48 uur. | Alleen: VIP-winback (2+ orders) en de test-arm "set-cart >= $300" in C4. | R2-VIP, C4-S (test) |
| Niet in flows | 20% en hoger, "up to 70%". | Alleen campagnes (BFCM), met echte einddatum van Floris. | Campagnes |

Regels tegen "leren afhaken":
- Nooit een code in de eerste 48 uur na een verlaten checkout of cart. De eerste mails winnen al zonder code.
- Cooldown: wie een flowcode kreeg, krijgt 30 dagen geen nieuwe flowcode (profieleigenschap, zie §7). In die periode toont de laatste mail alleen trede 0 en 1 plus "your code from {date} has expired".
- Codes zijn uniek, één gebruik, alleen one-time purchase products, verlopen echt. Geen code in onderwerpregel als woord "CODE" plus de code zelf (dan kan het niet gelekt worden via screenshots van inboxen).
- Een tweede verlating binnen 30 dagen krijgt nooit een hogere trede dan de eerste.
- Holdout: 10 tot 20 procent van elke code-mail krijgt dezelfde mail zonder code (A/B in de flow). Alleen opschalen als de code-arm de breakeven uit §1 haalt.

Twee besluiten voor Floris:
- **Besluit A (veilig, past in DECISIONS):** HI10 blijft de publieke welkomstcode. Unieke codes alleen in de laatste verlatingsmails, winback en post-purchase.
- **Besluit B (sterker, test):** Welkomstaanbod wordt per profiel een unieke 10%-code die 10 dagen na W1 vervalt. Dan zijn "expires Thursday" in W5 en "last call" waar. HI10 blijft live voor de ads en de site, maar verdwijnt uit de flows. Test als derde arm W1-C naast W1-A en W1-B.

---

## 5. Per flow en per mail

Notatie: **Offer** (wat, hoe groot, waar), **Urgentie** (apparaat en waarom het waar is), **Hero** (label / headline / subline), **Subject A / B · Preview**. Prijzen uit content/facts/products.csv, 7 oktober.

Let op een feitencheck vooraf: in products.csv staat de 6-delige set ACTIVE op $399 (compare-at $1.384), de $349-versie is "BDAY SALE" en UNLISTED. DECISIONS zegt $349. Alle links naar "de $349-set" moeten naar een product dat op dat moment echt $349 toont, anders is C3-P en W4 niet waar.

### 5.1 Welcome (W0 tot W5)

Escalatie: W1 opent met aanbod (pop-up belooft al een giveaway, dus de mail mag direct verkopen) → W2 en W3 bewijs met het aanbod in een P.S. / onderblok → W4 aanbod uitgerekend in prijzen → W5 laatste herinnering met de echte deadline (besluit B) of met de wekelijkse trekking (besluit A).

**W0 · kopers-pad (10 min)**
- Offer: geen. Alleen "your 4 gifts are in the box" als bevestiging.
- Urgentie: geen.
- Hero: label `YOUR ORDER` / "Thank you. Now the first egg." / "Your mystery gift, e-book and draw entry come with your order."
- Subject A "Thank you. Now the first egg." / B "Before your pan arrives: three steps" · Preview "Cold metal grabs your food, hot metal lets it go." (bestaand, houden)

**W1 · prospect (10 min)**
- Offer: 10% bovenop de sale (HI10, of in arm C een unieke code) + 4 gifts. Hero = het aanbod; Pan Pro Standard met prijs "$134 → $120.60 with your 10%" als eerste productkaart. Giveaway-bevestiging in één regel onder de hero.
- Urgentie: besluit A: "This week's PFAS-filter draw closes Sunday at midnight ET. Five winners every week." (waar zodra de actievoorwaarden een wekelijkse sluiting noemen). Besluit B: "Your code is yours until {datum +10 dagen}."
- Hero: label `WELCOME OFFER` / "10% off the sale price. Plus 4 gifts." / "Code HI10 works on top of up to 50% off. Your giveaway entry is in."
- Subject A "Your 10% is inside (plus 4 gifts)" / B "Welcome. 10% on top of the sale, no catch." · Preview "Code HI10 takes 10% off the sale price. Your giveaway entry is in."
- Bestaande test (code-blok tegen gift-card-beeld) blijft; voeg arm C toe bij besluit B.

**W2 · founder note Benjamin (dag 1)**
- Offer: alleen P.S.: "P.S. Your 10% (HI10) still works on top of the sale, and every order ships with 4 gifts."
- Urgentie: geen. Tekstmail blijft tekstmail.
- Hero: geen beeldhero; eerste zin is het verhaal.
- Subject A "Why I started Siraat's Kitchen" / B "The pan nobody else was making" · Preview "First orders shipped December 20, 2024. Here is why." (houden)

**W3 · bewijs (dag 3)**
- Offer: onderblok na het Light Labs-bewijs: code-blok klein plus "4 gifts with every order". Nooit boven het bewijs (Notion do-not: geen aanbod voor de proof beat).
- Urgentie: wekelijkse trekking in één regel naast het gift-blok.
- Hero: label `REPORT NO. 25895` / "Has your cookware actually been tested?" / "Ours has. Three questions to ask any titanium brand."
- Subject A "Has your cookware actually been tested?" / B "Three questions to ask any titanium pan brand" · Preview "Report no. 25895. An ISO/IEC 17025-accredited lab. Here is what it says." (houden; hook ROAS 1,49 op $562k)

**W4-US / W4-INT · drie manieren om te starten (dag 6)**
- Offer: drie kaarten met de prijs na 10% al uitgerekend: Pan Pro Standard $134 → $120.60; 6-delige set $349 → $314.10 (≈ $105 per pan met deksel); US: 12-delige set $599 → $539.10. Een "first piece under $80" (bv. snijplank $69 → $62.10). INT: zonder prijzen (bestaand besluit), wel "10% off with HI10".
- Urgentie: geen nieuwe. Gift-stack-strip.
- Hero: label `THREE WAYS TO START` / "One pan, the set, or the whole kitchen. All 10% less." / "Prices with HI10 already taken off. Free shipping and 4 gifts on all three."
- Subject A "Three ways to start (all 10% less)" / B "One pan for $120.60, or the set for $314" (alleen US) · Preview "Your 10% already taken off. Free shipping and 4 gifts on every order."

**W5 · in their words + laatste herinnering (dag 9)**
- Offer: grote code-hero bovenaan, reviews eronder (Tammy, Marilyn).
- Urgentie: besluit B: "Your 10% expires tomorrow at midnight." (waar, code verloopt dag 10). Besluit A: geen vervaldatum noemen; wel "This is the last email in this series" (waar) en de wekelijkse trekking.
- Hero (B): label `EXPIRES TOMORROW` / "Your 10% ends tomorrow." / "On top of the sale, with 4 gifts. After that, it is the regular sale price." (A): label `LAST REMINDER` / "Your 10% is still here." / "On top of the sale, with 4 gifts. 100,000+ happy customers started this way."
- Subject A "Your 10% expires tomorrow" (B) of "The last note about your 10%" (A) / B "What 100,000+ happy customers found out (and your 10%)" · Preview "Tammy is on her fourth pan. Your code still works until tomorrow night." (B) / "...Your code HI10 still takes 10% off." (A)

Test eerst in welcome: W1-A tegen W1-B (loopt al in de spec), daarna arm C (unieke 10-dagen-code) tegen de winnaar, op placed order rate en omzet per ontvanger na korting.

### 5.2 Checkout abandonment (C1 tot C4, plus C5 als test)

Escalatie: C1 cart + gifts (trede 0) → C2 bewijs + trekking (trede 1) → C3 set-upgrade (P) of gift-stack (S) (trede 1) → C4 unieke code 48 uur (trede 2, of 3 in de S-test) → C5 alleen voor C4-clickers: "expires tonight".

Verwijderen uit de huidige v3: "Reserved at today's price", "Your cart is still at today's price" en "nothing expires tonight" in C3. Shopify houdt geen prijs vast; als de sale wijzigt is de belofte onwaar.

**C1 · 1 uur**
- Offer: cart-blok bovenaan met per regel de doorgestreepte compare-at en "You save $X" (alleen als compare-at een echte eerdere prijs is; anders weglaten), daaronder in één regel "+ 4 gifts with this order ($70 value + a chance at a $450 PFAS filter)". Geen code.
- Urgentie: geen. Zekerheid: ships in 1 business day, 30-day returns.
- Hero: label `SAVED FOR YOU` / "Your cart, plus 4 free gifts." / "Free shipping, a mystery gift, the e-book and an entry in this week's PFAS-filter draw."
- Subject A "Forgetting something?" / B "Your pan (and 4 gifts) are still in your cart" · Preview "Free shipping, a mystery gift and 30-day returns. One click back."

**C2 · dag 2, 09:00**
- Offer: klein cart-blok; gift-strip. Conditioneel blok: profiel zat in welcome (HI10 ontvangen) → "Your HI10 still takes 10% off at checkout." Anders niets.
- Urgentie: trekking: "This week's draw closes Sunday at midnight ET. Orders before then are in." (waar als de actievoorwaarden de weekgrens vastleggen; zie §6).
- Hero: label `WHY SIRAAT` / "Three questions. Three straight answers." / "Lab report no. 25895, a 75-year warranty, and 30 days to return it unused."
- Subject A "Why Siraat?" / B "Need a second opinion on that pan?" · Preview "Well, how much time do you have? Three questions to ask any titanium brand." (houden)

**C3-P · pan-kopers (< $300), dag 3**
- Offer: upgrade in plaats van korting: 6-delige set $349, "about $116 a pan, lid included", tegenover één pan $134 + deksel $59 = $193. Gifts blijven.
- Urgentie: trekking (zelfde regel als C2). Geen prijsgarantie.
- Hero: label `THE MATH` / "3 pans + 3 lids for $349." / "About $116 a pan, lid included. Same 4 gifts, same 75-year warranty."
- Subject A "One pan, or three for $349?" / B "The math on the pan in your cart" · Preview "Three hammered pans and three lids. About $116 a pan, lid included."

**C3-S · set-kopers (>= $300), dag 3**
- Offer: gift-stack groot, in dollars: "$70 in gifts, plus a chance at a $450 PFAS water filter". Cart-blok met "You save $X" op de set.
- Urgentie: trekking. Tweede regel: "Your set ships within 1 business day." (waar voor voorraad).
- Hero: label `INCLUDED WITH YOUR SET` / "Your set, plus $70 in gifts." / "Free shipping, a mystery gift, the e-book and an entry in this week's $450 PFAS-filter draw."
- Subject A "Your set, plus four gifts" / B "$70 in gifts are waiting with your set" · Preview "Free shipping, a mystery gift, the e-book and this week's draw. 30-day returns."

**C4-US / C4-INT · dag 4, laatste mail**
- Offer: trede 2. Unieke 10%-code (Klaviyo-pool, 48 uur), automatisch toegepast via de link `/discount/{code}?redirect=/checkout`. Profielen met HI10 (welcome-lijst) krijgen in plaats daarvan de HI10-herinnering, geen tweede code (ze hebben al 10%, één code per order). Cooldown-profielen krijgen alleen de gifts. Test-arm S: 15% voor carts >= $300.
- Urgentie: echte vervaltijd van de code, als datum in de mail ("Expires {weekday} at {time} ET"). Plus de trekking.
- Hero: label `YOUR CODE · EXPIRES {DAY} {TIME}` / "10% off your cart. 48 hours." / "Already applied. On top of the sale price, with all 4 gifts. One use, just for you."
- Subject A "10% off your cart, for 48 hours" / B "Final call: your cart, 4 gifts and 10% off" · Preview "Your personal code is already applied. It expires {day} at midnight ET."
- US: 12-delige set blijft als alternatief onderin (besluit: geen backorder-waarschuwing nodig).

**C5 · test, +40 uur na C4, alleen wie C4 opende of klikte en niet kocht**
- Offer: dezelfde code.
- Urgentie: "expires tonight" (waar: code verloopt binnen 8 uur).
- Hero: label `EXPIRES TONIGHT` / "Your 10% ends at midnight." / "Your cart and 4 gifts are one click away."
- Subject A "Your code expires tonight" / B "8 hours left on your 10%" · Preview "After midnight it is the regular sale price. Your cart is saved."

Test eerst in checkout: C4 met unieke 48-uurs-code tegen C4 zonder code (gifts + trekking), 50/50, winnaar op omzet per ontvanger na kortingskosten. Daarna C5 aan of uit. Daarna in tak S: 10% tegen 15%.

### 5.3 Cart abandonment (K1 tot K3)

Escalatie: K1 waarde + gifts → K2 kosten per jaar + gifts → K3 unieke 10%-code 48 uur (of HI10-herinnering). Geen K4.

**K1 · 1 uur**
- Offer: cart-blok met "You save $X" + gift-regel. Geen code.
- Urgentie: geen.
- Hero: label `IN YOUR CART` / "One wipe. No scrubbing. 4 gifts included." / "Your cart is saved, with free shipping, a mystery gift and 30-day returns."
- Subject A "One pass with a damp cloth." / B "About cleaning the pan in your cart" · Preview "No scrubbing. That is the whole trick. And 4 gifts ship with it." (houden, preview aangevuld)

**K2-new / K2-returning · dag 2**
- Offer: K2-new: kosten-per-jaar-tabel ($30 pan x 5 tegen één pan, 75 jaar gedekt) met de cart-prijs ingevuld; gift-strip. K2-returning: kort, "same 4 gifts as last time", HI10/geen code.
- Urgentie: trekking.
- Hero (new): label `THE REAL PRICE` / "The pan you keep replacing is the expensive one." / "One pan, covered for 75 years. Today with 4 gifts."
- Subject A "The pan you keep replacing is the expensive one" / B "What a pan really costs per year" · Preview "A coated pan lasts a few years. This one is covered for 75." (houden)

**K3 · dag 3, laatste mail**
- Offer: trede 2 als in C4 (unieke 10% 48 uur, of HI10-herinnering, of alleen gifts bij cooldown).
- Urgentie: echte vervaltijd.
- Hero: label `YOUR CODE · 48 HOURS` / "Covered for 75 years. Now 10% less." / "Your personal 10% is applied to your cart. Returnable for 30 days. Expires {day}."
- Subject A "10% off your cart (expires {day})" / B "Covered for 75 years. Returnable for 30 days. 10% less." · Preview "Your code is already applied. Not for you? Send it back unused within 30 days."

Test eerst in cart: K3 met code tegen K3 zonder code. Oude data suggereert weinig lift van codes in cart; laat de holdout het bewijzen.

### 5.4 Browse abandonment (B1, B2)

Escalatie: dag 0 educatie + HI10-herinnering (alleen voor wie HI10 heeft) → dag 2 split: clickers krijgen een unieke 48-uurs-code, niet-clickers reviews + gifts.

**B1 · 4 uur**
- Offer: product dynamisch met sale-prijs en "+ 4 gifts". Conditioneel blok: welcome-lid → "Your HI10 takes another 10% off."
- Urgentie: geen.
- Hero: label `YOU LOOKED AT` / "{{ product }}: no coating to scratch off." / "Metal utensils welcome. Ships with 4 gifts, 30-day returns."
- Subject A "The pan with nothing to scratch off" / B "What a metal spatula does to your pan" · Preview "Metal utensils, no coating. And 4 gifts ship with it." (licht aangepast)

**B2-clicked · dag 2**
- Offer: unieke 10%-code, 48 uur (vervangt HI10 in de huidige template; HI10 is publiek en kan geen deadline dragen). HI10-profielen: HI10-herinnering.
- Urgentie: vervaltijd.
- Hero: label `48 HOURS ONLY · YOUR CODE` / "10% off the {{ product }} you looked at." / "On top of the sale price, with 4 gifts. Expires {day} at midnight ET."
- Subject A "10% off the pan you looked at (48 hours)" / B "Still thinking it over? Here is 10%." · Preview "A personal code, on top of the sale. It expires {day}."

**B2-notclicked · dag 2**
- Offer: geen code. Reviews + gift-stack.
- Urgentie: trekking.
- Hero: label `IN THEIR WORDS` / "Week one, in their words." / "Plus what ships with every order: 4 gifts and 30-day returns."
- Subject A "Week one, in their words" / B "What people wrote after the first egg" · Preview "The first egg, the second pan, the fourth." (houden)

Test eerst in browse: B2-clicked code tegen geen code; daarna code-timing dag 2 tegen dag 1.

### 5.5 Post-purchase (P1 tot P4)

Escalatie: geen korting tot het product binnen is en werkt. Pas P3 (dag 14) een unieke thank-you-code met 14 dagen looptijd op het bijpassende accessoire.

**P1 · 1 uur**
- Offer: geen code. Bevestig de 4 gifts (vermindert spijt, ondersteunt de 30 dagen).
- Hero: label `ORDER CONFIRMED` / "Good call. Here's what's coming." / "Your pan, your mystery gift, the e-book and your entry in this week's draw."
- Subject A "Good call. Here's what's coming." / B "You bought a pan from an ad. Good call." · Preview "Order confirmed. What is in the box, your 4 gifts, and when it ships." (houden)

**P2 · levering + 1 dag**
- Offer: geen. Techniek (eitje). Grootste bezwaar is plakken; een kortingsmail hier zou verkeerd vallen.
- Subject A "If you can do an egg, you can do anything" / B "First egg: heat first, then a thin layer of oil" (houden)

**P3-pan / P3-set / P3-accessory · dag 14**
- Offer: unieke 10%-code, 14 dagen geldig, op de cross-sell: deksel $59 → $53.10, 2 Pans + 2 Lids $199, snijplank vanaf $69. P3-accessory: Pan Pro Standard $134 → $120.60. Hero = het passende product met de prijs na code.
- Urgentie: "Your thank-you code works until {datum}" (waar, 14 dagen na toewijzing).
- Hero (pan): label `FOR CUSTOMERS ONLY · UNTIL {DATE}` / "The lid that fits your pan. 10% off." / "Your thank-you code, already applied. Valid until {date}."
- Subject A "The one thing your pan is missing (10% off)" / B "Which lid fits your pan? Your thank-you code inside" · Preview "Your customer code takes 10% off the lid, the board or a second pan. Until {date}."

**P4 · review request (live flow XzHrez)**: ongewijzigd, geen aanbod.

Test eerst in post-purchase: P3 met code tegen zonder code (cross-sell-RPR is nu $0,12 tot $0,58 per mail).

### 5.6 Winback (R1, R2, plus R3 als test)

Escalatie: R1 nieuw, geen code → R2 unieke code 72 uur (10%, VIP 15%) → R3 alleen voor R2-clickers "expires tonight".

**R1-pan / R1-set · dag 60**
- Offer: geen code. "Every order still ships with 4 gifts" onder de nieuwe producten.
- Hero: label `NEW SINCE YOUR LAST ORDER` / "Three things we made since your pan." / "Same titanium surface, same 75-year warranty, 4 gifts with every order."
- Subject A "New since your last order" / B "Three things we made since your pan" (houden)

**R2 · dag 90 (niet-VIP)**
- Offer: unieke 10%-code, 72 uur, plus de gifts. Producten met prijs na code.
- Urgentie: vervaltijd.
- Hero: label `YOUR CODE · 72 HOURS` / "10% off your next piece." / "On top of the sale, with 4 gifts. Expires {day} at midnight ET."
- Subject A "10% off your next piece (72 hours)" / B "Up to 50% off. What's the catch?" · Preview "Your personal code, on top of the sale. Free shipping and 4 gifts. Expires {day}."
- Alleen versturen terwijl "up to 50% off" echt live is (bestaande regel).

**R2-VIP · dag 90 (2+ orders)**
- Offer: unieke 15%-code, 72 uur (vervangt HI10: een publieke code is geen VIP-bedankje).
- Hero: label `FOR OUR REGULARS · 72 HOURS` / "15% off, because you came back." / "A code just for you, on top of the sale, with 4 gifts. Expires {day}."
- Subject A "A thank you: 15% on top of the sale" / B "For our regulars: 15% for 72 hours" · Preview "You have ordered more than once. This code is yours until {day}."

**R3 · test, +60 uur, alleen R2-clickers**
- Subject A "Your code expires tonight" / B "Last hours on your 15%" (VIP) · Hero label `EXPIRES TONIGHT` / "Your code ends at midnight." / "Your next piece, 4 gifts, 30-day returns."

Test eerst in winback: R2 met code tegen R2 zonder code (de oude data laat bijna geen verschil zien).

---

## 6. Urgentie: wat waar is en hoe je het waar maakt

| Apparaat | Status | Hoe waar maken | Gebruik |
| --- | --- | --- | --- |
| Unieke code met vervaltijd | Kan direct | Klaviyo-coupon (Shopify, unique), vervalt X dagen na toewijzing; Klaviyo maakt de code in Shopify met einddatum. | C4, C5, K3, B2-clicked, P3, R2, R3, W1-C/W5 (besluit B) |
| Wekelijkse PFAS-filter-trekking | Kan, na check | Actievoorwaarden (official rules) met: wekelijkse sluitingstijd (bv. zondag 23:59 ET), 5 winnaars, waarde $450, landen, en in de VS een gratis deelnamemogelijkheid (no purchase necessary), anders is "chance to win with your order" juridisch een loterij. Ik vond geen voorwaarden in de repo. Link naar de voorwaarden in elke mail die de trekking noemt. Alleen "win", nooit "free" (besluit). | C1 tot C4, K1, K2, B2, W1, W3, P1 |
| Maand-gift-stack ("October: 4 gifts") | Wacht op Floris | Einddatum oktoberactie is nog onbekend (besluit 7 okt). Zodra er een datum is: universal content block "offer of the month" met datum, centraal te wisselen. | Alle flows, als regel onder de hero |
| Verzendtempo | Waar | "Ships within 1 business day" (voorraad). In Q4 echte kerst-cut-offs per markt. | C1, C3-S, K1 |
| "Price held / reserved at today's price" | Niet waar | Shopify reserveert geen prijs. Verwijderen. | Nergens |
| "Low stock / selling fast" | Niet waar | Geen voorraadgrens bekend. Alleen bij echte BIS-situaties. | Nergens |
| Countdown-GIF | Alleen bij echte einddatum | Alleen als de timer naar de codevervaltijd of een sale-einde van Floris telt; nooit een loop-timer. | C5, R3, campagnes |

Tijdzone: codes vervallen op toewijzingstijd plus N dagen; schrijf in de copy de dag ("expires Friday"), niet het uur, tenzij getest in de preview, of reken met een vast tijdstip (verzending om 09:00 lokaal, vervalt na 2 dagen = "Friday morning"). Veilig alternatief: "valid for 48 hours from this email".

---

## 7. Klaviyo-setup

**Coupon-pools (Klaviyo > Coupons > Create coupon > Shopify > unique codes)**

| Pool | Prefix | Korting | Geldig | Shopify-instellingen |
| --- | --- | --- | --- | --- |
| SK_CART10_48H | CART- | 10% | 2 dagen na toewijzing | one-time purchase products, 1 gebruik, 1 per klant |
| SK_CHECKOUT10_48H | CO- | 10% | 2 dagen | idem |
| SK_CHECKOUT15_48H_SET | COS- | 15% | 2 dagen | idem, minimum $300 |
| SK_BROWSE10_48H | VIEW- | 10% | 2 dagen | idem |
| SK_THANKS10_14D | THX- | 10% | 14 dagen | idem |
| SK_WINBACK10_72H | BACK- | 10% | 3 dagen | idem |
| SK_VIP15_72H | VIP- | 15% | 3 dagen | idem |
| SK_WELCOME10_10D (besluit B) | HELLO- | 10% | 10 dagen | idem |

In de template: `{% coupon_code 'SK_CART10_48H' %}`. Gebruik dezelfde tag voor het code-blok en de auto-apply-link (`https://siraatskitchen.com/discount/{% coupon_code 'SK_CART10_48H' %}?redirect=/checkout`) en controleer in de preview dat het dezelfde code is. Pools krijgen nooit een einddatum op de pool zelf zonder dat de flow wordt aangepast.

**Profieleigenschappen en filters**
- Flow-actie "Update profile property" direct na elke code-mail: `last_flow_code_at` = vandaag, `last_flow_code_pool` = poolnaam.
- Conditionele split vóór elke code-mail: `last_flow_code_at` in de laatste 30 dagen → tak "gifts only"; `is in list Uw8eZG` (HI10 ontvangen) en niet besluit B → tak "HI10 reminder"; anders → tak "unique code".
- C5 en R3: trigger-split "opened or clicked previous email since flow start" plus Placed Order = 0.
- Holdout: A/B test in de flow-mail (variant zonder code-blok, 15 procent), winnaar op placed order value per recipient, na 30 dagen beoordelen met kortingskosten erbij (Shopify-rapport per pool-prefix).

**Conditionele blokken in de templates**
- Code-blok: `{% if person|lookup:'last_flow_code_pool' == 'SK_CART10_48H' %}` is niet nodig als de split per tak een eigen template heeft. Aanbevolen: drie varianten per laatste mail (code / HI10 / gifts only) in plaats van logica in één template. Simpeler te QA'en.
- HI10-regel in C2 en B1: show/hide-blok "show if profile is in list Uw8eZG".
- Universal content blocks: "Gift stack" (4 gifts met waarden en de trekkingregel), "Offer of the month" (leeg tot Floris een datum geeft), "Trust strip" (30-day returns, 75-year warranty, free shipping). Wijzigen op één plek.

**Rapportage**: per pool-prefix in Shopify (orders met kortingscode beginnend met CART-, CO-, enz.) naast Klaviyo-RPR. Daarmee is de kostenkant zichtbaar.

---

## 8. Wat eerst testen (volgorde)

1. **C4: unieke 10%-code 48 uur tegen geen code** (checkout heeft de hoogste RPR, dus het grootste absolute effect). 50/50, minimaal 2 weken of 400 ontvangers per arm.
2. **W1: A (code-blok) tegen B (gift card)**, daarna arm C (unieke 10-dagen-code, besluit B) tegen de winnaar.
3. **K3: code tegen geen code.**
4. **C5 aan tegen uit** (expires tonight voor C4-clickers).
5. **C4-S: 10% tegen 15%** op carts >= $300.
6. **B2-clicked, P3, R2: code tegen geen code**, parallel, kleinere volumes.
7. Onderwerp-tests per mail zoals hierboven, pas nadat de aanbodtest per mail beslist is (één variabele tegelijk).

---

## 9. De vijf belangrijkste veranderingen

1. Gifts en sale in dollars bovenaan elke verkoopmail ("Your cart, plus 4 free gifts"; "$70 in gifts plus a chance at a $450 PFAS filter"), niet als strip onderaan.
2. Unieke, verlopende Klaviyo-codes alleen in de laatste mail van checkout, cart, browse-clickers, winback en P3, met 30 dagen cooldown en een holdout. Geen code in de eerste 48 uur.
3. "Reserved at today's price" en elke andere niet-waargemaakte urgentie eruit; echte urgentie = codevervaltijd, wekelijkse trekking (na actievoorwaarden met gratis deelnamemogelijkheid) en de maandactie zodra Floris een einddatum geeft.
4. Lekkende publieke codes dicht (BFEXTRA10, NYEXTRA10, NTWDHPKL5C, EXTRA30, COOK10, COOKHAPPY e.a.) en de drie 100-procent-codes zonder limiet direct naar Floris.
5. Besluit B voorleggen: welkomstaanbod als unieke 10-dagen-code naast HI10 testen, zodat W5 een echte "expires tomorrow" krijgt; en de $349 tegenover $399 van de 6-delige set rechttrekken voordat C3-P en W4 live gaan.
