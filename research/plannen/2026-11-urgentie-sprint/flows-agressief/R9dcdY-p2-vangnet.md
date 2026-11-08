# R9dcdY · v4 · P2 vangnet · Fulfilled +12d (geen Delivered): te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `R9dcdY` (Metric), status live, 1 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 0 ontvangers (0 per week), $0 omzet, $0 per ontvanger, 0% unieke klik.
- Echte deadlines in deze flow: Zelfde mail als VQ93sx, voor orders zonder Delivered-event. Zelfde copy.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| P2 · the mistake that makes titanium stick | 12 d na trigger | 0 | - | The mistake that makes titanium stick | The mistake that makes titanium stick (read before dinner) | groen |

## P2 · the mistake that makes titanium stick

- Berichten: P2 · vangnet (`SVD5Jt`, template `UJ4XeW`)
- Positie: 12 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: The mistake that makes titanium stick
- Huidige preview: Medium on titanium works like high on a normal pan. The chef's five steps.
- Huidige hero en CTA: Chef guide. If you can do an egg, you can do anything. Heat first, then oil, then egg. · knop: Watch the chef video, Add the 11″28 cm28 cm (11″) lid

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | The mistake that makes titanium stick (read before dinner) | geen deadline; educatief | groen |
| Subject 2 | Medium is the new high. And Black Friday ends Nov 30. | [BFEND] | groen |
| Subject 3 | LAST CHANCE: the lid for your pan at Black Friday prices ⏰ | [BF48] | oranje |
| Preview 1 | The chef's five steps. Plus the lid that fits, on sale until {{DEADLINE}}. | [BFEND] | groen |
| Preview 2 | Medium on titanium works like high on a normal pan. The sale works until {{DEADLINE}}. | [BFEND] | groen |
| Hero | Don't turn it to high.\|Lid on sale until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Get the lid before the sale ends | [BFEND] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. Anything stick already? Reply with a photo, our team answers. The lid sale ends {{DEADLINE}}. | [BFEND]; reply-to is support | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your pan warranty expires if you don't register | Er is geen registratieplicht; verzonnen. |

## Voorwaarden in deze flow

- **[BF48]** de mail gaat uit op 29 of 30 nov (laatste 48 uur van BF), zelfde datumblok als [BF30]; 'last chance' en 'final hours' alleen dan
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
