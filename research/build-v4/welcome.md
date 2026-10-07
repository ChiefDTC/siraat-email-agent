# Bouwronde v4 · Welcome (agent "welcome")

Datum: 7 oktober 2026. Map: `klaviyo/templates/v3/welcome/`. Niets in Klaviyo, Shopify of Figma gewijzigd, niets gecommit.

## Wat er veranderd is (alle 8 mails opnieuw)

Lijn over de hele flow: hetzelfde aanbodkaartje (`{{BLOCK:offer}}`, "YOUR WELCOME OFFER · 10% on top of the sale · HI10") in elke prospect-mail, ook W2; het verhaal wisselt per mail. Aanbod staat in codebalk, aanbodbalk van de hero en de knop direct onder de hero (knop eindigt rond 600 px op mobiel); de hero-kop draagt het idee. Onder elke primaire knop een friction reducer.

| Mail | Onderwerp A (B) | Hero-kop | Mobiel | Nieuw |
| --- | --- | --- | --- | --- |
| w0 | Thank you. Now the first egg. (2 to 3 minutes on medium. Then the egg.) | First heat, then oil. | 2.933 px | AI-flitsbeeld egg-crack, opener uit 04-rewrites, eerlijke verwachting met Sandi R. (R143), Card Game-regel |
| w1-a | The pan with nothing on it (and your 10%) (Your 10% is inside (plus $70 in gifts)) | The pan with nothing on it. | 3.452 px | Idee-eerst: "Nothing on it to wear off." (coating slijt, titanium cooking surface, 20 dec 2024); Card Game in één regel; aanbodkaartje met mini-stack ($439 / $134 / $120.60); gifts-kop "$70 in gifts, included" |
| w1-b | idem (T04: zelfde onderwerp, preview, hero en volgorde) | idem | 3.467 px | Gift card + knop met "Not a cash card: it applies at checkout." |
| w2 | The pan nobody else was making (December 20, 2024) | (tekstmail) | 2.335 px | Benjamin-tekst uit 04-rewrites met drie gele [VRAAG FLORIS]-plekken, link naar rapport, aanbodkaartje onder de P.S. |
| w3 | Has your cookware actually been tested? (Report no. 25895: what it says) | Tested. Not claimed. (hero ongewijzigd) | 3.943 px | Closer look Pan Pro ("WHAT WAS TESTED"), drie vragen zonder "independent" (nu "ISO/IEC 17025-accredited"), certificaat met "Read it yourself", oude tekst-tabel weg |
| w4-us | Who are you cooking for? (Start with the Pan Pro (10% off already applied)) | Who are you cooking for? | 4.220 px | Volgens demo: closer look Pan Pro, maatkiezer, drie productkaarten met stickers (SAVE $305, set 6, SAVE $587), reviews Emma + Tammy (nieuw), AI-flitsbeeld pasta-lift |
| w4-int | Who are you cooking for? (Start with the Pan Pro (your 10% inside)) | Who are you cooking for? | 3.995 px | Zelfde zonder USD en zonder 12-delige set; kaarten Pan Pro (BEST SELLER-sticker, geen $-sticker) en 6-delige set; aanbodbalk "4 GIFTS"; AI-flitsbeeld two-sizes |
| w5 | Tammy is on her fourth pan (The last note about your 10%) | Skeptical first. Then the egg. | 3.734 px | Reviews als drie mini case studies (Michael G. R169, Fran G. R553, Tammy R138) met labels BEFORE / THE TEST / NOW; gifts; productkaart Pan Pro SAVE $305; "two promises" in de afsluiting |

Geen -nocode-varianten: v4 noemt er geen voor welcome (alleen HI10, besluit A). Geen `{% if %}`-logica in welcome; tailoring-tests slagen (44 ok, 0 fout).

## Werkwijze links (UTM)

- Alle HI10-links: `https://siraatskitchen.com/discount/HI10?redirect=<pad>%3Futm_source%3Dklaviyo%26utm_medium%3Demail%26utm_campaign%3Dv4-welcome%26utm_content%3D<mail>-<blok>` (UTM binnen redirect, `?` en `&` gecodeerd als %3F en %26, het pad zelf ongecodeerd).
- Gewone links (care-use, third-party-testing, deksel): `?utm_source=klaviyo&...` direct achter het pad.
- `utm_content`: w0, w1a, w1b, w2, w3, w4us, w4int, w5 met hero, cta1..3, offer, giftcard, size-mini/small/standard/large, tier1..3, prod-panpro, prod-lid, report. W1-A/B hebben `utm_term=t04-a` / `t04-b`.
- Header en footer (partials) hebben geen UTM in de HTML: die vangt Klaviyo's custom tracking params.

## Controles

- Mobiel exact 390 breed, geen ontbrekende lokale beelden, geen `[[`, `{{BLOCK`, em dash of verboden woorden (script in mijn scratch-map).
- Reviews: elke quote letterlijk (alleen ingekort met "...") uit `content/reviews/reviews.csv`, allemaal Trustpilot, 5 sterren; usable-lijst of 04-rewrites. Max 120 tekens, paarverschil binnen 30. Michael G. zonder het deel met de concurrentnaam.
- Onderwerpen max 50, previews 40 tot 90 tekens.
- Hero-register `content/media/hero-register/welcome.csv` bijgewerkt.

## Open punten

1. **Lengte**: w3 (3.943), w4-us (4.220), w4-int (3.995) en w5 (3.734) zitten boven ~3.500 px. Oorzaak: closer look (ca. 620 px mobiel) plus maatkiezer, kaarten, aanbodkaartje en reviews die de brief alle vier vraagt. Inkorten kan door in W4 de derde productkaart of in W3 het certificaatbeeld te schrappen. Keuze aan Floris.
2. **utm_campaign**: de brief zegt `v4-welcome`, v4-flow-system 1.5 en research/testing/04-utm.md zeggen `v3-welcome`. Gebouwd met `v4-welcome`; Klaviyo's custom tracking params moeten dezelfde waarde krijgen.
3. **W2 gaat niet live** voordat de drie [VRAAG FLORIS]-plekken (eigen scène, waarom van snijplank naar pan, hoe lang het duurde) door Benjamins echte verhaal zijn vervangen. "Often me" is weggelaten tot bevestigd is dat Benjamin replies leest (OVERZICHT vraag 30).
4. **Gifts-blok** niet in W3 en W4 (lengte); daar staat "Plus $70 in gifts with every order" in het aanbodkaartje. W4-INT noemt "4 gifts" zonder dollarbedrag (06-offer-design: INT geen dollars).
5. **W1 test T04**: beide armen krijgen onderwerp A; onderwerp B is voor T05b (fase 2).
6. **Productkaart-blok (bug/beperking)**: `blocks/productcard.html` en `closerlook.html` laden beelden altijd uit `{{SHARED}}/`; een kaart uit de eigen assets-map kan niet zonder blokwijziging. Ik heb alleen bestaande gedeelde kaarten gebruikt. Voor W4-INT is de `SAVE $305`-sticker bewust niet gebruikt (dollarbedrag voor niet-US); dus `card-panpro-bestseller.jpg`.
7. **Maatkiezer US** toont de huidige prijs doorgestreept met de HI10-prijs eronder (zoals de demo). Mini, Small en Large hebben geen compare-at in Shopify; de doorgestreepte waarde is dus de eigen verkoopprijs, geen anker. Akkoord laten geven of de streep weghalen.
8. **"Lighter than cast iron"** komt alleen voor als klantquote (niet gebruikt in deze ronde); "a now officially" in Michael G. is letterlijk (typfout van de klant).
9. W0: GIF's zijn 780 en 589 KB (QA A7 noemde 1,5 MB in totaal); ongewijzigd.
10. Beelden nog naar de Klaviyo-bibliotheek en `assets/klaviyo-urls.txt` (bestaat nog niet), daarna `build_all.sh welcome` voor de `.klaviyo.html`.
