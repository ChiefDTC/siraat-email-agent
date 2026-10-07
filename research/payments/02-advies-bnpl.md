# 02 · Advies termijnbetalen (BNPL) per markt

Datum: 7 oktober 2026. Basis: `01-inventaris.md` en `per-markt.csv`. Alleen gelezen, niets gewijzigd. Bedragen in USD tenzij anders vermeld. Kosten en lift zijn bandbreedtes; alles met "aanname" moet Floris of de leverancier bevestigen.

## Kern in vijf regels

1. Termijnbetalen bestaat al in de US (Shop Pay Installments, 5,2% van de orders) en in UK en EU (Klarna via Shopify Payments). De eerdere diagnose "geen BNPL" klopt niet; Klaviyo verstopt beide onder `shopify_payments`.
2. Het echte gat zit in AU en CA: geen enkele termijnoptie behalve PayPal Pay in 4, en de laagste checkout-voltooiing na SG (AU 45%, CA 38%, US 53%).
3. Advies: AU eerst met Afterpay via cross-border trade op een US-account, CA vier weken later als tweede stap. In de US geen nieuwe aanbieder, wel de bestaande termijnregel sterker tonen in cart en mails.
4. De breakeven ligt laag: Afterpay in AU verdient zichzelf terug bij 0,2 tot 0,6 procent extra omzet, onafhankelijke studies wijzen op 3 tot 14 procent.
5. Testen kan per markt maar met weinig statistische kracht; daarom een getrapte uitrol (AU, dan CA) met verschil-in-verschil tegen de andere markt, plus een 50/50 PDP-test in de US.

---

## 1. Analyse: iOS, Android en webview

### Orders (Klaviyo, 90 dagen, 17.674 webshop-orders)

| Apparaat | Aandeel orders | AOV | PayPal-aandeel |
|---|---|---|---|
| iOS browser (Safari, Chrome iOS) | 31,7% | $236 | 9,2% |
| iOS webview (Facebook, Instagram) | 31,1% | $185 | 6,9% |
| Mac desktop | 10,8% | $226 | 11,3% |
| Android browser | 10,2% | $229 | 10,7% |
| Windows desktop | 8,0% | $243 | 12,9% |
| Android webview | 6,7% | $184 | 8,7% |
| Android Samsung Internet | 1,1% | $252 | 14,3% |

Webview levert 38 procent van de orders, met een AOV die 20 procent lager ligt. Dat is de impulskoop van één pan uit Meta, niet per se een betaalprobleem.

### Checkout-voltooiing per browser (Shopify sessions, alle markten, 30 dagen)

| OS en browser | Sessies | Conversie per sessie | Checkout voltooid (van gestart) |
|---|---|---|---|
| iOS Instagram-webview | 25.967 | 2,3% | 58% |
| iOS Facebook-webview | 51.079 | 1,9% | 54% |
| Android Instagram-webview | 3.304 | 2,1% | 53% |
| Mac Safari | 13.941 | 1,8% | 52% |
| Android Facebook-webview | 20.345 | 1,7% | 51% |
| Windows Chrome | 17.095 | 1,4% | 50% |
| iOS Safari | 57.298 | 1,5% | 44% |
| Android Chrome | 37.543 | 1,0% | 39% |
| Samsung Internet | 4.200 | 1,1% | 35% |
| iOS Chrome | 12.913 | 1,4% | 34% |

### ATC-cohort (Klaviyo, bekende profielen, eerste ATC 7 t/m 29 sep, order binnen 7 dagen)

| Apparaat bij ATC | Profielen | Naar order |
|---|---|---|
| Desktop | 673 | 40,0% |
| iOS Safari | 803 | 33,7% |
| iOS webview | 1.893 | 33,6% |
| Android webview | 542 | 32,3% |
| Android Chrome | 553 | 27,8% |
| Samsung Internet | 84 | 16,7% |

Per markt: in de US converteert iOS webview (33%) slechter dan iOS Safari (39%) en desktop (46%); in AU juist beter (41% tegen 31%). AU-carts boven A$350 converteren 13% (n=47) tegen 33% voor US-carts boven $350 (n=292); te klein voor een harde conclusie, wel in lijn met een ontbrekende termijnoptie bij grote bedragen.

### Wat dit zegt

- **Webview is in de checkout niet het grootste lek.** Wie vanuit Facebook of Instagram een checkout start, maakt die vaker af dan wie in Safari start (Shop Pay werkt in de webview, het meeste verkeer is warm). De webview-wrijving zit eerder in de stap van sessie naar checkout en in de lagere AOV. Kanttekening: als Shop Pay de koper naar Safari doorstuurt, kan Shopify de voltooiing aan de webview-sessie toerekenen.
- **Android Chrome, Samsung Internet en iOS Chrome zijn de zwakke plekken.** Dat zijn de browsers zonder Apple Pay. Google Pay staat aan maar wordt bijna niet gebruikt (US: 19 orders tegen 431 Apple Pay). Eerste controle: verschijnt de Google Pay-knop in de checkout en als express-knop op Android Chrome?
- **Termijnen en Android.** Termijnbetalen trekt vooral kopers met minder krediet (Berg e.a., zie bronnen). Dat profiel overlapt met Android en met het pan-voor-$134-segment. Dat is een reden om de termijnregel juist op mobiel en in de cart zichtbaar te maken.

### Welk deel van de verliezen past bij een ontbrekende methode

Model: verlaten checkout-sessies per markt (Shopify, 30 dagen) maal het deel dat afhaakt omdat de gewenste methode ontbreekt, maal de helft die met die methode wel zou kopen, maal AOV. Baymard (2025) meet dat ongeveer 10 procent van de afhakers "not enough payment methods" noemt; waar termijnen al bestaan (US, UK) zet ik dat lager.

| Markt | Verlaten checkout-sessies / maand | Aandeel door ontbrekende methode (aanname) | Omzet per maand die erbij past |
|---|---|---|---|
| US | 2.450 | 2 tot 4% | $6.000 tot $12.000 |
| AU | 674 | 6 tot 10% | $3.900 tot $6.400 |
| CA | 431 | 5 tot 9% | $2.000 tot $3.600 |
| SG | 396 | 4 tot 8% | $1.800 tot $3.700 |
| UK | 67 | 2 tot 5% | $140 tot $340 |

In de US gaat het dan niet om termijnen (die zijn er) maar om Google Pay op Android, Venmo of Klarna-gewoontes. In AU en CA is termijnbetalen het voor de hand liggende ontbrekende stuk.

---

## 2. Wat de bronnen zeggen over effect (onafhankelijk eerst)

| Bron | Soort | Effect |
|---|---|---|
| Berg, Burg, Keil, Puri, Journal of Financial Economics 2025 | Academisch, Duitse webwinkel, quasi-experiment | BNPL verhoogt verkoop met ongeveer 20%, vooral via klanten met lage kredietwaardigheid; baten groter dan kosten |
| Stripe, A/B over 150.000+ checkout-sessies | Betaalverwerker, geen BNPL-verstrekker; echte 50/50 | Tot 14% meer omzet als BNPL in de checkout wordt getoond, via conversie en AOV; grootste effect bij orders van $500 tot $1.500 |
| Baymard 2025 | Onafhankelijk UX-onderzoek | Ongeveer 10% van checkout-afhakers noemt te weinig betaalmethoden |
| Worldpay Global Payments Report 2025 | Marktdata | BNPL ongeveer 6% van US e-commerce (2024) |
| Leveranciers (Afterpay, Klarna, Shopify) | Eigen claims, zelfselectie | 20 tot 50% hogere AOV en 20 tot 30% hogere conversie bij gebruikers; niet te vertalen naar winkelniveau |

Mijn bandbreedte voor Siraat, voorzichtig omdat PayPal Pay in 4 al een deel dekt en omdat Siraat's eigen termijnkopers juist kleinere orders doen (Shop Pay Installments AOV $231):

| Situatie | Conversie | AOV | Omzet |
|---|---|---|---|
| Markt zonder termijnen krijgt er een (AU, CA) | +2 tot +5% | +1 tot +3% | +3 tot +8% (AU), +2 tot +6% (CA) |
| Termijnen bestaan, alleen beter zichtbaar (US, UK) | +0,5 tot +1,5% | 0 tot +1% | +0,5 tot +2% |

---

## 3. Advies per markt

### Australia (12% van orders) · eerste markt

- **Aanbieder: Afterpay** via Cross Border Trade op een US-Afterpay-account. Afterpay is in AU de norm; Cross Border Trade laat een US-winkel AU-kopers bedienen, de koper ziet het schema in AUD, uitbetaling in USD. Klarna kan voor AU-kopers niet via Shopify Payments en vraagt een directe overeenkomst; Shop Pay Installments is er niet.
- **Kosten:** standaard 6% + $0,30 (bandbreedte 4 tot 6%), plus een cross-border-toeslag volgens contract (aanname 1 procentpunt). Tegen een internationale kaart via Shopify Payments (aanname 4,9%: basis 2,4% + 1% internationaal + 1,5% valutaconversie) is het verschil ongeveer 2,1 procentpunt.
- **Direct en gratis:** PayPal Pay Later-messaging aanzetten voor AU (Pay in 4 kost de winkel niets extra). Te controleren in de PayPal-instellingen van Shopify of dat voor AU beschikbaar is.
- **Verwachte lift:** omzet +3 tot +8%, dus $3.400 tot $9.100 per maand op $114.000.

### Canada (5%) · tweede markt

- **Aanbieder: Afterpay** via dezelfde cross-border-account (CA zit in het programma). Shop Pay Installments vraagt een Canadese entiteit. Klarna niet via Shopify Payments voor CA.
- **Kosten:** als AU, verschil ongeveer 2,1 procentpunt.
- **Lift:** +2 tot +6% omzet, $1.000 tot $3.100 per maand. CA heeft daarnaast een groter checkout-lek (38% voltooid) dat niet alleen aan betalen ligt; verzendtijd en douane eerst uitsluiten.

### United States (64%) · geen nieuwe aanbieder, wel zichtbaarheid

- **Aanbieder: Shop Pay Installments houden** (5,9% + $0,30 standaard; Plus kan onderhandelen). Klarna kan voor US-kopers nog niet via Shopify Payments; Afterpay erbij zou dezelfde kopers splitsen en meer kosten.
- **Affirm-app:** $6.300 per maand, AOV $333. Zelfde financier als Shop Pay Installments. Voorstel: laten staan tot de test klaar is, dan vergelijken of die kopers zonder de app via Shop Pay Installments kopen. Kosten van houden zijn klein.
- **Zichtbaarheid:** de PDP toont al "4 payments of $33.50" onder de prijs. Toevoegen: dezelfde regel in de cart drawer (nu Affirm-tekst), in de checkout- en cart-mails, en bij sets een maandbedrag. Prequalificatie aanzetten (staat uit) is een optie om te testen.
- **Lift:** +0,5 tot +2% omzet, $4.000 tot $16.000 per maand op $791.000.

### United Kingdom (4%) · bestaand Klarna zichtbaar maken

- **Aanbieder: Klarna via Shopify Payments** staat al aan (4 orders per maand). Het Klarna-messaging-script staat in de theme maar toont niets op de PDP. Eerst dat repareren: "Pay in 3 interest-free payments of £xx with Klarna".
- **Regels:** sinds 15 juli 2026 valt BNPL in de UK onder de FCA. De tekst moet de goedgekeurde Klarna-formulering zijn, met de verplichte kredietwaarschuwing. Geen eigen variaties in mails.
- **Clearpay** (Afterpay UK) via cross-border kan later, alleen als Klarna-messaging niets doet.
- **Lift:** +0,5 tot +2%, $200 tot $700 per maand. Lage prioriteit.

### Singapore (4%) · eerst iets anders oplossen

- Lokale leider is Atome; Afterpay en Klarna zijn er niet. Of een US-winkel Atome kan krijgen is onbekend (vraag aan Atome).
- SG heeft de laagste conversie (1,0%) en checkout-voltooiing (32%). PayPal wordt nauwelijks gebruikt (3%). Waarschijnlijker oorzaken: verzendkosten of levertijd in de checkout, prijs in USD versus SGD. Eerst een checkout-walkthrough, termijnen pas daarna.

### Waar de boodschap staat

| Plek | US | AU en CA (na livegang) | UK |
|---|---|---|---|
| PDP onder de prijs | Bestaat: "or 4 payments of $33.50" | "or 4 interest-free payments of A$xx with Afterpay" | "Pay in 3 interest-free payments of £xx with Klarna" |
| Cart drawer | Shop Pay Installments-regel naast het totaal (nu Affirm-tekst) | Afterpay-regel naast het totaal | Klarna-regel |
| Checkout | Staat er | Afterpay als betaaloptie | Staat er |
| Mails (checkout, cart, browse) | Regel onder de cart: "or 4 interest-free payments of $33.50 with Shop Pay" plus een kleine voetnoot over geschiktheid | Alleen tonen aan AU- of CA-profielen, bedrag in lokale valuta of zonder bedrag | Alleen met Klarna-formulering, of weglaten |
| Sets ($349, $599) | Maandbedrag noemen: "from $xx/month" (rentedragend, dus met APR-verwijzing) of 4 x $87,25 | 4 x A$-bedrag (Afterpay heeft een bovengrens per order) | |

Voor de mails: per markt alleen tonen waar de methode echt bestaat (filter op verzendland of presentment currency). Dit is een nieuwe claim, dus eerst akkoord van Floris en vastleggen in DECISIONS.md. Niets hiervan is in `klaviyo/templates` gezet.

---

## 4. Breakeven per aanbieder

Formule: extra kosten = verschoven omzet x feeverschil. Extra brutowinst = extra omzet x (marge minus BNPL-fee). Breakeven-lift = aandeel dat naar BNPL verschuift x feeverschil / (marge minus BNPL-fee).

Marge 83% (Intelligems: COGS 16,9% van netto-omzet). Ter controle ook 60% (aanname voor marge na verzending, fulfilment en retouren).

| Markt | Aanbieder | Feeverschil t.o.v. kaart | Verschuiving naar BNPL (aanname) | Breakeven-lift bij 83% | Bij 60% | Netto per maand bij middenscenario (83%) |
|---|---|---|---|---|---|---|
| US | Shop Pay Installments, meer zichtbaar | 3,5 pp (5,9 tegen 2,4) | +2,5 tot +4% van de omzet | 0,11 tot 0,18% | 0,16 tot 0,26% | +$6.700 |
| US | Affirm-app houden | 3,6 pp | 0,8% | 0,04% | 0,05% | +$1.300 |
| AU | Afterpay cross-border | 2,1 pp (7,0 tegen 4,9) | 8 tot 15% | 0,22 tot 0,41% | 0,32 tot 0,59% | +$4.500 |
| AU | PayPal Pay in 4-messaging | 0 pp | 2 tot 5% | 0% | 0% | +$1.100 |
| CA | Afterpay cross-border | 2,1 pp | 5 tot 10% | 0,14 tot 0,28% | 0,20 tot 0,40% | +$1.500 |
| UK | Klarna-messaging | 1,6 pp (aanname 6,5 tegen 4,9) | 2 tot 6% | 0,04 tot 0,13% | 0,06 tot 0,18% | +$300 |
| UK | Clearpay cross-border | 2,1 pp | 3 tot 8% | 0,08 tot 0,22% | 0,12 tot 0,32% | +$500 |
| SG | Atome (indien mogelijk) | 1,1 pp (aanname 6,0) | 3 tot 8% | 0,04 tot 0,11% | 0,06 tot 0,16% | +$500 |

Ter vergelijking: Shop Pay Installments kost nu ongeveer $1.400 per maand meer dan kaart (4,9% van $791.000 x 3,5 pp) en verdient dat terug bij 0,2 procent extra US-omzet.

**Slechtste geval.** Als Afterpay in AU alleen bestaande kaartkopers verschuift (geen lift) en 15% van de omzet pakt, kost het $360 per maand. Dat is het maximale risico van een test van acht weken: ongeveer $700.

---

## 5. Testopzet

Eerlijk vooraf: per markt is het verkeer klein. AU heeft 23.500 bezoekers en 568 orders per maand; een 50/50-test van vier weken ziet pas een verschil van ongeveer 23 procent in conversie. Een US-PDP-test ziet ongeveer 10 procent. De verwachte effecten zijn kleiner, dus de opzet leunt op meerdere metingen.

### Stap 1 · Nu, zonder kosten (week 0 tot 2)

- Google Pay-knop op Android Chrome controleren (checkout en express-knop).
- Klarna-messaging op de UK-PDP laten renderen.
- PayPal Pay Later-messaging voor AU aanzetten als dat in de PayPal-app kan.
- In Klaviyo een eigen event of property voor betaalmethode regelen (bijvoorbeeld via een Shopify Flow-tag op orders met `shop_pay_installments`), zodat mails en rapporten termijnkopers zien.

### Stap 2 · US: 50/50 PDP- en cart-boodschap via Intelligems (6 weken)

- Controle: huidige situatie (kleine grijze regel onder de prijs, Affirm in de cart drawer).
- Variant: termijnregel direct onder de prijs in de merkstijl ("or 4 interest-free payments of $33.50"), dezelfde regel in de cart drawer, bij sets een maandbedrag.
- Primaire metriek: omzet per bezoeker. Secundair: aandeel Shop Pay Installments, checkout-voltooiing op mobiel, conversie van carts vanaf $200, AOV.
- Splitsen op apparaat in de analyse (Android Chrome, iOS Safari, webview).

### Stap 3 · AU eerst, CA vier weken later (getrapte uitrol, 8 weken)

- Week 0: Afterpay live in AU (checkout plus PDP- en cart-regel). CA blijft gelijk en dient als controle.
- Week 4: Afterpay live in CA. AU loopt door.
- Meting: verschil-in-verschil op conversie per bezoeker, checkout-voltooiing en AOV, met US en UK als extra controle voor seizoen (oktober-actie, BFCM).
- Stopregel: als na vier weken het Afterpay-aandeel boven 10 procent ligt en de AU-checkout-voltooiing niet stijgt, alleen kosten, dan uitzetten.
- Binnen AU kan Intelligems daarnaast 50/50 de PDP-regel testen (met tegen zonder Afterpay-regel), zodat het effect van de boodschap los van de methode te zien is.

### Stap 4 · Mails (na stap 2 en 3)

- Checkout- en cart-mails: termijnregel onder de cart, per markt alleen waar de methode bestaat. A/B op unieke kliks en geplaatste orders, volgens PLAYBOOK 6.

### BFCM

Termijnen worden in november het meest gebruikt. Als AU vóór half november live moet, dan stap 3 starten zodra Floris akkoord geeft; de getrapte opzet blijft dan bruikbaar met BFCM in beide arms.

---

## Open vragen voor Floris

1. Land en entiteit van het Shopify Payments-account (US neem ik aan) en de huidige Plus-tarieven voor kaart, internationaal en valutaconversie.
2. Tarief van Shop Pay Installments op Plus: standaard 5,9% + $0,30 of onderhandeld?
3. Mag er een Afterpay-account (US, met Cross Border Trade voor AU en CA) worden aangevraagd? Wie tekent?
4. Waarom is Klarna van $35.000 in januari naar $1.000 in september gezakt: minder Europees verkeer of een instelling?
5. Waarom staat de Affirm-app naast Shop Pay Installments, en is er een contract met een minimum?
6. Mag de termijnregel in mails als nieuwe claim worden opgenomen (DECISIONS.md), inclusief de juridische voetnoot?
7. SG: is er interesse in Atome, of eerst de SG-checkout (verzending, valuta) laten doorlichten?

---

## Bronnen

Eigen data: Shopify Admin GraphQL en ShopifyQL (payments, sessions), Intelligems sitewide snapshot, Klaviyo Events API, live PDP-HTML; zie `01-inventaris.md`.

- Berg, Burg, Keil, Puri, "The Economics of Buy Now, Pay Later: A Merchant's Perspective", Journal of Financial Economics 171 (2025): https://www.isb.edu/faculty-and-research/research-directory/the-economics-of-buy-now-pay-later-a-merchant-s-perspective/ en NBER w33152: https://nber.org/system/files/working_papers/w33152/w33152.pdf
- Stripe, "Testing the impact of buy now, pay later across 150,000+ checkout sessions": https://stripe.com/blog/testing-the-impact-of-buy-now-pay-later
- Baymard, payment method selection en checkout-abandonment: https://baymard.com/blog/payment-method-selection
- Worldpay Global Payments Report 2025: https://www.worldpay.com/en-GB/global-payments-report-2025
- Overzicht academisch onderzoek BNPL (2026): https://arxiv.org/pdf/2609.09323
- Shop Pay Installments, landen en voorwaarden: https://help.shopify.com/manual/payments/shop-pay-installments/faq en https://www.affirm.com/terms/merchant-agreement/shop-pay
- Klarna via Shopify Payments (landen): https://help.shopify.com/en/manual/payments/shopify-payments/local-payment-methods/klarna en https://docs.klarna.com/platform/shopify/get-started/prerequisites/
- Afterpay Cross Border Trade: https://www.afterpay.com/en-AU/business/cross-border-trade en https://developers.cash.app/afterpay/guides/welcome/getting-started/cross-border-trade
- Afterpay merchant fees: https://www.afterpay.com/en-AU/business/afterpay-merchant-fees en https://wise.com/us/blog/afterpay-for-business
- Klarna-fees UK op Shopify: https://www.fena.co/blog/how-to-reduce-klarna-fees-on-shopify-uk-by-adding-pay-by-bank
- PayPal Pay in 4 Australië: https://www.paypal.com/au/smarthelp/article/faq4333
- FCA-regulering BNPL vanaf 15 juli 2026: https://www.fstech.co.uk/fst/BNPL_Lenders_Face_FCA_Oversight_From_July_2026.php

Let op: help.shopify.com, stripe.com en developers.cash.app waren vanuit deze sessie niet bereikbaar (netwerkfilter); cijfers uit die bronnen komen uit zoekresultaat-samenvattingen en moeten voor een contract op de pagina zelf worden nagelezen.
