# Welcome Flow v3 · spec (7 oktober 2026)

Figma: https://www.figma.com/design/j3idDGYnRZBAJ13T5aL5vj (pagina 01 flow, 02 mails oud vs nieuw, 03 content-inventaris).
Vervangt v2-spec (01-welcome-v2.md) na het lezen van Homestead's "Welcome Series Rebuild" (sept 2026, in `brand/`). Hun diagnose klopt en is overgenomen. Hun oplossing is aangepast op vijf punten.

## Wat we van Homestead overnemen
- Zeven "fix now"-punten voor de oude flow: sale-banner weg, kopersfilter, kapotte mail "Save 10%" uit, Shopify-links naar siraatskitchen.com, fallback 'there', "Free shipping on all orders", afzender "Siraat's Kitchen".
- Dag 0 en dag 1 dragen de omzet (75 procent). Platte oprichtersmail op dag 1.
- Bewijs in plaats van claims (Light Labs, vergelijkingstabel, echte reviews).
- Drie instapniveaus op budget (accessoire, pan, set).
- Iedereen krijgt elke mail tot hij koopt. Geen open-filters.
- Test: bestaande random split van 100 naar 50/50. A = oude mails met fixes, B = v3. Metric: omzet per nieuwe abonnee (nu €3,40, doel boven €3,88). Guardrail na 2 weken bij meer dan 20 procent achterstand. Winnaar na 4 weken.

## Wat we anders doen
1. Geen HI10. Welkomstkrediet als gift card: $25 op bestellingen vanaf $149, unieke code per profiel (Klaviyo unique coupon op een Shopify-korting met vast bedrag), 14 dagen geldig, niet stapelbaar. Bedrag en drempel beslist Floris.
2. Kopers krijgen een eigen pad (E0). Homestead's flow-filter gooit ze eruit.
3. Split op locatie voor E4: VS krijgt 12-delige set en USD-prijzen, niet-VS niet. VS is 64 procent van de orders, AU 13, CA 5, SG 4, UK 4.
4. Geen "non-stick" als kop (niet in de goedgekeurde claims). Wel "no coatings" en "pure titanium cooking surface".
5. Smart sending uit op alle mails. In plaats daarvan nieuwe leads 14 dagen uitsluiten van campagnes. SMS pas in fase 2.

## Structuur
```
Trigger: Added to list Uw8eZG. Filter: e-mail bevat niet test@, nooit in flow, herinstap nooit.
Split A: Placed Order > 0 ooit?
  JA  → 10 min → E0 You're in (and thank you) → einde
  NEE → 10 min → E1 You're in. One thing before you go. (A/B onderwerp)
        dag 1 10:00 → E2 Why I started Siraat's Kitchen (tekst, oprichter)
        dag 3 10:00 → E3 What's actually on your pan? (bewijs)
        dag 6 10:00 → Split B locatie = US?  → E4-US / E4-INT Three ways to start
        dag 9 10:00 → E5 In their words + gift card (A/B met/zonder gift card)
        dag 13 18:00 → Split C: geen order sinds start én geklikt? → E6 Your gift card expires tomorrow (tekst)
        dag 14 einde. Failure to launch uit; later 2 educatiemails dag 21 en 35.
Verzendfilter E1 t/m E6: Placed Order = 0 sinds flow-start.
```

## Copy
Staat volledig in Figma pagina 02 (live tekst). Register kalm. Claims alleen uit de goedgekeurde lijst. Reviews alleen geverifieerd (Marilyn B., Michael G., Jeanne K., Tammy, Kay S., Thomas H.).

## Open beslissingen (Floris)
1. Oprichtersnaam plus twee regels in eigen woorden.
2. Pop-up: belooft die een giveaway-lot, een code, of allebei? Verzamelt hij telefoonnummers?
3. Light Labs: publieke link of PDF.
4. Gift card: $25 of $30, drempel $149 of $199.
5. HI10 en COOKHAPPY uit alle flows en uit Shopify: ja of nee.
6. Levertijd 12-delige set (backorder).
7. Reply-to inbox voor de oprichtersmail.
8. Bedrijfsadres voor de footer.
9. Klantenaantal: 30.000 (oude mails) of 100K+ (guidelines).
10. Trustpilot-score tonen (nu 3,7) of weglaten.

## Bouwstappen
1. HTML-templates (live tekst Inter, koppen als TT Ramillas-afbeelding, hero 600 breed).
2. Shopify-korting vast bedrag + Klaviyo unique coupon.
3. Flow via API als draft naast de oude; 50/50-split in de oude flow.
4. Goedkeuring Floris, live, 2-weken-check, 4-weken-read.
