# Shopify-orderbevestiging · herontwerp B2, B3, B4 (11 nov 2026, middag)

Floris vond B te zwak. Doel nu: een klant die net bestelde denkt "wow, dit annuleer ik zeker niet" en weet precies wat er gebeurt. Drie UX-richtingen van dezelfde opbouw (Floris): 1 hero met live kop op het beeld, 2 "Welcome to Siraat." met samenvatting, 3 "Here's what to expect", 4 vier pijlers (non-toxic, performance, titanium, lab), 5 eerste week met titanium (Benjamin), 6 de praktische blokken uit B en C. Niets naar Shopify of Klaviyo-templates; alleen het herobeeld staat in de Klaviyo-bibliotheek.

| Bestand | Wat |
| --- | --- |
| `variant-b2.liquid` / `-b3` / `-b4` | Plakklare Shopify-code (bron: `_tools/build_b.py`, hergebruikt alle Liquid-logica van `build.py`) |
| `variant-b2-preview.html` enz. | Render op de voorbeeldorder (Pan Pro Standard $149, deksel $59, sheets "Free first pack, then $20 every 28 days", 5 gifts) |
| `previews/variant-b2.png` / `-mobile.png` enz. | 600 en 390 px, DSF 2. `_check-b*-au_nosub*` = AUD-order zonder abonnement. `_bg-b*` = beeld onder de herotekst (contrastmeting) |
| `_tools/contrast.py` | Meet contrast witte herotekst tegen het beeld eronder |
| `assets/oc-hero-flash-egg.jpg` | Nieuw herobeeld (Higgsfield gpt_image_2_6, flash-stijl, echte Pan Pro als referentie), Klaviyo-CDN in `assets/klaviyo-urls.txt` |

Bouwen: `python3 -I _tools/build_b.py`, dan `VARIANTS=b2,b3,b4 LIQUIDJS=<pad>/node_modules/liquidjs node _tools/render.js`, dan `python3 -I _tools/contrast.py`.

## Wat in alle drie hetzelfde is

- **Hero**: live tekst "Your order is confirmed." in Inter 700 op het beeld, eyebrow "THANK YOU, SARAH", regel "Order #... is in. Here is exactly what happens next." Achtergrondbeeld via `background`-attribuut + CSS, VML `v:rect` voor Outlook, donkere `bgcolor` #1C1510 als beelden uit staan (wit op #1C1510 = ruim 15:1), plus een CSS-gradient naar donker onderaan. Contrast gemeten op het beeld zelf: mediaan 18:1, slechtste 5 procent van de pixels 9:1 (mobiel) en 11:1 (600 px). Het beeld heeft onderaan een donker aanrecht, dus ook zonder gradient (Outlook) blijft het leesbaar.
- **Welkom**: "Welcome to Siraat." + kaart met beeld en naam van het hoofdproduct, variant, aantal, "Plus Stainless Steel Lid, a subscription and 5 free gifts.", ordernummer, totaal in de valuta van de klant. Knop "Track my order".
- **Verwachtingen**: bevestigd, ingepakt `sk_pack`, verzonden met tracking per mail, bezorgd in `sk_days` dagen (US 7 tot 12, INT 6 tot 14). Kader "May arrive in more than one parcel" alleen bij meer dan één verzendbaar item.
- **Pijlers** (alleen goedgekeurde claims, geen verzonnen keurmerken): Non-toxic (no coatings, no PFAS, PFOA, or BPA), Performance (sear, oven safe, metal utensil safe, dishwasher safe), Titanium (75-year warranty against defects, the original hammered pan), Lab (Light Labs, ISO/IEC 17025, 31 PFAS, report no. 25895, link naar /pages/third-party-testing). De "badges" zijn eigen feiten in pillen, geen certificaten.
- **Eerste week**: heat, oil, food (2 tot 3 min middelhoog, waterdruppel, theelepel olie, laten loslaten, begin met eieren), ondertekend Benjamin, Founder, Siraat.
- **Praktisch**: abonnementskader (plan letterlijk, vandaag gratis, eerste afschrijving, opzeggen, knop naar Recharge `/tools/recurring/login`), 5 gifts (wat verzonden wordt, wat digitaal is, de draw), bon met totalen en valutaregel, adres, hulp en annuleervenster (1 uur), 30-day returns, 75-year warranty, 100,000+, sterren.
- Liquid: `subtotal_line_items`, `selling_plan_allocation`, `presentment_currency`, giftsdetectie en settings bovenaan zijn ongewijzigd uit `build.py`; nieuw zijn `sk_pack` en de samenvatting (`sk_first_img`, `sk_first_var`, `sk_first_qty`, `sk_rest`).

## B2, B3, B4 vergeleken

| | B2 · Editorial | B3 · Steps | B4 · Cards |
| --- | --- | --- | --- |
| Pijlers | Groot beeld per pijler, beeld en tekst om en om (op mobiel beeld boven), lab als groot donker "No. 25895"-blok | Verticale keten met iconen, lijn en pillen, daarna donkere "What you get is exactly what we tested"-kaart met 4 badges | 2x2 kaartraster met kleine beelden, ook op mobiel 2x2 |
| Tijdlijn | Genummerde verticale keten | Genummerde verticale keten | Compacte rij van 4 iconen (mobiel 2x2) |
| Koppen | Instrument Serif italic (kalm, magazine) | Inter (Create-achtig) | Inter |
| Beelden | Hero + 3 shootfoto's + eifoto | Hero + productfoto, verder iconen | Hero + 3 kleine shootfoto's |
| Hoogte 600 / 390 px | ~6.440 / 8.340 | ~6.170 / 7.600 | ~5.580 / 6.930 |
| Sterk | Meeste "wow" en merkgevoel | Leest als een plan, werkt ook zonder beelden, dichtst bij de Create-referentie | Kortst en snelst te scannen |
| Zwak | Langst op mobiel; 2-koloms beelden vragen een goede client | Weinig productbeeld na de hero | Minder verhaal per pijler |

**Advies: B3 Steps.** De klant heeft net betaald en twijfelt aan twee dingen: gaat het goed komen, en was dit een goede keus. B3 beantwoordt allebei in dezelfde vorm (een keten van stappen), houdt het bewijs (rapport no. 25895) groot en concreet, en hangt niet af van beelden, dus het ziet er in Gmail met geblokkeerde beelden en in Outlook net zo uit. B4 is de tweede keus als de lengte telt. B2 is het mooiste, maar op mobiel 8.300 px.

## Wat het waard is (Shopify, 13 aug tot 11 nov 2026, 91 dagen)

- Orders: 21.715, total sales $4,96 mln.
- Geannuleerd: 333 orders, waarvan 196 met een bedrag (137 zijn $0-orders, vooral bots/tests), samen **$63.129**. 209 van de 332 binnen 24 uur, 264 binnen 72 uur (Triple Whale, telt 332).
- Terugbetaald binnen 3 dagen na de order zonder annulering: 115 orders, **$28.047** (Triple Whale, transacties).
- Per jaar (x 365/91): annuleringen ~$253.000, met de vroege refunds ~$366.000. **40 procent minder = ~$101.000 per jaar** (alleen annuleringen) of **~$146.000** (inclusief refunds binnen 3 dagen). Dat is omzet die blijft, geen winst. Floris' schatting van 1 miljoen is met deze cijfers niet te halen; daarvoor zou het verlies $2,5 mln per jaar moeten zijn. BFCM-volume kan het bedrag in november en december wel tijdelijk hoger maken.

## Floris beslist (B2 tot B4)

1. **Inpakbelofte** `sk_pack`: nu "within 1 business day" (verzendbeleid en helpcenter). "Within a few hours" alleen als het magazijn dat echt haalt (8 okt: mediaan 77 uur tot fulfillment). Een gebroken belofte in deze mail geeft juist tickets.
2. **Herobeeld**: AI-beeld (flash-stijl, geen tekst, kale gehamerde pan, handen gecontroleerd). Goedkeuren of een shootfoto kiezen.
3. **Koppen**: serif (B2) of Inter (B3, B4) voor de sectiekoppen; de hero is in alle drie Inter.
4. **Richting**: B2, B3 of B4. Daarna één keer "Send test notification" in Shopify en kijken in Gmail (web en iOS) en Outlook.
5. **Figma-rij** (DECISIONS 4 nov): nog niet gemaakt.

---

# Shopify-orderbevestiging · 3 varianten (11 nov 2026)

Nieuwe versie van Shopify Admin > Settings > Notifications > **Order confirmation**. Doel: de klant weet direct wat hij bestelde, wat het kost, wanneer het komt, wat los komt en hoe hij iets wijzigt. Minder annuleringen en minder "where is my order"-tickets. Niets is naar Shopify of Klaviyo gezet; alleen bestanden.

Taakverdeling met Klaviyo: deze mail = feiten en verwachtingen. P1-FIRST ("Good call. Here's what's coming.", +1 uur) = Benjamin, de eerste-ei-tip en de e-book-knop. Daarom geen founder-verhaal en geen verkoop in deze mail.

## Bestanden

| Bestand | Wat |
| --- | --- |
| `variant-a.liquid`, `variant-b.liquid`, `variant-c.liquid` | Plakklare Shopify-code (bron, gebouwd door `_tools/build.py`) |
| `variant-X-preview.html` | Dezelfde Liquid gerenderd op de voorbeeldorder (Pan Pro Standard $149, deksel $59, sheets-abonnement, 5 gifts) |
| `previews/variant-X.png` / `-mobile.png` | Render 600 px en 390 px breed, deviceScaleFactor 2 |
| `previews/_check-X-au_nosub*` | Controle: Australische order in AUD, zonder abonnement, 3 gifts |
| `_tools/build.py`, `_tools/render.js`, `_tools/samples.json` | Bouwen en renderen (liquidjs 10.16.1 + Playwright) |
| `IMAGE-BRIEF.md` | Beeldplekken en Higgsfield-prompts |

Opnieuw bouwen: `python3 -I _tools/build.py` en daarna `LIQUIDJS=<pad>/node_modules/liquidjs node _tools/render.js`. Wijzig nooit alleen in Shopify: bron aanpassen, bouwen, opnieuw plakken.

## In Shopify plakken

1. Shopify Admin > Settings > Notifications > Customer notifications > **Order confirmation**.
2. Klik **Edit code**. Kopieer eerst de huidige code naar een tekstbestand (terugval).
3. Vervang alles in het veld **Email body (HTML)** door de inhoud van `variant-X.liquid`.
4. Onderwerp (voorstel): `Order {{ order_name }} confirmed: here's what happens next`. Laat de afzender zoals hij is.
5. Bovenaan het bestand staan de instellingen als `assign`. Controleer ze voor je opslaat (zie "Floris beslist").
6. **Preview**, dan **Save**.

## Wat testen

1. **Send test notification** (knop in de editor) naar je eigen adres; bekijk op telefoon en desktop, Gmail en Apple Mail.
2. Echte testorder **met** abonnement (sheets met verkoopplan): abonnementskader zichtbaar, planregel letterlijk, datum eerste afschrijving klopt (orderdatum + 28 dagen), portalknop opent zonder inloggen.
3. Testorder **zonder** abonnement: geen abonnementskader, in C staat "None. Nothing in this order renews."
4. **Internationale order** (bijv. AU of UK in lokale valuta): valutaregel verschijnt, levertijd toont de INT-range, totaal met valutacode.
5. Order met **één** verzendbaar product (alleen een pan, geen gifts): het "meer dan één pakket"-kader verdwijnt.
6. Order **met kortingscode**: regel Discount verschijnt.
7. Controleer of de giftregels in de echte order dezelfde titels hebben als in de voorbeeldorder. De mail herkent gifts op prijs $0 en woorden in de titel (`mystery`, `shipping`, `cookbook`, `book`/`guide`, `filter`/`draw`). Andere titels vallen terug op "Included with your order."

## A, B en C vergeleken

| | A · Calm receipt | B · Experience | C · No surprises |
| --- | --- | --- | --- |
| Boven de vouw | Bedankt + knop, dan de orderregels | Groot sfeerbeeld + "Your order is confirmed." | Checklist met 6 antwoorden |
| Sterk in | Rustig, vertrouwd bonnetje; alles op een logische volgorde | Merkgevoel, PFAS-bewijs, sterren en 100,000+ (dichtst bij de Create-referentie) | Beantwoordt alle 6 ticketproblemen in de eerste schermhoogte |
| Zwak in | Abonnement en splitsing pas halverwege | Langst (~5.100 px op 600); eerste-week-tip overlapt met P1 (eerste ei); praktische blokken pas onderaan | Minder sfeer, wat herhaling tussen checklist en details |
| Hoogte 600 / 390 px | ~3.800 / 4.750 | ~5.100 / 6.150 | ~4.300 / 5.500 |

**Advies: C.** De tickets gaan over verrassingen (alleen het deksel ontvangen, abonnement niet gezien, valuta, levertijd). C zet al die antwoorden op het eerste scherm, met het abonnement in eigen woorden en een opzeglink, nog voordat de klant scrolt. Dat is ook de eerlijkste verdediging tegen chargebacks op de sheets. A is de veilige tweede keus. B liever niet als orderbevestiging: de first-cook-uitleg hoort bij P1/P2 en maakt de mail lang; het trustblok uit B kan wel onderaan C als dat gewenst is.

Meten na livegang (4 weken voor en na): Gorgias-tickets met tags/onderwerpen "where is my order", "only received", "subscription/cancel sheets", "currency/AUD"; annuleringen binnen 24 uur; opzeggingen van het sheets-abonnement voor de eerste afschrijving.

## Floris beslist

1. **Abonnementsportal**: nu `https://siraatskitchen.com/a/loop_subscriptions/customer` (LOG 30 okt: abonnementen lopen via Loop). Als het Recharge is: de Recharge-klantportallink. Liefst een link die zonder inloggen werkt (LOG 2 nov: 2 klikkers mailden direct daarna om op te zeggen).
2. **Levertijden**: US "7 to 12 days after it ships" (Klaviyo mediaan 7,1 d, p90 12,5 d; Ecomflow US 9,1 d), buiten de US "6 to 14" (verzendbeleid 6 tot 10, Ierland/Denemarken 8 tot 14). Bevestigen of aanpassen in `sk_days_us` / `sk_days_int`. Let op: de skillregel "geen levertijden in marketingmails" geldt niet voor deze transactionele mail, maar het moet wel kloppen.
3. **Annuleervenster**: 1 uur (verzendbeleid). Klopt dat in de praktijk?
4. **Kookboeklink**: `sk_cookbook_url` is leeg, dan staat er "Your download link arrives in a separate email". Klopt dat die mail er is (Shopify Digital Downloads of P1)?
5. **Weekly draw-tekst**: "Winners hear from us by email." Bevestigen; er zijn nog geen officiële actievoorwaarden.
6. **Sheets zonder actieve keuze** (LOG 10 nov: vooraf aangevinkt in checkout): deze mail maakt het abonnement zichtbaar, maar lost de toestemming niet op.
7. **Figma-rij** (DECISIONS 4 nov): nog niet gemaakt in deze sessie.
