# 03 · Winkelwagen, checkout, betaalmethoden en de klik uit de mail

Stand: 7 oktober 2026. Alleen gelezen. Bronnen: Shopify Admin API (paymentSettings, 250 recente orders met gateway en wallet, 100 orders met transacties, actieve kortingscodes, domeinen), Intelligems (funnel, experimenten, offers), Triple Whale (orders, kortingscodes, betaalgedrag per orderwaarde), Klaviyo API (Checkout Started en Placed Order 30 sept tot 7 okt, templates in de repo), Aftersell, Gorgias (7.496 tickets in 60 dagen, waarvan 369 pre-sale), Playwright op de live site (home, PDP's, lege winkelwagen, discount-links).

Wat niet gedaan is: een product in de winkelwagen leggen en de checkout openen. Die stap werd door de permissieregels van deze omgeving geweigerd (handeling in een gekoppelde winkel). De checkout-observaties hieronder komen dus uit data, tickets en de lege winkelwagen. Het visueel nalopen van winkelwagen en checkout staat in 05.

## 1. De cijfers van de laatste twee stappen

| Stap | Per maand | Opmerking |
|---|---|---|
| Winkelwagen gevuld | 17.854 sessies | |
| Winkelwagen verlaten | 9.557 (53,5 %) | mobiel 75,0 % verlaten carts, desktop 69,8 % (inclusief wie nooit checkout start) |
| Checkout gestart | 8.297 | |
| Checkout verlaten | 3.739 (45,1 %) | $867.000 winkelwaarde; IT+DE 66 %, paid search 46 %, email 46 %, paid social 40 % |
| Betaald | 4.558 | |

Klaviyo, geïdentificeerde checkouts (één week): 2.225 profielen, 68 procent betaalt binnen de week. Per valuta: USD 64 procent, AUD 78, SGD 86, CAD 70, GBP 82, EUR 72, CHF 60. Per cartwaarde: onder $100 **29 procent**, $100 tot $199 77 procent, $200 tot $348 80 procent, $349 tot $599 74 procent, $600+ 63 procent.

Twee dingen springen eruit. De carts onder $100 (371 per week, 17 procent) betalen bijna nooit: dat zijn accessoire-carts (deksel $59, board $69) waar de "free gifts" en de upsells niet bij passen, of carts met alleen gift-regels. En carts boven $600 verliezen meer dan het gemiddelde: daar beslissen financiering, levertijd en retourrisico.

## 2. Betaalmethoden

| Methode | Status | Bewijs |
|---|---|---|
| Shop Pay | Actief, dominant | Shopify `supportedDigitalWallets`: SHOPIFY_PAY, APPLE_PAY, GOOGLE_PAY. In 100 recente orders betaalt de grote meerderheid met wallet SHOPIFY_PAY |
| Apple Pay | Actief, circa 20 procent van de kaartbetalingen | wallet APPLE_PAY in de transacties |
| Google Pay | Actief, bijna niet gebruikt (1 van 100) | |
| PayPal | Actief, 9,6 procent van de orders | 24 van 250; één order met eerst een PayPal-FAILURE |
| Shop Pay Installments | Actief in de VS | Live PDP: "4 interest-free installments, or from $12.09/mo with Shop" boven de koopknop op de Pan Pro, "$54.06/mo" op de 12-set |
| Affirm | Bestaat, vrijwel ongebruikt | 1 van 250 orders. Gorgias 86578982: "The Affirm option is not working on my Canadian order"; lopende Affirm-dispute (FI6ZTF8MJ7MMJW30) |
| Klarna / Afterpay / Clearpay | Niet aanwezig | Geen gateway in 250 orders; AU (tweede markt, 609 orders per maand, AOV $192) en UK hebben Afterpay/Clearpay als gewoonte |

Conclusie: voor de VS is BNPL er (Shop Pay Installments) en staat de regel goed op de PDP. Het gat zit buiten de VS: AU, UK, CA, NZ hebben geen herkenbare BNPL, en Affirm werkt niet voor CA. Afterpay (AU, NZ, CA, UK als Clearpay) of Klarna via Shopify Payments toevoegen voor die markten. In de winkelwagen zelf moet bij carts boven $349 dezelfde termijnregel staan ("or 4 x $87.25, interest-free"); of dat zo is, moet visueel gecontroleerd worden (05).

## 3. Verzend- en retourcommunicatie: drie versies van de waarheid

| Waar | Wat staat er |
|---|---|
| PDP (live) | "Delivery From Your Local Warehouse · Fast & free shipping", "Free Express Shipping · from the US", "RISK-FREE PURCHASE: Cook on your pan at home for 30 days, and if it isn't the best pan you've owned, return it for a full refund", "30-Day Returns · free returns" |
| Refund policy (checkout-link) | "Products that have been used cannot be returned for a refund ... Return shipping for unused products is the customer's responsibility" |
| Shipping policy | "free worldwide shipping", "6 to 10 calendar days" (8 tot 14 voor sommige regio's), "In most cases, customers are not required to pay customs duties" |
| Orderbevestiging Europa (Gorgias 92082034) | "shipped from a warehouse outside of Europe. As a result ... VAT or import duties may be charged in some cases" |
| Lege winkelwagen (live) | "Subscribe today to get free shipping" (terwijl verzending altijd gratis is) |
| Tickets | 152 over customs/duties en 91 over herkomst in 60 dagen. Retourkosten van $12,30 tot $30,48 in tickets; klanten verwijzen naar "free returns" en "90 day return policy" |

Gevolg: de koper die de belofte op de PDP gelooft, voelt zich bij retour of douane bedrogen. Dat zie je terug in 6 procent refunds, 12,4 procent refunds op orders boven $700, chargebacks en Affirm-disputes. En wie twijfelt en het beleid in de checkout leest, ziet iets anders dan op de PDP.

Wat moet:
1. Kies één retourbelofte. Optie A: echt gratis retour binnen 30 dagen, ook na gebruik (sterk verkoopargument, kost retourverzending). Optie B: "30-day returns on unused items" en de PDP-tekst "cook on it for 30 days" weg. Wat niet kan is A beloven en B uitvoeren.
2. "Local warehouse" en "from the US" alleen tonen waar het klopt. Anders: "Free tracked shipping, 6 to 10 days".
3. Duties per markt waarmaken: Shopify Markets heeft "duties and import taxes collected at checkout" (DDP) per markt. Voor de EU, CH en NO aanzetten en de orderbevestiging herschrijven. Of die landen uit de advertenties halen: IT, DE, NL, CH, FR, SE samen circa 35.000 sessies per maand met 0,15 tot 0,8 procent CR.
4. Levertijd in de winkelwagen en op de PDP als bereik met datum ("Arrives Oct 14 to 18"), niet als "express".

## 4. Kortingscodeveld en het lekken van codes

Actieve codes in Shopify (status ACTIVE, geen einddatum, voor alle klanten), relevant voor de checkout:

| Code | Waarde | Gebruik | Risico |
|---|---|---|---|
| `98347983474334593` | **99 procent**, onbeperkt | aangemaakt 6 okt, 5 keer gebruikt (Triple Whale: 5 orders, $8,52 omzet, $1.656 korting) | Kritiek. Eén screenshot in een Facebookgroep en de voorraad gaat gratis de deur uit |
| `SRJACEP6YNN1` en `Copy of SRJACEP6YNN1` | **100 procent**, onbeperkt | 1 en 0 keer | Kritiek |
| `SJHNDFJNSAD934` | 100 procent, onbeperkt | 3 keer | Kritiek |
| `9MJ85MRZDE17` | 100 procent, limiet 3 | 1 keer | Hoog |
| EXTRA30 | 30 procent, onbeperkt, sinds BF 2025 | 140 keer | Hoog |
| SK25, B2B25, SORRY25 | 25 procent, alle klanten | | Hoog |
| LABOR20 (sinds 7 sept, nog actief), MEMORIAL, SIRAAT20, EXTRA20 | 20 procent | LABOR20 22 keer in september | Middel |
| BFEXTRA10 (7.626 keer), NYEXTRA10 (3.366), HI10 (1.722), SIRAAT10 (802), COOK10, COOKHAPPY, LABOR10, RAMADAN10, GOODFOOD, PAYDAY10, WINBACK10, CHECKOUT10, FLASH10 | 10 procent, onbeperkt | | Middel: staan op couponsites |

In de 30 dagen: 961 van 5.119 orders (19 procent) gebruikten een code. Top: SUGARCOATEDMASALA 160 (influencer), SIRAAT10 142, HI10 106 (AOV $308), THEGRUMPYCHEF 58, SIRAAT15 55, SIRAAT5 47. Totale korting $135.511, waarvan $58.000 via codes en $77.500 automatisch.

Het zichtbare codeveld in de checkout zet twijfelaars aan het zoeken ("siraat discount code") en kost conversie (ze gaan weg om te zoeken) en marge (ze vinden SIRAAT10 of EXTRA30). Aanpak:
1. Vandaag: de 99- en 100-procentcodes uitschakelen. Daarna EXTRA30, SK25, B2B25, SORRY25, LABOR20, MEMORIAL, BFEXTRA10, NYEXTRA10 een einddatum geven.
2. Flowcodes uniek en eenmalig maken (C4, K3, B2, P3, R2 staan al zo in de nieuwe flows, maar bestaan nog niet in Klaviyo).
3. HI10 is de welkomstcode en blijft, maar met "once per customer".
4. Influencercodes als aparte collab-codes laten staan (die verkopen).

Combinatie-probleem (te verifiëren in 05): HI10, SIRAAT10 en de meeste 10-procentcodes hebben `combinesWith` product = false en order = false. De gratis gifts komen als $0-regels via Bogos, en er draaien automatische kortingen ($77.500 per maand "no code"). Als een automatische productkorting actief is, weigert Shopify de code of kiest de beste van de twee. Ticket 80607829: "The discounts were never applied". Ticket 80427486: "the code doesn't work ... it is capitalizing it". Dit kan precies het moment zijn waarop iemand uit een mail met "10% off" afhaakt.

## 5. Vertrouwen in de winkelwagen en checkout

Wat de data laat zien:
- Herkomst: "Designed in the Netherlands, made in certified facilities in Asia" (macro 247066) staat niet op de site, "local warehouse" wel. Bij de eerste trackingmelding uit China voelt de koper zich misleid. Eerlijk vooraf zeggen kost minder dan de chargebacks.
- Nep-urgentie: de countdown reset per sessie (zie 02). In de checkout hoort geen timer; die moet ook niet in Intelligems-checkoutblokken komen.
- Vergelijkingssite: bestpansreviewed.com en bestpanreviewed.thehiddenstudy.com zijn domeinen van de eigen Shopify-winkel en sturen 8 procent van de geïdentificeerde checkouts aan (176 per week). Een "onafhankelijke" ranglijst die van de winkel zelf is, zonder duidelijke vermelding, is een FTC-risico en, als een koper het ontdekt, een vertrouwensbreuk. Een regel "This comparison is published by Siraat" volstaat.
- Reviews: 4.8 uit 3.281 op de PDP, maar in de winkelwagen en checkout is niets zichtbaar (te bevestigen in 05). Een regel "4.8 from 3,281 reviews · 75-year warranty" onder de checkout-knop in de winkelwagen is een standaard trust-blok.

## 6. Internationale ervaring

- 100 presentment-valuta's actief; de laatste 250 orders: USD 155, AUD 32, SGD 20, GBP 9, EUR 8, HKD 7, CAD 7, NZD 4, AED 3. De flows tonen bedragen altijd in USD (QA-rapport: 13 van 100 checkouts in SGD, CAD, GBP, LBP).
- 12-delige set staat buiten de VS (behalve SG) niet in de catalogus, maar de Aftersell-upsell na aankoop biedt hem aan. Een upsell die bij een niet-US-koper faalt of tot een order leidt die niet geleverd kan worden is verlies (controleren in Aftersell-instellingen).
- EU: conversie 0,15 tot 0,5 procent, 66 procent verlaten checkout, orderbevestiging die invoerrechten aankondigt. Dit is de grootste internationale lek.
- Markt "Shipping Costs To High" bestaat in Shopify Markets: nagaan welke landen daarin zitten en of daar wel of geen verzendkosten worden gerekend; "free worldwide shipping" moet dan per markt kloppen.

## 7. Post-purchase en checkout-upsells (Aftersell en Intelligems)

| Wat | 30 dagen |
|---|---|
| PPU-omzet | $64.459 uit 304 conversies, attach rate 5,9 procent |
| Bereik | 2.247 vertoningen op 5.125 orders (44 procent); show rate 51,8 procent |
| Stap 1 (12-delige set, gemiddeld $559) | 88 keer, $49.176 |
| Downsell (Deep Pan, gemiddeld $71) | 215 keer, $15.253 |
| Stap 2 | 1 keer, $30 |
| Thank-you-page (TYP) | 2.038 vertoningen, 20 conversies (1,0 procent), $7.744 |
| Onderdrukt | "Not eligible" 2.615 sessies (95,5 procent), "No funnel matched" 120 (herstelbaar, plafond circa $4.000 per maand) |

Er is één funnel ("Classic upsell") en die past bij pan-kopers. Wie al een set koopt, een accessoire koopt of buiten de VS zit, krijgt niets. Extra funnels: set-kopers krijgen deksel of snijplank of pizza steel; accessoirekopers de Pan Pro; niet-US de 6-set. Stap 2 vullen (deksel van de maat die net gekocht is). Let op: een ticket (82786829) meldt "I declined the 'deal' for the set" en kreeg toch een openstaand saldo. Eén keer kan toeval zijn, maar een one-click-upsell van $559 die per ongeluk wordt geaccepteerd eindigt in een retour of chargeback. In Aftersell de bevestigingsstap voor bedragen boven $300 aanzetten.

Intelligems: de enige actieve offer is een gratis e-guide (free gift, in test "Volume Offer Test Group"). Geen checkout-blokken gevonden in de lopende tests. Een trust-blok in de checkout ("75-year warranty · 30-day returns · 100,000+ customers") is een goede eerste Intelligems checkout-test.

## 8. De klik-route uit elke flow-mail

Getest op de live site (Playwright, iPhone en desktop, zonder winkelwagen):

| Link | Wat er gebeurt | Probleem | Fix |
|---|---|---|---|
| `/discount/HI10?redirect=/cart` (welcome, K-mails als fallback) | 302 naar `/cart`, cookie `discount_code=HI10` gezet. Op een nieuw apparaat: **"Your cart is empty · Continue shopping"** plus een nieuwsbriefblok "Subscribe today to get free shipping". Nergens staat dat HI10 actief is | Wie uit de mail klikt op een ander apparaat dan waar de cart staat (mail op telefoon, cart op laptop of andersom) komt in een lege winkelwagen zonder producten en zonder bevestiging van de korting | Nooit naar `/cart` linken. Cart-mails: cart-permalink `/cart/<variant_id>:<qty>,<variant_id>:<qty>?discount=CODE` uit de event-items, of de checkout-recovery-URL. Welcome: naar de PDP of een collectie |
| `/discount/HI10?redirect=/products/<pan>` | Landt goed op de PDP, cookie gezet. Geen banner "10% off applied at checkout" | De klant ziet $134 en weet niet of de 10 procent erbij komt; de prijs in de mail ($120,60 na code) staat nergens | Kleine banner bij `discount_code`-cookie: "HI10 · 10% off applied at checkout" (theme-snippet). Intelligems kan dit ook tonen |
| `/discount/K3_10_48H?redirect=/cart` (een code die niet bestaat) | Zelfde 302, cookie `discount_code=K3_10_48H`, geen foutmelding | Een verlopen of verkeerd gespelde flowcode faalt stil: de klant ontdekt het pas in de checkout. Dit geldt nu voor alle v3-codes (C4, K3, B2, P3, R2: "0 coupons in Klaviyo", QA-rapport) | Coupons aanmaken vóór livegang; theme-banner toont alleen geldige codes (via `/discount/...` is dat niet te valideren, dus Klaviyo-coupon moet bestaan) |
| `{{ event.extra.responsive_checkout_url }}&discount=HI10` (C1 en C4) | Recovery-URL `https://siraatskitchen.com/90708771156/checkouts/ac/<token>/recover?key=...` werkt op elk apparaat en herstelt de checkout | Werkt alleen als de code combineert met de automatische gift-kortingen (zie 4). Bij een Intelligems-prijstest kan de herstelde checkout een andere prijs tonen dan de klant zag | Combinatie testen in 05; prijstests nooit tegelijk met een flow die een prijs noemt |
| `/discount/HI10?redirect=/products/titanium-hammered-pan-set-with-lids-6-pcs-bday-sale` | Op iPhone liep de tweede navigatie via `shop.app/accounts/sur` (Shop-herkenning bij tweede bezoek) | Extra redirect voor terugkerende mobiele bezoekers; in deze omgeving faalde die, in het echt kost het tijd | Controleren met een echte iPhone; BDAY-listing redirecten naar de hoofdlisting (zelfde prijs) |
| Added to Cart-event (K-mails) | Event-URL wijst naar `2d0add-d6.myshopify.com`; Klaviyo `full_landing_site` staat bij 1.973 van 2.225 checkouts op het myshopify-domein | Als een link ooit de event-URL gebruikt, landt de klant op het myshopify-domein met een eigen cookie (andere cart) | In templates altijd `siraatskitchen.com` hardcoden; de K-mails doen dat al |

Samengevat: de klik uit een mail landt bijna altijd goed, maar de bevestiging van de korting ontbreekt en de cart-links zijn apparaat-gebonden. De e-mailbezoeker heeft de hoogste koopintentie (CR 2,9 procent) en toch 46 procent verlaten checkouts. Dit is het snelste geld.

## 9. Wat moet er veranderen, op volgorde

1. 99- en 100-procentcodes uit, oude 20 tot 30 procent codes een einddatum (Floris, 15 minuten).
2. Retourbelofte en verzendtekst gelijk trekken op PDP, winkelwagen, policies, orderbevestiging en Gorgias (Floris beslist, Claude schrijft de teksten, dev zet ze).
3. DDP aan voor EU/CH/NO of die landen uit de advertenties (Floris).
4. Cart-mails naar cart-permalinks of recovery-URL; welcome naar PDP (Claude).
5. Banner "code applied" en code-combinatie met gifts oplossen (dev).
6. Afterpay/Clearpay/Klarna voor AU, NZ, UK, CA (Floris, in Shopify Payments).
7. Aftersell: tweede en derde funnel, stap 2, bevestiging boven $300 (Floris).
8. Trust-blok in de winkelwagen en checkout, als Intelligems-test (dev, Claude copy).
