# Flow-systeem v3 · volledige logica

Versie 7 oktober 2026. Bindend voor de bouw. Besluiten: DECISIONS.md. Content per mail: content/mapping/mapping.csv.
Doel van elk onderdeel: conversie, orderwaarde, herhaalaankoop. Iemand zit nooit in twee verkoop-flows tegelijk.

## Prioriteit tussen flows (geen overlap)

1. Post-purchase (gekocht) wint altijd.
2. Checkout abandonment.
3. Cart abandonment (alleen als er geen Checkout Started is).
4. Browse abandonment (alleen als er geen Added to Cart en geen Checkout Started is).
5. Welcome (nieuwe inschrijver).
6. Winback (oude klant, geen order in 60 dagen).

Technisch: elke flow heeft een flow-filter "niet in [hogere flow] in de laatste X dagen" en elke mail een verzendfilter "Placed Order = 0 sinds flow-start" (behalve post-purchase).

Globale regels: smart sending UIT in alle flows (de prioriteit regelt overlap), quiet hours 21:00 tot 08:00 lokale tijd, UTM-tracking aan, afzender "Siraat's Kitchen" <send@siraatskitchen.com>, reply-to een gelezen inbox.

## 1. Checkout abandonment (vervangt Y2TmNB en Tsg2tV)

- Trigger: Checkout Started (RfMvni).
- Flow-filters: Placed Order = 0 sinds flow-start; niet in deze flow in de laatste 14 dagen; niet in post-purchase in de laatste 7 dagen.
- Herinstap: na 14 dagen.
- Split op cart-waarde: event value >= $300 = "set-koper" (tak S), anders "pan-koper" (tak P). Inhoud verschilt in C3 en C4.

| Stap | Wachttijd | Mail | Split en filter |
| --- | --- | --- | --- |
| 0 | 1 uur | C1 Your pan is still here | Verzendfilter: geen order |
| 1 | tot dag 2, 09:00 | C2 Why Siraat (drie vragen) | Geen order |
| 2 | 1 dag | C3 Reserved at today's price | Split S/P: S krijgt set-voordeel en gift-stack, P krijgt de pan-upgrade naar de 6-delige set ($349) |
| 3 | 1 dag | C4 Final call: cart and gifts | Split land: US krijgt 12-pcs als alternatief, INT niet |
| 4 | einde | | Naar browse/welcome nooit binnen 14 dagen |

A/B: onderwerp C1 ("Forgetting something?" tegen "Your pan is still here").

## 2. Cart abandonment (vervangt SwkMyn en TBWngE)

- Trigger: Added to Cart (QXcV8K).
- Flow-filters: Checkout Started = 0 sinds flow-start; Placed Order = 0 sinds flow-start; niet in checkout-flow in 7 dagen; niet in deze flow in 14 dagen.
- Herinstap: na 14 dagen.

| Stap | Wachttijd | Mail | Split |
| --- | --- | --- | --- |
| 0 | 1 uur | K1 One wipe. No scrubbing. | |
| 1 | 1 dag | K2 Built to outlast you (kosten per jaar) | Split: heeft eerder gekocht? Ja = korte versie zonder merkuitleg |
| 2 | 1 dag | K3 Covered for 75 years, returnable for 30 days | |

## 3. Browse abandonment (vervangt Wj6x6V en TyEjuQ)

- Trigger: Viewed Product.
- Flow-filters: Added to Cart = 0 sinds flow-start; Checkout Started = 0 sinds flow-start; Placed Order = 0 sinds flow-start; niet in cart- of checkout-flow in 7 dagen; niet in deze flow in 7 dagen.
- Herinstap: na 7 dagen.

| Stap | Wachttijd | Mail | Split |
| --- | --- | --- | --- |
| 0 | 4 uur | B1 No coating to scratch off (bekeken product dynamisch) | |
| 1 | 2 dagen | B2 Week one, in their words | Split: klikte B1? Ja = met productaanbod, nee = alleen reviews |

## 4. Welcome (vervangt SiaNLu en Failure to launch T2SmtR)

- Trigger: toegevoegd aan lijst Uw8eZG (Alia Card Game, giveaway order refund).
- Flow-filter: e-mail bevat niet test@; nooit eerder in deze flow.
- Herinstap: nooit.
- Split A: Placed Order > 0 ooit? Ja = kopers-pad (W0). Nee = prospect-pad.

| Stap | Wachttijd | Mail | Split en filter |
| --- | --- | --- | --- |
| A-ja | 10 min | W0 Thank you. Now the first egg. | Einde, post-purchase neemt over |
| A-nee 0 | 10 min | W1 The original + HI10 (giveaway in één regel bevestigd) | A/B: HI10 als code tegen HI10 als gift card |
| 1 | tot dag 1, 10:00 | W2 Why I started (tekst, Benjamin) | Geen order |
| 2 | tot dag 3, 10:00 | W3 Tested. Not claimed. | Geen order |
| 3 | tot dag 6, 10:00 | Split B: land = US? | |
| 3a | | W4-US Three ways to start (incl. 12-pcs) | Geen order |
| 3b | | W4-INT Three ways to start (zonder 12-pcs, zonder prijzen) | Geen order |
| 4 | tot dag 9, 10:00 | W5 In their words + HI10 herinnering | Geen order |
| 5 | einde dag 10 | | Failure to launch uit. Niet-kopers gaan naar campagnes. |

## 5. Post-purchase (vervangt RL3TU6, combineert met review-flow XzHrez)

- Trigger: Placed Order.
- Flow-filter: niet in deze flow in 30 dagen (herhaalaankoop start opnieuw na 30 dagen).
- Split A op aantal orders: eerste order (Placed Order = 1 ooit) of herhaalklant.

| Stap | Wachttijd | Mail | Split |
| --- | --- | --- | --- |
| 0 | 1 uur | P1 Good call. Here's what's coming. (wat in de doos zit, 4 gifts) | Herhaalklant: korte versie, geen merkuitleg |
| 1 | trigger Delivered Shipment + 1 dag (aparte flow-tak via conditional wait) | P2 If you can do an egg (chef-GIF's) | |
| 2 | 14 dagen na order | P3 What goes with your pan (cross-sell) | Split op gekocht product: pan = deksel en snijplank; set = vaatwasstrips en extra pan; accessoire = Pan Pro |
| 3 | 30 dagen na levering | P4 Review request (live flow XzHrez, ongewijzigd) | |

## 6. Winback (vervangt UEfh4h)

- Trigger: Placed Order, dan wachten.
- Filter per stap: Placed Order = 0 sinds flow-start.
- Herinstap: na 90 dagen.

| Stap | Wachttijd | Mail | Split |
| --- | --- | --- | --- |
| 0 | 60 dagen | R1 New since your last order | Split op gekocht product (zelfde als P3) |
| 1 | 30 dagen | R2 Your next piece (aanbod) | Split: VIP (2+ orders) krijgt sterker aanbod |

## Segmenten die nodig zijn

- US-profielen: Location country = United States (voor W4 en C4).
- Set-kopers vs pan-kopers: event value >= $300 of Items bevat "Set".
- Eerste koper vs herhaalklant: Placed Order count.
- VIP: Placed Order >= 2 ooit.
- Nieuwe inschrijvers 14 dagen uitsluiten van campagnes: segment "Joined Uw8eZG in last 14 days and Placed Order = 0".
