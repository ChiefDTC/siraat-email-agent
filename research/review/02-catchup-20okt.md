# Review-inhaalcampagne (20 okt 2026): fulfilled 20 sep tot 19 okt zonder reviewvraag

Probleem: reviewflow XzHrez (Delivered Shipment +14 dagen) start alleen op Delivered Shipment (VcUF33), en dat event komt maar bij ongeveer 40% van de orders. Vangnet TvfJYU (Fulfilled Order +21 dagen) staat sinds 19 okt 19:55 UTC live, maar pakt alleen fulfilments vanaf dat moment. Klanten die tussen 20 sep en 19 okt fulfilled zijn zonder Delivered Shipment kregen dus nooit een reviewvraag. Deze inhaalcampagne vult dat gat, in twee golven. Alles staat als CONCEPT: niets verstuurd, niets ingepland, geen previews, geen flowwijzigingen.

## Methode

Alleen geaggregeerde cijfers hier. Per-profieldata staat buiten de repo (scratchpad/review-catchup/).

1. Kandidaten: profielen met Fulfilled Order (VtEiZT) van 20 sep 00:00 UTC tot 19 okt 19:55 UTC (livegang TvfJYU), plus de 253 profielen van lijst UXBmYd (opnieuw getoetst met dezelfde regels).
2. Bezorgbewijs per order (op order-id of ordernummer gekoppeld aan de fulfilled order in het venster):
   - Klaviyo Delivered Shipment (VcUF33, Shopify);
   - Klaviyo Delivered (SMpL9v, ShipBob-tracking);
   - Klaviyo "Postflows - 4. Shipment Delivered" (UabgWz): carrier-tracking via de Postflows-app, status shipment_delivered;
   - voor orders zonder één van deze drie: Shopify Admin (fulfillments displayStatus en deliveredAt) en ShipBob (search-shipments, tracking_status Delivered), alleen gelezen.
   Bezorgdatum = vroegste bewijs. Geen bewijs = uitgesloten.
3. 12-delige set: elk Placed Order-event ooit met "Titanium Hammered Cookware Set" en "12-Pcs" in Items (dekt ook de "+ FREE PIZZA STEEL"-varianten), zelfde als het flowfilter.
4. Supportcontact: Gorgias (alleen gelezen) via de analytics-koppeling order-id naar Gorgias-klant naar tickets, alle tijd, inclusief spam. Alle 1.278 orders van de overgebleven profielen zijn in Gorgias teruggevonden. Extra vangnet: Klaviyo-events Opened Ticket en Resolved Ticket (Gorgias) en Ticket Created, alle tijd. Eén ticket in één van beide bronnen = uitgesloten.
5. Al reviewmail: Received Email sinds 15 aug met $flow XzHrez, TvfJYU of de oude reviewflows Vixr6X, SxEWJV, UvHra2 (zelfde regel als de backfill), of de backfillcampagne (niet verstuurd, dus 0). Plus wie al in de wachtrij van een reviewflow zit: Delivered Shipment na livegang XzHrez (6 okt 20:34 UTC) of een Fulfilled Order na livegang TvfJYU. Zij krijgen de flowmail, anders dubbel.
6. Refund (Xg6cwn) of annulering (TFervq) sinds 1 sep.
7. E-mailmarketing: consent moet SUBSCRIBED zijn en geen suppressie.

## Trechter

| Stap | Eraf | Over |
|---|---|---|
| Kandidaten (3.353 fulfilled + 253 uit UXBmYd, 100 overlap) | | 3.506 |
| Profiel niet meer leesbaar (samengevoegd of verwijderd) | 4 | 3.502 |
| Al een reviewmail gehad (vrijwel allemaal oude flow Vixr6X) | 604 | 2.898 |
| Zit al in wachtrij XzHrez of TvfJYU | 1.078 | 1.820 |
| Refund of annulering | 18 | 1.802 |
| Geen bezorgbewijs | 182 | 1.620 |
| Ooit de 12-delige set gekocht | 27 | 1.593 |
| Geen marketingtoestemming of onderdrukt | 350 | 1.243 |
| Ooit contact met support (Gorgias 397, alleen Klaviyo-ticketevent 14) | 411 | 832 |

Volgorde van toetsen is anders dan in de opdracht, omdat de dure checks (Shopify, ShipBob, Gorgias) alleen op wie overblijft zijn gedaan. Elke uitsluiting is definitief, de volgorde verandert het eindgetal niet.

Bezorgbewijs bij de 832: Postflows 797, Delivered Shipment 19, ShipBob 16. De Shopify- en ShipBob-check op 191 profielen (194 orders) zonder Klaviyo-bewijs leverde 2 extra bezorgde orders op; Shopify kent bij de Postflows-orders geen bezorging (vervoerder "Other", dus geen Delivered Shipment) en ShipBob verzendt ze niet. Postflows is daar de enige bron die "delivered" zegt.

Van de 253 uit UXBmYd blijven er 35 over: 168 eraf door supportcontact, 27 geen toestemming meer, 22 de 12-delige set (dat filter zat niet in de backfill).

## Golven

| Golf | Regel | Profielen | Klaviyo-lijst | Campagne (Draft) | Template |
|---|---|---|---|---|---|
| 1 | bezorgd tot en met 13 okt | 608 | RtpJBt "Review catch-up golf 1 (22 okt)" | 01M5CSHE3FYPP6JSSHHSE3P2RQ "Review catch-up · golf 1 · 22 okt" | WHMSBy (kloon van TuCKL4) |
| 2 | bezorgd na 13 okt | 224 | VeGwpV "Review catch-up golf 2 (3 nov)" | 01M5CSHG8HEQ089278KBZ863SP "Review catch-up · golf 2 · 3 nov" | VQT4WK (kloon van TuCKL4) |

Beide campagnes: onderwerp "Win your purchase amount back", preview "Two minutes. One honest review.", afzender en reply-to zoals de backfill, smart sending AAN, UTC (niet lokaal), datum 22 okt en 3 nov 14:00 UTC als richtwaarde, status Draft, niet ingepland. UTM utm_campaign v4-review-catchup-g1 en -g2. Template-HTML identiek aan TuCKL4 (de reviewmail uit de backfill en de flow); ordernummer in de sterlinks blijft leeg in een campagne, net als bij de backfill.

Lijst UXBmYd (253) en campagne 01M538JS4KMBVEPZ94EB90JB6X zijn niet aangeraakt.

## Openstaande punten

1. Postflows als bezorgbewijs: 797 van de 832 hebben alleen carrier-tracking via Postflows als bewijs (geen Delivered Shipment, Shopify zegt alleen "fulfilled", ShipBob verzendt deze orders niet). Telt Floris dat niet als bewijs, dan blijven er 35 over (golf 1: 35, golf 2: 0). Floris beslist.
2. Backfillcampagne 01M538JS4KMBVEPZ94EB90JB6X kan weg: de 35 die er nog in horen zitten in golf 1, de andere 218 voldoen niet meer (vooral supportcontact). Verwijderen alleen na akkoord.
3. Gorgias-analytics loopt ongeveer een dag achter; tickets van vandaag zijn mogelijk niet meegenomen (de Klaviyo-ticketevents vangen een deel op). Vlak voor verzending opnieuw toetsen.
4. Golf 2 vóór 3 nov opnieuw toetsen (refunds, nieuwe tickets, uitschrijvingen, eventuele reviewmail uit TvfJYU). Wie nu nog geen bezorgbewijs heeft maar later wel, kan dan ook nog in golf 2.
5. Uitsluiting op oude reviewflow Vixr6X (604) geldt sinds 15 aug, ook als die mail over een eerdere order ging. Strenger dan het flowfilter (30 dagen); bewust voorzichtig.
6. Supportregel telt elk ticket, ook door een agent gestarte mails en chats vóór aankoop. Strikt zoals gevraagd.
7. Verzenden of inplannen alleen na akkoord Floris, eerst een testmail per golf.
