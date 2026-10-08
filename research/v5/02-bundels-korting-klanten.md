# 02 · Bundels, kortingstiming en bestaande klanten (v5, fase 1: ontwerp)

Stand 8 oktober 2026, middag. Rol: logica-agent. Alleen gelezen: Shopify Admin API (producten, prijzen per markt, kortingscodes, ShopifyQL) en Klaviyo (events Placed Order, Checkout Started, Added to Cart, Ordered Product; flow-values-report). Niets gewijzigd in Shopify, Klaviyo, templates of flows. Ruwe events alleen in de scratchpad (geen e-mailadressen; profiel-ID's niet in de repo).

Bronnen: `DECISIONS.md`, `research/v5/00-feedback-floris.md`, `klaviyo/flows/v4-flow-system.md`, `scripts/build_flows.py`, `content/facts/shopify-titles.csv` en `products.csv`, `research/tailoring/10-productmatrix.md`, `research/personalisatie/01-voorstel.md`, `research/history/01-beste-mails.md` (+ `flow-messages-all.csv`), `research/timing/01-data.md`, `research/testing/06-meetplan-v4.md`.

## Kort (voor Floris)

1. **Brekend, vandaag:** de BDAY-listing van de 6-delige set (`...-6-pcs-bday-sale`, $349) staat sinds vanochtend op DRAFT en geeft een **404**. Acht templates linken ernaar en noemen $349: C3-P, W4-US, W4-INT, A2, R2, R2-nocode, R2-VIP (+nocode), N2 (+nocode). De fall sale zit op de hoofdlisting `titanium-hammered-pan-set-with-lids-6-pcs`: **$299, compare-at $598** (GBP 249, EUR 279, AUD 449, CAD 449, SGD 409, NZD 549, HKD 2.382). Fix: link naar de hoofdlisting, $349 wordt $299, rekensom opnieuw (sectie 1.3). Ook DECISIONS-regel "6-delige set = $349" bijwerken.
2. **Bundels routen op product, niet op $value.** Nu krijgt alles in `SET_TITELS` of met $value ≥ $300 dezelfde C3-S ("a lid for every pan, all three"). Dat klopt alleen voor de 6-delige set. Voorstel: één C3-S-template met een bundelblok per bundel (inhoud, rekensom, volgende stap) via `event.Items`, plus een routeringsfix: starterbundels (Duo, Kit, 2+2) en losse pannen tussen $250 en $300 naar C3-P (upgrade naar de $299-set). Nu krijgt een cart van Small + Large los ($286) géén C3.
3. **Kortingstiming:** [CIJFERS, sectie 2]. Advies cart: geen 10% in K1. K1 = cart + 4 gifts die verlopen + garantie; K2 (dag 1) bewijs en rekensom; 10% pas in K3 (dag 3, eigen code, 48 uur). Checkout volgt het besluit (HI10 in C1-C3), maar met gifts vooraan en HI10 als tweede regel.
4. **Bestaande klanten:** de template ziet alleen het trigger-event. Wat iemand eerder kocht kan alleen via (a) flowsplits/verzendfilters op Placed Order of **Ordered Product (XT7f8Z, met `Variant Name` = dekselmaat)** over all time, of (b) een profielveld (`siraat_owned`) dat een nachtelijke API-job vult (de flow-actie "Update profile property" kan niet via de API, wel in de UI). Ontwerp per geval in sectie 3.
5. **Logica-check:** 31 fixes, waarvan 6 hoog (404-links, P3-SET biedt wok/crêpe aan wie ze al heeft, R2/N2 bieden de set of pan aan die net gekocht is, gift-waarden in USD aan INT, W0 "first egg" aan klanten van een jaar geleden, N1 care-video op dag 182). Sectie 4.

---

## 1. Bundels

### 1.1 Inventaris (Shopify Admin API, 8 okt 2026, 13:45 UTC)

Prijzen USD (shopprijs). Inhoud uit metafield `product.whats_included` of `content/facts/products.csv`. Markten: `products.csv` (Gorgias-guidance) en `contextualPricing`.

| Titel (exact, = `Items` in events) | Handle | Status | Prijs | Compare-at | Inhoud | Markten |
| --- | --- | --- | --- | --- | --- | --- |
| Titanium Hammered Pan Set With Lids \| 6-Pcs | titanium-hammered-pan-set-with-lids-6-pcs | ACTIVE | **$299** (fall sale) | $598 | Pan Pro Mini 20 cm + Small 26 cm + Large 30 cm, elk met deksel; 5 guides | alle |
| Titanium Hammered Pan Set With Lids \| 6-Pcs (BDAY SALE) | ...-6-pcs-bday-sale | **DRAFT (404)** | $349 | $749 | idem | was alle |
| Titanium Hammered Pan Set With Lids \| 6-Pcs SB | ...-6-pcs-sb | DRAFT | $449 | $749 | idem | |
| Titanium Hammered Cookware Set \| 12-Pcs | titanium-hammered-cookware-set | ACTIVE | $599 | $1.186 | 3 pannen 8/10/12″ + 3 deksels, 2 L en 3 L steelpan + stockpot met deksels | **alleen US**; levert in twee delen |
| ... 12-Pcs \| + FREE PIZZA STEEL (EXCLUSIVE) en zonder (EXCLUSIVE) | ...-12-pcs-free-pizza-steel(-1) | DRAFT | $699 | $1.186 | 12-delig + pizza steel | US |
| Titanium Hammered Cookware Set Pro | titanium-hammered-cookware-set-pro | ACTIVE | $479 | $870 | Pan Pro 28 cm, Wok 28 cm, Deep 26 cm, flipper, ladle (**geen deksels**) | alle |
| Titanium Hammered Complete Edition | the-hammered-collection | ACTIVE | $495 | $900 | Pan Pro, Deep, Wok, Crêpe (**geen deksels**) | alle |
| Full Hammered Pro Edition | full-hammered-pro-edition | ACTIVE | $799 | $1.499 | Pan Pro Mini, "Medium", Standard, Large, elk met deksel; flipper, spatula, scooper, ladle | alle |
| The Just Everything Bundle \| 34-Pcs | the-just-everything-bundle-34-pcs | ACTIVE | $1.499 | $2.337 | 12-delig + roasting pan, wok, deep, crêpe, pizza steel, 4 planken, 4 utensils, pizza wheel, grill press, trivet, molens, 4 schorten | **alleen US** (12-delig, roasting) |
| 2 Pans + 2 Lids | 2-pans-and-2-lids | ACTIVE (4 okt) | $199 | geen | 2 pannen + 2 deksels; **welke maten staat nergens** (geen metafield) | alle |
| Titanium Hammered Pan Pro Duo | titanium-hammered-pan-pro-duo | ACTIVE | $229 | $570 | Small 10″ + Standard 11″ | alle |
| Titanium Hammered Pro Duo | titanium-pro-duo | ACTIVE | $199 | $394,95 | Pan Pro 28 cm + flipper | alle |
| Titanium Hammered Pan Pro Kit | titanium-hammered-pan-pro-kit | ACTIVE | $199 | $400 | Pan 26 cm + deksel + flipper | alle |
| Titanium Cook & Prep Bundle | titanium-hammered-pro-prep-cook-set | ACTIVE | $199 | $270 | Pan 28 cm + snijplank L | alle |
| Titanium Hammered Pan Pro & Utensil Set | titanium-hammered-pan-pro-utensil-set | ACTIVE | $249 | $340 | Pan Pro + utensils | alle |
| Titanium Hammered Pot Set With Lids \| 6-Pcs | titanium-hammered-pot-set-with-lids-6-pcs | DRAFT | $399 | $547 | 3 potten + deksels | (US) |
| Accessoirebundels: Utensil Set Bundle $149/$199,95 · Cutting Board Bundle $274/$720 · Salt & Pepper Mill Set $124/$200 | | ACTIVE | | | | alle |
| Wok & Deep Pan Pro / Wok & Deep Pan Set | | DRAFT / ARCHIVED | $229 | $570 | | |

Losse prijzen vandaag (voor rekensommen): Mini $129 · Small $137 · Standard $144 · Large $149 · deksel $59 (alle maten) · Deep vanaf $119 · Wok vanaf $119 · Crêpe $139 · utensil $29 per stuk. Let op: er staan **dubbele ACTIVE listings** met andere prijzen (Standard $157 en Large $169 op de `-copy`-handles, Small-copy $154 UNLISTED). Rekensommen in mails alleen op de hoofdhandles.

Automatische kortingen actief: FREE GIFT (Bxgy, de 4 gifts), 20% OFF, 30% OFF, 3 DEEP PANS - 30%, gratis verzending. HI10: 10%, combineert met niets, **niet** één keer per klant, 1.727 keer gebruikt.

### 1.2 Wat er nu misgaat in de routing

| Waar | Nu (build_flows.py) | Gevolg |
| --- | --- | --- |
| C3-S verzendfilter | `Items` contains-any SET_TITELS **of** $value ≥ 300 | Eén tekst voor alles: "A lid for every pan", "the same titanium surface on all three". Fout voor Complete Edition en Set Pro (geen deksels, 4 of 3 pannen + utensils), 12-delig en 34-delig (potten), Duo/Kit/2+2 (2 pannen of 1 pan) en losse carts ≥ $300. |
| SET_TITELS | bevat Pan Pro Duo, Pro Duo, Pan Pro Kit, 2 Pans + 2 Lids | Starterbundels van $199-229 krijgen "a set settles it" in plaats van de upgrade naar de $299-set. |
| C3-P verzendfilter | PANPRO en $value < 250 en geen set | Cart tussen $250 en $300 (Small + Large los = $286, Standard + deksel + plank) krijgt **geen C3**. Nu de set $299 kost is dat precies de beste upgradegroep. |
| C3-P inhoud | $349, link naar 404-listing, "about $116 a pan" | Prijs en link fout sinds vandaag. |
| P3-SET | toont altijd Crêpe + Wok | Complete Edition (heeft beide), Set Pro en 34-delig (heeft wok) krijgen aangeboden wat in de doos zat. |
| R1-SET | sluit wok uit bij Complete/Set Pro, crêpe bij Complete | Goed, maar 34-delig en Full Hammered Pro ontbreken (34-delig heeft alles). |
| Cart (K) | geen bundelherkenning; K2-new rekent een Pan Pro tegen 15 gecoate pannen | Een set in de cart krijgt de pan-rekensom. |

### 1.3 Ontwerp: een bundelscenario per product

Principe: **de flowsplit kiest de mailsoort (set, upgrade, accessoire), de template kiest het bundelblok.** Klaviyo staat geen samenkomende takken toe (Bouwnotitie 2.1), dus elke extra template betekent een extra verzendfilter; één C3-S met een `{% if %}`-keten houdt de flow klein en de bundels bij elkaar.

**Bundelgroepen (nieuw in build_flows.py, vervangt SET_TITELS voor C3-routing):**

```
SET6_TITELS   = Pan Set With Lids | 6-Pcs, ... (BDAY SALE), ... 6-Pcs SB, Titanium-Hammerpfannenset mit Deckel | 6-teilig
SET12_TITELS  = Cookware Set | 12-Pcs, 12-Pcs | + FREE PIZZA STEEL (2x), 12 pcs cookware set
SETPRO_TITELS = Titanium Hammered Cookware Set Pro
COMPLETE_TITELS = Titanium Hammered Complete Edition, Titanium Hammered – Complete Edition   (titel met en dash zoals in Shopify, exact kopiëren)
FULL_TITELS   = Full Hammered Pro Edition
ALL34_TITELS  = The Just Everything Bundle | 34-Pcs
STARTER_TITELS = Titanium Hammered Pan Pro Duo, Titanium Hammered Pro Duo, Titanium Hammered Pan Pro Kit,
                 2 Pans + 2 Lids, Titanium Cook & Prep Bundle, Titanium Hammered Pan Pro & Utensil Set,
                 Titanium Hammered Wok & Deep Pan Pro, Titanium Hammered Wok & Deep Pan Set
GROOT_SET = SET6 + SET12 + SETPRO + COMPLETE + FULL + ALL34      (vervangt SET_TITELS in C3-S, P3-SET, R1-SET)
```

**Checkout dag 3 (vervangt TS T2a/T2b/T3):**

| Volgorde | Verzendfilter (Checkout Started laatste 4 dagen) | Mail |
| --- | --- | --- |
| 1 | `Items` contains-any GROOT_SET | **C3-S** met bundelblok |
| 2 | geen GROOT_SET **en** (`Items` contains-any STARTER **of** PANPRO) **en** $value < 300 | **C3-P** (upgrade naar de $299-set; drempel van 250 naar 300) |
| 3 | geen GROOT_SET, geen PANPRO/STARTER, $value ≥ 300 (losse vormen, potten, plank + pan) | **C3-S** met het algemene blok (huidige tekst zonder "three"/"a lid for every pan") |
| 4 | rest kookgerei (wok/deep/crêpe/pizza/roast alleen, < $300) | geen C3 (ongewijzigd) |

Cart: K2-new krijgt hetzelfde bundelblok in plaats van de pan-rekensom als `Product Name` een bundel is (keten op `event|lookup:'Product Name'`). Post-purchase en winback: P3-SET en R1-SET gebruiken het "volgende stap"-deel van hetzelfde blok.

**Per bundel: wat er in de doos zit, de rekensom, de volgende stap**

Rekensom = eerlijk: alleen losse prijzen van vandaag en de compare-at uit Shopify; prijzen alleen bij US (`event.extra.presentment_currency == 'USD'` in checkout, `$currency` in cart, `shipping_address.country_code == 'US'` na aankoop). INT krijgt het blok zonder bedragen of met `item.line_price` uit het event (al in hun valuta).

| Bundel | What's in the box (mailtekst, Engels) | Rekensom (US) | Volgende stap in C3 / P3 / R1 |
| --- | --- | --- | --- |
| **Fall sale 6-delig ($299)** | Pan Pro Mini 8″ (20 cm), Small 10″ (26 cm), Large 12″ (30 cm), each with its own stainless steel lid. | Los: Mini $129 + Small $137 + Large $149 + 3 lids $177 = **$592**. Set **$299** (compare-at $598). **Let op "buy 2 get 4 free":** Small + Large los = $286, de set kost $13 meer. "You pay for the Small and the Large, the Mini and three lids come free" klopt dus bijna, niet exact. Veilige zin: "Six pieces for $299. Bought one by one: $592." Floris beslist of "buy 2, get 4 free" mag (zie open vraag 1). Met HI10: $269,10. | C3: geen upsell, gifts + garantie + "the 11″ is the one size it doesn't have" alleen als P.S. P3-SET: Standard 11″ (zit niet in de set) + snijplank (29% van setkopers). R1-SET: Utensil Set + Deep Pan. |
| **12-delig ($599, US)** | 3 frying pans 8″, 10″, 12″ with lids, 2-quart and 3-quart saucepans and a stockpot, each with a lid. Ships in two parcels, each with tracking. | $599 tegen compare-at $1.186; "about $50 a piece". Niet de som van losse potten (die zijn per Gorgias alleen in de set verkrijgbaar). | C3: splitlevering-geruststelling (R530). P3: snijplank + Utensil Set. R1: Wok of Deep (zit er niet in). Nooit aan INT tonen. |
| **Cookware Set Pro ($479)** | Pan Pro 11″ (28 cm), Wok Pan Pro 28 cm, Deep Pan Pro 26 cm, titanium flipper and ladle. | Los: $144 + $119 + $119 + $58 = **$440** vanaf-prijzen (wok/deep hebben grotere maten tot $139/$149). **Geen besparing tegen losse prijzen te claimen**; alleen compare-at $870. Advies: geen rekensom, wel "three shapes, one surface". | P3/R1: deksels in 28 cm (en 26 cm voor de deep), Crêpe Pan. Nooit wok of deep. |
| **Complete Edition ($495)** | Pan Pro 11″, Deep Pan Pro, Wok Pan Pro and Crêpe Pan Pro. | Los vanaf $144 + $119 + $119 + $139 = $521. Kleine besparing; compare-at $900. | P3/R1: deksels (28 cm), snijplank. Nooit wok, deep of crêpe. |
| **Full Hammered Pro Edition ($799)** | Four Pan Pro sizes (8″, 10″, 11″, 12″), each with a lid, plus flipper, spatula, scooper and ladle. ("Medium" in Shopify = Small 10″; nakijken.) | Los: $129 + $137 + $144 + $149 + 4 lids $236 + 4 utensils $116 = $911; compare-at $1.499. | P3/R1: Wok + Deep (vormen ontbreken), snijplank. Nooit een pan of deksel. |
| **34-delig ($1.499, US)** | "Everything we make": de lijst uit Shopify, kort: the 12-piece set, roasting pan, wok, deep, crêpe, pizza steel, 4 boards, 4 utensils, mills, 4 aprons. | compare-at $2.337. | Geen cross-sell (alles al in huis). P3: alleen service + review. R1/R2/V1/N2: **uitsluiten** van productaanbod; alleen dishwasher sheets of gift card. |
| **Pan Pro Duo ($229)** | Pan Pro Small 10″ and Standard 11″. | Los $137 + $144 = $281. | C3-P: "For $70 more, the set gives you three pans and three lids" klopt **niet** (set heeft Mini/Small/Large, geen Standard). Beter: deksels 26 + 28 cm ($118). |
| **2 Pans + 2 Lids ($199)** | Two hammered pans with matching lids. **Maten onbekend** (geen metafield): eerst vastleggen. | Zonder maten geen rekensom. | C3-P: upgrade naar 6-delig: "+$100 for a third pan and a third lid" (alleen als de maten overlappen). |
| **Pan Pro Kit ($199)** | Pan Pro 10″ (26 cm) with lid and a titanium flipper. | Los $137 + $59 + $29 = $225. | C3-P: upgrade naar de set (+$100: Mini en Large met deksels). P3: Mini (Small → Mini 33%). |
| **Pro Duo ($199)** | Pan Pro 11″ (28 cm) and a titanium flipper. | Los $144 + $29 = $173: de bundel is **duurder** dan los. Geen rekensom; Floris laten kijken (open vraag 2). | P3: deksel 28 cm. |
| **Cook & Prep ($199)** | Pan Pro 11″ and the Titanium Cutting Board L. | Los $144 + $89 = $233. | P3: deksel 28 cm, Mini. |
| **Pan Pro & Utensil Set ($249)** | Pan Pro 11″ and the utensil set. | Los $144 + $149 = $293. | P3: deksel 28 cm. |

### 1.4 Hoe de template de bundel herkent

| Bron | Veld | Betrouwbaarheid | Gebruik |
| --- | --- | --- | --- |
| Checkout Started, Placed Order | `event.Items` (lijst producttitels, exact zoals Shopify) | Hoog; titels veranderen alleen als iemand het product hernoemt | **Primair.** `{% with s=event.Items|join:',' %}` en substring-keten (al in gebruik en getest in `research/tailoring/test`). |
| idem | `event.extra.line_items[].product.handle` | Hoog, stabieler dan titels | Secundair: lus `{% for li in event.extra.line_items %}{% if li.product.handle == '...' %}`; niet bruikbaar om één variabele te zetten (Django in Klaviyo heeft geen `set`), dus alleen als het blok direct in de lus mag renderen. |
| Added to Cart | `Product Name`, `URL` (bevat de handle) | Hoog | `event|lookup:'Product Name'` |
| Viewed Product | `Name`, `URL` | Hoog | B1/B2 |
| Ordered Product (XT7f8Z) | `Name`, `Variant Name` ("Chrome / Standard 28CM") | Hoog, één event per regel | Alleen in flowsplits en segmenten (historie), niet in de template |

Keten (volgorde telt, specifiek eerst; substrings die in alle kopieën van een titel voorkomen):

```django
{% with s=event.Items|join:',' %}
{% if '34-Pcs' in s %}                           {# ALL34 #}
{% elif '12-Pcs' in s or '12 pcs' in s %}        {# SET12, vóór 6-Pcs #}
{% elif 'Pan Set With Lids' in s or '6-teilig' in s %}   {# SET6: niet 'Pot Set' #}
{% elif 'Full Hammered Pro' in s %}
{% elif 'Complete Edition' in s %}               {# vangt ook de titel met en dash #}
{% elif 'Cookware Set Pro' in s %}
{% elif 'Pan Pro Duo' in s %}                    {# vóór 'Pro Duo' #}
{% elif 'Pro Duo' in s %}
{% elif '2 Pans + 2 Lids' in s %}
{% elif 'Pan Pro Kit' in s %}
{% elif 'Cook & Prep' in s %}
{% elif 'Utensil Set' in s and 'Pan Pro' in s %}
{% else %}                                        {# fallback: huidig algemeen setblok, zonder "three" en "a lid for every pan" #}
{% endif %}
{% endwith %}
```

Fallbacks: (1) geen match → algemeen blok; (2) twee bundels in één cart → de eerste in de keten wint (zelden: 0 van de bundels-orders in de steekproef had twee grote sets); (3) nieuwe bundel in Shopify → valt in de fallback tot de keten is bijgewerkt. Daarom: **bij elke nieuwe bundel in Shopify de titel toevoegen aan `content/facts/shopify-titles.csv`, de groepen in build_flows.py en deze keten** (checklist-regel in PLAYBOOK voorstellen). Vooraf testen met de bestaande Django-run (`research/tailoring/test/matrix.py`) met een sample per bundeltitel.

---

## 2. Kortingstiming

[WORDT INGEVULD]

---

## 3. Bestaande klanten herkennen

### 3.1 Wat Klaviyo kan zien, en waar

| Mechaniek | Wat het weet | Waar bruikbaar | Beperking |
| --- | --- | --- | --- |
| **Flowfilter / verzendfilter / conditional split op "What someone has done"** met Placed Order (RSNxYV) en `Items` contains-any, over all time | Of iemand ooit een titel uit een lijst kocht | Elke flow; bepaalt **welke mail** iemand krijgt | Weet niet in de template wat; alleen ja/nee per lijst. Elke vraag = een eigen split of filter. |
| idem met **Ordered Product (XT7f8Z)**: `Name` equals X **en** `Variant Name` contains "28CM" | Product **en maat/variant** per orderregel | Splits en segmenten ("heeft deksel 28 cm") | Zelfde: alleen routing. Variantnamen van deksels: "Chrome / Standard 28CM" enz. |
| **Segmenten** ("v4 · Heeft deksel", "v4 · Heeft wok", "v4 · Heeft plank") | Idem, maar herbruikbaar | Conditional split "is in segment"; campagne-uitsluiting | Segmenten updaten met wat vertraging; templates zien geen segmenten. |
| **Trigger-event in de template** (`event.Items`, `event.extra.line_items`) | Alleen de order/checkout die de flow startte | Overal | Winback (dag 45/75), VIP en anniversary zien alleen de laatste of eerste order, niet de rest. |
| **`person|lookup:'veld'`** in de template | Profielvelden | Overal, ook voor inhoud binnen één mail | Er staat nu geen aankoophistorie in het profiel (alleen Alia-velden en `Shopify Tags`). |
| **Flow-actie "Update profile property"** | Kan bv. `owned_lid_28 = true` zetten na een order | Post-purchase | **Niet via de API** (weigert, Bouwnotitie 2.1); wel handmatig in de UI. Legt alleen vast wat na livegang gekocht wordt (geen historie). |
| **Nachtelijke profiel-job (API)**: script leest Placed Order/Ordered Product en schrijft `siraat_owned` (lijst: `pan_mini,pan_standard,lid_28,wok,board,apron,set6,...`), `siraat_first_order_at`, `siraat_orders` via Profiles API / bulk import | Volledige historie, inclusief vóór livegang | Overal in templates: `{% if 'lid_28' in person|lookup:'siraat_owned' %}` | Schrijft in Klaviyo (nu verboden voor agents; Floris moet het toestaan); vertraging tot 24 uur, dus de trigger-order zelf blijft uit het event komen. |
| **Shopify customer tags** via Shopify Flow ("owns-lid-28") → Klaviyo `Shopify Tags` | Idem | `person|lookup:'Shopify Tags'` | Vraagt een Shopify Flow-workflow (schrijft in Shopify). |

**Advies:** routing (welke mail) via splits op Ordered Product en Placed Order, die werken nu en via de API. Inhoud binnen een mail (welke kaart wel of niet) via één profielveld `siraat_owned` uit een nachtelijke job, na akkoord van Floris. Tot die job er is: de template sluit uit wat in het trigger-event staat, en de flow kiest een andere mail voor wie ooit X kocht.

### 3.2 Ontwerp per geval (exacte mechaniek)

| # | Geval | Mechaniek nu (API, zonder schrijven) | Met `siraat_owned` (later) |
| --- | --- | --- | --- |
| 1 | **Accessoire-checkout (deksel, plank, utensils, schort) van iemand die al een pan heeft** | Bestaat al half: C2-ACC krijgt iedereen, C3-ACC alleen nieuwe klanten. Nieuw: dag 1 splitsen. Verzendfilter op een nieuwe **C2-OWNER**: Checkout Started (4 d) zonder KOOK **en** Placed Order where `Items` contains-any KOOK+GROOT_SET at least once over all time. C2-ACC krijgt het omgekeerde filter (zero times). C2-OWNER: geen merkuitleg, geen PFAS-pitch; "for your [maat] pan" (deksel: maatkeuze via Ordered Product-split is te fijn, gebruik de maattabel 20/26/28/30 cm), eigenaar-review ("Pans and lids arrived promptly", R157), gift-stack. C3: geen (eigenaar, zoals nu). C4: code-router zoals nu. | In C1 al: `{% if 'pan_' in person|lookup:'siraat_owned' %}` "Adding to your Siraat kitchen" en de juiste dekselmaat voorselecteren. |
| 2 | **Deksel in checkout, al dezelfde dekselmaat in huis** (komt voor: deksel voor pan 2) | Niet onderscheidbaar zonder maat-split; laten. | `{% if 'lid_28' in owned and '28' in variant %}` "A second 28 cm lid?" (zelden; niet bouwen in fase 1). |
| 3 | **VIP V1 (dag 30 na order 2): nooit aanbieden wat ze al hebben** | `goes`-blok kijkt alleen naar order 2. Fix zonder schrijven: drie verzendfilter-varianten zijn te veel; daarom de kaarten in V1 beperken tot producten die **in geen van beide orders** zitten via een split vóór V1: CS "Ordered Product Name = Stainless Steel Lid at least once over all time" → V1-a (zonder dekselkaart) / V1-b (met). Zelfde voor plank en wok is 8 takken: niet doen. Praktisch: V1 = 15% exclusive op "your next piece" met de kaartrij uit de **trigger-order** (de 2e order is de meest recente en vaak de deksel/maat), plus de regel "Already have it? Reply and we'll swap the suggestion." | Kaarten met `{% if 'lid' not in owned %}`, `{% if 'board' not in owned %}`, `{% if 'wok' not in owned %}`. Eén template, geen extra takken. Dit is het sterkste argument voor de job. |
| 4 | **Winback R1/R2 (dag 45/75)**: geen wok/deksel/plank aan wie het al heeft | Trigger = laatste order, dus de template ziet die wel. R2 biedt nu de 6-delige set, Pan Pro 11″ en 2+2 aan iedereen: voeg dezelfde `{% if %}` toe als R1-SET (set uit in trigger → geen set; Standard in trigger → geen Pan Pro 11″). Eerdere orders: split vóór R2 op "Placed Order where Items contains-any GROOT_SET at least once over all time" → R2 zonder setkaart. | Volledig via `owned`. |
| 5 | **Anniversary N2 (dag 365)** | Trigger = eerste order (de flow loopt alleen bij order 1 = 1). Template ziet die; voeg `{% if %}` toe: set in order → geen setkaart; Standard in order → geen Pan Pro 11″-kaart. (Wie een tweede order plaatste valt al uit de flow.) | n.v.t. |
| 6 | **Geen care-video aan iemand die al een half jaar kookt** | N1 (dag 182): CTA "Show me the care video" vervangen door "The brown tint, fixed in 2 minutes" (zelfde care-pagina, ander anker) + één cross-sell-rij. Welcome **W0** (al klant): nu "Thank you. Now the first egg." aan iedereen met ooit een order. Split: Placed Order at least once **in the last 30 days** → W0 (first-egg, klopt) · anders → nieuwe **W0-OWNER** (of W1 zonder HI10-uitleg): "Welcome back, here's what's new" met de fall sale. P2/P2-SAFE/U1: al alleen bij eerste order met levering. P1-REPEAT: geen care-content als de vorige order > 60 dagen geleden kookgerei had (verzendfilter `Placed Order where Items KOOK at least once between 60 and 3650 days ago` → kortere P1-repeat zonder first-egg-blok). | `siraat_first_order_at` > 60 dagen → blok weg. |
| 7 | **Checkout van een bestaande klant voor kookgerei** | Al geregeld: geen C2 (HEEFT_GEKOCHT). Toevoeging: C1 toont bij eigenaar geen "Will eggs stick?"-bezwaar maar de maat-cross-sell. Kan in C1 alleen via profielveld; tot dan laten. | `owned`. |

**Beperkingen samengevat:** (1) de API kan geen "Update profile property" plaatsen; (2) een split per product vermenigvuldigt takken, en Klaviyo kent geen samenkomende takken; (3) templates zien geen segmenten; (4) Ordered Product en Placed Order gaan terug tot het begin van de Shopify-sync (november 2024), dus historie is volledig genoeg; (5) Placed Order `Items` kent geen maat bij wok/deep/deksel, Ordered Product `Variant Name` wel.

---

## 4. Logica-check per mail

Ernst: **H** = fout of kapot, vóór livegang fixen · **M** = onlogisch, fixen in v5 · **L** = verbetering.

| # | Mail | Probleem | Fix | Ernst |
| --- | --- | --- | --- | --- |
| 1 | C3-P | $349 en link naar de 404-listing; "about $116 a pan" | $299 en hoofdlisting; "about $100 a pan, lid included"; HI10-regel $269,10 | H |
| 2 | W4-US, W4-INT | idem 6-delige set-tegel ($349, $314,10 met HI10, link bday) | $299 / $269,10; INT zonder bedrag of in eigen valuta (GBP 249, EUR 279, AUD 449, ...) | H |
| 3 | A2 | idem ($349, "about $116 a pan") | idem | H |
| 4 | R2, R2-nocode, R2-VIP, R2-VIP-nocode | idem; plus set-kaart aan wie net een set kocht | link en prijs; `{% if %}` op trigger-order (sectie 3.2 #4) | H |
| 5 | N2, N2-nocode | idem; set-kaart en Pan Pro 11″ aan wie die als eerste order kocht | idem (sectie 3.2 #5) | H |
| 6 | P3-SET (+nocode) | Biedt altijd Crêpe + Wok aan, ook aan Complete Edition, Set Pro en 34-delig | Volgende-stap-keten uit 1.3 | H |
| 7 | C3-S | Eén tekst voor alle sets en voor losse carts ≥ $300 ("a lid for every pan", "all three") | Bundelblok uit 1.3, routing 1.3 | H |
| 8 | C3-P / routing | Cart van $250-$300 met Pan Pro krijgt geen C3; starterbundels krijgen C3-S | Drempel 300, STARTER naar C3-P | M |
| 9 | C1 | Onderwerp B en hero zetten HI10 vooraan; Floris: gifts die "pending" zijn en aflopen | Onderwerp "Your cart and 4 gifts are on hold" (alleen "expire" als waar: gifts gelden zolang de actie loopt, dus "on hold"/"saved", geen deadline); HI10 tweede regel | M |
| 10 | C1, C2, C3-S, C4-nocode, K1-K3, B, W1, W5, R1, P1 | "$70 in gifts" en "$15/$30/$25/$450 value" in USD aan iedereen | Waarden alleen bij US; INT: "4 gifts with every order" zonder bedrag (of omrekenen in de template is niet mogelijk) | H (INT is 55% van de orders) |
| 11 | C4 | "10% off your cart for 48 hours" | "Your 10% expires in 48 hours" + deadline-tegels (al gebouwd); onderwerp aanpassen | M |
| 12 | C4 / C4-nocode | Code wordt ook aan iemand met alleen een e-gift card gestuurd (werkt vermoedelijk niet) | Verzendfilter: Checkout Started zonder alleen "E-Gift Card" | L |
| 13 | C2-ACC | Eigenaar en nieuwe klant krijgen dezelfde merk/cadeau-mail | Split C2-OWNER (3.2 #1) | M |
| 14 | K1 | 10% (HI10) direct in K1 | Zie sectie 2: weg uit K1 en K2, 10% pas in K3 | M (beslissing Floris) |
| 15 | K2-new | Set of bundel in cart krijgt de 1-pan-rekensom (15 gecoate pannen) | Bundelblok uit 1.3 voor `Product Name` met een bundeltitel | M |
| 16 | K3 | Floris wil "we're removing your cart and discount"-urgentie | Alleen waar: de **code** vervalt na 48 uur (echt); de cart wordt niet verwijderd door Shopify (blijft tot de browser hem wist). Zin: "Your code expires Friday 9:00. After that, the cart stays, the 10% doesn't." | M |
| 17 | K-mails | Cart-links naar PDP, niet naar de cart | Blijft (open punt productmatrix 3) | L |
| 18 | B1 | HI10 vanaf mail 1 en "get 10% off this pan"-knop; Floris vraagt juist meer verhaal | Zie sectie 2: B1 zonder korting, verhaal + bewijs; 10% in B2 | M |
| 19 | B1, B2-notclicked, B2-clicked-nocode | Roasting pan en 12-delig in de productrijen zonder landcheck? (grep: 6 vermeldingen "roasting", 3 "12-p" zonder `country`-conditie in het bestand) | Elke verwijzing naar 12-delig, potten, roasting en 34-delig binnen `{% if US %}`; Viewed Product heeft geen land, dus `person.Country`-regel uit C4 gebruiken | H |
| 20 | W0 | "Thank you. Now the first egg." aan iedereen die ooit kocht | Split op order in laatste 30 dagen (3.2 #6) | M |
| 21 | W1-W5 | Bestaande klanten komen er niet in (W0-tak), maar wie tijdens de flow een cart-mail kreeg mist een W-mail (overslaan) en krijgt daarna W5 "last note about your 10%" zonder W1 gezien te hebben | Acceptabel; W5 opent met de code zelf | L |
| 22 | W4-INT | 12-delig wordt in INT niet getoond (goed), maar de set-tegel linkt naar de 404 | zie 2 | H |
| 23 | P1-REPEAT | First-egg-blokken voor iemand die al maanden kookt | 3.2 #6 | M |
| 24 | P3-PAN, P3-SET, P3-ACCESSORY | USD-prijzen aan iedereen (bekend, J1) | `country_code == 'US'`-regel | M |
| 25 | P3-NEXT | "YOU HAVE THE LID"-kaart: goed; maar bij eigenaar-tak (accessoire nu, pan eerder) is de maat van de eerdere pan onbekend | Maattabel tonen (20/26/28/30) in plaats van "your pan" | L |
| 26 | R1-PAN | Roasting-kaart (US) ook aan wie net de roasting pan kocht | `{% if 'Roasting' not in items %}` | M |
| 27 | R1-SET | 34-delig en Full Hammered Pro krijgen wok/crêpe/utensils aangeboden | Keten uit 1.3; 34-delig: geen productaanbod | M |
| 28 | R1-PAN, R1-ACC | "Two months" in onderwerp/preview klopt niet bij dag 45 (bekend) | "Six weeks" | L |
| 29 | R2 | Wordt verstuurd "zolang up to 50% off live is": de fall sale is "buy 2 get 4 free", geen 50% | Tekst nakijken op de huidige actie | M |
| 30 | V1 | "Twice is a habit" (Floris: slecht) en aanbod kan iets zijn wat in order 1 zat | Onderwerp "You're a VIP customer: 15% exclusive, for 14 days"; kaarten 3.2 #3 | M |
| 31 | N1 | "Show me the care video" op dag 182 (twee keer) | CTA naar de oplossing voor de bruine tint / "what to cook next"; care-video weg | M |
| 32 | N2 | 10% (flow), Floris wil 15% | Pool SK_ANNIV15_7D (nieuw), tekst 15% exclusive | M (besluit) |
| 33 | U1 | Prima; maar ook aan cadeaugevers (pan staat bij een ander) | Cadeau-proxy uit personalisatie 4.7 | L |
| 34 | A1/A2 | HI10 in de eerste mail van de laagste-intentie-flow | Zie sectie 2 | L |
| 35 | Alle verkoopflows | Fall sale (6-delig $299) staat nergens als hoofdaanbod | In C3-P, W4, A2, R2, N2 de set-tegel = fall sale; hero alleen als Floris een einddatum geeft (DECISIONS: geen harde datum) | M |

---

## 5. Open vragen voor Floris

1. Mag "Buy 2, get 4 free" in de mails? Small + Large los kost $286, de set $299; het klopt alleen tegen de compare-at. Veilig alternatief: "Six pieces for $299. Bought one by one: $592."
2. Pro Duo ($199) is duurder dan los ($144 + $29); 2 Pans + 2 Lids heeft geen maten op de pagina. Welke maten zitten erin?
3. Dubbele ACTIVE listings met andere prijzen (Standard $144 en $157, Large $149 en $169): welke is de echte prijs voor rekensommen?
4. Nachtelijke profiel-job `siraat_owned` (schrijft profielvelden in Klaviyo via de API): akkoord? Anders de UI-stap "Update profile property" in post-purchase (alleen nieuwe orders).
5. Cart zonder 10% in K1 en K2 (sectie 2): akkoord als test of direct?
6. Anniversary N2 naar 15% (nieuwe pool), en VIP-onderwerp.
7. DECISIONS bijwerken: 6-delige set = $299 (fall sale), niet meer $349; einddatum fall sale?
