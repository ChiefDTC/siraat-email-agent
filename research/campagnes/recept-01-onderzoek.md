# Recept-campagne 01 · onderzoek

Datum: 9 oktober 2026. Rol: recept-onderzoeker. Alleen gelezen: Klaviyo (REST, revision 2025-10-15, templates 2025-07-15, conversiemetric Placed Order RSNxYV, Klaviyo-attributie), repo, Email Love en het web. Niets aangemaakt of gewijzigd in Klaviyo of Shopify. Ruwe cijfers per campagne: `research/campagnes/recept-01-campagnes.csv`.

Doel van Floris: een recept-campagne die de funnel vernieuwt en rust geeft. Geen harde sale, wel een verhaal, de pan in beeld, simpele knoppen "Shop now" en "Shop the pan". Voorbeeld: "Cheesesteak Sandwiches Got an Upgrade" (01KXNSFG5BV37XCF5DP5QGCD08).

## Kort

1. **35 recept- en kookcampagnes sinds mei 2025.** Mediaan: 0,70% klik, $0,127 per ontvanger, RPR-index 0,97 (op de maandmediaan van alle campagnes), 0,88% uitschrijving. Recepten zijn dus gemiddeld, niet slecht: ze verkopen iets minder dan een sale, maar met lage uitschrijving zodra het segment klopt.
2. **Wat werkte:** een concreet avondeten in **één pan met de pan zelf in de hero** ("One Pot = Dinner Done", index 2,39, 1,32% klik, de beste pure receptmail ooit), een knop naar **de pan die we gebruikten**, praktische weekendrecepten (ontbijt, meal prep), een **creator of chef met naam** (Cheesesteak van Victoria 1,50; Chef Vladdy 1,40 met klikindex 1,53) en **kleine, actieve segmenten**. De twee absolute klikkampioenen zijn kookhulp, geen recept: "Why Food Sticks" (7,18% klik) en "Get Out of the Kitchen Quicker" ($1,10 per ontvanger), beide naar een klein "Highly Engaged"-segment.
3. **Wat niet werkte:** drankjes en desserts (de pan speelt geen rol: index 0,58 tot 0,85), sfeeronderwerpen zonder gerecht ("Unlock Memorie's" 0,46, "Seasonal cooking done better" 0,77), een recept herhalen naar de hele lijst (Sunday Recipe Day 4 oktober: cacio e pepe voor de tweede keer, naar 134.477 ontvangers, 0,29% klik, $0,049) en receptmails die eigenlijk productcollages zijn.
4. **Alle oude receptmails zijn één groot plaatje** (8 woorden live tekst, ingrediënten en methode als afbeelding) en tonen nog "100-DAY TRIAL", "Life Warranty" en "30,000 customers". De nieuwe mail moet live tekst zijn, met de vaste header en footer uit `klaviyo/templates/partials/`.
5. **Advies:** begin met **Concept B, "Steak with a brown butter mushroom pan sauce"** (snelst te maken, sterkste klantdata: steak is de favoriete maaltijd van 22%), op **vrijdag 16 of 23 oktober, 08:00 lokaal**, naar **HS // Engaged 90 Days (VKxqyA, 89.670)** min Welcome protection XdK77b en Sunset WuHSm6. Zet de reeks voort onder een nieuwe naam op vrijdag, niet als "Sunday Recipe Day".

## 1. Alle eerdere recept-campagnes in Klaviyo

Bron: `GET /api/campaigns` (email, ook gearchiveerd) plus `POST /api/campaign-values-reports` per campaign_id (opens, clicks, conversies, waarde, uitschrijvingen), timeframe 1 jan 2025 tot 9 okt 2026. Gezocht op naam, onderwerp en preheader: recipe, recept, Sunday, meal, dinner, breakfast, one pot, pancake, crepe, curry, soup, fall menu, cheesesteak, food sticks. Follow-ups naar niet-openers en sales met een recept-woordgrap ("Eggcellent") weggelaten. RPR- en klikindex: campagne gedeeld door de mediaan van alle campagnes in die maand (uit `research/history/campaigns-all.csv`), zodat seizoen en sales niet meetellen.

| Datum | Campagne | Onderwerp | Ontvangers | Klik | Omzet | Per ontvanger | Uitschr. | RPR-idx | Klik-idx |
|---|---|---|---|---|---|---|---|---|---|
| 2025-05-07 | Pancake Recipe | Dutch Baby Brunch Idea! | 3155 | 0.73% | $1377 | $0.436 | 1.02% | 1.78 | 0.78 |
| 2025-06-15 | Father's Day | Breakfast Idea for Father's Day | 7722 | 0.87% | $1285 | $0.166 | 1.28% | 1.00 | 0.81 |
| 2025-06-17 | Golden Saffron Rice | Summer Spice Series | 6611 | 0.44% | $174 | $0.026 | 1.35% | 0.16 | 0.41 |
| 2025-06-19 | Summer Solstice (salade) | Light it Up! | 6742 | 0.76% | $734 | $0.109 | 1.19% | 0.65 | 0.71 |
| 2025-06-23 | Recipe, Sip on this (cocktail) | Sip Sip Hooray! | 7933 | 0.90% | $1011 | $0.127 | 1.49% | 0.77 | 0.84 |
| 2025-07-13 | Meal Prep Hacks + Crepe Pan | Save Time, Money & Your Sanity | 6831 | 1.10% | $218 | $0.032 | 1.19% | 0.15 | 0.93 |
| 2025-07-27 | Crepe Pan Recipe | Sweet or Savory? | 6882 | 0.86% | $1336 | $0.194 | 1.48% | 0.91 | 0.73 |
| 2025-08-06 | Chicken Curry Recipe | Quick & Easy Dinner Done | 7260 | 0.86% | $465 | $0.064 | 1.33% | 0.65 | 0.71 |
| 2025-08-11 | Weekly Meal Pan | Top Tips for Meal Planning | 8044 | 1.07% | $1120 | $0.139 | 1.52% | 1.41 | 0.88 |
| 2025-08-19 | **Tired of the Same Dinners** | **One Pot = Dinner Done** | 8409 | **1.32%** | $1983 | $0.236 | 1.50% | **2.39** | 1.09 |
| 2025-09-04 | One Pot Wonders | One Pot Wonders | 9411 | 0.76% | $2120 | $0.225 | 1.25% | 1.44 | 0.83 |
| 2025-09-15 | Fall Recipe Drop (pompoenpasta) | A Recipe Worth Falling For, | 11003 | 0.70% | $1249 | $0.114 | 1.25% | 0.72 | 0.76 |
| 2025-09-30 | Recipe Drop: Zucchini | Zucchini + Feta Fritters, Yes Please! | 7502 | 0.45% | $746 | $0.099 | 0.71% | 0.63 | 0.49 |
| 2025-11-21 | One Pot Wonders (180 dagen) | Ready for a FlavorfuI Dinner? | 21584 | 0.52% | $6558 | $0.304 | 1.02% | 0.84 | 0.32 |
| 2025-12-23 | Christmas Recipe (drankje) | A Winter Warming Drink | 44312 | 0.61% | $3724 | $0.084 | 1.05% | 0.58 | 0.69 |
| 2026-01-11 | **Sunday Meal Prep Made Easy** | Free Recipe Inside | 34753 | 0.97% | $8347 | $0.240 | 0.94% | **1.56** | 1.11 |
| 2026-01-25 | Product Feature + Recipe (crêpe) | Bon Appetite! French Crepe Perfection | 43471 | 0.68% | $6699 | $0.154 | 0.94% | 1.00 | 0.78 |
| 2026-02-06 | Soup Weekend Cooking Idea | Warm Up With a Bowl of Soup | 62642 | 0.49% | $11821 | $0.189 | 0.67% | 1.37 | 0.74 |
| 2026-02-13 | Valentine Recipe (mousse) | Valentine's Day Dessert | 30786 | 0.33% | $4379 | $0.142 | 0.66% | 1.03 | 0.50 |
| 2026-03-14 | Saturday Simple Recipes | Eggs Done Differently | 42138 | 0.71% | $6177 | $0.147 | 0.67% | 1.29 | 1.06 |
| 2026-04-11 | Saturday Simple Recipes | Your Weekend Breakfast | 43608 | 0.74% | $6720 | $0.154 | 0.86% | 1.02 | 0.98 |
| 2026-05-01 | **Weekends Recipe Drop (Chef Vladdy)** | Free Recipe Inside | 40484 | 0.89% | $5833 | $0.144 | 0.59% | 1.40 | **1.53** |
| 2026-05-09 | Confit Byaldi (ratatouille) | Unlock Memorie's | 53961 | 0.27% | $2534 | $0.047 | 0.40% | 0.46 | 0.47 |
| 2026-05-16 | Refreshment Recipe Drop | Drink In a Summer's Delight | 67742 | 0.30% | $5929 | $0.088 | 0.53% | 0.85 | 0.52 |
| 2026-06-01 | June Kickoff (kokoswater) | Stay Hydrated this Summer | 75908 | 0.31% | $4418 | $0.058 | 0.50% | 0.62 | 0.63 |
| 2026-06-06 | Instagram Recipe Drop | Dinner Sorter | 85083 | 0.46% | $7722 | $0.091 | 0.53% | 0.97 | 0.94 |
| 2026-06-30 | June Wrap-Up | June Wrap-Up | 71591 | 0.54% | $6509 | $0.091 | 0.49% | 0.97 | 1.10 |
| 2026-07-15 | Meals You Can Make at Home | Easy Skillet Lasagne Recipe Inside | 46245 | 0.49% | $2991 | $0.065 | 0.62% | 0.62 | 0.91 |
| 2026-07-17 | *Why Food Sticks* (kookhulp) | Why Food Sticks | 3801 | **7.18%** | $1738 | $0.457 | 1.03% | **4.36** | **13.3** |
| 2026-07-21 | *Get Out of the Kitchen Quicker* (kookhulp) | Get Out of the Kitchen Quicker | 1940 | 3.14% | $2137 | **$1.101** | 0.88% | **10.51** | 5.81 |
| 2026-07-30 | **Cheesesteak (creator Victoria)** | New Weeknight Favorite Landed | 50357 | 0.29% | $7913 | $0.157 | 0.48% | 1.50 | 0.54 |
| 2026-08-13 | Customer Story (eieren) | He was skeptical | 40415 | 0.54% | $4271 | $0.106 | 0.53% | 1.11 | 1.00 |
| 2026-08-23 | Sunday Recipe Day (creator Serena) | ONE POT CACIO E PEPE | 48880 | 0.73% | $4044 | $0.083 | 0.57% | 0.87 | 1.35 |
| 2026-09-22 | HS Fall Menu | Seasonal cooking done better | 30262 | 0.40% | $1632 | $0.054 | 0.38% | 0.77 | 0.59 |
| 2026-10-04 | Sunday Recipe Day (herhaling) | ONE POT CACIO E PEPE | 134477 | 0.29% | $6570 | $0.049 | 0.33% | 0.63 | 0.67 |

Let op bij het lezen: opens zijn sinds Apple Mail Privacy onbetrouwbaar (ongeveer de helft is machine-open), dus klik en omzet per ontvanger tellen. Omzet is Klaviyo-attributie (5 dagen klik, 1 dag open): bij grote lijsten komt veel "omzet" van mensen die toch al kochten. Kleine segmenten (onder 10.000) geven wisselende uitkomsten.

### Templates van de 5 beste (HTML opgehaald, beelden bekeken)

| Template | Campagne | Opbouw | Wat opvalt |
|---|---|---|---|
| TnmJhJ | One Pot = Dinner Done (2,39) | Sale-balk, logo, hero "Whipped Ricotta One Pot Chicken Pasta" **in de Deep Pan Pro**, 3 regels intro ("one of our favourite RecipeTin Eats meals"), knop **"GET THE POT WE USED"**, ingrediënten en instructies als beeld, productblok Deep Pan Pro | Het enige recept waar de pan het hoofdbeeld is. Eén product, één knop, naar de PDP. |
| VS2SMp | Sunday Meal Prep (1,56) | Hero soep, reviewbalk ("4.9/5 by 30,000+"), knop "SHOP HEALTHIER COOKWARE", USP-gif met "100-DAY TRIAL" | Kort, persoonlijke aanhef "Hey {{first_name}}", januari (goede maand voor koken thuis). |
| Razee8 | Cheesesteak, creator Victoria (1,50) | Hero eten, "Got an Upgrade", intro over Victoria van "All I do is eat and eat", SHOP NOW, 100K+-blok, THE RECIPE (Ingredients, Method), "Find Your Perfect Pan for this Recipe" + SHOP THE PAN, USP-balk "100-DAY TRIAL" | Het voorbeeld van Floris. De hero toont **geen pan**, alleen broodjes. Ging naar Engaged 90 dagen niet-US, buiten recente kopers. |
| TMs8jh | Chef Vladdy (1,40, klikindex 1,53) | "GET COOKING WITH US", 100K+-blok, recept, SHOP BUNDLES | Chef met naam en een herkenbaar gerecht (Din Tai Fung-stijl kool). Hoogste klikindex van de gewone receptmails. |
| VdJxWD | Soup Weekend (1,37) | SHOP SIRAAT, 100K+-blok, Green Goddess Soup, ingrediënten, garnering, SHOP ACCESSORIES, USP "Life Warranty, 100 Day-Trial" | Februari, soep: seizoen en gerecht kloppen. |

Ter vergelijking ook UVr2ct (Why Food Sticks: genummerde stappen met foto, drie pannen, link naar /pages/care-use) en YuuVPr (Sunday Recipe Day, creator @seasonedbyserena, "Share your recipe on socials").

### Wat werkte en wat niet

| Factor | Werkte | Werkte niet |
|---|---|---|
| Recept-type | Avondeten in één pan (one pot 2,39 en 1,44), weekendontbijt en eieren (1,29 en 1,02), meal prep (1,56), soep in de winter (1,37), steak-achtig vlees (cheesesteak 1,50) | Drankjes (0,58 tot 0,85), dessert (1,03 maar klik 0,33%), saffraanrijst en ratatouille (0,16 en 0,46): niets dat de pan laat zien |
| Pan in beeld | Pan met eten als hero (TnmJhJ) | Alleen eten zonder pan (cheesesteak: goede omzet, maar klikindex 0,54) |
| Creator/UGC | Naam plus gerecht: Victoria 1,50, Chef Vladdy 1,40 | Creator alleen als handtekening onder een herhaald recept (Serena, 0,87 en 0,63) |
| Onderwerp | Gerecht plus voordeel: "One Pot = Dinner Done", "Eggs Done Differently"; preheader "Free Recipe Inside" | Sfeer zonder gerecht: "Unlock Memorie's", "Light it Up!", "Seasonal cooking done better", "Dinner Sorter" |
| Lengte | Kort: hero, 3 regels, knop, recept, één productblok | Productcollages (Fall Menu: 14 beelden, 3 woorden) |
| Publiek | 30 of 90 dagen engaged, of nog kleiner ("Highly Engaged" voor kookhulp) | De hele lijst (4 oktober: 134.477, 0,29% klik) |
| Dag | Do en vr: mediaan RPR-index 1,28 en 1,37 (n=4 en 5) | Zondag: 0,91 (n=7), dinsdag 0,77. Accountbreed is zondag de zwakste klikdag voor campagnes (0,50%, research/timing/01-data.md) |

Conclusie: een receptmail verkoopt als hij **bewijst wat de pan kan** (de pan doet iets dat je ziet), niet als hij alleen een lekker gerecht deelt.

## 2. Web- en concurrentieonderzoek

### Recepten die het pan-voordeel laten zien

Belangrijk vooraf, uit onze eigen feiten (`content/facts/facts.csv`, Gorgias 5326403): **voorverwarmen op medium, 2 tot 3 minuten, nooit op hoog vuur**, waterdruppeltest, dan een theelepel olie, eiwit laten loslaten voor je keert. Recepten met "smoking hot pan" (smash burgers, wokken op vol vuur) passen daarom niet en zouden plakklachten uitlokken. Het verschil van titanium tonen we dus niet met "hoge hitte" maar met:

- **Fond voor een pan sauce.** Geen coating, dus de bruine aanbaksels blijven in de pan en worden de saus (blussen, losschrapen, inkoken). Coated pannen geven nauwelijks fond. Dit is precies het klassieke patroon in skillet-recepten: aanbraden, eruit, aromaten in het vet, blussen met cider of bouillon, schrapen, inkoken, koude boter erdoor ([Vikalinka](https://vikalinka.com/wprm_print/boneless-pork-chops-with-apples-and-cider), [Aggie's Kitchen](https://aggieskitchen.com/hard-cider-pork-chops-with-apples-and-onions/print-recipe/15702/), [The Chopping Block](https://www.thechoppingblock.com/recipe-apple-cider-glazed-pork-chops)).
- **Metalen spatel mag** (claim "metal utensil safe", approved). Schrapen is deel van het recept. Review R220-M Carole: "I've had an old, metal spatula that was my mother's... I can use it with confidence on my pans now."
- **Van fornuis naar oven** (claim "oven safe", approved, zonder temperatuur van de pan noemen). De oventemperatuur van het recept zelf is kookinstructie, geen claim.
- **Krokant zonder coating:** gnocchi uit het pak direct bakken in plaats van koken ([Tesco Real Food](https://realfood.tesco.com/recipes/butternut-squash-and-sage-crispy-gnocchi.html), [Well Plated](https://www.wellplated.com/wprm_print/one-skillet-butternut-squash-gnocchi-with-italian-sausage)).
- **Vaatwasserbestendig en geen seasoning** (beide approved) als eindregel van het recept.

Herfst/oktober: appel en cider, pompoen en butternut, paddenstoelen, salie en bruine boter. Een harde trendbron voor oktober 2026 vond ik niet; de seizoensingrediënten zelf zijn de veilige keuze (Graza en Food52 sturen deze week precies pompoen- en soeprecepten, zie hieronder).

Doelgroep let op: Siraat heeft een flinke Midden-Oosten- en moslimdoelgroep (markt AE, merknaam). **Geen varkensvlees en geen alcohol als hoofdingrediënt.** Daarom kip in plaats van pork chops en "apple cider (cloudy apple juice)" in plaats van hard cider.

### Concurrenten (Email Love, september en oktober 2026)

| Merk | Mail | Wat ze doen | Les voor ons |
|---|---|---|---|
| Our Place | "Wok Tips, Tricks, and a Recipe" (juli 2026) | Kenji López-Alt als expert, "What can you do with this wok?", vier technieken met foto (sear, steam, eggs, smoke), een hack, dan het recept. Eén knop naar de wok. | Laat per beeld één ding zien dat de pan kan. Expert met naam. |
| Our Place | "A Fish Fry for Your Juneteenth Weekend", "A Mid-Autumn Festival Recipe" | Chef-recept rond een moment, één knop "Get the recipe", cookware als bijrol. | Rust: weinig verkoop, veel sfeer. |
| Made In | "Your Summer Cooking List" | Receptoverzicht, elk gerecht gekoppeld aan een techniek, niet aan een SKU. Email Love: "content-first sends build the habit of opening". | Techniek als haak. |
| Made In | "Limited. Legendary. Back Again." (26 sep) | Chef Tom Colicchio, archieffoto, gebraden vlees **in** de pan als hero, recepten onderaan. | Pan met eten als hero, verhaal van een persoon. |
| Graza | "Pumpkin, two ways" (7 okt 2026) | Twee pompoenrecepten, knoppen "MAKE IT" en "MAKE THIS TOO", dan één productblok "You'll need some olive oil". | Twee knoppen: recept en product. Seizoen direct in de kop. |
| Great Jones | "Every meal needs some greens" | Warme foodfotografie, cookware als "supporting character". | |

HexClad en Caraway hebben geen receptmails in de Email Love-bibliotheek. Gemeen patroon: pan of product zichtbaar in gebruik, een persoon met naam (chef, creator, oprichter), één recept of techniek, één of twee knoppen. Geen korting.

## 3. Drie recept-concepten

Opbouw voor alle drie (zoals het voorbeeld van Floris, maar in live tekst):

1. Vaste header (`klaviyo/templates/partials/header.html`, lockup zwart op licht).
2. Hero-foto: **de pan met het gerecht erin**, hamerslag zichtbaar.
3. Label + kop + 2 tot 3 regels verhaal (Benjamin of creator), knop **Shop now**.
4. Blok "100,000+ happy customers" met één 5-sterrenreview (letterlijk, uit `content/reviews/top.md`).
5. **THE RECIPE**: Ingredients en Method als live tekst, met tijd en porties.
6. "Why it works in titanium": drie korte regels (geen coating, dus fond; metalen spatel mag; oven safe / vaatwasser).
7. "The pan we used" met productfoto, maat, prijs per markt uit `content/catalog/products.json`, knop **Shop the pan**.
8. Vaste footer (`footer.html`: 30-day returns, 75-year warranty).

Noot: de skill `siraat-direct-response` zegt "nooit Shop now". Floris vraagt het nu expliciet voor deze campagne. Voorstel: in DECISIONS.md vastleggen als uitzondering voor receptmails ("Shop now" en "Shop the pan" mogen in recept-campagnes) **[VRAAG FLORIS ter bevestiging]**.

### Concept A · "One-pan cider chicken with apples and thyme"

- **Waarom het werkt voor Siraat:** bewijst drie dingen in één gerecht: aanbraden tot het vel vanzelf loslaat, fond die saus wordt (blussen met cider, schrapen met metaal), en van fornuis naar oven in dezelfde pan. Puur oktober (appel, cider, tijm). Halal-vriendelijk.
- **Haak:** "The one-pan Sunday." Benjamin's herfstgerecht: "In October this is what's in my pan on Sunday. One pan, the oven does half the work, and the best part of the sauce is what the chicken leaves behind." Alternatief: een klant of creator die het maakt **[VRAAG FLORIS: is er creator-materiaal voor de herfst?]**.
- **Pan:** Titanium Hammered Pan Pro Standard 28 cm (11"), US $144 (compare-at $288), GB £124, AU A$224. https://siraatskitchen.com/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern. Voor 6 tot 8 dijen: Pan Pro Large 30 cm (12"), US $149, https://siraatskitchen.com/products/titanium-hammered-pan-pro-large. (Pan Pro With Lid is in de US niet leverbaar, niet linken.)
- **Hero-foto:** bovenaanzicht van de pan op een houten plank, vier goudbruine kippendijen tussen appelpartjes en tijm, glanzende saus, een hand met een metalen spatel die door de saus gaat. Flash-stijl (skill `siraat-flash-style`) of warm avondlicht. Nieuw te maken (Higgsfield met echte productfoto als referentie, geen letters in beeld).
- **Review:** R220-M Carole (metalen spatel), of R173 Jeanne K. "This beautiful pan makes me want to cook more!".

**Serves 4 · 45 minutes**

Ingredients
- 4 bone-in, skin-on chicken thighs
- Salt and black pepper
- 1 tsp neutral oil
- 2 firm apples (Honeycrisp or Pink Lady), cut into wedges
- 2 shallots, halved
- 4 sprigs fresh thyme
- 1 cup (240 ml) cloudy apple juice or unfiltered apple cider
- 1 tbsp Dijon mustard
- 2 tbsp cold butter

Method
1. Pat the thighs dry, season well on both sides and leave them for 15 minutes. Heat the oven to 200°C / 400°F.
2. Preheat the pan on medium for 2 to 3 minutes. A drop of water should roll around like a bead. Add the oil.
3. Lay the thighs in skin side down and leave them alone for 8 to 10 minutes, until the skin is deep golden and lets go of the pan by itself. Turn them over.
4. Tuck the apples, shallots and thyme around the chicken and slide the whole pan into the oven for about 20 minutes, until the thickest piece reads 74°C / 165°F.
5. Back on the stove (the handle is oven hot, use a mitt). Move the chicken and apples to a plate.
6. Pour the apple juice into the pan and scrape up every brown bit with a metal spatula. Let it bubble until it has reduced by half, about 5 minutes, then stir in the mustard.
7. Off the heat, swirl in the cold butter until the sauce turns glossy. Return the chicken and apples and spoon the sauce over.
8. Serve straight from the pan with mash or crusty bread. Afterwards: warm water, a soft sponge, done.

Onderwerpregels + preheader
| # | Type | Subject | Preheader |
|---|---|---|---|
| 1 | Specificiteit | One pan, Sunday dinner | Crispy chicken, apples and a sauce made from the brown bits. |
| 2 | Nieuwsgierigheid + voordeel | The brown bits are the sauce | Cider chicken with apples, start to finish in one pan. Recipe inside. |
| 3 | Vraag | What's in your pan this Sunday? | Benjamin's October one-pan chicken. Stove to oven, 45 minutes. |

### Concept B · "Steak with a brown butter mushroom pan sauce"

- **Waarom het werkt voor Siraat:** steak is de favoriete maaltijd van 22% van de kopers en de tweede eerste kook (10%, enquête). Bewijst de korst bij medium vuur (gelijkmatige warmte, 3-ply met aluminium kern) en de fond voor een pan sauce, plus metalen tang en spatel. Paddenstoelen en tijm maken het herfst. Dit is het antwoord op de twijfel "werkt titanium echt" (15%) zonder het woord non-stick.
- **Haak:** een klantzin als kop: Jeanne K. (R173, Trustpilot 5 sterren, 25 juli 2026): "The meat is seared perfectly on the outside and tender inside." Daarna Benjamin: "Most people use their pan for eggs first. The second thing is almost always a steak. Here's how I do mine, and the 3-minute sauce that comes free with it." (Zin staat letterlijk in de review in `content/reviews/library.csv`; R173 heeft nog geen handmatige snippet met deze zin, dus voor gebruik nog door `research/copy/check_reviews.py` halen.)
- **Pan:** Titanium Hammered Pan Pro Standard 28 cm (11"), US $144 (compare-at $288), GB £124, AU A$224. https://siraatskitchen.com/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern
- **Hero-foto:** twee gesneden steaks in de pan, roze binnenkant, gebakken paddenstoelen ernaast, lepel die bruine boter overgiet, hamerslag zichtbaar aan de rand. Er is al bruikbaar beeld: `content/media/ai-flash/steak-sear-4x3-v5.jpg` en `content/media/chef-video/gif-steak-sear.gif` (die still staat al in de K3-hero; voor de campagne liever een nieuwe hero en de GIF bij de methode).
- **Review:** R173 Jeanne K. (zie boven).

**Serves 2 · 25 minutes**

Ingredients
- 2 steaks, ribeye or strip, about 1 inch (2.5 cm) thick
- Salt and black pepper
- 1 tsp neutral oil
- 2 tbsp butter
- 1 garlic clove, lightly crushed
- 2 sprigs thyme or rosemary
- 9 oz (250 g) mixed mushrooms, torn or sliced
- 1 shallot, finely chopped
- 1/2 cup (120 ml) beef stock
- 1 tsp Dijon mustard, or a splash of cream

Method
1. Take the steaks out of the fridge 30 minutes before cooking, pat them dry and salt them well.
2. Preheat the pan on medium for 3 minutes. Water drop test, then the oil.
3. Lay the steaks in and do not touch them for 3 to 4 minutes. When the crust is ready they release on their own. Turn and give them another 3 to 4 minutes for medium rare.
4. Add the butter, garlic and herbs. Tilt the pan and spoon the foaming butter over the steaks for a minute. Move them to a board to rest.
5. Same pan, same butter: add the mushrooms in one layer and leave them for 3 minutes before you stir, so they brown instead of steam. Add the shallot for the last minute.
6. Pour in the stock and scrape the bottom with a metal spatula. Everything brown dissolves into the sauce. Simmer for 2 to 3 minutes until it coats a spoon, then stir in the mustard or cream.
7. Slice the steaks, lay them back in the pan and spoon the mushrooms and sauce over. Serve it at the table, in the pan.

Onderwerpregels + preheader
| # | Type | Subject | Preheader |
|---|---|---|---|
| 1 | Story (klantzin) | "Seared perfectly on the outside" | Steak night, plus the 3-minute pan sauce that comes free with it. |
| 2 | Specificiteit | Steak, mushrooms, one pan | Brown butter, thyme and a sauce made from what the steak leaves behind. |
| 3 | Nieuwsgierigheid + voordeel | Don't wash the pan yet | The brown bits after a steak are a sauce. Here's how. |

### Concept C · "Crispy gnocchi with butternut squash, sage and brown butter"

- **Waarom het werkt voor Siraat:** krokant goudbruin zonder coating, zonder seasoning, in één pan in 25 minuten; vegetarisch en door de week. Met de Deep Pan Pro is het ook de tweede pan voor wie de koekenpan al heeft (in onze historie wint "een nieuw product aan bestaande kopers", index 6,9 voor deksels aan pankopers).
- **Haak:** "Don't boil the gnocchi." Een kooktruc als opening (de kookhulpmails zijn onze klikkampioenen), daarna het recept. Of: een klantfoto van gnocchi of pompoen uit de reviews (UGC mag, DECISIONS 7 okt).
- **Pan:** Titanium Hammered Deep Pan Pro 28 cm (11"), US $144 (compare-at $475), GB £109, AU A$209. https://siraatskitchen.com/products/titanium-hammered-deep-pan-pro (variant 28CM). Alternatief: Pan Pro Standard 28 cm.
- **Hero-foto:** Deep Pan schuin van boven, goudbruine gnocchi, oranje blokjes butternut, krokante salieblaadjes, parmezaan die erover valt, houten lepel. Warm herfstlicht of flash. Nieuw te maken.
- **Review:** R088 Chetan G. "works like a non-stick but gives crispy output like a cast iron pan." (over de crêpepan; bij dit gerecht beter een algemene review, bijvoorbeeld R518 Graham C.)

**Serves 3 to 4 · 25 minutes**

Ingredients
- 1 lb (500 g) shelf-stable potato gnocchi, straight from the pack
- 1 tbsp olive oil
- 14 oz (400 g) butternut squash, in 1/2 inch (1.5 cm) cubes
- 3 tbsp butter
- 12 fresh sage leaves
- 1 garlic clove, thinly sliced
- 3.5 oz (100 g) baby spinach
- 1.5 oz (40 g) Parmesan, finely grated
- Zest of half a lemon, a pinch of chili flakes, salt and pepper

Method
1. Preheat the pan on medium for 2 to 3 minutes, do the water drop test, then add the olive oil.
2. Add the squash in one layer, season, cover with a lid or a baking sheet and cook for 8 minutes. Uncover, toss and cook until the edges are browned and the cubes are tender. Tip them into a bowl.
3. Add the gnocchi to the empty pan in one layer. Leave them for 3 to 4 minutes until golden underneath, toss, and give them 3 minutes more. No boiling needed.
4. Push the gnocchi to one side, drop in the butter and, once it foams, the sage leaves. Fry for about a minute until the leaves crisp and the butter smells nutty.
5. Add the garlic for 30 seconds, then return the squash and toss everything together.
6. Fold in the spinach a handful at a time until it just wilts.
7. Off the heat, add the Parmesan, lemon zest and chili. Taste for salt and serve from the pan.

Onderwerpregels + preheader
| # | Type | Subject | Preheader |
|---|---|---|---|
| 1 | Nieuwsgierigheid + voordeel | Don't boil the gnocchi | Fry them straight from the pack. Squash, sage and brown butter, one pan. |
| 2 | Specificiteit | Crispy gnocchi, one pan, 25 minutes | Butternut squash and sage for a Thursday night. Recipe inside. |
| 3 | Vraag | What's for dinner tonight? | Golden gnocchi, brown butter and squash. Nothing to boil, one pan to wash. |

De skill vraagt 5 onderwerpregels per mail (incl. offer-type); de offer-variant laat ik hier bewust weg omdat deze campagne geen aanbod heeft. A/B: één variabele, bijvoorbeeld bij B regel 1 (klantzin) tegen regel 2 (specificiteit). Winnaar op unieke klikken, daarna omzet per ontvanger.

### Aanbeveling: welk concept eerst

**Eerst Concept B (steak).** Redenen: (1) grootste klantbelang: steak is de favoriete maaltijd (22%), en onze beste vleesmail (cheesesteak) haalde index 1,50; (2) er is al beeld (steak-sear still en GIF), dus snel klaar; (3) het bewijst het verschil dat koopwaardig is (korst plus pan sauce, geen coating) en sluit aan op de echte twijfel "werkt het"; (4) met paddenstoelen en tijm voelt het herfst zonder op een feestdag te leunen. Daarna **A (cider chicken)** eind oktober, als "the one-pan Sunday" voor de hele maand het meest oktober-achtig gerecht, en **C (gnocchi)** begin november, eventueel naar bestaande kopers met de Deep Pan als tweede pan.

## 4. Doelgroep en timing

### Segment

- **Opnemen:** `HS // Engaged 90 Days` (VKxqyA, 89.670 profielen, bijgewerkt 6 okt). Dit is het nieuwere van de twee identieke 90-dagen-segmenten (TMaWCL heeft dezelfde 89.670 maar is sinds sep 2025 niet aangepast).
- **Uitsluiten:** `v4 · Welcome protection` (XdK77b, 7.219: nieuwe inschrijvers zonder order, krijgen eerst de welcome), `v4 · Sunset · unengaged 120d` (WuHSm6, 75.716), plus de vaste uitsluitingen VSnBnJ (unsubscribe), W3q7Zy (bounced), W4vNzF (suppression), XTpfNG (spam). Optioneel `HS // Purchased in the last 7 days` (TLqivd): hun pan is nog onderweg en ze zitten in de post-purchase-flow.
- **Niet** naar de hele Email List (Uw8eZG): de herhaling van 4 oktober deed daar 0,29% klik en $0,049. De 30-dagen-segmenten (TNdhKc) zijn al een jaar niet bijgewerkt; niet gebruiken zonder controle.
- Wil Floris de kookhulp-aanpak testen: dezelfde mail eerst naar een klein "highly engaged"-segment (Y5rxC2 "Highly engaged", gebruikt voor Why Food Sticks; telt nu 0 profielen, dus eerst de definitie nakijken), na 24 uur naar de rest. Niet nodig voor de eerste keer.
- Markten: één Engelstalige mail; prijs in het productblok per markt uit `products.json` (helper in `build_template.py`), of zonder prijs met alleen "Shop the pan" als dat het bouwen vereenvoudigt. De pan is in alle 15 markten gepubliceerd.

### Dag en tijd

- **Vrijdag, 08:00 lokale tijd** (Klaviyo "send in recipient's local time"). Onderbouwing: campagneklik per weekdag ma tot zo 0,59 / 0,50 / 0,54 / 0,68 / **0,71** / 0,63 / **0,50%** (`research/timing/01-data.md`, sectie 3); orders pieken in het weekend (16 tot 17% per dag), en een mail werkt 24 tot 48 uur, dus vrijdag ochtend vangt het koken én kopen van het weekend. Bij de receptmails zelf: do en vr mediaan RPR-index 1,28 en 1,37 tegen zondag 0,91 (kleine n).
- Optioneel A/B op verzendtijd 08:00 tegen 17:30 lokaal (A/B 5 uit `research/timing/02-advies.md`), alleen als de onderwerp-test niet tegelijk loopt.
- **Cap: maximaal 3 campagnes per week per profiel** (02-advies; de week van 28 september met 9 campagnes gaf twee keer zoveel uitschrijvingen). In oktober lopen de fall-sale-mails (Email 3 en 4 staan in Draft). Plan de receptmail in een week met hooguit twee andere campagnes, en niet op dezelfde dag als een sale-mail. Voorstel: vrijdag 16 oktober of vrijdag 23 oktober.

### "Sunday Recipe Day" voortzetten?

**De reeks wel, de naam en de zondag niet.** De twee sends onder die naam scoorden 0,87 en 0,63, en de tweede was een herhaling naar de hele lijst. Zondag is accountbreed de zwakste klikdag. Voorstel: een vaste, rustige reeks van **één receptmail per 2 tot 3 weken op vrijdag**, met een eigen herkenbaar label in de hero (bijvoorbeeld "FROM BENJAMIN'S PAN" of "THE WEEKEND PAN"), steeds één gerecht dat één pan-voordeel bewijst, één pan in beeld, nooit een herhaald recept. In de mail mag het gerecht wel voor zondag zijn ("for Sunday"), zoals Concept A.

### Meten

- Succes: klik boven de mediaan van de receptmails (0,70%) en omzet per ontvanger boven $0,127, met uitschrijving onder 0,50% (laatste receptmails 0,33 tot 0,57%).
- UTM `cmp-JJMMDD` volgens `research/timing/03-meten.md`.
- Vergelijk "Shop now" (hero) en "Shop the pan" (productblok) per link in de Klaviyo-klikkaart: dat zegt of het verhaal of het productblok de klik doet.

## Open vragen voor Floris

1. "Shop now" en "Shop the pan" mogen in receptmails, ondanks de copyregel? (Vastleggen in DECISIONS.md.)
2. Is er creator- of klantmateriaal (foto of video) van een herfstgerecht in een Siraat-pan? Zo nee: Benjamin als verteller en een nieuwe hero via Higgsfield.
3. Akkoord met vrijdag in plaats van zondag, en een nieuwe reeksnaam?

## Bronnen

- Klaviyo: campagnes en `campaign-values-reports` (9 okt 2026), templates TnmJhJ, VS2SMp, Razee8, TMs8jh, VdJxWD, UVr2ct, YuuVPr; segmenten VKxqyA, TMaWCL, TNdhKc, XdK77b, WuHSm6.
- Repo: `research/history/01-beste-mails.md` en `campaigns-all.csv`, `research/timing/01-data.md` en `02-advies.md`, `research/survey/01-klantbegrip.md`, `.agents/product-marketing.md`, `content/catalog/products.json`, `content/reviews/top.md` en `library.csv`, `content/facts/claims.csv` en `facts.csv`, DECISIONS.md.
- Email Love: Our Place 1592843, 1810271, 1500575; Made In 1537790, 1811452; Graza 1871440; Great Jones 1027955.
- Web: [Tesco Real Food, crispy gnocchi](https://realfood.tesco.com/recipes/butternut-squash-and-sage-crispy-gnocchi.html), [Well Plated, one-skillet squash gnocchi](https://www.wellplated.com/wprm_print/one-skillet-butternut-squash-gnocchi-with-italian-sausage), [Vikalinka, pork chops with apples and cider](https://vikalinka.com/wprm_print/boneless-pork-chops-with-apples-and-cider), [Aggie's Kitchen, cider chops](https://aggieskitchen.com/hard-cider-pork-chops-with-apples-and-onions/print-recipe/15702/), [The Chopping Block, cider glaze](https://www.thechoppingblock.com/recipe-apple-cider-glazed-pork-chops). De recepten hierboven zijn eigen formuleringen op basis van gangbare techniek, geen overgenomen tekst.
