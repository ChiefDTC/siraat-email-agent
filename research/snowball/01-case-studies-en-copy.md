# Social Snowball · case studies, benchmarks en copy (21 okt 2026)

Opdracht Floris: zoveel mogelijk klanten via e-mail omzetten in actieve affiliates (Social Snowball, nu ~438 affiliates), zonder dat unsubscribes, bounces of spamklachten oplopen. Dit stuk bundelt wat er bekend is (case studies, benchmarks, de Social Snowball-flows die al in ons Klaviyo-account staan, voorbeelden van andere merken, deliverability, FTC) en eindigt met een concreet voorstel: aanbod, 10 onderwerpregels en 3 volledige mails.

Niets is aangemaakt of gewijzigd in Klaviyo, Shopify of Social Snowball. Alleen gelezen (Klaviyo-metrics, -flows en -templates via de API, 21 okt).

Werkwijze en beperkingen: socialsnowball.io, help.socialsnowball.io en de meeste merkpagina's waren vanuit deze sessie niet direct bereikbaar (proxy weigert de host). Alle externe cijfers komen daarom uit zoekresultaten met bron-URL; waar een cijfer van de leverancier zelf komt staat **[vendor]**. Eigen schattingen staan als **[schatting]**.

---

## 0. Kort (voor Floris)

1. **Realistische inschrijving via e-mail**: 2 tot 5% van de aangeschreven, betrokken klanten wordt affiliate na een uitnodiging plus een herinnering [schatting, onderbouwd in 2.1]. Via de thank-you-pagina of automatische inschrijving bij aankoop worden veel meer klanten "affiliate", maar die zijn grotendeels passief.
2. **Realistische activatie**: van affiliates die zelf ja zeiden maakt 5 tot 12% binnen 90 dagen minstens 1 verkoop; van automatisch ingeschreven kopers 1 tot 3% [schatting op basis van ReferralCandy, Extole, Rewardful, 2.2].
3. **Verdeling**: ongeveer 80% van wie verkoopt doet dat precies 1 keer; 3% haalt 5 of meer; een klein groepje van ongeveer 20% van de actieve affiliates levert ongeveer 80% van de verkopen ([ReferralCandy 3.000+ programma's](https://www.referralcandy.com/blog/referral-research-report-2021), [Extole](https://www.extole.com/blog/referral-stats-to-know-in-2026/)) [vendor].
4. **Verwachting per 100 affiliates (eerste 90 dagen)**: 7 tot 17 verkopen als ze via e-mail zelf kozen (midden ~10, ~$1.950 omzet bij ~$195 per order na korting); 2 tot 5 verkopen als ze automatisch bij aankoop zijn ingeschreven [schatting].
5. **Beste structuur voor Siraat**: dubbelzijdig. Vriend **15% korting** op de eerste order (moet sterker zijn dan de publieke HI10 van 10%), affiliate **10% cash** van wat de vriend betaalt, of **15% als store credit** (keuze). Na 5 verkopen 15% cash. 30 dagen cookie, commissie pas vrij na de retourtermijn.
6. **Rekenvoorbeeld**: vriend koopt de Pan Pro Duo ($229) met 15%: betaalt $194,65; affiliate krijgt $19,47 cash of $29,20 store credit.
7. **Grootste risico**: de standaardtemplates van Social Snowball die al als draft in ons Klaviyo-account staan, bevatten verzonnen verdiensten ("She earned $300", "$150 in cash, $110 in Amazon gift cards"), placeholders ("(your brand)", "(product)") en geen Siraat-header of -footer. Niet aanzetten zoals ze zijn (sectie 3).
8. **Deliverability**: alleen betrokken en tevreden klanten (geleverd, geen refund, geen open Gorgias-ticket, 4 of 5 sterren als het kan), maximaal 1 uitnodiging plus 1 herinnering, en vooral een blok in bestaande post-purchase-mails in plaats van extra mails.

---

## 1. Social Snowball case studies

### 1.1 Wat het product doet

- Maakt bij elke aankoop automatisch een affiliate-account met eigen link of kortingscode, getoond op de thank-you-pagina ([help: "turning customers into affiliates"](https://help.socialsnowball.io/en/articles/5955565-what-does-turning-customers-into-affiliates-mean), [Getting started](https://help.socialsnowball.io/en/articles/5325096-getting-started-with-social-snowball)). Gevolg: "aantal affiliates" zegt weinig, want iedereen die koopt kan er een zijn.
- **Safelinks**: de link maakt bij elke klik een unieke kortingscode, zodat codes niet op couponsites lekken (in onze eigen template WnR6Fp: "Your referral link automatically generates and applies a unique discount code whenever it's clicked").
- Uitbetaling: cash in bulk (PayPal, Venmo, bank, gift cards via een portaal), of **store credit als Shopify-gift card**, vast bedrag of percentage, eventueel automatisch na de fraudecheck ([payouts](https://help.socialsnowball.io/en/articles/5325094-how-do-i-pay-an-affiliate-their-commission), [store credit](https://help.socialsnowball.io/en/articles/6558055-sending-store-credit-payouts-with-gift-cards)).
- Prijs volgens de Shopify-listing: vanaf $249 p/m plus 3% van affiliate-omzet ([Shopify App Store](https://apps.shopify.com/social-snowball)); oudere reviews noemen andere tiers ([Tapfiliate](https://tapfiliate.com/blog/social-snowball-review)). Die 3% moet in de margeberekening.
- Reviews: Shopify 4,8 tot 4,9 sterren over ~1.000 reviews; een minder betrouwbare bron meldt Trustpilot-klachten van affiliates over uitbetalingen ([ainfluencer](https://ainfluencer.com/social-snowball/)). Les: uitbetalingen netjes en op tijd, anders krijgen we de klachten.

### 1.2 Merken en cijfers (alles [vendor] tenzij anders vermeld)

| Merk | Wat ze deden | Cijfers | Bron |
| --- | --- | --- | --- |
| Obvi (supplementen) | Thank-you-widget maakt automatisch affiliates, Safelinks tegen lekken | 84.000+ klanten "turned into affiliates", $100K+ incrementele omzet in 4 maanden, CPA $7 ("357% cheaper than paid") | [Noah Tucker op X](https://twitter.com/noatuck/status/1834237614712611205), [SS: best programs](https://www.socialsnowball.io/post/best-affiliate-marketing-programs) |
| Bees Mission | Elke koper wordt affiliate, code met eigen naam, delen vanaf thank-you-pagina | Affiliateprogramma +1750% in 2 maanden, topline +12% | [SS case](https://socialsnowball.io/post/how-bees-mission-increased-12-revenue-without-spending-on-ads) |
| Triquetra Health | Automatisch referralprogramma voor alle klanten **15%**, apart ambassador-tier **20%** met gratis product en community, TikTok Shop gekoppeld | 6.246 nieuwe affiliates automatisch, $350K+ affiliate-omzet in 1 maand, 5.260 orders | [SS case](https://socialsnowball.io/post/triquetra-health-case-study) |
| Buoy | Drie programma's samengevoegd, Safelinks | $400K+ in 12 maanden, CPA onder $20, 80% minder beheertijd | [SS case](https://www.socialsnowball.io/post/buoy-affiliate-marketing-case-study) |
| Wildbird | Vier tiers op basis van betrokkenheid en contentkwaliteit | $196K+ in minder dan 2 maanden, 9,2x ROI, CPA $19,01 | [SS case](https://www.socialsnowball.io/post/wildbird-affiliate-program-case-study) |
| Bones Coffee | Tracking, seeding en uitbetalingen geautomatiseerd, codelekken gestopt | $150K+ affiliate-omzet in een paar maanden | [SS case](https://www.socialsnowball.io/post/bones-coffee-affiliate-program-case-study) |
| Tailored Athlete | Oud programma (Stamped) vervangen, referral in de post-purchase-flow, **cash** uitbetaling | +444% referral-omzet, 10x ROI | [SS case](https://socialsnowball.io/post/tailored-athlete-referral-case-study) |
| Seeq | | $135K+ affiliate-omzet, CPA $7 | [SS case](https://www.socialsnowball.io/case-studies/seeq) |
| Outway / Sweet Dreams | | 9% van GMV uit klantreferrals, CAC -30% / 25% van GMV uit TikTok-creators (onbetrouwbare bron, niet bevestigd) | [eCommerce Fastlane](https://ecommercefastlane.com/social-snowball-review/) |

Claim van de CEO (podcast): klassieke referralprogramma's halen zelden meer dan 1% van de omzet, Social Snowball-klanten "frequently" 10%+ ([Quiet Light podcast](https://quietlight.com/podcast/frictionless-affiliate-programs-for-your-customers-and-creators/)) [vendor, niet geaudit]. Grootste netwerken hebben "millions" affiliates, "not all of them are active" ([Behind Company Lines](https://www.hireotter.com/behindcompanylines/episode-264-noah-tucker-ceo-founder-of-social-snowball)).

**Wat ontbreekt in alle case studies**: geen enkele noemt het percentage klanten dat zich inschrijft, het percentage affiliates met minstens 1 verkoop of de tijd tot de eerste verkoop. Obvi meldt 84.000 affiliates en $100K omzet in 4 maanden: bij een order van ~$50 tot $70 zijn dat grofweg 1.500 tot 2.000 orders, dus hooguit 2% van de affiliates verkocht iets [schatting]. Dat past bij de benchmarks hieronder.

---

## 2. Benchmarks klant-naar-affiliate en referral (DTC)

### 2.1 Inschrijving (enrollment) en delen

| Maatstaf | Waarde | Bron |
| --- | --- | --- |
| Deel van klanten dat meedoet, alle branches (mediaan) | 8,1%; niet-abonnement 5,8%, abonnement 14,2% | ReferralCandy via [Review42](https://resources.review42.com/referral-marketing-statistics/) [vendor, tweedehands] |
| Topprogramma's | 15 tot 20% van klanten doet mee | [Talkable](https://get.talkable.com/blog/tips-on-measuring-and-optimizing-referral-marketing-kpis) [vendor] |
| Share-action rate, 450+ Shopify-programma's | top 25% vanaf 4,64%, top 10% vanaf 13,38% | [ReferralCandy 2026](https://www.referralcandy.com/blog/referral-program-benchmarks-whats-a-good-conversion-rate-in-2025/) [vendor] |
| Share rate | "ideaal" 5 tot 9% | [Friendbuy](https://www.friendbuy.com/blog/referral-program-metrics) [vendor] |
| Mediane "advocacy rate" (400 programma's, ruime definitie) | ~19% | [Extole](https://www.extole.com/blog/referral-stats-to-know-in-2026/) [vendor] |
| Home-categorie | laagste van de vijf onderzochte categorieën; Sport haalt 2,2x het referral-aandeel van Home | [ReferralCandy industries](https://www.referralcandy.com/blog/top-ecommerce-industries-for-referral-programs/) [vendor] |
| Referral-aandeel van alle aankopen | gemiddeld 2,35% | ReferralCandy via [Opensend](https://www.opensend.com/post/referral-rate-statistics) [vendor] |
| Bereid om aan te bevelen tegenover doet het echt | 83% tegenover 29% | via [Inputkit](https://www.inputkit.io/en/blog/how-identify-leverage-promoters/) |

Vertaald naar e-mail voor Siraat [schatting]: post-purchase-mail open 45 tot 60%, klik op een referralblok of -knop 3 tot 6% van ontvangers, inschrijving 30 tot 60% van de klikkers. Dat geeft **1 tot 3% per mail**, en **2 tot 5% na uitnodiging plus herinnering** onder betrokken klanten. Kookgerei zit in de "Home"-hoek (eenmalige aankoop, lage frequentie), dus eerder de onderkant van de ranges. Het grote voordeel: 75 jaar garantie en een product dat je dagelijks gebruikt en waar mensen naar vragen.

### 2.2 Activatie: de meeste affiliates verkopen nooit

| Maatstaf | Waarde | Bron |
| --- | --- | --- |
| Referrers met precies 1 succesvolle referral | 80% | [ReferralCandy 3.000+ programma's](https://www.referralcandy.com/blog/referral-research-report-2021) [vendor] |
| Referrers met 5 of meer ("pro-referrers") | 3%, samen bijna de helft van alle referrals | idem |
| Aandeel advocates dat 80% van de referrals levert | ~20% | [Extole](https://www.extole.com/blog/referral-stats-to-know-in-2026/) [vendor] |
| Top 10% van affiliates | 50 tot 80% van de omzet | [QualityUnit](https://cdn.qualityunit.com/blog/track-affiliate-marketing-success) [vendor] |
| Affiliates met minstens 1 verkoop (SaaS, alle aanmeldingen) | 1,28%; van wie verkeer stuurt 16,8% | [Rewardful](https://rewardful.com/articles/state-of-saas-affiliate-programs-report) [vendor] |
| Activatie "breed programma" | 10 tot 20% is typisch, 10% is goed | [Reditus](https://www.getreditus.com/resources/glossary/affiliate-activation-rate), [QualityUnit](https://cdn.qualityunit.com/blog/track-affiliate-marketing-success) |
| Gezond programma | 10% van de affiliates verkoopt regelmatig; tijdens een actie 33% minstens 1 keer | [Practical Ecommerce](https://www.practicalecommerce.com/2-Affiliate-Promotion-Case-Studies) |

Realistische verdeling voor 100 klant-affiliates die zelf ja zeiden, eerste 90 dagen [schatting]:

| Groep | Aantal | Verkopen |
| --- | --- | --- |
| Nooit gedeeld of geen verkoop | 88 tot 95 | 0 |
| 1 verkoop (vriend of familielid) | 4 tot 9 | 4 tot 9 |
| 2 tot 4 verkopen | 1 tot 2 | 2 tot 6 |
| 5+ (iemand met publiek, kookclub, groepschat) | 0 tot 1 | 0 tot 5 |
| **Totaal** | **5 tot 12 actief** | **7 tot 17, midden ~10** |

Bij automatische inschrijving (iedere koper is affiliate) deel je dezelfde actieven door een veel grotere groep: 1 tot 3 actief per 100, 2 tot 5 verkopen.

**Tijd tot eerste verkoop**: geen bron gevonden met een cijfer. Praktijk [schatting]: wie deelt, doet dat in de eerste 7 tot 14 dagen na de eerste keer koken (aanbeveling volgt op enthousiasme); daarna zakt het snel. Vandaar timing rond levering plus een week, en na een 5-sterrenreview.

**Gemiddelde verkopen per actieve affiliate**: ~1,4 tot 2 in 90 dagen (volgt uit de 80%-met-1-verdeling).

### 2.3 Wat werkt in de structuur

- **Dubbelzijdig wint**: 2 tot 3x hogere deelname dan enkelzijdig ([Viral Loops via Review42](https://resources.review42.com/referral-marketing-statistics/)), +29% deelname ([Rivo](https://www.rivo.io/blog/referral-program-statistics)) [vendor, geen onderliggende data]. Elke cookware-concurrent werkt dubbelzijdig (sectie 4).
- **Percentage of vast bedrag**: vast is makkelijker te zeggen ("Give $20, get $20"); percentage beloont grotere orders (sets van $399 tot $599). Social Snowball ondersteunt beide ([SS guide](https://socialsnowball.io/post/how-ecommerce-brands-use-social-snowball-affiliate-marketing-customer-referrals)). Gebruikelijk bij SS-klanten: **15%** voor alle klanten, **20%** voor een ambassador-tier (Triquetra).
- **Cash of store credit**: store credit kost minder (marge) en brengt de verwijzer terug in de winkel; cash motiveert sterker bij dure, zelden gekochte producten. Een vuistregel uit de praktijk: store credit bij hoge frequentie en lage prijs, cash bij hoge prijs en lage frequentie ([Bloop](https://bloop.plus/blog/best-referral-incentives/), [WebToffee](https://www.webtoffee.com/blog/referral-program-ideas/)) [heuristiek, geen meting]. Siraat is het tweede type, dus cash als basis, store credit als hogere optie.
- **Waarde van een verwezen klant**: ongeveer 25% hogere CLV, ook na de beloning (Wharton, Duitse bank, [Schmitt, Skiera, Van den Bulte](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Schmitt-Skiera-vandenBulte-2011-Referral-Programs-Customer-Value.pdf)); HexClad meldt ~$100 hogere LTV en +17% AOV voor verwezen klanten ([Rivo case](https://www.rivo.io/case-studies/hexclad)) [vendor].
- **Cookie window**: 30 dagen is de standaard voor middenprijs-producten ([QualityUnit](https://cdn.qualityunit.com/faq/how-long-do-affiliate-cookies-last)). Met Safelinks werkt de code ook zonder cookie.
- **Tiers**: werken vooral voor de kleine groep die veel verkoopt (Wildbird 4 tiers, Triquetra 15/20%, HexClad en Caraway met cadeaus per aantal verwijzingen). Voor de massa is één eenvoudige regel beter.

---

## 3. De Social Snowball-flows in ons Klaviyo-account

### 3.1 Wat er staat (GET 21 okt 2026)

De integratie is op 20 okt 2026 aangezet: 17 metrics van Social Snowball, en 6 flows als **draft** (gekloonde SS-templates, afzender "SiraatsKitchen", smart sending uit, geen UTM).

| Flow (id) | Trigger (afgeleid uit naam) | Mails | Opbouw |
| --- | --- | --- | --- |
| Post purchase_Safelinks (Xszb66) | Enrolled in SocialSnowball through purchase (XzrVJZ) | 3 | 10 min: "You can make money promoting our products!" / +2 d, alleen als nog geen verkoop: "Following up on your new position" / +3 d, idem: "She earned $300 by referring friends to (your brand)!" |
| Approved Affiliate Application (VdsfMx) | Approved affiliate application (WWqT8n) | 3 | 1 min "Welcome aboard!" / +1 d follow-up / +2 d "$300"-mail, telkens overslaan als er al een New referral sale is |
| Manually Added Affiliates in SS Dashboard (YefepE) | Signed up via manual creation (VGnMT8) | 3 | idem |
| Manually upload affiliates CSV (RZXgjW) | Signed up via manual upload (TYAaJ3) | 3 | idem |
| SF Affiliate notification of sale (VnWwqJ) | New referral sale (Xqbr4d) | 1 | "You've got money!" met orderwaarde en commissie |
| Payout Sent (VdNKHq) | Payout sent (WManrA) | 1 | "Payout sent" met bedrag en gift-cardcode |

Overige metrics die SS stuurt: Signed up via sign up form (SJy5uM), via marketplace (TTWUnD), via Shopify customers import (WjpQvK), Pending (R2KsjG) en Rejected (UBBdkE) affiliate application, Discount code changed (TPjE3f), Affiliate changed program (UYJuV7), Welcome Gift Claimed (TciBqC), New Instagram Post/Story/Reel added by affiliate (V5mKgv, VBKxxJ, Y3ctEQ).

Profielvelden die de templates gebruiken: `Affiliate First Name`, `Referral Link - SocialSnowball`, `Referral Code - SocialSnowball`, `Referral Reward - SocialSnowball`, `Referral Friend Offer - SocialSnowball`, `Referral Currency - SocialSnowball`, `Social Snowball: Payout amount`, `Social Snowball: Affiliate Order Value`, `Gift card code - Social Snowball`. Let op: SS vult deze alleen voor profielen die echt affiliate zijn ([help](https://help.socialsnowball.io/en/articles/8619793-incorporating-social-snowball-data-into-existing-klaviyo-flows)), dus in een uitnodiging aan niet-affiliates staan ze leeg.

Belangrijk: bij het aanzetten van de Klaviyo-integratie zet SS zijn eigen post-purchase-mails uit ([help](https://help.socialsnowball.io/en/articles/5325087-integrating-klaviyo-with-social-snowball)). Klaviyo is vanaf nu dus de enige bron van affiliate-mails.

### 3.2 Doel en typische copy per flow

| Flow | Doel | Typische SS-copy | Wat Siraat ervan maakt |
| --- | --- | --- | --- |
| Post purchase enrollment | Koper weet dat hij een eigen link heeft, en deelt | "Great news! Your affiliate account is officially set up", link, "Earn {reward} per successful referral", knop naar dashboard | Pas na levering (niet 10 minuten na de order, dan wil hij zijn pan, geen bijbaan), en als blok in P-mails of als welkomstmail met deelkit (mail 3 in sectie 6) |
| Signed up as affiliate (formulier, handmatig, CSV, import) | Welkom plus eerste actie | idem, plus follow-up "Following up on your new position. Want to earn some extra cash?" | Eén welkomstmail met deelkit, één reminder als er na 7 dagen geen klik op de link is |
| Approved affiliate application | Goedkeuring bevestigen (alleen bij handmatige goedkeuring) | "Welcome aboard! Your affiliate account is waiting" | Zelfde als welkom; voor creators een persoonlijke mail van Benjamin |
| New referral sale | Beloning tastbaar maken, opnieuw laten delen | "Someone just made a purchase using your discount code, nice work! Purchase value / Your commission" | Behouden, warm en kort; geen naam van de vriend (privacy); vermelden wanneer de commissie vrijkomt |
| Payout sent | Vertrouwen: het geld komt echt | "You have been paid! You've received {amount}, here is your gift card" | Behouden; plus de deellink nog eens |
| Manual upload | Bestaande groep (creators, de 438) welkom heten | zoals welkom | Eenmalig, met uitleg waarom ze de mail krijgen |

### 3.3 Problemen in de huidige drafts (niet aanzetten zoals ze zijn)

1. **Verzonnen verdiensten**: "She earned $300 by referring friends", "Someone just made $300 from their referrals", "top affiliates this month: $150 in cash, $110 in Amazon gift cards, $75 in Starbucks gift cards". Dat geldt niet voor Siraat. De FTC rekent atypische of onbewezen verdienclaims als misleidend (sectie 4.3). Alleen echte cijfers, met de typische uitkomst erbij.
2. **Placeholders**: "(your brand)" in onderwerp en preview, "(product)" in de tekst, losse `{{ organization.name }}` midden in een zin.
3. **Geen vaste header en footer** (merkregel CLAUDE.md), knoppen "SHOP NOW" zonder link, headerlinks naar www.klaviyo.com, social-iconen zonder link.
4. **Knop naar de verkeerde pagina**: "View Your Affiliate Dashboard" linkt naar `affiliates.socialsnowball.io/auth/affiliate/signup` (aanmelden in plaats van inloggen); de verkoopmail linkt naar `socialsnowball.io/login-form`. Controleren welke portal-URL voor Siraat geldt [VRAAG FLORIS of uit SS-instellingen].
5. **Toon**: "Following up on your new position", "Want to earn some extra cash?", "watch the sales roll in!" Bijbaan-taal. Past niet bij Benjamin en roept MLM-associaties op.
6. **Timing**: welkom 10 minuten na de order, terwijl P1 (orderbevestiging) en de levering nog komen. Drie mails in 5 dagen bovenop de post-purchase-reeks.
7. **Smart sending uit** en geen UTM-parameters: geen bescherming tegen stapelen, geen meting in GA.

---

## 4. Wat andere merken doen

### 4.1 Cookware en aanverwant

| Merk | Vriend krijgt | Verwijzer krijgt | Opvallend | Bron |
| --- | --- | --- | --- | --- |
| HexClad | $100 off eerste order vanaf $300 tot $400 (bronnen verschillen) | Product: mengkommenset ($129) na 1 vriend, product van $199 na 3 | Cadeau in plaats van geld, tiers; Rivo meldt $450K referral-omzet in 90 dagen, 92x ROI [vendor]. Daarnaast affiliates via Awin, met verbod op eigen e-mailcampagnes zonder suppressielijst | [Rivo case](https://www.rivo.io/case-studies/hexclad), [coupons.com](https://www.coupons.com/coupon-codes/hexclad), [Awin](https://ui.awin.com/merchant-profile/21679) |
| Caraway | $100 off eerste order (2026) of 15% (oudere versie) | Product per aantal: snijplank ($95) bij 1, messenset ($245) bij 5; daarboven doorverwezen naar het officiële affiliateprogramma | Klantreferral gaat over in affiliate bij 5+, precies de "pro-referrer"-grens | [TechRadar](https://www.techradar.com/coupons/caraway), [Tom's Guide](https://www.tomsguide.com/home/home-appliances/kitchen-dining/caraway-home-coupon-codes) |
| Our Place | $20 off vanaf $100 | $20 | "Give $20, Get $20", via het loyaltyprogramma | [BHG](https://www.bhg.com.au/?p=1145371), [Slickdeals](https://daily.slickdeals.net/kitchen/our-place-always-pan-review-worth-it/) |
| Great Jones | onbekend bedrag | onbekend | "Refer a Pal", code werkt alleen voor nieuwe klanten | [Great Jones help](https://www.greatjonesgoods.com/pages/help) |
| Made In | geen klantreferral gevonden | | Affiliates via FlexOffers (creators) | [FlexOffers](https://www.flexoffers.com/affiliate-programs/made-in-cookware-affiliate-program/) |
| Manscaped, Ridge | geen officiële give/get-voorwaarden gevonden | | Manscaped stuurt op loyalty ("Members Only Rewards") | [Business Wire](https://www.businesswire.com/news/home/20250814565816/en) |

Patroon: bij een orderwaarde van $200 tot $400 krijgt de vriend 15% of $20 tot $100, de verwijzer een cadeau of tegoed van $20 tot $130. Siraat met 15% (~$34 op een gemiddelde order) zit in het midden.

### 4.2 Recente referralmails (Email Love, aug tot okt 2026)

Onderwerpregels uit de bibliotheek ([Email Love](https://emaillove.com/?s=refer%20a%20friend)):
- "Share the Love ♥️ Give $20 / Get $20" (Tea Forté)
- "Fall Referral Bonus: $75 for them, $75 for you" (xBloom Coffee, tijdelijk verhoogd)
- "Earn Up to $100 · Your Friends Save 10%" (ECOVACS, inleiding van verdienen eerst)
- "Earn $100* when you refer a friend" en "Invite a friend, save $100! 🎉" (Castlery, sterretje voor de voorwaarden)
- "Share Your TC002 Pixbar & Earn Up to $139.9" (Ulanzi, product in de onderwerpregel)
- "Be the friend with the good recommendations." (Betabrand, identiteit in plaats van geld)
- "A quick note from Jack at LSC" (London Sock Company, oprichtersnotitie)
- "Introducing The JA Ambassador Program" (Jonathan Adler, status)
- "Know someone who'd love Birdbuddy News?" (Birdbuddy, vraag)

### 4.3 Timing, hoeken, CTA's en compliance

- **Timing**: 1 tot 3 dagen na levering, of een P.S. in de orderbevestiging ([Viral Loops](https://viral-loops.com/blog/how-to-write-referral-program-emails/)); direct na een positieve review of NPS 9 tot 10 ([ReferralCandy](https://referralcandy.com/blog/best-time-to-ask-for-a-referral)). Voor kookgerei: na de eerste keer koken, dus levering plus 5 tot 10 dagen.
- **Hoeken**: (1) geef je vriend iets ("give 15%"), werkt het best want de klant voelt zich gul, niet verkoper; (2) verdien per vriend, met een concreet rekenvoorbeeld; (3) status ("insider", "founding member", vroeg toegang); (4) bewijs van andere affiliates, alleen met echte en typische cijfers; (5) oprichtersnotitie ("a quick note from").
- **Onderwerpregels**: zeg het aanbod duidelijk; dollarbedragen werken ([ReferralCandy](https://referralcandy.com/blog/referral-email-design-examples), [Mailchimp](https://mailchimp.com/resources/referral-emails/)).
- **CTA**: eerste persoon met voordeel ("Get my link", "Share my 15% code"), niet "Join now".
- **FTC, disclosure**: een referralcode of affiliatelink is een "material connection" en moet duidelijk vermeld worden wanneer een "significant minority" van het publiek het verband niet verwacht; zichtbaar en dicht bij de aanbeveling, niet alleen in de bio, in gewone woorden ("I get a commission if you buy with my link") ([Manatt over de Endorsement Guides 2023](https://manatt.com/insights/newsletters/advertising-law/an-in-depth-look-at-the-ftcs-updates-2), [Prefinery: FTC voor referralprogramma's](https://www.prefinery.com/blog/ftc-endorsement-guides-for-referral-programs/), [ContentStudio](https://contentstudio.io/blog/affiliate-disclosure-on-social-media)). Het merk is mede verantwoordelijk: monitoren en affiliates die misleiden stoppen.
- **FTC, verdienclaims**: claims moeten de typische deelnemer weerspiegelen; "unusually successful earnings by a handful of people" zijn geen bewijs ([FTC, juni 2026](https://www.ftc.gov/business-guidance/blog/2026/06/back-those-earnings-claims-other-lessons-ftcs-labor-task-force-work), [FTC over earnings claims](https://ftc.gov/business-guidance/blog/2025/01/concerned-about-deceptive-earnings-claims-sos-ftc-we-want-your-feedback)). Dus: nooit "earn $300", nooit "extra income", "side hustle" of "passive income". Wel: "10% of what your friend pays" plus een rekenvoorbeeld per verkoop, en eerlijk "most people share it with a friend or two".
- **Productclaims door affiliates**: affiliates mogen niets zeggen wat Siraat zelf niet mag (geen gezondheidsclaims, geen "lifetime", geen "risk-free"). Daarom in de deelkit kant-en-klare zinnen met alleen goedgekeurde claims.

---

## 5. Deliverability: werven zonder schade

### 5.1 Grenzen

- Spamklachten onder 0,1%, absolute grens 0,3% (Google en Yahoo bulk-sender-regels; Klaviyo zet bij hoge klachten op slot, [Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115000308972)).
- Unsubscribe per mail onder 0,3% (flows) en 0,5% (campagnes); bounce onder 0,5% ([Vortex IQ](https://docs.vortexiq.ai/nerve-centre/kpi-cards/klaviyo/unsubscribe-rate)) [vendor-richtwaarden].
- Stopregel: boven een van deze grenzen in de eerste 2.000 verzonden, de batch of flow pauzeren en segment versmallen.

### 5.2 Wie wel, wie niet

Wel (segment "Snowball · uitnodigbaar"):
- Placed Order minstens 1 keer, **Delivered Shipment (VcUF33) minstens 5 dagen geleden** (of Fulfilled Order VtEiZT plus 10 dagen waar levering ontbreekt).
- Geopend of geklikt in de laatste 90 dagen (Opened Email WyrTym of Clicked Email W247h8). Geen nieuwe of koude adressen.
- Bij voorkeur: 4 of 5 sterren gegeven (klik in reviewmail XzHrez, zie `research/referral/02-livegang-stappen.md` stap 4 voor het onderscheid 4 en 5 sterren) of positieve enquête.

Niet:
- **Refunded Order (Xg6cwn) ooit** of retour aangevraagd.
- **Opened Ticket (YzvjGf) in de laatste 30 dagen** (Gorgias), en alle profielen met tag schade of klacht.
- Al affiliate (een van de "Signed up as an affiliate"-metrics of `Referral Link - SocialSnowball` gevuld): die krijgen geen uitnodiging maar de welkomstmail.
- Uitnodiging of herinnering in de laatste 60 dagen ontvangen.
- Bounced, suppressed, of geen marketing consent (referral is marketing, niet transactioneel).
- Buiten de US in fase 1 (bedragen in USD; zoals in het referral-ontwerp).

### 5.3 Frequentie en plaats

- **Eerst inbouwen, dan pas los versturen.** Een referralblok in bestaande mails kost nul extra sends: P2 (handleiding), P3 (cross-sell) en de reviewmail XzHrez (na de sterrenklik). Social Snowball adviseert zelf de eerste post-purchase-mail en elke reviewvraag ([help](https://help.socialsnowball.io/en/articles/8619793-incorporating-social-snowball-data-into-existing-klaviyo-flows)). Nadeel: lagere aandacht per blok. Voordeel: geen extra uitschrijvingen.
- **Eén aparte uitnodiging plus één herinnering**, nooit meer. Herinnering alleen aan wie de uitnodiging opende maar niet inschreef; wie niet opende krijgt niets extra.
- Smart sending aan (16 uur), en een flowfilter "geen andere marketingmail in 24 uur" waar de bestaande post-purchase-reeks loopt.
- **Bestaande klantenbestand (100,000+)**: niet in één campagne. In golven van de meest betrokken klanten eerst: kopers 30 tot 120 dagen geleden met open in 30 dagen, dan 120 tot 365 dagen, nooit inactieve profielen. Elke golf eerst 2.000 tot 5.000 als test, grenzen uit 5.1 controleren, dan opschalen.
- Afzender "Benjamin at Siraat's Kitchen" voor de uitnodiging (persoonlijk, lagere klachtkans) [VRAAG FLORIS, staat ook open in referral-livegang punt 9].

### 5.4 Meten

Per mail: open, klik op de inschrijfknop, "Signed up as an affiliate"-events binnen 7 dagen (conversiemetric in Klaviyo instellen op die metric in plaats van Placed Order), unsub, spam. Per cohort: % affiliates met minstens 1 "New referral sale" na 30, 60 en 90 dagen. Dat is het cijfer dat telt, niet het aantal affiliates.

---

## 6. Aanbevelingen voor Siraat

### 6.1 Aanbod

| Onderdeel | Voorstel | Waarom |
| --- | --- | --- |
| Vriend | **15% off** de eerste order, via Safelink (unieke code per klik) | Moet beter zijn dan HI10 (10%), die iedereen al via de pop-up krijgt; anders heeft de link geen waarde. Een order heeft maar één code: de vriendcode vervangt HI10 |
| Affiliate, basis | **10% cash** van wat de vriend betaalt (na korting, zonder verzending en tax) | Eenvoudig, groeit mee met sets; past bij de SS-praktijk (10 tot 15%) |
| Affiliate, keuze | of **15% als Siraat store credit** (gift card) | Goedkoper in marge, brengt de klant terug (deksel, tweede pan) |
| Tier "Insider" | na 5 verkopen: **15% cash** | Beloont de 3% die het meeste doet (Caraway-grens) |
| Creators en ambassadeurs | apart programma, **20%** plus gratis product, handmatige goedkeuring | Zoals Triquetra; de 438 bestaande affiliates eerst indelen |
| Cookie | 30 dagen | Standaard; gelijk aan de retourtermijn |
| Vrijgave commissie | na de 30-day returns plus een paar dagen (order 35 tot 40 dagen oud, geen refund) | Geen commissie op retouren; zelfde regel als het eerdere referral-ontwerp [controleren of SS een wachttijd kent] |
| Uitsluitingen | geen eigen aankopen, alleen nieuwe klanten, geen couponsites | SS-fraudefilter plus Safelinks |

Rekenvoorbeelden (voor de mails, eerlijk en per verkoop):

| Wat de vriend koopt | Vriend betaalt met 15% | Jij krijgt 10% cash | of 15% store credit |
| --- | --- | --- | --- |
| Pan Pro Duo, $229 | $194.65 | $19.47 | $29.20 |
| Gemiddelde order, ~$230 | ~$195.50 | ~$19.55 | ~$29.33 |
| 6-Pcs set, $399 | $339.15 | $33.92 | $50.87 |
| 12-Pcs set, $599 | $509.15 | $50.92 | $76.37 |

Prijzen uit `content/facts/products.csv` (21 okt); bij een andere sale of andere prijs de tabel opnieuw rekenen.

Kosten per verwezen order van $230 [schatting]: 15% korting $34.50 + 10% commissie $19.55 + 3% SS-fee $5.87 = **~$60 (26% van de lijstprijs)**. Ten opzichte van een HI10-order (die al 10% kost) is de extra kost ~$37. Of dat goedkoper is dan betaalde acquisitie hangt af van de huidige blended CAC [VRAAG FLORIS]. Met 60% brutomarge (`research/potentie/02-bottom-up.md`) blijft er per order ~$78 over.

Alternatief om te testen: **"Give 15%, get $20"** (vast bedrag voor de affiliate). Makkelijker te zeggen, maar betaalt te weinig bij sets en te veel bij een losse Mini. Advies: start met 10%, test de framing in de copy ("$19.47 on a Pan Pro Duo").

### 6.2 Flow-ontwerp (samengevat)

1. **Blok in bestaande mails** (geen extra sends): P2 onderaan, P3 onder de cross-sell, reviewmail na 5 sterren. Tekst: "Know someone still on coated pans? Give them 15% off. Get 10% back." Knop "Get my link". Profielen die al affiliate zijn zien hun eigen link (`Referral Link - SocialSnowball`), de rest de aanmeldpagina.
2. **Uitnodiging** (mail 1): trigger Delivered Shipment + 7 dagen, of direct na een 5-sterrenklik; filters uit 5.2.
3. **Herinnering** (mail 2): +5 dagen, alleen geopend en niet ingeschreven.
4. **Welkom met deelkit** (mail 3): trigger elke "Signed up as an affiliate"-metric en "Enrolled in SocialSnowball through purchase", maar bij de laatste pas na levering (wacht tot Delivered Shipment, maximaal 14 dagen).
5. **Eén nudge** na 7 dagen alleen als er geen klik op de link is; daarna stilte.
6. **New referral sale** en **Payout sent**: houden, herschrijven in Siraat-stijl, met header en footer.
7. De zes SS-drafts niet live zetten; als basis voor 4 tot 6 gebruiken en daarna archiveren.

### 6.3 Tien onderwerpregels met preview

| # | Type | Subject | Preview |
| --- | --- | --- | --- |
| 1 | Offer | Give a friend 15% off your pan | And get 10% of what they pay, in cash. |
| 2 | Specificity | $19.47 for one text message | What a Pan Pro Duo earns you when a friend uses your link. |
| 3 | Question | Who asked about your pan? | Send them 15% off. You get 10% back. |
| 4 | Curiosity + benefit | The easiest $20 in your kitchen | One link, one friend, no coatings. |
| 5 | Story (founder) | A quick note from Benjamin | 100,000+ of you found us. Most through a friend. [VRAAG FLORIS: tweede zin alleen als waar, anders "This is how we'd like to grow."] |
| 6 | Identity | Be the friend who knew about titanium | 15% off for them. 10% back for you. |
| 7 | Specificity | Report no. 25895, now with your name on it | Share the pan you tested yourself. Your friend gets 15% off. |
| 8 | Offer (reminder) | Your 15% for a friend is still here | Your link takes 10 seconds to set up. |
| 9 | Question (reminder) | Still cooking on it? | Then someone you know should be too. 15% off from you. |
| 10 | Welcome | Your link is ready | Here's what to send, word for word. |

A/B-voorstel voor de uitnodiging: 1 (offer) tegen 3 (vraag). Eén variabele, winnaar op inschrijvingen per ontvanger.

### 6.4 Drie mails

Alle drie met de vaste header en footer uit `klaviyo/templates/partials/` en de lockup volgens de merkregels. Afzender Benjamin. Tags `{{ ... }}` zijn Klaviyo/Social Snowball; de aanmeldlink `[SIGNUP_URL]` en portal-URL `[PORTAL_URL]` komen uit de SS-instellingen.

---

#### Mail 1 · Uitnodiging (Delivered + 7 dagen, of na 5 sterren)

**Subject:** Give a friend 15% off your pan
**Preview:** And get 10% of what they pay, in cash.

**Hero:** LABEL `FOR FRIENDS` / `Give 15%.|Get 10% back.` / subline: `For anyone still on coated pans`

Hi {{ first_name|default:'there' }},

By now your pan has had its first egg. Maybe its first steak.

Here's something I hear a lot. Someone cooks for a friend, the friend picks up the pan, and asks where it's from. Usually followed by "what's it coated with?" Nothing. That's the point.

So we made it easy to pass on. Get your own link, and anyone who orders with it gets **15% off their first order**. When they do, you get **10% of what they paid**, in cash. Or 15% as Siraat store credit, if you'd rather put it toward a lid or a second pan.

What that looks like: a friend orders the Pan Pro Duo ($229). They pay $194.65. You get $19.47.

That's it. No quotas, no posting schedule. Most people share it with a friend or two, and that's exactly what it's for.

**[ Get my link ]**
`Takes about a minute. Your friend gets 15% off, free shipping and 30-day returns.`

What your friend gets, same as you did:
- A pure titanium cooking surface, no coatings. Tested free from PFAS by Light Labs, report no. 25895.
- A 75-year warranty.
- Free shipping and 30-day returns.

Benjamin
Founder, Siraat's Kitchen

P.S. If something isn't right with your pan, reply to this email instead. I'd rather fix that first.

<small>Commission is paid on new customers only, after their 30-day return window. Full terms: [TERMS_URL]. If you share your link publicly, say it's your referral link.</small>

Noten: woorden ~250 (klant, korte mail is P-niveau maar dit is een vraag, dus iets langer). Principes: reciprocity (je geeft je vriend iets), commitment (hun eerste ei, hun keuze), social proof via de vriendenvraag, authority (rapport). Geen verdienbelofte, alleen een rekenvoorbeeld per verkoop. De P.S. vangt ontevreden klanten op voordat ze spam klikken.

---

#### Mail 2 · Herinnering (+5 dagen, alleen geopend en niet ingeschreven)

**Subject:** Who asked about your pan?
**Preview:** Send them 15% off. You get 10% back.

**Hero:** LABEL `ONE LINK` / `Someone asked.|Send this.` / subline: `15% off for them, 10% back for you`

Hi {{ first_name|default:'there' }},

Short one. Last week I offered you a link that gives a friend 15% off.

If someone has already asked where your pan is from, this is the easy answer. If no one has, no problem. It'll come up the next time you cook for people.

Your friend gets 15% off their first order. You get 10% of what they pay, in cash, or 15% in store credit. On the $229 Pan Pro Duo that's $19.47 in cash or $29.20 in credit.

**[ Get my link ]**
`About a minute. Free shipping and 30-day returns for your friend.`

This is the last time I'll bring it up. The link stays available in your account if you want it later.

Benjamin

<small>Paid on new customers only, after their 30-day return window. Terms: [TERMS_URL].</small>

Noten: ~140 woorden. Belofte "last time" moet waar zijn (flowfilter: na mail 2 nooit meer een uitnodiging in 60 dagen, en de campagnegolven sluiten deze mensen uit). "In your account": alleen als SS een link op het klantaccount of de site toont [CHECK]; anders vervangen door "Just reply and I'll send it."

---

#### Mail 3 · Welkom en deelkit (na "Signed up as an affiliate" of "Enrolled through purchase" + levering)

**Subject:** Your link is ready
**Preview:** Here's what to send, word for word.

**Hero:** LABEL `YOUR LINK` / `Ready when|you are.` / subline: `15% off for friends, 10% back for you`

Hi {{ person|lookup:'Affiliate First Name'|default:'there' }},

Your link is set up. Here it is:

**{{ person|lookup:'Referral Link - SocialSnowball'|default:'' }}**

**[ Copy my link ]**  (knop naar de link zelf)

How it works, in three lines:
1. A friend opens your link. Their 15% off is applied automatically, with a code made just for them.
2. They order within 30 days. We track it back to you.
3. After their 30-day return window, you get {{ person|lookup:'Referral Reward - SocialSnowball'|default:'your commission' }}. You'll get an email the moment a sale comes in, and another when it's paid.

**What to send (copy, change, make it yours):**

Text message:
> "This is the pan I told you about. Pure titanium surface, no coating. Here's 15% off: [your link]. (It's my referral link, I get a little back if you order.)"

Instagram story or post, over a photo of something you cooked:
> "Made this on my titanium pan. No coatings, tested free from PFAS. 15% off with my link. #ad [your link]"

Email to a friend:
> "You asked what pan I use. It's from Siraat's Kitchen, a pure titanium cooking surface with no coatings. They test it for PFAS and publish the report (no. 25895). They also cover it with a 75-year warranty. My link gives you 15% off your first order: [your link]. Full disclosure, I get a small commission if you use it."

**A photo works better than words.** Your own pan, on your own stove, with real food on it. Eggs, a steak, whatever you made last night. Natural light or flash, both fine.

**Three rules, so this stays fair:**
- Say it's your referral link when you share it, especially in public posts. "#ad" or "my referral link" is enough.
- Only say what's true for you and what we can back up: no coatings, tested free from PFAS (report no. 25895), 75-year warranty, 30-day returns, free shipping. No health promises, please.
- No coupon sites, no paid ads on our name. Those sales don't count.

Your dashboard, with clicks, sales and payouts: **[ See my dashboard ]** ([PORTAL_URL])

Thank you for passing it on. It's how a small kitchen brand with 100,000+ happy customers keeps growing without shouting.

Benjamin

<small>Commission on new customers only. Paid after the 30-day return window. Earnings depend on how many friends order; most people refer one or two. Terms: [TERMS_URL].</small>

Noten: ~420 woorden, lang mag hier (handleiding, zoals P2). Principes: commitment (ze zeiden ja, nu de eerste stap), reciprocity, authority, liking (Benjamin). De deelkit bevat alleen claims uit `content/facts/claims.csv`, en de FTC-disclosure staat in elke kant-en-klare zin. "Earnings depend on..., most people refer one or two" is de typische-uitkomstregel. Bij "Enrolled through purchase" zonder levering de mail laten wachten tot Delivered Shipment.

---

### 6.5 Verwachting voor Siraat (eerste kwartaal) [schatting]

Uitgaande van ~6.000 orders per maand (200 per dag) en de filters uit 5.2:

| Bron | Bereik per maand | Inschrijving | Nieuwe affiliates per maand | Verkopen per kwartaal (bij 10 per 100) |
| --- | --- | --- | --- | --- |
| Uitnodiging + herinnering (flow) | ~3.500 betrokken, geleverde kopers zonder refund of ticket | 2 tot 5% | 70 tot 175 | 20 tot 50 |
| Blokken in P2, P3, reviewmail | dezelfde kopers, extra kans | +0,5 tot 1% | 20 tot 35 | 5 tot 10 |
| Golven bestaand bestand (betrokken kopers) | 20.000 tot 40.000 eenmalig | 2 tot 4% | 400 tot 1.600 eenmalig | 40 tot 160 |
| Bestaande 438 affiliates | | | | 5 tot 45 (afhankelijk van hoe ze erin kwamen) |

Orde van grootte: **70 tot 260 verwezen orders per kwartaal**, ofwel $14K tot $50K omzet bij ~$195 per order, naast ongeveer 18.000 gewone orders per kwartaal. Dat is 0,4 tot 1,4% van de orders, in lijn met de 2,35% branchegemiddeld voor volwassen programma's en onder de 10%-claims van de leverancier. Na 90 dagen bijstellen op echte cijfers.

### 6.6 Open punten voor Floris

1. Aanbod: 15% vriend / 10% cash of 15% store credit / 15% na 5 verkopen. Akkoord of anders?
2. Staat "automatisch affiliate bij aankoop" (thank-you-widget) aan in SS? Dan telt elke koper mee en moet de welkomstmail pas na levering.
3. Wie zijn de 438 huidige affiliates (creators, klanten via widget, import)? Bepaalt welke flow ze krijgen.
4. Kent SS een wachttijd voor commissies (lock period) tot na de 30-day returns?
5. Portal-URL en aanmeldpagina voor Siraat (de drafts linken naar een signup-pagina).
6. Afzender Benjamin voor de uitnodiging?
7. Blended CAC, om te bepalen of ~$60 per verwezen order goedkoop is.
8. Mag het "100,000+ ... most through a friend" (onderwerpregel 5) of is dat niet waar? Anders de alternatieve preview.
