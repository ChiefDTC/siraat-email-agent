# Afmeldingen 01 · Waar komen ze vandaan en wat doen we eraan (data)

Datum: 24 oktober 2026. Aanleiding: Floris stuurde een screenshot van sunsetmail S1 ("Should we keep writing to you?", knop "Yes, keep me on the list") en vroeg waar de afmeldingen vandaan komen. Alles alleen gelezen uit Klaviyo (account TdtTzz, Events API en metric aggregates, revision 2025-10-15). Niets gewijzigd, niets verstuurd. Profiel-ID's en ruwe events staan alleen in de scratchpad; hier staan uitsluitend aggregaten. Bouwt voort op `research/lijstkwaliteit/01-giveaway-instroom.md` (21 okt).

## Kern

1. **Ongeveer 2.500 afmeldingen per week** (laatste vier volle weken), 10.432 in de laatste 30 dagen en 26.798 in 90 dagen. 66 tot 71 procent komt van campagnes (0,42 tot 0,45 procent per mail), 27 tot 33 procent van flows (1,0 procent per mail). Afmeldingen zonder mail als bron bestaan vrijwel niet: 2 via de afmeldpagina en 0 via Shopify in 90 dagen.
2. **Bijna de helft meldt zich af zonder de mail te openen.** 49 procent gaat via de afmeldknop van Gmail of Apple Mail zelf (list-unsubscribe, "one click"), 47 procent via de link in de mail, 4 procent via een spamklacht. Wie zo afhaakt, reageert op hoeveel en hoe lang we mailen, niet op de inhoud van die ene mail.
3. **Twee groepen leveren 80 procent van de afmeldingen**: nieuwe aanmelders in hun eerste 30 dagen (37 procent, waarvan 22 procent al in week 1) en stille profielen zonder klik of order in 90 dagen (43 procent). Actieve klanten zijn 20 procent.
4. **De sunset-flow doet in de praktijk niets.** Hij vangt alleen wie nieuw in het segment valt (circa 4.000 per week), levert 0,45 procent klikkers en $1.168 omzet, en onderdrukt niemand: S1 belooft "we'll stop writing in about a week", maar 60 procent van de niet-klikkers krijgt daarna gewoon weer campagnes. Ondertussen zitten 82.025 profielen in het sunsetsegment die nooit een sunsetmail kregen en in 30 dagen 786.556 campagnemails ontvingen: **44 procent van alle campagnemail**.
5. **Frequentie is niet de directe trekker, volume wel.** Binnen dezelfde leeftijdsgroep stijgt de kans op afmelden per mail niet als iemand meer mails per week krijgt. Wie zich afmeldt kreeg 3,6 mails in de 7 dagen ervoor, tegen 3,0 bij een gemiddelde ontvanger. Wel duidelijk: een campagne binnen 24 uur na een flowmail bij een nieuwe aanmelder geeft 1,30 procent afmelding tegen 0,94 procent zonder (plus 38 procent).
6. **De welkomstmails zijn de duurste mails per ontvanger**: oude Welcome 1 4,5 procent, EB Welcome #1 2,9 procent, nieuwe W1 2,1 procent en W2 2,2 procent. Let op: W1 leek in Klaviyo 0,10 procent, maar de afmeldingen van de A/B-varianten (`SXwPrW`, `VnXKz4`) hangen niet aan het hoofdbericht `RN7Yy6`. Gecorrigeerd is het 2,14 procent.
7. **Spam loopt op**: 0,80 en 1,02 klachten per 1.000 mails in de weken van 12 en 19 oktober, tegen 0,3 tot 0,5 in september. Vooral HS-campagnes, de welkomstflow (v4 en restanten EB) en Failure to launch. Vrijwel alleen Outlook/Hotmail (59 procent in 90 dagen) en Yahoo/AOL (36 procent) melden klachten terug, dus het echte aantal ligt hoger.

## Methode

| Onderdeel | Keuze |
|---|---|
| Afmeldingen | Unsubscribed from Email Marketing `YcWddQ`, alle events 1 jul tot en met 24 okt (32.412). Bron per event: `message_id`, of `method_detail` als dat leeg is (juli). Flowberichten hebben een kort ID, campagneberichten een lang ID dat via de campaign-messages aan de campagne is gekoppeld. A/B-varianten van W1 (`SXwPrW`, `VnXKz4`) en B1 (`YyFeR4`, `UkNrdt`) handmatig aan het hoofdbericht gekoppeld. |
| Ontvangers | Received Email `YkRM4Q`: dagaggregaten per `$message`, `$flow` en Campaign Name (1 jul tot 24 okt), en alle losse events 16 jul tot 24 okt (5,36 miljoen, 206.465 profielen) voor de profielanalyse. |
| Overig | Spam `VQMAAk`, Clicked Email `W247h8` (Bot Click niet waar = menselijk), Placed Order `RSNxYV` (14 okt 2024 tot 24 okt 2026), Subscribed to List `SCvkku` voor Email List `Uw8eZG`. Profielen: `created`, `$source`, `alia_popup_name`, `alia_offer`, land. Flowdefinities `TbYQmX` en `Wzz6xC`, segmenten `WuHSm6` en `YxfuJT`, alle campagnes sinds mei met publiek. |
| Vensters | 30 dagen = 24 sep tot en met 23 okt, 90 dagen = 26 jul tot en met 23 okt (UTC). Afmeldingen tellen in het venster waarin ze vallen; een paar afmeldingen horen bij mails van voor het venster. Profielanalyse met 7- en 30-dagenterugblik vanaf 16 aug. |
| Bron van aanmelding | Zelfde indeling als het giveaway-onderzoek: Alia-variant zonder kortingscode = giveaway, Alia met code of kortingsvariant = kortingspop-up, `$source` -50 zonder Alia = checkout of Shopify-account, andere `$source` = oude Klaviyo-formulieren (Valentijn, Pasen, Pan Pop Up enzovoort), leeg = onbekend of import. |
| Leeftijd op de lijst | Vanaf het vroegste van profiel aangemaakt en eerste Subscribed to List voor `Uw8eZG`. |
| Status bij afmelding | Nieuw = jonger dan 30 dagen. Actief = menselijke klik of order in de 90 dagen ervoor. Sunset-definitie = 120 dagen geen menselijke klik, 180 dagen geen order, ouder dan 120 dagen. Stil = de rest (geen klik of order in 90 dagen, nog geen sunset). Sitebezoek is niet meegenomen (Active on Site niet opgehaald), dus "stil" is iets ruimer dan het Klaviyo-segment. |

## 1. Bron van de afmeldingen

### Hoe mensen zich afmelden

| Manier | 30 dagen | 90 dagen |
|---|---|---|
| Afmeldknop van de mailbox (list-unsubscribe, "one click") | 5.059 (48,5%) | 13.187 (49,2%) |
| Link in de mail (footer, "Unsubscribe in one tap", voorkeurenpagina) | 4.896 (46,9%) | 12.521 (46,7%) |
| Spamklacht (zet automatisch af) | 477 (4,6%) | 1.088 (4,1%) |
| Afmeldpagina zonder mail | 0 | 2 |
| Shopify (Accepts Marketing uit) | 0 | 0 (39 in begin juli) |
| **Totaal** | **10.432** | **26.798** |

Elke afmelding in het venster heeft een mail als bron. De voorkeurenpagina en Shopify spelen geen rol.

### Campagnes tegen flows, 30 dagen

| Bron | Afmeldingen | Aandeel | Ontvangen mails | Afmeldpercentage | Spamklachten |
|---|---|---|---|---|---|
| Campagnes | 7.396 | 70,90% | 1.768.481 | 0,42% | 574 |

### Campagnes tegen flows, 90 dagen

| Bron | Afmeldingen | Aandeel | Ontvangen mails | Afmeldpercentage | Spamklachten |
|---|---|---|---|---|---|
| Campagnes | 17.535 | 65,43% | 3.920.947 | 0,45% | 1369 |

### Per flow, 30 dagen

| Flow | Afmeldingen | Ontvangen | Afmeld% | Spam | Klik (uniek, incl. bots) |
|---|---|---|---|---|---|
| EB / Welcome Flow / Updated 02.03.26 | 744 | 33.400 | 2,23% | 75 | 2,78% |
| v4 · Welcome | 573 | 28.512 | 2,01% | 45 | 3,09% |
| EB / Failure to launch | 563 | 103.084 | 0,55% | 71 | 0,65% |
| EB / DEC 25 / Browse Abandonment | 131 | 7.588 | 1,73% | 13 | 5,30% |
| EB / DEC 25 / Browse Abandonment / Triple Pixel | 95 | 7.469 | 1,27% | 4 | 8,68% |
| v4 · Sunset | 90 | 13.878 | 0,65% | 4 | 0,45% |
| EB / Customer Winback / 5/8/25 | 81 | 15.829 | 0,51% | 11 | 1,12% |
| EB / Post Purchase Flow / 4/6/2026 | 78 | 9.359 | 0,83% | 22 | 32,63% |
| EB / Cart Abandonment / 2/03/26 | 71 | 4.756 | 1,49% | 6 | 5,51% |
| v4 · Cart abandonment | 64 | 4.790 | 1,34% | 3 | 4,70% |
| v4 · Browse abandonment | 39 | 5.416 | 0,72% | 1 | 4,08% |
| FREE E - GUIDE | 38 | 5.083 | 0,75% | 9 | 9,11% |
| v4 · Checkout abandonment | 37 | 2.738 | 1,35% | 2 | 8,44% |
| EB / DEC 25 / Checkout Abandonment | 35 | 2.528 | 1,38% | 1 | 5,14% |

### Per flow, 90 dagen

| Flow | Afmeldingen | Ontvangen | Afmeld% | Spam | Klik (uniek, incl. bots) |
|---|---|---|---|---|---|
| EB / Welcome Flow / Updated 02.03.26 | 3453 | 170.317 | 2,03% | 276 | 2,74% |
| EB / Failure to launch | 1513 | 315.339 | 0,48% | 276 | 0,93% |
| EB / DEC 25 / Browse Abandonment | 586 | 31.688 | 1,85% | 37 | 4,43% |
| v4 · Welcome | 573 | 28.512 | 2,01% | 45 | 3,09% |
| EB / Post Purchase Flow / 4/6/2026 | 416 | 55.481 | 0,75% | 57 | 27,71% |
| EB / DEC 25 / Browse Abandonment / Triple Pixel | 404 | 33.814 | 1,19% | 17 | 6,45% |
| EB / Customer Winback / 5/8/25 | 337 | 44.899 | 0,75% | 22 | 1,44% |
| EB / Cart Abandonment / 2/03/26 | 304 | 24.224 | 1,25% | 29 | 3,85% |
| Mystery Gift Reveal - Sheets | 216 | 19.190 | 1,13% | 4 | 1,48% |
| EB / Pan Education | 178 | 33.369 | 0,53% | 20 | 7,15% |
| EB / DEC 25 / Checkout Abandonment | 163 | 13.485 | 1,21% | 10 | 4,46% |
| FREE E - GUIDE | 151 | 16.002 | 0,94% | 24 | 10,14% |
| EB / Sunset Flow / 5/15/25 | 115 | 20.361 | 0,56% | 11 | 0,52% |
| EB / DEC 25 / Checkout Abandonment / Triple Pixel | 98 | 8.676 | 1,13% | 15 | 5,84% |

Lezing: de oude EB Welcome Flow (`SiaNLu`, uit sinds 8 okt) en v4 · Welcome (`T4a5Mk`) zijn samen goed voor 15 procent van alle afmeldingen in 90 dagen, op slechts 4 procent van de mails. Failure to launch (`T2SmtR`) heeft een laag percentage maar groot volume (315.339 mails) en evenveel spamklachten als de hele welkomstflow (276).

### Top 15 mails op absolute afmeldingen, 30 dagen

| # | Mail | Type | Verzonden | Ontvangers | Afmeldingen | Afmeld% | Spam |
|---|---|---|---|---|---|---|---|
| 1 | HS // Siraats Kitchen // October  Email 4: Sale Push (Plain Text) // 10.12.2026 | campagne | 2026-10-12 | 118.422 | 545 | 0,46% | 31 |
| 2 | Sunday Recipe Day / 30 Days Engaged | campagne | 2026-10-04 | 134.371 | 495 | 0,37% | 56 |
| 3 | Plain Text // Hammered Pan Pro 50% + 4 Free Gifts (One More Time) // 09.2026 //  | campagne | 2026-09-25 | 69.798 | 470 | 0,67% | 15 |
| 4 | Founder Note Sale - Why is it getting difficult for us | campagne | 2026-10-01 | 47.602 | 455 | 0,96% | 38 |
| 5 | HS // Siraats Kitchen // October Email 6: 5-Star Cookware for a 5-Star Experienc | campagne | 2026-10-14 | 58.147 | 434 | 0,75% | 15 |
| 6 | HS // Siraats Kitchen // September Email 15: Warehouse Clearance Sale - Final Ho | campagne | 2026-09-30 | 116.372 | 417 | 0,36% | 43 |
| 7 | HS // Siraats Kitchen // September Email 14: Join SMS Ahead of BFCM - US Only // | campagne | 2026-09-29 | 76.913 | 394 | 0,51% | 30 |
| 8 | Prime Sale - INT (ex US) - Founder Note | campagne | 2026-10-03 | 73.322 | 388 | 0,53% | 30 |
| 9 | HS // Siraats Kitchen // October Email 7: The Cutting Board, Plastic-Free // 10. | campagne | 2026-10-17 | 80.454 | 374 | 0,46% | 26 |
| 10 | HS // Siraats Kitchen // October Email 3: Sale Midweek // 10.10.2026 | campagne | 2026-10-10 | 115.580 | 364 | 0,31% | 37 |
| 11 | HS // Siraats Kitchen // October Email 2: Sale Launch - 4 Gifts With Every Order | campagne | 2026-10-06 | 111.581 | 342 | 0,31% | 30 |
| 12 | HS // Siraats Kitchen // October Email 5: The Video Send - Non-Toxic in Action / | campagne | 2026-10-11 | 117.991 | 331 | 0,28% | 29 |
| 13 | HS // Siraats Kitchen // October Email 8: The Dishwasher Sheets Push // 10.20.20 | campagne | 2026-10-20 | 65.272 | 299 | 0,46% | 17 |
| 14 | HS // Siraats Kitchen // September Email 11: Holiday Gift Guide Teaser // 10.03. | campagne | 2026-10-03 | 77.328 | 284 | 0,37% | 41 |
| 15 | EB / Welcome Flow / Updated 02.03.26 · Eb [DG] / Email #1 (FLOW Updated 5/31/25) | flow | doorlopend | 8.649 | 268 | 3,10% | 23 |

### Top 15 mails op afmeldpercentage (minstens 300 ontvangers), 30 dagen

| # | Mail | Type | Verzonden | Ontvangers | Afmeldingen | Afmeld% | Spam |
|---|---|---|---|---|---|---|---|
| 1 | v4 · Welcome · Old · Welcome 1 | flow | doorlopend | 3.164 | 143 | 4,52% | 11 |
| 2 | EB / Welcome Flow / Updated 02.03.26 · Eb [DG] / Email #1 (FLOW Updated 5/31/25) | flow | doorlopend | 8.649 | 268 | 3,10% | 23 |
| 3 | v4 · Cart abandonment · Old · Cart 2 | flow | doorlopend | 308 | 9 | 2,92% | 0 |
| 4 | v4 · Welcome · Old · Welcome 2 | flow | doorlopend | 2.912 | 80 | 2,75% | 7 |
| 5 | EB / Welcome Flow / Updated 02.03.26 · EB [DG] / Email #2 | flow | doorlopend | 8.252 | 226 | 2,74% | 21 |
| 6 | EB / Welcome Flow / Updated 02.03.26 · EB [DG] / Email #3 | flow | doorlopend | 3.642 | 92 | 2,53% | 5 |
| 7 | EB / DEC 25 / Checkout Abandonment / Triple Pixel · Email #2 | flow | doorlopend | 398 | 9 | 2,26% | 1 |
| 8 | v4 · Welcome · W2 | flow | doorlopend | 4.133 | 90 | 2,18% | 8 |
| 9 | v4 · Welcome · W1 | flow | doorlopend | 5.836 | 125 | 2,14% | 9 |
| 10 | EB / Post Purchase Flow / 4/6/2026 · Copy of Post Purchase Flow / Founder's Note | flow | doorlopend | 531 | 11 | 2,07% | 0 |
| 11 | v4 · Browse abandonment · Old · Browse 1 | flow | doorlopend | 787 | 16 | 2,03% | 1 |
| 12 | EB / Cart Abandonment / 2/03/26 · Email #1 | flow | doorlopend | 1.014 | 20 | 1,97% | 2 |
| 13 | v4 · Cart abandonment · K3 · pan nocode · T02-B | flow | doorlopend | 471 | 9 | 1,91% | 0 |
| 14 | EB / DEC 25 / Browse Abandonment · Copy of Email #1 | flow | doorlopend | 3.801 | 72 | 1,89% | 8 |
| 15 | EB / Welcome Flow / Updated 02.03.26 · EB [DG] / Email #4 | flow | doorlopend | 2.988 | 54 | 1,81% | 5 |

### Top 15 campagnes op afmeldpercentage (minstens 300 ontvangers), 30 dagen

| # | Mail | Type | Verzonden | Ontvangers | Afmeldingen | Afmeld% | Spam |
|---|---|---|---|---|---|---|---|
| 1 | Founder Note Sale - Why is it getting difficult for us | campagne | 2026-10-01 | 47.602 | 455 | 0,96% | 38 |
| 2 | HS // Siraats Kitchen // October Email 6: 5-Star Cookware for a 5-Star Experienc | campagne | 2026-10-14 | 58.147 | 434 | 0,75% | 15 |
| 3 | Plain Text // Hammered Pan Pro 50% + 4 Free Gifts (One More Time) // 09.2026 //  | campagne | 2026-09-25 | 69.798 | 470 | 0,67% | 15 |
| 4 | Prime Sale - INT (ex US) - Founder Note | campagne | 2026-10-03 | 73.322 | 388 | 0,53% | 30 |
| 5 | HS // Siraats Kitchen // September Email 14: Join SMS Ahead of BFCM - US Only // | campagne | 2026-09-29 | 76.913 | 394 | 0,51% | 30 |
| 6 | HS // Siraats Kitchen // September Email 13: This Week's Bestsellers // 09.26.20 | campagne | 2026-09-26 | 48.492 | 237 | 0,49% | 17 |
| 7 | HS // Siraats Kitchen // October Email 7: The Cutting Board, Plastic-Free // 10. | campagne | 2026-10-17 | 80.454 | 374 | 0,46% | 26 |
| 8 | HS // Siraats Kitchen // October Email 7: The Cutting Board, Plastic-Free // 10. | campagne | 2026-10-17 | 1.082 | 5 | 0,46% | 0 |
| 9 | HS // Siraats Kitchen // October  Email 4: Sale Push (Plain Text) // 10.12.2026 | campagne | 2026-10-12 | 118.422 | 545 | 0,46% | 31 |
| 10 | HS // Siraats Kitchen // October Email 8: The Dishwasher Sheets Push // 10.20.20 | campagne | 2026-10-20 | 65.272 | 299 | 0,46% | 17 |
| 11 | Floris / 9 October / Recipe / USA Only | campagne | 2026-10-09 | 26.559 | 110 | 0,41% | 4 |
| 12 | HS // Siraats Kitchen // October Email 1: Non-Toxic Origin - Plain-Text Founder  | campagne | 2026-10-08 | 60.760 | 246 | 0,40% | 13 |
| 13 | ALI FOUNDER EMAIL PRIME | campagne | 2026-10-06 | 45.380 | 179 | 0,39% | 19 |
| 14 | 6-piece set $349 - US - Lids on us | campagne | 2026-10-03 | 66.208 | 261 | 0,39% | 20 |
| 15 | Sunday Recipe Day / 30 Days Engaged | campagne | 2026-10-04 | 134.371 | 495 | 0,37% | 56 |

### Top 15 mails op absolute afmeldingen, 90 dagen

| # | Mail | Type | Verzonden | Ontvangers | Afmeldingen | Afmeld% | Spam |
|---|---|---|---|---|---|---|---|
| 1 | EB / Welcome Flow / Updated 02.03.26 · Eb [DG] / Email #1 (FLOW Updated 5/31/25) | flow | doorlopend | 41.005 | 1204 | 2,94% | 78 |
| 2 | EB / Welcome Flow / Updated 02.03.26 · EB [DG] / Email #2 | flow | doorlopend | 38.373 | 954 | 2,49% | 73 |
| 3 | HS // Siraats Kitchen // October  Email 4: Sale Push (Plain Text) // 10.12.2026 | campagne | 2026-10-12 | 118.422 | 545 | 0,46% | 31 |
| 4 | 10/8 Dishwasher Sheets Founder to Customer | campagne | 2026-08-10 | 84.061 | 542 | 0,64% | 19 |
| 5 | HS // Email 5: Warehouse Clearance Sale - Don't Miss It // 09.15.2026 | campagne | 2026-09-15 | 139.359 | 510 | 0,37% | 40 |
| 6 | INTL-01 - vr 4 sept 10:00 GMT - Siraat Birthday Sale | campagne | 2026-09-03 | 52.417 | 506 | 0,97% | 19 |
| 7 | Sunday Recipe Day / 30 Days Engaged | campagne | 2026-10-04 | 134.371 | 495 | 0,37% | 56 |
| 8 | HS // Siraats Kitchen // September Email 1: Warehouse Clearance Sale // 09.11.20 | campagne | 2026-09-11 | 124.348 | 482 | 0,39% | 34 |
| 9 | Plain Text // Hammered Pan Pro 50% + 4 Free Gifts (One More Time) // 09.2026 //  | campagne | 2026-09-25 | 69.798 | 470 | 0,67% | 15 |
| 10 | Founder Note Sale - Why is it getting difficult for us | campagne | 2026-10-01 | 47.602 | 455 | 0,96% | 38 |
| 11 | HS // Siraats Kitchen // September Email 6: Sweater Weather: Fall Kitchen Refres | campagne | 2026-09-17 | 125.135 | 446 | 0,36% | 39 |
| 12 | HS // Siraats Kitchen // October Email 6: 5-Star Cookware for a 5-Star Experienc | campagne | 2026-10-14 | 58.147 | 434 | 0,75% | 15 |
| 13 | 09/05 September is hard | campagne | 2026-09-05 | 92.724 | 426 | 0,46% | 24 |
| 14 | HS // Siraats Kitchen // September Email 15: Warehouse Clearance Sale - Final Ho | campagne | 2026-09-30 | 116.372 | 417 | 0,36% | 43 |
| 15 | EB / Welcome Flow / Updated 02.03.26 · EB [DG] / Email #3 | flow | doorlopend | 16.181 | 396 | 2,45% | 25 |

### Top 15 mails op afmeldpercentage (minstens 300 ontvangers), 90 dagen

| # | Mail | Type | Verzonden | Ontvangers | Afmeldingen | Afmeld% | Spam |
|---|---|---|---|---|---|---|---|
| 1 | v4 · Welcome · Old · Welcome 1 | flow | doorlopend | 3.164 | 143 | 4,52% | 11 |
| 2 | EB / Welcome Flow / Updated 02.03.26 · Eb [DG] / Email #1 (FLOW Updated 5/31/25) | flow | doorlopend | 41.005 | 1204 | 2,94% | 78 |
| 3 | v4 · Cart abandonment · Old · Cart 2 | flow | doorlopend | 308 | 9 | 2,92% | 0 |
| 4 | v4 · Welcome · Old · Welcome 2 | flow | doorlopend | 2.912 | 80 | 2,75% | 7 |
| 5 | EB / Pan Education · FLOW: Cutting Board Education / Email 2 | flow | doorlopend | 506 | 13 | 2,57% | 0 |
| 6 | EB / Welcome Flow / Updated 02.03.26 · EB [DG] / Email #2 | flow | doorlopend | 38.373 | 954 | 2,49% | 73 |
| 7 | EB / Welcome Flow / Updated 02.03.26 · EB [DG] / Email #3 | flow | doorlopend | 16.181 | 396 | 2,45% | 25 |
| 8 | Mystery Gift 2/4 - Why nobody does this (backlog 11-14 aug) | campagne | 2026-08-19 | 563 | 13 | 2,31% | 0 |
| 9 | v4 · Welcome · W2 | flow | doorlopend | 4.133 | 90 | 2,18% | 8 |
| 10 | v4 · Welcome · W1 | flow | doorlopend | 5.836 | 125 | 2,14% | 9 |
| 11 | v4 · Browse abandonment · Old · Browse 1 | flow | doorlopend | 787 | 16 | 2,03% | 1 |
| 12 | v4 · Cart abandonment · K3 · pan nocode · T02-B | flow | doorlopend | 471 | 9 | 1,91% | 0 |
| 13 | EB / DEC 25 / Browse Abandonment · Copy of Email #1 | flow | doorlopend | 15.697 | 296 | 1,89% | 20 |
| 14 | EB / Welcome Flow / Updated 02.03.26 · EB [DG] / Email #4 | flow | doorlopend | 13.600 | 256 | 1,88% | 16 |
| 15 | EB / DEC 25 / Browse Abandonment · Email #1 | flow | doorlopend | 15.991 | 290 | 1,81% | 17 |

### Top 15 campagnes op afmeldpercentage (minstens 300 ontvangers), 90 dagen

| # | Mail | Type | Verzonden | Ontvangers | Afmeldingen | Afmeld% | Spam |
|---|---|---|---|---|---|---|---|
| 1 | Mystery Gift 2/4 - Why nobody does this (backlog 11-14 aug) | campagne | 2026-08-19 | 563 | 13 | 2,31% | 0 |
| 2 | Mystery Gift 3/4 - The offer (backlog 11-14 aug) | campagne | 2026-08-23 | 547 | 7 | 1,28% | 0 |
| 3 | INTL-01 - vr 4 sept 10:00 GMT - Siraat Birthday Sale | campagne | 2026-09-03 | 52.417 | 506 | 0,97% | 19 |
| 4 | Founder Note Sale - Why is it getting difficult for us | campagne | 2026-10-01 | 47.602 | 455 | 0,96% | 38 |
| 5 | HS // Siraats Kitchen // September Email 4: Accessory Push // 09.13.2026 | campagne | 2026-09-13 | 4.998 | 46 | 0,92% | 0 |
| 6 | AU-01 - vr 4 sept 08:00 AEST - Father's Day Sale Ends Sunday (AU+NZ) | campagne | 2026-09-03 | 16.130 | 137 | 0,85% | 1 |
| 7 | HS // Siraats Kitchen // October Email 6: 5-Star Cookware for a 5-Star Experienc | campagne | 2026-10-14 | 58.147 | 434 | 0,75% | 15 |
| 8 | 8/28 Founder’s Pay Day Recommendation / 30 Days Engaged | campagne | 2026-08-28 | 44.206 | 318 | 0,72% | 28 |
| 9 | 8/3 Annivesary Offer Launch (Regular Subscribers) | campagne | 2026-08-03 | 22.135 | 158 | 0,71% | 13 |
| 10 | 8/6 Single Pan Non-Buyers/ Viewed Pans but Non-Buyers / AU Subscribers | campagne | 2026-08-06 | 437 | 3 | 0,69% | 0 |
| 11 | 8/31 Labor Day Sale Launch / US Only  | campagne | 2026-08-31 | 19.013 | 129 | 0,68% | 11 |
| 12 | 7/27 Healthy Habits Start Here / 30 Days Engaged (Non-US) | campagne | 2026-07-27 | 25.868 | 175 | 0,68% | 14 |
| 13 | Plain Text // Hammered Pan Pro 50% + 4 Free Gifts (One More Time) // 09.2026 //  | campagne | 2026-09-25 | 69.798 | 470 | 0,67% | 15 |
| 14 | 8/2 Early Access (Pan buyers more than Once) / Non-US Only | campagne | 2026-08-02 | 744 | 5 | 0,67% | 0 |
| 15 | 8/19 72 Hours Reminder / Non- US Only | campagne | 2026-08-19 | 24.234 | 157 | 0,65% | 12 |

Opvallend:
- Campagnes met de hoogste percentages zijn sales met een "founder note" of plain text naar brede of internationale lijsten: "Founder Note Sale" (0,96%), INTL-01 Birthday Sale (0,97%), AU-01 (0,85%), October Email 6 (0,75%, naar Engaged 30 + All buyers + INT).
- "Sunday Recipe Day | 30 Days Engaged" (4 okt) ging niet naar Engaged 30 Days maar naar de volledige Email List (134.371 ontvangers, Smart Sending uit, 56 spamklachten: de hoogste van alle campagnes). De naam klopt niet met het publiek.
- In v4 · Welcome draait de oude tak nog: "Old · Welcome 1" (4,52%) en "Old · Welcome 2" (2,75%) kregen op 23 okt nog 652 ontvangers.

## 2. De sunset-flow

### Trigger en filters (live sinds 8 okt, `TbYQmX`)

| Onderdeel | Instelling |
|---|---|
| Trigger | Toegevoegd aan segment `WuHSm6` "v4 · Sunset · unengaged 120d" (82.025 leden op 24 okt). |
| Segmentdefinitie | Mag e-mailmarketing ontvangen · meer dan 7 mails ontvangen in 120 dagen · Active on Site 0 keer in 120 dagen · Placed Order 0 keer in 180 dagen · Clicked Email met Bot Click niet waar 0 keer in 120 dagen · profiel minstens 120 dagen oud. Opens tellen niet mee. |
| Profielfilters flow | Niet in deze flow in 180 dagen · geen Welcome-mail (`T4a5Mk`) in 30 dagen · geen Post-purchase-mail (`X3ySuU`) in 30 dagen. Opnieuw instromen na 180 dagen. |
| S1 `UYqHSs` | Dag 1, 09:00 lokale tijd. "Should we keep writing to you?", afzender Siraat's Kitchen, Smart Sending uit. Knop "Yes, keep me on the list" linkt naar de homepage (`utm_content=s1-cta1`). Bevat ook "Choose fewer emails" en "Unsubscribe in one tap". |
| S2 `UTMtx4` | 4 dagen later, 09:00. "Last email from me (unless you tap)", afzender Benjamin at Siraat's Kitchen, Smart Sending uit. Alleen als sinds de start geen menselijke klik, geen sitebezoek en geen order. |
| Daarna | **Niets.** Geen profieleigenschap, geen suppressie, geen uitsluitingssegment. De spec (`klaviyo/flows/v4-flow-system.md` 2.8) had een stap 3 met `sunset_status = suppressed` en een wekelijkse suppressie; die is nooit gebouwd (ook vastgesteld op 15 okt in LOG.md). |
| Vervolg bij klik | Segment `YxfuJT` (menselijke klik in `TbYQmX` in 7 dagen) start v4 · Sunset · kept (`Wzz6xC`): S3 na 30 minuten, S4 na 4 dagen. |

### Instroom per week (S1 ontvangen)

| Week | S1 ontvangen | S2 ontvangen |
|---|---|---|
| 5 tot 11 okt (vanaf 9 okt) | 889 | 0 |
| 12 tot 18 okt | 4.346 | 2.388 |
| 19 tot 24 okt (deels) | 3.019 | 3.469 |
| **Totaal sinds start** | **8.254** | **5.857** |

Een segmenttrigger vuurt alleen voor wie er nieuw in valt. De 82.025 profielen die al in het segment zaten toen de flow live ging, hebben nooit S1 gehad. De instroom van circa 4.000 per week bestaat vooral (59 procent) uit aanmelders van juni die nu 120 dagen oud worden.

### Wat elke mail doet

| Mail | Ontvangers | Afmeldingen | Spam | Menselijke klikkers (profielen) | Waarvan op keep-knop of hero | Bot-kliks |
|---|---|---|---|---|---|---|
| S1 | 8.254 | 64 (0,78%) | 2 | 23 (0,28%) | 17 | 5 |
| S2 | 5.857 | 27 (0,46%) | 2 | 14 (0,24%) | 11 | 18 |
| Totaal flow | 14.111 mails | 91 | 4 | **37 unieke profielen (0,45% van S1)** | 28 | 23 |

Van de 37 menselijke klikkers klikten 9 nooit op de keep-knop of de hero (wel op voorkeurenlink, logo of footer), waarvan 4 alleen op de voorkeurenlink. Ook die tellen nu als "gebleven". S3 (kept) ging naar 34 profielen, S4 naar 19. Afmelden levert de flow dus 2,5 keer zoveel op als blijven (91 tegen 37).

### Wat gebeurt er met wie niet klikt

Ze blijven gewoon ingeschreven. Van de 1.420 niet-klikkers bij wie S2 minstens 7 dagen geleden is, kreeg 60 procent daarna weer een campagne (gemiddeld 0,63 per week; minder dan het lijstgemiddelde omdat de HS-campagnes sinds 8 okt vooral naar "HS // Engaged 180 Days Email" gaan). Slechts 5 van de 92 campagnes sinds 26 juli sluiten het sunsetsegment uit. De mail belooft "If you don't tap, we'll stop writing in about a week" en "this is the last one": die belofte wordt niet gehouden. Dat kost vertrouwen en is een klachtenrisico.

### Heractivatie en omzet

- 37 menselijke klikkers op 8.254 ontvangers (0,45 procent).
- 5 orders van S1-ontvangers na S1, $1.167,54 (alle kanalen), waarvan 3 van een klikker. Geen enkele order toegeschreven aan `TbYQmX` of `Wzz6xC`.
- Vergelijk met de oude sunset (`S7V4a7`, nu draft): 20.361 mails in 90 dagen, 0,52 procent klik, 0,56 procent afmelding.

### Is de definitie van "inactief" goed?

- **Klik in plaats van open: goed.** 77 procent van alle opens is een machine-open (Apple Mail Privacy, zie `research/lijstkwaliteit/01-giveaway-instroom.md`). Het segment gebruikt terecht alleen menselijke kliks, sitebezoek en orders.
- **Maar de campagnesegmenten gebruiken wel opens.** "EB [DG] Engaged 90 Days" (`TMaWCL`, 90.521), "HS // Engaged 90 Days" (`VKxqyA`, 90.521), "HS // Engaged 180 Days Email" (`W5PSSp`, 129.383) en "Engaged 30 Days" (`TNdhKc`, 56.764) tellen een open met `machine_open` niet waar mee. Ter vergelijking: op 20 sep waren er 36.840 profielen met een menselijke klik of order in 90 dagen of jonger dan 30 dagen. "Engaged" is dus 2,5 keer zo groot als de groep die echt iets doet.
- **120 dagen is te laat.** 37 procent van de afmelders vertrekt in de eerste 30 dagen en 22 procent is al 90 dagen stil maar nog geen 120 dagen. Op het moment van afmelden voldeed 21 procent (5.583 profielen in 90 dagen) al aan de sunsetdefinitie, terwijl ze nog campagnes kregen.
- **"Received meer dan 7 in 120 dagen" is zinnig** (wie weinig mail kreeg, is niet inactief maar onbereikt).
- **De klikregel voor "kept" is te ruim**: elke klik telt, ook voorkeurenpagina, logo en footer. Alleen een klik op de keep-knop zou moeten tellen.
- **Smart Sending staat uit** op S1 en S2. Daardoor kan S1 op dezelfde dag als een campagne landen.

## 3. Profiel van wie zich afmeldt (90 dagen, 26.691 unieke profielen)

### Bron van aanmelding

| Bron | Afmelders | Aandeel | Aandeel onder alle ontvangers | Afgemeld in 90 dagen per ontvanger | Waarvan koper |
|---|---|---|---|---|---|
| Kortingspop-up (Alia) | 12.965 | 48,6% | 40,2% (82.965) | 15,6% | 19% |
| Oude Klaviyo-formulieren | 4.609 | 17,3% | 29,0% (59.924) | 7,7% | 28% |
| Giveaway (Alia) | 4.399 | 16,5% | 13,5% (27.927) | 15,8% | 8% |
| Checkout of Shopify-account | 2.996 | 11,2% | 10,5% (21.621) | 13,9% | 93% |
| Onbekend of import | 1.656 | 6,2% | 6,5% (13.366) | 12,4% | 66% |
| Alia overig | 66 | 0,2% | 0,3% | 10,0% | 18% |

"Alle ontvangers" = profielen die tussen 16 jul en 24 okt minstens één mail kregen (206.465). Giveaway en kortingspop-up schrijven zich even vaak af (15,8 tegen 15,6 procent), wat het eerdere onderzoek bevestigt. 62 procent van de giveaway-afmelders vertrekt in de eerste 7 dagen.

### Leeftijd op de lijst bij afmelding

| Leeftijd | Afmelders | Aandeel | Waarvan koper |
|---|---|---|---|
| 0 tot 7 dagen | 5.799 | 21,7% | 709 |
| 7 tot 14 dagen | 1.781 | 6,7% | 437 |
| 14 tot 30 dagen | 2.378 | 8,9% | 659 |
| 30 tot 60 dagen | 4.216 | 15,8% | 1.309 |
| 60 tot 90 dagen | 2.373 | 8,9% | 1.028 |
| 90 tot 180 dagen | 4.931 | 18,5% | 1.862 |
| 180 tot 365 dagen | 4.797 | 18,0% | 1.857 |
| Ouder dan 365 dagen | 416 | 1,6% | 174 |

### Koper of niet-koper, en status op het moment van afmelden

- 30 procent was koper (minstens één order vóór de afmelding), 70 procent niet.

| Status bij afmelding | Afmelders | Aandeel | Spamklachten |
|---|---|---|---|
| Nieuw (jonger dan 30 dagen) | 9.958 | 37,3% | 404 |
| Stil (90 dagen geen klik of order, nog geen sunset) | 5.757 | 21,6% | 262 |
| Voldoet aan sunsetdefinitie (120 dagen) | 5.583 | 20,9% | 249 |
| Actief (klik of order in 90 dagen) | 5.393 | 20,2% | 169 |

### Een maand vooruit: wat elke groep oplevert en kost

Profielen die op 20 september op de lijst stonden en in de 30 dagen ervoor mail kregen, gevolgd tot 20 oktober (alle kanalen).

| Groep op 20 sep | Profielen | Campagnes per profiel | Flowmails per profiel | Afgemeld | Spam | Klikt | Koopt | Omzet per profiel | Omzet totaal |
|---|---|---|---|---|---|---|---|---|---|
| Nieuw (jonger dan 30 dagen) | 17.266 | 10,4 | 6,4 | 11,7% | 0,59% | 9,5% | 1,45% | $3,55 | $61.249 |
| Actief (klik of order in 90 dagen) | 19.574 | 12,8 | 1,4 | 7,7% | 0,28% | 14,9% | 1,80% | $4,13 | $80.843 |
| Stil 90 dagen, nog geen 120 | 43.705 | 11,8 | 0,7 | 3,8% | 0,17% | 2,3% | 0,32% | $0,80 | $35.142 |
| Sunsetdefinitie (120 dagen) | 75.410 | 9,1 | 0,1 | 2,7% | 0,15% | 2,1% | 0,20% | $0,55 | $41.783 |

Van de omzet van de twee stille groepen kwam $32.317 van mensen die in de 5 dagen voor hun order op een mail klikten ($16.499 stil, $15.818 sunset); de rest kocht zonder klik. Met 1 september als startdatum is het beeld gelijk.

### Mails in de 7 en 30 dagen voor afmelding

| | Afmelders (vanaf 16 aug, 21.420) | Gemiddelde ontvanger (steekproef 40.000, 8 meetmomenten) |
|---|---|---|
| Mails in 7 dagen ervoor, gemiddeld (mediaan) | 3,6 (3) | 3,0 (3) |
| waarvan campagnes / flows | 2,2 / 1,4 | |
| Mails in 30 dagen ervoor, gemiddeld (mediaan) | 10,1 (10) | 10,4 (10) |
| waarvan campagnes / flows | 6,8 / 3,4 | |
| Aandeel met 5 of meer mails in 7 dagen | 31% | |
| Flowmail én campagne in de 24 uur ervoor | 5,2% (1.122) | |

### Kans op afmelden per campagnemail (16 aug tot 18 okt)

| Leeftijd op de lijst | Campagnemails | Zonder flowmail in 24 uur ervoor | Met flowmail in 24 uur ervoor | 0 tot 2 mails in 7 dagen ervoor | 3 tot 4 | 5 tot 6 | 7 of meer |
|---|---|---|---|---|---|---|---|
| 0 tot 14 dagen | 153.535 | 0,94% | **1,30%** | 1,27% | 0,94% | 1,01% | 1,07% |
| 14 tot 30 dagen | 190.759 | 0,76% | 1,07% | 0,81% | 0,79% | 0,62% | 0,64% |
| 30 tot 90 dagen | 633.848 | 0,50% | 0,50% | 0,54% | 0,48% | 0,47% | 0,56% |
| 90 dagen en ouder | 2.074.063 | 0,35% | 0,42% | 0,42% | 0,30% | 0,29% | 0,32% |

Lezing:
- **Leeftijd verklaart het meeste.** Een campagnemail aan iemand van minder dan 14 dagen kost 2,9 keer zoveel afmeldingen als aan iemand van meer dan 90 dagen.
- **Meer mails per week verhoogt de kans per mail niet.** Wie veel mail verdraagt, blijft; wie het niet verdraagt, is al weg. Frequentie werkt via het totale volume: elke extra campagnemail kost 0,35 tot 1 procent kans op afmelding, ongeacht hoeveel er al waren.
- **Overlap tussen flow en campagne doet wel pijn, maar alleen bij nieuwe aanmelders** (plus 38 procent in de eerste 14 dagen, plus 42 procent in dag 14 tot 30). Nieuwe aanmelders krijgen in hun eerste 30 dagen 10,4 campagnes plus 6,4 flowmails, bijna 4 per week. Het segment "v4 · Welcome protection" (`XdK77b`) bestaat, maar is sinds 8 okt maar bij 1 van de 10 campagnes uitgesloten (Floris, 9 okt).

### Campagnemails per groep ontvangers (16 aug tot 18 okt)

| Ontvanger op moment van verzenden | Campagnemails | Aandeel | Afmeldingen | Per mail | Spam per 1.000 |
|---|---|---|---|---|---|
| Nieuw (jonger dan 30 dagen) | 344.294 | 11% | 3.029 | 0,88% | 0,83 |
| Actief (klik of order in 90 dagen) | 483.084 | 16% | 3.010 | 0,62% | 0,33 |
| Stil (geen klik of order in 90 dagen) | 2.224.827 | **73%** | 7.516 (**55%**) | 0,34% | 0,26 (57% van de klachten) |
| Land US | 1.587.114 | 52% | 5.813 | 0,37% | 0,33 |
| Land niet-US | 1.216.759 | 40% | 6.236 | **0,51%** | 0,30 |
| Land onbekend | 248.332 | 8% | 1.506 | 0,61% | 0,50 |

Per publiekstype: zonder engagementfilter (Email List, US Subscribers, INT, Email Only) 0,42 procent, Engaged 180/365 dagen 0,39 procent, Engaged 90 dagen 0,46 procent, Engaged 30 dagen 0,68 procent (hier zitten de nieuwe aanmelders in), kopers 0,49 procent.

## 4. Trend per week (12 weken)

| Week vanaf | Campagnemails | Campagnes (300+ ontvangers) | Flowmails | Afmeldingen | waarvan campagne | waarvan flow | Per mail | Spam | Spam per 1.000 |
|---|---|---|---|---|---|---|---|---|---|
| 27 jul | 240.577 | 8 | 66.901 | 1.583 | 1.085 | 498 | 0,51% | 140 | 0,46 |
| 3 aug | 240.665 | 10 | 74.308 | 1.848 | 1.177 | 671 | 0,59% | 140 | 0,44 |
| 10 aug | 221.933 | 6 | 74.574 | 1.800 | 1.150 | 650 | 0,61% | 149 | 0,50 |
| 17 aug | 185.789 | 7 | 70.141 | 1.704 | 943 | 761 | 0,67% | 174 | 0,68 |
| 24 aug | 88.313 | 2 | 65.181 | 1.607 | 723 | 884 | 1,05% | 112 | 0,73 |
| 31 aug | 274.047 | 6 | 69.236 | 2.428 | 1.544 | 884 | 0,71% | 260 | 0,76 |
| 7 sep | 357.503 | 7 | 72.305 | 2.287 | 1.539 | 748 | 0,53% | 226 | 0,53 |
| 14 sep | 358.962 | 4 | 67.118 | 2.108 | 1.436 | 672 | 0,49% | 138 | 0,32 |
| 21 sep | 272.317 | 5 | 68.448 | 1.938 | 1.217 | 721 | 0,57% | 148 | 0,43 |
| 28 sep | 675.483 | 9 | 65.464 | 3.371 | 2.655 | 716 | 0,45% | 256 | 0,35 |
| 5 okt | 488.215 | 6 | 64.856 | 2.487 | 1.830 | 657 | 0,45% | 262 | 0,47 |
| 12 okt | 312.212 | 4 | 53.933 | 2.192 | 1.603 | 589 | 0,60% | 292 | 0,80 |
| 19 okt (deels) | 112.074 | 3 | 47.864 | 1.198 | 746 | 452 | 0,75% | 163 | 1,02 |

Nieuwe aanmelders op Email List per week: circa 4.800 in augustus, 3.500 tot 5.000 in september en oktober, waarvan via de giveaway-pop-up: 32 procent in de week van 31 aug (1.815), daarna 52 tot 88 procent (4.239 in de week van 5 okt).

Wat veranderde:
- **24 tot 30 aug**: weinig campagnes (2), maar het hoogste percentage per mail (1,05 procent): de afmeldingen kwamen uit de welkomstflow (884 flowafmeldingen, de piek van de nieuwe aanmelders) en uit de staart van eerdere sends.
- **31 aug**: start van de giveaway-pop-up en van brede sends naar de volledige Email List en US Subscribers (Labor Day, "September is hard", US Exclusion Sale). Afmeldingen van 1.600 naar 2.400 per week, spam naar 0,76 per 1.000.
- **Vanaf 11 sep**: HS-campagnes (bureau) naar Email List plus All buyers plus US Subscribers plus INTL, 116.000 tot 139.000 ontvangers per stuk.
- **28 sep tot 4 okt**: 675.483 campagnemails in één week (9 campagnes, Prime Sale US en INT, Founder Note Sale, Sunday Recipe Day naar de hele lijst). Record: 3.371 afmeldingen.
- **8 okt**: v4-flows live (nieuwe Welcome, Sunset). Flowvolume daalt van 65.000 naar 48.000 tot 54.000 per week. De HS-campagnes gaan sindsdien naar "HS // Engaged 180 Days Email" (115.000 tot 118.000): smaller dan de volledige lijst, maar nog steeds op opens gebaseerd.
- **12 tot 24 okt**: minder campagnemails, maar hogere percentages (0,60 en 0,75 procent) en de hoogste spamratio van de periode (0,80 en 1,02 per 1.000). Bijdragers: Sale Push en Cutting Board (31 en 26 klachten), October Email 6 naar Engaged 30 plus INT (0,75 procent), welkomstflow (63 klachten in 13 dagen op 26.108 mails, 2,4 per 1.000, tegen 1,3 per 1.000 in de vier weken ervoor) en Failure to launch (38 klachten op 36.739 mails, 1,0 per 1.000, was 0,6). De week van 19 okt is nog niet compleet.

## 5. De vijf grootste oorzaken en wat we doen

Basis: circa 10.400 afmeldingen per 30 dagen. Campagneomzet ligt rond $110.000 per maand (1 aug tot 21 okt: $304.800). De schattingen hieronder overlappen deels; samen verwachten we 30 tot 40 procent minder afmeldingen, niet de optelsom.

### 1. Campagnes naar stille profielen (30 tot 120 dagen geen klik of order)

**Cijfers.** 73 procent van alle campagnemails gaat naar mensen zonder klik of order in 90 dagen. Zij leveren 55 procent van de campagneafmeldingen en 57 procent van de campagneklachten. De groep "stil, nog geen 120 dagen" (43.705 op 20 sep) kreeg 11,8 campagnes per maand: 1.637 afmeldingen (16 procent van het maandtotaal) en 72 klachten, 0,32 procent kocht, $0,80 per profiel.

**Maatregel.** Standaardpubliek voor elke campagne wordt "klik, order of sitebezoek in 90 dagen" plus "nieuw 0 tot 30 dagen", met menselijke kliks in plaats van opens (nieuw segment, of `TMaWCL` aanpassen zodat Opened Email eruit gaat). Stille profielen krijgen maximaal 1 campagne per week: de beste van de week, met Smart Sending aan. Bij grote momenten (BFCM-start, kerst-cutoff) mag de bredere lijst mee. 10 procent van de stille groep als controle die het oude ritme houdt.

**Verwacht effect.** Campagnes aan deze groep van 2,8 naar 1 per week (min 65 procent): **min 800 tot 1.000 afmeldingen per maand**, min 35 tot 45 klachten. **Omzet:** de groep leverde $16.499 per maand aan klikgedreven omzet; bij een derde van het volume verwachten we daar 30 tot 40 procent van te missen, dus **min $5.000 tot $6.500 per maand bruto**. Daartegenover staat betere inbox-plaatsing op de hele campagneomzet (1 procent beter = $1.100 per maand). Controlegroep beslist na 30 dagen.

### 2. Sunset vangt bijna niemand en onderdrukt niemand

**Cijfers.** 82.025 profielen voldoen aan de sunsetdefinitie maar kregen nooit S1. Ze ontvingen in 30 dagen 786.556 campagnemails (44 procent van alle campagnemail). Die groep (75.410 op 20 sep) leverde in een maand 2.062 afmeldingen (20 procent van het totaal) en 112 klachten, 0,20 procent kocht, $0,55 per profiel. De flow zelf: 0,45 procent klikt, $1.168 omzet, 60 procent van de niet-klikkers krijgt daarna weer campagnes.

**Maatregel.**
1. Stap 3 bouwen zoals gespecificeerd: na S2 plus 3 dagen een split op menselijke klik op de keep-knop, sitebezoek of order; ja wordt `sunset_status = kept`, nee wordt `sunset_status = suppressed`. Segment "v4 · Sunset · suppressed" uitsluiten van alle campagnes en wekelijks bulk-suppressen (na akkoord).
2. De 82.025 bestaande leden in porties van 10.000 per week door S1 en S2 sturen (bijvoorbeeld via een lijst als tweede ingang, of een kloon van `TbYQmX` met een lijsttrigger), zodat de inbox-reputatie niet in één keer schrikt.
3. "Kept" alleen bij een klik op `s1-cta1` of `s2-cta1` (URL bevat `utm_content=s1-cta1` of `s2-cta1`), niet op voorkeurenlink, logo of footer.
4. Smart Sending aan op S1 en S2.
5. Tot dat staat: sunsetsegment `WuHSm6` uitsluiten bij elke campagne.

**Verwacht effect.** De groep verdwijnt via suppressie in plaats van via afmelden of klagen: **min 1.700 tot 1.900 afmeldingen per maand** en **min circa 100 klachten per maand** (ongeveer 12 procent van alle klachten), campagnevolume min 35 tot 40 procent. **Omzet:** de groep had $15.818 klikgedreven omzet per maand, maar de sunset zelf haalt maar 0,45 procent terug, dus het risico is reëel: **min $5.000 tot $15.000 per maand bruto**. Daarom met 10 procent controle per portie (die blijft campagnes krijgen) en na twee porties beslissen. Bijvangst: 80.000 profielen minder in de Klaviyo-staffel. En we houden de belofte die S1 en S2 doen.

### 3. Welkomstmails 1 en 2 kosten 2 tot 4,5 procent per mail

**Cijfers.** Flowmails in de eerste 14 dagen: 4.558 afmeldingen in 9 weken, circa **2.200 per maand (21 procent van het totaal)**. Per mail: Old · Welcome 1 4,52 procent, EB Welcome #1 2,94 procent en #2 2,49 procent, nieuwe W1 2,14 procent en W2 2,18 procent, W3 1,36 procent. Welkomstklachten verdubbelden in de laatste twee weken naar 2,4 per 1.000. PLAYBOOK: boven 1 procent is een probleem.

**Maatregel.**
- Oude tak in `T4a5Mk` echt laten leeglopen (Old · Welcome 1 tot 8 kregen op 23 okt nog 652 ontvangers): nagaan waarom er nog instroom in de oude tak is.
- W1 en W2: verwachting zetten (wat je krijgt en hoe vaak), de link "Choose fewer emails" bovenin zoals in de sunsetmail, en in W1 nadrukkelijk het lot van de giveaway bevestigen zodat de mail herkend wordt.
- W1 niet binnen een paar uur na W0 laten landen.
- Afmeldingen van A/B-varianten voortaan meetellen (dashboard en dagrapport): W1 leek 0,10 procent.

**Verwacht effect.** W1 en W2 van gemiddeld 2,1 naar 1,3 tot 1,5 procent: **min 600 tot 750 afmeldingen per maand**. **Omzet:** licht positief. Een nieuwe aanmelder levert $3,55 in de eerste maand (alle kanalen); als de helft daarvan echt extra is, is dat **plus $1.000 tot $1.300 per maand**, oplopend omdat ze op de lijst blijven.

### 4. Campagnes bovenop de welkomstflow bij nieuwe aanmelders

**Cijfers.** Nieuwe aanmelders (0 tot 14 dagen) kregen 153.535 campagnemails in 9 weken, met 1.575 afmeldingen: circa **750 per maand (7 procent)**. Per campagnemail 1,0 procent, en 1,30 procent als er in de 24 uur ervoor een flowmail kwam (0,94 procent zonder). Nieuwe aanmelders krijgen in 30 dagen 10,4 campagnes plus 6,4 flowmails. "v4 · Welcome protection" (`XdK77b`) is sinds 8 okt maar bij 1 van de 10 campagnes uitgesloten.

**Maatregel.** `XdK77b` standaard uitsluiten bij alle campagnes, behalve één campagne per week die nieuwe aanmelders wel krijgen (met Smart Sending aan en niet op een dag met een welkomstmail). Afspraak met HS: dit segment staat altijd in de uitsluitingen. Holdout 90/10 zoals voorgesteld in het giveaway-onderzoek.

**Verwacht effect.** **Min 350 tot 450 afmeldingen per maand**, min 20 tot 30 klachten. **Omzet:** klein risico, **min $1.000 tot $3.000 per maand bruto**, want de welkomstflow draagt de eerste aankoop en de 1 campagne per week blijft. Meten met de holdout.

### 5. Niet-US-ontvangers krijgen US-campagnes

**Cijfers.** 40 procent van de campagnemails gaat naar profielen buiten de US. Per mail 0,51 procent afmelding tegen 0,37 procent in de US, plus 0,61 procent bij onbekend land. Het verschil met de US kost circa **830 afmeldingen per maand (8 procent)**. Hoogste campagnes: INTL-01 Birthday Sale 0,97 procent, AU-01 0,85 procent, Prime Sale INT 0,53 procent, October Email 6 met INT 0,75 procent.

**Maatregel.** Eigen INT-versie van elke salecampagne (prijzen en verzendkosten per land, geen Labor Day of Prime als kapstok), maximaal 2 campagnes per week naar INT, US-only acties strikt naar `VJkN42`, en land onbekend behandelen als INT.

**Verwacht effect.** Een kwart tot een derde van het verschil: **min 200 tot 300 afmeldingen per maand**. **Omzet:** neutraal tot positief (relevantere aanbiedingen), niet te kwantificeren zonder INT-omzet per campagne.

### Samenvatting

| # | Oorzaak | Aandeel nu | Maatregel | Afmeldingen per maand | Omzet per maand |
|---|---|---|---|---|---|
| 1 | Campagnes naar stille profielen | 16% (plus deel van 2) | Publiek op klik in plaats van open, stil max 1 per week | min 800 tot 1.000 | min $5.000 tot $6.500 bruto, controle |
| 2 | Sunset vangt niemand en onderdrukt niemand | 20% | Stap 3 bouwen, 82.000 leden in porties, kept alleen op knop | min 1.700 tot 1.900 | min $5.000 tot $15.000 bruto, controle |
| 3 | Welkomstmail 1 en 2 | 21% | Oude tak leeg, verwachting en minder-mail-link | min 600 tot 750 | plus $1.000 tot $1.300 |
| 4 | Campagnes bovenop welkomstflow | 7% | `XdK77b` uitsluiten, 1 campagne per week | min 350 tot 450 | min $1.000 tot $3.000 bruto |
| 5 | Niet-US krijgt US-campagnes | 8% | INT-versie, max 2 per week | min 200 tot 300 | neutraal tot positief |
| | **Samen (met overlap)** | | | **min 3.000 tot 4.000 (30 tot 40%)** | **min $10.000 tot $23.000 bruto als alles tegelijk gaat, vóór inbox-effect** |

Het omzetrisico zit vrijwel helemaal in 1 en 2. Die gaan daarom met een controlegroep. Een daling van de spamratio naar onder 0,3 per 1.000 beschermt de hele $110.000 campagneomzet per maand; één procent betere inbox-plaatsing compenseert al $1.100.

Bijvangst buiten de top 5: Failure to launch (`T2SmtR`, BACKLOG 5) stuurde 315.339 mails in 90 dagen met 1.513 afmeldingen en 276 klachten, evenveel klachten als de hele welkomstflow, voor $0,04 per ontvanger. Inkorten naar 3 mails haalt naar schatting 150 tot 250 afmeldingen en 40 tot 50 klachten per maand weg (aanname: volume min 60 procent, latere mails iets minder riskant).

## 6. Kanttekeningen

- Klachten komen alleen van providers met een feedbackloop (Outlook/Hotmail, Yahoo, Comcast). Gmail (56 procent van de mail) meldt niet per klacht terug. Absolute spamcijfers zijn dus onderteld; de verhoudingen tussen groepen zijn wel bruikbaar.
- "Stil" is hier gemeten op klik en order, niet op sitebezoek. Het Klaviyo-segment telt sitebezoek wel mee en is daardoor iets kleiner.
- De omzet per groep is via alle kanalen. Welk deel echt door mail komt, is niet te scheiden; "klikgedreven" (klik in de 5 dagen voor de order) is de bovengrens van wat mail kan verliezen.
- De sunset-flow draait pas 16 dagen; de cijfers per mail zijn klein (37 klikkers).
- De week van 19 okt is deels (tot 24 okt 12:00 UTC).

## 7. Open punten

- Waarom stromen er nog profielen in de oude tak van `T4a5Mk` (Old · Welcome)?
- Spamratio per provider (Received per Inbox Provider) toevoegen aan het dagrapport (BACKLOG 13).
- Na de eerste portie sunset (punt 2): omzet per profiel van controle tegen suppressie na 30 dagen.
