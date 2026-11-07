# Pop-up trigger A/B/C-test (Alia, 7 nov 2026)

Aanleiding: klanten zeggen dat de pop-up te snel komt. Huidige instelling in Alia: "When page loads" (direct) plus Smart Trigger, opnieuw na 5 dagen als hij gesloten is.

## Wat we weten
- De pop-up is Alia ("Card Game"), goed voor ongeveer 88% van de aanmeldingen (720 tot 1.000 per dag, research/smooche/00-plan.md). 60% van de kopers uit de pop-up koopt binnen 10 minuten. Elke verloren aanmelding kost dus direct omzet: test, niet zomaar omzetten.
- Op elke pagina laadt ook OptiMonk naast Alia (research/cro/02-pdp-audit.md). Checken of OptiMonk geen eigen pop-up toont; een tweede pop-up kan het "te snel"-gevoel versterken.
- Live meting bij concurrenten lukte niet: het netwerk van deze omgeving blokkeert hun sites en de pop-upscripts. Smooche (eerdere teardown): schermvullende kraskaart, timing niet gemeten.

## Bewijs (vooral leveranciersdata, via zoekresultaten)
- Omnisend, 1,24 mld weergaven: beste aanmeldratio bij 6 tot 10 s vertraging (2,4%), direct 1,9%. Getsitecontrol: meer dan 5 s 5,26% tegen 4,01% onder 2 s. Winst is echt maar klein (ongeveer +25% relatief per weergave).
- Scroll en exit intent: bronnen spreken elkaar tegen. Exit intent op mobiel is een noodsignaal (terugknop, snel omhoog scrollen), weinig data.
- Alia Smart Trigger: AI toont de pop-up een extra keer aan bezoekers die waarschijnlijk aanmelden, standaard alleen mobiel, kan vuren vóór je vertraging. "Tot 40% meer aanmeldingen" is een claim van Alia zelf.
- Google straft schermvullende pop-ups direct na binnenkomst uit Google-zoekresultaten op mobiel. Geldt niet voor Meta/TikTok-verkeer, wel voor organisch en merkzoekverkeer.
- Over kwaliteit van aanmelders per trigger is geen goed onderzoek; zelf meten.

## Voorstel: drie varianten, alleen de trigger verschilt
| | A (controle) | B (kort uitstel) | C (op interesse) |
|---|---|---|---|
| Trigger | When page loads | 8 s vertraging OF 40% scroll, wat eerst komt | 20 s vertraging OF exit intent (desktop); liever 2e paginaweergave als "Build a trigger" dat kan |
| Smart Trigger | aan | aan | aan |
| Opnieuw na sluiten | 7 dagen | 7 dagen | 7 dagen |

A blijft nodig als meetlat. Controleer in preview dat Smart Trigger niet binnen de 8 of 20 s van B en C vuurt; anders lost het de klacht niet op.

Gelijk houden in alle drie: ontwerp, aanbod en tekst; "Don't trigger if another popup viewed"; geen pop-up op cart, checkout, account en bedankpagina; niet tonen aan bekende abonnees en aan verkeer met utm_medium=email of sms.

## Opzet en duur
- In Alia de huidige pop-up twee keer dupliceren als variant, alleen de trigger aanpassen, handmatige verdeling 33/33/33, Smart Testing uit (dat schuift verkeer naar een winnaar en maakt de test onzuiver).
- Winnaar kiezen op **aanmeldingen per bezoeker** (of aantal aanmeldingen per arm bij gelijke verdeling), niet op Alia's aanmeldratio per weergave: B en C krijgen minder weergaven en lijken daardoor beter dan ze zijn. Omzet per bezoeker als vangrail.
- Steekproef: bij 4% basis en +15% verschil ongeveer 18.000 tot 22.000 bezoekers per arm. Bij 5.000 tot 15.000 bezoekers per dag: 4 tot 13 dagen. Minimaal 7 volle dagen, liefst 14, niet vroeg stoppen.
- Na 30 dagen per variant de eerste-aankoopratio van aanmelders vergelijken (als Alia de variant meegeeft aan Klaviyo; alia_popup_name staat al op het profiel).
- Let op: Black Friday vertekent gedrag; herhaal de winnaar in januari.

## Snelle winst los van de test
- Opnieuw tonen na sluiten van 5 naar 7 dagen.
- Uitsluiten van cart/checkout en van bezoekers uit e-mail/sms.
