# Browse Triple Pixel v3 · nieuw ontwerp voor flow QNZyEb (concept)

Versie 19 oktober 2026. Vervangt de 1:1-kopie van de negen v4-browsemails (WdRz5k) in de draft-flow **QNZyEb "v4 · Browse abandonment · Triple Pixel"**. **Niets is in Klaviyo aangepast: geen templates, geen flowwijziging.** Dit is ontwerp plus bron-HTML; livegang alleen na akkoord en klikwerk van Floris.

- Bron en previews: `klaviyo/templates/v3/browse-tp/` (`tp-*.html` bron, `tp-*.klaviyo.html` met CDN-links, `tp-*-preview.html` gerenderd op een TP-achtig event, `previews/tp-*-mobile-375.png` en `-desktop.png`).
- Bouwen: `python3 -I scripts/build_template.py klaviyo/templates/v3/browse-tp/tp-b1.html klaviyo/templates/v3/browse-tp/assets klaviyo/templates/v3/browse-tp/assets/klaviyo-urls.txt` (zelfde voor de andere vier). Preview met logica: `expand.py` + `render.py` zoals PLAYBOOK 12, op een event met `Price "$144.00"` en profiel US.
- Figma: rij 2b in oaxnBkz3MAbePRnorCrQwz, https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=58-2
- Achtergrond trigger en filters: `research/v6-golive/12-fixes.md`, sectie "Browse Triple Pixel concept (19 okt)".

## 1. Voor wie

Triple Pixel-viewers zijn bezoekers die Klaviyo zelf niet herkende (ander apparaat, geblokkeerde cookies, terugkerend advertentieverkeer). Ze bekeken een productpagina, dus ze zijn product-aware, maar kouder dan de WdRz5k-ontvangers: ze hebben misschien nooit een mail van ons gelezen en weten niet meer precies wat ze bekeken. Ontwerpregels die daaruit volgen:

1. **Het product eerst en groot.** In B1, B1-ACC en de CODE-mail is het bekeken product (event.ImageURL) het grote beeld van de mail, met naam, korte regel en prijs. Geen gebakken hero met kop in beeld: de kop is live tekst ("Here it is again.", "In case it got lost between tabs."). Dat is ook de opbouw van W1 v3 en Mystery v3.
2. **Bewijs dat je kunt controleren.** De drie vragen uit de chef-video (DECISIONS 1 okt: labrapport, rapportnummer, 75 jaar garantie) als genummerd blok in B1, het certificaat erbij als beeld met link naar het rapport. In de CODE-mail drie regels "In case you're new to us".
3. **Een reden om terug te komen per mail:** B1 het product terug plus HI10, B2-NOTCLICKED de 75-jaar garantie (concurrentie-idee 6: HexClad browse 2 zet de garantie in plaats van een korting in het onderwerp; wij hebben het sterkere getal), B2-CLICKED nocode het risico weg (twee beloftes), CODE een eigen 10% met echte einddatum.

## 2. Flowlogica (ongewijzigd)

Geen reden gevonden om de logica te veranderen: zelfde trigger, filters, wachttijden en splits als QNZyEb nu heeft. Alleen de templates zijn nieuw. Vijf ontwerpen dekken alle negen berichten (de nocode-varianten cooldown en T02-B en de pan/acc-varianten deelden in WdRz5k al één template).

| Stap | Bericht(en) in QNZyEb | Ontwerp | Timing |
| --- | --- | --- | --- |
| 1 | TP · B1 (121177227), kookgerei | `tp-b1.html` | 1 uur na V48nhq |
| 1 | TP · B1-ACC (121177228), accessoire | `tp-b1-acc.html` | 1 uur |
| 2 | TP · B2-NOTCLICKED (121177242) | `tp-b2-notclicked.html` | + 2 dagen tot 09:00, niet geklikt |
| 2 | TP · B2-CLICKED · pan/acc nocode · cooldown (121177244, 121177247) en · T02-B (121177251, 121177258) | `tp-b2-clicked-nocode.html` | + 2 dagen tot 09:00, geklikt, cooldown of T02 arm B |
| 2 | TP · CODE · B2-CLICKED · pan/acc (121177250, 121177252) | `tp-b2-clicked.html` | + 2 dagen tot 09:00, geklikt, T02 arm A, coupon B2_10_48H |

Filters (blijven): Added to Cart, Checkout Started, Placed Order 0 sinds flowstart; geen mail uit TZG9Mx, QUBUQV, T4a5Mk in 7 dagen; **geen mail uit WdRz5k in 7 dagen**; **geen Klaviyo Viewed Product (XNtYMB) in de laatste 1 dag**; niet in deze flow in 7 dagen; herinstap 7 dagen. Het open punt van de kliksplit 121177235 (nog $flow = WdRz5k, moet QNZyEb worden) blijft staan; zonder die fix krijgt bijna niemand in de kookgerei-tak een B2-CLICKED-mail.

## 3. Mails, onderwerp en preview

Alle vijf onderwerptypes per mail staan in de topcomment van elke bron. A/B: één variabele (onderwerp), winnaar op unieke kliks, minimaal 4 weken, geen automatische winnaar (PLAYBOOK 6). Waar de A-variant de huidige WdRz5k-tekst is, kunnen we TP direct vergelijken met de gewone browseflow.

| Mail | Onderwerp A | Onderwerp B | Preview | Knop |
| --- | --- | --- | --- | --- |
| TP · B1 | Get this pan with 10% off (controle, winnaar B1 WdRz5k) | Three questions to ask before you buy a pan | Here it is again, with the lab report, the 75-year warranty and 10% off. | Get 10% off this pan |
| TP · B1-ACC | Looked twice? Here's the detail. (controle) | We started with the cutting board | Here it is again. What it's made of, and 10% off with HI10. | Get 10% off this board/apron/... |
| TP · B2-NOTCLICKED | Why we can cover this pan for 75 years | How long did your last pan last? | Nothing on it to wear off. That's why the warranty is this long. | Get 10% off this pan |
| TP · B2-CLICKED nocode | "I ordered one pan to try it out" (controle) | Two promises, before you decide | If you change your mind, or if something's wrong. Both are covered. | Get mine + 4 gifts |
| TP · CODE · B2-CLICKED | Your own 10% expires in 48 hours (controle) | Want 10% off the one you went back to? | Already applied with the button. In 48 hours we remove it. | Use my 10% now |

Inhoud in het kort:
- **TP · B1**: codebalk HI10, header, "THE ONE YOU LOOKED AT / Here it is again. / In case it got lost between tabs.", groot productblok met HI10-regel, knop, "Ask these three questions." (lab, rapport 25895 met certificaat, 75 jaar), korte noot van Benjamin met één eerlijke beperking (zonder coating komt loslaten van hitte: 2 tot 3 minuten middelhoog, een theelepel olie), reviews R169 Michael G. (ei) en R240 Brandon W. (garantie), gifts-strook, knop, ondertekening. Principes: autoriteit, wederkerigheid, sociaal bewijs.
- **TP · B1-ACC**: zelfde opening met het accessoire groot, Benjamin: eerst titanium snijplanken, dan de pan; het about-blok per accessoire (bestaand blok), reviews R158 en R148, daarna "AND THE PAN THAT CAME AFTER" met de Pan Pro-kaart als tweede stap (concurrentie-idee 10: een kleine instap naast het bekeken product), gifts, knop. Ondertekening: één op vijf orders is een cadeau (enquête).
- **TP · B2-NOTCLICKED**: "COVERED FOR 75 YEARS / Nothing on it to wear off.", foto w1v3-intro, compacte productkaart, Benjamin legt het mechanisme uit (coating op metaal slijt, wij hebben er geen) en wat de garantie dekt (deuk, kromme bodem, losse greep of klinknagel, deksel die niet meer past), de enige vergelijking van deze flow (`vs kind="pfas"`), reviews R583 Scott Y. ("the last pans we ever have to purchase") en R240, gifts, knop.
- **TP · B2-CLICKED nocode**: geen code en geen HI10 (zoals v4 3.15). "BEFORE YOU DECIDE / Two promises.": (1) unused, binnen 30 dagen na levering terugsturen, volledige refund; (2) beschadigd of defect in de eerste 30 dagen: refund of vervanging, wij betalen de verzending, daarna (alleen bij kookgerei) de 75-jaar garantie. Dan Sunny C. (R025) als case, gifts-strook, reviews R029 Jerry G. en R240 over de service, knop.
- **TP · CODE · B2-CLICKED**: codebalk met vervaldatum, "YOUR OWN CODE / Your own 10%.", groot productblok, knop, één alinea met reden en einde ("made for you, so it has an end date ... we're removing your discount"), espresso aanbodblok met 48 uur, "In case you're new to us" (eerste orders 20 december 2024 en 100,000+ klanten, rapport 25895, 75 jaar), gifts met urgentieregel van de fall sale, reviews R577 en R240, knop, P.S. met de datum.

## 4. Wat is anders dan de kopie, en waarom

| Kopie (WdRz5k-templates) | v3 | Waarom |
| --- | --- | --- |
| Gebakken hero met kop en aanbodbalk, klein productkaartje eronder | Live kop + het bekeken product groot (B1, B1-ACC, CODE) | TP-bezoekers zijn vaak op een ander apparaat of via een advertentie gekomen; ze moeten eerst herkennen wat ze bekeken. Live tekst laadt ook zonder beelden. |
| B1: Benjamin-verhaal over PFAS (S1) | B1: drie vragen met rapport, certificaat en garantie | Kouder publiek: controleerbaar bewijs boven een verhaal. De drie vragen zijn de kern van bewijsmails (DECISIONS 1 okt). |
| B2-NOTCLICKED: sceptici (James, Tammy) + gietijzer | Garantie als hoofdboodschap + PFAS-vergelijking | Concurrentie-idee 6; de RVS- en gietijzervergelijking zitten al in cart en WdRz5k, PFAS past bij de reden waarom 68 tot 76% koopt. |
| B2-CLICKED nocode: Sunny C. | Twee beloftes vooraan, Sunny C. als bewijs | Prijs is het grootste bezwaar; zonder code halen we het risico weg in plaats van een korting te geven. |
| CODE: code + verhaal 20 dec 2024 | Code + drie regels "new to us" | Zelfde code, zelfde regels; korter verhaal, want deze lezer kent ons minder. |
| UTM utm_campaign=v4-browse in de templates | utm_campaign=v4-browse-tp in elke link | Zo is TP-omzet op linkniveau te scheiden van WdRz5k (was alleen op berichtniveau). |
| "Founder, Siraat's Kitchen" | "Founder, Siraat" | Merknaam in copy is Siraat (DECISIONS 15 okt). |

Ongewijzigd: HI10 in B1 en B1-ACC (codebalk, knoplink met de korting al toegepast), geen HI10 in B2-CLICKED nocode, coupon B2_10_48H met 48 uur in de CODE-mail, gifts-blokken, friction reducers via `{{FRICTION}}`, markt-helper browse (`<!-- MARKET-SIGNAL: browse -->`, de map heet browse-tp), vaste header en footer uit `partials/`.

## 5. Controle (19 okt)

- `python3 -I scripts/check_previews.py browse-tp`: 0 problemen. 0 em dashes in alle bronnen en builds.
- Playwright 375 px (2x): geen horizontale scroll (scrollWidth 375), geen kapotte beelden. Hoogte mobiel: B1 3.635, B1-ACC 3.471, B2-NOTCLICKED 3.412, B2-CLICKED nocode 2.752, CODE 3.599 px (grens ~3.600 op 390 px; B1 zit er net op).
- Beelden: alleen bestaande Klaviyo-CDN-beelden (`certificate.jpg`, `w1v3-intro.jpg`, plus gedeelde blokken), dus `.klaviyo.html` is compleet. Geen nieuwe Higgsfield-beelden, 0 credits.
- Reviews alleen uit `content/reviews/sets.json` (gecontroleerde Trustpilot-snippets), via `reviews3 ids=...`; Sunny C. letterlijk.

## 6. Open punten

1. [VRAAG FLORIS] Akkoord op de copy en de A/B-keuzes; B2-NOTCLICKED heeft geen controle uit WdRz5k (beide onderwerpen nieuw).
2. Kliksplit 121177235 naar $flow = QNZyEb (zie 12-fixes.md), anders werkt de B2-CLICKED-tak niet.
3. `qa_render.py` draait over vaste flowmappen; browse-tp nog toevoegen of de mails eenmalig met een Klaviyo template-render op een echt V48nhq-event controleren (vooral prijsnotatie "$144.00": met decimalen valt de prijsterugval van de browse-helper weg, dan bepaalt `person.Country` of de prijs zichtbaar is).
4. Shopify-productbeelden zijn soms `.webp` (zoals in de huidige templates); Outlook desktop toont die niet.

## 7. Livegang (alleen na akkoord, niets hiervan gedaan)

1. Vijf templates aanmaken in Klaviyo (CODE-editor, volledige HTML uit `tp-*.klaviyo.html`), namen "v4 · Browse TP · B1" enzovoort.
2. In QNZyEb per bericht "Change template" naar het nieuwe template (de nocode-berichten en de pan/acc-varianten krijgen hetzelfde template), onderwerp en preview uit sectie 3, B-varianten als A/B-test op onderwerp.
3. Preview-sends naar Gmail met uniek onderwerp per send (PLAYBOOK 6), daarna de livegangstappen uit 12-fixes.md.

Terugdraaien: in QNZyEb de templates terugzetten op de kopieën (WchdbC, TLQh4w, TGd2H8, WE3K7t, WzquL5, VWps9s, XPszZj, STVtpH, X3b2FU) of de flow op Draft laten.
