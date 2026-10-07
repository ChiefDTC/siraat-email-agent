# Build notes: Welcome (v3, UX-ronde 7 oktober 2026)

Map: `klaviyo/templates/v3/welcome/`. Bronnen direct bewerkt (niet via `scripts/gen_welcome_v3.py`, die is nu verouderd en zou de nieuwe bronnen overschrijven). Hero-register: `content/media/hero-register/welcome.csv`.

## Per mail

| Mail | Hero (label / kop / subregel) | Aanbodbalk | Mobiel | Wat er veranderde |
|---|---|---|---|---|
| W0 kopers | CARE AND USE / First heat, then oil. / Your first egg, in three steps. | geen (kopers-pad) | 2.771 px | Geen codebalk, geen aanbod. Drie stappen als icoonkaarten (warmte, waterdruppel, pan) met de twee GIF's, rij "goed om te weten" met 4 iconen, 1 review, kleine deksel-link ($59), card game in één regel. |
| W1-A | YOUR WELCOME OFFER / 10% off your first pan. / On top of the sale, plus $70 in gifts. | 10% OFF WITH HI10 · $70 IN GIFTS | 3.411 px | Codebalk, aanbodblok HI10 direct onder de hero, giveaway in één regel, gifts met beeld, knop, dan pas het verhaal (eerste orders 20 december 2024) in twee zinnen, 3 icoonrijen, 2 reviews, knop, iconen. |
| W1-B | WELCOME GIFT CARD / 10% off your first pan. / Your welcome gift card is inside. | idem | 3.426 px | Identiek aan W1-A, behalve het aanbod: gift-card-beeld met knop eronder en live tekst "10% on top of the sale ... HI10". Zelfde onderwerpen, zelfde kop, zelfde volgorde: de test meet alleen de framing. |
| W2 | geen (tekstmail Benjamin) | geen | 1.875 px | Brief ingekort, PFAS-regel met 31 compounds, P.S. met HI10 + $70 in gifts + 30-day returns, daaronder de knop "Claim my 10% + gifts". Geen codebalk. Preview noemt de P.S. |
| W3 | LIGHT LABS REPORT NO. 25895 / Tested. Not claimed. / 31 PFAS tested. Every one below detection. | idem | 3.474 px | Knop direct onder de hero plus tekstlink naar het rapport, drie vragen als icoonrijen, certificaat, aanbodkaartje na het bewijs, vergelijking in 2 kolommen (past op 390), 2 reviews, knop. Anatomie-doorsnede eruit (lengte). |
| W4-US | THE ONE MOST PEOPLE PICK / Start with the Pan Pro. / Five reasons, and the right size for you. | idem | 3.477 px | De Pan Pro is de held: 5 redenen met iconen (geen coating, lab-getest, metalen spatels + vaatwasser, inductie/gas/elektrisch/oven, 75 jaar garantie), maatkiezer met 4 maten, voor wie, prijs en prijs na HI10, aanbodkaartje, daarna pas de drie instappen (Pan Pro vanaf $114.30, 6-delige set $349 naar $314.10, 12-delige set $599 naar $539.10). Reviews eruit voor de lengte (W5 is de reviewmail). |
| W4-INT | SHIPS WORLDWIDE · DUTIES PAID / Start with the Pan Pro. / idem | idem | 3.431 px | Als W4-US, zonder prijzen ("Prices in your currency at checkout, HI10 taken off"), zonder 12-delige set; derde instap is de Cookware Set Pro. `{{BLOCK:icons-int}}`. |
| W5 | LAST REMINDER / Your 10% is still here. / Last welcome email. Code HI10 inside. | idem | 3.478 px | Aanbodkaartje direct onder de hero ("STILL YOURS", "The last time we mention it in this series"), gifts met beeld, knop, Tammy als uitgelichte quote plus 2 gelijke kaarten, Pan Pro en Duo met prijs na HI10, knop. |

Alle verkoopmails: drie keer dezelfde primaire knop "Claim my 10% + gifts" (in W0 "Watch the cook guide"), links met `https://siraatskitchen.com/discount/HI10?redirect=/products/...`, hero linkt naar dezelfde URL. Geen horizontale overloop (scrollWidth 390), geen kapotte beelden, geen `[[...]]` of `{{BLOCK` in de previews, geen gedachtestreepjes.

Boven de vouw: aanbodbalk in de hero staat op ongeveer 470 tot 510 px. De knop in het aanbodblok (W1-A, W5) of onder de gift card (W1-B) loopt van ongeveer 748 tot 802 px: de bovenkant valt net binnen 750, de onderkant net erbuiten. W3 en W4 hebben de knop op 535 tot 589 px.

## Coupons

- Geen nieuwe coupons nodig. Alles draait op HI10 (bestaat, actief).
- Testvoorstel W5 (niet gebouwd): een variant met een unieke code `{% coupon_code 'W5_10_72H' %}` (10 procent, vervalt 72 uur na toewijzing, Klaviyo-Shopify-coupon) en de regel "Expires 72 hours after this email" via `deadline=` in `{{BLOCK:offer}}`. Pas dan mag W5 een echte deadline noemen. Zie 04-offer-strategy besluit B (unieke 10-dagen-code als arm C in W1).

## Open punten voor Floris

1. **6-delige set $349 tegenover $399.** W4-US toont $349 naar $314.10 en linkt naar `titanium-hammered-pan-set-with-lids-6-pcs-bday-sale` (UNLISTED, $349). Het actieve product staat op $399. Als die unlisted pagina verdwijnt of de prijs $399 wordt, W4-US en W4-INT aanpassen.
2. **Maatprijzen.** Uit products.csv: Mini 8" $129, Small 10" $127, Standard 11" $134, Large 12" $139. Small is goedkoper dan Mini; dat staat zo in Shopify. Even controleren.
3. **"Voor wie"-teksten per maat** (eggs for one, breakfast for two, everyday for 1 or 2, a family) zijn mijn eigen keuzehulp, niet uit een bron. Graag akkoord.
4. **Gifts horen bij de Hammered Pan** (DECISIONS). In welcome staat daarom "WITH EVERY HAMMERED PAN" en "it all comes with your pan". Het blok zelf zegt standaard "WITH EVERY ORDER" (zo staat het in C1). Eén formulering kiezen voor alle flows.
5. **Giveaway-regel**: "Your entry is in: a chance at an order refund." Klopt met de Alia Card Game-belofte zoals in DECISIONS; de exacte Alia-tekst hebben we nog niet gezien.
6. **Duo-prijs**: Pan Pro Duo $229 (compare-at $570) uit products.csv; W5 toont $229 naar $206.10.
7. **W4 zonder reviews**: weggelaten om onder ~3.500 px te blijven; W5 draagt de reviews. Als Floris reviews in W4 wil, wordt de mail ongeveer 3.850 px.
8. **W0 en P2 overlappen** (zelfde drie stappen). W0 is nu kort; overweeg W0 over te slaan voor wie de laatste 7 dagen in post-purchase zat.
9. **Chef-video-stills** (W0, W4-INT) zijn bijgesneden boven de ingebakken ondertitel en dus vergroot; ze zijn zachter dan de shoot-foto's. Voor W4-INT eventueel later een scherpere still kiezen.
10. Oude heroes `hero-w0.jpg`, `hero-w1.jpg`, `hero-w3.jpg`, `hero-w4-us.jpg`, `hero-w4-int.jpg`, `hero-w5.jpg` staan nog in assets maar worden niet meer gebruikt. Bij upload naar Klaviyo alleen de nieuwe `*-hero.jpg` meenemen. `assets/klaviyo-urls.txt` bestaat nog niet, dus er is nog geen `.klaviyo.html` geschreven.
11. `scripts/gen_welcome_v3.py` niet meer draaien: hij overschrijft deze bronnen met de oude opbouw.

## Blok- en scriptbevindingen (niet aangepast)

- `offer.html`: de witte knop is 320 px met 26 px binnenmarge; labels langer dan ongeveer 20 tekens (bijv. "Shop the Pan Pro with 10%") lopen op mobiel en desktop over twee regels. Daarom in W4 ook "Claim my 10% + gifts".
- `features.html`: eyebrow en headline zijn verplicht; met lege waarden blijven twee lege div's staan (ongeveer 22 px wit). Optioneel maken zou helpen.
- `features.html` heeft vast 3 rijen; voor 5 redenen (W4) heb ik dezelfde opmaak inline geschreven.
- `gifts.html` standaard-eyebrow "WITH EVERY ORDER" botst met DECISIONS (gift-stack hoort bij de Hammered Pan), zie open punt 4.
