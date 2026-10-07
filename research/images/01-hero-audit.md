# Hero-audit flow-mails v3 (7 oktober 2026)

Bron: `content/media/hero-register/*.csv`, de 30 hero's in `klaviyo/templates/v3/*/assets/*-hero.jpg` en mobiele renders in `*/previews/*-mobile.png`.

Methode
- Bronresolutie per hero nagemeten (pixels van de uitsnede tegenover de 1200 px die de hero nodig heeft). Factor boven 1,0 = opgeschaald.
- Scherptemeting: randvariantie (PIL FIND_EDGES) op de linker- en rechterstrook van de hero, buiten de tekst. Scherpe shoot-foto's scoren 700 tot 2400, de zachte beelden 37 tot 90.
- Visueel beoordeeld op contactvel en op mobiel (390 px breed).

## A. Zacht door opschaling (chef-video-stills, uitgesneden boven ingebakken ondertitels)

| Mail | Bron | Uitsnede | Opschaling | Scherpte | Reden |
| --- | --- | --- | --- | --- | --- |
| w0 | chef-video/still-egg-in-pan.jpg | 520x520 | 2,3x | 46 | Wazige close-up, geen onderwerp herkenbaar, video-compressie zichtbaar |
| w4-int | chef-video/still-pan-top.jpg | 545x545 | 2,2x | 80 | Vlakke grijze pan, zacht, geen mens, geen sfeer |
| p2 | chef-video/still-egg-close.jpg | 540x540 | 2,2x | 58 | Chef in beeld maar zacht; schort-logo (monogram) staat midden achter de subregel |
| p3-pan | chef-video/still-dishwasher.jpg | 540x540 | 2,2x | 37 | Zachtste hero van alle 30; uitgesneden om "HEAT ON MEDIUM" te ontwijken |
| p3-accessory | chef-video/still-steak.jpg | 540x540 | 2,2x | 88 | Zacht, steak bruin op bruin, kop valt weg in de middentoon |
| b2-clicked | chef-video/still-egg-slide.jpg | 720x540 | 1,7x | 50 | Zacht; hand en ei precies achter de kop |
| b2-notclicked | chef-video/still-oil-shimmer.jpg | 746x560 | 1,6x | 69 | Zacht; chefgezicht precies achter de kop "In their words" |
| k3 | chef-video/still-steak-sear.jpg | 600x450 | 2,0x | 82 | Zacht en bruin; laatste cart-mail met deadline verdient een sterk beeld |

## B. Niet in flitsstijl en (licht) opgeschaald (Shopify-stock)

| Mail | Bron | Reden |
| --- | --- | --- |
| p1-first | Shopify 7d6b1b9a...jpg (1344x768, vierkant 768 px, 1,6x) | Zacht (243), daglicht-stockgezin, geen Siraat-product zichtbaar, kinderen achter de tekst |
| p1-repeat | Shopify chopstickssiraat.webp | Zacht (276), daglicht, generiek stockgevoel, gezicht in de bovenrand |
| p3-set | Shopify 1.9.png | Daglicht-stock, koppel met gezichten achter de kop, keukenrommel achter de subregel |
| r1-set | winback/src/Pan_LF_13.jpg | Zacht (258), grijze productopstelling op marmer, planken achter de kop, geen mens |

## C. Dubbel of bijna-dubbel tussen of binnen flows

| Mails | Probleem |
| --- | --- |
| c3-s en c3-p | Zelfde shot (P02 / P022 GasRange) twee keer in de checkout-flow; in strijd met PLAYBOOK 10 ("nooit twee keer dezelfde in één flow") |
| w1-a, w1-b en w4-us | w1-a en w1-b delen P04 (A/B, acceptabel); w4-us (P03) is dezelfde opstelling (steak, coquilles, pan) en oogt als dezelfde foto in dezelfde flow |
| c2 en w3 | Beide een hamerslag-close-up (P11-A en P11-E) met vrijwel dezelfde kop ("Tested. ..."); wie welcome en checkout krijgt ziet twee keer hetzelfde |
| k2-returning, c4-int | Ook hamerslag- en randclose-ups (P11-B, P11-C); vier van de dertig hero's zijn dezelfde grijze pan-close-up |
| b1 en w5 | P09-B en P09-A: zelfde set (pan met deksel, ei/omelet, granieten aanrecht) in browse en welcome |

## D. Rommelig achter de tekst (scherp, maar leesbaarheid of merk lijdt)

| Mail | Probleem |
| --- | --- |
| k2-new | Gegraveerd handvat met merktekst loopt schuin door de kop "$1.79 a year" |
| r1-pan | Monogram-onderzetter en verpakking met logo achter de kop: twee logo's in één beeld, rommelig |
| c1 | Drukke fornuisopname, deksel en pannen achter de kop (scherp, wel leesbaar dankzij de laag) |
| k1 | Hand met spons en pan midden achter de subregel |

## Prioriteit voor nieuwe basisbeelden

1. Groep A (8 mails): grootste kwaliteitswinst, allemaal zichtbaar zacht op desktop.
2. Groep B (4 mails): stijlbreuk, nu het enige "daglicht-stock" in de flows.
3. Groep C: c3-p, w4-us en c2 vervangen (3 mails), zodat elke flow alleen unieke beelden heeft.
4. Groep D: k2-new (1 mail). c1, k1 en r1-pan blijven voorlopig (scherp, echte shoot; r1-pan kan later).

Totaal 16 mails voor nieuwe beelden: 10 vierkant (w0, w4-int, w4-us, p1-first, p1-repeat, p2, p3-pan, p3-accessory, p3-set, r1-set) en 6 in 4:3 (b2-clicked, b2-notclicked, k3, k2-new, c2, c3-p).

Niet vervangen: b1, k1, k2-returning, c1, c3-s, c4-us, c4-int, w1-a, w1-b, w3, w5, r1-pan, r2, r2-vip (scherpe echte shoot- of productfoto's; echte foto blijft voorrang houden boven AI).
