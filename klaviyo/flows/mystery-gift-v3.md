# Mystery Gift v3 · onthulling en abonnement op de vaatwasstrips (concept)

Versie 19 oktober 2026. Vervangt de dode flow WvRupU "Mystery Gift Reveal, Sheets". **Niets is in Klaviyo of Shopify aangemaakt of gewijzigd; dit is ontwerp plus bron-HTML. Livegang alleen na akkoord en klikwerk van Floris.**

Mails: `klaviyo/templates/v3/mystery/` (bron `m1.html` t/m `m4.html`, `-preview.html` gerenderd op een US-profiel, `previews/` met `-mobile-375.png` en `-desktop.png`, `assets/` met `m1-hero.jpg` t/m `m4-hero.jpg` (Higgsfield v2 23 okt, 1200x792, pak en vellen als held; v1 in `assets/v1/`, zie `assets/PROMPTS.md`) en `klaviyo-urls.txt`). Bouwen: `python3 -I scripts/build_template.py klaviyo/templates/v3/mystery/m1.html klaviyo/templates/v3/mystery/assets klaviyo/templates/v3/mystery/assets/klaviyo-urls.txt` (zelfde voor m2 t/m m4).

## 1. Waarom opnieuw

- WvRupU triggerde op Ordered Product met ProductID `15675410415956`. Dat product bestaat niet meer (Shopify, gecontroleerd 19 okt: `null`). De huidige gift-regel is "Mystery Gift" ID `15785445622100` (handle `dishwashing-detergent-sheets-fresh-lemon-sca_clone_freegift`, actief). Sinds de week van 21 sep gaat er niets meer uit; WvRupU staat nu op **Draft** (GET 19 okt).
- Oude cijfers: mail 1 ongeveer 1.066 tot 1.070 verzendingen per week; 90 dagen 19.190 mails en $4.293 (v3-new-flows.md tabel 1).
- Oude opbouw (read-only gelezen, templates YfC2ev, TC8ELx, UFRf6c, Wqa6M7): vier platte tekstmails van Benjamin op dag 3, 7, 11 en 16 (wacht 3 d tot 10:00, dan 4, 4 en 5 dagen). Profielfilter: `rc_active_subscriber` is false of niet gezet. Geen verzendfilters, geen header of footer, geen links behalve de productpagina in mail 3 en 4.
- Wat we overnemen: de eerlijke toon ("this one asks", "anyone who subscribes gets it"), de onderwerpen van mail 1 en 3 als controle in de A/B. Wat we schrappen: claims die we niet kunnen onderbouwen (PVA-film "is a plastic", prijsvergrendeling, 10% store credit, packs van 3 en 6: Shopify kent nu één plan), "30 washes" (pak zegt 30 sheets, up to 60 washes), de verwarrende onderwerpregel "...about the sheets" (tickets: mensen dachten aan beddengoed).

## 2. Aanbod (gecontroleerd in Shopify, read-only, 19 okt)

- Product "Plastic-Free Dishwasher Sheets" (`dishwashing-detergent-sheets-fresh-lemon`, actief), $25. Selling plan group "60 washes, delivered every month", één plan, maandelijks, **20% korting** (PERCENTAGE 20). Dus $20 per pak in de US.
- Geen kortingscode nodig: de 20% zit in het abonnement op de productpagina. Geen deadline, dus geen urgentie in de mails (skill 6: schaarste moet waar zijn).
- Verkrijgbaar in alle markten (catalogus); prijzen via `{{PRICE:sheets}}` en `{{PRICE:sheets*0.8}}` binnen `{{IF:PRICED}}`, marktsignaal `profile` (het Ordered Product-event heeft geen verzendland). Zonder bekend land loopt de zin zonder bedrag.
- [VRAAG FLORIS] "Skip or cancel anytime" en "Manage it from your account" staan in M3 en M4. Dat is standaard in het Recharge-klantportaal en stond ook in de oude M3, maar staat niet in claims.csv. Bevestigen dat het portaal aanstaat voor alle markten.

## 3. Trigger en filters

- **Trigger**: Ordered Product (metric XT7f8Z, zelfde als WvRupU), triggerfilter `ProductID equals 15785445622100`.
  - Risico: de gift-app maakte op 22 sep een nieuwe kloon met een nieuw ID. Advies: tweede conditiegroep (OF) `ProductName equals "Mystery Gift"`, zodat een volgende kloon niet weer stil valt. Plus een wekelijkse check (backlog).
- **Flowfilters** (gelden bij instap en vóór elke stap):
  1. `rc_active_subscriber` is false **of** is niet gezet (zoals WvRupU).
  2. Placed Order where `Items` contains "Plastic-Free Dishwasher Sheets" zero times since starting this flow (wie zelf strips koopt of zich abonneert, stopt).
  3. Has not been in this flow over all time (herhaalkopers krijgen de gift opnieuw, maar de onthulling maar één keer).
  4. Received Email where Flow = WvRupU zero times over all time (wie de oude onthulling al kreeg, kent de strips).
  5. Refunded Order (Xg6cwn) zero times in the last 30 days.
- **Verzendfilter op elke mail** (send-email `additional_filters`): Received Email where Flow = **X3ySuU** (v4 · Post-purchase) zero times **in the last 2 days**. Overlapt een mail met P1, P2-safe of P3, dan slaat Klaviyo die ene mail over en loopt de flow door.
- **Herinstap**: nooit (`reentry_criteria` alltime plus filter 3, PLAYBOOK 4).
- Smart Sending: aan laten (standaard voor flows).

## 4. Tijdlijn en naast X3ySuU

| Stap | Wachttijd | Dag na order | Mail | Botsing met X3ySuU / review |
| --- | --- | --- | --- | --- |
| 1 | 3 dagen, tot 10:00 lokaal | 3 | **M1 The reveal** | P1 op uur 1: altijd meer dan 2 dagen eerder, nooit overgeslagen. |
| 2 | 9 dagen, tot 10:00 | 12 | **M2 How to use them** | Rond de mediane levering (11,7 dagen). P2 (levering + 1 dag, via 2.5b, dus dag 8 tot 16) kan binnen 2 dagen vallen: dan wordt M2 overgeslagen. Schatting 20 tot 30% van de US-ontvangers. Bewust geaccepteerd: P2 gaat over de pan en is belangrijker. |
| 3 | 11 dagen, tot 10:00 | 23 | **M3 The offer** (20% abonnement) | P3 op dag 20 om 09:00: M3 valt ruim 3 dagen later. P2-safe (dag 16) en review XzHrez (levering + 14, rond dag 26) blijven buiten het venster van 2 dagen in het gewone geval. |
| 4 | 7 dagen, tot 10:00 | 30 | **M4 Last one** (optioneel) | Ruim na P3; vóór Winback R1 (dag 45). |

- Educatie eerst, dan pas het aanbod (PLAYBOOK 5): de vraag komt pas op dag 23, ruim 10 dagen na de uitleg en na levering.
- Waarom M1 vóór levering: de onthulling hoort bij het wachten op de doos (P1 noemt de mystery gift al als verrassing). De uitleg (M2) wacht tot de doos er is.
- M4 is optioneel: wil Floris de reeks kort houden, dan M4 op Draft en na 4 weken vergelijken.

## 5. Mails, onderwerp en preview

| Mail | Onderwerp (A/B waar vermeld) | Preview | Knop | Hero |
| --- | --- | --- | --- | --- |
| M1 | A: "Let's reveal your mystery gift" (oude controle) · B: "What's in the small box in your order" | It's not overstock. It's the other half of a no-coating kitchen. | See my gift up close | `m1-hero.jpg` pak omhoog uit de giftdoos |
| M2 | "The ten-second way to use your gift" | One sheet where the pod goes. Half a sheet for a light load. | Show me the sheets | `m2-hero.jpg` wit vel in het doseerbakje, pak op de deur |
| M3 | A: "Alright, here's the offer" (oude controle) · B: "20% off every delivery, not just the first" | Including the part most brands would leave out. | Get 20% every month | `m3-hero.jpg` nieuwe pakken komen binnen, oud pak bijna op |
| M4 | "Last one from me about the dishwasher sheets" | The price isn't going anywhere. These emails are. | Keep my sheets coming | `m4-hero.jpg` stilleven pak, vellen, giftdoos en pan |

Alle vijf onderwerptypes per mail staan in de topcomment van elke bron. A/B: één variabele (onderwerp), winnaar op unieke kliks, minimaal 4 weken, geen automatische winnaar (PLAYBOOK 6).

Inhoud in het kort:
- **M1** (klant, ~190 woorden): wat er in de doos zit, voluit "Plastic-Free Dishwasher Sheets ... Dishwasher detergent, not bedding", waarom een kookgerei-merk dit stuurt (je koos een pan zonder coating, de pod zit in folie), drie feiten (30 sheets / up to 60 washes, pre-dosed, no plastic film, phosphate-free, bleach-free), waarde `{{GIFTS:mystery}}`. Principes: wederkerigheid, commitment, sympathie.
- **M2** (educatie, ~230 woorden): drie manieren (volle lading, halve sheet of twee lades, met de hand), waarom geen pods, de pan mag mee de vaatwasser in (laat afkoelen, nooit koud water op een hete pan). Geen aanbod. P.S. kondigt de vraag aan.
- **M3** (aanbod, ~170 woorden): "This one asks", rekensom (1 keer per dag = ongeveer twee maanden), espresso aanbodblok "20% off every delivery" met `{{PRICE:sheets*0.8}} a pack instead of {{PRICE:sheets}}` (geen doorgestreepte eigen prijs, PLAYBOOK 12), eerlijk dat iedereen de 20% krijgt. P.S. losse verpakking.
- **M4** (laatste, ~150 woorden): laatste mail over de strips, prijs blijft, geen deadline dus geen haast, "your gift pack is about halfway", zelfde aanbodblok, "a pan that's covered for 75 years".
- Opbouw zoals de andere v3-mails: vaste header (lockup monogram + SIRAAT) en footer uit `partials/`, label, kop en subregel als live tekst (Instrument Serif), foto 3:2 zoals `w1v3-intro.jpg`, knop via `{{BLOCK:cta}}` met friction reducer, ondertekening Benjamin / Founder, Siraat. Geen codebalk (geen code). Geen reviews: er bestaat geen enkele review over de strips (content/products/.../reviews.md).
- UTM: `utm_source=klaviyo&utm_medium=email&utm_campaign=v4-mystery&utm_content=m1-hero|m1-cta1|m3-ps ...`; header en footer krijgen hun UTM in de Klaviyo-versie via build_template.py.
- Controle: 0 em dashes, `check_previews.py klaviyo/templates/v3/mystery` 0 problemen, geen horizontale scroll op 375 px, mobiel 2.064 tot 2.270 px hoog.

## 6. Verwacht volume

- M1: ongeveer 900 tot 1.050 per week (oude M1 1.066 tot 1.070; minus abonnees, herhaalkopers die WvRupU al kregen en refunds).
- M2: ongeveer 650 tot 850 per week (min overlap met P2 en uitschrijvers).
- M3 en M4: ongeveer 700 tot 900 per week elk.
- Omzet: oude flow $4.293 per 90 dagen (ongeveer $0,22 per ontvanger). Een abonnement is $20 per maand per klant, dus elke 100 abonnees is ongeveer $2.000 per maand terugkerend. Meten: Placed Order met `Items` contains "Plastic-Free Dishwasher Sheets" binnen 30 dagen na M3 plus Recharge-abonnementen (Recharge MCP `query_metrics`).

## 7. Open punten

1. **Beelden in Klaviyo** (23 okt): v2 van `m1-hero.jpg` t/m `m4-hero.jpg` staat in de Klaviyo-bibliotheek (`siraat-mystery-m*-hero.jpg`), URL's in `assets/klaviyo-urls.txt`, `m1.klaviyo.html` t/m `m4.klaviyo.html` gebouwd. Templates en flow nog niet in Klaviyo; daarvoor `qa_render.py` groen en akkoord Floris.
2. [VRAAG FLORIS] Recharge-portaal (skip/cancel) bevestigen, zie 2.
3. [VRAAG FLORIS] M4 aan of uit.
4. Ordered Product-event: `first_name` komt uit het profiel; checken in een Klaviyo-preview op een echt profiel dat `person.Country` gevuld is voor de prijsregel (anders loopt de zin zonder bedrag, geen fout).

## 8. Livegang, klikstappen voor Floris

Alleen na akkoord. Niets hiervan is gedaan.

1. Beelden uploaden en templates bouwen (open punt 1). Vier templates aanmaken in Klaviyo (CODE-editor, volledige HTML uit `m1.klaviyo.html` t/m `m4.klaviyo.html`), namen "v4 · Mystery · M1 reveal" enzovoort.
2. Flows > Create flow > Build your own > naam **"v4 · Mystery Gift"**. Trigger: Metric **Ordered Product** > Trigger filter: `ProductID equals 15785445622100`, OF-groep `ProductName equals Mystery Gift`.
3. Flow filters (sectie 3, punt 1 t/m 5). Re-entry: uit.
4. Time delay 3 days, "Delay until a specific time" 10:00, profile timezone > Email M1 (onderwerp A, A/B-test met B toevoegen) > in de mail: Additional filters > "Received Email where Flow equals v4 · Post-purchase (X3ySuU) zero times in the last 2 days".
5. Time delay 9 days tot 10:00 > Email M2 (zelfde additional filter).
6. Time delay 11 days tot 10:00 > Email M3 (A/B onderwerp; zelfde filter).
7. Time delay 7 days tot 10:00 > Email M4 (zelfde filter).
8. Elke mail eerst **Manual**, dan preview-sends naar Gmail met uniek onderwerp per send (PLAYBOOK 6). Na goedkeuring: elke mail op **Live**, A/B-tests met "Start test" starten.
9. WvRupU blijft **Draft** (niet archiveren, cijfers blijven nodig). De trigger van WvRupU niet herstellen.

## 9. Terugdraaien

- Flow "v4 · Mystery Gift" > statusmenu > **Draft** (of per mail op Manual). Profielen in de wachtrij krijgen dan niets meer. Niet verwijderen.
- Signalen om terug te draaien: uitschrijving per mail boven 1 procent, spam boven 0,1 procent, tickets "what are these sheets" of "cancel my subscription" die oplopen (Gorgias), of M1 die gelijk valt met een verzendmail en verwarring geeft.
- Er wordt geen code of korting aangemaakt, dus er valt in Shopify niets terug te zetten.
