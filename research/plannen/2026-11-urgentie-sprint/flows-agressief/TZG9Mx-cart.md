# TZG9Mx · v4 · Cart abandonment: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `TZG9Mx` (Metric), status live, 10 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 9.899 ontvangers (4.949 per week), $27.256 omzet, $2,75 per ontvanger, 3,72% unieke klik.
- Echte deadlines in deze flow: Echt nu: BFCODE (extra 10%) tot einde BF, 5 gifts tot einde BF, unieke 48-uurscode K3_10_48H in CODE · K3. Niets eindigt vandaag behalve op 30 nov. Sterkste echte hefboom: de 48-uurscode plus een nieuwe herinnering op +44 uur.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| K1 | 15 min na trigger | 3.822 | $4,81 | Your cart, at Black Friday prices | Your cart is still open: extra 10% + 5 free gifts | groen |
| K1-ACC | 15 min na trigger | 189 | $3,68 | Picked it out? Black Friday is live. | Picked it out? Your extra 10% ends {{DEADLINE_SHORT}} | groen |
| K2-RETURNING | 2,01 d na trigger | 240 | $6,43 | Adding to your Siraat kitchen? Black Friday is live. | Welcome back. Your cart's extra 10% ends {{DEADLINE_SHORT}} | groen |
| K2-NEW | 2,01 d na trigger | 2.897 | $1,46 | 15 coated pans, or one. Priced for Black Friday. | 15 coated pans, or one. Black Friday ends Nov 30. | groen |
| K3 nocode (pan en acc, cooldown en T02-B) | 4,01 d na trigger | 279 | $0,00 | What if it's not for you? | Last email about your cart: extra 10% ends {{DEADLINE_SHORT}} | groen |
| CODE · K3 (pan en acc) | 4,01 d na trigger | 2.472 | $0,98 | Your own 10%, on top of the sale, for 48 hours | Your own 10% expires in 48 hours | groen |
| NIEUW · K3-REM (voorstel, +44 uur na CODE · K3) | nieuwe stap | - | - | (nieuw) | Your 10% expires in {{HOURS_LEFT}} hours | groen |

## K1

- Berichten: K1 (`Vb6YFp`, template `Rp3mf6`)
- Positie: 15 min na trigger. 14 dagen: 3.822 ontvangers, $18.376 omzet, $4,81 per ontvanger.
- Huidig onderwerp: Your cart, at Black Friday prices
- Huidige preview: An extra 10% on top of the sale, applied with the button.
- Huidige hero en CTA: Still in your cart. Hammered for an easy wipe: less food touches the metal. No coating. 4 gifts pending, free shipping. · knop: Return to my cart

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your cart is still open: extra 10% + 5 free gifts | [CART]; [BFCODE]; [GIFTS5] | groen |
| Subject 2 | Your Black Friday cart: prices go up {{DEADLINE_SHORT}} | [CART]; [PRICEUP]; [BFEND] | groen |
| Subject 3 | Your cart prices go up at MIDNIGHT ⏰ | [CART]; [BF30]; [PRICEUP] | oranje. Eén caps-woord plus één emoji; alleen op 30 nov. |
| Preview 1 | An extra 10% on top of the sale, already applied with the button. It ends with Black Friday, {{DEADLINE}}. | [BFCODE]; [BFEND] | groen |
| Preview 2 | 5 free gifts are added at checkout. Order after {{DEADLINE}} and they're gone. | [GIFTS5]; [GIFTSEND] | groen |
| Hero | Still in your cart.\|Extra 10% until {{DEADLINE_SHORT}}. | [CART]; [BFCODE]; [BFEND] | groen |
| CTA | Check out before it ends | [BFEND] | groen |
| Deadline-regel | Your extra 10% and the 5 free gifts end {{DEADLINE}}. The cart itself doesn't hold the price. | [BFCODE]; [GIFTSEND]; [PRICEUP] | groen |
| PS | P.S. You get 30 days to return it. The extra 10% won't wait that long. | [RETURN30]; [BFEND] | groen |

## K1-ACC

- Berichten: K1-ACC (`SKE4yh`, template `WrMYnX`)
- Positie: 15 min na trigger. 14 dagen: 189 ontvangers, $696 omzet, $3,68 per ontvanger.
- Huidig onderwerp: Picked it out? Black Friday is live.
- Huidige preview: An extra 10% on top of Black Friday prices, applied with the button.
- Huidige hero en CTA: Still in your cart. Picked it out? It's still here. 4 gifts ship with it. · knop: Finish my order

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Picked it out? Your extra 10% ends {{DEADLINE_SHORT}} | [CART]; [BFCODE]; [BFEND] | groen |
| Subject 2 | Your cart is still open, with 5 free gifts | [CART]; [GIFTS5] | groen |
| Subject 3 | ENDS TONIGHT: extra 10% on your cart ⏰ | [CART]; [BF30] | oranje |
| Preview 1 | An extra 10% on top of Black Friday prices, applied with the button, until {{DEADLINE}}. | [BFCODE]; [BFEND] | groen |
| Preview 2 | Add a pan before {{DEADLINE}} and the extra 10% counts on that too. | [BFCODE] werkt op de hele cart (Shopify-instelling controleren) | groen |
| Hero | Your pick, extra 10% off.\|Until {{DEADLINE_SHORT}}. | [BFCODE]; [BFEND] | groen |
| CTA | Get my extra 10% now | [BFCODE] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. Accessory today, pan later? Later means regular price, after {{DEADLINE}}. | [BFEND] | groen |

## K2-RETURNING

- Berichten: K2-RETURNING (`TV4Ts9`, template `T9seB4`)
- Positie: 2,01 d na trigger. 14 dagen: 240 ontvangers, $1.544 omzet, $6,43 per ontvanger.
- Huidig onderwerp: Adding to your Siraat kitchen? Black Friday is live.
- Huidige preview: You know how it works. Your cart is saved, with an extra 10% on top of the sale.
- Huidige hero en CTA: Welcome back. You know this pan. Same titanium, same 4 gifts. · knop: Finish my order, Stainless Steel Lid

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Welcome back. Your cart's extra 10% ends {{DEADLINE_SHORT}} | [CART]; [BFCODE]; [BFEND] | groen |
| Subject 2 | You know how it works. Order before Nov 30. | [BFEND] | groen |
| Subject 3 | LAST CHANCE: your Siraat cart at Black Friday prices ⏰ | [CART]; [BF48] | oranje |
| Preview 1 | Your cart is saved, with an extra 10% on top of the sale until {{DEADLINE}}. | [CART] (cartlink herstelt de items); [BFCODE] | groen |
| Preview 2 | Same titanium, same 5 free gifts. Gone after {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |
| Hero | Welcome back.\|Extra 10% until {{DEADLINE_SHORT}}. | [BFCODE]; [BFEND] | groen |
| CTA | Finish my order now | [CART] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. Your first pan is covered for 75 years. This price is covered until {{DEADLINE}}. | [W75]; [BFEND] | groen |

## K2-NEW

- Berichten: K2-NEW (`Ti3QPw`, template `YccRJV`)
- Positie: 2,01 d na trigger. 14 dagen: 2.897 ontvangers, $4.227 omzet, $1,46 per ontvanger.
- Huidig onderwerp: 15 coated pans, or one. Priced for Black Friday.
- Huidige preview: Our warranty runs 75 years. Here is the math, with an extra 10% on top of the sale.
- Huidige hero en CTA: The real price. 15 coated pans, or one. Covered for 75 years, nothing to wear off. 4 gifts pending. · knop: Finish my order, What the warranty covers

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | 15 coated pans, or one. Black Friday ends Nov 30. | [BFEND]; rekensom staat al in de huidige mail | groen |
| Subject 2 | Our warranty runs 75 years. Your extra 10% runs out {{DEADLINE_SHORT}}. | [W75]; [BFCODE]; [BFEND] | groen |
| Subject 3 | Your cart's extra 10% ends TONIGHT ⏰ | [CART]; [BF30] | oranje |
| Preview 1 | Here is the math, with an extra 10% and 5 free gifts until {{DEADLINE}}. | [BFCODE]; [GIFTS5]; [BFEND] | groen |
| Preview 2 | One pan for 75 years. One price until {{DEADLINE}}. | [W75]; [BFEND] | groen |
| Hero | 75 years of cover.\|10% extra until {{DEADLINE_SHORT}}. | [W75]; [BFCODE]; [BFEND] | groen |
| CTA | Finish my order before it ends | [BFEND] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. The warranty doesn't expire for 75 years. The extra 10% expires {{DEADLINE}}. | [W75]; [BFCODE]; [BFEND] | groen |

## K3 nocode (pan en acc, cooldown en T02-B)

- Berichten: K3 · pan nocode · cooldown (`UZQtYB`, template `SzCGdE`), K3 · pan nocode · T02-B (`WbfiSt`, template `YxUpdd`), K3 · acc nocode · cooldown (`WSTBQu`, template `UgQ5kp`), K3 · acc nocode · T02-B (`Xrhq7H`, template `U5yyv6`)
- Positie: 4,01 d na trigger. 14 dagen: 279 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: What if it's not for you?
- Huidige preview: Then it goes back unused within 30 days. An extra 10% on top of the sale, with the button.
- Huidige hero en CTA: Last email. What if it's not for you? 30 days to change your mind. 4 gifts pending. · knop: Finish my order

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Last email about your cart: extra 10% ends {{DEADLINE_SHORT}} | [LASTFLOW]; [BFCODE]; [BFEND] | groen |
| Subject 2 | Not for you? 30 days to send it back. Order before Nov 30. | [RETURN30]; [BFEND] | groen |
| Subject 3 | FINAL REMINDER: your cart at Black Friday prices ⏰ | [LASTFLOW]; [CART] | oranje. Caps op twee woorden. |
| Preview 1 | Then it goes back unused within 30 days. The extra 10% is gone after {{DEADLINE}}. | [RETURN30]; [BFCODE]; [BFEND] | groen |
| Preview 2 | This is the last reminder about this cart. The sale under it ends {{DEADLINE}}. | [LASTFLOW]; [BFEND] | groen |
| Hero | Last email.\|Order before {{DEADLINE_SHORT}}, decide at home. | [LASTFLOW]; [RETURN30]; [BFEND] | groen |
| CTA | Order now, decide at home | [RETURN30] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. No more reminders after this one. After {{DEADLINE}} this cart is regular price. | [LASTFLOW]; [PRICEUP] | groen |

## CODE · K3 (pan en acc)

- Berichten: CODE · K3 · pan (`SApxRv`, template `RC6Cdt`), CODE · K3 · acc (`TQrD6K`, template `VE7F7U`)
- Positie: 4,01 d na trigger. 14 dagen: 2.472 ontvangers, $2.413 omzet, $0,98 per ontvanger.
- Huidig onderwerp: Your own 10%, on top of the sale, for 48 hours
- Huidige preview: Already applied, on top of Black Friday prices. In 48 hours we remove the code.
- Huidige hero en CTA: Last email, 48 hours. Your 10% comes off soon: we're removing it in 48 hours. Your own code is already applied. · knop: Use my 10% now

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your own 10% expires in 48 hours | [CODE48]; [NOW] | groen |
| Subject 2 | YOUR CODE EXPIRES {{DEADLINE_SHORT}} ⏰ | [CODE48] | oranje. Drie caps-woorden: grens; liever 'Your code expires {{DEADLINE_SHORT}}'. |
| Subject 3 | Use it or lose it: your own 10% on this cart | [CODE48] | oranje. Verliesframing, waar omdat de code echt vervalt. |
| Preview 1 | Already applied, on top of Black Friday prices. On {{DEADLINE}} we remove it. | [CODE48] | groen |
| Preview 2 | One code, one use, made for this cart. After 48 hours it stops working. | [CODE48] | groen |
| Hero | Your own 10%.\|Gone {{DEADLINE_SHORT}}. | [CODE48] | groen |
| CTA | Use my 10% before it expires | [CODE48] | groen |
| Deadline-regel | Your code expires {{DEADLINE}}. After that the regular sale price applies. | [CODE48] | groen |
| PS | P.S. Black Friday prices run until Nov 30. This 10% on top doesn't. | [CODE48]; [BFEND] | groen |

## NIEUW · K3-REM (voorstel, +44 uur na CODE · K3)

- Berichten: geen (voorstel voor een nieuwe flowstap).
- Huidig onderwerp: (nieuw)
- Huidige preview: (nieuw)
- Huidige hero en CTA: (geen hero-beeld; tekstmail) · knop: (geen knop gevonden)
- Noot: Nieuwe stap; bestaat niet in Klaviyo. Grootste echte urgentie in de flow.

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your 10% expires in {{HOURS_LEFT}} hours | [CODEREM] | groen |
| Subject 2 | Order now: {{MINUTES_LEFT}} minutes left on your 10% | [CODEREM]; [MINS] | rood. Alleen met live GIF; als tekst veroudert hij in de inbox. |
| Subject 3 | FINAL HOURS: your cart code ⏰ | [CODEREM] | oranje |
| Preview 1 | Your own code stops working {{DEADLINE}}. Still applied with the button. | [CODEREM] | groen |
| Preview 2 | After this, no more reminders. Just the regular sale price. | [CODEREM]; [LASTFLOW] | groen |
| Hero | {{HOURS_LEFT}} hours left\|on your 10%. | [CODEREM] | groen |
| CTA | Use my 10% now | [CODEREM] | groen |
| Deadline-regel | Expires {{DEADLINE}}. | [CODEREM]; optioneel live GIF [MINS] | groen |
| PS | P.S. Decided against it? Ignore this. It's the last one. | [LASTFLOW] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your cart is reserved / we're holding your cart / price held | Verboden (DECISIONS 1 nov, BRIEF). De Shopify-cart houdt geen prijs vast. |
| Your cart expires at midnight | De cart vervalt niet. Wel waar op 30 nov: 'Your cart prices go up at midnight' ([BF30] + [PRICEUP]). |
| Your order is pending / will be canceled | Er bestaat geen order; nep-orderstatus (FTC Act sectie 5, CAN-SPAM). |
| Only 3 left / almost sold out | Geen echte voorraaddata per variant in de flow; valse schaarste. |
| We extended your discount 24 hours, it cannot be extended again | Verzonnen verlenging; BRIEF verbiedt 'no extensions'. |
| Your code expires tonight (in een 48-uurs codemail op het moment van uitgifte) | Op het uitgiftemoment zijn het nog 48 uur. Alleen waar in de nieuwe herinneringsstap [CODEREM]. |

## Voorwaarden in deze flow

- **[BF30]** de mail gaat uit op 30 nov (laatste BF-dag) en saleprijs, BFCODE en gifts stoppen echt op {{DEADLINE}}. In een flow alleen via een datumblok in onderwerp en hero ({% today %}-vergelijking, getest) of doordat Floris op 30 nov de onderwerpen omzet (PATCH flow-action) en op 1 dec terugzet; andere dagen valt de regel terug op de [BFEND]-versie
- **[BF48]** de mail gaat uit op 29 of 30 nov (laatste 48 uur van BF), zelfde datumblok als [BF30]; 'last chance' en 'final hours' alleen dan
- **[BFCODE]** BFCODE (extra 10% bovenop de sale, alleen abandonment) staat in de knoplink en werkt op het verzendmoment; BFCODE stopt met BF, dus de einddatum is [BFEND]
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[CART]** echte Added to Cart van dit profiel en geen order sinds flowstart (flowfilter RSNxYV = 0 staat erin); de knop herstelt de cart
- **[CODE48]** unieke Klaviyo-code (K3_10_48H, C4_10_48H of B2_10_48H, one use) vervalt in Shopify echt 48 uur na uitgifte; {{DEADLINE}} = days_later:2 met het uur van de coupon-instelling (template zegt nu 'expires on the morning of', dus uur controleren); {{DEADLINE_SHORT}} = weekdag
- **[CODEREM]** NIEUWE flowstap (bestaat nu niet): herinnering op uitgifte + 44 tot 46 uur, alleen als de code ongebruikt is (Placed Order = 0 sinds flowstart); {{HOURS_LEFT}} = echte uren tot de coupon-einde
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[LASTFLOW]** dit is echt de laatste mail van deze flow voor dit profiel (geen stap meer erna)
- **[MINS]** {{MINUTES_LEFT}} alleen naast een live countdown-GIF (Sendtric/NiftyImages) die naar de echte backend-eindtijd telt en daarna ENDED toont; als statische tekst nooit
- **[NOW]** de flowmail gaat uit op het moment dat de trigger valt (geen 'local time'-verschuiving), dus relatieve tijd klopt
- **[PRICEUP]** de producten in deze cart/checkout gaan op {{DEADLINE}} echt terug naar de normale prijs (einde BF). De Shopify-cart zelf vervalt niet en houdt geen prijs vast; de regel gaat over de prijs, nooit over de cart
- **[RETURN30]** 30 dagen retour vanaf bezorging, ongebruikt (DECISIONS 1 okt)
- **[W75]** 75 jaar garantie (DECISIONS 1 okt)
