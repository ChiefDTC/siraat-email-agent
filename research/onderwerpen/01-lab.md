# 01 · Onderwerpregel- en previewlab v4

Datum: 7 oktober 2026. Alleen gelezen: Klaviyo (GET plus de twee rapport-endpoints, revision 2025-10-15), templates en manifest. Niets gewijzigd in templates of Klaviyo. Copyregels: `.claude/skills/siraat-direct-response/SKILL.md` (incl. sectie 12), `.agents/product-marketing.md`, `research/survey/01-klantbegrip.md`. Testplafond: `research/testing/02-testroadmap.md` en v4-besluit 3.19 (max 2 tests per flow).

Bestanden:
- `voorstellen.csv`: per v4-mail (59) huidig A, B, preview, score, drie varianten (formule tussen haken), beste preview, testwaardig, hypothese.
- `historie.csv`: 320 historische onderwerpen (236 campagnes, 84 flowberichten) met open, klik, conversie, RPR en index tegen hun eigen groep.

## 1. Wat werkt bij Siraat-klanten (Klaviyo, laatste 365 dagen)

**Bron en methode.** `campaign-values-reports` en `flow-values-reports`, timeframe `last_365_days`, conversiemetric Placed Order (RSNxYV), alleen e-mail, minimaal 1.000 ontvangers. Onderwerpen via `/api/campaigns/{id}/campaign-messages` en `/api/flow-messages/{id}`. Campagnes: 236 (8 okt 2025 t/m 6 okt 2026). Flowberichten: 84 (21 zonder onderwerp, verwijderd of SMS, overgeslagen).

Campagnes verschillen sterk in publiek (30 dagen engaged tegen alle abonnees) en seizoen (BFCM, juni-dip). Daarom per campagne een index tegen de mediaan van hetzelfde publiek in dezelfde maand, en een gewogen regressie (log open en log klik op alle kenmerken tegelijk, met vaste effecten publiek x maand). Effect = verschil met vergelijkbare campagnes zonder dat kenmerk. t >= 2 is een redelijk signaal, daaronder richtinggevend.

**Belangrijk voorbehoud.** Opens zijn door Apple Mail Privacy Protection opgeblazen en zeggen weinig over het onderwerp; **klikratio is de beslissende maat** (zoals in de testroadmap). Het is observationeel: de body verschilt ook per mail. Veel formules komen weinig voor (vraag n=7, PFAS n=4), dus zie dit als hypotheses voor tests, niet als wetten.

### 1.1 Campagnes (n=236)

| Formule | n | Open | Klik | Wat het zegt |
| --- | --- | --- | --- | --- |
| Kort (<= 25 tekens) | 127 | +1,6% (t 0,7) | **+19% (t 2,5)** | Kort helpt klikken, niet openen. Lang (> 40) kost niets meetbaars (n=22). |
| Vraag | 7 | **+13,5% (t 2,4)** | **+57% (t 2,6)** | Sterkste formule, kleine n. Beste: "Non-sticking not happening?" (1,5% klik, 1,7x groep), "Why is it getting difficult for us?" (3,0x), "Non-toxic cookware AND dishwasher safe?" (open 1,3x). |
| Getal | 21 | **-8% (t -2,9)** | -4% (t -0,4) | Bij Siraat waren getallen generiek ("Top 5", "48hrs Left"). Specifiek bewijs (rapport 25895, 31 PFAS) is nog nooit getest. |
| PFAS / non-toxic | 4 | +3,5% (t 0,6) | -13% (t -0,7) | Te weinig data. Zelfde beeld in Failure to launch: "Cook Plastic & Toxin Free" en "Ditch the Micro-Plastics" 0,32 tot 0,36% klik, vergelijking ("Titanium Vs Stainless Steel", "Ceramic VS Titanium") 0,44 tot 0,46%. Vage gezondheid trekt niet; PFAS met bewijs is ongetest. |
| Korting (%, off, sale) | 42 | -2,7% (t -1,0) | **+68% (t 6,2)** | Het sterkste kliksignaal, maar dat zijn vooral salecampagnes (70% off). Bij flows juist niet (zie 1.2). |
| Persoonlijk (you/your) | 25 | -1% | +3% | Geen effect. |
| Voornaam-tag | 13 | **+13,7% (t 2,2)** | +17% (t 0,9) | Opent beter, klikt niet aantoonbaar beter. Niet nodig in v4 (rustige toon, risico op lege tag). |
| Emoji | 27 | -1% | **-25% (t -2,8)** | Kost kliks. Niet gebruiken (ook spamrisico). |
| Prijs ($) | 1 | | | Niet te meten. |
| Urgentie (last, ends, hours, tonight) | 27 | -3,8% | -9% | Geen winst. "Last Call for Flash Savings" 0,21% klik. |
| Founder / ik / we | 21 | **-7,5% (t -2,7)** | +16% (t 1,5) | Opent minder, klikt eerder meer. "I did something I shouldn't have" opende 9,8%: clickbait straft zich. |
| HOOFDLETTERS | 13 | -3% | +57% (t 3,7) | Valt samen met de grote sales; spamrisico. Niet in flows. |

Spamsignaal in de historie: tekenvervanging zoals "0ff", "BIack Friday", "BestseIIers" (om filters te omzeilen). Nooit doen: het is precies wat Gmail als spam leert.

### 1.2 Flowberichten (n=84, binnen dezelfde flow vergeleken)

| Bewijs | Wat het zegt voor v4 |
| --- | --- |
| Pan Education: "The #1 mistake that makes titanium stick" **6,9% klik** tegen 2,1 tot 4,0% voor "Why your pan is changing color...", "The right way to clean...", "5 things that will shorten..." | Nieuwsgierigheid + voordeel over een probleem dat ze zelf hebben wint ruim. Basis voor P2-test. |
| Checkout: mail 1 "Don't leave these hanging" 3,5 tot 5,3% klik, RPR $4,59 tot $7,83; "Join the Happy Chef Club" 1,5 tot 2,3%. | Eerste mail draagt de omzet; generieke clubtaal werkt niet. C1 laten zoals hij is. |
| Cart: "Hi {{ first_name }}, we saved these for you" 3,0% klik, RPR $2,55; "getting cooking with 10% off" 1,5%, $0,67; "Last Call for 10% Off!" opent 54% maar klikt 1,6 tot 1,7%. | Korting in het onderwerp van een vervolgmail verhoogt de klik niet; bezit/bewaard wel. |
| Welcome oud: "Last Call for an Extra 10% Off" 0,93% klik tegen "See Why We Are Top Rated" 0,91%. | Kortingsurgentie wint niet van social proof in welcome. |
| Post-purchase: "We've got a quick question for you!" 9,3% klik, RPR $0,76; "A note from Benjamin" 8,4 tot 9,0%; "100 Days to Try Us Out" 3,2% (en nu verboden). | Na aankoop werken vraag en Benjamin. Steunt VIP V2 en P1-varianten. |
| Sunset oud: "it's been a while" 11,8% open; "Staying or Going?" 5,7%. | Re-permission blijft laag; meet % kept, niet het onderwerp. |
| Kortingswoorden in flows (n=9): open -43%, klik -73% binnen de flow (t -2,9 en -2,1). | Vertekend door positie (kortingsmails zijn latere mails), maar er is geen enkel bewijs dat korting in een flowonderwerp helpt. |

### 1.3 Regels voor v4 (uit 1.1, 1.2 en de enquête)

1. **Klik is de maat.** Formules die opens kopen (voornaam, founder-intrige) kopen geen kliks.
2. **Vraag in de gedachte van de lezer** is de beste formule die we hebben (+57% klik, kleine n). Altijd met een preview die de lus sluit.
3. **Kort en specifiek**: <= 40 tekens voor mobiel, liefst <= 30. Nu zijn 9 A-onderwerpen en 8 B-onderwerpen langer dan 40.
4. **Geen emoji, geen hoofdletters, geen tekenvervanging.** Emoji kostte 25% kliks.
5. **Korting in het onderwerp alleen in de laatste mail met een echte code.** In campagnes klikt korting, in flows niet aantoonbaar.
6. **PFAS met bewijs is de grootste ongeteste kans.** De enquête zegt dat het de koopreden is (68 tot 76%), de historie heeft alleen vage gezondheidsonderwerpen getest. Vandaar de W1- en B1-test.
7. **Probleem-oplossend wint van uitleg**: "the mistake that makes it stick" boven "why it changes color".

## 2. Beoordeling per mail

Criteria (1 tot 10): **D** duidelijkheid, **N** nieuwsgierigheid, **R** relevantie voor de flowfase, **K** klanttaal (enquête en reviews), **M** mobiele lengte (10 als A en B <= 40 tekens, daarna -1 per 2 tekens over het langste), **P** preview vult aan in plaats van herhaalt, **S** spamrisico (10 = laag). Score = gemiddelde van de zeven.

Gemiddelde over 59 mails: **8,2**. Per flow: sunset 8,9, ugc 8,7, site 8,4, vip 8,4, welcome 8,3, post-purchase 8,2, winback 8,2, anniversary 8,1, cart 8,1, checkout 8,1, browse 7,5. Laagst: c4 6,7, b2-notclicked 7,0, b1 7,1, k3 7,3, b1-acc 7,4, w1-a/w1-b 7,4.

De basis is goed: rustige toon, echte quotes, eerlijke deadlines. De drie terugkerende zwaktes:
1. **Te lang voor mobiel** (b1, k2-new, k3, c2, c4, c4-nocode, p2, w1, b2-notclicked, p3-set, w4-us): juist de beste ideeen (c2, k2-new) verliezen hun clou.
2. **De koopreden staat bijna nergens in het onderwerp.** Alleen W1 ("No PFAS...") en C2/W3 (getest). Duurzaamheid ("peel", "wear off") en korting domineren.
3. **Preview herhaalt het onderwerp** bij korting (n2, v1, r2-vip, w1) en bij p3-pan (lid, lid, lid).

### Directe fouten (los van smaak)

| Mail | Probleem | Voorstel |
| --- | --- | --- |
| checkout/c4 | "10%%" in SUBJECT_A, topcomment, preview B en manifest. Zo verstuurd ziet de klant "10%%". | Bij de export controleren dat het "10%" wordt (of "Your own 10%, for 48 hours"). |
| site/a2 | "Where 100,000+ people started": claim moet letterlijk "100,000+ happy customers" zijn. | "Where 100,000+ happy customers started" (38). |
| checkout/c3-acc B | "The pan 100,000+ people cook on": zelfde claimafwijking. | "The pan 100,000+ happy customers chose". |
| browse/b1 A | "nothing on this pan to scratch off" ligt dicht tegen het verbod op scratch-proof. | "Tested for 31 PFAS. Read the report." |
| browse/b2-notclicked B | "the last Teflon": merknaam in onze eigen zin (product-marketing 9.3). | Variant 1 of 2. |
| browse/b1-acc A | "Looked twice?" klopt niet altijd (trigger is één bekeken product). | "Buying it for someone?" |
| winback/r2-vip-nocode B | Gelijk aan VIP V2 ("What should we make next?"); dezelfde klant kan beide krijgen. | "A thank-you to our regulars". |
| post-purchase/p3-pan(-nocode) | A en B bijna gelijk, geen echte A/B. | Zie varianten. |

Let op bij de varianten: "Tested for 31 PFAS" en "Report no. 25895" gelden voor de geteste Pan Pro en voor andere pannen als "the same titanium cooking surface"; de body moet dat zo zeggen, en "no coating" in de body altijd samen met "a pure titanium cooking surface".

## 3. Testplan binnen het plafond (max 2 tests per flow)

Bestaande tests uit `02-testroadmap.md` blijven staan. Onderwerptests alleen waar een plek vrij is. Winnaar op unieke kliks, dan omzet per ontvanger; nooit op opens.

| Flow | Al bezet | Onderwerptest | Fase | Hypothese (kort) |
| --- | --- | --- | --- | --- |
| Welcome | T04 (fase 1), T05b + T07 (fase 2) | **W1 = T05b met nieuwe armen**: "No PFAS. Report no. 25895 inside." tegen "Your 10% is inside (plus $70 in gifts)" | 2 | Koopreden met bewijs tegen aanbod. De belangrijkste open vraag voor alle onderwerpen. Akkoord Floris nodig (vervangt de huidige T05b-armen). |
| Browse | T01, T05a (fase 1); T03, T08 (fase 2) | **B1 = T05a met kortere armen**: "Tested for 31 PFAS. Read the report." tegen "The pan 100,000+ happy customers chose" | 1 | Zelfde principe (autoriteit tegen social proof), nu beide <= 40 tekens. |
| Post-purchase | T02 (P3) | **P1-first**: "Good call. Here's what's coming." tegen "You chose no PFAS. Good call." | 1 | Koopreden bevestigen geeft meer kliks naar gids en video. Guardrail: retourverzoeken over plakken. |
| Post-purchase · levering | geen | **P2**: "If you can do an egg, you can do anything" tegen "The 1 mistake that makes titanium stick" | 1 | Historisch 6,9% tegen 2,1 tot 4,0% klik voor de "mistake"-formule. Guardrail: plak-retouren (28% van retouren). |
| Winback | T02 (R2) | **R1-pan**: "How's your pan doing?" tegen "What pan owners add next" | 1 | Inhoud beloven wint van check-in. Lange looptijd, 80%-regel. |
| Anniversary | T02 (N2) | **N1**: "How's your pan at six months?" tegen "The brown tint on your pan, explained" | 1 | Check-in-vraag tegen uitleg over verkleuring (historisch zwak, 2,5%). |
| Site | geen | **A1** na 4 weken: "Not sure which pan? Start here." tegen "Four eggs or five?" | na wk 4 | Kort en specifiek over de maattwijfel (15%). |
| Checkout, cart | T01, T02 (fase 1); T02, T03 (fase 2) | geen; **later (fase 3)**: C2 autoriteit tegen James' quote, K1 met of zonder PFAS, K2-new rekensom tegen vraag | 3 | Zie de mails. |
| VIP, sunset, UGC | | geen | | Te klein volume of andere maat (antwoorden, % kept). |

Inkorten zonder test (geen testplek nodig, één variabele verandert niet): b1 (via T05a), k2-new, k3, c2, c4, c4-nocode, p2 (via de test), b2-notclicked, p3-set, w4-us, plus de fouten in sectie 2. Voorstel per mail: de kortste variant met dezelfde formule als het huidige A.

## 4. Per mail: score, varianten, beste preview

Tekens tussen haken. Formules per mail verschillen: vraag, specifiek, nieuwsgierigheid + voordeel, verhaal (alleen echte reviews, letterlijk, gecontroleerd in `content/reviews/reviews.csv`), aanbod, koopreden/klanttaal, persoonlijk.

### anniversary

| Mail | Huidig A / B (tekens) | Preview | D | N | R | K | M | P | S | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n1 | A: How's your pan at six months? (29)<br>B: The brown tint on your pan, explained (37) | A brown tint, a bit of sticking, a loose handle. The three short answers. | 8 | 7 | 9 | 7 | 10 | 8 | 10 | **8.4** |
| n2-nocode | A: One year ago this week (22)<br>B: A year on titanium. 74 years to go. (35) | A year ago this week you placed your first order. 74 years left on your warranty. | 8 | 7 | 9 | 6 | 10 | 8 | 10 | **8.3** |
| n2 | A: One year ago this week (22)<br>B: Happy first year. Here's 10% off. (33) | A year ago you placed your first order. Here's 10% off, yours for 7 days. | 8 | 6 | 8 | 6 | 10 | 7 | 8 | **7.6** |

**n1**: Sterke servicemail. A is warm maar algemeen; B belooft een antwoord op een echte twijfel. Preview vult goed aan.
- V1 (Vraag + koopreden, 33): `Six months in. Anything worn off?`
- V2 (Specifiek (3 dingen), 40): `The brown tint, the sticking, the handle`
- V3 (Gebruik (steak 22%), 31): `Six months in. Steak night yet?`
- Beste preview (69): A brown tint, a bit of sticking, a loose handle. Three short answers.
- Testwaardig: **ja**. Anniversary-plek 2 (naast T02 op N2): A vraag (liking) 'How's your pan at six months?' tegen B uitleg 'The brown tint on your pan, explained'. Hypothese: de check-in-vraag haalt meer unieke kliks, want historisch klikte 'Why your pan is changing color (and why that's a good thing)' maar 2,5% tegen 6,9% voor 'The #1 mistake that makes titanium stick': verkleuring trekt minder dan een probleem dat je zelf hebt. Guardrail: tickets over verkleuring en plakken.

**n2-nocode**: Goed: 74 jaar is specifiek en alleen Siraat kan het zeggen. A zegt weinig; B is de sterkere hoofdregel.
- V1 (Specifiek (getal), 21): `1 year down, 74 to go`
- V2 (Vraag, 24): `How many eggs in a year?`
- V3 (Klanttaal (slijten), 34): `A year in, and nothing to wear off`
- Beste preview (81): A year ago this week you placed your first order. 74 years left on your warranty.

**n2**: B met korting is helder maar de preview herhaalt de 10%. Liever de jaardag in het onderwerp en de code in de preview.
- V1 (Specifiek (getal), 21): `1 year down, 74 to go`
- V2 (Aanbod (echte termijn), 35): `A year in: your own 10%, for 7 days`
- V3 (Vraag, 24): `How many eggs in a year?`
- Beste preview (80): A year ago you placed your first order. Your own 10% code is inside, for 7 days.


### browse

| Mail | Huidig A / B (tekens) | Preview | D | N | R | K | M | P | S | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| b1-acc | A: Looked twice? Here's the detail. (32)<br>B: What it's made of, in two lines (31) | What it's made of, how it lasts, and 10% off with HI10. | 7 | 7 | 7 | 5 | 10 | 7 | 9 | **7.4** |
| b1 | A: Lab-tested: nothing on this pan to scratch off (46)<br>B: 100,000+ happy customers cook on this pan (41) | Metal utensils welcome. No coating, and a lab report to prove it. | 7 | 6 | 8 | 6 | 7 | 8 | 8 | **7.1** |
| b2-clicked-nocode | A: "I ordered one pan to try it out" (33)<br>B: Still thinking it over? (23) | Sunny C. started with one. Your first order comes with 4 gifts too. | 6 | 8 | 8 | 8 | 10 | 9 | 10 | **8.4** |
| b2-clicked | A: Here is your 10%, for the next 48 hours (39)<br>B: "I ordered one pan to try it out" (33) | A personal code, on top of the sale, already applied. It runs out in 48 hours. | 9 | 5 | 9 | 6 | 10 | 8 | 7 | **7.7** |
| b2-notclicked | A: Week one, in their words (24)<br>B: The first egg, the fourth pan, the last Teflon (46) | The first egg, the second pan, the fourth. And HI10 takes 10% off. | 6 | 7 | 7 | 7 | 7 | 6 | 9 | **7.0** |

**b1-acc**: 'Looked twice?' is niet altijd waar (de trigger is één bekeken product). Geen koopreden of klanttaal; cadeau (19%) ontbreekt.
- V1 (Vraag (cadeau 19%), 22): `Buying it for someone?`
- V2 (Nieuwsgierigheid + voordeel, 35): `The detail on the one you looked at`
- V3 (Aanbod, 31): `10% off the piece you looked at`
- Beste preview (75): What it's made of, how to care for it, and HI10 for 10% off. Free shipping.

**b1**: A is 46 tekens (afgekapt op mobiel) en 'nothing to scratch off' schuurt tegen het verbod op scratch-proof. B mist het letterlijke 'happy customers' niet, maar is 41 tekens. Preview is goed.
- V1 (Autoriteit + koopreden (T05a-A kort), 36): `Tested for 31 PFAS. Read the report.`
- V2 (Social proof (T05a-B kort), 38): `The pan 100,000+ happy customers chose`
- V3 (Vraag (vergelijking RVS 41%), 29): `Stainless steel, or titanium?`
- Beste preview (65): Metal utensils welcome. No coating, and a lab report to prove it.
- Testwaardig: **ja**. T05a (fase 1, bestaand). Zelfde principe, kortere armen: A autoriteit 'Tested for 31 PFAS. Read the report.' tegen B social proof 'The pan 100,000+ happy customers chose', zelfde preview. Omdat 68 tot 76% koopt om PFAS en 60% al zocht, wint specifiek bewijs over de koopreden op unieke kliks van massa. Armen inkorten vraagt akkoord Floris (de test zelf blijft T05a).

**b2-clicked-nocode**: Quote van Sunny is echt en sterk; zonder context weet de lezer niet wie het zegt, maar de preview lost dat op. B is generiek.
- V1 (Vraag, 19): `Start with one pan?`
- V2 (Specifiek (gifts), 21): `One pan, $70 in gifts`
- V3 (Prijs als waarde, 22): `15 coated pans, or one`
- Beste preview (67): Sunny C. started with one. Your first order comes with 4 gifts too.

**b2-clicked**: Helder en waar (unieke code, 48 uur). Lang voor wat het zegt; 'Here is your' kost tekens. Kortingsonderwerpen klikken historisch beter (+68% in campagnes), maar openen niet beter.
- V1 (Aanbod kort, 26): `Your own 10%, for 48 hours`
- V2 (Nieuwsgierigheid + voordeel, 35): `A code for the one you went back to`
- V3 (Vraag, 33): `Still thinking it over? 10% helps`
- Beste preview (78): A personal code, on top of the sale, already applied. It runs out in 48 hours.

**b2-notclicked**: A is vaag over wat erin zit; B is 46 tekens en gebruikt 'Teflon' als merk in onze eigen zin. Preview is cryptisch ('the second pan, the fourth').
- V1 (Verhaal (R017 Marilyn B.), 26): `"I only need the new one."`
- V2 (Vraag, 25): `What happens in week one?`
- V3 (Prijs als waarde, 22): `15 coated pans, or one`
- Beste preview (72): Three customers on their first week with no coating. HI10 takes 10% off.


### cart

| Mail | Huidig A / B (tekens) | Preview | D | N | R | K | M | P | S | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| k1-acc | A: Picked it out? It's still here. (31)<br>B: Still deciding? Your cart is saved. (35) | Saved in your cart, with 4 gifts. HI10 takes an extra 10% off. | 9 | 5 | 9 | 5 | 10 | 8 | 9 | **7.9** |
| k1 | A: Nothing on it to peel off (25)<br>B: How long do you scrub a pan? (28) | No scrubbing. That's the whole trick. And 4 gifts ship with every order. | 8 | 7 | 8 | 9 | 10 | 7 | 10 | **8.4** |
| k2-new | A: The pan you keep replacing is the expensive one (47)<br>B: How many pans have you thrown out since 2020? (45) | Even if a coated pan lasted 5 years, that's 15 pans in 75. Here's the math. | 7 | 8 | 9 | 7 | 6 | 9 | 10 | **8.0** |
| k2-returning | A: Adding to your Siraat kitchen? (30)<br>B: "I am on my 4th pan from Siraat" (32) | You know how it works. Your cart is saved, and HI10 still takes 10% off. | 8 | 6 | 9 | 7 | 10 | 8 | 10 | **8.3** |
| k3-nocode | A: What if it's not for you? (25)<br>B: The last email about your cart (30) | Then it goes back unused within 30 days. Your cart and 4 gifts are saved. | 8 | 8 | 10 | 7 | 10 | 9 | 10 | **8.9** |
| k3 | A: Last chance: your own 10% ends in 48 hours (42)<br>B: What if it's not for you? (25) | Your code is already applied to your cart. It runs out 48 hours after this email. | 9 | 5 | 9 | 5 | 9 | 8 | 6 | **7.3** |

**k1-acc**: Duidelijk, maar 'still here' en 'saved' zeggen allebei hetzelfde. Geen reden om terug te gaan.
- V1 (Vraag (cadeau 19%), 19): `For you, or a gift?`
- V2 (Specifiek (gifts), 28): `Your cart, plus $70 in gifts`
- V3 (Nieuwsgierigheid + voordeel, 31): `What it's made of, in two lines`
- Beste preview (62): Saved in your cart, with 4 gifts. HI10 takes an extra 10% off.

**k1**: A is klanttaal ('peeling') op zijn best. De koopreden (PFAS) ontbreekt in onderwerp en preview; 'No scrubbing' belooft meer dan de techniek.
- V1 (Koopreden + klanttaal, 29): `No PFAS. Nothing to peel off.`
- V2 (Vraag (pijn 41%), 28): `Is your old pan peeling yet?`
- V3 (Autoriteit, 39): `Tested for 31 PFAS. Saved in your cart.`
- Beste preview (79): Tested for 31 PFAS, every one below detection. Your cart and 4 gifts are saved.
- Testwaardig: **later**. Fase 3 of zodra cart een plek vrij heeft: 'Nothing on it to peel off' (duurzaamheid) tegen 'No PFAS. Nothing to peel off.' (koopreden erbij). Eén variabele: wel of geen PFAS. Verwachting: koopreden wint op kliks.

**k2-new**: Beste prijsantwoord in de reeks (waarde over tijd), maar A is 47 en B 45 tekens: de clou valt weg op mobiel.
- V1 (Specifiek (rekensom), 22): `15 coated pans, or one`
- V2 (Vraag (prijsbezwaar), 32): `Is it really worth it? The math.`
- V3 (Nieuwsgierigheid + voordeel, 26): `Why the $30 pan costs more`
- Beste preview (75): Even if a coated pan lasted 5 years, that's 15 pans in 75. Here's the math.
- Testwaardig: **later**. Fase 3: '15 coated pans, or one' (specifiek) tegen 'Is it really worth it? The math.' (vraag). Prijs is het bezwaar van 27 tot 55%; een concrete rekensom haalt meer kliks dan de vraag.

**k2-returning**: Passend voor terugkerende kopers. Geen probleem, wel weinig spanning.
- V1 (Specifiek, 28): `Same titanium. Same 4 gifts.`
- V2 (Vraag (gebruik), 25): `Which pan is always busy?`
- V3 (Persoonlijk, 23): `Pan number two is saved`
- Beste preview (72): You know how it works. Your cart is saved, and HI10 still takes 10% off.

**k3-nocode**: Sterk: benoemt de laatste twijfel en de preview geeft het antwoord (30 dagen retour, ongebruikt).
- V1 (Specifiek (risico weg), 36): `30 days to return. 75 years covered.`
- V2 (Verhaal (R240 Brandon W.), 27): `"They honored the warranty"`
- V3 (Aanbod (gifts), 28): `Your cart, with $70 in gifts`
- Beste preview (73): Then it goes back unused within 30 days. Your cart and 4 gifts are saved.

**k3**: Waar (laatste mail, echte 48 uur), maar 42 tekens en 'Last chance' plus '%' is de klassieke spamcombinatie. Historisch: 'Last Call for 10% Off!' opende 54%, klikte maar 1,6%.
- V1 (Aanbod kort, 26): `Your own 10%, for 48 hours`
- V2 (Nieuwsgierigheid + voordeel, 29): `Why your code has an end date`
- V3 (Specifiek, 32): `10% off. Code applied. 48 hours.`
- Beste preview (81): Your code is already applied to your cart. It runs out 48 hours after this email.


### checkout

| Mail | Huidig A / B (tekens) | Preview | D | N | R | K | M | P | S | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| c1 | A: Something stop you at checkout? (31)<br>B: Your cart, plus 4 gifts, still saved (36) | Saved exactly as you left it. Free shipping, and HI10 takes 10% more. | 9 | 8 | 10 | 7 | 10 | 8 | 10 | **8.9** |
| c2-acc | A: Yours, or a gift? Both work. (28)<br>B: "Such lovely gifts" (19) | What it is made of, how to look after it, and 10% off with HI10. | 8 | 7 | 8 | 7 | 10 | 7 | 10 | **8.1** |
| c2 | A: Has the pan in your cart actually been tested? (46)<br>B: "I honestly thought this might be another scam" (47) | Ours has. Light Labs tested it for 31 PFAS compounds. Every one below detection. | 9 | 8 | 10 | 8 | 6 | 9 | 9 | **8.4** |
| c3-acc | A: Most kitchens start with the pan (32)<br>B: The pan 100,000+ people cook on (31) | Your cart is saved. Still cooking on a coated pan? Here is the one change worth making. | 8 | 7 | 8 | 6 | 10 | 8 | 10 | **8.1** |
| c3-p | A: One pan, or three for $349? (27)<br>B: "I ordered one pan to try it out" (33) | Three hammered pans and three lids. About $116 a pan, lid included. | 9 | 8 | 9 | 7 | 10 | 9 | 9 | **8.7** |
| c3-s | A: $70 in gifts ship with your set (31)<br>B: "I've replaced all the pans..." (31) | Free shipping, a mystery gift, the e-book and a chance at a PFAS water filter. | 9 | 6 | 9 | 6 | 10 | 8 | 8 | **8.0** |
| c4-nocode | A: Your cart and $70 in gifts, one last time (41)<br>B: "They honored the warranty" (27) | Your $70 in gifts are still attached to your cart. Plus two promises. | 9 | 6 | 9 | 6 | 9 | 8 | 9 | **8.0** |
| c4 | A: Last chance: your own 10%% ends in 48 hours (43)<br>B: "They honored the warranty" (27) | Your code is already applied, and your $70 in gifts are still attached. | 8 | 5 | 9 | 5 | 8 | 8 | 4 | **6.7** |

**c1**: Goed: vraag in de gedachte van de lezer, 31 tekens. Historisch was de eerste checkoutmail de sterkste van het account ('Don't leave these hanging' 3,5 tot 5,3% klik).
- V1 (Specifiek (bezit), 28): `Saved exactly as you left it`
- V2 (Verhaal (R017 Marilyn B.), 26): `"I only need the new one."`
- V3 (Aanbod (gifts), 28): `Your cart, plus $70 in gifts`
- Beste preview (69): Saved exactly as you left it. Free shipping, and HI10 takes 10% more.

**c2-acc**: Cadeau-hoek is terecht (19% koopt als cadeau). Preview gaat over iets anders dan het onderwerp (materiaal en zorg).
- V1 (Vraag kort, 13): `Who's it for?`
- V2 (Specifiek (risico weg), 31): `Free shipping, 4 gifts, 30 days`
- V3 (Nieuwsgierigheid + voordeel, 31): `What it's made of, in two lines`
- Beste preview (74): For you or someone else: free shipping, 4 gifts, 30 days to return unused.

**c2**: Inhoudelijk de beste: koopreden met bewijs, preview sluit de lus. Maar A is 46 en B 48 tekens.
- V1 (Vraag kort, 29): `Was your pan actually tested?`
- V2 (Klanttaal + autoriteit, 31): `Non-toxic, with a report number`
- V3 (Verhaal ingekort (R466 James), 31): `"...this might be another scam"`
- Beste preview (80): Ours has. Light Labs tested it for 31 PFAS compounds. Every one below detection.
- Testwaardig: **later**. Fase 3 (checkout is vol met T01, T02, T03): autoriteit 'Was your pan actually tested?' tegen social proof met James' quote. Twijfel 'is het echt' (15%) wordt sterker weggenomen door een rapport dan door een andere klant.

**c3-acc**: B wijkt af van de vaste claim (moet '100,000+ happy customers' zijn). A is duidelijk maar vlak.
- V1 (Vraag (klanttaal), 30): `Still cooking on a coated pan?`
- V2 (Specifiek (waarde), 26): `$134, covered for 75 years`
- V3 (Autoriteit, 34): `Now the pan, with report no. 25895`
- Beste preview (83): Your cart is saved. Most kitchens start with the 11-inch pan, covered for 75 years.

**c3-p**: Concreet keuzemoment met echte prijs. Preview rekent het uit. Goed.
- V1 (Specifiek (per pan), 33): `3 pans + 3 lids: about $116 a pan`
- V2 (Nieuwsgierigheid + voordeel, 32): `The math on one pan versus three`
- V3 (Verhaal (R370 Sonya D.), 37): `"I'm going to have to get the set!!!"`
- Beste preview (67): Three hammered pans and three lids. About $116 a pan, lid included.

**c3-s**: Helder aanbod, maar wie een set in de cart heeft twijfelt over prijs, niet over gifts.
- V1 (Nieuwsgierigheid + voordeel, 29): `Every pan on your stove, done`
- V2 (Vraag, 30): `Is a set the right first step?`
- V3 (Koopreden, 26): `A whole stove with no PFAS`
- Beste preview (78): Free shipping, a mystery gift, the e-book and a chance at a PFAS water filter.

**c4-nocode**: Eerlijk en waar (geen nep-deadline). 41 tekens; 'one last time' valt op mobiel weg.
- V1 (Eerlijk / laatste, 29): `One last note about your cart`
- V2 (Nieuwsgierigheid + voordeel, 37): `Two promises that come with your cart`
- V3 (Vraag, 28): `Still deciding on your cart?`
- Beste preview (69): Your $70 in gifts are still attached to your cart. Plus two promises.

**c4**: FOUT: in topcomment en manifest staat '10%%' (dubbel procentteken); zo verstuurd ziet de klant '10%%'. Daarnaast 43 tekens en 'Last chance' + '%' (spamrisico).
- V1 (Aanbod kort, 26): `Your own 10%, for 48 hours`
- V2 (Nieuwsgierigheid + voordeel, 29): `Why your code has an end date`
- V3 (Specifiek, 28): `10% off your cart. 48 hours.`
- Beste preview (71): Your code is already applied, and your $70 in gifts are still attached.


### post-purchase

| Mail | Huidig A / B (tekens) | Preview | D | N | R | K | M | P | S | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| p1-first | A: Good call. Here's what's coming. (32)<br>B: The first egg will tell you (27) | Order confirmed. Your 4 gifts, your e-book and the one tip that matters. | 8 | 7 | 9 | 7 | 10 | 8 | 10 | **8.4** |
| p1-repeat | A: Good to see you again (21)<br>B: Round two. Here's what's coming. (32) | Your order is in. Same careful packing, same 4 gifts. | 8 | 6 | 9 | 6 | 10 | 7 | 10 | **8.0** |
| p2-safe | A: When your pan arrives: the first egg (36)<br>B: Is your pan on the stove yet? (29) | Heat first, then oil, then the egg. Keep this for your first cook. | 9 | 7 | 10 | 8 | 10 | 9 | 10 | **9.0** |
| p2 | A: If you can do an egg, you can do anything (41)<br>B: The one mistake that makes titanium stick (41) | Medium on titanium works like high on a normal pan. The chef's five steps. | 7 | 8 | 10 | 7 | 9 | 9 | 10 | **8.6** |
| p3-accessory-nocode | A: Now meet the pan (16)<br>B: "I ordered one pan to try it out" (33) | The original hammered titanium pan. Free shipping and 4 gifts with every order. | 8 | 7 | 9 | 6 | 10 | 8 | 10 | **8.3** |
| p3-accessory | A: Now meet the pan (16)<br>B: "I ordered one pan to try it out" (33) | Your thank-you code takes 10% off the Pan Pro. It ends 14 days after this email. | 8 | 6 | 9 | 6 | 10 | 8 | 9 | **8.0** |
| p3-apron-nocode | A: An apron deserves a pan (23)<br>B: Was the apron a gift? (21) | The pan it was made for, for you or for them. 4 gifts with every order. | 7 | 8 | 8 | 6 | 10 | 8 | 10 | **8.1** |
| p3-apron | A: An apron deserves a pan (23)<br>B: Was the apron a gift? (21) | Here is 10% off the pan it was made for, for you or for them. | 7 | 7 | 8 | 6 | 10 | 8 | 9 | **7.9** |
| p3-next-nocode | A: What goes next to your pan (26)<br>B: How is the pan treating you? (28) | The board or the lid that matches your order. 4 gifts with every order. | 8 | 7 | 9 | 6 | 10 | 8 | 10 | **8.3** |
| p3-next | A: What goes next to your pan (26)<br>B: How is the pan treating you? (28) | The board or the lid that matches your order, 10% off with your own code. | 8 | 6 | 9 | 6 | 10 | 8 | 9 | **8.0** |
| p3-pan-nocode | A: Which lid fits your pan? (24)<br>B: The lid that fits your pan (26) | The lid in your pan's size, plus the board. 4 gifts with every order. | 9 | 6 | 9 | 6 | 10 | 6 | 10 | **8.0** |
| p3-pan | A: Which lid fits your pan? (24)<br>B: Your thank-you code: 10% off, 14 days (37) | The lid in your pan's size, plus the board. 10% off with your own code. | 9 | 6 | 9 | 6 | 10 | 6 | 9 | **7.9** |
| p3-set-nocode | A: The pan your set is missing (27)<br>B: "Works like a non-stick but gives crispy output" (48) | Crepe or wok: the two shapes a set doesn't cover. 4 gifts with every order. | 9 | 8 | 9 | 7 | 6 | 8 | 10 | **8.1** |
| p3-set | A: The pan your set is missing (27)<br>B: "Works like a non-stick but gives crispy output" (48) | Crepe or wok, 10% off with your own code. It ends 14 days after this email. | 9 | 7 | 9 | 7 | 6 | 8 | 9 | **7.9** |

**p1-first**: Prettig en kort, maar bevestigt niet waarom ze kochten. Klanten willen weten 'whether it keeps its promises'.
- V1 (Commitment + koopreden, 29): `You chose no PFAS. Good call.`
- V2 (Nieuwsgierigheid + voordeel, 35): `The one tip our chef gives everyone`
- V3 (Klanttaal (twijfel), 26): `Will it keep its promises?`
- Beste preview (72): Order confirmed. Your 4 gifts, your e-book and the one tip that matters.
- Testwaardig: **ja**. Post-purchase-plek 2 (naast T02 op P3): A 'Good call. Here's what's coming.' tegen B 'You chose no PFAS. Good call.' Eén variabele: de koopreden in het onderwerp. Bevestigen in hun woorden geeft meer kliks naar gids en video en minder 'is it legit'-tickets. Metric: unieke kliks; guardrail: retourverzoeken over plakken binnen 30 dagen.

**p1-repeat**: Warm en kort. Preview herhaalt 'same' twee keer en voegt weinig toe.
- V1 (Vraag, 32): `Which pan did you add this time?`
- V2 (Verhaal (R138 Tammy), 32): `"I am on my 4th pan from Siraat"`
- V3 (Specifiek, 30): `Order two is in. Same 4 gifts.`
- Beste preview (76): Your order is in, with the same 4 gifts. Your pans are covered for 75 years.

**p2-safe**: Precies goed voor de fase. Preview is de techniek in één zin.
- V1 (Nieuwsgierigheid + voordeel, 39): `The 1 mistake that makes titanium stick`
- V2 (Specifiek, 39): `2 to 3 minutes on medium. Then the egg.`
- V3 (Klanttaal, 27): `The first egg will tell you`
- Beste preview (66): Heat first, then oil, then the egg. Keep this for your first cook.

**p2**: B is de bewezen formule (oude Pan Education: 'The #1 mistake...' 6,9% klik, beste van de reeks). A is een mooie chefzin maar vaag en 41 tekens.
- V1 (Nieuwsgierigheid + voordeel kort, 39): `The 1 mistake that makes titanium stick`
- V2 (Specifiek, 39): `2 to 3 minutes on medium. Then the egg.`
- V3 (Vraag, 24): `Made your first egg yet?`
- Beste preview (74): Medium on titanium works like high on a normal pan. The chef's five steps.
- Testwaardig: **ja**. Hulpflow 'Post-purchase · levering' (eigen plek): A chefverhaal 'If you can do an egg, you can do anything' tegen B 'The 1 mistake that makes titanium stick'. Een onderwerp dat een concrete fout belooft op te lossen haalt meer unieke kliks naar de 5 stappen (historisch 6,9% tegen 2,1 tot 4,0%). Guardrail: retourverzoeken over plakken (28% van retouren) per arm.

**p3-accessory-nocode**: Kort en logisch na een accessoire. Mist de reden om de pan te willen.
- V1 (Koopreden, 37): `The pan: no PFAS, nothing to wear off`
- V2 (Vraag, 18): `Ready for the pan?`
- V3 (Prijs als waarde, 22): `15 coated pans, or one`
- Beste preview (79): The original hammered titanium pan. Free shipping and 4 gifts with every order.

**p3-accessory**: Idem; preview draagt de code goed.
- V1 (Aanbod, 36): `Your thank-you code: 10% off the pan`
- V2 (Koopreden, 37): `The pan: no PFAS, nothing to wear off`
- V3 (Vraag, 18): `Ready for the pan?`
- Beste preview (80): Your thank-you code takes 10% off the Pan Pro. It ends 14 days after this email.

**p3-apron-nocode**: Speels en kort. B raakt de gever (19%). A is net iets te slim.
- V1 (Verhaal (R138 Tammy), 29): `"I even gifted one to my son"`
- V2 (Nieuwsgierigheid + voordeel, 27): `What the apron was made for`
- V3 (Koopreden, 30): `The pan to go with it: no PFAS`
- Beste preview (71): The pan it was made for, for you or for them. 4 gifts with every order.

**p3-apron**: Idem, met code.
- V1 (Aanbod, 31): `10% off the pan it was made for`
- V2 (Verhaal (R138 Tammy), 29): `"I even gifted one to my son"`
- V3 (Vraag, 21): `Was the apron a gift?`
- Beste preview (61): Here is 10% off the pan it was made for, for you or for them.

**p3-next-nocode**: Duidelijk. Kan concreter (welk stuk).
- V1 (Specifiek, 33): `The lid or the board for your pan`
- V2 (Verhaal (R216 Janet R.), 40): `"will be looking for a larger size soon"`
- V3 (Vraag, 32): `Which pan do you reach for most?`
- Beste preview (71): The board or the lid that matches your order. 4 gifts with every order.

**p3-next**: Idem, met code.
- V1 (Aanbod, 28): `Your thank-you code: 10% off`
- V2 (Specifiek, 33): `The lid or the board for your pan`
- V3 (Vraag, 28): `How is the pan treating you?`
- Beste preview (73): The board or the lid that matches your order, 10% off with your own code.

**p3-pan-nocode**: A en B zijn bijna hetzelfde (geen echte A/B). Preview herhaalt 'lid'.
- V1 (Specifiek, 32): `The lid in your pan's exact size`
- V2 (Nieuwsgierigheid, 40): `Two weeks in. The question we hear most.`
- V3 (Vraag, 25): `Cooking with the lid off?`
- Beste preview (83): Cut to your pan's size, plus the board that goes with it. 4 gifts with every order.

**p3-pan**: Idem; B met code is helder.
- V1 (Aanbod, 37): `Your thank-you code: 10% off, 14 days`
- V2 (Specifiek, 32): `The lid in your pan's exact size`
- V3 (Vraag, 25): `Cooking with the lid off?`
- Beste preview (80): Cut to your pan's size, plus the board. 10% off with your own code, for 14 days.

**p3-set-nocode**: A is sterk. B is 48 tekens en de quote zet 'non-stick' vooraan.
- V1 (Vraag, 19): `Crepes or stir-fry?`
- V2 (Specifiek, 33): `Two shapes your set doesn't cover`
- V3 (Persoonlijk, 37): `Two weeks with your set. What's next?`
- Beste preview (75): Crepe or wok: the two shapes a set doesn't cover. 4 gifts with every order.

**p3-set**: Idem, met code.
- V1 (Aanbod, 33): `Crepe or wok, 10% off for 14 days`
- V2 (Vraag, 19): `Crepes or stir-fry?`
- V3 (Specifiek, 33): `Two shapes your set doesn't cover`
- Beste preview (75): Crepe or wok, 10% off with your own code. It ends 14 days after this email.


### site

| Mail | Huidig A / B (tekens) | Preview | D | N | R | K | M | P | S | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a1 | A: Not sure which pan? Start here. (31)<br>B: Four eggs or five? (18) | Four sizes, one titanium cooking surface. Here is how to pick yours in 30 seconds. | 9 | 8 | 9 | 7 | 10 | 8 | 10 | **8.7** |
| a2 | A: Where 100,000+ people started (29)<br>B: One pan, or three? (18) | Most kitchens start with the 11-inch pan. Some go straight to three. Here's how to choose. | 8 | 7 | 8 | 6 | 10 | 8 | 10 | **8.1** |

**a1**: Goede hulpvraag. B raakt de maattwijfel (15%) in 18 tekens.
- V1 (Klanttaal (maat), 31): `Count your eggs. Pick your pan.`
- V2 (Koopreden, 24): `Non-toxic, in four sizes`
- V3 (Vraag, 29): `Cooking for one, two or four?`
- Beste preview (82): Four sizes, one titanium cooking surface. Here is how to pick yours in 30 seconds.
- Testwaardig: **ja**. Na de eerste 4 weken (site heeft geen andere test): A herkenning 'Not sure which pan? Start here.' tegen B nieuwsgierigheid 'Four eggs or five?'. Kort en specifiek over de maattwijfel (15%) wint op unieke kliks; korte onderwerpen klikten historisch +19% (campagnes, gecorrigeerd voor publiek en maand).

**a2**: A wijkt af van de vaste claim: moet '100,000+ happy customers' zijn.
- V1 (Social proof (claim letterlijk), 38): `Where 100,000+ happy customers started`
- V2 (Prijs als waarde, 22): `15 coated pans, or one`
- V3 (Vraag (vergelijking), 29): `Stainless steel, or titanium?`
- Beste preview (90): Most kitchens start with the 11-inch pan. Some go straight to three. Here's how to choose.


### sunset

| Mail | Huidig A / B (tekens) | Preview | D | N | R | K | M | P | S | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| s1 | A: Should we keep writing to you? (30)<br>B: Still want our emails? One tap. (31) | One tap keeps you on the list. No tap, and we'll stop writing in about a week. | 10 | 7 | 10 | 7 | 10 | 9 | 9 | **8.9** |
| s2 | A: Last email from me (unless you tap) (35)<br>B: Should I stop writing? (22) | One tap and you stay. Otherwise this is goodbye, and that's okay. | 9 | 8 | 10 | 7 | 10 | 9 | 9 | **8.9** |

**s1**: Eerlijk en helder. Oude sunset haalde 11,8% open; de vraag is goed.
- V1 (Specifiek, 29): `One tap keeps you on the list`
- V2 (Koopreden, 27): `Still cooking without PFAS?`
- V3 (Vraag kort, 26): `Stay on the list? One tap.`
- Beste preview (78): One tap keeps you on the list. No tap, and we'll stop writing in about a week.

**s2**: Persoonlijk en waar. 'Last email' is hier echt de laatste.
- V1 (Vraag, 31): `Should I take you off the list?`
- V2 (Specifiek, 27): `One tap, or this is goodbye`
- V3 (Persoonlijk, 25): `A last note from Benjamin`
- Beste preview (65): One tap and you stay. Otherwise this is goodbye, and that's okay.


### ugc

| Mail | Huidig A / B (tekens) | Preview | D | N | R | K | M | P | S | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| u1 | A: Show us your first egg? (23)<br>B: One photo, 15% off your next order (34) | Reply with a photo of your first egg, or anything you cooked. We'll send you 15% off. | 9 | 8 | 9 | 8 | 10 | 8 | 9 | **8.7** |

**u1**: Kort, concreet, uitnodigend. Steak (22% favoriet) mag erbij.
- V1 (Vraag (steak 22%), 25): `First egg or first steak?`
- V2 (Aanbod, 31): `Your first egg is worth 15% off`
- V3 (Persoonlijk, 30): `I'd love to see your first egg`
- Beste preview (85): Reply with a photo of your first egg, or anything you cooked. We'll send you 15% off.


### vip

| Mail | Huidig A / B (tekens) | Preview | D | N | R | K | M | P | S | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| v1-nocode | A: Twice is a habit. Thank you. (28)<br>B: For our regulars: a note from Benjamin (38) | You came back for a second order. A thank you from Benjamin, and HI10 still works. | 8 | 7 | 9 | 6 | 10 | 8 | 10 | **8.3** |
| v1 | A: Twice is a habit. Here's 15% off. (33)<br>B: 15% off, 14 days, for our regulars (34) | You've ordered twice. This personal 15% code is yours for 14 days. | 9 | 6 | 9 | 6 | 10 | 7 | 8 | **7.9** |
| v2 | A: A question from Benjamin (24)<br>B: What should we make next? (25) | You've ordered twice. I'd love to know what you want us to make next. | 9 | 8 | 10 | 7 | 10 | 8 | 10 | **8.9** |

**v1-nocode**: Warm. Geen reden waarom een vaste klant iets zou doen.
- V1 (Verhaal (R138 Tammy), 32): `"I am on my 4th pan from Siraat"`
- V2 (Vraag, 32): `Which pan do you reach for most?`
- V3 (Persoonlijk, 30): `A thank-you note from Benjamin`
- Beste preview (82): You came back for a second order. A thank you from Benjamin, and HI10 still works.

**v1**: Helder, maar de preview herhaalt '15%' uit het onderwerp.
- V1 (Nieuwsgierigheid + voordeel, 33): `Why regulars get a different code`
- V2 (Persoonlijk, 35): `A thank-you from Benjamin (15% off)`
- V3 (Vraag, 35): `What would you add to your kitchen?`
- Beste preview (62): Two orders in. Your own code, on top of the sale, for 14 days.

**v2**: Sterk: historisch klikten vraagmails na aankoop het best (9,3% klik).
- V1 (Vraag (44% wil meer titanium), 28): `Pots, sets or bakeware next?`
- V2 (Specifiek, 28): `Two orders in. One question.`
- V3 (Nieuwsgierigheid + voordeel, 37): `One line from you decides what's next`
- Beste preview (69): You've ordered twice. I'd love to know what you want us to make next.


### welcome

| Mail | Huidig A / B (tekens) | Preview | D | N | R | K | M | P | S | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w0 | A: Thank you. Now the first egg. (29)<br>B: 2 to 3 minutes on medium. Then the egg. (39) | Cold metal grabs your food, hot metal lets it go. | 8 | 7 | 10 | 8 | 10 | 9 | 10 | **8.9** |
| w1-a | A: No PFAS, nothing to wear off, and your 10% (42)<br>B: Your 10% is inside (plus $70 in gifts) (38) | Your Card Game entry is in. HI10 takes 10% off the sale price, with 4 gifts. | 7 | 6 | 9 | 8 | 9 | 5 | 8 | **7.4** |
| w1-b | A: No PFAS, nothing to wear off, and your 10% (42)<br>B: Your 10% is inside (plus $70 in gifts) (38) | Your Card Game entry is in. HI10 takes 10% off the sale price, with 4 gifts. | 7 | 6 | 9 | 8 | 9 | 5 | 8 | **7.4** |
| w2 | A: The pan nobody else was making (30)<br>B: December 20, 2024 (17) | It's Benjamin. I wanted to write to you myself. (Your 10% is in the P.S.) | 7 | 8 | 8 | 5 | 10 | 9 | 10 | **8.1** |
| w3 | A: Has your cookware actually been tested? (39)<br>B: Report no. 25895: what it says (30) | Ours has. Report no. 25895, from an ISO/IEC 17025-accredited lab. | 9 | 8 | 10 | 8 | 10 | 9 | 10 | **9.1** |
| w4-int | A: Who are you cooking for? (24)<br>B: Start with the Pan Pro (your 10% inside) (40) | One, two, or a family? Pick your pan by that. Free shipping, duties paid. | 8 | 8 | 9 | 7 | 10 | 9 | 10 | **8.7** |
| w4-us | A: Who are you cooking for? (24)<br>B: Start with the Pan Pro (10% off already applied) (48) | One, two, or a family? Pick your pan by that. Your 10% is already taken off. | 8 | 8 | 9 | 7 | 6 | 9 | 10 | **8.1** |
| w5 | A: Tammy is on her fourth pan (26)<br>B: The last note about your 10% (28) | She gave one to her son, too. And your code HI10 still takes 10% off. | 7 | 9 | 9 | 8 | 10 | 9 | 10 | **8.9** |

**w0**: Goed voor bestaande klanten. Preview is de techniek in hun taal.
- V1 (Nieuwsgierigheid + voordeel, 39): `The 1 mistake that makes titanium stick`
- V2 (Vraag, 29): `Has your first egg gone well?`
- V3 (Klanttaal (mechanisme), 36): `Cold metal grabs. Hot metal lets go.`
- Beste preview (78): Cold metal grabs your food, hot metal lets it go. Two minutes on medium first.

**w1-a**: A propt drie ideeen in 42 tekens. Preview herhaalt de 10% en noemt de Card Game pas daarna. De pop-up belooft een giveaway, niet een korting.
- V1 (Koopreden + autoriteit, 33): `No PFAS. Report no. 25895 inside.`
- V2 (Bevestiging (wat ze vroegen), 26): `Your Card Game entry is in`
- V3 (Specifiek, 36): `31 PFAS tested. All below detection.`
- Beste preview (82): Your Card Game entry is in. HI10 takes 10% off, and 4 gifts ship with every order.
- Testwaardig: **ja**. T05b (fase 2, in de winnaar van T04): A koopreden 'No PFAS. Report no. 25895 inside.' tegen B aanbod 'Your 10% is inside (plus $70 in gifts)', zelfde preview. Vervangt de huidige T05b-armen (die allebei met '10%' openen). Hypothese: de koopreden van 68 tot 76% haalt evenveel of meer unieke kliks dan korting, en een hogere RPR. Historisch klikten kortingsonderwerpen +68% in campagnes, dus dit is de belangrijkste open vraag voor alle onderwerpen. Akkoord Floris nodig.

**w1-b**: Zelfde onderwerpen en preview als w1-a (T04 test alleen het aanbodblok).
- V1 (Koopreden + autoriteit, 33): `No PFAS. Report no. 25895 inside.`
- V2 (Bevestiging (wat ze vroegen), 26): `Your Card Game entry is in`
- V3 (Specifiek, 36): `31 PFAS tested. All below detection.`
- Beste preview (82): Your Card Game entry is in. HI10 takes 10% off, and 4 gifts ship with every order.
- Testwaardig: **ja**. Zelfde test als w1-a (T05b draait in de T04-winnaar).

**w2**: Intrigerend, maar 'nobody else was making' is een impliciete claim die niet in claims.csv staat; 'the original' wel. B alleen een datum is te cryptisch zonder context.
- V1 (Persoonlijk, 20): `A note from Benjamin`
- V2 (Specifiek (claim), 37): `The first orders shipped Dec 20, 2024`
- V3 (Vraag, 33): `Why titanium, and why no coating?`
- Beste preview (73): It's Benjamin. I wanted to write to you myself. (Your 10% is in the P.S.)

**w3**: Sterk: de vraag die de koper zelf heeft, preview sluit de lus met het rapportnummer. 39 tekens, net goed.
- V1 (Klanttaal, 24): `Non-toxic is easy to say`
- V2 (Vraag (vergelijking RVS 41%), 29): `Stainless steel, or titanium?`
- V3 (Specifiek, 36): `31 PFAS tested. All below detection.`
- Beste preview (65): Ours has. Report no. 25895, from an ISO/IEC 17025-accredited lab.

**w4-int**: Goede maatvraag. B is 40 tekens, net op de grens.
- V1 (Klanttaal (maat), 31): `Count your eggs. Pick your pan.`
- V2 (Specifiek, 31): `Mini, Small, Standard or Large?`
- V3 (Vraag (cadeau 19%), 33): `For you, or someone you cook for?`
- Beste preview (73): One, two, or a family? Pick your pan by that. Free shipping, duties paid.

**w4-us**: Idem. B is 49 tekens: afgekapt voor '(10% off already applied)'.
- V1 (Klanttaal (maat), 31): `Count your eggs. Pick your pan.`
- V2 (Prijs als waarde, 22): `15 coated pans, or one`
- V3 (Vraag (cadeau 19%), 33): `For you, or someone you cook for?`
- Beste preview (76): One, two, or a family? Pick your pan by that. Your 10% is already taken off.

**w5**: Nieuwsgierig en echt (R138). Wie Tammy is blijkt pas in de preview, dat is prima.
- V1 (Verhaal (R138 Tammy), 32): `"I am on my 4th pan from Siraat"`
- V2 (Prijs als waarde, 22): `15 coated pans, or one`
- V3 (Vraag (klanttaal), 30): `Still cooking on a coated pan?`
- Beste preview (69): She gave one to her son, too. And your code HI10 still takes 10% off.


### winback

| Mail | Huidig A / B (tekens) | Preview | D | N | R | K | M | P | S | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| r1-acc | A: Ready for the pan? (18)<br>B: Still cooking on a coated pan? (30) | You started with us the other way round. Here's the pan most kitchens start with. | 8 | 7 | 9 | 7 | 10 | 9 | 10 | **8.6** |
| r1-pan | A: How's your pan doing? (21)<br>B: What pan owners add next (24) | Six weeks with your pan. Here is what owners add next, with HI10 and 4 gifts. | 8 | 7 | 9 | 6 | 10 | 8 | 10 | **8.3** |
| r1-set | A: The shapes a set leaves out (27)<br>B: Which pan do you reach for most? (32) | The flat one, the deep one, the board and the tools. HI10 takes 10% off. | 8 | 8 | 9 | 6 | 10 | 8 | 10 | **8.4** |
| r2-nocode | A: Ready for pan number two? (25)<br>B: Your next piece comes with 4 gifts (34) | If one pan is always busy, this is for the second. Free shipping and 4 gifts. | 9 | 7 | 9 | 7 | 10 | 8 | 10 | **8.6** |
| r2 | A: Here is your 10%, for the next 72 hours (39)<br>B: Ready for pan number two? (25) | Your own code, applied with one tap. It ends 72 hours after this email. | 9 | 5 | 8 | 6 | 10 | 8 | 7 | **7.6** |
| r2-vip-nocode | A: You came back. Thank you. (25)<br>B: What should we make next? (25) | You have ordered more than once. A thank you, and 4 gifts with every order. | 8 | 7 | 8 | 6 | 10 | 8 | 10 | **8.1** |
| r2-vip | A: For our regulars: 15% for 72 hours (34)<br>B: Why you're getting 15% (and why it ends) (40) | You've ordered more than once. This 15% code is yours for 72 hours. | 9 | 7 | 9 | 6 | 10 | 7 | 8 | **8.0** |

**r1-acc**: Goed. B is klanttaal en sterker dan A.
- V1 (Autoriteit + koopreden, 33): `Report no. 25895, for the pan too`
- V2 (Verhaal (R017 Marilyn B.), 26): `"I only need the new one."`
- V3 (Prijs als waarde, 22): `15 coated pans, or one`
- Beste preview (81): You started with us the other way round. Here's the pan most kitchens start with.

**r1-pan**: Warm, maar A is een vraag zonder belofte; B is de echte inhoud van de mail.
- V1 (Gebruik (steak 22%), 30): `Six weeks in. Steak night yet?`
- V2 (Specifiek, 25): `A lid, a wok, a crepe pan`
- V3 (Klanttaal, 23): `Is one pan always busy?`
- Beste preview (77): Six weeks with your pan. Here is what owners add next, with HI10 and 4 gifts.
- Testwaardig: **ja**. Winback-plek 2 (naast T02 op R2): A liking 'How's your pan doing?' tegen B social proof 'What pan owners add next'. Het onderwerp dat de inhoud belooft (wat anderen toevoegen) haalt meer unieke kliks dan een check-in. Lange looptijd door volume; beslissen met de 80%-regel.

**r1-set**: Goed: een gat in de set is een concrete reden.
- V1 (Specifiek, 28): `Crepe pan, wok, board, tools`
- V2 (Verhaal (R538 Pam B.), 30): `"He already had the whole set"`
- V3 (Vraag, 24): `Crepes or stir-fry next?`
- Beste preview (72): The flat one, the deep one, the board and the tools. HI10 takes 10% off.

**r2-nocode**: Helder. Preview geeft de reden (één pan is altijd bezet).
- V1 (Klanttaal, 23): `Is one pan always busy?`
- V2 (Verhaal (R138 Tammy), 32): `"I am on my 4th pan from Siraat"`
- V3 (Specifiek, 31): `Pan two: free shipping, 4 gifts`
- Beste preview (77): If one pan is always busy, this is for the second. Free shipping and 4 gifts.

**r2**: Waar en duidelijk, maar puur korting; 39 tekens.
- V1 (Aanbod kort, 26): `Your own 10%, for 72 hours`
- V2 (Nieuwsgierigheid + voordeel, 26): `A code for your second pan`
- V3 (Klanttaal, 23): `Is one pan always busy?`
- Beste preview (71): Your own code, applied with one tap. It ends 72 hours after this email.

**r2-vip-nocode**: B is gelijk aan het VIP-V2-onderwerp; dezelfde klant kan beide krijgen.
- V1 (Verhaal (R138 Tammy), 29): `"I even gifted one to my son"`
- V2 (Specifiek, 40): `4 gifts, free shipping, 75 years covered`
- V3 (Persoonlijk, 27): `A thank-you to our regulars`
- Beste preview (75): You have ordered more than once. A thank you, and 4 gifts with every order.

**r2-vip**: Helder en eerlijk over de deadline. Preview herhaalt '15%' en '72 hours'.
- V1 (Nieuwsgierigheid + voordeel, 40): `Why you're getting 15% (and why it ends)`
- V2 (Persoonlijk, 30): `A thank-you from Benjamin: 15%`
- V3 (Vraag, 28): `What's next in your kitchen?`
- Beste preview (82): You've ordered more than once. Made for you, so it ends 72 hours after this email.
