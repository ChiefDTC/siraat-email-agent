# Polijstronde v4 (eindredactie, 7 oktober 2026)

Lengte = mobiele render op 390 px, inclusief footer (~546 px), van de `-preview.html` na Django-render op het voorbeeld-event (tabel onderaan). Niets in Klaviyo, Shopify of Figma gewijzigd, niets gecommit.

## Per mail (inkorting)

| Mail | Oud | Nieuw | Wat ging eruit |
| --- | --- | --- | --- |
| w3 | 3.943 | 3.247 | Closer look "What was tested" (de drie vragen + certificaat dragen het bewijs al) |
| w4-us | 4.220 | 3.534 | Closer look (W3 doet de uitleg); maatkiezer zonder doorgestreepte prijzen |
| w4-int | 3.995 | 3.345 | Closer look |
| w5 | 3.734 | 3.485 | Iconenblok; tussenkop "In their words" (de opener zegt het al) |
| k1 | 3.793 | 3.578 | Iconenblok; aanhef in de afsluiting |
| k2-new | 3.978 | 3.288 | Iconenblok; gifts-blok vervangen door één regel ($70 in gifts + kans op filter); voetnoot onder de som korter; afsluiting korter |
| k3 | 3.789 | 3.598 | Iconenblok (beide takken, Two promises zegt hetzelfde); regel "A few photos..."; afsluiting zonder herhaling "last email" |
| b1 | 3.771 | 3.580 | Iconenblok |
| b2-notclicked | 4.036 | 3.343 | Closer look (vier verhalen dragen de mail; B1 doet de uitleg) |
| c1 | 3.719 | 3.588 | Iconenblok |
| c2 | 3.692 | 3.561 | Iconenblok |
| c3-s | 3.703 | 3.589 | Iconenblok |
| c4-us | 3.690 | 3.559 | Iconenblok (Two promises zegt het) |
| r1-acc | 3.694 | 3.543 | Iconenblok; kaarten nu via het blok |
| r2 | 3.800 | 3.113 | Gifts-blok wordt een zin in het codeblok; reden + "daarna" van de deadline uit de opener naar het codeblok (stond dubbel); iconenblok |
| r2-vip | 3.833 | 3.122 | Idem; afsluiting korter |
| v1 | 3.752 | 3.065 | Idem (gifts in codeblok, dubbele deadline-uitleg uit opener, iconen) |
| v1-nocode | 3.649 | 3.517 | Iconenblok |
| n2 | 3.815 | 3.102 | Idem als v1 |
| p3-accessory | 4.012* | 3.286 | Iconenblok; gifts-blok wordt een regel in het codeblok |
| p3-accessory-nocode | 3.772* | 3.527 | Iconenblok |
| p3-next | 4.337* | 3.558 | Iconenblok (*oude preview toonde alle takken tegelijk) |
| a2 | 3.706 | 3.534 | Iconenblok |

Bewust lang gelaten: p2 (3.990) en p1-first (3.818, onboarding, geen verkoopmail). Overal bleven aanbod, cart/product en knop boven de vouw en minimaal 2 reviews (k2-new had al één case, ongewijzigd).

Keuze om te controleren: in r2, r2-vip, v1, n2, k2-new en p3-accessory is het gifts-blok een zin geworden ("Plus $70 in gifts with every order"). Alleen de iconen schrappen was niet genoeg; de gifts zijn bij terugkerende klanten al bekend. Terugzetten kan per mail met `{{BLOCK:gifts ...}}`.

## Prijzen (opdracht 2)
- Live gecontroleerd (Replo, alleen lezen): Mini $129 / compare-at $180, Small $127 / $419, Standard $134 / $439, Large $139 / $455. Mini, Small en Large hebben dus wél een compare-at in Shopify; alleen Standard is door Floris bevestigd als anker. De skill en de brief zeggen "geen compare-at": die regel klopt niet met Shopify.
- Weggehaald: alle strepen door de eigen verkoopprijs om een codeprijs te tonen. W4-US maatkiezer ($129, $127, $134, $139); P3-pan, P3-next, P3-set (deksel $59, plank $69, crêpe $139, wok $119, tweede Pan Pro $127). Nu: prijs gewoon, codeprijs in de note ("$53.10 with your code").
- Blijft (echte compare-at): Pan Pro Standard $439 bij $134, 12-delige set $1,186 bij $599, Roasting Pan $250 bij $199. A1 streept alleen $439 bij Standard.

## Blokken en scripts
- `productcard`: `img` mag `{{IMG}}/bestand` zijn; `us="1"` (prijs + note alleen US), `us="price"` (alleen prijsregel), `uscond` overschrijft; geen lege prijsdivs meer. Voorwaarde per trigger in `USCOND` (build_template.py). Alle 23 inline kaarten (k2-returning, p3-*, r1-acc, r1-pan) zijn nu blokken; k2-returning gebruikt `us="1"`/`us="price"` in plaats van een if/else met dubbele kaarten.
- Header: `.navhide` staat nu in `blocks/_style.css` (post-purchase miste de regel, daardoor stond COOKWARE naast het logo op 390 px) en de nav-cel kreeg 20 px links. `v3/checkout/partials` (kopie) verwijderd.
- `research/tailoring/test/expand.py` opnieuw afgeleid van build_template.py; `kltags.py` kent nu `unsubscribe_url` (sunset rendert).
- Hero's >250 KB opnieuw opgeslagen (q80-82): p3-apron(-nocode), hero-w0/w3/w4-int/w5 (ongebruikt), w3-hero (283 KB), r1-acc-hero (255 KB). w3-hero en r1-acc blijven net boven 250 KB bij q80.

## Consistentie
- Friction reducer overal 12/18 px en de drie standaardteksten (US/HI10, unieke code, INT); c4-int houdt "One use, already applied. Duties paid. 30-day returns."
- "A real person reads every email", "I read every answer", "I'll tell you" en varianten overal vervangen door "our team" / "Every reply reaches our team".
- Gifts: "with every order" in plaats van "with your order". E-book-label in het gifts-blok ongewijzigd (open vraag 33).
- Ondertekening was al overal "Benjamin / Founder, Siraat's Kitchen". "Pure titanium surface" kwam niet voor.

Controles: `check_previews.py` 0 problemen; `run_tests.sh` 44 ok, 0 FOUT (geen verwachte tekst aangepast); geen `{%` in previews; geen em dash.
