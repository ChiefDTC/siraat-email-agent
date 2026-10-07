# P4 · Review request (live, niet herbouwd)

Status 7 oktober 2026. P4 is de bestaande reviewflow. Niet opnieuw gebouwd in v3; deze notitie legt vast hoe hij aansluit op P1 tot P3.

## Wat er live staat

- Flow: "Review request · Delivered +14d (Siraat DS)" (XzHrez), bron `klaviyo/flows/review-request-flow.json`.
- Template-referentie: `klaviyo/templates/review-request.html` (titel "Win your purchase amount back").
- Trigger: Delivered Shipment (VcUF33). Wachttijd 14 dagen na bezorging, 09:30 lokale tijd. A/B-test op onderwerpregel loopt.
- Instapfilters: één keer per klant ooit, 12-delige set uitgesloten op alle producttitels, geen mail uit de oude reviewflow in 30 dagen.
- Sterren-routing: 4 en 5 naar Trustpilot (evaluate/siraatskitchen.com), 1 tot 3 naar /pages/your-experience?rating=N&order={{ event.extra.order_number }}.
- Incentive in de mail: elke maand wint één reviewer het volledige aankoopbedrag terug (loting).

## Aansluiting op v3

| Mail | Moment | Opmerking |
| --- | --- | --- |
| P1 | Placed Order + 1 uur | p1-first of p1-repeat |
| P2 | Delivered + 1 dag | chef-gids, vraagt om een foto of video terug (UGC) |
| P3 | Placed Order + 14 dagen | cross-sell, drie varianten |
| P4 | Delivered + 14 dagen | live reviewflow, ongewijzigd |

## Punten om te beslissen

1. **Tijdstip klopt niet met v3-flow-system.md.** Dat document zegt "30 dagen na levering", live is 14 dagen na levering. Bij 6 tot 10 dagen levertijd landt P4 dan rond dag 20 tot 24 na de order, vlak na P3 (dag 14). Voorstel: P3 laten staan, en in de reviewflow een verzendfilter "geen mail uit post-purchase v3 in de laatste 3 dagen", zodat cross-sell en reviewverzoek niet op opeenvolgende dagen vallen. Alternatief is de geplande test 7 tegen 14 dagen (BACKLOG item 8) uitbreiden met 21 dagen.
2. **Incentive.** Live: maandelijkse loting van het aankoopbedrag. Mapping-notitie noemde een gift card van 20 procent. Eén versie kiezen en die overal gelijk houden. In geen enkele mail "unsolicited" of "independent" bij reviews (DECISIONS, 7 okt).
3. **Opener voor de volgende revisie.** Review R028 (Carlos C.): "Spend the time reading the emails Siraat sends you detailing best cooking methods, cleaning methods, and how to get the most out of your pans." Past als bewijs dat P2 werkt.
4. **Stijl.** De live reviewmail heeft nog niet de vaste header en footer uit `partials/`. Bij de volgende template-wissel ombouwen naar de v3-opbouw (header, hero, knop onder de hero, footer), routing-links ongewijzigd laten en daarna de links in de live flow controleren (PLAYBOOK 7.4).
5. **12-delige set.** Nog uitgesloten. Volgens DECISIONS (7 okt) is de levertijd nu een paar dagen; uitsluiting kan eraf zodra Floris dat bevestigt (BACKLOG item 7).
