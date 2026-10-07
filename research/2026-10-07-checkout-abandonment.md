# Checkout abandonment · deep research en voorstel

Datum: 7 oktober 2026. Bronnen: Klaviyo API (flows Y2TmNB, Tsg2tV, SwkMyn, TBWngE, metrics september 2026), templates gerenderd, Shopify-kortingscodes via Replo, Email Love (12 mails volledig bekeken: Le Creuset, Our Place, Great Jones, Brooklinen, Cuisinart, Ridge, Casper, Solo Stove).

## 1. Wat er nu draait

Drie flows raken dezelfde persoon, gebouwd door Homestead in december 2025:

| Flow | Trigger | Structuur | 30 dagen |
| --- | --- | --- | --- |
| Y2TmNB "EB · Checkout Abandonment" | Checkout Started (RfMvni) | Split 50/50. Helft A: nog eens gesplitst, 25 procent krijgt 4 mails (10 min, +1d 08:00, +2d, +1d), 25 procent krijgt maar 1 mail na 30 min. Helft B: 5 mails (10 min, +1d, +1d, +2d, +1d). Geen order sinds start, niet in flow in 10 dagen. | 5.335 ontvangers, $12.798, $2,48 per ontvanger, 1,2 procent uitschrijving |
| Tsg2tV "Triple Pixel Checkout" | Triple Whale checkout (RtgBgs) | 50 procent 4 mails, 50 procent 1 mail | 3.255 ontvangers, $4.975 |
| SwkMyn "Cart Abandonment" | Added to Cart (QXcV8K) | 50 procent: 15 min "we saved these for you", +2d "10% off", +1d "Last call 10% off". 50 procent: 1 mail na 30 min | 9.227 ontvangers, $18.555, $2,02 per ontvanger |
| TBWngE (cart, klein) | | | 1.285 ontvangers, $144 |

Samen ongeveer $36.000 per maand uit abandonment, op een omzet van $1,08 miljoen (september). Eerste checkout-mail "New AB Checkout 1" doet $8,41 per ontvanger, de beste mail in het hele account.

**Volumes september:** Checkout Started 10.233 events bij 6.770 unieke profielen, Placed Order 5.102 orders bij 4.907 unieke klanten. Netto ongeveer 2.000 unieke achterlaters per maand. De flows bereiken er ongeveer 1.750 met een eerste mail.

### Wat er mis is

1. **De helft van de achterlaters krijgt maar één mail.** De "1 mail na 30 minuten"-tak is een A/B-test die Homestead nooit heeft afgesloten. Dat is de grootste lek: mail 2 en 3 zijn precies waar de koper overtuigd wordt.
2. **Drie flows overlappen.** Iemand die een product in de cart legt en naar checkout gaat, zit in cart-flow én checkout-flow én (als de pixel vuurt) Triple Pixel-flow. Geen enkele flow sluit de andere uit. Dat verklaart de 1,2 procent uitschrijving en deels de klachten over "te veel mails".
3. **Alles is beeld.** De templates zijn SYSTEM_DRAGGABLE met beeldslices en één dynamisch line-items-blok. Geen live tekst, dus geen dark mode, geen dynamische bedragen, slecht leesbaar op Gmail met afbeeldingen uit.
4. **De korting is inconsistent.** Checkout-mails: geen code, alleen "30,000 happy customers". Cart-mails 2 en 3: "Your Cart + 10% Off" met code COOKHAPPY (187 keer gebruikt). Mail "VPBrLr" noemt "Prime Time Sale up to 56% off". Ondertussen draait de site altijd 41 tot 50 procent plus mystery gift. De 10 procent komt daar bovenop (Shopify-code stapelt op compare-at prijs), zonder limiet, zonder einddatum.
5. **Het merk ontbreekt.** Copy is generiek ("professional grade tools", "anti-microbial, knife-friendly"). Geen oprichter, geen "no coatings", geen "pure titanium cooking surface", geen 100-day trial als argument, geen echte review met naam. "30,000 customers" terwijl de brand guidelines 100.000+ zeggen.
6. **Fouten in copy.** "kitchen wear" in plaats van "kitchenware", "Non-stick" in een kaartje terwijl we juist geen coating hebben (de guidelines verbieden "non-stick" als claim).

## 2. Wat de beste merken doen (Email Love)

Vast patroon: drie mails in 48 tot 72 uur.

| Mail | Timing | Rol | Voorbeelden |
| --- | --- | --- | --- |
| 1 | 1 tot 4 uur | Neutrale herinnering, dynamisch cart-blok, geen nieuwe korting | Great Jones "Forgetting something?", Brooklinen "Looks like you forgot your cart" |
| 2 | +24 uur | Reden om te geloven: reviews, garantie, bezwaren wegnemen | Casper "Why Casper?", Solo Stove "Need a final opinion on that item?" |
| 3 | +48 tot 72 uur | Deadline of aanbod | Cuisinart "Final call to save 15%", Brooklinen "We can't hold your cart forever" |

Over korting:
- Premium merken (Le Creuset, Great Jones, Casper) geven geen procent in mail 1 en 2. Le Creuset geeft alleen gratis verzending.
- Massamerken (Cuisinart, Ridge, DreamCloud) beginnen direct met 10 tot 20 procent.
- Manieren om korting groot te maken zonder mensen te leren dat afhaken loont: (a) de korting die al in de cart zit tonen als "je liet $X aan korting liggen" (DreamCloud), (b) auto-apply aan de checkout, geen deelbare code (Brooklinen), (c) code pas in mail 3 met harde einddatum en eenmalig gebruik (Cuisinart), (d) waarde in plaats van marge: gratis gift, gratis verzending, Klarna/Shop Pay (Our Place, Solo Stove).

Beste onderwerpregels gezien: "Forgetting something?", "We can't hold your cart forever", "Need a final opinion on that item?", "Why Casper?" met preview "Well, how much time do you have?", "Still thinking it over? Save up to 60% on your cart", "Final call to save 15% on your cart", "Someone left this review:", "So about this 20% off?".

## 3. Voorstel Siraat: "zwaar op wie wij zijn, zwaar op de korting"

Eén nieuwe flow die de drie oude vervangt. Vier mails in 72 uur. Elke mail heeft twee lagen: bovenin het cart-blok met de korting in dollars, onderin één merkverhaal.

### Trigger en filters
- Trigger: Checkout Started (RfMvni). Cart-flow apart houden maar met filter "geen Checkout Started sinds flow-start", zodat niemand in beide zit. Triple Pixel-flow uitzetten (dubbel van checkout).
- Profile filter: Placed Order gelijk aan 0 sinds flow-start; niet in deze flow in 14 dagen; niet in cart-flow in 3 dagen.
- Smart sending uit (anders blokkeert de welcome flow mail 1).
- Re-entry: 14 dagen.

### De vier mails

| # | Timing | Onderwerp (A) | Onderwerp (B, test) | Preview | Hoofdblok | Merkblok |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 uur, direct | Forgetting something? | Your pan is still here | You left {{ savings }} in savings sitting in your cart | Cart-blok: product, aantal, doorgestreepte prijs, prijs nu, "You save $X". CTA "Return to checkout". | Trust-strip: no coatings, 100-day trial, lifetime warranty, free shipping. |
| 2 | +23 uur (dag 2, 09:00 lokale tijd) | Why Siraat? | Need a second opinion on that pan? | Well, how much time do you have? | Cart-blok klein. CTA "Go to my cart". | Vier blokken: "No coatings, ever. A pure titanium cooking surface. Nothing to flake, nothing to wear off." / "Cook with it for 100 days. Not the best pan you own? Send it back." / "Lifetime warranty, because there is no coating to fail." / Eén echte review met naam (Marilyn B., Michael G. of Jeanne K. uit voice-of-customer). Afsluiting door de oprichter. |
| 3 | +24 uur (dag 3) | Your cart is still at today's price | Someone left this review: | We are holding it at {{ savings }} off for 24 more hours | Cart-blok met "reserved at today's price until {tomorrow}". CTA "Complete my order". | "Why there is no coating": de 3-laags opbouw (0,5 mm puur titanium, aluminium kern, rvs bodem), gevolgd door Trustpilot-score en aantal reviews. |
| 4 | +24 uur (dag 4, laatste) | Final call: your cart and your gift | Last chance before it goes back on the shelf | Complete your order tonight and the mystery gift is in the box | Cart-blok. Daaronder de gift-stack van de maand (oktober: 4 gifts, tot 50 procent). CTA "Finish my order". | Korte oprichtersnoot: waarom hij geen coatings meer wilde in zijn keuken. Daarna "Questions about titanium? Reply to this email." |

### Hoe de korting groot en toch gezond is
- De korting is de **evergreen 41 tot 50 procent plus de gifts**, getoond in dollars per cart ("You save $187"). Dat is groot, eerlijk en traint niemand om af te haken: je krijgt niets extra's door te wachten.
- Geen 10 procent code meer in de flow. COOKHAPPY en HI10 zijn onbeperkt en zonder einddatum; die lekken nu 10 procent marge bovenop de 41 procent. Afhalen uit flows (ook de cart-flow), ongeldig maken in Shopify.
- Urgentie via "reserved at today's price" en "gift expires", geen fake countdown.
- Een extra 5 procent eenmalige code alleen in een **winback 7 dagen later buiten de flow**, zonder sets die al op 50 procent staan. Dit testen als aparte flow in november.

### Uitsluitingen
- 12-delige set in backorder: in alle mails geen leverbelofte op die set. Mail 4 ("back on the shelf") niet sturen aan carts met de 12-delige set; daarvoor een variant "Your set is reserved, delivery in week X".
- Klanten met een order in de laatste 30 dagen krijgen mail 1 wel, mail 2 tot 4 niet (ze kennen het merk al).

### A/B-tests, in volgorde
1. Mail 1 onderwerp: "Forgetting something?" tegen "Your pan is still here". Winnaar op unieke klik.
2. Mail 4: met gift-deadline tegen zonder deadline. Winnaar op omzet per ontvanger.
3. Daarna timing mail 1: 1 uur tegen 4 uur.

### Verwachte impact
Huidig: ongeveer 1.750 bereikte achterlaters per maand, de helft krijgt 1 mail. Als iedereen 4 mails krijgt en mail 2 en 3 de helft van de omzet per ontvanger van mail 1 halen, is de conservatieve schatting +$8.000 tot $12.000 per maand bovenop de huidige $18.000 uit checkout plus Triple Pixel. Werkelijke lift pas na 30 dagen meten.

## 4. Bouwplan

1. Vier HTML-templates in de Siraat DS-stijl (live tekst, Instrument Serif koppen, cart-blok met Klaviyo `event.extra.line_items`, savings berekend uit compare_at_price en price).
2. Figma-bestand "Checkout Flow v2" met flow-diagram en vier mails, zoals Welcome Flow v2.
3. Flow via API aanmaken als draft met filters, delays, ab-test op mail 1.
4. Floris keurt copy en beeld goed, zet de flow live.
5. Dag 1: oude Y2TmNB en Tsg2tV op draft, cart-flow filteren. Dag 7: cijfers in Slack.
6. Dag 30: rapport, A/B-winnaar vastzetten, test 2 starten.

Open vragen voor Floris: (1) oprichtersnaam in de mails, Floris of Benjamin; (2) mogen de 10 procent codes COOKHAPPY en HI10 uit de flows; (3) levertijd 12-delige set voor de variant van mail 4.
