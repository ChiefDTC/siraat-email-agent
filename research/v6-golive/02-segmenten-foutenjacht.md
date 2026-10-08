# 02 · Segmenten en flowfilters: foutenjacht (red team)

Datum: 8 oktober 2026, 19:20 tot 19:45 UTC. Alleen GET op de Klaviyo-API (revision 2025-10-15). Niets geschreven in Klaviyo, niets gecommit.
Vergeleken: de live definities van de 13 v4-flows (alle Draft) en segmenten WuHSm6 en YxfuJT tegen `exports/live/flows/*.json`, `OVERZICHT.md`, `GO-LIVE.md`, `research/v5/08-integratie.md`, `DECISIONS.md` en `scripts/build_flows.py`.

Ernst: **BLOKKEREND** = niet live zetten zonder fix · **BELANGRIJK** = fout bij echte klanten, vóór of direct na livegang oplossen · **KLEIN** = randgeval of meetfout.

---

## Fouten

### 1. BLOKKEREND · Browse: klik-split op B1 kan nooit waar zijn (Klaviyo heeft de A/B-berichten hernoemd)

- **Scenario**: klant bekijkt een pan, krijgt B1 (A/B T05a), klikt op B1. Twee dagen later krijgt hij toch **B2-NOTCLICKED** ("Skeptical? So were they."). Niemand krijgt ooit B2-CLICKED of de code-mail CODE · B2-CLICKED · pan. T02 in browse meet niets.
- **Bewijs**: flow WdRz5k, split `119850697`: `Clicked Email (W247h8) where Campaign Name contains "B1 · T05a" > 0 since flow start`. De A/B-actie `119850693` heeft live als berichtnamen: main `B1`, variaties `B1 Test #1 October 08, 2026 Variation A` (YyFeR4) en `... Variation B` (UkNrdt). Bedoeld was `B1 · T05a-A` / `B1 · T05a-B` (`exports/live/flows/browse.json`). "Campaign Name" op Received/Clicked Email is de berichtnaam (gecontroleerd op live events, bv. `"Campaign Name": "Copy of Post Purchase Flow | IT'S ON ITS WAY"` met `$flow: RL3TU6`).
- **Zelfde oorzaak, KLEIN**: welcome-variaties heten `W1 Test #1 October 08, 2026 Variation A/B` in plaats van `W1 · T04-A/B` (alleen rapportage).
- **Fix** (UI, 2 minuten): in WdRz5k de twee variaties hernoemen naar `B1 · T05a-A` en `B1 · T05a-B` (en in T4a5Mk naar `W1 · T04-A/B`). Of de split wijzigen naar `Clicked Email where $flow equals WdRz5k AND Campaign Name contains "B1 Test #1"`. Na de fix met een testprofiel klikken en de split nalopen.

### 2. BLOKKEREND (voor groep A) · T2SmtR (Failure to launch) heeft de filter uit GO-LIVE stap 8 nog niet

- **Scenario**: nieuwe inschrijver komt in het v4-pad van T4a5Mk, krijgt W1 t/m W5 (dag 0 tot ~11) en daarna vanaf dag 30 nog tien FTL-mails in tien dagen uit de oude flow T2SmtR. T01 (oud tegen nieuw) is vervuild, en de extra Received Emails duwen niet-klikkers sneller richting sunset.
- **Bewijs**: T2SmtR (live, trigger lijst Uw8eZG): flowfilter `Placed Order = 0 since flow start`, na 30 dagen alleen split `Placed Order = 0 in the last 30 days`. Geen voorwaarde op "Old · Welcome".
- **Fix**: in T2SmtR, in de bestaande split na 30 dagen, de voorwaarde toevoegen `Received Email where Campaign Name contains "Old · Welcome" at least once in the last 60 days` (zoals GO-LIVE stap 8). Niet als flowfilter.

### 3. BELANGRIJK · Sunset WuHSm6 negeert echte opens: lezers zonder klik krijgen "last email"

- **Scenario**: abonnee leest elke week de nieuwsbrief in Gmail (echte opens), klikt nooit, bezoekt de site niet. Hij komt in WuHSm6, krijgt S1 en S2 ("Last email from me"). Omdat hij volgens het bureausegment `HS // Engaged 90 Days` (VKxqyA, telt `Opened Email where machine_open = false`) wél engaged is, blijft hij daarna campagnes krijgen. Belofte gebroken, en we jagen lezers weg.
- **Bewijs**: steekproef 20 leden van WuHSm6: 2 van 20 hebben tientallen opens met `machine_open = false` tot 6 en 7 oktober (profielen 01KREM4HGDPHRVJM46Y90NWXS7: 46, 01KREMBHWMWKZ4GGS2XP0ZW20N: 29). Grofweg 10% van 75.425 = ~7.500 echte lezers. Oud sunsetsegment XY4NVp (17.394) telt opens wel mee; v4 is 4,3 keer zo groot.
- **Fix**: groep toevoegen aan WuHSm6: `Opened Email where machine_open equals false, count equals 0, in the last 90 days` (metric WyrTym). Apple MPP-opens (machine_open = true) blijven dan buiten beschouwing, zoals bedoeld in plan 3.16. Daarna profile_count opnieuw bekijken.

### 4. BELANGRIJK · Sunset-backlog: de 75.425 huidige leden komen nooit in de flow, en "suppressed" bestaat niet

- **Scenario A**: TbYQmX gaat live. Een segment-trigger reageert alleen op profielen die ná livegang het segment binnenkomen. De 75.425 die er nu al in zitten krijgen nooit S1/S2, zolang ze niet eruit en er weer in gaan. Doet iemand in de UI "add existing profiles", dan gaan er in één keer 75k S1-mails uit (piek in klachten en bounces).
- **Scenario B**: wie S2 krijgt en niet klikt, blijft gewoon in WuHSm6 en op de lijst. Er is geen segment `v4 · Sunset · suppressed` (GET /api/segments, 59 segmenten: alleen WuHSm6, YxfuJT en het oude XY4NVp). Herinstap na 180 dagen geeft dan opnieuw S1/S2.
- **Fix**: (a) bewust kiezen: backlog in porties van max. 5.000 per dag toevoegen (UI), of het oude S7V4a7 de bestaande groep laten afhandelen en v4 alleen voor nieuwe instroom. (b) Segment `v4 · Sunset · suppressed` aanmaken zoals GO-LIVE stap 3 beschrijft (in WuHSm6, Received Email Campaign Name contains "SUNSET · S2" ≥1 in 60 d en 0 in 3 d) en de wekelijkse bulk-suppress inplannen vóór de eerste S2 (5 dagen na livegang).

### 5. BELANGRIJK · Browse stuurt "10% off" naar klanten die net gekocht hebben

- **Scenario**: klant koopt de Pan Pro Standard, kijkt de volgende dag op de productpagina naar de verzorging. Browse start (geen kooper-uitsluiting), na 1 uur komt B1 "Get this pan with 10% off", twee dagen later B2. Tegelijk loopt post-purchase.
- **Bewijs**: WdRz5k profielfilter: alleen `Added to Cart = 0`, `Checkout Started = 0`, `Placed Order = 0` **since flow start**, plus Received Email van cart, checkout en welcome in 7 dagen. Geen post-purchase (X3ySuU) en geen "Placed Order in de laatste N dagen". Meting: van 50 kopers (29 en 30 september) hadden er 6 (12%) een Viewed Product binnen 7 dagen na de order. Bij ~180 orders per dag zijn dat ~20 foute browse-mails per dag.
- **Fix**: aan het profielfilter van WdRz5k toevoegen: `Placed Order count equals 0 in the last 30 days` en `Received Email where $flow equals X3ySuU count equals 0 in the last 7 days`. Zelfde overweging voor cart TZG9Mx (`Placed Order = 0 in the last 3 days`), daar is het minder dringend.

### 6. BELANGRIJK · Checkout: 14,5% van de checkouts krijgt geen C3

- **Scenario**: klant zet een Deep Pan Pro, Wok, Crêpe Pan, Roasting Pan of Pizza Steel in de checkout (zonder Pan Pro of set), of een Pan Pro met totaal ≥ $300 zonder grote set. C3-S vereist een grote set, C3-P een Pan Pro/starter **en** $value < 300, C3-ACC vereist **geen** kookgerei. Hij valt overal buiten: C1, C2, dan 4 dagen niets, dan C4.
- **Bewijs**: QUBUQV acties `119850603` (C3-S), `119850606` (C3-P), `119850613` (C3-ACC). Op de laatste 200 Checkout Started-events: C3-P 76, C3-ACC 54, C3-S 41, **geen C3: 29** (Deep Pan 7, Roasting 4, Crêpe 4, Wok 4, Pan Pro + Wok ≥ $300 2, enz.). `$value` is in USD (ook bij CH/AU/UK/CA-orders `$currency_code: USD`), dus de drempel zelf klopt.
- **Fix**: C3-P verruimen naar `Items contains-any PANPRO+VORM+STARTER+["Titanium Hammered Roasting Pan","Titanium Hammered Pizza Steel"]` en de `$value < 300`-voorwaarde vervangen door `Items contains-any GROOT_SET = 0` (die staat er al). Of een vierde verzendfilter op C3-P als vangnet: `KOOK > 0 AND GROOT_SET = 0` zonder waardegrens. In `build_flows.py` en in de live flow gelijk houden.

### 7. BELANGRIJK · Dubbele post-purchase met oude flows die live blijven

- **Scenario**: koper van een pan krijgt binnen drie weken: YyaMjx "Your E-Guide Is Ready" (3 min), TSUnLs (3 mails, elke order met Mystery Gift), v4 P1 (1 uur), YcXbHx Pan Education (6 live mails vanaf "In Transit"), v4 P2 én YcXbHx "The #1 mistake that makes titanium stick" (zelfde onderwerp als v4 P2 "The mistake that makes titanium stick"), WvRupU Mystery Gift Reveal (4 mails, incl. "Alright, here's the offer", start op elke order want elke order bevat Mystery Gift), XzHrez review (+14 d), v4 P3 met code (dag 20). Ongeveer 17 mails in 21 dagen, waarvan twee met dezelfde boodschap.
- **Bewijs**: live flows YcXbHx (trigger VjA7Qr "Postflows - 2. Shipment In Transit", laatste event vandaag), WvRupU (trigger XT7f8Z Ordered Product, ProductID 15675410415956), TSUnLs (Placed Order met Mystery Gift), YyaMjx. GO-LIVE stap 9 laat ze alle vier "ongewijzigd live". In 200 recente orders zit Mystery Gift in 182.
- **Fix**: minimaal YcXbHx Email 2 (de "mistake"-mail) op Draft of de hele Pan Education op Draft bij groep B (v4 P1/P2/P2-SAFE dekt het). WvRupU: verzendfilter `Received Email where $flow equals X3ySuU = 0 in the last 2 days` op elke mail, of de offer-mail na v4 P3 plannen.

### 8. BELANGRIJK · Welcome: 27% van de nieuwe inschrijvers heeft geen land, en valt in W4-INT

- **Scenario**: Amerikaanse inschrijver via Alia zonder locatie krijgt W4-INT in plaats van W4-US (geen US-prijzen en -bundels).
- **Bewijs**: T4a5Mk split `119850671`: `location['country'] equals "United States" OR equals "US"`. Laatste 100 leden van Uw8eZG: United States 45, **leeg 27**, Canada 7, UK 6, AU 4, rest 11. Van de 27 lege heeft niemand `country_code`. Een eigen profielveld `Country` bestaat bij geen enkel gecontroleerd profiel (13 kopers en leden). 62% van de bekende landen is US, dus ~17 van de 27 lege zijn waarschijnlijk Amerikanen.
- **Fix**: kies bewust. Optie 1: tweede split vóór W4: `location['country'] is set` → huidige landsplit; niet gezet → W4-INT (dat is nu al marktveilig) maar rapporteer het als aparte groep. Optie 2: onbekend naar W4-US laten gaan als US-prijzen in de template achter `{% if %}` staan. In beide gevallen: in de template-preview een profiel zonder land testen.

### 9. BELANGRIJK · Welcome W1 en checkout C1 vallen binnen 10 minuten samen

- **Scenario**: bezoeker schrijft zich in bij de checkout (Shopify, `$source -50`) of via Alia en start een checkout zonder af te ronden. W1 (20 min, met HI10) en C1 (30 min) komen 10 minuten na elkaar. De welcome-filter kijkt alleen of er al een checkoutmail **ontvangen** is in de laatste dag; op minuut 20 is C1 er nog niet.
- **Bewijs**: T4a5Mk standaard verzendfilter: `Received Email $flow QUBUQV = 0 in the last 1 day` en idem TZG9Mx. QUBUQV C1 na 30 minuten, geen welcome-uitsluiting.
- **Fix**: welcome-standaardfilter uitbreiden met `Checkout Started = 0 in the last 1 day` en `Added to Cart = 0 in the last 1 day` (dan wacht W1 niet, maar valt hij weg) of beter: een split na de 20 minuten "Checkout Started > 0 since flow start → wacht 2 dagen" vóór W1.

### 10. KLEIN · Post-purchase: W0 en P1 binnen 40 minuten voor checkout-inschrijvers

- **Scenario**: klant vinkt marketing aan in de checkout, komt via de order in Uw8eZG (sample: lid en koper 01M4EF0SADFT0T1FEVZF03CH87, beide 19:14). Komt de lijstinschrijving ná de order, dan krijgt hij W0 "Thank you. Now the first egg." (20 min) en P1 "Good call. Here's what's coming." (1 uur).
- **Fix**: in T4a5Mk split `119850653` (Placed Order > 0 all time) een eerste tak toevoegen: `Placed Order > 0 in the last 2 days` → einde.

### 11. KLEIN · Post-purchase P3: venster van 21 dagen is krap

- **Scenario**: order om 23:30 (profieltijd). 1 uur → 00:30 dag 1; 16 dagen tot 09:00 → dag 17 09:00; 4 dagen tot 09:00 → dag 21 09:00 = 21 dagen 9,5 uur na de order. `Placed Order ... in the last 21 days` ziet de order dan niet meer en de klant valt in P3-NEXT · eigenaar in plaats van P3-SET/PAN/NEXT-deksel. Bij tijdzoneverschil tussen profiel en server kan dit ook eerder op de avond gebeuren.
- **Bewijs**: X3ySuU acties 119850553 (16 d tot 09:00), 119850555 (4 d tot 09:00), alle P3-filters `in-the-last 21 day`.
- **Fix**: in alle P3-filters 21 vervangen door 25 dagen (P2-SAFE 17 → 18 mag ook). In `build_flows.py` gelijk trekken.

### 12. KLEIN · Sunset S1 heeft geen verzendfilter

- **Scenario**: profiel komt 's nachts in WuHSm6 (120 dagen-grens), koopt die ochtend om 08:00 of bezoekt de site, en krijgt om 09:00 toch S1 "Should we keep writing to you?".
- **Bewijs**: TbYQmX actie 119850754 (S1): `additional_filters: null`. S2 heeft wel Clicked (bot false) / Active on Site / Placed Order = 0 since flow start.
- **Fix**: dezelfde drie voorwaarden als S2 op S1 zetten.

### 13. KLEIN · Sunset raakt opnieuw wie al door de oude sunset ging, en heropt-ins na lange tijd

- **Scenario A**: 5 van 20 gesamplede WuHSm6-leden hebben al `Unengaged = true` (gezet door het oude S7V4a7). Zij krijgen S1/S2 een tweede keer.
- **Scenario B**: oud profiel (aangemaakt > 120 dagen geleden, bv. koper uit 2025) schrijft zich nu opnieuw in. Na de welcome en 30 dagen (flowfilter) kan hij in sunset vallen als hij alleen leest en de site niet bezoekt. De voorwaarde `created at least 120 days ago` meet de profielleeftijd, niet de inschrijfdatum.
- **Fix**: A: flowfilter op TbYQmX `properties['Unengaged'] is not true` (of bewust accepteren). B: in WuHSm6 een groep `Is in list Uw8eZG, added more than 120 days ago` (lidmaatschap met datum) in plaats van of naast `created`.

### 14. KLEIN · Browse en cart starten ook op gratis producten

- **Scenario**: bezoeker bekijkt de pagina van "PFAS Water Purifier Giveaway", "The Green Clean E-Guide" of "E-Gift Card" en krijgt B1-ACC "Looked twice? Here's the detail.".
- **Bewijs**: WdRz5k trigger Viewed Product zonder trigger_filter (cart TZG9Mx heeft wel `Price > 0` en de gift-uitsluitingen). In 200 recente Viewed Product-events: Giveaway, E-Guide en E-Gift Card elk 1 keer.
- **Fix**: triggerfilter op WdRz5k: `Name not-contains Giveaway`, `not-contains E-Guide`, `not-contains E-Book`, `not-contains Mystery Gift`.

### 15. KLEIN · Winback zonder refundfilter

- **Scenario**: klant stuurt de pan terug (Refunded Order), krijgt op dag 45 toch "How's your pan doing?" en op dag 75 een code.
- **Bewijs**: UyFc78 heeft geen profielfilter; R1/R2-filters bevatten geen Refunded Order (post-purchase, VIP en anniversary wel).
- **Fix**: op elke UyFc78-mail `Refunded Order (Xg6cwn) = 0 since flow start`.

### 16. KLEIN · Codes vlak na elkaar (bewust, maar weet het)

- VIP V1 (15%, 14 dagen) kan komen terwijl de P3-code (10%, 14 dagen) nog geldig is; de cooldown-split slaat alleen over als de klant een code **gebruikte** (Discount Codes niet leeg in 45 dagen). Past bij het besluit van 8 okt ("VIP krijgt 15%, ook vlak na een eerdere code als die niet gebruikt is").
- R2-VIP (15%, dag 75) komt 45 dagen na V1, buiten de 30-dagen-cooldown.
- Welcome HI10 en C4/K3-codes: W1 heet niet "CODE · ...", dus de cooldown ziet HI10 niet. Wie W1 kreeg, krijgt in de 50%-arm toch de unieke C4/K3-code.
- De oude flows (Old · Cart 2/3, Old · Welcome 3/8, oude winback UEfh4h) delen codes zonder "CODE ·"-naam; de cooldown ziet ze niet. Verdwijnt vanzelf na groep A/B.

### 17. KLEIN · Livegang-volgorde en A/B-status

- Sunset · kept (Wzz6xC) is segment-getriggerd: klikken op S1 vóór Wzz6xC live staat, leveren geen S3/S4 op. Wzz6xC uiterlijk tegelijk met TbYQmX live zetten.
- De A/B-acties in T4a5Mk en WdRz5k staan op `experiment_status: draft`, `started: null`. Bij livegang in de UI controleren dat de test echt start (anders gaat alles naar één bericht).
- Oude sunset S7V4a7 (segment XY4NVp, 17.394) en v4 TbYQmX nooit tegelijk live: vier afscheidsmails.

---

## Gecontroleerd en in orde

| Onderwerp | Wat gecontroleerd | Uitkomst |
|---|---|---|
| Trigger-metrics actief | Laatste event per metric (GET /api/events, sort -datetime) | Alle 13 vandaag: Checkout Started 19:18, Added to Cart 19:21, Viewed Product 19:20, Placed Order 19:14, Delivered Shipment 19:19, Active on Site 19:20, Received/Clicked/Opened Email 19:17 tot 19:21, Refunded 16:23, Opened Ticket 19:21, Fulfilled 18:56, Triple Pixel 18:40. Ook Postflows In Transit/Delivered en Ordered Product actief. |
| Metric-ID's | Alle metric_id's in de 13 flows tegen /api/metrics | Overeenkomstig OVERZICHT (RSNxYV = Shopify Placed Order, niet Ordered Product; UdCdLD = Active on Site, XNtYMB = Viewed Product; W247h8 = Clicked, WyrTym = Opened). Geen verwisseling gevonden. |
| `$flow`-filters | Formaat op live events (`"$flow": "RL3TU6"`) | Flow-ID als string, dus `$flow equals "TbYQmX"` enz. werkt. Alle verwezen ID's (X3ySuU, QUBUQV, TZG9Mx, T4a5Mk, WdRz5k, VTkxFL, UyFc78, TbYQmX) bestaan. |
| CODE-cooldown | "Campaign Name" op Received Email = berichtnaam | Klopt; alle codemails heten "CODE · ...", geen nocode-mail heet zo. |
| Bot Click | Aanwezig op Clicked Email in juni, augustus en september (60 events) | Altijd aanwezig (20% true). Filter `Bot Click equals false` telt dus menselijke klikken, ook 120 dagen terug. |
| WuHSm6 operatoren | Received Email `greater-than 7` (= minstens 8), Active on Site / Placed Order (180 d) / Clicked (bot false) `equals 0`, `created at-least 120 day`, consent email | Zoals bedoeld (08-integratie sectie 4); `created` werd door Klaviyo geaccepteerd als `at-least` (niet `not-in-the-last`). Gesamplede leden: aangemaakt 12 mei, dus > 120 dagen. SMS-only valt buiten (email-consent). Recente kopers (180 d) en recente klikkers vallen buiten. |
| YxfuJT (kept) | Definitie, trigger Wzz6xC | Clicked Email, `$flow = TbYQmX`, `Bot Click = false`, > 0 in 7 dagen. Wzz6xC triggert op dit segment; flowfilter alleen "niet in flow 365 d", geen eis "nog in segment". Uit het segment vallen na 7 dagen haalt niemand uit de flow; tweede klik geeft geen tweede instap. Werkt. |
| VIP-operator | `Discount Codes length-greater-than 0` | Door Klaviyo geaccepteerd; Discount Codes is op live events een lijst (180 van 200 leeg). |
| Currency | `$value` en `$currency_code` op Placed Order/Checkout Started | Altijd USD, ook bij CH/AU/UK/CA. Drempels $300 consistent. |
| Productnamen | 200 Checkout Started + 200 Placed Order + 200 Viewed Product + 200 Added to Cart tegen de titellijsten | Alle kookgerei-titels staan in KOOK/SET; onbekend zijn alleen accessoires en gifts (correct ACC). Kookwoord-splits (cart/browse) sorteren alle 2026-titels goed. |
| Cart-trigger | Gifts uitgesloten | Price > 0 plus not-contains Mystery Gift / E-Book / Free Shipping / Giveaway: de vier automatische gifts komen niet binnen. |
| Abandonment na order | Checkout, cart, site | Alle drie stoppen op `Placed Order = 0 since flow start` op elke mail; cart stopt ook bij Checkout Started; checkout sluit 7 dagen na een post-purchase-mail uit; site sluit 30 dagen kopers uit. (Browse niet: fout 5.) |
| Bestaande klanten | Welcome v4-pad, cart K2, checkout C2/C3-ACC | Kopers krijgen W0 i.p.v. W1-W5; K2-NEW/C2/C3-ACC alleen bij 0 orders all time. |
| A/B-percentages | Alle profile-sample splits | 50/50 overal (T01 bovenaan, T02 onder de cooldown), A/B-acties 0,5/0,5, geen automatische winnaar. Geen tak waar niemand in valt (behalve fout 1). |
| siraat_owned | 13 echte profielen, sync-state, sleutels | Sync liep 14:29 (98.691 profielen, 0 fouten); kopers sinds de run hebben het veld nog niet, maar xsell staat alleen in P3/R/V/N (dag 20+), dus geen probleem. Sleutels (`panpro_standard`, `deep`, `wok`, `lid_28`, `board`, `set6`) zijn gelijk aan `v5lib.XOWN`. `siraat_orders` aanwezig (bv. 3). Nachtroutine trig_01WF2aAEzd6Ekb7AeW2kVvcd staat in LOG. |
| Afzenders | from/reply-to op alle 13 flows | send@ / support@; Benjamin op W2, V2, S2, S3, S4; smart sending overal uit (zoals plan). |
| Oude live flows | GET /api/flows status live (24) | Exact de lijst uit GO-LIVE stap 9; geen onverwachte extra verkoopflow. Overlap zie fouten 2 en 7. |

## Niet kunnen controleren (alleen GET)

- Of `person.Country` als templatetag gevuld wordt (renderen vraagt een POST). Geen enkel profiel heeft een eigen eigenschap `Country`; `location.country` is er bij 73%, `country_code` bij 13%. Eén template-preview op een echt profiel blijft nodig.
- Hoe Klaviyo de A/B-variatienaam in "Campaign Name" zet: XzHrez (enige live flow met A/B) heeft nog niets verstuurd. Fout 1 blijft hoe dan ook staan, want noch `B1` noch `B1 Test #1 ...` bevat `B1 · T05a`.
