# BFCM 2026 · Welk mailformat levert het meest op? (vr 27 nov)

Stand: donderdag 26 nov 2026, 16:10 UTC. Alleen gelezen in Klaviyo (campaign-values-reports met conversiemetric Placed Order RSNxYV, campagnetemplates via `/api/campaign-messages/{id}/template`, Placed Order-events met attributie). Niets gewijzigd. Bedragen in USD, Klaviyo-attributie. Ruwe data: scratchpad `golive/fmt/` (values.json, html/, final2.json, orders26.json, orders25.json). Segmentcijfers en tiers sluiten aan op `segment-strategie.md`.

## Samenvatting

1. **Het format is niet de grootste hefboom.** Binnen hetzelfde publiek (US 90D, verkoopmails november) haalt tekst mediaan $0,176 per ontvanger (n=6) en de beeldmail met productraster $0,200 (n=4, waarvan 3 op zaterdag 08:15). Dat verschil (~15%) valt weg tegen aanbod, publiek en dag.
2. **Tekst wint op orderwaarde en op de 12-delige set.** Gemiddelde order uit Email 11 (tekst) $357 en uit "Most unique product" (tekst) $480, tegen $243 uit de Gift Guide (raster). In beide tekstmails is 48% van de omzet de 12-delige set; in de Gift Guide 39%.
3. **Het raster wint op aantal orders en in INT.** Gift Guide US 77 orders (de meeste van de week, vooral losse pannen, deksels, vaatwasstrips); Gift Guide INT $0,188 is de beste INT-mail van november naar een lijstsegment (INT-tekst Email 9: $0,116).
4. **Vorig jaar op Black Friday hielden alle drie de golven stand:** raster 08:00 $0,59, raster 13:00 $0,64, tekst 18:00 $0,651 (beste van de dag, 50 woorden, één code).
5. **Beste US-mail van november is het dichtste voorbeeld van vrijdag:** F13 Lucky Friday, tekstbrief van Benjamin met een extra 15% bovenop BF, "already applied", drie producten als tekstregels: $0,247. Vorig jaar was de beste mail ooit ook een tekst met een extra korting bovenop de sale ("Last Push", extra 30%, afhakers): $0,77.
6. **Hybride (lange brief met meerdere blokken) en single-hero beeldmails zijn de zwakste vormen:** mediaan $0,100 en $0,100 tot $0,108 in 2026. Kort en één product werkt; lang met 15 tot 24 links niet.
7. **Product: focus op de 12-delige set (US) en 6-delige set (INT) klopt.** De 12-delige set is 16% van de campagne-orders maar 28% van de campagne-omzet deze week. Damascus-messenset: 1 campagne-order (15 in de hele winkel), Just Everything: 7 (58 totaal). Die twee horen niet in het hoofdblok.
8. **Advies vrijdag:** 08:00 hybride (korte brief Benjamin + één blok 12-delig / INT 6-delig), 13:00 raster (de drie deals plus bestsellers), 18:00 korte tekstbrief "last hours". Onderwerp 08:00 en 13:00 met het aanbod ("Extra 20% off, already applied"), 18:00 persoonlijk; hoogstens één emoji.
9. Vandaag (Thanksgiving US, Bon Appétit INT) is nog niet te beoordelen: 3 tot 8 uur oud, $0,056 en $0,044 per ontvanger.

## 1. Methode in het kort

- **Campagnes:** alle e-mailcampagnes met verzending tussen 1 sep en 26 nov 2026 en tussen 20 nov en 5 dec 2025, minimaal 3.000 ontvangers, zonder testsends, zonder Zaymo-goedkeuring en zonder servicemails (vertragingsmail kopers 2025, "Free first pack" vaatwasstrips, SMS-aanmeldmail). 103 campagnes.
- **Format bepaald uit de echte HTML** (niet uit de naam): aantal inhoudsbeelden (header, footer, navigatie en iconen eruit gefilterd op basis van beelden die in 6 of meer templates terugkomen), woorden live tekst, links naar de winkel, aantal verschillende productlinks. Daarna elke mail nagelezen en waar nodig handmatig gecorrigeerd.
  - **tekst**: brief, geen hero, 0 inhoudsbeelden (soms een kleine header), 60 tot 550 woorden live tekst. HS-tekstmails, onze Benjamin-brieven, vorig jaar "48 Hours Left", "Plain text reminder", "8 Hours Left".
  - **single-hero**: ontworpen beeldmail (tekst in beelden, 5 tot 9 woorden live tekst) rond één aanbod of één product, geen productraster.
  - **grid**: ontworpen beeldmail met 3 of meer productkaarten (bestsellers, gift guide, bundels). Ook "Win your order back" (brief plus 6 productkaarten).
  - **hybride**: brief van 150+ woorden plus 1 tot 6 beelden of productblokken (Founder letter E6, Thanksgiving prep plan E5, Thanksgiving Roast, Roasting Pan INT, vandaag Thanksgiving en Bon Appétit).
- **Eerlijk vergelijken:** (a) alleen verkoopmails (recepten en educatie apart gemarkeerd als "content"), (b) per periode (BFCM 2025, sep-okt 2026, nov 2026) en markt, (c) gematchte paren: zelfde publiek, paar dagen uit elkaar, (d) index = $/ontvanger gedeeld door de mediaan van alle sends in dezelfde periode en markt (1,00 = gemiddeld).
- **Kanttekeningen:** opens zijn vervuild door Apple-proxy, dus niets beslist op open. Klaviyo-attributie (5 dagen) verdeelt orders over overlappende mails in de BF-week. Alle rasters in november zijn HS-mails op zaterdag 08:15, de tekstmails vooral door de week; dag en afzender lopen dus mee. A/B-campagnes staan als één regel (totaal).

## 2. Vergelijking per format

### 2a. Verkoopmails, mediaan en gemiddelde $/ontvanger

| Periode | Format | n | $/ontv. mediaan | $/ontv. gem. | Klik mediaan | $/klik mediaan | Index mediaan |
|---|---|---|---|---|---|---|---|
| BFCM 2025 (20 nov t/m 3 dec) | tekst | 4 | **0,557** | 0,541 | 1,64% | $34 | **1,38** |
| | grid | 11 | 0,434 | 0,424 | 1,72% | $24 | 1,08 |
| | single-hero | 4 | 0,246 | 0,250 | 0,99% | $25 | 0,61 |
| sep-okt 2026 | tekst | 15 | **0,107** | 0,108 | 0,83% | $14 | **1,44** |
| | grid | 3 | 0,070 | 0,066 | 0,70% | $8 | 0,95 |
| | single-hero | 10 | 0,065 | 0,085 | 0,56% | $13 | 0,87 |
| nov 2026 US (1 t/m 25) | tekst | 6 | 0,176 | 0,189 | 0,58% | $30 | 1,06 |
| | grid | 4 | **0,200** | 0,201 | 0,69% | $29 | **1,51** |
| | hybride | 3 | 0,111 | 0,101 | 0,52% | $26 | 0,87 |
| | single-hero | 2 | 0,110 | 0,110 | 0,55% | $20 | 0,86 |
| nov 2026 INT (1 t/m 25) | grid | 4 | 0,097 | 0,112 | 0,73% | $15 | 1,04 |
| | single-hero | 2 | 0,106 | 0,106 | 0,75% | $15 | 1,18 |
| | hybride | 3 | 0,088 | 0,098 | 0,80% | $11 | 0,97 |
| | tekst | 1 | 0,116 | 0,116 | 0,78% | $15 | 0,76 |

Uitschrijf per format verschilt nauwelijks (mediaan 0,30 tot 0,48% in 2026); spam overal onder 0,09% in 2026. Format is geen deliverability-risico.

Lezing: tekst is over de hele periode de stabielste vorm (beste index in BFCM 2025 en sep-okt 2026). In november US haalt het raster de hoogste mediaan, maar drie van de vier rasters zijn zaterdag-ochtend-sends van HS met het volle aanbod; de vierde ("Win your order back", woensdag) deed $0,181, gelijk aan de tekstmails van die week.

### 2b. Gematchte paren (zelfde publiek, korte afstand)

| Paar | Publiek | Tekst | Beeld | Verschil |
|---|---|---|---|---|
| Email 9 tekst (wo 18 nov) vs Email 10 Gift Guide raster (za 21 nov) | US VMjhb2 | $0,169, klik 0,64% | $0,194, klik 0,75% | raster +15% |
| idem | INT XrFa5r | $0,116, klik 0,78% | $0,188, klik 0,73% | raster +62% |
| Email 11 tekst (ma 23 nov, deal-lancering $649) vs Gift Guide raster | US (180D-achtig) vs 90D | $0,205, klik 0,39% | $0,194 | tekst +6%, met breder publiek |
| Oct Email 10 en 11 tekst (25 en 27 okt) vs Oct Email 9 en 12 single-hero (23 en 31 okt) | VKxqyA (E90, alle markten) | $0,171 / $0,155 | $0,168 / $0,165 | gelijk |
| Oct Email 4 tekst (12 okt) vs Oct Email 3 en 5 single-hero (10 en 11 okt) | W5PSSp (E180) | $0,074 | $0,039 / $0,045 | tekst +75% |
| BF 2025: 08:00 raster, 13:00 raster, 18:00 tekst | E180 / E30 / E90 + BFCM-lijst | $0,651 (18:00) | $0,590 / $0,640 | tekst gelijk of beter, als derde golf van de dag |
| E6 Founder letter hybride vs Email 3 single-hero (INT) | XrFa5r | hybride $0,156 | $0,114 | hybride +37% (korte brief, 1 productfoto) |
| E5 Thanksgiving prep hybride (549 woorden, 24 links) vs E6 (211 tot 233 woorden) | US / INT 90D | $0,137 / $0,051 | | lange hybride verliest, vooral INT |

### 2c. Wat de vormen anders doen (BF-week 2026, orders uit e-mailcampagnes)

| Mail | Format | Orders | Gem. order | Orders met 12-delig | 12-delig in omzet |
|---|---|---|---|---|---|
| Most unique product (24 nov) | tekst, 1 product | 30 | **$480** | 10 | **48%** |
| Email 11 BF Week Is Here (23 nov) | tekst, 1 product + 5 gifts | 64 | $357 | 15 | 48% |
| Email 13 Still Deciding (25 nov, kijkers + afhakers) | single-hero | 29 | $339 | 5 | 37% |
| Selling out before BF (20 nov) | tekst, sale-collectie | 51 | $311 | 6 | 25% |
| Thanksgiving x BF (vandaag, loopt nog) | hybride | 17 | $309 | 3 | 33% |
| Email 9 Before the Rush (18 nov) | tekst | 56 | $266 | 4 | 22% |
| Gift Guide US (21 nov) | grid, 5 producten | **77** | $243 | 10 | 39% |
| Gift Guide INT (21 nov) | grid | 41 | $245 | 0 (US-only) | 6-delig: 9 orders |

Tekst met één product trekt minder kliks (0,39 tot 0,64%) maar duurdere orders en meer sets; het raster trekt meer kliks en meer kleine orders (deksels, vaatwasstrips, losse pannen). Per ontvanger komt het op hetzelfde uit.

### 2d. Beste en slechtste voorbeelden

- Beste ooit: vorig jaar "Last Push for Abandoned Orders" (tekst, afhakers 30d) $0,77; "Plain text reminder" BF 18:00 $0,651; "Highlight Bestsellers" BF 13:00 (raster) $0,640.
- Beste 2026 (lijst, geen gedragssegment): F13 Lucky Friday (tekst, extra 15% bovenop BF, al toegepast) $0,247; HS Email 7 (raster, 180D) $0,223; Email 11 (tekst) $0,205; Email 4 Thanksgiving Pans (raster) $0,205.
- Slechtste 2026: Roasting Pan Teaser (single-hero) $0,027; HS Email 8 recept (tekst, content) $0,028 INT en $0,043 US; resends naar niet-openers als beeldmail $0,020 tot $0,047; Thanksgiving Roast (hybride, 330 woorden, 23 links) $0,053.
- Vergelijking tekst onderling: korte tekstbrieven (60 tot 150 woorden) index 1,32; 151 tot 250 woorden 1,03; 251+ woorden 0,97.

### 2e. Onderwerp, stem, aantal links (2026, verkoop- en contentmails)

- Aanbod in het onderwerp (%, $, off, free, gifts, sale): index 1,09 (n=28) tegen 0,95 zonder (n=42); open iets lager (39,7 tegen 42,4%). Vorig jaar op BF: twee onderwerpen met "62% Off" en één zonder ("Don't let this burn"), alle drie rond $0,60.
- Emoji: index 0,71 (n=10) tegen 1,03 zonder, maar de emoji-onderwerpen waren vooral HS-contentmails. F13 had één emoji en was de beste. Conclusie: emoji helpt niet; hoogstens één.
- Stem: Benjamin 1,03 tegen merkstem 0,97 (n=34 en 55). Geen effect op zich; de brief werkt door kort en één aanbod, niet door de naam.
- Links: 4 tot 6 links index 1,21; 0 tot 3: 0,99; 7 tot 12: 0,95; 13+: 1,07 (vooral rasters en hybrides). Tekstbrieven met 3 tot 4 links naar hetzelfde aanbod geven de hoogste $/klik ($29 tot $30 in november US).

## 3. Welke producten verkopen uit e-mail in de BF-week (18 t/m 26 nov 2026)

Bron: 5.764 Placed Order-events, waarvan 531 toegeschreven aan een campagne (e-mail + SMS, $163.975) en 847 aan een flow ($257.336). Gratis cadeaus en gratis Pizza Steel weggelaten. Aandeel = deel van de orders waarin het product zit.

| Product | Alle orders | Campagne-orders | Campagne-omzet (verdeeld) | Flow-orders |
|---|---|---|---|---|
| 12-delige set (incl. variant met Pizza Steel) | 737 (12,8%) | 84 (15,8%) | **~$45.900 (28%)** | 130 |
| 6-delige set | 810 (14,1%) | 85 (16,0%) | ~$24.900 (15%) | 134 |
| Pan Pro Standard | 1.552 (26,9%) | 87 (16,4%) | ~$11.800 | 169 |
| Pan Pro Large | 1.046 (18,1%) | 85 (16,0%) | ~$11.500 | 129 |
| Deksel (Stainless Steel Lid) | 869 (15,1%) | 104 (19,6%) | ~$11.300 | 153 |
| Vaatwasstrips | 557 (9,7%) | 78 (14,7%) | ~$8.300 | 103 |
| 2 Pans + 2 Lids | 203 | 17 | ~$4.400 | 45 |
| Just Everything-bundel (34-delig) | 58 | **7** | | 10 |
| Damascus 67 Layer Knife Set (8-delig) | 15 | **1** | | 4 |

Conclusies:
- **US: de 12-delige set als hoofdproduct is juist.** Het is de grootste omzetpost uit campagnes (28%) en uit de hele winkel (~$421k van $1,67M). Tekstmails met de set als enige product halen de hoogste orderwaarde.
- **De extra 20% op Damascus en Just Everything levert weinig op als hoofdblok.** Samen 8 campagne-orders in negen dagen. Noem ze als tweede en derde regel ("Also extra 20% off: ..."), niet als gelijkwaardige kaarten.
- **INT: de 6-delige set klopt.** In de INT-mails is de 6-delige set het meest gekochte product uit de Gift Guide (9 van 41 orders); daarnaast Pan Pro Standard en Large.
- **Veel orders zijn losse pannen plus deksel.** Wie de set niet wil, koopt een Pan Pro (Standard/Large) met deksel. Een raster met die twee naast de deals vangt die groep (zoals de Gift Guide: 77 orders).
- Vorig jaar (24 nov t/m 2 dec 2025, 843 campagne-orders) was het beeld gelijk zonder sets: Pan Pro Standard in 40% van de orders, deksel 29%, Pan Pro Large 24%, wok 18%. De set bestond toen nog niet.

## 4. Vandaag (26 nov)

| Mail | Format | Ontv. | Klik | Orders | $/ontv. | Stand |
|---|---|---|---|---|---|---|
| Thanksgiving x Black Friday · US (01M8AQT4QCVKCMAEVGSSTG62D8) | hybride (hero + brief + 1 knop, extra 10%) | 78.399 | 0,25% | 17 (gem. $309) | 0,056 | 08:15 lokaal, dus 3 uur oud aan de oostkust, net verstuurd aan de westkust |
| As seen in Bon Appétit · INTL (01M8AQT6SZ8FB8F2CEM519FKN5) | hybride | 58.782 | 0,35% | 11 (gem. $234) | 0,044 | 3 tot 8 uur oud |

Om 14:50 UTC stond het op $0,020 en $0,038; nu $0,056 en $0,044. Te vroeg voor een oordeel. Ter vergelijking: Thanksgiving vorig jaar (single-hero, E30) eindigde op $0,238. Morgenochtend opnieuw kijken voordat de 13:00-golf vastligt.

## 5. Advies vrijdag 27 november

Uitgangspunt: format verschuift de omzet per ontvanger hooguit 15 tot 20%; het aanbod (extra 20%, al toegepast) en de juiste golfvolgorde doen de rest. Gebruik daarom per golf het format dat bij de taak van die golf past, zoals vorig jaar (raster, raster, tekst: alle drie $0,59 tot $0,65). Dit sluit aan op wat HS al heeft staan (Email 15 lancering 08:00, Email 16 Bestsellers 13:00, Email 17 "A Note Before Black Friday Ends" tekst 18:00).

| Golf | US | INT | Onderwerp | Waarom (data) |
|---|---|---|---|---|
| **08:00 lancering** | **Hybride:** korte brief Benjamin (80 tot 120 woorden) die het aanbod uitlegt ("extra 20% on top, already applied, no code"), daaronder één productblok 12-delige set met prijs, knop; Damascus en Just Everything als twee tekstregels met link. 1 primaire knop, 3 tot 5 links. | **Hybride:** zelfde opbouw met de 6-delige set als enig blok. | Met het aanbod: "Extra 20% off the 12-piece set, already applied" / INT "Extra 20% off the 6-piece set, already applied". Geen emoji. | F13 (tekst, extra 15% bovenop BF, al toegepast) was de beste US-mail van november ($0,247). Korte brief + één productfoto was in INT de beste hybride (E6 $0,156). De set haalt in één-productmails 48% van de omzet en gem. $357 tot $480 per order. |
| **13:00 tweede golf** | **Raster:** de drie deals (12-delig groot, Damascus, Just Everything) plus Pan Pro Standard, Pan Pro Large met deksel en 6-delig. Korte kop, geen lange tekst. | **Raster:** 6-delig groot, plus Pan Pro Standard, Pan Pro Large, deksel. | Met het aanbod en "bestsellers": "Up to 70% off our bestsellers, extra 20% on the sets". Hoogstens één emoji. | Raster haalt de meeste orders (Gift Guide 77 US) en vangt de koper van een losse pan; vorig jaar BF 13:00 raster $0,640, hoogste klik van de dag (2,34%). INT Gift Guide $0,188, beste INT-mail. |
| **18:00 laatste uren** | **Tekst:** Benjamin, 60 tot 120 woorden, één aanbod (12-delig met extra 20%, eindigt om middernacht), 2 tot 3 links naar dezelfde pagina, P.S. met de deadline. | **Tekst:** zelfde, 6-delig. | Persoonlijk, zonder %: bv. "Before midnight" / "A short note before tonight". Geen emoji. | Vorig jaar was de avondtekst de beste golf van BF ($0,651, 50 woorden). Korte tekstbrieven index 1,32; INT-tekst met één aanbod deed $0,125 tot $0,146 (sep-okt). |

Alle golven: Smart Sending uit en de publieken zoals in `segment-strategie.md` (08:00 180D, 13:00 en 18:00 90D).

## 6. Do's en don'ts uit onze data

1. **Do: één product per brief, 3 tot 5 links naar hetzelfde aanbod.** Tekstmails met één product halen de duurste orders ($357 tot $480) en de hoogste $/klik ($29 tot $30). Mails met 4 tot 6 links: index 1,21.
2. **Do: kort.** Tekstbrieven van 60 tot 150 woorden: index 1,32; 151 tot 250: 1,03; boven 250: 0,97. Vorig jaar hadden de BF-tekstmails 50 tot 130 woorden, ook de beste mail ooit ("Last Push", extra 30% bovenop de sale, ~130 woorden, $0,77).
3. **Do: zeg letterlijk dat de korting al is toegepast en zet het aanbod in het onderwerp van de verkoopgolven.** Aanbod in onderwerp index 1,09 tegen 0,95.
4. **Don't: lange hybride met veel blokken en 15 tot 24 links.** Thanksgiving prep plan (549 woorden, 24 links) $0,137 US en $0,051 INT; Thanksgiving Roast (330 woorden, 23 links) $0,053.
5. **Don't: Damascus en Just Everything als gelijkwaardige kaarten naast de set.** Samen 8 campagne-orders deze week; ze nemen ruimte van de set en van de losse pannen.
6. **Don't: een resend als beeldmail naar niet-openers verwachten dat die iets oplevert.** Resend 1 en 2 deden $0,020 tot $0,047; als er zaterdag een resend gaat, dan als korte tekst.

## 7. Volledige tabel

Alle campagnes 20 nov t/m 5 dec 2025 en 1 sep t/m 26 nov 2026 (min. 3.000 ontvangers, zonder testsends en servicemails). Tier: E30/E90/E180 = engaged-segment, Alle = hele (markt)lijst, Intent = kijkers/afhakers, Resend = niet-openers, Kopers, SMS = SMS-abonnees. "Content" = recept of educatie zonder verkoopkern (niet meegeteld in 2a). Woorden live tekst = tekst die niet in beelden staat (beeldmails 5 tot 9). Vorig jaar staan tekstmails dubbel in de HTML (desktop en mobiel), dus de echte lengte is ongeveer de helft.

| Datum (UTC) | Campagne | Onderwerp | Markt | Publiek | Format | Ontv. | Open | Klik | Conv. | Omzet | $/ontv. | Uitschr. | Spam | Aanbod in onderwerp | Stem | Links | Woorden live tekst | Hoofdproduct | Let op |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025-11-20 do 08:15 | 11/20 Feature Bundle / 90 Days Engaged | Stack Your Savings | alle | E90 (S6kBRe+TMaWCL) | **grid** | 18.760 | 51,6% | 1,01% | 0,10% | $3.257 | **0,174** | 1,14% | 0,037% | nee | merk | 12 | 7 | meerdere |  |
| 2025-11-21 vr 08:21 | 11/21 One Pot Wonders for Busy Weeknights / 180 Days Engaged | Ready for a FlavorfuI Dinner? | alle | E180 (S6kBRe+TSVhx9) | **single-hero** | 21.584 | 47,3% | 0,53% | 0,11% | $6.558 | **0,305** | 1,02% | 0,070% | nee | merk | 6 | 7 | sale-collectie | content |
| 2025-11-22 za 08:12 | 11/22 Low in Stock Items / 30 Days Engaged | Warehouse Update | alle | E30 (S6kBRe+TNdhKc) | **grid** | 17.326 | 55,9% | 2,07% | 0,23% | $8.885 | **0,514** | 1,21% | 0,029% | nee | merk | 10 | 7 | meerdere |  |
| 2025-11-23 zo 08:15 | [Follow-up] 11/20 Feature Bundle / 90 Days Engaged | Fire Up Your Savings | alle | Resend (UwS4LP) | **grid** | 5.292 | 29,0% | 0,91% | 0,06% | $992 | **0,188** | 0,97% | 0,019% | nee | merk | 12 | 7 | meerdere |  |
| 2025-11-24 ma 08:12 | 11/24 48 Hours Left [Plain text] / Engaged 180 Days | A note from James, | alle | E180 (TSVhx9) | **tekst** | 12.920 | 52,4% | 1,51% | 0,26% | $6.876 | **0,533** | 1,24% | 0,016% | nee | James | 7 | 115 | sale-collectie |  |
| 2025-11-25 di 17:00 | Clone 11/25 10 Days 10 % Off Special Offer Ends Tonight / 30 Days Enga | Hey [naam], 52% 0ff BundIes Ends Tonight | alle | E30 (S6kBRe+TNdhKc) | **grid** | 35.768 | 32,7% | 1,72% | 0,14% | $14.488 | **0,406** | 0,78% | 0,036% | ja | merk | 9 | 7 | meerdere |  |
| 2025-11-26 wo 08:11 | 11/26 Staff Picks / 180 Days Engaged | The Top 3 Kitchen Favorites | alle | Alle (XYRq7Q) | **grid** | 37.584 | 50,8% | 1,42% | 0,14% | $11.828 | **0,315** | 1,49% | 0,021% | nee | merk | 12 | 19 | meerdere |  |
| 2025-11-27 do 08:07 | 11/27 Thanks Giving / 30 Days Engaged | Happy Thanksgiving | alle | E30 (TNdhKc) | **single-hero** | 27.378 | 61,8% | 0,99% | 0,12% | $6.509 | **0,238** | 1,31% | 0,048% | nee | merk | 6 | 7 | sale-collectie |  |
| 2025-11-28 vr 08:03 | 11/28 [8 AM] Black Friday + 62% Off Sitewide / 180 Days Engaged | 62% 0ff Cookware! | alle | E180 (S6kBRe+TSVhx9) | **grid** | 30.704 | 40,0% | 2,84% | 0,28% | $18.059 | **0,590** | 0,73% | 0,124% | ja | merk | 19 | 55 | meerdere |  |
| 2025-11-28 vr 13:03 | 11/28 [1 PM] Highlight Bestsellers / 90 Days Engaged | 62% Off these BestseIIers | alle | E30 (S6kBRe+TNdhKc) | **grid** | 27.011 | 57,1% | 2,34% | 0,27% | $17.222 | **0,640** | 0,95% | 0,119% | ja | merk | 10 | 7 | meerdere |  |
| 2025-11-28 vr 18:06 | 11/28 [6 PM] Plain text reminder / Engaged 90 Days | Don’t Iet this burn | alle | E90 (S6kBRe+TMaWCL) | **tekst** | 28.491 | 60,9% | 1,83% | 0,29% | $18.507 | **0,651** | 1,09% | 0,060% | nee | merk | 5 | 97 | sale-collectie |  |
| 2025-11-29 za 10:02 | 11/29 [10 AM]: Black Friday Sale Extension / 30 Days Engaged | Black Weekends | alle | E30 (S6kBRe+TNdhKc) | **grid** | 26.325 | 59,6% | 1,80% | 0,23% | $13.376 | **0,509** | 1,03% | 0,034% | nee | merk | 20 | 50 | meerdere |  |
| 2025-11-29 za 13:56 | 11/29 Last Push for Abandoned Orders / 30 Days Abandoned Cart or Check | I Just Got Fired for Doing This | alle | Intent (Tgt2x2+UuABDJ) | **tekst** | 12.069 | 57,1% | 1,53% | 0,48% | $9.286 | **0,770** | 1,21% | 0,050% | nee | merk | 2 | 266 | sale-collectie |  |
| 2025-11-29 za 17:02 | 11/29 [5 PM]: Bestsellers / 30 Days Engaged | 62% Off this Top Trio | alle | E30 (S6kBRe+TNdhKc) | **grid** | 28.479 | 56,7% | 1,79% | 0,21% | $12.321 | **0,434** | 1,09% | 0,049% | ja | merk | 12 | 7 | meerdere |  |
| 2025-11-30 zo 10:03 | 11/30 Black Friday Weekend Extension 120 Days Engaged | The Timer’s Started | alle | E180 (S6kBRe+W8v83J) | **grid** | 28.132 | 57,2% | 1,33% | 0,25% | $15.714 | **0,560** | 1,03% | 0,039% | nee | merk | 11 | 7 | meerdere |  |
| 2025-11-30 zo 17:02 | 11/30 [5 PM] 8 Hours Left (Plain text) / Engaged 30 Days | Time’s ticking | alle | E30 (S6kBRe+TNdhKc) | **tekst** | 11.045 | 60,4% | 1,76% | 0,29% | $6.399 | **0,580** | 1,42% | 0,036% | nee | merk | 7 | 185 | sale-collectie |  |
| 2025-11-30 zo 21:17 | Clone 11/30 [5 PM] 8 Hours Left (Plain text) / Engaged 30 Days | Time’s ticking | alle | E30 (TNdhKc) | **tekst** | 25.526 | 61,0% | 1,50% | 0,16% | $10.191 | **0,400** | 1,82% | 0,051% | nee | merk | 7 | 185 | sale-collectie |  |
| 2025-12-01 ma 08:15 | Clone 12/1 [AM]: Cyber Monday - 42% Sitewide Off + 5% Off / 30 Days En | Trim the Fat | alle | E30 (TNdhKc) | **single-hero** | 27.899 | 54,0% | 0,90% | 0,08% | $4.195 | **0,151** | 1,55% | 0,151% | nee | merk | 7 | 9 | sale-collectie |  |
| 2025-12-01 ma 17:02 | 12/1 [PM]: Cyber Monday / 30 Days Engaged | Cyber Monday Specials! | alle | E30 (TNdhKc) | **single-hero** | 20.799 | 58,2% | 0,99% | 0,14% | $5.284 | **0,255** | 0,91% | 0,029% | nee | merk | 8 | 9 | sale-collectie |  |
| 2025-12-02 di 10:14 | Clone 12/1 [PM]: Cyber Monday / 30 Days Engaged (2nd December Resend) | This Cyber Monday Deal is Ending Soon! | alle | E30 (TNdhKc) | **single-hero** | 29.591 | 54,6% | 1,13% | 0,17% | $10.506 | **0,355** | 1,24% | 0,085% | ja | merk | 8 | 9 | sale-collectie |  |
| 2025-12-03 wo 08:14 | 12/3 Cyber Monday Extension + 5% Off [VIP5] / 120 Days Engaged | One Last Call | alle | E180 (W8v83J) | **grid** | 24.776 | 53,8% | 0,91% | 0,10% | $4.715 | **0,191** | 1,28% | 0,053% | nee | merk | 10 | 9 | meerdere |  |
| 2026-09-03 do 12:32 | AU-01 - vr 4 sept 08:00 AEST - Father's Day Sale Ends Sunday (AU+NZ) | FATHER'S DAY IS SUNDAY | INT | Alle (QVnhWd+TLKCJU) | **tekst** | 16.169 | 34,1% | 0,87% | 0,03% | $1.205 | **0,075** | 0,84% | 0,012% | nee | Benjamin | 5 | 193 | sale-collectie |  |
| 2026-09-03 do 16:46 | INTL-01 - vr 4 sept 10:00 GMT - Siraat Birthday Sale | IT'S OUR BIRTHDAY | INT | Alle (ShPpDV) | **tekst** | 52.514 | 43,1% | 2,00% | 0,07% | $6.534 | **0,125** | 0,95% | 0,036% | nee | Benjamin | 5 | 230 | sale-collectie |  |
| 2026-09-04 vr 00:58 | US-01 - do 3 sept 09:00 ET - Labor Day Sale Live | THE LABOR DAY IS COMING CLOSER | US | Alle (VJkN42) | **tekst** | 56.147 | 34,4% | 0,47% | 0,02% | $2.374 | **0,042** | 0,49% | 0,052% | nee | Benjamin | 7 | 215 | sale-collectie |  |
| 2026-09-05 za 17:36 | 09/05 Dishwasher Plastic on your plates | There's plastic on your dinner plate right now | mix | Kopers (U5Ksvk) | **tekst** | 37.760 | 40,2% | 0,78% | 0,07% | $3.831 | **0,102** | 0,46% | 0,019% | nee | Benjamin | 3 | 119 | dishwashing-detergent- | content |
| 2026-09-05 za 17:55 | 09/05 September is hard | I did something I shouldn't have | mix | Alle (Uw8eZG) | **tekst** | 92.779 | 31,2% | 0,75% | 0,05% | $11.914 | **0,128** | 0,45% | 0,027% | nee | Benjamin | 4 | 253 | pan-pro-standard |  |
| 2026-09-07 ma 14:20 | 09/07 Labour Day Sale | 144 years. That's how long people have fought for this day. | US | Alle (VJkN42) | **tekst** | 53.278 | 30,6% | 0,34% | 0,04% | $5.704 | **0,107** | 0,36% | 0,058% | nee | Benjamin | 6 | 239 | sale-collectie | A/B, totaal |
| 2026-09-08 di 18:14 | 09/08 US EXCLUSION SALE DAY | 50% OFF, 4 Free Gifts, Last Hours. Then Nothing. | US | Alle (Uw8eZG) | **tekst** | 71.263 | 33,1% | 0,83% | 0,04% | $6.889 | **0,097** | 0,45% | 0,028% | ja | Benjamin | 7 | 228 | pan-pro-standard-4 |  |
| 2026-09-11 vr 16:00 | HS September Email 1: Warehouse Clearance Sale · 09.11.2026 | Warehouse Clearance Sale: Up to 58% Off | INT | Alle (ShPpDV+U5Ksvk+Uw8eZG+VJkN42) | **single-hero** | 124.437 | 36,8% | 1,25% | 0,05% | $15.388 | **0,124** | 0,38% | 0,033% | ja | merk | 5 | 7 | sale-collectie |  |
| 2026-09-12 za 08:00 | HS September Email 2: Warehouse Clearance Sale , Bundle Spotlight (US  | A whole kitchen set up in one easy click | US | E180 (UmXcLi+Vnb28D+XHT3z5) | **grid** | 21.957 | 41,4% | 0,70% | 0,04% | $1.262 | **0,058** | 0,36% | 0,046% | nee | merk | 7 | 7 | 6-delig |  |
| 2026-09-12 za 08:00 | HS September Email 2: Warehouse Clearance Sale , Bundle Spotlight (INT | A whole kitchen set up in one easy click | INT | E180 (UmXcLi+Vnb28D+XHT3z5) | **grid** | 18.293 | 44,4% | 0,87% | 0,02% | $1.275 | **0,070** | 0,40% | 0,044% | nee | merk | 7 | 7 | 6-delig |  |
| 2026-09-13 zo 14:00 | HS September Email 3: Dishwasher-Safe & Easy Cleanup · 09.13.2026 | Non-toxic cookware AND dishwasher safe? | mix | E180 (U5Ksvk+XHT3z5) | **tekst** | 63.695 | 47,2% | 0,69% | 0,03% | $3.134 | **0,049** | 0,48% | 0,042% | nee | Benjamin | 8 | 553 | dishwashing-detergent- | content |
| 2026-09-13 zo 14:00 | HS September Email 4: Accessory Push · 09.13.2026 | Your kitchen is *almost* ready | mix | Kopers (UfyDPs+Vnb28D+WwHjkS) | **grid** | 5.006 | 45,9% | 1,34% | 0,04% | $59 | **0,012** | 0,92% | 0,000% | nee | merk | 8 | 7 | sale-collectie |  |
| 2026-09-15 di 16:00 | HS Email 5: Warehouse Clearance Sale , Don't Miss It · 09.15.2026 | Still here (for now), still up to 50% off | INT | Alle (ShPpDV+U5Ksvk+Uw8eZG+VJkN42) | **single-hero** | 139.449 | 34,3% | 0,68% | 0,02% | $10.130 | **0,073** | 0,35% | 0,032% | ja | merk | 3 | 7 | sale-collectie |  |
| 2026-09-17 do 17:00 | HS September Email 6: Sweater Weather: Fall Kitchen Refresh · 09.17.20 | So long, summer ☀️ | INT | Alle (ShPpDV+U5Ksvk+Uw8eZG+VJkN42) | **single-hero** | 125.188 | 36,2% | 0,37% | 0,02% | $6.806 | **0,054** | 0,34% | 0,039% | nee, emoji | merk | 7 | 7 | sale-collectie | content |
| 2026-09-18 vr 18:15 | HS September Email 7: Net New Dishwasher Focus · 09.18.2026 | Put it in the dishwasher. Yes, really. | mix | E180 (XHT3z5) | **single-hero** | 53.240 | 44,4% | 0,63% | 0,04% | $4.881 | **0,092** | 0,38% | 0,038% | nee | merk | 12 | 5 | sale-collectie | content |
| 2026-09-19 za 14:00 | HS September Email 8: Roasting Pan Teaser · 09.19.2026 | Something's coming to your oven 👀 | mix | E180 (U5Ksvk+XHT3z5) | **single-hero** | 41.217 | 40,9% | 0,77% | 0,02% | $1.107 | **0,027** | 0,43% | 0,041% | nee, emoji | merk | 7 | 5 | Roasting Pan | content |
| 2026-09-21 ma 16:00 | HS September Email 9: Roasting Pan Launch · 09.21.2026 | NEW IN: Titanium Hammered Roasting Pan | US | Alle (VJkN42) | **single-hero** | 61.616 | 34,1% | 0,41% | 0,02% | $2.853 | **0,046** | 0,27% | 0,045% | nee | merk | 9 | 5 | Roasting Pan |  |
| 2026-09-22 di 14:00 | HS September Email 10: Fall Menu · 09.22.2026 | Seasonal cooking done better | mix | E180 (XHT3z5) | **grid** | 30.262 | 42,2% | 0,40% | 0,03% | $1.632 | **0,054** | 0,38% | 0,046% | nee | merk | 12 | 5 | meerdere | content |
| 2026-09-25 vr 09:15 | Plain Text · Hammered Pan Pro 50% + 4 Free Gifts (One More Time) · 09. | I can't do this a third time | US | Alle (Uw8eZG) | **tekst** | 69.858 | 35,9% | 0,84% | 0,06% | $8.080 | **0,116** | 0,66% | 0,024% | nee | Benjamin | 5 | 292 | pan-pro-standard |  |
| 2026-09-25 vr 14:25 | HS September Email 12: Roasting Pan Follow-Up · 09.25.2026 | Be part of the roasting revolution 👀 | US | Alle (VJkN42) | **single-hero** | 62.238 | 33,2% | 0,22% | 0,02% | $2.063 | **0,033** | 0,27% | 0,047% | nee, emoji | merk | 9 | 5 | Roasting Pan |  |
| 2026-09-26 za 09:00 | HS September Email 13: This Week's Bestsellers · 09.26.2026 | What everyone’s buying this week 👀 | mix | E180 (XHT3z5) | **grid** | 48.519 | 44,7% | 0,51% | 0,04% | $3.453 | **0,071** | 0,47% | 0,047% | nee, emoji | merk | 11 | 5 | meerdere |  |
| 2026-09-29 di 11:03 | 09/05 September is hard / Resend to Non-Openers | I did something I shouldn't have | US | Resend (Tzy9Jq) | **tekst** | 17.336 | 10,8% | 0,36% | 0,02% | $674 | **0,039** | 0,31% | 0,029% | nee | Benjamin | 4 | 253 | pan-pro-standard |  |
| 2026-09-30 wo 08:15 | HS September Email 15: Warehouse Clearance Sale , Final Hours · 09.30. | Up to 50% off storewide ends tonight | mix | Alle (Uw8eZG) | **single-hero** | 116.433 | 34,9% | 0,65% | 0,05% | $11.827 | **0,102** | 0,34% | 0,048% | ja | merk | 9 | 5 | sale-collectie |  |
| 2026-10-01 do 08:00 | Founder Note Sale - Why is it getting difficult for us | Why is it getting difficult for us? | mix | E30 (TNdhKc) | **tekst** | 47.616 | 47,6% | 1,32% | 0,03% | $4.624 | **0,097** | 0,90% | 0,088% | nee | Benjamin | 3 | 176 | 6-delig |  |
| 2026-10-02 vr 14:48 | Prime Sale - US - Founder Note | Up to 70% off. Our biggest sale ever | US | Alle (VJkN42) | **tekst** | 66.134 | 35,8% | 0,40% | 0,02% | $4.944 | **0,075** | 0,31% | 0,044% | ja | Benjamin | 3 | 139 | 6-delig |  |
| 2026-10-03 za 08:15 | HS September Email 11: Holiday Gift Guide Teaser · 10.03.2026 · US | Our holiday gift guide drops soon! | US | Alle (X2p52X) | **single-hero** | 77.364 | 32,6% | 0,30% | 0,02% | $2.629 | **0,034** | 0,35% | 0,070% | ja | merk | 5 | 5 | sale-collectie | content |
| 2026-10-03 za 08:30 | Prime Sale - INT (ex US) - Founder Note | [naam], 70% OFF + 4 GIFTS | INT | Alle (UbXDP6) | **tekst** | 73.409 | 39,9% | 1,41% | 0,07% | $10.739 | **0,146** | 0,54% | 0,053% | ja | Benjamin | 3 | 148 | 6-delig |  |
| 2026-10-03 za 22:42 | 6-piece set $349 - US - Lids on us | [naam], free lids (this won't last) | US | Alle (VJkN42) | **tekst** | 66.218 | 39,5% | 0,39% | 0,03% | $6.448 | **0,097** | 0,39% | 0,050% | ja | Benjamin | 6 | 169 | 6-delig | A/B, totaal |
| 2026-10-04 zo 10:00 | Sunday Recipe Day / 30 Days Engaged | ONE POT CACIO E PEPE 🍝 | mix | Alle (Uw8eZG) | **single-hero** | 134.477 | 34,4% | 0,30% | 0,02% | $6.778 | **0,050** | 0,35% | 0,058% | nee, emoji | merk | 6 | 7 | pan-pro-standard | content |
| 2026-10-06 di 08:45 | HS October Email 2: Sale Launch , 4 Gifts With Every Order · 10.06.202 | 4 FREE gifts + Up to 70% off 🎁 | mix | Alle (Uw8eZG) | **single-hero** | 111.630 | 35,8% | 0,49% | 0,03% | $6.351 | **0,057** | 0,30% | 0,037% | ja, emoji | merk | 16 | 5 | sale-collectie |  |
| 2026-10-06 di 21:00 | ALI FOUNDER EMAIL PRIME | PRIME SALE 70% off our #1 pan (ends tonight) | mix | Alle (Uw8eZG) | **tekst** | 45.413 | 33,1% | 1,09% | 0,05% | $5.022 | **0,111** | 0,39% | 0,057% | ja | Benjamin | 7 | 226 | pan-pro-standard | A/B, totaal |
| 2026-10-08 do 09:15 | HS October Email 1: Non-Toxic Origin , Plain-Text Founder · 10.03.2026 | The pan nobody else was making | mix | E180 (W5PSSp) | **tekst** | 60.790 | 41,9% | 0,82% | 0,03% | $4.677 | **0,077** | 0,40% | 0,025% | nee | Benjamin | 2 | 156 | sale-collectie | content |
| 2026-10-09 vr 08:30 | Floris / 9 October / Recipe / USA Only | Friday steak night recipe, sauce included | US | E90 (VNX8N9) | **hybride** | 26.575 | 39,5% | 0,30% | 0,03% | $1.504 | **0,057** | 0,41% | 0,023% | nee | Benjamin | 15 | 530 | pan-pro-standard | content |
| 2026-10-10 za 08:15 | HS October Email 3: Sale Midweek · 10.10.2026 | Still live: 4 gifts + Up to 50% off ❗ | mix | E180 (W5PSSp) | **single-hero** | 115.657 | 38,4% | 0,43% | 0,02% | $4.505 | **0,039** | 0,30% | 0,047% | ja, emoji | merk | 11 | 5 | sale-collectie |  |
| 2026-10-11 zo 08:15 | HS October Email 5: The Video Send , Non-Toxic in Action · 10.11.2026 | The egg test 🍳 | mix | E180 (W5PSSp) | **single-hero** | 118.043 | 38,1% | 0,78% | 0,02% | $5.306 | **0,045** | 0,28% | 0,039% | nee, emoji | merk | 8 | 5 | sale-collectie | content |
| 2026-10-12 ma 08:15 | HS October  Email 4: Sale Push (Plain Text) · 10.12.2026 | Up to 50% off + a note from Benjamin | mix | E180 (W5PSSp) | **tekst** | 118.458 | 39,9% | 0,46% | 0,04% | $8.796 | **0,074** | 0,47% | 0,042% | ja | Benjamin | 3 | 144 | sale-collectie |  |
| 2026-10-14 wo 08:15 | HS October Email 6: 5-Star Cookware for a 5-Star Experience · 10.14.20 | They switched. Here’s what they said. | INT | Alle (TNdhKc+U5Ksvk+UbXDP6) | **tekst** | 58.191 | 40,8% | 0,50% | 0,04% | $3.941 | **0,068** | 0,76% | 0,028% | nee | Benjamin | 2 | 172 | sale-collectie | content |
| 2026-10-16 vr 18:15 | HS October Email 13: Bundle Push , 3 Pans + 3 Lids at $299 · 10.16.202 | A PFAS-free kitchen for $299 | US | Alle (VJkN42) | **single-hero** | 64.488 | 32,1% | 0,27% | 0,01% | $2.631 | **0,041** | 0,29% | 0,029% | ja | merk | 10 | 5 | 6-delig |  |
| 2026-10-17 za 07:00 | HS October Email 7: The Cutting Board, Plastic-Free · 10.17.2026 | Is your cutting board non-toxic? | mix | E90 (VKxqyA+YnvTfr) | **single-hero** | 80.498 | 40,8% | 0,53% | 0,05% | $7.051 | **0,088** | 0,48% | 0,047% | nee | merk | 10 | 5 | titanium-cutting-board | content |
| 2026-10-20 di 08:15 | HS October Email 8: The Dishwasher Sheets Push · 10.20.2026 | What's in your dishwasher detergent? | mix | E90 (U5Ksvk+VKxqyA) | **single-hero** | 65.311 | 37,9% | 0,35% | 0,04% | $4.882 | **0,075** | 0,54% | 0,046% | nee | merk | 11 | 5 | dishwashing-detergent- | content |
| 2026-10-23 vr 08:15 | HS October Email 9: Bundle Upgrade · 10.23.2026 · A | Your PFAS-free kitchen starts here | mix | E90 (U5Ksvk+Uiyqhq) | **single-hero** | 46.225 | 41,5% | 0,63% | 0,05% | $7.763 | **0,168** | 0,50% | 0,030% | ja | merk | 11 | 5 | 6-delig |  |
| 2026-10-25 zo 08:15 | HS October Email 10: The Roasting Pan + Sale (Plain Text) · 10.25.2026 | A note on the non-toxic roasting pan | mix | E90 (VKxqyA+WHeYpt) | **tekst** | 48.877 | 41,8% | 0,83% | 0,07% | $8.340 | **0,171** | 0,48% | 0,035% | nee | Benjamin | 2 | 140 | Roasting Pan |  |
| 2026-10-27 di 08:15 | HS October Email 11: Late-Month Sale Push (Plain Text) · 10.27.2026 | The October sale ends this week | mix | E90 (VKxqyA) | **tekst** | 83.306 | 42,0% | 0,70% | 0,07% | $12.899 | **0,155** | 0,57% | 0,028% | ja | Benjamin | 2 | 114 | sale-collectie |  |
| 2026-10-31 za 08:15 | HS October Email 12: Halloween , Black Friday Early Access · 10.31.202 | The October sale ENDS TONIGHT ⏰ | mix | E90 (VKxqyA) | **single-hero** | 84.564 | 41,9% | 0,82% | 0,05% | $13.979 | **0,165** | 0,46% | 0,038% | ja | merk | 12 | 5 | sale-collectie |  |
| 2026-11-01 zo 08:15 | HS November Email 1: Black Friday Prices Start Today · 11.01.2026 · IN | Black Friday Savings Start Today | INT | Alle (UbXDP6) | **single-hero** | 75.034 | 39,3% | 0,89% | 0,04% | $7.417 | **0,099** | 0,44% | 0,025% | nee | merk | 10 | 5 | 6-delig |  |
| 2026-11-01 zo 08:15 | HS November Email 1: Black Friday Prices Start Today · 11.01.2026 · US | Black Friday Savings Start Today | US | Alle (VJkN42) | **single-hero** | 74.434 | 36,8% | 0,59% | 0,04% | $7.583 | **0,102** | 0,36% | 0,022% | nee | merk | 10 | 5 | 12-delig |  |
| 2026-11-02 ma 09:00 | SK · Roasting Pan INT launch · New in stock + BF special · 11.04.2026  | New in. Already 70% off. | INT | Alle (VbcqPX) | **hybride** | 73.390 | 40,2% | 0,80% | 0,04% | $6.462 | **0,088** | 0,30% | 0,019% | ja | merk | 12 | 282 | Roasting Pan |  |
| 2026-11-03 di 08:15 | HS November Email 2: Weekly Recipe: A Weeknight Dinner From Our Kitche | What I cooked last Tuesday | US | E180 (TntB6g) | **tekst** | 67.688 | 42,5% | 0,25% | 0,02% | $5.902 | **0,087** | 0,36% | 0,027% | nee | Benjamin | 2 | 177 | 12-delig | content |
| 2026-11-03 di 08:15 | HS November Email 2: Weekly Recipe: A Weeknight Dinner From Our Kitche | What I cooked last Tuesday | INT | E180 (S9BZVJ) | **tekst** | 52.831 | 47,5% | 0,34% | 0,04% | $4.896 | **0,093** | 0,50% | 0,015% | nee | Benjamin | 2 | 171 | 6-delig | content |
| 2026-11-04 wo 09:00 | SK · Win Your Order Back · 1 order refunded today · 11.04.2026 · US | Win your order back (today only) | US | E90 (VMjhb2) | **grid** | 74.697 | 44,5% | 0,82% | 0,08% | $13.496 | **0,181** | 0,29% | 0,029% | nee | merk | 22 | 202 | 12-delig |  |
| 2026-11-04 wo 09:00 | SK · Win Your Order Back · 1 order refunded today · 11.04.2026 · INTL | Win your order back (today only) | INT | E90 (XrFa5r) | **grid** | 52.047 | 52,4% | 1,19% | 0,04% | $4.008 | **0,077** | 0,29% | 0,015% | nee | merk | 22 | 195 | 6-delig |  |
| 2026-11-05 do 08:15 | HS November Email 3: November Sale Push 1: The Set Your Kitchen Starts | Replace the whole drawer in one order! | US | E90 (UmXcLi+VMjhb2) | **single-hero** | 72.534 | 46,8% | 0,52% | 0,03% | $8.554 | **0,118** | 0,46% | 0,030% | nee | merk | 9 | 5 | 12-delig |  |
| 2026-11-05 do 08:15 | HS November Email 3: November Sale Push 1: The Set Your Kitchen Starts | Replace the whole drawer in one order! | INT | E90 (XrFa5r) | **single-hero** | 49.206 | 52,6% | 0,61% | 0,05% | $5.589 | **0,114** | 0,47% | 0,018% | nee | merk | 9 | 5 | 6-delig |  |
| 2026-11-06 vr 18:07 | 2 Pans + 2 Lids · tekstbrief Benjamin · US · concept | I need to show you something | US | E90 (VMjhb2) | **tekst** | 76.794 | 49,4% | 0,64% | 0,07% | $12.631 | **0,165** | 0,63% | 0,043% | nee | Benjamin | 15 | 307 | 2-pans-and-2-lids |  |
| 2026-11-07 za 08:15 | HS November Email 4: The Thanksgiving Pans at Black Friday Prices · 11 | Up to 70% OFF pans for Thanksgiving | US | E90 (VMjhb2) | **grid** | 73.289 | 46,9% | 0,63% | 0,06% | $15.055 | **0,205** | 0,40% | 0,034% | ja | merk | 12 | 5 | 12-delig |  |
| 2026-11-07 za 08:15 | HS November Email 4: The Thanksgiving Pans at Black Friday Prices · 11 | Up to 70% OFF pans for Thanksgiving | INT | E90 (XrFa5r) | **grid** | 51.371 | 54,4% | 0,74% | 0,06% | $5.952 | **0,116** | 0,41% | 0,035% | ja | merk | 12 | 5 | 6-delig |  |
| 2026-11-08 zo 10:00 | HS November Email 1: Black Friday Prices Start Today · 11.01.2026 · US | Still cooking on coated pans? | US | Resend (VVWCHc) | **single-hero** | 45.115 | 5,8% | 0,21% | 0,01% | $918 | **0,020** | 0,16% | 0,031% | nee | merk | 10 | 5 | 12-delig |  |
| 2026-11-08 zo 10:00 | HS RESEND 1 · November Email 1: Black Friday Prices Start Today · 11.0 | Still cooking on coated pans? | INT | Resend (Vikk4d) | **single-hero** | 43.726 | 6,8% | 0,32% | 0,01% | $2.045 | **0,047** | 0,35% | 0,005% | nee | merk | 10 | 5 | 6-delig |  |
| 2026-11-10 di 15:24 | E5 Thanksgiving prep plan · US · 2026-11-10 | Your Thanksgiving, in 3 days and 2 pans | US | E90 (VMjhb2) | **hybride** | 74.375 | 45,1% | 0,52% | 0,05% | $10.185 | **0,137** | 0,33% | 0,020% | nee | Benjamin | 24 | 549 | deep-pan-pro |  |
| 2026-11-11 wo 09:00 | E5 Thanksgiving prep plan · INT · 2026-11-10 | A big dinner, in 3 days and 2 pans | INT | E90 (XrFa5r) | **hybride** | 52.508 | 52,5% | 0,51% | 0,02% | $2.679 | **0,051** | 0,29% | 0,023% | nee | Benjamin | 24 | 530 | deep-pan-pro |  |
| 2026-11-11 wo 19:00 | E6 Founder letter · US · 2026-11-11 | December 20, 2024 | US | E90 (VMjhb2) | **hybride** | 81.256 | 46,6% | 1,01% | 0,05% | $9.035 | **0,111** | 0,48% | 0,060% | nee | Benjamin | 15 | 233 | pan-pro-standard |  |
| 2026-11-12 do 08:15 | E6 Founder letter · INT · 2026-11-11 | December 20, 2024 | INT | E90 (XrFa5r) | **hybride** | 52.694 | 55,2% | 1,28% | 0,07% | $8.194 | **0,156** | 0,44% | 0,025% | nee | Benjamin | 14 | 211 | pan-pro-standard |  |
| 2026-11-13 vr 16:10 | F13 Lucky Friday · US · 2026-11-13 | I made Friday the 13th your lucky day 🍀 | US | E90 (VMjhb2) | **tekst** | 73.428 | 47,7% | 0,52% | 0,09% | $18.156 | **0,247** | 0,44% | 0,042% | nee, emoji | Benjamin | 5 | 260 | 12-delig |  |
| 2026-11-14 za 08:15 | HS November Email 7: November Sale Push 2: Free Gifts With Every Order | Every order ships with FREE gifts | US | E180 (TntB6g+U5Ksvk) | **grid** | 99.306 | 38,0% | 0,55% | 0,07% | $22.099 | **0,223** | 0,39% | 0,046% | ja | merk | 11 | 5 | 12-delig |  |
| 2026-11-14 za 08:15 | HS November Email 7: November Sale Push 2: Free Gifts With Every Order | Every order ships with FREE gifts | INT | E180 (S9BZVJ+U5Ksvk) | **grid** | 62.702 | 44,8% | 0,49% | 0,03% | $4.114 | **0,066** | 0,42% | 0,019% | ja | merk | 11 | 5 | 6-delig |  |
| 2026-11-15 zo 10:00 | HS November Resend 2: November Sale Push 2 (Non-Openers) · 11.15.2026  | FREE gifts are still waiting for you | US | Resend (TuVuqV) | **grid** | 72.527 | 24,6% | 0,30% | 0,01% | $2.946 | **0,041** | 0,27% | 0,028% | ja | merk | 11 | 5 | 12-delig |  |
| 2026-11-15 zo 10:00 | HS November Resend 2: November Sale Push 2 (Non-Openers) · 11.15.2026  | FREE gifts are still waiting for you | INT | Resend (TEbZ7H) | **grid** | 40.869 | 24,1% | 0,38% | 0,01% | $1.238 | **0,030** | 0,32% | 0,022% | ja | merk | 11 | 5 | 6-delig |  |
| 2026-11-16 ma 17:18 | Thanksgiving Roast · US · 2026-11-17 | 15% off the roasting pan, before Thanksgiving | US | E90 (VMjhb2) | **hybride** | 75.518 | 44,2% | 0,15% | 0,02% | $4.037 | **0,053** | 0,22% | 0,041% | ja | Benjamin | 23 | 330 | Roasting Pan |  |
| 2026-11-17 di 08:15 | HS November Email 8: Weekly Recipe: The Thanksgiving Main · 11.17.2026 | The main that frees up your oven | US | E180 (TntB6g) | **tekst** | 100.528 | 39,5% | 0,42% | 0,03% | $4.351 | **0,043** | 0,46% | 0,030% | ja | Benjamin | 3 | 189 | 12-delig | content |
| 2026-11-17 di 08:15 | HS November Email 8: Weekly Recipe: The Thanksgiving Main · 11.17.2026 | The main that frees up your oven | INT | E180 (S9BZVJ) | **tekst** | 55.275 | 44,6% | 0,45% | 0,02% | $1.531 | **0,028** | 0,49% | 0,014% | ja | Benjamin | 3 | 179 | 6-delig | content |
| 2026-11-18 wo 08:15 | HS November Email 9: Before the Rush: A Note From Benjamin · 11.18.202 | No need to wait for Black Friday | US | E90 (VMjhb2) | **tekst** | 88.240 | 46,1% | 0,64% | 0,06% | $14.875 | **0,169** | 0,56% | 0,041% | nee | Benjamin | 2 | 95 | 12-delig |  |
| 2026-11-18 wo 08:15 | HS November Email 9: Before the Rush: A Note From Benjamin · 11.18.202 | No need to wait for Black Friday | INT | E90 (XrFa5r) | **tekst** | 48.820 | 50,4% | 0,78% | 0,05% | $5.667 | **0,116** | 0,51% | 0,002% | nee | Benjamin | 2 | 85 | 6-delig |  |
| 2026-11-20 vr 09:00 | Selling out before Black Friday | ⚠️ Selling out before Black Friday | US | E90 (VMjhb2) | **tekst** | 86.509 | 44,0% | 0,63% | 0,06% | $15.843 | **0,183** | 0,33% | 0,042% | nee, emoji | merk | 4 | 214 | sale-collectie | A/B, totaal |
| 2026-11-21 za 08:15 | HS Email 10: The Black Friday Gift Guide: Who Gets Which Pan · 11.21.2 | The Gift Guide: Up to 70% OFF | US | E90 (VMjhb2) | **grid** | 96.653 | 43,4% | 0,75% | 0,08% | $18.744 | **0,194** | 0,51% | 0,032% | ja | merk | 13 | 5 | 12-delig |  |
| 2026-11-21 za 08:15 | HS Email 10: The Black Friday Gift Guide: Who Gets Which Pan · 11.21.2 | The Gift Guide: Up to 70% OFF | INT | E90 (XrFa5r) | **grid** | 53.651 | 51,3% | 0,73% | 0,07% | $10.060 | **0,188** | 0,49% | 0,011% | ja | merk | 13 | 5 | 6-delig |  |
| 2026-11-23 ma 08:15 | HS November Email 11: Black Friday Week Is Here · 11.23.2026 US | A Black Friday sale note from Benjamin | US | Alle (RNuYDm) | **tekst** | 111.736 | 35,4% | 0,39% | 0,06% | $22.846 | **0,205** | 0,47% | 0,036% | ja | Benjamin | 4 | 186 | 12-delig |  |
| 2026-11-23 ma 08:15 | HS November Email 11: Black Friday Week Is Here · 11.23.2026 INTL | A Black Friday sale note from Benjamin | INT | SMS (R5LmyU) | **tekst** | 3.634 | 41,0% | 1,65% | 0,14% | $1.318 | **0,363** | 1,07% | 0,055% | ja | Benjamin | 4 | 157 | 6-delig |  |
| 2026-11-24 di 22:00 | Most unique product · text only · US · 2026-11-24 | Claim your free titanium hammered pizza steel | US | E90 (VMjhb2) | **tekst** | 86.429 | 41,5% | 0,53% | 0,03% | $14.388 | **0,167** | 0,47% | 0,031% | ja | Benjamin | 4 | 282 | 12-delig |  |
| 2026-11-25 wo 10:00 | HS November Email 13: Still Deciding? Black Friday Prices Are On · 11. | Still deciding? 5 FREE gifts await | US | Intent (T3EWq6+VprSf5) | **single-hero** | 37.332 | 31,0% | 0,82% | 0,07% | $9.736 | **0,261** | 0,45% | 0,029% | ja | merk | 11 | 5 | 12-delig |  |
| 2026-11-25 wo 10:00 | HS November Email 13: Still Deciding? Black Friday Prices Are On · 11. | Still deciding? 5 FREE gifts await | INT | Intent (TvUeki+XrwgLh) | **single-hero** | 10.098 | 39,0% | 1,57% | 0,08% | $1.373 | **0,136** | 0,83% | 0,040% | ja | merk | 11 | 5 | 6-delig |  |
| 2026-11-26 do 08:15 | Thanksgiving x Black Friday · US · 2026-11-26 | 🦃 Happy Thanksgiving (+ an extra 10% off) | US | E90 (VMjhb2) | **hybride** | 78.399 | 16,9% | 0,25% | 0,02% | $4.393 | **0,056** | 0,13% | 0,013% | ja, emoji | Benjamin | 12 | 229 | sale-collectie | loopt nog (uren oud) |
| 2026-11-26 do 08:15 | As seen in Bon Appétit · INTL · 2026-11-26 | As seen in Bon Appétit (+ an extra 10% off) | INT | Alle (VdfJTJ) | **hybride** | 58.782 | 25,0% | 0,35% | 0,02% | $2.573 | **0,044** | 0,26% | 0,009% | ja | Benjamin | 12 | 265 | sale-collectie | loopt nog (uren oud) |
