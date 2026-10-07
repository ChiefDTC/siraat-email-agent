# Bouwronde v4 · checkout (agent "checkout")

Datum: 7 oktober 2026. Map: `klaviyo/templates/v3/checkout/`. Hero-register: `content/media/hero-register/checkout.csv`.
Generator (alleen hulpmiddel, niet in de repo): scratchpad `checkout/gen.py` + `mails.py`; de bron-templates in de map zijn de waarheid.

## Wat er gebouwd is

| Mail | Onderwerp A | Hero (label / kop / subregel) | Mobiel (incl. footer) | Nieuwe onderdelen |
| --- | --- | --- | --- | --- |
| c1 | Something stop you at checkout? | YOUR CART IS SAVED / Right where you left it. / Free shipping. 4 gifts. 30-day returns. | 3.719 px (pan); 3.005 px (schort) | Vergelijkingstabel VT-A (alleen kookgerei, vervangt features); reviewregel Marilyn B. direct onder de knop |
| c2 | Has the pan in your cart actually been tested? | STILL COMPARING? GOOD. / Has it been tested? / Ours has. Report no. 25895. | 3.692 px | Geen nieuw blok; drie vragen + certificaat + bronvoetnoot. AI-flitsbeeld olive-oil |
| c2-acc | Yours, or a gift? Both work. | STILL IN YOUR CART / Yours, or a gift? Both work. / 30 days to change your mind. | ~3.250 px echt (preview 3.922 toont alle 7 accessoire-regels) | Gifts-blok toegevoegd; features-rij vervangen door korte cadeau-alinea |
| c3-p | One pan, or three for $349? | ONE PAN OR THREE / One pan, or three? / 3 pans + 3 lids, about $116 a pan. | 3.510 px | Productkaart 6-delige set (card-set6, geen SAVE); value stack 2.2 (alleen USD); rekensom "15 pans. Or one." AI-flitsbeeld three-pans |
| c3-s | $70 in gifts ship with your set | 4 GIFTS WITH YOUR SET / Every pan, one decision. / One 75-year warranty covers it all. | 3.703 px | Closer look 6-delige set (alleen als '6-Pcs' in de cart; anders features "Every piece, covered") |
| c3-acc | Most kitchens start with the pan | WHAT GOES WITH IT / Most kitchens start with the pan / No coating. Covered for 75 years. | 3.440 px | Productkaart Pan Pro: USD met SAVE $305 + BEST SELLER, andere valuta zonder prijs |
| c4-us | 10% off your cart, for 48 hours | LAST EMAIL ABOUT YOUR CART / Your cart, 10% less. / Your own code. 48 hours, then it ends. | 3.690 px | "Two promises" met reviews per belofte (Steven T. bij retour, Brandon W. bij garantie); 12-delige set als productkaart (US ONLY, SAVE $587) |
| c4-int | idem | idem, subregel "Your own code. Duties paid. 48 hours." | 3.472 px | Two promises; icons-int; geen 12-delige set |
| c4-us-nocode | Last reminder: your cart and 4 gifts | LAST EMAIL ABOUT YOUR CART / Still yours, if you want it. / Two promises come with it. | 3.456 px | Nieuw template (T02-B en cooldown). Geen code, geen HI10 |
| c4-int-nocode | idem | idem, subregel "Duties paid. Two promises come with it." | 3.304 px | Nieuw template |

Alle mails: codebalk, header/footer uit partials, hero met aanbodbalk, cart + knop boven de vouw (knop eindigt rond 735 px), friction reducer onder elke knop (12 px, één regel), iconen, gifts, reviews (alleen letterlijk Trustpilot uit reviews-positive-usable.csv of 04-rewrites, gecontroleerd met eigen script), drie knoppen, Benjamin. Onderwerp max 50, preview 40 tot 90 (gecontroleerd). Geen em dash, geen verboden woorden (grep), geen ontbrekende beelden, geen `[[`, `{{BLOCK`, `{%` in de previews.

Tailoring-test `research/tailoring/test/run_tests.sh`: alle 12 checkout-controles ok. Extra gecontroleerd met de test-render: c1 schort-tak (verzending/retour-alinea, service-reviews, geen pan-quote), c3-s set6-tak tegen features-tak, c4 garantiezin alleen bij kookgerei, c4-int zonder 12-delige set, c3-acc USD-prijs.
Variant-previews opnieuw gerenderd: `c1-preview-schort.html`, `c4-us-preview-schort.html`, `c2-acc-preview-plank.html`.

## Keuzes

- **UTM**: `utm_source=klaviyo&utm_medium=email&utm_campaign=v4-checkout&utm_content=<mailid>-<blok>` op elke link naar siraatskitchen.com (hero, cta1..3, offer, keep1/keep2, prod-set6, prod-panpro, set12, report). Checkout-links: achter `&discount=...`. `/discount/CODE?redirect=/pad`-links: UTM's URL-gecodeerd binnen `redirect` (`%3F`, `%26`), conform 04-utm 5.3b. Geen `utm_term` (de nocode-mail wordt zowel voor T02-B als voor cooldown gebruikt; een vaste `t02-b` zou cooldown verkeerd labelen).
- **Let op**: de brief zegt `v4-checkout`, v4-flow-system 1.1/1.5 en 04-utm zeggen `v3-checkout`. Ik volgde de brief. Gelijktrekken in Klaviyo `custom_tracking_params`.
- Header- en footerlinks (partials) hebben geen UTM; niet aangepast (buiten mijn grenzen).
- **-nocode**: v4 1.4 zegt "geen code; gift-stack, trekking, 30-day returns" en 3.15 "een unieke code vervangt HI10". Dus ook geen HI10 en geen `&discount` in de links. Codebalk toont "WITH EVERY ORDER · $70 IN GIFTS".
- **C2 zonder "independent"** (3.24 nog open): vraag 1 is nu "A lab report you can read?". Anatomie met laagdiktes (mm) is weggehaald (claim needs-proof); de oude `anatomy.jpg` met mm-labels wordt niet meer gebruikt.
- **C1 onderwerp**: 04-rewrites vervangt "Forgetting something?" door "Something stop you at checkout?". v4 T12: in fase 1 alleen A, geen test.
- **Wachttijden in SEND**: volgens v4 2.1 (C1 30 min, C2 24 uur, C3 dag 3 09:00, C4 dag 5 09:00 met code 48 uur).
- **C3-P zonder Pan Pro Duo** (plan noemde PK Duo SAVE $341): er is geen Duo-kaart in shared en een tweede upsell maakt de keuze diffuser. Wel productkaart set + value stack.
- **C3-P en gifts**: het gifts-blok is vervangen door de value stack, die dezelfde vier gifts met waarde noemt (06-offer-design 2.2), anders werd de mail 4.000+ px.
- **C4 12-delige set**: pill "US ONLY" in plaats van "BEST SELLER" (geen data dat de 12-delige een bestseller is).
- **C4 reviews**: in de Two promises-rijen (proof gematcht aan de belofte) in plaats van een los reviewblok; scheelt 400 px.
- Lid-prijs: "One Pan Pro + lid from $154" komt uit de actieve listing Titanium Hammered Pan Pro With Lid ($154-169).

## Open punten

1. **Lengte**: c1 (3.719), c2 (3.692), c3-s (3.703), c4-us (3.690) zitten 5 procent boven ~3.500 px, inclusief de footer van 546 px. Alle verplichte onderdelen plus het eigen idee passen niet onder 3.500 zonder iets verplichts te schrappen. Kandidaat om te schrappen als Floris korter wil: het iconenblok (131 px) dubbelt met de friction reducers.
2. **Gift-naam in het gedeelde gifts-blok**: `partials/blocks/gifts.html` zegt "Plastic-Free Home e-book", DECISIONS en het beeld zeggen "The Green Clean E-Guide". In de value stack van C3-P staat "The Green Clean e-guide". Blok aanpassen (niet mijn map).
3. **Beelden naar Klaviyo**: `assets/klaviyo-urls.txt` bestaat niet; daarom geen `.klaviyo.html`. Nieuw te uploaden: alle tien hero's (c1, c2, c2acc, c3acc, c3p, c3s, c4us, c4int, c4us-nocode, c4int-nocode), `certificate.jpg`, `anatomy-mobile.jpg` (niet meer gebruikt in c2, mag weg), `cart-fallback.jpg`.
4. **Ongebruikte assets** in de map: `anatomy.jpg` (met mm), `anatomy-mobile.jpg`, `egg-slide.gif`, `set6.jpg`, `set12.jpg`, `p-panpro.jpg`. Niet verwijderd.
5. `content/media/ai-flash/index.csv`: olive-oil-4x3-01 (c2) en three-pans-4x3-01 (c3-p) op "in gebruik" zetten (buiten mijn grenzen).
6. C4-code op een e-gift card (tailoring J4) en 75-jaar garantie op accessoires (3.27): garantiezin in C4 staat nu alleen bij kookgerei-carts.
7. "Light Labs" alternatieve rij 4 in VT-A: "Tested by Light Labs" tegen "Testing varies by brand" (rij "PTFE is itself a PFAS" niet gebruikt).
8. De fallback-URL van checkout-links (als `responsive_checkout_url` ontbreekt) krijgt `&discount=...&utm_...` achter `/discount/HI10?redirect=/cart`; daar landen de UTM's op de discount-URL, niet in de redirect. Alleen relevant zonder checkout-URL.
9. HI10-prijzen in C3-P en C3-acc zijn statisch ($314.10, $120.60); bij een prijswijziging in Shopify meeschrijven. De $349-set hangt aan de BDAY-listing (v4 3.20).
