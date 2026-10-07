# 01 · Inbox- en deliverability-check van de 59 v4-mails

Datum: 7 oktober 2026. Alleen lokaal gemeten, niets naar Klaviyo, geen templates gewijzigd. Inventaris: `exports/manifest.csv` (59 mails). Elke mail is gebouwd zoals de export (`build_template.py` via `qa_render.py`) en met Django gerenderd op de echte voorbeeld-events per trigger. Bouwt op `research/lijst/02-deliverability.md` (Outlook-spamratio 0,31 procent in Q3, verdubbeld volume sinds september) en `klaviyo/flows/v4-flow-system.md` (timing en prioriteit).

Nieuwe gereedschappen (opnieuw draaien vanuit /tmp met `python3 -I`):
- `scripts/inbox_checks.py`: statische controles, ook als waarschuwingen in `scripts/qa_render.py` (punt f, nooit FOUT).
- `scripts/qa_inbox.py` + `scripts/qa_inbox.js`: volledig rapport met browsermetingen (dark-mode-simulatie, contrast, lettergrootte, tap targets). Uitvoer `exports/qa/inbox-report.md`, `exports/qa/inbox-data.json`, screenshots `exports/qa/darkmode/`.

## Verslag

De mails zelf zijn gezond voor de inbox. Geen enkele mail komt in de buurt van Gmail-clipping: geschat 20 tot 52 KB verzonden (inclusief Klaviyo-linktracking), tegen een grens van 102 KB. Elke mail heeft veel live tekst (845 tot 2.600 tekens), beeld beslaat hooguit een derde van het oppervlak, 13 tot 31 links naar maar drie domeinen, geen linkverkorters, alles https, elk beeld heeft een alt-attribuut. Spamwoorden zijn mild: "Last chance" in het onderwerp van C4 en K3, "FREE" in hoofdletters in de codebalk.

De echte problemen zitten in weergave en frequentie:
1. **Dark mode**: het header-logo (zwart lockup op transparant) verdwijnt in Gmail-apps, Outlook.com en de Outlook-app (contrast 1,1:1). Bij volledige inversie (Gmail iOS, Outlook Windows) verdwijnt ook het witte footer-logo. Dat raakt precies de Outlook-groep die nu 0,31 procent klachten geeft: een afzender die je niet herkent, meld je sneller als spam.
2. **Outlook Windows**: 14 mails hebben een knop zonder VML (het witte aanbodblok-knopje), daar wordt het een smalle balk waarin alleen de tekst klikbaar is. De preheader mist `mso-hide:all` in alle 59.
3. **Toegankelijkheid**: grijs #727272 op crème haalt 4,48:1 (net onder AA), #9A948B 2,8 tot 3,0:1. Footer-links zijn 17 px hoog, iconen 32 px, het header-logo 34 px. De friction reducer staat op 12 px.
4. **Frequentie**: met de v4-regels kan een actieve nieuwe inschrijver 8 flowmails in 7 dagen krijgen, een bestaande abonnee 6 flowmails plus 3 campagnes. Dat is twee keer het plafond van 4 per week uit het lijstvoorstel. In de oude T01-arm blijft Failure to launch draaien: tot 10 mails per week voor juist de niet-klikkers.

## Top 10 fixes (voorstel, templates zijn niet aangepast)

| # | Fix | Waar | Raakt | Waarom |
|---|---|---|---|---|
| 1 | **Logo dark-mode-proof.** Header: lockup met crème achtergrond ingebakken (`siraat-lockup-black-email.png` geplat op #F8F7F2, via script uit het officiële bestand, niet nagetekend), zodat Gmail en Outlook een leesbaar crème label tonen. Footer idem: `siraat-lockup-white-email.png` geplat op #282828. Optioneel daarbovenop een wissel voor Apple Mail en Outlook.com: `.lg-d` (witte lockup) naast `.lg-l` met `@media (prefers-color-scheme: dark)` en `[data-ogsc]`, en dan `color-scheme: light dark`. Gmail-apps ondersteunen geen van beide, dus het geplatte bestand is de enige oplossing die overal werkt. | `partials/header.html`, `partials/footer.html`, `logo-black.png`/`logo-white.png` in elke assets-map | 59 | Logo 1,1:1 in gedeeltelijke inversie, wit footer-logo 1,3:1 in volledige inversie |
| 2 | **Eén plafond over flows en campagnes.** Segment "v4 · Frequentieplafond" = Received Email (alle mail) minstens 4 keer in 7 dagen (2 voor niet-klikkers 90 d), uitsluiten bij elke campagne; campagnes wijken altijd voor checkout/cart/browse. Oude T01-arm (T2SmtR) uitsluiten van campagnes of T2SmtR in de oude arm inkorten. Welcome-overslaan van 1 naar 2 dagen na een checkout- of cartmail. | flowconfiguratie, segmenten (geen template) | alle profielen | Max nu 8 tot 10 per week; uitschrijving sprong van 0,98 naar 1,60 procent bij 3 naar 4 per week |
| 3 | **VML-knop in het aanbodblok** en in de twee losse knoppen: `<v:roundrect fillcolor="#FFFFFF">` met tekst #321E1D, zoals `cta.html` al doet. | `partials/blocks/offer.html`; w2 "Shop with my 10%", v1/v1-nocode "Claim my 15%" | 14 | In Outlook Windows valt padding op `<a>` weg: knop van 18 px hoog |
| 4 | **Contrast**: #727272 naar #6E6E6E (4,75:1 op crème, 5,1:1 op wit); #9A948B voor tekst op licht naar #767067 (4,57:1 / 4,9:1). Doorgestreepte prijs mag #767067 met line-through. PLAYBOOK 2 meeveranderen. | blokken `cta` (sub), `gifts`, `ugc`, `compare`, `productcard`, ondertekening in de bronnen | 59 | 310 tekstregels onder AA over 59 mails, vooral friction reducer en "Founder, Siraat's Kitchen" |
| 5 | **Tap targets in header en footer**: footer-navigatie `display:block;padding:15px 4px` op de `<a>` (nu op de td, link 17 px); social-iconen in een `<a>` met 6 px padding (44x44); header-logo-link `display:block;padding:5px 0`. | `partials/header.html`, `partials/footer.html` | 59 | 8 links per mail onder 44 px |
| 6 | **Preheader `mso-hide:all`** toevoegen. Kan centraal in `build_template.py` (regex op `<div style="display:none;font-size:1px`), dan hoeven de 59 bronnen niet aangepast. | `build_template.py` of de preheader-div per bron | 59 | Outlook desktop kan de preheader boven de mail tonen |
| 7 | **Eigen plain-text-versie** meesturen in `export_klaviyo.py` (attribuut `text` van de template), gemaakt uit de HTML zonder verborgen desk/mob-blokken, zonder navigatie en met korte links. Voor de tekstmails W2, S2 en V2 is de tekstversie de mail zelf. | `scripts/export_klaviyo.py` (nieuw veld), geen template | 59, vooral 7 met dubbele regels | Klaviyo's automatische versie zet desk- en mob-varianten allebei in de tekst en begint met drie navigatie-URL's met UTM |
| 8 | **Kaartlinks groter**: "Shop the set →", "Find my size →", "Pick →" zijn 16 tot 20 px hoog. `display:inline-block;padding:12px 0` op de link in `productcard.html` en de maatkiezers, of de hele kaart als link. | `partials/blocks/productcard.html`, maatkiezers in w4, c3-p, r1, n1/n2, v1, r2 | 19 | Tap target < 44 px midden in de verkoopzone |
| 9 | **Spamwoorden**: onderwerp C4 "Last chance: your own 10% ends in 48 hours" naar "Your own 10% ends in 48 hours" (deadline blijft echt), idem K3-body; "FREE SHIPPING" in de codebalk van de nocode-mails in zinskapitalen; review met "!!!" in P3-set vervangen door een andere letterlijke Trustpilot-review. | `checkout/c4.html`, `cart/k3.html`, 13 nocode-mails, `post-purchase/p3-set.html` | 16 | Klassieke filters wegen "last chance", hoofdletters-FREE en "!!!" mee |
| 10 | **Kleine tekst**: friction reducer van 12 naar 14 px en twee regels op mobiel accepteren; lopende noten in kaarten en compare-noten van 12/13 naar 14 px. Gemeten breedte (Arial, zoals Gmail): de US-regel is 334 px bij 12 px en 390 px bij 14 px, de beschikbare breedte is 346 px. De varianten "One use, already applied ..." (398 px) en "duties paid" (403 px) lopen nu al op twee regels. Besluit nodig: PLAYBOOK 12 schrijft 12 px en één regel voor. | `cta.html` (sub), `productcard.html`, `compare.html` | 59 | De opdracht vraagt >= 14 px voor body op mobiel |

Kleiner, niet in de top 10: lege alt op de vergelijkingskop (`compare-cap-panpro.png`, 512 px) in b1, c1, k2-new, a2, voorstel `alt="Siraat Titanium Pan Pro"`; `icon-discount-tag.png` (brick op transparant) haalt in dark mode net 3,0:1; vier gift-beelden en packshots op wit worden in dark mode witte tegels (verwacht en acceptabel, ze staan in witte kaarten); onderwerp B van W2 in de topcomment is "December 20, 2024" (niet gebruikt, v4 3.19); W2 bevat nog `[VRAAG FLORIS ...]`-plekken (bekend, mail staat op NIET LIVE).

## 1. Gmail-clipping

| Maat | Bereik over 59 mails |
|---|---|
| Ruwe HTML na rendering (grootste event-variant) | 11 tot 37 KB |
| Quoted-printable gecodeerd (zoals verzonden; elke `=` wordt `=3D`) | 12 tot 39 KB |
| Geschat verzonden: QP + 600 bytes per link (Klaviyo-klikredirect) + 0,5 KB | **20 tot 52 KB** (max w4-us 52, c1 50, a2 48) |
| Grens Gmail | ~102 KB |

Marge minimaal 50 KB. Zelfs met 900 bytes per trackinglink blijft de grootste mail onder 65 KB. Bewaking: `qa_render.py` waarschuwt vanaf 80 KB geschat, ernstig vanaf 95 KB.

## 2. Spamsignalen, links, alt-teksten en plain text

**Onderwerp en preview.** Geen uitroeptekens, geen woorden in hoofdletters, geen "$$$", geen "FREE". Eén trigger: "Last chance" in onderwerp A van C4 en K3 (ook in de body). Onderwerpen met "% off" (k3, b2, p3, r2) zijn gangbaar en niet gemarkeerd.

**Body.** "FREE" in hoofdletters in 35 mails (codebalk "FREE SHIPPING · 4 GIFTS WITH EVERY ORDER" in nocode-mails, icoonteksten); "!!!" twee keer in een review in P3-set (6 uitroeptekens in die mail); "no cost" in een review in V1/V1-nocode; "cash" in W1-B ("Not a cash card"). Allemaal licht; alleen de hoofdletters en "!!!" zijn makkelijk weg te nemen.

**Tekst tegenover beeld.** Live tekst 845 (V2) tot 2.601 tekens (P2); beeld beslaat 1 tot 32 procent van het mailoppervlak op 600 px. Geen enkele mail is "één groot beeld". De hero bevat gebakken tekst, maar alles wat daarin staat staat ook live (aanbodbalk, codebalk, alt).

**Links.** 13 tot 31 links per mail, allemaal https, drie domeinen (siraatskitchen.com, facebook.com, instagram.com), geen linkverkorters, geen linktekst die een ander domein noemt. Klaviyo herschrijft bij verzending elke link naar zijn eigen klikdomein; dat is normaal en zit in de grootte-schatting.

**Alt-teksten.** Elk beeld heeft een alt-attribuut. Hero-alts noemen het aanbod letterlijk (h11). Lege alt op decoratieve iconen (18 tot 20 px) is correct; de 512 px vergelijkingskop met lege alt staat al als waarschuwing in de export.

**Plain-text-versie.** `export_klaviyo.py` stuurt alleen `html` mee, geen `text`. Klaviyo maakt dan volgens zijn eigen documentatie bij verzending automatisch een tekstversie uit de HTML (ook bij CODE-templates). Niet zelf bevestigd in Klaviyo (geen API-calls in deze sessie): controleer één keer met `GET /api/templates/U8Ngv8` (veld `text`) en "Preview > Plain text" in de editor. Benadering van hoe die versie eruitziet (`inbox_checks.plain_text`, html2text-achtig, CSS telt niet):

```
Saved exactly as you left it. Free shipping, and HI10 takes 10% more.

EXTRA 10% OFF YOUR ORDER · CODE HI10

COOKWARE (https://siraatskitchen.com/collections/pans?utm_source=klaviyo&utm_medium=email&utm_campaign=v4-checkout&utm_content=c1-nav-pans)
SETS (https://siraatskitchen.com/collections/bundles?utm_source=...)
ABOUT (https://siraatskitchen.com/pages/faq?utm_source=...)

STILL IN YOUR CART
Titanium Hammered Pan Pro Standard
Qty 1
$134.00
HI10 takes an extra 10% off, and your $70 in gifts are still attached to this cart.
Complete my order → (https://siraatskitchen.com/checkouts/.../recover?key=x&discount=HI10&utm_...)
Free shipping. 30-day returns. 100,000+ happy customers.
...
"Great to know no chemicals are being released into our food when cooking with this pan!"   (2x: desktop- en mobielversie)
```

Bevindingen: geen Django-restanten (0 van 59), wel (a) in 7 mails 3 tot 5 regels dubbel doordat verborgen desk/mob-varianten allebei meekomen (c1, k1, c3-p, p3-accessory(-nocode), p3-set, r1-acc, r2), (b) elke tekstversie begint na de preheader met drie navigatie-URL's met lange UTM, (c) bij founder-mails W2, S2, V2 is de tekstversie voor veel lezers (Apple Watch, sommige zakelijke filters) de echte mail. Fix 7.

## 3. Dark mode

Vier weergaven per mail op 390 px: licht, `prefers-color-scheme: dark`, gedeeltelijke inversie (Gmail Android, Outlook.com, Outlook-app: lichte vlakken donker, donkere tekst licht) en volledige inversie (Gmail iOS, Outlook Windows: alle kleuren omgekeerd). Beelden blijven in alle clients ongewijzigd. Inversie is een simulatie in Chromium (HSL-lichtheid omgekeerd, begrensd op 7 en 93 procent), geen echte client.

| Weergave | Wat er gebeurt | Clients |
|---|---|---|
| `prefers-color-scheme: dark` | Niets: `<meta name="color-scheme" content="light">` en geen dark-mode-CSS, dus de mail blijft licht. Goed. | Apple Mail, iOS Mail, Outlook Mac |
| Gedeeltelijke inversie | Crème en wit worden bijna zwart. **Header-logo zwart op transparant: 1,1:1, onzichtbaar.** Gift-beelden en packshots op wit worden witte tegels. Brick-knoppen, codebalk en footer blijven. Tekstcontrast blijft in orde. | Gmail Android, Outlook.com, Outlook iOS/Android |
| Volledige inversie | Als hierboven, plus: footer wordt lichtgrijs, **wit footer-logo 1,3:1**, Facebook/Instagram-iconen verliezen hun vorm, codebalk wordt licht met donkere tekst, knop wordt zalm met donkere tekst (leesbaar). | Gmail iOS, Outlook Windows (dark) |

Witte PNG-randen: de transparante PNG's (logo's, iconen, stickers) zijn schoon uitgesneden, zonder witte halo. Eén PNG is dekkend met een lichte achtergrond: `compare-cap-panpro.png` (RGB, 1024x284, vergelijkingskop in b1, c1, k2-new, a2); die wordt in dark mode een lichte strook boven de vergelijkingstabel. De overige lichte "randen" zijn JPG's met witte achtergrond (gift-ebook, gift-filter, gift-mystery, gift-shipping in 35 mails; packshot-1, p-set6, p-lid, p-wok, p-board). Dat is de foto zelf; ze staan in licht ook al in witte kaarten, dus acceptabel.

Tekstcontrast in de simulaties: 0 tot 2 regels per mail onder AA, alleen de #9A948B-noten (3,6 tot 3,7:1). Door de inversie wordt #727272 op donker zelfs beter leesbaar dan in licht.

Screenshots (licht · dark · gedeeltelijk · volledig naast elkaar): `exports/qa/darkmode/checkout-c1.jpg`, `browse-b1.jpg`, `welcome-w1-a.jpg`, `welcome-w2.jpg`, `post-purchase-p2.jpg`, `winback-r2-vip.jpg`.

## 4. Outlook (Windows, Word-engine)

| Onderdeel | Stand | Oordeel |
|---|---|---|
| Hoofdtabel | `width="600"` als attribuut plus `max-width` in de stijl | Goed, geen ghost table nodig |
| `max-width` op div of tabel zonder width | Niet gevonden | Goed |
| Beelden | Alle beelden hebben een `width`-attribuut | Goed (anders toont Outlook de 1200 px bron) |
| Primaire knop `{{BLOCK:cta}}` | `v:roundrect` met `<!--[if !mso]>`-fallback | Goed (bulletproof) |
| Aanbodblok-knop (wit op espresso) en twee losse knoppen | Alleen `<a style="display:block;padding">` in een td met bgcolor | **14 mails zonder VML** (n2, b2-clicked, k3, c4, v1, v1-nocode, w1-a, w2, w3, w4-int, w4-us, w5, r2, r2-vip). Knop wordt 18 px hoog, alleen de tekst klikbaar |
| Verborgen mobiele varianten (`.mob`, `.ug-mob`) | `display:none;max-height:0;overflow:hidden;mso-hide:all` | Goed |
| Preheader | `display:none` zonder `mso-hide:all` | **59 mails**: kan zichtbaar worden in Outlook desktop |
| Achtergrondafbeeldingen | Geen | Niets nodig |
| Fonts | `@import` buiten mso, Arial afgedwongen in mso | Goed |
| `border-radius`, `letter-spacing`, `text-transform` | Genegeerd door Outlook | Cosmetisch, acceptabel |

Relevantie: Hotmail/Outlook.com is 12,5 procent van de mail maar 63 procent van de teruggemelde klachten (02-deliverability). Die lezers zien de Outlook.com-weergave (dark mode gedeeltelijk, VML niet nodig); Outlook Windows is vooral Office 365 (2 procent). Fix 1 weegt voor de klachtengroep dus zwaarder dan fix 3.

## 5. Toegankelijkheid (390 px)

| Toets | Uitkomst | Waar |
|---|---|---|
| Lopende tekst >= 14 px | Bodytekst 15 tot 16 px: goed. Onder 14 px: friction reducer 12 px (in alle verkoopmails, 77 keer), "One use, already applied" 12 px (15), kaartteksten 13 px, Light Labs-noot 12 px, eyebrows 11 tot 12 px (labels, geen lopende tekst) | `cta.html` sub, `productcard.html`, `compare.html`, `gifts.html` |
| Tap targets >= 44 px | Primaire knoppen 56 px: goed. Te klein: header-logo-link 34 px, footer-navigatie 17 px (4 links), Facebook/Instagram 32x32, kaartlinks 16 tot 20 px (19 mails), maatkiezer-rijen 43 px (w4) | `header.html`, `footer.html`, `productcard.html` |
| Contrast WCAG AA (4,5:1; groot 3:1) | Bodytekst #282828 op crème 13,7:1. Onder AA: #727272 op crème 4,48:1 (friction reducer, ondertekening, noten: 1 tot 11 regels per mail), #9A948B 2,8 tot 3,0:1 (doorgestreepte prijs $439/$1,186 in 22 mails, Light Labs-noot) | kleuren in PLAYBOOK 2 |
| Taal en structuur | `lang="en"`, tabellen `role="presentation"`, alt overal | Goed |

## 6. Frequentie-risico met de v4-timing

Regels die meetellen (v4-flow-system 1.2 en 1.3): Smart Sending uit in flows; campagneplafond 3 per 7 dagen, **flowmails tellen niet mee**; nieuwe inschrijvers 14 dagen geen campagnes; welcome-mail overgeslagen bij een checkout- of cartmail in de laatste **1 dag**; browse start niet na een welcome-, cart- of checkoutmail in 7 dagen; cart niet na een checkoutmail in 7 dagen; checkout niet na een post-purchase-mail in 7 dagen. Browse en cart hebben géén post-purchase-filter.

**Scenario A, nieuwe inschrijver, actieve shopper, koopt niet (v4-arm).**

| Dag | Mail |
|---|---|
| 0, 10:20 | W1 |
| 1, 09:00 | W2 (nog geen cart/checkout) |
| 1, 10:30 | K1 (Added to Cart 10:00) |
| 1, 20:30 | C1 (Checkout Started 20:00; cart stopt) |
| 2, 20:30 | C2 |
| 3, 09:00 | W3 overgeslagen (C2 12,5 uur eerder) |
| 4, 09:00 | C3 |
| 6, 09:00 | C4, en W4 (C3 was 48 uur eerder, dus W4 gaat ook) |

**8 flowmails in 7 dagen**, twee op dezelfde ochtend. Geen campagnes (welkomstbescherming).

**Scenario B, bestaande abonnee (> 14 dagen), geen klant.** Browse B1 (dag 0), B2 (dag 2), cart K1 en checkout C1 (dag 3), C2 (dag 4), C3 (dag 6): **6 flowmails plus 3 campagnes = 9 in 7 dagen.**

**Scenario C, klant net na de order.** P1 (dag 0), browse B1 en B2 (dag 1 en 3), cart K1, K2-returning (dag 4 en 5): **5 flowmails plus 3 campagnes = 8.** Rond levering: P2, U1 (levering + 4) en P3 (order + 20) binnen 8 dagen, plus campagnes.

**Scenario D, oude T01-arm (50 procent van de nieuwe inschrijvers tot 20 november).** T2SmtR blijft daar live: 10 mails van dag 30 tot 41, dus 6 tot 7 per week, plus 3 campagnes: **tot 10 per week**, voor profielen die per definitie niet kochten en vaak niet klikken. Dat is de groep waar 82 procent van de spamklachten vandaan komt.

**Past dat bij de regels?**
- Het campagneplafond (3) werkt, maar telt flows niet mee. Het lijstvoorstel (03-voorstel 3) wil 4 per 7 dagen voor flows en campagnes samen, 2 voor niet-klikkers, en campagnes die wijken voor abandonment. Alle vier de scenario's gaan daar overheen (8, 9, 8, 10).
- De prioriteitsregels voorkomen twee verkoopflows tegelijk binnen de abandonment-keten, maar welcome en checkout lopen wél samen (1-dagvenster te kort), en browse/cart lopen door na een aankoop.
- Risico concentreert zich in scenario D (niet-klikkers) en in piekweken met 4+ campagnes. Scenario A en B raken mensen die net actief op de site waren: daar is de klachtkans laag, maar de uitschrijfkans stijgt (timing 10: 3 naar 4 mails per week gaf 0,98 naar 1,60 procent).

Voorstel (fix 2): segment "v4 · Frequentieplafond" op alle Received Email (4 in 7 dagen; 2 voor geen klik in 90 dagen) uitsluiten bij campagnes; welcome-overslaan naar 2 dagen; browse en cart de post-purchase-filter van checkout geven (post-purchase-mail in 7 dagen); oude T01-arm uitsluiten van campagnes zolang T2SmtR loopt.

## 7. Wat er in de QA-poort is toegevoegd

`scripts/qa_render.py` roept `inbox_checks.warnings()` aan per mail, na de Django-rendering; alles is waarschuwing ("let op"), nooit FOUT, en een fout in de checks breekt de poort niet. `qa_render.py --static`: 59 mails, 59 groen, 0 FOUT (ongewijzigd). Automatisch bewaakt:
- geschatte verzonden grootte > 80 KB (Gmail-clipping)
- spamsignalen in onderwerp A/B, preview en body; uitroeptekens; hoofdletterwoorden in onderwerp en preview
- weinig live tekst tegenover beelden, > 40 links, > 6 linkdomeinen, linkverkorters, http-links, linktekst met ander domein
- beeld zonder alt, alt als bestandsnaam, beeld zonder width-attribuut
- Outlook: knop zonder VML, verborgen element of preheader zonder `mso-hide:all`, achtergrondbeeld zonder VML, max-width zonder width
- dark mode: donker beeld op transparant zonder dark-mode-variant (het header-logo)
- plain text: regels die dubbel in Klaviyo's tekstversie komen door verborgen varianten

Niet in de poort (browser, trager): contrast, tap targets, lettergrootte en de dark-mode-simulatie. Die staan in `python3 -I scripts/qa_inbox.py` (ongeveer 1 minuut voor 59 mails). Frequentie is flowconfiguratie, geen templatecheck.

## 8. Per mail

Bron: `exports/qa/inbox-data.json`. Geldt voor alle 59 en staat daarom niet per regel: header-logo onleesbaar in dark mode, preheader zonder `mso-hide:all`, 7 footer-links onder 44 px, header-logo-link 34 px. "Contrast < AA" telt regels buiten de footer in de lichte weergave; zonder kleur tussen haakjes is het #727272 (4,48:1). "Tekst < 14 px" telt regels van meer dan 40 tekens; de friction reducer (12 px) zit erin. "Tap < 44 px" zonder header en footer.

| Mail | KB (ruw / geschat verzonden) | Links | Live tekst (tekens) | Beeld % | Contrast < AA (licht) | Tekst < 14 px | Tap < 44 px | Bijzonderheden |
|---|---|---|---|---|---|---|---|---|
| anniversary/n1 | 25 / 40 | 22 | 1997 | 22 | 4 | 1 (+1 buiten friction reducer) | 3: "Find my size →" 16 px, "Shop the board →" 16 px, "Shop the wok →" 16 px | body: "FREE"; dark: lichte kaders p-board.jpg, p-lid.jpg, p-wok.jpg |
| anniversary/n2-nocode | 28 / 44 | 24 | 1849 | 22 | 4 | 2 (+1 buiten friction reducer) | 3: "Find my size →" 16 px, "Shop the pan →" 16 px, "Shop the set →" 16 px | body: "FREE" x2; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg +3 |
| anniversary/n2 | 25 / 41 | 23 | 1944 | 21 | 4 | 1 | 3: "Find my size →" 16 px, "Shop the pan →" 16 px, "Shop the set →" 16 px | Outlook: knop zonder VML "Claim my 10% →"; dark: lichte kaders p-lid.jpg, p-panpro.jpg, p-set6.jpg |
| browse/b1-acc | 26 / 39 | 19 | 1614 | 18 | 7 ((154,148,139) 3.0:1) | 3 | 0 | body: "FREE"; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg; dark: icon-discount-tag.png |
| browse/b1 | 32 / 46 | 20 | 2039 | 19 | 8 ((154,148,139) 2.8:1, (154,148,139) 3.0:1) | 4 (+1 buiten friction reducer) | 0 | dark: lichte kaders compare-cap-panpro.png, gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg +1; dark: icon-discount-tag.png, icon-pfas-tested.png |
| browse/b2-clicked-nocode | 25 / 38 | 19 | 1620 | 17 | 8 ((154,148,139) 3.0:1) | 4 (+1 buiten friction reducer) | 0 | body: "FREE"; dark: icon-discount-tag.png |
| browse/b2-clicked | 28 / 40 | 18 | 1905 | 15 | 8 ((154,148,139) 3.0:1) | 3 (+1 buiten friction reducer) | 0 | body: "FREE"; Outlook: knop zonder VML "Use my 10% now →"; dark: icon-discount-tag.png |
| browse/b2-notclicked | 27 / 40 | 19 | 1777 | 17 | 7 ((154,148,139) 3.0:1) | 3 | 0 | body: "FREE"; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg; dark: icon-discount-tag.png |
| cart/k1-acc | 26 / 39 | 19 | 1598 | 18 | 7 ((154,148,139) 3.0:1) | 3 | 0 | body: "FREE"; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg; dark: icon-discount-tag.png |
| cart/k1 | 29 / 42 | 19 | 1834 | 23 | 8 ((154,148,139) 3.0:1) | 3 | 0 | plain-text: 4 regels dubbel (desk/mob); dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg +1; dark: icon-discount-tag.png |
| cart/k2-new | 30 / 43 | 20 | 2142 | 19 | 8 ((154,148,139) 2.8:1, (154,148,139) 3.0:1) | 6 (+3 buiten friction reducer) | 0 | dark: lichte kaders compare-cap-panpro.png; dark: icon-discount-tag.png, icon-gift.png |
| cart/k2-returning | 29 / 45 | 23 | 1866 | 18 | 7 ((154,148,139) 3.0:1) | 4 (+1 buiten friction reducer) | 0 | body: "FREE"; dark: lichte kaders card-deeppan.jpg, card-lid.jpg, gift-ebook.jpg, gift-filter.jpg +2; dark: icon-discount-tag.png |
| cart/k3-nocode | 27 / 40 | 19 | 1837 | 18 | 8 ((154,148,139) 3.0:1) | 3 | 0 | body: "FREE"; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg; dark: icon-discount-tag.png |
| cart/k3 | 26 / 38 | 18 | 1929 | 17 | 6 ((154,148,139) 3.0:1) | 2 | 0 | onderwerp A: "Last chance"; body: "Last chance"; Outlook: knop zonder VML "Use my 10% now →"; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg; dark: icon-discount-tag.png |
| checkout/c1 | 37 / 50 | 18 | 2067 | 20 | 7 ((154,148,139) 2.8:1) | 5 (+2 buiten friction reducer) | 0 | plain-text: 3 regels dubbel (desk/mob); dark: lichte kaders compare-cap-panpro.png, gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg +5; dark: icon-discount-tag.png |
| checkout/c2-acc | 26 / 39 | 18 | 1644 | 18 | 6 | 3 | 0 | body: "FREE"; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg +1; dark: icon-discount-tag.png |
| checkout/c2 | 26 / 39 | 20 | 1914 | 20 | 7 ((154,148,139) 3.0:1) | 4 (+1 buiten friction reducer) | 1: "Read report no. 25895 " 17 px | dark: lichte kaders certificate.jpg, gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg +2; dark: icon-discount-tag.png |
| checkout/c3-acc | 28 / 41 | 20 | 1915 | 18 | 7 ((154,148,139) 3.0:1) | 4 (+1 buiten friction reducer) | 0 | body: "FREE"; dark: lichte kaders card-panpro-save305.jpg, gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg +2; dark: icon-discount-tag.png |
| checkout/c3-p | 29 / 44 | 22 | 2379 | 16 | 5 | 6 (+3 buiten friction reducer) | 2: "Keep my one pan and ch" 17 px, "Keep my one pan and ch" 17 px | body: "FREE"; dark: lichte kaders card-set6.jpg, packshot-1.jpg; dark: icon-discount-tag.png |
| checkout/c3-s | 28 / 41 | 18 | 1941 | 18 | 6 | 3 | 0 | plain-text: 3 regels dubbel (desk/mob); dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg +1; dark: icon-discount-tag.png |
| checkout/c4-nocode | 26 / 38 | 18 | 2089 | 19 | 7 ((154,148,139) 3.0:1) | 4 (+1 buiten friction reducer) | 0 | body: "FREE"; dark: lichte kaders card-set12-save587.jpg, gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg +2; dark: icon-discount-tag.png |
| checkout/c4 | 26 / 38 | 17 | 1990 | 17 | 5 | 2 | 0 | onderwerp A: "Last chance"; body: "Last chance"; Outlook: knop zonder VML "Use my 10% now →"; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg +1; dark: icon-discount-tag.png |
| post-purchase/p1-first | 25 / 36 | 16 | 2399 | 20 | 4 | 1 (+1 buiten friction reducer) | 0 | dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg +1; dark: icon-tracking-email.png |
| post-purchase/p1-repeat | 20 / 31 | 16 | 1371 | 26 | 4 | 1 (+1 buiten friction reducer) | 0 | dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg +1; dark: icon-tracking-email.png |
| post-purchase/p2-safe | 20 / 31 | 16 | 2240 | 28 | 3 | 1 (+1 buiten friction reducer) | 0 | - |
| post-purchase/p2 | 24 / 36 | 18 | 2601 | 25 | 3 | 1 (+1 buiten friction reducer) | 0 | - |
| post-purchase/p3-accessory-nocode | 28 / 42 | 20 | 1628 | 28 | 5 ((154,148,139) 3.0:1) | 2 (+1 buiten friction reducer) | 0 | body: "FREE"; plain-text: 4 regels dubbel (desk/mob); dark: lichte kaders card-panpro-bestseller.jpg, gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg +2 |
| post-purchase/p3-accessory | 28 / 42 | 21 | 1842 | 27 | 5 ((154,148,139) 3.0:1) | 3 (+2 buiten friction reducer) | 0 | plain-text: 4 regels dubbel (desk/mob); dark: lichte kaders card-panpro-bestseller.jpg, panpro-mob.jpg |
| post-purchase/p3-apron-nocode | 25 / 38 | 20 | 1719 | 24 | 5 ((154,148,139) 3.0:1) | 2 (+1 buiten friction reducer) | 0 | body: "FREE" x2; dark: lichte kaders card-panpro-bestseller.jpg, gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg +1 |
| post-purchase/p3-apron | 29 / 43 | 21 | 2092 | 21 | 6 ((154,148,139) 3.0:1) | 2 (+1 buiten friction reducer) | 0 | body: "FREE"; dark: lichte kaders card-panpro-bestseller.jpg, gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg +1 |
| post-purchase/p3-next-nocode | 27 / 43 | 24 | 1646 | 23 | 4 | 3 (+2 buiten friction reducer) | 2: "See it →" 16 px, "See it →" 16 px | body: "FREE" x2; dark: lichte kaders card-board.jpg, card-lid.jpg, card-wok.jpg, gift-ebook.jpg +3 |
| post-purchase/p3-next | 25 / 42 | 25 | 1753 | 23 | 4 | 3 (+2 buiten friction reducer) | 2: "See it →" 16 px, "See it →" 16 px | dark: lichte kaders card-board.jpg, card-lid.jpg, card-wok.jpg |
| post-purchase/p3-pan-nocode | 26 / 41 | 22 | 1674 | 24 | 4 | 3 (+2 buiten friction reducer) | 0 | body: "FREE" x2; dark: lichte kaders card-board.jpg, card-lid.jpg, gift-ebook.jpg, gift-filter.jpg +2 |
| post-purchase/p3-pan | 26 / 42 | 23 | 1836 | 22 | 4 | 3 (+2 buiten friction reducer) | 0 | body: "FREE"; dark: lichte kaders card-board.jpg, card-lid.jpg |
| post-purchase/p3-set-nocode | 26 / 41 | 22 | 1658 | 24 | 4 | 3 (+2 buiten friction reducer) | 0 | body: "FREE" x2; dark: lichte kaders card-crepe.jpg, card-wok.jpg, gift-ebook.jpg, gift-filter.jpg +2 |
| post-purchase/p3-set | 32 / 48 | 23 | 2046 | 23 | 4 | 4 (+3 buiten friction reducer) | 0 | 6 uitroeptekens in de body; body: "!!!" x2, "FREE"; plain-text: 3 regels dubbel (desk/mob); dark: lichte kaders card-crepe.jpg, card-wok.jpg, ugc-prod-crepe.jpg, ugc-prod-set6.jpg +1 |
| site/a1 | 30 / 47 | 26 | 2006 | 18 | 8 ((154,148,139) 2.8:1) | 3 | 4: "Pick the Mini →" 16 px, "Pick the Small →" 16 px, "Pick the Standard →" 16 px | body: "FREE"; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg +3 |
| site/a2 | 33 / 48 | 22 | 1833 | 21 | 7 ((154,148,139) 2.8:1, (154,148,139) 3.0:1) | 6 (+3 buiten friction reducer) | 0 | dark: lichte kaders card-panpro-bestseller.jpg, card-set6.jpg, compare-cap-panpro.png, gift-ebook.jpg +3 |
| sunset/s1 | 13 / 22 | 14 | 983 | 27 | 2 | 1 (+1 buiten friction reducer) | 0 | - |
| sunset/s2 | 12 / 21 | 14 | 1002 | 2 | 3 | 1 (+1 buiten friction reducer) | 0 | - |
| ugc/u1 | 18 / 29 | 17 | 1956 | 23 | 4 | 2 (+2 buiten friction reducer) | 0 | - |
| vip/v1-nocode | 27 / 42 | 23 | 1883 | 21 | 4 | 1 | 3: "Find my size →" 16 px, "Shop the set →" 16 px, "Shop the set →" 16 px | body: "no cost"; Outlook: knop zonder VML "Shop with my 10% →"; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg +3 |
| vip/v1 | 25 / 40 | 23 | 1899 | 21 | 4 | 1 | 3: "Find my size →" 16 px, "Shop the set →" 16 px, "Shop the set →" 16 px | body: "no cost"; Outlook: knop zonder VML "Claim my 15% →"; dark: lichte kaders p-lid.jpg, p-set6.jpg, p-setpro.jpg |
| vip/v2 | 11 / 20 | 13 | 845 | 2 | 1 | 1 | 0 | - |
| welcome/w0 | 20 / 32 | 17 | 1505 | 32 | 4 | 2 (+2 buiten friction reducer) | 0 | - |
| welcome/w1-a | 25 / 38 | 18 | 1898 | 21 | 6 | 3 (+1 buiten friction reducer) | 0 | body: "FREE"; Outlook: knop zonder VML "Claim my 10% + gifts →"; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg |
| welcome/w1-b | 26 / 39 | 20 | 1929 | 28 | 11 ((154,148,139) 2.8:1) | 4 (+2 buiten friction reducer) | 0 | body: "FREE", "cash"; dark: lichte kaders gift-card.jpg, gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg +1 |
| welcome/w2 | 14 / 22 | 13 | 2010 | 1 | 1 | 1 | 0 | Outlook: knop zonder VML "Claim my 10% + gifts →" |
| welcome/w3 | 23 / 36 | 19 | 1533 | 28 | 5 | 3 (+1 buiten friction reducer) | 1: "Or read the lab report" 17 px | body: "FREE"; Outlook: knop zonder VML "Claim my 10% + gifts →"; dark: lichte kaders certificate.jpg |
| welcome/w4-int | 29 / 48 | 29 | 1746 | 21 | 5 | 3 (+1 buiten friction reducer) | 7: "Mini 8″ (20 cm) Eggs a" 43 px, "Pick →" 20 px, "Small 10″ (26 cm) Brea" 43 px | body: "FREE"; Outlook: knop zonder VML "Claim my 10% + gifts →"; dark: lichte kaders card-panpro-bestseller.jpg, card-set6.jpg |
| welcome/w4-us | 32 / 52 | 31 | 1842 | 20 | 7 ((154,148,139) 3.0:1) | 3 (+1 buiten friction reducer) | 3: "Mini 8″ (20 cm) Eggs a" 43 px, "Small 10″ (26 cm) Brea" 43 px, "Large 12″ (30 cm) A fa" 43 px | body: "FREE"; Outlook: knop zonder VML "Claim my 10% + gifts →"; dark: lichte kaders card-panpro-save305.jpg, card-set12-save587.jpg, card-set6.jpg |
| welcome/w5 | 27 / 40 | 19 | 1939 | 21 | 5 ((154,148,139) 3.0:1) | 2 | 0 | Outlook: knop zonder VML "Claim my 10% + gifts →"; dark: lichte kaders card-panpro-save305.jpg, gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg +1 |
| winback/r1-acc | 29 / 42 | 20 | 1681 | 27 | 5 ((154,148,139) 3.0:1) | 1 | 0 | plain-text: 4 regels dubbel (desk/mob); dark: lichte kaders card-panpro-save305.jpg, gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg +2 |
| winback/r1-pan | 30 / 48 | 26 | 1949 | 22 | 5 ((154,148,139) 3.0:1) | 2 (+1 buiten friction reducer) | 3: "Find my size →" 16 px, "See the wok →" 16 px, "See the crepe pan →" 16 px | body: "FREE"; dark: lichte kaders card-roast.jpg, gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg +4 |
| winback/r1-set | 30 / 47 | 26 | 1787 | 22 | 4 | 1 | 4: "See the crepe pan →" 16 px, "See the wok →" 16 px, "See the utensils →" 16 px | body: "FREE"; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg +4 |
| winback/r2-nocode | 28 / 44 | 24 | 1830 | 22 | 4 | 2 (+1 buiten friction reducer) | 3: "Shop the pan →" 16 px, "See the bundle →" 16 px, "Shop the set →" 16 px | body: "FREE" x2; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg +3 |
| winback/r2-vip-nocode | 28 / 44 | 24 | 1876 | 22 | 4 | 2 (+1 buiten friction reducer) | 3: "Shop the set →" 16 px, "Shop the set →" 16 px, "See the bundle →" 16 px | body: "FREE"; dark: lichte kaders gift-ebook.jpg, gift-filter.jpg, gift-mystery.jpg, gift-shipping.jpg +3 |
| winback/r2-vip | 25 / 41 | 23 | 1912 | 21 | 4 | 1 | 3: "Shop the set →" 16 px, "Shop the set →" 16 px, "See the bundle →" 16 px | Outlook: knop zonder VML "Claim my 15% →"; dark: lichte kaders p-2p2l.jpg, p-set6.jpg, p-setpro.jpg |
| winback/r2 | 31 / 47 | 23 | 2057 | 22 | 4 | 2 (+1 buiten friction reducer) | 3: "Shop the pan →" 16 px, "See the bundle →" 16 px, "Shop the set →" 16 px | Outlook: knop zonder VML "Use my 10% now →"; plain-text: 3 regels dubbel (desk/mob); dark: lichte kaders p-2p2l.jpg, p-panpro.jpg, p-set6.jpg, ugc-prod-panpro-b.jpg +2 |
