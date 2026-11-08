# Rn556d · v4 · BFCM Welcome · direct A/B (hoofdlijst): te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `Rn556d` (Added to List), status live, 1 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 7.169 ontvangers (3.584 per week), $24.990 omzet, $3,49 per ontvanger, 4,07% unieke klik.
- Echte deadlines in deze flow: Echt nu: BF-sale zonder code tot 30 nov, 5 gifts tot 30 nov. Eén mail direct na aanmelding; tweede beste RPR van de welkomstkant.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| BF-W1 direct · D glass | 0 min na trigger | 7.169 | $3,49 | You're just in time 🧡 | ENDS {{DEADLINE_SHORT}}: up to 70% off + 5 free gifts ⏰ | oranje |

## BF-W1 direct · D glass

- Berichten: BF-W1 direct · D glass (`TauWAG`, template `TdfWqT`)
- Positie: 0 min na trigger. 14 dagen: 7.169 ontvangers, $24.990 omzet, $3,49 per ontvanger.
- Huidig onderwerp: You're just in time 🧡
- Huidige preview: Your prices: up to 70% off. No code needed, it's ready on the site.
- Huidige hero en CTA: Siraat hammered titanium pans in a dark vault · knop: Pan Pro Standard, Pan Set, 6 Pcs

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | ENDS {{DEADLINE_SHORT}}: up to 70% off + 5 free gifts ⏰ | [SALE70]; [GIFTS5]; [BFEND] | oranje |
| Subject 2 | You made it. Up to 70% off until Nov 30. | [SALE70]; [BFEND] | groen |
| Subject 3 | ENDS TONIGHT: up to 70% off, no code needed ⏰ | [BF30] | oranje |
| Preview 1 | Up to 70% off, no code, already on the site. Black Friday ends {{DEADLINE}}. | [SALE70]; [BFEND] | groen |
| Preview 2 | 5 free gifts ($555 value) ship with every order until {{DEADLINE}}. Then they're gone. | [GIFTS5] (US; INT zonder waarde); [GIFTSEND] | groen |
| Hero | Up to 70% off.\|Gone {{DEADLINE_SHORT}}. | [SALE70]; [BFEND] | groen |
| CTA | Get my 70% off before it ends | [SALE70]; [BFEND] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. Black Friday is the only time this year that up to 70% off and 5 free gifts come together. It ends {{DEADLINE}}. | Floris bevestigt dat er in 2026 na 30 nov geen actie komt met dezelfde korting plus 5 gifts | oranje |
| INT-variant prev2 | 5 free gifts ship with every order, duties paid, until {{DEADLINE}}. Then they're gone. | [GIFTS5]; [GIFTSEND] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your VIP price expires tonight | De prijs is voor iedereen en eindigt pas 30 nov; 'VIP' is hier een label van de sale, geen persoonlijke prijs. |
| You're just in time, only hours left | Alleen op 30 nov waar; anders vals. |

## Voorwaarden in deze flow

- **[BF30]** de mail gaat uit op 30 nov (laatste BF-dag) en saleprijs, BFCODE en gifts stoppen echt op {{DEADLINE}}. In een flow alleen via een datumblok in onderwerp en hero ({% today %}-vergelijking, getest) of doordat Floris op 30 nov de onderwerpen omzet (PATCH flow-action) en op 1 dec terugzet; andere dagen valt de regel terug op de [BFEND]-versie
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
