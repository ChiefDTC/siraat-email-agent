# 10 · Technische QA-audit live flows (28 okt 2026, vóór Black Friday)

Alleen gelezen. Niets in Klaviyo of Shopify gewijzigd. Werk van de andere agent (filters en herinstap post-purchase, TP · B2-NOTCLICKED op Manual, vangnetflows `Yfeu2i` en `YhQJdb`, W1-test) staat hieronder als **in uitvoering** en is niet aangeraakt.

## Bereik en werkwijze

- **29 live flows**, 0 op Manual. Daarin 141 send-email-acties (132 live, 9 draft) plus 3 A/B-tests met elk 2 varianten. Alle 150 gekoppelde templates zijn via de API opgehaald.
- **Render**: zelfde route als `scripts/qa_render.py` (Django-engine met `kltags`, `after_render`, `tags_filters`, `mail_checks.preview_problems`). Elke mail is gerenderd op de qa-samples per trigger plus 3 echte recente events per triggermetric, met het bijbehorende profiel. Daarnaast is elke template één keer door `POST /api/template-render` van Klaviyo gehaald.
- **Links**: 91 unieke bestemmingen. Alle siraatskitchen.com-paden (collecties, producten, pagina's, `/discount/...?redirect=`) geven 200. Social, Trustpilot, Snowball en delivery.shopifyapps.com blokkeert de proxy: die zijn met de hand te controleren.
- **Beelden**: 300 unieke beeld-URL's, allemaal 200. Alleen lokale paden uit de testsamples laden niet, en die staan niet in de mails.
- **Producten en codes**: Shopify (alleen lezen). Alle gelinkte producten zijn ACTIVE. Alle 8 coupon-pools die de mails gebruiken (`B2_10_48H`, `C4_10_48H`, `K3_10_48H`, `R2_10_72H`, `R2_VIP_15_72H`, `SK_REGULARS15_14D`, `P3_THANKYOU_10_14D`, `SK_ANNIV15_7D`) bestaan in Shopify, staan op ACTIVE, hebben geen einddatum, zijn eenmalig per klant te gebruiken en mogen combineren met productkortingen. De welkomstcode is actief, maar Shopify staat hem maar één keer per klant toe. Er staan geen codes in dit rapport.
- **Prijzen**: per markt vergeleken met `contextualPricing` in Shopify, voor US, CA, GB, DE, AU, NZ en SG.
- **Deliverability**: `flow-values-report` per bericht, over 14 dagen (14 tot 28 okt) en 3 dagen (25 tot 28 okt).
- **Frequentie**: steekproef van 150 nieuwe aanmelders (lijst `Uw8eZG`, 12 tot 14 okt) en 150 kopers (Placed Order met $value > 0, 12 tot 14 okt). Per profiel zijn de Received Email-events geteld in de eerste 7 en 14 dagen.

## Problemen (blokkerend bovenaan)

| # | Ernst | Flow | Mail (actie-ID) | Wat is er mis | Voorgestelde fix | API of UI |
|---|---|---|---|---|---|---|
| 1 | **blokkerend** | QUBUQV, T4a5Mk, TZG9Mx, VLGhbR, X3ySuU, VTkxFL, UyFc78, XbYT7T | 44 mails met het set-blok of de prijsregels per markt, o.a. C3-S 119850603, C3-P 119850606, W1-B 119850658, W4-US 119850673, W4-INT 119850674, K2-NEW 119850636, A1 119850748, A2 119850750, alle 21 P3-acties 119850558 t/m 119850579, V1 119850713/714, R1 en R2 119850720 t/m 735, N1/N2 119850738/741/742 | **Internationale prijzen zijn verouderd.** `content/catalog/products.json` is van 8 okt; Shopify rekent nu hogere prijzen. 6-delige set: mail £249 / €279 / C$449 / A$449 / NZ$549 / S$409, site £309 / €339 / C$559 / A$559 / NZ$679 / S$509. Verder Standard €139 (site €149), Large €144 (€159) en C$234 (C$239), Small €134 (€139), deksel C$69 (C$79), wok C$174/€109 (C$209/€129), plank £49/€79/C$94 (£59/€89/C$109), pizza, mills en utensils in CA, DE, AU en NZ. W4-INT alleen al ging in 14 dagen naar 2.067 mensen. **US klopt overal** (Mini $99, Small $137, Standard $144, Large $149, set $299, 12-delig $599). | Catalogus opnieuw uit Shopify genereren, `build_template.py` draaien, `qa_render.py` moet groen zijn, `export_klaviyo.py --live` en de flowacties opnieuw koppelen. Of bevestigen dat de nieuwe Shopify-prijzen tijdelijk zijn (Halloween). | API |
| 2 | **blokkerend (vóór 1 nov)** | QUBUQV, TZG9Mx, X3ySuU, UyFc78, XbYT7T, VTkxFL, WdRz5k, QNZyEb, T4a5Mk | Gifts-regel "Your 4 gifts end when the fall sale ends." in C1 119850587, C2 119850597, C2-ACC 119850599, C3-S/P/ACC 119850603/606/613, C4 119850618/621, K1 119850627, K1-ACC 119850628, K2 119850633/636, K3 119850637/642/644/647, B2 119850702/704/706/707/708/709, TP B2 121177244/247/250/251/252/258, P3 nocode en CODE (alle 21), R1/R2 (alle 10), N1/N2, V1. Setblok "FALL SALE · Buy 2, get 4 free", "This month ..." in C3-P 119850606, W1-B 119850658, W4-US 119850673, W4-INT 119850674, A1/A2. | De fall sale stopt op 31 okt, maar de gifts lopen door in de novembersale (DECISIONS 19 okt). Vanaf 1 nov is de urgentieregel dus onwaar en heet het setblok naar een sale die niet meer bestaat. UyFc78 stuurt zijn eerste R1 rond 22 nov, midden in de bevriezing, met deze tekst. | `urgency="1"` uit `gifts5` halen (of een tekst zonder einddatum) en "FALL SALE" en "This month" uit het setblok halen. Daarna herbouwen, QA en export. Open vraag aan Floris: blijft de set $299 in november? | API |
| 3 | hoog | Yp6sKv, TkV5DY | AFF S5 · SALE 121648342, AFF S5 · PAY 121648396 | **Bedrag commissie of uitbetaling rendert leeg** ("Your commission: $ ." en "We just sent you $"). Het testprofiel van Snowball zet `Social Snowball: Payout amount` als tekst ("$19.90"). Daar geeft `floatformat:2` een lege string op, en de valuta komt er dan nog eens voor. Er zijn nog 0 echte referral-sales geweest, dus nog niemand heeft dit gezien. Ook staat "20% of what they pay" in de mail als het profiel nog 20% heeft. | Het bedrag tonen zonder `floatformat` als de waarde al een valutateken heeft (of het `$` wegstrippen), en het else-pad ("shown in your dashboard") laten gelden als de waarde niet numeriek is. Daarna één render op een echt Snowball-event. | API |
| 4 | hoog | T2SmtR (EB Failure to launch) | Titanium vs Non-Stick 90714929, How to Store + Care 108678769, Titanium Vs Stainless Steel 108679684, Micro-Plastic Free 90716322 | Deze 4 mails zijn live, met ongeveer 300 ontvangers per dag per mail. Ze hebben de banner "SIRAAT PRIME TIME SALE · UP TO 56% OFF", de claim "100-DAY TRIAL" (beleid is 30 dagen), "Lifetime" (beleid is 75 jaar) en "100K+". Ze hebben geen vaste header en footer en geen lockup, **geen postadres** in de footer (CAN-SPAM), en Micro-Plastic Free heeft geen UTM. De 6 mails die vandaag naar Draft zijn gegaan, stuurden in de laatste 3 dagen nog 600 tot 1.200 mails elk. | Op Draft zetten tot ze vervangen zijn, of de banner, de trial-regel en de footer met adres vervangen. | API (status), UI (inhoud) |
| 5 | hoog | YyaMjx (FREE E - GUIDE) | E-Guide Flow 106865245 | Gaat 3 minuten na **elke** Placed Order naar de koper, zonder filter (2.873 in 14 dagen). De mail bestaat alleen uit beelden: Prime Time 56%-banner, "45% off ... Cookware Set Pro", geen postadres, geen UTM, smart sending uit. Doet hetzelfde als P1 (e-book, 1 uur later). Afmelding 1,12% (14 dagen) en 1,48% (3 dagen). Downloadlink handmatig te controleren (een andere delivery-URL dan in P1). | Flow op Draft (P1 levert het e-book al), of de mail opnieuw bouwen in de vaste opmaak. | API (status) |
| 6 | hoog | UEfh4h (EB Customer Winback) | Email #1 81010377, #2 81011317, Copy of #2 104289065, #3 81011677 | Live tot 14 dec (besluit Floris), ongeveer 155 mails per dag. Prime Time 56%-banner, "Your 10% Off Ends Tonight" zonder echte deadline, geen postadres, geen vaste header en footer. Oude 50/50-split 81062241 zonder einde. | Banner en "ends tonight" eruit, footer met adres, of stoppen zodra v4 · Winback stuurt (22 nov). Beslissing Floris. | UI |
| 7 | hoog | T4a5Mk (oude welcome-arm) | Old · Welcome 6/7/8 119850678, 119850682, 119850684 | De split staat sinds 19 okt op 100% nieuw, maar wie er eerder in zat, loopt de oude arm nog af: in 3 dagen 81 + 756 + 811 mails. Prime Time 56%-banner, "100-DAY TRIAL", geen postadres. Lost zichzelf op rond 31 okt. | Accepteren, of Old · Welcome 7 en 8 op Manual zetten (de arm blijft dan staan voor een rollback). | API |
| 8 | hoog | QUBUQV | C1 119850587 | Bounce 33,3% over 14 dagen (431 op 1.294, bouncegolf 12 tot 21 okt), in de laatste 3 dagen nog 3,4%. Afmelding 1,62%. | Bounces van de laatste 30 dagen controleren op botdomeinen naast storebotmail; het storebot-filter uitbreiden; hard bounces onderdrukken. | API (filter), UI |
| 9 | hoog | QNZyEb, VLGhbR, T4a5Mk | TP · B1 121177227, A1 119850748, A2 119850750, W1 (A/B 119850659) | Bounce boven 2%: TP · B1 3,18% (14 dagen) en 5,2% (3 dagen), A1 2,47%, A2 2,41% en 4,0% (3 dagen), W1 2,40% en 2,2% (3 dagen). TP en site starten op pixel-events, dus ook op profielen zonder geldige mailbox. | Profielfilter "e-mail niet ongeldig of gebounced", en het filter "test@/storebot" ook in TP, site en welcome. Daarna de bounce per bron (Alia, pixel) bekijken. | API (filter) |
| 10 | hoog | T4a5Mk, QUBUQV, TZG9Mx | W1 (13 klachten), W2 119850663 (11), W3 119850667 (10), C2 119850597, K1 119850627, K2-NEW 119850636 | Spam boven 0,1% over 14 dagen: W1 0,16%, W2 0,19%, W3 0,20%, C2 0,17%, K1 0,11%, K2-NEW 0,13%. Afmelding: C2 2,48%, W1 1,71%, W2 1,73%, W3 1,21%. Voor een nieuwe aanmelder is C2 de derde mail in 26 uur. | C2 naar 48 uur (R4, staat voor 30 okt). Welcome-afmeldingen volgen in de W1-test (in uitvoering). Geen campagnes naar welcome-profielen in dag 0 tot 3. | UI |
| 11 | hoog, **in uitvoering** | QNZyEb | TP · B2-NOTCLICKED 121177242 | Spam 0,44% (2 op 456), boven de Gmail-grens van 0,3%. | Op Manual zetten (R5, gebeurt door de andere agent). | API |
| 12 | hoog, **in uitvoering** | VQ93sx, R22pzb, XzHrez, VPixnJ | P2 119850581, AFF A1 121654816, review 119577631, U1 119850759 | Er komen sinds ~22 okt weinig bezorgevents binnen (Postflows UabgWz, Delivered VcUF33), dus deze flows bereiken bijna niemand. | Vangnetflows `Yfeu2i` (P2) en `YhQJdb` (AFF S1) staan als draft klaar; Postflows herstellen (R1). | UI/API |
| 13 | hoog, **in uitvoering** | X3ySuU | trigger en profielfilter | Geen triggerfilter `$value > 0`, dus ook de $0-orders van TikTok-samples krijgen P1 tot en met P3 (~137 per week). Herinstap staat op 30 dagen. | Triggerfilter `$value > 0` en herinstap naar 7 dagen (05-herinstap-postpurchase.md). | UI |
| 14 | laag | WdRz5k, XzHrez, T4a5Mk | A/B 119850693 (B1, sinds 8 okt), 119577637 (review, sinds 6 okt), 119850659 (W1, **in uitvoering**) | A/B-tests zonder einddatum. Een automatische winnaar staat nergens aan (goed), en de winnaarmaat is unieke klikken. Varianten van W1 en B1 heten nog "Test #1 October 08, 2026 Variation A/B". | Einddatum en besliskader vastleggen (B1 vóór 20 nov dicht, review half januari). | UI |
| 15 | laag | QNZyEb, WdRz5k, UyFc78, X3ySuU, UEfh4h | T02-splits 121177246/249, 119850703/705, 119850729/731, 119850559, plus oude split 81062241 | De T02-splits in browse, TP, winback en post-purchase staan nog op 50/50. Alleen checkout en cart staan op 100% code (besluit 28 okt). Alle oud/nieuw-splits (119850583, 119850622, 119850648, 119850685) staan op 100% nieuw. Geen verdeling die achterloopt. | Bevestigen dat R6 alleen voor checkout en cart gold. Anders ook deze splits naar 100. | API |
| 16 | laag | T4a5Mk, QUBUQV, TZG9Mx, WdRz5k | 17 "Old · ..."-acties (o.a. 119850590 t/m 616, 119850626/632/639, 119850689) | Ze staan live achter een split van 0%, en hebben Prime Time 56%, 100-day trial, "30,000+ Customers" (Old · Browse 1) en geen adres. Old · Welcome 3 119850664 rendert niet in Klaviyo (Django-fout `first_name|default:'there',`). | Laten staan voor een rollback, maar na de bevriezing op Draft. | API |
| 17 | laag | UYALJ8 | Thank you Email 91003608 | Staat op transactional, maar heeft een promotiebanner "SUMMER SALE: UP TO 40% OFF" en de knop "UPGRADE YOUR UTENSILS NOW". Geen vaste header of adres. Lage aantallen. | Banner en promotieknop eruit, of transactional uitzetten. | UI |
| 18 | laag | WsQDYu | BIS 1 112422991, BIS 2 112424186 | Gedachtestreepje in de tekst, en de preheader "You're first in line ... limited restock". Geen vaste header en footer, geen UTM, "Siraat Kitchen". Afmelding 3,6% en 3,9% (n = 85 en 51). | Tekst en opmaak naar de standaard, UTM aanzetten. | UI |
| 19 | laag | UyFc78, XbYT7T | R1 119850720 t/m 723, N1 119850738 | Deze mails bieden de welkomstcode aan kopers aan. In Shopify werkt die maar één keer per klant; ongeveer 2,3% van de orders gebruikte hem, en voor die klanten werkt de code dus niet. | Voor kopers de eigen pool of geen code gebruiken. | API |
| 20 | laag | QUBUQV, T4a5Mk, TZG9Mx, VLGhbR | C3-S, C3-P, W1-B, W4-US, W4-INT, K2-NEW, A1, A2 | De doorgestreepte prijs van de set is $598 en van het 12-delige $1,186, maar de site toont nu $997 en $1,997. $598 is geen bevestigd anker in DECISIONS (alleen $1,186). | Anker laten bevestigen of geen streep tonen. | API |
| 21 | laag | Wn2tsq | Email #2 113594201 | Live op een segment van 41 profielen uit juli, met Prime Time-inhoud. In 14 dagen 0 verstuurd. | Flow op Draft. | API |
| 22 | laag | alle | afzender en reply-to | De afzendernaam verschilt: "Siraat's Kitchen", "Benjamin at Siraat's Kitchen", "Benjamin from Siraat" en "SiraatsKitchen". Op T2SmtR, YyaMjx, WsQDYu, Wn2tsq en UYALJ8 staat geen reply-to. Afzender is overal send@siraatskitchen.com. | Eén afzendernaam per type na het merkbesluit (DECISIONS 15 okt). | UI |
| 23 | laag | YwsKcf | M3 121895224 | "Delivered every month" klopt niet precies: het abonnement in Shopify levert elke 28 dagen. 20% klopt. | Tekst naar "every 4 weeks". | API |
| 24 | laag | alle CODE-mails | 15 acties met `coupon_code` | Die rendert Klaviyo via de API niet zonder profiel ("customer profile is required"); lokaal renderen ze schoon. | Eén preview per pool in de Klaviyo-UI op een echt profiel. | UI |

## Wat in orde is

- **Status**: alle v4-mails staan op de bedoelde status. M4 Mystery staat op draft (bedoeld), de 6 FTL-mails staan sinds vandaag op Draft (bedoeld), Pan Flash Email 1 en Pickup-mail staan op draft. Er staat geen flow op Manual.
- **ID's**: alle 23 metrics in triggers en filters bestaan. De flow-ID's in `$flow`-filters bestaan (Vixr6X en WvRupU staan op draft; dat is bedoeld, zij dienen alleen als dedupe). De triggersegmenten WuHSm6 (83.373 profielen), YxfuJT en YbCB68 en lijst Uw8eZG bestaan. Er zijn geen filters op lijst- of segmentlidmaatschap met verwijderde ID's. Mystery-trigger ProductID 15785445622100 is ACTIVE. De Items-namen in de filters dekken alle verkochte pannen, sets, deksels en schorten van de laatste 14 dagen.
- **Timing**: alle wachttijden gebruiken de tijdzone van het profiel. De volgorde klopt met v4-flow-system.md. Bekend en gepland: C2 na 1 dag (R4), de eerste winback-mail rond 22 nov, VIP vanaf ~7 nov en de review-vangnetgolf rond 14 nov.
- **Instellingen**: smart sending staat uit in v4, zoals bedoeld (v4-flow-system.md). Het staat aan in affiliate, Mystery en FTL. Transactional staat alleen aan op UYALJ8. UTM staat aan op elke v4-, affiliate- en Mystery-mail, met `utm_campaign` per flow.
- **Render**: alle v4-, affiliate-, Mystery- en reviewmails renderen zonder restanten van `{% %}` of `{{ }}`, zonder "None" en zonder $0. Elke mail heeft een preheader met minstens 300 opvulposities en een afmeldlink. Uitzonderingen staan in punt 3 en 16.
- **Merk**: elke v4-mail heeft de vaste header-lockup en footer-lockup (geplatte CDN-versies). Affiliate heeft geen logo en Mystery geen header; beide zijn toegestane uitzonderingen. XzHrez en TvfJYU hebben de witte lockup in de hero (uitzondering van 12 okt). Overal staan Benjamin, 30-day returns, de 75-year warranty (N1 en N2: "74 years left") en 100,000+. "30,000" komt alleen in Old · Browse 1 voor. Er staat geen Halloween en geen oktoberdatum in de copy. De oktoberdatums in de CODE-mails zijn dynamisch (vandaag + 48 of 72 uur).
- **US-prijzen** kloppen met Shopify, ook in de sale.

## Dekking en frequentie

| Groep (steekproef 150) | Mails in de eerste 7 dagen | Mails in de eerste 14 dagen | Uit 3 of meer flows in 14 dagen |
|---|---|---|---|
| Nieuwe aanmelder | gem. 5,3 (flows 3,6, campagnes 1,7), mediaan 6, p90 8, max 11 | gem. 8,1 (flows 4,8, campagnes 3,3), mediaan 9, p90 12, max 15 | 8% (in 7 dagen 6%) |
| Koper | gem. 2,0 (alleen flows, 0 campagnes), p90 3, max 7 | gem. 4,1 (flows 2,3, campagnes 1,8), p90 6, max 12 | 22% (in 7 dagen 13%) |

- Bij nieuwe aanmelders komt het meeste uit welcome (T4a5Mk), daarna cart, checkout en post-purchase.
- Bij kopers komt het meeste uit P1 (X3ySuU) en de E-Guide-flow (YyaMjx), die vrijwel altijd allebei binnen een uur na de order komen. Daarna browse (WdRz5k, na de aankoop), P2 en U1.
- De kopers in de steekproef bestelden vóór 23 okt. Sinds 23 okt komt Mystery M1 erbij op dag 3. Een koper zit nu dus standaard in 4 flows in de eerste 2 weken: P1, E-Guide, Mystery en P2 of P2-SAFE, plus U1 en review.
- Met punt 5 (E-Guide uit) gaat er per koper één mail af.

## Deliverability (14 dagen, alles boven de grens)

Grenzen: bounce > 2%, spam > 0,1%, afmelding > 1%. n = ontvangers. Mails met minder dan 50 ontvangers zijn weggelaten.

| Flow | Mail (actie-ID) | n | Bounce | Spam | Afmelding |
|---|---|---|---|---|---|
| QUBUQV | C1 119850587 | 1.294 | **33,31%** | 0 | **1,62%** |
| QUBUQV | Old · Checkout 1 119850590 | 52 | **44,23%** | 0 | **6,90%** |
| QUBUQV | C2 119850597 | 609 | 0,82% | **0,166%** | **2,48%** |
| QUBUQV | C2-ACC 119850599 | 85 | 0 | 0 | **1,18%** |
| QUBUQV | C3-S 119850603 / C3-P 119850606 | 169 / 323 | 0,59 / 0,31% | 0 | **1,19 / 1,24%** |
| QUBUQV | CODE · C4 119850620 | 308 | 0,65% | **0,327%** (1) | 0,98% |
| QUBUQV | Old · Checkout 4 / 5 | 62 / 88 | 1,61 / 1,14% | 0 | **1,64 / 1,15%** |
| QNZyEb | TP · B1 121177227 | 629 | **3,18%** | 0 | 0,16% |
| QNZyEb | TP · B2-NOTCLICKED 121177242 | 456 | 1,32% | **0,444%** | 0,67% |
| T4a5Mk | W1 (A/B 119850659) | 8.252 | **2,40%** | **0,161%** | **1,71%** |
| T4a5Mk | W2 119850663 | 6.012 | 0,95% | **0,185%** | **1,73%** |
| T4a5Mk | W3 119850667 | 5.188 | 1,10% | **0,195%** | **1,21%** |
| T4a5Mk | W0 119850655 | 54 | 0 | 0 | **1,85%** |
| T4a5Mk | Old · Welcome 1 119850652 | 1.526 | **2,82%** | **0,472%** | **3,10%** |
| T4a5Mk | Old · Welcome 2 / 4 / 5 | 1.593 / 981 / 1.021 | 0,75 / 0 / 0% | **0,316 / 0,306%** / 0,098% | **1,58 / 2,14 / 1,18%** |
| TZG9Mx | K1 119850627 | 1.821 | 0,93% | **0,111%** | 0,72% |
| TZG9Mx | K1-ACC 119850628 | 171 | 0,58% | 0 | **2,94%** |
| TZG9Mx | K2-NEW 119850636 | 1.519 | 0,79% | **0,133%** | 0,86% |
| TZG9Mx | CODE · K3 · acc 119850641 / nocode 119850642 | 70 / 74 | 0 / 1,35% | 0 | **2,86 / 1,37%** |
| TZG9Mx | CODE · K3 · pan 119850646 / nocode 119850647 | 734 / 693 | 1,23 / 0,58% | 0 | **1,10 / 1,16%** |
| TZG9Mx | Old · Cart 1 / 2 | 70 / 78 | 0 | 0 | **1,43 / 5,13%** |
| VLGhbR | A1 119850748 / A2 119850750 | 688 / 581 | **2,47 / 2,41%** | 0 | 0,75 / 0,88% |
| WdRz5k | B1-ACC 119850694 | 504 | 0,60% | 0 | **1,20%** |
| WdRz5k | Old · Browse 1 119850689 | 113 | 0,88% | 0 | **2,68%** |
| WsQDYu | BIS 1 112422991 / BIS 2 112424186 | 85 / 51 | 1,18 / 0% | 0 | **3,57 / 3,92%** |
| YwsKcf | M1 121895219 | 323 | 0,31% | **0,311%** (1) | 0,62% |
| YyaMjx | E-Guide Flow 106865245 | 2.873 | 0,87% | 0,070% | **1,12%** |

In de laatste 3 dagen liggen boven 2% bounce: TP · B1 (5,2%), A2 (4,0%), C1 (3,4%), B1-ACC (3,2%), TP · B2-NOTCLICKED (2,5%), W1 (2,2%) en CODE · K3 · pan (2,1%). Spamklachten in 3 dagen: W3 4, W1 3, W4-US 2, en C2, K1, M1, S2 en FTL Review Focus elk 1.

## Bronnen

Werkbestanden staan in de scratchpad `audit/` en niet in git: definities, templates, renders, events en rapporten.
