# Asset register (content/assets)

Eén lijst van elk beeld dat Siraat's Kitchen heeft: Shopify-productfoto's, Shopify Files, Google Drive (ad statics en shoot), Figma-placeholders. Doel: snel een bruikbare foto voor een mail vinden, zien of er tekst in het beeld staat en of hij al in een mail gepland is.

Bestanden:

- `index.csv`: het register, 5.934 rijen (stand 7 oktober 2026).
- `visual-checks.csv`: elk beeld dat echt bekeken is (2.128 sleutels), met `use` en `text_in_image`. Deze waarden gaan voor alles bij een refresh. Handmatige correcties hier doen.
- `summary.md`: telling per bron en per Drive-map van de eerste crawl.
- `contact-shopify.png`: oude contactsheet van de eerste crawl.
- Script: `scripts/refresh_assets.py`.

## Kolommen

| kolom | betekenis |
| --- | --- |
| source | `shopify-product` (afbeelding aan een product), `shopify-file` (Content > Files), `drive` (ad statics en overig uit Drive), `drive-shoot` (high production shoot), `figma` (placeholder in de flow-mockup) |
| id | Shopify gid (`gid://shopify/MediaImage/…`, `gid://shopify/ProductImage/…`), Drive file id of Figma node id. In mapping.csv staat alleen het getal achter de laatste `/` |
| title | bestandsnaam |
| folder_or_product | producttitel, Drive-map of `HP shoot / images` en `HP shoot / square` |
| url_or_viewurl | Shopify CDN-url (voeg `&width=600` toe voor mailformaat) of Drive view-url |
| width, height, bytes | pixels en bestandsgrootte (bytes niet voor productfoto's) |
| category | grove soort uit de eerste crawl: packshot, lifestyle, ad-static, product-cutout, logo, ui-screenshot, other |
| notes | status, handle, alt-tekst, aanmaakdatum of Drive-map |
| product_handle | Shopify handle. Productfoto's: de handle van het product zelf (kan een draft- of kopie-listing zijn). Files, Drive en shoot: afgeleid uit titel en alt-tekst (bijv. `P09-A_Pan_Lid` wordt de Pan Pro, `12pc` wordt `titanium-hammered-cookware-set`). Leeg als onbekend of als het om een concurrent gaat |
| use | `hero` (sterke foto zonder tekst, breed genoeg voor bovenaan een mail), `product-card` (product los op effen achtergrond), `detail` (close-up van materiaal, rand, handvat), `lifestyle` (in gebruik, sfeer, mensen), `packshot` (productfoto die niet als kaart werkt, vaak met tekst), `not-for-email` (ad statics met tekst, UI-screenshots, logo's, iconen, stockfoto's van andere producten, concurrenten) |
| text_in_image | `yes`, `no` of `unknown`. Bekeken: alle Shopify Files in lifestyle, packshot en product-cutout (2.099 bestanden, bijna-dubbelen via perceptuele hash samengevoegd) en alle 29 shootbeelden. Productfoto's erven het oordeel via dezelfde CDN-url. Ad statics zijn altijd `yes` |
| used_in | mail-id's uit `content/mapping/mapping.csv` die dit beeld gebruiken. Shootbeelden erven dit van hun Shopify-kopie met dezelfde shotnaam en vorm |

Logo's staan op `not-for-email` (category `logo`). Voor de header van een mail het logo uit `brand/logo/` gebruiken, niet uit dit register.

## Tellingen (7 oktober 2026)

`use` (alle 5.934 rijen):

| use | rijen |
| --- | ---: |
| not-for-email | 4.265 |
| product-card | 671 |
| lifestyle | 419 |
| hero | 243 |
| detail | 206 |
| packshot | 130 |

`text_in_image`: yes 3.425, no 1.820, unknown 689 (unknown is Drive packshot/lifestyle/other, Shopify Files `other`, Figma en svg-iconen; niet bekeken).

Hero zonder tekst: 243 rijen, 202 unieke beelden (productfoto's tellen per product mee). Rijen met `used_in`: 44.

## Een beeld vinden

Met Python (stdlib), vanuit de repo-root:

```python
import csv
rows = list(csv.DictReader(open('content/assets/index.csv')))

# hero-kandidaten zonder tekst voor de Pan Pro, nog niet gepland in een mail
[r['url_or_viewurl'] for r in rows
 if r['use'] == 'hero' and r['text_in_image'] == 'no' and not r['used_in']
 and r['product_handle'] == 'original-siraat-100-pure-titanium-pan-with-hammered-pattern']

# product-cards voor de 6-delige set
[r for r in rows if r['use'] == 'product-card'
 and r['product_handle'] == 'titanium-hammered-pan-set-with-lids-6-pcs']

# wat gebruikt mail C1
[r['title'] for r in rows if 'C1' in r['used_in'].split(',')]

# alle shootbeelden, breed formaat
[r for r in rows if r['source'] == 'drive-shoot' and r['folder_or_product'].endswith('images')]
```

Of in de shell: `grep ',hero,no,' content/assets/index.csv | grep crepe`.

Let op: `hero` is een oordeel op een thumbnail van 300 px. Controleer voor gebruik altijd het origineel (scherpte, uitsnede op 600 px breed) en de herkomst: een deel is AI-gegenereerd of stock.

## Verversen

```
python3 -I scripts/refresh_assets.py --dumps /pad/naar/dumps     # Shopify + shoot
python3 -I scripts/refresh_assets.py --no-drive                   # alleen afgeleide kolommen opnieuw
python3 -I scripts/refresh_assets.py --dumps DIR --dry-run        # alleen tellen
```

Zonder `--dumps` blijven de Shopify-rijen zoals ze zijn. Met `--dumps` worden alle Shopify-rijen opnieuw opgebouwd uit de dumps; voor bestaande rijen blijven `category`, `use`, `text_in_image` en `product_handle` staan, nieuwe rijen krijgen een geraden categorie (staat in notes). Drive-shoot wordt gelezen via `https://drive.google.com/embeddedfolderview?id=<id>` (mappen `1eGJRW_AeQvbuYPHqnLuqBhy-VQd1SApd` images en `1bvJPfwpE70CMgDKMsUo9uiDTWIxQfRph` square), afmetingen via de eerste 64 KB van `drive.usercontent.google.com`. Zonder netwerk valt het script terug op `content/media/hp-shoot/index.csv`. Drive ad statics en Figma worden niet ververst (die kwamen uit de eerste crawl).

Volgorde voor `use` en `text_in_image`: `visual-checks.csv` gaat voor de bestaande waarde in index.csv, die gaat voor de regels op category en titel. Ad statics worden altijd `not-for-email` met tekst.

### De Shopify-dumps maken

Met de Shopify MCP-tool `graphql_query` (of de Admin API). Pagineer met `after: <endCursor>` tot `hasNextPage` false is en sla elke pagina op als `.json` in één map. Bestandsnamen maken niet uit, het script herkent `products` en `files` aan de inhoud.

Producten (alle statussen, ook draft en archived):

```graphql
query Products($after: String) {
  products(first: 50, after: $after) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id title handle status
      images(first: 100) { nodes { id url altText width height } }
    }
  }
}
```

Files (alleen afbeeldingen):

```graphql
query Files($after: String) {
  files(first: 250, after: $after, query: "media_type:IMAGE") {
    pageInfo { hasNextPage endCursor }
    nodes {
      ... on MediaImage {
        id alt createdAt
        image { url width height }
        originalSource { fileSize }
      }
    }
  }
}
```

Nieuwe beelden na een refresh zijn nog niet bekeken: hun `text_in_image` is `unknown` (of `yes` bij ad statics). Bekijk ze (thumbnail via `&width=300`) en zet het oordeel in `visual-checks.csv` (kolommen `key` = numeriek Shopify-id of Drive-id, `url_path` = CDN-url zonder query, `use`, `text_in_image`, `method`, `checked_on`), daarna het script nog eens draaien.
