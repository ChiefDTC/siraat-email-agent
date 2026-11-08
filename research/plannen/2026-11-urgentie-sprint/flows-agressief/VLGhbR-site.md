# VLGhbR · v4 · Site abandonment: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `VLGhbR` (Metric), status live, 2 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 2.779 ontvangers (1.389 per week), $1.480 omzet, $0,53 per ontvanger, 1,91% unieke klik.
- Echte deadlines in deze flow: Echt nu: BFCODE (extra 10%) en gifts tot einde BF. Geen code met eigen einddatum.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | 2 u na trigger | 1.624 | $0,91 | Four eggs or five? Black Friday is live. | Four eggs or five? Pick by {{DEADLINE_SHORT}}. | groen |
| A2 | 2,08 d na trigger | 1.155 | $0,00 | Where 100,000+ customers started, priced for Black Friday | Where 100,000+ customers started. Ends {{DEADLINE_SHORT}}. | groen |

## A1

- Berichten: A1 (`Tmfm4K`, template `QWPjqS`)
- Positie: 2 u na trigger. 14 dagen: 1.624 ontvangers, $1.480 omzet, $0,91 per ontvanger.
- Huidig onderwerp: Four eggs or five? Black Friday is live.
- Huidige preview: Four sizes, one titanium surface. An extra 10% on top of Black Friday prices.
- Huidige hero en CTA: Which size? Four eggs or five? How to pick your pan in 30 seconds. Extra 10% off with code BFCODE, plus 4 free gifts. · knop: Get 10% off my pan, Pick the Mini

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Four eggs or five? Pick by {{DEADLINE_SHORT}}. | [BFEND] | groen |
| Subject 2 | Your size, extra 10% on top, until Nov 30 | [BFCODE]; [BFEND] | groen |
| Subject 3 | ENDS TONIGHT: every size + an extra 10% ⏰ | [BF30]; [BFCODE] | oranje |
| Preview 1 | Four sizes, one titanium surface. Extra 10% on top of Black Friday prices until {{DEADLINE}}. | [BFCODE]; [BFEND] | groen |
| Preview 2 | Pick in 30 seconds. Order before {{DEADLINE}} and the 5 free gifts come with it. | [GIFTS5]; [GIFTSEND] | groen |
| Hero | Pick your size.\|Extra 10% until {{DEADLINE_SHORT}}. | [BFCODE]; [BFEND] | groen |
| CTA | Get 10% off my size now | [BFCODE] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. Between two sizes? Take the bigger one. You have 30 days to return it. | [RETURN30] | groen |

## A2

- Berichten: A2 (`WW785H`, template `UhMjpE`)
- Positie: 2,08 d na trigger. 14 dagen: 1.155 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: Where 100,000+ customers started, priced for Black Friday
- Huidige preview: Most people start with one pan. An extra 10% on top of Black Friday prices.
- Huidige hero en CTA: Best seller: Titanium Hammered Pan Pro, / 11″ / 28 cm / 28 cm (11″) · knop: The Pan Pro, 11″28 cm28 cm (11″), Get 10% off this pan

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Where 100,000+ customers started. Ends {{DEADLINE_SHORT}}. | [BFEND] | groen |
| Subject 2 | The best seller, an extra 10% until Nov 30 | Pan Pro is de bestseller (staat al in de template); [BFCODE]; [BFEND] | groen |
| Subject 3 | LAST CHANCE: the best seller at Black Friday prices ⏰ | [BF48] | oranje |
| Preview 1 | Most people start with one pan. Extra 10% on top of Black Friday prices until {{DEADLINE}}. | [BFCODE]; [BFEND] | groen |
| Preview 2 | The Pan Pro, 5 free gifts, an extra 10%. All three end {{DEADLINE}}. | [GIFTS5]; [BFCODE]; [GIFTSEND] | groen |
| Hero | Where most start.\|Extra 10% until {{DEADLINE_SHORT}}. | [BFCODE]; [BFEND] | groen |
| CTA | Get 10% off this pan now | [BFCODE] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. Last email about it from us. The price is what changes next, {{DEADLINE}}. | [LASTFLOW]; [PRICEUP] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your order is pending / will be canceled | Er bestaat geen order; nep-orderstatus (FTC Act sectie 5, CAN-SPAM). |
| Only 3 left / almost sold out | Geen echte voorraaddata per variant in de flow; valse schaarste. |
| We extended your discount 24 hours, it cannot be extended again | Verzonnen verlenging; BRIEF verbiedt 'no extensions'. |
| Your code expires tonight (in een 48-uurs codemail op het moment van uitgifte) | Op het uitgiftemoment zijn het nog 48 uur. Alleen waar in de nieuwe herinneringsstap [CODEREM]. |

## Voorwaarden in deze flow

- **[BF30]** de mail gaat uit op 30 nov (laatste BF-dag) en saleprijs, BFCODE en gifts stoppen echt op {{DEADLINE}}. In een flow alleen via een datumblok in onderwerp en hero ({% today %}-vergelijking, getest) of doordat Floris op 30 nov de onderwerpen omzet (PATCH flow-action) en op 1 dec terugzet; andere dagen valt de regel terug op de [BFEND]-versie
- **[BF48]** de mail gaat uit op 29 of 30 nov (laatste 48 uur van BF), zelfde datumblok als [BF30]; 'last chance' en 'final hours' alleen dan
- **[BFCODE]** BFCODE (extra 10% bovenop de sale, alleen abandonment) staat in de knoplink en werkt op het verzendmoment; BFCODE stopt met BF, dus de einddatum is [BFEND]
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[LASTFLOW]** dit is echt de laatste mail van deze flow voor dit profiel (geen stap meer erna)
- **[PRICEUP]** de producten in deze cart/checkout gaan op {{DEADLINE}} echt terug naar de normale prijs (einde BF). De Shopify-cart zelf vervalt niet en houdt geen prijs vast; de regel gaat over de prijs, nooit over de cart
- **[RETURN30]** 30 dagen retour vanaf bezorging, ongebruikt (DECISIONS 1 okt)
