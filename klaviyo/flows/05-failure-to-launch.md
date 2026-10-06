# Failure to launch (ingekort tot 3 mails)

Vervangt: EB | Failure to launch (T2SmtR, 10 mails, 105.835 verzendingen per maand)

**Trigger:** Added to List: Email List (Uw8eZG)  
**Trigger filters:** Geen  
**Profile filters:**
- Placed Order = 0 times since starting this flow
- Opened Email ≥ 1 in the last 14 days (alleen wie de welcome flow heeft geopend)

**Instellingen:**
- Eerste wachtstap 14 dagen (nu 30), daarna 3 mails in 7 dagen
- Smart sending AAN op alles
- Na de laatste mail: niet geopend → Update profile property FTL_unopened = true (input voor sunset)

## Vertakking

```
Trigger: Added to List "Email List"
│
└─ [14 dagen, 09:00]
    └─ Conditional split: Placed Order = 0 AND Opened Email ≥ 1 (last 14 d)?
         ├─ NO  → exit
         └─ YES
              ├─ F1  Titanium vs non-stick
              ├─ [3 dagen, 09:00] ─ F2  Care FAQ
              └─ [4 dagen, 09:00] ─ F3  What customers really think
                   └─ split: Opened Email = 0 since F1? → YES: property FTL_unopened = true
```

## Berichten

| # | Bestand | Wanneer | Onderwerp | Preview | Incentive | Filter op bericht | Smart sending | Notities |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [f1-titanium-vs-nonstick.html](../emails/05-failure-to-launch/f1-titanium-vs-nonstick.html) | 14 dagen na trigger, 09:00 | Us vs the pan in your drawer | Why titanium hits differently. | Geen | Placed Order = 0 since start | AAN |  |
| 2 | [f2-care-faq.html](../emails/05-failure-to-launch/f2-care-faq.html) | 3 dagen, 09:00 | Unlocking the non-stick effect | Stick-free every time, in three steps. | Geen | Placed Order = 0 since start | AAN |  |
| 3 | [f3-real-reviews.html](../emails/05-failure-to-launch/f3-real-reviews.html) | 4 dagen, 09:00 | What our customers really think | Real reviews inside. | Geen | Placed Order = 0 since start | AAN | Laatste mail. Daarna property-update voor sunset. |
