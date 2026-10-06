# Cart Abandonment (nieuw)

Vervangt: EB | Cart Abandonment | 2/03/26 (SwkMyn) + Triple Pixel variant (TBWngE)

**Trigger:** Added to Cart (Shopify, QXcV8K)  
**Trigger filters:** Geen  
**Profile filters:**
- Checkout Started = 0 times since starting this flow
- Placed Order = 0 times since starting this flow
- Has not been in this flow in the last 7 days
- Received Email from flow 'Checkout Abandonment' = 0 in the last 3 days

**Instellingen:**
- Smart sending UIT op K1, AAN op K2 tot K4
- Geen random sample split. Eén tak.
- first_name altijd met |default:'' (huidige mails tonen 'Hi ,')

## Vertakking

```
Trigger: Added to Cart (Shopify)
│
├─ [1 uur] ─ K1  We saved these for you (geen korting)
├─ [1 dag, 09:00] ─ K2  Questions before you decide? (trial, care)
├─ [1 dag, 09:00] ─ K3  Get cooking with 10% off (COOK10)
└─ [1 dag, 09:00] ─ K4  Last call for 10%
     (K3 en K4 alleen als Checkout Started = 0 in laatste 3 dagen)
```

## Berichten

| # | Bestand | Wanneer | Onderwerp | Preview | Incentive | Filter op bericht | Smart sending | Notities |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [k1-we-saved-these.html](../emails/03-cart-abandonment/k1-we-saved-these.html) | 1 uur na trigger | {{ first_name|default:'Hey' }}, we saved these for you | Your cart is waiting. Free shipping on every order. | Geen | Checkout Started = 0 AND Placed Order = 0 since start | UIT |  |
| 2 | [k2-questions.html](../emails/03-cart-abandonment/k2-questions.html) | 1 dag, 09:00 | Questions before you decide? | 100 days to try it. Here's how the first cook goes. | Geen | Checkout Started = 0 AND Placed Order = 0 since start | AAN |  |
| 3 | [k3-cook10.html](../emails/03-cart-abandonment/k3-cook10.html) | 1 dag, 09:00 | {{ first_name|default:'Hey' }}, get cooking with 10% off | Your cart plus 10% off, valid 48 hours. | COOK10 uniek, 10%, 48 uur | Checkout Started = 0 in last 3 days AND Placed Order = 0 since start | AAN |  |
| 4 | [k4-last-call.html](../emails/03-cart-abandonment/k4-last-call.html) | 1 dag, 09:00 | Last call for 10% off | Your code ends tonight. | COOK10 | Checkout Started = 0 in last 3 days AND Placed Order = 0 since start AND Opened Email ≥ 1 since start | AAN |  |
