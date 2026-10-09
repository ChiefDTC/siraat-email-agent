# Recept-campagne 01 · copy

Datum: 9 oktober 2026. Rol: copywriter. Concept B uit `recept-01-onderzoek.md`: steak with a brown butter mushroom pan sauce, Titanium Hammered Pan Pro Standard {{SIZE:28}}. Niets gebouwd of verstuurd; alleen dit bestand.

Bronnen gecontroleerd: DECISIONS.md (o.a. 9 okt: "Shop now" en "Shop the pan" mogen in receptcampagnes; 8 okt: Standard $144, gifts-regel, "duties paid"), skill `siraat-direct-response`, `.agents/product-marketing.md`, `research/survey/01-klantbegrip.md`, `content/reviews/library.csv` en `reviews.csv`, `content/catalog/products.json`, `content/facts/claims.csv` en `facts.csv`, v3 welcome W2 en W3 (toon), PLAYBOOK h12 (macro's).

Markering in dit document:
- **[US]** = zin of waarde die in de US anders is dan elders (via macro opgelost, of alleen in de US waar).
- **[MARKT]** = marktgevoelig (eenheden, prijs, verzending, beeld), met de oplossing erbij.
- **[VRAAG FLORIS]** = keuze die ik niet zelf mag maken.

Marktsignaal voor de bouw: campagne naar profielen, dus `<!-- MARKET-SIGNAL: profile -->` (person.Country, dan person.country_code).

---

## 1. Onderwerpregels en preheaders

Vijf types volgens de skill. Lengte in tekens tussen haakjes.

| # | Type | Subject | Preheader |
|---|---|---|---|
| 1 | Nieuwsgierigheid + voordeel | Don't wash the pan yet (22) | The brown bits after a steak are a 5-minute sauce. Recipe inside. |
| 2 | Specificiteit | Steak, mushrooms, one pan, 25 minutes (37) | Brown butter, thyme and a sauce made from what the steak leaves behind. |
| 3 | Vraag | Steak tonight? (14) | Medium heat, a real crust, and a pan sauce from the brown bits. |
| 4 | Story (letterlijke klantzin, R576 Beverly G.) | "Medium rare and browned very nice" (35) | Beverly cooked a rib eye in hers. Here's how I do mine, sauce included. |
| 5 | Offer (zacht, niet aanbevolen) | Steak night, plus 4 gifts with your pan (39) | A recipe from Benjamin. The fall sale is on, the gifts come with every order. |

Afzender: "Benjamin from Siraat" of de vaste afzender **[VRAAG FLORIS]**. De preheader van regel 4 spreekt als Benjamin ("I"); bij een andere afzendernaam wordt het "Here's how Benjamin does his, sauce included."

**Top-2 voor de A/B-test (één variabele: nieuwsgierigheid tegen sociaal bewijs)**
- **A: "Don't wash the pan yet"** met preheader 1. Kookhulp-haak; de twee klikkampioenen in onze historie waren kookhulp ("Why Food Sticks", "Get Out of the Kitchen Quicker"). Opent een lus die de mail sluit (stap 6).
- **B: "Medium rare and browned very nice"** (met aanhalingstekens) en preheader 4. Echte klantzin, steak is de favoriete maaltijd van 22%.
- Zelfde preheaderlengte houden (beide circa 65 tekens). Winnaar op unieke klikken, daarna omzet per ontvanger. Regel 5 niet testen: de mail is bewust geen sale-mail.

---

## 2. Bloktekst, exact zoals in de mail

### 2.0 Topregel (boven de header, klein, caps)

THE WEEKEND PAN · A RECIPE FROM BENJAMIN

### 2.1 Header

Vaste header uit `klaviyo/templates/partials/header.html` (`{{HEADER}}`, lockup zwart op licht). Geen eigen tekst.

### 2.2 Hero

Beeld: de pan met de steak (zie alt-teksten, sectie 3).

Label: FROM BENJAMIN'S PAN

Kop (`Line1|Line2`): Steak night, with|the sauce it leaves behind

Subline: A pan sauce from the brown bits. 25 minutes.

### 2.3 Verhaal + knop

Most people cook eggs first in a new pan. The second thing is almost always a steak, so here's how I do mine.

Medium heat, no rush. And when the steaks come out, the brown bits they leave behind turn into a mushroom sauce in about five minutes.

Knop: **Shop now**

### 2.4 Social proof

Eyebrow: 100,000+ HAPPY CUSTOMERS

Sterren: ★★★★★

Quote: "I cooked a rib eye steak for supper. It was perfect, medium rare and browned very nice!"

Naam: Beverly G., on Trustpilot

Controle: R576 (Trustpilot via Gorgias, 11 april 2026, 5 sterren, verified yes, usable_in_email yes). Letterlijke substring van de volledige tekst, 87 tekens (max 120), grammatica onveranderd gelaten. Geverifieerd met een substring-check tegen `content/reviews/reviews.csv` (zelfde regel als `research/copy/check_reviews.py`, dat alleen 04-rewrites.md leest; die run gaf "errors 0 checked 48"). Er bestaat geen `scripts/check_reviews.py`.
Reserve: R173 Jeanne K. "The meat is seared perfectly on the outside and tender inside." (62 tekens, letterlijk). Let op: R173 staat in `reviews.csv` op usable_in_email = no, in `library.csv` op "ja, alleen snippet". Daarom R576 als eerste keus.

### 2.5 THE RECIPE

Eyebrow: THE RECIPE

Titel: Steak with a brown butter mushroom pan sauce

Meta: Serves 2 · 25 minutes

**Ingredients** (twee kolommen)

| For the steak | For the sauce |
|---|---|
| 2 rib eye or strip steaks, about 1 inch (2.5 cm) thick | 9 oz (250 g) mixed mushrooms, torn |
| Salt and black pepper | 1 shallot, finely chopped |
| 1 tsp neutral oil | 1/2 cup (120 ml) beef stock |
| 3 tbsp butter | 1 tsp Dijon mustard |
| 1 garlic clove, lightly crushed | A splash of cream, if you like |
| 2 sprigs thyme or rosemary | Flaky salt, to finish |

**Method**

1. Take the steaks out of the fridge 30 minutes before you cook. Pat them dry and salt both sides.
2. Set the pan on medium for 2 to 3 minutes. Flick in a drop of water. When it beads up and glides, the pan is ready. Add the oil.
3. Lay the steaks in and leave them alone for 3 to 4 minutes. They stick at first, then let go on their own once the crust has formed. Turn them and give them 3 minutes more for medium rare.
4. Add 2 tbsp of the butter with the garlic and herbs. Tilt the pan and spoon the foaming butter over the steaks for about a minute, until it smells nutty and turns golden brown. Move the steaks to a board to rest.
5. Same pan, same brown butter. Add the mushrooms in one layer and wait 3 minutes before you stir, so they brown instead of steam. Add the shallot for the last minute.
6. Pour in the stock and scrape the bottom with a metal spatula. Every brown bit the steak left behind dissolves into the sauce.
7. Let it bubble for 2 to 3 minutes, until it coats a spoon. Take the pan off the heat and stir in the mustard, the last tbsp of butter and the cream. Pour in the juices from the board.
8. Slice the steaks, lay them back in the pan and spoon the sauce over. Take the whole pan to the table.

Tip (klein, onder de methode): Steak thicker than 1.5 inches (4 cm)? After step 3, slide the pan into a 400°F (200°C) oven for 4 to 6 minutes, then carry on. The handle comes out hot too, so grab a towel.

**Pan-moment** (callout direct onder de methode, serif-cursief of met lichte achtergrond):

That brown layer in step 6 has a name: fond. A coated pan is made to let go of everything, so there's little of it left to work with. On titanium it stays put, and it's the best part of dinner.

### 2.6 Why this pan

Eyebrow: WHY THIS PAN

- **The brown bits become your sauce.** A pure titanium cooking surface with no coatings, so the fond stays in the pan instead of sliding off a coating.
- **Scrape as hard as you like.** Metal spatulas and tongs are fine on it.
- **Stove to oven, one pan.** Sear on the stove, finish a thick cut in the oven, serve from it.

Kleine regel eronder: Tested free from PFAS by Light Labs, report no. 25895.

(Optioneel als link op "report no. 25895" naar de labpagina; zie linkdoelen.)

### 2.7 Find your pan for this recipe

Kop: Find your pan for this recipe

Beeld: productfoto Pan Pro Standard (`partials/shared/pc-standard.jpg` of de eerste Shopify-productfoto).

Productnaam: Titanium Hammered Pan Pro Standard, {{SIZE:28}}

Regel: The pan in the photos, and our best seller.

Prijs: `{{IF:PRICED}}<s>{{WAS:standard}}</s> {{PRICE:standard}}{{ENDIF}}` **[MARKT]**

Sale-regel (één regel, eerlijk, geen datum): The fall sale is on, and every order comes with 4 free gifts.

Knop: **Shop the pan**

Onder de knop: `{{FRICTION}}` **[US]**

### 2.8 P.S. van Benjamin

P.S. Made it? Reply with a photo of your pan. I'd love to see it.

Benjamin
Founder, Siraat's Kitchen

### 2.9 Footer

Vaste footer uit `klaviyo/templates/partials/footer.html` (`{{FOOTER}}`): "Free shipping on all orders · 30-day returns · 75-year warranty", afmelden, voorkeuren. Geen eigen tekst.

---

## 3. Alt-teksten

| Beeld | Alt |
|---|---|
| Header-lockup | Uit de partial (niet wijzigen). |
| Hero (voorkeur: nieuw beeld, gesneden steak met paddenstoelen in de pan) | Sliced medium-rare steak with browned mushrooms and pan sauce in a hammered titanium pan |
| Hero (bestaand: `content/media/ai-flash/steak-sear-4x3-v5.jpg`) | A man laughs as he bastes a steak with thyme and garlic in a hammered titanium pan |
| GIF bij de methode, optioneel (`content/media/chef-video/gif-steak-sear.gif`) | A steak searing in a hammered titanium pan and turning over with a golden crust |
| Sterren in het proof-blok | 5 out of 5 stars |
| Productfoto | Siraat Titanium Hammered Pan Pro Standard, {{SIZE:28}} |

Let op bij de hero: het bestaande beeld `steak-sear-4x3-v5.jpg` toont een glas rode wijn links en staat al in de K3-hero. Voor de Midden-Oosten-doelgroep (onderzoek, sectie 2: geen alcohol) en om herhaling te vermijden: liever een nieuwe hero of een uitsnede zonder het glas (kopie bewerken, DECISIONS 7 okt) **[MARKT]**. De chef-GIF heeft ingebakken ondertitels (DECISIONS 7 okt); bij twijfel weglaten.

---

## 4. Linkdoelen

Campagnecode volgens `research/timing/03-meten.md`: `cmp-JJMMDD`. Hieronder voor vrijdag 16 oktober (`cmp-261016`); bij een andere verzenddag de datum aanpassen. Elke link een eigen `utm_content`.

| Element | Doel |
|---|---|
| Logo in header | `https://siraatskitchen.com/?utm_content=cmp-261016-hdr-1` |
| Shop now (hero) | Voorstel: `https://siraatskitchen.com/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern?utm_content=cmp-261016-hero-1`. Alternatief: `https://siraatskitchen.com/collections/pans?utm_content=cmp-261016-hero-1` **[VRAAG FLORIS]** |
| Report no. 25895 (optioneel) | De labpagina zoals in W3 ("Read it yourself") met `utm_content=cmp-261016-why-1` |
| Productfoto en productnaam | Zelfde als Shop the pan, `utm_content=cmp-261016-pan-img` |
| Shop the pan | `https://siraatskitchen.com/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern?variant=51034913571156&utm_content=cmp-261016-pan-1` |
| Footer | Uit de partial |

Variant: de catalogus heeft voor deze listing één variant ("Default Title", 28 cm / 11", id 51034913571156, beschikbaar in alle 15 landen). De `variant=`-parameter is dus niet nodig maar kan geen kwaad. Er is geen aparte Standard-variant om te kiezen.

Keuze Shop now: de PDP is mijn voorstel (onderzoek: "een knop naar de pan die we gebruikten" werkte; één mail, één pan). Met de collectie als doel meet de klikkaart beter of het verhaal of het productblok de klik doet, maar de lezer moet dan zelf kiezen. Floris beslist.

---

## 5. Prijs en maat per markt (uit `products.json`, via macro's)

| Markt | {{SIZE:28}} | {{WAS:standard}} | {{PRICE:standard}} |
|---|---|---|---|
| US (en NO, betaalt in USD) | 11″ | $288 | $144 |
| CA | 28 cm | C$448 | C$224 |
| UK | 28 cm | £248 | £124 |
| EU | 28 cm | €278 | €139 |
| AU | 28 cm | A$448 | A$224 |
| NZ | 28 cm | NZ$548 | NZ$274 |
| SG | 28 cm | S$408 | S$204 |
| HK, ME, overig, onbekend | 28 cm (11″) bij onbekend | leeg | leeg |

Daarom staat de prijsregel in `{{IF:PRICED}}`; de rest van het blok loopt zonder bedrag. Nooit bedragen met de hand typen (PLAYBOOK h12). Let op: `.agents/product-marketing.md` noemt nog $134; DECISIONS 8 okt en de catalogus zeggen $144.

---

## 6. US-only en marktgevoelige zinnen

| Zin of element | Markering | Oplossing |
|---|---|---|
| `{{FRICTION}}` onder Shop the pan | **[US]** | US: "Free shipping from the US. 30-day returns. 100,000+ happy customers." Elders: "Free shipping, duties paid. 30-day returns. 100,000+ happy customers." Macro regelt het. |
| Prijsregel met doorgestreepte compare-at | **[MARKT]** | `{{IF:PRICED}}`; leeg in HK, ME en overig. |
| Productnaam met maat | **[MARKT]** | `{{SIZE:28}}`: 11″ in de US, 28 cm elders, 28 cm (11″) onbekend. |
| Ingrediënten en oven: oz/cup/°F met gram/ml/°C ertussen | **[MARKT]** | Beide eenheden in elke markt, US eerst (één Engelstalige mail). Bewust geen IF-tak: houdt de mail simpel. |
| "rib eye or strip steaks" | **[MARKT]** | US-namen; buiten de US heet strip ook sirloin. Eventueel "rib eye or sirloin" **[VRAAG FLORIS]**. |
| "The fall sale is on, and every order comes with 4 free gifts." | **[MARKT]** | Bewust zonder bedrag, dus overal waar. Geen einddatum (DECISIONS 7 en 8 okt). Als Floris bedragen wil: `{{GIFTS:total}}` (US $70, UK £55 enz., HK/ME "4 free gifts"). |
| Hero-beeld met wijnglas | **[MARKT]** | Zie sectie 3. |
| Termijnen (Affirm, Shop Pay Installments) | **[US]** | Bewust niet opgenomen: rustige receptmail, en de claim wacht nog op akkoord. |

---

## 7. Keuzes en controles

- **Knoppen:** "Shop now" en "Shop the pan" zijn een vastgelegde uitzondering (DECISIONS 9 okt). Geen andere knoppen, geen code, geen deadline.
- **Medium heat** in stap 2, nergens "high heat" of "smoking hot". Eerlijke beperking zit in stap 3 ("They stick at first, then let go on their own"), in lijn met "Skip the heat, and it sticks".
- **Claims:** "a pure titanium cooking surface" en "no coatings" staan samen; "metal spatulas and tongs are fine" (approved: metal utensil safe); oven zonder pantemperatuur (de 400°F/200°C is de oven voor het recept, geen claim over de pan); PFAS-regel met rapportnummer. Geen non-stick, geen "lifetime", geen levertijden, geen gezondheidsclaim, geen merknamen. "The handle comes out hot too" is eerlijk en botst niet met de verboden claim "the handle stays cool".
- **"Best seller":** facts.csv ("Standard 11" (28 cm, best seller)").
- **Fond-zin** ("A coated pan is made to let go of everything, so there's little of it left to work with"): vergelijking op categorie, geen merk, geen gezondheidsclaim. Komt uit de onderzoeksnotitie ("coated pannen geven nauwelijks fond").
- **Ingrediënten:** geen varken, geen alcohol (onderzoek, sectie 2). Recept in eigen woorden, gebaseerd op gangbare techniek.
- **Invloed:** sociaal bewijs (100,000+, Beverly G.), autoriteit (report no. 25895), liking/unity (Benjamin, "here's how I do mine", P.S.). Geen schaarste.
- **Lengte:** circa 550 woorden inclusief recept; zonder recept circa 180. Past bij "kort: hero, 3 regels, knop, recept, één productblok".
- **Gedachtestreepje:** `grep -c` op U+2014 in dit bestand geeft 0.

## 8. Open punten voor Floris

1. Shop now naar de PDP (voorstel) of naar /collections/pans?
2. Hero: nieuw beeld (gesneden steak met paddenstoelen, geen wijn) of een uitsnede van `steak-sear-4x3-v5.jpg` zonder het glas?
3. Afzendernaam "Benjamin from Siraat" voor deze reeks, passend bij de "I"-stem en de P.S.?
4. "strip" of "sirloin" voor een internationale lijst?
