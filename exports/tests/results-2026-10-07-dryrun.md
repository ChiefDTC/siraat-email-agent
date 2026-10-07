# Testrapport v4-flows · 2026-10-07 · PROEF op oude flows

Gegenereerd door `scripts/test_report.py` --dry-run --cohort. Venster 2026-08-26 tot 2026-10-08 (UTC, verzenddatum), 43 dagen data. Klaviyo flow-series-report, conversion metric Placed Order (RSNxYV). BFCM-bevriezing 20 nov 2026 t/m 6 dec 2026 telt niet mee. Beslisregels: `research/testing/05-beslisregels.md`.

**Proef.** De v4-flows staan nog niet live. Arm A en B zijn hier bestaande splits in de oude flows, alleen om te laten zien dat ophalen, groeperen en rekenen werken. Geen beslissingen op baseren.

**Cohort onvolledig** (--cohort-max): niet alle kopers opgehaald, cohortcijfers zijn een ondergrens.

## Samenvatting

| Test | Stratum | Advies | Toelichting |
| --- | --- | --- | --- |
| T01 | welcome | **GEEN DATA** | Een arm heeft geen verzendingen: split, A/B-start of berichtnamen controleren. |
| T01 | checkout | **DOORLOPEN** | 45% van n, n gehaald rond 29 nov 2026. Tot 19 november, oud pad uiterlijk dan uit. |
| T01 | cart | **NIET KIJKEN** | Minder dan 14 dagen of minder dan 30 conversies per arm (51% van n, n gehaald rond 17 nov 2026). |
| T01 | browse | **DOORLOPEN** | 19% van n, n gehaald rond 6 apr 2027. Tot 19 november, oud pad uiterlijk dan uit. |
| T02 | gepoold | **STOP / ONDERZOEK** | Guardrail: verdeling 2718/2392 wijkt af van 50/50 (SRM p=0.0000): test ongeldig tot de oorzaak bekend is. |
| T04 | w1 | **NIET KIJKEN** | Minder dan 14 dagen of minder dan 30 conversies per arm (6% van n, n gehaald rond 4 aug 2028). |
| T05a | b1 | **DOORLOPEN** | 72% van n, n gehaald rond 23 okt 2026. Let op: uitschrijving B 1.85% (andere arm 1.60%); spam B 0.122% boven 0,10% (bezorgbaarheid, geen testbeslissing); uitschrijving A 1.60% (andere arm 1.85%); spam A 0.113% boven 0,10% (bezorgbaarheid, geen testbeslissing). |

Leeswijzer: n = instromers (T01, delivered van de eerste mail van het pad) of ontvangers (overige tests). RPR = Klaviyo-geattribueerde omzet / n. Conversie (attr.) = unieke converters / n (bij T01 opgeteld over het pad, dus een bovengrens). Cohort = kopers binnen 7 dagen (welcome 14) na de instapmail, los van attributie; alleen met `--cohort`. P(B>A) = kans dat B beter is (Bayesiaans). Lift = B t.o.v. A, mediaan met 90%-interval.

## T01 · Oud tegen nieuw (PROEF: interne splits oude flows)

A = pad A, B = pad B. Primair: omzet per instromer en conversie.

| Stratum | Arm | Berichten | n | Omzet | RPR | Conv. (attr.) | Cohort | Klik | Uitschr. | Spam | AOV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| checkout | A | Copy of Email #1; Email #1; Email #2; Email #3; Email #4 | 1138 | $6,920 | $6.08 | 2.81% | 6/914 = 0.66% | 8.44% | 4.04% | 0.176% | $216 |
| checkout | B | New AB Checkout 1; New AB Checkout 2; New AB Checkout 3; New AB Checkout 4; New  | 1209 | $12,290 | $10.17 | 3.47% | 6/980 = 0.61% | 8.77% | 3.56% | 0.000% | $286 |
| cart | A | Email #1; Email #3 | 2947 | $8,674 | $2.94 | 0.98% | 9/2356 = 0.38% | 3.77% | 1.87% | 0.170% | $289 |
| cart | B | Copy of Email #1; Copy of Email #3 | 2846 | $10,680 | $3.75 | 1.12% | 6/2281 = 0.26% | 4.11% | 2.04% | 0.176% | $324 |
| browse | A | Email #1 | 9904 | $11,286 | $1.14 | 0.46% | 21/7652 = 0.27% | 3.69% | 1.33% | 0.010% | $245 |
| browse | B | Copy of Email #1 | 9619 | $7,351 | $0.76 | 0.35% | 13/7440 = 0.17% | 3.11% | 0.95% | 0.021% | $216 |
| welcome | A | EB [DG] \| Email #2; EB [DG] \| Email #3; EB [DG] \| Email #4; EB [DG] \| Email #5;  | 24644 | $63,016 | $2.56 | 1.03% | 23/16192 = 0.14% | 6.59% | 8.31% | 0.402% | $240 |
| welcome | B | (geen) | 0 | $0 |  |  |  |  |  |  |  |

| Stratum | P(B>A) RPR | Lift RPR (90%) | P(B>A) conv. | P(B>A) cohort | P(B>A) klik | P(B>A) uitschr. | SRM p | Advies | Toelichting |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| checkout | 96% | +63% (+3% tot +159%) | 82% | 45% | 61% | 27% | 0.143 | **DOORLOPEN** | 45% van n, n gehaald rond 29 nov 2026. Tot 19 november, oud pad uiterlijk dan uit. |
| cart | 78% | +28% (-23% tot +113%) | 70% | 24% | 75% | 68% | 0.185 | **NIET KIJKEN** | Minder dan 14 dagen of minder dan 30 conversies per arm (51% van n, n gehaald rond 17 nov 2026). |
| browse | 7% | -33% (-57% tot +5%) | 11% | 10% | 1% | 1% | 0.041 | **DOORLOPEN** | 19% van n, n gehaald rond 6 apr 2027. Tot 19 november, oud pad uiterlijk dan uit. |

## T02 · Code tegen geen code (PROEF: laatste mails oude flows)

A = A, B = B. Primair: omzet per ontvanger en conversie.

| Stratum | Arm | Berichten | n | Omzet | RPR | Conv. (attr.) | Cohort | Klik | Uitschr. | Spam | AOV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| checkout-4 | A | Email #4 | 927 | $1,238 | $1.34 | 0.54% | 1/773 = 0.13% | 1.94% | 0.86% | 0.000% | $248 |
| checkout-4 | B | New AB Checkout 4 | 601 | $80 | $0.13 | 0.17% | 4/520 = 0.77% | 1.66% | 0.33% | 0.000% | $80 |
| cart-3 | A | Email #3 | 1419 | $850 | $0.60 | 0.21% | 2/1145 = 0.17% | 1.83% | 1.13% | 0.000% | $283 |
| cart-3 | B | Copy of Email #3 | 1423 | $2,338 | $1.64 | 0.49% | 3/1111 = 0.27% | 1.55% | 0.98% | 0.070% | $334 |
| cart-3-tp | A | Email #3 | 372 | $144 | $0.39 | 0.27% | 0/296 = 0.00% | 1.61% | 0.54% | 0.000% | $144 |
| cart-3-tp | B | Copy of Email #3 | 368 | $0 | $0.00 | 0.00% | 2/301 = 0.66% | 0.82% | 0.82% | 0.000% |  |

| Stratum | P(B>A) RPR | Lift RPR (90%) | P(B>A) conv. | P(B>A) cohort | P(B>A) klik | P(B>A) uitschr. | SRM p | Advies | Toelichting |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| checkout-4 | 3% | -88% (-99% tot -25%) | 17% | 96% | 37% | 13% | 0.000 | **(stratum)** | Beslissing op de gepoolde regel; per stratum alleen bij eigen 80%-bewijs. |
| cart-3 | 89% | +161% (-27% tot +946%) | 89% | 67% | 28% | 36% | 0.940 | **(stratum)** | Beslissing op de gepoolde regel; per stratum alleen bij eigen 80%-bewijs. |
| cart-3-tp | 42% | -30% (-97% tot +1156%) | 25% | 87% | 18% | 66% | 0.883 | **(stratum)** | Beslissing op de gepoolde regel; per stratum alleen bij eigen 80%-bewijs. |
| gepoold | 62% | +19% (-53% tot +197%) | 55% | 96% | 18% | 26% | 0.000 | **STOP / ONDERZOEK** | Guardrail: verdeling 2718/2392 wijkt af van 50/50 (SRM p=0.0000): test ongeldig tot de oorzaak bekend is. |

## T04 · W1-A tegen W1-B (PROEF: Tsg2tV Email #1 tegen Copy of Email #1)

A = A, B = B. Primair: omzet per ontvanger en conversie.

| Stratum | Arm | Berichten | n | Omzet | RPR | Conv. (attr.) | Cohort | Klik | Uitschr. | Spam | AOV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w1 | A | Email #1 | 679 | $2,136 | $3.15 | 2.06% | 4/560 = 0.71% | 4.27% | 0.44% | 0.295% | $153 |
| w1 | B | Copy of Email #1 | 662 | $1,037 | $1.57 | 0.60% | 2/528 = 0.38% | 4.38% | 1.21% | 0.000% | $259 |

| Stratum | P(B>A) RPR | Lift RPR (90%) | P(B>A) conv. | P(B>A) cohort | P(B>A) klik | P(B>A) uitschr. | SRM p | Advies | Toelichting |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w1 | 16% | -47% (-83% tot +51%) | 1% | 25% | 54% | 93% | 0.642 | **NIET KIJKEN** | Minder dan 14 dagen of minder dan 30 conversies per arm (6% van n, n gehaald rond 4 aug 2028). |

## T05a · Onderwerp B1 (PROEF: Wj6x6V Email #1 tegen Copy of Email #1)

A = A, B = B. Primair: unieke klik (RPR als rem).

| Stratum | Arm | Berichten | n | Omzet | RPR | Conv. (attr.) | Cohort | Klik | Uitschr. | Spam | AOV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| b1 | A | Email #1 | 9768 | $6,737 | $0.69 | 0.29% | 7/7588 = 0.09% | 2.69% | 1.60% | 0.113% | $241 |
| b1 | B | Copy of Email #1 | 9874 | $6,443 | $0.65 | 0.22% | 11/7679 = 0.14% | 2.34% | 1.85% | 0.122% | $293 |

| Stratum | P(B>A) RPR | Lift RPR (90%) | P(B>A) conv. | P(B>A) cohort | P(B>A) klik | P(B>A) uitschr. | SRM p | Advies | Toelichting |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| b1 | 44% | -5% (-46% tot +66%) | 19% | 81% | 6% | 92% | 0.449 | **DOORLOPEN** | 72% van n, n gehaald rond 23 okt 2026. Let op: uitschrijving B 1.85% (andere arm 1.60%); spam B 0.122% boven 0,10% (bezorgbaarheid, geen testbeslissing); uitschrijving A 1.60% (andere arm 1.85%); spam A 0.113% boven 0,10% (bezorgbaarheid, geen testbeslissing). |

