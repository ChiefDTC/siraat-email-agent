# 02 · Timingadvies per flow

Datum: 7 oktober 2026. Onderbouwing: `01-data.md` (sectienummers tussen haakjes). Dit is een voorstel; `klaviyo/flows/v3-flow-system.md` is niet aangepast. Elke regel "Verandert t.o.v. v3" zegt wat er anders is.

## De vijf principes uit onze eigen data

1. **Na 15 minuten is het natuurlijke koopmoment voorbij.** Van wie na 5 minuten nog niet afrekende, koopt 14,3% binnen 15 minuten en maar 4 procentpunt meer in het hele uur daarna (1b). Een mail na 15 tot 30 minuten stoort dus bijna niemand die toch al zou kopen.
2. **Sneller is niet slechter.** In de oude 50/50-split gaf mail 1 na 10 minuten 375 kopers tegen 350 na 30 minuten (+7%, binnen de ruis) (1c). Er is geen bewijs dat een uur wachten beter is; wel dat elk uur wachten 1 tot 2 procent van de verlaters "vanzelf" laat kopen zonder dat wij iets toevoegen.
3. **Een mail werkt 24 tot 48 uur.** 70% van de orders na een klik komt binnen 1 uur na de klik; na een checkoutmail is 77% van de orders binnen 24 uur en 86% binnen 48 uur binnen (4). De volgende mail hoort niet eerder dan 20 tot 24 uur later.
4. **Welkom is een sprint, geen marathon, maar stopt niet op dag 10.** De kans op een eerste aankoop per dag halveert elke 4 tot 5 dagen tot dag 10 (0,50% op dag 1, 0,09% op dag 10) en zakt daarna langzaam (0,04% op dag 31). Dag 10 tot 30 levert nog 1,2% extra kopers op tegen 1,9% in dag 1 tot 10 (6).
5. **Het pakket komt pas na 12 dagen.** Mediaan order tot levering 11,7 dagen, p75 14,7, p90 19,2 (7). Alles wat "nu je pan er is" zegt, moet op levering wachten, niet op een vaste dag na de order.

## Globale regels

| Regel | Advies | Data | Verandert t.o.v. v3 |
| --- | --- | --- | --- |
| Quiet hours | **22:00 tot 07:00** lokaal voor alle vervolgmails. Mail 1 van checkout en cart gaat realtime, ook 's avonds. | Realtime mails 21-22 uur: order 24u 2,66% (even goed als overdag). 22-06 uur: klik 2,6-2,7% tegen 3,2-3,3%, order 1,7-1,8% tegen 2,3-2,6% (3b). 19% van alle orders valt tussen 19:00 en 23:00 (3a). | v3: 21:00 tot 08:00. Twee goede uren per dag erbij. |
| Uitvoering quiet hours | Klaviyo kent (voor zover ik weet) geen quiet hours voor e-mail in flows; doe het met "wacht x dagen, tot HH:MM" in de tijdzone van het profiel. Voor mail 1 geen vertraging tot de ochtend. | | Technische noot bij v3 |
| Verzenduur vervolgmails | Venster 09:00 tot 20:00. Standaard "tot 09:00" (piek orders 09-12 uur), A/B tegen "zelfde uur als de trigger" (zie A/B 2). | Orders pieken 09-12 uur lokaal (7,1-7,4% per uur), weekend 16-17% per dag (3a). | v3 zegt 09:00 voor checkout en 10:00 voor welcome: één tijd, 09:00. |
| Weekdagen | Geen weekdagfilter in flows. | Realtime mails: geen weekdagverschil (klik 2,7-3,4%, order 2,0-2,7%). Weekend is de beste koopdag (3a, 3b). | Geen |
| Smart sending | Uit, zoals v3. | Prioriteit regelt overlap. | Geen |
| Attributievenster | 5 dagen klik, 1 dag open (Klaviyo-instelling niet wijzigen zonder reden). | 88-98% van de orders na een klik valt binnen 5 dagen (4). | Nieuw |
| Tijdzone | Alle delays op "profiel-tijdzone" (bestaande instelling). Profielen zonder tijdzone vallen terug op account (US/Eastern). | 244.493 profielen met tijdzone; AU/UK/US hetzelfde patroon in lokale tijd (3a). | Geen |

## 1. Checkout abandonment

- **Trigger**: Checkout Started (RfMvni, Shopify). De Triple Pixel-variant (RtgBgs) niet meer als trigger gebruiken: twee triggers geven dubbele instap.
- **Flowfilters**: Placed Order = 0 sinds start; niet in deze flow in 14 dagen; niet in post-purchase in 7 dagen (zoals v3).
- **Herinstap**: 14 dagen (zoals v3).

| Stap | Wanneer | Mail | Split | Waarom |
| --- | --- | --- | --- | --- |
| 1 | **30 min** na trigger (geen quiet hours) | C1 | geen | Natuurlijke golf is na 15 min voorbij (14,3% binnen 15 min, +2,5 pp tot 30 min). 10 min gaf +7% kopers tegen 30 min, niet significant. 30 min is de veilige middenweg die nog in de "hete" sessie valt. |
| 2 | **24 uur na C1**, binnen 09:00-20:00 (anders volgende 09:00) | C2 | Eerdere koper: korte versie | 77% van het effect van C1 zit in 24 uur. Oude mail 2 op "dag 1 08:00" was de zwakste ($0,41-0,73); de stap blijft, het moment schuift naar "24 uur later" (test A/B 2). |
| 3 | **dag 3**, tot 09:00 | C3 | Cart >= $300 (S) tegen < $300 (P) | Herstel loopt van 8,7% (24u) naar 10,6% (3d). Oude mail 3 (bonus, dag 3-4) deed $1,34-2,39. |
| 4 | **dag 5**, tot 09:00 | C4 (unieke code 72 uur volgens 04-offer-strategy) | Land US / INT, met terugval | 3d naar 7d herstel nog +1,7 pp; een code die tot dag 8 loopt valt in dat venster. |
| exit | dag 8 | | | Na 7 dagen zakt de kans per dag onder de 0,3%. |

Splits: >= $300 is 27,9% van de verlaters en herstelt 15,5% tegen 11,1% (8): de moeite waard voor inhoud en trede. Eerdere kopers (4,8%) herstellen 26,9%: geen code nodig, korte versie. **Landsplit**: 16% van de verlaters heeft nog geen land in het profiel; gebruik als terugval het eventveld `Customer Locale` (en-US = US) of zet "onbekend" in de INT-tak.
**Verandert t.o.v. v3**: C1 30 min in plaats van 1 uur; C2 24 uur na C1 in plaats van "tot dag 2, 09:00"; C3 dag 3 en C4 dag 5 in plaats van dag 3 en 4 (meer lucht tussen code-mails, deadline loopt door tot dag 8); Triple Pixel-trigger weg.

## 2. Cart abandonment

- **Trigger**: Added to Cart (QXcV8K). Flowfilters zoals v3 (geen Checkout Started en geen order sinds start; niet in checkoutflow in 7 dagen; niet in deze flow in 14 dagen).

| Stap | Wanneer | Mail | Split | Waarom |
| --- | --- | --- | --- | --- |
| 1 | **30 min** | K1 | | Cart-verlaters kopen nauwelijks vanzelf na 15 min (+1,0 pp tussen 30 en 60 min). Oude 15-min-arm deed $2,90 tegen $2,27 bij 30 min. Wie in die 30 min naar checkout gaat valt er via de filter uit. |
| 2 | **24 uur na K1**, venster 09-20 | K2 | Eerdere koper: korte versie | Oude K2 pas op dag 2 tot 08:00: $0,79. Cart-orders komen trager binnen (mediaan 9,5 uur na verzending), dus 24 uur ertussen. |
| 3 | **dag 3**, tot 09:00 | K3 (code) | | Herstel 24u 5,8%, 3d 7,2%, 7d 8,5%. |

Geen waarde-split in cart: >= $300 herstelt niet beter (8,9-9,3% tegen 7,7-12,8%).
**Verandert t.o.v. v3**: K1 30 min in plaats van 1 uur; K2 24 uur na K1 (v3: 1 dag, vrijwel gelijk); K3 dag 3 (gelijk).

## 3. Browse abandonment

- **Trigger**: Viewed Product (Klaviyo onsite XNtYMB). Eén trigger; de Triple Pixel-variant (V48nhq) eruit (zelfde mensen, dubbele instap).
- **Flowfilters**: zoals v3, plus **niet in welcome in de laatste 7 dagen** (zie overlap).

| Stap | Wanneer | Mail | Split | Waarom |
| --- | --- | --- | --- | --- |
| 1 | **1 uur**, quiet hours 22-07 | B1 | | Na 15 min koopt nog 1,9% binnen 1 uur en 2,8% binnen 4 uur: weinig te storen. 1 uur geeft cart/checkout de kans eerst te vuren (de filter checkt op verzendmoment). Oude 10/30-min-mails deden $0,59-1,31 met 1,0-1,8% uitschrijving. |
| 2 | **dag 2**, tot 09:00 | B2 | Klikte B1: ja = productaanbod, nee = reviews (v3) | Orders na een browsemail: mediaan 9,9 uur, 78% binnen 48 uur. |

**Verandert t.o.v. v3**: B1 1 uur in plaats van 4 uur (A/B 3 toetst dit); extra filter "niet in welcome in 7 dagen"; Triple Pixel-trigger weg.

## 4. Welcome

- **Trigger**: toegevoegd aan Email List Uw8eZG.
- **Nieuw: eerst 20 minuten wachten, dan pas splitsen.** 20,3% van de inschrijvers koopt binnen 10 minuten na inschrijving; de inschrijving gebeurt tijdens de aankoop. Een split op moment nul stuurt deze kopers het prospect-pad in (W1 met HI10 na een aankoop). Nu krijgt 10,7% van de ontvangers van welcome-mail 2 en 13,3% van "Last Call 10%" de mail terwijl ze al gekocht hebben (2).
- **Split A na 20 min**: Placed Order sinds flowstart > 0 → geen welcome, post-purchase neemt over (W0 alleen voor wie al vóór de inschrijving klant was, 1,3%). Anders prospect-pad.
- **Verzendfilter op elke mail**: Placed Order = 0 sinds flowstart, en geen mail uit checkout- of cartflow in de laatste 24 uur (stap overslaan, niet uitstappen).

| Stap | Wanneer | Mail | Kans op eerste order die dag (6) | Waarom |
| --- | --- | --- | --- | --- |
| 0 | 20 min | W1 (giveaway + HI10) | 1,3% koopt nog op dag 0 na het eerste uur | Na 20 min is de checkout-golf voorbij (nog ongeveer 1% van de inschrijvers koopt tussen minuut 10 en 20). |
| 1 | dag 1, tot 09:00 | W2 Benjamin | 0,50% | Hoogste kans na dag 0. |
| 2 | dag 3, tot 09:00 | W3 | 0,24% | |
| 3 | dag 6, tot 09:00 | W4 US / INT | 0,13% | |
| 4 | dag 10, tot 09:00 | W5 + HI10-herinnering | 0,09% | Oude dag-10-mail "Last Call 10%" deed $0,26 per ontvanger, drie keer een campagne ($0,086). |
| 5 | dag 14 | einde, naar campagnes | 0,07% | Vanaf dag 14 is welcome niet meer sterker dan de 0,04-0,06% per dag die doorloopt tot dag 30. |

- **Campagnes**: nieuwe inschrijvers zonder order 14 dagen uitsluiten (v3), want 9,8% schrijft zich in week 1 al uit en 12,2% binnen 14 dagen (6).
- **Failure to launch (T2SmtR) uit**: 37% van alle flowmails, 3,9% van de flowomzet, $0,013-0,093 per ontvanger (2). Dag 30-60 levert per dag 0,02-0,04% kopers: dat is campagnewerk.
**Verandert t.o.v. v3**: wachten 20 min vóór split A (v3: split meteen, W0/W1 na 10 min); W1 na 20 min; verzendtijd 09:00 in plaats van 10:00; W5 op dag 10 in plaats van dag 9; filter "geen checkout/cart-mail in 24 uur"; einde dag 14.

## 5. Post-purchase

- **Trigger**: Placed Order. Split eerste koper / herhaalklant (v3).

| Stap | Wanneer | Mail | Waarom |
| --- | --- | --- | --- |
| 1 | 1 uur | P1 wat er komt | Zoals v3. |
| 1b | **Fulfilled Order (VtEiZT) + 0, max dag 5** | Verzendbericht met tracking (als Shopify dit niet al stuurt) | De oude "It's On Its Way" had 29,8% klik, 96% op tracking; in de Founder's Note klikte ook 96% op tracking. Mensen zoeken hun pakket. Fulfilment mediaan 2,8 dagen. Besluit voor Floris: dubbel met de Shopify-verzendmail of niet. |
| 2 | **Delivered Shipment + 1 dag, tot 09:00; vangnet dag 16** | P2 eerste ei | Mediaan levering 11,7 dagen (US 12,0, AU 9,9, UK 10,7), p75 14,7. Maar slechts 36% van de orders krijgt een Delivered Shipment-event (US 37%, CA 9%, overige landen 1%). Conditional split: wel geleverd binnen 16 dagen → P2 dag erna; niet → P2 op dag 16 met tekst die niet aanneemt dat het pakket er is ("When your pan arrives"). |
| 3 | **levering + 7 dagen (vangnet order + 21 dagen)** | P3 wat past bij je pan | v3 zegt 14 dagen na order: dan heeft ongeveer de helft de pan nog niet. Herhaalkopers: 25% binnen 14 dagen, 46% binnen 30 dagen na de eerste order (7). Dag 19-21 valt midden in het venster 14-30 dagen. Tweede order is vooral deksel, tweede pan, snijplank. |
| 4 | levering + 14 dagen, 09:30 | Review (XzHrez, live) | v3 zegt "30 dagen na levering" maar de live flow en PLAYBOOK zeggen 14 dagen. 14 aanhouden. |

**Verandert t.o.v. v3**: P1b tracking-mail (besluit), vangnet dag 16 voor P2, P3 van "14 dagen na order" naar "levering + 7 dagen", review op 14 dagen na levering.

## 6. Winback

- **Trigger**: Placed Order, dan wachten. Filter per stap: geen order sinds start. Herinstap 90 dagen.

| Stap | Wanneer | Mail | Waarom |
| --- | --- | --- | --- |
| 1 | **dag 45** na laatste order, tot 09:00 | R1 nieuw sinds je order / je volgende stuk | Mediaan tijd tot 2e order 35 dagen; 57% van de herhaalaankopen valt binnen 45 dagen. Kans per periode: dag 30-60 1,65%, dag 60-90 0,97% (7). Bij dag 60 is de helft van het venster al weg. |
| 2 | **dag 75**, tot 09:00 | R2 aanbod (VIP 2+ orders sterker) | Kans dag 60-90 nog bijna 1%; daarna 0,6% per 30 dagen. |
| exit | dag 90 | naar campagnes | |

Herhaalklanten (2e naar 3e order mediaan 33 dagen) volgen hetzelfde ritme, dus geen aparte tijdlijn.
**Verandert t.o.v. v3**: R1 dag 45 in plaats van 60; R2 dag 75 in plaats van 90.

## 7. Replenishment (vaatwasstrips)

Niet bouwen op dit moment. 24 Recharge-abonnementen in twee maanden en 160 betaalde strip-orders in twee jaar; de strips zitten als Mystery Gift in de doos en verschijnen niet als product. Er is geen interval te meten. Eerst de bestaande "Mystery Gift Reveal, Sheets"-flow (WvRupU, $0,17-0,32 per ontvanger) laten lopen en een eigen event of profieleigenschap voor "strips ontvangen" toevoegen. Dan na 3 maanden opnieuw kijken.

## 8. Overlap en prioriteit

| Situatie | Hoe vaak | Effect | Advies |
| --- | --- | --- | --- |
| Welcome + browse in dezelfde week | 30,2% van de welcome-weken | uitschrijf 7,24% tegen 5,14% | Browse: filter "niet in welcome in 7 dagen". Welcome doet in week 1 al productuitleg. |
| Welcome + cart | 10,5% | 7,13% tegen 5,62% | Cart wint (v3). Welcome-mail die dag overslaan via verzendfilter "geen cart/checkout-mail in 24 uur". |
| Welcome + checkout | 5,2% | 6,86% tegen 5,72% | Idem. |
| Twee verlatingsflows in een week | 10,9% van de verlatingsweken | geen verschil (5,0 tegen 5,2%) | Prioriteit uit v3 volstaat. |

Het verschil in uitschrijving is deels "actieve mensen krijgen meer mail" en dus geen zuiver effect (9). Het advies is daarom: geen nieuwe exits, wel overslaan van de welcome-mail op een dag met een verkoopmail.

## 9. Frequentie

- Maximaal 3 campagnes per week per profiel. Bij alleen-campagne-ontvangers stijgt de uitschrijving per week van 0,51% (3 mails) naar 0,70-0,76% (4-5 mails); de week van 28 sep met 9 campagnes op 6 dagen gaf 3.408 uitschrijvingen en 187 spamklachten, twee keer normaal (10).
- Flowmails tellen niet mee voor de cap (ze zijn gedragsgestuurd), maar de welcome-uitsluiting van 14 dagen voor campagnes blijft.
- Uitschrijving per mail is het hoogst in welcome (1,82%) en browse (1,42%): daar geen extra mails toevoegen.

## 10. A/B-voorstellen waar de data twijfel laat

Meet elke test op **orders binnen 7 dagen na instap per arm (alle orders, niet Klaviyo-attributie)**, omdat attributie de snelste mail bevoordeelt (1c). Splits via een random-split (`profile-sample`) direct na de trigger. Steekproef: checkout heeft ongeveer 2.400 verlaters per maand; bij 12% basisherstel zie je een verschil van 3 procentpunt (25% relatief) met ongeveer 1.850 per arm, dus 6 tot 8 weken.

| # | Test | Arm A | Arm B | Waarom twijfel | Duur |
| --- | --- | --- | --- | --- | --- |
| 1 | C1-moment | 30 min | 1 uur (v3) | 10 tegen 30 min gaf +7%, niet significant; 1 uur is nooit getest. | 8 weken |
| 2 | C2/K2-moment | 24 uur na mail 1 (zelfde uur) | tot dag 2, 09:00 | Realtime-uren doen 3,2% klik, de 08:00-batch 1,9%, maar dat is ook een andere mail. | 8 weken |
| 3 | B1-moment | 1 uur | 4 uur (v3) | Browse heeft hoge uitschrijving; later kan rustiger zijn. Volume groot genoeg (ongeveer 16.000 per arm per 90 dagen). | 4 weken |
| 4 | Welcome-verzenduur W2-W5 | tot 09:00 | zelfde uur als inschrijving | Welcome-mails om 10:00 doen 1,4% klik tegen 2-3% op andere uren, maar dat zijn andere mails. | 4 weken |
| 5 | Campagne-uur | 08:00 lokaal | 17:30 lokaal | Campagneklik 17-19 uur 0,89% tegen 0,54% om 08-10 uur, maar avondsegmenten waren kleiner en actiever. | 4 campagnes |
| 6 | P3-moment | levering + 7 dagen | levering + 14 dagen | Herhaalkoop piekt 7-21 dagen; de pan moet eerst gebruikt zijn. | 8 weken |

Volgorde: 3 en 4 eerst (meeste volume), dan 1 en 2, dan 6. Eén test per flow tegelijk.

## Overzicht: alle tijden in één tabel

| Flow | Stap 1 | Stap 2 | Stap 3 | Stap 4 | Einde |
| --- | --- | --- | --- | --- | --- |
| Checkout | 30 min | +24 u | dag 3, 09:00 | dag 5, 09:00 (code 72 u) | dag 8 |
| Cart | 30 min | +24 u | dag 3, 09:00 (code) | | dag 6 |
| Browse | 1 uur | dag 2, 09:00 | | | dag 3 |
| Welcome | 20 min (na split) | dag 1, 09:00 | dag 3, 09:00 | dag 6 / dag 10, 09:00 | dag 14 |
| Post-purchase | 1 uur, tracking bij fulfilment | levering + 1 d (vangnet dag 16) | levering + 7 d (vangnet dag 21) | review levering + 14 d | |
| Winback | dag 45 | dag 75 | | | dag 90 |
