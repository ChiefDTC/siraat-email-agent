# Quiz-popup: meten en A/B-test (rol: meet- en testanalist, 8 nov 2026)

Bron: BRIEF.md in deze map, research/popup/2026-11-trigger-test.md, research/lijstkwaliteit/01-giveaway-instroom.md, research/lijst/01-cohorten.md. Live data alleen gelezen: Klaviyo (profielen, metrics, formulieren, Subscribed to List `SCvkku`), Shopify ShopifyQL (sessions, sales). Geen klantdata overgenomen, alleen namen van eigenschappen en totalen. Niets gewijzigd in Klaviyo, Alia of Shopify.

## 1. Samenvatting

- **Primaire maat:** omzet binnen 14 dagen per toegewezen bezoeker (per popupweergave), over alle orders van aanmelders uit die arm, niet alleen e-mail-toegeschreven. Bevestiging op 30 dagen. Aanmeldingen per bezoeker is de belangrijkste vangrail, niet het doel.
- **Duur:** 21 dagen bij 50/50 (MDE circa 12 tot 15% op de primaire maat), daarna 14 dagen wachten tot het laatste cohort rijp is. Start na de trigger-test en na de BFCM-piek: **2 december**, eerste besluit rond 6 januari, bevestiging in januari met een holdout.
- **Eigenschap:** `siraat_goal` met vaste codes (`non_toxic`, `performance`, `replace_coating`, `gift`, `other`), plus `siraat_goal_first`, `siraat_goal_at`, `siraat_goal_source`. Terugval: aparte Klaviyo-lijst per antwoord met een flow die de eigenschap zet.
- **Trigger-test:** opeenvolgend, niet factorieel. Trigger-test eerst afmaken, winnaar bevriezen, quiztest draait op die trigger in beide armen.

## 2. Wat Alia nu al naar Klaviyo schrijft (gecontroleerd 8 nov, 40 nieuwste profielen)

| Eigenschap | Wat erin staat (waarden, geen klantdata) | Bruikbaar voor |
| --- | --- | --- |
| `$source` | "Alia sign-up" (ook -50 en -9 via Shopify-sync) | Herkomst pop-up |
| `alia_popup_name` | "Card Game 0 SEC", "Card Game 10 SEC", "Card Game 20 SEC" | **Variant per arm**. Bevestigt dat de trigger-test live is |
| `alia_popup` | Zelfde waarden als `alia_popup_name` | Dubbel, idem |
| `alia_flow_name` | Zelfde waarden, soms leeg | Idem |
| `alia_campaign` | "US \| Evergreen 10 SEC" bij alle drie de varianten | **Niet** gebruiken als variant: de naam zegt 10 SEC maar staat ook bij 0 en 20 |
| `user_id` | Getal (Alia-ID) | Koppeling met Alia-export |
| `$consent`, `$consent_timestamp`, `Accepts Marketing`, `$sms_consent_method` | Toestemming | Niet voor de test |
| `alia_offer` | Niet meer gezien in de steekproef (was er in oktober wel) | Niet op rekenen |

Overige bevindingen:
- Event `Alia Reward Claimed` (`TBeZmH`) bestaat, met eigenschappen `shopify_code` en `text`. Laatste event 12 sep 2026: Alia kan dus events met eigen eigenschappen naar Klaviyo sturen, maar doet dat nu niet.
- Geen enkel Klaviyo-formulier staat live (0 live formulieren). `query_form_values` en `query_form_series` leveren voor de pop-up dus niets op: alle trechterdata (weergave, stap, verzending) komt uit Alia.
- `Survey Answer - Triple Pixel` (`StqVtw`) heeft één event uit okt 2025. De post-purchase survey komt dus niet in Klaviyo binnen; validatie op persoonsniveau moet via een export van de surveytool (zie 8).
- Alia overschrijft `alia_*` bij elke nieuwe interactie (research/lijst/01-cohorten.md). Daarom een eigen eigenschap die de eerste keuze vasthoudt.

## 3. Datavastlegging: hoe het antwoord op het profiel komt

### 3.1 Eigenschappen (voorstel)

| Eigenschap | Type | Waarde | Regel |
| --- | --- | --- | --- |
| `siraat_goal` | tekst | `non_toxic`, `performance`, `replace_coating`, `gift`, `other` | Laatste antwoord. Alleen deze codes, kleine letters, nooit de knoptekst |
| `siraat_goal_first` | tekst | Zelfde codes | Eerste antwoord, wordt nooit overschreven (flow zet hem alleen als hij leeg is) |
| `siraat_goal_at` | datum | Tijdstip van antwoord | Voor rijping van cohorten en voor de race met de welkomflow |
| `siraat_goal_source` | tekst | `alia_quiz_v1` (ophogen bij elke tekstwijziging van de vraag) | Zo blijven verdelingen per versie vergelijkbaar |
| `siraat_goal_label` | tekst | De getoonde knoptekst | Alleen ter controle, nooit in segmenten |

Koppeling codes aan de angles uit de brief (definitieve tekst volgt van de copyrol):
- `non_toxic`: "Ditch the toxins from my home" (PFAS, toxiciteit; survey ~70%).
- `performance`: "Better performance from my cookware" (non-stick die echt werkt, eieren, steak).
- `replace_coating`: "My old pan is peeling" (pijnpunt 41% in de survey). Optioneel; als er maar 4 knoppen komen, opgaan in `performance`.
- `gift`: "It's a gift" (survey ~1 op 5).
- `other`: "Just browsing" of "Something else". Houdt de andere antwoorden zuiver; zonder deze optie kiezen twijfelaars de bovenste knop.

Volgorde van de knoppen: als Alia het toestaat, willekeurig per bezoeker (behalve `other` altijd onderaan). Anders vaste volgorde en dat noteren, want de bovenste optie krijgt extra keuzes (zie 8).

Controlearm: `siraat_goal` blijft leeg. De arm herken je aan `alia_popup_name`.

### 3.2 Terugval als Alia de eigenschap niet kan schrijven (in volgorde van voorkeur)

1. **Verborgen veld of custom property in het Alia-formulier** per tak (vaste waarde per antwoordknop). Bij Alia navragen of een antwoordknop een eigenschap meegeeft aan de Klaviyo-sync. Dit is de schoonste route.
2. **Lijst per antwoord.** Elke tak synct naar een eigen lijst ("Quiz · non_toxic" enz.) naast of in plaats van `Uw8eZG`. Een kleine Klaviyo-flow per lijst zet met "Update profile property" `siraat_goal`, `siraat_goal_at` en (als leeg) `siraat_goal_first`. Let op: de welkomflow triggert nu op `Uw8eZG`. Als Alia per tak een andere lijst gebruikt, moet ook `Uw8eZG` gevuld blijven of moet de welkomtrigger mee. Altijd ook op `Uw8eZG`, anders verandert de instroom van alle bestaande flows.
3. **Event.** Alia stuurt al events (`Alia Reward Claimed` met `text`). Per tak een andere "reward"-tekst of een eigen event "Quiz Answered" met eigenschap `goal`. Een flow op dat event zet de profieleigenschap. Voordeel: datum en versie komen gratis mee.
4. **URL als noodgreep.** De knop na het antwoord linkt naar een landingspagina met `?goal=non_toxic`; Active on Site legt de URL vast. Minder betrouwbaar (37% van de sessies is in-app prefetch, links worden niet altijd gevolgd). Alleen als 1 tot 3 niet kunnen.

### 3.3 Controles voor livegang

- Testprofielen (adres met `test@`, staat al uitgesloten in de welkomflow) door elke tak laten lopen: komt de juiste code binnen, binnen hoeveel seconden na Subscribed to List?
- **Race met de welkomflow.** De welkom wacht nu 5 minuten. Als de eigenschap later binnenkomt dan de lijstinschrijving, valt een quiz-aanmelder in het standaardpad. Meet de vertraging; houd de wachttijd ruim boven het 99e percentiel.
- **Vangnet:** een tak "geen `siraat_goal`" in de welkom blijft gewoon de huidige welkom (`T4a5Mk`). Zo kost een mislukte vastlegging nooit een mail.
- **Vastlegratio** (aanmelders in quizarm met `siraat_goal` gevuld) is een dagelijkse controle. Onder 95%: uitzoeken; onder 90%: test pauzeren, want dan is de vergelijking per angle scheef.

## 4. Testopzet

### 4.1 Armen

| | Controle | Quiz |
| --- | --- | --- |
| Pop-up | Huidige pop-up (Card Game) met de winnende trigger uit de trigger-test | Vraag "What is your main goal?", daarna aanbod en tekst per antwoord, daarna e-mail en SMS |
| Aanbod | Huidig (5 gifts, free shipping, kans op PFAS-waterfilter US) | Exact hetzelfde aanbod; alleen de verpakking en de tekst verschillen |
| Trigger, uitsluitingen, herhaling | Gelijk: winnaar trigger-test, niet op cart/checkout/account/bedankpagina, niet voor bekende abonnees en utm_medium=email of sms, opnieuw na 7 dagen | Gelijk |
| Welkomflow | Huidige welkom | Welkom per angle |
| Verdeling | 50% | 50% |

In Alia: handmatige verdeling 50/50, Smart Testing uit, Smart Trigger in beide armen gelijk. Bezoeker blijft in zijn arm (cookie), ook bij een volgende sessie.

Belangrijk: als het aanbod in de quizarm anders wordt (ander percentage, andere gift), test je twee dingen tegelijk. Dan weet je niet of de vraag of het aanbod wint. Aanbod gelijk houden.

Let op: de quizarm test **twee onderdelen samen**, de quiz-pop-up en de welkom per angle. Dat is bewust (de vraag is of het geheel meer oplevert), maar daardoor kun je het effect niet aan één onderdeel toeschrijven. Wil je dat later weten: in fase 2 binnen de quizarm 50/50 welkom per angle tegen de huidige welkom.

### 4.2 Primaire maat

**Omzet binnen 14 dagen per toegewezen bezoeker** = som van alle Placed Order-omzet (`RSNxYV`, alle kanalen, niet alleen toegeschreven) van aanmelders uit de arm, binnen 14 dagen na aanmelding, gedeeld door het aantal popupweergaven (unieke bezoekers met weergave) in die arm.

Waarom deze maat:
- Aanmeldratio alleen is misleidend: de quiz kan minder aanmelders opleveren die meer kopen, of meer aanmelders van lagere kwaliteit. Omzet per aanmelder alleen is ook misleidend: als de quiz minder (maar warmere) aanmelders oplevert, stijgt die maat vanzelf. Per bezoeker vangt beide effecten.
- Weergaven zijn een eerlijke noemer, omdat de trigger in beide armen gelijk is. (In de trigger-test kon dat niet, daar verschilt het aantal weergaven per arm.)
- 14 dagen omdat 21% van de aanmelders binnen 24 uur koopt en 60% van de pop-upkopers binnen 10 minuten: het grootste deel van de omzet zit vooraan. 30 dagen als bevestiging.
- Alle orders, niet flow-toegeschreven: in de sale neemt BF-W1 (`Rn556d`) de welkom over, en campagnes en direct verkeer tellen ook.

Beperking: omzet van bezoekers die de pop-up zien, sluiten en toch kopen, valt buiten Klaviyo. Vraag Alia of hun rapport omzet per variant over alle bezoekers geeft (inclusief niet-aanmelders). Zo ja: dat wordt een tweede primaire controle. Zo nee: sitebrede conversie per dag als vangrail (zie 4.4).

Uitschieters: orders boven het 99e percentiel (circa $1.000, controleren) afkappen op die grens, vooraf vastgelegd. Eén grote set kan anders een arm laten winnen.

### 4.3 Secundaire maten

| Maat | Definitie | Bron |
| --- | --- | --- |
| Aanmeldingen per bezoeker | E-mailaanmeldingen / weergaven per arm | Alia (variant), Klaviyo `alia_popup_name` |
| SMS-aanmeldingen per bezoeker | Idem voor SMS | Alia, SMS List |
| Stapuitval | Quiz: weergave, antwoord, e-mail, SMS, succes. Controle: weergave, e-mail, SMS, succes | Alia stapstatistiek |
| Omzet per aanmelder 14 en 30 dagen | Per arm en per angle | Klaviyo segmenten (zie 6) |
| Koopratio 24 uur, 14 en 30 dagen | Per arm en per angle | Idem |
| AOV per angle | Omzet / orders binnen 30 dagen | Idem |
| Welkomflow-omzet per ontvanger per angle | Flowrapport per tak | Klaviyo flow-values-report |
| Uitschrijving en spamklacht 30 dagen | Per arm en per angle | Klaviyo |
| Vastlegratio | Aandeel quizaanmelders met `siraat_goal` | Klaviyo |
| Verdeling angles | Aandeel per code | Klaviyo |

Per angle zijn de aantallen klein (een angle met 10% van de antwoorden levert in 21 dagen circa 1.500 aanmelders). Uitkomsten per angle zijn dus richtinggevend, met betrouwbaarheidsinterval, geen eigen beslissing.

### 4.4 Vangrails

- Aanmeldingen per bezoeker in de quizarm niet meer dan 10% lager dan controle (de quiz voegt een stap toe; dat is het grootste risico).
- Sitebrede conversie per dag (Shopify) niet afwijkend van de trend van de vorige week, gecorrigeerd voor campagnedagen.
- Uitschrijving en spam per arm niet hoger dan 1,25 keer controle.
- Verhouding weergaven tussen de armen tussen 49 en 51% (sample ratio mismatch). Daarbuiten is de verdeling kapot en zegt de test niets.

## 5. Powerberekening met echte cijfers

### 5.1 Basiscijfers (gelezen 8 nov)

| Cijfer | Waarde | Bron |
| --- | --- | --- |
| Sessies 1 t/m 7 nov | 206.218, circa 29.500 per dag (82% mobiel) | ShopifyQL sessions |
| Sessies week 2 t/m 7 nov | 170.644 (6 dagen); oktoberweken 94.000 tot 108.000 per 7 dagen | ShopifyQL |
| Nieuwe abonnees Email List 2 t/m 7 nov | 10.192, circa 1.700 per dag (oktober 5.000 tot 8.400 per week) | Klaviyo `SCvkku` |
| Aanmeldingen per sessie | 6,0% totaal, circa 5,3% via Alia (Alia ~88% van de aanmeldingen) | Afgeleid |
| Koopratio Alia-aanmelders binnen 30 dagen | 10,5 tot 12,1% | research/lijstkwaliteit/01-giveaway-instroom.md |
| Omzet per Alia-aanmelder binnen 30 dagen | $22,90 tot $24,63 | Idem |
| AOV | $229 tot $247 (oktober tot begin nov) | ShopifyQL sales |
| Klaviyo-formulieren live | 0 (formulierrapporten leeg) | Klaviyo get_forms |

Niet alle sessies doen mee: uitgesloten pagina's en verkeer uit e-mail en SMS vallen weg. Aanname: 80% telt mee, circa **23.600 sessies per dag, 11.800 per arm**. De verkeerscijfers van november zijn hoger dan oktober door de sale; december ligt vermoedelijk lager. Daarom dagen ruim plannen.

### 5.2 Primaire maat: omzet per bezoeker

Per bezoeker is de omzet bijna altijd $0 (5,3% meldt aan, daarvan koopt ~11%: 0,58% van de bezoekers koopt via de pop-up). Gemiddeld circa $1,22 per bezoeker (5,3% x $23), met spreiding circa $18,60 per bezoeker (aanname: bestedingsspreiding 0,6 keer het gemiddelde van circa $210 per koper). Formule: n per arm = 2 x (1,96 + 0,84)^2 x variantie / verschil^2 (tweezijdig 5%, power 80%).

| Te vinden verschil (relatief) | Bezoekers per arm | Dagen bij 11.800 per arm | Dagen bij 14.700 per arm (alle sessies) |
| --- | ---: | ---: | ---: |
| 10% | circa 365.000 | 31 | 25 |
| 15% | circa 162.000 | 14 | 11 |
| 20% | circa 91.000 | 8 | 6 |

### 5.3 Secundaire maten

| Maat | Basis | Te vinden verschil | Per arm nodig | Dagen |
| --- | --- | --- | ---: | ---: |
| Aanmeldingen per bezoeker | 5,3% | 10% relatief | circa 28.000 bezoekers | 3 |
| Aanmeldingen per bezoeker | 5,3% | 5% relatief | circa 112.000 bezoekers | 10 |
| Omzet per aanmelder 30 d | $23, koopratio 11% | 10% | circa 18.000 aanmelders | 24 (bij circa 750 aanmelders per arm per dag) |
| Omzet per aanmelder 30 d | idem | 15% | circa 8.000 aanmelders | 11 |

### 5.4 Advies duur

- **21 volle dagen**, altijd hele weken (weekdag-effect: za en zo liggen 13 tot 19% boven het jaargemiddelde, do 11% onder). Daarmee vind je een verschil van circa 12 tot 15% op omzet per bezoeker en ruim 5% op aanmeldingen.
- Is het verkeer in december lager dan 20.000 per dag: verlengen naar 28 dagen.
- Daarna **14 dagen wachten** tot het laatste cohort 14 dagen oud is. 30-dagenbevestiging 30 dagen na het einde.
- Kleinere verschillen dan 10% zijn met dit verkeer niet in redelijke tijd aan te tonen. Een quiz die maar 5% beter is, zie je niet; dan beslist de bijvangst (de angle-data, zie 7).
- Analyse: zoals de eerdere flowtests (research/flows-audit/2026-10-19-ab-tests.md) Bayesiaans, kans dat quiz beter is dan controle, plus het verschil met 90%-interval.

## 6. Timing rond BFCM

Kalender: VIP-sale loopt al, Thanksgiving 26 nov, Black Friday 27 nov, Cyber Monday 30 nov. In BFCM 2025 viel 33% van de novemberorders in Cyber 5.

Advies: **niet testen in de piek.**
- Gedrag in de piek is anders (koopt toch, "up to 70%" overstemt elke angle). Een winnaar uit de piek zegt weinig over januari.
- Risico: de pop-up levert 88% van de aanmeldingen en 60% van die kopers koopt binnen 10 minuten. Een quiz die 10% aanmeldingen kost, kost in de drukste week direct omzet.
- De trigger-test heeft het verkeer tot circa 21 nov nodig. Een tweede test ernaast steelt verkeer en maakt beide onzuiver.

Plan:

| Periode | Wat |
| --- | --- |
| 8 tot circa 21 nov | Trigger-test loopt (sinds circa 7 of 8 nov, in Alia de startdatum controleren). Quiz bouwen in Alia als concept, welkom per angle als concept, vastlegging testen met testprofielen en preview. Geen live verkeer naar de quiz |
| circa 21 nov | Trigger-winnaar kiezen, bevriezen tot na de quiztest |
| 22 nov tot 1 dec | Piek. Niets veranderen aan de pop-up |
| 2 dec tot 22 dec (of 29 dec) | Quiztest 50/50, 21 tot 28 dagen |
| tot circa 12 jan | Laatste cohort rijp (14 dagen), besluit |
| jan tot begin feb | Bij winst: quiz naar 90%, 10% holdout op de oude pop-up, 4 weken. Januari is de sterkste maand buiten Q4 en de eerlijkste meetlat |

Let op december: kerstcadeaus. Het aandeel `gift` zal hoger liggen dan de 1 op 5 uit de survey, en de verzendgrens voor kerst verandert het koopgedrag in de laatste week. Beide armen hebben daar evenveel last van, dus de vergelijking blijft eerlijk, maar de angleverdeling uit december is niet de verdeling van het jaar. Herhaal de verdelingscheck in januari.

Optie als Floris de quiz toch in BFCM wil: 10% van het verkeer naar de quiz vanaf het einde van de trigger-test, alleen om de vastlegging en de angleverdeling te leren, niet om te beslissen. Kost weinig, maar het blijft een wijziging in de piek; mijn advies is nee.

## 7. Samenhang met de trigger-test (A direct / B 10 s / C 20 s)

Advies: **opeenvolgend.**
- **Factorieel** (3 triggers x 2 pop-ups = 6 cellen van 16,7%) halveert het verkeer per cel ten opzichte van de quiztest en verdrievoudigt de looptijd: met circa 3.900 bezoekers per cel per dag is 15% op omzet per bezoeker pas na circa 40 dagen te zien. Bovendien loopt de trigger-test al; de quiz er middenin toevoegen maakt de eerste helft van de trigger-test anders dan de tweede.
- Er is wel een echte wisselwerking te verwachten: een quiz bij 20 s treft een warmere bezoeker dan een quiz bij paginalading. Dat is juist een reden om eerst de trigger vast te zetten en de quiz op die trigger te testen.
- De trigger-test meet op aanmeldingen per sessie; de quiztest op omzet per bezoeker. Andere vragen, dus ook daarom na elkaar.
- Variantnamen: de quizvariant krijgt een eigen naam in `alia_popup_name` (bijvoorbeeld "Quiz v1 20 SEC" naast "Card Game 20 SEC"), zodat oude en nieuwe tests in Klaviyo te scheiden zijn. `alia_campaign` niet gebruiken (staat nu op "US | Evergreen 10 SEC" bij alle drie de triggervarianten).
- Observatie vandaag: van 31 Alia-profielen in een half uur 17 op 0 SEC, 6 op 10 SEC, 8 op 20 SEC. Dat past bij de verwachting dat latere triggers minder weergaven krijgen. Te klein om iets uit af te leiden.

## 8. Rapportage

### 8.1 Segmenten (alleen voorstel, niets aangemaakt)

| Segment | Definitie |
| --- | --- |
| Quiztest · controle | `alia_popup_name` = naam controlevariant AND aangemeld (Subscribed to List `Uw8eZG`) sinds teststart |
| Quiztest · quiz | `alia_popup_name` = naam quizvariant AND aangemeld sinds teststart |
| Quiztest · quiz · {angle} (5x) | Quiz AND `siraat_goal_first` = code |
| Quiztest · quiz · geen antwoord | Quiz AND `siraat_goal` is not set (vastlegfout, moet bijna leeg zijn) |
| Angle · {code} (5x, blijvend) | `siraat_goal` = code, ongeacht test. Voor campagnes en ads |

Gebruik `siraat_goal_first` voor de testanalyse (vaste toewijzing) en `siraat_goal` voor campagnes (meest recente wens).

Omzet per cohort: per segment de Placed Order-events binnen 14 en 30 dagen na de aanmelddatum ophalen (API, segmentleden plus events per profiel, zoals in research/lijstkwaliteit/01-giveaway-instroom.md). Klaviyo-standaardrapporten geven alleen toegeschreven omzet; dat is niet de primaire maat.

Flowrapport: welkom per angle met per tak eigen berichtnamen ("W1 · non_toxic"), zodat het flow-values-report per tak omzet per ontvanger geeft.

### 8.2 Wekelijkse check (maandag, in de dagelijkse bewaking en in #claude-mail)

1. Verdeling weergaven 49 tot 51%? (Alia)
2. Vastlegratio boven 95%? Vertraging eigenschap tegen welkomwachttijd?
3. Aanmeldingen per bezoeker per arm, met interval.
4. Stapuitval quiz: weergave naar antwoord, antwoord naar e-mail.
5. Angleverdeling, vergeleken met de vorige week en met de survey.
6. Rijpe cohorten (14 dagen oud): omzet per bezoeker en per aanmelder per arm.
7. Uitschrijving en spam per arm en per angle.
8. Sitebrede conversie en bijzonderheden (campagnedagen, storingen, Alia-wijzigingen).

Tussentijdse cijfers zijn voor bewaking, niet om de test vroeg af te ronden.

### 8.3 Beslisregels (vooraf vastgelegd)

- **Vroeg stoppen alleen bij schade:** na minimaal 7 dagen en 50.000 bezoekers per arm aanmeldingen per bezoeker in de quizarm meer dan 15% lager met kans van 95% of meer; of vastlegratio onder 90% die niet binnen 2 dagen te repareren is; of verdeling weergaven buiten 48 tot 52%. Dan terug naar 100% controle.
- **Niet vroeg stoppen bij winst.** Een vroege voorsprong is bij deze aantallen vaak toeval.
- **Quiz wint** als na 21 dagen plus 14 dagen rijping: kans dat omzet per bezoeker (14 d) hoger is dan controle minimaal 90%, en aanmeldingen per bezoeker niet meer dan 5% lager. Bevestigen op 30 dagen en in de januari-holdout.
- **Gelijkspel** (kans tussen 30 en 90%, verschil binnen plus of min 5%): quiz toch invoeren als aanmeldingen per bezoeker niet meer dan 5% lager zijn. Reden: de angle op het profiel heeft waarde voor campagnes en ads (zie 9) die deze test niet meet. Dit is een bewuste keuze van Floris, niet van de analyse.
- **Controle wint** (kans quiz beter onder 30%): quiz eruit, wel de les per stap meenemen (waar vallen ze af).
- Beslissing per angle: geen. Wel een volgende test als één angle duidelijk achterblijft (bijvoorbeeld de tekst na `performance` herschrijven).

## 9. Validatie van het antwoord

Verwachting: `non_toxic` circa 60 tot 75% (survey: 68 tot 76% als belangrijkste driver), `gift` circa 15 tot 25% (in december hoger), de rest verdeeld.

Wat een afwijking betekent:

| Uitkomst | Mogelijke uitleg | Wat doen |
| --- | --- | --- |
| `non_toxic` ruim onder 50% | (a) Bezoekers zijn geen kopers: de survey meet kopers, de quiz meet ook prijszoekers en twijfelaars. (b) Volgorde: de bovenste knop trekt extra. (c) Tekst: "Ditch the toxins" spreekt minder aan dan "non-toxic" in klanttaal | Koopratio per angle naast de verdeling leggen: koopt `non_toxic` vaker, dan klopt (a) en is de quiz juist een goede voorspeller. Volgorde willekeurig maken of omdraaien in een week. Tekst dicht bij klanttaal ("Non stick without toxic coating") |
| `non_toxic` boven 85% | Sociale wenselijkheid of de bovenste knop, of te weinig onderscheid tussen de opties | Dan zegt het antwoord weinig; opties scherper maken (pijn "peeling" los van "toxins") |
| `gift` veel hoger dan 25% buiten december | Gift-tekst trekt mensen die het aanbod als cadeaukans zien | AOV en koopratio per angle bekijken |
| `other` boven 20% | Opties passen niet, of mensen willen snel door | Antwoordopties herzien; is `other` vooral een niet-koper, dan werkt hij als filter (ook waardevol) |
| Verdeling verschuift per trigger of per apparaat | Haast op mobiel, eerste knop klikken om door te gaan | Per apparaat rapporteren |

Persoonsniveau (sterkste controle): bij kopers die later de post-purchase survey invullen, het quizantwoord naast hun surveyantwoord leggen. De survey komt niet in Klaviyo binnen (laatste event 2025), dus via een export van de surveytool, gekoppeld op profiel-ID buiten de repo; alleen totalen opslaan, geen klantdata. Doel: 70% of meer overeenstemming tussen `non_toxic` en "non-toxic/PFAS-free" in de survey. Veel lager: het quizantwoord is een momentopname en weegt minder zwaar in segmentatie.

Copyregel die hieruit volgt: de zin "7 in 10 of our customers came for the same reason" komt uit de survey en mag alleen bij `non_toxic` staan. Nooit quizcijfers als klantcijfers presenteren, en nooit een percentage tonen bij een angle waar de survey dat niet onderbouwt.

## 10. Hergebruik van de angle

- **Campagnes:** segmenten Angle · {code} voor onderwerpregels en hero per angle; of één campagne met dynamische blokken (`{% if person.siraat_goal == 'gift' %}`). Meten met een kleine holdout: dezelfde campagne generiek tegen per angle, omzet per ontvanger 3 dagen.
- **Flows:** browse, cart en checkout kunnen een regel per angle krijgen (bijvoorbeeld bij `gift` de cadeaugarantie en verzendgrens in december). Pas na de welkomtest, één ding tegelijk.
- **Ads:** Klaviyo-segmenten per angle naar Meta als custom audience: lookalikes per angle, uitsluiting van kopers, creatives per angle (gift-creatives naar lookalike gift). Klaviyo synchroniseert segmenten naar Meta; niets handmatig uploaden. Meten per adset op CPA en nieuwe-klant-ROAS.
- **Productontwikkeling en survey:** de verdeling per maand is een goedkope, doorlopende peiling van wat bezoekers (niet alleen kopers) willen.

## 11. Open vragen voor Floris of Alia

1. Kan een antwoordknop in Alia een eigen eigenschap of verborgen veld naar Klaviyo sturen? Zo niet: lijst per tak of event?
2. Geeft Alia omzet per variant over alle bezoekers (ook wie sluit en toch koopt)?
3. Kan Alia de knopvolgorde willekeurig maken?
4. Exacte startdatum van de trigger-test, en welke triggervariant wint rond 21 nov.
5. Akkoord met start 2 december en geen quiz in de piek.
