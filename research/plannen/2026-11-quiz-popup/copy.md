# Quiz-popup: copy per angle (concept, 8 nov 2026)

> **Correctie (8 nov 2026):** het cijfer "41% coating die afbladdert/slijt" uit de PDF-samenvatting klopt niet met de ruwe surveytelling. Ruwe open antwoorden (n=760): plakken 34.1%, toxisch/PFAS 29.9%, gezondheid 15.8%, coating bladdert/krast 14.5%. Gebruik voor de performance-angle geen 41%; zie next-step.md voor de juiste bewijsregels.


Rol: copywriter. Bron: `BRIEF.md`, skill siraat-direct-response, DECISIONS.md (5 gifts 7 nov, BF 31 okt), `.agents/product-marketing.md` en de surveyrapport-PDF (vraagteksten letterlijk gecontroleerd). Popup-copy in het Engels (US), notities in het Nederlands. Gestructureerde versie: `copy.json` (zelfde inhoud). Niets in Klaviyo of Alia aangepast, niet gecommit.

## Kort
- **Favoriete vraag: Q3 "What made you look today?"** Hij vraagt naar het moment, niet naar een identiteit, dus elk antwoord is makkelijk en eerlijk (ook "I'm shopping for a gift"). Hij past bij de koper die al zocht (60%) en vaak dezelfde dag koopt (38%), en de antwoorden zijn bijna letterlijk klanttaal ("peeling", "PFAS out of my kitchen"). Q1 is de veilige controle-vraag, Q2 de doelvraag.
- Elk resultaatscherm: label, kop, bewijsregel met echt surveycijfer, één regel mechanisme, het bestaande aanbod (5 gifts), e-mailveld, knop, frictieregel. Twee varianten per angle: A rationeel, B emotioneel.
- Alle bewijsregels zijn herschreven naar wat de vraag echt meet. Het voorbeeld "7 in 10 say non-toxic was their #1 reason" is net niet juist: de vraag was "What is most important for them?" (meerkeuze, ~70%), dus: "told us toxin-free cookware is what matters most to them". Zie tabel bewijs.

## Onderzoek: hoe sterke merken quiz-popups doen
Directe meting bij Caraway, GreenPan, HexClad, Our Place en Made In lukte niet: zoekresultaten tonen geen popup-copy en hun sites, wisepops.com en community.shopify.com zijn vanuit deze omgeving niet bereikbaar (zelfde beperking als in `research/popup/2026-11-trigger-test.md`). Wat wel vindbaar was, met de kanttekening dat de meeste cijfers van leveranciers zelf komen:
- **Meerstaps werkt beter dan een kale e-mailvraag, maar de winst verschilt sterk per bron.** Wisepops (1,8 mln sessies): meerstaps 5,64% tegen 3,07% enkelstaps; een latere Wisepops-ronde 5,17% tegen 4,62%; Omnisend 2026 2,3% tegen 2,0%. Zelf meten blijft nodig. ([Wisepops via zoekresultaat](https://wisepops.com/blog/micro-commitment-popups), [Crazy Egg popup statistics](https://www.crazyegg.com/blog/?p=109699), [Rejoiner](https://rejoiner.com/resources/email-capture))
- **Mechanisme is commitment.** Na een eerste klik is de e-mail een kleine volgende stap (OptiMonk). Een merchant op de Klaviyo-community meldt 3,5 tot 5% naar 8 tot 9% door een micro-commitment voor de vraag (anekdote, geen controlegroep). Een Shopify-community-test: e-mail als laatste in plaats van eerst gaf ongeveer het dubbele. ([OptiMonk multi-step](https://www.optimonk.com/features/multi-step-flows), [Klaviyo community](https://community.klaviyo.com/strategic-advice-27/idea-how-we-increased-our-new-visitor-form-sign-up-rate-by-60-3672), [Shopify community](https://community.shopify.com/t/we-tested-asking-for-the-email-last-instead-of-first-it-roughly-doubled-opt-ins-on-its-own/654027), [Justuno one-step vs two-step](https://www.justuno.com/blog/quick-video-optimizing-email-pop-ups-with-a-b-tests-one-step-opt-in-vs-two-step-opt-in/))
- **Function of Beauty** vraagt eerst naar haar en doelen, en vraagt de e-mail pas om de uitkomst te zien, met een aparte opt-in. Curlsmith (Octane AI): 89% voltooiing, 100.000+ aanmelders in 7 maanden. Desert Does It (OptiMonk): aanmeldratio verdubbeld met een quiz-popup. Leverancierscijfers. ([Visual Quiz Builder over Function of Beauty](https://www.visualquizbuilder.com/post/ecommerce-quiz-examples), [Curlsmith case](https://www.casestudies.com/company/octane-ai/case-study/how-curlsmith-gained-100k-email-subscribers), [Desert Does It](https://www.optimonk.com/desert-does-it-case-study), [Glossy over Function of Beauty data](https://www.glossy.co/new-face-of-beauty/how-function-of-beauty-used-customer-data-to-launch-a-new-shampoo))
- **De antwoorden zijn het waardevolst in de flow erna.** Farmers Defense (Amped) en Midnight Hour (Zaymo) sturen gesegmenteerde mails op basis van het antwoord. ([Amped Farmers Defense](https://amped.io/case-studies/farmers-defense), [Zaymo Midnight Hour](https://www.zaymo.com/case-studies/midnight-hour-turns-in-email-quizzes-into-zero-party-data/), [Digioh](https://www.digioh.com/blog/product-quizzes-collect-zero-party-data))
- **HexClad draait ook Alia** volgens een tech-tracker (niet bevestigd). Ritual: in de resultaten alleen app-listings, niet te bevestigen dat het het merk zelf is. ([brandsearch HexClad](https://brandsearch.co/brands/hexclad.eu))
- **Kanttekening uit de meetdata:** meerstaps verhoogt soms de data maar verlaagt het totaal aantal aanmeldingen. Daarom staat in elke vraag een overslaan-link naar het gewone aanbod, en meten we op aanmeldingen per sessie.

Wat ik daaruit heb overgenomen: (1) vraag eerst, e-mail daarna; (2) vijf korte antwoorden van 3 tot 7 woorden in klanttaal; (3) het resultaatscherm herhaalt hun keuze terug ("You were already looking"), dan bewijs, dan pas het aanbod; (4) altijd een uitweg zonder vraag.

## Gedeelde blokken (op elk resultaatscherm)
- Aanbod US: **5 free gifts with every order ($555 value)**. Mystery gift, Free shipping, Plastic-free e-book, Favorites cookbook, and a chance to win a PFAS water filter.
- Aanbod INT: **5 free gifts with every order** (geen bedrag, DECISIONS 7 nov).
- E-mailveld placeholder: "Your email address"
- Frictieregel onder de knop: "Free shipping. 30-day returns. 100,000+ happy customers."
- Kleine lettertekst: "By signing up you agree to receive marketing emails from Siraat. Unsubscribe anytime. PFAS water filter: weekly draw, see official rules."
- Codescherm zonder code (aanbevolen, zie open punt 1): "No code needed. Your 5 gifts are added at checkout."

## 1. Vraagscherm, drie varianten
### Q1: What brings you
- Kop: **What brings you to Siraat?**
- Subline: Pick one. We'll show you what fits.
- Knoppen:
  - "Non-toxic cookware, no coatings" → `non_toxic`
  - "My nonstick keeps peeling" → `performance`
  - "Moving on from stainless or cast iron" → `switch`
  - "Cooking for my family" → `family`
  - "It's a gift" → `gift`
- Link onder de knoppen: "Skip, just show me the gifts" → gewone gift-scherm (zie sectie 3)

### Q2: Main goal
- Kop: **What's your main goal?**
- Subline: One tap. Then your offer.
- Knoppen:
  - "Get coatings out of my kitchen" → `non_toxic`
  - "A pan that doesn't flake off" → `performance`
  - "Easier than stainless or cast iron" → `switch`
  - "Cook clean for my family" → `family`
  - "Find a gift that lasts" → `gift`
- Link onder de knoppen: "Skip, just show me the gifts" → gewone gift-scherm (zie sectie 3)

### Q3: What made you look
- Kop: **What made you look today?**
- Subline: Be honest. It changes what we show you.
- Knoppen:
  - "I want PFAS out of my kitchen" → `non_toxic`
  - "The coating on my pan is peeling" → `performance`
  - "Stainless and cast iron are hard work" → `switch`
  - "I cook for little ones" → `family`
  - "I'm shopping for a gift" → `gift`
- Link onder de knoppen: "Skip, just show me the gifts" → gewone gift-scherm (zie sectie 3)

Notitie: Q1 en Q2 gebruiken voor familie neutrale woorden ("Cooking for my family") zodat we niets suggereren over veiligheid van andere pannen. Q3 "I cook for little ones" is warmer; geen claim, wel een antwoordlabel. "Safer" bewust vermeden (vergelijkende veiligheidsclaim).

## 2. Resultaatschermen per angle (A rationeel, B emotioneel)
Opbouw per scherm: LABEL / kop / bewijsregel / mechanisme / aanbodregel + gedeeld aanbodblok / e-mailveld / knop / frictieregel / kleine letters. Daarna het bedankscherm.

### Non-toxic / health (`non_toxic`)
Bron cijfer: S6 (n=3,358) en S9 (n=1,675) 'What is most important for them?': toxin-free cookware ~70%. S8 (n=3,678): 60% zocht al actief naar non-toxic/PFAS-free.  
Link bedankscherm: https://siraatskitchen.com/pages/third-party-testing

**Variant A (rationeel)**
- Label: YOU'RE IN GOOD COMPANY
- Kop: **No PFAS. And the paper to prove it.**
- Bewijs: 7 in 10 Siraat customers told us toxin-free cookware is what matters most to them.
- Mechanisme: A pure titanium cooking surface with no coatings. Tested by Light Labs, report no. 25895: 31 PFAS compounds, every one below the detection limit.
- Aanbod: Here's your offer: 5 free gifts with every order ($555 value). Mystery gift, Free shipping, Plastic-free e-book, Favorites cookbook, and a chance to win a PFAS water filter.
- E-mailveld: "Your email address" / knop: **Claim my 5 gifts**
- Onder de knop: Free shipping. 30-day returns. 100,000+ happy customers.
- Bedankscherm: **Your 5 gifts are waiting** / Check your inbox. The first email has report no. 25895, so you can read it yourself. / Your code: BFCODE (of: "No code needed. Your 5 gifts are added at checkout.") / knop: Read the lab report

**Variant B (emotioneel)**
- Label: YOU WERE ALREADY LOOKING
- Kop: **You don't have to wonder what's in your pan.**
- Bewijs: 6 in 10 Siraat customers were already searching for PFAS-free cookware before they found us.
- Mechanisme: No coating means nothing on the surface to question. No PFAS, PFOA, or BPA.
- Aanbod: Here's what comes with your first order: 5 free gifts with every order ($555 value). Mystery gift, Free shipping, Plastic-free e-book, Favorites cookbook, and a chance to win a PFAS water filter.
- E-mailveld: "Your email address" / knop: **Send me my offer**
- Onder de knop: Free shipping. 30-day returns. 100,000+ happy customers.
- Bedankscherm: **That's one less thing to wonder about** / Your welcome email is on its way, with the full lab report inside. / Your code: BFCODE (of: "No code needed. Your 5 gifts are added at checkout.") / knop: Shop the Black Friday Sale

**Welkomstmail 1, teaser:** onderwerp A "Report no. 25895, as promised", onderwerp B "Has your cookware been tested?", preview "31 PFAS tested. Every one below the detection limit. Your 5 gifts inside."

### Performance / failing coating (`performance`)
Bron cijfer: S3 (n=776, open text, auto-grouped): coating/non-stick wearing off 41%, grootste frustratie met oude pannen.  
Link bedankscherm: https://siraatskitchen.com/collections/black-friday-sale

**Variant A (rationeel)**
- Label: NOTHING TO WEAR OFF
- Kop: **A pan with no coating can't peel.**
- Bewijs: 4 in 10 Siraat customers say their biggest frustration with their old pans was the coating wearing off.
- Mechanisme: Pure titanium cooking surface, no coatings. Nothing sticks when the heat is right. Covered for 75 years.
- Aanbod: Here's your offer: 5 free gifts with every order ($555 value). Mystery gift, Free shipping, Plastic-free e-book, Favorites cookbook, and a chance to win a PFAS water filter.
- E-mailveld: "Your email address" / knop: **Claim my 5 gifts**
- Onder de knop: Free shipping. 30-day returns. 100,000+ happy customers.
- Bedankscherm: **Your 5 gifts are waiting** / Check your inbox. We'll show you the one trick that makes titanium release: medium heat, 2 to 3 minutes, then a teaspoon of oil. / Your code: BFCODE (of: "No code needed. Your 5 gifts are added at checkout.") / knop: See the pans

**Variant B (emotioneel)**
- Label: THE LAST PAN YOU REPLACE
- Kop: **Tired of buying the same pan again?**
- Bewijs: You're not alone. 4 in 10 Siraat customers came to us because their old coating wore off.
- Mechanisme: There's nothing on ours to flake off. That's why it comes with a 75-year warranty.
- Aanbod: With your first order: 5 free gifts with every order ($555 value). Mystery gift, Free shipping, Plastic-free e-book, Favorites cookbook, and a chance to win a PFAS water filter.
- E-mailveld: "Your email address" / knop: **Send me my offer**
- Onder de knop: Free shipping. 30-day returns. 100,000+ happy customers.
- Bedankscherm: **Good. No more peeling.** / Your welcome email is on its way, with how to cook your first egg on titanium. / Your code: BFCODE (of: "No code needed. Your 5 gifts are added at checkout.") / knop: Shop the Black Friday Sale

**Welkomstmail 1, teaser:** onderwerp A "Nothing on it to peel", onderwerp B "15 pans, or one.", preview "Why titanium doesn't flake, the heat trick, and your 5 gifts."

### Gift (`gift`)
Bron cijfer: S1 (n=8,885) 'Who is this purchase for?': ~1 in 5 koopt als cadeau (19%).  
Link bedankscherm: https://siraatskitchen.com/collections/black-friday-sale

**Variant A (rationeel)**
- Label: GIFTING THIS YEAR
- Kop: **A gift that's covered for 75 years.**
- Bewijs: About 1 in 5 Siraat customers buy their pan as a gift.
- Mechanisme: No PFAS, PFOA, or BPA. 30-day returns if it's not quite right. The 5 gifts come with it.
- Aanbod: Here's your offer: 5 free gifts with every order ($555 value). Mystery gift, Free shipping, Plastic-free e-book, Favorites cookbook, and a chance to win a PFAS water filter.
- E-mailveld: "Your email address" / knop: **Claim my 5 gifts**
- Onder de knop: Free shipping. 30-day returns. 100,000+ happy customers.
- Bedankscherm: **Your 5 gifts are waiting** / Check your inbox. We'll help you pick the right size for them. / Your code: BFCODE (of: "No code needed. Your 5 gifts are added at checkout.") / knop: Find their pan

**Variant B (emotioneel)**
- Label: FOR SOMEONE WHO COOKS
- Kop: **Give them the pan they'd never buy themselves.**
- Bewijs: They'd be in good company. About 1 in 5 Siraat customers buy for someone else.
- Mechanisme: The original hammered titanium pan. No coating to wear off, so it's still a good gift years from now.
- Aanbod: And something for you, with every order: 5 free gifts with every order ($555 value). Mystery gift, Free shipping, Plastic-free e-book, Favorites cookbook, and a chance to win a PFAS water filter.
- E-mailveld: "Your email address" / knop: **Send me my offer**
- Onder de knop: Free shipping. 30-day returns. 100,000+ happy customers.
- Bedankscherm: **That's one gift sorted** / Your welcome email is on its way, with gift picks by size. / Your code: BFCODE (of: "No code needed. Your 5 gifts are added at checkout.") / knop: Shop the Black Friday Sale

**Welkomstmail 1, teaser:** onderwerp A "Who are you cooking for?", onderwerp B "A gift covered for 75 years", preview "Gift picks by size, 30-day returns, and 5 gifts with every order."

### Stainless / cast iron switch (`switch`)
Bron cijfer: S1 (n=6,792) 'Which options did they seriously compare?': stainless steel 41%, ceramic 17%, cast iron 13%.  
Link bedankscherm: https://siraatskitchen.com/collections/black-friday-sale

**Variant A (rationeel)**
- Label: NO COATING, LIKE STAINLESS
- Kop: **No coating, like stainless. Eggs that let go.**
- Bewijs: 4 in 10 Siraat customers compared us with stainless steel before choosing titanium.
- Mechanisme: Cold metal grabs your food, hot metal lets it go. Medium heat for 2 to 3 minutes, a teaspoon of oil, and it slides. No seasoning.
- Aanbod: Here's your offer: 5 free gifts with every order ($555 value). Mystery gift, Free shipping, Plastic-free e-book, Favorites cookbook, and a chance to win a PFAS water filter.
- E-mailveld: "Your email address" / knop: **Claim my 5 gifts**
- Onder de knop: Free shipping. 30-day returns. 100,000+ happy customers.
- Bedankscherm: **Your 5 gifts are waiting** / Check your inbox. We'll show you the water-drop test that tells you the pan is ready. / Your code: BFCODE (of: "No code needed. Your 5 gifts are added at checkout.") / knop: See the pans

**Variant B (emotioneel)**
- Label: THE EASIER SWITCH
- Kop: **You wanted no coating. Not a fight with every egg.**
- Bewijs: Stainless steel is what most Siraat customers weighed us against. 4 in 10 of them.
- Mechanisme: Titanium keeps the part you liked about stainless, nothing on the surface. Get the heat right and it lets go. No seasoning, dishwasher safe.
- Aanbod: With your first order: 5 free gifts with every order ($555 value). Mystery gift, Free shipping, Plastic-free e-book, Favorites cookbook, and a chance to win a PFAS water filter.
- E-mailveld: "Your email address" / knop: **Send me my offer**
- Onder de knop: Free shipping. 30-day returns. 100,000+ happy customers.
- Bedankscherm: **Breakfast is about to get easier** / Your welcome email is on its way, with how to heat titanium so food lets go. / Your code: BFCODE (of: "No code needed. Your 5 gifts are added at checkout.") / knop: Shop the Black Friday Sale

**Welkomstmail 1, teaser:** onderwerp A "Cold metal grabs. Hot metal lets go.", onderwerp B "No coating, no seasoning, no fight", preview "The 2-minute heat trick for titanium, and your 5 gifts."

### Family / kids (`family`)
Bron cijfer: S2 (n=592) 'What do they value most when cooking?': health & safety 76%. Partner/familie 11 tot 19% (S6, S9); 'family safety' 5% (S6). Geen kids-specifieke data.  
Link bedankscherm: https://siraatskitchen.com/pages/third-party-testing

**Variant A (rationeel)**
- Label: WHAT DINNER COOKS ON
- Kop: **Know exactly what your family's dinner cooks on.**
- Bewijs: 76% of Siraat customers say health and safety is what they value most when cooking.
- Mechanisme: A pure titanium cooking surface with no coatings. No PFAS, PFOA, or BPA, tested by Light Labs, report no. 25895.
- Aanbod: Here's your offer: 5 free gifts with every order ($555 value). Mystery gift, Free shipping, Plastic-free e-book, Favorites cookbook, and a chance to win a PFAS water filter.
- E-mailveld: "Your email address" / knop: **Claim my 5 gifts**
- Onder de knop: Free shipping. 30-day returns. 100,000+ happy customers.
- Bedankscherm: **Your 5 gifts are waiting** / Check your inbox. The lab report is in the first email, so you can read it yourself. / Your code: BFCODE (of: "No code needed. Your 5 gifts are added at checkout.") / knop: Read the lab report

**Variant B (emotioneel)**
- Label: FOR THE PEOPLE YOU FEED
- Kop: **One less thing to worry about at dinner.**
- Bewijs: You're like most of our customers. 76% say health and safety matters most when they cook.
- Mechanisme: Nothing on the surface to wear off into the pan. Dishwasher safe for the nights the kids win.
- Aanbod: With your first order: 5 free gifts with every order ($555 value). Mystery gift, Free shipping, Plastic-free e-book, Favorites cookbook, and a chance to win a PFAS water filter.
- E-mailveld: "Your email address" / knop: **Send me my offer**
- Onder de knop: Free shipping. 30-day returns. 100,000+ happy customers.
- Bedankscherm: **Dinner just got simpler** / Your welcome email is on its way, with the lab report and how to pick a size for your table. / Your code: BFCODE (of: "No code needed. Your 5 gifts are added at checkout.") / knop: Shop the Black Friday Sale

**Welkomstmail 1, teaser:** onderwerp A "What your family's dinner cooks on", onderwerp B "Report no. 25895, for your kitchen", preview "No PFAS, PFOA, or BPA. The lab report, and your 5 gifts."

## 3. Overslaan en controle
**Overslaan ("Skip, just show me the gifts")**: 5 FREE GIFTS / **5 free gifts with every order.** / 100,000+ happy customers cook on Siraat. / gedeeld aanbodblok / knop **Claim my 5 gifts** / Free shipping. 30-day returns. 100,000+ happy customers.. Bedankscherm: Your 5 gifts are waiting / Check your inbox for your welcome email. / Your code: BFCODE. Welkomstmail: de huidige BF-W1 ("You're just in time").

**Controle (A/B, geen vraag)**
- Controle = de huidige live Alia-popup, ongewijzigd gedupliceerd. Onderstaande tekst is alleen een referentie als de live tekst niet bruikbaar is; de live tekst wint.
- Referentietekst: BLACK FRIDAY / **5 free gifts with every order.** / $555 value. Plus a chance to win a PFAS water filter. / 100,000+ happy customers. / e-mailveld / knop **Claim my 5 gifts** / Free shipping. 30-day returns. 100,000+ happy customers. / link "No thanks"
- Bedankscherm: Your 5 gifts are waiting / Check your inbox for your welcome email. / Your code: BFCODE / knop Shop the Black Friday Sale
- Let op: "$555 value" alleen tonen aan US-bezoekers; INT zonder bedrag.

## 4. Bewijsregels: wat de vraag echt meet
| Angle | Regel in de popup | Vraag in de enquête | Cijfer | n |
| --- | --- | --- | --- | --- |
| Non-toxic A | 7 in 10 ... toxin-free cookware is what matters most | "What is most important for them?" (S6, S9, meerkeuze) | ~70% | 3,358 en 1,675 |
| Non-toxic B | 6 in 10 ... already searching for PFAS-free cookware | "Which statement best describes them as a home cook?" (S8) | 60% | 3,678 |
| Performance | 4 in 10 ... biggest frustration ... coating wearing off | open vraag, automatisch gegroepeerd (S3) | 41% | 776 |
| Gift | About 1 in 5 ... buy as a gift | "Who is this purchase for?" (S1) | 19% | 8,885 |
| Switch | 4 in 10 ... compared us with stainless steel | "Which options did they seriously compare?" (S1) | 41% | 6,792 |
| Family | 76% ... health and safety ... value most when cooking | "What do they value most when cooking?" (S2) | 76% | 592 |

Niet gebruikt: "#1 reason" (vraag was niet single-choice reden), "microplastics", "your old pan is toxic", alles over kinderen als veiligheidsclaim (geen data, en geen gezondheidsclaims). Performance-cijfer komt uit open tekst, automatisch gegroepeerd: richtinggevend, n=776.

## 5. Meten en bouwen (voorstel, niets aangezet)
- Alia: één popup met vraagstap, antwoord als profielveld naar Klaviyo (bijv. `quiz_angle` = non_toxic | performance | gift | switch | family | skip). Veldnaam en of Alia een keuzestap met vertakking ondersteunt: **[VRAAG FLORIS / Alia]**.
- Test 1: controle (huidige popup) tegen quiz (Q3), 50/50, Smart Testing uit. Winnaar op aanmeldingen per sessie, vangrail omzet per bezoeker en 7-dagen-koopratio van aanmelders. Niet tegelijk met de lopende trigger-test op dezelfde bezoekers, of de trigger gelijk houden in beide armen.
- Test 2 (pas na test 1): A tegen B per angle, of Q1 tegen Q3. Eén variabele per test.
- Flow: conditional split op `quiz_angle` na de trigger in Rn556d; per angle eigen W1-onderwerp en hero, rest van de flow eerst gelijk.

## 6. Open punten voor Floris
1. **Code op het bedankscherm.** DECISIONS 31 okt: de extra 10% BF-code alleen in abandonment-flows, en BF-W1 zegt "No code needed". Een code in de popup botst daarmee. Advies: bedankscherm zonder code ("No code needed. Your 5 gifts are added at checkout."). BFCODE staat alleen als placeholder voor als je anders beslist. **[VRAAG FLORIS]**
2. **Officiële regels PFAS-filter.** De kleine letters verwijzen naar "official rules"; die moeten bestaan (link) voor de popup live gaat. Is de trekking alleen US? **[VRAAG FLORIS]**
3. **Live Alia-tekst** voor de controle: de echte tekst kopiëren, niet mijn referentie. Card Game/order refund nog actief? **[VRAAG FLORIS]**
4. **Familie-angle** gebruikt alleen feiten (no PFAS, PFOA, or BPA; rapport 25895) en het 76%-cijfer. Akkoord dat deze angle meedoet zonder kids-data?
5. Bestaat er een cadeaupagina of size-guide om de gift-angle naartoe te sturen? Nu naar de BF-collectie.

## Controle op de regels
Geen em dash of en dash (script controleert). Geen: lifetime, risk-free, free returns, purifier, free filter, unlock, journey. Oprichter Benjamin (niet genoemd in de popup; teasers zijn voor mails die van Benjamin komen). Filter altijd "a chance to win". $555 alleen US. Geen nieuwe kortingen, geen verzonnen percentages.
