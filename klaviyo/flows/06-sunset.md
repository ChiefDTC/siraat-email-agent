# Sunset Flow (met echte suppressie)

Vervangt: EB | Sunset Flow | 5/15/25 (S7V4a7, zet alleen een property)

**Trigger:** Added to Segment: Sunset Segment (XY4NVp)  
**Trigger filters:** Segment aanpassen: opens met machine_open = false, 90 dagen geen klik, geen non-machine open, geen Active on Site, geen order  
**Profile filters:**
- Placed Order = 0 in the last 90 days

**Instellingen:**
- Smart sending AAN
- Laatste stap is 'Unsubscribe profile from email' (Klaviyo flow action), niet alleen een property
- Wie opent of klikt: property Re_engaged = true en exit

## Vertakking

```
Trigger: Added to Segment "Sunset Segment"
│
├─ S1  Should we keep emailing you?
├─ [5 dagen, 09:00]
│    └─ split: Opened or Clicked since start?
│         ├─ YES → property Re_engaged = true → exit
│         └─ NO  → S2  This is our last email
└─ [5 dagen]
     └─ split: Opened or Clicked since start?
          ├─ YES → property Re_engaged = true → exit
          └─ NO  → Unsubscribe profile from email marketing
```

## Berichten

| # | Bestand | Wanneer | Onderwerp | Preview | Incentive | Filter op bericht | Smart sending | Notities |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [s1-staying-or-going.html](../emails/06-sunset/s1-staying-or-going.html) | Direct | Should we keep emailing you? | One click keeps you on the list. No click and we stop. | Geen | Placed Order = 0 in last 90 days | AAN |  |
| 2 | [s2-last-email.html](../emails/06-sunset/s2-last-email.html) | 5 dagen, 09:00 | This is our last email | Unless you click, we'll stop here. | Geen | Opened Email = 0 AND Clicked Email = 0 since start | AAN | Daarna: niet geopend → unsubscribe. |
