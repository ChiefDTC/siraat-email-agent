# Post Purchase (met holiday next-purchase gift card)

Vervangt: EB | Post Purchase Flow | 4/6/2026 (RL3TU6)

**Trigger:** Placed Order (Shopify, RSNxYV)  
**Trigger filters:** Geen  
**Profile filters:**
- Geen (iedere order)

**Instellingen:**
- Smart sending UIT (transactioneel karakter)
- 'On its way' hoort in de Pan Education / shipping flow op het event Shipment In Transit, niet op een vaste dag
- Holiday-tak: trigger filter op orderdatum tussen 20 nov en 31 dec (of gebruik een tijdelijke conditional split op 'Placed Order in last 1 day' tijdens die periode)

## Vertakking

```
Trigger: Placed Order
│
└─ Conditional split: Placed Order count > 1 (all time)?
     ├─ YES (repeat) ─ [2 min] ─ R1  Welcome back
     └─ NO (first order)
          ├─ [2 min] ─ P1  We've got your order
          ├─ [1 dag, 09:30] ─ P2  A note from Benjamin
          ├─ [2 dagen, 09:30] ─ P3  Get ready to cook (3-step method, 100-day trial)
          └─ Conditional split: order placed between 20 Nov and 31 Dec?
               ├─ NO  → exit
               └─ YES ─ [7 dagen] ─ P4  Your $25 for January (JAN25, 1 to 15 Jan)
                              (JAN50 voor orders > $400 via extra split)
```

## Berichten

| # | Bestand | Wanneer | Onderwerp | Preview | Incentive | Filter op bericht | Smart sending | Notities |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [p1-weve-got-your-order.html](../emails/07-post-purchase/p1-weve-got-your-order.html) | 2 min na order | We've got your order | Order {{ event.extra.order_number|default:'' }} is confirmed. Here's what happens next. | Geen | Geen | UIT | Order-items blok werkt met event.extra.line_items van Placed Order. |
| 2 | [p2-founder-note.html](../emails/07-post-purchase/p2-founder-note.html) | 1 dag, 09:30 | A note from Benjamin | Why your pan has dents in it. | Geen | Geen | UIT |  |
| 3 | [p3-get-ready-to-cook.html](../emails/07-post-purchase/p3-get-ready-to-cook.html) | 2 dagen, 09:30 | Get ready to cook: the 3-step method | Heat, oil, food. In that order. | Geen | Geen | UIT |  |
| 4 | [p4-your-25-for-january.html](../emails/07-post-purchase/p4-your-25-for-january.html) | 7 dagen (alleen orders 20 nov tot 31 dec) | {{ first_name|default:'Hey' }}, we set aside $25 for you in January | A $25 gift card, valid 1 to 15 January. | JAN25 uniek, $25 vast, min. $99, geldig 1 tot 15 jan (JAN50 bij order > $400) | Placed Order between 20 Nov and 31 Dec | UIT | Campagne op 2 januari naar segment 'Holiday buyers zonder herhaalorder' als herinnering. |
| 5 | [r1-welcome-back.html](../emails/07-post-purchase/r1-welcome-back.html) | 2 min na order (repeat buyers) | Welcome back | Thank you for ordering again. | Geen | Placed Order count > 1 | UIT |  |

## Wijzigingen 28 okt 2026 (A/B Q4)

- Verzendfilter $0 (28 okt 2026, A/B Q4): elke mail heeft een extra conditiegroep "Placed Order met $value > 0, minstens 1 keer in de laatste N dagen" (N = wachttijd + buffer). TikTok-samples, seeding en gratis vervangingen krijgen zo geen mails; een betaalde order valt altijd binnen het venster. Details en terugdraaien: research/ab-tests-q4/07-uitgevoerd.md, exports/rollback/2026-10-28-abq4/.
- X3ySuU P2-SAFE (119850554): extra verzendfilters: geen mail met Campaign Name "P2-SAFE" in 30 dagen, geen mail uit VQ93sx in 30 dagen, geen mail uit het P2-vangnet R9dcdY in 30 dagen.
- VQ93sx P2 (119850581): extra filter "geen mail uit R9dcdY in 30 dagen" (dedupe met het vangnet).
- Nieuw, live: **R9dcdY** "v4 · P2 vangnet · Fulfilled +12d (geen Delivered)". Trigger Fulfilled Order (VtEiZT), 12 dagen tot 13:00, P2 · vangnet (template UJ4XeW, kopie van UKxRjv). Alleen pankopers (45 dagen), slaat over bij Delivered sinds de start, bij een VQ93sx-mail of P2-SAFE in 30 dagen. Herinstap 30 dagen. Reden: Delivered Shipment valt sinds ~22 okt grotendeels weg. Script: scripts/build_fallback_flows.py.
- T15 voorbereid: library-template TW2TUt (P1-FIRST met dekselkaart), start in de UI (research/ab-tests-q4/06-ui-stappen.md).
- Nog in de UI (Floris): triggerfilter $value > 0, herinstap 7 dagen, profielfilter 7 dagen.
