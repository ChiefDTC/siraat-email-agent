# Browse Abandonment (samengevoegd)

Vervangt: EB | DEC 25 | Browse Abandonment (Wj6x6V) + Triple Pixel variant (TyEjuQ)

**Trigger:** Viewed Product (Klaviyo onsite, XNtYMB)  
**Trigger filters:** Geen  
**Profile filters:**
- Added to Cart = 0, Checkout Started = 0, Placed Order = 0 since starting this flow
- Has not been in this flow in the last 7 days (beide varianten gelijk, nu 2 en 30 dagen)
- Received Email from flow 'Browse Abandonment Triple Pixel' = 0 in the last 7 days (of zet die flow uit)
- Received Email from flow 'Cart Abandonment' = 0 in the last 3 days

**Instellingen:**
- Smart sending UIT op B1, AAN op B2
- Afzender send@ (nu support@, inconsistent met de rest)

## Vertakking

```
Trigger: Viewed Product
│
├─ [2 uur] ─ B1  Still looking at {{ event.ProductName }}?
└─ Conditional split: Added to Cart since start?
     ├─ YES → exit (Cart flow neemt over)
     └─ NO  → [2 dagen, 09:00] ─ B2  What 100,000 cooks say
```

## Berichten

| # | Bestand | Wanneer | Onderwerp | Preview | Incentive | Filter op bericht | Smart sending | Notities |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [b1-still-looking.html](../emails/04-browse-abandonment/b1-still-looking.html) | 2 uur na trigger | Still looking at {{ event.ProductName|default:'this' }}? | Free shipping and 100 days to try it. | Geen | Added to Cart = 0, Checkout Started = 0, Placed Order = 0 since start | UIT |  |
| 2 | [b2-what-cooks-say.html](../emails/04-browse-abandonment/b2-what-cooks-say.html) | 2 dagen, 09:00 | What 100,000 cooks say about it | Real reviews, and the 100-day trial if they're wrong. | Geen | Added to Cart = 0 AND Placed Order = 0 since start | AAN | Geen korting in browse: de incentive bewaren voor cart en checkout. |

## Wijzigingen 28 okt 2026 (A/B Q4)

- WdRz5k: T05a gesloten met A. Variatie B (119850692) is nu **BR1-B**: onderwerp "Your pan, at the sale price", preview "The sale price, plus an extra 10% with HI10. The lab report is inside.", template Ye4tQy (kopie van library RDeehg: codebalk SALE PRICE + EXTRA 10%, aanbodbalk in de hero opnieuw geschilderd, prijsregel). Loopt sinds 28 okt 23:41 UTC.
- QNZyEb: TP · B2-NOTCLICKED (121177242) op **manual** (0,50% spam). BR1-B voor TP · B1 klaar als TgpB6X, start in de UI.
