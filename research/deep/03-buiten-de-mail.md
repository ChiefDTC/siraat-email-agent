# 03 · Buiten de mail: wat er na de klik gebeurt

Datum: 7 oktober 2026. Alleen gelezen: Shopify Admin (Plus, betaalwallets, valuta), Klaviyo-events, Intelligems, Gorgias. De site zelf (siraatskitchen.com) is vanuit deze omgeving geblokkeerd, dus PDP-observaties komen uit `content/products/` en `content/facts/` (Shopify-data van 7 okt). Elke fix heeft een eigenaar buiten e-mail; niets is aangepast.

---

## 0. De trechter in één tabel (30 dagen, Intelligems)

| Stap | Waarde | Lezing |
|---|---|---|
| Sessies | 339.651 (82 procent mobiel) | Verkeer daalt (-25 procent tegenover vorige periode) |
| Bounce | 71,5 procent | Hoog, typisch voor Meta-verkeer in de webview |
| Bekeek een PDP | 73 procent | Bezoekers landen vooral direct op een PDP |
| Add to cart | 5,25 procent van sessies | De PDP is de grootste afvalbak: 95 procent koopt niet |
| Checkout gestart | 2,42 procent | 74 procent van de carts komt niet in de checkout |
| Order | 1,36 procent per sessie, 1,64 per bezoeker | 44 procent van de checkouts wordt verlaten |

Per 100 bezoekers: 5 leggen iets in de cart, 2,4 starten de checkout, 1,4 kopen. De grootste absolute lekken: **PDP naar cart** en **cart naar checkout**. E-mail kan alleen de mensen terughalen die een adres achterlieten; de site moet de rest doen.

---

## 1. De tien fixes buiten e-mail, gerangschikt op verwachte impact

Impact = geschatte extra netto-omzet per maand bij een omzet van circa $1,1 miljoen per maand. Zekerheid: H (sterk bewijs en eigen data), M, L.

| # | Fix | Waarom (bewijs) | Verwachte impact | Zekerheid | Eigenaar |
|---|---|---|---|---|---|
| 1 | **Beleid en belofte gelijktrekken, plus een "leer-garantie"** | 100 van 154 lage Trustpilot-reviews over retour of de oude 100-day trial, 47 noemen het "scam". Beleid: alleen ongebruikt, retour op eigen kosten, "sticking is not a defect". Site-bar zei nog "100-DAY TRIAL". Meta-analyse: soepeler beleid verhoogt aankopen meer dan retouren (Janakiraman e.a. 2016). | +3 tot 8 procent conversie op koud verkeer via betere reputatie en risico-omkering; retouren kunnen licht stijgen. $30.000 tot $80.000 per maand. | M | Floris (beleid), site, Gorgias |
| 2 | **Termijnbetaling zichtbaar maken** (Shop Pay Installments in de VS; Afterpay/Klarna in AU, NZ, UK, CA) | Shop Pay, Apple Pay en Google Pay staan aan, maar BNPL is vrijwel afwezig (Affirm 19 orders van 5.143). 13 procent van de orders is boven $350. AU is 12 procent van de orders, waar Afterpay de norm is. Benchmarks: conversie +3 tot 6 procent op Shopify (Tenten), AOV +12 tot 18 procent. | Conservatief +2 procent conversie en +5 procent AOV op orders boven $200: $15.000 tot $40.000 per maand | M tot H | Floris, Shopify-instellingen |
| 3 | **In-app browser-wrijving verminderen** | 40 procent van de orders komt uit FB/IG-webview. Daar werken Shop Pay-autofill en vaak Apple Pay niet; casus: 0,83 procent tegen 2,84 procent conversie na doorsturen naar Safari. Samsung Internet-ATC's converteren 8 procent, iOS 32 procent. | Als de webview-checkout 10 procent beter converteert: circa $20.000 per maand | M | Site (Replo/theme), ads-team (landingspagina's) |
| 4 | **PDP beantwoordt de drie twijfels boven de vouw**: "Will it stick?" (20-seconden watertest-video), "Does it work on my stove?" (inductie, gas, glas), "Which size?" (maathulp met standaard 11") | Pre-sale vragen: materiaal 160, deksels 82, herkomst 69, maat 54, schoonmaken 52, plakken 51 (526 tickets in 90 dagen). PDP naar cart is het grootste lek (5,25 procent). Spiegel: reviews verhogen conversie op dure producten circa 380 procent; Baymard: specificaties en antwoorden op de PDP. | +5 procent ATC-ratio: circa $40.000 tot $55.000 per maand | M | Site, content |
| 5 | **Okendo-reviews gericht tonen** op de PDP en in mails: filter op inductie, eieren, maat, "after 3 months"; kritische reviews met antwoord | 2.226 Okendo-reviews op de pannen, niet gebruikt in de repo. Trustpilot-reviews zijn deels met gift card uitgelokt en worden "fake" genoemd. Koopkans piekt bij 4,2 tot 4,5 sterren. | Indirect, versterkt fix 4; plus bewijs voor mails | H | Site, Okendo, e-mail |
| 6 | **Levertijd als datum** op PDP, cart en checkout, per land | Beleid: 6 tot 10 kalenderdagen, ook voor de VS. Baymard: shoppers prefereren een leverdatum boven "standard shipping"; 41 procent van sites toont geen datum. Gift-season komt eraan. | +1 tot 2 procent checkout-conversie; Q4 meer | M | Shopify (delivery customization, Plus), site |
| 7 | **Prijs- en listingarchitectuur opschonen**: één 6-delige set (nu $349 verborgen, $399 actief, $449 "SB"), Pan Pro-kopielistings weg, badges die kloppen met compare-at, "was"-prijzen verdedigbaar (FTC 233.1, EU Omnibus voor EU-markt, ACCC voor AU) | 31 inconsistenties in de productbibliotheek; permanent 69 procent korting op de Pan Pro; checkouts van $100 tot $199 worden in 43 procent van de gevallen verlaten, $200 tot $349 in 24 procent. | Moeilijk te kwantificeren; vooral risico- en vertrouwensreductie | M | Floris, merchandising |
| 8 | **Discount-links en cart-herstel waterdicht** | Mails gebruiken `/discount/CODE?redirect=` en `responsive_checkout_url`. Op een ander apparaat bestaat de cart niet; alleen de checkout-URL herstelt. Een redirect naar een lege cart is de duurste fout in een flow. | Bescherming van de $36.000 per maand abandonment-omzet | H | E-mail (QA), site |
| 9 | **Pre-sale service als verkoopkanaal**: chat of een duidelijke "Ask Benjamin's team" op PDP en in mails; pre-sale tickets automatisch in een Klaviyo-flow | Gorgias heeft vrijwel geen chat (27 chattickets in 90 dagen) maar antwoordt per e-mail mediaan binnen circa 7 minuten. Van 431 pre-sale vragenstellers kocht 13 procent binnen 30 dagen, circa acht keer de siteconversie per bezoeker. | Klein volume, hoge kwaliteit: $5.000 tot $15.000 per maand | M | Gorgias, site, e-mail |
| 10 | **Post-purchase onboarding om retouren te voorkomen**: watertest-video vóór levering, eerste-ei-mail na levering, "reply if it sticks" met snelle coaching vóór de retourvraag | Plakken in 222 van 806 retourverzoeken (28 procent); retouren stegen van 3,4 naar 5,5 procent van de bruto-omzet (april tot september). | 1 procentpunt minder retour: circa $13.000 per maand, plus betere reviews | M tot H | E-mail, Gorgias |

Samen: realistisch $100.000 tot $250.000 extra netto per maand als de top vijf goed gebeurt. Ter vergelijking: het hele v3-flowsysteem mikt op +$40.000 tot +$80.000 per maand. **Buiten de mail ligt meer dan in de mail.**

---

## 2. Per onderwerp, concreet

### 2.1 Landingspagina's vanuit mail

- Elke verkoopmail stuurt nu naar een PDP of de checkout. Voor checkout en cart is dat goed (de cart is het doel). Voor welcome, browse en campagnes werkt een **flow-specifieke landingspagina** beter: dezelfde belofte als de mail, het aanbod al toegepast, één product per bezwaar.
- Minimaal drie pagina's: (a) "Start here" voor welcome (één pan, de watertest, garantie, keuzehulp maat), (b) "Is titanium right for you?" voor twijfelaars (eerlijk: wat wel, wat niet, vergelijking met rvs, gietijzer, gecoat), (c) set-pagina met "build your kitchen" en termijnen.
- Bestaande bouwstenen: Replo (project 4ebf66e0-...), quiz.siraatskitchen.com, bestpansreviewed.com (8,4 procent van de orders, AOV $291: dit format werkt voor vergelijkers).
- Meten met UTM per mail (research/testing/04-utm.md).

### 2.2 Shopify checkout

- Plus-winkel met Shop Pay, Apple Pay, Google Pay, PayPal (8,6 procent van de orders), lokale valuta ingeschakeld (AUD, SGD, GBP en meer tonen in de checkout).
- **Ontbreekt:** zichtbare termijnbetaling. Shop Pay Installments bestaat alleen in de VS (en CA in beperkte vorm); voor AU is Afterpay de verwachting. Opdracht: inventariseren wat technisch aan staat en wat niet, per markt.
- **Shipping Protection** staat in 13,5 procent van de orders. Check of het standaard aangevinkt is; een vooraf aangevinkte betaalde optie is wrijving en een vertrouwensrisico.
- **Vertrouwen in de checkout:** checkout-blokken (Plus checkout extensibility) met garantie in één regel, retourbeleid exact zoals het is, en een review. Niet meer dan drie elementen.
- **Codes:** 82 procent van de orders zonder code. Openbare codes (BFEXTRA10, NYEXTRA10 enz.) staan nog open (zie 04-offer-strategy). Een veld "Discount code" in de checkout zet mensen aan het zoeken op couponsites; overweeg het veld minder prominent te maken als codes via links werken.

### 2.3 Verzendkosten en levertijd

- Gratis verzending wereldwijd en DDP (geen invoerrechten) zijn sterke punten die nu als losse icoontjes staan.
- 6 tot 10 kalenderdagen in de VS is traag naast Amazon. Niet verstoppen (dat geeft "where is my order"-tickets: 1.182 orderstatus-tickets in 90 dagen), wel als datum en met tracking-mails die de wachttijd vullen met de watertest.
- Kerst: cutoff per land berekenen en vanaf half november op PDP, cart en in mails tonen.

### 2.4 De discount-link en cart-herstel op een ander apparaat

- `https://siraatskitchen.com/discount/HI10?redirect=/products/...` zet de code in een cookie en stuurt door. Werkt op elk apparaat, maar de cart is leeg als de klant op een ander apparaat zit. Voor cart- en checkoutmails altijd `responsive_checkout_url` (plus `&discount=` waar nodig), die herstelt de checkout ook op een ander apparaat.
- Browse-mails: link naar de PDP met de juiste variant (`?variant=`), anders kiest de klant opnieuw een maat (keuzestress).
- QA-opdracht: elke link in elke flowmail op iPhone in Gmail, op Android in Gmail en op desktop testen met een lege browser.

### 2.5 PDP-bezwaren (wat moet erop)

Volgorde op basis van pre-sale vragen en retourredenen:
1. "Will food stick?" Eerlijk: geen coating, dus 2 minuten ritueel. Video van 20 seconden. Review van iemand die het leerde (Aggie M., Marilyn B.).
2. "Will it work on my stove?" Inductie, gas, elektrisch, glas/keramiek. Review Mrs J. (inductie).
3. "Which size?" Standard 11" als aanbevolen start; maattabel met cm en inch; wat past erin (2 eieren, 2 steaks).
4. "Which lid?" 82 pre-sale vragen over deksels: deksel-compatibiliteit per maat op de PDP, en "add the matching lid" als upsell (deksel zit al in 14 procent van de orders).
5. "What is it made of / is it safe?" Drie lagen, Light Labs met echt rapport, "not guaranteed nickel-free" eerlijk vermelden voor wie dat zoekt.
6. "Where is it made?" Ontworpen in Nederland, gemaakt bij gecertificeerde partners in Azië, verzonden uit de VS: zeggen voordat het gevraagd wordt.
7. Garantie en retour in gewone taal, gelijk aan het beleid.

Verboden claims die nog live staan (productbibliotheek inconsistentie 11) eerst weghalen: "scientifically proven to retain more nutrients", "scratch-proof", "lifetime", "100-day trial", "free express shipping".

### 2.6 Reviews (Okendo)

- Okendo-reviews ophalen en per bezwaar taggen (plakken, inductie, maat, schoonmaken, deksel, set).
- Review-verzoek na de eerste-ei-ervaring (dag 14 na levering, PLAYBOOK 5) met foto-incentive die niet afhankelijk is van sterren.
- Trustpilot en Okendo niet tegelijk vragen; één verzoek per order.
- Kritische reviews beantwoorden met de oplossing (watertest, garantie), zichtbaar.

### 2.7 Pop-up (Alia) en lijstkwaliteit

- Pop-up blijft de giveaway (besluit). Toevoegen: één segmentatievraag (kookplaat of doel). Testen of die vraag de opt-in-ratio meer dan 10 procent verlaagt; zo niet, houden.
- Timing en frequentie: niet direct bij binnenkomst op de PDP van Meta-verkeer (die bezoeker wil de pan zien); pas na scroll of exit intent. Alia-instelling, A/B.
- Bron per abonnee als profiel-eigenschap vastleggen, zodat conversie en klachten per bron meetbaar zijn.

### 2.8 SMS

- SMS levert nu circa $5.000 per maand (Intelligems), op 1.257 bezoekers. Benchmarks: abandoned-checkout SMS heeft de hoogste omzet per bericht ($3,46 tot $10,05) en conversie per verzending rond 2,4 procent.
- Siraat-logica: SMS alleen voor (1) checkout abandonment na 1 uur, één bericht; (2) verzendupdates met de watertest-link (vermindert "where is my order" en plakken); (3) BFCM en kerst-cutoff. Geen dagelijkse SMS-campagnes.
- Opt-in in de checkout (consent) en na aankoop; niet in de giveaway.
- Compliance: TCPA (VS), quiet hours per tijdzone, dubbele opt-in waar vereist.

### 2.9 Retargeting afstemmen met Meta

- Paid social: 136.591 sessies en $472.000 netto-omzet in 30 dagen. Retargeting en e-mail jagen op dezelfde afhaker.
- Afstemmen: (a) Klaviyo-segmenten (checkout gestart, geen order, 0 tot 3 dagen) als custom audience **uitsluiten** van Meta-retargeting in de eerste 24 tot 48 uur, omdat e-mail daar goedkoper is; daarna juist opnemen met bewijs-creatives (watertest, reviews) in plaats van korting. (b) Kopers 30 dagen uitsluiten van acquisitie. (c) Dezelfde boodschap per fase: Meta toont het bewijs dat de mail van die dag ook toont.
- Meten met een geo- of audience-holdout (Meta lift test), niet met platform-ROAS.

### 2.10 Klantenservice (Gorgias) als conversiekanaal

- Gorgias antwoordt snel (mediaan eerste reactie circa 7 minuten; kan automatische eerste reacties bevatten, controleren). Gebruik dat als argument: "Questions? Reply to this email. A real person answers, usually within the hour."
- Pre-sale tickets (is_pre_sale) via de Klaviyo-metric "Opened Ticket" in een korte flow: antwoord gegeven, daarna 48 uur later één mail met het juiste product en bewijs.
- Macro's en AI-guidance gelijktrekken met het beleid (macro 247063 zegt dat de klant retour betaalt, guidance zegt gratis; verwarring wordt een 1-sterrenreview).
- Retourverzoeken met "stick" eerst een coaching-antwoord met video, met een concreet aanbod ("try these 3 steps for a week; if it still sticks, we'll make it right"). Dat is een beleidskeuze voor Floris.

### 2.11 Post-purchase onboarding en retouren

- Tijdlijn: order (bevestiging plus "what to expect: no coating, 2-minute ritual"), verzending (video watertest), levering (eerste-ei-mail), dag 3 ("how did the first egg go? reply"), dag 14 (review), dag 30 (cross-sell: deksel of tweede maat).
- Doel: retour-ratio van 5,5 naar 4 procent van bruto-omzet, en minder lage reviews over plakken.

---

## 3. Wat dit vraagt van e-mail

- Elke mail sluit aan op een pagina die hetzelfde bezwaar beantwoordt.
- Elke mail noemt het beleid precies.
- De checkoutmail toont termijnen zodra die bestaan ("or 4 interest-free payments of $33.50").
- E-mail levert data terug aan site en ads: welke bezwaren klikken (blok-UTM), welke reviews werken.

---

## Bronnen

- Intelligems sitewide snapshot (conversie, apparaat, kanaal), 7 sep t/m 6 okt 2026
- Shopify Admin GraphQL: plan Plus, `paymentSettings.supportedDigitalWallets` = Shop Pay, Apple Pay, Google Pay; presentment-valuta
- Klaviyo-events Placed Order, Checkout Started, Added to Cart (30 dagen, geaggregeerd, `04-siraat-diagnose.md`)
- Gorgias analytics: intents 90 dagen, kanaal en eerste reactietijd, pre-sale naar order
- content/facts/site-pages-and-policies.md (refund en shipping policy), content/products/README.md (31 inconsistenties), content/reviews/summary.md
- Baymard: https://baymard.com/lists/cart-abandonment-rate en https://baymard.com/blog/shipping-speed-vs-delivery-date
- Shop Pay conversie: https://www.shopify.com/enterprise/blog/shopify-checkout
- BNPL op Shopify: https://tenten.co/shopify/bnpl-shopify-comparison-2026/
- In-app browser: https://link.boo/fix/shopify-apple-pay-missing-instagram-browser
- Spiegel Research Center: https://spiegel.medill.northwestern.edu/star-ratings-and-review-content/
- Retourbeleid meta-analyse: https://news.utdallas.edu/?p=11491
- FTC 16 CFR 233: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-233 ; EU Omnibus: https://pagecrawl.io/blog/eu-omnibus-30-day-lowest-price-monitoring
- SMS-benchmarks: https://www.clickminded.com/sms-marketing-benchmarks/
