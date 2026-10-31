# BFCM 2026 · lifecycle-varianten (voorbeelden, niet live)

Gemaakt 31 okt 2026. Niets in Klaviyo, Shopify of Figma aangepast; bronmails in `klaviyo/templates/v3/<flow>/` zijn niet gewijzigd. Per mail: `<naam>-bf.html` (bron met blokken), `<naam>-bf.klaviyo.html` (build), `<naam>-bf-preview.html` (Django-render op een voorbeeld-event) en `previews/<naam>-bf-375.png`.

## Algemene regels (Floris, 31 okt, gaat boven de eerdere werkhypothese HI10)
- Aanbod: Black Friday Sale, "Up to 70% off", voor iedereen, via https://siraatskitchen.com/collections/black-friday-sale. Nooit "70% off everything".
- Geen enkele code in welcome, post-purchase, winback of VIP: alle `/discount/HI10?redirect=` en eigen codes (R2_10_72H, R2_VIP_15_72H, SK_REGULARS15_14D, P3_THANKYOU_10_14D) zijn eruit. Codemails (P3, R2, R2-VIP, V1) zijn gebouwd op hun codeloze zus: tijdens BF krijgen beide router-armen dezelfde mail.
- Topbalk overal: bf-topbar "BLACK FRIDAY SALE IS LIVE" (ink #272727, geel), boven de vaste {{HEADER}} (lockup-logo) en {{FOOTER}} blijven.
- Welcome: hero vervangen door bf-hero (Exclusive dark) + bf-topbar; codebalk HI10 weg; HI10-aanbodkaart wordt bf-deal "Up to 70% off"; hoofd- en slotknop bf-cta "Shop the sale" naar de BF-collectie (UTM-waarden gelijk aan de bron).
- Post-purchase: alleen de topbalk, rustig, geen dealblok. Wel weggehaald wat tijdens de sale niet klopt: vaste prijzen (xsell prices="none", prijszinnen) en de gifts5-regel "Your 4 gifts end when the fall sale ends."
- Winback en VIP: bf-hero "Worth / locking up." met sub "Black Friday Sale is live. Up to 70% off." (geen early access, de sale is al live); knoppen bf-cta naar de sale.
- Brieven zonder hero (W2, V2) blijven brieven: alleen topbalk, P.S. over de sale, knop bf-cta.
- Geen bedragen die niet exact met Shopify kloppen: {{PRICE}}/{{WAS}} en xsell-prijzen weg; giftwaarden ($70 in gifts) en de orderregel in P1 (echte orderdata) blijven.
- "Non-toxic" mag (Floris), tekst van Benjamin en reviews ongewijzigd. Geen gedachtestreepje (gecontroleerd op bron, build en preview).
- Build: `python3 -I scripts/build_template.py <naam>-bf.html assets assets/klaviyo-urls.txt` (assets = samengevoegde inhoud van welcome, post-purchase, winback, vip; klaviyo-urls.txt samengevoegd). Map `lifecycle` staat niet in v5lib.FLOWSIG, dus elke mail heeft `<!-- MARKET-SIGNAL: profile|order -->`.
- Previews zijn met Django gerenderd (PLAYBOOK, "Previews met logica"): expand (afgeleid van build_template) + research/tailoring/test/render.py op voorbeeld-events (welcome: profiel US, W4-INT: UK; post-purchase/winback/VIP: Placed Order US met pan, set, plank of schort). Alle shots 375 px breed zonder horizontale overloop, nagekeken.

## Open vragen [VRAAG FLORIS]
- Code-routers (P3, R2/R2-VIP T02, VIP V1): tijdens BF naar de codeloze tak sturen? De BF-varianten gaan daarvan uit.
- VIP verliest tijdens BF de 15%-code; de sale vervangt die. Akkoord?
- Zitten alle vier de pan-maten en de sets in /collections/black-friday-sale (W4 zegt per maat "In the Black Friday Sale")?
- Onderwerp-test Q1 (W1) loopt op dezelfde template: in BF beide onderwerpen BF-versie (zie W1-A).

## Per mail

### W0 (`w0-bf.html`)
- Bron: `klaviyo/templates/v3/welcome/w0.html`
- Flow/bericht: v4 · Welcome, stap 2, pad bestaande klant (CS A2: al klant)
- Onderwerpen (BF): A: 'Thank you. Now the first egg.' (ongewijzigd, rustig) / SPEC: '2 to 3 minutes on medium. Then the egg.' / Q: 'Ready for your first egg?'
- Preview: Cold metal grabs your food, hot metal lets it go. (ongewijzigd)
- Wijzigingen: bf-topbar boven de header; hero vervangen door bf-hero (06-slate-flatlay) met de kookgids als idee; beide knoppen bf-cta (zelfde link naar de kookgids); prijs van het deksel ({{PRICE:lid}}) weg in de cross-sell-regel (saleprijs onbekend); verder ongewijzigd, geen aanbodblok (klantmail)
- Aannames: Klantmail zonder aanbod in de bron: alleen de topbalk meldt de sale, geen dealblok
- Shot: `previews/w0-bf-375.png`

### W1 (T04 dicht met A; Q1 loopt als onderwerptest op dezelfde template, variatie 119850658) (`w1-a-bf.html`)
- Bron: `klaviyo/templates/v3/welcome/w1-a.html`
- Flow/bericht: v4 · Welcome (lijst Uw8eZG), stap 3, prospectpad
- Onderwerpen (BF): A (BF van A): 'No PFAS. Here's the paper. Up to 70% off.' / Q1 (BF van variatie B): 'The Black Friday Sale is live' / C+B: 'The paper behind no PFAS, now in the sale' / SPEC: 'Report no. 25895. Up to 70% off.' / Q: 'Has your pan been tested?' / OFFER: 'Up to 70% off, plus 4 gifts'
- Preview: Light Labs report no. 25895. The Black Friday Sale is live: up to 70% off.
- Wijzigingen: codebalk HI10 vervangen door bf-topbar; hero vervangen door bf-hero (01-plinths); hoofd- en slotknop bf-cta naar /collections/black-friday-sale (utm gelijk, utm_term t04-a); aanbodkaart HI10 vervangen door bf-deal "Up to 70% off"; alle /discount/HI10-links omgezet naar de gewone productlink; P.S. en tekst verder ongewijzigd
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan; Q1 blijft een onderwerptest op deze ene template
- Shot: `previews/w1-a-bf-375.png`

### W2 (brief van Benjamin, tekstmail) (`w2-bf.html`)
- Bron: `klaviyo/templates/v3/welcome/w2.html`
- Flow/bericht: v4 · Welcome, stap 4 (dag 1), prospectpad
- Onderwerpen (BF): A: 'The pan nobody else was making' (ongewijzigd, het verhaal draagt de mail) / SPEC: 'December 20, 2024' / OFFER in P.S.: 'A note from Benjamin (and the sale)'
- Preview: It's Benjamin. I wanted to write to you myself. (The Black Friday Sale is in the P.S.)
- Wijzigingen: Geen hero in de bron, dus geen bf-hero (brief blijft brief): alleen bf-topbar; P.S. HI10 vervangen door de sale; offer-kaart HI10 vervangen door bf-deal "Up to 70% off" + bf-cta (cream) naar de sale; verhaal Benjamin ongewijzigd
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan
- Shot: `previews/w2-bf-375.png`

### W3 (`w3-bf.html`)
- Bron: `klaviyo/templates/v3/welcome/w3.html`
- Flow/bericht: v4 · Welcome, stap 5 (dag 3), prospectpad
- Onderwerpen (BF): A: 'Has your cookware been tested?' (ongewijzigd) / SPEC: 'Report no. 25895. Up to 70% off.' / OFFER: 'The proof first. Then the sale.' / C+B: 'Six things to check before Black Friday' / Q: 'Skeptical about Black Friday deals? Good.'
- Preview: Six things you can check yourself, before you buy. Then up to 70% off.
- Wijzigingen: codebalk HI10 vervangen door bf-topbar; hero vervangen door bf-hero (02-gallery-vitrines, pan in een vitrine = bewijs); beide knoppen bf-cta naar de sale; /discount/HI10-links omgezet; bewijsladder, certificaat en reviews ongewijzigd
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan
- Shot: `previews/w3-bf-375.png`

### W4-US (`w4-us-bf.html`)
- Bron: `klaviyo/templates/v3/welcome/w4-us.html`
- Flow/bericht: v4 · Welcome, stap 6 (dag 6), prospectpad, splitsing op land (US)
- Onderwerpen (BF): A: 'Who are you cooking for?' (ongewijzigd) / OFFER: 'Your size, up to 70% off' / SPEC: 'Four sizes, one surface' / Q: 'Which size is yours this Black Friday?' / C+B: 'The size most people get right the first time'
- Preview: One, two, or a family? Pick your pan by that. Up to 70% off in the Black Friday Sale.
- Wijzigingen: codebalk HI10 vervangen door bf-topbar; hero vervangen door bf-hero (04-pan-tower, alle maten); beide knoppen bf-cta naar de sale; prijsregels met HI10 in de maatkiezer vervangen door "In the Black Friday Sale"; regel "Your 10% comes off at checkout" vervangen door "Up to 70% off in the Black Friday Sale"; productkaart 6-delig zonder pil FALL SALE, zonder "Buy 2, get 4 free" en zonder prijs; 12-delig: beeld card-set12-save587 (bedrag in het beeld) vervangen door de Shopify-productfoto 12pcsset.webp, prijs weg; /discount/HI10-links omgezet naar gewone productlinks
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan; aanname: alle vier de maten en de sets zitten in de BF-collectie [VRAAG FLORIS]; fall-setaanbod (Buy 2, get 4 free) niet meegenomen
- Shot: `previews/w4-us-bf-375.png`

### W4-INT (`w4-int-bf.html`)
- Bron: `klaviyo/templates/v3/welcome/w4-int.html`
- Flow/bericht: v4 · Welcome, stap 6 (dag 6), prospectpad, splitsing op land (internationaal)
- Onderwerpen (BF): A: 'Who are you cooking for?' (ongewijzigd) / OFFER: 'Your size, up to 70% off' / SPEC: 'Four sizes, one surface' / Q: 'Which size is yours this Black Friday?' / C+B: 'The size most people get right the first time'
- Preview: One, two, or a family? Pick your pan by that. Free shipping, duties paid.
- Wijzigingen: codebalk HI10 vervangen door bf-topbar; hero vervangen door bf-hero (04-pan-tower, alle maten); beide knoppen bf-cta naar de sale; prijsregels met HI10 in de maatkiezer vervangen door "In the Black Friday Sale"; regel "Your 10% comes off at checkout" vervangen door "Up to 70% off in the Black Friday Sale"; productkaart 6-delig zonder pil FALL SALE, zonder "Buy 2, get 4 free" en zonder prijs; /discount/HI10-links omgezet naar gewone productlinks
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan; aanname: alle vier de maten en de sets zitten in de BF-collectie [VRAAG FLORIS]; fall-setaanbod (Buy 2, get 4 free) niet meegenomen
- Shot: `previews/w4-int-bf-375.png`

### W5 (`w5-bf.html`)
- Bron: `klaviyo/templates/v3/welcome/w5.html`
- Flow/bericht: v4 · Welcome, stap 7 (laatste welcome-mail), prospectpad
- Onderwerpen (BF): A: 'Tammy is on her fourth pan' (ongewijzigd) / OFFER: 'Up to 70% off, and two promises' / SPEC: 'Her 4th pan. Your Black Friday price.' / Q: 'What would it take to convince you?' / C+B: 'Three skeptics, one year later'
- Preview: Three customers, two promises, and the Black Friday Sale: up to 70% off.
- Wijzigingen: codebalk HI10 vervangen door bf-topbar; hero vervangen door bf-hero (09-chefs-table); hoofdknop bf-cta (donker); offer-kaart HI10 vervangen door bf-deal "Up to 70% off" + bf-cta (cream) als slotknop; P.S. over HI10 vervangen door een P.S. over de sale
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan
- Shot: `previews/w5-bf-375.png`

### P1-FIRST (`p1-first-bf.html`)
- Bron: `klaviyo/templates/v3/post-purchase/p1-first.html`
- Flow/bericht: v4 · Post-purchase (trigger Placed Order RSNxYV), stap 1, CS eerste order
- Onderwerpen (BF): A: 'Good call. Here's what's coming.' (ongewijzigd) / B: 'The first egg will tell you' (ongewijzigd)
- Preview: Ongewijzigd (zie hieronder)
- Wijzigingen: Alleen bf-topbar "BLACK FRIDAY SALE IS LIVE" (ink) boven de header; rustig, geen dealblok; verder alles ongewijzigd
- Aannames: Topbalk meldt alleen de sale, zonder bedrag of druk
- Shot: `previews/p1-first-bf-375.png`

### P1-REPEAT (`p1-repeat-bf.html`)
- Bron: `klaviyo/templates/v3/post-purchase/p1-repeat.html`
- Flow/bericht: v4 · Post-purchase, stap 1, CS herhaalorder
- Onderwerpen (BF): A: 'Good to see you again' (ongewijzigd) / B: 'Round two. Here's what's coming.' (ongewijzigd)
- Preview: Ongewijzigd (zie hieronder)
- Wijzigingen: Alleen bf-topbar "BLACK FRIDAY SALE IS LIVE" (ink) boven de header; rustig, geen dealblok; verder alles ongewijzigd
- Aannames: Topbalk meldt alleen de sale, zonder bedrag of druk
- Shot: `previews/p1-repeat-bf-375.png`

### P2 (`p2-bf.html`)
- Bron: `klaviyo/templates/v3/post-purchase/p2.html`
- Flow/bericht: v4 · Post-purchase · levering (Delivered Shipment VcUF33), plus vangnet R9dcdY
- Onderwerpen (BF): A: 'The mistake that makes titanium stick' (ongewijzigd) / B: 'Can you do an egg? Then anything.' (ongewijzigd)
- Preview: Ongewijzigd (zie hieronder)
- Wijzigingen: Alleen bf-topbar "BLACK FRIDAY SALE IS LIVE" (ink) boven de header; rustig, geen dealblok; verder alles ongewijzigd
- Aannames: Topbalk meldt alleen de sale, zonder bedrag of druk
- Shot: `previews/p2-bf-375.png`

### P2-SAFE (`p2-safe-bf.html`)
- Bron: `klaviyo/templates/v3/post-purchase/p2-safe.html`
- Flow/bericht: v4 · Post-purchase, stap 2 (tak zonder Delivered Shipment, X3ySuU)
- Onderwerpen (BF): A: 'When your pan arrives: the first egg' (ongewijzigd) / B: 'Is your pan on the stove yet?' (ongewijzigd)
- Preview: Ongewijzigd (zie hieronder)
- Wijzigingen: Alleen bf-topbar "BLACK FRIDAY SALE IS LIVE" (ink) boven de header; rustig, geen dealblok; verder alles ongewijzigd
- Aannames: Topbalk meldt alleen de sale, zonder bedrag of druk
- Shot: `previews/p2-safe-bf-375.png`

### P3-PAN (`p3-pan-bf.html`)
- Bron: `klaviyo/templates/v3/post-purchase/p3-pan-nocode.html`
- Flow/bericht: v4 · Post-purchase, stap 3, router-tak pan (in BF beide takken: p3-pan en p3-pan-nocode)
- Onderwerpen (BF): Onderwerp en preview van p3-pan-nocode (ongewijzigd, zie oorspronkelijke kopcommentaar)
- Preview: Ongewijzigd (zie hieronder)
- Wijzigingen: Alleen bf-topbar "BLACK FRIDAY SALE IS LIVE" (ink) boven de header; rustig, geen dealblok; xsell zonder prijzen (prices="none", saleprijzen staan niet in de bron); gifts5 zonder urgentieregel ("Your 4 gifts end when the fall sale ends." klopt niet tijdens BF); verder alles ongewijzigd. Gebouwd op de codeloze versie: geen enkele code in post-purchase tijdens BF (Floris, 31 okt), dus de codetak p3-pan (P3_THANKYOU_10_14D) en p3-pan-nocode krijgen allebei deze mail
- Aannames: Topbalk meldt alleen de sale, zonder bedrag of druk; de P3-code wordt tijdens BF niet uitgedeeld (router: tijdens BF naar de codeloze tak) [VRAAG FLORIS of de code-router zo moet]
- Shot: `previews/p3-pan-bf-375.png`

### P3-SET (`p3-set-bf.html`)
- Bron: `klaviyo/templates/v3/post-purchase/p3-set-nocode.html`
- Flow/bericht: v4 · Post-purchase, stap 3, router-tak set (in BF beide takken: p3-set en p3-set-nocode)
- Onderwerpen (BF): Onderwerp en preview van p3-set-nocode (ongewijzigd, zie oorspronkelijke kopcommentaar)
- Preview: Ongewijzigd (zie hieronder)
- Wijzigingen: Alleen bf-topbar "BLACK FRIDAY SALE IS LIVE" (ink) boven de header; rustig, geen dealblok; xsell zonder prijzen (prices="none", saleprijzen staan niet in de bron); gifts5 zonder urgentieregel ("Your 4 gifts end when the fall sale ends." klopt niet tijdens BF); verder alles ongewijzigd. Gebouwd op de codeloze versie: geen enkele code in post-purchase tijdens BF (Floris, 31 okt), dus de codetak p3-set (P3_THANKYOU_10_14D) en p3-set-nocode krijgen allebei deze mail
- Aannames: Topbalk meldt alleen de sale, zonder bedrag of druk; de P3-code wordt tijdens BF niet uitgedeeld (router: tijdens BF naar de codeloze tak) [VRAAG FLORIS of de code-router zo moet]
- Shot: `previews/p3-set-bf-375.png`

### P3-NEXT (`p3-next-bf.html`)
- Bron: `klaviyo/templates/v3/post-purchase/p3-next-nocode.html`
- Flow/bericht: v4 · Post-purchase, stap 3, router-tak next (in BF beide takken: p3-next en p3-next-nocode)
- Onderwerpen (BF): Onderwerp en preview van p3-next-nocode (ongewijzigd, zie oorspronkelijke kopcommentaar)
- Preview: Ongewijzigd (zie hieronder)
- Wijzigingen: Alleen bf-topbar "BLACK FRIDAY SALE IS LIVE" (ink) boven de header; rustig, geen dealblok; xsell zonder prijzen (prices="none", saleprijzen staan niet in de bron); gifts5 zonder urgentieregel ("Your 4 gifts end when the fall sale ends." klopt niet tijdens BF); verder alles ongewijzigd. Gebouwd op de codeloze versie: geen enkele code in post-purchase tijdens BF (Floris, 31 okt), dus de codetak p3-next (P3_THANKYOU_10_14D) en p3-next-nocode krijgen allebei deze mail
- Aannames: Topbalk meldt alleen de sale, zonder bedrag of druk; de P3-code wordt tijdens BF niet uitgedeeld (router: tijdens BF naar de codeloze tak) [VRAAG FLORIS of de code-router zo moet]
- Shot: `previews/p3-next-bf-375.png`

### P3-APRON (`p3-apron-bf.html`)
- Bron: `klaviyo/templates/v3/post-purchase/p3-apron-nocode.html`
- Flow/bericht: v4 · Post-purchase, stap 3, router-tak apron (in BF beide takken: p3-apron en p3-apron-nocode)
- Onderwerpen (BF): Onderwerp en preview van p3-apron-nocode (ongewijzigd, zie oorspronkelijke kopcommentaar)
- Preview: Ongewijzigd (zie hieronder)
- Wijzigingen: Alleen bf-topbar "BLACK FRIDAY SALE IS LIVE" (ink) boven de header; rustig, geen dealblok; prijszin Pan Pro ({{PRICE:standard}}) weg (saleprijs onbekend); xsell zonder prijzen (prices="none", saleprijzen staan niet in de bron); gifts5 zonder urgentieregel ("Your 4 gifts end when the fall sale ends." klopt niet tijdens BF); verder alles ongewijzigd. Gebouwd op de codeloze versie: geen enkele code in post-purchase tijdens BF (Floris, 31 okt), dus de codetak p3-apron (P3_THANKYOU_10_14D) en p3-apron-nocode krijgen allebei deze mail
- Aannames: Topbalk meldt alleen de sale, zonder bedrag of druk; de P3-code wordt tijdens BF niet uitgedeeld (router: tijdens BF naar de codeloze tak) [VRAAG FLORIS of de code-router zo moet]
- Shot: `previews/p3-apron-bf-375.png`

### P3-ACCESSORY (`p3-accessory-bf.html`)
- Bron: `klaviyo/templates/v3/post-purchase/p3-accessory-nocode.html`
- Flow/bericht: v4 · Post-purchase, stap 3, router-tak accessory (in BF beide takken: p3-accessory en p3-accessory-nocode)
- Onderwerpen (BF): Onderwerp en preview van p3-accessory-nocode (ongewijzigd, zie oorspronkelijke kopcommentaar)
- Preview: Ongewijzigd (zie hieronder)
- Wijzigingen: Alleen bf-topbar "BLACK FRIDAY SALE IS LIVE" (ink) boven de header; rustig, geen dealblok; prijs Pan Pro ({{PRICE:standard}}) weg uit de opener (saleprijs onbekend); xsell zonder prijzen (prices="none", saleprijzen staan niet in de bron); gifts5 zonder urgentieregel ("Your 4 gifts end when the fall sale ends." klopt niet tijdens BF); verder alles ongewijzigd. Gebouwd op de codeloze versie: geen enkele code in post-purchase tijdens BF (Floris, 31 okt), dus de codetak p3-accessory (P3_THANKYOU_10_14D) en p3-accessory-nocode krijgen allebei deze mail
- Aannames: Topbalk meldt alleen de sale, zonder bedrag of druk; de P3-code wordt tijdens BF niet uitgedeeld (router: tijdens BF naar de codeloze tak) [VRAAG FLORIS of de code-router zo moet]
- Shot: `previews/p3-accessory-bf-375.png`

### R1-PAN (`r1-pan-bf.html`)
- Bron: `klaviyo/templates/v3/winback/r1-pan.html`
- Flow/bericht: v4 · Winback (UyFc78), stap 1 (dag 45), pad kookgerei
- Onderwerpen (BF): A: 'Worth locking up. Up to 70% off.' / C+B: 'What pan owners add next, now in the sale' / SPEC: 'A lid, a wok, a crepe pan. Up to 70% off.' / Q: 'How's your pan doing?' (ongewijzigd, rustig) / OFFER: 'The Black Friday Sale is live'
- Preview: Worth locking up. The Black Friday Sale is live: up to 70% off.
- Wijzigingen: codebalk HI10 vervangen door bf-topbar; hero vervangen door bf-hero "Worth locking up." (Exclusive dark); beide knoppen bf-cta naar de sale (utm_content gelijk); alle /discount/HI10-links omgezet naar gewone links; HI10-zinnen vervangen door de sale; xsell zonder prijzen (prices="none") en zonder HI10-noot; gifts5 zonder urgentieregel (die noemt de fall sale)
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan
- Shot: `previews/r1-pan-bf-375.png`

### R1-SET (`r1-set-bf.html`)
- Bron: `klaviyo/templates/v3/winback/r1-set.html`
- Flow/bericht: v4 · Winback (UyFc78), stap 1 (dag 45), pad set
- Onderwerpen (BF): A: 'Worth locking up. Up to 70% off.' / C+B: 'The shapes a set leaves out, now in the sale' / SPEC: 'One size, a board, the tools. Up to 70% off.' / Q: 'Which pan do you reach for most?' / OFFER: 'The Black Friday Sale is live'
- Preview: Worth locking up. The Black Friday Sale is live: up to 70% off.
- Wijzigingen: codebalk HI10 vervangen door bf-topbar; hero vervangen door bf-hero "Worth locking up." (Exclusive dark); beide knoppen bf-cta naar de sale (utm_content gelijk); alle /discount/HI10-links omgezet naar gewone links; HI10-zinnen vervangen door de sale; xsell zonder prijzen (prices="none") en zonder HI10-noot; gifts5 zonder urgentieregel (die noemt de fall sale)
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan
- Shot: `previews/r1-set-bf-375.png`

### R1-ACC (`r1-acc-bf.html`)
- Bron: `klaviyo/templates/v3/winback/r1-acc.html`
- Flow/bericht: v4 · Winback (UyFc78), stap 1 (dag 45), pad accessoire
- Onderwerpen (BF): A: 'Ready for the pan? It's in the sale.' / C+B: 'The pan most kitchens start with, up to 70% off' / SPEC: 'Pan Pro, up to 70% off' / Q: 'Ready for the pan?' (ongewijzigd) / OFFER: 'The Black Friday Sale is live'
- Preview: Worth locking up. The Black Friday Sale is live: up to 70% off.
- Wijzigingen: codebalk HI10 vervangen door bf-topbar; hero vervangen door bf-hero "Worth locking up." (Exclusive dark); beide knoppen bf-cta naar de sale (utm_content gelijk); alle /discount/HI10-links omgezet naar gewone links; HI10-zinnen vervangen door de sale; xsell zonder prijzen (prices="none") en zonder HI10-noot; gifts5 zonder urgentieregel (die noemt de fall sale); prijsvergelijking met HI10 weg
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan
- Shot: `previews/r1-acc-bf-375.png`

### R2 (en R2-NOCODE) (`r2-bf.html`)
- Bron: `klaviyo/templates/v3/winback/r2-nocode.html`
- Flow/bericht: v4 · Winback (UyFc78), stap 2 (dag 75), tak niet-VIP; in BF beide armen (T02-A met code en T02-B zonder)
- Onderwerpen (BF): A: 'Worth locking up. Up to 70% off.' / C+B: 'Pan number two, in the sale' / SPEC: 'Up to 70% off, 4 gifts' / Q: 'Ready for pan number two?' / OFFER: 'The Black Friday Sale is live'
- Preview: Worth locking up. The Black Friday Sale is live: up to 70% off.
- Wijzigingen: Gebouwd op de codeloze versie r2-nocode: geen enkele code in winback tijdens BF (Floris, 31 okt), dus geen R2_10_72H, geen 72-uurstegels; bf-topbar boven de header; hero vervangen door bf-hero "Worth locking up."; beide knoppen bf-cta naar de sale; opener noemt de sale; xsell zonder prijzen; gifts5 zonder urgentieregel
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan; de code-router (T02) moet tijdens BF naar deze codeloze mail sturen [VRAAG FLORIS]
- Shot: `previews/r2-bf-375.png`

### R2-VIP (en R2-VIP-NOCODE) (`r2-vip-bf.html`)
- Bron: `klaviyo/templates/v3/winback/r2-vip-nocode.html`
- Flow/bericht: v4 · Winback (UyFc78), stap 2 (dag 75), tak VIP; in BF beide armen (T02-A met code en T02-B zonder)
- Onderwerpen (BF): A: 'Worth locking up. Up to 70% off.' / C+B: 'You came back. Here is the sale.' / SPEC: '4 gifts, free shipping, up to 70% off' / Q: 'What should we make next?' / OFFER: 'For our regulars: the Black Friday Sale'
- Preview: Worth locking up. The Black Friday Sale is live: up to 70% off.
- Wijzigingen: Gebouwd op de codeloze versie r2-vip-nocode: geen enkele code in winback tijdens BF (Floris, 31 okt), dus geen R2_VIP_15_72H, geen 72-uurstegels; bf-topbar boven de header; hero vervangen door bf-hero "Worth locking up."; beide knoppen bf-cta naar de sale; opener noemt de sale; xsell zonder prijzen; gifts5 zonder urgentieregel
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan; de code-router (T02) moet tijdens BF naar deze codeloze mail sturen [VRAAG FLORIS]; VIP verliest tijdens BF de 15%-code, de sale (tot 70%) vervangt die
- Shot: `previews/r2-vip-bf-375.png`

### V1 (en V1-NOCODE) (`v1-bf.html`)
- Bron: `klaviyo/templates/v3/vip/v1-nocode.html`
- Flow/bericht: v4 · VIP, stap 1 (30 dagen na de 2e order); in BF beide armen (v1 met code en v1-nocode)
- Onderwerpen (BF): A: 'You're a VIP. Thank you.' (ongewijzigd) / C+B: 'What VIPs add next, now in the sale' / SPEC: 'Two orders. Up to 70% off.' / Q: 'Which pan do you reach for most?' / OFFER: 'Worth locking up: the Black Friday Sale'
- Preview: Two orders makes you a VIP. The Black Friday Sale is live: up to 70% off.
- Wijzigingen: Gebouwd op de codeloze versie v1-nocode: geen enkele code in VIP tijdens BF (Floris, 31 okt), dus geen SK_REGULARS15_14D; bf-topbar boven de header; hero vervangen door bf-hero "Worth locking up." (03-velvet-trunk-steel-lids); beide knoppen bf-cta naar de sale; opener noemt de sale; xsell zonder prijzen; gifts5 zonder urgentieregel
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan; VIP-router moet tijdens BF naar deze codeloze mail sturen [VRAAG FLORIS]; VIP verliest tijdens BF de 15%-code, de sale (tot 70%) vervangt die
- Shot: `previews/v1-bf-375.png`

### V2 (vraag van Benjamin, tekstmail) (`v2-bf.html`)
- Bron: `klaviyo/templates/v3/vip/v2.html`
- Flow/bericht: v4 · VIP, stap 2 (10 dagen na V1)
- Onderwerpen (BF): A: 'A question from Benjamin' (ongewijzigd) / B: 'What should we make next?' (ongewijzigd)
- Preview: You've ordered twice. I'd love to know what you want us to make next. (ongewijzigd)
- Wijzigingen: Tekstmail zonder hero in de bron: geen bf-hero (brief blijft brief), wel bf-topbar; P.S. (if-tak over de oude 15%-code) vervangen door een P.S. over de sale, want tijdens BF deelt V1 geen code uit; knop bf-cta (cream) naar de sale
- Aannames: Aanbod (Floris, 31 okt): Black Friday Sale tot 70% korting voor iedereen via /collections/black-friday-sale; geen extra code in deze flow (alleen abandonment krijgt BFCODE); "Up to 70% off", nooit "70% off everything"; geen bedragen of prijzen per product omdat de saleprijzen per product niet in de bron staan
- Shot: `previews/v2-bf-375.png`
