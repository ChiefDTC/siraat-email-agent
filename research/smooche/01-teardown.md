# Smooche teardown: van pop-up tot eerste mails (31 okt 2026)

Read-only onderzoek. Niets gewijzigd in Klaviyo of Shopify, geen mail verstuurd, niet gecommit.
Bronnen: twee PDF's van Floris (Gmail-prints), Floris' beschrijving van pop-up en twee platte mails, Email Love MCP, poging tot WebFetch van smooche.com.

## 0. Wat we wel en niet konden zien

| Bron | Resultaat |
| --- | --- |
| PDF "You joined at the right time 👻" | Volledig gelezen (7 pagina's) |
| PDF "Happy Halloween 🎃" | Volledig gelezen (8 pagina's) |
| Email Love: Smooche | Niet aanwezig (search_brands leeg, search_emails "geen brand"). Geen journey-data. Eventueel via `request_brand` laten verzamelen (niet gedaan, is een schrijfactie). |
| WebFetch smooche.com | Geblokkeerd: `getaddrinfo ENOTFOUND smooche.com`. Het domein valt buiten de toegestane netwerkdomeinen van deze sessie. Toevoegen in de netwerkinstellingen als we de site live willen bekijken. |
| Plattetekstmails "No tricks, just a treat" en "Found your new make-up?" | Alleen via Floris' samenvatting, geen PDF. Afzender volgens Floris "Chloe from Smooche" / "Chloe at Smooche" <hey@smooche.com>. |

Belangrijk verschil: beide PDF's zijn **ontworpen HTML-mails** met afzendernaam "Smooche", niet platte brieven van "Chloe". Smooche mengt dus twee stijlen: platte persona-brieven (Chloe) en zware beeldmails (merk). De conversiemotor zit niet alleen in de platte tekst.

## 1. Transcriptie van de twee PDF's

### Mail A: "You joined at the right time 👻"
- **Afzender:** Smooche <hey@smooche.com>
- **Ontvangen:** 31 okt 2026 00:28 (Gmail-tijd van Floris, waarschijnlijk CET, dus 30 okt 23:28 UTC). Aanmeldtijd onbekend; vermoedelijk kort na de pop-up (welkomstmail).
- **Preview:** niet zichtbaar in de print.
- **Layout (van boven naar beneden):**
  1. Hero, donkerrood met spinnenweb: woordmerk SMOOCHE, vijf groene Trustpilot-achtige sterren (zonder score of aantal), kop "A Halloween Treat To Welcome You In", subregel "Our Halloween sale takes up to 60% off everything, no code needed.", knop **SHOP THE SALE**.
  2. "Discover The Collection": vier productkaarten (Color Changing Foundation, Reverse-time Peptide Serum, Ultra Peptide and Collagen Lifting Mask, Under-Eye Reset Patches). Elk met badge "UP TO 60% OFF", twee bullets, knop **SHOP NOW**.
  3. Footer grijs: woordmerk, links About Us / Sale / Bestsellers / New Arrivals, betaalicoontjes (Apple Pay, Mastercard, Discover, Amex, Visa, Afterpay, Amazon, Shop, PayPal), Instagram en TikTok.
  4. Wettelijke footer: "Smooche, 8605 Santa Monica Boulevard PMB 44698 West Hollywood, California 90069", "Click here to unsubscribe from all e-mails." (in deze mail geen "receive fewer emails").
- **Lengte:** ongeveer 70 woorden, bijna alles in afbeeldingen. 5 knoppen (1 hoofd, 4 product).
- **Aanbod:** "up to 60% off everything, no code needed" (automatisch, geen code).
- **Urgentie/schaarste:** geen deadline in deze mail; "Halloween" is de impliciete tijdsdruk.
- **Linkdoelen:** niet zichtbaar in de print (Gmail-print toont geen URL's).

### Mail B: "Happy Halloween 🎃"
- **Afzender:** Smooche <hey@smooche.com>
- **Ontvangen:** 31 okt 2026 14:04 (circa 13,5 uur na mail A).
- **Layout:**
  1. Hero rode envelop met wassen zegel "Expires Today": kop "Your Halloween Surprise", subregel "You have $12.24 store credit left", stippelkader "USE CODE: HW-XCS68", knop **REDEEM MY CREDIT**.
  2. Donker tekstblok: "Hey beauty, Happy Halloween! Quick reminder from us, yesterday we added $12.24 to your account. Our customer support team just checked and noticed you have not used it yet." Rode balk: "The credit in your account expires today." Daarna: "Treat yourself today to Korean-formulated beauty...", nogmaals de code, "at checkout on any order of $30 or more."
  3. "Explore Korean Inspired Skincare": vier producten in raster, elk met tekstlink **REDEEM CREDIT**.
  4. Drie USP's met beeld: Skin-Loving Ingredients, Real Korean Formulas ("over 20 years of research. Trusted by leading dermatologists worldwide"), Loved By Real Customers ("Foundation 4.8 stars, Serum 4.9 stars").
  5. Grote modelfoto, daarna dezelfde footer als mail A.
- **Lengte:** ongeveer 180 woorden. 1 hoofdknop plus 4 tekstlinks, allemaal "redeem".
- **Aanbod:** "$12.24 store credit" die in werkelijkheid een kortingscode is (HW-XCS68) met minimum van $30.
- **Urgentie:** "Expires Today" (zegel, balk, hero). Persoonlijke framing: "yesterday we added", "our customer support team just checked".
- **Observatie:** Floris meldde zich pas de avond ervoor aan; "yesterday we added $12.24 to your account" en een supportteam dat "checked" zijn vrijwel zeker sjabloontekst. Het vreemde bedrag ($12.24) is bedoeld om echt en persoonlijk te lijken. Of iedereen hetzelfde bedrag en dezelfde code krijgt, weten we niet (HW-XCS68 oogt uniek).

### Plattetekstmails (volgens Floris)
- **"No tricks, just a treat"** (welkom direct na aanmelding), afzender Chloe. "Welcome to the Smooche family! Your Halloween offer is live... No codes, no tricks. Everything is up to 60% off, and it's already applied... more than 100,000 women... Color Changing Foundation running pretty low on stock... limited time". Alleen woordmerk boven en onder, IG/TikTok, footer met "receive fewer emails".
- **"Found your new make-up?"** (browse/site abandonment): "the sale ends tonight at midnight... Once midnight hits, it's gone. No extensions this time."
- Het is onduidelijk of "No tricks" en "You joined at the right time" twee mails in dezelfde welkomstflow zijn (bijvoorbeeld A/B of mail 1 en 1b) of verschillende flows. Floris kan dat checken aan de tijdstempels in zijn inbox.

## 2. De funnel zoals hij nu loopt

1. **Pop-up** (Halloween, schermvullend): "Try your luck, Scratch below to see what you win". Gouden kraskaart. Na krassen: "You've Got 60% off", knop **CLAIM**.
2. **Landing:** /collections/the-hits (bestsellers), niet de homepage en geen PDP.
3. **Korting:** volgens Floris niet automatisch toegepast in zijn sessie, terwijl de mails zeggen "no code needed" en "already applied". De 60% is bovendien gelijk aan de publieke sitewide sale ("up to 60% off everything"). De kraskaart geeft dus niets extra: hij verpakt de openbare sale als persoonlijke winst.
4. **Mail 1 (minuten na aanmelding):** welkom plus "your offer is live", 60%, social proof (100,000+ women), voorraad-claim op de bestseller, "limited time".
5. **Mail 2 (zelfde dag, circa 13 uur later):** tweede, nieuw aanbod bovenop de sale: "store credit" $12.24 met "expires today".
6. **Browse/site abandonment:** "sale ends tonight at midnight, no extensions".

Ritme: minstens twee mails binnen 14 uur, met elke mail een andere reden om nu te kopen (welkom, krediet, deadline).

## 3. Waarom dit converteert

| Mechaniek | Waarom het werkt |
| --- | --- |
| Gamification in de pop-up | Krassen is een kleine investering; de "winst" voelt verdiend (endowment). Hogere opt-in dan een statisch "10% off". |
| Onmiddellijkheid | Mail 1 komt binnen minuten, terwijl de bezoeker nog op de site is. Dag 0 draagt in elke welkomstflow het grootste deel van de omzet (ook bij ons: dag 0 en 1 = 75 procent, Homestead). |
| Geen code, al toegepast (belofte) | Minder frictie bij checkout, geen gezoek naar codes. Werkt alleen als het echt zo is. |
| Eén doel per mail | Platte mail: één link naar een samengestelde collectie. HTML-mail: één hoofdknop, verder alleen product-shortcuts. |
| Collectie als landing | "The Hits" beperkt de keuze tot bewezen bestsellers; minder keuzestress dan de homepage. |
| Persona-afzender | "Chloe from Smooche" leest als een mens; plattetekst landt vaker in Primary (Gmail) dan een beeldmail. |
| Opeenstapelende redenen | Sale, dan "krediet" dat vandaag verloopt, dan "middernacht". Elke mail opent een nieuwe lus. |
| Specificiteit | "$12.24", "running pretty low", "100,000 women": concrete details verhogen geloofwaardigheid, ook als ze niet persoonlijk zijn. |
| Thema | Halloween geeft een natuurlijke deadline en een excuus voor "treat". Black Friday doet hetzelfde. |

## 4. Vergelijkbare merken (Email Love, Smooche niet aanwezig)

| Merk | Wat we zagen | Relevant voor Siraat |
| --- | --- | --- |
| **NOBL** (bagage, DTC, Klaviyo) | 201 mails in 12 maanden, 3,85 per week. Twee afzenders: hello@ (140) en daniel@ (61, oprichter). Mail 25 okt "A quick note about the bag you travel with": opent met "Daniel here.", 5 korte alinea's pijn ("The stuck zipper. The bad wheels."), dan "Black Friday Sale is live now with 67% OFF", één knop SHOP NOBL, ondertekening "Daniel, Founder, NOBL", regel "100,000+ 5-Star Reviews". Wel een menubalk en logo, dus "plat ogend" maar met merkopmaak. Gem. 141 woorden, 11 beelden. | Bijna exact het Benjamin-model: founder-afzender als tweede kanaal naast de merkafzender, korte pijnbrief, één knop, BF al eind oktober "live". |
| **Danessa Myricks Beauty** | Afzendernaam "Danessa @ Danessa Myricks Beauty", onderwerp "A quick note from me". Verder sterk visueel: gem. 44 woorden, 12 beelden, 36% GIF. | Persona in de afzendernaam werkt ook boven een ontworpen mail. |
| **TUSHY** | Nieuwsbrieven van "Morgan from TUSHY" (persona, geen oprichter). | Zelfde patroon als "Chloe from Smooche". |
| **Gainful** | "A quick note from Eric and Jahaan" (oprichters), 29 okt. | Oprichtersnoot als pre-BF-aanloop. |

Beperking: Email Love levert voor deze merken geen geordende welkomstflow met tijden (de journeys van Graza, BRĒZ en TUSHY bevatten alleen thumbnails, geen tekst of vertragingen). Over aantal mails en wachttijden in hun welkomstflows kunnen we dus niets hard zeggen. Een kraskaart- of spin-pop-up is niet terug te vinden in Email Love (gaat over mails, niet over sites).

## 5. Wat Siraat kan overnemen (Black Friday)

Context: onze pop-up is Alia "Card Game" met belofte "kans om je order terugbetaald te krijgen"; Black Friday wordt 70% off met 4 gifts; HI10 en unieke codes mogen stapelen (besluiten 7 en 19 okt).

1. **Mail 1 binnen 1 tot 2 minuten** in plaats van 10 minuten. De bezoeker zit dan nog op de site.
2. **Afzendernaam "Benjamin from Siraat"** op de plattetekst-varianten (oprichter is altijd Benjamin). Testen tegen "Siraat" op W1. Let op: een brief zonder vaste header is een uitzondering op de merkregel en heeft akkoord van Floris nodig (zoals bij affiliate en S2c).
3. **Echt automatisch toegepaste korting.** Shopify-discountlink `siraatskitchen.com/discount/<CODE>?redirect=/collections/<bf-collectie>` zet de code in de sessie. Smooche belooft "already applied" maar levert het volgens Floris niet; dat kost vertrouwen en conversie. Bij ons: 70% is automatisch, HI10 via de link erbij. Testen per markt voor livegang.
4. **Eén CTA naar een samengestelde BF-collectie** (ons "The Hits"): Pan Pro, 6-delige set, Pro Duo, 12-delige set (VS). Niet naar de homepage.
5. **Pop-up als onthulling, niet als loterij.** "Scratch to reveal your Black Friday price" met eerlijke uitkomst (zie 6). De Alia Card Game kan blijven voor de echte trekking (order refund).
6. **Tweede reden op dag 0 of 1:** ons welkomstkrediet / gift card (besluit 7 okt) als echte unieke code met echte vervaldatum. Mag in de vorm "your $25 gift card", niet "we added credit to your account" tenzij het echt Shopify store credit is.
7. **Social proof en specificiteit uit eigen data:** "100,000+ happy customers" (goedgekeurd), echte sterren uit Okendo/Trustpilot met aantal, echte voorraad uit Shopify/Ecomflow als we schaarste noemen.
8. **Deadline alleen als hij echt is:** einde BF-sale (datum nog van Floris), einde unieke code, einde gifts. Countdown in de mail mag, mits de prijs daarna echt omhoog gaat.

## 6. Juridische en ethische risico's, en de eerlijke versie

| Smooche-tactiek | Risico | Eerlijke versie voor Siraat |
| --- | --- | --- |
| "Try your luck... see what you win", iedereen krijgt 60% | EU: Richtlijn oneerlijke handelspraktijken, bijlage I punt 31 (valse indruk dat de consument iets gewonnen heeft) is altijd verboden. VS: FTC Act sectie 5 (misleidend), plus kansspelregels als het een "kans" heet. Ook risico op klachten en chargebacks. | "Scratch to reveal your Black Friday offer" zonder "luck" of "win". Of echte variabele prijzen met gepubliceerde kansen en reglement. |
| Kraswinst = publieke sitewide sale | Misleidend: de "prijs" is wat iedereen krijgt. | Zeggen wat het is: "Black Friday is live: 70% off, plus your extra 10% (HI10)". De extra 10% is dan echt exclusief voor aanmelders. |
| "No code needed / already applied" terwijl het niet werkt | Misleidende prijsclaim; frustratie bij checkout. | Discountlink gebruiken en per markt testen; anders de code duidelijk tonen. |
| "Up to 60% off everything" | EU Omnibus (prijsaanduidingsrichtlijn art. 6 bis): korting moet gelden ten opzichte van de laagste prijs in de 30 dagen ervoor. VS: FTC Guides Against Deceptive Pricing (16 CFR 233), Californië B&P 17501. Een permanente "sale" is risicovol. | Bij ons: 50% okt, 70% Halloween en BF. Voor EU/UK-klanten de referentieprijs controleren (30-dagenlaagste). Compare-at alleen tonen als die prijs echt gehanteerd is. |
| "Running pretty low on stock" | Valse schaarste (bijlage I punt 7: vals beweren dat iets maar heel kort beschikbaar is; algemene misleiding). | Alleen noemen met echte voorraaddata, liefst concreet ("under 40 sets left in the US warehouse"), anders weglaten. |
| "Sale ends tonight at midnight. No extensions this time." en daarna weer sale | Valse deadline als de sale doorloopt of direct terugkomt (BF na Halloween). | Alleen echte einddata. Na het einde gaat de prijs echt omhoog. Geen "no extensions" als BF al gepland is. |
| "Yesterday we added $12.24 to your account. Our customer support team just checked..." | Gefabriceerde persoonlijke handeling; "store credit" is een kortingscode met $30 drempel. Misleidend en slecht voor vertrouwen. | "Here's a $25 gift card for your first order (on orders over $149), valid until <datum>." Geen nep-supportcheck. Echte Shopify store credit alleen als we het echt boeken. |
| Trustpilot-achtige sterren zonder bron of aantal | Misleidende beoordelingsweergave (FTC-regel over nepreviews 2024, EU bijlage I punt 23 ter). | Bron en aantal noemen; alleen geverifieerde reviews (ons beleid). |
| Persona "Chloe" (bestaat ze?) | Licht risico als het een verzonnen persoon is die beweert dingen gedaan te hebben. | Benjamin bestaat en is oprichter; alleen dingen laten zeggen die waar zijn. |
| Alia Card Game "kans op order refund" (onze eigen pop-up) | Een echte trekking: in de VS reglement nodig met "no purchase necessary" (alternatieve deelname), looptijd, kansen, ongeldig waar verboden. | Reglement-link in pop-up en W1; nagaan of Alia dit al heeft. |

## 7. Voorstel BF-mechaniek Siraat (nog niets gebouwd)

- **Pop-up (Alia):** "Scratch to reveal your Black Friday price" → onthult "70% off + extra 10% for subscribers" (eerlijk, voor iedereen gelijk, en dat staat er ook). Optioneel naast de bestaande refund-trekking met reglement.
- **Klik → BF-collectie** met discountlink die HI10 in de sessie zet.
- **W1 binnen 2 min**, afzender "Benjamin from Siraat", korte brief: wie hij is, "the original hammered titanium pan", 70% plus jouw 10% al toegepast via de knop, 30-day returns en 75-year warranty, één knop naar de collectie. A/B: plat tegen huidige W1.
- **Dag 0 avond of dag 1:** tweede reden: gift card of gifts-blok ("4 gifts with every order while the sale runs").
- **Laatste 24 uur van de sale:** echte deadline-mail, ook als browse-abandonment-variant.
- **Meten:** omzet per nieuwe abonnee (huidige baseline in welcome v3), Primary-plaatsing van de platte variant, spam- en afmeldpercentages.

## 8. Open vragen voor Floris
1. Tijdstip van aanmelding bij Smooche, en de tijden van "No tricks, just a treat" en "Found your new make-up?" (dan kunnen we hun flow exact uittekenen).
2. Werkte de CLAIM-knop met een code in de URL, of alleen een gewone collectielink?
3. Mag smooche.com aan de toegestane domeinen worden toegevoegd voor een live check van pop-up en checkout?
4. BF-einddatum, en of de extra 10% voor aanmelders blijft.
5. Akkoord op een platte Benjamin-brief zonder vaste header in de welkomstflow (uitzondering op de merkregel)?
