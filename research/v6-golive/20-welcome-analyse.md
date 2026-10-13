# 20 · Waarom verkoopt de oude welcome beter? (13 okt 2026)

Vraag Floris: sinds go-live (8 okt 22:30 UTC) haalt de oude welcome 18 orders en $5,862 ($2.54 per ontvanger), de nieuwe 11 orders en $3,292 ($1.46). Waarom, en wat testen we daartegen?

Alleen gelezen in Klaviyo (flow T4a5Mk "v4 · Welcome", stand 13 okt 09:25 UTC). Niets gewijzigd, niets live gezet. Ruwe data en scripts: scratchpad `golive/wel/` (rep.json, def.json, orders.json, buyers2.json, buyrows.json).

## Kort antwoord

**De oude welcome verkoopt niet meer. Hij krijgt meer orders op zijn naam.** Klaviyo schrijft een order toe aan een mail als iemand die mail opende of erop klikte en binnen 5 dagen bestelt. Twee derde van de welcome-kopers bestelt binnen een uur na W1: ze schreven zich in via de pop-up terwijl ze al aan het winkelen waren. Of zo'n order "van de mail" is, hangt dus vooral af van de vraag of ze de mail toevallig even openden. De oude W1 ("Sarah, Thanks For Joining Us") wordt vaker geopend, dus pakt hij meer van die orders.

Tellen we alle orders van iedereen die W1 kreeg (wel of niet toegeschreven), dan zijn beide armen gelijk:

| Iedereen die W1 kreeg, alle orders daarna | Oud | Nieuw |
|---|---|---|
| Ontvangers W1 (nieuw incl. W0) | 1,216 | 1,221 |
| Kopers | 48 (3.9%) | 52 (4.3%) |
| Orders | 49 | 52 |
| Omzet | $14,076 | $14,064 |
| Omzet per ontvanger | **$11.58** | **$11.52** |
| Waarvan door Klaviyo aan de welcome toegeschreven | 18 orders | 11 orders |

Fisher exact op kopers 48/1,216 tegen 52/1,221: p = 0,76. Er is geen verschil in verkoop. Het verschil zit volledig in de toeschrijving, en die zit volledig in mail 1.

Wat wel echt verschilt: **de nieuwe flow kost half zoveel uitschrijvingen** (W1 2,3% tegen 4,3%, p = 0,005; hele flow 45 tegen 84, p = 0,001). En de oude W1 wordt iets vaker geopend (43% tegen 40%, p = 0,08) en geklikt (3,0% tegen 2,4%, p = 0,45, niet significant).

## 1. Per mail (8 okt 22:30 tot 13 okt 09:25 UTC, flow-values-report per flow_message_id)

Open en klik = uniek, gedeeld door afgeleverd. Orders en omzet = Klaviyo-toeschrijving (Placed Order RSNxYV).

| Mail | Ontv. | Afgel. | Open | Klik | Orders | Omzet | Uitschr. | Spam |
|---|---|---|---|---|---|---|---|---|
| Old · Welcome 1 | 1,216 | 1,174 | 43.2% | 2.98% (35) | **15** | **$4,894** | 51 (4.3%) | 3 |
| Old · Welcome 2 | 922 | 911 | 41.4% | 1.76% (16) | 2 | $831 | 31 (3.4%) | 2 |
| Old · Welcome 3 | 0 | 0 | | | | | | |
| Old · Welcome 4 (alleen openers) | 189 | 188 | 59.0% | 1.06% (2) | 1 | $138 | 2 | 0 |
| Old · Welcome 5 | 1 | 1 | | | | | | |
| **Oud totaal** | **2,328** | | | | **18** | **$5,862** | **84** | 5 |
| W0 (bestaande klant) | 7 | 7 | | 0 | 0 | | 0 | 0 |
| W1 [AB] (A + B) | 1,214 | 1,190 | 39.6% | 2.44% (29) | **8** | **$2,413** | 27 (2.3%) | 2 |
| W2 (Benjamin, tekst) | 761 | 752 | 36.4% | 0.66% (5) | 3 | $879 | 14 (1.9%) | 1 |
| W3 | 296 | 295 | 33.2% | 2.37% (7) | 0 | | 4 (1.4%) | 2 |
| **Nieuw totaal** | **2,278** | | | | **11** | **$3,292** | **45** | 5 |

Waar zit het verschil: **W1** verklaart 7 van de 7 orders en $2,481 van de $2,570 verschil. W2 is gelijk (nieuw 3 tegen oud 2), W3/W4 samen 1 order verschil.

Varianten in W1 (T04): A (codekaart) 632 ontvangen, B (gift card) 598. Alle kopers na W1: A 26 ($7,613), B 25 ($6,152). Geen verschil tussen A en B.

Bijvangst: **Old · Welcome 3 is sinds go-live nooit verstuurd** (0 ontvangen, 0 drops). Het template X6LnJ9 bevat `{{ first_name|default:'there', }}` (komma in de tag), vermoedelijk een renderfout waardoor Klaviyo de mail overslaat. Geen actie nodig (oude arm), wel goed om te weten bij het lezen van de cijfers.

## 2. Timing en aantal mails

Uit de flowdefinitie (tijden in de tijdzone van het profiel):

| Stap | Oud | Nieuw |
|---|---|---|
| Mail 1 | 5 min na inschrijving | 5 min na inschrijving (eerst check: geen order sinds start; wie ooit kocht krijgt W0) |
| Mail 2 | volgende dag 10:00 | volgende dag 10:00 |
| Mail 3 | +1 dag 10:00 (W3, wordt niet verstuurd) | +2 dagen 09:00 (dag 3) |
| Mail 4 | +1 dag (dag 3), alleen openers | +3 dagen 09:00 (dag 6, US/INT) |
| Daarna | W5 dag 5, W6 dag 7, W7 dag 9, W8 dag 10 "Last Call ... Expires Tonight" | W5 dag 10 |
| Mails in de eerste 72 uur | 2, plus W4 voor openers rond uur 58 tot 82 | 3 (W3 rond uur 57 tot 81) |

De eerste twee mails komen in beide armen op exact hetzelfde moment. Frequentie verklaart niets: de oude arm krijgt door de kapotte W3 zelfs minder mails. De nieuwe W1 en W2 hebben wel een skipfilter (geen checkout- of cartmail in de laatste dag); dat scheelt in W2 ongeveer 160 ontvangers (761 tegen 922), maar die mensen kopen dan via die andere flow.

## 3. Aanbod, onderwerp en preview naast elkaar

Beide armen geven **hetzelfde aanbod in mail 1: HI10, 10% op de salesprijs**, zonder deadline. De oude welcome heeft geen gifts, wel "Use code HI10" twee keer in beeld.

| | Oud | Nieuw |
|---|---|---|
| W1 onderwerp | `{{ first_name }}, Thanks For Joining Us` | No PFAS. Here's the paper. And 10%. |
| W1 preview | It's great to have you here | Light Labs report no. 25895. HI10 takes 10% off the sale price. |
| W1 opbouw | 100% beeld: "Welcome to Siraat's Kitchen!", 10% en code HI10 en knop SHOP 10% OFF NOW in het eerste scherm, lijstje voordelen, tweede codebanner. Kort. Links naar /collections/all. Topbalk noemt nog 100-DAY TRIAL. | Codebalk, hero (PFAS-idee), knop, Card Game-regel, labtekst, vergelijking met een PFAS-pan, aanbodkaart (A) of gift card (B), gifts, 2 reviews, knop. Lang (~3,600 px op mobiel). Alle links naar de Pan Pro-pagina met HI10 toegepast. |
| W2 onderwerp / preview | A Note from Benjamin / `{{ first_name }}`, Thanks for joining us | The pan nobody else was making / It's Benjamin. I wanted to write to you myself. (Your 10% is in the P.S.) |
| W2 | Tekst van Benjamin, raadt de snijplank aan met link, HI10 onderaan | Founder note (PFAS, snijplank naar pan, 20 dec 2024, "Skip the heat"), HI10 in de P.S. en aanbodkaart |
| W3 | Hey `{{ first_name }}`, Save 10% On a Lifetime of Use (niet verstuurd) | Has your cookware been tested? / Six things you can check yourself, before you buy. |
| W4 | Straight from the kitchen / Hot off the line | Who are you cooking for? |
| Einde reeks | W8 "Last Call for an Extra 10% Off" / "Expires Tonight" (HI10 verloopt niet echt) | W5 "Tammy is on her fourth pan", laatste keer HI10 |

Het oude onderwerp leest als een bevestiging met je naam erin. Wie net in de pop-up zat en de code zoekt, opent die. Dat is precies het moment waarop twee derde van de kopers bestelt (zie 4).

## 4. Orders: wie, wanneer, wat

Placed Order-events sinds go-live: 911. Daarvan 601 van profielen die sinds go-live op de welcomelijst kwamen, plus 1 buiten de lijst met een welcome-mail. Per koper opgezocht welke W1 hij kreeg en wanneer hij bestelde (Received/Opened/Clicked Email per profiel).

**Tijd tussen W1 en order (alle kopers na W1):**

| | Oud | Nieuw |
|---|---|---|
| Binnen 1 uur | 32 orders, $8,917 (8 openden de mail eerst) | 33 orders, $9,874 (7 openden de mail eerst) |
| 1 tot 24 uur | 15 orders, $4,482 (11 openden eerst) | 16 orders, $3,331 (4 openden eerst) |
| Na 24 uur | 2 orders, $677 | 3 orders, $859 |
| Mail geopend vóór de order | 21 van 49 | 13 van 51 nagekeken |
| Geklikt vóór de order | 11 van 49 | 6 van 51 nagekeken |
| Toegeschreven aan welcome | 18 | 11 |

Het aantal kopers per uur-bucket is in beide armen hetzelfde. Alleen de fractie die de mail vóór de order opende verschilt, en daarmee de toeschrijving. Opvallend: tussen 1 en 24 uur openden 11 van 15 oude kopers de mail eerst, tegen 4 van 16 nieuwe. Dat is het enige stukje waar de oude mail mogelijk meer doet (terugkomen dezelfde dag), maar het levert per saldo niet meer kopers op.

**Gebruik van de code.** HI10 bij 9 van 49 oude en 9 van 51 nieuwe kopers (18%). Andere codes (XXXXXXXX): 4 tegen 3. Vier op vijf kopers betalen dus zonder code; de code is niet de reden dat ze kopen, wel een reden om de mail te openen.

**Orderwaarde.** Toegeschreven: oud $326 gemiddeld (W1 $326), nieuw $299 (W1 $302). Alle kopers: oud gemiddeld $287, mediaan $204; nieuw $270, mediaan $203. Gelijk.

**Producten (alle kopers na W1, aantal orders met het product):**

| | Oud (49) | Nieuw (52) |
|---|---|---|
| Pan Pro Mini/Small/Standard/Large | 23 | 25 |
| 6-delige set | 7 | 13 |
| 12-delige set | 8 | 7 |
| Wok/Deep/Crêpe | 5 | 9 |
| Complete Edition | 3 | 0 |
| Deksel | 6 | 5 |
| Snijplank | 6 | 4 |

Nieuw verkoopt meer 6-delige sets en losse pannen, oud iets vaker de grote bundels. Pan Pro en 6-delige set samen zijn in beide armen ruim de helft: dat zijn de twee producten die in W1 horen.

## 5. Statistiek

Fisher exact (tweezijdig):

| Vergelijking | Oud | Nieuw | p |
|---|---|---|---|
| Toegeschreven orders hele flow per ontvanger | 18 / 2,328 | 11 / 2,278 | 0,26 |
| Toegeschreven orders W1 | 15 / 1,216 | 8 / 1,221 | 0,15 |
| **Alle kopers na W1** | 48 / 1,216 | 52 / 1,221 | **0,76** |
| Open W1 | 507 / 1,174 | 471 / 1,190 | 0,08 |
| Klik W1 | 35 / 1,174 | 29 / 1,190 | 0,45 |
| **Uitschrijvingen W1** | 51 / 1,174 | 27 / 1,190 | **0,005** |
| **Uitschrijvingen hele flow** | 84 / 2,328 | 45 / 2,278 | **0,001** |

**Wordt het verschil groter?** Nee. Toegeschreven orders cumulatief (oud tegen nieuw): 9 okt 2-0, 10 okt 7-1, 11 okt 12-7, 12 okt 15-10, 13 okt 18-11. Het gat ontstond in de eerste twee dagen (7 tegen 1). Sinds 11 okt is het per dag gelijk (11 tegen 10). Alle kopers per dag: oud 1/8/16/10/9/5, nieuw 0/5/9/19/15/4 (8 t/m 13 okt).

**Steekproef.** Bij ~4% kopers per W1-ontvanger is een echt verschil van 25% (4% naar 5%) pas te zien met ~6.700 ontvangers per arm, ongeveer 3,5 tot 4 weken bij het huidige volume (~280 per arm per dag). Na 4,5 dag is niets te beslissen, en zeker niet op Klaviyo-toeschrijving.

## 6. Conclusie

1. Hoofdoorzaak: **toeschrijving, geen verkoop.** Twee derde van de welcome-kopers was al aan het winkelen en bestelt binnen een uur. De oude W1 wordt door die mensen vaker geopend (persoonlijk "Thanks For Joining Us", code direct zichtbaar), dus krijgt hij de orders op zijn naam. Alle kopers geteld: $11.58 tegen $11.52 per ontvanger.
2. Het gat zit volledig in mail 1 en ontstond op dag 1 en 2; het groeit niet.
3. Echte winst van de nieuwe flow: de helft minder uitschrijvingen.
4. Echte les van de oude W1: in de eerste minuten na de pop-up wil iemand de code. Onderwerp en eerste scherm moeten die meteen geven, en de link moet de code op hun bestaande cart zetten. De nieuwe W1 stuurt iedereen naar de Pan Pro-pagina, ook wie een set in de cart heeft.
5. Meetregel voor T01 welcome: beslis op **orders en omzet per W1-ontvanger van alle kopers** (zoals in tabel 4), niet op Klaviyo-toeschrijving. Uitschrijvingen als tweede maat.

## 7. Voorstel: W1-v2 als nieuwe A/B-variant tegen Old · Welcome 1

Bron: `klaviyo/templates/v3/welcome/w1-v2.html` (gebouwd: `w1-v2.klaviyo.html`, `w1-v2-preview.html`). Screenshot 375 px: `research/v6-golive/img/20-w1-v2-375.jpg`. Niet in Klaviyo.

**Idee:** de snelheid en het "hier is je code" van de oude W1, met de lage uitschrijving, het bewijs en de gifts van de nieuwe. Korter, code boven de vouw, cartlink.

**Onderwerpen (5 types, skill siraat-direct-response):**
- Offer: `{{ first_name|default:'Hi' }}, here's your 10%` (gekozen)
- Specificity: `HI10: 10% off, plus 4 gifts`
- Question: `Already picked a pan?`
- Story: `"The last pans we ever have to purchase"`
- Curiosity + benefit: `Thanks for joining. Your code is inside.`

**Preview:** `Thanks for joining. HI10 takes 10% off on top of the sale, sets included.`

**Opbouw (3.435 px op 375 px, incl. footer):**
1. Codebalk YOUR WELCOME 10% · CODE HI10, vaste header (lockup).
2. "Thanks for joining, Sarah. Here is the code you came for."
3. Aanbodblok: 10% on top of the sale, code HI10 als live tekst, "Works on everything, sets included. The 6-piece set: $299, or $269.10 with HI10." Knop "Claim my 10% + gifts" naar /collections/all met HI10 toegepast.
4. **Cartlink**: "Already something in your cart? Apply my 10% to my cart" (/discount/HI10?redirect=/cart). Friction reducer.
5. Card Game-regel (één regel, besluit 7 okt).
6. Korte noot van Benjamin: geen coatings, niets dat kan slijten, Light Labs 31 PFAS, report no. 25895, 75 jaar garantie, 30 dagen retour.
7. "Where most people start": Pan Pro 11″ ($144, $129.60 met HI10) en de 6-delige set ($299, compare-at $598). Dit zijn de twee producten die welcome-kopers het meest kopen.
8. Gifts-strook ($70 in gifts), 2 reviews (R583 Scott Y., R029 Jerry G.), knop met friction reducer, ondertekening Benjamin met P.S. naar W2.

**Aanbod:** HI10, ongewijzigd (geen deadline, DECISIONS). Gifts erbij. Geen nieuwe korting: de code is niet de koopreden (18% gebruikt hem), maar wel de reden om te openen.

**Timing:** 5 minuten na inschrijving, zoals nu. Niet later: de koper zit dan nog in zijn sessie.

**Test:** variant B (gift card) vervangen door W1-v2, want A en B zijn gelijk (26 tegen 25 kopers). Zo loopt in de nieuwe arm A tegen v2, en lezen we beide af tegen Old · Welcome 1 in de 50/50. Primaire maat: kopers en omzet per W1-ontvanger (alle orders binnen 5 dagen, script zoals `buy_an.py`); daarna unieke kliks, uitschrijvingen. Minimaal 4 weken, niet beslissen vóór dag 14.

**QA:** `mail_checks.preview_problems` = 0 en `bg_problems` = 0 (Klaviyo-versie en preview), 48,5 KB, geen em dash, geen horizontaal scrollen op 375 px, ook niet in de Gmail-iOS-simulatie. Django-render op een US-profiel: geen restanten `{{ }}`/`{% %}`.

**Eventueel W2 (niet gebouwd):** W2 is gelijk aan de oude (3 tegen 2 orders), maar klikt slecht (0,66% tegen 1,76%). De oude W2 zet vroeg in de tekst een link naar een startproduct. Voorstel: in de nieuwe W2 na de alinea over de pan één regel "Here is the pan I would start with" met link naar de Pan Pro (HI10 toegepast), en een onderwerptest "A note from Benjamin" (oude onderwerp, 41% open) tegen "The pan nobody else was making" (36%).
