# Voice of customer: Meta-advertentiecommentaren, november 2026

Analyse van 8 november 2026. Bron: Meta-commentexport tot en met 29 oktober 2026 (Facebook en Instagram), 9,224 rijen, volledig doorgerekend met pandas (geen steekproef). Aangevuld en getrianguleerd met de telbestanden van Floris van 5 november 2026 (ad comments export 2 nov, 58,748 Gorgias-tickets, reviews/Reddit/social, Meta-adperformance, post-purchase survey) en met research/2026-10-06-voice-of-customer.md en research/plannen/2026-11-quiz-popup/BRIEF.md.

Alleen geaggregeerde cijfers en anonieme citaten. Geen namen, geen profiellinks, geen ruwe data in de repo.

## Methode en kanttekeningen

- Ontdubbeld op tekst plus tijdstip: 9,224 rijen worden **7,994 unieke commentaren** onder 358 posts (april 2025 tot 29 oktober 2026). De export van Floris (2 nov) telt 8,107 uniek; het verschil is de laatste vier dagen.
- Indeling per commentaar: tekst (5,214), **keyword-commentaar** (2,200, bijna allemaal "Wings" of "Recipe" als reactie op een comment-to-DM-actie), naam-tag (234), alleen emoji (270), leeg/sticker (76).
- Thema's zijn regex-regels op de 5,214 tekstcommentaren, handmatig gecontroleerd op precisie met steekproeven per thema. Eén commentaar kan meerdere thema's hebben. Sentiment is een woordenlijst (positief, negatief, gemengd, neutraal), dus een schatting.
- **Reply Count telt alle reacties**, ook van andere gebruikers. "Onbeantwoord" betekent dus: niemand heeft gereageerd, ook Siraat niet. De export heeft geen auteurskolom; reacties van Siraat zijn niet te scheiden.
- **Belangrijke correctie op eerdere telling**: het bestand van 2 nov schat 32,6% "alleen een tag". In deze export zijn pure naam-tags maar 234 (2,9%). Het verschil zit vrijwel zeker in de 2,200 keyword-commentaren ("Wings", hoofdletter, max. 4 woorden) die de oude regel als tag telde. Instagram-@-vermeldingen lijken in de export grotendeels te ontbreken, dus het echte tag-volume ligt hoger dan 234, maar is niet betrouwbaar te meten.

## 1. Overzicht

### Volume per maand (uniek)

| Maand | Alle | Tekst | Keyword | Tag |
|---|---:|---:|---:|---:|
| 2025-04 | 4 | 3 | 0 | 1 |
| 2025-05 | 80 | 75 | 0 | 1 |
| 2025-06 | 164 | 151 | 0 | 11 |
| 2025-07 | 112 | 100 | 1 | 11 |
| 2025-08 | 137 | 120 | 0 | 14 |
| 2025-09 | 100 | 96 | 0 | 4 |
| 2025-10 | 116 | 110 | 0 | 6 |
| 2025-11 | 764 | 717 | 1 | 28 |
| 2025-12 | 87 | 82 | 0 | 1 |
| 2026-01 | 248 | 242 | 0 | 1 |
| 2026-02 | 686 | 613 | 8 | 4 |
| 2026-03 | 155 | 132 | 2 | 9 |
| 2026-04 | 459 | 404 | 2 | 26 |
| 2026-05 | 2,135 | 404 | 1,596 | 43 |
| 2026-06 | 845 | 439 | 330 | 13 |
| 2026-07 | 271 | 68 | 183 | 10 |
| 2026-08 | 508 | 420 | 44 | 24 |
| 2026-09 | 486 | 438 | 22 | 17 |
| 2026-10 | 637 | 600 | 11 | 10 |

De piek in mei 2026 is één Instagram-creatorpost met een "comment WINGS for the recipe"-actie: 2,072 keyword-commentaren op één post.

### Per platform

| Platform | Uniek | Tekst | Keyword | Negatief (van tekst) | Positief (van tekst) |
|---|---:|---:|---:|---:|---:|
| Facebook | 3,779 | 3,461 | 8 | 34% | 8% |
| Instagram | 4,215 | 1,753 | 2,192 | 10% | 57% |

Facebook is waar de bezwaren staan (oudere doelgroep, objection-video's van het eigen merkaccount). Instagram is vooral creator- en receptcontent en is overwegend positief.

### Top 20 posts op aantal commentaren

Neg/pos/plakt/scam/prijs = % van de tekstcommentaren op die post. Onb. = vragen zonder enige reactie.

| # | Creative (verkort) | Pl. | Totaal | Tekst | Tag | Keyword | Neg | Pos | Plakt | Scam | Prijs | Vragen | Onb. | Periode |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Creator-recept wings, comment-to-DM | IG | 2,311 | 174 | 2 | 2,072 | 1 | 40 | 0 | 1 | 1 | 10 | 7 | mei tot okt 26 |
| 2 | V-10-04 "This is the only pan I'll ever use" | FB | 1,161 | 1,069 | 65 | 2 | 27 | 6 | 14 | 8 | 14 | 347 | 103 | apr 25 tot mrt 26 |
| 3 | TikTok Comment H3 "I really want this pan but it's too expensive" | FB | 410 | 392 | 11 | 0 | 38 | 6 | 16 | 16 | 27 | 83 | 21 | aug 25 tot okt 26 |
| 4 | Creator-recept (whitelisted, Ad Code ...V5R) | IG | 373 | 328 | 0 | 0 | 2 | 81 | 2 | 0 | 1 | 14 | 11 | jun tot okt 26 |
| 5 | Creative #15 Hook 2 "Rating every cookware pan..." | FB | 250 | 238 | 10 | 0 | 28 | 10 | 15 | 15 | 8 | 80 | 74 | aug tot okt 26 |
| 6 | TOXICCOATING-ASMR-LIFETIMEGUARANTEE "No coating did that" | FB | 166 | 132 | 26 | 0 | 32 | 8 | 14 | 20 | 14 | 40 | 28 | mei tot sep 26 |
| 7 | Creator-video "Control over eggs" | IG | 149 | 145 | 0 | 0 | 4 | 69 | 8 | 1 | 1 | 12 | 12 | apr tot sep 26 |
| 8 | Creator-recept Chicken Fricassee | IG | 146 | 98 | 1 | 27 | 4 | 30 | 3 | 3 | 1 | 22 | 7 | mei tot sep 26 |
| 9 | Creator-recept C (feb 2026) | IG | 143 | 132 | 0 | 0 | 3 | 77 | 4 | 2 | 1 | 3 | 3 | feb tot apr 26 |
| 10 | Creator-recept chicken (WL) | IG | 128 | 47 | 0 | 66 | 15 | 47 | 9 | 4 | 4 | 5 | 1 | mei tot aug 26 |
| 11 | @Chef Creative #15 Hook 2 QUIZ | FB | 108 | 106 | 0 | 1 | 34 | 5 | 17 | 16 | 12 | 34 | 34 | sep tot okt 26 |
| 12 | Creator-recept (Ad Code ...M7C) | IG | 105 | 99 | 0 | 0 | 3 | 76 | 2 | 2 | 0 | 1 | 0 | feb tot jun 26 |
| 13 | Creator-recept D | IG | 103 | 88 | 0 | 0 | 0 | 93 | 0 | 0 | 0 | 4 | 0 | feb tot okt 26 |
| 14 | VSL-video "I almost didn't buy this pan" | FB | 97 | 92 | 3 | 0 | 35 | 4 | 18 | 18 | 17 | 23 | 8 | jan tot jul 26 |
| 15 | RVS-angle script Hook 4 | FB | 95 | 92 | 2 | 0 | 49 | 7 | 28 | 16 | 13 | 15 | 5 | jan tot apr 26 |
| 16 | Creative #34 "If you've been thinking about getting a Siraat" | FB | 92 | 89 | 0 | 1 | 42 | 3 | 8 | 25 | 20 | 23 | 19 | aug tot okt 26 |
| 17 | Static "Eggs slide" (Variant 2) | FB | 92 | 88 | 1 | 0 | 39 | 3 | 15 | 12 | 12 | 29 | 4 | nov 25 tot okt 26 |
| 18 | HexClad-vergelijking UGC | FB | 78 | 70 | 7 | 0 | 33 | 7 | 11 | 19 | 10 | 24 | 18 | apr tot sep 26 |
| 19 | COOKPERFORMANCE-OBJCTN-MASTERY UGC | FB | 73 | 46 | 26 | 0 | 35 | 13 | 9 | 28 | 11 | 9 | 0 | apr tot jun 26 |
| 20 | Static "Pizza Stones Were Never Designed for This" | FB | 68 | 67 | 1 | 0 | 19 | 19 | 3 | 9 | 10 | 14 | 6 | jan 26 |

### Tags (deelsignaal)

Naam-tags zijn zeldzaam in deze export (234, 2,9%). Meeste tags absoluut en relatief:

| Creative | Tags | % van commentaren op die creative |
|---|---:|---:|
| V-10-04 "This is the only pan I'll ever use" | 65 | 6% |
| COOKPERFORMANCE-OBJCTN-MASTERY UGC ("I almost didn't buy this pan because I thought") | 27 | 32% |
| TOXICCOATING-ASMR "No coating did that" | 26 | 15% |
| Static "When the Coating Collapses" | 11 | 22% |
| TikTok Comment H3 "too expensive" | 11 | 3% |
| Creative #15 Hook 2 | 10 | 3% |

Lezing: mensen taggen een partner of vriend bij **pijn-herkenning over coating** (Coating Collapse, toxic coating ASMR) en bij een **eerlijk bezwaar dat wordt weerlegd** (Mastery UGC). Ze taggen niet bij de "rating"-video's of bij prijs-hooks. Dat past bij de surveypijn "oude coating bladdert af" (41%).

## 2. Thema's

Basis: 5,214 unieke tekstcommentaren. "Jul-okt 26" = aandeel van het thema dat in juli tot oktober 2026 viel; die maanden zijn 29% van alle tekst, dus alles daarboven groeit.

| Thema | Aantal | % tekst | % FB | % IG | Likes | Posts | Negatief | Jul-okt 26 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Positief algemeen (geen eigenaar, vaak over het gerecht) | 1,154 | 22,1% | 5,2% | 55,6% | 1,211 | 87 | 0% | 10% |
| Plakt / niet anti-aanbak | 639 | 12,3% | 14,9% | 7,0% | 860 | 111 | 87% | **43%** |
| Scam / nep / misleidend / AI | 573 | 11,0% | 14,2% | 4,7% | 67 | 138 | 79% | **45%** |
| Recept / eten | 540 | 10,4% | 2,7% | 25,4% | 1,223 | 55 | 5% | 12% |
| Prijs (te duur of "how much") | 532 | 10,2% | 14,3% | 2,1% | 119 | 99 | 30% | 31% |
| Klacht van bestaande klant | 358 | 6,9% | 8,6% | 3,5% | 563 | 88 | 83% | **47%** |
| Vergelijking RVS | 267 | 5,1% | 6,9% | 1,7% | 646 | 62 | 72% | 34% |
| Vergelijking gietijzer/carbon | 226 | 4,3% | 5,8% | 1,5% | 904 | 44 | 30% | 28% |
| Inductie en fornuistype | 225 | 4,3% | 6,1% | 0,9% | 45 | 41 | 11% | 27% |
| Vlekken, verkleuring, schoonmaak | 206 | 4,0% | 4,9% | 2,2% | 502 | 66 | 50% | 33% |
| Herkomst (China, waar gemaakt) | 189 | 3,6% | 4,6% | 1,8% | 39 | 60 | 47% | 32% |
| Is het echt puur titanium / lagen / aluminium | 181 | 3,5% | 4,9% | 0,7% | 217 | 54 | 33% | **49%** |
| Koopsignaal (waar te koop, link, "I need this") | 161 | 3,1% | 2,5% | 4,2% | 282 | 52 | 4% | 30% |
| Gezondheid, toxisch, PFAS | 145 | 2,8% | 3,9% | 0,6% | 176 | 40 | 36% | 28% |
| Olie/boter nodig | 138 | 2,6% | 3,4% | 1,1% | 211 | 49 | 66% | 39% |
| Maat, set, assortiment | 132 | 2,5% | 3,4% | 0,9% | 130 | 45 | 18% | **45%** |
| Verzending, levering, land | 112 | 2,1% | 2,7% | 1,1% | 315 | 54 | 38% | 29% |
| AI- of acteur-opmerking (los geteld) | 112 | 2,1% | | | | | 29% | |
| Deksel, handgreep, oven | 109 | 2,1% | 2,7% | 0,9% | 33 | 43 | 20% | 37% |
| Eigenaar positief (strikte regel, ondergrens) | 104 | 2,0% | 2,3% | 1,4% | 334 | 50 | 0% | 36% |
| Hitte, voorverwarmen, kromtrekken, bolle bodem | 96 | 1,8% | 2,5% | 0,6% | 167 | 35 | 58% | 25% |
| Garantie en retour | 94 | 1,8% | 2,1% | 1,1% | 128 | 43 | 70% | 34% |
| Goedkoper bij Temu/Ali/Amazon/Walmart (los geteld) | 85 | 1,6% | | | | | 24% | |
| Andere merken (Made In, Our Place, Le Creuset, Kaizen, Okura, Plateful) | 67 | 1,3% | 1,9% | 0,0% | 4 | 38 | 22% | 34% |
| Gewicht | 65 | 1,2% | 1,7% | 0,3% | 110 | 27 | 31% | 43% |
| HexClad / hybride | 55 | 1,1% | 1,4% | 0,3% | 26 | 18 | 25% | **51%** |
| Titanium geleidt slecht / hotspots | 50 | 1,0% | 1,3% | 0,3% | 9 | 23 | 70% | 36% |
| Klantenservice | 48 | 0,9% | 0,8% | 1,3% | 26 | 28 | 56% | 19% |
| Oude coating bladdert af (los geteld) | 36 | 0,7% | | | | | | |
| Cadeau (los geteld) | 22 | 0,4% | | | | | | |
| Vaatwasser | 7 | 0,1% | | | | | | |

Opmerkingen:
- "Eigenaar positief" is een ondergrens: de strikte regel mist veel "love mine". De bredere regel uit het bestand van 2 nov telt 365 (7,1%). Verhouding eigenaar-klacht tegenover eigenaar-lof ligt dus tussen 1:1 en 3:1.
- Twee lange negatieve teksten zijn letterlijk 8 en 5 keer gepost (zelfde schrijver op meerdere ads). In de unieke telling tellen ze per keer mee, omdat elke post apart zichtbaar is.
- Hoogste likes op niet-merkcontent gaan naar pro-gietijzer en pro-RVS-reacties (tot 109 likes). Dat publiek is een luide tegenstem onder de RVS- en gietijzer-angles.

### Citaten per thema (anoniem, letterlijk, interpunctie ongewijzigd)

**Plakt / niet anti-aanbak**
- "When it arrived it worked great but couple washes and it sticks like any stainless, think it does have a coating. Still like it..."
- "I got a couple of this, eggs definitely stick to the pan, I loose 1/3 of my breakfast"
- "I followed the instructions before cooking so that it's non stick. Put a little oil as well but my food still got stuck in."
- "Please someone explain what I have to do so it doesn't stick"
- "Received mine a couple weeks ago and it is phenomenal, just follow directions and it works great."

**Scam / nep / misleidend / AI**
- "These are false advertised cheap pans that are NOT NON STICK! Dont be fooled like me"
- "That is pressed, not hammered! Every pocket is a uniform depth and no two 'hammer' marks overlap."
- "The ai content is pathetic. Creates zero trust in the product."
- "Wow, this guy gets around. Last week he was pretending to be a cardiologist in some other ad."
- "Fake adverts … terrible Pan and zero customer service … plus they delete bad comments"

**Prijs**
- "Looks great but the price is super high even with black Friday big discount. 2. How is this pan over time? 3. How do you need to take care of this pan?"
- "I really want this pan but it's too expensive."
- "No way this thing is 100 percent titanium for that price"
- "How much?  Somebody save me the click"
- "I ordered one and while they are expensive, they will well out last competition."

**Herkomst en "is het echt titanium"**
- "Where the pan was made? Can't really find any info on the ads."
- "Is it solid titanium or coated with a layer of titanium over aluminum?  Truth please!"
- "More lies. Stainless steel bottom. Aluminum  center,  titanium cooking surface. Its NOT solid titanium."
- "This is chinese pan, you can buy it on Aliexpress for one third of the price lol."
- "SCAM.. if the pan is made of a layer of stainless steel, aluminium and titanium (non magnetic materials).. how come a magnet stick to it?"

**Gezondheid, toxisch, PFAS**
- "How do we know this pan is different? How can we be sure it is non-toxic?  Is there aluminum in the pan? What materials are used?"
- "So instead of eating teflon I will be consuming now titanium bits. I dont now whats worse"
- "Teflon is not toxic and human bodies don't digest it ... Just learn how to use a stainless steel pan properly."
- "won't ever have to worry about it flaking chemicals into our food!" (eigenaar)

**Vergelijking RVS, gietijzer, HexClad**
- "Titanium pans, it sticks....if you know how to use cast iron and stainless, they are the best"
- "Honestly, stainless is great, you just need to learn how to cook."
- "How does this pan compare to hexclad pans. I have those, and love them.."
- "That wasn't even a hexclad you compared it to! For sure this fake"
- "I'm safe for now.  I have a stainless steel, a cast iron pan and  a French Le  Creuset  pan.  Eventually, I will invest in your titanium pan."

**Olie, hitte, vlekken, schoonmaak**
- "I want to see a video of someone cleaning it after using butter and cooking 8 eggs"
- "Sure, food doesn't stick…. if you use a liter of oil to cook and once temperature is too high those marks won't come out of the pan."
- "Everything sticks in ,it gets really dark and ugly just after a few uses . I just hope it's healthier ."
- "i've got one of these pans . i can honestly say it's brilliant super easy too clean you can cook at lower temperatures"

**Vragen: inductie, maat, deksel, oven**
- "Is it induction compatible"
- "How is the heat distribution using induction? I'd like one of these but this is a question I can't find an answer to"
- "Would like to have a smaller one, more like maybe 8" for eggs and hot sandwiches."
- "They need to come with lids! Then I would buy a set of them."
- "Can I use it in the oven?"

**Verzending, garantie, retour, service (bestaande klanten)**
- "Hello, could you explain why you lie on your website about free returns but are trying to make me pay up to $230 to ship mine back to China?"
- "Do NOT buy SiraatKitchen products. It's a scam and the company does not honor risk free purchase."
- "Don't waste your money, pure titanium doesn't warp like the bottom of mine did after 3 uses! ... Don't honor lifetime warranty!"
- "I posted a question yesterday... no answer yet."
- "I'm reading very mixed reviews on Trustpilot here in UK so I shall not buy this product, attractive though it appears."

**Positief en koopsignaal**
- "Got one of these, it's the best pan I've ever had."
- "Love my new pans!  I took way too long to decide to order."
- "I love mine! I bought one for my Mom, too!"
- "This would make a great house warming gift!! Such a staple every kitchen needs"
- "Okay we need this pan asap"

## 3. Triangulatie over vier bronnen

Bronnen: comments (deze analyse, % van tekst), tickets (Gorgias, % van 28,814 unieke mensen, 365 dagen), reviews (342 unieke reviewers incl. kritische extra trek, en Trustpilot n=100), survey (post-purchase, per vraag eigen n).

| Thema | Comments | Tickets | Reviews | Survey | Bronnen | Lezing |
|---|---|---|---|---|---:|---|
| Plakt / expectation gap | 12,3% (639), groeit naar 21% in Q4 | 8,5% (2,448); 86 retourverzoeken per 90 d om non-stick | 13%; klacht:lof 1,5:1; TP 24 van 100 | 14,8% "werkt titanium echt"; 2,3% open "stick" | **4/4** | Grootste product- en verwachtingsprobleem. |
| Prijs | 10,2% | laag (prijswoorden 28 per 90 d) | 64, waarvan 35 kritisch | 27,2% bijna-afhaker; 55% in open vraag; 47% "overpriced" | 4/4 | Grootste aankoopdrempel, geen klachtthema na aankoop. |
| Echtheid, scam, China | 11,0% scam + 3,6% herkomst | 2,7% herkomst, 1,3% scam | 16 echtheid, ca. 15 over de ads | 4,9% echtheidswoorden | **4/4** | Vertrouwenstekort, aangewakkerd door AI- en acteurcontent. |
| Echt titanium / lagen | 3,5%, groeit (49% in jul-okt) | 98 per 90 d materiaal/magneet | binnen echtheid | 14,8% "werkt het echt" | 3/4 | Transparantie over 3 lagen ontbreekt in ads. |
| Retourfrictie | 1,8% (70% neg) | **22,7%** retour/refund | 52 noemen het, 88% frictie; TP 27/100 "retour na gebruik" | 0,3% | 3/4 | Post-purchase probleem met compliance-risico (zie 6). |
| Inductie | 4,3% (meest gestelde productvraag) | 1,4% | 8 | 2,0% | 4/4 | Simpele vraag, slecht beantwoord in ads. |
| Maat, deksel | 4,6% samen | deksel 10,3%, maat 3,8% | 19 kritisch | **15,0%** maat/welk product | 4/4 | Groter in tickets en survey dan in comments. |
| Vlekken, schoonmaak | 4,0% | 4,4% kromtrekken/verkleuring | 74 schoonmaak (45 positief) | n.v.t. | 3/4 | Gemengd, uitleg helpt. |
| Gewicht | 1,2% | 1,0% | 43 | 0,4% | 4/4 | Klein maar consistent ("heavier than expected"). |
| Non-toxic als motief | 2,8%, 36% sceptisch | 1,4% | 21, waarvan 15 positief | **68 tot 76%** motief | 4/4 | Motief van kopers, twijfel bij niet-kopers. |
| Cadeau | 0,4% | 0,9%; stijgend (223 tegen 179 per 90 d) | n.v.t. | 18,5% (nov 2025) | 3/4 | Seizoensmotief; comments meten dit niet. |
| Klantenservice | 0,9% | label "No Reply" 16,8% | 86, waarvan 41 kritisch | n.v.t. | 3/4 | Snelheid per mail wordt geprezen; bereikbaarheid niet. |

## 4. Ads: negatief tegenover positief, tags en ROAS

### Koppeling commentaar en ROAS

Join van commentaren aan advertentienamen uit het Meta-performancebestand (365 dagen, beide accounts, spend van minimaal $10k of €10k). 21 advertenties hebben minimaal 30 tekstcommentaren.

| Advertentie (hook) | Tekst | Neg | Pos | Plakt | Scam | Prijs | Spend | ROAS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| TikTok Comment H3 "I really want this pan but its too expensive" | 394 | 38% | 6% | 15% | 16% | 26% | 289,577 | 1.79 |
| V-10-04 "This is the only pan I'll ever use" | 1,076 | 27% | 6% | 14% | 8% | 14% | 237,949 | 1.78 |
| Objection + offer UGC "I almost didn't buy this pan" | 34 | 53% | 3% | 26% | 21% | 15% | 236,157 | 1.71 |
| TOXICCOATING-ASMR "No coating did that" | 144 | 35% | 8% | 17% | 19% | 12% | 188,073 | 1.52 |
| Creative #15 Hook 2 "Rating every cookware pan..." | 229 | 30% | 10% | 16% | 16% | 8% | 150,390 | 1.41 |
| COOKPERFORMANCE-MASTERY UGC | 57 | 35% | 14% | 7% | 30% | 11% | 132,574 | 1.62 |
| HexClad-vergelijking UGC | 86 | 34% | 8% | 10% | 19% | 9% | 131,205 | 1.49 |
| CLEANUPDOUBT "I cooked salmon skin on no oil" | 32 | 38% | 19% | 16% | 9% | 12% | 122,681 | 1.49 |
| RVS-angle Hook 4 | 92 | 49% | 7% | 28% | 16% | 13% | 84,416 | 1.33 |
| Creative #34 | 102 | 42% | 6% | 12% | 24% | 17% | 71,563 | 1.59 |
| Static "Eggs slide" | 88 | 39% | 3% | 15% | 12% | 12% | 48,064 | 1.75 |
| Creative #61 "If you don't want to eat plastic and forever chemicals" | 65 | 58% | 6% | **45%** | 17% | 0% | 35,654 | 1.55 |
| Static "When the Coating Collapses" | 37 | 16% | 22% | 3% | 11% | 14% | 29,061 | 1.30 |
| Creative #71 "Why is Siraat titanium so expensive?" | 62 | 48% | 8% | 21% | 21% | 6% | 16,710 | 1.93 |
| Creator-recept "Marry me Chicken" | 96 | 8% | **73%** | 7% | 1% | 0% | 16,021 | **2.63** |

Bevindingen:
- **Negatieve commentaren voorspellen de ROAS van een ad niet.** Rangcorrelatie (n=20, zonder de creator-ad): negatief +0,20, plakt -0,04, scam +0,25, prijs +0,13. De helft met het hoogste plakt-aandeel heeft gewogen ROAS 1.59, de laagste helft 1.62. Ook "neg hoog" (1.64) tegenover "neg laag" (1.56) wijst niet op schade per ad. Commentaren volgen bereik en publiek (Facebook, 45+), niet conversie.
- Dat maakt ze niet onschuldig: ze zijn publiek zichtbaar op elke ad, ze voeden "scam" en Trustpilot-zoekgedrag ("check out their reviews") en ze zijn het vroegste signaal van de verwachtingskloof die later als retour en ticket terugkomt.
- **Creator-receptcontent op Instagram** is de enige categorie met duidelijk positieve reacties (69 tot 93% positief op vijf posts) en de hoogste ROAS in de lijst (2.63). Nadeel: weinig productvragen, het gesprek gaat over het gerecht.
- **Prijsbezwaar frontaal benoemen werkt**: "too expensive" (1.79 tot 1.99), "Why is Siraat titanium so expensive?" (1.93), "Our pans aren't cheap" (2.04). Dezelfde ads krijgen veel negatieve reacties, maar converteren.
- **Creative #61 trekt bestaande klanten aan om te klagen**: 45% van de reacties gaat over plakken, 31% zijn eigenaar-klachten. Een non-toxic hook met eieren in beeld triggert precies de groep bij wie het niet lukte.
- **RVS-aanval** ("Why your stainless steel pan is lying to you", RVS Hook 4) krijgt de meeste tegenstand (49% negatief, 28% plakt) en een lagere ROAS (1.33 tot 1.42). De RVS-kopers reageren met "learn to cook", en eigenaren schrijven "sticks like stainless".
- **AI- en acteurcontent**: 112 opmerkingen over AI, acteurs of nep-experts. Hooks met "3-star Michelin chef" en "cardiologist"-achtige personages kosten geloofwaardigheid.

### Onbeantwoorde vragen

| Periode | Vragen (tekst) | Zonder enige reactie | Koopvragen (prijs, link, inductie, maat, deksel, verzending) | Zonder reactie |
|---|---:|---:|---:|---:|
| Tot en met juli 2026 | 743 | 233 (31%) | 247 | 37 (15%) |
| **Augustus tot oktober 2026** | **380** | **346 (91%)** | **100** | **79 (79%)** |

- Reactieratio op alle tekstcommentaren: 40 tot 59% per maand tot mei 2026, daarna 15% (juni), 12% (aug), 9% (sep), **7% (okt)**.
- Klachten van bestaande klanten sinds augustus: 162, waarvan **158 zonder reactie**.
- Sinds september draait er een tweede Facebook-pagina (ID eindigend op 564804). Daar is de reactieratio in oktober **3%** (387 tekstcommentaren). Vermoedelijk is die pagina niet gekoppeld aan Gorgias (Gorgias telt 362 Instagram-ad-comments en 1,177 Facebook-tickets in een jaar).
- Onbeantwoorde vragen per thema (hele periode): scam 90%, klantenservice 80%, HexClad 74%, olie 73%, eigenaar-klacht 71%, plakt 67%, gewicht 64%. Inductie (27%) en koopsignaal (30%) worden het best beantwoord.

## 5. Acties per thema, gerangschikt op impact

Impact = volume over vier bronnen x invloed op conversie of retour x snelheid van uitvoeren.

### 1. Plakken: de verwachtingskloof dichten (alle bronnen, groeiend)
- **E-mail**: post-purchase P1 (first) uitsturen op bezorging in plaats van op order, met als enige taak de methode. Onderwerp: "Before your first egg: 90 seconds". Preview: "Preheat, water test, then oil. That's the whole trick." Plus in de welkomflow een eerlijke objection-mail (W2 of W3): "Will eggs stick? The honest answer." De FTL-flow (geen herhaalaankoop, geen review) richten op "having trouble? reply to this mail" vóór een retourverzoek ontstaat.
- **FAQ/PDP**: boven de vouw, niet in de FAQ verstopt: "Titanium is naturally low-stick, not Teflon. Preheat 2 to 3 minutes on medium, wait until water drops dance, add a little oil, and let food release on its own." Dit staat al als FAQ-regel ("not zero-stick like Teflon") maar staat haaks op hero-claims als "Eggs slide".
- **Ad-hook**: eerlijke learning-curve-angle die al bewezen is in comments: "Day one my eggs stuck. Day three they slid. Here's what changed." of "The 90-second water test nobody tells you about." Demo altijd met zichtbare voorverwarming en olie.
- **CS-macro / comment-reply**: "Sorry to hear that. It isn't a coated non-stick, so heat is everything: 2 to 3 minutes on medium, water drops should dance, then a little oil, and wait until the food lets go. Send us a DM with a photo and we'll walk you through it." Nooit "user error" suggereren in het openbaar.
- **Product/gebruik**: insert-kaart met watertest plus QR naar 60-secondenvideo in de doos; overwegen "first egg"-kaart op de handgreepwikkel. De refund policy noemt plakken expliciet "geen defect": daarmee wordt elke verwachtingsfout een retourconflict.

### 2. Reageren op comments herstellen (operationeel, direct)
- Tweede Facebook-pagina koppelen aan Gorgias, inclusief Instagram-ad-comments.
- SLA 24 uur op vragen; standaardmacro's voor de vijf meest gestelde vragen (inductie, prijs, waar gemaakt, deksel/maat, plakt).
- Negatieve commentaren niet verbergen of verwijderen (zie compliance); alleen spam en scheldwoorden.
- 79 koopvragen sinds augustus kregen geen antwoord; prijs en "where can I buy" zijn directe omzet.

### 3. Retourbelofte en policy gelijktrekken (compliance, zie 6)
- **E-mail**: in alle mails "30-day returns" alleen met de echte voorwaarde, of de policy verruimen. Nooit "hassle-free", "risk-free" of "free returns whatever the reason" zolang gebruikte pannen niet terug mogen.
- **FAQ/PDP**: één duidelijke zin bij de knop: wat wel en niet terug kan.
- **CS-macro**: geen kortingsaanbod om te houden als eerste antwoord op een retourverzoek (reviews noemen dat als frustratie).

### 4. Echtheid, herkomst en "is het echt titanium"
- **E-mail**: welkomst-bewijsmail (W3) begint met de bouw: "Yes, there's aluminium inside. Here's why." Daarna labrapport 25895 en de 75-jaar garantie.
- **FAQ/PDP**: "3 layers: a pure titanium cooking surface (the only part that touches food), an aluminium core for even heat and a steel base for induction. Designed in the Netherlands, made by certified partners in Asia." Dit staat in de ticketmacro maar niet in de ads.
- **Ad-hook**: "Is it solid titanium? No. And that's the point." Toon de doorsnede en een magneet op de bodem.
- **CS-macro**: één vaste comment-reply op "where is it made?" en "is it solid titanium?" met dezelfde zin als de PDP.
- **Product**: het woord "hammered" wordt betwist ("pressed, not hammered"); claim nalopen op "hand-hammered" in ads.

### 5. Prijs
- **E-mail**: checkout C1 tot C3 en welkom W4: kosten per jaar ("a pan you won't replace"), "You Already Replaced It Twice"-framing (ROAS 2.47 als static), plus Shop Pay Installments in de US.
- **FAQ/PDP**: "Why does it cost more than a non-stick pan?" met levensduur en garantie.
- **Ad-hook**: doorgaan met frontale prijs-hooks; nieuw: "How much? Somebody save me the click." met de prijs in de eerste seconde.
- **CS-macro**: op "how much?" altijd de prijs plus link geven, niet alleen "check our website".

### 6. Inductie en fornuistype
- **FAQ/PDP**: icoonrij onder de prijs: "Induction, gas, electric, ceramic. Oven-safe." Flat-top-gebruikers krijgen een eigen tip (lagere stand, langer voorverwarmen).
- **Ad**: tekstoverlay "Works on induction" in de eerste 3 seconden van video's die op Facebook draaien.
- **CS-macro**: "Yes. The steel base makes it work on induction, gas, electric and ceramic."
- **E-mail**: in P1 één regel per fornuistype.

### 7. RVS- en gietijzer-verdedigers
- **Ad-hook**: niet aanvallen maar aanvullen: "Love your cast iron? Keep it. This one is for eggs, fish and anyone who wants half the weight." De angle "your stainless steel pan is lying to you" uitfaseren.
- **E-mail**: vergelijkingsblok `vs kind="steel"` of `kind="castiron"` met de twee eerlijke gedeelde rijen (ook voorverwarmen).
- **CS-macro**: geen discussie aangaan; één vriendelijke reply ("Both are great pans. Titanium is lighter and needs no seasoning.").

### 8. Maat en deksel
- **FAQ/PDP**: maat meten uitleggen (bovenrand tegenover bodem), en welke deksel past bij welke pan. "Do they come with a lid?" komt terug in comments, tickets (deksel 10,3%) en reviews.
- **E-mail**: browse en cart: "Which size is right for you?"-blok; post-purchase P3 deksel als cross-sell.
- **Product**: wens naar een 8 inch eierpan en een tweehandige pan komt meerdere keren terug.

### 9. Olie en "no oil"-claims
- **Ad**: "no oil"-demo's (salmon skin "on no oil") niet meer gebruiken of uitleggen; 138 commentaren gaan over olie, 66% negatief.
- **FAQ/PDP**: "A little oil, like any uncoated pan."

### 10. Vlekken en verkleuring
- **E-mail**: P2 (care) met "brown or rainbow marks are heat patina, not damage" en de baking soda-routine.
- **FAQ/PDP en CS-macro**: dezelfde zin. Garantie dekt verkleuring niet: dat vooraf zeggen.

### 11. Creator-receptcontent en comment-to-DM
- **Ad**: meer whitelisted creator-recepten op Instagram (positieve omgeving, hoogste ROAS in de set).
- **E-mail**: de 1,945 "Wings"-commentaren zijn DM-leads. Controleren of de DM-automatisering e-mails vastlegt in Klaviyo; zo niet, de DM laten eindigen met een opt-in voor het recept per mail ("Get the recipe + 9 more in your inbox").

### 12. Cadeau (seizoen)
- **E-mail**: alleen in Q4: cadeau-angle en "gift receipt"-regel (tickets vragen om geen prijs op de pakbon).
- **FAQ**: "Can I send it as a gift without prices?"

## 6. Compliance-risico's (expliciet voor Floris)

1. **Retourbelofte tegenover refund policy.** De site belooft "30-Day Returns, hassle-free guarantee" en "free returns". De refund policy zegt dat gebruikte producten niet terug kunnen tenzij ze defect zijn, en dat plakken geen defect is. Comments (94 over retour en garantie, 70% negatief), reviews (46 van 52 retour-reviews negatief) en tickets (22,7% retour/refund) laten zien dat klanten dit als misleidend ervaren ("does not honor risk free purchase", "$230 to ship mine back to China"). Een belofte op de PDP die de policy niet waarmaakt is een risico onder de FTC-regels voor misleidende claims en geeft chargebacks. Advies: óf de policy verruimen (30 dagen, ook gebruikt), óf de belofte overal beperken tot de echte voorwaarde. In e-mails nu al geen "hassle-free", "risk-free" of "money back guarantee".
2. **Reviewaantallen en dubbele reviews.** De productpagina toont "4.8 · 38,393 reviews", de widget op dezelfde pagina 2,289 en de categoriekaarten 3,281. In een steekproef van 300 on-site reviews is 52% tekst herhaald onder andere namen. Daarnaast meldt een klant een kortingsaanbod voor een review. De FTC-regel over reviews en testimonials (16 CFR deel 465, sinds oktober 2024) verbiedt nep- of misleidende reviews en reviewaantallen, en het onderdrukken van negatieve reviews. Commentaren noemen dit al ("I fell for the bot reviews", "they delete bad comments"). Advies: alleen een verifieerbaar aantal tonen, duplicaten verwijderen, geen reviewtellingen in e-mail of ads tot dit is opgeschoond, en negatieve ad-comments niet verbergen. DECISIONS.md (7 okt) noemt dat Floris het Trustpilot-incentiverisico accepteert; deze bevindingen gaan verder dan dat.
3. **"Eggs slide" tegenover de plakklachten.** De static "Eggs slide" (ROAS 1.75, nog actief tot oktober) en "no oil"-demo's tegenover 639 plakcommentaren, 2,448 tickets en de eigen FAQ ("not zero-stick like Teflon"). Een demo moet representatief zijn voor normaal gebruik. Advies: in elke eierdemo de voorverwarming en de olie in beeld en in tekst, "Eggs slide" vervangen door "Eggs release" met de methode erbij, en in e-mail nooit "nothing sticks".
4. **Kleinere punten**: advertentienaam bevat nog "LIFETIMEGUARANTEE" terwijl het besluit "75-year warranty" is (check de copy in die ad); "hand-hammered" wordt betwist; acteurs als "Michelin chef" of arts moeten echt zijn of als acteur worden aangeduid (FTC Endorsement Guides).

## 7. Aansluiting op de quiz-popup (4 antwoorden)

| Quiz-antwoord | Survey | Comments | Oordeel |
|---|---|---|---|
| Non-toxic ("Ditch the toxins") | Nummer 1 motief, 68 tot 76% | Weinig genoemd (2,8%) en 36% sceptisch: "how can we be sure it is non-toxic?", "is there aluminum?", "Teflon is not toxic". Non-toxic hooks (#15, #61, toxic coating ASMR) trekken veel plak- en scamreacties. | **Bevestigd als motief, met voorwaarde.** De welkomflow voor dit antwoord moet binnen twee mails bewijs geven (labrapport 25895, 3-lagenbouw, wat het eten raakt) en de techniek uitleggen, anders volgt teleurstelling. |
| Oude coating bladdert af | 41% pijn | 36 directe vermeldingen (0,7%), maar de static "When the Coating Collapses" heeft het hoogste tag-aandeel (22%) en het laagste negatief-aandeel (16%) van alle Facebook-ads. | **Bevestigd als deelbare pijn.** Sterkste emotionele ingang; mensen taggen er anderen bij. |
| Overstap van RVS | 41% vergeleek met RVS | 267 RVS-commentaren, 72% negatief; de meest gelikete reacties zijn pro-RVS en pro-gietijzer. Eigenaren schrijven "sticks like stainless". | **Deels tegengesproken.** Niet framen als "RVS is slecht". Wel: "Lighter than stainless, no seasoning like cast iron, same preheat habit." Eerlijk zeggen dat de techniek lijkt op RVS. |
| Cadeau | 18,5% (nov 2025), 1,7% (mrt tot mei 2026) | 22 vermeldingen (0,4%); comments meten dit motief niet. Tickets met cadeautaal stijgen (223 tegen 179 per 90 d). | **Neutraal, seizoensgebonden.** Alleen tonen in Q4; flow met levertijd tot de feestdag en gift-receipt. |

Suggestie voor een vijfde antwoord: **"I'm tired of replacing pans"** (levensduur, 75 jaar garantie). De static "You Already Replaced It Twice" haalt ROAS 2.47 en de survey noemt "lifetime value" (5,3%) en "lifetime guarantee" (9,4%). Het vermijdt de plakbelofte en sluit aan op het prijsbezwaar.

## 8. Klanttaal: 30 sterke zinnen (letterlijk, anoniem)

Positief en ervaring
1. "Got one of these, it's the best pan I've ever had."
2. "I took way too long to decide to order."
3. "Love love mine was worth every penny"
4. "it's been a complete game changer"
5. "you can cook at lower temperatures"
6. "Received mine a couple weeks ago and it is phenomenal, just follow directions and it works great."
7. "you get what you pay for"
8. "I was sceptical but now I have one" (ingekort)
9. "won't ever have to worry about it flaking chemicals into our food"
10. "I really cook eggs and they don't stick!!"
11. "Easy to clean and heats very quickly (need less heat.)"
12. "Love these pans!! Light weight, easy clean!"
13. "the light weight of a super high quality pan is incredible"
14. "I love mine! I bought one for my Mom, too!"
15. "I have the collection. It doesn't get better!"
16. "This would make a great house warming gift!!"
17. "Honey this pan is beautiful and so is the dish!"
18. "Okay we need this pan asap"

Bezwaren die als hook werken (vraag of twijfel van de klant zelf)
19. "I really want this pan but it's too expensive."
20. "How much?  Somebody save me the click"
21. "How can we be sure it is non-toxic?"
22. "Is it solid titanium or coated with a layer of titanium over aluminum?  Truth please!"
23. "Where the pan was made? Can't really find any info on the ads."
24. "I want to see a video of someone cleaning it after using butter and cooking 8 eggs"
25. "How is this pan over time?"
26. "Every no-stick pan I've ever bought loses its non-stick after about a year of use."
27. "I'm safe for now. ... Eventually, I will invest in your titanium pan."
28. "I'd like one of these but this is a question I can't find an answer to"
29. "Please someone explain what I have to do so it doesn't stick"
30. "Would like to have a smaller one, more like maybe 8" for eggs"


## 9. Wat ontbreekt en vervolg

- Auteurskolom in de export (om Siraat-reacties te scheiden van gebruikersreacties) en de tweede Facebook-pagina expliciet in de Gorgias-koppeling controleren.
- Adnova-commentaarveld gaf in de performance-export overal 491; daarom is ROAS hier op naam gekoppeld (21 ads). Een export met ad-ID per commentaar maakt de koppeling exact.
- De "Wings"-DM-flow: aantal e-mailadressen dat daaruit in Klaviyo kwam is onbekend.
