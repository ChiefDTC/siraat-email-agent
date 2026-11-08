# Welkomflow per angle (quiz-popup), plan (8 nov 2026)

> **Correctie (8 nov 2026):** het cijfer "41% coating die afbladdert/slijt" uit de PDF-samenvatting klopt niet met de ruwe surveytelling. Ruwe open antwoorden (n=760): plakken 34.1%, toxisch/PFAS 29.9%, gezondheid 15.8%, coating bladdert/krast 14.5%. Gebruik voor de performance-angle geen 41%; zie next-step.md voor de juiste bewijsregels.


Rol: FLOW PLANNER. Alleen gelezen: Klaviyo (GET en rapporten), de site (publieke pagina's), de repo. Niets aangepast, niets gecommit.
Bronnen in de repo: `BRIEF.md` (deze map), `research/plannen/2026-11-welcome-audit.md`, `klaviyo/templates/v3/flows-nov/welcome/` (wn2 t/m wn5, US en INT), PLAYBOOK.md, DECISIONS.md, skill siraat-direct-response, `research/copy/01-dr-research.md` (reviewshortlist), `research/ux-round2/comparisons.md` (vergelijkingsrijen).

## 0. Kort

- **Architectuur:** één welkomflow op lijst Uw8eZG met een vertakking op `siraat_goal` na de bestaande stops (besteld, bestaande klant). Drie angle-takken plus een **terugvaltak "geen antwoord" = de huidige reis** (BF-W1, BF-W2/BF-W3, staart). Geen aparte flows.
- **Mails per tak:** Non-toxic 6, Performance 7 (subtak "overstap van RVS of gietijzer" gebruikt dezelfde 7 in een andere volgorde), Gift 5 plus één deadline-campagne. Drie mails zijn gedeeld over alle takken (Benjamin, maatkiezer, laatste mail met "Two promises"), met een eigen openingsalinea per antwoord.
- **Verwachte impact (schatting):** +14 tot +28% omzet per aanmelder over de hele reis, ongeveer $3.89 naar $4.40 tot $5.00, bij ~6,500 aanmelders per week $3,300 tot $7,100 per week extra. De grootste onzekerheid is niet de flow maar de popup: een extra vraag kan het aantal aanmeldingen verlagen. Daarom eerst de popup testen, met de terugvaltak als vangnet.

## 1. Huidige welkomflow in Klaviyo (gelezen 8 nov 2026)

### Opbouw
| Flow | Status | Trigger | Rol |
| --- | --- | --- | --- |
| T4a5Mk "v4 · Welcome" | live | lijst Uw8eZG | Hoofdwelcome. Flowfilter: e-mail bevat geen `test@` en nooit eerder in deze flow. |
| Rn556d "v4 · BFCM Welcome · direct A/B (hoofdlijst)" | live, 100% sinds 6 nov | lijst Uw8eZG | BF-W1 op 0 minuten. |
| YqKCmH "v4 · BF follow-up BF-W2/BF-W3 · TEST (draft)" | live | lijst Uw8eZG | BF-W2 dag 1 10:00, BF-W3 dag 2 09:00. |

Stappen T4a5Mk (uit de audit, bevestigd via de API): wacht 5 min, uitstapsplit (Placed Order sinds flowstart, of mail uit Rn556d in de laatste dag), split "ooit besteld" naar W0, W1 (A/B), dag 1 W2 (Benjamin), dag 3 W3, landsplit, dag 6 W4-US/INT, dag 10 W5-US/INT. Na W1 heeft geen mail een eigen verzendfilter. Gevolg sinds 6 nov: nieuwe aanmelders krijgen BF-W1 en verlaten T4a5Mk bij de uitstapsplit; de staart loopt leeg.

### Cijfers laatste 90 dagen (flow-values-report, conversie Placed Order RSNxYV, opgehaald 8 nov 2026)
| Mail | Ontvangers | Open | Klik | Conversie | Omzet | Per ontvanger | Uitschr. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| W0 (bestaande klant) | 149 | 61.7% | 6.71% | 0.67% | $1,177 | $7.90 | 0.67% |
| W1 (A/B) | 18,468 | 45.1% | 3.96% | 1.02% | $56,320 | **$3.12** | 1.85% |
| W2 Benjamin | 13,528 | 41.2% | 2.22% | 0.18% | $6,331 | $0.47 | 1.56% |
| W3 | 12,698 | 38.4% | 1.23% | 0.15% | $5,599 | $0.45 | 1.06% |
| W4-US | 6,482 | 37.5% | 1.18% | 0.06% | $1,310 | $0.20 | 0.48% |
| W4-INT | 5,193 | 36.4% | 1.54% | 0.04% | $401 | $0.08 | 0.95% |
| W5 (twee varianten) | 8,436 | 35.6 tot 36.8% | 0.58 tot 1.08% | 0.05% | $549 | $0.07 | 0.76% |
| Oud Welcome 1, 2, 4 t/m 8 (uitloop) | 15,235 | | | | $15,710 | $1.03 | |
| **Totaal T4a5Mk** | **80,189** | 42.3% | 2.05% | 0.36% | **$87,398** | **$1.10** | 1.43% |
| BF-W1 (Rn556d) | 7,925 | 37.1% | 4.29% | 1.04% | $25,529 | **$3.31** | 1.58% |

Lezing:
- W1 en BF-W1 dragen de reis: ruim $3 per ontvanger. W2 t/m W5 samen: $14,190 op 46,337 ontvangers = **$0.31 per ontvanger**.
- Per aanmelder (nieuw pad): W1 $3.12 plus staart $14,190 / 18,468 = $0.77, samen **~$3.89 per aanmelder**. Dit is de basislijn voor de schatting in sectie 5.
- Uitschrijving W1 1.85% en W2 1.56% zit boven de 1%-grens (PLAYBOOK 6). Een mail die past bij het antwoord moet dit eerder verlagen dan verhogen; bewaken.

## 2. Wat er buiten bekend is (bronnen)

- **Alia schrijft quizantwoorden als profieleigenschap naar Klaviyo**; de helppagina beschrijft een Conditional Split op "Properties about someone" met die eigenschap, en adviseert: als twee paden bijna hetzelfde zijn, niet splitsen. [Alia Help Center: Personalizing your Klaviyo welcome flow using Alia quiz responses](https://intercom.help/alia-help-center/en/articles/13345828-personalizing-your-klaviyo-welcome-flow-using-alia-quiz-responses). Alia stuurt verder eigen eigenschappen (zoals `alia_offer`, de code moet bij de klik op Submit worden meegestuurd om in de flow beschikbaar te zijn): [Alia: synced properties](https://intercom.help/alia-help-center/en/articles/14046234-understanding-the-alia-and-klaviyo-integration-synced-properties).
- **Klaviyo** beschrijft het patroon "quizantwoord wordt profieleigenschap, welkomflow splitst op het antwoord" (voorbeeld: splits op "Hair Goal" of "Skin Type"): [Klaviyo Developers: Integrate a quiz and survey platform](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_quiz_and_survey_platform). Klaviyo Academy: per split één eigenschap, wie eraan voldoet gaat het "Yes"-pad: [Personalize your welcome series with profile properties](https://academy.klaviyo.com/en-us/quick-guides/personalize-your-welcome-series-with-profile-properties).
- **Tegengeluid:** een antwoord in de Klaviyo Community raadt voor "cadeau tegenover voor mezelf" twee aparte welkomflows met een flowfilter aan: [Klaviyo Community, vraag 8395](https://community.klaviyo.com/questions/8395). Afgewogen in sectie 3.
- **Case studies (zelfgerapporteerd, niet onafhankelijk):** een bureau meldt een quiz-gestuurde welkomflow die de omzet per ontvanger van $1.65 naar $4.51 bracht (+173%), order rate +106%: [Web Profits, customer lifecycle](https://webprofits.com.au/customer-lifecycle). Een supplementenmerk met vijf welkompaden via conditional splits op een popupvraag: [Contra, skincare/pop-up quiz](https://contra.com/p/glrBrvWo-growing-a-skincare-brands-email-list-with-a-pop-up-quiz). Segmentatie van welkominhoud op voorkeur (zonder quiz): +47% omzet per mail bij icelolly.com: [casestudies.com, Kickdynamic](https://www.casestudies.com/company/kickdynamic/case-study/icelollycom-customer-case-study-2). Quizwaarde stijgt met de mandwaarde (ConvertFlow, eigen data: $13.49 omzet per quizweergave bij manden boven $150): [ConvertFlow, ecommerce personalization](https://www.convertflow.com/blog/ecommerce-personalization).
- **Algemene benchmark personalisatie:** McKinsey, "The value of getting personalization right, or wrong, is multiplying" (2021): personalisatie geeft meestal 10 tot 15% omzetstijging: [kopie van het rapport](https://assets.super.so/f7785043-6038-445b-9b2a-38bfd53ed1b8/files/ddb8c26b-0d4c-40bd-ac63-ea1f94dbf3b6/the-value-of-getting-personalization-right-or-wrong-is-multiplying.pdf), [Business Chief](https://businesschief.com/technology-and-ai/mckinsey-prioritise-personalisation-for-10-15-revenue-lift). Klaviyo-benchmark 2024 adviseert de welkomflow te segmenteren op zoveel mogelijk profielkenmerken (advies, geen meting): [Klaviyo 2024 Benchmark Report](https://resources.klaviyo.com/2024-benchmark-report).

Let op: intercom.help, developers.klaviyo.com en webprofits.com.au zijn in deze omgeving niet bereikbaar; de inhoud komt uit de zoekresultaten, niet uit de volledige pagina. Voor livegang de twee Alia-pagina's zelf lezen (vooral de exacte naam van de eigenschap en de synctijd).

## 3. Architectuur

### Advies: één flow, vertakking op `siraat_goal`, terugvaltak = huidige reis

```
Lijst Uw8eZG
  flowfilter: geen test@, nooit eerder in deze flow, (overgang) niet in T4a5Mk/Rn556d/YqKCmH in 30 dagen
  wacht 5 minuten                        (Alia-sync van het antwoord, zoals nu al in T4a5Mk)
  uitstapsplit: Placed Order sinds start -> einde
  split: ooit besteld? ja -> W0, einde
  split 1: siraat_goal = gift ?                      ja -> TAK GIFT
  split 2: siraat_goal = performance of switch ?     ja -> split 2b: switch? -> TAK PERFORMANCE (volgorde A of B)
  split 3: siraat_goal = non_toxic of family ?       ja -> TAK NON-TOXIC
  anders (leeg, onbekend, ander antwoord)            -> TERUGVALTAK = huidige reis (BF-W1, BF-W2, BF-W3, staart)
```

Waarom één flow en geen vier:
1. **Eén trigger, geen dubbele mails.** Alle aanmelders komen op Uw8eZG. Vier flows op dezelfde lijst moeten elkaar via flowfilters uitsluiten; als het Alia-antwoord een paar seconden na de lijstinschrijving binnenkomt, kan iemand in twee flows tegelijk starten (de huidige Rn556d en T4a5Mk laten zien hoe snel dat gebeurt: de uitstapsplit "mail uit Rn556d" is er juist om die reden). In één flow beslist één split op één moment.
2. **De stops staan één keer vooraan** (besteld, bestaande klant, test@), en gelden voor elke tak. Nu zit "besteld" alleen in de uitstapsplit; bij vier flows moet dat vier keer goed staan.
3. **De terugvaltak is gratis.** Wie de vraag overslaat, de oude popup (A) zag, of via een ander formulier binnenkomt, krijgt exact de huidige reis. Er gaat geen omzet verloren als de quiz tegenvalt.
4. **Meten per tak** kan gewoon in één flow (flow-values-report per `flow_message_id`, zoals de audit al doet). Het Community-advies voor aparte flows gaat over overzicht in de UI, niet over werking; met heldere namen (`NT1`, `PF1`, `G1`) is dat ondervangen.
5. **Smart Sending en de 1%-uitschrijfgrens** zijn per flow makkelijker te bewaken.

Wanneer toch apart: alleen als de gifttak na de feestdagen een eigen ritme krijgt (bijvoorbeeld verjaardagen, Moederdag). Dan kan hij later als eigen flow worden losgeknipt; de templates blijven gelijk.

### Eigenschap en antwoorden (voorstel voor Alia)
| Popupknop (Engels, voorstel) | `siraat_goal` | Tak | Grond in de enquête |
| --- | --- | --- | --- |
| "Get the toxins out of my kitchen" | `non_toxic` | Non-toxic | 68 tot 76% noemt non-toxic als belangrijkste reden |
| "A pan that actually performs" | `performance` | Performance | (41% geschrapt, zie correctie) |
| "I'm switching from stainless or cast iron" | `switch` | Performance, volgorde B | 41% vergeleek met roestvrij staal |
| "It's a gift" | `gift` | Gift | ongeveer 1 op 5 koopt als cadeau |
| (optioneel) "Safer cooking for my family" | `family` | Non-toxic, met eigen alinea's | partner/familie is het restant van "voor wie" |

Advies: vier knoppen, zonder `family`. Een vijfde knop maakt de popup langer en "safer for my family" duwt de copy richting een gezondheidsclaim (verboden). Wie voor familie kookt, past in Non-toxic; de maatkiezer heet al "Who are you cooking for?". Wil Floris `family` toch, dan wordt het een waarde die in Non-toxic valt met één andere openingsalinea, geen eigen tak.
De waarden zijn een voorstel; de echte naam en waarden van de eigenschap volgen uit Alia (sectie 2) en moeten in een testprofiel bevestigd worden voordat de split gebouwd wordt.

### Wat er gebeurt met de BFCM-inhoud
- **Twee lagen scheiden: angle en aanbod.** Elke angle-mail heeft één vast aanbodblok (hero-aanbodbalk, productkaarten met prijs, gifts-regel, friction reducer). Tot en met 30 nov is dat de Black Friday Sale (tot 70% off, 5 free gifts, $555 value alleen in USD-mails, free shipping), met dezelfde catalogusbedragen als BF-W1 en wn2 t/m wn5. Vanaf 1 dec wordt alleen dat blok gewisseld (in het bouwscript één variabele, zoals `PRICES_US` in `make_welcome.py`), de angle-inhoud blijft staan. Het aanbod na BFCM is nog niet bekend: [VRAAG FLORIS].
- **BF-W1 blijft de eerste mail in de terugvaltak** (kopie, op 5 minuten in plaats van 0). De angle-W1's nemen de structuur van BF-W1 over (aanbod in onderwerp, preview en eerste scherm, productkaarten met prijs), omdat die structuur bewezen werkt ($3.31). Alleen kop, eerste zin, bewijs en volgorde van de kaarten verschillen per antwoord.
- **BF-W2/BF-W3 (YqKCmH)** gaan in de terugvaltak mee. Angle-takken krijgen ze niet: hun dag 1 en dag 2/3 zijn de angle-mails. Zo krijgt niemand twee mails op dezelfde dag.
- **Geen einddatum in flowmails** (DECISIONS): de sale-einddatum 30 nov komt alleen in de harde push uit campagnes. Uitzondering die Floris moet goedkeuren: de verzenddeadline in de gifttak (sectie 4.3).

### Wat er gebeurt met de bestaande filters
| Filter nu | In de nieuwe flow |
| --- | --- |
| Flowfilter "geen test@", "nooit eerder in de flow" | Blijft gelijk. |
| Uitstapsplit "Placed Order sinds flowstart" | Blijft vooraan. **Plus** in elke angle-mail een verzendfilter "Placed Order = 0 sinds flowstart" (nu ontbreekt die na W1; aanbeveling uit de audit). |
| Uitstapsplit "mail uit Rn556d in de laatste dag" | Vervalt zodra Rn556d en YqKCmH in deze flow zijn opgenomen (terugvaltak). Tijdens de overgang vervangen door flowfilter "niet in T4a5Mk/Rn556d/YqKCmH in 30 dagen" (PLAYBOOK 7). |
| Split "ooit besteld" naar W0 | Blijft vóór de angle-split: bestaande klanten krijgen W0, geen angle-tak. |
| W1-filter "geen mail uit checkout QUBUQV of cart TZG9Mx in de laatste dag" | Op alle verkoopmails van de takken (W1, dag 1, de maatkiezer en de laatste mail), niet op de Benjamin-brief. |
| Landsplit US/INT | Blijft, per tak vlak voor de eerste mail met prijzen (W1). Mails met prijzen hebben een US- en een INT-versie (zelfde patroon als wn2 t/m wn5). |

## 4. Mailschema per angle

Algemene regels voor alle takken (skill siraat-direct-response): kalm register, zinskapitalen, geen uitroeptekens, één idee per mail, Benjamin is de enige "ik", ondertekening `Benjamin` / `Founder, Siraat`, onder elke primaire knop de friction reducer (US `Free shipping. 30-day returns. 100,000+ happy customers.`, INT `Free shipping, duties paid. 30-day returns. 100,000+ happy customers.`). Garantie als "covered for 75 years", retour als "30-day returns" (ongebruikt, binnen 30 dagen na levering), nooit "free returns", "lifetime", "risk-free" of levertijden. Reviews alleen letterlijk uit de shortlist (01-dr-research.md §5), bij de bouw controleren met `python3 -I research/copy/check_reviews.py`. Elke onderwerpregel hieronder is een van de vijf types; bij de bouw de overige drie per mail aanvullen (skill §5).

### Enquêtezinnen: exacte formulering die mag
Alleen deze, letterlijk, altijd als "our customers" (anoniem, geaggregeerd, 22,160 antwoorden):
- "68% of our customers say non-toxic is what matters most to them." (of afgerond: "About 7 in 10 of our customers...")
- "60% of our customers were already looking for PFAS-free cookware before they found us."
- (geschrapt: 41%-claim klopt niet, zie correctie bovenaan)
- "41% of our customers compared us with stainless steel before they bought."
- "About 1 in 5 of our customers buy Siraat as a gift."
- "15% of our customers almost didn't buy because they weren't sure titanium really works."
- "7 in 10 of our customers chose the Hammered Pan Pro." (held-product 71%)
- "Eggs are the first thing most of our customers cook." (eerste kookmoment nummer 1)
Popupzin uit de brief ("70% of our customers came for the same reason") wordt "About 7 in 10 of our customers came for the same reason: non-toxic cookware." Niet: "microplastics" als eigen claim, "your old pan is toxic" als kop.

### Gecontroleerde landingspagina's (curl, HTTP 200 op 8 nov 2026)
| URL (siraatskitchen.com) | Gebruik | Opmerking |
| --- | --- | --- |
| /collections/black-friday-sale | primaire knop tot 30 nov | zoals BF-W1 |
| /products/original-siraat-100-pure-titanium-pan-with-hammered-pattern | Pan Pro Standard | PDP noemt "scratch" en "lifetime" en een concurrent; niet aan ons, wel melden aan Floris |
| /products/titanium-hammered-pan-set-with-lids-6-pcs | 6-delige set | |
| /products/titanium-hammered-cookware-set-12-pcs-free-pizza-steel-1 | 12-delige set (alleen US) | |
| /products/titanium-hammered-pan-pro-mini, -small, -large | maatkiezer | |
| /products/titanium-hammered-deep-pan-pro, /products/titanium-hammered-wok-pan-pro | laatste mail | |
| /pages/third-party-testing | labrapport 25895 | schoon |
| /pages/non-stick-test | waterdruppeltest, ei | schoon, past op Performance |
| /blogs/compare/titanium-vs-stainless-steel-pans-pros-cons-and-best-use-cases | RVS-vergelijking | geen verboden woorden gevonden; voor gebruik één keer lezen |
| /pages/size-guide | maat kiezen (gift en maatkiezer) | schoon |
| /products/e-gift-card | cadeaubon $25, $50, $100, $200, digitaal | optielabels tonen nog euro-tekens (facts.csv): eerst laten herstellen |
| /pages/about-us, /pages/warranty | Benjamin, garantie | warranty-pagina noemt "lifetime" en "scratch": laten nakijken |
Niet gebruiken: /pages/stainless (nep-afteltimer "00 HR 00 MIN", nikkel/chroom-claim), /pages/the-gift-they-want-to-see-under-the-tree (verouderd "30,000+", "Michelin-starred chefs", "limited time"), /pages/6-reasons-why-this-is-the-safest-pan-for-me-and-my-family, /pages/loox-reviews (noemt de oude 100-dagenregel). /pages/take-our-quiz bestaat (lege pagina zonder script-inhoud in de HTML): navragen of dat een oude quiz is die met de popup botst.

**Cadeauverpakking:** niet gevonden op PDP, winkelwagen (cart.js heeft alleen het standaard notitieveld), FAQ, verzendbeleid en de cadeaupagina's. Dus niet noemen. Een cadeaubericht via de winkelwagennotitie: [VRAAG FLORIS] of het thema dat toont.

### 4.1 Tak NON-TOXIC (`non_toxic`, ook `family`): 6 mails
Pijler 1 "Non-toxic, for real". Bewijs eerst, geen angst.

| # | Wanneer | Doel | Onderwerp A / B | Preview | Hero | Kernboodschap | Bewijs | CTA en landing | Aanbod vooraan |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NT1 | 5 min | eerste order | A "You said no toxins. Here's the paper." B "Report no. 25895" | "Up to 70% off, 5 free gifts. No code needed." | Label NO PFAS / "You asked for no toxins.\|Here's the proof." Pan naast het labrapport, prijs en 70% OFF-tag eronder (US) | "About 7 in 10 of our customers came for the same reason." Wat erop zit (niets: pure titanium cooking surface, no coatings), hoe dat bewezen is (31 PFAS, alle onder de detectiegrens, ISO/IEC 17025). Vier productkaarten zoals BF-W1. | 68%-zin, Light Labs 25895, review R025 Sunny C. ("Getting rid of teflon for good."), 100,000+, 75 jaar, 30 dagen | "Get my PFAS-free pan" naar /collections/black-friday-sale, tekstlink /pages/third-party-testing | BF Sale + 5 gifts |
| NT2 | dag 1, 10:00 | begrip, klik naar PDP | A "What PFAS is (and where it hides in a pan)" B "Why we tested for 31 PFAS, not one" | "A short explainer. No scare stories." | Label THE SHORT VERSION / "PFAS in one minute" schema: coating op aluminium tegenover titanium oppervlak | Wat PFAS is in drie zinnen, waarom een coating de plek is waar ze zitten, en waarom "PFOA-free" niet hetzelfde is als PFAS-free. Rij "PTFE is itself a PFAS" alleen na akkoord Floris (comparisons.md A4); anders "Third-party tested by Light Labs" tegen "Testing varies by brand". Eén product: Pan Pro Standard. | 60%-zin, review R583 Scott Y. (coatings lieten los, "the last pans we ever have to purchase"), rapportnummer | "Show me the pan" naar de Pan Pro-PDP, secundair /pages/third-party-testing | BF in aanbodbalk, niet in de kop |
| NT3 | dag 3, 10:00 | vertrouwen (gedeeld) | A "The pan nobody else was making" B "December 20, 2024" | "Why I started with no coating at all." | Benjamin-brief, afzender Benjamin (wn2-structuur) | **Gedeelde Benjamin-mail** met openingsalinea voor `non_toxic`: "You told us you want the toxins out of your kitchen. That's exactly where I started." Daarna het vaste verhaal (titanium snijplanken, de originele gehamerde pan, eerste orders 20 december 2024, 100,000+ klanten). | 75 jaar, 100,000+, één eerlijke beperking (voorverwarmen) | "Get the pan I started with" naar Pan Pro-PDP | BF in P.S. en aanbodbalk |
| NT4 | dag 5, 09:00 | bewijs tegen twijfel | A "Has your cookware actually been tested?" B "Six things you can check yourself" | "Not the label. The paper." | W3-structuur, certificaat in beeld | Aangepaste W3 (VCjUYQ): zes controleerbare punten, maar met productkaart met prijs bovenaan (diagnose audit). | Light Labs, review R438 David H. als losse quote (4 sterren, niet in het 5-sterrenblok), R577 Thomas D. | "Get the tested pan" naar Pan Pro-PDP, tekstlink rapport | BF-kaarten |
| NT5 | dag 7, 09:00 | maat en set, orderwaarde (gedeeld) | A "Who are you cooking for?" B "15 coated pans, or one" | "Pick your size. Every size is in the sale." | Maatkiezer (wn4 US/INT) | **Gedeelde maatkiezer**. Opening voor `non_toxic`/`family`: "Swap the pan you use most first." Prijsbezwaar met waarde over tijd. | Reviews Michael G. en Tammy (zoals wn4), 75 jaar | "Find my size" naar /pages/size-guide of direct de kaarten | BF-kaarten met prijs (US), 70% OFF (INT) |
| NT6 | dag 10, 09:00 | laatste duw (gedeeld) | A "My last welcome email (and 70% off)" B "Tammy is on her fourth pan" | "Two promises, then I'll stop." | wn5 | **Gedeelde laatste mail**: "Where I'd start", Two promises (ongebruikt 30 dagen terug, kapot of defect: vervanging of terugbetaling, dan 75 jaar). P.S. per antwoord. Echte laatste mail is de enige urgentie. | Tammy R138, R017 Marilyn B. | "Start with the Pan Pro" naar PDP | BF |

Variant `family` (als Floris die knop wil): andere openingsalinea in NT1 en NT5 ("You're cooking for more than one."), geen claims over kinderen of gezondheid, review R563 Louise T. (dochter) in NT5.

### 4.2 Tak PERFORMANCE (`performance`, `switch`): 7 mails
Pijler 2 "Pure titanium performance". Belofte: werkt, als je het ritueel kent. Altijd de eerlijke beperking.

| # | Wanneer | Doel | Onderwerp A / B | Preview | Hero | Kernboodschap | Bewijs | CTA en landing | Aanbod vooraan |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PF1 | 5 min | eerste order | A "Why your last pan started peeling" B "The pan with no coating to peel" | "Up to 70% off, 5 free gifts. No code needed." | Label NO COATING / "Your coating gave up.\|This pan has none." Close-up gehamerd oppervlak, prijs en tag eronder | "41% of our customers told us their old pan's coating was peeling or wearing off." Een coating slijt, titanium heeft niets dat kan slijten; daarom 75 jaar. Kaarten zoals BF-W1. | 41%-zin, R583 Scott Y., 75 jaar, 100,000+ | "Get my pan" naar /collections/black-friday-sale | BF + 5 gifts |
| PF2 | dag 1, 10:00 | twijfel "werkt het" | A "The egg test (and the one rule that makes it work)" B "Cold metal grabs. Hot metal lets go." | "Medium heat, 2 to 3 minutes, one drop of water." | GIF van een ei dat glijdt (chef-media, `make_chef_media.py`) | **Eitest**: voorverwarmen op medium 2 tot 3 minuten, waterdruppel vormt een bolletje, theelepel olie, ei erin, niet bewegen. "Skip the heat, and it sticks." | 15%-zin ("weren't sure titanium really works"), "Eggs are the first thing most of our customers cook", R169 Michael G. (scepticus, ei gleed) of R069 Aggie M. | "Try the egg test myself" naar Pan Pro-PDP, tekstlink /pages/non-stick-test | BF in aanbodbalk |
| PF3 | dag 3, 10:00 | verschil met coating | A "Coated vs titanium, row by row" B "\"Makes all of our others 'non stick' seem really sticky.\"" | "Five rows. One of them is a tie." | Vergelijkingsblok `{{BLOCK:compare}}` tabel A (coated nonstick), rij 4 alleen na akkoord | **Coatingvergelijking**: pure titanium surface, geen coating om te slijten, metalen gerei mag, vaatwasser, labtest. | R577 Thomas D. (onderwerp B is letterlijk), Light Labs | "See the pan" naar Pan Pro-PDP | BF-kaart |
| PF4 | dag 5, 09:00 | verschil met RVS en gietijzer | A "Titanium vs stainless, honestly" B "41% of our customers compared us with stainless" | "Two rows where stainless ties. Three where it doesn't." | Tabel B (RVS) met twee eerlijke "same"-rijen; regel gietijzer (tabel C) eronder | **Vs stainless**: RVS is ook coatingvrij en PFAS-vrij (eerlijk), het verschil zit in loslaten en schoonmaken; gietijzer: geen inbranden, vaatwasser. | 41%-zin, R220 Carole (60 jaar koken, metalen spatel), R088 Chetan G. ("crispy output like a cast iron pan") | "Get the pan that lets go" naar Pan Pro-PDP, tekstlink naar de RVS-blog (gecontroleerd, niet /pages/stainless) | BF-kaart |
| PF5 | dag 7, 10:00 | vertrouwen (gedeeld) | A "The pan nobody else was making" B "December 20, 2024" | "Why I left the coating off." | Benjamin-brief | **Gedeelde Benjamin-mail**, opening `performance`: "You told us you want a pan that performs. I wanted one that keeps performing." | 75 jaar, eerlijke beperking | "Get the pan I started with" naar PDP | BF in P.S. |
| PF6 | dag 9, 09:00 | maat en set (gedeeld) | A "Who are you cooking for?" B "Every size is 70% off" | "Pick your size." | Maatkiezer | **Gedeelde maatkiezer**, opening: "Most people start with the pan they use every day." | Michael G., Tammy | "Find my size" | BF-kaarten |
| PF7 | dag 12, 09:00 | laatste duw (gedeeld) | A "My last welcome email (and 70% off)" B "\"I only need the new one.\"" | "Two promises, then I'll stop." | wn5 | **Gedeelde laatste mail**, P.S. performance: het ritueel in één zin. | R017 Marilyn B. (onderwerp B letterlijk), Tammy | "Start with the Pan Pro" | BF |

Subtak `switch` (overstappers van RVS of gietijzer): dezelfde zeven templates, volgorde PF1, **PF4 op dag 1**, PF2 op dag 3, PF3 vervalt of komt op dag 5 (een overstapper van RVS heeft geen coating om te vervangen), daarna PF5 t/m PF7. PF1 krijgt voor `switch` een andere kop via een if-blok: "You left coatings behind.|Now leave the sticking behind." Geen eigen templates nodig, alleen een extra split 2b.

### 4.3 Tak GIFT (`gift`): 5 mails plus 1 deadline-campagne
Pijler 4 "Made for people who love to cook". Kort, keuzehulp, nooit levertijden zonder akkoord.

| # | Wanneer | Doel | Onderwerp A / B | Preview | Hero | Kernboodschap | Bewijs | CTA en landing | Aanbod vooraan |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G1 | 5 min | eerste order | A "The gift they won't buy themselves" B "A gift that's covered for 75 years" | "Up to 70% off, 5 free gifts with your order." | Label FOR SOMEONE WHO COOKS / "The pan they'd never\|buy for themselves." Pan Pro in de hand, prijs en tag | "About 1 in 5 of our customers buy Siraat as a gift." Makkelijkste keuze: de Pan Pro Standard ("7 in 10 of our customers chose the Hammered Pan Pro"). Drie kaarten: Pan Pro, 6-delige set, 12-delige set (US). | 1-op-5-zin, R563 Louise T. (cadeau voor haar dochter), 75 jaar, 30 dagen, 100,000+ | "Pick their pan" naar /collections/black-friday-sale | BF + 5 gifts |
| G2 | dag 1, 10:00 | keuzehulp | A "Which pan for which cook?" B "For the one who cooks every night" | "Three cooks, three picks." | Drie personen (flitsstijl), elk met een product | **Cadeaugids per ontvanger**: de beginner (Mini of Small), de dagelijkse kok (Pan Pro Standard), de hele keuken (6- of 12-delige set). Maat twijfel: size guide. | R407 Emma (sceptisch, wil hem doorgeven aan haar zoon), Tammy (gaf er een aan haar zoon) | "Find the right one for them" naar de kaarten, tekstlink /pages/size-guide | BF-kaarten |
| G3 | dag 3, 10:00 | vertrouwen (gedeeld) | A "Why a pan is a better gift than it sounds" B "December 20, 2024" | "The story behind the box." | Benjamin-brief | **Gedeelde Benjamin-mail**, opening `gift`: "You're buying for someone else. Here's what you're actually giving them." | 75 jaar ("covered for 75 years"), 100,000+ | "Choose their gift" naar /collections/black-friday-sale | BF in P.S. |
| G4 | dag 5, 09:00 | twijfel over maat of tijd | A "Not sure of their size?" B "Let them choose (gift card)" | "A gift card works too. $25 to $200." | Cadeaubon-beeld (bestaand Shopify-beeld) | Twee routes: kies samen met de size guide, of geef de digitale cadeaubon ($25, $50, $100, $200). Pas na akkoord: de verzenddeadline (zie hieronder). | R563 Louise T. (andere zin dan G1) of R407 Emma | "Send a gift card" naar /products/e-gift-card, tweede knop "See the sizes" | geen kaarten, BF-regel |
| G5 | dag 8, 09:00 | laatste duw (gedeeld) | A "My last welcome email (and 70% off)" B "Tammy is on her fourth pan" | "Two promises, then I'll stop." | wn5 | **Gedeelde laatste mail**, P.S. gift: cadeaubon als uitweg. Two promises letterlijk (30 dagen gelden vanaf levering, zie risico). | Tammy | "Start with the Pan Pro" | BF |
| G-deadline | campagne op de door Floris bevestigde verzenddag | laatste kans voor levering voor kerst | A "Last day to order for Christmas (US)" B "Order today, it's under the tree in time" | "After today, the gift card is the safe bet." | Doos met strik alleen als er een echt beeld is | Echte deadline met reden en wat erna komt (skill §6): na vandaag de cadeaubon. | 100,000+, 30 dagen | naar /collections/black-friday-sale en /products/e-gift-card | sale of opvolger |

**Verzenddeadline.** Marketingmails noemen geen levertijden (skill §3); een kerstdeadline is dus een uitzondering die Floris in DECISIONS moet zetten. Het verzendbeleid zegt: verwerking binnen 1 werkdag, US 6 tot 10 kalenderdagen, de meeste andere landen 6 tot 10, Ierland en Denemarken 8 tot 14, "estimates only". Rekenvoorbeeld (geen advies, wel de orde van grootte): voor levering vóór 25 december in de US is bestellen uiterlijk rond 12 december nodig, INT rond 9 tot 10 december. [VRAAG FLORIS]: echte datum per markt en of ShipBob/Ecomflow die haalt in december.
Uitvoering: in de flow de deadlineregel tonen met een datumvoorwaarde (de Django-tag `now` staat op de allowlist, PLAYBOOK 12; eerst in een Klaviyo-preview bevestigen) en daarnaast één campagne op de deadline naar segment `siraat_goal = gift` en geen order sinds aanmelding. Na de deadline toont G4 alleen de cadeaubon.
**Cadeauverpakking:** bestaat niet op de site, dus niet noemen.

### 4.4 Gedeelde mails en hergebruik
| Gedeeld onderdeel | Bron | Per antwoord verschilt |
| --- | --- | --- |
| Benjamin-brief (NT3, PF5, G3) | wn2 (W2, VjPTKM) | één openingsalinea via `{% if person|lookup:'siraat_goal' == ... %}`, P.S. |
| Maatkiezer (NT5, PF6; G2 is een eigen variant) | wn4-us/int | openingszin |
| Laatste mail "Two promises" (NT6, PF7, G5) | wn5-us/int | P.S. en review |
| Aanbodblok (alle mails) | BF-W1 en `make_welcome.py` | niets; één wissel op 1 dec |
| W0 (bestaande klant) | TPiMrZ | niets, staat vóór de split |
| Terugvaltak | BF-W1, BF-W2, BF-W3, wn-staart | niets (huidige reis) |

### 4.5 Schema in één tabel
| Dag | Non-toxic (6) | Performance (7) | Switch (zelfde 7) | Gift (5 + campagne) | Terugval (huidig) |
| --- | --- | --- | --- | --- | --- |
| 0 (5 min) | NT1 papier + kaarten | PF1 coating bladdert | PF1 met switch-kop | G1 cadeau + kaarten | BF-W1 |
| 1 | NT2 PFAS uitgelegd | PF2 eitest | PF4 vs RVS/gietijzer | G2 cadeaugids | BF-W2 |
| 2 | | | | | BF-W3 |
| 3 | NT3 Benjamin (gedeeld) | PF3 coatingvergelijking | PF2 eitest | G3 Benjamin (gedeeld) | staart wn2 (na de A/B uit de audit) |
| 5 | NT4 getest? | PF4 vs RVS/gietijzer | PF3 (optioneel) | G4 maat of cadeaubon | wn3 |
| 7 | NT5 maatkiezer (gedeeld) | PF5 Benjamin (gedeeld) | PF5 Benjamin | | wn4 |
| 8 | | | | G5 laatste (gedeeld) | |
| 9 | | PF6 maatkiezer (gedeeld) | PF6 maatkiezer | | wn5 |
| 10 | NT6 laatste (gedeeld) | | | | |
| 12 | | PF7 laatste (gedeeld) | PF7 laatste | | |
| datum | | | | G-deadline (campagne) | |

## 5. Verwachte impact (schatting, geen meting)

Basis (sectie 1): ~$3.89 per aanmelder over de reis ($3.12 W1, $0.77 staart). Ongeveer 6,500 aanmelders per week (audit) is ~$25,300 per week uit de welkomreis.

Aannames:
- **W1 per antwoord: +10 tot +20%.** McKinsey noemt 10 tot 15% voor personalisatie in het algemeen; de huidige W1 opent al met non-toxic, dus voor de grootste groep is de winst klein, voor gift en performance groter. De bureaucase ($1.65 naar $4.51) is zelfgerapporteerd en begon lager; die neem ik niet over.
- **Staart: +30 tot +60%** ($0.77 naar $1.00 tot $1.23 per aanmelder), omdat elke mail een eigen argument plus product met prijs krijgt (icelolly +47% per mail als referentie). Overlapt met de wn-test uit de audit: niet allebei optellen.

| Scenario | W1 | Staart | Per aanmelder | Per week (6,500) |
| --- | ---: | ---: | ---: | ---: |
| Nu | $3.12 | $0.77 | $3.89 | $25,300 |
| Voorzichtig | $3.43 | $1.00 | $4.43 (+14%) | $28,800 (+$3,500) |
| Optimistisch | $3.74 | $1.23 | $4.97 (+28%) | $32,300 (+$7,000) |

Wat de schatting kan omgooien:
- **Aanmeldratio van de popup.** Een vraag vóór het e-mailveld kan aanmeldingen kosten of opleveren (leveranciers melden vooral winst, onafhankelijk bewijs is er niet). Elke 5% minder aanmelders kost ongeveer $1,300 per week en vreet de voorzichtige winst grotendeels op. Daarom is de popuptest stap 1.
- **Verdeling van de antwoorden.** Als 70% `non_toxic` kiest, lijkt die tak sterk op de huidige reis en is de extra winst vooral in gift en performance. Dat is prima, maar het verwachte effect zit dan dichter bij het voorzichtige scenario.
- **Uitschrijving.** Doel: W1 per tak onder de huidige 1.85%.
- Black Friday vertekent alles (BF-W1 $3.31 tegen een normale maand). Herhaal de vergelijking in januari.

## 6. Implementatieplan

### Volgorde
1. **Voorbereiding (Floris, 1 tot 2 dagen).** Alia: popupvariant B met de vraag (vier knoppen), antwoord als profieleigenschap; met een testprofiel bevestigen hoe de eigenschap heet en hoe snel hij in Klaviyo staat (moet binnen de 5 minuten wachttijd). Besluiten: rij "PTFE is itself a PFAS", kerstdeadline per markt, aanbod na 30 nov, wel of geen `family`.
2. **Fase 1, zo snel mogelijk vóór de BF-piek: alleen W1 per antwoord.** NT1, PF1, G1 (US en INT) bouwen op de BF-W1-structuur. De nieuwe flow (één trigger, split zoals sectie 3) laat na W1 iedereen de huidige reis volgen (BF-W2, BF-W3, staart). W1 levert 80% van de omzet van de reis; hier zit dus de meeste winst met het minste werk. Rn556d, T4a5Mk en YqKCmH krijgen de overgangsfilter en gaan daarna op Draft (PLAYBOOK 7).
3. **Popuptest A/B in Alia**, 50/50, handmatig, Smart Testing uit, naast of na de lopende triggertest (niet tegelijk twee variabelen in dezelfde popup: eerst de triggertest afronden of de quiz alleen in de winnende trigger testen). Primair: aanmeldingen per sessie en omzet per aanmelder binnen 14 dagen op profielniveau (`alia_popup_name`). A gaat vanzelf naar de terugvaltak.
4. **Fase 2: tak Non-toxic volledig** (grootste groep, snelst meetbaar), dan **Gift** uiterlijk eind november zodat G4 en de deadline-campagne vóór de kerstdeadline draaien, dan **Performance** met de switch-volgorde (begin december).
5. **Na 30 nov:** het aanbodblok wisselen in alle takken in één keer (bouwvariabele), angle-inhoud blijft.
6. **Testen binnen de takken** (pas na 4 weken stabiel): onderwerpregels per W1 (één variabele, winnaar op unieke kliks, dan omzet per ontvanger).

### Meten
- Popup: aanmeldingen per sessie per arm (niet per weergave), omzet per aanmelder na 14 en 30 dagen.
- Takken: flow-values-report per `flow_message_id`, plus per tak "omzet per profiel dat de split binnenkomt" (hulpsegment per `siraat_goal`, zoals WXWtRc in de audit).
- Eerlijk over de steekproef: bij ~1.5% orders per aanmelder is een verschil van 25% in orders pas met ~16,000 profielen per arm zichtbaar, dus maanden. Beslis op kliks en omzet per ontvanger als leidende signalen, en bewaak uitschrijving (> 1% is een probleem) en spam (> 0.157%).
- Optioneel, na de BF-periode: binnen de quizantwoorders 20% naar de terugvaltak (profile-sample) om het effect van de mails los te zien van het effect van de popup.

### Templates: hergebruik en nieuw
| Soort | Templates | Aantal bronnen | Met US/INT |
| --- | --- | ---: | ---: |
| Nieuw | NT1, NT2, PF1, PF2, PF3, PF4, G1, G2, G4, G-deadline (campagne) | 10 | ~16 (W1's, PF4, G1, G2 hebben prijzen; NT2, PF2, PF3, G4 één versie met marktmacro's) |
| Aangepast | NT4 (uit W3 VCjUYQ), Benjamin-brief (uit wn2, met if-blokken), maatkiezer (wn4 US/INT, openingszin), laatste mail (wn5 US/INT, P.S.) | 4 | 7 |
| Ongewijzigd | W0, BF-W1, BF-W2, BF-W3, wn-staart (terugvaltak) | 0 | 0 |
| **Totaal werk** | | **14 bronnen** | **~23 HTML-bestanden** |
Bouwen met `klaviyo/templates/v3/flows-nov/welcome/_tools/make_welcome.py` (helpers, vaste header en footer, productcard-blok, aanbodvariabele), QA-poort `qa_render.py`, review-check, `grep -c` op streepjes, en een rij in Figma (DECISIONS 4 nov).

### Risico's
1. **Race tussen lijst en eigenschap.** Komt het antwoord na de split binnen, dan gaat de quizbeantwoorder naar de terugvaltak. Geen schade, wel verdunning. Meten: aandeel profielen met `siraat_goal` in de terugvaltak; boven 5% de wachttijd naar 10 minuten.
2. **Dubbele mails in de overgang** met Rn556d/YqKCmH/T4a5Mk. Oplossing: overgangsfilter en de oude flows na uitloop op Draft, nooit archiveren.
3. **Claims.** NT2 kan richting gezondheidsclaim schuiven; geen ziekte, geen kinderclaims, "PTFE is a PFAS" alleen na akkoord. PF4 noemt geen merken. Landingspagina's met verouderde claims niet gebruiken (lijst in 4).
4. **Retour bij cadeaus.** 30 dagen gelden vanaf levering; een cadeau dat op 12 december aankomt ligt op 25 december nog onder de boom. [VRAAG FLORIS]: verlengde retourtermijn voor de feestdagen, anders in de gifttak "unused" en "30 days from delivery" heel duidelijk houden.
5. **Cadeaubon** toont euro-tekens in de optielabels: eerst laten herstellen, anders G4 zonder link naar de bon.
6. **Te veel takken voor het volume.** Gift (ongeveer 1 op 5) en switch zijn klein; daarom switch als volgorde binnen Performance en `family` binnen Non-toxic.
7. **Twee popuptests tegelijk** (trigger en quiz) maken beide onleesbaar: één tegelijk.
8. **Uitschrijving op dag 0 en 1** zit nu al boven 1%: per tak bewaken, de quiz mag het niet verergeren.

### Open vragen voor Floris
1. Naam en waarden van de eigenschap in Alia (`siraat_goal`: `non_toxic`, `performance`, `switch`, `gift`), en wel of geen `family`.
2. Akkoord op rij "PTFE is itself a PFAS" (NT2, PF3).
3. Kerstdeadline per markt, en of die in flowmails mag (uitzondering op "geen levertijden").
4. Aanbod vanaf 1 december.
5. Retourtermijn voor cadeaus in december; cadeaubericht via winkelwagennotitie.
6. Wat is /pages/take-our-quiz en moet die weg of naar de nieuwe quiz verwijzen?
