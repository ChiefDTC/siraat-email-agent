# E5 en E6 · nieuwe copy, drie varianten, US en INT

Stand 5 nov 2026. Basis: de platte tekst van Homestead (Figma). Copy in het Engels, toelichting in het Nederlands. Bronnen gecontroleerd: DECISIONS.md, PLAYBOOK.md, skill siraat-direct-response, content/facts/claims.csv en facts.csv, content/catalog/products.json (prijzen 31 okt), content/reviews/top.md (alle quotes letterlijk uit de gecontroleerde snippets, 5 sterren, max 120 tekens, paarverschil max 30).

Niets in Klaviyo, Figma of Shopify aangepast.

---

## 0. Wat er anders is dan bij Homestead, en waarom

| Homestead | Wat ik schreef | Reden |
|---|---|---|
| "Nothing sticks when the heat is right." | "Cold metal grabs your food, hot metal lets it go." plus de waterdruppeltest | "Non-stick" mag niet als claim (claims.csv: needs-proof). Release komt van hitte en timing, dat is de uitleg die we wel mogen geven. |
| Pan Pro Large op "medium-high" | "medium for 2 to 3 minutes" | Gorgias 5326403: medium, nooit hoog. Voorkomt plakklachten na de mail. |
| "Clean up both pans in under a minute." | "Both pans go in the dishwasher." | "Under a minute" staat nergens. "Dishwasher safe" is approved. |
| "a centimeter thick" in de US-mail | US "about 3/8 inch (1 cm)", INT "about 1 cm" | US-lezer denkt in inches. |
| "4 FREE gifts" | "4 gifts with every order", filter als "a weekly chance to win" | DECISIONS 7 okt: bij de filter alleen "win", nooit "free". |
| "PFAS-free water purifier ($450 value)" | US "a weekly chance to win {{GIFTS:filterline}}" (= a $450 PFAS water filter), INT "a weekly chance to win a PFAS water filter" | Skill en PLAYBOOK h11/v5: nooit "purifier", nooit "free filter". De opdracht noemde "a PFAS-free water purifier"; ik volg de vaste regel. **Floris: akkoord?** |
| "Offer valid while supplies last 11/01 to 11/30" | "Ends Monday, November 30." (INT: "Ends Monday 30 November.") en in de kleine letters "Offer valid November 1 to 30." | "While supplies last" leest als voorraaddruk zonder bewijs. Einddatum 30 nov is opgegeven. |
| "It's the pan Siraat started with." | "the original hammered titanium pan. First orders shipped December 20, 2024." | Siraat begon met titanium snijplanken (PLAYBOOK 1). Het originele gehamerde pan-claim mag wel (owner override). |
| "The surface that's there on day one is the same surface ten years from now." | "There's no coating on it, so there's nothing to wear thin." | "Ten years" is een levensduurclaim zonder bron. Titanium kan cosmetisch krassen (claims.csv: scratch-proof forbidden). |
| "That's why we call it the last pan you'll ever buy." | Alleen in de mond van een klant (R583 Scott Y.: "the last pans we ever have to purchase") of als vraag, met de 75-jarige garantie als bewijs | Geen eigen levensduurbelofte; "covered for 75 years", nooit "lasts 75 years". |
| Onderwerp "One PFAS-free pan for life" | Niet gebruikt | "For life" leest als "lifetime" (forbidden sinds 1 okt). |
| Review "Buy it because it's safe, it's the only pan you will need in your kitchen, life long." | Vervangen door reviews uit top.md | Niet gevonden in onze reviewbibliotheek (content/reviews), dus niet te controleren, en "life long" botst met de garantieregel. **Floris: als Homestead de bron heeft (Trustpilot-link), kan hij terug.** |
| "100,000+ Siraat customers agree." | "100,000+ happy customers" | Vaste formulering (DECISIONS 7 okt). |
| "Benjamin, Founder, Siraat" | `Benjamin` / `Founder, Siraat` | DECISIONS 15 okt: merknaam in copy is Siraat. |

**Open punten voor Floris**

1. Gratis Titanium Hammered Pizza Steel bij de 12-delige set (US): staat in de Homestead-tekst maar niet in DECISIONS. Overgenomen, graag bevestigen. Gemarkeerd als [VRAAG FLORIS: pizza steel].
2. {{SAVE:standard}} en {{STACK:standard}} bestaan nog niet als macro. Floris vult ze in (US: save $336 = $480 min $144; waardestapel $550 = $480 + $15 + $30 + $25, filter telt niet mee).
3. E6 A heeft één plek voor een echt detail van Benjamin (welke pan hij weggooide, of waarom titanium). Zonder dat detail loopt de tekst ook. Gemarkeerd als [VRAAG FLORIS: detail].
4. E5 INT: Thanksgiving is een US-feest (Canada was 12 okt). De INT-versie gaat over "a big dinner" en noemt Thanksgiving alleen tussen haakjes. Homestead stuurt E5 ook naar INT; dit is het voorstel.
5. E6 sluit volgens de kalender Pan Pro Standard-kopers uit; dat segment bestaat nog niet (kalender-november-2026.md).
6. Geen "VIP Black Friday"-label gebruikt, dus de einddatum mag erin.

---

## 1. Gedeelde bouwstenen

Alle varianten: vaste header bovenaan, vaste footer onderaan (`klaviyo/templates/partials/`), logo = lockup. Topbar boven de header: `BLACK FRIDAY SALE IS LIVE` (DECISIONS 31 okt).

**Friction reducer onder elke primaire knop**
- US: `Free shipping from the US. 30-day returns. 100,000+ happy customers.` (macro `{{FRICTION}}`)
- INT: `Free shipping, duties paid. 30-day returns. 100,000+ happy customers.`

**BF-band (espresso-blok, `{{BLOCK:offer}}`-stijl, zonder deadline-parameter)**

US:
> BLACK FRIDAY SALE
> Up to 70% off, plus 4 gifts with every order.
> Free shipping ({{GIFTS:ship}}) · The Plastic-Free Home e-book ({{GIFTS:ebook}}) · A mystery gift ({{GIFTS:mystery}}) · A weekly chance to win {{GIFTS:filterline}}
> With the 12-piece set: a Titanium Hammered Pizza Steel, free. [VRAAG FLORIS: pizza steel]
> Ends Monday, November 30.
> [Button: Get my Black Friday price] → https://siraatskitchen.com/collections/black-friday-sale

INT:
> BLACK FRIDAY SALE
> Up to 70% off, plus 4 gifts with every order.
> Free shipping, duties paid · The Plastic-Free Home e-book · A mystery gift · A weekly chance to win a PFAS water filter
> Ends Monday 30 November.
> [Button: Get my Black Friday price] → https://siraatskitchen.com/collections/black-friday-sale

**Ondertekening:** `Benjamin` / `Founder, Siraat`

**Kleine letters (boven de footer):** US `Offer valid November 1 to 30. Gifts while the sale runs; the water filter is a weekly draw.` INT `Offer valid 1 to 30 November. The water filter is a weekly draw.`

**Reviews in deze mails (allemaal uit top.md, gecontroleerde snippets)**

| ID | Klant | Snippet | Tekens |
|---|---|---|---|
| R562 | M. K. | "The Deep Pan Pro is my 'go to' favourite because I like to cook big meals" | 73 |
| R518 | Graham C. | "We cooked the best omelette we have ever eaten when we used the pan for the first time." | 87 |
| R411 | Deb | "I purchased the hammered pro pan standard. It is beautiful and lightweight." | 75 |
| R138 | Tammy | "I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns." | 101 |
| R583 | Scott Y. | "These hammered Titanium pans from Siraat have been the best we have owned yet... the last pans we ever have to purchase." | 120 |
| R240 | Brandon W. | "Siraat replaced a pan free of charge... I just sent them the picture and they honored the warranty." | 99 |
| R169 | Michael G. | "The real test was my egg the next morning... the egg released completely and slid around the pan like it was non-stick." | 119 |
| R011 | Lorraine | "We have purchased twice from Siraat... Expensive but definitely Value for money. Quality cookware!" | 98 |
| R399 | Anthony | "My deliveries were prompt and I live in Melbourne, Australia... I love their titanium cookware" | 94 |

Paren per mail: R562 + R518 (verschil 14), R411 + R138 (26), R583 + R240 (21), R169 + R011 (21), R399 + R138 (7). "Non-stick" staat alleen in een klantcitaat (R169), dat mag (top.md spelregels).

---

# E5 · di 10 nov · Weekly Recipe (Thanksgiving sides)

Pijler 4 (made for people who love to cook). Receptcampagne, dus "Shop the pan"-knoppen mogen (DECISIONS 9 okt). Eén idee: twee bijgerechten vooruit maken.

## E5 · Variant A · Recept eerst, rijk opgemaakt

**Invalshoek:** het recept is de mail. Twee receptkaarten met tijd, pan en genummerde stappen, een "make ahead"-regel per recept, dan pas de BF-band. Voor de lezer die kookt en bewaart.

**Onderwerp**
- A (specificiteit): `Make it Tuesday, serve it Thursday`
- B (curiosity + benefit): `The Thanksgiving side that's better reheated`

**Preview:** `Two sides, two pans, done before the big day.`
INT-onderwerp A: `Make it ahead, serve it hot` · B: `The side dish that's better reheated` · Preview: `Two sides, two pans, done before the big dinner.`

**Blokopbouw**

| # | Blok | Inhoud | Knop |
|---|---|---|---|
| 0 | Topbar | BLACK FRIDAY SALE IS LIVE | |
| 1 | Vaste header | lockup | |
| 2 | Hero 1200x1200 | foto zoete-aardappelschijven in de Pan Pro Large (flash-stijl). Label `WEEKLY RECIPE` / `Make it Tuesday.\|Serve it Thursday.` / subline `Two sides that get better overnight.` (INT: `Make it ahead.\|Serve it hot.`) | |
| 3 | Intro (live tekst) | Benjamin-opener | |
| 4 | Receptkaart 1 | titel, meta-regel (pan, tijd), ingrediënten, 5 stappen, make-ahead-kader | `Shop the Pan Pro Large` |
| 5 | Receptkaart 2 | idem | `Shop the Deep Pan Pro` |
| 6 | "Why these two pans" | drie iconregels (`{{BLOCK:features}}`): titanium, Light Labs, vaatwasser | |
| 7 | Reviews | R562 + R518 | |
| 8 | BF-band | zie sectie 1 | `Get my Black Friday price` |
| 9 | Afsluiter + ondertekening + P.S. | | |
| 10 | Kleine letters, vaste footer | | |

### E5 A · US

Benjamin here.

Thanksgiving Thursday has one stove and five dishes that all want it at 4 pm. So I take two sides off the list early. Both get made the Tuesday before. Both reheat while the turkey rests. And the sweet potatoes, honestly, come out better the second day.

**Maple sweet potato rounds**
Pan Pro Large · 20 minutes · make ahead up to 2 days

You need: 2 large sweet potatoes, olive oil, 2 tablespoons maple syrup, flaky salt.

1. Slice the sweet potatoes into rounds about 3/8 inch (1 cm) thick.
2. Heat the Pan Pro Large on medium for 2 to 3 minutes. Flick in a drop of water. When it balls up and glides, add a thin layer of olive oil.
3. Lay the rounds flat and leave them alone for 4 minutes. Cold metal grabs your food, hot metal lets it go.
4. Flip. Another 4 minutes, until they're golden on both sides and soft in the middle.
5. Drizzle with maple syrup. Salt. Done.

Make ahead: into the fridge in a covered dish. On Thursday, 8 minutes in a low oven.
One honest note: if a round sticks, the pan wasn't hot yet. Give the next batch another minute.

[Shop the Pan Pro Large] → /products/titanium-hammered-pan-pro-large
{{FRICTION}}

**Green beans with shallots and almonds**
Deep Pan Pro · 10 minutes · make ahead up to 2 days

You need: 1 lb green beans, 2 shallots, a knob of butter, half a lemon, a handful of toasted almond slivers.

1. Blanch the beans for 3 minutes in salted boiling water. Drain and leave them in the colander.
2. Slice the shallots and soften them in a little butter in the Deep Pan Pro over medium-low.
3. Beans back in. Toss.
4. Squeeze of lemon, almonds on top.

Make ahead: fridge. On Thursday, back into the Deep Pan Pro on the lowest heat while everything else rests. They'll hold there for 30 minutes.
Why the Deep Pan: the higher sides mean you can toss a full batch without beans going over the edge.

[Shop the Deep Pan Pro] → /products/titanium-hammered-deep-pan-pro
{{FRICTION}}

**Why these two pans** (iconregels)
- A pure titanium cooking surface, no coatings.
- Tested free from PFAS by Light Labs, report no. 25895.
- Dishwasher safe. Thursday night, that matters.

**Reviews**
- "The Deep Pan Pro is my 'go to' favourite because I like to cook big meals" · M. K., verified buyer
- "We cooked the best omelette we have ever eaten when we used the pan for the first time." · Graham C., verified buyer

**BF-band US** (sectie 1)

Happy cooking,
Benjamin
Founder, Siraat

P.S. The Black Friday sale is live: up to 70% off and 4 gifts with every order. Doing the whole kitchen? The 12-piece set comes with a free Titanium Hammered Pizza Steel [VRAAG FLORIS: pizza steel]. Just arrived and selling fast. Ends Monday, November 30.
[Shop the 12-piece set] → /products/titanium-hammered-cookware-set

### E5 A · INT

Benjamin here.

A big dinner has one stove and five dishes that all want it at the same moment. So I take two sides off the list early. Both get made two days ahead. Both reheat while the main course rests. And the sweet potatoes, honestly, come out better the second day. (Cooking for Thanksgiving this month? These are the two I'd make.)

**Maple sweet potato rounds**
Pan Pro Large · 20 minutes · make ahead up to 2 days

You need: 2 large sweet potatoes, olive oil, 2 tablespoons maple syrup, flaky salt.

1. Slice the sweet potatoes into rounds about 1 cm thick.
2. Heat the Pan Pro Large on medium for 2 to 3 minutes. Flick in a drop of water. When it balls up and glides, add a thin layer of olive oil.
3. Lay the rounds flat and leave them alone for 4 minutes. Cold metal grabs your food, hot metal lets it go.
4. Flip. Another 4 minutes, until they're golden on both sides and soft in the middle.
5. Drizzle with maple syrup. Salt. Done.

Make ahead: into the fridge in a covered dish. On the day, 8 minutes in a low oven.
One honest note: if a round sticks, the pan wasn't hot yet. Give the next batch another minute.

[Shop the Pan Pro Large]
Free shipping, duties paid. 30-day returns. 100,000+ happy customers.

**Green beans with shallots and almonds**
Deep Pan Pro · 10 minutes · make ahead up to 2 days

You need: 500 g green beans, 2 shallots, a knob of butter, half a lemon, a handful of toasted almond slivers.

1. Blanch the beans for 3 minutes in salted boiling water. Drain and leave them in the colander.
2. Slice the shallots and soften them in a little butter in the Deep Pan Pro over medium-low.
3. Beans back in. Toss.
4. Squeeze of lemon, almonds on top.

Make ahead: fridge. On the day, back into the Deep Pan Pro on the lowest heat while everything else rests. They'll hold there for 30 minutes.
Why the Deep Pan: the higher sides mean you can toss a full batch without beans going over the edge.

[Shop the Deep Pan Pro]
Free shipping, duties paid. 30-day returns. 100,000+ happy customers.

**Why these two pans**, **Reviews**: als US.

**BF-band INT** (sectie 1)

Happy cooking,
Benjamin
Founder, Siraat

P.S. The Black Friday sale is live: up to 70% off and 4 gifts with every order. Doing the whole kitchen? The 6-piece set gives you three pans and three lids. Just arrived and selling fast. Ends Monday 30 November.
[Shop the 6-piece set] → /products/titanium-hammered-pan-set-with-lids-6-pcs

---

## E5 · Variant B · Thanksgiving prep plan (dinsdag, woensdag, donderdag)

**Invalshoek:** een draaiboek in plaats van een recept. Drie dagkaarten, met de pannen als held: wat ze op welke dag doen. Lost het echte probleem van de lezer op (één fornuis op donderdag). Pannen krijgen elk een productkaart met prijs (US).

**Onderwerp**
- A (specificiteit): `Your Thanksgiving, in 3 days and 2 pans`
- B (vraag): `What can you cook before Thursday?`

**Preview:** `Tuesday, Wednesday, Thursday. The plan that frees up your stove.`
INT-onderwerp A: `A big dinner, in 3 days and 2 pans` · B: `What can you cook two days early?` · Preview: `Day one, day two, the big day. The plan that frees up your stove.`

**Blokopbouw**

| # | Blok | Inhoud | Knop |
|---|---|---|---|
| 0 | Topbar | BLACK FRIDAY SALE IS LIVE | |
| 1 | Vaste header | | |
| 2 | Hero 1200x1200 | beide pannen op het fornuis, flash-stijl. Label `THANKSGIVING PREP PLAN` (INT `BIG DINNER PREP PLAN`) / `Three days.\|Two pans.` / subline `One free stove on Thursday.` (INT `One free stove on the day.`) | |
| 3 | Intro | | |
| 4 | Dagkaart TUESDAY | zoete aardappel, kort recept | |
| 5 | Dagkaart WEDNESDAY | sperziebonen, kort recept | |
| 6 | Dagkaart THURSDAY | tijdlijn opwarmen (T-30, T-10, serveren) | |
| 7 | Twee productkaarten naast elkaar (`{{BLOCK:productcard}}`) | Pan Pro Large, Deep Pan Pro; US met prijs, INT met "70% off" | `Shop the Pan Pro Large` / `Shop the Deep Pan Pro` |
| 8 | Reviews | R562 + R518 | |
| 9 | BF-band | | `Get my Black Friday price` |
| 10 | Ondertekening, P.S., kleine letters, vaste footer | | |

### E5 B · US

Benjamin here.

Here's the problem with Thanksgiving: everything wants the stove at the same time. Here's my fix: two sides get done before Thursday, in two pans, and on the day they only need warming up.

**TUESDAY · Maple sweet potato rounds (Pan Pro Large, 20 minutes)**
Slice 2 large sweet potatoes into 3/8 inch (1 cm) rounds. Heat the Pan Pro Large on medium for 2 to 3 minutes, until a drop of water balls up and glides, then add a thin layer of olive oil. Lay the rounds flat. Don't move them for 4 minutes. Flip, 4 more. Maple syrup, salt. Into the fridge.

**WEDNESDAY · Green beans with shallots and almonds (Deep Pan Pro, 10 minutes)**
Blanch the beans 3 minutes, drain. Soften 2 sliced shallots in butter in the Deep Pan Pro. Beans back in, a squeeze of lemon, toasted almond slivers. Into the fridge. Both pans go in the dishwasher. That's Wednesday.

**THURSDAY · The warm-up**
- 30 minutes before dinner: green beans into the Deep Pan Pro, lowest heat. They hold there.
- 10 minutes before: sweet potatoes into a low oven for 8 minutes.
- Turkey out to rest. Your sides are already hot.

Why it works in these pans: the cooking surface is pure titanium with no coatings, so the only trick is heat. Cold metal grabs your food, hot metal lets it go. Tested free from PFAS by Light Labs, report no. 25895.

**Productkaarten**
- Pan Pro Large · `{{WAS:large}} {{PRICE:large}}` · "Room for a whole batch of rounds." · [Shop the Pan Pro Large]
- Deep Pan Pro · `{{FROM:deep}}` · "Higher sides for sauces, pasta and one-pan dinners." · [Shop the Deep Pan Pro]
Onder de kaarten: {{FRICTION}}

**Reviews:** R562 M. K. + R518 Graham C.

**BF-band US**

Have a good Thanksgiving,
Benjamin
Founder, Siraat

P.S. Cooking for a crowd every year? The 12-piece set is the whole kitchen in one box, and right now it comes with a free Titanium Hammered Pizza Steel [VRAAG FLORIS: pizza steel]. Just arrived and selling fast. The sale ends Monday, November 30.
[Shop the 12-piece set]

### E5 B · INT

Benjamin here.

Here's the problem with a big dinner: everything wants the stove at the same time. Here's my fix: two sides get done in the two days before, in two pans, and on the day they only need warming up. (Thanksgiving, a birthday, the whole family on a Sunday. Same plan.)

**DAY ONE · Maple sweet potato rounds (Pan Pro Large, 20 minutes)**
Slice 2 large sweet potatoes into 1 cm rounds. Heat the Pan Pro Large on medium for 2 to 3 minutes, until a drop of water balls up and glides, then add a thin layer of olive oil. Lay the rounds flat. Don't move them for 4 minutes. Flip, 4 more. Maple syrup, salt. Into the fridge.

**DAY TWO · Green beans with shallots and almonds (Deep Pan Pro, 10 minutes)**
Blanch the beans 3 minutes, drain. Soften 2 sliced shallots in butter in the Deep Pan Pro. Beans back in, a squeeze of lemon, toasted almond slivers. Into the fridge. Both pans go in the dishwasher. That's day two.

**THE BIG DAY · The warm-up**
- 30 minutes before dinner: green beans into the Deep Pan Pro, lowest heat. They hold there.
- 10 minutes before: sweet potatoes into a low oven for 8 minutes.
- Main course out to rest. Your sides are already hot.

Why it works in these pans: the cooking surface is pure titanium with no coatings, so the only trick is heat. Cold metal grabs your food, hot metal lets it go. Tested free from PFAS by Light Labs, report no. 25895.

**Productkaarten (zonder bedragen)**
- Pan Pro Large · `70% off` · "Room for a whole batch of rounds." · [Shop the Pan Pro Large]
- Deep Pan Pro · `Up to 70% off` · "Higher sides for sauces, pasta and one-pan dinners." · [Shop the Deep Pan Pro]
Onder de kaarten: `Free shipping, duties paid. 30-day returns. 100,000+ happy customers.`

**Reviews:** R562 M. K. + R518 Graham C.

**BF-band INT**

Happy cooking,
Benjamin
Founder, Siraat

P.S. Cooking for a crowd every year? The 6-piece set gives you three pans and a lid for each. Just arrived and selling fast. The sale ends Monday 30 November.
[Shop the 6-piece set]

Opmerking: controleer of het Deep Pan Pro op alle varianten 70% af staat; daarom op de kaart "Up to 70% off". Pan Pro Large INT (GB £129 bij £430) is 70%.

---

## E5 · Variant C · Kort en direct: één recept, sterke BF-sectie

**Invalshoek:** het snelste recept (sperziebonen, 10 minuten) als haak, daarna een volle BF-sectie met vier producten en de gifts. Voor de lezer die het recept scant en voor de sale komt. Ongeveer de helft van de lengte van A.

**Onderwerp**
- A (specificiteit): `10-minute green beans, made Tuesday`
- B (aanbod): `A Thanksgiving side + up to 70% off`

**Preview:** `One side dish, one pan, and the Black Friday prices.`
INT-onderwerp A: `10-minute green beans, made ahead` · B: `A make-ahead side + up to 70% off` · Preview: `One side dish, one pan, and the Black Friday prices.`

**Blokopbouw**

| # | Blok | Inhoud | Knop |
|---|---|---|---|
| 0 | Topbar | BLACK FRIDAY SALE IS LIVE | |
| 1 | Vaste header | | |
| 2 | Hero 1200x900 (4:3) | sperziebonen in de Deep Pan Pro. Label `WEEKLY RECIPE` / `Ten minutes.\|Made Tuesday.` / subline `Reheats while the turkey rests.` (INT `Ten minutes.\|Made ahead.` / `Reheats while dinner rests.`). Aanbodbalk onder in de hero: US `UP TO 70% OFF  ·  {{GIFTS:TOTAL}}`, INT `UP TO 70% OFF  ·  4 GIFTS WITH EVERY ORDER` | |
| 3 | Recept (compact, 4 stappen) | | `Shop the Deep Pan Pro` |
| 4 | Kop "This week's Black Friday prices" | | |
| 5 | Productraster 2x2 (`{{BLOCK:productcard}}`) | US: Deep Pan Pro, Pan Pro Large, 6-piece set, 12-piece set (+ pizza steel). INT: Deep Pan Pro, Pan Pro Large, Pan Pro Standard, 6-piece set. Sticker op de sets: `JUST ARRIVED` | per kaart `Shop the pan` / `Shop the set` |
| 6 | Gifts (`{{BLOCK:gifts5}}`, raster) | vier gift-beelden | |
| 7 | Eén review | R562 M. K. (Deep Pan) | |
| 8 | Primaire knop + friction | | `Get my Black Friday price` |
| 9 | Ondertekening, kleine letters, vaste footer | | |

### E5 C · US

Benjamin here. One side dish this week, because Thanksgiving is busy enough.

**Green beans with shallots and almonds** · Deep Pan Pro · 10 minutes
1. Blanch 1 lb green beans for 3 minutes. Drain.
2. Soften 2 sliced shallots in a little butter in the Deep Pan Pro.
3. Beans back in, a squeeze of lemon, a handful of toasted almond slivers.
4. Fridge. On Thursday, lowest heat in the same pan while the turkey rests. It holds for 30 minutes.

Pure titanium cooking surface, no coatings, straight into the dishwasher after.

[Shop the Deep Pan Pro]
{{FRICTION}}

**This week's Black Friday prices**
- Deep Pan Pro · `{{FROM:deep}}` · "Higher sides for sauces, pasta and one-pan dinners."
- Pan Pro Large · `{{WAS:large}} {{PRICE:large}}` · "Room for the whole family."
- 6-piece set · `{{WAS:set6}} {{PRICE:set6}}` · "Mini, Small and Large, each with its own lid." · sticker JUST ARRIVED
- 12-piece set · `{{WAS:set12}} {{PRICE:set12}}` · "The whole kitchen. Plus a free Pizza Steel." [VRAAG FLORIS: pizza steel] · sticker JUST ARRIVED

Onder het raster: `The sets just arrived and they're selling fast.`

**Gifts**
Kop: `4 gifts with every order`
Free shipping {{GIFTS:ship}} · Plastic-Free Home e-book {{GIFTS:ebook}} · Mystery gift {{GIFTS:mystery}} · Chance to win {{GIFTS:filterline}} (weekly draw)

**Review:** "The Deep Pan Pro is my 'go to' favourite because I like to cook big meals" · M. K., verified buyer

[Get my Black Friday price] → /collections/black-friday-sale
{{FRICTION}}
`Up to 70% off. Ends Monday, November 30.`

Benjamin
Founder, Siraat

### E5 C · INT

Benjamin here. One side dish this week, because a big dinner is busy enough.

**Green beans with shallots and almonds** · Deep Pan Pro · 10 minutes
1. Blanch 500 g green beans for 3 minutes. Drain.
2. Soften 2 sliced shallots in a little butter in the Deep Pan Pro.
3. Beans back in, a squeeze of lemon, a handful of toasted almond slivers.
4. Fridge. On the day, lowest heat in the same pan while everything else rests. It holds for 30 minutes.

Pure titanium cooking surface, no coatings, straight into the dishwasher after.

[Shop the Deep Pan Pro]
Free shipping, duties paid. 30-day returns. 100,000+ happy customers.

**This week's Black Friday prices** (kaarten zonder bedragen)
- Deep Pan Pro · `Up to 70% off` · "Higher sides for sauces, pasta and one-pan dinners."
- Pan Pro Large · `70% off` · "Room for the whole family."
- Pan Pro Standard · `70% off` · "The size most kitchens start with."
- 6-piece set · `Up to 70% off` · "Mini, Small and Large, each with its own lid." · sticker JUST ARRIVED

Onder het raster: `The 6-piece set just arrived and it's selling fast.`

**Gifts**
Kop: `4 gifts with every order`
Free shipping, duties paid · Plastic-Free Home e-book · Mystery gift · Chance to win a PFAS water filter (weekly draw)
Let op: `{{BLOCK:gifts5}}` toont standaard de lokale gift-waarde per markt (£55, €70 ...). INT mag geen bedragen, dus hier de variant zonder bedragen: onder elk beeld "Included", bij de filter "Chance to win".

**Review:** R399 Anthony: "My deliveries were prompt and I live in Melbourne, Australia... I love their titanium cookware"

[Get my Black Friday price]
Free shipping, duties paid. 30-day returns. 100,000+ happy customers.
`Up to 70% off. Ends Monday 30 November.`

Benjamin
Founder, Siraat

Opmerking: 6-piece set INT staat in GB op £309 bij £1,030 (70%), maar check per markt; daarom "Up to 70% off".

---

# E6 · wo 11 nov · Founder letter (Pan Pro Standard)

Pijler 3 (built for life) met bewijs uit pijler 1. Platte brief binnen vaste header en footer (founder-notes halen 1,3% klik, PLAYBOOK 1). Segment E90 minus Pan Pro Standard-kopers.

Prijzen US (catalogus 31 okt): Pan Pro Standard {{PRICE:standard}} = $144, {{WAS:standard}} = $480, dus precies 70% off en {{SAVE:standard}} = $336.

**Veterans Day-regel (alleen US, eerste regel van de brief, alle drie varianten):**
`First, for Veterans Day: thank you to everyone who serves and has served.`

## E6 · Variant A · Founder-brief, persoonlijk en specifiek

**Invalshoek:** waarom Benjamin deze pan maakte. Van titanium snijplanken naar de vraag "kun je op titanium koken zonder coating erop?", de eerste orders op 20 december 2024, 100,000+ klanten in iets meer dan een jaar. De pan is de held, het aanbod volgt rustig. Platte tekst, één beeld.

**Onderwerp**
- A (specificiteit): `December 20, 2024`
- B (curiosity + benefit): `Why this pan came first`

**Preview:** `The original hammered titanium pan, and why it's 70% off this week.`
INT: zelfde onderwerpen en preview.

**Blokopbouw**

| # | Blok | Inhoud | Knop |
|---|---|---|---|
| 0 | Topbar | BLACK FRIDAY SALE IS LIVE | |
| 1 | Vaste header | | |
| 2 | Brief (live tekst, links uitgelijnd binnen 600 px) | geen hero; één foto halverwege | |
| 3 | Beeld 1200x900 | Pan Pro Standard, close-up van het hamerpatroon (echte foto) | |
| 4 | Brief vervolg + aanbod in de tekst | | `Get my Pan Pro at 70% off` |
| 5 | Twee reviews als citaat in de brief | R411 + R138 | |
| 6 | Ondertekening + P.S. | | |
| 7 | Kleine letters, vaste footer | | |

### E6 A · US

First, for Veterans Day: thank you to everyone who serves and has served.

Benjamin here. I want to tell you how the Pan Pro Standard happened.

Siraat didn't start with pans. We started with titanium cutting boards. And the question that came after was obvious: could you cook on titanium too, with nothing coated on top of it?

[VRAAG FLORIS: detail. Eén echte zin van Benjamin, bijvoorbeeld welke pan hij weggooide of wat hem aan coatings stoorde.]

The Pan Pro was the answer. A pure titanium cooking surface, a hammered pattern, no coatings of any kind. We shipped the first orders on December 20, 2024. Since then, more than 100,000 people have bought from us, in a little over a year. Others started hammering titanium after that. This was the first one.

(beeld: hamerpatroon close-up)

Here's what I like most about it. There's no coating on it, so there's nothing to wear thin and nothing to peel. It goes in the dishwasher. Metal spatulas are fine. And we had it tested: Light Labs, an ISO/IEC 17025-accredited lab, checked it for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895, and you can read it yourself.

The one thing it asks of you is heat. Medium for 2 to 3 minutes, until a drop of water balls up and glides, then a teaspoon of oil. Cold metal grabs your food, hot metal lets it go.

This week the Pan Pro Standard is {{PRICE:standard}}, down from {{WAS:standard}}. That's 70% off, and every order comes with 4 gifts: free shipping, the Plastic-Free Home e-book, a mystery gift, and a weekly chance to win {{GIFTS:filterline}}.

[Get my Pan Pro at 70% off] → /products/original-siraat-100-pure-titanium-pan-with-hammered-pattern
{{FRICTION}}

Two people who said it better than I can:

"I purchased the hammered pro pan standard. It is beautiful and lightweight." Deb, verified buyer

"I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns." Tammy, verified buyer

And it's covered for 75 years.

Benjamin
Founder, Siraat

P.S. 30-day returns, counted from the day the box arrives. The sale ends Monday, November 30.

### E6 A · INT

Benjamin here. I want to tell you how the Pan Pro Standard happened.

Siraat didn't start with pans. We started with titanium cutting boards. And the question that came after was obvious: could you cook on titanium too, with nothing coated on top of it?

[VRAAG FLORIS: detail]

The Pan Pro was the answer. A pure titanium cooking surface, a hammered pattern, no coatings of any kind. We shipped the first orders on 20 December 2024. Since then, more than 100,000 people have bought from us, in a little over a year. Others started hammering titanium after that. This was the first one.

(beeld)

Here's what I like most about it. There's no coating on it, so there's nothing to wear thin and nothing to peel. It goes in the dishwasher. Metal spatulas are fine. And we had it tested: Light Labs, an ISO/IEC 17025-accredited lab, checked it for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895, and you can read it yourself.

The one thing it asks of you is heat. Medium for 2 to 3 minutes, until a drop of water balls up and glides, then a teaspoon of oil. Cold metal grabs your food, hot metal lets it go.

This week the Pan Pro Standard is 70% off, and every order comes with 4 gifts: free shipping with duties paid, the Plastic-Free Home e-book, a mystery gift, and a weekly chance to win a PFAS water filter.

[Get my Pan Pro at 70% off]
Free shipping, duties paid. 30-day returns. 100,000+ happy customers.

Two people who said it better than I can:

"I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns." Tammy, verified buyer

"My deliveries were prompt and I live in Melbourne, Australia... I love their titanium cookware" Anthony, verified buyer

And it's covered for 75 years.

Benjamin
Founder, Siraat

P.S. 30-day returns, counted from the day the box arrives. The sale ends Monday 30 November.

---

## E6 · Variant B · "The last pan": coating tegen puur titanium

**Invalshoek:** het rekenkundige argument zonder getallen te verzinnen. Een gecoate pan is een pan met een einddatum, want de coating slijt met gebruik; puur titanium heeft niets om te verliezen. Bewijs: vergelijkingstabel (categorie, nooit merk), de 75-jarige garantie met wat hij dekt, en een klant die zelf "the last pans" zegt. Wij beloven geen levensduur, de klant zegt het en de garantie bewijst het.

**Onderwerp**
- A (story, letterlijk citaat): `"The last pans we ever have to purchase"`
- B (vraag): `How many pans have you thrown out?`

**Preview:** `Why a coated pan has an end date, and this one has a 75-year warranty.`
INT: zelfde.

**Blokopbouw**

| # | Blok | Inhoud | Knop |
|---|---|---|---|
| 0 | Topbar | BLACK FRIDAY SALE IS LIVE | |
| 1 | Vaste header | | |
| 2 | Hero 1200x1200 | Pan Pro Standard. Label `BENJAMIN'S NOTE` / `A pan with|no end date.` / subline `Covered for 75 years.` Aanbodbalk US `70% OFF  ·  {{GIFTS:TOTAL}}`, INT `70% OFF  ·  4 GIFTS WITH EVERY ORDER` | |
| 3 | Brief, deel 1 | het argument | `Get my Pan Pro at 70% off` |
| 4 | Vergelijking `{{BLOCK:vs kind="pfas"}}` | kop `Your next pan vs a coated pan`, 5 rijen hieronder | |
| 5 | Garantieblok | wat 75 jaar dekt | |
| 6 | Reviews | R583 + R240 | |
| 7 | Aanbod (`{{BLOCK:offer}}`) | prijs US, gifts | `Get my Pan Pro at 70% off` |
| 8 | Ondertekening, P.S., kleine letters, vaste footer | | |

**Vergelijkingsrijen** (uit research/ux-round2/comparisons.md tabel A, categorie "Coated nonstick", geen merken)

| Siraat Titanium | Coated nonstick |
|---|---|
| Pure titanium surface | A PTFE or ceramic coating |
| No coating to wear off | Coating wears with use |
| Metal utensils welcome | Wood or silicone advised |
| Third-party tested by Light Labs | Testing varies by brand |
| Dishwasher safe | Hand wash advised |

Rij 4 is bewust de zachte variant. De scherpere "Lab tested PFAS-free / PTFE is itself a PFAS" mag alleen na akkoord van Floris (comparisons.md: risico middel). Voetnoot: `Light Labs report no. 25895: 31 PFAS compounds tested, all below detection.`

### E6 B · US

First, for Veterans Day: thank you to everyone who serves and has served.

Benjamin here. A quick question before the sale stuff: how many frying pans have you thrown out?

Most people I talk to can count a few. Not because they cooked wrong. Because a coated pan wears with use, and once the coating starts to go, the pan is done. That's the deal with coatings. They come with an end date nobody prints on the box.

The Pan Pro Standard doesn't have that problem, because there's nothing on it to lose. The cooking surface is pure titanium, with no coatings of any kind. No coating means nothing to wear thin, nothing to peel, nothing to baby. Metal spatula, dishwasher, Tuesday night, all fine.

[Get my Pan Pro at 70% off]
{{FRICTION}}

(vergelijkingstabel)

I'm not going to tell you how many years it lasts. I'll tell you what we put in writing instead: a 75-year warranty. If it dents, if the base warps, if a handle or rivet comes loose, or if the lid stops fitting, we take care of it.

One customer sent us a photo and that was it:

"Siraat replaced a pan free of charge... I just sent them the picture and they honored the warranty." Brandon W., verified buyer

And another said the thing I'd never write myself:

"These hammered Titanium pans from Siraat have been the best we have owned yet... the last pans we ever have to purchase." Scott Y., verified buyer

**Aanbodblok**
Pan Pro Standard
`{{WAS:standard}}  {{PRICE:standard}}` · You save {{SAVE:standard}}
Plus 4 gifts with every order: free shipping, the Plastic-Free Home e-book, a mystery gift, and a weekly chance to win {{GIFTS:filterline}}.
Tested free from PFAS by Light Labs, report no. 25895.
[Get my Pan Pro at 70% off]
{{FRICTION}}

Benjamin
Founder, Siraat

P.S. Changed your mind after it arrives? Unused, within 30 days of delivery, you get a full refund. The sale ends Monday, November 30.

### E6 B · INT

Benjamin here. A quick question before the sale stuff: how many frying pans have you thrown out?

Most people I talk to can count a few. Not because they cooked wrong. Because a coated pan wears with use, and once the coating starts to go, the pan is done. That's the deal with coatings. They come with an end date nobody prints on the box.

The Pan Pro Standard doesn't have that problem, because there's nothing on it to lose. The cooking surface is pure titanium, with no coatings of any kind. No coating means nothing to wear thin, nothing to peel, nothing to baby. Metal spatula, dishwasher, a busy weeknight, all fine.

[Get my Pan Pro at 70% off]
Free shipping, duties paid. 30-day returns. 100,000+ happy customers.

(vergelijkingstabel)

I'm not going to tell you how many years it lasts. I'll tell you what we put in writing instead: a 75-year warranty. If it dents, if the base warps, if a handle or rivet comes loose, or if the lid stops fitting, we take care of it.

One customer sent us a photo and that was it:

"Siraat replaced a pan free of charge... I just sent them the picture and they honored the warranty." Brandon W., verified buyer

And another said the thing I'd never write myself:

"These hammered Titanium pans from Siraat have been the best we have owned yet... the last pans we ever have to purchase." Scott Y., verified buyer

**Aanbodblok (zonder bedragen)**
Pan Pro Standard · 70% off
Plus 4 gifts with every order: free shipping with duties paid, the Plastic-Free Home e-book, a mystery gift, and a weekly chance to win a PFAS water filter.
Tested free from PFAS by Light Labs, report no. 25895.
[Get my Pan Pro at 70% off]
Free shipping, duties paid. 30-day returns. 100,000+ happy customers.

Benjamin
Founder, Siraat

P.S. Changed your mind after it arrives? Unused, within 30 days of delivery, you get a full refund. The sale ends Monday 30 November.

Let op: "No coating means nothing to wear thin, nothing to peel" is een "Nothing to X"-tic (skill 9: rantsoeneren). Hij staat alleen in deze variant.

---

## E6 · Variant C · Kort en hard: de Pan Pro Standard met waardestapel

**Invalshoek:** most aware, dus het aanbod mag voorop. Hero met prijs (US) of 70% (INT), daaronder meteen de knop, dan de waardestapel als bonnetje, drie bewijsregels, twee reviews, de twee beloftes. Ongeveer 150 woorden lopende tekst. Voor wie de pan al kent en op de sale wachtte.

**Onderwerp**
- A (aanbod): `The original pan, 70% off`
- B (specificiteit): `1 pan, 4 gifts, 75-year warranty`

**Preview:** US `{{PRICE:standard}} for the Pan Pro Standard. Ends November 30.` (als macro's in de preview niet werken: `$144 for the Pan Pro Standard. Ends November 30.`) · INT `70% off the Pan Pro Standard, plus 4 gifts. Ends 30 November.`

**Blokopbouw**

| # | Blok | Inhoud | Knop |
|---|---|---|---|
| 0 | Topbar | BLACK FRIDAY SALE IS LIVE | |
| 1 | Vaste header | | |
| 2 | Hero 1200x900 (4:3) | packshot Pan Pro Standard. Label `BLACK FRIDAY` / `The original pan.|70% off.` / subline in het beeld `Plus 4 gifts. Ends Nov 30.` (INT `Plus 4 gifts. Ends 30 Nov.`); de prijs US `{{WAS:standard}} {{PRICE:standard}}` als live tekst direct onder het beeld, niet in het beeld (prijs per markt). Aanbodbalk `70% OFF  ·  4 GIFTS WITH EVERY ORDER` | |
| 3 | Knop direct onder de hero | | `Get my Pan Pro at 70% off` |
| 4 | Korte brief (3 alinea's) | | |
| 5 | Waardestapel (bonnetje) | US met bedragen, INT met "Included" | |
| 6 | Drie iconregels | titanium, Light Labs, 75 jaar | |
| 7 | Reviews | R169 + R011 | |
| 8 | "Two promises" | retour en defect | `Get my Pan Pro at 70% off` |
| 9 | Ondertekening, kleine letters, vaste footer | | |

### E6 C · US

First, for Veterans Day: thank you to everyone who serves and has served.

Benjamin here. Short one today.

The Pan Pro Standard is the original hammered titanium pan. Pure titanium cooking surface, no coatings. Right now it's {{PRICE:standard}} instead of {{WAS:standard}}. That's 70% off, the lowest price we've put on it this year [VRAAG FLORIS: klopt "lowest this year"? Anders schrappen].

If it's been on your list for a while, this is the week.

**Waardestapel**
| | |
|---|---|
| Titanium Hammered Pan Pro Standard | ~~{{WAS:standard}}~~ {{PRICE:standard}} |
| Free shipping | {{GIFTS:ship}} included |
| Plastic-Free Home e-book | {{GIFTS:ebook}} included |
| Mystery gift | {{GIFTS:mystery}} included |
| Weekly chance to win {{GIFTS:filterline}} | entered with your order |
| 75-year warranty | included |
| 30-day returns | included |
| **Value** | **{{STACK:standard}}** |
| **Your price** | **{{PRICE:standard}}** |

**Iconregels**
- A pure titanium cooking surface, no coatings
- Tested free from PFAS by Light Labs, report no. 25895
- Covered for 75 years

**Reviews**
- "The real test was my egg the next morning... the egg released completely and slid around the pan like it was non-stick." Michael G., verified buyer
- "We have purchased twice from Siraat... Expensive but definitely Value for money. Quality cookware!" Lorraine, verified buyer

**Two promises**
Changed your mind? Send it back unused within 30 days of delivery for a full refund.
Something wrong? Damaged or defective in the first 30 days, we refund or replace it and pay the shipping. After that, the 75-year warranty takes over.

[Get my Pan Pro at 70% off]
{{FRICTION}}

The sale ends Monday, November 30.

Benjamin
Founder, Siraat

### E6 C · INT

Benjamin here. Short one today.

The Pan Pro Standard is the original hammered titanium pan. Pure titanium cooking surface, no coatings. Right now it's 70% off [VRAAG FLORIS: "the lowest price we've put on it this year" ook INT?].

If you've had it in your cart for a while, this is the week.

**Waardestapel (zonder bedragen)**
| | |
|---|---|
| Titanium Hammered Pan Pro Standard | 70% off |
| Free shipping, duties paid | included |
| Plastic-Free Home e-book | included |
| Mystery gift | included |
| Weekly chance to win a PFAS water filter | entered with your order |
| 75-year warranty | included |
| 30-day returns | included |

**Iconregels:** als US.

**Reviews**
- "The real test was my egg the next morning... the egg released completely and slid around the pan like it was non-stick." Michael G., verified buyer
- "We have purchased twice from Siraat... Expensive but definitely Value for money. Quality cookware!" Lorraine, verified buyer

**Two promises:** als US.

[Get my Pan Pro at 70% off]
Free shipping, duties paid. 30-day returns. 100,000+ happy customers.

The sale ends Monday 30 November.

Benjamin
Founder, Siraat

Opmerking hero C: de live prijsregel onder het beeld is `{{WAS:standard}} {{PRICE:standard}}` met de eerste prijs doorgestreept (compare-at uit Shopify).

---

## 2. Reservelijst onderwerpen (skill: vijf typen per mail)

E5: `Make it Tuesday, serve it Thursday` (specificiteit) · `The Thanksgiving side that's better reheated` (curiosity + benefit) · `What can you cook before Thursday?` (vraag) · `"My 'go to' favourite"` (story, R562) · `A Thanksgiving side + up to 70% off` (aanbod).

E6: `December 20, 2024` (specificiteit) · `Why this pan came first` (curiosity + benefit) · `How many pans have you thrown out?` (vraag) · `"The last pans we ever have to purchase"` (story, R583) · `The original pan, 70% off` (aanbod).

Testadvies: per mail één variabele. E5: A tegen C (rijk recept tegen kort + sale) op unieke kliks en omzet per ontvanger. E6: A tegen B is een principetest (liking/autoriteit tegen sociale bewijskracht + garantie).

## 3. Gecontroleerde claims

| Claim | Status | Bron |
|---|---|---|
| Pure titanium cooking surface + no coatings (altijd samen) | approved | claims.csv, PLAYBOOK 1 |
| Tested free from PFAS by Light Labs, ISO/IEC 17025, report no. 25895, 31 PFAS compounds, below detection limit | approved, geldt voor alle pannen | claims.csv r42, DECISIONS 7 okt |
| The original hammered titanium pan, first orders December 20, 2024 | owner override | claims.csv, DECISIONS 1 okt |
| Siraat begon met titanium snijplanken; 100,000+ in iets meer dan een jaar | PLAYBOOK 1, brand | |
| 75-year warranty, dekking (deuk, kromme bodem, losse greep of klinknagel, deksel past niet) | owner override | DECISIONS 1 okt, skill 3 |
| 30-day returns (ongebruikt, binnen 30 dagen na levering) | owner override | DECISIONS 1 okt |
| Free shipping (US "from the US"), INT "duties paid" | approved | DECISIONS 8 okt |
| 100,000+ happy customers | approved | DECISIONS 7 okt |
| Dishwasher safe, metal utensil safe | approved | claims.csv |
| Up to 70% off, 4 gifts blijven in november | approved | DECISIONS 19 okt, 31 okt |
| Gift-waarden US $15/$30/$25, filter $450 als kans | approved | DECISIONS 8 okt, PLAYBOOK v5 |
| Pan Pro Standard $144 bij $480 (70%), Large $149 bij $497, set6 $299, set12 $649 bij $2,047 | catalogus 31 okt | products.json |
| "Just arrived and selling fast" alleen bij 6- en 12-delige set | approved | DECISIONS 1 nov |
| Gratis Pizza Steel bij 12-delige set | **niet in DECISIONS** | alleen Homestead-tekst |
| "Lowest price this year" (E6 C) | **niet gecontroleerd** | [VRAAG FLORIS] |
| Vermeden: non-stick als claim, lifetime, for life, scratch-proof, levensduur in jaren, oventemperatuur, levertijden, "purifier", "free filter", merknamen, next batch, reserve | | skill 3, DECISIONS 1 nov |

Controle: geen gedachtestreepje of en-streepje in dit bestand (grep U+2014 en U+2013 = 0).
