# 03 Assets: gift-stack beelden en iconenset

Datum: 2026-10-07. Alleen gelezen in Shopify, Klaviyo-export en asset-register; niets geüpload, niets gecommit.

## 1. Wat er al is

Bronnen doorzocht: `content/assets/index.csv` (5,934 rijen: Shopify Files, Shopify-producten, Drive, Figma), `email-cdn.csv`, Replo `shopify_products_search` (Mystery, E-Book, Purifier, Free Shipping), de oktobercampagnes in `klaviyo/figma/10-oktober-campagnes.js`. De Replo-sitecode (git) en de live PDP waren niet bereikbaar (proxy 403), dus de gift block zelf is niet uitgelezen. De vier gift-producten in Shopify (status ACTIVE, handle `*-sca_clone_freegift`) hebben wel elk een featured image, en dat zijn vrijwel zeker de beelden die de gift block toont.

| Gift | Waarde | Echt beeld | Kwaliteit |
|---|---|---|---|
| Free Shipping | $15 | `free-delivery_c71e7dbb...webp` (512px cartoon doos met "FREE") | off-brand, niet bruikbaar |
| Plastic-Free Home E-Book | $30 | `ChatGPT_Image_1_okt_2025_11_51_42.png` (1024px, cover op crème) | goed, maar titel "The Green Clean Guide" en verhaspelde mini-tekst |
| Mystery Gift | $25 | `GiftSiraat_87ead149...jpg` (612px kraft doos, rood lint op zwart) | schoon, maar laag van resolutie |
| Win a PFAS Water Purifier | $450, 5 winnaars per week | `Water_filter_free.webp` (1254px vrijstaande PNG) | goed |

Waarden: `content/facts/facts.csv` regel 42 en `claims.csv` regel 23 (copy doc okt 2026). $15 + $30 + $25 = $70 gegarandeerd; de Klaviyo-tekst "Over $70 in guaranteed gift value" is dus strikt "$70". Purifier $450 staat ook in de plain-text mail van 10 oktober.

Klaviyo: het gift-stack beeld `7c7cd551...jpeg` (variant A) en `f854ecf3...jpeg` (variant B) zijn byte-identiek: navy blok met vier witte lijn-iconen, geen foto's. Navy is geen merkkleur en er staat een typfout in ("Purifyer").

Overige vondsten in Shopify Files: `free_ebook_siraat.webp` (ad met tekst, niet voor mail), `eguides_5_free` (oude TAIMA-guides, niet van Siraat), `Free_Shipping_Siraat.png` (wit truck-icoon, transparant), `Gift.svg` en `box.svg` (20px UI-iconen).

## 2. Wat ik gemaakt heb

`content/media/gifts/` (zie README daar)
- `sources/`: 20 downloads plus `contact-sheet-sources.jpg`.
- `final/gift-ebook-mockup.png`: hardcover-mockup met PIL uit de bestaande cover; AI-rug met wartekst vervangen door effen rug.
- `final/gift-mystery-cutout.png`: doos vrijgesteld uit de Shopify-foto, plus `gift-mystery-photo-dark.jpg` (origineel vierkant).
- `final/gift-purifier.png`: Shopify-beeld bijgesneden en gecentreerd.
- `final/gift-free-shipping.png`: eigen truck-icoon in brick op crème.
- `final/gift-stack-preview.png`: het hele blok in merkkleuren (600px @2x), als voorbeeld voor C4 en W5.
Alles 1200x1200, transparant en op crème.

`content/media/icons/` (zie README daar): 16 lijn-iconen, SVG en PNG 48 en 96 px, brick en ink, `preview.png`. Scripts om alles opnieuw te bouwen staan in beide mappen.

## 3. Wat nog nodig is

Beslissing van Siraat
- E-book naam: cover zegt "The Green Clean Guide", gift heet "Plastic-Free Home E-Book". Eén naam kiezen. Liefst de echte PDF-cover aanleveren (Drive), dan vervalt AI.

Foto of AI
1. Mystery gift in hoge resolutie en merkkleur (huidige is 612px stock, rood lint). Nodig voor elk gebruik groter dan een tegel.
2. E-book cover zonder verhaspelde tekst. Alleen als er geen echte cover is.
3. Optioneel: purifier in een keukensetting naast een Siraat-pan. De productfoto volstaat voor de stack.

Free shipping heeft geen foto nodig; het icoon is genoeg.

### Higgsfield-prompts (model rendert geen tekst; titel en logo komen daarna in Figma)

Mystery gift
> Studio product photo of a single square gift box wrapped in plain natural kraft paper, tied with a matte brick-red (#AC3B19) satin ribbon and a soft hand-tied bow, three-quarter top view, centred, on a seamless warm cream background (#F8F7F2), soft diffused daylight from the upper left, gentle contact shadow, crisp paper texture, minimal and premium. Plain paper, no text, no letters, no labels, no logo, no tag, no pattern. Square 1:1, high resolution.

E-book cover (blanco, titel later in Figma)
> Front-facing hardcover book standing upright on a seamless warm cream background, soft shadow, the cover is pale sage green with a hand-painted watercolour wreath of olive branches framing simple plastic-free kitchen objects: a glass jar, a wooden brush, a bar of soap, a lemon, a linen cloth. The top third of the cover and the spine are completely empty plain sage green for a title to be added later. No text, no letters, no labels on any object, no logo. Square 1:1, high resolution.

Purifier lifestyle (optioneel)
> The white countertop water purifier from the reference image, unchanged, standing on a light oak kitchen counter next to a hammered titanium frying pan, morning window light, cream wall behind, shallow depth of field, calm and clean. Keep the purifier exactly as in the reference. No text, no labels, no logos, no screens with numbers. 4:5 vertical.
(Referentie: `content/media/gifts/sources/shopify-Water_filter_free.png`.)

## 4. Iconen: aandachtspunten

- Brick op de donkere footer (#282828) is te zwak. Voeg een witte of titanium variant toe als de iconen in de footer komen.
- Iconen bevatten geen cijfers; "30-day", "75-year" en "100,000+" staan in het label.
- Claims die de iconen dragen (75 jaar, 30 dagen, 100,000+, PFAS getest) volgen DECISIONS.md.
