# Gift Card flows en december-campagnes

Vervangt: EB - E-Gift Card (UYALJ8, 1 transactionele mail)

**Trigger:** Flow A: Placed Order where Items contains 'E-Gift Card'. Campagnes: engaged 90 dagen, 15 tot 24 december  
**Trigger filters:** Flow A: Ordered Product ProductID = 12245272494420  
**Profile filters:**
- Flow A: geen

**Instellingen:**
- Flow A is transactioneel (G1) plus één marketingmail (G2) met smart sending AAN
- Campagnes GC1 tot GC3: audience Engaged 90 Days, exclusies Unengaged 180, Sunset, For Suppression, bought in last 7 days
- Shopify stuurt de gift card zelf naar de ontvanger; Klaviyo mailt alleen de koper

## Vertakking

```
Flow A: Placed Order with E-Gift Card
│
├─ [2 min] ─ G1  Thanks for gifting Siraat's Kitchen (hoe het werkt)
└─ [14 dagen, 09:00] ─ G2  Has it been opened yet? (herinnering + pan-tips om door te sturen)

Campagnes (geen flow):
├─ 15 dec ─ GC1  Too late to ship? A gift card arrives in a minute
├─ 20 dec ─ GC2  The gift that arrives today (last ship date voorbij)
└─ 23 dec ─ GC3  Christmas Eve: still time for a Siraat gift card
```

## Berichten

| # | Bestand | Wanneer | Onderwerp | Preview | Incentive | Filter op bericht | Smart sending | Notities |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [g1-thanks-for-gifting.html](../emails/09-gift-card/g1-thanks-for-gifting.html) | 2 min na order (transactioneel) | Thanks for gifting Siraat's Kitchen | Here's how your gift card works. | Geen | Geen | UIT (transactioneel) |  |
| 2 | [g2-opened-yet.html](../emails/09-gift-card/g2-opened-yet.html) | 14 dagen, 09:00 | Has your gift been opened yet? | A gentle reminder, plus the pan most people choose. | Geen | Geen (Klaviyo ziet verzilvering niet) | AAN | 'Resend' linkt naar het account; Shopify kan een gift card opnieuw mailen vanuit de admin. |
| 3 | [gc1-too-late-to-ship.html](../emails/09-gift-card/gc1-too-late-to-ship.html) | Campagne 15 dec | Too late to ship? A gift card arrives in a minute | $25 to $200, delivered by email, never expires. | Geen | Engaged 90 Days, excl. bought in last 7 days | AAN | Voeg een $150-variant toe met de framing 'Gift a pan'. |
| 4 | [gc2-arrives-today.html](../emails/09-gift-card/gc2-arrives-today.html) | Campagne 20 dec | The gift that arrives today | Last ship date has passed. This one is instant. | Geen | Engaged 90 Days, excl. bought gift card in last 7 days | AAN |  |
| 5 | [gc3-christmas-eve.html](../emails/09-gift-card/gc3-christmas-eve.html) | Campagne 23 dec | Christmas Eve plan: a Siraat gift card | Delivered by email in a minute. Schedule it for the morning. | Geen | Engaged 30 Days | AAN | Korte mail, mobiel eerst. |
