# Klaviyo flows · Siraat's Kitchen

Nieuwe flow-opzet uit de Klaviyo-audit van 6 oktober 2026. Negen flows, 35 e-mails, één sms.
Elke flow heeft een spec met trigger, filters, vertakking en timing in `flows/`, en per e-mail
een Klaviyo-klaar HTML-voorbeeld in `emails/`.

Open `index.html` in een browser om alle flows met vertakking en mailvoorbeelden naast elkaar te zien.

## Flows

| # | Flow | Vervangt | Mails | Incentive |
| --- | --- | --- | --- | --- |
| 01 | [Welcome](flows/01-welcome.md) | Welcome Flow 02.03.26 | 5 | HI10, 10%, 7 dagen |
| 02 | [Checkout Abandonment](flows/02-checkout-abandonment.md) | Checkout Abandonment + Triple Pixel | 4 per tak + sms | A/B: GIFT25 ($25) vs CHECKOUT10 (10%) |
| 03 | [Cart Abandonment](flows/03-cart-abandonment.md) | Cart Abandonment + Triple Pixel | 4 | COOK10, 10%, 48 uur |
| 04 | [Browse Abandonment](flows/04-browse-abandonment.md) | Browse Abandonment + Triple Pixel | 2 | Geen |
| 05 | [Failure to launch](flows/05-failure-to-launch.md) | Failure to launch (10 mails) | 3 | Geen |
| 06 | [Sunset](flows/06-sunset.md) | Sunset Flow | 2 + unsubscribe-actie | Geen |
| 07 | [Post Purchase](flows/07-post-purchase.md) | Post Purchase Flow 4/6/2026 | 4 + 1 repeat | JAN25 / JAN50 next-purchase card (holiday-tak) |
| 08 | [Winback](flows/08-winback.md) | Customer Winback | 3 | WINBACK10, 10%, 5 dagen |
| 09 | [Gift Card](flows/09-gift-card.md) | EB - E-Gift Card | 2 flow + 3 campagnes | Geen |

## Kortingscodes die in Klaviyo moeten bestaan (unieke codes, Klaviyo coupon sets)

| Code-set | Type | Geldigheid | Minimum | Gebruikt in |
| --- | --- | --- | --- | --- |
| HI10 | 10% | 7 dagen na aanmaak | geen | Welcome |
| GIFT25 | $25 vast | 72 uur | $99 | Checkout tak A |
| CHECKOUT10 | 10% | 72 uur | geen | Checkout tak B |
| COOK10 | 10% | 48 uur | geen | Cart |
| JAN25 / JAN50 | $25 / $50 vast | 1 tot 15 januari | $99 | Post Purchase holiday-tak |
| WINBACK10 | 10% | 5 dagen | geen | Winback |

## Klaviyo-variabelen in de HTML

- `{{ first_name|default:'there' }}` overal met default, nooit zonder.
- `{% coupon_code 'NAAM' %}` voor unieke codes.
- Checkout Started en Placed Order: `event.extra.line_items`, `event.extra.checkout_url`, `event.extra.order_status_url`.
- Added to Cart en Viewed Product: `event.ProductName`, `event.ImageURL`, `event.URL`.
- `{{ unsubscribe_link }}`, `{{ manage_preferences_link }}`, `{{ organization.name }}`, `{{ organization.full_address }}`.

De grijze productblokken in de bestsellers-mails zijn placeholders; vervang ze in Klaviyo door
productafbeeldingen of een product feed-blok. De reviewquotes zijn voorbeeldteksten, vervang ze door
echte Loox- of Trustpilot-reviews voordat je verstuurt.

## Opnieuw genereren

```
python3 klaviyo/build.py
```

Alle teksten, onderwerpen, timings en filters staan in `build.py` onder `FLOWS`. Pas daar aan en
draai het script opnieuw; de markdown-specs, HTML-mails en `index.html` worden overschreven.

## Figma

Bestand: https://www.figma.com/design/K8qNiZ7OEThlRrUXH7QImi (team Siraats Kitchen, Professional plan, Full seat).

- Pagina 1: negen secties, een per flow, met de 35 mails als 600px-frames plus een meta-strook (onderwerp, preview, timing, filters) boven elke mail.
- Pagina 2 "Oktober campagnes (drafts)": de Klaviyo-drafts van Homestead uit `campaigns/oct-drafts.json`.
- Stijl: Homestead "SIRAAT – Client Review 2026" (achtergrond #2B2929, tekst #F2F2F2, TT Ramillas Trl Light It voor koppen, Inter Bold uppercase +5% voor navigatie). TT Ramillas staat niet in Figma's bibliotheek; de scripts vallen terug op Instrument Serif Italic tot het font lokaal is geïnstalleerd.
- `figma_js.py` genereert `figma/*.js`; elk script bouwt een sectie opnieuw (verwijdert eerst de oude met dezelfde naam) via de Figma MCP `use_figma`. Afbeeldingen worden daarna met `upload_assets` op de `IMG`-frames gezet (zie de session-scratch scripts; vereist netwerktoegang tot cdn.shopify.com, d3k81ch9hvuctc.cloudfront.net, cdn.klaviyomail.com en mcp.figma.com).

## Design system (Figma, oktober 2026)

Bestand K8qNiZ7OEThlRrUXH7QImi, pagina's `00 Foundations`, `01 Components`, `02 Samples`.

- Tokens: crème #F8F7F2 (basis), paper #FFFFFF, sand #ECE7DD, ink #282828, charcoal #2B2929 (footer), espresso #321E1D (donker verhaalblok), brick #AC3B19 (knoppen, eyebrows, bars), titanium #C9C6C0 (tekst op donker). Variabelen in collectie "Email tokens".
- Type: Instrument Serif Italic als display (TT Ramillas Trl Light Italic zodra lokaal geïnstalleerd), Inter voor al het andere. Schaal 56/44/34 display, 22 heading, 12 eyebrow caps +12%, 16 body, 13 caption, 11 legal.
- Componenten (600px, auto-layout, tekst-properties): Bars/Announcement, Header Light/Dark, Hero Image full-bleed, Hero Cream product, Text/Section intro, Split image left/right, Product Grid 2, Product Single, Offer/Code, Proof/Review, Text/Numbered list, Proof/Comparison, Bars/Trust, Text/Dark story, Image full width, Image grid 3, Text/Founder note, Footer/Built for Life, Spacer.
- `ds.py` genereert `figma/ds-01-components.js`; `figma/ds-00-foundations.js` bouwt de Foundations-pagina. Beide draaien via de Figma MCP `use_figma`.
- Foto's: `upload_assets` naar de pagina, daarna de imageHash kopiëren naar de `IMG`-frames in de instances (instance-kinderen kunnen niet direct als upload-target).

## Fotografie

- `figma/photos/`: brandfoto's uit de Drive-map "Siraat flash style" (verkleind naar 1800px): flash-shoot 1.10, 1.12, 1.23, 1.24, lifestyle azure/ember, schorten Azure/Moss/Caramel Oak/Ember + details. In Figma op pagina "03 Fotos".
- Twaalf shootfoto's (1.1, 1.3, 1.4, 1.7, 1.8, 1.9, 1.11, 1.14 t/m 1.17, 1.25, 1.26) zijn groter dan 6 MB en konden niet via de Drive-koppeling binnenkomen. Sleep ze rechtstreeks in Figma op pagina "03 Fotos".
- `figma/ai/`: AI-beelden (Higgsfield, gpt_image_2_5) met de productfoto van de Hammered Pan Pro als referentie. Flash-stijl volgens de skill `siraat-flash-style`.
- AI-regel: laat het model nooit letters, logo of opdruk renderen (bandjes komen gespiegeld of verhaspeld terug). Prompt altijd "plain cream straps, no text, no patch"; bestaand beeld schoonmaken met een edit-pass ("only change: plain straps, nothing else"). Het echte monogram komt daarna in Figma. Referenties voor de stijl: twee shootfoto's + de Shopify-productfoto via `media_import_url` (Figma-screenshot-URL werkt als bron, upload.higgsfield.ai is geblokkeerd).

## Font

- Koppen: **TT Ramillas Light Italic** (TypeType, desktop-licentie via MyFonts, order 18927546368170). Bestand in `klaviyo/fonts/TTRamillas-LightItalic.ttf`. In Figma heet hij "TT Ramillas" / "Light Italic"; de generators proberen die eerst en vallen terug op Instrument Serif Italic als het font niet lokaal staat.
- E-mail: alleen desktop-licentie, dus koppen in TT Ramillas gaan als beeld mee (hero gebakken via `scratchpad/tools/hero_tt.js`, font geïnstalleerd in `~/.fonts`). Lopende tekst blijft Inter als echte tekst; serif-fallback in HTML is Instrument Serif met Times New Roman.
