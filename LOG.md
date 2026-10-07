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

- Content-index gebouwd (CONTENT-INDEX.md): Drive-mappen, Notion-databases en pagina's, Homestead-docs, Figma en MCP-bronnen in kaart. Officiële logo's in `brand/logo/`. Brand Guidelines v1.4 gelezen en samengevat in het playbook (claims, pijlers, voice, aanbod).
- Vondst: de Homestead Flow Doc is een leeg sjabloon. Hun flow-copy is nooit gedocumenteerd; de enige bron is Klaviyo zelf. De Copy Doc bevat wel alle campagnes van september en oktober.
- Vondst: de welcome-pop-up geeft een giveaway-lot, geen kortingscode. De welkomstreeks mag dus niet openen met een aanbod.

- Welcome Flow v2 ontworpen en in een nieuw Figma-bestand gezet: https://www.figma.com/design/74S1Tjr8BkSgQfm6vLnrLo (pagina 01 Flow: schema met trigger, drie splits, wachttijden; pagina 02 Emails: E0 tot en met E6 met echte foto's, reviews en producten). Spec en volledige copy in klaviyo/flows/01-welcome-v2.md. Twee onderzoeken erbij in research/.
- Diagnose oude welcome: 8 mails in 10 dagen, allemaal beeldslices, mail 1 na 5 minuten met code HI10 die de pop-up niet meer belooft; 2,7 procent uitschrijf op mail 1, 0,16 procent spamklachten. Afzender "Benjamin" terwijl de brand guidelines Floris noemen.
- Besluiten v2: 5 mails in 7 dagen (6 voor klikkers), geen code, aanbodblok wisselbaar, tak voor bestaande klanten, A/B op onderwerp mail 1, oprichter = Floris (te bevestigen).

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
- 2026-10-07 · Checkout-onderzoek geschreven (research/2026-10-07-checkout-abandonment.md): drie overlappende flows, helft krijgt 1 mail, 10%-codes stapelen op sale. Voorstel: 4 mails in 72 uur, merk plus korting in dollars. Welcome flow ontleed: 100%-split is dood hout, open-filters laten 8.000 mensen per maand mail 3 tot 5 overslaan, kopers krijgen niets. Overzicht van alle live flows in README gezet. Failure to launch: 107.520 mails, $3.608, 490 uitschrijvingen.
- 2026-10-07 · Homestead-PDFs gelezen (flow-aanbevelingen, welcome rebuild): diagnose klopt, oplossing aangepast (gift card i.p.v. HI10, kopers-pad, VS-split, geen non-stick-kop). Nieuwe Figma-file Welcome Flow v3 gebouwd (j3idDGYnRZBAJ13T5aL5vj): flow-diagram, 8 nieuwe mails naast 8 oude, content-inventaris. Spec in klaviyo/flows/01-welcome-v3.md. 10 open beslissingen voor Floris.
- 2026-10-07 · Email Design Kit gebouwd in Figma (PVyLDbrzyQB4RhEQGGW5HS): variabelen (13 kleuren, spacing, radius), 13 tekststijlen, 20 componenten (header, samengestelde hero, banners, label-pills, knoppen, productkaarten, review, vergelijkingstabel met de drie vragen, certificaat-blok, trust-rij, offer-blok, GIF-blok, founder note, checklist, footer), 6 heroes met echte TT Ramillas-koppen als PNG. Floris' 7 Slack-punten verwerkt in de kit (30-day returns, 75-year warranty, origineel sinds 20 dec 2024, HI10). Drive-shootmap (1eGJRW…) niet leesbaar via de koppeling: staat in een ander Google-account.
- 2026-10-07 · Vier content-agents klaar: reviews (605, 431 positief), claims en feiten (41 claims, 90 producten, beleid uit Shopify), hooks en video (69 hooks, 162 video's), foto-index (5.905 beelden). Koppel-agent: 22 mails in 6 flows gemapt met 20 unieke hero-foto's uit Shopify Files (content/mapping). DECISIONS.md aangelegd. Klaviyo-sleutel heeft nog geen campaigns/lists/forms-scope; shoot-mappen niet gedeeld met siraatskitchen@gmail.com.
- 2026-10-07 · Drive-netwerk open: High production shoot gelezen via openbare link. 29 beelden (14 shots, 3:2 en 1:1) in content/media/hp-shoot met contact sheet en gebruikstabel. Klaviyo-sleutel geeft nog steeds 403 op campaigns, lists en forms.
- 2026-10-07 · Klaviyo-sleutel werkt volledig (200 op campaigns, lists, forms). Pop-up blijkt Alia Card Game (US Evergreen), niet Klaviyo; alle Klaviyo-forms draft.
- 2026-10-07 · Voorbeeldmail C2 Why Siraat gebouwd als nieuwe standaard (template Yn7nyJ, niet live). 65 eigen beelden naar Shopify Files (email-*). Register af. Trustpilot nog geblokkeerd in deze container.
- 2026-10-07 · Baselines vastgelegd (baselines/, 90 dagen tot 6 okt): flows 10,8% van omzet, welcome $2,53 per nieuwe inschrijver, checkout-recovery 0,97%, campagnes tekst $0,118 vs beeld $0,080 per ontvanger, uitschrijf 0,54%, spam 0,042%. C2-voorbeeld in Figma kit (04 Samples).
