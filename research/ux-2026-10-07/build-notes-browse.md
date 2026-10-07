# Bouwnotities browse (B1, B2-clicked, B2-notclicked)

Datum: 7 oktober 2026. Doel Floris: een echt aanbod met echte urgentie.

## Per mail
| Mail | Hero (label / kop / subregel) | Aanbodbalk | Mobiel | Knoppen |
| --- | --- | --- | --- | --- |
| B1 | THE PAN YOU VIEWED / 10% off the pan you looked at. / Code HI10, on top of the sale. Plus 4 gifts. | EXTRA 10% OFF WITH HI10 · $70 IN GIFTS | 3.163 px | 3x Get 10% off this pan |
| B2-clicked | 48 HOURS ONLY · YOUR CODE / 10% off, 48 hours. / On top of the sale. Plus 4 gifts. | YOUR 10% CODE EXPIRES IN 48 HOURS | 3.393 px | 2x Claim my 10% + knop in aanbodblok (deadline) |
| B2-notclicked | 100,000+ HAPPY CUSTOMERS / In their words. 10% off for you. / Code HI10 on top of the sale. | EXTRA 10% OFF WITH HI10 · $70 IN GIFTS | 3.289 px | 3x Get 10% off this pan |

Links: B1 en B2-notclicked `https://siraatskitchen.com/discount/HI10?redirect=<productpad>`, B2-clicked `https://siraatskitchen.com/discount/{% coupon_code 'B2_10_48H' %}?redirect=<productpad>`. Productpad = `{{ event.URL|cut:'https://siraatskitchen.com'|default:'/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern' }}`.
**Bug hersteld:** de knop "USE HI10 NOW" in B2-clicked ging naar de productpagina zonder korting; elke knop past nu de code toe.

## Coupons (niet aangemaakt, alleen nodig)
- `B2_10_48H`: Klaviyo-coupon, Shopify unique codes, 10% op one-time purchase products, vervalt 2 dagen na toewijzing, 1 gebruik, 1 per klant. In een Klaviyo-preview controleren dat codebalk, codevak en links dezelfde code tonen.

## Eventvelden (gecontroleerd op echte events, alleen gelezen)
- De live browseflow (Wj6x6V) draait op metric XNtYMB "Viewed Product". Velden: `Name`, `ImageURL`, `Price` (tekst met $, bijv. "$134"), `CompareAtPrice` ("$439"), `URL` (siraatskitchen.com), `Value`.
- **Bugs in de oude templates:** `event.ProductName` bestaat niet (altijd fallback-naam) en `${{ event.Price|floatformat:2 }}` op "$134" gaf een lege of kapotte prijs. Nu `event.Name` en `{{ event.Price }}` zoals het binnenkomt.

## Besluiten voor Floris / open punten
1. Klaviyo-filter `cut` testen in een preview met een echt event (redirect moet `/products/...` worden). Bij een www-URL valt hij terug op de Pan Pro-link.
2. B2-clicked: HI10-ontvangers (welcome-lijst) liever een HI10-herinnering dan een tweede code; split nog in te richten. Cooldown 30 dagen per profiel.
3. Test voorgesteld: B2-clicked code tegen geen code (holdout).
4. Publieke lekcodes (BFEXTRA10, EXTRA30, enz.) maken "expires in 48 hours" commercieel zwak; zie 04-offer-strategy.
5. B1 vergelijkingsrij "Lab report you can read: Not always / No. 25895" (vervangt "Warranty: Varies by brand").
6. B2-hero's zijn uitsnedes van kopieën van chef-stills zonder ondertitel (`browse/assets/_src/`), ongeveer 1,6x opgeschaald.
7. Hero's nog uploaden (geen klaviyo-urls.txt). Oude `water-test.gif` wordt niet meer gebruikt (had ingebakken tekst).
