# Mystery Gift flow: hero-beelden (Higgsfield, 19 oktober 2026)

Status: concept. Niet in Klaviyo geupload. Vervangen de placeholders in deze map.

## Werkwijze

- Model: `gpt_image_2_5` (GPT Image 2.5, variant flare), quality high, resolutie 2k, ratio 3:2 (2048x1360). 2,75 credits per beeld, 8 beelden = 22 credits.
- Bewerking: midden uitgesneden naar 3:2 (1200:792) en verkleind naar 1200x792, JPEG kwaliteit 80 (Pillow). Geen opschaling.
- Stijl: skill siraat-flash-style (directe flits, lachende mensen, woonkeuken 's avonds). Schorten effen met effen creme banden, geen patch, geen tekst (PLAYBOOK 3).
- Referenties via `media_import_url` (upload.higgsfield.ai is geblokkeerd):
  - pan: Shopify CDN `email-hp-square-P04-A_Stovetop_Pan.jpg` (media `d34f4530-45b6-4a80-885b-2b119bd446ac`)
  - kraft doos met rood lint: Shopify CDN `GiftSiraat_87ead149-...jpg` (media `f531ff5b-dab4-49da-b8ef-732a40d16f89`)
  - vel in pan: Shopify CDN `sheet_in_pan.webp` (media `02e1a889-6331-4c20-9b6c-f80b8461027a`)
- Het echte pak (packshot met SIRAAT, Dishwasher Sheets, Up to 60 washes) is bewust niet als referentie gebruikt: het model zou de tekst verhaspelen. In m4 staat het pak zonder opdruk (wit met okerband). Echte packshot later in Figma of als apart blok.
- Alle vier op volle grootte gecontroleerd: geen letters, logo's of etiketten, geen zwarte coating, handen en vingers in orde. Gezichten zijn verzonnen personen: nooit als klant of review gebruiken.

## Beelden

### m1-hero.jpg

- De reveal: lachende vrouw opent de kraft doos naast een gehamerde pan
- Gekozen job: `59b78b37-566d-4ed3-940e-88d70ae28cb5`
- Afgekeurde variant: `2a76dab8-d326-48f2-96c4-ab216519ea80`
- Referenties: pan (P04-A) + kraft doos (GiftSiraat)
- Gekozen: meer donkere ruimte links, doos in het midden van het beeld, pan rechts. Afgekeurd: pan stond links in de kopruimte.

Prompt (beide varianten gelijk):

> Candid flash snapshot of a woman in her early 30s with curly dark hair, in an ochre apron that is completely plain fabric with plain cream straps over a cream knit sweater, laughing hard with crinkled eyes and open mouth at the moment she lifts the lid off a small kraft paper gift box tied with a red satin ribbon bow (like the gift box reference), at a wooden kitchen counter, a shiny hammered titanium frying pan sits on the counter next to the box. A friend partly cut off at the right edge laughs along. Cozy lived-in home kitchen at night, wooden open shelves with spice jars, plants and cookbooks behind her. Direct on-camera flash as the only key light, hard crisp flash shadow on the wall behind the subject, slightly blown highlights on skin and steel, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Email hero composition, horizontal 3:2: all subjects and products sit in the right 55 percent of the frame; the left 40 percent is a calm, dark, low-detail area where the flash falls off into a plain dark wall and an empty counter, so a headline can sit there. Cookware matches the reference photo: bare silver titanium pan, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handle without any engraving, zero coating; never black nonstick cookware. The gift box is plain kraft paper with only the red ribbon, no tag, no print. Strictly no text, no letters, no numbers, no logos, no labels on jars, bottles or packaging anywhere in the image.

### m2-hero.jpg

- Hand laat een vaatwasvel in het bakje vallen, gehamerde pannen in het rek
- Gekozen job: `dd91a834-2c36-476a-9429-e3371d600532`
- Afgekeurde variant: `357b30e1-1b9b-4609-b9dd-609c321254ec`
- Referenties: pan (P04-A) + sheet_in_pan
- Gekozen: hamerslag alleen binnenin, buitenkant glad zoals de echte pan. Afgekeurd: pannen ook aan de buitenkant gehamerd. Let op: het vel is grijzig en papierachtig, het echte vel is wit en doorschijnend.

Prompt (beide varianten gelijk):

> Candid flash close-up of a laughing woman's hands, with a sleeve of a mustard knit sweater, dropping one thin translucent white dissolvable detergent sheet (a soft flexible rectangle like the sheet in the reference photo, no print on it) into the open detergent cup of a dishwasher door; the bottom rack is loaded with clean shiny hammered titanium frying pans and a saucepan glinting under the flash, a few water droplets, her blurred smiling face visible at the top right edge. Plastic-free, no plastic pods, no plastic bottles in sight, a linen towel and a wooden brush on the counter. Cozy lived-in home kitchen at night with warm tiles. Direct on-camera flash as the only key light, hard crisp flash shadow on the wall behind the subject, slightly blown highlights on skin and steel, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Email hero composition, horizontal 3:2: all subjects and products sit in the right 55 percent of the frame; the left 40 percent is a calm, dark, low-detail area where the flash falls off into a plain dark wall and an empty counter, so a headline can sit there. Cookware matches the reference photo: bare silver titanium pan, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handle without any engraving, zero coating; never black nonstick cookware. Strictly no text, no letters, no numbers, no logos, no labels on jars, bottles or packaging anywhere in the image.

### m3-hero.jpg

- Drie vrienden ruimen samen af, stapel pannen gaat de vaatwasser in
- Gekozen job: `b45193c1-f0b5-4520-a387-959246cccfb6`
- Afgekeurde variant: `670a1c7e-4efc-4716-a15b-c4069bab97b7`
- Referenties: pan (P04-A)
- Gekozen: meer echte lach, hamerslag goed zichtbaar. Afgekeurd: stijver, minder energie.

Prompt (beide varianten gelijk):

> Candid flash snapshot of three friends in their late 20s and 30s doing the dishes together after a dinner party, cracking up laughing, one in a deep forest green apron loading a stack of shiny hammered titanium frying pans into an open dishwasher, one drying a titanium saucepan with a linen towel, one holding a wine glass and laughing with eyes squeezed shut, aprons are completely plain fabric with plain cream straps over casual knitwear and tees. Dinner leftovers, candles and stacked plates on the counter, lived-in home kitchen at night with wooden shelves crowded with spice jars and plants. Direct on-camera flash as the only key light, hard crisp flash shadow on the wall behind the subject, slightly blown highlights on skin and steel, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Email hero composition, horizontal 3:2: all subjects and products sit in the right 55 percent of the frame; the left 40 percent is a calm, dark, low-detail area where the flash falls off into a plain dark wall and an empty counter, so a headline can sit there. Cookware matches the reference photo: bare silver titanium pan, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handle without any engraving, zero coating; never black nonstick cookware. Strictly no text, no letters, no numbers, no logos, no labels on jars, bottles or packaging anywhere in the image.

### m4-hero.jpg

- Stilleven: doos, pak sheets zonder opdruk, losse vellen en pan op houten aanrecht
- Gekozen job: `0ab791be-ee7a-40a1-b9a1-55abb3c60197`
- Afgekeurde variant: `a50f6c87-71fa-4409-b648-3c3a961803de`
- Referenties: pan (P04-A) + kraft doos (GiftSiraat) + sheet_in_pan
- Gekozen: pak staand zoals het echte pak (wit met okerband, zonder tekst), pan buitenkant glad. Afgekeurd: pak te vierkant, pan buitenkant gehamerd.

Prompt (beide varianten gelijk):

> Calm candid flash still life on a worn wooden kitchen counter at night: a small kraft paper gift box tied with a red satin ribbon bow (like the gift box reference) with its lid slightly lifted, next to it a slim paper sleeve pack of dishwasher detergent sheets that is plain matte white with a solid mustard ochre band across the bottom and absolutely no print or text on it, two thin translucent white detergent sheets fanned out beside it, and a shiny hammered titanium frying pan resting at the back right. Warm direct on-camera flash, hard crisp shadows cast onto the counter and the tiled wall, slightly blown highlights on the steel, warm tungsten glow, 35mm film grain, slight vignette, compact point-and-shoot look, intimate and quiet. Email hero composition, horizontal 3:2: the objects sit in the right 55 percent of the frame; the left 40 percent is calm dark empty wooden counter and dark wall for a headline. Cookware matches the reference photo: bare silver titanium pan, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handle without any engraving, zero coating; never black nonstick cookware. Strictly no text, no letters, no numbers, no logos, no labels on jars, bottles or packaging anywhere in the image.
