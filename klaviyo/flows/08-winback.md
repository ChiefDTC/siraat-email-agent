# Customer Winback (met herhaalcheck)

Vervangt: EB | Customer Winback | 5/8/25 (UEfh4h)

**Trigger:** Placed Order (Shopify)  
**Trigger filters:** Geen  
**Profile filters:**
- Placed Order = 0 times in the last 60 days (gecontroleerd op elke mail, ontbreekt nu)
- Has not been in this flow in the last 90 days

**Instellingen:**
- Smart sending AAN
- Geen random sample split

## Vertakking

```
Trigger: Placed Order
│
└─ [60 dagen, 09:00]
    └─ split: Placed Order = 0 in last 60 days?
         ├─ NO  → exit
         └─ YES
              ├─ WB1  What's new since your last order
              ├─ [3 dagen, 09:00] ─ WB2  10% off your next pan (WINBACK10)
              └─ [2 dagen, 09:00] ─ WB3  10% expires tonight
```

## Berichten

| # | Bestand | Wanneer | Onderwerp | Preview | Incentive | Filter op bericht | Smart sending | Notities |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [wb1-whats-new.html](../emails/08-winback/wb1-whats-new.html) | 60 dagen na order, 09:00 | What's new since your last order | The pieces customers add second. | Geen | Placed Order = 0 in last 60 days | AAN |  |
| 2 | [wb2-winback10.html](../emails/08-winback/wb2-winback10.html) | 3 dagen, 09:00 | 10% off your next pan | A thank-you for being a customer. Valid 5 days. | WINBACK10 uniek, 10%, 5 dagen | Placed Order = 0 in last 60 days | AAN |  |
| 3 | [wb3-expires.html](../emails/08-winback/wb3-expires.html) | 2 dagen, 09:00 | Your 10% expires tonight | Last chance for the returning-customer code. | WINBACK10 | Placed Order = 0 in last 60 days AND Opened Email ≥ 1 since start | AAN |  |
