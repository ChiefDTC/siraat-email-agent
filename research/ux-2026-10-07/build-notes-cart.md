# Bouwnotities cart (K1, K2-new, K2-returning, K3)

Datum: 7 oktober 2026. Bron-HTML gegenereerd en gebouwd volgens PLAYBOOK 10 en 11, referentie C1.

## Per mail
| Mail | Hero (label / kop / subregel) | Aanbodbalk | Mobiel | Knoppen |
| --- | --- | --- | --- | --- |
| K1 | STILL IN YOUR CART / One wipe. 10% off. / Code HI10 on top of the sale. No scrubbing. | EXTRA 10% OFF WITH HI10 · $70 IN GIFTS | 3.326 px | 3x Finish my order |
| K2-new | STILL IN YOUR CART / $1.79 a year. Now 10% off. / Covered for 75 years. Code HI10 inside. | idem | 3.183 px | 3x Finish my order |
| K2-returning | WELCOME BACK / Your cart, 10% off. / A thank-you for coming back. | idem | 3.136 px | 2x knop + knop in aanbodblok |
| K3 | YOUR CODE · 48 HOURS / Your cart, now 10% less. / Your personal code. 30-day returns. | YOUR 10% CODE EXPIRES IN 48 HOURS | 3.422 px | 2x knop + knop in aanbodblok |

Volgorde overal: codebalk · header · hero 4:3 · productkaart (inline, stijl BLOCK:cart, met HI10- of coderegel) · knop · (rekensom K2-new / aanbodblok K2-returning en K3) · gifts · uitleg (features) · reviews · knop · iconen · Benjamin · footer.
Alle links: `https://siraatskitchen.com/discount/HI10?redirect=/cart`; K3: `https://siraatskitchen.com/discount/{% coupon_code 'K3_10_48H' %}?redirect=/cart`.

## Coupons (niet aangemaakt, alleen nodig)
- `K3_10_48H`: Klaviyo-coupon, Shopify unique codes, 10% op one-time purchase products, vervalt 2 dagen na toewijzing, 1 gebruik, 1 per klant. Wordt 7 keer in K3 aangeroepen (codebalk, links, codevak): in een Klaviyo-preview controleren dat het overal dezelfde code is.

## Eventvelden (gecontroleerd op echte events in Klaviyo, alleen gelezen)
- De cartflow (SwkMyn, live) draait op metric QXcV8K "Added to Cart" (Shopify). Die heeft `Product Name` (met spatie), `ImageURL`, `Price` (getal, bijv. 129), `Quantity`, `CompareAtPrice` (getal) en `URL` (op het myshopify-domein).
- **Bug in de oude templates:** die gebruikten `event.ProductName`; dat veld bestaat niet, dus elke mail toonde de fallback "Titanium Hammered Pan Pro", ook bij een pizza steel. Nu: `{{ event|lookup:'Product Name'|default:... }}`.

## Besluiten voor Floris / open punten
1. K1 en K2 geven nu HI10 in de hero (opdracht: aanbod in elke hero). 04-offer-strategy raadde in K1/K2 geen code aan; zo een A/B-holdout (K1 zonder HI10) overwegen.
2. K3 hoort per tak: unieke code / HI10-herinnering (welcome-lijst) / alleen gifts (cooldown 30 dagen). Nu is alleen de code-variant gebouwd. Flow-split en profieleigenschap `last_flow_code_at` instellen.
3. Cart-link `/cart` is leeg op een ander apparaat. Alternatief: product-URL uit het event, maar die staat op het myshopify-domein. Floris kiezen.
4. K2-new rekensom gebruikt $134 (Pan Pro Standard); bij een ander product in de cart klopt $1.79 niet exact (voetnoot staat erin).
5. Gift-waardes ($15, $30, $25, $450) en "chance to win" bevestigen; compare-at niet getoond (Pan Pro $439 nog verifiëren).
6. K3-hero is een uitsnede van een kopie van de chef-still (`cart/assets/_src/k3-steak-sear-crop.jpg`, ondertitel weggesneden); 2x opgeschaald, onder de laag acceptabel.
7. Geen klaviyo-urls.txt in assets: hero's nog uploaden, daarna opnieuw bouwen voor `.klaviyo.html`. Oude `tint.gif` wordt niet meer gebruikt.
8. Preview: productbeeld, naam en prijs zijn na de build met voorbeelddata ingevuld (product-sample.jpg), omdat build_template alle `{{ event... }}` vervangt door `#`.
