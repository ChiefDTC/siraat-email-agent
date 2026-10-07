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

__DATA__

---

__SEGMENTEN__

---

__VOORSTEL__
