# WTY94m · v4 · Abonnement S1 (Loop, test 20%): te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `WTY94m` (Metric), status live, 1 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 260 ontvangers (130 per week), $0 omzet, $0,00 per ontvanger, 10,38% unieke klik.
- Echte deadlines in deze flow: Echt nu: gratis eerste pak sheets, abonnement in Loop met een echte volgende afschrijfdatum. Dat is de enige echte deadline: beslissen vóór de eerste afschrijving.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| S1 skip-tip (b) | 15 min na trigger | 260 | $0,00 | Your first pack of sheets is on us | Your first pack is on us. Your next one: {{NEXT_CHARGE}}. | groen |

## S1 skip-tip (b)

- Berichten: S1 skip-tip (b) (`VDW3P7`, template `Rs5ebw`)
- Positie: 15 min na trigger. 14 dagen: 260 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: Your first pack of sheets is on us
- Huidige preview: Your free dishwasher sheet pack is on us.
- Huidige hero en CTA: A pack of Siraat Dishwasher Sheets with sheets in front · knop: See my subscription

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your first pack is on us. Your next one: {{NEXT_CHARGE}}. | [SUBNEXT] | groen |
| Subject 2 | Skip, keep or cancel before {{NEXT_CHARGE}} | [SUBNEXT] | groen |
| Subject 3 | HEADS UP: your next pack ships {{NEXT_CHARGE}} ⏰ | [SUBNEXT] | oranje |
| Preview 1 | Here is exactly how it works, so nothing is a surprise on {{NEXT_CHARGE}}. | [SUBNEXT] | groen |
| Preview 2 | Change it in one tap until {{NEXT_CHARGE}}. | [SUBNEXT] | groen |
| Hero | Your first pack is on us.\|Next one {{NEXT_CHARGE}}. | [SUBNEXT] | groen |
| CTA | See my subscription | geen backend-voorwaarde (geen claim) | groen |
| Deadline-regel | Your next delivery is {{NEXT_CHARGE}}. Skip or cancel any time before. | [SUBNEXT] | groen |
| PS | P.S. 20% off every refill, as long as you stay. | [SUB]: 20% blijft gelden | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your free pack will be charged unless you act now | Alleen waar als de volgende levering echt betaald is en de datum klopt; nooit 'unless you act now' zonder {{NEXT_CHARGE}}. |

## Voorwaarden in deze flow

- **[SUB]** Loop-abonnement met 20% op elke levering is actief
- **[SUBNEXT]** {{NEXT_CHARGE}} = echte volgende afschrijfdatum uit Loop voor dit profiel; overslaan of opzeggen kan echt tot die datum
