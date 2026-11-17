# Welcome v6 · "The sealed envelope" (concept, 17 nov 2026)

Status: **concept**. Niet in Klaviyo als template of flow; live welcome T4a5Mk is niet aangeraakt. Welcome-tests starten na Cyber Monday (2 dec), zoals afgesproken.

- HTML: `klaviyo/templates/v3/welcome/v6-envelope/` (`e1.html` t/m `e5.html` = Klaviyo-versie, `-preview.html` = Django-tags vervangen). Bouwen: `python3 -I _tools/build.py`, renders: `node _tools/shot.js`.
- Renders (600 en 390 px, DSF 2): `klaviyo/templates/v3/welcome/v6-envelope/renders/`.
- Beelden: 7 envelop-beelden (Revana-set van Floris), 1200 px JPG < 300 KB, in de Klaviyo-bibliotheek (`assets/klaviyo-urls.txt`). Productbeelden en gifts uit de bestaande gedeelde set.
- Figma: bestand oaxnBkz3MAbePRnorCrQwz, pagina All emails, rij "Row 1e · v6 · Welcome · Sealed envelope (concept, 17 nov)" (node 330:106), direct onder Row 1d.

## Idee

Van Smooche overgenomen: één object (een verzegelde envelop) dat in mail 1 opengaat en door de hele reeks terugkomt, een "how it works" in 3 stappen, productkaarten met een quote als kop en de code op elke kaart, een vergelijkingstabel, platte brieven ertussen.

Bewust niet overgenomen, en waarom:

| Smooche | Waarom niet |
| --- | --- |
| "VIP", wax seal "VIP", "handpicked" | Iedereen die zich inschrijft krijgt hetzelfde. Selectie suggereren is misleidend. |
| "How much is inside?", "What if yours is the biggest one?" | Het bedrag varieert niet (altijd 10%). Een variabel bedrag suggereren is niet waar. |
| "Tap to reveal", onthulling pas in de checkout | Het aanbod staat gewoon in mail 1. De "onthulling" is de echte inhoud: 10% plus 5 gifts, en daarna het verhaal. |
| "Disappears tomorrow at midnight", countdown "extra 30% off" | HI10 heeft geen einddatum (DECISIONS, skill: HI10 never gets a deadline). Er is ook geen extra korting. Geen deadline, geen countdown. |
| Before/after-resultaten | Geen echte before/after van koken beschikbaar; nooit nep-resultaten. Alleen echte product- en envelopbeelden. |
| Merk in de vergelijking ("your old foundation") | Alleen "a PFAS-coated pan", geen merknamen, geen gezondheidsclaim (DECISIONS 8 okt). |

Eerlijke vervanger van urgentie: geen. De reeks zegt juist "no clock on it". Dat is ook het onderscheid van Siraat ("We never scare people into buying", Brand System 09).

## Aanbod

- **HI10**: 10% korting, 1x per klant (Shopify appliesOncePerCustomer), geen einddatum. Toegepast via `/discount/HI10?redirect=<URL-encoded pad + UTM>` (patroon F13/ROAST15). Cartlink `/discount/HI10?redirect=/cart`.
- **5 free gifts with every order**: Free shipping, Plastic-free e-book, Mystery gift, Favorites Cookbook, chance to win a PFAS water filter (weekly draw). Geen totaalbedrag in de mails (de $450-filter hoort niet in een optelsom).
- Live W1 (UkRMjM) is nu de Black Friday-mail zonder code. Na BF valt welcome terug op HI10; deze concepten gaan daarvan uit. [VRAAG FLORIS: blijven de 5 gifts na 30 nov?]

## Reeks

Trigger, filters en timing als v4 (T4a5Mk): inschrijving op de lijst, geen order sinds start (kopers verlaten de flow), bestaande klanten naar W0.

| # | Timing | Rol | Onderwerp A / B | Preview |
| --- | --- | --- | --- | --- |
| E1 | 5 min | **Geld** (vervangt W1). Envelop gaat open: 10% + 5 gifts, code als live tekst, knop en cartlink boven de vouw, how it works in 3 stappen, gifts, korte noot van Benjamin ("no lottery, no secret amount, no clock"), rapport 25895. | Your welcome envelope is here / Inside: 10% off and 5 free gifts | Open it: 10% off with HI10, plus 5 free gifts with every order. Same for everyone, no expiry. |
| E2 | +1 dag 10:00 | **Verhaal**. "Het tweede ding in je envelop": naam (sirat, path), de mark (S I R A A T, in de stijl van square Kufic), de zandlijn, oorsprong (snijplanken, de originele gehamerde titanium pan, eerste orders 20 dec 2024, 100,000+). Aanbod in de P.S. | What the seal on your envelope says / From sirat, the Arabic word for path | The second thing in your envelope: what our name means. (Your 10% is in the P.S.) |
| E3 | +2 dagen 09:00 | **Bewijs**. Drie checks (rapport 25895 / oppervlak / 75 jaar + 30 dagen), tabel Siraat vs "a PFAS-coated pan" (4 rijen uit research/ux-round2/comparisons.md A, rij PTFE weggelaten), eerlijke regel over voorverwarmen, review R169. | Report no. 25895 / Has your pan been tested? | 31 PFAS compounds tested. Every one below the detection limit. Read it yourself. |
| E4 | +3 dagen 09:00 | **Herinnering met productkaarten**. "Still sealed?" = de code is nog niet gebruikt (kopers zijn al uit de flow). Drie kaarten met een letterlijke klantquote als kop, de code op elke kaart en een eigen knop: Pan Pro Standard (R518 Graham C.), 6-delige set (R398 Fatima), Wok (R466 James). Geen prijzen (post-BF-prijzen nog onbekend). | Still sealed? / "I ended up buying the whole collection" | Your 10% is still unused. Three places people start, in their own words. |
| E5 | +4 dagen 09:00 | **Platte brief van Benjamin**, laatste mail. Geen druk, twee beloftes (30 dagen retour ongebruikt; defect in 30 dagen: refund of vervanging, wij betalen verzending; daarna 75 jaar garantie), twee tekstlinks met HI10, reply-vraag. Vaste header en footer blijven (CLAUDE.md, geen uitzondering voor welcome). | Last note about the envelope / Two promises, before you decide | No clock on it. Just two promises, and the pan I would start with. |

A/B per mail: alleen het onderwerp, winnaar op unieke kliks, daarna omzet per ontvanger.

## Hoe het past bij W1 tot W5

- W1 brengt $2.96 per ontvanger en maakt het grootste deel van de welcome-omzet (research/v6-golive/20-welcome-analyse.md: kopers bestellen vaak binnen een uur, de code is de reden om te openen). Daarom houdt E1 dezelfde rol: code direct zichtbaar, knop boven de vouw, cartlink. E1 is een **test tegen de W1 die na BF live staat**, niet een stille vervanging.
- E2 t/m E5 vervangen de slots W2 t/m W5 (zelfde timing). Ze zijn ook te combineren met v5 "Brand story" (Row 1c): E2 overlapt met v5 W2 (The name); kies er één.
- Voorstel testvolgorde vanaf 2 dec: (1) E1 tegen huidige W1, 50/50, minimaal 4 weken, beslissen op kopers en omzet per W1-ontvanger (alle orders, niet Klaviyo-toeschrijving) en uitschrijvingen. (2) Pas daarna E2 t/m E5 als blok tegen W2 t/m W5.
- Concept "Row 1d" (322:89, eerder op 17 nov in Figma) bevat een countdown/deadline-tegels in E2, "tap to break the seal at checkout" en "4 gifts"; die versie voldoet niet aan de eerlijkheidsregels hierboven. Row 1e is de versie om verder mee te gaan.

## QA (17 nov)

| Mail | 600 px | 390 px | Overloop | Kapotte beelden | Em dash |
| --- | --- | --- | --- | --- | --- |
| E1 | 2,757 | 2,852 | nee | 0 | 0 |
| E2 | 2,617 | 2,637 | nee | 0 | 0 |
| E3 | 2,532 | 2,809 | nee | 0 | 0 |
| E4 | 2,650 | 2,760 | nee | 0 | 0 |
| E5 | 1,338 | 1,532 | nee | 0 | 0 |

Alle mobiele hoogtes onder 3,700 px. Reviews letterlijk gecontroleerd tegen content/reviews/reviews.csv. Niet gedaan: qa_render.py per markt (concept zonder marktlogica: friction reducer en "Free shipping" zijn US-tekst; voor livegang `{{FRICTION}}` en `{{IF:US}}` gebruiken of een INT-versie maken).

## Open vragen voor Floris

1. Blijven de 5 gifts na 30 nov, en welke prijzen/sale gelden er vanaf 2 dec?
2. Het zegel op de envelop-beelden is AI-gegenereerd; is de mark daarop goed genoeg (CLAUDE.md: logo nooit nagebouwd)? In de header staat altijd de officiële lockup.
3. Mag "the size most people pick first" (Pan Pro Standard) blijven? Bron: welcome-kopers (analyse 20), niet in claims.csv.
4. Row 1d (322:89) laten staan, verwijderen of als "afgekeurd" markeren?
