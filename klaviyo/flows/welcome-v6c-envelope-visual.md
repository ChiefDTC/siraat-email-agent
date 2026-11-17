# Welcome v6c · Sealed envelope, visual DR (concept, 17 nov 2026)

Status: **concept**. Niet in Klaviyo als template of flow; live welcome T4a5Mk niet aangeraakt. Tests vanaf 2 dec.

Waarom: feedback Floris op v6b: copy goed, maar de UX en visuele rijkdom van Smooche. v6c gebruikt **dezelfde copy, aanbod, prijzen, onderwerpen, previews en links als v6b** (`welcome-v6b-envelope-dr.md`); alleen de vorm is anders.

- HTML: `klaviyo/templates/v3/welcome/v6c-envelope-visual/` (`e1..e5.html` Klaviyo, `-preview.html`).
- Secties: `_tools/sections.py` (HTML/CSS, TT Ramillas uit klaviyo/fonts + Inter) → `node _tools/render.js` (Playwright, JPG q80, 1200 px; kaarten en maattegels 600 px) → `sections/*.jpg`, Klaviyo-URL's in `klaviyo-urls.txt` (namen v6c-*, herziene versies v6c-r2-*). Mail: `python3 -I _tools/build.py`, renders `node _tools/shot.js`.
- Renders 600 en 390 px (DSF 2): `renders/`.
- Figma: oaxnBkz3MAbePRnorCrQwz, All emails, "Row 1g · v6c · Welcome · Visual DR (concept, 17 nov)" (node 337:106), onder v6b. Renders boven 4000 px in twee slices.

## Visueel

- Hero per mail als één ontworpen beeld: kop in TT Ramillas (150 px op 1200) op crème of donker, envelopfoto full-bleed eronder met zachte overgang, badge "10% OFF + 5 FREE GIFTS" (E1) of "31 PFAS COMPOUNDS TESTED" (E3).
- Torn-paper strips (SVG-pad, 1200 x 56) tussen elk kleurvlak: crème, zand, donker #282828, brick #AC3B19, oranje accent #C4642C.
- Grote cijfers als grafiek: "$293 SAVED" (bundel E1, E3, complete the set E4), "31 / 0 / 75" (E3), "$129.60" (value stack E2), "10% OFF" (recap E5).
- Stappenstrook met grote cijfers (E1), ronde productkaarten en maattegels op zandpanelen (2 per rij, elk een eigen link), vergelijkingstabel, bezwaren in donkere kaarten met oranje rand.
- Live HTML: preheader, codebalk, vaste header, regel onder de hero, gestippelde codebox HI10, hoofdknoppen (rond, wit op donker/brick/oranje, brick op crème), reviews (letterlijk), ondertekening, footer. Elk beeld heeft een beschrijvende alt-tekst met prijzen en is gelinkt met `/discount/HI10?redirect=...` (getest: 302 naar PDP, discount_code=HI10).

## Cijfers (17 nov)

| Mail | 600 px | 390 px | Beeldaandeel 390 / 600 | Gewicht (HTML + beelden) |
| --- | --- | --- | --- | --- |
| E1 | 4,711 | 3,781 | 60% / 71% | ~0.6 MB |
| E2 | 4,478 | 3,618 | 59% / 70% | ~0.56 MB |
| E3 | 4,452 | 3,551 | 63% / 74% | ~0.53 MB |
| E4 | 4,598 | 3,697 | 60% / 71% | ~0.59 MB |
| E5 | 2,011 | 1,911 | 31% / 43% (brief) | ~0.16 MB |

Geen overloop, 0 kapotte beelden, 0 gedachtestreepjes. Elke sectie onder 250 KB. Tekst in beeld minimaal 32 px op 1200 (koppen 92 tot 150 px), dus leesbaar op 390 px. E1 mobiel 3,781 px: iets boven de richtlijn van ~3,700.

## Eerlijkheid

Geen countdown, geen "ends when Black Friday ends" (de gifts zijn niet aantoonbaar aan BF gekoppeld en de reeks start na BF), geen VIP, geen variabel bedrag, geen compare-at. Prijzen Shopify 17 nov (US). Geen Higgsfield-beelden gemaakt: de envelopfoto's en Shopify-productfoto's droegen de secties.

## Open vragen

Zoals v6b (HI10 combineert met geen enkele korting: blijven de gifts staan? Gifts na 30 nov? $144 of $149, $199 of $249? Compare-at? Trustpilot-score?), plus: is het AI-zegel op de envelopfoto's goed genoeg voor livegang?
