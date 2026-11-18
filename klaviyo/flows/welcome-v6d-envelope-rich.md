# Welcome v6d · Sealed envelope, rich detail (concept, 17 nov 2026)

Status: **concept**. Niet in een flow; live welcome T4a5Mk niet aangeraakt. Wel 5 code-templates in Klaviyo als TEST (geen testmails verstuurd): E1 XmXWKG, E2 REbgQF, E3 V5LxaR, E4 TPJrVB, E5 Sv56kX (`klaviyo/templates/v3/welcome/v6d-envelope-rich/klaviyo-template-ids.json`).

Waarom: feedback Floris op v6c: te veel vet, en de UX moet op detailniveau beter, met echte productfotografie overal (zoals Smooche, ook armen die het product vasthouden). Copy, aanbod, prijzen (Shopify 17 nov), onderwerpen, previews en HI10-links blijven als v6b/v6c.

- Map: `klaviyo/templates/v3/welcome/v6d-envelope-rich/`. Bouwen: `_tools/make_gif.py` (envelop-GIF), `_tools/sections.py` + `node _tools/render.js` (secties), `_tools/build.py` (mails), `node _tools/shot.js` (renders 600 en 390 px in `renders/`).
- Beelden: `gen/` (Higgsfield en uitsneden), `sections/` (gerenderde secties), Klaviyo-URL's in `klaviyo-urls.txt` (namen v6d-* en v6d-r2-*).
- Figma: oaxnBkz3MAbePRnorCrQwz, All emails, "Row 1h · v6d · Welcome · Rich detail (concept, 17 nov)" (node 342:106), onder v6c.

## Beelden

| Beeld | Hoe | Waar |
| --- | --- | --- |
| Envelop-GIF (verzegeld, handen breken zegel, kaart "10% OFF + 5 FREE GIFTS") | PIL, envelopfoto's, 6 frames, 607 KB; onderschrift met aanbod in elk frame, dus frame 1 zegt al alles (Outlook) | E1 hero |
| Twee armen houden pannen omhoog tegen brick | Higgsfield gpt_image_2_6, Shopify-foto Pan Pro Standard als referentie, geen tekst | E5 aanbod |
| Generieke versleten gecoate pan (zwart, krassen, geen merk) | Higgsfield gpt_image_2_6, studio op zand | E3 vergelijking, met regel "Illustration of a typical worn coated pan. No brand shown." |
| Flash-foto: vrouw schuift een ei uit de pan | Higgsfield, flitsstijl (skill siraat-flash-style), productfoto als referentie, banden zonder tekst | E2 verhaal |
| Flat-lay achtergrond (open kraft doos, linnen) + de echte gift-beelden | Higgsfield (geen tekst) + gift-beelden uit de gift-blokken, uitgesneden | E1 "5 free gifts" |
| Ei voor de schaal | Higgsfield + remove_background | E2 maatlijn |
| Uitsneden Pan Pro Standard, Mini, 6-, 12-delig, 2 Pans + 2 Lids, Roasting Pan | Higgsfield remove_background op Shopify-foto's | kaarten, bundel, anatomie, maatlijn, recap |

Pan-anatomie: labels pure titanium cooking surface, no coating to wear off, hammered texture, works on induction, gas and electric (Shopify-beschrijving). "Stay-cool handle" bewust weggelaten: staat niet in de Shopify-beschrijving en is een verboden claim (skill: never "the handle stays cool"). Maatlijn op schaal (diameters 20, 26, 28, 30 cm; Small en Large gebruiken de Standard-uitsnede op schaal, zelfde ontwerp). Reviews als ontworpen kaarten met initiaal (geen klantfoto's: een gegenereerde foto naast een echte naam zou misleiden).

## Typografie

Zie PLAYBOOK §13 (nieuw, 17 nov). In de beelden: koppen Ramillas Light Italic, tekst Inter 400, labels en knoppen 600, alleen prijzen, code en grote cijfers 800. Live: knoppen Inter 600 15 px ls 1,2 px, tekst 16 tot 17 px regelhoogte ~1,6, hoogstens één vet stuk per alinea.

## Cijfers (17 nov)

| Mail | 600 px | 390 px | Beeldaandeel 390 / 600 | Gewicht |
| --- | --- | --- | --- | --- |
| E1 | 4,934 | 3,725 | 75% / 83% | ~1.25 MB (GIF 607 KB) |
| E2 | 4,350 | 3,324 | 73% / 82% | ~0.7 MB |
| E3 | 4,336 | 3,283 | 77% / 84% | ~0.57 MB |
| E4 | 4,707 | 3,576 | 74% / 82% | ~0.67 MB |
| E5 | 2,762 | 2,417 | 52% / 67% | ~0.3 MB |

Geen overloop, 0 kapotte beelden, 0 gedachtestreepjes. HI10-link getest (E2 maat Small: 302 naar PDP, discount_code=HI10). Beeldaandeel ligt boven de 60 tot 70% uit de v6c-brief, omdat Floris om beeld in elke sectie vroeg; codebox, knoppen, brief en footer blijven live.

## Open vragen

Zoals v6b (HI10 combineert met geen enkele korting: blijven de gifts staan? gifts na BF? $144/$149, $199/$249? compare-at? Trustpilot-score?), plus: is de gegenereerde gecoate pan als illustratie akkoord, en mag de GIF in E1 (607 KB)?
