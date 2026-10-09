# 16 · Gmail iPhone: lege productkaart en witte footer (10 okt 2026)

## Wat Floris zag

Preview-send INT-receptmail als UK-profiel, Gmail-app iPhone, tweede testmail in dezelfde thread als de eerste:
1. Productkaart "Find your pan for this recipe": links het panbeeld, rechts een lege witte kolom; daaronder Gmail's `•••` en pas daarna los "£248 £124" en "SHOP THE PAN", tegen "The fall sale is on..." aan.
2. Footer wit in plaats van #282828: navigatie (lichte tekst) bijna onzichtbaar, logo als zwart blok (de lockup `logo-white-dark.png` heeft #282828 ingebakken).

## Oorzaak

- **Gmail-trimming in een thread (hoofdoorzaak).** De `•••` is Gmail's knop "getrimde inhoud tonen": Gmail ziet het einde van de tweede mail als herhaling van de eerste (zelfde afzender, zelfde onderwerp, zelfde tekst) en klapt het in. De knip viel midden in de kaart. Bij het uitklappen zet Gmail het getrimde deel los onder de mail, buiten de oorspronkelijke tabellen: losse `<tr>`/`<td>` vallen weg, en daarmee alles wat alleen op die cel stond. De footer had zijn donkere vlak alleen als CSS (`style="background:#282828"`, geen `bgcolor`) op één `<td>`; zonder die cel staat lichte tekst op wit. Bewezen met de simulatie `gmailtrim` op de oude build: exact het beeld van Floris (contrast 1,12:1 op de navigatie), zie `research/campagnes/recept-01-int-gmailsim/voor-UK-gmailtrim-onderkant.jpg`.
- **Kwetsbare constructies die het erger maakten:** productkaart met een vaste kolom van 200 px plus een `<a>` om blok-divs (titel, tekst, prijs), stapelen alleen via media queries; footer en header zonder `bgcolor`; hoofdkolom en knop met vaste breedte (zonder `<style>` werd de mail 430 tot 460 px breed).
- **Niet de oorzaak:** de Klaviyo-HTML die Gmail ontving is structureel in orde (gecontroleerd op de US-verzending van 9 okt in de testinbox, bericht 1a1211595b946173), geen ongesloten tags, 53 KB (ruim onder de 102 KB-clipgrens). De light-only-wijziging en de preheader-div spelen geen rol.

## Fix (geldt voor alle 63 mails)

- `partials/blocks/productcard.html`: hybride kaart van geneste tabellen. Beeld en tekst zijn twee inline-block tabellen (max 200 en 308 px); op desktop naast elkaar, op mobiel tekst onder het beeld, ook zonder media queries. Titel, tekst, prijs en "Shop the pan" in eigen cellen binnen de kaart. Outlook: ghost table.
- `partials/footer.html`: `bgcolor="#282828"` + inline `background-color` op de buitencel, de binnentabellen en elke tekstcel. Valt een laag weg, dan blijft het vlak donker. Laatste regel: verborgen unieke verzendstempel `{% today '%Y%m%d%H%M%S' as sk_ref %}ref {{ sk_ref }}` zodat Gmail twee mails niet als herhaling inklapt.
- `partials/header.html` bgcolor; navigatie mag afbreken. `blocks/cta.html` vloeiend (`width:100%;max-width:340px`). `blocks/closerlook.html`: gekleurde divs naar cellen met bgcolor.
- `scripts/build_template.py`: elke `<table>/<td>/<th>` met een kleur krijgt automatisch bgcolor én inline background-color (`bg_attrs`); hoofdkolom `width:100%;max-width:600px` (`fluid_main`), Outlook houdt 600 px via de MSO-stijl.

## QA

- `mail_checks.bg_problems` (statisch, FOUT in `qa_render.py`): kleur alleen als CSS op een cel, bgcolor zonder inline kleur, gekleurde div, lichte tekst zonder donker bgcolor-vlak.
- `scripts/qa_mail_shots.js` modi `gmailios` (alle `<style>`, `<link>`, classes en color-scheme weg; te brede mail wordt ingeschaald) en `gmailtrim` (idem plus de laatste rijen los achter `•••`). FOUT in `qa_render.py` bij een tekstcel die leeg rendert, tekst buiten zijn cel of in een kolom < 48 px, of tekst met contrast < 2,2:1. Screenshots `exports/qa/shots/<flow>-<id>-gmailios.jpg` en `-gmailtrim.jpg`.
- Resultaat 10 okt: `qa_render.py` 63/63 groen. 54 mails zijn zonder `<style>` nog iets breder dan 375 px (Gmail schaalt in): waarschuwing, geen fout.

## Testen in Gmail: let op

- Twee testmails met hetzelfde onderwerp naar hetzelfde adres komen in één thread; Gmail trimt dan de herhaalde inhoud van de tweede en toont die na `•••` zonder de opmaak eromheen. Beoordeel een testmail daarom altijd als **eerste** mail van een thread: geef elke preview-send een uniek onderwerp (bijv. "[T3]" erachter) of verwijder de vorige testmail eerst. De verzendstempel in de footer voorkomt het trimmen in echte verzendingen; bevestig één keer met een Klaviyo-preview dat `{% today '%Y%m%d%H%M%S' %}` uren, minuten en seconden geeft.
