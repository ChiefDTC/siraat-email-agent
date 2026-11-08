# UyFc78 · v4 · Winback: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `UyFc78` (Metric), status live, 10 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 0 ontvangers (0 per week), $0 omzet, $0 per ontvanger, 0% unieke klik.
- Echte deadlines in deze flow: Echt nu: BF-sale tot 30 nov. R1 op 45 dagen, R2 op 75 dagen na de laatste order. Geen ontvangers in de laatste 14 dagen (flow nog te jong voor 45 dagen). CODE · R2 en CODE · R2-VIP hebben geen coupon in de template, dus geen code-deadline.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| R1-SET | 45 d na trigger | 0 | - | Your prices: up to 70% off. | Your prices: up to 70% off. Ends {{DEADLINE_SHORT}}. | groen |
| R1-PAN (kook en eigenaar) | 45 d na trigger | 0 | - | Your prices: up to 70% off. | Your prices: up to 70% off. Ends {{DEADLINE_SHORT}}. | groen |
| R1-ACC | 45 d na trigger | 0 | - | Ready for the pan? It's in the sale. | Ready for the pan? It's in the sale until {{DEADLINE_SHORT}}. | groen |
| R2-VIP (nocode en CODE) | 75 d na trigger | 0 | - | Your next piece, up to 70% off. | Last email from me: your next piece, up to 70% off | groen |
| R2 (nocode en CODE) | 75 d na trigger | 0 | - | A second pan, up to 70% off. | Last email at this price: a second pan ⏰ | oranje |

## R1-SET

- Berichten: R1-SET (`Wm75BB`, template `YyvDfz`)
- Positie: 45 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: Your prices: up to 70% off.
- Huidige preview: Your prices: up to 70% off. The Black Friday Sale is live.
- Huidige hero en CTA: Siraat hammered titanium cookware, dark studio, Black Friday Sale · knop: (geen knop gevonden)

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your prices: up to 70% off. Ends {{DEADLINE_SHORT}}. | [SALE70]; [BFEND] | groen |
| Subject 2 | Last email at this price ⏰ | [LASTPRICE] | oranje |
| Subject 3 | ENDS TONIGHT: the pan your set is missing | [BF30] | oranje |
| Preview 1 | Six weeks with your set. The piece it's missing is up to 70% off until {{DEADLINE}}. | [SALE70]; [BFEND] | groen |
| Preview 2 | 5 free gifts with every order, and the sale ends {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |
| Hero | Your set, plus one.\|Up to 70% off until {{DEADLINE_SHORT}}. | [SALE70]; [BFEND] | groen |
| CTA | Add to my set before it ends | [BFEND] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. Next time you hear from us at this price is next Black Friday. | [LASTPRICE]; Floris bevestigt dat er tot BF 2027 geen gelijke prijs komt | rood. Pas waar als dat echt zo is; anders schrappen. |

## R1-PAN (kook en eigenaar)

- Berichten: R1-PAN · kook (`S9efY2`, template `X9d3jx`), R1-PAN · eigenaar (`VJ62YY`, template `TQRhxC`)
- Positie: 45 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: Your prices: up to 70% off.
- Huidige preview: Your prices: up to 70% off. The Black Friday Sale is live.
- Huidige hero en CTA: Siraat hammered titanium cookware, dark studio, Black Friday Sale · knop: (geen knop gevonden)

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your prices: up to 70% off. Ends {{DEADLINE_SHORT}}. | [SALE70]; [BFEND] | groen |
| Subject 2 | A second pan, at the price that ends Nov 30 | [BFEND] | groen |
| Subject 3 | ENDS TONIGHT: your second pan at up to 70% off ⏰ | [BF30] | oranje |
| Preview 1 | Six weeks since your pan. The second one is up to 70% off until {{DEADLINE}}. | [SALE70]; [BFEND] | groen |
| Preview 2 | Same titanium, same 75-year warranty. Different price after {{DEADLINE}}. | [W75]; [PRICEUP] | groen |
| Hero | One pan is never enough.\|Second one on sale until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Get my second pan now | [SALE70] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. The gifts come again with a second order: 5 of them, until {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |

## R1-ACC

- Berichten: R1-ACC (`V74Ynm`, template `VLwFAn`)
- Positie: 45 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: Ready for the pan? It's in the sale.
- Huidige preview: Your prices: up to 70% off. The Black Friday Sale is live.
- Huidige hero en CTA: Siraat hammered titanium cookware, dark studio, Black Friday Sale · knop: (geen knop gevonden)

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Ready for the pan? It's in the sale until {{DEADLINE_SHORT}}. | [SALE70]; [BFEND] | groen |
| Subject 2 | Board first, pan now: Black Friday ends Nov 30 | [BFEND] | groen |
| Subject 3 | LAST CHANCE: the pan at Black Friday prices ⏰ | [BF48] | oranje |
| Preview 1 | You started with us on the accessories. The pan is up to 70% off until {{DEADLINE}}. | [SALE70]; [BFEND] | groen |
| Preview 2 | 5 free gifts with your first pan order, until {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |
| Hero | Now the pan.\|Up to 70% off until {{DEADLINE_SHORT}}. | [SALE70]; [BFEND] | groen |
| CTA | Get the pan before it ends | [BFEND] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. 30 days to return it if it's not for you. | [RETURN30] | groen |

## R2-VIP (nocode en CODE)

- Berichten: R2-VIP nocode · cooldown (`Y4TGLG`, template `VrZEcN`), CODE · R2-VIP (`RrzWZZ`, template `VWnsjw`), R2-VIP nocode · T02-B (`WNRBxs`, template `RWnpzA`)
- Positie: 75 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: Your next piece, up to 70% off.
- Huidige preview: Your next piece, up to 70% off. The Black Friday Sale is live.
- Huidige hero en CTA: Siraat hammered titanium cookware, dark studio, Black Friday Sale · knop: (geen knop gevonden)

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Last email from me: your next piece, up to 70% off | [LASTFLOW]; [SALE70] | groen |
| Subject 2 | Your next piece, at the price that ends {{DEADLINE_SHORT}} ⏰ | [BFEND] | oranje |
| Subject 3 | ENDS TONIGHT: your next piece at Black Friday prices | [BF30] | oranje |
| Preview 1 | You've ordered more than once. The next piece is up to 70% off until {{DEADLINE}}. | [VIP2]; [SALE70]; [BFEND] | groen |
| Preview 2 | This is the last email in this series. The price ends {{DEADLINE}}. | [LASTFLOW]; [BFEND] | groen |
| Hero | Your next piece.\|On sale until {{DEADLINE_SHORT}}. | [BFEND] | groen |
| CTA | Get my next piece now | [SALE70] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. No more emails from this series after this one. | [LASTFLOW] | groen |

## R2 (nocode en CODE)

- Berichten: R2 nocode · cooldown (`VDsLDA`, template `V7uCPe`), CODE · R2 (`UpqFqk`, template `TqhfGv`), R2 nocode · T02-B (`XYgsri`, template `Ufb5cM`)
- Positie: 75 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: A second pan, up to 70% off.
- Huidige preview: A second pan, up to 70% off. The Black Friday Sale is live.
- Huidige hero en CTA: Siraat hammered titanium cookware, dark studio, Black Friday Sale · knop: (geen knop gevonden)

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Last email at this price: a second pan ⏰ | [LASTFLOW]; [LASTPRICE] | oranje |
| Subject 2 | A second pan, up to 70% off until Nov 30 | [SALE70]; [BFEND] | groen |
| Subject 3 | ENDS TONIGHT: a second pan at up to 70% off | [BF30] | oranje |
| Preview 1 | If one pan is always busy, the second one is up to 70% off until {{DEADLINE}}. | [SALE70]; [BFEND] | groen |
| Preview 2 | Last email in this series. After {{DEADLINE}}, regular price. | [LASTFLOW]; [PRICEUP] | groen |
| Hero | A second pan.\|Last email, sale until {{DEADLINE_SHORT}}. | [LASTFLOW]; [BFEND] | groen |
| CTA | Get my second pan now | [SALE70] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. That's the last one from this series. The sale ends {{DEADLINE}}. | [LASTFLOW]; [BFEND] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| We miss you: here's 30% off, today only | Er bestaat geen winback-code met einddatum (CODE · R2 heeft nu geen coupon). |
| Your account will be deleted | Verzonnen. |
| Last email at this price (op 1 tot 29 nov zonder campagne-uitsluiting) | Campagnes met dezelfde prijs lopen door; alleen waar met [LASTPRICE]. |

## Voorwaarden in deze flow

- **[BF30]** de mail gaat uit op 30 nov (laatste BF-dag) en saleprijs, BFCODE en gifts stoppen echt op {{DEADLINE}}. In een flow alleen via een datumblok in onderwerp en hero ({% today %}-vergelijking, getest) of doordat Floris op 30 nov de onderwerpen omzet (PATCH flow-action) en op 1 dec terugzet; andere dagen valt de regel terug op de [BFEND]-versie
- **[BF48]** de mail gaat uit op 29 of 30 nov (laatste 48 uur van BF), zelfde datumblok als [BF30]; 'last chance' en 'final hours' alleen dan
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[LASTFLOW]** dit is echt de laatste mail van deze flow voor dit profiel (geen stap meer erna)
- **[LASTPRICE]** na deze mail krijgt dit profiel geen mail meer met deze prijs: alleen waar op 30 nov ([BF30]) of als het profiel tot 30 nov uit alle BF-campagnes is gesloten. Anders misleidend, want campagnes lopen door
- **[PRICEUP]** de producten in deze cart/checkout gaan op {{DEADLINE}} echt terug naar de normale prijs (einde BF). De Shopify-cart zelf vervalt niet en houdt geen prijs vast; de regel gaat over de prijs, nooit over de cart
- **[RETURN30]** 30 dagen retour vanaf bezorging, ongebruikt (DECISIONS 1 okt)
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
- **[VIP2]** profiel heeft echt 2 of meer orders (flowtrigger VIP)
- **[W75]** 75 jaar garantie (DECISIONS 1 okt)
