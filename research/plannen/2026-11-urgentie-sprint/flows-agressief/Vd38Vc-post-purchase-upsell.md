# Vd38Vc · v4 · Post-purchase upsell 50% test · TEST (draft): te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `Vd38Vc` (Metric), status live, 6 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 0 ontvangers (0 per week), $0 omzet, $0 per ontvanger, 0% unieke klik.
- Echte deadlines in deze flow: Echt nu: BF-sale en gifts tot 30 nov; 'ships free on its own' staat al in de copy. Live maar 0 ontvangers in 14 dagen (test). pp-addon (+2 uur) is de enige mail in de hele account waar 'before your order ships' bijna altijd klopt, mits er een mechanisme is om toe te voegen.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| pp-addon US | 2 u na trigger | 0 | - | Forgot the lid? | Forgot the lid? Add it before your order ships | rood |
| pp-addon INT | 2 u na trigger | 0 | - | Forgot the lid? | Forgot the lid? Add it before your order ships | rood |
| pp-complete US en INT | 3,08 d na trigger | 0 | - | Complete your kitchen | Complete your kitchen before {{DEADLINE_SHORT}}: up to 70% off | groen |
| pp-twopans US en INT | 21,08 d na trigger | 0 | - | Two pans, one dinner | Two pans, one dinner. The second is on sale until Nov 30. | groen |

## pp-addon US

- Berichten: pp-addon US (`Rxy7yQ`, template `V8pSzN`)
- Positie: 2 u na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: Forgot the lid?
- Huidige preview: The lid, the tools, a second size. Still 70% off, and it ships free.
- Huidige hero en CTA: Siraat Wok Pan Pro · knop: Wok Pan Pro, Add the Wok Pan Pro

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Forgot the lid? Add it before your order ships | [UNSHIP] | rood |
| Subject 2 | Forgot the lid? Still up to 70% off until {{DEADLINE_SHORT}} | [SALE70]; [BFEND] | groen |
| Subject 3 | ORDER NOW: the lid ships free, Black Friday ends Nov 30 ⏰ | [SHIPSEP]; [BFEND] | oranje |
| Preview 1 | The lid, the tools, a second size. Up to 70% off and it ships free on its own until {{DEADLINE}}. | [SALE70]; [SHIPSEP]; [BFEND] | groen |
| Preview 2 | Your order hasn't shipped yet. Add it now. | [UNSHIP] | rood |
| Hero | Forgot something?\|Up to 70% off until {{DEADLINE_SHORT}}. | [SALE70]; [BFEND] | groen |
| CTA | Add the lid now | [SALE70] | groen |
| Deadline-regel | Black Friday prices end {{DEADLINE}}. It ships free on its own. | [BFEND]; [SHIPSEP] | groen |
| PS | P.S. Just ordered? Reply now. If your first order hasn't left, our team will try to combine them. | [SUPPORTMERGE] | oranje |

## pp-addon INT

- Berichten: pp-addon INT (`UvnPXb`, template `WhNHtE`)
- Positie: 2 u na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: Forgot the lid?
- Huidige preview: The lid, the tools, a second size. Still 70% off, and it ships free.
- Huidige hero en CTA: Siraat Wok Pan Pro · knop: Wok Pan Pro, Add the Wok Pan Pro

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Forgot the lid? Add it before your order ships | [UNSHIP] | rood |
| Subject 2 | Forgot the lid? Still up to 70% off until {{DEADLINE_SHORT}} | [SALE70]; [BFEND] met INT-tijdzone | groen |
| Subject 3 | ORDER NOW: the lid ships free, duties paid ⏰ | [SHIPSEP]; INT duties paid | oranje |
| Preview 1 | The lid, the tools, a second size. Up to 70% off, free shipping, duties paid, until {{DEADLINE}}. | [SALE70]; [SHIPSEP]; [BFEND] | groen |
| Preview 2 | Your order hasn't shipped yet. Add it now. | [UNSHIP] | rood |
| Hero | Forgot something?\|Up to 70% off until {{DEADLINE_SHORT}}. | [SALE70]; [BFEND] | groen |
| CTA | Add the lid now | [SALE70] | groen |
| Deadline-regel | Black Friday prices end {{DEADLINE}}. It ships free on its own, duties paid. | [BFEND]; [SHIPSEP] | groen |
| PS | P.S. Just ordered? Reply now. If your first order hasn't left, our team will try to combine them. | [SUPPORTMERGE] | oranje |

## pp-complete US en INT

- Berichten: pp-complete US (`TSmMky`, template `Xtdymw`), pp-complete INT (`QPTNAP`, template `UqKzBM`)
- Positie: 3,08 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: Complete your kitchen
- Huidige preview: Picked for what you just ordered, at 70% off.
- Huidige hero en CTA: Siraat Wok Pan Pro · knop: Wok Pan Pro, Get the Wok Pan Pro

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Complete your kitchen before {{DEADLINE_SHORT}}: up to 70% off | [SALE70]; [BFEND] | groen |
| Subject 2 | Picked for your order. Black Friday ends Nov 30. | [BFEND] | groen |
| Subject 3 | LAST CHANCE: complete your kitchen at Black Friday prices ⏰ | [BF48] | oranje |
| Preview 1 | Picked for what you just ordered. Up to 70% off and 5 free gifts until {{DEADLINE}}. | [SALE70]; [GIFTS5]; [BFEND] | groen |
| Preview 2 | Three pieces your pan can't replace. The price on all three ends {{DEADLINE}}. | [BFEND] | groen |
| Hero | Complete your kitchen.\|Before {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Complete my kitchen now | [SALE70] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. Each order gets its own 5 free gifts until {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |

## pp-twopans US en INT

- Berichten: pp-twopans US (`VAaqvD`, template `RnhAS4`), pp-twopans INT (`TaHunx`, template `YxZ8TY`)
- Positie: 21,08 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: Two pans, one dinner
- Huidige preview: The Pan Pro crisps, the Deep Pan Pro simmers. 40 minutes.
- Huidige hero en CTA: Siraat Pan Pro Standard · knop: Pan Pro Standard, Deep Pan Pro

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Two pans, one dinner. The second is on sale until Nov 30. | [BFEND]; mail gaat 21 dagen na de order, dus alleen voor orders tot 9 nov valt hij vóór 30 nov | groen |
| Subject 2 | Make this tonight. Second pan on sale until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| Subject 3 | ENDS TONIGHT: the Deep Pan Pro at Black Friday prices ⏰ | [BF30] | oranje |
| Preview 1 | The Pan Pro crisps, the Deep Pan Pro simmers. 40 minutes, and up to 70% off until {{DEADLINE}}. | [SALE70]; [BFEND] | groen |
| Preview 2 | One recipe, two pans. The second pan's Black Friday price ends {{DEADLINE}}. | [BFEND] | groen |
| Hero | Two pans, one dinner.\|Second pan on sale until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Get the Deep Pan Pro now | [SALE70] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. After {{DEADLINE}} the recipe still works. The price doesn't. | [BFEND] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your order is on hold until you add the lid | Verzonnen orderstatus. |
| Add it to your order (zonder order-edit of samenvoegen) | Shopify laat klanten geen items aan een geplaatste order toevoegen; het wordt een tweede order. Alleen met [UNSHIP]. |
| Last chance before your box is sealed | We weten niet wanneer de doos dichtgaat; nep-procesclaim. |
| Your 5 gifts are waiting for this add-on | De gifts zitten al bij de eerste order. |

## Voorwaarden in deze flow

- **[BF30]** de mail gaat uit op 30 nov (laatste BF-dag) en saleprijs, BFCODE en gifts stoppen echt op {{DEADLINE}}. In een flow alleen via een datumblok in onderwerp en hero ({% today %}-vergelijking, getest) of doordat Floris op 30 nov de onderwerpen omzet (PATCH flow-action) en op 1 dec terugzet; andere dagen valt de regel terug op de [BFEND]-versie
- **[BF48]** de mail gaat uit op 29 of 30 nov (laatste 48 uur van BF), zelfde datumblok als [BF30]; 'last chance' en 'final hours' alleen dan
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
- **[SHIPSEP]** een tweede order wordt los verzonden en krijgt zelf gratis verzending en de gifts; de copy belooft niet dat het in hetzelfde pakket zit
- **[SUPPORTMERGE]** support (Gorgias) kan een tweede order echt samenvoegen met een nog niet verzonden eerste order; Floris bevestigt
- **[UNSHIP]** de order van dit profiel staat op het verzendmoment nog op unfulfilled (verzendfilter Fulfilled Order = 0 sinds flowstart) EN er bestaat een echte manier om toe te voegen aan dezelfde zending (order-edit-link of supportteam voegt samen vóór fulfillment, getest). Zonder dat mechanisme niet waar
