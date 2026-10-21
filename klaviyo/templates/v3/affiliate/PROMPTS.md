# Affiliate/referral (Social Snowball): beelden v2 met pan-referentie (21 oktober 2026)

Status: v2 gegenereerd, verkleind, geupload naar Klaviyo en verwerkt in de `.klaviyo.html`-bestanden (zie `assets/klaviyo-urls.txt`). De v1-beelden staan ter vergelijking in `assets/v1/` (met de oude URL-lijst).

## Waarom v2

Floris vond v1 niet goed genoeg. Problemen v1: hamerslag ook aan de buitenkant van de pan (echte pan is buiten glad), zachtere flits in aff-hero-share, geen kopruimte in aff-hero-dinner. Pan-spec nu vastgelegd in `PAN-REFERENCE.md` (uit Figma "Siraat · Pan reference (baseline)").

## Werkwijze

- Model: `gpt_image_2_5`, quality high, resolutie 2k, 2,75 credits per beeld.
- Credits: 6 generaties x 2,75 = 16,5 (saldo 3166,53 naar 3150,03). Budget was 45. Alleen aff-payout opnieuw gegenereerd (1 keer).
- Referenties (via `media_import_url` met Figma-asset-URL, want upload.higgsfield.ai is geblokkeerd): T01 PDP-packshot (Figma node 2:69, media `7c79da55-c0f4-4821-a2ee-e6610b83f712`) en 13 Pro Duo zijaanzicht (node 2:29, media `e4437585-faac-47f3-8693-b70173f04e66`), beide als `image_references`.
- Stijl: skill siraat-flash-style, harde flits expliciet ("harsh and bright, hard crisp black flash shadow"). Schorten effen met effen creme banden, geen patch, geen tekst (PLAYBOOK 3).
- Bewerking (Pillow, center-crop, LANCZOS, JPEG q82 progressive): 3:2 naar 1200x797, 4:5 naar 960x1200, 1:1 naar 1000x1000. Alles onder 300 KB.
- Upload: `POST /api/image-upload` (multipart). Alle CDN-URLs geven 200.
- Gezichten zijn verzonnen personen: nooit als klant, affiliate of review gebruiken.

## Beelden v2

### aff-hero-share.jpg (3:2, 1200x797, 130 KB)

- Vrouw in mosgroene schort (mosterdtrui) houdt de pan schuin naar de camera, vriendin pakt lachend de greep. Links donkere kopruimte.
- Job: `461505fb-bc92-4cee-81c1-3f63ffe506ba`
- Check tegen referentie: Pan klopt: hamerslag alleen binnen (bodem en onderste wand), buitenkant glad geborsteld, twee klinknagels bij de greep, lange holle greep met ophanggat. Flits nu hard met duidelijke schaduw.
- CDN: https://cdn.klaviyomail.com/company/TdtTzz/images/bc9df2cb-fb28-4f38-ba4a-2e31f7a3929d.jpeg

> Candid flash snapshot at a cozy dinner party at home: a smiling woman in her early 30s with dark wavy hair, wearing a deep forest green apron that is completely plain fabric with plain cream straps, no patch, over a mustard knit sweater, holds out the silver frying pan toward a laughing friend in a navy sweater as if recommending it, tilting it so the hammered inside cooking surface faces the camera, the friend reaches for the long handle and cracks up with crinkled eyes and open mouth. Wine glasses and plates on the counter, lived-in home kitchen at night with wooden open shelves crowded with plain unlabeled spice jars and plants. Direct on-camera flash as the only key light, harsh and bright, hard crisp black flash shadow outline on the wall right behind the subjects, slightly blown highlights on skin and steel, specular flash glint on the pan, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Email hero composition, horizontal 3:2: both people and the pan sit in the right 55 percent of the frame, the pan large and clearly visible; the left 40 percent is a calm, dark, low-detail area where the flash falls off into a plain dark wall, empty space for a headline. The frying pan must be the exact pan from the reference photos (ignore the spatula in the second reference): a bright silver tri-ply stainless frying pan; ONLY the inside cooking surface has small hand-hammered dimples in a fine scale-like pattern on the base and lower inner wall, the upper inner wall is smooth; the OUTSIDE of the pan body is completely smooth brushed stainless steel with NO hammered texture at all; polished thin flared rim; long hollow stainless steel handle with a narrow neck that widens and flattens toward the end and ends in a hanging hole, attached with two small round rivets just below the rim; no lid, no coating, never black nonstick, no engraving, no text and no logo on the pan or handle. Strictly no text, no letters, no numbers, no logos, no patches, no labels, no book spines anywhere in the image.

### aff-hero-dinner.jpg (3:2, 1200x797, 128 KB)

- Man in okerschort schept pasta en geroosterde groente uit de pan op borden van twee lachende vrienden. Linker 40 procent bijna zwart: kopruimte.
- Job: `ebae8b39-d6c7-40ab-8595-578dfd7c9076`
- Check tegen referentie: Pan klopt: glad buiten, hamerslag binnen, klinknagels op de juiste plek. Uiteinde greep valt in de hand (ophanggat niet zichtbaar).
- CDN: https://cdn.klaviyomail.com/company/TdtTzz/images/2415da14-a0cf-4937-8a17-755db43c2b86.jpeg

> Candid flash snapshot of three friends in their late 20s and 30s around a wooden home kitchen island at night, laughing hard: a man in an ochre apron that is completely plain fabric with plain cream straps, no patch, over a grey tee, serves golden roasted vegetables and pasta straight from the silver frying pan onto plates, the pan held up at chest height toward the camera so its smooth silver outside, polished rim and long riveted handle are clearly visible, two friends hold out ceramic plates, one woman throws her head back laughing. Wine glasses and a rustic sourdough loaf on the island. Direct on-camera flash as the only key light, harsh and bright, hard crisp black flash shadow outline on the wall right behind the subjects, slightly blown highlights on skin and steel, specular flash glint on the pan, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Email hero composition, horizontal 3:2: all three people and the pan are grouped in the right 55 percent of the frame; the left 40 percent of the frame is a dark, almost black, empty area (unlit plain dark wall and shadow, no objects, no shelves, no windows) as copy space for a headline. The frying pan must be the exact pan from the reference photos (ignore the spatula in the second reference): a bright silver tri-ply stainless frying pan; ONLY the inside cooking surface has small hand-hammered dimples in a fine scale-like pattern on the base and lower inner wall, the upper inner wall is smooth; the OUTSIDE of the pan body is completely smooth brushed stainless steel with NO hammered texture at all; polished thin flared rim; long hollow stainless steel handle with a narrow neck that widens and flattens toward the end and ends in a hanging hole, attached with two small round rivets just below the rim; no lid, no coating, never black nonstick, no engraving, no text and no logo on the pan or handle. Strictly no text, no letters, no numbers, no logos, no patches, no labels, no book spines anywhere in the image.

### aff-sale.jpg (4:5, 960x1200, 183 KB)

- Man in navy schort lacht naar zijn telefoon (scherm weg van camera) en houdt de pan met steak op het gasfornuis vast.
- Job: `c4d044a5-e5a6-4727-88f5-86c74f4b9b2c`
- Check tegen referentie: Pan klopt: groot in beeld, hamerslag binnen rond de steak, gladde buitenkant, twee klinknagels, greep correct.
- CDN: https://cdn.klaviyomail.com/company/TdtTzz/images/0995830d-e6d3-415f-9cc4-1ec9888f0d9b.jpeg

> Candid flash snapshot of a man in his early 30s with a short beard, wearing a navy apron that is completely plain fabric with plain cream straps, no patch, over a cream knit sweater, standing at a home stove at night and laughing with delight while looking down at his phone in one hand, the phone screen faces away from the camera; with his other hand he holds the long handle of the silver frying pan on the stove, the pan in the foreground with seared steak and a little steam, the hammered inside cooking surface visible around the food and the smooth outside clearly visible. Lived-in home kitchen, wooden open shelves with plain unlabeled glass jars and trailing plants, warm tiles. Direct on-camera flash as the only key light, harsh and bright, hard crisp black flash shadow outline on the wall right behind the subjects, slightly blown highlights on skin and steel, specular flash glint on the pan, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Vertical 4:5. The frying pan must be the exact pan from the reference photos (ignore the spatula in the second reference): a bright silver tri-ply stainless frying pan; ONLY the inside cooking surface has small hand-hammered dimples in a fine scale-like pattern on the base and lower inner wall, the upper inner wall is smooth; the OUTSIDE of the pan body is completely smooth brushed stainless steel with NO hammered texture at all; polished thin flared rim; long hollow stainless steel handle with a narrow neck that widens and flattens toward the end and ends in a hanging hole, attached with two small round rivets just below the rim; no lid, no coating, never black nonstick, no engraving, no text and no logo on the pan or handle. Strictly no text, no letters, no numbers, no logos, no patches, no labels, no book spines anywhere in the image.

### aff-payout.jpg (4:5, 960x1200, 221 KB)

- Twee vrienden (mosgroene en okerschort) proosten; op tafel vooraan de pan met kip en citroen, greep naar rechts.
- Job: `b3a80678-e83f-47f0-a2c9-718ddc50f12a`
- Eerste poging: `1690e727-c156-4bd9-9e32-492327576974 (afgekeurd: greep vooraan maar klinknagels op de achterwand, fysiek onjuist; man in navy trui)`
- Check tegen referentie: Pan klopt: klinknagels nu op de wand waar de greep vastzit, hamerslag binnen, gladde buitenkant.
- CDN: https://cdn.klaviyomail.com/company/TdtTzz/images/6809ff05-b55f-4e24-bd39-8f61c6e3574d.jpeg

> Candid flash snapshot of two friends in their late 20s and 30s clinking wine glasses over a home-cooked dinner, both laughing hard, a woman in a deep forest green apron over a mustard sweater and a man in an ochre apron, aprons completely plain fabric with plain cream straps, no patch, over casual knitwear. On the wooden table in the foreground, large and sharp, one silver frying pan with golden roast chicken thighs and lemons, seen from a three-quarter angle with its long handle pointing to the right side of the frame, the two round rivets visible on the inside wall exactly where the handle joins the pan and nowhere else, smooth silver outside and polished rim clearly visible, candles and bread beside it. Lived-in home kitchen at night behind them with wooden shelves and plants. Direct on-camera flash as the only key light, harsh and bright, hard crisp black flash shadow outline on the wall right behind the subjects, slightly blown highlights on skin and steel, specular flash glint on the pan, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Vertical 4:5, celebration mood. The frying pan must be the exact pan from the reference photos (ignore the spatula in the second reference): a bright silver tri-ply stainless frying pan; ONLY the inside cooking surface has small hand-hammered dimples in a fine scale-like pattern on the base and lower inner wall, the upper inner wall is smooth; the OUTSIDE of the pan body is completely smooth brushed stainless steel with NO hammered texture at all; polished thin flared rim; long hollow stainless steel handle with a narrow neck that widens and flattens toward the end and ends in a hanging hole, attached with two small round rivets just below the rim; no lid, no coating, never black nonstick, no engraving, no text and no logo on the pan or handle. Strictly no text, no letters, no numbers, no logos, no patches, no labels, no book spines anywhere in the image.

### aff-block.jpg (1:1, 1000x1000, 170 KB)

- Close-up: vrouw in mosterdtrui en mosgroene schort geeft de lege pan aan open handen (navy mouw), hamerslag binnen vol in beeld.
- Job: `2ae7f758-01f1-4f50-9c66-6c4a50db0e9a`
- Check tegen referentie: Pan klopt het best van de vijf: hamerslag, gladde binnenwand bovenin, klinknagels, greep met ophanggat. Kleine vage vlek op de greep onder de duim, geen leesbare tekst. Handen in orde.
- CDN: https://cdn.klaviyomail.com/company/TdtTzz/images/fe8529dd-9c21-48be-9113-18a3ff6eceb0.jpeg

> Candid flash close-up across a worn wooden kitchen counter: one person's hands, sleeve of a mustard knit sweater, pass the empty silver frying pan by its long handle to another person's open hands, sleeve of a navy sweater, the pan tilted toward the camera so the hammered dimpled inside cooking surface, the two rivets and the hanging hole at the end of the handle are clearly visible, the smooth outside wall visible at the edge; a plain forest green apron edge with a plain cream strap visible, a blurred laughing face at the top edge of the frame. A wooden spoon and a small bowl of herbs on the counter. Direct on-camera flash as the only key light, harsh and bright, hard crisp black flash shadow outline on the wall right behind the subjects, slightly blown highlights on skin and steel, specular flash glint on the pan, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Square 1:1. Anatomically correct hands with five fingers each. The frying pan must be the exact pan from the reference photos (ignore the spatula in the second reference): a bright silver tri-ply stainless frying pan; ONLY the inside cooking surface has small hand-hammered dimples in a fine scale-like pattern on the base and lower inner wall, the upper inner wall is smooth; the OUTSIDE of the pan body is completely smooth brushed stainless steel with NO hammered texture at all; polished thin flared rim; long hollow stainless steel handle with a narrow neck that widens and flattens toward the end and ends in a hanging hole, attached with two small round rivets just below the rim; no lid, no coating, never black nonstick, no engraving, no text and no logo on the pan or handle. Strictly no text, no letters, no numbers, no logos, no patches, no labels, no book spines anywhere in the image.

---

## Archief v1 (vervangen)

Status: gegenereerd, verkleind en geupload naar Klaviyo (zie `assets/klaviyo-urls.txt`). Niet gecommit.

##### Werkwijze

- Model: `gpt_image_2_5` (GPT Image 2.5), quality high, resolutie 2k. 2,75 credits per beeld.
- Credits: 6 generaties x 2,75 = 16,5 credits (saldo 3183,03 naar 3166,53). Budget was 40.
- Referentie: pan P04-A (Shopify CDN `email-hp-square-P04-A_Stovetop_Pan.jpg`, media `d34f4530-45b6-4a80-885b-2b119bd446ac`, hergebruikt uit mystery) als `image_references`.
- Stijl: skill siraat-flash-style. Schorten effen met effen creme banden, geen patch, geen tekst (PLAYBOOK 3 gaat voor op "logo-print straps" uit de skill: het model verhaspelt opdruk).
- Bewerking (Pillow, LANCZOS, JPEG kwaliteit 82, progressive): 3:2 naar 1200x797, 4:5 naar 960x1200, 1:1 naar 1000x1000. Alle bestanden onder 300 KB.
- Upload: `POST /api/image-upload` (multipart) in Klaviyo. Alle CDN-URLs geven 200.
- Gezichten zijn verzonnen personen: nooit als klant, affiliate of review gebruiken.

##### Beelden

###### aff-hero-share.jpg (3:2, 1200x797, 148 KB)

- Vrouw in groene schort geeft gehamerde pan aan lachende vriendin, links donkere kopruimte
- Job: `022021c3-8ca9-44bc-8764-4178582f0e37`
- Opmerking: flits iets zachter dan de rest (meer kaarslicht), harde flitsschaduw beperkt. Kopruimte links is goed donker.

> Candid flash snapshot at a cozy dinner party at home: a smiling woman in her early 30s with dark wavy hair, wearing a deep forest green apron that is completely plain fabric with plain cream straps over a mustard knit sweater, warmly hands a shiny hammered titanium frying pan to a laughing friend in a navy sweater, as if she is recommending it, the friend reaches for the handle and cracks up with crinkled eyes and open mouth. Candles, wine glasses and plates on the counter, lived-in home kitchen at night with wooden open shelves crowded with spice jars, plants and cookbooks. Direct on-camera flash as the only key light, hard crisp flash shadow on the wall behind the subjects, slightly blown highlights on skin and steel, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment. Email hero composition, horizontal 3:2: both people and the pan sit in the right 55 percent of the frame; the left 40 percent is a calm, dark, low-detail area where the flash falls off into a plain dark wall, so a headline can sit there. Cookware matches the reference photo: bare silver titanium pan, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handle without any engraving, zero coating; never black nonstick cookware. Strictly no text, no letters, no numbers, no logos, no patches, no labels on jars, bottles or packaging anywhere in the image.

###### aff-hero-dinner.jpg (3:2, 1200x797, 173 KB)

- Drie vrienden aan het kookeiland, man in okerschort schept op uit de pan, anderen houden borden op
- Job: `1ab65ea3-6dc6-40a0-b542-b0d61cba941e`
- Opmerking: geen echte kopruimte (vol beeld); geschikt als beeld zonder tekst eroverheen. Pan ook aan de buitenkant gehamerd.

> Candid flash snapshot of three friends in their late 20s and 30s around a wooden home kitchen island, celebrating and laughing hard, one man in an ochre apron that is completely plain fabric with plain cream straps over a grey tee is serving golden roasted vegetables and pasta straight from a shiny hammered titanium frying pan onto plates, two friends hold out ceramic plates, one woman throws her head back laughing with eyes squeezed shut, the other grins with her mouth open. Wine glasses, a rustic sourdough loaf and a salad bowl on the island, lived-in home kitchen at night with wooden shelves crowded with spice jars and plants. Direct on-camera flash as the only key light, hard crisp flash shadow on the wall behind the subjects, slightly blown highlights on skin and steel, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed party-photo energy. Horizontal 3:2, subjects slightly right of center with darker falloff on the left side. Cookware matches the reference photo: bare silver titanium pan, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handle without any engraving, zero coating; never black nonstick cookware. Strictly no text, no letters, no numbers, no logos, no patches, no labels on jars, bottles or packaging anywhere in the image.

###### aff-sale.jpg (4:5, 960x1200, 190 KB)

- Man in navy schort lacht naar zijn telefoon (scherm niet zichtbaar), pan met steak dampt op het fornuis
- Gekozen job (tweede poging): `88701878-ae45-46ca-8e60-c79d69339465`
- Afgekeurd: `ea51d205-2165-4292-846f-8768c27196c4` (boekruggen en een potetiket met nepletters op volle grootte)
- Opmerking: hand rust vlak naast de kookplaat; pan buitenkant gehamerd.

> Candid flash snapshot of a man in his early 30s with a short beard, wearing a navy apron that is completely plain fabric with plain cream straps over a cream knit sweater, leaning on the kitchen counter and laughing with delight while looking down at his phone in one hand; the phone screen faces away from the camera so no screen content is visible. Behind him a shiny hammered titanium frying pan sits on the stove with a little steam rising. Cozy lived-in home kitchen at night, wooden open shelves with plain unlabeled glass jars of spices and dried pasta, trailing plants, ceramic bowls, warm tiles, no books. Direct on-camera flash as the only key light, hard crisp flash shadow on the wall behind him, slightly blown highlights on skin and steel, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, genuine unposed moment, vertical 4:5. Cookware matches the reference photo: bare silver titanium pan, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handle without any engraving, zero coating; never black nonstick cookware. Strictly no text, no letters, no numbers, no logos, no patches, no readable screen, no book spines, no labels on jars, bottles or packaging anywhere in the image.

###### aff-payout.jpg (4:5, 960x1200, 267 KB)

- Twee vrienden (groene en okerschort) proosten boven twee gehamerde pannen met kip en pasta
- Job: `0c8e03d6-cf7e-4a0a-8f1f-210c08cc283b`

> Candid flash snapshot of two friends in their late 20s and 30s clinking wine glasses over a home-cooked dinner, both laughing hard, a woman in a deep forest green apron and a man in an ochre apron, aprons are completely plain fabric with plain cream straps over casual knitwear. On the wooden table between them two shiny hammered titanium frying pans full of food: golden roast chicken with lemons and herby pasta, candles, bread, a salad bowl. Lived-in home kitchen at night behind them with wooden shelves crowded with spice jars and plants. Direct on-camera flash as the only key light, hard crisp flash shadow on the wall behind the subjects, slightly blown highlights on skin, glass and steel, warm tungsten glow in the background, dark night window, 35mm film grain, deep blacks at the frame edges, slight vignette, imperfect amateur framing, shot on a compact point-and-shoot camera, celebration mood, genuine unposed moment, vertical 4:5. Cookware matches the reference photo: bare silver titanium pans, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handles without any engraving, zero coating; never black nonstick cookware. Strictly no text, no letters, no numbers, no logos, no patches, no labels on bottles or packaging anywhere in the image.

###### aff-block.jpg (1:1, 1000x1000, 192 KB)

- Close-up: handen geven de pan door over een houten aanrecht, lachende mond bovenin beeld
- Job: `135301f0-a96e-4d8e-aced-371b8637cddc`
- Opmerking: hamerslag alleen binnenin, buitenkant glad (klopt met het echte product). Handen in orde.

> Candid flash close-up across a worn wooden kitchen counter: one person's hands, with the sleeve of a mustard knit sweater, pass a shiny hammered titanium frying pan by its handle to another person's open hands, sleeve of a navy sweater, the edge of a plain forest green apron with a plain cream strap visible, a blurred laughing face at the top edge of the frame. A wooden spoon, a small bowl of herbs and a linen towel on the counter. Cozy home kitchen at night. Warm direct on-camera flash as the only key light, hard crisp shadows cast onto the counter, slightly blown highlights on the steel and skin, warm tungsten glow in the background, 35mm film grain, deep blacks at the frame edges, slight vignette, compact point-and-shoot look, square 1:1. Cookware matches the reference photo: bare silver titanium pan, the hammered dimple texture is on the inside cooking surface, smooth polished silver exterior, plain riveted steel handle without any engraving, zero coating; never black nonstick cookware. Anatomically correct hands with five fingers each. Strictly no text, no letters, no numbers, no logos, no patches, no labels anywhere in the image.
