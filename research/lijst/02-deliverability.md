# 02 · Deliverability: authenticatie, klachten, bounces en wie er nog mail krijgt

Datum: 7 oktober 2026. Alleen gelezen: Klaviyo REST (GET, revision 2025-10-15) en Klaviyo MCP (metric aggregates, segmenten, campagnes), openbare DNS-lookups via de systeemresolver (8.8.8.8). Alleen aggregaten. Geen Google Postmaster Tools, geen Microsoft SNDS en geen Alia-toegang in deze sessie.

## Samenvatting

1. **Authenticatie is technisch in orde, het beleid niet.** SPF en DKIM staan goed voor Klaviyo (eigen verzenddomein `send.siraatskitchen.com`, DKIM-selectors `kl` en `kl2` op `siraatskitchen.com`, dus DKIM-alignment). DMARC staat op `p=none` en is een CNAME naar een standaardrecord van de registrar (mijndomein), met rapporten naar een adres van mijndomein. Siraat krijgt dus waarschijnlijk zelf geen DMARC-rapporten en heeft geen zicht op wie namens het domein mailt.
2. **De accountbrede spamratio (0,04 tot 0,05 procent) verbergt het echte cijfer.** Gmail en Apple sturen geen klachten per bericht terug naar Klaviyo. Gmail is 56 procent van alle verzonden mail, en telt in de noemer mee met nul klachten. Bij de providers die wel klachten terugmelden ligt de ratio in Q3 op **0,18 procent**; bij Hotmail/Outlook op **0,31 procent** (juli 0,50, september 0,22) en bij Yahoo/AOL op 0,11 procent. Gmail's eigen grens is 0,10 procent gewenst en 0,30 procent harde grens; het Gmail-cijfer zelf is alleen in Postmaster Tools te zien.
3. **Volume en frequentie zijn in september en oktober sterk gestegen.** Mails per week gingen van 150 tot 310 duizend (april tot augustus) naar 340 tot 740 duizend (september, eerste week oktober). In de week van 28 september kreeg elke ontvanger gemiddeld 4,4 mails, waarvan 4,1 campagnes. 10 van de 33 campagnes sinds 1 september hadden Smart Sending uit, waaronder vijf in die ene week.
4. **Een groot deel van de lijst is niet betrokken en krijgt toch alles.** Van de circa 167 duizend profielen die nog mail ontvangen, is 89.759 betrokken in 90 dagen (inclusief niet-machinale opens en sitebezoek); de rest, circa 77 duizend (46 procent), niet. Op kliks gemeten is het aandeel nog veel groter (zie paragraaf 6). Campagnes gaan in september naar de volledige Email List (`Uw8eZG`) of naar "EB | US Subscribers" zonder engagementfilter; het segment "Unengaged 180 Days" werd maar 7 van 81 keer uitgesloten.
5. **One-click unsubscribe werkt** (Klaviyo registreert `ONE_CLICK_UNSUBSCRIBE` als methode). Bounces zijn laag (0,17 procent in de laatste 4 weken, hard 0,04 procent). Het bot-klikaandeel stijgt wel, van 16 naar 32 procent van de klikkers: een teken dat meer mail bij zakelijke filters en beveiligingsscanners aankomt, en dat ongefilterde klikcijfers steeds meer opblazen.

## 1. Authenticatie (DNS, 7 oktober 2026)

| Record | Waarde | Oordeel |
|---|---|---|
| Afzender in Klaviyo | `send@siraatskitchen.com`, naam "SiraatsKitchen" | Let op: naam zonder spatie en apostrof; "Siraat's Kitchen" is herkenbaarder in de inbox |
| Return-path / verzenddomein | `send.siraatskitchen.com` CNAME naar `u161779.wl030.sendgrid.net` (Klaviyo-infrastructuur), SPF `v=spf1 include:sendgrid.net ~all`, MX `mx.sendgrid.net` | Goed. SPF-alignment relaxed (subdomein van het From-domein) |
| DKIM | `kl._domainkey` en `kl2._domainkey.siraatskitchen.com` CNAME naar Klaviyo/SendGrid, beide met een geldige RSA-sleutel | Goed, d= is het From-domein, dus DKIM-aligned |
| SPF hoofddomein | `v=spf1 a mx include:spf.mijndomeinhosting.nl ~all` | Alleen voor mail via mijndomein. Klaviyo hoeft hier niet in (eigen return-path) |
| DMARC | `_dmarc.siraatskitchen.com` CNAME naar `dmarc-none.mijndomein.nl`: `v=DMARC1; p=none; sp=none; pct=100; adkim=r; aspf=r; rua=mailto:dmarc@reportdmarc.nl` | **Zwak punt.** Voldoet aan het minimum van Gmail en Yahoo (een DMARC-record bestaat), maar `p=none` beschermt niet tegen spoofing, en de rapporten gaan naar de registrar, niet naar Siraat |
| BIMI | geen record op `default._bimi` | Pas zinvol na `p=quarantine` of `p=reject` |
| MX hoofddomein | `mx1/mx2.mijndomein.nl` | Inkomende mail via mijndomein |
| Shopify-, Gorgias- of Google-DKIM | Geen records gevonden op gangbare selectors (`shopify`, `gorgias`, `google`, `mailer`, `s1`) | Onbekend of Shopify-notificaties en Gorgias-antwoorden als `@siraatskitchen.com` uitgaan en DMARC halen. Uitzoeken vóór het DMARC-beleid strenger wordt |

**Aanbevolen volgorde (niet zelf uitgevoerd):**
1. Eigen DMARC-record in plaats van de CNAME naar mijndomein: `v=DMARC1; p=none; rua=mailto:<eigen adres of DMARC-dienst>; fo=1`. Twee tot vier weken rapporten lezen.
2. Alle bronnen die als `@siraatskitchen.com` mailen (Klaviyo, Shopify, Gorgias, eventueel Google Workspace of mijndomein-mailboxen) laten signeren met DKIM op het eigen domein.
3. Daarna `p=quarantine; pct=25`, oplopend naar 100, later `p=reject`. Pas dan BIMI overwegen (vraagt een VMC of CMC).
4. Google Postmaster Tools en Microsoft SNDS koppelen voor `siraatskitchen.com` en `send.siraatskitchen.com`. Zonder Postmaster is de Gmail-spamratio voor 56 procent van de mail onzichtbaar.

## 2. One-click unsubscribe

- Klaviyo zet automatisch `List-Unsubscribe` en `List-Unsubscribe-Post` (RFC 8058) op marketingmail. Het werkt aantoonbaar: in de Unsubscribed-events staat `ONE_CLICK_UNSUBSCRIBE` als methode naast `EMAIL_LINK` en `SPAM_REPORT` (zie verdeling in 01-cohorten, paragraaf 5).
- De headers zelf zijn niet via de API te lezen. Controle: een ontvangen campagne in Gmail openen, "Show original", zoeken naar `List-Unsubscribe-Post: List-Unsubscribe=One-Click`.
- Uitschrijving moet binnen 2 dagen verwerkt zijn (Gmail/Yahoo-eis); Klaviyo doet dat direct.

## 3. Spam, bounce en uitschrijving per week

Bron: metric aggregates (Received Email `YkRM4Q`, Bounced Email `XDdu6P`, Marked Email as Spam `VQMAAk`, Unsubscribed from Email Marketing `YcWddQ`, Dropped Email `RCULWK`, Clicked Email `W247h8` gesplitst op Bot Click), kalenderweken maandag tot en met zondag, US/Eastern. Ratio's per verzonden mail (Received), klikkers per unieke ontvanger.

| Week (ma) | Mails | Ontvangers | Mails per ontvanger | Bounce % (waarvan hard) | Spam % | Uitschrijf % | Menselijke klikkers % | Botklik-aandeel klikkers |
|---|---|---|---|---|---|---|---|---|
| 2026-04-06 | 207.137 | 81.349 | 2,5 | 0,24 (0,024) | 0,083 | 0,89 | 2,51 | 16% |
| 2026-04-13 | 210.126 | 75.638 | 2,8 | 0,15 (0,013) | 0,037 | 0,77 | 2,97 | 16% |
| 2026-04-20 | 163.149 | 76.446 | 2,1 | 0,15 (0,023) | 0,050 | 0,81 | 2,70 | 17% |
| 2026-04-27 | 242.262 | 82.457 | 2,9 | 0,16 (0,024) | 0,032 | 0,70 | 3,01 | 18% |
| 2026-05-04 | 255.108 | 79.732 | 3,2 | 0,18 (0,034) | 0,028 | 0,72 | 3,26 | 17% |
| 2026-05-11 | 230.160 | 89.353 | 2,6 | 0,28 (0,055) | 0,045 | 0,96 | 3,33 | 16% |
| 2026-05-18 | 307.603 | 89.959 | 3,4 | 0,15 (0,025) | 0,048 | 0,76 | 3,70 | 16% |
| 2026-05-25 | 308.405 | 92.221 | 3,3 | 0,19 (0,048) | 0,054 | 0,70 | 3,28 | 16% |
| 2026-06-01 | 284.778 | 101.521 | 2,8 | 0,24 (0,051) | 0,044 | 0,68 | 2,41 | 16% |
| 2026-06-08 | 203.528 | 91.910 | 2,2 | 0,19 (0,050) | 0,046 | 0,80 | 2,59 | 16% |
| 2026-06-15 | 353.331 | 112.492 | 3,1 | 0,18 (0,036) | 0,023 | 0,59 | 2,49 | 17% |
| 2026-06-22 | 265.050 | 111.454 | 2,4 | 0,20 (0,031) | 0,037 | 0,69 | 2,34 | 19% |
| 2026-06-29 | 282.136 | 107.648 | 2,6 | 0,65 (0,045) | 0,085 | 0,64 | 2,28 | 20% |
| 2026-07-06 | 233.378 | 97.732 | 2,4 | 0,26 (0,051) | 0,130 | 0,70 | 2,46 | 18% |
| 2026-07-13 | 172.925 | 69.469 | 2,5 | 0,22 (0,042) | 0,136 | 0,87 | 3,03 | 20% |
| 2026-07-20 | 357.274 | 84.560 | 4,2 | 0,12 (0,014) | 0,032 | 0,46 | 3,08 | 20% |
| 2026-07-27 | 307.124 | 112.487 | 2,7 | 0,12 (0,014) | 0,045 | 0,51 | 1,85 | 20% |
| 2026-08-03 | 312.266 | 110.200 | 2,8 | 0,19 (0,039) | 0,050 | 0,59 | 2,36 | 18% |
| 2026-08-10 | 296.639 | 117.547 | 2,5 | 0,23 (0,032) | 0,045 | 0,61 | 2,00 | 20% |
| 2026-08-17 | 255.977 | 112.005 | 2,3 | 0,21 (0,036) | 0,070 | 0,67 | 2,06 | 20% |
| 2026-08-24 | 153.363 | 59.908 | 2,6 | 0,33 (0,125) | 0,070 | 1,04 | 3,44 | 18% |
| 2026-08-31 | 343.372 | 150.497 | 2,3 | 0,22 (0,040) | 0,077 | 0,71 | 2,38 | 19% |
| 2026-09-07 | 429.644 | 148.858 | 2,9 | 0,17 (0,023) | 0,051 | 0,53 | 2,58 | 19% |
| 2026-09-14 | 426.109 | 151.952 | 2,8 | 0,16 (0,020) | 0,032 | 0,49 | 1,94 | 24% |
| 2026-09-21 | 340.693 | 143.010 | 2,4 | 0,19 (0,044) | 0,044 | 0,57 | 1,62 | 26% |
| 2026-09-28 | 739.922 | 166.861 | 4,4 | 0,16 (0,039) | 0,034 | 0,45 | 2,48 | 32% |

| Periode | Mails | Spam % | Uitschrijf % | Bounce % |
|---|---|---|---|---|
| april tot en met juni (13 weken) | 3,31 mln | 0,046 | 0,73 | 0,23 |
| juli tot en met september (13 weken) | 4,37 mln | 0,055 | 0,58 | 0,19 |
| laatste 4 weken | 1,94 mln | 0,039 | 0,50 | 0,17 |

**Lezing.**
- Per mail dalen spam en uitschrijving licht, maar dat komt doordat het volume harder groeit dan de klachten: het absolute aantal uitschrijvingen in de week van 28 september (3.340) is het hoogste van het halfjaar.
- Spampieken in de weken van 29 juni tot 13 juli (0,09 tot 0,14 procent) vallen samen met de flash-sale- en jubileumreeks naar "EB | US Subscribers".
- Bounces zijn gezond. De week van 24 augustus (hard 0,125 procent) is een uitschieter; de bounce-piek van 29 juni (0,65 procent) is soft (tijdelijk geweigerd), een typisch teken van throttling door een provider.
- Menselijke klikkers per ontvanger dalen van circa 3 procent (april tot mei) naar 1,6 tot 2,5 procent (september). Meer mail naar dezelfde mensen levert niet evenredig meer kliks op.

## 4. Spamklachten per mailbox-provider (Q3: juli tot en met september)

| Provider | Mails | Aandeel | Klachten | Ratio Q3 | Jul / aug / sep |
|---|---|---|---|---|---|
| Gmail | 2.196.702 | 56,2% | 1 | 0,000% (geen terugmelding) | n.v.t. |
| Yahoo / AOL (Verizon Media) | 747.326 | 19,1% | 795 | **0,106%** | 0,113 / 0,104 / 0,103 |
| Hotmail / Outlook.com | 488.929 | 12,5% | 1.495 | **0,306%** | 0,505 / 0,279 / 0,215 |
| Apple iCloud | 199.559 | 5,1% | 0 | geen terugmelding | n.v.t. |
| Office 365 (zakelijk) | 78.392 | 2,0% | 0 | geen terugmelding | n.v.t. |
| Gsuite (zakelijk) | 51.375 | 1,3% | 0 | geen terugmelding | n.v.t. |
| Comcast | 49.167 | 1,3% | 84 | 0,171% | 0,147 / 0,253 / 0,135 |
| Overig (top-9 restgroep) | 77.297 | 2,0% | 23 | 0,030% | |

Aandeel berekend binnen deze negen groepen (samen het overgrote deel van de verzendingen).

**Wat dit betekent.** De drie providers die klachten terugmelden komen samen op 0,18 procent. Er is geen reden om aan te nemen dat Gmail-gebruikers milder zijn; Gmail's eigen cijfer kan in dezelfde orde liggen. Microsoft handhaaft sinds mei 2025 dezelfde eisen als Gmail en Yahoo voor bulkverzenders; 0,3 tot 0,5 procent bij Outlook is een directe bedreiging voor inboxplaatsing daar. Microsoft-adressen krijgen relatief veel mail van de giveaway-lijst (Hotmail is 12,5 procent van de mail, maar 63 procent van alle teruggemelde klachten).

## 5. Wie krijgt er nog mail: frequentie en doelgroepen

**Volume per week, flows tegenover campagnes (laatste 6 volle weken):**

| Week (ma) | Campagnemails | Campagne-ontvangers | Campagnes per ontvanger | Welcome SiaNLu | Failure to launch T2SmtR |
|---|---|---|---|---|---|
| 2026-08-24 | 88.313 | 45.033 | 2,0 | 19.600 | 12.903 |
| 2026-08-31 | 274.047 | 143.413 | 1,9 | 21.783 | 13.646 |
| 2026-09-07 | 357.505 | 144.992 | 2,5 | 18.665 | 21.350 |
| 2026-09-14 | 358.960 | 144.945 | 2,5 | 15.490 | 25.629 |
| 2026-09-21 | 272.317 | 135.680 | 2,0 | 15.022 | 27.207 |
| 2026-09-28 | 675.483 | 164.681 | **4,1** | 14.469 | 23.757 |

Failure to launch is verdubbeld (13 naar 24 tot 27 duizend mails per week): de grote juli/augustus-instroom van de giveaway komt nu in de dag 30 tot 41-reeks, bovenop de campagnes.

**Doelgroepen van de 81 verstuurde campagnes sinds 9 juli** (aantal keer opgenomen):

| Doelgroep | Profielen | Keer opgenomen | Engagementfilter? |
|---|---|---|---|
| EB, US Subscribers (`VJkN42`) | 71.052 | 21 | Nee, alleen land en consent |
| EB [DG] Engaged 30 Days (`TNdhKc`) | 54.864 | 11 | Ja |
| Email List (`Uw8eZG`), volledig | 214.453 leden | 10, waarvan 8 sinds 5 september | Nee |
| Engaged 180 Days (`XHT3z5`) | 55.412 | 8 | Ja |
| Engaged 90 Days (`TMaWCL`) | 89.759 | 5 | Ja |
| HS, Email Only Subscribers (`X2p52X`) | 163.100 | 2 | Nee |

Vaste uitsluitingen (spam, bounce, unsubscribe, "For Suppression" `W4vNzF` met 5.371 profielen) staan bijna altijd aan. "Unengaged 180 Days, Non-Buyers" (`Ur6Ehr`, 20.060) werd maar 7 keer uitgesloten, het Sunset Segment (`XY4NVp`, 17.365) 2 keer.

Voorbeeld: "Sunday Recipe Day | 30 Days Engaged" (4 oktober) ging naar de volledige Email List (134.371 afgeleverd), met Smart Sending uit, ondanks de naam.

**Smart Sending.** 10 van de 33 campagnes sinds 1 september stonden met Smart Sending uit: 09/05 September is hard, 09/07 Labour Day Sale, 09/08 US Exclusion Sale Day, Roasting Pan shipping today, 09/05 resend to non-openers, Founder Note Sale (1 okt), Prime Sale US en INT (2 en 3 okt), 6-piece set (3 okt), Sunday Recipe Day (4 okt).

## 6. Aandeel nooit-betrokken profielen dat nog mail krijgt

Drie manieren van meten, van ruim naar streng:

| Meting | Uitkomst | Bron |
|---|---|---|
| Klaviyo-definitie "Engaged 90 Days" (sitebezoek, niet-machinale open of menselijke klik in 90 dagen) | 89.759 betrokken van circa 167.000 profielen die in de week van 28 september mail kregen: **circa 77.000 (46 procent) niet betrokken** | Segment `VKxqyA`, Received Email uniek per week |
| Menselijke klik (Bot Click = false) in de laatste 90 dagen | 22.888 unieke klikkers: **circa 86 procent van de ontvangers klikte 90 dagen niet** | Clicked Email-events 8 juli tot 6 oktober |
| Cohorten januari tot en met augustus, minstens 45 dagen oud: geen klik en geen order sinds aanmelding, niet uitgeschreven en geen spamklacht | **45,6 procent van alle aanmelders**, 55,4 procent van de Alia-aanmelders, oplopend van 49 procent (april) naar 60,1 procent (augustus) | Zie 01-cohorten en `cohorten.csv` |

**Waar de klachten vandaan komen (1 juli tot 6 oktober):**

| | Spamklachten | Uitschrijvingen |
|---|---|---|
| Totaal (events) | 2.646 | 27.369 |
| Van profielen zonder menselijke klik in de 90 dagen ervoor | **81,8%** | 75,0% |
| Idem, ook zonder order | 74,9% | 67,5% |
| Van aanmelders jonger dan 30 dagen | 29,7% | 38,2% |
| Van aanmelders jonger dan 60 dagen | **50,6%** | 54,0% |
| Uit campagnes / uit flows | 59% / 41% | 61% / 39% |

Methode van uitschrijven (1 juli tot 6 oktober): one-click 13.230 (48 procent), link in de mail 12.979 (47 procent), via spamklacht 1.119 (4 procent).

Conclusie: de klachten komen bijna volledig van mensen die niet klikken, en de helft van nieuwe aanmelders in hun eerste twee maanden. Precies die groep krijgt sinds september de meeste extra campagnes. Kanttekening: bounce-onderdrukking is in de cohortmeting niet afgetrokken (het effect is klein, hard bounce 0,04 procent per week), en opens tellen bewust niet mee (Apple Mail Privacy).

## 7. Wat de API niet laat zien

- Klaviyo's Deliverability Hub (inbox-plaatsing, domeinreputatie) heeft geen publieke API-endpoint; alleen de metrics hierboven zijn uit te lezen.
- Gmail-spamratio, domein- en IP-reputatie: alleen Google Postmaster Tools. Microsoft: SNDS.
- Alia (pop-up): geen leestoegang in deze sessie. Wat Alia met dubbele of wegwerpadressen doet, is onbekend.
