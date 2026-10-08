# 10 · Productmatrix: wat ziet elke koper, per product en per flow

Stand 8 oktober 2026. Vraag van de eigenaar: "Als iemand een checkout verlaat met een apron, wat gebeurt daarmee?" Elke klant moet een mail krijgen over zijn product: juiste hero, eerste zin, bezwaar, review van een echte koper, cross-sell uit de echte kooppatronen en het juiste aanbod.

## Methode

- Per productcategorie een voorbeeld-event per trigger: `research/tailoring/test/mksamples.py` (84 samples `<co|atc|vp|po>_x_<cat>.json`, exacte Shopify-titels).
- `research/tailoring/test/matrix.py` loopt per categorie de route uit `03-routing.md` en `v4-flow-system.md` (nieuwe klant, US), rendert elke mail met Django en controleert verplichte blokken en verboden inhoud. Platte tekst per cel: `python3 -I matrix.py --dump=<map>`. Vóór de bouw: 450 cel-mails gerenderd en gelezen; na de bouw 472 cel-mails, 0 FOUT.
- Screenshots per cel: `research/tailoring/test/matrix_shots.py` → `exports/qa/matrix/<flow>-<mail>-<cat>-<mobile|desktop>.jpg`.
- Oordeel per cel (een cel = alle mails van die flow voor die koper): **goed** = over zijn product, juiste bezwaar en cross-sell; **zwak** = klopt, maar generiek; **fout** = verkeerd product, verkeerde uitleg of verkeerde route.

## Matrix (vóór → na)

Telling 20 categorieën x 7 flows = 140 cellen (7 n.v.t.: accessoires krijgen geen anniversary). **Vóór: 28 goed, 80 zwak, 25 fout. Na: 106 goed, 27 zwak, 0 fout.**

| Product | checkout | cart | browse | post-purchase | winback | vip | anniversary |
|---|---|---|---|---|---|---|---|
| Pan Pro Mini | zwak → **goed** | goed | goed | zwak → **goed** | zwak → **goed** | zwak → **goed** | goed |
| Pan Pro Small | zwak → **goed** | goed | goed | zwak → **goed** | zwak → **goed** | zwak → **goed** | goed |
| Pan Pro Standard | zwak → **goed** | goed | goed | zwak → **goed** | zwak → **goed** | zwak → **goed** | goed |
| Pan Pro Large | zwak → **goed** | goed | goed | zwak → **goed** | zwak → **goed** | zwak → **goed** | goed |
| Deep Pan | zwak → **goed** | zwak → **goed** | goed | zwak → **goed** | zwak → **goed** | zwak → **goed** | goed |
| Wok | zwak → **goed** | zwak → **goed** | goed | zwak → **goed** | fout → **goed** | zwak → **goed** | goed |
| Crêpe | zwak → **goed** | zwak → **goed** | goed | zwak → **goed** | zwak → **goed** | zwak → **goed** | goed |
| Pizza Steel | fout → **goed** | fout → **goed** | fout → **zwak** | fout → **goed** | fout → **zwak** | zwak → **goed** | fout → **goed** |
| Roasting Pan | fout → **zwak** | fout → **zwak** | fout → **zwak** | fout → **goed** | fout → **zwak** | zwak → **goed** | fout → **goed** |
| Potten 2L/3L/7,5L | fout → **goed** | fout → **goed** | fout → **zwak** | fout → **goed** | fout → **zwak** | zwak → **goed** | fout → **goed** |
| 6-delige set | zwak → **goed** | fout → **goed** | goed | fout → **goed** | goed | zwak → **goed** | goed |
| 12-delige set | zwak → **goed** | fout → **goed** | goed | zwak → **goed** | goed | zwak → **goed** | goed |
| Pro/Complete/Just Everything | zwak → **goed** | fout → **goed** | goed | zwak → **goed** | goed | zwak → **goed** | goed |
| Deksel | zwak → **goed** | zwak → **goed** | zwak → **goed** | zwak | zwak | zwak → **goed** | n.v.t. |
| Schort | fout → **goed** | zwak → **goed** | zwak → **goed** | fout → **goed** | zwak | zwak → **goed** | n.v.t. |
| Snijplank | zwak → **goed** | zwak → **goed** | zwak → **goed** | zwak | zwak | zwak → **goed** | n.v.t. |
| Utensils | zwak → **goed** | zwak → **goed** | zwak → **goed** | zwak | zwak | zwak → **goed** | n.v.t. |
| Peper-zoutmolen | zwak → **goed** | zwak → **goed** | zwak → **goed** | zwak | zwak | zwak → **goed** | n.v.t. |
| Dishwasher sheets | zwak | zwak | zwak | zwak | zwak | zwak → **goed** | n.v.t. |
| E-gift card | zwak | zwak | zwak | goed | zwak | zwak | n.v.t. |

### Wat er vóór fout ging (gezien in de gerenderde mails)

- **Schort, checkout**: C1 zei niets over de schort (algemene service-reviews), C3-ACC zette "no coatings" direct na "An apron does want something to cook in" (claims.md: de schort heeft een PVC-coating). Na aankoop raakte de schort `p3-apron` nooit: de flowfilters zochten "Siraat Signature Apron - Azure", Shopify heet "(Azure)".
- **Pizza steel, pot, roasting pan**: C1 "The 11-inch is our best seller", K1 "let the pan cool" plus de Pan Pro-anatomie, K2 de rekensom "1 Siraat Pan Pro 11″ $134", B1 "THE PAN YOU VIEWED: 3 Litre Pot", P2 de eerste-ei-gids, P3 "you started with an accessory", R1 "your pan has a routine: the water drop", N1 "your pan has seen a lot of breakfasts".
- **Wok**: R1 bood een wok aan wie net een wok had.
- **Sets**: K2 rekende 15 gecoate pannen tegen één Pan Pro bij een cart van $599; de $349-set (BDAY SALE) stond in geen titellijst (C2-ACC, geen P2, P3 "Now meet the pan").
- **Pan Pro per maat**: de cross-sell negeerde de kooppatronen (Small → Mini 33%, Standard → Mini 19%, Large → deksel 21%): P3 toonde altijd de plank, R1 een vaste lijst.

## Wat elke koper nu ziet (bron: `scripts/make_product_blocks.py`)

Eerste zin = de kop van het about-blok onder de cart ("ABOUT YOUR <PRODUCT>"), met 3 feiten. Reviews letterlijk uit `content/reviews/reviews.csv` (Trustpilot, 5 sterren, het script controleert het). Aanbod blijft per mail zoals het was (HI10 of eigen code, 4 gifts); de goes-links dragen dezelfde korting (HI10 of de eigen code in de redirect). Geen prijzen in de nieuwe blokken (55% van de orders is internationaal).

| Categorie | Kop (about) | Bezwaar dat weg moet | Review (echt, Trustpilot) | Goes with (kooppatroon) | Hero C1 |
|---|---|---|---|---|---|
| set12 | A complete PFAS-free kitchen. | Why two parcels? Pans and pots can travel separately, each with its own tracking. Nothing is missing. | R530, Lauren W.: "I ordered a full set of the titanium cookware. It arrived in phases. All of it works as stated." | Titanium Cutting Board + Siraat Signature Apron ("Three in ten set owners add a board next.") | c1-hero-set |
| setall | The whole kitchen, in one order. | What if I do not use every piece? Unused pieces can go back within 30 days of delivery. | R398, Fatima: "I ended up buying the whole collection. The food turned out much better cooked and juicier." | Salt & Pepper Mill Set + Dishwasher Sheets | c1-hero-set |
| setbig | Every pan you need, one surface. | What if I do not use every piece? Unused pieces can go back within 30 days of delivery. | R398, Fatima: "I ended up buying the whole collection. The food turned out much better cooked and juicier." | Titanium Cutting Board + Siraat Signature Apron ("Three in ten set owners add a board next.") | c1-hero-set |
| pot | Soups, sauces and pasta, on titanium. | Same warranty as the pans? Yes. Every pot is covered for 75 years. | R018, Susan: "Our pots and pans are beautiful. They clean up very well and look brand new after every cleaning." | Pan Pro 11″ + Deep Pan Pro | c1-hero-pot (P05-A shoot) |
| set6 | Three pans, three lids, one decision. | Pans and lids in one box? They can travel in separate parcels, each with its own tracking. | R025, Sunny C.: "I ordered one pan to try it out. I'm so glad I did. I am so happy with this pan that I'm ordering the set." | Titanium Cutting Board + Siraat Signature Apron ("Three in ten set owners add a board next.") | c1-hero-set (P03-A shoot) |
| standard | The size most kitchens start with. | Will eggs stick? Not once it is hot. Medium heat for 2 to 3 minutes, the water drop test, then a thin layer of oil. | R411, Deb: "I purchased the hammered pro pan standard. It is beautiful and lightweight." | Pan Pro Mini 8″ + Stainless Steel Lid, 28 cm ("One in five 11″ owners comes back for the Mini.") | bestaande c1-hero |
| large | Room for the whole family. | Which lid fits? The 30 cm Stainless Steel Lid. One in five Large owners adds it next. | R473, Joanne W.: "I saved up and bought the large fry pan. It's a whole new way to cook." | Pan Pro Small 10″ + Stainless Steel Lid, 30 cm ("One in five Large owners adds the lid, one in seven the 10″.") | bestaande c1-hero |
| small | Dinner for two, done right. | Is 10″ big enough? For two, yes. Cooking for 3 or more most nights? The 11″ is the better pick. | R401, Renata N.: "Now I can cook knowing I have the top of the line cookware..." | Pan Pro Mini 8″ + Stainless Steel Lid, 26 cm ("One in three Small owners comes back for the Mini.") | bestaande c1-hero |
| mini | The one you grab for breakfast. | Too small to be useful? It is the pan owners buy most as their second one, for the quick jobs. | R324, Jim M.: "I ordered a 2nd smaller pan because of this experience." | Pan Pro 11″ + Stainless Steel Lid, 20 cm ("One in five Mini owners comes back for the 11″.") | bestaande c1-hero |
| deep | Sears like a skillet, holds like a sauté pan. | Is there a lid for it? Match the diameter: the 20, 26, 28 and 30 cm lids fit. There is no lid for the 24 cm yet. | R562, M. K.: "The Deep Pan Pro is my 'go to' favourite because I like to cook big meals" | Wok Pan Pro + Stainless Steel Lid ("The deep pan and the wok are the pair most often bought together.") | bestaande c1-hero |
| wok | Toss it. Nothing spills. | Metal spatula? Yes. There is no coating on it to scratch. | R014, Caliann: "Also, I purchased their titanium wok a few months ago and it performs exactly as expected." | Deep Pan Pro + Crêpe Pan Pro ("The wok and the deep pan are the pair most often bought together.") | bestaande c1-hero |
| crepe | A low rim, so the spatula slides under. | Will crêpes stick? Heat it first on medium, then a few drops of oil. The first one is the test. | R088, Chetan G.: "This is the best crepe pan that I have used that works like a non-stick but gives crispy output like a cast iron pan." | Pan Pro 11″ + Wok Pan Pro | bestaande c1-hero |
| pizza | Lift it in, bake, lift it out. | Dishwasher? Yes. Let it cool first, or use warm water and a little soap. | R048, Sergio C.: "Have used my pizza stone a couple of times and it has made an excellent crust." | Titanium Cutting Board + Pan Pro 11″ | c1-hero-pizza (PizzaSteelReady, Shopify) |
| roast | Sear, roast and make the gravy in one pan. | Will a turkey fit? Check the size above against your bird. Unused, it can go back within 30 days of delivery. | geen echte review (gat) | Titanium Cutting Board + Pan Pro 11″ | bestaande c1-hero |
| panpro | The original hammered titanium pan. | Will eggs stick? Not once it is hot. Medium heat for 2 to 3 minutes, the water drop test, then a thin layer of oil. | R473, Joanne W.: "I saved up and bought the large fry pan. It's a whole new way to cook." | Pan Pro Mini 8″ + Stainless Steel Lid ("The second order is most often a smaller size or a lid.") | bestaande c1-hero |
| board | Nothing soaks in. | Knife marks? Every board shows them. On titanium they are surface lines, not grooves that hold bacteria. | R490, Nagaraju P.: "The cutting board itself is awesome and exceeded my expectations." | Pan Pro 11″ + Titanium Utensil Set ("One in five board owners adds the 11″ pan.") | bestaande c1-hero |
| lid | Sized to your pan. | Which size? Match the diameter: Mini 20 cm, Small 26 cm, Standard 28 cm, Large 30 cm. | R157, Robert H.: "Pans and lids arrived promptly and in good condition. Excellent quality and we look forward to using them for a long time." | Pan Pro Mini 8″ + Titanium Cutting Board | bestaande c1-hero |
| mill | Heavy, metal, and easy to fill. | Which salt? Sea salt, Himalayan or rock salt. | R256, DMZ: "Really well made, plastic free, salt and pepper grinders." | Siraat Signature Apron + Titanium Cutting Board | bestaande c1-hero |
| utensil | Made for your pans. | Will they mark my pan? Any marks are cosmetic. There is no coating to scrape off. | R018, Susan: "I received a free metal spatula as a gift. It works great and does not scratch the pans." | Pan Pro 11″ + Titanium Cutting Board | bestaande c1-hero |
| apron | Made for the cook who stays at the stove. | Machine washable? Wipe it down, or hand wash cold and let it air dry. | R200, Deborah G.: "It comes beautifully boxed, and the apron, bottle and spatula are such lovely gifts." | Salt & Pepper Mill Set + Pan Pro 11″ | c1-hero-apron (ApronAzureEating, Shopify) |
| sheets | One sheet, one load. | How many washes? 30 sheets, up to 60 washes when you tear them in half. | geen echte review (gat) | Pan Pro 11″ + Titanium Cutting Board | bestaande c1-hero |
| giftcard | They pick the pan and the size. | Can it be combined with a code? Yes. It works as payment, and one discount code still applies. | geen echte review (gat) | geen | bestaande c1-hero |

## Waar de blokken staan

| Blok | Mails |
|---|---|
| `{{BLOCK:about}}` (feiten, bezwaar, review) | C1 (alle), K1 (niet-Pan Pro kookgerei, in plaats van de Pan Pro-anatomie), K1-ACC en B1-ACC (vervangt de feitentabel), K2-NEW (niet-Pan Pro, in plaats van de rekensom) |
| `{{BLOCK:goes}}` (2 rijen) | C1, K2-NEW (niet-Pan Pro), R1-PAN (vervangt de vaste lijst), V1, V1-NOCODE |
| `{{BLOCK:goes1}}` (1 rij, naast een hoofdkaart) | P3-PAN en -NOCODE (vervangt de plank; deksel blijft hoofdkaart), P3-SET en -NOCODE (snijplank, 29% van de setkopers) |
| `{{BLOCK:noun}}` / `{{BLOCK:label}}` (pan, wok, pizza steel, pot, set ...) | B1, B2-*, K1, P3-ACCESSORY, R1-PAN, N1, N2 |
| `{{BLOCK:pick}}` (hero per groep) | C1: set, pot, pizza steel, schort, anders de bestaande hero |

Techniek: één `{% with s=<event-expressie> %}` per blok en per veld één `{% if %}/{% elif %}`-keten (zelfde prioriteit overal: set, pot, Pan Pro per maat, vorm, overig kookgerei, accessoires). C1 is 80,3 KB in de export (was 40,6; eerste versie 195 KB; inbox-waarschuwing vanaf 80 KB, blokkade vanaf 100 KB), 31 beelden in de bron, waarvan per ontvanger maar een deel wordt getoond. Pan Pro met deksel in dezelfde order krijgt geen deksel aangeboden.

## De schort, concreet

Checkout met alleen een schort (2% van de checkouts, mediaan $56, 0% bestaande klant):
1. **C1** (30 min): hero "YOUR APRON IS SAVED / Ready when you are. / 16-oz canvas. 4 gifts. 30-day returns." (echte Shopify-foto, Azure-schort). Cart, knop, dan "ABOUT YOUR APRON · Made for the cook who stays at the stove": 16-oz canvas met water-repellent finish, verstelbare banden, echte voorzak en vier kleuren; bezwaar "Machine washable? Wipe it down, or hand wash cold"; review Deborah G. ("the apron, bottle and spatula are such lovely gifts"). Goes with: Salt & Pepper Mill Set (cadeauduo, cross-sell.md) en de Pan Pro 11″ ("The size most kitchens start with"). Geen panuitleg, geen vergelijkingstabel.
2. **C2-ACC** (dag 1): "Yours, or a gift? Both work." met de schortfeiten en de cadeauhoek (ongewijzigd, was al goed).
3. **C3-ACC** (dag 3): de brug naar de pan blijft, maar zonder "no coatings" naast de schort: "tested free from PFAS by Light Labs (report no. 25895), and a 75-year warranty".
4. **C4** (dag 5): eigen code, 48 uur.
Na aankoop: P3-APRON (de titels kloppen nu), zelfde PFAS-zin zonder "no coatings".

Is een accessoire-pad met PFAS-pan-cross-sell logisch? Ja, maar als tweede stap: de schort is vaak een cadeau of een opstap (0% eerder klant, $12 netto per order), dus C1 verkoopt de schort en noemt de pan alleen als tweede rij in "Goes with"; C3-ACC en P3-APRON maken de brug naar de pan, met het PFAS-bewijs in plaats van "no coatings".

## Routing (scripts/build_flows.py)

- Titellijsten zijn nu de exacte Shopify-titels (Admin API, alle statussen, 8 okt): schorten "(Azure)" enz., "Pan Set With Lids | 6-Pcs (BDAY SALE)" en "| 6-Pcs SB", "Cookware Set | 12-Pcs | + FREE PIZZA STEEL" (2x), "Titanium Hammered Pot Set With Lids | 6-Pcs", de BDAY- en "With Lid"-varianten van de Pan Pro, "Wok & Deep Pan Pro/Set". Lijst: `content/facts/shopify-titles.csv`.
- Nieuw `P2_TITELS` (Pan Pro, vormen, sets): P2 en P2-SAFE (eerste ei) niet meer aan wie alleen een pizza steel, roasting pan of pot kocht.
- Dry-run `build_flows.py --offline`: 12 flows, 0 fouten.

## Open punten

1. **Okendo-export** (2.226 reviews): pot, roasting pan, sheets en gift card hebben nog geen echte review; Small en Mini maar één of twee bruikbare quotes.
2. **Klaviyo-preview met een echt profiel**: `{% with s=event.Items|join:',' %}` en `|cut` (cart-links) zijn standaard Django maar niet in Klaviyo zelf bevestigd.
3. **Cart-links**: K-mails gaan nu naar de productpagina uit `event.URL` (myshopify-domein eraf geknipt), niet naar `/cart` (leeg op een ander apparaat). Een echte cart-permalink kan pas als Added to Cart een variant-ID meestuurt.
4. **E-book**: mails noemen nu "The Green Clean E-Guide" (= /products/e, DECISIONS-link, coverbeeld). De orderregel heet in Shopify "Plastic-Free Home E-Book" (handle the-green-clean-e-guide): Floris kiest één naam (audit D7).
5. **Hero's met "your pan" in het beeld** (R1-PAN, P3-PAN, N1) blijven voor pot/pizza steel/roasting pan; nieuwe hero's alleen in C1.
6. Accessoire-P3 (plank, molen, sheets, deksel als eerste order) blijft de algemene "Now meet the pan"; R1-ACC idem.
7. Gift card: C4-code werkt vermoedelijk niet op een gift card (tailoring J4), niet aangepast.
