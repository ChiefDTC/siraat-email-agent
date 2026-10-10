# 18 · K1 cart: voorstel links naar de cart en grotere productkaart

Datum: 10 okt 2026. Vervolg op `17-k1-check.md`. Alleen lokaal gebouwd en gerenderd, niets in Klaviyo gewijzigd (geen API-writes, geen uploads, geen sends).

**Figma:** https://www.figma.com/design/ahGP2wWoVIif8ETXcBq1Dj?node-id=79-2 (bestand Flow System v4, pagina "K1 cart · nu vs nieuw (10 okt)", frame "K1 vergelijking" 79:3).
Screenshot van de Figma-pagina: `img/18-k1-figma.png`.

![Figma nu vs nieuw](img/18-k1-figma.png)

## Bestanden

- Bron nieuw: `klaviyo/templates/v3/cart/k1-v2.html`, gebouwd met `build_template.py` naar `k1-v2.klaviyo.html` en `k1-v2-preview.html`. Huidig: `k1.html` (live als UQkhFj), ongewijzigd.
- Screenshots (echt Added to Cart-event, US, Titanium Hammered Pan Pro Standard, Qty 1, Price 144, CompareAtPrice 288, VariantID 51034913571156; voornaam "Alex", geen klantgegevens):
  - nu: `img/18-k1-nu-375.jpg` (mobiel, volle lengte), `img/18-k1-nu-600.jpg`
  - nieuw: `img/18-k1-nieuw-375.jpg`, `img/18-k1-nieuw-600.jpg`, `img/18-k1-nieuw-gmailios.jpg`

## A. Linkwijzigingen per element

Cart-permalink: `https://siraatskitchen.com/cart{% if event.VariantID %}/{{ event.VariantID }}:{{ event.Quantity|default:1|floatformat:0 }}{% endif %}?utm_source=klaviyo&utm_medium=email&utm_campaign=v4-cart&utm_content=k1-<blok>`. Zonder VariantID wordt dat `/cart`.

| Element | Nu | Nieuw |
|---|---|---|
| Hero (utm k1-hero) | productpagina uit `event.URL` (bijv. `/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern`); op een ander apparaat of in de Gmail-browser is de cart daar leeg | `/cart/51034913571156:1`: Shopify opent de checkout met de pan erin, op elk apparaat |
| Productkaart (utm k1-product) | alleen het beeld van 88 px, naar de productpagina | beeld op volle breedte en productnaam, naar de cart-permalink |
| Knop 1 (utm k1-cta1) | "Finish my order" naar de productpagina | "Complete my order" naar de cart-permalink |
| Knop 2 (utm k1-cta2) | "Finish my order" naar de productpagina | "Complete my order" naar de cart-permalink |
| Header, nav, footer | ongewijzigd | ongewijzigd |

Gecontroleerd op vijf renders: echt event (permalink), zonder VariantID (`/cart`), EUR/NL (permalink, geen prijs), CompareAtPrice gelijk aan Price (geen streep), leeg event (`/cart`, placeholderbeeld).

## Knopteksten

- Beide knoppen: **Complete my order** (was "Finish my order"). Ik-vorm met voordeel volgens de skill siraat-direct-response; de knop opent nu echt de checkout met het product erin, dus belofte en bestemming kloppen.
- Friction reducer onder beide knoppen ongewijzigd: `Free shipping from the US. 30-day returns. 100,000+ happy customers.` (via `{{FRICTION}}`).
- Valt de gifttest tegen en gaan we naar `?storefront=true` of `/cart`, dan wordt de knop **Return to my cart** (PLAYBOOK 10).

## B. Productkaart

- Beeld op volle breedte (478 px desktop, ca. 297 px op 375 px, Shopify-beeld met `&width=1000`), was 88 px. Fallbackbeeld (264 px) blijft op eigen maat.
- Productnaam 18 px (klikbaar), `Qty 1` links, prijs rechts.
- Prijs alleen bij USD (`{{IF:US}}` plus `$currency == 'USD'`, zoals nu). Compare-at doorgestreept alleen als `event.CompareAtPrice > event.Price`: in het voorbeeld ~~$288.00~~ $144.00.
- **[VRAAG FLORIS] compare-at bevestigen.** Shopify geeft nu $288 bij $144 voor de Pan Pro Standard; PLAYBOOK 12 noemt $439 bij $134 als bevestigd anker en zegt dat andere maten geen bevestigde compare-at hebben. Zonder akkoord de compare-at-regel weglaten.
- Inline gebouwd met dezelfde technieken als `partials/blocks/productcard.html` (geneste tabellen, `bgcolor` plus inline `background-color` op elk vlak, geen classes nodig). Het blok zelf kan het niet: daar is het beeld max 200 px en de was-prijs een vaste waarde, hier komen beeld en prijzen uit het event.

## Checks

- `mail_checks.preview_problems` en `bg_problems`: 0 op ruwe HTML en op alle vijf renders (huidig en nieuw).
- `qa_render.after_render`: 0 problemen. Browser (`qa_mail_shots.js`) light 375/600, gmailios, gmailtrim: geen overflow, geen kapotte of afgesneden beelden, geen lege cellen, geen contrastproblemen. Gmail iOS schaalt in tot 84 procent, net als nu.
- Lengte op 375 px: nu 3.456 px, nieuw 3.738 px. Boven de richtlijn van 3.600, onder de harde grens van 3.780. Bij akkoord inkorten (bijv. de closer look, die nu deels dubbel is met het grote productbeeld).
- Geen gedachtestreepje, geen kortingscode.

## Nog testen voor livegang

1. **Gifts bij de cart-permalink.** De permalink gaat met een 302 direct naar de Shop Pay-checkout en slaat de gift-app op de cartpagina over. Testorder: komen de 4 gifts mee? Zo niet: `?storefront=true` (landt op de cartpagina) of `/cart`.
2. **Meerdere producten.** De permalink maakt een cart met alleen het triggerproduct. Tellen hoe vaak een K1-cart meer dan één product heeft; zo ja, overwegen `/cart` te gebruiken voor die gevallen.
3. **Compare-at** door Floris laten bevestigen (zie B).
4. UTM's op een permalink: in een testklik controleren dat `utm_content` in de checkout-sessie terechtkomt.
5. Daarna pas export via `export_klaviyo.py` (dry-run, dan live) en een testmail met een uniek onderwerp.
