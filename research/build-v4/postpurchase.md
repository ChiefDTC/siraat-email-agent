# Bouwronde v4 · post-purchase (agent postpurchase, 7 oktober 2026)

Map: `klaviyo/templates/v3/post-purchase/`. 14 bron-templates: p1-first, p1-repeat, p2, p2-safe (nieuw), p3-pan, p3-set, p3-accessory, p3-next, p3-apron en vijf `-nocode` (nieuw). Doel (research/deep): de eerste week laten slagen. P1 en P2 zijn onboarding met de chef-methode (eerst heet, dan olie, dan ei), zonder codebalk en zonder verkoop. P3 is cross-sell met bedankcode; deksel in dezelfde maat als de pan staat centraal in P3-pan.

De bronnen zijn gegenereerd met een script in de scratch-map (niet in de repo). Verdere wijzigingen: gewoon in de HTML.

## Per mail

| Mail | Onderwerp A | Hero-kop | Mobiel (px, echte tak) | Nieuwe onderdelen |
| --- | --- | --- | --- | --- |
| p1-first | Good call. Here's what's coming. | Good call. / Here's what's next. | 3.820 (pan), 3.206 (schort) | geen (CL bewust niet: lengte; chef-noot en tijdlijn doen het werk) |
| p1-repeat | Good to see you again | Good to see / you again. | 2.812 | geen |
| p2 | If you can do an egg, you can do anything | If you can / do an egg, | 4.015 (handleiding, mag lang) | stap-frames uit de chef-video (2 stills + lichte GIF) |
| p2-safe | When your pan arrives: the first egg | Your first egg, / step by step. | 3.497 | zelfde stap-frames |
| p3-pan (+nocode) | Which lid fits your pan? | The lid / that fits. | 3.524 / 3.227 | PK deksel (met maat per pan), PK snijplank |
| p3-set (+nocode) | The pan your set is missing | The pan your / set is missing. | 3.490 / 3.227 | PK crêpepan, PK wok |
| p3-accessory (+nocode) | Now meet the pan | Now meet / the pan. | 3.866 / 3.603 (INT-voorbeeld, US +1 regel) | CL Pan Pro, PK Pan Pro (BEST SELLER-kaart) |
| p3-next (+nocode) | What goes next to your pan | What goes / next to your pan | 3.652 / 3.319 | PK-stijl hoofdkaart (dynamisch) |
| p3-apron (+nocode) | An apron deserves a pan | An apron / deserves a pan. | 3.434 / 3.155 | PK Pan Pro (BEST SELLER-kaart) |

Previews per echte tak (Django-render op voorbeeld-events uit research/tailoring/test/samples): `<mail>-<tak>-preview.html` en `previews/<mail>-<tak>-mobile.png`. De gewone `<mail>-preview.html` toont alle `{% if %}`-takken tegelijk.

## Wat veranderde

- **P1-first**: opener bevestigt hun keuze (titanium cooking surface, no coatings, 75 jaar); chef-noot staat direct onder de order en noemt de eerlijke beperking ("Skip the heat, and it sticks"); afsluiting vraagt om te replyen vóór ze opgeven als iets plakt (retourpreventie, alleen bij kookgerei). Reviews Marilyn B. en Sandi R. Tijdlijnstap "When it arrives" in plaats van "the day after delivery" (P2 gaat maar naar 36%). Iconenrij weg (geen verkoopmail, lengte).
- **P1-repeat**: knop "Read the care guide" (e-book hebben ze al; e-book-link in de gifts-noot). Reviews Tammy en Don J.
- **P2**: lid-upsell eruit (geen verkoop). "high heat" uit de heat-tint-zin. Plakken-blok met "Still sticking? Reply..." (coaching vóór retour). Stappen 2 en 3 krijgen stills uit de GIF's, stap 4 een GIF met halve frames (385 kB in plaats van 780; QA A7: was 1,7 MB aan GIF's). UGC-oproep zonder belofte van korting (OVERZICHT 36 open).
- **P2-safe (nieuw)**: zelfde gids, opener "either on your stove already or on its way to you", afsluiting voor wie nog niets heeft ("Reply with your order number"). Geen levertijden.
- **P3 (alle)**: P3 gaat nu op dag 20, dus geen "two weeks in" meer. Codebalk, hero met aanbodbalk, productkaart + knop boven de vouw, compacte code-regel met einddatum, reden en wat-daarna ("Made for you, so it has an end date. After that, the regular price applies."), gifts, reviews, 3 knoppen, iconen, Benjamin. Het grote espresso-aanbodblok is vervangen door een compacte versie (zelfde kleur, code, deadline) om onder ~3.500 px te blijven. Prijzen alleen bij verzendland US (`shipping_address.country_code == 'US'`), ook in P3-pan, P3-set en P3-accessory (tailoring J1 opgelost).
- **P3-pan**: maat per pan in de kaart (`Your 11″ Pan Pro takes the 28 cm lid.` voor Mini/Small/Standard/Large en crêpe), altijd met "Pick the same diameter as your pan". Reviews David A. (verkeerd deksel, snel opgelost) en Robert H. (pans and lids); Nina G. ("handle stays cool") eruit.
- **-nocode**: zelfde mail zonder code: giftbalk "FREE SHIPPING · 4 GIFTS WITH EVERY ORDER" op de plek van de codebalk, eigen hero met die aanbodbalk, gewone prijzen, gifts-blok op de plek van de code, `utm_term=t02-b`.

## Keuzes

- **UTM**: `utm_campaign=v4-postpurchase` (brief zegt `v4-<flow>`; v4-flow-system 1.5 noemt nog `v3-postpurchase`: gelijktrekken). Mail-ID's `p1first`, `p1rep`, `p2`, `p2safe`, `p3pan`, `p3set`, `p3acc`, `p3next`, `p3apron`. Bij `/discount/<code>?redirect=` staan de UTM's URL-gecodeerd achter het pad binnen `redirect` (`%3F`, `%3D`, `%26`). P3 met code `utm_term=t02-a`, nocode `t02-b` (ook de cooldown-tak krijgt t02-b; filter in de analyse op T02-split, niet alleen op de term).
- **Productkaarten** zijn inline gebouwd in de opmaak van `blocks/productcard.html`, omdat dat blok alleen beelden uit `partials/shared` kan tonen; eigen witte kaartbeelden in `assets/card-{lid,board,crepe,wok,panpro}.jpg` (crème naar wit, zelfde formule als place_sticker --white). Pan Pro gebruikt de gedeelde `card-panpro-bestseller.jpg` (geen SAVE-sticker: INT-kopers krijgen dezelfde mail).
- Reviews alleen uit reviews-positive-usable.csv of 04-rewrites, letterlijk, max 120 tekens, paarverschil max 30 (eigen controle gedraaid; check_reviews.py werkt alleen op 04-rewrites).

## Open punten

1. **Uploaden**: nieuwe beelden (14 hero's, card-*.jpg, water-test-still.jpg, oil-shimmer-still.jpg, egg-slide-lite.gif) staan nog niet in de Klaviyo-bibliotheek; `assets/klaviyo-urls.txt` aanvullen, dan maakt build_template ook de `.klaviyo.html`.
2. **Bug/beperking blok**: `{{BLOCK:productcard}}` zet altijd `{{SHARED}}/` voor het beeld en heeft geen US-only prijs. Voorstel: parameter `src` (volledig pad) en `us="1"`.
3. **build_all.sh** pakt elk `.html` dat niet op `-preview.html` eindigt als bron; oude variant-previews (`p1-first-preview-schort.html`) werden daardoor als bron gebouwd. Verwijderd en vervangen door `<mail>-<tak>-preview.html`.
4. **Header op mobiel**: in de header-partial raakt "SIRAAT" bijna "COOKWARE" (390 px). Partial, niet aangepast.
5. **Gifts-blok**: het e-book-beeld toont "The Green Clean Guide", het label zegt "Plastic-Free Home e-book" (en de order-regel ook). Eén naam kiezen (partial).
6. **E-book-link** blijft `/products/e` (DECISIONS); OVERZICHT 33 vraagt nog of dat de betaalpagina van $50 is.
7. **"Piece most often ordered with the pan"** (P3-pan) steunt op de orderanalyse van de coördinator (pan + deksel sterkste combinatie) en research/deep (deksel in 14% van de orders); bevestigen als feit.
8. **P3-accessory** is 3.866 px (CL Pan Pro is de uitleg). Als het korter moet: CL eruit, de intro draagt dan de uitleg.
9. **Deep Pan 24 cm** heeft geen deksel (geaccepteerd risico, v4 2.5); P3-pan zegt "Pick the same diameter as your pan: 20, 26, 28 or 30 cm".
10. **v4 1.4 nocode-definitie**: "geen code" gekozen (niet HI10), zoals de router in v4 beschrijft.
