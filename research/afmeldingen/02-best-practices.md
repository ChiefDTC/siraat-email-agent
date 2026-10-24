# 02 · Afmeldingen en spamklachten: best practices van buiten

Datum: 24 oktober 2026. Extern deel van het onderzoek naar afmeldingen en spamklachten. Een ander stuk levert de eigen Klaviyo-analyse; dit stuk vat samen wat benchmarks, inboxproviders, Klaviyo zelf en case studies zeggen, en vertaalt dat naar maatregelen voor Siraat.

**Werkwijze en beperking.** Gezocht met WebSearch (ongeveer 35 zoekvragen). WebFetch kon in deze sessie geen enkele site openen (klaviyo.com, help.klaviyo.com, omnisend.com en andere werden door de proxy geweigerd). Alle cijfers komen dus uit zoekresultaten en samenvattingen van de pagina's, niet uit eigen lezing van de volledige pagina. Waar een cijfer alleen via een tweede bron te vinden was, staat dat erbij. Herbekijken voordat een cijfer extern gebruikt wordt.

**Labels in dit stuk.**
- **[Officieel]**: Google, Yahoo of Klaviyo-documentatie over hun eigen regels of product.
- **[Vendor]**: cijfer of claim van een partij die er iets aan verkoopt (ESP, agency, tool). Richtinggevend, niet onafhankelijk getoetst.
- **[Onderzoek]**: peer-reviewed of groot panel-/datasetonderzoek.
- **[Anekdote]**: losse ervaring, forum, community.

## Kern in zes punten

1. **Siraat zit ver boven elke benchmark.** Per mail ligt een normaal afmeldpercentage voor e-commercecampagnes rond 0,2 procent en voor flows rond 0,4 tot 0,9 procent. Spam hoort onder 0,1 procent per verzending te blijven, en Klaviyo noemt alles boven 0,05 procent al "needs attention". De eigen cohortcijfers (19 procent van de giveaway-aanmelders uitgeschreven in 30 dagen, 0,8 procent met minstens één spamklacht; zie `research/lijstkwaliteit/01-giveaway-instroom.md`) zijn cohortcijfers en niet direct vergelijkbaar met cijfers per verzending. Ze wijzen wel op hetzelfde: te veel mail naar mensen die niet reageren.
2. **De belangrijkste oorzaak volgens alle bronnen is frequentie en relevantie, niet de inhoud van één mail.** In het Litmus/Fluent-onderzoek noemt 57 procent "te veel of irrelevante mail" als reden om op spam te klikken. 50 procent zegt dat ze op spam klikken omdat afmelden niet makkelijk ging.
3. **Mailen naar engaged segmenten is de grootste hefboom, en sunsetten de tweede.** Er is geen onafhankelijk gecontroleerd onderzoek naar, maar het advies is eensgezind (Google, Yahoo, Klaviyo, deliverability-specialisten), en de enige case met cijfers (agency, footwear) laat spam dalen van 0,4 naar minder dan 0,08 procent.
4. **Na Apple MPP is "geopend" geen bruikbaar teken van activiteit.** Definieer actief als: klik, site-activiteit (Active on Site, Viewed Product), aankoop, of een niet-Apple-open. Klaviyo heeft hiervoor het filter "Apple Privacy Open = False".
5. **Een "minder mail" of "pauzeer"-optie houdt een deel van de afmelders vast**, maar de cijfers erover (minus 82 procent afmeldingen met snooze, minus 76 procent met een preference center) zijn vendor-claims zonder methode. Klaviyo heeft geen ingebouwde pauzeknop; dat moet je bouwen met een profieleigenschap en segmenten.
6. **Minder mail is niet gratis.** De enige gedocumenteerde frequentieverlaging (catalogusverkoper van 2 naar 1 per week) hield de afmeldingen gelijk en liet de omzet sterk dalen. Daarom: niet minder mailen naar iedereen, maar minder naar wie niet reageert, en altijd met een holdout testen.

---

## 1. Benchmarks

Let op de definitie. Benchmarks zijn bijna altijd **per verzending** (afmeldingen gedeeld door afgeleverde mails), niet per profiel over een periode. De eigen cohortcijfers van Siraat zijn van de tweede soort.

### 1.1 Afmeldingen per mailtype

| Mailtype | Afmeldpercentage per mail | Bron, jaar | Label |
|---|---|---|---|
| Campagnes, alle sectoren | 0,20% | Omnisend, data 2025 (20 mrd campagnemails, 27.000+ merken) | [Vendor] |
| Automations (alle flows) | 0,59% | Omnisend, data 2025 | [Vendor] |
| Campagnes, e-commerce | 0,19% (alle sectoren 0,22%) | Mailchimp-benchmarks, bijgewerkt dec 2023, via tweede bron | [Vendor] |
| Campagnes, e-commerce (oudere Mailchimp-data) | 0,27% | Mailchimp, oudere publicatie, via tweede bron | [Vendor] |
| Welcome | 0,87% | Omnisend, via tweede bron | [Vendor] |
| Welcome | 0,08% (zorg boven 0,15%) | Branvas, 2026 | [Vendor], lijkt erg laag |
| Abandoned cart | 0,45% | Omnisend, via tweede bron | [Vendor] |
| Abandoned cart | 0,04% (zorg boven 0,10%) | Branvas, 2026 | [Vendor], lijkt erg laag |
| Order follow-up | 0,86% | Omnisend, via tweede bron | [Vendor] |
| Winback (late stappen) | 0,25 tot 0,50% | Branvas en Retention Side, 2026 | [Vendor] |
| Flows tegenover campagnes, portfolio | 0,60% tegenover 0,18% | BS&Co, januari 2026 | [Vendor] |
| E-commerce algemeen | 0,20 tot 0,30% | Opensend | [Vendor] |

Klaviyo publiceert zelf geen openbare afmeldcijfers per flowtype. In het account staan onder **Analytics > Benchmarks > Flows** wel de afmeld- en spampercentages per flow tegenover een peergroep van ongeveer 100 vergelijkbare bedrijven (top 25 procent, mediaan, onderste 25 procent). **Dat is voor Siraat de beste vergelijking**, beter dan de publieke cijfers hierboven, die sterk uiteenlopen (welcome: 0,08 tegenover 0,87 procent). Klaviyo's eigen benchmarkpublicaties (2024 Benchmark Report over 2023, het 2025-rapport en het abandoned-cart-onderzoek over 143.000 flows) gaan over omzet per ontvanger, klik en conversie, niet over afmeldingen.

**Lezing.** Flows hebben normaal twee tot vier keer zo veel afmeldingen per mail als campagnes, vooral welcome en post-purchase: dat zijn de eerste mails die iemand krijgt. Een welcome-mail met 0,5 tot 1 procent afmeldingen is dus niet alarmerend. Een campagne boven 0,3 procent wel.

### 1.2 Drempels

| Metric | Gezond | Aandacht | Probleem | Bron | Label |
|---|---|---|---|---|---|
| Spam (per mail) | < 0,01% | 0,01 tot 0,05% | > 0,05% | Klaviyo, Deliverability-tab in campagnes en flows | [Officieel] |
| Afmelding (per mail) | < 0,3% | 0,3 tot 1% | > 1% | Klaviyo, idem | [Officieel] |
| Bounce | < 1% | 1 tot 2% | > 2% | Klaviyo, idem | [Officieel] |
| Spam gemeld door Gmail-gebruikers | < 0,1% | 0,1% schaadt inboxplaatsing | > 0,3%: geen recht meer op "mitigation" | Google, Email sender guidelines FAQ | [Officieel] |
| Spam Yahoo | < 0,1% | | > 0,3% | Yahoo, via Bird en Resend | [Officieel], via tweede bron |

Let op: de spamcijfers in Klaviyo zijn ondertellingen. Gmail geeft geen klachten per adres terug (alleen in Postmaster Tools, als percentage per dag), en Apple Mail ook niet. **Google Postmaster Tools** is dus de echte meter voor Gmail. Klaviyo houdt campagnes ook zelf in de gaten en kan een account pauzeren bij hoge spam- of bouncepercentages (anti-abuse monitoring).

---

## 2. Sunset- en re-permissionmails

### 2.1 Werken ze?

Ja, maar vooral **voor de deliverability van de rest van de lijst**, en minder als manier om mensen terug te winnen.

- **Return Path (nu Validity), ongeveer 2014, 300 miljoen mails, 100 miljoen abonnees** [Vendor, groot]: meer dan 25 procent van de adressen was inactief. Winbackmails werden door 12 procent gelezen (gewone mails: 14 procent). **Re-permissionmails ("bevestig dat je wilt blijven") scoorden slecht: 1,8 procent gelezen.** 45 procent van de ontvangers las later weer een mail van het merk, gemiddeld na 57 dagen, vaak zonder de winbackmail zelf te lezen. Afzenders die het meest naar inactieven mailden, kregen het meest geblokkeerd of in spam gezet. Advies van de auteurs: niet direct na één winbackmail verwijderen. Cijfers zijn oud; het mechanisme geldt nog.
- **Elite Brands, footwear retailer** [Vendor, agency-case]: spam van 0,4 naar minder dan 0,08 procent en CTR van 1,2 naar 3,5 procent, na een re-engagementflow voor profielen zonder activiteit in 180+ dagen en suppressie van wie niet reageerde.
- **NR10, Shopify-merk** [Vendor]: lijst van 50.318 naar 33.027 profielen in 14 dagen, Klaviyo-kosten van $545 naar $375 per maand, spam 0,04 naar 0,03 procent. 10.000 kopers zijn teruggehaald in plaats van verwijderd.
- **GrowPronto** [Vendor, zonder data]: een re-engagementflow haalt 5 tot 10 procent van de inactieven terug.
- **phpList re-opt-in** [Vendor]: 13 procent van de ontvangers opende, 40 procent daarvan bleef. Dus ongeveer 5 procent van de ontvangers.

**Conclusie.** Reken op 5 tot 10 procent die terugkomt. De waarde zit vooral in de 90 procent die je daarna niet meer mailt: minder spamklachten, betere inboxplaatsing voor kopers, lagere Klaviyo-kosten.

### 2.2 Copy en ontwerp

Er zijn geen gecontroleerde tests naar specifieke formuleringen gevonden. Wat wel onderbouwd is:

- **Onderwerpregel.** Bij Return Path scoorden "miss you" (13 procent gelezen) en "come back" (12,7 procent) beter dan procentkorting (11 procent). **Een vast bedrag korting scoorde het hoogst: 21 procent**, maar werd weinig getest. Breakup-onderwerpen ("Closing the loop", "Should we stop emailing you?") zijn gangbaar en eerlijk; ActiveCampaign en SendGrid gebruiken ze als voorbeeld. [Vendor]
- **Eén duidelijke hoofdactie.** SendGrid: één doel, één vraag ("Wil je onze mails nog?"). Kies je voor twee knoppen, maak "blijf" dan de primaire knop en de andere secundair. [Vendor]
- **Een derde optie: "minder mail".** Volgens een Return Path-medewerker hielden sommige klanten tot 50 procent vast van mensen die zich wilden afmelden, door voorkeuren aan te bieden. [Vendor]
- **Persuasief plus informatief.** Onderzoek naar 1.506 re-permissionmails van 1.396 bedrijven (Journal of Marketing, Bocconi): alleen informeren verhoogt het aantal opt-ins niet significant; een mix van overtuigen (wat je mist, waarom het de moeite waard is) en informatie werkt wel. [Onderzoek]
- **Afmeldknop zichtbaar, eventueel bovenaan.** Er is geen gecontroleerde test die aantoont dat een link bovenaan beter werkt dan in de footer. Experts zeggen "it depends" (MediaPost), en adviseren het vooral bij hoge klachtcijfers bij een provider. Wel bewezen: wie niet makkelijk kan afmelden, klikt op spam (50 procent bij Litmus/Fluent). In een sunsetmail, waar afmelden het gewenste alternatief voor spam is, is een zichtbare link bovenaan logisch. [Vendor]
- **Toon.** De oprichter die persoonlijk schrijft, kort en zonder schuldgevoel. Dat past bij de platte brieven van Benjamin die Siraat al heeft (affiliate-uitzondering). Let op: voor sunsetmails geldt de vaste header en footer, tenzij Floris een uitzondering maakt.

**Voorstel voor de opbouw (te testen):**
1. Onderwerp: "Should we stop emailing you?" of "Still want to hear from Benjamin?"
2. Bovenaan, klein: "Not for you anymore? Unsubscribe in one click."
3. Twee zinnen van Benjamin: wat je mist (75-year warranty, recepten, de beste aanbiedingen) en eerlijk dat we stoppen als je niet reageert.
4. Primaire knop: "Yes, keep me on the list". Secundaire knop: "Only send me the big sales" (zet een eigenschap, zie 3.1).
5. Eventueel een vast bedrag als bedankje, maar alleen in mail 2 of 3 en alleen bij oud-kopers (zie 2.3).

### 2.3 Aantal mails en timing

| Bron | Advies | Label |
|---|---|---|
| Klaviyo Help Center, Create a sunset flow | Maximaal 3 mails. Na de laatste een korte wachttijd (ongeveer 3 dagen bij dagelijkse verzenders, langer bij minder frequente). Flowfilter: wie opent of klikt tijdens de flow, valt eruit. Wie de hele flow doorloopt, krijgt een tag en wordt gesuppresst. | [Officieel] |
| Klaviyo Help Center, prebuilt Sunset-segment | Marketing-eligible, profiel minstens 180 dagen oud, recent mail ontvangen, nooit geopend (oud; voor MPP vervangen door klikcriterium) | [Officieel] |
| Diverse agencies | 2 tot 3 mails, enkele dagen tussenruimte; of 3 mails in 21 dagen | [Vendor] |
| Klaviyo Academy, winback | Wachttijd langer dan de gemiddelde aankoopcyclus, of datumgestuurd op voorspelde volgende orderdatum | [Officieel] |

**Advies voor Siraat:** 3 mails in ongeveer 10 tot 14 dagen (dag 0, dag 4, dag 9), daarna 3 tot 5 dagen wachten en dan taggen en suppressen.

### 2.4 Hoe definieer je inactief na Apple MPP?

- **Klaviyo** [Officieel]: voorbeeld van een engaged segment is "geopend of geklikt in de laatste 30 dagen, **zonder MPP-opens**, of aangemeld in de laatste 15 dagen". In de segmentbouwer: Opened Email waar Apple Privacy Open = False. Klaviyo waarschuwt dat de vlag alleen zegt dat het een machine-open *kan* zijn.
- **Specialisten** [Vendor]: klik als hoofdsignaal, plus site-activiteit en aankoop. Vensters van 90 dagen (wekelijkse verzenders) tot 180 dagen totale inactiviteit. Spam Resource (Al Iverson) wijst erop dat opens ook na MPP nog iets zeggen, zolang je niet alleen op opens vertrouwt.
- **Eigen data Siraat**: 77 procent van alle opens is een machine-open (research/lijstkwaliteit/01). Opens zijn dus vrijwel waardeloos als signaal.

**Advies.** Actief = in de laatste X dagen minstens één van: klik op een mail (zonder Bot Click), Active on Site of Viewed Product, Placed Order, of een open met Apple Privacy Open = False. Let op de valkuil uit de Klaviyo-community: "OR active on site" kan profielen meenemen die nooit zijn aangemeld; combineer altijd met "can receive email marketing".

### 2.5 Wanneer suppressen?

- Pas na een sunsetflow en niet direct na één mail (Return Path: 85 procent van de mensen die na een winback stopten, had die mail wel gelezen).
- Alleen lijsten en segmenten sunsetten die je echt wilt suppressen (Klaviyo).
- Suppressie in Klaviyo geldt alleen voor e-mail; SMS-toestemming blijft staan (Klaviyo-community).
- **Differentiëren naar waarde** (Practical Ecommerce) [Vendor]: nooit-kopers sneller (bij Siraat: 60 tot 90 dagen zonder klik, voor giveaway-aanmelders 30 tot 45 dagen), oud-kopers later (180 dagen), en hoogwaardige kopers na suppressie nog bereiken via betaalde media (custom audience) of SMS.
- Suppressie is omkeerbaar: suppressed profielen tellen niet mee voor de Klaviyo-prijs en kunnen terugkomen bij een nieuwe aanmelding of aankoop.

---

## 3. Afmeldingen voorkomen

### 3.1 Preference center: frequentie, pauze, alleen sales, SMS

**Wat Klaviyo standaard kan** [Officieel]:
- De gehoste Manage Preferences-pagina kan lijsten tonen en vragen stellen. Klaviyo beschrijft zelf een vraag met keuzerondjes ("daily / weekly / monthly") die in een profieleigenschap wordt opgeslagen. Die eigenschap gebruik je in campagnesegmenten (help-artikel "Create email frequency segments").
- Afmeldpagina en voorkeurenpagina kunnen samen gebruikt worden om mensen hun voorkeuren te laten aanpassen in plaats van zich helemaal af te melden.
- Sinds de vernieuwing van de consent-pagina's (november 2022) kun je iemand van de afmeld- of voorkeurenpagina naar de SMS-aanmeldpagina sturen.
- Er bestaat **geen ingebouwde pauzeknop**. Werkwijze uit de community: profieleigenschap `snooze_until`, segment "snoozed", dat segment uitsluiten van campagnes. Een segment-getriggerde flow kan iemand maar één keer laten instromen; werk daarom met een datum-eigenschap in plaats van een flow. [Anekdote]
- Volledig eigen pagina's (custom hosted pages) kunnen alleen op betaalde, geverifieerde accounts en zonder support van Klaviyo.

**Wat het oplevert** (allemaal [Vendor], geen methode bekend):
- Oracle: een snooze-optie "verlaagt afmeldingen doorgaans met 82 procent", bij een klein aantal eigen klanten. Litmus noemt het "gemiddeld 82 procent", wat sterker klinkt dan de bron.
- Single Grain via Litmus: e-commerceklant met getrapt preference center, 76 procent minder afmeldingen en 189 procent meer engagement. Origineel niet gevonden.
- Digioh: "tot 30 procent minder afmeldingen".
- Bloom & Wild (Econsultancy, Braze) [Vendor, case]: bijna 18.000 klanten kozen ervoor om geen Moederdag-mails te krijgen. Volgens het bedrijf hadden die klanten 1,7 keer zo hoge lifetime value. Dit laat zien dat een opt-out voor één onderwerp klanten vasthoudt in plaats van verliest.

**Advies voor Siraat:** in de voorkeurenpagina drie opties bovenaan, vóór "unsubscribe from all":
1. "Only sales and new launches" (ongeveer 2 tot 4 mails per maand)
2. "Pause for 30 days"
3. "Everything" (huidige frequentie)
Plus, als Siraat SMS heeft: "Text me only the big sales".

### 3.2 Frequency capping en Smart Sending

- **Smart Sending** [Officieel]: standaard 16 uur voor e-mail (SMS en push 24 uur), per kanaal apart in te stellen onder de accountinstellingen. Staat standaard aan voor campagnes en voor alle flowmails behalve de voorgebouwde abandoned cart. Klaviyo raadt aan Smart Sending aan te laten voor campagnes. Een wijziging van het venster werkt niet met terugwerkende kracht. A/B-tests die door Smart Sending geen resultaat opleveren, worden automatisch afgebroken.
- Smart Sending is een **minimum** en geen weekplafond. Een echte cap (bijvoorbeeld maximaal 3 marketingmails per 7 dagen) bouw je met een segment "Received Email at least 3 times in the last 7 days" dat je uitsluit van campagnes.
- Eigen data: sinds 4 september gingen 7 campagnes uit met Smart Sending uit (research/lijstkwaliteit/01). Dat is tegen het advies van Klaviyo in.
- Langer venster dan 16 uur: geen officieel advies gevonden. Agencies zetten het voor campagnes vaak op 24 tot 48 uur in drukke periodes.

### 3.3 Verwachtingen scheppen bij aanmelding

- Litmus/Fluent: de belangrijkste reden voor spamklachten is te veel of irrelevante mail (57 procent). Kentico: 38 procent zegt mail van bekende bedrijven als spam te melden omdat er te vaak gemaild wordt, tegenover 34 procent omdat het ongevraagd is. MarketingSherpa (2008): 50 procent vindt te veel mail van bekende bedrijven ook spam.
- Advies: in de pop-up en in de eerste zin van W1 zeggen hoe vaak er mail komt en waarover ("2 to 3 emails a week: recipes, care tips and our best deals"). Bij een giveaway expliciet maken dat inschrijving ook betekent dat je merkmail krijgt (Klaviyo-advies voor giveaway-lijsten: in de eerste mail herinneren hoe iemand zich heeft aangemeld).

### 3.4 Giveaway- en contestaanmelders

- **Klaviyo-community en ViralSweep** [Anekdote, Vendor]: double opt-in wordt aangeraden om bounce, spam en afmeldingen bij giveaway-lijsten te verlagen. Klaviyo zet double opt-in standaard aan op nieuwe lijsten; de bevestigingslink is 72 uur geldig (Klaviyo Help Center, Franse versie).
- **Yahoo** vraagt afzenders om confirmed opt-in te gebruiken [Officieel, via tweede bron].
- **Nadeel**: een deel bevestigt nooit, dus kleinere lijst en minder W1-omzet. Geen bron kwantificeert dat. Siraat haalt veel omzet binnen 24 uur na aanmelding (10,2 procent van de Alia-giveaway-aanmelders koopt binnen 24 uur, research/lijstkwaliteit/01). **Een harde double opt-in kan die omzet raken en is daarom niet het eerste middel.**
- **Alternatief met minder omzetrisico**: een kortere "proefperiode" voor giveaway-aanmelders. Welcome-flow laten lopen, campagnes alleen naar wie in 14 dagen klikt of koopt, en wie na 30 dagen niets heeft gedaan direct de sunsetflow in. De eigen data ondersteunen dat: de 81 procent die in 14 dagen niets doet, levert 67 procent van de afmeldingen en 76 procent van de spamklachten in dag 14 tot 30.
- Prijs aan het product koppelen (een Siraat-pan winnen in plaats van iets generieks) trekt relevantere aanmelders [Vendor].
- Duitsland en Oostenrijk vereisen double opt-in wettelijk (vendor-bron). Relevant als niet-US-aanmelders daar vandaan komen.

### 3.5 Segmentatie op engagement voor campagnes

- **Klaviyo** [Officieel]: nieuwe accounts krijgen standaard engaged segmenten van 30, 60 en 90 dagen. De Academy-cursus "Strengthen your sender reputation" leert een engagement-gebaseerd verzendschema: breed naar recent actieven, smaller naar minder actieven. Bij problemen met één inboxprovider: 3 tot 5 campagnes lang de minst actieve ontvangers bij die provider overslaan.
- **Gangbaar schema** (agencies, community): 30 dagen voor dagelijkse verzenders, 60 tot 90 dagen voor 2 tot 3 per week, en af en toe (grote sales) 180 dagen. Nooit naar de hele lijst zonder filter.
- **Eigen data**: 16 campagnes sinds 4 september gingen naar de volledige Email List of "EB | US Subscribers" zonder engagementfilter.
- **Klaviyo-segmentpagina** [Vendor, eigen product]: relevante mail maakt afmelden en spam minder waarschijnlijk, maar Klaviyo geeft er geen cijfers bij.

### 3.6 Gmail en Yahoo sinds 2024

| Regel | Status | Gevolg voor Siraat |
|---|---|---|
| SPF, DKIM, DMARC (minstens p=none), aligned | Verplicht voor bulkverzenders (5.000+ per dag naar Gmail). Afwijzing vanaf april 2024 | Controleren in `research/deliverability/01-inbox-check.md` |
| One-click unsubscribe (RFC 8058, List-Unsubscribe-Post) | Verplicht voor marketingmail. Handhaving vanaf juni 2024 | Klaviyo voegt de header automatisch toe aan elke mail [Officieel]. Zichtbare link in de mail blijft nodig |
| Afmelding binnen 2 dagen verwerken | Verplicht | Klaviyo doet dit direct |
| Spam < 0,3% (Postmaster Tools) | Boven 0,3%: geen "mitigation" meer. Boven 0,1%: al slechtere inboxplaatsing | **Het echte doel is < 0,1%.** Postmaster Tools wekelijks bekijken |
| Gmail "Manage subscriptions" (aangekondigd 8 juli 2025) | Overzicht van afzenders, gesorteerd op hoe vaak ze mailen, met afmelden in één klik | Wie vaak mailt, staat bovenaan. Verwachting: meer afmeldingen bij weinig betrokken abonnees; afmelden is wel beter dan spam (blokkeren stuurt mail naar spam en meldt niet af) |

---

## 4. Case studies met cijfers

| Merk of studie | Wat ze deden | Resultaat | Label en kanttekening |
|---|---|---|---|
| Footwear retailer (Elite Brands) | Re-engagementflow voor 180+ dagen inactief, daarna suppressie | Spam 0,4% naar < 0,08%, CTR 1,2% naar 3,5% | [Vendor] agency-case, onbekend merk |
| Fashionmerk (Elite Brands) | 80.000 inactieve profielen gesuppresst via sunsetflow | Opens campagnes boven 25% | [Vendor], geen spamcijfer |
| Shopify-merk (NR10) | Opschoning in 14 dagen, 10.000 kopers via re-permission behouden | Profielen 50.318 naar 33.027, kosten $545 naar $375 per maand, spam 0,04% naar 0,03% | [Vendor] |
| Bloom & Wild (2019) | Opt-out voor Moederdag-mails | Bijna 18.000 opt-outs in plaats van afmeldingen. Opt-outers 1,7 keer hogere LTV (eigen claim). 5 keer zoveel positieve reacties | [Vendor] Braze, Econsultancy |
| Oracle-klanten | Snooze-optie in preference center | "Doorgaans 82% minder afmeldingen" | [Vendor], kleine groep, geen methode |
| E-commerceklant (Single Grain via Litmus) | Getrapt preference center | 76% minder afmeldingen, 189% meer engagement | [Vendor], origineel niet gevonden |
| Return Path (ongeveer 2014) | Analyse van winbackmails | 12% gelezen, re-permission 1,8%, vast bedrag korting 21%, 45% leest later weer | [Vendor], groot maar oud |
| Blackbaud | List-Unsubscribe-header toegevoegd | Direct betere inboxplaatsing en minder spamklachten. Minder dan 1% gebruikte de header | [Vendor] |
| Catalogusverkoper (MyTotalRetail) | Frequentie van 2 naar 1 per week | Afmeldingen gelijk, omzet sterk gedaald | [Anekdote], belangrijk tegenvoorbeeld |
| Jean&Len (Klaviyo) | Segmenten op interesse, engagement en koopkans | Opens +185% naar 46,5% | [Vendor], geen cijfer over afmeldingen |

**Wat ontbreekt.** Geen enkele case is een gerandomiseerde test die afmeldingen of spam meet en tegelijk de omzet. Dat moet Siraat daarom zelf doen met een holdout (zie maatregel 1 en 2).

---

## 5. Klaviyo-specifiek: wat te gebruiken

| Onderdeel | Wat het doet | Hoe voor Siraat |
|---|---|---|
| **Deliverability-tab** (campagnes en flows) | Toont bounce, spam en afmelding per mail met de drempels uit 1.2 | Na elke campagne bekijken; boven 0,05% spam of 1% afmelding: oorzaak zoeken |
| **Benchmarks > Flows / Campaigns** | Vergelijking met ongeveer 100 vergelijkbare bedrijven, per flow, inclusief afmeldingen en spam | Beste bron voor "is dit normaal" per flow |
| **Smart Sending** | 16 uur standaard, per kanaal | Altijd aan voor campagnes. Venster eventueel naar 24 uur |
| **Engaged segmenten** | 30/60/90 dagen standaard | Herdefiniëren zonder MPP-opens: klik, site, order, of open met Apple Privacy Open = False |
| **Flowfilters** | Bepalen wie in een flow blijft | Sunset: "has not clicked email since starting this flow" en "has not placed order since starting this flow"; uitsluiten van wie in de flow geweest is (in de laatste X dagen). Winback: exit bij aankoop |
| **Prebuilt sunset-flow en -segment** | Sjabloon in de flowbibliotheek en de segmentbibliotheek | Als startpunt, criteria aanpassen naar klik/site/order |
| **Preference page** | Lijsten en vragen met keuzerondjes, opgeslagen als profieleigenschap; link naar SMS-aanmelding | "Only sales", "pause 30 days" en frequentie als eigenschap. Campagnesegmenten erop filteren |
| **Unsubscribe page** | Kan naar de preference page of SMS-aanmelding verwijzen | Opt-down aanbieden vóór "unsubscribe from all" |
| **List-Unsubscribe-header** | Automatisch in elke mail | Niets te doen; zichtbare link in de footer houden |
| **Double opt-in** | Per lijst, bevestigingslink 72 uur geldig | Alleen als test op een aparte giveaway-lijst (zie maatregel 9) |
| **Suppressie** | Alleen e-mail; SMS-toestemming blijft | Na sunset taggen en suppressen; hoogwaardige kopers naar Meta custom audience |
| **Anti-abuse monitoring** | Klaviyo kan verzending pauzeren bij hoge bounce of spam | Reden temeer om spam onder 0,05% per mail te houden |

**Wat Klaviyo zelf adviseert, samengevat:** stuur naar engaged segmenten en bouw een verzendschema op engagement; laat Smart Sending aan voor campagnes; zet een winback- en sunsetflow op en suppress wie niet reageert; behandel opens met de Apple Privacy-vlag voorzichtig; gebruik double opt-in voor lijsten met risico (zoals giveaways); laat mensen hun voorkeuren aanpassen in plaats van zich helemaal af te melden.

---

## 6. Geprioriteerde maatregelen voor Siraat

Volgorde: verwachte winst op spam en afmeldingen, gedeeld door moeite en omzetrisico. "Effect" is een inschatting op basis van de bronnen hierboven en de eigen cohortcijfers; met de data-analyse van het andere agent te toetsen.

| # | Maatregel | Verwacht effect | Moeite | Risico voor omzet |
|---|---|---|---|---|
| 1 | **Nooit meer naar de hele lijst.** Standaard campagnes naar "engaged 60 dagen" (klik, site, order, of niet-Apple-open) plus aanmelders van de laatste 14 dagen. Alleen bij grote sales naar 120 tot 180 dagen. 10 procent van de breedere groep als holdout om omzetverlies te meten. | Groot. Grootste bron van spamklachten (de 81 procent niet-actieve giveaway-aanmelders) krijgt veel minder campagnes. Spam per campagne verwacht ruim omlaag | Laag (2 segmenten, regel in PLAYBOOK) | Laag. Inactieven kopen weinig na dag 1 ($5 per aanmelder in dag 1 tot 30). Holdout laat het zien |
| 2 | **Smart Sending altijd aan voor campagnes**, plus een weekplafond: uitsluitsegment "3 of meer marketingmails ontvangen in 7 dagen" (flows niet meegeteld of apart). | Middel tot groot. Ruim 3 campagnes per week bij giveaway-aanmelders gaat omlaag | Laag | Laag tot middel. Testen met holdout, want het enige frequentiegeval met data liet omzetverlies zien |
| 3 | **Sunsetflow, gedifferentieerd.** Nooit-kopers: na 60 dagen zonder klik/site/order (giveaway: na 30 tot 45 dagen). Kopers: na 180 dagen. 3 mails in ongeveer 10 dagen, daarna taggen en suppressen. Hoogwaardige kopers daarna naar Meta custom audience. | Groot op spam en lijstkosten, 5 tot 10 procent komt terug | Middel (flow, 3 mails, segmenten) | Laag. Wie maanden niet klikt, koopt zelden via mail |
| 4 | **Opt-down op de voorkeuren- en afmeldpagina**: "Only sales and launches", "Pause for 30 days", "Everything". Opgeslagen als profieleigenschap, campagnes filteren erop. | Middel. Een deel van de afmelders blijft bereikbaar voor sales; vendor-claims 30 tot 82 procent minder afmeldingen zijn te optimistisch | Middel (preference page, 2 eigenschappen, segmentfilters) | Geen. Houdt mensen vast die anders weg zijn |
| 5 | **Zichtbare afmeldregel bovenaan in sunsetmails en in campagnes naar de 90 tot 180-dagengroep** ("Too many emails? Choose fewer or unsubscribe"), met link naar de opt-down. A/B testen op spam per mail. | Middel op spam; afmeldingen kunnen iets stijgen, wat goed is (afmelding is beter dan spam) | Laag (blok in partial) | Zeer laag |
| 6 | **Giveaway-proefperiode.** Giveaway-aanmelders krijgen de welcome-flow, maar campagnes pas na een klik of order; wie na 30 dagen niets heeft gedaan, gaat direct de sunsetflow in. | Groot voor dat cohort (67 procent van afmeldingen en 76 procent van spam in dag 14 tot 30 komt van de niet-actieven) | Middel | Laag. Kopen in dag 1 tot 30 na de eerste dag is klein ($5 per aanmelder) |
| 7 | **Verwachting zetten** in de Alia-pop-up en in de eerste regel van W1: hoe vaak, waarover, en dat de giveaway-inschrijving ook merkmail betekent. Plus link "choose how often" in W1. | Middel op spam ("I never signed up" en "too many") | Laag (tekst; Alia-toegang nodig) | Zeer laag |
| 8 | **Niet-US-aanmelders apart behandelen**: geen US-specifieke campagnes (US-prijzen, US-feestdagen, US-verzending) naar AU, CA, SG en andere landen. | Middel. Niet-US schrijft zich in 30 dagen vaker uit (23 tegen 17 procent bij giveaway) | Middel (landsegmenten, deels onbekend land) | Laag |
| 9 | **Double opt-in alleen testen**, niet uitrollen: een A/B op een deel van de giveaway-instroom, gemeten op omzet per aanmelder na 30 en 60 dagen, spam en afmelding. | Onzeker; waarschijnlijk minder spam maar ook minder lijstgroei | Middel (Alia-koppeling, aparte lijst) | **Middel tot hoog**: 10 procent koopt binnen 24 uur, deels uit W1. Daarom alleen als test |
| 10 | **Monitoring**: Google Postmaster Tools koppelen en wekelijks spamrate Gmail bekijken (doel < 0,1 procent); Klaviyo Deliverability-tab en Benchmarks per flow in de wekelijkse update. | Indirect; voorkomt dat een probleem weken onopgemerkt blijft | Laag | Geen |
| 11 | **Sunset-copy testen**: onderwerp "Should we stop emailing you?" tegen een vast bedrag als bedankje ("$10 to stay", alleen bij oud-kopers); één primaire "keep me"-knop plus secundaire "only sales". | Klein tot middel op het aantal dat blijft | Laag | Laag (korting alleen bij kopers) |
| 12 | **SMS als downgrade** (alleen als Siraat SMS heeft of wil): op de afmeldpagina "text me only the big sales" aanbieden. | Klein tot middel; behoudt bereik bij een deel van de afmelders | Middel tot hoog (SMS-programma, kosten per bericht, toestemming) | Positief als het werkt; kosten per SMS meewegen |

**Volgorde om te starten:** 1, 2 en 10 kunnen deze week (instellingen en segmenten). Daarna 3 en 6 (sunset en giveaway-proefperiode, één flow met twee ingangen), dan 4, 5 en 7. 9 en 12 zijn pas zinvol na de eerste resultaten.

---

## Bronnen

Officieel (Google, Yahoo, Klaviyo):
- Google, Email sender guidelines FAQ: https://support.google.com/a/answer/14229414
- Klaviyo, How to create a sunset flow: https://help.klaviyo.com/hc/en-us/articles/360017518492
- Klaviyo, Understanding the deliverability tab in campaigns and flows: https://help.klaviyo.com/hc/en-us/articles/12695416712219
- Klaviyo, Anti-abuse and campaign performance monitoring: https://help.klaviyo.com/hc/en-us/articles/115000308972
- Klaviyo, Guide to benchmarks: https://help.klaviyo.com/hc/en-us/articles/360050110072
- Klaviyo Academy, Compare your performance with benchmarks: https://academy.klaviyo.com/en-us/quick-guides/compare-your-performance-with-benchmarks
- Klaviyo, Smart Sending: https://help.klaviyo.com/hc/en-us/articles/115002779311
- Klaviyo, Smart Sending for campaigns: https://help.klaviyo.com/hc/en-us/articles/115005078227
- Klaviyo, Default account settings: https://help.klaviyo.com/hc/en-us/articles/360004059711
- Klaviyo, Create an engaged segment: https://help.klaviyo.com/hc/en-us/articles/115000200072
- Klaviyo, How to identify iOS 15 Mail Privacy Protection opens: https://help.klaviyo.com/hc/en-us/articles/4416791883163
- Klaviyo Academy, Build your engaged segments: https://academy.klaviyo.com/en-us/courses/strengthen-your-sender-reputation/lessons/build-your-engaged-segments
- Klaviyo Academy, Strengthen your sender reputation: https://academy.klaviyo.com/strengthen-your-sender-reputation
- Klaviyo, Strengthen your sender reputation: https://help.klaviyo.com/hc/en-us/articles/115005250368
- Klaviyo Academy, Say goodbye to unengaged customers: https://academy.klaviyo.com/en-us/courses/automating-the-customer-journey-with-flows/lessons/say-goodbye-to-unengaged-customers
- Klaviyo, Create email frequency segments: https://help.klaviyo.com/hc/en-us/articles/115000769631
- Klaviyo, Custom code consent pages: https://help.klaviyo.com/hc/en-us/articles/115005077067
- Klaviyo, Unsubscribes in Klaviyo: https://help.klaviyo.com/hc/en-us/articles/115005078267
- Klaviyo, How to add an unsubscribe link: https://help.klaviyo.com/hc/en-us/articles/115006054267
- Klaviyo, Double opt-in process (FR): https://help.klaviyo.com/hc/fr-fr/articles/115005251108
- Klaviyo blog, consent pages (2022): https://klaviyo.com/blog/subscriber-consent
- Klaviyo, Abandoned cart benchmarks: https://www.klaviyo.com/marketing-resources/abandoned-cart-benchmarks
- Klaviyo, Segmentation: https://klaviyo.com/products/email-marketing/segmentation
- Klaviyo blog, Sunset flow emails: https://www.klaviyo.com/uk/blog/sunset-flow-emails

Gmail en Yahoo, uitleg door derden:
- Mailgun, Gmail/Yahoo webinar takeaways: https://www.mailgun.com/blog/deliverability/gmail-yahoo-webinar-key-takeaways/
- Bird, Gmail and Yahoo sender requirements: https://bird.com/docs/knowledge-base/deliverability/gmail-yahoo-requirements
- Resend, Avoid Yahoo spam folder: https://resend.com/guides/email/deliverability/avoid-yahoo-spam-folder
- Movable Ink, Gmail subscription manager: https://movableink.com/blog/relevance-or-bust-what-gmails-new-subscription-manager-means-for-marketers
- Bird, Gmail Manage subscriptions: https://bird.com/blog/gmail-new-manage-subscriptions-feature
- Yespo, Gmail Manage subscriptions: https://yespo.io/blog/google-begins-rollout-new-subscription-management-dashboard-gmail-users

Benchmarks [Vendor]:
- Omnisend, Email marketing benchmarks: https://www.omnisend.com/blog/email-marketing-benchmarks/
- Mailchimp-data via Findymail: https://findymail.com/blog/average-unsubscribe-rates
- Mailchimp-data via Suped: https://www.suped.com/knowledge/email-deliverability/sender-reputation/what-is-a-good-unsubscribe-rate-for-email-marketing
- Branvas, 80+ ecommerce benchmarks 2026: https://branvas.com/blogs/news/ecommerce-email-marketing-benchmarks
- Retention Side, ecommerce benchmarks 2026: https://retentionside.com/blog/ecommerce-email-marketing-benchmarks
- BS&Co, benchmarks januari 2026: https://bsandco.us/blog-post/ecommerce-email-marketing-benchmarks-january-2026
- Opensend, unsubscribe statistics: https://www.opensend.com/post/email-unsubscribe-rate-statistics-ecommerce

Sunset, re-engagement, MPP:
- Validity, 7 reactivation campaign insights: https://www.validity.com/blog/7-email-reactivation-campaign-insights/
- MarketingProfs over Return Path (2014): https://www.marketingprofs.com/charts/2014/25126/how-to-win-back-inactive-email-subscribers
- EcommerceBytes over Return Path (2014): https://www.ecommercebytes.com/2014/05/14/email-marketers-give-inactive-customers-soon/
- Elite Brands, footwear case: https://www.elitebrands.org/blog/how-we-boosted-klaviyo-deliverability-20-for-a-footwear-retailer
- Elite Brands, sunset flow: https://www.elitebrands.org/blog/the-klaviyo-sunset-flow-mistake-that-harms-deliverability
- NR10, Klaviyo list-cleaning case: https://nr10.com/klaviyo-list-cleaning-case-study/
- GrowPronto, list cleaning: https://blogs.growpronto.com/p/how-to-clean-your-email-list-in-4-steps-c5a0
- phpList, list cleaning: https://www.phplist.org/how-we-cleaned-our-lists-reduced-our-bounce-rate-and-doubled-our-open-rate-with-phplist/
- Spam Resource, The goal of sunsetting: https://www.spamresource.com/2023/05/the-goal-of-sunsetting.html
- Mailflow Authority, sunset policies: https://mailflowauthority.com/email-deliverability/sunset-policies
- Suped, sunsetting best practices: https://www.suped.com/learn/email-deliverability/what-are-the-best-practices-for-sunsetting-inactive-email-subscribers-according-to-isps-and-gdpr
- Practical Ecommerce, rethink your sunset policy: https://www.practicalecommerce.com/rethink-your-email-sunset-policy
- SendGrid, re-engagement tips: https://sendgrid.com/blog/4-tips-for-sending-re-engagement-email-campaigns
- ActiveCampaign, re-engagement subject lines: https://activecampaign.com/blog/re-engagement-email-subject-lines
- GetResponse, re-engagement examples: https://www.getresponse.com/blog/picking-the-right-re-engagement-tactics
- Bocconi over re-permission-onderzoek (Journal of Marketing): https://www.unibocconi.it/en/news/navigating-opt-maze-balancing-transparency-and-persuasion-data-consent
- Klaviyo Community, engaged segment en MPP: https://community.klaviyo.com/marketing-30/how-to-defined-engaged-segment-10619
- Klaviyo Community, engaged never subscribed: https://community.klaviyo.com/marketing-30/fixing-large-number-of-engaged-never-subscribed-13713

Preference center, afmelden, spamredenen:
- Litmus, email preferences: https://www.litmus.com/blog/we-want-your-email-preference-new-approach-to-opting-in
- Oracle, snooze in email marketing: https://blogs.oracle.com/marketingcloud/the-evolving-use-of-snooze-in-email-marketing
- Digioh, preference center: https://www.digioh.com/blog/email-preference-center
- Twilio, preference center: https://www.twilio.com/en-us/blog/insights/the-power-of-an-email-preference-center
- Practical Ecommerce, pros and cons of preference centers: https://www.practicalecommerce.com/Pros-Cons-of-Email-Preference-Centers
- Klaviyo Community, pause subscription: https://community.klaviyo.com/marketing-30/pause-email-marketing-subscription-4952
- Klaviyo Community, snooze 30 days: https://community.klaviyo.com/marketing-30/snooze-emails-30-days-vs-once-per-month-emails-9189
- Klaviyo Community, custom preference page: https://community.klaviyo.com/accounts-and-settings-2/how-can-i-create-a-custom-manage-preference-page-5911
- Klaviyo Community, suppression only email: https://community.klaviyo.com/marketing-30/suppressed-are-only-suppressed-for-email-how-to-unsubscribe-from-email-and-sms-2357
- Blackbaud, list-unsubscribe recap: https://community.blackbaud.com/blogs/1/8399
- MediaPost, unsubscribe link placement: https://www.mediapost.com/publications/article/103837/None
- Zoho, unsubscribe link and abuse complaints: https://help.zoho.com/portal/en/kb/campaigns/faqs/deliverability-compliance/articles/does-highlighting-the-unsubscribe-link-in-my-email-reduce-abuse-complaints
- Fulcrum Tech (Litmus/Fluent-cijfers): https://fulcrumtech.net/resources/keep-email-subscribers/
- MarketingCharts (MarketingSherpa 2008): https://www.marketingcharts.com/digital-36897
- Econsultancy, Bloom & Wild: https://econsultancy.com/case-studies/view/bloom-wild-put-the-customer-first-with-mothers-day-opt-out/
- Braze, Bloom & Wild: https://www.braze.com/customers/bloom-and-wild-case-study

Frequentie en giveaways:
- MyTotalRetail, e-mail list fatigue: https://mytotalretail.com/article/e-mail-marketing-four-tips-combat-e-mail-list-fatigue-45154/all
- PleasePoint, sending frequency: https://www.pleasepoint.com/en/blog/frecuencia-emails/how-often-should-i-send-emails-to-customers
- Holistic Email Marketing, frequency testing: https://www.holisticemailmarketing.com/blog/email-frequency-testing-the-key-to-unlocking-more-email-revenue/
- Klaviyo Community, giveaway list problems: https://community.klaviyo.com/analytics-72/why-am-i-getting-high-bounces-spam-complaints-and-unsubscribe-rates-from-a-list-i-collected-through-a-giveaway-1764
- UpViral, double opt-in for giveaways: https://www.upviral.com/blog/double-opt-in-when-running-giveaways
- ViralSweep, Klaviyo integration: https://support.viralsweep.com/en/articles/9272790-klaviyo

Eigen data waarnaar verwezen wordt: `research/lijstkwaliteit/01-giveaway-instroom.md` (21 okt 2026).
