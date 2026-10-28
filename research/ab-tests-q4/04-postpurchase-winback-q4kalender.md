# A/B-tests Q4 · 04 · Post-purchase, winback, failure to launch, sunset en de Q4-kalender voor alle flows

Datum: 28 oktober 2026. Een van vier agents die de Q4-tests voorbereiden. Dit stuk dekt v4 · Post-purchase (`X3ySuU`), v4 · Post-purchase · levering (`VQ93sx`), EB | Customer Winback (`UEfh4h`, plus v4 · Winback `UyFc78`), EB | Failure to launch (`T2SmtR`), v4 · Sunset (`TbYQmX`, plus Sunset · kept `Wzz6xC`) en het overkoepelende plan voor alle flows van 29 oktober tot en met Cyber Monday 30 november.

Alles alleen gelezen in Klaviyo (account TdtTzz, revision 2025-10-15): flowdefinities, `POST /api/flow-values-reports` per bericht (14 okt 00:00 tot 28 okt 00:00 UTC, conversie Placed Order `RSNxYV`), `POST /api/metric-aggregates` (Received Email `YkRM4Q` per `$flow` per dag, Placed Order op `$attributed_flow`, Delivered Shipment `VcUF33`, Fulfilled Order `VtEiZT`, Postflows `UabgWz`), segmentgroottes en één campaign-values-report. Niets gewijzigd, niets verstuurd. Alleen aggregaten, geen profieldata. Rekenwerk in de scratchpad (`q4/`).

Regels (PLAYBOOK 6 en `research/flows-audit/2026-10-19-ab-tests.md`): één variabele per test, winnaar op unieke kliks (Bot Click uit) met omzet per ontvanger als controle, minimaal vier weken, geen automatische winnaar, maximaal 2 tests per flow, bij twijfel wint A. Power: 80 procent, 5 procent tweezijdig, 50/50 tenzij anders vermeld.

---

## 0. Samenvatting voor Floris

1. **Post-purchase is nu de beste naflow, maar mist volume.** X3ySuU plus levering: 4.399 mails, $4.673, **$1,06 per ontvanger** in 14 dagen. P1-REPEAT haalt $4,31 per ontvanger, P1-FIRST $0,86, P2 $1,19. P3 (dag 21, cross-sell met de T02-codetest) stuurt vanaf 29 of 30 oktober, precies op Halloween 70%.
2. **Er loopt geen enkele A/B-test in deze vijf flows**, alleen T02 (code tegen geen code) op P3 en R2, en een vergeten 50/50-wachttijdsplit (1 tegen 2 dagen) in de oude winback. De P1-dekselkaart (T15) en het affiliate-blok in P1 zijn nog niet gestart.
3. **Bezorgsignaal valt weg.** Delivered Shipment zakte van ~150 naar ~50 per dag terwijl orders stegen naar 250 tot 330 per dag; Postflows (trigger affiliate S1) van ~330 naar ~40. Daardoor kreeg P2 nog maar ~30 per dag en affiliate A1 maar 36 mails in 14 dagen. Fulfilled Order komt in golven (822 op 24 okt). Eerst laten nagaan of dit een fulfillment-achterstand of een kapotte koppeling is.
4. **Top 3 voor BFCM** (verwachte extra omzet per week in de BFCM-weken): (1) BFCM-kopersreeks naar eerdere kopers met holdout, $1.500 tot $4.000; (2) post-purchase herinstap 30 naar 7 dagen zodat herhaalkopers P1-REPEAT krijgen, $900 tot $1.800; (3) P1-FIRST met dekselkaart (T15), $450 tot $900.
5. **Failure to launch en sunset leveren vrijwel niets op** ($0,012 en $0,036 per ontvanger). FTL: 6 nulmails op Draft vóór 1 november. Sunset: niet uit, wel Smart Sending aan, pauze van 13 november tot en met 1 december, en de suppressiestap bouwen voor een start op 2 december in porties met 10 procent controle.
6. **Bevriezing 20 november tot en met 1 december**: geen nieuwe tests, geen templatewissels, lopende tests door maar BFCM-dagen apart rapporteren. Laatste startdatum voor een test die vóór de bevriezing iets moet laten zien: 1 november.

---

## 1. Per mail: de afgelopen 14 dagen (14 tot 28 okt 2026) en de stand van tests

Klik = unieke klik per ontvanger (Klaviyo-rapport, bots niet apart gefilterd). Omzet = Klaviyo-toeschrijving op Placed Order. Per dag = ontvangers / 14.

### 1.1 v4 · Post-purchase `X3ySuU` (trigger Placed Order, herinstap 30 dagen)

| Mail | Moment | Ontv. | Per dag | Klik | Orders | Omzet | Per ontv. | Uitschr. | Spam | Test |
|---|---|---|---|---|---|---|---|---|---|---|
| P1-FIRST `R3gbkQ` | 1 uur, eerste order | 2.749 | 196 | 7,24% | 13 | $2.366 | $0,86 | 0,36% | 0 | geen. T15 dekselkaart gepland, niet gestart. Affiliate-blok klaar als `TVFnbF`, niet gekoppeld |
| P1-REPEAT `WqxPSh` | 1 uur, herhaalorder | 303 | 22 | 5,30% | 5 | $1.301 | **$4,31** | 0% | 0 | geen. Affiliate-blok klaar als `Rwes4z`, niet gekoppeld |
| P2-SAFE `TZ6TKb` | dag 17, pan zonder Delivered | 497 | (start ~25 okt, ~170) | 5,85% | 0 | $0 | $0 | 0,60% | 0 | geen |
| P3 (12 mails, SET, PAN, NEXT, ACCESSORY, APRON) | dag 21 | 0 | eerste mails ~29 tot 30 okt | | | | | | | **T02 live** (split `119850559`, 50% eigen code tegen 50% geen code; cooldown-tak zonder code) |
| **Totaal X3ySuU** | | 3.549 | 254 | | 18 | $3.667 | $1,03 | | | |

Metric-aggregates bevestigen: 20 orders, $3.720 toegeschreven aan X3ySuU. Ontvangers per dag stegen van ~150 naar ~450 in de laatste drie dagen (P2-SAFE start, meer orders).

### 1.2 v4 · Post-purchase · levering `VQ93sx` (trigger Delivered Shipment)

| Mail | Moment | Ontv. | Per dag | Klik | Orders | Omzet | Per ontv. | Uitschr. | Test |
|---|---|---|---|---|---|---|---|---|---|
| P2 `RCgdNW` | bezorging + 1 dag 09:00 | 850 | 61 (van 154 naar 30) | 5,55% | 7 | $1.006 | $1,19 | 0,24% | geen |

Delivered Shipment per dag (8 tot 27 okt): 157, 147, 105, 15, 95, 212, 160, 144, 124, 83, 49, 112, 63, 43, 47, 56, 57, 34, 51, 47. Fulfilled Order: 246, 203, 92, 7, 12, 137, 44, 56, 22, 16, 1, 39, 52, 10, 54, 21, **822**, 46, 25, 188. Orders liepen in dezelfde weken op van 173 naar 333 per dag. P2-SAFE (dag 17) vangt pankopers zonder Delivered op; review (`TvfJYU`, Fulfilled + 21) en affiliate S1 (`R22pzb`, Postflows) hebben geen dag-17-vangnet.

### 1.3 EB | Customer Winback `UEfh4h` (oud, loopt tot 14 dec; Placed Order + 60 dagen; Smart Sending uit)

| Mail | Moment | Ontv. | Per dag | Klik | Orders | Omzet | Per ontv. | Uitschr. | Test |
|---|---|---|---|---|---|---|---|---|---|
| Email #1 `Wrnas5` "Serving Up New Must-Haves" | dag 60 | 2.210 | 158 | 0,59% | 0 | $0 | $0 | 0,45% | |
| Email #2 `XWQLLB` "We Cut a Deal for You" | +2 dagen (arm A) | 1.102 | 79 | 0,73% | 1 | $145 | $0,13 | 0,27% | **oude 50/50-split `81062241`** (2 tegen 1 dag), geen einddatum, geen eigenaar |
| Copy of Email #2 `WW78hc` | +1 dag (arm B) | 1.114 | 80 | 0,63% | 1 | $104 | $0,09 | 0,72% | idem |
| Email #3 `WC4V9Y` "10% Off Expires Tonight" | +1 dag | 2.164 | 155 | 0,23% | 3 | $361 | $0,17 | 0,56% | |
| **Totaal** | | 6.590 | 471 | | 5 | $610 | **$0,09** | 0,50% | |

Alle vier de mails dragen nog de banner "PRIME TIME / 56%" (audit 4.14) en mail 3 belooft "10% off" naast een sale van 50 en straks 70 procent. Filters: geen order na 9 okt, nooit in v4 · Winback.

**v4 · Winback `UyFc78`**: 0 mails. Eerste R1 rond 23 november (orders van 9 okt + 45 dagen), dus midden in de BFCM-week. R2 (T02 live, splits `119850731` en `119850729`) vanaf eind december.

### 1.4 EB | Failure to launch `T2SmtR` (lijst `Uw8eZG` + 30 dagen, 10 mails, Smart Sending aan)

| Mail | Ontv. | Klik | Orders | Omzet | Uitschr. | Spam | Oordeel |
|---|---|---|---|---|---|---|---|
| Bestsellers + Product Reviews `S6wMyn` | 4.384 | 0,21% | 1 | $63 | 0,46% | 0 | Draft |
| Healthy Habits Start Here `U6PsqR` | 4.137 | 0,36% | 0 | $0 | 0,51% | 1 | Draft |
| FAQ's `RifeeX` | 4.284 | 0,23% | 0 | $0 | 0,35% | 0 | Draft |
| Titanium vs Non-Stick `WFwksy` | 4.206 | 0,43% | 1 | $129 | 0,41% | 1 | houden |
| How to Store + Care `WFZ9ka` | 3.993 | 0,30% | 1 | $160 | 0,43% | 0 | houden |
| Titanium Vs Stainless Steel `RA3fUx` | 4.016 | 0,43% | 1 | $144 | 0,55% | 3 | houden |
| Micro-Plastic Free `RgzVJY` | 3.879 | 0,10% | 0 | $0 | 0,39% | 1 | houden (19 okt deed hij $161), banner eruit |
| Titanium Care `WwCjFD` | 3.816 | 0,26% | 0 | $0 | 0,37% | 1 | Draft |
| Ceramic VS Titanium `S5P3Wn` | 3.803 | 0,40% | 0 | $0 | 0,21% | 2 | Draft |
| Review Focus `SmQwfi` | 3.574 | 0,28% | 0 | $0 | 0,34% | 2 | Draft |
| **Totaal** | **40.092** (2.864 per dag) | 0,30% | 5 | $496 | 0,40% (161) | 11 | **$0,012 per ontvanger** |

Geen test. Instroom: alleen wie na 30 dagen geen order en geen v4-W2 had. Sinds 19 okt staat welcome op 100% nieuw, dus de oude arm valt rond 18 tot 21 november weg en FTL zakt dan vanzelf, met een staart tot ~1 december. Kanttekening uit `afmeldingen/01-data.md`: de oude welcome-tak kreeg op 23 okt nog instroom, dus er blijft een restlek.

### 1.5 v4 · Sunset `TbYQmX` en Sunset · kept `Wzz6xC`

| Mail | Ontv. | Per dag | Klik | Orders | Omzet | Uitschr. | Spam | Test |
|---|---|---|---|---|---|---|---|---|
| S1 `UYqHSs` "Should we keep writing to you?" | 8.430 | 602 | 0,26% | 2 | $597 | 0,77% | 1 | geen |
| S2 `UTMtx4` "Last email from me (unless you tap)" | 8.043 | 575 | 0,32% | 0 | $0 | 0,47% | 3 | geen |
| S3 kept `SmGgU3` | 44 | 3 | 13,6% | 1 | $155 | 0% | 0 | geen |
| S4 kept `XJXVru` | 27 | 2 | 0% | 0 | $0 | 0% | 0 | geen |
| **Totaal sunset** | 16.544 (1.182 per dag) | | | 3 | $752 | 103 | 4 | **$0,045 per ontvanger** |

Segment `WuHSm6` telt nu 83.390 profielen. Smart Sending staat uit op S1 en S2. Na S2 gebeurt niets: geen suppressie, geen uitsluitingssegment (zie `afmeldingen/01-data.md`, sectie 2). Besluit over uitzetten ligt bij Floris.

### 1.6 Lopende of geplande zaken die deze flows raken

| Wat | Stand 28 okt | Raakt |
|---|---|---|
| Affiliate-blok P1 (`TVFnbF`, `Rwes4z`) | klaar in de bibliotheek, niet gekoppeld (P1-FIRST gebruikt nog `XhZ3Xr`) | P1-FIRST concurreert met T15 om hetzelfde testslot |
| Affiliate S1 `R22pzb` | live sinds 22 okt; A1 36 ontvangers in 14 dagen, 1 order ($104) | bereik hangt aan Postflows, dat nu wegvalt |
| Mystery Gift `YwsKcf` | live sinds 23 okt; M1 179 ontvangers, 3,35% klik, 2 uitschrijvingen (1,12%), M4 draft | M1 op dag 3 en P1 op 1 uur; M2 dag 12, M3 dag 23 valt naast P3 (dag 21). M1 slaat over bij een X3ySuU-mail binnen 2 dagen |
| Review `XzHrez` | A/B `119577637` live ("Win your purchase amount back" tegen "How was your experience?"); 468 ontvangers in 14 dagen, 3,21% klik | beslissen half januari, buiten dit plan |
| Review-vangnet `TvfJYU` | live, eerste mails vanaf ~9 nov (Fulfilled + 21) | in BFCM groot volume door de Fulfilled-golf van 24 okt |

---

## 2. Tests en ingrepen, gesorteerd op verwachte extra omzet per week

Bedragen zijn schattingen: ontvangers x omzet per ontvanger x realistische winst, voor nu en voor de BFCM-weken (2 tot 4 keer het volume, zie ab-tests 19 okt sectie 3). Niet optelbaar: overlap tussen 1, 2 en 4.

| # | Test of ingreep | Soort | Extra per week nu | Extra per week BFCM | API of UI | Klaar vóór BFCM |
|---|---|---|---|---|---|---|
| 1 | BFCM-kopersreeks met holdout | nieuwe reeks, holdout-test | n.v.t. | **$1.500 tot $4.000** | API (segment, lijst, campagnes als draft), versturen na akkoord | ja, als akkoord vóór 4 nov |
| 2 | Post-purchase herinstap 30 naar 7 dagen | ingreep | $300 tot $600 | **$900 tot $1.800** | UI (trigger-instelling) | ja, 5 minuten |
| 3 | T15 · P1-FIRST deksel- en setkaart | A/B | $180 tot $350 | $450 tot $900 | template via API, A/B starten alleen in UI | ja, start 1 nov |
| 4 | P3 in de sale (tweede aankoop dag 21) | ingreep plus T02-besluit | $150 tot $350 | $250 tot $700 | template via API, wissel in UI | ja, vóór 6 nov |
| 5 | Winback met de sale als haak | vaste wissel (A/B niet zinvol op dit volume) | $250 tot $500 | $300 tot $700 | template via API, wissel API of UI | ja, vóór 6 nov |
| 6 | Affiliate-oproep op het juiste moment | ingreep plus A/B na BFCM | $50 tot $150 | $100 tot $400 | API (template-swap is voorbereid) | deels |
| 7 | Failure to launch inkorten | ingreep | ~$0 (min $30 omzet, min 45 uitschrijvingen) | ~$0 | API of UI (status per mail) | ja, vóór 1 nov |
| 8 | Sunset: Smart Sending, pauze in BFCM, suppressie vanaf 2 dec met controle | ingreep plus holdout | $0 tot min $150 | $0 tot min $300 (bewust) | Smart Sending en status: UI; segment en property: deels API | ja (pauze), suppressie na BFCM |

### 2.1 BFCM-kopersreeks: heractivatie van eerdere kopers

| | |
|---|---|
| Hypothese | 100.295 kopers ooit, slechts 8.950 kochten twee keer. Kopers krijgen in BFCM dezelfde algemene campagnes als niet-kopers. Een mail die uitgaat van wat ze al hebben (pan zonder deksel: het deksel; één pan: de 6-delige set; set: accessoires) en de 70% als reden van nu, haalt meer tweede orders dan de algemene campagne op dezelfde dag. Het cohort van november 2025 (14.045 kopers) is in BFCM precies een jaar klant |
| Variabele | Mailen tegen niet mailen (holdout). De kopersmail vervangt op die dag de algemene HS-campagne voor deze groep, dus de vraag is: wat levert de kopersmail extra op bovenop alle andere kanalen |
| Opzet | Segment "Kopers · mailbaar · geen order 30 dagen" (~38.000; de buyers-campagne van 5 sep bereikte 37.760). Random 15% holdout als statische lijst (API: profielen toevoegen aan lijst). 3 mails: ~13 nov (aanloop, "what your pan is missing"), BF 27 nov, CM 30 nov. Inhoud per `siraat_owned`. Kalm-register mag hier luid worden (campagne), zelfde feitregels |
| Metric | Orders per profiel (alle kanalen) van 13 nov tot 7 dec, holdout tegen ontvangers; controle uitschrijving en spam per mail |
| Power | Bij 2 tot 3% kopers in de periode en 15% holdout: verschil van 22 tot 27% zichtbaar. Eén periode, geen herhaling nodig |
| Extra omzet | Basis buyers-campagne $0,10 per ontvanger (vaatwasstrips, 5 sep). Aanname BFCM-kopersmail $0,25 tot $0,50, waarvan $0,05 tot $0,15 boven de algemene mail. 3 mails x ~32.000 = **$5.000 tot $14.000 over BFCM, $1.500 tot $4.000 per week** |
| Risico | Middel. Kopers van oktober tegen 50% zien 70%: mail alleen naar "geen order 30 dagen". Prijsclaims alleen echte compare-at. Holdout kost een deel van de omzet bewust. Overlap met HS: de kopersmail vervangt, niet erbij |
| API of UI | API: segment (mag sinds 8 okt), holdoutlijst, templates en campagnes als draft. Versturen of inplannen pas na akkoord Floris |
| Klaar vóór BFCM | Ja, als Floris vóór 4 november akkoord geeft (bouw 3 mails plus QA ~3 dagen) |

Vijf onderwerpen (kopersmail 1, kalm met sale, skill sectie 5): "The lid your pan is missing" (curiosity + benefit) · "One year with your pan" (specificity, alleen cohort november 2025) · "Which lid fits your pan?" (vraag) · "\"I only need the new one.\"" (verhaal, alleen als review-check slaagt) · "70% off, for the pan you already love" (aanbod). Voor een A/B binnen de reeks: alleen in mail 1, eigendom-onderwerp tegen aanbod-onderwerp.

### 2.2 Post-purchase herinstap van 30 naar 7 dagen (audit uitbreiden, punt E)

| | |
|---|---|
| Hypothese | Wie binnen 30 dagen opnieuw bestelt, krijgt nu geen P1-REPEAT ($4,31 per ontvanger, de sterkste naflowmail). 12,7% van de orders had een order in de 30 dagen ervoor. Vanaf ~8 november valt de buffer van vóór de livegang weg, en in BFCM bestellen juist oktoberkopers opnieuw |
| Variabele | Bereik, geen A/B: herinstap 7 dagen; flowfilter "niet in deze flow in 7 dagen"; P2-SAFE (`119850554`) extra filter "geen P2 ontvangen in 30 dagen" |
| Metric | P1-REPEAT-ontvangers per dag en omzet per ontvanger, voor en na; controle uitschrijving en dubbele P2 |
| Power | Geen test. Voor/na-meting in de dagelijkse bewaking |
| Extra omzet | ~30 extra P1-REPEAT per dag nu, 60 tot 120 in BFCM, x $4,31 x 50% incrementeel = **$450 per week nu, $900 tot $1.800 in BFCM** |
| Risico | Laag. Kopers die twee keer in een week bestellen krijgen twee keer P1 (bewust, het is een bevestiging). P3 valt voor herhaalkopers toch weg door "geen order sinds start" |
| API of UI | UI. Herinstap is een trigger-instelling; het flowfilter kan via de API, maar live flows wijzigen we in de UI |
| Klaar vóór BFCM | Ja, kan morgen |

### 2.3 T15 · P1-FIRST met deksel- en setkaart

| | |
|---|---|
| Hypothese | P1 heeft de hoogste klik van alle flows (7,24%). De Lid Launch aan pankopers was de beste cross-sell ooit. Een zichtbare kaart met foto, prijs en knop direct onder de orderregels verkoopt meer deksels en sets in de week van de bestelling, zeker met 70% korting |
| Variabele | Vorm van de cross-sell: huidige dekselregel (A) tegen productkaart (B). Onderwerp, preview en de rest gelijk |
| B | Label "MADE FOR YOUR PAN", deksel op de pan, prijs alleen US, knop "Add the lid that fits my pan", eronder "Free shipping. 30-day returns. 100,000+ happy customers." (INT: "Free shipping, duties paid. 30-day returns. 100,000+ happy customers.") |
| Metric | Unieke klik; controle omzet per ontvanger en uitschrijving (nu 0,36%) |
| Power | 196 per dag: +30% in 26 dagen, MDE in 4 weken 29%. Bij 2,5 keer BFCM-volume: +20% in 22 dagen, MDE 18% |
| Extra omzet | 1.370 ontvangers per week x $0,86 x 15 tot 30% = $180 tot $350; BFCM 3.400 per week = $450 tot $900 |
| Risico | Laag tot middel: verkoopblok in een bevestiging. Bezet het enige testslot van P1-FIRST, dus het affiliate-blok gaat niet in P1-FIRST tot T15 beslist is |
| API of UI | Template bouwen en als bibliotheektemplate klaarzetten via API; A/B aanmaken en starten alleen in de UI (API kan een flow-A/B niet starten) |
| Klaar vóór BFCM | Ja: bouwen 29 tot 31 okt, start 1 nov, beslissen 7 dec op de dagen buiten 20 nov tot 1 dec |

### 2.4 P3 in de sale: tweede aankoop op dag 21

| | |
|---|---|
| Hypothese | P3 (set, pan, deksel, accessoire, schort) stuurt vanaf 29 oktober en valt daarmee volledig in Halloween 70% en BFCM. P3 noemt de sale nu niet. Een salerij met de echte prijs en echte einddatum maakt van "the pan your set is missing" een moment |
| Variabele | Ingreep: een salerij in alle P3-templates (codes en nocode gelijk). Geen A/B: de rij is ware informatie en P3 heeft al T02 |
| T02-besluit | Floris besloot 19 okt dat unieke codes mogen stapelen op 70%. Advies: T02 laten lopen tot 19 nov, van 20 nov tot en met 1 dec alle P3- en R2-splits op nocode (iedereen de gift-stack, geen extra 10% op 70%), daarna hervatten. Margebesluit [VRAAG FLORIS] |
| Metric | Omzet per ontvanger P3, voor (29 okt tot 5 nov) tegen na; klik als controle |
| Power | Als A/B op ~300 per dag in BFCM: +30% in 43 dagen. Te traag, daarom vaste wissel |
| Extra omzet | Aanname P3 $0,50 tot $0,70 per ontvanger (Lid Launch $0,69), salerij +30 tot 60%: 1.000 tot 2.500 ontvangers per week = $150 tot $350 nu, $250 tot $700 in BFCM |
| Risico | Middel: einddatums Halloween en BFCM nog niet bekend (DECISIONS 7 okt: geen harde datum tot Floris die geeft) [VRAAG FLORIS]. Zonder einddatum: "Sale price this week" niet gebruiken, alleen de prijs |
| API of UI | Templates via API; koppelen aan de flowacties via `PATCH /api/flow-actions` (zoals voorbereid voor P1) of in de UI |
| Klaar vóór BFCM | Ja, vóór 6 nov |

### 2.5 Winback met de sale als haak (`UEfh4h`, tot 14 dec)

| | |
|---|---|
| Hypothese | Winback doet $0,09 per ontvanger met 0,23 tot 0,73% klik. Mail 1 zegt "Serving Up New Must-Haves", mail 3 "10% Off Expires Tonight", alle vier met de verlopen 56%-banner. Een klant van 60 dagen terug die hoort dat zijn volgende pan of deksel nu 70% minder kost, klikt vaker dan op een 10%-code |
| Variabele | Inhoud van mail 1 en mail 3 (onderwerp plus hero met de sale als reden), mail 2 krijgt alleen de banner eruit |
| Waarom geen A/B | 158 per dag op 0,59% klik: MDE in 4 weken 143%, +100% vraagt ~50 dagen. Dus vaste wissel met voor/na-meting, en de oude 50/50-wachttijdsplit `81062241` op 100% (1 dag; geen verschil gemeten, $0,13 tegen $0,09) |
| Metric | Klik en omzet per ontvanger, 14 dagen voor tegen 14 dagen na, sale-dagen apart |
| Extra omzet | 3.300 mails per week x $0,08 tot $0,15 extra = $250 tot $500; in BFCM $300 tot $700 |
| Risico | Laag. Kalm register (flow). Alleen echte compare-at en echte einddatum. v4-winback R1 start ~23 nov midden in BF-week: R1 krijgt dezelfde salerij (zelfde ingreep, `UyFc78` acties `119850720` tot `119850723`) |
| API of UI | Templates via API, wissel via API of UI na akkoord |
| Klaar vóór BFCM | Ja, vóór 6 nov |

Vijf onderwerpen voor mail 1 (klant, kalm): "How's the pan treating you?" (vraag) · "The lid your pan was waiting for" (curiosity + benefit) · "70% off, for pan number two" (aanbod) · "Two months in. What's next?" (specificity) · "\"I only need the new one.\"" (verhaal, na review-check). Keuze: "70% off, for pan number two" voor mail 1, "How's the pan treating you?" blijft het v4-onderwerp van R1.

### 2.6 Affiliate-oproep op het juiste moment

| | |
|---|---|
| Hypothese | Iemand deelt zijn link als iemand naar de pan vraagt: na het eerste koken, niet in de bevestiging. Maar S1 hangt aan Postflows, dat nu ~40 per dag vuurt, dus het "juiste moment" bereikt bijna niemand |
| Ingreep nu | (a) P1-REPEAT krijgt het blok (`Rwes4z`, voorbereid; herhaalkopers zijn de beste ambassadeurs; geen test op P1-REPEAT). (b) P1-FIRST niet, want T15 bezet dat slot. (c) Postflows-gat laten uitzoeken (punt 0.3) |
| Test na BFCM | 7 dec: A/B op P2-SAFE (`119850554`, dag 17, pankopers zonder bezorgevent): met blok tegen zonder. Metric: klik op de deellink per ontvanger, controle P2-SAFE-klik en uitschrijving. Power: bij 1% deelklik en 170 per dag is +50% pas in ~90 dagen te zien; dit is een richtingtest |
| Waarom niet in BFCM | Vriendenkorting 15% naast 70% off: stapelt Snowball op de sale? [VRAAG FLORIS] Deals-kopers in BFCM delen eerder een saleprijs dan een link |
| Extra omzet | Referral-orders (na 15% korting en 15% commissie): $50 tot $150 per week nu, $100 tot $400 in BFCM via P1-REPEAT-volume |
| API of UI | API: `PATCH /api/flow-actions/119850552` met template `Rwes4z` (stappen in `klaviyo/flows/affiliate-system-v1.md` sectie 6). A/B in december alleen in de UI |
| Klaar vóór BFCM | P1-REPEAT ja; P2-SAFE-test nee (7 dec) |

### 2.7 Failure to launch inkorten

| | |
|---|---|
| Hypothese | 6 van de 10 mails brachten in 14 dagen samen $63 op 23.998 mails en 90 uitschrijvingen. De andere 4 dragen alle omzet. FTL heeft evenveel spamklachten als de hele welkomstflow (90 dagen). In BFCM bereiken de campagnes dezelfde mensen al |
| Ingreep | Bestsellers, Healthy Habits, FAQ's, Titanium Care, Ceramic VS Titanium, Review Focus op Draft (flow blijft live). In de 4 overblijvers de "PRIME TIME / 56%"-banner, "100-day" en "lifetime" eruit (audit 4.14) |
| Waarom geen test | Holdout op orders gaat niet: 5 toegeschreven orders op ~4.400 instromers in 14 dagen. Het verschil is al duidelijk |
| Metric | Mails, uitschrijvingen en spam per week voor/na; FTL-omzet blijft ~$480 per 14 dagen |
| Effect | Min ~1.700 mails per dag, min ~45 uitschrijvingen en ~3 spamklachten per week. Omzet ~$0 (min $30 per week) |
| Risico | Laag. Terugdraaien = status terug op Live |
| API of UI | API kan (status per flow-actie), anders 2 minuten UI. Bannerverwijdering: template-edit, UI of API |
| Klaar vóór BFCM | Ja, vóór 1 nov. FTL zakt daarna vanzelf rond 18 tot 21 nov (oude welcome-arm leeg) |

### 2.8 Sunset: niet uit, wel eerlijk, en suppressie na Cyber Monday

| | |
|---|---|
| Situatie | 1.182 mails per dag, $0,045 per ontvanger. S1 belooft "we'll stop writing in about a week", maar niemand wordt onderdrukt; in BFCM komen er dagelijks campagnes, dus de belofte breekt juist dan het hardst (klachtenrisico) |
| Ingreep vóór BFCM | (a) Smart Sending aan op S1 en S2 (nu uit). (b) Flow op pauze (manual) van 13 nov tot en met 1 dec, zodat niemand in die weken "last email" krijgt en daarna 10 BFCM-mails. (c) `WuHSm6` in BFCM maximaal 3 campagnes: BF-aankondiging, Black Friday, Cyber Monday, met Smart Sending aan |
| Na Cyber Monday (2 dec) | Stap 3 bouwen: split na S2 + 3 dagen op klik op de keep-knop (`utm_content` s1-cta1 of s2-cta1), sitebezoek of order; ja `sunset_status = kept`, nee `sunset_status = suppressed`; segment "v4 · Sunset · suppressed" uitsluiten in alle campagnes. Daarna de 83.000 bestaande leden in porties van 10.000 per week, elke portie met 10% controle die campagnes blijft krijgen |
| Metric | Per portie na 30 dagen: omzet per profiel, uitschrijving en spam, controle tegen gesuppresseerd |
| Power | Portie van 10.000 met 1.000 controle: bij $0,55 omzet per profiel per maand (afmeldingen 01) en zeer scheve verdeling is alleen een groot verschil zichtbaar; beslissen na twee porties, gepoold |
| Effect | Pauze kost ~$0 tot $300 per week toegeschreven. Suppressie later: min 1.700 tot 1.900 afmeldingen en ~100 klachten per maand, omzetrisico min $5.000 tot $15.000 per maand bruto, daarom met controle |
| API of UI | Smart Sending en flowstatus: UI (status kan via API, maar live flow: UI met akkoord). Splitstap met profiel-update kan de API niet plaatsen: UI. Segment via API |
| Klaar vóór BFCM | Pauze en Smart Sending ja; suppressie bewust na BFCM (in lijn met audit uitbreiden 1.8) |

---

## 3. Q4-kalender voor alle flows, 29 oktober tot en met Cyber Monday 30 november

Sale-fases: nu 50%, Halloween 70% (vanaf ~30 okt, einddatum onbekend), november 70% met de 4 gifts, Black Friday 27 nov, Cyber Monday 30 nov. Testslots in andere flows volgen `2026-10-19-ab-tests.md`; stand op 28 okt: T04 (W1) en T05a (B1) live, T02 live in checkout, cart, browse, TP-browse, P3 en R2; T14 (C1), T16 (A1), T15 (P1) nog niet gestart; T01 overal 100% nieuw.

| Datum | Flow(s) | Actie | Wie | Type |
|---|---|---|---|---|
| **29 okt** | Welcome | T04 W1 beëindigen met de winnaar volgens de regel (A tenzij B P ≥ 95% op omzet per ontvanger) | Floris UI, Claude rapport | test stop |
| 29 okt | Post-purchase | Herinstap 30 naar 7 dagen plus P2-SAFE-filter (2.2) | Floris UI | ingreep |
| 29 okt | Post-purchase | Claude bouwt T15-template en P3-salerij als draft (2.3, 2.4) | Claude API | bouw |
| 29 tot 30 okt | P3 | Eerste P3-mails; dagelijks bewaken (uitschrijving, T02-armen) | Claude | bewaken |
| **30 okt** | Welcome | Start T05b (W1-onderwerp) en T17 (W2-onderwerp). Let op: als W1 in de sale "10%" noemt, A en B samen aanpassen of T05b pas 7 dec | Floris UI | test start |
| 30 okt | FTL | 6 nulmails op Draft, banners en oude claims uit de 4 overblijvers (2.7) | Floris of Claude na akkoord | ingreep |
| 30 okt | Sunset | Smart Sending aan op S1 en S2 | Floris UI | ingreep |
| 30 okt | Post-purchase · affiliate | P1-REPEAT naar `Rwes4z` (affiliate-blok) | Claude API na akkoord | ingreep |
| 30 okt | Checkout, site | T14 (C1) en T16 (A1) starten als Floris dat nog wil; met BFCM-volume net 4 weken vóór de bevriezing, beslissen 7 dec | Floris UI | test start |
| **31 okt** | Alle codeflows | T02-besluit voor de sale (advies: 50/50 tot 19 nov, nocode 20 nov tot 1 dec) | Floris | besluit |
| 31 okt | Kopers | Akkoord op de BFCM-kopersreeks (2.1); Claude bouwt segment, holdoutlijst en 3 mails als draft | Floris, Claude | bouw |
| **1 nov** | Post-purchase | Start T15 (P1-FIRST dekselkaart) | Floris UI | test start |
| 1 nov | Cart | Start T18 (K1-onderwerp) | Floris UI | test start |
| 1 nov | Alle | Begin rapportageperiode "sale" (1 nov tot 6 dec) in `scripts/test_report.py` | Claude | meting |
| **3 tot 6 nov** | P3, winback, v4-winback R1 | Salerij live in P3-templates; winback mail 1 en 3 vernieuwd, split `81062241` op 100%; R1-salerij klaar voor ~23 nov | Claude API na akkoord, Floris controleert | ingreep |
| 5 nov | Browse | T05a (B1) beslissen op data t/m 31 okt; start T19 (B2-NOTCLICKED) | Floris UI | test stop en start |
| 6 nov | Kopers | Testmails kopersreeks aan Floris; holdoutlijst vastzetten | Claude | QA |
| ~8 nov | Post-purchase, VIP | Buffer van vóór de livegang valt weg: controleren of P1-REPEAT-volume stijgt na de herinstapwijziging; VIP-filter "minstens 2" (audit G) | Claude bewaken | meting |
| ~9 nov | Review | `TvfJYU` begint (Fulfilled + 21), grote golf door 822 fulfillments op 24 okt | Claude bewaken | meting |
| **12 nov** | Alle | Laatste dag voor nieuwe template- of filterwijzigingen in post-purchase en winback | | grens |
| **13 nov** | Kopers | Kopersmail 1 (aanloop) naar 85%, 15% holdout | Floris plant in | campagne |
| 13 nov | Sunset | Flow op pauze (manual) tot en met 1 dec | Floris UI | ingreep |
| 18 tot 21 nov | FTL | Oude welcome-arm leeg, FTL-volume halveert vanzelf | Claude bewaken | meting |
| **20 nov t/m 1 dec** | Alle | **Bevriezing**: geen nieuwe tests, geen templatewissels. Lopende tests (T05b, T17, T15, T18, T19, eventueel T14 en T16, review-onderwerp) lopen door; BFCM-dagen apart. T02-splits op nocode (als besloten) | | bevriezing |
| ~23 nov | v4-winback | Eerste R1 (orders van 9 okt) met salerij | automatisch | |
| **27 nov (BF)** | Kopers | Kopersmail 2 | Floris plant in | campagne |
| **30 nov (CM)** | Kopers | Kopersmail 3 | Floris plant in | campagne |
| **2 dec** | Sunset | Sunset weer live met stap 3 (suppressie), eerste portie van 10.000 met 10% controle | Floris UI, Claude segment | ingreep |
| 2 dec | Alle codeflows | T02 terug naar 50/50 | Floris UI | test hervat |
| 7 dec | Alle | Rapport alle tests (voor, sale, BFCM, na). T15, T17, T14, T16 beslissen. Kopers-holdout uitlezen (orders 13 nov tot 7 dec). Start affiliate-test P2-SAFE en T07 (W3-hero) | Claude, Floris | beslissen |

### 3.1 Welke tests bevriezen tijdens BFCM en waarom

| Test | Tijdens 20 nov tot 1 dec | Reden |
|---|---|---|
| T02 code tegen geen code (C4, K3, B2, TP-browse, P3, R2) | op nocode zetten (besluit Floris) of laten lopen maar BFCM uitsluiten | extra 10% op 70% raakt de marge; kopersgedrag in de sale zegt niets over de rest van het jaar |
| T05b W1-onderwerp | loopt door, BFCM apart | onderwerp noemt "10%": als W1 in de sale een ander aanbod krijgt, test pauzeren of A en B samen aanpassen |
| T15 P1-FIRST kaart | loopt door, BFCM apart | dekselprijs in de sale veel lager; winnaar alleen uitrollen als hij buiten de sale wint of in beide dezelfde kant op wijst |
| T17, T18, T19, T14, T16 | lopen door, BFCM apart | onderwerpen zonder aanbod, sale-neutraal |
| Winback- en P3-salerij | geen test, blijft staan | ware informatie; na 1 dec terug naar gewone tekst of nieuwe einddatum |
| Kopers-holdout | moet doorlopen | dit is juist de BFCM-meting |
| Sunset | gepauzeerd | belofte "we stop writing" niet te houden met dagelijkse campagnes |
| Nieuwe tests | geen | gedrag en volume zijn anders; de eerste nieuwe start 7 dec |

### 3.2 Hoe flows en BFCM-campagnes samenleven

**Smart Sending** (Klaviyo-standaard 16 uur):

| Flow | Nu | In BFCM | Waarom |
|---|---|---|---|
| P1, P1-REPEAT, P2, P2-SAFE, review, Mystery M1 tot M3, affiliate S5a/S5b | uit (Mystery aan) | uit laten | service en bevestiging moeten aankomen, ook op campagnedagen |
| P3, v4-winback R1/R2, oude winback | uit | **aan vanaf 12 nov** | verkoopmails; op BF en CM mag de campagne voorgaan |
| Checkout, cart | (andere agents) | uit laten | hoogste intentie, wint van elke campagne |
| Browse, site abandonment, welcome W2 tot W5 | (andere agents) | aan | bij dagelijkse campagnes anders 2 tot 3 mails per dag |
| FTL | aan | aan | slaat zichzelf over op campagnedagen |
| Sunset | uit | aan, en gepauzeerd 13 nov tot 1 dec | zie 2.8 |

**Uitsluitingen in BFCM-campagnes** (HS en Floris):
- `XdK77b` Welcome protection: uitsluiten behalve 1 campagne per week en de BF- en CM-campagne (afmeldingen 01, oorzaak 4).
- "HS // Purchased in the last 7 days" (`TLqivd`): uitsluiten van algemene salecampagnes tot BF, dan meenemen; zij zitten in P1 en Mystery. Kopers van 50% die 70% zien: risico op retour binnen 30 dagen, dus geen "price drop"-boodschap naar recente kopers.
- Kopersreeks-dagen (13, 27, 30 nov): segment "Kopers · mailbaar" krijgt de kopersmail in plaats van de algemene HS-campagne (uitsluiten in de HS-campagne van die dag, holdout krijgt de algemene campagne wel).
- `WuHSm6` sunset: maximaal 3 BFCM-campagnes, Smart Sending aan.
- Altijd: Unsubscribed, Bounced, Spam, For Suppression.

**Frequentie**:
- Doel per profiel: maximaal 1 campagne plus 1 marketing-flowmail per dag, servicemails apart. Op BF en CM mogen 2 campagnes alleen naar wie in 30 dagen klikte of kocht.
- Nieuwe aanmelders (0 tot 14 dagen): welkomstflow plus 1 campagne per week; een campagne binnen 24 uur na een flowmail kost +38% afmelding.
- Stille profielen (90 dagen geen klik of order): maximaal 1 campagne per week, plus BF en CM.
- Post-purchase-ontvangers: P1 op 1 uur, Mystery M1 op dag 3 (slaat over bij X3ySuU-mail binnen 2 dagen), P2 of P2-SAFE, P3 op dag 21: geen extra regel nodig, Smart Sending op P3 vangt de campagnedagen.

---

## 4. Open punten voor Floris

1. Akkoord op de BFCM-kopersreeks met 15% holdout, en vóór 4 november (2.1).
2. T02 in de sale: 50/50 laten lopen, of van 20 nov tot en met 1 dec op nocode (2.4, 3.1).
3. Echte einddatums van Halloween 70% en de novembersale, nodig voor de salerij in P3 en winback.
4. Stapelt de Snowball-vriendenkorting (15%) op 70% off? Bepaalt of het affiliate-blok in BFCM verder mag dan P1-REPEAT.
5. Delivered Shipment en Postflows vallen sinds ~18 okt weg (0.3): fulfillment-achterstand of koppeling? Raakt P2, review, UGC en affiliate S1.
6. Sunset: akkoord op niet uitzetten, wel Smart Sending aan, pauze 13 nov tot 1 dec en suppressie met controle vanaf 2 dec.
7. Failure to launch: akkoord op 6 mails naar Draft vóór 1 november.
