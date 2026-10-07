# Build notes · post-purchase v3 (7 oktober 2026)

Herbouw van P1-first, P1-repeat, P2, P3-pan, P3-set en P3-accessory volgens PLAYBOOK 10 en 11. P4 (p4-note.md) ongewijzigd.

## Per mail

| Mail | Hero (label · kop · subregel · aanbodbalk) | Bronfoto | Mobiel |
| --- | --- | --- | --- |
| P1-first | ORDER CONFIRMED · "Good call. 4 gifts coming." · "Here is what happens next" · YOUR 4 GIFTS ARE ON THE WAY | Shopify Files 7d6b1b9a (gezin aan ontbijt) | 3.789 px |
| P1-repeat | ORDER CONFIRMED · "Good to see you again." · "Same careful packing, same 4 gifts" · SAME 4 GIFTS, ON THE WAY | Shopify Files chopstickssiraat.webp | 2.793 px |
| P2 | CHEF GUIDE · "If you can do an egg," · "you can do anything" · HEAT FIRST · THEN OIL · THEN EGG | chef-video still-egg-close (uitsnede) | 3.949 px |
| P3-pan | FITS YOUR PAN · "The lid, 10% off" · "For owners only. Your code is inside." · YOUR 10% CODE EXPIRES IN 14 DAYS | chef-video still-dishwasher (uitsnede) | 3.183 px |
| P3-set | FOR SET OWNERS · "The pan your set is missing" · "Crepe or wok, 10% off. Code inside." · YOUR 10% CODE EXPIRES IN 14 DAYS | Shopify Files 1.9.png (stel bakt crêpes) | 3.240 px |
| P3-accessory | FOR SIRAAT OWNERS · "Now meet the pan." · "Your 10% thank-you code is inside." · YOUR 10% CODE EXPIRES IN 14 DAYS | chef-video still-steak (uitsnede) | 3.472 px |

Register: `content/media/hero-register/post-purchase.csv`.

## Coupon (aanmaken in Klaviyo, niet gedaan)

- `P3_THANKYOU_10_14D`: Shopify unique coupon via Klaviyo, 10 procent, één gebruik per code, vervalt 14 dagen na toewijzing. Uitsluiten: abonnementen (Recharge). Gebruikt in P3-pan, P3-set en P3-accessory (codebalk, aanbodblok en in de knop-URL `/discount/<code>?redirect=...`).
- Testen in een preview: dat de tag meerdere keren in één mail dezelfde code geeft (codebalk, aanbodblok, vier links), en dat de tag binnen een href werkt.

## Besluiten voor Floris / open punten

1. **E-book-link ontbreekt.** Geen downloadlink gevonden voor het Plastic-Free Home e-book. Knop "Download your e-book" (P1-first, P1-repeat) wijst tijdelijk naar https://siraatskitchen.com/pages/faq. Echte link nodig (PDF in Shopify Files of de productpagina van het digitale product).
2. **Set van 6 = $349** in P3-accessory ($314.10 met code). In Shopify staat de actieve listing op $399; $349 is de unlisted BDAY-listing. Floris beslist; link wijst nu naar de actieve listing `titanium-hammered-pan-set-with-lids-6-pcs`.
3. **Prijzen na code** (10 procent): lid $59 naar $53.10, 2 Pans + 2 Lids $199 naar $179.10, board vanaf $69 naar $62.10, crêpe $139 naar $125.10, wok vanaf $119 naar $107.10, sheets $25 naar $22.50, Pan Pro Standard $134 naar $120.60. Compare-at $439 bewust niet getoond (audit: niet geverifieerd). Checken dat de coupon op deze producten werkt.
4. **P3-set voor Complete Edition / Set Pro.** Die sets bevatten al crêpe en/of wok. Split of filter toevoegen (bijv. Items bevat "Complete Edition" of "Set Pro" uitsluiten of naar P3-pan sturen).
5. **P3-pan maat van het deksel.** Nu "Pick the size of your pan". Dynamisch maken op basis van de gekochte maat kan met een line-item-conditie; nog niet gebouwd.
6. **Gift-waardes en de trekking** ($15, $30, $25, $450) laten bevestigen. In P1 staat geen "weekly" of aantal winnaars meer, alleen "entered in the draw". Actievoorwaarden (official rules) zijn nodig zodra de trekking genoemd wordt (04-offer-strategy).
7. **Hero-foto's uit de chef-video** hebben ingebakken ondertitels. Ik heb kopieën uitgesneden boven de ondertitel (originelen ongewijzigd, kopieën in `post-purchase/assets/src/`). Daardoor is de bron maar 540 px breed, opgeschaald naar 1200: iets zacht. Betere vervanging zodra er schone frames zijn.
8. **P2 hero:** de kop valt deels over het gezicht van de chef (frame kon niet hoger uitgesneden worden). Leesbaar, maar een schoner frame (ei in de pan zonder tekst) is beter.
9. **Codebalk P3 en de vouw:** door de codebalk boven de header staat de eerste knop in P3 op ongeveer 800 tot 850 px (aanbodbalk in de hero op ongeveer 470 px). Iets boven de doelwaarde van 750 px.
10. **P1-first en P2 zijn langer dan 3.400 px** (servicemails, geen verkoopmail). P2: chef-GIF's (oil-shimmer, egg-slide) samen ongeveer 1,7 MB.
11. **Nieuwe iconen** (alleen in deze flow, `post-purchase/assets/`): icon-tracking-email, icon-package, icon-egg, zelfde stijl als de gedeelde set (Lucide-achtig, 1.75 stroke, brick). Kandidaten om naar `partials/shared` te verhuizen.
12. **Klaviyo-HTML niet geschreven:** `build_template.py` schrijft geen `.klaviyo.html` zolang `partials/shared/klaviyo-urls.txt` ontbreekt en de nieuwe beelden (heroes, iconen, oil-shimmer.gif) niet in `assets/klaviyo-urls.txt` staan. Eerst uploaden.
13. Water-test-GIF (ingebakken "TRY THE WATER TEST") niet meer gebruikt; stap 2 staat zonder beeld.
