# 04 · Siraat-diagnose: waarom onze klanten afhaken, gerangschikt, met bewijs

Datum: 7 oktober 2026. Alleen gelezen, alleen aggregaten. Geen persoonsgegevens opgeslagen (profiel-ID's alleen gehasht in een tijdelijke scratchpad, niet in de repo).

## Databronnen en methode

| Bron | Wat | Venster |
|---|---|---|
| Klaviyo Events API (revision 2025-10-15, GET) | Placed Order (5.143 events), Checkout Started (10.576 events, 10.434 checkout-tokens), Added to Cart (12.625 events, 3.736 profielen) | Orders en checkouts 7 sep t/m 6 okt; ATC 21 sep t/m 6 okt |
| Intelligems (Shopify-pixel) | Trechter, apparaat, kanaal, omzet per bezoeker | 7 sep t/m 6 okt |
| ShopifyQL (via Intelligems) | Maandomzet, retouren, nieuw versus terugkerend | april t/m 6 okt; 90 dagen |
| Shopify Admin GraphQL | Plan, betaalwallets, valuta | 7 okt |
| Gorgias analytics | Intents, pre-sale, retour/annulering-teksten (zoekwoorden), kanaal, reactietijd, pre-sale naar order | 90 dagen; pre-sale 120 tot 30 dagen geleden |
| Repo | baselines/, research/ (alle mappen), content/reviews, content/products, content/facts | t/m 7 okt |

**Definities.** "Echte checkout" = checkout-token met minstens één betaald product en waarde van minstens $20 (7.625 van 10.434; de rest zijn lege of alleen-gift-checkouts en webhook-ruis). "Verlaten" = geen order van hetzelfde profiel binnen 1 uur. "Herstel" = order van hetzelfde profiel binnen 14 dagen na het verlaten. Klaviyo ziet alleen bekende profielen (e-mail of eerdere klik), dus ATC-cohorten zijn de warmere helft van het verkeer.

**Kanttekeningen.** (1) September bevat de Labor Day-sale; (2) "Customer Locale" is de browsertaal, niet het land; (3) zoekwoordtelling in tickets is grof (een ticket kan meerdere thema's raken); (4) Intelligems toont bedragen met een EUR-label maar de verhoudingen zijn bruikbaar; (5) de mediane eerste reactietijd van Gorgias kan automatische bevestigingen bevatten.

---

## 1. Kerncijfers in één oogopslag

| Meting | Waarde |
|---|---|
| Conversie per bezoeker (site) | 1,64 procent; per sessie 1,36 procent |
| Mobiel | 82 procent van sessies, 74 procent van orders; mobiel converteert per bezoeker even goed als desktop (1,66 tegen 1,56 procent) |
| In-app browser (FB/IG) | 40 procent van orders (FBAN 19,5, Instagram 13,8, FBAV 6,9) |
| Echte checkouts in 30 dagen | 7.625, waarvan 61,7 procent binnen 1 uur koopt; 2.920 verlaten door 1.775 unieke profielen |
| Tijd tot aankoop bij kopers | 96 procent binnen 15 minuten na checkout-start |
| Herstel na verlaten | 4,6 procent koopt binnen 14 dagen (135 orders, $37.760); verspreid over 1 uur tot 14 dagen |
| Waarde verlaten checkouts | $1,1 miljoen (scheef door enkele grote carts; mediaan set-checkout $599) |
| Single-item checkout | 44 procent verlaten; met meerdere producten 24 procent |
| Nieuwe klanten | 88 procent van netto-omzet (90 dagen); 72 procent van orders op de dag dat het profiel ontstond |
| Betaalmethoden | Shopify Payments (incl. Shop Pay, Apple Pay, Google Pay) 86 procent, PayPal 9 procent, TikTok Shop 2 procent, Affirm 0,4 procent; geen Klarna, Afterpay of zichtbare Shop Pay Installments |
| Orders met kortingscode | 18 procent; grootste codes zijn creator-codes (SUGARCOATEDMASALA 158) en SIRAAT10/15/5 |
| Retouren | 5,5 procent van bruto-omzet in september (april 3,4 procent) |
| Orders per maand | mei 8.014, september 5.100 (dalend verkeer) |

---

## 2. Waarom ze afhaken, gerangschikt

Rangorde = geschatte omzet die erachter zit maal hoe zeker het bewijs is.

### 1. Het risico "plakt het bij mij?" is niet afgedekt, en het beleid maakt het erger

- **Bewijs.** Plakken: 222 van 806 retourverzoeken (28 procent), 102 van 387 refundtickets, 81 van 154 lage Trustpilot-reviews (180 dagen), 51 pre-sale tickets. Retour/trial: 112 retourverzoeken noemen "trial" of "100 day", 165 noemen retourverzending of label; 100 van 154 lage reviews gaan over retour of de trial, 47 noemen Siraat "scam" of "fake". Het beleid sinds 15 sep: alleen ongebruikt, retour op eigen kosten, "food sticking is not a defect". De site-balk en help-artikelen zeiden nog "100-DAY TRIAL" (content/facts). Macro 247063 en guidance 5302114 spreken elkaar tegen over retourkosten.
- **Mechanisme.** Verliesaversie plus spijtaversie bij een ervaringsgoed: je weet pas of het werkt na gebruik, en na gebruik mag het niet meer terug. Wie Trustpilot leest voor de aankoop (vergelijkers), ziet "scam".
- **Wat het kost.** Moeilijk exact; het raakt conversie bovenin (reputatie), retouren onderin ($74.000 in september) en reviews.
- **Zekerheid.** Hoog voor het bestaan van het probleem, middel voor de grootte.

### 2. Betalen in de verkeerde context: in-app browser, Android, geen termijnen

- **Bewijs.** 40 procent van orders uit de FB/IG-webview. ATC-cohort (bekende profielen, 7 dagen): Mac 42 procent order, iOS 32 procent, Windows 32 procent, Android 23 procent, Samsung Internet 8 procent. BNPL vrijwel afwezig (Affirm 19 orders) terwijl 13 procent van de orders boven $350 ligt. Single-item checkouts van $100 tot $199 worden in 43 procent verlaten.
- **Mechanisme.** Wrijving en pijn van betalen. In de webview ontbreken autofill en vaak Apple Pay; Android-gebruikers missen Apple Pay en hebben vaker geen Shop Pay. Termijnen ontkoppelen betalen en gebruik.
- **Zekerheid.** Middel tot hoog (eigen data plus sterke externe casus); de precieze oorzaak per Android-segment moet een CRO-audit bevestigen.

### 3. De PDP beantwoordt de twijfel niet (de grootste absolute lek)

- **Bewijs.** ATC-ratio 5,25 procent van sessies, bounce 71,5 procent. Pre-sale vragen (526 in 90 dagen): materiaal en veiligheid 160, deksels 82, herkomst 69, maat 54, schoonmaken 52, plakken 51, oven/vaatwasser 30, inductie en kookplaat 24. Okendo heeft 2.226 reviews op de pannen die niet gericht worden ingezet. Verboden of onjuiste claims staan nog live (nutrients, scratch-proof, lifetime, 100-day trial).
- **Mechanisme.** Onzekerheid en keuzestress; sociaal bewijs ontbreekt waar het nodig is.
- **Zekerheid.** Middel (PDP zelf niet bekeken: site geblokkeerd in deze omgeving).

### 4. Te veel keuze en tegenstrijdige prijzen

- **Bewijs.** Drie listings van de 6-delige set ($349 verborgen, $399 actief, $449 "SB"); Mini duurder dan Small; Pan Pro-kopielistings met eigen prijzen (30 checkouts in 30 dagen bevatten een "-copy"-listing); badges die niet kloppen. Checkouts met de 6-Pcs SB-listing worden in 43 procent verlaten, de 12-delige set in 30 procent. Deep Pan (varianten zonder specs, geen deksel voor 24 cm) wordt in 46 procent verlaten, de hoogste van alle pannen.
- **Mechanisme.** Choice overload bij een moeilijke, onzekere keuze; wantrouwen bij prijsverschillen.
- **Zekerheid.** Middel.

### 5. Levertijd en verwachting

- **Bewijs.** Beleid 6 tot 10 kalenderdagen, ook in de VS; "Order Status" is het grootste ticket-thema met een intent (1.182 in 90 dagen) en "No Reply" (3.395, grotendeels automatische mails) daarboven; 66 tickets over vertraging. Geen leverdatum zichtbaar bekend.
- **Mechanisme.** Onzekerheid over het moment; bij cadeaus doorslaggevend.
- **Zekerheid.** Middel; Q4 hoog.

### 6. Prijs zonder anker dat de koper gelooft

- **Bewijs.** Prijs/valuta/korting is het grootste pre-sale thema in de oudere VoC-steekproef (22 van 152). Permanente compare-at van $439 bij $134. Codes in verlaten checkouts: 7,7 procent heeft al een code. Korting in cart-mails trok de omzet niet omhoog (dag-2-mail met 10 procent: $0,79 per ontvanger).
- **Mechanisme.** Referentieprijs ongeloofwaardig; de echte vergelijking (de nonstick-pan die je elke 12 tot 18 maanden vervangt) wordt niet gemaakt.
- **Zekerheid.** Middel.

### 7. Te veel mail voor te weinig intentie (giveaway-lijst)

- **Bewijs.** Nieuwe lead krijgt 18 mails in 41 dagen plus browse, cart en campagnes; welcome 1,73 procent uitschrijving per week; failure-to-launch $0,04 per ontvanger; flows 0,076 procent spam tegenover campagnes 0,033 procent.
- **Mechanisme.** Reactance en deliverability-erosie.
- **Zekerheid.** Hoog.

### 8. Geen pre-sale gesprek

- **Bewijs.** Gorgias is in de praktijk alleen e-mail (27 chattickets in 90 dagen). Pre-sale vragenstellers (431, 120 tot 30 dagen geleden) kochten in 13 procent binnen 30 dagen; 165 van hen waren al klant. De reactie is snel (mediaan eerste reactie circa 7 minuten), maar de bezoeker weet niet dat hij het kan vragen.
- **Zekerheid.** Middel; volume klein, signaal sterk.

### Wat níet de oorzaak lijkt

- **Verzendkosten**: gratis, dus de Baymard-nummer 1 valt weg.
- **Valuta in de checkout**: lokale valuta staan aan (AUD, SGD, GBP, CAD en meer worden in de checkout getoond). Het oudere bezwaar "prijzen in USD" komt nu eerder uit mails en ads die USD tonen aan AU- en CA-klanten.
- **Internationaal als zodanig**: checkouts met browsertaal en-AU (20 procent verlaten), en-GB (16), en-SG (18), en-CA (27) worden juist minder verlaten dan en-US (42 procent). Mogelijke verklaringen: vergelijkingsgedrag in de VS (Amazon, HexClad), meer impulsverkeer uit Meta, of de 6 tot 10 dagen levering die in de VS slechter afsteekt. Dit is de verrassendste bevinding en vraagt verificatie (CRO-audit, opdracht 05).
- **Tijd**: wie koopt, koopt meteen. Het probleem is niet dat mensen "erover nadenken", maar dat ze vastlopen of twijfelen.

---

## 3. Per type koper

| Type | Wat we zien | Waarom ze afhaken | Wat ze terugbrengt |
|---|---|---|---|
| **Pan-koper** (Pan Pro, 70 procent van orders; mediaan checkout $144) | Single-item, vaak impuls uit Meta, mobiel in de webview. Standard 40 procent verlaten, Large 30, Small 43, Mini 44. Wie een deksel toevoegt verlaat maar 21 procent. | Risico plakken, betaalwrijving in de webview, maatkeuze, "is dit een scam" na Trustpilot | Herstelde cart in een echte browser met Apple Pay/Shop Pay; de watertest-video; review van iemand die het leerde; deksel als logische aanvulling ("complete it with the lid"); termijnen vanaf $134 |
| **Set-koper** (6-delig $349 tot $449, 12-delig $599, Pro $479, Full Pro $799; mediaan $599) | Bewuster: 12-delig 30 procent verlaten, 6-delig 36, 6-Pcs SB 43. Vaak via bestpansreviewed.com of zoekverkeer. | Prijs in één keer, overleg met partner, welke set, verwarring over listings en prijzen, levertijd | Termijnen; "what's in the box" visueel; vergelijkingstabel 6 tegen 12; deelbare samenvatting voor de partner; prijs per stuk tegenover losse aankoop; echte set-reviews (er zijn er nog nauwelijks: Okendo ophalen) |
| **Potten-koper** (Pot Set 6-Pcs, $195.668 in 90 dagen, in de data als set) | 41 procent verlaten. Status van het product onduidelijk (DRAFT in facts, actief in verkoop; Gorgias zegt "niet los verkrijgbaar"). | Geen reviews over potten (gat in content/reviews), dekselvragen | Potten-specifieke bewijsmail en PDP; consistentie in service-antwoorden |
| **Deep Pan-koper** (mediaan $169) | Hoogste verlaatpercentage van de pannen: 46 procent. | Maatverwarring (Standard = 24 cm hier, 28 cm bij de koekenpan; 28 en 30 cm zonder specs; geen deksel voor 24 cm) | Maathulp en dekselcompatibiliteit; review over roerbakken en sauzen |
| **Pizza Steel-koper** (mediaan $149) | 35 procent verlaten; vaak cadeau of hobby. | Weinig reviews (Sergio C. als enige productbewijs), diameter onbekend in de data | Video van het resultaat, specificaties, cadeau-angle |
| **Accessoire en schort** (mediaan $89; snijplank 29, utensils 22, waterfles 76 procent verlaten) | Accessoires gaan meestal mee met een pan. Schort komt vooral als gift; zelfstandig weinig volume. | Lage prijs, lage urgentie; schort heeft PVC/PU (niet in een "no coatings"-zin) | Als add-on in de cart en post-purchase, niet als eigen flow; de waterfles-checkout (76 procent verlaten) apart onderzoeken |
| **Cadeaukoper** (gift in 47 pre-sale tickets en 45 annuleringen; e-gift card 0 orders in 30 dagen) | Q4 komt eraan. Annuleringen binnen het 1-uursvenster ("ordered by mistake", "changed my mind": 72). | Levering vóór de datum, maat voor een ander, retour na de feestdagen | Cutoff-datum per land, gift receipt, verlengde ruiltermijn voor cadeaus, e-gift card als veilige keuze (labels nu in euro: fixen) |
| **Internationaal** (36 procent van orders: AU 12, CA 5, SG 4, UK 4, AE 2, HK 2) | Checkout-conversie beter dan US. AU-orders kleiner (AOV $187). Lokale valuta staan aan. | Mails tonen USD; levertijd; geen Afterpay in AU; Middle East-vertragingen (eigen flow) | Prijzen in lokale valuta in mails (of zonder bedrag), Afterpay/Klarna per markt, "No import duties" (DDP) als feit |
| **Vergelijker** (bestpansreviewed.com 8,4 procent van orders, AOV $291, 84 procent checkout-conversie) | Hoogste waarde en zekerheid. | Komt pas na onderzoek; afhakers zijn mensen die nog vergelijken | Vergelijkingstabellen, Light Labs-rapport, garantievoorwaarden, set-voordeel |
| **Bestaande klant** (12 procent van omzet) | Repeat-AOV $194. | Geen logische tweede stap behalve deksel; ervaring met plakken | Onboarding die de eerste week laat slagen; deksel en tweede maat; referral; cadeau voor een ander |

---

## 4. Wat de bestaande research al dekt (en wat niet)

| Al gedaan | Waar |
|---|---|
| Flowsysteem v3 (31 mails), nieuwe flows, UX-standaard, offer-ladder, testplan, UTM, QA, copy-playbook, productbibliotheek, VoC, beelden | research/ux-2026-10-07, copy, testing, qa-2026-10-07, potentie, ux-round2, content/ |
| Niet gedaan | Checkout- en PDP-CRO, betaalmethoden/BNPL, webview, landingspagina's per flow, SMS-strategie, Meta-afstemming, retourbeleid en leer-garantie, Okendo-mining, Gorgias pre-sale als flow, prijsarchitectuur en compliance, Q4 cadeau-logistiek, deliverability-diepte, lijstkwaliteit per bron, referral |

Die lijst is de basis voor `05-agent-backlog.md`.
