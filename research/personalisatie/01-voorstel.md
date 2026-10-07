# 01 · Personalisatie en productaanbevelingen in de v4-flows

Stand 7 oktober 2026. Alleen gelezen: Klaviyo-API (GET, revision 2025-10-15) en Shopify (ShopifyQL en één GraphQL-query op het deksel). Geen templates gewijzigd, niets in Klaviyo of Shopify aangemaakt. Codeblokken hieronder zijn **voorstellen** voor de bouw, niet ingebouwd.

Bronnen: `klaviyo/flows/v4-flow-system.md`, `research/tailoring/00-data.md` en `03-routing.md`, `research/survey/01-klantbegrip.md`, `.agents/product-marketing.md`, `content/products/*/cross-sell.md` en `product.md`. Nieuwe data: Placed Order-events (RSNxYV) van 1 november 2024 tot 7 oktober 2026 (profiel-ID's gehasht, alleen in de scratchpad, hier alleen aggregaten), ShopifyQL over 365 dagen, en een scan van alle 436 Klaviyo-templates op feed- en catalogustags.

## Kort

1. **Catalogus:** de Shopify-catalogus is in Klaviyo gesynct (BIS-templates gebruiken `{% catalog %}`), maar de Catalog API laat alleen `$custom` zien (0 items). Er bestaan vier feeds: `Bestseller`, `New_Products`, `Abandoned_Cart`, `Browsed_Product`, alleen in oude drag-and-drop-templates. In CODE-templates werkt `{% with item=feeds.Bestseller|index:0 %}` (bewezen in dit account) of `{% for item in feeds.X %}`.
2. **Advies:** aanbevelingen in de flows op **regels uit het trigger-event** (maat, deksel, vorm), feed alleen als derde kaart met statische terugval. Een feed kent de maat niet en kan gratis gift-producten tonen.
3. **Kooppatroon:** de tweede aankoop is een tweede (kleinere) maat, een deksel of een vorm. Standard → Mini 19%, Small → Mini 33%, deksel 19 tot 21%. Mediaan 35 dagen tot order 2 (deksel en plank 24 dagen). 9,2% wordt herhaler; AOV 2e order $177.
4. **Segmenten:** internationaal is 55% van de orders (12 maanden), dus de USD-regel geldt voor de meerderheid. Cadeau is in de data maar 5 tot 8,5% zichtbaar (enquête 19%); vorige pan (RVS, gietijzer) is nergens zichtbaar: klikvraag in P1 voorgesteld.
5. **Meeste winst:** P3-pan (deksel in jouw maat), R1-pan (tweede maat), K2 (deksel-regel), B2 (vaak samen gekozen), V1 (derde order). Code-skeletten in sectie 4.

---

## 1. Klaviyo-catalogus en product feeds

### 1.1 Wat er is

| Vraag | Antwoord | Bewijs |
| --- | --- | --- |
| Is er een catalogus via de API? | **Nee, niet zichtbaar.** `GET /api/catalog-items`, `/catalog-categories`, `/catalog-variants` geven alle drie `data: []`. Een filter op `$shopify` geeft fout 400: "Supported values: {'$custom'}". De Catalog API toont alleen een eigen API-catalogus, niet de Shopify-sync. | API-respons 7 okt |
| Is de Shopify-catalogus wel in Klaviyo gesynct? | **Ja.** De code-templates "BIS 1" en "BIS 2 · It's Back" (RQD4RN) gebruiken `{% catalog event.ProductID unpublished="cancel" %}` met `catalog_item.url` en `catalog_item.featured_image.full.src`. Dat werkt alleen met een gesyncte catalogus. Daarnaast draaien vier product feeds (hieronder) op die catalogus. | templatescan |
| Welke velden? | Feed-item (zoals de bestaande templates ze gebruiken): `item.title`, `item.url`, `item.image_full_url`, `item.price`, `item.regular_price` (= compare-at). Catalog lookup: `catalog_item.title`, `.url`, `.featured_image.full.src` / `.thumbnail.src`; prijs onder `catalog_item.metadata` **[CONTROLEREN in preview]**. Categorieën = Shopify-collecties. | templatescan, Viewed Product-event |
| Categorieën bruikbaar? | Matig. Een Pan Pro zit in 21 collecties, waarvan 15 sale-collecties ("PRIME SALE 70% OFF", "Warehouse Clearance" dubbel). Alleen "Titanium Pans", "Cookware", "Best Sellers" zijn bruikbare feedfilters. | `Categories` in Viewed Product (XNtYMB) |
| Gratis gift-producten in de catalogus? | Ja, Mystery Gift, Free Shipping, e-book en de filterloting zijn ACTIVE producten met prijs $0 en zitten in 87% van de orders. Een feed op "bestseller" kan ze bovenaan zetten. **Elke feed moet ze uitsluiten** (filter in de feed, plus een titelcheck in de template). | `content/products/README.md`, tailoring 00-data |

### 1.2 Bestaande feeds

Gevonden in 14 van de 436 templates, **allemaal drag-and-drop** (SYSTEM_DRAGGABLE); geen enkele v4-code-template gebruikt een feed.

| Feednaam (exact, hoofdlettergevoelig) | Waar gebruikt | Waarschijnlijk type |
| --- | --- | --- |
| `feeds.Bestseller` | 8 campagnes (o.a. "10/1 Cook Clean this Month") en "Customer Winback Email 1/2" | catalogusfeed, sortering bestseller |
| `feeds.New_Products` | Customer Winback Email 1/2 | catalogusfeed, nieuwste eerst |
| `feeds.Abandoned_Cart` | "Abandon Cart Email 1/2" | aanbevelingsfeed (gepersonaliseerd) **[CONTROLEREN]** |
| `feeds.Browsed_Product` | "Browse Abandonment Email 1" | aanbevelingsfeed (gepersonaliseerd) **[CONTROLEREN]** |

De feeddefinitie (type, filters, sortering, uitsluitingen) is niet via de API te lezen. Eén keer kijken in Klaviyo > Content > Products > Product feeds, en daar ook nakijken of gift-producten zijn uitgesloten.

### 1.3 Syntaxis in een CODE-template

De klaviyo.com-documentatie was vanuit deze sessie niet bereikbaar (egress geblokkeerd). De vorm hieronder is wat **in dit account al werkt** (uit de eigen templates), aangevuld met de loopvorm uit Klaviyo's eigen tutorials ("feeds" is een gereserveerde naam die alle feeds bevat die in de template voorkomen).

Vorm A, per positie (zo bouwt de drag-and-drop-editor het in dit account, dus bewezen):

```django
{% if feeds.Bestseller|index:0 %}{% with item=feeds.Bestseller|index:0 %}
  <a href="{{ item.url }}"><img src="{{ item.image_full_url }}" alt="{{ item.title }}" width="176"></a>
  {{ item.title }}
  {% if person.Country == 'United States' or person.Country == 'US' %}{{ item.price }}{% endif %}
{% endwith %}{% endif %}
```

Vorm B, loop (korter, één keer testen in preview):

```django
{% for item in feeds.Bestseller|slice:":3" %}
  {% if item.title != 'Mystery Gift' and item.title != 'Free Shipping' and 'E-Book' not in item.title and 'Giveaway' not in item.title %}
    ... kaart ...
  {% endif %}
{% endfor %}
```

Catalog lookup op een product-ID uit het event (bewezen in BIS 2):

```django
{% catalog event.ProductID %}
  <a href="{{ catalog_item.url }}"><img src="{{ catalog_item.featured_image.full.src }}" alt="{{ catalog_item.title }}"></a>
{% endcatalog %}
```

Let op: `unpublished="cancel"` (zoals in BIS) **annuleert de hele mail** als het product niet gepubliceerd is. In een aanbevelingsblok weglaten.

Regels voor gebruik in de v4-templates:
1. Feednaam exact als in Klaviyo; de template-preview toont een gepersonaliseerde feed alleen met een testprofiel dat historie heeft.
2. Prijs uit een feed is de USD-shopprijs. Zelfde regel als nu: alleen tonen bij US (`person.Country` of `event.extra.shipping_address.country_code == 'US'`).
3. Elke feed-sectie in `{% if feeds.X|index:0 %}` zetten, zodat een lege feed geen leeg blok achterlaat; daaronder een statische terugval (zie sectie 4).
4. UTM: `item.url` heeft geen UTM. Voorstel: `{{ item.url }}?utm_source=klaviyo&utm_medium=email&utm_campaign=v4-postpurchase&utm_content=p3pan-feed1` (als `item.url` al een `?` bevat: `&`). In `/discount/<code>?redirect=` kan de feed-URL niet zonder het pad te kennen; daarom codelinks naar de collectie laten gaan en de feedkaart naar de PDP.

### 1.4 Advies: regels eerst, feed als aanvulling

De catalogus is klein (circa 15 verkoopbare producten), de logica die de meeste winst geeft is bekend (deksel in dezelfde diameter, tweede maat, wok of deep pan) en hangt af van **variant en maat**, wat een feed niet kan. Dus:
- **Hoofdkaart** = regel op basis van het trigger-event (`event.Items`, `event.extra.line_items[].title`, `.variant_title`, `.product.handle`, `.product.images`). Alle velden bestaan al in Placed Order en Checkout Started.
- **Tweede rij** ("Often chosen next") = een feed, alleen waar de regel niets sterks heeft (accessoire-kopers, VIP). Altijd met statische terugval.
- Geen gepersonaliseerde feed als hoofdblok in post-purchase: hij weet niet welke maat de klant heeft en kan het net gekochte product opnieuw tonen.

---

## 2. Kooppatronen (laatste 12 maanden)

Bron A: Klaviyo Placed Order, 8 okt 2025 t/m 7 okt 2026, **90.513 orders** (komt overeen met Shopify: 90.091). Betaalde regels; gratis gift-regels en Shipping Protection genegeerd. Voor "eerste order" zijn 17.408 profielen met een order tussen 1 nov 2024 en 7 okt 2025 uitgesloten (anders lijkt een oude klant nieuw). Bron B: ShopifyQL over 365 dagen (product, nieuw/terugkerend, land). Categorieën zoals in tailoring 00-data ("vorm" = deep, wok, crêpe, pizza steel, roasting, pots).

### 2.1 Samen in één order

37% van de orders heeft meer dan één betaald product. Top-combinaties (aandeel van alle orders):

| Combinatie | Orders | % |
| --- | --- | --- |
| Pan Pro Standard + Stainless Steel Lid (beide titels samen, incl. oude titel "Lid for Pan Pro") | 8.850 | 9,8% |
| Pan Pro Large + deksel | 6.644 | 7,3% |
| Deep Pan Pro + Wok Pan Pro | 3.943 | 4,4% |
| Pan Pro Standard + Utensil | 3.897 | 4,3% |
| Pan Pro Standard + Wok | 3.834 | 4,2% |
| Pan Pro Standard + Deep Pan | 3.797 | 4,2% |
| Pan Pro Mini + Standard | 3.217 | 3,6% |
| Pan Pro Large + Small | 2.545 | 2,8% |
| Pan Pro Small + deksel | 2.514 | 2,8% |
| Crêpe + Standard / Wok / Deep | 2.389 tot 2.490 elk | 2,6 tot 2,8% |

Bij een order met een Pan Pro: **24% neemt een deksel mee**, 20% een tweede pan of vorm, 7% een snijplank.

### 2.2 Tweede aankoop: wat en wanneer

Cohort: eerste order vóór 7 april 2026 (minstens 6 maanden kijktijd), n = 45.648.

| | Waarde |
| --- | --- |
| Koopt ooit een tweede keer (tot 7 okt) | 9,2% |
| Binnen 180 dagen | 7,4% |
| Dagen tot 2e order (orders binnen 1 uur na de eerste niet meegeteld) | p25 14 · **mediaan 35** · p75 83 |
| Aandeel herhalers binnen 14 / 30 / 45 / 60 / 90 dagen | 25% / 46% / 57% / 66% / 77% |
| Mediaan dagen als de 2e order een deksel bevat / een snijplank / een pan / een vorm | **24** / 24 / 30 / 32 |
| AOV 1e order tegen 2e order (zelfde klanten) | $217 tegen **$177** (Shopify: terugkerend $192, nieuw $225) |
| 2e order met kortingscode | 41% (1e order 52%). Codes "REPLAC..." (vervanging) 161 keer: kleine ruis |

Wat zit er in de tweede order, per eerste aankoop (n = herhalers in het hele venster, meerdere producten per order mogelijk):

| Eerste order | n | Tweede order: top |
| --- | --- | --- |
| **Pan Pro** (alle maten) | 4.856 | Pan Pro Mini 19% · deksel 19% · Standard 16% · Small 16% · Deep 13% · Wok 12% · Large 9% · snijplank 8%. Categorie: nog een pan 54%, vorm 28%, deksel 26%, plank 17%, utensils 12% |
| · Standard 11" | 2.554 | **Mini 19%** · deksel 19% · Standard 18% · Small 16% · Deep 13% · Wok 11% · plank 9% |
| · Large 12" | 1.549 | **deksel 21%** · Large 16% · Small 15% · Standard 14% · Mini 14% · Deep 14% · Wok 13% |
| · Small 10" | 900 | **Mini 33%** · deksel 19% · Small 16% · Deep 12% · Wok 11% · plank 10% · Crêpe 9% |
| · Mini 8" | 558 | **Standard 20%** · deksel 17% · Wok 15% · Small 14% · Deep 13% |
| Vorm (deep, wok, crêpe, pizza) | 761 | Deep 19% · Crêpe 16% · deksel 16% · Standard 15% · Wok 12% |
| Set | 55 | **Snijplank 29%** · Utensil Set Bundle 22% · Pizza Steel 13% · Crêpe 11% · Deep 11% |
| Snijplank | 154 | Nog een plank 23% · Standard 20% · deksel 14% · Wok 11% |
| Schort | 2 | te weinig data (schort is 0,1% van de orders) |

Deksel: wie de eerste pan **zonder** deksel kocht, neemt in de 2e order in 22% een deksel; wie er al een had, in 32% (een deksel voor de tweede pan).
Derde order (1.102 profielen): deksel 21%, Mini 15%, Deep 12%, Small 12%, Standard 10%, Wok 10%, Utensil Set 9%. AOV $169.

Shopify bevestigt het patroon (aandeel van orders, terugkerend tegen nieuw, 365 dagen): deksel 24% tegen 21%, **Mini 16% tegen 8%**, snijplank 13% tegen 8,5%, Deep 13% tegen 10%, Wok 11% tegen 9%, Utensil Set 6,4% tegen 2,2%, en Standard 15% tegen 44%. De tweede aankoop is dus **een tweede (kleinere) maat, een deksel of een vorm**, bijna nooit nog een Standard als eerste keus.

### 2.3 AOV en herhaling per segment

| Segment (signaal in de data) | Aandeel orders | AOV | Herhaling 180 d |
| --- | --- | --- | --- |
| US (verzendland) | 45,2% | $203 | 8,1% |
| Internationaal | **54,8%** (GB 14%, AU 12%, SG 4%, CA 3%, AE 2%, HK 2%) | $203 (Shopify: AE $282, CH $259, GB $206, AU $208, US $218) | 7,3% |
| Cadeau-proxy: andere achternaam op verzendadres dan op factuuradres | 4,8% (andere naam: 8,5%) | $214 | 5,8% |
| Gezin-proxy: Large, set of 2+ stuks kookgerei | 37,2% | $296 | 8,0% |
| Eén pan, zonder deksel | ~60% van de eerste orders | | 7,2% |
| Eerste order alleen snijplank | 1,5% | $113 | 6,1% |
| Set | 1,5% | $619 | (n te klein) |

- Internationaal is over twaalf maanden **de meerderheid** (tailoring 00-data zag 37% in één week in oktober). De regel "prijzen alleen bij US" raakt dus 55% van de post-purchase- en winback-ontvangers.
- Cadeau: de proxy ziet maar 4,8 tot 8,5%, de enquête 19%. De meeste gevers laten het naar zichzelf sturen. Per maand stabiel (4,1 tot 5,3%; november en december het hoogst). Schort-orders hebben het hoogste cadeau-aandeel (9%).
- Geen enkel enquêteveld zit in Klaviyo: de metric "Survey Answer - Triple Pixel" (StqVtw) heeft één event zonder eigenschappen, en in 300 recente profielen staan alleen Alia-velden (popup, aanbod) en Shopify Tags.

---

## 3. Segmenten die de inhoud moeten sturen, en hun Klaviyo-signaal

| Segment | Omvang (enquête / data) | Wat er in de mail anders moet | Signaal in Klaviyo nu | Betrouwbaarheid | Beter signaal (voorstel) |
| --- | --- | --- | --- | --- | --- |
| **Cadeaukoper** | 19% (S1) / 4,8 tot 8,5% zichtbaar | P2, U1, N1 gaan over "your first egg" bij een pan die bij een ander staat. Gever: "forward this to the person cooking on it", maat-ruil, retour 30 dagen ongebruikt | Placed Order: `event.extra.shipping_address.last_name` ≠ `event.extra.billing_address.last_name`. Schort, molens of e-gift card in `Items`. Kortingscodes MOTHER.., VALENT.. | Laag tot middel: mist gevers die naar zichzelf laten sturen | Eén vraag in P1 met klikbare antwoorden (zie 4.7): "Who is this for? Me / Someone else". Segment = Clicked Email where URL contains `who=gift` |
| **Gezin / gedeeld huishouden** | 12% (S1) / 37% gezin-proxy | Large en set: batch-koken, "a pan for each burner", deksel 30 cm; herhaling iets hoger (8,0%) | `Items` bevat "Pan Pro Large", SET_TITELS, of 2+ kookgerei; `$value` ≥ 300 | Middel | Zelfde klikvraag ("Cooking for: 1 to 2 / 3 to 4 / 5+") |
| **Health-first** | 60 tot 76% (S2, S8) | Is de standaard voor iedereen: PFAS-vrij met rapport 25895 in elke fase (klantbegrip D1) | Geen apart signaal nodig. Eventueel `full_landing_site` in Placed Order (landingspagina, bv. een PFAS-blog) | n.v.t. | Geen split. Niet personaliseren, wel in de basistekst |
| **Upgrader van gietijzer of RVS** | RVS 41%, gietijzer 13% overwogen (S1) | Vergelijking op categorie: "lighter than cast iron" (R138 Tammy), "no sticking like stainless if you preheat" | **Geen.** De enquête vraagt het vorige merk niet; Klaviyo heeft geen veld | geen | Klikvraag in P1: "What were you cooking on before? Coated nonstick / Stainless / Cast iron / Ceramic". Gebruik in P2 (techniek), N1 en R1 |
| **Internationaal** | 55% van de orders (12 mnd) | Geen USD-prijzen, "duties paid", geen 12-delige set (alleen US) | Orders: `event.extra.shipping_address.country_code`. Profiel: `person.Country` (C4 gebruikt dit al). Cart: `$currency`, Checkout: `event.extra.presentment_currency` | Hoog (orders), middel (profiel: 16% zonder land) | Bestaand; uitbreiden naar elke feed- en aanbevelingskaart |
| **Bezit (maat en vorm)** | 100% van de kopers | Deksel in de juiste diameter, tweede maat, wok of deep | `Items` en `event.extra.line_items[].title / variant_title` op het trigger-event. Metric "Ordered Product" (XT7f8Z, per regel) voor segmenten "heeft ooit X" | Hoog voor de trigger-order, laag voor eerdere orders in de template | Segment per bezit via Ordered Product; in de template alleen het trigger-event |
| **Herhaalkoper / VIP** | 9,2% wordt herhaler | Geen merkuitleg; deksel voor pan 2, Utensil Set | Placed Order count (flow-splits), Shopify Tags | Hoog | Bestaand (VIP-flow) |

Belangrijkste gat: Klaviyo-templates zien alleen het **trigger-event**. Wat iemand in een eerdere order kocht, weet de template niet (behalve via segmenten of profielvelden). Profielvelden zetten via de flow ("Update profile property") lukte via de API niet (bouwnotitie 2.1), wel in de UI. Voorstel bij de bouw: in de post-purchase-flow één actie "Update profile property" `pan_sizes` / `has_lid` per tak, zodat R1, V1 en N2 later weten wat er al staat. **[VRAAG FLORIS]** of die UI-stap mag.

---

## 4. Voorstel per v4-mail

Volgorde = verwachte winst (volume per week uit v4/tailoring x hoe sterk het patroon is). Alle blokken gebruiken velden die in de echte events bestaan; Django-condities zoals in tailoring 03-routing (getest in `research/tailoring/test`). Copy in de blokken is een voorbeeld binnen de claims (siraat-direct-response), de herschrijf-agent maakt hem af. Variant-ID's van de deksel (Chrome) komen uit Shopify, 7 okt 2026: Mini 20 cm `53294486421844`, Small 26 cm `52401107206484`, Standard 28 cm `52401107239252`, Large 30 cm `52401107272020`.

| # | Mail (volume/week) | Blok | Data | Fallback | Waarom de meeste winst |
| --- | --- | --- | --- | --- | --- |
| 1 | **P3-pan** (~500) | Hoofdkaart "Your [maat] takes the [cm] lid" met directe variantlink | `event.Items` (maat) | Huidige tekst "Pick the same diameter as your pan" + link naar de deksel-PDP | 24% koopt de deksel er al bij; 22% van de herhalers zonder deksel koopt hem bij order 2, mediaan 24 dagen (P3 valt op dag 20). Eén klik minder (maat al gekozen) |
| 2 | **R1-pan** (~900) | Hoofdkaart "tweede maat" + rij deksel/vorm | `event.Items` (maat, deksel ja/nee) | Deep Pan Pro (13%) en de deksel-regel | 2e order = 2e maat: Standard → Mini 19%, Small → Mini 33%, Mini → Standard 20%, Large → deksel 21% / Small 15%. R1 valt op dag 45, 57% van de herhalers koopt binnen 45 dagen |
| 3 | **P3-next** (~150) en **P3-set** (~200) | Set: snijplank + Utensil Set (29% / 22% van de 2e orders na een set). Next: "deksel voor je tweede pan" als de order al een deksel had en 2+ pannen | `event.Items` | Huidige kaarten | Set-kopers hebben de pannen al; plank en utensils zijn hun echte vervolg |
| 4 | **K2-new / K2-returning** (~600) | Eén regel onder de productkaart: "Your Standard takes the 28 cm lid. $59." | Added to Cart `Product Name` (maat zit in de titel) | Regel weg | Deksel zit in 24% van de pan-orders; de regel verhoogt de cart, geen extra mail |
| 5 | **B2-clicked / B2-notclicked** (~1.400) | Regel "Often chosen together" onder het bekeken product | `event.Name` | Regel weg | Deep + Wok 4,4%, Standard + deksel 9,8%, Standard + Wok/Deep 4,2%: dit zijn de echte paren |
| 6 | **VIP V1** (~140) | Rij "What regulars add next": deksel, Mini, Deep, Utensil Set (3e order) + `feeds.Bestseller` als derde kaart | Placed Order (2e order) `Items` + feed | Statische drie kaarten | Derde order: deksel 21%, Mini 15%, Deep 12% |
| 7 | **P1-first / P2 / U1** (cadeau, ~55) | Gever-variant: "Was it a gift? Forward the first-egg guide." en geen "your first egg" | Andere achternaam verzend/factuur; later de klikvraag | Huidige tekst | Klein volume, maar haalt een duidelijke mismatch weg (klantbegrip D7) |
| 8 | **P1-first** (~1.000) | Twee klikvragen (wie, waarop kookte je) als zero-party data | Clicked Email URL | n.v.t. | Voedt 1, 2, 7 en het RVS/gietijzer-blok in N1 en R1 |

Niet personaliseren (weinig winst of al gedaan): C1 tot C4 (checkout heeft geen adres en de categorie-router doet het werk), welcome (geen aankoopdata), sunset, N2 (eerst backfill-besluit 3.26).

### 4.1 P3-pan · deksel in de juiste maat

Plaats: vervangt de hoofdkaart "The one thing your pan is missing". Volgorde in de if-keten = meest verkochte maat eerst; bij twee pannen wint de eerste die matcht (de tweede maat staat in de rij eronder als "and for your [maat]"... alleen als je die wilt bouwen; anders weglaten).

```django
{% with items=event.Items|join:',' %}
{% if 'Pan Pro Standard' in items or 'Pan Pro Large' in items or 'Pan Pro Small' in items or 'Pan Pro Mini' in items %}
<!-- blok p3pan-lidmatch -->
<tr><td style="padding:22px 44px 4px 44px;font-family:Inter,Arial,Helvetica,sans-serif;">
  <div style="font-size:12px;letter-spacing:1px;color:#AC3B19;font-weight:600;">MATCHED TO YOUR PAN</div>
  <div style="font-size:22px;line-height:28px;color:#282828;padding-top:6px;">
    Your {% if 'Pan Pro Standard' in items %}11-inch Standard{% elif 'Pan Pro Large' in items %}12-inch Large{% elif 'Pan Pro Small' in items %}10-inch Small{% else %}8-inch Mini{% endif %}
    takes the {% if 'Pan Pro Standard' in items %}28{% elif 'Pan Pro Large' in items %}30{% elif 'Pan Pro Small' in items %}26{% else %}20{% endif %} cm lid.
  </div>
  <div style="font-size:15px;line-height:22px;color:#4A4A4A;padding-top:8px;">Steams, melts, keeps warm, stops the splatter.</div>
  {% if event.extra.shipping_address.country_code == 'US' %}<div style="font-size:15px;font-weight:600;padding-top:8px;">$59 <span style="color:#AC3B19;">$53.10</span> with your code</div>{% endif %}
  <a href="https://siraatskitchen.com/discount/{% coupon_code 'P3_THANKYOU_10_14D' %}?redirect=/products/stainless-steel-lid%3Fvariant%3D{% if 'Pan Pro Standard' in items %}52401107239252{% elif 'Pan Pro Large' in items %}52401107272020{% elif 'Pan Pro Small' in items %}52401107206484{% else %}53294486421844{% endif %}%26utm_source%3Dklaviyo%26utm_medium%3Demail%26utm_campaign%3Dv4-postpurchase%26utm_content%3Dp3pan-lidmatch">Add the {% if 'Pan Pro Standard' in items %}28{% elif 'Pan Pro Large' in items %}30{% elif 'Pan Pro Small' in items %}26{% else %}20{% endif %} cm lid</a>
</td></tr>
{% else %}
  {# fallback: wok, deep, crêpe zonder Pan Pro: de huidige kaart "Pick the same diameter as your pan" #}
{% endif %}
{% endwith %}
```

Let op: `Items` bevat titels, geen varianten; wok en deep pan hebben de maat alleen in `event.extra.line_items[].variant_title`. Daarom blijft de fallback voor vormen. Uitbreiding (optioneel): een loop over `event.extra.line_items` met `{% if 'Deep' in li.title and '24' in li.variant_title %}` om de deep 24 cm (geen deksel) uit te sluiten.

### 4.2 R1-pan · tweede maat (dag 45)

```django
{% with items=event.Items|join:',' %}
<!-- blok r1pan-nextsize -->
{% if 'Pan Pro Small' in items and 'Pan Pro Mini' not in items %}
  {% with h='titanium-hammered-pan-pro-mini' n='Pan Pro Mini 8"' why='For eggs and one-person breakfasts, next to your Small.' p='$129' %}…kaart…{% endwith %}
{% elif 'Pan Pro Standard' in items and 'Pan Pro Mini' not in items %}
  {% with h='titanium-hammered-pan-pro-mini' n='Pan Pro Mini 8"' why='The egg pan next to your Standard.' p='$129' %}…kaart…{% endwith %}
{% elif 'Pan Pro Mini' in items and 'Pan Pro Standard' not in items %}
  {% with h='original-siraat-100-pure-titanium-pan-with-hammered-pattern' n='Pan Pro Standard 11"' why='Room for dinner for 2 to 4.' p='$134' %}…kaart…{% endwith %}
{% elif 'Pan Pro Large' in items and 'Pan Pro Small' not in items %}
  {% with h='titanium-hammered-pan-pro-small' n='Pan Pro Small 10"' why='The weeknight pan next to your Large.' p='$127' %}…kaart…{% endwith %}
{% else %}
  {% with h='titanium-hammered-deep-pan-pro' n='Deep Pan Pro' why='Sauces, pasta, one-pan dinners.' p='From $119' %}…kaart…{% endwith %}
{% endif %}
{% endwith %}
```

Kaart (één keer uitgeschreven, binnen elke `with`):

```django
<a href="https://siraatskitchen.com/products/{{ h }}?utm_source=klaviyo&utm_medium=email&utm_campaign=v4-winback&utm_content=r1pan-nextsize">{{ n }}</a>
<div>{{ why }}</div>
{% if event.extra.shipping_address.country_code == 'US' %}<div>{{ p }}</div>{% endif %}
```

Beelden: `{{IMG}}/card-mini.jpg` enz. via de bestaande build (statisch per tak), of `catalog_item.featured_image.thumbnail.src` met `{% catalog <product_id> %}` (product-ID's uit Shopify bij de bouw invullen). Statisch heeft de voorkeur: de packshots in `content/products/*/img` zijn gecontroleerd, de Shopify-hoofdbeelden niet altijd.

Tweede rij blijft de deksel-rij die er al is (verborgen bij deksel in de order), met de maatregel uit 4.1.

### 4.3 P3-set en P3-next

P3-set, hoofdkaart: Titanium Cutting Board V2, tweede kaart Titanium Utensil Set Bundle ($149), derde Pan Pro Standard als de set hem niet bevat ("Pan Set With Lids | 6-Pcs" en "12-Pcs" hebben geen Standard 11", zie cross-sell.md). Conditie voor de derde kaart: `{% if 'Pan Pro Standard' not in items %}`.

P3-next bij twee pannen en één deksel in de order: tekst "One lid, two pans? Add the [maat]" met dezelfde if-keten als 4.1, maar op de tweede Pan Pro-titel. Alleen bouwen als de eerste ronde (4.1) werkt; het volume is klein.

### 4.4 K2-new en K2-returning · deksel-regel in de cart

```django
{% with pn=event|lookup:'Product Name' %}
{% if 'Pan Pro' in pn and 'Lid' not in pn and 'Deep' not in pn and 'Wok' not in pn and 'Cr' not in pn %}
<!-- blok k2-lidline -->
<div style="font-size:14px;line-height:21px;color:#4A4A4A;padding-top:8px;">
  Most people add the lid: your {% if 'Standard' in pn %}Standard takes the 28 cm{% elif 'Large' in pn %}Large takes the 30 cm{% elif 'Small' in pn %}Small takes the 26 cm{% elif 'Mini' in pn %}Mini takes the 20 cm{% else %}pan takes the lid in the same diameter{% endif %}
  {% if event.Price and event|lookup:'$currency' == 'USD' %}($59){% endif %}.
  <a href="https://siraatskitchen.com/products/stainless-steel-lid?utm_source=klaviyo&utm_medium=email&utm_campaign=v4-cart&utm_content=k2new-lidline">Add the lid</a>
</div>
{% endif %}
{% endwith %}
```

"Most people add the lid" mag niet: 24% is geen meerderheid. Feitelijke formulering: "Often added: the lid." Fallback: regel verdwijnt (geen `else`).

### 4.5 B2-clicked en B2-notclicked · vaak samen gekozen

```django
{% with nm=event.Name %}
<!-- blok b2-pair -->
{% if 'Deep Pan' in nm %}{% with pair='Wok Pan Pro' h='titanium-hammered-wok-pan-pro' %}…regel…{% endwith %}
{% elif 'Wok' in nm %}{% with pair='Deep Pan Pro' h='titanium-hammered-deep-pan-pro' %}…regel…{% endwith %}
{% elif 'Cr' in nm and 'pe Pan' in nm %}{% with pair='Pan Pro Standard 11"' h='original-siraat-100-pure-titanium-pan-with-hammered-pattern' %}…regel…{% endwith %}
{% elif 'Pan Pro' in nm %}{% with pair='the Stainless Steel Lid in the same diameter' h='stainless-steel-lid' %}…regel…{% endwith %}
{% elif 'Set' in nm or 'Edition' in nm %}{% with pair='Titanium Cutting Board' h='titanium-cutting-board-v2' %}…regel…{% endwith %}
{% endif %}
{% endwith %}
```

Regel: `Often chosen together: <a href="https://siraatskitchen.com/products/{{ h }}?utm_source=klaviyo&utm_medium=email&utm_campaign=v4-browse&utm_content=b2c-pair">{{ pair }}</a>`. Geen prijs (Viewed Product heeft geen valuta). Fallback: geen regel.

### 4.6 VIP V1 · wat vaste klanten als derde kopen

Twee statische kaarten (deksel met maatregel uit 4.1 op `event.Items`, Utensil Set Bundle) en één feedkaart:

```django
{% if feeds.Bestseller|index:0 %}{% with item=feeds.Bestseller|index:0 %}
{% if item.title not in event.Items|join:',' and item.price %}
<!-- blok v1-feed1 -->
<a href="{{ item.url }}?utm_source=klaviyo&utm_medium=email&utm_campaign=v4-vip&utm_content=v1-feed1"><img src="{{ item.image_full_url }}" width="176" alt="{{ item.title }}"></a>
<div>{{ item.title }}</div>
{% if event.extra.shipping_address.country_code == 'US' %}<div>{{ item.price }}</div>{% endif %}
{% else %}
  {# fallback: Deep Pan Pro, statisch #}
{% endif %}
{% endwith %}{% else %}
  {# fallback: Deep Pan Pro, statisch #}
{% endif %}
```

`item.price` als waarheidstest sluit $0-gifts uit als de feed ze bevat; beter is ze in de feed zelf uit te sluiten. Controleren of `item.url` al een `?` bevat.

### 4.7 P1-first · twee klikvragen (zero-party data)

Onder de tijdlijn, als klikbare knoppen (geen formulier nodig):

```html
<!-- blok p1first-ask -->
<div>Quick one, so we send the right tips: what were you cooking on before?</div>
<a href="https://siraatskitchen.com/pages/first-cook?prev=coated&utm_source=klaviyo&utm_medium=email&utm_campaign=v4-postpurchase&utm_content=p1first-ask-coated">A coated pan</a> ·
<a href="...?prev=stainless...">Stainless steel</a> ·
<a href="...?prev=castiron...">Cast iron</a> ·
<a href="...?prev=ceramic...">Ceramic</a>
<div>And is this pan for you? <a href="...?who=me...">For me</a> · <a href="...?who=gift...">It's a gift</a></div>
```

Segmenten: "Clicked Email where URL contains `prev=castiron`" enz., en `who=gift`. Wordt gelezen in P2 (gietijzer: "preheat like you're used to, lighter to lift"; RVS: "heat first, then oil, same as stainless"), U1 (gift: geen "your first egg"), N1 en R1. Landingspagina `first-cook` bestaat nog niet **[VRAAG FLORIS]**; tot dan naar de bestaande care-pagina. In P2 en U1 de condities met een segment-split in de flow (templates zien geen segmenten; `person|lookup:'...'` werkt alleen op profielvelden).

Cadeau-variant op adresdata (direct bruikbaar, zonder klikvraag):

```django
{% if event.extra.shipping_address.last_name and event.extra.billing_address.last_name and event.extra.shipping_address.last_name|lower != event.extra.billing_address.last_name|lower %}
  <!-- blok p1first-gift --> Sending it to someone? Forward this email: the first-egg steps are below, and unused items can go back within 30 days.
{% else %}
  … huidige intro …
{% endif %}
```

In P2 en U1 (Delivered Shipment, geen adres in het event) kan dit alleen via een flow-split op de Placed Order-eigenschap of via het `who=gift`-segment.

### 4.8 Bouwvolgorde en meting

1. 4.1 (P3-pan) en 4.4 (K2): alleen `event.Items` / `Product Name`, geen nieuwe objecten. `utm_content` `p3pan-lidmatch`, `k2new-lidline` meet het effect in GA4 en Shopify (deksel-attach in P3-orders).
2. 4.2 (R1-pan) en 4.5 (B2).
3. 4.7 klikvragen (na akkoord en pagina), daarna de segment-varianten in P2/U1/N1.
4. 4.6 feeds pas na een blik op de feeddefinities in de UI.

Elke nieuwe conditie eerst in `research/tailoring/test` (Django-run) en daarna één preview met een echt profiel in Klaviyo (US en INT, Standard en Small, met en zonder deksel). Geen T-test erbij in fase 1 (max 2 tests per flow); meten als voor/na op attach-rate per mail.

## 5. Open vragen voor Floris

1. Mag in de post-purchase-flow in de UI een "Update profile property" (`pan_sizes`, `has_lid`) zodat R1/V1/N2 eerdere aankopen kennen?
2. Klikvragen in P1 en een landingspagina `first-cook`: ja of nee?
3. Feeddefinities (`Abandoned_Cart`, `Browsed_Product`, `Bestseller`, `New_Products`) nakijken: type en of gift-producten zijn uitgesloten.
4. Waar staan de enquête-antwoorden (Triple Whale / KnoCommerce)? Een koppeling naar Klaviyo (profielveld "who is this for") zou het cadeau-signaal van 5% naar 19% brengen.
