# YhQJdb · AFF S1 vangnet · Fulfilled +12d (geen Postflows): te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `YhQJdb` (Metric), status live, 4 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 0 ontvangers (0 per week), $0 omzet, $0 per ontvanger, 0% unieke klik.
- Echte deadlines in deze flow: Zelfde mails als R22pzb voor orders zonder Postflows-event.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| A1 · announce (vangnet) | 14 d na trigger | 0 | - | Your order can pay for itself | Your friends are shopping Black Friday. Send your link before Nov 30. | groen |
| A2 · nudge-1 (vangnet) | 17 d na trigger | 0 | - | Has anyone asked about your pan? | Has anyone asked about your pan? Answer before Nov 30. | groen |

## A1 · announce (vangnet)

- Berichten: AFF S1 · A1 · announce · na review · vangnet (`SPVPkk`, template `UCmGQP`), AFF S1 · A1 · announce · vangnet (`TsWRWX`, template `VfnKts`)
- Positie: 14 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: Your order can pay for itself
- Huidige preview: Friends get 15% off their first order. You get 15% of what they pay.
- Huidige hero en CTA: Two friends in a kitchen at night, one holding a hammered titanium pan · knop: Share my link, your dashboard

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your friends are shopping Black Friday. Send your link before Nov 30. | [AFF]; [BFEND] (BF is het moment dat vrienden kopen) | groen |
| Subject 2 | Your order can pay for itself. Best week to share: this one. | [AFF]; 'best week' waar zolang BF loopt (hoogste verkeer) | oranje |
| Subject 3 | ENDS NOV 30: your friends' 15% on top of Black Friday | [AFFSTACK]; 15% heeft zelf geen einde, dus de regel gaat over de BF-prijs | rood. Alleen als de 15% echt stapelt op de saleprijs. |
| Preview 1 | Friends get 15% off. You get 15% of what they pay. Black Friday ends {{DEADLINE}}. | [AFF]; [BFEND] | groen |
| Preview 2 | Every friend who orders before {{DEADLINE}} also gets 5 free gifts. | [AFF]; [GIFTS5]; [GIFTSEND] | groen |
| Hero | Your order can pay for itself.\|Share before {{DEADLINE_SHORT}}. | [AFF]; [BFEND] | groen |
| CTA | Share my link now | [AFF] | groen |
| Deadline-regel | Black Friday ends {{DEADLINE}}. That's when your friends are buying. | [BFEND] | groen |
| PS | P.S. Eight friends and your whole order is back. | staat al in de template (8 vrienden x 15%, max $50 per order); berekening per ordergrootte | oranje |

## A2 · nudge-1 (vangnet)

- Berichten: AFF S1 · A2 · nudge-1 · na review · vangnet (`RzTJ76`, template `VaKv84`), AFF S1 · A2 · nudge-1 · vangnet (`TZkEec`, template `XAcrfa`)
- Positie: 17 d na trigger. 14 dagen: 0 ontvangers, $0 omzet, $0 per ontvanger.
- Huidig onderwerp: Has anyone asked about your pan?
- Huidige preview: That is the moment your link pays. Give 15%, get 15%.
- Huidige hero en CTA: A hammered titanium pan passed across a dinner table · knop: Share my link, your dashboard

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Has anyone asked about your pan? Answer before Nov 30. | [AFF]; [BFEND] | groen |
| Subject 2 | The moment your link pays: Black Friday | [AFF]; [BFEND] | groen |
| Subject 3 | Share now: your friends' Black Friday ends {{DEADLINE_SHORT}} ⏰ | [AFF]; [BFEND] | oranje |
| Preview 1 | That's the moment your link pays. Give 15%, get 15%, while Black Friday runs until {{DEADLINE}}. | [AFF]; [BFEND] | groen |
| Preview 2 | Save your link in your notes now. Your friends have until {{DEADLINE}} for Black Friday prices. | [AFF]; [BFEND] | groen |
| Hero | Someone will ask.\|Have your link ready. | [AFF] | groen |
| CTA | Share my link now | [AFF] | groen |
| Deadline-regel | Black Friday prices for your friends end {{DEADLINE}}. | [BFEND] | groen |
| PS | P.S. Your 15% is paid 45 days after their order ships. | uitbetaling 45 dagen na verzending via Tremendous (DECISIONS 21 okt) | groen |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| Your link expires tonight | De Snowball-link vervalt niet. |
| Double commission ends tonight | Bestaat niet; alleen met [AFFDL]. |
| Your friends' 15% ends Nov 30 | De vriendenkorting heeft geen einddatum. |

## Voorwaarden in deze flow

- **[AFF]** Snowball-link en 15/15 zijn actief voor dit profiel
- **[AFFSTACK]** de 15% vriendenkorting stapelt in Shopify echt op de BF-saleprijs (combinatie-instelling controleren); anders niet zeggen
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
