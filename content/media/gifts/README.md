# Gift-stack beelden (oktober 2026, 4 gifts)

De gift block op de Hammered Pan PDP en de oktobercampagne tonen vier gifts. Waarden komen uit `content/facts/facts.csv` en `claims.csv` (copy doc okt 2026). Volgens DECISIONS.md (2026-10-07): bij de filter altijd "win", nooit "free".

| Gift | Waarde | Shopify-product (gift-app clone) | Beste echte bron | Klaar voor mail |
|---|---|---|---|---|
| Free Shipping | $15 | `free-shipping-sca_clone_freegift` | geen foto; icoon `free-delivery_...webp` (cartoon, off-brand) | `final/gift-free-shipping.png` (eigen truck-icoon, brick op crème) |
| Plastic-Free Home E-Book | $30 | `the-green-clean-e-guide-sca_clone_freegift` | `ChatGPT_Image_1_okt_2025_11_51_42.png` (cover "The Green Clean Guide") | `final/gift-ebook-mockup.png` (PIL-mockup, transparant) |
| Mystery Gift | $25 | `dishwashing-detergent-sheets-fresh-lemon-sca_clone_freegift` | `GiftSiraat_87ead149-...jpg` (kraft doos, rood lint, 612px) | `final/gift-mystery-cutout.png` (vrijstaand, opgeschaald) |
| Win a PFAS Water Purifier | $450, 5 winnaars per week | `entry-to-win-your-order-sca_clone_freegift` | `Water_filter_free.webp` (eigenlijk PNG, vrijstaand, 1254px) | `final/gift-purifier.png` |

Totaal gegarandeerd: $15 + $30 + $25 = $70. Het Klaviyo-blok zegt "Over $70"; strikt is het precies $70.

## Mappen

- `sources/` originele downloads (Shopify CDN en Klaviyo CDN), extensie gecorrigeerd naar het echte formaat. Overzicht: `contact-sheet-sources.jpg`.
- `final/` bewerkte beelden, 1200x1200 (600 @2x). `*.png` transparant, `*-cream.jpg` op crème #F8F7F2. Overzicht: `contact-sheet-final.jpg`.
- `final/gift-stack-preview.png` voorbeeld van het hele blok in merkkleuren (600px @2x). Kop staat in Georgia als placeholder; in de echte mail moet de kop een TT Ramillas PNG zijn (PLAYBOOK).

## Opnieuw bouwen

```
python3 -I build_gifts.py          # e-book mockup, mystery cut-out, purifier
node render_stack.js               # free-shipping tile + stack preview (playwright, chromium /opt/pw-browsers/chromium)
python3 -I make_contact_sheet.py final contact-sheet-final.jpg
```

## Let op

- De e-book cover heet "The Green Clean Guide", het gift heet "Plastic-Free Home E-Book". Siraat moet kiezen welke naam geldt, anders zegt de mail iets anders dan het plaatje.
- De cover is AI-art met verhaspelde mini-tekst op de potjes ("Eaviro cody") en op de rug. De mockup laat de rug weg (effen groen); de potjes blijven klein en zijn op 140px niet leesbaar.
- Het mystery-gift beeld is een stockfoto van 612px (doos zelf ca. 300px). Prima voor een tegel tot ca. 150px breed, te zacht voor een hero. Het rode lint is niet brick.
- Volgens facts.csv is het mystery gift in Shopify een clone van de dishwasher sheets. Toon de doos, niet de sheets, anders is het geen verrassing meer.
- De purifier-afbeelding is de Shopify productfoto. Niet bevestigd dat dit exact het model is dat gewonnen wordt.
- Het oude Klaviyo-blok (`sources/klaviyo-giftstack-A.jpeg`) is navy met witte lijn-iconen en heeft een typfout: "Purifyer".
- Niets is geüpload. Voor gebruik in Klaviyo eerst naar de Klaviyo-bibliotheek of Shopify Files.
