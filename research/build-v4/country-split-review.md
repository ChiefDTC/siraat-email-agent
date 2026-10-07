# Landsplit in de checkout-flow: nodig of niet?

Review 7 oktober 2026. Flow `v4 · Checkout abandonment` (Y6yj2z, Draft), stap 5K-6K. Niets gewijzigd in Klaviyo of Shopify.

## Kort antwoord

De split heeft een echte reden, maar hij is te zwaar gebouwd en bevat een fout. Advies: **vereenvoudigen**. Eén C4-mail (plus de nocode-versie) die zelf het land kiest met een `{% if %}`. Dan heeft de flow 2 splits in plaats van 11, en 3 C4-mails in plaats van 12.

## Waarom de split er is

Er zijn twee verschillen tussen de US- en de INT-mail die er echt toe doen:

1. **De 12-delige set wordt alleen in de US verkocht** (bevestigd door de eigenaar; de productpagina geeft buiten de US-winkel een 404). Een buitenlandse klant mag die kaart dus niet zien.
2. **Internationale orders zijn "duties paid"** (bevestigd door de eigenaar). Dat haalt de grootste twijfel van buitenlandse klanten weg.

De rest van de mail is woord voor woord hetzelfde. Voor twee blokken heb je geen aparte tak nodig. Dat regel je in de mail zelf, en de mails C1 tot en met C3 doen dat al zo.

## Wat er misgaat

- **Fout:** bij 3% van de checkouts staat in het profiel "US" in plaats van "United States". De split ziet die klanten als buitenland, dus Amerikanen krijgen de INT-mail zonder set.
- **De structuur is opgeblazen.** Omdat Klaviyo geen takken laat samenkomen, staat de code-router vier keer in de flow. Dat zijn 12 mails om te onderhouden, met 12 keer dezelfde tekst. Bij elke wijziging is de kans groot dat er één vergeten wordt. Nu al heeft c4-us geen iconenblok en c4-us-nocode wel.

## Wat je verliest zonder split

Weinig. Een rapport per land in de flowstatistiek haal je ook uit Shopify of uit Klaviyo-rapporten op profielland. De T02-test (wel of geen code) loopt 50/50 willekeurig, dus US en INT verdelen zich vanzelf eerlijk over beide armen. Per land analyseren kan achteraf nog steeds.

## Voorgestelde structuur

Dag 5: **cooldown-split** (code gehad in de laatste 30 dagen?) en dan de **T02-split** 50/50. Daarna `c4` (met code) of `c4-nocode`, en `c4-nocode` voor de cooldown-tak. In de template staat één US-voorwaarde voor de set-kaart, voor de "duties paid"-regels en voor het iconenblok.

Nog niet gebouwd. Wat er moet gebeuren:

- **Templates:** c4-us en c4-int samenvoegen tot `c4.html`, en de twee nocode-versies tot `c4-nocode.html`. De hero kiest met een `{% if %}` tussen de US- en de INT-afbeelding, of krijgt één neutrale afbeelding. UTM wordt `c4` en `c4nocode`. Dezelfde vraag speelt bij W4-US en W4-INT in de welkomstflow.
- **Script `build_flow_checkout.py`:** `land`, `has_country`, `locale` en drie van de vier routers weghalen. De manifest-ID's aanpassen.
- **Plan `v4-flow-system.md`:** de regels 5K, 6K, 5A-6A, het T02-stratum en de mailtabel bijwerken.

---

## Technische bijlage

**Verschil tussen de templates** (`diff`, `klaviyo/templates/v3/checkout/`)

- c4-us en c4-int verschillen in: de hero-afbeelding en de alt-tekst (INT: "duties paid"), de subregels onder de knoppen (INT: "Duties paid"), en de offer-note (INT: plus "Shipping is free and duties are paid..."). Verder heeft US een set-kaart (`pill="US ONLY"`, $599/$1,186, alleen bij kookgerei) en INT `icons-int`. c4-us heeft **geen** iconenblok.
- c4-us-nocode en c4-int-nocode hebben hetzelfde patroon: een cart-regel en een alinea met "duties paid", de set-kaart tegenover een extra knop, en `icons` tegenover `icons-int`.
- `icons-int` gebruikt hetzelfde bestand als `icons`, alleen icoon 4 is anders: no-duties in plaats van pfas-tested (`scripts/build_template.py` r. 20-35).

**Bronnen voor de aanname**

- `content/products/titanium-hammered-cookware-set/product.md`: "Alleen United States. Buiten de US nooit noemen".
- Site: `/products/titanium-hammered-cookware-set.js` geeft 200, maar `/en-au/`, `/en-ca/`, `/en-gb/`, `/en-sg/` en `/en-ae/` geven 404.
- Shopify `markets` (alleen gelezen): USA (US), Australia, Canada (`ADD_DUTIES_AT_CHECKOUT`), EURO, Germany, Netherlands, UK, NZ, Norway, Singapore, MIDDLE EAST (USD), RoW (USD: TH, TW, MX, JP, enz.), "Shipping Costs To High" (USD).
- "Duties paid" en "set alleen US": bevestigd door de eigenaar op 7 oktober 2026. Kanttekening voor later: de verzendpolicy op de site zegt "In most cases, customers are not required to pay customs duties", en de Canada-markt in Shopify staat op `ADD_DUTIES_AT_CHECKOUT`. Mogelijk moet de site-tekst gelijkgetrokken worden met wat we in de mails beloven.
- PLAYBOOK r. 118 en 136 laten "No import duties" toe voor INT. `gift-free-shipping/claims.md` doet dat ook.

**Data: Checkout Started (RfMvni)**

Steekproef: 3.600 events, 18 juli tot 7 oktober 2026, 9 vensters van 10 dagen met per venster 400 events. Het ging om 3.055 profielen, opgehaald met `include=profile`.

| Signaal | Uitkomst |
|---|---|
| Profielland "United States" | 2.001 (55,6%) |
| Profielland "US" (ISO-code; de split stuurt die naar INT) | 112 (3,1%), plus "AU" 19 en "CA" 16 |
| Profielland ander land | 982 (27,3%) |
| Geen profielland | 505 (14,0%), waarvan 478 met en-US |
| Routering in de huidige flow | US 2.479 (68,9%), INT 1.121 (31,1%) |
| `Customer Locale` en-US | 77,4%. Geen waardeloze regel: de locale volgt de Shopify-markt (en-AU, en-CA, en-SG enz.) |
| `presentment_currency` USD | 76,1%. AUD 222, CAD 143, SGD 111, EUR 109, GBP 82 |
| Locale en valuta wijzen naar hetzelfde | 97,2% |
| `shipping_address` in het event | maar 123 van de 3.600 (3,4%). Waar het er is, komt het in 100% overeen met valuta en profielland |
| USD, terwijl het profiel een ander land dan de US heeft | ongeveer 157 (4,4%): Thailand 37, Australië 37, Canada 18, Taiwan 10 (RoW- en Midden-Oosten-markten rekenen in USD) |

De aantekening in `research/tailoring/00-data.md` r. 97 klopt niet meer. Die zegt "INT-checkouts staan ook op USD", maar 24% van de checkouts is in een andere valuta.

**Betrouwbaarste signaal in de template**

1. Profielland als dat gezet is, met "United States" en "US" allebei als US.
2. Is er geen profielland, dan `event.extra.presentment_currency == 'USD'`.

Het valutasignaal wordt al gebruikt in C1 tot en met C3 (`USCOND['checkout']`). Alleen het valutasignaal zou ongeveer 4% (RoW-landen in USD) de US-versie geven. De syntaxis voor het profielland in een template (`person.location.country` of `person|lookup:'$country'`) is in dit account nog nergens gebruikt. Controleer die eerst met een preview op een echt profiel. Werkt die niet, dan is valuta alleen een acceptabele terugval.

**Telling van de flow**

| | Nu | Voorstel |
|---|---|---|
| Landsplits | 3 | 0 |
| Router-splits | 4 × 2 = 8 | 2 |
| Splits totaal | 11 | 2 |
| C4-mailknopen | 12 | 3 |
| C4-templates | 4 | 2 |

De cijfers komen uit `scripts/build_flow_checkout.py` r. 192-210.
