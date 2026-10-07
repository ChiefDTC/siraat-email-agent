# Email Love benchmarks · e-commerce e-mail UX voor Siraat

Datum: 7 oktober 2026. Bron: Email Love MCP (search_emails, search_brands, list_journeys, get_journey, fetch_email, get_email_html) plus de volledige screenshots van elke genoemde mail (r2-previews, in delen bekeken op 700 px breed). Budget: 16 fetch_email en 2 get_email_html gebruikt (18 van 40).

Context Siraat: premium titanium cookware, AOV $150 tot $250, altijd sale tot 50 procent plus 4 gratis gifts (free shipping $15, Plastic-Free Home E-Book $30, mystery gift $25, wekelijkse kans op een PFAS-waterzuiveraar van $450), welkomstcode HI10 = 10 procent extra bovenop de sale. Claims volgens `content/facts/summary.md`: "75-year warranty", "Free 30-day returns", "Free shipping on all orders", "100K+ happy customers", "with a pure titanium cooking surface" plus "No coatings". Concurrenten nooit bij naam noemen in Siraat-copy; "non-stick" niet als kop.

Belangrijke beperking: Email Love journeys tonen per merk welke mails in welke fase vallen, maar geen wachttijden of flow-triggers. Waar ik timing noem is die gebaseerd op echte verzenddatums (HexClad, Our Place) of uitdrukkelijk als aanname gemarkeerd.

Opvallend: Our Place verkoopt een **Titanium Pro**-lijn ("patented no-coating, non-toxic Titanium NoCo interior") en mailt daar sinds december 2025 met dezelfde mechaniek als Siraat: sale plus "Extra 10% off with code SAVE10PRO". Dat is de meest directe benchmark in de hele bibliotheek.

---

## 1. Offer in de hero, boven de vouw

### Voorbeelden

1. **Our Place · "Take an Extra 10% Off Titanium 🔥"** (id 856033, 28 dec 2025, https://emaillove.com/email-inspiration-from-our-place-221)
   - Rode codebalk helemaal bovenaan: "EXTRA 10% OFF TITANIUM PRO COLLECTION" met rechts een donkere pill "USE CODE SAVE10PRO". De code staat dus nog boven het logo.
   - Kop met gemarkeerd bedrag: "Save Over $245*" in een donker blok, daarna "on the Last Cookware Set You'll Ever Need".
   - In de productfoto drie stickers: "SELLING FAST" (schuin, donkerrood), "HOLIDAY SALE" (groene cirkel) en "Extra 10% off: Code SAVE10PRO" (groen label). De code staat daardoor twee keer boven de vouw.
   - Asterisk-uitleg direct onder de knop: "*with bundle + sale savings".
   - Brede pill-knop (ongeveer 85 procent van de breedte) "SHOP NOW".
2. **Our Place · "Tick, Tick, Cyber Monday"** (id 766129, 1 dec 2025, https://emaillove.com/email-inspiration-from-our-place-190)
   - Eerste element van de mail is een live countdown (MotionMail-GIF, alt "motionmailapp.com"): DAYS / HOURS / MINUTES / SECONDS, serif cijfers op crème. Daaronder de codebalk "EXTRA 10% OFF TITANIUM PRO COLLECTION WITH CODE: SAVE10PRO".
   - Ronde badge in de hero: "BIGGEST DISCOUNT IS 46%".
   - Bodytekst als urgentie: "Only 24 hours left to get our best deals of the year and $30 bonus points when you spend $300 or more."
   - HTML: volledig gesneden beelden met de complete tekst in alt-attributen (Klaviyo).
3. **Great Jones · "30% OFF SITEWIDE"** (id 1759757, 9 sep 2026, https://emaillove.com/email-inspiration-from-great-jones-143)
   - Bovenbalk "Sale extended: 30% off sitewide!"
   - Kop "Labor Day Sale", product, dan "30% off everything" groot.
   - Codezin als live tekst met code in accentkleur: "Use code LABORDAY30 at checkout."
   - Expires-regel cursief onder de knop: "Offer ends September 14, 11:59pm PT. Exclusions apply and offers cannot be combined."
4. **Huel · "$15 off? 💸"** (welkomstreeks, id 22069, https://emaillove.com/huel-email-design-25)
   - Hero "Easy money..." met fles; daaronder "Hey there. Fancy $15 off your first Huel order?"
   - Apart blok "⬇️ How to claim ⬇️" met **unieke code** "PAYDAYJUNE-92V0ZF", twee genummerde stappen (in cart, dan in het codeveld), tweede knop "Get $15 off".
   - Kleine regels: minimum $66 en "only valid until 11:59 pm PT on July 31st 2023".
5. **Care.com · "Still thinking about it? Here's your 20% off"** (browse, id 1619484, https://emaillove.com/email-inspiration-from-care-com-152)
   - "20" in een enorme cijferkop met "% OFF memberships*" ernaast, knop "Claim special offer", daaronder "Use code: TRYCARE20" en "Expires: 08/04/26 at 11:59 PM CDT".

### Aanbeveling voor Siraat

Bouw elke sale-mail met een vaste bovenstructuur: (1) codebalk boven het logo, (2) hero met het hoogste getal en een sticker, (3) knop, (4) expires-regel. Concreet: balk "EXTRA 10% OFF ON TOP OF THE SALE · CODE HI10" (donkere pill rond HI10, zoals SAVE10PRO). Hero-kop "Up to 50% off + 4 free gifts", sticker in de foto "Extra 10% off: code HI10" en tweede sticker "Ships free worldwide". Onder de knop: "Code HI10 works on top of sale prices. Ends Sunday 11:59 PM ET." Zet de code ook als live tekst onder de hero (niet alleen in het beeld), zodat Gmail met beelden uit en dark mode hem tonen. In flows (welkom, checkout) een unieke Klaviyo-code in de stijl van Huel met "How to claim" in twee stappen; in campagnes de vaste code. Een live countdown (MotionMail of Sendtric) alleen in de laatste 24 uur van een echte deadline, als eerste element zoals Our Place. Let op: HI10 in de welkomstflow wacht nog op beslissing 5 (welcome-v3 spec stelt een $25 gift card voor).

---

## 2. Iconenrijen en benefit-strips

### Voorbeelden

1. **Great Jones · "Don't Miss Your Free Dutch Baby"** (id 1339673, https://emaillove.com/email-inspiration-from-great-jones-139)
   - Kader "Make your kitchen your happy place" met drie lijniconen in drie merkkleuren (pan, eieren, ovenschaal), ongeveer 40 px, telkens een kop plus een kleine tweede regel: "Free Shipping / on orders $100+", "Nonstick & Nontoxic / for stress-free cooking", "30-Day Trial / with free returns". Twee regels per item is het patroon: belofte plus voorwaarde.
2. **HexClad · "Why folks love us"** (id 1119597, https://emaillove.com/email-inspiration-from-hexclad-cookware-2)
   - Eén smalle regel onderaan op zwart: klein lijnicoon plus caps-label "LIFETIME WARRANTY", "FREE SHIPPING", "30-DAY RETURN GUARANTEE". Icoon ongeveer 20 px, links van de tekst, alles op één regel.
3. **Quince · "Last call for Cashmere Reversible Two Tone Throw"** (cart, id 9860, https://emaillove.com/quince-email-design)
   - Twee niveaus: bovenaan drie kolommen met dunne lijniconen (ster, dollar, persoon) en een zin elk ("The savings are waiting. Just fill in your details."), verticale scheidingslijnen. Lager een donkere band met drie iconen plus caps-kop en uitleg: "SUSTAINABLE LUXURY FOR ALL", "FREE SHIPPING & 365-DAY RETURNS", "$20 REFERRAL REWARD".
4. **Fellow · "Still brewing over your decision?"** (cart, id 580054, https://emaillove.com/email-inspiration-from-fellow-51)
   - Vier dikke zwarte iconen (ongeveer 45 px) met een merkeigen detail (warranty-icoon is het Fellow-logo, support is hun waterkoker): "Free Shipping on orders $75+*", "30 Day Returns", "Extended warranty with product registration", "Dedicated Support Team".
5. **Our Place · footer in "Titanium Price Drop 👀"** (id 1291384, https://emaillove.com/email-inspiration-from-our-place-341)
   - Vijf iconen in een rij, één woord of twee per item: "Free Returns" (pijl met "100 day trial" erin), "Text Exclusives", "Rewards", "Without PFAS" (doorgestreept PFAS), "Get $20".

### Aanbeveling voor Siraat

Eén vaste strip van vier items, live tekst onder 40 px lijniconen in de merkkleur, twee regels per item (kop plus voorwaarde), dezelfde in elke mail zodat hij herkenbaar wordt. Copy: "Free shipping / on every order, worldwide", "Free 30-day returns / on unused items", "75-year warranty / against defects", "No coatings / pure titanium surface". In sale-mails een tweede, smalle variant direct onder de hero (HexClad-stijl, één regel, 11 tot 12 px caps): "FREE SHIPPING · FREE 30-DAY RETURNS · 75-YEAR WARRANTY". Het PFAS-icoon van Our Place (doorgestreept woord) is een goed idee voor "No PFAS", maar teken een eigen versie. Geen "Lifetime warranty" of "100-day trial", die zijn vervallen.

---

## 3. Gift-with-purchase stacks

### Voorbeelden

1. **Estée Lauder · "Your Pick 🎁 Choose Your Free 8-Piece Gift, with your purchase."** (id 1832464, 2 okt 2026, https://emaillove.com/email-inspiration-from-estee-lauder-433)
   - Drie oplopende drempels, elk met eigen kop en knop, en de **cumulatieve waarde** vetgedrukt: "Free 6-Piece Gift / Up to a $168 Value. Choose yours with any $50 purchase", "Add a Free Full-Size Eye Cream / Yours with $90 purchase. Both gifts together, up to a $246 value", "Choose a Free Full-Size Moisturizer / Yours with $140 purchase. All gifts together, up to a $327 value." Daarna "Shop Bestsellers to Unlock Your Gift".
2. **Solo Stove · "Summit Holiday Special! 30% off + Free gift"** (id 782430, 5 dec 2025, https://emaillove.com/email-inspiration-from-solo-stove-142)
   - Korting en gift visueel gescheiden: rood schild "LIMITED TIME 30% OFF" in de foto, daaronder een aparte rode band met foto's van het gift aan beide kanten: "+ FREE ROASTING STICKS / SET OF 4 STICKS WITH SUMMIT FIRE PIT PURCHASES / USE CODE: TOASTY". Goudbalk "ENDS SOON!" erboven.
3. **Solo Stove · "Don't miss out on this FREE pizza oven gift"** (id 206604, https://emaillove.com/email-inspiration-from-solo-stove-29)
   - Het gift staat in de hero in een rode cirkel: "FREE Infrared Thermometer", met een hand die het gift vasthoudt voor het product. Datum in de kop: "Free Memorial Day Gift / Now through 05/18", code "HOTPIZZA" in rood.
4. **Omaha Steaks · "Sitewide savings + FREE GIFT on $129+."** (id 1843073, https://emaillove.com/email-inspiration-from-omaha-steaks-319)
   - Rij van drie ronde productfoto's met "OR" ertussen en exacte hoeveelheden: "8 FREE Omaha Steaks Smash Burgers, 4 FREE Boneless Pork Chops, or 4 FREE Caramel Apple Tartlets on $129+".
5. **Great Jones · "Don't Miss Your Free Dutch Baby"** en **GreenPan · "🦃 SAVE UP TO 60%: Get Feast-Ready"** (id 1835034)
   - Great Jones: "FREE" in vier kleuren als kop, gift en hoofdproduct samen gefotografeerd. GreenPan: gift met handgeschreven pijltjes en labels ("Made for Nonstick", "Durable & long-lasting") en "FREE with any purchase over $450".

### Aanbeveling voor Siraat

Toon de vier gifts als vier gelijke kaarten (2x2 op mobiel), elk met een foto of illustratie, naam en doorgestreepte waarde, en daarboven één optelsom zoals Estée Lauder: kop "4 free gifts with your pan", subkop "$70 in gifts, yours free". Kaarten: "Free worldwide shipping · $15 value", "Plastic-Free Home E-Book · $30 value", "Mystery kitchen gift · $25 value", "A weekly chance to win a PFAS water purifier · $450 value". Tel de $450 niet op in de $70 (het is een kans, geen gift) en zet onder de kaart "No purchase necessary. See terms." (laten checken; een winactie zonder koopplicht vraagt die regel). Gebruik het Solo Stove-patroon: korting en gifts in twee verschillende vlakken, nooit in één zin gepropt. Voor de mystery gift een ingepakte doos met vraagteken (Omaha-achtige ronde foto) in plaats van een leeg vak.

---

## 4. Cart- en checkout-abandonment

### Voorbeelden

1. **Quince · "Last call for Cashmere Reversible Two Tone Throw"** (id 9860)
   - Volgorde: "RETURN TO YOUR CART / COMPLETE YOUR ORDER", drie benefit-kolommen, "Don't miss out on your cart. Our limited run products sell quick.", pill-knop "RETURN TO CART", pas daarna "WHAT'S IN YOUR CART" met één grote productfoto (ongeveer 35 procent van de breedte, gecentreerd), prijs vet, naam eronder. Knop staat dus boven de cart.
2. **Quince · "$20 off expires soon"** (id 9914, https://emaillove.com/quince-email-design-2)
   - Eskalatiemail: "TIME IS RUNNING OUT / $20 OFF EXPIRES SOON", "your offer for $20 off your order of $200 or more expires in a few days. Activate by clicking below (discount applies automatically at checkout)." Geen code nodig: korting zit in de link.
3. **True Classic · "Your second chance at style!"** (id 739098, 22 nov 2025, https://emaillove.com/email-inspiration-from-true-classic-223)
   - Bovenbalk "SAVE UP TO 50% OFF →". Kop "LIKE ALL THE PREMIUM BRANDS / But half the price." Cart-blok: foto links (ongeveer 45 procent breed), rechts naam en "Price: $114.99". Daarna risicowegnemers: "NOT SURE? TRY BEFORE YOU BUY", "100 DAY GUARANTEE", dan twee halve knoppen naast elkaar "Keep Shopping" en "Read FAQ's", dan UGC-strip "200k 5-Star Reviews / Trusted By 4 Mil+".
4. **The North Face · "You left something in your cart."** (id 1795894, https://emaillove.com/email-inspiration-from-the-north-face-294)
   - Kop "In your cart today. In the outdoors tomorrow." Knop "Head Back to Cart" vóór en ná een productfoto op bijna volle breedte. Bovenbalk met de lopende sale.
5. **DIFF Eyewear · "Hi Friend, You left something in your cart"** (id 1836157) en **Huel · "Hueligan, take another look."** (id 7954)
   - DIFF: unieke code al in de preheaderzone ("Use Code FREESHIPQ8JN4LBW for Free Shipping!"), knop "Complete Checkout". Huel: geen korting, wel service ("No question is too big or too small, just drop us a message at support@huel.com") en "we've saved the items you were looking at".

### Aanbeveling voor Siraat

Knop boven de cart, cart groot, besparing expliciet. Volgorde mail 1: kop "Your pan is still waiting", subregel "Prices in your cart are sale prices. Code HI10 takes another 10% off.", knop "Return to my cart" (volle breedte, 52 px hoog), dan het Klaviyo-cartblok met foto op minstens 50 procent breedte, doorgestreepte compare-at prijs naast de sale-prijs en een regel "You save $305" (dynamisch: compare-at min prijs), daarna de 4-gifts-kaarten "Included with your order", daarna de iconenstrip en één echte review. Mail 2 (+1 dag): risico wegnemen zoals True Classic ("Not sure? Free 30-day returns. 75-year warranty."), plus support-zin zoals Huel ("Questions about induction or care? Reply to this email, a real person answers."). Mail 3 (+2 dagen): Quince-eskalatie "Your extra 10% expires tonight" met een auto-apply link in plaats van een code. Bovenbalk in alle drie: "UP TO 50% OFF + 4 FREE GIFTS". Zie ook `research/2026-10-07-checkout-abandonment.md` voor de huidige flowproblemen.

---

## 5. Browse-abandonment met offer en urgentie

### Voorbeelden

1. **Care.com · "Still thinking about it? Here's your 20% off"** (id 1619484)
   - Het getal is de hero ("20" van bijna 40 procent van de schermhoogte), code als live tekst, vervaldatum met tijdzone. Pas daarna de inhoud ("84% of family caregivers...").
2. **Brooklinen · "You left these internet favorites behind..."** (id 1556256, 7 jul 2026, https://emaillove.com/email-inspiration-from-brooklinen-305)
   - "Hey You, Where'd You Go? / We've Got Savings For You!" met witte knop "Claim Offer", daaronder "your exclusive deal before it's too late" en een 2x2-grid met "Selling fast"-badge op de eerste kaart.
3. **KURU · "Still interested in these?"** (id 1601450, https://emaillove.com/email-inspiration-from-kuru-footwear-230)
   - Geen korting maar sterke review-urgentie: bovenbalk "Free US Shipping | 91-Day Returns & Exchanges" (herhaald boven de footer), groene reviewkaart "Walk a mile in someone else's shoes." met twee reviews en sterren, knop "Take A Second Look".
4. **Fellow · "Still brewing over your decision?"** (id 580054)
   - Minimal: "Hey there, we noticed you had a close encounter with this...", product links, naam als link rechts, outline-knop "SHOP NOW", dan de iconenrij. Geen offer: past bij een merk zonder sale.
5. **Graza · "Your kitchen deserves MICHELIN STAR EVOO"** (id 9169, abandonment, https://emaillove.com/graza-email-design-9)
   - "Checking Us Out? 👀", grap "I know you can't help it, we look pretty dang good", dan een lange review van een scepticus ("I was super skeptical and just thought it was millennial marketing").

### Aanbeveling voor Siraat

Browse krijgt geen extra korting bovenop wat iedereen al ziet, maar maakt de bestaande sale en HI10 zichtbaar plus een deadline. Mail 1 (2 uur na view): kop "Still thinking about the pan?", productkaart van het bekeken product met sale-prijs en doorgestreepte prijs, knop "See it again", dan een scepticus-review in Graza-stijl (Siraat heeft "Cleanup is 30 seconds", Thomas H.). Mail 2 (+1 dag, alleen zonder cart): Care.com-hero met het getal "10%" groot en "extra on top of the sale", regel "Use code HI10 · Ends Sunday 11:59 PM ET", knop "Claim my extra 10%". Brooklinen-badge "Selling fast" alleen op producten die echt laag op voorraad zijn.

---

## 6. Review- en social-proof-modules

### Voorbeelden

1. **Our Place · "“Everything just cooks better.”"** (id 1276944, 1 mei 2026, https://emaillove.com/email-inspiration-from-our-place-338)
   - Subject is een klantquote. Kop "NO (SUGAR) COATING NECESSARY", dan "It sounds almost too good to be true, but here's what happened when customers put it to the test." Drie **even hoge kaarten** met dunne zwarte rand en ronde hoeken, zigzag (quote links, foto rechts, dan omgekeerd), vetgedrukte kernzin in de quote ("I will never use another pan again"), naam met streepje ervoor ("Mark B."). Foto's tonen telkens het bewijs (ei glijdt uit de pan).
2. **KURU · "Still interested in these?"** (id 1601450)
   - Donkergroene kaart met grote aanhalingstekens, reviewtekst, naam, vijf lichtgele sterren onder de naam, scheidingslijn tussen twee reviews, witte knop in de kaart.
3. **True Classic · "Your second chance at style!"** (id 739098)
   - UGC-strip: vier staande klantfoto's naast elkaar, links boven "200k 5-Star Reviews", rechts boven "Trusted By 4 Mil+", onder "Follow Us / @trueclassic".
4. **HexClad · "Why folks love us"** (id 1119597)
   - Telblok onderaan: vijf goudkleurige sterren, "50,000+" in serif goud, "5-Star Reviews" in wit serif. Geen individuele review, alleen het volume.
5. **Brooklinen · "100K 5-Star Reviews Don't Lie"** (id 1141635, https://emaillove.com/email-inspiration-from-brooklinen-248) en **Caraway · "The Reviews Are In ✍️"** (id 7543)
   - Brooklinen: telling in de subject en de body ("150,000 5-star reviewers"), Wirecutter-badge op de productfoto's. Caraway: kaart met foto links en quote rechts, naam in caps "GERALD M.", en per review een eigen productknop ("Shop Squareware →").

### Aanbeveling voor Siraat

Standaardmodule: kop "100K+ cooks made the switch", sterrenrij plus Trustpilot-score als live tekst, dan drie even hoge kaarten in Our Place-zigzag (vaste hoogte, ronde hoeken 16 px, dunne rand), elke quote met één vetgedrukte kernzin en een foto die het bewijs laat zien: ei dat glijdt, pan in de vaatwasser, metalen spatel op het oppervlak. Voorbeeldquote met toegestane claim: "Cleanup is 30 seconds." (Thomas H.). Onder de kaarten een UGC-strip van vier klantfoto's (True Classic) met "@siraatskitchen". In campagnes (LOUD register) mag het telblok van HexClad ("100K+ happy customers" groot in serif); in flows de kaarten. Alleen echte reviews met naam en initiaal, nooit herschreven.

---

## 7. CTA-ontwerp

### Voorbeelden

1. **Our Place** (alle bekeken mails): brede pill-knoppen, ongeveer 85 procent van de breedte, ongeveer 50 px hoog, caps 14 tot 16 px, kleur uit de hero ("SHOP NOW", "SHOP THE COLLECTION", "SHOP CYBER MONDAY DEALS"). Secundaire link als onderstreepte caps met pijl: "SHOP TITANIUM PRO →". Knopkopie benoemt soms het product: "SHOP TITANIUM ALWAYS PAN® PRO".
2. **HexClad · "Welcome to the HexClad family."** (id 87397, https://emaillove.com/email-inspiration-from-hexclad-cookware): rode rechthoekige knop "Shop Now" in de hero met kleine regel "DETAILS BELOW" eronder; per product in "MOST POPULAR" een eigen volle-breedte rode knop "Buy Now" direct onder de productkaart. In de nieuwere mails outline-pill op zwart ("Shop Now" vier keer per mail).
3. **The North Face** (id 1795894): dezelfde knop "Head Back to Cart" twee keer, boven en onder de productfoto: het sticky-patroon in e-mail (je ziet altijd een knop binnen één scroll).
4. **True Classic** (id 739098): knoppen met pijl-icoon links ("→ Keep Looking", "→ Give It A Try"), en een duo-rij "Keep Shopping" plus "Read FAQ's" voor wie nog twijfelt.
5. **Bombas · "These Compression Socks Live Up to the Hype"** (id 457711, https://emaillove.com/email-inspiration-from-bombas-105): twee gelijke zwarte knoppen naast elkaar in de hero ("Shop Women" / "Shop Men"), herhaald halverwege. Brooklinen gebruikt "Claim Offer" als primaire knop en "Shop Now" als onderstreepte tekstlink: duidelijke hiërarchie.

### Aanbeveling voor Siraat

Eén primaire knopstijl: volle breedte op mobiel (minstens 88 procent), 52 px hoog, 16 px caps of zinskapitalen, live HTML-knop (geen beeld), kleur met contrast 4,5:1 in licht en donker. Werkwoord plus uitkomst, nooit alleen "Shop now": hero "Claim 50% off + 4 gifts", cart "Return to my cart", product "Get the pan", browse "Claim my extra 10%", review "Leave a review". Herhaal de primaire knop elke ongeveer 600 px scroll (na hero, na gifts, na reviews), altijd met dezelfde tekst. Secundaire acties als onderstreepte tekstlink met pijl: "Compare sizes →", "Read the care guide →". Onder de eerste knop een microregel zoals HexClad "DETAILS BELOW" of Our Place "*with bundle + sale savings": voor Siraat "Code HI10 applies at checkout".

---

## 8. Productuitleg ("why this pan")

### Voorbeelden

1. **Our Place · "Our Titanium Pro Is Stainless Steel"** (id 1491506, 17 jun 2026, https://emaillove.com/email-inspiration-from-our-place-373)
   - Kop "The Stainless Steel Evolution", sticker "SECRETLY ON SALE RIGHT NOW". Probleem-oplossing in twee zinnen ("We love stainless steel cookware for the way it sears... but not the part where dinner gets stuck"). Dan **gelaagde uitleg**: "WE LAYERED THREE MATERIALS TOGETHER, GIVING EACH ONE A SPECIFIC JOB", drie kaarten met macrofoto links en een blauwe kopbalk rechts: "EXTERIOR / Heavy-duty stainless steel...", "CORE / A responsive aluminum layer...", "INTERIOR / A patented, non-toxic Titanium NoCo® (no-coating) surface...". Knop "SHOP TITANIUM ALWAYS PAN® PRO".
2. **HexClad · "Why folks love us"** (id 1119597)
   - "CLASS THAT LASTS", dan "LET US EXPLAIN:", dan een anatomie met de pan als halve cirkel rechts in beeld en gelabelde lagen links met gouden scheidingslijnen: "Peaks / stainless steel... searing power", "Valleys / Scratch-resistant nonstick valleys...", "Easy Cleanup / ... dishwasher". 
3. **HexClad · "Welcome to the HexClad family."** (id 87397)
   - Featurelijst "WHY YOU'LL LOVE HEXCLAD": acht cursieve regels met lijnen die naar de rand van een pan lopen ("Induction-ready", "Metal utensil safe", "Oven safe up to 500F"...). Daarna een **tabel** voor het second-purchase-programma: "FIRST PURCHASE MINIMUM $250 / $450 / $750" tegenover "SECOND PURCHASE CREDIT EARNED $25 / $50 / $75".
4. **Le Creuset · "Signature 9-Piece Cookware Set: $580 Off"** (id 1798586, 22 sep 2026, https://emaillove.com/email-inspiration-from-le-creuset-69)
   - Productuitleg in één zin per set plus prijsanker "$1,244.99 (Was $1,825)", dan afwisselende kaarten (foto links of rechts) per set met dezelfde Was-notatie en outline-knop "BUY NOW". Een vergelijking via prijs en inhoud.
5. **Huel · welkomstreeks** ("Why Huel is not a meal replacement", id 22051; "Which Huel product is right for me?", id 22050)
   - Mythe ontkrachten in een aparte mail, en een quiz-achtige keuzehulp om te kiezen tussen producten.

### Aanbeveling voor Siraat

Maak een vaste anatomie-module in de Our Place-vorm (het formaat werkt duidelijk voor titanium): kop "Three layers. One job each.", drie kaarten met macrofoto en kopbalk: "COOKING SURFACE / Pure titanium. No coatings. Nothing to wear off.", "CORE / An aluminum core that heats fast and evenly.", "BASE / Works on all cooktops, including induction." (3-ply alleen voor de Pan Pro-lijn; laagdikte in mm pas na bewijs). Daarna een eerlijke vergelijkingstabel zonder merknamen, kolommen "Coated pans", "Stainless steel", "Siraat titanium", rijen "Coating that wears off", "Food slides right off", "Dishwasher safe", "Metal utensils", "Warranty" (laatste cel "75 years"). Geen "non-stick" als kop: gebruik "Food slides right off" of "natural release". Een korte GIF (ei glijdt over het gehamerde oppervlak, 2 seconden, onder 1 MB) als hero van deze module. De HexClad-prijstabel is een goed format voor de "Three ways to start"-tiers (onder $80, de pan $134, de set).

---

## Drie flowsequenties

### A. Welkom · HexClad (sent dates uit Email Love, 2025 en 2026)

| # | Subject | Verzonden | Wat erin zit | Offer |
| --- | --- | --- | --- | --- |
| 1 | "Welcome to the HexClad family." (id 87397) | 5 mrt 2025 | Hero "GET UP TO $75 back on your second purchase", knop plus "DETAILS BELOW", wat ons anders maakt, 8 features, tiertabel, "MOST POPULAR" met Buy Now per set | Geen korting, wel credit op 2e aankoop ($25/$50/$75 bij $250/$450/$750) |
| 2 | "Why folks love us" (id 1119597) | 3 apr 2026, 21:35 | "CLASS THAT LASTS", anatomie peaks/valleys, kaart "GET 30% OFF OUR BEST-SELLING SET NOW", tiertabel, referral-balk, categorieën, 50,000+ reviews, trust-strip | 30% op de set, plus credit-programma |
| 3 | "Gordon Ramsay ❤️‍🔥 these pans" (id 1161389, preheader "Here's why") | 6 apr 2026 (+3 dagen) | Autoriteit: "Good Enough For Gordon", quote "Buy HexClad once, and you'll use it for life.", zelfde 30%-kaart | 30% op de set |
| 4 | "A letter from HexClad's founder 💌" (id 1187123) | 11 apr 2026 (+8 dagen) | Oprichter (Danny Winer) in de keuken, persoonlijke brief, belofte | Herhaling offer onderaan |

Patroon: de offer staat vanaf mail 2 in **elke** mail als vast kaartje halverwege (zelfde beeld, zelfde "30% OFF"), terwijl het verhaal per mail wisselt: product, autoriteit, oprichter. Het credit-programma stuurt de AOV omhoog (drempels op $250, $450, $750). De mails 2 tot 4 lijken één reeks (3 april tot 11 april); dat het om dezelfde trigger gaat is mijn aanname.

### B. Welkom en browse · Huel (journey "Pre-Purchase Welcome", 8 mails, plus "Abandonment")

Volgorde op basis van inhoud (Email Love geeft geen wachttijden): "Welcome to the Huel family" (id 4715) · "Why Huel is not a meal replacement" (22051, mythe) · "Which Huel product is right for me?" (22050, keuzehulp) · "When to Huel ⏰" (22073, gebruiksmomenten) · "Tips from the Huel experts" (22074) · "$15 off? 💸" (22069, unieke code, minimum $66, harde vervaldatum) · "More Huel for your money 💰" (22067, bundels en abonnement) · abandonment "Hueligan, take another look." (7954, service in plaats van korting).

Patroon: vier tot vijf educatiemails eerst, de offer pas laat en dan als unieke code met vervaldatum, gevolgd door een value-mail over bundels. Escalatie loopt via vorm (generiek, dan uniek met deadline), niet via steeds hogere korting.

### C. Post-purchase · Graza (journey "Post-Purchase", 4 mails)

"Hello again to our fave customer!!" (id 20148, cross-sell en gift-ideeën, "Mo EVOO. Mo money") · "How's that EVOO tasting??" (20149, reviewverzoek met kop "We Think We're 5 Olives / But what do you think??", vijf getekende olijven als sterren, knop "Leave A Review", daarna recepten met UGC-foto's) · "SQUEEZE, REFILL, REPEAT" (20102, refill-reminder met stappen) · "WE'LL TRADE YA" (16023, survey met beloning). Abandonment ervoor: "Your kitchen deserves MICHELIN STAR EVOO" (9169), "Let's pick up where we left off" (20145), "WHY IS IT SO GOOD?!?" (20146).

Patroon: geen korting in post-purchase; waarde komt uit gebruik (recepten), het reviewverzoek is merkeigen getekend, de refill-mail is het enige verkoopmoment.

### Bonus · campagne-escalatie Our Place End of Summer Sale (echte verzenddatums)

26 aug "Tomorrow, a Sale" · 27 aug 04:14 "End of Summer Sale 🍳" · 27 aug 21:10 "Our Sale Is Live" · 28 aug "Perfectly Sized Savings" · 4 sep "Final Few Sale Favorites" · 5 sep "The End of Summer Sale Shortlist" · 6 sep "End of Summer Sale Ends Soon" · 8 sep "Ends Tomorrow" · 9 sep 04:26 "Sale Ends at Midnight" (hero "LAST CALL" vier keer in vervagend terracotta, "Our biggest discount is 67% off,* and double points end when the sale does") · 9 sep 22:32 "A Few Hours Left". Tien mails in vijftien dagen, twee per dag op launch en op de laatste dag. Voor Siraat met een altijd-sale: gebruik deze cadans alleen rond echte deadlines (einde van de 4-gifts-maand, HI10-verval), anders verliest "ends" zijn kracht.

### Wat Siraat hieruit overneemt

- **Welkom:** mail 1 direct (HI10 of gift card volgens beslissing 5, unieke code, "How to claim" in twee stappen, vervaldatum 7 dagen), mail 2 +1 dag anatomie "Three layers", mail 3 +3 dagen reviews in kaarten, mail 4 +5 dagen oprichter Benjamin en "First orders shipped December 20, 2024", mail 5 +7 dagen "Your code expires tonight" met live countdown. De offer staat vanaf mail 1 als vast kaartje in elke mail (HexClad).
- **Checkout/cart:** 3 mails (1 uur, +1 dag, +2 dagen), escalatie via risico wegnemen en dan deadline, niet via hogere korting (Quince, True Classic).
- **Post-purchase:** geen korting; reviewverzoek 14 dagen na bezorging met merkeigen sterren (Graza), daarna gebruik en zorg, en de vaatwasstrips als refill-moment.

---

## Bronnenlijst (Email Love-id's)

HexClad 87397, 1119597, 1161389, 1187123 · Our Place 856033, 766129, 1758627, 1491506, 1276944, 1291384 (plus sale-reeks 1717477 tot 1760795) · Great Jones 1339673, 1759757 · Le Creuset 1798586 · Solo Stove 782430, 206604 · Estée Lauder 1832464 · Omaha Steaks 1843073 · GreenPan 1835034 · Quince 9860, 9914 · True Classic 739098 · The North Face 1795894 · DIFF 1836157 · Fellow 580054 · Care.com 1619484 · KURU 1601450 · Brooklinen 1141635, 1556256 · Bombas 457711 · Caraway 7543 · Huel 4715, 22051, 22050, 22073, 22074, 22069, 22067, 22068, 7954 · Graza 9169, 20145, 20146, 20148, 20149, 20102, 16023.

Niet gevonden in Email Love: Made In (de slug "made-in" is een Brits handelsmerk), Manscaped-gifts, Hestan, Misen, All-Clad, Ridge, AG1, Oura en Dyson zijn niet doorzocht of leverden niets relevants binnen het budget.
