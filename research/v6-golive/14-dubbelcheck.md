# 14 · Dubbelcheck na de v5-livegang

# ACTIE NODIG: 7 punten

Plus 1 besluit voor Floris (punt 8) en 6 bekende open punten uit 01/02 die nog steeds open staan (sectie C).

Datum: 8 oktober 2026, 22:33 tot 23:40 UTC (livegang 22:29 UTC). Dubbelcheck-agent. Alleen gelezen: Klaviyo-API (TdtTzz, revision 2025-10-15, templates 2025-07-15) en Shopify Admin GraphQL (alleen query). Niets gewijzigd in Klaviyo of Shopify, niets gecommit. Codes in dit bestand alleen als prefix (repo is publiek).

---

## Samenvatting

| # | Ernst | Wat | Deadline |
|---|---|---|---|
| 1 | BLOKKEREND voor codemails | Coupon-vervaltijden werken niet voor de codes die nu klaarliggen: elke pool heeft 100 vooraf aangemaakte codes met vervaldatum **8 oktober 2027** (Klaviyo) en `endsAt: null` (Shopify). De mails beloven 48 uur, 72 uur, 7 of 14 dagen | vóór de eerste echte B2 (vr 10 okt 09:00 profieltijd) |
| 2 | BELANGRIJK | A/B-tests T04 (W1) en T05a (B1) zijn niet gestart: er wordt niets getest | zo snel mogelijk (UI, 2 min) |
| 3 | BELANGRIJK | FREE E-GUIDE (YyaMjx) live naast P1, dat nu zelf de e-book-download heeft: elke koper krijgt het e-book twee keer, plus banners "UP TO 56% OFF" en "45% off" | nu (UI) |
| 4 | BELANGRIJK | Pan Education YcXbHx Cutting Board-tak (live) heeft nog de banners "100-DAY TRIAL" en "UP TO 56% OFF" (overstapplan zei: eerst weghalen) | nu (UI) |
| 5 | BELANGRIJK | Browse WdRz5k sluit kopers niet uit: koper bekijkt de productpagina en krijgt "Get this pan with 10% off" (bekend uit 02 fout 5, niet opgelost) | vandaag |
| 6 | KLEIN, wel checken | Pool B2_10_48H heeft in Klaviyo 0 codes (de andere 100+); in Shopify 1 code. Nog nooit een B2-code uitgegeven | vóór vr 10 okt 09:00 |
| 7 | KLEIN | Klik-split na B1 (119850697) en B1-ACC (119850698): Bot Click staat in een aparte voorwaardegroep, niet in dezelfde voorwaarde | deze week |
| 8 | BESLUIT | T01-oud-armen (50% van checkout, cart, browse, welcome) tonen "100-DAY TRIAL", "UP TO 56% OFF", "30,000" en COOK10. Bewust zo gelaten als controlegroep, maar in strijd met DECISIONS ("nooit 100-day trial") | Floris |

Alles wat verder gevraagd is, klopt (sectie B).

---

## A. Actiepunten met bewijs en fix

### 1. Coupons: vervaltijd niet actief voor de klaarliggende codes

**Bewijs Klaviyo** (`GET /api/coupon-codes/?filter=equals(coupon.id,"<pool>")`):

| Pool | Prefix | Codes in Klaviyo | Waarvan UNASSIGNED | `expires_at` van alle codes | Verwacht |
|---|---|---|---|---|---|
| C4_10_48H | CO- | 103 | 100 | 2027-10-08T21:44 | 48 uur |
| K3_10_48H | CART- | 101 | 100 | 2027-10-08T21:48 | 48 uur |
| B2_10_48H | VIEW- | **0** | 0 | n.v.t. | 48 uur |
| P3_THANKYOU_10_14D | THX- | 101 | 100 | 2027-10-08T19:54 | 14 dagen |
| R2_10_72H | BACK- | 101 | 100 | 2027-10-08T19:51 | 72 uur |
| R2_VIP_15_72H | VIP- | 101 | 100 | 2027-10-08T20:03 | 72 uur |
| SK_REGULARS15_14D | REG- | 101 | 100 | 2027-10-08T19:58 | 14 dagen |
| SK_ANNIV15_7D | YEAR- | 101 | 100 | 2027-10-08T19:49 | 7 dagen |

De 7 Coupon Assigned-events sinds 1 september (19:56 tot 21:50 UTC vandaag) hebben allemaal `CouponExpirationDate` = toewijzing/batch + 1 jaar en gingen alle 9 toegewezen codes naar testprofielen (lolagroothuis+...). Er is dus nog geen echte klant met een code. Maar de volgende 100 klanten per pool krijgen een code uit deze batches, met 1 jaar geldigheid.

**Bewijs Shopify** (`codeDiscountNodeByCode`, 2 toegewezen en 1 niet-toegewezen code per pool): alle codes van een pool zitten in één korting "C4_10_48H (2026-10-08 11:06)", "K3_10_48H (2026-10-08 11:06)", "P3_THANKYOU_10_14D (2026-10-08 11:06)", "R2_10_72H (...11:06)", "R2_VIP_15_72H (...11:06)", "SK_REGULARS15_14D (...11:05)", "SK_ANNIV15_7D (2026-10-08 19:46)": status ACTIVE, **`endsAt: null`**, usageLimit 1, appliesOncePerCustomer true, combineert met productkortingen (goed: gifts blijven). Niets in Shopify laat een code na 48 uur vervallen.

Conclusie: "We're removing your discount in 48 hours" en "Gone in 72 hours" kloppen niet zolang deze batches worden uitgegeven. Als Floris de vervaltijd in Klaviyo heeft aangepast, geldt dat alleen voor codes die Klaviyo daarna aanmaakt; de 100 klaarliggende codes per pool zijn eerder gemaakt (laatste batch 21:48 UTC).

Wanneer het eerst echt raakt: B2 vr 10 okt 09:00 (profieltijd), K3 za 11 okt 09:00, C4 di 13 okt 09:00, P3 dag 21, R2/R2-VIP dag 75, V1 dag 30, N2 dag 365.

**Fix** (Floris, UI, plus controle door Claude):
1. Klaviyo > Content > Coupons > per pool openen > instelling **Expiration** controleren: C4, K3, B2 48 uur; R2 en R2-VIP 72 uur; P3 en SK_REGULARS15_14D 14 dagen; SK_ANNIV15_7D 7 dagen. Opslaan.
2. De klaarliggende codes ongeldig maken, zodat Klaviyo nieuwe aanmaakt met de juiste vervaltijd. Twee wegen:
   - (a) per pool in de coupon de niet-toegewezen codes verwijderen (Coupons > pool > Codes, of via API `DELETE /api/coupon-codes/{pool}-{code}` voor status UNASSIGNED, na "ga" van Floris), of
   - (b) per pool een nieuwe coupon aanmaken met de juiste vervaltijd (bijv. `C4_10_48H_V2`) en de coupon-tag in de 16 CODE-templates omzetten (`export_klaviyo.py --update` + herkoppelen). Robuuster, maar meer werk.
3. Controle: één testprofiel door een codemail sturen (preview met echte code), daarna `GET /api/coupon-codes/?filter=equals(coupon.id,"C4_10_48H")`: de nieuwe code moet `expires_at` ≈ +48 uur hebben, en in Shopify de bijbehorende korting een `endsAt` (of een eigen korting per batch met einddatum). Pas dan is de belofte in de mail waar.
4. Zolang dit niet klopt: de CODE-mails op **Manual** zetten is de veilige tussenstap (profielen wachten, niemand krijgt een valse deadline). De nocode-tak (T02-B) loopt gewoon.

### 2. A/B-tests T04 en T05a staan op draft

**Bewijs**: T4a5Mk actie 119850659 en WdRz5k actie 119850693: `status: live`, `experiment_status: draft`, `current_experiment.started: null`, allocaties 0,5/0,5, winnermetriek unique-clicks, automatische winnaar uit.

- T04 (W1): main = W1 (template YnbURS, inhoud gelijk aan variatie A SUgZZ3, 41.897 tekens: HI10 als codeblok); variatie B = Vf6FLK (gift card). Onderwerpen gelijk.
- T05a (B1): main = B1 (X6J5wt) "Get this pan with 10% off"; variatie A (Y2f9n9) zelfde onderwerp; variatie B (StGY9U) "Why I started making this pan".

**Wat er nu gebeurt**: een flow-A/B-blok waarvan de test niet gestart is, stuurt het hoofdbericht (de main action) naar iedereen; er wordt niets verdeeld en niets gemeten. Dus ja: iedereen krijgt variant A-inhoud (W1 met codeblok; B1 met "Get this pan with 10% off"). Variant B gaat naar niemand. In Received Email verschijnt dan Campaign Name "W1" / "B1" in plaats van "... Variation A/B" (te bevestigen bij de eerste echte verzending, zie sectie D).

Gevolg naast de meting: niets kapot. De B1-klik-split werkt op `$flow`, niet op de naam, dus B2-CLICKED klopt ook zonder gestarte test.

**Fix** (UI, Floris): Flows > *v4 · Welcome* > klik op de A/B-kaart W1 > **Test settings** / **Edit test**: verdeling 50/50, winnaar **handmatig**, metriek unieke kliks > **Start test** > bevestigen. Daarna hetzelfde in *v4 · Browse abandonment* op de A/B-kaart B1. Controle door Claude: `GET /api/flows/{id}/?additional-fields[flow]=definition` moet `experiment_status: live` en een `started`-tijd tonen. De API kan de test niet starten (bekend uit 01/02).

### 3. FREE E-GUIDE YyaMjx stuurt het e-book dubbel met P1

**Bewijs**: YyaMjx live, trigger Placed Order, geen filter, mail "Your E-Guide Is Ready" na 3 minuten (template S2EMYW). P1-FIRST en P1-REPEAT (X3ySuU, +1 uur) bevatten nu de e-book-download (fix 10 in 12-fixes.md). Elke koper krijgt dus twee e-bookmails binnen een uur. S2EMYW heeft bovendien nog de beeldblokken "SIRAAT PRIME TIME SALE | UP TO 56% OFF" en "45% off on our bestselling Titanium Hammered Cookware Set Pro" (alt-teksten), die volgens 11-overstapplan §3.3 weg moesten.

Het overstapplan zegt: YyaMjx uit zodra P1 de echte download heeft en de link getest is. P1 heeft de link; de handmatige test van delivery.shopifyapps.com staat in 12-fixes.md nog open.

**Fix**: Floris opent één P1-testmail (uit de testavond) en klikt "Download your e-book". Werkt de link: Flows > *FREE E - GUIDE* > statusmenu > **Draft** (niet archiveren). Werkt hij niet: YyaMjx laten lopen, maar in de mail de twee bannerblokken verwijderen en P1-link fixen.

### 4. Pan Education YcXbHx: Cutting Board-tak live met verouderde claims

**Bewijs**: YcXbHx is live; de 7 pan-mails staan op draft (klopt), de 2 Cutting Board-mails (103384104 template SNhvTL, 103384140 template U88mqB) op live. Beide templates hebben de beeldblokken "SIRAAT PRIME TIME SALE | UP TO 56% OFF" en "FREE SHIPPING | FREE SHIPPING | 100-DAY TRIAL | MADE WITH LOVE". DECISIONS 2026-10-01: nooit "100-day trial". Het overstapplan (§0 punt 6, tabel 4) zegt: Cutting Board-tak blijft "na het weghalen van twee verouderde beeldblokken".

**Fix** (UI): Flows > *EB | Pan Education* > mailkaart "FLOW: Cutting Board Education | Email 1" > Edit content > de twee beeldblokken (bovenste banner en de strook met 100-DAY TRIAL) verwijderen > Save. Zelfde in Email 2. Tot dat gebeurt: beide mails op **Manual**.

### 5. Browse stuurt kortingsmail naar verse kopers

**Bewijs**: WdRz5k profielfilter (live): Added to Cart, Checkout Started, Placed Order elk 0 *since flow start*, plus geen cart-, checkout-, welcome-mail in 7 dagen, niet in flow 7 dagen. Geen "Placed Order in de laatste N dagen" en geen uitsluiting van post-purchase (X3ySuU). Uit 02-foutenjacht fout 5: 12% van de kopers bekijkt binnen 7 dagen nog een product, ~20 mails per dag "Get this pan with 10% off" aan iemand die de pan net kocht.

**Fix** (API na "ga" van Floris, of UI): aan de flowfilter van WdRz5k toevoegen: `Placed Order` count equals 0 *in the last 30 days* en `Received Email` where `$flow` equals `X3ySuU` count equals 0 *in the last 7 days*. UI: Flows > *v4 · Browse abandonment* > Trigger > Flow filters > Add filter > "What someone has done" > Placed Order > zero times > in the last 30 days. Zelfde aan de profielfilter van de site-flow is niet nodig (VLGhbR sluit 30 dagen kopers al uit).

### 6. Pool B2_10_48H heeft nog geen codes in Klaviyo

**Bewijs**: `coupon-codes` voor B2_10_48H geeft 0 codes; alle andere pools 101 tot 103. In Shopify bestaat "B2_10_48H (2026-10-08 11:06)" met 1 code (`codesCount 1`), ACTIVE, `endsAt null`. Waarschijnlijk alleen omdat B2-CLICKED bij de testavond nooit verstuurd is (de klik-split was kapot); Klaviyo maakt een batch bij het eerste gebruik. Niet bewezen dat dat goed gaat.

**Fix**: na punt 1 een preview met echt profiel van *CODE · B2-CLICKED · pan* (WdRz5k actie 119850706): Flows > *v4 · Browse abandonment* > mailkaart > Preview > profiel `lolagroothuis+...` > controleren dat een VIEW-code verschijnt; daarna `GET /api/coupon-codes/?filter=equals(coupon.id,"B2_10_48H")` moet codes met `expires_at` ≈ +48 uur tonen.

### 7. Bot Click in een aparte voorwaardegroep

**Bewijs**: split 119850697: groep 1 `Clicked Email where $flow equals WdRz5k > 0 since flow start` EN groep 2 `Clicked Email where Bot Click equals false > 0 since flow start`. Groep 2 telt elke menselijke klik op elke mail (ook een campagne). Wie alleen een botklik op B1 had maar een echte klik op een campagne, gaat toch naar CODE · B2-CLICKED. Zelfde bouw in 119850698 (B1-ACC). Het segment YxfuJT laat zien dat twee filters in één voorwaarde wel kunnen (daar staan `$flow` en `Bot Click` samen).

**Fix** (UI): Flows > *v4 · Browse abandonment* > split na "Wait 2 days" onder B1 > voorwaarde 1 (Clicked Email, Flow = v4 · Browse abandonment) > **Add filter** > Bot Click is false > voorwaarde 2 verwijderen > Save. Idem in de split onder B1-ACC (Campaign Name contains B1-ACC). Impact is klein; geen haast.

### 8. Besluit: oude claims in de T01-controlegroep

**Bewijs**: de 17 "Old · ..."-mails in QUBUQV, TZG9Mx, WdRz5k en T4a5Mk zijn live (dat is T01, 50% van de instroom). Templates: Old · Checkout 1 t/m 5, Old · Welcome 3, 7 en 8 bevatten de banner "100-DAY TRIAL"; alle 17 "UP TO 56% OFF"; Old · Browse 1 "30,000"; Old · Cart 2 COOK10 (Shopify: ACTIVE, werkt). Was vóór de livegang ook zo (oude flows), dus geen nieuwe schade, maar DECISIONS zegt "nooit 100-day trial" en het retourbeleid is 30 dagen.

**Keuze voor Floris**: (a) zo laten tot de T01-uitslag (zuivere controlegroep), of (b) in de 8 betrokken oude templates alleen de banner met 100-DAY TRIAL weghalen (verandert de controle nauwelijks). Advies: (b).

---

## B. Gecontroleerd en in orde

### B1. Status (GET /api/flows, 97 flows, 25 live)

| Groep | Verwacht | Gevonden |
|---|---|---|
| 13 v5-flows | live, alle mails live | live; alle send-email-acties live: X3ySuU 24, VQ93sx 1, QUBUQV 14, TZG9Mx 13, T4a5Mk 15 + A/B (main + 2 variaties live), WdRz5k 9 + A/B, VTkxFL 4, UyFc78 10, XbYT7T 3, VLGhbR 2, TbYQmX 2, Wzz6xC 2, VPixnJ 1. Geen enkele draft- of manual-mail |
| 12 oude flows uit | draft | Y2TmNB, Tsg2tV, SwkMyn, TBWngE, Wj6x6V, TyEjuQ, SiaNLu, RL3TU6, TSUnLs, SxN86d, WvRupU, S7V4a7: alle draft |
| TEST v5 (op naam gezocht, ook kleine letters) | draft | 14 gevonden, alle draft: Vjgd99, Udi8vX, SzTvEP, TqMjb7, TdvNjN, Rbc9M9, VJTeSu, RGSbY3, VHtuLj, WNQjm9, X5jkrF, QP8Sfr, WzxNmj, SrAYTK. Geen andere flow met "test" in de naam |
| YcXbHx | alleen Cutting Board live | flow live; 7 pan-mails draft, 2 Cutting Board-mails live (zie punt 4) |
| Blijven live | YyaMjx, UEfh4h, T2SmtR, XzHrez, WsQDYu, UYALJ8, TLHht3, UcGzaL, Y4a7fJ, Wn2tsq, Vixr6X | alle 11 live |
| Andere live flows | geen | geen: 13 + 11 + YcXbHx = 25 live, precies de verwachte set |

### B2. Overlap met v5 (wie krijgt dubbel)

| Live oude flow | Overlap met v5 | Oordeel |
|---|---|---|
| YyaMjx FREE E-GUIDE | e-book dubbel met P1 | **punt 3** |
| YcXbHx Cutting Board | geen inhoudelijke overlap (P1/P3 gaan over pannen) | claims: **punt 4** |
| UEfh4h oude winback | trigger Placed Order, net als UyFc78. Filters op alle 4 mails: Placed Order = 0 *after 2026-10-09T00:00Z* en Received Email `$flow = UyFc78` = 0 alltime. Orders tussen 22:29 en 00:00 UTC (1,5 uur, ~15 orders) komen in beide; hun eerste oude mail is dag 60, de nieuwe R1 dag 45, dus de tweede filter houdt ze tegen zodra R1 is verstuurd. Alleen wie R1 overslaat (alle R1-filters onwaar) kan op dag 60 de oude reeks krijgen. Code GOODFOOD: Shopify ACTIVE (34 keer gebruikt) | aanvaardbaar |
| T2SmtR Failure to launch | split 90675572 nu: Placed Order 0 in 30 d **en** Received Email Campaign Name = "W2" 0 keer in 60 d. v5-arm (krijgt W2) krijgt geen FTL; oude arm wel | klopt. Randgeval: wie W2 overslaat (checkout- of cartmail in de laatste dag) krijgt later toch FTL |
| XzHrez review (Delivered +14 d) | naast P2 (+1 d) en U1 (+4 d) op hetzelfde Delivered Shipment | zo ontworpen |
| Vixr6X Trustpilot | XzHrez sluit 30 dagen Trustpilot-ontvangers uit | goed; gaat 12 okt uit |
| UYALJ8 E-Gift Card | koper krijgt ook P1 | klein, bekend |
| WsQDYu, TLHht3, UcGzaL, Y4a7fJ, Wn2tsq | geen | goed |

### B3. Definities per v5-flow (live)

Overal: smart sending **uit** in alle v5-mails (zo ontworpen), afzender send@ / reply-to support@, geen TEST-filter: de definities van alle 13 flows bevatten nergens `siraat_test`, `lolagroothuis`, `floris` of een gmail-adres. De enige "test" is de welcome-filter `email not-contains test@` (bestond al, 02 fout 19).

| Flow | Trigger + filters | Splits en wachttijden | Oordeel |
|---|---|---|---|
| X3ySuU Post-purchase | Placed Order; niet in flow 30 d | +1 u P1-FIRST (1 order) / P1-REPEAT (>1) · 16 d tot 09:00 P2-SAFE (pan/set in 17 d, geen levering, geen refund) · 4 d tot 09:00 · 2e order = einde · cooldown (CODE · in 30 d) · T02 50% · 7 P3-typen × 3 (code, nocode-T02-B, nocode-cooldown) | klopt |
| VQ93sx Levering | Delivered Shipment; pan/set-order in 30 d, niet in flow 30 d, geen P2-SAFE in 30 d | 1 d tot 09:00 P2 (geen refund) | klopt |
| QUBUQV Checkout | Checkout Started `$value > 0`; Placed Order 0 sinds start, niet in flow 14 d, geen X3ySuU-mail 7 d | T01 50% · v5: 30 min C1 · 1 d C2/C2-ACC · 2 d 09:00 C3-S/C3-P/C3-ACC · 2 d 09:00 cooldown · T02 50% CODE · C4 / nocode · oud: Old · Checkout 1 t/m 5 | klopt (C3-gat, zie C) |
| TZG9Mx Cart | Added to Cart, Price > 0, geen gifts; Checkout Started en Placed Order 0 sinds start, geen QUBUQV-mail 7 d, niet in flow 14 d | T01 50% · kookgerei: 30 min K1 · 1 d K2-RETURNING/K2-NEW · 2 d 09:00 cooldown · T02 CODE · K3 · pan; anders K1-ACC · 3 d 09:00 K3-acc-router · oud: Old · Cart 1 t/m 3 | klopt |
| T4a5Mk Welcome | lijst Uw8eZG; niet `test@`, nooit eerder in flow | T01 50% · 20 min · besteld sinds start = einde · ooit besteld W0 / anders W1 (A/B) · 1 d 09:00 W2 · 2 d W3 · 3 d landsplit W4-US/W4-INT · 4 d W5 · oud: Old · Welcome 1 t/m 8 | klopt, A/B zie punt 2 |
| WdRz5k Browse | Viewed Product; zie punt 5 | T01 50% · 1 u kookwoord-split · B1 (A/B) / B1-ACC · 2 d 09:00 klik-split (`$flow = WdRz5k` + Bot Click) · cooldown · T02 · oud: Old · Browse 1 | klik-split werkt nu; zie punt 5, 7 |
| VTkxFL VIP | Placed Order; precies 2 orders, nooit eerder | 30 d 09:00 · split (CODE in 30 d EN order met code in 45 d) → V1 nocode / CODE · V1 · 10 d V2 | klopt (geen T02, zo ontworpen) |
| UyFc78 Winback | Placed Order; geen flowfilter | 45 d 09:00 R1-SET/PAN·kook/PAN·eigenaar/ACC · 30 d 09:00 ≥2 orders → R2-VIP-router, anders R2-router, beide cooldown + T02 | klopt (geen refundfilter, zie C) |
| XbYT7T Anniversary | Placed Order; 1 order, kookgerei, nooit eerder | 182 d N1 · 183 d cooldown → N2 nocode / CODE · N2 | klopt |
| VLGhbR Site | Active on Site; niets gedaan sinds start, geen order 30 d, geen browse/cart/checkout/post-purchase-mail 7 d, welcome 10 d, niet in flow 14 d | 2 u A1 · 2 d 09:00 A2 | klopt |
| TbYQmX Sunset | segment WuHSm6; niet in flow 180 d, geen welcome- of post-purchase-mail 30 d | 1 d 09:00 S1 (geen filter) · 4 d 09:00 S2 (geen menselijke klik, bezoek, order sinds start) | klopt (S1-filter, zie C) |
| Wzz6xC Sunset kept | segment YxfuJT; niet in flow 365 d | 30 min S3 · 4 d 09:00 S4 | klopt |
| VPixnJ UGC | Delivered Shipment; 1 order, kookgerei, nooit eerder, nooit 12-delige set | 4 d 09:00 U1 (geen ticket, geen refund 30 d, Fulfilled Order 60 d) | klopt |

Alle `profile-sample`-splits staan op 50%: T01 in QUBUQV, TZG9Mx, T4a5Mk, WdRz5k; T02 in X3ySuU, QUBUQV, TZG9Mx (2), WdRz5k (2), UyFc78 (2). `$flow`-verwijzingen wijzen naar bestaande v5-ID's.

### B4. Templates (alle 89 v5-berichten, 106 templates incl. A/B en oude armen)

Per v5-bericht de HTML van de gekoppelde template opgehaald (`GET /api/templates/{id}`):
- 89/89 bevatten `light only`, `/pages/about-us`, `#BDB8B0`;
- 0 met `%%` buiten Klaviyo-tags;
- 46 keer `siraat_` (owned, cats, orders), 46 keer met `|default`;
- 0 met open bouwmacro's (`{{IF:`, `{{PRICE`, `{{SIZE`, `{{SHIP}}`, `{{GIFTS`, `{{IMG}}`), VRAAG, TODO, `/pages/faq`, `/products/e`, "100-DAY", "30,000", "lifetime warranty" of een lang streepje;
- elke CODE-template gebruikt precies één pool (C4, K3, B2, P3, R2, R2-VIP, SK_REGULARS15_14D, SK_ANNIV15_7D), geen kruisgebruik.

Onderwerpen en previews van de 89 v5-berichten: geen `{`, `}`, `[`, `]`, placeholder of lang streepje. Alleen de oude armen hebben `{{ first_name }}` in het onderwerp (zo bedoeld). K3-onderwerp: "We're removing your discount" (fix 18 staat live).

### B5. Segmenten

| Segment | Leden | Definitie | Oordeel |
|---|---|---|---|
| WuHSm6 v4 · Sunset · unengaged 120d | 75.415 | e-mailconsent · Received Email > 7 in 120 d · Active on Site 0 in 120 d · Placed Order 0 in 180 d · Clicked Email (Bot Click false) 0 in 120 d · **created at least 120 days ago** | created-regel staat. Echte opens tellen niet mee (02 fout 3) en de 75.415 huidige leden komen nooit in TbYQmX (segmenttrigger, 01 bevinding 7): zie C |
| YxfuJT v4 · Sunset · kept (klik 7d) | 0 | Clicked Email met `$flow = TbYQmX` en Bot Click false (beide in één voorwaarde) in 7 d | klopt; 0 is verwacht |
| XdK77b v4 · Welcome protection | 7.243 | in lijst Uw8eZG toegevoegd in 14 d en Placed Order 0 in 14 d | klopt; alleen voor campagnes (Homestead moet hem uitsluiten) |
| XY4NVp oude Sunset Segment | 17.384 | | trigger van S7V4a7 (draft), geen risico |

### B6. Overige codes (Shopify, alleen lezen)

HI10: ACTIVE, appliesOncePerCustomer true. GOODFOOD (oude winback) en COOK10 (Old · Cart 2): ACTIVE, dus de oude armen sturen geen dode code.

---

## C. Bekende open punten uit 01/02 die nog steeds open staan (live gecontroleerd)

| Uit | Punt | Nu live | Advies |
|---|---|---|---|
| 01 #6 / 02 #6 | 14% van de checkouts krijgt geen C3 (Deep, Wok, Crêpe, Roasting, Pizza, Pan Pro ≥ $300 zonder set) | C3-P nog `$value < 300` en PANPRO-lijst | C3-P verruimen (02 fout 6) |
| 02 #9 | W1 en C1 binnen 10 minuten bij inschrijving in de checkout | welcome-filters kijken alleen naar ontvangen checkoutmail in 1 d | Checkout Started 0 in 1 d aan W1 toevoegen |
| 02 #12 | S1 zonder verzendfilter | 119850754 `additional_filters: null` | S2-filters ook op S1 |
| 02 #15 | Winback zonder refundfilter | UyFc78 geen Refunded Order-filter | Refunded Order 0 sinds start op elke R-mail |
| 01 #7 / 02 #4 | Sunset-backlog: 75.415 huidige leden komen nooit in TbYQmX; geen "suppressed"-segment | ongewijzigd | bewust kiezen: porties toevoegen of alleen nieuwe instroom; suppressed-segment vóór de eerste S2 (dag 5) |
| 02 #3 | WuHSm6 telt echte opens niet mee (~10% lezers krijgt "last email") | geen Opened Email-voorwaarde | groep `Opened Email machine_open = false` 0 keer in 90 d toevoegen |

---

## D. Eerste echte activiteit sinds 22:29 UTC

Gemeten van 22:37 tot 23:31 UTC, elke 5 minuten (`GET /api/events`, metrics Received Email YkRM4Q, Dropped Email RCULWK, Skipped Send X3wTrc, Bounced Email XDdu6P, Marked Email as Spam VQMAAk, Unsubscribed from Email Marketing YcWddQ, Coupon Assigned XUMYt7, Opened en Clicked Email).

**Belangrijk om te weten: Received Email loopt in de API meer dan een uur achter.** Om 23:31 UTC was de nieuwste Received Email nog van 22:29:22. Opens, kliks, orders, SMS en afmeldingen komen wel direct binnen. Dat het versturen werkt, blijkt uit opens en een afmelding op mails die ná 22:29 uit de nieuwe flows zijn verstuurd:

| Signaal na 22:29 | Flow | Bericht | Aantal |
|---|---|---|---|
| Opened Email | T4a5Mk (T01-oud-arm) | Old · Welcome 1 | 1 |
| Opened Email | WdRz5k (T01-oud-arm) | Old · Browse 1 | 2 |
| Afmelding (one-click) 23:00 | T4a5Mk | Old · Welcome 1 (message WCZQNi) | 1 |

De v5-armen (W1 na 20 min, C1/K1 na 30 min, B1/P1 na 1 uur) hadden om 23:31 nog geen open of klik in de API; dat past bij de wachttijden en de kleine aantallen in het eerste uur. Niet als fout te tellen.

| Metric sinds 22:29 | Aantal | Toelichting |
|---|---|---|
| Received Email | 2 | beide 22:29: YyaMjx (E-Guide) en Wj6x6V "Copy of Email #1" om 22:29:22, 3 seconden nadat Wj6x6V op Draft ging (22:29:19): mail die al in de wachtrij stond. Geen andere verzending uit een uitgezette flow gezien |
| Bounced Email | 1 | 22:29:00, Y2TmNB (oud, vóór het uitzetten), hard bounce |
| Dropped Email / Skipped Send | 0 / 0 | geen renderfouten of overgeslagen sends gemeld |
| Marked as Spam | 0 | |
| Unsubscribed | 8 | 1 uit v5-flow T4a5Mk (oude arm, zie boven); de rest uit campagnes (HS // Engaged 180 Days) en oude flowmails van vóór 22:29 |
| Coupon Assigned | 0 | nog geen echte code uitgegeven (zie punt 1) |
| Placed Order | 3 (22:30, 22:38, 22:55) | kopers zijn ingeschreven; hun P1 valt na 23:30 |

**Oud en nieuw tegelijk**: in dit eerste uur niet waargenomen (behalve de ene Wj6x6V-mail uit de wachtrij). Wat structureel dubbel kan, staat in B2 (YyaMjx e-book, punt 3).

**A/B zonder gestarte test**: bij de eerste W1- en B1-verzendingen in Received Email controleren dat Campaign Name "W1" / "B1" is (hoofdbericht, iedereen dezelfde variant). Lukt pas als de Received-achterstand weg is.

**Vervolg**: deze sectie opnieuw draaien bij de 24-uurscontrole (03-draaiboek 6.2), via het 12-uursrapport (routine trig_017iU43jScAopEQivhUtENwr, 07:52 Amsterdam). Pas dan zijn T01-verdeling, bounces per v5-mail en dubbele ontvangers echt te meten.
