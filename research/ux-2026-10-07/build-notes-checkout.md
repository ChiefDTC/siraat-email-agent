# Build notes checkout (C2 tot C4), 7 oktober 2026

Referentie: C1 (niet aangepast). Hero-register: content/media/hero-register/checkout.csv.

## Per mail

| Mail | Hero (label / kop / subregel / aanbodbalk) | Mobiel | Desktop |
| --- | --- | --- | --- |
| C2 | STILL IN YOUR CART / Tested. Then 10% off. / Lab report 25895. Your cart is saved. / EXTRA 10% OFF WITH HI10 · $70 IN GIFTS | 3.441 px (was 4.004) | 3.538 px |
| C3-P | UPGRADE YOUR CART / Make it three / 3 pans + 3 lids for $349, plus HI10. / 6-PIECE SET $349 · EXTRA 10% WITH HI10 | 3.197 px (was 3.636) | 3.181 px |
| C3-S | 4 GIFTS WITH YOUR SET / Your set, 10% lighter / HI10 on top of the sale, plus 4 gifts. / EXTRA 10% OFF WITH HI10 · $70 IN GIFTS | 3.301 px (was 3.657) | 3.029 px |
| C4-US | LAST REMINDER / 10% off, 48 hours / Your own code, applied with one click. / YOUR 10% CODE EXPIRES IN 48 HOURS | 3.373 px (was 3.770) | 3.178 px |
| C4-INT | idem | 3.166 px (was 3.048) | 2.958 px |

Hero-werkwijze: voor P02, P022 en P07 eerst een donkerder werkkopie gemaakt in de scratch-map (horizontale band in het midden extra donker), omdat de subregel anders over glimmende deksels en kip viel. Originelen niet aangeraakt.

## Coupons (niet aangemaakt)

- **C4_10_48H**: Klaviyo unique coupon (Shopify), 10 procent, verloopt 48 uur na toewijzing, 1 gebruik, 1 per klant. Gebruikt in C4-US en C4-INT (codebalk, cart-regel, aanbodblok, knoplinks, link 12-delige set). Komt overeen met pool SK_CHECKOUT10_48H uit 04-offer-strategy; naam kiezen en in beide templates gelijk houden.
- Controleren in een Klaviyo-preview dat meerdere `{% coupon_code 'C4_10_48H' %}`-tags in één mail dezelfde code geven.
- Controleren of de coupon ook op de 12-delige set geldt (C4-US zegt "Your code works here too").

## Besluiten voor Floris / open punten

1. **HI10 in C2 en C3 tegen de offer-strategie.** 04-offer-strategy zegt: geen code in de eerste 48 uur, codes pas in de laatste mail. De brief (en C1) zet HI10 in elke checkout-hero. Gebouwd volgens de brief. Advies: A/B in C2 (met en zonder HI10).
2. **C4 voor HI10-profielen.** Wie al HI10 heeft (welcome-lijst Uw8eZG) krijgt in C4 een tweede 10 procent-code; één code per order, dus geen stapeling, maar wel onnodige korting. Voorstel: conditionele split vóór C4 (HI10-lijst krijgt C1-achtige mail met HI10-herinnering) plus 30 dagen cooldown.
3. **Fallback-link C4.** Zonder `responsive_checkout_url` valt de knop terug op `https://siraatskitchen.com/checkout?utm_source=klaviyo&discount=CODE`. Testen in een testcheckout, net als `&discount=` achter de checkout-URL in C1.
4. **6-delige set $349 of $399.** C3-P gebruikt $349 en linkt naar `titanium-hammered-pan-set-with-lids-6-pcs-bday-sale` (UNLISTED, $349). Als Floris naar $399 gaat: hero, aanbodbalk, rekensom ($116 per pan) en onderwerp aanpassen.
5. **Rekensom C3-P**: "One pan + lid $154+" komt uit products.csv (Pan Pro With Lid $154-169). Prijzen voor livegang tegen Shopify checken.
6. **Compare-at 12-delige set $1,186** (C4-US) verifiëren. Feitenbestand noemt de 12-pcs nog als backorder; DECISIONS (7 okt) zegt normaal tonen. Gevolgd: DECISIONS.
7. **Gift-waardes** ($15, $30, $25, $450) en de trekking: uit het standaard gifts-blok, nog door Floris te bevestigen.
8. **C3-P en C3-S hero-foto's** (P022 en P02) zijn dezelfde scène; ze zitten in verschillende takken (P/S) dus niemand ziet beide. P02/P022 tonen ook potten (12-delige set), terwijl C3-P de 6-delige set verkoopt. Liever later een foto met drie pannen en deksels.
9. **Nieuwe hero's** moeten nog naar de Klaviyo-bibliotheek; `assets/klaviyo-urls.txt` bestaat niet, dus build_template schrijft nog geen `.klaviyo.html`.
10. C2 mobiel is 3.441 px, net boven het doel van ~3.400 (footer alleen al ~550 px).
