# Flows-ontwerp urgentie-sprint (8 nov 2026, rol: flow architect)

Vraag Floris: welke van de 6 urgentiemails (FLASH, VIP-WEEKEND, CREDIT, LAST-HOURS, GIFTS, DRAW) worden dynamische Klaviyo-flows in plaats van losse campagnes, en de hele "Redeem your $X"-reis voor store credit 100% als flow.

Alleen gelezen en ontworpen. Niets aangemaakt in Klaviyo, Shopify of Rise.ai: geen flows, segmenten, lijsten, coupons, geen testmails. Klaviyo alleen met GET (`kl.py`): 129 flows met triggers en definities van TZG9Mx, QUBUQV, WdRz5k, X3ySuU, Vd38Vc, T4a5Mk, Rn556d, YqKCmH, UyFc78; lijsten; metrics; eigenschapsnamen (geen waarden) van Placed Order, Coupon Assigned en Coupon Used. Geen klantdata in dit stuk. BF-code blijft BFCODE.

Gelezen: BRIEF.md, copy/, copy-agressief/, ux/, scheduling/kalender.md, segmentation/segmenten.md, `research/plannen/2026-11-punten-store-credit.md`, `research/plannen/2026-11-urgentie.md`, CLAUDE.md, DECISIONS.md, PLAYBOOK.md (sectie 4), `klaviyo/flows/v4-flow-system.md`, `scripts/build_aff_flows.py` (bewezen definitievorm voor `POST /api/flows`).

---

## 0. Kort

| Mail | Wordt | Trigger | Waarom |
|---|---|---|---|
| 3 CREDIT | **100% flow, 4 delen** | C-L lijst "URG · Credit · bf26" (import of Rise-uitgifte), C-X datumeigenschap `rise_wallet_next_expiration_date` (7 d, 2 d, 1 d, dag zelf), C-R Rise-event "credit uitgegeven" (doorlopend), C-E blok in P1 (X3ySuU) | Bedrag en vervaldatum zijn per persoon; wie verzilvert valt er vanzelf uit (saldo 0). Vervangt campagnes L1, L2, X1 tot X4 en de CREDIT-campagne van 30 nov |
| 2 VIP-WEEKEND | **campagne + flow** | Campagne vr 13 (en do 26) deelt de code uit; flow F-VIP start op **Coupon Assigned** (XUMYt7) van de VIP-pool | Aankondiging is één moment voor een groep; de herinneringen (zo 12:00 niet-openers, zo 17:00 laatste uren) hangen af van gedrag en codegebruik per persoon. Geen segment E per campagne meer nodig |
| 1 FLASH | **campagne + flow**, prijs = huidige websiteprijs | Campagne do 12 (en 19) met persoonlijke code; flow F-FLASH op Coupon Assigned van de FLASH-pool (14:00 niet-openers, 17:00 laatste uren) | Prijsregel Floris: geen eigen lagere flashprijs. Het enige dat per persoon echt eindigt is een persoonlijke code. Zonder code geen flash, dan een gewone mail zonder deadline |
| 4 LAST-HOURS | **stap in de flows** voor FLASH, VIP en CREDIT; **campagne** voor GIFTS, DRAW en E19 | In flows: split "geopend, niet geklikt, sinds flowstart" | Binnen een flow kent Klaviyo de start per persoon; na een campagne zonder code niet |
| 5 GIFTS | **campagne** | Lijst/segment, ma 30 nov 07:00 | Eén einde voor iedereen (einde sale). Besluit 1 nov: geen sale-einddatum in flowmails |
| 6 DRAW | **campagne**, later een P1-blok | zo 22 nov 09:00 | Eén sluitmoment (zondag 23:59 PT, regels). Na publicatie van de regels: regel "You're in this week's draw" in P1 (template-wissel, geen nieuwe mail) |
| (optie, na BF) | F-FLASH-P persoonlijk 24-uursvenster op gedrag | Segment "hete kijker" (hero 2x bekeken in 7 d, geen cart/checkout, geen flowcode in 30 d) | Pas na BFCM testen: cart TZG9Mx, checkout QUBUQV en browse WdRz5k geven al een persoonlijke code van 48 u op dezelfde events. Een tweede flow op Viewed Product of Added to Cart geeft dubbele mails en dubbele codes |

Nodig vóór er iets gebouwd wordt (details sectie 8):
1. **Rise.ai**: koppeling met Klaviyo aan, eigen Rise-mails uit, test met 5 interne adressen waarin `rise_wallet_balance` en `rise_wallet_next_expiration_date` op het profiel verschijnen, eventnamen voor uitgifte en verzilvering. Lukt dat niet: CSV-import (sectie 3.5).
2. **Floris**: ja of nee op een persoonlijke code voor FLASH (op de huidige prijzen, percentage) en het VIP-percentage; per mechaniek de couponpools in Klaviyo (per regio, of één pool met vaste eindtijd); eindmoment en tijdzone van het tegoed (23:59 ET of per regio, gelijk aan het einde van de sale).
3. **Eén proef-datumflow** in de editor (draft) die we met GET uitlezen, zodat de JSON-velden van de datumtrigger kloppen (sectie 4.0).

---

## 1. Uitgangspunten

1. **Prijsregel Floris (8 nov):** alles wat "flash" heet gebruikt de huidige websiteprijzen. Geen flow of mail die afhangt van een aparte lagere flashprijs. Prijzen in flowmails komen uit de catalogus of de PRICE-macro, nooit hard in de copy. Gevolg voor copy.md: `{{FLASH_PRICE}}` = de huidige prijs, en zinnen als "Then it goes back to $249" of "One day at this price" vervallen, want de prijs gaat niet terug. Wat wel eindigt, is de persoonlijke code (als Floris die geeft). Doorgeven aan de copy-rol.
2. **Besluit 1 nov:** flows noemen de einddatum van de sale niet. De flows hieronder noemen alleen een persoonlijke deadline: de vervaldatum van het eigen tegoed of van de eigen code. GIFTS en DRAW (deadline voor iedereen) blijven daarom campagnes.
3. **Register (PLAYBOOK 1):** flows zijn kalm, campagnes LOUD. De flowmails voor FLASH en VIP zijn vervolgmails van een LOUD campagne en mogen de campagnetoon houden (zelfde deadline, zelfde week); CREDIT C-X houdt de toon van het tegoedplan.
4. **Echte deadline uit de bron, niet uit de copy.** In flows op Coupon Assigned staat de echte vervaltijd in het event (`CouponExpirationDate`). In C-X staat hij op het profiel. De mail toont die waarde, zodat de tekst niet kan afwijken van de backend.
5. **Smart sending** uit op alle mails met een deadline vandaag (anders verdringt de campagne van 08:30 de mail van 17:00), aan op mails zonder deadline (C-R, C-L herzending). Bescherming via vaste filters per mail (sectie 6).
6. **Geen samenkomende takken** (v4 2.1, zoals S1 R22pzb): waar twee paden dezelfde staart hebben, staat de staart dubbel.
7. **Naam:** alle sprintflows heten "URG · ...". Segment G ("kreeg vandaag sprintmail") moet dan ook `Received Email` met `$flow` = de URG-flow-ID's tellen, niet alleen Campaign Name.
8. **Holdout tegoed:** profieleigenschap `siraat_credit_cohort` = "holdout" komt in geen enkele credit-flow (flowfilter).

---

## 2. Per mail

### 2.1 CREDIT: "Your $X store credit expires tonight" (100% flow)

Zie sectie 3 voor de hele reis. Samengevat:

| | |
|---|---|
| Campagne of flow | Flow, vier delen: C-L (lancering), C-X (vervaldatum), C-R (punten klaar, doorlopend), C-E (verdiend, blok in P1) |
| Trigger | C-L: lijst "URG · Credit · bf26 uitgegeven" (nieuw). C-X: datumeigenschap `rise_wallet_next_expiration_date`, 7 dagen ervoor, eenmalig. C-R: Rise-metric "credit issued" met trigger-filter reden = cashback. C-E: geen eigen flow |
| Flowfilters | `rise_wallet_balance` > 0 (wordt bij elke stap opnieuw gecontroleerd: verzilverd = uit), cohort niet "holdout", e-mail marketing toegestaan |
| Stappen | C-L: L1 di 17 nov 17:00 lokaal, L2 vr 20 nov 17:00 alleen niet-openers. C-X: X1 ma 23 nov 09:00, X2 za 28 nov 09:00, X3 zo 29 nov 09:00, X4 ma 30 nov 12:00, X5 (laatste uren) ma 30 nov 20:00 voor openers zonder klik |
| Deadline-mechanisme | Vervaldatum van het tegoed in Rise, gesynchroniseerd op het profiel; de mail toont die datum en het live saldo |
| Wat nodig is | Rise: koppeling, profielvelden, events, eigen mails uit, test. Floris: tijdzone vervaltijd, lijst + import, besluit holdout. Fallback: CSV met `siraat_credit_expires` (datum) en `siraat_credit_balance` |

Waarom geen campagne meer: de oude kalender heeft X4 (flow, 30 nov 12:00) en CREDIT (campagne, zelfde slot) dubbel. De flow wint: hij loopt op de echte datum per profiel, sluit verzilveraars automatisch uit en werkt na BF ongewijzigd door voor het doorlopende tegoed van 90 dagen.

### 2.2 VIP-WEEKEND: "VIP only: extra 10% on top, ends Sunday midnight" (campagne + flow)

| | |
|---|---|
| Campagne of flow | Aankondiging = campagne (vr 13 nov 08:30, optioneel do 26 nov 17:00, doelgroep segment B uit segmenten.md). Herinneringen = flow F-VIP |
| Trigger F-VIP | Metric **Coupon Assigned** (XUMYt7), trigger-filter `CouponID` = ID van de VIP-pool (numeriek, uit het eerste event na aanmaak; per regio een pool = drie waarden in één OF-groep) |
| Flowfilters | Coupon Used (USRsNP) met `CouponID` = VIP-pool sinds flowstart = 0; Placed Order sinds flowstart = 0; niet in de flow in de laatste 3 dagen (één keer per weekend) |
| Stappen | 1. Wacht tot zondag 12:00 lokaal (`delay_until_weekdays` zondag). 2. Split: Opened Email van de VIP-campagne sinds flowstart = 0 → JA: R-a "Your extra 10% ends tonight" (resend, nieuw onderwerp). NEE → 3. 3. Wacht tot 17:00. 4. Split: geklikt sinds flowstart = 0 → JA: LAST-HOURS (Benjamin, platte brief, minimale footer). NEE → einde |
| Deadline-mechanisme | Couponpool met vaste eindtijd zondag 23:59 per regio (kalender D2). De mail toont `event.CouponExpirationDate`, omgerekend per regio in de template (testen, sectie 9) |
| Wat nodig is | Floris: percentage, stapelen ja of nee, 3 pools (US/AM, EU, APAC) met eindtijd, elk aan een Shopify-kortingsregel, one use. Sjablonen R-a en LAST-HOURS bestaan (urg-vip, urg-last) |

Waarom deze vorm: de campagne zet het moment (iedereen vrijdagochtend), de flow doet het werk dat nu drie handmatige segmenten en twee extra campagnes vraagt. Wie de code gebruikt of bestelt, valt uit de flow. Een lijst-trigger kan ook (lijst vullen op do 20:00 UTC, dan valt `delay_until_time` 08:30 voor US, EU en APAC op vrijdag), maar dan moet iemand via de API een lijst vullen; de campagne is eenvoudiger en de code-uitgifte is het startsignaal.

Evergreen na BF: de bestaande VIP-flow VTkxFL (15%, R2-VIP) krijgt dezelfde herinnering via een eigen F-VIP-pool zodra Floris dat wil; datum-variant met `vip_code_expires_at` is pas nodig als codes buiten Klaviyo worden uitgegeven.

### 2.3 FLASH: "24-hour flash deal ends tonight" (campagne + flow, huidige prijzen)

| | |
|---|---|
| Campagne of flow | Aankondiging = campagne (do 12 nov 08:30, optioneel do 19), doelgroep A-US/A-INT uit segmenten.md. Vervolg = flow F-FLASH |
| Aanbod | Het product of de set **op de huidige websiteprijs** plus een persoonlijke code van X% (Floris kiest X, of geen code). Geen aparte flashprijs |
| Trigger F-FLASH | Coupon Assigned (XUMYt7), trigger-filter `CouponID` = FLASH-pool(s) |
| Flowfilters | Coupon Used FLASH sinds flowstart = 0; Placed Order sinds flowstart = 0; Checkout Started sinds flowstart = 0 (die zit in QUBUQV met C-codes, één code per order); niet in de flow in de laatste 5 dagen |
| Stappen | 1. Wacht 5 u 30 min (= 14:00 lokaal bij verzending 08:30). 2. Split: Opened Email FLASH-campagne sinds flowstart = 0 → JA: R-a "Last hours: ..." NEE → 3. 3. Wacht 3 uur (17:00). 4. Split: geklikt = 0 → JA: LAST-HOURS. NEE → einde |
| Deadline-mechanisme | Pool met vaste eindtijd 23:59 per regio (dan klopt "ends tonight" voor iedereen en vervalt het tijdzoneprobleem niet, maar wordt het per pool geregeld). Alternatief: code geldig 24 uur na aanmaak; dan zegt de copy "your code ends tomorrow at {{tijd}}" uit `CouponExpirationDate`, niet "tonight" |
| Wat nodig is | Floris: ja/nee code, percentage, product/set (copy noemt het), pools. Zonder code: FLASH-campagne zonder deadline-onderwerp, geen F-FLASH |

Let op bij "24 uur na aanmaak": Klaviyo maakt codes in voorraad aan. De Coupon Assigned-events van 8 nov laten bij de bestaande pools zien dat `CouponExpirationDate` vastligt bij het aanmaken van de code (codes die tot 10 uur na aanmaak werden toegewezen, hadden dezelfde vervaltijd) en bij deze pools een jaar na aanmaak ligt. Een "24 uur geldig" na aanmaak is dus voor de lezer korter dan 24 uur, en de bestaande "48H"-pools (B2, K3, C4) moeten in Shopify gecontroleerd worden: als die codes pas na een jaar vervallen, is "your code expires in 48 hours" in die flows niet waar. Daarom hier: vaste eindtijd per pool, en altijd de vervaltijd uit het event tonen.

### 2.4 LAST-HOURS: brief van Benjamin aan openers zonder klik

| | |
|---|---|
| In flows | Laatste stap van F-FLASH (17:00), F-VIP (zo 17:00) en C-X (X5, 30 nov 20:00). Split "Opened Email bron-mail ≥ 1 en Clicked Email = 0 sinds flowstart" |
| Als campagne | Op GIFTS (30 nov), DRAW (22 nov) en E19, zoals de kalender (17:00, op 30 nov 20:00), segment E per moedermail |
| Uitsluiten | De campagne LAST-HOURS van 30 nov sluit ontvangers van C-X X5 uit (`Received Email` met `$flow` = C-X in de laatste 1 dag), anders twee brieven van Benjamin op één avond |
| Opmaak | Platte brief zonder header, minimale footer (afmelden, voorkeuren, adres), zoals de designer bouwde (urg-last) |

### 2.5 GIFTS: "Your 5 free gifts end tonight" (campagne)

Blijft campagne: de gifts eindigen voor iedereen met de sale, een flow kan dat niet persoonlijker maken en mag de sale-einddatum niet noemen (besluit 1 nov). Kalender: ma 30 nov 07:00, resend 13:00, LAST-HOURS 20:00. Flowtaak: geen.

### 2.6 DRAW: "Order by Sunday midnight to enter this week's filter draw" (campagne)

Blijft campagne (één sluitmoment, één set regels). Flowdeel later, alleen na gepubliceerde regels (kalender D3): in P1 van X3ySuU een regel "You're in this week's filter draw. Drawn on Monday." via template-wissel (`PATCH /api/flow-actions/{id}`, zoals de affiliate-blokken), geen nieuwe mail.

---

## 3. De Redeem-reis als flows

### 3.1 Kaart

```
Rise of CSV: tegoed uitgegeven (bf26, vervalt 30 nov 23:59)
        |
        v
[C-L] lijst "URG · Credit · bf26 uitgegeven" (toevoegen = start)
   split holdout-check (flowfilter) -> uit
   wacht tot di 17:00 lokaal ........ L1 "Your past order earned you {points} points"
   wacht 3 d tot vr 17:00 ........... split L1 niet geopend? -> L2 (Benjamin, tekst)
        |
        v  (zelfde profiel, eigen trigger)
[C-X] datum rise_wallet_next_expiration_date, 7 d ervoor
   flowfilter: saldo > 0 (elke stap) ... verzilverd = uit, restsaldo = blijft met nieuw bedrag
   ma 23 nov 09:00 .................. X1 "Your points expire in 7 days"
   za 28 nov 09:00 .................. X2 "{points} points expire in 48 hours"
   zo 29 nov 09:00 .................. X3 "${credit} disappears tomorrow"
   ma 30 nov 12:00 .................. X4 "Your ${credit} expires tonight"  (= CREDIT)
   ma 30 nov 20:00 .................. split geopend X4 en niet geklikt -> X5 LAST-HOURS
        |
        v  na BF, doorlopend
[C-E] order (Placed Order) -> P1 in X3ySuU krijgt blok "This order earns about N points, ready on {datum}"
[C-R] Rise-event credit uitgegeven (cashback, 30 d na fulfillment) -> R1 "Your points are ready" (smart sending aan)
[C-X] zelfde datumflow, tak cohort != bf26: X1 7 d, X3 1 d, X4 dag zelf, zonder sale-taal
```

Exit bij verzilvering, in volgorde van betrouwbaarheid:
1. `rise_wallet_balance` = 0 (Rise werkt het saldo bij na een order met de wallet). Staat in de flowfilter, dus Klaviyo controleert het vóór elke stap.
2. Rise-event "credit redeemed" sinds flowstart = 0 (naam pas zichtbaar na koppeling), als extra flowfilter.
3. Fallback zonder Rise-sync: Placed Order sinds flowstart = 0. Grof (wie zonder tegoed bestelt, krijgt ook geen herinnering meer), maar nooit onwaar. `payment_gateway_names` (gift_card) zit in Placed Order alleen genest onder `$extra` en is in flowfilters niet bruikbaar; een Shopify Flow-tag op de order komt waarschijnlijk te laat in het Klaviyo-event (ordertags worden bij het aanmaken meegestuurd). Niet op bouwen zonder test.

Gedeeltelijk verzilverd: saldo blijft > 0, profiel blijft in C-X, de mail toont het nieuwe saldo ("You used some already. {points} points are left").

### 3.2 Wat Rise.ai moet leveren

| Gegeven | Vorm in Klaviyo | Nodig voor | Status 8 nov |
|---|---|---|---|
| Saldo | profiel `rise_wallet_balance` (getal, USD) | flowfilter C-L/C-X, bedrag in de mail | ontbreekt (geen Rise-velden op profielen) |
| Eerstvolgende vervaldatum | profiel `rise_wallet_next_expiration_date` (datum, ISO, door Klaviyo als datum herkend) | trigger C-X | ontbreekt |
| Walletcode of inwissellink | profiel, bv. `rise_wallet_code` of een URL die het tegoed toepast | gastkopers zonder account (regel "or enter code ...") | onbekend, navragen |
| Event uitgifte | metric, eigenschappen bedrag, vervaldatum, reden (bulk/cashback) | C-R trigger, C-L trigger als Rise het event ook bij bulk stuurt | metric ontbreekt (185 metrics, geen Rise) |
| Event verzilvering | metric, eigenschappen bedrag, restsaldo | exit 2, meting | ontbreekt |
| Instelling | Rise-eigen store-credit-mails uit | geen dubbele mails | Floris |
| Werkt bulk-upload de profielvelden bij? | test met 5 interne adressen, binnen 1 uur zichtbaar | alles | niet getest |
| Tijdzone vervaltijd | 30 nov 23:59, ET of per regio (dan 3 data in de CSV) | copy "expires tonight at 11:59 PM ET" | besluit Floris (kalender punt 6) |

### 3.3 Klaviyo-eigen velden (altijd, ook met Rise)

Eenmalige profielimport op de dag van uitgifte, zodat de mails een terugval hebben en de cohort bekend is: `siraat_points`, `siraat_points_last_order`, `siraat_last_order_month`, `siraat_credit_cohort` ("bf26" of "holdout"), `siraat_credit_expires` (als **datum**: 2026-11-30). Profielen van cohort bf26 tegelijk in lijst "URG · Credit · bf26 uitgegeven" (start C-L). Een CSV-import naar een lijst start een lijstflow; controleren met de 5 testadressen. Werkt dat niet: C-L op een segment "cohort = bf26" laten starten.

### 3.4 Klaviyo-template (live saldo, terugval)

```
{% with bal=person|lookup:'rise_wallet_balance'|default:person|lookup:'siraat_credit_balance'|default:0 %}
{% widthratio bal 1 100 %} points = ${{ bal|floatformat:0 }}{% endwith %}
```
INT: alleen punten, geen dollarbedrag. De `default`-keten in de editor testen op een profiel zonder Rise-veld (Klaviyo ondersteunt geketende filters in `with`, maar dit exacte patroon is nog niet gerenderd).

### 3.5 Terugval als Rise niet naar Klaviyo synct

1. Floris geeft het tegoed in Rise via de bulk-CSV (Rise blijft de bron voor de kassa).
2. Wij importeren dezelfde lijst in Klaviyo: `siraat_credit_balance` (getal), `siraat_credit_expires` (datum), cohort, punten; profielen in lijst "URG · Credit · bf26 uitgegeven".
3. C-X draait op `siraat_credit_expires` in plaats van de Rise-datum; flowfilter `siraat_credit_balance` > 0 **en** Placed Order sinds flowstart = 0.
4. Saldo bijwerken: dagelijkse (minimaal op 22, 27 en 29 nov) export uit Rise van saldo per klant, opnieuw importeren in `siraat_credit_balance`. Zonder die herimport blijft exit 3 (elke order) de regel.
5. Mail toont dan "up to ${credit}" niet: alleen het geïmporteerde bedrag met de zin "Already used it? Then ignore this one." Liever niet: daarom is de Rise-sync het eerste wat Floris test.

---

## 4. JSON-schetsen voor POST /api/flows

Vorm zoals `scripts/build_aff_flows.py` (revision 2025-10-15, bewezen op R22pzb): `{"data":{"type":"flow","attributes":{"name":...,"definition":{triggers, profile_filter, entry_action_id, actions}}}}`. Alle mails `status: draft`, flow draft. Hulpfuncties `pm()`, `tf()`, `G()`, `email()`, `wait()` uit dat script. Metric-ID's: Placed Order RSNxYV, Received Email YkRM4Q, Opened Email WyrTym, Clicked Email W247h8, Checkout Started RfMvni, Coupon Assigned XUMYt7, Coupon Used USRsNP.

### 4.0 Datumtrigger: eerst uitlezen

Er is nog geen enkele datumflow in het account (alle 129 flows: metric of lijst). De velden van een datumtrigger in de API zijn hier niet bewezen. Werkwijze: in de editor één draft-flow "URG · test datum" met trigger "Date property: rise_wallet_next_expiration_date, 7 days before, one-time" maken, met GET `?additional-fields[flow]=definition` uitlezen, verwijderen, en de vorm hieronder vervangen. Verwachte vorm (te bevestigen):

```json
{"type": "date", "date_type": "profile-property",
 "property": "rise_wallet_next_expiration_date",
 "timedelta": {"unit": "day", "value": -7},
 "recurrence": "one-time"}
```

### 4.1 C-X "URG · Credit · vervaldatum" (kern van Redeem)

```json
{"name": "URG · Credit · vervaldatum",
 "definition": {
  "triggers": [{"type": "date", "date_type": "profile-property", "property": "rise_wallet_next_expiration_date",
                "timedelta": {"unit": "day", "value": -7}, "recurrence": "one-time"}],
  "profile_filter": {"condition_groups": [
    {"conditions": [{"type": "profile-property", "property": "properties['rise_wallet_balance']",
                     "filter": {"type": "numeric", "operator": "greater-than", "value": 0}}]},
    {"conditions": [{"type": "profile-property", "property": "properties['siraat_credit_cohort']",
                     "filter": {"type": "string", "operator": "not-equals", "value": "holdout"}}]},
    {"conditions": [{"type": "profile-marketing-consent", "consent": {"channel": "email", "can_receive_marketing": true,
                     "consent_status": {"subscription": "any", "filters": null}}}]}]},
  "entry_action_id": "w0",
  "actions": [
   {"temporary_id": "w0", "type": "time-delay", "data": {"unit": "days", "value": 0, "secondary_value": null, "timezone": "profile", "delay_until_time": "09:00:00"}, "links": {"next": "coh"}},
   {"temporary_id": "coh", "type": "conditional-split",
    "data": {"profile_filter": {"condition_groups": [{"conditions": [{"type": "profile-property", "property": "properties['siraat_credit_cohort']", "filter": {"type": "string", "operator": "equals", "value": "bf26"}}]}]}},
    "links": {"next_if_true": "x1", "next_if_false": "e1"}},

   {"temporary_id": "x1", "type": "send-email", "data": {"status": "draft", "message": {"name": "URG CX · X1 · 7 dagen", "subject_line": "Your points expire in 7 days", "smart_sending_enabled": false,
     "additional_filters": {"condition_groups": [{"conditions": [{"type": "profile-metric", "metric_id": "YkRM4Q", "measurement": "count", "measurement_filter": {"type": "numeric", "operator": "less-than", "value": 3}, "timeframe_filter": {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 1}, "metric_filters": null}]}]},
     "template_id": "TPL_X1", "...": "afzender Benjamin from Siraat, utm_campaign urg-credit-x1"}}, "links": {"next": "w2"}},
   {"temporary_id": "w2", "type": "time-delay", "data": {"unit": "days", "value": 5, "secondary_value": null, "timezone": "profile", "delay_until_time": "09:00:00"}, "links": {"next": "x2"}},
   {"temporary_id": "x2", "type": "send-email", "data": {"status": "draft", "message": {"name": "URG CX · X2 · 48 uur", "subject_line": "{{ points }} points expire in 48 hours", "smart_sending_enabled": false, "template_id": "TPL_X2", "additional_filters": "zelfde vorm, waarde 4"}}, "links": {"next": "w3"}},
   {"temporary_id": "w3", "type": "time-delay", "data": {"unit": "days", "value": 1, "secondary_value": null, "timezone": "profile", "delay_until_time": "09:00:00"}, "links": {"next": "x3"}},
   {"temporary_id": "x3", "type": "send-email", "data": {"status": "draft", "message": {"name": "URG CX · X3 · morgen", "smart_sending_enabled": false, "template_id": "TPL_X3", "additional_filters": "waarde 4"}}, "links": {"next": "w4"}},
   {"temporary_id": "w4", "type": "time-delay", "data": {"unit": "days", "value": 1, "secondary_value": null, "timezone": "profile", "delay_until_time": "12:00:00"}, "links": {"next": "x4"}},
   {"temporary_id": "x4", "type": "send-email", "data": {"status": "draft", "message": {"name": "URG CX · X4 · vandaag", "subject_line": "Your ${{ credit }} expires tonight", "smart_sending_enabled": false, "template_id": "TPL_X4", "additional_filters": null}}, "links": {"next": "w5"}},
   {"temporary_id": "w5", "type": "time-delay", "data": {"unit": "hours", "value": 8, "secondary_value": null, "timezone": "profile"}, "links": {"next": "s5"}},
   {"temporary_id": "s5", "type": "conditional-split", "data": {"profile_filter": {"condition_groups": [
      {"conditions": [{"type": "profile-metric", "metric_id": "WyrTym", "measurement": "count", "measurement_filter": {"type": "numeric", "operator": "greater-than", "value": 0}, "timeframe_filter": {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 1}, "metric_filters": [{"property": "$message", "filter": {"type": "string", "operator": "equals", "value": "X4_MESSAGE_ID"}}]}]},
      {"conditions": [{"type": "profile-metric", "metric_id": "W247h8", "measurement": "count", "measurement_filter": {"type": "numeric", "operator": "equals", "value": 0}, "timeframe_filter": {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 1}, "metric_filters": [{"property": "$message", "filter": {"type": "string", "operator": "equals", "value": "X4_MESSAGE_ID"}}]}]}]}},
    "links": {"next_if_true": "x5", "next_if_false": null}},
   {"temporary_id": "x5", "type": "send-email", "data": {"status": "draft", "message": {"name": "URG CX · X5 · laatste uren (Benjamin)", "smart_sending_enabled": false, "template_id": "TPL_LAST_CREDIT", "additional_filters": null}}, "links": {"next": null}},

   {"temporary_id": "e1", "type": "send-email", "data": {"status": "draft", "message": {"name": "URG CX · evergreen · 7 dagen", "smart_sending_enabled": true, "template_id": "TPL_E7"}}, "links": {"next": "ew6"}},
   {"temporary_id": "ew6", "type": "time-delay", "data": {"unit": "days", "value": 6, "secondary_value": null, "timezone": "profile", "delay_until_time": "09:00:00"}, "links": {"next": "e2"}},
   {"temporary_id": "e2", "type": "send-email", "data": {"status": "draft", "message": {"name": "URG CX · evergreen · morgen", "smart_sending_enabled": true, "template_id": "TPL_E1"}}, "links": {"next": "ew1"}},
   {"temporary_id": "ew1", "type": "time-delay", "data": {"unit": "days", "value": 1, "secondary_value": null, "timezone": "profile", "delay_until_time": "12:00:00"}, "links": {"next": "e3"}},
   {"temporary_id": "e3", "type": "send-email", "data": {"status": "draft", "message": {"name": "URG CX · evergreen · vandaag", "smart_sending_enabled": false, "template_id": "TPL_E0"}}, "links": {"next": null}}
  ]}}
```

Toelichting:
- Trigger op 23 nov 00:00, `w0` wacht tot 09:00 lokaal: X1 ma 23 nov 09:00. Daarna 5 d → za 28, 1 d → zo 29, 1 d tot 12:00 → ma 30, 8 u → 20:00.
- X4 en X5 zonder cap-filter: CREDIT gaat voor (prioriteit uit segmenten.md). De campagnes van 30 nov sluiten C-X-ontvangers uit (sectie 6).
- `X4_MESSAGE_ID` is pas na aanmaak bekend (Klaviyo-ID van de flowmail); dus na POST de split met `PATCH /api/flow-actions/{id}` invullen, of de split op `Opened Email` met `$flow` = flow-ID en "sinds flowstart" zetten (dan telt ook X1 tot X3 als open: minder scherp, wel zonder tweede stap).
- `{{ points }}` en `{{ credit }}` in het onderwerp: in Klaviyo als `{{ person|lookup:'rise_wallet_balance'|... }}` uitschrijven, zelfde logica als 3.4.
- Wordt de vervaldatum per regio anders (3 tijden), dan is de datum voor APAC in UTC soms 30 nov 12:59: datumflows werken op de datum, niet op het uur; controleren dat het profiel in de juiste dag landt (sectie 9).

### 4.2 C-L "URG · Credit · lancering bf26"

```json
{"name": "URG · Credit · lancering bf26",
 "definition": {
  "triggers": [{"type": "list", "id": "LIST_CREDIT_BF26"}],
  "profile_filter": {"condition_groups": [
    {"conditions": [{"type": "profile-not-in-flow", "timeframe_filter": {"type": "date", "operator": "alltime"}}]},
    {"conditions": [{"type": "profile-property", "property": "properties['siraat_credit_cohort']", "filter": {"type": "string", "operator": "equals", "value": "bf26"}}]},
    {"conditions": [{"type": "profile-property", "property": "properties['rise_wallet_balance']", "filter": {"type": "numeric", "operator": "greater-than", "value": 0}}]}]},
  "entry_action_id": "w1",
  "actions": [
   {"temporary_id": "w1", "type": "time-delay", "data": {"unit": "days", "value": 0, "secondary_value": null, "timezone": "profile", "delay_until_time": "17:00:00", "delay_until_weekdays": ["tuesday"]}, "links": {"next": "l1"}},
   {"temporary_id": "l1", "type": "send-email", "data": {"status": "draft", "message": {"name": "URG CL · L1 · You have $X waiting", "subject_line": "Your past order earned you {{ points }} points", "smart_sending_enabled": false, "template_id": "TPL_L1"}}, "links": {"next": "w2"}},
   {"temporary_id": "w2", "type": "time-delay", "data": {"unit": "days", "value": 3, "secondary_value": null, "timezone": "profile", "delay_until_time": "17:00:00"}, "links": {"next": "s2"}},
   {"temporary_id": "s2", "type": "conditional-split", "data": {"profile_filter": {"condition_groups": [{"conditions": [{"type": "profile-metric", "metric_id": "WyrTym", "measurement": "count", "measurement_filter": {"type": "numeric", "operator": "equals", "value": 0}, "timeframe_filter": {"type": "date", "operator": "flow-start"}, "metric_filters": [{"property": "$flow", "filter": {"type": "string", "operator": "equals", "value": "THIS_FLOW_ID"}}]}]}]}},
    "links": {"next_if_true": "l2", "next_if_false": null}},
   {"temporary_id": "l2", "type": "send-email", "data": {"status": "draft", "message": {"name": "URG CL · L2 · Benjamin tekst", "smart_sending_enabled": true, "template_id": "TPL_L2"}}, "links": {"next": null}}
  ]}}
```

- Lijst vullen op ma 16 nov (na de Rise-upload); `delay_until_weekdays` dinsdag houdt iedereen tot di 17 nov 17:00 lokaal vast, ongeacht het uur van de import. L2 op vr 20 nov 17:00 (lege sprintdag; do 19 is FLASH 2).
- Eerst E90-kopers in de lijst, 24 u later de slapers (segmenten.md, mail 3): de flow werkt dan per groep een dag later; de weekdag-wachttijd verschuift de slapers naar di 24 nov 17:00. Liever: slapers op ma 16 23:00 UTC toevoegen, dan valt het ook op dinsdag maar loopt de verzending per tijdzone gespreid. Keuze bij de bouw.
- `THIS_FLOW_ID` pas na aanmaak bekend: split na POST patchen.
- Holdout krijgt cohort "holdout" en staat niet op de lijst.

### 4.3 F-VIP "URG · VIP-weekend · herinneringen" (Coupon Assigned)

```json
{"name": "URG · VIP-weekend · herinneringen",
 "definition": {
  "triggers": [{"type": "metric", "id": "XUMYt7", "trigger_filter": {"condition_groups": [{"conditions": [
     {"type": "metric-property", "metric_id": "XUMYt7", "field": "CouponID", "filter": {"type": "string", "operator": "equals", "value": "VIP_POOL_US"}},
     {"type": "metric-property", "metric_id": "XUMYt7", "field": "CouponID", "filter": {"type": "string", "operator": "equals", "value": "VIP_POOL_EU"}},
     {"type": "metric-property", "metric_id": "XUMYt7", "field": "CouponID", "filter": {"type": "string", "operator": "equals", "value": "VIP_POOL_APAC"}}]}]}}],
  "profile_filter": {"condition_groups": [
    {"conditions": [{"type": "profile-metric", "metric_id": "RSNxYV", "measurement": "count", "measurement_filter": {"type": "numeric", "operator": "equals", "value": 0}, "timeframe_filter": {"type": "date", "operator": "flow-start"}, "metric_filters": null}]},
    {"conditions": [{"type": "profile-metric", "metric_id": "USRsNP", "measurement": "count", "measurement_filter": {"type": "numeric", "operator": "equals", "value": 0}, "timeframe_filter": {"type": "date", "operator": "flow-start"}, "metric_filters": null}]},
    {"conditions": [{"type": "profile-not-in-flow", "timeframe_filter": {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 3}}]}]},
  "entry_action_id": "w1",
  "actions": [
   {"temporary_id": "w1", "type": "time-delay", "data": {"unit": "days", "value": 0, "secondary_value": null, "timezone": "profile", "delay_until_time": "12:00:00", "delay_until_weekdays": ["sunday"]}, "links": {"next": "s1"}},
   {"temporary_id": "s1", "type": "conditional-split", "data": {"profile_filter": {"condition_groups": [{"conditions": [{"type": "profile-metric", "metric_id": "WyrTym", "measurement": "count", "measurement_filter": {"type": "numeric", "operator": "equals", "value": 0}, "timeframe_filter": {"type": "date", "operator": "flow-start"}, "metric_filters": [{"property": "Campaign Name", "filter": {"type": "string", "operator": "contains", "value": "URG · VIP"}}]}]}]}},
    "links": {"next_if_true": "ra", "next_if_false": "w2"}},
   {"temporary_id": "ra", "type": "send-email", "data": {"status": "draft", "message": {"name": "URG VIP · R-a · ends tonight", "subject_line": "Your extra 10% ends tonight", "smart_sending_enabled": false, "template_id": "TPL_VIP_RA"}}, "links": {"next": null}},
   {"temporary_id": "w2", "type": "time-delay", "data": {"unit": "hours", "value": 5, "secondary_value": null, "timezone": "profile"}, "links": {"next": "s2"}},
   {"temporary_id": "s2", "type": "conditional-split", "data": {"profile_filter": {"condition_groups": [{"conditions": [{"type": "profile-metric", "metric_id": "W247h8", "measurement": "count", "measurement_filter": {"type": "numeric", "operator": "equals", "value": 0}, "timeframe_filter": {"type": "date", "operator": "flow-start"}, "metric_filters": [{"property": "Campaign Name", "filter": {"type": "string", "operator": "contains", "value": "URG · VIP"}}]}]}]}},
    "links": {"next_if_true": "lh", "next_if_false": null}},
   {"temporary_id": "lh", "type": "send-email", "data": {"status": "draft", "message": {"name": "URG VIP · LAST-HOURS · Benjamin", "smart_sending_enabled": false, "template_id": "TPL_LAST_VIP"}}, "links": {"next": null}}
  ]}}
```

- `CouponID` is in de events een getal als tekst ("9240206"); de echte waarde pas na aanmaak van de pool uit het eerste Coupon Assigned-event halen. Werkt `string equals` niet op dit veld, dan `numeric equals`.
- Coupon Used zonder `metric_filters`: wie welke Klaviyo-code dan ook gebruikt, valt eruit. Met filter `CouponID` = VIP-pool is het preciezer; beide zijn waar.
- Niet-openers krijgen alleen R-a (12:00), openers zonder klik alleen LAST-HOURS (17:00): nooit twee vervolgmails op één dag, zoals de kalender (sectie 5) eist.
- VIP-weekend 2 (do 26 tot zo 29): zelfde flow, nieuwe pools in de trigger, of een kopie met de nieuwe pool-ID's.

### 4.4 F-FLASH "URG · Flash · herinneringen"

Zelfde vorm als 4.3 met:
- trigger-filter op de FLASH-pools;
- extra flowfilter Checkout Started (RfMvni) sinds flowstart = 0 (die zitten in QUBUQV);
- `w1` = `{"unit": "minutes", "value": 330}` (14:00 bij verzending 08:30), split niet geopend `Campaign Name contains "URG · FLASH"` → R-a "Last hours: {product}" ; anders `w2` = 3 uur → split niet geklikt → LAST-HOURS;
- in de mails de vervaltijd uit `{{ event.CouponExpirationDate }}` (opmaak testen), nooit een flashprijs.

### 4.5 Gedeelde filterblokken

Cap per mail (`additional_filters`), tot en met 26 nov waarde 3, vanaf 27 nov waarde 4:
```json
{"condition_groups": [{"conditions": [{"type": "profile-metric", "metric_id": "YkRM4Q", "measurement": "count",
  "measurement_filter": {"type": "numeric", "operator": "less-than", "value": 3},
  "timeframe_filter": {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 1}, "metric_filters": null}]}]}
```
Net een cart/checkout/browse-mail (1 uur), voor F-FLASH en F-VIP:
```json
{"conditions": [{"type": "profile-metric", "metric_id": "YkRM4Q", "measurement": "count",
  "measurement_filter": {"type": "numeric", "operator": "equals", "value": 0},
  "timeframe_filter": {"type": "date", "operator": "in-the-last", "unit": "hour", "quantity": 1},
  "metric_filters": [{"property": "$flow", "filter": {"type": "string", "operator": "equals", "value": "TZG9Mx"}}]}]}
```
(één conditie per flow-ID: TZG9Mx, QUBUQV, WdRz5k, QNZyEb; elk als eigen groep, want binnen een groep is het OF. `unit: hour` is niet eerder via de API gebruikt; anders `day` 1.)

### 4.6 F-FLASH-P (optie na BF): persoonlijk 24-uursvenster op gedrag

| | |
|---|---|
| Trigger | Segment "URG · Flash · hete kijker": E90, nooit gekocht, Viewed Product hero of 2 Pans + 2 Lids ≥ 2 in 7 d, Added to Cart en Checkout Started = 0 in 7 d, `last_flow_code_at` niet in de laatste 30 d, Received Email van WdRz5k/QNZyEb in 4 d = 0 |
| Stappen | Wacht tot 17:00 lokaal → mail P1 met eigen code (pool 24 u, huidige prijzen) → Coupon Assigned start F-FLASH-P-herinnering: +18 u "6 hours left" als code niet gebruikt, met `CouponExpirationDate` |
| Waarom pas na BF | Cart, checkout en browse geven al codes op deze events (B2/K3/C4, regel één code per persoon per 30 dagen). Eerst meten hoeveel kijkers na de browse-flow zonder code overblijven; in januari als test met holdout |

---

## 5. Samenspel met bestaande flows

| Flow | Trigger | Botsing | Regel |
|---|---|---|---|
| Cart TZG9Mx | Added to Cart | F-FLASH/F-VIP op dezelfde dag; cart-code K3 en sprintcode in één order kan niet (één code per order) | F-FLASH en F-VIP: niet als in 1 uur een cart/checkout/browse-mail kwam (4.5); F-FLASH: Checkout Started sinds start = 0. Credit stapelt (betaalmiddel), geen uitsluiting |
| Checkout QUBUQV | Checkout Started | idem, C4-code | idem |
| Browse WdRz5k, QNZyEb | Viewed Product | F-FLASH-P zou op hetzelfde gedrag vuren | F-FLASH-P alleen na de browse-flow (4 d stilte) en zonder flowcode in 30 d; pas na BF |
| BF-direct Rn556d, Welcome T4a5Mk, BF follow-up YqKCmH | lijst Uw8eZG | nieuwe aanmelders krijgen ochtendmails | Sprintflows raken ze nauwelijks (credit = kopers; VIP = kopers; FLASH volgt de campagne-doelgroep). Geen extra filter; de cap van 3 per dag vangt de rest |
| Post-purchase X3ySuU | Placed Order | C-X kan een herinnering sturen een uur na een order zonder tegoed | X1 tot X3: `additional_filters` Placed Order in de laatste 1 dag = 0. X4/X5 niet (laatste dag). C-E = blok in P1 via template-wissel, geen extra mail |
| Upsell Vd38Vc | Placed Order (+2 u, test) | idem | idem |
| VIP VTkxFL | Placed Order (2e order) | VIP-weekendcode boven op R2-VIP 15% | VIP-campagne sluit ontvangers van een VTkxFL-codemail in 7 d uit; regel één code per 30 dagen (`last_flow_code_at`) |
| Winback UyFc78, oude winback UEfh4h | Placed Order +45 d | | Dynamisch blok "You have X points until {datum}" als saldo > 0 (tegoedplan); geen nieuwe mail |
| Failure to launch T2SmtR | lijst, 19:00 | X5 20:00 en LAST-HOURS 17:00 | Cap-filter; FTL is klein |
| Sunset TbYQmX | lijst | Slapende kopers krijgen tegoed | Credit-flows sluiten Sunset bewust niet uit (tegoedplan), wel spamstop 0,3% |

---

## 6. Maximaal per persoon per dag en voorrang

- Voorrang (segmenten.md): CREDIT > VIP > FLASH > GIFTS > DRAW. LAST-HOURS telt mee als vervolgmail, niet als eigen sprintmail.
- Cap: alle mails samen 3 per dag tot en met 26 nov, 4 vanaf 27 nov. In flows via `additional_filters` (4.5), in campagnes via de uitsluiting uit de kalender.
- Hoogste voorrang krijgt geen cap: X4 en X5 (30 nov) en L1 (17 nov). De campagnes van die dag sluiten die ontvangers uit:
  - 30 nov v2-mon-pm 13:00: uitsluiten `Received Email` `$flow` = C-X in de laatste 1 dag.
  - 30 nov LAST-HOURS 20:00 (campagne): uitsluiten ontvangers van C-X X5.
  - 17 nov: geen andere sprintmail; Rise-L1 op 17:00 (kalender punt 7, niet 19:00 vanwege FTL).
- Per sprintdag nooit twee vervolgmails voor één persoon: in F-FLASH en F-VIP sluiten de twee splits elkaar uit.
- Smart sending: uit op X1 tot X5, L1, F-FLASH, F-VIP (deadline); aan op L2, C-R, evergreen-takken.

---

## 7. Bouwvolgorde

| # | Wat | Afhankelijk van | Bouwen (draft) | Live uiterlijk |
|---|---|---|---|---|
| 1 | Besluiten Floris: code FLASH ja/nee en %, VIP % en stapelen, tijdzone tegoed | | | ma 9 / di 10 nov |
| 2 | Proef-datumflow in de editor, GET, verwijderen (4.0) | Floris of ik op akkoord | di 10 nov | n.v.t. |
| 3 | VIP-pools (3) en F-VIP | 1, pools | wo 11 nov | **do 12 nov 12:00 CET** (campagne vr 13 08:30 APAC = do 21:30 UTC) |
| 4 | FLASH-pools en F-FLASH (alleen bij ja op code) | 1, pools | di 10 nov | **wo 11 nov 12:00 CET** |
| 5 | Rise-koppeling en test met 5 adressen; eventnamen noteren | Rise-plan | Floris, vóór vr 13 nov | |
| 6 | Lijst "URG · Credit · bf26 uitgegeven", profielimport, C-L | 5 (of fallback 3.5) | vr 13 nov | **ma 16 nov** (lijst vullen ma 16, L1 di 17 17:00) |
| 7 | C-X op de echte datumtrigger, met X4 als vervanger van de CREDIT-campagne | 2, 5 | ma 16 nov | **vr 20 nov** (vóór de bevriezing van 20 nov en ruim vóór de eerste trigger op 23 nov 00:00 in APAC = 22 nov 13:00 UTC) |
| 8 | Campagnes van 30 nov uitsluiting C-X toevoegen; CREDIT-campagne en Rise-X4-campagne schrappen | 7 | wo 25 nov | |
| 9 | F-VIP voor weekend 2 (nieuwe pools) | 3 | ma 23 nov | wo 25 nov 12:00 CET |
| 10 | C-E blok in P1 (X3ySuU), C-R "Your points are ready", evergreen-tak C-X | cashback in Rise aan | december | half december (eerste cashback komt 30 d na fulfillment) |
| 11 | DRAW-regel in P1 | gepubliceerde regels | na D3 | |
| 12 | F-FLASH-P als test | meting browse-flow | januari | |

Elke flow eerst als draft met alle mails op draft; testmails naar interne adressen ontvangen en bekeken vóór live (DECISIONS 8 okt). Niet in Auto-modus live zetten (PLAYBOOK 9).

---

## 8. Wat Floris en Rise.ai moeten leveren

**Rise.ai**
1. Plan met bulk store credit, Klaviyo-integratie en cashback; Klaviyo koppelen; eigen store-credit-mails uit.
2. Profielvelden `rise_wallet_balance` en `rise_wallet_next_expiration_date` (datum) zichtbaar binnen een uur na de bulk-upload; navragen of een walletcode of inwissellink op het profiel kan.
3. Eventnamen en eigenschappen voor uitgifte en verzilvering (zie 3.2).
4. Vervaldatum per uitgifte: 30 nov 23:59 in de gekozen tijdzone; zegt Rise alleen een datum, welke tijdzone geldt?

**Floris**
5. FLASH: product of set (huidige prijs), ja of nee persoonlijke code en percentage. Bij nee vervalt F-FLASH en verliest de FLASH-campagne het deadline-onderwerp.
6. VIP: percentage, stapelen met BFCODE/HI10, drie pools met eindtijd zo 15 nov 23:59 PT/CET/AEDT (en zo 29 nov).
7. Tegoed: tijdzone (ET of per regio), holdout 5% ja of nee, wie uploadt.
8. Bestaande pools B2/K3/C4 in Shopify controleren: vervallen die codes echt na 48 uur? De Coupon Assigned-events tonen een vervaltijd een jaar na aanmaak (sectie 2.3).
9. Akkoord op de bouw van de flows als draft (ik bouw met POST /api/flows op akkoord; nu niets aangemaakt).

**Copy-rol (doorgeven)**
10. FLASH-copy zonder eigen flashprijs en zonder "goes back to $249"; deadline = de code ("Your code ends tonight at 11:59 PM PT").
11. Teksten voor R-a VIP, R-a FLASH, X1 tot X5, L1, L2 als flowmails; LAST-HOURS-varianten voor credit.

---

## 9. Risico's en open punten

1. **Datumtrigger-JSON niet bewezen** (geen datumflow in het account). Oplossing 4.0.
2. **Coupon Assigned als trigger**: metric bestaat en vuurt (events van 8 nov), maar is niet eerder als flowtrigger gebruikt. Test: één draft-flow op een testpool, testprofiel een code geven via een previewmail, kijken of de flow start. Werkt het niet: F-VIP/F-FLASH als lijstflow (lijst vullen met de campagne-doelgroep, sectie 2.2).
3. **Opened Email en Apple MPP**: "geopend" is vaak automatisch. R-a gaat dan naar minder mensen en LAST-HOURS naar meer; dat is acceptabel omdat LAST-HOURS de deadline herhaalt (kalender sectie 5).
4. **Tijdweergave van `CouponExpirationDate`** (UTC) in de template: Klaviyo-datumfilters rekenen niet per profieltijdzone om. Per regio-pool is de tijd bekend; dan beter de vaste tekst per pool ("11:59 PM PT") via een split op `CouponID` of op land, en de eventwaarde alleen als controle.
5. **Datum en regio**: een vervaltijd 23:59 ET is in APAC al 1 dec. Datumflows rekenen op de kalenderdag van de eigenschap; met één datum (2026-11-30) krijgt APAC X4 op 30 nov 12:00 lokaal terwijl het tegoed in ET pas 1 dec 15:59 AEDT verloopt. Dat is te vroeg, niet onwaar, mits de copy de exacte tijd met tijdzone noemt.
6. **Lijstflow op CSV-import**: start naar verwachting bij import, testen met de 5 adressen.
7. **Bevriezing 20 nov tot 6 dec** (v4 testplan): nieuwe flows na 20 nov alleen C-X-uitsluitingen en VIP 2; de rest moet er vóór 20 nov staan.
8. **`siraat_*`-sync staat sinds 8 okt stil** (segmenten.md): de fallback van 3.5 mag niet op die nachtelijke sync leunen; eigen eenmalige import.
