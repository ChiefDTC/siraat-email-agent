# Welcome-audit en herbouw voor Black Friday (7 nov 2026)

Doel: omzet per ontvanger van de welcome (flow T4a5Mk, "v4 · Welcome") van ongeveer $1.07 naar $1.75+ tijdens de VIP Black Friday-sale (tot 70% off plus 4 gifts, geen einddatum in flowmails). Benchmark in het account: BF-W1 in flow Rn556d, $3.58 per ontvanger.
Bron: Klaviyo API (alleen GET en rapporten), flow-values-report 24 okt t/m 7 nov 2026, conversiemetric Placed Order (RSNxYV). Niets gewijzigd in Klaviyo, geen testmails.

## 1. Opbouw van T4a5Mk (live)

Trigger: lijst Uw8eZG. Flowfilter: e-mail bevat geen `test@`, nooit eerder in de flow.

1. Split 119850648: 100% naar het nieuwe pad (oude pad "Old · Welcome 1..8" krijgt geen nieuwe instroom; resten lopen nog uit).
2. Wacht 5 minuten.
3. Uitstapsplit 119850651: eruit als (a) Placed Order sinds flowstart, of (b) een mail uit Rn556d ontvangen in de laatste dag.
4. Split 119850653: ooit besteld? Ja: **W0** "Thank you. Now the first egg." (TPiMrZ), einde. Nee: verder.
5. **W1**, A/B 119850659 (handmatig, winnaar op unieke kliks): A "No PFAS. Here's the paper. Up to 70% off." (Sq2bvX), B "The Black Friday Sale is live" (XMAs8s). Extra filters: geen order sinds start, geen mail uit checkout QUBUQV of cart TZG9Mx in de laatste dag.
6. Dag 1, 10:00: **W2** "The pan nobody else was making" (VjPTKM), afzender Benjamin.
7. Dag 3, 09:00: **W3** "Has your cookware been tested?" (VCjUYQ).
8. Split op profielland (US of United States, anders INT).
9. Dag 6, 09:00: **W4-US** (SWZdPy) en **W4-INT** (XV8AC3) "Who are you cooking for?".
10. Dag 10, 09:00: **W5** "Tammy is on her fourth pan" (US UZU8qz, INT VVrcgf). Einde.

Geen mail heeft een eigen verzendfilter na W1; de stop op "besteld" zit alleen in de uitstapsplit vooraan.

## 2. Cijfers per mail (24 okt t/m 7 nov 2026)

| Mail | Wanneer | Ontvangers | Open | Klik | Orders | Omzet | Per ontvanger | Uitschr. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| W0 (bestaande klant) | 5 min | 101 | 60.4% | 6.93% | 2 | $1,177 | $11.65 | 0.00% |
| W1 (A/B) | 5 min | 12,334 | 44.8% | 3.91% | 117 | $37,237 | **$3.09** | 1.69% |
| W2 | dag 1 | 9,316 | 40.9% | 2.36% | 16 | $4,302 | $0.47 | 1.30% |
| W3 | dag 3 | 9,343 | 37.8% | 1.24% | 13 | $4,604 | $0.50 | 0.94% |
| W4-US | dag 6 | 5,416 | 35.9% | 1.29% | 3 | $995 | $0.19 | 0.46% |
| W4-INT | dag 6 | 3,920 | 35.4% | 1.54% | 2 | $401 | $0.10 | 1.03% |
| W5-US | dag 10 | 3,936 | 35.4% | 0.54% | 2 | $279 | $0.07 | 0.79% |
| W5-INT | dag 10 | 3,179 | 34.8% | 1.17% | 2 | $270 | $0.09 | 0.63% |
| Oud 6, 7, 8 (uitloop) | | 3,059 | | | 3 | $1,425 | $0.47 | |
| **Totaal T4a5Mk** | | **50,684** | | | **160** | **$50,690** | **$1.00** | |
| BF-W1 (Rn556d, benchmark) | 0 min | 6,458 | 36.6% | 4.11% | 70 | $23,136 | **$3.58** | 1.62% |

Dagelijkse ontvangers (flow-series-report) laten zien dat de welcome leegloopt sinds Rn556d op 6 nov naar 100% ging:

| | 1 nov | 3 nov | 5 nov | 6 nov | 7 nov |
| --- | ---: | ---: | ---: | ---: | ---: |
| BF-W1 | 533 | 691 | 904 | 1,554 | 1,381 |
| W1 | 1,361 | 714 | 895 | 452 | 212 |
| W2 | 905 | 638 | 588 | 645 | 306 |

## 3. Wat de mails zeggen en waar de knop heen gaat

- **W1**: kop "The sale of the year. No PFAS, and here is the paper.", aanbod in de hero en in de onderwerpregel, labrapport 25895, vergelijking met een PFAS-pan, 4 gifts-raster, 2 reviews. Knoppen naar /collections/black-friday-sale, tekstlink naar het labrapport. Werkt: $3.09.
- **W2**: korte brief van Benjamin (waarom de pan, 75 jaar, labrapport), de sale staat in de P.S. en in een donker blok eronder, daarna het gifts-raster. Eén knop naar de sale-collectie. Geen product, geen prijs.
- **W3**: "Six things you can check yourself": zes bewijspunten, certificaat, drie reviews, gifts-raster. Het labrapport krijgt 4 links, de sale 2. Geen product, geen prijs.
- **W4-US/INT**: maatkiezer Mini, Small, Standard, Large plus de 6- en 12-delige set (12 alleen US). Goede opbouw, maar bij elk product staat alleen "In the Black Friday Sale": geen prijs, geen percentage.
- **W5**: drie klantverhalen (Michael G., Gwen, Tammy), twee beloftes, twee reviews, sale-blok onderaan, gifts-raster. Eén knop naar de sale-collectie. Geen product.
- **BF-W1** (benchmark): onderwerp "You're just in time", preview "Your prices: up to 70% off. No code needed", eerste regel is het aanbod, direct daaronder vier productkaarten met prijs, doorgestreepte compare-at en 70% OFF-tag (Pan Pro Standard $144, 6-delige set $299, 12-delige set $649, Wok $119), drie iconen (100,000+, 75 jaar, 30 dagen), één zin van Benjamin. 12 productlinks plus de collectie. Kort, geen uitleg.

Waarom BF-W1 beter is: het aanbod staat in onderwerp, preview en eerste scherm; de lezer ziet meteen een concreet product met een prijs en de besparing; elke kaart is een eigen route naar een productpagina (minder stappen dan via de collectie); er is niets te lezen voordat je kunt kiezen.

## 4. Diagnose

1. **Omzet zit in één mail.** W1 levert 73% van de omzet. W2 t/m W5 krijgen 35,110 ontvangers (69% van het volume) en halen samen $11,151: **$0.32 per ontvanger**. Klik zakt van 3.9% (W1) naar 2.4%, 1.2%, 1.3% en 0.5 tot 1.2%.
2. **De staart verkoopt niet.** In W2, W3 en W5 staat geen enkel product en geen prijs; W4 heeft producten zonder prijs. Elke mail heeft dezelfde generieke knop naar de collectie. De onderwerpregels van W2 t/m W5 noemen de sale niet (W2 zet hem zelfs in de P.S.). In W3 gaan meer links naar het labrapport dan naar de sale. Het gifts-raster staat in elke mail en maakt ze lang zonder nieuw argument.
3. **De welcome loopt leeg, en daarna komt niets.** Sinds 6 nov krijgt elke nieuwe aanmelder BF-W1 en verlaat daardoor de welcome bij split 119850651. W1 zakte van 1,361 per dag naar 212, W2 volgt. Nieuwe aanmelders krijgen nu BF-W1 (dag 0), BF-W2 (dag 1, live sinds 7 nov) en BF-W3 (dag 2) en daarna geen flowmail meer. Over ongeveer tien dagen draait de staart van T4a5Mk nog op een paar honderd mensen. Het doel van $1.75 moet dus gemeten worden over de hele aanmeldreis (Rn556d + YqKCmH + staart), niet over T4a5Mk alleen.
4. **Wat ontbreekt** (afgezet tegen BF-W1): aanbod in het eerste scherm (W2, W5), productfocus met prijs (alle vier), één primaire actie per mail met productkaarten als route, urgentie zonder datum (alleen W5 heeft de ware "laatste mail"), sociaal bewijs dat bij de claim past (W3 en W5 hebben reviews, maar bij geen enkel product).
5. **Uitschrijvingen** op W1 (1.69%) en W2 (1.30%) liggen boven de 1%-grens uit PLAYBOOK 6. BF-W1 zit op 1.62%. Bewaken in de test.

## 5. Wat er veranderd is per mail

Bron: `klaviyo/templates/v3/flows-nov/welcome/_tools/make_welcome.py` (hergebruikt de helpers van homestead-e5-e6 en de vaste header en footer). Uitvoer `wn2..wn5-us|int.html`, `.klaviyo.html`, `-preview.html`; screenshots in `welcome/previews/` op 375 en 600 px. Gecontroleerd: geen horizontale overloop, 0 kapotte beelden, elk beeld en het hele hero-beeld klikbaar, hoogte 2,700 tot 3,530 px op 375 px (onder de 3,600), geen streepjes, geen einddatum, geen code, geel alleen op de 70% OFF-tags, topbalk en knoppen ink.

Gemeenschappelijk: hero met het aanbod in het glaspaneel ("VIP Black Friday"), direct daaronder in US de prijs met doorgestreepte compare-at en de tag (zelfde catalogusbedragen als BF-W1), dan de primaire knop met friction reducer. Productkaarten met prijs (US) of 70% OFF (INT) en elk een eigen link. Eén primaire knop, boven en onder herhaald. Gifts als één regel in plaats van het raster (behalve in de bon van wn3). Elke mail een ander idee dan BF-W1/W2/W3, zodat ze ook als vervolg na BF-W3 kunnen draaien. Geen 12-delige set, geen bedragen en geen US-macro's in INT.

| Slot | Oud | Nieuw (wn) | Verwacht effect |
| --- | --- | --- | --- |
| W2 | Brief, sale in de P.S., geen product | **"The one pan I'd buy at 70% off"** (B: "December 20, 2024"), afzender Benjamin. Eén product: de Pan Pro Standard ($144, was $480) boven de vouw, het verhaal in drie zinnen (eerste pan, 20 december 2024, geen coating), vier feiten, één eerlijke beperking (voorverwarmen), review Gwen, daarna 6- en 12-delige set. | Klik van 2.4% naar het niveau van W1 (3.5 tot 4%) omdat er meteen iets te kiezen is; omzet per ontvanger $0.47 naar ongeveer $1.20 |
| W3 | Zes bewijzen, geen product | **"What 70% off actually gets you"** (B: de letterlijke review "Expensive but definitely Value for money"). Het grootste bezwaar (prijs, enquête) beantwoord met de bon van de 6-delige set: $997 naar $299, gifts met waarde, garantie en retour, "Value $1,067 / Your price $299", onder $100 per pan met deksel. Bewijs in één alinea (BF-W3 doet het uitgebreid). Review Lorraine. Daarna Pan Pro en 12-delige set. | Hogere orderwaarde (set als hoofdproduct); $0.50 naar ongeveer $1.00 |
| W4 | Maatkiezer zonder prijs | **"Who are you cooking for?"** (onderwerp blijft, zodat de inhoud het verschil maakt; B: "Every size is 70% off"). Vier maten met maat in de naam ({{SIZE}}), prijs en tag, plus 6- en 12-delige set, gifts-regel, reviews Michael G. en Tammy. | Van 1.3% klik met bijna geen orders naar kopers die hun maat al kozen; $0.19/$0.10 naar ongeveer $0.80 |
| W5 | Drie verhalen, geen product | **"My last welcome email (and 70% off)"** (B: "Tammy is on her fourth pan"), afzender Benjamin. "Where I'd start": Pan Pro, 6-delige set, Deep Pan (from $119), 12-delig in US, één verhaal (Tammy), twee beloftes, echte laatste mail als enige urgentie, P.S. "no code needed". | $0.07/$0.09 naar ongeveer $0.60 |

De schattingen zijn aannames (geen meting): ze gaan uit van de structuur van BF-W1 bij een lezer die later in de reis en minder warm is. Rekenvoorbeeld voor de reis: BF-W1 $3.58 en vier vervolgmails van gemiddeld $1.10 bij 75% bereik geeft (3.58 + 4 × 0.75 × 1.10) / 4 = **$1.72 per verstuurde mail**, tegen nu $1.00. Haal je $1.75 niet met de staart alleen, dan zit de rest in BF-W2/BF-W3 (nog geen cijfers).

## 6. Voorstel A/B: nieuw tegen huidig

**Waar.** Omdat nieuwe aanmelders de welcome verlaten, kan de test niet in de huidige staart van T4a5Mk draaien. Voorstel (Floris zet het in de UI; Claude mag live flows niet wijzigen):

1. In YqKCmH na BF-W3: wacht 1 dag, dan een `profile-sample` 50%-split (werkt via de API, PLAYBOOK 12), dan de bestaande land-split.
2. **Arm A (huidig):** kopieën van de huidige W2, W3, W4-US/INT en W5-US/INT op dag 3, 5, 7 en 9.
3. **Arm B (nieuw):** wn2, wn3, wn4 en wn5 (US/INT) op dezelfde dagen en uren (10:00, 09:00).
4. Elke mail een verzendfilter "Placed Order = 0 sinds flowstart" (nu zit die alleen vooraan), plus "geen mail uit checkout of cart in de laatste dag" zoals W1.
5. Previewteksten en onderwerpen zoals in de meta van elke bron (`SUBJECT A`, `PREVIEW`). Geen automatische winnaar.

Alternatief: in T4a5Mk de voorwaarde "mail uit Rn556d" uit split 119850651 halen en de staart naar dag 3 en later schuiven. Meer werk en meer risico op dubbele mails met BF-W2/BF-W3; niet aanbevolen.

**Hoe beoordelen.**
- Primair: omzet en orders per profiel dat de split binnenkomt, binnen 14 dagen na de split, op profielniveau (zelfde methode als de Rn556d-vergelijking met hulpsegment WXWtRc). Daarnaast de flow-toegeschreven omzet per ontvanger per arm (flow-values-report per flow_message_id).
- Secundair: unieke klik per mail, orderwaarde.
- Vangrails per mail: uitschrijving boven 1% is een probleem (PLAYBOOK 6), spam boven 0.157% (welcome-norm uit november-plan). Arm B stopt als een mail twee dagen achter elkaar boven die grens zit.
- Steekproef: ongeveer 6,500 aanmelders per week, dus ~3,200 per arm. De huidige staart zet ongeveer 0.4% van de profielen om. Om een verdubbeling (0.4% naar 0.8%) met 80% power te zien zijn ~5,900 profielen per arm nodig: ongeveer 2 weken. Start rond 10 nov, eerste beslissing rond 24 nov, de rest van de sale op de winnaar.
- Dit is een pakkettest (vier mails tegelijk). Wint B, dan daarna per slot de onderwerpregel testen (A/B in de meta).

## 7. Open punten voor Floris

1. **Prijzen in US.** De nieuwe mails tonen in US prijs en compare-at zoals BF-W1. BF-W2/BF-W3 en E5/E6 zijn op verzoek zonder bedragen. Eén schakelaar `PRICES_US` in make_welcome.py geeft de prijsloze versie.
2. **Topbalk.** Ink met crème tekst (DECISIONS 5 nov). BF-W2/BF-W3 hebben sinds 7 nov een oranje balk; voor één lijn in de reis kan dezelfde override als in make_bfw.py.
3. **Figma.** De rij in Figma (bestand oaxnBkz3MAbePRnorCrQwz, regel 4 nov) is nog niet gemaakt.
4. **Klaviyo.** Templates aanmaken, de test in YqKCmH bouwen en live zetten: Floris (of Claude in gewone modus met akkoord).
