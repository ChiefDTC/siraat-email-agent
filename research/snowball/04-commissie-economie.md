# Social Snowball · commissie-economie (21 okt 2026)

Vraag Floris: affiliatecommissie 20%, vriendenkorting 10% via de affiliatelink of -code, uitbetaling in cash via Tremendous. Dit stuk rekent uit wat een doorverwezen order oplevert, waar het verlies begint, wat vergelijkbare merken betalen, hoe groot het risico op niet-incrementele omzet is en welke structuur we adviseren.

Alles is alleen gelezen (Shopify ShopifyQL en GraphQL, Triple Whale summary). Niets aangepast. Alleen totalen, geen klantgegevens. Model: `python` in de scratchpad, cijfers hieronder overgenomen.

## 1. Kort advies

- **Basis: 15% commissie op netto omzet** (na alle kortingen, zonder verzending en btw), **vriend 10%** alleen op een eerste order, **plafond $50 commissie per order**, **niet combineerbaar** met HI10, flowcodes of andere codes.
- **Creator-tier 20%** alleen voor goedgekeurde creators met eigen publiek (link, geen openbare code), na een proefmaand met bewezen nieuwe klanten. Niet als standaard voor iedereen.
- **BFCM (1 nov t/m 2 dec):** commissie 10%, vriendenkorting blijft 10% maar stapelt nergens mee.
- **Uitbetaling:** pas na 45 dagen (30 dagen retour vanaf levering plus levertijd), minimum $50, standaard via Tremendous gift card of Visa virtual card (0% fee), Tremendous-saldo aanvullen per bankoverschrijving, nooit met een creditcard. Optie: **25% in store credit** in plaats van 15% cash (kost Siraat ca. 8% van de omzet).
- **Kosten per doorverwezen order** (gemiddelde order $250 vóór codes): ca. **$64** (vriendenkorting $25, commissie $32, platform $6,40, fee $0 tot $1,30). **Bijdrage na kosten: ca. $88** (tegen $76,80 bij 20%/10%). Breakeven-orderwaarde: $119 (bij 20%/10%: $127).
- **Is 20%/10% verstandig?** Bij de prijzen zoals ze nu echt zijn verliest Siraat er geen geld op per order (bijdrage $77), en het is goedkoper dan betaalde ads (nieuwe-klant-CPA $163). Maar 20% ligt twee tot zes keer boven wat kookgerei-merken betalen (3 tot 10%), het programma moet dan minstens 40% echt nieuwe klanten opleveren om beter te zijn dan geen programma, en bij echte prijsverlaging of stapeling gaat het snel onder nul. Daarom: 15% als basis, 20% als verdiende tier.

## 2. Marge: wat een order nu kost

### 2.1 Bronnen en cijfers (laatste 30 dagen, totalen)

| Post | Waarde | Per order | Bron |
| --- | --- | --- | --- |
| Orders | 5.916 (Shopify) / 5.689 (TW) | ca. 197 per dag | ShopifyQL `sales`, TW summary 21 sep t/m 20 okt |
| Bruto verkoop (na sale-prijs, vóór codes) | $1.478.190 | $249,90 | ShopifyQL |
| Kortingen (codes, HI10, flowcodes) | $91.572 | $15,50 (6,2% van bruto) | ShopifyQL |
| Retouren (sales reversals) | $70.781 | 4,8% van bruto (TW: 4,96%) | ShopifyQL, TW |
| AOV (Shopify) | $229,51 | | ShopifyQL |
| COGS orders | $252.139 | $44,30 (17,7% van bruto) | TW (Shopify unitCost) |
| Verzending en fulfilment | $207.377 | $36,50 | TW (ingestelde verzendkosten) |
| Betaalkosten | $34.178 | $6,00 (2,65%) | TW |
| Brutowinst na COGS, verzending, betaling | $792.966 | $139,40 | TW |
| Advertentiekosten | $781.913 | $137,40 | TW |
| Nieuwe-klant-CPA | | $162,60 | TW |
| Netto winst (marge) | $57.841 | 4,0% | TW |
| Aandeel nieuwe klanten in orders | 84,5% | | TW |

Kostprijzen (Shopify `inventoryItem.unitCost`, voorbeelden): Pan Pro Standard $12,50 (prijs $144), Pan Pro Large $13,50 ($149), Pan Pro Mini $10 ($129), Crêpe Pan $14,24 ($139), 6-delige set $57,90 ($299), 12-delige set $186 ($599), deksel $5,55 tot $6,53 ($59), snijplank $13,84 tot $25,34 ($69 tot $99), utensil set $38 ($149).

Kanttekeningen:
- Kostprijzen staan in Shopify, maar het is niet zeker dat invoerrechten ("duties paid" in alle markten) en inbound vracht erin zitten. Als dat niet zo is, ligt de echte COGS hoger. Even nagaan bij Floris.
- Verzendkosten komen uit Triple Whale ($36,50 per order gemiddeld). Per product is dat niet zichtbaar; in 2.4 staan aannames per product (pan $20, 6-delig $35, 12-delig $60), duidelijk als aanname.
- Retourverzending is gratis (Gorgias-guidance, zie `content/facts/summary.md`); aanname $15 per retour.

### 2.2 De sale verlaagt de echte prijs nauwelijks

Belangrijkste vondst. "50% off" en "70% off" zijn percentages ten opzichte van de compare-at prijs, niet ten opzichte van wat klanten normaal betalen. De verkoopprijs ligt nu al op ongeveer 30% van compare-at (Pan Pro Standard $144 tegen $480, 6-delig $299 tegen $997, 12-delig $599 tegen $1.997).

Wat klanten echt betaalden (ShopifyQL):

| Periode | AOV | Codekorting in % van bruto | Pan Pro Standard, bruto per stuk |
| --- | --- | --- | --- |
| Week van 24 nov 2025 (BFCM) | $240,53 | 7,8% | |
| November 2025 | $243,46 | 7,2% | $163,70 |
| Augustus 2026 | $217,78 | 13,3% | $153,10 |
| September 2026 | $222,08 | 13,2% | $150,30 |
| Oktober 2026 (t/m 20e) | $226,89 | 5,3% | $145,20 |

Gevolg: in de praktijk is er geen "normale prijs" die tijdens de sale halveert. Het echte margerisico zit in **codes die bovenop de sale-prijs komen** (HI10, flowcodes, straks de vriendencode) en in een eventuele **echte** prijsverlaging. Floris vroeg ook om de letterlijke varianten; die staan in 2.3 als stresstest.

### 2.3 Bijdrage per doorverwezen order

Model per order: omzet na vriendenkorting, min 5% retouren (product komt terug, verzending niet), min COGS, verzending ($36,50 + $0,75 retour), betaalkosten 3%, commissie (alleen op niet-geretourneerde orders, dankzij de wachttijd), Tremendous-fee en Social Snowball platformfee 3% van affiliate-omzet (Snow Day-plan; bij Blizzard $499 p/m vast valt die weg). Bedragen in USD.

Ter vergelijking, zonder programma: gewone order $250 zonder code levert **$150,70**, met HI10 **$127,70**.

**A. Realiteit: orderwaarde $250 vóór codes (sale-banner verandert de prijs niet), Tremendous 4%**

| Vriendenkorting \ commissie op netto | 0% | 10% | 15% | 20% | 25% |
| --- | --- | --- | --- | --- | --- |
| 0% | 143,5 | 118,8 | 106,5 | 94,1 | 81,8 |
| 10% | 121,3 | 99,0 | 87,9 | **76,8** | 65,7 |
| 15% | 110,1 | 89,1 | 78,6 | 68,1 | 57,6 |

- 20% commissie op **bruto** (vóór vriendenkorting) in plaats van netto: $71,90 (ruim $5 duurder per order).
- Vast bedrag per order, met 10% vriendenkorting: $25 → $96,60, $35 → $86,70, $45 → $76,80. Zonder vriendenkorting: $118,80 / $109 / $99,10.
- Stapeling HI10 + vriendencode (20% korting) met 20% commissie: $59,40.

**B. Stresstest: de sale verlaagt de echte orderwaarde letterlijk met 50% ($125)**

| Vriendenkorting \ commissie | 0% | 10% | 15% | 20% | 25% |
| --- | --- | --- | --- | --- | --- |
| 0% | 32,1 | 19,8 | 13,6 | 7,4 | 1,2 |
| 10% | 21,0 | 9,8 | 4,3 | **-1,3** | -6,8 |
| 15% | 15,4 | 4,9 | -0,4 | -5,6 | -10,9 |

Vast bedrag: $25 + 10% vriend -$3,70, $35 -$13,60, $45 -$23,50.

**C. Stresstest: letterlijk 70% off ($75)**

| Vriendenkorting \ commissie | 0% | 10% | 15% | 20% | 25% |
| --- | --- | --- | --- | --- | --- |
| 0% | -12,5 | -19,9 | -23,6 | -27,3 | -31,0 |
| 10% | -19,2 | -25,8 | -29,2 | **-32,5** | -35,8 |
| 15% | -22,5 | -28,8 | -31,9 | -35,1 | -38,2 |

Bij een echte 70%-korting verliest elke order al geld zonder programma, omdat COGS plus verzending ($81) hoger is dan de omzet. Dit laat zien waarom een vast bedrag per order of commissie op bruto gevaarlijk is zodra de echte prijs daalt.

**Tremendous-fee (20%/10%, order $250, commissie $42,75):**

| Uitbetaling | Fee | Bijdrage |
| --- | --- | --- |
| Gift card, Visa virtual card, goed doel | 0% ($0) | $78,50 |
| Gift card, saldo met creditcard aangevuld | 3% ($1,28) | $77,20 |
| Bank, PayPal, Venmo | 4% ($1,71) | $76,80 |
| PayPal en saldo via creditcard | 7% ($2,99) | $75,50 |

De fee is klein naast de commissie zelf. Het platform (3% van affiliate-omzet, $6,40 per order) weegt zwaarder; vanaf ongeveer $16.600 affiliate-omzet per maand is Blizzard ($499 vast) goedkoper dan Snow Day (3%). Prijzen van Social Snowball verschillen per bron (zie sectie 6), dus offerte opvragen.

**Breakeven-orderwaarde** (vóór codes, bijdrage = 0): zonder programma $86, met 15%/10% $119, met 20%/10% $127.

### 2.4 Per product (eigen kostprijs, verzendkosten als aanname)

| Product (prijs) | Geen programma | 20%/10% (commissie) | 15%/10%, plafond $50 (commissie) | Letterlijk 70% off + 10% + 20% |
| --- | --- | --- | --- | --- |
| Pan Pro Standard ($144) | $95,80 | $57,30 ($24,60) | $63,70 ($18,50) | -$5,60 |
| 6-delige set ($299) | $175,80 | $96,00 ($51,10) | $109,30 ($38,30) | -$34,70 |
| 12-delige set ($599) | $296,60 | $136,60 ($102,40) | $193,80 ($47,50) | -$125,20 |

Het plafond raakt alleen de grote sets, daar scheelt het $57 per order zonder dat de affiliate op een pan iets merkt.

### 2.5 Combinaties die geld verliezen

- Elke combinatie bij een **echte** prijsverlaging van 70% (al verlies zonder programma).
- Bij een echte 50%-verlaging: 20% + 10% vriend, 15% + 15% vriend, 25% met elke vriendenkorting, en elk vast bedrag vanaf $25 met vriendenkorting.
- Orders onder ca. $119 tot $127 netto met 15 tot 20% commissie en 10% vriendenkorting (een losse Mini-pan of snijplank met een extra code komt daar dichtbij).
- Niet in verlies, wel dun: stapeling van HI10 of een flowcode met de vriendencode (bijdrage $59 bij 20%).
- Economisch verlies (zie 4): elke order die ook zonder affiliate was gekomen. Dan betaal je $39 tot $51 extra voor niets.

## 3. Benchmarks

Bijna niemand publiceert zijn eigen voorwaarden; de cijfers komen uit affiliate-directories en kunnen oud zijn. Onderscheid: **affiliate/creator** (publishers, creators, couponsites, betaald per verkoop) tegenover **klantreferral** (bestaande klant geeft een vriend korting, krijgt zelf korting of product).

| Merk | Type | Commissie | Vriend / klantvoordeel | Bron |
| --- | --- | --- | --- | --- |
| HexClad US | Affiliate | 5 tot 10% (oudere Admitad-listing tot 23,75%, gesloten) | | [Shopper.com](https://www.shopper.com/partnerships/hexclad-com-affiliate-program), [The Affiliate Monkey](https://theaffiliatemonkey.com/affiliate/hexclad-cookware-us-affiliate-program/) |
| HexClad CA | Affiliate | tot 15%, cookie 14 dagen, uitbetaling vanaf $10 | | [Lasso](https://getlasso.co/affiliate/hexclad-ca/) |
| HexClad UK (Awin) | Affiliate | niet-geautoriseerde codes: 0% commissie | | [Awin](https://ui.awin.com/merchant-profile-terms/44987) |
| HexClad | Klantreferral | Verwijzer krijgt producten (oplopend per verwijzing, eerste ca. $129) | Vriend ca. $100 off eerste order; eigen link niet bruikbaar | [Coupons.com](https://www.coupons.com/coupon-codes/hexclad), [GrabOn](https://grabon.com/hexclad-coupons/) (derden) |
| Caraway | Affiliate | 3,2 tot 6,4%, alleen eerste aankoop, cookie 14 dagen | | [RevShare](https://www.revshare.so/programs/advertiser/caraway), [AffiliList](https://www.affililist.com/affiliate/caraway) |
| Made In | Affiliate (Impact) | 8 tot 10% | | [LinkClicky](https://linkclicky.com/affiliate-program/made-in-cookware/) |
| Our Place | Affiliate (Impact) | 10%, cookie 14 dagen | | [LinkClicky](https://linkclicky.com/affiliate-program/our-place/), [affi.io](https://affi.io/m/our-place) |
| Great Jones | | Geen openbaar programma gevonden | | zoekresultaten zonder programma |
| Condition 1 (outdoor, op Social Snowball) | Affiliate | 10% (AvantLink 8%) | | [Condition 1](https://condition1.com/pages/affiliate-program) |
| DTC algemeen | Affiliate | mediaan ca. 8,4%, DTC start vaak 10 tot 15%; home 8 tot 15% | | [ReferralCandy](https://www.referralcandy.com/blog/affiliate-commission-rates), [Post Affiliate Pro](https://www.postaffiliatepro.com/faq/typical-affiliate-commission-rates/) |

Conclusie: kookgerei betaalt affiliates 3 tot 10%, DTC in het algemeen 10 tot 15%. 20% is hoog, maar Siraat heeft een hogere productmarge (COGS 18% van bruto) dan HexClad of Caraway waarschijnlijk hebben, en een hoge CPA ($163). Een klantreferral in deze categorie draait vaker om een vast bedrag of product (HexClad, eigen ontwerp in `research/referral/01-ontwerp.md`: give $25, get $25) dan om een percentage.

## 4. Incrementaliteit: betalen voor orders die toch kwamen

Risico's, van groot naar klein:

1. **Couponsites en browserextensies** (Honey, RetailMeNot, Capital One Shopping) vangen een openbare affiliatecode op en plakken die in de checkout van klanten die al wilden kopen. Bureaus schatten dat 66 tot 71% van coupon- en cashbackconversies niet incrementeel is (niet tot een primaire studie terug te voeren, richtinggevend) ([Hamster Garage](https://www.hamstergarage.com/article/affiliate-incrementality-ecommerce-measurement-guide), [Haus case study](https://www.haus.io/case-study/affiliate-on-off-test-reveals-the-incrementality-of-loyalty-sites-for-global-dtc-brand)). Bij Siraat extra risico: 84,5% van de orders is nieuw en de sale is luid, dus mensen zoeken actief naar "Siraat code".
2. **Bestaande klanten en lijstleden** die HI10 of een flowcode al hebben en de vriendencode gebruiken omdat die even groot is.
3. **Zelfverwijzing**: affiliate koopt via de eigen link, of laat een huisgenoot dat doen.
4. **Creators die alleen de laatste klik pakken**: klant zag een Meta-advertentie, googlet daarna een code.

Rekensom (20%/10%, order $250): een echt nieuwe order levert $76,80; een order die toch was gekomen (met HI10) kost $50,90 extra. Breakeven: **40% van de doorverwezen orders moet echt incrementeel zijn**. Bij 15%/10% met plafond is dat **31%**, bij 10%/10% 22%. Kosten per incrementele order (commissie, fee, platform): 20%/10% $102 bij 50% incrementeel, $170 bij 30%; 15%/10% $80 respectievelijk $133. Ter vergelijking: nieuwe-klant-CPA via ads $163.

Instellingen in Social Snowball om dit te beperken (functies volgens de helpcentrum-artikeltitels; de pagina's zelf waren vanuit deze sessie niet bereikbaar, dus bij inrichten nalopen):

| Instelling | Advies | Waarom |
| --- | --- | --- |
| Alleen nieuwe klanten ("restrict affiliate purchases to new customers only") | Aan, voor de vriendenkorting én de commissie | Bestaande klanten niet belonen; HI10 staat al op een keer per klant |
| Zelfverwijzing blokkeren ("block commissions on self-referrals", tagging self-referral orders) | Aan; plus eigen controle op zelfde adres | Geen commissie op eigen of huisgenoot-orders |
| Link of code | Klantreferral en creators: unieke link met automatisch toegepaste korting. Openbare code alleen voor goedgekeurde creators, en met naam (niet "SIRAAT10") | Codes lekken naar couponsites; een link moet echt geklikt worden |
| Couponsites | In de voorwaarden: geen plaatsing op coupon- of cashbacksites, geen bieden op merknaam in Google; overtreding = 0% commissie (zoals HexClad UK op Awin) | Grootste bron van niet-incrementele orders |
| Combineerbaarheid in Shopify | Vriendencode combineert met niets (geen order-, product- of verzendcode) | Geen stapeling met HI10 of flowcodes |
| Attributie- of cookievenster | 14 dagen (Caraway, Our Place, HexClad CA gebruiken 14) | Langer geeft meer toevalstreffers; Siraat koopt snel |
| Wachttijd ("custom delay commission filters", maturation period) | 45 dagen na order | 30 dagen retour vanaf levering, mediane levering ca. 12 dagen, 12-delige set in twee delen |
| Minimum uitbetaling | $50 | Minder losse kleine betalingen, minder fees en fraude met een enkele order |
| Omzetbasis ("including/excluding tax and shipping in revenue calculations") | Exclusief verzending en btw, na kortingen | Commissie alleen op wat Siraat echt ontvangt |
| Plafond | $50 per order, en review bij meer dan 10 orders per affiliate per maand | Grote sets en uitschieters |
| Meten | Holdout: een maand lang voor de helft van de nieuwe affiliates de code niet openbaar, alleen link; daarnaast aandeel "nieuwe klant, eerste sessie via affiliatelink" volgen in Triple Whale | Incrementaliteit zichtbaar maken voordat we naar 20% gaan |

## 5. Advies

| Onderdeel | Keuze |
| --- | --- |
| Commissie basis | 15% op netto omzet (na alle kortingen, zonder verzending en btw) |
| Creator-tier | 20% voor goedgekeurde creators na een proefmaand met minimaal 10 nieuwe klanten en minder dan 10% retouren, alleen via link |
| Vriendenkorting | 10%, alleen eerste order, vervangt HI10, niet combineerbaar |
| Plafond | $50 commissie per order |
| BFCM (1 nov t/m 2 dec) | Commissie 10% (tier 15%); de sale is dan zelf de reden om te kopen en het lekrisico is het grootst |
| Wachttijd | 45 dagen na order, alleen niet-geretourneerde orders |
| Uitbetaling | Tremendous, standaard gift card of Visa virtual card (0%); bank of PayPal mag, 4% voor Siraat (of laten dragen door de affiliate); saldo aanvullen per bank, nooit creditcard (+3%) |
| Store credit | Optie 25% als Siraat-tegoed in plaats van 15% cash. Kost Siraat ca. 7,5 tot 9% van de netto omzet (35% variabele kosten op het tegoed, plus 0 tot 15% niet verzilverd). Social Snowball kan commissies als Shopify-kortingscode uitbetalen ([help-artikel](https://help.socialsnowball.io/en/articles/9467346-sending-discount-codes-as-commissions)). Let op: werkt alleen bij affiliates die zelf nog iets willen (deksels, snijplanken, sheets) |
| Minimum uitbetaling | $50 |
| Attributie | 14 dagen, link eerst |

**Verwachte kosten per doorverwezen order** (order $250 vóór codes, standaard 15%/10%): vriendenkorting $25, commissie $32,10 (na retouren), platform $6,40, fee $0 tot $1,30, totaal ca. **$64**. Bijdrage na alles **$88**, tegen $128 voor een gewone order met HI10. Ten opzichte van een HI10-order kost het programma $39 extra per order; het verdient zich terug zodra minstens **31%** van de doorverwezen orders echt nieuw is. Op een letterlijke 70%-sale is elke order verlieslatend, met of zonder programma; daar beschermt de netto basis de commissie in elk geval tegen meer schade.

**Eerlijk over 20%/10%:** financieel niet roekeloos zolang de sale de echte prijs niet verlaagt (bijdrage $77 per order, kosten per incrementele order onder de ads-CPA bij 50% incrementaliteit). Wel onverstandig als standaard: het ligt ver boven de branche, maakt Siraat aantrekkelijk voor couponsites, vraagt 40% incrementaliteit om het goed te maken en laat weinig ruimte als codes stapelen of als november echt dieper gaat. Beter: start op 15%, laat creators 20% verdienen met bewezen nieuwe klanten, en kijk na 8 weken naar de incrementaliteit voordat de basis omhoog gaat.

Open punten voor Floris:
- Zitten invoerrechten en inbound vracht in de Shopify-kostprijs?
- Gaat de echte verkoopprijs in november omlaag, of blijft het bij compare-at? (Bepaalt of tabel B of C relevant wordt.)
- Social Snowball-plan: Snow Day (3% van affiliate-omzet) of Blizzard (vast)?
- Verhouding tot de eerder ontworpen klantreferral (give $25, get $25, `research/referral/01-ontwerp.md`) en de bestaande affiliatecode GOODFOOD: een programma, niet twee.

## 6. Bronnen

Eigen data (read-only, 21 okt 2026): ShopifyQL `sales` laatste 30 dagen, per maand en per week (nov 2025 tot okt 2026), per product; Shopify GraphQL `products.variants.inventoryItem.unitCost`; Triple Whale summary KPIs 21 sep t/m 20 okt 2026. Tremendous-fees: zoals opgegeven door Floris (niet online geverifieerd).

Web:
- Social Snowball: [prijzen](https://socialsnowball.io/pricing), [FAQ](https://socialsnowball.io/faqs), [revenue calculation tax/shipping](https://help.socialsnowball.io/en/articles/8308786-including-excluding-tax-shipping-costs-in-revenue-calculations), [discount codes als commissie](https://help.socialsnowball.io/en/articles/9467346-sending-discount-codes-as-commissions), [tutorials (artikeltitels nieuwe klanten, self-referral, delay filters, Tremendous)](https://help.socialsnowball.io/en/collections/2994447-tutorials), [Influencer Marketing Hub review](https://influencermarketinghub.com/social-snowball/), [Roster vergelijking](https://www.getroster.com/?p=8820)
- Kookgerei: zie tabel in sectie 3
- Benchmarks: [ReferralCandy](https://www.referralcandy.com/blog/affiliate-commission-rates), [Post Affiliate Pro](https://www.postaffiliatepro.com/faq/typical-affiliate-commission-rates/)
- Commissiebasis bij andere apps (ter vergelijking): [ReferralCandy](https://help.referralcandy.com/en/articles/2457874-how-are-cash-rewards-or-commissions-calculated-on-referred-purchases), [GrowthHero](https://help.growthhero.io/article/33-commission-calculation-strategies)
- Incrementaliteit: [Hamster Garage](https://www.hamstergarage.com/article/affiliate-incrementality-ecommerce-measurement-guide), [Haus](https://www.haus.io/case-study/affiliate-on-off-test-reveals-the-incrementality-of-loyalty-sites-for-global-dtc-brand), [PartnerCentric (tegengeluid)](https://partnercentric.com/blog/affiliate-marketing-and-coupon-sites-myths-surrounding-incremental-growth)
