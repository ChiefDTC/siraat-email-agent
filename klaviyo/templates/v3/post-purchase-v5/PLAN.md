# PP v5 · Post-purchase + delivery (DRAFT, 19 nov 2026)

Opdracht Floris: post-purchase en levering samen in één reeks, veel beter design (niveau BF-W1 B / welcome v6d), met de getailorde viewed-product upsell (UUZr3e / YyGsj3) erin. **Alles draft: niets live, geen testmails, X3ySuU, VQ93sx, UUZr3e, R9dcdY en hun templates ongewijzigd.**

| Wat | ID |
|---|---|
| Flow (draft) | **Ukz7F9** "v5 · Post-purchase + delivery (draft)", trigger Placed Order, alle 9 mails op draft (vervangt de eerste draft SqSdTv, verwijderd 19 nov avond: upsell naar +5 min) |
| Templates (bibliotheek) | PP1 first UYYaHy · PP1 repeat WanZBq · PP2 upsell T7V2RF · PP3 delivered WGLMSD · PP3 safe XfaA9S · PP4 CODE UcGBq9 · PP4 nocode SWEwaT (namen "PP v5 · ... · TEST") |
| Flowkopieën (Klaviyo kloont bij koppelen) | PP2 T6x2rT, PP1 VrkGdB / RdtSA2, PP3 VXJuuQ / X99jnG, PP4 nocode VT7e9s, CODE X4w53i |
| Figma | rij 1m, node 381:106 (bijgewerkt 19 nov avond; rij 1l 376:106 hero-scenario's ook) (oaxnBkz3MAbePRnorCrQwz) |

## 1. Huidige staat (gelezen 19 nov, laatste 30 dagen, conversie RSNxYV)

**X3ySuU "v4 · Post-purchase"** (live, Placed Order, niet in flow 30 d): 1 uur > P1-FIRST / P1-REPEAT (filters op ordertelling) > 16 dagen 09:00 > P2-SAFE (pankoper, geen Delivered sinds start, geen VQ93sx/R9dcdY/P2-SAFE in 30 d) > 4 dagen > split herhaalorder = exit > split cooldown (CODE-mail in 30 d) > ja: nocode-keten / nee: 50/50 T02 (CODE tegen nocode T02-B) > lineaire keten van P3-SET, P3-NEXT deksel, P3-PAN, P3-ACCESSORY kook, P3-NEXT eigenaar, P3-APRON, P3-ACCESSORY acc (elk met eigen Items-filters).
**VQ93sx "levering"** (live, Delivered Shipment VcUF33): 1 dag 09:00 > P2 (chef-gids). Vangnet R9dcdY (Fulfilled +12 d).

| Mail | Ontvangers | Klik | Conversie | Omzet | $/ontv. | Uitschrijf |
|---|---|---|---|---|---|---|
| P1-FIRST | 11.287 | 7,61% | 0,46% | $8.619 | $0,77 | 0,36% |
| P1-REPEAT | 816 | 6,02% | 0,61% | $605 | $0,74 | 0,00% |
| P2-SAFE | 3.432 | 6,91% | 0,18% | $815 | $0,24 | 0,26% |
| P2 (VQ93sx) | 1.774 | 6,98% | 0,57% | $1.562 | $0,89 | 0,23% |
| CODE · P3-SET | 520 | 2,32% | 0,39% | $427 | $0,83 | 0,77% |
| P3-SET nocode T02-B | 553 | 2,74% | 0 | $0 | $0 | 0,36% |
| CODE · P3-PAN | 877 | 2,52% | 0,23% | $116 | $0,13 | 0,57% |
| P3-PAN nocode T02-B | 925 | 2,18% | 0,44% | $242 | $0,26 | 0,76% |
| P3-NEXT deksel (CODE / T02-B) | 164 / 178 | 1,8 / 2,8% | 0 | $0 | $0 | 0 / 0,56% |
| P3-ACCESSORY, P3-APRON, P3-NEXT eigenaar, cooldown-varianten | 1 tot 93 per mail | | | ~$0 | | tot 1,32% |

Lezing: P1 en P2 doen het werk, P3 is versnipperd over 16 mails met te weinig volume voor een T02-uitslag (P3-SET pleit voor de code, P3-PAN voor geen code). Er zit 3 weken gat tussen P1 en de eerste verkoopmail; de getailorde upsell vult dat gat op dag 2.

## 2. De nieuwe reeks (flow Ukz7F9, lineair, elke mail met eigen filters)

Wijziging 19 nov avond (Floris): de upsell komt **5 minuten na de bestelling**; de bevestiging PP1 blijft op 1 uur na de bestelling (55 minuten na de upsell), omdat Shopify zelf direct de orderbevestiging stuurt en PP1 vooral verwachting en tip geeft. Copy aangepast ("thanks for your order" in plaats van "your order is on its way"). Filter op PP2: geen andere VIP15-upsellmail in 1 dag (Campaign Name bevat VIP15, dekt ook UUZr3e). Ordered Product-splits/-filters op 12-Pcs/34-Pcs blijven (dekken Aftersell).

| # | Mail | Timing | Doel | Wie (filter/split) | Onderwerp | Preview |
|---|---|---|---|---|---|---|
| 2 | PP2-UPSELL · VIP15 | +5 min | Getailorde upsell: 12-Pcs (VS) / 6-Pcs (rest) bovenaan, max 3 bekeken producten, nooit iets in bezit | bekeek een aanbiedbaar product (30 d) of had nooit 12-Pcs/34-Pcs; geen VIP15-mail in 1 d; geen refund | A thank-you: 15% off, picked for you | Thanks for your order. Here is 15% off, once, until Monday, Nov 30. |
| 1 | PP1-FIRST | +1 uur | Bevestiging, verwachting, e-book, de ene tip | eerste order ooit, betaalde order | Good call. Here's what happens next. | Order confirmed. Your 5 free gifts, your e-book and the one tip that matters. |
| 1b | PP1-REPEAT | +1 uur | idem, herkenning | meer dan 1 order | Good to see you again | idem |
| 3 | PP3-DELIVERED | dag 8, 09:00 | Eerste gebruik: het ei, de chef-stappen, deksel in de juiste maat | Delivered Shipment sinds start, pankoper, geen VQ93sx/R9dcdY/P2-SAFE in 30 d | Your first egg, step by step | Medium on titanium works like high on a normal pan. The chef's five steps. |
| 3b | PP3-SAFE | dag 11, 09:00 | Vangnet als Delivered niet binnenkwam | nog geen "PP v5 · PP3"-mail, pankoper, zelfde dedupe | Before your first cook: the egg | Heat first, then oil, then the egg. Keep this for your first cook. |
| 4 | CODE · PP v5 · PP4 | dag 21, 09:00 | Cross-sell op wat ze kochten, 10% eigen code 14 dagen (P3_THANKYOU_10_14D) | geen CODE-mail in 30 d (cooldown-split), geen nieuwe order sinds start, geen refund | How is the pan treating you? | What owners add next, with your own 10% for 14 days. |
| 4b | PP4 nocode · cooldown | dag 21, 09:00 | idem zonder code | wel een CODE-mail in 30 d | How is the pan treating you? | What owners add next. 5 free gifts with every order. |

Onderwerpregels om te testen (één variabele): PP1 "Good call. Here's what happens next." tegen "Order confirmed. Here's the one tip." · PP2 "A thank-you: 15% off, picked for you" tegen "15% off, once, as a thank-you" (UUZr3e) · PP3 "Your first egg, step by step" tegen "The mistake that makes titanium stick" (VQ93sx) · PP4 "How is the pan treating you?" tegen "The lid in your pan's size".

**Splits die vervallen**: de 7 aparte P3-categoriemails worden één PP4-template dat zelf kiest (set-koper: Standard 11″ of Deep, plank of Wok, utensils of Crêpe; pankoper: deksel in maat of utensils, 6-Pcs of Deep, plank of Wok; accessoire/schort: Standard of Large, 6-Pcs of Deep, plank of utensils). Elk vak toont het alternatief als de klant de voorkeur al heeft (order, `ppv_vr_<key> == 9`, `siraat_owned`). De T02-test (code tegen geen code) is niet meegenomen: te weinig volume; terug te zetten met een profile-sample-split vóór PP4. De herhaalorder-exit van X3ySuU is vervangen door het filter "geen nieuwe order sinds start" op PP4.

## 3. Wat er in design veranderd is

- Opbouw zoals BF-W1 B: ontworpen beeldsecties (1200 breed) met live tekst, prijzen en knoppen ertussen; gescheurde randen tussen kleurvlakken (crème, zand, donker); één primaire knop per sectie; vaste header en footer uit `partials/`.
- PP1: armen-met-pannen-hero op brick, orderblok live, gifts flat-lay (5 free gifts, echte gift-beelden), tip-sectie met flash-foto en drie witte stapkaarten, "From order to first egg" met gouden cijfers, ontworpen reviewkaarten.
- PP2: dezelfde topkaart als BF-W1 B (12-Pcs $2,047 / $649 / **$551.65**, of 6-Pcs "15% OFF" buiten de VS), daaronder getinte productkaarten: bovenkant beeld (echte uitsnede met grondschaduw), onderkant live in dezelfde tint met naam, regel, prijs (VS) en knop. Dynamiek ongewijzigd uit YyGsj3 (`build_tailored.py`: CHAIN, owned_cond, HERO_OK).
- PP3: ei-foto als hero, donkere sectie "Cold metal grabs. Hot metal lets go." met de vijf chef-stappen, ei-GIF, "If something sticks"-kader, dekselkaart met de maat uit de order (11″ of 28 cm enz.).
- PP4: shoot-foto (flash-stijl) als hero, drie productkaarten, espresso codeblok met echte einddatum (vandaag + 14 dagen), reviewkaarten.
- Geen nagebakken schaduwwaas meer: uitsneden met harde, schone rand (alfa < 24 weg, > 232 vol) en een korte contactschaduw plus brede zachte schaduw (v6d `ground.py`). Bundels zonder eigen uitsnede (Complete Edition, Cookware Set Pro, Full Hammered Pro, 2 Pans + 2 Lids, 34-Pcs) zijn gelegd uit de echte uitsneden van precies hun stukken, elk stuk met eigen schaduw.

## 4. Beelden en Photoroom

**19 nov avond (Floris): harde schaduw en mooier aanzicht.** De Photoroom MCP kan geen harde schaduw op transparant (generate_ai-shadows heeft alleen een beeldinvoer, geen preset, en levert zacht op wit), dus zonder extra credits zelf gemaakt: `_tools/hardshadow.py` (per los onderdeel een zwarte, platgedrukte slagschaduw van het onderste deel van het silhouet, kleine verschuiving rechtsonder, blur ~2 px, dekking 52%, plus contactschaduw 70% langs de onderrand). Wok, Deep Pan en Crêpe nu in 3/4-aanzicht met gehamerde binnenkant (3 extra remove-background-generaties op uitsneden van Shopify-sfeerbeelden: wok-09, deep-pan-03 met ragù, crepe-pan-02 met crêpe; plaat weggefilterd, bruine kleurzweem van het decor eruit). Product 70 tot 80% van de kaartbreedte, kaart 680 hoog. Totaal Photoroom: 18 generaties. Kaarten opnieuw in de bibliotheek (`sections/hard2/klaviyo-urls.txt`). Vergelijking oud/nieuw: scratchpad `ppv5/vergelijking-oud-nieuw.jpg`. Upsell YyGsj3 (en flowkopieën RSxshv, SqVeyJ, VnKWX5 in UUZr3e) kreeg nieuwe hero's ppv-set12-hard / ppv-set6-hard; 12 van 12 scenario's opnieuw goed.


15 generaties `generate_remove-background` op de echte Shopify-productfoto's (Admin API, eerste media per product): 12-Pcs, 6-Pcs, Pan Pro Standard, Large, Small, Mini, Deep, Wok, Pizza Steel, Crêpe, Cutting Board, Utensil Set, Damascus messenset, Roasting Pan, Stainless Steel Lid. Alle 15 gelukt, 2000 px RGBA. GenerationId's in `gen/photoroom-generations.txt` (opnieuw downloaden met get_ai_tool_image_result, geen nieuwe credits). Geen ai-shadows gebruikt: de eigen grondschaduw is reproduceerbaar en past op de getinte kaart (ai-shadows zet een witte achtergrond). Sfeerbeelden hergebruikt: v6d `arms.png`, `flash-egg.png`, `egg.jpg`, gifts flat-lay, gescheurde randen; post-purchase `friends-greeting` en `egg-slide-lite.gif`. Higgsfield niet gebruikt. 35 secties in de Klaviyo-bibliotheek (`sections/klaviyo-urls.txt`).

## 5. Getest

- Klaviyo template-render API op de bibliotheektemplates: PP1 first/repeat, PP2 (VS Standard-koper die Wok en Deep bekeek: 12-Pcs + Wok + Deep; VS 12-Pcs-koper die Pizza Steel en messen bekeek: geen hero, Pizza Steel + messen; VK: 6-Pcs hero, alleen Wok), PP3 delivered (VS, 11″-deksel) en safe (VK, 28 cm), PP4 nocode (DE, plankkoper: Standard, 6-Pcs, utensils, geen bedragen). Geen restanten `{% %}`/`{{ }}`.
- PP4 CODE: de API weigert `coupon_code` zonder echt profiel; daarom lokaal met Django (`_tools/preview.py`): pankoper krijgt deksel, 6-Pcs, plank; 12-Pcs-koper Standard, plank, utensils.
- Renders 600 en 390 in `renders/` (geen overloop, geen kapotte beelden, geen em dash). 21 unieke links, alle 200 (`linkcheck.txt`). Reviews letterlijk uit `content/reviews/reviews.csv`, 5 sterren, max 120 tekens.

## 6. Gevonden, voor Floris

1. **E-booklink in de live P1 geeft 404** (delivery.shopifyapps.com/-/b3a2...; ook de twee andere Digital Downloads-links). v5 linkt naar /products/e (200). Live P1-FIRST/REPEAT moeten een werkende link krijgen. [VRAAG FLORIS: juiste downloadlink]
2. Prijzen volgen Shopify (zoals YyGsj3): Pan Pro Standard $144 en 2 Pans + 2 Lids $199, terwijl DECISIONS $149 (18 nov) en $249 (8 nov) noemt. Eén van de twee bijwerken.
3. VIP15-PICKS eindigt ma 30 nov; daarna heeft PP2 een nieuwe code nodig (voorstel: unieke Klaviyo-coupon 72 uur, dan kan PP2 evergreen).
4. PP4 deksel-kaart linkt naar de dekselpagina zonder variant; maat staat in de tekst.
5. Trackers UFAa3W en WZzjKR (ppv_vr_*) moeten live en eenmalig gevuld zijn, anders toont PP2 alleen de hero.

## 7. Livegang (alleen op akkoord Floris)

1. Copy, prijzen (punt 6.2) en e-booklink akkoord. 2. Trackers live + backfill (let op: met 5 minuten wachttijd moet WZzjKR de Ordered Product-events, ook Aftersell, binnen 5 minuten verwerkt hebben; anders vangt alleen event.Items en siraat_owned het bezit) (zie post-purchase-viewed/SCENARIOS.md 5-6). 3. VIP15-PICKS actief zetten met echte einddatum (of nieuwe unieke code). 4. Testmails van alle 7 templates naar een intern profiel (unieke onderwerpen, PLAYBOOK 6). 5. Ukz7F9 live met filter "geen mail uit X3ySuU/VQ93sx in 30 dagen" op de instap; X3ySuU en VQ93sx 21 dagen laten uitlopen, dan hun mails op draft (PLAYBOOK 7). UUZr3e niet live zetten (zit in PP2).

## Bestanden

`_tools/cuts.py` (uitsneden, bundels) · `_tools/sections.py` + `render.js` (beeldsecties) · `_tools/build.py` (7 templates naar `out/`) · `_tools/preview.py` + `ctx.py` (lokale Django-render) · `_tools/klaviyo.py` (templates + API-render naar `api/`) · `_tools/flow.py` (draftflow, `flow-definition.json`, `flow-readback.json`) · `_tools/shot.js` (renders).
