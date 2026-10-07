# 01 · De funnel in cijfers

Periode: 7 september tot en met 6 oktober 2026 (30 dagen). Alleen gelezen, niets gewijzigd.
Bronnen: Intelligems sitewide (sessies, funnelstappen, per apparaat, kanaal, land, bezoekerstype), Triple Whale (omzet, advertentie-uitgaven, landingspagina's, Core Web Vitals, kortingscodes), Klaviyo API (Checkout Started RfMvni en Placed Order RSNxYV, 30 sept tot 7 okt), Shopify Admin API (betalingen van de laatste 250 orders), Aftersell.

Let op bij het lezen:
- Intelligems labelt de valuta als "EUR", maar de winkel rekent in USD (Shopify `currencyCode: USD`, Triple Whale USD). De bedragen zijn dollars.
- Intelligems telt conversie per sessie in de funnel (1,36 procent) en per bezoeker in de KPI's (1,64 procent). Triple Whale meet met zijn eigen pixel lager (1,18 procent per sessie). De verhoudingen tussen segmenten kloppen in alle drie de bronnen; de absolute cijfers verschillen.
- De hele periode ligt 22 tot 26 procent lager dan de 30 dagen ervoor (bezoekers -25 procent, orders -26 procent, omzet -22 procent). De conversie zelf is vlak (-0,6 procent). Het verlies zit dus in het verkeer, niet in de site.

## 1. Topline

| Wat | Waarde | Bron |
|---|---|---|
| Sessies | 339.651 | Intelligems |
| Unieke bezoekers | 280.823 | Intelligems |
| Orders | 4.609 (Shopify incl. TikTok en concepten: 5.119) | Intelligems, Triple Whale |
| Netto-omzet | $1.069.658 | Intelligems |
| Bruto verkoop | $1.182.688 | Triple Whale |
| AOV | $232 | Intelligems |
| Omzet per bezoeker | $3,80 | Intelligems |
| Advertentie-uitgaven | $624.656 (Meta $396.945, Google $194.578, TikTok $23.581, AppLovin $9.552) | Triple Whale |
| Blended ROAS / NC-ROAS | 1,89 / 1,62 | Triple Whale |
| Nettowinst na alles | $93.290 (7,9 procent) | Triple Whale |
| Kortingen | $135.511 (11,5 procent van bruto) | Triple Whale |
| Terugbetalingen | $71.009 (6,0 procent) | Triple Whale |
| Nieuwe klanten | 83,7 procent van de orders | Triple Whale |

Wat dit betekent: met 7,9 procent nettomarge en NC-ROAS 1,62 is elke procentpunt conversie op betaald verkeer direct winst. Een conversieverbetering van 10 procent op dezelfde advertentiebudgetten is circa $107.000 extra omzet per maand en vrijwel de hele huidige nettowinst erbij.

## 2. De funnel (sessies, sitewide)

| Stap | Sessies | Van vorige stap | Van alle sessies |
|---|---|---|---|
| Sessies | 339.651 | | 100 % |
| Bekeek een PDP | 248.966 | | 73,3 % |
| Bounce (1 pagina) | 242.893 | | 71,5 % |
| Toegevoegd aan winkelwagen | 17.854 | 7,2 % van PDP-bekijkers | 5,25 % |
| Checkout gestart | 8.297 | 46,5 % van ATC | 2,42 % |
| Betaald | 4.558 | 54,9 % van checkouts | 1,34 % |

Bron: Intelligems conversiefunnel en snapshot "conversion".

De drie grote kranen:
1. **PDP naar winkelwagen**: van 100 PDP-bekijkers doen er 7 iets. 71 procent van alle sessies stuitert.
2. **Winkelwagen naar checkout**: 9.557 winkelwagens per maand worden nooit een checkout (53,5 procent).
3. **Checkout naar betaald**: 3.739 gestarte checkouts per maand worden niet betaald (45,1 procent). Bij $232 AOV is dat $867.000 aan winkelwaarde per maand.

Klaviyo bevestigt dit apart (geïdentificeerde checkouts, 30 sept tot 7 okt): 2.225 unieke profielen startten een checkout, 1.513 (68 procent) betaalden binnen de week, 712 niet. Alleen de USD-checkouts die niet betaald werden: $89.807 in 7 dagen.

## 3. Per apparaat

| Apparaat | Sessies | PDP-view | ATC | Checkout | CR (sessie) | Verlaten winkelwagen | Verlaten checkout | AOV | Omzet |
|---|---|---|---|---|---|---|---|---|---|
| Mobiel | 277.195 (82 %) | 77,1 % | 5,45 % | 2,45 % | 1,36 % | 75,0 % | 44,3 % | $227 | $859.745 |
| Desktop | 62.456 (18 %) | 56,4 % | 4,36 % | 2,31 % | 1,32 % | 69,8 % | 42,9 % | $254 | $209.913 |

Bron: Intelligems. Triple Whale geeft hetzelfde beeld (mobiel 1,18 procent, desktop 1,24 procent, tablet 1,14 procent).

Conclusie: mobiel is geen apart probleem. Mobiel doet zelfs meer add-to-carts. Het mobiele verlies zit in winkelwagen naar checkout (75 procent verlaat de winkelwagen tegen 70 procent op desktop) en in de vorige 30 dagen daalde mobiel CR met 10 procent terwijl desktop steeg. Core Web Vitals (Triple Whale, p75 alle apparaten): LCP 2.492 ms (net onder de grens van 2.500), INP 184 ms, CLS 0, TTFB 128 ms, FCP 2.136 ms. Geen rood, wel krap: één extra zwaar hero-beeld of script duwt LCP over de grens.

## 4. Per kanaal

| Kanaal | Sessies | CR (bezoeker) | AOV | Omzet / bezoeker | Omzet | Funnel (PDP / ATC / checkout / verlaten checkout) |
|---|---|---|---|---|---|---|
| Paid Social | 136.591 | 1,97 % | $207 | $4,08 | $471.915 | 89 % / 6,4 % / 2,8 % / 40 % |
| Paid Search | 106.211 | 1,07 % | $251 | $2,67 | $250.120 | 78 % / 3,9 % / 1,7 % / 46 % |
| Direct | 29.938 | 0,82 % | $279 | $2,27 | $59.902 | |
| Organic Search | 26.418 | 1,28 % | $254 | $3,25 | $77.236 | |
| Email (Klaviyo) | 22.438 | 2,89 % | $242 | $7,00 | $119.197 | coll. 48 % / 7,9 % / 4,0 % / 46 % |
| Other | 11.638 | 3,04 % | $293 | $8,90 | $74.468 | |
| Organic Social | 4.410 | 1,08 % | $213 | $2,29 | $9.801 | |
| SMS | 1.698 | 1,75 % | $234 | $4,09 | $5.147 | |

Bron: Intelligems audience source_channel en conversion-snapshot per kanaal.

Opvallend:
- **Paid Search** converteert half zo goed als Paid Social en zakte 21 procent in CR ten opzichte van de vorige periode. 24.463 betaalde zoeksessies (23 procent) landen op een blog of contentpagina in plaats van een PDP (Intelligems Sankey: 12.358 naar Blog, 12.105 naar Content). Blogsessies stuiteren 86 procent en leveren 23 winkelwagens op 32.079 sessies.
- **Email** heeft de hoogste koopintentie maar 46 procent verlaten checkouts, net zo hoog als paid search. 40 procent van de mailklikken landt op een collectie, 17 procent op "Other" (de /discount/-redirect en checkout-recovery). Zie 03, paragraaf 7.
- **Direct** zakte 37 procent in CR. Veel "direct" is in werkelijkheid mail-app-verkeer zonder UTM en terugkerende kopers die een code proberen.

## 5. Per land

| Land | Sessies | CR (bezoeker) | AOV | Omzet | Opmerking |
|---|---|---|---|---|---|
| US | 179.128 | 1,98 % | $244 | $715.035 | 67 % van de omzet |
| AU | 28.913 | 2,41 % | $192 | $108.815 | beste markt per bezoeker |
| SG | 23.409 | 1,02 % | $232 | $46.102 | |
| CA | 19.230 | 1,63 % | $196 | $50.188 | Affirm werkt niet voor CA (Gorgias) |
| **IT** | **16.076** | **0,15 %** | $284 | $6.244 | 22 orders op 14.351 bezoekers |
| GB | 12.808 | 1,61 % | $214 | $36.458 | |
| AE | 8.110 | 1,69 % | $213 | $23.473 | |
| HK | 7.332 | 1,60 % | $239 | $21.752 | |
| **DE** | **6.976** | **0,27 %** | $250 | $4.246 | CR -73 % tegen vorige periode |
| IE | 5.339 | 1,07 % | $201 | $9.030 | |
| Overig | 32.330 | 0,77 % | $238 | $48.315 | NL 0,28 %, CH 0,79 %, FR 0,42 %, SE 0,20 %, JP 0,24 % (Triple Whale) |

Bron: Intelligems audience country_code; aanvulling Triple Whale web_analytics.

IT en DE samen: PDP-view 46 procent, ATC 1,3 procent, verlaten winkelwagen 87 procent, **verlaten checkout 66 procent** (sitewide 44 procent). Dat is geen productprobleem maar een vertrouwens- en kostenprobleem in de checkout. De orderbevestiging voor Europa zegt letterlijk "shipped from a warehouse outside of Europe ... VAT or import duties may be charged in some cases" (Gorgias 92082034), terwijl de site "free worldwide shipping" en "in most cases no customs duties" belooft. Europese kopers die dat lezen annuleren of starten een chargeback ("merchant misrepresentation", Gorgias 85587094).

## 6. Nieuw tegen terugkerend

| Type | Bezoekers | Orders | CR | AOV | Omzet / bezoeker | Omzet |
|---|---|---|---|---|---|---|
| Nieuw | 258.117 (84 %) | 3.174 | 1,23 % | $224 | $2,75 | $710.931 |
| Terugkerend | 48.069 | 1.435 | 2,99 % | $250 | $7,46 | $358.727 |

Nieuwe bezoekers: ATC 4,5 procent, checkout 2,1 procent, verlaten checkout 43 procent. De terugkerende bezoeker is 2,7 keer zoveel waard. De nieuwe bezoeker uit een advertentie moet op de PDP overtuigd worden, want 71 procent ziet maar één pagina.

## 7. Landingspagina's (Triple Whale pixel, 30 dagen)

| Landingspagina | Sessies | Bounce | ATC | Orders | CR | Omzet / sessie |
|---|---|---|---|---|---|---|
| /products/original-siraat-...-hammered-pattern (Pan Pro Standard) | 155.268 | 76 % | 5,3 % | 2.242 | 1,44 % | $2,98 |
| /best-non-toxic-pans-2026/ (vergelijkingssite bestpansreviewed) | 22.247 | 86 % | 0,06 % | 4 | 0,02 % | $0,06 |
| Pan Pro Large | 17.088 | 75 % | 5,7 % | 236 | 1,38 % | $2,91 |
| / (home) | 16.209 | 54 % | 6,5 % | 331 | 2,04 % | $5,65 |
| /pages/chef-advertorial | 12.070 | 60 % | 4,9 % | 178 | 1,47 % | $2,84 |
| /collections/warehouse-clearance | 11.515 | 63 % | 7,3 % | 194 | 1,68 % | $4,11 |
| /pages/10-reasons-why-families-are-switching | 10.388 | 77 % | 2,3 % | 68 | 0,65 % | $1,10 |
| /pages/michelin-star-chefs-recommend | 8.296 | 75 % | 1,8 % | 33 | 0,40 % | $0,89 |
| /collections/prime-sale | 6.109 | 66 % | 5,5 % | 64 | 1,05 % | $2,08 |
| Pan Pro Small | 6.005 | 80 % | 4,7 % | 55 | 0,92 % | $1,66 |
| Deep Pan Pro | 5.586 | 79 % | 3,4 % | 40 | 0,72 % | $2,11 |
| **12-Pcs Cookware Set** | 5.407 | **89 %** | 3,1 % | 48 | 0,89 % | $4,64 |
| Cutting Board V2 | 5.193 | 72 % | 6,2 % | 90 | 1,73 % | $2,56 |
| Pizza Steel | 4.741 | 84 % | 5,3 % | 88 | 1,86 % | $3,91 |
| /cfv6 | 4.281 | 93 % | 0,05 % | 0 | 0 % | $0 |
| Crêpe Pan | 4.071 | 83 % | 5,5 % | 44 | 1,08 % | $1,94 |
| 6-Pcs Pan Set | 2.774 | 81 % | 6,3 % | 51 | 1,84 % | $6,94 |
| /collections/all | 2.265 | 60 % | 8,7 % | 65 | 2,87 % | $7,81 |
| Pan Pro Mini | 2.079 | 80 % | 6,5 % | 50 | 2,41 % | $3,85 |
| Roasting Pan | 1.557 | 82 % | 5,2 % | 12 | 0,77 % | $1,51 |

Notities:
- De vergelijkingssite (bestpansreviewed.com en bestpanreviewed.thehiddenstudy.com, beide domeinen staan in Shopify) stuurt wel kopers door: 176 van 2.225 geïdentificeerde checkouts kwamen van bestpansreviewed.com (Klaviyo, week 30 sept). De 0,02 procent CR op die landing is dus een meetartefact (de klik naar de winkel start een nieuwe sessie). Zie 03 voor het vertrouwensrisico.
- /cfv6: 4.281 sessies, 93 procent bounce, 0 orders. Een dode of kapotte advertentie-URL. Uitzetten of herstellen.
- De 12-delige set heeft de hoogste bounce van alle PDP's (89 procent) bij de hoogste omzet per sessie. Dat is de PDP met het meeste geld per verbeterde procent.
- Advertorials "10 reasons" (0,65 procent) en "Michelin" (0,40 procent) halen een derde van de chef-advertorial (1,47 procent). Samen 18.684 sessies.

## 8. Orderwaarde en betaalmiddelen

| Orderwaarde | Orders | Omzet | Terugbetaald |
|---|---|---|---|
| < $100 | 439 | $23.537 | 1,6 % |
| $100 tot $199 | 3.082 (60 %) | $454.001 | 1,0 % |
| $200 tot $349 | 811 | $204.411 | 1,6 % |
| $350 tot $499 | 285 | $119.117 | 2,5 % |
| $500 tot $699 | 273 | $169.490 | 5,3 % |
| $700 en meer | 229 | $212.132 | **12,4 %** |

Bron: Triple Whale orders_table, Shopify-orders.

787 orders per maand boven $350 brengen $500.000 op (47 procent van de omzet). In de checkout-data (Klaviyo) zit 23 procent van de geïdentificeerde checkouts boven $349; daarvan betaalde 70 procent (onder $100: 29 procent, $100 tot $199: 77 procent).

Betaalmiddelen in de laatste 250 orders (Shopify): Shopify Payments 218 (bijna allemaal Shop Pay, daarna Apple Pay, 1 Google Pay), PayPal 24 (9,6 procent), Shop Cash 4, TikTok 2, **Affirm 1**. Shop Pay Installments is actief in de VS (de live PDP toont "4 interest-free installments, or from $12.09/mo with Shop"). Klarna, Afterpay en Clearpay ontbreken; voor AU, UK, CA en NZ is er dus geen herkenbare BNPL, en Affirm werkt volgens een klant niet voor Canada (zie 03).

## 9. Waar lekt het meeste geld (dollars per maand)

Schattingen op basis van de cijfers hierboven, conservatief (lage kant) en realistisch (hoge kant). Niet optelbaar zonder overlap: een verbetering op de PDP verandert ook de mix verderop.

| # | Lek | Wat er nu gebeurt | Hefboom | Extra omzet per maand |
|---|---|---|---|---|
| 1 | PDP naar winkelwagen (betaald verkeer) | 225.871 sessies landen op een PDP, 71 % stuitert, ATC 5,25 % | ATC +10 % relatief (5,25 naar 5,8 %) via claims, prijsanker, bewijs, maathulp; ATC-naar-order blijft 25,5 % | $55.000 tot $110.000 |
| 2 | Checkout naar betaald | 3.739 verlaten checkouts ($867.000 winkelwaarde) | voltooiing 54,9 naar 58 % via betaalopties, duidelijke retour- en douanetekst, code-conflicten oplossen, recovery-link | $40.000 tot $70.000 |
| 3 | Winkelwagen naar checkout | 9.557 winkelwagens zonder checkout | +3 procentpunt (46,5 naar 49,5 %) via schonere cart (gifts als één regel, besparing in dollars, BNPL-regel, geen prijssprong) | $35.000 tot $68.000 |
| 4 | Geen BNPL buiten de VS en geen termijnregel in de winkelwagen | circa 1.900 checkouts per maand boven $349, 26 tot 37 % niet betaald; VS heeft Shop Pay Installments op de PDP, AU/UK/CA/NZ niets; Affirm werkt niet voor CA | Afterpay/Clearpay/Klarna voor niet-US, termijnregel in de cart bij $349+; +5 procentpunt op het niet-US deel en +2 op US | $15.000 tot $30.000 |
| 5 | Europa en andere niet-kernmarkten | IT, DE, NL, CH, FR, SE: circa 35.000 sessies, CR 0,15 tot 0,8 %, 66 % verlaten checkout | CR naar 1,0 % door DDP echt waar te maken en de orderbevestiging te herschrijven, of deze landen uit de advertenties halen | $25.000 tot $50.000 (of evenveel minder verspilde advertentiekosten) |
| 6 | Paid search op blog en content | 24.463 betaalde sessies op blog/content, bounce 64 tot 86 % | naar PDP of een koopbare vergelijkingspagina routeren, +0,5 procentpunt CR | $20.000 tot $40.000 |
| 7 | Post-purchase upsell bereik | Aftersell toont een aanbod bij 2.247 van 5.125 orders (44 %), één funnel, stap 2 vrijwel ongebruikt | tweede funnel voor set- en accessoirekopers, stap 2 vullen | $15.000 tot $25.000 |
| 8 | Kortingslek | $135.511 korting per maand; 99 %- en 100 %-codes actief zonder limiet; 30 %, 25 %, 20 %-codes van oude acties nog open | sluiten, codes uniek en eenmalig | $10.000 tot $20.000 marge, plus het risico dat een 100 %-code rondgaat |

Samengevat: de grootste dollars zitten op de PDP van de Pan Pro (155.268 sessies, één pagina) en in de laatste twee stappen (winkelwagen en checkout). Mobiel en sitesnelheid zijn niet het probleem.

Aanvulling na de visuele controle (7 okt, zie 02): op de PDP zelf staan drie dingen die lek 1 en lek 2 verklaren en die geen test nodig hebben om op te lossen: een countdown die per bezoeker op 02:42 begint, "High demand, few units left" bij meer dan 1.000 op voorraad, en "Delivery from your local warehouse / free express shipping from the US" terwijl pakketten uit China komen. De PDP belooft ook "cook on it for 30 days, full refund", het beleid zegt "used products cannot be returned". Dat is de bron van een deel van de 6 procent refunds en de chargebacks.
