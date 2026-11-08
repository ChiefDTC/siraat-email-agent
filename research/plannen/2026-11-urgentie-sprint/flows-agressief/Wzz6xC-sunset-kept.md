# Wzz6xC · v4 · Sunset · kept: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `Wzz6xC` (Added to List), status live, 2 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 108 ontvangers (54 per week), $374 omzet, $3,46 per ontvanger, 6,48% unieke klik.
- Echte deadlines in deze flow: Na de tik in Sunset. Echt nu: BF-einde. Klein volume maar $3,46 per ontvanger: mensen die net bleven kopen.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| SUNSET-KEPT · S3 | 30 min na trigger | 61 | $0,00 | You're staying. Thank you. | You're staying. Up to 70% off ends Nov 30. | groen |
| SUNSET-KEPT · S4 | 4,02 d na trigger | 47 | $7,96 | The pan we started with | The pan we started with, up to 70% off until {{DEADLINE_SHORT}} | groen |

## SUNSET-KEPT · S3

- Berichten: SUNSET-KEPT · S3 (`SmGgU3`, template `UKiBi4`)
- Positie: 30 min na trigger. 14 dagen: 61 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: You're staying. Thank you.
- Huidige preview: One quick tap so we only send what you came for.
- Huidige hero en CTA: (geen hero-beeld; tekstmail) · knop: My first titanium pan, A full set, pans and lids

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | You're staying. Up to 70% off ends Nov 30. | [SALE70]; [BFEND] | groen |
| Subject 2 | Thank you. One tap, then the sale before {{DEADLINE_SHORT}}. | [BFEND] | groen |
| Subject 3 | You stayed just in time: Black Friday ends {{DEADLINE_SHORT}} ⏰ | [BFEND] | oranje |
| Preview 1 | One quick tap so we only send what you came for. The sale ends {{DEADLINE}}. | [BFEND] | groen |
| Preview 2 | Pan, set or gift? Pick one, and get it before {{DEADLINE}}. | [BFEND] | groen |
| Hero | You're staying.\|Black Friday until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | My first titanium pan | [SALE70] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. 5 free gifts with every order until {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |

## SUNSET-KEPT · S4

- Berichten: SUNSET-KEPT · S4 (`XJXVru`, template `SGYWKp`)
- Positie: 4,02 d na trigger. 14 dagen: 47 ontvangers, $374 omzet, $7,96 per ontvanger.
- Huidig onderwerp: The pan we started with
- Huidige preview: Why I'd still pick it today, and the paper that backs it up.
- Huidige hero en CTA: (geen hero-beeld; tekstmail) · knop: Show me the pans, Choose fewer emails

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | The pan we started with, up to 70% off until {{DEADLINE_SHORT}} | [SALE70]; [BFEND] | groen |
| Subject 2 | Since you stayed: the original pan, Black Friday priced until Nov 30 | [BFEND] | groen |
| Subject 3 | LAST CHANCE: the original hammered titanium pan ⏰ | [BF48] | oranje |
| Preview 1 | Why I'd still pick it today, and the paper that backs it up. On sale until {{DEADLINE}}. | [BFEND] | groen |
| Preview 2 | First shipped December 20, 2024. Copied since. On sale until {{DEADLINE}}. | merkverhaal (DECISIONS 1 okt); [BFEND] | groen |
| Hero | The original.\|On sale until {{DEADLINE_SHORT}}. | merkverhaal; [BFEND] | groen |
| CTA | Show me the pans | [SALE70] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. 75-year warranty, 30-day returns. The price is the only thing with a deadline. | [W75]; [RETURN30]; [BFEND] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| You unlocked a VIP price for staying | Er is geen prijs voor blijven. |

## Voorwaarden in deze flow

- **[BF48]** de mail gaat uit op 29 of 30 nov (laatste 48 uur van BF), zelfde datumblok als [BF30]; 'last chance' en 'final hours' alleen dan
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[RETURN30]** 30 dagen retour vanaf bezorging, ongebruikt (DECISIONS 1 okt)
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
- **[W75]** 75 jaar garantie (DECISIONS 1 okt)
