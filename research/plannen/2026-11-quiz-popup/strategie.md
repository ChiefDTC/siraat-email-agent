# Strategie: quiz-pop-up met angles (8 nov 2026)

Rol: STRATEEG. Vraag van Floris (na gesprek met Colin): hoe zinnig is een pop-up die eerst vraagt "wat is je doel?", daarna tekst en aanbod per antwoord toont en elke angle een eigen welkomflow geeft? En wat is de beste versie?
Bronnen: BRIEF.md, research/survey/ (pdf, 22,160 antwoorden), research/popup/2026-11-trigger-test.md, research/lijstkwaliteit/01-giveaway-instroom.md, research/plannen/2026-11-welcome-audit.md, DECISIONS.md. Klaviyo (account TdtTzz) en Shopify alleen gelezen. Niets gewijzigd, niets gecommit.

## 1. Advies in het kort

**Doen, maar kleiner en slimmer dan "vier volledige welkomflows".**

1. **Eén vraag vóór het e-mailveld**, als tik (geen typen): vier angles plus "Just looking" als overslaan. De vraag is de haak, niet een extra drempel.
2. **Het aanbod blijft voor iedereen gelijk** (wat de live pop-up nu belooft, plus 5 gifts, free shipping, kans op de PFAS water filter). Per angle verschuift alleen de kop, de bewijsregel en welke gift vooraan staat.
3. **Personalisatie eerst alleen in W1 en het succesvenster**, niet in vier aparte flows. Pas als een angle in de echte pop-up 15% of meer van de antwoorden haalt én de W1-variant wint, bouw je een eigen staart.
4. **Testen als echte A/B in Alia**: huidige pop-up tegen quiz-pop-up, 50/50, Smart Testing uit, start ná de lopende trigger-test en na Cyber Monday (vanaf ongeveer 2 december), herhalen in januari.
5. **Winnaar kiezen op omzet per bezoeker (7 en 30 dagen)**, niet op aanmeldratio. De quiz mag een paar procent aanmeldingen kosten als de aanmelders meer opleveren.

Waarom niet groter: 60 tot 76% van de kopers noemt hetzelfde motief (non-toxic). De meeste invullers zullen dus "non-toxic" kiezen en krijgen in feite de huidige boodschap. De winst zit in de andere 25 tot 40%, en die groepen zijn per dag klein (zie 7). Vier volledige flows kosten veel bouw en onderhoud voor segmenten van 50 tot 150 mensen per dag.

## 2. Wat we nu weten (eigen data)

| Wat | Cijfer | Bron |
|---|---|---|
| Pop-up | Alia ("Card Game", US Evergreen), ongeveer 88% van de aanmeldingen | DECISIONS 7 okt, smooche/00-plan |
| Klaviyo-formulieren | Alle 34 op draft; laatste 90 dagen samen 23 weergaven, 0 aanmeldingen. Basis zit dus niet in Klaviyo-forms | Klaviyo get_forms, query_form_values (8 nov) |
| Aanmeldingen Email List (Subscribed to List, per week) | 5,009 (week 5 okt), 5,240, 6,126, 8,395, 10,192 (week 2 nov, 6 dagen) | Klaviyo metric SCvkku |
| Bezoekers per week (Shopify) | 92,413, 77,438, 86,198, 127,920, 134,515 | Shopify sessions |
| **Aanmeldingen per bezoeker (alle bronnen)** | **5.4%, 6.8%, 7.1%, 6.6%, 7.6%** | eigen berekening |
| Waarvan via de pop-up (88%) | **ongeveer 4.8 tot 6.7% van alle bezoekers** | eigen berekening |
| Zichtbaarheid | 37% van de sessies (in-app prefetch Instagram/Facebook) ziet nooit een pop-up; per bezoeker die de pop-up kan zien ligt de ratio dus hoger | trigger-test, Clarity |
| Oude Klaviyo-pop-ups (laatste 365 dagen, per weergave) | 4.5% tot 8.6% submit rate (BFCM 2025 6.7%, Cyber Monday 7.2%, New Year 8.6%, Valentines 4.5%) | Klaviyo query_form_values |
| Omzet per aanmelder, 30 dagen | giveaway-pop-up $24.97, kortingspop-up $29.49 (koopt 11.0% tegen 13.8%) | lijstkwaliteit/01 |
| Stille aanmelders | 81% van de giveaway-aanmelders klikt en koopt niet in 14 dagen | lijstkwaliteit/01 |
| Snelheid | 60% van de pop-up-kopers koopt binnen 10 minuten, vóór W1 | smooche/00-plan |
| Welkom per mail | W1 $3.09 per ontvanger; W2 tot W5 samen $0.32 | welcome-audit |

Lezing: de omzet van een aanmelder valt in de eerste minuten (succesvenster en W1). Daar moet de angle het verschil maken, niet in mail 4.

Let op: in de Alia-data zelf (weergaven, aanmeldratio per weergave, per variant) kan ik niet; die cijfers staan alleen in het Alia-dashboard. Floris: graag de aanmeldratio per weergave van "US | Evergreen" over de laatste 30 dagen, dan is de basis exact.

## 3. Wat de survey precies zegt (letterlijke antwoordopties)

Gebruik deze formuleringen. Een andere vraag geeft een ander getal; noem altijd het getal bij de juiste vraag.

| Vraag (letterlijk) | n | Uitkomst (letterlijke optie) |
|---|---|---|
| "What is most important for them?" (2026) | 3,358 | "Toxin-Free Cookware" 71%, "Effortless non stick" 9%, "Lifetime Value/ Cost Savings" 5%, "Family safety" 5%, "cooking performance" 4%, "ease of use / maintanance" 3%, "Premium cookware" 2%, "Its a gift" 1% |
| "What matters most when choosing new cookware?" | 1,547 | "Non-toxic and PFAS-free materials" 68%, "Easy cleaning and convenience" 16%, "Lifetime guarrantee" 9% |
| "What do they value most when cooking?" | 592 | "Health & safety (toxin-free, clean cooking)" 76%, "Durability & quality (long-lasting cookware)" 18% |
| "Main reason + biggest frustration with old cookware" (open, auto-grouped) | 776 | "Coating / non-stick wears off" 41%, "Toxic / health concern" 27% |
| "Who is this purchase for?" (2025) | 8,885 | "Myself" 69%, "A gift" 19%, "A shared household purchase" 12% |
| "Who are they purchasing for?" (2026) | 2,850 | "Myself" 78%, "Spouse/ Partner" 11%, "Family member" 8% |
| "Which options did they seriously compare before choosing Siraat?" | 6,792 | "Stainless steel" 41%, "Ceramic" 17%, "Cast Iron" 13%, "Hybrid pans" 13% |
| "Which statement best describes them as a home cook?" | 3,678 | "I was actively searching for non-toxic/PFAS-free cookware" 60% |
| "What almost stopped them from buying?" | 3,060 | "Price / Budget concerns" 27%, "Wasn't sure about the size/which product to choose" 15%, "Uncertainty about whether titanium really works" 15% |

Twee belangrijke punten voor de angles:
- "Family safety" is maar 5% en is hetzelfde motief als non-toxic. Een aparte gezin-angle haalt kopers weg uit de hoofdgroep zonder nieuwe boodschap.
- Cadeau is 19% als vraag "voor wie", maar 1% als "wat is het belangrijkst". Cadeau is een situatie, geen motief. In de pop-up werkt het wel als keuze, omdat een gever echt iets anders moet horen (maat, retour, levering).

## 4. Benchmarks: harde data tegen leveranciersmarketing

Er is geen onafhankelijk, gecontroleerd onderzoek naar quiz-pop-ups. Bijna alles komt van partijen die pop-ups of quizzen verkopen. Hieronder per bron wat het is.

### Aanmeldratio: quiz of multi-step tegen gewone pop-up

| Bron | Uitkomst | Soort |
|---|---|---|
| Omnisend, popupstatistieken | Multi-step 2.1% tegen single-step 2.0%; gemiddelde pop-up 2.1%; Wheel of Fortune 3.5% | Leverancier, grote dataset, methode niet openbaar. Verschil multi-step vrijwel nul |
| Popupsmart, benchmark jan 2024 tot sep 2026 | Geen meetbaar voordeel van multi-step zodra je alleen echte aanmeldingen telt (klikken op stap 1 zonder e-mail weggelaten) | Leverancier, maar de enige die de juiste noemer gebruikt |
| Wisepops, 1.8 mln sessies | Multi-step 5.64% tegen single-step 3.07% (+84%) | Leverancier; definitie van "conversie" onduidelijk (mogelijk interactie in plaats van aanmelding) |
| Rejoiner (2017) | Twee stappen 11.9% tegen drie stappen 8.27% (conversie = couponcode gebruikt) | Oude case, andere maatstaf, wel richting: elke extra stap kost |
| Klaviyo Academy | Goede formulieren rond 2.75 tot 3% submit rate | Leverancier, algemeen |
| Alia, eigen cases | ZQuiet quiz 2.5% naar 19%; Graza kookquiz 4.5% naar 13.8%; Kut from the Kloth +199% e-mail; gemiddeld "15 tot 20% opt-in" | Leveranciersmarketing, voor/na zonder controlegroep, vaak met ander aanbod tegelijk |
| Alia, Firebelly Tea | Liep een quiz naast de gewone pop-up en **schrapte de quiz** na twee maanden omdat de gewone Alia-pop-up beter converteerde | Leverancier, maar tegen eigen quiz in: nuttig tegenvoorbeeld |
| Octane AI, cases (Curlsmith, Cake, Doe Lashes) | Quizconversie 6.3%; 84 tot 89% maakt de quiz af; "3x meer opt-ins dan pop-ups"; Octane-blog "7 tot 25%" | Leverancier; het gaat om productquizzen op een pagina (bezoeker kiest zelf), niet om een pop-up die onderbreekt |

**Wat ik als waar aanneem:** een vraag van één tik vóór het e-mailveld kost niet automatisch aanmeldingen; de betrouwbaarste bronnen (Omnisend, Popupsmart) zien ongeveer gelijk. De grote sprongen (2x, 3x, 19%) komen uit voor/na-cases waarin ook het aanbod of het ontwerp veranderde. Onze eigen basis ligt al hoog (4.8 tot 6.7% van alle bezoekers, 4.5 tot 8.6% per weergave bij oude Klaviyo-pop-ups), dus een verdubbeling is niet realistisch. Realistische verwachting: **min 10% tot plus 15% aanmeldingen per bezoeker**. Dat moet de test uitwijzen.

### Afhaken per extra stap

- Popupsmart: de winst van multi-step verdwijnt als je alleen ingevulde e-mails telt. Dus: wie op stap 1 klikt maar stap 2 niet afmaakt, is geen winst.
- Rejoiner: van twee naar drie stappen min 30% conversie (relatief).
- Formulieronderzoek (HubSpot 2024, alleen via een B2B-blog geciteerd, origineel niet gevonden): ongeveer 4% minder conversie per extra veld. Typvelden kosten meer dan tikken.
- Alia zelf: "de meest effectieve pop-ups hebben 2 tot 3 stappen maximaal".

Gevolg voor ons ontwerp: precies één vraagscherm, alleen knoppen, en de huidige stappen niet verlengen. Als de huidige pop-up al een sms-stap heeft, blijft die achter de e-mail en komt er geen vierde stap bij.

### Effect op omzet per aanmelder

- Geen benchmark die alleen het effect van een gesegmenteerde welkomflow meet. Eén bureaucase: welkom van $1.65 naar $4.51 per ontvanger na een quizflow (één klant, geen controlegroep).
- Kut from the Kloth (Alia): welkomomzet +145%. Leveranciersmarketing, ook meer aanmelders.
- Firebelly Tea (Alia): aankoopratio na aanmelding 14% naar 36%, maar dat is na het schrappen van de quiz.
- Wel hard: de enige personalisatie die in onze eigen data werkt is relevantie in het eerste scherm (BF-W1 $3.58 tegen staartmails $0.32). Een angle-specifiek W1 en succesvenster is dus de plek waar we het moeten zoeken.

Rekensom break-even: verliest de quiz 5% aanmeldingen, dan moet de omzet per aanmelder 5.3% stijgen (30 dagen: van $24.97 naar $26.29) om gelijk te spelen. Verliest hij 10%, dan 11.1% (naar $27.74).

## 5. Tooladvies

| | Alia (nu live) | Klaviyo-formulier | OptiMonk |
|---|---|---|---|
| Vraag vóór e-mail (mini quiz) | Ja, "Mini Quiz" is een standaardformaat; Alia noemt het zelf het formaat met de hoogste aanmeldratio | Ja (multi-step, radioknoppen) | Ja (survey/conversational) |
| Ander scherm of tekst per antwoord | **Waarschijnlijk** via knoppen die naar een eigen stap linken (de Alia-help over stappen waarschuwt dat knoppen naar andere stappen kunnen linken). Niet bevestigd: een Alia-blog zegt dat "statische mini-quizzes" geen conditionele logica hebben. Controleren in de editor | **Nee.** Community 2021, 2025 en aug 2026: geen vertakking binnen het formulier, alleen erna in de flow | Ja volgens OptiMonk (survey-antwoord stuurt vervolg) |
| Antwoord naar Klaviyo-profiel | **Ja.** Elk antwoord wordt een profieleigenschap; de vraagtekst is de naam van de eigenschap. Alia schrijft al `alia_popup_name`, `alia_campaign`, `alia_offer` | Ja | Ja (veldkoppeling naar custom property) |
| A/B-test met eigen verdeling | Ja (varianten, handmatige verdeling) | Ja | Ja |
| Smart Trigger, huidige ontwerpen en data | Ja, blijft | Nee, alles opnieuw | Nee; staat al dubbel op de site (cro/02) |

**Advies: Alia, binnen de huidige campagne, als tweede variant naast de huidige pop-up.** Geen Klaviyo-formulier (geen vertakking, Smart Trigger en historie weg) en geen OptiMonk (tweede pop-up-script, staat al op de schrap-lijst in cro/04).

Simpelste opzet:
1. Kopie van de huidige Alia-pop-up. Eerste stap: Mini Quiz met vijf knoppen. Daarna één e-mailstap per angle (vier kopieën van dezelfde stap, alleen kop en bewijsregel anders). "Just looking" gaat naar de huidige e-mailstap.
2. Lukt routeren per knop niet: één gedeelde e-mailstap met een algemene kop ("Your 5 free gifts are ready"). Dan gebeurt de personalisatie alleen in het succesvenster (als dat per antwoord kan) en in W1. Dat is nog steeds 80% van de waarde.
3. Antwoord komt als profieleigenschap binnen. Vraagtekst kort en vast houden, bijv. "What brings you to Siraat?", want die tekst wordt de naam van de eigenschap; nooit meer wijzigen na livegang.
4. In Klaviyo: in de welkomreis (BF-reis Rn556d nu, later T4a5Mk) één conditional split direct na de trigger op die eigenschap. Of: in W1 per angle een eigen blok met `{% if person|lookup:'What brings you to Siraat?' == '...' %}` (werkt op profielvelden; let op dat de eigenschap er bij het verzenden al staat, wacht 1 tot 2 minuten).

Open voor Floris (5 minuten in de Alia-editor): kan een quizknop naar een eigen stap linken; hoe heet de eigenschap precies in Klaviyo (één testaanmelding met een test@-adres, dat filter staat al in de welcome); schrijft Alia ook de variantnaam weg.

## 6. De angles (vier plus overslaan)

| # | Knop (Engels, in klanttaal) | Angle | Waarom deze | Verwacht aandeel (aanname) |
|---|---|---|---|---|
| 1 | **"Cook without PFAS"** | Non-toxic / gezondheid | 68 tot 76% noemt het; 60% zocht er al actief naar | 45 tot 65% |
| 2 | **"A nonstick that doesn't peel"** | Prestatie / coating die het begeeft | Grootste frustratie: "Coating / non-stick wears off" 41%; klanttaal "The peeling of non stick coatings" | 10 tot 20% |
| 3 | **"Easier than stainless or cast iron"** | Vervangen van RVS/gietijzer | Meest vergeleken: "Stainless steel" 41%, "Cast Iron" 13%; twijfel "whether titanium really works" 15% | 5 tot 15% |
| 4 | **"It's a gift"** | Cadeau | "A gift" 19% (2025); december is het cadeauseizoen | 5 tot 15% (hoger in december) |
| 5 | "Just looking" (kleine tekstlink) | Overslaan | Neutraal, geen oordeel (geen confirmshaming) | rest |

Waarom niet "family/kids safety": "Family safety" is 5% en hetzelfde motief als non-toxic. Het zou de hoofdgroep splitsen zonder nieuwe boodschap en een gezondheidsclaim over kinderen uitlokken die we niet willen maken. Gezin komt terug als zin binnen angle 1 ("for everyone you cook for").

Volgorde van de knoppen: vast, met non-toxic bovenaan (de meeste mensen zoeken die). Willekeurige volgorde (Alia kan dat) geeft eerlijkere aandelen maar maakt de grootste groep trager; alleen gebruiken als het doel puur meten is.

**Vóór of na het e-mailveld: vóór.** Eén tik zonder e-mail is een kleine stap die nieuwsgierig maakt (de bezoeker wil zien wat er "voor hem" komt), en alleen dan kan de e-mailstap de juiste kop tonen. Na het e-mailveld levert het wel data op, maar geen hogere aanmelding en geen relevanter aanbod op het moment dat het telt. Als de test laat zien dat de vraag vooraf te veel kost, is de terugvaloptie: dezelfde vraag als stap na de e-mail (zoals een sms-stap), met alleen personalisatie in succesvenster en W1.

**Overslaan: ja**, als "Just looking" onder de knoppen, plus de gewone sluitknop. Wie overslaat, krijgt de huidige pop-up. Geen dwang, want dwang kost aanmeldingen bij precies de mensen die het snelst kopen.

## 7. Segmentgrootte en meetbaarheid

Bij 900 pop-up-aanmeldingen per dag buiten de BF-piek (oktober 720 tot 1,000) en een 50/50-test krijgt de quizarm ongeveer 450 per dag:

| Angle | Aandeel (aanname) | Per dag in de quizarm | Per 14 dagen |
|---|---|---|---|
| Non-toxic | 55% | ~250 | ~3,500 |
| Coating | 15% | ~70 | ~950 |
| RVS/gietijzer | 10% | ~45 | ~630 |
| Cadeau | 10% | ~45 | ~630 |
| Overslaan | 10% | ~45 | ~630 |

Wat is meetbaar:
- **Pop-up-test (quiz tegen huidig) op aanmeldingen per bezoeker**: bij 5% basis en 10% relatief verschil ongeveer 30,000 bezoekers per arm. De site heeft ongeveer 12,000 tot 19,000 bezoekers per dag, dus binnen een week genoeg; toch 14 volle dagen draaien voor weekdagpatroon en de omzetvangrail.
- **Omzet per aanmelder tussen de twee armen**: bij 11% aankoop in 30 dagen en +15% relatief ongeveer 5,800 aanmelders per arm, dus ongeveer 2 weken instroom; het 30-dagenresultaat is pas 30 dagen later compleet. Gebruik 7 dagen als eerste lezing.
- **Per angle apart (bijv. cadeau-W1 tegen generieke W1)**: met 45 per dag niet in een redelijke tijd. Daarom per angle niet A/B-testen op omzet, maar alleen bekijken (klik, aankoop, uitschrijving) en de hele quizarm tegen controle beoordelen.

## 8. De pop-up scherm voor scherm

Ontwerp en beeld van de huidige pop-up blijven (gelijk in beide armen, behalve deze schermen). Copy in het Engels, volgens siraat-direct-response, geen streepjes.

**Scherm 1, de vraag (geen e-mailveld)**
- Kop: "What brings you to Siraat?"
- Subregel: "Pick one. We'll show you where to start, plus your 5 free gifts."
- Vier knoppen (zie 6), daaronder tekstlink "Just looking".
- Sluitknop rechtsboven zoals nu.

**Scherm 2, e-mail (kop en bewijsregel per antwoord; aanbod, veld en knop overal gelijk)**

| Antwoord | Kop | Bewijsregel (eerlijk, met juiste bron) |
|---|---|---|
| Cook without PFAS | "You're in good company." | "7 in 10 of our customers told us toxin-free cookware mattered most. Pure titanium, no coating, lab report no. 25895." |
| A nonstick that doesn't peel | "Nothing on it to peel off." | "The frustration our customers named most: a coating that wears off. Ours has no coating, and a 75-year warranty." |
| Easier than stainless or cast iron | "The pan people pick over stainless." | "Stainless steel is the pan our customers compared us with most. Preheat, add a little oil, and it lets go." |
| It's a gift | "A gift they'll use every morning." | "1 in 5 of our customers bought Siraat as a gift. 30-day returns, 75-year warranty." |
| Just looking | huidige kop | huidige tekst |

Daaronder voor iedereen gelijk: het aanbod zoals de live pop-up het nu belooft (deelname aan de giveaway als die nog loopt), "5 free gifts" ($555 value alleen in de US), e-mailveld, knop, "No thanks". Geen nieuwe code, geen nieuw percentage.

**Scherm 3, sms (alleen als de huidige pop-up hem heeft)**: ongewijzigd.

**Scherm 4, succes (per antwoord, als Alia dat toelaat)**
- Non-toxic: "Here's the paper." Knop naar de Pan Pro of de sale-collectie, tekstlink naar het labrapport.
- Coating: "Start with the pan everyone starts with." Knop naar Hammered Pan Pro (71% van de kopers kocht die).
- RVS/gietijzer: "Heat first, then oil. Same as stainless, lighter than cast iron." Knop naar Pan Pro, link naar de verzorgingspagina.
- Cadeau: "Not sure about the size? Most people pick the Standard." Knop naar de 6-delige set of de Pan Pro, plus de retourregel.
- Overslaan: huidige succespagina.

Elke angle krijgt zijn eigen UTM of linkparameter (bijv. `?angle=pfas`), zodat ook kopen in de eerste 10 minuten per angle zichtbaar is in Shopify en Triple Whale.

## 9. Aanbod per angle (binnen het bestaande aanbod)

Geen nieuwe kortingen. Alleen welke gift vooraan staat en hoe het aanbod geframed wordt.

| Angle | Gift vooraan | Framing | Bewijs erbij |
|---|---|---|---|
| Non-toxic | Kans op de **PFAS water filter** (altijd "win", nooit "free", nooit purifier) en het **Plastic-free ebook** | "A PFAS-free kitchen starts with the pan" | Labrapport 25895, certificaat |
| Coating | **Favorites cookbook** en **Mystery gift** | "One pan, nothing to replace" | 75-year warranty, 100,000+ customers |
| RVS/gietijzer | **Favorites cookbook** (eerste koken goed doen) | "If it doesn't suit how you cook, send it back" | 30-day returns, 75-year warranty |
| Cadeau | **Free shipping** en **Mystery gift** | "It arrives with 5 free gifts, shipping included" | 30-day returns |
| Overslaan | Huidige volgorde | Huidig | Huidig |

**Voorstellen voor Floris (niet zelf invoeren):**
1. Cadeau: een gift-optie in de winkelwagen (cadeaubericht, prijsloze pakbon of gift receipt) en een verlengde retourtermijn tot half januari voor decemberorders. Dat beantwoordt het gever-bezwaar (maat, past het?) zonder korting.
2. Cadeau: een "gift box"-presentatie van de 6-delige set (alleen beeld en tekst, zelfde prijs).
3. Coating: een "trade in your old pan"-verhaal kan sterk zijn, maar alleen als het echt bestaat. Niet gebruiken zonder besluit.

## 10. Welkomflow per angle

Fase 1 (met de pop-up-test, klein):
- **W1 per angle**: andere onderwerpregel, hero-kop en eerste blok; productkaarten, aanbod, footer en header blijven (vaste header en footer uit `klaviyo/templates/partials/`).
  - Non-toxic: zoals nu (huidige W1 is al PFAS en labrapport).
  - Coating: hero "Nothing on it to peel off", vergelijking met een PFAS-coated pan (mag, DECISIONS 8 okt), review over duurzaamheid.
  - RVS/gietijzer: hero "Stainless steel, or titanium?", vergelijking op categorie (geen merken), Tammy R138 "lighter than my old cast iron pans" (verbatim controleren met check_reviews.py), techniekregel voorverwarmen.
  - Cadeau: hero "For you, or someone you cook for?", maatkeuze in één regel, retour 30 dagen, geen "your first egg"-taal.
- Uitvoering: één conditional split vooraan in de welkomreis of één W1-template met `if`-blokken. Geen vier flows.
- Staart (W2 tot W5) gelijk voor iedereen, behalve één wissel: W4 (maat) toont bij cadeau "which size for them".

Fase 2 (alleen na een winnende fase 1, januari): een eigen staart voor een angle die 15% of meer van de antwoorden haalt en in W1 duidelijk beter klikt. Post-purchase kan het antwoord ook gebruiken (cadeau: geen "your first egg" in P2 en U1; dat probleem staat al in survey/01 punt D7).

## 11. Testplan en meting

| Onderdeel | Keuze |
|---|---|
| Armen | A: huidige pop-up (controle). B: quiz-pop-up. Zelfde trigger (winnaar van de trigger-test), zelfde aanbod, zelfde uitsluitingen |
| Verdeling | 50/50 handmatig in Alia, Smart Testing uit |
| Start | Na afloop van de trigger-test en na Cyber Monday (vanaf ongeveer 2 december). Niet tijdens de BF-week: twee tests op dezelfde pop-up maken beide onleesbaar |
| Duur | Minimaal 14 volle dagen; herhalen in januari (december is cadeau-zwaar en vertekent het cadeau-aandeel) |
| Primair | Omzet per bezoeker die de pop-up kon zien, 7 dagen (Alia-variant plus Shopify/Triple Whale) |
| Secundair | Aanmeldingen per bezoeker (niet per weergave), aankoop en omzet per aanmelder na 7 en 30 dagen (Klaviyo, segment op `alia_popup_name` per variant), verdeling van de antwoorden |
| Vangrails | Uitschrijving W1 onder 1.7% (huidig niveau), spam onder 0.157%, aanmeldingen per bezoeker niet meer dan 10% lager |
| Beslisregel | B wint als omzet per bezoeker gelijk of hoger is en aanmeldingen niet meer dan 10% dalen. Dalen aanmeldingen meer dan 10%: terugvaloptie (vraag na de e-mail) testen |

## 12. Risico's

1. **Minder aanmeldingen door de extra klik.** Betrouwbaarste bronnen zien geen verschil, maar Rejoiner en Firebelly laten zien dat het ook mis kan gaan. Beperken: één scherm, alleen tikken, "Just looking" als uitweg, meten per bezoeker.
2. **Te kleine segmenten.** Coating, RVS en cadeau krijgen samen misschien 35% en per stuk 45 tot 70 mensen per dag in de testarm. Daarom niet per angle op omzet testen en geen vier volledige flows bouwen.
3. **De "70%"-claim.** "70% of our customers came for the same reason" is niet wat de survey meet. De survey vraagt kopers wat het belangrijkst was, niet waarom ze kwamen, en het is 71% van 3,358 antwoorden in één survey (68 tot 76% over alle surveys). Eerlijk: "7 in 10 of our customers told us toxin-free cookware mattered most." Voor de andere angles geen percentage van "mensen zoals jij" verzinnen; alleen de cijfers uit sectie 3 bij de juiste vraag. Het coating-cijfer (41%) komt uit open antwoorden die automatisch gegroepeerd zijn; daarom zonder percentage formuleren ("the frustration our customers named most").
4. **Gezondheidsclaims.** "Non-toxic" mag (besluit 31 okt). Niet: "your old pan is toxic", "microplastics", iets over kinderen of gezondheidseffecten. "Fry an egg, no oil" niet (bron van retouren).
5. **Zelfselectie en spel.** Bezoekers kiezen de knop die het mooiste aanbod lijkt te geven. Omdat het aanbod gelijk is, speelt dat niet; houd het zo.
6. **Twee tests tegelijk.** De trigger-test loopt nu. Overlap maakt beide onbruikbaar.
7. **Eigenschapnaam = vraagtekst.** Wie de vraag later herschrijft, breekt de splits en segmenten. Vastleggen in DECISIONS bij livegang.
8. **Google-straf op mobiel** voor schermvullende pop-ups direct na binnenkomst uit organisch zoeken (trigger-test). De quiz verandert daar niets aan; de trigger-keuze wel.
9. **BF-vertekening.** Gedrag in de sale is niet het gedrag in januari. Herhalen.
10. **Bouwlast.** Elke extra variant moet bij elke aanbodwijziging mee (zoals de 5-gifts-ronde in 93 templates). Fase 1 houdt het bij vier pop-upschermen en één W1 met blokken.

## 13. Wat Floris moet beslissen

1. Akkoord op fase 1 (vraag vóór e-mail, aanbod gelijk, alleen W1 en succesvenster per angle).
2. Akkoord op de vier angles en de knopteksten, met "Just looking" als overslaan.
3. In de Alia-editor checken: knop naar eigen stap, naam van de eigenschap, variantnaam naar Klaviyo. Plus de huidige aanmeldratio per weergave uit het Alia-dashboard.
4. Voorstellen cadeau (gift receipt, verlengde retour in december, gift-box-presentatie): ja of nee.
5. Startdatum na de trigger-test en na Cyber Monday.

## 14. Bronnen

Eigen data (alleen gelezen, 8 nov 2026):
- Klaviyo get_forms en query_form_values (laatste 90 en 365 dagen), metric SCvkku per week en lijst (4 okt tot 7 nov).
- Shopify ShopifyQL `FROM sessions SHOW sessions, online_store_visitors TIMESERIES week SINCE 2026-10-05 UNTIL 2026-11-07`.
- research/survey/post-purchase-survey-insights.pdf (pagina 2, 6, 7, 10, 12, 13), research/survey/01-klantbegrip.md, research/lijstkwaliteit/01-giveaway-instroom.md, research/popup/2026-11-trigger-test.md, research/plannen/2026-11-welcome-audit.md, research/smooche/00-plan.md, research/cro/02-pdp-audit.md en 04-actieplan.md, DECISIONS.md.

Web (zoekresultaten; de Alia-helppagina's zelf waren in deze omgeving niet te openen, intercom.help en help.aliapopups.com staan niet op de netwerklijst):
- Alia, quizantwoorden naar Klaviyo: https://intercom.help/alia-help-center/en/articles/13345828-personalizing-your-klaviyo-welcome-flow-using-alia-quiz-responses
- Alia, gesynchroniseerde eigenschappen: https://help.aliapopups.com/en/articles/14046234-understanding-the-alia-and-klaviyo-integration-synced-properties
- Alia, segmenten op mini-quizdata: https://intercom.help/alia-help-center/en/articles/11112488-how-to-create-segments-in-klaviyo-using-the-mini-quiz-data
- Alia, stappen toevoegen en beheren: https://intercom.help/alia-help-center/en/articles/12569406-how-to-add-and-manage-steps-in-your-alia-popup
- Alia, best practices (2 tot 3 stappen): https://intercom.help/alia-help-center/en/articles/12569654-alia-best-practices-design-conversion-tips
- Alia, FAQ (randomize mini quiz): https://intercom.help/alia-help-center/en/collections/12496922-faqs
- Alia cases: https://www.aliapopups.com/blog/zquiet-alia-case-study, https://www.aliapopups.com/success-stories/kut, https://www.aliapopups.com/blog/firebelly-tea-generates-13k-in-incremental-revenue-and-2x-their-signups-with-alia-popup, https://www.aliapopups.com/blog/15-ecommerce-gamification-examples-that-drive-conversions, https://www.aliapopups.com/blog/9-killer-ecommerce-popup-examples-with-results
- Klaviyo, formulieranalyse (multi-step submit rate): https://help.klaviyo.com/hc/en-us/articles/360015960712-Understanding-sign-up-form-analytics
- Klaviyo, multi-step analytics: https://klaviyo.com/blog/multi-step-form-analytics
- Klaviyo Academy, formulieren meten: https://academy.klaviyo.com/en-us/courses/getting-started-with-sign-up-forms/lessons/measure-the-effectiveness-of-your-forms
- Klaviyo community, geen vertakking in formulieren: https://community.klaviyo.com/marketing-30/conditional-steps-with-sign-up-form-3209, https://community.klaviyo.com/marketing-30/forms-with-built-in-conditional-split-logic-11393, https://community.klaviyo.com/marketing-30/how-to-set-up-a-conditional-url-redirect-based-on-form-responses-17264, https://community.klaviyo.com/marketing-30/website-pop-up-conditional-input-fields-19646
- Klaviyo, quiz-integratie: https://developers.klaviyo.com/en/docs/guide_to_integrating_a_quiz_and_survey_platform
- OptiMonk surveys naar Klaviyo-eigenschappen: https://www.optimonk.com/features/surveys, https://www.optimonk.com/features/klaviyo-lists-and-segments
- Omnisend popupstatistieken: https://www.omnisend.com/blog/email-popup-statistics/
- Omnisend multi-step (definitie aanmeldratio): https://support.omnisend.com/en/articles/7325323-create-multi-step-signup-forms
- Popupsmart, multi-step benchmark: https://popupsmart.com/blog/multi-step-forms-shopify
- Wisepops, micro-commitment: https://wisepops.com/blog/micro-commitment-popups
- Rejoiner, aantal stappen: https://rejoiner.com/resources/email-capture-best-practices/
- Justuno, één tegen twee stappen (methode, geen cijfers): https://blog.justuno.com/optimizing-email-pop-ups-ab-tests-one-step-opt-in-two-step-opt-in
- Octane AI cases: https://www.casestudies.com/company/octane-ai/case-study/how-curlsmith-gained-100k-email-subscribers, https://www.casestudies.com/company/octane-ai/case-study/cake-increases-revenue-10-with-octane-ai, https://www.casestudies.com/company/octane-ai/case-study/doe-lashes-3x-email-opt-ins-with-octane-ai, https://www.octaneai.com/blog/how-to-create-a-shopify-quiz-with-octane-ai
- Formuliervelden (HubSpot 2024 via derde): https://brixongroup.com/en/lead-forms-in-b2b-the-perfect-balancing-act-between-data-depth-and-conversion-rate
- Welkomflow-benchmarks: https://help.klaviyo.com/hc/en-us/articles/360033669452-Performance-Benchmarks-for-Flow-Emails, https://revenuehunt.com/klaviyo-zero-party-data/
- Privy: geen bruikbare cijfers over quiz- of multi-step-pop-ups gevonden.
