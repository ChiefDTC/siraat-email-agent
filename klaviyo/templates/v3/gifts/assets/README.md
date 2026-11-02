# Gifts-mail: beelden ("your free gifts are here")

Beelden voor de nieuwe bezorgmail met de twee gratis e-books bij elke bestelling. Gemaakt op 2 nov 2026. Niets in Shopify of Klaviyo aangepast. Alles web-geoptimaliseerd, max ~300 KB, retina (2x).

Bronnen:
- Cookbook: `2026-10-31_Siraat-Favorites-Cookbook.pdf` (50 pagina's, 25 recepten). De PDF zelf staat NIET in de repo (te groot), pagina's gerenderd met pdftoppm op 220 dpi.
- E-book: Shopify-product "The Green Clean E-Guide" (handle `e`, id 12292629725524), productfoto 1 (`ChatGPT_Image_1_okt_2025_11_51_42.png`, 1024x1024 mockup op cream). Voorkant eruit gesneden.

| Bestand | Formaat | Grootte | Bron / opmerking |
|---|---|---|---|
| cookbook-cover.jpg | 1200x1552 | 212 KB | PDF pagina 1, schoon |
| cookbook-mockup.png | 1200x1000 | 223 KB | pagina 1 als staand hardcover (perspectief, rug, zachte schaduw) op cream |
| cookbook-spread.jpg | 1200x860 | 155 KB | pagina's 2 (welkom), 16 (Garlic-Butter Ribeye), 29 (Crispy Pizza Night), gewaaierd op cream |
| recipe-garlic-butter-ribeye.jpg | 600x600 | 79 KB | foto pagina 16, zonder hoofdstuklabel |
| recipe-garlic-butter-shrimp.jpg | 600x600 | 87 KB | foto pagina 22, zonder hoofdstuklabel |
| recipe-crispy-pizza-night.jpg | 600x600 | 105 KB | foto pagina 29, zonder hoofdstuklabel |
| ebook-cover.jpg | 600x806 | 95 KB | echte cover uit Shopify (Green Clean Guide), opgeschaald van ~464 px breed |
| ebook-mockup.png | 1200x1000 | 264 KB | echte cover, zelfde hardcover-behandeling op cream |
| duo-hero.png | 1200x900 | 245 KB | cookbook + echte e-book cover op Night #0E0E0E met warme gloed; bovenste ~280 px vrij voor de HTML-kop, geen tekst ingebakken |
| ebook-cover-alt.jpg | 600x776 | 41 KB | PLACEHOLDER: zelf ontworpen cover in cookbook-stijl ("The Plastic-Free Home", eyebrow "THE GREEN CLEAN GUIDE", pil "A FREE E-GUIDE"), zonder logo |
| ebook-mockup-alt.png | 1200x1000 | 173 KB | PLACEHOLDER-cover als hardcover op cream |
| duo-hero-alt.png | 1200x900 | 182 KB | duo-hero met de placeholder-cover |

## Let op (echte e-book cover)
- De Shopify-cover is AI-gegenereerd en heeft rare tekst in de illustratie ("Eoviro cody", onleesbaar flesetiket) en een typfout onderaan ("naturaily"). Op mailformaat klein, maar zichtbaar in de mockup en duo-hero.
- Titel op de cover is "The Green Clean Guide", niet "Plastic-Free Home". Kies vóór gebruik: echte cover (klopt met wat de klant krijgt) of de `-alt` placeholder (mooier, maar dan moet de e-book PDF zelf ook die cover krijgen).
- Bronbestand is maar 1024 px; voor een scherpere cover is het originele ontwerp of de PDF nodig (delivery.shopifyapps.com is via de proxy geblokkeerd).

## Opnieuw maken
`_tools/make.py` (alle beelden) en `_tools/altcover.py` (placeholder-cover). Ze verwachten gerenderde pagina's in `hi/` (pdftoppm -r 220 -png) en de Shopify-foto in `dl/e1.png` naast het script; pas `OUT` zo nodig aan. Draaien met `python3 -I`.

## Afgeleid voor de mail (2 nov 2026)
- `duo-hero-email.jpg` en `duo-hero-alt-email.jpg` (1200x680): duo-hero zonder de lege bovenkant (y 220 tot 900), boven- en onderrand uitgefaded naar Night #0E0E0E zodat er geen naad met het donkere mailvlak is.
- `fb.png`, `ig.png`: kopie uit roasting-int/assets voor de vaste footer; hun CDN-links staan in `klaviyo-urls.txt`. De gift-beelden zelf staan nog niet in Klaviyo (de .klaviyo.html gebruikt `https://upload-pending.invalid/gifts/...`, zie `_tools/render_gifts.py`).
