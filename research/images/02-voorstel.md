# Voorstel nieuwe hero-beelden (7 oktober 2026)

Basis: `01-hero-audit.md`. Nieuwe beelden in `content/media/ai-flash/` (register `index.csv`, prompts in `README.md`). Per mail een testhero met `scripts/make_hero.py` en de huidige kop, subregel, label en aanbodbalk (overgenomen uit de huidige hero; de copy-ronde kan die nog veranderen, dan alleen make_hero opnieuw draaien). Niets vervangen in templates, assets of registers.

Per mail staan in `research/images/test-heroes/`:
- `<mail>-new.jpg`: testhero 1200 px met het nieuwe beeld
- `<mail>-voor-na.jpg`: huidige hero links, nieuwe rechts

## Vervangingstabel

| Mail | Huidige hero (voor) | Nieuw basisbeeld | Testhero (na) | Leesbaarheid | Opmerking |
| --- | --- | --- | --- | --- | --- |
| w0 | klaviyo/templates/v3/welcome/assets/w0-hero.jpg | content/media/ai-flash/egg-crack-1x1-01.jpg | research/images/test-heroes/w0-new.jpg | Goed | Ei en pan onder de tekst, past bij "first egg" |
| w4-us | klaviyo/templates/v3/welcome/assets/w4-us-hero.jpg | content/media/ai-flash/pasta-lift-1x1-01.jpg | research/images/test-heroes/w4-us-new.jpg | Redelijk | Pasta-slierten lopen door de subregel; kop goed. Lost de bijna-dubbel met w1 op |
| w4-int | klaviyo/templates/v3/welcome/assets/w4-int-hero.jpg | content/media/ai-flash/two-sizes-1x1-01.jpg | research/images/test-heroes/w4-int-new.jpg | Zeer goed | Twee maten pan, past bij "the right size for you" |
| p1-first | klaviyo/templates/v3/post-purchase/assets/p1-first-hero.jpg | content/media/ai-flash/pan-trophy-1x1-01.jpg | research/images/test-heroes/p1-first-new.jpg | Goed | Pan als trofee, past bij "Good call" |
| p1-repeat | klaviyo/templates/v3/post-purchase/assets/p1-repeat-hero.jpg | content/media/ai-flash/friends-greeting-1x1-01.jpg | research/images/test-heroes/p1-repeat-new.jpg | Goed | Begroeting, past bij "Good to see you again" |
| p2 | klaviyo/templates/v3/post-purchase/assets/p2-hero.jpg | content/media/ai-flash/egg-plate-1x1-01.jpg | research/images/test-heroes/p2-new.jpg | Goed | Ei glijdt op het bord; zachtste groep opgelost |
| p3-pan | klaviyo/templates/v3/post-purchase/assets/p3-pan-hero.jpg | content/media/ai-flash/lid-steam-1x1-01.jpg | research/images/test-heroes/p3-pan-new.jpg | Goed | Glad RVS-deksel met knop, zoals het echte deksel |
| p3-accessory | klaviyo/templates/v3/post-purchase/assets/p3-accessory-hero.jpg | content/media/ai-flash/pan-reflection-1x1-01.jpg | research/images/test-heroes/p3-accessory-new.jpg | Goed | Spiegeling in de pan, speels |
| p3-set | klaviyo/templates/v3/post-purchase/assets/p3-set-hero.jpg | content/media/ai-flash/crepe-flip-1x1-01.jpg | research/images/test-heroes/p3-set-new.jpg | Redelijk | Pan staat deels achter de subregel. Pan is geen platte crêpepan |
| r1-set | klaviyo/templates/v3/winback/assets/r1-set-hero.jpg | content/media/ai-flash/full-stove-1x1-01.jpg | research/images/test-heroes/r1-set-new.jpg | Redelijk tot goed | Pannen onder de subregel; volle set past bij set-eigenaren |
| b2-clicked | klaviyo/templates/v3/browse/assets/b2-clicked-hero.jpg | content/media/ai-flash/egg-slide-4x3-01.jpg | research/images/test-heroes/b2-clicked-new.jpg | Goed | Ei glijdt los, zelfde verhaal als de oude still, nu scherp |
| b2-notclicked | klaviyo/templates/v3/browse/assets/b2-notclicked-hero.jpg | content/media/ai-flash/sauce-taste-4x3-01.jpg | research/images/test-heroes/b2-notclicked-new.jpg | Goed | Proeven van de lepel |
| k2-new | klaviyo/templates/v3/cart/assets/k2-new-hero.jpg | content/media/ai-flash/pan-microphone-4x3-01.jpg | research/images/test-heroes/k2-new-new.jpg | Goed | Geen gegraveerd handvat meer achter de kop |
| k3 | klaviyo/templates/v3/cart/assets/k3-hero.jpg | content/media/ai-flash/steak-sear-4x3-01.jpg | research/images/test-heroes/k3-new.jpg | Goed | Gezicht rechtsboven raakt het label net; pan valt deels onder de aanbodbalk |
| c2 | klaviyo/templates/v3/checkout/assets/c2-hero.jpg | content/media/ai-flash/olive-oil-4x3-01.jpg | research/images/test-heroes/c2-new.jpg | Goed | Haalt de dubbele hamerslag-close-up met w3 weg |
| c3-p | klaviyo/templates/v3/checkout/assets/c3p-hero.jpg | content/media/ai-flash/three-pans-4x3-01.jpg | research/images/test-heroes/c3-p-new.jpg | Zeer goed | Drie pannen met deksels, letterlijk "Make it three"; c3-s houdt P02 |

## Beoordeling leesbaarheid

- Alle 16 testhero's: kop in TT Ramillas en label goed leesbaar op desktop en op 390 px mobiel; het donkere midden van de flitsval doet wat het moet doen.
- Scherpte: bronbeelden zijn 2048 of 2336 px breed en worden verkleind naar 1200; geen opschaling meer (oud: tot 2,3x).
- Zwakste drie (subregel over een licht object): w4-us, p3-set, r1-set. Bruikbaar; bij een volgende ronde kan de subregel licht omhoog of kan het object lager in een nieuwe generatie.
- Let op casting: elke mail heeft een eigen beeld en de hoofdpersonen binnen post-purchase verschillen (p2, p3-pan en p3-accessory zijn daarvoor opnieuw gegenereerd). Het model hergebruikt wel graag dezelfde typen: de bebaarde man uit k3 lijkt op die in p1-repeat en r1-set, de brunette uit p1-first op die in w4-us en k2-new, en bijfiguren aan de rand lijken soms op elkaar. Acceptabel, wel bewust houden bij nieuwe generaties (casting expliciet variëren).

## Wat blijft (geen nieuw beeld voorgesteld)

b1, k1, k2-returning, c1, c3-s, c4-us, c4-int, w1-a, w1-b, w3, w5, r1-pan, r2, r2-vip: scherpe echte shoot- of productfoto's. Echte foto blijft voorrang houden.

## Na akkoord (door Siraat of in een volgende sessie)

1. Copy-ronde afwachten, dan per mail `python3 -I scripts/make_hero.py content/media/ai-flash/<beeld>.jpg klaviyo/templates/v3/<flow>/assets/<mail>-hero.jpg "<kop>" "<subregel>" "<LABEL>" --offer="..." [--ratio=4:3]`.
2. Hero-register `content/media/hero-register/<flow>.csv` bijwerken (bronfoto = ai-flash-pad), status in `content/media/ai-flash/index.csv` op "in gebruik".
3. Templates opnieuw bouwen met `scripts/build_template.py`, beelden naar de Klaviyo-bibliotheek, links in `klaviyo-urls.txt`.
4. PLAYBOOK 10 zegt nu "altijd een shoot-foto of geverifieerde Shopify-foto": bij akkoord een regel toevoegen dat AI-flashbeelden uit `content/media/ai-flash/` ook mogen.
