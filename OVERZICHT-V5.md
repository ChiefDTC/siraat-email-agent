# Siraat · Flow System v5: het complete overzicht

Stand: 8 oktober 2026. Alles staat als **concept (Draft)** in Klaviyo. Er is nog niets live en er gaat nog niets naar klanten.

---

## 1. In één alinea: waarom dit systeem bijzonder is

De meeste merken hebben één checkout-mail voor iedereen: dezelfde tekst, dezelfde pan, dezelfde dollars, dezelfde korting. Dit systeem kijkt bij elke mail naar **wie** de klant is, **wat** hij in zijn cart of order heeft, **wat hij al bezit**, **waar hij woont** en **welke fase** hij in zit, en bouwt daar de mail op. Een Australiër met een schort in zijn cart krijgt een andere mail dan een Amerikaan met de fall-set, en iemand die al drie pannen heeft krijgt nooit meer een pan aangeboden. Alles is eerlijk (geen nep-urgentie, alleen echte reviews), gebaseerd op jullie eigen data (12 maanden orders, 384 campagnes, de enquête van 349 klanten) en wordt gemeten met A/B-tests tegen de oude flows.

---

## 2. Wat er vandaag (7 en 8 oktober) allemaal is gebeurd

### Jouw input en besluiten
- **Feedback per flow** (vastgelegd in `research/v5/00-feedback-floris.md`): meer urgentie, gifts in plaats van korting vooraan, reviews op drie pijlers, directe vergelijking met PFAS-pannen, tailoring per product, bundel en markt, cross-sell, betere AI-beelden, VIP en anniversary 15%, een vervolgflow na "keep me on the list".
- **Besluiten** (vastgelegd in `DECISIONS.md`):
  - $349-listing vervalt, alles linkt naar de fall-set van **$299** ("Buy 2, get 4 free", six pieces).
  - Gifts-urgentie: "your 4 gifts end when the fall sale ends" (fall sale loopt heel oktober).
  - Laatste codemail: "we're removing your discount" (waar: de unieke code vervalt echt).
  - Cart: **geen HI10 in K1 en K2**, eerste korting pas in K3. Checkout houdt HI10 in C1 t/m C3.
  - VIP en anniversary **15%** (coupon SK_ANNIV15_7D door jou aangemaakt).
  - **Duties paid in alle markten**, ook Canada. Verzendtekst: buiten de US "Free shipping", in de US "Free shipping from the US".
  - Gift-waarden per valuta (zie §5). Prijzen: Standard $144, Large $149, Pro Duo $199 (Mini + Standard + 2 deksels).
  - Vergelijking mag direct "PFAS pan" noemen.
  - Benjamins verhaal in W2 (PFAS twee jaar geleden, van snijplank naar pan, zes maanden testen).
  - Nachtelijk bezit-script mag, en moet elke dag gecontroleerd worden.

### Wat er gebouwd en gedaan is (op volgorde)
1. **Export en eerste bouw** van de flows in Klaviyo als concept, met een QA-poort zodat een kapotte mail nooit meer naar Klaviyo kan.
2. **Fixes**: de foute Klaviyo-tag die de preview brak, de ruwe weergave in de editor, de afgesneden pan in de vergelijkingstabel.
3. **Landsplit vereenvoudigd**: in plaats van vier keer dezelfde tak kiest de mail zelf.
4. **Onderzoeksagents** (allemaal in `research/`):
   - klantbegrip uit de enquête (PFAS is koopreden nr. 1, prijs het enige echte bezwaar)
   - beste mails ooit (384 campagnes, 160 flowmails)
   - concurrenten (Graza, HexClad, Made In en anderen via Email Love)
   - inbox en deliverability (Gmail, dark mode, Outlook, frequentie)
   - onderwerpregel-lab (320 historische onderwerpen)
   - personalisatie en kooppatronen (90.513 orders)
   - meetsysteem voor de A/B-tests
   - bottom-up omzetmodel
   - kritische audit vóór livegang
5. **v5-ronde na jouw feedback**: zeven agents voor markten en valuta, reviews, bundels en korting, copy en urgentie, cross-sell, AI-beelden (maken + onafhankelijk controleren) en de sunset-vervolgflow. Daarna een bouwronde in drie stappen: gedeelde bouwstenen, alle 61 mails, integratie.
6. **Bezit-sync**: 98.691 klantprofielen kregen een lijst van wat ze bezitten; elke nacht om 03:27 bijgewerkt.
7. **Klaviyo**: 61 templates bijgewerkt, 13 flows als concept, segmenten aangemaakt, coupons gecontroleerd.
8. **Figma**: alle 61 v5-mails en flowkaarten bijgewerkt.

---

## 3. De 13 flows en wanneer welke mail komt

Alle tijden zijn in de tijdzone van de klant. "Tot 09:00" betekent dat vervolgmails 's ochtends landen, nooit 's nachts. Elke verkoopmail stopt zodra iemand bestelt.

| Flow | Start als | Mails en timing | ID |
|---|---|---|---|
| **Checkout abandonment** | Checkout gestart, niet betaald | C1 na 30 min · C2 na 1 dag · C3 dag 3 om 09:00 · C4 dag 5 om 09:00 (laatste, eigen code) | QUBUQV |
| **Cart abandonment** | Product in cart, geen checkout | K1 na 30 min · K2 na 1 dag · K3 dag 3 om 09:00 (eerste korting) | TZG9Mx |
| **Browse abandonment** | Product bekeken | B1 na 1 uur · B2 dag 2 om 09:00 (wie klikte: eigen code) | WdRz5k |
| **Welcome** | Inschrijving (Alia) | W1 na 20 min · W2 dag 1 (Benjamin) · W3 dag 3 · W4 dag 6 · W5 dag 10 | T4a5Mk |
| **Post-purchase** | Bestelling | P1 na 1 uur · P2-safe dag 17 als nog niet geleverd · P3 dag 21 (cross-sell, eigen 10%) | X3ySuU |
| **Post-purchase · levering** | Pakket geleverd | P2 "first egg" de dag erna om 09:00 | VQ93sx |
| **Winback** | Bestelling, dan stilte | R1 dag 45 · R2 dag 75 (10% of 15% voor terugkerende klanten) | UyFc78 |
| **VIP** | Tweede bestelling | V1 dag 30 (15% exclusive) · V2 dag 40 (vraag van Benjamin) | VTkxFL |
| **Anniversary** | Eerste bestelling met kookgerei | N1 na 6 maanden · N2 na 1 jaar (15%) | XbYT7T |
| **Site abandonment** | Op de site, niets bekeken | A1 na 2 uur · A2 dag 2 | VLGhbR |
| **Sunset** | 120 dagen geen klik, geen bezoek, geen order | S1 · S2 ("last email unless you tap") | TbYQmX |
| **Sunset · kept** (nieuw) | Klikte in de sunset-mail (geen bot) | S3 na 30 min · S4 dag 4 | Wzz6xC |
| **UGC first egg** | Pakket geleverd | U1: "cook something, reply with a photo, 15% on your next order" | VPixnJ |

**Voorrang**: iemand zit nooit in twee verkoopflows tegelijk. Post-purchase gaat boven alles, dan checkout, cart, browse, welcome. Wie net een checkout-mail kreeg, krijgt geen browse-mail.

---

## 4. Alle scenario's: wat krijgt wie?

### Per product (wat de klant in de cart heeft of kocht)
| Klant heeft | Wat de mails doen |
|---|---|
| **Pan Pro** (Mini, Small, Standard, Large) | PFAS-vergelijking, maat in jouw eenheid, deksel in de juiste maat, de Mini als aanvulling (Small → Mini 39%, Standard → Mini 20%) |
| **Fall-set** (3 pannen + 3 deksels) | "Buy 2, get 4 free. Six pieces for $299", what's in the box, rekensom per markt; nooit nog een Small/Mini aanbieden |
| **Andere sets** (12-delig, Complete, Pro Duo, Kit) | Eigen inhoud en rekensom per bundel; 12-delig alleen in de US |
| **Schort** | Schortverhaal (canvas, verstelbaar, cadeau), geen panuitleg; daarna pas de pan als tweede stap |
| **Accessoire** (plank, utensils, molen, sheets) | Verhaal over dat accessoire; nieuwe klant krijgt daarna de pan, bestaande eigenaar niet |
| **Gift card** | Eigen regel, bedragen alleen in de US |
| **US-only** (12-delig, potten, roasting pan, 2 Pans + 2 Lids) | Verschijnen nooit bij klanten buiten de US |

### Nieuwe klant tegen bestaande klant
- Elke nacht weet Klaviyo wat iemand bezit (`siraat_owned`). Daardoor:
  - iemand met een deksel in de checkout die al een pan heeft krijgt de eigenaarsversie;
  - VIP, winback en anniversary bieden nooit iets aan dat de klant al heeft;
  - geen "first egg" of care-video aan iemand die al maanden kookt.

### Korting: wie krijgt wat en wanneer
| Flow | Eerste korting | Vorm |
|---|---|---|
| Checkout | HI10 automatisch in C1 t/m C3 (jouw besluit) | C4: eigen 10%-code, 48 uur, "we're removing your discount" |
| Cart | Pas in K3 | Eigen 10%-code, 48 uur |
| Browse | B2, alleen wie in B1 klikte | Eigen 10%-code, 48 uur |
| Welcome | HI10 | Openbare welkomstcode |
| Post-purchase | P3 dag 21 | Eigen 10%, 14 dagen |
| Winback | R2 | 10% (72 uur) of 15% exclusive voor terugkerende klanten |
| VIP | V1 | 15% exclusive, 14 dagen |
| Anniversary | N2 | 15%, 7 dagen |

**Cooldown**: wie in de laatste 30 dagen al een eigen code kreeg (en die gebruikte), krijgt de versie zonder code. VIP krijgt de 15% ook als de vorige code ongebruikt bleef. Zo stapelen we geen kortingen.

**Test code tegen geen code (T02)**: bij elke laatste codemail krijgt de helft de code en de helft niet. Zo zien we of de korting zichzelf terugverdient.

---

## 5. Valuta en markten: hoe het werkt

### Het probleem
55% van de orders komt van buiten de US (UK 14%, Australië 12%, Singapore 4%, Canada 3%, VAE 2%, Hongkong 2%, Nieuw-Zeeland 2%). De oude mails toonden iedereen dollars, inches, "$70 in gifts" en US-only producten.

### Hoe de mail het land bepaalt (per flowtype het betrouwbaarste signaal)
| Flow | Signaal |
|---|---|
| Checkout | De valuta van de checkout (USD telt alleen als US bij een US- of leeg profielland) |
| Cart | Het IP-land van de bezoeker |
| Post-purchase, winback, VIP, anniversary | Het verzendland van de order |
| Browse, welcome, site, sunset, UGC | Het land op het profiel |

### Wat er per markt verandert
| Markt | Prijzen | Gifts | Waterfilter | Maten | Verzendregel |
|---|---|---|---|---|---|
| US | $ | $70 | $450 | 11″ | Free shipping from the US |
| Canada | C$ | C$95 | C$620 | 28 cm | Free shipping, duties paid |
| VK | £ | £55 | £350 | 28 cm | Free shipping, duties paid |
| Europa | € | €70 | €410 | 28 cm | Free shipping, duties paid |
| Australië | A$ | A$100 | A$660 | 28 cm | Free shipping, duties paid |
| Nieuw-Zeeland | NZ$ | NZ$120 | NZ$820 | 28 cm | Free shipping, duties paid |
| Singapore | S$ | S$95 | S$590 | 28 cm | Free shipping, duties paid |
| Hongkong, Midden-Oosten, Noorwegen, rest | geen bedrag | "4 free gifts" | geen bedrag | 28 cm | Free shipping, duties paid |
| Land onbekend | geen bedrag | "4 free gifts" | geen bedrag | 28 cm (11″) | Free shipping |

Prijzen komen uit de productcatalogus (`content/catalog/products.json`, 64 producten, 15 landen), niet meer hard in de mail. De fall-set kost bijvoorbeeld $299 in de US, £249 in het VK en A$449 in Australië.

---

## 6. Wat erin zit dat het sterk maakt

1. **Urgentie die waar is**: de echte vervaldatum van de eigen code (met tegels: 48 UUR · VR · 10 OKT), "your 4 gifts end when the fall sale ends", "we're removing your discount". Nooit "your cart will be deleted" (Shopify bewaart de cart) of nep-countdowns.
2. **Gifts vooraan in plaats van korting**: in checkout en cart zijn de 4 gifts (met beelden en waarde per markt) de haak, de korting komt pas aan het eind.
3. **Reviews op drie pijlers**: kwaliteit, levering en service, uit 734 echte reviews (289 bruikbaar). Geen review twee keer achter elkaar, de zwakke "scrambled eggs"-review is weg, verdachte reviews worden niet gebruikt.
4. **Klanttaal uit de enquête**: PFAS-vrij met Light Labs-rapport 25895 als hoofdidee; prijs beantwoord met waarde ("15 coated pans, or one") en in de US met termijnbetaling.
5. **Verhaallijn in plaats van herhaling**: Benjamins tijdlijn (PFAS, snijplank, zes maanden testen, 20 december 2024, 100,000+ klanten) loopt over de mails heen, en elke flow vergelijkt met iets anders (PFAS-pan, roestvrij staal, gietijzer). 24 herhalingen zijn eruit.
6. **Cross-sell op echte kooppatronen**: P3, winback, VIP en anniversary bieden het logische volgende product (deksel in jouw maat, de Mini, de fall-set) en nooit wat je al hebt.
7. **Beelden die kloppen**: alle 16 oude AI-beelden hadden de hamerslag aan de buitenkant. Opnieuw gemaakt met de echte pan als voorbeeld, onafhankelijk gecontroleerd: 13 goed, 3 afgekeurd en vervangen door echte foto's.
8. **Techniek die je niet ziet maar die het verschil maakt**:
   - QA-poort: geen enkele mail kan naar Klaviyo met een fout, losse code, verkeerde maat, dollars buiten de US of een open placeholder. Elke mail wordt in zeven markten getest.
   - Werkt in Gmail (geen afknippen), dark mode, Outlook en op mobiel.
   - Codes zijn uniek, één keer bruikbaar, combineerbaar met de gratis gifts.

---

## 7. Hoe we meten: de A/B-tests

| Test | Waar | Wat |
|---|---|---|
| **T01** oud tegen nieuw | Checkout, cart, browse, welcome | 50% krijgt de oude flow, 50% de nieuwe. Zo meten we of v5 echt meer oplevert. |
| **T02** code tegen geen code | Elke laatste codemail | Verdient de korting zichzelf terug? |
| **T04** | Welcome W1 | Twee versies van de eerste welkomstmail |
| **T05a** | Browse B1 | Twee onderwerpen ("Get this pan with 10% off" tegen "Why I started making this pan") |

Beslisregels: alleen op maandag kijken, de eerste 14 dagen niets beslissen, vroeg stoppen alleen bij 99% zekerheid, op de einddatum wint een versie bij 95%. BFCM (20 november t/m 6 december) telt apart. Script: `scripts/test_report.py`.

Verwachte extra omzet (bottom-up model, per jaar): realistisch +$1,0 mln, ambitieus +$2,45 mln volgens Klaviyo-toeschrijving; ongeveer de helft daarvan is echt extra. De T01-test laat zien hoeveel.

---

## 8. Wat er nog moet gebeuren vóór live

**Jij**
- [ ] Bij de 9 coupons in Klaviyo de vervaltijd goed zetten en "Product and collection coupons" aanvinken.
- [ ] In het sunset-segment "Created · is at least 120 days ago" toevoegen (de API weigerde dat).
- [ ] Lekcodes in Shopify uitzetten (100%-codes, BFEXTRA10, NTWDHPKL5C, NYEXTRA10, EXTRA30).
- [ ] Vier oude naflows uit vóór post-purchase live gaat (FREE E-GUIDE, E-Book, Pan Education, Mystery Gift).
- [ ] T2SmtR: voorwaarde toevoegen (zie `exports/GO-LIVE.md` stap 8).
- [ ] Afspraak met Homestead over wie campagnes verstuurt.
- [ ] Testcheckouts doen met lolagroothuis+pan@gmail.com, +set, +schort, +int.
- [ ] Bestandsnaam in Figma naar "v5".
- [ ] Vraag: mag de Pan Pro een doorgestreepte prijs van $288 tonen?

**Ik**
- [ ] Testronde: flow op Manual, jouw testcheckouts volgen in Klaviyo, Gmail en Shopify; controleren dat code, vervaldatum, land en productblokken in het echt kloppen.
- [ ] Bij livegang: per groep in dezelfde minuut nieuw aan en oud uit, daarna 24 uur later controleren dat elke 50/50-split in beide kanten mensen heeft.

---

## 9. Waar alles staat

| Wat | Waar |
|---|---|
| Alle besluiten | `DECISIONS.md` |
| Jouw feedback v5 | `research/v5/00-feedback-floris.md` |
| Markten en valuta | `research/v5/01-markten.md`, `content/catalog/` |
| Bundels, korting, klantherkenning | `research/v5/02-bundels-korting-klanten.md` |
| Copy en urgentie per mail | `research/v5/03-copy-spec.md` |
| Cross-sell | `research/v5/04-cross-sell.md` |
| Beelden | `research/v5/05-beeld-*` |
| Sunset kept | `research/v5/06-sunset-kept.md` |
| Bezit-sync | `research/v5/07-sync-owned.md` |
| Reviews | `content/reviews/` |
| Flowopbouw per mail | `exports/live/flows/OVERZICHT.md` |
| Go-live-checklist | `exports/GO-LIVE.md` |
| Figma | https://www.figma.com/design/ahGP2wWoVIif8ETXcBq1Dj |
