# Q4 A/B- en optimalisatieplan flows (28 okt 2026)

Samenvatting van vier agent-analyses:
- 01-welcome.md
- 02-checkout-cart.md
- 03-browse-site.md
- 04-postpurchase-winback-q4kalender.md

Niets is in Klaviyo gewijzigd. Alles hieronder wacht op akkoord van Floris. Bedragen zijn schattingen van extra omzet per week, geen bewezen effecten.

## Eerst repareren (geen test, wel geld)

| # | Wat | Waarom | Wie |
|---|---|---|---|
| R1 | Bezorgevents herstellen (Postflows UabgWz, Delivered Shipment VcUF33) | Sinds ongeveer 22 okt gaan er nog maar 30 tot 70 events per dag door, waar dat 150 tot 430 was. Ecomflow verstuurt wel 160 tot 370 orders per dag. Daardoor krijgen P2, affiliate S1 en review XzHrez bijna niemand. | Floris (Postflows/Shopify/Ecomflow). Tijdelijk kunnen de flows starten op Fulfilled Order plus een vaste wachttijd, met akkoord. |
| R2 | $0-orders uitzoeken | Het aandeel steeg van 2% naar 10% van de orders. Vooral Pan Pro Standard, 186 in 9 dagen. Dit vertekent elke conversiemeting. | Floris |
| R3 | Herinstap post-purchase van 30 naar 7 dagen | Dan krijgen herhaalkopers P1-REPEAT, de beste mail ($4,31 per ontvanger). Geschat +$900 tot $1.800. | UI, 5 min |
| R4 | C2 checkout naar 48 uur (T22) | C2 heeft 2,38% afmeldingen per mail. Voor nieuwe aanmelders is het de 3e mail in 26 uur. | UI |
| R5 | TP · B2-NOTCLICKED op Manual | 0,50% spam, boven de Gmail-grens van 0,3%. | API, akkoord nodig |
| R6 | T02 op 100% code tot 6 dec | Met code: 2,6% klik en $0,81 per ontvanger. Zonder code: 1,1% klik en $0,14 per ontvanger (klik p=0,008). | API |
| R7 | 6 FTL-mails zonder omzet op Draft vóór 1 nov | Ongeveer 3.000 mails per dag voor $0,012 per ontvanger. | API, akkoord nodig |

## Top 10 tests

| # | Test | Flow | Extra per week | Start | Beslissen | Bouw |
|---|---|---|---|---|---|---|
| 1 | BFCM-reeks (3 mails) naar ~38.000 eerdere kopers, 15% holdout | kopers | $1.500 tot $4.000 | akkoord vóór 4 nov, mails 13/27/30 nov | 7 dec | API (draft) |
| 2 | Q1: W1-onderwerp "Your 10% works on top of the sale" | welcome | $630 tot $1.580 | 29 okt (T04 dicht met A) | 19 nov | API (variatie patchen), anders UI |
| 3 | T21: HI10 al toegepast in K1 | cart | $200 tot $1.100 | na akkoord (tegen besluit 8 okt) | dec | UI |
| 4 | BR1: B1 met saleprijs plus HI10 | browse + TP | $110 tot $260 (nov $220 tot $520) | 1 nov | dec | template API, start UI |
| 5 | T15: dekselkaart in P1-FIRST | post-purchase | $450 tot $900 | 1 nov | dec | UI |
| 6 | T23: cartmail dag 7 over betalen in termijnen, 50% holdout | cart | $200 tot $600 | 1 nov | dec | UI |
| 7 | Q2: W5 als Black Friday vroege toegang | welcome | $200 tot $560 | live uiterlijk 5 nov | na BFCM | UI, BF-datum nodig |
| 8 | Winback met saleaanbod als haak (vaste wissel, geen A/B: te weinig volume) | winback | $300 tot $700 | 3 tot 6 nov | dec | API/UI |
| 9 | BR3: setaanbeveling in B2-NOTCLICKED | browse | $80 tot $205 | 5 nov | dec | UI, setprijs nov nodig |
| 10 | T24: checkoutmail dag 14 over termijnen | checkout | $120 tot $300 | 1 nov | dec | UI |

Daarna, na BFCM:
- T05b (W1, social proof)
- T17 (W2 "A note from Benjamin")
- BR2 (B1-opbouw)
- T14/T18 (C1/K1-onderwerp)
- T07 (W3-hero)
- T19 (B2 garantie of social proof)
- C2-onderwerp (T26)

## Kalender

- 29 okt: T04 dicht met A, Q1 start, herinstap post-purchase naar 7 dagen.
- 30 okt: C2 naar 48 uur, FTL inkorten, Smart Sending aan in sunset.
- 1 nov: BR1, T15, T23, T24 en, na akkoord, T21.
- 3 tot 6 nov: saleblok in P3 en winback; W5 als vroege toegang live.
- 5 nov: BR3.
- 13, 27, 30 nov: kopersmails BFCM.
- 13 nov tot en met 1 dec: sunset pauze.
- 20 nov tot en met 1 dec: bevriezing. Geen nieuwe tests; BFCM-dagen apart rapporteren.
- 2 dec: sunset met suppressie en 10% controle.
- 7 dec: alles beslissen en de volgende ronde starten.

## Meten

- Omzet per ontvanger is op dit volume alleen bij W1 te bewijzen. De rest beslissen we op unieke klik, met omzet als richting en afmelding en spam als bewakers.
- Geen automatische winnaar (PLAYBOOK 6).

## Open bij Floris

1. Einddatums van de Halloween- en novembersale, en de datum van Black Friday vroege toegang.
2. Stapelt de Snowball-korting van 15% op de sale?
3. Blijven de "4 gifts" na 31 okt? Anders gaat de regel uit checkout en cart.
4. Blijft de set in november $299?
5. Akkoord op R1 tot en met R7 en tests 1 tot en met 10.
