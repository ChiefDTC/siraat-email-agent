# 01 · Timingdata: cijfers, query's en datakwaliteit

Datum: 7 oktober 2026. Alleen gelezen uit Klaviyo (account TdtTzz, REST revision 2025-10-15). Niets aangemaakt of gewijzigd.
Venster: 12 maanden (8 okt 2025 t/m 7 okt 2026) voor triggers, orders, klikken, inschrijvingen en uitschrijvingen; 90 dagen (9 jul t/m 6 okt 2026) voor Received Email; 7 dagen (29 sep t/m 5 okt) voor Opened Email. Orderhistorie terug tot oktober 2024 voor eerste-of-herhaalkoper.
Scripts: `research/timing/scripts/` (fetch + analyse). Uitkomsttabellen: `research/timing/tabellen/`. Ruwe events staan niet in de repo (bevatten profiel-ID's).

---

## 0. Datasets

| Metric (ID) | Venster | Events | Velden |
| --- | --- | --- | --- |
| Placed Order (RSNxYV) | okt 2024 t/m 7 okt 2026 | 109.142 (90.470 in 12 mnd), 98.538 profielen | $value, Items, Discount Codes, profiel-locatie en tijdzone |
| Checkout Started (RfMvni) | 12 mnd | 129.141 | $value, Items, Customer Locale, locatie |
| Added to Cart (QXcV8K) | 12 mnd | 282.511 | $value, Product Name, locatie |
| Viewed Product, Klaviyo onsite (XNtYMB) | 60 dagen | 132.078 | product, locatie |
| Viewed Product, Triple Pixel (V48nhq) | 60 dagen | 119.850 | product |
| Subscribed to List (SCvkku) | 12 mnd | 291.539 (234.450 op Email List Uw8eZG) | list_id, locatie |
| Clicked Email (W247h8) | 12 mnd | 274.714 | URL, $flow, $message, Bot Click, Handoff Time (verzendmoment) |
| Opened Email (WyrTym) | 7 dagen | 350.121 | machine_open, $flow, Handoff Time |
| Received Email (YkRM4Q) | 90 dagen | 4.420.009 | $flow, $message |
| Unsubscribed from Email Marketing (YcWddQ) | 12 mnd | 91.832 | message_id, method |
| Marked Email as Spam (VQMAAk) | 12 mnd | 6.572 | |
| Delivered Shipment (VcUF33) | 12 mnd | 16.043 | Delivery Hours, Transit Hours |
| Fulfilled Order (VtEiZT) | 12 mnd | 84.028 | FulfillmentHours |
| Flowdefinities | stand 7 okt | SiaNLu, Y2TmNB, Tsg2tV, SwkMyn, TBWngE, Wj6x6V, TyEjuQ, RL3TU6, UEfh4h, T2SmtR, XzHrez | `GET /api/flows/{id}?additional-fields[flow]=definition` |

Query (zo te herhalen):

```
GET https://a.klaviyo.com/api/events
  ?filter=and(equals(metric_id,"RfMvni"),greater-or-equal(datetime,2025-10-07T00:00:00Z),less-than(datetime,2025-10-22T00:00:00Z))
  &fields[event]=datetime,event_properties.$value,event_properties.Items
  &include=profile&fields[profile]=location
  &page[size]=200&sort=datetime
headers: revision: 2025-10-15, accept: application/vnd.api+json
```
`scripts/fetch_events.py METRIC START END OUT "veld1,veld2" CHUNKS [profile]` knipt het venster in stukken en pagineert parallel (6 threads, ongeveer 1.000 events per seconde zonder 429's). Volumes per maand: `POST /api/metric-aggregates` met `interval month`, `timezone US/Eastern` (`scripts/agg.sh`). Maximaal venster daar is 1 jaar.

Methode-afspraken:
- **Episode**: een trigger telt als nieuwe instap als hetzelfde profiel die trigger niet in de 7 dagen ervoor had (benadert de herinstapregel van de flows).
- **Herstel** = eerste Placed Order van hetzelfde profiel na het trigger-moment (niet Klaviyo-attributie).
- **Lokale tijd** = tijdzone uit het Klaviyo-profiel (`location.timezone`), beschikbaar voor 244.493 profielen.
- **Eerste/herhaalkoper** = aantal eerdere Placed Orders sinds oktober 2024.

---

## 1. Natuurlijke herstelcurve (vraag 1)

### 1a. Alle triggers, % dat een order plaatst binnen X (cohort tot 30 sep, dus 7 dagen opvolging)

| Trigger | n episodes | 15 min | 1 uur | 4 uur | 24 uur | 3 dagen | 7 dagen |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Checkout Started | 111.485 | 73,9% | 75,1% | 75,6% | 76,2% | 76,7% | 77,2% |
| Added to Cart | 115.064 | 30,0% | 32,2% | 32,9% | 34,0% | 35,0% | 35,9% |
| Viewed Product (onsite) | 45.246 | 11,3% | 13,0% | 13,7% | 14,8% | 15,8% | 16,9% |
| Viewed Product (Triple Pixel) | 32.789 | 17,1% | 19,9% | 21,0% | 22,7% | 24,4% | 26,1% |

Lezing: driekwart van alle Checkout Started-events is gewoon een geslaagde aankoop (Shopify vuurt het event voor iedereen die het e-mailveld invult). Voor timing telt alleen de groep die na een paar minuten nog niet gekocht heeft.

### 1b. Echte verlaters: wie na X minuten nog niet kocht, % dat daarna alsnog koopt (cumulatief vanaf trigger)

Checkout Started, nog geen order na 15 minuten (n = 29.054):

| Segment | n | 30 min | 1 uur | 2 uur | 4 uur | 12 uur | 24 uur | 3 dagen | 7 dagen |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Alle | 29.054 | 2,9% | 4,6% | 5,6% | 6,3% | 7,4% | 8,7% | 10,6% | 12,3% |
| US | 9.909 | 3,1% | 4,8% | 5,9% | 6,6% | 7,9% | 9,5% | 11,6% | 13,6% |
| Niet-US (bekend land) | 14.576 | 3,7% | 5,8% | 7,1% | 7,9% | 9,3% | 10,9% | 13,1% | 15,2% |
| Cart >= $300 | 8.127 | 3,8% | 5,9% | 7,3% | 8,1% | 9,6% | 11,2% | 13,5% | 15,5% |
| Cart < $300 | 20.927 | 2,6% | 4,1% | 5,0% | 5,6% | 6,6% | 7,8% | 9,5% | 11,1% |
| Nieuwe klant | 27.690 | 2,8% | 4,4% | 5,4% | 6,0% | 7,1% | 8,3% | 10,0% | 11,6% |
| Eerder gekocht | 1.364 | 5,8% | 8,7% | 10,6% | 11,8% | 14,8% | 17,8% | 22,4% | 26,9% |

Checkout, nog geen order na 5 minuten (n = 33.910): 11,5% koopt in minuut 5 tot 10, 14,3% binnen 15 min, 18,3% binnen 1 uur, 21,8% binnen 24 uur, 24,9% binnen 7 dagen.

Added to Cart, nog geen order na 15 minuten (n = 80.597):

| Segment | n | 30 min | 1 uur | 4 uur | 24 uur | 3 dagen | 7 dagen |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Alle | 80.597 | 2,1% | 3,1% | 4,2% | 5,8% | 7,2% | 8,5% |
| US | 32.666 | 2,2% | 3,4% | 4,5% | 6,2% | 7,7% | 9,0% |
| Niet-US | 44.428 | 2,1% | 3,2% | 4,4% | 5,9% | 7,4% | 8,9% |
| Eerder gekocht | 5.255 | 4,1% | 6,1% | 8,3% | 11,7% | 15,6% | 18,4% |

Viewed Product (onsite), nog geen order na 15 minuten (n = 40.130): 1,2% in 30 min, 1,9% in 1 uur, 2,8% in 4 uur, 3,9% in 24 uur, 6,3% in 7 dagen. Triple Pixel-variant (n = 27.184): 2,1 / 3,4 / 4,8 / 6,8 / 10,9%.

Belangrijk: dit is niet "zonder mail". De oude flows mailden de hele periode na 10 tot 30 minuten. Wat vóór de eerste mail gebeurt (eerste 10 minuten) is puur natuurlijk; daarna is het natuurlijk plus mail. Volledige tabel: `tabellen/q1_conditional.csv`.

### 1c. Het natuurlijke deel tussen 10 en 30 minuten, gemeten met de oude 10/30-minuten-split

De oude checkoutflows verdeelden instromers 50/50 over "mail 1 na 10 min" en "mail 1 na 30 min". Omdat de enige flowfilter "geen order sinds start" is, is het verschil in aantal ontvangers tussen de armen gelijk aan het aantal mensen dat in minuut 10 tot 30 zonder mail kocht. Received Email, 90 dagen, kopers binnen 7 dagen na de mail:

| Flow | Ontvangers 10 min | Kopers 7d | Ontvangers 30 min | Kopers 7d | Natuurlijke kopers 10-30 min (verschil) | Totaal arm 10 | Totaal arm 30 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Checkout Y2TmNB | 1.222 | 180 | 1.188 | 122 | 34 (2,8%) | 180 | 156 |
| Checkout Tsg2tV | 1.409 | 195 | 1.351 | 136 | 58 (4,1%) | 195 | 194 |
| Samen | 2.631 | 375 | 2.539 | 258 | 92 | 375 | 350 |

Lezing: 2,8 tot 4,1 procent koopt tussen minuut 10 en 30 zonder enige mail; dat klopt met de curve in 1b (2,9%). Met mail na 10 minuten komen er in totaal ongeveer 7 procent meer kopers uit dan met mail na 30 minuten (375 tegen 350), maar het verschil valt binnen de ruis (standaardfout ongeveer 25 kopers). De omzet-per-ontvanger in het Klaviyo-rapport ($5,62 tegen $4,28 en $4,86 tegen $3,78) overdrijft het voordeel, omdat de snelle mail natuurlijke kopers op zijn naam krijgt.
Voor cart en browse werkt deze rekenmethode niet (die flows filteren ook op "Checkout Started sinds start", dus het verschil in ontvangers bevat ook doorstromers naar checkout). Daar alleen de rapportcijfers: cart 15 min $2,90 tegen 30 min $2,27; browse 10 min $0,59 en $1,31 tegen 30 min $0,74 en $1,18 (gemengd).

---

## 2. Prestaties per stap in de huidige flows (vraag 2)

Bron: `baselines/flow-messages-90d.csv` (Klaviyo-rapport, 90 dagen) plus wachttijden uit de live flowdefinities. "tot 08:00" = Klaviyo-delay "x dagen, tot dit uur" in de tijdzone van het profiel.

### Checkout (Y2TmNB, trigger Shopify Checkout Started; Tsg2tV, trigger Triple Pixel)

| Stap | Moment | Mail | Delivered | Klik | Conv. | $/ontv. | Uitschr. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 10 min (arm A, 50%) | New AB Checkout 1 | 2.201 | 4,00% | 2,36% | **$7,86** | 1,04% |
| 1 | 10 min (25%) | Email #1 | 1.330 | 3,31% | 2,10% | $5,62 | 1,35% |
| 1 | 30 min (25%) | Copy of Email #1 | 1.273 | 3,61% | 2,20% | $4,28 | 1,49% |
| 2 | +1 dag tot 08:00/08:30 | Email #2 / AB 2 "Happy Chef Club" | 2.377 / 822 | 1,56% / 1,58% | 0,29% / 0,37% | $0,41 / $0,67 | 1,26% / 1,70% |
| 3 | +1 tot 2 dagen | #3 "Special Extra Bonus" / AB 3 | 2.307 / 1.432 | 2,73% / 2,44% | 0,52% / 0,91% | $1,34 / $2,39 | 0,82% / 1,26% |
| 4 | +1 tot 2 dagen | #4 "Can't Keep these Forever" / AB 4 | 2.292 / 1.053 | 1,66% / 1,33% | 0,31% / 0,19% | $0,68 / $0,44 | 0,61% / 0,86% |
| 5 | +1 dag (alleen arm A) | AB 5 | 1.307 | 1,68% | 0,76% | $1,26 | 0,92% |
| Tsg2tV 1 | 10 / 30 min | Email #1 / Copy | 1.519 / 1.480 | 4,74% / 5,27% | 2,04% / 1,69% | $4,86 / $3,78 | 0,53% / 1,15% |
| Tsg2tV 2-4 | dag 1, 3, 4 om 08:00 | #2, #3, #4 | 2.734 / 2.581 / 2.541 | 2,2-3,7% | 0,35-0,47% | $0,73 / $0,80 / $2,11 | 0,9-1,3% |

Lezing: mail 1 levert 70 tot 80 procent van de flowomzet. Mail 2 op dag 1 is in beide flows de zwakste (merkmail, $0,41 tot $0,73). Mail 3 en 4 met bonus of deadline doen het weer beter dan mail 2. De oude arm met vijf mails (AB) heeft dezelfde uitschrijving als de vier-mail-arm.

### Cart (SwkMyn)

| Stap | Moment | Mail | Delivered | Klik | Conv. | $/ontv. | Uitschr. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 15 min | Email #1 | 6.380 | 2,63% | 0,86% | $2,90 | 1,11% |
| 1 | 30 min | Copy of Email #1 | 5.983 | 2,86% | 0,84% | $2,27 | 1,50% |
| 2 | +2 dagen tot 08:00 | #2 "10% off" | 11.206 | 1,76% | 0,36% | $0,79 | 1,12% |
| 3 | +1 dag tot 08:00 | #3 "Last Call 10%" (2 varianten) | 2.968 / 3.000 | 1,7% | 0,30-0,54% | $1,09 / $0,97 | 0,8-0,9% |

### Browse (Wj6x6V onsite, TyEjuQ Triple Pixel): één mail

| Flow | 10 min | 30 min |
| --- | --- | --- |
| Wj6x6V | $0,59, klik 2,63%, uitschr. 1,65% | $0,74, klik 2,37%, uitschr. 1,78% |
| TyEjuQ | $1,31, klik 3,41%, uitschr. 1,26% | $1,18, klik 3,12%, uitschr. 1,03% |

Browse heeft de hoogste uitschrijving van alle verlatingsflows (1,42% gemiddeld).

### Welcome (SiaNLu, actieve tak "DG")

| Dag | Moment | Mail | Delivered | Klik | Conv. | $/ontv. | Uitschr. | Filter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 5 min | #1 Thanks For Joining | 48.136 | 2,38% | 0,71% | $1,78 | **2,75%** | geen |
| 1 | tot 10:00 | #2 A Note from Benjamin | 45.705 | 2,14% | 0,29% | $0,62 | 2,24% | geen |
| 2 | tot 10:00 | Additional 1 (smart sending aan) | geen verzendingen in rapport | | | | | |
| 3 | +1 dag | #3 Straight from the kitchen | 19.767 | 1,90% | 0,23% | $0,59 | 2,35% | opende >0, geen order |
| 5 | +2 dagen tot 10:00 | #4 Cook with the Best | 17.119 | 1,34% | 0,13% | $0,31 | 1,78% | opende >=2, geen order |
| 7 | +2 dagen tot 10:00 | #5 Ultimate showdown | 17.137 | 1,03% | 0,09% | $0,23 | 1,45% | idem |
| 9 | +2 dagen tot 10:00 | Additional 2 Top Rated | 31.997 | 0,85% | 0,06% | $0,13 | 0,85% | geen |
| 10 | +1 dag | Additional 3 Last Call 10% | 31.265 | 0,95% | 0,14% | $0,26 | 0,65% | geen |

Gemeten met Received Email: 10,7% van de ontvangers van #2 en 13,3% van de ontvangers van "Last Call for an Extra 10% Off" had na de inschrijving al gekocht. Mail #1, #2 en Additional 2 en 3 hebben geen "geen order"-filter. Van de ontvangers van #1 koopt 3,9% binnen 24 uur na de mail, van #2 0,52%, van #3 0,32%, van Additional 3 0,14%.

### Failure to launch (T2SmtR): 30 dagen wachten, daarna 10 mails in 12 dagen

343.932 delivered in 90 dagen, $0,013 tot $0,093 per ontvanger, klik 0,23-0,50%. Dit is 37% van alle flowmails voor 3,9% van de flowomzet.

### Post-purchase (RL3TU6)

| Moment (eerste koper) | Mail | Delivered | Klik | $/ontv. | Uitschr. | Waar klikken ze |
| --- | --- | --- | --- | --- | --- | --- |
| 2 min | We've Got Your Order | 10.430 + 1.929 | 7,1-8,2% | $0,58-0,82 | 0,32-0,36% | 72-78% care-use-pagina |
| +1 dag 08:30 | Founder's Note | 12.239 | 7,4% | $0,12 | **1,36%** | 96% tracking (!) |
| +1 dag 08:30 | 100 Days to Try | 12.114 | 2,9% | $0,13 | 0,91% | 83% garantiepagina |
| +1 dag 08:30 (dag 3) | It's On Its Way | 12.047 | **29,8%** | $0,33 | 0,24% | 96% tracking |
| +3 dagen 08:30, als fulfilled (dag 6) | Get Ready to Cook | 7.561 | 6,8% | $0,09 | 0,71% | 94% care-use |

### Winback (UEfh4h): trigger Placed Order, 60 dagen wachten

R1 "New Must-Haves" $0,235 (16.000 delivered), R2 na 1 of 2 dagen $0,25 / $0,07, R3 "Expires Tonight" $0,20. Klik 0,45-0,79%.

---

## 3. Tijd van de dag en dag van de week (vraag 3)

### 3a. Wanneer kopen mensen (alle orders, lokale tijd, 12 mnd, n = 76.683, waarvan US 39.046)

| Uur lokaal | 00-06 | 06-08 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| % orders | 5,0 | 6,2 | 6,2 | 7,1 | 7,4 | 6,9 | 6,4 | 6,0 | 5,8 | 5,5 | 5,3 | 5,2 | 5,0 | 4,8 | 5,0 | 4,9 | 4,2 | 3,0 |

Piek 09:00 tot 12:00, daarna vlak tot 22:00. 19,0% van de orders valt tussen 19:00 en 23:00. US, AU en UK hebben hetzelfde patroon in lokale tijd (AU iets hoger 15-17 uur).
Weekdag (ma t/m zo): 14,2 / 13,1 / 12,9 / 12,6 / 14,0 / **16,1 / 17,0**%. Weekend is het sterkst.

### 3b. Klikratio en order binnen 24 uur per lokaal verzenduur (Received Email, 90 dagen)

Alleen mail 1 van checkout, cart en browse (realtime verzonden, dus het uur volgt de trigger; n = 84.483):

| Lokaal verzenduur | 00-06 | 06-08 | 08-10 | 10-12 | 12-14 | 14-17 | 17-19 | 19-21 | 21-22 | 22-24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n | 6.371 | 4.282 | 10.683 | 11.598 | 10.329 | 13.722 | 8.386 | 8.018 | 4.102 | 6.957 |
| Klik | 2,64% | 2,87% | 3,29% | 3,23% | 3,30% | 3,18% | 3,18% | 2,93% | 2,56% | 2,66% |
| Order binnen 24u | 1,84% | 2,10% | 2,26% | 2,61% | 2,56% | 2,43% | 2,35% | 2,27% | 2,66% | 1,70% |

Vervolgmails (checkout en cart mail 2+, "tot 08:00"): 91% gaat tussen 08:00 en 10:00, klik 1,91%, order 24u 0,79%. Andere uren hebben te weinig volume voor een vergelijking.
Campagnes (3,05 mln verzendingen; verzonden in lokale tijd, 48% tussen 08:00 en 10:00): klik 08-10 0,54%, 10-12 0,50%, 12-17 0,66-0,67%, **17-19 0,89%**, 19-21 0,73%. Let op: avondcampagnes waren vaak kleinere, actievere segmenten; dit is geen schone test.
Campagne-klik per weekdag (ma t/m zo): 0,59 / 0,50 / 0,54 / 0,68 / 0,71 / 0,63 / 0,50%.

### 3c. Opens en klikken in lokale tijd

Echte opens (machine_open = false, 7 dagen, n = 70.844) en klikken (12 mnd, n = 177.188 zonder botklikken) pieken om 08:00 lokaal, omdat campagnes en vervolgmails om 08:00 tot 08:30 vertrekken. Dat zegt iets over de verzendtijd, niet over de voorkeur van de lezer. Apple Mail Privacy-opens zijn uitgesloten; ze zijn er ongeveer de helft van alle opens.

Smart Send Time: niet gebruikt in dit account; de data hierboven laat geen sterk uur zien voor realtime mails tussen 08:00 en 21:00. Voor campagnes is een test 08:00 tegen 17:30 lokaal zinvol (zie 02-advies).

---

## 4. Latentie: verzending, open, klik, order (vraag 4)

| Stap | Flow | Campagne |
| --- | --- | --- |
| Verzending tot eerste klik, mediaan | 4,5 uur | 3,6 uur |
| % klikken binnen 1 / 4 / 24 / 48 uur | 28,5 / 48,1 / 73,8 / 81,7% | 24,8 / 52,1 / 82,4 / 89,9% |
| Verzending tot echte open, mediaan (7d steekproef) | 2,1 uur | 63 min |
| Open tot klik, mediaan (n = 3.311) | 24 seconden; 90% binnen 3,5 uur | |
| Klik tot order (orders met klik in 7d ervoor, n = 8.516) | mediaan 12 min; 46% binnen 10 min, 70% binnen 1 uur, 85% binnen 24 uur | mediaan 11 min; 74% binnen 1 uur, 87% binnen 24 uur |

Verzending tot order (orders na een klik), per flowtype:

| Flow | n | Mediaan | Binnen 1u | 4u | 24u | 48u | 72u |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Checkout | 617 | 3,9 u | 28,7% | 50,2% | 77,0% | 86,1% | 90,4% |
| Cart | 508 | 9,5 u | 15,4% | 34,4% | 68,3% | 81,7% | 87,2% |
| Browse | 655 | 9,9 u | 23,1% | 38,0% | 66,4% | 77,7% | 85,5% |
| Welcome | 1.687 | 3,5 u | 35,3% | 52,2% | 75,6% | 84,9% | 88,7% |
| Winback | 87 | 4,9 u | 25,3% | 46,0% | 82,8% | 90,8% | 92,0% |
| Post-purchase | 273 | 57,7 u | 11,4% | 22,7% | 34,8% | 44,7% | 52,4% |
| Campagnes | 3.804 | 7,0 u | 13,5% | 39,2% | 69,6% | 81,0% | 86,3% |

Lezing: na een verlatingsmail is 77 tot 86 procent van het effect binnen 48 uur binnen. Een volgende mail eerder dan 20 tot 24 uur na de vorige valt in de staart van de vorige. Attributievenster: 5 dagen klik dekt 88 tot 98 procent; het accountvenster hoeft niet langer.

---

## 5. Leesdiepte via geklikte URL's (vraag 5)

Klaviyo bewaart in Clicked Email de URL zonder UTM; 0,0% van de geklikte URL's bevat `utm_`. Positie in de mail is daarom alleen af te leiden uit welke bestemming bij welk blok hoort. Unieke klikken per profiel en bestemming, flows, 90 dagen (`tabellen/q5_urls.csv`):

| Mail | Unieke klikken | Waar naartoe |
| --- | --- | --- |
| Checkout New AB 1 | 92 | 96% checkout-herstel (hoofdknop) |
| Checkout Y2TmNB #1 | 51 | 53% checkout-herstel, 27% /cart, 16% homepage (logo) |
| Checkout Tsg2tV #1 | 79 | 82% /cart, 6% homepage, 5% about-us |
| Checkout Tsg2tV #4 | 78 | 51% /cart, 32% collectie all (onderste blokken) |
| Cart #1 | 197 | 33% pan-productpagina, 14% Pan Pro Large, 14% homepage, 8% deksel |
| Cart #3 | 54 | 24% homepage, 11% collectie, 7% pan |
| Browse TyEjuQ #1 | 809 | 36% collectie all, 14% pan, 13% homepage, 8% Large |
| Welcome #1 | 1.230 | 77% collectie all (hoofdknop), 12% homepage, 4% about-us |
| Welcome #4 | 271 | 32% pan, 28% snijplank, 13% bestek (productblokken) |
| Welcome Additional 3 | 436 | 43% bundles, 13-13% twee sets |
| Post-purchase Order | 831 | 78% care-use, 12% homepage, 5% bundles |
| Founder's Note | 949 | 96% tracking |
| It's On Its Way | 3.937 | 96% tracking |
| Review (Vixr6X) | 382 | 90% reviews |

Wat we wel zien: (1) de hoofdknop trekt 75 tot 96 procent van de klikken als er één duidelijke knop is; (2) de logo-link (homepage) pakt 12 tot 24 procent in verlatingsmails, dat zijn klikken die niet naar de cart gaan; (3) footerklikken (social, policies, about) zijn 1 tot 5 procent; (4) in de Founder's Note klikt 96% op tracking, dus lezers zoeken de pakketinformatie, niet het verhaal.
Wat we niet kunnen meten: scrolldiepte, welke van twee knoppen met dezelfde URL is geklikt, en of een productblok bovenaan of onderaan geklikt werd als dezelfde productpagina twee keer voorkomt. Oplossing in 03-meten.md (eigen parameter per blok in de link zelf).

---

## 6. Welcome: van inschrijving tot eerste aankoop (vraag 6)

230.510 unieke inschrijvers op Email List Uw8eZG in 12 maanden; 1,3% was al koper. Prospects (geen eerdere order):

| Venster na inschrijving | Cohort | % eerste order (cumulatief) |
| --- | --- | --- |
| 1 uur | 226.357 | 22,5% |
| 24 uur (dag 0) | 226.357 | 23,5% |
| 48 uur (dag 1) | 225.635 | 23,9% |
| dag 3 | 224.021 | 24,3% |
| dag 7 | 221.695 | 24,8% |
| dag 10 | 219.671 | 25,1% |
| dag 14 | 217.470 | 25,4% |
| dag 30 | 208.519 | 26,3% |
| dag 60 | 185.980 | 27,5% |
| dag 90 | 170.465 | 28,1% |

Binnen het eerste uur: 32.490 kopers binnen 2 minuten, 8.319 in minuut 2-5, 5.415 in 5-10, 1.978 in 10-15, 1.861 in 15-30, 983 in 30-60. **20,3% van alle inschrijvers koopt binnen 10 minuten**: de inschrijving gebeurt in dezelfde sessie als de aankoop (pop-up of marketingvinkje in de checkout).

Dagelijkse kans op een eerste order voor wie nog niet kocht (cohort met 60 dagen opvolging, n = 186.676):

| Dag | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 14 | 21 | 31 | 41 | 51 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kans per dag | 0,50% | 0,29% | 0,24% | 0,18% | 0,17% | 0,13% | 0,12% | 0,10% | 0,09% | 0,09% | 0,07% | 0,06% | 0,04% | 0,03% | 0,02% |

Wie na het eerste uur nog niet kocht: 1,3% koopt nog op dag 0, ongeveer 1,9% in dag 1 tot 10, 1,2% in dag 10 tot 30, 1,0% in dag 30 tot 60. De kans per dag halveert ruwweg elke 4 tot 5 dagen tot dag 10 en zakt daarna langzaam.
Per land, % eerste order binnen dag 0 / dag 10 / dag 30: US 27,1 / 28,6 / 29,5; AU 28,3 / 29,6 / 30,6; UK 27,6 / 29,3 / 30,3; CA 22,6 / 24,2 / 25,1; overig 25,1 / 26,7 / 27,6.

Uitschrijving na inschrijving (cumulatief, % van inschrijvers): dag 1 4,6%, dag 3 7,5%, dag 7 9,8%, dag 10 10,9%, dag 14 12,2%, dag 30 16,3%, dag 60 22,2%, dag 90 25,5%.

---

## 7. Herhaalaankoop, levertijd, vaatwasstrips (vraag 7)

98.538 kopers sinds oktober 2024; 8.541 met een tweede order (16% daarvan binnen 1 dag, dat zijn vooral split- of aanvullende orders).
Dagen tussen 1e en 2e order (2e order minstens 1 dag later, n = 7.174): **mediaan 35 dagen**; p10 8, p25 14, p75 82, p90 175.

| Gap | 1-7 d | 7-14 | 14-21 | 21-30 | 30-45 | 45-60 | 60-90 | 90-120 | 120-180 | 180-270 | 270+ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| % van herhalers | 9,0 | 15,0 | 12,4 | 9,4 | 11,3 | 8,8 | 11,1 | 6,3 | 7,1 | 6,0 | 2,7 |

Cumulatief % kopers met een 2e order: 14 dagen 1,8%, 30 dagen 3,4%, 60 dagen 5,0%, 90 dagen 5,9%, 180 dagen 7,0%, 365 dagen 8,0%.
Kans per periode (cohort met 6+ maanden opvolging, n = 63.070): dag 0-30 3,3%, 30-60 1,65%, 60-90 0,97%, 90-120 0,61%, 120-180 0,75%.
Per eerste aankoop: pan (n = 87.243) 6,1% binnen 90 dagen, mediaan 34,5 dagen; accessoire (n = 10.140) 4,2%, mediaan 42 dagen; set (n = 1.130, vooral recent) te weinig opvolging. Orders >= $300 herhalen iets vaker (7,1% tegen 5,5-5,9%) en sneller (mediaan 30 dagen). 2e naar 3e order: mediaan 33 dagen (n = 1.179).
Wat de 2e order is: deksel (1.610), Pan Pro Mini (1.242), Standard (1.231), Deep (1.137), Wok (1.067), Small (1.038), snijplank (998), bestek (907). Dus vooral een tweede pan plus deksel.

Vaatwasstrips: 160 orders in 2 jaar met de strips als betaald product, Recharge "Subscription started" 24 keer (aug-sep 2026). De strips zitten vooral als Mystery Gift in de doos en zijn niet als product in de orderregels te zien. Er is geen data om een refill-interval op te baseren.

Levertijd (Delivered Shipment, `Delivery Hours` = order tot levering, gecontroleerd tegen order-tijdstempels, correlatie 0,96):

| Regio | n | p25 | Mediaan | p75 | p90 |
| --- | --- | --- | --- | --- | --- |
| Alle | 16.043 | 9,3 d | **11,7 d** | 14,7 d | 19,2 d |
| US | 12.954 | 9,7 | 12,0 | 15,0 | 20,0 |
| AU | 1.758 | 7,9 | 9,9 | 12,1 | 15,2 |
| UK | 800 | 9,2 | 10,7 | 12,1 | 15,0 |
| CA | 277 | 10,4 | 13,2 | 17,0 | 21,3 |

Order tot fulfilment: mediaan 2,8 dagen (p90 10). Transit: mediaan 3,1 dagen.
Dekking: maar 35,9% van de orders (9 jul-20 sep) heeft een Delivered Shipment-event: UK 91%, AU 86%, US 37%, CA 9%, overige landen 1%. Een flowtak die wacht op Delivered Shipment heeft dus een vangnet op tijd nodig.

---

## 8. Splits: groottes en verschil in gedrag (vraag 8)

| Split | Grootte (checkout-verlaters na 15 min, n = 29.673) | Verschil in herstel 7d | Waard? |
| --- | --- | --- | --- |
| Cartwaarde >= $300 | 27,9% (mediaan cart $189, p75 $338) | 15,5% tegen 11,1% (24u: 11,2 tegen 7,8) | Ja, voor inhoud en aanbodtrede |
| Land US / niet-US | US 34%, niet-US bekend 50%, onbekend 16% | 13,6% tegen 15,2% | Alleen voor productinhoud (12-pcs), niet voor timing |
| Eerdere koper | 4,8% | 26,9% tegen 11,6% | Ja: korte versie, geen korting nodig |
| Ooit HI10 gebruikt | 1,1% | te klein | Nee |
| Geklikt / niet geklikt | zie 4: 70% van de orders na een klik valt binnen 1 uur | | Ja als exit (geklikt en niet gekocht na 24u = sterkste signaal) |

Cart-verlaters (n = 81.974): 18,1% >= $300, herstel 7d 8,9-9,3% voor >= $300 tegen 7,7-12,8% eronder (geen verschil). Eerdere kopers 18,4% tegen 7,8%.
Kortingscodes: 50,9% van de orders gebruikt een code; top BFEXTRA10 7.706, MOTHER10 4.018, NYEXTRA10 3.384; HI10 1.611 (1,8% van de orders).
Locatie "onbekend" (16% van de checkout-verlaters) betekent: het profiel heeft nog geen adres. De landsplit moet daarom een terugval hebben (Customer Locale op het event, of "onbekend = INT-versie zonder prijzen").

---

## 9. Overlap tussen flows (vraag 9)

Received Email, 12 weken, per profiel per week (95.320 profielweken met een welcome-mail):

| Welcome-week met ook | Aandeel | Uitschrijf in die week | Zonder | Mails die week |
| --- | --- | --- | --- | --- |
| Browse | 30,2% | 7,24% | 5,14% | 4,6 tegen 4,1 |
| Cart | 10,5% | 7,13% | 5,62% | 5,8 tegen 4,1 |
| Checkout | 5,2% | 6,86% | 5,72% | 6,9 tegen 4,1 |
| Post-purchase | 8,1% | 3,17% | 6,01% | 6,5 tegen 4,0 |
| Campagne | 55,8% | 2,79% | 9,53% | 4,7 tegen 3,7 |

Weken met twee of meer verlatingsflows tegelijk: 7.558 van 69.357 (10,9%). Uitschrijving 4,99% tegen 5,22% bij één flow (geen verschil).
Triggers bij nieuwe prospects (12 mnd, n = 169.368): binnen 10 dagen na inschrijving 1,1% checkout verlaten, 2,8% cart verlaten; product bekeken (onsite) 4,6%.
Lezing: overlap welcome met verlatingsflows gaat samen met 1,1 tot 2,1 procentpunt meer uitschrijving in die week. Het causale deel is niet te scheiden van "deze mensen zijn actiever en krijgen meer mail". Welcome plus campagne heeft juist lagere uitschrijving, omdat de nieuwste inschrijvers (hoogste uitschrijfkans) nog geen campagne kregen.

---

## 10. Frequentie en moeheid (vraag 10)

Uitschrijvingen 12 mnd: 91.832 (EMAIL_LINK 48.050, ONE_CLICK 40.328, SPAM_REPORT 3.283). Spamklachten 6.572. In 90 dagen komt 52% van de uitschrijvingen uit campagnes, 28% uit flows, 20% zonder bericht-ID.
Uitschrijving per mail per flowgroep (90 dagen): welcome 1,82%, browse 1,42%, cart 1,10%, checkout 1,04%, winback 0,80%, post-purchase 0,69%, overige 0,49%, campagnes 0,44%.
Per profielweek (12 weken, 1,33 mln profielweken): mails per week mediaan 3, p90 5, p99 8.

| Mails die week | Profielweken | Uitschrijf per profielweek | Uitschrijf per 1.000 mails | Spam per profielweek |
| --- | --- | --- | --- | --- |
| 1 | 291.754 | 2,46% | 24,6 | 0,10% |
| 2 | 335.475 | 1,68% | 8,4 | 0,06% |
| 3 | 391.764 | 0,98% | 3,3 | 0,04% |
| 4 | 121.826 | 1,60% | 4,0 | 0,07% |
| 5 | 74.428 | 1,41% | 2,8 | 0,06% |
| 6-7 | 98.670 | 0,93% | 1,4 | 0,05% |
| 8-10 | 16.167 | 1,27% | 1,5 | 0,06% |

Lezing: deze tabel laat geen "meer mail = meer uitschrijving" zien, maar dat komt door omgekeerde oorzaak: wie zich uitschrijft krijgt die week geen mails meer, en nieuwe inschrijvers (hoogste uitschrijfkans) zitten in de lage aantallen. Wel zichtbaar: de sprong van 3 naar 4 mails per week (0,98% naar 1,60%), en bij alleen-campagne-ontvangers van 3 naar 4-5 (0,51% naar 0,70-0,76%). Account-week: de week van 28 sep met 9 campagnes op 6 dagen (675.545 delivered) gaf 3.408 uitschrijvingen en 187 spamklachten, het dubbele van een normale week.

---

## Datakwaliteit en wat ontbrak

- Shopify en Triple Whale niet nodig gehad: alle order-, fulfilment- en leverdata komen via de Shopify-integratie in Klaviyo. Shopify-orders met bron "tiktok" en "Shop" zitten erin (geen e-mailkanaal); niet uitgesloten, effect op de timingcurves klein.
- Herstel = elke order van het profiel, niet alleen voor het verlaten product. Iemand die iets anders koopt telt als herstel.
- Profiellocatie ontbreekt vaker bij niet-kopers (checkout "onbekend" koopt 8%), dus landvergelijkingen gaan over profielen met bekend land.
- Received Email alleen 90 dagen, Opened Email alleen 7 dagen (volume). Opens zijn voor 50%+ machine-opens; alleen klikken en orders gebruikt als hoofdmaat.
- Clicked Email bevat geen UTM en geen bloknaam; positie is niet meetbaar.
- Viewed Product: twee bronnen (Klaviyo onsite en Triple Pixel) met verschillend publiek; 60 dagen.
- Delivered Shipment dekt maar 36% van de orders (US 37%, landen buiten US/UK/AU bijna 0).
- De 10/30-minuten-vergelijking is alleen voor checkout zuiver; voor cart en browse filtert de flow ook op doorstroom naar checkout.
- Welcome "Additional 1" staat live maar heeft geen verzendingen in het 90-dagenrapport (smart sending aan); niet verder onderzocht.
- Opvallend en niet verklaard: 20% van de inschrijvers koopt binnen 10 minuten, maar maar 6,8% van de ontvangers van welcome-mail 1 had al gekocht. Mogelijk komen checkout-inschrijvers via een andere route op de lijst of staat de Placed Order later in Klaviyo. Nakijken voor de W0-split.
