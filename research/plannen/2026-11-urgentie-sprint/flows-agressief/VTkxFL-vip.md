# VTkxFL · v4 · VIP: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `VTkxFL` (Metric), status live, 4 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 6 ontvangers (3 per week), $0 omzet, $0,00 per ontvanger, 0,00% unieke klik.
- Echte deadlines in deze flow: Echt nu: profiel heeft 2+ orders; de sale is voor iedereen ('for everyone' staat in de template), dus 'VIP ONLY' is pas waar met een eigen VIP-code. CODE · V1 heeft nu geen coupon. 6 ontvangers in 14 dagen.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| V1 (nocode en CODE) | 30 d na trigger | 6 | $0,00 | You're a VIP. Thank you. | VIP ONLY: your own 15% on top, ends {{DEADLINE_SHORT}} | rood |
| V2 (Benjamin) | 40 d na trigger | 0 | - | A question from Benjamin | A question from Benjamin (before Black Friday ends) | groen |

## V1 (nocode en CODE)

- Berichten: V1 nocode · cooldown (`XFLrcf`, template `TXgi26`), CODE · V1 (`TtTByE`, template `Ub94TK`)
- Positie: 30 d na trigger. 14 dagen: 6 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: You're a VIP. Thank you.
- Huidige preview: Two orders makes you a VIP. The Black Friday Sale is live: up to 70% off.
- Huidige hero en CTA: Siraat hammered titanium cookware, dark studio, Black Friday Sale · knop: (geen knop gevonden)

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | VIP ONLY: your own 15% on top, ends {{DEADLINE_SHORT}} | [VIPCODE]; [VIP2] | rood. Pas waar met unieke VIP-code; anders S2. |
| Subject 2 | You're a VIP. Black Friday ends Nov 30. | [VIP2]; [BFEND] | groen |
| Subject 3 | Two orders in. Your third at up to 70% off ends {{DEADLINE_SHORT}} ⏰ | [VIP2]; [SALE70]; [BFEND] | oranje |
| Preview 1 | Two orders makes you a VIP. The pieces you don't have yet are up to 70% off until {{DEADLINE}}. | [VIP2]; [SALE70]; [BFEND] | groen |
| Preview 2 | Your own 15%, one use, until {{DEADLINE}}. On top of Black Friday. | [VIPCODE] | rood |
| Hero | You're a VIP.\|Up to 70% off until {{DEADLINE_SHORT}}. | [VIP2]; [BFEND] | groen |
| CTA | Get my third piece now | [VIP2] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. Every order, even your third, gets 5 free gifts until {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |

## V2 (Benjamin)

- Berichten: V2 (`R4sFry`, template `Xw74Sx`), V2 (`WrJjWZ`, template `Ywfp5B`)
- Positie: 40 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: A question from Benjamin
- Huidige preview: You've ordered twice. I'd love to know what you want us to make next.
- Huidige hero en CTA: (geen hero-beeld; tekstmail) · knop: (geen knop gevonden)

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | A question from Benjamin (before Black Friday ends) | [BFEND] | groen |
| Subject 2 | You've ordered twice. What should we make next? | [VIP2] | groen |
| Subject 3 | Benjamin here: one question, and the sale ends Nov 30 | [BFEND] | groen |
| Preview 1 | I'd love to know what you want us to make next. Reply before {{DEADLINE}} and I read it the same week. | Benjamin of team leest echt replies in die week | oranje |
| Preview 2 | One reply, one idea. And up to 70% off on what we make now, until {{DEADLINE}}. | [SALE70]; [BFEND] | groen |
| Hero | What should we make next? | geen backend-voorwaarde (geen claim) | groen |
| CTA | Reply to Benjamin | reply-to werkt | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. | [BFEND] | groen |
| PS | P.S. Whatever you answer, your 5 free gifts with any order end {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| VIP ONLY: up to 70% off | De sale is voor iedereen; 'VIP only' alleen met [VIPCODE]. |
| VIP early access | Er is geen vroege toegang meer: BF is live voor iedereen. |

## Voorwaarden in deze flow

- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
- **[VIP2]** profiel heeft echt 2 of meer orders (flowtrigger VIP)
- **[VIPCODE]** NIEUW: unieke VIP-code per profiel (DECISIONS 8 okt: VIP krijgt 15%) met echte einddatum {{DEADLINE}}, alleen naar dit segment; CODE V1 heeft nu geen coupon in de template
