# 17 · K1 cart abandonment: waarom zo weinig kliks?

Datum: 10 okt 2026, ca. 12:30 UTC. Alleen GET-calls en lokale rendering, niets live gewijzigd.
Flow `v4 · Cart abandonment` (TZG9Mx), K1 = message Vb6YFp (template UQkhFj), oud = `Old · Cart 1` VN83i2 (template XAxUNv).
Aanleiding: performance-check 10 okt 12:30 (1 unieke klik op 74 ontvangers voor K1, 5 op 78 plus 1 order voor oud).

## Cijfers (eigen telling uit events, sinds 8 okt 22:30 UTC tot 10 okt ca. 12:20 UTC)

| | K1 (Vb6YFp) | Oud Cart 1 (VN83i2) |
|---|---|---|
| Received Email | 83 | 88 |
| Unieke openers (alle) | 32 | 34 |
| Unieke openers zonder machine_open (echte opens) | 8 | 16 |
| Unieke klikkers | 1 | 5 (11 klikken, 6 van één profiel) |
| Order na ontvangst (profiel-match, elke attributie) | 1 | 2 |
| Checkout Started na ontvangst | 2 | 3 |

K1-ACC (SKE4yh, accessoires) kreeg 6 ontvangers, 0 kliks. De rapportcijfers 74/78 zijn een eerdere stand, de verhouding is gelijk.

## 1. Flowlogica: wie krijgt K1, wanneer

- Trigger Added to Cart (QXcV8K), Price > 0, geen Mystery Gift, E-Book, Free Shipping of Giveaway.
- Flowfilters voor beide armen gelijk: geen Checkout Started en geen Placed Order sinds flowstart, geen Received Email uit checkout-flow QUBUQV in 7 dagen, niet in deze flow in 14 dagen.
- Eerste split: 50/50 random (profile-sample). Waar-arm = nieuw: 30 min wachten, dan split pan/accessoire (ATC in 1 dag met Hammer, Pan, Pot, ookware, Everything, fanne of Prep Bundle) naar K1, anders K1-ACC. Onwaar-arm = oud: 15 min wachten, dan Old Cart 1.
- Message-filters: K1 sluit Checkout Started en Placed Order uit, oud alleen Placed Order. Omdat de flowfilter Checkout Started al voor iedereen uitsluit, maakt dat geen verschil.
- Conclusie: beide armen krijgen dezelfde soort mensen (random 50/50, 83 tegen 88). Verschillen: K1 komt 15 minuten later, en de oude arm bevat ook accessoire-winkelwagens (11 lids, borden, schorten), die in de nieuwe arm naar K1-ACC gaan. K1 krijgt dus alleen de pan-carts (44 van 83 een Hammered Pan Pro, verder sets, deep pan, wok). Geen fout in de logica gevonden.

## 2. Template en rendering

Live K1 (UQkhFj) komt inhoudelijk overeen met `klaviyo/templates/v3/cart/k1.klaviyo.html` (alleen door Klaviyo genormaliseerde attributen).

Variabelen die K1 gebruikt: `event.URL` (met `cut` naar een pad, fallback `/cart`), `event.ImageURL` (in `{% if %}`), `event|lookup:'Product Name'` (fallback "Your item"), `event.Quantity`, `event.Price` (alleen bij `$currency == 'USD'`), `event|lookup:'_ip_country_code'` voor giftbedragen per markt.
In 1.567 echte Added to Cart events van 8 tot 10 okt hebben alle events URL, ImageURL, Product Name, Price, Quantity, `$currency` en `_ip_country_code`. Geen URL met querystring (dus geen dubbele `?`). Voor alle 83 K1-ontvangers was een triggerevent met beeld te vinden.

Gerenderd met Django op 8 echte events van K1-ontvangers (US, CA, SG, AU; pan, set 6, set 12, deep pan) plus een leeg event, daarna `qa_mail_shots.js` op 375 px in light, apple, gmailios en gmailtrim:
- Geen lege productkaart, beeld laadt, geen overflow, geen lege tekstcellen, geen contrastproblemen. Leeg event valt netjes terug op placeholderbeeld en `/cart`.
- gmailios schaalt de mail in (gmailScale 0,84, hero 448 px), bekend en leesbaar.
- gmailtrim: alleen de social-iconen in het getrimde deel laden niet (simulatie-artefact, onschuldig).
- Prijs staat er alleen bij US-bezoekers met USD. Geen compare-at prijs, terwijl CompareAtPrice in elk event zit (bijv. 139 tegen 455).
- Screenshots: `img/17-k1-apple-licht.jpg`, `img/17-k1-gmailios.jpg`.

De rendering is dus niet de oorzaak: de productkaart en knop zijn er voor iedere ontvanger.

Oud Cart 1 (drag-and-drop) is niet lokaal te renderen (`feeds.Abandoned_Cart|index` is Klaviyo-specifiek, feed niet lokaal). Opbouw statisch: groot beeld naar `event.URL`, daarna twee productkaarten uit de feed met beeld, prijs en doorgestreepte compare-at en knop "GO TO CART" (naar de productpagina), vier beeldblokken naar `event.URL`.

## 3. Links in K1

- Hero, productkaart, knop 1 ("Finish my order →") en knop 2 gaan alle vier naar `https://siraatskitchen.com` + pad uit `event.URL`, dus naar de **productpagina** van het eerste product, niet naar de winkelwagen of checkout. `/cart` alleen als URL ontbreekt (kwam niet voor).
- Nav en footer: home, collections/pans, bundles, accessories, about-us, third-party-testing.
- HTTP-status (curl, iPhone UA): alle siraatskitchen.com-links en alle productpagina's uit de K1-carts 200 zonder redirect. Instagram/Facebook niet testbaar via de proxy.
- Primaire CTA: op 375 px staat "Finish my order" op ca. 655 tot 708 px. Op een iPhone in Mail of Gmail is dat rond of net onder de vouw; hero en productkaart (ook klikbaar) staan erboven.
- Probleem: de knop belooft "Finish my order" maar opent een productpagina. Op een ander apparaat of in de in-app browser van Gmail is de winkelwagen leeg, dus de klant moet opnieuw toevoegen. Dat raakt conversie na de klik, niet het aantal kliks. De oude mail linkt ook naar productpagina's.
- Cart-permalink `https://siraatskitchen.com/cart/{VariantID}:{Quantity}` werkt (302 naar Shop Pay-checkout); VariantID zit in elk event.

## 4. Onderwerp en preview

| | Onderwerp | Preview |
|---|---|---|
| K1 | The hammered pattern: an easy wipe | Less food touches the metal, so cleanup is a quick wipe. Your cart is saved. |
| Oud | Hi {{ first_name }}, we saved these for you | Get Cooking Now |

- `mail_checks.preview_problems`: K1 0 problemen (inbox toont alleen de preheader). Oud: 2 problemen (tekst voor de preheader, geen opvulling, body loopt de preview in).
- Alle opens vrijwel gelijk (32 tegen 34), maar die zijn vooral Apple MPP. Echte opens (zonder machine_open): 8 tegen 16. K1-onderwerp leest als productuitleg, niet als "je winkelwagen". Het woord cart staat pas aan het eind van de preview. Oud noemt de voornaam en "we saved these for you".

## 5. Klikdata (Clicked Email, property URL)

K1: 1 klik, `/products/titanium-hammered-pan-pro-mini?utm_content=k1-cta1` (knop 1, het eigen cartproduct). Geen order.

Oud: 11 kliks van 5 profielen, allemaal op iOS of Android mobiel:
- 6 kliks van één profiel: home, pan-pro-large (2x), stainless-steel-lid, standaardpan (met hammered pattern).
- stainless-steel-lid (2 profielen), standaardpan (2 profielen), pan-pro-large (1).
- Meerdere kliks gaan naar producten die NIET in de cart zaten (pan-pro-large bij iemand met small + lid, standaardpan bij iemand met wok). Die komen uit de twee feedkaarten. De oude mail scoort dus kliks met extra producten om door te bladeren, niet met de eigen cart.

## Toeval of echt?

Fisher exact: kliks 1/83 tegen 5/88 p = 0,21; echte opens 8/83 tegen 16/88 p = 0,13; klik per echte opener 1/8 tegen 5/16 p = 0,62; orders 1 tegen 2 p = 1,0. Vijf van de elf oude kliks komen van één persoon. Met deze aantallen is het verschil **waarschijnlijk grotendeels toeval**; er is geen technische fout. Pas bij ca. 300 tot 400 ontvangers per arm is een verschil van 1 tegen 6 procent klik betrouwbaar te zien (ongeveer een week bij het huidige volume).

## Oorzaak (meest waarschijnlijk)

Geen kapotte mail: flowlogica, variabelen, beelden, links en inbox-preview zijn in orde. Het verschil zit in de opzet:
1. **Onderwerp**: K1 opent met een productclaim in plaats van de winkelwagen. Half zo veel echte opens (8 tegen 16, nog niet significant).
2. **Eén klikdoel**: K1 toont alleen het eerste product (klein, 88 px) en elke link gaat naar dezelfde productpagina. Oud toont een groot beeld plus twee feedproducten met doorgestreepte compare-at prijs; daar kwamen de meeste oude kliks vandaan.
3. **Knop belooft wat de link niet doet**: "Finish my order" opent een productpagina, waar de cart op een ander apparaat leeg is. Dit verklaart niet het klikverschil, wel mogelijk minder orders na een klik.

## Fixvoorstel (niet uitgevoerd, wacht op akkoord)

1. Knoppen, hero en productkaart naar de cart-permalink: `https://siraatskitchen.com/cart/{{ event.VariantID }}:{{ event.Quantity|default:1|floatformat:0 }}` met fallback `/cart` als VariantID ontbreekt. Let op: de permalink gaat direct naar de checkout en slaat de gift-app op de cartpagina over; testen of de 4 gifts dan nog worden toegevoegd. Anders `?storefront=true` toevoegen (landt op de cartpagina) of `/cart` gebruiken.
2. Onderwerp A/B in K1: huidige regel tegen een cartregel, bijvoorbeeld "Your cart is saved, with 4 gifts" of "Still thinking about the {{ event|lookup:'Product Name'|truncatewords:4 }}?" (copy via siraat-direct-response-skill, geen kortingscode in K1).
3. Productkaart groter (beeld op volle breedte zoals de oude mail) en compare-at doorgestreept voor USD als `event.CompareAtPrice > event.Price`, binnen de bestaande US-voorwaarde.
4. Niet nu stoppen: A/B laten lopen tot ten minste 300 ontvangers per arm (rond 15 tot 17 okt), daarna opnieuw tellen op echte opens, kliks en orders. Fix 1 kan eerder, want die raakt alleen conversie na de klik.
