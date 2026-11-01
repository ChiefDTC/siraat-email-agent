# Review-inhaalcampagne golf 3 (1 nov 2026): wie nog nooit een reviewvraag kreeg

Vraag: welke klanten met een betaalde, verzonden order kregen tot nu toe geen enkele reviewmail, ook niet uit golf 1 (21 okt) of golf 2 (28 okt)? Uitkomst: 51 profielen. Lijst en campagne staan klaar als CONCEPT: niets verstuurd, niets ingepland, geen flow aangeraakt.

Alleen geaggregeerde cijfers hier. Per-profieldata staat buiten de repo (scratchpad/review-golf3/).

## Venster

- Fulfilled Order (VtEiZT) van 20 sep 2026 00:00 UTC tot 19 okt 2026 19:55 UTC (livegang vangnet TvfJYU). Zelfde venster als golf 1 en 2: golf 3 pakt wie daar toen buiten viel (vooral "zit al in wachtrij XzHrez", die de flowmail toch nooit kreeg, en wie toen nog geen bezorgbewijs had).
- Vanaf 19 okt 19:55 dekt TvfJYU (Fulfilled + 21 d, eerste mails rond 9 nov). Vanaf 1 nov ~14:30 UTC dekken T5riz5 (Postflows) en TF2B5x (ShipBob) nieuwe bezorgingen.
- 50 van de 51 zijn fulfilled tot en met 18 okt (minstens 14 dagen geleden), 1 op 19 okt.
- Vóór 20 sep niet opnieuw bekeken: daar liep de oude reviewflow Vixr6X nog.

## Regels (zelfde als golf 2, twee aanpassingen)

1. Order telt alleen als `$value` > 0, financial status paid of partially_refunded en niet geannuleerd. Nieuw: $0-orders (TikTok-affiliates) eruit.
2. Al reviewmail: Received Email sinds 15 aug met $flow XzHrez, TvfJYU, T5riz5, TF2B5x of de oude reviewflows Vixr6X, SxEWJV, UvHra2, of een mail uit golf 1, golf 2 of de backfillcampagne. Let op: bij campagnes staat in `$message` het campagne-id, niet het bericht-id.
3. Wachtrij: Delivered Shipment (VcUF33) sinds 18 okt (XzHrez stuurt na 14 dagen dus komt nog), een nieuwe Fulfilled Order na 19 okt 19:55 (TvfJYU), of Postflows/ShipBob-bezorging na 1 nov 14:30 (nieuwe flows).
4. Refund (Xg6cwn) of annulering (TFervq) sinds 1 sep.
5. Ooit de 12-delige set gekocht (Placed Order, zelfde filter als de flows).
6. E-mailmarketing: consent SUBSCRIBED en geen suppressie.
7. Supportcontact ooit: Gorgias (analytics, order-id naar klant naar tickets, inclusief spam, alle 425 orders teruggevonden) plus Klaviyo-events Opened Ticket, Resolved Ticket en Ticket Created.
8. Bezorgbewijs is geen harde eis meer (tweede aanpassing). TvfJYU stuurt ook zonder bewijs op Fulfilled + 21 dagen; bij verzending op 4 nov is elke order uit het venster minstens 16 dagen fulfilled, 50 van de 51 minstens 17. 7 van de 51 hebben geen bewijs.

## Trechter

| Stap | Eraf | Over |
|---|---|---|
| Profielen met fulfilled order in venster | | 3.353 |
| Alleen $0-orders of volledig terugbetaald | 126 | 3.227 |
| Profiel niet leesbaar (samengevoegd of verwijderd) | 4 | 3.223 |
| Al een reviewmail (golf 1 of 2: 793, XzHrez 664, oude flow Vixr6X 594, overlap mogelijk) | 2.038 | 1.185 |
| Zit nog in wachtrij XzHrez, TvfJYU of nieuwe flows | 223 | 962 |
| Refund of annulering sinds 1 sep | 25 | 937 |
| Ooit de 12-delige set gekocht | 37 | 900 |
| Geen marketingtoestemming of onderdrukt | 488 | 412 |
| Ooit contact met support (Gorgias 350, alleen Klaviyo-ticketevent 11) | 361 | 51 |

De supportregel weegt zwaar: golf 1 en 2 hebben iedereen zonder ticket al gehad, dus wat overblijft is vooral wie toen om een ticket werd uitgesloten.

## De 51

| Orderweek (maandag, UTC) | Profielen |
|---|---|
| 14 sep | 2 |
| 21 sep | 4 |
| 28 sep | 6 |
| 5 okt | 28 |
| 12 okt | 11 |

| Land | Profielen |
|---|---|
| US | 35 |
| Buiten de US | 16 (AU 4, SG 3, SA 2, CA 2, ES, IE, KW, CH, NZ elk 1) |

Bezorgbewijs: Postflows 42, Delivered Shipment 1, ShipBob 1, geen 7.

## Advies

- Volume is klein. Golf 1 had 2,7% unieke klikken (16 op 599), golf 2 3,8% (8 op 214). Op 51 is dat 1 tot 2 klikken, hooguit 1 review. Wel bijna gratis: kloon van een bestaande mail, en het gat 20 sep tot 19 okt is daarmee dicht.
- Timing: nu versturen, niet wachten tot de veegactie van 17 nov. Deze orders zijn 3 tot 6 weken geleden geleverd; elke week later scoort slechter, en vanaf half november loopt de BF-druk op (BFCM kopers 13, 27 en 30 nov, BF-content in de flows sinds 31 okt, Homestead om de 1 à 2 dagen om 08:15 UTC).
- Voorstel: woensdag 4 nov 14:00 UTC (10:00 ET), smart sending aan, mits die ochtend geen Homestead-campagne gaat; anders donderdag 5 nov. Hercheck dezelfde ochtend (refund, nieuwe tickets, uitschrijving, reviewmail uit een flow).
- Te beslissen door Floris: de supportregel. Alleen tickets ná de order tellen (spam niet) levert op orderniveau ongeveer 35 orders extra op; geen open ticket en geen ticket in de laatste 30 dagen ongeveer 87 extra. Beide zijn op orderniveau geteld, niet per profiel. Dat is meer volume, met meer kans dat de mail bij iemand met een probleem landt.

## Klaar in Klaviyo (Draft)

| | |
|---|---|
| Lijst | YsBcUY "Review golf 3 (1 nov)", 51 profielen |
| Campagne | 01M6BQVP3TDA6ERSKMRVKYVXK8 "Review catch-up · golf 3 · 4 nov", status Draft, niet ingepland |
| Bericht | 01M6BQVP5220HS0DZ0538GMVJW, template S3Ku6i (HTML identiek aan golf 2 VQT4WK) |
| Instellingen | kloon van golf 2: onderwerp "Win your purchase amount back", preview "Two minutes. One honest review.", afzender en reply-to gelijk, smart sending aan, UTC (niet lokaal), richtdatum 4 nov 14:00 UTC, UTM utm_campaign v4-review-catchup-g3 |

Versturen of inplannen alleen na akkoord Floris, eerst een testmail.

## Niet geverifieerd

- Gorgias-analytics loopt ongeveer een dag achter; tickets van vandaag kunnen ontbreken (Klaviyo-ticketevents vangen een deel op).
- Bezorgevents in Klaviyo zijn sinds ~22 okt veel lager (zie log 28 okt); voor dit venster maakt dat weinig uit, wel voor de 7 zonder bewijs.
- XzHrez, TvfJYU, T5riz5 en TF2B5x staan live (gecontroleerd 1 nov). Sinds 14:30 waren er geen Postflows- of ShipBob-bezorgingen voor deze profielen.
- Orders vóór 20 sep niet opnieuw getoetst.
