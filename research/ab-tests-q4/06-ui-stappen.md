# A/B Q4 · 06 · Klikinstructies voor de UI (28 okt 2026)

Voor Floris. Alles hieronder kan niet via de API (nieuwe A/B op een gewone mail, splits, extra acties, triggerinstellingen). De templates staan klaar in de Klaviyo-bibliotheek, QA is gedaan (zie 07-uitgevoerd.md) en van elke nieuwe mail ging een testmail naar Floris ("[TEST] ..." op 28 okt rond 23:55 UTC).

Vaste instellingen voor elke A/B-test (PLAYBOOK 6):
- Verdeling 50/50.
- Winnaar op **unique clicks** (Klaviyo: "Winning metric: Click rate").
- **Automatische winnaar uit** ("Automatically end test and send winner": nee). Wij beslissen met de data, ook omzet per ontvanger.
- Variatienamen: `<mail> · <test>-A` en `<mail> · <test>-B`.
- Onderwerp en preview van B gelijk aan A, tenzij de test over het onderwerp gaat.
- Na het opslaan: "Start test" (anders loopt er niets) en de flow-actie zelf moet op Live staan.
- Laat het Claude weten zodra een test loopt. Claude controleert dan via de API de variaties, de templates en de filters.

Volgorde: begin met 1 tot en met 6. De tests 7 en 8 kosten het meeste klikwerk.

---

## 0. Eerst: post-purchase X3ySuU (Floris, ongeveer 10 minuten)

Niet via de API te doen. Dit hoort bij de reparaties.

1. Open flow **v4 · Post-purchase** (https://www.klaviyo.com/flow/X3ySuU/edit), klik op de **trigger** (Placed Order).
2. **Trigger filter**: Add filter > `$value` > is greater than > `0`. Opslaan. Dan houden TikTok-samples ($0, tag "Free sample", bron tiktok) geen herinstapvenster meer bezet. Sinds vanavond houdt ook een verzendfilter ze tegen, dus dit is extra.
3. **Re-entry criteria**: "Allow people to enter this flow multiple times" > **after 7 days** (nu 30).
4. **Profile filters**: "Has not been in this flow in the last 30 days" wordt **7 days**. Toont de UI de melding dat de herinstap dit overneemt, haal het filter dan weg. Blijft het op 30 staan, dan verandert er niets.
5. Opslaan. Klaar. Claude meet daarna P1-REPEAT per dag tegen de basislijn (05-herinstap, sectie 5.2).

---

## 1. T15 · P1-FIRST met dekselkaart (post-purchase X3ySuU)

| | |
|---|---|
| Flow / actie | X3ySuU, mail **P1-FIRST** (actie 119850551) |
| Klikken | Klik op P1-FIRST > **Create A/B test** |
| A | huidige P1-FIRST (template blijft zoals hij is) |
| B | Change template > Saved templates > **AB Q4 · T15-B · P1-FIRST dekselkaart** (TW2TUt). Onderwerp en preview gelijk aan A: "Good call. Here's what's coming." / "Order confirmed. Your 4 gifts, your e-book and the one tip that matters." |
| Wat verschilt | Alleen de dekselregel ("ONE SIZE NOTE") is in B een productkaart met foto en knop "Add the lid that fits my pan". Dezelfde voorwaarden: alleen bij een losse Pan Pro, niet als het deksel al in de order of in siraat_owned zit. Geen prijs op de kaart, omdat de dekselprijs met de sale wisselt |
| Verdeling | 50/50, winnaar unique clicks, automatisch uit |
| Hoe lang | Start nu, beslissen op 7 december (BFCM-dagen apart). Het affiliate-blok gaat niet in P1-FIRST zolang T15 loopt |

## 2. BR1 · TP · B1 met de saleprijs (browse Triple Pixel QNZyEb)

De WdRz5k-helft loopt al sinds 28 okt 23:41 UTC (via de API, variatie B van de oude T05a). Deze tweede helft zet de test ook in de TP-flow, zodat we gepoold kunnen beslissen.

| | |
|---|---|
| Flow / actie | QNZyEb, mail **TP · B1** (actie 121177227) |
| Klikken | Klik op TP · B1 > **Create A/B test** |
| A | huidige TP · B1 |
| B | Template **AB Q4 · BR1-B · TP B1 sale-prijs (QNZyEb)** (TgpB6X). Onderwerp **"Your pan, at the sale price"**, preview **"The sale price, plus an extra 10% with HI10. The lab report is inside."** |
| Wat verschilt | Onderwerp, preview, codebalk ("SALE PRICE + EXTRA 10% · CODE HI10") en de regel onder de prijs ("That's the sale price. HI10 takes an extra 10% off it, already applied with the button."). Verder byte-gelijk |
| Verdeling | 50/50, winnaar unique clicks, automatisch uit |
| Hoe lang | Tot 7 december, beslissen samen met de WdRz5k-helft op klik, omzet per ontvanger als richting |

## 3. T14 · C1-onderwerp (checkout QUBUQV)

| | |
|---|---|
| Flow / actie | QUBUQV, mail **C1** (actie 119850587) |
| Klikken | Klik op C1 > **Create A/B test** |
| A | "Your cart + 4 gifts are still pending" |
| B | **"Don't leave these hanging"**. Preview gelijk aan A: "They ship the moment you place the order. One tap left." Template gelijk aan A (niets wijzigen) |
| Verdeling | 50/50, winnaar unique clicks, automatisch uit |
| Hoe lang | Start nu, besluit in december (op de dagen buiten 20 nov tot 1 dec). Realistisch 6 weken |

## 4. T21 · K1 met HI10 al toegepast (cart TZG9Mx)

Let op: dit wijkt af van DECISIONS 8 okt ("geen HI10 in K1 en K2"). Het valt onder het akkoord van 28 okt ("alle testen starten"); daarom staat het als test, niet als wijziging.

| | |
|---|---|
| Flow / actie | TZG9Mx, mail **K1** (actie 119850627). Niet K1-ACC |
| Klikken | Klik op K1 > **Create A/B test** |
| A | huidige K1 |
| B | Template **AB Q4 · T21-B · K1 met HI10 toegepast** (W4XNNw). Onderwerp en preview gelijk aan A: "The hammered pattern: an easy wipe" / "Less food touches the metal, so cleanup is a quick wipe. Your cart is saved." |
| Wat verschilt | Codebalk "EXTRA 10% ALREADY APPLIED · CODE HI10" (A: "STILL PENDING ON YOUR CART · $70 IN GIFTS"), de regel onder de cart ("Your extra 10% is already applied with the button below.") en alle cartlinks via `/discount/HI10?redirect=/cart`. Hero, blokken en reviews gelijk |
| Verdeling | 50/50, winnaar unique clicks, automatisch uit |
| Hoe lang | Start nu, eerste lezing 20 nov, besluit december of januari (omzet per K1-ontvanger over de hele cartpad, na korting). K1 draagt maar één test: **T18 pas na dit besluit** |

## 5. T23 · K4 op dag 7 over betalen in termijnen (cart TZG9Mx, alleen US, 50% holdout)

K3 heeft zes eindpunten (pan: 119850644, 119850646, 119850647; accessoire: 119850637, 119850641, 119850642). Klaviyo kan paden niet samenvoegen, dus de stap komt onder elk van die zes.

Onder **elk** van de drie K3-pan-mails:
1. **+ Conditional split** > "Random sample" > **50%**. Noem hem "T23 holdout".
2. JA-tak: **Update profile property** `ab_k4` = `mail`. NEE-tak: **Update profile property** `ab_k4` = `control`, daarna niets.
3. JA-tak verder: **Time delay** **3 days**, "until" **09:00**, tijdzone profiel (K3-pan gaat op dag 4, dus K4 op dag 7).
4. **Trigger split**: `_ip_country_code` equals `US`. NEE-tak: niets.
5. JA-tak: **Email** > Saved templates > **AB Q4 · T23 · K4 termijnen (cart dag 7, US)** (WJB7C2).
   - Onderwerp **"Is the price what stopped you?"**, preview **"Shop Pay Installments and Affirm are at checkout. Your cart is still saved."**
   - Afzender "Siraat's Kitchen" <send@siraatskitchen.com>, reply-to support@siraatskitchen.com.
   - UTM campaign `v4-cart`. Smart sending uit.
   - Naam "K4 · termijnen (T23)".
6. Verzendfilters van de K4-mail (Additional filters): kopieer die van K3-pan (Checkout Started 0 since starting this flow, Placed Order 0 since starting this flow). Geen $0-filter nodig: dit is een cartflow.

Onder **elk** van de drie K3-acc-mails: hetzelfde, maar de wachttijd is **4 days** tot 09:00 (K3-acc gaat op dag 3).

Mail op **Live** zetten. Geen A/B-test-instelling nodig: het is een holdout (mail tegen geen mail). Meting: alle orders per profiel binnen 14 dagen na de split, op `ab_k4`. Looptijd tot begin december, besluit in december samen met T24.

## 6. T24 · C5 op dag 14 over betalen in termijnen (checkout QUBUQV, alleen US, 50% holdout)

C4 heeft drie eindpunten: 119850618 (cooldown), 119850620 (CODE · C4), 119850621 (nocode · T02-B). Onder **elk**:
1. **Conditional split** "Random sample" **50%**, naam "T24 holdout".
2. JA: **Update profile property** `ab_c5` = `mail`. NEE: `ab_c5` = `control`, daarna niets.
3. JA verder: **Time delay** **9 days** tot **09:00** (C4 gaat op dag 5, C5 dan op dag 14).
4. **Trigger split**: `$extra.presentment_currency` (in de UI: "extra presentment_currency") equals `USD`. NEE: niets.
5. JA: **Email** > Saved templates > **AB Q4 · T24 · C5 termijnen (checkout dag 14, US)** (VeFfkA).
   - Onderwerp **"Is the price what stopped you?"**, preview **"Shop Pay Installments and Affirm are at checkout. Your order is still saved."**
   - Afzender "Siraat's Kitchen", reply-to support@.
   - UTM campaign `v4-checkout`. Smart sending uit.
   - Naam "C5 · termijnen (T24)".
6. Verzendfilters: neem alle verzendfilters van CODE · C4 over (onder meer Placed Order 0 since starting this flow).

Mail op **Live**. Meting op `ab_c5`, besluit in december, gepoold met T23.

## 7. T22 · C2 na 48 uur in plaats van 24 uur (checkout QUBUQV)

De nieuwe arm loopt na C1 in één rechte lijn:

1. Wachttijd 119850595 (1 dag tot 08:30)
2. C2 en C2-ACC
3. Wachttijd 119850601 (2 dagen tot 09:00)
4. C3-S, C3-P en C3-ACC
5. Wachttijd 119850615 (2 dagen tot 09:00)
6. Split 119850617 (cooldown)
7. Split 119850619 (T02, 100% code)
8. De C4-mails

De keuze tussen C2 en C2-ACC, en tussen de C3-mails, maken de verzendfilters per mail.

1. Klik op de **lijn tussen C1 en de wachttijd 119850595** > **+ Conditional split** > "Random sample" **50%**. Naam: "T22 · C2 24u/48u".
2. **JA-tak (A, 24 uur)**: laat het bestaande pad eraan hangen. Zet bovenaan de JA-tak een **Update profile property** `ab_c2` = `24h`.
3. **NEE-tak (B, 48 uur)**:
   - **Update profile property** `ab_c2` = `48h`.
   - **Time delay 2 days** tot **09:00**, tijdzone profiel.
   - Daarna kopieën van het hele pad, in deze volgorde. Gebruik bij elke actie "Clone" en sleep de kloon naar de NEE-tak. Klonen nemen template, onderwerp en verzendfilters mee:
     - C2
     - C2-ACC
     - wachttijd 2 dagen tot 09:00
     - C3-S
     - C3-P
     - C3-ACC
     - wachttijd 2 dagen tot 09:00
     - de cooldown-split met zijn mail
     - de T02-split (op **100% code**, zoals nu)
     - CODE · C4 en C4 nocode · T02-B
   - Geef elke kloon de naam "<naam> · T22-B".
4. Controleer na het klonen dat elke kloon op **Live** staat en dezelfde verzendfilters heeft als het origineel. Klaviyo zet klonen soms op Draft.
5. Geen A/B-instelling. Meting op `ab_c2`:
   - Omzet per C1-ontvanger over C2 tot en met C4.
   - Afmeldingen per C1-ontvanger over het hele pad.
   - Doel: afmelding op C2 van 2,4% naar ongeveer 1,2%, zonder dat de omzet per ontvanger meer dan 10% daalt.
   - Looptijd tot begin december, besluit op 7 december.

Als T22 meer werk blijkt dan dit waard is: zet smart sending aan op C2 (één vinkje, actie 119850597). Dan is er geen meting.

## 8. T18 · K1-onderwerp (cart TZG9Mx), pas na het besluit over T21

| | |
|---|---|
| Flow / actie | TZG9Mx, K1 (119850627) |
| Wanneer | Na het besluit over T21 (december of januari). K1 draagt één test tegelijk |
| Klikken | K1 > Create A/B test (of, als T21 dan beslist is, de winnaar van T21 als A) |
| A | "The hammered pattern: an easy wipe" |
| B | **"{{ first_name\|default:'Hi' }}, we saved these for you"**, preview gelijk aan A, template gelijk aan A |
| Verdeling | 50/50, winnaar unique clicks, automatisch uit, minstens 4 weken |

---

## Wacht op Floris (niet gebouwd)

| Test / item | Wat ontbreekt |
|---|---|
| Q2 · W5 als vroege toegang tot Black Friday | Datum Black Friday-prijzen en of de vroege lijst echt een dag eerder kan (link, collectie of code) |
| BR3 · setaanbeveling in B2-NOTCLICKED | Blijft de 6-delige set in november $299 en "Buy 2, get 4 free"? |
| Winback met de sale als haak (UEfh4h mail 1 en 3, v4-winback R1) | Echte einddatum van Halloween 70% en de novembersale; "70% off" alleen met bevestigde reikwijdte |
| P3-salerij | Zelfde einddatums |
| Regel "Your 4 gifts end when the fall sale ends" in C1, C2 en cart | Klopt die na 31 okt nog? De gifts lopen in november door (DECISIONS 19 okt). Niet aangepast |
| Affiliate-blok in BFCM | Stapelt de Snowball-vriendenkorting (15%) op 70%? |
| BFCM-kopersreeks (3 concepten staan als Draft) | Reikwijdte en startdatum van de novembersale ("up to 70%" staat er nu), setprijs in november, Black Friday-aanbod, einddatum (geen "last chance" zonder echte einde). Holdoutlijst XN5G3M vullen op 12 nov (Claude, 15% random uit segment SpBxrC) |
| Oude banners en claims (winback, FTL) | Geen akkoord, niet uitgevoerd |
