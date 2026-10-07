# Reviews per bezwaar en per product · analyse

Datum: 7 oktober 2026. Rol: voice-of-customer. Alleen gelezen: niets gepubliceerd, verborgen, beantwoord of gewijzigd in Okendo, Loox, Shopify, Klaviyo of Gorgias. Namen staan zoals gepubliceerd (voornaam plus initiaal of alleen voornaam). Klantquotes zijn letterlijk; inkorten alleen met "...".

Bestanden in deze map:

| Bestand | Wat |
| --- | --- |
| `01-analyse.md` | Dit stuk: bronnen, sterrenverdeling, tagging, betrouwbaarheid, advies rating |
| `quotes-per-bezwaar.csv` | Top 8 bezwaren: per bezwaar 3 bewijsquotes plus 1 kritische review met antwoord (32 regels) |
| `quotes-per-product.csv` | Per product tot 5 quotes, gaten expliciet gemarkeerd (51 regels) |
| `reviews-tagged.csv` | Alle 704 bereikbare reviews getagd (product, maat, kookplaat, thema, sterren, lengte, foto, tijd sinds aankoop, verdacht-import) |
| `02-pdp-blokken.md` | Drie PDP-bezwarenblokken (Engels, live tekst) en de filterstrategie |

---

## 1. Wat bereikbaar was en wat niet

| Bron | Resultaat |
| --- | --- |
| Okendo Storefront API `api.okendo.io` | **Geblokkeerd** door de proxy (connect_rejected). Store-ID (subscriberId) gevonden: `752cb18e-9cf9-4a13-aebf-d5506309ee69`. Het endpoint dat de widget aanroept: `https://api.okendo.io/v1/stores/752cb18e-9cf9-4a13-aebf-d5506309ee69/products/shopify-<productId>/reviews?limit=5&orderBy=date%20desc&lastEvaluated=...` |
| Shopify metafields (Replo `shopify_metafields_get`, plus de PDP-HTML van siraatskitchen.com, 64 producten) | `okendo.summaryData` en `okendo.ReviewsWidgetSnippet`: per reviewgroep het totaal, de sterrenverdeling en **alleen de 5 nieuwste reviews**. Zo 19 Okendo-reviews met tekst. |
| Loox (oude reviewapp, nog in metafields) | `loox.reviews` op de Pan Pro Standard: 100 reviews met naam en tekst, zonder sterren per review. `loox.num_reviews` 375, `loox.avg_rating` 4.2. `loox.io` zelf is geblokkeerd. |
| Trustpilot | `content/reviews/reviews.csv`: 585 reviews uit Gorgias-notificaties (10 april t/m 6 oktober 2026). |
| Gorgias | Alleen aggregaten: 484 pre-sale tickets in 90 dagen, gematcht op trefwoorden in klantberichten. Plus de cijfers uit `research/deep/04` (526 pre-sale, 7 okt). |
| Molens (127 reviews, 4.8) | Niet terug te vinden: geen `okendo`- of `reviews`-metafield op de molens, geen widget-data in de HTML. Het getal in `content/products/salt-pepper-mill-set/product.md` is dus onbevestigd. |

Conclusie: van de 2.226 Okendo-reviews op de pannen kon ik er 5 lezen. De analyse per bezwaar rust daarom op 704 reviews (585 Trustpilot, 100 Loox, 19 Okendo). Voor de echte Okendo-mining is een export nodig (zie 1.1).

### 1.1 Wat Floris moet aanleveren

**Optie A (snelst): Okendo CSV-export.** Okendo admin, Reviews, Export (alle statussen, alle producten, alle datums). Kolommen:

| Kolom | Waarom |
| --- | --- |
| Review ID | Ontdubbelen, terugvinden |
| Product ID, product handle, product name | Per product taggen (nu is alles gegroepeerd) |
| Variant name (maat, kleur) | Pan Pro per maat, Deep Pan per maat |
| Rating | Echte verdeling per product |
| Title, body | De tekst |
| Reviewer display name (zoals gepubliceerd) | Alleen dit gebruiken, nooit e-mail of achternaam |
| Verified buyer (ja/nee) | Alleen geverifieerde reviews citeren |
| Order ID of order-match | Intern, om echtheid te checken, niet publiceren |
| Date created | Tijd sinds aankoop, trends |
| Status (approved, rejected, pending) | Zien wat niet getoond wordt |
| Source of external provider (Okendo request, import, Shopify, Loox-migratie) | Belangrijkste kolom: wat is geïmporteerd (zie hoofdstuk 3) |
| isIncentivized | Gestimuleerde reviews apart houden |
| Media (ja/nee, URL's) | Fotoreviews voor PDP en mail |
| Reply body, reply date | Welke kritiek al een antwoord heeft |
| Helpful / unhelpful count | Sortering "Most helpful" |
| Reviewer attributes en product attributes (als ingesteld) | Kookplaat, huishouden |
| Country | US tegenover AU, CA, UK |

**Optie B: netwerk.** Voeg `api.okendo.io` toe aan Allowed domains van deze omgeving. Dan haal ik alles zelf op via het openbare endpoint hierboven (alleen lezen, gepagineerd).

**Daarnaast: Loox-export** (alle 375 plus de 18 en 39 op andere producten) met dezelfde kolommen, en het antwoord op de vraag waar de Okendo-reviews vandaan komen (geïmporteerd uit Loox, Judge.me, AliExpress of een CSV?).

---

## 2. Sterrenverdeling per product

| Bron | Product of groep | n | 5 | 4 | 3 | 2 | 1 | Gemiddeld | Opmerking |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Okendo | Alle pannen en sets (gegroepeerd, staat op 15 PDP's) | 2.226 | 1.843 (82,8%) | 336 (15,1%) | 38 (1,7%) | 6 (0,3%) | 3 (0,1%) | 4,80 | 97,9% recommended; 5 merkantwoorden; 0 foto's; gemiddeld 11,6 woorden per review |
| Okendo | Cutting Board (Anti-Microbial) | 296 | 273 | 21 | 1 | 0 | 1 | 4,91 | 10 foto's; gemiddeld 6,5 woorden per review |
| Okendo | Stainless Steel Lid | 4 | 4 | 0 | 0 | 0 | 0 | 5,00 | |
| Okendo | Titanium Utensil | 2 | 2 | 0 | 0 | 0 | 0 | 5,00 | |
| Okendo | Titanium Water Bottle | 3 | 1 | 0 | 0 | 1 | 1 | 2,67 | "dropshipped", "$15 op AliExpress" |
| Loox | Pan Pro Standard | 375 | ? | ? | ? | ? | ? | 4,2 | Dit is wat Google ziet (structured data, zie 3.3) |
| Loox | Pro Duo, Cookware Set Pro, Titanium Pan Pro (gedeeld) | 18 | ? | ? | ? | ? | ? | 4,7 | |
| Loox | Utensil Set Bundle | 39 | ? | ? | ? | ? | ? | 4,8 | |
| Trustpilot (180 d) | Alles | 585 | 384 | 47 | 12 | 14 | 128 | 3,93 | 24% is 1 of 2 sterren |
| Trustpilot | Pan Pro (getagd) | 337 | 193 | 31 | 8 | 11 | 94 | 3,65 | |
| Trustpilot | Wok | 16 | 10 | 1 | 1 | 0 | 4 | 3,81 | |
| Trustpilot | Crêpe | 6 | 5 | 0 | 0 | 1 | 0 | 4,50 | |
| Trustpilot | Cutting Board | 9 | 6 | 1 | 1 | 0 | 1 | 4,22 | |
| Trustpilot | Set of bundel (welke onbekend) | 19 | 11 | 0 | 0 | 0 | 8 | 3,32 | |

Per maat (Mini, Small, Standard, Large), per set (6-delig, 12-delig, Pot Set), Deep Pan, Pizza Steel en Crêpe bestaat in Okendo geen eigen verdeling zichtbaar: de widget toont overal dezelfde 4,8 uit 2.226. De verdeling per product komt pas met de export.

---

## 3. Betrouwbaarheid: drie patronen die eerst opgehelderd moeten worden

Dit is geen beschuldiging; het zijn patronen in de data die Floris moet kunnen verklaren voordat we de Okendo-score of Okendo-quotes inzetten.

### 3.1 Okendo en de rest vertellen een ander verhaal

| | Okendo pannen | Loox Pan Pro Standard | Trustpilot |
| --- | --- | --- | --- |
| Gemiddeld | 4,80 | 4,2 | 3,93 |
| Aandeel 1 en 2 sterren | 0,4% (9 van 2.226) | onbekend, maar ruim 40 van de eerste 51 reviews in de feed zijn klachten | 24% (142 van 585) |
| Woorden per review | 11,6 | lang (klachten) en kort (zie 3.2) | 65 |

Zelfde product, zelfde klanten. Een verschil van factor 60 in het aandeel lage sterren is niet te verklaren met "andere platformen trekken andere klanten".

### 3.2 Een blok korte, gelijkvormige reviews

- **Loox-feed (Pan Pro Standard):** de eerste 51 reviews zijn lang, specifiek en overwegend negatief (plakken 32 keer, retour/service 16). Daarna volgen 49 korte zinnen van 3 tot 9 woorden in hetzelfde naampatroon (voornaam plus initiaal). 19 daarvan delen hun tekst letterlijk met een andere naam: "Lightweight and heats evenly. Love it" (4 keer), "The quality is immediately noticeable" (3 keer), "My eggs slide right off. Amazing", "Works great on my induction stove", "The hammered surface really prevents sticking" (elk 2 keer), en meer.
- **Okendo, snijplank:** 4 van de 5 zichtbare reviews hebben een tijdstempel van precies 00:00 op 28 en 29 januari 2026, geen bron (externalProvider), het label Verified Buyer en generieke zinnen ("My knives glide across this like butter"). Twee namen, **Marcus T.** en **Sarah M.**, zijn exact de namen die `content/reviews/summary.md` al als "bestaat in geen enkele bron" (Marcus T.) en als Taima-quote (Sarah M.) aanmerkte.

Waarom dit ertoe doet: de FTC-regel over consumentenreviews (16 CFR Part 465, van kracht sinds oktober 2024) verbiedt verzonnen reviews en het onderdrukken van negatieve reviews, met boetes per overtreding. Als deze blokken uit een import komen (bijvoorbeeld een migratie met gegenereerde reviews), moeten ze eruit. Als ze echt zijn, moet de order-match dat kunnen laten zien.

In de quote-bestanden heb ik alle reviews uit deze patronen uitgesloten (kolom `imported_suspect = yes` in `reviews-tagged.csv`). Geen enkele gekozen quote komt uit deze blokken.

### 3.3 Google ziet iets anders dan de bezoeker

- Op de Pan Pro Standard staat in de structured data (SchemaPlus, JSON-LD) `aggregateRating 4.2 uit 375, "Loox Reviews"` met vijf reviews die allemaal klachten zijn ("Don't say it's non stick when it is clearly not", "Why is my pan magnetic???"). De bezoeker ziet in de widget 4,8 uit 2.226. Twee scores voor hetzelfde product.
- Dezelfde JSON-LD bevat de oude productbeschrijving met verboden claims: "Scientifically proven to retain more nutrients", "Scratch-Resistant", "a lifetime of reliable use".

### 3.4 Gegroepeerde reviews op set-PDP's

Okendo groepeert alle pannen. Op de 12-delige set, de 6-delige set en de Cookware Set Pro staat dus "4.8, 2,226 reviews", terwijl geen enkele zichtbare 5-sterrenreview de 12-delige of 6-delige set bij naam noemt. De enige Okendo-review over de 12-delige set is "I'm missing the large lid" (3 sterren). Groeperen mag, maar het moet op de pagina staan ("Reviews across the Titanium Hammered line").

---

## 4. Tagging: wat de 704 reviews zeggen

Methode: regels op trefwoorden (script in de scratchpad, uitkomst in `reviews-tagged.csv`). Grof: een review kan meerdere thema's hebben; "laag" is 1 tot 3 sterren, "onb." zijn Loox-reviews zonder sterren.

| Thema | 4 en 5 sterren | 1 tot 3 sterren | Onbekend | Pre-sale tickets 90 d (trefwoord) |
| --- | --- | --- | --- | --- |
| Service (support, vervanging, retour) | 219 | 116 | 17 | 35 (retour, garantie) |
| Levering | 111 | 51 | 10 | 50 |
| Plakken en leercurve | 88 | 83 | 39 | 50 |
| Schoonmaken en patina | 75 | 40 | 17 | 67 |
| Gezondheid / PFAS | 50 | 10 | 4 | 165 (materiaal en veiligheid) |
| Prijs | 28 | 68 | 14 | n.v.t. |
| Set | 26 | 9 | 4 | 54 |
| Cadeau | 21 | 8 | 1 | 35 |
| Gewicht | 19 | 5 | 8 | 21 |
| Maat | 17 | 8 | 5 | 95 |
| Deksel | 15 | 10 | 6 | 66 |
| Vertrouwen / echtheid ("scam", "fake", magneet) | 5 | 35 | 6 | 16 |
| Herkomst | 1 (4 sterren, kritisch) | | | 69 |
| Oven | 1 | 0 | | 11 |

Overige tags:

- **Kookplaat:** inductie 11, gas 8, glas/keramisch 4, elektrisch 2. Op glas of elektrisch is er geen enkele positieve quote.
- **Tijd sinds aankoop:** 66 van 704 noemen het (9%). Bijna alles is eerste gebruik of eerste week. Langere termijn: Caliann (wok, "a few months ago"), Stephen B. (plakken na 3 maanden, vervangen), N. W. (wok, twee maanden). Niets na 6 of 12 maanden.
- **Lengte:** 286 lang (>45 woorden), 246 middel, 172 kort. Okendo-reviews zijn gemiddeld 11,6 woorden: te kort om een bezwaar te beantwoorden.
- **Foto:** Okendo pannen 0 foto's op 2.226 reviews; snijplank 10. Trustpilot onbekend in de data.

### 4.1 Wat de kopers vragen tegenover wat de reviews bewijzen

| Pre-sale vraag (rang uit 04) | Bewijs in reviews | Gat |
| --- | --- | --- |
| 1 Materiaal en veiligheid (160) | Sterk op "geen forever chemicals"; zwak op "is het echt titanium" en "waarom magnetisch" | Een review (Olivier L., 1 ster) zegt met een XRF-meting dat het kookoppervlak RVS 321 is. Light Labs 25895 test PFAS, niet de samenstelling. Een materiaalcertificaat is nodig. |
| 2 Deksels (82) | 4 korte Okendo-reviews ("Fits perfectly") | Geen review over welke deksel op welke pan past |
| 3 Herkomst (69) | Geen | Alleen transparantie helpt ("shipped from Asia", Marissa G.) |
| 4 Maat (54) | Een paar | Klanten snappen niet hoe gemeten wordt (J. H.), Small blijkt groot (Emma), mini wok heeft geen wokvorm (Paulette S.) |
| 5 Schoonmaken (52) | Sterk | Verkleuring is de grootste kritiek; uitleg ontbreekt op de PDP |
| 6 Plakken (51) | Sterk, mits met techniek | De PDP-claim "Naturally Non-Stick" lokt precies de 1-sterrenreviews uit |
| 7 Oven en vaatwasser (30) | Drie korte bevestigingen | Geen kritiek: dit is een informatievraag |
| 8 Inductie en kookplaat (24) | Inductie en gas ja | Glas en elektrisch: alleen kritiek (Palma O.) |

Belangrijkste les: de reviews bewijzen vooral wat kopers al geloven (gezond, makkelijk schoon) en service. Ze bewijzen nauwelijks wat kopers vóór aankoop vragen (maat, deksel, herkomst, kookplaat). Dat lossen we op met (a) de Okendo-export en filters, en (b) betere vragen in het reviewverzoek.

### 4.2 Reviewverzoek verbeteren (voorstel, niets aangepast)

Okendo ondersteunt reviewer-attributen en productvragen. Drie vragen leveren het ontbrekende bewijs:

- "What cooktop do you use?" (Induction, Gas, Electric coil, Glass or ceramic)
- "Which size did you buy, and how many do you cook for?"
- "How long have you been cooking with it?" (in een tweede verzoek na 60 dagen)

Plus de vraag om een foto van het eerste ei. Eén verzoek per order: niet tegelijk Trustpilot en Okendo vragen (zie `research/deep/03`).

---

## 5. Advies: of en hoe de rating getoond wordt

Onderzoek (Spiegel Research Center): de koopkans piekt bij 4,2 tot 4,5 sterren; een score dicht bij 5,0 wordt minder geloofd. Siraat toont 4,8 terwijl de bekendste openbare score (Trustpilot) 3,9 is en Google 4,2 ziet. Dat verschil is precies wat bezoekers "fake" laat zeggen (47 van 154 lage Trustpilot-reviews).

Advies, in volgorde:

1. **Eerst de herkomst ophelderen** (hoofdstuk 3). Reviews uit een import zonder order-match verwijderen. Dat is geen cosmetiek maar een juridisch risico. Verwachting: de score zakt dan richting 4,3 tot 4,6, en dat is de zone waarin vertrouwen en koopkans het hoogst zijn. Niet sturen op een doelscore: we tonen wat er is.
2. **Eén score per product, één bron.** De Loox-structured data uitzetten of laten verwijzen naar dezelfde bron als de widget. Geen twee scores voor één pan.
3. **Score altijd met verdeling.** Toon het getal nooit los: altijd de vijf balken, het aantal en een klikbare regel "Read the 3-star and lower reviews". Kritiek verbergen is precies wat de FTC-regel verbiedt en wat kopers wantrouwen.
4. **Gegroepeerd? Zeg het.** Op set-PDP's: "4.8 from 2,226 reviews across the Titanium Hammered line" en een standaardfilter op het eigen product zodra er genoeg zijn (vanaf circa 20).
5. **Merkantwoord bij elke kritische review.** Nu 5 antwoorden op 2.226. Doel: elke review van 1 tot 3 sterren een antwoord in de toon van `quotes-per-bezwaar.csv` (eerlijk, met de techniek of de oplossing, geen excuusformules). Dit is werk voor support, niet voor deze opdracht.
6. **In mails geen sterscore.** Daar werken letterlijke quotes die het bezwaar raken, met naam en product (PLAYBOOK 11, skill sectie 7). Okendo-quotes pas gebruiken na de export en alleen met Verified Buyer.

---

## 6. Hoe de quote-bestanden zijn gemaakt

- Top 8 bezwaren = de acht pre-sale thema's uit `research/deep/04` (hoofdstuk 2, punt 3), ververst met een trefwoordtelling in Gorgias (484 pre-sale tickets, 90 dagen, alleen aantallen).
- Per bezwaar: 3 quotes van 4 of 5 sterren, max 120 tekens, letterlijk (script controleert dat elke quote woordelijk in de bron staat), plus 1 kritische review met het juiste antwoord op basis van `content/facts` (guidance 5326403, 5831676, macro 247042, 347467).
- Uitgesloten: verdachte importblokken, reviews die een concurrent noemen, quotes over de oude 100-day trial of lifetime, en zinnen met verboden claims ("the handle stays cool", "titanium coating").
- Bij oven en vaatwasser bestaat geen kritische review; daar staat de dichtstbijzijnde (plakken) met de uitleg dat dit een informatievraag is.
- Gaten staan als lege regels met "GAT" in `quotes-per-product.csv` (Pot Set, 12-delig, 6-delig, Deep Pan, Pizza Steel, Mini en Small).
