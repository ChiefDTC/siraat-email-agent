# VPixnJ · v4 · UGC first egg: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `VPixnJ` (Metric), status live, 1 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 429 ontvangers (214 per week), $154 omzet, $0,36 per ontvanger, 0,00% unieke klik.
- Echte deadlines in deze flow: Echt nu: 15% na een foto-reply, geen einddatum op die 15%. Urgentie alleen via de sale.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| U1 | 4 d na trigger | 429 | $0,36 | Show us your first egg? | Show us your first egg, and use your 15% before Nov 30 | oranje |

## U1

- Berichten: U1 (`RBrHK9`, template `SRZXtf`)
- Positie: 4 d na trigger. 14 dagen: 429 ontvangers, $154 omzet, $0,36 per ontvanger.
- Huidig onderwerp: Show us your first egg?
- Huidige preview: Reply with a photo of your first egg, or anything you cooked. We'll send you 15% off.
- Huidige hero en CTA: Your first week: show us your first egg. How did it go? Reply with a photo and get 15% off your next order. · knop: Send my photo, care and use page

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Show us your first egg, and use your 15% before Nov 30 | [UGC15]; 15% stapelt op de sale (flowcodes stapelen, DECISIONS 19 okt); [BFEND] | oranje |
| Subject 2 | One photo = 15% off. Black Friday ends {{DEADLINE_SHORT}}. | [UGC15]; [BFEND] | oranje |
| Subject 3 | Reply with your egg. Get 15%. Today. | 15% wordt dezelfde dag gestuurd (team-SLA) | rood |
| Preview 1 | Reply with a photo of your first egg. We'll send you 15% off to use before Black Friday ends. | [UGC15]; 15% komt vóór {{DEADLINE}} | oranje |
| Preview 2 | A phone photo is perfect. Your 15% plus up to 70% off until {{DEADLINE}}. | [UGC15]; stapelen getest | oranje |
| Hero | Your first egg.\|Our 15%. | [UGC15] | groen |
| CTA | Send my photo now | geen backend-voorwaarde (geen claim) | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}, so send it this week. | [BFEND] | groen |
| PS | P.S. Faces optional. Eggs mandatory. | geen backend-voorwaarde (geen claim) | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Send your photo by tonight for 15% | Geen einddatum op de 15%; alleen met [UGC15] plus een echte einddatum. |

## Voorwaarden in deze flow

- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[UGC15]** de 15% wordt echt na een foto-reply gestuurd; een einddatum op de 15% bestaat nu niet, dus deadline alleen via de sale [BFEND]
