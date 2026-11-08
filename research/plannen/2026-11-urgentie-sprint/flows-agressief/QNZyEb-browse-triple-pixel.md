# QNZyEb · v4 · Browse abandonment · Triple Pixel: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `QNZyEb` (Metric), status live, 8 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 1.918 ontvangers (959 per week), $648 omzet, $0,34 per ontvanger, 3,13% unieke klik.
- Echte deadlines in deze flow: Zelfde mechaniek als WdRz5k (BFCODE, gifts, B2_10_48H). Kleiner volume; copy gelijk houden aan WdRz5k zodat de samenvoeging (BACKLOG 3) één set onderwerpen heeft.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| TP · B1 | 1 u na trigger | 1.527 | $0,39 | The pan you looked at, priced for Black Friday | The pan you looked at: extra 10% until {{DEADLINE_SHORT}} | groen |
| TP · B1-ACC | 1 u na trigger | 92 | $0,00 | Looked twice? Black Friday is live. | Looked twice? Extra 10% ends {{DEADLINE_SHORT}}. | groen |
| TP · B2-CLICKED nocode (pan en acc, cooldown en T02-B) | 2,04 d na trigger | 14 | $0,00 | "I ordered one pan to try it out" | "I ordered one pan to try it out" (Black Friday ends Nov 30) | groen |
| TP · CODE · B2-CLICKED (pan en acc) | 2,04 d na trigger | 12 | $4,43 | Your own 10%, on top of Black Friday prices | Your own 10% expires in 48 hours | groen |

## TP · B1

- Berichten: TP · B1 (`UpRjF9`, template `TY9hCH`)
- Positie: 1 u na trigger. 14 dagen: 1.527 ontvangers, $594 omzet, $0,39 per ontvanger.
- Huidig onderwerp: The pan you looked at, priced for Black Friday
- Huidige preview: Here it is again, with the lab report, the 75-year warranty and an extra 10% on top of the sale.
- Huidige hero en CTA: {{ event.Name / default:'Titanium Hammered Pan Pro' }} · knop: Read report no. 25895 yourself

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | The pan you looked at: extra 10% until {{DEADLINE_SHORT}} | [BFCODE]; [BFEND] | groen |
| Subject 2 | Still thinking? Black Friday ends Nov 30. | [BFEND] | groen |
| Subject 3 | ENDS TONIGHT: the pan you looked at, up to 70% off ⏰ | [BF30]; [SALE70] | oranje |
| Preview 1 | Up to 70% off, plus an extra 10% with the button, until {{DEADLINE}}. | [SALE70]; [BFCODE]; [BFEND] | groen |
| Preview 2 | Here it is again, with the lab report and 5 free gifts. The price ends {{DEADLINE}}. | [GIFTS5]; [BFEND] | groen |
| Hero | The one you looked at.\|Extra 10% until {{DEADLINE_SHORT}}. | [BFCODE]; [BFEND] | groen |
| CTA | Get this pan before it ends | [BFEND] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. 5 free gifts with every order until {{DEADLINE}}. After that, none. | [GIFTS5]; [GIFTSEND] | groen |

## TP · B1-ACC

- Berichten: TP · B1-ACC (`RYqpy3`, template `SVXXh8`)
- Positie: 1 u na trigger. 14 dagen: 92 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: Looked twice? Black Friday is live.
- Huidige preview: Here it is again. What it's made of, and an extra 10% on top of the sale.
- Huidige hero en CTA: {{ event.Name / default:'Titanium Hammered Pan Pro' }} · knop: The Pan Pro, 11″28 cm28 cm (11″), Get 10% off this pan

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Looked twice? Extra 10% ends {{DEADLINE_SHORT}}. | [BFCODE]; [BFEND] | groen |
| Subject 2 | Looked twice. Black Friday is live until Nov 30. | [SALE70]; [BFEND] | groen |
| Subject 3 | LAST CHANCE: what you looked at, plus 10% ⏰ | [BF48]; [BFCODE] | oranje |
| Preview 1 | An extra 10% on top of Black Friday prices, applied with the button, until {{DEADLINE}}. | [BFCODE]; [BFEND] | groen |
| Preview 2 | What it's made of, and why the price ends {{DEADLINE}}. | [BFEND] | groen |
| Hero | Looked twice.\|Extra 10% until {{DEADLINE_SHORT}}. | [BFCODE]; [BFEND] | groen |
| CTA | Get my extra 10% now | [BFCODE] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. Add a pan before {{DEADLINE}} and the extra 10% counts on that too. | [BFCODE] werkt op de hele cart | groen |

## TP · B2-CLICKED nocode (pan en acc, cooldown en T02-B)

- Berichten: TP · B2-CLICKED · pan nocode · cooldown (`URBRAY`, template `SPjGMd`), TP · B2-CLICKED · pan nocode · T02-B (`SmxF8u`, template `QPCirr`), TP · B2-CLICKED · acc nocode · cooldown (`UeANYm`, template `W5EsqB`), TP · B2-CLICKED · acc nocode · T02-B (`TsjfEW`, template `Ut6jDg`)
- Positie: 2,04 d na trigger. 14 dagen: 14 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: "I ordered one pan to try it out"
- Huidige preview: If you change your mind, or if something is wrong. Both are covered. Extra 10% on top of the sale.
- Huidige hero en CTA: {{ event.Name / default:'Titanium Hammered Pan Pro' }} · knop: Get mine + 4 gifts

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | "I ordered one pan to try it out" (Black Friday ends Nov 30) | [REVIEW]; [BFEND] | groen |
| Subject 2 | Try one pan. 30 days to return it. Order by {{DEADLINE_SHORT}}. | [RETURN30]; [BFEND] | groen |
| Subject 3 | ENDS TONIGHT: try one pan with an extra 10% ⏰ | [BF30]; [BFCODE] | oranje |
| Preview 1 | She started with one. Extra 10% on top of the sale until {{DEADLINE}}. | [REVIEW]; [BFCODE]; [BFEND] | groen |
| Preview 2 | If you change your mind, it's covered. If you wait past {{DEADLINE}}, the price isn't. | [RETURN30]; [BFEND] | groen |
| Hero | Start with one.\|Extra 10% until {{DEADLINE_SHORT}}. | [BFCODE]; [BFEND] | groen |
| CTA | Try one pan now | [BFCODE] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. Returns have 30 days. The Black Friday price has until {{DEADLINE}}. | [RETURN30]; [BFEND] | groen |

## TP · CODE · B2-CLICKED (pan en acc)

- Berichten: TP · CODE · B2-CLICKED · pan (`ULYBfA`, template `QQdytM`), TP · CODE · B2-CLICKED · acc (`X7Nh3i`, template `QXt524`)
- Positie: 2,04 d na trigger. 14 dagen: 12 ontvangers, $53 omzet, $4,43 per ontvanger.
- Huidig onderwerp: Your own 10%, on top of Black Friday prices
- Huidige preview: Already applied with the button. In 48 hours we remove it, then the regular sale price applies.
- Huidige hero en CTA: {{ event.Name / default:'Titanium Hammered Pan Pro' }} · knop: Use my 10% now

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your own 10% expires in 48 hours | [CODE48]; [NOW] | groen |
| Subject 2 | Use it or lose it: 10% on the pan you looked at ⏰ | [CODE48] | oranje |
| Subject 3 | YOUR CODE ENDS {{DEADLINE_SHORT}} | [CODE48] | oranje |
| Preview 1 | Already applied. On {{DEADLINE}} we remove it, then the regular sale price applies. | [CODE48] | groen |
| Preview 2 | One use, made for you, gone in 48 hours. | [CODE48] | groen |
| Hero | Your own 10%.\|Gone {{DEADLINE_SHORT}}. | [CODE48] | groen |
| CTA | Use my 10% before it expires | [CODE48] | groen |
| Deadline-regel | Your code expires {{DEADLINE}}. After that the regular sale price applies. | [CODE48] | groen |
| PS | P.S. The sale runs to Nov 30. Your 10% on top runs to {{DEADLINE}}. | [CODE48]; [BFEND] | groen |

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
- **[CODE48]** unieke Klaviyo-code (K3_10_48H, C4_10_48H of B2_10_48H, one use) vervalt in Shopify echt 48 uur na uitgifte; {{DEADLINE}} = days_later:2 met het uur van de coupon-instelling (template zegt nu 'expires on the morning of', dus uur controleren); {{DEADLINE_SHORT}} = weekdag
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[NOW]** de flowmail gaat uit op het moment dat de trigger valt (geen 'local time'-verschuiving), dus relatieve tijd klopt
- **[RETURN30]** 30 dagen retour vanaf bezorging, ongebruikt (DECISIONS 1 okt)
- **[REVIEW]** de geciteerde review staat letterlijk en geverifieerd in de huidige template (naam en ID)
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
