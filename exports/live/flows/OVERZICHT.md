# v4-flows · overzicht voor controle

Gegenereerd door `scripts/build_flows.py` op 2026-10-08 15:42 (dry-run). Modus: W4 `split`, A/B `action`, T02 op V1/N2 `uit`. De JSON per flow staat ernaast (`<slug>.json`).

Leeswijzer: ⏱ wachttijd · ◆ split (JA/NEE) · 🔀 A/B-actie · ✉ mail (berichtnaam · template-ID · onderwerp). "standaard" = de verzendfilter die op elke mail van die flow staat (zie kop). Takken komen nooit samen: waar het plan een gedeeld vervolg heeft, staat het vervolg per tak apart.

## Samenvatting

| # | Flow | Acties | Mails | Splits | A/B | Controle | Ontbrekend |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | v4 · Post-purchase (`postpurchase`) | 30 | 24 | 3 | 0 | OK | 0 |
| 2 | v4 · Post-purchase · levering (`levering`) | 2 | 1 | 0 | 0 | OK | 0 |
| 3 | v4 · Checkout abandonment (`checkout`) | 26 | 14 | 3 | 0 | OK | 0 |
| 4 | v4 · Cart abandonment (`cart`) | 26 | 13 | 6 | 0 | OK | 0 |
| 5 | v4 · Welcome (`welcome`) | 34 | 17 | 4 | 1 | OK | 0 |
| 6 | v4 · Browse abandonment (`browse`) | 22 | 11 | 8 | 1 | OK | 0 |
| 7 | v4 · VIP (`vip`) | 8 | 4 | 1 | 0 | OK | 0 |
| 8 | v4 · Winback (`winback`) | 17 | 10 | 5 | 0 | OK | 0 |
| 9 | v4 · Anniversary (`anniversary`) | 6 | 3 | 1 | 0 | OK | 0 |
| 10 | v4 · Site abandonment (`site`) | 4 | 2 | 0 | 0 | OK | 0 |
| 11 | v4 · Sunset (`sunset`) | 4 | 2 | 0 | 0 | OK | 0 |
| 12 | v4 · Sunset · kept (`sunsetkept`) | 4 | 2 | 0 | 0 | OK | 2 |
| 13 | v4 · UGC first egg (`ugc`) | 2 | 1 | 0 | 0 | OK | 0 |

Volgorde = bouwvolgorde voor `--live` (een flow verwijst via "Received Email where $flow = ..." naar flows die eerder in de lijst staan). Welcome staat vóór browse, omdat browse filtert op welcome-mails.

## Klaviyo-controle (GET)

| Metric | Verwacht | In Klaviyo |
| --- | --- | --- |
| RfMvni | Checkout Started | Checkout Started |
| QXcV8K | Added to Cart | Added to Cart |
| XNtYMB | Viewed Product | Viewed Product |
| RSNxYV | Placed Order | Placed Order |
| VcUF33 | Delivered Shipment | Delivered Shipment |
| UdCdLD | Active on Site | Active on Site |
| YkRM4Q | Received Email | Received Email |
| W247h8 | Clicked Email | Clicked Email |
| WyrTym | Opened Email | Opened Email |
| Xg6cwn | Refunded Order | Refunded Order |
| YzvjGf | Opened Ticket | Opened Ticket |
| VtEiZT | Fulfilled Order | Fulfilled Order |

- Lijst Uw8eZG: Email List
- Segment "v4 · Sunset · unengaged 120d": WuHSm6
- Segment "v4 · Sunset · suppressed": **ONTBREEKT**
- Segment "v4 · Welcome-bescherming": **ONTBREEKT**
- Segment "v4 · Campagne-cap": **ONTBREEKT**
- Segment "v4 · Heeft kookgerei": **ONTBREEKT**
- Segment "v4 · VIP": **ONTBREEKT**
- Segment "v4 · US": **ONTBREEKT**
- Coupons in Klaviyo: **geen** (alle 8 pools ontbreken)
- Bestaande v4-flows: QWEdbK v4 · Welcome (draft), SLRQPi v4 · Winback (draft), SNwQWU v4 · Checkout abandonment (draft), Spvjdq v4 · Site abandonment (draft), TKPEVE v4 · Browse abandonment (draft), URcvwu v4 · VIP (draft), UshtNX v4 · Cart abandonment (draft), VSqzNN v4 · Post-purchase (draft), Vhi3iH v4 · Sunset (draft), WNDDGi v4 · Post-purchase · levering (draft), WXiUkJ v4 · UGC first egg (draft), YqCwrh v4 · Anniversary (draft)

### Templates die nog geëxporteerd moeten worden

2 templates ontbreken in `exports/live/templates.csv`:

- `v4 · Sunset · kept · s3-kept`
- `v4 · Sunset · kept · s4-kept`

### Coupons (plan 1.4 en 4.4)

| Pool | Korting | Vervalt na | Mail | In Klaviyo |
| --- | --- | --- | --- | --- |
| C4_10_48H | 10% | 48 uur | c4 (checkout) | nee |
| K3_10_48H | 10% | 48 uur | k3 (cart) | nee |
| B2_10_48H | 10% | 48 uur | b2-clicked (browse) | nee |
| P3_THANKYOU_10_14D | 10% | 14 dagen | p3-* (post-purchase) | nee |
| R2_10_72H | 10% | 72 uur | r2 (winback) | nee |
| R2_VIP_15_72H | 15% | 72 uur | r2-vip (winback) | nee |
| SK_REGULARS15_14D | 15% | 14 dagen | v1 (VIP) | nee |
| SK_ANNIV15_7D | 15% | 7 dagen | n2 (anniversary, besluit 8 okt) | nee |

## v4 · Post-purchase (`postpurchase`, utm_campaign `v4-postpurchase`)

- **Trigger**: Placed Order
- **Flowfilters**: niet in deze flow in de laatste 30 dagen
- **Herinstap**: 30 dagen
- P1-FIRST/P1-REPEAT en de P3-router als verzendfilters (geen samenkomende takken). Categorie op Placed Order in de laatste 21 dagen.
- P3-NEXT staat twee keer (deksel in order; of eigenaar die nu een accessoire kocht), want OF tussen twee EN-blokken kan niet in één filter.
- Titellijsten = exacte Shopify-producttitels (8 okt 2026, alle statussen); P2 en P2-SAFE alleen bij pannen en sets (P2_TITELS).
- T02 in P3: één split, alle vijf P3-mails in beide armen (strata P3-pan, P3-set, P3-accessory, P3-next, P3-apron).

- ⏱ wacht 1 uur
- ✉ **P1-FIRST** · `UbyWKv` · "Good call. Here's what's coming."
  - filter: Placed Order = 1 over all time
- ✉ **P1-REPEAT** · `VDtNSq` · "Good to see you again"
  - filter: Placed Order > 1 over all time
- ⏱ wacht 16 dagen, tot 09:00
- ✉ **P2-SAFE** · `Tmgphz` · "When your pan arrives: the first egg"
  - filter: Placed Order (Items contains-any P2_TITELS) > 0 in de laatste 17 dagen EN Delivered Shipment = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen
- ⏱ wacht 4 dagen, tot 09:00
- ◆ split: Placed Order = 2 over all time
  - JA:
    - (einde)
  - NEE:
    - ◆ split: Received Email (Campaign Name contains CODE ·) > 0 in de laatste 30 dagen
      - JA:
        - ✉ **P3-SET nocode · cooldown** · `QXBdhx` · "The pan your set is missing"
          - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 21 dagen EN (Placed Order (Items contains-any SET_TITELS) > 0 in de laatste 21 dagen OF Placed Order ($value greater-than-or-equal 300) > 0 in de laatste 21 dagen)
        - ✉ **P3-NEXT · deksel nocode · cooldown** · `RPULTY` · "How is the pan treating you?"
          - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 21 dagen EN Placed Order (Items contains-any SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order ($value greater-than-or-equal 300) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any DEKSEL_TITELS) > 0 in de laatste 21 dagen
        - ✉ **P3-PAN nocode · cooldown** · `Yrdwwa` · "Which lid fits your pan?"
          - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 21 dagen EN Placed Order (Items contains-any SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order ($value greater-than-or-equal 300) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any DEKSEL_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any PANPRO+VORM_TITELS) > 0 in de laatste 21 dagen
        - ✉ **P3-ACCESSORY · kook nocode · cooldown** · `SLRARP` · "Now meet the pan"
          - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 21 dagen EN Placed Order (Items contains-any SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order ($value greater-than-or-equal 300) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any DEKSEL_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any PANPRO+VORM_TITELS) = 0 in de laatste 21 dagen
        - ✉ **P3-NEXT · eigenaar nocode · cooldown** · `RPULTY` · "How is the pan treating you?"
          - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any E-Gift Card) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 over all time
        - ✉ **P3-APRON nocode · cooldown** · `Yn22gV` · "An apron deserves a pan"
          - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any E-Gift Card) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 over all time EN Placed Order (Items contains-any SCHORT_TITELS) > 0 in de laatste 21 dagen
        - ✉ **P3-ACCESSORY · acc nocode · cooldown** · `SLRARP` · "Now meet the pan"
          - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any E-Gift Card) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 over all time EN Placed Order (Items contains-any SCHORT_TITELS) = 0 in de laatste 21 dagen
      - NEE:
        - ◆ split: random 50%
          - JA:
            - ✉ **CODE · P3-SET** · `UYcw5P` · "The pan your set is missing"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 21 dagen EN (Placed Order (Items contains-any SET_TITELS) > 0 in de laatste 21 dagen OF Placed Order ($value greater-than-or-equal 300) > 0 in de laatste 21 dagen)
            - ✉ **CODE · P3-NEXT · deksel** · `VHgz9Z` · "How is the pan treating you?"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 21 dagen EN Placed Order (Items contains-any SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order ($value greater-than-or-equal 300) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any DEKSEL_TITELS) > 0 in de laatste 21 dagen
            - ✉ **CODE · P3-PAN** · `VFfyZu` · "Which lid fits your pan?"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 21 dagen EN Placed Order (Items contains-any SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order ($value greater-than-or-equal 300) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any DEKSEL_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any PANPRO+VORM_TITELS) > 0 in de laatste 21 dagen
            - ✉ **CODE · P3-ACCESSORY · kook** · `YxgwXH` · "Now meet the pan"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 21 dagen EN Placed Order (Items contains-any SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order ($value greater-than-or-equal 300) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any DEKSEL_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any PANPRO+VORM_TITELS) = 0 in de laatste 21 dagen
            - ✉ **CODE · P3-NEXT · eigenaar** · `VHgz9Z` · "How is the pan treating you?"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any E-Gift Card) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 over all time
            - ✉ **CODE · P3-APRON** · `UsDdSp` · "An apron deserves a pan"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any E-Gift Card) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 over all time EN Placed Order (Items contains-any SCHORT_TITELS) > 0 in de laatste 21 dagen
            - ✉ **CODE · P3-ACCESSORY · acc** · `YxgwXH` · "Now meet the pan"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any E-Gift Card) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 over all time EN Placed Order (Items contains-any SCHORT_TITELS) = 0 in de laatste 21 dagen
          - NEE:
            - ✉ **P3-SET nocode · T02-B** · `QXBdhx` · "The pan your set is missing"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 21 dagen EN (Placed Order (Items contains-any SET_TITELS) > 0 in de laatste 21 dagen OF Placed Order ($value greater-than-or-equal 300) > 0 in de laatste 21 dagen)
            - ✉ **P3-NEXT · deksel nocode · T02-B** · `RPULTY` · "How is the pan treating you?"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 21 dagen EN Placed Order (Items contains-any SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order ($value greater-than-or-equal 300) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any DEKSEL_TITELS) > 0 in de laatste 21 dagen
            - ✉ **P3-PAN nocode · T02-B** · `Yrdwwa` · "Which lid fits your pan?"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 21 dagen EN Placed Order (Items contains-any SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order ($value greater-than-or-equal 300) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any DEKSEL_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any PANPRO+VORM_TITELS) > 0 in de laatste 21 dagen
            - ✉ **P3-ACCESSORY · kook nocode · T02-B** · `SLRARP` · "Now meet the pan"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 21 dagen EN Placed Order (Items contains-any SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order ($value greater-than-or-equal 300) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any DEKSEL_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any PANPRO+VORM_TITELS) = 0 in de laatste 21 dagen
            - ✉ **P3-NEXT · eigenaar nocode · T02-B** · `RPULTY` · "How is the pan treating you?"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any E-Gift Card) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 over all time
            - ✉ **P3-APRON nocode · T02-B** · `Yn22gV` · "An apron deserves a pan"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any E-Gift Card) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 over all time EN Placed Order (Items contains-any SCHORT_TITELS) > 0 in de laatste 21 dagen
            - ✉ **P3-ACCESSORY · acc nocode · T02-B** · `SLRARP` · "Now meet the pan"
              - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any E-Gift Card) = 0 in de laatste 21 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 over all time EN Placed Order (Items contains-any SCHORT_TITELS) = 0 in de laatste 21 dagen

## v4 · Post-purchase · levering (`levering`, utm_campaign `v4-postpurchase`)

- **Trigger**: Delivered Shipment
- **Flowfilters**: Placed Order (Items contains-any P2_TITELS) > 0 in de laatste 30 dagen EN niet in deze flow in de laatste 30 dagen EN Received Email (Campaign Name contains P2-SAFE) = 0 in de laatste 30 dagen
- **Herinstap**: 30 dagen

- ⏱ wacht 1 dagen, tot 09:00
- ✉ **P2** · `T7nCfp` · "The mistake that makes titanium stick"
  - filter: Refunded Order = 0 in de laatste 30 dagen

## v4 · Checkout abandonment (`checkout`, utm_campaign `v4-checkout`)

- **Trigger**: Checkout Started · triggerfilter: event.$value greater-than 0
- **Flowfilters**: Placed Order = 0 sinds flowstart EN niet in deze flow in de laatste 14 dagen EN Received Email ($flow = v4 · Post-purchase (VSqzNN)) = 0 in de laatste 7 dagen
- **Herinstap**: 14 dagen
- **Standaard verzendfilter op elke v4-mail**: Placed Order = 0 sinds flowstart
- **Verwijst naar**: v4 · Post-purchase
- Oud pad uit Y2TmNB (GET): wacht 10 minuten → UD7QXp "Don’t leave these hanging" → wacht 1 dagen tot 08:30 → TK3h6j "Join the Happy Chef Club" → wacht 1 dagen → VPBrLr "We’ve cooked something for you!" → wacht 2 dagen → UMURrd "One Click to Cooking Better for Life" → wacht 1 dagen → RbaQfc "We Can’t Keep these Forever"
- Landsplit vervallen (country-split-review): C4 is één template `c4` / `c4-nocode`, land via {% if %} in de template.
- Categorie (C2/C2-ACC, C3-S/C3-P/C3-ACC) als verzendfilter op Checkout Started in de laatste 2/4 dagen (Bouwnotitie 2.1).
- v5: C3-S = grote set in de checkout (GROOT_SET_TITELS); C3-P = Pan Pro of starterbundel (Pro Duo, Kit, 2 Pans + 2 Lids) onder $300 zonder grote set. Geen $value-route naar C3-S meer.

- ◆ split: random 50%
  - JA:
    - ⏱ wacht 30 minuten
    - ✉ **C1** · `U8Ngv8` · "Your cart + 4 gifts are still pending"
      - filter: standaard
    - ⏱ wacht 1 dagen
    - ✉ **C2** · `Syf9Si` · "Has the pan in your cart been tested?"
      - filter: standaard EN Checkout Started (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 2 dagen EN Placed Order = 0 over all time
    - ✉ **C2-ACC** · `QZH3pZ` · "Yours, or a gift? Both work."
      - filter: standaard EN Checkout Started (Items contains-any KOOK_TITELS+SET_TITELS) = 0 in de laatste 2 dagen
    - ⏱ wacht 2 dagen, tot 09:00
    - ✉ **C3-S** · `Veb75W` · "What's in the box with your set"
      - filter: standaard EN Checkout Started (Items contains-any GROOT_SET_TITELS (sets zonder starterbundels)) > 0 in de laatste 4 dagen
    - ✉ **C3-P** · `W75UJK` · "One pan, or three?"
      - filter: standaard EN Checkout Started (Items contains-any PANPRO_TITELS+STARTER_TITELS) > 0 in de laatste 4 dagen EN Checkout Started ($value less-than 300) > 0 in de laatste 4 dagen EN Checkout Started (Items contains-any GROOT_SET_TITELS (sets zonder starterbundels)) = 0 in de laatste 4 dagen
    - ✉ **C3-ACC** · `SL7UKX` · "The pan we made after the board"
      - filter: standaard EN Checkout Started (Items contains-any KOOK_TITELS+SET_TITELS) = 0 in de laatste 4 dagen EN Placed Order = 0 over all time
    - ⏱ wacht 2 dagen, tot 09:00
    - ◆ split: Received Email (Campaign Name contains CODE ·) > 0 in de laatste 30 dagen
      - JA:
        - ✉ **C4 nocode · cooldown** · `SAqA6j` · "Last email about your cart"
          - filter: standaard
      - NEE:
        - ◆ split: random 50%
          - JA:
            - ✉ **CODE · C4** · `UdzWU2` · "We're removing your discount in 48 hours"
              - filter: standaard
          - NEE:
            - ✉ **C4 nocode · T02-B** · `SAqA6j` · "Last email about your cart"
              - filter: standaard
  - NEE:
    - ⏱ wacht 10 minuten
    - ✉ **Old · Checkout 1** · `UD7QXp` · "Don’t leave these hanging"
      - filter: standaard
    - ⏱ wacht 1 dagen, tot 08:30
    - ✉ **Old · Checkout 2** · `TK3h6j` · "Join the Happy Chef Club"
      - filter: standaard
    - ⏱ wacht 1 dagen
    - ✉ **Old · Checkout 3** · `VPBrLr` · "We’ve cooked something for you!"
      - filter: standaard
    - ⏱ wacht 2 dagen
    - ✉ **Old · Checkout 4** · `UMURrd` · "One Click to Cooking Better for Life"
      - filter: standaard
    - ⏱ wacht 1 dagen
    - ✉ **Old · Checkout 5** · `RbaQfc` · "We Can’t Keep these Forever"
      - filter: standaard

## v4 · Cart abandonment (`cart`, utm_campaign `v4-cart`)

- **Trigger**: Added to Cart · triggerfilter: event.Price greater-than 0 EN event.Product Name not-contains Mystery Gift EN event.Product Name not-contains E-Book EN event.Product Name not-contains Free Shipping EN event.Product Name not-contains Giveaway
- **Flowfilters**: Checkout Started = 0 sinds flowstart EN Placed Order = 0 sinds flowstart EN Received Email ($flow = v4 · Checkout abandonment (SNwQWU)) = 0 in de laatste 7 dagen EN niet in deze flow in de laatste 14 dagen
- **Herinstap**: 14 dagen
- **Standaard verzendfilter op elke v4-mail**: Checkout Started = 0 sinds flowstart EN Placed Order = 0 sinds flowstart
- **Verwijst naar**: v4 · Checkout abandonment
- Oud pad uit SwkMyn (GET): wacht 15 minuten → XTCs5P "Hi {{ first_name }}, we saved these for you" → wacht 2 dagen tot 08:00 → ULxcYG "Hi {{ first_name }}, getting cooking with 10% off" → wacht 1 dagen tot 08:00 → UFTWDi "Last Call for 10% Off!"
- CS K: Added to Cart waarvan Product Name een kookwoord bevat, in de laatste 1 dag (OF tussen de woorden).

- ◆ split: random 50%
  - JA:
    - ⏱ wacht 30 minuten
    - ◆ split: (Added to Cart (Product Name contains Hammer) > 0 in de laatste 1 dagen OF Added to Cart (Product Name contains Pan) > 0 in de laatste 1 dagen OF Added to Cart (Product Name contains Pot) > 0 in de laatste 1 dagen OF Added to Cart (Product Name contains ookware) > 0 in de laatste 1 dagen OF Added to Cart (Product Name contains Everything) > 0 in de laatste 1 dagen OF Added to Cart (Product Name contains fanne) > 0 in de laatste 1 dagen OF Added to Cart (Product Name contains Prep Bundle) > 0 in de laatste 1 dagen)
      - JA:
        - ✉ **K1** · `UnutzT` · "The hammered pattern: an easy wipe"
          - filter: standaard
        - ⏱ wacht 1 dagen
        - ✉ **K2-RETURNING** · `QTssZ3` · "Adding to your Siraat kitchen?"
          - filter: standaard EN Placed Order > 0 over all time
        - ✉ **K2-NEW** · `T72Ceu` · "15 coated pans, or one"
          - filter: standaard EN Placed Order = 0 over all time
        - ⏱ wacht 2 dagen, tot 09:00
        - ◆ split: Received Email (Campaign Name contains CODE ·) > 0 in de laatste 30 dagen
          - JA:
            - ✉ **K3 · pan nocode · cooldown** · `TBpqmc` · "What if it's not for you?"
              - filter: standaard
          - NEE:
            - ◆ split: random 50%
              - JA:
                - ✉ **CODE · K3 · pan** · `Rz5KNx` · "We're removing your cart's 10%"
                  - filter: standaard
              - NEE:
                - ✉ **K3 · pan nocode · T02-B** · `TBpqmc` · "What if it's not for you?"
                  - filter: standaard
      - NEE:
        - ✉ **K1-ACC** · `Yt7LFd` · "Picked it out? It's still here."
          - filter: standaard
        - ⏱ wacht 3 dagen, tot 09:00
        - ◆ split: Received Email (Campaign Name contains CODE ·) > 0 in de laatste 30 dagen
          - JA:
            - ✉ **K3 · acc nocode · cooldown** · `TBpqmc` · "What if it's not for you?"
              - filter: standaard
          - NEE:
            - ◆ split: random 50%
              - JA:
                - ✉ **CODE · K3 · acc** · `Rz5KNx` · "We're removing your cart's 10%"
                  - filter: standaard
              - NEE:
                - ✉ **K3 · acc nocode · T02-B** · `TBpqmc` · "What if it's not for you?"
                  - filter: standaard
  - NEE:
    - ⏱ wacht 15 minuten
    - ✉ **Old · Cart 1** · `XTCs5P` · "Hi {{ first_name }}, we saved these for you"
      - filter: Placed Order = 0 sinds flowstart
    - ⏱ wacht 2 dagen, tot 08:00
    - ✉ **Old · Cart 2** · `ULxcYG` · "Hi {{ first_name }}, getting cooking with 10% off"
      - filter: (Placed Order = 0 in de laatste 10 dagen OF Checkout Started = 0 in de laatste 10 dagen OF Checkout Started (Triple Pixel) = 0 in de laatste 10 dagen) EN Placed Order = 0 sinds flowstart
    - ⏱ wacht 1 dagen, tot 08:00
    - ✉ **Old · Cart 3** · `UFTWDi` · "Last Call for 10% Off!"
      - filter: (Placed Order = 0 in de laatste 10 dagen OF Checkout Started = 0 in de laatste 10 dagen OF Checkout Started (Triple Pixel) = 0 in de laatste 10 dagen) EN Opened Email > 0 sinds flowstart EN Placed Order = 0 sinds flowstart

## v4 · Welcome (`welcome`, utm_campaign `v4-welcome`)

- **Trigger**: lijst Uw8eZG
- **Flowfilters**: email not-contains test@ EN niet in deze flow over all time
- **Herinstap**: geen grens (alleen via flowfilter)
- **Standaard verzendfilter op elke v4-mail**: Placed Order = 0 sinds flowstart EN Received Email ($flow = v4 · Checkout abandonment (SNwQWU)) = 0 in de laatste 1 dagen EN Received Email ($flow = v4 · Cart abandonment (UshtNX)) = 0 in de laatste 1 dagen
- **Verwijst naar**: v4 · Cart abandonment, v4 · Checkout abandonment
- Oud pad uit SiaNLu (GET): wacht 5 minuten → YdWRjr "{{ first_name|default:'Hey' }}, Thanks For Joining Us" → wacht 1 dagen tot 10:00 → TicuGn "A Note from Benjamin" → wacht 1 dagen tot 10:00 → R8HSS3 "Hey {{ first_name|default:'there' }}, Save 10% On a Lifetime of Use" → wacht 1 dagen → SqPaYF "Straight from the kitchen" → wacht 2 dagen tot 10:00 → SCsFQT "Cook with the Best" → wacht 2 dagen tot 10:00 → WZkL9P "The ultimate showdown" → wacht 2 dagen tot 10:00 → Tkx4bs "See Why We Are Top Rated" → wacht 1 dagen → RqvU5g "Last Call for an Extra 10% Off"
- W4-modus: split (landsplit w4-us/w4-int, US = United States of US).
- T2SmtR (Failure to launch) kan geen filter v3_arm krijgen (update-profile kan niet via API): zie GO-LIVE.md.

- ◆ split: random 50%
  - JA:
    - ⏱ wacht 20 minuten
    - ◆ split: Placed Order > 0 sinds flowstart
      - JA:
        - (einde)
      - NEE:
        - ◆ split: Placed Order > 0 over all time
          - JA:
            - ✉ **W0** · `Ypywny` · "Thank you. Now the first egg."
              - filter: standaard
          - NEE:
            - 🔀 A/B-actie **T04 · W1-A code-blok tegen W1-B gift card** (50/50, geen automatische winnaar, winnaar op unique-clicks)
              - ✉ **W1 · T04-A** · `Wuunna` · "No PFAS. Here's the paper. And 10%."
                - filter: standaard
              - ✉ **W1 · T04-B** · `VwWimX` · "No PFAS. Here's the paper. And 10%."
                - filter: standaard
            - ⏱ wacht 1 dagen, tot 09:00
            - ✉ **W2** · `Xa7FbE` · "The pan nobody else was making" · afzender Benjamin at Siraat's Kitchen
              - filter: standaard
            - ⏱ wacht 2 dagen, tot 09:00
            - ✉ **W3** · `SstjtH` · "Has your cookware been tested?"
              - filter: standaard
            - ⏱ wacht 3 dagen, tot 09:00
            - ◆ split: (location['country'] equals United States OF location['country'] equals US)
              - JA:
                - ✉ **W4-US** · `QZ9Hpa` · "Who are you cooking for?"
                  - filter: standaard
                - ⏱ wacht 4 dagen, tot 09:00
                - ✉ **W5** · `RngYXB` · "Tammy is on her fourth pan"
                  - filter: standaard
              - NEE:
                - ✉ **W4-INT** · `VGN577` · "Who are you cooking for?"
                  - filter: standaard
                - ⏱ wacht 4 dagen, tot 09:00
                - ✉ **W5** · `RngYXB` · "Tammy is on her fourth pan"
                  - filter: standaard
  - NEE:
    - ⏱ wacht 5 minuten
    - ✉ **Old · Welcome 1** · `YdWRjr` · "{{ first_name|default:'Hey' }}, Thanks For Joining Us"
      - filter: Placed Order = 0 sinds flowstart
    - ⏱ wacht 1 dagen, tot 10:00
    - ✉ **Old · Welcome 2** · `TicuGn` · "A Note from Benjamin"
      - filter: Placed Order = 0 sinds flowstart
    - ⏱ wacht 1 dagen, tot 10:00
    - ✉ **Old · Welcome 3** · `R8HSS3` · "Hey {{ first_name|default:'there' }}, Save 10% On a Lifetime of Use"
      - filter: Placed Order = 0 sinds flowstart
    - ⏱ wacht 1 dagen
    - ✉ **Old · Welcome 4** · `SqPaYF` · "Straight from the kitchen"
      - filter: Opened Email > 0 sinds flowstart EN Placed Order = 0 sinds flowstart EN Placed Order = 0 sinds flowstart
    - ⏱ wacht 2 dagen, tot 10:00
    - ✉ **Old · Welcome 5** · `SCsFQT` · "Cook with the Best"
      - filter: Opened Email ≥ 2 sinds flowstart EN Placed Order = 0 sinds flowstart EN Placed Order = 0 sinds flowstart
    - ⏱ wacht 2 dagen, tot 10:00
    - ✉ **Old · Welcome 6** · `WZkL9P` · "The ultimate showdown"
      - filter: Opened Email ≥ 2 sinds flowstart EN Placed Order = 0 sinds flowstart EN Placed Order = 0 sinds flowstart
    - ⏱ wacht 2 dagen, tot 10:00
    - ✉ **Old · Welcome 7** · `Tkx4bs` · "See Why We Are Top Rated"
      - filter: Placed Order = 0 sinds flowstart
    - ⏱ wacht 1 dagen
    - ✉ **Old · Welcome 8** · `RqvU5g` · "Last Call for an Extra 10% Off"
      - filter: Placed Order = 0 sinds flowstart

## v4 · Browse abandonment (`browse`, utm_campaign `v4-browse`)

- **Trigger**: Viewed Product
- **Flowfilters**: Added to Cart = 0 sinds flowstart EN Checkout Started = 0 sinds flowstart EN Placed Order = 0 sinds flowstart EN Received Email ($flow = v4 · Cart abandonment (UshtNX)) = 0 in de laatste 7 dagen EN Received Email ($flow = v4 · Checkout abandonment (SNwQWU)) = 0 in de laatste 7 dagen EN Received Email ($flow = v4 · Welcome (QWEdbK)) = 0 in de laatste 7 dagen EN niet in deze flow in de laatste 7 dagen
- **Herinstap**: 7 dagen
- **Standaard verzendfilter op elke v4-mail**: Placed Order = 0 sinds flowstart
- **Verwijst naar**: v4 · Cart abandonment, v4 · Checkout abandonment, v4 · Welcome
- Oud pad uit TyEjuQ (GET): wacht 10 minuten → X9w6vN "Hi {{ first_name|default:'' }}, we saw you looking..."
- Kookgerei-split: Viewed Product waarvan Name een kookwoord bevat in de laatste 1 dag (plan: trigger split; nu CS met dezelfde uitkomst).
- Klik-split: Clicked Email waarvan Campaign Name 'B1 · T05a' (of 'B1-ACC') bevat sinds flowstart; bij de eerste test controleren dat Campaign Name de berichtnaam is.
- Oud pad: TyEjuQ 10-minutenarm ($1,31 tegen $1,18 per ontvanger, research/timing/01-data.md).

- ◆ split: random 50%
  - JA:
    - ⏱ wacht 1 uur
    - ◆ split: (Viewed Product (Name contains Hammer) > 0 in de laatste 1 dagen OF Viewed Product (Name contains Pan) > 0 in de laatste 1 dagen OF Viewed Product (Name contains Pot) > 0 in de laatste 1 dagen OF Viewed Product (Name contains ookware) > 0 in de laatste 1 dagen OF Viewed Product (Name contains Everything) > 0 in de laatste 1 dagen OF Viewed Product (Name contains fanne) > 0 in de laatste 1 dagen OF Viewed Product (Name contains Prep Bundle) > 0 in de laatste 1 dagen)
      - JA:
        - 🔀 A/B-actie **T05a · B1-onderwerp (authority tegen social proof)** (50/50, geen automatische winnaar, winnaar op unique-clicks)
          - ✉ **B1 · T05a-A** · `VwGNp3` · "Get this pan with 10% off"
            - filter: standaard
          - ✉ **B1 · T05a-B** · `VwGNp3` · "Why I started making this pan"
            - filter: standaard
        - ⏱ wacht 2 dagen, tot 09:00
        - ◆ split: Clicked Email (Campaign Name contains B1 · T05a) > 0 sinds flowstart
          - JA:
            - ◆ split: Received Email (Campaign Name contains CODE ·) > 0 in de laatste 30 dagen
              - JA:
                - ✉ **B2-CLICKED · pan nocode · cooldown** · `Uuxu3s` · ""I ordered one pan to try it out""
                  - filter: standaard EN Added to Cart = 0 sinds flowstart
              - NEE:
                - ◆ split: random 50%
                  - JA:
                    - ✉ **CODE · B2-CLICKED · pan** · `TwZq3f` · "Your own 10% expires in 48 hours"
                      - filter: standaard EN Added to Cart = 0 sinds flowstart
                  - NEE:
                    - ✉ **B2-CLICKED · pan nocode · T02-B** · `Uuxu3s` · ""I ordered one pan to try it out""
                      - filter: standaard EN Added to Cart = 0 sinds flowstart
          - NEE:
            - ✉ **B2-NOTCLICKED** · `TEeUzw` · "Skeptical? So were they."
              - filter: standaard EN Added to Cart = 0 sinds flowstart
      - NEE:
        - ✉ **B1-ACC** · `TYaFUJ` · "Looked twice? Here's the detail."
          - filter: standaard
        - ⏱ wacht 2 dagen, tot 09:00
        - ◆ split: Clicked Email (Campaign Name contains B1-ACC) > 0 sinds flowstart
          - JA:
            - ◆ split: Received Email (Campaign Name contains CODE ·) > 0 in de laatste 30 dagen
              - JA:
                - ✉ **B2-CLICKED · acc nocode · cooldown** · `Uuxu3s` · ""I ordered one pan to try it out""
                  - filter: standaard EN Added to Cart = 0 sinds flowstart
              - NEE:
                - ◆ split: random 50%
                  - JA:
                    - ✉ **CODE · B2-CLICKED · acc** · `TwZq3f` · "Your own 10% expires in 48 hours"
                      - filter: standaard EN Added to Cart = 0 sinds flowstart
                  - NEE:
                    - ✉ **B2-CLICKED · acc nocode · T02-B** · `Uuxu3s` · ""I ordered one pan to try it out""
                      - filter: standaard EN Added to Cart = 0 sinds flowstart
          - NEE:
            - (einde)
  - NEE:
    - ⏱ wacht 10 minuten
    - ✉ **Old · Browse 1** · `X9w6vN` · "Hi {{ first_name|default:'' }}, we saw you looking..."
      - filter: standaard

## v4 · VIP (`vip`, utm_campaign `v4-vip`)

- **Trigger**: Placed Order
- **Flowfilters**: Placed Order = 2 over all time EN niet in deze flow over all time
- **Herinstap**: geen grens (alleen via flowfilter)
- V1-cooldown (--vip-cooldown=codes): cooldown = CODE-mail in 30 dagen EN Placed Order in 45 dagen met Discount Codes niet leeg. Onbevestigd in de API: de list-operator 'length-greater-than' op 'Discount Codes'. Weigert Klaviyo de POST, dan opnieuw met --vip-cooldown=discounts, en anders --vip-cooldown=none.
- T02 op V1: uit (eerste 4 weken 100% code zonder cooldown; daarna --t02-new).
- siraat_regular = true (update profile) kan niet via de API; segment 'v4 · VIP' = Placed Order minstens 2 keer.
- Flowfilter Placed Order = 2 over all time geldt bij elke stap: een 3e order vóór dag 30 haalt iemand uit de flow.

- ⏱ wacht 30 dagen, tot 09:00
- ◆ split: Received Email (Campaign Name contains CODE ·) > 0 in de laatste 30 dagen EN Placed Order (Discount Codes length-greater-than 0) > 0 in de laatste 45 dagen
  - JA:
    - ✉ **V1 nocode · cooldown** · `SthPxw` · "You're a VIP. Thank you."
      - filter: Refunded Order = 0 sinds flowstart EN Placed Order = 0 in de laatste 14 dagen
    - ⏱ wacht 10 dagen, tot 09:00
    - ✉ **V2** · `XXNYBe` · "A question from Benjamin" · afzender Benjamin at Siraat's Kitchen
      - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 sinds flowstart
  - NEE:
    - ✉ **CODE · V1** · `Xw4sFp` · "You're a VIP. Here's 15% off."
      - filter: Refunded Order = 0 sinds flowstart EN Placed Order = 0 in de laatste 14 dagen
    - ⏱ wacht 10 dagen, tot 09:00
    - ✉ **V2** · `XXNYBe` · "A question from Benjamin" · afzender Benjamin at Siraat's Kitchen
      - filter: Placed Order = 0 sinds flowstart EN Refunded Order = 0 sinds flowstart

## v4 · Winback (`winback`, utm_campaign `v4-winback`)

- **Trigger**: Placed Order
- **Flowfilters**: geen
- **Herinstap**: geen grens (alleen via flowfilter)
- **Standaard verzendfilter op elke v4-mail**: Placed Order = 0 sinds flowstart
- **Verwijst naar**: v4 · Post-purchase, v4 · VIP
- Geen herinstapgrens (3.11): elke order start een nieuwe run; de oude stopt via de verzendfilter Placed Order = 0 sinds start.
- R1-router als verzendfilters op Placed Order in de laatste 46 dagen. R2 alleen zolang 'up to 50% off' live is.

- ⏱ wacht 45 dagen, tot 09:00
- ✉ **R1-SET** · `TtN9Kv` · "The shapes a set leaves out"
  - filter: standaard EN Received Email ($flow = v4 · Post-purchase (VSqzNN)) = 0 in de laatste 7 dagen EN Received Email ($flow = v4 · VIP (URcvwu)) = 0 in de laatste 7 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 46 dagen EN (Placed Order (Items contains-any SET_TITELS) > 0 in de laatste 46 dagen OF Placed Order ($value greater-than-or-equal 300) > 0 in de laatste 46 dagen)
- ✉ **R1-PAN · kook** · `RN2wJV` · "How's your pan doing?"
  - filter: standaard EN Received Email ($flow = v4 · Post-purchase (VSqzNN)) = 0 in de laatste 7 dagen EN Received Email ($flow = v4 · VIP (URcvwu)) = 0 in de laatste 7 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 in de laatste 46 dagen EN Placed Order (Items contains-any SET_TITELS) = 0 in de laatste 46 dagen EN Placed Order ($value greater-than-or-equal 300) = 0 in de laatste 46 dagen
- ✉ **R1-PAN · eigenaar** · `RN2wJV` · "How's your pan doing?"
  - filter: standaard EN Received Email ($flow = v4 · Post-purchase (VSqzNN)) = 0 in de laatste 7 dagen EN Received Email ($flow = v4 · VIP (URcvwu)) = 0 in de laatste 7 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 in de laatste 46 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 over all time
- ✉ **R1-ACC** · `Wr3C7u` · "Ready for the pan?"
  - filter: standaard EN Received Email ($flow = v4 · Post-purchase (VSqzNN)) = 0 in de laatste 7 dagen EN Received Email ($flow = v4 · VIP (URcvwu)) = 0 in de laatste 7 dagen EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) = 0 over all time
- ⏱ wacht 30 dagen, tot 09:00
- ◆ split: Placed Order ≥ 2 over all time
  - JA:
    - ◆ split: Received Email (Campaign Name contains CODE ·) > 0 in de laatste 30 dagen
      - JA:
        - ✉ **R2-VIP nocode · cooldown** · `VLAPnG` · "You came back. Thank you."
          - filter: standaard
      - NEE:
        - ◆ split: random 50%
          - JA:
            - ✉ **CODE · R2-VIP** · `Xj8VQZ` · "15% exclusive discount, 72 hours"
              - filter: standaard
          - NEE:
            - ✉ **R2-VIP nocode · T02-B** · `VLAPnG` · "You came back. Thank you."
              - filter: standaard
  - NEE:
    - ◆ split: Received Email (Campaign Name contains CODE ·) > 0 in de laatste 30 dagen
      - JA:
        - ✉ **R2 nocode · cooldown** · `TB3EhL` · "Ready for pan number two?"
          - filter: standaard
      - NEE:
        - ◆ split: random 50%
          - JA:
            - ✉ **CODE · R2** · `Yjhg45` · "Your 10% expires in 72 hours"
              - filter: standaard
          - NEE:
            - ✉ **R2 nocode · T02-B** · `TB3EhL` · "Ready for pan number two?"
              - filter: standaard

## v4 · Anniversary (`anniversary`, utm_campaign `v4-anniversary`)

- **Trigger**: Placed Order
- **Flowfilters**: Placed Order = 1 over all time EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 over all time EN niet in deze flow over all time
- **Herinstap**: geen grens (alleen via flowfilter)
- **Verwijst naar**: v4 · VIP, v4 · Winback
- Triggerfilter 'Items bevat kookgerei' als flowfilter: Placed Order met KOOK+SET minstens 1 keer over all time (samen met Placed Order = 1 over all time is dat de eerste order). Een filter 'in de laatste dag' zou bij de herbeoordeling op dag 182 iedereen eruit halen.
- Placed Order = 1 over all time wordt bij elke stap opnieuw gecontroleerd: wie binnen het jaar opnieuw koopt, krijgt geen N1/N2.
- 182 en 183 dagen in één wachttijd (als Klaviyo weigert: --max-delay=91).

- ⏱ wacht 182 dagen, tot 09:00
- ✉ **N1** · `QX8tha` · "Six months in. Anything worn off?"
  - filter: Refunded Order = 0 sinds flowstart EN Received Email ($flow = v4 · VIP (URcvwu)) = 0 in de laatste 14 dagen EN Received Email ($flow = v4 · Winback (SLRQPi)) = 0 in de laatste 14 dagen EN Opened Ticket = 0 in de laatste 14 dagen
- ⏱ wacht 183 dagen, tot 09:00
- ◆ split: Received Email (Campaign Name contains CODE ·) > 0 in de laatste 30 dagen
  - JA:
    - ✉ **N2 nocode · cooldown** · `RZT3F7` · "One year ago this week"
      - filter: Refunded Order = 0 sinds flowstart EN Placed Order = 0 in de laatste 14 dagen
  - NEE:
    - ✉ **CODE · N2** · `WTpa8c` · "One year in. Here's 15% off."
      - filter: Refunded Order = 0 sinds flowstart EN Placed Order = 0 in de laatste 14 dagen

## v4 · Site abandonment (`site`, utm_campaign `v4-site`)

- **Trigger**: Active on Site
- **Flowfilters**: Viewed Product = 0 sinds flowstart EN Added to Cart = 0 sinds flowstart EN Checkout Started = 0 sinds flowstart EN Placed Order = 0 sinds flowstart EN Placed Order = 0 in de laatste 30 dagen EN Received Email ($flow = v4 · Browse abandonment (TKPEVE)) = 0 in de laatste 7 dagen EN Received Email ($flow = v4 · Cart abandonment (UshtNX)) = 0 in de laatste 7 dagen EN Received Email ($flow = v4 · Checkout abandonment (SNwQWU)) = 0 in de laatste 7 dagen EN Received Email ($flow = v4 · Post-purchase (VSqzNN)) = 0 in de laatste 7 dagen EN Received Email ($flow = v4 · Welcome (QWEdbK)) = 0 in de laatste 10 dagen EN niet in deze flow in de laatste 14 dagen
- **Herinstap**: 14 dagen
- **Standaard verzendfilter op elke v4-mail**: Viewed Product = 0 sinds flowstart EN Added to Cart = 0 sinds flowstart EN Checkout Started = 0 sinds flowstart EN Placed Order = 0 sinds flowstart
- **Verwijst naar**: v4 · Browse abandonment, v4 · Cart abandonment, v4 · Checkout abandonment, v4 · Post-purchase, v4 · Welcome
- 'Can receive email marketing' niet als filter: marketingmails gaan in Klaviyo nooit naar uitgeschreven profielen.

- ⏱ wacht 2 uur
- ✉ **A1** · `SJBkFR` · "Four eggs or five?"
  - filter: standaard
- ⏱ wacht 2 dagen, tot 09:00
- ✉ **A2** · `SePNBv` · "Where 100,000+ customers started"
  - filter: standaard

## v4 · Sunset (`sunset`, utm_campaign `v4-sunset`)

- **Trigger**: segment WuHSm6
- **Flowfilters**: niet in deze flow in de laatste 180 dagen EN Received Email ($flow = v4 · Welcome (QWEdbK)) = 0 in de laatste 30 dagen EN Received Email ($flow = v4 · Post-purchase (VSqzNN)) = 0 in de laatste 30 dagen
- **Herinstap**: 180 dagen
- **Verwijst naar**: v4 · Post-purchase, v4 · Welcome
- Stap 3 (update profile sunset_status) kan niet via de API. Vervanging: segment 'v4 · Sunset · suppressed' = in 'v4 · Sunset · unengaged 120d' EN Received Email waarvan Campaign Name 'SUNSET · S2' bevat, minstens 1 keer in 60 dagen EN 0 keer in de laatste 3 dagen. Wie klikt, de site bezoekt of koopt valt vanzelf uit het unengaged-segment.
- Geen Opened Email-filter (3.16).
- S2-filter telt alleen menselijke klikken (Clicked Email waarvan Bot Click = false, research/v5/06 fix 3); een scannerklik slaat S2 niet meer over. Segment WuHSm6 zelf wordt in de hoofdsessie bijgewerkt (research/v5/08-integratie.md).
- Vervolg voor wie klikt: aparte flow 'v4 · Sunset · kept' (sunsetkept).

- ⏱ wacht 1 dagen, tot 09:00
- ✉ **SUNSET · S1** · `VvayeT` · "Should we keep writing to you?"
- ⏱ wacht 4 dagen, tot 09:00
- ✉ **SUNSET · S2** · `ScNNsY` · "Last email from me (unless you tap)" · afzender Benjamin at Siraat's Kitchen
  - filter: Clicked Email (Bot Click equals False) = 0 sinds flowstart EN Active on Site = 0 sinds flowstart EN Placed Order = 0 sinds flowstart

## v4 · Sunset · kept (`sunsetkept`, utm_campaign `v4-sunset-kept`)

- **Trigger**: Clicked Email · triggerfilter: event.$flow equals Vhi3iH EN event.Bot Click equals False
- **Flowfilters**: niet in deze flow in de laatste 365 dagen
- **Herinstap**: geen grens (alleen via flowfilter)
- **Verwijst naar**: v4 · Cart abandonment, v4 · Checkout abandonment, v4 · Sunset
- 'Kept' zonder update-profile: segment 'v4 · Sunset · kept' = Clicked Email (Bot Click false) where $flow = v4 · Sunset, minstens 1 keer in de laatste 180 dagen. Keuze in S3: Clicked Email waarvan URL het pad bevat.
- Geen korting en geen coupon (06-sunset-kept, 4). Klik op S1 en S2 geeft één instap (flowfilter 365 dagen).
- Terugval als de triggerfilter $flow weigert: Campaign Name contains 'SUNSET · S'.

- ⏱ wacht 30 minuten
- ✉ **SUNSET-KEPT · S3** · **ONTBREEKT** `v4 · Sunset · kept · s3-kept` · "You're staying. Thank you." · afzender Benjamin at Siraat's Kitchen
  - filter: Placed Order = 0 sinds flowstart
- ⏱ wacht 4 dagen, tot 09:00
- ✉ **SUNSET-KEPT · S4** · **ONTBREEKT** `v4 · Sunset · kept · s4-kept` · "The pan we started with" · afzender Benjamin at Siraat's Kitchen
  - filter: Placed Order = 0 sinds flowstart EN Received Email ($flow = v4 · Checkout abandonment (SNwQWU)) = 0 in de laatste 3 dagen EN Received Email ($flow = v4 · Cart abandonment (UshtNX)) = 0 in de laatste 3 dagen

## v4 · UGC first egg (`ugc`, utm_campaign `v4-ugc`)

- **Trigger**: Delivered Shipment
- **Flowfilters**: Placed Order = 1 over all time EN Placed Order (Items contains-any KOOK_TITELS+SET_TITELS) > 0 over all time EN niet in deze flow over all time EN Placed Order (Items contains-any 12-pcs (backorder)) = 0 over all time
- **Herinstap**: geen grens (alleen via flowfilter)
- Backorder-uitsluiting gelezen uit XzHrez (12-delige set). Reply-to support@ (Gorgias-macro UGC15).

- ⏱ wacht 4 dagen, tot 09:00
- ✉ **U1** · `WxV8CQ` · "Show us your first egg?"
  - filter: Opened Ticket = 0 sinds flowstart EN Refunded Order = 0 in de laatste 30 dagen EN Fulfilled Order > 0 in de laatste 60 dagen

