# Flows-audit · Failure to launch (T2SmtR) in november: pauzeren? (1 nov 2026)

Vraag: moet "EB | Failure to launch" in november op pauze? Alleen gelezen via de Klaviyo-API (GET, `flow-values-reports`, `flow-series-reports`, `campaign-values-reports`, events en segmentlidmaatschap van een steekproef). **Niets aangepast.** Conversie = Placed Order (RSNxYV), Klaviyo-attributie.

## Advies in het kort

**Pauzeren: de 4 nog live mails op Draft zetten tot 1 december** (flow blijft Live, profielen lopen door zonder mail, er bouwt geen wachtrij op). Akkoord Floris nodig.

Waarom, in cijfers:
1. **Levert bijna niets op**: laatste 30 dagen 94.887 mails, 16 orders, $3.074, **$0,03 per ontvanger** (alle flows zonder FTL $0,88, campagnes $0,077). De 4 live mails: $0,05 per ontvanger.
2. **Blokkeert campagnes**: FTL stuurt om 08:00 lokaal, Homestead om 08:15 lokaal met smart sending aan. Wie een FTL-mail krijgt, wordt door de campagne overgeslagen. Steekproef 31 okt en 1 nov: op **66 van 66** dagen met een FTL-mail kreeg dat profiel **geen** campagne (Halloween E12 $0,14 per ontvanger, BF-launch E1). 94% van de FTL-ontvangers zit in "HS // Engaged 90 Days". Schatting november: ~11.000 campagnemails geblokkeerd, ongeveer evenveel omzet ($1.100 à $1.650) als FTL zelf toegeschreven krijgt ($1.250 à $1.900).
3. **Verkeerde claims**: alle 4 live templates hebben de banner "SIRAAT PRIME TIME SALE | UP TO 56% OFF", 3 noemen "100-DAY" (proefperiode; wij zeggen 30 dagen retour), 1 "Lifetime" (wij zeggen 75 jaar garantie). Dat botst met DECISIONS.md en met "up to 70% off" in november.
4. **Spam is níet het argument**: FTL zit met 0,042% (30 d) onder het flowgemiddelde. Uitzetten haalt ~5% van alle klachten weg, maar het flowpercentage stijgt juist (0,079% naar 0,098%) omdat FTL laag scoort. Zie sectie 4.

## 1. De flow

| Onderdeel | Waarde |
|---|---|
| Flow | T2SmtR "EB \| Failure to launch", Live, aangemaakt 29 sep 2025 |
| Trigger | Toegevoegd aan lijst Uw8eZG "Email List" (232.806 profielen, single opt-in) |
| Flowfilter | Placed Order 0 keer sinds start flow |
| Stap 1 | Wacht 30 dagen tot 08:00 (profieltijdzone) |
| Split 90675572 | Door als: geen order in de laatste 30 dagen **en** geen Received Email met Campaign Name "W2" in de laatste 60 dagen (sinds 8 okt, zodat de v4/v5-welcome geen FTL krijgt). Anders uit de flow |
| Mails | 10, waarvan **6 Draft sinds 28 okt 19:17 UTC** (akkoord Floris: Bestsellers + Product Reviews, Healthy Habits, FAQ's, Titanium Care, Ceramic VS Titanium, Review Focus) en **4 Live** |
| Timing live mails | dag 33 Titanium vs Non-Stick, dag 35 How to Store + Care, dag 36 Titanium Vs Stainless Steel, dag 37 Micro-Plastic Free; allemaal rond 08:00 lokaal (de eerste wachttijden eindigen om 08:00, de latere zijn hele dagen) |
| Smart sending | aan op alle mails |
| Afzender | SiraatsKitchen, send@siraatskitchen.com |

Instroom: tot 8 okt kreeg iedereen FTL; van 8 tot 19 okt alleen de oude welcome-arm (50%); sinds 19 okt (100% nieuwe welcome) vrijwel alleen nog wie W2 niet kreeg. Gevolg voor november: ~1.350 mails per dag tot ~10 nov, ~680 per dag tot ~25 nov, daarna ~250. **Schatting november: ~25.000 FTL-mails** (bandbreedte 20.000 tot 27.000).

Let op december: de BF-groep van Rn556d (25% van de aanmeldingen sinds 31 okt) krijgt na BF-W1 geen W2 en komt daardoor na 30 dagen wél in FTL (eerste FTL-mail rond 3 dec, met de oude Prime Time-banner). Vóór FTL weer aan gaat: de voorwaarde "W2" vervangen door "ooit een mail uit T4a5Mk of Rn556d ontvangen".

## 2. Per mail

### Laatste 30 dagen (2 okt tot 1 nov)

| Mail | Status | Ontvangers | Open | Klik | Orders | Omzet | Per ontv. | Afmeld | Spam | Bounce |
|---|---|---|---|---|---|---|---|---|---|---|
| Bestsellers + Product Reviews | Draft | 8.863 | 36,2% | 0,31% | 1 | $63 | $0,01 | 0,48% | 0,080% (7) | 0,89% |
| Healthy Habits Start Here | Draft | 8.973 | 34,8% | 0,28% | 0 | $0 | $0,00 | 0,51% | 0,067% (6) | 0,84% |
| FAQ's | Draft | 9.170 | 35,9% | 0,34% | 0 | $0 | $0,00 | 0,42% | 0,044% (4) | 0,58% |
| **Titanium vs Non-Stick** | Live | 10.841 | 34,9% | 0,34% | 4 | $1.016 | $0,09 | 0,48% | 0,056% (6) | 0,48% |
| **How to Store + Care** | Live | 10.760 | 33,7% | 0,32% | 2 | $282 | $0,03 | 0,56% | 0,019% (2) | 0,41% |
| **Titanium Vs Stainless Steel** | Live | 10.498 | 34,4% | 0,41% | 4 | $642 | $0,06 | 0,50% | 0,048% (5) | 0,49% |
| **Micro-Plastic Free** | Live | 10.134 | 34,5% | 0,23% | 1 | $161 | $0,02 | 0,44% | 0,020% (2) | 0,31% |
| Titanium Care | Draft | 8.745 | 35,6% | 0,37% | 3 | $666 | $0,08 | 0,53% | 0,046% (4) | 0,30% |
| Ceramic VS Titanium | Draft | 8.665 | 35,3% | 0,39% | 1 | $243 | $0,03 | 0,43% | 0,023% (2) | 0,31% |
| Review Focus | Draft | 8.238 | 35,4% | 0,29% | 0 | $0 | $0,00 | 0,66% | 0,024% (2) | 0,33% |
| **Totaal** | | **94.887** | 35,0% | 0,33% | **16** | **$3.074** | **$0,03** | 0,50% | **0,042% (40)** | 0,49% |
| waarvan 4 live | | 42.233 | | | 11 | $2.101 | $0,05 | | 0,036% (15) | |

Open- en klikpercentages op afgeleverde mails; open is opgeblazen door Apple Mail Privacy.

### Laatste 90 dagen (3 aug tot 1 nov)

| Mail | Ontvangers | Klik | Orders | Omzet | Per ontv. | Afmeld | Spam |
|---|---|---|---|---|---|---|---|
| Bestsellers + Product Reviews | 30.305 | 0,42% | 7 | $1.574 | $0,05 | 0,56% | 0,090% (27) |
| Healthy Habits Start Here | 28.650 | 0,34% | 2 | $214 | $0,01 | 0,52% | 0,056% (16) |
| FAQ's | 30.510 | 0,28% | 2 | $497 | $0,02 | 0,47% | 0,072% (22) |
| Titanium vs Non-Stick | 32.126 | 0,33% | 10 | $1.981 | $0,06 | 0,46% | 0,063% (20) |
| How to Store + Care | 31.471 | 0,38% | 8 | $1.752 | $0,06 | 0,51% | 0,054% (17) |
| Titanium Vs Stainless Steel | 31.153 | 0,45% | 8 | $1.264 | $0,04 | 0,41% | 0,084% (26) |
| Micro-Plastic Free | 30.427 | 0,24% | 7 | $1.083 | $0,04 | 0,40% | 0,066% (20) |
| Titanium Care | 29.022 | 0,43% | 11 | $1.981 | $0,07 | 0,35% | 0,059% (17) |
| Ceramic VS Titanium | 28.505 | 0,45% | 3 | $537 | $0,02 | 0,35% | 0,056% (16) |
| Review Focus | 27.757 | 0,25% | 2 | $290 | $0,01 | 0,47% | 0,043% (12) |
| **Totaal** | **299.926** | 0,36% | **60** | **$11.174** | **$0,04** | 0,45% | **0,065% (193)** |

### Sinds 29 okt (alleen de 4 live mails)

| Dag | Mails | Spam | Afmeld | Omzet |
|---|---|---|---|---|
| 29 okt | 1.403 | 0 | 2 | $216 |
| 30 okt | 1.577 | 0 | 4 | $0 |
| 31 okt | 1.303 | 0 | 7 | $216 |
| 1 nov | 1.442 | 0 | 0 | $0 |
| **Samen** | **5.725** | **0** | **13 (0,23%)** | **$432 ($0,075)** |

## 3. Vergelijking (laatste 30 dagen, e-mail)

| | Ontvangers | Klik | Per ontv. | Afmeld | Spam | Bounce |
|---|---|---|---|---|---|---|
| Failure to launch T2SmtR | 94.887 | 0,33% | $0,03 | 0,50% | 0,042% | 0,49% |
| Alle flows | 279.620 | 1,76% | $0,59 | 0,88% | 0,079% | 1,06% |
| Alle flows zonder FTL | 184.733 | 2,50% | $0,88 | 1,08% | 0,098% | 1,35% |
| Welcome T4a5Mk | 58.591 | 1,94% | $1,06 | 1,54% | 0,150% | 1,31% |
| Sunset TbYQmX | 23.453 | 0,29% | $0,03 | 0,58% | 0,021% | 0,35% |
| Winback UEfh4h | 15.614 | 0,53% | $0,10 | 0,51% | 0,019% | 0,24% |
| Cart TZG9Mx | 9.222 | 3,11% | $2,10 | 1,09% | 0,055% | 0,72% |
| Checkout QUBUQV | 5.601 | 4,32% | $4,42 | 1,43% | 0,102% | 12,41% |
| Campagnes (35 stuks) | 1.696.436 | 0,56% | $0,077 | 0,39% | 0,033% | 0,07% |
| Homestead E12 Halloween (31 okt, Engaged 90) | 84.561 | | $0,14 | 0,37% | 0,021% | |
| Homestead E11 Late-Month (27 okt) | 83.306 | | $0,155 | 0,54% | 0,026% | |

FTL zit op het niveau van sunset: laagste klik en omzet van alle flows, lager dan een gemiddelde campagne.

## 4. Spam- en klachtenruimte

| | Klachten 30 d | Mails 30 d | Percentage |
|---|---|---|---|
| FTL | 40 | 94.887 | 0,042% |
| Alle flows | 218 | 279.620 | 0,079% |
| Flows zonder FTL | 178 | 184.733 | 0,098% |
| Campagnes | 555 | 1.696.436 | 0,033% |
| Account totaal | 773 | 1.976.056 | 0,039% |
| Account zonder FTL | 733 | 1.881.169 | 0,039% |

- FTL is 18% van de flowklachten en 5% van alle klachten. Sinds de inkorting naar 4 mails (29 okt): 0 klachten op 5.725 mails.
- De 0,118% uit smooche/04 is de oktobermeting van Klaviyo op een ander venster; met deze 30-dagenmeting zitten flows op 0,079%. In beide gevallen trekt FTL het percentage **omlaag**: zonder FTL stijgt het flowpercentage (hier 0,079% naar 0,098%), het accountpercentage blijft 0,039%.
- Google's grens van 0,1% gaat over klachten van Gmail-gebruikers op alle mail van het domein (Postmaster Tools), niet over Klaviyo's percentage per flow. Wat FTL wel doet: veel volume met zwakke betrokkenheid (0,33% klik), dat telt mee voor de domeinreputatie. In november schatten we ~25.000 FTL-mails tegen ~1,5 à 2 miljoen campagnemails: klein.
- Conclusie: FTL vreet geen meetbare spamruimte. Het argument om te pauzeren is omzet en botsing met campagnes, niet spam.

## 5. Overlap met Homestead-campagnes in november

Steekproef: 250 willekeurige FTL-ontvangers van 29 okt (10:00 tot 22:00 UTC, 1.173 FTL-ontvangers in dat venster), segmentlidmaatschap op 1 nov.

| Segment | Aandeel FTL-ontvangers |
|---|---|
| HS // Engaged 90 Days | 94% |
| HS // Engaged 180 Days Email | 94% |
| EB [DG] Engaged 30 Days | 39% |
| EB [DG] Engaged 180 Days \| 7/31/26 | 39% |
| Product Viewers L30 Days | 18% |
| HS // INT Subscribers (non US) | 20% |
| All buyers | 0% |
| EB [DG] Unengaged 180 Days \| Non-Buyers | 0% |

Dus: 100% krijgt de volledige-lijstmails (E1, E11, E15, E19) en 94% alle E90-mails. Volgens de Homestead-kalender krijgt een E90-lezer in november ~15 campagnemails plus 3 resends (zie `research/homestead/kalender-november-2026.md`). FTL voegt daar 4 mails in 5 dagen aan toe, om 08:00 lokaal.

**Botsing met smart sending (gemeten):** 90 FTL-ontvangers uit E90, al hun Received Email-events 29 okt tot 1 nov. Op 31 okt en 1 nov waren er 66 profieldagen met een FTL-mail; op **geen enkele** daarvan kwam die dag ook een campagne. Van de 90 kregen er 49 de Halloween-mail en 44 de BF-launch E1; de rest kreeg op die dag FTL in plaats daarvan. FTL om 08:00 lokaal valt precies 15 minuten voor de 08:15-campagnes, die smart sending (16 uur) aan hebben.

Schatting november (FTL-volume per dag x aandeel in het segment, per Homestead-maildag; de 3 BF-mails van 27 nov hebben smart sending uit en tellen niet): **~11.000 campagnemails niet verstuurd** naar betrokken lezers. Bij $0,10 à $0,15 per ontvanger (E90-campagnes eind oktober $0,14 à $0,155, BF-week hoger) is dat **$1.100 à $1.650** aan toegeschreven campagneomzet. FTL zelf: ~25.000 mails x $0,05 à $0,075 = **$1.250 à $1.900**, en een deel daarvan zou zonder FTL via de campagne toch zijn binnengekomen. Netto ongeveer nul, met de verkeerde claims als nadeel en ~60 à 125 afmeldingen (0,23 à 0,50%) onder precies de mensen die in de BF-week het meeste opleveren.

## 6. Opties

| Optie | Wat | November-effect (schatting) | Oordeel |
|---|---|---|---|
| **A. Pauzeren (advies)** | De 4 live mails (90714929, 108678769, 108679684, 90716322) op Draft tot 1 dec; flow blijft Live. Niet de flow op Manual (dan stapelt een wachtrij op die in december in één keer kan gaan) | -25.000 mails, -$1.250 à $1.900 FTL-omzet, +~11.000 campagnemails bij betrokken lezers (+$1.100 à $1.650), -60 à 125 afmeldingen, geen Prime Time/100-day-claims meer | Doen |
| B. Houden met strakker filter (engaged only) | Split extra: Engaged 30 | Haalt maar 6% weg (94% is al E90); botsing en claims blijven | Niet zinvol |
| C. Houden, maar aanpassen | Banner en claims vervangen (BF-band, 30 dagen retour, 75 jaar); eerste wachttijd tot 19:00 in plaats van 08:00, zodat FTL na een ochtendcampagne zelf wordt overgeslagen en alleen op lege dagen (9 in november) verstuurt; alleen Titanium vs Non-Stick en Titanium Vs Stainless Steel houden | ~8.000 à 10.000 mails, geen campagneblokkade, ~$600 à $900 | Kan, maar kost een middag templatewerk voor ~$700; beter meenemen in de herbouw (BACKLOG 5) |

Na 1 december: FTL niet zomaar terugzetten. Eerst (1) banners en claims vervangen, (2) de "W2"-voorwaarde vervangen zodat de BF-groep van Rn556d niet in de oude reeks belandt, (3) zendtijd weg van de campagnetijd, of FTL samenvoegen met de welcome (BACKLOG item 5).

## Bronnen

- Klaviyo GET `/api/flows/T2SmtR` (definitie), `/api/flows/T2SmtR/flow-actions`, `/api/flow-messages/*`, `/api/templates/*` (banners), `/api/lists/Uw8eZG`, `/api/segments`, `/api/profiles/*/relationships/segments` (250 profielen), `/api/events` (Received Email 29 okt 10:00 tot 22:00 UTC; per profiel 29 okt tot 1 nov), `/api/campaigns` (smart sending). POST `flow-values-reports` en `campaign-values-reports` (last_30_days, last_90_days), `flow-series-reports` (dagelijks, 30 d).
- LOG.md 8 okt (W2-voorwaarde), 28 okt (6 mails Draft), DECISIONS.md (19 okt, Black Friday 2026), research/flows-audit/2026-10-19-*.md, research/smooche/04-meer-output-november.md.
