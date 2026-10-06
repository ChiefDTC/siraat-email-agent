# Logboek

Nieuwste bovenaan. Elke regel: datum, wat er gedaan is, wat het opleverde of wat we leerden.

## 2026-10-06

**Gedaan**
- Klaviyo-audit van alle flows en campagnes. Besluit: hero-afbeelding plus live tekst voor flows, afbeeldingsslices alleen voor campagnes. Homestead bouwde alles als 8 tot 15 beeldslices met één regel live tekst.
- Design system in Figma: Foundations (tokens, type), 21 componenten, samples (Welcome 01, Review request), fotopagina.
- Reviewmail "Win your purchase amount back" gebouwd als CODE-template S2tykT. Hero vierkant met TT Ramillas-kop als afbeelding, Inter voor tekst, vijf klikbare sterrenrijen, geen navigatie, geen footerblokken.
- Nieuwe reviewflow XzHrez aangemaakt via de API en live gezet: trigger Delivered Shipment, 14 dagen, geen herinstap, 12-delige set uitgesloten (drie titels), filters op ticket na bezorging, refund en volledige fulfilment. A/B-test op onderwerpregel (A "Win your purchase amount back", B "How was your experience?"), 50/50, winnaar op unieke kliks, gestart door Siraat in de editor.
- Oude reviewflow Vixr6X: template was om 17:46 vervangen door een conceptversie met placeholder-links. Siraat heeft de juiste template teruggezet (gecontroleerd in de HTML). E-mailstap gaat op 12 oktober op Draft; herinnering ingepland.
- Dagelijks Slack-rapport: eerste editie handmatig gepost in #claude-mail. Routine aangemaakt (08:52 Amsterdam) maar zonder connectors; moet opnieuw in de Routines-UI.

**Geleerd**
- Delivered Shipment (Shopify) is de betrouwbare bezorgtrigger: 3.360 in augustus, 2.880 in september, gelijk aan het ordervolume. Postflows-variant vuurt 2,5 keer zo vaak.
- Gorgias-tickets: 3.500 per maand, 2.300 unieke klanten. Een filter "nooit een ticket" sluit bijna iedereen uit. Alleen tickets ná bezorging tellen.
- Fulfilled Partial Order: 4.500 per maand, 2.000+ klanten. Zonder "volledig fulfilled"-filter krijgen deelzendingen een reviewverzoek te vroeg.
- Oude reviewflow (90 dagen): 10.784 mails, 50,3 procent open, 3,3 procent klik, 0,74 procent uitschrijf, $0,25 per ontvanger.
- Klaviyo kloont bij elke flow-koppeling de template. Een update van de bron komt niet vanzelf in de flow.
- De API kan een flow-A/B-test aanmaken maar niet starten. Variaties alleen via PATCH op de flow-action.
- AI-beelden: lettering op schortbandjes gaat altijd mis. Regel vastgelegd: geen tekst laten renderen.
- Auto-modus blokkeert wijzigingen aan live flows, ook met akkoord. Gewone modus gebruiken voor dat werk.

**Cijfers week 30 sep tot 6 okt (flows)**
- 75.633 ontvangers, $32.303 omzet.
- Welcome: 16.805, open 49,2, klik 1,4, uitschrijf 1,73, $11.982.
- Failure to launch: 28.171, open 33,0, klik 0,3, uitschrijf 0,45, $1.224.
- Cart Abandonment: 2.684, open 47,6, klik 2,2, uitschrijf 1,16, $3.737 ($1,39 per ontvanger, hoogste).
- Browse Abandonment (2 flows): 8.257, klik 2,1 tot 2,3, $7.134.
- Post Purchase: 5.134, open 56,7, klik 9,0, $819.

**Cijfers week 30 sep tot 6 okt (campagnes)**
- Founder-notes: 1,3 procent klik (Founder Note Sale 47.616 mails $4.624; Prime Sale INT 73.409 mails $9.662).
- Homestead-beeldmails: 0,3 tot 0,6 procent klik (Warehouse Clearance 116.433 mails $11.827; Sale Launch 4 Gifts 111.629 mails $2.822, open 20,5 procent).
