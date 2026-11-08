# UEfh4h · EB | Customer Winback | 5/8/25: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `UEfh4h` (Metric), status live, 4 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 6.493 ontvangers (3.246 per week), $436 omzet, $0,07 per ontvanger, 0,42% unieke klik.
- Echte deadlines in deze flow: Oude flow (loopt tot 14 dec, DECISIONS 8 okt). Hero's tonen nog 'SIRAAT PRIME TIME SALE | UP TO 56% OFF' en Email #3 heeft een beeld 'Your 10% Off Ends Tonight' zonder zichtbare code in de HTML: controleren of die 10% echt na 1 dag vervalt, anders is dit nu een nep-deadline live (rood). Copy hieronder vervangt de Prime Time-claim door BF.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| Email #1 | 60 d na trigger | 2.151 | $0,01 | Serving Up New Must-Haves | Up to 70% off, and it ends {{DEADLINE_SHORT}} | groen |
| Email #2 (en Copy of Email #2) | 62 d na trigger | 2.159 | $0,07 | We Cut a Deal for You | We cut a deal for you: 10% on top of Black Friday | oranje |
| Email #3 | 63 d na trigger | 2.183 | $0,12 | 10% Off Expires Tonight | Your 10% expires TONIGHT ⏰ | rood |

## Email #1

- Berichten: Email #1 (`Wrnas5`, template `XYvwWJ`)
- Positie: 60 d na trigger. 14 dagen: 2.151 ontvangers, $32 omzet, $0,01 per ontvanger.
- Huidig onderwerp: Serving Up New Must-Haves
- Huidige preview: What’s new in the kitchen
- Huidige hero en CTA: SIRAAT PRIME TIME SALE / UP TO 56% OFF · knop: ADD TO CART

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Up to 70% off, and it ends {{DEADLINE_SHORT}} | [SALE70]; [BFEND] | groen |
| Subject 2 | New in the kitchen, at Black Friday prices until Nov 30 | [BFEND] | groen |
| Subject 3 | ENDS TONIGHT: up to 70% off + 5 free gifts ⏰ | [BF30] | oranje |
| Preview 1 | Our bestsellers, up to 70% off with 5 free gifts until {{DEADLINE}}. | [SALE70]; [GIFTS5]; [BFEND] | groen |
| Preview 2 | Two months since your order. The biggest sale of our year ends {{DEADLINE}}. | flowdelay 60 dagen; 'biggest sale' waar als er in 2026 geen diepere sale is | oranje |
| Hero | Up to 70% off.\|Until {{DEADLINE_SHORT}}. | [SALE70]; [BFEND] | groen |
| CTA | Get up to 70% off now | [SALE70] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. Every order gets 5 free gifts until {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |

## Email #2 (en Copy of Email #2)

- Berichten: Email #2 (`XWQLLB`, template `SnhBpR`), Copy of Email #2 (`WW78hc`, template `QVNr98`)
- Positie: 62 d na trigger. 14 dagen: 2.159 ontvangers, $145 omzet, $0,07 per ontvanger.
- Huidig onderwerp: We Cut a Deal for You
- Huidige preview: Cook Healthier with 10% Off
- Huidige hero en CTA: SIRAAT PRIME TIME SALE / UP TO 56% OFF · knop: ADD TO CART

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | We cut a deal for you: 10% on top of Black Friday | 10%-code uit deze mail werkt echt bovenop de sale (template controleren) | oranje |
| Subject 2 | Your 10% ends {{DEADLINE_SHORT}} | de 10%-code heeft echt einddatum {{DEADLINE}} (nu onbekend) | rood. Pas waar als Floris de code een echte einddatum geeft. |
| Subject 3 | Up to 70% off + your 10%: Black Friday ends Nov 30 | [BFEND] | groen |
| Preview 1 | Cook healthier with 10% off, on top of up to 70% off, until {{DEADLINE}}. | 10%-code met echte einddatum | rood |
| Preview 2 | 5 free gifts with every order until {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |
| Hero | 10% on top.\|Until {{DEADLINE_SHORT}}. | 10%-code met echte einddatum | rood |
| CTA | Use my 10% now | 10%-code werkt | oranje |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. Black Friday ends {{DEADLINE}}. Your 10% and the gifts go with it. | [BFEND]; code vervalt echt met BF | rood |

## Email #3

- Berichten: Email #3 (`WC4V9Y`, template `XqVJvK`)
- Positie: 63 d na trigger. 14 dagen: 2.183 ontvangers, $259 omzet, $0,12 per ontvanger.
- Huidig onderwerp: 10% Off Expires Tonight
- Huidige preview: Don't let it spoil!
- Huidige hero en CTA: SIRAAT PRIME TIME SALE / UP TO 56% OFF · knop: (geen knop gevonden)

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your 10% expires TONIGHT ⏰ | de 10%-code uit Email #2 vervalt echt vandaag om {{DEADLINE}} | rood. Huidige claim; alleen houden als het waar is. |
| Subject 2 | Last email: up to 70% off ends {{DEADLINE_SHORT}} | [LASTFLOW]; [BFEND] | groen |
| Subject 3 | Use it or lose it: your 10% + Black Friday prices | 10%-code vervalt echt | rood |
| Preview 1 | Don't let it spoil. Your 10% stops at {{DEADLINE}}. | 10%-code vervalt echt op {{DEADLINE}} | rood |
| Preview 2 | Last email in this series. Black Friday ends {{DEADLINE}}. | [LASTFLOW]; [BFEND] | groen |
| Hero | Last email.\|Black Friday until {{DEADLINE_SHORT}}. | [LASTFLOW]; [BFEND] | groen |
| CTA | Use my 10% before it ends | 10%-code vervalt echt | rood |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. No more emails from this series. | [LASTFLOW] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| We miss you: here's 30% off, today only | Er bestaat geen winback-code met einddatum (CODE · R2 heeft nu geen coupon). |
| Your account will be deleted | Verzonnen. |
| Last email at this price (op 1 tot 29 nov zonder campagne-uitsluiting) | Campagnes met dezelfde prijs lopen door; alleen waar met [LASTPRICE]. |
| Your 10% Off Ends Tonight (huidige Email #3, beeld) | Alleen waar als de code uit Email #2 echt 24 uur later vervalt; niet zichtbaar in de template. |

## Voorwaarden in deze flow

- **[BF30]** de mail gaat uit op 30 nov (laatste BF-dag) en saleprijs, BFCODE en gifts stoppen echt op {{DEADLINE}}. In een flow alleen via een datumblok in onderwerp en hero ({% today %}-vergelijking, getest) of doordat Floris op 30 nov de onderwerpen omzet (PATCH flow-action) en op 1 dec terugzet; andere dagen valt de regel terug op de [BFEND]-versie
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[LASTFLOW]** dit is echt de laatste mail van deze flow voor dit profiel (geen stap meer erna)
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
