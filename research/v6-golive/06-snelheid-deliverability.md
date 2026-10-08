# 06 · Snelheid en deliverability vóór de livegang van de 13 flows

Datum: 8 oktober 2026 (avond). Alleen gelezen: Klaviyo REST (GET, plus de leesquery's metric-aggregates en flow/campaign-values-reports, revision 2025-10-15), openbare DNS (8.8.8.8 en 1.1.1.1) en de beelden zelf (gedownload en gemeten). Niets gewijzigd in Klaviyo, niets geüpload. Bouwt voort op `research/lijst/02-deliverability.md` (7 okt) en `research/deliverability/01-inbox-check.md` (7 okt, v4-mails).

Bronnen in deze map:
- `06-mails.csv`: alle 100 mailacties uit de 13 Draft-flows (83 v5-templates en 17 "Old ·"-templates van de T01-controle-arm), per mail HTML-grootte, beeldgewicht, grootste beeld, formaten, hosts, live tekst, onderwerp, preview en Smart Sending.
- `compressed/`: 33 gecomprimeerde kopieën (21 v5, 12 oude arm) (alleen ter beoordeling, niets vervangen of geüpload).

Meetmethode HTML: de echte template-HTML uit Klaviyo (`GET /api/templates/{id}`), lokaal gerenderd met de Django-motor van `scripts/qa_render.py` op alle voorbeeld-events per trigger en alle zeven markten (US, UK, AU, CA, SG, EU, onbekend); per mail telt de zwaarste variant. "Geschat verzonden" = quoted-printable + 600 bytes per link (Klaviyo-klikredirect) + 0,5 KB (zelfde formule als `scripts/inbox_checks.py`).

---

## Stoplicht in één oogopslag

| # | Onderdeel | Stand | Kern |
|---|---|---|---|
| 1a | Gmail-clipping (102 KB) | **GROEN** | v5: 21 tot 50 KB geschat verzonden (mediaan 39). Oude arm: max 81 KB (Old · Checkout 2). |
| 1b | Beeldgewicht v5-mails | **ORANJE** | Mediaan 280 KB per mail, prima. Uitschieters: W0 1,34 MB en P2/P2-SAFE 0,89 MB door drie GIF's; 16 hero's tussen 200 en 292 KB. |
| 1c | Beeldgewicht oude T01-arm | **ORANJE** | Bestaande mails, niet nieuw, wel zwaar: Old · Welcome 7 laadt 4,5 MB (Shopify-originelen van 3000 tot 4000 px), Welcome 4/5/6 een ticker-GIF van 1,57 MB. |
| 1d | CDN, formaten, externe requests | **GROEN** | v5-beelden 100% via Klaviyo-CDN (`cdn.klaviyomail.com`), JPEG/PNG/GIF, max 1200 px. 12 tot 19 beelden plus 1 Google Fonts-import per mail. |
| 2a | SPF, DKIM | **GROEN** | Eigen verzenddomein `send.siraatskitchen.com`, DKIM `kl`/`kl2` op het eigen domein (aligned). Ongewijzigd sinds 7 okt. |
| 2b | DMARC, BIMI | **ORANJE** | `p=none`, rapporten naar de registrar (reportdmarc.nl), geen BIMI. Voldoet aan het Gmail/Yahoo-minimum; geen blokkade voor morgen. |
| 2c | One-click unsubscribe en voorkeuren | **GROEN** | Alle 100 mails hebben een uitschrijflink; alle 83 v5-mails ook "Manage preferences". Klaviyo zet List-Unsubscribe-Post zelf. |
| 2d | Preheaders | **ROOD** (1 fix) | B2-CLICKED (2 berichten in Browse WdRz5k) heeft als preview letterlijk `Already applied. On {day} morning, we remove it.` Moet vóór live. Verder: controleren in de testronde of de preview niet dubbel komt. |
| 2e | Onderwerpen, spamwoorden, tekst/beeld, alt | **GROEN** | v5 schoon (geen "Last chance", geen "!", geen FREE in onderwerp). Alt overal; 1.600 tot 2.700 tekens live tekst. Oude arm wel "Last Call ... !", "Expires Tonight", `Hi {{ first_name }},` zonder default. |
| 3a | Volume bij livegang, warm-up | **GROEN** | Netto ongeveer -1.000 tot +1.000 mails per dag op ~69.000 per dag (±1,5%). Geen warm-up nodig, mits niemand "Add past profiles" gebruikt. |
| 3b | Huidige reputatiecijfers | **GROEN / ORANJE** | 30 dagen: spam 0,040%, bounce 0,17% (hard 0,037%), uitschrijving 0,51%. Outlook 0,16% spam (was 0,31% in Q3). Checkout-mails: 18 tot 20% bounce op de eerste mail. |
| 4a | Sunset (WuHSm6, 75.424) | **ORANJE** | 35% van de Email List (215.033) is 120 dagen niet betrokken. De flow pakt alleen nieuwe instromers; de 75k moeten apart en gedoseerd. Suppress-segment bestaat nog niet. |
| 4b | Frequentie flows + campagnes | **ROOD** | Campagneplafond en welkomstbescherming bestaan nog niet als segment; 8 van 29 campagnes in 30 dagen met Smart Sending uit; piekweek 4,4 mails per ontvanger. |
| 4c | Smart Sending in flows | **ORANJE** | Uit in alle 100 berichten (bewust, vervangen door profielfilters). Aanzetten voor de niet-tijdkritische flows. |
| 4d | Quiet hours | **GROEN** | Alle wachttijden in profieltijdzone, dagmails om 08:00 tot 10:00; alleen directe mails (30 min tot 2 uur na een actie) volgen het moment van de klant. |
| 4e | Apple MPP en opens | **ORANJE** | 86% van de open-events heeft geen e-mailclient (machine/proxy); 39% van de kliks is een botklik. Sturen op menselijke kliks; de v4-segmenten doen dat al. |

---

## 1. Laadsnelheid

### 1a. Gmail-clipping: GROEN

| Groep | Mails | Geschat verzonden (min · mediaan · max) | Ruwe HTML max |
|---|---|---|---|
| v5-templates | 83 | 21 · 39 · 50 KB (W4-US) | 31 KB |
| Oude T01-arm ("Old ·") | 17 (4 niet lokaal te renderen, Klaviyo-eigen filters) | 44 · 55 · 81 KB (Old · Checkout 2) | 72 KB |

Grens Gmail ~102 KB. Ruimste marge: ruim 50 KB bij elke v5-mail. Het verschil tussen ruwe template (tot 77 KB, P3-PAN) en verzonden mail komt doordat de marktlogica bij verzending wegvalt; alleen de tak van de klant blijft over.

### 1b en 1c. Beeldgewicht en top 10

Top 10 zwaarste mails van alle 100 (beeldgewicht van de zwaarste variant; dit is wat een lezer bij openen laadt):

| # | Mail | Flow | Beeld totaal | Grootste beeld | HTML geschat |
|---|---|---|---|---|---|
| 1 | Old · Welcome 7 | Welcome (T01 oud) | **4.511 KB**, 25 beelden | 564 KB, 3000x3000 JPEG (Shopify-origineel, plus twee van 3794 en 4000 px) | 78 KB |
| 2 | Old · Welcome 4 | Welcome (T01 oud) | 3.022 KB | 1.573 KB GIF 1200x100, 410 frames (ticker) | 44 KB |
| 3 | Old · Welcome 6 | Welcome (T01 oud) | 2.949 KB | zelfde ticker-GIF | 44 KB |
| 4 | Old · Welcome 5 | Welcome (T01 oud) | 2.927 KB | zelfde ticker-GIF | 47 KB |
| 5 | Old · Welcome 8 | Welcome (T01 oud) | 2.630 KB | 767 KB PNG 1200x620 | 53 KB |
| 6 | Old · Checkout 5 | Checkout (T01 oud) | 1.752 KB | 653 KB PNG 1200x3186 | 57 KB |
| 7 | Old · Checkout 2 | Checkout (T01 oud) | 1.617 KB | 1.457 KB PNG 1200x3506 | 81 KB |
| 8 | Old · Welcome 3 | Welcome (T01 oud) | 1.497 KB | 601 KB PNG 1200x1504 | n.v.t. |
| 9 | **W0** | Welcome (v5) | **1.340 KB** | 664 KB GIF 960x420, 14 frames (ei in de pan), plus 396 KB GIF | 38 KB |
| 10 | Old · Welcome 1 | Welcome (T01 oud) | 1.121 KB | 445 KB PNG 1200x1331 | 46 KB |

Zwaarste v5-mails daarna: P2-SAFE 890 KB en P2 888 KB (GIF 560 KB, 840x368, 14 frames), R1-ACC 466 KB, K1 437 KB, W3 430 KB, W4-US 394 KB. Mediaan v5: 280 KB; de lichtste (V2, S2, S3, S4) 24 KB.

**Hero-regel (< 200 KB, max 1200 px breed).** Alle v5-hero's zijn JPEG van 1200 px breed (1200x900 of 1200x1200). 16 van de 110 unieke v5-beelden zitten boven 200 KB, hoogste 292 KB (R1-ACC), dan W3 274, P2-SAFE 246, W5 245, R1-PAN 239, P3-APRON 236/238, P2 236, N2 228/232, V1 217/219, K2-NEW 211, P3-NEXT 205/207, K1 202. Geen enkel v5-beeld is breder dan 1200 px. De oude arm gebruikt PNG voor foto's (tot 1.457 KB) en drie Shopify-originelen van 3000 tot 4000 px.

### 1d. Formaat, CDN en externe requests: GROEN

- v5: 82 JPEG, 25 PNG (iconen, logo's, vergelijkingskop; de grootste PNG is 71 KB), 3 GIF, geen WebP (goed: Outlook desktop toont geen WebP).
- Hosts: v5-beelden komen allemaal van `cdn.klaviyomail.com`; productbeelden uit het event (cart/checkout) van `cdn.shopify.com` met `&width=200/600`. Oude arm: `d3k81ch9hvuctc.cloudfront.net` (oudere Klaviyo-CDN) en drie Shopify-originelen zonder breedteparameter.
- Externe requests per v5-mail: 12 tot 19 beelden, 1 Google Fonts-CSS (Gmail negeert die, Apple Mail laadt hem plus 2 fontbestanden), 1 open-pixel. Geen scripts, geen achtergrondbeelden, geen derde partijen.
- Laadtijd: 280 KB is op 4G ruim onder een seconde; Gmail cachet beelden via zijn proxy. Snelheid is voor de v5-mails geen probleem, alleen voor W0, P2/P2-SAFE en de oude welcome-mails merkbaar op een trage verbinding.

### Compressievoorstellen (kopieën in `compressed/`)

| Wat | Nu | Kopie | Hoe | Raakt |
|---|---|---|---|---|
| W0 GIF ei-in-pan (aba7aa86) | 664 KB, 960 px | **388 KB**, 600 px | 600 px breed (de mail is 600), 48 kleuren, fuzz 8% | W0 |
| W0 tweede GIF (6706f177) | 396 KB | **241 KB** | idem | W0 |
| P2 GIF (6953bf24) | 560 KB, 840 px | **398 KB**, 600 px | idem | P2, P2-SAFE |
| 18 v5-hero's > 195 KB (16 boven 200) | 197 tot 292 KB | **142 tot 195 KB** | JPEG progressive, q78 (q70 tot q74 waar nodig) op 1200 px; vier zeer gedetailleerde (R1-ACC, W3, P2-SAFE, P3-APRON x2) op 1000 px q78 | R1-ACC, W3, P2-SAFE, W5, R1-PAN, P3-APRON (2), P2, N2 (2), V1 (2), K2-NEW, P3-NEXT (2), K1, N1, U1 |
| Oude arm: 12 zwaarste beelden | 9.033 KB samen | **2.525 KB** | PNG-foto's naar JPEG q80; Shopify-originelen naar 1200 px; ticker-GIF als stilstaand frame (6 KB) | Old · Welcome 1/3/4/5/6/7/8, Old · Checkout 1/2/5 |

Effect: W0 van 1.340 naar ~909 KB, P2 en P2-SAFE van ~890 naar ~730 KB, de 16 hero-mails elk 30 tot 120 KB lichter, Old · Welcome 7 van 4,5 naar ~3,1 MB (met alle oude beelden als JPEG op 1200 px onder 1,5 MB). Alleen de GIF's en de oude arm leveren echt snelheid op; de hero-winst is klein (13 tot 40%), de foto's zijn al redelijk gecomprimeerd.

Kanttekeningen: de GIF-kopieën hebben minder kleuren (licht zichtbare banding in de rook/stoom), even naast het origineel bekijken. De oude arm is de controlegroep van T01; beelden comprimeren verandert niets aan inhoud of opmaak, maar wie de test zuiver wil houden laat die arm zoals hij is (hij draait nu ook al zo live). Advies: GIF's en hero's na de eerste meetweek vervangen, oude arm pas als T01 klaar is of nooit.

---

## 2. Gmail en Google

"Indexeren" bestaat in Gmail niet zoals bij zoeken: Gmail beslist per bericht over inbox, Promotions of spam op basis van authenticatie, de reputatie van domein en verzenddomein (Postmaster Tools), en vooral of ontvangers openen, klikken, verwijderen of spam melden. Promotions is voor marketingmail normaal en geen straf. De knoppen die we hebben: authenticatie, klachten laag houden en niet-betrokkenen niet blijven mailen (deel 4).

### 2a/2b. DNS (8 okt, live opgevraagd)

| Record | Waarde | Oordeel |
|---|---|---|
| Afzender | flows: `send@siraatskitchen.com`, naam "Siraat's Kitchen" (94) of "Benjamin at Siraat's Kitchen" (6), reply-to `support@siraatskitchen.com`; accountstandaard nog "SiraatsKitchen" | Goed in de flows. Accountstandaard alleen relevant voor campagnes die hem overnemen |
| Verzenddomein | `send.siraatskitchen.com` CNAME `u161779.wl030.sendgrid.net`, SPF `v=spf1 include:sendgrid.net ~all`, MX `mx.sendgrid.net` | GROEN, SPF aligned (relaxed) |
| DKIM | `kl._domainkey` en `kl2._domainkey` CNAME naar SendGrid, 2048-bit RSA-sleutels geldig | GROEN, d=siraatskitchen.com |
| SPF hoofddomein | `v=spf1 a mx include:spf.mijndomeinhosting.nl ~all` | Klaviyo hoeft er niet in |
| DMARC | CNAME naar `dmarc-none.mijndomein.nl`: `p=none; sp=none; adkim=r; aspf=r; rua=mailto:dmarc@reportdmarc.nl` | ORANJE: voldoet, maar rapporten gaan naar de registrar |
| BIMI | geen `default._bimi` | Pas na `p=quarantine` en een VMC/CMC |
| Google-verificatie | `google-site-verification=2gm2...` op het hoofddomein | Onbekend of dit Postmaster Tools of Search Console is: Floris checkt |
| Shopify/Gorgias-DKIM | niet gevonden (`shopify`, `gorgias`, `google`, `s1`, `s2`, `k1`) | Uitzoeken vóór DMARC strenger wordt |

### 2c. One-click unsubscribe: GROEN

Alle 100 templates bevatten `{% unsubscribe %}`; de 83 v5-templates ook `{% manage_preferences_link %}` ("Manage preferences"); de 17 oude alleen uitschrijven. Klaviyo zet `List-Unsubscribe` en `List-Unsubscribe-Post` zelf; in de laatste drie maanden liep 48% van de uitschrijvingen via one-click (02-deliverability §6). Controle in de testronde: in Gmail "Show original", zoek `List-Unsubscribe=One-Click`.

### 2d. Preheaders: ROOD door één fout

- **Fout:** in Browse WdRz5k hebben de berichten "CODE · B2-CLICKED · pan" en "CODE · B2-CLICKED · acc" als flow-preview `Already applied. On {day} morning, we remove it.` De `{day}` komt letterlijk uit de bron-topcomment (`klaviyo/templates/v3/browse/b2-clicked.html`) en wordt in de flow-preview niet vervangen. De template zelf rendert de dag wel goed in zijn verborgen preheader. Fix: preview in beide berichten vervangen door bijvoorbeeld `Already applied. In 48 hours we remove it.` (zelfde vorm als C4), en in `build_flows.py` een controle op `{` in preview en onderwerp.
- Elke v5-mail heeft de preview twee keer: in het flowbericht (`preview_text`) én als verborgen div bovenaan de template (identieke tekst, op B2 na). Als Klaviyo de flow-preview ook invoegt, kan Gmail "tekst · tekst" tonen. In de testronde één mail in Gmail en Apple Mail bekijken; komt hij dubbel, dan `preview_text` in de flowberichten leegmaken (de template-preheader blijft).
- Lengte: 48 tot 87 tekens, niets afgekapt op desktop; op mobiel zien lezers 35 tot 50 tekens, de belangrijkste woorden staan vooraan. De opvulling na de preheader is kort (8 keer `&nbsp;&zwnj;`): bij korte previews (C1, 55 tekens) loopt Gmail door in de codebalk ("STILL PENDING ON YOUR CART · $70 IN GIFTS", in hoofdletters). Voorstel: opvulling naar ~90 paren in `build_template.py` (+1 KB).
- W2 mist `mso-hide:all` op de preheader (Outlook desktop kan hem tonen). Klein.

### 2e. Onderwerpen, spamwoorden, tekst/beeld, alt: GROEN

- v5-onderwerpen: 16 tot 40 tekens, geen uitroeptekens, geen "free", geen "last chance" (C4/K3 zijn nu "We're removing your discount in 48 hours" en "We're removing your cart's 10%"). Mild: "15% exclusive discount, 72 hours" (R2-VIP), "Your 10% expires in 72 hours" (R2), "You're a VIP" (hoofdletters is een afkorting, prima).
- Oude T01-arm (bestaande mails): "Last Call for 10% Off!", "We've cooked something for you!", preview "Expires Tonight" (Old · Checkout 5, Old · Welcome 8), en `Hi {{ first_name }}, ...` zonder default in Old · Cart 1 en 2 (wordt "Hi , we saved these" bij profielen zonder naam). Niet aanpassen tijdens T01, wel weten.
- Tekst tegenover beeld: 1.600 tot 2.700 tekens live tekst per v5-mail (V2 en sunset ~900 tot 1.300), beeld 12 tot 19 stuks; geen enkele mail is een groot beeld. De oude arm heeft soms maar 50 tot 350 tekens live tekst (alles in beeld).
- Alt-teksten: 807 beelden met alt, 735 lege alts op kleine of decoratieve iconen (correct), 4 lege alts op een beeld van 100 px of groter (het vergelijkingskopje `adf1c2fa...png`), 0 zonder alt-attribuut.
- Gmail Promotions-annotaties (JSON-LD met DiscountOffer of PromotionCard): niet aanwezig. Optioneel, alleen zinvol voor de codemails (C4, K3, B2-CLICKED, R2, P3, V1, N2) en pas na livegang.

---

## 3. Volume en reputatie bij livegang

### 3a. Hoeveel mail komt erbij: GROEN, geen warm-up nodig

Basis: 8 sep tot 8 okt 2026. Nu ~69.000 mails per dag: campagnes 1,86 mln in 30 dagen (62.000 per dag, 36 campagnes), flows 306.000 (10.200 per dag). Instroom per dag (uniek, US/Eastern): Checkout Started 287, Added to Cart 245, Viewed Product 1.010, Active on Site 1.396, Placed Order 161, Delivered Shipment 84, nieuwe inschrijvers Email List ~610.

| Groep | v5-flow | Vervangt (30 d verzonden) | Nu per dag | v5 geschat per dag | Verschil |
|---|---|---|---|---|---|
| A | Welcome T4a5Mk | SiaNLu 71.180 | 2.373 | 2.000 tot 2.600 (T01: oude arm 8 mails, nieuwe 5 + W0) | ~0 |
| A | Checkout QUBUQV | Y2TmNB + Tsg2tV 8.933 | 298 | 300 tot 400 (75 tot 85 echte verlaters x 4 mails) | +50 |
| A | Cart TZG9Mx | SwkMyn + TBWngE 10.677 | 356 | 300 tot 400 | ~0 |
| A | Browse WdRz5k | Wj6x6V + TyEjuQ 27.879 | 929 | 800 tot 1.100 | ~0 tot +150 |
| (A) | Failure to launch T2SmtR blijft, alleen oude arm (GO-LIVE stap 8) | 112.891 | 3.763 | ~1.900 na 30 dagen | **-1.900** (geleidelijk) |
| B | Post-purchase X3ySuU + levering VQ93sx | RL3TU6 18.954 | 632 | ~400 (P1 160, P2 85, P3 150 vanaf dag 21) | -230 |
| B | Winback UyFc78 | UEfh4h 15.298 | 510 | 0 de eerste 45 dagen, daarna ~290 | **-510**, later -220 |
| C | Site VLGhbR | nieuw | 0 | 200 tot 500 (A1, A2; streng gefilterd) | +200 tot +500 |
| C | Sunset TbYQmX + kept Wzz6xC | S7V4a7 7.613 | 254 | 250 tot 600 (alleen nieuwe instromers) | 0 tot +350 |
| C | VIP VTkxFL, UGC VPixnJ, Anniversary XbYT7T | nieuw | 0 | 50 tot 120; anniversary pas vanaf april 2027 | +50 tot +120 |
| | **Totaal** | | **~9.100** | **~6.300 tot 8.600** (zonder T2SmtR-halvering ~8.200 tot 10.500) | **-2.800 tot +1.400** |

Dat is hooguit 2% van het dagvolume, kleiner dan de gewone schommeling tussen campagneweken (340.000 tot 740.000 per week). Een warm-up is dus niet nodig. Drie dingen kunnen dat wel veranderen:
1. **"Add past profiles"** op Welcome, Sunset of Sunset · kept. Op Sunset zou dat 75.424 niet-betrokkenen in één keer S1 en S2 sturen: 150.000 mails naar precies de groep die 82% van de klachten geeft. Nooit doen; zie 4a voor de gedoseerde route. Metric-getriggerde flows nemen standaard alleen nieuwe events.
2. **Oude naflows**: OVERZICHT-V5 §8 zegt "vier oude naflows uit vóór post-purchase live" (E-Book TSUnLs, Free E-Guide YyaMjx, Pan Education YcXbHx, Mystery Gift WvRupU, samen ~1.000 per dag), GO-LIVE stap 9 zegt "blijven ongewijzigd live". Floris beslist; blijven ze aan, dan krijgen kopers P1 plus een naflow op dezelfde dag.
3. **Winback-gat**: met UEfh4h uit en UyFc78 pas na 45 dagen eerste mail, krijgen kopers van augustus en september geen winback. Bewust kiezen, of UEfh4h laten lopen tot de eerste R1 verstuurd is (eind november, midden in BFCM).

### 3b. Reputatie laatste 30 dagen

| | Ontvangen | Bounce (hard) | Spam | Uitschrijving | Menselijke kliks |
|---|---|---|---|---|---|
| Alles | 2.063.918 | 0,17% (0,037%) | 0,040% (825) | 0,51% | 12.709 unieke klikkers; 39% van alle kliks is een botklik |
| Campagnes | 1.861.236 | 0,08% | 0,025% | 0,40% | klikratio 0,71% |
| Flows | 306.419 | 0,71% | 0,056% | 0,94% | klikratio 1,96% |

Per provider (spamklachten worden alleen door Microsoft, Yahoo en Comcast teruggemeld): Hotmail/Outlook 440 op 275.908 = **0,16%** (Q3 was 0,31%, verbetering), Yahoo/AOL 352 op 378.078 = 0,09%, Gmail 1,11 mln ontvangen en niet zichtbaar zonder Postmaster Tools.

Per huidige flow (de flows die morgen vervangen worden):

| Flow | Ontvangers | Bounce | Spam | Uitschrijving |
|---|---|---|---|---|
| Welcome SiaNLu | 71.180 | 1,01% | **0,102%** | **1,82%** |
| Browse Wj6x6V | 13.709 | 0,55% | **0,125%** | 1,51% |
| Cart SwkMyn | 9.374 | 0,58% | 0,097% | 1,23% |
| Checkout Y2TmNB | 5.658 | **6,47%** | 0 | 1,17% |
| Post-purchase RL3TU6 | 18.954 | 0,43% | 0,064% | 0,65% |
| Winback UEfh4h | 15.298 | 0,33% | 0,013% | 0,48% |
| Failure to launch T2SmtR (blijft) | 112.891 | 0,47% | 0,038% | 0,46% |

**Checkout-bounces.** De eerste mails van de oude checkout halen 17,8 tot 19,7% bounce (Y2TmNB-berichten R4g5Wr, RZ4Urm, RpzC3U); de audit zag bij C1 16 tot 17%. Oorzaak: in de checkout getypte of nep-adressen die nog nooit mail kregen. C1 van v5 krijgt dezelfde instroom, dus ~15 tot 20 bounces per dag. In het totaal (0,17%) valt dat weg en Klaviyo onderdrukt een hard bounce direct, maar het is het eerste cijfer om te volgen. Boven 20% op C1: filter "Bounced Email = 0 keer ooit" helpt niet (nieuwe adressen); wel Shopify-adresvalidatie in de checkout of een botfilter op Checkout Started.

---

## 4. Open-behoud

### 4a. Sunset en wat WuHSm6 betekent: ORANJE

Segment "v4 · Sunset · unengaged 120d" (WuHSm6): **75.424 profielen**, 35% van de Email List (215.033) en ~45% van wie nu mail ontvangt. Definitie (klopt, en de voorwaarde "profiel minstens 120 dagen oud" staat er nu in): mag marketing ontvangen, meer dan 7 mails in 120 dagen, 0 keer Active on Site en 0 menselijke kliks in 120 dagen, 0 orders in 180 dagen.

Wat dat betekent:
- Deze groep krijgt nu elke campagne naar de volle lijst (Uw8eZG is in 30 dagen 6 keer de hele doelgroep geweest). Ze kosten reputatie zonder op te leveren: 82% van de spamklachten komt van profielen zonder menselijke klik in 90 dagen (02-deliverability §6).
- De Sunset-flow is segment-getriggerd en neemt alleen wie er vanaf livegang nieuw in valt. De 75.424 van vandaag krijgen dus niets, tenzij iemand "Add past profiles" doet (niet doen, zie 3a).
- Na S2 zonder klik moeten ze echt van de lijst. Het segment "v4 · Sunset · suppressed" uit GO-LIVE stap 3 bestaat nog niet; zonder dat segment en de wekelijkse bulk-suppress blijven ze campagnes krijgen.

Voorstel voor de bestaande 75k: per direct uitsluiten van alle campagnes (exclusie WuHSm6). Daarna in batches van ~10.000 per dag een sunset-campagne (S1-inhoud, dan S2 na 4 dagen) naar wie in WuHSm6 zit, kliks bewaren, de rest suppressen. Netto wordt de campagnelijst ~35% kleiner; de omzet daalt nauwelijks (geen order in 180 dagen, geen klik in 120), open- en klikratio's stijgen, en Gmail ziet minder ongeopende mail.

### 4b. Frequentie per persoon per week: ROOD

- Nu: 2,3 tot 2,9 mails per ontvanger per week, piek 4,4 (week van 28 sep: 740.725 mails aan 167.058 mensen), waarvan ~90% campagnes. Eerste week oktober tot nu 1,8.
- Met de flows erbij (scenario's uit 01-inbox-check §6): actieve shopper zonder aankoop 8 tot 9 in 7 dagen (6 flowmails plus 3 campagnes), oude T01-arm met T2SmtR tot 10. Uitschrijving springt van 0,98% naar 1,60% bij 3 naar 4 mails per week (timing-onderzoek).
- Flowfilters zijn goed (checkout wijkt voor post-purchase, cart voor checkout, browse voor cart/checkout/welcome, site voor alles, sunset voor welcome/post-purchase). Wat ontbreekt zit aan de campagnekant: de segmenten "v4 · Campagne-cap" en "v4 · Welcome-bescherming" uit GO-LIVE stap 3 bestaan niet (gecontroleerd in de segmentenlijst). De laatste Homestead-campagne (8 okt, "October Email 1") gaat naar "HS // Engaged 180 Days Email" met Smart Sending aan: goed, maar zonder die twee uitsluitingen.
- Smart Sending stond in 8 van 29 campagnes van de laatste 30 dagen uit (o.a. Sunday Recipe Day 4 okt, Prime Sale US/INT 2-3 okt, Founder Note Sale 30 sep, Resend to Non-Openers 29 sep).

### 4c. Smart Sending in flows: ORANJE

Uit in alle 100 berichten. Voor checkout, cart, browse, welcome, P1/P2 en sunset is dat juist (tijdgevoelig of de logica hangt aan de verzending). Aanzetten (16 uur) voor wat geen haast heeft: Site A1/A2, Winback R1/R2, VIP V1/V2, Anniversary N1/N2, P3-varianten, UGC U1. Een overgeslagen mail kost daar weinig, een vijfde mail op één dag wel.

### 4d. Quiet hours: GROEN

Alle wachttijden in de tijdzone van het profiel. Dagmails vallen om 08:00 (cart), 09:00 (meeste) of 10:00 (welcome). Directe mails (W1 20 min, C1/K1 30 min, B1 1 uur, P1 1 uur, A1 2 uur) volgen het moment waarop de klant actief was; C2 komt exact 1 dag na de checkout, op hetzelfde kloktijdstip. Let op: zonder bekende tijdzone valt Klaviyo terug op US/Eastern; voor AU/NZ/SG (16% van de orders) is 09:00 Eastern 's avonds of 's nachts. Kleine groep, wel in de testronde met een AU-profiel kijken.

### 4e. Apple MPP en opens: ORANJE, sturen op kliks

Van 1,08 mln open-events in 30 dagen heeft 86% geen e-mailclient (machine-opens: Apple Mail Privacy, beveiligingsscanners, proxies); "Gmail image proxy" is 9,5%. Openratio's van 33 tot 58% zeggen dus weinig. Klikratio's (0,3 tot 1,4% campagnes, 0,35 tot 10% flows) en orders zijn de maat; daarbij 39% botkliks eruit filteren (`Bot Click = false`). De v4-segmenten (sunset, kept, T01-rapportage) gebruiken al menselijke kliks en sitebezoek. Campagnes als "Resend to Non-Openers" werken door MPP slecht: de echte niet-openers met iPhone tellen als geopend en krijgen de resend niet, de rest krijgt hem dubbel.

---

## 5. Acties

### Vóór livegang (morgen)

| # | Wie | Wat | Waar |
|---|---|---|---|
| 1 | Floris (UI) of Claude (na "ga") | Preview van "CODE · B2-CLICKED · pan" en "· acc" vervangen: `Already applied. In 48 hours we remove it.` | Klaviyo, flow WdRz5k, beide berichten, Content > Preview text |
| 2 | Floris | Op Sunset TbYQmX, Sunset · kept Wzz6xC en Welcome T4a5Mk **geen** "Add past profiles" bij het live zetten | Klaviyo, flow-instellingen |
| 3 | Floris | Beslissen over de vier oude naflows (OVERZICHT-V5 zegt uit, GO-LIVE zegt aan) en over het winback-gat (UEfh4h tot eind november laten lopen of niet) | Klaviyo, flows TSUnLs, YyaMjx, YcXbHx, WvRupU, UEfh4h |
| 4 | Floris + Homestead | WuHSm6 uitsluiten bij elke campagne vanaf de eerste na livegang; Smart Sending altijd aan | Klaviyo, campagne > Recipients |
| 5 | Floris (UI) | Segmenten aanmaken: "v4 · Campagne-cap" (Received Email ≥ 3 in 7 dagen, flows meegeteld) en "v4 · Welcome-bescherming" (lid Uw8eZG < 14 dagen, geen order); bij elke campagne uitsluiten | Klaviyo, Segments; GO-LIVE stap 3 |
| 6 | Claude, testronde | Eén mail per groep in Gmail en Apple Mail: preview niet dubbel, `List-Unsubscribe=One-Click` aanwezig, DKIM `d=siraatskitchen.com` pass, beelden laden; een AU-testprofiel voor de tijdzone | Gmail "Show original" |

### Na livegang

| # | Wie | Wanneer | Wat | Waar |
|---|---|---|---|---|
| 7 | Claude | +1 uur, +24 uur, daarna dagelijks 14 dagen | Per bericht bounce, spam, uitschrijving. Alarm: C1 bounce > 20%, spam > 0,08% per flow, uitschrijving > 2% per mail | flow-values-report; `scripts/test_report.py` uitbreiden |
| 8 | Floris | deze week | Google Postmaster Tools koppelen voor `siraatskitchen.com` en `send.siraatskitchen.com` (kijken of de bestaande google-site-verification daarvoor is); Microsoft SNDS | postmaster.google.com |
| 9 | Floris | week 1 | Eigen DMARC-record i.p.v. de CNAME naar mijndomein, rua naar een eigen adres of DMARC-dienst; na 2 tot 4 weken rapporten `p=quarantine; pct=25`, later BIMI | DNS bij mijndomein |
| 10 | Claude (na akkoord) | week 1 | Sunset-segment "v4 · Sunset · suppressed" en wekelijkse suppress-routine; bestaande 75k in batches van ~10.000 per dag door een sunset-campagne | Klaviyo segmenten, ROUTINES.md |
| 11 | Claude | na eerste meetweek | Gecomprimeerde W0- en P2-GIF's en de 18 hero's uploaden en in de templates vervangen (eerst Floris laten kijken naar `compressed/`) | `klaviyo/templates/v3/*/assets`, export --update |
| 12 | Claude | na eerste meetweek | `build_template.py`: preheader-opvulling naar ~90 paren, `mso-hide:all` in W2; `build_flows.py`: weigeren als preview of onderwerp `{` bevat | scripts |
| 13 | Floris (UI) | na eerste meetweek | Smart Sending aan voor Site, Winback, VIP, Anniversary, P3, U1 | Klaviyo, per bericht |
| 14 | Claude | na T01 | Oude arm afbouwen of de zware oude beelden vervangen (Old · Welcome 7: 4,5 MB) | Klaviyo |
| 15 | Claude | optioneel, na BFCM-voorbereiding | Gmail Promotions-annotatie (JSON-LD DiscountOffer) in de codemails testen | templates C4, K3, B2, R2, P3, V1, N2 |
