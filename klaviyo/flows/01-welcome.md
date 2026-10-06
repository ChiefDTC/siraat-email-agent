# Welcome Flow (nieuw)

Vervangt: EB | Welcome Flow | Updated 02.03.26 (SiaNLu)

**Trigger:** Added to List: Email List (Uw8eZG)  
**Trigger filters:** Geen  
**Profile filters:**
- Placed Order = 0 times since starting this flow (op elke mail)
- Email not contains test@example.com

**Instellingen:**
- Smart sending UIT op mail 1, AAN op mail 2 tot 5
- Re-entry: nooit (een profiel doorloopt de welcome flow eenmaal)
- Alle mails van send@siraatskitchen.com, reply-to support@

## Vertakking

```
Trigger: Added to List "Email List"
│
├─ [5 min] ─ W1  Welcome + 10% (HI10 uniek)
├─ [1 dag, 10:00] ─ W2  Note from Benjamin
├─ [2 dagen, 10:00] ─ W3  Why titanium, not coating
├─ [2 dagen, 10:00] ─ W4  100,000 kitchens (bestsellers)
├─ [2 dagen, 10:00] ─ W5  Your 10% expires tonight
│
└─ Conditional split: Placed Order > 0 since start?
     ├─ YES → exit (Post Purchase flow neemt over)
     └─ NO  → exit (Failure to launch pakt ze op dag 14 op)
```

## Berichten

| # | Bestand | Wanneer | Onderwerp | Preview | Incentive | Filter op bericht | Smart sending | Notities |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [w1-welcome-10.html](../emails/01-welcome/w1-welcome-10.html) | 5 min na trigger | {{ first_name|default:'Welcome' }}, here's your 10% off | One code, one cookware upgrade. Valid 7 days. | HI10 uniek, 10%, 7 dagen | Placed Order = 0 since start | UIT | Zet de code als tekst, niet alleen in een afbeelding (huidige fout). |
| 2 | [w2-note-from-benjamin.html](../emails/01-welcome/w2-note-from-benjamin.html) | 1 dag, 10:00 | A note from Benjamin | Why I started making pans out of titanium. | Geen | Placed Order = 0 since start | AAN |  |
| 3 | [w3-why-titanium.html](../emails/01-welcome/w3-why-titanium.html) | 2 dagen, 10:00 | Why food sticks (and why it won't on titanium) | The 3-step method that makes a titanium pan release like non-stick. | Verwijst naar HI10 | Placed Order = 0 since start | AAN |  |
| 4 | [w4-social-proof.html](../emails/01-welcome/w4-social-proof.html) | 2 dagen, 10:00 | What 100,000 kitchens figured out | The three pans people buy first. | Verwijst naar HI10 | Placed Order = 0 since start AND Opened Email ≥ 1 since start | AAN |  |
| 5 | [w5-expires-tonight.html](../emails/01-welcome/w5-expires-tonight.html) | 2 dagen, 10:00 | Your 10% ends tonight | After midnight the code stops working. | HI10 | Placed Order = 0 since start | AAN | Daarna conditional split op Placed Order; beide takken eindigen. |
