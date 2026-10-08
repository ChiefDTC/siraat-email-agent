# 04 · Cross-sell in post-purchase, levering, winback, VIP en anniversary (ontwerp, fase 1)

Stand 8 oktober 2026. Vraag van de eigenaar: "waarom zit er nog geen cross-sell in post-purchase; cross selling, cross selling", en VIP/winback mogen nooit iets aanbieden dat de klant al heeft (feedback Floris, `00-feedback-floris.md`).
Alleen gelezen: Placed Order-events 7 okt 2025 t/m 7 okt 2026 (90.470 orders, 81.869 profielen; profiel-ID's alleen in de scratchpad, hier alleen aggregaten), Ordered Product (XT7f8Z, alleen veldnamen), Shopify-producten (prijzen en inhoud vandaag). **Geen templates gewijzigd, niets in Klaviyo of Shopify aangemaakt, niet gecommit.** Alle Django hieronder is een voorstel; het prototype staat in de scratchpad en is lokaal met Django 4.2 getest (sectie 6.3).

## Kort

1. **Er zit wel cross-sell in, maar hij biedt aan wat de klant al heeft.** Het huidige `goes`/`goes1`-blok kijkt alleen naar de eerste categorie in de order. Gerenderd: Standard + Mini krijgt de Mini aangeboden, Small + Mini de Mini, Large + Small de Small, de fall-sale-set (Mini, Small, Large + 3 deksels) de Small, 6-Pcs + plank de plank, schort + molens de schort, deep + wok wordt "your set". R2 en N2 tonen statisch Pan Pro 11″ en de 6-delige set aan iedereen, ook aan wie ze heeft. V1 (VIP) ziet alleen order 2, niet order 1.
2. **Kooppatroon (12 maanden, 180 dagen volgen):** de volgende order is een tweede, kleinere maat, een deksel, een plank of een tweede vorm. Small → Mini 39% van de herhalers, Standard → Mini 20%, Large → deksel 19%, Mini → Standard 26%. Mediaan 28 tot 30 dagen tot de volgende order, p25 14 dagen. 3e order: deksel 22%, Mini 15%, plank 14%.
3. **Mechaniek in drie lagen:** (1) nu al: alles uit de trigger-order uitsluiten in de template; (2) nieuw: één Klaviyo-flow op Ordered Product die per regel een profielvlag `own_<token>` zet (incl. deksel- en dieptematen), plus eenmalige backfill, zodat V1, R1, R2 en N1/N2 ook eerdere orders kennen; (3) flow-splits op Ordered Product-historie alleen voor mails met één hoofdproduct (P3-pan: heeft al een 28 cm-deksel → p3-next).
4. **Moment:** P1 en P2 alleen één rustige regel (deksel in jouw maat, geen code), P3 (dag 20) is de cross-sell-mail, R1/R2, V1, N1/N2 elk een bezitsbewust blok van 2 tot 3 kaarten. U1 en review: niets.
5. **Aanbod:** P3 eigen 10% (14 d, bestaat), R1 HI10, R2 10%/15% (72 u), V1 **15% exclusive** ("You're a VIP customer"), N2 **15%** (Floris; nu 10% in de flow), plus de fall-sale-set **3 pans + 3 lids $299** als upgradekaart, alleen voor wie Mini, Small en Large nog niet heeft (dus vooral Standard-, vorm- en pottenkopers). US-only (12-delige set, potten, roasting pan) alleen bij verzendland US.

---

## 1. Data en methode

- Bron: Klaviyo Placed Order (RSNxYV), `Items` (producttitels), tijd, land. Gratis regels (gifts, "(100% off)", E-Guide, giveaway, Shipping Protection) en componentregels van bundels ("(Copy)", "(12PC)") genegeerd. "Titanium Utensil" (losse spatel) zit vaak gratis in de order (73% samen met trivet): telt niet als bezit van de Utensil Set.
- "Volgende order" = eerste order van hetzelfde profiel meer dan 1 uur later. Kans = aandeel van alle orders met product X (tot 10 april 2026, dus minstens 180 dagen kijktijd) waarbij de volgende order binnen 180 dagen Y bevat. "Van herhalers" = aandeel binnen de volgende orders. Sets en schort zijn pas sinds mei tot juli 2026 groot: daar 60 dagen kijktijd en vooral de samen-in-één-order-cijfers.
- Venster is 12 maanden, dus de mediaan (28 tot 30 dagen) ligt lager dan de 35 dagen uit `personalisatie/01-voorstel.md` (langer venster, eerste orders). Beide kloppen voor hun cohort.
- 34% van de herhaalorders bevat een categorie die de klant al had (21% alleen al-bezeten: Standard → Standard 30% van de Standard-herhalers, molens 58%, planken 25%). Dat zijn vaak cadeaus en tweede keukens. De regel "nooit aanbieden wat je al hebt" kost dus iets, maar Floris wil hem; we tonen dezelfde maat wel als P.S.-regel ("Cooking for someone else too? Reply and we will set up a gift") en niet als kaart.

## 2. Cross-sell-matrix

Eerste getal = kans dat de volgende order binnen 180 dagen Y bevat en Y nog in geen eerdere order zat ("nieuw"), van alle orders met dat product. Tussen haakjes: aandeel van de volgende orders met Y (ook al-bezeten) en mediane dagen. Samen = aandeel van de orders met X waarin Y ook zat (zelfde order).

| Gekocht | n orders | Herhaalt 180 d (mediaan) | Top 3 volgende aankoop (nieuw voor de klant) | Samen in één order | Beste accessoire-pasvorm |
|---|---|---|---|---|---|
| Pan Pro Standard 11″ | 42.143 | 7,7% (28 d) | Mini 1,4% (20%, 29 d) · plank 1,2% (18%, 26 d) · Small 1,1% (15%, 34 d); deksel 1,0% (15%, 39 d) | deksel 12%, utensil 11%, wok 11%, Large 10%, deep 10%, plank 9% | **deksel 28 cm**, Mini, plank, deep. Fall-sale-set (heeft geen 11″) |
| Pan Pro Large 12″ | 22.683 | 8,1% (30 d) | Mini 1,3% (17%) · Standard 1,3% (26%, 24 d) · plank 1,3% (17%); deksel 1,6% (19%, 34 d) | **deksel 20%**, Standard 19%, Small 11% | **deksel 30 cm**, Small, Standard, plank |
| Pan Pro Small 10″ | 11.465 | 10,1% (28 d) | **Mini 3,7% (39%, 24 d)** · deksel 1,4% (19%, 30 d) · plank 1,3% (14%, 23 d) | Standard 24%, deksel 23%, Large 22% | **Mini**, deksel 26 cm, plank, wok |
| Pan Pro Mini 8″ | 7.829 | 9,8% (28 d) | **Standard 2,5% (26%, 20 d)** · plank 1,5% (18%, 30 d) · wok 1,4% (15%, 25 d) | Standard 45%, deksel 24%, Small 19% | Standard, deksel 20 cm, plank, wok |
| Deep Pan Pro | 9.107 | 10,4% (29 d) | Mini 1,7% (18%, 36 d) · plank 1,6% (19%, 28 d) · deksel 1,5% (20%, 49 d) | Standard 46%, **wok 43%**, crêpe 26% | wok, Mini, plank, Utensil Set; deksel alleen 20/26/28/30 cm (24 cm heeft er geen) |
| Wok Pan Pro | 8.244 | 9,8% (32 d) | Mini 1,9% (20%, 26 d) · plank 1,6% (20%, 30 d) · deksel 1,4% (19%, 38 d) | Standard 54%, **deep 48%**, crêpe 30% | deep, Mini, plank, Utensil Set |
| Crêpe Pan Pro | 5.958 | 10,4% (29 d) | plank 1,6% (17%) · deksel 1,5% (17%, 27 d) · Mini 1,4% (15%) | Standard 44%, wok 41%, deep 40% | Standard, plank, Utensil Set (spatel eronder) |
| Pizza Steel | 1.428 | 13,3% (33 d) | Standard 1,9% (18%, 27 d) · plank 1,7% (18%, 31 d) · deksel 1,7% (20%, 45 d) | Standard 9%, plank 8%, crêpe 7% | plank (Large), Standard, crêpe |
| Snijplank | 9.775 | 8,9% (30 d) | Mini 1,2% (15%, 34 d) · deksel 1,0% (16%, 39 d) · wok/deep 1,0% | Standard 37%, Large 14%, deksel 14% | Standard, Mini, Utensil Set, Non Slip Mat |
| Deksel (alleen) | 12.247 | 10,6% (28 d) | Mini 1,8% (18%, 20 d) · Small 1,5% (17%, 24 d) · plank 1,5% (16%, 30 d) | Standard 42%, Large 37%, Small 22% | Mini of Small (tweede pan), plank |
| Utensil Set Bundle | 2.372 | 13,4% (32 d) | Mini 2,0% (17%, 52 d) · plank 1,7% (22%, 16 d) · wok 1,5% | Standard 35%, deksel 32%, plank 29% | plank, Mini, deep, wok |
| Schort | 1.169 | 7,9% (60 d-venster, 17 d) | plank 1,1% · Mini 1,0% · deksel 1,0% | Standard 41%, deksel 35%, Large 28% | molenset (cadeauduo), plank, Standard |
| Molens | 573 | 10,7% (60 d) | molens opnieuw 58% van de herhalers (cadeau) · plank 1,0% · Standard 0,7% | plank 14%, deksel 9%, Utensil Set 9% | plank, schort, Standard |
| Fall-sale-set / Pan Set With Lids 6-Pcs (Mini, Small, Large + 3 deksels) | 825 | te nieuw (sinds mei) | n te klein; eerste herhalers: molens, Utensil Set, plank | **Utensil Set 12%, plank 10%, schort 10%**, wok 7% | **Standard 11″** (zit er niet in), Utensil Set, plank, deep/wok |
| Pot Set 6-Pcs (US) | 713 | 8,7% (60 d) | plank 1,9% · Utensil Set 1,6% · pizza 1,3% | **Pan Set 6-Pcs 60%**, Utensil Set 17%, schort 16% | Pan Set (als die ontbreekt), Standard, plank |
| 12-delige set (US) | 169 | te nieuw | geen | Utensil Set 11%, plank 11%, pizza 5% | Standard 11″ (zit er niet in), Utensil Set, plank, crêpe |
| Cookware Set Pro / Complete (pan, wok, deep) | klein | n.v.t. | n.v.t. | n.v.t. | deksel 28 en 26 cm (geen deksels in de set), plank, crêpe, Mini |
| Roasting Pan (US) | 30 | n te klein | n.v.t. | n.v.t. | plank (Large), Large, Utensil Set |
| Dishwasher sheets | 158 betaald | n te klein | n.v.t. | Standard 30% | geen kaart: abonnement na de gift (BACKLOG 6) |

Derde order (1.132 profielen, mediaan 18 dagen na order 2): deksel 22% (nieuw 13%), Standard 15%, Mini 15% (nieuw 13%), plank 14% (nieuw 9%), Small 12%, deep 12%, Utensil Set 8%.

**US-only, bevestigd in de data:** Pot Set 702 van 713 orders US, losse potten 61/61, roasting pan 30/30, 12-delige set 147 van 169 (rest: profielland ≠ verzendland). Deze kaarten alleen bij `event.extra.shipping_address.country_code == 'US'` (Placed Order) of `person.Country` (profiel), nooit als terugval.

**Fall sale (Floris, vanaf vandaag):** Shopify toont "Titanium Hammered Pan Set With Lids | 6-Pcs" ACTIVE op **$299** (inhoud Mini 8″, Small 10″, Large 12″, elk met deksel). Dezelfde titel als de oude 6-delige set, dus de routing (`Pan Set With Lids`) werkt al. In de mails staan nog $349 (R2, N2, V1, A2, P3-accessory) en Pan Pro 11″ $134 (Shopify vandaag $144, Small $137): prijzen in kaarten uit één bron halen, niet hardcoden. **[VRAAG FLORIS]** prijs Standard en einddatum fall sale.

## 3. Wat er nu misgaat (gerenderd, `goes.html` met Django)

| Order | Toont nu | Fout |
|---|---|---|
| Standard + Mini | Mini, deksel 28 | Mini zit in de order |
| Small + Mini | Mini, deksel 26 | idem |
| Large + Small | Small, deksel 30 | Small zit in de order |
| Fall-sale-set (Small, Large, Mini, deksel als losse titels) | Small, plank | Small zit in de order |
| 6-Pcs + plank | plank, schort | plank zit in de order |
| Standard + deksel + plank | Mini, plank | plank zit in de order |
| Schort + molenset | schort, plank | schort zit in de order |
| Deep + wok (los) | plank, schort, "your set" | token `Wok & Deep` matcht twee losse producten |
| V1 (order 2 = deksel, order 1 = Standard + Mini) | Mini (via 'lid'-categorie) | V1 ziet order 1 niet |
| R2, N2 | Pan Pro 11″, 2 Pans + 2 Lids, 6-delige set ($349) | statisch, ook voor eigenaars; prijs set klopt niet meer |

## 4. Uitsluiting: exacte Klaviyo-mechaniek

### Laag 1 · trigger-order (kan nu, geen nieuwe objecten)
- Alle mails met een Placed Order-trigger (P1, P2-safe, P3, R1, R2, V1, N1, N2) hebben `event.Items` en `event.extra.line_items[]` (titel, `variant_title`, `line_price`). Het blok zet per token een bezitsvlag uit de titels (sectie 6), inclusief wat een set impliceert (6-Pcs = Mini, Small, Large, deksels 20/26/30; Cookware Set Pro = Standard, wok, deep; Pan Pro Duo = Small + Standard).
- Deksel in de order zonder maat in `Items`: aangenomen dat hij past op de pan(nen) in dezelfde order (de data: 12 tot 24% neemt het deksel bij de pan). Exacte maat komt uit laag 2.
- **Beperking:** de levering-flow (P2, trigger Delivered Shipment) heeft geen `Items`; daar alleen laag 2.

### Laag 2 · eerdere orders als profielvlaggen (nieuw, nodig voor VIP, winback, anniversary)
Templates zien geen segmenten en geen historie, wel profielvelden (`person|lookup:'own_mini'`).
1. **Eén flow "v4 · Bezit"**, trigger **Ordered Product (XT7f8Z)**, trigger filter `$value` greater than 0 (sluit gifts uit). Geen flow filter (elke regel telt). Elk event is één orderregel, dus één tak per regel: trigger splits op `Name` (contains "Pan Pro Mini", "Pan Pro Small", ... ) en voor deksels en deep pan op `Variant Name` (contains "20CM", "26CM", "28CM", "30CM"). Elke eindtak: actie **Update profile property** `own_<token>` = `true` (bundels: meerdere acties achter elkaar, bijv. 6-Pcs zet `own_mini`, `own_small`, `own_large`, `own_lid20`, `own_lid26`, `own_lid30`). Tokens: `mini, small, std, large, deep, wok, crepe, lid20, lid26, lid28, lid30, board, utset, apron, mill, pizza, pot, roast`.
   Ordered Product vuurt gelijk met Placed Order; P1 komt na 1 uur, dus de vlag staat er (voor P1 is laag 1 genoeg).
2. **Backfill** (eenmalig): per token een segment "Ordered Product where Name contains X (en Variant Name contains Y) and $value > 0 at least once over all time", exporteren en terug importeren met kolom `own_<token>` = true (Klaviyo UI, of API bulk import met een schrijfsleutel). Omvang in 12 maanden: Standard 41.064 profielen, Large 22.320, deksel 11.768, Small 11.246, plank 9.493, deep 8.878, wok 8.095, Mini 7.698, Utensil Set 2.335, pizza 1.389, schort 1.152, set 817, pot set 704. Ouder dan 12 maanden: Placed Order loopt terug tot november 2024, zelfde segmenten.
3. Waarom niet Shopify-tags: kan ook (Shopify Flow "Order created → add customer tag own-mini", Klaviyo synct "Shopify Tags" naar het profiel, template `'own-mini' in person|lookup:'Shopify Tags'|default:''|join:','`), maar dat is schrijven in Shopify. Alleen na akkoord van Floris; het blok in sectie 6 werkt met beide (één regel verschil).
4. **[VRAAG FLORIS]** "Update profile property" in een flow lukte niet via de API (bouwnotitie 2.1): de flow wordt in de UI gebouwd.

### Laag 3 · flow-splits voor mails met één hoofdproduct (kan nu)
- **P3-pan**, vóór de router: conditional split "Ordered Product where Name contains 'Stainless Steel Lid' and Variant Name contains '28CM' at least once over all time" alleen voor Standard-orders (idem 30CM/Large, 26CM/Small, 20CM/Mini). JA → **p3-next** (tweede pan, plank). Zo krijgt niemand een deksel-hoofdmail voor een deksel die hij al heeft, ook zonder laag 2.
- **P3-set**: split "Ordered Product where Name contains 'Crêpe' over all time" → hoofdkaart wok in plaats van crêpe.
- Verzendfilters blijven zoals in v4 (Placed Order zero times since starting this flow, Refunded Order = 0).

## 5. Ontwerp per mail

Volgorde bij mediane levering (v4 3.10): P1 dag 0, P2 levering + 1 (~dag 13), U1 levering + 4, P3 dag 20, review levering + 14, R1 dag 45, R2 dag 75, N1 dag 182, N2 dag 365; VIP: order 2 + 30 (V1), + 40 (V2).

| Mail | Moment | Cross-sell-blok | Aanbod | Uitsluiting | Waarom (data) |
|---|---|---|---|---|---|
| **P1-first / P1-repeat** | order + 1 u | Eén regel onder het orderoverzicht, alleen als de order een Pan Pro **zonder** deksel heeft: "Your 11″ takes the 28 cm lid." met link naar de juiste variant. Geen kaart, geen code, geen prijs buiten US | geen (gifts en verzending gelden al voor elke order) | laag 1 | 12 tot 23% neemt het deksel al bij de pan; wie het vergat, krijgt de maat zonder te zoeken. Bevestiging blijft bevestiging |
| **P2 (levering) en P2-safe** | levering + 1 / dag 16 | In de eerste-ei-gids één tipregel: "For a set yolk on top, cover the pan for the last minute." en alleen bij geen deksel: "No lid yet? Your 11″ takes the 28 cm." | geen | P2: laag 2 (`own_lid28`), anders regel weg. P2-safe: laag 1 + 2 | 25% van de herhaalorders valt vóór dag 14; dit is service, geen verkoop |
| **U1, review** | levering + 4 / + 14 | geen | | | vraagt al iets van de klant |
| **P3-pan / P3-next / P3-set / P3-accessory / P3-apron** | dag 20 | De cross-sell-mail. Hoofdkaart per categorie (sectie 2: deksel in jouw maat, Mini bij Small, Standard bij Mini/set) plus 1 tot 2 rijen "What [Small] owners add next", allemaal niet in bezit. Bij Standard-, vorm- en potkopers zonder Mini/Small/Large: fall-sale-kaart | **eigen 10%, 14 dagen** (P3_THANKYOU_10_14D, bestaat) | laag 1 + 3 (laag 2 zodra live) | dag 20 ligt net vóór de mediaan (28 d) en vóór de deksel-mediaan (30 tot 39 d) |
| **R1-pan / R1-set / R1-acc** | dag 45 | Blok "What to add next", 2 rijen + fall-sale-kaart (regels zoals P3). Vervangt de vaste roasting-pan-kaart door de bezitsbewuste rij (roasting alleen US, en alleen bij Large/set-kopers) | HI10 in de links | laag 1 + 2 | 57% van de herhaalorders binnen 45 dagen; wie nu niets kocht, mist de eerste stap |
| **R2 / R2-VIP** | dag 75 | De drie statische kaarten (Pan Pro 11″, 2 Pans + 2 Lids, 6-delige set) worden: kaart 1 = eerste vrije kandidaat, kaart 2 = tweede, kaart 3 = fall-sale-set of, als die in bezit is, Utensil Set | eigen **10%** / **15% exclusive** (VIP), 72 uur | laag 1 + 2 | statische kaarten raken nu ook eigenaars |
| **V1 / V1-nocode** | order 2 + 30 | Kop (Floris): **"You're a VIP customer. 15% off, get it now."** Blok "Picked for your kitchen", 3 rijen uit het derde-orderpatroon: deksel in een maat die ontbreekt, Mini of Small, plank, Utensil Set, deep/wok. Geen care-video (feedback Floris) | **eigen 15% exclusive, 14 d** (SK_REGULARS15_14D) | **laag 2 verplicht** (order 1 is niet in het event); tot laag 2 live is: laag 1 + split "Ordered Product contains X over all time" alleen voor de hoofdkaart | deksel 22%, Mini 15%, plank 14% van de derde orders |
| **V2** | order 2 + 40 | geen blok (tekst van Benjamin). P.S. mag: "Cooking for someone else? Reply and we will help you pick." | | | |
| **N1** | dag 182 | Service-mail: 2 rijen "Still on our list for your kitchen", onderaan | HI10 | laag 1 + 2 | rustig; N1 is service |
| **N2 / N2-nocode** | dag 365 | 3 kaarten zoals R2 | **15% exclusive, 7 d** (Floris: anniversary 15%; pool nu SK_ANNIV10_7D, nieuwe pool `SK_ANNIV15_7D` nodig) | laag 1 + 2 | |
| **Levering-flow (2.5b)** | | = P2 | | | |

Uitgangspunten voor elk blok:
- Nooit iets tonen dat in bezit is (laag 1 + 2). Dezelfde maat opnieuw (30% van de Standard-herhalers) alleen als tekstregel "Cooking for someone else too?", nooit als kaart.
- Nooit een gift-product of $0-regel (feeds niet als hoofdblok, `personalisatie` 1.4).
- Prijs alleen bij verzendland US (`event.extra.shipping_address.country_code == 'US'`; zonder adres `person.Country`). Internationaal: geen prijs, wel "Your code works on these too."
- Code in de link via de bestaande `pre`/`post` (zelfde code als de rest van de mail; P3, R2, V1, N2 eigen code; R1 en N1 HI10).
- Maten buiten de US in cm eerst ("28 cm lid for your 11-inch pan"); in de US inch eerst. Maatnotatie volgt de besluiten van de maten-agent.

## 6. Blokspec `xsell`

### 6.1 Data, kandidaten en terugval

Per categorie (eerste match in de order, zelfde volgorde als `make_product_blocks.py`) een vaste lijst van 4 kandidaten. Het blok toont de eerste 2 die niet in bezit zijn; P3 toont 1 rij naast de hoofdkaart, R2/N2 3 kaarten.

| Categorie | Kandidaten (volgorde) | Kop (Engels) | Datazin (Engels, alleen waar de data het draagt) |
|---|---|---|---|
| Standard | lid28, Mini, plank, deep | What 11″ owners add next | One in five 11″ owners comes back for the Mini. |
| Large | lid30, Small, Standard, plank | What Large owners add next | One in five Large owners adds the lid next. |
| Small | Mini, lid26, plank, wok | What Small owners add next | One in three Small owners comes back for the Mini. |
| Mini | Standard, lid20, plank, wok | What Mini owners add next | One in four Mini owners comes back for the 11″. |
| Deep | wok, Mini, plank, Utensil Set | Goes with your deep pan | The deep pan and the wok are the pair most often bought together. |
| Wok | deep, Mini, plank, Utensil Set | Goes with your wok | idem, omgekeerd |
| Crêpe | Standard, plank, Utensil Set, wok | Goes with your crêpe pan | |
| Pizza steel | plank, Standard, crêpe, Utensil Set | Goes with your pizza steel | |
| Roasting pan (US) | plank, Large, Utensil Set, Standard | Goes with your roasting pan | |
| Pot / Pot Set (US) | fall-sale-set, Standard, plank, Utensil Set | Now the pans | |
| Fall-sale-set / 6-Pcs | Standard 11″, Utensil Set, plank, deep | The one size your set does not have | The 11″ is the size most kitchens start with. |
| 12-delige set (US) | Standard 11″, Utensil Set, plank, crêpe | Goes with your set | |
| Set Pro / Complete / Duo | lid28, plank, crêpe, Mini | Goes with your set | |
| Plank | Standard, Mini, Utensil Set, deep | Goes with your board | One in five board owners adds the 11″ pan. |
| Deksel | Mini, Small, plank, deep | Goes with your lid | |
| Utensils | plank, Mini, deep, wok | Goes with your utensils | |
| Molens | plank, schort, Standard, Utensil Set | Goes with your mills | |
| Schort | molenset, plank, Standard, Mini | Goes with your apron | |
| Sheets | Standard, plank, Mini, deep | (geen kop: abonnementsflow) | |

Fall-sale-kaart (apart, onder het blok): alleen als `own_mini`, `own_small` en `own_large` alle drie leeg zijn. Kop "Every other size, in one box", regel "Mini, Small and Large, each with its own lid." Prijs alleen US: "$299". Geen doorgestreepte prijs tot Floris de compare-at als anker bevestigt (PLAYBOOK).

**Terugval** (alles in bezit of geen categorie): geen productkaarten, maar één regel "Already have the full line-up? Reply and tell us what you cook most. We will point you to the right next piece." (bestaat al in P3-set). Geen feed als terugval (kan gifts tonen).

### 6.2 Beelden per product (echte productfoto's, kopieën)

Rijbeelden 240x240 (getoond op 64 px), kaarten 600 breed, via `make_product_blocks.py` uit `content/products/*/img` (originelen nooit wijzigen, DECISIONS 7 okt).

| Token | Beeld nu | Bron | Actie |
|---|---|---|---|
| std / mini / small | `pc-standard.jpg`, `pc-mini.jpg`, `pc-small.jpg` | `titanium-hammered-pan-pro/img/packshot-1` en `-3` (Mini en Small delen packshot-3) | maat staat in de naam; beeld is per maat niet te onderscheiden. Liever drie aparte Shopify-packshots per maat |
| large | ontbreekt | `titanium-hammered-pan-pro/img/packshot-2.jpg` | `pc-large.jpg` maken |
| deep, wok, crepe | `pc-deep/wok/crepe.jpg` | packshot-3 / -3 / -2 | ok |
| lid20 tot lid30 | `pc-lid.jpg` | `stainless-steel-lid/img/packshot-1.jpg` | ok; maat in de naam |
| board | `pc-board.jpg` | `titanium-cutting-board-v2/img/packshot-2.jpg` | ok |
| utset | `pc-utensil.jpg` | Shopify CDN `Utensils05-V2_1.webp` | ok |
| apron, mill | `pc-apron.jpg`, `pc-mill.jpg` | packshot-1 | ok |
| set6 (fall sale) | ontbreekt als rijbeeld; `p-set6.jpg` in post-purchase/winback/vip/anniversary assets | `titanium-hammered-pan-set-with-lids-6-pcs/img/packshot-1.jpg` | `pc-set6.jpg` maken |
| pizza, roast | ontbreekt als rijbeeld | `titanium-hammered-pizza-steel/img/packshot-1.jpg`, `titanium-hammered-roasting-pan/img/packshot-1.jpg` | `pc-pizza.jpg`, `pc-roast.jpg` (roast alleen US) |

Geen AI-beelden in cross-sell-kaarten (hammered patroon alleen binnenin, feedback Floris).

### 6.3 Django/Klaviyo-skelet (voorstel, niet in templates)

Prototype: `scratchpad/xs/gen_xsell.py` (generator) en `test_xsell.py`. Gegenereerd 15,2 KB (huidige `goes.html` 21,7 KB). Lokaal getest met Django 4.2 op 13 orders:

| Order (+ eerder bezit) | Toont |
|---|---|
| Standard | deksel 28, Mini |
| Standard + deksel | Mini, plank |
| Standard + Mini | deksel 28, plank |
| Small + Mini | deksel 26, plank |
| Large + Small | deksel 30, Standard |
| Deep + wok | Mini, plank |
| Fall-sale-set | Standard, Utensil Set |
| 6-Pcs + plank | Standard, Utensil Set |
| Pot Set (US) | fall-sale-set, Standard |
| Schort + molens | plank, Standard |
| VIP: order 2 deksel, eerder Standard + Mini + plank + deksel 28 | Small, deep |
| VIP: order 2 Mini, eerder Small + deksel 26 | Standard, deksel 20 |
| Alles al in bezit | terugval |

Opbouw (ingekort; de generator schrijft de volledige ketens):

```django
{% with s=event.Items|join:',' %}
{# 1. bezit: trigger-order (laag 1) of profielvlag (laag 2) #}
{% if 'Pan Pro Mini' in s or 'Pan Set With Lids' in s or '12-Pcs' in s or person|lookup:'own_mini' %}{% firstof 'y' as o_mini %}{% endif %}
{% if 'Pan Pro Standard' in s or 'Cookware Set Pro' in s or 'Pan Pro Duo' in s or person|lookup:'own_std' %}{% firstof 'y' as o_std %}{% endif %}
{% if 'Pan Pro Standard' in s and 'Lid' in s or person|lookup:'own_lid28' %}{% firstof 'y' as o_lid28 %}{% endif %}
{# ... idem small, large, deep, wok, crepe, lid20, lid26, lid30, board, utset, apron, mill, pizza #}

{# 2. categorie: eerste match wint #}
{% if '12-Pcs' in s %}{% firstof 'set12' as k %}{% elif 'Pot' in s %}{% firstof 'pot' as k %}{% elif 'Pan Set With Lids' in s %}{% firstof 'set6' as k %}{% elif 'Pan Pro Standard' in s %}{% firstof 'std' as k %}{% elif 'Pan Pro Small' in s %}{% firstof 'small' as k %}{# ... #}{% endif %}

{# 3. vrije kandidaten per categorie #}
{% if k == 'small' %}
  {% if not o_mini %}{% firstof 'mini' as a1 %}{% endif %}{% if not o_lid26 %}{% firstof 'lid26' as a2 %}{% endif %}
  {% if not o_board %}{% firstof 'board' as a3 %}{% endif %}{% if not o_wok %}{% firstof 'wok' as a4 %}{% endif %}
{% elif k == 'std' %}
  {% if not o_lid28 %}{% firstof 'lid28' as a1 %}{% endif %}{% if not o_mini %}{% firstof 'mini' as a2 %}{% endif %}
  {% if not o_board %}{% firstof 'board' as a3 %}{% endif %}{% if not o_deep %}{% firstof 'deep' as a4 %}{% endif %}
{% endif %}

{# 4. eerste en tweede vrije kandidaat #}
{% firstof a1 a2 a3 a4 as c1 %}
{% if a1 %}{% firstof a2 a3 a4 as c2 %}{% elif a2 %}{% firstof a3 a4 as c2 %}{% elif a3 %}{% firstof a4 as c2 %}{% endif %}

{# 5. één renderer per rij: velden per token #}
{% if c1 %}
<tr data-xs="{{ c1 }}">
  <td width="76"><img src="{{SHARED}}/{% if c1 == 'mini' %}pc-mini{% elif c1 == 'lid26' %}pc-lid{% elif c1 == 'board' %}pc-board{% endif %}.jpg" width="64" height="64" alt=""></td>
  <td><a href="[[pre]]{% if c1 == 'mini' %}titanium-hammered-pan-pro-mini{% elif c1 == 'lid26' %}stainless-steel-lid%3Fvariant%3D52401107206484{% endif %}[[post]]">
    <b>{% if c1 == 'mini' %}Pan Pro Mini 8&Prime;{% elif c1 == 'lid26' %}Stainless Steel Lid, 26 cm{% endif %}</b><br>
    {% if c1 == 'mini' %}The breakfast pan: eggs and small portions.{% elif c1 == 'lid26' %}Fits your 10&Prime; Small.{% endif %}
    {% if event.extra.shipping_address.country_code == 'US' %}<span>{# prijs per token #}</span>{% endif %}
    See it&nbsp;&rarr;</a></td>
</tr>
{% endif %}
{# idem c2 #}
{% if not c1 %}<tr><td>Already have the full line-up? Reply and tell us what you cook most.</td></tr>{% endif %}

{# 6. fall-sale-kaart #}
{% if not o_mini and not o_small and not o_large %}…kaart 3 pans + 3 lids…{% endif %}
{% endwith %}
```

Let op bij de bouw:
1. **`firstof … as`** is standaard Django (zet een variabele binnen de `with`; `{% if %}` maakt geen nieuwe laag) en staat op de tag-allowlist in PLAYBOOK, maar is in Klaviyo zelf nog niet bevestigd. **[CONTROLEREN]** in één Klaviyo-preview met een echt profiel. Valt het weg: dezelfde generator rolt de rijen uit per categorie (groter, circa 40 KB, nog onder de clipping-grens in P3/R1/V1, niet in C1).
2. `person|lookup:'own_mini'` werkt pas na laag 2; tot dan is de vlag leeg en valt het blok terug op laag 1 (geen fout).
3. Variant-links met `?variant=` binnen `/discount/<code>?redirect=` URL-encoded zetten (`%3Fvariant%3D…`), zoals nu bij de deksel. Variant-ID's deksel (Chrome): 20 cm 53294486421844, 26 cm 52401107206484, 28 cm 52401107239252, 30 cm 52401107272020 (`personalisatie` 4).
4. Tokens in profielnamen en tags mogen geen voorvoegsel van elkaar zijn (`lid2` naast `lid26` mag niet).
5. Tests: de 13 orders hierboven plus US/INT als vaste cases in `research/tailoring/test/matrix.py`; regel "geen kaart-token dat ook als bezit gemarkeerd is" als automatische controle.
6. `utm_content` per mail en rij: `p3pan-xs1`, `r1pan-xs2`, `v1-xs1`, `n2-xs3`, `p1-lidline`, `p2-lidline`, zodat attach per mail meetbaar is (voor/na, geen extra T-test in fase 1).

### 6.4 Copy per moment (Engels, binnen de claims)

- **P1 regel:** "Your 11″ takes the 28 cm lid. Steams, melts, stops the splatter." Link: "Add the 28 cm lid". (Geen "free shipping" als losse belofte; de gifts staan al in de mail.)
- **P2 tipregel:** "For a set yolk on top, cover the pan for the last minute. No lid yet? Your 11″ takes the 28 cm."
- **P3 rij-intro:** "What Small owners add next" / "One in three Small owners comes back for the Mini." Noot: "Your thank-you code works on these too."
- **R1:** "What to add next" / "Picked from what is already in your kitchen." Noot: "HI10 is already applied."
- **R2:** eyebrow "HERE IS YOUR 10%" (VIP: "YOUR 15% EXCLUSIVE DISCOUNT"), kop kaarten "Your next piece".
- **V1:** onderwerp "You're a VIP customer: 15% off, just for you", hero-kop "You're a VIP customer.", sub "15% exclusive discount. Get it now." Blok "Picked for your kitchen" / "Nothing you already own. Your 15% works on all of these." (de zin "Nothing you already own" alleen na laag 2).
- **N1:** "Still on our list for your kitchen."
- **N2:** "One year of cooking. 15% off what comes next."
- **Fall-sale-kaart:** "Every other size, in one box." / "Mini, Small and Large, each with its own lid." US: "$299".
- **Dezelfde maat opnieuw (P.S.):** "Cooking for someone else too? Reply and we will help you pick the size."

## 7. Besluiten en open vragen voor Floris

1. Flow "v4 · Bezit" (Ordered Product → `own_<token>`) in de UI bouwen en de backfill via segment-export/import: akkoord? Of liever Shopify-tags via Shopify Flow (schrijft in Shopify)?
2. Anniversary N2 naar 15%: nieuwe coupon-pool `SK_ANNIV15_7D` (prefix YEAR-), V1 blijft SK_REGULARS15_14D maar met de nieuwe kop.
3. Fall sale: einddatum, of de $299 ook buiten de US geldt (lokale prijs), en of $349 in DECISIONS vervangen wordt.
4. Prijzen in kaarten: Shopify toont vandaag Standard $144 en Small $137, de mails $134. Eén prijsbron (content/facts) en de build laten controleren.
5. P1 en P2: één deksel-regel zonder code. Akkoord dat P1 dat mag (bevestiging blijft verder schoon)?
6. Dishwasher sheets niet als kaart: na de gift naar de abonnementsflow (BACKLOG 6).

Volgende stap na akkoord: `make_product_blocks.py` uitbreiden met het `xsell`-blok (generator uit 6.3), `goes`/`goes1` vervangen in P3, R1, V1, statische kaarten in R2/N2 vervangen, P1/P2-regels toevoegen, QA-matrix uitbreiden, dan één Klaviyo-preview voor `firstof … as` en `person|lookup`.
