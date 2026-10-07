# 01 · Meetkader voor het v3-flowsysteem

Datum: 7 oktober 2026. Rol: CRO- en experimentation-lead. Alleen gelezen in Klaviyo (TdtTzz), niets aangemaakt of gewijzigd.
Bronnen: `klaviyo/flows/v3-flow-system.md`, `baselines/` (README en alle csv's), `research/ux-2026-10-07/` (00 t/m 04, build-notes), `research/copy/05` en `06`, DECISIONS.md, PLAYBOOK §4 en §6, topcomments van `klaviyo/templates/v3/*/*.html`. Live gelezen: flow-report checkout (laatste 7 dagen, per variatie) en de flow-acties van Y2TmNB.
`research/timing/` bestond nog niet bij het schrijven; zodra die output er is, de timingtest (T06 in 02) daarop afstemmen.

Doel: na livegang bewijzen dat v3 beter is dan wat er nu draait, en daarna per flow blijven verbeteren met tests die echt iets kunnen aantonen bij ons verkeer.

---

## 1. Wat we meten

### 1.1 Primaire metric: omzet per ontvanger (RPR), per flow

**Definitie.** Klaviyo-geattribueerde Placed Order-waarde (`RSNxYV`, Shopify) gedeeld door delivered. Dit is dezelfde definitie als in `baselines/README.md` (RPR = conversion_value / delivered), zodat elk getal direct naast de baseline kan.

Twee niveaus, en we zijn altijd expliciet welk niveau we bedoelen:

| Niveau | Teller | Noemer | Wanneer |
| --- | --- | --- | --- |
| **Flow-RPR per instromer** (hoofdcijfer voor oud tegen nieuw en voor alle tests die op padniveau splitsen) | omzet van alle mails in het pad | aantal profielen dat het pad instroomt (delivered van de eerste mail van het pad) | Oud tegen nieuw, HI10-in-vroege-mails, timing C1 |
| **Mail-RPR** (Klaviyo-standaard per bericht/variatie) | omzet toegeschreven aan die mail of variatie | delivered van die mail of variatie | A/B-test binnen één mail: onderwerp, hero, lengte, code tegen geen code |

Waarom het verschil ertoe doet: als C1 na 30 minuten gaat in plaats van na 1 uur, krijgen meer mensen C1 (de vroege kopers zijn nog niet weggefilterd). De mail-RPR daalt dan bijna vanzelf, terwijl de flow misschien meer opbrengt. Timing en alles wat bepaalt wie een mail krijgt, beoordelen we dus altijd per instromer, nooit per mail.

**Baselines om te verslaan (90 dagen, uit `baselines/`, eigen herberekening per instromer):**

| Flow | Flow-RPR per delivered (baseline #) | Instromers per week (eerste mail, 90d / 12,9 wk) | Conversie per instromer | Omzet per instromer | AOV (waarde / orders) |
| --- | --- | --- | --- | --- | --- |
| Welcome (SiaNLu) | $0.696 (#2) | ~3.740 (eerste mail 48.136) | 1,28% (617 / 48.136) | $3.05 | $233 |
| Checkout (Y2TmNB + Tsg2tV) | $2.359 (#3) | ~607 (5 eerste-mailvarianten, 7.803) | 3,19% (249 / 7.803) | $8.24 | $255 |
| Cart (SwkMyn + TBWngE) | $1.472 (#4) | ~996 (12.810) | 1,43% (183 / 12.810) | $3.85 | $263 |
| Browse (TyEjuQ + Wj6x6V) | $0.968 (#5) | ~6.010 (77.326, één mail) | 0,43% (329 / 77.326) | $0.97 | $221 |
| Post-purchase (RL3TU6) | $0.309 (#6) | ~1.260 (eerste mails per tak, 16.237) | 0,66% | $1.27 | $168 |
| Winback (UEfh4h) | $0.198 (#7) | ~1.245 (eerste mail 16.000) | 0,31% | $0.59 | $189 |

Kanttekening: conversie per instromer is hier de som van unieke converters per mail gedeeld door instromers. Een persoon die op twee mails converteert telt twee keer, dus dit is een bovengrens. Na week 2 van v3 herberekenen met echte v3-volumes: v3 heeft andere filters (geen open-filters in welcome, strengere browse-filters, cart sluit checkout-starters uit), dus de volumes verschuiven.

### 1.2 Secundaire metrics

| Metric | Definitie | Waarom |
| --- | --- | --- |
| Placed order rate | conversion_uniques / delivered (mail) of / instromers (flow) | Minder ruis dan RPR (geen spreiding in orderwaarde), dus eerder significant. Vroege indicator voor RPR. |
| AOV | conversion_value / conversions | C3-P (set-upgrade naar $349), W4 (tiers) en gifts moeten AOV verhogen; codes verlagen hem. |
| Unieke klikratio | clicks_unique / delivered | Primaire metric voor onderwerptests (PLAYBOOK §6: nooit op opens, Apple MPP). |
| Uitschrijfratio | unsubscribe_uniques / delivered | Kosten van meer of agressievere mails. |
| Spamklachtratio | spam_complaints / delivered | Bezorgbaarheid. |
| Marge-bijdrage per ontvanger (alleen bij codetests) | zie §1.4 | Een code die meer omzet maar minder marge geeft, verliest. |

### 1.3 Guardrails (stoppen of niet uitrollen als één hiervan breekt)

Gemeten per arm, vanaf 1.000 delivered per arm (daaronder is één afmelding te veel ruis).

| Guardrail | Baseline | Grens per mail of arm | Actie |
| --- | --- | --- | --- |
| Uitschrijfratio | flows 0,94% gemiddeld (#12); checkout-mails 0,5 tot 1,5% | > 1,0% (PLAYBOOK: > 0,5 signaal, > 1 probleem) **of** > 1,5x de controle-arm | Onderzoeken; > 2x controle = arm stoppen |
| Spamklachtratio | flows 0,076% (#13) | > 0,10% per mail of > 2x controle | Arm stoppen. Account-breed nooit boven 0,3% (Gmail/Yahoo-grens) |
| Bounce | flows 0,52% | > 2% op een mail | Lijstkwaliteit checken, geen testbeslissing |
| Refundratio | Refunded Order `Xg6cwn` / Placed Order, 30 dagen | stijging > 2 procentpunt tegen controle | Korting of belofte trekt verkeerde kopers (30-day returns) |
| Tickets | Opened Ticket `YzvjGf` na flowmail | zichtbare piek met een "code werkt niet"-onderwerp | Code-tests eerst repareren, data van die dagen apart zetten |
| Kortingskosten | korting / omzet per arm | code-arm boven breakeven (§1.4) zonder conversiewinst | Code-arm niet uitrollen |
| Sample ratio mismatch | 50/50-split | chi-kwadraat op aantallen per arm p < 0,01 | Test ongeldig tot de oorzaak (filter, splitvolgorde) is gevonden |

### 1.4 Codes: marge-bijdrage en breakeven

Placed Order-waarde in Klaviyo is na korting. Met brutomarge m (door Floris te bevestigen, rekenvoorbeeld 60%) en korting d:

- Marge-bijdrage per ontvanger = conversie x AOV-na-korting x (1 - (1 - m) / (1 - d)).
- Breakeven-lift in conversie voor een code (zelfde AOV): m / (m - d) - 1.

| Brutomarge m | 10% code | 15% code |
| --- | --- | --- |
| 50% | +25% meer kopers nodig | +43% |
| 60% | +20% | +33% |
| 70% | +17% | +27% |

Een code die minder dan deze lift oplevert, kost geld, ook als de RPR licht stijgt.

### 1.5 Attributievenster

- **Voor rapportage en vergelijking met de baseline:** het Klaviyo-accountvenster, ongewijzigd, zoals in `baselines/` (last touch, Klaviyo-standaard). Niet wijzigen tijdens een test, anders breekt de vergelijking met de baseline. Instelling noteren in de eerste weekrapportage (Settings > Attribution in de UI; via de API niet leesbaar).
- **Voor beslissingen op padniveau:** cohortconversie, onafhankelijk van attributie: elk profiel krijgt in de flow een profieleigenschap met zijn arm (§2.3), en we tellen Placed Order binnen een vast venster na instroom:

| Flow | Cohortvenster | Waarom |
| --- | --- | --- |
| Checkout, cart | 7 dagen na instroom | Flow duurt 4 dagen, plus 48 uur codegeldigheid, plus marge |
| Browse | 7 dagen | Flow duurt 2 dagen plus 48 uur code |
| Welcome | 14 dagen | Flow duurt 10 dagen |
| Post-purchase P3, winback R2 | 30 dagen na de mail | Code geldig 14 respectievelijk 3 dagen; herhaalaankoop is traag |

Cohortconversie lost twee problemen op: (1) Apple MPP blaast opens op en opens tellen mee in attributie, (2) een arm met meer mails krijgt meer kansen om omzet "toegeschreven" te krijgen. Klaviyo-RPR blijft het rapportcijfer; bij tegenspraak beslist de cohortconversie.

---

## 2. Nieuw tegen oud vergelijken

### 2.1 Wat Klaviyo al kan (gecontroleerd)

De live checkoutflow Y2TmNB gebruikt al een random split: conditional split met `{"type": "profile-sample", "percentage": 50}` (actie 111934707, en daaronder nog een 50%-split 96015049). Een willekeurige steekproef op flowniveau werkt dus in dit account en via de API-definitie. Daar bouwen we op.

Bijvangst uit dezelfde flow: de huidige opzet test al **10 tegen 30 minuten** voor de eerste checkoutmail (RpzC3U na 10 min, RZ4Urm na 30 min, elk 25% van de instroom). Over 90 dagen: 28 tegen 28 converters op 1.330 tegen 1.273 delivered. Geen meetbaar verschil. Zie T06 in 02.

### 2.2 Aanbevolen opzet: één flow per trigger, twee paden (methode A)

Per verkoopflow (checkout, cart, browse, welcome):

```
Trigger (zelfde als nu)
  └─ Conditional split: profile-sample 50%
       ├─ ja  → Update profile property  v3_arm = "new"   → v3-pad (C1..C4 enz.)
       └─ nee → Update profile property  v3_arm = "old"   → oud pad: dezelfde wachttijden en dezelfde
                                                            templates als de huidige live flow (template-ID's
                                                            hergebruiken, bv. XRCR7P voor checkout #1)
  (einde van elk pad) → Update profile property  v3_arm_done = vandaag
```

- Oude flows (Y2TmNB, Tsg2tV, SwkMyn, TBWngE, Wj6x6V, TyEjuQ, SiaNLu, T2SmtR) gaan op Draft zodra de nieuwe flow live staat (PLAYBOOK §7: niet archiveren, de cijfers blijven nodig).
- Voordeel: beide armen hebben exact dezelfde trigger, dezelfde instroomfilters en dezelfde periode. Seizoen, sales en verkeer vallen weg uit de vergelijking.
- Het oude pad houdt zijn eigen interne splits niet aan (dus geen 3-weg 10/30 min meer): neem de best presterende oude variant ("New AB Checkout 1"-pad voor checkout, Email #1-pad voor cart).
- Kanttekening: de oude mails bevatten claims die DECISIONS verbiedt (bijv. "100 days to try" in de oude checkout-specs). Daarom loopt het oude pad zo kort als de steekproef toelaat (§3) en stopt het uiterlijk op 20 november.

**Methode B (als methode A te veel bouwwerk is):** oude flows live laten met een extra flowfilter `v3_arm is not "new"`; de nieuwe flow zet als eerste actie na de split de eigenschap. Werkt omdat Klaviyo flowfilters vóór elke stap opnieuw controleert en de oude flows pas na 10 minuten of later de eerste mail sturen. Nadelen: race bij instroom, twee rapporten naast elkaar, en een oude eigenschap van een vorige instroom moet aan het einde gereset worden. Alleen als noodoplossing.

**Methode C (geen split mogelijk):** voor post-purchase en winback (lage conversie, lange cyclus, geen omzetdoel in P1/P2) is een 50/50 oud-tegen-nieuw duur en traag. Daar vergelijken we voor en na: 4 weken v3 tegen hetzelfde kalendervenster in de baseline, plus de codetest binnen v3 (T02). Zwakker bewijs, uitdrukkelijk zo benoemen in het rapport.

### 2.3 Profieleigenschappen voor meting (moeten in de bouw, nu niet aangemaakt)

| Eigenschap | Gezet door | Waarde | Gebruik |
| --- | --- | --- | --- |
| `v3_arm` | Update profile property direct na de 50%-split | `new` / `old` | Cohortconversie per arm via segment "v3_arm = new AND Placed Order at least once in the last 7 days" |
| `v3_arm_flow` | idem | `checkout` / `cart` / `browse` / `welcome` | Zelfde segment per flow |
| `v3_arm_at` | idem | datum | Venster na instroom berekenen |
| `test_<id>` | bij elke padtest (T03, T06) | `a` / `b` | Idem voor padtests |
| `last_flow_code_at`, `last_flow_code_pool` | na elke codemail (staat al in 04-offer-strategy §7) | datum, poolnaam | Cooldown en kostentoewijzing |

Bij A/B-tests binnen één mail (Klaviyo-actie `ab-test`) is geen eigenschap nodig: Klaviyo rapporteert per `variation` (getest: `get_flow_report` met `group_by: variation, variation_name` werkt; niet-geteste mails geven een lege variatie).

### 2.4 Regels voor alle splits

- 50/50 tenzij anders vermeld. Ongelijke verdeling (bv. 80/20) kost bij dezelfde looptijd ruim anderhalf keer zoveel instromers voor dezelfde zekerheid.
- Klaviyo-instelling bij flow-A/B: **geen automatische winnaar** (PLAYBOOK §6). Winnaar kiezen wij, met de regels in 03.
- Nooit midden in een test de split, de wachttijd of de templates van één arm aanpassen. Als het moet: nieuwe test-ID, nieuwe startdatum.
- Elke arm krijgt eigen `utm_term` (zie 04), zodat Shopify en GA de arm ook zien.

---

## 3. Steekproef en looptijd

### 3.1 Rekenmethode

Twee proporties, tweezijdig, alpha 5% (z = 1,96), power 80% (z = 0,84), 50/50:

n per arm = ( 1,96 x √(2 x p̄ x (1 - p̄)) + 0,84 x √(p1(1 - p1) + p2(1 - p2)) )² / (p2 - p1)²

met p1 = baseline-conversie, p2 = p1 x (1 + MDE), p̄ = (p1 + p2) / 2.

Voor RPR (omzet, veel nullen) is de variantie groter dan voor conversie alleen. Met variatiecoëfficiënt CV van de orderwaarde geldt: n_RPR ≈ n_conversie x (1 + CV²). Aanname CV = 0,7 (orders lopen van een pan van $129 tot de 12-delige set van $599; te verifiëren met orderdata), dus **n_RPR ≈ 1,5 x n_conversie**.

Ter controle één regel uitgerekend: checkout per instromer, p1 = 3,19%, MDE +50% → p2 = 4,785%, p̄ = 3,99%.
Teller: (1,96 x √(2 x 0,0399 x 0,9601) + 0,84 x √(0,0309 + 0,0456))² = (1,96 x 0,2768 + 0,84 x 0,2766)² = (0,5425 + 0,2324)² = 0,6005. Noemer: 0,01595² = 0,000254. n = 2.362 per arm, totaal 4.724 instromers, bij 607 per week = **7,8 weken**. Voor RPR x 1,5 = 11,6 weken.

### 3.2 Tabel: n per arm en weken (50/50) per test-eenheid

Volume = ontvangers per week van de eenheid (baselines, 90 dagen / 12,9 weken). Weken = 2 x n / volume. Eerst conversie, tussen haakjes RPR.

| Eenheid | Baseline-conversie | Volume/wk | MDE +20% | MDE +30% | MDE +50% | MDE +100% |
| --- | --- | --- | --- | --- | --- | --- |
| Welcome per instromer | 1,28% | 3.740 | 33.250 · 17,8 wk (26,5) | 15.439 · 8,2 wk (12,3) | 6.033 · 3,2 wk (4,8) | 1.804 · 1,0 wk (1,4) |
| W1 (mail) | 0,71% | 3.740 | 60.326 · 32 wk (48) | 28.020 · 15 wk (22) | 10.956 · 5,9 wk (8,7) | 3.280 · 1,8 wk (2,6) |
| Checkout per instromer | 3,19% | 607 | 13.057 · 43 wk (64) | 6.057 · 20 wk (30) | 2.362 · 7,8 wk (11,6) | 702 · 2,3 wk (3,4) |
| C1 (mail) | 2,10% | 607 | 20.081 · 66 wk | 9.320 · 31 wk | 3.639 · 12 wk (18) | 1.085 · 3,6 wk (5,3) |
| C2 (mail) | 0,34% | 461 | 126.492 · 549 wk | 58.763 · 255 wk | 22.986 · 100 wk | 6.889 · 30 wk |
| C4 (mail) | 0,47% | 477 | 91.373 · 383 wk | 42.446 · 178 wk | 16.601 · 70 wk | 4.974 · 21 wk (31) |
| Cart per instromer | 1,43% | 996 | 29.712 · 60 wk | 13.795 · 28 wk (41) | 5.390 · 10,8 wk (16) | 1.611 · 3,2 wk (4,8) |
| K1 (mail) | 0,84% | 996 | 50.916 · 102 wk | 23.648 · 47 wk | 9.245 · 19 wk (28) | 2.767 · 5,6 wk (8,3) |
| K3 (mail) | 0,41% | 590 | 104.814 · 355 wk | 48.691 · 165 wk | 19.045 · 65 wk | 5.707 · 19 wk (29) |
| Browse per instromer = B1 | 0,43% | 6.010 | 101.098 · 34 wk (50) | 46.965 · 15,6 wk (23) | 18.369 · 6,1 wk (9,1) | 5.504 · 1,8 wk (2,7) |
| B2-clicked (mail) | ~0,8% | ~175 | 53.486 · 611 wk | 24.841 · 284 wk | 9.712 · 111 wk | 2.907 · 33 wk |
| P3 (mail, aanname) | ~0,2% | ~900 | 215.369 · 479 wk | 100.060 · 222 wk | 39.146 · 87 wk | 11.737 · 26 wk |
| R2 (mail) | 0,10% | 1.242 | 431.213 · 694 wk | 200.351 · 323 wk | 78.390 · 126 wk | 23.511 · 38 wk |
| **Gepoolde codemails** (C4 + K3 + B2-clicked + R2 + P3) | ~0,40% | ~3.380 | 107.447 · 64 wk (95) | 49.914 · 30 wk (44) | 19.523 · 11,5 wk (17) | 5.851 · 3,5 wk (5,2) |

B2-clicked: B1-klikratio 2,9% x 6.010 = ~175 per week; conversie geschat. P3: geen directe oude tegenhanger, geschat uit de oude post-purchase-mails ($0,12 tot $0,58 RPR, 0,05 tot 0,6% conversie).

Klikratio (voor onderwerp- en herotests), zelfde formule:

| Eenheid | Baseline-klik | Volume/wk | MDE +15% | MDE +20% | MDE +25% |
| --- | --- | --- | --- | --- | --- |
| B1 | 2,9% | 6.010 | 25.055 · 8,3 wk | 14.410 · 4,8 wk | 9.425 · 3,1 wk |
| W1 | 2,4% | 3.740 | 30.443 · 16,3 wk | 17.511 · 9,4 wk | 11.455 · 6,1 wk |
| W3 (aanname ~3.400 ontvangers/wk, klik ~2,0%) | 2,0% | ~3.400 | 36.693 · 21,6 wk | 21.109 · 12,4 wk | 13.809 · 8,1 wk |
| C1 | 3,9% | 607 | 18.424 · 61 wk | 10.593 · 35 wk | 6.927 · 23 wk |

### 3.3 Wat dit betekent (de eerlijke conclusie)

1. **Welcome en browse zijn onze testlabs.** Alleen daar zijn effecten van +30% binnen 8 tot 16 weken aantoonbaar en +50% binnen 3 tot 6 weken.
2. **Checkout en cart:** oud tegen nieuw kan alleen een groot verschil (+50% of meer) binnen 8 tot 11 weken aantonen. Dat is realistisch voor v3 (aanbod in dollars, gifts, codes), maar een verschil van 20% zien we daar nooit hard.
3. **Losse late mails (C2, C4, K3, B2, P3, R2) zijn individueel niet te testen** op conversie. Een code tegen geen code per mail duurt jaren. Daarom één **gepoold codeprogramma** (T02): dezelfde vraag ("maakt een unieke code extra marge?") in alle laatste mails tegelijk, gestratificeerd per mail geanalyseerd. Dan is +50% in ~12 weken aantoonbaar, +100% in ~4 weken.
4. **De breakeven van een code (+20% bij 60% marge) is met 95% zekerheid niet binnen redelijke tijd te bewijzen.** Daarom beslissen we codes niet met een klassieke significantietoets maar met een asymmetrische regel (03 §2): geen code is de standaard, de code moet zich bewijzen met een kans van minstens 80% dat de lift boven breakeven ligt.
5. Een klein verschil kun je niet "aflezen". Een test die zijn n niet haalt, eindigt als "geen aantoonbaar verschil" en dan kiezen we de goedkoopste of merkveiligste variant, niet de variant die toevallig voor ligt.
6. Met alpha 10% in plaats van 5% (verdedigbaar voor goedkope, omkeerbare contentkeuzes zoals onderwerpregels) daalt elke n met ongeveer 21%.

### 3.4 Minimale looptijd, ook als n eerder gehaald is

- Minimaal 2 volle weken (ma t/m zo), zodat elke weekdag in beide armen zit.
- Minimaal de flowduur plus het cohortvenster na de laatste instromer die meetelt (checkout: instroom stopt na week X, meten tot X + 7 dagen).
- Minimaal 30 conversies per arm voordat we naar RPR kijken; daaronder alleen klik en conversie.

### 3.5 Kalender

- Zomertijd eindigt 1 november 2026: weekgrenzen in UTC verschuiven van 04:00Z naar 05:00Z (zie 03).
- **BFCM-bevriezing 20 november t/m 6 december 2026** (Thanksgiving 26 nov, Black Friday 27 nov, Cyber Monday 30 nov): geen nieuwe tests starten, codetests pauzeren (campagnecodes met 20% en meer vertroebelen alles), oud pad uit. Lopende contenttests op welcome en browse mogen doorlopen maar BFCM-weken worden apart gerapporteerd en niet samengevoegd met de rest.
- Oktober Prime Sale en eerdere sales zitten in de baseline (baselines/README): voor-na-vergelijkingen altijd naast hetzelfde soort periode leggen.

---

## 4. Holdout voor kortingscodes (bewijzen dat codes extra omzet geven)

### 4.1 Vraag

Levert een unieke 48/72-uurs-code in de laatste mail meer marge op dan dezelfde mail zonder code (gifts, trekking, risk reversal), en levert HI10 in de eerste mails van checkout, cart en browse meer op dan dezelfde mails zonder code?

Waarom dit de belangrijkste test is: de oude data zegt nee (04-offer-strategy §1: C1 zonder code doet $4,28 tot $7,86 per ontvanger, cart-mail met 10% op dag 2 maar $0,79; winback "10% expires tonight" $0,20 tegen $0,24 voor de nieuwe-producten-mail), maar de v3-bouw heeft HI10 in bijna elke hero gezet (build-notes checkout punt 1, cart punt 1). Elke 10% aan iemand die toch al kocht, is pure margeverlies.

### 4.2 Opzet

**Fase 1 (test, vanaf livegang): 50/50 binnen v3.**
- T02, laatste mails: in C4-US, C4-INT, K3, B2-clicked, R2, R2-VIP en P3 (pan, set, accessory) een Klaviyo `ab-test`-actie: variant A = mail met unieke code (huidige build), variant B = dezelfde mail zonder code (codebalk wordt gift-balk, aanbodblok wordt gifts plus trekking plus "30-day returns"). Zelfde onderwerp, behalve het woord "10%". Templates `-nocode` moeten nog gebouwd worden.
- T03, vroege mails: een padsplit (profile-sample 50%) direct na de trigger in checkout, cart en browse: pad A met HI10 in C1 tot C3, K1, K2, B1 en B2-notclicked (huidige build), pad B dezelfde mails zonder HI10 (aanbod = sale plus gifts in dollars). De laatste mail is in beide paden gelijk (en valt zelf onder T02).
- Welcome is uitgezonderd: HI10 in welcome is een besluit (DECISIONS 7 okt). Een welcome-holdout zonder HI10 kan pas na akkoord van Floris (zie 02, T13).

**Fase 2 (na beslissing, blijvend): kleine permanente holdout.**
Wint de code, dan blijft 10% van de codemails zonder code, permanent. Dat kost weinig en laat zien of het effect blijft (codes slijten, couponsites lekken). Verliest de code, dan krijgt 10% wel een code, om te zien of het beeld kantelt in Q1. Rapport per kwartaal, gepoold over alle mails.

### 4.3 Analyse

- Per mail (stratum) per arm: delivered, conversies, omzet, korting (Shopify, per codeprefix, zie 03).
- Gepoolde lift = gewogen gemiddelde van de verschillen per stratum (Mantel-Haenszel voor conversie, ontvanger-gewogen voor marge per ontvanger). Niet de ruwe totalen optellen: R2 heeft veel volume en weinig conversie, C4 omgekeerd; ruw optellen geeft een vertekend beeld.
- Beslissing op marge-bijdrage per ontvanger (§1.4), met de regel in 03 §2.3.

### 4.4 Lekken die de test verstoren

- Publieke codes zonder einddatum (BFEXTRA10 7.626 keer gebruikt, NYEXTRA10, NTWDHPKL5C, EXTRA30, enz.; 04-offer-strategy §2). Iemand in de no-code-arm die BFEXTRA10 googelt, krijgt alsnog 10%. Dat drukt het gemeten codeeffect. Vóór de start moeten die codes dicht (actie Floris). Zo niet: in de analyse apart tellen hoeveel orders in de no-code-arm een publieke code gebruikten (Placed Order heeft de kortingscode als eigenschap; Shopify-orders ook).
- HI10-profielen (welcomelijst Uw8eZG) krijgen volgens 04-offer-strategy in de laatste mail een HI10-herinnering in plaats van een unieke code. Die tak valt buiten T02 of wordt een eigen stratum.
- Cooldown (`last_flow_code_at` < 30 dagen) gaat altijd naar de no-code-tak en telt niet mee in T02.
