# Review backfill (16 okt 2026): gat tussen oude en nieuwe reviewflow

Oude reviewflow Vixr6X ging op 12 okt 06:01 UTC naar draft (gepland). Nieuwe flow XzHrez (Delivered Shipment +14 dagen) live sinds 6 okt 20:34 UTC; eerste mails 21 okt. Klanten bezorgd 20 sep tot 6 okt kregen daardoor vaak geen reviewvraag.

## Lijst (Klaviyo-lijst UXBmYd, 253 profielen)
| Stap | Aantal |
|---|---|
| Delivered Shipment-events 20 sep 00:00 tot 6 okt 20:34 UTC | 1.208 |
| Unieke profielen | 989 |
| Min refund of annulering (1 sep tot 16 okt) en storebot-adressen | 974 |
| Min wie sinds 15 aug een mail kreeg uit Vixr6X, XzHrez, SxEWJV of UvHra2 | 386 |
| Min wie na 6 okt 20:34 opnieuw bezorgd is (staat al in XzHrez-wachtrij) | 362 |
| Mag e-mailmarketing ontvangen (campagne) | 253 |

Scripts en ruwe data: scratchpad/golive/backfill-*.json, backfill_check.py.

## Campagne (CONCEPT, niet ingepland)
- Campagne 01M538JS4KMBVEPZ94EB90JB6X, bericht 01M538JS4YF4AVH6VPGHAPMCB9, template-kopie TuCKL4 van RFcjsS (zelfde reviewmail als de flow, r1-short).
- Onderwerp "Win your purchase amount back", preview "Two minutes. One honest review.", afzender SiraatsKitchen <send@siraatskitchen.com>, zelfde als flowvariant A.
- Smart sending uit, UTM utm_campaign=v4-review-backfill. Render zonder restanten; ordernummer in de sterlinks is leeg (geen event in een campagne).
- Testmail naar Floris 16 okt 21:06 UTC.
- Versturen alleen na akkoord Floris.

## Recente mails van de 253 (check 16 okt 21:15 UTC, Received Email sinds 13 okt)
- Gemiddeld 1,8 mails per persoon; 5 kregen niets, 234 kregen 1 of 2, 14 kregen 3 of meer.
- 239 kregen HS October Email 6 "5-Star Cookware for a 5-Star Experience" (14 okt), 182 kregen HS Email 13 Bundle Push (16 okt 18:15 UTC). 197 kregen een mail in de laatste 24 uur.
- Gepland door Homestead: Email 7 Cutting Board (17 okt, verstuurt nu), Email 8 Dishwasher Sheets (20 okt), Email 9 Bundle Upgrade (23 okt).
- Geen eerdere reviewvraag (al uitgesloten). Advies: versturen zondag 19 okt, tussen Cutting Board (17 okt) en Dishwasher Sheets (20 okt).
