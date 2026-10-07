# 04 · Voorgestelde wijzigingen voor klaviyo/flows/v3-flow-system.md (en v3-new-flows.md)

Niet zelf doorgevoerd in het flowdocument (een timing-agent levert ook wijzigingen). Hieronder per sectie wat erbij of anders moet, klaar om samen te voegen. Achtergrond: 00-data.md (cijfers), 01-journey-matrix.md (mismatches), 03-routing.md (exacte filters).

## A. Nieuwe sectie bovenaan, na "Prioriteit tussen flows"

> ### Categorie-router (vanaf 7 oktober 2026)
> Elke verkoop- en klantflow kent vier paden: KOOKGEREI, SET, ACCESSOIRE, BESTAANDE KLANT. Accessoire = geen enkel kookgerei of set in de cart/order (15% van de checkouts, 9,5% van de orders). Nooit pan-uitleg aan een accessoire-cart. Bestaande klanten krijgen geen merkuitleg (C2) en geen brug-mail (C3-acc).
> Splitvelden: `Items` (lijst, exacte titels, `contains-any`) bij Checkout Started en Placed Order; `Product Name` / `Name` (string, substring) bij Added to Cart en Viewed Product. Titellijsten en kookgerei-woorden: research/tailoring/03-routing.md.
> Prijzen: alleen tonen in USD (cart: `$currency`) of bij verzendland US (post-purchase, winback: `shipping_address.country_code`). 37% van de orders gaat buiten de US.

## B. Sectie 1, Checkout abandonment

Vervangen: "Split op cart-waarde: event value >= $300 ..." door:

- Trigger filter: `$value` greater than 0 (sluit carts met alleen gratis gifts uit).
- Na C1: trigger split `Items contains-any KOOK_TITELS + SET_TITELS`. JA = kookgerei-pad, NEE = accessoire-pad.
- Kookgerei-pad: conditional split "Placed Order at least once over all time": JA slaat C2 over. C3: S als `$value >= 300` of `Items contains-any SET_TITELS`; P als `Items contains-any PANPRO_TITELS` en `$value < 250`; anders geen C3.
- Accessoire-pad: C2-acc (dag 2) → C3-acc alleen als Placed Order = 0 over all time (dag 3) → C4-US/C4-INT (dag 4).

Tabel, nieuwe regels:

| Stap | Wachttijd | Mail | Split en filter |
| --- | --- | --- | --- |
| 1-acc | tot dag 2, 09:00 | C2-acc Yours, or a gift? (feitregel per accessoire, cadeau-hoek) | Accessoire-pad. Geen order |
| 2-acc | 1 dag | C3-acc Most kitchens start with the pan (cart blijft hoofdknop) | Alleen Placed Order = 0 over all time |

A/B C1: onderwerp B "Your pan is still here" is fout bij 15% van de carts. Vervangen door "Your cart is still here (+10% off)" of in het onderwerp zelf: `{% if 'Pan' in event.Items|join:',' %}Your pan is still here{% else %}Your cart is still here{% endif %}`.

## C. Sectie 2, Cart abandonment

- Trigger filters: `Price` greater than 0; `Product Name` doesn't contain "Mystery Gift", "E-Book", "Free Shipping", "Giveaway". 47% van alle Added to Cart-events is een automatisch toegevoegde gift; 3,8% van de flow-starts zou nu op een gift beginnen.
- Na 1 uur: conditional split "Added to Cart where Product Name contains Hammer / Pan / Pot / ookware / Everything / fanne / Prep Bundle, at least once in the last 1 day". JA = K1 → K2 → K3 (ongewijzigd). NEE = K1-acc → (2 dagen) → K3.

| Stap | Wachttijd | Mail | Split |
| --- | --- | --- | --- |
| 0-acc | 1 uur | K1-acc Picked it out? It's still here. | Accessoire-pad |
| 2-acc | 2 dagen | K3 | Accessoire-pad (geen K2: de jaarsom gaat over een pan) |

## D. Sectie 3, Browse abandonment

- Na 4 uur: trigger split `Name` contains kookgerei-woorden. JA = B1 → B2. NEE = B1-acc → (2 dagen) → B2-clicked als er geklikt is, anders einde.

## E. Sectie 5, Post-purchase

Vervangen: "Split op gekocht product: pan = deksel en snijplank; set = vaatwasstrips en extra pan; accessoire = Pan Pro" door de P3-router:

1. Placed Order count over all time = 2 → geen P3 (VIP V1 op dag 30 heeft al een 15%-code; nu krijgen ~140 per week twee codes binnen 16 dagen).
2. Kookgerei of set in de order:
   - set of `$value >= 300` → P3-set
   - `Items contains-any` "Stainless Steel Lid", "Titanium Hammered Pan Pro With Lid" → **P3-next** (hoofdkaart snijplank; ~135 per week kregen nu "The lid, 10% off" voor een deksel die al onderweg was)
   - Pan Pro, wok, deep, crêpe → P3-pan
   - alleen pizza steel, roasting pan of pots → P3-accessory ("Now meet the pan")
3. Alleen accessoires:
   - E-Gift Card → geen P3
   - heeft eerder kookgerei gekocht → **P3-next** (hoofdkaart deksel, of plank als er een deksel in de order zat)
   - schort → **P3-apron**
   - anders → P3-accessory

P2: alleen als `Items contains-any KOOK_TITELS + SET_TITELS` (trigger split vóór de conditional wait). Accessoire-orders krijgen geen chef-eierles (~110 per week).

## F. Sectie 6, Winback

- R1: vóór de bestaande pan/set-split een trigger split `Items contains-any KOOK_TITELS + SET_TITELS`. NEE + nooit kookgerei gekocht → **R1-acc**; NEE + wel eerder kookgerei → R1-pan.

## G. Sectie "Segmenten die nodig zijn"

Toevoegen:
- `HEEFT_KOOKGEREI`: Placed Order where Items contains-any KOOK_TITELS + SET_TITELS, at least once, over all time.
- Set-kopers: `Items contains-any SET_TITELS` of value >= $300 (niet "Items bevat Set": dat matcht ook "Salt & Pepper Mill Set" en "Titanium Utensil Set Bundle").

## H. v3-new-flows.md

- UGC (sectie 8): flow filter erbij: `HEEFT_KOOKGEREI`.
- Anniversary (sectie 7): trigger filter: Placed Order `Items contains-any KOOK_TITELS + SET_TITELS`.
- VIP: tekst "start pas 30 dagen na de 2e order, dus na het P3-codevenster" klopt niet meer als P3 bij order 2 vervalt; aanpassen naar "P3 slaat order 2 over, V1 is de enige code".

## I. Lijst van elke wijziging in mails (7 oktober 2026)

Nieuw (bron, `-preview.html` met voorbeeld-event, `previews/` desktop 700 en mobiel 390):

| Mail | Map | Hero (bron, register) | Mobiel |
| --- | --- | --- | --- |
| c2-acc | checkout | Apron_Ember.webp (stel in Ember- en Moss-schort), 4:3, HI10-balk | 2.871 px |
| c3-acc | checkout | apron_lifestyle_image.webp (kok in Moss-schort met pan), 4:3 | ~2.800 px |
| k1-acc | cart | ApronAzureEating.webp, 4:3 | ~2.950 px |
| b1-acc | browse | apronmossspaghetti.webp, 4:3 | ~3.000 px |
| p3-next | post-purchase | Photo_Tossing_Vegetables_in_Pan_Pro.jpg, 1:1, codebalk P3 | ~3.320 px |
| p3-apron | post-purchase | Photo_Salmon_Cooking_with_Herbs_in_Pan_Pro.jpg, 1:1, codebalk P3 | ~3.560 px |
| r1-acc | winback | Photo_Three_Pans_with_Vegetables_on_Stove_Pro.jpg, 1:1, HI10-balk | ~3.340 px |

Extra variant-previews (zelfde template, ander voorbeeld-event): `checkout/c1-preview-schort.html`, `checkout/c4-us-preview-schort.html`, `checkout/c2-acc-preview-plank.html`, `post-purchase/p1-first-preview-schort.html`, `post-purchase/p3-next-preview-deeppan.html`, `browse/b2-clicked-preview-deksel.html` (met PNG's in `previews/`).

Gewijzigd (alle opnieuw gebouwd en gerenderd; originelen staan in git):

| Mail | Wijziging |
| --- | --- |
| checkout/c1 | Features-blok "One pan. Nothing to wear off." alleen bij kookgerei in de cart |
| checkout/c4-us | Blok "Cooking for a full house? The 12-piece set" alleen bij kookgerei in de cart |
| cart/k1, k2-new, k2-returning, k3 | Prijs in de productkaart alleen bij `$currency` USD |
| browse/b1 | Knoplabel (3x) en eyebrow: "set" of "pan" naar bekeken product |
| browse/b2-notclicked | Knoplabel (3x): "set" of "pan" |
| browse/b2-clicked | Features-blok alleen bij kookgerei; subregel "Pure titanium cooking surface" alleen bij kookgerei ("Pure titanium" bij plank en utensils, anders "From Siraat's Kitchen"); eyebrow neutraal |
| post-purchase/p1-first | Intro "Thank you for choosing a pan..." alleen bij kookgerei (anders "Thank you for ordering from us..."); kop "From order to first egg" / "From order to your door"; tijdlijnregel "your first cook" en chef-tip alleen bij kookgerei |
| post-purchase/p3-pan | "Made for your Pan Pro." wordt "Pick the same diameter as your pan." |
| winback/r1-pan | Deksel-rij alleen als de vorige order geen deksel had; "Fits the Pan Pro you already own" wordt "Fits the pan you already own: match the diameter." |

Niet gewijzigd: scripts/, partials/, alle andere v3-mails.

Previews: de `-preview.html` van de gewijzigde en nieuwe mails is nu gerenderd met Django op een voorbeeld-event (research/tailoring/test), omdat build_template.py `{% if %}`-tags anders als tekst in de preview laat staan. De `.klaviyo.html` ontstaat pas na het uploaden van de nieuwe hero's (geen `klaviyo-urls.txt`-regels).

## J. Nog open (niet gebouwd, wel gezien)

1. P3-pan, P3-set, P3-accessory, R1-pan, R1-set, R2: USD-prijzen ook aan de 37% buitenlandse kopers. Zelfde regel als in P3-next toevoegen (`{% if event.extra.shipping_address.country_code == 'US' %}` rond elke prijsregel).
2. Reviews in C1, C4 en K3 gaan over de koekenpan; bij een accessoire-cart passen ze half. Laten zoals het is (sociale bewijskracht blijft geldig) of later de reviews ook voorwaardelijk maken.
3. K3 warranty-regel "Dents, a warped base, loose handles" bij een schort of molen: is de 75-year warranty winkelbreed? content/products zegt per product ja, PLAYBOOK zegt "op cookware". [VRAAG FLORIS]
4. C4-code op een e-gift card: geldt een Shopify-kortingscode op een gift card? Waarschijnlijk niet. Gift-card-carts eventueel uit C4 halen.
5. Pot Set 6-Pcs ($196k in 90 dagen) kwam niet voor in 800 orders en 800 checkouts. Titel in een echte order nakijken en aan KOOK_TITELS toevoegen; de woordtest ("Pot") vangt hem in templates al.
6. Dishwasher sheets: 10 of 30 vellen per pak. [VRAAG FLORIS]
7. Hero's c2acc, c3acc, k1acc, b1acc, p3-next, p3-apron, r1-acc uploaden naar de Klaviyo-bibliotheek; daarna `assets/klaviyo-urls.txt` aanvullen en opnieuw bouwen. In checkout ook `p-panpro.jpg` (kopie uit post-purchase) en in cart en browse `cart-fallback.jpg`.
8. Eén keer in Klaviyo een preview met een echt profiel draaien voor C1, C2-acc en P3-next om `join` + `in` te bevestigen.
