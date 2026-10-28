# A/B-tests Q4 · 05 · Herinstap van v4 · Post-purchase (X3ySuU)

Datum: 28 oktober 2026. Vraag van Floris: is 7 dagen herinstap de goede keuze, of beter een paar uur, een paar dagen of iets anders?

Alles alleen gelezen. Klaviyo (account TdtTzz, revision 2025-10-15): flowdefinities van X3ySuU, VQ93sx, YwsKcf, R22pzb, XzHrez en TvfJYU, alle Placed Order-events (RSNxYV) van 1 juli tot 28 oktober 19:20 UTC (25.185 orders, waarvan 618 van $0), `flow-values-reports` van 8 tot 28 oktober, en Received Email (YkRM4Q) voor de 114 profielen met een herhaalorder sinds de livegang (9 oktober). Aftersell: funnels en TYP-omzet. Niets gewijzigd, niets verstuurd. In dit stuk staan alleen aggregaten. Rekenwerk staat in de scratchpad (`herinstap/`, met `sim.py` als simulatie van de flowlogica).

**$0-orders** (TikTok-affiliate-samples) zijn uit alle tellingen van orders, gaten en omzet gehaald. De simulatie laat ze wel de flow in, omdat de echte flow ze ook binnenlaat (zie 1.1).

---

## 0. Samenvatting voor Floris

1. **Het gat is veel kleiner dan we dachten.** Over 90 dagen kwam 5,7% van de betaalde orders binnen 30 dagen na een vorige betaalde order. In plan R3 stond 12,7% en "~30 extra P1-REPEAT per dag". Uit de data volgt **ongeveer 5 per dag (36 per week) bij 7 dagen herinstap**. Het grootste deel van die herhaalorders valt tussen dag 7 en dag 30.
2. **Orders binnen een paar uur zijn geen gemiste P1-REPEAT.** 259 tweede orders kwamen binnen een uur (83% daarvan binnen 15 minuten). Dat zijn tweede checkouts: elke tweede order heeft een eigen checkout, er gaan opnieuw gifts mee, en een kwart heeft precies dezelfde items als de eerste order. Een Aftersell-upsell die in de originele order wordt opgenomen, zit er niet bij. Bij een tweede checkout binnen het uur krijgt de eerste P1 al de vorm P1-REPEAT, omdat Klaviyo op het moment van versturen 2 orders telt. **Een herinstap van een paar uur levert dus niets op en geeft dubbele mails.**
3. **Nieuwe bevinding: verkeerde P1 bij kopers die voor het eerst bestellen.** Kopers die voor het eerst bestellen en binnen het uur een tweede checkout doen, krijgen P1-REPEAT ("Good to see you again") in plaats van P1-FIRST. Ze missen dan de e-booklink en de tijdlijn. Dat zijn ongeveer 20 per week. Gezien bij 51 van de 56 gevallen sinds de livegang. Deze groep kocht vaak nog een keer binnen 5 dagen (15% van hen, gemiddeld $42 per order). Daardoor ziet P1-REPEAT er beter uit dan hij is.
4. **$4,31 per ontvanger is grotendeels selectie.** Het cijfer rust op 5 orders. Over 20 dagen is het $3,29 per ontvanger (8 orders op 450 ontvangers). Herhaalkopers bestellen ook zonder mail vaak opnieuw: binnen 5 dagen al voor $12 tot $30 per order, tegen $4,58 voor alle andere orders. Ik reken daarom met $0,80 tot $2,15 echte extra omzet per extra P1-REPEAT.
5. **Extra omzet bij 7 dagen: $30 tot $80 per week nu, $60 tot $310 in de BFCM-weken.** In plan R3 stond $450, en $900 tot $1.800 in BFCM. Dat was te hoog. Het effect op afmeldingen en spam is verwaarloosbaar.
6. **Advies: 7 dagen, met drie kleine aanvullingen** (sectie 5). Bij 7 dagen valt Mystery M1 nooit samen met P1. Er komt geen tweede P1 binnen een week. Er zijn ook minder dubbele P2-SAFE-mails, en die kunnen we met één filter helemaal wegnemen. Let op: de wachttijd staat op twee plekken, de herinstap van de trigger **en** het flowfilter "has not been in this flow in the last 30 days". Allebei moeten ze naar 7, anders verandert er niets.
7. **Ook belangrijk, los van de herinstap.** De trigger heeft geen filter op `$value`. Daardoor gaan de TikTok-samples de flow in: nu zo'n 137 per week, eerder 15 tot 25. Ze krijgen P1, P2-SAFE (vaak een pan) en P3 met een eigen code. Advies: triggerfilter `$value > 0`. Dat kan alleen in de UI.

---

## 1. De flowdefinitie (GET 28 okt)

### 1.1 Trigger, filters en herinstap

| Onderdeel | Live waarde |
|---|---|
| Trigger | Placed Order (RSNxYV), `trigger_filter: null`. Ook $0-orders starten de flow. |
| Profielfilter | `profile-not-in-flow` in de laatste 30 dagen |
| Herinstap | `reentry_criteria {duration 30, unit day}` |
| Smart Sending | uit op alle 26 mails |
| Status | live, alle mails live |

Volgens Klaviyo zet de nieuwe instelling voor herinstap een oud filter "has not been in flow in X days" om naar "re-entry after X days" (Klaviyo-helpcentrum via zoekresultaat, zie bronnen). Hier staan ze allebei, dus allebei aanpassen.

### 1.2 P1-FIRST tegenover P1-REPEAT

Er is geen conditional split. De twee mails staan achter elkaar na één wachttijd van 1 uur. Elke mail heeft een eigen verzendfilter:

- **P1-FIRST** `R3gbkQ` (actie 119850551): Placed Order **equals 1, over all time**.
- **P1-REPEAT** `WqxPSh` (actie 119850552): Placed Order **greater than 1, over all time**.

Het filter wordt bekeken op het moment van versturen, dus 1 uur na de order. Orders van die tussentijd tellen mee. Ook $0-orders tellen mee: een sample in het verleden maakt van een koper die voor het eerst betaalt een "repeat".

### 1.3 Na P1

| Stap | Wachttijd | Dag na order | Mail | Voorwaarde |
|---|---|---|---|---|
| 1 | 1 uur | 0 | P1-FIRST of P1-REPEAT | zie 1.2 |
| 2 | 16 dagen tot 09:00 | ~16,5 | **P2-SAFE** `TZ6TKb` | order met een P2-titel (48 titels) in 17 dagen, **geen Delivered Shipment sinds de start van de flow**, geen refund in 30 dagen |
| 3 | 4 dagen tot 09:00 | ~20,5 | split: Placed Order **equals 2** over all time, JA = einde (VIP) | |
| 3a | direct | | cooldown-split (CODE-mail in 30 dagen) en daarna T02 50/50 | |
| 3b | direct | | **P3** (12 varianten: SET, NEXT deksel, PAN, ACCESSORY kook, NEXT eigenaar, APRON, ACCESSORY acc; met code of nocode) | Placed Order **0 since flow start**, geen refund in 30 dagen, productfilters in 21 dagen |

Naast de flow lopen:

| Flow | Trigger | Herinstap | Raakt X3ySuU |
|---|---|---|---|
| P2 `VQ93sx` | Delivered Shipment, +1 dag 09:00 | 30 dagen, plus filter "geen P2-SAFE in 30 dagen" | P2 en P2-SAFE sluiten elkaar maar in één richting uit |
| Mystery `YwsKcf` | Ordered Product Mystery Gift, M1 dag 3, M2 dag 12, M3 dag 23 (M4 draft) | eenmalig | elke mail slaat over bij een X3ySuU-mail in 2 dagen. Smart Sending staat aan (16 uur) |
| Review `XzHrez` / `TvfJYU` | Delivered +14 dagen, of Fulfilled +21 dagen | eenmalig | geen; loopt nooit twee keer |
| Affiliate S1 `R22pzb` | Postflows, +3 dagen | eenmalig | geen; loopt nooit twee keer |

Gevolg: alleen X3ySuU zelf (P1, P2-SAFE, P3) kan door een kortere herinstap twee keer komen. Review, affiliate en Mystery niet.

---

## 2. Data over 90 dagen (30 juli tot 28 oktober, zonder $0)

18.452 betaalde orders van 17.302 kopers. 823 kochten 2 keer en 139 kochten 3 keer of vaker in deze periode. 547 orders van $0 zijn eruit gehaald.

### 2.1 Tijd sinds de vorige betaalde order

We kijken terug tot 1 juli. Daardoor is de groep 30 tot 90 dagen te laag: voor orders uit augustus zien we maar ongeveer 30 dagen terug.

| Gat | Orders 90 d | Per week | Aandeel | Gem. orderwaarde |
|---|---|---|---|---|
| binnen 1 uur | 259 | 20 | 1,4% | $185 |
| 1 tot 24 uur | 108 | 8 | 0,6% | $203 |
| 1 tot 3 dagen | 64 | 5 | 0,3% | $163 |
| 3 tot 7 dagen | 74 | 6 | 0,4% | $160 |
| 7 tot 30 dagen | 505 | 39 | 2,7% | $192 |
| 30 tot 90 dagen | 407 | 32 (ondergrens) | 2,2% | $207 |
| geen order eerder in de data | 17.035 | | 92,3% | $223 |

- In de laatste 60 dagen kwam 5,7% van de betaalde orders binnen 30 dagen na een vorige betaalde order. Met $0-orders erbij is het 6,1%. De 12,7% uit plan R3 komt in deze data niet terug.
- Per week schommelt het weinig: tussen 1 uur en 30 dagen 40 tot 105 orders, de piek in week 42 (Halloween-aanloop). Een trend omhoog is er niet.
- 1 tot 24 uur verder uitgesplitst: 1 tot 3 uur 34, 3 tot 6 uur 15, 6 tot 24 uur 59.

### 2.2 Add-ons en upsells binnen een paar uur

Van de 259 tweede orders binnen een uur:

- 118 binnen 5 minuten, 96 binnen 5 tot 15 minuten, 28 binnen 15 tot 30 minuten, 17 binnen 30 tot 60 minuten.
- **0** hadden dezelfde checkout als de vorige order. Elke tweede order is dus een nieuwe checkout.
- 62 (24%) hadden precies dezelfde items. Dat lijkt op dubbel afrekenen of een nieuwe poging na een betaalfout. 16 waren een deel van de eerste order. 61 waren minder dan de helft van de eerste orderwaarde: een echte add-on, vaak een deksel (45), snijplank (42) of utensils (25).
- In zo'n 80 van de tweede orders zaten opnieuw de gratis gifts (Free Shipping, Giveaway, E-Book, Mystery Gift). Dat gebeurt bij een gewone checkout, niet bij een Aftersell-upsell na aankoop.
- Bron: 235 web (online store), 22 Shop-app, 2 TikTok.
- Aftersell: één funnel actief ("Classic upsell"). De omzet van de bedankpagina (TYP) was $77 tot $1.830 op losse dagen. Volgens Aftersell (leveranciersclaim) gaat een geaccepteerde upsell na aankoop "into the original order". Een TYP-upsell kan óf samengevoegd worden, óf "as a separate order" binnenkomen. In de orderdata zie ik geen aparte Aftersell-bron. Of de TYP-instelling op "separate order" staat, moet Floris nog in Aftersell bevestigen.

Conclusie: van de snelle tweede orders is ongeveer een kwart een add-on, een kwart een dubbele order en de rest een tweede, losse checkout. Geen van deze groepen heeft een tweede bevestiging met nieuwe inhoud nodig.

### 2.3 Wat krijgen herhaalkopers nu (gezien in Received Email, 133 herhaalorders sinds 9 oktober)

| Gat | n | P1 na order 1 | P1 na order 2 |
|---|---|---|---|
| binnen 1 uur | 56 | 51 x P1-REPEAT (verkeerd bij kopers die voor het eerst bestellen), 5 geen | 0 |
| 1 tot 24 uur | 31 | 20 x P1-FIRST, 4 x P1-REPEAT, 7 geen | 0 |
| 1 tot 3 dagen | 16 | 8 x FIRST, 4 x REPEAT, 4 geen | 0 |
| 3 tot 7 dagen | 11 | 7 x FIRST, 2 x REPEAT, 2 geen | 1 |
| 7 tot 30 dagen | 19 | 15 x FIRST, 3 x REPEAT, 1 geen | 0 |

- Bij order 2 komt dus vrijwel nooit een P1. Shopify stuurt wel de orderbevestiging en de 3PL de tracking.
- P3 valt voor elke herhaalkoper weg: er is een order sinds de start van de flow.
- In de 14 dagen na de herhaalorder kreeg een herhaalkoper gemiddeld 0,44 mail uit X3ySuU, 0,68 uit andere flows en 0,93 campagne. Dat is een ondergrens, omdat de recente orders nog geen volle 14 dagen hebben. Bij de andere flows valt op dat de oude flow FREE E-GUIDE (`YyaMjx`) nog live is en hier 0,14 mail per herhaalkoper verstuurt.

---

## 3. Risico per herinstap-instelling

Simulatie van de echte flowlogica (P1-split op het verstuurmoment, P2-SAFE-kandidaat bij een P2-titel, P3 alleen zonder latere order en als het aantal orders niet 2 is). Entries van 30 juli tot 7 oktober (9,9 weken), $0-orders laten we binnen zoals de echte trigger doet. P2-SAFE-kandidaten tellen als verstuurd, omdat de bezorgevents sinds ~22 oktober bijna wegvallen (plan R1). Tot dat hersteld is, krijgt vrijwel elke pankoper P2-SAFE.

| Per week | 0 (altijd) | 1 dag | 3 dagen | **7 dagen** | 14 dagen | 30 dagen (nu) |
|---|---|---|---|---|---|---|
| Extra herhaalorders met een eigen P1-REPEAT | 75 | 47 | 42 | **36** | 21 | 0 |
| waarvan nutteloos (tweede checkout binnen 1 uur) | 20 | 0 | 0 | 0 | 0 | 0 |
| Twee P1-mails binnen 24 uur | 30 | 0 | 0 | 0 | 0 | 0 |
| Twee P1-mails binnen 1 tot 7 dagen | 10 | 11 | 6 | **0** | 0 | 0 |
| Dubbele P2-SAFE binnen 30 dagen (zonder extra filter) | 31 | 16 | 14 | **11** | 4 | 0 |
| Extra P3 (bij de 3e order of later) | 11 | 7 | 6 | **5** | 3 | 0 |
| Mystery M1 (dag 3) valt weg door P1 binnen 2 dagen | ja, bij orders op dag 1 tot 3 (~5/week) | ja (~5/week) | deels (dag 3) | **nee** | nee | nee |
| Mystery M2 (dag 12) of M3 (dag 23) valt weg | mogelijk | mogelijk | mogelijk | **~3/week** | ~2/week | nee |
| X3ySuU-mails in 14 dagen na een herhaalorder (gemiddeld, max) | 1,8 (max 10) | 1,3 (4) | 1,2 (4) | **1,1 (3)** | 0,8 (2) | 0,5 (1) |
| **Alle mails in 14 dagen** (plus ~1,6 uit andere flows en campagnes) | ~3,4 | ~2,9 | ~2,8 | **~2,7** | ~2,4 | ~2,1 |

Toelichting:
- **Twee P1-mails kort na elkaar.** Dat gebeurt alleen bij 0 dagen (twee bevestigingen binnen het uur, allebei "Good to see you again"). Bij 1 en 3 dagen krijgt een koper die voor het eerst bestelde, en na een paar dagen opnieuw bestelt, een P1-REPEAT na de P1-FIRST. Dat is te verdedigen, maar het levert weinig op.
- **P2 en review.** Die lopen niet door elkaar door de herinstap: P2 (VQ93sx) heeft zijn eigen herinstap van 30 dagen en de review is eenmalig. Het echte risico is P2-SAFE: elke run controleert "Delivered sinds de start" alleen voor zichzelf. Een tweede order kan dus een tweede P2-SAFE geven, ook na een P2 bij de eerste levering ("When your pan arrives" terwijl de pan er al is). Hetzelfde filter dat VQ93sx al heeft, lost dit op (5.2).
- **Mystery en affiliate S1.** Die zijn allebei eenmalig. Een overgeslagen Mystery-mail komt dus nooit meer. Bij 7 dagen kan M1 niet botsen. M2 of M3 vallen af en toe weg; dat was in het ontwerp al geaccepteerd ("P2 is belangrijker"). Affiliate S1 heeft geen filter op X3ySuU, alleen Smart Sending. Het volume is klein door het Postflows-gat.

---

## 4. Alternatieven voor één herinstap-instelling

| Alternatief | Werkt het? | Oordeel |
|---|---|---|
| **A. Aparte korte herhaalflow** ("v4 · Post-purchase · herhaal": trigger Placed Order met `$value > 0`; profielfilter Received Email `$flow = X3ySuU` minstens 1 keer in 30 dagen; verzendfilter Received Email `$flow = X3ySuU` 0 keer in 24 uur; eigen herinstap 7 dagen; 1 uur wachten en een kopie van P1-REPEAT; geen P2-SAFE en geen P3) | Ja. Vangt de orders vanaf ~24 uur na de vorige P1 (~47 per week). X3ySuU blijft precies zoals hij is, dus geen dubbele P2-SAFE of P3 en een schone meting. | Beste vorm op papier, maar levert maar ~11 per week meer op dan B, met een extra flow om te onderhouden. Mystery moet de nieuwe flow-ID in zijn filter krijgen. **Bouwbaar via de API als draft** (`POST /api/flows`). |
| **B. Herinstap 7 dagen plus P2-SAFE-filter** | Ja, ~36 per week. | **Advies**: 5 minuten in de UI, weinig nieuwe risico's. |
| **C. Split op "Placed Order since flow start"** | Nee, niet voor P1. Een flow kan midden in een run niet reageren op een nieuwe order. Zo'n split stuurt alleen latere stappen (P3 doet dit al). | Geen oplossing voor het gat. Wel goed als aanvulling: P2-SAFE stoppen als er sinds de start een nieuwe order met een pan is. |
| **D. Smart Sending op P1** | Werkt deels: een tweede P1 binnen 16 uur valt weg. Maar P1 valt ook weg na elke campagne in de afgelopen 16 uur, en in BFCM gaat er elke dag een campagne uit. Klaviyo: standaardvenster voor e-mail 16 uur. | Afraden voor een bevestiging. Wel aan laten op Mystery. |
| **E. Orders binnen X uur samenvoegen** (verzendfilter op P1-REPEAT: Received Email `$flow = X3ySuU` 0 keer in 24 uur) | Ja, dit is het filter dat alternatief A gebruikt. Binnen X3ySuU is het overbodig zodra de herinstap minstens 1 dag is. | Gebruiken in A. Bij 0 dagen herinstap haalt 6 uur samenvoegen nog maar de helft van de dubbele P1's binnen 24 uur weg (gesimuleerd: 30 naar 4 per week, maar 42 van de 77 orders binnen 1 tot 24 uur krijgen dan nog een tweede P1). |

### Wat zeggen de bronnen

- **Klaviyo-helpcentrum** (via zoekresultaten; help.klaviyo.com kon in deze sessie niet direct geopend worden). Er zijn drie opties: "once only", "re-enter whenever they newly qualify" en "after a set time period". Een oud filter "has not been in flow in X days" wordt "Allow re-entry after a time period (X days)". Klaviyo noemt geen vaste aanbevolen termijn voor post-purchase. [leverancier]
- **Klaviyo, post-purchase-gids.** Splits nieuwe en terugkerende kopers met "Placed Order equals 1 over all time", met JA voor kopers die voor het eerst bestellen. Klaviyo zegt er niet bij dat de order die de flow startte meetelt, of hoe dubbele checkouts gaan; dat is precies het misgrijpen uit 0.3. [leverancier]
- **Klaviyo Community** (moderator, maart 2026). De herinstap in de triggerinstellingen "is same as adding 'has not been in this flow in the last 30 days'". Een andere gebruiker (niet bevestigd) zegt dat de variant "in the last X days" bij elke stap opnieuw wordt bekeken. [community, geen officiële bron]
- **Klaviyo, Smart Sending.** Standaard 16 uur voor e-mail. Staat het uit, dan gaat de mail ook binnen het venster. [leverancier]
- **Aftersell-documentatie.** Een upsell na aankoop gaat "added to the original order". Een upsell op de bedankpagina kan samengevoegd worden of "a second order that is distinct from the original". [leverancier]
- **DTC-blogs** (topgrowthmarketing, attribuly; niet volledig te lezen in deze sessie). Ze adviseren een split bovenaan op het aantal orders, en dat het herhaalpad de merkintroductie overslaat. Over overlappende orders zeggen ze niets concreets. [bureau of leverancier, marketingcontent]

---

## 5. Omzet, afmeldingen en aanbeveling

### 5.1 Schatting per optie (zonder $0-orders)

Aannames:
- Extra omzet per extra P1-REPEAT is $0,80 tot $2,15. Dat is 25 tot 50% van de toegeschreven $3,29 tot $4,31: herhaalkopers bestellen ook zonder mail vaak opnieuw (2.3 en 0.4).
- In BFCM 2 tot 3 keer zoveel herhaalorders.
- Afmelding P1-FIRST 0,35% (13 op 3.686), P1-REPEAT 0% (0 op 450), P2-SAFE 0,49% (3 op 608). Spam P1-FIRST 0,03% (1).

| Optie | Extra P1-REPEAT per week | Extra omzet per week nu | Per week BFCM | Extra afmeldingen per week | Extra spam | Verwarring |
|---|---|---|---|---|---|---|
| 0 (altijd) | 55 nuttig + 20 dubbel | $44 tot $118 | $90 tot $350 | ~0,4 | ~0,02 | hoog: 30 dubbele P1's per week, Mystery M1 valt weg |
| 1 dag | 47 | $38 tot $101 | $75 tot $300 | ~0,25 | <0,02 | middel: P1 na 1 tot 7 dagen, Mystery M1 |
| 3 dagen | 42 | $34 tot $90 | $65 tot $270 | ~0,2 | <0,02 | laag tot middel |
| **7 dagen + P2-SAFE-filter** | **36** | **$29 tot $77** | **$60 tot $230** | **~0,1** | **~0** | **laag** |
| 14 dagen | 21 | $17 tot $45 | $35 tot $135 | <0,1 | ~0 | zeer laag |
| 30 dagen (nu) | 0 | $0 | $0 | 0 | 0 | geen; wel verkeerde P1 bij dubbele checkout |
| A. Aparte herhaalflow | ~47 | $38 tot $101 | $75 tot $300 | ~0,2 | ~0 | laag |

De bedragen liggen ver onder plan R3 ($450 per week, $900 tot $1.800 in BFCM). De oorzaak is het volume: ongeveer 5 per dag in plaats van 30 per dag. Zelfs met 100% toeschrijving van $4,31 komt optie 7 dagen niet boven ~$155 per week.

### 5.2 Aanbeveling met concrete instellingen

**Nu (UI, ~10 minuten, Floris):**

1. X3ySuU > trigger > **Re-entry criteria: after 7 days**.
2. X3ySuU > Profile filters: "has not been in this flow **in the last 30 days**" naar **7 days**, of weghalen als de UI meldt dat de herinstap het overneemt. Laat je dit staan op 30, dan verandert er niets.
3. X3ySuU > trigger filter: **`$value` greater than 0**. Dan blijven de TikTok-samples (~137 per week) eruit en houden ze geen herinstapvenster bezet. Los besluit, maar het hangt hiermee samen.

**Daarna (API kan, maar het gaat om een live flow, dus na akkoord):**

4. P2-SAFE (actie 119850554) krijgt twee verzendfilters erbij: Received Email waar Campaign Name P2-SAFE bevat, 0 keer in 30 dagen; en Received Email `$flow = VQ93sx`, 0 keer in 30 dagen. Dat haalt de ~11 dubbele P2-SAFE per week weg. Via `PATCH /api/flow-actions/119850554/` met de volledige `definition`, of in de UI.
5. Mystery M1 tot M3 hoeven niet te veranderen.

**Open, in de UI nagaan:**

6. Het misgrijpen tussen P1-FIRST en P1-REPEAT bij een tweede checkout binnen het uur (~20 per week). In de UI kijken of er een tijdoptie is als "Placed Order at least once, more than 1 day ago" (of "before"). Zo ja: P1-REPEAT = minstens 1 order ouder dan 1 dag, P1-FIRST = de rest. Zo nee: accepteren. Via de API proberen we dit niet, omdat ik de syntax niet heb kunnen testen.
7. Aftersell: bevestigen dat de TYP-upsell op "merge with original order" staat. Op "separate order" start elke upsell een nieuwe Placed Order.

**Meten** (voor/na, geen A/B): P1-REPEAT-ontvangers per dag (verwacht 20 naar 25 tot 26 per dag), dubbele P2-SAFE per week (verwacht 0), afmeldingen op P1-REPEAT (verwacht onder 0,3%), en de 5-daagse omzet per herhaalorder tegen de basislijn in 2.3 ($12 tot $30). Evaluatie op 7 december, met de BFCM-weken apart.

**Alternatief A** (aparte herhaalflow) alleen als Floris ook de orders van 1 tot 7 dagen wil hebben. Bouwen als draft via `POST /api/flows` met een kloon van template `WqxPSh`. Live zetten en het Mystery-filter aanpassen doet Floris.

### 5.3 Wat kan via de API en wat alleen in de UI

| Actie | API | UI |
|---|---|---|
| Herinstap van X3ySuU | nee (`definition` niet in `PATCH /api/flows`) | ja |
| Profielfilter en triggerfilter van X3ySuU | nee (zelfde reden) | ja |
| Verzendfilters P2-SAFE en P1 | ja, `PATCH /api/flow-actions/{id}` | ja |
| Nieuwe herhaalflow als draft | ja, `POST /api/flows` met `definition` en `reentry_criteria` | |
| Flow live zetten | technisch ja (`PATCH` status), maar het beleid is: Floris | ja |
| Aftersell TYP-instelling | nee (alleen lezen) | Aftersell-app |

---

## Bronnen

- Klaviyo, re-entry en flow triggers (via zoekresultaten): https://help.klaviyo.com/hc/en-us/articles/115002779051-Understand-flow-triggers-and-filters en https://help.klaviyo.com/hc/en-us/articles/360003040052 [leverancier]
- Klaviyo, post-purchase flow: https://help.klaviyo.com/hc/en-us/articles/360028872611 [leverancier]
- Klaviyo, Smart Sending: https://help.klaviyo.com/hc/en-us/articles/115002779311 [leverancier]
- Klaviyo Community, herinstap gelijk aan het filter: https://community.klaviyo.com/marketing-30/how-do-i-do-browse-abandonment-flow-profile-filter-has-not-been-in-this-flow-19032 [community]
- Klaviyo Community, wanneer filters gelden: https://community.klaviyo.com/marketing-30/flow-filters-has-not-been-in-flow-at-any-time-and-has-not-been-in-flow-in-the-last-x-days-5569 [community]
- Klaviyo Community, nieuw tegen terugkerend: https://community.klaviyo.com/marketing-30/conditional-split-for-post-purchase-new-vs-returning-8525 [community]
- Aftersell, post-purchase overview: https://aftersell.mintlify.app/aftersell/post_purchase_overview [leverancier]
- Top Growth Marketing, post-purchase playbook 2026: https://topgrowthmarketing.com/post-purchase-email-flow-for-dtc-brands/ [bureau]
- Attribuly, repeat-customer blueprints: https://attribuly.com/blogs/klaviyo-post-purchase-flow-repeat-customer-blueprints/ [leverancier, niet volledig gelezen]

Kanttekening: help.klaviyo.com, attribuly.com en ecommercebadassery.com konden in deze sessie niet direct geopend worden (netwerkinstelling). De Klaviyo-claims komen uit de samenvattingen van de zoekresultaten.
