# 01 · Betaalinventaris per markt

Datum: 7 oktober 2026. Alleen gelezen in Shopify, Klaviyo en Intelligems. Niets gewijzigd. Alleen aggregaten, geen persoonsgegevens opgeslagen (profiel-ID's alleen gehasht in een tijdelijke scratchpad buiten de repo).

Bijbehorende data: `research/payments/per-markt.csv` (betaalmethode, apparaat en ATC-cohort per markt).

## Bronnen en vensters

| Bron | Wat | Venster |
|---|---|---|
| Shopify Admin GraphQL | `shop.paymentSettings.supportedDigitalWallets`, plan, winkeladres, markets met valuta | 7 okt |
| ShopifyQL `FROM payments` (Shopify-analytics) | Omzet en orders per `payment_method`, `digital_wallet`, `billing_country`; transacties `sale` + `capture` | 30 dagen (7 sep t/m 6 okt), 90 dagen, per maand sinds januari |
| ShopifyQL `FROM sessions` (via Intelligems) | Sessies, ATC, checkout, voltooid per land, apparaat, OS en browser | 7 sep t/m 6 okt |
| Intelligems sitewide snapshot | Conversie per bezoeker, AOV, COGS per land | 7 sep t/m 6 okt |
| Klaviyo Events API (revision 2025-10-15, GET) | Placed Order (18.487 events, 17.674 webshop-orders), Added to Cart (22.030 events, 4.949 profielen in het cohort) | Orders 8 jul t/m 6 okt; ATC 7 sep t/m 6 okt |
| Live PDP (Hammered Pan, curl met US-, AU-, CA-, GB- en SG-localisatie) | Welke betaalboodschap de theme rendert | 7 okt |

**Belangrijke methodenoot.** Klaviyo's `$extra.payment_gateway_names` toont Shop Pay Installments en Klarna als `shopify_payments`. Daarom leek BNPL in de eerdere diagnose (research/deep/04) afwezig. Shopify's eigen payments-dataset splitst wel op betaalmethode. Voor aandeel per methode gebruik ik daarom Shopify, voor apparaat en ATC-cohorten Klaviyo.

---

## 1. Wat staat technisch aan

| Instelling | Waarde |
|---|---|
| Plan | Shopify Plus |
| Winkeladres | US; winkelvaluta USD; Shopify Payments-account (land niet leesbaar met deze scope, maar Shop Pay Installments werkt alleen bij een US-, CA- of UK-entiteit en draait hier voor US-kopers, dus vrijwel zeker een US-account) |
| Wallets (`supportedDigitalWallets`) | Shop Pay, Apple Pay, Google Pay |
| Markets met eigen valuta | Australia (AUD), Canada (CAD), United Kingdom (GBP), New Zealand (NZD), EURO en Germany en Netherlands (EUR); Singapore, Middle East en RoW op USD met lokale valuta aan |
| Shop Pay Installments | **Actief sinds maart 2026**, alleen US-kopers. Plannen: $35 tot $50 in 2 termijnen, $50 tot $1.000 in 3 of 4 renteloze termijnen of 3, 6, 12 maanden met rente, boven $1.000 alleen maandtermijnen met rente. Prequalificatie staat uit. |
| Affirm | Aparte Affirm-app als eigen gateway, plus Affirm-messaging in de cart drawer (alleen US-sleutel ingevuld, CA-sleutel leeg) |
| Klarna | Via Shopify Payments, wordt alleen getoond aan kopers in Europa en UK (Shopify ondersteunt Klarna nog niet voor US-kopers). Klarna on-site-messaging-script staat in de theme, maar er staan geen Klarna-placements op de PDP. |
| Overige methoden via Shopify Payments | Amazon Pay, Bancontact, MobilePay (iDEAL en BLIK sinds april niet meer gebruikt) |
| PayPal | Actief in alle markten. PayPal toont zelf Pay in 4 aan kopers in onder meer US, AU en UK, zonder extra kosten voor de winkel. Niet te meten in de data. |
| Afterpay, Clearpay, Zip, Atome, Sezzle | Niet aanwezig |
| PDP-boodschap | `shopify-payment-terms` staat direct onder de prijs: "4 payments of $33.50" bij de Pan Pro van $134. Wordt alleen voor US gerenderd; voor AU, CA, GB en SG staat er niets. |

## 2. Tabel per markt: methoden, aandeel, AOV en conversie

Venster 7 sep t/m 6 okt 2026, Shopify payments, factuurland. Bedragen in USD (shop-valuta).

### United States (3.224 orders, $791.102, AOV $245)

| Methode | Actief | Orders | Aandeel orders | Aandeel omzet | AOV |
|---|---|---|---|---|---|
| Shop Pay (kaart) | ja | 2.046 | 63,5% | 64,3% | $249 |
| Apple Pay | ja | 431 | 13,4% | 12,5% | $230 |
| PayPal | ja | 243 | 7,5% | 7,7% | $250 |
| Kaart zonder wallet | ja | 230 | 7,1% | 8,3% | $286 |
| **Shop Pay Installments** | ja | 169 | **5,2%** | **4,9%** | **$231** |
| Affirm (eigen app) | ja | 19 | 0,6% | 0,8% | $333 |
| Amazon Pay | ja | 20 | 0,6% | 0,5% | $212 |
| Google Pay | ja | 19 | 0,6% | 0,5% | $211 |
| Overig (Shop Cash e.d.) | ja | 47 | 1,5% | 0,4% | $62 |
| Klarna, Afterpay | nee | | | | |

### Australia (599 orders, $114.327, AOV $191)

| Methode | Actief | Orders | Aandeel orders | Aandeel omzet | AOV |
|---|---|---|---|---|---|
| Shop Pay (kaart) | ja | 342 | 57,1% | 58,3% | $195 |
| Apple Pay | ja | 118 | 19,7% | 20,4% | $198 |
| **PayPal** | ja | 107 | **17,9%** | 16,6% | $178 |
| Kaart zonder wallet | ja | 30 | 5,0% | 4,5% | $173 |
| Google Pay | ja | 2 | 0,3% | 0,2% | $96 |
| Shop Pay Installments, Afterpay, Klarna | nee | | | | |

### Canada (273 orders, $51.303, AOV $188)

| Methode | Actief | Orders | Aandeel orders | Aandeel omzet | AOV |
|---|---|---|---|---|---|
| Shop Pay (kaart) | ja | 175 | 64,1% | 66,7% | $195 |
| Apple Pay | ja | 42 | 15,4% | 15,1% | $185 |
| Kaart zonder wallet | ja | 25 | 9,2% | 8,3% | $170 |
| PayPal | ja | 23 | 8,4% | 8,2% | $183 |
| Overig, Google Pay | ja | 8 | 2,9% | 1,7% | |
| Shop Pay Installments, Afterpay, Klarna | nee | | | | |

### Singapore (207 orders, $47.890, AOV $231)

| Methode | Actief | Orders | Aandeel orders | Aandeel omzet | AOV |
|---|---|---|---|---|---|
| Shop Pay (kaart) | ja | 106 | 51,2% | 52,5% | $237 |
| Apple Pay | ja | 63 | 30,4% | 32,3% | $245 |
| Kaart zonder wallet | ja | 26 | 12,6% | 9,3% | $171 |
| PayPal | ja | 6 | 2,9% | 3,5% | $282 |
| Google Pay | ja | 6 | 2,9% | 2,4% | $188 |
| Atome, Afterpay, Klarna | nee | | | | |

### United Kingdom (180 orders, $36.665, AOV $204)

| Methode | Actief | Orders | Aandeel orders | Aandeel omzet | AOV |
|---|---|---|---|---|---|
| Shop Pay (kaart) | ja | 80 | 44,4% | 43,5% | $199 |
| Apple Pay | ja | 62 | 34,4% | 33,9% | $201 |
| Kaart zonder wallet | ja | 16 | 8,9% | 11,2% | $257 |
| PayPal | ja | 12 | 6,7% | 6,2% | $190 |
| Google Pay | ja | 5 | 2,8% | 3,3% | $243 |
| **Klarna (Shopify Payments)** | ja | 4 | 2,2% | 1,7% | $158 |
| Shop Pay Installments, Clearpay | nee | | | | |

### Conversie per apparaat en markt (Shopify sessions, 7 sep t/m 6 okt)

| Markt | Apparaat | Sessies | Conversie per sessie | Checkout voltooid (van gestart) |
|---|---|---|---|---|
| US | mobiel | 143.747 | 1,61% | 52,9% |
| US | desktop | 31.893 | 1,71% | 63,8% |
| AU | mobiel | 24.308 | 1,90% | 45,6% |
| AU | desktop | 3.781 | 2,30% | 44,4% |
| CA | mobiel | 15.393 | 1,27% | 37,7% |
| CA | desktop | 2.907 | 1,51% | 33,3% |
| SG | mobiel | 16.393 | 1,02% | 32,4% |
| SG | desktop | 3.708 | 0,62% | 35,4% |
| UK | mobiel | 4.225 | 1,54% | 53,3% |
| UK | desktop | 716 | 3,49% | 71,4% |

Intelligems (per bezoeker, zelfde venster): US 1,98%, AU 2,41%, CA 1,63%, UK 1,61%, SG 1,02%, totaal 1,64%. COGS is 16,9% van netto-omzet, dus productmarge 83%.

**Lezing.** AU converteert per bezoeker het best, maar maakt maar 45% van de gestarte checkouts af tegen 53% in de US. CA (38%) en SG (32%) lekken nog meer in de checkout. Dat is de stap waar een ontbrekende betaalmethode zichtbaar wordt.

## 3. Ordergrootte per markt (Klaviyo Placed Order, 90 dagen, webshop)

| Markt | Orders | Aandeel orders | Aandeel omzet | AOV | Mediaan | Orders vanaf $200 | Orders vanaf $350 |
|---|---|---|---|---|---|---|---|
| US | 11.699 | 66,2% | 67,6% | $221 | $148 | 27,6% | 14,2% |
| AU | 1.703 | 9,6% | 9,0% | $201 | $157 | 23,0% | 9,9% |
| SG | 861 | 4,9% | 4,8% | $214 | $171 | 29,6% | 12,4% |
| CA | 806 | 4,6% | 4,1% | $194 | $154 | 23,7% | 10,7% |
| UK | 552 | 3,1% | 3,2% | $219 | $184 | 36,8% | 15,2% |
| Totaal | 17.674 | | | $216 | $149 | 27,6% | 13,4% |

In de laatste 30 dagen is AU 12,4% van de orders (de bekende 12 procent); over 90 dagen 9,6%.

## 4. Trend per maand (Shopify payments, bruto, USD)

| Maand | Kaart (SP) | PayPal | Shop Pay Installments | Affirm | Klarna (SP) |
|---|---|---|---|---|---|
| jan | 1.637.976 | 307.596 | 0 | 0 | 35.755 |
| mrt | 1.380.328 | 121.712 | 18.602 | 0 | 23.239 |
| mei | 1.564.320 | 156.374 | 53.424 | 12.640 | 7.560 |
| jul | 1.182.575 | 125.942 | 64.875 | 13.499 | 5.353 |
| aug | 1.382.864 | 135.869 | 69.820 | 15.881 | 3.689 |
| sep | 983.771 | 99.425 | 40.424 | 6.046 | 1.158 |

Shop Pay Installments is sinds de start in maart gegroeid naar 4 tot 5 procent van de omzet. Klarna is van $35.755 in januari teruggevallen naar $1.158 in september; dat loopt gelijk met minder Europees verkeer (DE en IT sessies stijgen, orders dalen), maar kan ook een instelling zijn. Open vraag aan Floris.

## 5. Bijzonderheden die ertoe doen

1. **Google Pay wordt bijna niet gebruikt.** US: 19 Google Pay-orders tegen 431 Apple Pay in 30 dagen, terwijl Android 18 procent van de orders levert. Apple Pay dekt ongeveer een vijfde van de iOS-orders, Google Pay een paar procent van de Android-orders. Te controleren of de Google Pay-knop in de checkout en als express-knop op Android Chrome verschijnt.
2. **AU leunt op PayPal.** 17,9% van de AU-orders tegen 7,5% in de US. In AU biedt PayPal zelf Pay in 4 aan; het hoge aandeel past bij vraag naar termijnen.
3. **Shop Pay Installments wordt niet vooral voor grote orders gebruikt.** AOV $231 tegen $249 voor Shop Pay met kaart. Termijnen helpen hier vooral kopers met een krapper budget over de drempel, wat aansluit bij het onderzoek van Berg e.a. (zie 02).
4. **Affirm dubbel.** De Affirm-app ($6.322 in 30 dagen, AOV $333) draait naast Shop Pay Installments, dat zelf door Affirm wordt gefinancierd. Twee checkout-opties van dezelfde partij.
5. **PDP-boodschap alleen in de US.** Buiten de US rendert de PDP geen enkele termijnregel, ook niet in UK waar Klarna wel in de checkout staat.
