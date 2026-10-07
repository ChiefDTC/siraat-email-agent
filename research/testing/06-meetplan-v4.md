# 06 · Meetplan v4-tests (T01, T02, T04, T05a)

Datum: 7 oktober 2026, de dag voor livegang. Hoort bij `01-meetkader.md` (definities), `02-testroadmap.md` (tests) en `03-rapportage.md`. De korte versie voor de eigenaar staat in `05-beslisregels.md`. Rapport draaien: `scripts/test_report.py` (uitleg onderaan).

Volumes zijn opnieuw gemeten op de oude flows: Klaviyo flow-series-report, 8 volle weken (10 aug t/m 4 okt 2026), conversion metric Placed Order (RSNxYV). Bron en berekening: `exports/tests/plan-2026-10-07.md` (`test_report.py --plan`). Ze liggen dicht bij de baselines in 01 §1.1.

## 1. Volumes waar we mee rekenen

| Eenheid | Instromers per week (oud) | Per arm bij 50/50 | Conversie per instromer (attr., bovengrens) | Omzet per instromer |
| --- | --- | --- | --- | --- |
| Welcome (SiaNLu) | 4.065 | 2.032 | 1,15% | $2,70 |
| Checkout (Y2TmNB + Tsg2tV) | 604 | 302 | 2,96% | $7,76 |
| Cart (SwkMyn + TBWngE) | 996 | 498 | 1,38% | $3,87 |
| Browse (TyEjuQ + Wj6x6V) | 6.182 | 3.091 | 0,40% | $0,93 |

Wat dit voor de andere tests betekent: T04 (W1) en T05a (B1) lopen alleen in de v4-arm van T01, dus krijgen een kwart van de instroom (T05a alleen bij kookgerei, aanname 85%). T02 loopt in checkout en cart ook alleen in de v4-arm. Daardoor:

| Test | Per arm per week | Basis |
| --- | --- | --- |
| T02 gepoold (C4, K3, B2-clicked, R2, P3) | ~1.340 | conversie ~0,18% (oude laatste mails: C4 0,57%, K3 0,43%, R2 0,11%, P3 0,03%) |
| T04 W1-A tegen W1-B | ~965 | conversie W1 0,71%, klik 2,4% |
| T05a B1-onderwerp | ~1.315 | klik 3,06%, conversie 0,40% |

Cooldown (code in de laatste 30 dagen) gaat buiten T02 om en maakt T02 nog kleiner. Na week 2 rekenen we alles opnieuw met echte v4-volumes (`--plan` vervangen door de cijfers uit het eerste rapport).

## 2. Per test

Steekproef: twee proporties, alpha 5% tweezijdig, power 80%, 50/50. Voor omzet per ontvanger is ongeveer 1,5 keer zoveel nodig (orderwaarde varieert, CV 0,7). "Aantoonbaar na 6 weken" = het kleinste verschil dat we op 19 november met die zekerheid kunnen zien.

### T01 · Oud tegen nieuw, per flow (padsplit 50/50)

- **Primaire KPI:** omzet per instromer (alle mails van het pad, gedeeld door delivered van de eerste mail) en **cohortconversie**: aandeel instromers met een Placed Order binnen 7 dagen na de eerste mail (welcome 14 dagen), los van Klaviyo-attributie. Bij tegenspraak beslist de cohortconversie (01 §1.5).
- **Secundair:** unieke klik per instromer, uitschrijvingen per instromer, spam per instromer (per instromer, niet per mail: v4 en oud sturen een ander aantal mails), AOV.
- **Arm herkennen:** berichtnamen "Old · ..." = oud pad, de rest van de flow = v4. Instapmail oud "Old · Checkout 1" (cart, browse, welcome idem), v4 C1, K1/K1-ACC, B1/B1-ACC, W0/W1.

| Flow | n per arm (+30% / +50%) | Weken (conversie / omzet) bij geplande MDE | Aantoonbaar na 6 weken (conv. / omzet) |
| --- | --- | --- | --- |
| Welcome | 17.235 / 6.736 | +30%: 8,5 / 12,6 | +36% / +45% |
| Browse | 50.320 / 19.682 | +30%: 16,3 / 24,3 | +52% / +65% |
| Checkout | 6.545 / 2.553 | +50%: 8,4 / 12,6 | +61% / +76% |
| Cart | 14.289 / 5.583 | +50%: 11,2 / 16,7 | +71% / +90% |

- **Looptijd:** vaste horizon. Instroom tot en met 19 november (6 weken), dan oud pad uit (verboden claims, BFCM). Cohorten worden rijp tot 26 november (welcome 3 december); de beslissing van 20 november gebruikt alleen rijpe cohorten.
- **Stopregel:** v4 is de standaard. Oud wint alleen als P(oud beter) >= 95% op omzet per instromer en de cohortconversie dezelfde kant op wijst. Vroeg stoppen mag na 14 dagen en minstens 30 conversies per arm als P(v4 beter) >= 99%: dan het oude pad direct uit (scheelt verboden claims).
- **Bij een winnaar:** v4 (of geen bewijs): T01-split naar 100% v4, oude flows Y2TmNB, Tsg2tV, SwkMyn, TBWngE, Wj6x6V, TyEjuQ, SiaNLu, T2SmtR op Draft (niet archiveren). Oud aantoonbaar beter in een flow: v4 blijft wel live (oud pad mag niet blijven), maar die flow gaat per mail door het rapport en bovenaan de testlijst van fase 2.

### T02 · Unieke code tegen geen code in de laatste mail (gepoold)

- **Primaire KPI:** omzet per ontvanger en conversie binnen 7 dagen per stratum, gepoold (gewicht = ontvangers per stratum). Beslissend is of de code genoeg extra kopers oplevert om de korting terug te verdienen: breakeven +20% kopers bij 10% code en 60% marge (+33% bij 15%, R2-VIP).
- **Secundair:** klik, uitschrijving, spam, AOV, refunds, gebruik van publieke lekcodes in de nocode-arm.
- **Arm herkennen:** "CODE · X" (A) tegen "X nocode · T02-B" (B). "... nocode · cooldown" telt niet mee. V1 en N2 zitten de eerste 4 weken niet in T02.
- **n:** gepoold ~1.340 per arm per week bij 0,18%. +50%: 44.461 per arm (33 weken). Aantoonbaar na 12 weken: +90% (conversie). Deze test kan de breakeven van +20% dus nooit hard bewijzen; daarom de asymmetrische regel.
- **Looptijd:** fase 1 (tot 19 november) plus fase 2 (7 december t/m 31 januari), samen ~12 weken. BFCM telt niet mee (T02 dan 100% code).
- **Stopregel:** vaste horizon 31 januari. Code blijft alleen als P(codelift > breakeven) >= 80%; anders geen code. Vroeg stoppen alleen richting geen code: P(zonder code beter op omzet) >= 99% na minstens 4 weken.
- **Bij een winnaar:** geen code: split 90/10 (10% houdt de code als permanente holdout). Code: split 90/10 de andere kant op. Kwartaalrapport op de holdout.

### T04 · W1: HI10 als code-blok (A) tegen gift card (B)

- **Primaire KPI:** omzet per ontvanger van W1 en conversie binnen 14 dagen na W1 (cohort, via `--cohort`).
- **Secundair:** unieke klik W1 (snelste signaal), uitschrijving, spam, aandeel orders met HI10.
- **Arm:** "W1 · T04-A" tegen "W1 · T04-B" (Klaviyo A/B-actie, geen automatische winnaar). Verzendingen op het hoofdbericht "W1" betekenen dat iemand "Start test" niet heeft geklikt; het rapport meldt dat.
- **n:** ~965 per arm per week. Conversie +50%: 10.944 per arm (11 weken, omzet 17). Aantoonbaar na 6 weken: +72% (conversie); klik +25% in ~6 weken.
- **Looptijd:** mag na BFCM doorlopen (contenttest), BFCM-dagen tellen niet. Vaste horizon: geplande n of 15 januari 2027, wat eerst komt.
- **Stopregel:** B wint bij P(B beter op omzet) >= 95% op de horizon; vroeg bij >= 99% met conversie in dezelfde richting. Anders A (één framing in alle flows).
- **Bij een winnaar:** A/B-test in Klaviyo beëindigen met de winnaar. Daarna T05b (onderwerp W1) in de winnende W1.

### T05a · B1-onderwerp: authority (A) tegen social proof (B)

- **Primaire KPI (opdracht):** omzet per ontvanger en conversie binnen 7 dagen. Eerlijk: een onderwerpregel verandert vooral wie opent en klikt, en conversie +30% is pas na ~38 weken aantoonbaar. Daarom beslist **unieke klik** en is omzet de rem (B mag niet duidelijk slechter zijn).
- **Secundair:** omzet per ontvanger, conversie, uitschrijving, spam. Opens nooit (Apple MPP).
- **Arm:** "B1 · T05a-A" tegen "B1 · T05a-B".
- **n:** ~1.315 per arm per week, klik 3,06%. +20% klik: 13.628 per arm (~10 weken). Aantoonbaar na 6 weken: +27% klik.
- **Looptijd en stopregel:** als T04. B wint bij P(B beter op klik) >= 95% en P(B beter op omzet) >= 20%; A wint bij P(A beter op klik) >= 95%; anders A.
- **Bij een winnaar:** winnend principe noteren; wint hetzelfde principe ook in T05b (W1), dan voorstel voor PLAYBOOK (na akkoord).

## 3. Waarom Bayesiaans en waarom 95%

Een vaste n halen we voor 19 november bij geen enkele test (tabel §2). Een kans "B is beter" is wel elke week uit te rekenen en is eerlijk zolang we (1) alleen beslissen op de horizon of bij een heel strenge vroege drempel (99%), en (2) bij twijfel de standaard kiezen: v4 in T01, geen code in T02, A in T04 en T05a. Dit vervangt voor deze vier tests de 90%-contentregel uit 03 §2.2; de coderegel (80% boven breakeven) en de guardrails uit 01 §1.3 blijven.

Rekenwijze in het script: Beta-binomiaal (vlakke prior) voor conversie, klik en uitschrijving. Omzet per ontvanger = conversie x orderwaarde, met een Gamma-verdeling voor de gemiddelde orderwaarde (CV 0,7), 40.000 trekkingen. Per-profieldata voor een echte bootstrap geeft Klaviyo niet in een rapport; de cohortmodus haalt wel orders per koper op.

## 4. Rapport draaien

```
cd /tmp
python3 -I /home/user/siraat-email-agent/scripts/test_report.py             # live, sinds 8 okt
python3 -I /home/user/siraat-email-agent/scripts/test_report.py --cohort    # plus cohortconversie (duurt 5 tot 20 min)
python3 -I /home/user/siraat-email-agent/scripts/test_report.py --dry-run   # proef op de oude flows
python3 -I /home/user/siraat-email-agent/scripts/test_report.py --plan      # volumes en steekproef opnieuw
```

- Uitvoer: `exports/tests/results-YYYY-MM-DD.md` (samenvatting met advies per test bovenaan) en `.csv` (één regel per test, stratum en arm).
- Eén report-call per run (Klaviyo-limiet 2 per minuut, 225 per dag). Alleen lezen.
- Cohort: haalt Placed Order-events in het venster op en per koper de Received Email-events (`$message` = instapmail van de arm). Telt een koper als die binnen 7 dagen (welcome 14) na de instapmail bestelt. Noemer = delivered van de instapmail op rijpe dagen. Cache per profiel in `~/.cache/siraat-test-report/` (alleen tijd en bericht-ID, geen e-mailadressen).
- Elke maandag draaien, resultaat in `research/testing/results.csv` en een logregel (03 §1).

## 5. Bekende beperkingen

- Klaviyo-conversie per instromer telt een koper die op twee mails converteert twee keer (bovengrens). Daarom de cohortconversie.
- Flow-series-report dateert op verzenddatum (UTC-dagen), niet op orderdatum.
- De cooldown-tak en HI10-profielen zitten niet in T02; hun volume weten we pas na livegang.
- Aannames in de volumes (85% kookgerei in browse en cart, 5% bestaande klanten in welcome, conversie B2-clicked 0,8%) na week 2 vervangen door echte cijfers.
