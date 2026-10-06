# Siraat's Kitchen · E-mail agent

Dit is het geheugen en de werkplaats van de e-mailmarketing-agent die Homestead vervangt.
Elke sessie van Claude begint met het lezen van deze repo en eindigt met het bijwerken ervan.

## Hoe de repo werkt

| Bestand | Wat erin staat | Wie schrijft |
| --- | --- | --- |
| `PLAYBOOK.md` | De vaste regels: merk, stijl, techniek, segmentatie, testen. Verandert zelden. | Claude, na akkoord van Siraat |
| `BACKLOG.md` | Wat er nog gebouwd of getest moet worden, in volgorde. | Siraat en Claude |
| `LOG.md` | Wat er gedaan is en wat het opleverde, per datum. Hier zit het leren. | Claude, elke sessie |
| `ROUTINES.md` | De automatische taken (dagelijks rapport in Slack, herinneringen) en hun prompts. | Claude |
| `klaviyo/` | Alle bouwmateriaal: templates (HTML), flow-definities (JSON), Figma-scripts, foto's, fonts. | Claude |

## Start van een sessie (voor Claude)

1. Lees `PLAYBOOK.md` volledig.
2. Lees de laatste tien regels van `LOG.md` en de bovenste vijf items van `BACKLOG.md`.
3. Vraag niets wat daar al staat. Begin met het bovenste backlog-item, tenzij Siraat iets anders zegt.
4. Sluit af met een logregel in `LOG.md` en, als er iets gebouwd is, een commit van de bestanden.

## Belangrijkste ID's

| Wat | ID / link |
| --- | --- |
| Klaviyo account | TdtTzz |
| Figma design system | https://www.figma.com/design/K8qNiZ7OEThlRrUXH7QImi |
| Figma Welcome Flow v2 | https://www.figma.com/design/74S1Tjr8BkSgQfm6vLnrLo |
| Oude welcome flow (live) | https://www.klaviyo.com/flow/SiaNLu/edit |
| Review flow (live sinds 6 okt 2026) | https://www.klaviyo.com/flow/XzHrez/edit |
| Review template (bron) | https://www.klaviyo.com/email-editor/S2tykT/edit |
| Oude review flow (uit op 12 okt 2026) | https://www.klaviyo.com/flow/Vixr6X/edit |
| Slack rapportkanaal | #claude-mail (C0C7A159Q6M) |
| Shopify-store | siraatskitchen.com |

## Metric-ID's in Klaviyo (nodig voor filters en rapporten)

| Metric | ID | Bron |
| --- | --- | --- |
| Placed Order | RSNxYV | Shopify |
| Fulfilled Order | VtEiZT | Shopify |
| Fulfilled Partial Order | UHUr2m | Shopify |
| Delivered Shipment | VcUF33 | Shopify |
| Refunded Order | Xg6cwn | Shopify |
| Cancelled Order | TFervq | Shopify |
| Opened Ticket | YzvjGf | Gorgias |
| Resolved Ticket | SzcCyb | Gorgias |
| Received Email | YkRM4Q | Klaviyo |
| Postflows 4. Shipment Delivered | UabgWz | Postflows (vuurt 2,5x per zending, niet gebruiken als trigger) |
