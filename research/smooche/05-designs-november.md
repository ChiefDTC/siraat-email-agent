# Smooche · 05 · Designs november (1 nov 2026)

Uitwerking van de top 5 uit `04-meer-output-november.md`, op verzoek van Floris (1 nov): eerst een plan met designs in Figma, dan pas bouwen in Klaviyo. **Status: concept, niets in Klaviyo of Shopify gewijzigd, niets live.**

- Figma (pagina "BFCM 2026 · Flows (Black Friday-stijl)"), rij "November meer output (plan, 1 nov)": https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=210-2
  - titelkaart 210:5, tijdlijn Smooche vs Siraat 210:21, previews 210:77 (C1b), 210:81 (W1b), 210:85 (K1b), 210:89 (BF-W2), 210:93 (BF-W3), 210:97 (stock alert), 210:101 (last day), 210:105 (final hours). Previews zijn de US-versie, 375 px, 2x.
- Bronnen: `klaviyo/templates/v3/bfcm/november/nov-*.html` (gemaakt met `_tools/make_nov.py`), build `*.klaviyo.html` en `*-preview.html`, renders `previews/nov-*-{us,int}-375.png`.
- Bouwen en controleren: `python3 -I _tools/make_nov.py`, `python3 -I _tools/render_nov.py <uitmap>` (build_template + Django-render per markt + checks), `node _tools/shot_nov.js <uitmap> <shots>` (375 en 600 px, 2x, kapotte beelden en overloop). Alles vanuit /tmp.
- Nieuw blok `partials/blocks/bf-stock.html` (`{{BLOCK:bf-stock ...}}`): donkere kaart met drie voorraadregels (NEXT BATCH geel, SELLING FAST stock red, IN STOCK grijs).

## Gecontroleerd
Alle 8 mails, US (person.Country United States, checkout co_set6, cart atc_x_set6) en INT (Germany, co_pan_eur, atc_lid_eur): build zonder fouten, Django-render zonder restanten, 0 gedachtestreepjes, vaste header met lockup (monogram + SIRAAT) en vaste footer aanwezig, 0 kapotte beelden, geen horizontale overloop op 375 en 600 px. BFCODE alleen in C1b en K1b (3x, placeholder). 12-delige set alleen in de US-tak.

## De mails (verzendvolgorde)

| # | Mail | Afzender | Trigger en timing | Filters | Onderwerp A / B | Preview | Waarom (plan 04) |
|---|---|---|---|---|---|---|---|
| 1 | C1b checkout (`nov-c1b`) | Benjamin from Siraat | QUBUQV, nieuwe stap na C1: +1 uur na Started Checkout | Placed Order 0 sinds start; < 3 Received Email laatste dag; geen BFCODE-mail uit cart laatste uur | Your Black Friday cart is saved / Benjamin here, about your cart | Your extra 10% is still on it, and so are your 4 gifts. | punt 2: C1 $7,96 per ontvanger, Smooche 3 mails in 90 min |
| 2 | W1b welcome (`nov-w1b`, = signup/bf-w1b + voorraadblok) | Benjamin from Siraat | T4a5Mk na W1 en Rn556d na BF-W1: +3 uur | Placed Order 0; geen Started Checkout laatste 3 uur; geen abandonment-mail laatste dag; < 3 mails laatste dag; holdout 20% | Up to 70% off is still waiting / The short version | The short version: three picks, up to 70% off, no code needed. | punt 3: gat tussen W1 ($2,74) en de volgende ochtend |
| 3 | K1b cart (`nov-k1b`) | Benjamin from Siraat | TZG9Mx, nieuwe stap na K1: +3 uur na Added to Cart | Placed Order 0; Started Checkout 0 sinds start; < 3 mails laatste dag | Your cart, still at Black Friday prices / Still thinking it over? | Benjamin here. An extra 10% is applied with the button, on top of up to 70% off. | punt 4: K1 $3,59, geen tweede dag-0-contact |
| 4 | BF-W2 (`nov-bf-w2`, = lifecycle/w2-bf 54 woorden + voorraadregel) | Benjamin from Siraat | Rn556d na BF-W1: 1 dag tot 10:00 | Placed Order 0; geen abandonment-mail laatste dag (overslaan); < 3 mails laatste dag | The pan nobody else was making / A note from Benjamin (and the sets) | It's Benjamin. A short note, and a heads-up about the sets. | punt 1: BF-groep krijgt na BF-W1 niets meer |
| 5 | BF-W3 (`nov-bf-w3`, = signup/bf-w3 + voorraadblok voor de sets) | Siraat | Rn556d: +2 dagen tot 09:00 | idem | Built to last. Priced for Black Friday. / Why there's nothing to wear off | Nothing on it to wear off. That's why it's covered for 75 years. | punt 1 |
| 6 | Stock alert (`nov-stock`, nieuw, campagne) | Benjamin from Siraat | campagne di 17 of wo 18 nov 08:15 lokaal | Engaged 90 dagen; zonder kopers 14 d, BF-signupreeks dag 0 tot 3 en campagne laatste 16 u | Our sets sold out. Here's what that means. / A stock update from Benjamin | The current batch of sets is gone. The pans are in stock. Up to 70% off until Monday, November 30. | verzoek Floris 1 nov: eerlijke voorraadurgentie |
| 7 | Last day (`nov-last-day`, = signup/bf-last ingevuld) | Siraat | campagne zo 29 nov 18:00 lokaal + laatste stap BF-reeks | Engaged 60 d + abandoners 30 d zonder order; zonder kopers 7 d | Black Friday ends tomorrow / One day left: up to 70% off | Up to 70% off until Monday, November 30. Then prices go back to normal. | punt 6: echte deadline |
| 8 | Final hours (`nov-final-hours`, korte brief) | Benjamin from Siraat | campagne ma 30 nov 11:00 lokaal | Klikkers 30 d + abandoners 14 d zonder order; zonder kopers sinds 27 nov | Final hours / Last day: up to 70% off | The Black Friday Sale ends today. This is my last email about it. | punt 6 |

Alle mails: up to 70% off (nooit "70% off everything"), extra 10% met BFCODE alleen in C1b en K1b, 4 gifts, 30-day returns, 75-year warranty, 100,000+ customers, oprichter Benjamin, reply "our team will help". Markt via `{{USONLY}}`/`{{IF:US}}` (12-delige set alleen US) en `{{SIZE}}`, `{{GIFTS}}`, `{{FRICTION}}`.

## Einddatum en voorraad (Floris, 1 nov)
- Einde sale: **Monday, November 30** (Cyber Monday). Klok en tijdzone niet nodig in de copy. Lost de oude placeholders [END DATE] en {{SALE_END}} op.
- Voorraad Shopify 1 nov ~15:00 UTC: onder nul 6-Pcs set (-627), Pan Pro Duo (-452), 12-Pcs set (-8; ShipBob 0 op voorraad, ~600 wachtende orders), Pan Pro & Utensil Set (-96). Laag: Wok Pan Pro 24/26/28 cm 84/126/78, Pan Pro Mini 166, Deep Pan 24 cm 197, molens 9. Ruim: Pan Pro Standard 935, Large 518, Small 454, Pizza Steel 828.
- Nieuwe batch 6-Pcs en 12-Pcs: aankomst magazijn week van 9 nov (12-Pcs ~800 stuks, grotendeels al gereserveerd door de ~600 wachtende orders). Copy: "Orders now reserve yours from our new batch, arriving in mid-November. Most of the next 12-piece batch is already reserved." (alleen US). Geen harde verzenddatum, geen aantallen.
- Regels in de mails (drempels, geen aantallen): Wok Pan Pro 24 en 28 cm "fewer than 100 left of each", Pan Pro Mini "fewer than 200 left", Pan Pro Standard/Small/Large "plenty in stock". In C1b en K1b een gele NEXT BATCH-regel alleen als er een 6-Pcs of 12-Pcs set in de cart zit.
- **Wekelijks controleren** (elke maandag, en op de ochtend van de stock alert en de deadline-mails): kloppen de drempels nog? Wok onder 100, Mini onder 200, Standard ruim. Zodra een regel niet meer klopt: regel aanpassen of weghalen. Later dynamisch via catalogus/voorraad in Klaviyo (catalog item inventory) in plaats van vaste tekst.

## Open vragen voor Floris
1. Akkoord op de 8 concepten en de afzender "Benjamin from Siraat" (C1b, W1b, K1b, BF-W2, stock alert, final hours)?
2. BF-groep: W2/W3 als nieuwe stappen in Rn556d (dit voorstel) of exit-split 119850651 in T4a5Mk aanpassen zodat de BF-groep alleen W1 overslaat?
3. Pan Pro Duo (-452) en Pan Pro & Utensil Set (-96): wanneer komt daar voorraad? Nu niet in de NEXT BATCH-regels genoemd.
4. Mogen de gifts ($70) en "4 gifts" blijven staan in november, ook bij orders uit de nieuwe batch?
5. Stock alert: datum (voorstel 17 of 18 nov) en wie verstuurt hem (wij of Homestead)?
6. BFCODE: combinaties in Shopify gefixt (product + verzending), voordat C1b en K1b live gaan?
7. Knoptekst "SHOP NOW"/"SHOP IT" op de productkaarten (Smooche-stijl, wijkt af van de copy-skill): akkoord?
