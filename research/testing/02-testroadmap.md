# 02 · Testroadmap v3-flows

Datum: 7 oktober 2026. Rekenwerk en definities: `01-meetkader.md`. Rapportage en beslisregels: `03-rapportage.md`. UTM per variant: `04-utm.md`.

## Spelregels

- **Maximaal 2 tests tegelijk per flow.** Uitzondering: de gepoolde codetest T02 raakt alleen de laatste mail en telt als één test over alle flows.
- **Eén variabele per test** (PLAYBOOK §6). Twee tests in dezelfde flow zitten nooit op hetzelfde element van dezelfde mail.
- **ICE** = Impact x Confidence x Ease, elk 1 tot 10 (max 1000). Impact = verwachte omzet per jaar die de beslissing raakt (volume x RPR x waarschijnlijke lift). Confidence = hoeveel bewijs er al is (baselines, oude splits, benchmarks) en of de test met ons verkeer een uitspraak kan doen. Ease = bouwwerk (nieuwe templates, splits, coupons, akkoord Floris).
- Volumes en baselines uit `baselines/` (90 dagen). Na 2 weken v3 opnieuw rekenen met echte v3-volumes.
- "n" = per arm, 50/50, alpha 5%, power 80%, tenzij anders vermeld. RPR-tests hebben ongeveer 1,5x deze n nodig (01 §3.1).

## Fasering

| Fase | Periode | Wat |
| --- | --- | --- |
| 1 | Livegang (week 0) t/m 19 november | T01 oud tegen nieuw in vier flows, T02 codeprogramma, T04 W1 code tegen gift card, T05a onderwerp B1 |
| Bevriezing | 20 november t/m 6 december (BFCM) | Geen starts. T02 gepauzeerd (alle mails met code, zoals gebouwd). Oud pad uit, v3 100%. |
| 2 | 7 december t/m eind januari | T02 hervat, T03 HI10 in vroege mails, T05b onderwerp W1, T07 hero W3, T08 lengte B2-notclicked |
| 3 | februari en later | T09 unieke welkomstcode, T13 welcome-holdout, T10 10 tegen 15%, T11 C5, T06 timing (alleen met reden) |

Waarom T03 pas in fase 2: T03 is een tweede padsplit in checkout, cart en browse. Naast T01 en T02 zou dat drie tests in dezelfde flow zijn.

## Overzicht, gesorteerd op ICE

| # | Test | Flow / mail | I | C | E | ICE | Fase | Primaire metric | Aantoonbaar binnen looptijd |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T01 | Oud tegen nieuw (padsplit 50/50) | Welcome, checkout, cart, browse | 10 | 8 | 6 | 480 | 1 | Omzet per instromer (cohort) | Welcome +40%, browse +50%, checkout/cart alleen +60% of meer in 5 tot 6 weken |
| T02 | Unieke 48/72u-code tegen geen code (gepoold) | C4, K3, B2-clicked, R2, R2-VIP, P3 | 9 | 7 | 5 | 315 | 1 en 2 | Marge-bijdrage per ontvanger | +50% in ~12 weken, +100% in ~4 weken |
| T03 | HI10 in vroege mails tegen geen code (padsplit) | C1 t/m C3, K1, K2, B1, B2-notclicked | 9 | 6 | 5 | 270 | 2 | Marge-bijdrage per instromer | Zie test; beslissing via 80%-regel |
| T05 | Onderwerp-principe: authority tegen social proof | a: B1, b: W1 | 5 | 6 | 9 | 270 | a: 1, b: 2 | Unieke klikratio, dan RPR | +20% klik: B1 5 wk, W1 9 wk |
| T07 | Hero met aanbodbalk tegen zonder | W3 | 6 | 5 | 8 | 240 | 2 | Unieke klikratio, cohortconversie welcome | +25% klik in ~8 wk |
| T04 | HI10 als code-blok tegen als gift card | W1-A / W1-B | 5 | 5 | 9 | 225 | 1 | Klik W1, RPR W1 | +25% klik in ~6 wk, conversie alleen +50% |
| T08 | Lengte: kort tegen lang | B2-notclicked | 5 | 5 | 7 | 175 | 2 | Unieke klikratio, RPR | +20% klik in ~5 wk |
| T09 | Unieke 10-dagen-welkomstcode tegen HI10 (padsplit, besluit B) | Welcome W1 t/m W5 | 8 | 5 | 4 | 160 | 3 | Marge per instromer welcome | +30% in ~8 wk |
| T13 | Welcome-holdout zonder HI10 | Welcome | 7 | 5 | 3 | 105 | 3 (akkoord Floris) | Marge per instromer | +30% in ~8 wk |
| T10 | 10% tegen 15% bij carts >= $300 | C4-S | 4 | 4 | 6 | 96 | 3 | Marge per ontvanger | Alleen enorme verschillen |
| T11 | C5 "expires tonight" aan tegen uit | Checkout na C4 | 4 | 4 | 6 | 96 | 3 | Omzet per C4-ontvanger | Alleen enorme verschillen |
| T12 | Onderwerp C1 (huidige spec-A/B) | C1 | 2 | 4 | 9 | 72 | niet nu | Klik | +25% klik pas na ~23 wk |
| T06 | Timing C1: 30 min tegen 1 uur (padsplit) | Checkout | 4 | 3 | 5 | 60 | 3, alleen met reden | Omzet per instromer | Alleen +50% of meer in ~8 wk |

---

## Per test

### T01 · Oud tegen nieuw (fase 1)

- **Hypothese:** omdat v3 aanbod en gifts in dollars bovenaan zet, unieke verlopende codes alleen aan het eind gebruikt, de prioriteit tussen flows regelt (niemand in twee verkoopflows) en de welkomstreeks inkort van 8 + 10 naar 6 mails, is de omzet per instromer in elke verkoopflow hoger dan in de oude flow, zonder hogere uitschrijving.
- **Varianten:** pad OLD = beste huidige pad met dezelfde templates en wachttijden (checkout: "New AB Checkout 1"-pad van Y2TmNB; cart: SwkMyn Email #1 t/m #3; browse: TyEjuQ; welcome: SiaNLu plus T2SmtR blijft voor dat pad aan). Pad NEW = v3. Opzet: 01 §2.2 (methode A).
- **Metric:** omzet per instromer, cohortvenster 7 dagen (welcome 14). Secundair: conversie per instromer, AOV, mails per instromer, uitschrijvingen per instromer (niet per mail: v3 en oud sturen een verschillend aantal mails).
- **n en looptijd (conversie per instromer, 50/50):**

| Flow | Instromers/wk | Baseline | n per arm voor +30% / +50% | Weken +30% / +50% | Gepland |
| --- | --- | --- | --- | --- | --- |
| Welcome | 3.740 | 1,28% | 15.439 / 6.033 | 8,2 / 3,2 | 5 weken of tot 19 nov |
| Browse | 6.010 | 0,43% | 46.965 / 18.369 | 15,6 / 6,1 | tot 19 nov |
| Checkout | 607 | 3,19% | 6.057 / 2.362 | 20 / 7,8 | tot 19 nov |
| Cart | 996 | 1,43% | 13.795 / 5.390 | 28 / 10,8 | tot 19 nov |

- **Beslissing:** v3 wordt 100% op 20 november, tenzij v3 aantoonbaar slechter is (bovengrens van het 90%-interval van de relatieve lift onder 0) of een guardrail breekt. Checkout en cart halen hun n voor +50% niet vóór BFCM; dan rapporteren we de puntschatting met interval en de cohortconversie, en vullen aan met de voor-na-vergelijking tegen dezelfde weken in de baseline. Het oude pad heeft verboden claims (DECISIONS), dus langer doorlopen is geen optie.
- **Bouw nodig:** profile-sample-split, oud pad in de nieuwe flow (template-ID's van de huidige mails), Update profile property `v3_arm`, oude flows op Draft.

### T02 · Codeprogramma: unieke code tegen geen code in de laatste mail (fase 1, door in fase 2)

- **Hypothese:** omdat een persoonlijke code met echte vervaltijd een reden geeft om nu te kopen, converteert de laatste mail met code minstens zoveel beter dat de kortingskosten terugverdiend worden (breakeven +20% bij 60% marge en 10% code, +33% bij 15%). Tegenhypothese uit de baselines: korting is in deze flows geen motor (04-offer-strategy §1), gifts en zekerheid wel.
- **Varianten:** A = huidige build (C4_10_48H, K3_10_48H, B2_10_48H, R2_10_72H, R2_VIP_15_72H, P3_THANKYOU_10_14D). B = dezelfde mail zonder code: codebalk wordt "4 GIFTS WITH EVERY ORDER · 30-DAY RETURNS", aanbodblok wordt gift-stack plus trekking plus risk reversal, onderwerp zonder "10%" (bv. C4 "Last reminder: your cart and 4 gifts"). Klaviyo `ab-test`-actie per mail, 50/50, geen automatische winnaar.
- **Strata:** C4-US, C4-INT, K3, B2-clicked, R2, R2-VIP, P3-pan, P3-set, P3-accessory. HI10-tak en cooldown-tak tellen niet mee.
- **Metric:** marge-bijdrage per ontvanger (01 §1.4), gepoold met weging per stratum. Secundair: conversie, AOV, refundratio, codegebruik per prefix.
- **n:** gepoold ~3.380 ontvangers/wk, conversie ~0,4%. +50%: 19.523 per arm, 11,5 weken (RPR 17). +100%: 5.851 per arm, 3,5 weken.
- **Looptijd:** fase 1 (tot 19 nov, ~5 weken) plus fase 2 (vanaf 7 dec, nog ~7 weken) = ~12 weken. BFCM-weken tellen niet mee.
- **Beslissing:** 03 §2.3 (asymmetrisch: geen code is standaard, code blijft alleen bij P(lift > breakeven) >= 80%). Per stratum alleen afwijken als dat stratum alleen al die drempel haalt (alleen R2 en P3 hebben er genoeg volume voor, en zelfs die nauwelijks).
- **Voorwaarde:** publieke lekcodes dicht (01 §4.4). Coupons en `-nocode`-templates bouwen. Preview-check dat de coupon-tag overal in de mail dezelfde code geeft (build-notes winback: tag staat 12 keer in R2).

### T03 · HI10 in vroege mails tegen geen code (fase 2)

- **Hypothese:** omdat C1 zonder code al de beste mail van het account was ($4,28 tot $7,86 per ontvanger) en de oude cartmail met 10% op dag 2 maar $0,79 deed, levert HI10 in C1 t/m C3, K1, K2 en B1 vooral korting op aan mensen die toch al kochten. Zonder HI10 (sale plus gifts in dollars) is de marge per instromer gelijk of hoger.
- **Varianten:** padsplit 50% direct na de trigger in checkout, cart en browse. Pad A = huidige build (HI10 in codebalk, hero en knoppen via `/discount/HI10`). Pad B = dezelfde mails met "4 GIFTS · FREE SHIPPING · 30-DAY RETURNS" in plaats van de HI10-balk en links zonder `/discount/`. Uitzondering in beide paden: profielen op de welcomelijst Uw8eZG zien de HI10-regel (die hebben hem al, 04-offer-strategy §5.2). De laatste mail is in beide paden gelijk (en valt onder T02).
- **Metric:** marge-bijdrage per instromer, cohort 7 dagen, gepoold over de drie flows (gestratificeerd). Secundair: conversie per instromer per flow, aandeel orders met HI10.
- **n:** checkout per instromer +30%: 6.057 per arm (20 wk); gepoold met cart en browse kan het sneller, maar browse domineert dan het volume. Realistisch: 8 weken, beslissing met de 80%-regel. De vraag is hier niet "verkoopt HI10 meer" (vrijwel zeker iets) maar "verkoopt HI10 meer dan 20% extra", en dat vraagt een asymmetrische beslisregel.
- **Bouw:** `-nohi10`-varianten van C1, C2, C3-P, C3-S, K1, K2-new, K2-returning, B1, B2-notclicked. Eigenschap `test_t03 = a/b`.
- **Let op:** de build-notes (checkout punt 1, cart punt 1) adviseren deze test al. Hij gaat in tegen de huidige brief (aanbod in elke hero); daarom eerst akkoord van Floris op de test, niet op de uitkomst.

### T04 · W1: HI10 als code-blok tegen als gift card (fase 1, staat in de spec)

- **Hypothese:** omdat een "welcome gift card" voelt als iets dat je al bezit (endowment) en niet als korting, klikken en kopen meer nieuwe inschrijvers uit W1-B dan uit W1-A.
- **Varianten:** W1-A (code-blok) en W1-B (gift-card-beeld), verder identiek (build-notes welcome). Klaviyo `ab-test` 50/50 op W1, geen automatische winnaar.
- **Metric:** unieke klikratio W1 (beslissend), RPR W1 en orders met HI10 binnen 14 dagen per variant (secundair, via `$attributed_variation`).
- **n:** klik 2,4%, +20%: 17.511 per arm (9,4 wk); +25%: 11.455 per arm (6,1 wk). Conversie W1 0,71%: +50% vraagt 10.956 per arm (5,9 wk).
- **Looptijd:** van livegang tot 19 november (~6 weken, ~11.000 per arm).
- **Beslissing:** B wint alleen als klik P(B > A) >= 90% en RPR niet slechter. Anders A (simpeler, één framing in alle flows). Zie 03 §2.2.

### T05 · Onderwerp-principe: authority tegen social proof (a fase 1, b fase 2)

- **Hypothese:** omdat de koper twijfelt aan "is dit echt beter dan HexClad of Our Place" (research/copy), werkt een onderwerp met specifiek bewijs (authority: rapportnummer, lab) beter dan een onderwerp met massa (social proof: 100,000+ happy customers), of omgekeerd. De uitkomst bepaalt de standaard voor alle onderwerpen (copy-playbook §5: liever een principe-test dan "(+10% off)" aan het eind).
- **T05a, B1 (browse, ~6.010/wk):** A authority "Lab-tested: nothing on this pan to scratch off" tegen B social proof "100,000+ happy customers cook on this pan". Preview gelijk. Vervangt de huidige spec-A/B van B1 (die test "10% off" tegen productbelofte, twee variabelen tegelijk).
- **T05b, W1 (welcome, na T04):** A "Your 10% is inside, and so is report no. 25895" tegen B "Your 10% is inside. 100,000+ happy customers started here." In de winnende W1-variant van T04.
- **Metric:** unieke klikratio (beslissend), daarna RPR. Opens niet gebruiken.
- **n:** B1 +20% klik: 14.410 per arm, 4,8 weken. W1 +20%: 17.511 per arm, 9,4 weken.
- **Beslissing:** 03 §2.2 (contentregel). Herhaling van dezelfde winnaar in B1 en W1 maakt het een merkregel (PLAYBOOK bijwerken na akkoord).
- Copy volgens `research/copy/05-siraat-copy-playbook.md`: alleen goedgekeurde claims, "100,000+ happy customers" letterlijk.

### T07 · Hero met aanbodbalk tegen zonder, W3 (fase 2)

- **Hypothese:** W3 is de bewijsmail. Een aanbodbalk in de hero ("10% OFF WITH HI10 · $70 IN GIFTS") vóór het bewijs breekt de proof beat (04-offer-strategy §5.1: "nooit boven het bewijs"). Zonder balk lezen meer mensen door en klikken ze vaker op het aanbod onderaan.
- **Varianten:** A = huidige W3 (codebalk en aanbodbalk in de hero). B = zelfde mail, hero zonder aanbodbalk en zonder codebalk boven de header; aanbodkaartje na het bewijs blijft.
- **Metric:** unieke klikratio, cohortconversie welcome (14 dagen) via `$attributed_variation`.
- **n:** klik ~2,0%, +25%: 13.809 per arm, ~8 weken bij ~3.400 W3-ontvangers per week.
- **Waarom W3 en niet B1:** B1 krijgt in fase 2 T03 (HI10 of niet), en de aanbodbalk ís daar de HI10-balk. Twee tests op hetzelfde element mag niet.

### T08 · Lengte kort tegen lang, B2-notclicked (fase 2)

- **Hypothese:** wie B1 niet klikte, leest geen 3.289 px. Een korte versie (hero, één review-rij, gift-strip, knop; ~1.800 px) haalt meer klikken en evenveel omzet.
- **Varianten:** A = huidige B2-notclicked. B = kort.
- **Metric:** unieke klikratio, RPR (secundair).
- **n:** ~5.800 ontvangers/wk (B1-niet-klikkers), klik ~2,5% (aanname), +20%: ~16.800 per arm, ~5,8 weken.
- Bij winst: de lengteregel (~3.400 px) in PLAYBOOK heroverwegen voor tweede mails.

### T09 · Unieke 10-dagen-welkomstcode tegen HI10 (fase 3, besluit B van Floris)

- **Hypothese:** een persoonlijke code die echt verloopt op dag 10 maakt "Your 10% expires tomorrow" in W5 waar en verhoogt de conversie in de welcomeflow, zonder extra korting (beide 10%).
- **Varianten:** padsplit 50% na de kopers-split: pad A HI10 (huidig), pad B pool SK_WELCOME10_10D in W1 t/m W5, W5 met echte deadline.
- **Metric:** omzet en marge per instromer, cohort 14 dagen.
- **n:** 1,28% per instromer, +30%: 15.439 per arm, 8,2 weken.

### T13 · Welcome-holdout zonder HI10 (fase 3, alleen na akkoord Floris)

- **Hypothese:** de pop-up belooft een giveaway, geen korting (PLAYBOOK §5). Een deel van de welcome-kopers had zonder HI10 ook gekocht.
- **Varianten:** padsplit 80/20: 20% krijgt welcome zonder code (gifts, bewijs, Benjamin).
- **Metric:** marge per instromer, cohort 14 dagen. 80/20 vraagt ~1,6x de instromers van 50/50: +30% in ~13 weken.
- Gaat in tegen het besluit "HI10 blijft" (DECISIONS 7 okt). Daarom alleen voorleggen, niet inplannen.

### T10 · 10% tegen 15% bij carts >= $300, C4-S (fase 3)

- Uit 04-offer-strategy §8 punt 5. Volume C4-S is een fractie van ~477 per week; alleen zinvol als T02 laat zien dat codes in C4 werken. Breakeven voor 15% ligt op +33% meer kopers. Waarschijnlijk niet te beslissen binnen een kwartaal; dan 10% houden.

### T11 · C5 "expires tonight" aan tegen uit (fase 3)

- Alleen voor C4-openers of -klikkers zonder order. Metric: omzet per C4-ontvanger (niet per C5-ontvanger, want C5 bereikt alleen een selectie). Klein volume; alleen bij een duidelijk signaal uit T02.

### T12 · Onderwerp C1 uit de spec (niet nu)

- De spec vraagt een A/B "Forgetting something?" tegen "Your pan is still here (+10% off)". Bij 607 ontvangers per week en 3,9% klik duurt +25% klik ~23 weken, en de varianten verschillen in twee dingen (vraag tegen bezit, plus wel of geen korting). Advies: C1 met één onderwerp starten (A), de principe-uitkomst van T05 later naar C1 overzetten.

### T06 · Timing C1: 30 minuten tegen 1 uur (fase 3, alleen met reden)

- **Bestaand bewijs:** de live checkoutflow test al 10 tegen 30 minuten (01 §2.1): 28 tegen 28 converters op ~1.300 delivered per arm. Geen verschil.
- **Hypothese:** eerder sturen vangt de twijfelaar terwijl de intentie het hoogst is; later sturen laat de spontane kopers eerst zelf afrekenen (scheelt een "onnodige" mail en, met HI10 in C1, korting).
- **Varianten:** padsplit 50%: wachttijd 30 min tegen 1 uur, verder identiek.
- **Metric:** omzet per instromer (niet per C1-ontvanger, 01 §1.1), cohort 7 dagen, en aandeel orders met HI10.
- **n:** 3,19%, +50%: 2.362 per arm, 7,8 weken. Een timingverschil van +50% is onwaarschijnlijk; deze test zal bijna zeker "geen verschil" opleveren.
- **Advies:** alleen draaien als `research/timing/` een concrete reden geeft (bijv. verkeer per uur van de dag). Anders 1 uur houden, of kiezen op de kostenkant: met HI10 in C1 (zolang T03 niet beslist is) is later sturen goedkoper, want meer spontane kopers rekenen zonder code af.

---

## Nieuwe flows uit de parallelle bouw (anniversary, site, sunset, UGC, VIP)

Templates staan in `klaviyo/templates/v3/{anniversary,site,sunset,ugc,vip}/`. Geen tests in de eerste 4 weken: eerst een eigen baseline (RPR, klik, uitschrijving per mail) opbouwen, want er is geen oude tegenhanger. Daarna:
- VIP v1 ("Twice is a habit. Here's 15% off.") wordt een extra stratum in T02 (code tegen geen code), met breakeven +33% voor 15%.
- Sunset s1/s2: geen omzettest; meet het aandeel dat klikt ("keep me") en het effect op de accountbrede spam- en bounceratio.
- Site a1/a2 en anniversary n1/n2: onderwerp-principe (T05) pas overnemen als T05a en T05b dezelfde winnaar geven.

## Bouwlijst voor de tests (niet uitgevoerd, alleen nodig)

| Wat | Voor | Wie |
| --- | --- | --- |
| Profile-sample-split + `v3_arm` + oud pad in de nieuwe flows | T01 | Flow-bouw |
| `-nocode`-templates C4-US, C4-INT, K3, B2-clicked, R2, R2-VIP, P3 x3 | T02 | Template-bouw |
| Klaviyo-coupons uit de build-notes (C4_10_48H, K3_10_48H, B2_10_48H, R2_10_72H, R2_VIP_15_72H, P3_THANKYOU_10_14D) | T02 | Klaviyo (akkoord DECISIONS 7 okt) |
| Publieke lekcodes dicht | T02, T03 | Floris (Shopify) |
| `-nohi10`-templates (9 mails) + `test_t03` | T03 | Template-bouw, fase 2 |
| B1-onderwerpen T05a | T05 | Copy |
| UTM per blok en per variant | alle | 04-utm.md |
| `research/testing/results.csv` bijhouden | alle | Wekelijks (03) |
