# Urgentie, social proof en direct response · ronde 7 oktober 2026

Opdracht eigenaar: meer urgentie (countdown), meer social proof (klantfoto's, reviews), betere UX en meer direct response, alles eerlijk. Plus de aanvulling klantbegrip (post-purchase-enquête, `research/survey/01-klantbegrip.md`). Niets naar Klaviyo of Shopify geschreven, niets gecommit, `scripts/build_flow_checkout.py` niet aangeraakt.

## 1. Countdown: hoe hij werkt

**Gekozen: (a) Klaviyo-datumtag.** In een CODE-template werkt:

```
{% today '%Y-%m-%d' as today %}{{ today|days_later:2|format_date_string|date:'l, F j' }}
```

Bron: help.klaviyo.com "Date variables in templates reference" (NL/DE/PT-versies tonen precies dit voorbeeld) en de Klaviyo-community (`days_later` werkt alleen op `%Y-%m-%d`, `%Y-%m-%dT%H:%M:%S` of `%m-%d-%Y`). help.klaviyo.com zelf is vanuit de sessie geblokkeerd, dus via zoekresultaten gecontroleerd. **Eerste Klaviyo-preview controleren** (de datum moet verschijnen, geen lege plek).

In de bron schrijf je de macro `{{DATE:<dagen>:<Django-datumformaat>[:upper]}}`; `build_template.py` maakt daar de tag van. Voorbeeld: `{{DATE:2:D:upper}}` wordt `FRI`, `{{DATE:2:l, F j}}` wordt `Friday, October 9`.

Blokken:
- `{{BLOCK:deadline label="..." amount="48" unit="HOURS" days="2" note="..."}}`: los blok, lichte kaart met drie klok-tegels (48 HOURS · FRI DAY · OCT 9 DATE).
- `{{BLOCK:offer ... deadline="YOUR CODE RUNS OUT" days="2" amount="48" unit="HOURS"}}`: dezelfde tegels in het donkere aanbodblok. Zonder `days` blijft het oude regeltje (`deadline-line.html`).
- Codebalk bovenaan: `YOUR 10% · ENDS FRI OCT 9 · <code>` (in de eerste 600 px).
- P.S. onderaan elke codemail: "Your code runs out on the morning of Friday, October 9."

**Waarom dit eerlijk is.** De code wordt bij verzending toegewezen en vervalt X uur later. Alle codemails gaan om 09:00 lokale tijd (C4, K3, B2, P3, R2, V1, N2 staan op "tot 09:00"), dus de code vervalt op de getoonde dag in de ochtend. De tag rekent in de accounttijdzone (US/Eastern); 09:00 lokaal valt overal ter wereld op dezelfde of een latere kalenderdag in ET, dus de getoonde datum is **nooit te laat**, hooguit een dag te vroeg (Australie, Azie). Daarom geen uur in de tegels en "morning" in de tekst. Geen countdown in mails zonder echte deadline: niet in de nocode-mails, niet bij HI10, niet in welcome.

| Mail | Pool | Looptijd | `days` |
| --- | --- | --- | --- |
| c4 | C4_10_48H | 48 uur | 2 |
| k3 | K3_10_48H | 48 uur | 2 |
| b2-clicked | B2_10_48H | 48 uur | 2 |
| p3-pan, p3-set, p3-next, p3-apron, p3-accessory | P3_THANKYOU_10_14D | 14 dagen | 14 |
| r2 | R2_10_72H | 72 uur | 3 |
| r2-vip | R2_VIP_15_72H | 72 uur | 3 |
| v1 | SK_REGULARS15_14D | 14 dagen | 14 |
| n2 | SK_ANNIV10_7D | 7 dagen | 7 |

**(b) Countdown-GIF (alleen beschrijving, geen account aangemaakt).** Diensten als Sendtric, NiftyImages of MotionMail maken een tikkende timer als beeld; de einddatum gaat als parameter in de beeld-URL. In Klaviyo kun je die einddatum met dezelfde tag in de URL zetten (`...?end={% today '%Y-%m-%d' as today %}{{ today|days_later:2|format_date_string|date:'Y-m-d' }}T09:00`), zodat elke ontvanger zijn eigen timer krijgt die bij het openen echt aftelt. Nodig: een account van de eigenaar, controle dat de dienst een per-ontvanger-URL toestaat en welke tijdzone hij gebruikt, en een test in Gmail en Apple Mail (Outlook toont alleen het eerste frame). Advies: eerst de tag-variant live, de GIF als A/B daarna.

## 2. Klantfoto's: wat er is

**Gevonden: 0 bruikbare echte klantfoto's.**
- Okendo: pannen 0 foto's op 2.226 reviews; snijplank `mediaCount 10`, maar de media staan niet in de PDP-HTML (alleen via api.okendo.io, geblokkeerd).
- Loox (Shopify-metafield `loox.review_feed` op de Pan Pro Standard, alleen gelezen): 4 reviews met foto, alle 4 met 1 tot 4 sterren en een klacht (William J. 4 sterren "The lid is too small", Jafrin Z. 1, Anny H. 3, Glen R. 1). Niet bruikbaar, en images.loox.io is geblokkeerd.
- Trustpilot: geblokkeerd. Shopify Files: geen bestanden met review/ugc/customer. Klaviyo-beeldbibliotheek: Homestead-kaarten met packshots en quotes van onbekende herkomst, niet gebruikt.

Daarom is `{{BLOCK:ugc}}` gebouwd als drie reviewkaarten (beeld, 5 sterren, letterlijke quote, voornaam + "Verified buyer", product). Het beeld is nu een **productfoto van het product uit de review** (kopieën in `klaviyo/templates/partials/shared/ugc-prod-*.jpg`, 328 px = 2x, bijgesneden uit `content/products/*/img/packshot-*.jpg`; originelen niet aangepast), nooit als klantfoto gepresenteerd. Zodra er echte klantfoto's zijn: `ugc-cust-<naam>.jpg` met dezelfde 328 px en `img1="..."`. Desktop drie kolommen, mobiel drie rijen met het beeld links.

Gebruikt in: c1 (kookgerei-tak: Beverley S. PFAS, Avril "works perfectly", Tammy gietijzer), r2 (Don J. tweede pan, Tammy 4e pan, Beverly G. steak), p3-set (Chetan G. crepe, Pam B. wok als cadeau, Sonya D. set). Alle quotes letterlijk uit `content/reviews/reviews.csv`, 5 sterren, gecontroleerd.

## 3. Per flow wat er veranderd is

| Flow | Urgentie | Social proof | Direct response / klantbegrip |
| --- | --- | --- | --- |
| Checkout | C4: codebalk met datum, tegels in het aanbod, P.S. met datum. Geen set-kaart meer in de laatste codemail (Hick's law, en lengte). | C1: derde review-rij met beeld (ugc) in plaats van het tweede reviewblok; quote-regel onder de cart eruit (Avril dekt "werkt het"). C4/K3: reviews in de "Two promises" bij het bezwaar. | Cart-regel overal: "your $70 in gifts are still attached to this cart" (endowment). C4: "HERE IS YOUR 10%", "Last chance for your code", knop "Use my 10% now". C1: maat Standard = "for cooking for 2 to 4", US-termijnregel (Shop Pay Installments, Affirm), vergelijking "No PFAS. No coating.". C2: hero "Non-toxic is easy to say. Here's the report: no. 25895." C3-p: termijnregel US, maatregel. |
| Cart | K3: codebalk met datum, tegels, P.S.; onderwerp "Last chance: your own 10% ends in 48 hours". | K3: reviews in de beloftes, los reviewblok weg (lengte). | K1: hero "Nothing on it to peel off" + "No PFAS. Lab report no. 25895", eerste alinea PFAS, onderwerp "Nothing on it to peel off". K2-new: termijnregel US. |
| Browse | B2-clicked: codebalk met datum, tegels, P.S.; onderwerp "Here is your 10%, for the next 48 hours". | | B1: hero "No PFAS. No coating.", eerste alinea Light Labs 31 PFAS, vergelijking nu tegen stainless steel (tabel B uit comparisons.md, twee eerlijke "too"-rijen). |
| Welcome | Geen (HI10 krijgt nooit een deadline). | | W1-A en W1-B: hero "No PFAS. Nothing to wear off. Report no. 25895", blok "THE IDEA" nu "No PFAS. Here is the paper." met link naar het rapport, onderwerp A "No PFAS, nothing to wear off, and your 10%" (beide armen gelijk, T04 test alleen het aanbod). W4: Standard "Everyday cooking for 2 to 4". |
| Post-purchase | P3 (5 codemails): tegels (14 DAYS) in het codeblok, codebalk met datum, P.S. | P3-set: drie reviews met beeld in plaats van twee. | "HERE IS YOUR THANK-YOU 10%". P1-first en P2/P2-safe openen met de twijfel ("whether it keeps its promises, the first egg will tell you"); P2 noemt steak als tweede kook. Gifts-blok uit p3-pan/set/next (lengte; P.S. noemt de gifts). |
| Winback | R2/R2-VIP: codebalk met datum, tegels (72 HOURS), P.S. | R2: drie reviews met beeld (tweede pan, vierde pan, steak). | "HERE IS YOUR 10%/15%", knop "Use my 10% now", onderwerp R2 "Here is your 10%, for the next 72 hours". |
| VIP, Anniversary | V1 (14 dagen), N2 (7 dagen): codebalk, tegels, P.S. | | "HERE IS YOUR 15%", "HERE IS YOUR ANNIVERSARY GIFT". |

Gift card-vorm voor codemails: **niet gedaan**. Een unieke procentcode is geen tegoed; "gift card" belooft geld. Eerst de W1-test (T04: HI10 als code tegen HI10 als gift card) uitlezen; wint B, dan een "thank-you card" voor P3/V1 overwegen.

## 4. C4 vereenvoudigd

Nieuwe ID's: **`checkout/c4.html`** (code, T02-A) en **`checkout/c4-nocode.html`** (T02-B en cooldown). UTM `utm_content=c4-*` en `c4nocode-*`. W4 is **niet** samengevoegd: het verschil is groot (prijzen in de maattabel, drie tegen twee productkaarten, andere hero) en welcome heeft geen event, dus alleen het profielland zou kiezen.

Landvoorwaarde in de template (US-tak, anders INT):

```
person.Country == 'United States' or person.Country == 'US' or not person.Country and event.extra.presentment_currency == 'USD' or not person.Country and not event.extra.presentment_currency
```

`person.Country` is de vorm uit Klaviyo's "Message personalization reference"; de community meldt dat `person.location.country` niet werkt. Nog niet op een echt profiel getest. INT krijgt de INT-hero, "Duties paid" in de friction reducers en de duties-zin in het aanbod; c4-nocode US krijgt de 12-delige set (alleen bij kookgerei), INT de iconen met "No import duties". De oude c4-us, c4-int, c4-us-nocode en c4-int-nocode staan nog in de map maar zijn uit de inventaris (v4-flow-system.md sectie 5, plus bouwnotitie), uit `qa_render.py` en uit de export (export en QA slaan nu alles over wat niet in de inventaris staat).

## 5. Gewijzigde scripts en tests

- `scripts/build_template.py`: `{{DATE:...}}`-macro, blokken deadline en ugc, offer met `days`, `today` als besturingstag in commentaar (zoals `if`), preview vult een voorbeelddatum in, standaard cart-regel met "$70 in gifts are still attached". `research/tailoring/test/expand.py` opnieuw afgeleid (script: scratch `mkexpand.py`, kopieert build_template t/m de _style.css-regel).
- `research/tailoring/test/kltags.py`: Klaviyo `today`, `days_later`, `format_date_string`. `scripts/qa_render.py`: allowlist plus `today`/`days_later`, alleen inventaris-mails. `scripts/export_klaviyo.py`: alleen inventaris-mails. `run_tests.sh`: tests voor c4, c4-nocode en c1 (63 controles).
- Blokken: `partials/blocks/deadline.html` (nieuw), `deadline-offer.html`, `deadline-line.html` (het oude regeltje), `ugc.html`, `_style.css` (mobiel ugc en tegels), `codebar.html` (lange tags breken in de ruwe editor).
- Nieuwe beelden (nog te uploaden bij export): `welcome/assets/w1-hero-pfas.jpg`, `checkout/assets/c2-hero-pfas.jpg`, `browse/assets/b1-hero-pfas.jpg`, `cart/assets/k1-hero-pfas.jpg` (nieuwe namen, zodat de oude CDN-koppeling niet het oude beeld levert), `partials/shared/ugc-prod-{panpro,panpro-b,panpro-c,wok,set6,crepe}.jpg`. Hero-register bijgewerkt.

## 6. QA

- `python3 -I scripts/qa_render.py`: 59 mails, 59 groen, 0 FOUT. Boven 3.600 px (waarschuwing, onder de grens van 3.780): c1 3.671, b1 3.605, p3-apron 3.603; p1-first en p2 mogen langer.
- `scripts/check_previews.py`: 0 problemen. `research/tailoring/test/run_tests.sh`: 63 ok, 0 FOUT. `scripts/export_klaviyo.py` (dry-run): 59/59 klaar, 95 beelden te uploaden.
- Zelf bekeken (desktop 700 en mobiel 390): C1, C4, K3, W1-B, P3-pan, R2. Aangepast na het kijken: W1-hero naar drie regels (kop liep tot de rand), B1-kop korter, dubbele kop in R2, ontbrekende tabelopening in de eerste C4-versie.

Screenshots:
- `klaviyo/templates/v3/checkout/previews/c4-mobile.png` en `c4-desktop.png`
- `klaviyo/templates/v3/checkout/previews/c1-desktop.png` (ugc in drie kolommen)
- `klaviyo/templates/v3/cart/previews/k3-mobile.png`
- `klaviyo/templates/v3/welcome/previews/w1-b-mobile.png`
- `klaviyo/templates/v3/post-purchase/previews/p3-pan-mobile.png`
- `exports/qa/shots/winback-r2-mobile-rendered.jpg`

## 7. Open punten voor de eigenaar

1. **Datumtag en `person.Country` in een Klaviyo-preview controleren** (testprofiel met land "US", een met "Netherlands", een zonder land) voordat C4 live gaat. De datum toont de ochtend van de vervaldag in US/Eastern.
2. **Termijnregel** ("Prefer to pay over time? Shop Pay Installments and Affirm are at checkout.") staat nu in C1, C3-p en K2-new, alleen US. DECISIONS zegt: pas na akkoord op de claim. Akkoord geven of de zin schrappen.
3. **Maatregel** Standard 11" = "cooking for 2 to 4" (A1, Gorgias) is nu overal gelijk; bevestigen.
4. **Klantfoto's**: een Okendo-export met media-URL's (en de 10 snijplankfoto's) of een paar foto's van klanten met toestemming. Het ugc-blok is er klaar voor.
5. **Flow Y6yj2z** (andere agent): landsplits weg, berichten c4 en c4-nocode koppelen. Welcome-split W4: voeg "US" toe naast "United States".
6. **Countdown-GIF** (optie b): account bij een timerdienst als je de tikkende versie wilt testen.
7. De .klaviyo.html-bestanden in de mailmappen zijn niet bijgewerkt voor mails met nieuwe beelden (die worden pas bij `--live` gebouwd); de dry-run en QA bouwen vers.
