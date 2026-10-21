# 01 · Giveaway-instroom: hoe slecht is hij echt, en wat doen we eraan

Datum: 21 oktober 2026. Alleen gelezen uit Klaviyo (Events API GET en metric aggregates, revision 2025-10-15). Niets gewijzigd, niets verstuurd. Profiel-ID's alleen in de scratchpad; hier staan uitsluitend aggregaten. Bouwt op `research/lijst/01-cohorten.md` (7 okt) en `03-voorstel.md`; dit stuk beantwoordt de vraag van Floris: wat doen we aan laagwaardige instroom uit de giveaway-pop-up?

## Kern in vijf punten

1. **De giveaway is iets zwakker dan de kortingspop-up, maar niet dramatisch.** In dezelfde twee weken (31 aug tot 13 sep, beide pop-ups tegelijk live) koopt 10,5 procent van de giveaway-aanmelders binnen 30 dagen tegen 12,1 procent bij de kortingspop-up, voor $22,90 tegen $24,63 per aanmelder. Uitschrijving (19,0 tegen 19,2 procent) en spamklachten (0,8 tegen 0,9 procent) zijn gelijk. Het grotere verschil over de hele periode (11,0 tegen 13,8 procent) komt voor een deel door seizoen: de korting liep vooral in augustus (jubileumsale), de giveaway in september en oktober.
2. **Het echte probleem is wat er ná de pop-up gebeurt, voor alle pop-up-aanmelders.** 81 procent van de giveaway-aanmelders klikt en koopt niet in de eerste 14 dagen. Die groep krijgt in dag 14 tot 30 toch nog 7,5 mails (waarvan 6,8 campagnes, ruim 3 per week), en levert in die periode 67 procent van de uitschrijvingen en 76 procent van de spamklachten van het cohort.
3. **Giveaway-aanmelders krijgen meer campagnemail dan wie dan ook.** In hun eerste 30 dagen 10,1 campagnemails, tegen 6,6 voor de kortingspop-up en 4,8 voor checkout-aanmelders. Oorzaak: sinds 4 september gingen 16 campagnes naar de volledige Email List (`Uw8eZG`) of naar "EB | US Subscribers" (`VJkN42`), beide zonder engagementfilter, en 7 daarvan met Smart Sending uit.
4. **Geen bot- of nepprobleem zichtbaar.** 0,00 procent wegwerpdomeinen, minder dan 0,05 procent typodomeinen, maximaal 5 giveaway-aanmeldingen per minuut, geen pieken. Hard bounce is 1,4 procent bij de giveaway, maar ook 1,5 procent bij de kortingspop-up en 1,6 procent bij checkout-opt-in: een algemeen typfoutprobleem, niet giveaway-specifiek.
5. **Zwakste subgroep: giveaway via Shopify-sync** (Alia-gegevens, maar binnengekomen met `$source` -50, 2.235 profielen): 8,3 procent koopt in 30 dagen, $18,60 per aanmelder. Uitzoeken hoe deze route ontstaat (Alia zet de klant in Shopify met Accepts Marketing).

## Methode

| Onderdeel | Keuze |
|---|---|
| Cohort | Eerste Subscribed to List-event (`SCvkku`) voor Email List `Uw8eZG` per profiel, 1 augustus tot en met 14 oktober 2026 (US/Eastern): **51.208 profielen**. |
| Bron | Profieleigenschappen op 21 okt: `$source`, `alia_campaign`, `alia_popup_name`, `alia_offer`, `Shopify Tags`. Klaviyo-formulieren tellen niet mee: alle 35 staan op draft, Form submitted (`VLq6p4`, `XimcLu`) is 0 in de periode. De pop-up is Alia (DECISIONS 7 okt). |
| Groepen | **Giveaway**: Alia-variant Order Refund, Card Game, Scratch Off, 0 Seconds, 8 Seconds or 25% Scroll, New Heading Copy, Giveaway, Scroll Depth, zonder kortingscode (21.491). **Kortingspop-up**: Alia Control of Smart Offers met code (BIRTHDAY10, SIRAAT10/15/5, LABOR10, PRIMETIME10) (23.870). **Shopify checkout/account**: `$source` -50 zonder Alia-gegevens (4.773). **Shop-login**: -50 met tag "Login with Shop" (919). **Overig**: back in stock, landingspagina's, API (151). Binnen Giveaway en Korting: "Alia" (`$source` Alia sign-up) of "Alia via Shopify" (-50 met Alia-gegevens). |
| Uitkomsten | Placed Order `RSNxYV` (alle kanalen, vanaf 2 uur vóór aanmelding), Clicked Email `W247h8` met Bot Click niet waar, Opened Email `WyrTym` (totaal en "menselijk": `machine_open` niet waar), Unsubscribed `YcWddQ`, Marked as Spam `VQMAAk`, Bounced `XDdu6P` met Bounce Type Hard, Received Email `YkRM4Q` (campagne = geen `$flow`). Alle events 31 jul tot 21 okt 23:05 UTC volledig opgehaald (2,6 mln opens, 4,4 mln ontvangen mails). |
| Vensters | Alleen profielen van wie het venster volledig verstreken is. 30 dagen: aanmelding tot 21 sep. 60 dagen: tot 22 aug (dus alleen kortingspop-up en checkout; de giveaway is daarvoor te jong). |
| Land | Klaviyo-locatie of `country_code`. Let op: land is vaak alleen bekend na een order. "Onbekend" (ongeveer 20 procent) bevat dus vrijwel alleen niet-kopers, en de US/niet-US-conversie is daardoor overschat. Vergelijk per land vooral klik en uitschrijving. |

Opens zijn onbetrouwbaar door Apple Mail Privacy: 77 procent van alle opens is een machine-open. Gebruik klik als signaal, opens hooguit "menselijk".

## 1. De cijfers per bron (30 dagen na aanmelding)

| Bron | Aanmelders | Ooit geopend (menselijk) | Klik 30 d | Uitschrijf 30 d | Spam 30 d | Hard bounce 30 d | Koopt 30 d (waarvan binnen 24 u) | Omzet per aanmelder 30 d | Omzet na dag 1 per aanmelder | Mails 30 d (campagnes) |
|---|---|---|---|---|---|---|---|---|---|---|
| **Giveaway** | 21.491 (30 d compleet: 7.870) | 66% (41%) | 15,8% | **19,3%** | 0,8% | 1,4% | **11,0%** (9,4%) | **$24,97** | $5,19 | **17,3 (10,1)** |
| Giveaway, Alia direct | 19.256 | 66% (41%) | 17,0% | 19,2% | 0,8% | 1,2% | 12,0% (10,2%) | $27,32 | $5,85 | 17,6 (10,3) |
| Giveaway, via Shopify | 2.235 | 67% (41%) | 12,8% | 19,6% | 1,0% | 1,7% | 8,3% (7,2%) | $18,60 | $3,43 | 16,5 (9,5) |
| **Kortingspop-up** | 23.870 | 70% (46%) | 15,3% | 17,0% | 0,7% | 1,5% | 13,8% (11,7%) | $29,49 | $5,38 | 13,9 (6,6) |
| **Checkout/account (-50)** | 4.773 | 81% (56%) | 37,2% | 14,4% | 0,4% | 1,6% | 94,2% (94,1%) | $200,45 | $3,67 | 15,2 (4,8) |
| Shop-login | 919 | 88% (62%) | 48,8% | 18,7% | 0,3% | 0,3% | 82,3% (80,8%) | $222,09 | $20,44 | 15,7 (5,4) |
| Overig (BIS, landingspagina) | 151 | 82% (59%) | 35,7% | 23,5% | 2,6% | 0,0% | 24,3% | $67,91 | $21,59 | n.v.t. |

"Ooit geopend" en de klik zijn tot en met 21 oktober gemeten, de overige kolommen in het 30-dagenvenster. Spam = aandeel aanmelders met minstens één klacht (Gmail en Apple melden niet terug, dus onderteld).

**60 dagen** (alleen kortingspop-up en checkout compleet): kortingspop-up koopt 14,7 procent, $32,65 per aanmelder, 22,3 procent uitgeschreven, 1,0 procent spamklacht, 27,3 mails (14,5 campagnes). Checkout: 94,4 procent, $199,84, 21,9 procent uitgeschreven. Voor de giveaway komt het 60-dagenbeeld vanaf 30 oktober (Order Refund) en half november (Card Game).

### Eerlijke vergelijking: dezelfde weken (31 aug tot 13 sep)

| | Aanmelders | Klik 30 d | Uitschrijf 30 d | Spam 30 d | Koopt 30 d | Omzet 30 d | Omzet na dag 1 | Campagnemails 30 d |
|---|---|---|---|---|---|---|---|---|
| Giveaway (vooral Order Refund) | 4.353 | 14,6% | 19,0% | 0,8% | 10,5% | $22,90 | $4,35 | 9,4 |
| Kortingspop-up (Smart Offers) | 4.625 | 16,0% | 19,2% | 0,9% | 12,1% | $24,63 | $5,16 | 8,4 |
| Checkout/account | 841 | 35,4% | 16,3% | 0,5% | 93,8% | $196,21 | $4,24 | 7,5 |

Lezing: de giveaway kost ongeveer 1,5 procentpunt conversie en $1,70 per aanmelder ten opzichte van een kortingspop-up in dezelfde weken. Zijn uitschrijvings- en klachtcijfers zijn niet slechter. Een hoge uitschrijving (19 procent in 30 dagen) zien we bij alle bronnen, zelfs bij kopers uit de checkout (14 tot 16 procent): dat is een frequentie- en doelgroepprobleem, geen bronprobleem.

### Giveaway-varianten (14 dagen, want Card Game is pas sinds 21 sep groot)

| Variant | Aanmelders | Klik 14 d | Uitschrijf 14 d | Spam 14 d | Koopt 14 d | Omzet 14 d |
|---|---|---|---|---|---|---|
| Card Game (US \| Evergreen) | 10.830 (14 d compleet: 7.159) | 14,4% | 14,7% | 0,9% | 10,8% | $26,66 |
| Order Refund (Evergreen en INT) | 5.262 | 11,5% | 13,8% | 0,5% | 9,5% | $20,51 |
| 0 Seconds | 1.603 | 14,2% | 14,7% | 0,5% | 9,7% | $22,13 |
| 8 Seconds or 25% Scroll | 1.350 | 13,6% | 15,6% | 0,7% | 9,4% | $23,50 |
| Scratch Off | 1.610 | 15,8% | 16,2% | 0,6% | **8,0%** | $20,19 |

Ter vergelijking, kortingspop-up 14 dagen: klik 12,8 procent, uitschrijf 13,1 procent, spam 0,5 procent, koopt 13,3 procent, $28,02.

### Per land (14 en 30 dagen)

| Bron, land | Aanmelders | Klik 30 d | Uitschrijf 30 d | Spam 30 d | Koopt 30 d (alleen land bekend, overschat) |
|---|---|---|---|---|---|
| Giveaway, US | 11.053 | 16,0% | 16,5% | 0,9% | 13,9% |
| Giveaway, niet-US | 6.250 | 22,9% | 23,4% | 0,8% | 12,7% |
| Giveaway, onbekend | 4.188 | 3,6% | 20,3% | 0,6% | 0% (per definitie) |
| Korting, US | 12.093 | 15,9% | 14,3% | 0,8% | 17,3% |
| Korting, niet-US | 7.339 | 22,1% | 19,2% | 0,4% | 16,3% |
| Checkout, US | 3.265 | 34,8% | 12,7% | 0,5% | 94,9% |
| Checkout, niet-US | 1.482 | 43,2% | 18,4% | 0,4% | 94,6% |

Niet-US-aanmelders klikken vaker, maar schrijven zich ook vaker uit (vooral Australië, Canada, Singapore). Vermoedelijk krijgen ze campagnes die over US-prijzen, -verzending of -feestdagen gaan. Het land-onbekend-deel (geen klik, geen order) is de kern van de dode instroom: 3,6 procent klikt ooit, 20 procent schrijft zich uit.

## 2. Wat het kost

### De groep die in 14 dagen niets doet

Giveaway-aanmelders met een compleet 30-dagenvenster (7.870). "Niets doen" = geen menselijke klik en geen order in dag 0 tot 14.

| Dag 14 tot 30 | Niets gedaan in 14 d (81%) | Wel geklikt of gekocht (19%) |
|---|---|---|
| Profielen | 6.400 | 1.470 |
| Mails per profiel (campagnes) | 7,5 (6,8) | 7,6 (6,1) |
| Koopt alsnog | 0,44% | 1,77% |
| Omzet per profiel (alle kanalen) | $1,06 | $3,96 |
| Aandeel in de omzet van dag 14 tot 30 | 54% | 46% |
| Uitschrijving | 4,5% (67% van alle uitschrijvingen) | 9,6% |
| Spamklacht | 0,30% (76% van alle klachten) | 0,41% |

Met menselijke opens als extra signaal (opent, klikt of koopt in 14 dagen) is de stille groep 57 procent in plaats van 81 procent, met $0,95 omzet en 0,24 procent spam per profiel in dag 14 tot 30.

Bij de kortingspop-up (60-dagenvenster compleet) is het beeld hetzelfde: wie in 30 dagen niet klikt of koopt (78 procent) koopt in dag 30 tot 60 nog 0,44 procent, $0,96 per profiel, krijgt in die 30 dagen 14,3 mails en schrijft zich voor 5,8 procent uit (0,27 procent spam). Uit `research/lijst/01-cohorten.md` §5: na 60 dagen zonder klik of order nog 0,36 procent conversie en $0,85 per profiel in de 30 dagen daarna.

### Omgerekend per maand

Huidige giveaway-instroom: 8.612 aanmelders in 1 tot 14 oktober, dus circa **18.500 per maand**.

| Post | Per 1.000 giveaway-aanmelders | Per maand (18.500) |
|---|---|---|
| Campagnemails aan de stille 81% in dag 14 tot 30 | 5.530 | circa 102.000 |
| Uitschrijvingen in dag 0 tot 30 | 193 | circa 3.570 |
| Spamklachten in dag 0 tot 30 (alleen terugmeldende providers) | 8 | circa 150 |
| Hard bounces in dag 0 tot 30 | 14 | circa 260 |
| Omzet van de stille groep in dag 14 tot 30 (alle kanalen) | $860 | circa $15.900 |

Ter vergelijking: campagnes leverden 1 augustus tot 21 oktober $304.800 geattribueerde omzet op 3,62 miljoen campagnemails, dus **$84 per 1.000 campagnemails** gemiddeld. De stille giveaway-groep brengt in dag 14 tot 30 ongeveer $0,14 per ontvangen mail op, maar via alle kanalen en zonder klik: welk deel daarvan door e-mail komt is onbekend, en het is beduidend minder dan het totaal (wie nooit klikt, krijgt geen klik-attributie; deze omzet loopt vooral via site, ads en SMS).

Het risico zit niet in de omzet van deze groep zelf, maar in wat zij met de reputatie doen: 3 op de 4 spamklachten komen van stille aanmelders. Een kleine daling in inbox-plaatsing bij Gmail (56 procent van de mail) raakt de volle $110.000 aan campagneomzet per maand, niet alleen de $16.000 van de stille groep.

## 3. Aanbevelingen, gerangschikt

Volgorde: grootste effect op klachten en mailvolume per eenheid omzetrisico eerst.

### 1. Geen campagnes meer naar de volledige lijst of "US Subscribers"; standaard naar een engaged-segment plus nieuwe aanmelders

**Waarom.** 16 van de 18 brede verzendingen sinds 1 augustus vielen na 4 september, precies toen de giveaway-instroom begon (laatste: Email List op 6 okt, US Subscribers op 16 okt). Daardoor krijgen giveaway-aanmelders 10,1 campagnemails in hun eerste 30 dagen, 50 procent meer dan de kortingspop-up in augustus.

**Wat in Klaviyo.**
- Standaardpubliek voor elke campagne: bestaande segmenten "EB [DG] Engaged 90 Days" (`TMaWCL`) of "v5 · Engaged 90 Days · US" (`VNX8N9`) plus een nieuw segment **"Nieuw 0 tot 14 dagen"**: Subscribed to List `Uw8eZG` minstens 1 keer in de laatste 14 dagen, kan e-mailmarketing ontvangen.
- Email List `Uw8eZG` en US Subscribers `VJkN42` alleen nog als publiek bij maximaal 4 grote momenten per jaar (BFCM-start, Kerst-cutoff), altijd met Smart Sending aan en de gewone uitsluitingen (`VSnBnJ`, `W3q7Zy`, `W4vNzF`, `XTpfNG`, `UfyDPs`).
- Smart Sending standaard aan (7 van de 18 brede verzendingen hadden hem uit).

**Omzetrisico.** Laag. De mensen buiten "engaged 90 dagen" en buiten "nieuw 14 dagen" leveren via campagnes weinig geattribueerde omzet. Meten: voor/na per campagne omzet per ontvanger, spam per 1.000 en uitschrijving per 1.000; omzet per week uit campagnes.

**API of UI.** Segment aanmaken: API (POST /api/segments) of UI. Publiek van concept-campagnes zetten: API (PATCH campaign audiences) of UI. Werkafspraak met het campagnebureau (HS/EB-campagnes): UI en afspraak, geen API.

**Verwacht effect.** Campagnemails aan aanmelders van 15 tot 90 dagen zonder klik: min 40 tot 60 procent. Uitschrijving in 30 dagen van de giveaway: van 19 naar circa 15 tot 16 procent (het niveau van de kortingspop-up in augustus met minder brede sends). Spamklachten account-breed: min 20 tot 30 procent (aanname: klachten volgen het volume aan stille ontvangers).

### 2. Engagement-poort na 14 dagen voor pop-up-aanmelders (giveaway eerst)

**Wat.** Wie via de pop-up binnenkomt en in 14 dagen niet klikt, niet koopt en de site niet bezoekt, krijgt nog maar 1 campagne per week (de beste van de week) tot hij een signaal geeft. Welcome en abandonment-flows lopen gewoon door.

**Wat in Klaviyo.**
- Nieuw segment **"Pop-up · stil na 14 d"**: (`$source` equals "Alia sign-up" OR `alia_popup_name` is set) AND Subscribed to List `Uw8eZG` at least once in the last 60 days AND zero times in the last 14 days AND Clicked Email (Bot Click is false) zero times in the last 60 days AND Placed Order zero times in the last 60 days AND Active on Site (`UdCdLD`) zero times in the last 14 days.
- Dit segment uitsluiten bij alle campagnes behalve de ene weekcampagne.
- Holdout: in de welcome-flow T4a5Mk bij de start een Random Sample-split (90/10) die `gate_test` = `poort` of `controle` zet; segment alleen voor `poort`. Zo is het omzeteffect meetbaar.

**Omzetrisico.** De stille groep levert in dag 14 tot 30 $1,06 per profiel via alle kanalen. Bij 3 naar 1 campagne per week verwachten we hooguit 20 tot 35 procent daarvan te missen (veel van die omzet komt niet via e-mail): **$3.000 tot $5.500 per maand** als bovengrens bij 18.500 aanmelders. Daartegenover: circa 70.000 minder campagnemails per maand, circa 150 tot 200 minder uitschrijvingen en circa 50 minder spamklachten per maand (op basis van 289 uitschrijvingen en 19 klachten per 6.400 stille profielen in 16 dagen, gehalveerd).

**Meten.** Poort tegen controle na 30 en 60 dagen: omzet per aanmelder (alle kanalen), uitschrijving, spam per 1.000, aandeel dat alsnog klikt. Stop als de poortgroep meer dan $1 per aanmelder achterblijft in 60 dagen.

**API of UI.** Segment: API of UI. Random Sample-split en property zetten in de flow: UI (flow-bewerking via de API is beperkt en riskant in een live flow). Campagne-uitsluitingen: API voor concepten of UI.

**Verwacht effect.** Uitschrijving dag 14 tot 30 voor de stille groep van 4,5 naar circa 2 tot 2,5 procent, spam van 0,30 naar circa 0,12 tot 0,15 procent.

### 3. Snellere sunset voor pop-up-aanmelders: 60 dagen in plaats van 120

**Wat.** De huidige v4 · Sunset (`TbYQmX`) start pas na 120 dagen zonder klik (segment `WuHSm6`). Voeg een tweede ingang toe voor pop-up-aanmelders: na 60 dagen zonder menselijke klik, order of sitebezoek krijgen ze S1 en S2 ("Should we keep writing to you?"). Wie klikt blijft (`sunset_status = kept`), de rest wordt gesuppressed. 30 tot 45 dagen is te vroeg: in dag 30 tot 60 koopt de stille groep nog 0,44 procent, $0,96 per profiel, ongeveer evenveel als in de 30 dagen ervoor.

**Wat in Klaviyo.** Nieuw segment **"v4 · Sunset · pop-up 60d"**: kan e-mailmarketing ontvangen AND (`$source` equals "Alia sign-up" OR `alia_popup_name` is set) AND profiel aangemaakt meer dan 60 dagen geleden AND Clicked Email (Bot Click false) zero times in the last 60 days AND Active on Site zero times in the last 60 days AND Placed Order zero times over all time AND Received Email at least 8 times in the last 60 days. Een tweede trigger kan een flow niet hebben: kloon `TbYQmX` als "v4 · Sunset · pop-up" met dit segment als trigger, zelfde S1 en S2, zelfde `sunset_status`-logica.

**Omzetrisico.** Uit het januari-tot-juli-cohort: na 60 dagen zonder klik of order nog $0,85 per profiel in de 30 dagen daarna via alle kanalen, en een deel daarvan blijft ook zonder mail. Met de 10 procent controle uit punt 2 meetbaar.

**Meten.** Aandeel kept na S2, account-brede spam- en bounceratio, omzet per aanmelder van poort- tegen controlegroep op dag 90.

**API of UI.** Segment: API of UI. Flow klonen en trigger zetten: UI (of API create-flow met de definitie van `TbYQmX`, daarna in de UI controleren). Suppressie blijft wekelijks na akkoord.

**Verwacht effect.** Na 60 dagen valt circa 75 procent van de giveaway-aanmelders die niets deden uit de campagnestroom: bij 18.500 per maand circa 11.000 profielen minder per maand die verder 3 mails per week krijgen, dus op termijn honderdduizenden mails per maand minder aan niet-klikkers.

### 4. Eigen welkomstak voor giveaway-aanmelders

**Wat.** Giveaway-aanmelders hebben geen code gekregen en kwamen voor "kans op terugbetaling van je order". Geef ze in de welcome eerst duidelijkheid en een keuze, en pas dan verkoop.
- W1 (bestaand, DECISIONS 7 okt): bevestigt de deelname in één regel en verkoopt; voeg één regel verwachting toe ("Expect 2 to 3 emails a week from Benjamin: recipes, care tips and our best deals") en de trekkingsdatum.
- W2: één-klikvraag "What brings you here?" (pan, set, gift, just looking) die `shopping_for` zet, plus keuze "weekly digest only" die `email_frequency = weekly` zet. Wie weekly kiest valt in de engagement-poort-uitsluiting van punt 2.
- Kookplaatvraag als in `research/lijst/03-voorstel.md` §1.

**Wat in Klaviyo.** In `T4a5Mk` een conditional split direct na de trigger: `alia_popup_name` is in [Card Game, Order Refund, Scratch Off, 0 Seconds, 8 Seconds or 25% Scroll, New Heading Copy, Giveaway] AND `alia_offer` is not set: JA naar de giveaway-tak, NEE naar de bestaande reeks. Links in W2 zetten profieleigenschappen via een voorkeurenpagina of link-tracking.

**Omzetrisico.** Klein, mits W1 blijft verkopen (de 24-uursaankoop is 9 tot 10 procent en komt vooral uit de pop-up-sessie). Meten: uitschrijving per mail W1 tot W4 per tak (nu circa 1 tot 2 procent per mail), klik per mail, conversie dag 1 tot 30.

**API of UI.** Splits en nieuwe mails in een live flow: UI. Templates zelf kunnen via de API, met de vaste header en footer uit `klaviyo/templates/partials/`.

**Verwacht effect.** Aanname: uitschrijving per welcome-mail in de giveaway-tak van 1 tot 2 procent naar 0,8 tot 1,2 procent; 5 tot 15 procent kiest weekly in plaats van uit te schrijven. Onzeker: nog niet getest.

### 5. Pop-up: verwachting en adresvalidatie (Alia, niet Klaviyo)

**Wat.**
- Copy in Alia Card Game: onder de giveaway-belofte één regel over wat ze krijgen en hoe vaak ("Enter to win your order back. You'll also get our recipes and best deals, 2 to 3 emails a week."). Pop-up blijft de giveaway (DECISIONS 7 okt).
- Real-time e-mailvalidatie in Alia (syntaxis, domein, MX, typo-suggestie "did you mean gmail.com?") als Alia dat ondersteunt. Hard bounce is 1,4 procent van alle giveaway-aanmelders in 30 dagen (circa 260 per maand), bijna allemaal "Invalid Address".
- **Geen double opt-in nu.** Zonder bot- of nepprobleem kost double opt-in typisch 20 tot 40 procent van de aanmelders, inclusief een deel van de 9 procent dat binnen 24 uur koopt, terwijl punt 1 tot 3 hetzelfde klachtprobleem goedkoper oplossen.
- Captcha: niet nodig (zie punt 6).

**Wat in Klaviyo.** Niets; dit staat in Alia. Alle 35 Klaviyo-formulieren staan op draft. Wel: de route "giveaway via Shopify-sync" (`$source` -50 met Alia-gegevens, de zwakste subgroep) bij Alia navragen: zet Alia de klant in Shopify met Accepts Marketing zonder dat de bezoeker de e-mailcheckbox zag?

**Omzetrisico.** Copy: klein, mogelijk 5 tot 10 procent minder aanmeldingen van mensen die geen mail willen (dat zijn precies de latere uitschrijvers). Meten in Alia: aanmeldratio per variant; in Klaviyo: uitschrijving in 14 dagen per variant (de tabel hierboven als nulmeting).

**API of UI.** Alia-UI. Klaviyo is hier niet de knop.

### 6. Nep- en botaanmeldingen opschonen: nu niet nodig, wel bewaken

**Bevinding.** 0 van 21.491 giveaway-aanmelders op een wegwerpdomein (lijst van 50 bekende domeinen), 1 op een typodomein, maximaal 5 aanmeldingen in één minuut, geen minuut met 10 of meer. Domeinmix gelijk aan de kortingspop-up (52 procent gmail.com, 12 procent yahoo.com, 8 procent hotmail.com). Geen aanwijzing voor bots.

**Wel doen.** Een regel in het dagelijkse rapport: aanmeldingen per uur uit Alia en aandeel hard bounce in de eerste 7 dagen per variant. Drempel: meer dan 30 aanmeldingen per minuut of hard bounce boven 3 procent in een week, dan onderzoeken.

**API of UI.** Volledig via de API (events lezen); niets te wijzigen.

## 4. Samenvatting voor Floris

| Nr | Maatregel | Waar | API of UI | Verwacht effect | Omzetrisico |
|---|---|---|---|---|---|
| 1 | Campagnes naar engaged 90 d plus nieuw 14 d, niet naar volledige lijst | Klaviyo campagnes | segment API of UI, afspraak bureau UI | min 20 tot 30% spamklachten, uitschrijving giveaway 30 d van 19% naar 15 tot 16% | laag |
| 2 | Poort na 14 d: stille pop-up-aanmelders 1 campagne per week, 10% controle | segment, T4a5Mk | segment API, split UI | circa 70.000 mails, 150 tot 200 uitschrijvingen en 50 klachten minder per maand | tot $3.000 tot $5.500 per maand (bovengrens, alle kanalen) |
| 3 | Sunset na 60 d voor pop-up-aanmelders | kloon van TbYQmX | segment API, flow UI | circa 11.000 stille profielen per maand uit de campagnestroom | klein, meetbaar via controle |
| 4 | Welkomstak giveaway: verwachting en frequentiekeuze | T4a5Mk | UI (templates API) | uitschrijving per welcome-mail min 30 tot 40% (aanname) | klein |
| 5 | Pop-up-copy met frequentie, adresvalidatie, geen double opt-in | Alia | Alia-UI | minder late uitschrijvers, min circa 260 hard bounces per maand | klein |
| 6 | Bots bewaken, niet opschonen | dagelijks rapport | API | geen | geen |

## 5. Open punten

- 60-dagenbeeld giveaway: herhalen vanaf 30 oktober (Order Refund) en 20 november (Card Game).
- Alia: wat zet de Shopify-route (Accepts Marketing), welke validatie is mogelijk, en de aanmeldratio per variant inclusief bezoekers die de pop-up sluiten.
- Welk deel van de omzet van stille aanmelders door e-mail komt: alleen de holdout uit punt 2 beantwoordt dat.
