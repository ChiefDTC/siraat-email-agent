# 04 · Actieplan: top 15 fixes

Gerangschikt op verwachte extra omzet (of behouden marge) per maand, gecorrigeerd voor moeite. Bedragen zijn schattingen op basis van 01 tot 03 (periode 7 sept tot 6 okt 2026, $1,07 miljoen netto per maand, 4.609 orders, AOV $232). Ze overlappen deels en zijn niet op te tellen; de som van de "realistisch"-kolom ligt ruwweg op $150.000 tot $250.000 per maand extra.

Moeite: S = uren, M = dagen, L = weken. Eigenaar: Floris (beslissing of instelling in Shopify, Aftersell, Markets), dev (theme, Replo, scripts), Claude (copy, mails, testopzet, analyse).

| # | Fix | Waarom (bewijs) | Extra per maand | Moeite | Eigenaar | Test? |
|---|---|---|---|---|---|---|
| 1 | **99- en 100-procentcodes uitzetten; EXTRA30, SK25, B2B25, SORRY25, LABOR20, MEMORIAL, BFEXTRA10, NYEXTRA10 einddatum; HI10 "once per customer"** | `98347983474334593` (99 %, onbeperkt, 5 keer gebruikt sinds 6 okt, $1.656 weggegeven), `SRJACEP6YNN1` en kopie (100 %), `SJHNDFJNSAD934` (100 %); 19 % van de orders gebruikt een code | $10.000 tot $20.000 marge, plus het voorkomen van een onbeperkt verlies | S | Floris | Nee |
| 2 | **Nep-urgentie en onware leverclaims van de PDP halen** (countdown die per sessie op 02:42 begint, "High demand, few units left" bij 1.098 op voorraad, "Local warehouse / Free Express Shipping from the US") | Live gezien op alle pannen-PDP's; tickets over herkomst China en chargebacks "merchant misrepresentation"; terugkerende bezoekers (2,7x zoveel waard) zien de timer elke dag opnieuw | $20.000 tot $45.000 (minder refunds en chargebacks, hogere CR bij terugkerende bezoekers; deel als test meten) | S | dev, Claude levert vervangtekst | Deels: "eerlijke deadline" tegen "geen timer" als Intelligems content-test |
| 3 | **Eén retourbelofte overal** (PDP "cook on it 30 days, full refund, free returns" tegen beleid "used cannot be returned, customer pays return shipping") | Tickets met $12 tot $30 retourkosten die naar "free returns" verwijzen; 12,4 % refunds op orders boven $700 | $15.000 tot $35.000 (CR van twijfelaars plus minder disputes); kies A (echte gratis gebruikstest) of B (eerlijk "unused") | S tot M | Floris beslist, Claude teksten, dev | Ja, als Floris A overweegt: A tegen B op PDP-badge, beslissen op winst per bezoeker na retouren |
| 4 | **Live chat-test uitlopen en uitrollen** | Intelligems "live chat" (sinds 4 okt, 46.194 bezoekers): CR 1,20 naar 1,35 % (+12 %), omzet per bezoeker +12 %, kans beter dan controle 92 %; nog niet klaar (te kort) | $40.000 tot $85.000 als het effect standhoudt (+$0,31 per bezoeker op 280.000 bezoekers), realistisch de helft | S | Floris | Ja, loopt: tot 14 dagen en 300 orders per arm, dan beslissen |
| 5 | **Verboden en onbewezen claims van alle PDP's en collecties** (indestructible, built to last a lifetime, 548°C/1000°F, 750°F, Stay Cool Handle, naturally nonstick als kop, "purifier", "Scientifically proven ... nutrients", "30 of 30 tests") | Live gezien (02, 0a); DECISIONS en claims.csv; de zichtbare 1-sterreview op de PDP citeert letterlijk "Siraat advertises it as naturally nonstick" | $10.000 tot $25.000 (verwachtingen kloppen, minder plak-retouren) plus juridisch risico weg | M | Claude teksten, dev metafields en theme | Nee (compliance) |
| 6 | **PDP Pan Pro: bezwaar "plakken" boven de vouw, Mini als vierde maatkaart, deksel-vinkje, prijs en knop boven de vouw op desktop, chatknop niet over de Large-kaart** | 155.268 landingssessies op één PDP, 76 % bounce, ATC 5,3 %; plakken is het nummer-1-bezwaar (60 van 400 tickets, 81 van 154 lage reviews); 41 tickets over deksels | $30.000 tot $70.000 | M | dev, Claude copy | Ja, Intelligems content/template-test op de Pan Pro, 14 dagen, beslissen op winst per bezoeker |
| 7 | **Cart-mails en welcome-links repareren** (`/discount/CODE?redirect=/cart` geeft op een ander apparaat een lege winkelwagen; geen bevestiging dat de code actief is; ongeldige code faalt stil) | Live getest; email-bezoekers CR 2,9 % maar 46 % verlaten checkouts; v3-coupons bestaan nog niet in Klaviyo | $10.000 tot $25.000 | S tot M | Claude (templates: cart-permalink of recovery-URL, PDP als landing), dev (banner "HI10 applied at checkout") | Banner: ja (Intelligems); links: nee |
| 8 | **Code-combinatie met de gratis gifts oplossen** (HI10 en SIRAAT10 combineren niet met product- of orderkortingen; Bogos-gifts en $77.500 aan automatische korting per maand) | Tickets "the discounts were never applied", "code doesn't work"; te bevestigen in de checkout (05) | $8.000 tot $20.000 | S tot M | dev, Floris | Nee, eerst vaststellen |
| 9 | **EU, CH, NO: DDP aan in Shopify Markets en orderbevestiging herschrijven, of deze landen uit de advertenties** | IT 0,15 % CR op 16.076 sessies, DE 0,27 %, NL 0,28 %, 66 % verlaten checkouts; bevestiging zegt "VAT or import duties may be charged"; 152 tickets over customs in 60 dagen | $25.000 tot $50.000 extra omzet, of hetzelfde bedrag minder verspild advertentiebudget | M | Floris | Nee |
| 10 | **Paid search niet meer op blog en content laten landen; advertorials "10 reasons" en "Michelin" herzien of uit** | 24.463 betaalde zoeksessies op blog/content (86 % bounce op blog); paid search CR 1,07 % tegen 1,97 % paid social, -21 %; advertorials 0,65 % en 0,40 % tegen chef-advertorial 1,47 %; /cfv6 geeft 404 (4.281 sessies) | $20.000 tot $40.000 | S tot M | Floris (ads), dev (/cfv6) | Ja, Intelligems URL-split: chef-advertorial tegen 10-reasons op hetzelfde verkeer |
| 11 | **BNPL buiten de VS (Afterpay/Clearpay/Klarna voor AU, NZ, UK, CA) en termijnregel in de winkelwagen bij $349+** | AU is tweede markt (609 orders, $114.000 per maand) zonder herkenbare BNPL; Affirm werkt niet in CA; carts $600+ betalen maar 63 % | $15.000 tot $30.000 | S | Floris | Nee (betaalmethode); de cart-regel wel als test |
| 12 | **Aftersell: tweede en derde funnel, stap 2 vullen, bevestiging boven $300, 12-set niet aan niet-US** | Aanbod bij 44 % van de orders; stap 2 één conversie; "No funnel matched" 120 per maand; ticket over een niet-gewilde set-upsell | $15.000 tot $25.000 | S | Floris | Ja, Aftersell split-test per funnelstap |
| 13 | **Set-PDP's: compare-at = som van losse prijzen, "wat zit erin" boven de vouw, één bedrag (12-set "$587" tegen "$487"), BDAY-tekst weg en BDAY-listing redirecten** | 12-set: 89 % bounce, hoogste omzet per sessie; 6-set: twee listings met dezelfde prijs; Mini "2 Pans + 2 Lids $199 / $844" | $15.000 tot $35.000 | M | Floris (prijzen), dev, Claude copy | Ja, anker-test in Intelligems (huidig anker tegen som van losse prijzen), beslissen op winst per bezoeker |
| 14 | **Trust-blok in winkelwagen en checkout** ("4.8 from 3,281 reviews · 75-year warranty · 30-day returns · free tracked shipping") en geen timer in de checkout | Winkelwagen naar checkout 46,5 %, mobiel 75 % verlaten carts | $10.000 tot $30.000 | S | dev, Claude copy | Ja, Intelligems checkout-block (trustBadge) |
| 15 | **Testdiscipline en scriptdieet**: één test per paginagebied, minimaal 14 dagen en 300 orders per arm; Loox naast Okendo en OptiMonk naast Alia schrappen | 5 tests tegelijk op dezelfde pagina's sinds 1 tot 4 okt; prijstest USD gestopt na 2 dagen (137 tegen 42 orders) terwijl de eigen beschrijving 14 dagen en 300 orders eist; FREE GIFTS-test na 1 dag; Upgrade & Save US: CR -16 %, omzet per bezoeker -2 % (stoppen); 174 scripts van 22 domeinen op de PDP, LCP p75 2.492 ms | indirect: voorkomt dat verkeerde winnaars worden uitgerold; snelheid houdt mobiel onder 2,5 s | S | Claude (testkalender), Floris, dev | n.v.t. |

## Wat als test moet en wat niet

Direct doen, geen test (juridisch, eerlijkheid of kapot): 1, 2 (behalve de vervangende deadline), 3 (als B), 5, 7 (links), 8, 9, 11 (betaalmethode).

Intelligems-tests, in deze volgorde, één tegelijk per gebied:
1. Live chat (loopt, laten uitlopen).
2. Pan Pro PDP-template (fix 6), daarna de anker-test op de sets (fix 13).
3. Trust-blok in de checkout (fix 14).
4. URL-split advertorials (fix 10).
5. Daarna pas weer prijzen: de klaarstaande SGD-, CAD- en AUD-tests en de USD ABC "4-gift block" (die laatste heeft een regels-pagina voor de loterij nodig).

Stoppen: "Template Changes Test · okt 1" (Upgrade & Save US): CR 2,41 naar 2,04 procent, kans beter dan controle 2 procent, omzet per bezoeker -2 procent, winst per bezoeker -5 procent. "collection template": omzet per bezoeker -7 procent (nog niet significant, laten uitlopen of stoppen als de live chat-test schoon moet blijven).

## Eerste week

| Dag | Wat | Wie |
|---|---|---|
| 1 | Codes (fix 1), countdown, "few units left" en "local warehouse" weg (fix 2) | Floris, dev |
| 1 | Besluit retourbelofte A of B (fix 3) | Floris |
| 2 tot 3 | Claimteksten voor alle PDP's en collecties (fix 5), retour- en verzendteksten per markt | Claude |
| 2 tot 3 | Cart-mail-links en coupons in Klaviyo (fix 7) | Claude |
| 3 | Checkout handmatig doorlopen met HI10 en met een flowcode (05, stap 4 tot 6) en combinatie vaststellen (fix 8) | Floris of dev |
| 4 | Upgrade & Save US-test stoppen; live chat laten lopen | Floris |
| 5 | DDP-besluit EU/CH/NO of advertenties uit (fix 9); /cfv6 herstellen | Floris |
| 7 | Pan Pro PDP-test live (fix 6) | dev, Claude |
