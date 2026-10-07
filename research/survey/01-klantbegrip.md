# 01 · Klantbegrip uit de post-purchase-enquête, vertaald naar de mails

Datum: 7 oktober 2026. Bron: `post-purchase-survey-insights.pdf` (22.160 antwoorden, 9 enquêtes, 2025 tot mei 2026). Volledig klantprofiel: `.agents/product-marketing.md`. Alleen gelezen: geen templates, Klaviyo of Shopify gewijzigd. Copyregels blijven die van `.claude/skills/siraat-direct-response/SKILL.md`; waar de enquête-aanbeveling botst met de claims staat dat erbij.

## A. De 7 belangrijkste inzichten

1. **Eén reden wint overal: non-toxic / PFAS-vrij.** 68 tot 76 procent op elke vraag naar wat telt (76% health & safety, 68% non-toxic bij een nieuwe pan, 69 tot 71% "toxin-free cookware"). 44% kocht om "microplastics, PFAS, PFOA" te vermijden. Unprompted vertellen ze een vriend: "non-toxic / PFAS-free" (26%, de grootste benoemde groep). Duurzaamheid ("nothing to wear off") is reden twee (9 tot 18%).
2. **Ze waren al op zoek.** 60% zocht actief naar non-toxic pannen. Ze kennen het probleem; ze willen bewijs dat dit de oplossing is. Problem-uitleg is voor de 18% die het niet wist.
3. **Het oude pijnpunt is slijten plus gif.** Coating slijt of bladdert 41%, gif-zorg 27%. Klanttaal: "peeling", "doesnt last", "flake off".
4. **Prijs is het enige echte bezwaar.** 27% bijna-stop, 55% van de open twijfels, 47% vindt de pan "overpriced" (kleine steekproef, n=152). Het rapport: rechtvaardig met waarde over de tijd en betaalopties, niet met korting.
5. **Stainless steel is de echte concurrent, niet alleen nonstick.** 41% vergeleek RVS, dan keramiek 17%, gietijzer 13%, hybride 13%. "Like stainless steel but sticks destroying food."
6. **Twee twijfels na prijs: maat (15%) en "werkt titanium echt" (15%).** Na aankoop blijft de twijfel: "Whether it keeps its promises", "Not sure first time trying it", "curious if it will be as good as".
7. **Kort besluit, eieren eerst, steak als favoriet, 1 op 5 is een cadeau.** 38% kocht op de dag van ontdekking. Eerste kook: eieren 36%, steak 10%. Favoriete maaltijd: steak 22%, vis 9%. 19% koopt als cadeau, partner 11 tot 19%.

Plus: 88% geeft de ervaring 4 of 5 sterren, 53% zou ons aanraden, en 44% wil meer titanium (potten, sets, bakeware). Meta is de grootste ontdekkingsbron (49% IG + 32% FB in S2; 35% FB + 22% IG open in S7), maar in S9 leidt Google met 42%.

**Wat we niet overnemen uit het rapport:** "Fry an egg, no oil, nothing sticks" (botst met de techniek en is de bron van 28% van de retouren), "your old non-stick is toxic" als kop (angst als hoofdtoon, en "toxic" over andermans product is een claim die we niet kunnen bewijzen), "microplastics" (geen bewijs in claims.csv). Wel: dezelfde richting, binnen de claims.

## B. Per flow: koopreden, bezwaar, klantzinnen

Klantzinnen: E = enquête (anoniem, alleen als "what customers told us" of als bron voor onze eigen zin), R = echte review (met naam, verbatim, check met `research/copy/check_reviews.py`).

| Flow | Koopreden om te raken | Bezwaar om weg te nemen | Klantzinnen |
| --- | --- | --- | --- |
| **Checkout** (meest bewust, 38% beslist dezelfde dag) | Je koos PFAS-vrij; hier is het papier (rapport 25895) | Prijs (C1/C3: waarde over 75 jaar, termijnen US), maat (C1), "werkt het" (C2) | R017 Marilyn B. "I only need the new one." · R466 James "I honestly thought this might be another scam. But it's real titanium." · E "Non stick without toxic coating" |
| **Cart** | Geen coating om af te bladderen, PFAS-vrij | Prijs (K2: "15 pans, or one"), plakken/schoonmaken (K1) | E "The peeling of non stick coatings" · R011 Lorraine "Expensive but definitely Value for money." · R143 Sandi R. (dun laagje olie) |
| **Browse** | Non-toxic met bewijs, het origineel | Vergelijken met RVS en andere titanium-merken | E "Toxic free non stick. Like stainless steel but sticks destroying food." · R049 Libby "I'm trying to replace all my Teflon pans" |
| **Welcome** (60% zocht al) | W1: PFAS-vrij en waarom (geen coating); W3: de drie vragen | W2/W3 vergelijken, W4 maat, W5 prijs en twijfel | R169 Michael G. "I don't want the forever chemicals." · R138 Tammy "non-toxic and so much lighter than my old cast iron pans" · E "Nontoxic nonstick cooking surface" |
| **Post-purchase** | Bevestig hun keuze in hun woorden ("you chose a pan with no PFAS and nothing to peel") | "Whether it keeps its promises": eerste kook moet lukken (P2), maat/deksel (P3) | E "Pans look great, but have to wait to test it when it arrives" · E "Whether it keeps its promises" · R017, R192 Kathy "I followed the directions for proper heating and the pan works perfectly." |
| **Winback** | Tweede pan voor wie de eerste goed bevalt; nog op een coated pan? | Prijs (geen korting als enige argument), welke vorm | E "Bought crepe pan 1st, loved it! So got deep pan now!" · R138 Tammy "4th pan" · E "I bought this hoping I never need buy another nonstick pan of this size" |
| **Site** | Non-toxic als categorie ("not sure which pan?") | Maat (15%), keuze pan of set | E "Looking for something non toxic but easy to cook with at the same time" |
| **Sunset** | Herinner aan waarom ze kwamen: PFAS-vrij koken | Te veel mail | Geen klantquote nodig; één regel "no PFAS, nothing to wear off" |
| **VIP** | Ze vertellen het door (53% aanbevelen) | Geen; vraag wat ze willen (44% meer titanium) | R138 Tammy "I even gifted one to my son" · E "Bought crepe pan 1st, loved it!" |
| **Anniversary** | "Nothing has worn off" is hier het bewijs van de koopreden | Verkleuring, plakken na maanden (N1) | E "Non-stick feature doesnt last very long" (over het oude, als contrast) · R056 Stacey K. (patina) |
| **UGC** | Het eerste ei als bewijs voor een vriend | "I have to try my pan before I would be able to tell my friends" | E "I have to try my pan before I would be able to tell my friends how I like it" · E "Eggs and stir fry veggies" |

## C. Onderwerpregels en hero-regels in klanttaal (Engels)

Allemaal binnen de claims; body koppelt "no coatings" altijd aan "a pure titanium cooking surface".

| # | Regel | Type | Flow |
| --- | --- | --- | --- |
| 1 | Non-toxic is easy to say. Here's the report. | Specificiteit, autoriteit | C2, W3 (subject) |
| 2 | Nothing on it to peel off | Klanttaal (peeling) | K1, B1 (subject of hero `Nothing on it|to peel off`) |
| 3 | Is it really worth $134? | Vraag, prijs | K2, C3 (subject) |
| 4 | 15 coated pans, or one | Specificiteit, prijs | K2-new, C3-p (hero) |
| 5 | Stainless steel, or titanium? | Vraag, vergelijking | B1, W3 (subject) |
| 6 | "Whether it keeps its promises" | Enquêtezin als vraag van de klant | P2 (subject, met in de body "one customer told us that's what they wanted to find out") |
| 7 | The first egg will tell you | Nieuwsgierigheid + belofte | P1-first, P2-safe (subject) |
| 8 | No PFAS. Nothing to wear off. Report no. 25895. | Specificiteit | W1 (hero `No PFAS.|Nothing to wear off.`, subline "Report no. 25895, read it yourself") |
| 9 | For you, or someone you cook for? | Vraag, cadeau (19%) | Q4-campagne, C2-acc |
| 10 | Tonight, a steak. No coating. | Specificiteit, gebruik (steak 22%) | N1, R1-pan, P3 (subject; body: medium heat, laat los voor je keert) |

A/B-voorstel: in W1 en C2 de koopreden testen, niet de korting: A "No PFAS. Nothing to wear off." tegen B de huidige "The pan with nothing on it". Eén variabele: PFAS-kop tegen duurzaamheidskop.

## D. Wat in de huidige mails (v3) botst met wat klanten zeggen

1. **De koopreden staat bijna alleen in de footer.** "Non-toxic" komt in de body van v3 twee keer voor ("Every pan says non-toxic" in C2 en W3); het hoofdidee is bijna overal "nothing on it to wear off" (7 keer) en het aanbod ("10%" circa 100 keer, "$70 in gifts" als blokkop in 17 mails). Klanten kopen om PFAS te vermijden, niet om slijtage. PLAYBOOK 1 zet pijler "Non-toxic, for real" alleen op koud publiek en welcome; de enquête zegt dat het in elke fase de reden is, ook na de aankoop.
2. **Prijs wordt beantwoord met korting, niet met waarde.** Alleen K2-new en C3-p doen de 75-jaarsrekensom; geen enkele mail noemt Affirm of Shop Pay Installments. Rapport en deep/01: korting is het zwakste antwoord.
3. **Er wordt alleen met "coated nonstick" vergeleken.** "Titanium vs. coated nonstick" in B1, K2-new, A2. Stainless steel (41%) en gietijzer (13%) komen niet voor, terwijl Tammy's "lighter than my old cast iron pans" er klaar voor is.
4. **De twijfel na aankoop wordt niet benoemd.** P1-first opent met "Here is what happens next"; de klant denkt "Whether it keeps its promises". Benoem het eerst, geef dan de techniek. P2 doet de techniek goed.
5. **De maatregel spreekt zichzelf tegen.** Standard 11": "right for one or two people" (C1), "Everyday cooking for 1 or 2" (W4), "Cooking for 2 to 4" (A1, en Gorgias 8566447 in `product.md`). 15% twijfelt over de maat; één regel overal.
6. **Alleen eieren.** "egg" staat circa 30 keer in v3, "steak" 2 keer. Steak is de favoriete maaltijd (22%), vis 9%. Eieren blijven de eerste kook; steak hoort in N1, R1 en P3.
7. **Cadeau is een bijzaak.** 19% koopt als cadeau, maar het cadeauperspectief zit alleen in C2-acc en P3-apron. Een gever krijgt nu "your first egg"-mails (P2, U1) over een pan die bij een ander staat.

## Top 5 aanpassingen voor de mails (voor de herschrijf-agent, niets zelf gewijzigd)

1. **Hero-idee in W1, C2, B1, K1 naar PFAS-vrij met bewijs**, duurzaamheid als tweede zin. Kop in hun woorden: "No PFAS. Nothing to wear off." Footerregel blijft.
2. **Prijs als waarde:** de 15-pannen-rekensom en (US, na akkoord op de claim) een termijnregel in C1/C3/K2; korting blijft in de codebalk, niet in de kop.
3. **Eén maatregel overal** (voorstel: tel je eieren, Standard = 2 tot 4, zoals A1 en Gorgias), Floris bevestigt.
4. **Post-purchase P1/P2 opent met hun twijfel** ("You're probably wondering if it keeps its promises. The first egg will tell you.") en eindigt met de UGC-vraag; steak als tweede kook.
5. **Vergelijkingsblok RVS en gietijzer** (categorie, geen merk) in browse en W3, met Tammy R138; plus een cadeauvariant voor Q4 en een "who is this for"-vraag als zero-party data **[VRAAG FLORIS]**.
