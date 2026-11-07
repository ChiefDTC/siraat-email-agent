# Punten en store credit voor eerdere kopers (7 nov 2026)

Vraag Floris: elke eerdere koper krijgt een persoonlijk bericht in MediaMarkt-stijl, bijvoorbeeld "Your order of $120 earned you 1,200 points = $12 store credit. Redeem it now." Elke dollar is N punten, punten zijn korting, eerdere aankopen worden beloond ("your purchase unlocked a gift") en het tegoed verloopt echt. Plus een Klaviyo-systeem "Redeem your $X".

Alleen gelezen en uitgezocht. Niets aangemaakt in Shopify, Klaviyo, Rise.ai of een andere app, geen testmails. Geen klantdata in dit stuk, alleen totalen. De BF-code heet hier BFCODE.

## 1. Kort advies

1. **Tool: Rise.ai** (staat al op de site, zie `research/cro/02-pdp-audit.md`). Rise geeft elke klant een wallet die onder water een echte Shopify gift card is. Daardoor werkt het tegoed ook voor gastkopers (zonder account), kan het in bulk via CSV met een vervaldatum worden uitgegeven, en zet Rise het saldo en de eerstvolgende vervaldatum als profieleigenschap in Klaviyo. Shopify native store credit is gratis maar vraagt dat de klant inlogt bij het afrekenen, heeft geen bulk-import en geen Klaviyo-sync: niet geschikt voor 100.000 gastkopers in drie weken.
2. **Punten zijn de presentatie, dollars de motor.** Eén vaste koers overal: **100 points = $1**. In Rise staat gewoon tegoed in dollars; de mail rekent punten uit (saldo x 100). Punten zijn ook valutaneutraal, wat past bij de regel dat er geen USD buiten de US in mails komt.
3. **Lancering (eenmalig, met terugwerkende kracht):** **10 points per $1** die de klant ooit netto betaalde (na kortingen en refunds), dus 10 procent terug. Minimaal 500 points ($5), maximaal **5,000 points ($50)**. Vervalt **30 november 2026 om 23:59** (winkeltijd), samen met de sale. Dat is echte urgentie.
4. **Doorlopend (vanaf nu, voor elke nieuwe order):** **5 points per $1** (5 procent terug), vrijgegeven 30 dagen na fulfillment (na de retourtermijn), geldig 90 dagen. Zo stapelt het nieuwe tegoed niet op de 70 procent van deze sale en trekt het een tweede order naar december en januari.
5. **Minimum besteding kan technisch niet** (tegoed is een betaalmiddel, geen korting; zie sectie 3). De marge bewaken we met het plafond van $50 en de vervaldatum, niet met regels in de kassa.
6. **Kosten:** bij 3 tot 10 procent verzilvering $70k tot $230k aan tegoed, tegen $0,8M tot $2,6M omzet. Het plan verdient zichzelf terug zolang minstens ~18 procent van de verzilverde orders er zonder het tegoed niet was geweest (sectie 4).

## 2. Uitgangscijfers (Shopify, alleen totalen)

| | Waarde | Bron |
|---|---|---|
| Kopers sinds 1 dec 2024 | 103.927 | ShopifyQL `sales` |
| Orders | 115.472 (115.639 alle) | ShopifyQL, `ordersCount` |
| Netto omzet | $25,02M (bruto $28,55M, kortingen $2,63M) | ShopifyQL |
| AOV | $222,71 (nov 2025 $243, okt 2026 $231, nov 2026 tot nu $250) | ShopifyQL |
| Netto per koper (gemiddeld) | ~$241, dus ~2,410 points of ~$24 | berekend |
| Terugkerende kopers | 8,9 procent | ShopifyQL |
| Klantaccounts | Nieuwe klantaccounts aan, inloggen bij afrekenen niet verplicht | Admin GraphQL `shop.customerAccountsV2` |
| Gift cards | Aan | `shop.features.giftCards` |

De verdeling van de levenslange besteding per klant kon ik niet ophalen (de klantfilters op bedrag werken niet via deze tool). Het effect van het plafond van $50 schat ik daarom: met een AOV van $223 en 8,9 procent herhaalkopers zit naar schatting 10 tot 15 procent van de kopers boven $500. Gemiddeld tegoed na plafond en minimum: **~$22 per koper**, totaal uitstaand ~$2,3M nominaal. Dat is geen kostenpost: kosten ontstaan alleen bij verzilvering.

Klaviyo (GET, 100 recente profielen en de volledige metriclijst): er zijn **geen Rise-eigenschappen en geen Rise-metrics** in Klaviyo. De Rise-Klaviyo-koppeling staat dus niet aan, of Rise wordt niet gebruikt. Wel aanwezig: `siraat_orders`, `siraat_first_order_at`, `siraat_last_order_at`, `siraat_owned` (nachtelijke sync), Social Snowball- en Alia-velden. "Siraat Last Order Value" kwam in de steekproef niet voor.

## 3. Tools vergeleken

| | **Rise.ai (advies)** | Shopify native store credit | Okendo Loyalty | Klaviyo unieke coupon | Puntenapp (Smile, Rivo, LoyaltyLion) |
|---|---|---|---|---|---|
| Staat al live | Script laadt op de PDP; plan en status onbekend | Ja (nieuwe klantaccounts aan) | Okendo reviews wel; loyalty-module onbekend | Ja | Nee |
| Werkt voor gastkopers | Ja, wallet is een gift card met code | **Nee, klant moet inloggen** | Via coupon na inwisselen | Ja | Na inwisselen naar code |
| Bulk uitgeven | CSV-bulktool in het dashboard, stuurt zelf geen mail; een eenmalige upload zit in elk plan | Alleen per klant via `storeCreditAccountCredit` (geen bulk-operatie): 100k losse API-calls met write-scope | Puntenimport, niet als tegoed | Codes per persoon, vast bedrag per pool | CSV-import van punten |
| Vervaldatum | Ja, per uitgifte | Ja (`expiresAt`, verloopt 23:59 winkeltijd; oudste eerst afgeboekt) | Punten-expiry | Ja | Ja |
| Klaviyo | `rise_wallet_balance`, `rise_wallet_next_expiration_date` op het profiel, events met `expiration_date` | Niets; eigen sync nodig | `Okendo Loyalty Points Balance` | Coupon Assigned | Saldo als eigenschap |
| Minimum besteding of productuitsluiting | Nee bij inwisselen; wel een minimum om tegoed te verdienen (cashback-regel) | Nee | Ja (coupon) | **Ja** | Ja (coupon) |
| Stapelt op sale en BFCODE | Ja (betaalmiddel) | Ja (betaalmiddel) | Hangt af van coupon | Nee, één code per order | Hangt af |
| Persoonlijk bedrag | Ja | Ja | Ja | Nee (vast bedrag per pool) | Ja |
| Kosten | Plannen naar ordervolume; derde partijen noemen $17 tot $600 per maand, bij ~7.000 tot 14.000 orders per maand waarschijnlijk het Pro- of Premium-plan (bronnen spreken elkaar tegen, deels van concurrent Rivo) | $0 | Okendo-plan | $0 | $49 tot $999 per maand |
| Tijd tot live | Dagen (al geinstalleerd) | Script plus eigen Klaviyo-sync, en inlogfrictie | 1 tot 2 weken | 1 dag | 1 tot 2 weken plus thema |

Waarom niet de coupon-route, terwijl die wel een minimum kan afdwingen? Floris wil een persoonlijk bedrag ("your $12") en de taal van tegoed. Een kortingscode mag volgens `research/giftcard/02-bedrag-of-korting.md` geen "credit" of "in your account" heten, en het bedrag zou per pool vast zijn. Wel bruikbaar als terugvaloptie (sectie 7).

Waarom geen echte puntenapp nu? Punten die eerst ingewisseld moeten worden voor een code voegen een stap toe en de installatie kost te veel tijd voor een sale die op 30 november eindigt. Na BFCM opnieuw bekijken als Floris een volwaardig puntenprogramma (tiers, punten voor reviews en verwijzingen) wil.

Juridisch (VS, zie ook `research/giftcard/02`): promotioneel tegoed mag verlopen, mits duidelijk staat dat het promotioneel is en wanneer het verloopt (Californie: vervaldatum duidelijk zichtbaar). In elke mail dus letterlijk: "Promotional store credit, no purchase needed to receive it. Expires November 30, 2026 at 11:59 PM ET." Nooit "gift card" noemen (het is technisch wel een gift card in Rise, maar het is promotioneel en verloopt).

## 4. Economie

Aannames (te controleren): contributiemarge per BF-order ~50 procent van de betaalde omzet (normaal ~60 procent na verzending, fulfilment en retour, zie `research/giftcard/02`; bij 70 procent korting lager), BF-order $250 (AOV nov 2026 tot nu), gemiddeld tegoed $22, en meestal wordt het hele tegoed in een order gebruikt (Shopify en Rise passen alles toe tot het orderbedrag).

Verzilvering: algemene benchmarks noemen 20 tot 30 procent van verdiende punten verzilverd en ~25 procent breakage, maar dat geldt voor actieve leden die zelf punten spaarden, en de cijfers komen vooral van leveranciers (Smile, Rivo, Spendgo). Ons geval is ongevraagd tegoed voor vooral eenmalige kopers met 23 dagen looptijd; eigen data: 8,9 procent herhaalkopers en de oude winback haalt $0,07 per ontvanger. Ik reken daarom met 3, 6 en 10 procent van de 103.900 kopers.

| Scenario | Verzilvering | Orders met tegoed | Tegoed uitgegeven | Omzet die orders | Deel echt extra | Extra contributie | Netto na tegoed |
|---|---|---|---|---|---|---|---|
| Laag | 3% | 3.120 | $69k | $780k | 50% | $195k | **+$126k** |
| Midden | 6% | 6.230 | $137k | $1,56M | 50% | $390k | **+$253k** |
| Hoog | 10% | 10.390 | $229k | $2,60M | 40% | $520k | **+$291k** |

Breakeven: een order met tegoed kost $22 en een extra order levert ~$125 contributie. Het plan wint zolang meer dan **~18 procent** van de verzilverde orders er zonder tegoed niet was geweest. Het grootste risico is dus niet het tegoed zelf, maar kannibalisatie: kopers die in de sale toch al kwamen. Plus de app-kosten (enkele honderden dollars per maand).

Effectieve extra korting op een BF-order: $22 op $250 is 8,8 procent bovenop de 70 procent. Met het plafond van $50 maximaal 20 procent van een gemiddelde order. Wie BFCODE (alleen in abandonment-flows) en tegoed combineert, krijgt maximaal ~19 procent extra; dat accepteren we, omdat het niet te blokkeren is.

Doorlopend (5 points per $1, na 30 dagen, 90 dagen geldig): op $250 is dat $12,50 tegoed. Bij 15 procent verzilvering kost het ~$0,30 per order. Doel: herhaalaankoop van 8,9 naar 11 procent in 2027. Tegoed wordt niet uitgegeven op refunds (Rise rekent op subtotaal na korting; refunds na de 30 dagen apart afboeken).

Meten: holdout. 5 procent van de kopers (willekeurig, Klaviyo `profile-sample`) krijgt geen tegoed en geen mail. Het verschil in orders per koper tussen groep en holdout tot 31 december is de echte extra omzet.

## 5. Retroactieve lancering: berekening en uitgifte

**Berekening** (script, alleen lezen, draait lokaal; de CSV komt nooit in de repo):

1. Alle orders uit Shopify (bulk-export via GraphQL `bulkOperationRunQuery`, alleen lezen): klant-e-mail, `currentSubtotalPriceSet` na refunds, valuta, financiele status.
2. Per klant: netto betaald in USD (shopValuta). Uitsluiten: volledig gerefunde orders, orders met chargeback, interne en test-accounts, wholesale-tag, klanten zonder e-mail.
3. Points = afronden(netto x 10). Minimaal 500, maximaal 5,000. Tegoed = points / 100.
4. Basis: levenslange besteding (beloont trouwe kopers en is eerlijk), niet alleen de laatste order. In de mail tonen we wel de laatste order ("Your order from March 2026 earned you ..."), want dat leest persoonlijker. Klopt alleen als de punten van die order genoemd worden; daarom twee velden: `points_last_order` en `points_total`.
5. CSV voor Rise: email, amount, expiration 2026-11-30, reason "BF26 thank-you credit". CSV voor Klaviyo (profielimport): `siraat_points`, `siraat_points_last_order`, `siraat_last_order_month`, `siraat_credit_expires` = 2026-11-30, `siraat_credit_cohort` = "bf26" of "holdout".

**Uitgifte:** Floris uploadt de Rise-CSV (bulktool; let op: de bulktool tijdens een proefperiode beeindigt de proef). Eerst 5 interne adressen, controleren, dan de rest.

**Sync naar Klaviyo:** primair via de Rise-integratie (`rise_wallet_balance`, `rise_wallet_next_expiration_date`, plus events bij uitgifte en verzilvering). Of bulk-uitgifte de profieleigenschappen meteen bijwerkt, staat nergens; daarom ook onze eigen profielimport met `siraat_points` (eenmalige startwaarde). De mails tonen het live Rise-saldo als dat er is, anders `siraat_points`:

```
{% with bal=person|lookup:'rise_wallet_balance'|default:0 %}{% widthratio bal 1 100 %} points = ${{ bal|floatformat:0 }}{% endwith %}
```

(In INT-mails alleen punten, geen dollarbedrag.)

**Valuta:** Rise-wallets zijn in USD; Shopify zet gift cards bij afrekenen om naar de lokale valuta. Nog te testen met een INT-checkout (sectie 8).

## 6. Flowkaart Klaviyo

| # | Naam | Type en trigger | Wanneer | Filters | Inhoud |
|---|---|---|---|---|---|
| L1 | "You have $X waiting" | Campagne, segment `rise_wallet_balance > 0` en cohort bf26 | Zo snel als de upload klopt, streefdatum di 17 nov 19:00 lokaal | Ingeschreven, geen holdout, geen Sunset-onderdrukking | Launch, mail A hieronder |
| L2 | Herzending | Campagne | +2 dagen, alleen niet-openers en niet-kopers | idem, geen order sinds L1 | Andere onderwerpregel, tekstmail van Benjamin |
| X1 | 7 dagen | Flow, **datumeigenschap** `rise_wallet_next_expiration_date` | 7 dagen ervoor (23 nov), 09:00 lokaal | Saldo > 0 op het moment van versturen | "Your points expire in 7 days", met BF-producten |
| X2 | 48 uur | idem | 2 dagen ervoor (28 nov, Black Friday) | idem | Countdown-mail, mail B hieronder |
| X3 | 24 uur | idem | 1 dag ervoor (29 nov) | idem | Kort, LOUD, "$X disappears tomorrow" |
| X4 | Laatste dag | idem | Dag zelf (30 nov), 12:00 lokaal | idem | "Tonight at midnight", tekstmail Benjamin |
| E1 | "You just earned X points" | Flow, trigger Placed Order (RSNxYV) | 1 uur na order | Niet in holdout | Kort: "This order will earn about {{ event.value x 5 }} points, ready on {datum + 30 dagen}". Kan ook als blok in de bestaande post-purchase P1 (liever, minder mails) |
| E2 | "Your points are ready" | Flow, trigger Rise-event uitgifte (naam pas zichtbaar na koppeling) | Direct | Saldo > 0 | "2,490 points = $24.90 ready to use until {datum}" |
| X1 tot X3 doorlopend | Dezelfde datumflow | Werkt na BF voor elk tegoed met 90 dagen | 7 d, 2 d, 1 d | | Zelfde mails zonder sale-taal (aparte tak op cohort) |

Regels:
- Datumflow: de eigenschap moet een echte datum zijn in Klaviyo (ISO). Rise zet die; ons importveld `siraat_credit_expires` als datum importeren, zodat de flow ook op ons veld kan draaien als Rise niet synct.
- Iedereen die verzilvert, valt automatisch uit X1 tot X4 (saldo 0). Gedeeltelijk verzilverd: mail toont het restsaldo.
- Campagne-cap en smart sending zoals de BF-kalender; L1 vervangt die avond een gewone BF-campagne voor kopers, niet erbij.
- Winback UyFc78 en de BF-winback (`research/plannen/2026-11-sunset-winback.md`) krijgen een dynamisch blok "You have X points ($Y) until Nov 30" als `rise_wallet_balance > 0`.
- Vaste header en footer, logo als lockup, Benjamin als afzender en ondertekening, 30-day returns, 75-year warranty, 100,000+ happy customers. Geel alleen op sale-tags. Previews in Figma (oaxnBkz3MAbePRnorCrQwz) bij de bouw.

## 7. Terugvaloptie als Rise niet kan

Als Rise geen bulk of Klaviyo-koppeling in het plan heeft of te duur is: Klaviyo unieke coupons in vier pools (500, 1,000, 2,500, 5,000 points = $5, $10, $25, $50 off, minimum $100, vervalt 30 nov). Elke klant krijgt de pool die het dichtst onder zijn punten ligt. Voordeel: minimumbedrag afdwingbaar, geen app. Nadelen: bedrag is afgerond, het mag geen "store credit" heten ("$25 off, earned by your past orders"), en het stapelt niet met BFCODE. Shopify native store credit alleen als Floris accepteert dat klanten moeten inloggen bij het afrekenen.

## 8. Wat Floris moet doen, per app

**Rise.ai (dashboard)**
1. Controleer of Rise actief is en welk plan: nodig zijn bulk store credit, Klaviyo-integratie en cashback/workflows. Zo nodig upgraden (vraag de prijs bij ~10.000 orders per maand in BF).
2. Integrations > Klaviyo: koppelen. Rise-eigen mails voor store credit **uitzetten** (anders dubbele mails).
3. Instellingen wallet: valuta en weergave op de accountpagina; balanswidget op de site aan (of uit tot 17 nov).
4. Test met 5 interne adressen via de bulktool (bedrag, vervaldatum 30 nov 23:59): controleer in Klaviyo of `rise_wallet_balance` en `rise_wallet_next_expiration_date` binnen een uur verschijnen.
5. Testorders: tegoed plus sale plus 5 gifts; tegoed plus BFCODE; INT-checkout in GBP of EUR; gastcheckout met de walletcode; werkt een checkout-link die het tegoed automatisch toepast?
6. Volledige CSV uploaden (die maak ik op akkoord, buiten de repo).
7. Cashback-regel doorlopend: 5 procent van subtotaal, uitgifte 30 dagen na fulfillment, geldig 90 dagen, geen tegoed op refunds.

**Shopify**
8. Geen wijziging nodig voor Rise. Wel: Gorgias-macro "How do I use my points?" en een FAQ-regel op de site.

**Klaviyo**
9. Profielimport met `siraat_points`, `siraat_points_last_order`, `siraat_last_order_month`, `siraat_credit_expires`, `siraat_credit_cohort` (ik lever het bestand, Floris of ik op akkoord).
10. Segment "Points · balance > 0 · bf26", holdout-segment, campagnes L1 en L2, datumflow X1 tot X4, E1 als blok in P1. Templates bouw ik op akkoord.

## 9. Twee voorbeeldmails (opzet, geen HTML)

**Mail A · L1 launch (campagne, US)**
- Onderwerp: "Your past order earned you {{points}} points"
- Preview: "That's ${{credit}} off anything in the Black Friday Sale. Until Nov 30."
- Afzender: Benjamin from Siraat
- Vaste header (lockup).
- Hero: Floris' gouden kaart als kopie met "1,200 POINTS" in plaats van "GIFT CARD" (origineel niet aanpassen), kop "Your order earned you 1,200 points." subregel "= $12 in store credit, ready to use now".
- Persoonlijke regel: "Your order in March 2026 earned you {{points_last_order}} points. Together with your other orders, you now have {{points}} points = ${{credit}}."
- Knop: "Use my ${{credit}}" naar de BF-collectie. Friction reducer: "Applied at checkout. Stacks with up to 70% off. 30-day returns."
- Hoe het werkt, drie iconregels: 1. Pick anything in the sale. 2. Your credit is applied at checkout (or enter code {{wallet_code}}). 3. Your 5 free gifts ship with it.
- Blok 5 gifts (gifts5, US "$555 value").
- Twee productkaarten (Pan Pro Standard, 6-delige set) met sale-tag in geel.
- Benjamin, twee zinnen: "You were here before most people knew what a titanium pan was. This is our thank you."
- Juridische regel klein boven de footer: "Promotional store credit, no purchase needed to receive it. Expires November 30, 2026 at 11:59 PM ET. 100 points = $1. Not redeemable for cash."
- Vaste footer.
- INT-versie: alleen punten, "applied in your currency at checkout", INT-friction reducer.

**Mail B · X2 48 uur (flow, Black Friday)**
- Onderwerp: "{{points}} points expire in 48 hours"
- Preview: "${{credit}} is still in your account. After Sunday it's gone."
- Codebalk boven de header: "YOUR ${{credit}} CREDIT · EXPIRES NOV 30, 11:59 PM ET".
- Vaste header.
- Hero: countdown-beeld (echte deadline) met "${{credit}} LEFT".
- Saldo groot, live uit Rise: "You still have {{points}} points = ${{credit}}." Bij gedeeltelijk verzilverd: "You used some already. {{points}} points are left."
- Knop: "Use my ${{credit}} before Sunday".
- Rekensom op een bestseller: "Pan Pro Standard: sale price minus your ${{credit}} = you pay $X" (via PRICE-macro, alleen US).
- Reviews (reviews3, 2 echte Trustpilot-reviews).
- Friction reducer en dezelfde knop nog een keer.
- Juridische regel en vaste footer.

## 10. Open vragen voor Floris

1. Is Rise actief en op welk plan? Mag het geupgraded worden voor bulk, Klaviyo en cashback?
2. Akkoord op 10 points per $1 retroactief, minimum 500, plafond 5,000 ($50), op levenslange netto besteding?
3. Vervaldatum 30 nov 23:59 ET voor het lanceringstegoed, en daarna 5 points per $1, 30 dagen wachttijd, 90 dagen geldig?
4. Akkoord dat het tegoed stapelt met 70 procent off, gifts en BFCODE (niet te blokkeren)?
5. INT meedoen in de lancering (punten in mail, omrekening bij afrekenen), of alleen US?
6. Holdout van 5 procent voor de meting?
7. Juridische regel (promotioneel, vervaldatum) door iemand laten lezen vanwege Californie?
8. Wie uploadt: Floris de Rise-CSV en ik de Klaviyo-profielimport, of alles door Floris?

## Bronnen

- Rise.ai: [Klaviyo store credit emails setup](https://help.rise.ai/en/articles/9997285-rise-ai-klaviyo-store-credit-emails-setup), [Rise Klaviyo integration](https://help.rise.ai/en/articles/4002782-rise-klaviyo-integration), [Advanced actions Klaviyo](https://help.rise.ai/en/articles/5178932-advanced-actions-with-klaviyo-x-rise-integration), [Bulk loyalty card tool](https://help.rise.ai/en/articles/5682663-how-to-use-the-bulk-loyalty-card-tool), [Bulk wallet creation](https://intercom.help/internal-303707/en/articles/10429356-bulk-wallet-creation), [Cashback program setup](https://intercom.help/internal-303707/en/articles/12305862-cashback-program-setup-guide), [How Rise data is mapped in Shopify](https://intercom.help/internal-303707/en/articles/13770961-how-rise-ai-data-is-mapped-in-shopify), [Multi-currency](https://intercom.help/internal-303707/en/articles/12617287-using-rise-ai-in-stores-that-sell-in-multiple-currencies), [Shopify App Store](https://apps.shopify.com/gift-card-loyalty-program). Prijzen: [Rivo over Rise-prijzen](https://www.rivo.io/blog/rise-ai-pricing) (concurrent), [Costbench](https://costbench.com/software/loyalty-program/rise-ai/).
- Shopify: [Store credit help](https://help.shopify.com/en/manual/customers/store-credit), [StoreCreditAccountCreditInput](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/StoreCreditAccountCreditInput), [community: geen bulk-operatie](https://community.shopify.dev/t/how-to-apply-customer-credit-in-bulk-to-1000-customers/3719), [store credit als betaalmiddel](https://apps.shopify.com/built-in-features/store-credit).
- Okendo: [Okendo data sent to Klaviyo](https://support.okendo.io/en/articles/15307216-okendo-data-sent-to-klaviyo), [Use loyalty with Klaviyo](https://support.okendo.io/en/articles/8978453-use-loyalty-with-klaviyo).
- Benchmarks (leveranciers, met voorzichtigheid): [Smile.io loyalty metrics](https://blog.smile.io/loyalty-metrics-program-performance), [Rivo points expiry statistics](https://www.rivo.io/blog/points-expiry-impact-statistics), [Eightx loyalty economics](https://eightx.co/blog/loyalty-program-economics-5pct-earn-rate), [Voucherify loyalty breakage](https://voucherify.io/glossary/loyalty-breakage), [Spendgo redemption rate](https://resources.spendgo.com/blog/understanding-average-loyalty-program-redemption-rate-tips-for-improving-yours).
- help.rise.ai en help.shopify.com waren vanuit deze sessie niet direct te openen (netwerk); de inhoud komt uit zoekresultaten. Voor de bouw de pagina's zelf nalezen.
