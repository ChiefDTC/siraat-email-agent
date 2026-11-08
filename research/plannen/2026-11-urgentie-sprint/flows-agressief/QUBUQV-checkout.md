# QUBUQV · v4 · Checkout abandonment: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `QUBUQV` (Metric), status live, 9 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 4.808 ontvangers (2.404 per week), $22.921 omzet, $4,77 per ontvanger, 3,68% unieke klik.
- Echte deadlines in deze flow: Echt nu: echte Started Checkout, BFCODE tot einde BF, 5 gifts tot einde BF, unieke 48-uurscode C4_10_48H in CODE · C4. Hoogste RPR van alle flows; elke echte deadline telt hier het zwaarst.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | 10 min na trigger | 1.693 | $10,21 | Your cart, at Black Friday prices | Your checkout is still open: extra 10% applied | groen |
| C2 | 1,01 d na trigger | 1.095 | $4,18 | Tested, and now priced for Black Friday | Tested, and still in your checkout. Ends {{DEADLINE_SHORT}}. | groen |
| C2-ACC | 1,01 d na trigger | 135 | $0,00 | Yours, or a gift? Priced for Black Friday. | Yours, or a gift? Order by {{DEADLINE_SHORT}}. | groen |
| C3-S | 3,01 d na trigger | 232 | $0,00 | Your set, priced for Black Friday | Your set, at Black Friday prices until {{DEADLINE_SHORT}} | groen |
| C3-P | 3,01 d na trigger | 610 | $0,49 | One pan, or three? Black Friday is live. | One pan, or three? Decide before {{DEADLINE_SHORT}}. | groen |
| C3-ACC | 3,01 d na trigger | 113 | $0,00 | The pan we made after the board, priced for Black Friday | The pan we made after the board. Black Friday ends Nov 30. | groen |
| C4 nocode (cooldown en T02-B) | 5,01 d na trigger | 100 | $0,00 | Last email about your Black Friday cart | Last email about your checkout. Ends {{DEADLINE_SHORT}}. | groen |
| CODE · C4 | 5,01 d na trigger | 830 | $0,92 | Your own 10%, on top of Black Friday prices | Your own 10% expires in 48 hours | groen |
| NIEUW · C4-REM (voorstel, +44 uur na CODE · C4) | nieuwe stap | - | - | (nieuw) | Your 10% expires in {{HOURS_LEFT}} hours | groen |

## C1

- Berichten: C1 (`WhTznn`, template `Udgz6f`)
- Positie: 10 min na trigger. 14 dagen: 1.693 ontvangers, $17.284 omzet, $10,21 per ontvanger.
- Huidig onderwerp: Your cart, at Black Friday prices
- Huidige preview: An extra 10% on top of the sale, applied with the button. Your 4 gifts are still pending.
- Huidige hero en CTA: Still pending: your set, plus 4 gifts. / Still pending: your cart, plus 4 gifts. / Saved at the last step, one tap left. 4 gifts pending, free shipping. · knop: Complete my order

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your checkout is still open: extra 10% applied | [CHECKOUT]; [BFCODE] | groen |
| Subject 2 | One click left. Extra 10% ends {{DEADLINE_SHORT}}. | [CHECKOUT]; [BFCODE]; [BFEND] | groen |
| Subject 3 | Your checkout prices go up at MIDNIGHT ⏰ | [CHECKOUT]; [BF30]; [PRICEUP] | oranje |
| Preview 1 | An extra 10% on top of the sale, applied with the button. 5 free gifts on this order until {{DEADLINE}}. | [BFCODE]; [GIFTS5]; [BFEND] | groen |
| Preview 2 | Finish in one click. Black Friday prices end {{DEADLINE}}. | [CHECKOUT]; [BFEND] | groen |
| Hero | One click left.\|Extra 10% until {{DEADLINE_SHORT}}. | [CHECKOUT]; [BFCODE]; [BFEND] | groen |
| CTA | Complete my order now | [CHECKOUT] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. Your 5 free gifts are added to this checkout. Complete it before {{DEADLINE}} to get them. | [GIFTS5] (gift-app voegt ze toe in de checkout); [GIFTSEND] | oranje. Controleer dat de gifts echt in de checkout staan, niet pas na de order. |

## C2

- Berichten: C2 (`RZpvpp`, template `QUUPik`)
- Positie: 1,01 d na trigger. 14 dagen: 1.095 ontvangers, $4.576 omzet, $4,18 per ontvanger.
- Huidig onderwerp: Tested, and now priced for Black Friday
- Huidige preview: Why I had our pan lab-tested. Plus an extra 10% on top of the sale.
- Huidige hero en CTA: Tested, not claimed. Non-toxic is easy to say. Here's the paper: Light Labs report no. 25895. 4 gifts still pending on your cart. · knop: Complete my order, Read report no. 25895

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Tested, and still in your checkout. Ends {{DEADLINE_SHORT}}. | [CHECKOUT]; [BFEND] | groen |
| Subject 2 | Report no. 25895, plus an extra 10% until Nov 30 | [BFCODE]; [BFEND] | groen |
| Subject 3 | LAST CHANCE: your checkout at Black Friday prices ⏰ | [CHECKOUT]; [BF48] | oranje |
| Preview 1 | Why I had our pan lab-tested. Your checkout is still open, extra 10% until {{DEADLINE}}. | [CHECKOUT]; [BFCODE] | groen |
| Preview 2 | No PFAS, here's the paper. The extra 10% ends with Black Friday. | [BFCODE]; [BFEND] | groen |
| Hero | Tested, not claimed.\|Your checkout, still open. | [CHECKOUT] | groen |
| CTA | Complete my order now | [CHECKOUT] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. The lab report doesn't expire. The Black Friday price does, {{DEADLINE}}. | [BFEND] | groen |

## C2-ACC

- Berichten: C2-ACC (`UXedMJ`, template `Yp8nzj`)
- Positie: 1,01 d na trigger. 14 dagen: 135 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: Yours, or a gift? Priced for Black Friday.
- Huidige preview: An extra 10% on top of Black Friday prices, applied with the button.
- Huidige hero en CTA: Still in your cart. Yours, or a gift? Both work. 4 gifts ship with it, either way. · knop: Complete my order

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Yours, or a gift? Order by {{DEADLINE_SHORT}}. | [BFEND] | groen |
| Subject 2 | Gift it before Black Friday ends: extra 10% applied | [BFCODE]; [BFEND] | groen |
| Subject 3 | ENDS TONIGHT: extra 10% on your checkout ⏰ | [CHECKOUT]; [BF30] | oranje |
| Preview 1 | An extra 10% on top of Black Friday prices, applied with the button, until {{DEADLINE}}. | [BFCODE]; [BFEND] | groen |
| Preview 2 | Giving it away? 5 free gifts ride along until {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |
| Hero | Yours or theirs.\|Extra 10% until {{DEADLINE_SHORT}}. | [BFCODE]; [BFEND] | groen |
| CTA | Complete my order now | [CHECKOUT] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. 30-day returns work for gifts too. The extra 10% doesn't last 30 days. | [RETURN30]; [BFEND] | groen |

## C3-S

- Berichten: C3-S (`VvC24X`, template `TVmMTy`)
- Positie: 3,01 d na trigger. 14 dagen: 232 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: Your set, priced for Black Friday
- Huidige preview: Every piece, the same tested titanium surface. An extra 10% on top of the sale.
- Huidige hero en CTA: What's in the box. Every pan, one decision. One 75-year warranty for every piece. 4 gifts pending. · knop: Complete my order

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your set, at Black Friday prices until {{DEADLINE_SHORT}} | [CHECKOUT]; [BFEND] | groen |
| Subject 2 | Every piece, one warranty. Extra 10% ends Nov 30. | [W75]; [BFCODE]; [BFEND] | groen |
| Subject 3 | LAST CHANCE: your set + 5 free gifts ⏰ | [CHECKOUT]; [BF48]; [GIFTS5] | oranje |
| Preview 1 | Every piece, the same tested titanium surface. Extra 10% on top until {{DEADLINE}}. | [BFCODE]; [BFEND] | groen |
| Preview 2 | Your set has the biggest saving in your checkout. It ends {{DEADLINE}}. | set heeft echt het grootste absolute verschil met de compare-at in Shopify; [BFEND] | oranje |
| Hero | Your set.\|Extra 10% until {{DEADLINE_SHORT}}. | [BFCODE]; [BFEND] | groen |
| CTA | Complete my set order | [CHECKOUT] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. After {{DEADLINE}} the same set costs more and ships without the 5 gifts. | [PRICEUP]; [GIFTSEND] | groen |

## C3-P

- Berichten: C3-P (`WF2QWP`, template `WDiKfH`)
- Positie: 3,01 d na trigger. 14 dagen: 610 ontvangers, $297 omzet, $0,49 per ontvanger.
- Huidig onderwerp: One pan, or three? Black Friday is live.
- Huidige preview: Most of our 100,000+ customers start with one. An extra 10% on top of the sale.
- Huidige hero en CTA: One pan, or three? Buy 2 pans, get 4 pieces free: six pieces, the same 4 gifts. · knop: Get the 6-piece set, Keep my one pan and check out

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | One pan, or three? Decide before {{DEADLINE_SHORT}}. | [BFEND] | groen |
| Subject 2 | Buy 2 pans, get 4 pieces free. Ends Nov 30. | 6-delige set staat in BF nog als 'Buy 2, get 4 free' (six pieces) op de site; [BFEND] | oranje. Controleer dat de BF-listing deze formule nog gebruikt (DECISIONS 8 okt gold voor de fall sale). |
| Subject 3 | ENDS TONIGHT: your pan + an extra 10% ⏰ | [CHECKOUT]; [BF30] | oranje |
| Preview 1 | Most of our 100,000+ customers start with one. Extra 10% on top until {{DEADLINE}}. | [BFCODE]; [BFEND] | groen |
| Preview 2 | Keep your one pan, or take the 6-piece set. Either way, the price ends {{DEADLINE}}. | [BFEND] | groen |
| Hero | One or three.\|Extra 10% until {{DEADLINE_SHORT}}. | [BFCODE]; [BFEND] | groen |
| CTA | Complete my order now | [CHECKOUT] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. The 6-piece set just arrived and is selling fast. | [STOCK6] | oranje |

## C3-ACC

- Berichten: C3-ACC (`Rd7W5Y`, template `TkWZtN`)
- Positie: 3,01 d na trigger. 14 dagen: 113 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: The pan we made after the board, priced for Black Friday
- Huidige preview: We started with cutting boards too. Black Friday is live, plus an extra 10%.
- Huidige hero en CTA: {{ item.title }} · knop: Complete my order, The Pan Pro, 11″28 cm28 cm (11″)

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | The pan we made after the board. Black Friday ends Nov 30. | [BFEND] | groen |
| Subject 2 | Your checkout, extra 10%, until {{DEADLINE_SHORT}} | [CHECKOUT]; [BFCODE]; [BFEND] | groen |
| Subject 3 | LAST CHANCE: extra 10% on your checkout ⏰ | [CHECKOUT]; [BF48] | oranje |
| Preview 1 | We started with cutting boards too. Extra 10% on top of the sale until {{DEADLINE}}. | [BFCODE]; [BFEND] | groen |
| Preview 2 | Add the pan before {{DEADLINE}} and the extra 10% covers the whole checkout. | [BFCODE] werkt op de hele checkout | groen |
| Hero | Board first.\|Pan before {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Complete my order now | [CHECKOUT] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. 5 free gifts with this checkout until {{DEADLINE}}. After that, none. | [GIFTS5]; [GIFTSEND] | groen |

## C4 nocode (cooldown en T02-B)

- Berichten: C4 nocode · cooldown (`UaWEuj`, template `RR39cn`), C4 nocode · T02-B (`SUUzf5`, template `XPiQbV`)
- Positie: 5,01 d na trigger. 14 dagen: 100 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: Last email about your Black Friday cart
- Huidige preview: Black Friday prices, an extra 10% with the button, and then we stop reminding you.
- Huidige hero en CTA: Last email. Still yours, if you want it. 4 gifts pending, 30 days to decide. · knop: Complete my order

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Last email about your checkout. Ends {{DEADLINE_SHORT}}. | [LASTFLOW]; [BFEND] | groen |
| Subject 2 | FINAL REMINDER: your Black Friday checkout ⏰ | [LASTFLOW]; [CHECKOUT] | oranje |
| Subject 3 | Your checkout, an extra 10%, and then we stop | [LASTFLOW]; [BFCODE] | groen |
| Preview 1 | Black Friday prices, an extra 10% with the button, until {{DEADLINE}}. Then we stop reminding you. | [BFCODE]; [LASTFLOW] | groen |
| Preview 2 | Last reminder. The 5 free gifts end {{DEADLINE}}. | [LASTFLOW]; [GIFTSEND] | groen |
| Hero | Last email.\|Extra 10% until {{DEADLINE_SHORT}}. | [LASTFLOW]; [BFCODE]; [BFEND] | groen |
| CTA | Complete my order now | [CHECKOUT] | groen |
| Deadline-regel | Ends {{DEADLINE}}: Black Friday prices, the extra 10% and your 5 free gifts. | [BFEND]; [BFCODE]; [GIFTSEND] | groen |
| PS | P.S. This is the last one from me about this checkout. | [LASTFLOW] | groen |

## CODE · C4

- Berichten: CODE · C4 (`RKvJmd`, template `UukQd9`)
- Positie: 5,01 d na trigger. 14 dagen: 830 ontvangers, $764 omzet, $0,92 per ontvanger.
- Huidig onderwerp: Your own 10%, on top of Black Friday prices
- Huidige preview: Already applied to your cart. In 48 hours we remove it, then the regular sale price applies.
- Huidige hero en CTA: Last email, 48 hours. Your 10% runs out, then we're removing your discount. Your own code is already applied. · knop: Use my 10% now

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your own 10% expires in 48 hours | [CODE48]; [NOW] | groen |
| Subject 2 | Use it or lose it: 10% on your checkout ⏰ | [CODE48] | oranje |
| Subject 3 | YOUR 10% ENDS {{DEADLINE_SHORT}} | [CODE48] | oranje. Caps op drie woorden. |
| Preview 1 | Already applied to your checkout. On {{DEADLINE}} we remove it. | [CODE48] | groen |
| Preview 2 | One use, made for this checkout. 48 hours, then the regular sale price. | [CODE48] | groen |
| Hero | Your own 10%.\|48 hours. | [CODE48] | groen |
| CTA | Use my 10% now | [CODE48] | groen |
| Deadline-regel | Your code expires {{DEADLINE}}. After that the regular sale price applies. | [CODE48] | groen |
| PS | P.S. Last email about this checkout. The code goes, the checkout link keeps working. | [LASTFLOW]; checkout-URL blijft geldig | groen |

## NIEUW · C4-REM (voorstel, +44 uur na CODE · C4)

- Berichten: geen (voorstel voor een nieuwe flowstap).
- Huidig onderwerp: (nieuw)
- Huidige preview: (nieuw)
- Huidige hero en CTA: (geen hero-beeld; tekstmail) · knop: (geen knop gevonden)
- Noot: Nieuwe stap; bestaat niet in Klaviyo.

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your 10% expires in {{HOURS_LEFT}} hours | [CODEREM] | groen |
| Subject 2 | Order now: {{MINUTES_LEFT}} minutes left on your checkout code | [CODEREM]; [MINS] | rood |
| Subject 3 | FINAL HOURS: your own 10% ⏰ | [CODEREM] | oranje |
| Preview 1 | Your code stops working {{DEADLINE}}. Your checkout is one click away. | [CODEREM]; [CHECKOUT] | groen |
| Preview 2 | {{HOURS_LEFT}} hours, then the regular sale price. | [CODEREM] | groen |
| Hero | {{HOURS_LEFT}} hours left\|on your 10%. | [CODEREM] | groen |
| CTA | Complete my order now | [CHECKOUT] | groen |
| Deadline-regel | Expires {{DEADLINE}}. | [CODEREM] | groen |
| PS | P.S. No more emails about this checkout after this one. | [LASTFLOW] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your cart is reserved / we're holding your cart / price held | Verboden (DECISIONS 1 nov, BRIEF). De Shopify-cart houdt geen prijs vast. |
| Your cart expires at midnight | De cart vervalt niet. Wel waar op 30 nov: 'Your cart prices go up at midnight' ([BF30] + [PRICEUP]). |
| Your order is pending / will be canceled | Er bestaat geen order; nep-orderstatus (FTC Act sectie 5, CAN-SPAM). |
| Only 3 left / almost sold out | Geen echte voorraaddata per variant in de flow; valse schaarste. |
| We extended your discount 24 hours, it cannot be extended again | Verzonnen verlenging; BRIEF verbiedt 'no extensions'. |
| Your code expires tonight (in een 48-uurs codemail op het moment van uitgifte) | Op het uitgiftemoment zijn het nog 48 uur. Alleen waar in de nieuwe herinneringsstap [CODEREM]. |
| Your 4 gifts are still pending (huidige C1/C2/C3/C4-hero en preview) | Niet nep, maar 'pending' ligt tegen 'pending order' aan en '4' is achterhaald: wordt '5 free gifts are on this checkout'. |

## Voorwaarden in deze flow

- **[BF30]** de mail gaat uit op 30 nov (laatste BF-dag) en saleprijs, BFCODE en gifts stoppen echt op {{DEADLINE}}. In een flow alleen via een datumblok in onderwerp en hero ({% today %}-vergelijking, getest) of doordat Floris op 30 nov de onderwerpen omzet (PATCH flow-action) en op 1 dec terugzet; andere dagen valt de regel terug op de [BFEND]-versie
- **[BF48]** de mail gaat uit op 29 of 30 nov (laatste 48 uur van BF), zelfde datumblok als [BF30]; 'last chance' en 'final hours' alleen dan
- **[BFCODE]** BFCODE (extra 10% bovenop de sale, alleen abandonment) staat in de knoplink en werkt op het verzendmoment; BFCODE stopt met BF, dus de einddatum is [BFEND]
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[CHECKOUT]** echte Started Checkout van dit profiel en geen order sinds flowstart (flowfilter staat erin); knop gaat naar de checkout-URL
- **[CODE48]** unieke Klaviyo-code (K3_10_48H, C4_10_48H of B2_10_48H, one use) vervalt in Shopify echt 48 uur na uitgifte; {{DEADLINE}} = days_later:2 met het uur van de coupon-instelling (template zegt nu 'expires on the morning of', dus uur controleren); {{DEADLINE_SHORT}} = weekdag
- **[CODEREM]** NIEUWE flowstap (bestaat nu niet): herinnering op uitgifte + 44 tot 46 uur, alleen als de code ongebruikt is (Placed Order = 0 sinds flowstart); {{HOURS_LEFT}} = echte uren tot de coupon-einde
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[LASTFLOW]** dit is echt de laatste mail van deze flow voor dit profiel (geen stap meer erna)
- **[MINS]** {{MINUTES_LEFT}} alleen naast een live countdown-GIF (Sendtric/NiftyImages) die naar de echte backend-eindtijd telt en daarna ENDED toont; als statische tekst nooit
- **[NOW]** de flowmail gaat uit op het moment dat de trigger valt (geen 'local time'-verschuiving), dus relatieve tijd klopt
- **[PRICEUP]** de producten in deze cart/checkout gaan op {{DEADLINE}} echt terug naar de normale prijs (einde BF). De Shopify-cart zelf vervalt niet en houdt geen prijs vast; de regel gaat over de prijs, nooit over de cart
- **[RETURN30]** 30 dagen retour vanaf bezorging, ongebruikt (DECISIONS 1 okt)
- **[STOCK6]** Floris bevestigt in de backend dat de nieuwe voorraad 6-pcs en/of 12-pcs net binnen is ('Just arrived and selling fast', DECISIONS 1 nov); nooit een getal zonder echte voorraaddata
- **[W75]** 75 jaar garantie (DECISIONS 1 okt)
