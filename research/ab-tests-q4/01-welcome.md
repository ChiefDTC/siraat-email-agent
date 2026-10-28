# A/B-tests Q4 · Welcome (28 okt 2026)

Vraag Floris: zoveel mogelijk optimaliseren vóór Black Friday. Dit deel gaat over de welcome-flow: **v4 · Welcome `T4a5Mk`** (live) en de oude arm daarvan (de "Old · Welcome 1 tot 8"-tak in dezelfde flow, achter split `119850648`). De oude losse flow `SiaNLu` (EB | Welcome Flow | Updated 02.03.26) staat sinds 8 okt op Draft en verstuurt niets.

Alleen gelezen. Klaviyo (account TdtTzz, revision 2025-10-15): flowdefinitie `T4a5Mk`, flow-messages per actie, `POST /api/metric-aggregates` over **14 okt 00:00 tot 28 okt 00:00 UTC** voor Received Email `YkRM4Q` (uniek, per `$message` en `$variation`), Clicked Email `W247h8` (uniek, alleen `Bot Click` = 0), Placed Order `RSNxYV` (op `$attributed_flow` en `$attributed_message` / `$attributed_variation`), Spam `VQMAAk`, en Unsubscribed `YcWddQ` als losse events per `message_id` (alle methodes, ook de afmelding die bij een spamklacht hoort). Niets gewijzigd in Klaviyo, niets verstuurd. Rekenwerk in de scratchpad (`abq4w/`), hier alleen aggregaten.

Regels (PLAYBOOK 6, het plan van 19 okt): één variabele per test, winnaar op unieke kliks, omzet per ontvanger als controle, geen automatische winnaar, minstens vier weken, maximaal 2 tests per flow, bij twijfel wint A.

---

## 1. Samenvatting

1. **Welcome draait nu op ongeveer 3.000 mails per dag** en leverde in 14 dagen $34.800 toegeschreven omzet op 35.700 mails: **$0,98 per ontvanger**, de nieuwe arm $1,06, de oude arm $0,79. (Het getal $0,88 uit de briefing komt uit een ander venster of uit het flowrapport, dat achterloopt.)
2. **Bijna alle omzet zit in W1.** W1 maakt $2,83 per ontvanger en 85% van de omzet van de nieuwe arm. Daarna valt het weg: W2 $0,34, W3 $0,24, W4-US $0,43, en **W4-INT, W5-US en W5-INT samen 0 orders op 4.100 mails**. Elke procent op W1 is meer waard dan een verdubbeling van W3.
3. **De afmeldingen zitten in W1 en W2:** 1,81% en 1,98% per mail, samen 249 van de 361 afmeldingen in de nieuwe arm. W2 heeft ook de meeste spamklachten (2,0 per 1.000). W4 en W5 zitten onder 1%.
4. **T04 (W1) heeft geen winnaar.** Sinds 15 okt: A $2,72 per ontvanger, B $3,07, 4,0 tegen 4,1% klik, 38 tegen 41 orders. P(B beter op omzet per ontvanger) ongeveer 69%, ver onder de 95% van de regel. Dus **A blijft**, en het W1-slot is vanaf 29 okt vrij.
5. **Vóór BFCM is alleen W1 snel genoeg.** In 21 dagen (29 okt tot 19 nov) ziet W1 op klik een verschil van ongeveer 21%; W2 34%; W4 en W5 pas rond 90%. Omzet per ontvanger is op W1 pas bij +48% in 21 dagen zichtbaar. Beslissen vóór BFCM gaat dus op klik met afmelding als bewaker, omzet per ontvanger als controle.
6. **Advies: twee tests vóór BFCM**, binnen de regel van 2 per flow:
   - **Q1:** het W1-onderwerp over de sale. Dit kan via de API door variatie B van de bestaande A/B te patchen.
   - **Q2:** in W5 een vroege toegang tot Black Friday, in de UI.
   De rest (W2, W3, het aanbod en social proof in W1) start op 7 december.

---

## 2. Cijfers per mail, 14 dagen (14 tot 28 okt)

Klik = unieke menselijke klik per ontvanger. Afm. = afmeldingen per ontvanger (alle methodes). Spam = spamklachten per 1.000 ontvangers. Omzet = Klaviyo-toeschrijving (Placed Order op `$attributed_message`).

### Nieuwe arm (v4, 100% van de instroom sinds 19 okt)

| Mail | Actie / bericht | Moment | Ontvangers | Per dag nu* | Klik | Orders | Omzet | Per ontv. | Afm. | Spam |
|---|---|---|---|---|---|---|---|---|---|---|
| W1 (A/B T04) | 119850659 / `RN7Yy6` | 5 min na inschrijving | 7.690 | ~825 | 4,15% | 81 | $21.783 | **$2,83** | **1,81%** (139) | 1,6 (12) |
| W0 (al klant) | 119850655 / `VZYNbF` | 5 min | 54 | 4 | 7,4% | 0 | $0 | $0,00 | 1,9% (1) | 0 |
| W2 | 119850663 / `RHuJcG` | dag 1, 10:00 | 5.545 | ~620 | 2,00% | 9 | $1.861 | $0,34 | **1,98%** (110) | **2,0** (11) |
| W3 | 119850667 / `SSTz6y` | dag 3, 09:00 | 4.761 | ~540 | 1,01% | 7 | $1.144 | $0,24 | 1,41% (67) | 1,7 (8) |
| W4-US | 119850673 / `XDaaZn` | dag 6, 09:00 | 1.973 | ~250 | 0,71% | 2 | $840 | $0,43 | 0,46% (9) | 0 |
| W4-INT | 119850674 / `TrhmmM` | dag 6, 09:00 | 1.880 | ~200 | 1,33% | 0 | $0 | $0,00 | 0,90% (17) | 0,5 (1) |
| W5-US | 119850679 / `Wp85L8` | dag 10, 09:00 | 1.081 | ~125 | 0,65% | 0 | $0 | $0,00 | 0,74% (8) | 0 |
| W5-INT | 119850680 / `TXF9D2` | dag 10, 09:00 | 1.162 | ~145 | 0,95% | 0 | $0 | $0,00 | 0,86% (10) | 0 |
| **Nieuwe arm** | | | **24.146** | | 2,23% | 99 | $25.628 | **$1,06** | 1,50% (361) | 1,3 (32) |

*Gemiddelde van de laatste 3 dagen. W1 groeide van ~240 per dag (14 okt, 50/50) naar ~825 per dag sinds de oude arm dicht is; W2 tot W5 groeien nog mee.

### Oude arm (loopt leeg)

Split `119850648` staat sinds 19 okt op 100% nieuw. Old · Welcome 1 kreeg sinds 20 okt niemand meer, Old 2 sinds 21 okt niet, Old 4 en 5 zijn leeg. Old 6, 7 en 8 versturen nog aan de laatste instromers en zijn rond 30 okt leeg. Old · Welcome 3 (`VikvdE`) verstuurde in deze 14 dagen niets.

| Mail | Bericht | Ontvangers | Klik | Orders | Omzet | Per ontv. | Afm. | Spam |
|---|---|---|---|---|---|---|---|---|
| Old · Welcome 1 | `WCZQNi` | 1.754 (t/m 19 okt) | 2,34% | 15 | $5.601 | $3,19 | **4,10%** (72) | 4,6 (8) |
| Old · Welcome 2 | `SkvLPj` | 1.805 | 2,11% | 3 | $1.218 | $0,67 | 2,27% (41) | 2,8 (5) |
| Old · Welcome 4 | `YgbdBZ` | 1.120 | 1,79% | 3 | $572 | $0,51 | 2,32% (26) | 2,7 (3) |
| Old · Welcome 5 | `U4ipYq` | 1.127 | 1,69% | 2 | $274 | $0,24 | 1,15% (13) | 0,9 (1) |
| Old · Welcome 6 | `X298nK` | 1.176 | 0,85% | 2 | $977 | $0,83 | 0,85% (10) | 0,9 (1) |
| Old · Welcome 7 | `TkE72p` | 2.446 | 0,57% | 1 | $524 | $0,21 | 0,98% (24) | 0,4 (1) |
| Old · Welcome 8 | `WVvS3m` | 2.112 | 0,66% | 0 | $0 | $0,00 | 0,90% (19) | 0,5 (1) |
| **Oude arm** | | **11.540** | 1,35% | 26 | $9.166 | **$0,79** | 1,78% (205) | 1,7 (20) |

Let op: Old · Welcome 8 heeft het onderwerp "Last Call for an Extra 10% Off" en de preview "Your Extra Discount Expires Tonight". HI10 verloopt niet, dus die deadline is niet waar. De mail is over een paar dagen leeg; daarna alle Old-stappen op Draft zetten (niet archiveren), zoals in PLAYBOOK 7.

### Lopende A/B-tests in welcome

| Test | Waar | A | B | Sinds | Stand (15 okt 00:33 tot 28 okt) | Winnaar? |
|---|---|---|---|---|---|---|
| **T04 W1** | A/B 119850659, A 119850657 (`VnXKz4`, template Sq2bvX), B 119850658 (`SXwPrW`, template Rx7mRa = W1 v3) | "No PFAS. Here's the paper. And 10%." | "{{ first_name }}, here's your 10%" met de W1 v3-template | 8 okt, B vervangen 15 okt | A: 3.712 ontv., 4,04% klik, 38 orders, $10.086, **$2,72**, afm. 1,67%, spam 6. B: 3.723 ontv., 4,14% klik, 41 orders, $11.431, **$3,07**, afm. 1,72%, spam 6 | **Nee.** Klik p ≈ 0,8, orders p ≈ 0,7, P(B beter op omzet per ontvanger) ≈ 69%. Volgens de regel blijft A. B verschilt in onderwerp én template, dus deze uitslag zegt niet wat werkt. Besluitdatum 29 okt (morgen) |
| T01 welcome oud/nieuw | split 119850648 | oud pad | v4 | 8 okt | afgerond 19 okt (100% nieuw) | v4 (besluit Floris) |
| T05b, T17, T07, T06 (plan 19 okt) | W1, W2, W3, aanbod | | | | niet gestart | zie sectie 4 voor de nieuwe volgorde |

Op 44 van de 125 welcome-orders in deze 14 dagen staat geen variatie; dat zijn orders na W0, W2 tot W5 en de oude arm.

---

## 3. Waar de omzet wegvalt en waar de afmeldingen zitten

**Omzet.** De reeks verdient in de eerste minuten en daarna nauwelijks nog.
- W1 maakt $2,83 per ontvanger. Een op de honderd ontvangers koopt via W1, met gemiddeld $269 per order. In de laatste 7 dagen was dat ~5.800 ontvangers en ~$15.800 per week.
- W2 tot W5 maken samen ~$0,15 per ontvanger, ongeveer $3.100 per week. **85% van de omzet komt uit 32% van de mails.**
- **W4-INT en W5 (US en INT) leverden 0 orders op 4.100 mails.** Dat is na de oude Old · Welcome 8 de zwakste plek. Old · Welcome 6 maakte op dezelfde plek in de reeks (dag 7 tot 9) nog $0,83, met een productvergelijking.
- **Hefboom 1: W1.** Op ~$16.000 per week levert elke 5% winst ongeveer $800 per week op. Dat is meer dan W3 en W4 samen verdienen.
- **Hefboom 2: de staart (W4-INT, W5).** De basis is $0. Daar mag de mail een andere taak krijgen: vroege toegang tot Black Friday of een cadeaugids, in plaats van nog een keer HI10.

**Afmeldingen.**
- W1 en W2 samen: 249 van de 361 afmeldingen in de nieuwe arm. Bij het huidige volume is dat **ongeveer 175 per week**.
- W2 heeft per mail de meeste afmeldingen (1,98%) en spamklachten (2,0 per 1.000). W2 is een brief van "Benjamin at Siraat's Kitchen", een dag na de pop-up. Waarschijnlijk herkent een deel van de giveaway-aanmelders de afzender niet (research/afmeldingen/01, punt 3).
- Spam in de hele nieuwe arm is 1,3 per 1.000. Dat ligt boven de grens van 1 per 1.000 (02-best-practices).
- Wat een afmelding kost: een nieuwe aanmelder levert in de eerste maand $3,55 op via alle kanalen (01-data). Een derde minder afmeldingen in W1 en W2 (~58 per week) is dus ongeveer $100 tot $200 per week, plus wat die mensen in december kopen.

---

## 4. Voorgestelde tests, gesorteerd op verwachte extra omzet per week

Rekenbasis (laatste 7 dagen, nieuwe arm op 100%): W1 ~5.800 ontvangers per week à $2,72, W2 ~4.350 à $0,34, W3 ~3.800 à $0,24, W4-US ~1.750 à $0,43, W4-INT ~1.400 en W5 ~1.900 à $0 (W5 groeit nog naar ~2.800).
- **Power** (80%, 5% tweezijdig, 50/50):
  - Klik: n per arm = 15,7 × 2 × (1−p) / (p × d²), met d = de relatieve verbetering.
  - Omzet per ontvanger op W1: variatiecoëfficiënt ~11, uit 1,05% kopers à $269 met spreiding ~$150.
- **"Vóór BFCM"** betekent: beslist op data tot en met 19 november, zodat de winnaar vanaf 20 november (begin van de bevriezing) door Black Friday (27 nov) en Cyber Monday (30 nov) loopt.
- In november stijgt de instroom waarschijnlijk 2 tot 4 keer (vorig jaar 3,5 tot 16 keer meer orders per week, plan 19 okt). Daardoor zijn de tests sneller rond.
- **Spanning met de regel van vier weken.** Een test die op 29 okt start, heeft pas op 26 nov vier weken. Voor Q1 stel ik voor:
  - op 19 nov te beslissen, alleen als het verschil op klik er dan is;
  - anders laten doorlopen;
  - de BFCM-dagen apart te rapporteren.
  [VRAAG FLORIS]

### Q1 · W1-onderwerp: de sale noemen (voor de sale, start 29 okt)

| | |
|---|---|
| Mail | W1, A/B 119850659 (hoofdactie 119850656), variaties 119850657 (A) en 119850658 (B) |
| Hypothese | In een sale van 50 en straks 70% zegt het huidige onderwerp alleen "10%". Een nieuwe aanmelder komt van een pop-up in de sale. Een onderwerp dat zegt dat de 10% bovenop de sale komt, sluit aan op wat hij net zag en trekt meer kliks. HexClad en Our Place maken van hun welkomstmail direct de toegang tot de lopende sale (concurrentie-idee 4). Het onderwerp noemt geen percentage voor de sale, zodat het van 50% naar 70% en terug niet aangepast hoeft te worden |
| Wat verandert | **Onderwerp.** Preview, template (Sq2bvX), afzender en aanbod gelijk aan A |
| Vijf onderwerpen | Curiosity+benefit "The sale price, then 10% more" · Specificity "HI10: 10% on top of the sale" · Question "Saw the sale? Your 10% stacks." · Story (geen woordelijke review die past, vervalt) · Offer "Your 10% works on top of the sale" |
| A / B | A "No PFAS. Here's the paper. And 10%." (huidig, T04-winnaar volgens de regel). B **"Your 10% works on top of the sale"** (34 tekens). Feit: HI10 stapelt op 50 en 70% (DECISIONS 19 okt) |
| Primaire maat | Unieke klik (Bot Click uit). Bewaker: afmelding (niet meer dan +20% relatief) en spam. Controle: omzet per ontvanger |
| Volume en looptijd | ~412 per arm per dag. Na 21 dagen (19 nov) ~8.650 per arm: **klik zichtbaar vanaf +21%** (d = 0,20 vraagt 9.170 per arm, 22 dagen); afmelding zichtbaar vanaf ±31%; omzet per ontvanger pas vanaf +48% (+20% vraagt ~119 dagen). Met de Halloween- en novemberinstroom gaat het sneller |
| Verwachte extra omzet | W1 ~$15.800 per week. Winnend onderwerp +4 tot 10% omzet = **$630 tot $1.580 per week**, in de BFCM-weken bij dubbele instroom tot ~$3.000. Kans dat B wint: middel (~50%) |
| Risico | Laag tot middel. Een sale-onderwerp kan meer koopjesjagers laten klikken die zich later afmelden; daarom de bewaker. Geen nep-urgentie, geen deadline (HI10 heeft er geen) |
| Klaviyo | **Via de API.** De A/B 119850659 bestaat al en loopt. Stappen: `PATCH /api/flow-actions/119850658/`, met als `subject_line` het nieuwe onderwerp, `preview_text` gelijk aan A en `template_id` Sq2bvX in plaats van Rx7mRa. Dan zijn A en B gelijk op het onderwerp na. Meten vanaf het tijdstip van de patch, op `$variation` (`SXwPrW` = B). De verdeling blijft 50/50 en de winnaar handmatig. Let op: LOG 7 en 12 okt meldt dat een PATCH op een lopende A/B eerder werd geweigerd. Probeer het één keer. Lukt het niet, dan in de UI: T04 beëindigen met A, en een nieuwe A/B op W1 zoals in het plan van 19 okt. Eerst T04 formeel afsluiten (regel in `research/testing/results.csv`) |
| Vóór BFCM? | **Ja**, als het verschil op klik minstens ~20% is. Anders loopt de test door de sale en beslissen we in december op de dagen buiten de sale |

### Q2 · W5: vroege toegang tot Black Friday (alleen nov, start ~5 nov)

| | |
|---|---|
| Mail | W5-US 119850679 en W5-INT 119850680 (gewone mails, nu 0 orders op 2.243) |
| Hypothese | Wie na 10 dagen en vijf mails niet kocht, wacht vaak op een betere deal. Dat zegt hij niet, maar Black Friday is drie weken weg. Een eerlijke vroege toegang ("you'll get the Black Friday prices a day before everyone else") geeft hem een reden om te blijven. Dan koopt hij op Black Friday via mail in plaats van via een advertentie. De huidige W5 ("Tammy is on her fourth pan", laatste noot over HI10) levert nu niets op. Concurrenten sturen nog niets over BFCM (tijdlijn dag 16) |
| Wat verandert | **Aanbod en inhoud van de mail** (de hele mail is de variabele, zoals bij T19). A = huidige W5. B = korte brief van Benjamin: Black Friday-datum, wat de vroege lijst krijgt, één knop "Put me on the early list" (de klik is de aanmelding, via een gelinkte pagina of een segment "clicked W5-B early link"), daaronder een losse pan voor wie nu al wil |
| Vijf onderwerpen (B) | Curiosity+benefit "A day before everyone else" · Specificity "Black Friday, one day early" · Question "Waiting for Black Friday?" · Story "Tammy is on her fourth pan" (A blijft A) · Offer "Early access to our Black Friday prices" |
| Primaire maat | Unieke klik (aanmelding voor vroege toegang), bewaker afmelding. Echte uitkomst: omzet per ontvanger tot en met 30 nov (inclusief Black Friday-orders van de lijst) |
| Volume en looptijd | ~135 per arm per dag (US en INT samen). In 15 dagen (5 tot 19 nov) ~2.000 per arm: klik pas zichtbaar bij +90%. Maar het doel is vooral om de lijst te bouwen. Het verschil in kliks (verwacht 0,8% tegen 3 tot 6%) is groot genoeg om in een week te zien |
| Verwachte extra omzet | 2.000 tot 2.800 ontvangers per week × 4% aanmeldingen × 10 tot 20% koopt op BF × $250 = **$200 tot $560 per week** aan BFCM-omzet, plus wat de huidige W5 mist ($0). Onzeker |
| Risico | Middel. Vroege toegang moet echt zijn (een link of collectie die een dag eerder opengaat), anders is het nep-schaarste. Datum en vorm van de vroege toegang ontbreken nog [VRAAG FLORIS]. Geen datum in de mail tot Floris die geeft (DECISIONS 7 okt) |
| Klaviyo | **Alleen in de UI**: nieuwe A/B op een gewone mail kan niet via de API. Claude bouwt de B-template (vaste header en footer, lockup, `build_template.py`, QA), Floris maakt de A/B en start hem. Na 30 nov de A/B beëindigen en W5 weer op A |
| Vóór BFCM? | **Ja, het moet ervoor**, anders heeft het geen nut. Bouwen 29 okt tot 3 nov, live uiterlijk 5 nov |

### Q3 · W2-onderwerp: "A note from Benjamin" (T17 uit het plan van 19 okt, start 7 dec)

| | |
|---|---|
| Mail | W2, actie 119850663, afzender "Benjamin at Siraat's Kitchen" |
| Hypothese | De oude W2 met hetzelfde verhaal en het onderwerp "A Note from Benjamin" maakte in deze 14 dagen $0,67 per ontvanger, tegen $0,34 voor W2. Een onderwerp dat zegt wat de mail is (een brief van de oprichter), wordt herkend. Dat wint van een productclaim en kan ook de spamklachten op W2 (2,0 per 1.000) verlagen |
| Wat verandert | Onderwerp |
| Vijf onderwerpen | Curiosity+benefit "The pan nobody else was making" (A) · Specificity "December 20, 2024" · Question "Can I tell you why I made this?" · Story "A note from Benjamin" (B, geen review nodig) · Offer "Your 10% is in the P.S." |
| Primaire maat | Unieke klik. Bewakers: afmelding en spam (beide moeten dalen of gelijk blijven). Controle: omzet per ontvanger |
| Volume en looptijd | ~310 per arm per dag. Klik in 21 dagen zichtbaar vanaf +34%, in 28 dagen +30%, +20% vraagt ~62 dagen. Spam is te zeldzaam om te toetsen; alleen richting |
| Verwachte extra omzet | W2 ~$1.480 per week × +20 tot 40% = **$300 tot $600 per week**, plus ~10 tot 20 minder afmeldingen per week |
| Risico | Laag |
| Klaviyo | Alleen UI (W2 is een gewone mail). Variatie B alleen het onderwerp, preview gelijk |
| Vóór BFCM? | **Nee.** Welcome heeft vóór BFCM al twee tests (Q1, Q2). Start 7 dec, beslissen half januari. Als Floris liever T17 dan Q2 draait, kan T17 op 29 okt starten. Een besluit vóór BFCM kan alleen als het verschil groter is dan 34% |

### Q4 · W1-onderwerp: social proof tegen authority (T05b, start 7 dec of na Q1)

| | |
|---|---|
| Mail | W1, dezelfde A/B 119850659 |
| Hypothese | Na Q1 weten we of de sale in het onderwerp werkt. Buiten de sale is de vraag of een groot, echt getal ("100,000+ happy customers") bij een koude inschrijver meer kliks trekt dan het labrapport |
| Wat verandert | Onderwerp |
| A / B | A = winnaar Q1, of "No PFAS. Here's the paper. And 10%." buiten de sale. B "100,000+ happy customers. Here's your 10%." |
| Primaire maat | Unieke klik, bewaker afmelding, controle omzet per ontvanger |
| Volume en looptijd | Als Q1: +20% in ~22 dagen, kleinere verschillen in 4 tot 6 weken |
| Verwachte extra omzet | +3 tot 8% op ~$15.800 = **$470 tot $1.260 per week** (plan 19 okt rekende $1.600 tot $4.300 per maand bij 600 per dag) |
| Risico | Laag |
| Klaviyo | API, door variatie B opnieuw te patchen (onderwerp), zoals bij Q1 |
| Vóór BFCM? | **Nee**, het W1-slot is tot 19 nov bezet door Q1. Daarna door BFCM, start 7 dec |

### Q5 · W1: verwachting zetten en "fewer emails" bovenaan (afmeldingen, na Q4 of in januari)

| | |
|---|---|
| Mail | W1, variatie B via template |
| Hypothese | De helft van de afmelders gebruikt de afmeldknop van de mailbox zonder de mail te openen (01-data, punt 2). Giveaway-aanmelders herkennen W1 niet als iets waarvoor ze zich aanmeldden. Eén regel bovenaan helpt: wat je krijgt en hoe vaak ("Two or three emails a week from us: recipes, care tips and our best prices. Fewer? Choose here."), plus de link naar de voorkeuren. Dan daalt de afmelding zonder dat klik of omzet daalt (02-best-practices, maatregel 7) |
| Wat verandert | Lengte en inhoud bovenaan (één regel en een link). Onderwerp en aanbod gelijk |
| Primaire maat | **Afmelding plus spam** (bewaakte maat), met klik en omzet per ontvanger als bewaker (mag niet meer dan 10% dalen) |
| Volume en looptijd | Afmelding 1,8%. Min 30% (naar ~1,25%) is in ~23 dagen zichtbaar, min 20% in ~52 dagen |
| Verwachte extra omzet | ~30 tot 40 afmeldingen per week minder × $3,55 per aanmelder per maand, de helft echt extra = **$50 tot $120 per week**, oplopend omdat ze op de lijst blijven voor december |
| Risico | Laag, mits de voorkeurenpagina echt een "minder mail"-keuze heeft. Anders is de link een belofte die we niet waarmaken. De opt-down is nog niet gebouwd [VRAAG FLORIS] |
| Klaviyo | API (PATCH variatie B met een nieuwe template-ID). Claude bouwt de kopie van de A-template met alleen die regel extra |
| Vóór BFCM? | **Nee**, het W1-slot is bezet. Beter: de opt-down eerst bouwen (02-best-practices, maatregel 4) |

### Q6 · W3-hero: pan in gebruik tegen certificaat (T07, start 7 dec)

| | |
|---|---|
| Mail | W3, actie 119850667, template VCjUYQ |
| Hypothese | W3 is gestegen van $0,06 naar $0,24, maar klikt maar 1,0%. Vier van de zeven beeld-hero's in de historische top 10 tonen de pan tijdens het koken. Een certificaat als eerste beeld trekt minder dan eten in de pan |
| Wat verandert | Hero |
| Primaire maat | Unieke klik, controle omzet per ontvanger |
| Volume en looptijd | ~270 per arm per dag: +40% in ~28 dagen, +30% in ~50 dagen |
| Verwachte extra omzet | W3 ~$900 per week × +20 tot 50% = **$180 tot $450 per week** |
| Risico | Laag. Bestaand beeld uit de shoot, flash-stijl, geen nieuwe AI-letters |
| Klaviyo | Alleen UI (gewone mail) |
| Vóór BFCM? | Nee |

### Q7 · W4-US: cadeaugids in november (alternatief voor Q2)

| | |
|---|---|
| Mail | W4-US, actie 119850673 |
| Hypothese | Eén op de vijf kopers koopt de pan als cadeau (enquête okt). In november zoekt een deel van de nieuwe aanmelders een cadeau, niet een pan voor zichzelf. Een W4 die de maatkeuze stelt als "voor wie koop je?" (Mini voor iemand alleen, Standard voor een stel, set voor een gezin) past bij die vraag |
| Wat verandert | Onderwerp en invalshoek van de mail. A "Who are you cooking for?". B "Buying a pan as a gift? Here's the size." met dezelfde maatkaarten, nu met de ontvanger als kop |
| Primaire maat | Unieke klik, controle omzet per ontvanger |
| Volume en looptijd | ~125 per arm per dag, klik 0,7%: in 21 dagen pas bij +90% zichtbaar. Geen echte test vóór BFCM, alleen richting |
| Verwachte extra omzet | W4-US ~$750 per week × +20 tot 50% = **$150 tot $375 per week**, alleen in nov en dec |
| Risico | Laag. Telt als derde test in welcome, dus alleen in plaats van Q2 |
| Klaviyo | Alleen UI |
| Vóór BFCM? | Alleen als vaste wissel van 5 nov tot 24 dec, niet als test met een winnaar |

### Q8 · Welkomstaanbod in de sale: HI10 tegen geen extra code (marge, januari)

| | |
|---|---|
| Mail | Hele reeks (random split vóór W1 in de prospect-tak, plus kopieën van W1 tot W5 zonder code) |
| Hypothese | Met 70% korting maakt 10% extra (dus 73%) weinig verschil in koopgedrag, maar kost het 10% van de W1-omzet. Een nieuwe aanmelder in de sale koopt om de sale, de 4 gifts en het rapport. Zonder HI10 blijft de omzet per ontvanger bijna gelijk en stijgt de marge |
| Wat verandert | Aanbod (kortingshoogte voor nieuwe inschrijvers in de sale) |
| A / B | A HI10 bovenop de sale. B geen extra code, "the sale price is the price", plus de 4 gifts. (Alternatief: B = 15%, maar dat kost marge zonder duidelijke reden.) |
| Primaire maat | **Marge per ontvanger** binnen 14 dagen (omzet min korting), alle orders van het cohort, Bayesiaans. Controle: omzet per ontvanger, afmelding |
| Volume en looptijd | Omzet per ontvanger op W1 heeft een variatiecoëfficiënt van ~11: −10% is pas na maanden zichtbaar. Een beslissing kan alleen Bayesiaans (P(B ≥ A − 5% op marge)) na 6 tot 8 weken |
| Verwachte extra omzet | Omzet −$1.600 tot +$300 per week, **marge +$0 tot +$1.600 per week**. Grootste onzekerheid in deze lijst |
| Risico | Middel tot hoog. Welkomstaanbod weghalen midden in BFCM kan W1 raken, juist in de duurste weken. HI10 staat op couponsites |
| Klaviyo | Alleen UI (split en vijf kopieën; de flowdefinitie is via de API niet aan te passen) |
| Vóór BFCM? | **Nee.** Advies: in de sale HI10 houden (besluit 19 okt). Na de sale toetsen tegen $25 off $150+ (T06). Wil Floris toch een ander percentage in de sale, dan zonder test als besluit, met een voor/na-meting |

### Overzicht

| # | Test | Mail | Variabele | Extra per week | Maat | Kan via | Vóór BFCM |
|---|---|---|---|---|---|---|---|
| Q1 | Sale in het onderwerp | W1 | Onderwerp | $630 tot $1.580 | Klik, bewaker afmelding | **API** (PATCH variatie B) | Ja, bij ≥ +20% klik |
| Q4 | Social proof tegen authority | W1 | Onderwerp | $470 tot $1.260 | Klik, bewaker afmelding | API | Nee (7 dec) |
| Q3 | "A note from Benjamin" | W2 | Onderwerp | $300 tot $600 | Klik, bewaker afmelding en spam | UI | Nee (7 dec) |
| Q2 | Vroege toegang tot BF | W5 | Aanbod en inhoud | $200 tot $560 | Klik, daarna omzet t/m 30 nov | UI | Ja, moet ervoor |
| Q6 | Hero in gebruik | W3 | Hero | $180 tot $450 | Klik | UI | Nee |
| Q7 | Cadeaugids | W4-US | Invalshoek | $150 tot $375 (nov, dec) | Klik | UI | Alleen als wissel |
| Q5 | Verwachting en "fewer" | W1 | Lengte | $50 tot $120, minder afmeldingen | Afmelding, bewaker klik | API | Nee |
| Q8 | Geen HI10 in de sale | Reeks | Aanbod | Marge $0 tot $1.600 | Marge per ontvanger | UI | Nee |

Q1 en Q4 kunnen niet tegelijk (zelfde mail). De extra omzet tel je dus niet op.

---

## 5. Kalender welcome

| Wanneer | Actie | Wie |
|---|---|---|
| **29 okt** | T04 sluiten: A blijft (regel). Regel in `research/testing/results.csv`. **Q1** live via PATCH van variatie 119850658 (onderwerp B, template Sq2bvX), of in de UI als de PATCH wordt geweigerd | Floris akkoord, Claude patcht en controleert |
| 29 okt tot 3 nov | Q2-template W5 bouwen (Draft, QA, previews). Floris geeft de Black Friday-datum en de vorm van de vroege toegang | Claude, Floris |
| ~30 okt | Old · Welcome 6 tot 8 zijn leeg: Old-stappen op Draft (Old 8 heeft een onjuiste deadline) | Floris of Claude na akkoord |
| **5 nov** | **Q2** live in de UI op W5-US en W5-INT | Floris |
| elke maandag | `scripts/test_report.py` met de sale-dagen apart | Claude |
| **19 nov** | Q1 beslissen op klik (data 29 okt tot 19 nov), alleen bij ≥ +20% en geen hogere afmelding. Anders laten doorlopen | Claude rapport, Floris |
| 20 nov t/m 6 dec | Bevriezing. Q2 tot 30 nov, dan W5 terug op A | |
| **7 dec** | Rapport met de periodes vóór, tijdens en na de sale. Start **Q4** (W1, als Q1 klaar is) en **Q3** (W2). **Q6** (W3) volgt zodra Q3 beslist is (regel: maximaal 2 tests per flow) | Floris |
| januari | **Q5** (na de opt-down) en **Q8/T06** (aanbod, marge) | |

---

## 6. Open punten voor Floris

1. Mag Q1 op 19 nov beslist worden (na 3 weken) als het verschil op klik duidelijk is, ook al zegt de regel minstens vier weken?
2. Black Friday: vanaf welke datum gelden de prijzen? Kan de vroege lijst echt een dag eerder (link, collectie of code)? Zonder dat geen Q2.
3. Q2 (W5, vroege toegang) of T17 (W2-onderwerp) als tweede test vóór BFCM? Advies: Q2, omdat die alleen nu zin heeft.
4. Akkoord dat T04 met A sluit (B lag voor met $3,07 tegen $2,72, maar P ≈ 69%)?
