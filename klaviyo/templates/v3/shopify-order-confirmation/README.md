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
