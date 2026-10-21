# Social Snowball · flowstructuur affiliate-levenscyclus (21 okt 2026)

Opdracht Floris: bijna elke tevreden klant wordt affiliate, zonder dat uitschrijvingen, bounces of spamklachten stijgen. Dit stuk legt de complete levenscyclus vast als Klaviyo-flows, met triggers, filters, timing, een frequentiebudget, risico's, invoegpunten in de bestaande flows en verwachte aantallen. Alles is ontwerp: **niets in Klaviyo, Shopify of Social Snowball is aangemaakt of gewijzigd.** Alleen gelezen (GET en één read-only flow-values-rapport). Geen klantdata in dit bestand, alleen aantallen.

Bronnen: README, PLAYBOOK, DECISIONS, LOG (laatste 40 regels), `klaviyo/flows/v4-flow-system.md`, `research/flows-audit/2026-10-19-*.md`, `research/review/02-catchup-20okt.md`, `research/referral/01-ontwerp.md` (eerder referral-ontwerp zonder app, route A), live flowdefinities X3ySuU, VQ93sx, XzHrez, TvfJYU, VPixnJ, VTkxFL, UyFc78, Klaviyo-metrics en -events van 20 en 21 okt.

---

## 0. Wat de live data zegt (en waarom het ontwerp daardoor anders is dan gedacht)

| Feit (gemeten 21 okt, read-only) | Gevolg voor het ontwerp |
| --- | --- |
| Social Snowball stuurt 17 metrics naar Klaviyo (lijst in 1.1). Op 20 en 21 okt fired elke metric precies 1 keer, allemaal op **hetzelfde profiel**: dat is de koppelingstest, geen echte activiteit. | Trigger-ID's zijn echt en bruikbaar. Echte volumes voor sale, payout en aanmelding zijn nog 0. |
| **"Enrolled in SocialSnowball through purchase" (XzrVJZ)**: 438 events op 437 profielen (142 op 20 okt vanaf 14:40 UTC, 296 op 21 okt). Dat zijn de "~438 affiliates". | **Elke koper wordt automatisch affiliate**, ongeveer 17 tot 22 minuten na Placed Order (steekproef 14 profielen). "Werven" van nieuwe kopers is dus niet nodig: het gaat om **activeren** (laten weten dat er een link is en laten delen). |
| Een derde van een steekproef van 40 ingeschreven profielen had de laatste order meer dan 48 uur eerder; 1 had geen order in Klaviyo. | Snowball schrijft ook recente oudere orders in (vermoedelijk achterstand of fulfilment). Bestaande klanten van vóór 20 okt (98.538 kopers sinds okt 2024) zijn **niet** ingeschreven: daar zit de echte werving. |
| Profieleigenschappen (steekproef 120): `Social Snowball - Affiliate Status` = Active (120/120), `Program - Social Snowball` = Default program, `Referral Code Type - SocialSnowball` = tracking link, `Referral Friend Offer - SocialSnowball` = **10%**, `Referral Reward - SocialSnowball` = **20%**, `Referral Currency` = $, `Referral Link - SocialSnowball` gevuld, welcome gift status None. | Mails kunnen de link en het aanbod per profiel tonen. De programmavoorwaarden komen uit Snowball, niet uit de template typen. Vriendenaanbod 10% is gelijk aan HI10: zwak verschil (zie besluit B2). |
| Marketingtoestemming in dezelfde steekproef: 111 SUBSCRIBED, 6 NEVER_SUBSCRIBED, 3 UNSUBSCRIBED. Landen: ~80% US, verder AU, SG, CA, UK, HK. | Alle Klaviyo-mails in dit plan zijn marketing en gaan alleen naar wie mag. Snowball's eigen systeemmails (als die aan staan) bereiken de rest. |
| Event-properties zijn mager: New referral sale (Xqbr4d) heeft `$value` en `Social Snowball - Conversion ID`; Payout sent (WManrA) alleen Conversion ID; Instagram-events een `Link`. Op het testprofiel staan ook `Social Snowball: Affiliate Order Value` en `Social Snowball: Payout amount` als profieleigenschap. | Bedragen in sale- en payoutmails komen uit `event.$value` (orderwaarde) en de profieleigenschap Payout amount. Commissie = 20% van de orderwaarde, maar alleen tonen als bevestigd is wat Snowball als basis neemt (na korting, zonder verzending). |
| Gorgias Opened Ticket (YzvjGf) heeft `tags`. Laatste 800 tickets: feedback 304, negative 214, return/exchange 203, order-status 183, positive 90, product 64, order-change/cancel 46, quality_issue 10, manufacturing defects 7, complaint 3, chargeback 2, disputifier 12. | "Schade of defect" is in Klaviyo te filteren op ticket-tags, zonder extra koppeling. |
| Flowcijfers laatste 30 dagen (flow-values-rapport, conversie Placed Order): P1-FIRST (bericht R3gbkQ, waarschijnlijk) 2.133 ontvangers, klik 8,0%, uitschrijf 0,24%, spam 0,047%, bounce 0,52%; P1-REPEAT (WqxPSh) 306, klik 4,6%, uitschrijf 0%; P2 (VQ93sx, RCgdNW) 954, klik 4,9%, uitschrijf 0,53%; U1 (VPixnJ, RBrHK9) 573, klik 1,4%, uitschrijf 0,18%, $0; review XzHrez 32, klik 9,4%. P2-SAFE en P3 hebben nog geen volume (eerste mails eind oktober). | Kopers-flows zijn schoon (uitschrijf 0,2 tot 0,5%). Campagnes zijn het probleem (~360 uitschrijvingen per dag op 45k tot 135k ontvangers, bijna dagelijks). Het plan voegt dus **geen campagnes** toe en ruilt elke extra flowmail tegen een campagne. |

Flowmail-ID's van P1-FIRST en P1-REPEAT zijn afgeleid uit het volume (de API gaf geen naam terug); bij de bouw één keer in de UI bevestigen.

---

## 1. Bouwstenen

### 1.1 Social Snowball-metrics in Klaviyo (account TdtTzz)

| Metric | ID | Gebruik in dit plan |
| --- | --- | --- |
| Enrolled in SocialSnowball through purchase | **XzrVJZ** | Trigger S1 (activatie kopers) en S0 (pilotlabel) |
| Social Snowball - Signed up as an affiliate via Shopify customers import | **WjpQvK** | Trigger S2 (werving bestaande klanten na import) |
| Social Snowball - Signed up as an affiliate via sign up form | **SJy5uM** | Trigger S3 (aanmelders, als auto-approve aan staat) |
| Social Snowball - Signed up as an affiliate via marketplace | TTWUnD | S3 (creators via de Snowball-marktplaats) |
| Social Snowball - Signed up as an affiliate via manual creation / manual upload | VGnMT8 / TYAaJ3 | S3 alleen als Floris handmatig creators toevoegt |
| Social Snowball - Pending affiliate application | R2KsjG | S3a ontvangstbevestiging (alleen als Snowball die niet zelf stuurt) |
| Social Snowball - Approved affiliate application | **WWqT8n** | Trigger S3 bij handmatige goedkeuring |
| Social Snowball - Rejected affiliate application | UBBdkE | Geen mail; uitsluiten van S1 tot en met S6 |
| Social Snowball - New referral sale | **Xqbr4d** | Trigger S5 (verkoopmelding, mijlpalen); stopfilter in S1 tot en met S4 |
| Social Snowball - Payout sent | **WManrA** | Trigger S5b (uitbetaling) |
| Social Snowball - Welcome Gift Claimed | TciBqC | Stopfilter S4 (als de welcome gift aangezet wordt) |
| Social Snowball - Affiliate changed program | UYJuV7 | Trigger mijlpaalmail bij tier-upgrade (fase 2) |
| Social Snowball - Discount code changed | TPjE3f | Geen mail |
| Social Snowball - New Instagram Post / Story / Reel added by affiliate | V5mKgv / VBKxxJ / Y3ctEQ | Trigger S5c (bedankt voor je post), koppelt aan UGC |

### 1.2 Overige metrics

Placed Order RSNxYV, Fulfilled Order VtEiZT, Delivered Shipment VcUF33, Postflows 4. Shipment Delivered UabgWz (alleen als bewijs in een filter, nooit als trigger: vuurt 2,5 keer per zending), Refunded Order Xg6cwn, Cancelled Order TFervq, Opened Ticket (Gorgias) YzvjGf, Resolved Ticket SzcCyb, Received Email YkRM4Q, Clicked Email W247h8 (`URL`, `$flow`, `Bot Click`), Active on Site UdCdLD.

### 1.3 Profieleigenschappen (Snowball vult ze; letterlijke sleutels)

`Referral Link - SocialSnowball`, `Referral Code - SocialSnowball`, `Referral Friend Offer - SocialSnowball`, `Referral Reward - SocialSnowball`, `Referral Currency - SocialSnowball`, `Social Snowball - Affiliate Status`, `Program - Social Snowball`, `Social Snowball: Payout amount`, `Social Snowball: Affiliate Order Value`, `Gift card code - Social Snowball`.

In templates altijd via lookup, met terugval als de waarde leeg is (geen kapotte mail):
`{% with link=person|lookup:'Referral Link - SocialSnowball' %}{% if link %}...{{ link }}...{% endif %}{% endwith %}`
Het aanbod in de copy komt uit `person|lookup:'Referral Friend Offer - SocialSnowball'` en `person|lookup:'Referral Reward - SocialSnowball'` (nu 10% en 20%), zodat een programmawijziging de mails niet laat liegen. QA: qa_render.py met een sample-profiel met en zonder deze eigenschappen.

Eigen eigenschappen (gezet door flow-acties "Update profile property"):

| Eigenschap | Waarden | Gezet door |
| --- | --- | --- |
| `snow_pilot` | `in` / `uit` / `holdout` | S0, bij inschrijving |
| `snow_invite_at` | datum | S1, S2 (laatste wervings- of activatiemail) |
| `snow_stage` | `invited`, `clicked`, `active`, `dormant` | S1 tot en met S6 (voor segmenten en rapport) |

### 1.4 Gedeelde filtersets (exact, in Klaviyo-taal)

**F-KLANT (elke Snowball-mail aan klanten, als verzendfilter op het moment van versturen):**
1. Can receive email marketing.
2. Refunded Order (Xg6cwn) zero times in the last 60 days.
3. Cancelled Order (TFervq) zero times in the last 60 days.
4. Opened Ticket (YzvjGf) zero times in the last 21 days (benadering van "geen open ticket": Klaviyo kent de ticketstatus niet; 21 dagen dekt de mediane doorlooptijd plus marge). Alternatief bij de bouw: Opened Ticket zero times since starting this flow, plus de 21-dagenregel.
5. **Schade of defect, ooit:** Opened Ticket (YzvjGf) where `tags` contains any of `quality_issue`, `manufacturing defects`, `complaint`, `chargeback`, `disputifier`, `return/exchange` zero times over all time. (`negative` niet ooit, wel in de laatste 90 dagen: Opened Ticket where `tags` contains `negative` zero times in the last 90 days.) Tags worden soms pas later gezet; daarom staat regel 4 er ook.
6. **Lage review:** Clicked Email (W247h8) where `URL` contains `your-experience` zero times in the last 180 days (de 1 tot 3 sterren-route van XzHrez, TvfJYU en de catch-up-campagnes).
7. Social Snowball - Rejected affiliate application (UBBdkE) zero times over all time.
8. E-mail bevat niet `storebotmail.joonix.net` (zoals QUBUQV).
9. Placed Order (RSNxYV) zero times in the last 2 days (net weer gekocht: P1 heeft voorrang).
10. Received Email (YkRM4Q) where Flow equals X3ySuU, VQ93sx, VPixnJ, XzHrez of TvfJYU zero times in the last 2 days (nooit twee Siraat-flowmails binnen 48 uur).

**F-WERVING (extra bij elke wervings- of activatiemail):**
11. Received Email where Message Name starts with `SNOW · INVITE` zero times in the last 30 days (de vraag uit de opdracht), en in S1/S2 strenger: zero times in the last 365 days (één echte uitnodiging per jaar).
12. New referral sale (Xqbr4d) zero times over all time (wie al verdient, krijgt geen uitleg meer).
13. Engaged in de laatste 90 dagen (alleen S2, bestaande klanten; kopers in S1 zijn per definitie betrokken): Clicked Email where Bot Click is false at least once in the last 90 days OR Active on Site (UdCdLD) at least once in the last 90 days OR Placed Order at least once in the last 90 days. Opens tellen niet (Apple MPP).
14. "Nog geen affiliate" (alleen bij werving van bestaande klanten vóór de import): `Social Snowball - Affiliate Status` is not set. Bij kopers vanaf 20 okt is iedereen al affiliate; daar vervangt regel 12 deze regel.

**F-BEZORGD (S1):** Delivered Shipment (VcUF33) at least once in the last 45 days OR Postflows 4. Shipment Delivered (UabgWz) at least once in the last 45 days. In de catch-up van 20 okt had ~90% van de gefulfilde orders een van beide (Postflows draagt ~60%); zonder bewijs geen activatiemail.

**Berichtnamen:** elke wervings- en activatiemail krijgt een naam die begint met `SNOW · INVITE` (S1-A1, S1-A2, S2-W1, S4-REV), elke overige Snowball-mail `SNOW ·`. Zo werken regel 11 en de campagne-uitsluiting zonder extra segmenten (zelfde truc als `CODE ·` in v4 1.4).

---

## 2. De levenscyclus als flows

Overzicht. "Nieuw" = nieuwe flow. "Blok" = alleen een blok in een bestaande mail, geen extra mail.

| # | Flow (naam in Klaviyo) | Doel | Trigger | Mails | Extra mails per klant |
| --- | --- | --- | --- | --- | --- |
| S0 | v4 · Snowball · pilotlabel (nieuw, geen mails) | 20%-pilot en holdout | XzrVJZ | 0 | 0 |
| B | Blokken "Earn with Siraat" in P1-REPEAT, P2, P2-SAFE, U1, V2 | Bewustzijn op het moment van tevredenheid | bestaande flows | 0 | 0 |
| S1 | v4 · Snowball · activatie kopers (nieuw) | Klant weet dat hij een link heeft en deelt | XzrVJZ | A1, A2 (A2 alleen klikkers) | 1, gecompenseerd (sectie 3) |
| S4 | v4 · Snowball · na review (nieuw) | Bedankje plus link na 4 of 5 sterren | Clicked Email (Trustpilot-link) | REV1 | 0 netto (vervangt A1) |
| S2 | v4 · Snowball · werving bestaande klanten (nieuw) | Klanten van vóór 20 okt worden affiliate | WjpQvK (na import in golven) | W1, W2 (W2 alleen klikkers) | 1, gecompenseerd |
| S3 | v4 · Snowball · welkom aanmelders (nieuw) | Aanmelding, goedkeuring, welkom, deelkit, 3 duwtjes | WWqT8n / SJy5uM / TTWUnD | AF0 tot en met AF3 | alleen wie zelf aanmeldt |
| S5 | v4 · Snowball · verkoop en uitbetaling (nieuw) | Eerste sale vieren, mijlpalen, uitbetaling | Xqbr4d, WManrA, V5mKgv/VBKxxJ/Y3ctEQ | SALE1, SALE-M3, SALE-M10, PAY1, POST1 | alleen bij succes |
| S6 | v4 · Snowball · slapend (nieuw) | Affiliate met eerdere sale weer laten delen | Segment "Snowball · slapend 60d" | D1 | max 1 per 120 dagen |
| S7 | Campagneblok en BFCM | Delen in de sterkste week van het jaar | campagnes | 0 extra (blok), 1 vervangende affiliate-mail | 0 netto |

### 2.0 S0 · pilotlabel (hulpflow, geen mails)

- Trigger XzrVJZ. Flowfilter: has not been in this flow over all time.
- Stap 1: Conditional split, Random sample (profile-sample) 20% → Update profile property `snow_pilot = in`. Anders: split 11% van de rest (≈ 10% van totaal) → `snow_pilot = holdout`, overige → `snow_pilot = uit`.
- Na 7 dagen pilot: split naar 90% `in`, 10% `holdout` (sectie 5.4). De holdout blijft affiliate (Snowball schrijft iedereen in) maar krijgt geen Klaviyo-blokken of -mails: zo meten we wat de mails toevoegen bovenop "iedereen heeft een link".
- Waarom een label in plaats van een split per flow: de API kan geen splits toevoegen aan live flows, en de blokken in P1-REPEAT, P2, P2-SAFE en U1 kunnen in de template zelf op `person|lookup:'snow_pilot' == 'in'` controleren. Eén label stuurt alles.
- Timing klopt: inschrijving 17 tot 22 minuten na Placed Order, P1 gaat na 1 uur, dus het label staat er bij P1.

### 2.1 Blokken "Earn with Siraat" in bestaande mails (geen extra mails)

Nieuw blok `{{BLOCK:earn}}` in `klaviyo/templates/partials/blocks/earn.html` (vaste opbouw, kalm register): eyebrow "SHARE SIRAAT", één regel kop als PNG (TT Ramillas), twee zinnen, de persoonlijke link als knop ("Copy my link" via `{{BLOCK:cta}}`), één regel friction ("Your friends get {{offer}} off their first order. You earn {{reward}} of what they spend."). Toont alleen als `snow_pilot == 'in'` en de link gevuld is. Geen beelden boven 120 KB, past binnen de lengtenorm van PLAYBOOK 12. Exacte invoegplek en actie-ID's in sectie 4.

### 2.2 S1 · activatie kopers (de "werving" van nieuwe kopers)

- **Trigger**: Enrolled in SocialSnowball through purchase (**XzrVJZ**).
- **Flowfilters**: has not been in this flow in the last 365 days · `snow_pilot` equals `in` · e-mail niet storebot.
- **Herinstap**: 365 dagen (herhaalkopers krijgen hem niet bij elke order).
- Waarom niet Delivered Shipment als trigger: vuurt maar bij ~40%. XzrVJZ dekt elke koper; bezorging wordt in de verzendfilter gecontroleerd (F-BEZORGD).

| Stap | Wachttijd | Reden | Split / voorwaarde | Mail | Verzendfilter | Smart sending |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 31 dagen, tot 09:00 | Na de eerste kookweken en na de reviewvraag (P2 dag 13, U1 dag 16, P3 dag 20, review dag 26 of fallback dag 24), vóór winback R1 (dag 45). Vrij gat in de kalender (sectie 3.1). | CS: Received Email where Message Name starts with `SNOW · INVITE` at least once in the last 365 days → JA einde (REV1 ging al) | **A1** `SNOW · INVITE · A1` "Who do you cook for?" Benjamin-stem, link, drie kant-en-klare deelteksten (sms, WhatsApp, Instagram-story), "How it works" in drie regels | F-KLANT 1 tot 10, F-WERVING 11 en 12, F-BEZORGD | **Aan** (16 uur) |
| 1b | direct | | Update profile property `snow_invite_at` = vandaag, `snow_stage` = invited | | | |
| 2 | 6 dagen, tot 09:00 (dag 37) | Alleen wie interesse toonde. 8 dagen vóór R1. | CS: Clicked Email where Message Name starts with `SNOW · INVITE · A1` at least once since starting this flow AND New referral sale (Xqbr4d) zero times since starting this flow. NEE → einde | **A2** `SNOW · INVITE · A2` "Three ways people share it" (deelideeën, één echte Trustpilot-review over doorgeven) | F-KLANT, Xqbr4d zero since start | Aan |
| einde | | Geen derde mail. Wie niet klikt, hoort alleen nog het blok in campagnes (S7) en V2. | | | | |

Aantal mails: 1 voor iedereen, 2 voor klikkers (verwacht 5 tot 8%).

### 2.3 S4 · na review (bedankje plus link)

- **Trigger**: Clicked Email (**W247h8**). **Triggerfilter**: `URL` contains `trustpilot.com/evaluate` AND `Bot Click` is false.
- **Flowfilters**: has not been in this flow over all time · `snow_pilot` equals `in`.
- Bron van de klik: XzHrez (5 en 4 sterren gaan beide naar Trustpilot, PLAYBOOK 5), TvfJYU en de catch-up-campagnes. 4 en 5 sterren zijn niet te scheiden; allebei tevreden genoeg.

| Stap | Wachttijd | Mail | Verzendfilter | Smart sending |
| --- | --- | --- | --- | --- |
| 1 | 1 dag, tot 09:00 | **REV1** `SNOW · INVITE · REV` "Thank you. One more thing you can do." Bedankt voor de review, link, deelteksten. Geen beloning gekoppeld aan de review zelf (Trustpilot-regels). | F-KLANT, F-WERVING 11 en 12 | Aan |

REV1 telt als de uitnodiging: A1 slaat daarna over (stap 1 van S1). Netto 0 extra mails voor reviewers.

**Er bestaat nu geen review-bedankmail**: de klik gaat direct naar Trustpilot. REV1 is dus tegelijk de bedankmail.

### 2.4 S2 · werving bestaande klanten (98.538 kopers van vóór 20 okt)

Bestaande klanten zijn niet automatisch affiliate. Twee routes:

| | **Route I · import (advies)** | Route II · uitnodiging met aanmeldformulier |
| --- | --- | --- |
| Hoe | Floris importeert in Snowball een gefilterde Shopify-klantenlijst (sign-up via Shopify customers import, metric WjpQvK bestaat al). Klaviyo stuurt daarna de uitleg met hun link. | Campagne of flow met een link naar het Snowball-aanmeldformulier; klant meldt zich zelf aan (SJy5uM). |
| Frictie | Geen: de link staat al in de mail | Formulier, account, wachten op goedkeuring |
| Bereik | Bijna iedereen in de golf heeft een link | 2 tot 5% van ontvangers meldt zich aan (aanname) |
| Risico | Snowball-systeemmails naar de hele golf (controleren, besluit B1) | Extra campagne, meer uitschrijvingen |

**Import in golven** (de lijst wordt in Klaviyo gebouwd als segment, Floris exporteert en importeert):

Segment "Snowball · wervingspool" = Placed Order at least once over all time AND Placed Order zero times in the last 30 days AND F-KLANT 1 tot 8 AND F-WERVING 13 (betrokken 90 dagen) AND 14 (nog geen affiliate) AND Placed Order where `Items` bevat kookgerei of set at least once (HEEFT_KOOKGEREI). Golven per 5.000 profielen, beste eerst: 2+ orders, dan eerste order 45 tot 365 dagen geleden met klik in 30 dagen, dan de rest.

- **Trigger S2**: WjpQvK (Signed up via Shopify customers import). **Flowfilters**: has not been in this flow over all time; Received Email where Message Name starts with `SNOW · INVITE` zero times in the last 365 days.

| Stap | Wachttijd | Mail | Verzendfilter | Smart sending |
| --- | --- | --- | --- | --- |
| 1 | tot de eerstvolgende dag 09:00 | **W1** `SNOW · INVITE · W1` "You already have a Siraat link" (Benjamin: je kookt er al mee, je vrienden krijgen {{offer}}, jij {{reward}}) | F-KLANT, F-WERVING 11 tot 13 | Aan |
| 2 | 7 dagen, tot 09:00 | **W2** alleen voor W1-klikkers zonder sale (zelfde split als S1 stap 2) | F-KLANT, Xqbr4d zero since start | Aan |

Golfgrootte begrenst de dagbelasting: 5.000 per golf, gespreid over 5 werkdagen (1.000 per dag) door de import per dag te doen. Volgende golf pas na de 7-dagencontrole (sectie 5).

### 2.5 S3 · aanmelding, goedkeuring, welkom en deelkit (wie zelf aanmeldt)

Voor creators en klanten die zich zelf via het formulier of de marktplaats aanmelden. Niet voor kopers die via S1 lopen (die krijgen geen aparte welkomstmail: A1 is hun welkom).

- **S3a ontvangst** (alleen als Snowball zelf geen bevestiging stuurt): trigger Pending affiliate application (R2KsjG), direct, 1 mail AF0 "We got your application". Transactioneel van aard; als marketing alleen naar wie mag.
- **S3 welkom**: trigger Approved affiliate application (**WWqT8n**). Staat goedkeuring automatisch aan, dan een tweede kopie van deze flow met trigger Signed up via sign up form (SJy5uM) en een derde voor marktplaats (TTWUnD); flowfilter "not in flow v4 · Snowball · welkom aanmelders in the last 365 days" voorkomt dubbel. Flowfilter: XzrVJZ zero times in the last 30 days (net gekocht: S1 regelt het).

| Stap | Wachttijd | Mail | Inhoud | Verzendfilter | Smart sending |
| --- | --- | --- | --- | --- | --- |
| 1 | direct | **AF1 welkom + deelkit** `SNOW · AF1` | Link en code, voorwaarden uit de profieleigenschappen, deelkit: 3 kant-en-klare posts (tekst plus beeld), 6 beelden in flash-stijl (bestaande shootfoto's, geen nieuwe claims), 2 korte video-snippets uit de chef-video (met ondertitels), "wat je wel en niet mag zeggen" (alleen goedgekeurde claims: "pure titanium cooking surface", "no coatings", "No PFAS, PFOA, or BPA", 30-day returns, 75-year warranty; geen gezondheidsclaims) | Can receive email marketing | **Uit** (ze vroegen erom) |
| 2 | 3 dagen, tot 09:00 | **AF2 dag 3** `SNOW · NUDGE · 1` | "Your first share, in 60 seconds": één post om te kopiëren, story-sjabloon | Xqbr4d zero since start | Aan |
| 3 | 7 dagen, tot 09:00 (dag 10) | **AF3 dag 10** `SNOW · NUDGE · 2` | Recept plus deeltekst ("the egg test"), wat werkt bij anderen | Xqbr4d zero since start; Opened Email or Clicked Email where Message Name starts with `SNOW ·` at least once since start | Aan |
| 4 | 11 dagen, tot 09:00 (dag 21) | **AF4 dag 21** `SNOW · NUDGE · 3` | Kort, Benjamin: "Was this not for you? No problem." plus een link naar voorkeuren voor alleen affiliate-mails | Xqbr4d zero since start; Clicked Email where Message Name starts with `SNOW ·` at least once since start (wie nooit klikte krijgt AF4 niet: geen derde mail in het luchtledige) | Aan |

Noot AF2: geen klikvoorwaarde, het is de eerste duw. AF3 alleen als ze minstens één Siraat-mail openden of klikten sinds de start (open telt hier wel, omdat het geen verkoopbeslissing is maar een leven-teken; Apple MPP maakt het ruim, dat is acceptabel). Na een sale stopt de reeks (Xqbr4d).

**Kopers in S1 krijgen niet de drie duwtjes van dag 3, 10, 21.** Dat zou 3 mails per koper toevoegen. Hun "duwtje" is A2 (alleen klikkers) en het blok in V2 en campagnes. Als S1 laat zien dat klikkers converteren, kan A2 later uitgebreid worden naar een tweede duw op dag 51 voor A1-klikkers (na R1), nooit voor niet-klikkers.

### 2.6 S5 · verkoopmelding, mijlpalen en uitbetaling

Deze mails zijn goed nieuws en verlagen eerder uitschrijvingen. Toch begrensd.

**S5a Sale**: trigger New referral sale (**Xqbr4d**). Flowfilter: has not been in this flow in the last 3 days (max 1 verkoopmail per 3 dagen; Snowball's eigen notificatie per sale blijft het realtime kanaal).

| Stap | Wachttijd | Split | Mail | Smart sending |
| --- | --- | --- | --- | --- |
| 1 | 15 minuten | CS: Xqbr4d equals 1 over all time | **SALE1** `SNOW · SALE · 1` "Your first friend just ordered" (bedrag uit `event.$value` x reward, alleen als B3 bevestigt hoe Snowball rekent; anders zonder bedrag) plus "Who's next?" met link | Uit |
| 1 | | CS: Xqbr4d equals 3 over all time | **SALE-M3** "Three friends in" (mijlpaal, eventueel tier-upgrade fase 2) | Uit |
| 1 | | CS: Xqbr4d equals 10 over all time | **SALE-M10** "Ten kitchens" (Benjamin, persoonlijk, eventueel product als dank: deksel of schort) | Uit |
| 1 | | anders | geen mail (Snowball's eigen melding volstaat) | |
| 2 | direct | | Update profile property `snow_stage` = active | |

**S5b Payout**: trigger Payout sent (**WManrA**). Flowfilter: not in this flow in the last 14 days. 1 mail **PAY1** `SNOW · PAY` direct: "You've been paid" (bedrag uit `Social Snowball: Payout amount`), plus een nieuwe deeltekst voor de huidige actie. Eerste uitbetaling krijgt de feestversie (CS: WManrA equals 1 over all time), latere een korte versie.

**S5c Post**: trigger New Instagram Post / Story / Reel (V5mKgv / VBKxxJ / Y3ctEQ), drie korte flows of één met de Post-trigger en de andere als fase 2. Flowfilter: not in this flow in the last 30 days. 1 mail **POST1** "We saw your post" met verwijzing naar de UGC15-ruil uit U1 (15% via Gorgias-macro na een foto, bestaand mechanisme). Smart sending aan.

**Mijlpaal via programma's (fase 2, besluit Floris):** een tweede Snowball-programma "Ambassador" (bijv. 25% na 5 sales). Affiliate changed program (UYJuV7) triggert dan een upgrademail.

### 2.7 S6 · slapende affiliates heractiveren

- **Trigger**: segment "Snowball · slapend 60d" = Xqbr4d at least once over all time AND Xqbr4d zero times in the last 60 days AND F-WERVING 13 (betrokken 90 dagen) AND can receive email marketing.
- **Flowfilters**: has not been in this flow in the last 120 days.
- 1 mail **D1** `SNOW · DORMANT` op de eerstvolgende dag 09:00: wat er nieuw is (actie, nieuw product), één kant-en-klare post, link. Verzendfilter F-KLANT; campagne-uitsluiting die dag. Smart sending aan.
- Daarna niets. Slapend zonder sale ooit (kopers die nooit deelden) krijgen **geen** heractivatie: dat is de groep met het hoogste uitschrijfrisico.

### 2.8 S7 · campagnemomenten (BFCM en daarna)

Geen extra campagnes. Twee vormen:

1. **Blok in bestaande campagnes** (alle campagnes vanaf de 20%-pilotfase, alleen voor wie een link heeft): `{% if person|lookup:'Referral Link - SocialSnowball' and person|lookup:'snow_pilot' != 'holdout' %}` een strook onder de laatste knop: "Share the sale: your friends get the 70% off plus {{offer}} with your link. You earn {{reward}}." De "plus {{offer}}" alleen als B2 bevestigt dat de Snowball-korting stapelt op de sale (anders: "Your friends get the 70% off. You earn {{reward}} of what they spend.").
2. **Eén vervangende affiliate-mail in BFCM**: segment "Snowball · actief of geïnteresseerd" = Xqbr4d at least once OR Clicked Email where Message Name starts with `SNOW ·` in the last 60 days OR S3-aanmelders. Op de BFCM-dag waarop zij **geen** gewone campagne krijgen (uitsluiten van die campagne): "Your link is worth the most this week". Black Friday 2026 is 27 november; voorstel donderdag 26 november (Thanksgiving, deelmoment) of maandag 30 november (Cyber Monday). Datum pas als Floris de BFCM-kalender vastzet (DECISIONS 7 okt).

---

## 3. Frequentiebudget: totaal mails per klant mag niet stijgen

### 3.1 Kalender van een gemiddelde US-koper (mediaan levering dag 12)

| Dag | Nu | Met Snowball |
| --- | --- | --- |
| 0 | P1-FIRST of P1-REPEAT | zelfde mail; P1-REPEAT met blok, P1-FIRST alleen P.S.-regel |
| ~3 | Shopify-verzendmail (niet Klaviyo) | zelfde |
| 13 (16) | P2 (VQ93sx, 40%) of P2-SAFE (dag 16) | zelfde mail, met blok |
| 16 | U1 (VPixnJ, alleen met Delivered Shipment) | zelfde mail, omgebouwd tot "share your first egg" (UGC + link) |
| 20 | P3 (codemail, T02) | zelfde, **geen blok** (één doel per verkoopmail) |
| 24 / 26 | Review fallback / review | zelfde, **geen blok** (reviewklik niet verdunnen) |
| 27 | | REV1 voor reviewklikkers (vervangt A1) |
| 31 | | **A1** (wie geen REV1 kreeg), ruilt tegen een campagne |
| 37 | | A2 (alleen A1-klikkers, ~5 tot 8%), ruilt tegen een campagne |
| 45 | Winback R1 | zelfde |
| 50 | VIP V1 (alleen 2e order) | zelfde; V2 (dag 60) met P.S. |
| doorlopend | campagnes, bijna dagelijks | zelfde, met blok; 1 minder op de A1-dag |

### 3.2 Regels die het budget afdwingen

1. **Ruil tegen campagne.** Segment "Snowball · campagnepauze" = Received Email where Message Name starts with `SNOW · INVITE` or `SNOW · DORMANT` or `SNOW · NUDGE` at least once in the last 1 day. Uitsluiten bij **elke** campagne (naast "v4 · Campagne-cap" en "v4 · Welcome-bescherming"). Wie A1, A2, REV1, W1, W2, D1 of een duwtje krijgt, slaat die dag de campagne over. Netto 0.
2. **Tellen in de campagne-cap.** Het segment "v4 · Campagne-cap" (max 3 campagnes per 7 dagen) telt nu alleen campagnes. Voorstel: ook `SNOW · INVITE` en `SNOW · DORMANT` meetellen, zodat een week met A1 maximaal 2 campagnes heeft. (Zelfde UI-stap als de cap zelf; de API weigerde dat segment eerder.)
3. **Geen twee Siraat-mails binnen 48 uur uit flows** (F-KLANT 10). A1 op dag 31 en A2 op dag 37 liggen ver van P3 (20), review (24/26) en R1 (45).
4. **Eén uitnodiging per 365 dagen** (`SNOW · INVITE`), en nooit binnen 30 dagen na een eerdere (opdrachtregel).
5. **Verkoop- en uitbetalingsmails** alleen bij succes, max 1 per 3 dagen (sale) en 14 dagen (payout). Geen campagne-uitsluiting nodig (gewenst nieuws), maar wel meetellen in het rapport.
6. **Smart sending**: aan (16 uur) voor alle wervings-, activatie-, duw- en slaapmails, uit voor welkom en sale/payout. Afwijking van de globale regel "uit in alle flows" (v4 1.3) omdat dit de laagste prioriteit is. Meten: wordt meer dan 30% overgeslagen door smart sending, dan uit en vertrouwen op regel 1.
7. **Prioriteit**: Snowball-mails zijn rang 8, onder Winback en Site abandonment. Bestaande flows krijgen er geen filter bij (R1 en P3 blijven zoals ze zijn), Snowball wijkt altijd.

### 3.3 Netto-effect per klant (eerste 60 dagen)

| Groep | Aandeel kopers (aanname) | Extra flowmails | Minder campagnes | Netto |
| --- | --- | --- | --- | --- |
| Koper zonder klik op A1 | ~90% | +1 (A1) | -1 | 0 |
| Koper die op A1 klikt | ~6% | +2 (A1, A2) | -2 | 0 |
| Reviewklikker | ~3% | +1 (REV1) | -1 | 0 |
| Valt af op F-KLANT (ticket, refund, lage review) | ~25% | 0 | 0 | 0 (ziet hooguit het blok in een mail die toch al gaat, zie de noot onder sectie 4) |
| Bestaande klant in importgolf | n.v.t. | +1 tot +2 | -1 tot -2 | 0 |

---

## 4. Waar het blok "Earn with Siraat" komt (exacte acties)

Template-wijzigingen gaan via de bron in `klaviyo/templates/v3/<map>/`, `build_template.py`, `qa_render.py` en `export_klaviyo.py` (PLAYBOOK 12). Daarna in de flow "Change template" of de flow-action patchen (PLAYBOOK 4). Vaste header en footer blijven (`partials/header.html`, `footer.html`). Alle blokken achter `{% if person|lookup:'snow_pilot' == 'in' and person|lookup:'Referral Link - SocialSnowball' %}`.

| Mail | Flow | Actie-ID | Template | Bericht (30 d) | Wat | Waarom |
| --- | --- | --- | --- | --- | --- | --- |
| P1-FIRST | X3ySuU | **119850551** | XhZ3Xr | R3gbkQ (afgeleid), 2.133 ontv., uitschrijf 0,24% | Alleen een P.S.-regel, geen knop: "P.S. Your order came with a personal Siraat link. Once the pan has proven itself, I'll show you how it works." | Klant heeft nog niets gekookt; vragen om te delen voelt te vroeg. Wel het idee planten, zodat A1 geen verrassing is. P1 is de mail met de hoogste klik (8%): niets afleiden van care-use en tracking. |
| P1-REPEAT | X3ySuU | **119850552** | UCEkN9 | WqxPSh (afgeleid), 306 ontv., uitschrijf 0% | Volledig blok onder de eerste knop | Herhaalkopers zijn bewezen tevreden; beste affiliates. |
| P2 (levering) | VQ93sx | **119850581** | UKxRjv | RCgdNW, 954 ontv., uitschrijf 0,53% | Blok onderaan, na de gebruikstips, vóór de footer | Moment van eerste ervaring. Onderaan, zodat de uitleg voorgaat. Uitschrijving P2 ligt al op 0,53%: bewaken, bij +20% relatief blok eruit. |
| P2-SAFE | X3ySuU | **119850554** | SvHrU6 | nog geen volume | Zelfde blok als P2 | Dekt de 60% zonder Delivered Shipment. |
| U1 (UGC) | VPixnJ | **119850759** | SRZXtf | RBrHK9, 573 ontv., klik 1,4%, $0 | **Ombouwen**: "Show us your first egg" + "Post it with your link: friends get {{offer}}, you earn {{reward}}". UGC15-ruil blijft. | U1 levert nu niets ($0); delen en foto's posten zijn dezelfde handeling. Snowball meet Instagram-posts (V5mKgv), dus de UGC-belofte wordt meetbaar. Geen extra mail. |
| Review A en B | XzHrez | A/B **119577637** (main 119577631, varianten 119577632 en 119577635) | variant-templates | WWGnBW, 32 ontv. | **Geen blok** | De reviewtest loopt tot half januari; een tweede vraag verdunt de Trustpilot-klik en raakt de test. Het bedankje komt als REV1 (S4). |
| Review fallback | TvfJYU | **121192022** | UEEzSL | nog weinig volume | **Geen blok** | Idem. |
| P3 (alle varianten) | X3ySuU | 119850558 tot 119850579 | div. | nog geen volume | **Geen blok** | Codemail met T02-test; één doel per mail. |
| V2 (VIP) | VTkxFL | **119850717** (Xw74Sx) en **119850718** (Ywfp5B) | | eerste mails rond 8 nov | P.S.-regel met link: "You've ordered twice. If a friend asks about the pan, this link gives them {{offer}} off." | Tekstmail van Benjamin, VIP = meest tevreden groep. V1 (code) niet. |
| Winback R1/R2 | UyFc78 | 119850720 tot 119850735 | | eerste mails ~23 nov | **Geen blok** | Doel is een eigen herhaalaankoop. |

**Noot: blok bij klanten met een ticket.** P2 en U1 sluiten refunds al uit in hun verzendfilter, U1 ook tickets sinds start. P2, P2-SAFE en P1-REPEAT hebben geen ticketfilter, en een template kan niet op events filteren, alleen op profieleigenschappen. Oplossing: een nachtelijke routine (zoals `sync_owned`) zet `snow_block_ok = false` voor profielen met een Opened Ticket in 21 dagen, een defect-tag ooit of een klik op `your-experience` in 180 dagen; het blok toont alleen bij `snow_block_ok != false`. Tot die routine draait: blok in P2, P2-SAFE en P1-REPEAT alleen in de 20%-pilot, en uitschrijving per mail tegen de holdout volgen (5.2).

---

## 5. Risico's en vangrails

### 5.1 Waar het mis kan gaan

| Risico | Kans | Vangrail |
| --- | --- | --- |
| Snowball stuurt **zelf** mails (welkom affiliate, sale, payout) naar alle 438 ingeschreven kopers, naast Klaviyo | hoog, onbekend | Besluit B1: in Snowball de eigen e-mails uitzetten behalve sale en payout, of in Klaviyo geen SALE1/PAY1. Eerst controleren wat er nu al uitgaat (Snowball-dashboard, test-inschrijving). |
| Klant voelt zich "verkocht" vlak na aankoop | middel | Geen vraag in P1-FIRST, A1 pas op dag 31, alleen na bezorgbewijs en zonder ticket. |
| Uitschrijvingen stijgen door extra mail | middel | Ruil tegen campagne (3.2), één uitnodiging per jaar, A2 alleen klikkers, geen duwtjes voor kopers. |
| Spamklacht op wervingsmails aan oude klanten (S2) | middel | Alleen betrokken 90 dagen, golven van 5.000, slechtste groepen laatst, stopregel per golf. |
| Bounces in S2 (oude adressen) | laag tot middel | Alleen wie in 90 dagen klikte of op de site was: adres leeft. Klaviyo suppresseert hard bounces zelf. |
| Self-referral, couponsites, eigen tweede adres | middel | Snowball-fraudeinstellingen (zelfde e-mail, adres, IP); steekproef referral-orders per week; alarm bij refundratio referral-orders > 1,5x winkelgemiddelde. |
| Commissie 20% op orders met 70% korting plus 10% vriendenkorting | hoog (marge) | Besluit B2/B3: vriendkorting niet stapelen in BFCM of commissie op netto orderwaarde; GOODFOOD (affiliatecode) blijft apart. |
| Vriendenaanbod 10% = HI10 (publieke code) | hoog (zwak aanbod) | Besluit B2: vriend 15% of een vast bedrag; test in fase 2 met een tweede programma. |
| Deliverability: link naar een Snowball-domein in de mail | laag tot middel | Link-domein vóór livegang door VirusTotal en Spectrum/ActiveArmor-check (incident 17 okt). Liefst een link op siraatskitchen.com (Snowball "tracking link" kan op het eigen domein, controleren). |
| Trustpilot: review koppelen aan beloning | middel | REV1 noemt de review alleen als bedankje; geen beloning voor de review, geen "unsolicited". |

### 5.2 KPI's en alarmdrempels (dagelijks in `scratchpad/golive/daily.py`, plus wekelijks rapport in #claude-mail)

| KPI | Waar | Groen | Signaal (bekijken) | Stop (actie op Draft of blok uit) |
| --- | --- | --- | --- | --- |
| Uitschrijving per Snowball-mail (A1, A2, REV1, W1, D1, AF2-4) | flow-values per bericht, na 500 ontv. | < 0,4% | 0,5% (PLAYBOOK 6) | > 1,0% |
| Uitschrijving P2, P2-SAFE, U1, P1-REPEAT met blok tegen holdout | zelfde mail, `snow_pilot` in tegen holdout | gelijk | +20% relatief | +50% relatief of > 1,0% |
| Spamklachten per Snowball-mail | idem | < 0,03% | 0,05% | > 0,08% (Gmail-grens 0,1% op accountniveau) |
| Bounce per mail | idem | < 0,7% | 1,0% | > 2,0% (alleen S2 realistisch) |
| Accountbreed: uitschrijvingen per dag | alle mails | ±5% van 14-dagengemiddelde (~360) | +10% | +20% twee dagen achter elkaar |
| Accountbreed: spamratio | alle mails | < 0,02% | 0,05% | 0,08% |
| Klik A1 (uniek, Bot Click uit) | | > 3% | < 2% | < 1% na 1.000 ontv. (copy herzien) |
| Smart-sending-overgeslagen | Klaviyo "Skipped" per bericht | < 15% | 30% | n.v.t. (instelling aanpassen) |
| Tickets over referral/affiliate/commission (Gorgias zoekterm) | Gorgias | < 5 per week | 10 per week | 25 per week |
| Refundratio referral-orders | Placed Order met Snowball-code tegen Refunded | ≤ winkel | 1,5x | 2x (fraudecontrole) |
| Activatie: affiliates met ≥1 sale | Xqbr4d, uniek per profiel | zie sectie 6 | onder conservatief na 60 dagen | n.v.t. |

### 5.3 A/B-tests (één variabele, winnaar op unieke klik en referral-sales, nooit op opens)

Volume S1 ~3.500 per maand (sectie 6): ~1.750 per arm. Groot effect (klik 3% naar 4,5%) zie je in ~4 weken; kleine effecten niet. Maximaal één test tegelijk in S1. A/B-slots moeten in de UI worden aangemaakt (API kan geen A/B toevoegen, LOG 19 okt 20:55).

| # | Test | Waar | Varianten | Maat | Start |
| --- | --- | --- | --- | --- | --- |
| TS1 | Framing | A1 | A "Give your friends {{offer}} off" (vriend eerst) tegen B "Earn {{reward}} on every friend's order" (verdienen eerst) | unieke klik op de link, Xqbr4d per ontvanger in 60 dagen, uitschrijving als controle | na de 20%-pilot, 4 weken |
| TS2 | Timing | S1 stap 1 | dag 31 tegen dag 38 (twee paden na profile-sample) | Xqbr4d per ontvanger in 60 dagen | na TS1 (januari) |
| TS3 | Blok aan of uit | P2, P2-SAFE, U1 | `snow_pilot` in tegen holdout (permanent 10%) | Xqbr4d per profiel, uitschrijving P2 | doorlopend (holdout) |
| TS4 | Onderwerp BFCM-affiliatemail | S7 | "Your link is worth the most this week" tegen "Your friends get 70% off. You get paid." | unieke klik | BFCM, alleen als het segment > 2.000 is |
| TS5 | Aanbod (fase 2, besluit Floris) | Snowball-programma B (bijv. vriend 15% of $25) voor 50% van de nieuwe kopers via S0 | 10%/20% tegen alternatief | referral-sales en marge per affiliate | februari |

### 5.4 Uitrolplan

| Fase | Wanneer (voorstel) | Wat | Doorgaan als |
| --- | --- | --- | --- |
| 0 · voorwaarden | t/m 27 okt | Besluiten B1 tot B5 (sectie 7), Snowball-eigen mails gecontroleerd, link-domein schoon, blokken en mails gebouwd en door qa_render groen, testmails ontvangen en bekeken (DECISIONS 8 okt: livegang pas na testmails). | alles afgevinkt |
| 1 · pilot 20% | 28 okt tot 4 nov (7 dagen) | S0 op 20% `in`, 10% holdout. Blokken in P1-REPEAT, P2, P2-SAFE, U1 live voor `in`. S4 (REV1) live. **S2 golf 1**: 20% van de eerste 5.000 (1.000 profielen, beste groep). S5 live (sale en payout zodra B1 duidelijk is). A1 heeft nog geen ontvangers (eerste inschrijvers bereiken dag 31 op 20 nov). | geen stopdrempel geraakt, signalen besproken |
| 2 · 50% | 4 tot 11 nov | S0 naar 50% `in`. S2 golf 1 de rest (4.000). S3 live. | idem |
| 3 · 90/10 | vanaf 11 nov | S0 90% `in`, 10% holdout blijvend. S2 golven van 5.000 per week tot de pool op is of een golf de stopdrempel raakt. | idem; per golf 7 dagen kijken |
| BFCM | 20 nov tot 6 dec | Geen nieuwe tests, geen nieuwe S2-golven (inbox staat vol, campagnes 2x). A1 loopt door (eerste kopers van 20 okt), want delen in BFCM is het sterkste moment, en A1 ruilt nog steeds tegen een campagne. S7-blok in campagnes, één vervangende affiliate-mail. | |
| Evaluatie | 15 dec en 31 jan | Holdout tegen `in`: extra referral-sales per profiel, uitschrijving. TS1 beslissen. | |

Terugdraaien: S0 split naar 0% `in` zet alle blokken en Snowball-flows tegelijk uit (de blokken lezen het label, S1 filtert erop). Flows op Draft, nooit verwijderen (cijfers blijven nodig, PLAYBOOK 7).

---

## 6. Verwachte aantallen

### 6.1 Uitgangspunten

| Grootheid | Waarde | Bron |
| --- | --- | --- |
| Kopers per maand | ~5.850 (P1-FIRST ~170 per dag, P1-REPEAT ~25 per dag) | flow-values 30 d, live sinds 9 okt |
| Ingeschreven via aankoop | ~100% van de kopers (438 inschrijvingen tegen 298 orders sinds 20 okt 14:40, inclusief achterstand) | XzrVJZ |
| Marketingtoestemming | ~92% | steekproef 120 |
| Geen ticket in 21 d, geen defect-tag | ~72% (catch-up: 33% ooit supportcontact; 21 dagen plus tags is ruimer) | 02-catchup, aanname |
| Geen refund of annulering in 60 d | ~98% | catch-up 18 op 1.820 |
| Bezorgbewijs (VcUF33 of UabgWz) | ~90% | catch-up |
| **Bereik S1 + S4 (A1 of REV1) per maand** | **~3.500** (5.850 x 0,92 x 0,72 x 0,98 x 0,90) | |
| Bereik blokken (P2 of P2-SAFE, U1, P1-REPEAT) | ~4.800 kookgerei-kopers per maand, waarvan ~2.300 ook U1 | |
| Wervingspool bestaande klanten (S2) | ~24.000 van 98.538 (toestemming ~75%, betrokken 90 d ~40%, geen ticket of defect ~80%, kookgerei) | aanname |
| Referral-orderwaarde | $200 (AOV nieuwe klant $224 min 10%) | research/deep/02, referral/01 |
| Commissie | 20% van de orderwaarde (~$40), vriend 10% (~$22) | Snowball-profiel |
| Incrementeel aandeel | 50% (een deel van de vrienden had via ads of zoekmachine toch gekocht) | aanname, gelijk aan flows-audit |

"Inschrijving %" is bij kopers 100% (automatisch). De echte trechter is: **bereikt → klikt op de link → activeert (≥1 sale binnen 90 dagen) → sales per actieve affiliate.**

### 6.2 Nieuwe kopers (S1, S4, blokken), per maandcohort, volle uitrol

| | Conservatief | Basis | Optimistisch |
| --- | --- | --- | --- |
| Bereikt met A1 of REV1 | 3.500 | 3.500 | 3.500 |
| Klik op A1/REV1 | 2,5% | 4% | 6% |
| Activatie (≥1 sale in 90 d, van bereikt) | 1,0% | 2,5% | 5,0% |
| Actieve affiliates per cohort | 35 | 88 | 175 |
| Sales per actieve affiliate (90 d) | 1,2 | 1,5 | 2,0 |
| **Referral-orders per maandcohort** | **42** | **131** | **350** |
| Omzet (x $200) | $8.400 | $26.200 | $70.000 |
| Commissie (20%) | $1.700 | $5.200 | $14.000 |
| Incrementele omzet (50%) | $4.200 | $13.100 | $35.000 |
| Extra uitschrijvingen (A1 0,4%, A2 0,3%, REV1 0,2%) | ~15 per maand | ~15 | ~15 |
| Bespaarde campagne-uitschrijvingen (ruil, ~0,4% per campagnemail) | ~14 | ~14 | ~14 |

Steady state na ongeveer 3 maanden (cohorten stapelen, sales lopen 90 dagen na). Ter vergelijking: het eerdere ontwerp zonder app (`research/referral/01-ontwerp.md` 8) rekende 202 / 607 / 1.618 vriendenorders per jaar; basis hier ~1.570 per jaar, dus aan de bovenkant daarvan, omdat Snowball elke koper zonder moeite een link geeft.

### 6.3 Bestaande klanten (S2), eenmalig over de hele pool van ~24.000

| | Conservatief | Basis | Optimistisch |
| --- | --- | --- | --- |
| Activatie (van bereikt) | 0,5% | 1,5% | 3,0% |
| Actieve affiliates | 120 | 360 | 720 |
| Sales per actieve (90 d) | 1,2 | 1,5 | 2,0 |
| Referral-orders | 144 | 540 | 1.440 |
| Omzet | $29.000 | $108.000 | $288.000 |
| Extra uitschrijvingen (W1 0,6%, W2 0,3%) | ~150 | ~150 | ~150 (verspreid over 5+ weken; minder dan één halve campagnedag) |

### 6.4 Wat de getallen het meest bepaalt

1. Of Snowball zelf al mailt (B1): zo ja, is een deel van de "activatie" al bereikt en is A1 een tweede mail over hetzelfde.
2. Het vriendenaanbod (B2): 10% is gelijk aan HI10, dus de vriend wint weinig. Met 15% of $25 ligt de basis eerder op 3 tot 4% activatie.
3. BFCM: de eerste A1-cohorten (orders vanaf 20 okt) bereiken dag 31 midden in de 70%-sale, de beste deelweek van het jaar. Dat kan de eerste twee cohorten richting optimistisch duwen, mits het aanbod stapelt (B2).

---

## 7. Besluiten en open punten voor Floris

| # | Vraag | Advies |
| --- | --- | --- |
| B1 | Welke e-mails stuurt Social Snowball zelf (welkom affiliate, sale, payout, maandoverzicht)? | Snowball: alleen sale- en payoutmeldingen aan (transactioneel van aard, bereikt ook wie geen marketing wil). Welkomst- en promotiemails uit; die doet Klaviyo met het frequentiebudget. Dan SALE1 alleen voor mijlpalen 1, 3 en 10, geen dubbel. |
| B2 | Vriendenaanbod 10% (= HI10) en stapelen op de sale? | Vriend 15% of $25 (eerder advies "Give $25, get $25"). In BFCM bevestigen of de Snowball-korting stapelt op 70% off; zo niet, dan de copy "your friends get the 70% off". |
| B3 | Commissie 20%: over welk bedrag (na korting, zonder verzending)? Uitbetaling in geld of tegoed (`Gift card code - Social Snowball` wijst op tegoed)? | Tegoed (gift card) is goedkoper en brengt de affiliate terug; tonen als "store credit" alleen als dat zo is ingesteld. Bedragen pas in de mail als dit vaststaat. |
| B4 | Bestaande klanten importeren in Snowball (route I) in golven van 5.000? | Ja, volgens de wervingspool in 2.4. |
| B5 | Linkdomein: kan de tracking link op siraatskitchen.com? | Ja graag; anders het Snowball-domein vóór livegang laten controleren (VirusTotal, Spectrum, ActiveArmor). |
| B6 | Welcome gift voor affiliates (TciBqC, status nu None)? | Fase 2: kleine gift bij de eerste sale (schort of deksel), niet bij aanmelding (voorkomt aanmelden alleen voor de gift). |
| B7 | Smart sending aan voor Snowball-mails (afwijking van v4 1.3)? | Ja, met meting van overgeslagen mails (3.2 regel 6). |

## 8. Bouwlijst (na akkoord, in volgorde)

1. Besluiten B1 tot B5.
2. Blok `partials/blocks/earn.html` en macro `{{BLOCK:earn}}` in `build_template.py` (en `expand.py` opnieuw afleiden), sample-profielen met en zonder Snowball-eigenschappen in `research/tailoring/test/samples/`.
3. Mails A1, A2, REV1, W1, W2, AF0 tot AF4, SALE1, SALE-M3, SALE-M10, PAY1, POST1, D1 in `klaviyo/templates/v3/snowball/` (Engels, Benjamin, skill siraat-direct-response, vaste header en footer, geen gedachtestreepje, alleen goedgekeurde claims: 30-day returns, 75-year warranty, 100,000+ happy customers).
4. Template-updates P1-FIRST (P.S.), P1-REPEAT, P2, P2-SAFE, U1 (ombouw), V2 (P.S.); qa_render groen; export; in de flows "Change template".
5. Segmenten: "Snowball · campagnepauze", "Snowball · wervingspool", "Snowball · slapend 60d", "Snowball · actief of geïnteresseerd"; campagne-cap uitbreiden (UI).
6. Flows S0, S1, S4, S2, S3, S5, S6 als Draft via `POST /api/flows/` (definitie met filters uit 1.4), daarna A/B-slot TS1 in de UI.
7. Rapport: `daily.py` uitbreiden met de KPI's uit 5.2 (per bericht en accountbreed), wekelijks overzicht in #claude-mail.
8. Uitrol volgens 5.4.
