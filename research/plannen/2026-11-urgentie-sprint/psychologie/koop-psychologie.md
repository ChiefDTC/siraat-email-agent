# Koop-psychologie: waarom en wanneer mensen kopen, en waar de grens ligt (8 nov 2026)

Doel (Floris): één referentiekader voor het hele team (Homestead, copywriters, designers, Claude). Welke psychologische hefbomen sturen de aankoop van een pan van $100 tot $300, op welk moment in de reis werkt welke boodschap, en waar gaat eerlijke overtuiging over in manipulatie. Dit stuk gaat over de onderliggende koop-psychologie en timing. De catalogus van dark patterns, met juridisch kader en wat er nu op de live site misgaat, staat in `../black-hat/black-hat-referentie.md`. Dit bestand verwijst daarnaar voor de black-hat-kant en herhaalt die niet.

Alleen gelezen. Niets in Klaviyo, Shopify of de site gewijzigd. Eigen data: Klaviyo `POST /api/metric-aggregates` op Placed Order (RSNxYV) per dag en per uur (dec 2025 tot 7 nov 2026, en 1 nov tot 5 dec 2025), plus bestaande bevindingen uit `../scheduling/kalender.md`, `research/smooche/00-plan.md`, `research/popup/2026-11-trigger-test.md`, `research/plannen/2026-11-welcome-audit.md` en `research/cro/01-funnel.md`. Alleen totalen, geen persoonsgegevens.

**Bronkwaliteit** (staat bij elk bewijs):

| Label | Betekenis |
|---|---|
| **[PR]** | Peer-reviewed onderzoek (tijdschrift, veldexperiment of meta-analyse) |
| **[IND]** | Grote steekproef uit de industrie (Adobe, Shopify, Klaviyo, Omnisend; eigen meting van een platform, methode deels openbaar) |
| **[V]** | Vendor-claim (app-maker, blog, persbericht zonder methode) |
| **[A]** | Anekdote, vuistregel of eigen inschatting |
| **[S]** | Siraat-eigen data (Klaviyo, Clarity, Intelligems); echt gemeten, maar vaak kleine aantallen en zonder controlegroep |

---

## 0. Kort (voor wie maar één scherm leest)

1. **Echte deadlines zijn de sterkste hefboom die we hebben, en we hebben er eigen bewijs voor.** Mails met een echte einddatum halen $0,165 tot $0,171 per ontvanger, zonder deadline $0,03 tot $0,13; 62 tot 74% van de orders van een deadlinemail valt binnen 24 uur [S]. Dat past bij de tweede piek vlak voor de vervaldatum die Inman en McAlister (1994) bij coupons vonden [PR]. Nep-deadlines voegen daar weinig aan toe en kosten vertrouwen (zie black-hat 2.A).
2. **Snelheid wint het van overtuigen op het eerste moment.** 60% van de pop-upkopers koopt binnen 10 minuten, 90% binnen 24 uur [S]. W1 levert $3,09 per ontvanger, W2 tot W5 samen $0,32 [S]. Het eerste contact moet kort zijn en direct naar het aanbod; uitleg hoort later.
3. **Siraat-kopers kopen 's ochtends en in het weekend.** US 35% van de orders tussen 06:00 en 12:00 lokaal, piek 09:00 tot 12:00; zaterdag en zondag het sterkst (trendgecorrigeerd jaarindex 113 en 119, donderdag 89) [S]. Op feestdagen schuift het naar middag en avond: Black Friday 2025 piekte om 17:00 ET, Thanksgiving om 21:00 ET [S].
4. **Vorig jaar viel een derde van de novemberorders in de Cyber 5.** 1 nov tot 1 dec 2025: 15.645 orders. Week 1 9%, week 2 15%, week 3 20%, 22 tot 26 nov 23%, Thanksgiving tot Cyber Monday 33%. Black Friday alleen al 10% (1.565 orders, 5,8 keer een gewone dag in begin november) [S].
5. **Begin van de maand en begin van het jaar verkopen beter.** Dag 1 tot 7 van de maand index 108 tot 109, dag 15 tot 28 index 94 tot 96 (trendgecorrigeerd, jan tot okt 2026) [S]; januari 2026 was de sterkste maand buiten Q4 (9.057 orders). Past bij het fresh-start-effect [PR] en bij loonbetaling [PR], maar valt ook samen met onze eigen campagnekalender.
6. **Gratis werkt sterker dan korting van dezelfde waarde** (Shampanier, Mazar en Ariely 2007) [PR]. De gifts zijn dus geen bijzaak; ze moeten echt gratis, concreet en met echte waarde gepresenteerd worden.
7. **Tegoed voelt als ander geld.** Gift cards en tegoed worden vrijer uitgegeven, vooral aan "leuke" dingen (Helion en Gilovich 2014) [PR], en korte geldigheid verhoogt verzilvering fors (Shu en Gneezy 2010) [PR]. Het Rise-tegoed is daarom krachtig, mits het bedrag en de vervaldatum echt zijn.
8. **De rode lijn is altijd dezelfde vraag: zou de klant zich bedrogen voelen als hij wist wat wij weten?** Als een deadline, voorraad, prijs, tegoed of review niet waar is in de backend, mag het niet in de mail. Dat is ook de juridische lijn (FTC, CAN-SPAM, UCPD bijlage I, Omnibus; zie black-hat sectie 1).

---

## 1. Siraat-eigen data in één overzicht [S]

### 1.1 Wanneer kopen onze klanten?

| Meting | Uitkomst | Bron |
|---|---|---|
| Uur van de dag (lokaal, 8.731 orders 9 okt tot 8 nov) | US piek 09:00 tot 12:00 (7,4 tot 7,7% per uur), INT 08:00 tot 11:00 (8,4 tot 8,5%); 18:00 tot 24:00 nog 23 tot 24%; na 22:00 sterke daling | `scheduling/kalender.md` 1.1 |
| Weekdag (dec 2025 tot nov 2026, ten opzichte van 29-daags voortschrijdend gemiddelde) | ma 96, di 93, wo 90, do 89, vr 98, **za 113, zo 119** | nieuwe meting, deze sessie |
| Weekdag laatste 30 dagen (lokaal) | US za 123, INT za 143 en zo 129 | `kalender.md` 1.2 |
| Dag van de maand (jan tot okt 2026, 72.150 orders, trendgecorrigeerd) | dag 1 tot 3: 109, dag 4 tot 7: 108, dag 8 tot 14: 101, dag 15 tot 17: 96, dag 18 tot 24: 94, dag 25 tot 28: 95, dag 29 tot 31: 100 | nieuwe meting |
| Jaarwissel | 20 tot 24 dec 2025: 101 tot 156 orders per dag; 1 tot 3 jan 2026: 311 tot 343. Januari 9.057 orders, hoogste maand buiten nov/dec | nieuwe meting |
| Gemiddelde orderwaarde per maand | jan $188, mei $218, okt $228, nov (tot 7e) $249 | nieuwe meting |

Let op bij de dag van de maand: Homestead en wij sturen vaak een nieuwe actie rond de 1e (Nov E1 op 1 nov, oktober-actie). Het effect is dus deels eigen kalender, niet alleen loonbetaling. Richting, geen wet.

### 1.2 De BFCM-curve van 2025 (Placed Order per dag, Eastern Time)

| Periode 2025 | Orders | Aandeel van 1 nov tot 1 dec |
|---|---|---|
| 1 tot 7 nov | 1.415 | 9,0% |
| 8 tot 14 nov | 2.356 | 15,1% |
| 15 tot 21 nov | 3.183 | 20,3% |
| 22 tot 26 nov (weekend voor Thanksgiving tot woensdag) | 3.590 | 22,9% |
| 27 nov (Thanksgiving) tot 1 dec (Cyber Monday) | 5.101 | 32,6% |
| waarvan Black Friday 28 nov | 1.565 | 10,0% |
| waarvan Cyber Monday 1 dec | 967 | 6,2% |

Dagwaarden in de Cyber 5: Thanksgiving 841, Black Friday 1.565, zaterdag 1.062, **zondag 666 (dal)**, Cyber Monday 967, daarna 655, 518, 410, 289.

Uurprofiel (ET, hele winkel, dus inclusief INT in de nacht):

| Dag 2025 | Piekuur ET | 00 tot 06 | 06 tot 12 | 12 tot 18 | 18 tot 24 |
|---|---|---|---|---|---|
| Thanksgiving 27 nov | 21:00 | 22% | 21% | 29% | 27% |
| Black Friday 28 nov | 17:00 | 21% | 27% | 33% | 18% |
| zaterdag 29 nov | 09:00 | 24% | 29% | 26% | 21% |
| Cyber Monday 1 dec | 15:00 | 24% | 27% | 30% | 18% |

Lezing: (1) De opbouw is geleidelijk; elke week meer dan de vorige, het weekend vóór Thanksgiving is al sterk. Wachten met de beste boodschap tot Black Friday laat 57% van de maand liggen. (2) Black Friday is de grootste dag, maar het is een middagdag; de avond van Thanksgiving (gezin, telefoon op de bank) is een eigen moment. (3) De zondag van het Cyber-weekend is het dal: de beste dag om niet te pushen of alleen te herinneren. (4) Dit jaar loopt de sale tot 30 nov (maandag), dus de laatste dag is zelf een Cyber Monday met een echte einddatum: dubbel moment.

### 1.3 Hoe snel kopen ze na een contact?

| Moment | Uitkomst | Bron |
|---|---|---|
| Pop-up naar aankoop | 60% van de kopers binnen 10 minuten (vóór W1), 90% binnen 24 uur | `smooche/00-plan.md` |
| W1 tegenover de rest | W1 $3,09 per ontvanger (117 orders), W2 tot W5 samen $0,32; BF-W1 $3,58 | `2026-11-welcome-audit.md` |
| Deadlinemail | 31 okt "ENDS TONIGHT" 74% van de orders binnen 24 uur, 4 nov "today only" 62%, gemiddeld alle campagnes 51% | `kalender.md` 1.3 |
| Brief van Benjamin om 13:07 ET | 85% van de orders binnen 24 uur, 40% binnen 6 uur | `kalender.md` 1.3 |
| Op de productpagina (Clarity, mobiel, betaald) | Add to cart mediaan 1:35, eerste klikken rond 36 s; na 30 s nog 39% op de site; 37% van de sessies is nooit zichtbaar (in-app prefetch) | `popup/2026-11-trigger-test.md` |
| Founder-notes | 1,3% klik tegen 0,3 tot 0,6% voor beeldmails | PLAYBOOK 1 |

### 1.4 Apparaat en betalen

- Mobiel 82% van de sessies; mobiel converteert ongeveer gelijk aan desktop (Triple Whale 1,18 tegen 1,24%) en doet zelfs meer add-to-carts. Het verlies zit in winkelwagen naar checkout (mobiel 75% verlaat de winkelwagen, desktop 70%) [S, `cro/01-funnel.md`].
- Betalen: bijna alles Shop Pay en Apple Pay; Shop Pay Installments en Affirm alleen in de US; checkouts boven $349 blijven 26 tot 37% onbetaald; geen BNPL voor AU, UK, CA, NZ [S].

---

## 2. De hefboomkaarten

Per kaart: **wat het is**, **bewijs**, **wanneer het werkt**, **hoe Siraat het eerlijk inzet**, **waar het black-hat wordt (rode lijn)** en **hoe we het meten**. Voorbeeldregels zijn in het Engels, zoals in de mails. Ze volgen de vaste claims (30-day returns, 75-year warranty, 100,000+ happy customers, Benjamin als oprichter) en de skill siraat-direct-response.

Journey-momenten die in de kaarten terugkomen: **pop-up**, **welcome**, **browse**, **cart**, **checkout**, **post-purchase**, **winback**, **campagne**, **laatste uren**.

---

### Kaart 1. Verliesaversie

- **Wat het is.** Een verlies weegt psychologisch ongeveer twee keer zo zwaar als een even grote winst. "Mis $305 aan korting" voelt sterker dan "bespaar $305".
- **Bewijs.** Kahneman en Tversky (1979, prospecttheorie) en Tversky en Kahneman (1991): verliesaversie-coëfficiënt rond 2 [PR]. Een meta-analyse (Brown e.a. 2024, Journal of Economic Literature, 607 schattingen) vindt gemiddeld rond 1,8 tot 2 [PR]. Let op: in kleine, alledaagse bedragen is het effect kleiner (Gal en Rucker 2018 noemen het overschat) [PR].
- **Wanneer het werkt.** Cart en checkout (de klant heeft al iets "in handen"), laatste uren, verlopend tegoed, winback. Het werkt slecht bij koude bezoekers die nog niets bezitten (pop-up, eerste advertentie).
- **Hoe Siraat het eerlijk inzet.** Het verlies benoemen dat echt gebeurt: "Your 70% price ends tonight at 11:59 PM PT. After that, the Pan Pro Standard goes back to $439." (alleen als de compare-at echt terugkomt). Of: "Your $22 store credit expires Sunday. It can't be moved to a new date." (alleen als Rise dat zo instelt).
- **Rode lijn.** Een verlies verzinnen dat niet bestaat: "your cart will be deleted", "price held for 15 minutes", "your order is pending" (black-hat A1, E-groep). Ook fout: angst als hoofdtoon (PLAYBOOK 1: bewijs eerst, dan vreugde). Gezondheidsangst ("PFAS is poisoning your family") is verboden.
- **Meten.** A/B onderwerpregel winst- tegen verliesframing, winnaar op unieke kliks en RPR; vangrails uitschrijving (onder 0,5%) en spamklachten (onder 0,1%).

### Kaart 2. Endowment (bezit voelt waardevoller)

- **Wat het is.** Wat we al (een beetje) bezitten, waarderen we hoger. Een gevulde winkelwagen, een "gereserveerd" tegoed op naam of een gekozen maat voelt al als van jou.
- **Bewijs.** Kahneman, Knetsch en Thaler (1990): mokken-experiment, verkopers vroegen ongeveer twee keer zoveel als kopers wilden betalen [PR]. Effect is groter als het bezit concreet en persoonlijk is; kleiner bij handelaren en bij abstracte goederen (List 2003) [PR].
- **Wanneer het werkt.** Cart en checkout (toon het eigen product met foto), post-purchase (de pan staat in je keuken), tegoed (bedrag op naam), maatkiezer in welcome (W4 "Who are you cooking for?").
- **Hoe Siraat het eerlijk inzet.** De eigen winkelwagen tonen met foto, maat en prijs, knop "Return to my cart" (PLAYBOOK 10). In post-purchase: "Your pan arrives this week. Here is the first thing to cook in it." Bij tegoed: "Benjamin, your account holds $22 in store credit."
- **Rode lijn.** Bezit suggereren dat er niet is: "Your order #4471 is waiting", een nep-orderbevestiging, "(1) item reserved for you", "Your gift is on hold" zonder dat iets is vastgezet. Dat is black-hat E-groep (nep-persoonlijke status).
- **Meten.** RPR cart- en checkoutmails met en zonder productblok; klik op "Return to my cart" tegen generieke knop.

### Kaart 3. Deadlines en de laatste-uren-piek

- **Wat het is.** Een einddatum zet uitstel om in beslissen. Mensen beslissen vooral net na het eerste contact en net voor het einde, met een dal ertussen.
- **Bewijs.** Inman en McAlister (1994, Journal of Marketing Research): coupon-verzilvering heeft naast de piek bij uitgifte een tweede piek vlak vóór de vervaldatum, verklaard met spijt-theorie [PR]. Krishna en Zhang (1999, Management Science) over korte tegenover lange coupontermijnen [PR]. Siraat: deadlinemails 62 tot 74% van de orders binnen 24 uur, RPR $0,165 tot $0,171 tegen $0,03 tot $0,13 zonder deadline [S, kleine aantallen: 20 tot 60 orders per campagne]. Adobe: op Cyber Monday 2025 lag de piek tussen 20:00 en 22:00 met $16 mln per minuut, de laatste uren van de Cyber-week [IND]. Let op: bij ons verschoof het op deadlinedagen niet naar de avond (31 okt 24% na 18:00); de deadline maakt de hele dag drukker [S].
- **Wanneer het werkt.** Campagne (start en einde), laatste uren, verlopende unieke codes in checkout/cart (K3, C4, B2), tegoed dat verloopt, VIP-weekend, wekelijkse trekking "order by Sunday".
- **Hoe Siraat het eerlijk inzet.** Eén backend-eindtijd per regio met tijdzone in de copy (`kalender.md` sectie 3): "Ends tonight at 11:59 PM PT." Countdown-GIF alleen als die naar dezelfde echte eindtijd telt. Hoofdmail 's ochtends, avondbrief (LAST-HOURS, 17:00 lokaal, op 30 nov 20:00) als vangnet voor wie al keek.
- **Rode lijn.** Een deadline die niet eindigt of terugkomt: "ends tonight" terwijl de sale doorloopt, resettende timer per bezoeker, "no extensions" en daarna verlengen (black-hat A1 tot A4). Siraat-site doet nu A1 (timer in localStorage); dat moet eerst weg, anders ondermijnt het de echte deadline in de mail.
- **Meten.** Aandeel orders binnen 24 uur na verzending, RPR per deadlinemail, en na de deadline: zakt de verkoop echt (zo niet, dan geloofde niemand hem). Over meerdere weken: RPR van deadlinemails mag niet dalen (gewenning).

### Kaart 4. Korte versus lange termijn (uitstel)

- **Wat het is.** Bij een lange termijn denken mensen "dat doe ik later" en vergeten het. Een kortere termijn verhoogt de kans dat het echt gebeurt, ook als die objectief minder gunstig is.
- **Bewijs.** Shu en Gneezy (2010, Journal of Marketing Research, "Procrastination of enjoyable experiences"): bonnen voor een bakkerij met een termijn van ongeveer drie weken werden ruim drie keer zo vaak verzilverd als bonnen van twee maanden (in de veldstudie rond 31% tegen 6%); niet-verzilveraars zeiden "I kept thinking I could do it later" [PR]. Precieze percentages verschillen per samenvatting; het originele artikel is leidend.
- **Wanneer het werkt.** Tegoed (Rise), unieke codes in cart/checkout/browse (48 uur), post-purchase cross-sell, winback-aanbod.
- **Hoe Siraat het eerlijk inzet.** Het tegoed voor nieuwe orders (5 points per $1) is 90 dagen geldig; zet in de herinneringsmails een concreet tussenmoment ("Use it before Dec 20 and it arrives before Christmas" als de verzendcutoff klopt). BF-tegoed: korte, echte termijn (bijvoorbeeld 30 nov) en één herinnering per fase, niet elke dag.
- **Rode lijn.** De termijn kunstmatig inkorten in de mail terwijl de code of het tegoed in de backend langer geldig is, of een "48-hour code" die in Shopify een jaar geldt (bevinding flows-ontwerp: Coupon Assigned toont 1 jaar). Dan is de deadline onwaar, ook al is het aanbod goed.
- **Meten.** Verzilveringspercentage tegoed en codes per termijnlengte (test 14 tegen 30 dagen in januari, niet in BF).

### Kaart 5. Schaarste

- **Wat het is.** Wat beperkt beschikbaar is, lijkt waardevoller en vraagt nu-actie. Werkt sterker als de schaarste net ontstaat of komt door vraag van anderen.
- **Bewijs.** Worchel, Lee en Adewole (1975): koekjes uit een pot met 2 werden hoger gewaardeerd dan uit een pot met 10, nog hoger als de pot net leeg raakte door vraag [PR]. Cialdini (Influence, 1984/2021) als overzicht [A, boek op basis van PR]. Meta-analyse Lynn (1991): schaarste verhoogt waardering, effect matig [PR]. Mathur e.a. (2019, CSCW, 11.000 webshops): low-stock- en high-demand-berichten zijn een van de meest voorkomende dark patterns, deels willekeurig gegenereerd [PR].
- **Wanneer het werkt.** Campagne (beperkte oplage of beperkt aantal gifts), cart (als een maat echt bijna op is), back-in-stock, mystery gift zolang de voorraad strekt.
- **Hoe Siraat het eerlijk inzet.** Alleen met een echte, controleerbare bron: Shopify-voorraad of een vast aantal. "We packed 2,000 mystery gifts for Black Friday. When they're gone, orders ship without one." (alleen als dat zo is en we het teller-getal echt bijhouden). Of tijdschaarste in plaats van voorraadschaarste: de gifts eindigen als de sale eindigt (echt).
- **Rode lijn.** Nep-voorraad en nep-vraag: "only 3 left" zonder voorraaddata, de hardgecodeerde "93% sold"-balk en "Due to high demand, quantities are limited" die nu op de site staan (black-hat B1 tot B3, UCPD bijlage I punt 7). "Limited restock" in de BIS-flow controleren.
- **Meten.** Alleen inzetten met echte voorraad; dan CR per sessie met en zonder voorraadregel. Klachten en reviews met "fake" als vangrail.

### Kaart 6. Goal-gradient (bijna-daar-effect)

- **Wat het is.** Hoe dichter bij een doel, hoe harder mensen werken om het te halen. Ook een kunstmatige voorsprong (2 stempels cadeau op een kaart van 12) versnelt.
- **Bewijs.** Kivetz, Urminsky en Zheng (2006, Journal of Marketing Research): koffiekaartklanten kochten sneller naarmate de gratis koffie dichterbij kwam; een kaart van 12 met 2 bonusstempels werd sneller afgemaakt dan een kaart van 10 zonder; ook online op een muziekbeoordelingssite [PR]. Na het doel zakt de motivatie (reset). Nunes en Drèze (2006) over de "endowed progress" [PR].
- **Wanneer het werkt.** Punten en tegoed (Rise), gratis verzending of een gift boven een drempel, cart (bijna bij de volgende tier), post-purchase (tweede aankoop), VIP-status.
- **Hoe Siraat het eerlijk inzet.** "You have 1,850 points. At 2,500 points your next order gets $25 off." Of in de cart: "Add the Small Pan Pro and your order qualifies for the 6-piece set price." Startbonus mag (zoals de 2 bonusstempels) als die echt op het account staat: "We added 500 welcome points to your account."
- **Rode lijn.** Een voortgangsbalk die niet klopt of nooit gehaald kan worden, punten die stilletjes minder waard worden, of een drempel die verschuift als je hem nadert. Ook: punten tonen als korting terwijl het tegoed technisch niet stapelt met de BF-korting, zonder dat te zeggen.
- **Meten.** Verzilvering en tijd tot tweede order per puntenstand; AOV in de buurt van drempels (zit er een piek net boven de drempel, dan werkt het).

### Kaart 7. Mental accounting (tegoed en gift cards als "ander geld")

- **Wat het is.** Mensen verdelen geld in potjes. Tegoed, een cadeaubon of "gevonden geld" komt in een potje voor iets leuks en wordt makkelijker uitgegeven dan geld van de eigen rekening.
- **Bewijs.** Thaler (1985, 1999, mental accounting) [PR]. Helion en Gilovich (2014, Journal of Behavioral Decision Making): met een gift card gaven mensen meer uit aan hedonistische producten, in het lab en in een campusboekwinkel, omdat ze zich minder schuldig voelen [PR]. Arkes e.a. (1994): onverwacht verkregen geld wordt sneller en vrijer uitgegeven [PR]. Siraat: het tegoedplan rekent met 3 tot 10% verzilvering en een gemiddeld tegoed van ~$22 per koper [A, schatting in `2026-11-punten-store-credit.md`].
- **Wanneer het werkt.** Tegoed na aankoop (post-purchase, VIP), winback ("je hebt nog $22"), campagne CREDIT, welcome als "gift card" in plaats van code (besluit 7 okt, A/B HI10 als code tegen gift card).
- **Hoe Siraat het eerlijk inzet.** Het tegoed als bedrag op naam met herkomst: "Your last order earned you $22 in store credit. It's already in your account and works at checkout." Hedonistisch framen past: "Put it toward the Wok you've been eyeing."
- **Rode lijn.** Verzonnen tegoed ("You have $50 waiting" zonder Rise-saldo), tegoed dat alleen werkt bij een minimum dat niet genoemd wordt, of tegoed dat in de mail "geld" heet maar alleen bij volle prijs geldt. Black-hat E-groep en BRIEF ("verzonnen tegoed" verboden).
- **Meten.** Verzilveringspercentage, incrementaliteit met een holdout (10% van de tegoedgroep krijgt geen mail), AOV van tegoed-orders tegenover gewone orders.

### Kaart 8. Ankers en referentieprijzen

- **Wat het is.** Het eerste getal dat we zien, stuurt wat we redelijk vinden. Een doorgestreepte prijs of een vergelijking ("onder $100 per pan") verandert hoe de prijs voelt.
- **Bewijs.** Tversky en Kahneman (1974, anchoring) [PR]. Ariely, Loewenstein en Prelec (2003, "coherent arbitrariness"): zelfs een willekeurig getal (laatste cijfers van het sofinummer) verschoof de betalingsbereidheid met 60 tot 120% [PR]. Meta-analyse Compeau en Grewal (1998): advertised reference prices verhogen waargenomen waarde en koopintentie [PR]. Juridisch: Omnibus artikel 6a (EU, laagste prijs 30 dagen) en FTC Guides Against Deceptive Pricing (16 CFR 233, US) [wet].
- **Wanneer het werkt.** Campagne, welcome W3 ("What 70% off actually gets you"), productkaarten, cart (besparing in dollars).
- **Hoe Siraat het eerlijk inzet.** Alleen echte compare-at uit Shopify die Floris bevestigde (Pan Pro Standard $439 bij $134, 12-delige set $1,186 bij $599, Roasting Pan $250 bij $199; PLAYBOOK 12). Waarde-ankers die controleerbaar zijn: "6 pieces for $349. Under $60 a piece, with a 75-year warranty." Of het anker per jaar: "$134 over 75 years of warranty is under $2 a year."
- **Rode lijn.** Een compare-at waarvoor nooit verkocht is, het percentage in de EU niet op de laagste prijs van 30 dagen baseren, de eigen verkoopprijs doorstrepen om een codeprijs te tonen, of "was $249" schrijven als die prijs niet terugkomt (besluit 8 nov: zinnen geschrapt). Zie black-hat D-groep.
- **Meten.** CR per productkaart met en zonder anker; retouren en klachten "not really on sale".

### Kaart 9. Het free-effect (gratis is een eigen categorie)

- **Wat het is.** Nul is geen gewone prijs. Iets gratis krijgen voelt als winst zonder risico, en mensen kiezen het onevenredig vaak.
- **Bewijs.** Shampanier, Mazar en Ariely (2007, Marketing Science): bij Hershey's Kiss 1 cent en Lindt-truffel 15 cent koos ongeveer 27% de Kiss; bij Kiss gratis en truffel 14 cent (zelfde verschil) koos ongeveer 69% de Kiss. "De prijs naar nul brengen is sterker dan een vijf keer grotere verlaging binnen positieve prijzen" [PR]. Gratis verzending als drempel: veel vendor-data [V].
- **Wanneer het werkt.** Campagne (gifts), welcome, cart en checkout (gifts als één regel in de cart), mystery gift, gratis verzending in de friction reducer.
- **Hoe Siraat het eerlijk inzet.** Gift-with-purchase boven blanco korting (PLAYBOOK 8): "4 gifts with every order: free shipping ($15), the e-guide ($30), a mystery gift ($25) and a chance to win a PFAS water filter." Alleen "win" bij de filter, nooit "free filter" (PLAYBOOK 11). Echte waarde per gift tonen.
- **Rode lijn.** "Free" dat niet gratis is (verzendkosten op het "gratis" item, gift die alleen bij een niet-genoemde drempel geldt), opgeblazen giftwaarden, of "free filter" voor een trekking. FTC Guide Concerning Use of the Word "Free" (16 CFR 251) [wet].
- **Meten.** A/B "$70 in gifts" tegen "extra 10% off" van dezelfde kostprijs: RPR en AOV.

### Kaart 10. Social proof

- **Wat het is.** Bij twijfel doen we wat anderen zoals wij doen. Specifiek en dichtbij ("mensen in jouw situatie") werkt beter dan vaag ("iedereen").
- **Bewijs.** Goldstein, Cialdini en Griskevicius (2008, Journal of Consumer Research): de norm "75% van de gasten hergebruikt de handdoek" verhoogde hergebruik van 35% naar 44%, en "gasten in deze kamer" nog meer; replicaties zijn gemengd [PR]. Spiegel Research Center (2017, één retailer, 7,8 mln gebruikers): product met 5 reviews heeft 270% hogere koopkans dan zonder; effect groter bij duurdere producten (380%); koopkans piekt bij 4,0 tot 4,7 sterren, niet bij 5,0 [IND]. Schindler en Yalch (2006): precieze getallen ("99.44%") worden als geloofwaardiger gezien dan ronde [PR].
- **Wanneer het werkt.** Browse en cart (twijfel over prijs), welcome W4/W5, checkout (laatste twijfel), campagne. Minder in post-purchase (al gekocht).
- **Hoe Siraat het eerlijk inzet.** Letterlijke Trustpilot-reviews met naam (PLAYBOOK 12, reviews3), een review die een bezwaar beantwoordt ("Expensive but definitely value for money"), "100,000+ happy customers" (goedgekeurd). Precies en dichtbij als het klopt: "Tammy is on her fourth pan." Een eerlijke 4,x-score met een paar kritische reviews werkt beter dan alleen 5 sterren.
- **Rode lijn.** Nepreviews, gekochte reviews met sentimentvoorwaarde, negatieve reviews verbergen, "X people are viewing this" of "Sarah from Ohio just bought" zonder echte data (FTC 16 CFR 465, boete tot $53.088 per overtreding; black-hat C-groep). Let op het open punt: Trustpilot-incentive (gift card voor review) mag volgens Floris, maar dan nooit "independent" of "unsolicited" erbij.
- **Meten.** Klik en RPR per reviewset; CR op de PDP met reviewblok boven tegen onder de vouw.

### Kaart 11. Autoriteit en bewijs (labtest, garantie, oprichter)

- **Wat het is.** Bij een claim die je niet zelf kunt controleren (geen PFAS, puur titanium) vertrouw je op een onafhankelijke bron, een expert of iemand die er persoonlijk voor instaat.
- **Bewijs.** Milgram en de autoriteitsliteratuur in Cialdini [PR/A]. Voor productclaims: derdepartijcertificering verhoogt vertrouwen en betalingsbereidheid, vooral bij geloofsgoederen (credence goods) waar de koper de eigenschap niet kan zien (Dulleck en Kerschbamer 2006, overzicht) [PR]. Siraat: founder-notes 1,3% klik tegen 0,3 tot 0,6% [S]; de drie vragen uit de chef-video (labrapport, certificaat met rapportnummer, 75-jaar garantie) zijn de kern van bewijsmails (besluit 1 okt).
- **Wanneer het werkt.** Welcome W2/W3 (de coating-waarheid), browse (twijfel), checkout (laatste twijfel over gezondheid), winback.
- **Hoe Siraat het eerlijk inzet.** "Tested by Light Labs. Report 25895. Every Siraat pan has the same titanium cooking surface." Met link naar het rapport. Benjamin als afzender en ondertekening ("Benjamin, Founder, Siraat's Kitchen"). Garantie als bewijs van vertrouwen in het product: "75-year warranty. If it fails, we replace it."
- **Rode lijn.** "Doctor recommended", medische claims, nep-experts, een rapport citeren dat iets anders zegt dan de claim, of "100% pure titanium pan" als losse claim (besluit 6 okt: "with a pure titanium cooking surface", altijd met "no coatings"). Concurrenten bij naam aanvallen is verboden.
- **Meten.** Klik op het labrapport, RPR van bewijsmails, Gorgias-tickets over "is it really PFAS-free" (moet dalen).

### Kaart 12. Keuze-overload (en het tegendeel)

- **Wat het is.** Te veel opties kunnen verlammen. Maar niet altijd: wie weet wat hij wil, vindt meer keuze juist fijn.
- **Bewijs.** Iyengar en Lepper (2000): jamproeverij met 24 smaken trok meer mensen, maar 30% kocht bij 6 smaken tegen 3% bij 24 [PR]. Scheibehenne, Greifeneder en Todd (2010, meta-analyse, 50 experimenten, N = 5.036): gemiddeld effect vrijwel nul, met grote spreiding [PR]. Chernev, Böckenholt en Goodman (2015, meta-analyse): overload treedt op bij moeilijke keuzes, onduidelijke voorkeur, complexe opties en tijdsdruk [PR]. Bij ons: op mobiel en in een mail met een deadline zijn juist die omstandigheden aanwezig.
- **Wanneer het werkt.** Pop-up en welcome W1 (één aanbod, één knop), laatste uren (één product, één knop), cart (niet afleiden). Meer keuze mag in welcome W4 (maatkiezer) en in de collectie, voor mensen die al vergelijken.
- **Hoe Siraat het eerlijk inzet.** Per mail één primaire knop, drie keer herhaald (PLAYBOOK 11); maximaal 2 grote onderdelen per mail (PLAYBOOK 12); een duidelijke aanbeveling ("Where I'd start: the Pan Pro Standard") en drie tiers (pan, 6-delig, 12-delig) met een gemarkeerde middelste.
- **Rode lijn.** Keuze verbergen om naar de duurste optie te sturen, een "decoy" die niemand wil en alleen bestaat om een andere optie duur te laten lijken zonder echte functie, of de goedkope optie onvindbaar maken. Vooraf aangevinkte add-ons in de checkout (black-hat F-groep).
- **Meten.** Klikverdeling per knop (UTM per blok), CR per mail met 1 tegen 3 productkaarten.

### Kaart 13. Commitment en consistentie

- **Wat het is.** Na een kleine stap (aanmelden, quiz, maat kiezen) willen mensen consequent blijven en de grotere stap ook zetten.
- **Bewijs.** Freedman en Fraser (1966, foot-in-the-door): wie eerst een klein verzoek toestond, stemde veel vaker in met een groot [PR]. Meta-analyses (Burger 1999) vinden een klein maar betrouwbaar effect [PR].
- **Wanneer het werkt.** Pop-up (aanmelding als eerste ja), welcome (keuze bevestigen), browse (je bekeek de Wok), cart, post-purchase (review, tweede pan bij de eerste), abonnement vaatwasstrips.
- **Hoe Siraat het eerlijk inzet.** Verwijzen naar wat de klant echt deed: "You picked the 11″ Pan Pro. Here's the lid that fits it." Of de aanmelding: "You entered the giveaway. While you wait for the draw, here's your Black Friday price."
- **Rode lijn.** Confirmshaming ("No thanks, I like toxic pans"), een klein ja omzetten in een abonnement zonder duidelijke toestemming (ROSCA; black-hat F/negative option), of een quiz die altijd het duurste antwoord geeft.
- **Meten.** Conversie van browse- en cartmails met verwijzing naar het eigen product tegen generiek.

### Kaart 14. Wederkerigheid (eerst geven)

- **Wat het is.** Wie iets krijgt zonder voorwaarde, voelt de neiging iets terug te doen. Werkt het best als het persoonlijk, onverwacht en echt nuttig is.
- **Bewijs.** Regan (1971): proefpersonen die een ongevraagde cola kregen, kochten twee keer zoveel loten [PR]. Strohmetz e.a. (2002): een snoepje bij de rekening verhoogde de fooi; een persoonlijk extra snoepje nog meer (tot 23%) [PR]. Gneezy en List (2006): het effect van een cadeau kan snel uitdoven [PR].
- **Wanneer het werkt.** Welcome (gratis e-guide, kookadvies vóór het aanbod), post-purchase (educatie eerst, PLAYBOOK backlog 4), mystery gift, winback (een nuttig recept zonder verkoop), mail van Benjamin.
- **Hoe Siraat het eerlijk inzet.** De e-guide en de "first cook"-mail geven zonder voorwaarde. Post-purchase eerst "How to preheat titanium so nothing sticks", pas daarna een cross-sell. Mystery gift als echte verrassing in het pakket.
- **Rode lijn.** Een "cadeau" dat een verplichting verbergt (gratis proef die een abonnement wordt), schuld opwekken ("we gave you this, the least you can do"), of een "gift" waarvan de waarde opgeblazen is.
- **Meten.** Tweede-orderpercentage na 60 dagen voor post-purchase met educatie eerst tegen cross-sell eerst; uitschrijving.

### Kaart 15. Present bias (nu telt zwaarder dan later)

- **Wat het is.** We wegen directe beloning en directe kosten zwaarder dan alles wat later komt. Goed nieuws voor "nu kopen"; slecht nieuws voor een abstract voordeel als "75 jaar meegaan".
- **Bewijs.** Laibson (1997), O'Donoghue en Rabin (1999): hyperbolische verdiscontering en uitstelgedrag [PR]. Gelman e.a. (2014, Science): uitgaven stijgen op de dag dat het salaris binnenkomt en blijven dagen hoger, vooral bij mensen met weinig buffer [PR].
- **Wanneer het werkt.** Pop-up en welcome (direct voordeel), cart en checkout (verzending, levertijd voor de feestdagen), BNPL, campagne met "today's price".
- **Hoe Siraat het eerlijk inzet.** Het lange voordeel naar nu halen: "Tonight's dinner, no sticking, no coating." Directe voordelen voorop: gratis verzending, gifts in dit pakket, "order by Dec 15 for Christmas" (alleen met de echte verzendcutoff).
- **Rode lijn.** Inspelen op impuls bij mensen die het niet kunnen betalen (BNPL agressief pushen, zie kaart 18), of "arrives tomorrow" zonder dat het klopt (nooit levertijden in marketingmails, PLAYBOOK 11).
- **Meten.** Klik op "today"-framing tegen "for life"-framing per moment; orders per dag van de maand (zie 1.1).

### Kaart 16. Spijt-aversie en risico wegnemen

- **Wat het is.** Mensen vermijden beslissingen waar ze later spijt van kunnen krijgen. Twee kanten: spijt van kopen (verkeerde maat, werkt het wel) en spijt van niet kopen (prijs weg). Een garantie of retourbelofte haalt de eerste weg.
- **Bewijs.** Simonson (1992, Journal of Consumer Research): wie zich de spijt voorstelt, kiest vaker nu en vaker het veilige merk [PR]. Inman en McAlister (1994) verklaren de deadline-piek met spijt [PR]. Over garanties en retourbeleid: een meta-analyse van Janakiraman, Syrdal en Freling (2016): ruimer retourbeleid verhoogt aankopen meer dan retouren [PR].
- **Wanneer het werkt.** Checkout en cart (laatste twijfel), browse, welcome W3 (bezwaren), laatste uren (spijt van niet kopen).
- **Hoe Siraat het eerlijk inzet.** Friction reducer onder elke knop: "Free shipping. 30-day returns. 100,000+ happy customers." (PLAYBOOK 12). Maatspijt wegnemen: "Not sure about the size? Swap it within 30 days." (alleen als ruilen zo werkt). Spijt van niet kopen eerlijk: "If you've been waiting for the lowest price of the year, this is it." (alleen als dat waar is).
- **Rode lijn.** Spijt opwekken met onwaarheid ("you'll never see this price again" als dezelfde prijs in januari terugkomt), garantie of retour mooier voorstellen dan de voorwaarden ("lifetime" of "100-day trial", besluit 1 okt: nooit), of retour moeilijk maken na verkoop.
- **Meten.** CR checkoutmails met en zonder friction reducer; retourpercentage (mag niet sterk stijgen).

### Kaart 17. Fresh start (tijdsmarkeringen)

- **Wat het is.** Rond een nieuw begin (maandag, de 1e van de maand, nieuwjaar, verjaardag, verhuizing) voelen mensen zich losser van hun oude zelf en beginnen ze vaker aan iets ambitieus: gezonder koken, een nieuwe keuken.
- **Bewijs.** Dai, Milkman en Riis (2014, Management Science): Google-zoekopdrachten naar "diet", sportschoolbezoek en doelen op stickK stijgen na tijdsmarkeringen (begin week, maand, jaar, na feestdagen en verjaardag) [PR]. Siraat: dag 1 tot 7 van de maand index 108 tot 109 tegen 94 tot 96 later in de maand; 1 tot 3 januari 2026 ruim twee keer de dagen voor Kerst; januari sterkste maand buiten Q4 [S, deels eigen kalender].
- **Wanneer het werkt.** Campagne (januari "non-toxic kitchen reset", begin van de maand), winback (nieuw jaar), welcome op maandag, anniversary-flow (één jaar met je pan).
- **Hoe Siraat het eerlijk inzet.** "New year, no coatings. Start with one pan." of "It's been a year since your first Siraat pan. Here's what to add next." Past bij de pijler "Non-toxic, for real" zonder angst.
- **Rode lijn.** Een "nieuw begin" koppelen aan schuld of angst over gezondheid ("Still poisoning your family in 2027?"), of nep-jubilea en verzonnen persoonlijke mijlpalen.
- **Meten.** RPR van campagnes op de 1e tot 3e tegenover midden van de maand (zelfde type mail), januari tegen december.

### Kaart 18. Pijn van betalen en BNPL

- **Wat het is.** Betalen doet psychologisch pijn, en die pijn remt de aankoop. Hoe verder het betalen van het moment van kopen af staat (creditcard, termijnen), hoe minder pijn en hoe meer mensen uitgeven.
- **Bewijs.** Prelec en Loewenstein (1998, "The red and the black") en Prelec en Simester (2001): betalingsbereidheid met creditcard tot twee keer hoger dan met contant geld in een veilingexperiment [PR]. Di Maggio, Katz en Williams (2022, NBER 30508): toegang tot BNPL verhoogt totale uitgaven (rond $60 per week), ook bij mensen zonder liquiditeitsprobleem; bij lage inkomens meer roodstand [PR, werkdocument]. Adobe: BNPL $20 mrd in de feestdagen 2025, meer dan $1 mrd op Cyber Monday, 82% via mobiel [IND]. Siraat: Shop Pay Installments en Affirm in de US; geen BNPL buiten de US; checkouts boven $349 26 tot 37% onbetaald [S].
- **Wanneer het werkt.** Cart en checkout boven $349 (6- en 12-delige set), PDP, campagne voor sets.
- **Hoe Siraat het eerlijk inzet.** Neutraal en volledig: "Or 4 interest-free payments of $87.25 with Shop Pay." (alleen US, alleen na akkoord op de claim, besluit 7 okt). Niet als hoofdboodschap, wel als regel onder de prijs bij sets.
- **Rode lijn.** BNPL als reden om te kopen wat je niet kunt betalen ("Can't afford it? Pay later!"), rente of voorwaarden verzwijgen, termijnbedrag groter tonen dan de totaalprijs. Niet richten op segmenten met betalingsproblemen. CFPB ziet BNPL als krediet (US) [wet].
- **Meten.** Betaalratio van checkouts boven $349 voor en na de termijnregel; chargebacks en mislukte termijnbetalingen.

---

## 3. Koopmomentenkaart: de reis, de kans en de boodschap

Volgorde van de reis voor een typische Siraat-koper: advertentie (Meta/TikTok, mobiel) naar PDP, pop-up, welcome, browse/cart/checkout, aankoop, post-purchase, en later winback of campagne. "Kans" = hoe waarschijnlijk iemand op dit moment koopt, op basis van eigen data waar die er is.

| Moment | Kans | Wat er in het hoofd gebeurt | Hefbomen die passen | Boodschap die past (voorbeeld) | Wat niet past |
|---|---|---|---|---|---|
| **Eerste sessie op de PDP** (mobiel, uit in-app browser) | Laag per sessie, maar de grootste stroom. ATC mediaan 1:35; na 30 s nog 39% aanwezig [S] | "Is dit echt, wat kost het, past het?" | Autoriteit (labtest), social proof, anker, free (gifts) | Prijs met echte compare-at, "Tested by Light Labs, report 25895", 4,x-sterrenscore | Nep-timer, "93% sold", pop-up binnen 2 s |
| **Pop-up en de eerste 10 minuten** | Zeer hoog: 60% van de pop-upkopers koopt binnen 10 min, 90% binnen 24 u [S] | Net ja gezegd (commitment), nog warm | Commitment, free, eenvoud (één keuze) | "Unlocked: your Black Friday price" plus code en auto-apply-link; één knop terug naar de pan | Lange uitleg, vijf producten, "you won" |
| **W1 (binnen minuten)** | Hoog: $3,09 per ontvanger, 73% van de welcome-omzet [S] | "Waar was ik? O ja, die pan." | Endowment (je prijs staat klaar), present bias, eenvoud | Kort, aanbod in de eerste regel, productkaarten met prijs (BF-W1-model) | Oprichtersverhaal als opening |
| **Welcome W2 tot W5 (dag 1 tot 10)** | Laag: samen $0,32 per ontvanger [S] | Twijfel: prijs, gezondheid, maat | Autoriteit, social proof, spijt wegnemen, keuze vereenvoudigen, wederkerigheid | Benjamin-brief met één pan, bon "what 70% off gets you", maatkiezer, verhalen | Dezelfde deadline elke dag |
| **Browse (bekeken, niet in cart)** | Middel | "Interessant, later misschien" | Commitment (wat je bekeek), social proof, present bias | "You looked at the Wok. Here's what owners say after a month." | Nep-schaarste |
| **Cart (in cart, niet afgerekend)** | Hoog | Bijna, maar iets houdt tegen (prijs, verzending, twijfel) | Endowment, spijt wegnemen, goal-gradient (tier), free | "Return to my cart" met eigen product; friction reducer; gifts als één regel | Afleiden met andere producten bovenaan |
| **Checkout (begonnen)** | Hoogste: C1 $7,96 tot $10,21 per ontvanger [S] | Laatste drempel: betalen, vertrouwen | Pijn van betalen (BNPL-regel), spijt wegnemen, deadline als de code echt verloopt | "Complete my order", "One use, already applied. 30-day returns." | "Your order is pending" |
| **Aankoop en post-purchase** | Laag voor nu, hoog voor de toekomst | Bevestiging zoeken ("goede keus?") | Wederkerigheid, endowment, consistentie, goal-gradient (tegoed) | Eerst "how to preheat", dan review, dan het deksel dat past, tegoed op naam | Direct cross-sell in mail 1 |
| **Winback (60 tot 180 dagen stil)** | Laag | Vergeten of tevreden zonder meer | Fresh start, mental accounting (tegoed), wederkerigheid | Founder-note, "Your $22 credit is still here", nieuwjaar | "We miss you" plus nep-deadline |
| **Campagne, start van een actie** | Middel, piek in de eerste ochtend [S] | "Wat is er nieuw?" | Free, anker, social proof, deadline (aankondigen) | 08:30 lokaal, "The Black Friday price is live. Here's what's in it." | Vijf boodschappen tegelijk |
| **Campagne, de vijf dagen ervoor tot Black Friday** | Opbouwend: week 3 en 22 tot 26 nov samen 43% van de maand in 2025 [S] | Vergelijken, wachten op "de echte deal" | Spijt van niet kopen (eerlijk), social proof, autoriteit | "Same price as Black Friday. Order now and it arrives before Thanksgiving." (alleen als waar) | Beloven dat het op BF niet goedkoper wordt als dat onzeker is |
| **Thanksgiving-avond en Black Friday** | Hoogste dag (BF 10% van de maand); BF piek 17:00 ET, Thanksgiving 21:00 ET [S] | Iedereen koopt, veel ruis | Eenvoud, social proof, free | Korte mail, één aanbod, voor de middag binnen; Thanksgiving een avondbrief van Benjamin | Tien mails op één dag |
| **Zondag in het Cyber-weekend** | Dal (666 orders in 2025) [S] | Moe van de sale | Wederkerigheid, rust | Hooguit een resend of niets | Extra druk |
| **Laatste 24 uur (30 nov)** | Hoog: 62 tot 74% van de orders van deadlinemails binnen 24 u [S]; Adobe Cyber Monday piek 20:00 tot 22:00 [IND] | "Nu of nooit" (als het echt is) | Deadline, verliesaversie, spijt van niet kopen, eenvoud | Hoofdmail 's ochtends, LAST-HOURS-brief 20:00 lokaal, tijdzone in de tekst | Verlengen na "final hours" |
| **Na de deadline** | Laag | "Gemist" | Eerlijkheid (consistentie) | Niets, of pas in december een nieuw, ander aanbod | "Extended by popular demand" |
| **Begin van de maand en januari** | Hoger: dag 1 tot 7 index 108 tot 109; januari sterk [S] | Nieuw begin, loon binnen | Fresh start, present bias | "New year, no coatings" op 1 tot 3 jan, maandcampagnes rond de 1e | Schuld of angst |

### Dagdeel- en weekdagregels (uit eigen data)

- **Hoofdmail 08:30 lokaal** (zondag 09:00): ligt vóór de ochtendpiek van 09:00 tot 12:00 [S].
- **Tweede contact op een ander uur** (13:00 of 14:00 resend aan niet-openers): de brief van 13:07 ET verkocht 40% binnen 6 uur [S].
- **Avondbrief alleen bij een echte deadline** (17:00, op 30 nov 20:00): op gewone dagen is de avond 23% en zakt het na 22:00 [S].
- **Weekend is koopdag, maandag niet**: deadlines die zondag 23:59 eindigen pakken de twee sterkste dagen [S].
- **Feestdagen zijn anders**: op Thanksgiving en Black Friday ligt de piek later (17:00 tot 21:00 ET) [S]; Adobe ziet de piek op Cyber Monday 20:00 tot 22:00 [IND].
- **Hoeveel contacten vóór een aankoop?** Geen betrouwbare publieke data; de "rule of 7" is een vuistregel [A]. Eigen data zegt: het eerste contact na een signaal (pop-up, cart, checkout) is veruit het meest waard, en daarna nog 60 tot 70% erbij uit vervolgmails in cart en checkout (`research/potentie/02-bottom-up.md`) [S]. Vuistregel voor de sprint: maximaal 1 sprintmail per dag, maximaal 3 mails per persoon per dag (4 vanaf 27 nov), zoals in de kalender.

### Markt- en apparaatcontext [IND]

- Adobe, US online feestdagen 2025 (1 nov tot 31 dec): $257,8 mrd, mobiel 56,4% van de omzet; Cyber Monday $14,25 mrd, mobiel 57,5%; Cyber Week $44,2 mrd [IND].
- Shopify BFCM 2025: $14,6 mrd (+27%), piek $5,1 mln per minuut om 12:01 ET op Black Friday, 32% van de orders via Shop Pay [IND].
- Klaviyo BFCM 2025: $3,8 mrd toegeschreven (5 dagen attributievenster), e-mail en sms samen 42% van de omzet van klanten, 43% op piekdagen [IND, eigen attributie].
- Omnisend 2025: bij kleine e-commercemerken 15% meer orders op Black Friday dan op Cyber Monday; 42% van de merken deed het beter op Cyber Monday [IND].
- Klaviyo zegt zelf dat historische "beste verzenddag"-tabellen geen goede gids zijn; test op je eigen lijst [IND]. Wij doen dat met eigen orderdata.

---

## 4. Waar de lijn ligt (samenvatting voor het team)

De volledige catalogus staat in `../black-hat/black-hat-referentie.md`. Vier toetsen, in deze volgorde:

1. **Is het waar in de backend?** Deadline, voorraad, prijs, compare-at, tegoed, gift, review. Zo niet: niet gebruiken. Geen asterisk nodig is de norm (PLAYBOOK 1).
2. **Zou de klant zich bedrogen voelen als hij alles wist?** Als het antwoord ja is, is het manipulatie, ook als het technisch klopt (bijvoorbeeld een "48-hour code" die in Shopify een jaar geldig is).
3. **Werkt het alleen omdat de klant iets niet weet?** Eerlijke overtuiging helpt een beslissing die de klant zelf ook zou nemen met alle informatie; manipulatie werkt juist door informatie weg te houden.
4. **Is het vaker dan het echte moment?** Elke dag "last chance" leert de lijst de deadline te negeren. Eén echt einde per mechaniek.

Wat nu eerst moet (uit black-hat sectie 3): de resettende timer, de hardgecodeerde "93% sold"-balk en "quantities are limited" van de site halen. Zolang die staan, verzwakken ze elke echte deadline in onze mails.

---

## 5. Meetplan in één tabel

| Hefboom | Primaire maat | Vangrail | Wanneer testen |
|---|---|---|---|
| Deadline | Orders binnen 24 u, RPR | Uitschrijf onder 0,5%, klachten onder 0,1%, verkoop zakt na deadline | Elke deadlinemail (meten, niet testen in BF) |
| Korte termijn | Verzilvering codes en tegoed | Marge per order | Januari: 14 tegen 30 dagen |
| Verliesaversie | Unieke kliks, RPR | Uitschrijf | Onderwerpregel A/B in flows |
| Free effect | RPR, AOV | Marge | Gifts tegen extra 10% (zelfde kosten), december |
| Social proof | CR per sessie, klik | Reviewklachten | Reviewset A/B in welcome W3 |
| Autoriteit | Klik op labrapport, RPR | Tickets "is it safe" | Bewijsblok in browse B1 |
| Goal-gradient | Tijd tot tweede order, AOV rond drempels | Tegoedkosten | Rise na BF |
| Mental accounting | Verzilvering, incrementele omzet | Holdout 10% | CREDIT en C-X-flow |
| Keuze-overload | CR per mail, klikverdeling | AOV | 1 tegen 3 productkaarten in cart |
| BNPL | Betaalratio checkouts boven $349 | Chargebacks, mislukte termijnen | Termijnregel in cart en C1 (US) |
| Fresh start | RPR dag 1 tot 3 tegen midden van de maand | Uitschrijf | Januari-campagnes |
| Timing | Orders per uur na verzending | Ontvangers per dag (max 3) | Resend-tijd 13:00 tegen 14:00 |

Regels uit PLAYBOOK 6 gelden: één variabele per test, winnaar op unieke kliks of omzet, nooit op opens, minimaal vier weken in flows, geen automatische winnaar. BF vertekent gedrag; herhaal winnaars in januari.

---

## 6. Spiekbrief voor het team (één pagina)

**De drie vragen bij elke regel:** Is het waar in de backend? Zou de klant zich bedrogen voelen als hij alles wist? Is dit het echte moment of de zoveelste "laatste kans"?

**Per moment de hoofdhefboom:**

| Moment | Hoofdhefboom | Eén regel |
|---|---|---|
| Pop-up | Eenvoud + free | "Unlocked: your Black Friday price." Code zichtbaar, één knop. |
| W1 (minuten) | Present bias + endowment | Aanbod in de eerste regel, productkaarten met prijs. Snel, kort. |
| Welcome W2 tot W5 | Autoriteit + social proof | Benjamin, Light Labs rapport 25895, echte reviews, één pan aanbevolen. |
| Browse | Commitment + social proof | "You looked at the Wok. Here's what owners say." |
| Cart | Endowment + spijt wegnemen | Eigen product, "Return to my cart", "Free shipping. 30-day returns." |
| Checkout | Pijn van betalen + spijt wegnemen | "Complete my order", termijnregel bij $349+ (US). |
| Post-purchase | Wederkerigheid | Eerst kookadvies, dan review, dan het passende deksel. |
| Winback | Fresh start + tegoed | Founder-note, echt tegoed op naam, nieuwjaar. |
| Campagne start | Free + anker | Gifts met echte waarde, echte compare-at. |
| Laatste 24 uur | Deadline + verliesaversie | Echte eindtijd met tijdzone, ochtendmail plus avondbrief. |

**Timing:**
- Hoofdmail 08:30 lokaal; resend 13:00 of 14:00; avondbrief alleen bij een echte deadline (17:00, op 30 nov 20:00).
- Zaterdag en zondag kopen het meest; maandag het minst. Dag 1 tot 7 van de maand beter dan de rest.
- Vorig jaar: een derde van november in de Cyber 5, Black Friday 10%, zondag van het Cyber-weekend het dal. De weken ervoor groeien elke week; niet alles opsparen voor Black Friday.
- Max 1 sprintmail per dag, max 3 mails per persoon per dag (4 vanaf 27 nov).

**Woorden die mogen (als het waar is):** "Ends tonight at 11:59 PM PT", "Your $22 store credit expires Sunday", "4 gifts with every order", "Tested by Light Labs, report 25895", "30-day returns", "75-year warranty", "100,000+ happy customers", "with a pure titanium cooking surface, no coatings".

**Woorden die nooit mogen:** "only 3 left" zonder voorraaddata, "93% sold", "selling fast", "no extensions" (en dan verlengen), "your order is pending", "price held for you", "next batch", "reserved", "lifetime", "100-day trial", "free filter", "doctor recommended", "you won", een compare-at die nooit gold, een review die niet letterlijk van Trustpilot komt.

**Meten:** unieke kliks en omzet per ontvanger, nooit opens. Vangrails: uitschrijf onder 0,5%, spamklachten onder 0,1%, retour en chargebacks niet omhoog.

---

## 7. Bronnen

Peer-reviewed en werkdocumenten:
- Kahneman, D., en Tversky, A. (1979). Prospect theory. Econometrica 47(2). Tversky en Kahneman (1991), Loss aversion in riskless choice, QJE 106(4).
- Brown, A., Imai, T., Vieider, F., en Camerer, C. (2024). Meta-analysis of empirical estimates of loss aversion. Journal of Economic Literature 62(2).
- Gal, D., en Rucker, D. (2018). The loss of loss aversion. Journal of Consumer Psychology 28(3).
- Kahneman, D., Knetsch, J., en Thaler, R. (1990). Experimental tests of the endowment effect. Journal of Political Economy 98(6). List, J. (2003), QJE 118(1).
- [Inman, J. J., en McAlister, L. (1994). Do coupon expiration dates affect consumer behavior? Journal of Marketing Research 31(3), 423 tot 428.](https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/1072225)
- [Krishna, A., en Zhang, Z. J. (1999). Short- or long-duration coupons. Management Science 45(8).](https://pubsonline.informs.org/doi/references/10.1287/mnsc.45.8.1041)
- [Shu, S., en Gneezy, A. (2010). Procrastination of enjoyable experiences. Journal of Marketing Research 47(5), 933 tot 944.](https://rady.ucsd.edu/faculty-research/faculty/ayelet-gneezy.html)
- Worchel, S., Lee, J., en Adewole, A. (1975). Effects of supply and demand on ratings of object value. JPSP 32(5). Lynn, M. (1991), Scarcity effects on value: a quantitative review, Psychology and Marketing 8(1).
- Mathur, A., e.a. (2019). Dark patterns at scale. Proceedings of the ACM on HCI (CSCW).
- [Kivetz, R., Urminsky, O., en Zheng, Y. (2006). The goal-gradient hypothesis resurrected. Journal of Marketing Research 43(1), 39 tot 58.](https://business.columbia.edu/faculty/research/goal-gradient-hypothesis-resurrected-purchase-acceleration-illusionary-goal) Nunes, J., en Drèze, X. (2006), The endowed progress effect, JCR 32(4).
- Thaler, R. (1985). Mental accounting and consumer choice. Marketing Science 4(3); (1999) JBDM 12(3). Arkes, H., e.a. (1994), The psychology of windfall gains, OBHDP 59(3).
- [Helion, C., en Gilovich, T. (2014). Gift cards and mental accounting: green-lighting hedonic spending. Journal of Behavioral Decision Making 27(4), 386 tot 393.](https://econbiz.de/Record/gift-cards-and-mental-accounting-green-lighting-hedonic-spending-helion-chelsea/10010517801)
- Tversky, A., en Kahneman, D. (1974). Judgment under uncertainty. Science 185. Ariely, D., Loewenstein, G., en Prelec, D. (2003), Coherent arbitrariness, QJE 118(1). Compeau, L., en Grewal, D. (1998), Comparative price advertising: an integrative review, Journal of Public Policy and Marketing 17(2).
- [Shampanier, K., Mazar, N., en Ariely, D. (2007). Zero as a special price. Marketing Science 26(6), 742 tot 757.](https://people.duke.edu/~dandan/webfiles/PapersPI/Zero%20as%20a%20Special%20Price.pdf)
- [Goldstein, N., Cialdini, R., en Griskevicius, V. (2008). A room with a viewpoint. Journal of Consumer Research 35(3), 472 tot 482.](https://acawiki.org/A_Room_with_a_Viewpoint:_Using_Social_Norms_to_Motivate_Environmental_Conservation_in_Hotels)
- [Schindler, R., en Yalch, R. (2006). It seems factual, but is it? Effects of using sharp versus round numbers in advertising claims. Advances in Consumer Research 33.](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_journals_195849757/Details)
- Dulleck, U., en Kerschbamer, R. (2006). On doctors, mechanics, and computer specialists: the economics of credence goods. Journal of Economic Literature 44(1).
- Iyengar, S., en Lepper, M. (2000). When choice is demotivating. JPSP 79(6).
- [Scheibehenne, B., Greifeneder, R., en Todd, P. (2010). Can there ever be too many options? Journal of Consumer Research 37(3), 409 tot 425.](https://ideas.repec.org/a/oup/jconrs/v37y2010i3p409-425.html) Chernev, A., Böckenholt, U., en Goodman, J. (2015), Choice overload: a conceptual review and meta-analysis, Journal of Consumer Psychology 25(2).
- Freedman, J., en Fraser, S. (1966). Compliance without pressure. JPSP 4(2). Burger, J. (1999), The foot-in-the-door compliance procedure: a multiple-process analysis and review, PSPR 3(4).
- Regan, D. (1971). Effects of a favor and liking on compliance. JESP 7(6). Strohmetz, D., e.a. (2002), Sweetening the till, Journal of Applied Social Psychology 32(2). Gneezy, U., en List, J. (2006), Putting behavioral economics to work, Econometrica 74(5).
- Laibson, D. (1997). Golden eggs and hyperbolic discounting. QJE 112(2). O'Donoghue, T., en Rabin, M. (1999), Doing it now or later, AER 89(1).
- [Gelman, M., Kariv, S., Shapiro, M., Silverman, D., en Tadelis, S. (2014). Harnessing naturally occurring data to measure the response of spending to income. Science 345(6193), 212 tot 215.](https://escholarship.org/content/qt2mh786jw/qt2mh786jw.pdf)
- Simonson, I. (1992). The influence of anticipating regret and responsibility on purchase decisions. JCR 19(1). Janakiraman, N., Syrdal, H., en Freling, R. (2016), The effect of return policy leniency on consumer purchase and return decisions: a meta-analytic review, Journal of Retailing 92(2).
- [Dai, H., Milkman, K., en Riis, J. (2014). The fresh start effect. Management Science 60(10), 2563 tot 2582.](https://knowledge.wharton.upenn.edu/article/need-fresh-start-heres-begin/)
- Prelec, D., en Loewenstein, G. (1998). The red and the black. Marketing Science 17(1). Prelec, D., en Simester, D. (2001), Always leave home without it, Marketing Letters 12(1).
- [Di Maggio, M., Katz, J., en Williams, E. (2022). Buy now, pay later credit: user characteristics and effects on spending patterns. NBER Working Paper 30508.](https://www.nber.org/papers/w30508)

Industrie (grote steekproef) en vendor:
- [Adobe, 2025 holiday shopping recap (feestdagen, mobiel, BNPL).](https://business.adobe.com/assets/pdfs/resources/sdk/adobe-holiday-shopping-recap/2025-holiday-shopping-recap.pdf)
- [Adobe, Cyber Monday 2025: $14,25 mrd, piek 20:00 tot 22:00.](https://news.adobe.com/news/2025/12/adobe-cyber-monday-hits-record)
- [Shopify, BFCM 2025: $14,6 mrd, piek 12:01 ET.](https://www.shopify.com/news/bfcm-data-2025)
- [Klaviyo, BFCM 2025 recap (persbericht).](https://www.businesswire.com/news/home/20251202774732/en)
- [Omnisend, Black Friday tegenover Cyber Monday bij kleine merken (2025).](https://www.omnisend.com/latest-news/58-of-smb-ecommerce-brands-saw-black-friday-outperform-cyber-monday/)
- [Klaviyo, best day to send emails (2023-campagnes, per branche).](https://www.klaviyo.com/blog/best-day-to-send-emails)
- [Spiegel Research Center (2017), How online reviews influence sales.](https://spiegel.medill.northwestern.edu/How-Online-Reviews-Influence-Sales)

Intern: `../black-hat/black-hat-referentie.md`, `../scheduling/kalender.md`, `../flows-ontwerp/flows-ontwerp.md`, `../BRIEF.md`, `research/smooche/00-plan.md`, `research/popup/2026-11-trigger-test.md`, `research/plannen/2026-11-welcome-audit.md`, `research/plannen/2026-11-punten-store-credit.md`, `research/cro/01-funnel.md`, `research/potentie/02-bottom-up.md`, `PLAYBOOK.md`, `DECISIONS.md`.

Niet opnieuw geverifieerd in deze sessie (achtergrondkennis, betrouwbaar maar zonder eigen check van het volledige artikel): de exacte percentages van Regan, Strohmetz, Iyengar en Lepper, Prelec en Simester, en de meta-analyses van Brown e.a., Burger, Lynn, Compeau en Grewal en Janakiraman e.a. Gebruik in klantcopy nooit een wetenschappelijk cijfer; dit stuk is voor het team.
