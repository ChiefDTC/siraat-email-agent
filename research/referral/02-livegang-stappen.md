# Referral · livegang stap voor stap (15 okt 2026)

Hoort bij `01-ontwerp.md`. Alles hieronder is nog **niet** gedaan. Volgorde aanhouden: eerst de besluiten van Floris (sectie 0), dan Shopify en Klaviyo, dan testen, dan pas live. Kortingscodes staan nergens in de repo (publiek); voorbeelden als `REF-XXXXXXXX`.

## 0. Wat Floris moet beslissen

1. **Aanbod**: optie A (15% / $25), **B (Give $25, get $25, advies)** of C ($20 / deksel). Bij A of C: hero's en bedragen in de twee bronnen aanpassen (sectie 5).
2. **Fase 1 alleen US**: ja (advies) of meteen alle markten (dan eerst lokale pools of procenten, en de mails per markt).
3. **Minimumbedrag vriend $100**: ja (advies; dekt de Mini-pan van $99 niet, wel elke andere pan en set).
4. **Beloning pas na de retourtermijn** (order 40 dagen oud, zonder refund): ja (advies).
5. **Plafond**: 10 beloningen per verwijzer per jaar (advies).
6. **Wie draait de batch** elke maandag: een agent (alleen lezen) plus een klik van Floris voor `--apply`, of volledig automatisch als geplande taak (vraagt een Klaviyo-sleutel met events:write).
7. **Wijziging in de live reviewmail XzHrez**: de 5-sterrenlink een eigen kenmerk geven (stap 4). Zonder dit geen REF1-REVIEW.
8. **P1-regel** toevoegen in de live post-purchase-mails (stap 6): ja of nee.
9. **Afzender**: "Siraat's Kitchen" zoals alle flows, of "Benjamin at Siraat's Kitchen" (tekstachtige mail, voor de klant persoonlijker).

## 1. Shopify

Geen eigen Shopify-korting met de hand aanmaken: Klaviyo maakt de kortingsregel (price rule) zelf aan bij stap 2. Wel vooraf:

- Controleren dat er geen automatische korting bestaat die met een vast bedrag stapelt op de 6-delige set (Shopify > Discounts > lijst; "Combinations" van de REF-regel na stap 2 nalopen: niet combineren met andere orderkortingen; wel met gratis verzending als dat nu bij orders zo werkt).
- Na stap 2 in Shopify > Discounts de nieuwe regel openen (titel begint met de Klaviyo-couponnaam) en noteren: type vast bedrag, $25, minimum $100, eenmalig gebruik, een per klant, geldt voor one-time purchase. Niets wijzigen in Shopify (wijzigingen gelden alleen per batch van 100 codes, 01 sectie 2).
- Optioneel en alleen na test: "Customer eligibility" op een klantsegment met 0 orders. Testen met een testklant die al besteld heeft (code moet weigeren) en na de volgende batch van 100 codes opnieuw controleren. Lukt het niet blijvend, dan alleen de batchregel.

## 2. Klaviyo-coupons (Klaviyo > Coupons > Create coupon > Shopify)

| Pool (exact) | Type | Waarde | Minimum | Geldt voor | Gebruik | Vervalt | Prefix | Voor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `REF_FRIEND_25` | vast bedrag | $25 | $100 subtotaal | alle one-time purchase producten | 1 keer, 1 per klant | 60 dagen na toewijzing | `REF-` | vriend (ref1, ref1-review, ref2-thanks) |
| `REF_THANKS_25` | vast bedrag | $25 | $50 | alle one-time purchase producten | 1 keer, 1 per klant | 90 dagen na toewijzing | `THANKS-` | verwijzer (ref2-thanks) |

Bij optie A: `REF_FRIEND_15` (15%, minimum $100). Bij optie C: `REF_FRIEND_20` ($20) plus `REF_LID_100` (100% op product Stainless Steel Lid, alle maten, 1 stuk via "maximum 1 item": in Klaviyo niet mogelijk volgens de community, dan via een Shopify-cadeauproduct oplossen; dit is de reden dat C handwerk is).

Na aanmaken: in de template-editor Preview met een testprofiel, controleren dat `{% coupon_code 'REF_FRIEND_25' %}` overal in de mail dezelfde code geeft (zeven keer in ref1), en dat `https://siraatskitchen.com/discount/REF-XXXXXXXX?redirect=...` de korting in de winkelwagen zet en naar de Pan Pro gaat.

## 3. Templates naar Klaviyo

1. Hero's uploaden: `klaviyo/templates/v3/referral/assets/ref1-hero.jpg` en `ref1-review-hero.jpg` via `scripts/export_klaviyo.py` (eerst dry-run, dan `--live --i-am-sure`), of handmatig in de bibliotheek, en de CDN-regels toevoegen aan `klaviyo/templates/v3/referral/assets/klaviyo-urls.txt` (`ref1-hero.jpg <url>`).
2. Bouwen: `python3 -I scripts/build_template.py klaviyo/templates/v3/referral/ref1.html klaviyo/templates/v3/referral/assets klaviyo/templates/v3/referral/assets/klaviyo-urls.txt` (idem ref1-review). Pas met alle URL's ontstaat `ref1.klaviyo.html`.
3. QA: `qa_render.py` kent de map `referral` nog niet. Voeg `'referral'` toe aan `FLOWS`, `'referral':[('none','geen event')]` aan `VARIANTS` en de twee mails aan de inventaris in `klaviyo/flows/v4-flow-system.md` sectie 5, of draai de kopie zoals op 15 okt (beide statisch groen). Dan `python3 -I scripts/qa_render.py --only=referral/ref1,referral/ref1-review` (vanuit /tmp).
4. Templates aanmaken in Klaviyo (CODE-editor): "v4 · Referral REF1" en "v4 · Referral REF1-REVIEW".

## 4. Reviewmail XzHrez: 5-sterrenlink onderscheiden

Nu gaan 5 en 4 sterren naar dezelfde URL (gecontroleerd in de live templates R4bgQf en RAz57u), dus een klik op 5 sterren is niet te herkennen.

- In beide templates (A/B-varianten van actie 119577637: hoofdactie 119577631 met R4bgQf, variant 119577632 met RAz57u) alleen de eerste ster-link wijzigen naar
  `https://www.trustpilot.com/evaluate/siraatskitchen.com?utm_content=r1-stars5`
  en de tweede (4 sterren) naar `...?utm_content=r1-stars4`. Bron in de repo: `klaviyo/templates/v3/review/r1-short.html` (twee `href`'s). Trustpilot negeert onbekende parameters; na de wijziging de link één keer openen om dat te bevestigen.
- Volgens PLAYBOOK 4: in de flow opnieuw "Change template" of de flow-actie patchen; de A/B-test loopt door (alleen een link wijzigt, geen copy).

## 5. Bij een ander aanbod dan B

Hero opnieuw maken (de aanbodbalk), bijvoorbeeld optie A:
`python3 -I scripts/make_hero.py klaviyo/templates/v3/referral/assets/src/P06-A_Stovetop_1920w_q82.jpg klaviyo/templates/v3/referral/assets/ref1-hero.jpg "Who's next|at your stove?" "A code for one friend, from you." "FOR ONE FRIEND" "--offer=THEIR FIRST ORDER 15% OFF  ·  \$25 BACK FOR YOU"`
(ref1-review: bron `P04-A_Stovetop_Pan_1920w_q82.jpg`, kop `"Five stars.|Pass it on?"`, label `"THANK YOU"`). Daarna in beide bronnen "$25 off their first order" en de mailto-tekst (`%2425`) aanpassen, en de couponnaam.

## 6. P1-regel (live post-purchase X3ySuU)

In P1-FIRST (actie 119850551, template SNfTa7, bron `klaviyo/templates/v3/post-purchase/p1-first.html`) en P1-REPEAT (actie 119850552, template Uw4wjc, bron `p1-repeat.html`) een P.S. onder de ondertekening:

> P.S. In a few weeks, once the pan has proven itself, I'll send you a code to share with one friend.

Alleen tonen bij USD-orders in fase 1: `{% if event.extra.presentment_currency == 'USD' %}...{% endif %}`. Bouwen, QA, template in de flow wisselen (PLAYBOOK 4 en 7). Geen andere wijziging aan P1.

## 7. Flows (eerst op Draft)

Bestaande ids waar aan gehaakt wordt: post-purchase **X3ySuU** (live), levering **VQ93sx** (live, bron van de titellijst), review **XzHrez** (live), checkout **QUBUQV** (bron van de botfilter-syntax). Metrics: Fulfilled Order **VtEiZT**, Placed Order **RSNxYV**, Refunded Order **Xg6cwn**, Cancelled Order **TFervq**, Opened Ticket Gorgias **YzvjGf**, Clicked Email **W247h8**, Received Email **YkRM4Q**, Coupon Assigned **XUMYt7**.

### 7.1 `v4 · Referral` (REF1)

- **Trigger**: Fulfilled Order (VtEiZT). Triggerfilters: `Items` contains any of de 48 titels in `research/referral/kook-set-titels.json`; `$currency_code` equals `USD`.
- **Flowfilters**:
  - has not been in this flow (alltime), plus `reentry_criteria {duration 1, unit alltime}` (PLAYBOOK 4);
  - `{"type":"profile-property","property":"email","filter":{"type":"string","operator":"not-contains","value":"storebotmail.joonix.net"}}` (exact zoals op QUBUQV).
- **Stap 1**: time-delay 26 dagen, `delay_until_time` 09:00:00, timezone profile.
- **Stap 2**: send-email REF1, onderwerp A "Who do you cook for?", preview "Give one friend $25 off their first order. You get $25 back.", afzender send@siraatskitchen.com "Siraat's Kitchen", reply-to support@siraatskitchen.com, smart sending uit. Verzendfilters (`additional_filters`):
  - Refunded Order (Xg6cwn) count equals 0, in-the-last 60 days;
  - Cancelled Order (TFervq) count equals 0, in-the-last 60 days;
  - Opened Ticket (YzvjGf) count equals 0, flow-start;
  - Received Email (YkRM4Q) count equals 0 in-the-last 60 days, metric_filters `$flow` equals `<id van v4 · Referral · review>`;
  - Received Email (YkRM4Q) count equals 0 in-the-last 2 days, metric_filters `$flow` equals `X3ySuU`; idem `XzHrez`.
  - Let op: een overgeslagen mail wordt niet ingehaald. Bij veel skips (Klaviyo "Skipped Send") de 2-dagenregel naar 1 dag.

### 7.2 `v4 · Referral · review` (REF1-REVIEW)

- **Trigger**: Clicked Email (W247h8). Triggerfilters: `$flow` equals `XzHrez`; `URL` contains `r1-stars5`; `Bot Click` equals false.
- **Flowfilters**: has not been in this flow (alltime); geen eerdere REF1 (Received Email, `$flow` = id van v4 · Referral, 0 keer alltime); e-mail bevat niet `storebotmail.joonix.net`; profiel met Placed Order met `$currency_code` USD ten minste 1 keer in 90 dagen (fase 1 US).
- **Stap 1**: time-delay 1 dag, 09:00 profieltijd. **Stap 2**: send-email REF1-REVIEW, onderwerp A "Know someone still on a coated pan?". Verzendfilters: Refunded Order 0 in 60 dagen, Opened Ticket 0 sinds flowstart.
- Volume: XzHrez ca. 3.400 verzonden per maand, 3,3% klik in de oude basis; het aandeel 5-sterrenklikken is onbekend, dus enkele tientallen per maand.

### 7.3 `v4 · Referral · beloning` (fase 1b, mail ref2-thanks nog te bouwen)

- Trigger: metric "Referral Reward Earned" (eigen event uit de batch, bestaat pas na de eerste `--apply`).
- Mail ref2-thanks (kort, Benjamin): "Your friend ordered. Here is your $25." met `{% coupon_code 'REF_THANKS_25' %}` (eigen gebruik, 90 dagen) en een nieuwe `{% coupon_code 'REF_FRIEND_25' %}` voor de volgende vriend. Bouwen volgens dezelfde opbouw zodra Floris het aanbod kiest; tot de eerste beloning (vroegst 40 dagen na de eerste vriendenorder, dus ca. 10 weken na livegang) is er tijd.

### 7.4 Wekelijkse batch (maandag)

```
python3 -I research/referral/referral_batch.py --pool=REF_FRIEND_25 --out=~/referral-batch.csv --state=~/referral-rewarded.txt
```
Alleen lezen. Uitvoer: per vriendenorder status OK / WACHT / NEE met reden, en een totaal (codes toegewezen, orders, omzet). CSV met profiel-id's staat buiten de repo (het script weigert een pad in de repo). Na controle van de OK-regels:
```
python3 -I research/referral/referral_batch.py --pool=REF_FRIEND_25 --apply --i-am-sure
```
Dat stuurt per OK-order een event "Referral Reward Earned" naar de verwijzer (start 7.3) en schrijft het order-id in het state-bestand. Getest op 15 okt alleen lezend op pool K3_10_48H: 94 codes, koppeling werkt, 0 orders met die codes in 30 dagen.

## 8. Testen vóór live

1. Testprofiel met een USD-testorder met een pan: REF1 in de flow-preview, code verschijnt overal gelijk, mailto opent met ingevulde tekst (Gmail web, Gmail iOS, Apple Mail), sms-link op iPhone en Android, kopieerlink werkt.
2. Testorder als "vriend" met de code: korting $25 bij $100+, geweigerd onder $100, geweigerd bij tweede gebruik, niet te combineren met HI10.
3. Batch draaien: de testorder moet als WACHT verschijnen (te jong) en als NEE bij zelfde adres.
4. Klik op 5 sterren in een testverzending van XzHrez: REF1-REVIEW start na 1 dag; klik op 4 sterren start niets.
5. Testmails met uniek onderwerp (PLAYBOOK 6, Gmail-thread).
6. Pas na akkoord Floris: flows op Live.

## 9. Meetplan

| Wat | Hoe | Doel na 8 weken |
| --- | --- | --- |
| Codes uitgedeeld | Coupon Assigned (XUMYt7) met `CouponKey` = REF_FRIEND_25, per week | volgt het volume (ca. 3.000 tot 4.000 per maand bij US-kookgerei) |
| Deelgedrag | Klik op de mailto-, sms- of kopieerknop is niet meetbaar (mailto wordt niet getrackt); proxy: klikratio op de hero en knoppen (Clicked Email in de flow) | klik REF1 boven 2% |
| Codes gebruikt | Placed Order met `Discount Codes` die begint met `REF-` (segment of batch-CSV), per week | 0,5% of meer van de uitgedeelde codes |
| Omzet via referral | Som `$value` van die orders; daarnaast GA4/Shopify `utm_source=referral` | richtwaarde realistisch $45k per jaar (01 sectie 8) |
| Echt nieuwe klanten | Batchstatus OK tegen NEE (reden "geen nieuwe klant", "zelfde adres") | NEE-aandeel onder 20% |
| Kosten | Shopify-rapport Discounts per code-prefix: totaal korting `REF-` (vriend) en `THANKS-` (verwijzer) | kosten onder 20% van referral-omzet |
| Bijvangst verwijzer | Orders met `THANKS-`-codes en hun `$value` | |
| Afmeldingen | Unsubscribe en spam per flowmail | onder 0,5% (PLAYBOOK 6) |

Rapport: wekelijks een regel in LOG.md uit de batchsamenvatting (alleen aggregaten). Na 8 tot 12 weken: besluit A houden, aanbod testen (B tegen C) of naar route B (app).
