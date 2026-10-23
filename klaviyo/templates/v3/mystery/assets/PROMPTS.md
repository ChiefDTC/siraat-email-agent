# Mystery Gift flow: hero-beelden v2 (Higgsfield, 23 oktober 2026)

Status: in de Klaviyo-bibliotheek geupload (alleen beelden), URL's in klaviyo-urls.txt, .klaviyo.html opnieuw gebouwd. Flow en templates niet in Klaviyo. Oude beelden in assets/v1/.

## Waarom opnieuw (Floris: "echt beter")

Zwakke punten van v1, op volle grootte bekeken:

| Mail | Wat zwak was |
| --- | --- |
| m1 | Het product (de strips) is nergens te zien: alleen een lege kraft doos en de pan. De pan is de held, niet de gift. 40% van het beeld is lege donkere ruimte voor een kop die al als live tekst boven het beeld staat, dus op 375 px is alles klein. Vriendin rechts half afgesneden. |
| m2 | Het vel is grijs, gevlekt en doorschijnend (het echte vel is helder wit en mat). Het doseerbakje is een vreemd los kastje. Geen pak in beeld, dus geen herkenning. Gezicht afgesneden, linkerhelft donker en leeg. |
| m3 | Geen strips en geen pak: drie vrienden laden pannen in. Het verhaal van de mail (abonnement, nooit meer zonder) zit niet in het beeld. |
| m4 | Pak is een generieke witte envelop met okerband in de verkeerde verhouding; vellen lijken op vetvrij papier (doorschijnend). Doos domineert. Geen flitslicht, eerder een studiostilleven. |

Algemeen: de v1-prompt vroeg om "translucent white" vellen en om kopruimte links. Beide klopten niet: het echte vel is opaak wit en de kop staat als live tekst boven de foto.

## Werkwijze v2

- Model: `gpt_image_2_5` (flare), quality high, 2k, 3:2 (2048x1360). 2,75 credits per beeld; 5 generaties = 13,75 credits (m3 twee keer).
- Bewerking: midden uitgesneden naar 1200:792, verkleind naar 1200x792 (Lanczos), JPEG q82 progressive, 157 tot 183 KB.
- Stijl: skill siraat-flash-style plus PLAYBOOK 3 (effen schorten, effen creme banden, geen patch, nooit tekst of logo).
- Compositie: product groot en scherp in het midden, geen lege kopruimte.
- Referenties (echte productfoto's uit Shopify, product 15483020443988, read-only opgehaald):
  - pak zonder opdruk: packshot `DishwasherSheets01.webp` met alle tekst en het logo weggepoetst (PIL, horizontale interpolatie), gehost in Klaviyo als `siraat-mystery-ref-pack-blank` (https://cdn.klaviyomail.com/company/TdtTzz/images/9f1b2bfe-ca62-41e1-8732-b6acb57b49fa.jpeg), Higgsfield media `ef188cd6-6e91-4fcd-83d2-080165affb16`.
  - echte vellen: uitsnede zonder tekst uit `dishwashersheetdoseittotheload.webp` (twee handen met witte vellen), Klaviyo `siraat-mystery-ref-sheets-hands` (https://cdn.klaviyomail.com/company/TdtTzz/images/3263eb34-935f-46a3-b5da-88ff1feaaf17.jpeg), Higgsfield media `d4e5d428-5f5b-43e6-9085-1f7a58b27fd1`.
  - kraft doos met rood lint: Higgsfield media `f531ff5b-dab4-49da-b8ef-732a40d16f89` (uit v1).
  - pan: T01 uit `klaviyo/templates/v3/affiliate/PAN-REFERENCE.md`, Higgsfield media `7c79da55-c0f4-4821-a2ee-e6610b83f712`.
- upload.higgsfield.ai blijft geblokkeerd (CONNECT 403); daarom de referenties eerst als beeld in Klaviyo gehost en dan via `media_import_url` geimporteerd.
- Het pak blijft zonder opdruk (PLAYBOOK 3). Herkenning komt uit vorm en kleur: wit pak met okerband, zoals op de productpagina. Echte opdruk kan later in Figma.
- Gezichten zijn verzonnen personen: nooit als klant of review gebruiken.

## Beelden

### m1-hero.jpg (de onthulling)

- Lachende vrouw (oker schort, creme trui) houdt het pak met twee handen omhoog, net uit de kraft doos; deksel met rood lint ernaast, verzenddoos achter haar, vriendin rechts.
- Gekozen: job `2f63945c-19fc-40f2-83c5-dd36175a3282` (poging 1). Referenties: pak + doos.
- Beter: het product is nu de held en groot in beeld; op 375 px direct herkenbaar als het witte pak met de okerband. Handen in orde, geen tekst.

> Candid flash snapshot at a wooden kitchen counter at night: a woman in her early 30s with curly dark hair, wearing an ochre apron over a cream knit sweater, laughing in happy surprise with crinkled eyes and open mouth as she lifts the dishwasher sheets pack up out of a small open kraft paper gift box, holding the pack up toward the camera with both hands at chest height so the pack is big in the frame. The gift box is like the gift box reference: plain kraft paper, its lid with a red satin ribbon bow lying next to it, crinkled kraft paper shred inside. An opened brown cardboard shipping box sits behind her on the counter, a friend at the right edge laughs along, partly cut off. Cozy lived-in home kitchen, wooden shelves with spice jars and plants. The product is the hero and must match the pack reference photo exactly in shape and colour: a slim flat paper envelope pack, matte warm-white paper on the upper two thirds and a solid mustard-ochre band across the bottom third, softly rounded paper edges, about the size of a paperback book. The pack is completely blank: no print, no letters, no logo, no label on it. Direct on-camera flash as the only key light, hard crisp flash shadow on the wall behind, slightly blown highlights on skin, paper and steel, warm tungsten glow in the background, dark night window, 35mm film grain, warm colour cast, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Horizontal 3:2 email photo with tight framing: the pack and sheets are large, sharp and close to the centre of the frame, easy to recognise on a phone screen; no empty copy space. Aprons are completely plain fabric with plain cream straps, no patch. Strictly no text, no letters, no numbers, no logos, no labels on anything in the image.

### m2-hero.jpg (gebruik)

- Hand in mosterdkleurige trui zet een helder wit vel in het doseerbakje, pak ligt op de open deur, gehamerde pannen in het rek.
- Gekozen: job `0a602e77-b03a-4975-8a22-b23b1e3dd874` (poging 1). Referenties: vellen + pak + pan.
- Beter: het vel is wit en mat zoals het echte vel (was grijs), pak in beeld, pannen gehamerd binnen en glad buiten.

> Candid flash close-up at an open dishwasher in a home kitchen at night: a woman's hand with a mustard knit sleeve places one single bright white dishwasher sheet into the open detergent dispenser cup on the inside of the open dishwasher door; the sheet is large, sharp, clearly bright white and in the centre of the frame. The dishwasher sheets pack lies flat on the open dishwasher door right next to the dispenser, front facing up toward the camera. The bottom rack is loaded with two shiny hammered titanium frying pans and plates glinting under the flash, a few water droplets; her blurred smiling face is visible at the top right edge. The dishwasher sheets match the sheet reference photo: bright opaque white, matte, slightly fibrous paper-like rectangles about the size of a playing card with crisp edges; never grey, never translucent, never plastic film, no print on them. The product is the hero and must match the pack reference photo exactly in shape and colour: a slim flat paper envelope pack, matte warm-white paper on the upper two thirds and a solid mustard-ochre band across the bottom third, softly rounded paper edges, about the size of a paperback book. The pack is completely blank: no print, no letters, no logo, no label on it. Any pan is the exact Siraat pan: bright silver frying pan, the inside cooking surface covered in small hand-hammered dimples, the outside completely smooth brushed stainless steel, polished flared rim, long hollow stainless handle with a hanging hole, two round rivets; no coating, no lid, never black nonstick. Direct on-camera flash as the only key light, hard crisp flash shadow on the wall behind, slightly blown highlights on skin, paper and steel, warm tungsten glow in the background, dark night window, 35mm film grain, warm colour cast, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Horizontal 3:2 email photo with tight framing: the pack and sheets are large, sharp and close to the centre of the frame, easy to recognise on a phone screen; no empty copy space. Aprons are completely plain fabric with plain cream straps, no patch. Strictly no text, no letters, no numbers, no logos, no labels on anything in the image.

### m3-hero.jpg (abonnement, nieuwe voorraad)

- Man in navy schort haalt een nieuw pak uit een kraft verzendzakje, tweede nieuw pak en een bijna leeg oud pak op het aanrecht, partner in roestkleurige trui met groen schort lacht met rode wijn, open vaatwasser met pan.
- Gekozen: job `995397f2-2580-46e8-a96b-796d9f8ac933` (poging 2). Afgekeurd: `9c8626a0-08a5-4779-9413-e925ad52bffd` (poging 1: vrouw met blote schouders onder het schort, geen verzendzakje, zwakke flitsschaduw).
- Beter: het beeld vertelt nu de mail (nieuwe pakken komen binnen, oud pak bijna op) in plaats van pannen inladen.

> Candid flash snapshot late at night in a lived-in home kitchen after dinner: a man in his 30s in a navy apron over a grey tee laughs with relief as he pulls a brand-new dishwasher sheets pack out of a small kraft paper mailer envelope that just arrived, holding the pack up near his face toward the camera; on the counter in front of him stands a second identical new pack, and next to it an almost empty, crumpled old pack. Beside him the dishwasher is open and full of dinner plates and a shiny hammered titanium frying pan. His partner, wearing a rust-coloured chunky knit sweater with long sleeves under a deep forest green apron, leans in from the left laughing hard, holding a glass of red wine. A torn-open small kraft paper mailer envelope lies flat on the counter next to the packs. Wooden shelves with spice jars, candles, dark window. The product is the hero and must match the pack reference photo exactly in shape and colour: a slim flat paper envelope pack, matte warm-white paper on the upper two thirds and a solid mustard-ochre band across the bottom third, softly rounded paper edges, about the size of a paperback book. The pack is completely blank: no print, no letters, no logo, no label on it. Any pan is the exact Siraat pan: bright silver frying pan, the inside cooking surface covered in small hand-hammered dimples, the outside completely smooth brushed stainless steel, polished flared rim, long hollow stainless handle with a hanging hole, two round rivets; no coating, no lid, never black nonstick. Harsh direct on-camera flash as the only key light, a hard crisp dark flash shadow outline of both people on the wall right behind them, slightly blown highlights on skin, paper and steel, warm tungsten glow in the background, dark night window, 35mm film grain, warm colour cast, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Horizontal 3:2 email photo with tight framing: the pack and sheets are large, sharp and close to the centre of the frame, easy to recognise on a phone screen; no empty copy space. Aprons are completely plain fabric with plain cream straps, no patch. Strictly no text, no letters, no numbers, no logos, no labels on anything in the image.

### m4-hero.jpg (laatste mail)

- Flitsstilleven: pak rechtop in het midden, drie witte vellen en een gescheurde halve, kraft doos met lint links, pan rechtsachter, linnen doek.
- Gekozen: job `ace95aa4-c36f-4845-8d33-32792e22a4ed` (poging 1). Referenties: pak + vellen + doos + pan.
- Beter: pak in de echte verhouding en groot, vellen opaak wit met de halve sheet uit de copy, harde flitsschaduw achter het pak.

> Candid flash still life on a worn wooden kitchen counter at night, seen from slightly above at about 45 degrees, tight framing: the dishwasher sheets pack stands upright, leaning slightly, large and sharp in the centre of the frame; in front of it three bright white dishwasher sheets are fanned out and one more sheet is torn neatly in half; to the left the small plain kraft paper gift box with its red satin ribbon lid lifted off and resting against it, like the gift box reference; at the back right a shiny hammered titanium frying pan is partly in frame. A linen towel at the edge. Hard direct flash with crisp shadows cast onto the counter and the tiled wall, slightly blown highlights on the paper and the steel, warm tungsten glow, 35mm film grain, slight vignette, compact point-and-shoot look, intimate and quiet. The product is the hero and must match the pack reference photo exactly in shape and colour: a slim flat paper envelope pack, matte warm-white paper on the upper two thirds and a solid mustard-ochre band across the bottom third, softly rounded paper edges, about the size of a paperback book. The pack is completely blank: no print, no letters, no logo, no label on it. The dishwasher sheets match the sheet reference photo: bright opaque white, matte, slightly fibrous paper-like rectangles about the size of a playing card with crisp edges; never grey, never translucent, never plastic film, no print on them. Any pan is the exact Siraat pan: bright silver frying pan, the inside cooking surface covered in small hand-hammered dimples, the outside completely smooth brushed stainless steel, polished flared rim, long hollow stainless handle with a hanging hole, two round rivets; no coating, no lid, never black nonstick. Horizontal 3:2 email photo with tight framing: the pack and sheets are large, sharp and close to the centre of the frame, easy to recognise on a phone screen; no empty copy space. Aprons are completely plain fabric with plain cream straps, no patch. Strictly no text, no letters, no numbers, no logos, no labels on anything in the image.

## Archief v1 (19 oktober 2026, bestanden in assets/v1/)

Status: concept. Niet in Klaviyo geupload. Vervangen de placeholders in deze map.

### Werkwijze

- Model: `gpt_image_2_5` (GPT Image 2.5, variant flare), quality high, resolutie 2k, ratio 3:2 (2048x1360). 2,75 credits per beeld, 8 beelden = 22 credits.
- Bewerking: midden uitgesneden naar 3:2 (1200:792) en verkleind naar 1200x792, JPEG kwaliteit 80 (Pillow). Geen opschaling.
- Stijl: skill siraat-flash-style (directe flits, lachende mensen, woonkeuken 's avonds). Schorten effen met effen creme banden, geen patch, geen tekst (PLAYBOOK 3).
- Referenties via `media_import_url` (upload.higgsfield.ai is geblokkeerd):
  - pan: Shopify CDN `email-hp-square-P04-A_Stovetop_Pan.jpg` (media `d34f4530-45b6-4a80-885b-2b119bd446ac`)
  - kraft doos met rood lint: Shopify CDN `GiftSiraat_87ead149-...jpg` (media `f531ff5b-dab4-49da-b8ef-732a40d16f89`)
  - vel in pan: Shopify CDN `sheet_in_pan.webp` (media `02e1a889-6331-4c20-9b6c-f80b8461027a`)
- Het echte pak (packshot met SIRAAT, Dishwasher Sheets, Up to 60 washes) is bewust niet als referentie gebruikt: het model zou de tekst verhaspelen. In m4 staat het pak zonder opdruk (wit met okerband). Echte packshot later in Figma of als apart blok.
- Alle vier op volle grootte gecontroleerd: geen letters, logo's of etiketten, geen zwarte coating, handen en vingers in orde. Gezichten zijn verzonnen personen: nooit als klant of review gebruiken.

### Beelden

#### m1-hero.jpg

- De reveal: lachende vrouw opent de kraft doos naast een gehamerde pan
- Gekozen job: `59b78b37-566d-4ed3-940e-88d70ae28cb5`
- Afgekeurde variant: `2a76dab8-d326-48f2-96c4-ab216519ea80`
- Referenties: pan (P04-A) + kraft doos (GiftSiraat)
- Gekozen: meer donkere ruimte links, doos in het midden van het beeld, pan rechts. Afgekeurd: pan stond links in de kopruimte.

Prompt (beide varianten gelijk):

> Candid flash snapshot of a woman in her early 30s with curly dark hair, in an ochre apron that is completely plain fabric with plain cream straps over a cream knit sweater, laughing hard with crinkled eyes and open mouth at the moment she lifts the lid off a small kraft paper gift box tied with a red satin ribbon bow (like the gift box reference), at a wooden kitchen counter, a shiny hammered titanium frying pan sits on the counter next to the box. A friend partly cut off at the right edge laughs along. Cozy lived-in home kitchen at night, wooden open shelves with spice jars, plants and cookbooks behind her. Direct on-camera flash as the only key light, hard crisp flash shadow on the wall behind the subject, slightly blown highlights on skin and steel, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Email hero composition, horizontal 3:2: all subjects and products sit in the right 55 percent of the frame; the left 40 percent is a calm, dark, low-detail area where the flash falls off into a plain dark wall and an empty counter, so a headline can sit there. Cookware matches the reference photo: bare silver titanium pan, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handle without any engraving, zero coating; never black nonstick cookware. The gift box is plain kraft paper with only the red ribbon, no tag, no print. Strictly no text, no letters, no numbers, no logos, no labels on jars, bottles or packaging anywhere in the image.

#### m2-hero.jpg

- Hand laat een vaatwasvel in het bakje vallen, gehamerde pannen in het rek
- Gekozen job: `dd91a834-2c36-476a-9429-e3371d600532`
- Afgekeurde variant: `357b30e1-1b9b-4609-b9dd-609c321254ec`
- Referenties: pan (P04-A) + sheet_in_pan
- Gekozen: hamerslag alleen binnenin, buitenkant glad zoals de echte pan. Afgekeurd: pannen ook aan de buitenkant gehamerd. Let op: het vel is grijzig en papierachtig, het echte vel is wit en doorschijnend.

Prompt (beide varianten gelijk):

> Candid flash close-up of a laughing woman's hands, with a sleeve of a mustard knit sweater, dropping one thin translucent white dissolvable detergent sheet (a soft flexible rectangle like the sheet in the reference photo, no print on it) into the open detergent cup of a dishwasher door; the bottom rack is loaded with clean shiny hammered titanium frying pans and a saucepan glinting under the flash, a few water droplets, her blurred smiling face visible at the top right edge. Plastic-free, no plastic pods, no plastic bottles in sight, a linen towel and a wooden brush on the counter. Cozy lived-in home kitchen at night with warm tiles. Direct on-camera flash as the only key light, hard crisp flash shadow on the wall behind the subject, slightly blown highlights on skin and steel, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Email hero composition, horizontal 3:2: all subjects and products sit in the right 55 percent of the frame; the left 40 percent is a calm, dark, low-detail area where the flash falls off into a plain dark wall and an empty counter, so a headline can sit there. Cookware matches the reference photo: bare silver titanium pan, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handle without any engraving, zero coating; never black nonstick cookware. Strictly no text, no letters, no numbers, no logos, no labels on jars, bottles or packaging anywhere in the image.

#### m3-hero.jpg

- Drie vrienden ruimen samen af, stapel pannen gaat de vaatwasser in
- Gekozen job: `b45193c1-f0b5-4520-a387-959246cccfb6`
- Afgekeurde variant: `670a1c7e-4efc-4716-a15b-c4069bab97b7`
- Referenties: pan (P04-A)
- Gekozen: meer echte lach, hamerslag goed zichtbaar. Afgekeurd: stijver, minder energie.

Prompt (beide varianten gelijk):

> Candid flash snapshot of three friends in their late 20s and 30s doing the dishes together after a dinner party, cracking up laughing, one in a deep forest green apron loading a stack of shiny hammered titanium frying pans into an open dishwasher, one drying a titanium saucepan with a linen towel, one holding a wine glass and laughing with eyes squeezed shut, aprons are completely plain fabric with plain cream straps over casual knitwear and tees. Dinner leftovers, candles and stacked plates on the counter, lived-in home kitchen at night with wooden shelves crowded with spice jars and plants. Direct on-camera flash as the only key light, hard crisp flash shadow on the wall behind the subject, slightly blown highlights on skin and steel, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Email hero composition, horizontal 3:2: all subjects and products sit in the right 55 percent of the frame; the left 40 percent is a calm, dark, low-detail area where the flash falls off into a plain dark wall and an empty counter, so a headline can sit there. Cookware matches the reference photo: bare silver titanium pan, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handle without any engraving, zero coating; never black nonstick cookware. Strictly no text, no letters, no numbers, no logos, no labels on jars, bottles or packaging anywhere in the image.

#### m4-hero.jpg

- Stilleven: doos, pak sheets zonder opdruk, losse vellen en pan op houten aanrecht
- Gekozen job: `0ab791be-ee7a-40a1-b9a1-55abb3c60197`
- Afgekeurde variant: `a50f6c87-71fa-4409-b648-3c3a961803de`
- Referenties: pan (P04-A) + kraft doos (GiftSiraat) + sheet_in_pan
- Gekozen: pak staand zoals het echte pak (wit met okerband, zonder tekst), pan buitenkant glad. Afgekeurd: pak te vierkant, pan buitenkant gehamerd.

Prompt (beide varianten gelijk):

> Calm candid flash still life on a worn wooden kitchen counter at night: a small kraft paper gift box tied with a red satin ribbon bow (like the gift box reference) with its lid slightly lifted, next to it a slim paper sleeve pack of dishwasher detergent sheets that is plain matte white with a solid mustard ochre band across the bottom and absolutely no print or text on it, two thin translucent white detergent sheets fanned out beside it, and a shiny hammered titanium frying pan resting at the back right. Warm direct on-camera flash, hard crisp shadows cast onto the counter and the tiled wall, slightly blown highlights on the steel, warm tungsten glow, 35mm film grain, slight vignette, compact point-and-shoot look, intimate and quiet. Email hero composition, horizontal 3:2: the objects sit in the right 55 percent of the frame; the left 40 percent is calm dark empty wooden counter and dark wall for a headline. Cookware matches the reference photo: bare silver titanium pan, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handle without any engraving, zero coating; never black nonstick cookware. Strictly no text, no letters, no numbers, no logos, no labels on jars, bottles or packaging anywhere in the image.