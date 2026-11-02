# Gift-levering na aankoop · copy (concept, 2 nov 2026)

Nieuwe post-purchase mail die direct na de order beide e-books levert: The Favorites Cookbook (nieuw) en het Plastic-Free Home E-Book (bestaand gift, cover "The Green Clean Guide"). Vervangt op termijn de inhoud van flow YyaMjx "FREE E - GUIDE" (nu: "Your E-Guide Is Ready", 3 minuten na Placed Order, template S2EMYW, beeldmail met PRIME TIME SALE-banner en set-promo). Niets in Klaviyo of Shopify aangepast.

Status: alleen copy. Nog geen HTML, geen beelden geüpload, geen flowwijziging.

## Bronnen en feiten

- Cookbook (PDF 31 okt 2026, 50 pagina's): 25 recepten in 6 hoofdstukken (Eggs & Breakfast, Steak & Red Meat, Fish & Seafood, Pasta & Pizza Night, Stir-Fries & Curries, Chicken, Roasts & Comfort), plus pan school (5 stappen, water-drop test), heat guide & care, toolkit, sides, five pan sauces, doneness & conversions, fix list ("If it sticks"), short shopping list, "In your own words", weekly dinner planner en printable shopping list. Elk recept in US en metrisch. "What 21,000+ Siraat home cooks told us". Cijfers uit het boek: 28% noemt steak/rood vlees als favoriete maaltijd (n = 1,291), 1 op 3 kookt eerst een ei (32%, n = 405).
- E-book: product "The Green Clean E-Guide" (handle `e`), gift-regel "Plastic-Free Home E-Book" ($30). PDP-details: 90 pagina's PDF, DIY-schoonmaakrecepten, ingrediëntengidsen, eco-tips, direct te downloaden (content/products/gift-green-clean-e-guide/product.md). De productpagina zelf gaf vandaag een bot-check en de Shopify-beschrijving is leeg; inhoud dus uit de repo. Huidige Klaviyo-preview: "Natural cleaning tips & DIY recipes for a toxin-free home".
- Gifts op de checkout ("These gifts are included"): Favorites Cookbook, Mystery Gift, Plastic-Free Home E-Book, PFAS Water Purifier Giveaway (weekly draw entry), Free Shipping.

## Vragen voor Floris (open)

1. **[VRAAG FLORIS] Downloadlink cookbook.** Nog geen URL. In de copy staat `{{COOKBOOK_URL}}`.
2. **[VRAAG FLORIS] Downloadlink e-book.** De live template S2EMYW gebruikt `https://delivery.shopifyapps.com/-/396da74b7735ff7f/6d8678add81ad2ad`; DECISIONS (8 okt) noemt `.../b3a2da5476fdac80/509b1c473bc15d58`. Welke is juist? In de copy staat `{{EBOOK_URL}}`.
3. **[VRAAG FLORIS] Krijgt iedereen het cookbook?** De mail gaat ervan uit dat het cookbook op elke order zit (zoals op de checkout). Zo niet: conditioneel blok op de orderregel.
4. **[VRAAG FLORIS] Giveaway.** Hoe en wanneer horen winnaars het? Tot er antwoord is, zegt de mail alleen dat de deelname binnen is. Facts.csv zegt "5 winners a week"; niet in de copy gezet zonder bevestiging en officiële regels.
5. **Waarden.** Checkout zegt Mystery Gift $35, facts.csv en PLAYBOOK $25. Deze mail noemt bewust geen bedragen (zie transactioneel), dus geen conflict in de copy, wel in de rest van de flows.
6. **Twee dingen in het cookbook zelf** (niet in deze mail overgenomen): p. 7 noemt "Oven safe up to 572°F (300°C)" (skill: geen oventemperatuur), en p. 46 citeert een klant met "the lifetime warranty is a big plus" (beleid is 75-year warranty). Afzender in het boek is "The Siraat Kitchen team", footer "Siraat Kitchen" (DECISIONS 15 okt: merknaam is Siraat).

## Vaste afspraken voor alle varianten

- Vaste header en footer uit `klaviyo/templates/partials/` (CLAUDE.md). Geen codebalk, geen offer-bar in de hero, geen BF-topbalk, geen gift-waarden, geen productblokken (zie transactioneel).
- Knoppen (twee primaire, gelijkwaardig): **Download my cookbook** · **Download my e-book**. Onder de knoppen geen verkoop-friction-reducer; wel een gebruiksregel: `PDF · opens on phone, tablet or computer · yours to keep`.
- Naam e-book in de mail: "the Plastic-Free Home E-Book", één keer met "(the cover says The Green Clean Guide)", zodat het cover-beeld en de checkout-naam kloppen.
- Gifts-bevestigingsblok: zelfde tekst in alle varianten (hieronder per variant herhaald voor de bouw), zonder bedragen.
- Hoogstens één zachte tweede actie. Advies: geen link, maar een antwoordvraag ("Reply and tell me what you cook first"). Dat telt niet als promotie en geeft reply-signaal voor deliverability.
- Personalisatie: alleen `{{ first_name|default:'there' }}` in de aanhef van B.

---

## Variant A · Clean delivery card

Korte, rustige mail. Twee kaarten (cover links, tekst en knop rechts; op mobiel onder elkaar), dan het gifts-blok, dan P.S. Ongeveer 140 woorden.

**Sender name:** Siraat
**Subject (3):**
1. Your two books are ready
2. Your Favorites Cookbook is here
3. Downloads inside: your cookbook and e-book

**Preview (2):**
1. 25 recipes and a 90-page home guide. Yours to keep.
2. Both download links are inside, ready when you are.

**Hero** (beeld: both-books hero)
- LABEL: INCLUDED WITH YOUR ORDER
- Headline: `Your books|are ready`
- Subline: Two downloads, yours to keep.

**Body**

> Thanks for your order. Two of your gifts don't need a box, so here they are now.

**Card 1 · The Favorites Cookbook**
> 25 recipes in 6 chapters, built from the answers of 21,000+ Siraat home cooks. From the perfect fried egg to a Sunday roast, with a five-step pan school, a heat guide and a fix list for when something sticks. US and metric in every recipe.
>
> Button: **Download my cookbook**

**Card 2 · The Plastic-Free Home E-Book**
> 90 pages of DIY cleaning recipes, ingredient guides and eco tips for the rest of your kitchen and home. (The cover says The Green Clean Guide. Same book.)
>
> Button: **Download my e-book**

Under the buttons: `PDF · opens on phone, tablet or computer · yours to keep`

**Gifts-confirmation block** (kop: "The rest of your gifts")
- **Mystery gift:** packed with your order. We'll keep what's inside a surprise.
- **Giveaway:** you're entered in this week's draw for a PFAS water filter.
- **Free shipping:** already applied to this order.

> When your order ships, you'll get a separate email with tracking.

**P.S.** Start on pages 6 and 7 of the cookbook. Two minutes of pan school makes every recipe after it better.

---

## Variant B · Warm letter from Benjamin

Tekstmail-gevoel (founder-notes halen de hoogste klik, PLAYBOOK 1). Kleine hero of alleen het both-books beeld, dan een korte brief, twee knoppen, gifts-blok, ondertekening. Ongeveer 200 woorden.

**Sender name:** Benjamin from Siraat
**Subject (3):**
1. Start with an egg
2. Your books arrived first
3. 21,000 of you told us what to cook

**Preview (2):**
1. Your cookbook and e-book are inside. A note from Benjamin.
2. Two downloads, and the one thing to do on day one.

**Hero** (beeld: both-books hero, of geen hero en direct de brief)
- LABEL: A NOTE FROM BENJAMIN
- Headline: `Start with|an egg`
- Subline: Your cookbook and e-book are inside.

**Body**

> Hi {{ first_name|default:'there' }},
>
> Thank you for your order. Before your box gets to you, I wanted you to have something to cook from.
>
> After every order we ask a few short questions. What do you love to eat? What will you cook first? More than 21,000 of you answered. Steak won the favorite-meal question by a long way. And nearly one in three said the first thing they'd cook was an egg, the classic "will it stick?" test.
>
> So we built a cookbook around those answers. The Favorites Cookbook has 25 recipes in 6 chapters, and it opens with the egg.
>
> Button: **Download my cookbook**
>
> Your second book is the Plastic-Free Home E-Book (the cover says The Green Clean Guide). It's 90 pages of DIY cleaning recipes and ingredient guides for the rest of your home.
>
> Button: **Download my e-book**
>
> One honest tip for your first cook in a Siraat pan. There's no coating on it, so release comes from heat and timing. Medium heat for 2 to 3 minutes, flick in a drop of water, and wait until it forms one bead that glides. Then a teaspoon of butter or oil. Skip the preheat, and the egg sticks.
>
> Reply and tell me what you cook first. I read these.
>
> Benjamin
> Founder, Siraat

**Gifts-confirmation block** (onder de brief, kop: "Also on your order")
- **Mystery gift:** packed with your order. We'll keep what's inside a surprise.
- **Giveaway:** you're entered in this week's draw for a PFAS water filter.
- **Free shipping:** already applied to this order.

**P.S.** If an egg does stick, it's almost always the heat, not you. The fix list is on page 44.

---

## Variant C · "What's inside" showcase

Leveringsmail met etalage van het cookbook: hero, cookbook-knop direct onder de hero, hoofdstukrij (6 kleurchips in de kleuren van het boek), drie receptteasers met beeld, dan e-book-kaart, gifts-blok, P.S. Ongeveer 220 woorden. Dit is de meest visuele en minst "transactioneel" ogende variant; geen productnamen of prijzen bij de recepten.

**Sender name:** Siraat
**Subject (3):**
1. 25 recipes, 6 chapters, yours
2. Steak won. Here's the recipe.
3. What 21,000+ home cooks love to cook

**Preview (2):**
1. Your Favorites Cookbook and e-book are ready to download.
2. From the perfect fried egg to a Sunday roast. Download inside.

**Hero** (beeld: cookbook cover of both-books hero)
- LABEL: THE FAVORITES COOKBOOK
- Headline: `Steak won.|Eggs came first.`
- Subline: 25 recipes from 21,000+ home cooks.

**Body**

> Your order came with two books. Both are ready now.
>
> We asked Siraat home cooks what they love to eat and what they'd cook first. Steak and red meat topped the favorite-meal list at 28%. One in three said their first cook would be an egg. The Favorites Cookbook is built around those answers.
>
> Button: **Download my cookbook**

**Inside: 6 chapters** (chips)
Eggs & Breakfast · Steak & Red Meat · Fish & Seafood · Pasta & Pizza Night · Stir-Fries & Curries · Chicken, Roasts & Comfort

**Plus** (één regel): five-step pan school · heat guide · five pan sauces in five minutes · the "if it sticks" fix list · a weekly dinner planner

**Three to start with** (receptteasers, beeld + naam + één regel, geen knop per recept)
1. **The Perfect Fried Egg** · 5 min · Lacy edges, a runny yolk, and the best way to get to know your pan.
2. **Garlic-Butter Ribeye** · 25 min + rest · A deep brown crust, a pink middle and butter you spoon over the top.
3. **Shakshuka** · 35 min · Eggs set in a spiced tomato and pepper sauce. Breakfast, lunch or a Tuesday dinner.

**E-book card · The Plastic-Free Home E-Book**
> 90 pages of DIY cleaning recipes, ingredient guides and eco tips. (The cover says The Green Clean Guide.)
>
> Button: **Download my e-book**

Under the buttons: `PDF · opens on phone, tablet or computer · yours to keep`

**Gifts-confirmation block** (kop: "The rest of your gifts")
- **Mystery gift:** packed with your order. We'll keep what's inside a surprise.
- **Giveaway:** you're entered in this week's draw for a PFAS water filter.
- **Free shipping:** already applied to this order.

**P.S.** Print the planner on page 47. It's a full week of dinners from the book, with room for your own.

---

## Alt-teksten

| Beeld | Alt-tekst |
| --- | --- |
| Cookbook cover | The Favorites Cookbook by Siraat: 25 recipes built from the answers of 21,000+ home cooks |
| E-book cover | The Plastic-Free Home E-Book (The Green Clean Guide): DIY cleaning recipes and eco tips |
| Both books hero | Your two Siraat books: The Favorites Cookbook and the Plastic-Free Home E-Book, ready to download |
| Recipe teaser 1 (p. 10) | The Perfect Fried Egg: a sunny-side-up egg with lacy edges in a hammered titanium pan |
| Recipe teaser 2 (p. 16) | Garlic-Butter Ribeye: a seared ribeye with herb butter, garlic and thyme in a hammered titanium pan |
| Recipe teaser 3 (p. 13) | Shakshuka: eggs set in a spiced tomato and pepper sauce with feta and parsley |

Beeldnotities: receptbeelden zijn volgens het colofon "digitally generated illustrations"; gebruik ze uit het PDF (uitsnede van een kopie, DECISIONS 7 okt) en zeg in de copy nergens "photo". E-book cover: gebruik `content/media/gifts/final/gift-ebook-mockup.png` (rug weggelaten, verhaspelde mini-tekst niet leesbaar). Hero-label staat in het beeld; alt-tekst noemt het label niet als aanbod, want er is geen aanbod.

## Transactioneel: wat eruit moet

Doel: later als transactional in Klaviyo (aanvraag via Klaviyo support, per flowbericht goedgekeurd). Een transactionele mail mag alleen leveren en bevestigen wat de klant al heeft gekocht of gekregen.

Laat weg:
- Elke korting, code of sale: geen codebalk, geen HI10, geen BFCODE, geen "VIP BLACK FRIDAY"-topbalk, geen "up to 70% off", geen offer-bar in de hero.
- Productpromotie en cross-sell: geen productkaarten, geen "Shop the pan", geen set-banner (de huidige S2EMYW heeft "45% off ... Cookware Set Pro" en PRIME TIME SALE: die gaan er allebei uit).
- Gift-waarden in dollars ($30, $35/$25, $15, $450): die lezen als verkoopargument. Alleen bevestigen wat er is.
- Social proof en verkoopclaims als argument (100,000+ customers, Light Labs, 75-year warranty in de body). In de vaste footer-claimsregel mogen ze blijven als de footer-variant dat toelaat, zie hieronder.
- Review- of referral-verzoek, refer-a-friend-rij (`footer-refer-row.html` niet toevoegen), social-knoppen als oproep.
- Urgentie of deadlines, ook niet rond de giveaway.
- Meer dan één zachte extra actie. Advies: alleen "reply and tell me what you cook first", zonder link.

Wel houden: beide downloadknoppen, de gifts-bevestiging (mystery gift in het pakket, giveaway-deelname, free shipping toegepast), de verwijzing naar de aparte verzendmail, de pan-school-tip (gebruiksinstructie bij een gekocht product).

Header en footer: CLAUDE.md eist de vaste header en footer. De vaste versies bevatten winkelnavigatie (header: Cookware, Sets, About; footer: Titanium cookware, Bundles & sets, Accessories, Lab results). **[VRAAG FLORIS]** Voor de transactionele versie een footer-variant zonder winkelnavigatie (alleen logo, claims-regel, unsubscribe, voorkeuren, adres) en een header met alleen de lockup, of de vaste versie houden en het risico nemen dat Klaviyo de mail niet als transactioneel accepteert. Variant A past het best; C is door de receptetalage het meest grensgeval; B kan als de brief geen verkoopzin krijgt.

Instellingen bij de bouw: smart sending uit (staat nu al uit), UTM-parameters uit (al uit), geen extra filters die op marketingtoestemming leunen. Let op: YyaMjx heeft nu een filter "Placed Order $value > 0 in de laatste 3 dagen"; die kan blijven.

## Advies

- **Aanbevolen: variant A** als basis, onderwerp 1 "Your two books are ready" (24 tekens, specifiek, geen "free" in de onderwerpregel). Het past bij de leverfunctie en heeft de beste kans op transactionele goedkeuring.
- Test daarna A tegen B (afzender "Siraat" met kaarten tegen "Benjamin from Siraat" met brief). Eén variabele is hier lastig, omdat B ook de afzender wijzigt; meet op downloadklikken (unieke klikken op beide knoppen) en antwoorden, niet op omzet.
- C bewaren voor een later moment (bijvoorbeeld als dag-2 "open your cookbook"-mail voor wie niet heeft gedownload), zodat de levering zelf transactioneel kan blijven.
