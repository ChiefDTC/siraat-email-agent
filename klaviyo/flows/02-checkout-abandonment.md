# Checkout Abandonment (samengevoegd, A/B gift card vs 10%)

Vervangt: EB | DEC 25 | Checkout Abandonment (Y2TmNB) + Triple Pixel variant (Tsg2tV)

**Trigger:** Checkout Started (Shopify, RfMvni)  
**Trigger filters:** Geen  
**Profile filters:**
- Placed Order = 0 times since starting this flow
- Has not been in this flow in the last 7 days
- Received Email from flow 'Checkout Abandonment Triple Pixel' = 0 since start (of zet die flow uit)
- Email not contains test@example.com

**Instellingen:**
- Smart sending UIT op C1 en de sms, AAN op C2 tot C4
- Sms alleen bij SMS consent, quiet hours aan (21:00 tot 09:00 lokale tijd), Texas-segment uitsluiten
- Eén 50% random sample split direct na de trigger: tak A = $25 gift card, tak B = 10% code. Na 4 weken winnaar kiezen en de split verwijderen
- Geen geneste splits meer

## Vertakking

```
Trigger: Checkout Started (Shopify)
│
├─ [1 uur] ─ C1  You left something on the stove (cart, geen korting)
│
├─ Conditional split: SMS consent?
│    └─ YES → [1 uur] SMS-1  "Your cart is saved: {{ checkout_url }}"
│
└─ Random sample split 50%
     ├─ A (gift card)
     │    ├─ [1 dag, 09:00] ─ C2a  $25 is waiting in your account (GIFT25)
     │    ├─ [1 dag, 09:00] ─ C3   Still deciding? 100 days to try it
     │    └─ [1 dag, 09:00] ─ C4a  Your $25 expires tonight
     └─ B (10%)
          ├─ [1 dag, 09:00] ─ C2b  10% off to finish your order (CHECKOUT10)
          ├─ [1 dag, 09:00] ─ C3   Still deciding? 100 days to try it
          └─ [1 dag, 09:00] ─ C4b  Your 10% expires tonight
```

## Berichten

| # | Bestand | Wanneer | Onderwerp | Preview | Incentive | Filter op bericht | Smart sending | Notities |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [c1-left-on-the-stove.html](../emails/02-checkout-abandonment/c1-left-on-the-stove.html) | 1 uur na trigger | You left something on the stove | Your cart is saved. Free shipping, 100-day trial. | Geen (bewust: eerst de twijfelaars zonder korting laten converteren) | Placed Order = 0 since start | UIT |  |
| 2 | [c2a-25-in-your-account.html](../emails/02-checkout-abandonment/c2a-25-in-your-account.html) | 1 dag, 09:00 (tak A) | {{ first_name|default:'Hey' }}, there's $25 in your account | A $25 gift card toward your cart. Valid 72 hours. | GIFT25 uniek, $25 vast, min. $99, 72 uur | Placed Order = 0 since start | AAN | Test-tak A. |
| 3 | [c2b-10-off-to-finish.html](../emails/02-checkout-abandonment/c2b-10-off-to-finish.html) | 1 dag, 09:00 (tak B) | {{ first_name|default:'Hey' }}, 10% off to finish your order | Your cart plus 10% off. Valid 72 hours. | CHECKOUT10 uniek, 10%, 72 uur | Placed Order = 0 since start | AAN | Test-tak B. |
| 4 | [c3-still-deciding.html](../emails/02-checkout-abandonment/c3-still-deciding.html) | 1 dag, 09:00 (beide takken) | Still deciding? Here's what actually matters | 100 days to try it. Free returns. No coating to wear off. | Verwijst naar code van C2 | Placed Order = 0 since start | AAN |  |
| 5 | [c4a-25-expires-tonight.html](../emails/02-checkout-abandonment/c4a-25-expires-tonight.html) | 1 dag, 09:00 (tak A) | Your $25 expires tonight | After midnight the gift card is gone. | GIFT25 | Placed Order = 0 since start | AAN |  |
| 6 | [c4b-10-expires-tonight.html](../emails/02-checkout-abandonment/c4b-10-expires-tonight.html) | 1 dag, 09:00 (tak B) | Your 10% expires tonight | After midnight the code is gone. | CHECKOUT10 | Placed Order = 0 since start | AAN |  |

## Sms

- **SMS-1** (1 uur na C1, alleen met SMS consent): `Siraat's Kitchen: your cart is saved and ships free. Finish here: {{ event.extra.checkout_url }} Reply STOP to opt out.`
