# Plan · nieuwe onderdelen per mail (31 flow-mails v3)

Onderdelen (gebouwd in deze ronde, zie `01-research.md`):

- **ST** sticker in het beeld (`make_sticker.py` + `place_sticker.py`): `NEW`, `BEST SELLER`, `SAVE $XX`. Pill-variant als live tekst in `productcard`.
- **PK** productkaart met stickerbeeld (`blocks/productcard.html`): beeld 200 px desktop, 132 px mobiel, doorgestreepte prijs, HI10-prijs, tekstlink.
- **VT** vergelijkingstabel (`blocks/compare.html`): A tegen coated, B tegen stainless, C tegen cast iron (`comparisons.md`).
- **CL** callout-anatomie (`blocks/closerlook.html`): Pan Pro, Roasting Pan, 6-delige set.

Grondregel: per mail hooguit **twee** van de vier nieuwe onderdelen, anders wordt het een catalogus. VT en het bestaande `features`-blok sluiten elkaar uit (zelfde inhoud). CL en de C2-anatomie (lagen) sluiten elkaar uit.

Prijzen voor SAVE-stickers alleen uit Shopify compare-at: Pan Pro Standard $439 tegen $134 = **SAVE $305** (DECISIONS: mag), 12-delig $1,186 tegen $599 = **SAVE $587** (US only), Roasting Pan $250 tegen $199 = **SAVE $51**, Pan Pro Duo $570 tegen $229 = **SAVE $341**. De 6-delige set van $349 staat op een verborgen listing zonder compare-at: **geen SAVE-sticker** tot dat in Shopify staat (de $399-listing heeft $1,384, maar daar linken we niet naar).

## Per mail

| Mail | Wat erin komt | Waar | Opmerking |
| --- | --- | --- | --- |
| **B1** browse | VT-A (vervangt de huidige drie-koloms tekst-tabel "Nothing to scratch off") | Na de productkaart | Voetnoot "Honest note: a metal spatula can leave fine marks" behouden onder de tabel. Productkaart: ST `SAVE $305` als het bekeken product de Pan Pro is (statisch beeld, dus alleen in de fallback-kaart) |
| **B2-clicked** | PK met ST op het fallback-product | Productkaart | Unieke code staat al in de hero; geen tweede aanbod-sticker |
| **B2-notclicked** | CL Pan Pro | Na de reviews | Reviewmail, CL geeft de "waarom" zonder extra tekst |
| **K1** cart | CL Pan Pro (vervangt `features`) | Onder gifts | Onderwerp "One pass with a damp cloth": later voor/na-frame (schoonvegen) als dat beeld er is |
| **K2-new** | VT-A | Na "de rekensom" | De rekensom (kosten per jaar) en VT samen zijn het hele argument |
| **K2-returning** | PK x2 (deksel, tweede pan) met ST alleen op een product met compare-at | Na de cart | Bestaande klant: geen VT nodig |
| **K3** cart laatste | Niets nieuws in het beeld; eventueel pill `SAVE $305` in de productkaart | | Laatste mail met unieke code: rust, focus op code en deadline |
| **C1** checkout | VT-A (vervangt `features`) | Na gifts | **Demo gebouwd** |
| **C2** checkout "Why Siraat" | Blijft lagen-anatomie; geen CL. VT-A optioneel onder de drie vragen | | **Let op:** huidige anatomie en alt-tekst noemen 0.5 mm / 1 mm / 0.6 mm; claims.csv zet laagdikte op needs-proof. Labels zonder mm tot Floris de dikte bevestigt |
| **C3-P** checkout pan-koper | PK 6-delige set (zonder SAVE) en PK Pan Pro Duo met `SAVE $341`; ST `SAVE $305` op de pan in de rekensom | Setkaart en rekensom | Upsell-mail: hier hoort de prijs-sticker het meest |
| **C3-S** checkout set-koper | CL 6-delige set | Na de cart | Laat zien wat er in de doos zit (Made In-patroon) |
| **C4-US** / **C4-INT** | Geen nieuwe beelden; pill `BEST SELLER` in "Alternatief" | | Unieke code en deadline zijn de boodschap |
| **P1-first** / **P1-repeat** | CL van het gekochte product als "Know your pan" (Pan Pro of set), zonder prijs | Na de order | Geen verkoop, alleen uitleg; nummers en lijst helpen bij eerste gebruik |
| **P2** egg | Nieuw (ronde 3): stap-voor-stap met drie frames uit de chef-video | Stappen | Frames zonder ondertitel (DECISIONS) |
| **P3-pan** | PK deksel en snijplank; ST `NEW` alleen op echt nieuwe items | Productblok | |
| **P3-set** | PK crepe pan en wok; CL niet nodig | Productblok | |
| **P3-accessory** | CL Pan Pro + PK Pan Pro met `SAVE $305` en pill `BEST SELLER` | Product | Koper van accessoire kent de pan nog niet: dit is de plek voor de anatomie |
| **P4** (note) | Niets | | Tekstnotitie |
| **W0** buyers | Niets nieuws; eventueel CL zonder prijs als "your pan, up close" | | Koper, dus geen sticker |
| **W1-A** / **W1-B** | PK Pan Pro met `BEST SELLER`-sticker in "producten" (als die sectie er is) | | Aanbod is HI10; sticker is status, geen tweede aanbod |
| **W2** founder note | Niets | | Tekstmail, zo houden |
| **W3** bewijs | VT-A vervangt de huidige "How it compares"-tekst-tabel | Na certificaat | Rij 4 ("PTFE is itself a PFAS") eerst laten goedkeuren |
| **W4-US** | CL Pan Pro (vervangt "Five reasons") + PK x3 met `SAVE $305`, `SAVE $587` | Na hero; "Three ways to start" | **Demo gebouwd** |
| **W4-INT** | Zelfde als W4-US maar PK zonder 12-delige set (US only); `SAVE $305` op Pan Pro | | |
| **W5** laatste | VT-C (cast iron) of VT-B (stainless) als A/B naast de reviews; PK met stickers in "producten" | Na reviews | Tammy-review ("lighter than my old cast iron") direct onder VT-C |
| **R1-pan** winback | PK Roasting Pan met `NEW` + pill `US ONLY` (alleen US-segment), CL Roasting Pan | Producten | "New since your last order": de NEW-sticker is hier letterlijk waar. Eerst de roasting-pan-PDP corrigeren (zie hieronder) |
| **R1-set** | PK crepe pan, utensils, board; `NEW` alleen voor nieuwe items; CL 6-delige set niet nodig | Producten | |
| **R2** / **R2-VIP** | PK met `SAVE $XX` alleen als compare-at bestaat | Producten | Persoonlijke code is het aanbod; sticker ondersteunt |

## Andere UX-verbeteringen die ik zag

1. **Laagdikte in C2** (0.5 / 1 / 0.6 mm) in beeld en alt-tekst, terwijl claims.csv dit needs-proof noemt. Hoogste prioriteit van deze lijst: corrigeren of laten bevestigen.
2. **Roasting Pan PDP** belooft nog "Lifetime warranty" en "100-day trial" (facts.csv). Elke NEW-sticker die naar die pagina linkt, stuurt mensen naar verouderde beloftes. PDP eerst bijwerken.
3. **Kleine productthumbnails** (94 px in W4, W5, R1, P3): te klein voor een sticker en voor het product zelf. Overstappen op `productcard` (200/132 px) met witte achtergrond (crème van de packshot wordt via `--white` wit, schaduw blijft).
4. **Crème-verschil**: Shopify-packshots hebben #F7F2EC, de mail #F8F7F2. Op crème vlakken met `--bgmatch` gelijktrekken, op witte kaarten met `--white`; dan verdwijnen de zichtbare "doosjes" rond productfoto's.
5. **Tekst-tabellen in B1 en W3** (3 kolommen, 13 px grijs) zijn op mobiel krap. Vervangen door VT.
6. **Features en vergelijking dubbel**: C1, K1, K3 en C3 hebben `features` met dezelfde drie punten als de VT. Kies per mail één van beide.
7. **Maatkeuze W4**: de BEST SELLER-pill naast "Standard 11"" breekt op mobiel naar een eigen regel; prima, maar de nieuwe pill-stijl (ronde hoeken, 10 px) kan hier ook.
8. **Size guide visual**: zodra er packshots van bovenaf per maat zijn (nu alleen Standard), een beeld met vier pannen op schaal en inches/cm eronder voor W4 en B1.
9. **Bewijsbalk in plaats van "as seen in"**: geen persvermeldingen in facts. Light Labs-logo + "Report 25895" + "100,000+ happy customers" als smalle balk boven de footer, tot er echte pers is.
10. **Gewicht**: "lighter than cast iron" is het sterkste argument in VT-C maar heeft geen bron. Floris vragen om het gewicht van de Pan Pro Standard.
11. **Bestandsgewicht**: callout-beelden als JPG (65 tot 90 kB), niet als PNG (350 tot 535 kB). Stickerbeelden altijd ingebakken in een JPG van de productfoto, niet als losse transparante laag (mail kent geen overlap).

## Technisch

- Nieuwe blokken bouwen met `python3 -I scripts/build_research.py <bron> <uit>`; dat vult `{{RBLOCK:...}}` in en roept daarna het bestaande `build_template.py` aan. Zodra Floris akkoord geeft, kunnen de blokken naar `klaviyo/templates/partials/blocks/` en hun defaults naar de DEF in `build_template.py` (dan is `build_research.py` niet meer nodig).
- Beelden voor Klaviyo: uploaden met prefix `email-` naar Shopify Files of de Klaviyo-bibliotheek en in `assets/klaviyo-urls.txt` zetten; daarna maakt `build_template.py` ook de `.klaviyo.html`.
