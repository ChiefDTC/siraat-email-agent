# Concurrentie- en inspiratie-onderzoek · e-mailflows

Datum: 7 oktober 2026. Opdracht: de sterkste flowmails in premium DTC-kookgerei en verwante merken vinden, vergelijken met onze v4-mails en 15 eerlijke ideeën opleveren.

## Bron en methode

- **Email Love MCP was bereikbaar.** Gebruikt: `list_journeys`, `get_journey` (Graza, Crate & Barrel, TUSHY, Huel), `search_brands`, `search_emails` (op merk en op categorie: cart-abandonment, browse-abandonment, post-purchase, re-engagement), `fetch_email` (11 keer) en de volledige screenshots van 34 mails, die ik zelf heb bekeken. Eén keer gaf de server een 429 (rate limit), daarna werkte alles weer. `get_email_html` niet nodig gehad: de screenshots waren genoeg voor structuur en copy.
- **Beperking 1:** van de genoemde kookgereimerken staan op Email Love bijna alleen campagnes. Caraway (8 mails), HexClad (4), Misen (1), Owala (2) hebben geen flowmails behalve de HexClad-welcome; GreenPan, Le Creuset en Made In zijn vrijwel alleen sale-campagnes. Daarom per flowtype aangevuld met de beste DTC-voorbeelden uit andere categorieën (Graza als het meest verwante food/kitchen-merk met een volledige journey).
- **Beperking 2:** Email Love toont geen wachttijden of triggers. Timing noem ik alleen waar de mail het zelf zegt.
- **Eerder onderzoek** (niet herhaald, wel gebruikt): `research/2026-10-06-competitor-welcome-flows.md`, `research/ux-2026-10-07/02-emaillove-benchmarks.md`, `research/copy/01-dr-research.md` sectie 6 (Our Place "Safety Check" gebruikt hetzelfde lab, Made In-foundermail, Bonobos, PrettyLitter, Caraway).
- **Onze kant:** de v4-templates in `klaviyo/templates/v3/<flow>/` (onderwerpregels uit de topcomments) en de mobiele en desktop-previews van C1, C2, C4-US, K1, K3, B1, B2-notclicked, W1-A, W3, W5, P1-first-pan, P2, R1-pan, R2.

## Vijf kernbevindingen

1. **Wij winnen op bewijs, zij op beleving.** Geen enkele concurrentmail die ik zag heeft zo'n specifiek bewijs (rapportnummer, 31 stoffen, eerlijke beperking, friction reducer onder elke knop). Maar de beste mails (Graza, Material, Made In) verkopen met sfeer, mensen en eten; wij met productfoto's en blokken.
2. **Onze mails lijken te veel op elkaar.** C1, C2, C4, K1, B1, W1 en R1 hebben bijna dezelfde stapel: codebalk, hero, cartblok, knop, tekst, vergelijkingstabel of drie vragen, gifts-grid van vier, drie reviewkaarten met dezelfde packshot, Benjamin, footer. Wie vier mails in een week krijgt, ziet vier keer hetzelfde. Lengte is niet het probleem: desktop zijn onze mails 4,6 tot 5,0 keer zo hoog als breed, de concurrenten in abandonment 2,5 (Harry's) tot 5,4 (Ninja), mediaan rond 4.
3. **Niemand toont bij pannen echte klantfoto's, ook wij niet.** Okendo heeft 0 foto's op 2.226 pannenreviews (`research/reviews-okendo/01-analyse.md`). Al onze reviewkaarten tonen dezelfde packshot. Hier valt het meest te winnen, maar het vraagt eerst een verzamelproces.
4. **Interactie in de mail ontbreekt bij ons.** TUSHY (via Okendo) laat je in de mail een ster aanklikken, eBay vraagt met één klik waarom je wegbleef, Graza maakt van een herhaalmail een beslisboom. Wij vragen overal "reply", wat meer moeite kost dan klikken.
5. **Echte urgentie is zeldzaam; nep-urgentie is overal.** "Your cart is about to expire" (PrettyLitter), "popular items tend to go fast" (Stanley), "SELLING FAST" en countdown-GIF's (Our Place), "Don't let it slip away" plus timer (Landish). Onze 48-uurscode met reden en wat-daarna is eerlijker en specifieker dan alles wat ik zag. Dat houden.

---

## 1. Sterkste voorbeelden per flowtype

### 1.1 Abandoned checkout en cart

| Merk · onderwerp | Link | Wat ze doen |
| --- | --- | --- |
| **Graza** · "Your kitchen deserves MICHELIN STAR EVOO" (cart, jan 2024) | [emaillove.com/graza-email-design-9](https://emaillove.com/graza-email-design-9) | Hero "Checking Us Out?" met een knipoog, dan "I know you can't help it, we look pretty dang good". Daarna één grote review in typemachinefont: "I was super skeptical and just thought it was millennial marketing... I bought all of my children a set and then got a subscription for myself", ondertekend "A Real Person Named Megan". Lifestylefoto (kind en moeder koken). Geen korting, geen cartblok. Sociale bewijskracht via **de bekeerde scepticus**. |
| **Graza** · "WHY IS IT SO GOOD?!?" en "Let's pick up where we left off" (cart, nov 2024) | [graza-email-design-22](https://emaillove.com/graza-email-design-22) · [-23](https://emaillove.com/graza-email-design-23) | Sfeerfoto met eten als hero ("Everything tastes better with olive oil"), cartregel met totaal, één knop "Order More EVOO", daarna subscribe-aanbod. Kort: één scroll. |
| **Our Place** · "You left your cart behind." (cart, dec 2023) | [our-place-email-design-4](https://emaillove.com/our-place-email-design-4) | Cart, knop, dan een "Reasons to Love Our Place"-grid met acht iconen: free shipping, **Klarna "Buy Now Pay Later"**, returns, "Here to help! Reach out to CX", refer a friend. Sluit met "You're Always Welcome. Questions? We're here for you" plus het e-mailadres. Wel nep-urgentie in de kop ("Don't miss out"). |
| **Harry's** · "Last call ⏰" (checkout, nov 2025) | [email-inspiration-from-harrys-23](https://emaillove.com/email-inspiration-from-harrys-23) | Kop "So Close to the Finish Line" met geanimeerde mammoet: **goal-gradient** zonder te liegen. Eén alinea ("you've done most of the work, but stopped short at checkout"), unieke code in de tekst, knop, cartregels. Heel kort. |
| **Bonobos** · "Your cart is waiting for you!" (nov 2025) | [email-inspiration-from-bonobos-176](https://emaillove.com/email-inspiration-from-bonobos-176) | "Still thinking it over? Your cart is right where you left it." Eén lifestylefoto, één knop, "free shipping & returns" in de topbalk. Rust en zelfvertrouwen, geen korting. |
| Ter vergelijking: **PrettyLitter** · "Last chance on your favorite items" | [email-inspiration-from-prettylitter-107](https://emaillove.com/email-inspiration-from-prettylitter-107) | Cart, dan een reviewkaart met **"Rated 4.7/5 · 1,224 reviews · Trustpilot"**. Specifiek getal met bron. Maar ook "Last Chance" als nep-urgentie. |

Patroon: korte mails, één idee, een sfeerfoto of één sterke review. Korting alleen bij Harry's, PrettyLitter en Ninja, steeds als unieke code. Productrecommendations ("You might also like") bij Stanley, La Colombe, Ninja; in checkout leidt dat af.

### 1.2 Browse abandonment

| Merk · onderwerp | Link | Wat ze doen |
| --- | --- | --- |
| **Material** (kitchenware) · "We noticed you noticing us..." | [material-email-design-8](https://emaillove.com/material-email-design-8) | Kop "Thanks for stopping by", één product, daarna vier reviews die **elk bij een ander product horen** ("on The Coated Pan", "on The reBoard"), elk naast een **lifestylefoto** van dat product in gebruik. Slotblok "Put us to the test" met shipping, trial en guarantee. |
| **mindbodygreen** · "Still deciding? Read this first" (jul 2026) | [email-inspiration-from-mbg-health-coaching-166](https://emaillove.com/email-inspiration-from-mbg-health-coaching-166) | Platte tekst, opent met wat klanten zeggen ("I wish I had done this sooner"), twee lange verhaalreviews, **foto's en namen van de twee adviseurs** die je kunt spreken, en een **financieringsblok** (Affirm, rekenvoorbeeld per maand). Mooie mix van liking en prijsbezwaar. |
| **On** · "☁️ Still deciding on your order?" | [email-inspiration-from-on-7](https://emaillove.com/email-inspiration-from-on-7) | "Can't decide?" spreekt de keuzestress direct aan en zet het retourbeleid in als geruststelling. Wij kunnen "try it" niet zeggen (retour alleen ongebruikt), wel de vorm. |
| **Stanley 1913** · "The Perfect Stanley" | [email-inspiration-from-stanley-1913-2](https://emaillove.com/email-inspiration-from-stanley-1913-2) | "You've got great taste": validatie van de keuze (commitment). Drie aanbevolen alternatieven. Footer met "Stainless-steel warranty policy" en "Refer a friend". Minpunt: "popular items like these tend to go fast". |
| **Paula's Choice** · "Still Thinking It Over Friend?" (jul 2026) | [email-inspiration-from-paulas-choice-46](https://emaillove.com/email-inspiration-from-paulas-choice-46) | "Skincare without the guesswork": drie starter-kits als **begeleide keuze**. 20% korting in de hero, "money back guarantee" in de footer. |

Patroon: browse gaat over twijfel, niet over de cart. De beste mails helpen kiezen (Material, Paula's Choice) of nemen een persoon mee (mbg).

### 1.3 Welcome

| Merk · onderwerp | Link | Wat ze doen |
| --- | --- | --- |
| **HexClad** · "Welcome to the HexClad family." (mrt 2025) | [email-inspiration-from-hexclad-cookware](https://emaillove.com/email-inspiration-from-hexclad-cookware) | Geen code, maar **tegoed op de tweede aankoop, getrapt**: $250 eerste aankoop geeft $25, $450 geeft $50, $750 geeft $75. "What sets HexClad apart" plus een **geannoteerde pan** met acht callouts. Daarna een lange grid "Most popular". Lang (13,6 keer zo hoog als breed) en claims die wij niet mogen ("Lifetime Warranty", "Stay-cool handles"). |
| **Great Jones** · "Welcome! A housewarming gift of 10% off" (mrt 2025) | [email-inspiration-from-great-jones](https://emaillove.com/email-inspiration-from-great-jones) | Korting als "housewarming gift" (framing), een korte brief van de oprichter met handtekening, drie producten met één zin elk ("A good Dutch oven lasts forever; a Great Jones Dutch oven is your best friend forever"). Code vervalt 12 dagen na inschrijving (in de kleine lettertjes). |
| **Huel** · "Welcome to the Huel family" (mrt 2024) | [huel-email-design](https://emaillove.com/huel-email-design) | "Hi, I'm Julian, founder of Huel" met hoe hij het zelf gebruikt, dan "Huel & your day" (wanneer je wat neemt) en een **mythebuster-video** van de medeoprichter ("Nutrition Myths with James Collier"). Leert en verkoopt tegelijk. |
| **Huel** · "Your bag of Strawberry Shortcake Black Edition inside" (jan 2025) | [huel-email-design-21](https://emaillove.com/huel-email-design-21) | Gratis product in plaats van procenten, met "usually worth $42.50" (anchoring) en een unieke code. Nadeel: drie stappen om te claimen. |
| **Our Place** · "Welcome! You've made the Guest list." (zie eerdere research) | `research/2026-10-06-competitor-welcome-flows.md` | Lidmaatschap in plaats van code; "The Always Pan 101" met geannoteerde hero. |

Patroon: oprichter vroeg en kort, uitleg van het mechanisme met een beeld, product in gebruik. Alleen HexClad stuurt in elke mail een aanbod.

### 1.4 Post-purchase (inclusief review en UGC)

| Merk · onderwerp | Link | Wat ze doen |
| --- | --- | --- |
| **Graza** · "How's that EVOO tasting??" (review) | [graza-email-design-20](https://emaillove.com/graza-email-design-20) | "We Think We're 5 Olives. But what do you think??" met vijf olijven als sterren, één knop. Daaronder **iets geven**: "And just for you, a little inspo for dinner tonight" met drie receptfoto's. Vraag en cadeau in één mail (reciprociteit). |
| **TUSHY** · "Still holding it in? 👀" en "This is our final plea 💔" (review, via Okendo, jan 2026) | [email-inspiration-from-tushy-6](https://emaillove.com/email-inspiration-from-tushy-6) · [-7](https://emaillove.com/email-inspiration-from-tushy-7) | Korte platte tekst met humor, en **vijf klikbare sterren in de mail** ("How many stars?"). Eén klik is de eerste stap van de review. De derde mail zegt eerlijk "We promise this is the last email" en vraagt ook om kritiek ("Or tell us where we missed the mark"). |
| **Graza** · "SQUEEZE, REFILL, REPEAT" (herhaalaankoop) | [graza-email-design-19](https://emaillove.com/graza-email-design-19) | Gebruik in vier genummerde stappen met foto, dan "Cooking inspo just for you" met drie recepten. Het product wordt een gewoonte. |
| **Graza** · "Hello again to our fave customer!!" | [graza-email-design-21](https://emaillove.com/graza-email-design-21) | Na aankoop: abonnement, "Mo EVOO. Mo money (in your pocket)" en **"You can GIFT Graza!!!"** met unboxingfoto. Cadeau als tweede aankoop. |
| **Made In** · "The Cookware Mistake Almost Everyone Makes" (campagne, feb 2026) | [email-inspiration-from-made-in-170](https://emaillove.com/email-inspiration-from-made-in-170) | Educatie die verkoopt: "Stop using one pan for everything", per materiaal welke klus (stainless = deglaze, carbon = sear, ceramic = delicate), en onderaan een **videothumbnail met play-knop**: "How to make any pan non stick. There are 3 things you need to know." Precies ons P2-verhaal, maar als video. |
| **Italic** · "The Ultimate Linen Care Guide" (jun 2026) | [email-inspiration-from-italic-227](https://emaillove.com/email-inspiration-from-italic-227) | Verzorging als belofte ("How To Make Your Linens Last"), korte regels per product, "A few habits we swear by", dan pas "Complete your Home". |
| Ook gezien: **Rally** · "A quick favor from Rally's co-founder" | [email-inspiration-from-john-from-rally](https://emaillove.com/email-inspiration-from-john-from-rally) | Platte tekst van de oprichter met een enquêteverzoek en een loting (3 x $100). Eerlijk en kort. |

### 1.5 Winback en re-engagement

| Merk · onderwerp | Link | Wat ze doen |
| --- | --- | --- |
| **Graza** · "We miss you!" (re-engagement) | [graza-re-engagement-email](https://emaillove.com/graza-re-engagement-email) | "Ready for more Graza?" als **beslisboom** ("Do you have a mouth?", "Need a great gift idea?", "Has it been graced with the taste... recently?") die eindigt bij kopen of abonneren. Zelfselectie met humor. |
| **eBay** · "If the 90s can make a come back, so can you 🔙" (jun 2025) | [email-inspiration-from-ebay-19](https://emaillove.com/email-inspiration-from-ebay-19) | Gewone toon ("life gets busy"), vier categorieën, en een blok **"We want you back. Give us another chance. Tell us how we can make your experience better"** met één knop. |
| **Snake River Farms** · "It's Been A While!" | [snake-river-farms-re-engagement-email-design](https://emaillove.com/snake-river-farms-re-engagement-email-design) | Bestsellers als eten op het bord, dan **"You have 309 points to redeem"** (endowment) en "We've been busy testing and perfecting new recipes". |
| **Athletic Brewing** · "All out of brews?! Get 15% off your next order" | [athletic-brewing-company-email-design-19](https://emaillove.com/athletic-brewing-company-email-design-19) | Eén reden ("Do you miss the sight of Athletic brews in your fridge?"), unieke code met looptijd van een maand in de voorwaarden. |
| **Levi's** · "Don't let this be goodbye" (sunset) | [levis-email-design](https://emaillove.com/levis-email-design) | Sms-bubbels als hero, twee knoppen: "Keep me subscribed" en "Unsubscribe". Eerlijk en klein. Onze S1 doet hetzelfde ("Yes, keep me on the list"). |

---

## 2. Vergelijking met onze v4-mails

### 2.1 Checkout (C1 t/m C4) en cart (K1 t/m K3)

**Zij doen het beter**
- **Variatie.** Graza en Bonobos maken elke mail anders. Onze C1, C2 en C4 openen met hetzelfde cartblok, dezelfde gifts-grid en dezelfde reviewkaarten. Alleen het middenstuk (tabel, drie vragen, twee beloftes) wisselt.
- **Mensen en eten.** Onze review-thumbnails zijn allemaal dezelfde Pan Pro-packshot. Graza en Material zetten een foto naast de review waarop iemand kookt.
- **Betalen in termijnen zichtbaar maken.** Our Place zet Klarna als icoon in de cart, mbg rekent het per maand voor. Onze C1 noemt Shop Pay Installments en Affirm in één zin in de lopende tekst; C3-p (de prijsmail) toont alleen de prijs per pan.
- **Eén sterke verhaalreview.** Graza's "super skeptical... millennial marketing" is één groot blok. Wij hebben de equivalent (James, R466: "I honestly thought this might be another scam") alleen als B-onderwerp van C2 en als klein kaartje.

**Wij doen het beter**
- Friction reducer onder elke knop, unieke code al toegepast via de knop (Huel laat je drie stappen doen), prijs na code in dollars ($120.60), en de deadline met reden en wat-daarna ("Made for you, so it has an end date. After 48 hours the regular sale price applies"). Niemand anders legt de deadline uit.
- Bewijs in plaats van bijvoeglijke naamwoorden: rapport 25895 met afbeelding van het certificaat, "Read it yourself". Vergelijk HexClad "Why folks love us" (vaag) en Our Place die hetzelfde lab gebruikt zonder nummer.
- C4 "Two promises" met een retourreview en een garantiereview: sterker risk reversal dan "free returns" van Bonobos of On.
- Routering per cartinhoud (set, Pan Pro, accessoire) en per land. Geen enkele concurrent toont zichtbaar maatwerk.

### 2.2 Browse (B1, B2)

**Zij beter:** Material koppelt elke review aan een eigen product en eigen foto; Paula's Choice en Stanley helpen kiezen tussen drie opties. Onze B2-notclicked (de lezer klikte niet op B1) toont opnieuw dezelfde pan: wie niet klikte, twijfelt misschien aan het product of de maat, niet aan de prijs.
**Wij beter:** B1 heeft een eerlijke vergelijking met stainless steel inclusief wat stainless ook goed doet ("PFAS-free too", "Induction ready too"). Dat is geloofwaardiger dan de één-kant-wint-alles-tabellen elders.

### 2.3 Welcome (W1 t/m W5)

**Zij beter:** Huel en HexClad leggen het mechanisme uit met een beeld (geannoteerde pan, mythebuster-video). Onze W3 doet het met tekst en drie vragen. Great Jones en Huel laten de oprichter in de eerste mail zien met handtekening of gezicht; onze W2 van Benjamin is nog niet live (wacht op zijn echte verhaal, [VRAAG FLORIS]).
**Wij beter:** W1 bevestigt de Card Game-deelname in één regel en verkoopt dan met bewijs; HI10 is al toegepast; W4 "Who are you cooking for?" (commitment) en W5 als echt laatste mail met een verhaal (Tammy). HexClad stuurt in elke mail een aanbod; wij niet.

### 2.4 Post-purchase (P1, P2, P3, U1, review XzHrez)

**Zij beter:** TUSHY maakt de reviewstap één klik in de mail. Graza geeft iets terug in dezelfde mail als de vraag (recepten). Made In verkoopt dezelfde boodschap als onze P2 met een videothumbnail. Graza gebruikt de cadeau-hoek na aankoop; wij doen dat alleen in P3-apron.
**Wij beter:** P2 is de beste first-use-mail die ik zag: vijf stappen met foto, "If something sticks: a sticky pan is not a ruined pan", baking-soda-oplossing, en de eerlijke beperking. Geen concurrent pakt het grootste retourrisico (plakken, 28% van retourverzoeken) zo direct aan. P1 met tijdlijn en P2 op levering (via Delivered Shipment) is ook slimmer getimed dan wat Email Love toont.

### 2.5 Winback (R1, R2)

**Zij beter:** eBay en Graza maken het makkelijk om te antwoorden of te kiezen zonder te typen. Snake River Farms opent met eten en recepten, wij met een productlijst. Geen van onze winbackmails geeft iets dat geen korting is (een recept, een tip voor de tweede kook).
**Wij beter:** R1 kiest producten op basis van wat je al hebt ("Matched to your pan", deksel alleen als je er geen hebt) en noemt de routine die ze al kennen. R2 heeft een echte 72-uurscode met reden. Athletic Brewing en Cuisinart sturen een generieke code naar iedereen.

---

## 3. Vijftien ideeën om over te nemen

Alle ideeën binnen DECISIONS en `siraat-direct-response`: geen nep-urgentie, geen verzonnen claims, geen merknamen, reviews alleen letterlijk. Psychologie uit `research/copy/marketing-psychology.md`. Niets hiervan is gebouwd; dit zijn voorstellen.

| # | v4-mail | Wat precies | Waarom het werkt | Bron | Moeite |
| --- | --- | --- | --- | --- | --- |
| 1 | **C3-p** en **K2-new** (US) | Onder de prijs een termijnregel als zichtbaar prijsblok, niet in de lopende tekst: "$134, or 4 interest-free payments with Shop Pay" (bedrag per termijn alleen na controle van de actuele Shop Pay-voorwaarden). Alleen bij `country_code == 'US'`. | Prijs is bezwaar nummer 1 (27% bijna-stop). Framing en Mental Accounting: een kleiner bedrag per keer voelt als een andere rekening. Our Place en mbg doen het zichtbaar. | Our Place cart, mbg | Klein. [VRAAG FLORIS] akkoord op de exacte termijnclaim (DECISIONS 7 okt: "na akkoord op de claim") |
| 2 | **C2** (A-arm) | De James-review (R466) van klein kaartje naar één groot verhaalblok direct na de drie vragen, met kop "He thought so too." Volledige quote ingekort met "...", geen bewerking. | Bekeerde-scepticusbewijs werkt het best bij de vergelijker (segment C, 12% vergelijkt merken). Social Proof plus Pratfall: de lezer ziet zijn eigen twijfel terug. | Graza 9169 ("super skeptical") | Klein |
| 3 | **C1** | Kop of label vervangen door een eerlijke goal-gradient: "You got to the last step." in plaats van nog een keer "Your cart is saved". Geen voortgangsbalk die iets suggereert wat niet klopt; alleen de constatering dat ze hun e-mail al hebben ingevuld. | Goal-Gradient en Zeigarnik: een bijna-af taak trekt. Checkout Started betekent dat de lezer echt bij de laatste stap was. | Harry's "So Close to the Finish Line" | Klein |
| 4 | **B1** en **K1** | Een videothumbnail (still uit de chefvideo met ondertitels, of een frame zonder tekst, DECISIONS 7 okt) met play-icoon: "Watch: the 2-minute water test". Link naar de chefvideo. Vervangt geen bestaand blok, komt in plaats van de tweede knop. | 15% twijfelt of titanium echt werkt. Authority plus demonstratie verlagen Anxiety. Made In verkoopt precies dit ("How to make any pan non stick: 3 things you need to know"). | Made In 962677 | Klein (stills zijn er) |
| 5 | **B2-notclicked** | Wie B1 niet aanklikte krijgt nu weer dezelfde pan. Voorstel: één blok "Not the right one? Here's how people choose" met maximaal drie opties (Pan Pro Small, Standard 11", 6-delige set) en één zin per optie op basis van de maatregel. Drie, niet zes. | Paradox of Choice en Default Effect: een kleine, begeleide keuze. Maat is bezwaar nummer 2 (15%). Paula's Choice "without the guesswork", Stanley "You might also like". | Paula's Choice, Stanley | Middel (dynamische of vaste productkaarten) |
| 6 | **W4-us** en **W4-int** | De maatkeuze "Who are you cooking for?" als visuele beslisboom: "Cooking for one?" ja → Small; "Two to four?" ja → Standard 11", bestseller; "A family, or every pan at once?" → de 6-delige set. Elke uitkomst is een knop. | Commitment via zelfidentificatie en Hick's Law (één pad per lezer). Graza's beslisboom maakt van een keuze een spelletje. | Graza 4044 | Middel (beeld plus HTML-knoppen) |
| 7 | **W3** | Een geannoteerde doorsnede van de Pan Pro met drie labels: "Pure titanium cooking surface. The only part that touches food." / "Aluminum core for even heat." / "Magnetic stainless base for induction." Geen laagdiktes (claims.csv). | Reason-why en Authority: mensen geloven wat ze zien werken. Beantwoordt ook "is het echt titanium / waarom magnetisch" (160 pre-sale tickets). HexClad en Our Place gebruiken geannoteerde pannen. | HexClad welcome, Our Place 101 | Middel (beeld maken, kopie van bestaande foto) |
| 8 | **W3** (of een W3-variant) | "Three things people get wrong about titanium pans" als mythebuster, door Benjamin: (1) "It's a coating." Nee, pure titanium cooking surface, rapport 25895. (2) "It needs seasoning." Nee, no seasoning. (3) "Nothing sticks." Eerlijk: "Skip the heat, and it sticks." | Pratfall Effect: de eerlijke derde mythe maakt de eerste twee geloofwaardig, en trekt de anti-persona (de no-oil-koper) niet aan. Huel doet dit met een video van de medeoprichter. | Huel 4715 | Middel (copy, geen nieuw beeld nodig) |
| 9 | **Review-flow XzHrez** (en nieuwe reviewmails) | Okendo-sterren in de mail ("How many stars?" met vijf klikbare sterren). Eén klik opent het reviewformulier met de score al ingevuld. TUSHY verstuurt dit via Okendo, dus de techniek bestaat in ons eigen reviewplatform. | Foot-in-the-door en Activation Energy: één klik is de eerste toezegging, de rest volgt makkelijker. | TUSHY 893834 en 913374 (reviews@okendo.io) | Middel (Okendo-instelling; XzHrez is live, dus eerst Floris) |
| 10 | **U1** (first egg) | Na de fotovraag iets teruggeven in dezelfde mail: "After the egg: the steak" in drie regels (pan heet, leggen, laten liggen tot hij loslaat). Steak is de favoriete maaltijd (22%). | Reciprocity: geven voor vragen. Graza combineert de reviewvraag met "a little inspo for dinner tonight". Peak-End: de mail eindigt met een volgend succes, niet met een verzoek. | Graza 20149 | Klein |
| 11 | **U1 → C1, B2, W5** (UGC-lus) | Eerst verzamelen, dan tonen. Er zijn 0 klantfoto's bij pannenreviews (Okendo). U1 vraagt al om een foto van het eerste ei. Voorstel: die foto's (met toestemming, voornaam, DECISIONS 7 okt: klantfoto's mogen) als vaste set opslaan in `content/media/` en daarna de packshot in de reviewkaarten vervangen door de echte foto van die klant. | Social Proof is sterker met een echt gezicht of echte keuken dan met tekst alleen (Floris vroeg hier om). Material en Graza zetten de review naast een foto in gebruik. Eerlijk: alleen foto bij de review van dezelfde klant. | Material 5302, Graza 9169 | Groot (proces: verzamelen, toestemming, bijhouden) |
| 12 | **R1-pan** en **R1-set** | Een klikbare vraag in plaats van alleen "reply": "How's your pan doing?" met drie knoppen: "Love it" (→ reviewpagina), "It sticks sometimes" (→ de P2-gids plus support), "I'd like a second piece" (→ de productlijst). Elke klik zet een profieleigenschap. | Commitment en lagere drempel dan typen. Een "sticks"-klik vangt een ontevreden klant op vóór een lage review (plakken is 81 van 154 lage Trustpilot-reviews). eBay vraagt "Tell us how we can make your experience better". | eBay 284911, Graza 4044 | Middel (links met profiel-update in Klaviyo) |
| 13 | **R1-pan** | Bovenaan, vóór de productlijst, één bruikbaar blok: "Six weeks in: the steak test" of "The one thing to try next" met een receptfoto. Pas daarna "What pan owners add next". | Reciprocity en Liking: eerst waarde, dan het aanbod. Snake River Farms ("We've been busy testing and perfecting new recipes"), Graza en Made In houden zo de opens hoog. | Snake River Farms 19554, Made In 1537790 | Klein |
| 14 | **R1-pan** of **P3-pan** (Q4-variant) | Een cadeaublok voor de 19% die als cadeau koopt: "Who else should cook without coatings?" met de Pan Pro Standard en één zin over retour voor de ontvanger ("30 days to return, unused"). Geen extra korting, gewoon HI10 of de bestaande code. | Unity en Liking: de klant wordt aanbeveler. Tammy gaf er zelf een aan haar zoon (R138), dus het is echt gedrag. Graza "You can GIFT Graza!!!". | Graza 20148 | Klein |
| 15 | **C1** en **K1** (onder de reviews) | Een geaggregeerde score met bron en aantal, zoals "Rated X/5 from N reviews on Trustpilot", maar alleen met een gecontroleerd, actueel getal. Okendo 4,8 mag niet (herkomst onduidelijk). | Social Proof met specifiek getal en bron. PrettyLitter zet "4.7/5 · 1,224 reviews · Trustpilot" direct onder de quote. | PrettyLitter 619949 | Klein, maar pas na [VRAAG FLORIS] (Trustpilot-score en aantal; www.trustpilot.com moet nog in Allowed domains) |

### Bewust niet overnemen

- Countdown-GIF's, "SELLING FAST", "Your cart is about to expire", "popular items tend to go fast" (Our Place, Kiki Milk, Landish, Stanley). Geen echte reden, verboden in de skill.
- "Buy it, try it" en "100-day free returns" (On, Our Place). Ons retour is 30 dagen en alleen ongebruikt.
- Chefs of beroemdheden als endorsement (HexClad "Gordon Ramsay ❤️‍🔥 these pans", GreenPan "Bobby Flay Favorites"). Nooit chefnamen in mails.
- Een aanbod in elke welcome-mail (HexClad).
- Review-loterij van $1.000 (Crate & Kids). Bij ons al een gevoelig punt (Trustpilot-incentive) en in strijd met de regel "nooit unsolicited of independent".
- Getrapt tegoed op de tweede aankoop (HexClad: $25/$50/$75). Interessant voor AOV, maar een nieuw aanbod: alleen als Floris het wil testen tegen HI10.

---

## 4. Open vragen voor Floris

1. Termijnclaim voor US-mails (idee 1): mogen we "4 interest-free payments with Shop Pay" letterlijk zo zetten, en met bedrag per termijn?
2. Trustpilot-score en aantal reviews voor idee 15, en `www.trustpilot.com` toevoegen aan de toegestane domeinen.
3. Okendo: mag de live reviewflow XzHrez de in-mail sterren krijgen (idee 9)?
4. Is er een echte foto van Benjamin voor W2 en de afsluiting van C2 en K2 (Great Jones, Huel en mbg laten het gezicht zien)?
5. UGC-lus (idee 11): wie beheert de foto's die via U1 binnenkomen, en waar slaan we de toestemming op?
