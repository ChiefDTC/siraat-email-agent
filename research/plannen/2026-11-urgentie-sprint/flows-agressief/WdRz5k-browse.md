# WdRz5k · v4 · Browse abandonment: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `WdRz5k` (Metric), status live, 11 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 12.676 ontvangers (6.338 per week), $11.097 omzet, $0,88 per ontvanger, 2,87% unieke klik.
- Echte deadlines in deze flow: Echt nu: BFCODE tot einde BF, 5 gifts tot einde BF, B2_10_48H (48 uur) in CODE · B2. Hoog volume, lage RPR: de deadline moet de klik halen, niet de open.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | 1 u na trigger | 7.238 | $1,12 | Get this pan with 10% off | The pan you looked at: extra 10% until {{DEADLINE_SHORT}} | groen |
| B1-ACC | 1 u na trigger | 247 | $1,01 | Looked twice? Black Friday is live. | Looked twice? Extra 10% ends {{DEADLINE_SHORT}}. | groen |
| B2-CLICKED nocode (pan en acc, cooldown en T02-B) | 2,04 d na trigger | 71 | $0,00 | "I ordered one pan to try it out" | "I ordered one pan to try it out" (Black Friday ends Nov 30) | groen |
| B2-NOTCLICKED | 2,04 d na trigger | 5.048 | $0,47 | Skeptical? So were they. | Skeptical? So were they. Black Friday ends Nov 30. | groen |
| CODE · B2-CLICKED (pan en acc) | 2,04 d na trigger | 72 | $4,77 | Your own 10%, on top of Black Friday prices | Your own 10% expires in 48 hours | groen |
| NIEUW · B2-REM (voorstel, +44 uur na CODE · B2) | nieuwe stap | - | - | (nieuw) | Your 10% expires in {{HOURS_LEFT}} hours | groen |

## B1

- Berichten: B1 [AB0] (`UXPtQ6`, template `Wn3U5P`), B1 Test #1 October 08, 2026 Variation A [AB1] (`YyFeR4`, template `R6E5Zv`), B1 · BR1-B · sale-prijs (vanaf 28 okt) [AB2] (`UkNrdt`, template `Ye4tQy`)
- Positie: 1 u na trigger. 14 dagen: 7.238 ontvangers, $8.120 omzet, $1,12 per ontvanger.
- Huidig onderwerp: Get this pan with 10% off
- Huidige preview: Two years ago I read about PFAS. This pan is what came out of it.
- Huidige hero en CTA: The pan you viewed: this pan, 10% off. No PFAS, Light Labs report no. 25895. Extra 10% off with code BFCODE, plus 4 free gifts. · knop: Report no. 25895, read it yourself

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

## B1-ACC

- Berichten: B1-ACC (`XiD9BN`, template `VTwW7c`)
- Positie: 1 u na trigger. 14 dagen: 247 ontvangers, $250 omzet, $1,01 per ontvanger.
- Huidig onderwerp: Looked twice? Black Friday is live.
- Huidige preview: An extra 10% on top of Black Friday prices, applied with the button.
- Huidige hero en CTA: You had a look. Looked twice? Here is the detail. Extra 10% off with code BFCODE, plus 4 free gifts. · knop: Get 10% off this piece

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

## B2-CLICKED nocode (pan en acc, cooldown en T02-B)

- Berichten: B2-CLICKED · pan nocode · cooldown (`UgbaS5`, template `RDD8j6`), B2-CLICKED · pan nocode · T02-B (`T295CP`, template `SGpGH3`), B2-CLICKED · acc nocode · cooldown (`XR2VT3`, template `TgNv8M`), B2-CLICKED · acc nocode · T02-B (`VXXN3a`, template `UZcnke`)
- Positie: 2,04 d na trigger. 14 dagen: 71 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: "I ordered one pan to try it out"
- Huidige preview: Sunny C. started with one. An extra 10% on top of the sale, with the button.
- Huidige hero en CTA: In their words: I ordered one pan to try it out. Sunny C., verified buyer. 4 free gifts with every order, free shipping. · knop: (geen knop gevonden)

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

## B2-NOTCLICKED

- Berichten: B2-NOTCLICKED (`Yu3YvE`, template `VyZUHC`)
- Positie: 2,04 d na trigger. 14 dagen: 5.048 ontvangers, $2.383 omzet, $0,47 per ontvanger.
- Huidig onderwerp: Skeptical? So were they.
- Huidige preview: One thought it was a scam. One is on her fourth pan. An extra 10% on top of the sale.
- Huidige hero en CTA: In their words. Skeptical? So were they. From the first doubt to the fourth pan. Extra 10% off with code BFCODE, plus 4 free gifts. · knop: (geen knop gevonden)

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Skeptical? So were they. Black Friday ends Nov 30. | [BFEND] | groen |
| Subject 2 | One thought it was a scam. Decide before {{DEADLINE_SHORT}}. | [REVIEW]; [BFEND] | groen |
| Subject 3 | LAST CHANCE: up to 70% off for the skeptics ⏰ | [BF48]; [SALE70] | oranje |
| Preview 1 | One is on her fourth pan. Extra 10% on top of the sale until {{DEADLINE}}. | [REVIEW]; [BFCODE]; [BFEND] | groen |
| Preview 2 | 100,000+ customers, 30-day returns, 75-year warranty. The price ends {{DEADLINE}}. | [RETURN30]; [W75]; [BFEND] | groen |
| Hero | Skeptical first.\|10% extra until {{DEADLINE_SHORT}}. | [BFCODE]; [BFEND] | groen |
| CTA | Get it before the price ends | [BFEND] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. Still skeptical after it arrives? 30 days to send it back. | [RETURN30] | groen |

## CODE · B2-CLICKED (pan en acc)

- Berichten: CODE · B2-CLICKED · pan (`XdZTgq`, template `XRNAkP`), CODE · B2-CLICKED · acc (`Sp832c`, template `YcURLK`)
- Positie: 2,04 d na trigger. 14 dagen: 72 ontvangers, $344 omzet, $4,77 per ontvanger.
- Huidig onderwerp: Your own 10%, on top of Black Friday prices
- Huidige preview: Already applied. In 48 hours we remove it, then the regular sale price applies.
- Huidige hero en CTA: Your code, 48 hours. Your own 10% expires soon, then the regular sale price is back. · knop: Use my 10% now

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

## NIEUW · B2-REM (voorstel, +44 uur na CODE · B2)

- Berichten: geen (voorstel voor een nieuwe flowstap).
- Huidig onderwerp: (nieuw)
- Huidige preview: (nieuw)
- Huidige hero en CTA: (geen hero-beeld; tekstmail) · knop: (geen knop gevonden)
- Noot: Nieuwe stap; bestaat niet in Klaviyo.

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your 10% expires in {{HOURS_LEFT}} hours | [CODEREM] | groen |
| Subject 2 | Order now: {{MINUTES_LEFT}} minutes left on your 10% | [CODEREM]; [MINS] | rood |
| Subject 3 | FINAL HOURS: 10% on the pan you looked at ⏰ | [CODEREM] | oranje |
| Preview 1 | Your own code stops working {{DEADLINE}}. Still applied with the button. | [CODEREM] | groen |
| Preview 2 | After this, the regular sale price. No more reminders. | [CODEREM]; [LASTFLOW] | groen |
| Hero | {{HOURS_LEFT}} hours left\|on your 10%. | [CODEREM] | groen |
| CTA | Use my 10% now | [CODEREM] | groen |
| Deadline-regel | Expires {{DEADLINE}}. | [CODEREM] | groen |
| PS | P.S. It's the last one about this pan. | [LASTFLOW] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your order is pending / will be canceled | Er bestaat geen order; nep-orderstatus (FTC Act sectie 5, CAN-SPAM). |
| Only 3 left / almost sold out | Geen echte voorraaddata per variant in de flow; valse schaarste. |
| We extended your discount 24 hours, it cannot be extended again | Verzonnen verlenging; BRIEF verbiedt 'no extensions'. |
| Your code expires tonight (in een 48-uurs codemail op het moment van uitgifte) | Op het uitgiftemoment zijn het nog 48 uur. Alleen waar in de nieuwe herinneringsstap [CODEREM]. |
| Still looking? It's almost gone | Geen voorraaddata per product; valse schaarste. |

## Voorwaarden in deze flow

- **[BF30]** de mail gaat uit op 30 nov (laatste BF-dag) en saleprijs, BFCODE en gifts stoppen echt op {{DEADLINE}}. In een flow alleen via een datumblok in onderwerp en hero ({% today %}-vergelijking, getest) of doordat Floris op 30 nov de onderwerpen omzet (PATCH flow-action) en op 1 dec terugzet; andere dagen valt de regel terug op de [BFEND]-versie
- **[BF48]** de mail gaat uit op 29 of 30 nov (laatste 48 uur van BF), zelfde datumblok als [BF30]; 'last chance' en 'final hours' alleen dan
- **[BFCODE]** BFCODE (extra 10% bovenop de sale, alleen abandonment) staat in de knoplink en werkt op het verzendmoment; BFCODE stopt met BF, dus de einddatum is [BFEND]
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[CODE48]** unieke Klaviyo-code (K3_10_48H, C4_10_48H of B2_10_48H, one use) vervalt in Shopify echt 48 uur na uitgifte; {{DEADLINE}} = days_later:2 met het uur van de coupon-instelling (template zegt nu 'expires on the morning of', dus uur controleren); {{DEADLINE_SHORT}} = weekdag
- **[CODEREM]** NIEUWE flowstap (bestaat nu niet): herinnering op uitgifte + 44 tot 46 uur, alleen als de code ongebruikt is (Placed Order = 0 sinds flowstart); {{HOURS_LEFT}} = echte uren tot de coupon-einde
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[LASTFLOW]** dit is echt de laatste mail van deze flow voor dit profiel (geen stap meer erna)
- **[MINS]** {{MINUTES_LEFT}} alleen naast een live countdown-GIF (Sendtric/NiftyImages) die naar de echte backend-eindtijd telt en daarna ENDED toont; als statische tekst nooit
- **[NOW]** de flowmail gaat uit op het moment dat de trigger valt (geen 'local time'-verschuiving), dus relatieve tijd klopt
- **[RETURN30]** 30 dagen retour vanaf bezorging, ongebruikt (DECISIONS 1 okt)
- **[REVIEW]** de geciteerde review staat letterlijk en geverifieerd in de huidige template (naam en ID)
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
- **[W75]** 75 jaar garantie (DECISIONS 1 okt)
