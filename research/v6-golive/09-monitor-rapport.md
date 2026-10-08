LIVE: JA, NA DEZE 9 FIXES

# 09 · Monitor-rapport v5-testrun (8 oktober 2026, 21:35 tot 00:25 Amsterdam)

Monitor-agent. Bewaakt: lolagroothuis@gmail.com en alle plus-aliassen. Per v5-mail gecontroleerd met `scripts/qa_inbox.py mail` (mail_checks: onderwerp, preheader, afzender, grootte, links, UTM, linktekst, beelden, tags, markt, header/footer, afmelden, em dash, layout 375/600/1200, dark mode) plus handmatig: inhoud, product, cross-sell, code en vervaldatum, rekensommen tegen de winkel, kortingscode in een echte winkelwagen (cart.js, niet afgerekend). Per mail één Slack-bericht in #claude-mail (plus twee correctieberichten). Log per mail: `research/v6-golive/08-monitor-log.csv`. Screenshots en rapport per mail: `exports/qa/inbox/<alias>-<mail>/` (375, 600, 1200 px licht, 375/600 dark, 375 geforceerd donker).

Werkwijze en beperking: de proxy blokkeert klclick (tracking) en kmail-lists (web-view, afmelden). De eerste mail is als ontvangen HTML uit Gmail getest; daarna is elke mail opnieuw gerenderd uit de Klaviyo-template van precies dat flowbericht met het echte trigger-event en profiel (GET, alleen lezen) en tekstueel vergeleken met de ontvangen mail (P1: 100 procent gelijk). Codes uit de echte Coupon Assigned-events. Waar de render afweek (K1, R1) is de echte Gmail-tekst leidend geweest.

## 1. Verwacht tegenover ontvangen

47 v5-mails ontvangen, allemaal beoordeeld. Vertraging: de testflows hebben 3 tot 4 minuten wachttijd, in de praktijk kwam het volgende bericht 4 tot 39 minuten later (Klaviyo-verwerking, geen mailfout).

| Alias | Scenario | Verwacht | Ontvangen | Opmerking |
|---|---|---|---|---|
| +order | order Pan Pro Standard (US) | P1, P2-SAFE, P3 (code), R1, R2, N1, N2 | P1, P2-SAFE, CODE · P3-PAN | Winback en Anniversary niet gestart: die testflows gingen 6 tot 16 seconden vóór de order live, de order (19:35:04) viel nog buiten de trigger. Testartefact. Reserve +order2 is niet besteld. |
| +vip | order 1 Crêpe Pan Pro, order 2 Deep Pan Pro | P1, P2-SAFE, P3, R1, R2, N1, N2, V1, V2 | P1, P2-SAFE, N1, R1 (2x), CODE · R2-VIP, CODE · V1, V2 | P3 terecht overgeslagen (order 2 na flowstart). Geen P1-REPEAT (30-dagenfilter, klopt). **N2 nooit ontvangen** (zie H4). R1 dubbel en V2 vóór V1: testartefact van de korte wachttijden. |
| +sunset | testlijst | S1, S2 | S1, S2 | afzender S2 Benjamin |
| +sunsetkept | testlijst | S3, S4 | S3, S4 | afzender Benjamin |
| +welcome | welcome US variant A | W1 tot W5 | W1-A, W2, W3, W4-US, W5 | plus Site A1, A2 (site-test) |
| +welcomeabtb | welcome US variant B | W1-B, W2 tot W5 | W1-B, W2, W3, W4-US, W5 | A/B-split werkt |
| +welcomeint | welcome UK | W1, W2, W3, W4-INT, W5 | W1-A, W2, W3, W4-INT, W5 | plus Cart K1, K2-NEW, CODE · K3 (cart-test) |
| +pan | checkout Pan Pro (US) | C1, C2, C3-P, C4 | C1, C2, C3-P, CODE · C4 | T01 nieuw, T02 code |
| +set | checkout fall-set (US) | C1, C2, C3-S, C4 | C1, C2, C3-P, CODE · C4 | Het Checkout Started-event bevat een Pan Pro Standard, geen set. Mails kloppen met het event; de set-tak C3-S is niet getest. |
| +uk | checkout Pan Pro (GBP) | C1, C2, C3-P, C4 | C1, C2, C3-P, CODE · C4 | UK volledig goed: £, 28 cm, £55 gifts, duties paid, geen termijnregel |

Geen double opt-in-mail ("Confirm Your Subscription") voor +pan, +set of +uk. Alleen de bekende van 19:31 voor +order en +vip.

## 2. Fouten per ernst, met fix

Tijdens de run zijn de templates van alle Draft-flows en de meeste TEST-flows om 20:29 tot 20:45 UTC bijgewerkt (door een andere agent). Daardoor zijn L1 tot L4 in de echte Draft-flows al opgelost; ze bleven zichtbaar in de TEST-welcomeflow (templates van 19:57). Alles hieronder is nagelopen tegen de huidige Draft-templates.

### Hoog (blokkeert livegang)

**H1. Unieke codes verlopen niet, terwijl de mail "we're removing your discount" belooft.** Alle 8 uitgegeven codes (THX-XXXXXXXX, REG-XXXXXXXX, VIP-XXXXXXXX, CO-XXXXXXXX, CO-XXXXXXXX, CO-XXXXXXXX, CART-XXXXXXXX) hebben in Shopify `endsAt: null` en in Klaviyo CouponExpirationDate 2027-10-08, terwijl de mails 48 uur, 72 uur of 14 dagen noemen met datumtegels. Dat is onware urgentie en botst met het besluit "dat is waar, de unieke code vervalt". Fix: in Klaviyo bij elke coupon (C4_10_48H, K3_10_48H, B2_10_48H, R2_10_72H, R2_VIP_15_72H, P3_THANKYOU_10_14D, SK_REGULARS15_14D, SK_ANNIV15_7D, UGC) de vervaltermijn na toewijzing zetten (openstaand punt in OVERZICHT-V5 §8), daarna één nieuwe testcode in Shopify Admin controleren op een einddatum.

**H2. Lege cross-sell en ontbrekend dekselblok door `siraat_owned`.** In N1, R1 (2x), CODE · P3-PAN, CODE · V1 en CODE · R2-VIP staat de kop van het cross-sellblok ("Still on our list for your kitchen", "Goes with your crêpe pan", "Picked for your kitchen") zonder één product eronder (bevestigd in de echte Gmail-tekst van R1). In P1 ontbreekt het blok "ONE SIZE NOTE" (28 cm-deksel). Oorzaak: `person|lookup:'siraat_owned'` bestaat niet bij een klant die nog niet gesynct is; Klaviyo evalueert `'x' not in <leeg>` dan als onwaar en sluit alles uit (met een lege string verschijnen Pan Pro 11″, plank en utensils wel). Live raakt dit elke klant tussen order en nachtelijke sync (P1 altijd) en elk profiel dat de sync mist. Nog aanwezig in de Draft-flows (X3ySuU, UyFc78 gecontroleerd). Fix: in alle xsell/lid-blokken `{% with ow=person|lookup:'siraat_owned'|default:'' %}` (of `{% if not ow or 'lid_28' not in ow %}`), opnieuw exporteren.

**H3. Code breekt op mobiel over twee regels.** In elk codeblok (P3, V1, R2-VIP, C4, K3) staat de code op 375 px op twee regels ("CO-4PJ38LF" / "C"), op 1200 px op één. Fix: mobiele CSS `.offer-code{font-size:22px!important;letter-spacing:2px!important;white-space:nowrap}` (nu 26px/4px) en op 320 px nameten.

**H4. Anniversary N2 kwam niet aan bij +vip.** Verwacht rond 21:45 (N1 21:41). Geen Received Email, geen Coupon Assigned. De codepool SK_ANNIV15_7D werd in Shopify pas om 21:46:14 aangemaakt, precies op het verzendmoment (nu 101 codes). Waarschijnlijk is de eerste verzending overgeslagen omdat de pool nog leeg was. Fix: N2 hertesten (+order2 of preview met echte Send) nu de pool bestaat; tot die hertest is N2 niet bewezen.

### Middel

**M1. V2 P.S. noemt HI10 vlak na de 15% VIP-code.** "HI10 still takes an extra 10% off your next order" komt minuten (live: 10 dagen) na V1 met eigen 15%, en HI10 is één keer per klant. Fix: P.S. in v2 laten verwijzen naar de eigen 15%-code of weglaten.

**M2. K2-NEW "What the warranty covers" opent een pagina die "lifetime warranty" zegt**, de mail en DECISIONS zeggen 75 jaar. Fix: /pages/warranty in Shopify naar 75 jaar, of de link naar /policies/refund-policy.

**M3. P3-PAN "Add the lid, 10% off" opent de dekselpagina zonder variant** terwijl de tekst "Your 11″ Pan Pro takes the 28 cm lid" zegt. Fix: `?variant=52401107239252` (28 cm) per panmaat, zoals de cross-sell al doet.

**M4. W1 codebalk "YOUR WELCOME 10%% · CODE HI10"** (dubbel procentteken, zichtbaar in de Gmail-preview) in de TEST-welcometemplates WVXPLp en Y7nEEf. In de Draft-flow T4a5Mk (bijgewerkt 22:45 Amsterdam) zit het niet meer. Fix: TEST-welcome opnieuw koppelen en W1 A en B één keer echt ontvangen.

**M5. W2 P.S. "our The Green Clean E-Guide"** (dubbel lidwoord), drie keer ontvangen. Fix: "our" weghalen in w2.

**M6. Footer toont "SIRAATSKITCHEN" als bedrijfsnaam** (Klaviyo organization name), ook in de nieuwe templates (K1 om 23:14). Fix: Klaviyo Account > Organization name "Siraat's Kitchen".

### Laag of opgelost tijdens de run

- **L1 tot L4, opgelost in de Draft-templates om 22:29 tot 22:45**: header ABOUT naar /pages/faq, Facebook naar oude URL, Unsubscribe en View in browser 2,4:1 contrast op de donkere footer, zwarte lockup onzichtbaar in geforceerde dark mode. In C1 tot C4, K1 tot K3, A1, A2 en de hergerenderde P1 en R1 zijn ze weg. Nog wel in de TEST-welcomeflow; bij hertest controleren.
- P2-SAFE: GIF van 559 KB (totaal 889 KB beeld). Lichter maken of statisch beeld op mobiel.
- Doorgestreepte compare-at bij de sets ($598, £498, $1,186): open punt draaiboek 2.2, Floris beslist.
- Cart (K1 tot K3) bij profiel UK maar EU-IP toont €: volgens ontwerp (cart = IP-land). Overweeg profielland voorrang te geven als dat gevuld is.
- K-mails: knop "Finish my order" opent de PDP, niet de cart (bewuste keuze). Knoptekst "Back to my pan" of cart-permalink.
- K3-onderwerp "We're removing your cart's 10%", besluit noemde "your discount".
- W5 reviewcitaat "this is a now officially my favorite pan" (typfout in het citaat).
- Een nieuwe unieke code werkte ongeveer 1,5 minuut na ontvangst nog niet in de winkel, een minuut later wel.
- Recover-links (C1 tot C4) sturen zonder cookie door naar Shop Pay (shop.app) met discount_code; niet verder te volgen door de proxy, handmatig in een browser nalopen.
- P1-e-booklink gaat in de nieuwe template naar delivery.shopifyapps.com (download); niet te openen vanuit deze omgeving.
- Site-testflow sluit welcome-testflow VHtuLj uit, niet de testlijst-welcome SrAYTK; daardoor kreeg +welcome A1/A2 tijdens de welcome-reeks. Live sluit de site-flow T4a5Mk uit, dus testartefact.

Wat goed was (steekproef van wat expliciet is nagerekend): alle prijzen gelijk aan de winkel (US $99/$137/$144/$149, set $299, 12-delig $599; UK £109/£119/£124/£129, set £249, deksel £29/$59), alle HI10-bedragen en rekensommen ($562, $269,10, £444, £224,10), HI10 en elke unieke code geven echt korting in de winkelwagen, UK-mails zonder $ of inch met duties paid, US-mails met "Free shipping from the US" en termijnregel, geen em dash, geen ongerenderde tags (behalve M4), alle mails onder 102 KB (13 tot 27 KB HTML), alle shoplinks 200 met UTM, afzender Benjamin waar bedoeld (W2, S2, S3, S4, V2).

## 3. Dubbele mails uit oude live flows

12 mails uit oude flows naast de v5-reeksen, plus de Shopify-orderbevestigingen (3). Relevant voor de livegang: zonder uitzetten krijgt een klant dubbel.

| Alias | Oude mail (flow) | Tijd UTC |
|---|---|---|
| +order | Your Mystery Gift Is Here (TSUnLs, E-Book) | 19:36 |
| +order | We've Got Your Order (RL3TU6, Post Purchase) | 19:39 |
| +order | Your E-Guide Is Ready (YyaMjx, FREE E-GUIDE) | 19:39 |
| +vip | idem 3 mails na order 1, plus Mystery Gift opnieuw na order 2 | 19:37 tot 19:50 |
| +pan | Don't leave these hanging (Tsg2tV en Y2TmNB, beide oude checkoutflows) | 21:02, 21:05 |
| +set | Don't leave these hanging (Y2TmNB) | 20:59 |
| +uk | Don't leave these hanging (Y2TmNB) | 21:00 |
| +welcomeint | "Hi {{ first_name }}, we saved these for you" (SwkMyn, oude cart) | 21:16 |

Na een order kreeg een klant dus 3 oude mails binnen 5 minuten naast P1; na een checkout tot 2 oude checkoutmails naast C1. Fix: draaiboek 5.1/5.2 volgen (oude checkout Y2TmNB/Tsg2tV, oude cart SwkMyn/TBWngE, en de vier oude naflows E-Book, FREE E-GUIDE, Post Purchase, Pan Education uit in dezelfde minuut dat v5 aan gaat).

## 4. Niet getest (en waarom)

- Echte browse (B1/B2), cart-acc, checkout set/acc/gift card en de markten CA, AU, EU, SG, NZ, HK, XX: onsite-tracking en checkout uit deze sandbox bereiken Klaviyo niet; de testrun-agent heeft hiervan previews gemaakt (`research/v6-golive/previews/`), geen ontvangen mails.
- Checkout C3-S (set): het set-event kwam niet als set binnen.
- Winback R2 (gewone klant), Anniversary N2, cooldown-varianten (V1 nocode, R2 nocode): door de timing niet bereikt of niet sluitend (de cooldown-split liep vóór de vorige codemail aankwam).
- Post-purchase levering (P2) en UGC U1: geen Delivered Shipment-event.
- Unsubscribe, voorkeuren, web-view, Facebook, Instagram en recover-checkout: hosts geblokkeerd door de proxy, handmatig klikken.
- Gmail-tab: alle mails hebben alleen INBOX (geen CATEGORY-label zichtbaar via de API), tab niet vast te stellen. Apple Mail en Outlook: alleen gesimuleerd (dark mode, geforceerde inversie).

## 5. De 9 fixes vóór livegang

1. Vervaltermijn op alle 9 Klaviyo-coupons, één testcode in Shopify controleren (H1).
2. `|default:''` op elke `siraat_owned`-lookup, opnieuw exporteren en koppelen (H2).
3. Mobiele CSS van `.offer-code` (H3).
4. N2 hertesten nu de SK_ANNIV15_7D-pool bestaat (H4).
5. V2 P.S. zonder HI10 (M1).
6. Warranty-pagina naar 75 jaar of link naar refund-policy (M2).
7. P3-PAN dekselknop met de juiste variant (M3).
8. W2 "our The Green Clean E-Guide" (M5) en TEST-welcome opnieuw koppelen om M4 en L1 tot L4 in het echt te bevestigen.
9. Organisatienaam in Klaviyo naar "Siraat's Kitchen" (M6).

Daarnaast, al in het draaiboek: oude flows uit in dezelfde minuut (paragraaf 3).
