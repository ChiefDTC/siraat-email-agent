# BF signup flow (voorbeeld, niet live)

Opgesteld 31 okt 2026. Niets in Klaviyo, Shopify of Alia gewijzigd. Aanbod volgens Floris (31 okt): Black Friday Sale, "Up to 70% off", voor iedereen, via https://siraatskitchen.com/collections/black-friday-sale. Geen extra code in deze flow of pop-up (extra code alleen in abandonment-mails).

Waarom: W1 komt nu 6,5 minuten na aanmelding en verdient $2,83 per ontvanger; 60% van de kopers koopt binnen 10 minuten; tussen minuut 6 en de volgende ochtend komt niets (research/smooche/02-siraat-nu.md). Deze flow is sneller (1 minuut), heeft één knop naar de salecollectie en vult het gat op dag 0 met W1b.

## Bestanden
| Bestand | Rol |
|---|---|
| `popup-1-signup.html` | pop-up scherm 1 (aanmelding), 375 px mockup |
| `popup-2-reveal.html` | pop-up scherm 2 (kraskaart-reveal "Unlocked", geen code) |
| `bf-w1.html` | W1, ontworpen (A) |
| `bf-w1-letter.html` | W1, bijna platte brief (B) |
| `bf-w1b.html` | W1b, +3 uur, niet-kopers |
| `bf-w2.html` | dag 1, 09:00 |
| `bf-w3.html` | dag 3, 09:00 |
| `bf-last.html` | echte laatste dag van de sale, placeholders [END DATE] en [END TIME + TIMEZONE] |
| `*.klaviyo.html`, `*-preview.html` | uitvoer van build_template.py |
| `previews/*-375.png` | renders op 375 px |

## Productkaarten per markt (herbouw 31 okt 2026, feedback Floris)
Feedback: "meer producten, net als Smooche met een mooie Black Friday-stijl. Hammered Pan Pro Standard is belangrijkste, in de USA ook de 12 pcs en de 6 pcs set; buiten de USA de 6 pcs set pushen."

Opbouw (Smooche-welcome als voorbeeld): donker vlak (Night #0E0E0E) onder de vaste header, grote gecentreerde kop met gele markering, één regel aanbod, SHOP THE SALE, gele sectiebalk, productkaarten (blok `bf-product`, beeld en donker paneel om en om links/rechts, op mobiel beeld boven tekst), korte noot van Benjamin, bewijsrij (100,000+ / 75 years / 30 days), knop, vaste footer.

Blok `{{BLOCK:bf-product side="left|right" img url name kicker alt b1 b2}}` (opties: pill, btn, pad, bg, panel). Gele pil "UP TO 70% OFF", geen vaste $-prijzen (verschillen per markt). Werkt zonder `<style>` (hybride inline-blocks van 280 px, Outlook spooktabel); met `<style>` op mobiel 100% breed.

Markt: `{{USONLY}}...{{ELSEUS}}...{{/USONLY}}` op `person.Country` (MARKET-SIGNAL profile). Onbekend land krijgt de niet-US-kaarten. De 12-delige set staat alleen in de US-tak (us_only).

| Mail | US | Niet-US en onbekend |
|---|---|---|
| bf-w1 (welkom) | Pan Pro Standard, 12-delig, 6-delig, Deep Pan Pro | Pan Pro Standard, 6-delig, Deep Pan Pro, Wok Pan Pro |
| bf-w1b (korte versie, 3 keuzes) | Pan Pro Standard, 12-delig, 6-delig | Pan Pro Standard, 6-delig, Wok Pan Pro |
| bf-w2 (sets eerst) | 12-delig, 6-delig, Pan Pro Standard | 6-delig, Pan Pro Standard, Deep Pan Pro |
| bf-w3 (Pan Pro Standard uitgediept) | grote Pan Pro-sectie met eigen knop, dan 12-delig, 6-delig | idem, dan 6-delig, Deep Pan Pro |
| bf-last | Pan Pro Standard, 12-delig, 6-delig | Pan Pro Standard, 6-delig, Deep Pan Pro |
| bf-w1-letter | geen kaarten (platte A/B-arm), alleen een link naar de Pan Pro Standard in de tekst | idem |

Bullets alleen uit claims.csv/facts.csv: pure titanium cooking surface + zero coating, alle kookplaten incl. inductie, oven en vaatwasser (zonder temperatuur), non-toxic PFAS-/PTFE-free lab tested, 75 jaar garantie, setinhoud volgens PDP (6-delig: 3 pannen + 3 deksels; 12-delig: 3 pannen, 3 potten, 6 deksels). "OUR #1 SELLER" bij de Pan Pro volgt de PDP-tagline.

Renders: `previews/<mail>-us-375.png` en `<mail>-int-375.png` (Klaviyo-versie, Django-render met person.Country "United States" en "Germany"; script `_tools/render_bf.py`). De oude `<mail>-375.png` zijn de vorige versie. Let op: de `*-preview.html` uit build_template toont beide markttakken onder elkaar (de preview kent geen markt); kijk naar de -us/-int-renders.

Open punten productkaarten:
- Oventemperatuur: het brand book en de opdracht noemen 750°F / 400°C, maar claims.csv zegt dat die voor de pannen niet bevestigd is (alleen Roasting Pan PDP). Nu "Oven safe" zonder getal. [VRAAG FLORIS]
- Beeld 6-delige set is een PNG (Shopify levert geen JPG door transparantie), ~220 KB op 600 px. Liever een JPG of yellow-studio-versie uploaden.
- Kaarten linken naar de productpagina's: aanname dat de saleprijs daar ook staat.
- Knoptekst "SHOP NOW" op verzoek (Smooche-stijl); de copy-skill zegt anders "nooit Shop now". Uitzondering zoals bij de receptcampagnes (DECISIONS 9 okt). [bevestigen]

## Segment (doelgroep)
Naam: `BFCM 2026 · popup signups (not purchased)`.
- Ingeschreven via de BF-pop-up: `Subscribed to Email Marketing` met bron/methode Alia (`custom_method_detail` "Alia sign-up") **of** profieleigenschap `signup_source = bf_popup_2026` (door de pop-up te zetten; voorkeur, want ondubbelzinnig),
- en die inschrijving is **na de BFCM-start** ([START DATE], bijv. "sinds 2026-11-xx 00:00"),
- en `Placed Order` nul keer sinds de inschrijving,
- en e-mail kan marketing ontvangen.

Trigger van de flow: bij voorkeur **metric-trigger** "Subscribed to Email Marketing" (of de Alia-formulierinzending) met triggerfilter op de BF-pop-up, niet de segment-trigger: een segment-trigger kan minuten tot langer vertragen, en de 1 minuut is het punt. Het segment dient daarnaast voor uitsluiten van campagnes en voor `bf-last`.

Flowfilters (op de hele flow): `Placed Order` = 0 sinds flowstart; nooit eerder in deze flow; e-mail bevat geen `test@`.

## Relatie met de bestaande welcome (T4a5Mk)
De BF-pop-up-inschrijvers moeten de gewone welcome **tijdens** de sale niet ook krijgen. Optie: in T4a5Mk een flowfilter "niet in segment BFCM popup signups" tot het einde van de sale. Na de sale vallen ze terug in de gewone welcome (of niet, beslissing Floris).

## Stappen
| Stap | Wacht | Mail | Filter op de stap | Smart Sending |
|---|---|---|---|---|
| 1 | 1 minuut (geen "tot"-tijd, ook 's nachts) | W1: A/B `bf-w1` tegen `bf-w1-letter`, 50/50 | Placed Order = 0 sinds flowstart | **uit** |
| 2 | 3 uur | `bf-w1b` | Placed Order = 0 sinds flowstart; optioneel overslaan bij Started Checkout in de laatste 3 uur | aan |
| 3 | 1 dag, tot 09:00 (profieltijdzone) | `bf-w2` | Placed Order = 0 sinds flowstart | aan |
| 4 | 2 dagen, tot 09:00 | `bf-w3` | Placed Order = 0 sinds flowstart | aan |
| 5 | op [END DATE], 10:00 | `bf-last` | Placed Order = 0 sinds flowstart | aan |

- **Exit bij aankoop:** elke stap heeft het filter Placed Order = 0 sinds flowstart (Klaviyo-flowfilter "Placed Order zero times since starting this flow"), zodat kopers direct uit de reeks vallen.
- **bf-last** hangt niet aan een vaste wachttijd (wie op de laatste dag inschrijft, zou hem anders nooit krijgen; wie vroeg inschrijft, krijgt hem te vroeg). Twee opties: (a) een campagne op [END DATE] naar het segment, alleen wie minstens 1 dag in de flow zit; (b) in de flow een conditionele split "vandaag is [END DATE]" met een vertraging tot die datum. Optie (a) is eenvoudiger en betrouwbaar.
- Wie pas laat in de sale inschrijft, haalt W2/W3 misschien niet voor het einde: stop de flow (zet hem op manual) op [END DATE] na `bf-last`, zodat niemand na de sale nog "Priced for Black Friday" krijgt.
- **Uitsluiten van reguliere campagnes:** alle BF-campagnes en reguliere campagnes tijdens de reeks sluiten het segment uit zolang iemand in de eerste 3 dagen van de reeks zit (segment "in deze flow, Received Email W1 in de laatste 3 dagen"). Na dag 3 mogen ze campagnes weer krijgen. Uitzondering: de laatste-dagcampagne zelf als die `bf-last` vervangt.
- **Abandonment-flows** (checkout, cart, browse) blijven gewoon lopen; die hebben de extra code. Zet in W1b de skip bij Started Checkout, zodat iemand niet tegelijk W1b en de checkout-mail krijgt.
- Afzender: "Benjamin at Siraat's Kitchen", reply-to naar een inbox die gelezen wordt (W1 en de brief vragen om te antwoorden).

## A/B-tests
1. **W1 vorm**: `bf-w1` (ontworpen, hero, tegels) tegen `bf-w1-letter` (brief, één knop). Zelfde onderwerp, zelfde verzendtijd. Meten: omzet per ontvanger en orders binnen 72 uur (niet open rate). Minimaal ~2.000 ontvangers per arm voor er iets te zeggen valt; handmatige winnaar.
2. **Wachttijd W1**: 1 minuut tegen 0 minuten (als Klaviyo 0 toelaat; anders 1 tegen 3). Meten: orders binnen 1 uur na inschrijving, ook die zonder klik (Placed Order sinds inschrijving).
3. **Onderwerp W1** (na test 1, nooit tegelijk): "You're in. The sale is live." tegen "Benjamin here. You're in." Eén variabele.
4. **Pop-up** (Alia, 50/50, vóór de sale start): huidige Card Game tegen `popup-1`/`popup-2`. Meten: omzet per bezoeker binnen 7 dagen, niet alleen inschrijvingsratio.
5. Later, alleen als 1 en 2 duidelijk zijn: W1b wel/niet (holdout 20%), om te zien of het tweede contact op dag 0 extra orders oplevert of alleen afmeldingen.

## Open vragen voor Floris
- **"Up to 70% off"**: staat er echt minstens één product 70% onder de eerdere prijs (en in de EU onder de laagste prijs van 30 dagen)? Anders het percentage aanpassen.
- **"Same member price for everyone who signs up"** (pop-up 2, gevraagde tekst): er is geen aparte ledenprijs, de saleprijzen gelden voor iedereen. Kan verwarren of als misleidend gelezen worden. Voorstel: "Same Black Friday prices for everyone." [VRAAG FLORIS]
- **"Sign up to shop it first"** (pop-up 1): de sale is al live, dus "first" belooft iets wat we niet doen, tenzij er vroege toegang tot nieuwe drops of extra producten is. Voorstel: "Sign up and get our best picks." [VRAAG FLORIS]
- Collectie `/collections/black-friday-sale`: bestaat hij al en staan de saleprijzen ook op de gewone product- en collectiepagina's (tegels linken daarheen)?
- BFCM-start- en einddatum en -tijd (segment en `bf-last`).
- Hoe markeert de pop-up de inschrijving (eigenschap `signup_source`, aparte lijst, of Alia-methode)?
- Welke set is de echte bestseller (tegel in W1)?
- Mogen BF-pop-up-inschrijvers na de sale de gewone welcome krijgen?
- De giveaway "order refunded" van de huidige Card Game: verdwijnt die in de BF-pop-up? (Deze mockups noemen hem niet.)
