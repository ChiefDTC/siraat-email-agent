# Playbook · Siraat's Kitchen e-mail

Vaste regels. Alles hier is geleerd uit echte fouten of echte cijfers. Wijzig alleen met een reden in `LOG.md`.

## 1. Merk en toon

Bron: Brand Guidelines v1.4 (augustus 2026, goedgekeurd door Floris van der Heijden, kopie in `brand/`). Dit is leidend boven alles hieronder.

- One-liner: "Cook without coatings. Cook without compromise." Positionering: voor gezondheidsbewuste thuiskoks die niet willen kiezen tussen niet-giftig en prestaties; puur titanium dat gecoate pannen overtreft, met levenslange garantie en 100 dagen proef.
- Vier messaging-pijlers, per mail één, nooit alle vier: (1) Non-toxic, for real (koud publiek, welcome), (2) Pure titanium performance (bezwaren, cart/checkout, post-purchase), (3) Built for life (campagnes, vergelijkingen, retargeting), (4) Made for people who love to cook (recepten, community, UGC).
- Goedgekeurde claims, letterlijk: "100% pure titanium", "Free from PFAS, BPA and toxins", "No PFAS, PFOA, or BPA", "No coatings", "Lifetime warranty", "100-day trial", "Free shipping on all orders", "100K+ happy customers", "Anti-microbial" (alleen snijplank), "3-ply" (alleen Pan Pro-lijn). Plus uit de oktober-brief: "Tested free from Light Labs", "PFAS-free titanium cooking surface".
- Verboden: medische of ziekteclaims, "doctor recommended", aanvallen op concurrenten bij naam, vage superlatieven. Geen angst als hoofdtoon: bewijs eerst, dan vreugde.
- Beslissing Siraat (6 okt 2026): de kernclaim is "with a pure titanium cooking surface". Niet "100% pure titanium pan" als losse claim. Altijd in combinatie met "no coatings".
- Twee registers: campagnes LOUD (caps, emoji, echte countdowns, uitroeptekens, superlatieven die waar zijn), flows en productpagina's kalm (zinskapitalen, specificaties met middots, cijfers boven adjectieven, geen uitroeptekens). Reviewmails en educatie horen bij kalm.
- Elke regel: echte cijfers, echte deadlines, echte compare-at-prijzen. Nooit een asterisk nodig.
- Vuistregel: als een zin in de mail van elk willekeurig DTC-merk kan staan, scherp hem aan tot hij alleen van Siraat kan zijn.
- Oprichtersverhaal (kort): Nederlandse oprichters, begonnen met titanium snijplanken, uitgegroeid tot een complete cookware-lijn, ruim 100.000 klanten in iets meer dan een jaar. Eén materiaal is het hele idee: puur titanium, geen coating die kan slijten. Klanten gooien hun oude pannen binnen een week weg.

- Engels, Amerikaans publiek (US is de hoofdmarkt, INT-segment apart).
- Toon: eerlijk, direct, warm. Geen hype, geen uitroeptekens-stapels, geen "Don't miss out".
- Founder-notes (tekstmails van de oprichter) halen 1,3 procent klik tegenover 0,3 tot 0,6 procent voor beeldmails. Minstens één tekstmail per campagnereeks.
- Nooit een gedachtestreepje (em dash) in teksten, ook niet in Nederlandse berichten aan Siraat. Komma of nieuwe zin.

## 2. Visuele stijl (design system in Figma)

Let op: de brand guidelines (site) gebruiken Inter voor koppen en Terracotta #C75442 als merkrood, Ink #272727 voor knoppen. Siraat heeft voor e-mail gekozen voor TT Ramillas Light Italic als kopletter en brick #AC3B19. Dat is een bewuste afwijking voor e-mail; de rest van de site-canon (Ink, hairline #E4DED3, warm #F6F4F0) mag in e-mail gebruikt worden waar het past.

- Achtergrond: wit buiten de mail, crème #F8F7F2 alleen op de 600px-kolom. Nooit crème over het hele scherm.
- Kleuren: paper #FFFFFF, sand #ECE7DD (lijnen), ink #282828 (tekst), charcoal #2B2929, espresso #321E1D, brick #AC3B19 (knoppen, sterren, eyebrows), titanium #C9C6C0, grijs #727272 (bodytekst secundair), legal #9A948B.
- Koppen: TT Ramillas Light Italic. Licentie is desktop-only, dus in e-mail altijd als afbeelding (PNG, transparant, 2x). Nooit als webfont insluiten.
- Lopende tekst: Inter via `@import` van Google Fonts in de `<style>`. Klaviyo verwijdert `<link>`-tags. Gmail toont dan Arial, dat is acceptabel.
- Fallback-serif voor live tekst: Instrument Serif Italic, dan Times New Roman. Nooit Georgia bold (ziet er zwaar uit in Gmail).
- Logo: altijd de officiële bestanden uit `brand/logo/` (wit op foto of donker, zwart op crème of wit). Nooit nagetekend, nooit door AI.
- Hero: één vierkante afbeelding (600x600, 1200x1200 geleverd) met de kop erin gebakken en een donkere overlay. Het logo mag als overlay op de foto. Geen navigatiemenu's.
- Alles gecentreerd. Geen trust-bar, geen social footer, geen "Built for Life"-blok in flow-mails. Alleen privacy, terms, manage preferences, unsubscribe en adres onderin.
- Ruimte: buitenkant boven 8px (Gmail voegt zelf ongeveer 20px toe), intro-padding 28px, tussen hero en kop 28px.
- Afbeeldingen licht houden: hero als PNG maximaal 1,3 MB, liever JPG via Figma-export. Homestead-mails waren 250 KB tot 4,7 MB aan beeld en scoorden slechter dan tekstmails.

## 3. Foto's en AI-beeld

- Bronnen: Drive-map "Siraat flash style" (archief), Figma-pagina "03 Fotos" (werkbibliotheek), `klaviyo/figma/photos/` (repo-kopie, 1800px).
- AI-beelden (Higgsfield, gpt_image_2_5) alleen in flash-stijl met de echte productfoto als referentie.
- Regel zonder uitzondering: het model mag nooit letters, logo of opdruk renderen. Schortbandjes komen verhaspeld terug ("3IRAAT"). Prompt altijd "plain cream straps, no text, no patch". Bestaand beeld schoonmaken met een edit-pass "only change: plain straps, nothing else". Logo komt daarna in Figma.
- Referentiebeelden naar Higgsfield via `media_import_url` met een Figma-screenshot-URL. upload.higgsfield.ai is geblokkeerd.

## 4. Techniek: templates en flows via de API

- Templates: CODE-editor, volledige HTML, bron in `klaviyo/templates/`. Aanmaken met `create_email_template`, bijwerken met `update_email_template` (altijd de volledige HTML meesturen).
- Flow-templates: Klaviyo maakt bij elke koppeling aan een flow-mail een eigen kopie van de template (naam met datumprefix). De bron in de bibliotheek blijft S2tykT-achtig; wijzigingen in de bron komen niet automatisch in de flow. Na een template-update: in de flow opnieuw "Change template" doen of de flow-action patchen.
- Flows aanmaken: `POST /api/flows/` met `definition` (revision 2025-10-15). Acties met `temporary_id`, links via die id's. Geen `definition` in `PATCH /api/flows/`, alleen status en naam.
- Flow-acties aanpassen: `PATCH /api/flow-actions/{id}/` met `attributes.definition` die `id`, `type` en `data` bevat.
- A/B-test in een flow: actietype `ab-test` met `main_action` (send-email) en `current_experiment` (variations, allocations, winner_metric "unique-clicks", automatic_winner_selection_settings). De API kan de test niet starten; dat is één klik "Start test" in de editor. Variaties worden pas aangepast via `PATCH /api/flow-actions/{variatie-id}/`.
- Filter-syntax die bewezen werkt: `profile-metric` met `measurement count`, `measurement_filter numeric equals/greater-than`, `timeframe_filter` alltime / in-the-last / flow-start, `metric_filters` met `Items list contains-any` of `$flow string equals`.
- Geen herinstap: `reentry_criteria {duration 1, unit alltime}` plus een `profile-not-in-flow alltime` filter.
- Rate limit: na een reeks calls 1 tot 2 seconden wachten, anders 429.
- Rapporten: `get_flow_report` en `get_campaign_report` (MCP) met conversion metric RSNxYV. Flow-rapporten zijn groot (60 KB+): opslaan en met python samenvatten.

## 5. Segmentatie en filters (reviewflow als standaard)

- Welcome-pop-up: opt-in geeft een lot in de giveaway "Win your order for free", geen kortingscode. De welkomstreeks kan dus niet openen met een aanbieding. Eerst verhaal en bewijs, aanbod later in de reeks (bron: oktober-brief aan Homestead).
- Vaatwasstrips (Dishwashing Detergent Sheets) zijn het enige abonnementsproduct en het instapproduct. Ze komen als mystery gift mee. Eerst 10 dagen educatie, dan pas soft-sell met 20 procent op het abonnement; pak bevat 10 vellen, dus de refill-timing is kort.

- Trigger voor "na bezorging": Shopify-metric Delivered Shipment (VcUF33). Vuurt één keer per zending en loopt gelijk met het aantal orders. Niet de Postflows- of segment-variant gebruiken.
- Wachttijd reviewverzoek: 14 dagen na bezorging, 09:30 lokale tijd van de klant.
- Instapfilters: één keer per klant, ooit; set-kopers in backorder uitsluiten op alle producttitels (titels wijzigen per actie, dus altijd de hele lijst); geen mail uit een overlappende flow in de laatste 30 dagen.
- Verzendfilters (op het moment van versturen, niet bij instap): geen Gorgias-ticket sinds de start van de flow (dus ná bezorging), geen refund in 30 dagen, order volledig fulfilled in de laatste 60 dagen.
- Waarom niet "nooit een ticket": 3.500 tickets per maand bij 3.400 bezorgingen; het meeste is "waar blijft mijn pakket" vóór bezorging plus leveranciersmail. Dat filter gooit je beste klanten weg.
- Waarom "volledig fulfilled": ruim 2.000 klanten per maand krijgen een deelzending. Zonder dit filter vraag je een review terwijl de helft nog onderweg is.
- Sterren-routing in reviewmails: 5 en 4 sterren naar Trustpilot (https://www.trustpilot.com/evaluate/siraatskitchen.com), 3, 2 en 1 ster naar https://siraatskitchen.com/pages/your-experience met `?rating=N&order={{ event.extra.order_number }}`. Hero-afbeelding is geen link.
- Open punt: Trustpilot stuurt geen events naar Klaviyo. Check of Trustpilot's eigen automatische uitnodigingen uit staan, anders dubbele verzoeken.

## 6. Testen

- Eén variabele per test. Winnaar op unieke kliks, nooit op opens (Apple Mail Privacy vervuilt opens).
- Basislijn reviewmail: 3,3 procent klik, 0,74 procent uitschrijf (oude flow, 90 dagen, 10.784 mails).
- Steekproef: bij 3,3 procent basis en 3.600 mails per maand zie je een groot verschil (naar 5 procent) in een maand; een klein verschil (naar 4,3 procent) vraagt ongeveer 5.000 mails per arm. Minimaal vier weken laten lopen, geen automatische winnaar.
- Volgorde van tests per flow: 1 onderwerpregel, 2 wachttijd (7 tegenover 14 dagen via twee paden), 3 incentive-framing.
- Uitschrijfratio boven 0,5 procent op een flow-mail is een signaal, boven 1 procent is een probleem.

## 7. Overgang van een oude naar een nieuwe flow

1. Nieuwe flow live met instapfilter "geen mail uit de oude flow in 30 dagen".
2. Oude flow laten draaien tot iedereen die vóór de livegang de trigger kreeg erdoorheen is (voor de reviewflow: 6 dagen).
3. Dan de e-mailstap in de oude flow op Draft. Niet archiveren, de cijfers blijven nodig.
4. Controleer na elke template-wissel in een live flow de HTML op de echte links (Trustpilot, your-experience) en op verouderde blokken. Op 6 oktober 2026 stond er een conceptversie met placeholder-links in de live flow.

## 8. Producten en aanbod (bron: brand guidelines en Shopify)

- Hero: 12-delige Cookware Set ("A complete PFAS-free kitchen in one decision"), de Q4-push. Nu in backorder, dus tijdelijk niet pushen en uitgesloten van reviewverzoeken.
- Kernlijn: Titanium Hammered Pan Pro (Mini, Small, Standard, Large), Wok, Deep, Crepe, Roasting, Pizza Steel. Uitbreiding: snijplanken, schorten (Moss, Ember, Oak, Azure), molens, utensils.
- Naamgeving: Title Case, materiaal eerst ("Titanium Hammered..."), maat als suffix. Nooit "Ti" of "SK".
- Evergreen aanbod: 41 procent korting plus gratis mystery gift. Diepere kortingen zijn campagnemomenten. Oktober 2026: "4 gifts, up to 50 percent off". Bundel-eerst, gift-with-purchase boven blanco korting.
- Garanties: levenslange garantie op cookware (in ads soms "75-year warranty"), 100 dagen proef vanaf bezorging, gratis verzending, 30 dagen gratis retour.

## 9. Werken met Claude (permissies)

- Cloud-sessies in "Auto"-modus blokkeren wijzigingen aan live flows, ook met mondeling akkoord. Voor bouwwerk aan live flows: gewone modus en één keer "Allow".
- Klaviyo-API-key zit als credential in de omgeving (header Authorization: Klaviyo-API-Key, host a.klaviyo.com). Scopes: flows full, templates read, metrics read, segments read. Voor campagnes en profielen is een aparte key nodig.
- Routines (geplande taken) uit een sessie krijgen geen connectors mee. Routines die Slack of Klaviyo-MCP nodig hebben, worden in de claude.ai Routines-UI aangemaakt met de prompt uit `ROUTINES.md`.

## 10. Vaste opbouw van een flow-mail (vanaf 7 oktober 2026)

- Hero 1200x1200 via `scripts/make_hero.py`: kop in TT Ramillas en subregel als blok exact in het midden van het beeld, label bovenin gecentreerd. Altijd een shoot-foto of geverifieerde Shopify-foto, nooit twee keer dezelfde in één flow.
- Direct onder de hero de primaire knop (in checkout en cart: "Return to my cart"). Dezelfde knop nog één keer onderaan.
- HTML en preview bouwen met `scripts/build_template.py`; beelden in de Klaviyo-bibliotheek, links in `<assets>/klaviyo-urls.txt`.
- Beelden met labels krijgen op mobiel een aparte versie zonder labels plus live tekst eronder.
- Header en footer zijn vast en komen uit `klaviyo/templates/partials/` (header.html, footer.html). In elke bron-template staan alleen `{{HEADER}}` en `{{FOOTER}}`; `scripts/build_template.py` vult ze in. Header: monogram + "Built for Life" (TT Ramillas, PNG) en navigatie Cookware, Sets, About (live tekst, verborgen op mobiel). Footer: donker #282828, monogram + "Built for Life / Non-Toxic Cookware", vier navigatieregels, Facebook en Instagram, claims-regel, unsubscribe, voorkeuren, webversie, adres.
- Wijzig je header of footer, dan in de partial, en alle templates opnieuw bouwen.

## 11. UX-standaard en blokken (vanaf 7 oktober 2026, na UX-ronde)

Bron: research/ux-2026-10-07 (00-samenvatting, 01-ux-audit deel D). Referentiemail: `klaviyo/templates/v3/checkout/c1.html`.

- **Aanbod altijd in de hero.** `make_hero.py ... --offer="EXTRA 10% OFF WITH HI10  ·  $70 IN GIFTS"`. Checkout, cart en browse `--ratio=4:3`. Label en subregel zijn groot genoeg voor mobiel (40 en 48 px op 1200). Alt-tekst noemt het aanbod letterlijk.
- **Codebalk** `{{BLOCK:codebar}}` boven `{{HEADER}}` in elke verkoopmail (niet in P1, P2, W0, W2-tekstmail).
- **Cart en knop boven de vouw** in checkout en cart: hero, dan `{{BLOCK:cart}}`, dan `{{BLOCK:cta}}`.
- **Knoppen** alleen via `{{BLOCK:cta label="..." url="..."}}`: 340 px desktop, volle breedte mobiel, ik-vorm met voordeel ("Complete my order", "Claim my 10% + gifts", "Get 10% off this pan"). Drie keer dezelfde primaire knop. Links met de korting al toegepast: checkout `responsive_checkout_url` + `&discount=HI10`, elders `https://siraatskitchen.com/discount/HI10?redirect=/pad`.
- **Feiten als iconen**: `{{BLOCK:icons}}` (US) of `{{BLOCK:icons-int}}` (internationaal, "No import duties", DDP). Nooit levertijden in marketingmails.
- **Gifts** `{{BLOCK:gifts}}`: vier beelden met waarde, "$70 in gifts", filter is altijd "win/chance to win a PFAS water filter", nooit "purifier" of "free filter".
- **Uitleg over de pan** `{{BLOCK:features}}` met drie iconregels (i1..i3 = icoonnaam uit `partials/shared/icon-*.png`).
- **Reviews** `{{BLOCK:reviews q1 n1 q2 n2}}`: gelijke hoogte, quotes 5 sterren, max 120 tekens, lengteverschil max 30.
- **Aanbodblok** `{{BLOCK:offer}}` (espresso) met optioneel `deadline="..."` alleen bij een unieke verlopende code (`{% coupon_code 'NAAM' %}`). Geen "final call", "reserved", "expires tonight" zonder echte deadline.
- Gedeelde beelden staan in `klaviyo/templates/partials/shared/` en heten in de bron `{{SHARED}}/bestand`. CDN-links in `partials/shared/klaviyo-urls.txt`.
- Hero-foto's per flow in `content/media/hero-register/<flow>.csv`, nooit dubbel over flowpaden.

## 12. Bouwronde v4 (vanaf 7 oktober 2026)

- Bindend plan: klaviyo/flows/v4-flow-system.md. Copy volgt de skill siraat-direct-response en research/copy/05-siraat-copy-playbook.md.
- Nieuwe blokken naast die van h11: {{BLOCK:compare}} (vergelijkingstabel, rijen alleen uit research/ux-round2/comparisons.md), {{BLOCK:closerlook}} (callout-anatomie, img=panpro|roast|set6), {{BLOCK:productcard}} (kaart met sticker). Stickers via scripts/make_sticker.py en scripts/place_sticker.py.
- Hero: het aanbod staat altijd in de aanbodbalk en de codebalk; de kop draagt het idee van de mail.
- Onder elke primaire knop een friction reducer. UTM per blok volgens research/testing/04-utm.md.
- Reviews alleen letterlijk uit Trustpilot (reviews-positive-usable.csv); Okendo/Loox niet tot de herkomst duidelijk is.
- **Productkaart** `{{BLOCK:productcard ...}}` voor elke productkaart, nooit meer inline nabouwen. `img="card-x.jpg"` = gedeeld beeld uit `partials/shared`, `img="{{IMG}}/card-x.jpg"` = eigen beeld uit de assets-map van de flow. `now` leeg en `was` leeg = geen prijsregel. `us="1"` zet prijsregel en note binnen `{% if %}` op de US-voorwaarde van de trigger, `us="price"` alleen de prijsregel (note blijft zichtbaar), `uscond="..."` overschrijft de voorwaarde. Voorwaarden (build_template.py, USCOND): Placed Order (post-purchase, winback, vip, anniversary) `event.extra.shipping_address.country_code == 'US'`; Checkout `event.extra.presentment_currency == 'USD' or not event.extra.presentment_currency`; Added to Cart `event|lookup:'$currency' == 'USD'`; Viewed Product `'$' in event.Price`. Welcome, site, sunset en ugc hebben geen event: daar geen `us`.
- **Doorgestreepte prijs alleen bij een echte compare-at uit Shopify** die Floris bevestigt of die als anker in DECISIONS staat: Pan Pro Standard $439 bij $134, 12-delige set $1,186 bij $599, Roasting Pan $250 bij $199. Nooit de eigen verkoopprijs doorstrepen om een codeprijs te tonen: dan `now="$59"` en `note="$53.10 with your code"`. Maatkiezers zonder streep (Mini, Small, Large hebben in Shopify wel een compare-at, maar die is niet bevestigd als anker).
- **Lengte**: verkoopmails maximaal ~3.600 px op 390 px breed, inclusief footer (~550 px). Per mail maximaal 2 grote onderdelen (vergelijking, closer look, value stack, maatkiezer). Het iconenblok mag weg waar de friction reducers hetzelfde zeggen (verzending, retour). Aanbod, cart of product en knop blijven boven de vouw; minimaal 2 reviews. P2 en P2-safe (handleidingen) mogen langer.
- **Friction reducer** onder elke primaire knop in dezelfde stijl: `sub` met 12 px / 18 px, #727272, één regel op mobiel. Teksten: US en HI10 `Free shipping. 30-day returns. 100,000+ happy customers.`, unieke code `One use, already applied. 30-day returns. 100,000+ happy customers.`, INT `Free shipping, duties paid. 30-day returns. 100,000+ happy customers.` (INT met code: `One use, already applied. Duties paid. 30-day returns.`).
- **Reply-regels**: geen "A real person reads every email" en geen "I'll tell you" zolang niet vaststaat dat Benjamin zelf leest (OVERZICHT 30): `Reply and our team will help.` Ondertekening altijd `Benjamin` / `Founder, Siraat's Kitchen`.
- **Header**: de navigatie is op mobiel verborgen via `.navhide` in `partials/blocks/_style.css` (dus in elke mail, ook zonder eigen regel). Er zijn geen kopieën van de header meer in flowmappen; post-purchase/partials en winback/partials zijn symlinks naar de root.
- **Previews met logica**: na `build_template.py` de `-preview.html` overschrijven met een Django-render op een voorbeeld-event: `python3 research/tailoring/test/expand.py <bron> <assets> /dev/null <exp>` en `python3 research/tailoring/test/render.py <exp> research/tailoring/test/samples/<sample>.json <id>-preview.html assets ../../partials/shared`, dan `render_preview.js`. `expand.py` is een afgeleide van build_template.py (tot en met de _style.css-regel) en moet na elke wijziging aan build_template.py opnieuw worden afgeleid. Controle: `python3 -I scripts/check_previews.py` (0 problemen) en `bash research/tailoring/test/run_tests.sh` (0 FOUT).
- **Beeldscherpte en export** (vanaf 7 oktober 2026): elk beeld minimaal 2x zijn weergavebreedte, nooit opgeschaald boven de bron (controleer ook de uitsnede van de bronfoto, niet alleen de pixels van het eindbestand). Hero < 300 KB, kaart < 120 KB, GIF < 1 MB, mail < 1,5 MB. GIF's en stills uit de chef-video met `scripts/make_chef_media.py` (1080p-bron, bovenste 1920x840, gifsicle --lossy). Naar Klaviyo alleen via `scripts/export_klaviyo.py` (eerst dry-run, live met `--live --i-am-sure`), zie `exports/README.md`. `build_template.py` zet nu zelf UTM's op header- en footerlinks in de Klaviyo-versie; `expand.py` is daarna opnieuw afgeleid.
- **QA-poort: qa_render.py moet groen zijn voor elke export** (vanaf 7 oktober 2026). `python3 -I scripts/qa_render.py` (vanuit /tmp) bouwt elke mail zoals de export, rendert hem met Django op echte events per trigger (checkout: kookgerei, set, accessoire, EUR; cart, browse, post-purchase, winback, vip, anniversary idem; welcome, site, sunset, ugc zonder event) en meet in Chromium op 600 en 390 px: geen restanten `{% %}`/`{{ }}`, geen lege productregel, geen `$0`, geen overflow, hoofdtabel 600 px, hero en blokken op volle breedte, alle beelden laden, hoogte verkoopmail <= ~3.600 px. Ook de ruwe HTML (zoals de Klaviyo-code-editor hem toont) mag geen tekst in tabelcontext hebben. Rapport `exports/qa/render-report.md`, screenshots `exports/qa/shots/`. `export_klaviyo.py --live` weigert bij een FOUT; `run_tests.sh` draait `qa_render.py --static` mee.
  - Tag-allowlist: ingebouwde Django-tags (if/elif/else, for/empty, with, firstof, cycle, now, comment, spaceless, autoescape, filter, ifchanged, regroup, templatetag, verbatim, widthratio, lorem) plus Klaviyo `coupon_code`, `unsubscribe`, `unsubscribe_link`, `manage_preferences`, `manage_preferences_link`, `web_view`, `web_view_link`. Geen `_url`-varianten, geen load/include/extends/url. Filters: Django-standaard plus Klaviyo (`lookup` e.a.); `cut` en `slice` staan op twijfel tot een Klaviyo-preview ze bevestigt.
  - `build_template.py` zet besturingstags in HTML-tekst in commentaar (`<!--{% if ... %}-->`): Klaviyo/Django voert ze gewoon uit, de editor toont ze niet en de browser zet ze niet meer boven de tabel. Uitvoertags (`coupon_code`, `unsubscribe`) en tags in attributen blijven zoals ze zijn. `research/tailoring/test/kltags.py` registreert alleen de allowlist.

### v5-bouwstenen (vanaf 8 oktober 2026)

Gedeelde blokken en macro's voor de v5-flows. Code: `scripts/v5lib.py` (aangeroepen door `build_template.py`), sjablonen in `partials/blocks/` (gifts5*, reviews3*, bundle*, xsell*), reviews uit `content/reviews/sets.json` (`scripts/make_review_blocks.py`), prijzen uit `content/catalog/products.json`. Nooit bedragen, maten of verzendregels meer met de hand in een mail typen: altijd via deze macro's, dan klopt elke markt.

**Markt-helper.** De markt volgt uit de map van de mail, met per flowtype het beste signaal (`research/v5/01-markten.md` sectie 4):

| Flowmap | Signaal | Onbekend als |
|---|---|---|
| post-purchase, winback, vip, anniversary | `event.extra.shipping_address.country_code` | geen verzendland |
| checkout | `event.extra.presentment_currency`; USD telt als US als `person.Country` leeg of US is | geen valuta |
| cart | `event\|lookup:'_ip_country_code'` | geen IP-land |
| browse | `person.Country`, dan `person.country_code`, dan de prijsnotatie (`£`, `€`, `$134` zonder decimalen = US) | niets van dat alles |
| welcome, site, sunset, ugc | `person.Country`, dan `person.country_code` | geen profielland |

Markten: US, CA, UK, EU (EURO-prijslijst), AU, NZ, SG, HK, ME (Golfstaten), overig bekend land, onbekend. Een bron buiten `v3/<flow>/` zet `<!-- MARKET-SIGNAL: order|cart|checkout|browse|profile -->`. `person.Country` is de Klaviyo-tag voor het profielland; nog één keer in een Klaviyo-preview op een echt profiel bevestigen.

**Inline macro's** (overal, ook in alt-teksten en blokparameters):

| Macro | US | UK (voorbeeld) | onbekend |
|---|---|---|---|
| `{{SIZE:28}}` | 11″ | 28 cm | 28 cm (11″) |
| `{{SIZE:20:both}}` | 8″ (20 cm) | 20 cm | 20 cm (8″) |
| `{{PRICE:standard}}` | $144 | £124 | (leeg) |
| `{{PRICE:standard*0.9}}` (codeprijs) | $129.60 | £111.60 | (leeg) |
| `{{FROM:deep}}` (laagste variant) | from $119 | from £94 | (leeg) |
| `{{WAS:standard}}` (compare-at, alleen waar die bestaat) | $288 | £248 | (leeg) |
| `{{PRICE:standard\|tekst}}` | $144 | £124 | tekst |
| `{{SHIP}}` | Free shipping from the US | Free shipping, duties paid | Free shipping, duties paid |
| `{{FRICTION}}` | Free shipping from the US. 30-day returns. 100,000+ happy customers. | Free shipping, duties paid. 30-day returns. 100,000+ happy customers. | idem INT |
| `{{FRICTION:code}}` | One use, already applied. 30-day returns. 100,000+ happy customers. | One use, already applied. Duties paid. 30-day returns. | idem INT |
| `{{GIFTS:total}}` / `{{GIFTS:TOTAL}}` | $70 in gifts / $70 IN GIFTS | £55 in gifts | 4 free gifts |
| `{{GIFTS:filterline}}` | a $450 PFAS water filter | a £350 PFAS water filter | a PFAS water filter |
| `{{GIFTS:ship}}`, `ebook`, `mystery`, `filter` | $15, $30, $25, $450 | £10, £25, £20, £350 | (leeg) |

Gift-waarden: US $70/$450, CA C$95/620, UK £55/350, EU €70/410, AU A$100/660, NZ NZ$120/820, SG S$95/590; HK, Midden-Oosten, Noorwegen en de rest "4 free gifts" zonder bedrag (DECISIONS 8 okt). Prijzen alleen in de markten met een vaste prijslijst (US, CA, UK, EU, AU, NZ, SG); elders leeg, dus de zin moet zonder bedrag ook lopen of in `{{IF:PRICED}}` staan. Productsleutels voor PRICE/WAS/FROM: `mini small standard large deep wok crepe pizza roast lid lid20 lid26 lid28 lid30 board boardbundle utset utensil apron mill sheets set6 set12 setpro complete full everything duo2 panproduo produo kit cookprep panutensil withlid` of een Shopify-handle. US-only producten (12-delig, potten, roasting pan, 2 Pans + 2 Lids, 34-delig) geven buiten de US altijd leeg.

**Takken per markt:** `{{IF:US}}...{{ELIF:UK}}...{{ELIF:AU,NZ}}...{{ELSE}}...{{ENDIF}}`. Markten: US, CA, UK, EU, AU, NZ, SG, HK, ME, PRICED (alle markten met prijslijst), KNOWN (elk bekend land). Bijzondere vormen (zonder ELIF): `{{IF:INT}}` (bekend en niet US), `{{IF:NOTUS}}...{{ELSE}}`(else = US), `{{IF:UNKNOWN}}...{{ELSE}}`. **US-only:** `{{USONLY}}12-delige set, {{PRICE:set12}}{{ELSEUS}}de 6-delige set{{/USONLY}}`: elke zin, kaart of link over een US-only product staat hierin; onbekend telt als niet-US.

**Blokken:**

- **Gifts** `{{BLOCK:gifts5}}` (raster, vier gift-beelden met waarde per markt) of `{{BLOCK:gifts5 style="row"}}` (compacte strook voor direct onder de cart, met regel "Your $70 in gifts ship with this order."). Altijd de echte beelden `gift-shipping.jpg` (officieel site-beeld), `gift-ebook`, `gift-mystery`, `gift-filter`; zonder bedrag staat er "Included" en bij de filter "Chance to win". Opties: `urgency="1"` (regel "Your 4 gifts end when the fall sale ends."), `headline`, `eyebrow`, `note`, `line` (strook), `pad`. Voorbeeld C1: `{{BLOCK:gifts5 style="row" urgency="1" line="Your cart is waiting, with {{GIFTS:total}} still pending."}}` Macro's binnen een blokparameter mogen; aanhalingstekens in de tekst niet.
- **Reviews, drie pijlers** `{{BLOCK:reviews3 set="c1"}}`: 2 of 3 echte Trustpilot-reviews uit `content/reviews/top.md`, letterlijk, 5 sterren, naam, "Verified buyer" en een pijlerlabel (On quality, On delivery, On service; zo gekozen dat de set zo veel mogelijk pijlers dekt). Sets: elke mail-id uit top.md (c1, k3, w4-int, r2-vip ...) plus `kls-pan`, `kls-set`, `kls-int`, `kls-acc`, `kls-owner`. Opties: `n="2"`, `ids="R577,R516,R240"` (eigen keuze, moet in de gecontroleerde lijst staan), `pillars="K,L,S"`, `eyebrow="IN THEIR WORDS"`. R017 (Marilyn B.) kan niet meer. Na een wijziging in top.md: `python3 -I scripts/make_review_blocks.py`.
- **Bundel** `{{BLOCK:bundle}}`: "What's in the box" plus rekensom, gekozen op de producttitel (één if-keten op `event.Items`, in cart `Product Name`, in browse `Name`; `src="..."` overschrijft). Bundels: 6-delig/fall sale ("Buy 2, get 4 free.", "Six pieces for $299" met compare-at doorgestreept en "Bought one by one: $562."), 12-delig (US), 34-delig (US), Full Hammered Pro, Complete Edition, Cookware Set Pro, Pan Pro Duo, Pro Duo 2 pans + 2 lids (US, Mini + Pan Pro + 2 deksels, $199), Pro Duo (pan + flipper), Pan Pro Kit, Cook & Prep, Pan Pro & Utensil. Bedragen per markt uit de catalogus; de losse som alleen als die echt hoger is; compare-at alleen bij 6- en 12-delig (bevestigde ankers). US-only bundels en onbekende titels krijgen buiten de US het algemene blok ("Every piece, the same titanium surface.", tekst via `fallback="..."`).
- **Cross-sell** `{{BLOCK:xsell}}` (bedoeld voor P3, R1, R2, V1, N1, N2; werkt in elke flow): kandidaten per categorie uit de kooppatronen (`research/v5/04-cross-sell.md` 6.1, drie per categorie), één rij per product, nooit iets uit de huidige order of uit `person.siraat_owned` (lijst sleutels uit `scripts/sync_owned.py`; sets in de order tellen mee via hun inhoud), US-only nooit buiten de US, echte productfoto's `pc-*.jpg`, prijzen per markt (Mini $99, Small $137, Standard $144, Large $149, set $299). Opties: `pre="https://siraatskitchen.com/discount/HI10?redirect=/products/" post="%3Futm_source%3Dklaviyo..."` (code in de link; varianten worden dan zelf URL-gecodeerd), `fall="1"` (fall-sale-set als extra rij voor wie Mini, Small en Large nog niet heeft), `prices="us"` (alleen US-prijs; scheelt ~3 KB) of `prices="none"`, `headline`, `eyebrow`, `note`, `fallback` (regel als alles al in huis is, ook bij het 34-delige bundel). Grootte ~35 KB broncode in order-flows: niet naast `goes` in dezelfde mail.
- **Vergelijking** `{{BLOCK:vs kind="pfas"}}` ("Your future pan vs a PFAS pan", besluit 8 okt: direct "PFAS pan", geen gezondheidsclaim, geen merknamen), `kind="steel"` (vs stainless steel, twee eerlijke gedeelde rijen) en `kind="castiron"`. Rijen uit `research/ux-round2/comparisons.md`. Opties: `colA="Your pan"` (na aankoop), `headline`, `eyebrow`, `note`, `pad`. Eén vergelijking per flow (03-copy-spec §1), dus wissel tussen de drie.

**Beelden.** Hero's van de mails uit `research/v5/05-beeld-vervangingen.csv` zijn opnieuw gebouwd met `scripts/make_v5_images.py --heroes` (zelfde kop, label en aanbodbalk als v4; tekst aanpassen = `HERO` in dat script wijzigen en opnieuw draaien): de 13 goedgekeurde v5-AI-beelden (`-v5-2k.jpg`) en echte foto's voor de drie afgekeurde (p2: hp-shoot P09-A, k2-new: P11-A, c3-p: packshot 6-delige set). De oude `*-01.jpg` AI-beelden staan nergens meer in gebruik (hero-register en `content/media/ai-flash/index.csv`). Nieuwe kaartbeelden `pc-large`, `pc-set6`, `pc-set12`, `pc-pizza`, `pc-roast` via `--cards` (make_product_blocks.py ruimt ze niet meer op). Nieuwe en gewijzigde beelden moeten nog naar de Klaviyo-bibliotheek (export_klaviyo.py).

**Tests.** `python3 -I research/tailoring/test/v5_blocks.py` (zit in `run_tests.sh`) bouwt `research/tailoring/test/v5/demo.html` per signaal en rendert op US, UK, AU, CA, SG, EU en onbekend: verwachte macro-uitkomst per markt, geen USD of inch buiten de US, US-only nooit buiten de US, gifts5 altijd met de vier gift-beelden, reviews3 zonder R017, bundel per titel, cross-sell nooit uit de order of uit `siraat_owned`. `qa_render.py` rendert nu elke mail ook per markt: in v5-blokken is elk marktprobleem een FOUT; zet `V5-STRICT` in de topcomment van een herbouwde mail en dezelfde regels gelden voor de hele mail (plus geen R017). Zonder die markering staan de punten als "v5-markt" in het rapport (werklijst).
