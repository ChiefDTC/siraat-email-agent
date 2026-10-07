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
