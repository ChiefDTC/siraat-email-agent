# S1 abonnementsmail: meer opzeggingen of afmeldingen? (2 nov 2026)

Vraag Floris: zorgt de S1-mail (flow WTY94m, "S1 skip-tip (b)", onderwerp "Your first pack of sheets is on us") ervoor dat mensen hun sheets-abonnement opzeggen of zich afmelden? Alleen gelezen, niets gewijzigd in Klaviyo, Shopify of Gorgias. Alleen aggregaten.

## Opzet en groepen

- Flow WTY94m live sinds 30 okt 2026 11:47 UTC. Trigger Ordered Product, ProductID 15483020443988 EN $value 0; profielfilter eenmalig; 15 min wachten; split `profile-sample` 20%; JA-tak S1 (message VDW3P7, template Rs5ebw), NEE-tak niets.
- Periode: 30 okt 11:47 tot 2 nov ~02:00 UTC (ongeveer 2,5 dag).
- Instroom: 585 triggerevents, 573 unieke profielen.
- S1-groep: 114 profielen met Received Email van WTY94m (19,9%, klopt met 20%). Controle: 459 profielen zonder S1.
- Timing: S1 komt mediaan 16 min na de order (min 15, max ~17 u, de uitschieter wacht op verzendvenster).
- Toestemming is vergelijkbaar: S1 102 subscribed / 7 never / 5 nu uitgeschreven; controle 409 / 36 / 14.

## Bronnen en beperking

- Shopify `subscriptionContracts` (ook via `customer.subscriptionContracts`): **Access denied**. De Shopify-koppeling heeft geen leesrecht op abonnementscontracten van Loop. Echte status (actief, gepauzeerd, opgezegd, skip) is dus niet te tellen.
- Klaviyo heeft geen Loop-events (alleen oude Recharge-metrics). Geen skip- of cancel-event beschikbaar.
- Eerste echte afschrijving ($20) valt pas rond 27 nov; nu meten we dus alleen vroege opzegverzoeken.
- Vervangende maat: Gorgias-tickets (zoekwoorden subscription, cancel, dishwasher sheets, skip; sinds go-live), gematcht op e-mail met de groepen, en per ticket de intentie (veld 227095) en zo nodig de eerste klantmail gelezen. Wie zelf in de Loop-portal opzegt zonder ticket, zien we niet.

## Resultaten per groep

| Maat | S1 (n=114) | Controle (n=459) | p (Fisher, tweezijdig) |
|---|---|---|---|
| Opzegverzoek abonnement via Gorgias | 3 (2,6%) | 3 (0,65%) | 0,10 |
| Personen met opzeg-ticket (abonnement of hele order), na S1 / na order | 6 (5,3%) | 8 (1,7%) | 0,04 |
| waarvan hele order annuleren (pan e.d.) | 3 | 5 | |
| Cancelled Order (Shopify, in Klaviyo) | 1 | 1 | |
| Afmeldingen na instroom | 5 (4,4%) | 7 (1,5%) | 0,07 |
| waarvan door de S1-mail | 0 | n.v.t. | |
| Spam na instroom | 1 (via BF-campagne, niet S1) | 0 | |

Opmerkingen:
- Geen enkele afmelding of spammelding komt van de S1-mail (message_id per afmelding gecontroleerd). Alle afmeldingen in beide groepen komen van post-purchase X3ySuU ("Good call. Here's what's coming."), de e-guide-mail XtYsPr of de BF-campagne van 1 nov. Het verschil 4,4% tegen 1,5% is dus niet door S1 veroorzaakt; bij n=114 is dit ruis (4 extra personen).
- Eén S1-ticket (hele order annuleren) kwam binnen voor de S1-mail en telt niet mee.
- De 3 abonnement-opzeggers in S1: 1 schreef 31 min na S1 los "ik heb dit niet besteld, zeg elk abonnement op"; 2 antwoordden direct op de S1-mail met een opzegverzoek (na 21 min en na ~21 u).
- De 3 opzeggers in controle reageerden op de Loop-startmail ("your subscription has started") of via het contactformulier, met dezelfde toon ("wist niet dat ik me aanmeldde").

## Klikken

- 10 unieke klikkers (Klaviyo-dashboard toonde 9 op het moment van kijken), 19 klikken, **alle** op de CTA naar de Loop-portal (`/a/loop_subscriptions/customer?utm_content=s1-cta1`).
- 2 van de 10 klikkers dienden kort daarna via Gorgias een opzegverzoek in: één klikte 4 keer in 4 minuten op de portallink en mailde 3 minuten later "cancel"; de ander mailde 3 minuten na de klik. Dat wijst op frictie in de portal (inloggen per e-mailcode) en niet op een voorkeur voor skippen.
- Geen enkele klikker heeft een Cancelled Order. Skips kunnen we niet zien (geen Loop-data).

## Conclusie

- **Afmeldingen: nee.** S1 gaf 0 afmeldingen en 0 spam. Het verschil tussen de groepen komt van andere mails.
- **Opzeggingen: mogelijk licht meer, niet aangetoond.** Opzegverzoeken voor het abonnement 2,6% (3/114) tegen 0,65% (3/459), p=0,10. Dat zijn ruwweg 2 extra mensen; de verhouding (4x) rust op 3 tegen 3 gevallen, dus niet significant en met een zeer breed interval. Wel aannemelijk: S1 maakt het abonnement zichtbaar en mensen die het niet bewust kozen, zeggen eerder op. Dat is opzeggen voor de eerste afschrijving, wat chargebacks en boze tickets rond dag 28 kan schelen.
- De echte toets (behoud na de eerste afschrijving van 27 nov, skips) kan pas als Loop-data beschikbaar is.

## Aanbeveling

1. **Houden op 20%, niet uitbreiden** tot ~27 nov plus een week: dan is er afschrijvings- en chargebackdata per groep. Nu uitbreiden zou een eventueel negatief effect vergroten zonder bewijs; stoppen is ook niet nodig, want afmeldingen en spam zijn 0.
2. **Data regelen**: Loop-integratie met Klaviyo koppelen (events subscription cancelled / skipped / charged) of de Shopify-app scope `read_own_subscription_contracts` geven. Zonder dat blijft deze test op Gorgias-tickets leunen.
3. **Copy en portal**: 2 van 10 klikkers mailden direct daarna om op te zeggen. Controleer of de portallink zonder gedoe inlogt; overweeg in de copy expliciet "skip of pauzeer in 2 klikken" met een directe link (persoonlijke Loop-link via de integratie).
4. **Kern ligt niet bij S1**: in beide groepen zijn de opzeggers mensen die niet wisten dat ze een abonnement hadden. Checkout-opt-in en Loop-startmail duidelijker maken heeft meer effect dan S1 aanpassen.
5. Volgende meting: 30 nov (na eerste afschrijving), per groep: opzeg, skip, mislukte betaling, chargeback.
