# Bouwronde v4 · site, sunset, ugc (agent "nieuw")

Datum 7 oktober 2026. Mappen: `klaviyo/templates/v3/site/` (a1, a2), `sunset/` (s1, s2), `ugc/` (u1). Volgens v4-flow-system.md hebben deze flows geen `-nocode`-varianten (site: HI10 publiek; sunset: geen aanbod; ugc: code via Gorgias na een foto). Niets in Klaviyo, Shopify of Figma; niet gecommit.

## Werkwijze UTM (gekozen en gedocumenteerd)

- Kortingslinks: UTM's **binnen** `redirect`, gecodeerd (`?` = `%3F`, `&` = `%26`, `=` = `%3D`), zoals `research/testing/04-utm.md` 5.2b:
  `https://siraatskitchen.com/discount/HI10?redirect=/collections/pans%3Futm_source%3Dklaviyo%26utm_medium%3Demail%26utm_campaign%3Dv4-site%26utm_content%3Da1-cta1`
- Gewone links (sunset, ugc): `?utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign=v4-<flow>&amp;utm_content=<mail>-<blok>`.
- `utm_campaign` = `v4-site`, `v4-sunset`, `v4-ugc` zoals de brief zegt. **Let op**: v4-flow-system.md 1.1 zegt dat de slugs `v3-*` blijven voor de rapportage. Eén van beide moet winnen (zie open punten).
- Blokken: `hero`, `cta1..3`, `size-mini|small|standard|large` (a1), `card-pan`, `card-set` (a2), `guide` (u1). Header en footer (partials) hebben geen UTM; buiten mijn mandaat.
- Mailto-links (u1) hebben geen UTM.

## Per mail

| Mail | Onderwerp A / B | Preview | Hero (label / kop / subregel) | Mobiel | Nieuwe onderdelen |
| --- | --- | --- | --- | --- | --- |
| a1 | Not sure which pan? Start here. / Four eggs or five? | Four sizes, one titanium cooking surface. Here is how to pick yours in 30 seconds. | WHICH SIZE? / Four eggs\|or five? / How to pick your pan in 30 seconds (aanbodbalk HI10 + $70) | 3.550 px | Maatkiezer "Count your eggs" (4 maten, eieren als maat, HI10-prijs per maat, pill BEST SELLER), uitlegregel "Every size is the same pan, scaled". Closerlook getest en weer weggehaald (mail werd 4.300 px). |
| a2 | Where 100,000+ people started / One pan, or three? | Most kitchens start with the 11-inch pan. Some go straight to three. Here's how to choose. | WHERE MOST START / One pan,\|or three? / What 100,000+ kitchens picked first (aanbodbalk) | 3.706 px | 2x productcard (Pan Pro bestseller-sticker, 6-delige set via BDAY-listing $349), compare A (rij 4 vervangen door het alternatief "Tested by Light Labs / Testing varies by brand"; rij 1 "Titanium cooking surface") |
| s1 | Should we keep writing to you? / Still want our emails? One tap. | One tap keeps you on the list. No tap, and we'll stop writing in about a week. | QUICK QUESTION / Still want\|our emails? / One tap keeps you on the list (geen aanbodbalk) | 1.817 px | Geen. Features-blok met gifts en sales weggehaald (geen verkoopdruk); één knop, keuzekader minder/uitschrijven |
| s2 | Last email from me (unless you tap) / Should I stop writing? | One tap and you stay. Otherwise this is goodbye, and that's okay. | geen (tekstmail Benjamin) | 1.500 px | Geen. P.S. met HI10 en "free 30-day returns" weggehaald; Opened Email-filter uit de topcomment (besluit 3.16) |
| u1 | Show us your first egg? / One photo, 15% off your next order | Reply with a photo of your first egg, or anything you cooked. We'll send you 15% off. | YOUR FIRST WEEK / Show us\|your first egg / How did it go? (aanbodbalk SEND A PHOTO · GET 15% OFF YOUR NEXT ORDER) | 2.964 px | Toestemmingskader "Your photo, your call" (website, e-mails, social, alleen voornaam; "private" = niet delen, code blijft; later intrekken via support). Code-voorwaarden volgens v4: 15%, 1 gebruik, 60 dagen, één per klant. "Within 2 business days" eruit (responstijd-belofte). |

Vijf onderwerpen per mail (type tussen haken), A/B gekozen per mail:
- a1: The one question that picks your pan (C+B) · 8, 10, 11 or 12 inches? (SPEC) · Not sure which pan? Start here. (Q, A) · "Perfect over easy eggs for the first time" (STORY, R411) · Your size, plus 10% and $70 in gifts (OFFER). B = Four eggs or five? (nieuwsgierigheid + specifiek).
- a2: One pan, or three? (C+B, B) · Where 100,000+ people started (SPEC/SP, A) · Which one did 100,000+ people pick? (Q) · "I am on my 4th pan from Siraat" (STORY, R138) · 10% off where most people start (OFFER).
- s1: One tap keeps you on our list (C+B) · Still want our emails? One tap. (SPEC, B) · Should we keep writing to you? (Q, A) · (STORY n.v.t.) · (OFFER bewust niet).
- s2: Last email from me (unless you tap) (A) · Should I stop writing? (Q, B) · Before I take you off the list (C+B).
- u1: Show us your first egg? (Q, A) · One photo, 15% off your next order (OFFER, B) · "Then fried an egg which didn't stick" (STORY, R069) · Your first egg, in one photo (C+B) · 15% for a photo from your kitchen (SPEC).
Site heeft volgens v4 geen tests in de eerste 4 weken: alleen A versturen.

Reviews (letterlijk uit `content/reviews/reviews-positive-usable.csv`, 5 sterren, max 120 tekens, verschil max 30, met eigen script gecontroleerd): a1 R411 Deb + R465 Robert E.; a2 R017 Marilyn B. + R138 Tammy; u1 R069 Aggie M. + R518 Graham C.

## Controles

- Build + render per mail, 390 px mobiel bekeken in stukken van 1.400 px. Geen ontbrekende beelden, geen `[[`, `{{BLOCK`, em dash of verboden woorden (eigen grep), onderwerp max 50, preview 40 tot 90, preheader gelijk aan PREVIEW.
- Django-render (research/tailoring/test/render.py, met kopie van de huidige build_template-uitvouw) op voorbeeld-events: alle vijf renderen zonder resten. `{% unsubscribe_url %}` (s1, s2) kent de testharnas niet; gestubd, in Klaviyo een geldige tag.
- `run_tests.sh` faalt, maar niet op mijn mails (die staan er niet in): `research/tailoring/test/expand.py` is een oude kopie van build_template zonder compare/productcard-logica, dus c1 en c3-acc (nu met nieuwe blokken) breken in de expand-stap. Django moest in mijn scratch geïnstalleerd worden (pylib ontbreekt).
- Hero's: alle drie opnieuw gemaakt met make_hero.py en bekeken; leesbaar op 390 px. a1-subregel staat over de omelet, licht maar leesbaar.

## Bugs in blokken/scripts (gemeld, niet aangepast)

1. `partials/blocks/gifts.html`: label "Plastic-Free Home e-book" terwijl het beeld en DECISIONS "The Green Clean E-Guide" zeggen.
2. `blocks/productcard.html` en `closerlook.html` zetten altijd `{{SHARED}}/` voor het beeld: een eigen kaart in de assets-map van een flow kan niet via het blok.
3. `research/tailoring/test/expand.py` loopt achter op build_template.py (zie boven); `run_tests.sh` faalt daardoor voor c1 en c3-acc.
4. build_template.py schrijft `.klaviyo.html` alleen als alle beelden in klaviyo-urls.txt staan; hero's en productfoto's van site/sunset/ugc staan er nog niet in (alleen s2 heeft een .klaviyo.html).

## Open punten

1. `utm_campaign`: brief zegt `v4-<flow>`, v4-flow-system 1.1 zegt `v3-*` blijven. Ik volgde de brief. Floris of de hoofdagent kiest; zoeken-en-vervangen is één regel per mail.
2. Site-flow kent geen US/INT-split: prijzen in dollars en de US-iconen ("Free shipping") gaan ook naar INT-bezoekers. Overweeg een INT-tak of prijsloze variant.
3. 6-delige set: $349 alleen op de BDAY-listing (unlisted); hoofdlisting staat op backorder (-325). Hoe lang blijft BDAY live?
4. a1 en a2: "most of our 100,000+ customers started with one pan" steunt op verkoopcijfers (Pan Pro-maten ver boven de set in 90 dagen), niet op een cohortanalyse. Zacht genoeg? Anders "most people start with".
5. a1: Mini en Large tonen dezelfde packshot (p-panpro.jpg); er zijn alleen bovenaanzichten met eieren voor Small en Standard.
6. a2 mobiel 3.706 px, iets boven ~3.500 (footer is ~650 px). Verder inkorten kan door de set-kaart of de vergelijking te schrappen; ik hield beide.
7. u1: toestemmingstekst juridisch laten nalezen (VS). Gorgias moet "private" kunnen taggen en verwijderverzoeken afhandelen; UGC15-pool en macro bestaan nog niet (v4 4.x). OVERZICHT-FLORIS vraag 36 (akkoord op 15% voor een foto) staat nog open.
8. Sign-offs zeggen "Reply ... we'll tell you"; reply-to support@ (Gorgias) moet bevestigd zijn (v4 bouwlijst punt 4).
9. Masters met link-macro's staan in mijn scratch (`expand.py`); de HTML in de repo is nu de bron.
