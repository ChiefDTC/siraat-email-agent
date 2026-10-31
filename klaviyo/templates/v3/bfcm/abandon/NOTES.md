# BF 2026 abandonment-varianten (voorbeelden, niet live)

31 okt 2026. Restyle van de live abandonment-mails volgens het brand book ("Browse / cart / checkout abandon: add the yellow top bar and one ticket deal block above the product"), met het aanbod van Floris (31 okt): Black Friday Sale up to 70% off plus een extra 10% met code voor abandonment. Niets in Klaviyo, Shopify of Figma gewijzigd, niets gecommit, bronnen in `v3/checkout`, `cart`, `browse`, `site`, `browse-tp` ongewijzigd.

## Wat in elke mail hetzelfde is veranderd

1. **Topbar**: `bf-topbar` "BLACK FRIDAY SALE IS LIVE" (ink #272727, geel) boven `{{HEADER}}`. Dit vervangt de bestaande codebalk (`codebar`: HI10, gift-totaal of de eigen code met vervaldatum), omdat twee balken boven de header botsen. `tp-b2-clicked-nocode` had geen codebalk: topbar alleen toegevoegd.
2. **Deal-blok**: `bf-deal` "BLACK FRIDAY DEAL / Extra 10% off / On top of Black Friday prices, up to 70% off. Applied with the button, or use code BFCODE at checkout." direct boven het product- of cartblok (checkout: boven `BLOCK:cart`; cart en browse: boven de productkaart; site a1: boven de maatkiezer; a2: boven de eerste productkaart).
3. **Knoppen**: alle rust-knoppen (`BLOCK:cta`, #AC3B19) zijn `bf-cta` geel met ink tekst op een cream rij (#F8F7F2, de achtergrond van de mail). Label, link en friction reducer ongewijzigd.
4. **Code**: HI10 is overal weg. Placeholder `BFCODE` (repo is publiek, echte code pas bij upload invullen):
   - links `/discount/HI10?redirect=...` werden `/discount/BFCODE?redirect=...`;
   - checkout-links `responsive_checkout_url ... &discount=HI10` werden `&discount=BFCODE` (Shopify accepteert in `redirect` alleen een pad, dus de checkout-URL blijft de basis met `&discount=`); checkout-links zonder code (c4-nocode) kregen `&discount=BFCODE`;
   - winkel-links zonder code (cart-mails, nocode-mails) werden `https://siraatskitchen.com/discount/BFCODE?redirect=<oorspronkelijk pad>%3F<UTM's URL-gecodeerd>`; `/pages/`-links (garantie, labrapport) bleven direct;
   - tekst "HI10" (productkaart, maatkiezer, alt-teksten) werd "BFCODE".
5. **Prijzen**: vaste catalogusprijzen uit de v5-prijslijst (`{{PRICE}}`, `{{WAS}}`, `{{FROM}}`, inclusief "$X with HI10") zijn weggelaten, want die kloppen niet met de BF-prijzen. Prijzen uit het event (cart, checkout, bekeken product) blijven: die komen live uit Shopify.
6. **Fall sale eruit**: de gifts-regel "Your 4 gifts end when the fall sale ends." (`gifts5 urgency="1"`) is uitgezet. Het gifts-blok zelf blijft.
7. **Hero's met HI10 in de balk** (a1, a2, b1, b1-acc, b2-notclicked): nieuwe kopie `<naam>-hero-bf.jpg` met dezelfde foto en kop, balk "EXTRA 10% OFF · 4 FREE GIFTS". c3-p: nieuwe hero `c3p-hero-bf.jpg` (label BLACK FRIDAY, geen "THE FALL SALE"). Deze 6 beelden staan in `assets/klaviyo-urls.txt` met `https://UPLOAD-BIJ-EXPORT/...`: eerst uploaden, dan de URL invullen.
8. **Kopcommentaar**: nieuwe kop met BRON, SUBJECT_A, SUBJECT_B, PREVIEW en AANNAMES (de oude kop is weg, die noemde HI10; zie de bron). Preheader in de HTML = de nieuwe PREVIEW. `<!-- MARKET-SIGNAL -->` toegevoegd (checkout, cart, browse, profile voor site), omdat de builder het marktsignaal anders uit de mapnaam `abandon` haalt.

Structuur, productblokken, Klaviyo-variabelen, dynamische cart- en checkoutregels, reviews, gifts, sign-off en footer zijn ongewijzigd.

## Codemails (afwijking, besluit Floris nodig)

c4, k3, b2-clicked en tp-b2-clicked sturen een **unieke code** (C4_10_48H, K3_10_48H, B2_10_48H, 48 uur, router T02/CODE-cooldown). Daar blijft de unieke code in plaats van BFCODE: ook 10%, één code per order, en de mail zegt eerlijk "your own code ... 48 hours", wat met een publieke code niet meer waar is. Het `offer`-blok (code + deadline) is vervangen door het deal-blok met: "On top of Black Friday prices, up to 70% off. Applied with the button, or use your own code {% coupon_code %} at checkout, until <datum>." Alternatief: BFCODE ook hier, dan moeten onderwerp, hero en P.S. ("we're removing your discount") worden herschreven.

## Per mail

| BF-bestand | Bron | Flow en bericht dat het vervangt | Specifiek |
| --- | --- | --- | --- |
| c1-bf.html | checkout/c1.html | v4 · Checkout abandonment QUBUQV, C1 (U8Ngv8) | codebalk (gift-totaal) weg, deal boven cart, 2 knoppen |
| c2-bf.html | checkout/c2.html | QUBUQV, C2 (Syf9Si) | idem |
| c2-acc-bf.html | checkout/c2-acc.html | QUBUQV, C2-ACC (QZH3pZ) | idem |
| c3-s-bf.html | checkout/c3-s.html | QUBUQV, C3-S (Veb75W) | idem; bundelblok toont nog catalogusprijzen (zie open punten) |
| c3-p-bf.html | checkout/c3-p.html | QUBUQV, C3-P (W75UJK) | hero c3p-hero-bf.jpg, eyebrow "THE 6-PIECE SET" (was THE FALL SALE SET), tekst "In the 6-piece set", knop "Get the 6-piece set" (was "Upgrade to the 6-piece set", liep op 375 px over twee regels), regel "{{PRICE:set6*0.9}}" weg |
| c3-acc-bf.html | checkout/c3-acc.html | QUBUQV, C3-ACC (SL7UKX) | prijs uit productkaart weg |
| c4-bf.html | checkout/c4.html | QUBUQV, CODE · C4 (UdzWU2) | codemail: offer-blok door deal vervangen, unieke code blijft |
| c4-nocode-bf.html | checkout/c4-nocode.html | QUBUQV, C4 nocode cooldown + T02-B (SAqA6j) | checkout-links kregen &discount=BFCODE |
| k1-v2-bf.html | cart/k1-v2.html | v4 · Cart abandonment TZG9Mx, K1 (actie 119850627, template RXNZa3) | 6 /cart-links via /discount/BFCODE?redirect=, ook de restore-link /cart/VariantID:Qty |
| k1-acc-bf.html | cart/k1-acc.html | TZG9Mx, K1-ACC (Yt7LFd) | 4 links via BFCODE |
| k2-new-bf.html | cart/k2-new.html | TZG9Mx, K2-NEW (T72Ceu) | 4 links via BFCODE; bundelblok toont catalogusprijzen |
| k2-returning-bf.html | cart/k2-returning.html | TZG9Mx, K2-RETURNING (QTssZ3) | 6 links via BFCODE, "from"-prijzen deksel en Deep Pan weg |
| k3-bf.html | cart/k3.html | TZG9Mx, CODE · K3 pan/acc (Rz5KNx) | codemail, unieke code blijft |
| k3-nocode-bf.html | cart/k3-nocode.html | TZG9Mx, K3 nocode cooldown + T02-B (TBpqmc) | 4 links via BFCODE |
| b1-bf.html | browse/b1.html | v4 · Browse abandonment WdRz5k, B1 (VwGNp3, nu met A/B BR1 op variatie 119850692) | hero b1-hero-bf.jpg |
| b1-acc-bf.html | browse/b1-acc.html | WdRz5k, B1-ACC (TYaFUJ) | hero b1acc-hero-bf.jpg |
| b2-clicked-bf.html | browse/b2-clicked.html | WdRz5k, CODE · B2-CLICKED pan/acc (TwZq3f) | codemail, unieke code blijft |
| b2-clicked-nocode-bf.html | browse/b2-clicked-nocode.html | WdRz5k, B2-CLICKED nocode cooldown + T02-B (Uuxu3s) | 4 links via BFCODE |
| b2-notclicked-bf.html | browse/b2-notclicked.html | WdRz5k, B2-NOTCLICKED (TEeUzw) | hero b2-notclicked-hero-bf.jpg |
| a1-bf.html | site/a1.html | v4 · Site abandonment VLGhbR, A1 (SJBkFR) | hero a1-hero-bf.jpg; maatkiezer zonder prijzen, toont "10% off with BFCODE"; set6-kaart zonder prijs |
| a2-bf.html | site/a2.html | VLGhbR, A2 (SePNBv) | hero a2-hero-bf.jpg; productkaarten zonder prijs |
| tp-b1-bf.html | browse-tp/tp-b1.html | v4 · Browse abandonment · Triple Pixel QNZyEb, TP · B1 (121177227) | geen hero, deal boven het grote productblok |
| tp-b1-acc-bf.html | browse-tp/tp-b1-acc.html | QNZyEb, TP · B1-ACC (121177228) | Pan Pro-kaart zonder prijs |
| tp-b2-clicked-bf.html | browse-tp/tp-b2-clicked.html | QNZyEb, TP · CODE · B2-CLICKED pan/acc (121177250, 121177252) | codemail, unieke code blijft |
| tp-b2-clicked-nocode-bf.html | browse-tp/tp-b2-clicked-nocode.html | QNZyEb, TP · B2-CLICKED nocode (121177244, 121177247, 121177251, 121177258) | had geen codebalk; 3 links via BFCODE |
| tp-b2-notclicked-bf.html | browse-tp/tp-b2-notclicked.html | QNZyEb, TP · B2-NOTCLICKED (121177242) | deal tussen foto en productkaart |

Onderwerp en preview per mail staan in de kopcommentaar van elk bestand.

## Niet meegenomen

- Oude T01-armmails (Old · Checkout/Cart/Browse): de splits staan op 100% nieuw.
- BR1-variatie van B1 (RDeehg) en de UI-tests k4-installments (T23) en c5-installments (T24): A/B-varianten, geen vaste live mail.
- K1 (oude `cart/k1.html`): vervangen door k1-v2 (live sinds 10 okt).

## Aannames en open punten voor Floris

1. Aanbod: up to 70% off (collectie /collections/black-friday-sale) plus extra 10% met BFCODE; BFCODE moet stapelen op de saleprijzen. BFCODE bij upload vervangen door de echte code.
2. De 4 gifts ($70) en "Buy 2, get 4 free" bij de 6-delige set blijven in de mails staan. Klopt dat tijdens BF? Zo niet: gifts5-blokken en de set6-zinnen in c3-p, a1, a2 aanpassen.
3. Bundelblokken (c3-p, c3-s, k2-new) tonen nog setprijzen uit de v5-catalogus (bv. c3-p "Six pieces for $299 $598, bought one by one $562"). Die kloppen niet als de BF-prijzen anders zijn: catalogus in `scripts/v5lib.py` bijwerken of de prijsregel weghalen vóór upload. Niet aangepast, want dat raakt alle mails.
4. Nocode-mails (cooldown en T02-B) krijgen nu BFCODE. Als cooldown-ontvangers codevrij moeten blijven: deal-blok en BFCODE-links daar weghalen.
5. Codemails houden hun unieke code (zie boven).
6. De nieuwe hero's (6 beelden) moeten nog naar de Klaviyo-CDN; tot dan wijzen de `.klaviyo.html`-versies naar `https://UPLOAD-BIJ-EXPORT/...`.
7. Knoplabels als "Get 10% off this pan" en hero's met "10% off" blijven; in BF-context betekent dat de extra 10%.
8. UTM's ongewijzigd (utm_campaign v4-checkout enz.). Voorstel: `utm_term=bf26` om BF-verkeer apart te zien.

## Bouwen en previews

- Bouwen per mail (vanuit de scratchpad, met -I): `python3 -I scripts/build_template.py klaviyo/templates/v3/bfcm/abandon/<naam>-bf.html klaviyo/templates/v3/bfcm/abandon/assets klaviyo/templates/v3/bfcm/abandon/assets/klaviyo-urls.txt`. `assets/` bevat de assets van checkout, cart, browse, site en browse-tp; `klaviyo-urls.txt` is samengevoegd (eerste URL wint bij dubbele bestandsnamen, zelfde beeld).
- Varianten opnieuw maken uit de bronnen: `_tools/make_bf.py` (schrijft alleen in deze map).
- `previews/<naam>-bf-375.png` zijn screenshots op 375 px van de Django-gerenderde Klaviyo-versie (via de qa_render-contexten: checkout co_pan, cart atc_pan, browse vp_pan, site zonder event), niet van `-preview.html`. De `-preview.html`-bestanden tonen de Django-tags ongerenderd en worden daardoor 1.160 px of breder (ook bij de originele bronnen, bv. site/a1-preview.html). Gerenderd: alle 26 mails op alle qa_render-varianten zonder fouten, 375 px breed, geen horizontale overflow, 2.680 tot 3.810 px hoog (tp-b1 3.807, net boven de richtlijn van 3.600; het origineel was al lang).
- Gecontroleerd: 0 keer HI10 en 0 gedachtestreepjes in alle mailbestanden (`*.html`) van deze map; 22 van de 26 Klaviyo-versies bevatten BFCODE (de 4 codemails niet, die gebruiken hun unieke code).
