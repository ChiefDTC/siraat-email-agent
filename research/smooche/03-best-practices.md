# Smooche-stijl kraskaart + founder-welkomstmail: best practices voor BFCM 2026

Desk research, 31 oktober 2026. Geen systemen aangeraakt. Bronnen zijn via WebSearch gevonden; WebFetch was in deze sessie geblokkeerd voor o.a. popupsmart.com, recart.com, help.klaviyo.com en asa.org.uk, dus cijfers komen uit zoekresultaat-samenvattingen en moeten voor een beslissing op de bronpagina zelf worden nagelezen. Bijna alle prestatiecijfers komen van popup-leveranciers met belang bij het resultaat: lees ze als richting, niet als bewijs.

Context uit de repo: de huidige pop-up is Alia "Card Game" (campagne "US | Evergreen"), belofte "Win your order for free" / kans op refund van je order (DECISIONS.md, 2026-10-07). Alle 35 Klaviyo-forms staan op draft.

---

## 1. Gamified pop-ups: wat levert het op?

### Signup-lift versus een klassieke "10% off"

| Bron | Bevinding | Kanttekening |
|---|---|---|
| Sleeknote 2026 (516M+ views) | Spin-to-win 8,67%, quiz 8,65%, geen gamification 3,70% | Leverancier |
| OptiMonk intern | Lucky wheel 13,23% vs. simpele kortingspop-up 7,65% | Leverancier |
| EasyApps | Spin wheel 7,4% vs. 2,8% standaard | Leverancier |
| Popupsmart 2026 benchmark | Spin-to-win krijgt veel meer clicks (7,33% vs. 1,87% van displays, mediaan), maar **geen meetbaar hoger aantal leads** dan een gewone signup-pop-up. Ook kortingshoogte gaf geen meetbaar verschil in leads | Belangrijkste tegengeluid: de "spin" telt als click |
| Justuno | Tijdens BFCM daalde de conversie van spin-to-win naar 6,5% (rest van het jaar 13,3%) | Gamification-lift slinkt als iedereen al korting geeft |
| Recart Conversion Lab (A/B tegen evergreen control) | Kraskaart gaf dubbelcijferige lift in e-mail en SMS opt-in bij body care en kaarsen, maar **verlaagde** opt-ins bij een beautymerk (e-mail -12%, SMS -14%), downstream neutraal | Dichtst bij een echte test; resultaat verschilt per vertical |
| Recart mystery-box test | Evergreen pop-up was voor sommige merken betrouwbaarder | |
| Retainful, Lavender World (Claspo), Email Shakeup | Mystery discount gaf hogere opt-in (bijv. 1,64% naar 2,2%; één merk naar 11,78%) | Sequentieel getest, geen gelijktijdige A/B |
| OptiMonk Sassy Scents | 10% converteerde meer bezoekers dan 15%, maar 15% gaf meer orders | Meet omzet per bezoeker, niet alleen signup-rate |
| Alia CEO (podcast) | "Je pop-up converteert waarschijnlijk op 8%, de beste Shopify-merken halen 15 tot 20%"; adviseert mystery discount vs. vaste % te testen | Pitch, geen data |

**Conclusie:** gamification verhoogt vrijwel altijd interactie, maar de lift in echte e-mails en vooral in omzet is onzeker en hangt af van vertical en periode. Tijdens BFCM, als de hele site al in de aanbieding staat, wordt het verschil kleiner. Test daarom zelf, gelijktijdig, met omzet per bezoeker als primaire metriek.

### Welke tools kunnen een kraskaart?

| Tool | Kraskaart | Notities |
|---|---|---|
| **Alia** (huidig) | Ja, volgens derden: mystery offers, scratch cards, spin-to-win, quizzen, "learn to earn". Siraat draait al het format "Card Game". Een tracker ziet in sept. 2026 een "mystery discount scratch popup" op Alia bij een merk | Vanaf ca. $100/maand. Bevestig in Alia-dashboard welke reveal-opties en kansverdeling per uitkomst mogelijk zijn. HexClad (directe concurrent) staat in Alia's klantenlijst |
| **Klaviyo forms** | **Nee.** Wel native spin-to-win: 1 wheel per form, minimaal 1 e-mail- of SMS-consentveld, moet op alle devices tonen, per slice een beloning en kans, success step per slice (segmenteerbaar via `$success_step_name`). Klaviyo zegt zelf: A/B-test tegen een standaard form en check lokale sweepstakes-wetgeving. Kraskaart alleen via third-party of AMP-mail | Gratis binnen Klaviyo |
| **OptiMonk** | Ja, grote kraskaart-bibliotheek | Gratis plan (10.000 pageviews), betaald vanaf $29/m |
| **Wheelio** | Ja (wheel, scratch card, slot machine) | Vanaf ca. $14,92/m, 7 dagen trial |
| **Popupsmart, Claspo, Wisepops, Scratcher** | Gamification-formats; Scratcher is specialist | Niet in detail geverifieerd |

**Advies tool:** blijf in Alia. Het draait al, schrijft al naar Klaviyo ($source "Alia sign-up") en ondersteunt de formats. Een tweede pop-up-app erbij tijdens BFCM is risico zonder voordeel. Klaviyo forms vallen af voor een kraskaart.

### BFCM best practices pop-up
- 3 tot 4 weken vooraf: teaser/VIP early access pop-up; 1 week vooraf: laatste lijstpush; tijdens BFCM: sitewide-offer pop-up plus cart/exit pop-up. Zet pop-ups tijdens de sale niet uit (Alia newsletter).
- Merken die geen extra korting willen geven: e-mail verzamelen met de sitewide-korting als belofte, eventueel quiz voor segmentatie (Alia).
- Tijdens de sale: early-access-boodschap vervangen door de live aanbieding, pop-up doorlaten lopen t/m Cyber Monday, niet over navigatie of content heen (Gleam, OptiMonk, Wisepops).

---

## 2. Juridisch: mag "scratch to see what you win" als iedereen hetzelfde krijgt?

Kort antwoord: **het kras-mechaniek zelf mag, de taal "you won" en schijnwillekeur niet.** Als iedereen 60% krijgt is het juridisch een **cadeau/aanbieding**, geen **prijs**. Het moet dan ook zo gepresenteerd worden. Extra punt dat vaak gemist wordt: een "gewonnen" korting die je alleen kunt gebruiken door iets te kopen, is in UK/EU een prijs waarvoor je kosten moet maken, en dat is daar per definitie oneerlijk.

### VS (FTC)
- FTC Act sectie 5: beoordeling op de "net impression" van het hele ontwerp. De FTC dark-patterns staff report (sept. 2022) noemt als misleidend: countdown timers op aanbiedingen die niet echt tijdgebonden zijn, valse "bijna uitverkocht" en "28 mensen hebben dit in hun mandje"-meldingen.
- Prijsacties: de FTC-handhaving tegen Publishers Clearing House (2023, $18M) ging over dark patterns die suggereerden dat aankoop de winkans verhoogt of nodig was. Eerdere zaken: valse "je hebt gewonnen"-brieven leidden tot permanente verboden op prize promotions.
- **"60% off"** moet een echte korting zijn ten opzichte van een prijs waartegen echt verkocht is (16 CFR 233.1, Guides Against Deceptive Pricing; staten zoals Californië passen dit actief toe in class actions). Een opgeblazen compare-at prijs is het grootste risico, niet de kraskaart.
- **"Win your order for free"**: als deelname een aankoop vereist, is dat consideration. Prijs + kans + consideration = illegale loterij. Oplossing: een gratis alternatieve deelnamemethode (AMOE) met gelijke kansen, officiële regels, en echte winnaars die je aantoonbaar trekt (Texas AG-opinie, Mondaq/Klein Moynihan). Eigen kennis, verifiëren met jurist: New York en Florida eisen registratie en borgstelling als de totale prijzenpot boven $5.000 uitkomt.
- Als e-mail opt-in de enige deelname-eis is (geen aankoop), is er meestal geen consideration. Dan blijven officiële regels, eerlijke trekking en het leveren van de prijs nodig.

### VK (CMA, ASA/CAP Code, DMCC Act)
- **CAP 8.19:** je mag niet zeggen dat deelnemers een prijs hebben gewonnen als dat niet zo is. Het verschil tussen een gift (voor iedereen of velen) en een prijs (voor enkelen) moet altijd duidelijk zijn.
- **CAP 8.20:** winkansen niet overdrijven.
- **CAP 8.21.1:** niet claimen dat iemand iets heeft gewonnen als hij kosten moet maken om het te claimen. Een "gewonnen" kortingscode die alleen bij aankoop werkt valt hieronder.
- **CAP 8.25:** instant-win moet eerlijk en willekeurig worden toegekend, met onafhankelijke verificatie. De ASA heeft "winning moment"-algoritmes onderzocht die maar een klein deel van de beloofde prijzen uitkeerden (2023: £500 van £125.000).
- ASA Bier Nuts: "giveaway" mag alleen als (bijna) alle deelnemers iets krijgen. "Everyone who enters is a guaranteed winner" werd problematisch gevonden.
- **DMCC Act 2024, Schedule 20** (sinds 6 april 2025, CMA kan zelf boetes tot 10% van de wereldomzet opleggen): vals beweren dat een product maar beperkte tijd beschikbaar is om tot een direct besluit te dwingen, staat op de zwarte lijst (altijd verboden, geen bewijs van effect nodig).
- CMA-zaken Emma Sleep, Simba, Wowcher: timers die herstarten bij refresh, valse "high demand"-meldingen en klokken die suggereren dat de prijs terugspringt terwijl dat niet gebeurt.
- Eigen kennis, verifiëren: een UK prize draw met verplichte aankoop is een loterij onder de Gambling Act 2005, tenzij er een gratis deelnameroute is.

### EU
- **UCPD Bijlage I punt 31** (altijd oneerlijk): de valse indruk wekken dat de consument een prijs heeft gewonnen, of dat er een prijs is terwijl de consument moet betalen of kosten moet maken om hem te krijgen. Het HvJ-EU (*Purely Creative*, C-428/11) noemt dit verbod absoluut, zelfs bij een postzegel of telefoontje. "You've won 60% off" (alleen bruikbaar bij aankoop) is dus juridisch zwak in de EU.
- Ook in Bijlage I: vals beweren dat een aanbod maar zeer beperkte tijd beschikbaar is.
- **Omnibus / Prijsaanduidingsrichtlijn art. 6a:** elke aangekondigde prijsverlaging ("60% off", maar ook "Black Friday deal") moet gerekend worden vanaf de laagste prijs van de afgelopen 30 dagen. Voor de hele campagne blijft die referentieprijs gelden. Gevolg: als de prijs in oktober al verlaagd was, mag je in november niet "60% off" vanaf de originele prijs roepen.

### Australië
- Trade promotion lottery-vergunningen bij prijzenpotten boven: ACT $3.000, SA $5.000, NSW $10.000 (VIC, TAS, QLD, WA meestal niet). Een spin-to-win met willekeurige prijzen geldt als kansspel-promotie (Sprintlaw, LegalVision, Lawpath). Daarnaast geldt de Australian Consumer Law (ACCC) tegen misleiding.
- Een kraskaart waarbij iedereen dezelfde korting krijgt, is geen loterij (geen kans). Dan is alleen de ACL van belang.

### Praktische regels om het eerlijk te doen

**Variant A: iedereen krijgt hetzelfde (aanbevolen voor BFCM)**
1. Geen "win", "won", "winner", "lucky". Gebruik "Scratch to reveal your Black Friday price", "Unlocked: 60% off".
2. Zeg vooraf, zichtbaar in de pop-up: "Every card reveals our Black Friday offer: 60% off" of "Everyone gets at least 60% off". Het krassen is dan een reveal, geen gok.
3. Geen nep-animatie die "bijna" een hogere prijs laat zien, geen draaiende cijfers die toevallig altijd op 60 stoppen.
4. 60% moet gelden tegen een echte eerdere prijs (VS) en tegen de laagste prijs van de laatste 30 dagen (EU). Controleer per markt.

**Variant B: echte verschillende uitkomsten**
1. Echte willekeurige toewijzing, kansen gepubliceerd ("60% off: 97%. Free Frying Pan: 2,5%. Order refunded: 0,5%"), en de prijzen worden echt uitgekeerd.
2. Laagste uitkomst duidelijk vermeld: "Everyone gets at least 60% off".
3. Officiële regels (looptijd, landen, leeftijd, totale prijzenpot, hoe winnaars bekend worden).
4. Geen aankoopplicht om mee te doen of om de prijs te claimen (anders UK 8.21.1 / EU punt 31 / US consideration). Een productprijs (gratis pan) die je zonder aankoop krijgt is veilig; een "prijs" die alleen bij aankoop waarde heeft, noem je een korting en geen gewonnen prijs.
5. Australië: let op de vergunningsdrempels per staat. NY/FL: registratie boven $5.000.

**Deadlines en voorraad**
- Countdown alleen als de aanbieding echt stopt op dat moment, voor iedereen dezelfde, en niet herstart bij refresh. Geen evergreen-timer per bezoeker.
- "No extensions" alleen zeggen als je het echt niet verlengt. Verlengen na "no extensions" is precies het CMA/FTC-patroon. Dit past ook bij de PLAYBOOK-regel: alleen echte countdowns.
- Lage voorraad alleen met echte voorraaddata (bijv. Shopify inventory < X), nooit hardcoded.

**Huidige giveaway "Win your order for free"**
- Als deelname alleen een e-mailinschrijving vereist: officiële regels publiceren, eerlijke trekking, winnaars echt uitkeren, en in de mail niet suggereren dat bestellen de kans vergroot (het PCH-patroon).
- Als winnen afhangt van een bestelling ("je order terugbetaald"): AMOE (gratis deelname per post of formulier, zelfde kans) in de VS, gratis route in UK, en per land/staat checken. Laat Floris dit door een jurist laten bekijken vóór BFCM.

---

## 3. Welkomstmail: timing en vorm

### Direct versus vertraagd
- Cheetah Digital: direct versturen gaf 78% hogere opens, dubbele clicks en 12x hogere transactieratio en omzet per mail dan later versturen.
- Copernica: ca. 75% opent als de mail op dag 1 komt, 13% na één dag, 7% na twee tot drie dagen.
- Stripo: exacte lift-cijfers verschillen per bron en komen zelden uit gecontroleerde tests. Richting is wel eenduidig: **direct**.
- Bij een kraskaart met code is direct nog belangrijker: de mail is de plek waar de code terug te vinden is.

### Platte founderbrief versus HTML
- HubSpot: e-mails met minder HTML-elementen wonnen significant (in één test 5,3% hogere CTR). GoDaddy-roundup: tekstversie bracht 194,5% meer bezoekers dan een beeldzware versie (100.000 ontvangers).
- Campaign Creators: HTML 2% hogere opens en 2,71% hogere CTR. Litmus: platte tekst hogere opens, iets lagere CTR.
- Conclusie: gemengd, publiek-afhankelijk. Platte tekst wint vaker op clicks bij relatie/persoonlijke mails, HTML vaker bij productverkoop met beeld. Zelf A/B testen met klik-naar-open en omzet per ontvanger.
- **Huisregel let op:** CLAUDE.md eist in elke mail de vaste header en footer. Uitzonderingen bestaan alleen voor affiliate-mails (Social Snowball) en de Mystery Gift-flow. Een platte founderbrief zonder header vraagt een nieuwe expliciete uitzondering van Floris. Alternatief binnen de regels: briefstijl-tekst (Benjamin, korte alinea's, één tekstlink of knop) binnen de vaste header en footer.

### Benchmarks
- Klaviyo welcome-flows: gemiddelde open rate ca. 51% (opgeblazen door Apple MPP), top performers bijna 10% placed order rate, revenue per recipient ca. $2,35 (Branvas, toegeschreven aan Klaviyo, niet geverifieerd). Volgens Branvas piekt de order-intentie rond mail 3, mail 1 ca. 0,8 tot 1,2%.
- Klaviyo 2025: gemiddeld 1,42% conversie op flows (top 10%: 4,93%). Klaviyo 2026: flows 2,11% placed order rate vs. campagnes 0,16% (Prospeo-samenvatting).
- Omnisend: welcome heeft de hoogste omzet per mail van alle flows ($6,16), ca. 3% conversie (Stripo, "directional").

### Aantal en spreiding tijdens BFCM
- Geen bron geeft een BFCM-specifiek getal. Klaviyo's voorbeeld spreidt over enkele dagen tot een week, met vertragingen om nieuwe abonnees niet te overladen.
- Eigen afleiding: tijdens BFCM 3 tot 4 mails in 4 tot 5 dagen, mail 1 direct (code + Benjamin), mail 2 na ca. 24 uur (bewijs/reviews + code), mail 3 op de echte deadline van de aanbieding. Nieuwe abonnees ontvangen ook de BFCM-campagnes: zet een smart sending- of flow-filter zodat ze niet op één dag een welcome-mail én twee campagnes krijgen.

### Auto-apply link versus code
- Shopify: `https://{shop}/discount/{CODE}?redirect=/collections/{handle}` zet een cookie; de korting wordt in de checkout toegepast. Ongeldige codes falen stil in de checkout. Redirect moet op het eigen domein zijn. Meerdere domeinen (UK/EU/AU) vragen extra aandacht omdat parameters behouden moeten blijven.
- Klaviyo waarschuwt dat de code niet altijd wordt toegepast als de site de parameter wegfiltert. Een oude Shopify Community-thread meldt problemen met redirect; altijd testen in een privévenster.
- Korting is pas in de checkout zichtbaar, niet op product- of collectiepagina, tenzij het thema of een app de prijs toont. Zet de code daarom **ook** zichtbaar in de mail (link + code, niet óf/óf).

---

## 4. Landing: collectie, product of homepage?
- Message match is de sterkste factor: de pagina moet de belofte uit pop-up/mail herhalen (ConvertFlow, Replo).
- Monetate (via CloudCart): bezoekers die direct op een productpagina landen, converteren half zo vaak als op een speciale landingspagina (1,5% vs. 2,9%). Vendorcijfers, richting.
- Collectiepagina = middenfunnel, voor wie nog moet kiezen; PDP = voor hoge intentie op één product (Replo). ConvertFlow waarschuwt dat een collectie met twintig producten bounce veroorzaakt.
- Homepage is het zwakste doel voor een specifiek aanbod.
- Voor Siraat: een korte BFCM-collectie of sets-pagina (weinig producten, sets bovenaan, 60%-prijs zichtbaar) voor de pop-up en welcome-mail 1. Product-specifieke mails (bijv. de pan uit een ad) direct naar de PDP. Homepage niet gebruiken.

---

## Wat ik zou testen (BFCM 2026)

1. **Pop-up (Alia, 50/50 gelijktijdig):** huidige Card Game "Win your order for free" vs. kraskaart "Scratch to reveal your Black Friday price, everyone gets 60% off". Primaire metriek: omzet per bezoeker binnen 7 dagen; secundair: opt-in rate, kwaliteit (bounce, afmeldingen). Start vóór de sale, zodat je basisdata hebt voordat de BFCM-dip (Justuno) erin zit.
2. **Taal in de reveal:** "Unlocked" i.p.v. "You've won" in alle markten. Niet testen tegen "won": dat is het juridische risico.
3. **Welcome mail 1, direct:** briefstijl van Benjamin binnen vaste header/footer (huisregel) vs. huidige designed W1. Metriek: klik-naar-open en placed order rate 72 uur. Platte variant zonder header pas na akkoord van Floris.
4. **Link:** auto-apply link naar BFCM-collectie + code zichtbaar in de tekst, per domein getest.
5. **Landing:** BFCM-collectie vs. bestseller-PDP voor pop-up-verkeer (alleen als het verkeer groot genoeg is; anders collectie).
6. **Vooraf afvinken:** 60% klopt t.o.v. echte eerdere prijs (VS) en laagste 30-dagenprijs (EU), deadline is echt en wordt niet verlengd, giveaway heeft regels en AMOE.

---

## Bronnen

**Gamification en tools**
- Popupsmart benchmark: https://popupsmart.com/blog/popup-best-practices
- Popupsmart community (18.648 campagnes): https://community.popupsmart.com/t/which-popup-elements-actually-drive-conversions-data-from-18-648-campaigns/500
- Sleeknote popup statistics 2026: https://sleeknote.com/?p=139710
- Wisepops popup stats: https://wisepops.com/blog/popup-stats
- OptiMonk spin-to-win: https://www.optimonk.com/?p=63469
- EasyApps spin wheel guide: https://easyappsecom.com/guides/shopify-spin-wheel-popup-guide
- Justuno spin-to-win: https://www.justuno.com/blog/how-to-create-spin-to-win-popups-that-convert/
- Recart scratch card test: https://recart.com/laboratory/gamified-popups-scratch-card
- Recart mystery sale test: https://recart.com/laboratory/mystery-sale-popup
- Scratcher / Dansk Outlet: https://www.casestudies.com/company/scratcher/case-study/last-minute-easter-campaign-for-the-win
- Retainful mystery discount: https://www.retainful.com/blog/email-signup-popup
- Claspo Lavender World: https://claspo.io/cases/from-1.6-to-21-cr-how-lavender-world-found-the-right-popup-mechanic/
- OptiMonk Sassy Scents: https://optimonk.com/sassy-scents-case-study
- Klaviyo spin-to-win help: https://help.klaviyo.com/hc/en-us/articles/34614633330075
- Klaviyo blog spin-to-win: https://www.klaviyo.com/blog/spin-to-win-opt-in-forms
- Klaviyo community, geen scratch-off: https://community.klaviyo.com/marketing-30/scratch-off-and-reveal-prizes-1677
- Sleeknote Alia alternatives: https://sleeknote.com/?p=139782
- Alia Shopify App Store: https://apps.shopify.com/alia
- Growave over Alia: https://www.growave.io/apps/alia
- 1800DTC Alia: https://resources.1800dtc.com/tool/alia
- Taylor Sicard tracker: https://taylorsicard.com/brands/topicals
- Alia CEO podcast: https://www.audible.fr/pd/B0H3PWKLS9
- OptiMonk vs Wheelio: https://www.optimonk.com/optimonk-vs-wheelio
- OptiMonk scratch card library: https://www.optimonk.com/popup-library/scratch-card
- Wheelio listing: https://open.store/shopify-apps/wheelio-first-interactive-exit-intent-pop-up
- Alia BFCM: https://shaan-alia.beehiiv.com/p/how-to-use-alia-during-bfcm
- Alia BFCM excitement: https://shaan-alia.beehiiv.com/p/create-excitement-for-bfcm-w-your-popup
- Alia BFCM help center: https://intercom.help/alia-help-center/en/articles/16543475-your-bfcm-resource-center
- Gleam Black Friday popup: https://gleam.io/faq/marketing-and-growth-strategies/lead-generation-and-email-marketing/high-converting-black-friday-popup
- OptiMonk Black Friday popups: https://www.optimonk.com/black-friday-popups
- Wisepops BFCM: https://wisepops.com/blog/how-to-use-wisepops-for-bfcm

**Juridisch**
- FTC dark patterns (samenvatting Venable): https://www.venable.com/insights/blogs/2022/09/the-ftc-brings-more-light-to-dark-patterns-in-new
- FTC dark patterns (Hunton): https://www.hunton.com/privacy-and-cybersecurity-law-blog/ftc-releases-report-on-dark-patterns
- PCH-zaak (Hogan Lovells): https://biopreviewuat.hoganlovells.com/en/publications/deceptive-sweepstakes-prompt-ftc-action-and-consumer-payouts
- FTC PCH order: https://www.ftc.gov/system/files/ftc_gov/pdf/1823145pchorder.pdf
- FTC prize promotion ban: https://www.ftc.gov/node/85679
- 16 CFR 233: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-233
- Hobby Lobby phantom markdowns (BCLP): https://www.bclplaw.com/en-US/events-insights-news/beware-of-phantom-price-markdowns-ruling-against-hobby-lobby-highlights-risk.html
- Texas AG opinie sweepstakes: https://www2.texasattorneygeneral.gov/opinions/opinions/48morales/lo/1997/htm/lo1997008.htm
- Klein Moynihan, purchase to enter: https://kleinmoynihan.com/can-a-sweepstakes-require-a-purchase-to-enter-sweepstakes-attorney
- Mondaq AMOE: https://mondaq.co.uk/unitedstates/gaming/1307834/the-sweepstakes-amoe-in-a-nutshell
- ASA instant wins: https://www.asa.org.uk/advice-online/promotional-marketing-instant-wins.html
- ASA gifts vs prizes: https://www.asa.org.uk/Advice-Training-on-the-rules/Advice-Online-Database/Sales-Promotions-Gifts-v-Prizes.aspx
- ASA Kettle Foods: https://www.asa.org.uk/Rulings/Adjudications/2015/9/Kettle-Foods-Ltd/SHP_ADJ_301864.aspx
- CAP Code promotional marketing (pdf): https://www.asa.org.uk/static/ebac4f60-60a0-444b-916b515359968fdc/0f61dabf-c8cf-4268-90b503336e133241/The-CAP-Code-Promotional-marketing.pdf
- Lewis Silkin, Bier Nuts: https://adlaw.lewissilkin.com/post/102h43l/you-didnt-have-to-be-nuts-to-believe-this-promotion-was-genuine-but-it-helped
- CMS, online choice architecture: https://cms.law/en/int/legal-updates/tangled-web-uk-regulators-crack-down-on-harmful-online-choice-architecture
- CMA Emma (HSF Kramer): https://www.hsfkramer.com/notes/tmt/2024-posts/CMA-takes-court-action-against-Emma-Group-for-misleading-consumers
- CMA Simba (RPC): https://www.rpclegal.com/snapshots/consumer/autumn-2024/cma-targets-simba-for-misleading-online-choice-architecture/
- Gowling 2026, CMA: https://gowlingwlg.com/insights-resources/articles/2026/misleading-sales-practices-dont-sleep-on-the-cma
- Which? DMCC banned practices: https://www.which.co.uk/consumer-rights/regulation/consumer-protection-from-unfair-trading-regulations-2008
- Business Companion, unfair trading vanaf april 2025: https://www.businesscompanion.info/en/quick-guides/fair-trading/protection-from-unfair-trading-from-april-2025
- DWF over DMCC: https://dwfgroup.com/en/news-and-insights/insights/2024/1/ct24-the-dmcc
- UCPD Annex I: https://www.legislation.gov.uk/eudr/2005/29/annex/I/adopted
- Purely Creative (European Law Blog): https://www.europeanlawblog.eu/pub/the-cjeu-overshoots-the-mark-of-consumer-protection-winner-means-winner-and-prize-means-free-prize-c-42811
- CMS over Purely Creative: https://cms.law/en/gbr/legal-updates/luxury-car-not-a-prize-if-winner-has-to-buy-a-bus-ticket-to-collect-it-cjeu-claims
- UOKiK Black Friday prijzen: https://uokik.gov.pl/en/w-black-friday-jasne-ceny
- Talon.One EU price reductions: https://www.talon.one/blog/eu-requirements-for-advertising-with-price-reductions
- CMS NL prijsverlagingen: https://cms.law/en/nld/publication/netherlands-to-issue-new-rules-on-price-reduction-announcements
- LegalVision AU permits: https://legalvision.com.au/permits-need-run-trade-promotion-lottery
- Lawpath AU state-by-state: https://lawpath.com.au/blog/competition-permits-a-state-by-state-breakdown/2
- Sprintlaw AU game of chance: https://sprintlaw.com.au/articles/game-of-chance-promotions-legal-requirements-permits-and-best-practices/

**Welkomstmail en landing**
- Cheetah Digital welcome metrics: https://www.cheetahdigital.com/blog/delicious-metrics-hidden-in-welcome-email-data
- Copernica welcome: https://www.copernica.com/en/news/post/5-dos-for-an-effective-welcome-campaign
- Stripo welcome research: https://research.stripo.email/welcome-email-open-rates
- Branvas welcome sequence benchmark: https://branvas.com/blogs/news/welcome-email-sequence-benchmarks
- Klaviyo benchmarks: https://klaviyo.com/blog/ecommerce-benchmarks-2021
- Prospeo (Klaviyo 2026 data): https://prospeo.io/s/email-campaign-examples
- Klaviyo welcome series help: https://help.klaviyo.com/hc/en-us/articles/115002775172-Creating-a-Welcome-Series
- Klaviyo community welcome best practices: https://community.klaviyo.com/strategic-advice-27/how-to-build-a-welcome-series-in-klaviyo-best-practices-and-tips-15891
- HubSpot plain text vs HTML: https://blog.hubspot.com/marketing/plain-text-vs-html-emails-data
- Litmus A/B HTML vs plain: https://www.litmus.com/blog/the-results-are-in-a-b-testing-html-vs-plain-text-emails
- Campaign Creators: https://www.campaigncreators.com/blog/html-vs-plain-text-emails
- GoDaddy plain text ecommerce: https://www.godaddy.com/resources/skills/plain-text-emails-ecommerce
- Shopify shareable discount links: https://www.shopify.ca/blog/shareable-discount-links
- Klaviyo coupon link Shopify: https://help.klaviyo.com/hc/en-us/articles/115005253088-How-to-add-link-that-applies-a-coupon-code-to-a-Shopify-cart
- Shopify Community redirect issue: https://community.shopify.com/t/discount-applying-at-cart-level-when-website-accessed-via-discount-link/271573
- Replo landing vs collection vs PDP: https://www.replo.app/blog/landing-page-vs-collection-page-vs-pdp
- ConvertFlow Klaviyo landing pages: https://www.convertflow.com/blog/klaviyo-landing-pages
- CloudCart (Monetate-cijfer): https://blog.cloudcart.com/articles/how-to-create-high-converting-landing-pages-for-your-online-store-what-the-gurus-dont-tell-you-4-5
