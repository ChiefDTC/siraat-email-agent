# 03 · Meten: UTM-schema per blok en het meetplan na livegang

Datum: 7 oktober 2026. Hoort bij `01-data.md` en `02-advies.md`.

## 1. Waarom een eigen parameter per blok nodig is

- Klaviyo voegt bij verzending UTM's toe (`add_tracking_params: true`), maar het event Clicked Email bewaart de **oorspronkelijke** link. In 274.714 klikken in 12 maanden bevat 0,0% een `utm_`-parameter (01-data, 5).
- Daardoor zien we in Klaviyo alleen de bestemming, niet welk blok geklikt is. Twee knoppen naar dezelfde cart-link zijn niet te onderscheiden.
- Oplossing: zet de blokcode **in de link zelf** in de template. Dan staat hij in Clicked Email (`URL`), in Shopify/GA4 (landing_site) en in Triple Whale.

## 2. Schema

Klaviyo's automatische parameters blijven aan (utm_source=klaviyo, utm_medium=email, utm_campaign = flow- of campagnenaam). Wij voegen per link toe:

```
utm_content={mail}-{blok}-{positie}
```

| Deel | Waarden | Voorbeeld |
| --- | --- | --- |
| mail | code uit v3: c1..c4, k1..k3, b1, b2, w0..w5, p1..p4, r1, r2; campagnes: cmp-JJMMDD | c1 |
| blok | hdr (logo/navigatie), hero, cart (productregels), cta1, gifts, proof (reviews), faq, xsell (productblok), cta2, cta3, ps (tekstlink in P.S.), ftr (footer) | hero |
| positie | 1 = boven de vouw (eerste 600 px), 2 = midden, 3 = onder | 1 |

Voorbeelden:
- `{{ event.extra.responsive_checkout_url }}&utm_content=c1-hero-1`
- `https://siraatskitchen.com/products/titanium-hammered-pan-pro-standard?utm_content=w4-xsell-2`
- logo in de header: `https://siraatskitchen.com/?utm_content=c1-hdr-1`

Regels:
- Elke link in een mail krijgt een eigen `utm_content`, ook als de bestemming gelijk is.
- Gebruik `&` als de link al een `?` heeft (checkout-URL's hebben `?key=`). Test elke template met een previewklik.
- Geen persoonsgegevens in de parameter.
- De partials header en footer krijgen een variabele voor de mailcode, zodat `hdr` en `ftr` per mail te zien zijn.
- Vul hetzelfde schema in Figma bij elke knop in, zodat bouw en meting dezelfde namen gebruiken.

Uitlezen (zo te herhalen):
```
GET /api/events?filter=and(equals(metric_id,"W247h8"),greater-or-equal(datetime,...))
    &fields[event]=datetime,event_properties.URL,event_properties.$message,event_properties.Bot Click
```
Daarna `utm_content` uit `URL` halen, botklikken eruit, uniek per profiel per mail per blok tellen (`scripts/q5.py` is de basis).

## 3. Wat we niet kunnen meten (en hoe we het benaderen)

| Vraag | Meetbaar? | Benadering |
| --- | --- | --- |
| Scrolldiepte | Nee | Aandeel klikken op positie 3 (onder) tegen 1 (boven) per mail. Als positie 3 onder de 5% van de klikken blijft, is onderin lezen zeldzaam. |
| Leestijd | Nee | Geen. Opens zijn voor meer dan de helft machine-opens. |
| Welke van twee knoppen bij oude mails | Nee | Alleen voor nieuwe templates met dit schema. |
| Of een mail een order veroorzaakt | Deels | Holdout of A/B op instapniveau, orders binnen 7 dagen per arm (zie 4). |

## 4. Meetplan, 2 tot 4 weken na livegang

Vergelijk met `baselines/` (90 dagen tot 6 okt) en met `01-data.md`. Lees per week uit, beslis na 4 weken.

### 4a. Per flow, wekelijks

| Maat | Bron | Basislijn | Doel / alarm |
| --- | --- | --- | --- |
| Herstel 7 dagen van verlaters (orders, niet attributie) | events Checkout Started / Added to Cart + Placed Order, `scripts/q1b.py` | checkout 12,3% (na 15 min), cart 8,5%, browse 6,3% | Niet lager dan basis; doel +1 pp checkout |
| Omzet per ontvanger per mail | flow report, RSNxYV | C1-oud $4,28-7,86; K1-oud $2,27-2,90; B1-oud $0,59-1,31 | Per stap, in de volgorde van de flow |
| Klik per mail | flow report | zie 01-data, 2 | Mail 2+ niet onder 1,5% |
| Uitschrijving per mail | flow report | welcome 1,82%, browse 1,42%, checkout 1,04% | Alarm boven 1,5% (PLAYBOOK: boven 1% is probleem) |
| Spam per mail | flow report | flows 0,076% | Alarm boven 0,1% |
| Welcome: % eerste order dag 0-10 en dag 10-30 per inschrijfcohort | Subscribed to List + Placed Order, `scripts/q6.py` | dag 1-10: ongeveer 1,9% van wie na 1 uur nog niet kocht | Hoger |
| Welcome: aandeel mails aan mensen die al kochten | Received Email + Placed Order | 10,7% (mail 2), 13,3% (last call) | Onder 1% |
| Welcome: uitschrijving tot dag 7 en dag 14 per cohort | Unsubscribed + Subscribed | 9,8% en 12,2% | Lager |
| Post-purchase: P2-tak "geleverd" tegen "vangnet" | flow report per tak | 36% heeft Delivered Shipment | Vangnettak mag niet slechter scoren dan de geleverd-tak |
| Post-purchase: herhaalkoop 30 dagen per cohort | Placed Order | 3,4% | Hoger |

### 4b. Timing-specifiek

| Vraag | Hoe | Basislijn |
| --- | --- | --- |
| Komen orders na C1 nu sneller? | verzending tot order, mediaan per mail | checkout 3,9 uur, cart 9,5 uur, browse 9,9 uur |
| Valt mail 2 in de staart van mail 1? | % orders van de instromers dat tussen mail 1 en mail 2 valt | 77% binnen 24 uur na mail 1 |
| Werkt het nieuwe venster? | klik en order 24u per lokaal verzenduur | realtime 3,2% klik 08-21 uur, 2,6% 22-06 uur |
| Overlap | % welcome-weken met browse-mail en uitschrijving in die week | 30,2% en 7,24% |
| Frequentie | uitschrijving per profielweek bij 4+ mails | 1,60% |

### 4c. Per blok (nieuw, na het UTM-schema)

- Aandeel klikken per blok per mail: hero, cart, cta2, cta3, gifts, proof, hdr, ftr.
- Klik tot order per blok (welk blok levert kopers, niet alleen klikken).
- Beslisregel: een blok met minder dan 3% van de klikken en geen orders na 4 weken is kandidaat om te schrappen of naar boven te halen. Een header-logo met meer dan 15% van de klikken in een verlatingsmail (nu 12 tot 24%) is een lek: logo-link dan naar de cart laten wijzen.

### 4d. A/B-tests (uit 02-advies, 10)

- Uitlezen op orders binnen 7 dagen per arm (instapniveau), niet op Klaviyo-winnaar. Klaviyo's automatische winnaar uit.
- Per test noteren in LOG.md: start, armen, n per arm, herstel per arm, verschil met 95%-interval, besluit.
- Minimale duur 4 weken, ook als het verschil eerder groot lijkt (weekendeffect: zaterdag en zondag hebben 16-17% van de orders).

## 5. Rapport-query's (herhalen)

- Flow report per mail: `POST /api/flow-values-reports` met `timeframe {key: last_30_days}`, `conversion_metric_id: RSNxYV`, statistieken recipients, delivered, click_rate, conversion_rate, revenue_per_recipient, unsubscribe_rate, spam_complaint_rate; groeperen op flow_message_id.
- Volumes per dag of uur: `POST /api/metric-aggregates` met `interval hour` of `day`, `timezone US/Eastern`, `measurements [count, unique]`.
- Eventniveau: `scripts/fetch_events.py` (zie 01-data, 0), daarna de analysescripts in `research/timing/scripts/` (paden in de scripts verwijzen naar een tijdelijke map en moeten bij hergebruik aangepast worden).
