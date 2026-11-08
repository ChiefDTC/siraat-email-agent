# Quiz-popup: wat is de volgende stap na de klik? (8 nov 2026)

Rol: OFFER- EN COPYONTWERPER. Vraag van Floris: wat krijgt de klant na het antwoord op "What made you look today?". Een korting per antwoord, of iets anders?
Gelezen: BRIEF.md, ADVIES.md, strategie.md, copy.md, meten-ab.md, welkomflow-per-angle.md (deze map), DECISIONS.md, PLAYBOOK.md, CLAUDE.md, skill siraat-direct-response, de ruwe surveytelling (`2026-11-05_01_post-purchase-survey.md`, upload coördinator), `content/facts/` en `content/catalog/products.json`. Site alleen gelezen (products.json, PDP's, pagina's, 8 nov). Niets aangepast in Alia, Klaviyo of Shopify. Niet gecommit.
Bestanden: dit document, `next-step-copy.json` (alle copy, gestructureerd), `mock/index.html` plus `mock/mock-overview.png` (mobiele mocks, 375 px).

## 0. Advies in één alinea

**Geen korting per antwoord. Iedereen krijgt hetzelfde aanbod (5 free gifts, geen code), en elk antwoord krijgt een eigen volgende stap: het juiste bewijs, het juiste product en één tik na de aanmelding.**
- PFAS: het labrapport (report no. 25895) en de pan die getest is, Hammered Pan Pro Standard 11″.
- Afbladderen: een eerlijke uitleg "hoe krijg je het ei goed" (voorverwarmen, waterdruppel, olie) en een maatkeuze in één tik. Geen grotere belofte.
- RVS/gietijzer: de keuze "één pan of de hele stapel", met de 6-delige set (3 pannen en 3 deksels) als tweede optie.
- Cadeau: "Who's it for?" in één tik (Standard, 6-delige set of cadeaubon $20 tot $200), plus de retourregel. Een verzenddeadline alleen als Floris die bevestigt.
De extra tik zit altijd **na** het e-mailveld, in het succesvenster. Dan kost hij geen aanmeldingen. Een nieuwe korting is alleen een **besluit voor Floris** (sectie 3), en dan voor iedereen gelijk en als aparte test.

## 1. Correcties op de eerdere stukken (ruwe surveytelling)

De coördinator heeft de ruwe tellingen gedeeld. Daaruit volgen correcties die ook in copy.md, strategie.md en welkomflow-per-angle.md moeten:

| Wat eerder stond | Wat de ruwe data zegt | Wat ik gebruik |
| --- | --- | --- |
| "41% coating wears off" (open vraag) | Open vraag n=760 (25 sep tot 7 nov 2025): **Sticking 34.1%**, Toxic/PFAS 29.9%, Health 15.8%, **Coating peels/scratches 14.5%** | Geen 41%-zin meer. Voor "peeling": "Sticking was the frustration our customers named most with their old pans: about 1 in 3." (259 van 760) of een letterlijk anoniem antwoord |
| Non-toxic ~70% | "Toxin-Free Cookware" 3,448 van 4,930 = **69.9%** (16 mrt tot 14 mei 2026) | "7 in 10 of our customers told us toxin-free cookware mattered most to them." |
| 60% zocht al | 2,176 van 3,602 = **60.4%** (3 feb tot 16 mrt 2026) | "6 in 10 of our customers were already searching for non-toxic, PFAS-free cookware before they found us." |
| Stainless 41% | 2,733 van 6,662 = **41.0%** (7 nov tot 3 dec 2025) | "4 in 10 of our customers seriously compared us with stainless steel before choosing Siraat." |
| Cadeau "1 op 5" | 1,611 van 8,709 = **18.5%, alleen 7 nov tot 3 dec 2025**. Buiten het seizoen 1.7% ("Its a gift", n=4,930) | "Almost 1 in 5 of our customers bought Siraat as a gift last holiday season." Nooit zonder "holiday season" |

Meer uit de data die de keuze stuurt:
- **Kleven is de grootste verwachtingsfout.** Sticking is ook de nummer 1 klacht in advertentiereacties (12.5%), bij 8.5% van de ticketafzenders en in 1-ster Trustpilot over eieren. Gebruikte pannen kunnen niet terug, en kleven is geen defect (facts.csv, Gorgias 5302114). Dus voor het antwoord "My non-stick keeps peeling" nooit "eggs slide" of "nothing sticks" beloven. De officiële FAQ-zin is: "A hammered titanium surface is naturally low-stick, not zero-stick like Teflon." (PDP-FAQ, gelezen 8 nov). In de popup schrijf ik "not zero-stick like a coated pan", zodat er geen merknaam staat.
- **Maat** is 15.0% van "what almost stopped you" (451 van 2,997). Een maatkeuze is de sterkste micro-stap.
- **Deksel**: 10.3% van de tickets noemt een deksel. Op de site: de pan wordt los verkocht, deksel $59 apart; de 6-delige set heeft 3 deksels; "Pan Pro With Lid" is uitverkocht; "2 Pans + 2 Lids" $249 is alleen US. Daarom is de 6-delige set de tweede keuze in de RVS- en cadeautak.
- **Bestedingen per antwoord zijn bijna gelijk**: gemiddelde order "A gift" $207 tegen "Myself" $208; "Toxin-Free" $228 tegen "Effortless non stick" $224 (sectie 3 van de telling). Een cadeaukoper hoeft dus geen grotere korting om evenveel te besteden.
- **Publiek**: ongeveer 70% van de Meta-aankopen is 45+, 24 tot 29% is 65+. Mocks gebruiken 16 tot 17 px tekst, knoppen van 56 px hoog en hoog contrast. Geen claim over gewicht (staat niet in claims.csv).

## 2. De opties vergeleken

Producten en prijzen gecontroleerd op siraatskitchen.com (products.json en PDP, 8 nov 2026, USD): Pan Pro Standard 11″ $149 (compare-at $485), Mini 8″ $99, Small 10″ $144, Large 12″ $154, 6-delige set $299 (Mini, Small, Large plus 3 deksels; compare-at $997), Stainless Steel Lid $59, 12-delige set $649 (US), Gift Card $20, $25, $50, $100, $200. Pagina's met HTTP 200: /pages/third-party-testing, /pages/non-stick-test, /pages/size-guide, /products/e-gift-card, /collections/titanium-pans. **In de popup staan geen prijzen**: Alia is statisch, de saleprijs verandert na 30 nov en flashprijzen verzinnen mag niet. Prijzen alleen in W1 via de catalogusmacro's.

Rekenbasis marge (research/snowball/04-commissie-economie.md, 21 sep tot 20 okt): bruto per order $249.90, bijdrage na kostprijs, verzending en betaling $139.40 per order. Welkomstinstroom ~6,500 per week, ~11% koopt binnen 30 dagen, dus ~715 orders per week uit popup-aanmelders (schatting).

| Optie | Verwacht effect (schatting) | Margerisico | Complexiteit Alia/Klaviyo | Past bij besluiten | Meetbaarheid |
| --- | --- | --- | --- | --- | --- |
| **1. Zelfde aanbod, alleen framing per antwoord** (kop, bewijsregel) | Klein: 0 tot +5% omzet per bezoeker in de quizarm. Voor ~70% (non-toxic) verandert er bijna niets, want de huidige boodschap is al PFAS | Geen | Laag: 4 resultaatschermen, W1 met if-blokken | Volledig | Goed: quizarm tegen controle |
| **2. Ander voorop-product of bewijs per antwoord** (rapport + Pan Pro, eitest + maat, set met deksels, cadeaukiezer) | Middel: +3 tot +10% bovenop optie 1 (schatting; eigen data: relevantie in het eerste scherm is de enige personalisatie die werkt, BF-W1 $3.31 tegen staart $0.31; McKinsey 10 tot 15% voor personalisatie algemeen). De set in RVS/cadeau kan de orderwaarde verhogen | Geen korting. Licht positief als meer mensen de set kiezen | Middel: 4 succesvensters met knoppen per antwoord, UTM per knop | Volledig | Klikken per knop via `utm_content`; effect zit in de quizarm, niet los te testen |
| **3. Andere korting per antwoord** (bijv. cadeau 15%, rest 10%) | Meer aanmeldingen mogelijk, maar bezoekers kiezen dan het antwoord met de grootste korting. `siraat_goal` wordt onbruikbaar en de welkomtak klopt niet meer | Hoog. 10% extra op alle popup-orders kost ~$25 per order (18% van de bijdrage); break-even pas bij +22% orders. ~$17,900 per week als er geen extra orders komen | Hoog: 4 Shopify-codes of 4 Klaviyo-coupons, code per Alia-stap, codeweergave in W1 | **Botst** met DECISIONS 31 okt (BF-code alleen in abandonment) en met ADVIES (geen code op het bedankscherm). Twee variabelen in één test (vraag en aanbod) | Slecht: elk verschil kan van de korting of van de zelfselectie komen |
| **4a. Micro-stap vóór het e-mailveld** (maat of mini-uitslag "your match") | Kost aanmeldingen: Rejoiner van twee naar drie stappen min 30% relatief; Popupsmart: winst van multi-step verdwijnt als je alleen ingevulde e-mails telt | Geen | Middel | Past, maar de popup wordt langer | Stapuitval in Alia |
| **4b. Micro-stap ná het e-mailveld** (in het succesvenster) | Positief: maat is 15% van de twijfel; de tik brengt de bezoeker direct naar de juiste PDP, waar 60% van de popupkopers binnen 10 minuten koopt | Geen | Laag tot middel: knoppen met link in het succesvenster | Volledig | Klik per tik (UTM), orders per landing in Shopify/Triple Whale |
| **5. Garantie of risico-omkering per antwoord** (alleen bestaand beleid anders verwoord) | Klein, wel steun voor twijfel: non-toxic = het rapport; peeling = "covered for 75 years" (tegen defecten); RVS = 30 dagen retour; cadeau = retour "unused, counted from delivery" | Geen, mits eerlijk. Risico zit in de belofte: kleven valt niet onder garantie en gebruikt is niet retour | Laag (alleen tekst) | Past, mits geen "free returns", "risk-free", "lifetime" | Niet apart meetbaar |

Webonderzoek (zero-party data en quizaanbod):
- Er is **geen gepubliceerde test van "aanbod per antwoord" tegen "zelfde aanbod"**. Wat er is, komt van leveranciers zonder controlegroep: kortingen aan het eind van een quiz zouden beter werken dan dezelfde korting in een banner (RevenueHunt, zonder data). [RevenueHunt](https://revenuehunt.com/product-quiz-discounts/), [Visual Quiz Builder](https://www.visualquizbuilder.com/post/how-quiz-results-drive-smarter-dynamic-pricing-ecommerce)
- **Kortingsdiepte**: Recart (klanttest, 10% tegen 15%) meldt +5.6% omzet per bezoeker voor 15%, de winst op brutomarge staat niet in het fragment. Recart's no-popup-holdout: beste kortingspopup +7% omzet per bezoeker maar slechts +2% brutowinst per bezoeker (True Classic). Claspo (via podcast): 1 tot 10% converteert ~7%, 11 tot 15% ~6%, lagere kortingen geven betere omzet per bezoeker. Les: een diepere korting koopt vooral aanmeldingen, niet winst. [Recart 10 vs 15](https://blog.recart.com/10-vs-15-discount-which-offer-increased-revenue-per-visitor/), [Recart no-popup test](https://recart.com/laboratory/no-popup-vs-discount-popup-incrementality-test), [eCommerce Fastlane ep. 477](https://ecommercefastlane.com/podcast/episode-477/), [ep. 492](https://ecommercefastlane.com/podcast/episode-492/)
- **Korting en klantwaarde**: Klaviyo (7 A/B-tests) ziet meer herhaalkopers per weergave bij formulieren met korting; een Recharge-analyse ziet positieve 12-maandswaarde bij 1 tot 10% en negatieve bij 25% en meer. [Klaviyo](https://www.klaviyo.com/blog/discounts-on-signup-forms), [eCommerce Fastlane](https://ecommercefastlane.com/the-first-order-discount-sweet-spot-for-cpg-subscription-brands-is-deeper-than-you-think/)
- **Productaanbeveling na een quiz** (leverancierscases, geen controle): Geologie quiz naar aankoop 9% naar 13%, Wicked Edge AOV +61%, JOTT cadeauquiz add-to-cart +46%. Richting: de winst zit in het juiste product, niet in een extra korting. [Octane Geologie](https://www.octaneai.com/case-studies/geologie), [Wicked Edge](https://octaneai.com/customers/wicked-edge), [JOTT/Quizell](https://www.casestudies.com/company/quizell/case-study/jott-boosts-conversions-5-with-quizell)
- **Cadeauquizzen** vragen vrijwel altijd eerst naar de ontvanger. [Digioh](https://www.digioh.com/blog/interactive-gift-guide-quiz)
- Stappen en afhaken: zie strategie.md sectie 4 (Rejoiner, Popupsmart, Omnisend).
Let op: recart.com en blog.recart.com zijn in deze omgeving niet te openen; de Recart-cijfers komen uit zoekresultaten, niet uit de volledige pagina.

## 3. Aanbeveling en besluiten voor Floris

**Aanbeveling: optie 2 + 4b + 5 (framing), aanbod gelijk.** Waarom:
1. Het aanbod gelijk houden is de enige manier om de quiz eerlijk te testen (meten-ab.md 4.1) en om `siraat_goal` betrouwbaar te houden. Met een korting per antwoord kiest men het antwoord, niet de reden.
2. Prijs is wel het grootste bezwaar (27.2%), maar dat is geen angle-vraag: het geldt voor iedereen. Hoort dus in een aparte aanbodtest, voor iedereen gelijk.
3. De echte twijfels per antwoord (werkt het, welke maat, deksel, past het als cadeau) los je op met informatie en één tik, niet met geld.
4. Alles past binnen de besluiten: geen BFCODE in de popup, 5 gifts, geen flashprijzen, geen nieuwe beloftes.

**Besluit voor Floris 1 (alleen als hij toch een korting wil): één extra korting voor iedereen in de quizarm, niet per antwoord.**
| Bedrag | Kosten per popup-order | Bijdrage per order | Nodig om quitte te spelen | Kosten per week zonder extra orders |
| --- | ---: | ---: | ---: | ---: |
| 5% | $12.50 | $139.40 naar $126.90 | +9.9% orders | ~$8,900 |
| 10% (zoals HI10) | $25.00 | naar $114.40 | +21.9% orders | ~$17,900 |
| 15% | $37.50 | naar $101.90 | +36.8% orders | ~$26,800 |
Basis: bruto $249.90 en bijdrage $139.40 per order (sep tot okt), ~715 popup-orders per week (schatting), codes stapelen op de sale (DECISIONS 19 okt). Advies: niet tijdens BFCM (botst met 31 okt), en pas na de quiztest als eigen A/B (5 gifts tegen 5 gifts + 10%).

**Andere besluiten voor Floris (niet zelf ingevuld):**
2. Verzenddeadline voor kerst in de cadeautak ("Order by [DATUM FLORIS] for delivery before December 25 (US)"). Uitzondering op "geen levertijden in marketing". Datum per markt.
3. Retour voor cadeaus: 30 dagen gelden vanaf levering. Een cadeau dat op 12 december aankomt, is op 11 januari buiten de termijn. Verlengde termijn voor decemberorders, ja of nee.
4. Retourregel in de popup: de standaard friction reducer zegt "30-day returns" zonder "unused". Mag dat zo blijven, of overal "30-day returns on unused items"? "Hassle-free" gebruik ik niet. In de cadeautak staat "unused, counted from delivery" al expliciet.
5. Cadeaubericht of gift receipt: niet gevonden op de site; dus niet beloofd. Wil Floris de winkelwagennotitie als cadeaubericht tonen?
6. Aanbod vanaf 1 december: blijven de 5 gifts? De test start 2 dec. Alleen `offer_us`, `offer_int` en `gift_list` in de JSON wisselen.
7. Cadeaubon: optielabels toonden eerder euro-tekens (facts.csv). Op 8 nov geeft products.json $20 tot $200; even in de winkel controleren.
8. Officiële regels voor de filtertrekking (link in de kleine letters).

## 4. Copy per antwoord (Engels)

Volledig en gestructureerd in `next-step-copy.json`. Gedeeld op elk resultaatscherm:
- Aanbod US: "5 free gifts with every order ($555 value)." INT: "5 free gifts with every order." Gifts: "Mystery gift, free shipping, Plastic-free e-book, Favorites cookbook, and a chance to win a PFAS water filter."
- E-mailveld: "Your email address". Friction US: "Free shipping. 30-day returns. 100,000+ happy customers." INT: "Free shipping, duties paid. 30-day returns. 100,000+ happy customers." Link: "No thanks".
- Kleine letters: "By signing up you agree to receive marketing emails from Siraat. Unsubscribe anytime. PFAS water filter: weekly draw, see official rules."
- Succesvenster onderaan: "No code needed. Your 5 gifts are added at checkout."

### Vraagscherm
ONE QUICK QUESTION / **What made you look today?** / "Tap one. We'll show you where to start." / vier knoppen (Floris) / link "Skip, just show me the gifts".

### 4.1 "I want PFAS out of my kitchen" (`non_toxic`)
Volgende stap: het labrapport en de geteste pan (Pan Pro Standard 11″).

| | A rationeel | B emotioneel |
| --- | --- | --- |
| Label | NO PFAS. ON PAPER. | YOU WERE ALREADY LOOKING |
| Kop | No coating. No PFAS. Here's the paper. | Stop wondering what's in your pan. |
| Bewijs | 7 in 10 of our customers told us toxin-free cookware mattered most to them. | 6 in 10 of our customers were already searching for non-toxic, PFAS-free cookware before they found us. |
| Mechanisme | A pure titanium cooking surface with no coatings. Light Labs tested it for 31 PFAS, and every one came in below the detection limit (report no. 25895). | There's no coating on ours, so there's nothing to wear off and nothing to wonder about. No PFAS, PFOA, or BPA. |
| Aanbod/stap | Get the full lab report in your inbox, plus 5 free gifts with every order ($555 value). | Get the lab report and 5 free gifts with every order ($555 value). |
| Knop | Send me the lab report | Show me the proof |
| Succes | **Check your inbox.** Report no. 25895 is in your first email, so you can read it yourself. Most people start with the pan we had tested. Knoppen: "Read the lab report now" (/pages/third-party-testing), "See the pan we tested" (Pan Pro Standard) | **One less thing to wonder about.** Your first email is on its way, with the lab report and the pan most people start with. Knoppen: "See the pan we tested", "Read the lab report now" |
| W1 onderwerp / preview | Report no. 25895, as promised / 31 PFAS tested. Every one below the detection limit. Your 5 gifts inside. | Has your cookware actually been tested? / Not the label. The paper. Plus your 5 free gifts. |

### 4.2 "My non-stick keeps peeling" (`performance`)
Volgende stap: eerlijk "zo krijg je het ei goed" plus maatkeuze. Geen "eggs slide", geen "nothing sticks".

| | A rationeel | B emotioneel |
| --- | --- | --- |
| Label | NOTHING TO PEEL | THE LAST PAN YOU REPLACE |
| Kop | No coating, so nothing to peel. | Done buying the same pan again? |
| Bewijs | Sticking was the frustration our customers named most with their old pans: about 1 in 3. | "Degrading non-stick coatings." One of our customers, word for word, on what was wrong with their old pans. |
| Mechanisme | Pure titanium, no coatings. It's naturally low-stick, not zero-stick like a coated pan: preheat on medium for 2 to 3 minutes, add a little oil, and let food sear before you move it. | Ours has no coating to wear thin, and it's covered for 75 years. Give it two minutes of heat first. That's the whole trick. |
| Aanbod/stap | Get the 2-minute egg guide, plus 5 free gifts with every order ($555 value). | Get the egg guide and 5 free gifts with every order ($555 value). |
| Knop | Send me the egg guide | Show me how it cooks |
| Succes | **Your egg guide is on its way.** The short version: medium heat for 2 to 3 minutes, until a drop of water beads and glides. Then a teaspoon of oil. Then the egg. Tik: "Which size do you cook with most?" 8″ Mini (eggs, sauces and sides), 10″ Small (everyday meals for two), 11″ Standard (best-seller, most people start here), 12″ Large (family meals, searing steaks). Knop "Watch the water-drop test" (/pages/non-stick-test) | **Good. Nothing left to peel.** Your first email shows you how to cook an egg on titanium, step by step. One thing first: dezelfde maattik |
| W1 onderwerp / preview | The egg test (and the one rule that makes it work) / Medium heat, 2 to 3 minutes, one drop of water. Your 5 gifts inside. | Cold metal grabs. Hot metal lets go. / Why titanium has nothing to peel, and the 2-minute heat trick. |

Maatomschrijvingen letterlijk uit de PDP-FAQ ("Which size should I get?"). Het bewijs in B is een anoniem surveyantwoord, letterlijk (skill 12: nooit een naam).

### 4.3 "Stainless and cast iron are too much work" (`switch`)
Volgende stap: "één pan of de hele stapel", met de 6-delige set (3 deksels) als tweede keuze.

| | A rationeel | B emotioneel |
| --- | --- | --- |
| Label | NO COATING, LESS UPKEEP | THE EASIER SWITCH |
| Kop | The no-coating pan, without the upkeep. | You wanted no coating. Not a chore. |
| Bewijs | 4 in 10 of our customers seriously compared us with stainless steel before choosing Siraat. | Stainless steel is what our customers compared us with most: 4 in 10 of them. |
| Mechanisme | Same rhythm as stainless: heat first, then oil. The difference comes after dinner. No seasoning, dishwasher safe, metal utensil safe. | No seasoning. Heat it for 2 to 3 minutes, add a little oil, and clean up in under a minute. |
| Aanbod/stap | We'll help you pick one pan or the set. Plus 5 free gifts with every order ($555 value). | Pick your first pan, or the set with lids. 5 free gifts with every order ($555 value). |
| Knop | Help me pick | Find my first pan |
| Succes | **Check your inbox.** Your first email puts titanium next to stainless, row by row. Where do you want to start? Tik: "Replace one pan, or the whole stack?" One pan to start (Hammered Pan Pro Standard, 11″) / The whole stack (6-piece set: 8″, 10″ and 12″ pans, each with a lid) | **Your first email is on its way.** It puts titanium next to stainless, row by row. Want a head start? Dezelfde tik |
| W1 onderwerp / preview | Titanium vs stainless, honestly / Two rows where stainless ties. Three where it doesn't. Your 5 gifts inside. | No coating, no seasoning, no fuss / Why stainless fans switch, and the 2-minute heat rule. 5 gifts inside. |

"Clean up in under a minute" is goedgekeurd (DECISIONS 5 nov, E5/E6).

### 4.4 "I'm shopping for a gift" (`gift`)
Volgende stap: "Who's it for?" in één tik, de retourregel, en de deadline alleen na akkoord.

| | A rationeel | B emotioneel |
| --- | --- | --- |
| Label | GIFTING THIS YEAR | FOR SOMEONE WHO COOKS |
| Kop | A gift that's covered for 75 years. | Give the pan they'd never buy themselves. |
| Bewijs | Almost 1 in 5 of our customers bought Siraat as a gift last holiday season. | You're in good company: almost 1 in 5 of our customers bought Siraat as a gift last holiday season. |
| Mechanisme | Pure titanium, no coatings. Dishwasher safe, and it works on gas, electric, ceramic and induction. | The original hammered titanium pan. Nothing on it to wear off, so it's still a good gift years from now. |
| Aanbod/stap | We'll help you pick the right one for them. Plus 5 free gifts with every order ($555 value). | We'll help you pick their size. And 5 free gifts with every order ($555 value). |
| Knop | Help me choose their gift | Find their pan |
| Succes | **Who's it for?** Tap one and we'll take you straight there. Your first email has the same picks. Tikken: Someone who cooks for one or two (Pan Pro Standard 11″) / A whole household (6-piece set, 3 pans and 3 lids) / Not sure what they'd like (Gift card, $20 to $200). Klein: "30-day returns on unused items, counted from delivery." Alleen na besluit 2: "Order by [DATUM FLORIS] for delivery before December 25 (US)." | **Let's find their pan.** Tap one and we'll take you straight there. Your first email is on its way too. Dezelfde tikken en regels |
| W1 onderwerp / preview | The gift they won't buy themselves / Which pan for which cook, 30-day returns, and your 5 gifts. | Who's on your list? / Three cooks, three picks. Plus 5 free gifts with every order. |

### 4.5 Overslaan ("Skip, just show me the gifts", `other`)
5 FREE GIFTS / **5 free gifts with every order.** / 100,000+ happy customers cook on Siraat. / giftlijst / e-mail / **Claim my 5 gifts** / friction. Succes: **Your 5 gifts are waiting.** Check your inbox for your welcome email. Knop "See the pans" (/collections/titanium-pans). W1: de huidige, ongewijzigd.

Controle op de regels: geen em of en dash (script, 0), geen lifetime, risk-free, free returns, purifier, unlock, journey; filter altijd "a chance to win"; $555 alleen US; geen code; geen prijzen in de popup; geen "eggs slide"; "covered for 75 years" in plaats van "lasts".

## 5. Uitvoering

### 5.1 Alia, scherm voor scherm (quizvariant, naast de controle)
1. **Vraag** (Mini Quiz, geen e-mailveld): 4 knoppen + tekstlink "Skip". Elke knop zet de eigenschap en gaat naar zijn eigen resultaatstap. Vraagtekst na livegang nooit meer wijzigen (wordt de naam van de eigenschap in Klaviyo).
2. **Resultaat per antwoord** (4 stappen, kopie van de huidige e-mailstap): label, kop, bewijs, mechanisme, gifts-strook, aanbod, e-mailveld, knop, friction, "No thanks", kleine letters. Skip gaat naar de huidige e-mailstap.
3. **SMS-stap**: alleen als de huidige popup die heeft, ongewijzigd.
4. **Succes per antwoord** (4 + skip): kop, tekst, tikknoppen of knoppen met link en UTM (`utm_source=alia&utm_medium=popup&utm_campaign=quiz_v1&utm_content=<antwoord>_<stap>&angle=<antwoord>`, staat per knop in de JSON).
Vormgeving: knoppen minimaal 56 px, tekst 16 px of groter. In de mock zijn de resultaatkaarten 680 tot 770 px hoog bij 375 px breed: op kleine telefoons (667 px) moet in Alia de kleine lettertekst kleiner of het mechanisme onder een "Why?"-regel. Eerst in de Alia-preview op een iPhone SE-formaat controleren.
Terugval als Alia niet per knop naar een eigen stap kan: één gedeelde e-mailstap (kop "Your 5 gifts are ready") en de personalisatie alleen in W1 (strategie.md 5).

### 5.2 Profieleigenschappen (sluit aan op meten-ab.md 3.1, met één wijziging)
| Eigenschap | Waarden | Regel |
| --- | --- | --- |
| `siraat_goal` | `non_toxic`, `performance`, `switch`, `gift`, `other` | Laatste antwoord. **Wijziging:** `replace_coating` uit meten-ab vervalt; Floris' antwoord "My non-stick keeps peeling" is `performance`, het RVS-antwoord wordt `switch`, overslaan is `other` |
| `siraat_goal_first` | zelfde codes | Alleen zetten als leeg |
| `siraat_goal_at` | datum | Tijdstip van antwoord |
| `siraat_goal_source` | `alia_quiz_v1` | Ophogen bij elke tekstwijziging |
| `siraat_goal_label` | knoptekst | Alleen controle |
Wat er na de aanmelding getikt wordt (maat, set, cadeaubon) komt niet als eigenschap binnen maar via de UTM in de URL (Shopify, Triple Whale, Klaviyo Active on Site). Geen extra Alia-veld nodig.
Vastleggen: bij voorkeur een verborgen veld of eigenschap per Alia-knop met de code. Lukt dat niet: een kleine Klaviyo-flow die op de Alia-eigenschap ("What made you look today?") splitst en per tak `siraat_goal` met een vaste waarde zet (meten-ab 3.2).

### 5.3 Hoe het aanbod in Klaviyo komt
- **Geen coupon, geen code per antwoord.** Het aanbod (5 gifts) wordt al automatisch in de winkelwagen toegevoegd.
- **W1 per antwoord**: één template met `{% if person|lookup:'siraat_goal' == '...' %}`-blokken voor onderwerp-overeenkomstige hero, eerste blok en volgorde van de productkaarten, of de split uit welkomflow-per-angle.md sectie 3. Aanbodblok, header en footer gelijk (vaste partials).
- Afwijking van welkomflow-per-angle.md: de `switch`-W1 opent met de RVS-vergelijking (`{{BLOCK:vs kind="steel"}}`) en de kaart van de 6-delige set, dus de inhoud van PF4 komt naar W1. De `performance`-W1 opent met de eitest (PF2-inhoud) in plaats van "Why your last pan started peeling", en gebruikt de FAQ-lijn "naturally low-stick, not zero-stick". Dat volgt uit de correctie in sectie 1.
- Elke W1-belofte uit het succesvenster moet in W1 staan: rapport (non_toxic), eitest (performance), RVS-tabel (switch), keuze per ontvanger (gift).

### 5.4 Wat Floris zelf moet doen
Alia:
1. Popup dupliceren als variant "Quiz v1 [trigger]" (eigen `alia_popup_name`), stappen zoals 5.1, copy uit de JSON. INT-variant zonder "$555 value".
2. Per knop een vaste eigenschapswaarde instellen, met een test@-profiel bevestigen hoe het in Klaviyo heet en hoe snel (moet binnen de 5 minuten wachttijd van de welkom).
3. Succesknoppen met de URL's uit de JSON.
4. 50/50, Smart Testing uit, start na de triggertest en na Cyber Monday (2 dec).
5. Mobiele preview op klein scherm controleren.
Shopify: niets verplicht (geen code). Alleen na besluit: verzenddeadline-tekst, cadeaubericht via notitie, verlengde retour, cadeaubonlabels.
Besluiten uit sectie 3.

### 5.5 Volgorde van werk
1. Floris: besluiten 2 tot 8 en de Alia-check (knop naar eigen stap, eigenschapsnaam). Deze week.
2. Correcties uit sectie 1 doorvoeren in copy.md, copy.json, strategie.md en welkomflow-per-angle.md (41%-zinnen eruit).
3. Alia-variant als concept bouwen tijdens de triggertest (geen verkeer).
4. W1-varianten bouwen (make_welcome.py, qa_render, review-check, streepjescheck, Figma-rij), na go van Floris.
5. Testprofielen door alle 5 takken, vastlegratio en vertraging meten.
6. 2 dec: quiztest 50/50, 21 dagen, besluit rond 12 jan (meten-ab 5 en 6). Klikken per succesknop wekelijks bekijken.
7. Januari: bij winst 90/10 met holdout. Cadeautak blijft, maar zonder deadlineregel; het cadeau-aandeel valt buiten het seizoen naar ~2%.
8. Pas daarna, als Floris dat wil: aparte aanbodtest (5 gifts tegen 5 gifts + korting), voor iedereen gelijk.

## 6. Mockups
`mock/index.html` toont het vraagscherm, de 8 resultaatschermen (A en B per antwoord), het overslaan-scherm en 9 succesvensters, elk als mobiele popup van 375 px in Siraat-stijl (ink #272727, crème #F4F1EA, geel alleen op de kleine "$555 VALUE"-tag, logo-lockup `siraat-lockup-black-email.png` gekopieerd naar `mock/assets/`, echte gift- en productbeelden uit `partials/shared`). Onder elk succesvenster staat apart de onderwerpregel van W1 (annotatie, geen deel van de popup). Screenshot: `mock/mock-overview.png` (Playwright). Gecontroleerd: geen horizontale scroll op 375 px, logo en beelden laden, knoppen 56 px.
