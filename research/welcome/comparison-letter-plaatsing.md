# Plaatsing van de vergelijkingsbrief "Before you start comparing"

Datum: 18 nov 2026. Vraag Floris: waar in de klantreis heeft de lange founder letter (HTML `klaviyo/templates/v3/welcome/w2-before-you-compare/w2-before-you-compare.html`, template Yt8e54, niet live) het meeste effect, voor welk segment, en wat moet er per plaatsing aan de tekst veranderen?

Alleen gelezen: Klaviyo (flowdefinities, flow-values-report 30 dagen, events), Gorgias (tickets 180 dagen), de repo en het web. Niets gewijzigd in Klaviyo, Shopify of Gorgias, geen mails verstuurd. Analysescript: `research/welcome/scripts/cohort.py` (ruwe events staan niet in de repo).

## Kort antwoord

**Aanbeveling 1: Browse abandonment (WdRz5k), in plaats van B2-NOTCLICKED op dag 2 om 09:00, als 50/50-test vanaf 2 december.** Segment: mensen die een product bekeken, niet kochten en B1 niet aanklikten. Dit is het moment waarop iemand aan het vergelijken is. 81% van de late kopers (na het eerste uur) kwam eerst terug om een product te bekijken. Hun eerste terugkeer valt mediaan 23 uur na aanmelding. B2-NOTCLICKED is nu de zwakste stap met volume ($0,41 per ontvanger), dus een test kost weinig.

**Alternatief 2: Welcome (T4a5Mk), alleen voor "considerers" op dag 2 tot 3**, met een conditional split op Viewed Product sinds de start van de flow, na BFCM. Het heeft hetzelfde doel als aanbeveling 1, maar zo gaat de brief niet naar de 72% die niet terugkomt. Die groep koopt bijna niet (0,7%) en schrijft zich in de welcome het snelst uit. Nadelen: het volume is klein (ongeveer 1.100 per week), en tot half december worden de welcome-stappen overgeslagen voor iedereen die een BFCM-mail kreeg.

**Alternatief 3: Cart abandonment K2-NEW (TZG9Mx, dag 2) als kleine variant van 20%.** Hier zitten de mensen die tussen Siraat en een titanium-kopie kiezen op prijs ("it's between you and Okura", "we received a better deal from Plateful"). K2-NEW verdient al $1,50 per ontvanger, dus het risico is groter. Daarom alleen als kleine variant, met de rekensom erin.

**Niet doen:** de brief zoals hij nu is ergens live zetten. Wie vergelijkt, vergelijkt in de eerste plaats met andere titanium-pannen (Okura, Plateful, Taima, Kaizen). Daarbij stelt hij precies de vraag waar de brief tegen Siraat zelf werkt: "solid titanium of een laag?" Klanten schrijven al dat Siraat "only a surface layer" is en Okura "fully titanium". Een brief die anderen ervan beschuldigt geen echt titanium te leveren, valt dan op ons terug. Zie sectie 4.

## 1. De cijfers

### 1a. Tijd tot eerste order na aanmelding (lijst Uw8eZG)

Cohort: eerste aanmelding 20 okt t/m 9 nov 2026, opvolging tot 18 nov. 28.529 aanmelders, waarvan 28.425 zonder eerdere order (sinds 1 sep). Bron: Klaviyo events Subscribed to List (SCvkku), Placed Order (RSNxYV), Viewed Product (XNtYMB); script `research/welcome/scripts/cohort.py`.

| Binnen | % eerste order (cumulatief) |
| --- | --- |
| 2 min | 9,0% |
| 10 min | 13,9% |
| 1 uur | 16,0% |
| 24 uur | 17,0% |
| 3 dagen | 17,7% |
| 7 dagen | 18,2% |

- 87,5% van de kopers binnen 7 dagen koopt in het eerste uur. Een brief in de welcome bereikt die mensen dus niet: ze hebben dan al gekocht. Over 12 maanden geldt hetzelfde: 20,3% koopt binnen 10 minuten na aanmelding, de kans per dag halveert elke 4 tot 5 dagen (bron: `research/timing/01-data.md` §6, n = 226.357).
- Van wie na 1 uur niet kocht (n = 23.888), koopt 2,72% nog binnen 7 dagen: 1,25% op dag 0, 0,40% op dag 1, 0,36% op dag 2, daarna 0,15 tot 0,21% per dag.
- **27,7% van de niet-kopers komt binnen 7 dagen terug om een product te bekijken.** Hun conversie binnen 7 dagen is 7,97% (527 kopers). Bij niet-terugkomers is dat 0,71% (123). Van de 650 late kopers had 527 (81%) eerst opnieuw een product bekeken.
- Eerste terugkeer na aanmelding: p25 5,8 uur, mediaan 23,2 uur, p75 66,9 uur. Het vergelijkmoment valt dus op dag 1 tot 3.

### 1b. Productkijkers (browse), zelfde periode

Eerste Viewed Product 20 okt t/m 8 nov, geen eerdere order. Bron: dezelfde events.

| Groep | n | Order daarna |
| --- | --- | --- |
| Geen order in het eerste uur na de view | 25.321 | 4,97% in uur 1 tot dag 7 |
| Geen order in de eerste 48 uur (moment B2) | 24.555 | 2,50% op dag 2 tot 9 |

De 2,50% is de basislijn voor de testopzet (sectie 2). Over 12 maanden: Viewed Product, nog geen order na 15 min, 6,3% binnen 7 dagen (`research/timing/01-data.md` §1b).

### 1c. Flowmails nu, laatste 30 dagen (19 okt t/m 18 nov)

Bron: Klaviyo flow-values-report, conversion_metric_id RSNxYV (Klaviyo-toeschrijving, 5 dagen klik). Een selectie; de volledige tabel staat in de scratchpad (`cmp/fr30.json`).

| Flow · mail | Ontv. | Open | Klik | Orders | Omzet/ontv. | Uitschr. |
| --- | --- | --- | --- | --- | --- | --- |
| Browse · B1 (A/B, UXPtQ6) | 23.002 | 42,6% | 3,49% | 98 | $1,03 | 0,95% |
| **Browse · B2-NOTCLICKED "Skeptical? So were they." (Yu3YvE)** | **19.045** | 37,8% | 1,28% | 37 | **$0,41** | 0,72% |
| Cart · K1 (Vb6YFp) | 9.304 | 47,3% | 6,17% | 183 | $5,99 | 1,03% |
| Cart · K2-NEW "15 coated pans, or one." (Ti3QPw) | 7.609 | 40,2% | 2,04% | 34 | $1,50 | 0,94% |
| Checkout · C1 (WhTznn) | 4.186 | 46,1% | 7,78% | 149 | $12,87 | 1,27% |
| Checkout · C2 (RZpvpp) | 2.696 | 39,6% | 2,87% | 27 | $2,87 | 1,27% |
| Welcome · W1 (RN7Yy6) | 19.633 | 45,7% | 3,85% | 188 | $2,91 | 1,67% |
| Welcome · W2 Benjamin "The pan nobody else was making" (RHuJcG) | 14.448 | 42,0% | 2,34% | 20 | $0,38 | 1,41% |
| Welcome · W3 "Has your cookware been tested?" (SSTz6y) | 14.578 | 38,9% | 1,31% | 19 | $0,44 | 1,03% |
| Welcome · Old W6 "The ultimate showdown" (X298nK, vergelijkingsmail) | 826 | 79,3% | 0,97% | 1 | $0,90 | 0,97% |
| BF follow-up · bfw2 US (VZiGeB) | 5.246 | 38,7% | 2,26% | 19 | $0,97 | 1,25% |
| BFCM Welcome · BF-W1 (oud TauWAG) | 33.407 | 44,0% | 4,60% | 426 | $3,86 | 1,79% |

Lezing: na mail 1 verdienen founder- en bewijsmails in de welcome $0,38 tot $0,44 per ontvanger, met 1,0 tot 1,4% uitschrijvingen. Dat ligt niet aan de tekst. Ze gaan naar iedereen, ook naar de 72% die nooit terugkomt. In browse en cart zit de brief bij mensen die nog actief kijken.

### 1d. Wat pre-sale vragen zeggen over "vergelijken" (Gorgias, 180 dagen)

Bron: Gorgias analytics, 26.442 tickets (zonder spam), waarvan 1.340 pre-sale. Trefwoordtelling in onderwerp en klantberichten.

| Thema | Alle tickets | Pre-sale |
| --- | --- | --- |
| "solid/pure/real titanium", "coated", "fake", "knockoff", "same pan" | 321 | **67** |
| PFAS, PTFE, Teflon, toxic | 421 | 48 |
| "compare", "difference between", "vs", "better than" | 309 | 39 (vooral eigen producten: Pro tegen set, Deep tegen Standard) |
| Titanium-kopieen (Okura, Plateful, Taima, Kaizen) | 50 | 9 |
| Grote merken (Caraway, Our Place, Made In, GreenPan, All-Clad, Le Creuset) | 62 | 7 |
| HexClad | 44 | 3 |

Letterlijke voorbeelden (pre-sale, met ticket-ID):
- 80557606 (19 aug, antwoord op de mail "Why no cookware brand sells these"): "is siraatskitchen the same quality than okura? ... in other words the siraats kichen is only a surface layer, where as okura is fully titanium."
- 79593090 (16 aug, antwoord op browse "we saw you looking"): "trying to decide between you pans and taima pans. taima says they are pure titanium without multilayer construction."
- 103003755 (15 nov): "why do your adds discredit other pans that are layered when description of your pan says the cooking surface is .5mm pure titanium, 1mm aluminu..."
- 101571024 (9 nov): "i haven't ordered anything yet. i've been looking for quite a while. it's between you and okura."
- 101061102 (6 nov): "i have had so many 'pure titanium' companies pop up ... what makes your pans better than the others."
- 99684765 (2 nov, antwoord op W2 "The pan nobody else was making"): "because the fb was flooded with ads regarding them, i was sceptical of the correct materials used and which one would be fake. you sound like a company i could trust".
- 102733717 (13 nov, antwoord op W2): "december 20, 2024 what about okura? who is the first?"
- 102022611 (11 nov): bestelling geannuleerd omdat "we received a better deal from plateful".

Lezing:
1. Wie Siraat vergelijkt, doet dat vooral met andere titanium-pannen en vraagt dan: "is het massief titanium of een laag?" HexClad, Made In en Caraway komen pre-sale bijna niet voor (10 van de 1.340). Dat past bij de VoC: 41,0% vergeleek met rvs, 13,2% met hybride, 12,2% twijfelde door andere merken (Canada 19,4%) (`research/voc/2026-11-synthese.md` §8, S01); het hele "hammered titanium"-segment wordt op Reddit als één scamcategorie gezien (`research/voc/2026-11-reddit.md` punt 2).
2. De vragen komen binnen als antwoord op browse- en welcome-mails en via het contactformulier, vóór de aankoop. Met een sale hebben ze niets te maken; het gaat om echtheid en bouw.

### 1e. Concurrenten: waar staat hun vergelijkings- of founder-mail?

Bron: `research/concurrenten/tijdlijn.csv` (dag 37).
- Caraway: welkom 3 na 36 uur "Are You Cooking Clean?" (vergelijking met PFAS-nonstick), welkom 5 na 132 uur "The Problem: Traditional Cookware Is Toxic".
- HexClad: browse 2 na 25,6 uur "The last cookware you'll ever need"; welkom 6 na 240 uur "A letter from HexClad's founder" (de brief staat in een afbeelding).
- Made In: brieven van de co-founders als campagne (Chip na 651 uur, Jake na 723 uur), met een aanbod.
- Our Place: uitleg van de eigen titaniumlijn als campagne ("The Beauty of Titanium", "Meet Our Titanium Always Pan Pro").
- Okura (titanium-kopie) adverteert met precies het argument van de brief: "Other titanium pans claim 100%, most are only 94%" (14 ads, `research/voc/2026-11-synthese.md` §5, S09).

Grote merken zetten de vergelijking op dag 1,5 tot 5 van de welcome en de founder-brief later. Niemand valt een andere titanium-pan aan in een flow, behalve Okura in ads. Wie de brief stuurt zoals hij nu is, klinkt dus als de kopie.

### 1f. Best practice (web)

- Een vaste "dag voor de vergelijkingsmail" bestaat niet in openbare bronnen. Gangbaar: merkverhaal 1 tot 2 dagen na mail 1, daarna 2 tot 3 dagen tussen mails, en meer ruimte als er niet gekocht wordt ([1800DTC](https://1800dtc.com/resources/build-high-performance-e-commerce-email-welcome-series), [Foundr](https://foundr.com/articles/building-a-business/how-to-create-the-perfect-welcome-series), [Attn Agency](https://www.attnagency.com/blog/email-welcome-series-optimization)).
- "Us vs them" werkt omdat het de vraag beantwoordt die de koper al stelt. Het hoort daarom bij retargeting en flows na een eerste bezoek, niet bij een koud publiek ([Zipify](https://zipify.com/blog-ocu-us-vs-them-ad/), [Confect](https://confect.io/blog/Us-Vs.-Them-Ad-Examples)).
- Browse abandonment converteert volgens Klaviyo zelf 0,96% per mail. Dat is een cijfer van de leverancier ([Klaviyo](https://www.klaviyo.com/blog/browse-abandonment-email)).
- Juridisch: de FTC beoordeelt vergelijkende claims net als andere claims. Elke objectief toetsbare claim over een ander product ("they're not delivering real titanium", "fake reviews") moet je kunnen onderbouwen ([FTC Statement of Policy Regarding Comparative Advertising](https://www.ftc.gov/node/52436), [Kelley Drye](https://s3.amazonaws.com/cdn.kelleydrye.com/content/uploads/attachments/The-Law-of-Comparative-Advertising-in-the-United-States.pdf)).

Onze eigen data wegen zwaarder dan deze bronnen. De bronnen spreken de keuze in elk geval niet tegen: de brief hoort na het eerste bezoek, bij iemand die terugkomt.

## 2. Testopzet

### Aanbeveling 1: Browse B2-NOTCLICKED

| Onderdeel | Voorstel |
| --- | --- |
| Flow | WdRz5k "v4 · Browse abandonment" |
| Positie | Tak "B1 niet geklikt" (nu Yu3YvE, B2-NOTCLICKED "Skeptical? So were they."), zelfde vertraging: dag 2, 09:00 profieltijd |
| Split | Random split 50/50 vóór de mail (profile-sample 50). A = huidige B2, B = de herschreven brief. Geen Klaviyo-A/B-actie met automatische winnaar: die rekent op klik en toegeschreven omzet |
| Start | 2 december 2026, na de BF-sale en Cyber Monday (sale tot 30 nov, DECISIONS 31 okt en 1 nov). Tijdens BFCM verkopen de browse-mails de 70% en de BF-code; een brief zonder aanbod is dan geen eerlijke vergelijking. De VoC-synthese zegt ook: geen nieuwe flows tijdens BFCM |
| Succesmaat | Eerste Placed Order binnen 7 dagen na de split, alle orders, niet alleen toegeschreven (methode zoals `research/v6-golive/20-welcome-analyse.md`). Tweede maat: omzet per ontvanger op dezelfde basis |
| Bewaking | Uitschrijving per mail (nu 0,72%), spam (nu < 0,1%), aantal pre-sale tickets over "solid/coated/fake" van ontvangers |
| Minimum | Basislijn ongeveer 2,5% (1b). Om +25% relatief (2,5% naar 3,1%) te zien met 80% power en alpha 0,05: ongeveer 11.000 ontvangers per arm. Bij ongeveer 19.000 per 30 dagen (1c, BFCM-verkeer, in december vermoedelijk lager) duurt dat 5 tot 6 weken. Minstens 2 volle weken, ook als het eerder "duidelijk" lijkt |
| Stopregels | Direct stoppen (B uit) als na 2.000 ontvangers in B de uitschrijving boven 1,5% ligt of spam boven 0,15%. Ook stoppen als er een klacht of ticket komt dat de brief een concurrent beschuldigt. Winnaar pas kiezen op het minimum. Ligt B na het minimum niet boven A (p > 0,10), dan blijft A |
| Smart sending | Laten zoals nu (uit in browse). De flowfilters (geen cart, checkout of order sinds start, geen cartmail in 7 dagen) voorkomen al de dubbele druk |

### Alternatief 2: Welcome, tak "considerers" (na BFCM)

- Flow T4a5Mk. Na W1 een conditional split: Viewed Product (XNtYMB) > 0 sinds de start van de flow én geen order. Alleen de ja-tak krijgt de brief op dag 2, 09:00, in de plaats van W2 (RHuJcG) en niet ernaast: W2 vertelt al het kopieenverhaal en de datum 20 dec 2024. De nee-tak houdt W2.
- Split binnen de ja-tak 50/50 (brief tegen W2). Succes: eerste order binnen 7 dagen na de split.
- Volume: ongeveer 9.500 aanmelders per week (BFCM-cohort), daarvan ongeveer 8.000 niet-kopers na 1 uur. Ongeveer de helft van de 27,7% terugkomers is er vóór dag 2, dus ongeveer 1.100 per week in de tak. Met basislijn 8% in deze groep: om +20% relatief te zien zijn ongeveer 4.500 per arm nodig, dus ongeveer 8 weken. Niet vóór half december: wie in november BF-W1 kreeg, slaat E1 tot E5 twee weken over (filter "geen mail uit SdaYcV in 2 weken").

### Alternatief 3: Cart K2-NEW (20% variant)

- Flow TZG9Mx, stap K2-NEW (Ti3QPw, dag 2, 08:00), alleen nieuwe klanten. Split 80/20: 80% huidige K2-NEW, 20% de brief met het cartproduct en de rekensom.
- Succes: eerste order binnen 7 dagen. Stoppen als B na 1.000 ontvangers onder de helft van A zit op omzet per ontvanger ($1,50).
- Waarom maar 20%: K2-NEW verdient 3,7 keer zoveel per ontvanger als B2-NOTCLICKED. De verwachte winst is kleiner dan het risico.

## 3. Wat er per plaatsing aan de brief moet veranderen

### Altijd, in elke plaatsing

| Punt in de brief nu | Probleem | Wijziging |
| --- | --- | --- |
| "Years ago, I was working as a chef in a restaurant ... I threw off my apron" | Botst met het oprichtersverhaal in PLAYBOOK §1: begonnen met titanium snijplanken, uitgegroeid tot cookware. Een verzonnen verhaal is een bewijsrisico | Het echte verhaal: begonnen met titanium snijplanken, toen de pan die er nog niet was. Het chef-verhaal alleen als Floris bevestigt dat het waar is |
| "In November 2024, we finally started bringing our pans to the public" | DECISIONS 1 okt: eerste orders 20 december 2024 | "On December 20, 2024, we shipped our first hammered titanium pans." |
| "All of them are selling pans they claim are made with real titanium when that simply isn't what they're delivering" | Onbewezen en toetsbaar, dus onderbouwing nodig (FTC). En het valt op ons terug: Siraat is drie lagen met een titanium kookoppervlak. Klanten denken dat Okura en Taima "fully titanium" zijn (1d) | Weg. Zeg wat Siraat wel is: "a pure titanium cooking surface, no coating", met de bouw eerlijk in één zin (zie de FAQ-regel over de magneet in `research/voc/2026-11-synthese.md` §4.4, na bevestiging van de opbouw) |
| "hundreds of lookalikes ... Some are even doing bigger numbers than us" | Niet te bewijzen; de tweede zin werkt tegen ons | "You've probably seen pans that look exactly like ours." |
| "be careful with those comparison websites ... Fake reviews" | Onbewezen beschuldiging, en een glazen huis: onze eigen Okendo-rijen zijn voor 52% dubbele teksten en de site noemt 38,393 reviews tegen 2,289 in de widget (`research/voc/2026-11-synthese.md` §4.2) | Weg. Vervangen door wat de lezer zelf kan nagaan |
| "We don't even have enough stock to serve everyone" | Valse schaarste; DECISIONS 1 nov verbiedt het (voorraad is net binnen) | Weg |
| "Don't buy it ... If you don't buy a Siraat pan... DON'T BUY ANY" | Klinkt als een truc (anti-pitch), lokt "scam"-reacties uit en heeft geen knop | Eén rustige knop: "See the lab report" of "See the pan you looked at" |
| "PLEASE. Don't start comparing" | De lezer vergelijkt al; de brief moet hem helpen dat goed te doen | Kantelen naar de drie vragen uit de chef-video (DECISIONS 1 okt): (1) is there an independent lab report, (2) a certificate with the lab's name and a report number (Light Labs 25895), (3) a warranty that outlasts you (75 years). "Ask every brand these three questions. Including us." |
| "The Founder of Siraat" | DECISIONS 7 okt en PLAYBOOK: altijd Benjamin | "Benjamin" / "Founder, Siraat" |
| Hoofdletters, "PLEASE", "YOUR money" | Flows zijn kalm register (PLAYBOOK §1) | Zinskapitalen, geen roepende woorden |
| Footer "30-day returns" | Open punt VoC §4.1 | Zodra Floris kiest: "30-day returns on unused items" |

Vaste header en footer blijven (CLAUDE.md). De brief blijft live tekst, zonder afbeelding als tekstdrager (concurrentenidee 22).

### Browse (aanbeveling 1)

- Opening die naar het bezoek verwijst: "You were looking at the {{ event.Name }} again. Before you compare it with the others, here's what I'd check." Productnaam alleen als hij in het event staat, anders zonder naam.
- Na de drie vragen één kort productblok van de bekeken pan (`{{BLOCK:productcard}}`) en één knop naar die pan. Een tweede, tekstlink naar de labresultaten.
- Geen BF-code; na 1 dec geen sale-taal. Wel de friction reducers in één regel: verzending, 30-day returns (formulering zoals Floris besluit), 75-year warranty.
- Onderwerp, bijvoorbeeld: "Before you compare titanium pans". Preview: "Three questions to ask any brand. Including us."

### Welcome considerers (alternatief 2)

- Geen product-event in de welcome: de knop gaat naar de labresultaten of naar de Pan Pro Standard, en HI10 staat in de P.S., zoals in W2.
- Op W2 laten aansluiten: "the pan nobody else was making" en 20 dec 2024 in één zin, niet twee keer het hele kopieenverhaal. De vergelijking met PFAS-pannen (`{{BLOCK:vs kind="pfas"}}`) staat al in W1, dus geen tweede vergelijkingsblok (één vergelijking per flow, PLAYBOOK).

### Cart K2-NEW (alternatief 3)

- Het cartproduct bovenaan, met de prijs uit de cart.
- Na de drie vragen de rekensom tegen het prijsbezwaar ("one pan for 10 years"), want hier wint de kopie op prijs (1d).
- Korter dan de browseversie: maximaal 3.600 px op 390 px breed (PLAYBOOK, verkoopmail).

## 4. Risico's

1. **De brief keert zich tegen ons.** Pre-sale vragen gaan vooral over massief tegenover gelaagd titanium (67 tickets in 180 dagen). Ads en de productnaam zeggen nog "100% pure titanium", terwijl de constructie drie lagen is (`research/voc/2026-11-synthese.md` §4.4). Als we andere merken neerzetten als "geen echt titanium", krijgen we dezelfde vraag terug, harder. Dit punt weegt het zwaarst. De herschrijving in sectie 3 is daarom een voorwaarde, geen verfijning.
2. **Overlap met BFCM tot begin december.** Nieuwe aanmelders krijgen BF-W1 (SdaYcV, direct), bfw2 (dag 1, 10:00) en bfw3 (dag 2, 09:00) uit YqKCmH. De welcome-tak met 30% stopt na mail 1 voor wie BF-W1 kreeg, en de v6d-tak (70%) slaat E1 tot E5 over als er in 2 weken een BFCM-mail was. Een browse-B2 op dag 2 om 09:00 valt dus op dezelfde ochtend als bfw3: drie mails in ongeveer 24 uur voor iemand die aanmeldt en kijkt. Daarom pas starten op 2 december, of tot die tijd in de browse-tak filteren op "geen mail uit YqKCmH in de laatste 24 uur".
3. **Smart sending.** Browse, cart, checkout en welcome hebben smart sending uit; alleen BF follow-up (YqKCmH) heeft het aan (16 uur). Een bfw-mail kan dus wegvallen door een browse-mail, maar niet andersom. Laat smart sending uit in de testtak, anders gaat de test over wie er toevallig doorheen komt. Overlap regelen met de bestaande flowfilters.
4. **Toeschrijving.** Klaviyo schrijft orders toe aan geopende mails. Een lange tekstmail wordt anders geopend dan een beeldmail. Lees de test op alle orders van iedereen in de split, niet op toegeschreven omzet (les uit `research/v6-golive/20-welcome-analyse.md`).
5. **Kleine aantallen.** Met de huidige volumes duurt een betrouwbare uitslag 5 tot 6 weken (browse) of ongeveer 8 weken (welcome-tak). Tussentijdse cijfers zijn ruis; alleen de stopregels gelden eerder.
6. **Uitschrijvingen.** Lange founder-mails in de welcome zitten op 1,0 tot 1,4% uitschrijving (1c). In browse ligt de basis op 0,72%; de stopregel van 1,5% beschermt de lijst.

## 5. Wat ik niet kon onderzoeken

- Shopify en Triple Whale (eerste bezoek tot eerste order, aandeel kopers met meerdere sessies): niet gedaan. Klaviyo Viewed Product ziet alleen bekende profielen, dus anonieme bezoeken vóór de aanmelding ontbreken. Het percentage terugkomers (27,7%) is daardoor een ondergrens.
- Gorgias: trefwoordtelling, geen handcodering. "coated" telt ook "non-coated" mee. Of iemand vóór het ticket al besteld had, heb ik niet aan orders gekoppeld; ik heb het kenmerk "pre-sale" van Gorgias zelf gebruikt.
- Eerdere orders zijn alleen vanaf 1 sep 2026 meegenomen om kopers uit het cohort te halen. Over 12 maanden was 1,3% van de aanmelders al koper, dus het effect is klein.
- De basislijn voor B2-NOTCLICKED (2,5%) geldt voor alle kijkers zonder order na 48 uur, niet precies voor wie B1 niet aanklikte. Meet in week 1 van de test de echte basis in arm A en reken het minimum opnieuw uit.
- Juridische toetsing van vergelijkende claims: alleen de FTC-beleidstekst gelezen, geen advies.
