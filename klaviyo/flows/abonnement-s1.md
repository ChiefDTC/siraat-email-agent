# v4 · Abonnement S1 (Loop, test 20%)

Flow WTY94m, LIVE sinds 30 okt 2026 (akkoord Floris). Gebouwd met `scripts/build_subscription_flow.py`.

- Trigger: Ordered Product (XT7f8Z), ProductID = 15483020443988 (Non-Toxic Dishwasher Sheets) EN $value = 0. In Shopify heeft deze regel verkoopplan "Every 28 days" (Loop). Losse kopers ($35) en herhaalorders ($20) vallen erbuiten.
- Profielfilter: nooit eerder in deze flow (één keer per persoon).
- 15 minuten wachten.
- Conditional split, JA-tak: S1 variant b (template VFX3XC), onderwerp "Your first pack of sheets is on us", Smart Sending uit, status draft. NEE-tak: niets (controlegroep).
- Split: random sample 20% (API-conditie `profile-sample`, percentage 20).

## Status
Split, mail en flow live gezet via de API op 30 okt 2026. Backup oude split: scratchpad s1-split-backup.json.

## Meten
Opzeggen voor de eerste afschrijving (dag 28), skips (uit Loop), Gorgias-tickets over charge/subscription, afmeldingen en spam. Na een week met normale afmeldingen naar 50/50.
