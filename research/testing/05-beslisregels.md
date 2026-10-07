# 05 · Beslisregels voor de eigenaar (één pagina)

Geldt voor T01 (oud tegen nieuw), T02 (code tegen geen code), T04 (W1-A tegen W1-B) en T05a (onderwerp B1), live vanaf 8 oktober 2026. Onderbouwing en getallen: `06-meetplan-v4.md`. Het rapport `exports/tests/results-YYYY-MM-DD.md` zet bij elke test een van de adviezen hieronder.

## Kijken

- **Eén keer per week, op maandag**, met `scripts/test_report.py`. Niet tussendoor in Klaviyo naar A/B-percentages kijken: die schommelen de eerste weken alle kanten op.
- **De eerste 14 dagen niets beslissen**, en ook niet zolang een arm minder dan 30 conversies heeft (T05a: 30 kliks). Het rapport zegt dan **NIET KIJKEN**.
- Wat je wel elke week controleert: de guardrails (hieronder). Die mogen altijd een test stoppen.

## Stoppen

| Advies in het rapport | Wanneer | Wat jij doet |
| --- | --- | --- |
| **STOP / ONDERZOEK** | Uitschrijving of spam in een arm meer dan 2x de andere arm, of de verdeling wijkt af van 50/50 | Arm met het probleem stoppen als het na een week nog zo is. Bij een afwijkende verdeling: split of filter laten nakijken, cijfers van die test tellen tot de fix niet. |
| **STOP: ... WINT** | Na minstens 14 dagen en 30 conversies per arm een kans van 99% of meer | Mag eerder stoppen. Winnaar uitrollen (zie onder). |
| **DOORLOPEN** | Nog geen horizon en geen 99% | Niets doen. |
| **BESLIS: ...** | Horizon bereikt (geplande aantallen of einddatum) | Winnaar uitrollen. Onder 95% wint de standaard. |
| **GEEN DATA** | Een arm stuurt niets | Split, A/B-start ("Start test" in Klaviyo) of berichtnamen controleren. |

**Horizon en standaard per test**

| Test | Einde | Winnaar als | Bij twijfel |
| --- | --- | --- | --- |
| T01 oud tegen nieuw | instroom tot 19 november | Oud wint alleen bij P(oud beter) >= 95% | v4 |
| T02 code tegen geen code | 31 januari 2027 (zonder BFCM) | Code blijft alleen bij P(code verdient de korting terug) >= 80% | geen code |
| T04 W1-A tegen W1-B | geplande aantallen of 15 januari 2027 | P(B beter op omzet per ontvanger) >= 95% | A (code-blok) |
| T05a onderwerp B1 | geplande aantallen of 15 januari 2027 | P(B beter op klik) >= 95% en omzet niet duidelijk slechter | A (authority) |

Verlengen mag niet. Wat op de einddatum niet bewezen is, krijgt de standaard.

## Bij een winnaar

1. Klaviyo: A/B-test beëindigen met de winnaar, of het verliezende pad uit de split halen. T01: split naar 100% v4, oude flows op **Draft** (niet archiveren).
2. T02: nooit helemaal dicht. De winnaar krijgt 90%, de verliezer houdt 10% als blijvende controle.
3. Regel in `research/testing/results.csv` en een logregel in `LOG.md`.
4. Na 4 weken nameten. Verwacht een kleiner effect dan in de test; dat is normaal.
5. Pas daarna de volgende test in die flow starten.

## BFCM-bevriezing: 20 november t/m 6 december 2026

- **Geen nieuwe tests, geen beslissingen.** Het rapport telt deze dagen niet mee en toont ze apart.
- T01: oud pad uit op 20 november, v4 100%.
- T02: gepauzeerd, alle laatste mails met code. Hervat op 7 december.
- T04 en T05a mogen doorlopen, maar BFCM-weken tellen niet mee.
- Wel blijven kijken naar uitschrijving en spam: met BFCM-campagnes erbij is de lijst gevoeliger.

## Eerlijk over de aantallen

Met ons verkeer zien we in 6 weken alleen grote verschillen (welcome vanaf ongeveer +36%, checkout +61%, cart +71%). Een klein verschil ligt dus binnen de ruis. Daarom kiezen we bij twijfel altijd de standaard en niet de variant die toevallig voorligt.
