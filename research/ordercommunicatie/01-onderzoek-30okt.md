# Ordercommunicatie: waarom klanten niets horen (30 okt 2026)

Drie read-only agents (Shopify, Ecomflow, Klaviyo/Gorgias). Geen klantdata in dit bestand.

## Bevindingen
1. **Achterstand Ecomflow 9 tot 23 okt.** Order tot overdracht 10 tot 14,5 dagen (normaal 1 tot 2). Fulfilled Order in Klaviyo zakte van ~206 naar 28 per dag (15 t/m 21 okt); ingehaald met batches op 24 en 29 okt. Sinds 28 okt weer onder 12 uur.
2. **Na de verzendmail stilte.** Ecomflow zet carrier "Other" (GOFO, JT, iMile, SpeedX, UDS enz., 63% na 22 okt) en stuurt geen fulfillment events naar Shopify. Shopify stuurt dan geen onderweg/bezorgd-mail en orders blijven op Fulfilled. Alleen herkende carriers (USPS, AusPost, Royal Mail) werken.
3. **Blinde periode op de trackinglink:** last-mile nummer scant pas na vlucht en douane; mediaan 6,5 dagen "nog niet ontvangen" (p90 9,5). Voortgang staat op het YT-nummer dat de klant niet krijgt.
4. **Klaviyo stuurt geen enkele verzend-, tracking- of vertragingsmail.** Alleen P1 (1 uur na order), daarna marketing. Shippingflows (Postflows In Transit, Out for Delivery, Fulfillment Delayed, Split Shipment) staan op draft. Postflows-events komen wel binnen.
5. **Gorgias WISMO** (waar is mijn order, tracking, vertraging): 16,4 per dag (1 t/m 21 okt) naar 39,2 per dag (22 t/m 30 okt), 29% van alle tickets in de laatste week.
6. **Spook-fulfillments:** Ecomflow boekt e-book, giveaway en Free Shipping als losse fulfillment, dagen voor de echte zending. Order staat op "gedeeltelijk".
7. **"(unknown sender)"**: afzender/domeinauthenticatie in Shopify, niet via API te verifiëren.
8. ShipBob verstuurt nog delen van orders; 187 open Ecomflow-issues (61 self-pickup-required); 83 orders zonder label ouder dan 7 dagen.

Casussen: draft order 15 okt (2 pakketten GFNL, bezorgd 23 okt, Shopify weet het niet, 0 verzend/bezorgmails van Klaviyo). Trustpilot-review 28 okt: order 15 okt, pan pas 29 okt verzonden (USPS, label aangemaakt).

## Plan
**Klaviyo (wij, na akkoord):** A eenmalige update aan klanten met order 9 t/m 23 okt die nog niet bezorgd zijn; B flow "nog niet verzonden na 5 dagen"; C verzend- en onderweg-flows op Postflows-events in Siraat-stijl (transactional aanvragen); D klanten met open order uitsluiten van salecampagnes; E vangnetten R9dcdY/YhQJdb naar 8 tot 9 dagen.
**Ecomflow (Floris):** fulfillment events naar Shopify (IN_TRANSIT, OUT_FOR_DELIVERY, DELIVERED); juiste carriernamen; Canada-URL; digitale regels niet als fulfillment; open issues en orders zonder label.
**Shopify (Floris):** afzenderdomein authenticeren; verzendmail: "eerste scan kan 5 tot 7 dagen duren"; ShipBob uitzetten als dat de bedoeling is.
