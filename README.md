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

## Alle live flows (stand 7 oktober 2026, cijfers laatste 30 dagen)

| Groep | Flow-ID | Naam | Mails | Orders | Omzet | Uitschr. |
| --- | --- | --- | --- | --- | --- | --- |
| Nieuwe leads | SiaNLu | EB Welcome Flow (8 mails, open-filters, kopers krijgen niets) | 69.761 | 139 | $36.066 | 1.285 |
| Leads zonder order | T2SmtR | EB Failure to launch (30 dagen wachten, dan 10 mails) | 107.520 | 16 | $3.608 | 490 |
| Lead magnets | TSUnLs, YyaMjx, YcXbHx, Wn2tsq | E-Book, Free E-Guide, Pan Education, Pan Flash Buyers | 20.000 | 32 | $7.752 | 107 |
| Browse | Wj6x6V, TyEjuQ | Browse Abandonment + Triple Pixel-variant | 27.383 | 92 | $23.659 | 358 |
| Cart | SwkMyn, TBWngE | Cart Abandonment + Triple Pixel-variant | 10.514 | 59 | $18.699 | 121 |
| Checkout | Y2TmNB, Tsg2tV | Checkout Abandonment + Triple Pixel-variant | 8.591 | 62 | $17.773 | 91 |
| Na aankoop | RL3TU6, WvRupU, UEfh4h | Post Purchase, Mystery Gift Reveal Sheets, Winback 60d (10% code) | 43.716 | 51 | $7.397 | 307 |
| Reviews | Vixr6X, XzHrez | Trustpilot 4 emojis (uit op 12 okt), Review request (nieuw) | 2.725 | 4 | $712 | 22 |
| Overig | S7V4a7, WsQDYu, SxN86d, TLHht3, UcGzaL, Y4a7fJ | Sunset (segment XY4NVp), Back in Stock, Middle East delay, 3 CS-notificaties | | | | |

Daarnaast 46 flows op Draft (HKT, Farooq, Postflows, oude EB-versies). Volledige lijst: `curl -g "https://a.klaviyo.com/api/flows?page[size]=50"`.
Pad van een nieuwe lead die niet koopt: 8 welcome-mails (dag 0 tot 10) plus 10 failure-to-launch-mails (dag 30 tot 41) plus browse, cart en campagnes.
