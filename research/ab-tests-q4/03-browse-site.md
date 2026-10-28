# A/B-tests Q4 · Browse, Browse Triple Pixel en Site abandonment (28 okt 2026)

Deel 3 van 4. Flows: **v4 · Browse abandonment WdRz5k**, **v4 · Browse abandonment · Triple Pixel QNZyEb**, **v4 · Site abandonment VLGhbR** (ID's opgezocht via de flownaam). Oude browseflows voor de vergelijking: Wj6x6V (EB Browse, Klaviyo Viewed Product) en TyEjuQ (EB Browse · Triple Pixel), beide sinds 8 okt Draft.

Alleen gelezen. Klaviyo-API (account TdtTzz): flowdefinities, `flow-values-reports` per bericht (conversie Placed Order RSNxYV), `metric-aggregates` op Received Email YkRM4Q, Clicked Email W247h8, Placed Order (`$attributed_flow`, `$attributed_message`, `$attributed_variation`), Viewed Product XNtYMB (Klaviyo onsite), Viewed Product - Triple Pixel V48nhq en Active on Site UdCdLD, plus Placed Order- en Viewed Product-events (alleen producttitel, prijs en bedrag, geen profielgegevens in dit stuk). Niets gewijzigd in Klaviyo, niets verstuurd. Rekenwerk in de scratchpad (`ab03/`), niet in de repo.

Regels: PLAYBOOK 6 en het plan van 19 okt (`research/flows-audit/2026-10-19-ab-tests.md`): één variabele, minimaal 4 weken, geen automatische winnaar, maximaal 2 tests per flow (T02 telt als één), bij twijfel wint A. Test-ID's in dit stuk heten **BR1 tot BR5** (T21 tot T26 zijn al in gebruik in deel 1, 2 en 4); T16 en T19 houden hun nummer uit het plan van 19 okt.

---

## 1. Samenvatting voor Floris

1. **Browse verdient per dag ongeveer $530 minder dan de oude flows ($825 naar $293), en dat komt door twee dingen: minder bereik en kleinere orders.** Hoe vaak een bereikte bekijker koopt is gelijk gebleven (0,6 tot 0,7%).
2. **Ordergrootte is de hoofdoorzaak van de lagere omzet per ontvanger.** De gemiddelde browse-order daalde van $315 (oude flows, 24 sep tot 8 okt) naar $151 (19 tot 28 okt). Drie redenen: (a) de sale maakt losse pannen goedkoper (Deep Pan Pro $305 naar $119, Wok $194 naar $119, Pan Pro Large $209 naar $149; losse-pan-order in browse $215 naar $128), (b) sets vielen weg uit browse: 15 van 47 orders waren een set, nu 1 van 16, terwijl winkelbreed het setaandeel gelijk bleef (18 tot 30%) en 20% van de bekeken producten een set is, (c) 3 van de 16 browse-orders zijn $0-orders (winkelbreed steeg het aandeel $0-orders van 2% naar 10%, vooral Pan Pro Standard).
3. **De hogere "orders per 1.000" is voor een deel schijn.** Zonder de $0-orders is het 3,2 per 1.000, gelijk aan vroeger. De klikdaling (per verstuurde mail) komt doordat nu bijna de helft van de mails een tweede mail is (B2, 0,8 tot 1,4% klik). De eerste mail klikt 2,8%, net als de oude flow (2,9%).
4. **Volume: 902 naar ~490 mails per dag, maar het aantal bereikte mensen daalde harder.** De oude flows stuurden één mail, vaak twee keer aan dezelfde persoon (Klaviyo- en TP-flow). Nu krijgen ~285 mensen per dag een eerste mail (WdRz5k ~205, QNZyEb ~80). De bekijkers zijn niet minder geworden (1.150 naar 1.400 per dag). Het verschil zit in de filters, vooral "geen welcome-mail in 7 dagen" (30% van de bekijkers, bewust zo gekozen). Een deel van de oude browse-omzet was dus welcome-omzet: die staat nu op welcome.
5. **Triple Pixel neemt niets weg, maar voegt toe.** QNZyEb krijgt alleen bekijkers die Klaviyo zelf niet ziet (dedupe werkt twee kanten op) en haalt met TP · B1 de beste cijfers van alle browsemails ($1,20 per ontvanger, 3,75% klik). Het zwakke punt is TP · B2-NOTCLICKED: 0,75% klik, 0,76% uitschrijving en **2 spamklachten op 397 afgeleverd (0,50%)**, boven de Gmail-grens van 0,3%.
6. **Vijf tests plus twee uit het oude plan, samen ongeveer $300 tot $800 extra per week vóór de sale, $600 tot $1.500 in november door het volume.** Bovenaan: de eerste mail laten aansluiten op de sale (BR1), de product-eerst-opbouw van TP · B1 ook in WdRz5k (BR2) en een setaanbeveling in B2 op basis van het bekeken product (BR3). Omzet per ontvanger is in browse niet hard te meten (500+ dagen voor +30%); beslissen op klik met omzet als richting, en alleen grote verschillen.
7. **Niet testen maar meteen doen:** TP · B2-NOTCLICKED moet minder vaak (BR5 als holdout of direct uit), en het bereik van Site (VLGhbR) is sinds 15 okt van ~250 naar ~55 mails per dag gezakt; eerst uitzoeken.

---

## 2. Cijfers per mail, afgelopen 14 dagen (14 okt 00:00 tot 28 okt 00:00 UTC)

Klik = unieke klik per ontvanger. Omzet = Klaviyo-toeschrijving op Placed Order. Uitschrijving per afgeleverde mail. "Test" = stand van de lopende test op die mail.

### 2.1 Browse WdRz5k (trigger Viewed Product XNtYMB, 1 uur wachten, B2 na 2 dagen 09:00)

| Mail | Actie | Ontv. | Klik | Orders | Omzet | Per ontv. | Uitschr. | Spam | Test |
|---|---|---|---|---|---|---|---|---|---|
| B1 (pan-pad) | 119850693 | 2.357 | 2,46% | 8 | $786 | $0,33 | 0,47% | 1 | **T05a live** (zie 2.4) |
| B2-NOTCLICKED | 119850700 | 2.141 | 1,35% | 6 | $1.495 | $0,70 | 0,43% | 0 | geen; T19 gepland 5 nov |
| B1-ACC | 119850694 | 514 | 3,31% | 5 | $493 | $0,96 | 1,18% | 0 | geen |
| Old · Browse 1 (controle-arm) | 119850689 | 128 | 3,91% | 0 | $0 | $0 | 2,40% | 0 | T01 afgerond 19 okt, krijgt niemand meer |
| B2-CLICKED · pan nocode · T02-B | 119850707 | 28 | 7,1% | 1 | $599 | | 0 | 0 | **T02 live** (code tegen geen code) |
| CODE · B2-CLICKED · pan (T02-A) | 119850706 | 20 | 20,0% | 1 | $133 | | 0 | 0 | **T02 live** |
| B2-CLICKED · acc nocode · T02-B | 119850709 | 4 | | 1 | $89 | | 0 | 0 | T02 live |
| CODE · B2-CLICKED · acc (T02-A) | 119850708 | 3 | | 0 | $0 | | 0 | 0 | T02 live |
| B2-CLICKED · pan nocode · cooldown | 119850702 | 1 | | 0 | $0 | | 0 | 0 | geen |
| **Flow totaal** | | **5.196** | **2,29%** | **22** | **$3.595** | **$0,69** | **0,57%** | **1** | |

### 2.2 Browse Triple Pixel QNZyEb (trigger V48nhq, live sinds 19 okt 19:05, 9 mails)

| Mail | Actie | Ontv. | Klik | Orders | Omzet | Per ontv. | Uitschr. | Spam | Test |
|---|---|---|---|---|---|---|---|---|---|
| TP · B1 | 121177227 | 586 | 3,75% | 5 | $701 | **$1,20** | 0,18% | 0 | geen (onderwerp = variant A van B1) |
| TP · B2-NOTCLICKED | 121177242 | 401 | 0,75% | 1 | $143 | $0,36 | 0,76% | **2** | geen |
| TP · B1-ACC | 121177228 | 72 | 2,78% | 0 | $0 | $0 | 0 | 0 | geen |
| TP · CODE · B2-CLICKED · pan (T02-A) | 121177250 | 7 | | 0 | $0 | | 0 | 0 | **T02 live** |
| TP · B2-CLICKED · pan nocode · T02-B | 121177251 | 2 | | 0 | $0 | | 0 | 0 | **T02 live** |
| overige 4 mails (acc-code, cooldown) | | 0 | | | | | | | T02 live, nog geen ontvangers |
| **Flow totaal** | | **1.068** | **2,62%** | **6** | **$844** | **$0,79** | **0,38%** | **2 (0,19%)** | |

Spam: beide klachten op TP · B2-NOTCLICKED, 0,50% van de afgeleverde mails. De 1 klacht op 104 uit de opdracht is inmiddels 2 op 1.045 voor de hele flow.

### 2.3 Site abandonment VLGhbR (trigger Active on Site UdCdLD, 2 uur wachten, A2 na 2 dagen 09:00)

| Mail | Actie | Ontv. | Klik | Orders | Omzet | Per ontv. | Uitschr. | Spam | Test |
|---|---|---|---|---|---|---|---|---|---|
| A1 "Four eggs or five?" | 119850748 | 789 | 2,41% | 1 | $165 | $0,21 | 0,78% | 0 | geen; **T16 (gepland 22 okt) is nooit gestart** |
| A2 "Where 100,000+ customers started" | 119850750 | 727 | 1,10% | 1 | $128 | $0,18 | 0,70% | 0 | geen |
| **Flow totaal** | | **1.516** | **1,78%** | **2** | **$293** | **$0,19** | **0,74%** | **0** | |

Let op: Site stuurde 9 tot 15 okt 130 tot 410 mails per dag, sinds 16 okt 40 tot 80 (27 okt 184). Active on Site is niet gedaald (1.200 tot 2.000 profielen per dag). Waarschijnlijke reden: de vaste bezoekers zitten in "niet in deze flow in 14 dagen" en "geen order in 30 dagen", de eerste golf na livegang is op. Niet bewezen; zie 5.

### 2.4 Lopende test T05a op B1 (WdRz5k, A/B 119850693, 50/50, sinds 8 okt 22:43, winnaar handmatig)

| Variant | Onderwerp | 14 dagen: ontv. / klik / orders / omzet / per ontv. | Sinds start: ontv. / klik / orders / omzet / per ontv. |
|---|---|---|---|
| A (119850691) | "Get this pan with 10% off" | 1.102 / 3,4% / 3 / $404 / $0,37 | 1.496 / 3,2% / 3 / $404 / $0,27 |
| B (119850692) | "Why I started making this pan" | 1.162 / 2,8% / 5 / $383 / $0,33 | 1.563 / 2,9% / 6 / $982 / $0,63 |

(Unieke profielen uit metric-aggregates; wijkt een paar procent af van het flowrapport.) Geen verschil op klik (p ≈ 0,6) of orders. Volgens de regel blijft A. Advies: op **31 okt beëindigen met A**, niet op 5 nov wachten; het slot is nodig voor BR1 vóór de novembersale.

Andere lopende tests in deze drie flows: alleen T02 (code tegen geen code) op de B2-CLICKED-takken van WdRz5k en QNZyEb, met 3 tot 20 ontvangers per arm in 14 dagen. Geen test in Site.

---

## 3. Waarom browse daalde

### 3.1 De drie periodes naast elkaar

| | Oude flows Wj6x6V + TyEjuQ, 8 weken (13 aug tot 8 okt) | Oude flows, 24 sep tot 8 okt | v4 WdRz5k, 9 tot 19 okt | v4 WdRz5k + QNZyEb, 19 okt 19:00 tot 28 okt |
|---|---|---|---|---|
| Mails per dag | 902 | 1.021 | 380 | 490 |
| waarvan eerste mail (personen per dag) | 902 mails, ~520 tot 560 personen (75% van TyEjuQ ging ook naar Wj6x6V, audit 19 okt) | | 250 | 285 |
| Klik per mail | 2,9% | 2,5% | 2,8% | 2,2% |
| Klik eerste mail | 2,9% | 2,5% | 3,0% | 2,8% |
| Orders per 1.000 mails | 3,9 | 2,9 | 4,1 | 4,0 (zonder $0-orders 3,2) |
| Gemiddelde order | $237 | $302 | $175 | $150 |
| Omzet per mail | $0,91 | $0,89 | $0,73 | $0,60 |
| **Omzet per dag** | **$825** | **$907** | **$275** | **$293** |
| Orders per bereikte persoon | ~0,6% | | 0,63% | 0,68% |

De cijfers uit de opdracht ($1,01 naar $0,62, 4,6% naar 2,7%, 3,2 naar 4,1, 880 naar 480) kloppen voor de huidige periode. De "voorheen"-kant kan ik niet precies terugvinden: 880 per dag is het 8-weekse gemiddelde uit het go-live-draaiboek, maar omzet en klik in elk venster van de oude flows liggen op $0,89 tot $0,91 en 2,5 tot 2,9%. Het beeld is hetzelfde.

**Rekensom van het verlies ($825 naar $293 per dag):** bereikte personen ~540 naar ~285 (-47%), orders per persoon gelijk, gemiddelde order $237 naar $150 (-37%). 0,53 x 0,63 = 0,33; $825 x 0,33 ≈ $275. Dat verklaart het hele verschil.

### 3.2 Ordergrootte (grootste oorzaak van de lagere omzet per ontvanger)

Toegeschreven browse-orders gekoppeld aan de producten in de order (op uur en bedrag, 84 van 86 orders):

| Periode | Orders | Gem. order | Set of bundel | Losse pan | Accessoire | $0-orders |
|---|---|---|---|---|---|---|
| Oud, 24 sep tot 8 okt | 47 | $315 | 15 (gem. $560) | 26 (gem. $215) | 6 ($137) | 0 |
| v4, 9 tot 19 okt | 21 | $197 | 5 ($403) | 9 ($169) | 7 ($85) | 2 |
| v4 + TP, 19 tot 28 okt | 16 | $151 | 1 ($570) | 13 ($128) | 1 ($181) | 3 |

Winkelbreed (alle orders): gemiddelde betaalde order $227, $237 en $248; setorders 18%, 30% en 21%; $0-orders 2,0%, 3,4% en **10,4%** (vooral Pan Pro Standard, 186 stuks in 9 dagen). De winkel verkoopt dus niet kleiner. Browse wel.

- **Sale (prijs):** losse pannen kosten nu 40 tot 60% minder dan eind september (bekeken prijzen 1 tot 2 okt tegen 25 tot 26 okt: Deep Pan Pro $305 naar $119, Wok $194 naar $119, Large $209 naar $149, 6-delige set $579 naar $299, 12-delig $699 naar $649; Standard bleef $144). De losse-pan-order in browse ging van $215 naar $128.
- **Sets vallen weg uit browse (mix):** 20% van de bekeken producten is een set (zelfde aandeel in alle drie de periodes), maar sets zijn van 32% naar 6% van de browse-orders gegaan. B1 is gebouwd als "this pan + 10%": ook wie de set bekeek krijgt kop en onderwerp over "this pan", zonder setblok of rekensom. Daarnaast kopen nieuwe inschrijvers met HI10 vaker een set, en die vallen nu bewust onder welcome (filter 7 dagen).
- **$0-orders:** 3 van de 16 recente browse-orders zijn $0. Ze tellen als order maar niet als omzet. [VRAAG FLORIS: wat zijn de $0-orders van Pan Pro Standard sinds ~20 okt? Giveaway-winnaars, affiliate-pakketten of vervangingen?] Als het geen echte aankopen zijn, horen ze uit elke testmeting.

### 3.3 Verdeling tussen WdRz5k en QNZyEb, en de dedupe-filters

- QNZyEb neemt alleen mensen op die in de laatste dag **geen** Klaviyo Viewed Product hadden (de Triple Pixel-bekijkers die Klaviyo zelf niet herkent). WdRz5k slaat in B1, B1-ACC en B2-NOTCLICKED iedereen over die in 7 dagen een QNZyEb-mail kreeg. Beide flows sluiten cart, checkout en welcome in 7 dagen uit.
- Sinds 20 okt: WdRz5k bereikte 1.794 unieke profielen, QNZyEb 613. TP is dus ~25% van het browsebereik.
- WdRz5k eerste mails per dag: 250 (9 tot 19 okt, waarvan 63 in de oude controle-arm) naar 205. B1 zelf steeg van 154 naar 179 per dag omdat de controle-arm dicht is. Het verlies van ~45 eerste mails per dag is vooral die arm plus minder B1-ACC (33 naar 26), niet Triple Pixel. Een race (TP-event net vóór het Klaviyo-event) is mogelijk maar niet te meten zonder profielniveau; geen aanwijzing in de volumes.
- De oude TyEjuQ stuurde 450 tot 700 mails per dag, grotendeels aan mensen die ook de Klaviyo-browsemail kregen. QNZyEb stuurt 80 tot 190 per dag (eerste en tweede mail). Dat dubbele contact komt niet terug, en dat is goed: het leverde vooral uitschrijvingen (765 in 8 weken in de oude flows).
- Grootste snijder blijft "geen welcome-mail in 7 dagen" (30% van de bekijkers, audit 19 okt). Het voorstel uit die audit (7 naar 1 dag, +31 mails per dag) staat nog open.

### 3.4 Wachttijd voor de eerste mail

- Nu 1 uur in WdRz5k en QNZyEb, 2 uur in Site. De oude flows hadden een willekeurige 50/50-split van **10 tegen 30 minuten** (8 weken, ~25.000 per arm): 10 minuten $0,94 per ontvanger, 4,2 orders per 1.000, 3,0% klik; 30 minuten $0,89, 3,5 per 1.000, 2,7% klik. Korter was iets beter, niet significant (106 tegen 89 orders).
- Volgens de audit kocht 8% van de bekijkers binnen 1 uur en ging 15% binnen 1 uur naar cart of checkout. Hoe langer we wachten, hoe meer kopers en cart-mensen eruit vallen: minder mails, minder toegeschreven omzet, maar niet per se minder echte orders.
- Concurrenten: HexClad 0,7 tot 1,5 uur met het bekeken product, Our Place 4 uur zonder product.

### 3.5 Welke producten bekeken zijn

Steekproef Viewed Product (Klaviyo) op 1 tot 2 okt, 14 tot 15 okt en 25 tot 26 okt (4.472, 4.141 en 6.981 events): pannen 71 tot 76%, sets 16 tot 20%, accessoires 7 tot 8%. Pan Pro Standard is steeds ruim de helft van alle bekeken producten. Nieuw in de top in de laatste periode: Roasting Pan (US) en Pan Pro Mini. De mix verklaart de daling dus niet; wat wel veranderde is wat er gekocht wordt (3.2).

### 3.6 Effect van de sale op de mails

- B1 (beide flows) belooft in onderwerp, hero en aanbodbalk "10% off" met HI10, terwijl de site 50% korting geeft en vanaf Halloween 70%. De klik op de eerste mail bleef gelijk (2,8 tot 3,0%), dus de mail werkt nog, maar het aanbod in de mail is het kleinste getal dat de klant die dag ziet.
- Campagnedruk is niet gestegen: 1 tot 7 okt 100.000 tot 190.000 campagnemails per dag, 20 tot 27 okt 0 tot 83.000.
- De sale verlaagt de orderwaarde (3.2) en maakt de set relatief goedkoper ($299 voor 6 stuks tegen $119 tot $149 voor één losse pan). Dat is precies het moment om de set te tonen, en dat doet browse nu niet.

---

## 4. Tests, gesorteerd op verwachte extra omzet per week

Basis per week (14-daags gemiddelde): B1 pan-pad WdRz5k ~1.180 ontv. ($390), TP · B1 ~290 ($350), B2-NOTCLICKED WdRz5k ~1.070 ($750), TP · B2 ~200 ($72), B1-ACC ~260 ($245), A1 ~395 ($83). Browse en site samen ~$2.400 per week. Novembervolume voorzichtig 2x.

**Power, eerlijk:** omzet per ontvanger in browse heeft een variatiecoëfficiënt van ~19 (0,45% koopt, orders van $0 tot $600). Een verschil van 30% in omzet per ontvanger zien vraagt ~64.000 ontvangers per arm: 1,5 tot 7 jaar. Daarom voor elke test: **beslissen op unieke klik** (dat is wel meetbaar), **omzet per ontvanger als richting** (Bayesiaans, B alleen uitrollen als P(B ≥ A) op omzet minstens 80% is) en **bewakers**: uitschrijving niet meer dan 20% relatief hoger, spam niet boven 0,1% per mail (Gmail-grens 0,3%). Alle tests: drie periodes apart (tot 31 okt, sale 1 nov tot 6 dec, daarna), $0-orders niet meetellen, BFCM-dagen apart.

Slots: WdRz5k heeft nu T02 + T05a. Als T05a op 31 okt dicht gaat en T02 vanaf 1 nov op 0% staat (advies plan 19 okt, besluit Floris), zijn er in november twee slots vrij in WdRz5k. QNZyEb en Site hebben elk twee vrije slots.

### BR1 · Eerste mail: de sale in plaats van alleen 10% (WdRz5k B1 + QNZyEb TP · B1, gepoold)

| | |
|---|---|
| Hypothese | Wie een pan bekeek tijdens een sale van 50 tot 70% en een mail krijgt met "10% off", ziet het kleinste aanbod van de dag. Een eerste mail met de echte saleprijs van het bekeken product, plus HI10 er bovenop, trekt meer kliks en meer orders |
| Variabele | Aanbod-framing van de eerste mail als één pakket: onderwerp, aanbodbalk in de hero en de prijsregel op de productkaart (die drie horen samen, anders belooft het onderwerp iets wat de mail niet zegt). Template-opbouw, beelden, reviews en wachttijd gelijk |
| A | Huidige B1: "Get this pan with 10% off", aanbodbalk "EXTRA 10% OFF WITH HI10 · 4 FREE GIFTS" |
| B | Onderwerp **"Your pan, at the sale price"**, preview "The sale price, plus an extra 10% with HI10. The lab report is inside." Aanbodbalk "SALE PRICE + EXTRA 10% WITH HI10 · 4 FREE GIFTS". Productkaart: prijs uit `{{PRICE:...}}` en alleen voor Pan Pro Standard de bevestigde streepprijs ($439, $144, met HI10 $129.60); andere maten zonder streep. Geen percentage in het onderwerp, zodat B geldig blijft bij 50, 70 en BFCM zonder de test te wijzigen |
| Vijf onderwerpen (skill 5) | C+B "The pan you viewed, at its sale price" · SPEC "Report no. 25895, now at the sale price" · Q "Did you catch the sale price?" · STORY "\"I ordered one pan to try it out\"" (staat al als B2-onderwerp; letterlijk uit een review) · OFFER "Your pan, at the sale price" (gekozen) |
| Metric | Unieke klik (beslissend), omzet per ontvanger zonder $0-orders (richting), uitschrijving en spam als bewaker |
| Looptijd en power | ~238 per dag samen (119 per arm). Klik +50% (2,8% naar 4,2%): 23 dagen, met novembervolume 11. Klik +30%: 58 dagen, met novembervolume ~29. Omzet +30%: niet haalbaar (~540 dagen). Start 1 nov, eerste lezing 20 nov, besluit 7 dec op de dagen buiten BFCM |
| Verwachte extra omzet | Eerste mail pan-pad ~$740 per week. +15 tot 35% = **$110 tot $260 per week**, in november **$220 tot $520** |
| Risico | Middel. Prijs per markt moet kloppen (macro's, browse-helper; AUD/CAD/SGD tonen "$" in event.Price en krijgen geen bedrag). Gifts in november moeten blijven (DECISIONS 19 okt: ja). Twee templates (WdRz5k en TP) met dezelfde B-wijziging. HI10 stapelt op de sale (DECISIONS 19 okt) |
| API of UI | Template B via `build_template.py` + `export_klaviyo.py` (API). A/B-actie op 119850693 kan via de API klaargezet worden zodra T05a in de UI is beëindigd; **starten is één klik in de UI**. Voor QNZyEb 121177227 hetzelfde (nieuwe A/B) |
| Klaar vóór BFCM | **Ja**: bouwen 29 tot 30 okt, QA, T05a dicht op 31 okt, start 1 nov |

### BR2 · Opbouw van B1: product groot eerst (WdRz5k B1)

| | |
|---|---|
| Hypothese | TP · B1 (product groot bovenaan, daarna de drie vragen en rapport 25895) haalt $1,20 per ontvanger en 3,75% klik, WdRz5k B1 (hero met kop, dan productkaart) $0,33 en 2,46%. Andere doelgroep, dus niet vergelijkbaar, maar groot genoeg om te toetsen. HexClad doet hetzelfde: het bekeken product is de mail |
| Variabele | Template-opbouw. Onderwerp, preview, aanbod en wachttijd gelijk |
| A | Huidige B1 (template R6E5Zv / bron `v3/browse/b1.html`) |
| B | Kopie van TP · B1 (`v3/browse-tp/tp-b1.html`, template TY9hCH) met utm `v4-browse` in plaats van `v4-browse-tp`, verder byte-gelijk |
| Metric | Unieke klik, omzet per ontvanger als richting, uitschrijving en spam |
| Looptijd en power | ~168 per dag (84 per arm). Klik +50%: 36 dagen (november 18). Klik +30%: 93 dagen. Start pas na BR1 of tegelijk in een tweede slot alleen als BR1 een andere mail raakt (zie kalender): advies **na BR1, vanaf 7 dec**, of vóór BR1 als Floris liever eerst de opbouw test |
| Verwachte extra omzet | B1 WdRz5k ~$390 per week. +20 tot 50% = **$80 tot $195 per week** |
| Risico | Laag. Template bestaat en is live in QNZyEb; QA al gedaan op 19 okt |
| API of UI | Template via API (export), A/B starten in de UI |
| Klaar vóór BFCM | Bouwen ja (1 dag), starten na BR1. Niet allebei tegelijk op B1: dat zijn twee variabelen op dezelfde mail |

### BR3 · B2-NOTCLICKED: setaanbeveling op basis van het bekeken product (WdRz5k 119850700 + QNZyEb 121177242, gepoold)

| | |
|---|---|
| Hypothese | Sets zijn 20% van de bekeken producten maar nog maar 6% van de browse-orders. In de sale is de 6-delige set ($299) maar twee keer een losse pan. Een blok "dit hoort erbij" gekozen op het bekeken product (losse pan: de 6-delige set; set: wat er in de doos zit; accessoire: de pan) trekt de gemiddelde order omhoog bij gelijke klik |
| Variabele | Eén blok onder de productkaart in B2-NOTCLICKED. Onderwerp, invalshoek en de rest gelijk |
| A | Huidige B2-NOTCLICKED (WdRz5k "Skeptical? So were they.", TP "Why we can cover this pan for 75 years"; elke flow houdt zijn eigen A) |
| B | A plus `{{BLOCK:bundle}}` (set bekeken) of `{{BLOCK:xsell fall="1"}}` (losse pan bekeken). Eyebrow "MADE TO GO WITH IT", kop "Not just one pan?", regel "Buy 2, get 4 free. Six pieces for {{PRICE:set6}}." Knop "Upgrade to the 6-piece set", eronder `{{FRICTION}}`. Buiten de prijslijstmarkten zonder bedrag |
| Metric | Omzet per ontvanger en gemiddelde order zonder $0-orders (richting), klik op het setblok (utm_content `b2-set`), uitschrijving en spam |
| Looptijd en power | ~195 per dag (98 per arm). Klik +50%: 66 dagen (november 33). Dit is een AOV-test, dus eigenlijk niet te bewijzen op ons volume; beslissen op klik op het blok plus setaandeel in de orders. Minimaal tot half januari |
| Verwachte extra omzet | B2 samen ~$820 per week. +10 tot 25% = **$80 tot $205 per week** |
| Risico | Middel. Mail wordt langer (max ~3.600 px, PLAYBOOK 12): iets anders eruit. [VRAAG FLORIS: blijft de 6-delige set $299 en "Buy 2, get 4 free" in november? DECISIONS 8 okt koppelt die aan de fall sale.] Botst met T19 op dezelfde mail in WdRz5k: één van de twee |
| API of UI | Template via API, A/B starten in de UI (twee flows, twee klikken) |
| Klaar vóór BFCM | Ja, als Floris de setprijs voor november bevestigt. Start 5 nov in plaats van T19 (zie kalender) |

### T19 · B2-NOTCLICKED: social proof tegen garantie (WdRz5k 119850700, uit het plan van 19 okt)

| | |
|---|---|
| Hypothese | Wie B1 niet aanklikte twijfelt of de pan het houdt. De garantie (75 jaar) beantwoordt dat directer dan reviews |
| Variabele | Invalshoek van de hele mail (onderwerp en inhoud horen samen) |
| A | "Skeptical? So were they." (social proof, template VyZUHC) |
| B | "Why we can cover this pan for 75 years", preview "Nothing on it to wear off. That's why the warranty is this long." (template XmHxNn uit QNZyEb, kopie in de bibliotheek) |
| Metric | Unieke klik, omzet per ontvanger als richting, uitschrijving en spam |
| Looptijd en power | ~153 per dag (77 per arm). Klik +50%: 75 dagen (november 37). Besluit januari |
| Verwachte extra omzet | **$40 tot $150 per week.** Lager dan in het oude plan: de garantieversie loopt in QNZyEb slechter ($0,36, 0,75% klik, 2 spam) dan de social-proofversie in WdRz5k ($0,70, 1,35%). Andere doelgroep, maar het wijst eerder naar A |
| Risico | Laag. Template bestaat. Let op de spam op de garantieversie in TP |
| API of UI | A/B klaarzetten via API mogelijk, starten in de UI |
| Klaar vóór BFCM | Ja. **Advies: BR3 eerst**, T19 pas in januari |

### T16 · A1-onderwerp (Site VLGhbR 119850748, uit het plan van 19 okt, nooit gestart)

| | |
|---|---|
| Hypothese | "Four eggs or five?" is een raadsel voor iemand die geen product bekeek. Een onderwerp dat de keuze belooft klikt beter |
| Variabele | Onderwerp |
| A | "Four eggs or five?" |
| B | "Not sure which pan? Start here." (SUBJECT_B uit de bron `v3/site/a1.html`) |
| Metric | Unieke klik, omzet per ontvanger als richting, uitschrijving (nu 0,78%, boven het signaal van 0,5%) |
| Looptijd en power | Nu ~55 per dag (28 per arm). Klik +50%: 115 dagen, november 58. Alleen zinvol als het bereik terugkomt (5) |
| Verwachte extra omzet | A1 ~$83 per week. +10 tot 30% = **$8 tot $25 per week** |
| Risico | Laag |
| API of UI | Onderwerp-A/B klaarzetten via API, starten in de UI |
| Klaar vóór BFCM | Ja, maar lage prioriteit |

### BR4 · Wachttijd eerste mail: 1 uur tegen 4 uur (WdRz5k, random split na de trigger)

| | |
|---|---|
| Hypothese | Een later moment (4 uur) haalt de mensen eruit die toch al kochten of in cart belandden, en vangt wie 's avonds terugkomt. Netto meer orders per instromer of hetzelfde met minder mails |
| Variabele | Wachttijd vóór B1 en B1-ACC (1 uur tegen 4 uur). Alles daarna gelijk |
| A | 1 uur (nu) |
| B | 4 uur |
| Verwachting | Eerder A. De oude flows lieten 10 minuten iets beter scoren dan 30 (4,2 tegen 3,5 orders per 1.000), HexClad zit op 0,7 tot 1,5 uur. Met 4 uur valt de toegeschreven omzet zeker (minder mails), dus **meten op alle orders per instromer binnen 7 dagen (cohort)**, niet op toegeschreven omzet. Overweeg in plaats daarvan 20 minuten tegen 1 uur: meer kans op winst |
| Metric | Alle betaalde orders en omzet per instromer in 7 dagen (cohort via events, Claude telt), plus uitschrijving en spam per mail |
| Looptijd en power | ~205 instromers per dag (103 per arm). Bij ~3% kopers per instromer vraagt +20% ~14.000 per arm: 135 dagen; +40% ~4.000: 40 dagen. Alleen grote verschillen zichtbaar |
| Verwachte extra omzet | **-$40 tot +$40 per week**. Waarde zit in het leren, niet in de omzet |
| Risico | Middel. Nieuwe split boven B1 met dubbele paden (B1-pad en ACC-pad per arm), meer onderhoud. Gaat in tegen T05a/BR1 als die op dezelfde mail lopen: wachttijd is een andere variabele op hetzelfde moment, dus niet tegelijk met BR1 |
| API of UI | **Alleen UI**: een split en extra wachttijden toevoegen kan niet via de API (geen `definition` in PATCH flows) |
| Klaar vóór BFCM | Nee. Na BFCM (januari), nadat BR1 beslist is |

### BR5 · Triple Pixel: minder mails (QNZyEb, holdout op TP · B2-NOTCLICKED)

| | |
|---|---|
| Hypothese | TP-bekijkers zijn niet door Klaviyo herkend (ander apparaat, advertentieverkeer) en herkennen een tweede mail minder als iets waar ze om vroegen. TP · B2-NOTCLICKED kost meer dan het oplevert: 0,75% klik, $0,36 per ontvanger, 0,76% uitschrijving, 2 spamklachten op 397 (0,50%) |
| Variabele | Wel of geen tweede mail voor niet-klikkers (50% holdout) |
| A | Huidige flow: B1, na 2 dagen B2-NOTCLICKED |
| B | Alleen B1 (niet-klikkers krijgen niets meer) |
| Metric | Alle betaalde orders per TP-instromer in 7 dagen (cohort), spam en uitschrijving per instromer |
| Looptijd en power | ~48 per dag in de niet-klik-tak. Omzetverschil is niet meetbaar (B2 levert ~$72 per week). Spam is wel duidelijk: bij 0,5% tegen 0% zie je het binnen 3 tot 4 weken |
| Verwachte extra omzet | **-$70 tot $0 per week** aan omzet, maar het beschermt de afzenderreputatie van alle mails. Eén spamgolf in november kost meer dan een jaar TP · B2 |
| Risico | Laag aan de omzetkant. Advies: **niet als test maar direct** TP · B2-NOTCLICKED op Manual zetten tot na BFCM als Floris geen holdout wil; de holdout is alleen nodig als we willen weten of B2 ook incrementeel iets doet |
| API of UI | Holdout-split: alleen UI. Mail op Manual/Draft zetten: via de API (status van de flow-actie), na akkoord Floris |
| Klaar vóór BFCM | Ja (de directe variant vandaag, de holdout vóór 5 nov) |

### Samen

| # | Test | Mail | Extra per week (nu) | November | Start | API/UI | Vóór BFCM |
|---|---|---|---|---|---|---|---|
| 1 | BR1 sale-framing | B1 + TP · B1 | $110 tot $260 | $220 tot $520 | 1 nov | template API, start UI | ja |
| 2 | BR2 product eerst | B1 WdRz5k | $80 tot $195 | $160 tot $390 | 7 dec (na BR1) | template API, start UI | gebouwd ja, live na BFCM |
| 3 | BR3 setaanbeveling | B2-NOTCLICKED beide | $80 tot $205 | $160 tot $410 | 5 nov | template API, start UI | ja, na setprijs-akkoord |
| 4 | T19 garantie tegen social proof | B2-NOTCLICKED WdRz5k | $40 tot $150 | | januari | API klaarzetten, start UI | ja, maar na BR3 |
| 5 | T16 A1-onderwerp | A1 Site | $8 tot $25 | | na bereikcheck | API klaarzetten, start UI | ja |
| 6 | BR4 wachttijd 1 u tegen 4 u | B1-moment WdRz5k | -$40 tot +$40 | | januari | alleen UI | nee |
| 7 | BR5 TP minder mails | TP · B2-NOTCLICKED | -$70 tot $0 (beschermt reputatie) | | direct | UI (holdout) of API (mail uit) | ja |

Samen, zonder overlap: **ongeveer $300 tot $800 per week nu, $600 tot $1.500 per week in november** bij winnende varianten. Lage zekerheid: geen van deze tests kan omzet per ontvanger hard bewijzen.

---

## 5. Niet testen, wel doen of uitzoeken

| Wat | Waarom | Voorstel |
|---|---|---|
| $0-orders uit alle metingen | 10% van alle orders sinds 19 okt, 3 van 16 browse-orders. Ze blazen "orders per 1.000" op | Floris: wat zijn ze? Claude: in test_report.py orders met waarde 0 apart tellen |
| Site-bereik ~250 naar ~55 per dag | Active on Site is gelijk gebleven | Claude telt read-only per filter van VLGhbR hoeveel bezoekers van één dag eruit vallen (zoals de browse-audit), vóór T16 start |
| Welcome-filter browse 7 naar 1 dag | Audit 19 okt: +31 eerste mails per dag, ~$600 per maand | Besluit Floris; in BFCM eventueel 3 dagen |
| Herinstap browse 7 naar 4 dagen | Audit 19 okt: +54 per dag, ~$1.000 per maand | Besluit Floris |
| B1-ACC-niet-klikkers krijgen niets | B1-ACC haalt $0,96 per ontvanger, maar uitschrijving 1,18% | Eerst de uitschrijving begrijpen, dan pas een tweede mail |
| T05a beëindigen | Geen verschil na 3 weken, A blijft volgens de regel | 31 okt in de UI: End test, A als winnaar |

---

## 6. Kalender browse en site

| Wanneer | Actie | Wie |
|---|---|---|
| **29 okt** | Akkoord Floris op BR5 (TP · B2-NOTCLICKED op Manual of holdout) en op de setprijs in november (BR3). Antwoord over de $0-orders | Floris |
| **29 tot 30 okt** | Claude bouwt B-templates BR1 (WdRz5k en TP), BR3 (twee flows) en BR2 (alleen klaarzetten), QA-poort groen, alles Draft | Claude |
| **31 okt** | T05a beëindigen met A. T02-besluit voor de sale (deel 2) | Floris in UI |
| **1 nov** | Start **BR1** op 119850693 en 121177227 | Floris in UI, Claude controleert via API |
| **5 nov** | Start **BR3** op 119850700 en 121177242 (in plaats van T19). Holdout BR5 als gekozen | Floris in UI |
| **20 nov t/m 6 dec** | Bevriezing: niets nieuws, lopende tests door, BFCM-dagen apart | |
| **7 dec** | BR1 beslissen (klik, omzet als richting, buiten BFCM). Start **BR2** | Claude rapport, Floris |
| **januari** | BR3 beslissen. Start T19 of BR4. T16 als het Site-bereik terug is | |

---

## 7. Open punten voor Floris

1. Wat zijn de $0-orders (vooral Pan Pro Standard, 186 in 9 dagen)?
2. Blijven de 6-delige set voor $299 en "Buy 2, get 4 free" in de novembersale (BR3)?
3. TP · B2-NOTCLICKED: direct op Manual tot na BFCM, of eerst een holdout (BR5)?
4. Akkoord om T05a op 31 okt te sluiten met A, zodat BR1 op 1 nov kan starten.
5. Welcome-filter (7 naar 1 dag) en herinstap (7 naar 4 dagen) uit de audit van 19 okt: nog steeds open.
