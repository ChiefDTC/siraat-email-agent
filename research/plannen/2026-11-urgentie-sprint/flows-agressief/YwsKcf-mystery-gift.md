# YwsKcf · v4 · Mystery Gift: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `YwsKcf` (Metric), status live, 3 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 1.263 ontvangers (631 per week), $170 omzet, $0,13 per ontvanger, 4,04% unieke klik.
- Echte deadlines in deze flow: Dishwasher sheets als mystery gift; M3 verkoopt het abonnement (20% elke maand). Geen header en geen logo bovenaan (Floris 23 okt). Echt nu: geen deadline op het abonnement; wel BF-einde voor een tweede order en de echte gebruiksduur van het gratis pak (ongeveer twee maanden bij 1 keer per dag, staat in M3).

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| M1 reveal | 3 d na trigger | 1.093 | $0,16 | Let's reveal your mystery gift | Your mystery gift, revealed (5 gifts end Nov 30) | groen |
| M2 how to use | 12 d na trigger | 170 | $0,00 | The ten-second way to use your gift | Ten seconds, one sheet. Start tonight. | groen |
| M3 offer | 23 d na trigger | 0 | - | Alright, here's the offer | Your free pack runs out soon. Here's the refill. | oranje |

## M1 reveal

- Berichten: v4 · Mystery · M1 reveal (`RNvK6a`, template `Vpmw78`)
- Positie: 3 d na trigger. 14 dagen: 1.093 ontvangers, $170 omzet, $0,16 per ontvanger.
- Huidig onderwerp: Let's reveal your mystery gift
- Huidige preview: It's not overstock. It's the other half of a no-coating kitchen.
- Huidige hero en CTA: Lifting a pack of Plastic-Free Dishwasher Sheets out of the mystery gift box · knop: See my gift up close

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your mystery gift, revealed (5 gifts end Nov 30) | [GIFTSEND] | groen |
| Subject 2 | Open the small box first | het gift zit echt in de order van dit profiel | groen |
| Subject 3 | REVEALED: the gift most brands won't explain ⏰ | claim 'most brands' is een mening; caps | oranje |
| Preview 1 | It's not overstock. It's the other half of a no-coating kitchen. | staat al in de mail | groen |
| Preview 2 | Another order before {{DEADLINE}} brings another mystery gift. | [GIFTS5]; [GIFTSEND] | groen |
| Hero | Your mystery gift.\|Revealed. | geen deadline | groen |
| CTA | See my gift up close | geen backend-voorwaarde (geen claim) | groen |
| Deadline-regel | Every order until {{DEADLINE}} gets 5 free gifts, this one included. | [GIFTS5]; [GIFTSEND] | groen |
| PS | P.S. One sheet per load. Your pack lasts about two months. | 1 keer per dag, staat in M3 | groen |

## M2 how to use

- Berichten: v4 · Mystery · M2 how to use (`Twinff`, template `ViJfKJ`)
- Positie: 12 d na trigger. 14 dagen: 170 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: The ten-second way to use your gift
- Huidige preview: One sheet where the pod goes. Half a sheet for a light load.
- Huidige hero en CTA: Dropping one dishwasher sheet into the dispenser, pans in the rack · knop: Show me the sheets

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Ten seconds, one sheet. Start tonight. | geen claim, alleen instructie | groen |
| Subject 2 | Use your gift before the pods run out | o: suggestie, geen claim | oranje |
| Subject 3 | Black Friday ends Nov 30: one sheet, ten seconds | [BFEND] | groen |
| Preview 1 | One sheet where the pod goes. Half a sheet for a light load. | staat al in de mail | groen |
| Preview 2 | Up to 60 washes a pack. Black Friday on the pans ends {{DEADLINE}}. | staat al in de mail; [BFEND] | groen |
| Hero | One sheet.\|Ten seconds. | geen backend-voorwaarde (geen claim) | groen |
| CTA | Show me the sheets | geen backend-voorwaarde (geen claim) | groen |
| Deadline-regel | The pans that pair with it are up to 70% off until {{DEADLINE}}. | [SALE70]; [BFEND] | groen |
| PS | P.S. Your pack runs out in about two months. Then it's the pods again. | 1 keer per dag | groen |

## M3 offer

- Berichten: v4 · Mystery · M3 offer (`YgyYa5`, template `U4Gawu`)
- Positie: 23 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: Alright, here's the offer
- Huidige preview: Including the part most brands would leave out.
- Huidige hero en CTA: A fresh pack of dishwasher sheets arriving by mail, right on time · knop: Get 20% every month, the same page

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your free pack runs out soon. Here's the refill. | pak is na 23 dagen bij dagelijks gebruik deels op (ongeveer twee maanden totaal) | oranje |
| Subject 2 | Never out of sheets at 10 pm: 20% every month | [SUB]: 20% abonnement actief | groen |
| Subject 3 | Before your last sheet: 20% off every refill ⏰ | 20% actief; geen einddatum op de 20% | oranje |
| Preview 1 | Including the part most brands would leave out. 20% off, skip or cancel anytime. | staat al in de mail; overslaan/opzeggen kan echt | groen |
| Preview 2 | Your gift pack lasts about two months. Set the refill now so it lands before the last sheet. | eerste levering van het abonnement komt echt vóór het pak op is (timing in Loop) | oranje |
| Hero | Never run out.\|20% off every month. | geen backend-voorwaarde (geen claim) | groen |
| CTA | Get 20% every month | geen backend-voorwaarde (geen claim) | groen |
| Deadline-regel | Your free pack: about two months. Your refill: whenever you say. | 1 keer per dag | groen |
| PS | P.S. Add a pan before {{DEADLINE}} and that order gets 5 free gifts too. | [GIFTS5]; [GIFTSEND] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your 20% subscription offer ends tonight | Er is geen einddatum op de 20% (Loop). |
| Only a few packs left | Geen voorraaddata. |

## Voorwaarden in deze flow

- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
- **[SUB]** Loop-abonnement met 20% op elke levering is actief
