# UX- en conversie-audit flow-systeem v3

Datum: 7 oktober 2026. Scope: 31 mails in `klaviyo/templates/v3/` (checkout 6, cart 4, browse 3, welcome 8, post-purchase 5, winback 4), alle desktop-previews volledig bekeken (in stukken van 700x1400), mobiel bekeken op de bovenste 1000 px plus totale paginalengte. Bronnen: HTML-bronnen (onderwerpregels in de topcomment), referentie `klaviyo/templates/c2-why-siraat.html` (inhoudelijk gelijk aan v3 C2), DECISIONS.md, PLAYBOOK.md hoofdstuk 1 en 10, `klaviyo/flows/v3-flow-system.md`, `baselines/README.md`, `scripts/make_hero.py`.

Taal: analyse in het Nederlands, alle mailcopy in het Engels. Copy tussen aanhalingstekens is letterlijk bedoeld voor de bouwer.

Baselines om te verslaan (90 dagen, omzet per ontvanger): checkout $2.36, cart $1.47, browse $0.97, welcome $0.70, post-purchase $0.31, winback $0.20. Checkout-herstel 0.97 procent. Dat zijn lage cijfers voor deze ordergrootte; het grootste hefboompunt is het aanbod en de knop boven de vouw.

---

## Deel A. Wat er in het hele systeem misgaat (samenvatting)

1. **Het aanbod staat nergens in de hero.** In 31 mails noemt alleen B2-clicked, W5 en R2/R2-VIP het aanbod in de hero, en dan in de subregel van 19 px (desktop) of ongeveer 12 px (mobiel). Checkout en cart (10 mails, de hoogste RPR) noemen HI10 helemaal niet. De gift-stack staat in C3-S en C4 halverwege, in K3 als één grijze zin onderaan.
2. **De winkelwagen staat onderaan.** In C1 tot C4 en K1 tot K3 komt het cart-blok pas na 1 tot 2,5 schermhoogtes. C2: cart pas op 2.800 px van 3.919 px. K3: "Finish my order" is de laatste knop vlak boven de footer (feedback 3).
3. **Feiten als platte tekst.** "It ships within 1 business day", "It arrives in 6 to 10 days", "You have 30 days to decide" (C1), "6 to 10 days" (P1-first, P1-repeat en de preview-tekst van P1-repeat), en de trust-bar "30-DAY RETURNS / 75-YEAR WARRANTY / FREE SHIPPING" zijn tekst zonder iconen. Levertijd moet eruit (feedback 1).
4. **Reviewkaarten zijn ongelijk hoog.** Oorzaak in de HTML: de witte achtergrond en rand zitten op een geneste `<table>` binnen een `<td valign="top">`, dus elke kaart is zo hoog als zijn eigen tekst. Zichtbaar in vrijwel elke mail (C1: 190 px tegen 128 px; B1: 212 tegen 128). Ook de gift-tegels in W5, P1 en R2 zijn ongelijk (feedback 2).
5. **CTA's zijn zwak.** Knoppen zijn op mobiel niet over de volle breedte (ongeveer 180 tot 245 px breed op 390 px scherm), dezelfde neutrale werkwoorden ("Return to my cart", "See the pan", "See what's new"), geen voordeel in de knoptekst, en de knoppen sturen in checkout/cart niet naar een URL met de korting al toegepast.
6. **Hero-label en subregel zijn op mobiel te klein.** `make_hero.py` zet het label op 26 px en de subregel op 38 px in een 1200 px-beeld. Op een 390 px-telefoon is dat ongeveer 8,5 px en 12 px: onleesbaar. Juist daar zou het aanbod moeten staan.
7. **Geen echte urgentie.** C3-S zegt zelfs "nothing expires tonight". "Final call" en "Last reminder" (C4, K3) hebben geen deadline erachter. Echte deadlines zijn te maken met unieke, verlopende codes (zie deel D7).
8. **Te veel uitleg op de verkeerde plek, te weinig op de juiste.** Het "drie vragen"-blok staat in C2, W3, P3-accessory en (variant) R2: wie van welcome naar checkout gaat ziet het twee keer, met dezelfde hero-foto. Tegelijk ontbreekt: wat HI10 in dollars betekent, dat de code automatisch wordt toegepast, welke maat je moet kiezen, en waarom juist de Pan Pro (W4).
9. **Inconsistenties die vertrouwen kosten.**
   - "PFAS water purifier" (C3-S, C4, W5) tegen "PFAS water filter" (K3, P1, R2, DECISIONS). Kies "PFAS water filter", altijd met "win" of "a chance to win", nooit "free".
   - Pan Pro staat op "$134 $439" (W1, W4, P3, R2). Dat is 69 procent korting, terwijl R2 in de hero "Up to 50% off" belooft. Compare-at controleren in Shopify; de playbook eist echte compare-at-prijzen.
   - Gift-waardes ($15, $30, $25, $450) en "Five winners every week" (C3-S, C4) laten verifiëren door Floris voor livegang.
   - PLAYBOOK hoofdstuk 1 en 8 noemen nog "100-day trial" en "Lifetime warranty"; DECISIONS (1 okt) zegt 30-day returns en 75-year warranty. De mails volgen terecht DECISIONS; playbook bijwerken.
   - PLAYBOOK hoofdstuk 2 zegt "geen trust-bar" in flow-mails, de mails hebben er een. Met iconen (deel D2) is hij nuttig; regel in de playbook aanpassen.
10. **Hero-foto's dubbel over flows.** Dezelfde foto's komen terug: scallops/steak (C1, W1-A, W1-B), gehamerd oppervlak (C2, W3, R2-VIP), omelet (B2-clicked, W5, P3-pan), steak met deksel (B2-notclicked, W4-US, R1-pan), oven-kip (C4-INT, K3, W4-INT, R2), saus-afveeg (K1, P3-set), ei-flatlay (W0, P2), rode tegels met set (C3-S, P1-first, R1-set). Binnen één flow is het in orde, maar een welcome-abonnee die daarna afhaakt in checkout ziet C1 = W1 en C2 = W3. Bij herbouw unieke beelden per flowpad toewijzen.

---

## Deel B. Per mail

Scores 1 tot 10: H = helderheid, A = aanbodkracht, V = visuele hiërarchie, C = CTA, M = mobiel.

Overal waar "trust-bar met iconen", "gift-stack-blok", "aanbodblok", "reviewkaarten volgens spec" staat, gelden de specificaties uit deel D. Hero's worden gebouwd met `scripts/make_hero.py` (label, kop met `|` voor regelbreuk, subregel); de aanpassing van dat script staat in D1.

Standaardvervanging voor alle checkout- en cart-mails (verder "ICON-FEITEN"): verwijder elke levertijd. Vervang door drie icoon-feiten op één rij: [truck] "Free shipping", [return-arrow] "30-day returns", [shield] "75-year warranty". Voor INT een vierde: [globe] "Duties paid".

### Checkout

#### C1 · Your pan is still here
Onderwerp A/B: "Forgetting something?" / "Your pan is still here".
Scores: H 8 · A 2 · V 6 · C 5 · M 5

Top 5 fixes:
1. **Cart naar boven.** Verplaats het blok "Still in your cart" (line items) direct onder de hero, vóór "Hi Sarah". Voeg per regel onder de prijs een brick-regel toe: "10% off with HI10 at checkout". Daaronder de primaire knop.
2. **Aanbod in de hero.** Nieuwe hero (zie onder). Direct onder het cart-blok het compacte gift-stack-blok (4 iconen op één rij, D4).
3. **Blok "What happens after you order" schrappen.** "It ships within 1 business day" en "It arrives in 6 to 10 days" verdwijnen (feedback 1). "You have 30 days to decide" wordt het icoon-feit [return-arrow] "30-day returns" in de ICON-FEITEN-rij direct onder de knop.
4. **Knop.** Tekst "Complete my order" (in plaats van "Return to my cart"), volle breedte op mobiel, link `{{ event.extra.responsive_checkout_url }}` met `discount=HI10` als queryparameter (`?discount=HI10` of `&discount=HI10` afhankelijk van of de URL al een `?` bevat; eerst testen in een testcheckout). Herhaal de knop na het gift-stack-blok en onderaan (3 keer totaal).
5. **Reviewkaarten gelijk** (D3). Kies twee quotes van vergelijkbare lengte: Deb (175 tekens) inkorten tot "I cooked perfect over easy eggs for the first time in a non coated pan." en Susan laten staan.

Hero: label "STILL IN YOUR CART" · kop "Your cart,|10% lighter" · subregel "Code HI10 on top of the sale, plus 4 gifts".

Blokvolgorde: header · hero · cart-blok met HI10-regel · knop "Complete my order" · ICON-FEITEN · gift-stack (4 iconen) · "Hi Sarah" + 2 zinnen · 2 reviewkaarten · knop · founder-regel · footer.

#### C2 · Why Siraat (drie vragen)
Onderwerp: "Why Siraat?" / "Need a second opinion on that pan?"
Scores: H 7 · A 1 · V 5 · C 4 · M 4 (desktop 3.919 px, mobiel 4.004 px)

Top 5 fixes:
1. **Cart naar boven.** Het cart-blok staat nu op 2.800 px. Zet het onder de hero met dezelfde HI10-regel als C1.
2. **Aanbod toevoegen.** Hero met aanbod, en het aanbodblok (D5, compact, één regel code plus "Applied automatically") direct onder de knop.
3. **Inkorten.** De drie vragen blijven (dit is de kern volgens DECISIONS), maar als drie icoonrijen van één zin: [lab-flask] "Independent lab report: Light Labs, ISO/IEC 17025" · [document] "Report no. 25895, signed by the lab director" · [shield] "75-year warranty, no coating to fail". Schrap het ei-beeld met bijschrift (staat al in W0/P2) en de introzin "There are a lot of titanium pans out there". Lab-certificaat blijft als klikbare thumbnail, max 280 px hoog.
4. **Verschil met W3.** Wie de welcome-flow heeft gehad, kreeg dit blok al met dezelfde hero (gehamerd oppervlak). Gebruik een andere hero-foto en zet hier de cutaway (drie lagen) als hoofdbeeld onder de drie vragen.
5. **Knoppen** "Complete my order" (3x), volle breedte mobiel, met HI10 in de URL. Trust-bar naar ICON-FEITEN.

Hero: label "STILL IN YOUR CART" · kop "Tested. Then|10% off." · subregel "Lab report 25895. HI10 on top of the sale."

Blokvolgorde: header · hero · cart-blok + HI10-regel · knop · aanbodblok compact · drie vragen als icoonrijen · lab-certificaat thumbnail + link · cutaway · 2 reviews · gift-stack (4 iconen) · knop · ICON-FEITEN · founder-regel · footer.

#### C3-P · Pan-koper: upgrade naar de 6-delige set
Onderwerp: "Your cart is still at today's price" / "One pan, or three for $349?"
Scores: H 7 · A 6 · V 7 · C 6 · M 5

Top 5 fixes:
1. **Eigen cart boven de upsell, klein.** Nu staat "Or keep it simple" met het eigen product onderaan. Zet direct onder de hero een compacte twee-koloms keuze: links "Your cart: Pan Pro 11", $134" met tekstlink "Complete my order", rechts "6-piece set, $349" met knop. Dit is de beslissing van de mail; die moet boven de vouw.
2. **HI10 en gifts in de hero en in de rekensom.** "The math, plainly" krijgt een derde regel: "With HI10: another 10% off either option." Geen berekend eindbedrag zolang de saleprijs kan wijzigen.
3. **Prijsconsistentie.** Hero zegt "$349", rekensom zegt "One pan from $127", cart toont $134. Rekensom baseren op de pan die in de cart zit: "Your pan $134 + lid $59 = $193" via `event.extra.line_items` als dat kan, anders "from $186".
4. **Twee primaire knoppen voorkomen.** "SEE THE 6-PIECE SET" staat 3 keer als knop. Primaire knop: "Upgrade to the 6-piece set". Secundaire tekstlink: "Keep my one pan and check out". Onderaan dezelfde combinatie.
5. **Reviewkaarten gelijk**; Jardier M. inkorten tot "The quality is noticeably superior to other pans I've used."

Hero: label "UPGRADE YOUR CART" · kop "Make it|three" · subregel "3 pans + 3 lids, $349. Plus 10% with HI10."

Blokvolgorde: header · hero · keuzeblok (jouw cart / de set) · gift-stack 4 iconen · rekensom · setkaart met productbeeld · 1 regel lab + warranty met iconen · 2 reviews · knop + tekstlink · ICON-FEITEN · founder-regel · footer.

#### C3-S · Set-koper: reserved at today's price
Onderwerp: "Your cart is still at today's price" / "Your set, plus four gifts"
Scores: H 7 · A 5 · V 5 · C 5 · M 4

Top 5 fixes:
1. **Schrap "Nothing has changed and nothing expires tonight."** Dit haalt actief urgentie weg. Vervang door niets, of door een echte deadline als die er is (D7).
2. **Cart en gift-stack naar boven.** Volgorde: hero, cart-blok, knop, gift-stack met iconen. Nu staan de gifts op 1.450 px en het cart op 2.400 px.
3. **"What every piece in your set has" naar icoonrijen** (4 rijen, één zin elk): [no-coating] "Pure titanium cooking surface, no coatings" · [lab-flask] "Tested free from PFAS, report 25895" · [cooktop] "Gas, electric, induction, oven" · [shield] "One 75-year warranty for the whole set".
4. **Gift-stack-blok** volgens D4 met totaalregel "Worth $70 in gifts, plus a chance to win a $450 PFAS water filter." Woord "purifier" vervangen door "filter".
5. **HI10 toevoegen**: setkopers hebben de hoogste orderwaarde; 10 procent op $349+ is een sterk argument. Regel in de cart: "10% off with HI10 at checkout".

Hero: label "4 GIFTS WITH YOUR SET" · kop "Your set,|10% lighter" · subregel "HI10 on top of the sale. 4 gifts in the box."

Blokvolgorde: header · hero · cart-blok + HI10-regel · knop "Complete my order" · gift-stack · 4 icoonrijen · 2 reviews · knop · ICON-FEITEN · founder-regel · footer.

#### C4-INT · Final call, gifts included
Onderwerp: "Final call: your cart and your gifts" / "Your four gifts are still waiting"
Scores: H 7 · A 6 · V 6 · C 5 · M 5

Top 5 fixes:
1. **Echte deadline maken.** "Final call" zonder einde is loze urgentie. Voorstel: C4 krijgt een unieke Klaviyo-code (bijv. 15 procent of HI10 plus extra gift, beslissing Floris) die 48 uur na verzending verloopt. Dan mag de hero "Ends {{ datum }}" zeggen. Zonder unieke code: label "LAST REMINDER" laten en geen "final call" in de kop.
2. **Cart naar boven** (nu op 1.950 px). Cart-blok direct onder de hero.
3. **Gift-stack compact met iconen** (D4) in plaats van de lange genummerde lijst met uitleg per gift. "How each gift reaches you" schrappen; één regel "Nothing to add or enter: it all comes with your order." blijft.
4. **"Duties paid" als icoon-feit** in de ICON-FEITEN-rij (INT).
5. **Review Ozgard gaat over levertijd** ("less than I expected"). Vervangen door een review over koken, want levertijd noemen we niet meer.

Hero: met unieke code: label "ENDS {{ deadline }}" · kop "15% off,|48 hours" · subregel "Your code is inside. 4 gifts included." Zonder: label "LAST REMINDER" · kop "10% off +|4 gifts" · subregel "Your cart is saved. Code HI10 inside."

Blokvolgorde: header · hero · cart-blok + code-regel · knop · aanbodblok met code en deadline · gift-stack · 2 reviews · knop · ICON-FEITEN (met duties paid) · founder-regel · footer.

#### C4-US · Final call, met 12-delige set
Scores: H 6 · A 6 · V 5 · C 5 · M 4 (mobiel 3.770 px)

Top 5 fixes: 1 tot 4 als C4-INT. Daarnaast:
5. **12-delige set als kleine alternatief-kaart, onder de tweede knop**, niet ertussen. Nu concurreert "SEE THE 12-PIECE SET" met de cart. Titel "Cooking for a full house?" behouden, kaart max 200 px hoog op desktop. Compare-at $1,186 laten verifiëren.

Hero: als C4-INT.

Blokvolgorde: als C4-INT, met de 12-delige kaart na de reviews.

### Cart

Algemeen voor cart: links gaan naar `https://siraatskitchen.com/cart`. Op een ander apparaat is de cart leeg. Gebruik als fallback de product-URL uit het Added to Cart-event, en zet alle links via `/discount/HI10?redirect=/cart`.

#### K1 · One wipe. No scrubbing.
Onderwerp: "One pass with a damp cloth." / "About cleaning the pan in your cart"
Scores: H 7 · A 1 · V 5 · C 4 · M 5

Top 5 fixes:
1. **Cart naar boven** (nu op 2.150 px). Productkaart met prijs direct onder de hero.
2. **Aanbod**: hero met HI10, en onder de productkaart het gift-stack-blok (4 iconen, compact).
3. **Schoonmaak-uitleg inkorten**: de drie genummerde stappen worden één icoonrij: [sponge] "Warm water, soft sponge" · [dishwasher] "Dishwasher safe" · [sparkle] "Rainbow tint is normal". Chef-beeld met bijschrift mag blijven, maar onder de reviews.
4. **Knop** "Finish my order" (consequent voor cart), volle breedte mobiel, met HI10 in de link. Drie keer.
5. **Reviewkaarten gelijk.**

Hero: label "STILL IN YOUR CART" · kop "One wipe.|10% off." · subregel "Code HI10 on top of the sale. No scrubbing."

Blokvolgorde: header · hero · productkaart + HI10-regel · knop · gift-stack · korte intro (2 zinnen) · icoonrij schoonmaak · 2 reviews · chef-beeld · knop · ICON-FEITEN · founder-regel · footer.

#### K2-new · Built to outlast you
Onderwerp: "The pan you keep replacing is the expensive one" / "What a pan really costs per year"
Scores: H 7 · A 2 · V 6 · C 4 · M 4 (mobiel 3.407 px)

Top 5 fixes:
1. **Cart naar boven** (nu op 2.150 px).
2. **De rekensom ($15 tegen $1.79 per jaar) is het sterkste blok: houden**, direct onder de cart. Voeg een derde regel toe: "With HI10: another 10% off today."
3. **"Why it lasts" (3 punten) naar icoonrijen** van één zin; de uitleg van de drie lagen staat al in C2/W3.
4. **Kleine lettertekst** over wat de garantie dekt (nu 12 px grijs onder de trust-bar) verkorten tot één regel met link: "What the warranty covers →".
5. **Knop** "Finish my order", drie keer.

Hero: label "STILL IN YOUR CART" · kop "$1.79 a year.|Now 10% off." · subregel "Covered for 75 years. Code HI10 inside."

Blokvolgorde: header · hero · productkaart + HI10 · knop · rekensom · gift-stack · 3 icoonrijen · 2 reviews · knop · ICON-FEITEN · founder-regel · footer.

#### K2-returning · Good to see you again
Scores: H 8 · A 1 · V 6 · C 5 · M 6

Top 5 fixes:
1. **Terugkerende klanten krijgen een eigen bedankaanbod** in de hero. HI10 is publiek; beter een unieke code "THANKS-XXXX" (10 procent, 7 dagen geldig). Zonder nieuwe code: HI10.
2. **Productkaart staat al hoog (goed)**; zet hem boven de introtekst, direct onder de hero.
3. **Gift-stack** compact onder de kaart: "Same 4 gifts as last time."
4. **Reviewkaarten gelijk**; beide quotes inkorten tot onder 120 tekens.
5. **Knop** "Finish my order", 2 keer (mail is kort, dat is goed).

Hero: label "WELCOME BACK" · kop "Your cart,|10% off" · subregel "A thank-you for coming back. 4 gifts included."

Blokvolgorde: header · hero · productkaart · knop · aanbodblok (code) · gift-stack compact · 2 reviews · knop · ICON-FEITEN · founder-regel · footer.

#### K3 · Covered for 75 years, returnable for 30 days
Onderwerp: "Covered for 75 years. Returnable for 30 days." / "The last note about your cart"
Scores: H 7 · A 3 · V 5 · C 5 · M 5

Dit is de mail uit feedback 3: "Still in your cart" en "Finish my order" staan vlak boven de footer, de gifts als één grijze zin.

Top 5 fixes:
1. **Cart en "Finish my order" direct onder de hero.** Kopje "Still in your cart?" boven de productkaart.
2. **Gift-zin wordt het gift-stack-blok** (4 iconen, D4), direct onder de knop.
3. **"What happens after you order" naar ICON-FEITEN** met elk één korte regel eronder: [truck] "Free shipping" / "Tracking link by email" · [return-arrow] "30-day returns" / "Free return label" · [shield] "75-year warranty" / "Dents, warping, loose handles". Geen levertijd.
4. **Echte deadline** als laatste cart-mail: unieke code 48 uur geldig (D7), of anders geen "last" in de hero.
5. **De twee warranty-reviews (Steven T., Brandon W.) zijn goed gekozen**; inkorten tot gelijke lengte en als gelijke kaarten.

Hero: label "STILL IN YOUR CART" · kop "Finish your order,|10% off" · subregel "4 gifts. 30-day returns. 75-year warranty."

Blokvolgorde: header · hero · "Still in your cart?" + productkaart · knop "Finish my order" · gift-stack · ICON-FEITEN met subregels · 2 reviews · knop · founder-regel · footer.

### Browse

Feedback 5: browse heeft een echt aanbod met urgentie nodig. Voorstel: B1 krijgt HI10 plus gifts in de hero; B2 (beide takken) krijgt een unieke code met deadline.

#### B1 · No coating to scratch off
Onderwerp: "The pan with nothing to scratch off" / "What a metal spatula does to your pan"
Scores: H 7 · A 1 · V 6 · C 4 · M 5

Top 5 fixes:
1. **Aanbod in de hero** en een regel met de prijs na HI10 in de productkaart: "$134 · 10% off with HI10".
2. **Bekeken product direct onder de hero** (nu op 2.150 px), met knop "Get 10% off this pan" die naar `/discount/HI10?redirect=<product path>` gaat.
3. **Vergelijkingstabel houden** (helder, scanbaar), maar onder de productkaart. Rij "Warranty: Varies by brand" schrappen; vervangen door "Lab report you can read: Ask / No. 25895".
4. **"Honest note" (fijne krasjes)** behouden; het is goed vertrouwen. Wel naar 1 regel.
5. **Gift-stack** compact onder de knop.

Hero: label "THE PAN YOU VIEWED" · kop "10% off the pan|you looked at" · subregel "Code HI10, on top of the sale. Plus 4 gifts."

Blokvolgorde: header · hero · productkaart met HI10-prijsregel · knop · gift-stack · korte intro · vergelijkingstabel · eerlijke noot · 2 reviews · knop · ICON-FEITEN · lab-regel · footer.

#### B2-clicked · Still thinking it over?
Onderwerp: "10% off the pan you looked at" / "Still thinking it over?"
Scores: H 7 · A 5 · V 6 · C 5 · M 5

Top 5 fixes:
1. **Echte urgentie**: deze klikker is warm. Unieke code (15 procent of HI10 + extra gift, Floris beslist) geldig 72 uur, met de einddatum in de hero en in het codeblok: "Expires {{ datum }}, 23:59 ET".
2. **"USE HI10 NOW" linkt nu naar de productpagina zonder korting.** Alle links naar `/discount/<code>?redirect=<product path>`. Knoptekst "Claim my 10%" (of "Claim my 15%").
3. **Productkaart boven het codeblok**, codeblok direct eronder, dan gift-stack. Nu staat "Still thinking it over?" in de hero zonder het getal.
4. **Water-test-beeld** heeft ingebakken vette ondertitel ("TRY THE WATER TEST") die niet bij de huisstijl past. Vervangen door een frame zonder tekst (DECISIONS: er zijn genoeg frames zonder tekst) of schrappen.
5. **Drie reviewkaarten** (2 + 1 brede) zijn ongelijk. Twee gelijke kaarten.

Hero: label "ENDS {{ deadline }}" · kop "10% off,|72 hours" · subregel "On top of the sale. Plus 4 gifts." (Fallback zonder unieke code: label "10% ON TOP OF THE SALE" · kop "10% off the pan|you looked at".)

Blokvolgorde: header · hero · productkaart met prijs na korting · knop · codeblok met deadline · gift-stack · 2 reviews · knop · ICON-FEITEN · kleine voorwaardenregel · footer.

#### B2-notclicked · Week one, in their words
Scores: H 7 · A 1 · V 6 · C 4 · M 6

Top 5 fixes:
1. **Aanbod toevoegen.** Ook niet-klikkers krijgen HI10 in de hero; de reviews blijven het verhaal.
2. **Bekeken product ontbreekt helemaal.** Voeg de productkaart toe direct onder de hero (dynamisch uit Viewed Product).
3. **Knop** "Take another look" wordt "Get 10% off this pan".
4. **De 4-sterrenreview (Mrs H.)** staat als enige met een grijze ster. Eerlijk, maar in een mail met vier reviews is het de eerste die opvalt. Vervangen door een 5-sterrenreview over een tweede aankoop.
5. **Vier secties met eigen kop** ("The first egg", "The doubter"...) zijn mooi, maar lang. Twee per rij als gelijke kaarten met een klein label boven de quote.

Hero: label "100,000+ HAPPY CUSTOMERS" · kop "In their words.|10% off for you." · subregel "Code HI10 on top of the sale."

Blokvolgorde: header · hero · productkaart + HI10 · knop · 4 reviews in 2x2 · gift-stack · knop · ICON-FEITEN · founder-regel · footer.

### Welcome

#### W0 · Kopers-pad: Thank you. Now the first egg.
Onderwerp: "Thank you. Now the first egg." / "Before your pan arrives: three steps"
Scores: H 8 · A 2 · V 7 · C 5 · M 5

Dit is een service-mail voor wie al gekocht heeft; een kortingsaanbod hoort hier niet in de hero. Uitzondering op regel 4, expliciet.

Top 5 fixes:
1. **Overlap met P2.** Een koper krijgt P1, W0 en na levering P2 met dezelfde drie stappen en dezelfde hero-foto (ei-flatlay). Maak W0 kort (bevestiging card game in één regel, link naar de cook guide, één tip) of laat W0 vervallen voor wie in de laatste 7 dagen in post-purchase zit.
2. **Andere hero-foto dan P2.**
3. **"Good to know" naar ICON-FEITEN**: [no-seasoning] "No seasoning" · [utensil] "Metal utensil safe" · [dishwasher] "Dishwasher safe" · [shield] "75-year warranty". Dat dubbelt nu met de trust-bar eronder; één van beide schrappen.
4. **Zachte cross-sell onderaan**: lid ("The lid that fits your pan, $59"), als kleine kaart.
5. **Knop** "Watch the cook guide" is goed; volle breedte op mobiel.

Hero: label "CARE AND USE" · kop "First heat,|then oil." · subregel "Your first egg, in three steps" (ongewijzigd, andere foto).

Blokvolgorde: header · hero · knop · 2 zinnen intro + card-game-regel · 3 stappen met beelden · 1 review · ICON-FEITEN · lid-kaart · founder-regel · footer.

#### W1-A · The original + HI10 (codeblok)
Onderwerp: "Welcome. 10% on top of the sale, no catch." / "The original hammered titanium pan, plus 10%"
Scores: H 6 · A 6 · V 4 · C 5 · M 4

Feedback 6: het welkomstaanbod moet boven het verhaal over de originele gehamerde pan, in de hero. Op mobiel begint het aanbodblok nu op 890 px, onder de vouw.

Top 5 fixes:
1. **Hero leidt met het aanbod** (zie onder). De zin "The original hammered pan" wordt het label.
2. **Aanbodblok (het donkere espresso-blok, al goed ontworpen) direct onder de hero**, vóór "Hi Sarah". Codevak groter (code 32 px), knop wit op espresso "Claim my 10% + gifts" volle breedte.
3. **Gift-stack direct onder het aanbodblok.** DECISIONS: de gift-stack hoort bij de Hammered Pan; dat is precies de pan die W1 verkoopt. Totaal "Worth $70 in gifts, plus a chance to win a $450 PFAS water filter."
4. **Verhaal inkorten tot 3 zinnen** onder de gifts: card-game-regel (één zin), dan "Siraat makes the original hammered titanium pan. First orders shipped December 20, 2024. Look-alikes came after." "What makes it the original" naar 4 icoonrijen.
5. **Productkaart Pan Pro met prijs na HI10 en maatkeuze**: "Standard 11″: for 1 or 2 people · Large 12″: for a family". Compare-at $439 verifiëren.

Hero: label "THE ORIGINAL HAMMERED PAN" · kop "10% off|+ 4 gifts" · subregel "Welcome. Code HI10, on top of the sale."

Blokvolgorde: header · hero · aanbodblok (code + knop) · gift-stack · card-game-regel + 3 zinnen verhaal · 4 icoonrijen "What makes it the original" · productkaart + maatkeuze · 2 reviews · knop · ICON-FEITEN · founder-regel · footer.

#### W1-B · The original + HI10 als gift card
Scores: H 6 · A 6 · V 4 · C 5 · M 4

Top 5 fixes: identiek aan W1-A, met deze verschillen:
1. **De gift-card-visual is het sterkste beeld van de hele flow.** Zet hem in de hero: een hero-variant waarin de kaart op de foto ligt, of de kaart zelf direct onder een kortere hero.
2. **Tekst onder de kaart** nu twee regels klein grijs. Maak er één regel van 16 px: "Your welcome gift card: 10% on top of the sale. Applied automatically."
3. **Knop** "Use my gift card" is goed; volle breedte, direct onder de kaart.
4. **Zelfde volgorde als W1-A**, zodat de A/B-test alleen de framing meet (dat is ook de bedoeling volgens de topcomment).
5. **Gift-stack direct onder de kaart.**

Hero: label "WELCOME GIFT CARD" · kop "10% off|+ 4 gifts" · subregel "Your gift card is inside. Code HI10."

Blokvolgorde: als W1-A, met de gift-card-visual als aanbodblok.

#### W2 · Why I started (tekstmail, Benjamin)
Onderwerp: "Why I started Siraat's Kitchen" / "The pan nobody else was making"
Scores: H 8 · A 3 · V 7 · C 4 · M 7

Tekstmails halen 1,3 procent klik tegen 0,3 tot 0,6 voor beeldmails (playbook). Vorm houden.

Top 5 fixes:
1. **Aanbod bovenaan, als tekst**: één regel vóór "Hi Sarah" in 14 px, brick: "Your welcome code HI10 still takes 10% off on top of the sale →" (link `/discount/HI10?redirect=/products/...`). Geen banner.
2. **Alinea 3 (het idee, 8 regels) inkorten tot 4 regels.** Uitleg van het gehamerde patroon komt terug in W3 en W4.
3. **Twee links in de tekst** in plaats van één: "the pan that started it" en onderaan "Use HI10 on the Pan Pro".
4. **P.S. versterken** met de gifts: "P.S. Every Hammered Pan comes with 4 gifts right now: free shipping, a mystery gift, our Plastic-Free Home e-book and a chance to win a PFAS water filter."
5. **Geen knop** toevoegen; de tekstmail werkt als brief.

Hero: geen (tekstmail). Bovenste regel zie fix 1.

Blokvolgorde: header · aanbodregel · brief (5 korte alinea's) · handtekening · P.S. met gifts · footer.

#### W3 · Tested. Not claimed.
Onderwerp: "Has your cookware actually been tested?" / "Three questions to ask any titanium pan brand"
Scores: H 7 · A 3 · V 6 · C 4 · M 4 (mobiel 4.183 px)

Top 5 fixes:
1. **Aanbod in de hero en onder de eerste knop.** Nu staat HI10 pas op 3.500 px.
2. **Twee knoppen met verschillende doelen in de hero-zone.** Primair: "Shop the Pan Pro with 10%" (HI10-link). Secundair, tekstlink: "Read the lab report".
3. **Inkorten**: de drie vragen als icoonrijen (zie C2); de cutaway en de vergelijkingstabel houden, want dit is de bewijsmail. Introtekst naar 2 zinnen.
4. **Vergelijkingstabel op mobiel**: 5 kolommen worden te krap op 390 px. Op mobiel alleen "Coated pan" tegen "Siraat" tonen (aparte mobiele tabel met `display:none` switch).
5. **Gift-stack** compact boven de slotknop.

Hero: label "LIGHT LABS REPORT NO. 25895" · kop "Tested.|Then 10% off." · subregel "Read the report. Code HI10 on top of the sale."

Blokvolgorde: header · hero · knop + tekstlink rapport · drie vragen (icoonrijen) · certificaat-thumbnail · cutaway · vergelijkingstabel · 2 reviews · gift-stack · knop · ICON-FEITEN · founder-regel · footer.

#### W4-US · Three ways to start
Onderwerp: "Three ways to start" / "Under $80, one pan, or the whole kitchen"
Scores: H 6 · A 4 · V 5 · C 4 · M 3 (mobiel 5.206 px, de langste mail)

Feedback 7: veel meer over de pan zelf, waarom de Pan Pro.

Top 5 fixes:
1. **Herstructureer naar "Start with the Pan Pro"**: de Pan Pro wordt de hoofdzaak direct onder de hero, met een groot productbeeld en 5 icoonrijen "Why the Pan Pro":
   - [no-coating] "Pure titanium cooking surface. No coatings to wear off, ever."
   - [layers] "3-ply: titanium, an aluminium core for even heat, a steel base."
   - [hammer] "The hammered pattern: less of your food touches the metal."
   - [cooktop] "Gas, electric, induction and oven."
   - [lab-flask] "Lab tested: Light Labs report 25895. 75-year warranty."
2. **Maatkiezer** onder de Pan Pro: vier maten met voor wie ("Mini 8″: eggs for one", "Standard 11″: 1 or 2 people", "Large 12″: a family") en prijs per maat. Small-maat en prijzen per maat uit `content/facts/` halen, niet gokken.
3. **Prijs na HI10 tonen** en de gift-stack direct onder de Pan Pro (de gifts horen bij de Hammered Pan).
4. **"Start small" en "The whole kitchen" demoten**: één compacte rij van 3 kleine kaarten ("Or start smaller: board from $69" · "Or go all in: 6-piece set $349" · "12-piece set $599, US only"). Dishwasher Sheets eruit; die passen in post-purchase (P3-set).
5. **Knoppen**: "Shop the Pan Pro with 10%" (primair, 3x). "Choose your start" is te vaag.

Hero: label "THE ONE MOST PEOPLE PICK" · kop "Start with|the Pan Pro" · subregel "10% off with HI10, plus 4 gifts."

Blokvolgorde: header · hero · Pan Pro-kaart met prijs na HI10 · knop · 5 icoonrijen "Why the Pan Pro" · maatkiezer · gift-stack · 2 reviews over de Pan Pro · rij "Or start smaller / go all in" · knop · ICON-FEITEN · founder-regel · footer.

#### W4-INT · Three ways to start (zonder 12-pcs, zonder prijzen)
Scores: H 6 · A 3 · V 5 · C 4 · M 3

Top 5 fixes: als W4-US (Pan Pro centraal, 5 icoonrijen, maatkiezer zonder prijzen, gift-stack, knop "Shop the Pan Pro with 10%"). Verschillen:
1. **Geen prijzen is een zwakte**: toon "Prices in your currency at checkout" direct bij de Pan Pro, zodat het ontbreken van een prijs geen verrassing is.
2. **"Duties paid" als icoon in de ICON-FEITEN-rij** (staat er al, goed) en ook in de hero.
3. **Cookware Set Pro "Our first pick outside the US"** blijft als enige set in de compacte rij.

Hero: label "SHIPS WORLDWIDE · DUTIES PAID" · kop "Start with|the Pan Pro" · subregel "10% off with HI10, plus 4 gifts."

Blokvolgorde: als W4-US.

#### W5 · In their words + HI10 herinnering
Onderwerp: "In their words (and your 10% is still here)" / "What 100,000+ happy customers found out"
Scores: H 7 · A 6 · V 5 · C 6 · M 4

Top 5 fixes:
1. **Aanbodblok en gift-stack naar direct onder de hero.** Nu staan ze op 1.700 en 2.000 px, na 5 reviews.
2. **Echte deadline**: "This is the last time we mention it in this series" is waar, maar HI10 blijft werken. Voorstel: welkomstcode per profiel uniek en 10 dagen geldig vanaf inschrijving (D7). Dan zegt W5 terecht "Your 10% ends {{ datum }}". Zonder unieke code: geen "last chance".
3. **Gift-tegels gelijk** (nu 2x2 met tegel 4 hoger). Gift-stack-blok volgens D4 met iconen in plaats van cijfers.
4. **Productkaarten zonder prijs** (Pan Pro, Duo). Prijs en prijs na HI10 toevoegen; Duo-prijs uit Shopify.
5. **Reviews: 5 is te veel.** Featured quote (Tammy) plus 2 gelijke kaarten. Brandon W. (garantie) verplaatsen naar de garantieregel onderaan, die hem al noemt.

Hero: label "ENDS {{ deadline }}" (of "STILL YOURS") · kop "Your 10%|+ 4 gifts" · subregel "Last welcome email. Code HI10 inside."

Blokvolgorde: header · hero · aanbodblok + knop · gift-stack · featured review · 2 reviews · Pan Pro + Duo met prijzen · knop · ICON-FEITEN · founder-regel · footer.

### Post-purchase

Regel 4 (aanbod altijd bovenaan) geldt hier als volgt: P1 en P2 zijn service-mails; het "aanbod" bovenaan is de bevestiging van de 4 gifts. P3 krijgt wel een echt kortingsaanbod.

Levertijd (feedback 1): P1 noemt "Within 1 business day" en "6 to 10 days". Volgens de opdracht eruit. Risico: meer "waar is mijn bestelling"-vragen. Daarom vervangen door een tracking-belofte, niet door niets.

#### P1-first · Good call. Here's what's coming.
Onderwerp: "Good call. Here's what's coming." / "You bought a pan from an ad. Good call."
Scores: H 7 · A 5 · V 5 · C 4 · M 4 (mobiel 4.113 px)

Top 5 fixes:
1. **Timeline "From order to first egg" herschrijven zonder duur** en met iconen: [box] "We pack and check it" · [mail] "Your tracking link arrives by email" · [truck] "Free shipping, tracked to your door" · [egg] "The day after delivery: the chef's first-cook guide". Preview-tekst "and when it ships" mag blijven.
2. **Gifts boven de timeline, met iconen** (D4). Nu cijfers 1 tot 4 in ongelijke tegels.
3. **Hero-kop past niet**: "Good call. Here's what's coming." loopt over 3 regels en raakt de subregel. Twee regels (zie onder).
4. **Knop "Watch the cook guide" past niet bij moment 1 uur na aankoop.** Primaire actie: "See your 4 gifts" (anker) of de e-book-download ("Download your e-book"), als die link er is. Dat geeft direct waarde en bevestigt de gift-stack.
5. **Introtekst** (2 alinea's) naar 2 zinnen. Onderwerp B ("You bought a pan from an ad") schrappen: klinkt verwijtend en is niet voor iedereen waar.

Hero: label "ORDER CONFIRMED" · kop "Good call.|4 gifts coming." · subregel "Your order, your gifts, what happens next".

Blokvolgorde: header · hero · knop "Download your e-book" · order-blok · gift-stack met iconen · timeline met iconen · chef-tip · 2 reviews · ICON-FEITEN · founder-regel · footer.

#### P1-repeat · Good to see you again
Onderwerp: "Good to see you again" / "Round two. Here's what's coming."
Scores: H 8 · A 5 · V 6 · C 4 · M 5

Top 5 fixes:
1. **Preview-tekst "same 6 to 10 days" vervangen** door "Your order is in. Same packing, same 4 gifts."
2. **"Packed within 1 business day" en "6 to 10 days to you" eruit**; vervangen door [mail] "Tracking link by email" en [truck] "Free shipping".
3. **Gift-tegels gelijk en met iconen**; de dubbele introductie ("Your gifts, again" + een zin met alle vier + vier tegels) naar alleen de tegels.
4. **Knop "See the care guide"** werkt voor een terugkerende klant nauwelijks. Primair: "Download your e-book". Secundair: tekstlink care guide.
5. **Bedankregel naar boven**: "Thank you for coming back" staat nu onderaan; zet hem in de intro.

Hero: label "ORDER CONFIRMED" · kop "Good to see|you again." · subregel "Same packing, same 4 gifts".

Blokvolgorde: header · hero · knop · bedank-intro · order-blok · gift-stack · 3 icoon-stappen · founder-regel · footer.

#### P2 · If you can do an egg
Onderwerp: "If you can do an egg, you can do anything" / "First egg: heat first, then a thin layer of oil"
Scores: H 8 · A 1 · V 7 · C 5 · M 5

De beste educatiemail van het systeem. Weinig wijzigen.

Top 5 fixes:
1. **Water-test-beeld met ingebakken vette tekst** vervangen door een frame zonder tekst.
2. **"Looking after it" (3 kolommen, ongelijk hoog)** naar icoonrijen: [dishwasher] [sparkle] [no-seasoning].
3. **Lid-cross-sell** staat als grijze regel onder de laatste knop. Maak er een kleine productkaart van ("The lid that fits your Pan Pro, $59") na de "If something sticks"-box.
4. **UGC-oproep** ("Send us your first egg") naar direct onder de hero, met knop "Send us your first egg" (mailto/reply). Dat is de doelmetric van deze mail volgens p4-note.
5. **Andere hero dan W0.**

Hero: ongewijzigd: label "CHEF GUIDE" · kop "If you can|do an egg" · subregel "you can do anything. The chef's first-cook guide."

Blokvolgorde: header · hero · knop chef-video · intro · 5 stappen · "If something sticks" · lid-kaart · icoonrijen verzorging · 2 reviews · UGC-oproep · ICON-FEITEN · footer.

#### P3-accessory · Now meet the pan
Onderwerp: "Now the pan it was made for" / "The pan behind 100,000+ happy customers"
Scores: H 7 · A 2 · V 6 · C 5 · M 4 (mobiel 4.493 px)

Top 5 fixes:
1. **Aanbod**: klant-bedankcode in de hero (HI10 of unieke "THANKS-XXXX", 7 dagen). Een accessoire-koper overtuig je met een reden en een prijs.
2. **Pan Pro-kaart heeft een groot wit vlak boven de foto** (beeld valt naar beneden in de tabelcel). Beeld bovenaan uitlijnen (`valign="top"`), en de vinkjeslijst vervangen door de 5 icoonrijen uit W4.
3. **Drie vragen**: dit is de derde keer voor wie ook welcome kreeg. Inkorten tot één regel met icoon: [lab-flask] "Lab tested: report 25895, all pans. 75-year warranty."
4. **"Or go all in"**: utensils ("If you have the board, these are its other half") is los van de pan. Houd de 6-delige set, schrap utensils.
5. **Knop** "Meet the Pan Pro" wordt "Get the Pan Pro, 10% off".

Hero: label "FOR SIRAAT OWNERS" · kop "Now meet the pan.|10% off." · subregel "Your thank-you code is inside."

Blokvolgorde: header · hero · Pan Pro-kaart met prijs na code · knop · aanbodblok · icoonrijen "Why the Pan Pro" · lab-regel · 6-delige set · 2 reviews · knop · ICON-FEITEN · founder-regel · footer.

#### P3-pan · What goes with your pan
Onderwerp: "The one thing your pan is missing" / "Which lid fits your pan?"
Scores: H 7 · A 2 · V 6 · C 5 · M 4

Top 5 fixes:
1. **Aanbod in de hero**: "The lid, 10% off" met bedankcode.
2. **Lid-kaart: zelfde wit-vlak-probleem** als P3-accessory; beeld bovenaan.
3. **Lid-maat dynamisch**: als de gekochte maat in `event` zit, toon "The 11″ lid for your Standard Pan Pro". Grootste wrijving bij deze aankoop is de maatkeuze.
4. **4-sterrenreview (Joanna C.)** is wel relevant (noemt het deksel); houden, kaarten gelijk.
5. **Slotknop "Complete your kitchen"** naar `/collections/accessories` is vaag; zelfde knop als bovenaan: "Add the lid, 10% off".

Hero: label "FITS YOUR PAN" · kop "The lid,|10% off" · subregel "For owners only. Code inside."

Blokvolgorde: header · hero · lid-kaart · knop · aanbodblok · board + 2 Pans 2 Lids · 2 reviews · knop · ICON-FEITEN · founder-regel · footer.

#### P3-set · Two weeks with your set
Onderwerp: "Two weeks with your set" / "The one pan your set doesn't have"
Scores: H 7 · A 2 · V 6 · C 5 · M 4

Top 5 fixes:
1. **Hoofdproduct kiezen.** Hero gaat over "keep it shining", knop is dishwasher sheets ($25), maar het geld zit in de crepe-pan/wok ($119 tot $139). Primair: de ontbrekende pan. Sheets als kleine kaart.
2. **Aanbod**: bedankcode in de hero.
3. **Wit vlak boven de sheets-foto**; beeld bovenaan.
4. **"$25 $60 or 20% off on subscription"**: compare-at $60 bij $25 verifiëren. Abonnement is uitgesloten van HI10; zeg dat bij de code.
5. **Hero-foto (saus afvegen) is dezelfde als K1**; andere foto, bij voorkeur de set op het fornuis.

Hero: label "FOR SET OWNERS" · kop "The pan your set|is missing" · subregel "Crepe or wok, 10% off. Code inside."

Blokvolgorde: header · hero · crepe + wok kaarten · knop · aanbodblok · sheets-kaart · 2 reviews · knop · ICON-FEITEN · founder-regel · footer.

### Winback

#### R1-pan · New since your last order
Onderwerp: "New since your last order" / "Three things we made since your pan"
Scores: H 6 · A 1 · V 6 · C 4 · M 4 (mobiel 4.125 px)

Top 5 fixes:
1. **"We need to publicly apologize." schrappen.** Klinkt als een incident, wekt schrik, en de toon past niet bij de flow-register (kalm, direct). Openingszin: "Two months with your pan. Here is what we made since."
2. **Aanbod**: bedankcode of HI10 in de hero. Nu heeft R1 geen enkel aanbod.
3. **Drie productkaarten in 3 kolommen** zijn op desktop krap (tekst 13 px) en op mobiel lang. Twee kaarten per rij, of 2 Pans + 2 Lids als featured en wok/crepe als kleine rij.
4. **Lid-box** ("Still cooking without a lid?") is het meest relevante aanbod voor een pan-eigenaar. Omhoog, direct onder de hero.
5. **Knop "See what's new"** naar `/collections/all` is vaag. "Shop with my 10%".

Hero: label "NEW SINCE YOUR LAST ORDER" · kop "New pans,|10% off for you" · subregel "Same titanium. Same 75-year warranty."

Blokvolgorde: header · hero · lid-box · knop · aanbodblok · featured 2 Pans + 2 Lids · wok + crepe · 2 reviews · knop · ICON-FEITEN · founder-regel · footer.

#### R1-set · Your set, one step further
Scores: H 7 · A 1 · V 6 · C 4 · M 4

Top 5 fixes:
1. **Aanbod** in hero (zie R1-pan).
2. **3 kolommen naar 1 featured (crepe-pan) + 2 klein.**
3. **Knop** "Shop with my 10%".
4. **Hero-foto is dezelfde als P3-set-advies en P1-first** (rode tegels). Kies een andere.
5. **Reviewkaarten gelijk.**

Hero: label "FOR SET OWNERS" · kop "Your set,|one step further" · subregel "10% off what is new. Code inside."

Blokvolgorde: header · hero · featured crepe-pan · knop · aanbodblok · utensils + board · 2 reviews · knop · ICON-FEITEN · founder-regel · footer.

#### R2 · Up to 50% off. What's the catch?
Onderwerp: "Up to 50% off. What's the catch?" / "Your next piece: up to 50% off, with 4 gifts"
Scores: H 7 · A 6 · V 6 · C 5 · M 4 (mobiel 4.837 px)

Top 5 fixes:
1. **Tegenstrijdigheid**: hero "Up to 50% off", productkaart Pan Pro "$134 $439" (69 procent). Eén van beide klopt niet. Compare-at in Shopify controleren voor verzending.
2. **Gift-stack naar direct onder de hero** (nu op 2.200 px) en met iconen.
3. **"What's the catch?"-blok** (3 vragen) naar ICON-FEITEN met subregels; spaart 300 px.
4. **"The sale will not run forever"** is vaag. Of de echte einddatum (zodra Floris die geeft; DECISIONS: nog niet bekend), of schrappen.
5. **Knop "Shop the sale"** wordt "Shop up to 50% off". Producten in 3 kolommen naar 2 per rij.

Hero: label "UP TO 50% OFF + 4 GIFTS" · kop "Up to 50% off.|No catch." · subregel "Free shipping. 30-day returns. 4 gifts."

Blokvolgorde: header · hero · knop · gift-stack · producten (2 per rij) · ICON-FEITEN met subregels · 2 reviews · knop · founder-regel · footer.

#### R2-vip · Thank you for coming back
Onderwerp: "A thank you: 10% on top of the sale" / "For our regulars: HI10 on top of up to 50% off"
Scores: H 7 · A 5 · V 5 · C 5 · M 4 (mobiel 5.104 px)

Top 5 fixes:
1. **Het VIP-aanbod is hetzelfde als het publieke welkomstaanbod (HI10).** Volgens het flow-document krijgt VIP "sterker aanbod". Unieke VIP-code, bijv. 15 procent bovenop de sale, 7 dagen geldig (DECISIONS: geen maximale korting vastgelegd).
2. **Codeblok staat goed boven de producten**, maar hero noemt het getal pas in de subregel. Getal in de kop.
3. **Twee blokken met dezelfde 3 vragen ("The usual promises") en gifts** maken de mail 5.104 px op mobiel. Promises naar ICON-FEITEN.
4. **4-sterrenreview Mrs H.** vervangen door een 5-sterren herhaalkoper.
5. **Knop** "Shop with my 15%" (of 10%), volle breedte.

Hero: label "FOR OUR REGULARS" · kop "15% on top,|for you" · subregel "Up to 50% off, plus your code. Ends {{ datum }}."

Blokvolgorde: header · hero · aanbodblok met deadline · knop · gift-stack · producten · 2 reviews · knop · ICON-FEITEN · founder-regel · footer.

---

## Deel C. Uitleg: waar te weinig, waar te veel (feedback 8)

**Te weinig:**
- Wat HI10 concreet doet. Toon de prijs na korting bij elk product ("$134 → $120.60 with HI10") zodra de saleprijs vaststaat bij verzending, anders "10% off at checkout".
- Dat de korting automatisch wordt toegepast. Elke HI10-knop gaat via `/discount/HI10?redirect=...`; zeg erbij: "Applied automatically."
- Welke maat. Geen enkele verkoopmail heeft een maatkiezer; alleen "reply and we will tell you". Maatkiezer in W1, W4, P3-pan.
- Waarom de Pan Pro (W4, P3-accessory): zie de 5 icoonrijen.
- Wat de gifts waard zijn: alleen C3-S/C4 noemen de waarde. Overal dezelfde totaalregel.
- Browse: er is geen enkele reden om nu te kopen.

**Te veel:**
- C2 (3.919 px) en W3 (3.929 px): drie vragen + certificaat + cutaway + ei + tabel. Kies per mail twee bewijsstukken.
- W4-US (mobiel 5.206 px): zes producten in drie categorieën.
- P1-first: timeline met vier stappen en uitleg per stap.
- R2-vip: aanbod, gifts en promises herhalen dezelfde boodschap.
- Het drie-vragen-blok in C2, W3, P3-accessory en (variant) R2: één keer volledig (W3), elders als één icoonregel.

---

## Deel D. Systeemregels

### D1. Above-the-fold-patroon per flowtype

Doel: op een 390 x 844-telefoon (zichtbaar ongeveer 700 px na mailclient-chrome) staan aanbod, product/cart en knop zichtbaar.

Wijziging hero: `scripts/make_hero.py` aanpassen:
- Label 40 px (nu 26) en pil 84 px hoog: op mobiel ongeveer 13 px.
- Subregel 48 px (nu 38): op mobiel ongeveer 15,5 px.
- Nieuwe optionele zesde parameter `offer`: een brick-balk (#AC3B19) van 140 px hoog onderaan het beeld met de aanbodregel in Inter SemiBold 44 px, wit, hoofdletters, bijv. "10% OFF WITH HI10 · 4 GIFTS". Zo staat het aanbod altijd in het beeld, ook als de kop iets anders zegt.
- Voor checkout, cart en browse een 4:3-variant (1200x900) toestaan: scheelt 100 px op mobiel, en daarmee past de cart boven de vouw. Dit wijkt af van PLAYBOOK 10 (1200x1200); beslissing Siraat, aanbevolen.
- Alt-tekst van de hero bevat altijd het aanbod letterlijk (beelden staan vaak uit).

Patronen (van boven naar beneden):

| Flow | Boven de vouw (mobiel) | Direct daarna |
|---|---|---|
| Checkout | Header · hero 4:3 met aanbodbalk · cart-blok (line items, prijs, HI10-regel) · knop "Complete my order" | ICON-FEITEN · gift-stack · bewijs · reviews · knop · ICON-FEITEN · founder |
| Cart | Header · hero 4:3 met aanbodbalk · productkaart met prijs + HI10-regel · knop "Finish my order" | gift-stack · één bewijsblok · reviews · knop · ICON-FEITEN · founder |
| Browse | Header · hero 4:3 met aanbodbalk · bekeken product met prijs na korting · knop "Get 10% off this pan" | codeblok (met deadline in B2) · gift-stack · vergelijking/reviews · knop |
| Welcome | Header · hero 1:1 met aanbod in de kop · aanbodblok (code, "Applied automatically", knop) | gift-stack · kort verhaal of bewijs · product · reviews · knop |
| Post-purchase P1/P2 | Header · hero · knop (e-book of chef-guide) · order-blok of eerste stap | gift-stack (P1) · stappen · reviews |
| Post-purchase P3 | Header · hero met bedankcode · hoofdproduct met prijs na code · knop | aanbodblok · tweede product · reviews · knop |
| Winback | Header · hero met aanbod · aanbodblok of eerste product · knop | gift-stack · producten · reviews · knop |

### D2. Iconenset

Eén set, lijn-iconen, 2 px lijn, brick #AC3B19 op transparant, PNG geleverd op 96x96 en getoond op 32x32 (gift-stack 40x40). Zelf tekenen of uit een open set (bijv. Lucide, MIT) en exporteren; nooit AI-gegenereerd. Opslaan als `klaviyo/templates/partials/assets/icon-<naam>.png` en via `klaviyo-urls.txt` in de bibliotheek. Altijd `alt` met de tekst van het feit.

| Naam | Betekenis | Waar |
|---|---|---|
| truck | Free shipping | ICON-FEITEN alle mails, gift-stack |
| return-arrow | 30-day returns | ICON-FEITEN alle mails |
| shield | 75-year warranty | ICON-FEITEN, bewijsrijen |
| globe | Duties paid (INT) | ICON-FEITEN C4-INT, W4-INT, C3-S |
| gift-box | Mystery gift | gift-stack |
| book | Plastic-Free Home e-book | gift-stack, P1-knop |
| water-drop-filter | Chance to win a PFAS water filter | gift-stack |
| tag-percent | HI10 / kortingscode | aanbodblok, cart-regel |
| clock | Echte deadline (alleen bij een verlopende code) | aanbodblok B2, C4, K3, W5, R2-vip |
| lab-flask | Lab tested, Light Labs | bewijsrijen C2, W3, W4, P3 |
| document | Report no. 25895 | bewijsrijen C2, W3 |
| no-coating | Pure titanium cooking surface, no coatings | W1, W4, C3-S, P3 |
| layers | 3-ply: titanium, aluminium, steel | W4, P3-accessory |
| hammer | Hammered pattern | W1, W4 |
| cooktop | Gas, electric, induction, oven | C3-S, W4 |
| utensil | Metal utensil safe | B1, W0 |
| dishwasher | Dishwasher safe | K1, W0, P2 |
| no-seasoning | No seasoning | W0, P2 |
| sparkle | Rainbow tint is normal | K1, P2 |
| sponge | Warm water and a soft sponge | K1 |
| box | We pack and check it | P1 |
| mail | Tracking link by email | P1, P1-repeat, K3 |
| egg | First cook guide | P1 |
| chat | Reply, a real person reads it | founder-regel (optioneel) |

ICON-FEITEN-rij: 3 (of 4 voor INT) gelijke cellen, icoon gecentreerd 32 px, daaronder het feit in Inter SemiBold 12 px hoofdletters met 1 px letterspatiëring, optioneel een subregel 12 px grijs. Op mobiel blijven 3 naast elkaar (passen bij 390 px); 4 cellen worden 2x2. Nooit levertijd.

### D3. Reviewkaart-spec

- Twee kaarten per rij op desktop, gelijk hoog. Techniek: de achtergrond (#FFFFFF) en rand (1 px #ECE7DD) op de kolom-`<td>` zelf zetten, niet op een geneste tabel; tussen de twee kolommen een lege spacer-`<td width="14">`. Cellen in dezelfde `<tr>` krijgen in alle clients dezelfde hoogte. `valign="top"` op de inhoud. Op mobiel (class `stack`) onder elkaar, elke kaart volle breedte.
- Inhoud van boven naar beneden: 5 sterren (brick, 14 px) · quote Inter 15/22 px, maximaal 120 tekens (inkorten met "..." mag, niets toevoegen) · naam + "Verified buyer" 12 px grijs SemiBold · optioneel land.
- Twee quotes per rij selecteren op gelijke lengte (verschil maximaal 30 tekens).
- Alleen 5-sterrenreviews in verkoopmails; een 4-ster alleen als hij inhoudelijk uniek is (P3-pan, lid).
- Optioneel klantfoto 64x64 linksboven (DECISIONS: UGC mag).
- Geen oneven aantal: 2 of 4. Eén uitgelichte quote (W5-stijl) mag als volle breedte bovenaan.
- Onder de rij: "Join 100,000+ happy customers." (DECISIONS). Nooit "independent" of "unsolicited".
- Dezelfde spec voor gift-tegels en "Looking after it"-kolommen.

### D4. Gift-stack-blok-spec

- Kop (TT Ramillas PNG): "4 gifts with your order".
- Vier tegels: desktop 4 naast elkaar (elk ~125 px breed) in compact gebruik, of 2x2 in de uitgebreide versie; mobiel altijd 2x2. Gelijke hoogte volgens D3.
- Per tegel: icoon 40 px · titel Inter SemiBold 14 px · regel 12 px · waarde in brick.
  1. [truck] "Free shipping" · "$15 value"
  2. [book] "Plastic-Free Home e-book" · "$30 value"
  3. [gift-box] "Mystery gift in the box" · "$25 value"
  4. [water-drop-filter] "Chance to win a PFAS water filter" · "$450 value, drawn weekly"
- Totaalregel eronder, 14 px: "Worth $70 in gifts, plus a chance to win a $450 PFAS water filter. Nothing to add: it all comes with your order."
- Altijd "filter", altijd "win/chance to win", nooit "free filter".
- Waardes en "drawn weekly / five winners" eerst laten bevestigen door Floris.
- Positie: direct onder de eerste knop (checkout, cart, browse) of direct onder het aanbodblok (welcome, winback). In P1 boven de timeline.

### D5. Aanbodblok-spec

- Achtergrond espresso #321E1D (zoals W1-A en W5, die zijn goed), padding 28 px, gecentreerd.
- Eyebrow Inter 11 px wit 70 procent, 2 px letterspatiëring: "YOUR WELCOME OFFER" / "YOUR THANK-YOU CODE" / "YOUR CODE".
- Kop TT Ramillas PNG: "10% on top of the sale".
- Codevak: gestippelde rand wit, code Inter SemiBold 32 px, 6 px letterspatiëring. Live tekst (kopieerbaar), geen afbeelding.
- Regel 14 px: "Applied automatically with the button. Or enter it at checkout." Plus voorwaarden één regel: "One code per order. Not valid on subscriptions."
- Bij een echte deadline: [clock] "Expires {{ datum }} at 23:59 ET" in brick op crème-label.
- Knop wit op espresso, volle breedte binnen het blok op mobiel, tekst per flow (D6).
- Compacte variant (checkout/cart): één regel in de cart-kaart: [tag-percent] "10% off with HI10, applied at checkout".

### D6. CTA-regels

- **Formaat:** desktop minimaal 320 px breed, 56 px hoog; mobiel 100 procent breed (min 48 px hoog). Inter SemiBold 16 px, 1,5 px letterspatiëring, hoofdletters. Brick #AC3B19 met witte tekst (contrast ongeveer 6:1, voldoet aan AA). Bulletproof (VML voor Outlook), hele vlak klikbaar.
- **Wording per flow** (eerste persoon, voordeel erin):
  - Checkout: "Complete my order" (C3-P primair "Upgrade to the 6-piece set", secundair tekstlink "Keep my one pan and check out").
  - Cart: "Finish my order".
  - Browse: "Get 10% off this pan" (met unieke code: "Claim my 15%").
  - Welcome: "Claim my 10% + gifts" (W1-B: "Use my gift card"; W4: "Shop the Pan Pro with 10%").
  - Post-purchase: P1 "Download your e-book", P2 "Watch the chef video", P3 "Add the lid, 10% off" / "Get the Pan Pro, 10% off".
  - Winback: "Shop with my 10%" (R2: "Shop up to 50% off").
- **Herhaling:** precies 3 keer dezelfde primaire knop: onder de hero (of onder het cart-blok), na het aanbod/gift-blok of halverwege, en onderaan. Secundaire acties als tekstlink, nooit als tweede gelijke knop.
- **Links:** checkout naar `responsive_checkout_url` plus `discount=<code>` (testen); cart, browse, welcome, winback via `/discount/<code>?redirect=<pad>`. Nooit een knop met "HI10" erin die naar een pagina zonder de korting gaat (nu B2-clicked).
- **Hero-afbeelding** linkt naar dezelfde URL als de primaire knop (is nu al zo).

### D7. Urgentieregels

- Alleen echte deadlines. Geen "final call", "last chance", "ends soon" of countdown zonder een datum die technisch afdwingbaar is. "Last reminder" (dit is de laatste mail) mag, want dat is waar.
- Niet: "reserved", "your cart expires", "only X left", tenzij Shopify dat echt doet.
- **Echte deadlines maken:**
  1. **Unieke, verlopende codes.** Klaviyo unieke kortingscodes (Shopify-integratie, coupon met "expires X days after assignment") in de mail via de coupon-tag. Per profiel een code, geldig 48 tot 72 uur. Toepassen in B2-clicked, C4, K3, R2-vip, en als welkomstcode (zie 2). De deadline in de mail is dan per definitie waar. Datum tonen als vaste tekst berekend bij verzending (bijv. "{{ 'now'|date_add:3|date:'F j' }}" of de Klaviyo-equivalent; eerst testen in een preview).
  2. **Welkomstcode per profiel, 10 dagen geldig** vanaf inschrijving. Dan klopt "Your 10% ends {{ datum }}" in W5. HI10 blijft de publieke code voor campagnes. Beslissing Floris (DECISIONS: offer mail 1 nog niet definitief).
  3. **Wekelijkse trekking** van de PFAS-filter: als die echt elke zondag sluit, mag "This week's draw closes Sunday" in C4, K3 en W5. Laten bevestigen.
  4. **Einddatum oktober-actie / BFCM**: zodra Floris die geeft, in R2 en de gift-stack ("Gifts until {{ datum }}"). Tot die tijd geen datum (DECISIONS).
- Countdown-GIF alleen bij een vaste einddatum die voor iedereen gelijk is (campagne-einddatum), niet bij per-profiel-codes.
- Urgentie in de flow-toon: kalm en feitelijk ("Your code expires Friday at 23:59 ET."), geen uitroeptekens (PLAYBOOK 1).

### D8. Overige systeemregels

- Levertijd nergens in marketing-flows. In post-purchase vervangen door "tracking link by email". Levertijden blijven in Shopify-transactiemails en op de site.
- "PFAS water filter" overal; "Light Labs report no. 25895"; "100,000+ happy customers"; "75-year warranty"; "30-day returns". Geen "lifetime", "100-day trial" of "30,000".
- Compare-at-prijzen voor verzending checken tegen Shopify (Pan Pro $439, sheets $60, board $130, Set Pro $870, 12-pcs $1,186).
- Product- en gift-beelden: in tabelcellen `valign="top"` zodat er geen wit vlak boven het beeld valt (P3-accessory, P3-pan, P3-set).
- Hero-foto's: een register per flowpad bijhouden zodat iemand die welcome, dan checkout krijgt niet twee keer dezelfde foto ziet.
- Mobiele lengte: doel maximaal 3.200 px op 390 px breed voor verkoopmails (nu tot 5.206 px). Drie-koloms productrijen naar twee.
- Beelden met ingebakken tekst (water-test-frame) vervangen door frames zonder tekst.
- Footer is 530 px; acceptabel, maar de navigatie-items zijn klikdoelen die concurreren met de knop. Overweeg in checkout en cart een korte footer zonder de vier navigatieregels.

---

## Deel E. Bouwvolgorde (voorstel)

1. `make_hero.py`: groter label en subregel, `offer`-balk, 4:3-variant.
2. Partials: ICON-FEITEN-rij, gift-stack-blok, aanbodblok, reviewkaarten (gelijke hoogte), cart-blok met HI10-regel. Iconen tekenen en uploaden.
3. Checkout en cart herbouwen (hoogste RPR, grootste winst).
4. Browse met aanbod en unieke B2-code.
5. Welcome W1-A/B, W4, W5.
6. Winback en P3 met bedankcode.
7. P1/P2: levertijd eruit, gifts met iconen.
8. Open beslissingen voor Floris: unieke codes (welkom 10 dagen, B2/C4/K3 48 tot 72 uur, VIP 15 procent), 4:3-hero, compare-at Pan Pro, gift-waardes, trekking-dag, filter versus purifier.
