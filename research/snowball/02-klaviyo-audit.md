# Social Snowball · Klaviyo-audit (21 okt 2026)

Alleen lezen. Niets aangepast in Klaviyo of Shopify, niets verstuurd. Account TdtTzz, stand 21 okt ca. 22:00 UTC. Alle cijfers zijn totalen; profielgegevens staan alleen in de scratchpad van de sessie, niet in deze repo.

## Kort

- Social Snowball is op **20 okt om 14:40 UTC** gekoppeld. Er zijn 17 metrics bijgekomen (integratie "Social Snowball").
- **437 affiliates** (438 events, 1 dubbel), **allemaal via "Enrolled in SocialSnowball through purchase"**: elke koper wordt automatisch affiliate. 0 via aanmelding, handmatig, CSV, marketplace of Shopify-import (die metrics hebben alleen testevents van Snowball zelf).
- Van de 437: ca. **258 realtime** (inschrijving binnen 24 uur na de order, mediaan 32 minuten) en ca. **178 met terugwerkende kracht** voor orders van 13 tot 19 okt (98 daarvan uit orders van 17 okt). Batch van 96 inschrijvingen op 21 okt rond 05:00 UTC.
- **Nog geen echte referral sale, commissie $0.** Het enige "New referral sale"- en "Payout sent"-event is een sample-event van Snowball (Conversion ID `sample-entity`). In de 302 orders sinds de koppeling komt geen enkele affiliatecode voor.
- Instellingen zichtbaar op het profiel: **commissie 20%**, **vriendenkorting 10%**, programma "Default program", codetype "tracking link", valuta "$", status Active.
- De 6 conceptflows zijn **ongewijzigde Snowball-standaardsjablonen**: placeholders ("LOGO PLACE", stockfoto's, "(your brand)", "(product)"), verzonnen social proof ("She earned $300", Amazon- en Starbucks-cadeaubonnen), geen Siraat-header of -footer, geen Siraat-merk. Niet live zetten in deze vorm.
- Overlap: alle affiliates zijn kopers van de laatste 9 dagen; 420 van de 437 kunnen e-mailmarketing ontvangen. In de laatste 7 dagen kregen ze gemiddeld 2,5 mails (mediaan 2, max 9).

## 1. Social Snowball-metrics

Alle 17 aangemaakt op 20 okt 14:40 UTC, integratie "Social Snowball".

| Metric-id | Naam | Events 20 okt | Events 21 okt | Profielen | Wat erin zit |
| --- | --- | --- | --- | --- | --- |
| XzrVJZ | Enrolled in SocialSnowball through purchase | 142 | 296 | 437 | Echte data. Alleen `$event_id` |
| R2KsjG | Pending affiliate application | 1 | 1 | 1 (test) | Alleen `$event_id` |
| WWqT8n | Approved affiliate application | 1 | 1 | 1 (test) | Alleen `$event_id` |
| UBBdkE | Rejected affiliate application | 1 | 1 | 1 (test) | Alleen `$event_id` |
| SJy5uM | Signed up as an affiliate via sign up form | 1 | 1 | 1 (test) | Alleen `$event_id` |
| TYAaJ3 | Signed up as an affiliate via manual upload | 1 | 1 | 1 (test) | Alleen `$event_id` |
| VGnMT8 | Signed up as an affiliate via manual creation | 1 | 1 | 1 (test) | Alleen `$event_id` |
| TTWUnD | Signed up as an affiliate via marketplace | 1 | 1 | 1 (test) | Alleen `$event_id` |
| WjpQvK | Signed up as an affiliate via Shopify customers import | 1 | 1 | 1 (test) | Alleen `$event_id` |
| TPjE3f | Discount code changed | 1 | 1 | 1 (test) | Alleen `$event_id` |
| UYJuV7 | Affiliate changed program | 1 | 1 | 1 (test) | Alleen `$event_id` |
| TciBqC | Welcome Gift Claimed | 1 | 1 | 1 (test) | Alleen `$event_id` |
| V5mKgv | New Instagram Post added by affiliate | 1 | 1 | 1 (test) | `Link` (sample: socialsnowball.io) |
| VBKxxJ | New Instagram Story added by affiliate | 1 | 1 | 1 (test) | `Link` |
| Y3ctEQ | New Instagram Reel added by affiliate | 1 | 1 | 1 (test) | `Link` |
| Xqbr4d | New referral sale | 1 | 0 | 1 (test) | `Social Snowball - Conversion ID` (`sample-entity`), `$value` (sample 77.61) |
| WManrA | Payout sent | 1 | 0 | 1 (test) | `Social Snowball - Conversion ID` (`sample-entity`) |

Het "test"-profiel is een voorbeeldprofiel op het domein van Social Snowball zelf, met code `SAMPLECODE`. De testevents zijn op 20 okt 14:40 en opnieuw op 21 okt 21:29 UTC verstuurd (vermoedelijk "send test events" in het Snowball-dashboard).

**Belangrijk: de events zelf dragen bijna geen data.** Alles staat als **profieleigenschap** op de affiliate. Sleutels en waarden (geen persoonsgegevens):

| Profieleigenschap | Waarde bij alle 437 | Opmerking |
| --- | --- | --- |
| `Referral Reward - SocialSnowball` | `20%` | Commissie voor de affiliate |
| `Referral Friend Offer - SocialSnowball` | `10%` | Korting voor de vriend |
| `Referral Code - SocialSnowball` | per persoon | Vorm: voornaam (3 tot 8 letters) + 5 cijfers, bv. `ABCDE12345`; bij 423 van de 437 zit de voornaam erin |
| `Referral Link - SocialSnowball` | per persoon | Vorm: `https://www.siraatskitchen.com/<CODE>` (pad op de eigen site; niet getest, de site was vanuit deze sessie niet bereikbaar) |
| `Referral Code Type - SocialSnowball` | `tracking link` | Link past de unieke kortingscode automatisch toe |
| `Referral Currency - SocialSnowball` | `$` | Ook voor niet-US kopers |
| `Program - Social Snowball` | `Default program` | Eén programma |
| `Social Snowball - Affiliate Status` | `Active` | |
| `Social Snowball - Affiliate's most recent welcome gift status` | `None` | Geen welkomstcadeau ingesteld |
| `Gift card code - Social Snowball` | `GIFTCARD` | Placeholder, nog geen echte cadeaubon |
| `Affiliate First Name`, `Affiliate Last Name` | per persoon | Persoonsgegevens, niet overgenomen |
| `Social Snowball: Affiliate Order Value`, `Social Snowball: Payout amount` | alleen op testprofiel | Sample $85.30 en $19.90 |
| `Program - Social Snowball - Pending` / `- Rejected` | alleen op testprofiel | |

## 2. Affiliates: aantal, bron, verkopen

- **437 unieke profielen** met een inschrijvingsevent (Floris noemde ~438: dat is het aantal events, een profiel is twee keer ingeschreven).
- **Bron: 100% post-purchase-inschrijving** (XzrVJZ). Geen enkele echte inschrijving via aanmeldformulier, handmatig, CSV, marketplace of Shopify-import.
- **Timing**:
  - ca. 258 binnen 24 uur na hun order (1 binnen 5 minuten, 238 tussen 5 en 60 minuten, 18 tussen 1 en 24 uur);
  - ca. 178 met terugwerkende kracht, orders van 13 okt (1), 14 okt (11), 15 okt (6), 16 okt (16), 17 okt (98), 18 okt (34), 19 okt (12);
  - 1 zonder Placed Order sinds 1 sept.
- Ter vergelijking: sinds de koppeling (20 okt 14:00 UTC) zijn er 302 Placed Order-events. Vrijwel elke koper wordt dus automatisch affiliate.
- **Referral sales: 0.** Commissie totaal: $0. Geen enkele affiliatecode in de kortingscodes van de 302 orders sinds de koppeling (de codes die wel voorkomen zijn FREE SAMPLE, HI10, influencer- en seedingcodes).

## 3. De 6 conceptflows

Alle 6: status **draft**, gekloond op 20 okt tussen 14:49 en 14:58 UTC (16:49 tot 16:58 NL-tijd). Gemeenschappelijk voor alle berichten:

- Afzender **"SiraatsKitchen" (send-adres op siraatskitchen.com)**, geen reply-to. De live Siraat-flows gebruiken "Siraat's Kitchen" met reply-to naar het supportadres.
- Smart sending uit, niet transactioneel, geen UTM-parameters, geen extra filters, geen flowfilter.
- Templates zijn Snowball-voorbeeldsjablonen (namen als `WelcomeEmail#1_Safelinks`, gemaakt sept 2026, en twee uit 2022/2023). **Geen Siraat-header of -footer, geen lockup-logo, geen Siraat-kleuren of -typografie.** De afbeeldingen zijn placeholders: een grijs "afbeelding"-icoon, een rode banner met "LOGO PLACE", stockfoto's (drie mannen in pak op een trap, een polshorloge). Sociale iconen (Facebook, Instagram, Twitter) zonder link.
- Dashboardknop gaat naar de **algemene** Snowball-pagina (`affiliates.socialsnowball.io/auth/affiliate/signup` of `/login`), niet naar een Siraat-portal.
- Ondertekend met `{{ organization.name }}`, niet met Benjamin.

HTML van alle 14 templates staat in de scratchpad (`snowball/templates/<flow>_<bericht>_<template>.html`).

### 3.1 Xszb66 · "Social Snowball - Post purchase_Safelinks (clone)"

Trigger: **Enrolled in SocialSnowball through purchase** (XzrVJZ), dus elke koper.

| Stap | Inhoud |
| --- | --- |
| Wacht 10 minuten | |
| Mail 1 (RsgtW2, template TeGmsv) | Onderwerp "You can make money promoting our products! 💸", preview "Welcome to our affiliate program" |
| Wacht 2 dagen | |
| Split: heeft ooit een "New referral sale" (Xqbr4d)? | Ja: stop. Nee: door |
| Mail 2 (TGsTnk, VuSLSP) | "Following up on your new position" / "Want to earn some extra cash?" |
| Wacht 3 dagen | |
| Split: zelfde als boven | |
| Mail 3 (WzEmrh, Yn6eVL) | "She earned $300 by referring friends to (your brand)!" / "Looking for a way to share your love for (your brand)?" |

Copy:
- **Mail 1**: "Great news! Your affiliate account is officially set up." Referral-link (`Referral Link`), commissie (`Referral Reward`, dus "Earn 20% per successful referral"), knop "View Your Affiliate Dashboard".
- **Mail 2**: "You were recently invited to our affiliate program, so I wanted to follow up." Zelfde link en commissie, knop naar het dashboard.
- **Mail 3**: "Someone just made $300 from their referrals 👀". Verzonnen voorbeelden ("$150 in cash, $110 in Amazon gift cards, $75 in Starbucks gift cards"), stappenplan "Record a video with your (product)", vriendenkorting (`Referral Friend Offer`, dus 10%), link, dashboardknop. Stockfoto van drie mannen in pak.

Problemen: drie extra mails in 5 dagen voor **elke** koper, bovenop de bevestiging en de E-Guide; mail 1 komt 10 minuten na inschrijving, dus vaak vóór of rond de orderbevestiging van X3ySuU (1 uur). "(your brand)" en "(product)" letterlijk in onderwerp en tekst. Claims over verdiensten die niet waar zijn. Toon ("your new position", "earn extra cash") past niet bij Siraat.

### 3.2 VdsfMx · "Social Snowball - Approved Affiliate Application_Safelinks (clone)"

Trigger: **Approved affiliate application** (WWqT8n). Structuur: wacht 1 minuut, mail 1 "Welcome aboard!" / "Your affiliate account is waiting", wacht 1 dag, split op referral sale, mail 2 "Following up on your new position", wacht 2 dagen, split, mail 3 "She earned $300 by referring friends to (your brand)!".
Mail 1 voegt toe: "Your referral link automatically generates and applies a unique discount code whenever it's clicked." Mail 2 en 3 zijn tekstueel gelijk aan 3.1. Relevant alleen als er een aanmeldformulier met goedkeuring komt; nu 0 aanvragen.

### 3.3 YefepE · "Social Snowball - Manually Added Affiliates in SS Dashboard - Safelinks (clone)"

Trigger: **Signed up as an affiliate via manual creation** (VGnMT8). Zelfde structuur als 3.2 (1 minuut, 1 dag, 2 dagen). Mail 1 is tekstueel gelijk aan mail 1 van 3.1. Dashboardknop in mail 1 en 3 naar `/login`, mail 2 naar `/signup`. Nu 0 handmatige affiliates.

### 3.4 RZXgjW · "Social Snowball - Manually upload affiliates- CSV-Safelinks (clone)"

Trigger: **Signed up as an affiliate via manual upload** (TYAaJ3). Zelfde structuur als 3.2. Mail 1 is een **"we've made a change to our affiliate program"**-mail ("What's Changing? Seamless Tracking & Discounts: your referral link now automatically applies your unique discount code"). Bedoeld voor merken die van een ander programma overstappen; voor Siraat inhoudelijk onjuist (er was geen eerder programma). Nu 0 CSV-affiliates.

### 3.5 VnWwqJ · "4. Email - Template - Social Snowball - SF Affiliate notification of sale CLONE (clone)"

Trigger: **New referral sale** (Xqbr4d). Geen wachttijd, één mail: onderwerp "You've got money!💰", **geen preview-tekst**. Template "Transactional - Social Snowball emails" (2022): platte tekst. "Someone just made a purchase using your discount code, nice work! Purchase value: `Referral Currency` + `Social Snowball: Affiliate Order Value`. Your commission: `Referral Currency` + `Social Snowball: Payout amount`." Link "login to your portal here" naar `socialsnowball.io/login-form` (andere, oudere URL dan de rest). Let op: de bedragen komen van het **profiel**, niet van het event; bij twee sales kort na elkaar kan de mail het bedrag van de verkeerde sale tonen.

### 3.6 VdNKHq · "8. Email - Template - Social Snowball - Payout Sent (clone)"

Trigger: **Payout sent** (WManrA). Geen wachttijd, één mail: onderwerp "Payout sent", **geen preview-tekst**. Template heet "Post-purchase - Thank you" (2023). "You have been paid! for your referrals. You've received `Social Snowball: Payout amount`, here is your gift card: `Gift card code - Social Snowball`. Share your discount code `Referral Code` with your friends and earn more `Referral Currency`" (de laatste zin eindigt op het valutateken, dus "earn more $"). Navigatie SHOP / ABOUT / NEW / CONTACT en knop SHOP NOW linken naar **`www.klaviyo.com`** of nergens heen. Placeholderbanner en stockfoto. Gaat uit van uitbetaling in cadeaubonnen; de gift card-eigenschap staat nu op `GIFTCARD` (placeholder).

### Samenvatting problemen (alle 6)

1. Geen Siraat-header/footer en geen lockup-logo (schendt de vaste merkregel), placeholderafbeeldingen.
2. Placeholders in onderwerp en tekst: "(your brand)", "(product)".
3. Verzonnen verdiensten en cadeaubonnen (mail 3), niet toegestaan als claim.
4. Afzender "SiraatsKitchen" zonder reply-to; niet Benjamin, niet "Siraat's Kitchen".
5. Dashboardlinks naar de algemene Snowball-site, payout-mail linkt naar klaviyo.com.
6. Twee mails zonder preview-tekst.
7. Mailvolume: de post-purchase-variant voegt 3 mails toe voor elke koper, zonder smart sending en zonder uitsluiting van mensen die net andere flows krijgen.
8. Referral-sale- en payout-mail lezen bedragen van het profiel in plaats van het event.

## 4. Korting en commissie

- **Zichtbaar in Klaviyo**: commissie **20%** per verwijzing (`Referral Reward`), vriendenkorting **10%** (`Referral Friend Offer`), codetype "tracking link" (de link zet een unieke code in de checkout), valuta "$" voor iedereen, één programma ("Default program"), geen welkomstcadeau, uitbetaling als cadeaubon wordt in het payout-sjabloon verondersteld maar de cadeaubon-eigenschap is nog een placeholder.
- **Niet zichtbaar** en dus uit het Snowball-dashboard te halen: of 20% over de orderwaarde vóór of na korting gaat, minimumbedrag, of de 10% stapelt met HI10 of andere codes, alleen nieuwe klanten of ook bestaande, uitbetaalwijze (cash, PayPal, cadeaubon, tegoed), wachttermijn tegen retouren (retour is 30 dagen), fraudecontrole (eigen code gebruiken), landen.
- Let op: 20% commissie plus 10% korting is fors hoger dan het eerdere ontwerp in `research/referral/01-ontwerp.md` ("Give $25, get $25", beloning pas na de retourtermijn).

## 5. Overlap en maildruk

Basis: 437 affiliates, events sinds 1 sept.

- **Recente kopers**: 436 van 437 hebben een Placed Order tussen 13 en 21 okt (1 zonder order sinds 1 sept). Het zijn dus allemaal kopers die midden in de post-purchase-reeks zitten.
- **Mails in de laatste 7 dagen** (Received Email): gemiddeld 2,5, mediaan 2, maximum 9.
  - Verdeling: 0 mails 26, 1 mail 13, 2 mails 263, 3 mails 52, 4 mails 50, 5 mails 17, 6 mails 7, 7 mails 6, 8 of meer 3.
  - 410 kregen minstens één flowmail, 70 minstens één campagne.
  - Flowmails: v4 · Post-purchase X3ySuU 397, FREE E-GUIDE YyaMjx 369, v4 · Welcome T4a5Mk 90, Cart abandonment 36, Checkout abandonment 27, Browse abandonment 19, Post-purchase · levering VQ93sx 11, Back in Stock 9, overige 10.
  - Campagnes: October Email 7 (cutting board) 48, October Email 13 (bundle push) 36, October Email 8 (dishwasher sheets) 36, review catch-up 2.
- **E-mailstatus**: 397 subscribed, 23 never subscribed, 11 unsubscribed, 6 onderdrukt (bounce of klacht). **420 kunnen e-mailmarketing ontvangen, 17 niet.** 8 hebben sinds 1 sept een "Unsubscribed from Email Marketing"-event.

Gevolg: een koper krijgt nu in het eerste uur al 2 mails (E-Guide na 3 minuten, bevestiging na 1 uur). De Snowball post-purchase-flow zou daar binnen 10 minuten een derde bij zetten en in de eerste 5 dagen nog twee.

## 6. Bestaande Siraat-flows op order en levering

Live flows per trigger (concepten niet meegeteld):

| Trigger | Flow | Wat er gebeurt |
| --- | --- | --- |
| Placed Order (RSNxYV) | **X3ySuU v4 · Post-purchase** | Filter: niet in deze flow in de laatste 30 dagen. 1 uur: bevestiging ("Good call. Here's what's coming." nieuw, "Good to see you again" terugkerend). +16 dagen: "When your pan arrives: the first egg". +4 dagen: splits naar cross-sell ("The pan your set is missing", "Which lid fits your pan?", "Now meet the pan", "An apron deserves a pan") of "How is the pan treating you?" |
| Placed Order | YyaMjx FREE E-GUIDE | 3 minuten: "Your E-Guide Is Ready" |
| Placed Order | UYALJ8 E-Gift Card, VTkxFL VIP, XbYT7T Anniversary, UyFc78 Winback, UEfh4h Winback (oud) | Niet relevant voor de eerste weken |
| Delivered Shipment, Shopify (VcUF33) | **VQ93sx v4 · Post-purchase · levering** | Filter: heeft besteld. +1 dag: "The mistake that makes titanium stick" (1 mail) |
| Delivered Shipment | VPixnJ v4 · UGC first egg | Alleen eerste koper. +4 dagen: "Show us your first egg?" |
| Delivered Shipment | **XzHrez Review request · Delivered +14d** | Eén keer per profiel. +14 dagen: A/B-test reviewverzoek |
| Fulfilled Order (VtEiZT) | **TvfJYU Review request · fallback Fulfilled +21d** | Eén keer per profiel, als er geen Delivered is. +21 dagen: "Win your purchase amount back" |
| Delivered (ShipBob), Postflows, Wonderment, Fulfilled Partial | geen live flows | |

Plekken voor een affiliate-uitnodiging **zonder extra verzending**:

1. **Blok in VQ93sx** (1 dag na levering): de koper heeft de pan net, de mail is kort en er is één bericht in die flow. Link en vriendenkorting via `{{ person|lookup:"Referral Link - SocialSnowball" }}` en `Referral Friend Offer`.
2. **Blok in "How is the pan treating you?"** (X3ySuU, ca. 20 dagen na order) of onder de bedankmail na een goede review (XzHrez/TvfJYU, +14 of +21 dagen): beste moment qua tevredenheid, en na de retourtermijn-start.
3. **Niet** in de bevestiging van X3ySuU of de E-Guide: de pan is er dan nog niet.

Advies: de Snowball post-purchase-flow (Xszb66) niet live zetten; de referral-link als blok in bestaande mails opnemen, met Siraat-header en -footer. De transactionele mails (referral sale, payout) wel nodig zodra er verkopen zijn, maar dan herschreven in Siraat-stijl en met bedragen uit het event.

## Bronnen

- Klaviyo API (revision 2025-10-15): `/api/metrics`, `/api/events` per metric en per profiel, `/api/profiles` met subscriptions, `/api/flows/{id}?additional-fields[flow]=definition`, `/api/flow-messages/{id}/template`, `/api/metrics/{id}/relationships/flow-triggers`.
- Ruwe data (alleen scratchpad, niet in repo): events, profielevents, abonnementsstatus, 14 template-HTML's, flowdefinities.
