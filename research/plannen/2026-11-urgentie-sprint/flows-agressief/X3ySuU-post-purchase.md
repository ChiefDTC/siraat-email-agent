# X3ySuU · v4 · Post-purchase: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `X3ySuU` (Metric), status live, 24 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 8.016 ontvangers (4.008 per week), $4.437 omzet, $0,55 per ontvanger, 5,69% unieke klik.
- Echte deadlines in deze flow: Echt nu: BF-sale en 5 gifts tot 30 nov (elke order, ook een tweede). Geen order-edit: 'add it before your order ships' is pas waar als Floris een order-edit-link of samenvoegen via support bevestigt. P1 gaat 1 uur na de order uit, dus de order is dan bijna altijd nog niet verzonden (verzending binnen 1 werkdag, mediaan 77 uur tot fulfillment). CODE-varianten van P3 hebben nu geen coupon in de template.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| P1-FIRST | 1 u na trigger | 4.250 | $0,90 | Good call. Here's what's coming. | Order confirmed. Add the lid before your order ships | rood |
| P1-REPEAT | 1 u na trigger | 395 | $0,87 | Good to see you again | Good to see you again. Add a piece before your order ships | rood |
| P2-SAFE | 16,04 d na trigger | 1.838 | $0,12 | When your pan arrives: the first egg | Before your first cook: 3 steps (and the lid sale ends Nov 30) | groen |
| P3-SET (nocode en CODE) | 20,04 d na trigger | 526 | $0,00 | The pan your set is missing | The pan your set is missing: Black Friday prices end {{DEADLINE_SHORT}} | groen |
| P3-NEXT (deksel en eigenaar) | 20,04 d na trigger | 138 | $0,00 | How is the pan treating you? | What goes next to your pan: Black Friday prices end {{DEADLINE_SHORT}} | groen |
| P3-PAN | 20,04 d na trigger | 748 | $0,08 | Which lid fits your pan? | The lid that fits your pan: Black Friday prices end {{DEADLINE_SHORT}} | groen |
| P3-ACCESSORY (kook en acc) | 20,04 d na trigger | 118 | $0,00 | Now meet the pan | Now meet the pan: Black Friday prices end {{DEADLINE_SHORT}} | groen |
| P3-APRON | 20,04 d na trigger | 3 | $0,00 | An apron deserves a pan | An apron deserves a pan: Black Friday prices end {{DEADLINE_SHORT}} | groen |

## P1-FIRST

- Berichten: P1-FIRST (`R3gbkQ`, template `XhZ3Xr`)
- Positie: 1 u na trigger. 14 dagen: 4.250 ontvangers, $3.812 omzet, $0,90 per ontvanger.
- Huidig onderwerp: Good call. Here's what's coming.
- Huidige preview: Order confirmed. Your 4 gifts, your e-book and the one tip that matters.
- Huidige hero en CTA: Order confirmed. Good call, here's what's next: your order, 4 gifts and one tip. Your 4 gifts are on the way. · knop: Download your e-book, Add the 11″28 cm28 cm (11″) lid

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Order confirmed. Add the lid before your order ships | [UNSHIP] | rood. Pas waar met order-edit of samenvoegen; anders S2. |
| Subject 2 | Order confirmed. 5 gifts on the way, and the lid is still on sale | [GIFTS5] (order na 7 nov); [SALE70] | groen |
| Subject 3 | ENDS NOV 30: the lid for your pan at Black Friday prices | [BFEND] | oranje. Caps op twee woorden. |
| Preview 1 | Your 5 gifts, your e-book, one tip. And the matching lid at Black Friday prices until {{DEADLINE}}. | [GIFTS5]; [BFEND] | groen |
| Preview 2 | Want it in the same box? Add it before your order ships. | [UNSHIP] | rood |
| Hero | Order confirmed.\|Add the lid before it ships. | [UNSHIP] | rood. Veilige variant: 'Order confirmed.\|Your lid, on sale until {{DEADLINE_SHORT}}.' ([BFEND], groen). |
| CTA | Add the lid to my order | [UNSHIP]; anders 'Get the lid that fits' (groen) | rood |
| Deadline-regel | The lid is at Black Friday prices until {{DEADLINE}} and ships free on its own. | [BFEND]; [SHIPSEP] | groen |
| PS | P.S. A second order ships free and gets its own 5 gifts too, until {{DEADLINE}}. | [SHIPSEP]; [GIFTS5]; [GIFTSEND] | groen |

## P1-REPEAT

- Berichten: P1-REPEAT (`WqxPSh`, template `UCEkN9`)
- Positie: 1 u na trigger. 14 dagen: 395 ontvangers, $342 omzet, $0,87 per ontvanger.
- Huidig onderwerp: Good to see you again
- Huidige preview: Your order is in. Same careful packing, same 4 gifts.
- Huidige hero en CTA: Order confirmed. Good to see you again. Same packing, same 4 gifts on the way. · knop: Read the care guide, Download your e-book

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Good to see you again. Add a piece before your order ships | [UNSHIP] | rood |
| Subject 2 | Order in. Same 5 gifts, and Black Friday runs until Nov 30 | [GIFTS5]; [BFEND] | groen |
| Subject 3 | ENDS NOV 30: your next piece at Black Friday prices | [BFEND] | oranje |
| Preview 1 | Your order is in, with 5 free gifts. Anything to add is up to 70% off until {{DEADLINE}}. | [GIFTS5]; [SALE70]; [BFEND] | groen |
| Preview 2 | Same careful packing. Add the lid now while it's still Black Friday. | [SALE70]; [BFEND] | groen |
| Hero | Good to see you.\|One more piece, until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Add a piece before Black Friday ends | [BFEND] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. Ordered something you meant to add? Reply now. If your order hasn't left, our team will try to combine them. | [SUPPORTMERGE]; reply-to is support | oranje |

## P2-SAFE

- Berichten: P2-SAFE (`TZ6TKb`, template `SvHrU6`)
- Positie: 16,04 d na trigger. 14 dagen: 1.838 ontvangers, $224 omzet, $0,12 per ontvanger.
- Huidig onderwerp: When your pan arrives: the first egg
- Huidige preview: Heat first, then oil, then the egg. Keep this for your first cook.
- Huidige hero en CTA: When your pan arrives. Your first egg, step by step. Keep this for your first cook. Heat first, then oil, then egg. · knop: Watch the chef video, Add the 11″28 cm28 cm (11″) lid

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Before your first cook: 3 steps (and the lid sale ends Nov 30) | [BFEND] | groen |
| Subject 2 | Read this before you turn on the stove | pan is waarschijnlijk nog niet gebruikt (16 dagen na order; onbekend per profiel) | oranje |
| Subject 3 | LAST CHANCE: a second pan at Black Friday prices ⏰ | [BF48] | oranje |
| Preview 1 | Heat first, then oil, then the egg. Second pan or lid at Black Friday prices until {{DEADLINE}}. | [BFEND] | groen |
| Preview 2 | Keep this for your first cook. Black Friday ends {{DEADLINE}}. | [BFEND] | groen |
| Hero | First egg tonight?\|Lid on sale until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Get the lid before Black Friday ends | [BFEND] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. The chef video stays online. The Black Friday price on the lid doesn't: {{DEADLINE}}. | [BFEND] | groen |

## P3-SET (nocode en CODE)

- Berichten: P3-SET nocode · cooldown (`XzWEL9`, template `RHrSAF`), CODE · P3-SET (`QWCUZs`, template `SQPHk2`), P3-SET nocode · T02-B (`WjUzwT`, template `XmcycE`)
- Positie: 20,04 d na trigger. 14 dagen: 526 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: The pan your set is missing
- Huidige preview: What set owners add next. 4 gifts with every order.
- Huidige hero en CTA: For set owners. The pan your set is missing: what set owners add next. 4 gifts with every order, 30-day returns. · knop: See what fits my set

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | The pan your set is missing: Black Friday prices end {{DEADLINE_SHORT}} | [SALE70]; [BFEND] | groen |
| Subject 2 | Last email at this price: the pan your set is missing ⏰ | [LASTFLOW] (P3 is de laatste post-purchase-mail); [LASTPRICE] | oranje. Alleen op 30 nov of met uitsluiting van BF-campagnes; anders 'Black Friday ends Nov 30'. |
| Subject 3 | ENDS TONIGHT: the pan your set is missing + 5 free gifts | [BF30]; [GIFTS5] | oranje |
| Preview 1 | Picked for what you ordered. Up to 70% off and 5 free gifts until {{DEADLINE}}. | [SALE70]; [GIFTS5]; [BFEND] | groen |
| Preview 2 | Ships free on its own, with its own 5 gifts. The price ends {{DEADLINE}}. | [SHIPSEP]; [GIFTS5]; [BFEND] | groen |
| Hero | The pan your set is missing.\|Black Friday until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Get it before Black Friday ends | [BFEND] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. This is the last product email after your order. The next price you see from us is the regular one. | [LASTFLOW]; [LASTPRICE] | oranje |

## P3-NEXT (deksel en eigenaar)

- Berichten: P3-NEXT · deksel nocode · cooldown (`VavJD3`, template `Vwaqvi`), P3-NEXT · eigenaar nocode · cooldown (`YA6YXd`, template `W5JGRf`), CODE · P3-NEXT · deksel (`VGTwUg`, template `RiSQU5`), CODE · P3-NEXT · eigenaar (`UUBXAR`, template `Y8DBsg`), P3-NEXT · deksel nocode · T02-B (`V5SuhD`, template `RLDnPU`), P3-NEXT · eigenaar nocode · T02-B (`UhAUYe`, template `Rk5kYM`)
- Positie: 20,04 d na trigger. 14 dagen: 138 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: How is the pan treating you?
- Huidige preview: The board or the lid that matches your order. 4 gifts with every order.
- Huidige hero en CTA: For pan owners. What goes next to your pan, picked to match what you have. 4 gifts with every order, 30-day returns. · knop: See what fits my pan

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | What goes next to your pan: Black Friday prices end {{DEADLINE_SHORT}} | [SALE70]; [BFEND] | groen |
| Subject 2 | Last email at this price: the piece next to your pan ⏰ | [LASTFLOW] (P3 is de laatste post-purchase-mail); [LASTPRICE] | oranje. Alleen op 30 nov of met uitsluiting van BF-campagnes; anders 'Black Friday ends Nov 30'. |
| Subject 3 | ENDS TONIGHT: the piece next to your pan + 5 free gifts | [BF30]; [GIFTS5] | oranje |
| Preview 1 | Picked for what you ordered. Up to 70% off and 5 free gifts until {{DEADLINE}}. | [SALE70]; [GIFTS5]; [BFEND] | groen |
| Preview 2 | Ships free on its own, with its own 5 gifts. The price ends {{DEADLINE}}. | [SHIPSEP]; [GIFTS5]; [BFEND] | groen |
| Hero | What goes next to your pan.\|Black Friday until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Get it before Black Friday ends | [BFEND] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. This is the last product email after your order. The next price you see from us is the regular one. | [LASTFLOW]; [LASTPRICE] | oranje |

## P3-PAN

- Berichten: P3-PAN nocode · cooldown (`S83KTi`, template `TrPKN8`), CODE · P3-PAN (`VCggyS`, template `XJV5Pt`), P3-PAN nocode · T02-B (`TcPkrL`, template `S7KEfQ`)
- Positie: 20,04 d na trigger. 14 dagen: 748 ontvangers, $59 omzet, $0,08 per ontvanger.
- Huidig onderwerp: Which lid fits your pan?
- Huidige preview: The lid in your pan's size, plus 4 gifts with every order.
- Huidige hero en CTA: Fits your pan. The lid that fits: match it to your pan's diameter. 4 gifts with every order, 30-day returns. · knop: Add the lid that fits

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | The lid that fits your pan: Black Friday prices end {{DEADLINE_SHORT}} | [SALE70]; [BFEND] | groen |
| Subject 2 | Last email at this price: the lid that fits ⏰ | [LASTFLOW] (P3 is de laatste post-purchase-mail); [LASTPRICE] | oranje. Alleen op 30 nov of met uitsluiting van BF-campagnes; anders 'Black Friday ends Nov 30'. |
| Subject 3 | ENDS TONIGHT: the lid that fits + 5 free gifts | [BF30]; [GIFTS5] | oranje |
| Preview 1 | Picked for what you ordered. Up to 70% off and 5 free gifts until {{DEADLINE}}. | [SALE70]; [GIFTS5]; [BFEND] | groen |
| Preview 2 | Ships free on its own, with its own 5 gifts. The price ends {{DEADLINE}}. | [SHIPSEP]; [GIFTS5]; [BFEND] | groen |
| Hero | The lid that fits your pan.\|Black Friday until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Get it before Black Friday ends | [BFEND] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. This is the last product email after your order. The next price you see from us is the regular one. | [LASTFLOW]; [LASTPRICE] | oranje |

## P3-ACCESSORY (kook en acc)

- Berichten: P3-ACCESSORY · kook nocode · cooldown (`UsRrF2`, template `TeyeWP`), P3-ACCESSORY · acc nocode · cooldown (`VsZKS6`, template `Vi4pAc`), CODE · P3-ACCESSORY · kook (`WaE4Q7`, template `SeZaN7`), CODE · P3-ACCESSORY · acc (`UcXECQ`, template `T4tece`), P3-ACCESSORY · kook nocode · T02-B (`RWMfcw`, template `Rn6m9i`), P3-ACCESSORY · acc nocode · T02-B (`RMwJvJ`, template `SNzta4`)
- Positie: 20,04 d na trigger. 14 dagen: 118 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: Now meet the pan
- Huidige preview: We started with cutting boards too. Then the pan. 4 gifts with every order.
- Huidige hero en CTA: For Siraat owners. Now meet the pan: the original hammered titanium pan. 4 gifts with every order, 30-day returns. · knop: Get the Pan Pro

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Now meet the pan: Black Friday prices end {{DEADLINE_SHORT}} | [SALE70]; [BFEND] | groen |
| Subject 2 | Last email at this price: the pan, up to 70% off ⏰ | [LASTFLOW] (P3 is de laatste post-purchase-mail); [LASTPRICE] | oranje. Alleen op 30 nov of met uitsluiting van BF-campagnes; anders 'Black Friday ends Nov 30'. |
| Subject 3 | ENDS TONIGHT: the pan, up to 70% off + 5 free gifts | [BF30]; [GIFTS5] | oranje |
| Preview 1 | Picked for what you ordered. Up to 70% off and 5 free gifts until {{DEADLINE}}. | [SALE70]; [GIFTS5]; [BFEND] | groen |
| Preview 2 | Ships free on its own, with its own 5 gifts. The price ends {{DEADLINE}}. | [SHIPSEP]; [GIFTS5]; [BFEND] | groen |
| Hero | Now meet the pan.\|Black Friday until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Get it before Black Friday ends | [BFEND] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. This is the last product email after your order. The next price you see from us is the regular one. | [LASTFLOW]; [LASTPRICE] | oranje |

## P3-APRON

- Berichten: P3-APRON nocode · cooldown (`Xk4THX`, template `WvueCz`), CODE · P3-APRON (`UPYHft`, template `SttbJ8`), P3-APRON nocode · T02-B (`YqQugr`, template `RAyn5j`)
- Positie: 20,04 d na trigger. 14 dagen: 3 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: An apron deserves a pan
- Huidige preview: The pan it was made for, for you or for them. 4 gifts with every order.
- Huidige hero en CTA: Thank you. An apron deserves a pan, for you or for them. 4 gifts with every order, 30-day returns. · knop: Get the Pan Pro

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | An apron deserves a pan: Black Friday prices end {{DEADLINE_SHORT}} | [SALE70]; [BFEND] | groen |
| Subject 2 | Last email at this price: the pan for your apron ⏰ | [LASTFLOW] (P3 is de laatste post-purchase-mail); [LASTPRICE] | oranje. Alleen op 30 nov of met uitsluiting van BF-campagnes; anders 'Black Friday ends Nov 30'. |
| Subject 3 | ENDS TONIGHT: the pan for your apron + 5 free gifts | [BF30]; [GIFTS5] | oranje |
| Preview 1 | Picked for what you ordered. Up to 70% off and 5 free gifts until {{DEADLINE}}. | [SALE70]; [GIFTS5]; [BFEND] | groen |
| Preview 2 | Ships free on its own, with its own 5 gifts. The price ends {{DEADLINE}}. | [SHIPSEP]; [GIFTS5]; [BFEND] | groen |
| Hero | An apron deserves a pan.\|Black Friday until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Get it before Black Friday ends | [BFEND] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. This is the last product email after your order. The next price you see from us is the regular one. | [LASTFLOW]; [LASTPRICE] | oranje |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your order is on hold until you add the lid | Verzonnen orderstatus. |
| Add it to your order (zonder order-edit of samenvoegen) | Shopify laat klanten geen items aan een geplaatste order toevoegen; het wordt een tweede order. Alleen met [UNSHIP]. |
| Last chance before your box is sealed | We weten niet wanneer de doos dichtgaat; nep-procesclaim. |
| Your 5 gifts are waiting for this add-on | De gifts zitten al bij de eerste order. |
| Here's what's coming (huidig P1-FIRST-onderwerp) | Geen urgentie-lijn, maar 'coming' staat op de verboden lijst van deze sprint; voorstel: 'Order confirmed. Here's what's next.' |

## Voorwaarden in deze flow

- **[BF30]** de mail gaat uit op 30 nov (laatste BF-dag) en saleprijs, BFCODE en gifts stoppen echt op {{DEADLINE}}. In een flow alleen via een datumblok in onderwerp en hero ({% today %}-vergelijking, getest) of doordat Floris op 30 nov de onderwerpen omzet (PATCH flow-action) en op 1 dec terugzet; andere dagen valt de regel terug op de [BFEND]-versie
- **[BF48]** de mail gaat uit op 29 of 30 nov (laatste 48 uur van BF), zelfde datumblok als [BF30]; 'last chance' en 'final hours' alleen dan
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[LASTFLOW]** dit is echt de laatste mail van deze flow voor dit profiel (geen stap meer erna)
- **[LASTPRICE]** na deze mail krijgt dit profiel geen mail meer met deze prijs: alleen waar op 30 nov ([BF30]) of als het profiel tot 30 nov uit alle BF-campagnes is gesloten. Anders misleidend, want campagnes lopen door
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
- **[SHIPSEP]** een tweede order wordt los verzonden en krijgt zelf gratis verzending en de gifts; de copy belooft niet dat het in hetzelfde pakket zit
- **[SUPPORTMERGE]** support (Gorgias) kan een tweede order echt samenvoegen met een nog niet verzonden eerste order; Floris bevestigt
- **[UNSHIP]** de order van dit profiel staat op het verzendmoment nog op unfulfilled (verzendfilter Fulfilled Order = 0 sinds flowstart) EN er bestaat een echte manier om toe te voegen aan dezelfde zending (order-edit-link of supportteam voegt samen vóór fulfillment, getest). Zonder dat mechanisme niet waar
