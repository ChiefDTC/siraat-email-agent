# 04 · UTM-conventie per flow, mail en blok

Datum: 7 oktober 2026. Doel: in Shopify en GA4 zien welke flow, welke mail, welk blok en welke testvariant verkoopt. Klaviyo meet omzet per mail en per variant, maar niet per knop of blok; dat doen de UTM's.

## 1. De vijf parameters

| Parameter | Waarde | Voorbeeld |
| --- | --- | --- |
| `utm_source` | altijd `klaviyo` | `klaviyo` |
| `utm_medium` | altijd `email` (later `sms` voor SMS-flows) | `email` |
| `utm_campaign` | flow-slug (tabel §2), nooit de Klaviyo-flownaam met datum | `v4-checkout` |
| `utm_content` | `<mailid>-<blok>` (tabel §3 en §4) | `c4us-offer` |
| `utm_term` | testvariant: `<testid>-<a|b>`, of weglaten buiten een test | `t02-b` |

Regels:
- Alleen kleine letters, cijfers en koppeltekens. Geen spaties, geen underscores, maximaal 40 tekens per waarde.
- Nooit persoonsgegevens (e-mail, naam, Klaviyo-ID) in een UTM. Nooit een kortingscode in een UTM: unieke codes zouden dan in GA4 en in gedeelde links belanden.
- Mail-ID's zonder koppelteken (`c4us`, niet `c4-us`), zodat `utm_content` altijd precies één koppelteken tussen mail en blok heeft en simpel te splitsen is. Een tweede of derde knop van hetzelfde type krijgt een volgnummer: `cta1`, `cta2`, `cta3`.
- Elke A/B-variant is in Klaviyo een eigen template, dus `utm_term` staat hard in die template. Wisselt een test, dan wisselt de term.

## 2. `utm_campaign` per flow

| Flow | `utm_campaign` | Opmerking |
| --- | --- | --- |
| Welcome v3 | `v4-welcome` | |
| Checkout abandonment v3 | `v4-checkout` | |
| Cart abandonment v3 | `v4-cart` | |
| Browse abandonment v3 | `v4-browse` | |
| Post-purchase v3 | `v4-postpurchase` | |
| Winback v3 | `v4-winback` | |
| Review request (XzHrez) | `review` | Ongewijzigd laten tot de flow herbouwd wordt |
| Anniversary (n1, n2) | `v4-anniversary` | Nieuwe flow (parallelle bouw) |
| Site abandonment / keuzehulp (a1, a2) | `v4-site` | Nieuwe flow (parallelle bouw) |
| Sunset (s1, s2) | `v4-sunset` | s1 gebruikt nu `utm_campaign=sunse...`: gelijktrekken |
| UGC (u1) | `v4-ugc` | |
| VIP (v1, v2) | `v4-vip` | |
| Oud pad tijdens T01 | `old-<flow>` (bijv. `old-checkout`) | Via Klaviyo-instelling van de oude berichten (custom tracking params), templates niet aanpassen |

## 3. Mail-ID's

| Flow | Mail-ID's |
| --- | --- |
| Welcome | `w0`, `w1a`, `w1b`, `w2`, `w3`, `w4us`, `w4int`, `w5` |
| Checkout | `c1`, `c2`, `c3p`, `c3s`, `c4us`, `c4int`, later `c5` |
| Cart | `k1`, `k2new`, `k2ret`, `k3` |
| Browse | `b1`, `b2c` (clicked), `b2n` (not clicked) |
| Post-purchase | `p1first`, `p1rep`, `p2`, `p3pan`, `p3set`, `p3acc`, `p4` |
| Winback | `r1pan`, `r1set`, `r2`, `r2vip`, later `r3` |
| Nieuwe flows | `n1`, `n2`, `a1`, `a2`, `s1`, `s2`, `u1`, `v1`, `v2` |
| Testvarianten zonder code of zonder HI10 | zelfde mail-ID; het verschil zit in `utm_term` (`t02-b`, `t03-b`), niet in het mail-ID |

## 4. Blokken (`utm_content`-suffix)

Afgeleid van de blokken in `klaviyo/templates/partials/blocks/` en de opbouw van de v3-mails.

| Blok | Suffix | Waar |
| --- | --- | --- |
| Codebalk boven de header | `codebar` | bijna alle verkoopmails |
| Logo in de header | `logo` | header-partial |
| Navigatie header | `nav-cookware`, `nav-sets`, `nav-about` | header-partial |
| Hero-afbeelding en hero-knop | `hero` | elke mail met een beeldhero |
| Cart-blok (checkout) | `cart` | C1 t/m C4 |
| Productkaart (dynamisch product, browse en cart) | `product` | B1, B2, K1 t/m K3 |
| Productlijst met vaste producten | `prod-<kort>`: `prod-panpro`, `prod-set6`, `prod-set12`, `prod-duo`, `prod-lid`, `prod-board`, `prod-wok`, `prod-crepe`, `prod-2pan`, `prod-sheets`, `prod-utensils` | W4, W5, P3, R1, R2 |
| Primaire knoppen | `cta1`, `cta2`, `cta3` (van boven naar beneden) | alle mails |
| Aanbodblok (code, deadline, knop) | `offer` | W1-A, W3, W4, W5, C4, K2ret, K3, B2c, P3, R2 |
| Gift-card (W1-B) | `giftcard` | W1-B |
| Gift-stack | `gifts` | alle verkoopmails |
| Uitleg/features (drie kaarten) | `features` | |
| Reviews | `reviews` | |
| Vergelijking | `compare` | B1, W3 |
| Maatkiezer W4 | `size-mini`, `size-small`, `size-standard`, `size-large` | W4 |
| Drie instappen W4 | `tier1`, `tier2`, `tier3` | W4 |
| Labrapport-link | `report` | W3, C2, B1 |
| Garantie-link | `warranty` | K2new |
| P.S.-link founder note | `ps` | W2 |
| 12-delige set als alternatief | `set12` | C4-US |
| E-book | `ebook` | P1 |
| Kookgids, care & use | `guide` | W0, P2, n1 |
| Footer | `ft-cookware`, `ft-sets`, `ft-accessories`, `ft-testing`, `ft-fb`, `ft-ig` | footer-partial |

Vaste uitzonderingen zonder UTM: `{% unsubscribe %}`, `{% manage_preferences_url %}`, `{% web_view %}`, `mailto:`-links, Trustpilot-links in de reviewflow (extern domein).

## 5. Hoe het in de links komt

### 5.1 Klaviyo-instelling

Gezien op 7 oktober in de live checkoutflow Y2TmNB: `add_tracking_params: true`, `custom_tracking_params: null`. Klaviyo voegt dus nu zijn eigen standaard-UTM's toe (met de flownaam). Voor v3:
- Per bericht `add_tracking_params: true` laten en `custom_tracking_params` zetten op `utm_source=klaviyo`, `utm_medium=email`, `utm_campaign=<flow-slug>`. Dat vangt elke link die we vergeten.
- `utm_content` en `utm_term` staan hard in de HTML per link. **Te verifiëren in een testverzending:** dat Klaviyo een parameter die al in de link staat niet overschrijft of dubbel toevoegt. Als dat wel gebeurt: tracking params in Klaviyo uit voor v3 en alles in de HTML.

### 5.2 In de build, niet met de hand

`scripts/build_template.py` kent de bestandsnaam (mail-ID) en de blokken (`{{BLOCK:cta}}`, `{{BLOCK:offer}}`, enz.). Voorstel (niet uitgevoerd): een parameter `utm=` per blok, of automatisch: het script hangt `utm_content=<mailid>-<blok><volgnummer>` aan elke `[[url]]`, en leest `utm_term` uit de topcomment (`TEST: t02-b`). Zo blijft de conventie consistent over 40+ templates en hoeft niemand UTM's te typen. Header en footer (partials) krijgen hun suffix ook via het script.

### 5.3 Drie soorten links, drie manieren

**a) Gewone productlink**

```
https://siraatskitchen.com/products/stainless-steel-lid?utm_source=klaviyo&utm_medium=email&utm_campaign=v4-postpurchase&utm_content=p3pan-prod-lid&utm_term=t02-a
```

**b) Kortingslink via `/discount/<code>?redirect=<pad>`** (HI10 en unieke codes; het grootste deel van de v3-links)

Shopify zet bij `/discount/...` de korting in een cookie en stuurt door naar `redirect`. De sessie en dus de UTM-meting in Shopify en GA4 begint op de pagina waar de redirect landt. De UTM's moeten daarom **binnen** de redirect staan, URL-gecodeerd:

```
https://siraatskitchen.com/discount/HI10?redirect=%2Fproducts%2Foriginal-siraat-100-pure-titanium-pan-with-hammered-pattern%3Futm_source%3Dklaviyo%26utm_medium%3Demail%26utm_campaign%3Dv3-welcome%26utm_content%3Dw1a-offer%26utm_term%3Dt04-a
```

Bij een dynamisch pad (browse: `{{ event.URL|cut:'https://siraatskitchen.com'|default:'...' }}`) komt de UTM-string na het pad, gecodeerd (`%3Futm_source%3D...`). Als het eventpad zelf al een `?` bevat (variant-URL's), moet het `%26` worden: testen met een echt Viewed Product-event in een Klaviyo-preview.
Te verifiëren bij de eerste test: landt GA4 met de UTM's (DebugView), en blijft de korting staan in de cart.

**c) Checkout-link** (C1 t/m C4: `{{ event.extra.responsive_checkout_url }}&discount=...`)

UTM's achteraan toevoegen: `...&discount=CODE&utm_source=klaviyo&utm_medium=email&utm_campaign=v4-checkout&utm_content=c4us-cta1&utm_term=t02-a`. De fallback-URL in C4 (`https://siraatskitchen.com/checkout?utm_source=klaviyo&discount=...`) aanvullen met de overige vier. Checkout-pagina's tellen in Shopify mee als landingspagina; in GA4 alleen als de checkout-tracking (Shopify customer events) aanstaat. Controleren.

### 5.4 Cart-links

`/cart` (K1 t/m K3) toont een lege cart op een ander apparaat (build-notes cart punt 3). Dat is een conversieprobleem, geen UTM-probleem, maar de UTM maakt het zichtbaar: veel sessies op `k1-cta1` zonder add-to-cart in GA4 = dit lek.

## 6. Uitlezen

**GA4** (Explore, vrije vorm):
- Dimensies: Session source/medium, Session campaign, Session manual ad content, Session manual term.
- Metrics: Sessions, Add to carts, Purchases, Purchase revenue.
- Filter: Session source = klaviyo. Daarna `utm_content` in python splitsen op het eerste koppelteken: mail en blok.

**Shopify:** rapport sales/sessions per UTM (landingspagina). Via `mcp__Shopify__run-analytics-query` met ShopifyQL; de veldnamen voor UTM-parameters eerst opzoeken in de ShopifyQL-referentie (`mcp__Shopify__search_docs_chunks` of `mcp__Intelligems__get_shopifyql_reference`), niet raden.

**Wekelijkse vraag die dit beantwoordt** (blok in het dashboard, 03 §1.1):
1. Per mail: welk blok levert de meeste sessies en orders (hero, cart, offer, cta1, cta3, product)? Als `cta3` vrijwel niets doet, is de mail te lang (input voor T08).
2. Per test: `utm_term` a tegen b in sessies en orders, als tweede bron naast Klaviyo.
3. Codebalk: klikken mensen op de balk zelf? Zo niet, dan is het een label en geen knop.

## 7. Checklist per template vóór livegang

- [ ] Elke `href` naar siraatskitchen.com heeft `utm_content=<mailid>-<blok>`.
- [ ] Bij `/discount/`-links staan de UTM's gecodeerd in `redirect`.
- [ ] Testvarianten hebben de juiste `utm_term`.
- [ ] Geen kortingscode in een UTM-waarde.
- [ ] In Klaviyo: `custom_tracking_params` met source, medium en flow-slug.
- [ ] Eén testverzending: links aanklikken, GA4 DebugView en Shopify-landingspagina controleren, korting in de cart controleren.
