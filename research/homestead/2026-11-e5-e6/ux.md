# UX- en conversiereview Homestead E5 en E6 (november 2026)

Datum: 5 november 2026. Mails: E5 "Weekly Recipe: Thanksgiving Sides" (di 10 nov, E30) en E6 "One Pan for Life, at Black Friday Prices" (wo 11 nov, E90, founder-brief). Beide in een US- en een INTL-versie.

**Bron en beperking.** De Figma-nodes (bestand j4lQNzqaqdfplcqgLjf4Jn, nodes 7286-4272 en 7318-8290) waren niet te openen: de Figma-MCP weigert met "you don't have edit access to this file", ook voor alleen lezen (create_session, get_metadata en get_screenshot). Deze review steunt dus op de samenvatting van de mails (platte tekst met logo-header, zwarte "Plain Text"-balk als placeholder, tekstlinks als knoppen, geen beelden, alleen in E6 prijzen: $144, save $336, 4 gifts, waterfilter $450 value, ook in INTL; P.S. met BF-aanbod; footerregel "Offer valid while supplies last 11/01 to 11/30"), op `research/homestead/kalender-november-2026.md`, PLAYBOOK.md, DECISIONS.md en onze eigen ontwerpen van 4 november (`klaviyo/templates/v3/campaigns/pricelist-1104` en `win-order-back-1104`, previews op 375 px). Pixelmaten hieronder zijn schattingen voor 375 px breed; controleer ze in Figma zodra Floris of Homestead leestoegang geeft (bestand delen met het Figma-account van de MCP, of exporteer de twee frames als PNG).

## 0. Kader: wat bij Siraat werkt

- Founder-brieven klikken 1,3 procent tegenover 0,3 tot 0,6 procent voor beeldmails (PLAYBOOK §1). Platte tekst is dus geen probleem, het is juist ons sterkste format. De vraag is niet "beeld of tekst", maar: krijgt de lezer die wil kopen snel een duidelijk kliktarget en een prijs?
- Floris keurde op 4 november twee stijlen goed die we hier als referentie gebruiken:
  - **Brief met één productkaart** (`pl-us-c-letter`, `wb-*-b-letter`): crème kolom, vaste lockup-header, topbar "VIP BLACK FRIDAY SALE IS LIVE", aanhef en twee korte alinea's van Benjamin, daarna één productkaart (normale productfoto, badges "JUST ARRIVED" en "SELLING FAST", doorgestreepte compare-at, prijs, kortingssticker in geel), één brede knop (volle breedte, pil, "GET THE 12-PIECE DEAL →"), friction reducer eronder, twee zinnen afsluiting, ondertekening "Benjamin / Founder, Siraat". De eerste knop staat rond 1.100 px, de kaart al rond 470 px.
  - **Rich** (`wb-us-c2`): donkere hero met Instrument Serif/gele kop, gele #FFB800 knop met zwarte tekst direct onder de kop (boven de vouw), productraster 2 x 3 met echte productfoto's, prijs, compare-at en geel kortingslabel, tweede knop onderaan.
- Vaste regels die hier raken: vaste header en footer uit `partials/` (CLAUDE.md), topbar "BLACK FRIDAY SALE IS LIVE" (DECISIONS 31 okt), prijzen nooit in USD buiten de US (PLAYBOOK v5, macro `{{PRICE:..}}`), de filter is altijd "chance to win a PFAS water filter", nooit gratis of "value" alsof hij erbij zit (PLAYBOOK §11), 30-day returns en 75-year warranty, 100,000+ happy customers, ondertekening Benjamin. Geen harde einddatum zolang Floris die niet bevestigt (DECISIONS 7 okt, open vraag einde sale in de kalender §3). Geen "next batch"-taal; wel "Just arrived and selling fast" (DECISIONS 1 nov).

---

## E5 · Weekly Recipe: Thanksgiving Sides

### 1. Wat werkt al (houden)

- **Recept als waarde vóór verkoop.** Pijler 4 ("Made for people who love to cook"), past bij E30 en bij de week voor Thanksgiving. Een receptmail is de mail die mensen bewaren en terugzoeken; dat helpt de opens van de volgende mails.
- **Platte-tekstgevoel.** Leest als een bericht, niet als een folder. Laat in Gmail minder snel het Promoties-gevoel achter en past bij onze best klikkende vorm.
- **Logo-header.** Goed, mits het de vaste lockup (monogram + SIRAAT) uit `partials/header.html` is en niet een losse woordmerk-export.
- **Geen prijzen in de kern van het recept.** Een receptmail die meteen schreeuwt verliest het vertrouwen dat het recept opbouwt. Het aanbod hoort er wel in, maar als eigen blok (zie hieronder), niet in de bereidingsstappen.

### 2. Wat de conversie remt

| Punt | Wat er nu gebeurt (volgens samenvatting) | Waarom het remt | Ernst |
|---|---|---|---|
| Zwarte "Plain Text"-balk | Placeholder bovenaan | Eerste wat je ziet is een lege of nietszeggende balk. Moet de vaste topbar worden: "BLACK FRIDAY SALE IS LIVE" (DECISIONS 31 okt), klikbaar naar de BF-collectie. Dat is meteen het eerste kliktarget. | Hoog, en makkelijk |
| Eerste scherm op 375 px | Header (~70 px) + balk (~40 px) + aanhef en intro | Op een iPhone van 667 tot 844 px hoog zie je alleen tekst, geen beeld, geen product, geen knop. De lezer weet niet welke pan dit recept maakt. | Hoog |
| Scrollen tot de eerste knop | Eerste link pas na intro en (een deel van) het recept. Een recept van 300 tot 450 woorden is op 375 px met 16/26 px tekst ongeveer 1.200 tot 1.700 px. | Bij de schatting staat het eerste kliktarget pas op scherm 2 tot 3. In onze briefmail staat de kaart op ~470 px en de knop op ~1.100 px. | Hoog |
| Tekstlinks als knoppen | Onderstreepte links in de tekst | Kliktarget van een tekstlink is ~18 tot 22 px hoog, onder het minimum van 44 x 44 px (Apple HIG / WCAG 2.5.5). Mis-tikken en niet-zien. In de brief van 4 nov gebruiken we één echte knop en hielden we toch het briefgevoel. | Middel |
| Scanbaarheid recept | Platte tekst | Ingrediënten en stappen als doorlopende tekst zijn op mobiel lastig te volgen in de keuken. Ingrediënten moeten een lijst zijn, stappen genummerd, met tijd en aantal personen bovenaan. | Middel |
| Geen beeld | Geen foto van het gerecht of de pan | Een recept zonder foto van het eindresultaat wordt minder vaak gekookt en de pan blijft abstract. Eén foto van het gerecht in de pan (flash-stijl of shoot) doet beide. | Middel |
| Geen prijs | Product niet genoemd met prijs | Wie overtuigd raakt door het recept, moet nog doorklikken om te weten of het $144 of $440 is. In BF-week is "70% off" juist de reden om nu te klikken. | Middel |
| BF-aanbod alleen in P.S. | Aanbod helemaal onderaan | De kalender zegt zelf "BF-band onder recept"; de P.S. alleen is te laat en te klein. P.S. wordt gelezen, maar alleen door wie tot het einde scrolt. Het aanbod moet ook kort boven de vouw staan (topbar) en als blok direct na het recept. | Hoog |
| Footerregel "Offer valid while supplies last 11/01 to 11/30" | Klein in de footer | Noemt een einddatum die nog niet vaststaat (kalender §3: Floris zei "eindigt gewoon Black Friday") en "while supplies last" zonder echte voorraadgrens. Weg, of pas na bevestiging van Floris. | Hoog (juist) |
| Contrast | Onbekend zonder screenshot | Check: bodytekst minimaal #282828 op crème/wit (ruim AA). Grijze tekst niet lichter dan #727272 en alleen voor secundaire regels (4,6:1 op wit, net AA). Geel #FFB800 nooit als tekst op wit (1,9:1); alleen als vlak met zwarte tekst (11:1). | Middel |
| Alt-teksten | Geen beelden, dus alleen logo | Logo-alt "Siraat". Als er een gerechtfoto bijkomt: beschrijvende alt ("Roasted green beans with crispy shallots in a Siraat titanium pan"), niet "image1". | Laag |
| INTL | Geen prijzen in E5 | Goed, zo houden. Als er een prijs of kaart bijkomt: alleen via `{{PRICE:..}}` of een aparte INTL-versie zonder USD. Ook geen "Free shipping from the US" in INTL. | Laag (nu), hoog bij toevoegen prijs |

### 3. Aanbevolen blokopbouw

#### Optie A · "Plain text plus" (brief-gevoel, 1 à 2 beelden, echte knoppen)

Doel: het recept blijft de hoofdzaak, maar binnen het eerste scherm zie je wat je kookt en waarmee, en er is één duidelijke knop. Doellengte ~2.800 tot 3.200 px op 390 px inclusief footer.

| # | Blok | Doel | Inhoud | Knoptekst | Positie |
|---|---|---|---|---|---|
| 1 | Topbar | Aanbod meteen zichtbaar, eerste kliktarget | "BLACK FRIDAY SALE IS LIVE", klikbaar naar `/collections/black-friday-sale` | (hele balk is link) | 0 px |
| 2 | Vaste header | Merk | Lockup uit `partials/header.html` | | ~40 px |
| 3 | Intro van Benjamin | Waarom dit recept | Aanhef + 2 korte zinnen ("Three sides I make every year. All in one pan, all on one burner.") | | ~110 px |
| 4 | Beeld 1: gerecht in de pan | Belofte van het recept en de pan in één beeld | Foto 600 x 450 (4:3), gerecht in de Pan Pro, flash-stijl of shoot; geen tekst in het beeld | (beeld linkt naar receptpagina of product) | ~260 px, eindigt rond 540 px: binnen het eerste scherm |
| 5 | Recept-kop + feiten | Scanbaar | Naam van het gerecht, regel "Serves 6 · 25 min · Pan Pro Standard 11″" (INTL `{{SIZE:28}}`) | | ~560 px |
| 6 | Ingrediënten | Scanbaar | Opsomming met bullets, hoeveelheden eerst | | |
| 7 | Bereiding | Scanbaar | Genummerde stappen, max 2 regels per stap, één pan-tip (bijv. voorverwarmen op middelhoog, olie als het glanst) | | |
| 8 | Knop 1 | Wie wil koken, kan de pan kopen | Brede knop, volle breedte op mobiel, min 48 px hoog. Friction reducer eronder: `{{FRICTION}}` | "Shop the pan" (DECISIONS 9 okt: receptcampagnes mogen "Shop the pan") | ~1.300 tot 1.500 px |
| 9 | BF-band (compact) | Aanbod zonder het recept te overstemmen | Eén strook: "Black Friday: up to 70% off, plus 4 gifts with every order." met de pan als mini-kaart: foto, "Titanium Hammered Pan Pro", `{{PRICE:standard}}` met compare-at alleen US | "Shop Black Friday" | direct na knop 1 |
| 10 | Recept 2 en 3 (kort) | Meer waarde, meer redenen om de pan te gebruiken | Per side 3 regels + link "Full recipe" | | |
| 11 | Afsluiting + ondertekening | Brief-gevoel | "Happy Thanksgiving. Benjamin / Founder, Siraat" en P.S. met het aanbod (zoals nu) | P.S.-link "See the Black Friday prices" | |
| 12 | Vaste footer | | `partials/footer.html`, zonder de "11/01 to 11/30"-regel tot Floris de einddatum geeft | | |

Beeld 2 is optioneel: een productkaart in blok 9 (normale productfoto op crème, zoals in `pl-us-c-letter`). Dat is het tweede beeld; meer niet, anders verliest de mail het briefgevoel.

#### Optie B · "Rich" recept

Doel: recept als visueel verhaal, aanbod als tweede laag. Lengte ~3.400 px, binnen de grens van 3.600 px (PLAYBOOK §12).

| # | Blok | Doel | Inhoud | Knoptekst | Positie |
|---|---|---|---|---|---|
| 1 | Topbar + vaste header | | zoals A | | 0 px |
| 2 | Hero | Haak | Gerecht in de pan, 1200 x 900, kop als PNG (TT Ramillas) of live Instrument Serif Italic: "Three sides. One pan." Eyebrow "WEEKLY RECIPE · THANKSGIVING" | | ~110 px |
| 3 | Knop 1 direct onder de hero | Kliktarget boven de vouw | Gele #FFB800 knop met zwarte tekst | "Get the recipes" (naar receptpagina) of "Shop the pan" | ~560 px |
| 4 | Drie sides als kaarten | Scanbaar | Per side: foto (4:3), naam, "Serves 6 · 20 min", 3 regels, link "Full recipe →" | | |
| 5 | "The pan behind it" | Product | Eén productkaart via `{{BLOCK:productcard}}`, prijs via macro, compare-at alleen US en alleen bevestigd anker | "Shop the pan" | |
| 6 | BF-blok | Aanbod | "Up to 70% off + 4 gifts" met `{{BLOCK:gifts5 style="row"}}` (filter = "Chance to win") | "Shop Black Friday" | |
| 7 | Eén review | Bewijs | Letterlijke Trustpilot-review over koken (uit `content/reviews/top.md`) | | |
| 8 | Knop 2 + friction reducer | | | "Shop Black Friday" | |
| 9 | Vaste footer | | | | |

### 4. Meten (E5)

- **Test**: A (plain text plus) tegen de Homestead-versie (controle) op E30, 50/50. Eén variabele per test is hier niet haalbaar zonder twee rondes; de vergelijking is dus "pakket A tegen controle". Optie B pas testen in E8 (17 nov, ook recept, ook E30) tegen de winnaar van E5, zodat we twee recepttests in één maand hebben.
- **Winnaar op**: omzet per ontvanger (RPR, Placed Order met conversiemetric RSNxYV, 5 dagen attributie). Unieke klikratio als tweede metric, nooit opens (PLAYBOOK §6).
- **Bewakingsmetrics**: uitschrijfratio (stop boven 1,5 procent vanaf 1.000 ontvangers, kalender-vangrail), spam boven 0,15 procent.
- **Diagnose**: klikverdeling per blok via UTM `utm_content` per link (topbar, beeld, knop 1, BF-band, P.S.); aandeel kliks boven 600 px. Verwachting: in A komt minstens een derde van de kliks uit topbar en beeld/knop 1.
- **Steekproef**: E30 is klein. Bij ~1 procent klik en een paar tienduizend ontvangers is alleen een groot verschil zichtbaar; behandel een klein verschil als richting, niet als bewijs.

---

## E6 · One PFAS-free pan for life (founder-brief)

### 1. Wat werkt al (houden)

- **Founder-brief van Benjamin.** Ons sterkste format (1,3 procent klik). Kalender: "vorig jaar beste pre-BF-mail op wo" voor dit type.
- **Eén product, één idee.** Pan Pro Standard, pijler 3 "Built for life". Precies wat een brief moet doen.
- **Concreet aanbod met getallen.** $144, save $336, 4 gifts. Cijfers boven adjectieven (PLAYBOOK §1). Dat $144 en compare-at $480 zijn gelijk aan wat Floris op 4 nov goedkeurde in `wb-us-c2` (Pan Pro Standard $144, doorgestreept $480).
- **P.S. met aanbod.** De P.S. wordt in brieven bovengemiddeld gelezen; houden als tweede plek, niet als enige.
- **Uitsluiten Pan Pro Standard-kopers.** Goed idee; segment moet nog gebouwd worden (kalender).

### 2. Wat de conversie remt

| Punt | Wat er nu gebeurt | Waarom het remt | Ernst |
|---|---|---|---|
| "Plain Text"-balk | Placeholder | Zelfde als E5: wordt de topbar "BLACK FRIDAY SALE IS LIVE". | Hoog, makkelijk |
| Prijs zonder beeld | $144 en "save $336" staan in de tekst | De lezer moet zich de pan voorstellen. In onze brief van 4 nov staat precies hier één productkaart met foto, compare-at en kortingslabel, en dat behoudt het briefgevoel. | Hoog |
| Eerste knop laat | Tekstlink(s) in of na het verhaal, aanbod pas in de P.S. | Een founder-brief van ~250 tot 350 woorden is op 375 px ~900 tot 1.200 px. Als het aanbod pas in de P.S. staat, zit het eerste duidelijke kliktarget rond 1.200 tot 1.500 px, en dan als tekstlink. | Hoog |
| BF-aanbod alleen in P.S. | | Voor E90 (lezers die al weten wat Siraat is) is de prijs juist de nieuwe informatie. Die hoort halverwege de brief, niet alleen onderaan. | Hoog |
| Tekstlinks | | 44 x 44 px kliktarget ontbreekt; zie E5. Eén echte knop is genoeg. | Middel |
| INTL in USD | $144, $336, $450 staan ook in INTL | Mag niet (PLAYBOOK v5: nooit USD of inch buiten de US). Een Brit ziet $144 en weet niet wat hij betaalt, inclusief invoerrechten. INTL: prijzen via `{{PRICE:standard}}` / `{{WAS:standard}}` (UK £124 enz.) of zonder bedragen ("70% off, plus 4 gifts with every order"). Gifts in INTL: `{{GIFTS:total}}`, voor HK/ME/rest "4 free gifts" zonder bedrag. | Hoog (fout) |
| Waterfilter "$450 value" | Als onderdeel van de 4 gifts | Regel: de filter is altijd "a chance to win a $450 PFAS water filter", nooit alsof hij gratis meekomt. Met "value" erachter leest het als een gift die je krijgt. Formulering: "4 gifts with every order, including a chance to win a $450 PFAS water filter" (US), INT via `{{GIFTS:filterline}}`. | Hoog (claim) |
| "Save $336" | Rekensom op compare-at $480 | Klopt met de BF-kaart van 4 nov, maar DECISIONS noemt $439 als bevestigd anker voor Pan Pro Standard (7 okt). Laat Floris bevestigen welke compare-at nu in Shopify staat; de besparing moet daaruit volgen. | Middel |
| "One pan for life" | Kop/onderwerp | Floris: nooit "lifetime" (DECISIONS 1 okt), wel "75-year warranty". "For life" als beeldspraak is merktaal ("Built for Life" staat in de footer), maar in de buurt van de garantie moet "75-year warranty" staan, niet "lifetime warranty". Check de copy (copy.md van de andere agent). | Middel |
| Footerregel 11/01 to 11/30 | | Einddatum niet bevestigd; "while supplies last" is geen echte grens. Weg tot Floris beslist. | Hoog |
| Contrast en alt | | Als E5. Als er een productkaart bijkomt: alt "Titanium Hammered Pan Pro, 11 inch, $144" (US) en zonder bedrag in INTL, of via macro. | Middel |
| Platte-tekstgevoel | | Behouden: geen hero, geen rasters, geen iconenrij. Eén kaart en één knop zijn genoeg; dat bewees `pl-us-c-letter`. | |

### 3. Aanbevolen blokopbouw

#### Optie A · "Plain text plus" (aanbevolen standaard)

Model: `pricelist-1104/pl-us-c-letter` en `win-order-back-1104/wb-us-b-letter`. Doellengte ~2.700 tot 3.000 px op 390 px inclusief footer.

| # | Blok | Doel | Inhoud | Knoptekst | Positie |
|---|---|---|---|---|---|
| 1 | Topbar | Aanbod en eerste kliktarget | "BLACK FRIDAY SALE IS LIVE" | (balk is link) | 0 px |
| 2 | Vaste header | | Lockup | | ~40 px |
| 3 | Aanhef + opening | Haak | "Hi {{ first_name\|default:'there' }}," en 2 tot 3 korte alinea's: waarom één pan ("I would rather sell you one pan you keep than six you replace."), wat het is (pure titanium cooking surface, no coatings) | | ~110 tot 450 px |
| 4 | Productkaart (beeld 1) | Prijs en product zichtbaar binnen ~1,5 scherm | `{{BLOCK:productcard}}`: normale productfoto Pan Pro Standard op crème, badge "SELLING FAST" alleen als waar, naam "Titanium Hammered Pan Pro, {{SIZE:28}}", `{{PRICE:standard}}` met `{{WAS:standard}}` alleen US, geel label "-70%", regel "+ 4 gifts with every order" | (kaart is link) | ~470 tot 950 px |
| 5 | Eén alinea na de kaart | Bewijs | 2 zinnen: labtest (Light Labs, rapport 25895), "covered for 75 years" | | |
| 6 | Knop | Hoofdactie | Brede pil-knop volle breedte, min 48 px hoog; stijl zoals de brief van 4 nov (donker met gele tekst) of geel met zwarte tekst. Eronder `{{FRICTION}}` (US "Free shipping from the US. 30-day returns. 100,000+ happy customers.", INT "Free shipping, duties paid. ...") | "Get the pan for $144" (US); INT "Get the pan at 70% off" of met `{{PRICE:standard}}` | ~1.050 tot 1.150 px |
| 7 | Afsluiting | Briefgevoel, bezwaar wegnemen | "You have 30 days to send it back unused. Questions about sizes? Reply and our team will help." | | |
| 8 | Ondertekening | | Benjamin / Founder, Siraat | | |
| 9 | P.S. | Tweede kans, gifts | "P.S. Every order ships with 4 gifts, including a chance to win a $450 PFAS water filter." + tekstlink | "See the Black Friday prices" | |
| 10 | Vaste footer | | Zonder "11/01 to 11/30" | | |

Optioneel beeld 2: niet nodig. Als er één bij moet, dan een kleine GIF of still uit de chef-video (ei glijdt, zonder ondertitels) tussen blok 3 en 4, max 300 KB.

#### Optie B · "Rich" (Benjamin-brief als hero, productkeuze eronder)

Model: `win-order-back-1104/wb-us-c2`, maar met de brief bovenaan in plaats van een grote kop.

| # | Blok | Doel | Inhoud | Knoptekst | Positie |
|---|---|---|---|---|---|
| 1 | Topbar + vaste header | | | | 0 px |
| 2 | Hero | Haak + aanbod boven de vouw | Pan Pro op donker (shoot of packshot), kop Instrument Serif Italic "One pan. 75 years.", subregel "Pan Pro Standard, $144. Was $480." (INT via macro of zonder bedrag) | | ~110 px |
| 3 | Knop 1 | Kliktarget boven de vouw | Geel #FFB800, zwarte tekst, volle breedte | "Shop the Pan Pro" | ~520 tot 600 px |
| 4 | Korte brief van Benjamin | Vertrouwen | 3 alinea's, ondertekend, foto-loos | | |
| 5 | Maatkiezer | Juiste maat, minder twijfel | Vier kaarten Mini, Small, Standard, Large met foto, `{{SIZE:..}}` en `{{PRICE:..}}`, geen doorstreping op Mini/Small/Large (compare-at niet bevestigd als anker) | (kaarten zijn links) | |
| 6 | Gifts | Aanbod verzwaren | `{{BLOCK:gifts5}}` (filter "Chance to win") | | |
| 7 | Twee reviews | Bewijs | `{{BLOCK:reviews3 n="2"}}` | | |
| 8 | Knop 2 + friction reducer | | | "Shop the Pan Pro" | |
| 9 | Vaste footer | | | | |

Let op: B is een beeldmail en valt waarschijnlijk in de 0,3 tot 0,6 procent-klikband. Alleen inzetten als test, niet als standaard.

### 4. Meten (E6)

- **Test**: drie armen op E90 als het volume het toelaat (E90 is groot genoeg, US ~79.000 en INT ~54.000 engaged volgens de segmentcheck van 4 nov): controle (Homestead platte tekst), A (plain text plus), B (rich). Anders twee armen: controle tegen A; B later in E9 (18 nov, ook een Benjamin-brief).
- **Winnaar op**: omzet per ontvanger (RPR, 5 dagen, conversiemetric RSNxYV). Bij een brief is klikratio hoog maar kan de omzet tegenvallen; RPR beslist. Tweede metric: conversie per klik (orders / unieke klikkers), om te zien of de kaart kwalitatievere kliks oplevert.
- **US en INT apart rapporteren.** De INTL-versie met USD is de meest waarschijnlijke verliezer; de vergelijking INT-oud tegen INT-nieuw meet ook het effect van lokale prijzen.
- **Bewaking**: uitschrijfratio en spam per arm (stop boven 1,5 procent afmelding of 0,15 procent spam vanaf 1.000 ontvangers). Een brief met kaart mag niet meer afmeldingen geven dan de controle; doet hij dat wel, dan voelt hij te commercieel.
- **Diagnose**: UTM per link (topbar, kaart, knop, P.S.). Als in A meer dan de helft van de kliks op kaart en knop valt en de P.S.-kliks dalen, dan zat het aanbod in de controle te laag.
- **Geen winnaar op opens** en geen automatische winnaar na een paar uur: laat de campagne 5 dagen attributie draaien vóór het besluit.

---

## Samenvatting voor Homestead (kort, te delen)

1. Zwarte "Plain Text"-balk vervangen door de topbar "BLACK FRIDAY SALE IS LIVE" (link naar de BF-collectie).
2. Tekstlinks blijven mogen, maar elke mail krijgt één echte, brede knop (min 48 px hoog) met friction reducer eronder.
3. E5: één foto van het gerecht in de pan binnen het eerste scherm, recept als lijst en genummerde stappen, BF-band direct na het recept, P.S. blijft.
4. E6: één productkaart (foto, prijs, compare-at, gifts) halverwege de brief, knop "Get the pan for $144", P.S. blijft.
5. INTL zonder USD: prijzen en gift-waarden in lokale valuta of zonder bedrag.
6. Filter is "a chance to win a $450 PFAS water filter", nooit als gift met "value".
7. Footerregel "Offer valid while supplies last 11/01 to 11/30" eruit tot Floris de einddatum bevestigt.
8. Testen op omzet per ontvanger, niet op opens.
