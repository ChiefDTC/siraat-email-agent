# 08 · v5 stap 3: integratie (gedeelde onderdelen, tests, flowdefinities)

Datum: 8 oktober 2026. Agent, alleen lokaal. Klaviyo alleen gelezen (GET: segment WuHSm6, drie Placed Order-events). Niets geschreven in Klaviyo of Shopify, niets gecommit.

## 1. Wat er gedaan is

| # | Verzoek | Oplossing | Bestanden |
|---|---|---|---|
| 1 | V5-STRICT werkte alleen via tijdelijke meta-tags | `qa_render.py` leest V5-STRICT uit de topcomment van de **bron** (`is_strict`). Alle `<meta name="x-siraat-qa/x-siraat-build/siraat-qa">` uit 61 bronnen (en uit oude `.klaviyo.html`/previews) gehaald. Een zulke tag in de gebouwde mail is nu altijd FOUT. Rapport heeft een kolom V5-STRICT: 61/61 ja. | scripts/qa_render.py, 61 bronnen |
| 2 | cart-blok `$` alleen bij USD | `blocks/cart.html`: prijs alleen bij `presentment_currency == 'USD'`. De 8 inline kopieën (c1, c2, c2-acc, c3-acc, c3-p, c3-s, c4, c4-nocode) waren byte-gelijk aan het blok op pad/titel/regel na: teruggezet naar `{{BLOCK:cart pad title line}}` (uitkomst identiek). | partials/blocks/cart.html, 8 checkoutbronnen |
| 3 | about-blok marktveilig | Generator `make_product_blocks.py`: maten via `{{SIZE:28:both}}` enz. (US 11″ (28 cm), elders 28 cm, onbekend 28 cm (11″)); roasting pan-maten en gift card "$25 to $200" via `{{IF:US}}..{{ELSE}}..{{ENDIF}}` (elders "36 x 27 cm, 7 cm deep." en "Several amounts to choose from."); reviewlabels "Pan Pro Standard/Large/Small". `v5lib.SIZE_IN` kent nu 6 en 9 cm (zijhoogte deep pan, wok). | scripts/make_product_blocks.py, scripts/v5lib.py, blocks/about.html |
| 4 | offer-knop Outlook | `blocks/offer.html`: `v:roundrect` wit (#FFFFFF, tekst #321E1D, 320 x 54) met `<!--[if !mso]>`-fallback, zoals cta. QA-rapport: 0 keer "knop zonder VML". | partials/blocks/offer.html |
| 5 | xsell dubbele `?` | `v5lib.xrow`: na `?variant=`/`%3Fvariant%3D` sluit de UTM-staart aan met `&`/`%26`. Test in `v5_blocks.py` (elke xsell-link: hoogstens één query-start; en een eenheidstest per linkvorm). | scripts/v5lib.py, research/tailoring/test/v5_blocks.py |
| 6 | `mpcc` niet gebonden | Gebonden: `mpcc=person|lookup:'country_code'` in de profiel- en browse-binding (eigen ISO-veld, 47 tot 72% gevuld). Test: profiel met alleen `country_code` geeft per markt de juiste maat, verzendregel en gifts. | scripts/v5lib.py, v5_blocks.py |
| 7 | label noemt inches | `blocks/label.html`: "PAN PRO {{IF:US}}11″{{ELSE}}STANDARD{{ENDIF}}" (idem Large, Small). | via make_product_blocks.py |
| 8 | tests naar v5 | `matrix.py`: goes-eis vervangen door `data-xsell` in alle 22 mails met cross-sell, plus nieuwe harde controle "xsell biedt niets uit de order aan" (v5lib.XOWN). C3-routing gelijk aan build_flows. MUSTNOT "board bij standard/p3-pan" weg (plank is v5-kandidaat, 04-cross-sell 6.1). `mksamples.py`: Mini $99, Small $137, Standard $144, Large $149, set $299. `run_tests.sh`: $62.10/$120.60/"A second Pan Pro" vervangen door $99, $129.60, $144 en negatieve controles (deksel, schort, plank uit de order niet aangeboden). Geen controle verzwakt: US-only, siraat_owned, R017 en USD/inch buiten US blijven hard (v5_blocks, qa_render strict). | research/tailoring/test/{matrix.py,mksamples.py,run_tests.sh,v5_blocks.py} |
| 9 | export | `POOLS`: SK_ANNIV15_7D (vervangt SK_ANNIV10_7D, n2 gebruikt alleen 15). s3-kept/s4-kept heten "v4 · Sunset · kept · s3-kept/s4-kept". Manifest 61 regels, dry-run 61/61 klaar, 48 beelden te uploaden. | scripts/export_klaviyo.py, exports/manifest.csv |
| 10 | build_flows | zie 2. | scripts/build_flows.py |

## 2. Flowdefinities (scripts/build_flows.py)

- **Checkout**: `STARTER_TITELS` (Pan Pro Duo, Pro Duo, Pan Pro Kit, 2 Pans + 2 Lids) en `GROOT_SET_TITELS` (SET_TITELS zonder starters). C3-S = Items contains-any GROOT_SET (de $value ≥ 300-route is weg). C3-P = Items contains-any PANPRO+STARTER EN $value < 300 EN geen GROOT_SET. C4 = router c4 / c4-nocode (ongewijzigd).
- **Cart**: gecontroleerd, de flow doet niets met HI10 (geen enkele HI10-verwijzing in build_flows; K1/K2-templates hebben alleen nog HI10 in de topcomment).
- **Anniversary**: de flow verwijst niet naar een coupon (de template n2 doet dat, SK_ANNIV15_7D); alleen de couponlijst in het overzicht is bijgewerkt.
- **VIP**: router met eigen cooldown. Cooldown-tak (v1-nocode) alleen als CODE-mail in 30 dagen **EN** Placed Order in de laatste 45 dagen met `Discount Codes` niet leeg (dat is de trigger-order: flowfilter Placed Order = 2 all time, verzendfilter 0 orders in 14 dagen). Live-events bevestigen dat `Discount Codes` een lijst is (leeg zonder code) en `Total Discounts` een tekst "0.00". **Onbevestigd**: de API-operator `list / length-greater-than` (documentatie niet bereikbaar). Terugval: `--vip-cooldown=discounts` (Total Discounts > 0), dan `--vip-cooldown=none` (geen cooldown-split, iedereen V1 15%; past bij het besluit, enige risico is een tweede code vlak na een gebruikte). `--vip-cooldown=old` = oude gedrag.
- **Sunset**: S2-verzendfilter telt alleen Clicked Email met `Bot Click = false`. `--offline` gebruikt het bekende segment-ID WuHSm6.
- **Nieuw: v4 · Sunset · kept** (`sunsetkept`, sectie 6 van 06-sunset-kept): trigger Clicked Email met `$flow = v4 · Sunset` EN `Bot Click = false`; 30 minuten → S3-kept ("SUNSET-KEPT · S3", afzender Benjamin, Placed Order 0 sinds start); 4 dagen tot 09:00 → S4-kept (plus geen checkout-/cartmail in 3 dagen). Flowfilter: niet in deze flow in 365 dagen. Bouwvolgorde: na sunset.
- Dry-run (`--offline` en gewone GET-dry-run): **0 fouten in alle 13 flows**; alleen de 2 kept-templates ontbreken nog (worden door de export aangemaakt).

## 3. Wat de hoofdsessie in Klaviyo moet doen (na akkoord)

Alles vanuit `/tmp`, met `python3 -I`. `R=/home/user/siraat-email-agent`.

1. **QA-poort en templates**
   ```
   python3 -I $R/scripts/qa_render.py                                 # 61/61 groen
   python3 -I $R/scripts/export_klaviyo.py                            # dry-run 61/61 klaar
   python3 -I $R/scripts/export_klaviyo.py --live --i-am-sure --update   # 48 beelden uploaden, 59 PATCH, 2 nieuw (Sunset · kept)
   ```
   Daarna staan in `exports/live/templates.csv` ook `v4 · Sunset · kept · s3-kept` en `... · s4-kept`.
2. **Segment WuHSm6 bijwerken** (PATCH `/api/segments/WuHSm6`, zie sectie 4), vóór de sunset-flows.
3. **Flows opnieuw aanmaken.** De 12 bestaande v4-flows zijn Draft en hebben de oude routering (C3, VIP, S2). Verwijderen in Klaviyo (UI of `DELETE /api/flows/{id}`): VSqzNN, WNDDGi, SNwQWU, UshtNX, QWEdbK, TKPEVE, URcvwu, SLRQPi, YqCwrh, Spvjdq, Vhi3iH, WXiUkJ. Daarna `exports/live/flows.csv` leegmaken (bewaar als `flows-v4-oud.csv`): de flowfilters verwijzen via `$flow` naar ID's, en `--live` controleert dat elk ID in flows.csv nog bestaat met die naam. Dan in deze volgorde (elke stap schrijft het nieuwe ID in flows.csv, de volgende gebruikt het):
   ```
   for s in postpurchase levering checkout cart welcome browse vip winback anniversary site sunset sunsetkept ugc; do
     python3 -I $R/scripts/build_flows.py --live --only=$s || break; done
   ```
   Weigert Klaviyo bij `vip` de operator op Discount Codes: `python3 -I $R/scripts/build_flows.py --live --only=vip --vip-cooldown=discounts`, anders `--vip-cooldown=none`, en dan verder met winback. Controleer bij `sunsetkept` dat Klaviyo `$flow` als triggerfilter op Clicked Email en een vertraging van 30 minuten accepteert; terugval in de notitie van de flow (Campaign Name contains "SUNSET · S").
4. **Oude sunset S7V4a7**: uitzetten (Manual) op het moment dat v4 · Sunset live gaat, niet eerder; twee sunsets tegelijk geven vier afscheidsmails.
5. Optioneel: segment `v4 · Sunset · kept` (Clicked Email, $flow = nieuwe ID van v4 · Sunset, Bot Click = false, minstens 1 keer in 180 dagen).
6. Controle na de bouw: `python3 -I $R/scripts/build_flows.py` (GET-dry-run, 0 fouten, 0 ontbrekend). De couponcontrole meldt "geen": de API-key leest geen coupons; SK_ANNIV15_7D is volgens DECISIONS door Floris aangemaakt, even in de UI nakijken.

## 4. Nieuwe definitie segment WuHSm6 ("v4 · Sunset · unengaged 120d")

Huidige definitie (GET 8 okt): marketing toegestaan, Received Email > 7 in 120 d, Active on Site 0 in 120 d, Placed Order 0 in 180 d, Clicked Email 0 in 120 d (zonder botfilter). Nieuw: Clicked Email telt alleen menselijke klikken, en het profiel is ouder dan 120 dagen (plan 2.8).

```json
{"data": {"type": "segment", "id": "WuHSm6", "attributes": {"definition": {"condition_groups": [
  {"conditions": [{"type": "profile-marketing-consent", "consent": {"channel": "email", "can_receive_marketing": true,
     "consent_status": {"subscription": "any", "filters": null}}}]},
  {"conditions": [{"type": "profile-metric", "metric_id": "YkRM4Q", "measurement": "count",
     "measurement_filter": {"type": "numeric", "operator": "greater-than", "value": 7},
     "timeframe_filter": {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 120}, "metric_filters": null}]},
  {"conditions": [{"type": "profile-metric", "metric_id": "UdCdLD", "measurement": "count",
     "measurement_filter": {"type": "numeric", "operator": "equals", "value": 0},
     "timeframe_filter": {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 120}, "metric_filters": null}]},
  {"conditions": [{"type": "profile-metric", "metric_id": "RSNxYV", "measurement": "count",
     "measurement_filter": {"type": "numeric", "operator": "equals", "value": 0},
     "timeframe_filter": {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 180}, "metric_filters": null}]},
  {"conditions": [{"type": "profile-metric", "metric_id": "W247h8", "measurement": "count",
     "measurement_filter": {"type": "numeric", "operator": "equals", "value": 0},
     "timeframe_filter": {"type": "date", "operator": "in-the-last", "unit": "day", "quantity": 120},
     "metric_filters": [{"property": "Bot Click", "filter": {"type": "boolean", "operator": "equals", "value": false}}]}]},
  {"conditions": [{"type": "profile-property", "property": "created",
     "filter": {"type": "date", "operator": "not-in-the-last", "unit": "day", "quantity": 120}}]}
]}}}}
```

De laatste groep (profiel ouder dan 120 dagen) is niet tegen de API-documentatie gecontroleerd (niet bereikbaar). Weigert de PATCH die groep, stuur dan zonder de laatste groep en zet in de UI "Properties about someone · Created · is at least 120 days ago". Het effect is klein (Received Email > 7 in 120 dagen sluit nieuwe profielen al bijna uit); de botfilter is het belangrijke deel.

## 5. Eindstand controles (8 okt)

| Controle | Uitkomst |
|---|---|
| `python3 -I scripts/qa_render.py` (met browser, alle markten) | 61 mails, 61 groen, 0 FOUT, 61 V5-STRICT |
| `bash research/tailoring/test/run_tests.sh` | exit 0 (85 ok; matrix 472/0; v5-bouwstenen 3294/0; qa_render --static groen) |
| `python3 -I scripts/check_previews.py` | 0 problemen |
| `python3 -I scripts/export_klaviyo.py` (dry-run) | 61/61 klaar, 48 beelden te uploaden |
| `python3 -I scripts/build_flows.py --offline` en GET-dry-run | 13 flows, 0 fouten; 2 kept-templates nog te exporteren |

## 6. Open punten en risico's

- `person.Country` als Klaviyo-tag is nog niet bevestigd (01-markten sectie 1 punt 7: waarschijnlijk bestaat die niet; het land staat in `$country`/locatie). Door `mpcc` vallen profielen met `country_code` nu wel goed; de rest valt terug op "onbekend" (geen bedragen, cm met inch). Eén Klaviyo-preview op een echt profiel blijft nodig.
- VIP-operator en de segmentgroep "created" zijn onbevestigd (zie 2 en 4), elk met terugval.
- `goes`/`goes1` (oude cross-sell) zijn niet herzien en worden door geen mail meer gebruikt; `gifts.html` en `productcard.html` (v4) bevatten nog `$`, maar alleen binnen US-voorwaarden in de 4 + 11 mails die ze gebruiken (QA strict groen).
