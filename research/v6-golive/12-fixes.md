# 12 · Fixes vóór livegang (fix-agent, 8 okt 2026)

Doel Floris: 0 fouten vóór livegang. Alles eerst in de bron, dan QA, dan Klaviyo. Status van de flows is nergens gewijzigd: de 13 v5-flows staan op Draft, de 13 TEST-kopieën op Live (gecontroleerd na afloop).

## Werkwijze en uitkomst

1. Bronfixes (tabel hieronder).
2. `python3 -I scripts/qa_render.py`: **61 mails, 61 groen, 0 FOUT**. `research/tailoring/test/run_tests.sh`: 0 FOUT (v5-bouwstenen 3294 ok, matrix 472/0). `check_previews.py`: 0 problemen.
3. `python3 -I scripts/qa_inbox.py templates --markets=US,UK` (122 renders): logo in dark mode, afmeldlink, contrast en cm in US zijn weg. Over: "Finish my order" (punt 8, keuze Floris), GIF's > 300 KB (binnen de 1 MB-grens), lichte productfoto's in geforceerd donker (geaccepteerd).
4. `export_klaviyo.py` dry-run 61/61 klaar, daarna `--live --i-am-sure --update`: 61 bibliotheektemplates bijgewerkt, 2 nieuwe beelden geüpload (logo-black-cream.png, logo-white-dark.png). W1-a/W1-b daarna nog een keer (fix 9).
5. Herkoppelen: elke send-email-actie van de 13 v5-flows en de 13 TEST-kopieën met een v5-template (186 acties, 93 Draft + 93 Live) via `PATCH /api/flow-actions/{id}` met de bibliotheek-template_id; Klaviyo maakt daarbij een nieuwe verborgen kopie. 34 acties van de oude T01-paden ("Old · ...") bewust niet aangeraakt.
6. Controle in Klaviyo: van alle 186 gekoppelde kopieën de HTML opgehaald: 186/186 ABOUT naar /pages/about-us, afmeld- en webviewlink #BDB8B0, geplatte logo's (CDN 68a06000.../c8e347f7...), geen "%%". Steekproef `POST /api/template-render` (p1-first US, r1-pan US, w1-b TEST): alle fixes zichtbaar, afmeldlink rendert als `<a href="[unsubscribe_tag]" style="color:#BDB8B0;">Unsubscribe</a>`. Onderwerp en preview van alle 220 flowberichten (26 flows) gescand op `{`, `}`, `[`, `]`, VRAAG, placeholder, TODO, em dash: alleen de {day}-preview (fix 6) kwam terug.

Werkbestanden (niet in git): scratchpad `fix/inv.json` (alle acties vooraf), `fix/relink*.csv` (oud -> nieuw template per actie), `fix/verify.csv` (controle per actie), `fix/split-*-oud.json` (splits vóór de wijziging).

## Fouten en fixes

| # | Fout | Bestand (bron) | Oud -> nieuw | Waar in Klaviyo bijgewerkt | Gecontroleerd |
|---|---|---|---|---|---|
| 1 | ABOUT ging naar /pages/faq, oud Facebook-adres (al in de bron, nog niet geëxporteerd) | `partials/header.html`, `partials/footer.html` | /pages/faq -> /pages/about-us; facebook.com/siraatskitchen -> facebook.com/people/SiraatsKitchen/61567176126958/ | 61 bibliotheektemplates, 186 flowacties | ja, 186/186 |
| 2 | Afmeldlink en "View in browser" 2,4:1 op de donkere footer (Klaviyo-tag zonder kleur) | `partials/footer.html`; testtag `research/tailoring/test/kltags.py` nu zonder kleur zoals Klaviyo; preview in `build_template.py` | `{% unsubscribe 'Unsubscribe' %}` / `{% web_view 'View in browser' %}` -> `<a href="{% unsubscribe_link %}" style="color:#BDB8B0;">Unsubscribe</a>` / `<a href="{% web_view_link %}" style="color:#BDB8B0;">View in browser</a>` (7,5:1) | idem | ja, 186/186 + template-render |
| 3 | Headerlogo 2,8 tot 3,0:1 in geforceerde donkere modus (Gmail-app, Outlook) | nieuwe kopieën `brand/logo/lockup/siraat-lockup-black-email-on-cream.png` (lockup geplat op #F8F7F2) en `siraat-lockup-white-email-on-dark.png` (geplat op #282828), byte-gelijk in `partials/shared/logo-black-cream.png` / `logo-white-dark.png`; `header.html`, `footer.html` | `{{IMG}}/logo-black.png` (transparant) -> `{{SHARED}}/logo-black-cream.png`; footer idem met `logo-white-dark.png` (advies 1 uit research/deliverability/01-inbox-check.md). Originele lockups niet aangeraakt; `mail_checks.py` herkent de kopieën als lockup (md5) | idem + 2 beelden in de Klaviyo-bibliotheek | ja: qa_inbox geen logo-FOUT meer; CDN-bestanden md5-gelijk aan de kopieën |
| 4 | "cm" in US-mails | `scripts/v5lib.py` (XITEM lid20..lid30), `post-purchase/p1-first, p1-repeat, p2, p2-safe, p3-pan, p3-pan-nocode`, `partials/blocks/about.html` + generator `scripts/make_product_blocks.py`; testverwachting `run_tests.sh` | "Stainless Steel Lid, 28 cm" -> "Stainless Steel Lid, {{SIZE:28}}" (US 11″, UK 28 cm); "Your 11″ Pan Pro takes the 28 cm lid" -> "...the 11″ lid"; "Add the 28 cm lid" -> "Add the {{SIZE:28}} lid"; "20, 26, 28 or 30 cm" -> `{{SIZE:..}}` per maat (ook "Match the diameter: Mini ..."); niet-US-takken ongewijzigd | idem | ja (qa_inbox US: geen cm meer, behalve een letterlijke review in w4-int, die alleen naar INT gaat; template-render r1-pan US: "Stainless Steel Lid, 11″") |
| 5 | Grijze noot 2,8:1 ("Light Labs report no. 25895", "Preheat on medium...") in c1, w1-a, w1-b, r1-acc, b2-notclicked | `partials/blocks/compare.html` (noot), plus dezelfde noot in `checkout/c2.html` | #9A948B -> #6E6A63 (5,0:1 op crème, 5,4:1 op wit) | idem | ja (qa_inbox: geen contrastmelding meer) |
| 6 | Preview "Already applied. On {day} morning, we remove it." in CODE · B2-CLICKED · pan en · acc | `browse/b2-clicked.html` (topcomment PREVIEW en verborgen preheader) | -> "Already applied. In 48 hours we remove it." | preview_text van acties 119850706, 119850708 (WdRz5k) en 119881743, 119881747, 119881751 (WNQjm9) | ja; scan van alle 220 berichten: verder geen `{ } [ ]`/VRAAG/placeholder |
| 7 | Klik-split na B1 (119850697, WdRz5k) zocht Campaign Name "B1 · T05a", maar de A/B-berichten heten "B1 Test #1 October 08, 2026 Variation A/B": niemand kreeg B2-CLICKED | `scripts/build_flows.py` (klik-split) | metric_filter Campaign Name contains "B1 · T05a" -> `$flow equals WdRz5k` (Clicked Email, > 0, sinds flowstart). Bot Click = false kan niet via de API: Klaviyo accepteert maar één metric_filter per voorwaarde (twee filters geeft 400 "invalid field type") | 119850697 (WdRz5k, Draft) en TEST-kopie 119881726 + 119881727 (WNQjm9, `$flow equals WNQjm9`) | ja (GET na PATCH). Bot Click: UI-stap Floris |
| 8 | (W1 in welcome, alleen rapportage) variaties heten "W1 Test #1 October 08, 2026 Variation A/B" | geen | geen split hangt ervan af | niets gewijzigd | n.v.t. |
| 9 | Codebalk W1 (beide varianten) toonde "YOUR WELCOME 10%%" | `welcome/w1-a.html`, `w1-b.html` (tikfout in de bron, geen escaping in build_template/v5lib); nieuwe blokkade in `export_klaviyo.py` check(): "%%" buiten Klaviyo-tags | "10%%" -> "10%" | templates Wuunna, VwWimX; acties 119850656/57/58 (T4a5Mk) en 119881617/19 (VHtuLj) opnieuw gekoppeld | ja: 0 van 61 mails met "%%" (dry-run en *.klaviyo.html), 0 van 186 kopieën; template-render w1-b: "YOUR WELCOME 10%" |
| 10 | E-bookknop P1 ging naar /products/e (productpagina), niet naar de download | `post-purchase/p1-first.html`, `p1-repeat.html` (hero en knoppen, 3 links per mail) | `https://siraatskitchen.com/products/e?utm_...` -> `https://delivery.shopifyapps.com/-/b3a2da5476fdac80/509b1c473bc15d58` (zonder UTM, besluit Floris). **Handmatig te controleren**: de proxy blokkeert deze host; `mail_checks.py` meldt hem als "handmatig te controleren" in plaats van FOUT | p1-first, p1-repeat in X3ySuU en Vjgd99 | ja (HTML van de kopieën, template-render p1-first) ; link zelf: handmatig |
| 11 | Verzendregel ontbrak in P1 (11-overstapplan 3.2) | `p1-first.html` (blok "When to expect it" vervangt "We pack and check it"; trackingregel aangevuld), `p1-repeat.html` (in de trackingstrook) | US: "Your order ships within 1 business day. Delivery then takes 6 to 10 days." INT: "...6 to 10 days in most countries, 8 to 14 to Ireland and Denmark." Tracking: "It lands in your inbox the moment your order ships. The first tracking update can take 24 to 72 hours to show." Verzendkosten via bestaande `{{SHIP}}` | idem | ja (template-render p1-first US: "ships within 1 business day") |
| 12 | Mails keren om in donkere modus (Gmail-apps, Android-webviews): bron meldt alleen `light` (13-darkmode.md, stap 1) | `scripts/build_template.py` (functie `light_only`, Klaviyo-versie en preview); QA: `scripts/qa_mail_shots.js` (modus `forced` haalt de color-scheme-verklaring weg en blijft echte inversie tonen, nieuwe modus `apple` = auto-dark die de verklaring volgt), `scripts/qa_inbox.py` (`apple` in de weergaven) | `<meta name="color-scheme" content="light">` en `supported-color-schemes` -> `light only`, plus `<style>:root{color-scheme:light only;supported-color-schemes:light only;}</style>`. Geen gradient-truc, geen Outlook-regels (stap 2 na een echte testmail) | **Nog niet**: `export_klaviyo.py --live --update` geweigerd door de permissiecontrole (productie-deploy); herkoppelscript klaar in scratchpad `dm/kl/relink.py` (186 v4-acties, 34 'Old ·' overgeslagen), controle `dm/kl/verify.py` | lokaal ja: qa_render 61/61 groen, dry-run 61/61 met `light only` (diff alleen de meta's en het :root-blok), lichte modus c1, w1-a, p1-first byte-gelijk vóór/na; qa_inbox: `apple` licht, `forced` omgekeerd |
| 13 | H2 (09-monitor): lege cross-sell (kop zonder producten) in N1, R1, P3-PAN, V1, R2-VIP en geen ONE SIZE NOTE in P1, bij een profiel zonder `siraat_owned` (vóór de nachtelijke sync) | `scripts/v5lib.py` (xsell), `post-purchase/p1-first, p1-repeat, p2, p2-safe`, `checkout/c2-acc, c3-acc`, `cart/k1-acc, k2-returning`; test: `research/tailoring/test/kltags.py` (lookup geeft bij een ontbrekende property nu een "ontbrekend"-waarde zoals Klaviyo: `in`/`not in` onwaar), `v5checks.py` (`xsell_empty`, `lid_missing`), `qa_render.py` (profiel zonder siraat_* verplicht, FOUT bij lege cross-sell of ontbrekende dekselregel), `run_tests.sh` (allowlist-check alleen top-level defs) | `person\|lookup:'siraat_owned'` -> `person\|lookup:'siraat_owned'\|default:''` (ook `siraat_owned_cats`; `siraat_orders` -> `\|default:0`). Test faalde eerst op 25 mails (lege kop, P1/P1-repeat/P2-safe zonder dekselregel), na de fix 0 | **bron klaar, export wacht op akkoord** | ja: qa_render 61/61, run_tests 0 FOUT |
| 14 | H3: code breekt op mobiel over twee regels (P3, V1, R2-VIP, C4, K3) | `partials/blocks/_style.css`, `blocks/offer.html` (class `offer-wrap`), `blocks/codebar.html` (class `cb-code`) | mobiel (<=480 px) 26px/4px -> 22px/2px, `white-space:nowrap`, binnenmarge 26 -> 8 px; <=360 px 20px/1,5px; codebalk-code nowrap. Bewust niet in het 620-blok: de ruwe Klaviyo-weergave op 600 px moet de lange coupon_code-tag kunnen breken | **bron klaar, export wacht op akkoord** | ja: Playwright 320 en 375 px, 12 mails met codeblok, CART-XXXXXXXX (13 tekens) overal op één regel binnen beeld (ook CART-WWWWWWWW). Los punt: C4 heeft op 320 px 13 px overflow door het cart-blok (productregel), niet door de code |
| 15 | M1: V2 P.S. noemt HI10 vlak na de eigen 15% | `vip/v2.html` (P.S.-tak zonder last_flow_code_pool en topcomment) | "HI10 still takes an extra 10% off your next order, and every order comes with four gifts." -> "Every order still comes with four gifts, on us." (tak met SK_REGULARS15_14D verwijst nog steeds naar de eigen 15%) | **bron klaar, export wacht op akkoord** | ja (render v2: geen HI10) |
| 16 | M3: P3-PAN "Add the lid, 10% off" opent de dekselpagina zonder variant | `post-purchase/p3-pan.html` (hero, 2 knoppen, offer: 4 links), `p3-pan-nocode.html` (3 links) | `/products/stainless-steel-lid` -> `...?variant=` per pan uit de order: Standard 52401107239252, Large 52401107272020, Small 52401107206484, Mini 53294486421844, crêpe 28 cm; anders zonder variant (id's uit content/catalog/products.json, gelijk aan LIDVAR) | **bron klaar, export wacht op akkoord** | ja (render per pan: juiste variant, UTM blijft gecodeerd binnen redirect) |
| 17 | M5: W2 P.S. "our The Green Clean E-Guide" | `welcome/w2.html` | "our The Green Clean E-Guide" -> "The Green Clean E-Guide" | **bron klaar, export wacht op akkoord** | ja |
| 18 | K3-onderwerp "We're removing your cart's 10%" (besluit: "your discount") | `cart/k3.html` (topcomment SUBJECT_A en offer-onderwerp), `klaviyo/figma/v5/meta.json` | -> "We're removing your discount" (28 tekens) | **bron klaar, export wacht op akkoord** (onderwerp van het flowbericht in Klaviyo bij export mee bijwerken) | ja (bron) |

| 19 | **Inbox-preview toonde bodytekst** (Floris 9 okt, Gmail iPhone): na onderwerp en preheader ook "THE WEEKEND PAN · A RECIPE FROM BENJAMIN Siraat COOKWARE SETS ABOUT From Benjamin's pan: ...". Oorzaak: opvulling na de preheader was 8 keer `&nbsp;&zwnj;` (zie 06-snelheid 2d). Had: **62 van de 63 mails** (alle 61 flowmails + recept-01-steak US; recept-01-steak-int had al 200 trio's) | `scripts/build_template.py` (functie `preheader_fix`, geldt voor elke bron: vervangt de verborgen div direct na `<body>` door één vaste div, stijl `display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;color:transparent;`, preview-tekst + 200 keer `&#847;&zwnj;&nbsp;`; geen of lege preheader = bouwfout). Bronnen zelf niet gewijzigd. `export_klaviyo.py` (preheader-regex stopt ook bij `&#847;`), `research/tailoring/test/expand.py` opnieuw afgeleid (mkexpand.py), testfixture `research/tailoring/test/v5/demo.html` kreeg een preheader | 8 -> 200 opvulparen (+3,6 KB per mail; grootste mail p3-pan 87,4 KB, ruim onder 102 KB). Alle andere tekst (topbalk, logo-alt "Siraat", nav) staat in documentvolgorde ná de opvulling | **nog niets in Klaviyo: export wacht op akkoord Floris.** Bij export: 61 bibliotheektemplates (`--live --i-am-sure --update`) en opnieuw koppelen in de flows (fix 5), plus campagnetemplate recept-01 INT (US is al verstuurd) | ja: nieuwe QA-check (zie onder), 63/63 groen |

Controle na 13 tot 18: `qa_render.py` (met browser) 61/61 groen; alle 61 gebouwde mails: `light only` (meta en :root), ABOUT naar /pages/about-us, footerlinks #BDB8B0, geen "%%", geen em dash. Niets naar Klaviyo geëxporteerd.


**Nieuwe QA-check inbox-preview (fix 19).** `scripts/mail_checks.py`: `inbox_preview()` leest de mail zoals een inbox-preview (tekstnodes in documentvolgorde vanaf `<body>`, ook verborgen, alt-teksten als tekst, commentaar/head/style weg, witruimte samengevoegd; zero-width tekens `U+034F U+200C U+200B U+200D U+2060 U+FEFF U+00AD` tellen als lege positie, `&nbsp;` en figure space niet omdat clients witruimte samenvoegen). `preview_problems()` geeft FOUT bij geen of lege preheader, tekst vóór de preheader, of minder dan 300 lege posities tussen preheader en de eerste andere tekst. Zit in de `preheader`-controle van `mail_checks.run_checks` (dus ook `qa_inbox.py mail` op echte testmails) en in `qa_render.py` (punt h: ruw, per gerenderde variant en per markt US/UK/AU/CA/SG/EU/onbekend). Op de oude builds reproduceert de check precies de melding van Floris (8 lege posities, daarna "THE WEEKEND PAN · A RECIPE FROM BENJAMIN Siraat COOKWARE SETS ABOUT From Benjamin's pan: s..."). `qa_render.py` neemt nu ook `klaviyo/templates/campaigns/*.html` mee (flow `campaigns`, geen event); receptcampagnes vallen onder de lengte-uitzondering (geen verkoopmail, 4.830 px). Uitkomst 9 okt: `qa_render.py` (met browser) **63 mails, 63 groen, 0 FOUT**; `run_tests.sh` 0 FOUT (v5-bouwstenen 3294 ok); `check_previews.py` 0; `export_klaviyo.py` dry-run 61/61 klaar. Alle `.klaviyo.html` herbouwd en de preheader in de `-preview.html`-bestanden vervangen.

**Na de export nog doen (testronde).** Eén testmail per type naar Gmail iPhone en `python3 -I scripts/qa_inbox.py mail <bericht>`: de check vangt nu ook het geval dat Klaviyo de `preview_text` van het flowbericht als eigen verborgen div vóór de onze zet (dan "tekst vóór/na de preheader" als FOUT). Gebeurt dat, `preview_text` in de flowberichten leegmaken (06-snelheid 2d).

## UI-stappen voor Floris (kan niet via de API)

1. **Bot Click in de browse-klik-splits.** Flows > *v4 · Browse abandonment* > in de kookgerei-tak de conditional split direct na "Wait 2 days" (na B1) > in de voorwaarde *Clicked Email* (staat nu op "Flow equals v4 · Browse abandonment", at least once, since starting this flow) op het filtericoon > *Add filter* > *Bot Click* > *is false* > Save. Daarna dezelfde stap bij de split na B1-ACC (voorwaarde Campaign Name contains "B1-ACC"). Herhaal beide in *TEST v5 · Browse abandonment* (twee B1-splits, een per A/B-tak, en de B1-ACC-split). Daarna met een testprofiel op B1 klikken en nalopen dat B2-CLICKED komt.
2. **W1-rapportage**: niets nodig voor de werking. Voor rapporten op naam eventueel de twee variaties in *v4 · Welcome* hernoemen naar "W1 · T04-A" / "W1 · T04-B" (en in browse "B1 · T05a-A/B"); `scripts/test_report.py` zoekt anders niets.
3. **E-booklink** één keer met de hand openen in een testmail (de omgeving kan delivery.shopifyapps.com niet bereiken).

## Niet zelf besloten (voor Floris)

- **"Finish my order"** in k1, k1-acc, k2-new, k2-returning en k3-nocode gaat naar de productpagina (`event.URL`), niet naar de cart. Keuze: knoptekst aanpassen (bijv. "Back to my pan") of cart-permalink `/cart/{{ event.VariantID }}:{{ event.Quantity }}` (vervangt wel de bestaande cart door dat ene product). Zie 05-links.md.
- **Compare-at $288** (Pan Pro Standard, `{{WAS:standard}}` uit de catalogus) staat niet in DECISIONS als bevestigd anker (daar staat $439 bij $134); bevestigen of niet tonen.
- **Warranty-pagina** zegt "lifetime warranty", mails en DECISIONS zeggen 75 jaar (ook /pages/about-us: "made to last a lifetime"). Pagina aanpassen of k2-new naar /policies/refund-policy laten linken.

## Fix: storebot-filter op checkoutflow (10 okt 2026, akkoord Floris)
- Probleem: circa 22 van 90 checkouts per dag komen van Google Merchant Center testbots (adressen op storebotmail.joonix.net). Die kregen checkoutmails en bouncten: C1 34% bounce.
- Oplossing: op alle 14 mails van QUBUQV (C1 t/m C4, Old Checkout 1 t/m 5, ACC-varianten) een extra filtergroep: profieleigenschap email bevat niet "storebotmail.joonix.net".
- Controle: diff voor/na toont alleen die extra groep; trigger, profielfilter, splits en delays ongewijzigd. Flow blijft live.
- Bewust niet gefilterd: verdachte $19-checkouts met generieke namen, want die kunnen echt zijn.
- Nacontrole: na 24 uur mogen er geen Received Email events meer zijn naar storebot-adressen uit QUBUQV.

## Fix: K1 v2 live (10 okt 2026, akkoord Floris na testmail T2)
- Flow TZG9Mx, actie 119850627 (K1, message Vb6YFp): template UQkhFj vervangen door k1-v2 (bron klaviyo/templates/v3/cart/k1-v2.html, Klaviyo-kopie RXNZa3, los template XY7Gi7).
- Inhoud: hero, productkaart en knoppen naar /cart (hele winkelwagen, gift-app), knop "Return to my cart", restore-link naar /cart/VariantID:Qty?storefront=true, grote productkaart met compare-at uit het event (= Shopify-catalogus), RVS-zin en RVS-vergelijking weg, closer look weg.
- Controle: rest van de actie (onderwerp, preview, filters, afzender) ongewijzigd, flow live, render zonder restanten.
- Let op: de A/B oud tegen nieuw in de cartflow meet vanaf nu de nieuwe K1. Telling voor K1 opnieuw starten vanaf 10 okt 14:15 UTC.
- Nog open: Floris test of de restore-link de 4 gifts toevoegt.

## Uitrol: browse, cart en checkout naar 90% nieuw (12 okt 2026 ca. 09:50 UTC, akkoord Floris)
- Splits (profile-sample) van 50 naar 90 naar de nieuwe arm: browse 119850685 (WdRz5k), cart 119850622 (TZG9Mx), checkout 119850583 (QUBUQV). Welcome blijft 50/50. T02-codesplits (50/50) ongewijzigd.
- Controle: per actie alleen het percentage veranderd, flows live. Snapshots scratchpad/golive/<flow>-voor-9010.json.
- Terugdraaien: percentage terug naar 50 (of 0 voor 100% oud) op dezelfde drie acties.
- Bewaking: dagelijkse routine "Siraat 90/10 bewaking" (trig_01Tjvd8TSPX99Xt8VFTWNgNS) om 09:46 NL, alarm in #claude-mail alleen bij problemen.

## Review-hero korter live (12 okt 2026, expliciet akkoord Floris)
- XzHrez: de drie berichten in de A/B (acties 119577631, 119577632, 119577635) gekoppeld aan r1-short (bibliotheek W3XpNR; flow-kopieen X3aHU9, Va7A4g, SE3pzL). Was UxfsuQ, SVpzGN, WTnCid.
- Werkwijze: PATCH per variatie-actie werkt; PATCH op de ab-test-actie zelf wordt geweigerd zolang de test loopt.
- Controle: onderwerpen ongewijzigd, A/B-test live (50/50), flow live, render zonder restanten, Trustpilot-link aanwezig, preview en bg 0, beelden gelijk aan de bron.
- 12 okt, vervolg: header weg op verzoek Floris, witte logo-lockup in de hero (Klaviyo-beeld 382456929). Bibliotheek RFcjsS, flow-kopieen R4bgQf, RAz57u, Y9fywM op acties 119577631/632/635. Onderwerpen gelijk, A/B live, render zonder restanten, preview en bg 0. Screenshot img/19-review-zonder-header-375.jpg.

## W1 v3 als variant B live (15 okt 2026 ca. 00:33 UTC, expliciet akkoord Floris)
- Flow T4a5Mk (v4 · Welcome), W1-test 119850659, variant B = actie 119850658. Template RgF2K5 vervangen door W1 v3 (bron klaviyo/templates/v3/welcome/w1-v3.html, bibliotheek RGgUs4, flow-kopie X5yyXv).
- Onderwerp B: "{{ first_name|default:'Hi' }}, here's your 10%". Preview B: "Welcome to Siraat. HI10 takes 10% off on top of the sale." Variant A ongewijzigd.
- Controle: alleen subject_line, preview_text en template_id van B anders (ook gespiegeld in de ab-test-actie), A/B live 50/50, flow live, render zonder restanten. Snapshots scratchpad/golive/t4a5mk-acties-voor.json en -na.json.
- Meting: telling vanaf nu. Hoofdmaat alle orders per ontvanger binnen 5 dagen na W1, daarnaast open, klik, uitschrijvingen. Looptijd tot ca. 29 okt.
- Terugdraaien: template_id RgF2K5, onderwerp "No PFAS. Here's the paper. And 10%." en de oude preview terug op actie 119850658.
- Afzendernaam blijft "Siraat's Kitchen" in A en B (later voor alle mails tegelijk).

## Footer-links zwart (19 okt 2026 ca. 17:50 UTC, keuze en akkoord Floris: variant E)
- Unsubscribe, Manage preferences en View in browser in de vaste footer van #BDB8B0 naar #111111 (contrast 1,3:1 op #282828). Advies was B (#8C8780); Floris koos E.
- Repo: klaviyo/templates/partials/footer.html aangepast.
- Klaviyo: 89 flowmails in 15 live flows (alle v4-flows plus Review request) via bibliotheek-kopie en PATCH flow-action template_id. Elke mail gecontroleerd: oude kleur weg, 3x #111111, status ongewijzigd. A/B-tests W1 en browse blijven live met de nieuwe templates. Oude EB-flows en Old-armen hebben een andere footer en zijn niet aangeraakt.
- Mapping oud naar nieuw template per actie: research/footer-links/footer-applied-*.json. Oude HTML: scratchpad golive/footer-backup/.
- Terugdraaien: per actie template_id terugzetten naar de oude id (via bibliotheek-kopie van de backup-HTML, zelfde script scratchpad golive/footer_apply.py met kleur omgedraaid).
- Risico (gemeld): afmeldlink nauwelijks zichtbaar; CAN-SPAM vraagt "clear and conspicuous". Klaviyo stuurt wel de List-Unsubscribe-header mee (één-klik afmelden in Gmail/Yahoo). Spamklachten de komende week volgen in de 90/10-bewaking.

## Browse Triple Pixel concept (19 okt)

Status: **concept**. Flow en alle mails staan op Draft; niets verstuurd, niets gepland. Livegang alleen na expliciet akkoord van Floris.

**Waarom.** Bij de livegang (9 okt) gingen Wj6x6V (Viewed Product, XNtYMB) en TyEjuQ "EB | DEC 25 | Browse Abandonment | Triple Pixel" (Viewed Product - Triple Pixel, V48nhq) naar Draft. TyEjuQ haalde ~$6.000 in 11 dagen. WdRz5k (v4 · Browse abandonment) start alleen op XNtYMB, dus bezoekers die alleen het Triple Pixel-event geven krijgen sindsdien geen browsemail.

**Oude TyEjuQ (GET).** Trigger V48nhq zonder triggerfilter. Flowfilters: Checkout Started 0, Placed Order 0, Added to Cart 0 sinds flowstart, niet in deze flow in 30 dagen, e-mail bevat niet test@example.com. Herinstap 2 dagen. 50/50-split: 10 min of 30 min wachten, dan één mail "Hi {first_name}, we saw you looking..." (beide mails nu draft).

**Volume (metric-aggregates, 12 t/m 18 okt, UTC).** V48nhq gemiddeld ~2.350 events en ~960 unieke profielen per dag; XNtYMB ~2.360 events en ~1.190 unieke profielen. Op 18 okt: 1.072 TP-profielen, waarvan **191 zonder Shopify Viewed Product** (17 tot 19 okt), alle 191 met e-mail, 163 mogen marketing ontvangen. WdRz5k verstuurde 282 tot 545 mails per dag (~0,32 mail per uniek viewer). Verwachting nieuwe flow: **ongeveer 40 tot 70 mails per dag** (B1 plus B2), vooral B1.

**Nieuwe flow QNZyEb "v4 · Browse abandonment · Triple Pixel"** (POST /api/flows, revision 2025-10-15; snapshot `research/v6-golive/browse-tp-concept.json`).
- Trigger: metric V48nhq (Viewed Product - Triple Pixel), geen triggerfilter (zoals WdRz5k).
- Flowfilters: gelijk aan WdRz5k (Added to Cart, Checkout Started, Placed Order 0 sinds flowstart; Received Email uit TZG9Mx, QUBUQV en T4a5Mk 0 in 7 dagen; niet in deze flow in 7 dagen), plus **Received Email waar $flow = WdRz5k 0 keer in de laatste 7 dagen** (dedupe), plus **Viewed Product (XNtYMB) 0 keer in de laatste 1 dag**. Die laatste staat niet in WdRz5k maar wel in het plan (11-overstapplan sectie 7): beide flows wachten 1 uur, dus zonder dit filter kunnen ze B1 in dezelfde minuut sturen voordat de Received Email-dedupe iets ziet. Weg te halen in de UI als Floris dat niet wil.
- Herinstap 7 dagen (zoals WdRz5k).
- Opbouw: alleen de nieuwe arm van WdRz5k (vanaf actie 119850686), zonder oude arm en zonder 90/10-split 119850685. Wacht 1 uur > categoriesplit (nu op V48nhq, Name bevat Hammer/Pan/Pot/ookware/Everything/fanne/Prep Bundle in 1 dag) > kookgerei: TP · B1 / anders: TP · B1-ACC > wacht 2 dagen tot 09:00 > kliksplit (met Bot Click = false) > cooldown-split (Received Email Campaign Name bevat "CODE ·" in 30 dagen, gedeeld met alle v4-flows) > 50/50 T02 code of geen code, of B2-NOTCLICKED.
- A/B-test B1 (119850693) niet nagebouwd: TP · B1 = variant A ("Get this pan with 10% off", template R6E5Zv).
- Berichtnamen met "TP · " ervoor; utm_campaign per bericht `v4-browse-tp` (was `v4-browse`). De UTM's in de template-links zelf blijven `v4-browse` (zelfde template).
- B1-ACC-kliksplit zoekt nu Campaign Name bevat "TP · B1-ACC" (anders zou een klik op de B1-ACC uit WdRz5k meetellen).

| Actie | Bericht | Template (kopie) | Bron in WdRz5k |
|---|---|---|---|
| 121177227 | TP · B1 | WchdbC | 119850691 / R6E5Zv |
| 121177228 | TP · B1-ACC | TLQh4w | 119850694 / VTwW7c |
| 121177242 | TP · B2-NOTCLICKED | TGd2H8 | 119850700 / VyZUHC |
| 121177244 | TP · B2-CLICKED · pan nocode · cooldown | WE3K7t | 119850702 / RDD8j6 |
| 121177250 | TP · CODE · B2-CLICKED · pan | WzquL5 | 119850706 / XRNAkP |
| 121177251 | TP · B2-CLICKED · pan nocode · T02-B | VWps9s | 119850707 / SGpGH3 |
| 121177247 | TP · B2-CLICKED · acc nocode · cooldown | XPszZj | 119850704 / TgNv8M |
| 121177252 | TP · CODE · B2-CLICKED · acc | STVtpH | 119850708 / YcURLK |
| 121177258 | TP · B2-CLICKED · acc nocode · T02-B | X3b2FU | 119850709 / UZcnke |

**Controles (GET na aanmaken).**
- Flow status draft, 9 mails status draft, trigger V48nhq, 9 flowfilters zoals hierboven, entry 121177225 (wacht 1 uur).
- Alle 9 templatekopieën byte-gelijk aan de huidige templates van WdRz5k. In elke mail: header-lockup en footer-lockup (CDN), footer #282828, 3 footerlinks #111111 (Unsubscribe, Manage preferences, View in browser), ABOUT naar /pages/about-us, geen em dash. #BDB8B0 komt alleen nog voor in tagline en claimsregel (geen link).
- `POST /api/template-render` met een TP-achtig event (Name, URL, ImageURL, Price): 7 van 9 renderen zonder restanten `{{`/`{%`, productnaam staat erin, 3x #111111. De 2 CODE-mails geven "customer profile is required" (coupon_code-tag); de live CODE-template XRNAkP in WdRz5k geeft precies dezelfde melding, dus geen afwijking.
- Het TP-event heeft dezelfde vorm als het klaviyo.js-event: Name, URL, ImageURL, Price, CompareAtPrice, ProductID, Categories (200 recente events).

**Open punt vóór livegang (verplicht).** De kliksplit na TP · B1 (actie **121177235**) zoekt nog Clicked Email waar **$flow = WdRz5k**; dat moet **QNZyEb** zijn. `PATCH /api/flow-actions/121177235` is geweigerd door de permissiecontrole van deze sessie. Zonder fix gaat vrijwel iedereen in de kookgerei-tak naar B2-NOTCLICKED (dedupe sluit WdRz5k-mails uit). UI: Flows > *v4 · Browse abandonment · Triple Pixel* > kookgerei-tak, conditional split na "Wait 2 days" > voorwaarde *Clicked Email* > filter *Flow equals* > kies *v4 · Browse abandonment · Triple Pixel* > Save.

**Spiegelfilter voor WdRz5k (voorstel, NIET toegepast).** Flowfilter toevoegen op WdRz5k: *Received Email where Flow equals v4 · Browse abandonment · Triple Pixel (QNZyEb) zero times in the last 7 days*. API-vorm: `{"type":"profile-metric","metric_id":"YkRM4Q","measurement":"count","measurement_filter":{"type":"numeric","operator":"equals","value":0},"timeframe_filter":{"type":"date","operator":"in-the-last","unit":"day","quantity":7},"metric_filters":[{"property":"$flow","filter":{"type":"string","operator":"equals","value":"QNZyEb"}}]}` als nieuwe conditiegroep. Alleen tegelijk met de livegang van QNZyEb; WdRz5k is live, dus wijzigen vraagt akkoord Floris. Let op: een flowfilter op een live flow geldt ook voor wie er al in zit.

**Inhaalsegment SffqDu "TP browse gemist sinds 9 okt"** (alleen segment, geen campagne). V48nhq meer dan 0 keer na 2026-10-08T22:29Z, Placed Order 0 keer sindsdien, Received Email uit WdRz5k 0 keer sindsdien, mag e-mailmarketing ontvangen. Grootte na verwerking (19 okt 18:03 UTC): **2.788 profielen**. Bevat ook mensen die om andere redenen geen browsemail kregen (cart- of checkoutmail, eerder in WdRz5k); voor een inhaalcampagne eventueel nog Added to Cart en Checkout Started sinds 9 okt uitsluiten.

**Livegang (na akkoord Floris).**
1. Kliksplit 121177235 naar $flow = QNZyEb (UI-stap hierboven).
2. Eventueel: triggerfilter tegen gratis producten (Name bevat niet Giveaway, E-Guide, E-Book, Mystery Gift; 02-segmenten-foutenjacht bevinding 14). Komt in TP-events zelden voor (1 E-Guide in 200).
3. Alle 9 mails op Live: in de UI per mailkaart *Status* > *Live*, of via API `PATCH /api/flow-actions/{id}` met status live voor 121177227, 121177228, 121177242, 121177244, 121177250, 121177251, 121177247, 121177252, 121177258.
4. Flow op Live: statusmenu rechtsboven > *Live*, of `PATCH /api/flows/QNZyEb` met `status: live`.
5. Dezelfde minuut: spiegelfilter op WdRz5k (zie boven).
6. Na 1 uur en 24 uur: Received Email per $flow QNZyEb (verwacht 40 tot 70 per dag), geen profiel met mail uit WdRz5k én QNZyEb binnen 7 dagen, uitschrijving en bounce in de 90/10-bewaking meenemen.

**Terugdraaien.** QNZyEb op Draft (statusmenu of `PATCH /api/flows/QNZyEb` status draft); lopende profielen krijgen dan niets meer. Spiegelfilter van WdRz5k weer weghalen. Niet archiveren (PLAYBOOK 7). TyEjuQ niet terugzetten (verouderde claims).

### Livegang Browse Triple Pixel v3 en 100% nieuw (19 okt 2026, akkoord Floris "ja zet maar live")

- QNZyEb: 9 berichten op de v3-templates gezet (library-template + flow-action PATCH, mapping in `tp-v3-applied.json`; oude kopieën WchdbC, TLQh4w, TGd2H8, WE3K7t, XPszZj, VWps9s, X3b2FU, WzquL5, STVtpH blijven bestaan voor rollback). Onderwerp A uit browse-tp-v3.md sectie 3; B2-NOTCLICKED nu "Why we can cover this pan for 75 years". Preheaders uit dezelfde tabel.
- Kliksplit 121177235: Clicked Email $flow = WdRz5k vervangen door QNZyEb.
- 9 berichten live, flow QNZyEb live. Controle: header- en footerlockup, 3x #111111, geen em dash, render op TP-event zonder restanten (CODE-mails: bekende melding "customer profile is required", zelfde als live XRNAkP).
- Spiegeldedupe op WdRz5k: een flowfilter kan niet via de API (PLAYBOOK: geen definition in PATCH /api/flows). Daarom als berichtfilter "Received Email where $flow = QNZyEb 0 keer in 7 dagen" op alle 11 mails van de nieuwe arm (B1 hoofd + variant A en B, B1-ACC, alle B2/CODE). A/B-test 119850693 bleef live, zelfde experiment-id.
- Splits naar 100% nieuw: browse 119850685 en checkout 119850583 van 90 naar 100. Oude armen krijgen niemand meer, blijven staan voor rollback (terug naar 90).
- Backups van elke actie vóór de wijziging: scratchpad `tp/backup/`.
