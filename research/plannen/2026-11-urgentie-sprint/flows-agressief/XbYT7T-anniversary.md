# XbYT7T · v4 · Anniversary: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `XbYT7T` (Metric), status live, 3 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 0 ontvangers (0 per week), $0 omzet, $0 per ontvanger, 0% unieke klik.
- Echte deadlines in deze flow: Echt nu: SK_ANNIV15_7D (one use, 7 dagen) in CODE · N2, HI10 in N1, BF-einde. N1 op 182 dagen, N2 op 365 dagen: weinig ontvangers vóór 30 nov. Huidige N2-templates zeggen nog 'Your 4 gifts end when the fall sale ends': achterhaald.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| N1 | 182 d na trigger | 0 | - | Six months in. Anything worn off? | Six months in. Black Friday ends Nov 30. | groen |
| N2 nocode · cooldown | 365 d na trigger | 0 | - | One year ago this week | One year ago this week. Black Friday ends Nov 30. | groen |
| CODE · N2 | 365 d na trigger | 0 | - | One year in. Here's 15% off. | One year in: your 15% expires in 7 days | groen |
| NIEUW · N2-REM (voorstel, dag 6 na CODE · N2) | nieuwe stap | - | - | (nieuw) | Your 15% expires tomorrow | groen |

## N1

- Berichten: N1 (`RbGbXP`, template `VB9ERB`)
- Positie: 182 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: Six months in. Anything worn off?
- Huidige preview: There was nothing on it to wear off. Here's what owners add at six months.
- Huidige hero en CTA: Six months in. Nothing worn off: half a year of cooking, no coating. Extra 10% off with HI10 and 4 gifts. · knop: Find my second piece

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Six months in. Black Friday ends Nov 30. | [BFEND] | groen |
| Subject 2 | Nothing worn off. Your second piece is up to 70% off until {{DEADLINE_SHORT}}. | [SALE70]; [BFEND] | groen |
| Subject 3 | ENDS TONIGHT: your six-month piece + HI10 ⏰ | [BF30]; [HI10] | oranje |
| Preview 1 | There was nothing on it to wear off. Extra 10% with HI10 until the sale ends {{DEADLINE}}. | [HI10]; [BFEND] | groen |
| Preview 2 | What owners add at six months, up to 70% off with 5 gifts until {{DEADLINE}}. | [SALE70]; [GIFTS5] | groen |
| Hero | Six months.\|Nothing worn off. | geen backend-voorwaarde (geen claim) | groen |
| CTA | Find my second piece now | [SALE70] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. HI10 works once. The sale under it ends {{DEADLINE}}. | [HI10]; [BFEND] | groen |

## N2 nocode · cooldown

- Berichten: N2 nocode · cooldown (`WyXQvg`, template `XRk6hV`)
- Positie: 365 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: One year ago this week
- Huidige preview: A year ago this week you placed your first order. 74 years left on your warranty.
- Huidige hero en CTA: One year ago this week. A year on titanium: 74 years left on your warranty. 4 gifts with every order. · knop: (geen knop gevonden)

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | One year ago this week. Black Friday ends Nov 30. | [BFEND] | groen |
| Subject 2 | 74 years left on your warranty. Days left on this price. | [W75]; alleen in de laatste dagen van BF ([BF48]) zeggen 'days' | oranje |
| Subject 3 | ENDS TONIGHT: your anniversary piece at up to 70% off ⏰ | [BF30] | oranje |
| Preview 1 | A year ago you placed your first order. Up to 70% off until {{DEADLINE}}. | [SALE70]; [BFEND] | groen |
| Preview 2 | 5 free gifts with every order until {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |
| Hero | One year in.\|74 to go. | [W75] | groen |
| CTA | Shop with my 5 gifts | [GIFTS5] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. Prices go back up, the 5 free gifts stop. | [BFEND]; [GIFTSEND] | groen |
| PS | P.S. Your warranty runs 74 more years. The sale runs until {{DEADLINE}}. | [W75]; [BFEND] | groen |

## CODE · N2

- Berichten: CODE · N2 (`Sm72RF`, template `VP2rKg`)
- Positie: 365 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: One year in. Here's 15% off.
- Huidige preview: A year ago you placed your first order. Your own 15%, for 7 days.
- Huidige hero en CTA: One year, 15% for 7 days. A year on titanium: 74 years left on your warranty. Plus 4 gifts. · knop: Get my 15% now

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | One year in: your 15% expires in 7 days | [ANNIV7] | groen |
| Subject 2 | Your 15% ENDS {{DEADLINE_SHORT}} ⏰ | [ANNIV7] | oranje |
| Subject 3 | Use it or lose it: your anniversary 15% | [ANNIV7] | oranje |
| Preview 1 | A year ago you placed your first order. Your own 15%, one use, until {{DEADLINE}}. | [ANNIV7] | groen |
| Preview 2 | Already applied with the button. On {{DEADLINE}} it stops working. | [ANNIV7]; knop zet de code | groen |
| Hero | Your own 15%.\|Gone {{DEADLINE_SHORT}}. | [ANNIV7] | groen |
| CTA | Use my 15% before it expires | [ANNIV7] | groen |
| Deadline-regel | Your 15% expires {{DEADLINE}}. One use. | [ANNIV7] | groen |
| PS | P.S. 15% on top of up to 70% off, if you order before Nov 30. | SK_ANNIV15_7D stapelt op de sale (DECISIONS 19 okt: flowcodes stapelen); [BFEND] | groen |

## NIEUW · N2-REM (voorstel, dag 6 na CODE · N2)

- Berichten: geen (voorstel voor een nieuwe flowstap).
- Huidig onderwerp: (nieuw)
- Huidige preview: (nieuw)
- Huidige hero en CTA: (geen hero-beeld; tekstmail) · knop: (geen knop gevonden)
- Noot: Nieuwe stap; bestaat niet in Klaviyo.

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your 15% expires tomorrow | NIEUWE stap op dag 6, alleen als code ongebruikt; [ANNIV7] | groen |
| Subject 2 | FINAL DAY: your anniversary 15% ⏰ | stap op dag 7, [ANNIV7] | oranje |
| Subject 3 | Order now: {{MINUTES_LEFT}} minutes left on your 15% | [MINS]; [ANNIV7] | rood |
| Preview 1 | One use, already applied. It stops working {{DEADLINE}}. | [ANNIV7] | groen |
| Preview 2 | After tomorrow, no anniversary code until next year. | er komt echt geen nieuwe jubileumcode binnen 12 maanden (flowlogica) | groen |
| Hero | Last day.\|Your 15%. | [ANNIV7] | groen |
| CTA | Use my 15% now | [ANNIV7] | groen |
| Deadline-regel | Expires {{DEADLINE}}. | [ANNIV7] | groen |
| PS | P.S. That's the only reminder. | [LASTFLOW] | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your 15% expires tonight (op dag 1) | De code geldt 7 dagen; alleen waar op de laatste dag met een extra stap. |
| Your warranty is expiring | 74 jaar resterend; nooit. |

## Voorwaarden in deze flow

- **[ANNIV7]** SK_ANNIV15_7D (one use) vervalt echt 7 dagen na uitgifte; template toont 'ENDS' met days_later:7, {{DEADLINE}} = die datum
- **[BF30]** de mail gaat uit op 30 nov (laatste BF-dag) en saleprijs, BFCODE en gifts stoppen echt op {{DEADLINE}}. In een flow alleen via een datumblok in onderwerp en hero ({% today %}-vergelijking, getest) of doordat Floris op 30 nov de onderwerpen omzet (PATCH flow-action) en op 1 dec terugzet; andere dagen valt de regel terug op de [BFEND]-versie
- **[BF48]** de mail gaat uit op 29 of 30 nov (laatste 48 uur van BF), zelfde datumblok als [BF30]; 'last chance' en 'final hours' alleen dan
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[HI10]** HI10 werkt bovenop de sale, one use per klant; HI10 heeft geen einddatum, dus nooit 'HI10 expires'
- **[LASTFLOW]** dit is echt de laatste mail van deze flow voor dit profiel (geen stap meer erna)
- **[MINS]** {{MINUTES_LEFT}} alleen naast een live countdown-GIF (Sendtric/NiftyImages) die naar de echte backend-eindtijd telt en daarna ENDED toont; als statische tekst nooit
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
- **[W75]** 75 jaar garantie (DECISIONS 1 okt)
