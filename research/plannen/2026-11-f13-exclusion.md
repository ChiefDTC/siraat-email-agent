# F13 (LUCKY20): wie sluiten we uit? (13 nov 2026)

Vraag van Floris: recente kopers die nog op een backorder wachten krijgen anders "extra 20% off today" na een volle aankoop. Risico op annuleringen, boze tickets en price-match verzoeken.

## Data (Klaviyo, events 14 okt t/m 13 nov 2026, exact, geen sampling)

- Placed Order (RSNxYV) laatste 30 dagen: 10,649 orders, 10,174 unieke profielen.
- Status per laatste order: Shopify Fulfilled Order (VtEiZT) op order-id gematcht, Cancelled Order (TFervq) apart. Fulfilled Partial Order telt als nog wachtend (er mist nog iets).
- Huidige audience na bestaande uitsluitingen (VSnBnJ, W3q7Zy, W4vNzF, XTpfNG, TLqivd): US 83,560, INT 52,973.

| | US | INT | Totaal |
|---|---|---|---|
| Kopers laatste 30 dagen in audience | 4,340 | 1,208 | 5,548 |
| waarvan laatste order nog niet fulfilled | 2,124 | 43 | 2,167 |
| ... order 0 tot 7 dagen oud | 78 | 4 | 82 |
| ... order 8 tot 14 dagen oud | 1,259 | 28 | 1,287 |
| ... order 15 tot 30 dagen oud | 787 | 11 | 798 |
| waarvan laatste order fulfilled | 2,047 | 1,158 | 3,205 |
| waarvan laatste order geannuleerd | 169 | 7 | 176 |

Van de 2,124 wachtende US-kopers heeft 1,697 al een deelzending gehad: de rest van hun order staat dus in backorder. Het probleem zit vrijwel helemaal in de US; INT is bijna volledig verzonden. (De 0 tot 7 groep is klein omdat TLqivd die al uitsluit; de rest valt op de rand van het 7-dagenvenster.)

## Opties

- **A: alle kopers laatste 30 dagen uitsluiten.** Verlies 5,548 profielen (US 4,340 = 5.2%, INT 1,208 = 2.3%, samen 4.1%).
- **B: alleen kopers met onvervulde laatste order (plus bestaande 7 dagen).** Verlies 2,167 profielen (US 2,124 = 2.5%, INT 43 = 0.1%, samen 1.6%). Als segmentregel "Placed Order in 30 dagen en Fulfilled Order 0 keer in 30 dagen" zijn dat 2,302 profielen.

Afweging: recente kopers converteren goed (187 van de 5,548 bestelden al 2 keer of vaker in 30 dagen), maar een prijsverlaging vlak na aankoop is de grootste klachtbron. B dekt de annuleringskans (je kunt alleen annuleren voor verzending). A dekt daarnaast ook price-match: met 30 dagen retour kan iedereen die in de laatste 30 dagen kocht terugsturen en opnieuw kopen met LUCKY20, dus voor die groep is de mail in feite een uitnodiging tot een refund van het verschil.

## Advies: optie A

A kost maar 3,381 profielen meer dan B (2.5% van de audience) en haalt het hele price-match risico weg, ook bij de 3,205 kopers die hun pakket wel hebben. Dat zijn kopers die net vol betaald hebben; hun extra omzet op deze ene mail weegt niet op tegen tickets en refunds in BF-week.

Klaar segment: **WFqvwp "Siraat // Buyers last 30 days (F13 exclusion)"** (Placed Order minstens 1 keer in de laatste 30 dagen, zelfde opbouw als TriYPe). Toevoegen als uitsluiting aan beide draft-campagnes (01M7ANQKQ2ZR413ZDVBN79JZ4W en 01M7ANQP4Y8G9PKT2B8JMG9CBB); TLqivd mag blijven staan. Campagnes zijn niet aangepast, Floris beslist.

Kiest Floris toch B: dan alleen de US-campagne relevant (INT 43 profielen), segment nog aanmaken met Placed Order minstens 1 keer in 30 dagen en Fulfilled Order 0 keer in 30 dagen.
