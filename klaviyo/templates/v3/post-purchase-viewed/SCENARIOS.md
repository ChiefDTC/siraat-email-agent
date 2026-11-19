# PP viewed tailored · VIP15-PICKS (draft, 19 nov 2026)

Eén post-purchase upsell-mail, tailored op Viewed Product. Model van Floris: bovenaan de 12-Pcs set (alleen VS), daaronder wat de klant de afgelopen 30 dagen bekeek, nooit iets wat de klant al heeft (los of in een bundel). Alles DRAFT.

| Wat | ID |
|---|---|
| Hoofdflow (draft) | UUZr3e "PP viewed tailored · VIP15 (draft, 19 nov)" |
| Template (bibliotheek) | YyGsj3 "PP viewed tailored · VIP · TEST" (flowkopieën RSxshv, SqVeyJ, VnKWX5) |
| Tracker views (draft) | UFAa3W "PPV tracker · Viewed Product > ppv_vr" |
| Tracker bezit (draft) | WZzjKR "PPV tracker · Ordered Product > ppv_vr = 9" |
| Shopify-code | VIP15-PICKS (DiscountCodeNode 2371736961364), SCHEDULED start 2027-01-01, dus niet actief |
| Schema-profiel | zz-ppv-schema-20261119 (alleen external_id, geen e-mail, niet mailbaar; nodig omdat Klaviyo Update Profile alleen bestaande eigenschappen accepteert) |
| Figma | rij 1l, node 376:106 |
| Oude versie | flow TJn6qN (sets-only, 4 mails) staat draft en blijft ongebruikt; X6KkAM bestaat niet meer (door de vorige agent vervangen). Codes VIP15-SET12/-SET6 staan geparkeerd (2027) en zijn niet meer nodig. |

## 1. Bundel-inhoud (Shopify PDP "What's in the box", content/catalog/products.json, scripts/sync_owned.py)

| Bundel | Bevat |
|---|---|
| **Cookware Set 12-Pcs** ($649, alleen VS) | Pan Pro **Mini 8″, Small 10″, Large 12″**, 2-Qt en 3-Qt saucepan, 8-Qt stockpot, 6 deksels. **Niet** de Pan Pro Standard 11″ (28 cm). |
| 12-Pcs + FREE PIZZA STEEL | idem + Pizza Steel |
| Pan Set With Lids 6-Pcs ($299) | Mini 8″, Small 10″, Large 12″ + 3 deksels |
| 2 Pans + 2 Lids ($199 in Shopify, alleen VS) | Mini 8″ + Standard 11″ + 2 deksels |
| Cookware Set Pro ($479) | Standard 11″, Wok, Deep Pan, flipper, ladle |
| Complete Edition ($495) | Standard 11″, Wok, Deep Pan, Crêpe Pan |
| Full Hammered Pro Edition ($799) | Mini, Small (Medium), Standard, Large, elk met deksel, + 4 utensils |
| Just Everything Bundle 34-Pcs ($1,499, alleen VS) | de 12-Pcs + Roasting Pan, Wok, Deep, Crêpe, Pizza Steel + 4 boards, 4 utensils, pizza wheel, grill press, trivet, salt en pepper mill, 4 aprons. **Geen** Standard 11″, geen messen. |
| Pan Pro Duo ($229) | catalogus: Mini + Standard; Shopify-tekst: Small + Standard. Tegenstrijdig, dus beide als in bezit behandeld (veilig). |
| Pro Duo ($199) | Standard 11″ + flipper |
| Pan Pro Kit ($199) | Small 10″ + deksel + flipper |
| Cook & Prep ($199) | Standard 11″ + cutting board L |
| Pan Pro & Utensil Set ($249) | Standard 11″ + 4 utensils |
| Utensil Set Bundle ($149) | flipper, spatula, ladle, scooper |

**Let op voor Floris' voorbeeld**: "kocht 12-Pcs, bekeek de Hammered Pan Pro: niet tonen (zit in de 12-Pcs)". Dat klopt voor Mini, Small en Large, maar **niet voor de Pan Pro Standard 11″**: die zit niet in de 12-Pcs (en ook niet in de 34-Pcs). De mail volgt de echte inhoud en toont de Standard dus wel aan een 12-Pcs-koper (scenario s03), met de regel "11″. The pan Siraat started with." Wil Floris hem toch verbergen: in `_tools/ppv_catalog.py` bij `12-Pcs` `'std'` toevoegen en opnieuw bouwen.

## 2. Aanbiedbare producten (Shopify 19 nov, Viewed Product XNtYMB 20 okt tot 19 nov: 173.176 events)

Drempel voor een eigen blok: 500+ unieke kijkers in 30 dagen. Alle hieronder zijn actief; voorraadgetallen in Shopify staan voor bijna alles negatief (doorverkopen staat aan), dus geen voorraadfilter.

| Token | Product | Handle | US-prijs | Na 15% | Alleen VS | Unieke kijkers 30 d |
|---|---|---|---|---|---|---|
| hero | Cookware Set 12-Pcs | titanium-hammered-cookware-set | $649 (compare $2,047) | $551.65 | ja | 8.666 (+888 pizza-variant) |
| F | 6-Pcs (VS: kaart, rest: hero) | titanium-hammered-pan-set-with-lids-6-pcs | $299 (compare $997) | $254.15 | nee | 8.010 |
| L | Pan Pro Standard 11″ | original-siraat-100-pure-titanium-pan-with-hammered-pattern | $144 | $122.40 | nee | 41.609 |
| O | Pan Pro Mini 8″ | titanium-hammered-pan-pro-mini | $129 | $109.65 | nee | 5.340 |
| I | Pan Pro Large 12″ | titanium-hammered-pan-pro-large | $149 | $126.65 | nee | 3.757 |
| P | Deep Pan Pro | titanium-hammered-deep-pan-pro | from $119 | from $101.15 | nee | 3.034 |
| H | 2 Pans + 2 Lids | 2-pans-and-2-lids | $199 | $169.15 | ja | 2.274 |
| Q | Wok Pan Pro | titanium-hammered-wok-pan-pro | from $119 | from $101.15 | nee | 1.922 |
| N | Pan Pro Small 10″ | titanium-hammered-pan-pro-small | $137 | $116.45 | nee | 1.560 |
| R | Cutting Board (Anti-Microbial) | titanium-cutting-board-v2 | from $99 | from $84.15 | nee | 1.534 |
| E | Cookware Set Pro | titanium-hammered-cookware-set-pro | $479 | $407.15 | nee | 1.393 |
| D | Complete Edition | the-hammered-collection | $495 | $420.75 | nee | 1.381 |
| G | Roasting Pan | titanium-hammered-roasting-pan | $199 | $169.15 | ja (PLAYBOOK) | 1.185 |
| A | Just Everything 34-Pcs | the-just-everything-bundle-34-pcs | $1,499 | $1,274.15 | ja | 1.036 |
| K | Utensil Set Bundle | siraat-pure-titanium-utensils-bundle | $149 | $126.65 | nee | 831 |
| M | Crêpe Pan Pro | titanium-hammered-crepe-pan-pro | $139 | $118.15 | nee | 818 |
| B | Full Hammered Pro Edition | full-hammered-pro-edition | $799 | $679.15 | nee | 804 |
| J | Pizza Steel | titanium-hammered-pizza-steel | $149 | $126.65 | nee | 546 |
| C | Damascus 67 Layer Knife Set (8) | damascus-67-layer-knife-set-8-piece | $499 | $424.15 | ja (INT onbekend, [VRAAG FLORIS]) | 142, onder de drempel; opgenomen omdat Floris hem noemt en hij net nieuw is |

Niet opgenomen: Stainless Steel Lid (1.690, maat onbekend), oude Titanium Pan Pro (962, niet gehamerd), Cutting Board Bundle (530, valt onder board), Pan Pro Kit (438), Duo's (< 300), accessoires onder de 300.
Prijzen: Shopify-siteprijs vandaag. DECISIONS noemt hogere panprijzen (18 nov) en $249 voor 2+2; Shopify toont dat niet, dus de mail volgt Shopify. Compare-at alleen bij de bevestigde ankers (12-Pcs, 6-Pcs). Buiten de VS staan geen bedragen ("15% off with your code").

## 3. Regels in de mail

1. Land = verzendland van de order (`event.extra.shipping_address.country_code`). Onbekend telt als niet-VS.
2. Hero: VS = 12-Pcs; niet-VS = 6-Pcs (de 12-Pcs is daar niet te koop; de 6-Pcs is de best verkochte set buiten de VS en dezelfde keuze als BF-W1 van 19 nov). Hero valt weg als de klant die set al heeft (12-Pcs, 34-Pcs; voor de 6-Pcs ook Full Hammered Pro).
3. Kaarten: max 3, alleen producten met `ppv_vr_<key>` 1, 2 of 3. Volgorde: eerst emmer 1 (bekeken in de laatste ~3 dagen), dan 2 (3 tot 10 dagen), dan 3 (10 tot 30 dagen); binnen een emmer de hoogste prijs eerst. Alleen-VS-producten nooit buiten de VS.
4. Nooit tonen wat de klant heeft: `ppv_vr == 9` (tracker), plus vangnet op deze order (`event.Items`, ook bundels via hun inhoud) en `siraat_owned` (historie).
5. Geen hero en geen kaart: korte bedankregel zonder aanbod (komt zelden voor, de flow filtert dit grotendeels weg).

## 4. Scenario's (gerenderd met de Klaviyo template-render API op template YyGsj3, 12 van 12 goed)

| # | Kocht | Bekeek (emmer) | Land | In de mail |
|---|---|---|---|---|
| s01 | Pan Pro Standard | Wok (1), Deep (2) | VS | 12-Pcs hero, Wok, Deep Pan |
| s02 | 12-Pcs | Large (in set), Pizza Steel (1), messenset (2) | VS | geen hero, Pizza Steel, messenset |
| s03 | 12-Pcs | Standard 11″ (1), Pizza Steel (1) | VS | geen hero, Pizza Steel, Standard (zit niet in de set) |
| s04 | Mini | niets | VS | alleen 12-Pcs hero |
| s05 | 6-Pcs | Mini en Large (in bezit) | VS | alleen 12-Pcs hero |
| s06 | Standard | Wok (1), Deep (1), Pizza (2), Crêpe (3), Board (3) | VS | 12-Pcs hero, Deep, Wok, Pizza Steel (max 3) |
| s07 | Standard | Wok (2), 2+2 (1), 12-Pcs (1) | VK | 6-Pcs hero, Wok (geen VS-only, geen bedragen) |
| s08 | 34-Pcs | Wok (in bezit), Standard (1), messenset (3) | VS | geen hero, Standard, messenset |
| s09 | Standard + via Aftersell 12-Pcs | Deep (1), Large (in set) | VS | geen hero, Deep Pan |
| s10 | Standard | 6-Pcs (1), Roasting (1, VS-only) | onbekend | 6-Pcs hero, geen kaarten |
| s11 | Wok, eerder al 12-Pcs (alleen siraat_owned) | alleen Wok | VS | geen aanbod: bedankregel (flow stuurt dit pad meestal niet) |
| s12 | Deep Pan, tracker gemist (ppv_vr_dep = 1) | Deep, Wok (2) | VS | 12-Pcs hero, alleen Wok (vangnet event.Items houdt Deep weg) |

Renders: `tailored/renders/sNN-600.png` en `-390.png`, HTML in `tailored/sNN.html`, uitslag `tailored/results.json`. 31 unieke links, alle 200.

## 5. Techniek en waarom

- **Gekozen: tracker-flows die per product een getal op het profiel zetten, en één code-template die dat leest.** Een code-template ziet alleen het trigger-event (Placed Order) en het profiel, niet de Viewed Product-historie.
- **Afgevallen (a)** Klaviyo drag-and-drop "recently viewed" / product feeds: kan geen bundel-inhoud uitsluiten, geen eigen code per product en niet in onze code-templates (vaste header/footer).
- **Afgevallen (c)** Zaymo: recommendation rules kunnen "eerder bestelde producten" uitfilteren (10 laatste orders), maar niet de inhoud van een bundel (12-Pcs-koper zou de Mini nog zien). Dat breekt de kernregel.
- **Afgevallen** een nachtelijk script (zoals sync_owned): de routine "Siraat bezit-sync" vuurt elke nacht "SUCCEEDED", maar de state staat sinds 8 okt stil en profielen van na 8 okt hebben geen siraat_owned. Native flows zijn betrouwbaarder.
- Klaviyo Update Profile accepteert alleen **vaste waarden** (geen datum uit het event, getest via de API) en alleen **bestaande eigenschappen**. Daarom emmers (1/2/3/0) met wachttijden in plaats van datums, en een schema-profiel zonder e-mail dat de eigenschappen aanmaakt.
- **Placed Order mist Aftersell-regels** (gecontroleerd: order met Aftersell 12-Pcs toont in Placed Order alleen de Standard; Ordered Product XT7f8Z heeft de 12-Pcs wel, $699). Daarom draait de bezit-tracker op Ordered Product.

### Wat er bij livegang gebeurt

- **UFAa3W (Viewed Product)**: elk Viewed Product-event van een bekend profiel (nu ~170k per maand, ~70k profielen) loopt de flow in. Voor de 18 producten: staat `ppv_vr_<key>` op 9, dan niets. Anders `ppv_vr_<key>` = 1; na 73 uur = 2, na nog 169 uur = 3, na nog 481 uur = 0, telkens alleen als er sindsdien geen nieuwere view van dat product is en het niet in bezit is (de nieuwere view heeft zijn eigen pad). Zet geen e-mail, alleen deze eigenschap.
- **WZzjKR (Ordered Product)**: elke orderregel (ook Aftersell) zet `ppv_vr_<key>` = 9 voor het product en alles in die bundel (zie tabel 1). Eén keer per orderregel.
- **UUZr3e**: Placed Order, niet in deze flow in 30 dagen, wacht 2 dagen tot 09:00 (profieltijd). Bekeek in 30 dagen een aanbiedbaar product: mail. Anders VS zonder 12-Pcs/34-Pcs ooit: mail (alleen hero). Anders niet-VS zonder 6-Pcs/12-Pcs/34-Pcs/Full Hammered Pro: mail. Anders niets. Mailfilter: geen mail uit X3ySuU in de laatste dag. Smart sending uit.
- **Belangrijk**: een tracker ziet alleen views en orders vanaf livegang. Eenmalig vullen (voor livegang van UUZr3e): script dat de Viewed Product-events van de laatste 30 dagen per profiel leest (zoals `scratchpad/ppv2/views.py`, ~13 min) en per product de emmer zet (1/2/3 op leeftijd van de laatste view), plus 9 uit `siraat_owned` en uit Ordered Product-historie, via een bulk profile import van alleen de `ppv_vr_*`-velden. Daarna de bezit-sync repareren of vervangen.

## 6. Livegang (pas als Floris het zegt)

1. Floris keurt copy, de Standard-in-12-Pcs-keuze, messen buiten de VS en de prijzen.
2. Trackers WZzjKR en UFAa3W live zetten (eerst).
3. Eenmalige backfill draaien (zie 5) en een steekproef van 20 profielen controleren.
4. Shopify VIP15-PICKS: start = nu, eind 2026-12-01T04:59Z (ma 30 nov 23:59 ET; dat staat in de mail).
5. Testmail naar een intern profiel, dan in UUZr3e de drie mails op live en de flow live.
6. Op 1 dec flow UUZr3e uit (de mail noemt een vaste einddatum). Herinnering: geen flowstap (Klaviyo kan niet wachten tot een vaste datum); voorstel een campagne op zo 29 nov naar "kreeg PPV tailored, geen order sinds".

## 7. Wijziging 19 nov avond (Floris)

- UUZr3e: wachttijd nu **5 minuten** na Placed Order (was 2 dagen tot 09:00). Mailfilter "geen mail uit X3ySuU in 1 dag" vervangen door "geen mail met Campaign Name VIP15 in 1 dag" (geen dubbele upsell met v5 Ukz7F9). Hero-splits op Ordered Product 12-Pcs/34-Pcs/6-Pcs/Full Hammered Pro blijven (dekken Aftersell). Preview en copy: "Thanks for your order" in plaats van "your order is on its way".
- Hero-beelden nu Photoroom-uitsnede met harde schaduw: assets/ppv-set12-hard.jpg en ppv-set6-hard.jpg (`_tools/make_img_hard.py`). YyGsj3 en flowkopieën RSxshv, SqVeyJ, VnKWX5 bijgewerkt; 12 van 12 scenario's goed.
