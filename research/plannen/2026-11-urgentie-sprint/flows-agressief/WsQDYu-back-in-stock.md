# WsQDYu · BIS | Back in Stock Waitlist: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `WsQDYu` (Metric), status live, 2 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 101 ontvangers (50 per week), $2.191 omzet, $21,69 per ontvanger, 5,94% unieke klik.
- Echte deadlines in deze flow: Hoogste RPR van de account ($21,69, 101 ontvangers in 14 dagen). Echt nu: het product is echt terug (trigger), BF-prijs tot 30 nov. Huidige preview 'You're first in line, limited restock' is een schaarsteclaim zonder getal: alleen houden met echte voorraad.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| BIS 1 · on the list | 0 min na trigger | 99 | $22,13 | You're On The List! | You're on the list. Black Friday prices end Nov 30. | groen |
| BIS 2 · it's back | 0 min na trigger | 2 | $0,00 | It's Back! {{ event.ProductName }} | IT'S BACK: {{ event.ProductName }}, at Black Friday prices | oranje |

## BIS 1 · on the list

- Berichten: BIS 1 , You're On The List (`Scuk9u`, template `Vj75bH`)
- Positie: 0 min na trigger. 14 dagen: 99 ontvangers, $2.191 omzet, $22,13 per ontvanger.
- Huidig onderwerp: You're On The List!
- Huidige preview: We'll let you know the moment it's back.
- Huidige hero en CTA: Siraat Kitchen · knop: EXPLORE WHAT’S IN STOCK

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | You're on the list. Black Friday prices end Nov 30. | [BFEND] | groen |
| Subject 2 | You'll hear first. The price you'll get ends {{DEADLINE_SHORT}}. | [BISFIRST]; [BFEND] | oranje |
| Subject 3 | ON THE LIST: and 5 free gifts until Nov 30 | [GIFTS5]; [BFEND] | oranje |
| Preview 1 | We'll email you the moment it's back. Meanwhile, everything in stock is up to 70% off until {{DEADLINE}}. | [SALE70]; [BFEND] | groen |
| Preview 2 | If it's back before {{DEADLINE}}, it's at the Black Friday price. | product staat in de BF-collectie | oranje |
| Hero | You're on the list.\|Black Friday until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Explore what's in stock now | [SALE70] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. Can't wait? The rest of the range ships now, with 5 free gifts. | [GIFTS5] | groen |

## BIS 2 · it's back

- Berichten: BIS 2 , It's Back (`Rrh2Qh`, template `WwZUbW`)
- Positie: 0 min na trigger. 14 dagen: 2 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: It's Back! {{ event.ProductName }}
- Huidige preview: You're first in line , limited restock.
- Huidige hero en CTA: Siraat Kitchen · knop: (geen knop gevonden)

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | IT'S BACK: {{ event.ProductName }}, at Black Friday prices | [BIS]; product in BF-sale | oranje |
| Subject 2 | It's back, and you're first. Order before {{DEADLINE_SHORT}}. | [BIS]; [BISFIRST]; [BFEND] | groen |
| Subject 3 | Back in stock: order now, Black Friday ends Nov 30 ⏰ | [BIS]; [BFEND] | oranje |
| Preview 1 | You asked us to tell you. It's in stock now, up to 70% off until {{DEADLINE}}. | [BIS]; [SALE70]; [BFEND] | groen |
| Preview 2 | You're hearing it first. The Black Friday price and 5 gifts end {{DEADLINE}}. | [BISFIRST]; [GIFTSEND] | oranje |
| Hero | It's back.\|You're first. | [BIS]; [BISFIRST] | oranje |
| CTA | Get mine before it's gone | [BIS]; [STOCKNUM]; anders 'Get mine now' (groen) | rood |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. Only {{UNITS}} back in this restock. | [STOCKNUM] | rood. Alleen met echte voorraadvariabele. |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Only {{N}} left (zonder echte voorraadvariabele) | Valse schaarste. |
| Selling out again in hours | Geen data. |
| We held one for you | Niets wordt vastgehouden (verboden 'reserve'). |

## Voorwaarden in deze flow

- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[BIS]** het product staat op het verzendmoment echt weer op voorraad (BIS-trigger, catalog unpublished=cancel)
- **[BISFIRST]** de waitlist-mail gaat echt uit vóór een campagne of algemene aankondiging van deze restock
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
- **[STOCKNUM]** echte voorraad van deze variant op het verzendmoment staat als variabele {{UNITS}} in de mail (catalogusfeed of Shopify-voorraad); een verzonnen getal of 'selling out' zonder data is nepschaarste
