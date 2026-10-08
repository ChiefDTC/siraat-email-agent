# 01 · Kritische check vóór livegang v4

Datum: 8 oktober 2026. Rol: buitenstaander die zoekt waar het misgaat. Alleen gelezen: repo, Klaviyo (GET en rapporten), Shopify Admin (GraphQL, alleen query's). siraatskitchen.com was vanuit deze sessie geblokkeerd (egress), dus site-uitspraken komen uit `research/cro/` (7 okt) en Shopify-data. Niets gewijzigd, niets gecommit.

Methode: inversie ("wat laat deze livegang mislukken?"), zes echte klanttypes door de flowbomen van `exports/live/flows/OVERZICHT.md` gelopen, en elke aanname die te controleren was nagelopen tegen live data.

---

## Kort (voor de eigenaar)

Het systeem is goed doordacht, maar er zitten vier fouten in die pas zichtbaar worden als echte klanten erdoorheen gaan:

1. **De routering op producttitels klopt niet met de echte titels.** Schorten heten in Shopify "Siraat Signature Apron (Azure)", het script zoekt "Siraat Signature Apron - Azure". De $349-set waar acht mails naartoe linken heet "... | 6-Pcs (BDAY SALE)" en staat in geen enkele lijst. Gevolg: wie via onze eigen mail een set koopt, krijgt "Yours, or a gift?", geen eerste-ei-mail en op dag 20 "Now meet the pan (10% off)".
2. **De kortingslekken staan allemaal nog open** (gecontroleerd vandaag): 99%- en 100%-codes, BFEXTRA10 (7.626 keer gebruikt), NTWDHPKL5C (5.072), NYEXTRA10 (3.366), EXTRA30. HI10 is onbeperkt en per klant herbruikbaar, en v4 zet hem automatisch in de checkoutlink van C1 na 30 minuten. Daardoor meet T02 niet wat we denken, en geven we elke checkout-verlater 10% terwijl de beste checkoutmail ooit geen code had.
3. **Wie koopt, krijgt straks 15 tot 17 mails in 30 dagen**, omdat vier oude naflows ongemoeid blijven (FREE E-GUIDE op elke order, E-Book, 6 mails Pan Education op elke zending, ook voor schort- en plankkopers, 4 mails Mystery Gift met een 20%-aanbod). Smart sending staat uit, dus niets remt dit.
4. **Cart-mails sturen naar `/cart`.** Op een ander apparaat is die leeg. Dit is de flow met de hoogste opbrengst per ontvanger.

Daarnaast: W2 bevat nog drie zichtbare `[VRAAG FLORIS ...]`-plekken maar staat als "klaar" in de export; de checkout-templates in Klaviyo zijn ouder dan de repo; het oude pad van T01 blijft zes weken "100-DAY TRIAL" tonen aan de helft van de verlaters.

Advies: morgen niet alles tegelijk. Eerst de STOP-lijst, dan checkout en cart live, welcome pas als W2 af is, groep B pas als de oude naflows zijn opgeruimd.

---

## (a) STOP-lijst: vóór "turn on" opgelost

| # | Wat | Bewijs (vandaag gecontroleerd) | Fix | Wie |
|---|---|---|---|---|
| S1 | **Lekcodes uit** | Shopify, `status:active`: `98347983474334593` (99%), `SRJACEP6YNN1` + kopie (100%, geen limiet), `SJHNDFJNSAD934` (100%), `9MJ85MRZDE17` (100%, limiet 3, 1 gebruikt), BFEXTRA10 (7.626x), NTWDHPKL5C (5.072x), NYEXTRA10 (3.366x), EXTRA30 (30%, 140x), SK25, B2B25, MEMORIAL 20%, alle zonder einddatum | 100%/99% vandaag uit. 10%-lekcodes einddatum of uit. Collabs-codes laten staan | Floris (Shopify) |
| S2 | **Titellijsten in `scripts/build_flows.py` gelijk aan Shopify** | SCHORT_TITELS gebruikt " - Azure", Shopify heet "(Azure)". SET_TITELS mist "Titanium Hammered Pan Set With Lids \| 6-Pcs (BDAY SALE)" (de $349-listing uit 8 mails), "\| 6-Pcs SB", "\| 12-Pcs \| + FREE PIZZA STEEL" (twee varianten). KOOK_TITELS heeft "Pot Set With Lids 6-Pcs", Shopify heet "Titanium Hammered Pot Set With Lids \| 6-Pcs" | Lijsten uit `products(query:"status:active OR status:unlisted")` genereren, niet met de hand. Daarna dry-run en de categorietest uit sectie 1 met een echte BDAY-order | Claude |
| S3 | **W2 niet live met placeholders** | `welcome/w2.html` r. 41: drie zichtbare `[VRAAG FLORIS: ...]`. `exports/manifest.csv` zegt "klaar"; geen script blokkeert dit | Benjamins verhaal invullen of W2 tijdelijk uit de flow (wachttijd W3 aanpassen). Plus: QA-poort laten falen op `[VRAAG`, `TODO`, `[` + hoofdletters | Floris (tekst), Claude (QA-regel) |
| S4 | **Cart-links naar een echte cart** | k1, k1-acc, k2-new, k2-returning, k3: 5x `discount/<code>?redirect=/cart`. CRO 03 §8: op een tweede apparaat "Your cart is empty" | Cart-permalink uit het event (`/cart/<variant_id>:<qty>?discount=...`) of naar de PDP van `event.URL`. Minimaal in K3 (de codemail) | Claude |
| S5 | **Code + gifts samen in een echte checkout testen** | HI10: `combinesWith` product/order/shipping = false. Automatische korting "FREE GIFT" (BXGY, e-guide 100%) is actief. CRO 05 #4 nooit uitgevoerd. Elke mail belooft "10% plus $70 in gifts" | Test: `/discount/HI10?redirect=<PDP>` + pan in cart + checkout, en hetzelfde met een unieke code na S6. Bij conflict: pools op "combines with product discounts" | Floris (checkout), Claude (script en checklist) |
| S6 | **Klaviyo-objecten**: 8 coupon-pools, 4 segmenten, API-key met write-scopes | GET vandaag: geen v4-segment, geen coupon, alleen Y6yj2z (draft) | GO-LIVE stap 1 t/m 3. Bij de pools controleren of "vervalt na 48 uur" in uren kan; anders 2 dagen en de tekst "48 hours" aanpassen | Floris |
| S7 | **Checkout-templates opnieuw exporteren** | `exports/live/templates.csv`: c1/c2/c3 laatst geüpload 20:24; lokale bestanden 21:08 tot 21:11 (PFAS-hero, ugc, termijnregel). `build_flows.py` hergebruikt die ID's | `export_klaviyo.py --update` voor alle 10, dan pas flows | Claude |
| S8 | **T2SmtR-filter (GO-LIVE stap 8)** | Zonder deze stap krijgt ook de v4-arm na 30 dagen 10 FTL-mails | In de UI, vóór groep A | Floris |
| S9 | **A/B-acties starten en splits controleren** | API kan T04/T05a aanmaken, niet starten (LOG). Willekeur van `profile-sample` in geneste splits (T01 dan T02) is nergens bewezen | Na livegang "Start test" in W1 en B1. Na 24 uur: elke T02-split heeft verzendingen in beide armen | Floris (klik), Claude (controle 24 uur) |
| S10 | **Testprofielen door elke tak vóór live** | Zie sectie 2.4 | Matrix van 9 profielen, preview met echt event | Claude bouwt, Floris klikt |
| S11 | **Wie stuurt campagnes?** | Homestead maakte vannacht nog segmenten aan ("HS // Engaged 180 Days Email", 8 okt 02:24). Welkomstbescherming en campagneplafond werken alleen als de verzender ze uitsluit | Afspraak met Homestead vandaag, of campagnes tijdelijk via ons | Floris |

Vóór groep B (post-purchase, winback): B1 de oude naflows (zwakte 3) en B2 een beslissing over cadeaukopers (zwakte 11).

---

## (b) De 15 belangrijkste zwaktes, op impact

### 1. Categorie-routering faalt op echte producttitels (hoog, direct zichtbaar voor klanten)

**Bewijs.** Shopify vandaag: schorten "Siraat Signature Apron (Azure/Moss/Ember/Oak)"; script: "Siraat Signature Apron - Azure". De set waar C3-P, W4, P3-accessory, R2, R2-VIP, V1, A2 en N2 naartoe linken heet "Titanium Hammered Pan Set With Lids | 6-Pcs (BDAY SALE)" (UNLISTED, $349). Klaviyo-filters op `Items` gebruiken "contains-any" met exacte titels. De templates zelf zoeken op deelwoorden ("Pan", "Hammer"), de flowfilters op exacte titels: template en flow zijn het dus oneens over wie een pan heeft.

**Gevolg voor een setkoper via onze mail:** C2-ACC ("Yours, or a gift? Both work.") in plaats van C2; geen P2 en geen P2-safe (beide eisen KOOK-titels), dus geen eerste-ei-uitleg bij drie pannen terwijl plakken 25 tot 28% van de retouren is; P3 valt door de accessoire-router naar `p3-accessory` "Now meet the pan (10% off)"; geen UGC, geen anniversary; winback R1-acc "Ready for the pan?". Schortkopers missen `p3-apron`.

**Fix.** Titels genereren uit Shopify (incl. UNLISTED en ARCHIVED met recente orders), en een test die elke titel uit de laatste 90 dagen Placed Order door de router haalt. Overweeg één regel "categorie" als profiel-eigenschap via een Shopify-tag of Klaviyo-catalogus later.

### 2. Kortingsarchitectuur lekt marge en maakt T02 zinloos (hoog, geld)

**Bewijs.** HI10: actief, geen limiet, `appliesOncePerCustomer: false`, 1.724x gebruikt. C1, C2, C3-S, C3-P: `responsive_checkout_url ... &discount=HI10` (4x per mail), dus 10% staat al in de checkout 30 minuten na het verlaten. K1, B1, A1, R1 linken via `/discount/HI10`. De nocode-mails (T02-B) bevatten geen HI10, maar de klant heeft HI10 al drie keer gekregen en hij verloopt nooit. Historie (`research/history/01-beste-mails.md`): checkout 1 zonder code ("Don't leave these hanging") was de beste flowmail, $2,17 tot $7,83 per ontvanger; nu nog $9,08 op Y2TmNB-mail 1 (30 dagen).

**Gevolg.** T02 vergelijkt "unieke 10% met deadline" tegen "HI10 die je al hebt": geen van beide armen is "geen korting". De breakeven-regel (+20% kopers) is daarmee verkeerd gesteld, en zelfs als "geen code" wint blijft de 10% via HI10 betaald. Met de open lekcodes (S1) wordt het nog vager. Een lid van de welkomstlijst krijgt op dag 3 om 09:00 W3 (HI10) en K3 (eigen code, "ends Friday") in dezelfde minuut.

**Fix.** Beslissing D1. Minimaal: `&discount=HI10` uit de C1-links (code mag in de tekst blijven), HI10 op "once per customer", en T02 in checkout en cart pas meetellen als S1 klaar is.

### 3. Oude naflows blijven draaien naast v4 (hoog, frequentie en boodschap)

**Bewijs (Klaviyo, laatste 30 dagen).** FREE E-GUIDE (YyaMjx): trigger Placed Order, geen filter, 4.352 ontvangers. E-Book (TSUnLs): Placed Order met Mystery Gift (zit in bijna elke order), 3 mails. Pan Education (YcXbHx): trigger "Postflows - 2. Shipment In Transit" (Postflows, dezelfde bron die PLAYBOOK als trigger verbiedt), geen filter, 6 mails, 11.451 ontvangers. Mystery Gift Reveal (WvRupU): 4 mails, 9.703 ontvangers, waaronder "Alright, here's the offer" (sheets-abonnement 20%). Alle vier "blijven ongewijzigd live" in GO-LIVE.

**Gevolg.** Een pankoper krijgt in 30 dagen: Shopify-bevestiging, P1, E-Guide, E-Book (tot 3), Pan Education (6), Mystery Gift (4), P2, U1, P3, review: 15 tot 17 mails, met twee kortingen (P3 10% en sheets 20%) en dubbele uitleg (Pan Education en P2 over hetzelfde ei). Schort- en plankkopers krijgen 6 mails Pan Education over een pan die ze niet hebben.

**Fix.** Vóór groep B: FREE E-GUIDE en E-Book samenvoegen in P1 (downloadlink), Pan Education uit (P2 vervangt het) of filteren op kookgerei en ná P2, Mystery Gift na P3 laten starten (vertraging 25 dagen) en de 20% niet binnen het P3-codevenster.

### 4. Cart-mails sturen naar een lege winkelwagen (hoog, de best renderende flow)

**Bewijs.** Alle K-mails: `discount/HI10?redirect=/cart` (k3 met eigen code). CRO 03 §8 testte live: op een ander apparaat "Your cart is empty". Mails worden vaak op de telefoon gelezen, de cart staat op de laptop. Oude cart-flow SwkMyn: $1,95 per ontvanger, $17.786 in 30 dagen.

**Fix.** S4. Het Added to Cart-event heeft één product (geen hele cart): link naar `/cart/<variant>:<qty>?discount=...&utm...` of naar `event.URL` (PDP). Bij K3 de code via `/discount/<code>?redirect=<PDP>`.

### 5. Niets remt de frequentie, en de inbox is al kwetsbaar (hoog, risico)

**Bewijs.** Smart sending staat bewust uit in alle v4-flows. De prioriteitsregels kennen alleen v4-flows, niet de vier oude naflows, lead magnets, T2SmtR of campagnes. Outlook-spamratio 0,31% (grens 0,3%, `research/lijst`). Nieuw gevonden: checkout-mail 1 van Y2TmNB heeft een **bounce rate van 16 tot 17,5%** (308 bounces op 1.816 in 30 dagen; latere mails 0,3 tot 0,6%), welcome-mail 1 2,3%. Dat zijn typfouten en nepadressen uit de checkout, en v4 C1 erft dat. Het header-logo verdwijnt in dark mode (`research/deliverability/01-inbox-check.md`).

**Fix.** Segment "frequentieplafond" over alle mail (inbox-check fix 2) vóór de eerste campagne; smart sending aan op de oude naflows; checkout-e-mailvalidatie (typo-suggestie in Shopify checkout) onderzoeken; logo geplat op crème (inbox-check fix 1). Bounce per eerste mail dagelijks in het Slack-rapport.

### 6. De QA-poort ziet inhoud niet, en "klaar" betekent niet klaar (hoog, proces)

**Bewijs.** W2 met placeholders als "klaar" (S3). Klaviyo-versies van C1 tot C3 ouder dan de repo (S7). OVERZICHT.md toont C4-onderwerp nog met "10%%" en C1 als "Something stop you at checkout?" terwijl de plannen "Forgetting something?" zeggen: drie bronnen voor hetzelfde onderwerp. Titelaannames (S2) staan als "nakijken vóór livegang" in een commentaar, niet als blokkerende fout.

**Fix.** Eén poort vóór `--live`: (1) grep op placeholders, (2) template-hash in Klaviyo gelijk aan lokaal, (3) elke titel in een filter bestaat in Shopify, (4) onderwerp in flow = onderwerp in manifest. Fout = stop.

### 7. Het oude T01-pad verspreidt zes weken verboden claims (middel-hoog, juridisch)

**Bewijs.** Gecachte templates (`/tmp/hist/tpl`, 7 okt): alle 5 oude checkoutmails (UD7QXp, TK3h6j, VPBrLr, UMURrd, RbaQfc) en welcome 7 en 8 (Tkx4bs, RqvU5g) hebben een banner "FREE SHIPPING | 100-DAY TRIAL"; browse X9w6vN "Rated 4.9/5 by 30,000+ Customers"; welcome 2 "scratched non-stick pans". Oude welcome-laatste: "Your Extra Discount Expires Tonight" bij een code die nooit verloopt. DECISIONS verbiedt "100-day trial" en "30,000".

**Fix.** In de gekopieerde oude templates binnen de v4-flows alleen de banner vervangen (30-day returns) en de "expires tonight"-preview weghalen. Dat verandert de test nauwelijks en haalt het risico weg. Of T01 in checkout korter (3 weken).

### 8. Het e-book en de "$70 in gifts" kloppen niet met wat de klant krijgt (middel)

**Bewijs.** Orders bevatten nu "Plastic-Free Home E-Book" ($0). 72 vermeldingen in de mails noemen "Plastic-Free Home e-book", maar 21 links gaan naar `/products/e` = "The Green Clean E-Guide" voor $50. De $70 rekent het e-book als $50 aan een prijs waarvoor niemand koopt (referentieprijsrisico).

**Fix.** Knop naar de echte download of `/products/the-green-clean-e-guide` (UNLISTED, $0); gift-waarde onderbouwen of "4 free gifts" zonder dollarbedrag. Beslissing D7.

### 9. Belofte "10% plus gifts" is in de checkout niet bewezen (middel, zie S5)

**Bewijs.** HI10 combineert met niets; er draait een automatische BXGY-korting en gifts als $0-producten via een app. Tickets "The discounts were never applied" (CRO 03). De unieke pools krijgen de combinatie-instelling die Klaviyo standaard meegeeft.

**Fix.** S5. Na de test de combinatie-instelling per pool vastleggen in GO-LIVE.

### 10. Land en tijdzone: verkeerde versie en nachtzendingen (middel)

**Bewijs.** Steekproef van de 100 nieuwste profielen: 46 zonder land, 47 zonder tijdzone; van 48 Alia-inschrijvers 15 zonder land (31%), maar 10 met "United States". W4 kiest INT als het land leeg is, ook voor Amerikanen (welcome heeft geen valuta-terugval). Zonder tijdzone geldt de accounttijd (US/Eastern): "tot 09:00" is in Sydney middernacht, en Australië is na de US de grootste markt (32 van 250 orders). `person.Country` in C4 is nog nooit getest. Canada staat in Shopify Markets op `ADD_DUTIES_AT_CHECKOUT`, terwijl C4/INT "Duties paid" zegt.

**Fix.** W4: geen land = US-versie zonder 12-pcs-blok (neutraal), of W4 samenvoegen met `{% if %}`. Vervolgmails: "verstuur in de tijdzone van de ontvanger" plus een uurfilter is niet mogelijk; accepteer of zet AU-profielen via een segment op een eigen tak. Canada: één testcheckout, daarna de duties-regel per markt.

### 11. Cadeaukopers (19%) krijgen gebruiksmails, en Q4 staat voor de deur (middel-hoog, geld)

**Bewijs.** Enquête: 19% koopt als cadeau. Een gever krijgt P2 ("If you can do an egg"), U1 ("Show us your first egg?" met 15%), review, N1 ("How's your pan at six months?"), R1-pan. Er is geen detectie (factuur- en verzendnaam). BFCM begint 20 november; er is geen levertermijn-logica ("bestel vóór X voor Kerst", mediaan levering 11,7 dagen, internationaal langer).

**Fix.** Cadeauvlag op Placed Order (verzendnaam ongelijk aan klantnaam, of Shopify gift-optie) en een korte gevertak: "Hoe vond hij/zij het?", verzorgkaart om door te sturen, geen first-egg-UGC. Kerst-deadlinemails per markt als campagne. Beslissing D6.

### 12. We meten minder dan we denken (middel, leren)

**Bewijs.** `research/testing/06-meetplan-v4.md`: in 6 weken zien we alleen +36% (welcome) tot +71% (cart). T01 splitst per flow, niet per persoon: iemand kan v4 in checkout en oud in cart zijn. T02 is verward (zwakte 2). T04 en T05a sturen alles naar het hoofdbericht tot iemand "Start test" klikt. UTM's zijn dubbel gezet (hard in de HTML én `add_tracking_params`); niemand heeft één klik end-to-end gevolgd tot Shopify, GA4 en Triple Whale. Klaviyo-omzet is toegeschreven, niet extra; er is geen holdout op programmaniveau.

**Fix.** Eén testorder per flow met UTM-controle in Shopify en Triple Whale; T01 als vangnet behandelen (stopt slechte v4-flows), niet als bron van conclusies; vanaf februari een 10%-holdout op welcome en post-purchase (T13) om echte meeropbrengst te zien.

### 13. Drie prijzen voor dezelfde set (middel, vertrouwen en claims)

**Bewijs.** Shopify vandaag: 6-delige set $399 met compare-at $1.384 (ACTIVE, voorraad -330), $349 met compare-at $749 (BDAY, UNLISTED), $449 (SB, UNLISTED). 12-delig $599 en twee listings van $699 met gratis pizza steel (ticket "set $499 werd $699"). Wie $399 betaalde krijgt via W4, C3-P, R2 of A2 de set voor $349 te zien. Twee verschillende "was"-prijzen voor hetzelfde product is een referentieprijsrisico.

**Fix.** Beslissing D5: één listing, één compare-at, en de mails volgen.

### 14. Triple Pixel uitzetten kan bereik kosten (middel, ongetest)

**Bewijs.** Laatste 30 dagen: browse Triple Pixel (TyEjuQ) 13.901 ontvangers, $14.129; Klaviyo-browse (Wj6x6V) 13.502, $9.779. Checkout Triple Pixel (Tsg2tV) 3.222 ontvangers, $4.656. v4 gebruikt alleen Klaviyo-events. Hoeveel van de Triple Pixel-ontvangers Klaviyo zelf niet herkent, is niet gemeten.

**Fix.** Vóór het uitzetten: overlap per profiel over 30 dagen (Received Email uit TyEjuQ zonder Viewed Product XNtYMB in 24 uur ervoor). Is die groot: TyEjuQ als vangnet laten lopen met filter "niet in v4 · Browse in 7 dagen".

### 15. Overgang en eigenaarschap (middel, proces)

**Bewijs.** Oude flows op Draft "in dezelfde minuut" stopt iedereen die halverwege zit (welcome: ongeveer 4.000 nieuwe inschrijvers per week, dus rond 5.000 tot 6.000 midden in de reeks). Homestead werkt nog in het account. Volgens LOG blokkeert auto-modus wijzigingen aan live flows.

**Fix.** Oude welcome niet op Draft maar een flowfilter "Subscribed to list Uw8eZG zero times since 8 okt" (nieuwe instroom eruit, lopende mensen maken af), na 14 dagen Draft. Eén eigenaar per Klaviyo-object, schriftelijk met Homestead.

---

## 1. Klantreis per type (eerste 30 dagen, v4-arm)

Uitgangspunt: flowbomen in `exports/live/flows/OVERZICHT.md`, plus de oude flows die live blijven. "x" = mail.

| Type | Wat er gebeurt | Mails week 1 | Wat botst |
|---|---|---|---|
| **1. Nieuwe inschrijver US** (Alia, bekijkt pan, cart om 20:10, koopt niet) | d0 20:30 W1 (HI10) · 20:40 K1 (HI10) · d1 09:00 W2 **overgeslagen** (cart-mail < 24 u) · d1 20:40 K2-new · d3 09:00 **W3 en K3 tegelijk** (HI10 en eigen code "ends Fri") · d6 W4-US · d10 W5. Browse start niet (welcome-filter werkt). Campagnes vanaf d14, mits segment bestaat en de verzender het gebruikt | 6 | Founder-mail W2 valt definitief weg bij iedere cart-verlater. Twee codes op één ochtend. Oude arm: 8 welcome + 10 FTL op d30-41 als S8 ontbreekt |
| **2. Internationaal zonder land** (bijv. Australië, geen tijdzone) | Welcome zoals 1, alle "09:00"-mails om middernacht lokaal. W4 → INT (toevallig goed). Checkout: C4 kiest via valuta AUD → INT, "duties paid". Amerikaan zonder land krijgt W4-INT zonder set en met duties-tekst | 4-6 | Nachtzendingen; Canada ziet "duties paid" maar betaalt invoerrechten in de checkout (`ADD_DUTIES_AT_CHECKOUT`) |
| **3. Schortkoper** ($49) | P1-first (1 u) · FREE E-GUIDE · E-Book (1-3) · Pan Education 6x vanaf in-transit · Mystery Gift 4x incl. 20%-aanbod · review d+14 · P3 d20 via accessoire-tak (p3-apron wordt nooit geraakt door de titelfout) · R1-acc d45 | 6-8 | 6 mails pan-uitleg zonder pan; 16 mails in 30 dagen; garantie "75 jaar" in K3/C4 bij een schort is onbeslist (3.27) |
| **4. Setkoper > $300** (via onze link naar $349 BDAY) | Checkout: C1 · **C2-ACC "Yours, or a gift?"** · C3-S (via $value) · C4. Na koop: P1 · **geen P2, geen P2-safe** · P3 **"Now meet the pan (10% off)"** · geen UGC, geen anniversary · R1-acc "Ready for the pan?" | 4-5 | Fout 1. Wie $399 betaalde ziet in andere mails $349 (zwakte 13) |
| **5. Terugkerende klant** (heeft Pan Pro, legt Deep Pan in cart) | K1 "One pass with a damp cloth" (pan-uitleg aan eigenaar) · K2-returning (goed) · K3 code. Checkout: C1 met pan-uitleg en C3-P "One pan, or three for $349?". Winback R1/R2 loopt parallel; cooldown voorkomt een tweede code binnen 30 dagen, HI10 werkt toch altijd | 3-4 | K1 en C1 zijn niet klantbewust; HI10 is per klant onbeperkt herbruikbaar |
| **6. Cadeaukoper** (pan voor moeder) | P1 · P2 "If you can do an egg" · U1 "Show us your first egg?" · review · P3 · later N1 "How's your pan at six months?" | 3-4 + oude naflows | Alles gaat over gebruik door iemand die de pan niet heeft |

Wat wél goed gaat in alle zes: een aankoop stopt elke verkoopflow; browse wijkt voor welcome, cart en checkout; cooldown voorkomt een tweede unieke code binnen 30 dagen; de nocode-mails beloven geen deadline.

### 2.4 Testprofielen vóór "turn on" (minimaal)

| # | Profiel | Wat bewijzen |
|---|---|---|
| 1 | US, land "United States", nieuw, checkout met Pan Pro Standard | C1 → C2 → C3-P → C4, code verschijnt overal gelijk, datumtag gevuld, `/discount/`-link landt met code |
| 2 | Land "US" (ISO), checkout $349 BDAY-set | C2 (niet C2-ACC), C3-S, C4-US met set-blok |
| 3 | Land "Netherlands", checkout in EUR | C4-INT, "duties paid", geen USD-prijzen |
| 4 | Geen land, valuta AUD | C4-INT via terugval; W4-route bij welcome |
| 5 | Cart met schort (Azure) | K1-ACC, K3; na fictieve order: P3-apron |
| 6 | Cart met alleen een gratis gift | Geen instap (triggerfilter) |
| 7 | Bestaande klant, cart Deep Pan | K2-returning; C2 overgeslagen |
| 8 | Welcome-inschrijving + direct cart | W2/W3-overslaanregel, aantal mails per dag |
| 9 | Order met e-gift card | P3 eindigt (UYALJ8 neemt over) |

Plus één echte checkout per code-type (HI10, unieke pool) tot het betaalscherm, en één klik per flow gevolgd tot Shopify (UTM's) en Triple Whale.

---

## (c) Wat we juist goed doen (kort)

- Timing en volgorde zijn op 12 maanden eigen data gebaseerd, niet op benchmarks.
- Eén prioriteitsmodel tussen flows, met "overslaan" in plaats van "uitstappen" waar dat hoort.
- Eerlijke urgentie: echte vervaldatum per unieke code, geen countdown bij HI10 of nocode.
- Eén unieke code per persoon per 30 dagen, codes per pool herkenbaar.
- Testdiscipline: vaste horizon, standaard bij twijfel, guardrails op uitschrijving en spam, BFCM apart.
- Delivered Shipment (Shopify) als bezorgtrigger, met P2-safe voor de 64% zonder bezorgevent.
- Bewijs als kern (rapport 25895, PFAS) sluit aan op de enquête (68-76% koopt om non-toxic).
- Veel QA-gereedschap (render, 63 tests, inbox-check, dry-run) en alles reproduceerbaar in scripts.

---

## (d) Beslissingen voor de eigenaar

| # | Vraag | Advies |
|---|---|---|
| D1 | HI10 automatisch in de checkoutlink van C1 na 30 minuten, of C1 zonder code (de historische winnaar)? | C1 zonder auto-apply; HI10 mag in de tekst. T03 (met/zonder HI10 vroeg) naar voren halen in plaats van T02 in checkout |
| D2 | HI10 "once per customer"? | Ja |
| D3 | Gefaseerd live in plaats van alles op 8 oktober? | Dag 1 checkout en cart (na S1 t/m S7), browse na de Triple Pixel-overlapcheck, welcome als W2 klaar is, groep B na het opruimen van de oude naflows |
| D4 | Oude naflows (FREE E-GUIDE, E-Book, Pan Education, Mystery Gift): uit, samenvoegen of filteren? | E-Guide en E-Book in P1, Pan Education uit, Mystery Gift na P3 |
| D5 | Welke 6-delige set-listing blijft, met welke compare-at? | Eén listing op $349 met één onderbouwde compare-at, de andere doorsturen |
| D6 | Gevertak en Kerst-levertermijnen vóór 20 november? | Ja, klein beginnen: cadeauvlag plus twee mails |
| D7 | Welk e-book is de gift, en mag "$70 in gifts" blijven? | Eén e-book, juiste link; "$70" alleen met onderbouwing |
| D8 | Oude T01-arm: banners met "100-DAY TRIAL" vervangen of T01 inkorten? | Banner vervangen in de kopieën |
| D9 | Wie verstuurt de campagnes vanaf morgen, en met welke uitsluitingen? | Schriftelijk vastleggen met Homestead |
| D10 | Programma-holdout (5 tot 10%) vanaf februari? | Ja, anders weten we nooit wat de mails echt extra opleveren |

---

## Bronnen en controles van vandaag

- Shopify GraphQL: `discountNodes(status:active)` (2 pagina's), `codeDiscountNodeByCode` voor HI10 en `98347983474334593`, automatische korting "FREE GIFT", producten (sets, schorten, e-books) met status en compare-at, laatste 50 orders (line-item-titels).
- Klaviyo: `get_flows` (live en "v4"), `get_segments` (sinds 6 okt), triggers van TSUnLs, YyaMjx, YcXbHx, metric VjA7Qr, flow-rapporten 30 dagen (naflows; checkout, cart, browse incl. Triple Pixel; bounces), 3 Received Email-events (bevestigt `Campaign Name` = berichtnaam en `$flow` = flow-ID, dus de CODE-cooldown werkt technisch), 100 nieuwste profielen (land, tijdzone, bron).
- Repo: templates in `klaviyo/templates/v3/`, `scripts/build_flows.py` r. 78-110, `exports/live/templates.csv`, `exports/manifest.csv`, gecachte oude templates in `/tmp/hist/tpl`.
- Niet gecontroleerd (geblokkeerd of buiten bereik): siraatskitchen.com zelf (PDP-blok "Risk-free purchase", countdown), Triple Whale-attributie, Klaviyo coupon-instellingen in de UI.
