# UX-ronde 2 · onderzoek stickers, vergelijkingstabellen en callouts

Datum: 7 oktober 2026. Aanleiding: drie referenties van Floris in `refs/` (getande NEW-sticker, vergelijkingstabel roasting pan, "Take a closer look" met vier callouts).

Bronnen: Email Love MCP (10 calls: search en search_emails; de volledige screenshots zijn daarna als openbare r2-beelden bekeken, geen extra MCP-calls), de eerdere benchmark `research/ux-2026-10-07/02-emaillove-benchmarks.md`, Replo `shopify_products_search` (2 calls, roasting pan en 6-delige set actief bevestigd) en `content/assets/index.csv`.

Beperking: Caraway, Material en HexClad leveren in Email Love weinig of geen nieuwe mails op deze zoekwoorden (Caraway 0 treffers op "cookware", HexClad alleen de vier mails uit ronde 1). Our Place, Made In en Great Jones zijn goed vertegenwoordigd. Waar ik HexClad noem, komt het uit ronde 1.

---

## 1. Stickers en badges

### Wat de merken doen

1. **Our Place · "Your New Kitchen Is Over $570 Off"** (id 1753107, 7 sep 2026, https://emaillove.com/email-inspiration-from-our-place-431)
   Hero met set in terracotta. Rechtsboven een ronde, egale terracotta sticker (geen tanden) met serif tekst "Save over $570*", half over de rand van de foto. Lager een tweede banner met een pill met dunne rand: "Biggest Discount: 67% Off*". Asterisk-uitleg onder de knop: "*with bundle and sale savings". Eén sticker per beeld, kleur uit de foto zelf.
2. **Made In · "The Cookware Mistake Almost Everyone Makes"** (id 962677, 9 feb 2026, https://emaillove.com/email-inspiration-from-made-in-170)
   Twee keer een **outline-cirkel** in rood met dunne serif tekst "SAVE $97" en "SAVE $428", schuin over de kop of naast de set. Bedrag in dollars, niet in procenten. Daarnaast een blauw "tape"-label met handschrift ("WINTER SAVINGS EVENT", "BACK IN STOCK").
3. **Made In · "Ends Tomorrow: Price Drops on Best Sellers"** (id 980231, 16 feb 2026, https://emaillove.com/email-inspiration-from-made-in-173)
   Productgrid 2x4 met per foto rechtsboven een klein rood rechthoekig label "Save $19", "Save $49", "Save $244". Altijd dezelfde plek, altijd een dollarbedrag, naam en "SHOP" eronder.
4. **Great Jones · "Not to be blunt"** (id 1082338, 27 mrt 2026, https://emaillove.com/email-inspiration-from-great-jones-132)
   Getande ronde sticker (zelfde vorm als Floris' referentie) in bordeaux met witte tekst "Exclusive Great Jones color!", schuin rechtsboven het mes. Het dichtst bij de NEW-referentie.
5. **Honeylove · "Not all shapewear is created equal"** (id 610558, 17 okt 2025, https://emaillove.com/email-inspiration-from-honeylove-93)
   Kleine blauwe pill "NEW IN" in de hoek van een productfoto, plus ronde ✓/✕-badges op de foto's (zie vergelijkingen).
6. **Bodily · "Not all pumping bras are created equal"** (id 613673, 17 okt 2025, https://emaillove.com/email-inspiration-from-bodily-79)
   Ronde bordeaux sticker "SAVE 13%" rechtsboven op de 3-pack-foto, niet op de single.
7. Uit ronde 1: Our Place "Take an Extra 10% Off Titanium" (id 856033) met drie stickers in één hero ("SELLING FAST", "HOLIDAY SALE", code). Dat werkt daar, maar oogt drukker dan de rest van hun mails.

### Wat we overnemen

- **Vorm:** getande ronde sticker (Great Jones, Floris) voor de grote boodschap, kleine pill (Honeylove, Made In-labels) voor een status. Geen outline-cirkel en geen tape: past niet bij ons strakke crème-ink-brick.
- **Inhoud, vaste set:** `NEW` (alleen echt nieuwe producten: roasting pan, Just Everything Bundle), `BEST SELLER` (alleen Pan Pro Standard 11", bron facts.csv), `SAVE $XX` (dollarbedrag compare-at min prijs, alleen als de compare-at in Shopify staat en DECISIONS het toelaat; Pan Pro $439 tegen $134 = SAVE $305, 12-delig $1,186 tegen $599 = SAVE $587).
- **Regels:** maximaal één sticker per beeld, altijd in een hoek weg van het product, licht gedraaid (8 tot 12 graden), nooit over het logo of de pan-binnenkant. Dollar boven procent (Made In, Our Place): bij een AOV van $150 tot $250 is "$305" groter dan "69%". Geen asterisk nodig zolang het bedrag letterlijk compare-at min prijs is.
- **Gebouwd:** `scripts/make_sticker.py` (elke tekst, scallop of pill, 2x PNG), `scripts/place_sticker.py` (op een kopie, positie, schaal, draaiing, schaduw, crème naar wit). Bestanden in `assets/stickers/` en `assets/cards/`.

---

## 2. Vergelijkingstabellen

### Wat de merken doen

1. **Bodily** (id 613673): tabel onder de productuitleg. Eigen kolom in mintgroen met merkkop "Bodily / THE DO ANYTHING BRA", andere kolom "OTHER PUMPING BRA" zonder kleur. Zeven rijen met dunne lijnen; eigen kolom overal een icoon, concurrent alleen bij de twee rijen die hij ook kan. Eerlijke gedeelde rijen maken de rest geloofwaardiger. Daarna "Named Best Nursing & Pumping Bra by Women's Health, Glamour & Parents".
2. **Honeylove** (id 610558): vergelijking met foto's: "COMPETITOR" met ✕-badge tegen "HONEYLOVE" met ✓-badge, zelfde model, zelfde pose. Geen merknaam van de concurrent.
3. **Made In** (id 962677): vergelijking binnen het eigen assortiment: "Stainless Clad = deglaze + fond + sauces, Carbon Steel = naturally nonstick + high heat searing, CeramiClad = delicate foods + easy release". Categorie tegen categorie, niemand aangevallen.
4. **HexClad "Welcome to the HexClad family"** (ronde 1, id 87397): tabel als prijsmechaniek ("FIRST PURCHASE MINIMUM / SECOND PURCHASE CREDIT EARNED"), dunne lijnen, ronde hoeken.
5. **Floris' referentie** (roasting pan): eigen kolom wit, andere kolom grijs, vinkje tegen kruisje, 5 rijen, productfoto's die over de rand steken.

### Wat we overnemen

- Twee kolommen, eigen kolom wit en links, andere kolom warm grijs (#ECE8E1). Vijf rijen, gelijke hoogte (64 px, 68 px mobiel), tekst maximaal twee regels op 390 px.
- Altijd **een categorie** ("Coated nonstick", "Stainless steel", "Cast iron"), nooit een merknaam (brand guidelines verbieden aanvallen op HexClad, Caraway, Made In).
- **Gedeelde rijen** met een grijs vinkje (Bodily-principe) waar de andere categorie het ook kan, zoals inductie of PFAS-vrij bij RVS. Dat kost een kruisje maar wint vertrouwen.
- Bron-voetnoot onder de tabel (Light Labs-rapport, review).
- Productfoto over de rand: in mail kan dat niet met negatieve marges, dus het kopstuk (bovenrand met afgeronde hoeken, wit en grijs vlak, pan die erover steekt) is één beeld; de kolomtitels en alle rijen zijn live tekst. De pan wordt ingezet via vermenigvuldigen met de crème achtergrond, zodat hij zowel op crème als op wit natuurlijk staat met zijn eigen schaduw.
- **Gebouwd:** `blocks/compare.html` + `compare-row.html`, `scripts/make_compare_assets.py`, drie varianten met bron per rij in `comparisons.md`.

---

## 3. Callout-anatomie

### Wat de merken doen

1. **HexClad "Why folks love us"** (id 1119597, 3 apr 2026): "LET US EXPLAIN:", drie kopjes ("Peaks", "Valleys", "Easy Cleanup") met twee regels uitleg en dunne gouden scheidingslijnen, links naast een halve pan. Tekst live, pan als beeld.
2. **HexClad welkom** (ronde 1, id 87397): acht cursieve features met lijnen die naar de rand van de pan lopen.
3. **Made In "Stocked and Then Some"** (id 962677): flat lay van de 13-delige set, elk stuk met een dunne lijn naar een label in kleine caps ("8QT STOCK POT + LID", "3QT SAUCIER + LID", "10" CERAMICLAD NON STICK FRYING PAN"), plus de "SAVE $428"-cirkel. Dit is de "what's in the box"-anatomie.
4. **Our Place "Meet the Dual Handle Always Pan"** (id 1798223, 22 sep 2026): per feature een eigen sectie: caps-label ("ROOM TO BREATHE", "SEE HOW DINNER IS GOING"), foto, dan één grote serif-zin met de spec erin ("13-inch diameter for cooking without crowding"). Geen lijnen, wel dezelfde functie.
5. **Floris' referentie**: kop "Take a closer look." met lijn, product van bovenaf in het midden, vier callouts in de hoeken (kop in spatiëring-caps plus twee regels), dunne lijnen met een knik van de tekst naar het product.

### Wat we overnemen

- De Floris-opbouw op desktop: tekst linksboven, rechtsboven, linksonder, rechtsonder als **live tekst** in een tabel van twee kolommen; daartussen het beeld met de lijnen ingebakken. De verticale lijnen beginnen precies onder (of boven) de tekstkolom aan de buitenkant, knikken dan horizontaal naar het product en eindigen in een brick stip met crème rand.
- Mobiel: hetzelfde beeld met genummerde brick-stippen in plaats van lijnen, daaronder de vier callouts als genummerde lijst (15 px tekst). Geen tekst in het beeld, dus geen onleesbare labels op 390 px en alles blijft zichtbaar met beelden uit.
- Kop in Instrument Serif italic ("Take a closer look.") met een dunne ink-lijn eronder, zoals de referentie.
- Alleen onderbouwde callouts (zie claims.csv). "Stay-cool handle" en "lightweight" hebben geen bron en zijn weggelaten; "riveted" alleen als zichtbaar feit, niet als callout gebruikt.
- **Gebouwd:** `scripts/make_callout.py` met `assets/callouts/spec.json` voor Pan Pro (bovenaf, gedraaid zodat de steel naar rechts wijst), Roasting Pan (bovenaf met V-rack, dezelfde packshot als de referentie) en 6-delige set.

---

## 4. Andere visuele patronen die bij ons ontbreken

| Patroon | Gezien bij | Wat Siraat ermee kan | Status |
| --- | --- | --- | --- |
| "As seen in" / pers-balk | Bodily ("Named Best ... by Women's Health, Glamour & Parents"), Brooklinen Wirecutter-badge (ronde 1) | Alleen als er echte pers is. In facts staat niets. Alternatief nu: een bewijsbalk "Third-party tested by Light Labs · Report 25895 · 100,000+ happy customers · 75-year warranty" met het Light Labs-logo als beeld | Vraag aan Floris: pers of podcasts met link |
| Prijs-sticker SAVE $XX | Made In, Our Place, Bodily | Gebouwd. Op productkaarten en in C3-P / W4 / R1 | Klaar voor gebruik |
| Bestseller-label | Made In ("Best Sellers"), Brooklinen "Selling fast" | Gebouwd als pill en sticker. Alleen Pan Pro Standard | Klaar |
| NEW-label | Honeylove "NEW IN", Our Place "New, Times Two" (id 1841582: hele mail over nieuwe items) | Roasting pan (US, sinds sept 2026), Just Everything Bundle | Klaar; let op PDP roasting pan (nog "lifetime" en "100-day trial") |
| Stap voor stap met foto's | Huel "How to claim" (ronde 1), Our Place recepten | P2 en W0 als drie frames uit de chef-video: water-druppeltest, olie, ei. Frames zonder ondertitel kiezen (DECISIONS) | Nieuw blok voorstellen (ronde 3) |
| Voor/na | Honeylove concurrent tegen eigen product | Geen "concurrent na een jaar"-foto's (risico, geen bron). Wel "na het bakken / na één veeg" uit UGC of chef-video voor K1 ("One pass with a damp cloth") | UGC zoeken |
| Size guide visual | Our Place "13-inch diameter", Made In flat lay met maten | W4 maatkeuze nu alleen tekst. Visual met vier pannen naast elkaar met inches en cm. Vereist echte packshots per maat (nu alleen Standard van bovenaf) | Shoot of Shopify-foto's per maat nodig |
| Unboxing / wat zit erin | Made In 13-piece flat lay met labels | 6-delige set als callout gebouwd; 12-delige set kan dezelfde behandeling. Doosfoto bestaat niet (DECISIONS: zelf maken, Higgsfield, geen letters) | Deels klaar |
| Telblok reviews | HexClad "50,000+ 5-Star Reviews" (ronde 1) | "100,000+ happy customers" als groot cijfer in serif | Kan direct |
| Loyalty-balk | Our Place "Dirty Dishes Loyalty Club" in elke footer | Niet aan de orde zolang er geen programma is | Nee |
| Handgeschreven tape-labels | Made In | Past niet bij de strakke huisstijl | Nee |

---

## 5. Samengevat: nieuwe regels voor de mailstandaard

1. Eén sticker per beeld, alleen NEW, BEST SELLER of SAVE $XX, met een feit erachter.
2. Vergelijkingen altijd tegen een categorie, vijf rijen, minstens één eerlijke gedeelde rij als dat waar is, bron in de voetnoot.
3. Callouts: tekst live, lijnen of nummers in het beeld, vier stuks, alleen goedgekeurde claims.
4. Alles 2x, JPG voor foto's (callouts 65 tot 90 kB), PNG alleen voor transparantie en iconen.
