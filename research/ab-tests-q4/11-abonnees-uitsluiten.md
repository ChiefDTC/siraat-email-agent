# 11 · Abonnees uitsluiten uit Mystery Gift YwsKcf (29 okt 2026, 22:00 tot 23:00 UTC)

Vraag van Floris: worden de ongeveer 120 nieuwe abonnees van vandaag 100% zeker uitgesloten van M1 tot en met M4 van `v4 · Mystery Gift` (YwsKcf)? Dit rapport bevat geen klantdata, namen of ordernummers.

## Kort antwoord

- **Vóór deze sessie: nee.** De Items-filter (Placed Order, Items contains "Dishwasher Sheets") werkte niet: hij vangt niemand. De enige werkende uitsluiting was WPwuMk ("Subscription started on ReCharge"), en die komt sinds 16:14 UTC vandaag niet meer binnen. Van de 45 abonnees die nu in de flow zitten, zouden er 39 M1 krijgen (vanaf 1 nov 10:00 lokale tijd).
- **Nu: ja, voor alle 45.** Op M1 tot en met M4 staat een extra verzendfilter op Ordered Product (XT7f8Z) met Name contains "Dishwasher Sheets" = 0 keer in 90 dagen. Die filter vangt in de test 138 van de 138 sheets-kopers, ook bij $0.
- **Niemand** van de abonnees van vandaag heeft al een YwsKcf-mail ontvangen.

## 1. Werkt de Items-filter?

`Items` in Placed Order (RSNxYV) is een **lijst** met productnamen, bijvoorbeeld `["Shipping Protection", "Mystery Gift", "Plastic-Free Home E-Book", "PFAS Water Purifier Giveaway (Weekly Draw Entry)", "Free Shipping", "Titanium Hammered Pan Pro Standard", "Non-Toxic Dishwasher Sheets"]`. De sheets staan er ook in bij $0. De naam is altijd exact "Non-Toxic Dishwasher Sheets"; "Plastic-Free Dishwasher Sheets" kwam in de orders van 28 en 29 okt niet voor.

Hard getest met tijdelijke segmenten (Placed Order, laatste 2 dagen, aantal > 0), daarna allemaal verwijderd:

| Conditie | Profielen | Waarvan sheets-kopers (138) |
|---|---|---|
| Geen eigenschapsfilter (controle) | 816 | 138 |
| `Source Name` string contains "we" (controle op een gewone tekstwaarde) | 653 | 122 |
| `Items` string contains "Dishwasher Sheets" (**zoals nu in YwsKcf**) | **0** | **0** |
| `Items` string contains "Non-Toxic Dishwasher Sheets" | 0 | 0 |
| `Items` string equals "Non-Toxic Dishwasher Sheets" | 0 | 0 |
| `Items` string in ["Non-Toxic Dishwasher Sheets"] | 0 | 0 |
| `Items` **list contains-any** ["Non-Toxic Dishwasher Sheets"] | 156 | 138 |
| Ordered Product (XT7f8Z) `Name` string equals "Non-Toxic Dishwasher Sheets" | 156 | 138 |
| Ordered Product `Name` string contains "Dishwasher Sheets" | 156 | 138 |
| Ordered Product `ProductID` equals 15483020443988 | 156 | 138 |

Conclusie: een string-filter op een lijsteigenschap matcht in Klaviyo nooit. "Aantal = 0" is daardoor altijd waar en de filter laat iedereen door. Dat geldt voor de twee Items-filters in het profielfilter van de flow en voor de Items-filter op M1 tot en met M4. Een lijst vraagt type `list` met operator `contains-any` (het type dat QUBUQV al gebruikt), of een filter op Ordered Product, waar `Name` een gewone tekst is. In alle andere live flows staat `Items` als `list contains-any`; alleen YwsKcf had de string-variant.

De 18 profielen die meer in de segmenten zitten dan de 138 hebben een sheets-order van 27 okt laat (het segment kijkt 2 dagen terug, de eventlijst begon op 28 okt 00:00 UTC).

## 2. Komt WPwuMk binnen, en wanneer?

- 29 okt: **60 WPwuMk-events** (59 profielen), allemaal tussen 00:01 en **16:14 UTC**. Het event komt binnen dezelfde minuut als de order (mediaan 0 minuten, maximaal 88 minuten). Op tijd voor M1 dus, als het komt.
- Na 16:14 UTC: **0 events**, terwijl er tot 21:51 UTC nog 66 orders met sheets kwamen. "Order placed successfully on Recharge" (R5YMXn) stopt op dezelfde seconde. "Subscription cancelled" (YksUBL) kwam om 19:42 UTC nog wel binnen, dus de koppeling zelf leeft.
- Oorzaak (Shopify, alleen gelezen): tot 16:14 UTC hebben de sheets het verkoopplan `691181781332` ("Free first pack, then $20 every 28 days") en krijgt de order de tags "Subscription" en "Subscription First Order". Vanaf 16:14 UTC hebben de sheets het verkoopplan `691200917844` ("Every 28 days") en **geen** abonnementstags. Steekproef: 10 van 10 orders na 16:14 hebben het nieuwe plan zonder tags, 5 van 5 ervoor het oude plan met tags. Recharge ziet het nieuwe plan blijkbaar niet. **Floris moet in Recharge nakijken of deze 66 abonnementen wel bestaan en worden afgeschreven.** Dat is groter dan een mailprobleem.
- Recharge-analytics heeft 29 okt nog niet verwerkt (27 okt: 11 nieuwe abonnementen, 28 okt: 18).

Andere signalen in Klaviyo:

| Signaal | Betrouwbaar? |
|---|---|
| `rc_active_subscriber` (profiel) | Wordt **wel** gevuld zodra Recharge synct: true bij 51 van de 59 met WPwuMk, false bij 8 (nog niet bijgewerkt). Leeg bij alle 68 zonder WPwuMk. Alleen zo goed als de Recharge-sync. |
| `rc_active_sku` (profiel) | Gevuld met de sheets-SKU bij dezelfde 51. Zelfde beperking. |
| WPwuMk, R5YMXn (type CHECKOUT) | Op tijd, maar mist alles wat Recharge niet ziet. |
| Ordered Product (XT7f8Z) met Name "Dishwasher Sheets" | Komt van Shopify bij elke order, ook bij $0 en ongeacht verkoopplan. **Meest betrouwbaar.** |
| Placed Order `Items` met `list contains-any` | Even betrouwbaar, maar vraagt de exacte naam. |

## 3. De abonnees van vandaag, per profiel

Populatie: alle profielen met WPwuMk of met sheets in een Placed Order op 29 okt (UTC). Per profiel opgehaald: Ordered Product (Mystery Gift en sheets, sinds 31 jul), WPwuMk, Received Email per flow (sinds 1 sep), Placed Order met waarde > 0 (sinds 23 okt), Refunded Order (30 dagen) en de Recharge-velden.

| | Aantal |
|---|---|
| Abonnees van vandaag | **127** (59 met WPwuMk, 68 zonder) |
| Met Ordered Product "Mystery Gift" vandaag (trigger YwsKcf) | 84 |
| Door het profielfilter buiten de flow | 39 (35 `rc_active_subscriber` = true, 2 al eerder in de flow, 2 al een WvRupU-mail) |
| **In de flow** | **45** (39 zonder WPwuMk, 6 met WPwuMk en `rc_active_subscriber` nog false) |
| Al een YwsKcf-mail ontvangen | **0** |

Per mail, voor de 45 in de flow (M1, M2 en M3 hebben dezelfde uitsluitingsfilters):

| | Oude filters | Met de nieuwe filter |
|---|---|---|
| Zeker geblokkeerd | 6 (WPwuMk) | **45** |
| Krijgt de mail | 39 | 0 |
| Twijfel | 0 | 0 |

Klaviyo heeft geen API voor flowleden; "in de flow" is afgeleid uit de trigger en het profielfilter. Alle 45 hebben ook een betaalde order, dus de $0-filter blokkeert ze niet.

Kanttekening bij het profielfilter: de Items-tellingen daar staan op "sinds start van de flow". Ook met een werkende lijstfilter tellen ze de order die de flow start mogelijk niet mee. De uitsluiting moet dus op de verzendfilters staan (90 dagen), en daar staat hij nu.

## 4. Andere flows (alleen gerapporteerd, niets aangepast)

| Flow | Wat | Risico voor abonnees | Advies |
|---|---|---|---|
| **X3ySuU Post-purchase** | Trigger Placed Order zonder triggerfilter. Verlengingsorders van Recharge komen binnen als Placed Order met `Source Name` = `subscription_contract_checkout_one` (13 verlengingen sinds 27 sep, $20 tot $30). Na 7 van de 13 volgde een X3ySuU-mail. | **Hoog.** Elke 28 dagen start de post-purchase-reeks (P1 tot en met P3) opnieuw na een verlenging van $20. De eerste verlengingen van de nieuwe golf vallen rond 26 nov, midden in BFCM. | Triggerfilter `Source Name` is niet `subscription_contract_checkout_one`. |
| **UyFc78 Winback, VTkxFL VIP, XbYT7T Anniversary** | Zelfde trigger (Placed Order zonder filter). | Middel. Een verlenging telt als aankoop: winback schuift op, en VIP en Anniversary kunnen starten op een order van $20. | Zelfde triggerfilter, of bij VIP een waardegrens. |
| **WdRz5k Browse, QNZyEb Browse TP, TZG9Mx Cart, QUBUQV Checkout** | De sheets staan in de categorienavigatie van de header. Als het bekeken of achtergelaten product sheets is, toont de mail een sheets-FAQ ("30 sheets, up to 60 washes"). | Laag. Een abonnee die de sheets-pagina of het klantportaal bezoekt, kan een browse- of cartmail over sheets krijgen. | Profielfilter of vertakking: `rc_active_sku` is niet gezet, of Ordered Product sheets = 0 in 90 dagen, als het bekeken item sheets is. |
| **X3ySuU P3, UyFc78 R1/R2, VTkxFL V1, XbYT7T N1/N2** | Cross-sell-logica met een vertakking voor sheets-kopers ("Goes with your ..."). Geen sheets- of abonnementsaanbod gevonden in de tekst. | Laag. | Geen actie nodig voor het aanbod. Wel de triggerfilter hierboven. |
| WvRupU (oude Mystery Gift) | Staat stil (DECISIONS). | Geen. | Geen. |

Er is geen andere live flow die het abonnement aanbiedt zoals M3 dat doet.

## 5. Het gat en de fix

**Gat:** de Items-filters in YwsKcf zijn string-filters op een lijst en vangen niemand. De uitsluiting hing daardoor alleen aan WPwuMk en `rc_active_subscriber`, en die vallen weg zodra Recharge een order niet ziet. Sinds 16:14 UTC gebeurt dat met elke nieuwe abonnee.

**Toegepast** (valt onder het akkoord van Floris: alleen een extra uitsluitingsfilter op M1 tot en met M4):

- Acties: M1 `121895219`, M2 `121895221`, M3 `121895224`, M4 `121895236` (draft).
- Nieuwe conditiegroep in `additional_filters` (AND met de bestaande vier):
  `profile-metric` XT7f8Z (Ordered Product), count **equals 0**, **in-the-last 90 dagen**, metric_filter `Name` · `string` · `contains` · "Dishwasher Sheets".
- Teruggelezen via `GET /api/flow-actions/{id}` en `GET /api/flows/YwsKcf`: alle vier hebben 5 conditiegroepen, de nieuwe staat erin, de status is ongewijzigd (M1 tot en met M3 live, M4 draft, flow live). De rest van de actie (onderwerp, template, tracking) is gelijk aan de backup.
- Backups: `scratchpad/mystery_backup_29okt_v2.json` (volledige flowdefinitie vóór de wijziging) en `scratchpad/abo/actions-backup-voor-fix.json` (de vier acties vóór de wijziging).
- Terugdraaien: per actie de laatste conditiegroep (metric XT7f8Z) uit `additional_filters` halen en de actie patchen.

**Voorgesteld, niet toegepast** (dat zijn geen extra uitsluitingsfilters op M1 tot en met M4, dus beslissing Floris):

1. Profielfilter YwsKcf: de twee Items-condities omzetten naar `list contains-any` ["Non-Toxic Dishwasher Sheets", "Plastic-Free Dishwasher Sheets"], of vervangen door Ordered Product Name contains "Dishwasher Sheets" = 0 over 90 dagen. De verzendfilters dekken het nu af, dus dit is opruimen, geen gat.
2. De kapotte Items-verzendfilter op M1 tot en met M4 mag weg of omgezet worden naar `list contains-any`. Hij doet nu niets, maar is ook niet schadelijk.
3. **Recharge: het nieuwe verkoopplan 691200917844 nakijken** (urgent, buiten e-mail).
4. Triggerfilter `Source Name` is niet `subscription_contract_checkout_one` op X3ySuU, UyFc78, VTkxFL en XbYT7T, vóór de eerste verlengingen rond 26 nov.

Restrisico: als het sheets-product een naam krijgt zonder "Dishwasher Sheets", mist de nieuwe filter het. Dan ook de filter aanpassen (of overstappen op ProductID 15483020443988).
