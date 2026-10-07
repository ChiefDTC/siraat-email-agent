# 01 · Direct response research, vertaald naar Siraat

Datum: 7 oktober 2026. Opdracht van Floris: haal inspiratie uit de "Direct Response Copy Skill" en maak die bruikbaar voor onze flows.
Bronnen: `research/copy/direct-response-copy-skill.md` (volledig gelezen), `research/copy/influence-based-copywriting.md` (Cialdini in copy), `research/copy/social-proof-copywriting.md` (Daniel Doan, 9 vormen), PLAYBOOK, DECISIONS, `klaviyo/flows/v3-flow-system.md`, `research/ux-2026-10-07/*`, `content/facts/facts.csv` en `claims.csv`, `content/reviews/*`, `content/hooks/*`, `brand/proof/README.md`, `baselines/README.md`, de 31 v3-templates. Eigen onderzoek: WebSearch (4 zoekopdrachten, WebFetch van de bronpagina's werd door de proxy geblokkeerd, dus cijfers uit zoekresultaten staan gemarkeerd) en Email Love (9 calls, 10 mails bekeken).

Taal: notities Nederlands, copy Engels. Geen gedachtestreepjes.

---

## 1. De tien principes die voor ons tellen

### 1.1 Schwartz: schrijf voor het bewustzijnsniveau van de lezer
De skill noemt het "het belangrijkste framework". Minder bewust = langere copy en een andere kop. Most aware = kort, het aanbod, klaar.

Wat het voor ons betekent: onze flows lopen van ongeveer niveau 2 (Alia Card Game-inschrijver die voor een giveaway kwam) tot niveau 5 (iemand die zijn checkout halverwege liet staan). De v3-mails behandelen alle niveaus hetzelfde: elke mail heeft codebalk, hero met 10%, gifts, features, reviews, iconen, drie knoppen. Een checkout-verlater (niveau 5) krijgt drie schermlengtes uitleg; een giveaway-inschrijver (niveau 2) krijgt in W1 bijna geen uitleg en direct een kortingscode. Uitwerking per mail: `02-awareness-map.md`.

### 1.2 Hopkins: reason-why
Hopkins vond voor Schlitz het zuiveringsproces dat elke brouwer had, maar niemand vertelde. Hij won door het uit te leggen.

Onze reason-why, in één keten:
1. Er zit geen coating op het kookoppervlak (puur titanium, "with a pure titanium cooking surface" + "no coatings").
2. Dus er is niets dat kan slijten, afbladderen of in je eten terechtkomen.
3. Dus de pan gaat niet na een paar jaar de vuilnisbak in, en daarom durven we 75 jaar garantie te geven.
4. Maar: zonder coating komt het loslaten van warmte en timing, niet van chemie. Daarom: 2 tot 3 minuten op medium, de waterdruppeltest, een theelepel olie. "Cold metal grabs your food, hot metal lets it go." (chef-video)
5. En het gehamerde patroon zorgt dat minder eten het metaal raakt en de olie zich verdeelt (facts.csv, guidance 8566447).

Stap 4 is onze "Schlitz-water": iedere titaniumpan werkt zo, bijna niemand legt het uit vóór de aankoop. Het is ook het eerlijke antwoord op de grootste klacht (plakken: 81 van 154 lage Trustpilot-reviews in 180 dagen, 60 van 400 tickets). Wie het vóór de aankoop leest, koopt met de juiste verwachting: minder retouren, minder 1-sterrenreviews.

### 1.3 Ogilvy: Rolls-Royce-specificiteit
"At 60 miles an hour, the loudest noise in this new Rolls-Royce comes from the electric clock." Niet zeggen dat het stil is, een detail tonen waaruit de lezer het zelf concludeert.

Wat dat is voor een titanium pan (alleen feiten die we kunnen onderbouwen):

| Vaag (nu vaak) | Rolls-Royce-versie | Bron |
| --- | --- | --- |
| "Lab tested" | "Light Labs tested it for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895." | brand/proof, certificaat 30 okt 2025 |
| "Non-toxic, for real" | "There is nothing on the cooking surface to test for wear. It is titanium all the way to the aluminum core." | facts.csv layers |
| "Easy to use" | "A drop of water should form a ball and glide. That is when the oil goes in." | facts.csv preheat |
| "High performance" | "Medium on titanium works like high on a normal pan." | chef-video |
| "Built to last" | "If it dents, warps, or a rivet or handle comes loose, we replace it. For 75 years." | facts.csv warranty |
| "The original" | "Our first orders shipped on December 20, 2024. The look-alikes came after." | DECISIONS 1 okt |
| "Easy to clean" | "One pass with a damp cloth. Dark marks? Baking soda and water, a soft sponge, done." | hooks.csv, facts.csv |
| "Works on all stoves" | "Magnetic base. Gas, electric, ceramic and induction." | macro 247042 |
| "Customers love it" | "Tammy is on her fourth pan. She gave one to her son." | R138 |

Wat we NIET als specificiteit mogen gebruiken (claims.csv needs-proof): laagdiktes in mm (0.5 mm titanium, 1 mm aluminium, 0.6 mm staal; staat nu in de alt-tekst van C2), ovenbestendig tot 548°C / 1000°F, "30 of 30 tests passed", Mohs-hardheid.

### 1.4 Pijn kwantificeren (ShipFast-som), maar eerlijk
De skill: maak van vage frustratie een getal dat de lezer tegen de prijs kan afwegen.

Wat we hebben:
- Prijs: Pan Pro Standard 11" $134 (products.csv).
- Garantie: 75 jaar tegen defecten (dent, warped base, loose handle, broken rivets, lid that no longer fits). Let op: dat is de garantietermijn, geen gemeten levensduur. Schrijf "covered for 75 years", niet "lasts 75 years".
- Levensduur van gecoate pannen, uit eigen onderzoek (zoekresultaten, bronpagina's geblokkeerd voor volledige verificatie): de Cookware & Bakeware Alliance (VS-brancheorganisatie) noemt 5 tot 7 jaar voor een goede nonstickpan; reviewsites noemen 2 tot 3 jaar voor PTFE en 1 tot 2 jaar voor keramisch. Bronnen: [Ideal Home citeert de Cookware & Bakeware Alliance](https://www.idealhome.co.uk/all-rooms/cookware/whats-the-shelf-life-of-a-non-stick-pan), [America's Test Kitchen](https://www.americastestkitchen.com/articles/5117-how-often-should-i-replace-my-nonstick-pan), [Prudent Reviews](https://prudentreviews.com/how-long-do-non-stick-pans-last/), [Made In blog](https://madeincookware.com/blogs/how-long-do-non-stick-pans-last).
- Intern: in de Notion-brief W41 staat "coating wear = #1 frustration at 41% (survey)". Herkomst van de survey niet gevonden: [VRAAG FLORIS] voordat we het noemen.
- Klantentaal: "No more buying sets every few years" (R153 Wendy S.), "Teflon coated ceramic coated, all claimed to be nonstick. All failed" (R583 Scott Y.), "hexclad lost its within 6 months" (R123, alleen intern; geen concurrent noemen in mail).

De eerlijke som (aanbevolen, vervangt "$30 every two years" in K2-new):
> Say a good coated pan lasts 5 years. That is the cookware industry's own estimate for a quality one.
> Over the 75 years our warranty runs, that is 15 pans.
> 15 x $30 = $450. And you would still be cooking on a coating.
> One Siraat pan: $134. Nothing on it to wear off.

Waarom 5 jaar en niet 1 tot 2: de conservatieve aanname van de tegenpartij maakt de som onaanvechtbaar (Sugarman: "never make claims bigger than your proof"). Zelfs dan wint het. De $30 is een aanname voor een goedkope pan; schrijf het als "a $30 pan" zodat de lezer het voorbeeld herkent, niet als marktgemiddelde.

Tweede vorm (Superhuman-scenario): "The first scratch shows up. Then the egg starts to catch in one spot. Then you are scrubbing a pan that was supposed to be easy, and you are wondering what came off it." Alleen in welcome en K2; geen angst als hoofdtoon (PLAYBOOK 1).

### 1.5 De So What-keten
Feature: geen coating. So what? Niets om af te slijten. So what? Je koopt hem niet opnieuw en je hoeft niet te twijfelen wat er van je pan in je eten zit. So what? Je kookt het ei voor je kind zonder erover na te denken. Dat laatste is waar de copy woont.

| Feature | Functioneel | Financieel | Emotioneel (hier schrijven) |
| --- | --- | --- | --- |
| No coating | Niets om af te slijten | Geen pan om te vervangen | "You stop wondering what came off your pan." |
| Light Labs 25895 | Getest op 31 PFAS | Geen gok met $134 | "You can read the paper yourself, not just the label." |
| 75-year warranty | Defecten gedekt | Laatste aankoop in deze categorie | "The last frying pan you shop for." (als vraag of in klantwoorden, R583) |
| Metal utensil safe | Schraap gewoon | Geen speciale spatels | "Your mother's old metal spatula works again." (R220 Carole) |
| Dishwasher safe | Geen handwas | Tijd | "Dinner is done when dinner is done." |
| Hammered pattern | Minder contact, olie verdeelt | Minder olie | "The egg slides once the white sets." |

### 1.6 Sugarman: slippery slide en Caples: kop = 80 procent
In onze mails is de "kop" de hero (gebakken in het beeld) plus de onderwerpregel. Bevinding: 19 van de 31 hero-koppen gaan over korting ("10% off the pan you looked at", "Your cart, 10% off", "One wipe. 10% off.", "Tested. Then 10% off."), terwijl de aanbodbalk direct onder de kop hetzelfde zegt, de codebalk erboven ook, en de cartregel eronder ook. Het aanbod staat zo 4 tot 6 keer per mail; de ene unieke gedachte van de mail staat nergens groot. Gevolg: alle mails voelen hetzelfde, de lezer leert dat Siraat-mails "10%" zijn, en de kop doet zijn 80 procent niet.

Regel die hieruit volgt: het aanbod staat vast in codebalk en aanbodbalk (UX-standaard blijft). De hero-kop draagt de ene gedachte van die mail (Ogilvy-detail, reason-why, verhaal). De subregel verbindt die met het aanbod.

### 1.7 Testimonials als mini case study
Formule: voor-situatie + actie + uitkomst + tijd + emotie. Nu staan er vooral "great pan"-quotes ("I love my new pan. It looks good, cooks good and cleans good too", "Performs as described. Very pleased", service-quotes van Olwen T. en David F. in de VIP-mail). Die dragen bijna niets. We hebben betere echte reviews, zie §5.

### 1.8 Founder story: kwetsbaarheid, geloofwaardigheid, gedeelde weg
Wat we mogen gebruiken: Benjamin is oprichter; Nederlandse oprichters; begonnen met titanium snijplanken (PLAYBOOK 1); de originele gehamerde titanium pan; eerste orders 20 december 2024; look-alikes daarna; 100,000+ happy customers in iets meer dan een jaar; ontworpen in Nederland, gemaakt in gecertificeerde fabrieken in Azië.
Wat ontbreekt en de founder-mail nu generiek maakt (W2 leest als een persbericht met "The idea was simple"): het moment. Waarom Benjamin. Welke pan hij weggooide. Wat er misging bij de eerste versie. Hoeveel prototypes. Waarom gehamerd. Dat is [VRAAG FLORIS], zie §8. Contrast uit Email Love: de HexClad-founderbrief ("A letter from HexClad's founder", 11 april 2026) bevat geen enkel detail ("we're all about innovation", "one of the fastest-growing cookware companies in America"); de Made In-founderbrief van Chip ("They Trained Dogs to Keep the Knife Makers Warm", 1 sep 2026) opent met een open loop en een echte foto ("It all started in France, when we were just a company of 4 people..."). Wij willen de tweede.

### 1.9 CTA met voordeel en friction reducer
Knoppen zijn al ik-vorm ("Complete my order", "Claim my 10% + gifts"): goed. Wat ontbreekt is de regel eronder: risk reversal + social proof + gemak. Baymard (via zoekresultaten, [Retail Boss samenvatting](https://retailboss.co/10-reasons-for-abandonment-during-checkout-in-the-u-s)): 39 procent haakt af op extra kosten, 19 procent vertrouwt de site niet, 15 tot 18 procent op het retourbeleid. Onze drie friction-feiten raken precies die drie: free shipping, 100,000+ happy customers, 30-day returns. Standaardregel:
> Free shipping. 30-day returns. 100,000+ happy customers.

Per flow een variant in `04-rewrites.md`. Let op: "30-day returns" geldt voor ongebruikte producten (facts.csv). Nooit "risk-free" of "money-back" zeggen (oude 100-dagenbelofte; 100 van 154 lage reviews gaan over retour of de trial).

### 1.10 AI-tells en onze eigen tics
Uit de skill: em dashes, "delve", "unlock", "game-changer", "seamless", hedging, alle alinea's even lang, drieslag-opsommingen, geen "I". Gecontroleerd in de 31 templates: 0 em dashes (goed). Wel onze eigen tics die als sjabloon gaan voelen:
- "Just reply. A real person reads every email." staat in 13 mails bijna letterlijk, plus varianten in de rest. Bij de derde mail is het een formule.
- "Nothing to X, nothing to Y" en "No coating. Ever." in bijna elke features-rij.
- Dubbelepunt-constructies in elke subregel ("Your gift card: 10% on top...").
- "on us", "Good call", "no catch" komen uit het standaard DTC-register.
- "Pure titanium surface" zonder "cooking" (W1, W4): wijkt af van de goedgekeurde claim.

---

## 2. Influence-principes voor Siraat (Cialdini)

Bron: `influence-based-copywriting.md`. Kernregel uit dat document: elke mail gebruikt minstens twee principes bewust, sequenties bouwen op van reciprocity via commitment naar scarcity, en we testen principes, niet alleen woorden. Wat wij echt hebben per principe:

| Principe | Wat wij echt hebben | Waar het nu staat | Hoe we het gebruiken | Wat we NIET doen |
| --- | --- | --- | --- | --- |
| Reciprocity | De gift-stack: free shipping ($15), Plastic-Free Home e-book ($30), mystery gift ($25), kans op een PFAS water filter ($450 waarde). De chef-gids en care-video (gratis, ongevraagd). De drie vragen die je aan elk merk kunt stellen (waarde vóór de vraag). | Gifts-blok in bijna elke mail; chef-gids alleen in W0 en P2 | Geef eerst iets bruikbaars, vraag daarna. W3 en C2 geven de drie vragen weg; W0 en P2 de gids. Overweeg de waterdruppeltest al in browse/K1 weg te geven (vóór de aankoop). | Nooit "free filter" (het is een kans, DECISIONS). Geen "no strings", wel "included". |
| Commitment en consistency | Kleine eerste stap: maat kiezen ("Pick it by who you cook for"), de eerste-ei-gids, "reply with what you cook most", de welcome-deelname zelf (Card Game). Herhaalkopers die al een pan hebben. | W4 maatkiezer, reply-vragen onderaan | Laat de lezer iets kleins kiezen vóór de grote vraag: "Which one are you cooking for: one, two, or a family?" (Our Place "Which One Are You?", 26 sep 2026). Bij kopers: verwijs naar hun eigen keuze ("You chose a pan with nothing on it to wear off."). | Geen schuldgevoel ("you started, now finish"). |
| Social proof | 100,000+ happy customers (DECISIONS). 275 bruikbare geverifieerde reviews, 384 vijfsterren in 180 dagen. Herhaalkopers (Tammy, 4e pan). | Reviewblok + "Join 100,000+ happy customers" onder elke reviewrij | Specifieke mini case studies, gematcht aan de claim van de mail (§5). Aantal als friction reducer onder de knop. | Geen "independent" of "unsolicited" (Trustpilot-incentive, DECISIONS). Geen sterrenscore noemen zolang 26 procent van de notificaties 1 ster is. |
| Authority | Light Labs, ISO/IEC 17025-geaccrediteerd, rapport 25895, 31 PFAS onder detectiegrens, lab director Lev Spivak-Birndorf, Ann Arbor MI. De chef uit de care-video (naam en jaren onbekend: [VRAAG FLORIS]). "The original", eerste orders 20 dec 2024. | W3, C2, features-rij (Light Labs) | Rapportnummer altijd erbij: Our Place gebruikt hetzelfde lab (§6), dus "Light Labs" alleen is geen onderscheid; het nummer, de 31 en het leesbare certificaat wel. Chef-citaten letterlijk uit de video. | De ad-hook "22 years as a chef, hundreds of pans" alleen als die chef echt in de mail-video staat en Floris de cijfers bevestigt. Geen "doctor recommended". |
| Scarcity en urgency | Echt: unieke verlopende Klaviyo-codes (C4, K3, B2-clicked, P3, R2, R2-VIP). Mogelijk echt: de wekelijkse filtertrekking, pas na actievoorwaarden met sluitingstijd en gratis deelname in de VS (04-offer-strategy §6). Niet echt: "reserved", "low stock", "price held". | Offerblok met "Expires 48 hours after this email" | Deadline altijd met reden ("It is a personal code, so it has an end date."). Wat er na de deadline verandert, letterlijk: "After that, it is the regular sale price." | Geen countdown zonder echte einddatum. Geen "last chance" behalve in de echt laatste mail. |
| Unity | Identiteit: "people who cook without coatings", de one-liner "Cook without coatings. Cook without compromise.", klanten die hun oude pannen wegdoen (Marilyn, Fran, Noel), Nederlandse oprichters. | Nauwelijks | Spreek de lezer aan als iemand die al besloten heeft dat coatings niet meer hoeven: "If you have already thrown out one peeling pan, you are one of us." Kopers: "Welcome to the no-coating kitchen." | Geen "tribe", "family", "Siraat fam". Te Amerikaans-corporate voor onze stem. |
| Liking | Benjamin schrijft zelf, antwoordt op reply's, eerlijke beperkingen ("a metal spatula can leave fine marks"). | B1 "Honest note", afsluiting Benjamin | Meer eerlijke beperkingen (de skill: "honest limitations"), minder sjabloonzinnen. | Geen nep-persoonlijkheid ("Hey bestie"). |

Principe-lagen per flow (influence-doc: bouw op van reciprocity naar scarcity):
- Welcome: reciprocity (gifts + giveaway) → authority (W3) → unity/liking (W2 Benjamin) → commitment (W4 maatkeuze) → social proof + scarcity alleen als besluit B (unieke code) loopt.
- Checkout: liking + commitment (C1, jouw keuze staat klaar) → authority (C2) → social proof + commitment (C3) → scarcity met echte code (C4).
- Cart: reciprocity (K1 schoonmaakuitleg) → authority + pijnsom (K2) → scarcity + risk reversal (K3).
- Browse: reciprocity (B1, wat een metalen spatel doet) → social proof (B2).
- Post-purchase: commitment + liking (P1, "good call") → reciprocity (P2 gids) → reciprocity + scarcity (P3 bedankcode).
- Winback: liking + social proof (R1) → reciprocity + scarcity (R2).

---

## 3. Social proof-inventaris Siraat (Daniel Doan, 9 vormen)

| # | Vorm | Hebben we het? | Waar | Hoe sterk | Actie |
| --- | --- | --- | --- | --- | --- |
| 1 | Testimonials als verhaal | Ja, maar we kiezen de zwakke | `content/reviews/reviews.csv` (605 rijen), `reviews-positive-usable.csv` (275 bruikbaar, onder 45 woorden) | Sterk als we de verhaalvormige kiezen (R583, R169, R563, R025) | Shortlist §5, matchen aan de claim |
| 2 | Case studies | Bijna: lange reviews met probleem, oplossing, resultaat (R060 S. S. 900 woorden over keramische skillets en tortilla's, R169 Michael G., R583 Scott Y.) | reviews.csv, usable_in_email = no door lengte | Middel tot sterk | Eén case per flow, ingekort met "...", nooit aangevuld (§5.3) |
| 3 | Expert opinions | Ja: Light Labs, ISO/IEC 17025, rapport 25895, lab director bij naam op het certificaat. De chef uit de care-video. | brand/proof, certificaat-pdf, chef-video | Sterk (lab), middel (chef zonder naam) | Chef: naam, functie, toestemming [VRAAG FLORIS]. Lab: nummer altijd noemen. |
| 4 | Celebrity of influencer | Nee voor mail. Creators in ads (deluxbbq, POV slow breakfast) | hooks.csv, Adnova | Onbekend of toestemming voor mail | [VRAAG FLORIS]: mogen creator-citaten of -beelden in mail? |
| 5 | Social media / UGC | Toestemming ja (DECISIONS 7 okt: klantfoto's mogen). Geen UGC-map gevonden in `content/assets/index.csv` (categorieën: packshot, ad-static, lifestyle, logo). P2 vraagt al om een foto van het eerste ei. | DECISIONS, P2 | Nog leeg | Verzamelen: P2 "first egg"-oproep, reviewflow vraagt om foto, Trustpilot-foto's scrapen zodra het domein open is. |
| 6 | Product reviews | Ja, 384 vijfsterren in 180 dagen, 568 geverifieerd | reviews.csv | Sterk, maar 26 procent 1 ster | Geen gemiddelde score noemen. Wel "Verified buyer" + naam + product. |
| 7 | Comments en feedback | Indirect: replies op Benjamin-mails (geen archief gevonden) | Gorgias | Onbekend | Reply-vraag per mail laten verschillen en antwoorden (met toestemming) hergebruiken |
| 8 | Aantal klanten | Ja: 100,000+ happy customers | DECISIONS 7 okt | Sterk | Specifiek houden ("100,000+"), niet afronden naar "thousands". Ook "in a little over a year" mag (Brand Guidelines). |
| 9 | Awards en media | Niet aantoonbaar. Er staat een `Forbes-Emblem.png` in Shopify Files (geüpload 30 sep 2024), maar geen artikel, datum of citaat in content/facts. | content/assets/index.csv | Onbekend | Niet gebruiken tot Floris een link naar de vermelding geeft [VRAAG FLORIS]. |

Wat ontbreekt en hoe we het verzamelen:
1. Foto-reviews: reviewflow XzHrez vraagt bij 5 sterren om een foto van het gerecht in de pan (aanpassing reviewmail, na akkoord).
2. "First egg"-UGC: P2 heeft al "Reply with a photo or a short video". Maak het concreet: "Send us your first egg. We pick one a week to show other first-timers (with your name, only if you say yes)." Toestemming per foto vastleggen.
3. Herhaalkopers-citaten: Tammy (4e pan) is ons enige herhaalverhaal. In R1 en R2 een reply-vraag "Which pan do you reach for most?" en de antwoorden met toestemming verzamelen.
4. Chef met naam: naam, jaren ervaring, keuken. Dan kan het chef-citaat als expert-proof.
5. Media: alleen met bron.

Regel uit Doan die we overnemen: match de proof aan de claim. Een checkoutmail over garantie krijgt de reviewer van wie de pan is vervangen (R240 Brandon W.), niet "cooks good and cleans good".

---

## 4. Eigen onderzoek: wat werkt in DTC-mailcopy

### 4.1 Onderwerpregels (cijfers uit zoekresultaten; bronpagina's niet volledig geverifieerd)
- Onderwerpen onder 21 tekens: 31 procent hogere open rate en dubbele unieke clickrate (2,4 procent) in Yes Lifecycle Marketing-analyse van 7 miljard mails ([Data Axle](https://www.data-axle.com/about-us/news-media-coverage/data-email-subject-lines-under-21-characters-generate-the-highest-open-rates/)). Maar kort is niet heilig: GetResponse: "specific is the new short" ([GetResponse](https://blog.getresponse.com/email-subject-lines-specific-short)).
- Cijfers en vraagtekens in onderwerpen: 20 procent open tegen 12 procent zonder in een sales-mailstudie (zoekresultaatsamenvatting, [Prospeo](https://prospeo.io/s/what-is-a-subject-line)).
- Vertaling voor ons: twee lengtes testen. Kort en specifiek ("Report no. 25895", "Tammy's fourth pan") tegen langer met voordeel. Opens zijn vervuild door Apple MPP (PLAYBOOK 6): winnaar op unieke kliks en omzet per ontvanger.

### 4.2 Awareness toegepast op flows
Schwartz-samenvatting en toepassing op e-commerce ([Selzee](https://selzee.com/eugene-schwartz-5-levels-of-awareness)): "writing the wrong message for the wrong awareness level is the single biggest reason ads fail". Voor flows is de trigger het bewijs van bewustzijn: Viewed Product = product aware, Added to Cart / Checkout Started = most aware, Card Game-inschrijving = problem aware of zelfs unaware (kwam voor een prijs). Onze eigen data bevestigt het: de eerste checkoutmail zonder code doet $4,28 tot $7,86 per ontvanger (04-offer-strategy §1). Most aware wil zijn cart terug, geen essay.

### 4.3 Waarom mensen afhaken (Baymard, via zoekresultaten)
Extra kosten 39 procent, levering te traag 21 procent, geen vertrouwen 19 procent, retourbeleid 15 procent. Onze friction-regel moet dus "Free shipping" en "30-day returns" noemen; levertijden noemen we bewust niet (PLAYBOOK 11). Vertrouwen: rapportnummer en klantenaantal.

### 4.4 Reason-why voor kookgerei
De sterkste cookware-mails die we zagen geven het mechanisme met bron. Made In ("Sold Out 3x. Now Back for a Limited Time.", 4 okt 2026) over de papieren snijplank: "Wood looks good and treats your knife well, but it needs oiling and can't go in the dishwasher. Plastic is easy but sheds microplastics into your food. Our boards are neither: paper fibers fused with resin under heat and pressure, the same material professional kitchens have relied on since the 1960s." Met voetnoot: "Source: FILAB S.A.S., an independent materials and chemical analysis lab in Dijon, France. Report dated September 2025." Dat is precies Hopkins (reden) plus Ogilvy (specifiek) plus authority (lab met plaats en datum). Wij kunnen dat één op één: "Source: Light Labs, an ISO/IEC 17025-accredited lab in Ann Arbor, Michigan. Report no. 25895, released October 30, 2025."

---

## 5. Testimonials: shortlist van 15 mini case studies

Selectie op het verhaalpatroon (probleem, oplossing, waarom deze pan, emotie). Alle 15 zijn geverifieerd (Trustpilot via Gorgias, naam en datum). Citaten zijn letterlijk; ingekorte versies gebruiken alleen "..." en bestaande woorden in volgorde (gecontroleerd met een script, zie §5.2). Typfouten van de klant blijven staan. Reviews die de oude 100-dagenregel of "lifetime" noemen, kort ik in zonder dat deel.

| # | ID | Naam, datum, product | Verhaal (voor > actie > uitkomst > emotie) | Ondersteunt claim | Beste mail |
| --- | --- | --- | --- | --- | --- |
| 1 | R583 | Scott Y., 10 apr 2026, Crepe Pan Pro | Teflon en keramiek faalden, coatings lieten los > Siraat > "the best we have owned yet" > "the last pans we ever have to purchase" | Geen coating, laatste pan, pijnsom | K2-new, C4, W1 |
| 2 | R169 | Michael G., 27 jul 2026, Pan Pro | Green pans, vrouw wilde gewone nonstick, hij niet ("forever chemicals"), kocht "out of desperation" > volgde instructies > ei gleed > "super skeptical", nu favoriet | Techniek werkt, skepticus overtuigd | W5, B2, C1 |
| 3 | R563 | Louise T., 14 apr 2026, Pan Pro | Dochter klaagde over plakken en loslatende coatings > cadeau > "a past grumble" > "I can't wait to finish work, and go home to cook." | Cadeau, emotie, coating | P3, campagnes Q4, W4 |
| 4 | R025 | Sunny C., 25 sep 2026, set | Ging steeds terug naar nonstick > "ordered one pan to try it out" > "ordering the set" > "Getting rid of teflon for good." | Eén pan, dan de set | C3-P, P3-accessory, B2-clicked |
| 5 | R017 | Marilyn B., 30 sep 2026, Pan Pro | Volgde de instructies > roerei perfect > geeft nonstickpannen weg > "I only need the new one." | Instructies werken, vervangt alles | C1, P1, W5 |
| 6 | R069 | Aggie M., 6 sep 2026, Pan Pro | Voorverwarmen, waterdruppeltest > ei plakte niet > "So happy" | Het ritueel | W0, P2, K1 |
| 7 | R138 | Tammy, 4 aug 2026, Pan Pro | Vierde pan, lichter dan gietijzer, één aan haar zoon gegeven | Herhaalkoop, cadeau | W5 (uitgelicht), R1, R2-VIP, K2-returning |
| 8 | R220 | Carole, 12 jul 2026 | 60 jaar koken, "a ton of pans" > deed onderzoek > beste ooit; moeders metalen spatel werkt weer | Metal utensil safe, ervaring | B1, R1-pan |
| 9 | R466 | James, 9 mei 2026, Wok | Chef-vriend gebruikt hem > had eerder een no-brand titanium pan > dacht "another scam" > "it's real titanium" > kocht ook deep pan en wok | Echtheid, origineel vs look-alikes | C2, W3, R1, R2 |
| 10 | R407 | Emma, 21 mei 2026, Mini | Sceptisch > "wow it definitely is non stick" > klantenservice hielp met maat > wil hem doorgeven aan haar zoon | Maatadvies, erfstuk, garantie-gevoel | W4, K3 |
| 11 | R438 | David H., 14 mei 2026, Pan Pro (4 sterren) | Zocht "specifically for PFAS free cookware" > website overtuigde > "better than my current non-stick" | PFAS, bewijs | W3, C2 |
| 12 | R577 | Thomas D., 11 apr 2026 | "Makes all of our others "non stick" seem really sticky." | Release vergeleken | W1, C1 |
| 13 | R240 | Brandon W., 6 jul 2026 | Handvat werd los > stuurde een foto > "they honored the warranty" | 75-year warranty is echt | K3, C4, R2 |
| 14 | R143 | Sandi R., 4 aug 2026 | Eerste keer, "needed just a thin covering of oil" > "cleaned up beautifully" | Eerlijke verwachting (olie) | P2, W0 |
| 15 | R088 | Chetan G., 27 aug 2026, Crepe Pan | "works like a non-stick but gives crispy output like a cast iron pan" | Crepe pan, prestaties | P3-set, R1-set, R1-pan |

Reserve: R553 Fran G. (gooit Teflon weg), R518 Graham C. (beste omelet, eerste keer), R273 Steven T. (ongebruikt geretourneerd, refund "no questions asked"), R060 S. S. (lange case: keramische skillets, tortilla's), R542 Jibz C. (hele keuken vervangen), R547 Don J. (tweede aankoop in twee weken).

Niet gebruiken: R123 Clara C. (noemt HexClad, en "i hope it keeps" is geen bewijs), R156 San L. (noemt concurrent), R153 Wendy S. en R220 deel "100 day guarantee" (oud beleid), R364 Stephen B. (noemt "100 day warranty"), Nina G. "handle stays cool" (objections.csv: geen cool-handle-claim; staat nu in B2-clicked en P3-pan).

### 5.2 Ingekorte versies voor het reviewblok (max 120 tekens, paren binnen 30 tekens lengteverschil)
Zie `04-rewrites.md` per mail. Elke ingekorte versie is gecontroleerd: alle stukken tussen "..." komen letterlijk en in volgorde uit de originele review.

### 5.3 Eén echte klant-case per flow
Een case is een langere review, ingekort, als eigen blok ("ONE CUSTOMER, START TO FINISH") met naam, product en datum. Waar het het meeste effect heeft:
- Cart K2-new: R583 Scott Y. (coatings faalden, laatste pannen). Past op de pijnsom. Hoogste effect: K2 is de mail met de meeste twijfel over prijs.
- Checkout C2: R169 Michael G. (skepticus, green pans, ei de volgende ochtend). Past op de bewijsmail.
- Welcome W5: R169 of R563 Louise T. (dochter). W5 is de reviewmail; nu een losse quote van Tammy.
- Browse B2-notclicked: R466 James (dacht dat het weer een scam was). Vervangt de vier korte kaarten niet maar de "THE DOUBTER"-kaart (Avril, weinig inhoud).
- Post-purchase P2: R069 Aggie M. als "what the first egg should look like" (kort genoeg).
- Winback R1: R220 Carole (60 jaar, moeders spatel).

---

## 6. Email Love: 10 mails bekeken, wat we overnemen

| Merk, onderwerp, datum | Wat werkt (citaat) | Overnemen |
| --- | --- | --- |
| Our Place, "Safety Check", 25 sep 2026 | Hero "Third-Party Tested, for All Your Dinner Parties". Body: "We test our products obsessively. But we take non-toxic materials so seriously, it's nice to have a second opinion. That's why we work with Light Labs, an independent, accredited laboratory, to verify the safety and integrity of our cookware." | Belangrijk inzicht: Our Place gebruikt hetzelfde lab. "Light Labs tested" is dus geen onderscheid meer. Ons onderscheid: het rapportnummer, de 31 stoffen, het certificaat dat je kunt lezen. Hun "second opinion"-zin is goed: authority zonder arrogantie. |
| Our Place, "Which One Are You?", 26 sep 2026 | "Cook Like You Cook. Some nights are a stovetop grilled cheese, others are a full family-style table." Groepen "Weekday Regular", "Weekend Projects", "Host Who Needs the Most". | Commitment via zelfidentificatie. Voor W4: "Who are you cooking for?" in plaats van "Five reasons it's the one". |
| Made In, "Sold Out 3x. Now Back for a Limited Time.", 4 okt 2026 | Onderwerp met getal en echte schaarste. Body met reden-waarom en voetnoot "Source: FILAB S.A.S. ... Report dated September 2025." | Voetnoot-stijl voor Light Labs. Getal in onderwerp alleen als het waar is. |
| Made In (Chip), "They Trained Dogs to Keep the Knife Makers Warm", 1 sep 2026 | Platte tekst, foto van de vier oprichters bij de Eiffeltoren, open loop: "It all started in France, when we were just a company of 4 people..." | Model voor W2 Benjamin: echt moment, echte foto, open loop. Vraagt input van Floris. |
| HexClad, "A letter from HexClad's founder", 11 apr 2026 | "At HexClad, we're all about innovation and bringing new ideas to your kitchen." "One of the fastest-growing cookware companies in America." | Tegenvoorbeeld: geen enkel detail, kan van elk merk zijn (PLAYBOOK-vuistregel). Wel goed: "simply reply to this email". |
| HexClad, "Why folks love us", 3 apr 2026 | "Sure, it looks great, but why would you kick your cookware to the curb in favor of ours?" | Enter the conversation in their mind (Collier): stel de vraag die de lezer heeft. Hun antwoord ("the best, most high-tech") is weer vaag; het onze is 25895. |
| Huel, "Your 15% intro offer is waiting", 15 mrt 2026 | "You've just taken the first step toward better nutrition, and here's 15% off your first order to get you started." Unieke code (USSB15-...), voorwaarden in één regel: "cannot be applied alongside other discount codes. New customers only." | Commitment ("first step") + eerlijke voorwaarden. Onze "One code per order" netjes onder elke code. |
| Bonobos, "Your cart is waiting for you!", 23 nov 2025 | "We can't promise your picks will stick around." (Email Love-annotatie) | Eerlijke onzekerheid in plaats van nep-schaarste. Voor ons: niet nodig over voorraad, wel als toon. |
| PrettyLitter, "Last chance on your favorite items", 19 okt 2025 | Social proof direct na de cart ("25,000+ reviews") | Proof direct onder het cartblok, niet onderaan: één regel review onder de cart in C1. |
| Caraway, "The Reviews Are In", dec 2023 | Hero "Holiday Hosting Game Changers", quote "Love this! Was a huge hit as we prepared and served holiday meals!" naast het product | Quote naast het product dat het bewijst (match proof aan claim). "Game changers" is een AI-tell; niet overnemen. |

Eerdere benchmarks in `research/ux-2026-10-07/02-emaillove-benchmarks.md` (Our Place, HexClad, Huel, Solo Stove, Quince) blijven gelden voor layout.

---

## 7. Claims-risico's gevonden tijdens de copy-check (voor de bouw)

1. C2 alt-tekst cutaway: "0.5 mm pure titanium cooking surface, 1 mm aluminium core, 0.6 mm stainless steel base". Laagdiktes zijn needs-proof (claims.csv). Weghalen tot Floris bevestigt.
2. C1 features: "Metal utensils, high heat, dishwasher". Facts: nooit op hoog vuur, hoog vuur is de nummer 1 oorzaak van plakken. Vervangen.
3. B2-clicked en P3-pan review Nina G.: "the handle stays cool". Objections.csv: geen cool-handle-claim. Vervangen.
4. W1 en W4: "Pure titanium surface" zonder "cooking". Goedgekeurd is "with a pure titanium cooking surface" + "no coatings". Notion-brief W40/W41 zegt juist geen "pure" in nieuwe copy. Conflict: [VRAAG FLORIS]. Tot dan de PLAYBOOK-versie (besluit Siraat 6 okt) volgen.
5. Light Labs-claim op andere producten dan de geteste Pan Pro: DECISIONS 7 okt zegt het geldt voor alle pannen (zelfde titaniumlaag). Mag, maar formuleer zo dat het klopt: "Every pan has the same titanium cooking surface as the one Light Labs tested."
6. "PFAS water filter $450 value" in het gifts-blok: het is een kans. Het blok zegt "Win a PFAS water filter", goed. In copy nooit "$70 + $450 in gifts" optellen.
7. Weekelijkse trekking als deadline ("draw closes Sunday"): niet gebruiken tot de actievoorwaarden bestaan.
8. C3-P "$349" voor de 6-delige set: Shopify toont $399 zichtbaar, $349 is UNLISTED. Open bij Floris (00-samenvatting punt 1).

---

## 8. Wat Floris moet aanleveren [VRAAG FLORIS]

1. Benjamins echte verhaal: waarom hij begon, welke pan hij weggooide, het moment met de snijplank naar de pan, hoeveel prototypes, waarom gehamerd, wat er misging met de eerste batch, één foto van toen. Zonder dat blijft W2 generiek.
2. De chef uit de care-video: naam, functie, jaren ervaring, toestemming om hem bij naam te citeren.
3. Herkomst van de "41% coating wear"-survey (Notion W41).
4. Media of awards: is er een echte Forbes-vermelding (er staat een Forbes-logo in Shopify Files)? Link en datum.
5. Toestemming en format voor UGC-oproep in P2 en foto-vraag in de reviewflow.
6. Laagdiktes en oventemperatuur (voor Rolls-Royce-specificiteit in de toekomst).
7. Actievoorwaarden van de wekelijkse PFAS-filtertrekking (dan pas als deadline).
8. "Pure" in nieuwe copy: PLAYBOOK zegt "with a pure titanium cooking surface", de ads-brief zegt "titanium cooking surface" zonder "pure". Welke wint?
