# TbYQmX · v4 · Sunset: te agressieve copy

Urgentie-sprint 8 nov 2026, rol FLOWS-AGRESSIEF. Bewust te harde baseline voor Floris, die per flow met de hand afzwakt. Alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Copy in het Engels, toelichting in het Nederlands. Elke regel mag alleen live als 'waar als' op het verzendmoment klopt; anders terug naar de huidige copy.

- Flow: `TbYQmX` (Added to List), status live, 2 live e-mailstappen (oude armen met 0% instroom niet meegeteld).
- Laatste 14 dagen (25 okt tot 8 nov, conversie RSNxYV): 17.035 ontvangers (8.517 per week), $154 omzet, $0,01 per ontvanger, 0,36% unieke klik.
- Echte deadlines in deze flow: Echt nu: 'we stop writing' is waar als [SUNSET] klopt; BF-einde 30 nov. 8.517 ontvangers per week tegen $0,009: de enige echte deadline voor deze groep is het afscheid zelf. Na onderdrukking is 'last email at this price' echt waar.

Risico: groen = waar zodra de voorwaarde klopt, geen spamwoorden; oranje = caps, emoji, verliesframing of een datumblok/segment nodig; rood = nu niet waar of alleen met extra techniek (live GIF, order-edit, nieuwe code). Rood nooit sturen voordat het waar is gemaakt.

## Overzicht

| Mail | Positie | 14 d ontvangers | RPR 14 d | Huidig onderwerp | Agressief onderwerp 1 | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| SUNSET · S1 | 1 d na trigger | 9.155 | $0,02 | Should we keep writing to you? | Should we stop writing? (up to 70% off ends Nov 30) | groen |
| SUNSET · S2 | 5 d na trigger | 7.880 | $0,00 | Last email from me (unless you tap) | Last email from me, and the last one at this price | groen |

## SUNSET · S1

- Berichten: SUNSET · S1 (`UYqHSs`, template `XXvAMt`)
- Positie: 1 d na trigger. 14 dagen: 9.155 ontvangers, $154 omzet, $0,02 per ontvanger.
- Huidig onderwerp: Should we keep writing to you?
- Huidige preview: One tap keeps you on the list. No tap, and we'll stop writing in about a week.
- Huidige hero en CTA: Quick question: still want our emails? One tap keeps you on the list. · knop: Yes, keep me on the list, Choose fewer emails

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Should we stop writing? (up to 70% off ends Nov 30) | [SALE70]; [BFEND] | groen |
| Subject 2 | One tap, or we stop in a week. Black Friday ends {{DEADLINE_SHORT}}. | [SUNSET]; [BFEND] | groen |
| Subject 3 | Stay or go? Decide before {{DEADLINE_SHORT}} ⏰ | [SUNSET]; S2 komt vóór {{DEADLINE}} | oranje |
| Preview 1 | One tap keeps you on the list. No tap and we stop writing in about a week. | [SUNSET] | groen |
| Preview 2 | If you go, you miss up to 70% off and 5 free gifts until {{DEADLINE}}. | [SALE70]; [GIFTS5]; [BFEND] | groen |
| Hero | Still want us?\|One tap, or we stop. | [SUNSET] | groen |
| CTA | Yes, keep me on the list | [SUNSET] | groen |
| Deadline-regel | No tap within a week, and this list stops. Black Friday stops {{DEADLINE}}. | [SUNSET]; [BFEND] | groen |
| PS | P.S. Staying is free. So are the 5 gifts with any order until {{DEADLINE}}. | [GIFTS5]; [GIFTSEND] | groen |

## SUNSET · S2

- Berichten: SUNSET · S2 (`UTMtx4`, template `XCYzpT`)
- Positie: 5 d na trigger. 14 dagen: 7.880 ontvangers, $0 omzet, $0,00 per ontvanger.
- Huidig onderwerp: Last email from me (unless you tap)
- Huidige preview: One tap and you stay. Otherwise this is goodbye, and that's okay.
- Huidige hero en CTA: (geen hero-beeld; tekstmail) · knop: Keep me on the list, Choose fewer emails

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Last email from me, and the last one at this price | [LASTFLOW]; [SUNSET] (na onderdrukking echt geen mail meer, dus ook [LASTPRICE] waar) | groen |
| Subject 2 | This is goodbye. Up to 70% off ends Nov 30. | [SUNSET]; [BFEND] | groen |
| Subject 3 | LAST EMAIL: one tap keeps you (and your 70% off) ⏰ | [SUNSET]; [SALE70] | oranje |
| Preview 1 | One tap and you stay. Otherwise this is goodbye, and Black Friday ends {{DEADLINE}} without you. | [SUNSET]; [BFEND] | groen |
| Preview 2 | Last chance to stay on the list, and last email with these prices. | [SUNSET]; [LASTFLOW] | groen |
| Hero | Last email.\|Unless you tap. | [SUNSET] | groen |
| CTA | Keep me on the list | [SUNSET] | groen |
| Deadline-regel | After this email we stop writing to you. Black Friday ends {{DEADLINE}}. | [SUNSET]; [BFEND] | groen |
| PS | P.S. Want the sale but fewer emails? Choose fewer, and you still hear about the last day. | voorkeurenpagina werkt en BF-slotmail gaat naar 'fewer'-segment | oranje |

## Verleidelijk, maar nooit waar voor Siraat (zonder backend-wijziging)

| Regel | Waarom niet |
| --- | --- |
| FINAL NOTICE / Account closure | Klinkt als phishing en er sluit geen account. |
| You'll lose your gifts | Gifts horen bij een order, niet bij het abonnement op de lijst. |

## Voorwaarden in deze flow

- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[LASTFLOW]** dit is echt de laatste mail van deze flow voor dit profiel (geen stap meer erna)
- **[LASTPRICE]** na deze mail krijgt dit profiel geen mail meer met deze prijs: alleen waar op 30 nov ([BF30]) of als het profiel tot 30 nov uit alle BF-campagnes is gesloten. Anders misleidend, want campagnes lopen door
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
- **[SUNSET]** het profiel wordt na S2 zonder klik echt onderdrukt of uit de marketinglijst gehaald (flow-actie of segmentregel, controleren)
