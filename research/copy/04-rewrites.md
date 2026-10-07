# 04 · Rewrites per mail, klaar om in te bouwen

Datum: 7 oktober 2026. Status: voorstel, wacht op akkoord van Floris. De HTML is niet aangepast.
Wat blijft: het aanbod (HI10, $70 in gifts, unieke codes met hun termijn), de opbouw uit PLAYBOOK 11 (codebalk, header, hero met aanbodbalk, cart/product, knop, iconen, gifts, features, reviews, knop, Benjamin, footer). Wat verandert: de woorden.
Basis: `01-dr-research.md`, `02-awareness-map.md`, `03-copy-audit.md`, `06-offer-design.md`.

## Leeswijzer

- **Onderwerpen**: 5 per mail, type tussen haken: curiosity+benefit (C+B), specificity (SPEC), question (Q), story (STORY), offer (OFFER). Principe erachter: Rec, Com, SP, Aut, Sca, Uni, Lik.
- **Aanbevolen A/B**: één variabele. Waar mogelijk een principe-test (SP tegen Aut, Sca tegen Lik), winnaar op unieke kliks, daarna omzet per ontvanger (PLAYBOOK 6).
- **Hero**: `LABEL` / `Regel1|Regel2` / subregel (max ~45 tekens). De aanbodbalk onder de hero (`--offer=...`) blijft zoals hij is.
- **Opener**: de eerste zin(nen) live tekst na hero en knop.
- **Kernalinea's**: alleen waar de audit zwak was.
- **Knop** (ik-vorm, voordeel) en **friction reducer** (regel onder de knop: risk reversal + social proof + gemak).
- **Reviews**: `{{BLOCK:reviews}}` q1/n1/q2/n2. Alleen echte reviews, alleen ingekort met "...", geen woord veranderd (ook geen typfouten verbeterd). Max 120 tekens, lengteverschil max 30. Elke regel is met een script tegen `content/reviews/reviews.csv` gecontroleerd (zie onderaan). Het reviewblok toont 5 sterren, dus alleen 5-sterrenreviews in het blok.

Beleidsregel die overal geldt (refund policy, `content/facts/site-pages-and-policies.md`): retourzending van ongebruikte producten is voor rekening van de klant. Dus nooit "free returns" of "free 30-day returns" (staat nu in W2 en W5). Wel: "30-day returns". Defect of beschadigd binnen 30 dagen: refund of vervanging, wij betalen de verzending.

Standaard friction reducers (kies per mail):
- US verkoop: `Free shipping. 30-day returns. 100,000+ happy customers.`
- INT verkoop: `Free shipping, duties paid. 30-day returns. 100,000+ happy customers.`
- Mail met unieke code: `One use, already applied. 30-day returns. 100,000+ happy customers.`
- Klantmails: `Questions about your first cook? Reply. A person on our team answers.`
- Winback: `Free shipping. Same 75-year warranty. 4 gifts with every order.`

Afsluiting: de zin "Just reply. A real person reads every email." alleen nog in C1, W0 en W2. In de andere mails een reply-vraag die bij de mail hoort (staat per mail hieronder). [VRAAG FLORIS: leest Benjamin echt mee? Zo niet, "often me" uit W2 halen.]

## Offer-doorwerking (uit 06-offer-design.md)
- Value stack-blok (`{{BLOCK:stack}}`, nieuw voorstel): W1-A/B, W4-US (als drie tiers), W5, C3-P, C3-S, C4-US, K3, B2-clicked; korte versie in R2 en R2-VIP. Niet in W0, W2, W3, C1, C2, K1, P1, P2.
- Pan Pro Standard 11": `$439  $134  $120.60 with HI10`. Andere maten hebben geen compare-at: geen doorgestreepte prijs.
- 6-delige set: $349 (bevestigd), "about $116 a pan, lid included" of "$104.70 a pan with HI10". Geen compare-at tot Floris die geeft.
- Risk reversal "Two promises" (volledig) in C4 en K3; korte friction reducer elders. Nooit "free returns", "risk-free", "money-back".
- Elke deadline: één zin waarom ("made for you, so it has an end date") en één zin wat er daarna gebeurt ("the regular sale price applies").
- De PFAS water filter is altijd "a chance to win", nooit opgeteld bij de waarde.

---

# CHECKOUT

## Principe-test voor de flow
C2: Authority-onderwerp ("Has the pan in your cart actually been tested?") tegen Social proof-onderwerp ("\"I honestly thought this might be another scam\""). Zelfde mail. Leert ons welk principe niveau-5-twijfelaars over de streep trekt. Daarna C4: Scarcity-onderwerp tegen risk-reversal-onderwerp.

## C1 · 1 uur · niveau 5 · primair Lik, secundair SP
Onderwerpen
1. (C+B) The one question people ask at this step. Answered. · Lik
2. (SPEC) Your titanium pan is saved, exactly as you left it · Com
3. (Q) Something stop you at checkout? · Lik
4. (STORY) "I only need the new one." · SP
5. (OFFER) Your cart, plus 4 gifts, still saved · Rec

Aanbevolen A/B: A = 3 "Something stop you at checkout?" (Lik, vraag, 31 tekens) tegen B = 5 "Your cart, plus 4 gifts, still saved" (Rec). Vervangt "Forgetting something?" (uitwisselbaar met elk merk).
Preview A: `Saved exactly as you left it. Free shipping, and HI10 takes 10% more.`
Preview B: `Free shipping, a mystery gift, the e-book and HI10 on top. One tap back.`
Hero: `YOUR CART IS SAVED` / `Right where|you left it.` / `Free shipping. 4 gifts. 30-day returns.` (39) · principe: Lik + Rec
Opener (één regel direct onder het cartblok, boven de knop):
> "I followed your directions, made scrambled eggs and they came out of the pan perfectly." Marilyn B., verified buyer
(Proof direct onder de cart, PrettyLitter-patroon. Bron R017.)
Kernalinea (vervangt de features-rij, die voor niveau 5 te veel is; als de rij blijft, zie fix):
> Something stopped you? The two questions we hear most at this step: size and stove. The 11-inch is our best seller and suits one or two people. And every Siraat pan has a magnetic base, so it works on induction, gas, electric and ceramic.
Fix als de features-rij blijft: t3 `Metal utensils and the dishwasher` / d3 `No coating to protect. Scrape, rinse, repeat. Covered for 75 years.` ("high heat" eruit.)
Knop: `Complete my order` (blijft). Friction reducer: `Free shipping. 30-day returns. 100,000+ happy customers.`
Reviews:
- q1 (R017, Marilyn B.): "I followed your directions, made scrambled eggs and they came out of the pan perfectly... I only need the new one."
- q2 (R169, Michael G.): "The real test was my egg the next morning... the egg released completely and slid around the pan like it was non-stick."
(Als q1 al als opener staat: q1 = R577 Thomas D. en q2 = R518 Graham C., zie K1.)
Afsluiting: `Hi {{ first_name|default:'there' }}, if something stopped you, I would like to know what it was. Just reply. A real person reads every email.` Benjamin, Founder.

## C2 · dag 2 · niveau 5 met twijfel · primair Aut, secundair SP
Onderwerpen
1. (C+B) Three questions that sort real titanium from the rest · Aut + Rec
2. (SPEC) Report no. 25895, for the pan in your cart · Aut
3. (Q) Has the pan in your cart actually been tested? · Aut
4. (STORY) "I honestly thought this might be another scam" · SP
5. (OFFER) A tested pan, a saved cart, 10% on top · Rec

Aanbevolen A/B (flow-principe-test): A = 3 (Aut) tegen B = 4 (SP).
Preview A: `Ours has. Light Labs tested it for 31 PFAS compounds. Every one below detection.`
Preview B: `James thought so too. Then he ordered the wok and the deep pan.`
Hero: `STILL COMPARING? GOOD.` / `Has it been|tested?` / `Ours has. Report no. 25895.` (27) · Aut
Opener:
> Every pan says non-toxic. Few can show you the paper. Here are three questions to ask any brand, us included. One no, and keep looking.
Kernalinea's (de drie vragen, live tekst):
> **An independent lab report?** Yes. Light Labs, an ISO/IEC 17025-accredited lab, tested our Pan Pro for 31 PFAS compounds. Every one came back below the detection limit.
> **A certificate with a number you can check?** Report no. 25895, released October 30, 2025. Here it is. Read it yourself.
> **A warranty that outlasts you?** 75 years. With no coating to wear through, we can offer it.
Voetnoot onder het certificaat (Made In-stijl):
> Source: Light Labs, Ann Arbor, Michigan. Report no. 25895, released October 30, 2025. Tested product: Titanium Hammered Pan Pro. Every Siraat pan has the same titanium cooking surface.
Fix: alt-tekst cutaway zonder laagdiktes: `Cutaway of the Siraat pan: a titanium cooking surface, an aluminum core for even heat, and a stainless steel base for gas, electric and induction.`
Case-blok (optioneel, vervangt niets, onder de cutaway): R169 Michael G., zie W5.
Knop: `Complete my order`. Tekstlink: `Read report no. 25895 →`. Friction reducer: `Free shipping. 30-day returns. 100,000+ happy customers.`
Reviews:
- q1 (R466, James): "...I honestly thought this might be another scam. But it's real titanium."
- q2 (R555, Gwen): "Awesome pan and peace of mind that I am not ingesting bits of toxins when I cook."
Afsluiting: `Want the full report as a PDF? Reply and we will send it.` Benjamin.

## C3-P · dag 3 · pan-kopers · primair Com, secundair SP
Onderwerpen
1. (C+B) The math on one pan versus three · Com
2. (SPEC) 3 pans + 3 lids: about $116 a pan · Aut
3. (Q) One pan, or three for $349? · Com
4. (STORY) "I ordered one pan to try it out" · SP
5. (OFFER) The 6-piece set, and HI10 still works · Rec

Aanbevolen A/B: A = 3 (Com, blijft) tegen B = 4 (SP).
Preview A: `Three hammered pans and three lids. About $116 a pan, lid included.`
Preview B: `Sunny did. Then: "I'm ordering the set." Here is the math.`
Hero: `ONE PAN OR THREE` / `One pan,|or three?` / `3 pans + 3 lids, about $116 a pan.` (34) · Com
Opener:
> Keep your one pan. That is a good start. But if one pan is always busy in your kitchen, here is the math.
Kernalinea (rekensom, live tekst):
> One Pan Pro with a lid: from $154. The 6-piece set: three hammered pans and three stainless steel lids for $349. That is about $116 a pan, lid included. Same titanium cooking surface on all three, one 75-year warranty for all six pieces, and the same 4 gifts.
Features-kop: `Three pans. One warranty.` (vervangt "Nothing to wear off, times three").
Knop: `Upgrade to the 6-piece set`. Tekstlink: `Keep my one pan and check out`. Friction reducer: `HI10 works on either. Free shipping. 30-day returns.`
Reviews:
- q1 (R025, Sunny C.): "I ordered one pan to try it out. I'm so glad I did. I am so happy with this pan that I'm ordering the set."
- q2 (R006, M. A.): "...They heat quickly and are easy to cook on. We love them. Will likely purchase a set for our daughters at Christmas."
Afsluiting: `Cooking for one or two? Then one pan is the right call. Reply if you are unsure, and I will tell you honestly.` Benjamin.

## C3-S · dag 3 · set-kopers · primair Rec, secundair SP
Onderwerpen
1. (C+B) What ships in the box with your set · Rec
2. (SPEC) $70 in gifts ship with your set · Rec
3. (Q) Is a set the right first step? · Com
4. (STORY) "I've replaced all the pans and some pots in our kitchen" · SP
5. (OFFER) Your set, 4 gifts, and 10% on top · Rec

Aanbevolen A/B: A = 2 (Rec) tegen B = 4 (SP).
Preview A: `Free shipping, a mystery gift, the e-book and a chance at a PFAS water filter.`
Preview B: `One decision, every pan on your stove done. And HI10 takes 10% more.`
Hero: `4 GIFTS WITH YOUR SET` / `Every pan,|one decision.` / `One 75-year warranty covers it all.` (35) · Rec + Aut
Opener:
> A set is a bigger decision than one pan. Here is what it settles: every pan on your stove gets the same titanium cooking surface, the same 75-year warranty, and nothing on it to wear through. You make this choice once.
Features-kop: `What a set settles` (vervangt "Bought once. Built for life.").
Knop: `Complete my order`. Friction reducer: `Free shipping. 30-day returns. 100,000+ happy customers.`
Reviews:
- q1 (R530, Lauren W.): "I ordered a full set of the titanium cookware... All of it works as stated. It's also super lightweight. Easy to clean."
- q2 (R542, Jibz C.): "We ordered almost all the pans and some in different sizes too. I've replaced all the pans and some pots in our kitchen."
Afsluiting: `Not sure which pieces you need? Tell me what you cook in a normal week and I will tell you.` Benjamin.

## C4-US · dag 4 · laatste mail · primair Sca, secundair risk reversal
Onderwerpen
1. (C+B) Why your code has an end date · Sca
2. (SPEC) 10% off your cart. Code applied. 48 hours. · Sca
3. (Q) Still deciding on your cart? · Lik
4. (STORY) "They honored the warranty" · SP + risk reversal
5. (OFFER) 10% off your cart, for 48 hours · Sca

Aanbevolen A/B: A = 5 (Sca, blijft) tegen B = 4 (risk reversal/SP). Volgt op de C2-test.
Preview A: `Your personal code is already applied. After 48 hours, the regular sale price.`
Preview B: `Brandon sent one photo. Your cart is 10% off for 48 hours.`
Hero: `LAST EMAIL ABOUT YOUR CART` / `Your cart,|10% less.` / `Your own code. 48 hours, then it ends.` (38) · Sca
Opener:
> This is the last email about your cart. Your personal code takes 10% off and works for 48 hours. It is one code, made for you, so it has an end date. After that, the regular sale price applies.
Kernalinea (risk reversal, onder het offerblok):
> Still unsure? An unused pan can go back within 30 days of delivery. If it arrives damaged or with a defect, you choose a refund or a new one, and we pay the shipping. After that, the 75-year warranty covers dents, a warped base, and a loose handle or rivet.
Knop: `Complete my order`. Friction reducer: `One use, already applied. 30-day returns. 100,000+ happy customers.`
Reviews:
- q1 (R240, Brandon W.): "Siraat replaced a pan free of charge... I just sent them the picture and they honored the warranty."
- q2 (R583, Scott Y.): "Teflon coated ceramic coated... All failed... We suspect they will be the last pans we ever have to purchase."
12-delige set onderaan blijft.
Afsluiting: `After 48 hours your code stops working and the regular sale price applies. A question first? Reply.` Benjamin. (Bestaande zin, sterk.)

## C4-INT · zelfde als C4-US, met
Hero-subregel: `Your own code. Duties paid. 48 hours.` (37)
Extra regel in de kernalinea: `Shipping is free and duties are paid, so there is nothing more to pay at your door.`
Friction reducer: `Free shipping, duties paid. 30-day returns. 100,000+ happy customers.`
Reviews: zelfde als C4-US.

---

# CART

## Principe-test voor de flow
K2-new: Authority/logica (de som) tegen Social proof (Scott Y.). K3: Liking/risk reversal ("What if it's not for you?") tegen Scarcity ("Your personal 10%, good for 48 hours").

## K1 · 1 uur · niveau 4 tot 5 · primair Rec, secundair SP
Onderwerpen
1. (C+B) The cleanup trick for the pan in your cart · Rec
2. (SPEC) One pass with a damp cloth. · Rec
3. (Q) How long do you scrub a pan? · Rec
4. (STORY) "Cleaning the pan afterwards was so easy" · SP
5. (OFFER) Your cart and 4 gifts, saved · Rec

Aanbevolen A/B: A = 2 (blijft, SPEC) tegen B = 3 (Q). Beide Rec, test vorm.
Preview A: `No scrubbing. That is the whole trick. And 4 gifts ship with it.`
Preview B: `On titanium: one pass. Here is why, plus your saved cart.`
Hero: `STILL IN YOUR CART` / `One wipe.|No scrubbing.` / `Your cart is saved, with 4 gifts.` (32) · Rec
Opener:
> Here is what cleanup looks like on titanium. Let the pan cool. Warm water, a soft sponge, one pass. There is no coating, so there is nothing to scrub around.
Knop: `Finish my order`. Friction reducer: `Free shipping. 30-day returns. 100,000+ happy customers.`
Reviews:
- q1 (R518, Graham C.): "We cooked the best omelette we have ever eaten... Cleaning the pan afterwards was so easy."
- q2 (R553, Fran G.): "I am so happy to throw away my old Teflon pans... They disperse the heat very well, are non stick and are easy to clean."
Afsluiting: `Cooking on induction, or not sure about the size? Reply and ask.` Benjamin.

## K2-new · dag 2 · niveau 4, prijs-twijfel · primair Aut (som), secundair SP
Onderwerpen
1. (C+B) Why the $30 pan costs more · Aut
2. (SPEC) 15 pans or 1: the real price of a coated pan · Aut
3. (Q) How many pans have you thrown out since 2020? · Uni
4. (STORY) "Teflon coated ceramic coated, all claimed to be nonstick" · SP
5. (OFFER) The pan in your cart, 10% less with HI10 · Rec

Aanbevolen A/B (flow-principe-test): A = "The pan you keep replacing is the expensive one" (huidige A, Aut, bewezen hook) tegen B = 4 (SP).
Preview A: `Even if a coated pan lasted 5 years, that is 15 pans in 75. Here is the math.`
Preview B: `Scott Y. and his wife tried them all. This is what they bought last.`
Hero: `THE REAL PRICE` / `15 pans,|or one.` / `The math on the pan in your cart.` (33) · Aut
Opener:
> Say a good coated pan lasts 5 years. That is a generous guess. Over the 75 years our warranty runs, that is 15 pans.
Kernalinea (rekensom, vervangt "$30 every two years / $1.79 a year"):
> | | |
> | --- | --- |
> | 15 coated pans at $30 | $450, and still cooking on a coating |
> | 1 Siraat Pan Pro 11" | $134, nothing on it to wear off |
> Covered for 75 years against dents, a warped base, and a loose handle or rivet. With HI10, another 10% off today.
> Footnote: `Based on the Titanium Hammered Pan Pro Standard (11") at $134 and a $30 coated pan replaced every 5 years. What the warranty covers →`
Case-blok "ONE CUSTOMER, START TO FINISH" (R583, Scott Y., Crepe Pan Pro, april 2026):
> "My wife and I have gone through many different pans. Teflon coated ceramic coated, all claimed to be nonstick. All failed... Also the coatings eventually separated from the pan. These hammered Titanium pans from Siraat have been the best we have owned yet. We suspect they will be the last pans we ever have to purchase."
Knop: `Finish my order`. Friction reducer: `Free shipping. 30-day returns. 100,000+ happy customers.`
Reviews:
- q1 (R339, Jonathan D.): "Fantastic product which has no coating that could eventually flake off... This is definitely a life long pan!"
- q2 (R560, Donna G.): "We received our frying pan and absolutely love it! Might be the last one I ever have to buy" (emoji aan het eind weggelaten)
Afsluiting: `Not sure which size fits your stove? Reply with what you cook most and I will tell you honestly.` (bestaand)

## K2-returning · dag 2 · klant · primair Lik, secundair SP
Onderwerpen
1. (C+B) Your next pan cooks like the first · Lik
2. (SPEC) Same titanium, same 4 gifts, same free shipping · Rec
3. (Q) Adding to your Siraat kitchen? · Com
4. (STORY) "I am on my 4th pan from Siraat" · SP
5. (OFFER) HI10 still takes 10% off your cart · Rec

Aanbevolen A/B: A = 3 (Com, blijft) tegen B = 4 (SP).
Preview A: `You know how it works. Your cart is saved, and HI10 still takes 10% off.`
Preview B: `Tammy is. She gave one to her son, too. Your cart is saved.`
Hero: `WELCOME BACK` / `You know|this pan.` / `Same titanium. Same 4 gifts.` (28) · Lik
Opener:
> You know how this works: medium heat, the water test, a little oil. This one cooks the same way. Your cart is saved, and HI10 still takes 10% off.
Offerblok eyebrow: `STILL WORKS FOR YOU` (vervangt "A THANK-YOU FOR COMING BACK": HI10 is publiek, geen persoonlijk bedankje).
Knop: `Finish my order`. Friction reducer: `Free shipping. Same 75-year warranty. 4 gifts with every order.`
Reviews:
- q1 (R138, Tammy): "I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns."
- q2 (R547, Don J.): "This is my second purchase of Siraat frying pans in just a couple of weeks too, and I must say, they are the best!"
Afsluiting: `Which pan do you reach for most? Reply and tell me. It shapes what we make next.` Benjamin.

## K3 · dag 3 · laatste mail · primair Sca, secundair Aut (garantie)
Onderwerpen
1. (C+B) The last email about your cart (and a code) · Sca
2. (SPEC) Covered 75 years. Returnable 30 days. 10% off. · Aut
3. (Q) What if it's not for you? · Lik
4. (STORY) "I returned my pans, unused, and received a refund" · SP
5. (OFFER) Your personal 10%, good for 48 hours · Sca

Aanbevolen A/B (flow-principe-test): A = 3 (Lik, risk reversal) tegen B = 5 (Sca). Onderwerp wijkt nu af van C4 (dat was dubbel).
Preview A: `Then it goes back unused within 30 days. And your 10% code is in here.`
Preview B: `Applied to your cart with one tap. It ends 48 hours after this email.`
Hero: `YOUR CODE · 48 HOURS` / `The last email|about your cart.` / `Your own 10% code, good for 48 hours.` (36) · Sca
Opener (vervangt "STILL IN YOUR CART?"):
> This is the last email about your cart, so here is everything that protects you if you order. Unused, it can go back within 30 days of delivery. Damaged or defective, you choose a refund or a new one, and we pay the shipping. After that, the 75-year warranty covers it. And your personal code takes 10% off for the next 48 hours.
Features-kop: `What protects you` (vervangt "No risk on your side."; "no risk" is te sterk, retourzending is voor de klant).
Knop: `Finish my order`. Friction reducer: `One use, already applied. 30-day returns. 100,000+ happy customers.`
Reviews (blijven, matchen al):
- q1 (R273, Steven T.): "I returned my pans, unused, and received a refund, no questions asked. Easy return procedure."
- q2 (R240, Brandon W.): "Siraat replaced a pan free of charge... I just sent them the picture and they honored the warranty."
Afsluiting: bestaande zin houden ("Reply, I would rather answer it than lose you to a guess.").

---

# BROWSE

## Principe-test voor de flow
B1: Authority/mechanisme ("The pan with nothing to scratch off") tegen Social proof/verhaal (Carole en de spatel van haar moeder). B2-clicked: Scarcity tegen SP.

## B1 · 4 uur · niveau 3 tot 4 · primair Aut, secundair Rec
Onderwerpen
1. (C+B) What a metal spatula does to the pan you looked at · Aut
2. (SPEC) No coating, so nothing to scratch off · Aut
3. (Q) What does your spatula do to your pan? · Rec
4. (STORY) "I'm so glad I never got rid of it" · SP
5. (OFFER) 10% off the pan you looked at · Rec

Aanbevolen A/B (flow-principe-test): A = "The pan with nothing to scratch off" (huidige B, Aut) tegen B = 4 (SP). De korting zit al in codebalk en hero-balk.
Preview A: `Metal utensils welcome. No coating, and a lab report to prove it.`
Preview B: `Carole kept her mother's metal spatula. Now she uses it on her Siraat pan.`
Hero: `THE PAN YOU VIEWED` / `Nothing on it|to scratch off.` / `Metal spatulas welcome. Plus 4 gifts.` (37) · Aut
Opener (boven de vergelijkingstabel):
> Most pans are a metal body with a coating on top. The coating does the non-stick work, and it is also the part that scratches and wears. This one has a titanium cooking surface and no coating. So use the metal spatula.
Vergelijkingstabel en "Honest note" blijven (sterk).
Knop: `Get 10% off this pan`. Friction reducer: `Free shipping. 30-day returns. 100,000+ happy customers.`
Reviews:
- q1 (R220, Carole): "I've had an old, metal spatula that was my mother's... I can use it with confidence on my pans now."
- q2 (R577, Thomas D.): "This pan is fantastic. Makes all of our others "non stick" seem really sticky."
Afsluiting: `Wondering if it works on your stove? Reply and ask.` Benjamin.

## B2-clicked · dag 2 · niveau 4 · primair Sca, secundair SP
Onderwerpen
1. (C+B) A code for the pan you went back to · Sca + Lik
2. (SPEC) 10% off the pan you looked at, for 48 hours · Sca
3. (Q) Still thinking it over? · Lik
4. (STORY) "I ordered one pan to try it out" · SP
5. (OFFER) Your personal 10%, for the next 48 hours · Sca

Aanbevolen A/B: A = 2 (Sca, blijft) tegen B = 4 (SP).
Preview A: `A personal code, on top of the sale. It ends 48 hours after this email.`
Preview B: `Then Sunny ordered the set. Your personal 10% is inside, for 48 hours.`
Hero: `48 HOURS ONLY · YOUR CODE` / `Your own 10%,|for 48 hours.` / `Then the regular sale price again.` (33) · Sca
Opener:
> You went back to look at the {{ event.Name|default:'Titanium Hammered Pan Pro' }}. So here is a personal code: 10% off, on top of the sale price. It is made for you, so it has an end date, 48 hours after this email. After that, the regular sale price applies.
Knop: `Claim my 10%`. Friction reducer: `One use, already applied. 30-day returns. 100,000+ happy customers.`
Reviews (Nina G. "handle stays cool" eruit):
- q1 (R025, Sunny C.): "I ordered one pan to try it out... I am so happy with this pan that I'm ordering the set."
- q2 (R466, James): "...I honestly thought this might be another scam. But it's real titanium."
Afsluiting: `A question before you decide? Reply.` Benjamin.

## B2-notclicked · dag 2 · niveau 3 · primair SP, secundair Uni
Onderwerpen
1. (C+B) What people wrote after their first week · SP
2. (SPEC) The first egg, the fourth pan, the last Teflon · SP + Uni
3. (Q) What happens in week one? · Com
4. (STORY) Week one, in their words · SP
5. (OFFER) In their words, and 10% off with HI10 · Rec

Aanbevolen A/B: A = 4 (STORY, blijft) tegen B = 2 (SPEC).
Preview A: `The first egg, the second pan, the fourth. And HI10 takes 10% off.` (bestaand)
Preview B: `Four people, four first weeks. Their words, not ours.`
Hero: `100,000+ HAPPY CUSTOMERS` / `In their|words.` / `From skeptics to fourth-pan owners.` (34) · SP
Opener (boven de kaarten):
> Four people, four first weeks. Their words, not ours.
Kaarten (los, geen 120-limiet, wel kort):
- THE FIRST EGG: R017 Marilyn B. (blijft)
- THE FOURTH PAN: R138 Tammy (blijft)
- THE DOUBTER (vervangt Avril): R466 James: "I had actually bought a no-brand titanium pan from China on Amazon before, so I honestly thought this might be another scam. But it's real titanium."
- THE NEXT PAN (vervangt Sonya D.): R025 Sunny C.: "I ordered one pan to try it out. I'm so glad I did. I am so happy with this pan that I'm ordering the set. Getting rid of teflon for good."
Knop: `Get 10% off this pan`. Friction reducer: `Free shipping. 30-day returns. 100,000+ happy customers.`
Afsluiting: bestaand ("Reply with what you cook most. I will tell you honestly whether a Siraat pan fits.") is goed.

---

# WELCOME

## Principe-test voor de flow
Eerst loopt W1 A (code) tegen B (gift card): framing van het aanbod, onderwerp en hero gelijk in beide armen. Daarna W3: Authority ("Has your cookware actually been tested?") tegen Social proof ("\"I was looking specifically for PFAS free cookware\""). Daarna W5: Social proof ("Tammy is on her fourth pan") tegen Offer ("The last note about your 10%").

## W0 · kopers · primair Rec, secundair Com
Onderwerpen
1. (C+B) Before your pan arrives: three steps · Rec
2. (SPEC) 2 to 3 minutes on medium. Then the egg. · Rec
3. (Q) Ready for your first egg? · Com
4. (STORY) Thank you. Now the first egg. · Lik
5. (OFFER) Your cook guide, before the pan arrives · Rec

Aanbevolen A/B: A = 4 (blijft) tegen B = 2.
Preview: `Cold metal grabs your food, hot metal lets it go.` (blijft, chef-citaat)
Hero: blijft `CARE AND USE` / `First heat,|then oil.` / `Your first egg, in three steps.` (31)
Opener (vervangt "This email is not here to sell you anything", dat botst met de deksellink):
> Thank you. You chose a pan with nothing on it to wear off. That also means it cooks a little differently from a coated pan. Three steps, and your first egg slides.
Eerlijke verwachting, onder stap 3:
> The first time, use a thin layer of oil. Sandi did: "it definitely needed just a thin covering of oil, and it cleaned up beautifully."
Knop: `Watch the cook guide`. Friction reducer: `Two and a half minutes, straight from our chef.` (video is 2:34)
Review-kaart: R069 Aggie M. blijft.
Afsluiting: `Stuck on something, literally or not? Just reply. A real person reads every email.` (blijft)

## W1-A en W1-B · 10 min · niveau 2 tot 3 · primair Rec, secundair Aut
Let op testontwerp: onderwerp, preview, hero-kop en volgorde zijn gelijk in A en B. Alleen het aanbodblok verschilt (code tegen gift card).
Onderwerpen
1. (C+B) The pan with nothing on it (and your 10%) · Aut + Rec
2. (SPEC) First orders: December 20, 2024. Your 10% is inside. · Aut
3. (Q) Ever thrown out a pan because the coating wore off? · Uni
4. (STORY) Your entry is in. Here is the pan behind it. · Lik
5. (OFFER) Your 10% is inside (plus $70 in gifts) · Rec

Aanbevolen: tijdens de A/B-test op framing één onderwerp voor beide armen: 1 "The pan with nothing on it (and your 10%)". Na de framingtest: onderwerptest 5 (Rec) tegen 3 (Uni).
Preview: `Your Card Game entry is in. HI10 takes 10% off the sale price, with 4 gifts.`
Hero (A en B gelijk): `THE ORIGINAL, SINCE 2024` / `The pan with|nothing on it.` / `The original hammered titanium pan.` (35) · Aut
Opener (direct na het aanbodblok, vervangt "Your entry is in: a chance at an order refund." als losse regel):
> Your Card Game entry is in. While you wait, here is the pan behind it.
> Most pans are a body with a coating on top, and the coating is the part that wears out. Ours has a pure titanium cooking surface and no coatings. Heat it, add a little oil, and the egg slides.
> We shipped the first ones on December 20, 2024. The look-alikes came after.
Features-fix: d1 `Pure titanium cooking surface. Nothing to flake into your food.` ("cooking" toegevoegd, claimregel).
Gifts-eyebrow: `WITH EVERY ORDER` (bevestigd door Floris: gifts gelden bij elke order; nu staat "WITH EVERY HAMMERED PAN").
Knop: `Claim my 10% + gifts`. Friction reducer: `Free shipping. 30-day returns. 100,000+ happy customers.`
Reviews:
- q1 (R583, Scott Y.): "Teflon coated ceramic coated... All failed... We suspect they will be the last pans we ever have to purchase."
- q2 (R017, Marilyn B.): "I followed your directions, made scrambled eggs and they came out of the pan perfectly... I only need the new one."
W1-B extra: subregel onder de gift card `10% off the sale price. Not a cash card: it applies at checkout.` zodat niemand een geldwaarde verwacht.
Afsluiting: `Not sure which size? Reply and tell me who you cook for.` Benjamin.

## W2 · dag 1 · tekstmail Benjamin · primair Lik, secundair Uni
Onderwerpen
1. (C+B) Why our pans have nothing on them · Aut
2. (SPEC) December 20, 2024 · Aut + curiosity
3. (Q) How many pans have you thrown out? · Uni
4. (STORY) The pan nobody else was making · Lik
5. (OFFER) A note from Benjamin (and your 10%) · Lik + Rec

Aanbevolen A/B: A = 4 (STORY, huidige B) tegen B = 2 (SPEC, 17 tekens: kort en specifiek). Huidige A "Why I started Siraat's Kitchen" is de meest voorspelbare founder-regel.
Preview: `It's Benjamin. I wanted to write to you myself. (Your 10% is in the P.S.)`
Body (platte tekst; [VRAAG FLORIS]-plekken moeten gevuld zijn voordat dit live gaat):
> Hi {{ first_name|default:'there' }},
>
> It's Benjamin. I started Siraat's Kitchen, and you joined us yesterday, so I wanted to write to you myself.
>
> [VRAAG FLORIS: één echte scène. Bijvoorbeeld de pan die Benjamin weggooide, waar en wanneer, of de eerste titanium snijplank in zijn hand. Twee of drie zinnen, met een detail dat alleen hij kan weten.]
>
> We started with titanium cutting boards. Then we made the pan. [VRAAG FLORIS: waarom die stap, in één zin.]
>
> The idea is simple to say and took us a while to get right: a titanium cooking surface, a hammered pattern so less food touches the metal, and nothing on it to wear off. Our first orders shipped on December 20, 2024.
>
> I'll be honest about one thing. A pan with no coating cooks a little differently. Heat it on medium for 2 to 3 minutes, add a little oil, and the egg slides. Skip the heat, and it sticks. We put that in every box, because it is the difference between loving this pan and sending it back.
>
> Look-alikes have appeared since. You will recognize the hammered pattern. Ask them for a lab report. Ours is Light Labs report no. 25895: 31 PFAS compounds tested, every one below the detection limit.
>
> If you have a question, hit reply. A real person reads every email, often me.
>
> Benjamin
> Founder, Siraat's Kitchen
>
> P.S. Your welcome code HI10 still takes 10% off on top of the sale. Every order ships with 4 gifts: free shipping, a mystery gift, our Plastic-Free Home e-book and a chance to win a PFAS water filter. And unused pans can go back within 30 days.
("took us a while to get right" alleen houden als Floris bevestigt dat er een ontwikkeltraject was. "Free 30-day returns" in de huidige P.S. is fout: retourzending is voor de klant.)
Knop onder de P.S.: `Claim my 10% + gifts` (blijft).

## W3 · dag 3 · niveau 2 naar 3 · primair Aut, secundair Rec
Onderwerpen
1. (C+B) Three questions to ask any titanium pan brand · Aut + Rec
2. (SPEC) Report no. 25895: what it says · Aut
3. (Q) Has your cookware actually been tested? · Aut
4. (STORY) "I was looking specifically for PFAS free cookware" · SP
5. (OFFER) Tested, with 10% on top · Rec

Aanbevolen A/B (flow-principe-test): A = 3 (Aut, blijft) tegen B = 4 (SP, R438 David H., 4 sterren: alleen als onderwerp, niet in het 5-sterrenblok).
Preview A: `Ours has. Report no. 25895, from an ISO/IEC 17025-accredited lab.`
Preview B: `David found us that way. Here is what he checked, and what you can check too.`
Hero: blijft `LIGHT LABS REPORT NO. 25895` / `Tested.|Not claimed.` / `31 PFAS tested. Every one below detection.` (44)
Opener (direct onder de knop en tekstlink):
> Every pan says non-toxic. Few can show you the paper. Here are three questions to ask any brand, us included. If one answer is no, keep looking.
Drie vragen: zelfde tekst als C2. Voetnoot als C2.
Knop: `Claim my 10% + gifts`. Tekstlink: `Or read the lab report first →` (blijft). Friction reducer: `Free shipping. 30-day returns. 100,000+ happy customers.`
Reviews:
- q1 (R466, James): "...I honestly thought this might be another scam. But it's real titanium."
- q2 (R555, Gwen): "Awesome pan and peace of mind that I am not ingesting bits of toxins when I cook."
Afsluiting: `Want the full report as a PDF? Just reply.` (blijft)

## W4-US · dag 6 · niveau 3 naar 4 · primair Com, secundair SP
Onderwerpen
1. (C+B) Which size fits your stove (and your household) · Com
2. (SPEC) The 11-inch is our best seller. Is it yours? · SP + Com
3. (Q) Who are you cooking for? · Com
4. (STORY) "They directed me to the mini size" · SP
5. (OFFER) Start with the Pan Pro (10% off already applied) · Rec

Aanbevolen A/B: A = 3 (Com, Our Place "Which One Are You?") tegen B = 5 (Rec, huidige A).
Preview A: `One, two, or a family? Pick your pan by that. Your 10% is already taken off.`
Preview B: `Five reasons, the right size, and your 10% already taken off.`
Hero: `THE ONE MOST PEOPLE PICK` / `Who are you|cooking for?` / `Pick your size. Your 10% is applied.` (36) · Com
Opener (direct na de knop, vóór de maatkiezer; "Five reasons" schuift naar één regel):
> You have read why there is nothing on our pans. Now the practical part: which one. Pick it by who you cook for, not by what looks biggest.
Eén regel in plaats van "Five reasons it's the one":
> No coating. Lab tested, report no. 25895. Metal spatulas and the dishwasher. Every cooktop, oven too. 75-year warranty.
Maatkiezer blijft (prijzen en "with HI10" zijn goed).
Drie instappen blijven (Pan Pro, 6-delige set $349 → $314.10, 12-delige set $599 → $539.10): zie 06-offer-design voor de tier-weergave.
Knop: `Claim my 10% + gifts`. Friction reducer: `Free shipping. 30-day returns. 100,000+ happy customers.`
Reviews (nieuw, nu geen reviewblok):
- q1 (R407, Emma): "I wanted to get something I can pass down to my son as my mum passed her amazing quality pots to me."
- q2 (R138, Tammy): "I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns."
Afsluiting: `Still not sure? Reply with what you cook most and who for. I will tell you which size.` Benjamin.

## W4-INT · zoals W4-US, met
Hero-subregel: `Pick your size. Duties paid.` (28)
Preview A: `One, two, or a family? Pick your pan by that. Free shipping, duties paid.`
Friction reducer: `Free shipping, duties paid. 30-day returns. 100,000+ happy customers.`
Onderwerp 5 wordt `Start with the Pan Pro (your 10% inside)` (blijft).

## W5 · dag 9 · niveau 4 · primair SP, secundair Rec (Sca alleen bij besluit B)
Onderwerpen
1. (C+B) What 100,000+ happy customers found out · SP
2. (SPEC) Tammy is on her fourth pan · SP
3. (Q) What changed Michael's mind? · SP + curiosity
4. (STORY) "I was super skeptical" · SP
5. (OFFER) The last note about your 10% · Rec

Aanbevolen A/B (flow-principe-test): A = 2 (SP) tegen B = 5 (Rec/offer, huidige A).
Preview A: `She gave one to her son, too. And your code HI10 still takes 10% off.`
Preview B: `The last welcome email. HI10 still takes 10% off the sale, with 4 gifts.`
Hero: `100,000+ HAPPY CUSTOMERS` / `Skeptical first.|Then the egg.` / `Last welcome email. HI10 still works.` (36) · SP
Case-blok "ONE CUSTOMER, START TO FINISH" (R169, Michael G., Pan Pro, juli 2026), vervangt de uitgelichte Tammy-quote:
> "I had green pans and they were very maintenance heavy and not very non-stick. My wife had badgered me to get a traditional non-stick but I don't want the forever chemicals. I bought this pan out of desperation... The real test was my egg the next morning. I followed instructions and after a very light nudge, the egg released completely and slid around the pan like it was non-stick... I was super skeptical but this is a now officially my favorite pan."
Reviewblok blijft (Marilyn B. en Sandi R., sterk).
Aanbodkaartje: "The last time we mention it in this series." blijft (waar).
Knop: `Claim my 10% + gifts`. Friction reducer: `Free shipping. 30-day returns. 100,000+ happy customers.`
Fix: "Not for you? Free 30-day returns on unused pans" → `Not for you? Unused pans can go back within 30 days. Every pan has a 75-year warranty.`
Afsluiting: Benjamin.

---

# POST-PURCHASE

## Principe-test voor de flow
P3-pan: Commitment ("Which lid fits your pan?") tegen Reciprocity ("Your thank-you code: 10% off, 14 days").

## P1-first · 1 uur · klant · primair Com, secundair Rec
Onderwerpen
1. (C+B) Good call. Here's what's coming. · Com
2. (SPEC) Order confirmed: your pan, 4 gifts and one tip · Rec
3. (Q) Want the one tip our chef gives everyone? · Rec
4. (STORY) "I only need the new one." · SP
5. (OFFER) Your order is in, with 4 gifts · Rec

Aanbevolen A/B: A = 1 (blijft) tegen B = 3 (Q).
Preview: `Order confirmed. Your 4 gifts, your e-book and the one tip that matters.`
Hero: `ORDER CONFIRMED` / `Good call.|Here's what's next.` / `Your pan, 4 gifts, and one tip.` (31)
Opener (vervangt de claim-zin):
> Hi {{ first_name|default:'there' }}, your order is in. You chose a pan with no coating, covered for 75 years. Here is what happens next, and the one thing to know before it arrives.
Knop: `Download your e-book`. Bouwcheck: link gaat nu naar /pages/faq; moet naar de echte e-book-download. [VRAAG FLORIS: download-URL van het e-book.] Friction reducer: `Questions about your first cook? Reply. A person on our team answers.`
Reviews:
- q1 (R017, Marilyn B.): "I followed your directions, made scrambled eggs and they came out of the pan perfectly... I only need the new one."
- q2 (R143, Sandi R.): "...it definitely needed just a thin covering of oil, and it cleaned up beautifully. I am very impressed."
Afsluiting: bestaand (adres wijzigen, welk deksel past).

## P1-repeat · 1 uur · klant · primair Lik, secundair SP
Onderwerpen
1. (C+B) Round two. Here's what's coming. · Lik
2. (SPEC) Same careful packing, same 4 gifts · Rec
3. (Q) Which pan did you add this time? · Com
4. (STORY) "I am on my 4th pan from Siraat" · SP
5. (OFFER) Same 4 gifts, on the way · Rec

Aanbevolen A/B: A = "Good to see you again" (blijft) tegen B = 1.
Preview: `Your order is in. Same careful packing, same 4 gifts.` (blijft)
Hero: blijft `ORDER CONFIRMED` / `Good to see|you again.` / `Same packing, same 4 gifts.` (27)
Knop: `Read the care guide` (herhaalkoper heeft het e-book al; zelfde blok, ander label en link /pages/care-use). Friction reducer: `New shape? Same rules: medium heat, the water test, a little oil.`
Reviews (nieuw, één rij):
- q1 (R138, Tammy): "I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns."
- q2 (R547, Don J.): "This is my second purchase of Siraat frying pans in just a couple of weeks too, and I must say, they are the best!"

## P2 · levering + 1 dag · klant · primair Rec, secundair Aut (chef) en SP
Onderwerpen
1. (C+B) The one mistake that makes titanium stick · Rec (lus wordt gesloten in stap 1 en 5: te hoog vuur, te vroeg bewegen)
2. (SPEC) 2 to 3 minutes on medium. Then the egg. · Rec
3. (Q) Made your first egg yet? · Com
4. (STORY) If you can do an egg, you can do anything · Aut (chef-citaat)
5. (OFFER) Your free 5-step guide from our chef · Rec

Aanbevolen A/B: A = 4 (blijft) tegen B = 1.
Preview: `Medium on titanium works like high on a normal pan. The chef's five steps.` (blijft)
Hero blijft. Gids blijft (beste copy van de set).
Knop: `Watch the chef video`. Friction reducer: `Two and a half minutes. Then breakfast.`
Reviews (vervangt Marlene en Dawj, die "little to no oil" beloven):
- q1 (R069, Aggie M.): "I followed the instructions; let the pan heat up and did the water test... fried an egg which didn't stick to the pan."
- q2 (R143, Sandi R.): "...it definitely needed just a thin covering of oil, and it cleaned up beautifully. I am very impressed."
UGC-oproep (vervangt "We share the best ones, with your permission"):
> Made your first egg? Send us a photo. We would like to show the next first-timers what it looks like, with your first name, and only if you say yes.
[VRAAG FLORIS: willen we elke week één foto kiezen en tonen? Dan mag dat in de zin.]
Optioneel: deksel-upsell onder de reviews in plaats van midden in de gids (breekt de slide).

## P3-pan · dag 14 · klant · primair Com, secundair Rec + Sca
Onderwerpen
1. (C+B) The lid that fits your pan, 10% off · Com + Rec
2. (SPEC) The lid for your Pan Pro: $53.10 with your code · Rec
3. (Q) Which lid fits your pan? · Com
4. (STORY) Two weeks in. The question we hear most. · Lik
5. (OFFER) Your thank-you code: 10% off, 14 days · Rec + Sca

Aanbevolen A/B (flow-principe-test): A = 3 (Com) tegen B = 5 (Rec).
Preview A: `Here it is, plus two things owners add next. 10% off with your own code.`
Preview B: `Your own code takes 10% off the lid, the board or a second pan. 14 days.`
Hero: `FITS YOUR PAN` / `The lid|that fits.` / `10% off with your code, for 14 days.` (35) · Com
Opener: bestaand is goed ("two weeks in. The question we hear most now: which lid fits?"). Alleen laten staan als support die vraag echt het vaakst krijgt: objections.csv bevestigt lids als terugkerende vraag (41 van 400 tickets), dus mag.
Knop: `Add the lid, 10% off`. Friction reducer: `One use, already applied. Free shipping. 4 gifts with every order.`
Reviews (Nina G. "handle stays cool" en Robert H. eruit):
- q1 (R138, Tammy): "I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns."
- q2 (R241, David): "Bought the wok pan and the experience was amazing... I am considering buying more kitchenware from Siraat!"
(Er is geen 5-sterrenreview over het deksel zelf; Joanna C. "a must have" is 4 sterren. [Verzamelen via reviewflow.])

## P3-set · dag 14 · klant · primair Rec, secundair Sca
Onderwerpen
1. (C+B) The pan your set is missing · Com
2. (SPEC) The crepe pan: $125.10 with your thank-you code · Rec
3. (Q) Crepes or stir-fry? · Com
4. (STORY) "Works like a non-stick but gives crispy output" · SP
5. (OFFER) Two weeks with your set. Your thank-you code inside · Rec

Aanbevolen A/B: A = 1 (zonder "(10% off)") tegen B = 4 (SP).
Preview: `Crepe or wok, 10% off with your own code. It ends 14 days after this email.`
Hero: blijft `FOR SET OWNERS` / `The pan your|set is missing.` / `Crepe or wok, 10% off. Code inside.` (35)
Opener (vervangt "set owners ask us which shape", geen bron voor):
> Two weeks with your set. There are two shapes a set does not cover: the flat one and the deep one. Both are 10% off with your own thank-you code.
Knop: `Add the crepe pan, 10% off`. Friction reducer: `One use, already applied. Free shipping. 4 gifts with every order.`
Reviews (blijven, matchen):
- q1 (R088, Chetan G.): "This is the best crepe pan that I have used that works like a non-stick but gives crispy output like a cast iron pan."
- q2 (R538, Pam B.): "My son bought me the wok for Christmas and he already had the whole set. Great to cook with" (punt na "with" weggelaten; origineel heeft " ." )

## P3-accessory · dag 14 · klant · primair Rec, secundair SP
Onderwerpen
1. (C+B) Now meet the pan · Com
2. (SPEC) The Pan Pro 11": $120.60 with your code · Rec
3. (Q) Ready for the pan? · Com
4. (STORY) "I ordered one pan to try it out" · SP
5. (OFFER) Your thank-you code: 10% off the Pan Pro · Rec

Aanbevolen A/B: A = 1 (zonder "(10% off)") tegen B = 4 (SP).
Preview: `Your thank-you code takes 10% off the Pan Pro. It ends 14 days after this email.`
Hero: blijft `FOR SIRAAT OWNERS` / `Now meet|the pan.` / `Your 10% thank-you code is inside.` (34)
Opener: bestaand ("you started with an accessory. Most people start with the pan.") direct onder de hero zetten.
Knop: `Get the Pan Pro, 10% off`. Friction reducer: `One use, already applied. 30-day returns. Free shipping.`
Reviews:
- q1 (R025, Sunny C.): "I ordered one pan to try it out. I'm so glad I did. I am so happy with this pan that I'm ordering the set."
- q2 (R017, Marilyn B.): "I followed your directions, made scrambled eggs and they came out of the pan perfectly... I only need the new one."

---

# WINBACK

## Principe-test voor de flow
R1: Liking ("How's your pan doing?") tegen Social proof ("What pan owners add next"). R2: Scarcity ("10% off your next piece, for 72 hours") tegen Commitment ("Ready for pan number two?").

## R1-pan · dag 60 · klant · primair SP, secundair Lik
Let op: "New since your last order" is alleen waar voor de 2 Pans + 2 Lids. Niet meer als onderwerp.
Onderwerpen
1. (C+B) What pan owners add next · SP
2. (SPEC) The lid that fits your pan, and a 2-pan bundle · Com
3. (Q) How's your pan doing? · Lik
4. (STORY) "I am considering buying more kitchenware from Siraat!" · SP
5. (OFFER) Two months with your pan. HI10 still works. · Rec

Aanbevolen A/B (flow-principe-test): A = 3 (Lik) tegen B = 1 (SP).
Preview A: `Two months in. Tell us how it's going, and see what owners add next.`
Preview B: `The lid that fits, the wok, the crepe pan. HI10 takes 10% off, with 4 gifts.`
Hero: `TWO MONTHS IN` / `What goes next|to your pan.` / `Same titanium, same 75-year warranty.` (37) · SP
Opener: bestaand, zonder "what is new": `Hi {{ first_name }}, two months with your pan. Here is what pan owners add next. Same titanium cooking surface, same 75-year warranty.`
"NEW"-label alleen bij 2 Pans + 2 Lids als dat product echt na hun order verscheen; anders weg. [Bouwcheck: lanceringsdatum bundel.]
Knop: `Shop with my 10%`. Friction reducer: `Free shipping. Same 75-year warranty. 4 gifts with every order.`
Reviews:
- q1 (R088, Chetan G.): "This is the best crepe pan that I have used that works like a non-stick but gives crispy output like a cast iron pan."
- q2 (R241, David): "Bought the wok pan and the experience was amazing... I am considering buying more kitchenware from Siraat!"
Afsluiting: bestaand is goed ("How is the first pan doing? Reply and tell us, good or bad.").

## R1-set · dag 60 · klant · primair SP, secundair Lik
Onderwerpen
1. (C+B) The shapes a set leaves out · Com
2. (SPEC) Crepe pan, wok, board and tools for your set · Com
3. (Q) Which pan do you reach for most? · Lik
4. (STORY) "He already had the whole set" · SP
5. (OFFER) Your set, one step further. HI10 still works. · Rec

Aanbevolen A/B: A = 1 tegen B = 3.
Preview: `The flat one, the deep one, the tools and the board. HI10 takes 10% off.`
Hero: `FOR SET OWNERS` / `The shapes|a set leaves out.` / `Crepe, wok, board and tools.` (28)
Knop: `Shop with my 10%`. Friction reducer: `Free shipping. Same 75-year warranty. 4 gifts with every order.`
Reviews:
- q1 (R538, Pam B.): "My son bought me the wok for Christmas and he already had the whole set. Great to cook with"
- q2 (R088, Chetan G.): "This is the best crepe pan that I have used that works like a non-stick but gives crispy output like a cast iron pan."

## R2 · dag 90 · klant · primair Sca, secundair Com
Onderwerpen
1. (C+B) A code for your second pan · Sca + Com
2. (SPEC) 10% off your next piece, for 72 hours · Sca
3. (Q) Ready for pan number two? · Com
4. (STORY) "I am on my 4th pan from Siraat" · SP
5. (OFFER) Your personal code, plus $70 in gifts · Rec

Aanbevolen A/B (flow-principe-test): A = 2 (Sca, blijft) tegen B = 3 (Com).
Preview A: `Your own code, applied with one tap. It ends 72 hours after this email.`
Preview B: `If one pan is always busy, here is 10% off the second. For 72 hours.`
Hero: `YOUR CODE · 72 HOURS` / `Pan number|two?` / `Your own 10%, good for 72 hours.` (32) · Com + Sca
Opener (reden voor de code):
> If one pan is always busy, here is a code for the second. It is yours alone and works for 72 hours. After that, it expires and today's prices apply.
Knop: `Shop with my 10%`. Friction reducer: `One use, already applied. Free shipping. 4 gifts with every order.`
Reviews (vervangt Tyrone B. en Virginie M.):
- q1 (R547, Don J.): "This is my second purchase of Siraat frying pans in just a couple of weeks too, and I must say, they are the best!"
- q2 (R138, Tammy): "I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns."

## R2-VIP · dag 90 · 2+ orders · primair Rec, secundair Uni + Sca
Onderwerpen
1. (C+B) Why you're getting 15% (and why it ends) · Rec + Sca
2. (SPEC) 15% off, 72 hours, for customers with 2+ orders · Uni
3. (Q) What should we make next? · Lik
4. (STORY) "I even gifted one to my son" · SP
5. (OFFER) For our regulars: 15% for 72 hours · Uni + Sca

Aanbevolen A/B: A = 5 (blijft) tegen B = 1.
Preview: `You have ordered more than once. This 15% code is yours for 72 hours.` (blijft, ingekort)
Hero: `FOR OUR REGULARS · 72 HOURS` / `You came back.|Here's 15%.` / `Because you ordered more than once.` (35) · Rec + Uni
Opener:
> You have ordered from us more than once. That is the reason for this code: 15% off, on top of the sale, for 72 hours. It is a thank you, so it has an end date.
Knop: `Claim my 15%`. Friction reducer: `One use, already applied. Free shipping. 4 gifts with every order.`
Reviews (vervangt de service-quotes van Olwen T. en David F.):
- q1 (R138, Tammy): "I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns."
- q2 (R542, Jibz C.): "We ordered almost all the pans and some in different sizes too. I've replaced all the pans and some pots in our kitchen."
Afsluiting: bestaand ("What should we make next? Reply and tell me, I read every answer.").

---

## Controle

- Review-excerpts: elk stuk tussen "..." komt letterlijk en in volgorde uit `content/reviews/reviews.csv` (script `research/copy/check_reviews.py`, draaien vanuit de repo-root: `python3 -I research/copy/check_reviews.py`; resultaat 0 fouten op 48 regels bij oplevering). Lengte max 120 tekens, verschil per paar max 30.
- Hero-subregels: allemaal 45 tekens of minder.
- Geen em dashes in dit bestand.
- Geen nieuwe claims: alle feiten uit facts.csv, claims.csv, DECISIONS, brand/proof en de refund policy. Open punten staan als [VRAAG FLORIS].
