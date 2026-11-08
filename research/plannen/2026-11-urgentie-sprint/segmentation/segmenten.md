# Segmentatie urgentie-sprint (8 nov 2026)

Rol: segmentatie. Alleen gelezen in Klaviyo (segmenten, lijsten, campagnes, campaign-values-report, metric-aggregates, segmentleden als id-tellingen). Niets aangemaakt of gewijzigd, geen testmails. Alleen totalen; ruwe id-bestanden staan in de scratchpad, niet in de repo. Tellingen van 8 nov 2026, ca. 01:30 UTC.

## 0. Kort

| Mail | Doelgroep (kern) | US | INT | Totaal |
|---|---|---|---|---|
| 1 FLASH | E90 niet-kopers + productkijkers L30 + ATC L30, zonder P7 | 60.133 | 34.246 | ~94.400 |
| 2 VIP-WEEKEND | Mailbare kopers, geen order in 14 d | 23.507 | 21.332 | ~44.800 |
| 3 CREDIT | Kopers met tegoed > 0 (Rise), min 5% holdout | ~26.100 | ~21.300 | ~47.400 (nu 0: geen Rise-velden) |
| 4 LAST-HOURS | Openers zonder klik en zonder order van de moedermail | 20.000 tot 31.000 | 15.000 tot 23.000 | per moedermail |
| 5 GIFTS | Heel E90, zonder P7 | 75.212 | 48.083 | ~123.300 |
| 6 DRAW | Heel E90, zonder P7 (andere dag dan GIFTS) | 75.212 | 48.083 | ~123.300 |

Vaste uitsluitingen in elke sprintmail: VSnBnJ (afmelders), W3q7Zy (bounces), W4vNzF (For Suppression), XTpfNG (spam), plus Ur6Ehr (Unengaged 180 d, niet-kopers). SLVWps (Texas, sms) mag blijven staan, doet niets bij e-mail. US en INT altijd als twee campagnes: US op VMjhb2, INT op XrFa5r (overlap 0, gecontroleerd).

Grootste datagaten: (1) `siraat_last_order_at` en waarschijnlijk ook `siraat_owned` zijn sinds **8 okt** niet meer bijgewerkt (laatste waarde 8 okt 14:39; 0 kopers in de laatste 30 dagen volgens dat veld, terwijl UfyDPs er 9.054 telt). Recentheid daarom altijd via Placed Order-segmenten, niet via het profielveld. (2) Geen Rise-velden in Klaviyo (alleen `rc_credit_total_available_balance` van Recharge op 15 profielen, allemaal 0.00), dus het CREDIT-segment is nu leeg. (3) SpBxrC "BFCM · Kopers · mailbaar · geen order 30 d" toont profile_count 0 terwijl de definitie ~41.700 zou opleveren: segment rekent niet of is nooit gevuld; niet gebruiken voor je hem in de UI hebt gecontroleerd. Holdout-lijst XN5G3M is nog leeg (vullen op 12 nov). (4) Echte (niet-Apple) opens per campagne zijn via de API niet te tellen; de LAST-HOURS-schatting is daarom een bandbreedte.

## 1. Bestaande segmenten en lijsten (relevant, met grootte)

Basis en markt (Harmony v2, 3 nov):

| ID | Naam | Profielen | Gebruik |
|---|---|---|---|
| VMjhb2 | HS // US Subscribers Engaged 90D v2 | 82.821 | US-include alle sprintmails |
| XrFa5r | HS // INT Subscribers (non US) Engaged 90D v2 | 54.347 | INT-include alle sprintmails |
| R5rFrC | HS // No Country Subscribers Engaged 90D v2 | 16.326 | **niet** toevoegen: no-country zit al in VMjhb2 (geen of US-locale) of XrFa5r (niet-US locale) |
| RNuYDm / VdfJTJ / SBXxWs | US / INT / No Country Subscribers v2 (alle) | 114.506 / 77.642 / 26.721 | alleen voor einde-sale-dag, niet in de sprint |
| TntB6g / S9BZVJ | US / INT Engaged 180D v2 | 100.079 / 62.014 | niet in de sprint |
| VJkN42 / UbXDP6 / TqFRCn | oude US / INT / US-segmenten | 86.335 / 22.721 / 88.405 | niet meer gebruiken (v2 vervangt ze) |
| TNdhKc | EB [DG] Engaged 30 Days | 66.143 | E30, warmste groep (66.142 ervan zit in VMjhb2 of XrFa5r) |
| VKxqyA | HS // Engaged 90 Days (oud, zonder land) | 97.703 | niet gebruiken |

Na vaste uitsluitingen en Ur6Ehr: **US E90 = 77.805, INT E90 = 48.816.**

Uitsluitingen:

| ID | Naam | Profielen |
|---|---|---|
| VSnBnJ | Unsubscribe (Exclusion) | 12.888 |
| W3q7Zy | Bounced Emails | 3.124 |
| W4vNzF | For Suppression (60 d oud, 5+ ontvangen, nooit open/klik/site/order) | 6.721 |
| XTpfNG | Marked us as Spam | 4.170 |
| Ur6Ehr | Unengaged 180 Days, Non-Buyers | 25.565 (in VMjhb2 1.381, in XrFa5r 3.952 na uitsluitingen) |
| XY4NVp | Sunset Segment | 19.206 (in E90 maar 31; wel 6.543 slapende kopers) |
| WuHSm6 | v4 · Sunset · unengaged 120d | 88.626 (te breed, niet als uitsluiting) |
| XdK77b | v4 · Welcome protection | 15.848 (Homestead-kalender, niet nodig voor de sprint) |

Kopers en recentheid (Placed Order RSNxYV):

| ID | Naam | Profielen |
|---|---|---|
| U5Ksvk | All buyers | 104.031 (mailbaar na uitsluitingen 49.878: US 27.478, INT 22.400) |
| W92553 / SdCCdW / TLqivd / U45H9m / TriYPe | Purchased last 3 / 5 / 7 / 9 / 14 days | 1.946 / 2.696 / 3.525 / 4.041 / 5.377 |
| UfyDPs / Vnb28D | Bought last 30 / 60 days | 9.040 / 13.172 |
| WwHjkS | More than 1 purchase (all time) | 9.338 |
| TCQLcv / ThRYCu | 12-pcs / 6-pcs set buyers | 856 / (telt niet, definitie ontbreekt in de API-respons) |

Intentie: UmXcLi Product Viewers L30 (35.272), X9GUq4 L90 (73.146), VcDnvU 30 days ATC zonder order (7.600). Metric-aggregates 25 okt tot 8 nov: Checkout Started 7.036 unieke profielen, Added to Cart 8.957, Viewed Product 26.032; Active on Site 1 tot 8 nov 18.377. Er is **geen segment voor checkout-starters**; zie segment D.

Resend en lopend: VVWCHc / Vikk4d "Ressend 1 / November 2026 US / INTL" (47.690 / 46.401; ontvangen campagne, 0 opens). QZa2vQ (20), WdyATm AFF-inhaal (5.730), TZ8Cmj affiliates (351).

## 2. Kopers uitgesplitst (mailbaar, na uitsluitingen, 49.878)

| | US | INT |
|---|---|---|
| Order laatste 7 d (TLqivd) | 2.616 | 742 |
| 8 tot 30 d | 3.576 | 1.257 |
| 31 tot 60 d | 2.101 | 1.073 |
| Langer dan 60 d | 19.185 | 19.331 |
| In E90 (VMjhb2/XrFa5r) | 21.207 | 16.398 |
| Slapend (niet in E90) | 6.271 | 6.002 |
| 2+ orders (WwHjkS) | 2.622 | 2.499 |
| Historische CLV ≥ $400 | 3.916 | 2.829 |
| **VIP-top (2+ orders of CLV ≥ $400)** | **5.401** | **4.217** |

CLV-verdeling (alle 49.878): onder $150 18.498, $150 tot $300 20.838, $300 tot $500 6.115, $500+ 4.427. Markt bij kopers buiten E90 bepaald met dezelfde regel als v2 (land, anders locale).

## 3. Per mail

### Mail 1 FLASH ("24-hour flash deal ends tonight")

| | |
|---|---|
| Include US | VMjhb2 ∩ (niet-koper OF UmXcLi OF VcDnvU) = nieuw segment A-US |
| Include INT | idem op XrFa5r = A-INT |
| Exclusions | vast + Ur6Ehr + TLqivd (P7) + kopers van het flashproduct (als het een set is: TCQLcv/ThRYCu) |
| Grootte | US **60.133**, INT **34.246** |
| Waarom | Eén product extra scherp werkt het best bij wie nog geen Siraat heeft of net keek. E90-kopers zitten in VIP-WEEKEND; zij krijgen de flash alleen als die dag geen VIP-mail gaat (dan include = E90 min P7: US 75.212, INT 48.083). |
| Tijd | 16:00 UTC (calendar 12 en 19 nov), deadline 23:59 lokaal |

### Mail 2 VIP-WEEKEND ("VIP only: extra 10% on top, ends Sunday midnight")

| | |
|---|---|
| Include | segment B "SPRINT · Kopers · mailbaar" (US en INT apart via VMjhb2/XrFa5r **niet** als include gebruiken, want 12.273 slapende kopers vallen erbuiten; markt via segment B-US/B-INT op land/locale) |
| Exclusions | vast + TriYPe (P14, kochten net tegen de saleprijs) + holdout XN5G3M (als die gebruikt wordt voor de kopersreeks) |
| Grootte | US **23.507**, INT **21.332** (totaal 44.839); waarvan VIP-top 4.500 / 3.921 |
| Waarom | "VIP only" moet waar zijn: alleen mensen die al bij ons kochten, unieke code per profiel. E30-niet-kopers erbij (voorstel in urgentie.md) maakt het 91.800 en dan is "VIP" niet meer geloofwaardig. Als Floris toch breder wil: alleen E30-niet-kopers die in 30 d een product bekeken (US 17.092, INT 5.553), met eigen copy ("early access", niet "VIP"). |
| Personalisatie | VIP-top (segment C) krijgt een eigen variant ("you've ordered from us more than once"). Klaviyo kan in een template niet op segmentlidmaatschap testen, dus twee campagnes: C, en B min C. |
| Slapende kopers | 12.273 kopers zitten niet in E90, 6.543 daarvan in Sunset. Voor VIP-weekend 1 (13 tot 15 nov) alleen B ∩ (VMjhb2 ∪ XrFa5r) = US 17.278, INT 15.340; slapers pas in weekend 2 (26 tot 29 nov), wanneer de Thanksgiving-volumes de spamratio verdunnen. |
| Zondag 18:00 "laatste uren" | ontvangers mail 2, 0 kliks, geen order sinds verzending (segment E met $campaign = VIP-id); verwacht 40 tot 60% van de ontvangers. |

### Mail 3 CREDIT ("Your $X store credit expires tonight")

| | |
|---|---|
| Include | segment F "Points · balance > 0 · bf26": `rise_wallet_balance` > 0 OF `siraat_points` > 0, en `siraat_credit_cohort` = "bf26" |
| Exclusions | VSnBnJ, W3q7Zy, XTpfNG, holdout (`siraat_credit_cohort` = "holdout"). **Niet** W4vNzF/Sunset (plan store credit: ook slapers krijgen hun tegoed), wel spamstop 0,3%. |
| Grootte | nu **0** (geen Rise-velden in Klaviyo). Verwacht na upload: mailbare kopers 49.878 min 5% holdout = **~47.400** (US ~26.100, INT ~21.300) |
| Waarom | Alleen wie echt tegoed heeft; het bedrag komt uit het profiel. Iedereen die verzilvert valt eruit (saldo 0). Zonder Rise-sync en zonder import geen verzending. |
| Volgorde | Eerst de E90-kopers (37.605), 24 u later de slapers (12.273), zodat een slechte ontvangst van slapers de warme groep niet raakt. |

### Mail 4 LAST-HOURS resend (Benjamin, platte tekst)

| | |
|---|---|
| Include | per moedermail (FLASH, VIP, GIFTS of DRAW) segment E: ontvangen campagne X, geopend X ≥ 1, geklikt X = 0, Placed Order 0 in de laatste 1 dag |
| Exclusions | vast + Ur6Ehr + wie vandaag al een andere sprintmail kreeg (segment G) |
| Grootte | uit de rapporten 30 okt tot 8 nov: openers zonder klik = 30 tot 45% van de ontvangers (E4 US 73.288 ontvangers, 22.645 openers, 314 klikkers → 22.331). Op FLASH US 60k: ~20.000 tot 27.000; GIFTS US 75k: ~23.000 tot 31.000; INT ~15.000 tot 23.000. |
| Waarom | Opens zijn hoog (36 tot 49%), kliks onder 1%: deze groep leest maar heeft geen reden om nu te klikken. Apple MPP telt mee als open; dat maakt de groep groter (Floris wil dat). Variant met `machine_open = false` is kleiner maar niet via de API te tellen. |
| Tijd | dezelfde dag, 4 tot 6 u voor de deadline (bijv. 18:00 lokaal bij 23:59) |

### Mail 5 GIFTS ("Your 5 free gifts end tonight")

| | |
|---|---|
| Include | VMjhb2 (US), XrFa5r (INT) |
| Exclusions | vast + Ur6Ehr + TLqivd (P7) |
| Grootte | US **75.212**, INT **48.083** |
| Waarom | Gifts gelden voor iedereen; breedste mail. Op de laatste avond (30 nov) mogen de slapende kopers erbij (+12.273) als spam onder 0,15% bleef. Kopers P8 tot P30 blijven erin: tweede order krijgt ook gifts. |

### Mail 6 DRAW ("Order by Sunday midnight to enter this week's filter draw")

| | |
|---|---|
| Include | VMjhb2, XrFa5r |
| Exclusions | vast + Ur6Ehr + "Placed Order sinds maandag van die week" (in Klaviyo benaderd met TLqivd, P7: wie deze week al kocht doet al mee) |
| Grootte | US **75.212**, INT **48.083** |
| Waarom | Zelfde breedte als GIFTS, dus nooit op dezelfde dag als GIFTS. Alleen live met gepubliceerde trekkingsregels (BRIEF). |

## 4. Overlap en over-mailing

1. **Eén sprintmail per profiel per dag.** Prioriteit bij botsing: CREDIT > VIP > FLASH > GIFTS > DRAW. LAST-HOURS telt niet mee (gaat alleen naar openers van de moedermail van die dag).
2. Segment G "SPRINT · kreeg vandaag sprintmail" als uitsluiting in elke latere sprintcampagne van die dag (vereist dat alle sprintcampagnes in de naam "URG ·" krijgen).
3. Smart sending aan (16 u), behalve de LAST-HOURS-mail (moet dezelfde dag) en BF 27 en CM 30 nov.
4. Homestead-kalender: op een dag met een Homestead-lijstmail (E-reeks) de sprintmail alleen naar de groep die Homestead die dag niet mailt, of de sprintmail vervangt hem (afspraak met Homestead). Plan urgentie.md: L1-credit vervangt die avond een gewone BF-campagne voor kopers.
5. Wie kocht in 7 d krijgt geen FLASH/GIFTS/DRAW; wie kocht in 14 d geen VIP-code (anders "had ik maar gewacht"-klachten). Flows (cart, checkout) sluiten zichzelf al af bij order.
6. Cart/checkout-flow: uitsluiten wie in de laatste 1 uur een flowmail kreeg (Received Email met $flow ingesteld, 1 uur); zelfde regel als urgentie.md sectie 5.
7. Spamstop: boven 0,3% op 1.000+ ontvangers stoppen; voor INT bleef het 0,016 tot 0,044%.

## 5. Nieuwe segmentdefinities (klaar voor de API; niet aangemaakt)

Metric-ID's: Placed Order RSNxYV, Received Email YkRM4Q, Opened Email WyrTym, Clicked Email W247h8, Viewed Product XNtYMB, Added to Cart QXcV8K, Checkout Started RfMvni, Active on Site UdCdLD. Elke conditiegroep = EN, condities binnen een groep = OF.

**A-US "URG · Flash · US · niet-kopers + intentie"** (~60.100; INT-variant: VMjhb2 vervangen door XrFa5r, ~34.200):
```json
{"condition_groups":[
 {"conditions":[{"type":"profile-group-membership","is_member":true,"group_ids":["VMjhb2"]}]},
 {"conditions":[
  {"type":"profile-metric","metric_id":"RSNxYV","measurement":"count","measurement_filter":{"type":"numeric","operator":"equals","value":0},"timeframe_filter":{"type":"date","operator":"alltime"},"metric_filters":null},
  {"type":"profile-metric","metric_id":"XNtYMB","measurement":"count","measurement_filter":{"type":"numeric","operator":"greater-than","value":0},"timeframe_filter":{"type":"date","operator":"in-the-last","unit":"day","quantity":30},"metric_filters":null},
  {"type":"profile-metric","metric_id":"QXcV8K","measurement":"count","measurement_filter":{"type":"numeric","operator":"greater-than","value":0},"timeframe_filter":{"type":"date","operator":"in-the-last","unit":"day","quantity":30},"metric_filters":null}]},
 {"conditions":[{"type":"profile-metric","metric_id":"RSNxYV","measurement":"count","measurement_filter":{"type":"numeric","operator":"equals","value":0},"timeframe_filter":{"type":"date","operator":"in-the-last","unit":"day","quantity":7},"metric_filters":null}]}]}
```

**B "URG · Kopers · mailbaar"** (~49.900; campagne sluit P14 uit). B-US/B-INT: voeg de landgroepen van VMjhb2 resp. XrFa5r toe (zie definities in sectie 1, zonder de engagement-groep):
```json
{"condition_groups":[
 {"conditions":[{"type":"profile-marketing-consent","consent":{"channel":"email","can_receive_marketing":true,"consent_status":{"subscription":"any","filters":null}}}]},
 {"conditions":[{"type":"profile-metric","metric_id":"RSNxYV","measurement":"count","measurement_filter":{"type":"numeric","operator":"greater-than","value":0},"timeframe_filter":{"type":"date","operator":"alltime"},"metric_filters":null}]}]}
```
Landgroepen B-US (uit VMjhb2): groep 1 `location['country']` equals "United States" OF equals "US" OF not-set; groep 2 `$locale_country` not-set OF equals "US" OF country equals "United States" OF equals "US". B-INT (uit XrFa5r): country not-equals "United States" OF not-set; country not-equals "US" OF not-set; country is-set OF `$locale_country` not-equals "US".

**C "URG · VIP-top (2+ orders of $400+)"** (~9.600 mailbaar; US 5.401, INT 4.217):
```json
{"condition_groups":[
 {"conditions":[{"type":"profile-marketing-consent","consent":{"channel":"email","can_receive_marketing":true,"consent_status":{"subscription":"any","filters":null}}}]},
 {"conditions":[
  {"type":"profile-metric","metric_id":"RSNxYV","measurement":"count","measurement_filter":{"type":"numeric","operator":"greater-than","value":1},"timeframe_filter":{"type":"date","operator":"alltime"},"metric_filters":null},
  {"type":"profile-metric","metric_id":"RSNxYV","measurement":"sum","measurement_filter":{"type":"numeric","operator":"greater-than-or-equal","value":400},"timeframe_filter":{"type":"date","operator":"alltime"},"metric_filters":null}]}]}
```
(Telling hierboven met Klaviyo `historic_clv` ≥ 400; de som van $value is in de winkelvaluta en kan iets afwijken. Controleer de telling in de UI.)

**D "URG · Checkout-starters 14 d zonder order"** (ontbreekt nu; max. ~7.000 unieke profielen, mailbaar deel onbekend). Optioneel extra in FLASH en GIFTS, geen eigen mail (cart/checkout-flows lopen al):
```json
{"condition_groups":[
 {"conditions":[{"type":"profile-metric","metric_id":"RfMvni","measurement":"count","measurement_filter":{"type":"numeric","operator":"greater-than","value":0},"timeframe_filter":{"type":"date","operator":"in-the-last","unit":"day","quantity":14},"metric_filters":null}]},
 {"conditions":[{"type":"profile-metric","metric_id":"RSNxYV","measurement":"count","measurement_filter":{"type":"numeric","operator":"equals","value":0},"timeframe_filter":{"type":"date","operator":"in-the-last","unit":"day","quantity":14},"metric_filters":null}]}]}
```

**E "URG · Openers zonder klik · <campagne>"** (LAST-HOURS en VIP-zondag; vervang CAMPAIGN_ID, maak per campagne):
```json
{"condition_groups":[
 {"conditions":[{"type":"profile-metric","metric_id":"YkRM4Q","measurement":"count","measurement_filter":{"type":"numeric","operator":"greater-than","value":0},"timeframe_filter":{"type":"date","operator":"alltime"},"metric_filters":[{"property":"$campaign","filter":{"type":"string","operator":"equals","value":"CAMPAIGN_ID"}}]}]},
 {"conditions":[{"type":"profile-metric","metric_id":"WyrTym","measurement":"count","measurement_filter":{"type":"numeric","operator":"greater-than","value":0},"timeframe_filter":{"type":"date","operator":"alltime"},"metric_filters":[{"property":"$campaign","filter":{"type":"string","operator":"equals","value":"CAMPAIGN_ID"}}]}]},
 {"conditions":[{"type":"profile-metric","metric_id":"W247h8","measurement":"count","measurement_filter":{"type":"numeric","operator":"equals","value":0},"timeframe_filter":{"type":"date","operator":"alltime"},"metric_filters":[{"property":"$campaign","filter":{"type":"string","operator":"equals","value":"CAMPAIGN_ID"}}]}]},
 {"conditions":[{"type":"profile-metric","metric_id":"RSNxYV","measurement":"count","measurement_filter":{"type":"numeric","operator":"equals","value":0},"timeframe_filter":{"type":"date","operator":"in-the-last","unit":"day","quantity":1},"metric_filters":null}]}]}
```
Zelfde vorm als het bestaande VVWCHc (dat filtert op $campaign). Voor de VIP-zondagmail de open-groep weglaten (iedereen zonder klik).

**F "Points · balance > 0 · bf26"** (CREDIT; nu 0, verwacht ~47.400):
```json
{"condition_groups":[
 {"conditions":[
  {"type":"profile-property","property":"properties['rise_wallet_balance']","filter":{"type":"numeric","operator":"greater-than","value":0}},
  {"type":"profile-property","property":"properties['siraat_points']","filter":{"type":"numeric","operator":"greater-than","value":0}}]},
 {"conditions":[{"type":"profile-property","property":"properties['siraat_credit_cohort']","filter":{"type":"string","operator":"equals","value":"bf26"}}]},
 {"conditions":[{"type":"profile-marketing-consent","consent":{"channel":"email","can_receive_marketing":true,"consent_status":{"subscription":"any","filters":null}}}]}]}
```
Let op: `siraat_points` is een startwaarde; na verzilvering klopt alleen `rise_wallet_balance`. Zodra Rise synct, de `siraat_points`-conditie eruit.

**G "URG · kreeg vandaag sprintmail"** (uitsluiting, regel 4.2):
```json
{"condition_groups":[{"conditions":[{"type":"profile-metric","metric_id":"YkRM4Q","measurement":"count","measurement_filter":{"type":"numeric","operator":"greater-than","value":0},"timeframe_filter":{"type":"date","operator":"in-the-last","unit":"day","quantity":1},"metric_filters":[{"property":"Campaign Name","filter":{"type":"string","operator":"contains","value":"URG ·"}}]}]}]}
```

## 6. Open punten voor Floris

1. VIP-weekend: kopers zonder P14 (44.800), of breder met E30-kijkers (+22.600) onder een andere naam? Weekend 1 alleen E90-kopers (32.600)?
2. Nachtelijke sync `siraat_*` staat sinds 8 okt stil: herstarten, anders kloppen productuitsluitingen ("heeft al een Pan Pro") niet.
3. Rise-koppeling aanzetten of CSV-import met `siraat_points` en `siraat_credit_cohort`; tot dan is mail 3 niet te versturen.
4. SpBxrC controleren in de UI (definitie klopt, telling 0).
5. Bron: scripts en id-tellingen in de scratchpad (`seg/`), niet in de repo.
