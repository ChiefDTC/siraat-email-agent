# 03 · Rapportage, beslisregels en testlog

Datum: 7 oktober 2026. Hoort bij `01-meetkader.md` (definities) en `02-testroadmap.md` (tests). Alles hieronder is alleen lezen in Klaviyo en Shopify.

## 1. Wekelijks dashboard

Ritme: elke maandag, over de afgelopen kalenderweek maandag 00:00 tot maandag 00:00 **US/Eastern** (zelfde weekdefinitie als `baselines/account-weekly.csv`). Uitkomst: één regel per test in `results.csv` bijwerken, een kort blok in de dagelijkse Slack-update van maandag (#claude-mail, zie ROUTINES.md; die prompt kan later een blok "Tests" krijgen) en een logregel in LOG.md.

### 1.1 Welke cijfers

**Blok A · Gezondheid (per flow, v3 en oud pad apart):**

| Cijfer | Bron | Vergelijk met |
| --- | --- | --- |
| Delivered, instromers (delivered eerste mail van het pad) | flow report | baselines: instromers/wk (01 §1.1) |
| Omzet, RPR per delivered, omzet per instromer | flow report | baseline #2 t/m #7 |
| Conversie (uniek) per instromer, AOV | flow report | 01 §1.1 |
| Unieke klikratio | flow report | flows-90d.csv |
| Uitschrijf-, spam-, bounceratio per mail | flow report | guardrails 01 §1.3 |
| Flow-omzetaandeel van totale omzet | metric aggregates | baseline #1 (10,8%) |
| Checkout-herstelratio | metric aggregates | baseline #9 (0,97%) |
| Welcome-omzet per nieuwe abonnee | flow report + metric aggregates | baseline #8 ($2.53) |

**Blok B · Tests (per test-ID, per arm):** delivered, klikken, conversies, omzet, RPR, kortingskosten (codetests), uitschrijvingen, spam, cumulatief sinds start, plus voortgang naar de geplande n (procent) en de beslisstatistiek uit §2.

**Blok C · Codes:** aantal orders en kortingsbedrag per codeprefix (CO-, CART-, VIEW-, BACK-, VIP-, THX-, HI10, publieke lekcodes), Shopify.

**Blok D · Signalen:** SRM-check per test, guardrail-overschrijdingen, mails met 0 verzendingen (kapotte split of filter).

### 1.2 Hoe ophalen

Model-parameter in elke MCP-call: `claude-opus-5-5` (of het model dat de call doet). Flowrapporten zijn groot: opslaan in de scratchpad en met python samenvatten (PLAYBOOK §4).

**Weekgrenzen in UTC** (Klaviyo-reporttimeframe in ISO):

| Week (ET) | start | end |
| --- | --- | --- |
| t/m 26 okt 2026 (EDT) | `YYYY-MM-DDT04:00:00+00:00` | idem |
| week 26 okt tot 2 nov (overgang) | `2026-10-26T04:00:00+00:00` | `2026-11-02T05:00:00+00:00` |
| vanaf 2 nov 2026 (EST) | `YYYY-MM-DDT05:00:00+00:00` | idem |

**1 · Flowrapport per mail en per variant** (`mcp__Klaviyo__get_flow_report`)

```json
{
  "conversion_metric_id": "RSNxYV",
  "statistics": ["recipients","delivered","clicks_unique","click_rate","conversion_uniques","conversions",
                 "conversion_rate","unsubscribe_uniques","unsubscribe_rate","spam_complaints",
                 "spam_complaint_rate","bounced","bounce_rate"],
  "value_statistics": ["conversion_value","revenue_per_recipient","average_order_value"],
  "timeframe": {"start": "2026-10-12T04:00:00+00:00", "end": "2026-10-19T04:00:00+00:00"},
  "group_by": ["flow_id","flow_name","flow_message_id","flow_message_name","variation","variation_name"],
  "filters": "and(equals(send_channel,\"email\"),contains-any(flow_id,[\"<v3-checkout>\",\"<v3-cart>\",\"<v3-browse>\",\"<v3-welcome>\",\"<v3-postpurchase>\",\"<v3-winback>\",\"XzHrez\"]))"
}
```

- Getest op 7 oktober met Y2TmNB en Tsg2tV (laatste 7 dagen): werkt, mails zonder A/B geven `variation: ""`. Resultaat bevat per regel `statistics` en per flow een `flow_aggregation`.
- Tijdens T01 ook de oude flow-ID's opnemen zolang die nog versturen (Y2TmNB, Tsg2tV, SwkMyn, TBWngE, Wj6x6V, TyEjuQ, SiaNLu, T2SmtR).
- Padniveau: de `flow_message_id`'s per pad vastleggen in een mapping (`research/testing/message-map.csv`, aan te maken bij livegang: flow_message_id, mail-ID uit 04, pad, test-ID, variant). Omzet per pad = som over de berichten van dat pad.
- Let op: het flowrapport dateert op **verzenddatum**. Een order op maandag na een mail van zondag valt in de week van de mail.
- Lopend 4-wekenbeeld: dezelfde call met `"timeframe": {"key": "last_30_days"}`, direct vergelijkbaar met `baselines/flows-30d.csv`.

**2 · Totale omzet en flow-omzet op orderdatum** (`mcp__Klaviyo__query_metric_aggregates`)

```json
{"body": {"data": {"type": "metric-aggregate", "attributes": {
  "metric_id": "RSNxYV",
  "measurements": ["sum_value","count","unique"],
  "interval": "week",
  "timezone": "America/New_York",
  "filter": ["greater-or-equal(datetime,2026-10-12T00:00:00)","less-than(datetime,2026-10-19T00:00:00)"]
}}}}
```

Dezelfde call drie keer met een `by`:
- `"by": ["$attributed_flow"]` → omzet per flow op orderdatum (flow-omzetaandeel = som v3-flows / totaal zonder `by`).
- `"by": ["$attributed_channel"]` → e-mailaandeel (context baseline: 18,7%).
- `"by": ["$attributed_variation"]` → omzet per A/B-variant (T02, T04, T05, T07, T08). Variatie-ID's koppelen via de message-map.

Metric aggregates en flowrapport verschillen licht door datering (baselines/README: 90d $416,090 tegen $418,569). In het dashboard altijd zeggen welke bron een getal heeft.

**3 · Noemers en guardrails** (zelfde body, andere metric):

| Metric | metric_id | measurements | interval | Gebruik |
| --- | --- | --- | --- | --- |
| Checkout Started | `RfMvni` | `["unique"]` | `day` (dan optellen, zoals baseline #9) | Herstelratio |
| Added to Cart | `QXcV8K` | `["unique"]` | `day` | Volumecheck cart |
| Refunded Order | `Xg6cwn` | `["count","sum_value"]` | `week`, `by: ["$attributed_flow"]` | Refund-guardrail |
| Unsubscribed from Email Marketing | `YcWddQ` | `["unique"]` | `week` | Accountbreed |
| Marked Email as Spam | `VQMAAk` | `["unique"]` | `week` | Accountbreed |
| Opened Ticket (Gorgias) | `YzvjGf` | `["count"]` | `day` | Piek na codemails ("code werkt niet") |

**4 · Cohortconversie per arm (T01, T03, T06, T09)**

Vereist de profieleigenschappen uit 01 §2.3 en per arm twee segmenten (aan te maken bij de bouw, niet nu):
- `T01-<flow>-<arm>-instroom-<week>`: `v3_arm_flow = <flow>` AND `v3_arm = <arm>` AND `v3_arm_at` tussen maandag en zondag van die week.
- `T01-<flow>-<arm>-koper-<week>`: idem AND Placed Order at least once tussen maandag van die week en zondag + 7 dagen (welcome + 14).

Lezen met `get_segment` (profile_count) of `query_segment_values`. Cohortconversie = kopers / instroom. Een week is pas "rijp" als het venster voorbij is; tot dan als voorlopig markeren.

**5 · Kortingskosten (T02, T03)**

- Shopify-orders met een code die begint met de poolprefix, per week: ShopifyQL via `mcp__Shopify__run-analytics-query`, bijvoorbeeld `FROM sales SHOW orders, gross_sales, discounts, net_sales GROUP BY discount_code SINCE -7d UNTIL today`. Veldnamen eerst controleren met `mcp__Shopify__search_docs_chunks` (ShopifyQL-referentie) of `mcp__Intelligems__get_shopifyql_reference`; niet raden. Daarna in python groeperen op prefix.
- Kortingskosten per arm: codes zijn per arm uniek (alleen de code-arm krijgt een pool), dus kosten van de no-code-arm = orders met publieke codes (lek, apart rapporteren).
- Marge-bijdrage per ontvanger volgens 01 §1.4, met m zoals Floris die bevestigt.

**6 · Klik per blok (UTM)**

Klaviyo telt klikken per link niet per blok in het rapport. Per blok en per knop: GA4 (sessies en aankopen per `utm_content`) en Shopify (orders per landingspagina-UTM). Zie 04.

## 2. Beslisregels

### 2.1 Voor elke test

1. **Vaste horizon.** Looptijd en n staan vóór de start in `results.csv` (kolommen `planned_n_per_arm`, `planned_end`). Wekelijks kijken mag alleen voor guardrails en SRM.
2. **Vroeg stoppen wegens winst** alleen bij p < 0,001 én minstens 2 volle weken (Haybittle-Peto; laat de 5%-grens voor het einde vrijwel intact).
3. **Vroeg stoppen wegens schade:** guardrail uit 01 §1.3 (uitschrijving > 2x controle, spam > 0,10%, SRM p < 0,01).
4. **Minimaal 30 conversies per arm** voordat RPR meeweegt. Daaronder alleen klik en conversie.
5. **Geen n gehaald op de einddatum:** uitkomst "geen aantoonbaar verschil". Dan wint de controle, of de goedkoopste en merkveiligste variant. Niet verlengen tenzij in het plan stond tot wanneer.
6. **BFCM-weken** (20 nov t/m 6 dec) apart, nooit samenvoegen met gewone weken.

### 2.2 Contenttests (onderwerp, hero, lengte, framing: T04, T05, T07, T08, T12)

Goedkoop en omkeerbaar, dus een lagere drempel is verdedigbaar.

- **Uitrollen B** als: P(klikratio B > A) >= 90% (Beta-binomiaal, zie §2.5) **en** RPR van B niet aantoonbaar slechter (ondergrens 80%-interval van de relatieve RPR-lift > -10%) **en** geen guardrail.
- **Houden A** als P(B > A) < 90% op de einddatum.
- Frequentistisch equivalent als iemand dat liever ziet: tweezijdige z-toets op klikratio p < 0,10.

### 2.3 Codes en kortingen (T02, T03, T09, T10, T13)

Asymmetrisch: geen code (of de kleinste korting) is de standaard. De code moet zich bewijzen.

- Bereken per arm de marge-bijdrage per ontvanger (01 §1.4) en de relatieve conversielift L = conv_code / conv_nocode - 1.
- **Code blijft** als P(L > breakeven) >= 80% (breakeven +20% bij m = 60% en 10%, +33% bij 15%), met de posterior uit §2.5, **en** de marge-bijdrage per ontvanger van de code-arm hoger is (puntschatting) **en** de refundratio niet meer dan 2 procentpunt hoger.
- **Code gaat eruit** als P(L > breakeven) < 50% op de einddatum.
- Tussen 50% en 80%: code eruit in de mails met het laagste volume, doorlopen in de gepoolde rest tot de geplande horizon van fase 2; daarna hoe dan ook beslissen (geen code bij twijfel).
- Na de beslissing altijd de permanente 10%-holdout (01 §4.2).

### 2.4 Oud tegen nieuw (T01)

- **v3 naar 100%** op 20 november tenzij: bovengrens 90%-interval van de relatieve lift in omzet per instromer < 0 (v3 aantoonbaar slechter), of een guardrail breekt.
- Puntschatting negatief maar niet aantoonbaar: v3 blijft (oud pad heeft verboden claims), maar de flow komt bovenaan de testlijst van fase 2.
- Rapport per flow: lift met 90%-interval, cohortconversie per arm, en de voor-na-vergelijking met dezelfde weken in de baseline als extra bewijs.

### 2.5 Rekenhulp (geen apart script nodig)

- **P(B > A) op klik of conversie:** posterior Beta(1 + x, 1 + n - x) per arm, 100.000 trekkingen, aandeel waar B > A. Voor P(L > breakeven): aandeel trekkingen waar p_B / p_A - 1 > breakeven.
- **Interval voor RPR-verschil** (geen per-profieldata nodig): per arm variantie per ontvanger ≈ p x AOV² x (1 + CV²) - (p x AOV)², met CV = 0,7 tot er orderdata is. SE = √(var_A / n_A + var_B / n_B). 90%-interval = verschil ± 1,645 x SE; 80%-interval ± 1,28 x SE.
- **SRM:** chi-kwadraat met 1 vrijheidsgraad op (n_A - verwacht)² / verwacht + (n_B - verwacht)² / verwacht; > 6,63 betekent p < 0,01.
- **Gepoold over strata (T02):** per stratum het verschil in marge per ontvanger en zijn variantie; gewogen gemiddelde met gewicht = delivered van het stratum; SE uit de som van gewogen varianties.

### 2.6 Uitrollen

1. Winnende variant op 100% (Klaviyo: A/B-test beëindigen met de winnaar, of het verliezende pad uit de split halen).
2. Regel in `results.csv` op `status = rolled_out`, datum invullen.
3. Logregel in LOG.md. Als de uitkomst een principe is (bijv. authority wint van social proof in twee flows, of codes leveren niets op): voorstel voor PLAYBOOK of DECISIONS, pas na akkoord van Siraat of Floris.
4. **Naméting na 4 weken:** RPR van de uitgerolde variant naast de testschatting. Verwacht een lagere waarde (regressie naar het gemiddelde); onder 50% van de geschatte lift = notitie in `notes` en de test komt terug op de lijst.
5. Volgende test in die flow pas starten na het uitrollen.

## 3. Logformat: `research/testing/results.csv`

Eén regel per test per arm-vergelijking (bij T02 één regel per stratum plus één regel `stratum = pooled`). Bijwerken elke maandag; de regel wordt overschreven tot `status` op `decided` of `rolled_out` staat. Kommagescheiden, decimale punt, bedragen in USD, ratio's als fractie (0.0123), datums ISO.

| Kolom | Inhoud |
| --- | --- |
| `test_id` | T01 t/m T13 uit 02 |
| `stratum` | flow of mail (`checkout`, `c4-us`, `pooled`) |
| `flow_id` | Klaviyo flow-ID |
| `message_ids` | flow_message_id's, gescheiden door `;` |
| `hypothesis` | één zin |
| `variant_a` / `variant_b` | korte beschrijving, A = controle |
| `utm_term_a` / `utm_term_b` | zie 04 |
| `unit` | `message` of `entrant` |
| `primary_metric` | `click_rate`, `rpr`, `rev_per_entrant`, `margin_per_recipient` |
| `decision_rule` | `content_90`, `code_80`, `oldnew_90` (verwijzing naar §2) |
| `mde_rel` | relatieve MDE waarop gepland is |
| `planned_n_per_arm` | uit 01 §3.2 |
| `start_date` / `planned_end` / `end_date` | ISO |
| `status` | `planned`, `running`, `paused`, `stopped_guardrail`, `decided`, `rolled_out`, `inconclusive` |
| `n_a` / `n_b` | delivered (message) of instromers (entrant) |
| `clicks_a` / `clicks_b` | unieke klikken |
| `conv_a` / `conv_b` | unieke converters (Klaviyo) |
| `cohort_conv_a` / `cohort_conv_b` | kopers in cohortvenster (alleen padtests) |
| `rev_a` / `rev_b` | geattribueerde omzet |
| `rpr_a` / `rpr_b` | omzet / n |
| `aov_a` / `aov_b` | omzet / orders |
| `discount_a` / `discount_b` | kortingsbedrag (codetests) |
| `margin_pr_a` / `margin_pr_b` | marge-bijdrage per ontvanger (01 §1.4) |
| `unsub_rate_a` / `unsub_rate_b` | |
| `spam_rate_a` / `spam_rate_b` | |
| `refund_rate_a` / `refund_rate_b` | alleen codetests |
| `lift_rel` | B ten opzichte van A op de primaire metric |
| `ci90_low` / `ci90_high` | relatieve lift |
| `p_value` | tweezijdig |
| `prob_b_better` | posterior P(B > A), of P(L > breakeven) bij codetests |
| `srm_p` | |
| `decision` | `A`, `B`, `none` |
| `rolled_out_date` | |
| `post_check_rpr` | RPR 4 weken na uitrol |
| `source_notes` | welke calls, welke week-UTC, afwijkingen |
| `notes` | vrij, zonder gedachtestreepjes |

Voorbeeld (fictief, alleen om het format te tonen): `T04,w1,<welcome-v3>,<id-a>;<id-b>,Gift-card-framing verhoogt klik in W1,HI10 code-blok,HI10 gift card,t04-a,t04-b,message,click_rate,content_90,0.25,11455,2026-10-14,2026-11-19,,running,...`
