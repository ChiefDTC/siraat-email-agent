# YyaMjx · FREE E - GUIDE: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `YyaMjx` (Metric), status live, 1 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 4.449 ontvangers (2.224 per week), $2.834 omzet, $0,64 per ontvanger, 7,37% unieke klik.
- Echte deadlines in deze flow: Na het gratis e-book/cookbook bij een order. Hoge klik (7,4%) en $0,64 per ontvanger. Echt nu: BF-einde, gifts per order.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| E-Guide Flow | 3 min na trigger | 4.449 | $0,64 | Your two books are ready | Your two books are ready. Black Friday ends Nov 30. | groen |

## E-Guide Flow

- Berichten: E-Guide Flow (`XtYsPr`, template `Sid3kX`)
- Positie: 3 min na trigger. 14 dagen: 4.449 ontvangers, $2.834 omzet, $0,64 per ontvanger.
- Huidig onderwerp: Your two books are ready
- Huidige preview: 25 recipes and a 90-page home guide. Yours to keep.
- Huidige hero en CTA: Your two Siraat books: The Favorites Cookbook and the Plastic-Free Home E-Book, ready to download · knop: Download my cookbook, Download my e-book

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your two books are ready. Black Friday ends Nov 30. | [BFEND] | groen |
| Subject 2 | Download now, then the pan from page 1 at up to 70% off | [SALE70]; recept op pagina 1 gebruikt de Pan Pro (controleren) | oranje |
| Subject 3 | ENDS TONIGHT: cook the cookbook at Black Friday prices ⏰ | [BF30] | oranje |
| Preview 1 | 25 recipes and a 90-page home guide. The pans in them are up to 70% off until {{DEADLINE}}. | [SALE70]; [BFEND] | groen |
| Preview 2 | Yours to keep. The Black Friday price isn't, it ends {{DEADLINE}}. | [BFEND] | groen |
| Hero | Your books are ready.\|The pans are on sale until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Download my cookbook | downloadlink werkt | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. A second order gets its own 5 free gifts until {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your download link expires tonight | De Shopify-downloadlink vervalt niet op een gekozen moment; niet zeggen tenzij de link echt vervalt. |

## Voorwaarden in deze flow

- **[BF30]** de mail gaat uit op 30 nov (laatste BF-dag) en saleprijs, BFCODE en gifts stoppen echt op {{DEADLINE}}. In een flow alleen via een datumblok in onderwerp en hero ({% today %}-vergelijking, getest) of doordat Floris op 30 nov de onderwerpen omzet (PATCH flow-action) en op 1 dec terugzet; andere dagen valt de regel terug op de [BFEND]-versie
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
