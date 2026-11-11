# Beeldbrief · Shopify-orderbevestiging

Geen beelden gegenereerd. De voorbeelden gebruiken bestaande Siraat-beelden van de Shopify- en Klaviyo-CDN. Deze brief is voor wie later nieuwe beelden maakt in Higgsfield (flash-stijl, skill `siraat-flash-style`). Vaste regels voor elke prompt: nooit tekst, letters, logo of opdruk renderen (schortbandjes "plain cream straps, no text, no patch"), alleen kale gehamerde titanium pannen, nooit zwart gecoat kookgerei. Upload 1 of 2 echte shootfoto's als referentie; het logo komt er nooit in (in de mail staat het al in de header).

## Beeldplekken

| Variant | Plek | Nu in het voorbeeld | Formaat | Veilige tekstzone |
| --- | --- | --- | --- | --- |
| A | geen beeld (bewust: rustig bonnetje) | n.v.t. | n.v.t. | n.v.t. |
| B | hero, direct onder de header | `siraat-titanium-hammered-deep-pan-10-family-dinner.webp` (Shopify CDN, 1200x800) | 1200x800 (3:2), weergave 600x400 | Geen tekst in het beeld; kop staat als live tekst eronder. Houd onderste 15 procent rustig voor een eventuele crop naar 1200x700. |
| C | geen beeld (checklist moet boven de vouw) | n.v.t. | n.v.t. | n.v.t. |
| Alle (optioneel) | "What's in your box", boven of naast het giftsblok | nog niet, gifts gebruiken de echte gift-tegels | 1200x800 (3:2) | Linkerbovenhoek 30 procent leeg voor een eventuele label-pil. |

## Prompt 1 · Hero variant B (vervangt de family-dinner-foto, zodat P1 en de bevestiging niet dezelfde foto delen)

"Candid flash snapshot of two friends in their early 30s laughing in a cozy lived-in home kitchen at night, a woman in a deep forest green chef apron with plain cream straps, no text, no patch, over a mustard knit sweater, sliding a just-cooked fried egg out of a bare shiny hammered titanium frying pan onto a ceramic plate while her friend in a navy apron cracks up beside her, pan in the lower center of the frame with visible hammered texture, wooden open shelves crowded with spice jars and plants in the background, direct on-camera flash, hard flash shadow on the wall, slightly overexposed highlights on the steel, warm tungsten glow behind, 35mm film grain, slight vignette, amateur party-photo energy, shot on a compact point-and-shoot camera, horizontal 3:2, no text, no letters, no logos, no black coated cookware"

Negatief: text, letters, logo, watermark, label, black nonstick pan, studio softbox, daylight, stock smile, restaurant kitchen, more than 3 people.

## Prompt 2 · Alternatief hero B (sfeer, "first cook")

"Candid flash snapshot of a laughing man in his late 20s in an ochre chef apron with plain cream straps, no text, no patch, holding a bare hammered titanium pan over a gas flame and flicking a drop of water into it, the drop beading on the hot silver surface, a friend blurred in the background raising a glass, lived-in home kitchen at night, tiles and cluttered wooden shelves, direct on-camera flash, hard shadow on the cabinets, warm tones, 35mm film grain, imperfect framing, horizontal 3:2, subject on the right third, left third falling into warm darkness, no text, no letters, no logos, no black coated cookware"

## Prompt 3 · Packshot "What's in your box" (alle varianten, optioneel)

"Overhead flat lay on a warm oak kitchen table at night, laid out neatly: one bare shiny hammered titanium frying pan with a long silver handle, one stainless steel lid beside it, a small plain kraft gift box tied with red ribbon, a plain white pouch of dishwasher sheets with no print, a closed plain cream paperback cookbook with a blank cover, warm side light from a low lamp plus a soft on-camera flash fill, gentle shadows, a few herbs and a linen napkin as props, 35mm film grain, warm color cast, horizontal 3:2, top left area kept empty, no text, no letters, no logos, no printed labels, no black coated cookware"

Let op: e-book, kookboek en filter zijn in het echt digitaal of een loting. Toon in de packshot alleen wat echt in de doos zit (pan, deksel, mystery gift, sheets) of zet er in de mail een regel bij "Digital gifts arrive by email". De boeken liever weglaten als dat verwarring geeft; dat is precies het probleem uit de tickets.

## Bestaande beelden die nu gebruikt worden

- Lockup zwart (header): `brand/logo/lockup/siraat-lockup-black-email.png` = Klaviyo-CDN ae4dfc27.
- Lockup wit op donker (footer): `partials/shared/logo-white-dark.png` = Klaviyo-CDN c8e347f7 (zelfde als vaste footer).
- Orderregels: in Shopify `line.image`; in de preview Pan Pro Standard (Shopify CDN), `pc-lid.jpg`, `pc-sheets.jpg`.
- Gifts: de echte tegels `gift-mystery`, `gift-shipping`, `gift-ebook`, `gift-cookbook`, `gift-filter` (Klaviyo-CDN, zie `partials/shared/klaviyo-urls.txt`).
- Iconen: `icon-returns-30-day`, `icon-warranty-75-year`, `icon-customers-100k`.

## Herontwerp B2 tot B4 (11 nov 2026)

- Hero (alle drie): `assets/oc-hero-flash-egg.jpg`, 1168x880, Higgsfield gpt_image_2_6 met de echte Pan Pro-foto (P04-A) als referentie. Twee vrienden lachen, kale gehamerde pan met gebakken ei, onderste 40 procent donker aanrecht voor de live tekst. Klaviyo-CDN 5d0622a1. Afgekeurd: een tweede hero (witte randartefact door vignet) en een close-up met handen (waterdruppel werd een lepel).
- Pijlers: echte shootfoto's van de Shopify-CDN: P11-E (oppervlak, non-toxic), P04-A (steak, performance), P11-C (rand, titanium), P09-B (ei, eerste week). Lab-pijler zonder foto: donker blok met "No. 25895".
