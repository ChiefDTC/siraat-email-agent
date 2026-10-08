# Beeldcontrole v5 (onafhankelijke controle)

Datum: 2026-10-08. Gecontroleerd: de 16 beelden `content/media/ai-flash/*-v5.jpg` uit `research/v5/05-beeld-vervangingen.csv`.
Referentie: `content/products/titanium-hammered-pan-pro/img/packshot-1..3.jpg`, `titanium-hammered-crepe-pan-pro/img/packshot-1.jpg`, `titanium-hammered-cookware-set/img/packshot-1.jpg` (steelpannen, kookpan met twee oororen, deksels), `stainless-steel-lid/img/packshot-1.jpg`.
Methode: elk beeld volledig bekeken plus vergrote uitsneden van pan, handvat, handen en gezichten (`/tmp/claude-0/verify/`).

Criteria: 1 hamerslag alleen binnen, 2 buitenkant glad, 3 handvat recht, 1 stuk, 2 klinknagels, niet vervormd, 4 juiste panvorm, 5 handen/vingers/gezichten natuurlijk, 6 geen verminkte tekst of logo, 7 geen coating of zwart oppervlak, 8 flash-stijl.

Algemene opmerking: in alle beelden is de hamerslag een regelmatig hexagon-raster, scherper en regelmatiger dan de onregelmatige "kiezel"-hamerslag op de packshots, en loopt hij vaak tot vlak onder de rand (packshot: bovenste band van de wand glad). Dat valt binnen "hexagon-achtige hamerslag" en is niet als afkeurreden gebruikt. Er staat nergens een merktekst of logo op de pannen (het monogram op het handvat ontbreekt overal), dus ook niets verminkt.

## Samenvatting

| Beeld | Mail(s) | Oordeel |
|---|---|---|
| pan-trophy-1x1-v5 | p1-first | GOED |
| friends-greeting-1x1-v5 | p1-repeat | GOED |
| egg-plate-1x1-v5 | p2 | AFGEKEURD |
| lid-steam-1x1-v5 | p3-pan, p3-pan-nocode | GOED |
| pan-reflection-1x1-v5 | p3-accessory, p3-accessory-nocode | GOED |
| crepe-flip-1x1-v5 | p3-set, p3-set-nocode | GOED |
| full-stove-1x1-v5 | r1-set | GOED |
| egg-slide-4x3-v5 | b2-clicked, b2-clicked-nocode | GOED |
| sauce-taste-4x3-v5 | b2-notclicked | GOED |
| pan-microphone-4x3-v5 | k2-new | AFGEKEURD |
| olive-oil-4x3-v5 | c2 | GOED |
| three-pans-4x3-v5 | c3-p | AFGEKEURD |
| steak-sear-4x3-v5 | k3, k3-nocode | GOED |
| egg-crack-1x1-v5 | w0 | GOED |
| two-sizes-1x1-v5 | w4-int | GOED |
| pasta-lift-1x1-v5 | w4-us | GOED |

Totaal: 13 GOED, 3 AFGEKEURD, 0 TWIJFEL.

## Detail per beeld

| Beeld | 1 hamer binnen | 2 buiten glad | 3 handvat | 4 vorm | 5 handen/gezichten | 6 tekst/logo | 7 geen coating | 8 flash | Oordeel en toelichting |
|---|---|---|---|---|---|---|---|---|---|
| pan-trophy-1x1-v5 | ja | ja | ja (recht, 2 klinknagels binnen zichtbaar) | ja, koekenpan | ja | ja | ja | ja | GOED. Pan als trofee omhoog, beide gezichten en handen natuurlijk. |
| friends-greeting-1x1-v5 | n.v.t. (binnenkant vol soep) | ja | ja (lang recht handvat, klinknagels bij de rand) | ja, steelpan uit de set | ja (open hand, hand om brood) | ja | ja | ja | GOED. Toont geen hamerslag; het product is een steelpan, geen koekenpan. Bewust kiezen of dat past bij p1-repeat. |
| egg-plate-1x1-v5 | ja | ja | **nee** | ja, koekenpan | twijfel (pols sterk geknikt) | ja | ja | ja | **AFGEKEURD.** De pan heeft geen handvat: twee klinknagels zichtbaar, maar de man pakt de pan bij de rand vast en voorbij zijn vuist komt geen handvat tevoorschijn. Een klant ziet een pan zonder steel. |
| lid-steam-1x1-v5 | ja | ja | ja (2 klinknagels) | ja, koekenpan met RVS deksel | ja | ja | ja | ja | GOED. Deksel volledig RVS met RVS knop, past bij de setfoto. Kleine kanttekening: het deksel oogt iets kleiner dan de pandiameter, valt door perspectief nauwelijks op. |
| pan-reflection-1x1-v5 | ja | ja | ja (hand om handvat, klinknagels bij aanzet) | ja, koekenpan | ja | ja | ja | ja | GOED. Spiegelbeeld van het gezicht in de hamerslag is speels; de hoek van de reflectie is niet helemaal natuurkundig, maar een klant leest het als grap. |
| crepe-flip-1x1-v5 | ja | ja | ja (recht, aanzet met klinknagel) | ja, platte crêpepan met lage rand | ja (handen om bord en handvat natuurlijk) | ja | ja | ja | GOED. Panvorm klopt met de crêpepan-packshot. De crêpe in de lucht is kanten (crêpe dentelle), iets grillig maar geloofwaardig. |
| full-stove-1x1-v5 | ja | ja | ja (steelpan en koekenpannen 2 klinknagels; kookpan twee oororen zoals in de set) | ja, kookpan, steelpan, 3 koekenpannen | ja | ja | ja | ja | GOED. Volledige set op het fornuis, consistent met de set-packshot. |
| egg-slide-4x3-v5 | ja | ja | ja (2 klinknagels, recht) | ja, koekenpan | ja (hand om wijnglas natuurlijk) | ja | ja | ja | GOED. |
| sauce-taste-4x3-v5 | ja | ja | ja (2 klinknagels) | ja, diepe pan | ja (vingers aan beeldrand afgesneden, natuurlijk) | ja | ja | ja | GOED. Saus op lip en wang hoort bij het moment. |
| pan-microphone-4x3-v5 | n.v.t. (binnenkant niet zichtbaar) | ja | **nee** | **nee** | ja | ja | ja | ja | **AFGEKEURD.** Bij beide steelpannen zit het handvat vast aan de onderrand/bodem van de pan met één beugel en één klinknagel, in plaats van hoog op de wand vlak onder de rand met twee klinknagels (zie steelpan in de set-packshot en in full-stove). Productvorm klopt niet. |
| olive-oil-4x3-v5 | ja | ja | ja (beide pannen 2 klinknagels) | ja, koekenpannen | ja (hand om fles, hand om handvat, hand met spatel) | ja | ja | ja | GOED. |
| three-pans-4x3-v5 | ja | ja | **nee** | twijfel | ja | ja | ja | ja | **AFGEKEURD.** Handvatten zijn met één bout/beugel laag aan de buitenwand bevestigd (niet de gegoten Y-aanzet met twee klinknagels), en de binnenklinknagels staan op de achter- en zijwand, niet waar het handvat zit. De pannen ogen als sauteuses van een ander merk. Deksels leunen schuin tegen de pannen, oogt onnatuurlijk. |
| steak-sear-4x3-v5 | ja | ja | ja (2 klinknagels, recht) | ja, koekenpan | ja (hand om handvat en wijnglas natuurlijk) | ja | ja | ja | GOED. |
| egg-crack-1x1-v5 | ja | ja | ja (2 klinknagels, recht) | ja, koekenpan | ja (vingers bij ei natuurlijk) | ja | ja | ja | GOED. Kanttekening: er ligt al een gebakken ei in de pan terwijl ze een tweede ei breekt waarvan alleen eiwit druppelt; logisch net-niet, maar geen productfout. |
| two-sizes-1x1-v5 | ja | ja (onderkant niet in beeld, wand glad) | ja (beide 2 klinknagels, recht) | ja, twee formaten koekenpan | ja (wijzende hand acceptabel) | ja | ja | ja | GOED. |
| pasta-lift-1x1-v5 | ja | ja | ja (2 klinknagels, recht) | ja, koekenpan | ja (hand om tang, handen om bord) | ja | ja | ja | GOED. |

## Advies

- Opnieuw genereren: `egg-plate` (pan met volledig handvat, bij het handvat vastgehouden), `pan-microphone` (handvat hoog op de wand met twee klinknagels, zoals de steelpan uit de set), `three-pans` (koekenpannen zoals packshot, Y-handvat met twee klinknagels aan de binnenkant op de plek van het handvat; deksels los ernaast of in de hand).
- De kolom `controle` in `05-beeld-vervangingen.csv` staat voor alle 16 op `ok`; voor deze drie klopt dat niet. Niet door mij aangepast.
