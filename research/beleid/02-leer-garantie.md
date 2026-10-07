# 02 · Leer-garantie: drie varianten van risico-omkering, met cijfers

Datum: 7 oktober 2026. Opties voor Floris, geen besluit. Bronnen: `01-inventaris.md`, `inventaris.csv`, Gorgias analytics (180 dagen), research/deep/01 t/m 04, content/reviews. Alle bedragen per maand, USD, op basis van september 2026.

## 1. Uitgangspunt

**Het probleem in één zin.** Een titanium pan is een ervaringsgoed: je weet pas of hij bij jou plakt als je erop kookt, en zodra je erop gekookt hebt mag hij volgens het beleid niet meer terug. Dat is het zwaarste risicosignaal dat er is (verliesaversie plus spijtaversie, zie deep/01 rij 2 en 7).

**De huidige situatie is niet "streng beleid", maar twee beleidslijnen tegelijk.** De PDP's beloven sinds de thema-update: *"Cook on your pan at home for 30 days, and if it isn't the best pan you've owned, return it for a full refund."* Service weigert gebruikte pannen. Klanten krijgen dus de belofte van variant (c) en de uitvoering van variant (a). Elke keuze hieronder is beter dan dat, ook de strengste.

**Basiscijfers**

| Meting | Waarde | Bron |
|---|---|---|
| Bruto-omzet per maand | circa $1,35 mln ($74.000 retour = 5,5%) | deep/02, deep/04 |
| Orders per maand | circa 5.100 (september) | deep/04 |
| Gemiddelde bruto orderwaarde | circa $264 | afgeleid |
| Retour nu | 5,5% van bruto-omzet ($74.000); april 3,4% | ShopifyQL via deep/04 |
| Conversie per bezoeker | 1,64%; circa 311.000 bezoekers per maand | Intelligems via deep/04 |
| Tickets over plakken | 893 in 180 dagen (circa 150 per maand, circa 120 klanten) | Gorgias, 01 |
| Conflict belofte tegen beleid | 519 tickets in 180 dagen (17% van retour/refund/garantie) | Gorgias, 01 |
| Lage Trustpilot-reviews over retour/trial | 97 tot 100 van 154; 47 "scam" | content/reviews |

**Aanname die Floris moet bevestigen:** contributiemarge per extra order 65% van de orderwaarde (na inkoop en verzending, vóór marketing), dus circa $172 per extra order. Alle break-evens hieronder hangen hieraan. Andere aannames staan per variant en in paragraaf 6.

**Wat de meta-analyse zegt (Janakiraman, Syrdal en Freling, 2016, Journal of Retailing).** Een meta-analyse over vijf dimensies van soepel retourbeleid: tijd, geld, moeite, reikwijdte (wat mag terug) en ruil. Hoofdbevinding: soepeler beleid verhoogt aankopen gemiddeld sterker dan retouren. Per dimensie, zoals ik de samenvatting lees: soepelheid in geld en moeite verhoogt vooral aankopen; een langere termijn verhoogt retouren nauwelijks of verlaagt ze zelfs (wie een product langer heeft, gaat eraan hechten); soepelheid in reikwijdte (bijvoorbeeld gebruikte producten) verhoogt retouren het meest. Effectgroottes uit de studie neem ik niet over: ze komen uit andere categorieën en zijn niet een-op-een te vertalen naar een pan van $134. De studie geeft de richting, de eigen cijfers geven de orde van grootte, en alleen een test geeft het antwoord.

**Eigen aanwijzingen dat risico-omkering bij Siraat verkoopt**

- Ad "Try it risk free for 100 days": ROAS 2,49 op $11.323, tweede beste boven $10.000 spend (content/hooks).
- Oude checkoutmail zonder korting maar met zekerheid: $7,86 per ontvanger, tegenover $0,79 voor de cartmail met 10% korting (deep/01).
- Pre-sale vragen gaan over twijfel aan het product (materiaal 160, plakken 51), niet over prijs (deep/04).
- Vergelijkers (8,4% van orders, AOV $291) lezen Trustpilot; daar is retour het grootste klachtthema.

## 2. Variant (a): huidig beleid, helder en positief

**Wat het is.** Niets aan het beleid veranderen, wel overal hetzelfde zeggen: ongebruikt binnen 30 dagen terug voor een volledige refund; gebruikt alleen bij een defect via de 75-year warranty; plakken krijgt gratis coaching, geen refund. Alle PDP-blokken "Risk-free purchase ... return it for a full refund" eruit. Floris kiest één ding: retourlabel voor ongebruikte producten gratis of op kosten van de klant.

**Kernformulering (Engels, max. 40 woorden)**

> Not for you? Return it unused within 30 days of delivery for a full refund, return label included. Every Siraat pan carries a 75-year warranty against defects like a warped base or a loose handle.

(35 woorden. Als de klant de retour betaalt: "...for a full refund. Return shipping is on you." De rest gelijk.)

**Verwachte conversiewinst.** Ten opzichte van een eerlijke basis: 0 tot +2% relatief, via minder "scam"-reviews en minder conflicttickets. Ten opzichte van de site vandaag (die "risk-free" belooft): mogelijk 0 tot -2%, omdat een sterke belofte verdwijnt. Eerlijk gezegd: (a) is geen groeimaatregel, het is het dichten van een lek in vertrouwen en een juridisch risico.

**Extra retourkosten.** Bij betaald label: $0. Bij gratis label: circa 94 ongebruikte retouren per maand (561 tickets in 180 dagen noemen "unused") maal circa $20 = **circa $1.900 per maand (0,14% van bruto-omzet)**. Retourpercentage blijft rond 5,5%.

**Misbruikrisico.** Laag. Ongebruikt is controleerbaar met de foto's die het portaal al vraagt.

**Wat het oplevert naast conversie.** Minder van de 519 conflicttickets per half jaar (circa 85 per maand), minder lage reviews over retour (circa 16 per maand), en geen PDP-belofte meer die service niet nakomt.

**Testopzet.** Geen conversietest nodig: de PDP-belofte moet hoe dan ook gelijk met het beleid. Meten vóór en na: conflicttickets per 1.000 orders, lage Trustpilot-reviews over retour per maand, retour als % van bruto-omzet. Wel een A/B binnen (a) mogelijk: "return label included" tegen zonder, als Floris twijfelt over gratis labels (Intelligems content-test op PDP en cart, 6 weken).

**Service-macro (a): gebruikte pan, plakt, wil geld terug**

> Hi {{ticket.customer.firstname}},
>
> I'm sorry the pan isn't working for you yet. That is not how cooking on it should feel, and I'd like to fix it with you.
>
> There is no coating on a Siraat pan, so the release comes from heat, not from a layer. Three things solve almost every case:
> 1. Preheat on medium for 2 to 3 minutes. Never high.
> 2. Water test: a drop should roll around like a bead. If it vanishes at once, the pan is too hot.
> 3. Add a teaspoon of oil, wait 10 seconds, then add food and let it release on its own before you move it.
>
> Here is the 2-minute video: https://siraatskitchen.com/pages/care-use
>
> Could you try this a few times this week and tell me how it goes? A short video of your water test helps me spot what is happening.
>
> About returns, so you know where you stand: unused products can come back within 30 days of delivery for a full refund. A pan that has been cooked on can't be refunded, but it stays covered by our 75-year warranty against defects such as a warped base or a loose handle.
>
> Talk soon,
> {{current_user.firstname}}, Siraat's Kitchen

## 3. Variant (b): "Learn it in 30 days"

**Wat het is.** Gebruik is toegestaan. Wie binnen 30 dagen na bezorging meldt dat de pan blijft plakken terwijl hij de care-gids volgt, krijgt eerst persoonlijke coaching. Lost dat het niet op, dan kiest de klant: vervanging door een ander Siraat-product van gelijke waarde, of refund van die pan (Siraat betaalt het retourlabel). Ongebruikt retour zoals in (a).

**Voorwaarden (voorstel, Floris beslist)**

- Melding binnen 30 dagen na bezorging (Shopify-fulfilment of trackingdatum).
- Stap 1, coaching: klant stuurt een korte video of foto's van voorverwarmen en de watertest. Support antwoordt binnen een werkdag met concrete tips. Klant probeert minimaal 7 dagen.
- Stap 2, nog steeds plakken: vervanging of refund van de pan(nen) die het betreft. Bij sets: refund van de betreffende pan pro rata van de setprijs, of de hele set als het om alle pannen gaat.
- Eén claim per klant (e-mail, adres, betaalmiddel). Pan terug in redelijke staat, geen zichtbare schade door misbruik.
- Defecten blijven onder de 75-year warranty; verkleuring is geen plakprobleem (schoonmaakadvies).

**Kernformulering (Engels, max. 40 woorden)**

> Learn it in 30 days. Cook with your pan the way our care guide shows. Still sticking? We coach you one on one. Still not right after that? We replace or refund it, within 30 days of delivery.

(38 woorden.)

**Verwachte conversiewinst.** Schatting +1 tot +4% relatief. Onderbouwing: (1) het dekt precies het risico dat in twee derde van de trial-tickets zit (338 van 502 noemen ook plakken); (2) volgens de meta-analyse verhoogt soepelheid in reikwijdte retouren, maar hier is de reikwijdte smal (één klacht, met bewijs) en de moeite hoog (eerst coaching), dus de retourstijging blijft beperkt terwijl het signaal "we staan erachter" sterk is; (3) risico-omkering presteert in Siraat-ads en mails beter dan korting. Bij 5.100 orders: +1% = 51 orders ($8.700 contributie), +2,5% = 128 orders ($21.900), +4% = 204 orders ($35.000).

**Verwachte extra retourkosten**

| | Laag | Basis | Hoog |
|---|---|---|---|
| Plakmeldingen per maand (incl. extra omdat het beloofd wordt) | 110 | 150 | 200 |
| Opgelost door coaching | 60% | 40% | 25% |
| Haalt bewijsstap | 80% | 80% | 90% |
| Claims na coaching | 35 | 72 | 135 |
| Extra refund-dollars (70% kiest refund à $150) | $3.700 | $7.600 | $14.200 |
| Extra refunds als % van bruto-omzet | +0,3 pp | +0,6 pp | +1,1 pp |
| Retour totaal | circa 5,8% | circa 6,1% | circa 6,6% |
| Netto kosten (na restwaarde 25%, $20 label, 35% die nu al goodwill of chargeback krijgt, 30% kiest ruil à $55, coaching 20 min per melding) | **$3.300** | **$6.300** | **$11.400** |
| Break-even conversiewinst | +0,4% | +0,7% | +1,3% |

Lees de tabel zo: in het basisscenario is (b) terugverdiend bij circa 37 extra orders per maand, 0,7% meer conversie. De verwachte winst (+1 tot +4%) ligt daarboven, maar de onderkant van die schatting zit dicht bij de bovenkant van de kosten.

**Misbruikrisico.** Laag tot middel. Het bewijs (video van de watertest) en de coachingstap maken "even gratis lenen" onaantrekkelijk. Risico zit in klanten die de video's doorzien en toch claimen; afvangen met één claim per klant en de bestaande risk-tags in Gorgias (refund_abuse, excessive_claims). Praktisch risico: support moet coachen in plaats van weigeren; dat kost tijd (circa 50 uur per maand in het basisscenario) en vraagt een vaste werkwijze.

**Testopzet.** Twee opties:

1. **Visitor-split (aanbevolen voor zuiverheid).** Intelligems content-test, 50/50 op bezoekersniveau, op PDP-blok, cart en checkout-blok. De variant gaat als order-attribuut mee naar Shopify (tag `lg-b`), Gorgias toont de tag en de agent gebruikt de macro van die variant. Primair: omzet per bezoeker en conversie; leidend: add-to-cart per sessie; achteraf: claims en refunds per cohort tot 45 dagen na bezorging. Statistiek: conversie van 1,64% met circa 311.000 bezoekers per maand; een verschil van 5% relatief zien vraagt circa 384.000 bezoekers per arm (circa 2,5 maand), 3% vraagt bijna 7 maanden. Add-to-cart (5,25% per sessie) ziet 3% in circa 1,7 maand. Dus: 8 weken laten lopen, beslissen op add-to-cart plus omzet per bezoeker, retourcohort 45 dagen nameten.
2. **Per markt.** (b) aan in Australië en Nieuw-Zeeland (Australië alleen al circa 12% van orders; Shopify-markets heeft al eigen template-contexten voor Australia), VS als controle, 8 weken voor en 8 weken na (verschil in verschil). Eenvoudiger juridisch en operationeel (één beleidstekst per markt), maar minder zuiver en minder volume.

Niet doen: vóór-na in één markt in Q4. BFCM vertekent alles.

**Service-macro (b), stap 1: eerste melding "plakt"**

> Hi {{ticket.customer.firstname}},
>
> Thank you for telling us. Your pan is covered by Learn it in 30 days, so let's get it right together.
>
> First, the short version of what works: preheat on medium for 2 to 3 minutes, do the water test (a drop should roll like a bead), add a teaspoon of oil, wait 10 seconds, and let food release on its own before you move it. Video: https://siraatskitchen.com/pages/care-use
>
> Could you send me a short video (30 seconds is plenty) of your preheat and water test on your own stove? Then I can tell you exactly what to change. Most people need one or two adjustments.
>
> Give it a week with my tips. If it still sticks after that, we'll replace the pan or refund it. Your choice, and we cover the return label.
>
> {{current_user.firstname}}, Siraat's Kitchen

**Service-macro (b), stap 2: coaching heeft niet geholpen**

> Hi {{ticket.customer.firstname}},
>
> Thanks for giving it a real try and for the video. I'm sorry it still isn't working for you. As promised, you choose:
>
> 1. A replacement: another Siraat piece of the same value, for example a different size or the Deep Pan.
> 2. A refund for the pan: we send you a prepaid return label. Once it's back with us, the refund goes to your original payment method within 10 business days.
>
> Just reply with 1 or 2. Your 75-year warranty against defects stays with whatever you keep.
>
> {{current_user.firstname}}, Siraat's Kitchen

(Intern: tag `learn-30-claim`, één claim per klant, controle op risk-tags vóór stap 2.)

## 4. Variant (c): 30 dagen, ook gebruikt retour

**Wat het is.** Wat de PDP nu al belooft: kook er 30 dagen op; niet de beste pan die je hebt gehad, dan volledige refund, ook gebruikt. Met voorwaarden.

**Voorwaarden (voorstel)**

- 30 dagen na bezorging, alle onderdelen mee, normaal huishoudelijk gebruik (geen verbrande of kromgeslagen pan door misbruik).
- Eén gebruikte retour per huishouden.
- Retourlabel: gratis in de VS, of op kosten van de klant (dat laatste haalt een deel van het conversie-effect weg; meta-analyse: geld-soepelheid telt).
- Sets: hele set terug, of pro rata per stuk; vooraf vastleggen.
- Geen restocking fee (dat ondergraaft de belofte).

**Kernformulering (Engels, max. 40 woorden)**

> Cook on it for 30 days. If it is not the best pan you have owned, send it back, used, for a full refund. One return per household. Plus a 75-year warranty against defects.

(34 woorden.)

**Verwachte conversiewinst.** Schatting +3 tot +8% relatief (deep/03 rij 1). Dit is de sterkste belofte en de best verkoopbare zin. Maar de meta-analyse waarschuwt juist hier: soepelheid in reikwijdte (gebruikt mag terug) is de dimensie die retouren het meest verhoogt. +3% = 153 orders ($26.200), +5,5% = 280 orders ($48.100), +8% = 408 orders ($70.000).

**Verwachte extra retourkosten**

| | Laag | Basis | Hoog |
|---|---|---|---|
| Extra gebruikte retouren per maand (nu circa 130 weigeringen per maand, plus wie nu niet vraagt, plus belofte-effect) | 150 | 200 | 300 |
| Extra refund-dollars (gemiddeld $170, sets inbegrepen) | $25.500 | $34.000 | $51.000 |
| Extra refunds als % van bruto-omzet | +1,9 pp | +2,5 pp | +3,8 pp |
| Retour totaal | circa 7,4% | circa 8,0% | circa 9,3% |
| Netto kosten (na restwaarde 25%, $20 label, 35% die nu al goodwill of chargeback krijgt) | **$16.900** | **$22.500** | **$33.800** |
| Break-even conversiewinst | +1,9% | +2,6% | +3,9% |

Lees de tabel zo: (c) heeft de grootste mogelijke winst en de grootste spreiding. Bij +5,5% conversie levert het netto circa $25.000 per maand op; bij +2% is het in het lage scenario ongeveer quitte en kost het in het basisscenario circa $5.000 en in het hoge circa $16.000 per maand. Daarnaast: meer werkkapitaal in retouren, meer gebruikte pannen om af te zetten (B-stock of donatie), en een hoger retourpercentage dat bij betaalproviders en marketplaces zichtbaar wordt.

**Misbruikrisico.** Middel tot hoog. "Lenen voor een etentje", sets van $599 tot $799 die 30 dagen gebruikt worden, en seriële retourneerders. Afvangen: één gebruikte retour per huishouden (e-mail, adres, betaalmiddel), alle onderdelen, risk-tags, steekproef op staat. Ook dan blijft dit de variant met het meeste lek.

**Testopzet.** Zelfde opzet als (b), visitor-split via Intelligems met order-tag `lg-c`. Omdat het verwachte effect groter is, is het sneller te zien: 8% relatief in circa 1 maand, 5% in circa 2,5 maand. Een driearmige test (a/b/c) halveert het verkeer per arm; beter twee rondes: eerst (b) tegen (a), dan (c) tegen de winnaar. Retourcohort minimaal 45 dagen na bezorging nameten voor je beslist; de kosten komen pas na de conversie.

**Service-macro (c): gebruikte pan, wil terug**

> Hi {{ticket.customer.firstname}},
>
> Thanks for cooking with it and for being honest with us. If it isn't the pan for you, you can send it back within 30 days of delivery, used, for a full refund.
>
> Before you do: if sticking is the reason, here are the three things that fix most cases (preheat on medium, the water test, a teaspoon of oil): https://siraatskitchen.com/pages/care-use. Happy to look at a short video if you want to give it one more go.
>
> If you'd rather return it, start here: https://return.siraatskitchen.com. Choose "Used, 30-day promise", add two photos, and use your order number with a # in front. We'll email your return label once it's approved. Please include all parts and lids.
>
> The refund goes to your original payment method within 10 business days after the pan arrives back with us.
>
> {{current_user.firstname}}, Siraat's Kitchen

## 5. Naast elkaar

| | (a) Helder huidig beleid | (b) Learn it in 30 days | (c) 30 dagen, ook gebruikt |
|---|---|---|---|
| Belofte | Ongebruikt terug, gebruikt alleen bij defect | Gebruikt en plakt: coaching, dan ruil of refund | Gebruikt en niet tevreden: refund |
| Meta-analyse-dimensie | Geen verruiming (eventueel geld: gratis label) | Smalle reikwijdte, hoge moeite | Brede reikwijdte |
| Conversie (schatting, relatief) | 0 tot +2% t.o.v. eerlijke basis; mogelijk lager dan de site nu | +1 tot +4% | +3 tot +8% |
| Extra netto kosten per maand | $0 tot $1.900 | $3.300 tot $11.400 (basis $6.300) | $16.900 tot $33.800 (basis $22.500) |
| Retour als % bruto-omzet | circa 5,5% | circa 5,8 tot 6,6% | circa 7,4 tot 9,3% |
| Break-even conversie | n.v.t. | +0,4 tot +1,3% | +1,9 tot +3,9% |
| Misbruik | Laag | Laag tot middel | Middel tot hoog |
| Klopt met PDP-tekst van vandaag | Nee, PDP moet aangepast | Deels | Ja |
| Werkdruk support | Lager (minder conflict) | Hoger (coaching) | Middel (verwerking retouren) |
| Test | Niet nodig voor conversie; voor-na op conflict en reviews | Visitor-split 8 weken of markt AU/NZ | Visitor-split 4 tot 10 weken |

Wat in alle drie hetzelfde moet, los van de keuze: PDP, beleidspagina, warranty-pagina, help center, macro's en guidances zeggen dezelfde zin. Zolang de PDP "full refund after 30 days of cooking" zegt en service "used can't be returned", lekt elke variant.

## 6. Aannames en open vragen voor Floris

1. **Contributiemarge per extra order.** Aangenomen 65% ($172). Echte landed cost per pan en per set nodig; bij 50% stijgen alle break-evens met circa 30%.
2. **Retourlabel ongebruikte producten: gratis of klant betaalt?** Nu zeggen bronnen beide. Kosten gratis: circa $1.900 per maand. Wat kost een label echt per land (een ticket in oktober rekende $28,28 voor een deksel)?
3. **Restwaarde van een gebruikte pan.** Aangenomen 25% (B-stock). Bestaat er een afzetkanaal, of wordt het donatie (restwaarde 0, maar geen retourlabel nodig)?
4. **Goodwill-praktijk vandaag.** Aangenomen dat 35% van de klagers nu al iets krijgt (80% refund, 10%, 20% tegoed, chargeback). Hoeveel refund-dollars gaan nu naar gebruikte pannen? Dat bepaalt hoeveel van (b) en (c) echt extra is.
5. **Sets.** Mogen sets onder (b) of (c) vallen, en hoe (pro rata of hele set)? Sets ($349 tot $799) zijn per retour het grootste kostenrisico.
6. **Oudere orders met 100-day trial.** Guidance zegt "per geval". Komt er een vaste regel, zodat de 40 trial-tickets na 15 september niet elk een discussie worden?
7. **Juridisch.** EU, UK, Noorwegen, Australië en Nieuw-Zeeland zijn actieve markten. EU/UK: wettelijk herroepingsrecht 14 dagen, gebruik om het product te beoordelen mag; weigeren mag niet, waardevermindering verrekenen wel. "Klant betaalt retour" alleen als vooraf gemeld. VS: een "risk-free, full refund"-belofte op de PDP moet je nakomen (FTC 16 CFR 239). Laten toetsen door een jurist voordat een variant live gaat.
8. **Ads.** Staan "100 DAYS TO DECIDE", "Zero Risk Guarantee" en de "LIFETIMEGUARANTEE"-video's nog live in Meta?
9. **Deuk door een val: gedekt of niet?** Warranty-pagina zegt nee, guidance en mail N1 zeggen ja.
