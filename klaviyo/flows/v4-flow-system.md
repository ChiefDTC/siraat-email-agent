# Flow-systeem v4 · definitief bouwplan voor Klaviyo

Versie 7 oktober 2026. **Dit document is de enige bron voor de bouw in Klaviyo.** Het vervangt `v3-flow-system.md` en `v3-new-flows.md` als bouwspecificatie (die blijven staan als achtergrond).
Samengevoegd uit: `v3-flow-system.md`, `v3-new-flows.md`, `research/timing/01-data.md` en `02-advies.md` (12 maanden data), `research/tailoring/01-journey-matrix.md`, `03-routing.md` en `04-flow-wijzigingen.md`, `research/testing/01-meetkader.md`, `02-testroadmap.md` en `04-utm.md`, `research/ux-2026-10-07/04-offer-strategy.md`, `research/qa-2026-10-07/qa-report.md`, `research/potentie/flow-potentie.md`, `DECISIONS.md`, `README.md`.
Figma-structuur: `klaviyo/figma/v4/specs.json`. Mails: `klaviyo/templates/v3/<map>/<mail>.html` (de mailmap heet nog v3; de inhoud is de v4-bouw).

Niets in dit document is al in Klaviyo of Shopify aangemaakt. Geen live wijzigingen tot Floris de beslissingen in sectie 3 heeft genomen.

---

## Inhoud

1. Overzicht en globale regels
2. Flows, stap voor stap (11 flows plus één hulpflow)
3. Conflicten en besluiten
4. Bouwlijst voor Klaviyo
5. Mail-inventaris

---

## 1. Overzicht en globale regels

### 1.1 Alle flows

| # | Flow (naam in Klaviyo) | Soort | Trigger (metric-ID) | Vervangt | Mails | `utm_campaign` |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | v4 · Checkout abandonment | verkoop | Checkout Started (RfMvni) | Y2TmNB, Tsg2tV | c1, c2, c2-acc, c3-p, c3-s, c3-acc, c4 (+ nocode; land in de template) | v4-checkout |
| 2 | v4 · Cart abandonment | verkoop | Added to Cart (QXcV8K) | SwkMyn, TBWngE | k1, k1-acc, k2-new, k2-returning, k3 (+ nocode) | v4-cart |
| 3 | v4 · Browse abandonment | verkoop | Viewed Product, Klaviyo onsite (XNtYMB) | Wj6x6V, TyEjuQ | b1, b1-acc, b2-clicked, b2-notclicked (+ nocode) | v4-browse |
| 4 | v4 · Welcome | verkoop | Toegevoegd aan lijst Uw8eZG | SiaNLu, T2SmtR | w0, w1-a, w1-b, w2, w3, w4-us, w4-int, w5 | v4-welcome |
| 5 | v4 · Post-purchase | klant | Placed Order (RSNxYV) | RL3TU6 | p1-first, p1-repeat, p2-safe, p3-set, p3-pan, p3-next, p3-apron, p3-accessory (+ nocode) | v4-postpurchase |
| 5b | v4 · Post-purchase · levering | klant (hulpflow) | Delivered Shipment (VcUF33) | (P2-deel van RL3TU6) | p2 | v4-postpurchase |
| 6 | v4 · Winback | verkoop | Placed Order (RSNxYV), dan wachten | UEfh4h | r1-pan, r1-set, r1-acc, r2, r2-vip (+ nocode) | v4-winback |
| 7 | v4 · Site abandonment | verkoop (nieuw) | Active on Site (UdCdLD) | draft UEqeEm (niet gebruiken) | a1, a2 | v4-site |
| 8 | v4 · Sunset | onderhoud (nieuw) | Segment "v4 · Sunset · unengaged 120d" | S7V4a7 | s1, s2 | v4-sunset |
| 9 | v4 · VIP | klant (nieuw) | Placed Order (RSNxYV), 2e order | | v1, v2 (+ v1-nocode) | v4-vip |
| 10 | v4 · Anniversary | klant (nieuw) | Placed Order (RSNxYV), 1e order met kookgerei | | n1, n2 (+ n2-nocode) | v4-anniversary |
| 11 | v4 · UGC first egg | klant (nieuw) | Delivered Shipment (VcUF33) | | u1 | v4-ugc |
| (blijft) | Review request XzHrez | klant | live, ongewijzigd (levering + 14 dagen) | Vixr6X (uit op 12 okt) | review | review |

De `utm_campaign`-slugs blijven `v3-*` zoals in `research/testing/04-utm.md`, zodat de rapportage en `results.csv` niet breken.

### 1.2 Prioriteit tussen flows

Iemand zit nooit in twee verkoopflows tegelijk. Hogere wint, lagere wacht of slaat over.

| Rang | Flow | Wat de lagere flows doen |
| --- | --- | --- |
| 1 | Post-purchase (gekocht) | Elke verkoopflow stopt via "Placed Order = 0 sinds flow-start". Checkout start niet bij een post-purchase-mail in 7 dagen. |
| 2 | Checkout | Cart, browse en site starten niet als er in 7 dagen een checkout-mail was. |
| 3 | Cart | Browse en site starten niet bij een cart-mail in 7 dagen. Cart start niet als er sinds flow-start een Checkout Started is. |
| 4 | Browse | Site start niet bij een browse-mail in 7 dagen. |
| 5 | Welcome | Browse start niet bij een welcome-mail in 7 dagen (overlap: uitschrijf 7,24% tegen 5,14%). Een welcome-mail wordt **overgeslagen** (niet beëindigd) als er in 24 uur een checkout- of cart-mail was. |
| 6 | Winback | R1 overgeslagen bij een post-purchase- of VIP-mail in 7 dagen. |
| 7 | Site abandonment | Laatste verkoopvangnet: alleen zonder productview en zonder mail uit 1 tot 6 in 7 dagen (welcome 10 dagen). |
| klant | UGC (levering +4), VIP (2e order +30), Anniversary (dag 182 en 365) | Afstand via filters per mail (zie de flows). |
| onderhoud | Sunset | Niet in welcome of post-purchase in 30 dagen, geen order in 180 dagen. |

**Hoe "niet in flow X" in Klaviyo werkt.** Een flow-filter kan alleen "has not been in *this* flow" controleren. Voor andere flows gebruiken we overal:
`What someone has done` · **Received Email (YkRM4Q)** · where `Flow` equals `<naam flow X>` · **zero times** · in the last N days.
Daarom moeten de flownamen exact zijn zoals in 1.1. (Controleer bij de eerste bouw dat de dimensie `Flow` in de Received Email-filter beschikbaar is; zo niet, per flow een segment "Received Email from flow X in last 7 days" maken en filteren op "is not in segment".)

### 1.3 Globale regels

| Regel | Instelling | Bron en reden |
| --- | --- | --- |
| Smart sending | **Uit** in alle flows. | De prioriteit regelt overlap (v3). |
| Afzender | "Siraat's Kitchen" <send@siraatskitchen.com>; W2, S2, V2: "Benjamin at Siraat's Kitchen". Reply-to: een gelezen inbox (support@siraatskitchen.com, Gorgias). | QA A22: mails zeggen "Just reply". |
| Tijdzone | Alle delays in de tijdzone van het profiel. Zonder tijdzone: account (US/Eastern). | 244.493 profielen hebben een tijdzone. |
| Quiet hours | **22:00 tot 07:00 lokaal** voor vervolgmails, uitgevoerd met "wacht X dagen, tot 09:00". Eerste mails (C1, K1, B1, P1, A1) gaan realtime, ook 's avonds. | Timing 3b: realtime 21-22 uur even goed als overdag. Klaviyo kent voor e-mailflows geen quiet hours; "tot HH:MM" is de enige manier. |
| Verzenduur vervolgmails | **09:00 lokaal** (één tijd voor alle flows, ook de nieuwe flows die 10:00 noemden). Uitzondering: C2 en K2 "wacht 1 dag" zonder tijd (24 uur na mail 1, zelfde uur), zie besluit 3.5. | Orders pieken 09-12 uur (7,1-7,4% per uur). |
| Klaviyo-delay "X dagen, tot HH:MM" | Betekent: op kalenderdag (vandaag + X) om HH:MM. In de tabellen staat steeds het doel ("dag 3, 09:00") én de instelling. | Bij de bouw één keer controleren met een testprofiel. |
| Weekdagen | Geen weekdagfilter. | Weekend is de sterkste koopdag (16-17%). |
| Attributie | Accountvenster niet wijzigen tijdens tests (5 dagen klik, 1 dag open dekt 88-98%). | Timing 4, meetkader 1.5. |
| Frequentieplafond campagnes | Max **3 campagnes per profiel per week**. Segment "v4 · Campagne-cap" = Received Email where Flow is not set (campagnes) at least 3 times in the last 7 days; uitsluiten bij elke campagne. Flowmails tellen niet mee. | Timing 10: sprong 3 naar 4 mails per week (0,98% naar 1,60% uitschrijving); week 28 sep: 3.408 uitschrijvingen. |
| Nieuwe inschrijvers | 14 dagen geen campagnes: segment "v4 · Welcome-bescherming" uitsluiten. | 12,2% schrijft zich binnen 14 dagen uit. |
| Verzendfilter elke verkoopmail | Placed Order (RSNxYV) zero times since starting this flow. | v3. |
| Trigger-dubbels | Geen Triple Pixel-triggers (RtgBgs, V48nhq) meer. Nooit Postflows UabgWz als trigger. | Dubbele instap. |

### 1.4 Codes: één unieke code per persoon per 30 dagen

Discount ladder (offer-strategie §4): trede 0 sale + 4 gifts in dollars (elke mail), trede 1 gift-deadline of set-upgrade, trede 2 10% (HI10 of unieke code, alleen laatste mail), trede 3 15% (alleen VIP), 20%+ nooit in flows.

**Code-router** (staat vóór elke mail met een unieke code: C4, K3, B2-clicked, P3, R2, R2-VIP, V1, N2):

```
CONDITIONAL SPLIT "Cooldown?"
  Properties about someone · last_flow_code_at · is in the last · 30 days
  JA  → <mail>-nocode (geen code; gift-stack, trekking, 30-day returns). Telt niet mee in T02.
  NEE → A/B-actie T02 (50/50, geen automatische winnaar)
          A → <mail> met {% coupon_code 'POOL' %}
              → Update profile property: last_flow_code_at = datum van vandaag, last_flow_code_pool = 'POOL'
          B → <mail>-nocode
```

- Elke code is uniek, één gebruik, één per klant (DECISIONS 7 okt), alleen one-time purchase products, vervalt X na toewijzing. Eén kortingscode per order, dus een unieke code vervangt HI10 (stapelt niet).
- **Datum zetten**: als de actie "Update profile property" geen datum-van-vandaag kan zetten, terugval: alle codemails krijgen in Klaviyo een berichtnaam die begint met `CODE ·`, en de cooldown-split wordt `Received Email where Message Name starts with "CODE ·" at least once in the last 30 days`. Bij de bouw kiezen en hier noteren.
- Tijdens de BFCM-bevriezing (20 nov t/m 6 dec) staat de T02-split op 100% A.
- `{% coupon_code %}` staat meerdere keren per mail (P3 11 keer): in de preview met een testprofiel bevestigen dat het overal dezelfde code is (QA 2.2).

### 1.5 UTM-schema (bindend: `research/testing/04-utm.md`)

| Parameter | Waarde |
| --- | --- |
| `utm_source` | `klaviyo` |
| `utm_medium` | `email` |
| `utm_campaign` | flow-slug uit 1.1 (`v4-checkout` enz.); oud pad in T01: `old-<flow>` via Klaviyo custom tracking params |
| `utm_content` | `<mailid>-<blok>`; mail-ID zonder koppelteken: `c1`, `c2`, `c2acc`, `c3p`, `c3s`, `c3acc`, `c4`, `c4nocode` (was `c4us`, `c4int`), `k1`, `k1acc`, `k2new`, `k2ret`, `k3`, `b1`, `b1acc`, `b2c`, `b2n`, `w0`, `w1a`, `w1b`, `w2`, `w3`, `w4us`, `w4int`, `w5`, `p1first`, `p1rep`, `p2`, `p2safe`, `p3pan`, `p3set`, `p3next`, `p3apron`, `p3acc`, `r1pan`, `r1set`, `r1acc`, `r2`, `r2vip`, `a1`, `a2`, `s1`, `s2`, `v1`, `v2`, `n1`, `n2`, `u1`. Blokken: `codebar`, `logo`, `nav-*`, `hero`, `cart`, `product`, `prod-<kort>`, `cta1..3`, `offer`, `giftcard`, `gifts`, `features`, `reviews`, `compare`, `size-*`, `tier1..3`, `report`, `warranty`, `ps`, `set12`, `ebook`, `guide`, `ft-*`. |
| `utm_term` | testvariant `<testid>-<a|b>` (`t02-b`, `t04-a`), anders weglaten |

- Klaviyo per bericht: `add_tracking_params: true`, `custom_tracking_params` = source, medium, campaign. `utm_content` en `utm_term` hard in de HTML via `build_template.py` (voorstel 04-utm §5.2, nog niet gebouwd).
- `/discount/<code>?redirect=`-links: UTM's URL-gecodeerd binnen `redirect`. Checkout-links: `&utm_...` achteraan. Nooit een code of persoonsgegeven in een UTM.
- Het schema uit `research/timing/03-meten.md` (`{mail}-{blok}-{positie}`) vervalt; de positie is af te leiden uit `cta1..3` en de bloknaam.

### 1.6 Tests en holdouts (uit `research/testing/02-testroadmap.md`)

| Fase | Periode | Checkout | Cart | Browse | Welcome | Post-purchase | Winback | Nieuwe flows |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | livegang t/m 19 nov | T01 oud/nieuw 50/50, T02 code/geen code | T01, T02 | T01, T05a onderwerp B1 (T02 op B2-clicked telt gepoold) | T01, T04 W1-A/W1-B | T02 (P3), voor/na-vergelijking | T02 (R2, R2-VIP), voor/na | 4 weken geen test, baseline |
| bevriezing | 20 nov t/m 6 dec | v3 100%, oud pad uit, T02 100% code | idem | idem | idem (T04 mag doorlopen, apart rapporteren) | T02 100% code | idem | V1/N2 100% code |
| 2 | 7 dec t/m eind jan | T02, T03 HI10 in vroege mails (padsplit) | T02, T03 | T03, T08 lengte B2-notclicked | T05b onderwerp W1, T07 hero W3 | T02 | T02 | V1 en N2 als extra stratum in T02 |
| 3 | februari en later | T10 10/15% C4-S, T11 C5, T06 timing | | timing B1 1u/4u | T09 unieke welkomstcode, T13 holdout (alleen na akkoord) | timing P3 | | |

Na de T02-beslissing: permanent **10% holdout** (de verliezende arm blijft 10% krijgen). Maximaal 2 tests per flow; T02 telt gepoold als één test.

**T01-padsplit** (checkout, cart, browse, welcome), direct na de trigger:

```
CONDITIONAL SPLIT "T01" · Random sample (profile-sample) 50%
  JA  → Update profile property: v3_arm = new, v3_arm_flow = <flow>, v3_arm_at = vandaag → v4-pad
  NEE → Update profile property: v3_arm = old, v3_arm_flow = <flow>, v3_arm_at = vandaag → oud pad
        (zelfde wachttijden en template-ID's als het beste oude pad, zie per flow)
```
Op 20 november: split naar 100% JA (of verwijderen) en oude flows op Draft. Cohortconversie per arm (7 dagen, welcome 14) beslist; Klaviyo-RPR is het rapportcijfer.

### 1.7 Categorie-router (bouwstenen, exact uit `research/tailoring/03-routing.md`)

Vier paden in elke verkoop- en klantflow: **KOOKGEREI**, **SET**, **ACCESSOIRE** (geen kookgerei of set; 15% van de checkouts, 9,5% van de orders), **BESTAANDE KLANT** (geen merkuitleg C2, geen brug-mail C3-acc). Internationaal is een regel, geen pad: prijzen alleen bij USD (cart) of verzendland US (post-purchase, winback). C4 en W4 blijven op land gesplitst.

- `KOOK_TITELS` (exact, `Items` contains-any): Titanium Hammered Pan Pro Standard · Titanium Hammered Pan Pro Large · Titanium Hammered Pan Pro Small · Titanium Hammered Pan Pro Mini · Titanium Pan Pro · Titanium Hammered Deep Pan Pro · Titanium Hammered Wok Pan Pro · Titanium Hammered Crêpe Pan Pro · Titanium Hammered Pizza Steel · Titanium Hammered Roasting Pan · 2 Litre Titanium Hammered Pot With Lid · 3 Litre Titanium Hammered Pot With Lid · 7,5 Litre Titanium Hammered Pot With Lid · Pot Set With Lids 6-Pcs (titel nakijken in een echte order) · Titanium Hammered Pan Pro With Lid · Titanium Hammered Pan Pro & Utensil Set · Titanium Cook & Prep Bundle
- `SET_TITELS`: Titanium Hammered Pan Set With Lids | 6-Pcs · Titanium Hammered Cookware Set | 12-Pcs · Titanium Hammered Cookware Set Pro · Titanium Hammered Complete Edition · Titanium Hammered – Complete Edition · Full Hammered Pro Edition · The Just Everything Bundle | 34-Pcs · 2 Pans + 2 Lids · Titanium Hammered Pan Pro Duo · Titanium Hammered Pro Duo · Titanium Hammered Pan Pro Kit · 12 pcs cookware set · Titanium-Hammerpfannenset mit Deckel | 6-teilig
- `PANPRO_TITELS`: de vijf Pan Pro-titels (Standard, Large, Small, Mini, Titanium Pan Pro) plus Titanium Hammered Pan Pro With Lid
- `VORM_TITELS`: Titanium Hammered Deep Pan Pro · Titanium Hammered Wok Pan Pro · Titanium Hammered Crêpe Pan Pro
- `DEKSEL_TITELS`: Stainless Steel Lid · Titanium Hammered Pan Pro With Lid
- `SCHORT_TITELS`: de vier titels "Siraat Signature Apron" (Azure, Moss, Ember, Oak); exacte schrijfwijze bij de bouw uit een echt Placed Order-event kopiëren
- `KOOK_WOORDEN` (substring, OR, voor `Product Name` bij Added to Cart en `Name` bij Viewed Product): `Hammer`, `Pan`, `Pot`, `ookware`, `Everything`, `fanne`, `Prep Bundle`
- `HEEFT_GEKOCHT`: What someone has done · Placed Order · at least once · over all time
- `HEEFT_KOOKGEREI`: Placed Order where `Items` contains-any (KOOK_TITELS + SET_TITELS) · at least once · over all time
- `ORDER_2`: Placed Order · equals 2 · over all time

Klaviyo-vorm: `Items` is een lijst, dus "contains any of" met exacte titels. Als een trigger split geen OR tussen twee voorwaarden toestaat, twee trigger splits na elkaar die naar dezelfde mail leiden.

---

## 2. Flows, stap voor stap

Notatie: **CS** = conditional split, **TS** = trigger split, **AB** = A/B-actie in de flow, **UP** = Update profile property. "Filter" = verzendfilter op het bericht (overslaan, niet uitstappen). Alle mails: `klaviyo/templates/v3/<map>/`.

### 2.1 Checkout abandonment · `v4 · Checkout abandonment`

- **Trigger**: Checkout Started (RfMvni). **Trigger filter**: `$value` is greater than 0 (sluit $0-carts met alleen gifts uit, 2%).
- **Flow filters**: Placed Order (RSNxYV) zero times since starting this flow · has not been in this flow in the last 14 days · Received Email where Flow = "v4 · Post-purchase" zero times in the last 7 days.
- **Herinstap**: na 14 dagen. **Exit**: dag 7 (code C4 vervalt 48 uur na verzending op dag 5).
- **Oud pad T01**: "New AB Checkout 1"-pad van Y2TmNB (template-ID's en wachttijden overnemen), `utm_campaign=old-checkout`.

| Stap | Wachttijd (Klaviyo) | Reden (timing) | Split / voorwaarde (exact) | Mail per tak | Verzendfilter | Coupon |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | direct | | CS T01 · random sample 50% (zie 1.6) | JA: v4-pad · NEE: oud pad | | |
| 1 | 30 minuten | Natuurlijke golf na 15 min voorbij (14,3% binnen 15 min, +2,5 pp tot 30 min); 10 min gaf +7% kopers tegen 30 min, niet significant | | **c1.html** (pan-uitleg via `{% if %}` alleen bij kookgerei) | Placed Order = 0 sinds start | geen |
| 2 | direct | | **TS T1**: `Items` contains any of KOOK_TITELS + SET_TITELS | JA → kookgerei-pad (3K) · NEE → accessoire-pad (3A) | | |
| 3K | 1 dag (geen tijd: 24 uur na C1) | 77% van het effect van C1 zit in 24 uur | **CS S1**: HEEFT_GEKOCHT (Placed Order at least once over all time) | JA: geen C2 (bestaande klant) · NEE: **c2.html** | Placed Order = 0 sinds start | geen |
| 4K | 2 dagen, tot 09:00 (= dag 3, 09:00) | Herstel 8,7% (24u) naar 10,6% (3d) | **TS T2a**: `Items` contains any of SET_TITELS → **c3-s.html**. NEE → **TS T2b**: `$value` ≥ 300 → **c3-s.html**. NEE → **TS T3**: `Items` contains any of PANPRO_TITELS **en** `$value` < 250 → **c3-p.html**. NEE → geen C3 (pizza steel, roasting, pot, wok/deep/crêpe alleen, of 2 pannen < $300) | c3-s / c3-p / geen | Placed Order = 0 sinds start | geen |
| 5K | 2 dagen, tot 09:00 (= dag 5, 09:00) | 3d naar 7d nog +1,7 pp; code van 48 uur valt in dat venster | **CS land**: Location · Country equals United States → US. NEE → **TS** `Customer Locale` equals `en-US` en profielland is niet gezet → US. Anders INT (16% heeft geen land) | US / INT | | |
| 6K | direct | | **Code-router** (1.4), pool C4_10_48H | US: **c4-us.html** (A) of **c4-us-nocode** (B, cooldown) · INT: **c4-int.html** of **c4-int-nocode** | Placed Order = 0 sinds start | **C4_10_48H** (A), daarna UP last_flow_code_at |
| 3A | 1 dag (24 uur na C1) | idem 3K | | **c2-acc.html** (feitregel per accessoire, cadeau-hoek) | Placed Order = 0 sinds start | geen |
| 4A | 2 dagen, tot 09:00 (dag 3) | | **CS**: HEEFT_GEKOCHT | JA: geen C3 · NEE: **c3-acc.html** | Placed Order = 0 sinds start | geen |
| 5A-6A | 2 dagen, tot 09:00 (dag 5) | | land-split en code-router zoals 5K-6K | c4-us / c4-int (12-pcs-blok verbergt zich zonder kookgerei) | Placed Order = 0 sinds start | C4_10_48H |
| einde | | Na 7 dagen < 0,3% kans per dag | | | | |

- Onderwerp C1: alleen A "Forgetting something?" (T12: geen C1-onderwerptest; B "Your pan is still here" klopt niet bij 15% accessoire-carts).
- T02-stratum: C4-US, C4-INT. Test T10 (15% voor carts ≥ $300) pas in fase 3.
- Open: C4-code op een e-gift card werkt vermoedelijk niet (tailoring J4).

### 2.2 Cart abandonment · `v4 · Cart abandonment`

- **Trigger**: Added to Cart (QXcV8K). **Trigger filters**: `Price` is greater than 0 · `Product Name` doesn't contain "Mystery Gift" · doesn't contain "E-Book" · doesn't contain "Free Shipping" · doesn't contain "Giveaway" (47% van de events is een automatische gift).
- **Flow filters**: Checkout Started (RfMvni) zero times since starting this flow · Placed Order zero times since starting this flow · Received Email where Flow = "v4 · Checkout abandonment" zero times in the last 7 days · has not been in this flow in the last 14 days.
- **Herinstap**: 14 dagen. **Oud pad T01**: SwkMyn Email #1 t/m #3 (15-min-arm), `old-cart`.

| Stap | Wachttijd | Reden | Split / voorwaarde (exact) | Mail per tak | Verzendfilter | Coupon |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | direct | | CS T01 · random sample 50% | | | |
| 1 | 30 minuten | Cart-verlaters kopen nauwelijks vanzelf na 15 min (+1,0 pp tussen 30 en 60 min); oude 15-min-arm $2,90 tegen $2,27 bij 30 min | **CS K**: Added to Cart where `Product Name` contains "Hammer" OR "Pan" OR "Pot" OR "ookware" OR "Everything" OR "fanne" OR "Prep Bundle" · at least once · in the last 1 day | JA: **k1.html** · NEE: **k1-acc.html** | Checkout Started = 0 en Placed Order = 0 sinds start | geen |
| 2K | 1 dag (24 uur na K1) | Cart-orders komen trager (mediaan 9,5 uur), 24 uur ertussen | **CS**: HEEFT_GEKOCHT | JA: **k2-returning.html** · NEE: **k2-new.html** | idem | geen |
| 3K | 2 dagen, tot 09:00 (dag 3) | Herstel 24u 5,8%, 3d 7,2%, 7d 8,5% | **Code-router**, pool K3_10_48H | **k3.html** (A) / **k3-nocode** (B, cooldown) | idem | **K3_10_48H** |
| 2A | 3 dagen, tot 09:00 (dag 3) | Geen K2: de jaarsom gaat over een pan | **Code-router** | k3 / k3-nocode | idem | K3_10_48H |
| einde | dag 5 | | | | | |

- Geen waarde-split in cart (≥ $300 herstelt niet beter). Prijs in K-mails alleen bij `$currency` USD (gebouwd).
- T02-stratum: K3.

### 2.3 Browse abandonment · `v4 · Browse abandonment`

- **Trigger**: Viewed Product (XNtYMB, Klaviyo onsite). Niet V48nhq.
- **Flow filters**: Added to Cart zero times since starting this flow · Checkout Started zero times since starting this flow · Placed Order zero times since starting this flow · Received Email where Flow = "v4 · Cart abandonment" zero times in the last 7 days · idem "v4 · Checkout abandonment" · idem "v4 · Welcome" zero times in the last 7 days · has not been in this flow in the last 7 days.
- **Herinstap**: 7 dagen. **Oud pad T01**: TyEjuQ (beste van de twee), `old-browse`.

| Stap | Wachttijd | Reden | Split / voorwaarde (exact) | Mail per tak | Verzendfilter | Coupon |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | direct | | CS T01 · random sample 50% | | | |
| 1 | 1 uur | Na 15 min koopt nog 1,9% binnen 1 uur: weinig te storen; cart/checkout vuurt eerst | **TS**: `Name` contains "Hammer" OR "Pan" OR "Pot" OR "ookware" OR "Everything" OR "fanne" OR "Prep Bundle" | JA: **b1.html** (AB T05a onderwerp) · NEE: **b1-acc.html** | Placed Order = 0 sinds start | geen (HI10 in de mail, zie 3.1) |
| 2K | 2 dagen, tot 09:00 (dag 2) | 78% van de orders na een browsemail binnen 48 uur | **CS**: Clicked Email where `$message` = B1 · at least once · since starting this flow | JA → **code-router** (pool B2_10_48H): **b2-clicked.html** / **b2-clicked-nocode** · NEE → **b2-notclicked.html** | idem + Added to Cart = 0 sinds start | **B2_10_48H** (clicked, A) |
| 2A | 2 dagen, tot 09:00 | | **CS**: Clicked Email where `$message` = B1-acc · at least once · since starting this flow | JA → code-router → b2-clicked (dynamisch) / nocode · NEE → einde | idem | B2_10_48H |
| einde | dag 3 | | | | | |

- T05a (fase 1): B1-onderwerp A "Lab-tested: nothing on this pan to scratch off" (authority) tegen B "100,000+ happy customers cook on this pan" (social proof). Vervangt de A/B uit de topcomment van b1.html (die test twee variabelen).

### 2.4 Welcome · `v4 · Welcome`

- **Trigger**: toegevoegd aan lijst Uw8eZG (Alia Card Game; $source "Alia sign-up").
- **Flow filters**: Email doesn't contain "test@" · has not been in this flow over all time. **Herinstap**: nooit.
- **Verzendfilter op elke W-mail**: Placed Order zero times since starting this flow **en** Received Email where Flow = "v4 · Checkout abandonment" zero times in the last 1 day **en** idem "v4 · Cart abandonment" (overslaan, niet uitstappen).
- **Oud pad T01**: SiaNLu actieve tak "DG" (template-ID's en wachttijden), plus T2SmtR blijft voor dit pad live met extra flow-filter `v3_arm equals old`. `utm_campaign=old-welcome`.

| Stap | Wachttijd | Reden | Split / voorwaarde (exact) | Mail per tak | Verzendfilter | Coupon |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | direct | | CS T01 · random sample 50% | | | |
| 1 | 20 minuten | 20,3% koopt binnen 10 min na inschrijving (inschrijving tijdens aankoop); split op moment nul stuurt kopers het prospect-pad in (nu krijgt 10,7% van mail 2 hem na aankoop) | **CS A1**: Placed Order at least once · since starting this flow | JA → einde (post-purchase neemt over) · NEE → A2 | | |
| 2 | direct | | **CS A2**: HEEFT_GEKOCHT (Placed Order at least once over all time) | JA → **w0.html** → einde (1,3% was al klant) · NEE → prospect | | geen |
| 3 | direct | 1,3% koopt nog op dag 0 na het eerste uur | **AB T04** 50/50, geen auto-winnaar | A: **w1-a.html** (HI10 code-blok) · B: **w1-b.html** (HI10 als gift card) | standaard | HI10 (publiek) |
| 4 | 1 dag, tot 09:00 (dag 1) | Kans op eerste order 0,50% op dag 1, hoogste na dag 0 | | **w2.html** (tekst, Benjamin) | standaard | HI10 in P.S. |
| 5 | 2 dagen, tot 09:00 (dag 3) | 0,24% | | **w3.html** | standaard | HI10 |
| 6 | 3 dagen, tot 09:00 (dag 6) | 0,13% | **CS B**: Location · Country equals United States | JA: **w4-us.html** · NEE: **w4-int.html** | standaard | HI10 |
| 7 | 4 dagen, tot 09:00 (dag 10) | 0,09%; oude dag-10 "Last Call" $0,26 per ontvanger | | **w5.html** | standaard | HI10 (besluit A) |
| einde | dag 14 | Vanaf dag 14 is welcome niet sterker dan 0,04-0,06% per dag | | Naar campagnes; segment "v4 · Welcome-bescherming" sluit 14 dagen uit | | |

- Failure to launch (T2SmtR): uit voor het nieuwe pad vanaf livegang, helemaal op Draft op 20 november (37% van de flowmails, 3,9% van de flowomzet).
- Topcomments van de W-mails noemen 10:00 en W5 op dag 9: deze tabel gaat voor.

### 2.5 Post-purchase · `v4 · Post-purchase` (plus hulpflow 2.5b)

- **Trigger**: Placed Order (RSNxYV). **Flow filter**: has not been in this flow in the last 30 days.
- **Geen T01** (methode C: voor/na tegen dezelfde kalenderweken in de baseline). RL3TU6 gaat op Draft op het moment dat deze flow live gaat.

| Stap | Wachttijd | Reden | Split / voorwaarde (exact) | Mail per tak | Verzendfilter | Coupon |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 uur (realtime, ook 's avonds) | Bevestiging; 72-78% klikt naar care-use | **CS**: Placed Order equals 1 over all time | JA: **p1-first.html** (intro, tijdlijn, chef-tip alleen bij kookgerei via `{% if %}`) · NEE: **p1-repeat.html** | geen | geen |
| 1b | (besluit Floris) | Oude "It's On Its Way" 29,8% klik, 96% op tracking | | Tracking-mail bij Fulfilled Order (VtEiZT): **niet gebouwd**, alleen als Shopify de verzendmail niet al stuurt (besluit 3.13) | | |
| 2 | 16 dagen, tot 09:00 (dag 16) | Levering mediaan 11,7 d, p75 14,7; maar maar 36% krijgt een Delivered Shipment-event (US 37%, CA 9%, overig 1%) | **TS**: `Items` contains any of KOOK_TITELS + SET_TITELS. NEE → geen P2. JA → **CS**: Delivered Shipment (VcUF33) at least once since starting this flow | JA: geen (P2 al via 2.5b) · NEE: **p2-safe** (vangnet, tekst "When your pan arrives"; nog te schrijven) | Refunded Order (Xg6cwn) = 0 in 30 dagen | geen |
| 3 | 4 dagen, tot 09:00 (dag 20) | Levering + ~8 dagen voor de mediaan; herhaalkoop 14-21 dagen 12,4% van herhalers; dag 20 valt na U1 (levering +4) en vóór review (levering +14 bij snelle levering, zie 3.9) | **CS R0**: ORDER_2 (Placed Order equals 2 over all time) → JA: einde (VIP V1 neemt over) | | | |
| 3a | direct | | **TS A**: `Items` contains any of KOOK_TITELS + SET_TITELS → kookgerei-router. NEE → accessoire-router | | | |
| 3K | direct | | **TS A1**: `Items` contains any of SET_TITELS → p3-set; NEE → **TS** `$value` ≥ 300 → p3-set; NEE → **TS A2**: `Items` contains any of DEKSEL_TITELS → p3-next; NEE → **TS A3**: `Items` contains any of PANPRO_TITELS + VORM_TITELS → p3-pan; NEE → p3-accessory (pizza steel, roasting, pots: "Now meet the pan") | **p3-set** / **p3-next** / **p3-pan** / **p3-accessory**, elk via code-router | Placed Order = 0 sinds start, Refunded Order = 0 in 30 dagen | **P3_THANKYOU_10_14D** |
| 3A | direct | | **TS B1**: `Items` contains any of "E-Gift Card" → einde (UYALJ8 bestaat). NEE → **CS B2**: HEEFT_KOOKGEREI → p3-next. NEE → **TS B3**: `Items` contains any of SCHORT_TITELS → p3-apron. NEE → p3-accessory | **p3-next** / **p3-apron** / **p3-accessory**, elk via code-router | idem | P3_THANKYOU_10_14D |
| 4 | | Review: levering + 14 dagen | | Live flow **XzHrez**, ongewijzigd | | geen |

- Code-router per P3-mail: cooldown → `<mail>-nocode`; anders AB T02: A met code (+ UP last_flow_code_at, pool P3_THANKYOU_10_14D), B `-nocode`. T02-strata: P3-pan, P3-set, P3-accessory (P3-next en P3-apron als extra strata).
- P3-pan zegt "Pick the same diameter as your pan" (deep 24 cm heeft geen deksel: geaccepteerd risico).
- P3-pan, P3-set, P3-accessory tonen nog USD aan iedereen; zelfde `country_code == 'US'`-regel als P3-next toevoegen (tailoring J1, template-werk).

### 2.5b Post-purchase · levering · `v4 · Post-purchase · levering`

- **Trigger**: Delivered Shipment (VcUF33).
- **Flow filters**: Placed Order where `Items` contains any of KOOK_TITELS + SET_TITELS · at least once · in the last 30 days (het event zelf heeft geen Items) · has not been in this flow in the last 30 days · Received Email where Flow = "v4 · Post-purchase" and Message = P2-safe zero times in the last 30 days.

| Stap | Wachttijd | Reden | Mail | Verzendfilter |
| --- | --- | --- | --- | --- |
| 1 | 1 dag, tot 09:00 | "Nu je pan er is" hoort op levering te wachten | **p2.html** | Refunded Order = 0 in 30 dagen |

### 2.6 Winback · `v4 · Winback`

- **Trigger**: Placed Order (RSNxYV), daarna wachten.
- **Flow filter**: geen herinstapgrens (elke order start de klok opnieuw; de vorige run stopt via de verzendfilter). Zie besluit 3.11.
- **Verzendfilter op elke mail**: Placed Order zero times since starting this flow.
- Geen T01 (voor/na). UEfh4h op Draft bij livegang.

| Stap | Wachttijd | Reden | Split / voorwaarde (exact) | Mail per tak | Extra verzendfilter | Coupon |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 45 dagen, tot 09:00 | Mediaan tot 2e order 35 dagen; 57% van de herhaalaankopen binnen 45 dagen; dag 30-60 1,65%, dag 60-90 0,97% | **TS**: `Items` contains any of KOOK_TITELS + SET_TITELS. JA → **TS** `Items` contains any of SET_TITELS of (tweede TS) `$value` ≥ 300 → **r1-set.html**, anders **r1-pan.html**. NEE → **CS** HEEFT_KOOKGEREI → JA **r1-pan.html** · NEE **r1-acc.html** | r1-set / r1-pan / r1-acc | Received Email where Flow = "v4 · Post-purchase" zero in 7 dagen; idem "v4 · VIP" zero in 7 dagen | geen (HI10 in de mail) |
| 2 | 30 dagen, tot 09:00 (dag 75) | Kans dag 60-90 nog bijna 1% | **CS VIP**: Placed Order at least 2 over all time | JA → code-router (pool R2_VIP_15_72H): **r2-vip.html** / r2-vip-nocode · NEE → code-router (pool R2_10_72H): **r2.html** / r2-nocode | | **R2_VIP_15_72H** (15%, 72 u) / **R2_10_72H** (10%, 72 u) |
| einde | dag 90 | Daarna 0,6% per 30 dagen: campagnewerk | | | | |

- R2 alleen versturen zolang "up to 50% off" echt live is (bestaande regel uit de templates).
- T02-strata: R2, R2-VIP. R3 ("expires tonight" voor R2-clickers) niet bouwen.

### 2.7 Site abandonment · `v4 · Site abandonment` (nieuw)

- **Trigger**: Active on Site (UdCdLD, API). Niet TF6iAL (zelfde naam, geen events).
- **Flow filters**: can receive email marketing · Viewed Product, Added to Cart, Checkout Started, Placed Order zero times since starting this flow · Placed Order zero times in the last 30 days · Received Email where Flow = "v4 · Browse abandonment" / "v4 · Cart abandonment" / "v4 · Checkout abandonment" / "v4 · Post-purchase" zero times in the last 7 days · Received Email where Flow = "v4 · Welcome" zero times in the last 10 days · has not been in this flow in the last 14 days.
- **Herinstap**: 14 dagen. Geen tests in de eerste 4 weken.

| Stap | Wachttijd | Reden | Mail | Verzendfilter | Coupon |
| --- | --- | --- | --- | --- | --- |
| 1 | 2 uur | Lage intentie; geen eigen timingdata. Exit naar browse als iemand een product bekijkt | **a1.html** (maatkeuze) | Viewed Product, Added to Cart, Checkout Started, Placed Order = 0 sinds start | HI10 (publiek, geen unieke code) |
| 2 | 2 dagen, tot 09:00 | 09:00-regel (spec zei 10:00) | **a2.html** (bestsellers) | idem | HI10 |

### 2.8 Sunset · `v4 · Sunset` (vervangt S7V4a7)

- **Trigger**: segment **"v4 · Sunset · unengaged 120d"**: can receive email marketing · profiel aangemaakt meer dan 120 dagen geleden · Clicked Email (W247h8) where Bot Click is false zero times in the last 120 days · Active on Site (UdCdLD) zero times in the last 120 days · Placed Order zero times in the last 180 days · Received Email (YkRM4Q) at least 8 times in the last 120 days. Opens tellen niet.
- **Flow filters**: has not been in this flow in the last 180 days · Received Email where Flow = "v4 · Welcome" zero in 30 dagen · idem "v4 · Post-purchase" zero in 30 dagen.

| Stap | Wachttijd | Mail / actie | Verzendfilter |
| --- | --- | --- | --- |
| 1 | 1 dag, tot 09:00 | **s1.html** ("Yes, keep me on the list") | |
| 2 | 4 dagen, tot 09:00 | **s2.html** (tekst, afzender Benjamin) | Clicked Email, Active on Site, Placed Order zero times since starting this flow (geen Opened Email-filter: zie 3.16) |
| 3 | 3 dagen | **CS**: Clicked Email at least once since starting this flow OR Active on Site at least once since starting this flow OR Placed Order at least once since starting this flow | JA: UP `sunset_status = kept` → einde · NEE: UP `sunset_status = suppressed`, `sunset_at = vandaag` → einde |

Suppressie: segment `sunset_status equals suppressed` wekelijks bulk-suppressen (handmatig of via routine, na akkoord). Geen A/B; meten: % kept, spam- en bounceratio account-breed.

### 2.9 VIP · `v4 · VIP` (nieuw)

- **Trigger**: Placed Order (RSNxYV). **Flow filters**: Placed Order equals 2 over all time · has not been in this flow over all time · can receive email marketing.

| Stap | Wachttijd | Split / voorwaarde | Mail | Verzendfilter | Coupon / actie |
| --- | --- | --- | --- | --- | --- |
| 1 | 30 dagen, tot 09:00 | Code-router (pool SK_REGULARS15_14D). Eerste 4 weken: zonder T02-split (100% code bij geen cooldown); daarna stratum in T02 | **v1.html** / **v1-nocode** (zelfde mail met HI10; nog te bouwen) | Refunded Order zero since start; Placed Order zero in the last 14 days | **SK_REGULARS15_14D**; UP last_flow_code_at, last_flow_code_pool, `siraat_regular = true` |
| 2 | 10 dagen, tot 09:00 | | **v2.html** (tekst, Benjamin; geen tweede coupon-tag) | Placed Order zero since start; Refunded Order zero since start | geen |
| einde | | Winback R1 (dag 45) wordt overgeslagen door de VIP-filter; R2-VIP (dag 75) mag een code, 45 dagen na V1 | | | |

P3 slaat order 2 over (2.5 stap 3), dus V1 is de enige code na de 2e order.

### 2.10 Anniversary · `v4 · Anniversary` (nieuw)

- **Trigger**: Placed Order (RSNxYV). **Trigger filter**: `Items` contains any of KOOK_TITELS + SET_TITELS. **Flow filters**: Placed Order equals 1 over all time · has not been in this flow over all time.

| Stap | Wachttijd | Mail | Verzendfilter | Coupon |
| --- | --- | --- | --- | --- |
| 1 | 182 dagen, tot 09:00 | **n1.html** (service, geen codebalk, HI10 onder producten) | Refunded Order zero since start; Received Email where Flow = "v4 · VIP" or "v4 · Winback" zero in 14 dagen; Opened Ticket (YzvjGf) zero in 14 dagen | geen |
| 2 | 183 dagen, tot 09:00 (dag 365) | Code-router (pool SK_ANNIV10_7D): **n2.html** / **n2-nocode** | Refunded Order zero since start; Placed Order zero in 14 dagen | **SK_ANNIV10_7D**; UP last_flow_code_at |

- Controleren of Klaviyo 182 en 183 dagen in één delay accepteert; zo niet, delays van 91 dagen achter elkaar.
- Loopt alleen voor orders na livegang. Backfill (eerste order 360-367 dagen geleden, wekelijkse campagne met kopie van N2) is een besluit (3.15).

### 2.11 UGC first egg · `v4 · UGC first egg` (nieuw)

- **Trigger**: Delivered Shipment (VcUF33). **Flow filters**: Placed Order equals 1 over all time · HEEFT_KOOKGEREI · has not been in this flow over all time · zelfde backorder-uitsluiting op producttitels als XzHrez.
- Bereik: alleen orders met een Delivered Shipment-event (36%; UK 91%, AU 86%, US 37%).

| Stap | Wachttijd | Mail | Verzendfilter | Incentive |
| --- | --- | --- | --- | --- |
| 1 | 4 dagen, tot 09:00 | **u1.html**, reply-to support@siraatskitchen.com | Opened Ticket (YzvjGf) zero since start; Refunded Order zero in 30 dagen; Fulfilled Order (VtEiZT) at least once in 60 dagen | 15% via Gorgias-macro uit Shopify-bulkpool UGC15- (1 gebruik, 60 dagen), na een foto |

Spec zei levering +6; naar +4 zodat U1 niet de dag vóór of na P3 valt (3.10).

---

## 3. Conflicten en besluiten

"Keuze" = wat in sectie 2 staat. "Floris" = wat hij moet beslissen voordat er iets live gaat.

| # | Onderwerp | Bronnen die botsen | Keuze in v4 | Floris |
| --- | --- | --- | --- | --- |
| 3.1 | **HI10 in vroege mails** (C1-C3, K1, K2, B1, B2-notclicked, a1, a2) | Gebouwd: HI10 in hero, codebalk en onderwerp B. Offer-strategie §4: geen code in de eerste 48 uur (C1 zonder code was de beste mail van het account, $4,28-7,86). Testplan T03: pas in fase 2 testen, eerst akkoord. | Live zoals gebouwd (met HI10). T03 in fase 2 met `-nohi10`-varianten. Reden: templates niet wijzigen, en T01 meet nu het hele v3-pakket; een tweede padsplit in fase 1 maakt drie tests per flow. | Akkoord op T03 (de test, niet de uitkomst). Als hij liever direct zonder HI10 in C1/K1 start: 9 `-nohi10`-templates eerst bouwen en T03 vervalt. |
| 3.2 | **C1 na 30 min of 1 uur** | Timing: 30 min. v3, templates (SEND) en testplan T06: 1 uur ("met HI10 in C1 is later goedkoper"). | **30 min.** Data: na 15 min is de natuurlijke golf voorbij; 10 tegen 30 min gaf +7% kopers. De HI10-kosten van de 1,7 pp die tussen 30 en 60 min vanzelf koopt zijn kleiner dan het risico de hete sessie te missen. T06 alleen in fase 3. | Bevestigen. |
| 3.3 | **K1 30 min** | v3 1 uur; oude 15-min-arm deed beter ($2,90 tegen $2,27). | 30 min. | Geen. |
| 3.4 | **B1 na 1 uur of 4 uur** | Timing 1 uur; v3, template en routing 4 uur. | 1 uur (cart/checkout vuren eerst via de filters, die op verzendmoment checken). Timingtest 1u/4u pas in fase 3 (fase 1 heeft al T01 en T05a in browse). | Bevestigen; browse heeft de hoogste uitschrijving (1,42%), dus de eerste 2 weken uitschrijving per mail volgen. |
| 3.5 | **C2/K2 24 uur of "dag 2, 09:00"; quiet hours** | Timing: 24 uur na mail 1 binnen 09:00-20:00. v3: tot dag 2, 09:00 (21-08 quiet hours). Klaviyo kan bij uur-delays geen venster afdwingen. | "Wacht 1 dag" zonder tijd (24 uur, zelfde uur als mail 1). Nachtzendingen alleen als de checkout zelf 's nachts was (22-24 uur ~8% van de realtime-zendingen). Alle andere vervolgmails "X dagen, tot 09:00". Quiet hours 22-07 in plaats van 21-08. | Bevestigen; alternatief is overal "tot 09:00" (dan C2 soms al 9 uur na C1). A/B 2 uit timing pas als checkout/cart een testplek vrij hebben. |
| 3.6 | **C3/C4 dag 3 en 4 of 3 en 5; codeduur** | v3 dag 3/4; timing dag 3/5 met code 72 uur; templates en coupon C4_10_48H: 48 uur. | Dag 3 en dag 5, code **48 uur** (zoals gebouwd); exit dag 7. | Geen. |
| 3.7 | **Welcome-start** | v3: split meteen, W0/W1 na 10 min, 10:00, W5 dag 9, einde dag 10. Timing: 20 min wachten, dan split op "order sinds start", 09:00, W5 dag 10, einde dag 14. | Timing. Plus overslaan bij checkout/cart-mail in 24 uur. | Geen. |
| 3.8 | **Review 14 of 30 dagen na levering** | v3: 30 dagen. Live XzHrez en PLAYBOOK: 14 dagen. | **14 dagen**, XzHrez ongewijzigd. | Geen. |
| 3.9 | **P3-moment** | v3, templates, routing: order + 14 dagen. Timing: levering + 7, vangnet order + 21 (de helft heeft op dag 14 de pan nog niet). Maar levering is maar voor 36% bekend. | **Order + 20 dagen, 09:00** voor iedereen (≈ levering + 8 bij mediaan 11,7). Eén router, geen afhankelijkheid van een onbetrouwbaar event. Timingtest P3 (levering +7 tegen +14) in fase 3. | Bevestigen. |
| 3.10 | **U1 en P3 vlak na elkaar** | U1 levering + 6 (nieuwe flows) en P3 levering + 7 (timing) = twee mails op opeenvolgende dagen. | U1 naar **levering + 4**; P3 order + 20. Volgorde bij mediaan: P2 dag 13, U1 dag 16, P3 dag 20, review dag 26. | Geen. |
| 3.11 | **Winback-moment en herinstap** | v3 60/90 dagen, herinstap 90. Timing 45/75. Herinstap 90 betekent dat een 2e order binnen 90 dagen geen nieuwe winback start. | **45/75**, geen herinstapgrens (elke order herstart, oude run stopt via filter). | Geen. |
| 3.12 | **VIP, P3 en winback overlappen** | VIP-spec: V1 "na het P3-codevenster". Routing: P3 slaat order 2 over. Timing: R1 dag 45 valt 5 dagen na V2 (dag 40). | P3 niet bij order 2; R1 overgeslagen bij een VIP-mail in 7 dagen; R2-VIP op dag 75 mag (cooldown verstreken). | Geen. |
| 3.13 | **P1b tracking-mail** | Timing: oude verzendmail 29,8% klik, 96% op tracking. Niet gebouwd. | Niet in v4. | Stuurt Shopify al een verzendmail met tracking? Zo niet: P1b bouwen (Fulfilled Order VtEiZT + 0). |
| 3.14 | **Codebreedte en holdout** | Offer-strategie: holdout 10-20%. Testplan T02: 50/50, daarna permanent 10%. Nieuwe flows: V1 holdout 20%; testplan: 4 weken geen test. | T02 50/50 in fase 1-2, daarna 10% permanent. V1 en N2 eerst 4 weken 100% code, dan stratum in T02. | Brutomarge bevestigen (breakeven: 60% marge = +20% kopers voor 10%, +33% voor 15%). |
| 3.15 | **HI10-tak voor welcome-leden in laatste mails** | Offer-strategie: wie op Uw8eZG staat krijgt in C4/K3/B2 een HI10-herinnering, geen unieke code. Testplan: die tak telt niet in T02. Uw8eZG heeft 214k profielen: bijna elke verlater staat erop, dan gaat er nauwelijks een unieke code uit. | **Geen HI10-tak.** Iedereen zonder cooldown in T02. Een unieke code vervangt HI10 (één code per order). | Bevestigen. Anders: drie extra `-hi10`-templates en T02 krijgt veel minder volume. |
| 3.16 | **Sunset S2 en opens** | Spec: opens tellen niet (Apple MPP). Topcomment s2.html: Opened Email = 0 als verzendfilter. | Spec: geen Opened Email-filter. | Geen. |
| 3.17 | **Coupon-namen** | Offer-strategie: SK_CART10_48H, SK_CHECKOUT10_48H enz. Templates: C4_10_48H, K3_10_48H, B2_10_48H, P3_THANKYOU_10_14D, R2_10_72H, R2_VIP_15_72H. Nieuwe flows: SK_REGULARS15_14D, SK_ANNIV10_7D. | Namen zoals in de templates (templates niet wijzigen). Prefixen per pool voor Shopify-rapportage (4.4). | Geen. |
| 3.18 | **UTM-schema** | Timing 03-meten: `{mail}-{blok}-{positie}`. Testing 04-utm: `<mailid>-<blok>` + `utm_term`. | 04-utm. | Geen. |
| 3.19 | **Onderwerp-A/B's** | Topcomments hebben A/B per mail. Testplan: max 2 tests per flow; T12 geen C1-test; T05a vervangt B1-A/B. | Alleen T04 (W1) en T05a (B1) in fase 1. Overige mails: onderwerp A. Te lange onderwerpen/previews (5) eerst inkorten. | Geen. |
| 3.20 | **6-delige set $349** | DECISIONS: $349. Shopify: actief product $399, $349 alleen op UNLISTED `...-6-pcs-bday-sale`. | Links naar de bday-sale-listing (QA-patch 04 toegepast). | Hoe lang blijft de bday-sale-listing live? Als hij stopt moeten C3-P, W4, P3-accessory, R2, R2-VIP, V1, A2 en N2 mee. |
| 3.21 | **E-book-link** | DECISIONS: /products/e. QA A16: dat is een betaalpagina ($50); gratis variant `/products/the-green-e-guide-free`. | Volgt DECISIONS tot Floris anders zegt. | Welke link in P1 "Download your e-book"? |
| 3.22 | **Lekkende publieke codes** | Offer-strategie en meetkader: BFEXTRA10 (7.626 keer), NYEXTRA10, NTWDHPKL5C, EXTRA30, COOK10, COOKHAPPY, GOODFOOD en drie 100%-codes zonder limiet maken T02 en elke deadline zwak. | Voorwaarde vóór T02. | Deactiveren of einddatum geven (Shopify, Floris). |
| 3.23 | **PFAS-trekking** | Offer-strategie en QA A21: "chance to win with your order" zonder officiële regels en "no purchase necessary" is in de VS een risico. | Copy blijft "win" (DECISIONS). | Regels-pagina laten maken; daarna pas "draw closes Sunday" als urgentie. |
| 3.24 | **"Independent" lab** | C2 en W3 zeggen "An independent lab report?"; DECISIONS verbiedt "independent" (bij Trustpilot). | Ongewijzigd tot besluit. | Mag "independent" voor het lab? Anders "accredited". |
| 3.25 | **Welcome-holdout en unieke welkomstcode** | T13 gaat in tegen "HI10 blijft"; besluit B (unieke 10-dagen-code) is T09. | Niet ingepland. | Akkoord op T13 en/of besluit B voor fase 3. |
| 3.26 | **Anniversary-backfill** | Flow loopt alleen voor nieuwe orders; jaarmail pas in oktober 2027. | Niet ingepland. | Wekelijkse backfill-campagne met N2-kopie: ja of nee. |
| 3.27 | **75-year warranty op accessoires** | K3 noemt "dents, warped base, loose handles" ook bij een schort-cart. | Ongewijzigd. | Geldt de garantie winkelbreed? |

---

## 4. Bouwlijst voor Klaviyo (in volgorde)

Alles hieronder is nog niet aangemaakt. Volgorde: voorwaarden, objecten, templates, flows (op Draft), test, live in één moment per flowgroep.

### 4.1 Voorwaarden (Floris / buiten Klaviyo)

1. Besluiten uit sectie 3 (3.1, 3.2, 3.5, 3.13, 3.14, 3.15, 3.20, 3.21).
2. Publieke lekcodes dicht (3.22). 3. PFAS-regels-pagina (3.23). 4. Reply-to support@ in Gorgias bevestigen. 5. Gorgias-regel en macro voor UGC (tag `ugc-photo`, code uit UGC15-pool) en een plek voor foto's met toestemming.

### 4.2 Profieleigenschappen (ontstaan via flow-acties "Update profile property")

| Eigenschap | Waarden | Gezet in | Gebruik |
| --- | --- | --- | --- |
| `v3_arm` | new / old | T01-split in checkout, cart, browse, welcome | cohortconversie per arm; filter op T2SmtR |
| `v3_arm_flow` | checkout / cart / browse / welcome | idem | idem |
| `v3_arm_at` | datum | idem | venster na instroom |
| `test_t03` | a / b | fase 2 | T03 |
| `last_flow_code_at` | datum | na elke codemail (A-arm) | cooldown 30 dagen |
| `last_flow_code_pool` | poolnaam | idem | kostentoewijzing |
| `siraat_regular` | true | V1 | VIP-segment |
| `sunset_status` | kept / suppressed | Sunset stap 3 | suppressie |
| `sunset_at` | datum | Sunset stap 3 | herinschrijving volgen |

### 4.3 Segmenten

| Naam | Definitie | Voor |
| --- | --- | --- |
| v4 · Sunset · unengaged 120d | zie 2.8 | trigger Sunset |
| v4 · Sunset · suppressed | `sunset_status` equals suppressed | wekelijkse suppressie |
| v4 · Welcome-bescherming | Subscribed to List (SCvkku) Uw8eZG in de laatste 14 dagen **en** Placed Order zero times in 14 dagen (of: lid van Uw8eZG toegevoegd < 14 dagen) | uitsluiten bij campagnes |
| v4 · Campagne-cap | Received Email zonder flow at least 3 times in the last 7 days | uitsluiten bij campagnes |
| v4 · Heeft kookgerei | HEEFT_KOOKGEREI | rapportage, controles |
| v4 · VIP | Placed Order at least 2 over all time | rapportage |
| v4 · US | Location · Country equals United States | rapportage (splits gebruiken de voorwaarde direct) |
| v3_arm = new / old + order 7d | `v3_arm` equals new/old **en** `v3_arm_flow` equals X **en** Placed Order at least once in the last 7 days | T01-cohort (8 segmenten: 4 flows x 2 armen) |
| Optioneel: "Mail uit flow X in 7 dagen" | Received Email where Flow = X in 7 dagen | alleen als de Flow-dimensie in flowfilters niet werkt (1.2) |

### 4.4 Coupons (Klaviyo > Coupons > Shopify > unique codes)

Elke pool: unieke codes, **1 gebruik, 1 per klant**, alleen one-time purchase products, vervaltijd na toewijzing, geen einddatum op de pool zelf.

| Pool (exact zoals in de templates) | Prefix (voorstel) | Korting | Vervalt na | Mail |
| --- | --- | --- | --- | --- |
| C4_10_48H | CO- | 10% | 48 uur | c4-us, c4-int |
| K3_10_48H | CART- | 10% | 48 uur | k3 |
| B2_10_48H | VIEW- | 10% | 48 uur | b2-clicked |
| P3_THANKYOU_10_14D | THX- | 10% | 14 dagen | p3-pan, p3-set, p3-next, p3-apron, p3-accessory |
| R2_10_72H | BACK- | 10% | 72 uur | r2 |
| R2_VIP_15_72H | VIP- | 15% | 72 uur | r2-vip |
| SK_REGULARS15_14D | REG- | 15% | 14 dagen | v1 |
| SK_ANNIV10_7D | YEAR- | 10% | 7 dagen | n2 |
| UGC15 (Shopify bulk, niet Klaviyo) | UGC15- | 15% | 60 dagen | Gorgias-macro na U1 |

Niet aanmaken: W5_10_72H (alleen als besluit B), C4-S 15% (T10, fase 3). Na aanmaken: preview met testprofiel per codemail (code verschijnt, overal dezelfde, link `/discount/<code>` werkt).

### 4.5 Templates

1. Hero's en productbeelden van alle mappen uploaden naar de Klaviyo-bibliotheek en `assets/klaviyo-urls.txt` per map aanvullen (nu staan er alleen logo en social in; browse, cart, checkout en welcome hebben nog geen bestand). Dan `scripts/build_all.sh` voor de `.klaviyo.html` (nu alleen s2 en v2).
2. UTM-ondersteuning in `build_template.py` (04-utm §5.2) vóór de definitieve build.
3. Nog te bouwen (niet in deze opdracht): **p2-safe**; **-nocode** voor c4-us, c4-int, k3, b2-clicked, p3-pan, p3-set, p3-next, p3-apron, p3-accessory, r2, r2-vip, n2; **v1-nocode** (HI10); fase 2: **-nohi10** voor c1, c2, c3-p, c3-s, k1, k2-new, k2-returning, b1, b2-notclicked.
4. Copy-ronde (`research/copy/04-rewrites.md`) op de 31 oorspronkelijke mails, en de 5 te lange onderwerpen/previews inkorten (sectie 5).
5. Templates in Klaviyo aanmaken, naam `v4 · <flow> · <mail>`; codemails berichtnaam beginnen met `CODE ·` (terugval cooldown, 1.4).

### 4.6 Flows (alles eerst op Draft, filters en splits per sectie 2)

| Volgorde | Flow | Live-moment | Oude flow |
| --- | --- | --- | --- |
| 1 | v4 · Checkout abandonment | Groep A, samen | Y2TmNB en Tsg2tV op Draft bij livegang (oud pad zit in de v4-flow) |
| 2 | v4 · Cart abandonment | Groep A | SwkMyn en TBWngE op Draft |
| 3 | v4 · Browse abandonment | Groep A | Wj6x6V en TyEjuQ op Draft |
| 4 | v4 · Welcome | Groep A | SiaNLu op Draft; T2SmtR blijft live met filter `v3_arm equals old` tot 20 nov, dan Draft |
| 5 | v4 · Post-purchase + v4 · Post-purchase · levering | Groep B, samen | RL3TU6 op Draft op hetzelfde moment |
| 6 | v4 · Winback | Groep B | UEfh4h op Draft |
| 7 | v4 · Sunset | Groep C | S7V4a7 op Draft (PLAYBOOK §7: niet archiveren) |
| 8 | v4 · Site abandonment | Groep C | draft UEqeEm blijft Draft |
| 9 | v4 · VIP | Groep C | |
| 10 | v4 · UGC first egg | Groep C, na Gorgias-macro | |
| 11 | v4 · Anniversary | Groep C | |

Blijven ongewijzigd live: XzHrez (review), WsQDYu (back in stock), WvRupU (mystery gift sheets), UYALJ8 (e-gift card), lead magnets TSUnLs, YyaMjx, YcXbHx, Wn2tsq, Middle East delay SxN86d, CS-notificaties TLHht3, UcGzaL, Y4a7fJ. Vixr6X gaat zoals gepland op 12 oktober uit. Niets archiveren.

### 4.7 Vóór livegang per flow

Testprofiel door elke tak (cart met pan, set, schort, plank, gift card; US en INT; nieuw en bestaand), preview met echt event voor `join`/`in`-condities (C1, C2-acc, P3-next), linkcheck incl. `/discount/`-redirect met UTM, GA4 DebugView, coupon-preview, reply-to, afzendernaam, smart sending uit.

---

## 5. Mail-inventaris

Status: **gebouwd** = HTML en preview klaar, hero lokaal in `assets/`, upload naar Klaviyo nog open. **copy-ronde** = rewrite in `research/copy/04-rewrites.md` nog niet ingebouwd. **inkorten** = onderwerp B > 50 of preview > 90 tekens. **te bouwen** = bestaat nog niet. Geen enkele mail mist een hero (tekstmails W2, S2, V2 hebben er geen nodig); AI-flitsbeelden in `content/media/ai-flash` wachten nog op akkoord en zijn geen vereiste.

| Mail | Bestand | Flow | Stap | Tak | Onderwerp A | Onderwerp B | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| c1 | checkout/c1.html | Checkout | 1 | alle | Forgetting something? | (niet gebruiken: Your pan is still here (+10% off)) | gebouwd, copy-ronde |
| c2 | checkout/c2.html | Checkout | 3K | kookgerei, nieuw | Why Siraat? (Plus 10% off your cart) | Need a second opinion on that pan? | gebouwd, copy-ronde, "independent" (3.24) |
| c2-acc | checkout/c2-acc.html | Checkout | 3A | accessoire | Yours, or a gift? Both work. | "Such lovely gifts" | gebouwd |
| c3-s | checkout/c3-s.html | Checkout | 4K | set of ≥ $300 | Your set, plus four gifts | Your set, 10% lighter | gebouwd, copy-ronde |
| c3-p | checkout/c3-p.html | Checkout | 4K | Pan Pro < $250 | One pan, or three for $349? | The math on the pan in your cart | gebouwd, copy-ronde |
| c3-acc | checkout/c3-acc.html | Checkout | 4A | accessoire, nieuw | Most kitchens start with the pan | The pan 100,000+ people cook on | gebouwd, preview 91 (inkorten) |
| c4 | checkout/c4.html | Checkout | 6 | code (T02-A), land in de template | Last chance: your own 10% ends in 48 hours | "They honored the warranty" | gebouwd 7 okt (samengevoegd uit c4-us en c4-int, urgency-upgrade), deadline-tegels |
| c4-nocode | checkout/c4-nocode.html | Checkout | 6 | T02-B / cooldown, land in de template | Your cart and $70 in gifts, one last time | | gebouwd 7 okt (samengevoegd uit c4-us-nocode en c4-int-nocode) |
| k1 | cart/k1.html | Cart | 1 | kookgerei | One pass with a damp cloth. | Your pan is still in your cart (+10% off) | gebouwd, copy-ronde |
| k1-acc | cart/k1-acc.html | Cart | 1 | accessoire | Picked it out? It's still here. | "Such beautiful quality" | gebouwd |
| k2-new | cart/k2-new.html | Cart | 2K | nieuw | The pan you keep replacing is the expensive one | What a pan really costs per year (now 10% less) | gebouwd, copy-ronde |
| k2-returning | cart/k2-returning.html | Cart | 2K | bestaande klant | Adding to your Siraat kitchen? | Your cart, 10% off, as a thank-you | gebouwd, copy-ronde |
| k3 | cart/k3.html | Cart | 3K/2A | code | 10% off your cart, for 48 hours | Covered for 75 years. Returnable for 30 days. 10% less. | gebouwd, copy-ronde, B 55 (inkorten) |
| k3-nocode | | Cart | 3K/2A | T02-B / cooldown | | | te bouwen |
| b1 | browse/b1.html | Browse | 1 | kookgerei | T05a: Lab-tested: nothing on this pan to scratch off | T05a: 100,000+ happy customers cook on this pan | gebouwd, copy-ronde, onderwerpen T05a zetten |
| b1-acc | browse/b1-acc.html | Browse | 1 | accessoire | Looked twice? Here's the detail. | What it's made of (in two lines) | gebouwd |
| b2-clicked | browse/b2-clicked.html | Browse | 2 | klikte, code | 10% off the pan you looked at (48 hours) | Still thinking it over? Here is 10%. | gebouwd, copy-ronde |
| b2-clicked-nocode | | Browse | 2 | T02-B / cooldown | | | te bouwen |
| b2-notclicked | browse/b2-notclicked.html | Browse | 2K | niet geklikt | Week one, in their words | What people wrote after the first egg (+10% off) | gebouwd, copy-ronde |
| w0 | welcome/w0.html | Welcome | 2 | al klant | Thank you. Now the first egg. | Before your pan arrives: three steps | gebouwd, copy-ronde, beeld 1,5 MB (QA A7) |
| w1-a | welcome/w1-a.html | Welcome | 3 | T04-A code-blok | Your 10% is inside (plus $70 in gifts) | Welcome. 10% on top of the sale, no catch. | gebouwd, copy-ronde |
| w1-b | welcome/w1-b.html | Welcome | 3 | T04-B gift card | Your 10% is inside (plus $70 in gifts) | Welcome. 10% on top of the sale, no catch. | gebouwd, copy-ronde |
| w2 | welcome/w2.html | Welcome | 4 | prospect | Why I started Siraat's Kitchen | The pan nobody else was making | gebouwd, copy-ronde (tekstmail) |
| w3 | welcome/w3.html | Welcome | 5 | prospect | Has your cookware actually been tested? | Three questions to ask any titanium pan brand | gebouwd, copy-ronde, hero 317 KB (QA A8) |
| w4-us | welcome/w4-us.html | Welcome | 6 | US | Start with the Pan Pro (10% off already applied) | Which pan should you start with? | gebouwd, copy-ronde |
| w4-int | welcome/w4-int.html | Welcome | 6 | INT | Start with the Pan Pro (your 10% inside) | Which pan should you start with? | gebouwd, copy-ronde |
| w5 | welcome/w5.html | Welcome | 7 | prospect | The last note about your 10% | What 100,000+ happy customers found out (and your 10%) | gebouwd, copy-ronde, B 54 (inkorten) |
| p1-first | post-purchase/p1-first.html | Post-purchase | 1 | eerste order | Good call. Here's what's coming. | The first egg will tell you | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| p1-repeat | post-purchase/p1-repeat.html | Post-purchase | 1 | herhaalklant | Good to see you again | Round two. Here's what's coming. | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| p2 | post-purchase/p2.html | Post-purchase · levering | 1 | kookgerei, geleverd | The mistake that makes titanium stick | Can you do an egg? Then anything. | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| p2-safe | post-purchase/p2-safe.html | Post-purchase | 2 | kookgerei, geen levering bekend dag 16 | When your pan arrives: the first egg | Is your pan on the stove yet? | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| p3-set | post-purchase/p3-set.html | Post-purchase | 3K | set of ≥ $300 | The pan your set is missing | What set owners add next, 10% off | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| p3-next | post-purchase/p3-next.html | Post-purchase | 3K/3A | deksel in order, of eigenaar met accessoire | How is the pan treating you? | What goes next to your pan | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| p3-pan | post-purchase/p3-pan.html | Post-purchase | 3K | pan zonder deksel | Which lid fits your pan? | Your thank-you 10% ends in 14 days | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| p3-apron | post-purchase/p3-apron.html | Post-purchase | 3A | schort, nooit kookgerei | An apron deserves a pan | Was the apron a gift? | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| p3-accessory | post-purchase/p3-accessory.html | Post-purchase | 3K/3A | pizza/roasting/pot, of accessoire | Now meet the pan | From the board to the pan | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| p3-*-nocode (5) | post-purchase/p3-*-nocode.html | Post-purchase | 3 | T02-B / cooldown | zie bron | zie bron | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| r1-pan | winback/r1-pan.html | Winback | 1 | pan of eerder kookgerei | How's your pan doing? | What pan owners add next | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| r1-set | winback/r1-set.html | Winback | 1 | set of ≥ $300 | The shapes a set leaves out | Which pan do you reach for most? | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| r1-acc | winback/r1-acc.html | Winback | 1 | nooit kookgerei | Ready for the pan? | Still cooking on a coated pan? | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| r2 | winback/r2.html | Winback | 2 | niet-VIP, code | Your 10% expires in 72 hours | Ready for pan number two? | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| r2-vip | winback/r2-vip.html | Winback | 2 | VIP, code | 15% exclusive discount, 72 hours | You came back. Here's 15%. | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| r2-nocode, r2-vip-nocode | winback/r2-nocode.html, winback/r2-vip-nocode.html | Winback | 2 | T02-B / cooldown | Ready for pan number two? / You came back. Thank you. | | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| a1 | site/a1.html | Site | 1 | | Not sure which pan? Start here. | The question we get most: which size? | gebouwd |
| a2 | site/a2.html | Site | 2 | | Where 100,000+ people started | The pan most kitchens start with | gebouwd |
| s1 | sunset/s1.html | Sunset | 1 | | Should we keep writing to you? | Still want our emails? One tap. | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| s2 | sunset/s2.html | Sunset | 2 | | Last email from me (unless you tap) | Should I stop writing? | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| s3-kept | sunset/s3-kept.html | Sunset · kept | 1 | menselijke klik op S1 of S2 (30 min) | You're staying. Thank you. | Got it, you're still on the list | v5 herbouwd 8 okt (V5-STRICT, stap 2); nieuwe flow v4 · Sunset · kept (research/v5/06-sunset-kept.md, flowsectie 6) |
| s4-kept | sunset/s4-kept.html | Sunset · kept | 2 | dag 4, 09:00, geen order | The pan we started with | December 20, 2024 | v5 herbouwd 8 okt (V5-STRICT, stap 2); geen korting |
| v1 | vip/v1.html | VIP | 1 | code | You're a VIP. Here's 15% off. | 15% off, exclusive to VIPs | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| v1-nocode | vip/v1-nocode.html | VIP | 1 | T02-B (besluit 8 okt: VIP krijgt 15% ook na een ongebruikte code; cooldown niet meer hierheen) | You're a VIP. Thank you. | For our VIPs: a note from Benjamin | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| v2 | vip/v2.html | VIP | 2 | | A question from Benjamin | What should we make next? | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| n1 | anniversary/n1.html | Anniversary | 1 | | Six months in. Anything worn off? | How's your pan at six months? | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| n2 | anniversary/n2.html | Anniversary | 2 | code | One year in. Here's 15% off. | A year on titanium. 74 to go. | v5 herbouwd 8 okt (V5-STRICT, stap 2); coupon SK_ANNIV15_7D (15%) in plaats van SK_ANNIV10_7D |
| n2-nocode | anniversary/n2-nocode.html | Anniversary | 2 | cooldown / T02-B | One year ago this week | A year on titanium. 74 to go. | v5 herbouwd 8 okt (V5-STRICT, stap 2) |
| u1 | ugc/u1.html | UGC | 1 | | Show us your first egg? | One photo, 15% off your next order | v5 herbouwd 8 okt (V5-STRICT, stap 2) |

Totaal: 47 gebouwde mails (31 v3, 7 tailoring, 9 nieuwe flows) plus s3-kept en s4-kept (v5, 8 okt: vervolgflow v4 · Sunset · kept), 14 te bouwen varianten (p2-safe, 12 `-nocode`, v1-nocode) plus 9 `-nohi10` voor fase 2. Onderwerp B wordt alleen gebruikt waar een onderwerptest loopt (W1 via T05b in fase 2, B1 via T05a); elders A.

### Bouwnotitie 2.1 (7 okt 2026, Klaviyo-flow Y6yj2z, Draft)

Gebouwd met `scripts/build_flow_checkout.py` via de Flows API. Afwijkingen van de tabel hierboven, met dezelfde uitkomst per klant:
- Klaviyo staat geen samenkomende takken toe. Categoriekeuze (C2/C2-ACC, C3-S/C3-P/C3-ACC) zit daarom als verzendfilter op de mail zelf (Checkout Started met Items/$value in de laatste 2 of 4 dagen); per profiel komt per stap hoogstens één mail door. Bestaande klanten: filter Placed Order alltime = 0 op C2 en C3-ACC.
- Land: splits (US, land gezet = INT, geen land: trigger split op Customer Locale en-US). De code-router staat daardoor vier keer; berichten met "(geen land)" in de naam.
- Update profile property weigert de API. Cooldown via terugval 1.4: codemails heten "CODE · ...", split = Received Email where Campaign Name contains "CODE ·" in de laatste 30 dagen. Alle andere flows moeten hun codemails ook zo noemen. v3_arm wordt niet gezet; T01-arm is af te lezen aan de berichtnamen (C1.. tegen Old · ..).
- Post-purchase-uitsluiting gebruikt nu RL3TU6; omzetten naar de v4 · Post-purchase-flow zodra die bestaat.

### Bouwnotitie C4 vereenvoudigd (7 okt 2026, urgency-upgrade)

C4 heeft geen landsplit meer (advies `research/build-v4/country-split-review.md`, eigenaar bevestigde: INT is duties paid, de 12-delige set is alleen US). Twee templates: `checkout/c4.html` (code, T02-A) en `checkout/c4-nocode.html` (T02-B en cooldown). De template kiest zelf: **US** als `person.Country` "United States" of "US" is, of als er geen profielland is en `event.extra.presentment_currency` USD is (of leeg); anders **INT** (INT-hero, "duties paid" in friction reducers en offer-note, `icons-int` in plaats van de set-kaart). `person.Country` is de documentatievorm van Klaviyo (help "Message personalization reference"); nog niet getest op een echt profiel: bij de eerste preview controleren met een profiel met land "US" en een met "Netherlands". Werkt het niet, dan valt elke ontvanger zonder land terug op de valuta (de oude USCOND['checkout']).
Stap 5K-6K en 5A-6A in de flow worden: dag 5 09:00, code-router (cooldown, T02) en dan c4 of c4-nocode. De oude bestanden c4-us, c4-int, c4-us-nocode, c4-int-nocode blijven staan maar zijn uit deze inventaris en uit export/QA. Flow Y6yj2z en `scripts/build_flow_checkout.py` moeten nog worden aangepast (andere agent): 3 landsplits en 6 van de 8 router-splits eruit, manifest-ID's c4 en c4-nocode.
