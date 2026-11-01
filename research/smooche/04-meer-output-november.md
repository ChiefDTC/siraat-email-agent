# Smooche · 04 · Meer e-mailoutput in november (1 nov 2026)

Vraag Floris: Smooche stuurde een testadres ongeveer 13 mails in ongeveer 36 uur. Wij willen in november (Black Friday-maand) ook veel meer output. Dit stuk zet hun tijdlijn naast de onze, kiest welke tactieken bij Siraat passen en geeft een plan met volumes, omzetschatting, risico's en een top 5 voor deze week.

Alleen gelezen. Niets gewijzigd in Klaviyo, Shopify of Gmail. Bronnen:
- Gmail-thread "lukje" (1 nov, 13 Smooche-mails als .eml-bijlage). De inhoud van alle 13 mails was leesbaar (de thread toont de tekst van de bijlagen). Verzendtijden: de headers waren niet zichtbaar, maar elke Klaviyo-afmeldlink bevat een token met een tijdstempel; die komen tot op enkele minuten overeen met de ontvangsttijden die Floris liet zien. Persoonlijke gegevens (adres, bedrag van het "krediet", kortingscode) staan hier bewust niet in.
- Klaviyo TdtTzz (GET, `flow-values-reports`, `metric-aggregates`): flowdefinities van T4a5Mk, Rn556d, QUBUQV, TZG9Mx, WdRz5k, QNZyEb, VLGhbR, T2SmtR, TbYQmX, YyaMjx; Received Email, Marked Email as Spam en Unsubscribed per dag (18 tot 31 okt) en per maand (oktober); omzet per flow en per mail (2 okt tot 1 nov); campagnes en segmentgroottes.
- research/smooche/01 tot 03, klaviyo/templates/v3/bfcm/ (README, PLAN, signup/FLOW.md), DECISIONS.md (Black Friday 2026), LOG.md.

---

## 0. Kort

- Smooche: 13 mails in 41 uur na de aanmelding, 6 op de drukste dag, 5 binnen 3 uur. Cart en checkout samen: 3 mails in de eerste 90 minuten en dezelfde 3 precies 24 uur later.
- Siraat voor exact dezelfde reis (aanmelden, kijken, winkelwagen, checkout, niet kopen): 3 mails uit flows in 41 uur (W1, C1, C2) plus hooguit 1 campagne. Wie in de 25%-BF-groep van Rn556d zit, krijgt na BF-W1 **niets meer uit de welcome**: de exit-split in T4a5Mk haalt hem eruit. Dat is het grootste gat en het makkelijkst te dichten.
- Het geld zit in de eerste uren: checkout C1 $7,96 per ontvanger, cart K1 $3,59, welcome W1 $2,74. Een tweede contact op dag 0 is bij ons nergens aanwezig, terwijl Smooche daar zijn volume stapelt.
- Grens: onze flows staan al op 0,118% spamklachten (oktober, door Klaviyo gemeten), de welcome op 0,157%. Google wil onder 0,1% en nooit 0,3%. Meer volume dus alleen met vangrails (sectie 5).

---

## 1. Smooche-tijdlijn (gemeten)

Aanmelding: 30 okt rond 23:27 UTC (eerste mail 23:28). Tijden in UTC, uren na de aanmelding.

| # | UTC | Uur | Afzender | Onderwerp | Wat | Scenario |
|---|---|---|---|---|---|---|
| 1 | 30 okt 23:28 | 0,0 | Smooche | You joined at the right time 👻 | Welkom, beeldmail, up to 60% off | Aanmelding |
| 2 | 30 okt 23:58 | 0,5 | Chloe from Smooche | Found your new make-up? | Browse/site, platte brief, "sale ends tonight at midnight" | Browse |
| 3 | 31 okt 01:29 | 2,0 | Chloe from Smooche | No tricks, just a treat | Welkom 2, platte brief, "already applied", "low on stock" | Aanmelding |
| 4 | 31 okt 12:57 | 13,5 | Smooche | Happy Halloween 🎃 | "Store credit" (kortingscode met minimum), "expires today" | Aanmelding (krediet) |
| 5 | 31 okt 14:41 | 15,2 | Chloe from Smooche | Still want your foundation? | Cart, platte brief, "I read these myself" | Cart/checkout |
| 6 | 31 okt 15:42 | 16,3 | Smooche | Foundation that adapts to you | Product, "3 reasons", beeldmail | Cart/checkout (afgeleid) |
| 7 | 31 okt 15:56 | 16,5 | Chloe from Smooche | Your order is pending. | "Pending order", gratis verzending, "canceled within 24 hours" | Checkout |
| 8 | 1 nov 01:30 | 26,0 | Smooche | What the right foundation actually does | Educatie + reviews | Aanmelding |
| 9 | 1 nov 13:57 | 38,5 | Chloe from Smooche | (1) Your store credit is updated. | "Krediet verlengd met 24 uur", "cannot be extended again" | Aanmelding (krediet) |
| 10 | 1 nov 14:42 | 39,2 | Chloe from Smooche | Your foundation order is pending. | Checkout 2, "go back to my cart" | Cart/checkout |
| 11 | 1 nov 15:43 | 40,3 | Smooche | A photo of me went viral for the wrong reason | "Klantverhaal" als brief van "Jen", 60% off | Cart/checkout (afgeleid) |
| 12 | 1 nov 15:57 | 40,5 | Chloe from Smooche | #1 Korean Foundation is waiting for you. | Checkoutlink, beeldmail, 58% off | Cart/checkout |
| 13 | 1 nov 16:46 | 41,3 | Smooche | Your [bedrag] is about to disappear | Krediet, aftelklok (countdownmail.com), "final hours" | Aanmelding (krediet) |

Patroon:
- De cart/checkout-reeks loopt in blokken van drie: 14:41, 15:42, 15:56 op 31 okt en 14:42, 15:43, 15:57 op 1 nov, precies 24 uur later. De winkelwagen werd dus rond 14:30 UTC op 31 okt gestart. Stappen: +10 min, +1 uur, +1 u 15, +24 u, +25 u, +25 u 15. Mail 6 en 11 rekenen we daarom tot deze reeks (niet bevestigd).
- Welkomstreeks: 0 u, +2 u, +26 u (ook 24 uur uit elkaar).
- Kredietreeks: dag 0 middag "expires today", dag 1 "verlengd", dag 1 avond aftelklok.
- Floris stuurde de thread na 41,5 uur door; wat daarna kwam, zien we niet.

## 2. Tijdlijn naast elkaar (aantal mails per venster na de trigger)

Siraat: uit de flowdefinities (wachttijden, splits, overslaanfilters). Lokale vaste tijden (bijv. "1 dag tot 10:00") vallen afhankelijk van het uur van de trigger in een ander venster; de tabel geeft het gewone geval (trigger 's middags of 's avonds lokaal).

| Scenario | Smooche 0-6 u | 6-24 u | 24-72 u* | Siraat 0-6 u | 6-24 u | 24-72 u | Siraat-mails (wachttijd) |
|---|---|---|---|---|---|---|---|
| Aanmelding, gewone welcome (75%) | 2 | 1 | 3 | 1 | 1 | 1 | W1 +5 min (gemeten 6,5), W2 volgende dag 10:00, W3 2 dagen later 09:00 |
| Aanmelding, BF-groep Rn556d (25%) | 2 | 1 | 3 | 1 | 0 | 0 | BF-W1 direct, daarna exit uit welcome |
| Browse | 1 | 0 | 0 | 1 | 0 | 1 | B1 +1 uur, B2 2 dagen later 09:00 (33 tot 57 u) |
| Cart | 3** | 0 | 3** | 1 | 0 | 1 à 2 | K1 +15 min, K2 2 dagen later 08:00, K3 1 dag later 08:00 |
| Checkout | (zie cart) | | | 1 | 1 | 1 | C1 +10 min, C2 volgende dag 08:30, C3 2 dagen later 09:00 |
| Site | (zie browse) | | | 1 | 0 | 1 | S1 +2 uur, S2 2 dagen later 09:00 |
| **Hele reis zoals Floris (aanmelden, kijken, cart, checkout)** | **6** (in 2 u) | **4** | **3+** | **2** | **1** | **1** | W1, C1; B1 en K1 vallen weg (exit bij cart/checkout), W2/W3 overgeslagen door de abandonment-mail, dan C2, C3 |

\* Smooche gemeten tot 41,5 uur. \*\* Cart en checkout als één reeks.

Plus campagnes: Homestead stuurde 14 tot 31 okt 6 grote verzendingen (20, 23, 25, 27, 31 okt en 1 nov), ongeveer één per 2 à 3 dagen om 08:15 lokale tijd, vooral naar "HS // Engaged 90 Days" (92.039 profielen), "All buyers" (101.435) en op 1 nov de volledige US- (80.569) en INT-lijst (78.859). Een nieuwe aanmelder krijgt in de eerste 72 uur dus 1 à 2 campagnes.

### Huidig volume per abonnee

| | Mails |
|---|---|
| Flows, 18 tot 31 okt | ~9.500 per dag (welcome ~3.000, Failure to launch ~2.700, sunset ~1.100, cart ~430, browse ~350, checkout ~220) |
| Campagnes, 18 tot 31 okt | 344.000 in 14 dagen (~24.600 per dag gemiddeld, pieken 65.000 tot 93.000) |
| Campagnes, 2 tot 17 okt | 12 van de 16 dagen een verzending, tot 187.000 per dag (hele lijst) |
| Betrokken abonnee (Engaged 90d), eind okt | ~0,3 campagne per dag plus flows |
| Nieuwe aanmelder, eerste 72 uur | 3 à 4 mails (1 à 1,3 per dag); BF-groep 1 à 2 |
| Smooche-testadres | 13 in 41 uur (~7,6 per dag) |

Opvallend: Failure to launch (T2SmtR, 30 dagen na aanmelding, 10 mails waarvan 4 live) is goed voor 37.000 mails in 14 dagen en levert $0,03 per ontvanger. Sunset idem ($0,03). Dat is volume zonder omzet dat wel meetelt voor spam en reputatie.

## 3. Wat het oplevert: onze omzet per ontvanger (2 okt tot 1 nov)

| Flow | Ontvangers | Orders | Omzet | Per ontv. | Afmeld | Spam |
|---|---|---|---|---|---|---|
| Welcome T4a5Mk | 55.533 | 211 | $60.595 | $1,09 | 1,57% | 0,157% |
| · W1 | 13.121 | 130 | $35.921 | **$2,74** | 1,86% | 0,137% |
| · W2 | 8.970 | 19 | $4.828 | $0,54 | 1,65% | 0,223% |
| · W3 | 7.763 | 11 | $1.839 | $0,24 | 1,26% | 0,232% |
| Checkout QUBUQV | 5.347 | 86 | $24.607 | $4,60 | 1,23% | 0,094% |
| · C1 (+10 min) | 2.017 | 55 | $16.049 | **$7,96** | 1,04% | 0,099% |
| · C2 (dag 1) | 947 | 13 | $3.193 | $3,37 | 1,80% | 0,106% |
| Cart TZG9Mx | 8.749 | 71 | $19.179 | $2,19 | 1,10% | 0,057% |
| · K1 (+15 min) | 3.076 | 38 | $11.033 | **$3,59** | 0,72% | 0,098% |
| · K2 (dag 2) | 2.166 | 9 | $2.050 | $0,95 | 1,11% | 0,092% |
| Browse WdRz5k | 8.632 | 36 | $6.644 | $0,77 | 0,58% | 0,023% |
| Site VLGhbR | 3.370 | 6 | $1.823 | $0,54 | 0,62% | 0% |
| Post-purchase X3ySuU | 6.574 | 36 | $6.542 | $1,00 | 0,41% | 0,015% |
| Failure to launch T2SmtR | 93.492 | 16 | $3.074 | $0,03 | 0,50% | 0,043% |
| Rn556d (BF-W1, sinds 31 okt 22:00) | 121 | 1 | $144 | | 0,83% | 2 klachten |

Campagnes oktober: 1,56 miljoen mails, $143.882 toegeschreven (635 orders), **$0,092 per mail**; afmelding ~0,6% per mail, spam 0,050%. Flows oktober: 268.000 mails, $162.955, $0,61 per mail, spam 0,118%.

Les: elke mail in de eerste uren na een trigger is 10 tot 80 keer zoveel waard als een campagnemail. Extra volume eerst daar, dan pas in campagnes.

## 4. Tactieken van Smooche: wat past bij Siraat

| Tactiek | Smooche | Past? | Eerlijke Siraat-versie |
|---|---|---|---|
| Korte wachttijden, 3 mails in 90 min | cart/checkout +10 min, +1 u, +1 u 15 | **Ja** | C1b op +1 uur, K1b op +3 uur, browse 1 u naar 30 min, site 2 u naar 1 u |
| Herhaling na precies 24 uur | zelfde 3 mails een dag later | Ja, deels | C2 en K2 op +23 à 24 uur in plaats van vaste ochtendtijd; tweede dag-0-mail in welcome (W1b +3 u) |
| Persoonlijke afzender "Chloe from" | 7 van 13 mails | **Ja, met Benjamin** | "Benjamin from Siraat" (al in Rn556d) op platte brieven, binnen vaste header en footer; alleen dingen laten zeggen die waar zijn; reply naar gelezen inbox ("Reply and our team will help.") |
| Platte brief zonder logo | Chloe-mails | Alleen met akkoord | Merkregel: vaste header en footer. Brief-stijl kan binnen header en footer (zoals W2). Uitzondering alleen als Floris die geeft (zoals affiliate en Mystery) |
| Oprichtersverhaal | via "Jen" (verzonnen klant?) | **Ja** | Benjamin zelf (W2 "The pan nobody else was making") als campagne-brief; klantverhaal alleen van een echte Trustpilot-reviewer, letterlijk, met toestemming. Geen verzonnen personen |
| Educatie | "What the right foundation actually does" | **Ja** | "What a pure titanium cooking surface actually does", care-tips, vergelijking (PFAS-pan, staal) uit comparisons.md |
| Feestdagmails | Halloween-thema | **Ja** | Thanksgiving (26 nov: "What to cook it in"), Black Friday 27 nov, Small Business Saturday 28 nov, Cyber Monday 30 nov. Alleen echte aanbiedingen |
| "Store credit" met aftelklok en "verlenging" | kortingscode verpakt als tegoed, "we added it yesterday", "extended once" | **Nee zoals het is** | Wel: unieke Klaviyo-code (`{% coupon_code %}`) met echte vervaldatum van 48 uur in abandonment-mails ("Your extra 10%, one use, valid until Sunday 11:59 PM"), aftelklok alleen tot die echte vervaltijd. Geen nep-tegoed, geen nep-verlenging. Echte Shopify store credit kan alleen voor klanten met account en alleen als we het echt boeken |
| "Your order is pending, canceled in 24 h" | er is geen order | **Nee** | "Your Black Friday cart is saved" / "Your checkout is still open". Geen order suggereren die niet bestaat |
| "Low on stock", "ends tonight, no extensions" | terwijl de sale doorloopt | **Nee** | Alleen echte einddatum (BF-einde nog van Floris) en echte voorraad. Let op: 12-delige set staat op 0 bij ShipBob met 604 zendingen OnHold; die niet extra pushen |
| Beeldmail met veel kortingslabels | 58%, 60% | Ja (BF-stijl bestaat) | "Up to 70% off" (niet "70% off everything"), BF-blokken uit v3/bfcm |
| "Want fewer emails? Click here" | in elke Chloe-mail | **Ja, als vangrail** | Regel boven de footer in november: "Too much this month? Get one email a week instead." naar voorkeurenpagina (vraagt een voorkeur-eigenschap) |

## 5. Risico's en vangrails

| Risico | Nu | Vangrail |
|---|---|---|
| Spamklachten (Gmail/Yahoo-regels: onder 0,1%, nooit 0,3%) | flows 0,118%, welcome 0,157%, W2/W3 0,22%, Rn556d 2 klachten in de eerste dag | Stopregel: nieuwe stap of campagne boven 0,15% (vanaf 1.000 ontvangers) terug naar vorige stand; account-dag boven 0,1% twee dagen achter elkaar: campagnes alleen nog naar 30 dagen-kliker. Google Postmaster Tools voor het verzenddomein checken (Klaviyo ziet Gmail-klachten niet per mail) |
| Afmeldingen | campagnes ~0,6% per mail, welcome 1,6 à 1,9% | Nieuwe stap boven 1,5% afmelding na 1.000 ontvangers: inkorten of uitzetten. Founder-brief-vorm (lager in afmelding dan zware beeldmail is te testen) |
| Te veel per persoon | flows hebben smart sending uit | Extra stappen (W1b, C1b, K1b) krijgen filter "minder dan 3 Received Email in de laatste dag". Campagnes: smart sending aan (16 uur), in BF-week 8 uur; maximaal 3 mails per 24 uur per profiel, 4 op BF en CM |
| Overlap welcome en abandonment | welcome slaat over bij abandonment-mail laatste dag (werkt) | Zelfde regel op W1b en BF-stappen; W1b ook overslaan bij Started Checkout in de laatste 3 uur |
| Niet-betrokken volume schaadt reputatie | Failure to launch en sunset ~3.800 per dag, $0,03 per ontvanger | Failure to launch in november op pauze (de 30-dagenaanmelders krijgen al BF-campagnes); extra campagnes alleen naar betrokken segmenten |
| Gmail/Yahoo-afzenderregels | Klaviyo zet one-click unsubscribe | SPF, DKIM, DMARC-alignment controleren; afmelding binnen 2 dagen verwerken (Klaviyo direct); volume stapsgewijs opvoeren (week 1 +25%, niet in één keer verdubbelen) |
| BFCODE werkt niet zoals de mails zeggen | actief sinds 1 nov 12:22 UTC, combineert met niets, terwijl er automatische kortingen lopen | Eerst combinaties fixen (product + verzending aan), dan pas extra mails die BFCODE noemen |
| Misleiding (FTC, EU richtlijn oneerlijke handelspraktijken) | | Geen nep-order, nep-tegoed, nep-schaarste, nep-deadline; "Up to 70% off" alleen als het klopt tegen de echte eerdere prijs (EU: laagste prijs 30 dagen) |
| BF-A/B in Rn556d is scheef | BF-groep $36,29 per aanmelding, controle $40,22 (1 nov 13:46) | Verschil komt deels doordat de BF-groep W2/W3 mist; na de fix opnieuw meten |

## 6. Plan november (op volgorde)

Aannames voor de schatting: aanmeldingen nu ~1.000 tot 1.500 per dag (964 in 15,8 uur op 31 okt/1 nov), abandonment-volumes zoals oktober plus 20% voor BF-verkeer, ~85% van de ontvangers heeft na de eerste mail nog niet gekocht. Omzet per ontvanger voor een nieuwe stap = voorzichtig gekozen tussen de bestaande stappen ervoor en erna. Dit zijn schattingen; elke nieuwe stap krijgt waar mogelijk een holdout van 20% zodat we de echte extra omzet zien.

| # | Wijziging | Extra mails per dag | Omzetschatting november (~28 dagen) | Basis |
|---|---|---|---|---|
| 1 | **BF-groep Rn556d weer de welcome laten volgen**: exit-split 119850651 zo aanpassen dat BF-W1-ontvangers alleen W1 overslaan en W2 (dag 1) en W3 (dag 3) krijgen. Of de BF-reeks uit WjAc2q (bf-w1b, bf-w2, bf-w3, templates bestaan) achter BF-W1 hangen | 450 à 650 | $4.000 à $6.000 | 215 à 315 BF-niet-kopers per dag x (W2 $0,54 + W3 $0,24) |
| 2 | **Checkout C1b op +1 uur**: korte brief van Benjamin binnen header/footer, "Your Black Friday cart is saved", BFCODE-link, één knop | 70 à 85 | $4.000 à $5.000 | $2,00 per ontvanger (C2 haalt $3,37, C1 $7,96) |
| 3 | **Welcome W1b op +3 uur** voor niet-kopers (gewone en BF-groep): "Your Black Friday prices are ready", 3 productkaarten (template bf-w1b), holdout 20% | 650 à 1.000 | $5.000 à $12.000 | $0,30 à $0,45 per ontvanger, tussen W1 ($2,74) en W2 ($0,54) |
| 4 | **Cart K1b op +3 uur** en K2 naar de volgende ochtend (nu dag 2) | 90 à 110 | $2.000 à $3.000 | K1b $0,90 (zoals K2) |
| 5 | **Browse 1 uur naar 30 min, site 2 uur naar 1 uur** (geen extra mails) | 0 | $400 à $1.200 | +5 à 15% op $8.500 per maand |
| 6 | **Echte deadline-mails**: zodra Floris de BF-einddatum geeft, "Last day" en "Final hours" als campagne naar betrokken 60 dagen plus abandoners, en een laatste stap in de BF-flows (bf-last bestaat). Aftelklok alleen tot het echte einde | 2 verzendingen | $10.000 à $20.000 netto | 2 x ~75.000 x 2 à 3 keer de normale $0,092, min 30 à 50% vervroegde aankopen |
| 7 | **Meer campagnes, per segment**: 30 dagen-betrokken (~60.000) van 3 naar 5 per week; 31 tot 90 dagen 3 per week; 90 tot 180 dagen alleen BF-start en laatste dag. BF-week (23 nov tot 1 dec) dagelijks naar 60 dagen-betrokken, op BF en CM twee keer naar 30 dagen-klikkers. Elke week één brief van Benjamin en één educatie- of klantverhaalmail | ~17.000 gemiddeld, BF-week ~60.000 | $25.000 à $35.000 | +2 verzendingen per week x 60.000 x $0,065 (70% van $0,092 door verzadiging) plus BF-week |
| 8 | **Unieke vervallende code in abandonment** in plaats van vaste BFCODE (48 uur, echte aftelklok) | 0 | $3.000 à $8.000 | +10 à 20% op checkout + cart ($43.800 in okt); vraagt Shopify-kortingsopzet |
| 9 | Failure to launch en sunset in november op pauze of alleen kliker-180d | -3.000 à -3.800 | -$1.500 | ruimte in reputatie voor 1 tot 7 |

Totaal flows (1 tot 5): ~1.300 tot 1.850 extra mails per dag, ruwweg $15.000 tot $27.000 extra in november. Campagnes en deadlines (6 tot 8): $38.000 tot $63.000, maar onzekerder. Ter vergelijking: flows en campagnes samen brachten in oktober $306.800.

Wat het voor één nieuwe aanmelder betekent (zelfde reis als Floris, geen aankoop): nu 3 à 4 mails in 41 uur, na het plan 6 à 8 (W1/BF-W1, W1b, C1, C1b, C2, campagne, W2 als de abandonment-reeks is afgelopen). Bewust onder Smooche (13): wij hebben een spamkussen van bijna nul.

### Voorbeelden van copy (Engels, nog niet ter goedkeuring)

- C1b, afzender "Benjamin from Siraat": subject "Your Black Friday cart is saved", preview "Your extra 10% is still on it." Body: "Benjamin here. Your cart is still open, at Black Friday prices. Your extra 10% is applied through the button below. Every pan comes with 30-day returns and a 75-year warranty. Reply and our team will help." Knop "Complete my order".
- W1b: subject "Your Black Friday prices are ready", preview "Up to 70% off. No code needed."
- Klantverhaal (campagne): alleen een echte Trustpilot-review letterlijk, bijv. in de vorm van W5 "Tammy is on her fourth pan".
- Fewer-emails-regel: "Too much this month? Get one email a week instead."

## 7. Top 5 deze week

| # | Wat | Moeite | Akkoord Floris nodig |
|---|---|---|---|
| 1 | Gat BF-groep dichten: Rn556d-ontvangers krijgen W2 en W3 (exit-split T4a5Mk aanpassen) plus W1b. Backup vooraf, controle op dubbele W1 | 1 à 2 uur | Ja (live flow) |
| 2 | Checkout C1b (+1 u) en cart K1b (+3 u) als Benjamin-brief binnen header/footer, US/INT via macro's, filter max 3 mails per dag, qa_render groen. Tegelijk browse 30 min en site 1 uur | 1 dag | Ja (live flows en copy) |
| 3 | Welcome W1b (+3 u) op basis van bf-w1b, met holdout 20% en skip bij Started Checkout | 0,5 dag | Ja |
| 4 | Novemberkalender met Homestead: frequentie per segment (sectie 6 punt 7), wekelijkse Benjamin-brief, feestdagen, uitsluitingen; BF-einddatum vastleggen voor echte deadline-mails | 2 à 3 uur plan, afstemming Homestead | Ja (en Homestead) |
| 5 | Vangrails: dagelijkse spam- en afmeldcheck per nieuwe mail in de flowbewaking (#claude-mail) met de stopregels uit sectie 5, Postmaster Tools en DMARC checken, BFCODE-combinaties laten fixen | 1 à 2 uur | Monitoring nee; BFCODE in Shopify en Failure to launch pauzeren ja |

Daarna: unieke vervallende code in abandonment (punt 8), voorkeurenpagina "one email a week", Failure to launch pauzeren.

## 8. Open vragen voor Floris

1. Einddatum en -tijd van de Black Friday-sale (nodig voor punt 6 en bf-last).
2. Akkoord op "Benjamin from Siraat" als afzender van C1b, K1b en W1b, binnen vaste header en footer?
3. Unieke 48-uurscodes in abandonment in plaats van vaste BFCODE: ja of nee?
4. Mag Failure to launch in november op pauze?
5. Homestead: wie bouwt de extra campagnes, en mogen wij segmenten (30, 60, 90 dagen) aanleveren?
