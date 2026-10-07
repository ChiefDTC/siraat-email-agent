# Flow-systeem v3 · nieuwe flows

Versie 7 oktober 2026. Aanvulling op `klaviyo/flows/v3-flow-system.md` (6 herbouwde flows). Niets is in Klaviyo of Shopify aangemaakt; dit is ontwerp plus bron-HTML.
Mails: `klaviyo/templates/v3/{sunset,site,vip,anniversary,ugc}/` (bron, `-preview.html`, `previews/` desktop 700 en mobiel 390, `assets/`, `assets/src/` met kopieën van de bronfoto's). Hero-registers: `content/media/hero-register/{sunset,site,vip,anniversary,ugc}.csv`.

## 1. Wat er al bestaat (Klaviyo, GET /api/flows, 70 flows, 7 okt)

| Kandidaat | Bestaat al? | Cijfers 90 dagen | Besluit |
| --- | --- | --- | --- |
| Sunset / re-permission | Ja: S7V4a7 live (segment XY4NVp, 17.367 profielen), plus draft WPfe5T (Farooq) | 25.530 mails, open 10,3%, klik 0,41%, $304, uitschrijf 0,54% | **Herbouwen** (flow 2 hieronder). Huidige flow doet niets meetbaars en heeft geen duidelijke uitkomst. |
| Back in stock | Ja: WsQDYu live | 349 mails, $2.861, $8,20 per ontvanger (beste RPR van het account) | Niet dubbel bouwen. Werkt; volume is klein. Alleen het v3-jasje geven als er tijd over is. |
| Replenishment vaatwasstrips | Deels: WvRupU "Mystery Gift Reveal, Sheets" live voor gift-ontvangers zonder Recharge-abonnement (4 mails) | WvRupU: 19.190 mails, $4.293. Betaalde strip-orders: 156 in 90 dagen ($2.814 netto, Shopify) | Niet bouwen. Te klein volume voor een eigen flow; gift-ontvangers zijn al gedekt. Wel: WvRupU later naar v3-stijl (backlog 6). |
| Review-verzoek | Ja: XzHrez live (blijft) | Basislijn 3,3% klik | Blijft. UGC-fotoverzoek wordt een eigen, eerdere stap (flow 5). |
| Cross-sell 2e product (deksel bij pan) | Ja: P3 in Post-purchase v3 (dag 14, deksel/board/set met THX-code) | Deksel: 3.085 orders tegen ruim 17.000 pan-orders in 90 dagen | Niet dubbel. VIP en Anniversary tonen de deksel opnieuw op dag 30+ en dag 182. |
| VIP na 2e order | Nee | ~750 terugkerende klanten per maand (Shopify) | **Bouwen** (flow 3). |
| Birthday / anniversary | Nee (geen geboortedatum bekend; eerste-order-datum wel) | ~5.500 nieuwe klanten per maand | **Bouwen** als order-anniversary (flow 4). |
| Site abandonment | Alleen draft UEqeEm (Farooq, 2024) | Active on Site ~8.000 uniek per week, Viewed Product ~6.100 | **Bouwen** (flow 1). |
| UGC / "first egg" | Nee | 275 bruikbare reviews, bijna geen foto's | **Bouwen** (flow 5). |
| Price drop | Nee | Prijzen veranderen niet op productniveau (altijd-aan sale, acties via aparte UNLISTED-producten) | Niet bouwen: de trigger zou bijna nooit vuren. |
| Post-purchase cadeaukopers | Alleen UYALJ8 voor E-Gift Card (3 mails in 90 dagen) | Geen betrouwbaar gift-veld in Placed Order | Niet nu. Na Q4 opnieuw bekijken als Shopify een "this is a gift"-veld krijgt. |

## 2. Data waarop de keuze rust

- Shopify (ShopifyQL, 6 maanden): 4.900 tot 7.600 klanten per maand, waarvan 11 tot 17 procent terugkerend; AOV $209 tot $222. De tweede order is de grootste onbenutte hefboom.
- Klaviyo: Email List Uw8eZG 214.438 profielen; "Engaged 90 Days" 89.742; "Unengaged 180 Days, Non-Buyers" 20.062; Sunset Segment 17.367. Uitschrijvingen gemiddeld 1.960 per week, spam 84 per week (0,042%). Campagnes 90 dagen: 3,55 miljoen mails, $305k.
- Active on Site (UdCdLD): 7.100 tot 8.800 unieke profielen per week; Viewed Product (XNtYMB): 5.300 tot 6.700. Het verschil plus mensen die alleen collecties of de homepage zien is de site-abandonment-doelgroep.
- Shopify 90 dagen: Pan Pro Standard 6.180 orders, Large 5.142, Small 2.736, Mini 1.367; deksel 3.085 + 323 (S). Snijplank 1.552.
- Email Love (8 zoekopdrachten): Brooklinen "Baby come back" (winback met donkere lifestyle-hero), philosophy verjaardag als uitnodiging (exclusiviteit), Ripple "V.I.Pea's only" (VIP-korting in onderwerp), Estée Lauder "choose your gift" (gift boven korting), BARK en Jetboil (reviews en klantfoto's als hoofdinhoud). Overgenomen: mijlpaal als aanleiding, VIP-code persoonlijk en met looptijd, klantfoto's als proof.

## 3. Prioriteit en plaats tegenover de bestaande flows

Volgorde op verwachte omzet (zie 9): 1 Site abandonment, 2 Sunset, 3 Order anniversary, 4 VIP, 5 UGC first egg. Bouwvolgorde advies: Sunset eerst (klein, beschermt alle campagne-omzet), dan Site, VIP, Anniversary, UGC.

Plaats in de prioriteitslijst van v3-flow-system.md (verkoop-flows, iemand zit nooit in twee tegelijk):

1. Post-purchase v3
2. Checkout v3
3. Cart v3
4. Browse v3
5. Welcome v3
6. Winback v3
7. **Site abandonment (nieuw)**: alleen als er geen product bekeken is en niemand in 1 tot 6 zit.

Klant- en onderhoudsflows (geen verkoopconcurrent, wel afstand):
- **UGC first egg**: na P2 (levering +1), vóór review XzHrez (levering +14). Alleen eerste orders.
- **VIP**: start pas 30 dagen na de 2e order, dus na het P3-codevenster (dag 14 tot 28) en vóór Winback R1 (dag 60).
- **Anniversary**: dag 182 en 365, ruim na Winback R2 (dag 90). Overslaan als er in 14 dagen een VIP- of Winback-mail was.
- **Sunset**: laatste vangnet; filter sluit iedereen uit die in 30 dagen in Welcome of Post-purchase zat of in 180 dagen kocht.

Codes: alle nieuwe codes volgen de discount ladder uit research/ux-2026-10-07/04-offer-strategy.md (cooldown 30 dagen via `last_flow_code_at`, 15% alleen voor VIP).

## 4. Flow 1 · Site abandonment (nieuw) · map `site/`

- **Doel**: bekende bezoekers die de site zien maar geen product openen (vaak de vraag "welke maat?") naar een product en een eerste order brengen.
- **Trigger**: Active on Site (UdCdLD, API). Let op: TF6iAL heeft dezelfde naam maar geen events.
- **Flow-filters**: kan e-mailmarketing ontvangen; Viewed Product, Added to Cart, Checkout Started en Placed Order = 0 sinds flow-start; Placed Order = 0 in de laatste 30 dagen (sluit klanten uit die hun bestelling volgen); niet in Browse, Cart, Checkout of Post-purchase v3 in 7 dagen; niet in Welcome v3 in 10 dagen; niet in deze flow in 14 dagen.
- **Herinstap**: na 14 dagen.

| Stap | Wachttijd | Mail | Filter en exit |
| --- | --- | --- | --- |
| 0 | 2 uur | A1 Which pan is yours? (maatkeuze Mini/Small/Standard/Large, HI10, gifts) | Zelfde "sinds flow-start"-filters bij verzenden. Exit: wie een product bekijkt gaat naar Browse v3. |
| 1 | 2 dagen, 10:00 | A2 Where 100,000+ people started (bestsellers met prijs na HI10) | Idem. |
| 2 | einde | | |

- **Aanbod**: HI10 (publiek, trede 2 zonder deadline), gifts. Geen unieke code: lage intentie, dus geen "leren afhaken".
- **A/B**: A1 onderwerp "Not sure which pan? Start here." tegen "The question we get most: which size?".

## 5. Flow 2 · Sunset en re-permission (vervangt S7V4a7) · map `sunset/`

- **Doel**: deliverability. Inactieve profielen laten kiezen; wie niet reageert, uit de verzendingen. Beschermt de inbox-plaatsing van $305k campagne-omzet per 90 dagen en verlaagt Klaviyo-kosten.
- **Trigger**: nieuw segment "Sunset v3 · unengaged 120d": kan e-mailmarketing ontvangen; profiel ouder dan 120 dagen; Clicked Email (Bot Click = false) = 0 in 120 dagen; Active on Site = 0 in 120 dagen; Placed Order = 0 in 180 dagen; Received Email >= 8 in 120 dagen (wie weinig mail kreeg is niet inactief maar onbereikt). Opens tellen niet mee als bewijs van activiteit (Apple Mail Privacy).
- **Flow-filters**: niet in deze flow in 180 dagen; niet in Welcome v3 of Post-purchase v3 in 30 dagen.

| Stap | Wachttijd | Mail | Filter en exit |
| --- | --- | --- | --- |
| 0 | direct, 10:00 | S1 Still want to hear from us? (knop "Yes, keep me on the list", plus minder mails en uitschrijven) | |
| 1 | 4 dagen | S2 Last email from me (tekst, Benjamin) | Clicked Email, Active on Site en Placed Order = 0 sinds flow-start |
| 2 | 3 dagen | Split: Clicked Email > 0 of Active on Site > 0 of Placed Order > 0 sinds flow-start | Ja: update `sunset_status = kept`, einde. Nee: update `sunset_status = suppressed`, `sunset_at = vandaag`. |

- **Uitvoering suppressie**: Klaviyo-flows kunnen niet zelf onderdrukken. Segment `sunset_status = suppressed` wekelijks bulk-suppressen (of uitsluiten van alle campagnes en flows tot een nieuwe opt-in). Kopers blijven transactionele mails krijgen.
- **Exit**: elke klik of sitebezoek haalt iemand eruit.
- **A/B**: geen in de eerste maand; meet hoeveel procent "kept" wordt.

## 6. Flow 3 · VIP na de tweede order (nieuw) · map `vip/`

- **Doel**: van 2 naar 3 orders. Erkenning plus een persoonlijke 15%-code, en een vraag die feedback oplevert.
- **Trigger**: Placed Order. **Flow-filter**: Placed Order count over all time = 2 (het tellende event is de 2e order); nooit eerder in deze flow; kan e-mailmarketing ontvangen.

| Stap | Wachttijd | Mail | Filter en acties |
| --- | --- | --- | --- |
| 0 | 30 dagen, 10:00 | V1 Twice is a habit (unieke 15%-code, 14 dagen) | Refunded Order = 0 sinds start; Placed Order = 0 in 14 dagen; `last_flow_code_at` niet in 30 dagen (anders variant zonder code: zelfde mail met HI10). Daarna: update `last_flow_code_at`, `last_flow_code_pool = SK_REGULARS15_14D`, `siraat_regular = true`. |
| 1 | 10 dagen, 10:00 | V2 A question from Benjamin (tekst: wat moeten we maken, P.S. code nog een paar dagen geldig) | Placed Order = 0 sinds start. Geen tweede coupon-tag (die zou een nieuwe code maken). |
| 2 | einde | | Winback v3 neemt over op dag 60 (R2-VIP 15% op dag 90, ruim 30 dagen na V1). |

- **Exit**: Placed Order sinds flow-start stopt V2.
- **A/B**: V1 met code tegen V1 met HI10 (holdout 20%), winnaar op omzet per ontvanger na kortingskosten.

## 7. Flow 4 · Order anniversary (nieuw) · map `anniversary/`

- **Doel**: eenmalige kopers na het winbackvenster terugbrengen met een echte aanleiding (6 en 12 maanden), service eerst.
- **Trigger**: Placed Order. **Flow-filter**: Placed Order count over all time = 1 (eerste order); nooit eerder in deze flow.

| Stap | Wachttijd | Mail | Filter |
| --- | --- | --- | --- |
| 0 | 182 dagen, 10:00 | N1 Six months on titanium (patina, sticking, garantie; producten met HI10, geen codebalk) | Refunded Order = 0 sinds start; geen VIP- of Winback-mail in 14 dagen; Opened Ticket (Gorgias) = 0 in 14 dagen |
| 1 | 183 dagen, 10:00 | N2 One year ago this week (unieke 10%-code, 7 dagen) | Refunded Order = 0 sinds start; Placed Order = 0 in 14 dagen; `last_flow_code_at` niet in 30 dagen (anders variant zonder code). Daarna update `last_flow_code_at`. |

- **Let op**: de flow loopt alleen voor orders ná livegang. Klanten van oktober 2025 en later krijgen hun jaarmail pas als er een eenmalige backfill komt: segment "eerste order 360 tot 367 dagen geleden" met een kopie van N2 als wekelijkse campagne tot de flow zelf instroom heeft. Controleer of Klaviyo een vertraging van 182 dagen in één stap accepteert; zo niet, opdelen in stappen van 91 dagen.
- **Herhaalklanten**: wie inmiddels 2+ orders heeft krijgt N2 gewoon (het blijft hun eerste-order-jubileum); de cooldown voorkomt een code vlak na V1.

## 8. Flow 5 · UGC "first egg" met incentive (nieuw) · map `ugc/`

- **Doel**: klantfoto's van echte keukens (voor ads, reviews en mails; DECISIONS 7 okt: UGC mag gebruikt worden) en een kleine tweede-order-trigger. Haalt ook vroeg sticking-problemen op voordat ze een 1-sterreview worden.
- **Trigger**: Delivered Shipment (VcUF33). **Flow-filters**: Placed Order count all time = 1; nooit eerder in deze flow; dezelfde backorder-uitsluiting op producttitels als XzHrez.

| Stap | Wachttijd | Mail | Filter |
| --- | --- | --- | --- |
| 0 | 6 dagen, 10:00 | U1 Show us your first egg (reply met foto, 15% op de volgende order) | Opened Ticket (Gorgias) = 0 sinds start; Refunded Order = 0 in 30 dagen; Fulfilled Order >= 1 in 60 dagen |

- **Incentive-afhandeling**: reply-to support@siraatskitchen.com (Gorgias). Gorgias-regel: e-mail met bijlage en onderwerp/thread "My first egg" krijgt tag `ugc-photo`; macro stuurt een unieke 15%-code uit een Shopify bulk-pool `UGC15-` (1 gebruik, 60 dagen) en bedankt. Toestemming staat in de mail (voornaam, site, mails, Instagram; "private" = alleen code). Floris accepteert het incentive-risico (DECISIONS); in copy nooit "unsolicited" of "independent".
- **Exit**: Opened Ticket sinds start (iemand die al een probleem meldt, krijgt geen fotoverzoek).
- **Later**: als het werkt een tweede stap voor de 5-sterren-klikkers uit XzHrez (Clicked Email met URL bevat trustpilot) met hetzelfde verzoek.

## 9. Verwachte impact (aannames expliciet, per maand)

| Flow | Instroom | Mails | Aanname omzet per ontvanger | Verwachte omzet | Overige waarde |
| --- | --- | --- | --- | --- | --- |
| 1 Site abandonment | 4.000 tot 6.000 (uitgaande van 35% van Active on Site zonder productview, na filters op klanten, welcome en andere flows) | ~1,8 per persoon | $0,30 tot $0,50 (helft van Browse $0,97: lagere intentie) | **$2.200 tot $5.400** | |
| 2 Sunset | eerste golf 17.000 tot 20.000, daarna 2.000 tot 4.000 | 1,6 | ~$0,01 direct | ~$300 direct | 2 tot 5% betere inbox-plaatsing op ~$100k campagne-omzet per maand = **$2.000 tot $5.000**; minder actieve profielen in Klaviyo-pakket |
| 3 VIP | 450 tot 600 (2e orders per maand, ~70% met consent) | 1,8 | $1,50 tot $2,50 (herhaalkopers converteren hoger; R2-VIP-equivalent) | **$1.200 tot $2.700** | hogere kans op order 3 en feedback via V2 |
| 4 Anniversary | 3.500 tot 4.500 per mijlpaal (5.500 nieuwe klanten, consent en bereik ~70%) | 2 mijlpalen | N1 $0,15 tot $0,25; N2 $0,25 tot $0,40 | **$1.400 tot $2.900** (na volle aanloop, N2 pas na 12 maanden of met backfill) | service en garantie-uitleg, minder 1-sterreviews |
| 5 UGC first egg | 3.500 tot 4.500 eerste-order-leveringen | 1 | $0,05 tot $0,10 | $200 tot $450 | 50 tot 130 klantfoto's per maand bij 1,5 tot 3% reply; vroege opvang van sticking-klachten |

Kosten: VIP-code 15% en Anniversary-code 10% alleen op de geconverteerde orders; UGC-code 15% op ~30% van de fotosturers. Elke code-mail krijgt een holdout zoals in 04-offer-strategy.md.

## 10. Nieuwe coupons (aan te maken in Klaviyo > Coupons, Shopify unique)

| Pool | Prefix | Korting | Geldig | Instellingen | Gebruikt in |
| --- | --- | --- | --- | --- | --- |
| SK_REGULARS15_14D | REG- | 15% | 14 dagen na toewijzing | 1 gebruik, 1 per klant, alleen one-time purchase products | V1 |
| SK_ANNIV10_7D | YEAR- | 10% | 7 dagen na toewijzing | idem | N2 |
| UGC15 (Shopify bulk, niet Klaviyo) | UGC15- | 15% | 60 dagen | 1 gebruik, 1 per klant; uitgegeven door Gorgias-macro | U1 (na foto) |

In templates alleen `{% coupon_code 'SK_REGULARS15_14D' %}` en `{% coupon_code 'SK_ANNIV10_7D' %}`, steeds dezelfde tag in codebalk, aanbodblok en links.

## 11. Mails (bron, previews, beelden)

| Flow | Mail | Onderwerp A / B | Hero (bron) | Codebalk |
| --- | --- | --- | --- | --- |
| Site | a1 | Not sure which pan? Start here. / The question we get most: which size? | omelet (gempages d2a399da), 4:3, HI10-balk | HI10 |
| Site | a2 | Where 100,000+ people started / The pan most kitchens start with | sliding_eggs, 4:3, HI10-balk | HI10 |
| Sunset | s1 | Should we keep writing to you? / Still want our emails? One tap. | crepepanwebp, 4:3, geen balk | nee |
| Sunset | s2 | Last email from me (unless you tap) / Should I stop writing? | tekstmail | nee |
| VIP | v1 | Twice is a habit. Here's 15% off. / For our regulars: 15% off your next piece | siraatsignatureapronoak, 1:1, codebalk | REG-code |
| VIP | v2 | A question from Benjamin / What should we make next? | tekstmail | nee |
| Anniversary | n1 | Six months on titanium: a quick check / Half a year with your pan. Three things worth knowing. | Salmon_in_pan, 1:1, geen balk | nee (service) |
| Anniversary | n2 | One year ago this week / Happy first year. Here's 10% off. | IMG_6175 (uitsnede), 1:1, codebalk | YEAR-code |
| UGC | u1 | Show us your first egg? / Reply with a photo, get 15% off | Lifestyle_image_egg_1 (uitsnede zonder mok), 1:1, incentive-balk | nee |

Alle hero's zijn nieuw (niet in eerdere registers). Productbeelden zijn kopieën uit winback/post-purchase assets. Maatkaarten in A1: kopieën van 26CM-eggs en 28CM-egs (vier en vijf eieren, uit de Shopify-alt-tekst).

## 12. Open punten voor Floris / volgende sessie

1. Hero's en productbeelden uploaden naar de Klaviyo-bibliotheek en `assets/klaviyo-urls.txt` per map vullen; pas dan schrijft build_template.py de `.klaviyo.html`.
2. Segment "Sunset v3 · unengaged 120d" aanmaken en S7V4a7 volgens PLAYBOOK 7 uitfaseren.
3. Gorgias-regel en macro voor UGC (tag `ugc-photo`, code uit UGC15-pool) en een plek om foto's met toestemming te bewaren.
4. 6-delige set: products.csv toont het actieve product op $399, de $349-versie is UNLISTED. V1, A2 en N2 linken naar het actieve product en rekenen met $349 (DECISIONS). Rechttrekken vóór livegang, net als bij C3-P en W4.
5. Anniversary backfill (zie 7) en controle van de maximale wachttijd per stap.
6. "MOST ADDED" bij de deksel in N1 rust op Shopify 90 dagen (deksel is het meest verkochte niet-pan-product, 3.085 orders). Hercontroleren per kwartaal.
