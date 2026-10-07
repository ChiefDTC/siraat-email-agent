# 01 · Personalisatie en productaanbevelingen in de v4-flows

Stand 7 oktober 2026. Alleen gelezen: Klaviyo-API (GET, revision 2025-10-15) en Shopify (ShopifyQL en één GraphQL-query op het deksel). Geen templates gewijzigd, niets in Klaviyo of Shopify aangemaakt. Codeblokken hieronder zijn **voorstellen** voor de bouw, niet ingebouwd.

Bronnen: `klaviyo/flows/v4-flow-system.md`, `research/tailoring/00-data.md` en `03-routing.md`, `research/survey/01-klantbegrip.md`, `.agents/product-marketing.md`, `content/products/*/cross-sell.md` en `product.md`. Nieuwe data: Placed Order-events (RSNxYV) van 1 november 2024 tot 7 oktober 2026 (profiel-ID's gehasht, alleen in de scratchpad, hier alleen aggregaten), ShopifyQL over 365 dagen, en een scan van alle 436 Klaviyo-templates op feed- en catalogustags.

__SAMENVATTING__

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

__VOORSTEL__
