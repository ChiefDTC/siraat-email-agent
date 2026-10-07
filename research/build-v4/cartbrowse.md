# Bouwronde v4 · cart en browse (agent cartbrowse, 7 oktober 2026)

Mappen: `klaviyo/templates/v3/cart/` en `klaviyo/templates/v3/browse/`. Hero-registers bijgewerkt. Niets in Klaviyo, Shopify of Figma, niets gecommit.

## Per mail

| Mail | Onderwerp A | Hero-kop | Mobiel (px, incl. footer) | Nieuwe onderdelen |
| --- | --- | --- | --- | --- |
| k1 | One pass with a damp cloth. | One wipe. / No scrubbing. | 3.793 | closer look Pan Pro (vervangt features), ankerprijs $439 bij Standard |
| k1-acc | Picked it out? It's still here. | Picked it out? / It's still here. | 3.181 | geen (feitregels per accessoire behouden) |
| k2-new | The pan you keep replacing is the expensive one | 15 pans, / or one. | 3.978 | de som (15 tegen 1, dollars alleen bij USD), vergelijkingstabel titanium vs coated, case Scott Y. |
| k2-returning | Adding to your Siraat kitchen? | You know / this pan. | 3.552 | 2 productkaarten (deksel, Deep Pan Pro; prijzen alleen bij USD) |
| k3 | Your own 10% code, for 48 hours | The last email / about your cart. | 3.789 | "Two promises" (volledige risk reversal), offerblok met echte deadline |
| k3-nocode (nieuw) | What if it's not for you? | The last email / about your cart. | 3.469 | idem zonder code; codebalk "$70 IN GIFTS" |
| b1 | T05a A: Lab-tested: nothing on this pan to scratch off · B: 100,000+ happy customers cook on this pan | Nothing on it / to scratch off. | 3.771 | vergelijkingstabel (vervangt tekst-tabel), regel rapport 25895 met link, ankerprijs |
| b1-acc | Looked twice? Here's the detail. | Looked twice? / Here's the detail. | 3.205 | geen |
| b2-clicked | Your own 10%, for the next 48 hours | Your own 10%, / for 48 hours. | 3.405 (deksel-variant 3.3k) | value stack (Value $509 / Your price $120.60 bij Standard) in plaats van gifts-blok bij kookgerei |
| b2-clicked-nocode (nieuw) | "I ordered one pan to try it out" | "I ordered one pan / to try it out." | 3.025 | value stack zonder code |
| b2-notclicked | Week one, in their words | In their / words. | 4.036 | vier verhalen (James en Sunny C. vervangen Avril en Sonya D.), closer look Pan Pro |

Boven de vouw (390 px): codebalk, header, hero 4:3 met aanbodbalk, productkaart, knop en friction reducer eindigen rond 740 tot 790 px.

## Wat veranderde
- Copy volgens `research/copy/04-rewrites.md` (onderwerpen, preview, hero, opener, knop, friction reducer, reviews). Onder elke primaire knop een friction reducer. Benjamin tekent elke mail. "Just reply. A real person reads every email." staat in geen enkele cart- of browsemail meer.
- Hero's opnieuw gemaakt met de nieuwe kop; AI-flash voor k2-new, k3, b2-clicked, b2-notclicked (02-voorstel), de rest houdt de bronfoto. Nocode-varianten gebruiken hetzelfde beeld als hun A-variant (zelfde plek in de flow).
- Ankerprijs `$439 $134` en "With HI10 it's $120.60" alleen als het product Pan Pro Standard is, prijs $134, aantal 1 en valuta USD (cart) of prijs begint met "$134" (browse). Anders de oude zin.
- `{% if %}`-logica behouden: categorie (kookwoorden, set/pan, accessoire-feiten), USD-prijs (cart), `'$' in event.Price` (browse, QA A18). Nieuw: K3 en b2-clicked tonen de 75-jaar-garantie (tekst en icoon) alleen bij kookgerei (open punt 3.27, veilige keuze).
- UTM: `utm_source=klaviyo&utm_medium=email&utm_campaign=v4-cart|v4-browse&utm_content=<mailid>-<blok>`. Werkwijze: bij `/discount/CODE?redirect=` staan de UTM's url-gecodeerd achter het pad binnen `redirect` (`/cart%3Futm_source%3D...%26...`). K3/b2c: `utm_term=t02-a`, nocode: `t02-b` (zelfde mail-ID). Nocode-links gaan zonder discount direct naar `/cart` of het productpad.
- Previews: eerst officieel `build_template.py`, daarna de `-preview.html` overschreven met een Django-render (Klaviyo-syntax) op een echt voorbeeld-event uit `research/tailoring/test/samples` (atc_pan, atc_apron, vp_pan, vp_apron; b2-clicked ook vp_lid als `-preview-deksel`). Zo staan er geen ruwe `{% if %}` in de preview. Generator en controlescripts staan in de scratch-map van deze sessie (niet in de repo).
- Nieuwe beelden: `cart/assets/card-lid.jpg` (uitsnede van een kopie van de lid-packshot) en `card-deeppan.jpg`, beide via `place_sticker.py --white` zonder sticker.

## Controles
- `research/tailoring/test/run_tests.sh`: alle 15 cart/browse-regels ok.
- Eigen takkencheck (alle mails x 6 tot 8 voorbeeld-events): geen $-prijs bij EUR, geen pan-tekst of garantiezin bij accessoires in k1-acc, k3, k3-nocode, b1-acc, b2-clicked(-nocode). b1 en b2-notclicked krijgen alleen kookgerei (routing).
- Reviews: elk citaat letterlijk in `content/reviews/reviews.csv` (Trustpilot), 5 sterren, max 120 tekens, paarverschil max 30; alle uit reviews-positive-usable.csv of 04-rewrites.
- Geen ontbrekende lokale beelden, geen `[[`, `{{BLOCK`, em dash of verboden woorden; onderwerpen 23 tot 47 tekens, previews 55 tot 75.

## Open punten
1. **Lengte**: k1, k2-new, k3, b1 en b2-notclicked zitten op 3.770 tot 4.040 px incl. footer (~550 px). De nieuwe onderdelen uit het plan (vergelijkingstabel, closer look) kosten 550 tot 650 px; ik heb opener, notes en een knop geschrapt maar niet de vergelijking of de reviews. b2-notclicked is kandidaat voor T08 (lengte), fase 2.
2. **e-book-naam**: het gifts-blok (partial) noemt "Plastic-Free Home e-book", DECISIONS noemt het e-book "The Green Clean E-Guide" (beeld toont "The Green Clean Guide"). Mijn value stack volgt het blok. Gelijktrekken in `partials/blocks/gifts.html`.
3. **Blok productcard** kent alleen `{{SHARED}}`-beelden; eigen kaarten (deksel, Deep Pan) heb ik uitgevouwen met `{{IMG}}`. Voorstel: parameter `src` in het blok.
4. **Vergelijkingsrijen**: rij 1 "Pure titanium surface" uit comparisons.md botst met de verboden frase; gebruikt als "Titanium cooking surface". Rij 4 (PTFE is a PFAS) niet gebruikt; in plaats daarvan de alternatieve rij, ingekort tot "Tested by Light Labs / Testing varies by brand".
5. **Viewed Product URL met `?variant=`**: dan breekt `%3Futm_...` achter het pad (moet `%26` zijn). Testen met een echt event in de Klaviyo-preview.
6. **Prijsformaat Viewed Product**: ankerprijs vergelijkt de eerste 4 tekens met "$134"; als Shopify AUD/CAD ook als "$134" toont, ziet een niet-US-lezer de USD-anker. Met een echt INT-event controleren.
7. **Value stack en gifts-blok**: in b2-clicked(-nocode) vervangt de stack het gifts-blok bij kookgerei (dezelfde vier gifts met waarde, filter als "chance to win", niet opgeteld). Akkoord vragen.
8. **"MOST ADDED"-pill op het deksel** (k2-returning) steunt op cross-sell.md (deksel is de vaakst meegekochte combinatie in 750 orders).
9. Nog uploaden naar Klaviyo en `assets/klaviyo-urls.txt` vullen (nieuwe hero's, card-lid, card-deeppan, cart-fallback); daarna pas ontstaat `.klaviyo.html`.
10. Garantie op accessoires (3.27) en of Benjamin replies leest (04) blijven [VRAAG FLORIS].
