# Concurrenten-inbox: overzicht na dag 10 (stand 22 okt 2026, ca. 08:40 UTC)

Bron: alle mails sinds 12 okt 00:00 UTC aan lolagroothuis+<code>-<scenario>@gmail.com, per regel in `tijdlijn.csv`. Acties uit `log-*.csv` (HexClad en Our Place b handmatig door Floris, geen log). Kortingscodes staan nergens uitgeschreven.

## Aantal mails per merk en scenario

| Merk | w | b | c | co | Totaal | Status inschrijving |
|---|---|---|---|---|---|---|
| HexClad | 7 | 12 | 11 | n.v.t. | 30 | w/b/c handmatig (Floris), co niet gedaan |
| Our Place | 7 | 13 | 9 | 0 | 29 | alles gelukt; c pas om 11:18 in winkelwagen |
| Caraway | 5 (op hex-w) | 0 | 0 | 0 | 5 | w/b/c via footer "gelukt", maar geen enkele mail op cw-adressen; beide Caraway-mails kwamen op hex-w binnen |
| Made In | 0 | 0 | 0 | 0 | 0 | w/b/c footer "Thanks! You've been subscribed", co gestopt (telefoon verplicht) |
| Okura | 0 | 0 | 0 | 0 | 0 | w/b/c captcha, alleen co (checkout zonder betaling, opt-in aan) |
| Plateful | 0 | 0 | 0 | 1 | 1 | w/b/c captcha, co gelukt |
| Taima | 0 | 0 | 0 | 0 | 0 | niet gestart |

## Timing per adres (uren na eerste actie)

| Adres | 1e mail | 2e mail | 3e mail |
|---|---|---|---|
| hex-w | 0,0 welkom (benadering) | 1,5 browse "Still thinking about it?" | 25,6 browse 2 "The last cookware you'll ever need"; welkomreeks 0, 24, 48, 120 en 192,1 ("To know us is to 🫶 us") |
| hex-b | 0,0 welkom (benadering) | 1,0 browse "Great choice, chef!" | 25,0 browse 2 "Lasts a Lifetime – Guaranteed!" |
| hex-c | 0,0 welkom (benadering) | 0,7 cart "Your kitchen needs this!" | 48,0 welkom 3, cart 2 "The last cookware you'll ever need" pas na 168,7 uur (7 dagen), welkom 5 na 192,1 |
| Caraway (hex-w) | 0,0 welkom "Greetings From Caraway" | 12,0 "Our Top Caraway Picks" | 36,1 "Are You Cooking Clean?" (PFAS-vergelijking), daarna 84,1 welkom 4 (set, $230) en 132,2 welkom 5 "The Problem: Traditional Cookware Is Toxic" |
| op-b | 0,0 welkom (benadering) | 4,0 browse "You Left Before the Good Part" | 24,0 welkom 2 "Did you hear?", 28,0 browse 2 "We Can't Wait Forever 💔", 42,4 "Party of One" (campagne minis); daarna alleen campagnes, laatste 234,4 "Set Savings" |
| op-w | 0,07 welkom (4 min na popup) | 24,2 welkom 2 "Did you hear?" | |
| op-c | 0,08 welkom | 24,2 welkom 2 "Did you hear?" | (nog steeds geen cartmail, ook na 150 uur niet; alleen campagnes) |
| pf-co | 12,5 abandoned checkout | | |

HexClad-tijden zijn benaderd met de eerste welkomstmail als actietijd; de echte actie lag rond 10:30 tot 10:38 UTC, dus de browse- en cartmails komen eerder 0,7 tot 1,5 uur na de actie dan later.

## Patroon na dag 2

- **Vaste stap van 24 uur.** Our Place (welkom 2 en browse 2), HexClad (browse 2) en Caraway (welkom 2 naar 3) sturen hun vervolgmail allemaal ongeveer 24 uur na de vorige. Niemand gebruikt nog een kortingscode als tweede stap.
- **HexClad browse 2 = garantie in plaats van korting.** Onderwerpen "Lasts a Lifetime – Guaranteed!" en "The last cookware you'll ever need", met hetzelfde bekeken product, reviews en "Complete your order".
- **Our Place stuurt een verlopen sale door.** "Did you hear?" en "We Can't Wait Forever 💔" duwen October Prime Deals terwijl de kleine lettertjes zeggen dat die op 12 okt 23:59 PT eindigde. Slordig, en de browse 2 toont nog steeds geen bekeken product.
- **Caraway welkom 3 is materiaal-educatie.** Traditionele non-stick (PFAS/PTFE) tegenover hun keramiek, "getest op 220+ PFAS", plus vaste dollarbedragen korting op sets ($95 tot $190) zonder code.

## Patroon na dag 3

- **HexClad welkom 3 na precies 48 uur** ("Why folks love us", reviews) naar w, b en c tegelijk. De welkomreeks loopt dus in vaste stappen van 24 uur naast de browsemails.
- **HexClad browse 3 = betalen in termijnen.** "Price holding you back? We got you." legt Affirm uit in vier stappen. Na drie browsemails nog steeds geen kortingscode: eerst garantie, dan reviews, dan gespreid betalen.
- **Campagnes beginnen op dag 3.** Our Place "Party of One" en "Must See" (bestsellers, cadeau bij $300+), HexClad bakeware-reviews vanaf hello@. Our Place verstuurt dezelfde campagne gespreid over 9 uur.
- **Nog steeds geen enkele kortingscode** bij HexClad, Our Place en Caraway na 3 dagen. Alleen Plateful gaf 10% in de checkoutmail.

## Patroon na dag 4

- **Drempelcadeau is het BFCM-voorspel.** Our Place: gratis Titanium Perfect Pot Pro bij $300+ ("For You: A Free Gift"), na "Must See" met dezelfde drempel. Precies het idee van Homestead (vanaf $400 een gratis pizza steel).
- **Caraway welkom 4 duwt sets** met een dollarbedrag ("Save $230 on an all-in-one set"), nog steeds zonder code.
- **HexClad browse 3 ook voor hex-b**: "Buy now, pay later?". Termijnbetaling is dus een vaste stap, geen losse campagne.
- **Na 4 dagen nog steeds geen kortingscode** bij HexClad, Our Place en Caraway.

## Patroon na dag 5

- **Ritme campagnes:** Our Place stuurt elke dag om 05:15 UTC een campagne naar op-b en daarna gespreid naar c en w; HexClad stuurt om de dag een campagne via een apart segment (b en c, niet w).
- **Inhoud naast aanbod:** Our Place "One Oven. Endless Cravings." (8 bereidingen) en HexClad een pop-up evenement in New York. Geen korting, wel reden om te openen.
- **Nog steeds geen kortingscode** na 5 dagen bij HexClad, Our Place en Caraway.

## Patroon na dag 6

- **HexClad welkom 4 na precies 120 uur** ("Gordon Ramsay ❤️‍🔥 these pans", preview "Here's why") naar w, b en c binnen 2 minuten. Het ritme is dus 0, 24, 48 en daarna 120 uur: na drie dagen achter elkaar een pauze van drie dagen. Inhoud is puur autoriteit (17 Michelin-sterren, "Buy HexClad once, and you'll use it for life"), plus refer a friend en een winactie, zonder product of prijs.
- **Caraway welkom 5 na 132 uur is een angst-hook:** "The Problem: Traditional Cookware Is Toxic" met "a single scratch on a PTFE-coated pan releases 9,100+ microplastics". Daarna de oplossing: sets met tot $700 besparing, of de Fry Pan als kleine instap ("Not Ready for a Full Set?"), en 30 dagen geld-terug. Caraway loopt nu in stappen van 48 uur (36, 84, 132).
- **Our Place verstuurt elke campagne in dezelfde volgorde:** b om 07:15, c 7 uur later, w 9 uur later. Opnieuw geen korting.
- **Na 6 dagen nog steeds geen kortingscode** bij HexClad, Our Place en Caraway. Plateful blijft het enige merk met een code.

## Patroon na dag 7

- **Our Place verschuift het tijdstip.** "Look Closer" ging om 09:15 UTC naar op-b (niet 05:15 of 07:15), daarna weer c 7 uur en w 9 uur later. De volgorde b, c, w blijft vast, het startuur niet. Vanochtend om 05:15 kwam al de volgende campagne ("Mutually Beneficial") voor op-b, dus twee campagnes binnen 20 uur.
- **Our Place lanceert een verbeterde titanium-lijn.** "Look Closer" (preview "See how we refined our bestselling collection") presenteert Titanium Pro, Refined: een fijnere micro-textuur die makkelijker schoonmaakt, NoCo nonstick die "thrives under high heat", zonder prijs of korting. Dit is directe concurrentie op titanium en het verhaal is "we hebben het nog beter gemaakt".
- **Our Place duwt accessoires als aparte campagne.** "Mutually Beneficial" (preview "Get more out of your kitchenware") gaat alleen over Kitchen Tools ("Supporting Cast") en nieuwe Mini Utensil Essentials. Cross-sell naar wie al pannen heeft of overweegt, geen korting.
- **HexClad gebruikt de winactie als deadline.** "2x entries ends today 🍕" (preview "Get a pizza Italy!") geeft dubbele punten voor Gordon's Golden Ticket to Italy, alleen naar het hello@-segment (b en c, niet w). Urgentie met een einddatum, zonder prijs te verlagen.
- **Geen nieuwe mail van Caraway, Made In, Okura, Plateful of Taima** in de laatste 26 uur. Caraway's ritme van 48 uur voorspelt welkom 6 rond 180 uur (19 okt rond 22:45 UTC).
- **Na 7 dagen nog steeds geen kortingscode** bij HexClad, Our Place en Caraway. Plateful blijft het enige merk met een code.

## Patroon na dag 8 (20 okt)

- **HexClad stuurt de tweede cartmail pas na 7 dagen.** hex-c kreeg op 19 okt om 11:22 UTC (168,7 uur na de actie) "The last cookware you'll ever need" (preview "Your favorite kitchen staple is here."): dezelfde Hybrid Fry Pan 10 inch ($116), "You Qualify For Free Shipping", "Built To Last" met lifetime guarantee, een review van een klant die 5 tot 6 avonden per week kookt en "Complete your order". Hetzelfde onderwerp als browse 2 van hex-w na 25,6 uur. De cartflow heeft dus een tweede stap na een week, als late herinnering, nog steeds zonder korting.
- **Our Place slaat w over bij de accessoire-campagne.** "Mutually Beneficial" ging naar op-b (05:15) en op-c (12:15, weer 7 uur later), maar op-w kreeg hem niet. De eerste campagne die alleen naar wie producten heeft bekeken of in de winkelwagen had gaat. Accessoires dus alleen naar mensen met aantoonbare interesse.
- **Caraway welkom 6 bleef uit.** Het ritme van 48 uur voorspelde een mail rond 180 uur (19 okt 22:45 UTC); er kwam niets. De welkomreeks van Caraway lijkt na 5 mails (132 uur) klaar.
- **Rustigste dag tot nu toe:** 2 nieuwe mails (HexClad 1, Our Place 1). Geen mail van Made In, Okura, Plateful of Taima.
- **Na 8 dagen nog steeds geen kortingscode** bij HexClad, Our Place en Caraway. Plateful blijft het enige merk met een code.

## Patroon na dag 9 (21 okt)

- **HexClad welkom 5 na precies 192 uur (8 dagen).** "To know us is to 🫶 us" (preview "Really, friend.") ging om 10:39 tot 10:41 UTC naar w, b en c, net als welkom 4 binnen een paar minuten. Het ritme is nu 0, 24, 48, 120, 192 uur: na de eerste drie dagen een stap van 72 uur. De mail is vrijwel alleen beeld; in de tekst staan alleen de categorieen (pannen, messen, HexMills, schorten, tools), refer a friend $100 en de winactie. Een brede "kijk rond in het assortiment"-mail in plaats van een product.
- **HexClad zet een tweede beroemde chef in.** "We've got big news 📰" (preview "Massimo Bottura joins the Culinary Council") ging om 23:30 UTC alleen naar het hello@-segment (hex-c en hex-b, niet w). Puur autoriteit als nieuws, zonder product of prijs. Na Gordon Ramsay bouwt HexClad een "council" van chefs.
- **Our Place gebruikt voorraad als schaarste.** "Be Quick" (preview "The Wok's in stock, but not for long!") kwam om 05:15 UTC naar op-b: de Carbon Steel Wok van Kenji López-Alt, "Sold Out & Back for Seconds", "It's back, for now", met twee klantreviews (50 jaar wok-ervaring, werkt op inductie). Geen prijs, geen korting. Op 20 okt stuurde Our Place geen enkele campagne; het dagelijkse ritme heeft dus ook rustdagen.
- **Geen nieuwe mail van Caraway, Made In, Okura, Plateful of Taima.** Caraway is nu ruim 3 dagen stil na welkom 5; de reeks lijkt klaar.
- **6 nieuwe mails** (HexClad 5, Our Place 1). **Na 9 dagen nog steeds geen kortingscode** bij HexClad, Our Place en Caraway. Plateful blijft het enige merk met een code.

## Patroon na dag 10 (22 okt)

- **Our Place stuurt nu twee campagnes per dag naar op-b.** Na "Be Quick" (05:15 UTC) kwam om 16:15 UTC "It Takes Two" (preview "Breaking down our latest essentials"), en om 05:15 UTC vandaag al "Set Savings". "It Takes Two" ging alleen naar op-b; c en w kregen hem (nog) niet. De dichtheid loopt op richting BFCM.
- **Keuzehulp tussen twee eigen pannen.** "It Takes Two" zet de Dual Handle Always Pan (13 inch, keramisch nonstick, glazen deksel) naast de Titanium Braiser Pro (11,5 inch, titanium binnenkant met rvs body, hoge hitte, past in de Wonder Oven Pro): "the right one to reach for depends on the dish". Geen prijs, geen korting, wel een reden om te kiezen in plaats van te twijfelen. Our Place verkoopt titanium nu als de pan voor hoge hitte en een goudbruine korst, precies het terrein van Siraat.
- **"Set Savings" zonder getal.** Het onderwerp belooft besparing op de Cookware Set (twee Always Pans, twee Perfect Pots, steamer, spatels en lepels), maar de tekst noemt geen bedrag of percentage; de besparing zit hooguit in het beeld of pas op de site. Eerste "savings"-onderwerp sinds de verlopen Prime Deals, mogelijk het begin van de BFCM-opbouw.
- **"Be Quick" ging ook naar c en w** (12:15 en 14:15 UTC, weer 7 en 9 uur na b). Schaarste-campagnes gaan dus naar de hele lijst, de accessoire-campagne van 19 okt niet.
- **Referral in de footer.** Our Place zet in elke campagne "Get $20" (refer a friend) als vaste footerlink naast Rewards en Text Exclusives; HexClad zet "refer a friend $100" in elke mail. Geen van beide maakt er een eigen mail van in deze 10 dagen: referral is bij hen een altijd-aanwezige regel, geen campagne.
- **Geen nieuwe mail van HexClad** (voor het eerst sinds de start een dag zonder HexClad; welkom 6 zou bij een stap van 72 uur rond 264 uur vallen, 23 okt rond 10:40 UTC) **en niets van Caraway, Made In, Okura, Plateful of Taima.**
- **4 nieuwe mails** (allemaal Our Place). **Na 10 dagen nog steeds geen kortingscode** bij HexClad, Our Place en Caraway. Plateful blijft het enige merk met een code.

## Korting: wanneer en hoe hoog

- **Plateful** is het enige merk met een kortingscode: 10% in de abandoned checkout na 12,5 uur, 2 dagen geldig en al verrekend in de checkout-link (kortingscode aanwezig, niet uitgeschreven).
- **HexClad** en **Our Place** geven geen code, maar duwen een lopende sitebrede sale (Prime Time Sale, October Prime Deals). HexClad noemt in cart- en browsemails alleen gratis verzending; Our Place zegt "Prime Deals" zonder percentage in de tekst, met een einddatum (12 okt 23:59 PT) in de kleine lettertjes.
- **Caraway** geeft geen welkomstkorting; in mail 2 belooft het $50 korting op een tweede aankoop van $300+ (code pas na de eerste aankoop).

## Opvallende onderwerpen en previews

- HexClad: "You're In!" (welkom als toegang tot een sale), "Your kitchen needs this!", "Great choice, chef!" met preview "Not to mention, Gordon Ramsay approved...", "Still thinking about it?" met "Get it while it's hot 🔥".
- Our Place: "You Left Before the Good Part" / "Prime Deals are waiting".
- Caraway: "Greetings From Caraway 🍳", "Our Top Caraway Picks" met preview "All ⭐️⭐️⭐️⭐️⭐️ across the board."
- Plateful: "Lola, about your Titanium Pro Pan™ order": platte tekst, ondertekend door een persoon (Dannah), met factuurnummer en telefoonnummer. Leest als service, niet als marketing.

## Ideeen voor Siraat

1. **Browse-abandonment binnen 1 uur met het bekeken product.** HexClad stuurt na 0,7 tot 1,5 uur een mail met precies de bekeken pan, prijs, "Complete your order" en drie aanvullende producten. Siraat kan in de browse-flow de eerste mail naar 1 uur trekken, met de bekeken pan bovenaan en een set of deksel als aanvulling.
2. **Een checkoutmail die eruitziet als een persoonlijk bericht van Benjamin.** Plateful verstuurt platte tekst met het complete winkelmandje, adres en verzendmethode, ondertekend door een persoon. Dit past bij de founder-notes van Benjamin, die al het best presteren (97 tot 142 per 1000). Te testen als variant van checkout-mail 2, met de vaste header en footer.
3. **Een korting die al in de link zit.** Plateful verrekent de 10% al in de checkout-link, zodat de klant geen code hoeft over te typen. Voor een kortingsstap in de Siraat-checkoutflow kan dat met een Shopify-link waarin de korting automatisch wordt toegepast, met een korte geldigheid (2 dagen) als eerlijke schaarste.
4. **De welkomstmail als "You're in".** HexClad en Our Place maken van de welkomstmail direct de toegang tot de lopende sale. Siraat kan tijdens een sale een korte eerste welkomstmail sturen die begint met de actie en pas daarna het verhaal van Benjamin vertelt.
5. **Beloning voor de tweede aankoop in de welkomstreeks.** Caraway geeft geen welkomstkorting, maar wel $50 op een tweede aankoop boven $300. Siraat kan zo'n bundel- of tweede-pan-beloning noemen naast de 75 jaar garantie en 30 dagen retour, zonder de eerste marge weg te geven.

6. **Browse 2 na 24 uur met garantie als hoofdboodschap.** HexClad zet "Lasts a Lifetime" in het onderwerp. Siraat heeft een sterker getal: 75 jaar garantie. Een tweede browse-mail met onderwerp rond "75 years" en het bekeken product is een logische test.
7. **Materiaalvergelijking in de welkomstreeks.** Caraway zet traditioneel non-stick naast hun pan. Siraat kan coating tegenover ongecoat titanium zetten (geen coating die slijt), passend bij de regel dat pre-purchase mails over USP's en materiaal gaan en niet over gebruik.
8. **Prijsbezwaar beantwoorden met gespreid betalen.** HexClad zet "Price holding you back?" in het onderwerp en legt Affirm stap voor stap uit. Prijs is ook bij Siraat het grootste bezwaar (27% twijfelde). Als Siraat in de US een termijnoptie heeft, is dit een sterke derde browse- of cartmail zonder marge weg te geven. [VRAAG FLORIS: welke betaaloptie in termijnen hebben we?]

9. **Een welkomstmail met een autoriteit en een citaat, zonder product.** HexClad gebruikt na 5 dagen Gordon Ramsay en een citaat over "buy once, use for life". Siraat heeft geen beroemde chef, maar wel Benjamin en echte reviews. Een late welkomstmail met een citaat van een echte klant over jaren gebruik, plus de 75 jaar garantie, vertelt hetzelfde verhaal zonder te leunen op iemand die we niet hebben.
10. **Een kleine instap naast de set.** Caraway zet onder de set-aanbieding "Not Ready for a Full Set?" met de losse bestseller-pan. Siraat kan in welkomst- en browsemails onder de set altijd een tweede, lagere stap tonen (een losse pan), zodat wie de set te duur vindt niet afhaakt.
11. **Een pauze in de welkomstreeks na drie dagen.** HexClad stuurt op dag 0, 1 en 2 en pas weer op dag 5. Siraat kan testen of een pauze van twee tot drie dagen na de eerste drie mails de uitschrijvingen in de welkomstflow verlaagt (beide armen zitten nu boven 1%).
12. **Een productverbetering als eigen campagne.** Our Place verkoopt een kleine aanpassing (fijnere textuur, makkelijker schoonmaken) als nieuws met "Look Closer", zonder korting. Als Siraat iets aan pan, handgreep, verpakking of meegeleverde info verbetert, is dat een campagne met een close-up van het detail en Benjamin die uitlegt waarom. Belangrijk omdat Our Place nu ook op titanium inzet: Siraat moet het verschil benadrukken (puur titanium zonder coating tegenover hun nonstick-laag op titanium).
13. **Een accessoire-campagne voor bestaande kopers.** Our Place stuurt "Mutually Beneficial" met alleen tools en kleine accessoires. Siraat kan in de post-purchase flow of als campagne naar kopers een deksel, spatel of tweede maat aanbieden, met de 75 jaar garantie als reden om het setje compleet te maken.
14. **Urgentie zonder korting via een einddatum op iets anders dan prijs.** HexClad zet "ends today" op dubbele punten in een winactie. Siraat kan eerlijke deadlines gebruiken die geen marge kosten, zoals de laatste besteldag voor levering voor de feestdagen.
15. **Een late cartmail na 7 dagen.** HexClad stuurt de tweede cartmail pas na een week, met hetzelfde product, gratis verzending, de garantie en een klantreview over intensief gebruik. Siraat kan achteraan de cartflow een extra stap na 7 dagen testen voor wie nog niet kocht, met de bekeken pan, de 75 jaar garantie en een review van iemand die de pan al lang dagelijks gebruikt. Weinig risico op uitschrijvingen omdat er een week tussen zit.
16. **Accessoire-campagnes alleen naar betrokken profielen.** Our Place stuurde "Mutually Beneficial" wel naar b en c, maar niet naar w. Siraat kan cross-sell campagnes (deksel, spatel, tweede maat) beperken tot kopers en mensen die een product bekeken of in de winkelwagen hadden, zodat koude inschrijvers alleen de kernpan zien en de lijst minder vermoeid raakt.
17. **Een eerlijke voorraadmail bij herbevoorrading.** Our Place verkoopt "Sold Out & Back for Seconds" met "Be Quick" en echte reviews, zonder korting. Als een Siraat-pan of -maat uitverkocht was en terugkomt, is dat een campagne (en een back-in-stock flow) met onderwerp rond "It's back", alleen als de voorraad echt beperkt is, plus een review van iemand die de pan dagelijks gebruikt.
18. **Een late welkomstmail die het hele assortiment laat zien.** HexClad stuurt na 8 dagen een mail met alleen de categorieen en "To know us is to 🫶 us". Siraat kan achteraan de welkomstreeks (na de mails over materiaal, garantie en Benjamin) een korte overzichtsmail testen met pan, set, deksel en accessoires, voor wie na een week nog niet kocht en misschien een ander product zoekt.
19. **Een keuzehulp tussen twee Siraat-producten.** Our Place zet in "It Takes Two" twee pannen naast elkaar met per pan waarvoor hij het best is. Siraat kan in browse 2 of een campagne de losse pan naast de Pan Pro Duo (of twee maten) zetten met "welke past bij hoe jij kookt", zodat twijfel tussen producten geen reden wordt om niets te kopen.
20. **Referral als vaste regel in elke mail, plus eigen mails.** HexClad ($100) en Our Place ($20) zetten refer a friend in elke footer, maar sturen er geen eigen mail over. Siraat kan het Social Snowball-programma (vriend 15%, affiliate 15%) op dezelfde manier als vaste regel in footer of blok van alle bestaande mails zetten, naast de losse affiliate-mails van Benjamin. Zo ziet elke ontvanger het programma, ook wie de aankondiging mist. Kanttekening: wij geven een percentage en zij een vast bedrag; het advies om na BFCM 15/15 te testen tegen een vast bedrag blijft staan.
21. **Een "savings"-onderwerp altijd met het getal.** Our Place belooft "Set Savings" maar noemt geen bedrag in de mail. Als Siraat een setvoordeel communiceert, hoort het echte bedrag of percentage in onderwerp of preview en bovenaan de mail, anders voelt de belofte leeg.

## Open punten

- Caraway-adressen cw-w/b/c kregen niets, terwijl het hex-w-adres twee Caraway-mails kreeg: de footer-inschrijving van de agent werkte waarschijnlijk niet. Opnieuw proberen of handmatig doen.
- Made In stuurde na ruim 20 uur nog niets ondanks de bevestiging "subscribed"; mogelijk double opt-in of een vertraagde reeks.
- Okura (ok-co) en Our Place (op-c, op-co) stuurden ook op dag 2 geen cart- of checkoutmail. Our Place lijkt alleen browse te triggeren (op-b), niet cart of checkout.
- Made In, Caraway-adressen en Plateful (na de ene checkoutmail) bleven op dag 2 stil.
- Taima en HexClad co zijn nog niet gedaan.
