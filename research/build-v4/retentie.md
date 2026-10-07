# Bouwronde v4 · retentie (winback, VIP, anniversary)

Datum: 7 oktober 2026. Agent: retentie. Mappen: klaviyo/templates/v3/winback, vip, anniversary. Hero-registers winback.csv, vip.csv, anniversary.csv bijgewerkt.

## Mails (13)

| Mail | Onderwerp A | Hero-kop | Mobiel | Nieuwe onderdelen |
| --- | --- | --- | --- | --- |
| r1-pan | How's your pan doing? | What goes next / to your pan. | 3.536 px | productkaart Roasting Pan (alleen US, zonder NEW-sticker) |
| r1-set | The shapes a set leaves out | The shapes / a set leaves out. (AI-flitsbeeld full-stove) | 3.446 px | geen; rijen verdwijnen als de set dat stuk al heeft |
| r1-acc | Ready for the pan? | Ready for / the pan? | 3.694 px | closerlook Pan Pro + productkaart Pan Pro (SAVE $305 en BEST SELLER alleen US) |
| r2 | 10% off your next piece, for 72 hours | Your next / piece. | 3.800 px | "Two promises" (risk reversal, laatste mail) |
| r2-nocode (nieuw) | Ready for pan number two? | Your next / piece. | 3.428 px | codebalk zonder code |
| r2-vip | For our regulars: 15% for 72 hours | You came back. / Here's 15%. | 3.833 px | "Two promises" |
| r2-vip-nocode (nieuw) | You came back. Thank you. | You came back. / Thank you. | 3.477 px | codebalk zonder code |
| v1 | Twice is a habit. Here's 15% off. | Twice is / a habit. | 3.752 px | geen |
| v1-nocode (nieuw, HI10) | Twice is a habit. Thank you. | Twice is / a habit. | 3.649 px | geen |
| v2 (tekst) | A question from Benjamin | geen hero | 1.391 px | P.S. op profieleigenschap last_flow_code_pool |
| n1 | How's your pan at six months? | Half a year / on titanium. | 3.236 px | geen |
| n2 | One year ago this week | A year on / titanium. | 3.837 px | geen |
| n2-nocode (nieuw) | One year ago this week | A year on / titanium. | 3.418 px | codebalk zonder code |

Topcomment per mail: SUBJECT_A, SUBJECT_B, 5 onderwerpen (één per type), PREVIEW, SEND (45/75 dagen, 30+10 dagen, 182/365 dagen, tot 09:00), FILTERS volgens v4, UTM.

## Wat veranderd is

- Copy volgens 04-rewrites (R1, R2, R2-VIP) en de skill; "two months" vervangen door "six weeks" (R1 gaat nu op dag 45). Geen "why titanium"-uitleg; wel wat past bij wat ze hebben.
- "NEW" weg bij 2 Pans + 2 Lids (alleen waar als het product na hun order verscheen). Roasting Pan: PDP zegt op 7 okt nog "100-day trial · Lifetime warranty · Free express shipping" en "covered by a lifetime warranty" (live gecontroleerd), dus kaart zonder NEW-sticker. Eigen kaartbeeld zonder sticker: winback/assets/card-roast.jpg (kopie van de packshot, wit gemaakt).
- Prijzen overal alleen bij verzendland US (`event.extra.shipping_address.country_code == 'US'`), ook in r2, r2-vip, v1, n1, n2 (open punt uit tailoring 04).
- Deksel-rij alleen als de order geen "Lid" bevat (r1-pan, v1, n1, n2). r1-set: crepe, wok en utensils verdwijnen als de set ze al bevat.
- 6-delige set linkt overal naar `...-6-pcs-bday-sale` ($349); v1 en n2 linkten nog naar de $399-listing.
- n1: "high heat" weg (verboden), tekst nu "carbonized oil, not a defect" (facts.csv).
- Reviews: allemaal letterlijk uit reviews-positive-usable.csv, behalve Don J. (R547) die uit 04-rewrites komt. Gecontroleerd met een eigen script (check_reviews.py leest alleen 04-rewrites): letterlijk, 5 sterren, max 120 tekens, paarverschil max 30.
- -nocode-varianten: r2 en r2-vip en n2 zonder code en zonder HI10 (v4 1.4: "geen code; gift-stack, 30-day returns"), codebalk als live tekst "FREE SHIPPING · $70 IN GIFTS WITH EVERY ORDER". v1-nocode met HI10 (v4 2.9).

## UTM (gekozen werkwijze)

`utm_source=klaviyo&utm_medium=email&utm_campaign=v4-<flow>&utm_content=<mailid>-<blok>` (+ `utm_term=t02-a` op codemails, `t02-b` op -nocode). Mail-ID's zonder koppelteken (r1pan, r2vip, ...). Blokken: hero, cta1..3, offer, prod-<kort>.
Bij `/discount/CODE?redirect=/pad` staan de UTM's **binnen redirect, achter het pad**, met `?`, `=` en `&` gecodeerd als `%3F`, `%3D`, `%26`. Directe links (nocode, v2, n1-zorglinks) krijgen gewone `?utm_...`.
Let op: v4-flow-system.md en 04-utm.md zeggen `v3-<flow>`; de brief van deze ronde zegt `v4-<flow>`. Ik volgde de brief. Gelijktrekken met de andere agents.

## Previews

`<id>-preview.html` is na build_template.py nog door Django gerenderd met een voorbeeld-event (US-pankoper; r1-set een US-set, r1-acc een US-plank, v2 met pool SK_REGULARS15_14D), zodat de PNG's geen ruwe `{% if %}`-tags tonen. Bronbestanden en .klaviyo.html zijn ongewijzigd door die stap. Gecontroleerd: geen ontbrekende beelden, geen em dash, geen resttags, alle links met UTM, takken US/INT en wel/geen deksel.
run_tests.sh: alle 4 winback-controles ok.

## Open punten

1. Lengte: r2, r2-vip, v1, n2 en r1-acc zitten op 3.650 tot 3.840 px (doel ~3.500). Alles wat de brief verplicht staat erin (codebalk, hero, knop, offer, producten, gifts, reviews, iconen, 3 knoppen, Benjamin) plus de footer van ~550 px. Inkorten kan door in R2/R2-VIP de "Two promises" weg te laten (−180 px), maar de skill wil die in de laatste mail.
2. Roasting Pan: Gorgias-guidance 8566447 zegt nog "not available for purchase yet", Shopify ACTIVE met 270 voorraad. Kaart staat erin (alleen US); als Floris hem niet wil: rij weghalen. Zodra de PDP is bijgewerkt kan `card-roast-new.jpg` (shared) terug.
3. n1 heeft geen aanbodbalk in de hero (service-mail, v4 2.10) terwijl de brief "altijd aanbodbalk" zegt. Bewust zo gelaten.
4. v2 P.S. gebruikt `person|lookup:'last_flow_code_pool'`; in Klaviyo één keer testen met een profiel. Als de terugval "CODE ·"-berichtnaam wordt gebruikt (v4 1.4), werkt deze voorwaarde niet en moet de P.S. neutraal.
5. -nocode-mails krijgen ook ontvangers via de cooldown, niet alleen T02-B; die tellen dan mee onder utm_term=t02-b. In Klaviyo de cooldown-tak eventueel een eigen kopie met `utm_term=cooldown` geven.
6. Hero's 238 tot 290 KB (r1-acc 290 KB); QA-grens was 250 KB. make_hero.py bepaalt de compressie.
7. Bug/beperking blokken: `{{BLOCK:productcard}}` laadt het beeld altijd uit `{{SHARED}}`, dus een eigen kaart in de flowmap kan niet via het blok; ik heb dezelfde opmaak inline gezet. Ook berekent build_template `washtml` zelf, waardoor het blok niet zonder `was` te sturen is. Voorstel: parameter `src="IMG"` in het blok.
8. Uploaden naar Klaviyo en `assets/klaviyo-urls.txt` aanvullen (hero's, p-*.jpg, card-roast.jpg) staat nog open; daarom alleen v2.klaviyo.html.
