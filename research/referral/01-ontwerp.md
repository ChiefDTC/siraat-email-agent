# Referral · ontwerp (15 okt 2026)

Opdracht Floris: na elke aankoop een referral-mail met een eigen code, "helemaal geregeld". Er is nu geen referralprogramma. Dit stuk vergelijkt twee routes, kiest een aanbod, legt timing en filters vast en noemt de fraude-risico's. De livegang staat stap voor stap in `02-livegang-stappen.md`. Niets is live gezet, niets is aangemaakt in Klaviyo of Shopify.

Gebouwd: `klaviyo/templates/v3/referral/ref1.html` (hoofdmail) en `ref1-review.html` (na 5 sterren), batchscript `research/referral/referral_batch.py` (alleen lezen, behalve met `--apply`).

## 1. Kort advies

- **Nu route A (zonder app)**: Klaviyo unieke coupons (Shopify), een eigen code per klant die hij aan **een** vriend geeft, beloning van de verwijzer via een wekelijkse batch. Kost geen abonnement, past op wat al draait (zelfde coupon-mechaniek als C4, K3, P3), en we leren eerst of klanten delen.
- **Aanbod: "Give $25, get $25"** (optie B hieronder), vriend minimaal $100, alleen eerste order, beloning pas na de retourtermijn.
- **Fase 1 alleen US** (bedragen in USD; de QA-poort weigert USD buiten de US terecht). INT volgt met lokale pools of met procenten.
- **Overstappen naar route B** (app) als na 8 tot 12 weken blijkt dat referral loopt (richtwaarde: meer dan 50 vriendenorders per maand of de batch kost meer dan een uur per week). Dan Rivo of ReferralCandy, met de Klaviyo-integratie, en dezelfde mails als basis.

## 2. Hoe Klaviyo unieke coupons met Shopify werken

Bron: Klaviyo-helpartikel "How to create unique coupon codes for Shopify" (via zoekresultaten; help.klaviyo.com zelf was vanuit deze sessie niet bereikbaar), Klaviyo-community, en eigen GET's op account TdtTzz.

- **Aanmaken** in Klaviyo > Coupons > Create coupon > Shopify > unique codes. Klaviyo maakt in Shopify een kortingsregel (price rule) en genereert de codes zelf, in batches van ongeveer 100 tegelijk (Shopify-API-limiet). Codes kunnen dus al in Shopify staan voordat ze verstuurd zijn.
- **Instellingen** (in het Klaviyo-formulier, bij de bouw één keer nalopen): type (percentage, vast bedrag, gratis verzending), bedrag, geldigheid (producten of collecties), minimumbedrag, een gebruik per klant, combineren met andere kortingen, prefix, vervaltermijn. Elke unieke code is eenmalig.
- **In de mail**: `{% coupon_code 'NAAM' %}`. Elke ontvanger krijgt bij verzending een eigen code; dezelfde tag meerdere keren in een mail geeft dezelfde code (in v4 al gebruikt, P3 11 keer).
- **Vervaltermijn**: in flows "X dagen of uren na toewijzing"; de klok start pas bij versturen. Klaviyo rekent in UTC, Shopify in de winkeltijdzone, dus de datum kan een dag verschillen.
- **Beperkingen**:
  1. Een unieke code werkt **een keer**. Een "eigen code die je met al je vrienden deelt" kan dus niet met deze route: het wordt een code per vriend. Oplossing: bij elke beloning komt er een nieuwe code mee (ref2-thanks).
  2. Werkt niet op abonnementen (Recharge); geldt alleen voor one-time purchase.
  3. Wijzigingen aan de kortingsregel in Shopify zijn niet betrouwbaar: bij codes met een vervaltermijn maakt Klaviyo per batch een nieuwe price rule, dus een aanpassing in Shopify (zoals "alleen nieuwe klanten") geldt dan alleen voor de huidige batch. Bij codes zonder vervaltermijn komen nieuwe codes in dezelfde regel (community, onofficieel). Gevolg: "alleen nieuwe klanten" niet aan Shopify overlaten maar in de batch controleren.
  4. Shopify-limiet 20 miljoen codes per winkel (geen probleem).
  5. Een order heeft maar een kortingscode (Gorgias-guidance 5302107): de vriendencode vervangt HI10, stapelt niet. Gifts en sale blijven gewoon gelden.
- **Wat Klaviyo zelf meet** (GET op TdtTzz): metric **Coupon Assigned** (XUMYt7, met `CouponKey` en `UniqueCode`, op het profiel van de ontvanger) en **Coupon Used** (USRsNP, met `OriginallyAssignedTo`). Coupon Used is sinds juli 2026 niet meer gevuurd, terwijl er sinds september 123 unieke codes zijn toegewezen. Daar niet op bouwen. Wel betrouwbaar: **Placed Order** (RSNxYV) heeft `Discount Codes` en `$extra.shipping_address`. De batch koppelt dus Placed Order-codes aan Coupon Assigned.
- **Leesrechten nu**: `GET /api/coupons/` geeft een lege lijst (sleutel mist coupons-scope of er zijn geen API-zichtbare coupons); de pools zelf bestaan wel (Coupon Assigned-events voor C4, K3, B2, P3, R2-VIP, V1).

## 3. Route A tegenover route B

| | **A. Zonder app (Klaviyo + batch)** | **B. Met app** |
| --- | --- | --- |
| Software | $0 extra (Klaviyo en Shopify bestaan) | Rivo $49 tot $499 p/m (gratis plan bestaat); ReferralCandy $39 tot $799 p/m plus 0,25 tot 10,5% succesfee op de eerste drie orders van een vriend; Smile.io gratis tot ca. $999 p/m (bronnen spreken elkaar tegen); Yotpo Loyalty vanaf ca. $199 p/m |
| Code | Eenmalig, een per vriend, via `{% coupon_code %}` | Eigen deellink of herbruikbare code per klant, vaak een referral-pagina en pop-up op de site |
| Automatisch | Code in mail, toewijzing, eenmalig gebruik, vervaltermijn | Daarnaast: koppeling vriend aan verwijzer, beloning uitgeven, eigen dashboard, events naar Klaviyo voor flows |
| Handwerk | Wekelijkse batch (script, 10 tot 20 min), beloningsevent versturen | Instellen en bewaken |
| Fraude | Eigen regels in de batch (sectie 5), handmatige steekproef | Ingebouwd (zelfde e-mail, IP, apparaat, adres), wisselend per app |
| Sitewijziging | Geen | App-embed of pagina in het thema |
| Data | Alles in Klaviyo, eigen meetplan | In de app plus events in Klaviyo |
| Snelheid | Live na Floris' besluit en 1 middag bouwen | Installatie, thema, testen: 1 tot 2 weken |

Kosten B bij het realistische scenario (ca. 200 vriendenorders per jaar, $224 AOV nieuwe klant, `research/potentie/02-bottom-up.md`): ReferralCandy Grow $79 p/m plus 3,5% van ca. $3.700 per maand ≈ $210 p/m, ruim $2.500 per jaar, boven op de beloningen. Rivo Scale vanaf $49 p/m ≈ $600 per jaar. Pas bij 50+ vriendenorders per maand weegt het handwerk van A zwaarder dan dat.

Bronnen B (prijzen wisselen en komen deels van een concurrent, Rivo; voor besluit de officiële prijspagina's openen): [Rivo vs Smile.io vs ReferralCandy](https://rivo.io/blog/rivo-vs-smileio-vs-referralcandy), [Rivo: best Shopify referral app 2026](https://www.rivo.io/blog/shopify-referral-program-app), [Smile.io pricing (Capterra)](https://www.capterra.com/p/169446/Smile-io/pricing/), [Smile.io pricing (Costbench)](https://www.costbench.com/software/loyalty-program/smile-io/), [Yotpo pricing (ecommerce-platforms)](https://ecommerce-platforms.com/ecommerce-reviews/yotpo-reviews-and-pricing), [Yotpo Loyalty pricing (Rivo)](https://www.rivo.io/blog/yotpo-loyalty-pricing). Klaviyo: [How to create unique coupon codes for Shopify](https://help.klaviyo.com/hc/en-us/articles/115006155388), [community: expiration in flows](https://community.klaviyo.com/email-templates-and-coupons-32/expiration-date-of-unique-coupon-code-in-a-flow-setting-5567), [community: one per customer](https://community.klaviyo.com/marketing-30/dynamic-coupons-restricted-to-one-per-customer-per-product-5057).

**Later overstappen (A naar B)**: de app neemt de vriendcode en de beloning over; de Klaviyo-flows blijven, alleen de bron van de code wijzigt (app-property op het profiel, bijvoorbeeld `{{ person.referral_link }}`, in plaats van `{% coupon_code %}`). Stappen: app installeren op een testthema, zelfde aanbod instellen, appevents in Klaviyo controleren, in ref1 en ref1-review de code-regels vervangen, de pool REF_FRIEND_25 laten uitlopen (codes geldig 60 dagen), batch nog 70 dagen draaien voor openstaande codes, dan stoppen. De meetcode `utm_source=referral` blijft hetzelfde, zodat de cijfers doorlopen.

## 4. Aanbod: drie opties

Uitgangspunten: Pan Pro $134 tot $144, 6-delige set $299, AOV nieuwe klant $224, terugkerend $194 (`research/deep/02`). Productmarge ca. 83% (Intelligems COGS 16,9%), na verzending, fulfilment en retouren ca. 60% (aanname uit eerdere stukken). HI10 is 10% ($13,40 tot $14,40 op een pan), dus de vriend moet zichtbaar meer krijgen. Een korting voor de vriend vervangt HI10 (een code per order).

| | **A. Give 15%, get $25** | **B. Give $25, get $25 (advies)** | **C. Give $20, get a lid** |
| --- | --- | --- | --- |
| Vriend | 15% op eerste order, min. $100 | $25 vast op eerste order, min. $100 | $20 vast op eerste order, min. $100 |
| Verwijzer | $25-code op volgende order (90 dagen) | $25-code op volgende order (90 dagen) | Gratis deksel in eigen maat (verkoop $59, kostprijs ca. $10) of $25-code als hij er al een heeft |
| Op een pan ($144) | vriend $21,60 (15%) | vriend $25 (17%) | vriend $20 (14%) |
| Op de set ($299) | vriend $44,85 | vriend $25 (8%) | vriend $20 |
| Kosten per vriendenorder | $22 tot $45 + $25 als de verwijzer verzilvert | $25 + $25 bij verzilvering | $20 + ca. $10 tot $15 (deksel plus verzending) |
| Valuta | Procent werkt in elke markt | Vast USD, Shopify rekent om | Vast USD; deksel overal |
| Uitleg | Ongelijk, lastiger te delen | Symmetrisch, makkelijkst te zeggen | Product als beloning, sterk na P3 (22% van de herhalers koopt het deksel) |
| Risico | Duur op sets; voelt als nog een procentcode | Op een pan 17%, lager dan de 41% sale-korting; geen prijsondermijning | Handwerk: deksel in de juiste maat via een 100%-code op het deksel; werkt niet voor wie al alles heeft |

Marge-afweging B: vriendenorder $224 × 60% = $134 bijdrage, min $25 = $109, min de verwijzersbeloning ($25 × verzilvering; bij 50% gemiddeld $12,50) = ca. $97 per nieuwe klant. De $25 van de verwijzer komt alleen terug als hij opnieuw koopt (gemiddeld $194, dus ook nieuwe omzet). Breakeven: ruim boven elke redelijke CAC, mits de vriend echt nieuw is (vandaar de regels in sectie 5).

Waarom B: het verschil met HI10 is duidelijk ($25 tegen $14,40 op een pan), het kost op grote orders niet meer (vast bedrag), en "Give $25, get $25" is in een zin door te vertellen. C is het sterkste merkverhaal (product in plaats van korting) maar vraagt meer handwerk; geschikt als test in fase 2.

## 5. Fraude-risico's en tegenmaatregelen

| Risico | Tegenmaatregel | Waar |
| --- | --- | --- |
| Verwijzer gebruikt zijn eigen code | Batch: zelfde profiel, zelfde e-mail of zelfde verzendadres als een eerdere order van de verwijzer = geen beloning. Copy zegt "for a friend's first order". | `referral_batch.py` regels 2 en 3 |
| Nieuw e-mailadres van dezelfde persoon | Adrescontrole (adres + postcode) tegen alle orders van de verwijzer; plafond 10 beloningen per verwijzer per jaar; steekproef bij meer dan 3 per maand | batch regel 2 en 6 |
| Code op couponsites (RetailMeNot, Honey) | Unieke code werkt maar een keer, vervalt na 60 dagen, minimum $100; een gelekte code kost hooguit een keer $25 en levert geen beloning op als de koper geen nieuwe klant is | Klaviyo-coupon, batch regel 3 |
| Bestaande klant gebruikt vriendencode | Batch: vriend moet zijn eerste order plaatsen, anders geen beloning. Optioneel in Shopify "customer eligibility" op een segment met 0 orders (alleen als het blijft staan, zie 2.3; testen) | batch regel 3 |
| Bestellen, beloning pakken, retourneren | Beloning pas als de order 40 dagen oud is (30-day returns vanaf levering, mediaan levering 12 dagen) en zonder Refunded of Cancelled Order | batch regels 4 en 5 |
| Stapelen met HI10 of andere code | Shopify staat een code per order toe | Shopify |
| Beloning dubbel | State-bestand met beloonde order-id's; event `unique_id` per order | batch |
| Bots (Google storebot) | Flowfilter email bevat niet `storebotmail.joonix.net`, zoals op QUBUQV | flow |

## 6. Timing en triggers

Gemeten tijdlijn (v4-flow-system 2.5 en 3.10): orders worden na een mediaan van ca. 3 dagen verzonden, levering mediaan 11,7 dagen na order. Maar 36% van de orders krijgt een Delivered Shipment-event (US 37%, CA 9%, overig 1%).

| Moment | Wat | Trigger en reden |
| --- | --- | --- |
| P1 (1 uur na order) | Korte regel: "In a few weeks, once the pan has proven itself, I'll send you a code to share with one friend." | Bestaande mail, alleen tekstwijziging (02-livegang stap 6). Plant het idee zonder iets te vragen. |
| **REF1** | Hoofdmail met code | **Fulfilled Order (VtEiZT) + 26 dagen, tot 09:00**. Fulfilled Order dekt alle orders (Delivered Shipment maar 36%). +26 = ca. levering + 17 dagen bij de mediaan: na de eerste kookbeurten, na P3 (order + 20) en na de reviewvraag (levering + 14), zodat de klant eerst zijn eigen ervaring heeft. |
| **REF1-REVIEW** | Zelfde code, na 5 sterren | **Clicked Email (W247h8)** in XzHrez op de 5-sterrenlink, 1 dag wachten tot 09:00. Voorwaarde: de 5-sterrenlink krijgt een eigen kenmerk (nu is hij gelijk aan 4 sterren). Er komt geen review-event naar Klaviyo (Trustpilot stuurt niets), dus de klik is het beste signaal. Wie hem krijgt, krijgt REF1 niet meer (filter). |
| Beloning (ref2-thanks, fase 1b) | $25-code plus nieuwe vriendencode | Eigen event "Referral Reward Earned" uit de wekelijkse batch. |

Filters REF1 (exacte syntax in 02-livegang):
- Triggerfilter op Fulfilled Order: `Items` bevat een van de 48 kookgerei- en settitels (zelfde lijst als VQ93sx) en `$currency_code` is USD (fase 1 US; Fulfilled Order heeft beide velden, gecontroleerd).
- Flowfilter: niet eerder in deze flow (alltime); e-mail bevat niet `storebotmail.joonix.net`.
- Verzendfilters: Refunded Order (Xg6cwn) 0 keer in 60 dagen; Cancelled Order (TFervq) 0 keer in 60 dagen (geen retouren, geen annuleringen); Opened Ticket Gorgias (YzvjGf) 0 keer sinds flowstart; geen mail uit flow "v4 · Referral · review" in 60 dagen; geen mail uit X3ySuU of XzHrez in de laatste 2 dagen (geen twee Siraat-mails op een dag).
- Smart sending uit (globale regel), afzender "Siraat's Kitchen" (zoals de andere flows).

Herhaalde mail: een keer per klant ooit. Herhaalkopers krijgen hem bij hun eerste kookgerei-order; de beloningsmail brengt daarna steeds een nieuwe code.

## 7. Mails (klaar, niet live)

| Mail | Bestand | Onderwerp A / B | Preview |
| --- | --- | --- | --- |
| REF1 | `klaviyo/templates/v3/referral/ref1.html` | Who do you cook for? / Your code for one friend: $25 off | Give one friend $25 off their first order. You get $25 back. |
| REF1-REVIEW | `klaviyo/templates/v3/referral/ref1-review.html` | Know someone still on a coated pan? / $25 for a friend, $25 for you | You tapped five stars. Here is a code to share with one friend. |

Vijf onderwerpregels per mail staan in de topcomment van elke bron (skill sectie 5). Opbouw: vaste header en footer, hero met aanbodbalk, knop direct onder de hero, Benjamin-stem, aanbodblok met de code, "How it works" (REF1), twee letterlijke Trustpilot-reviews over doorgeven (Tammy R138, Louise T. R563, gecontroleerd), knop onderaan, P.S. Delen gaat met een `mailto:`-knop (onderwerp en tekst met de link al ingevuld), een kopieerbare link en een sms-link. De link `siraatskitchen.com/discount/<code>` zet de korting in de winkelwagen en stuurt naar de Pan Pro, met `utm_source=referral`.

Claims gebruikt: "pure titanium cooking surface, no coatings" (in de deeltekst), 30-day returns, free shipping. Geen nieuwe claims; het aanbod zelf is een besluit van Floris (02, beslispunt 1).

Previews: `klaviyo/templates/v3/referral/previews/ref1-mobile.png` en `ref1-review-mobile.png` (Django-render op een US-profiel). Checks: `check_previews.py` (referral 0 problemen), QA-render statisch voor beide mails groen (kopie van qa_render met de map referral, scripts niet gewijzigd), `check_reviews.py` 0 fouten, `run_tests.sh` groen, 0 gedachtestreepjes.

## 8. Verwachting

Geen eigen data. Bottom-up (`research/potentie/02-bottom-up.md`): 0,25% / 0,75% / 2% van 80.912 nieuwe klanten per jaar via referral = 202 / 607 / 1.618 vriendenorders, $45k / $136k / $362k omzet bij $224. Kosten bij B: $25 per vriendenorder plus ca. $12,50 verwijzersbeloning = $7,6k / $23k / $61k per jaar. Meetplan in 02-livegang sectie 8.
