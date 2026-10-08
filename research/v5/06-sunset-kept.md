# 06 · Sunset "keep me on the list": vervolgflow, segment en kortingsadvies

Datum: 8 oktober 2026. Vraag Floris (00-feedback-floris, Sunset): een flow voor wie in de sunset-mail op "keep me on the list" klikt, bijvoorbeeld een mail na een half uur, een eigen segment, en onderzoek of die persoon een korting verdient. Klaviyo alleen gelezen (MCP, GET). Niets aangemaakt, niets gecommit.

Nieuwe bestanden:
- `klaviyo/templates/v3/sunset/s3-kept.html` (30 minuten na de klik: bevestiging en één-tik-keuze)
- `klaviyo/templates/v3/sunset/s4-kept.html` (dag 4, 09:00: het verhaal en het bewijs, zonder korting)
- Flowsectie-voorstel voor `scripts/build_flows.py`: sectie 6 hieronder (getest in een kopie, dry-run offline: 0 fouten).

## Kort

1. **78.682 profielen** staan nu in "v4 · Sunset · unengaged 120d" (WuHSm6). De oude sunset (S7V4a7) haalde 0,42 procent menselijke klikkers per mail; wie klikte, bestelde in het attributievenster in ongeveer 3,7 procent van de gevallen, **zonder korting**, gemiddeld $205.
2. **Meten**: Klaviyo bewaart bij Clicked Email de URL **zonder querystring** (gecontroleerd op live events). "URL bevat keep" via UTM werkt dus niet. Trigger daarom op **Clicked Email met $flow = v4 · Sunset en Bot Click = false**. Een aparte bevestigingspagina is optioneel (zie 2.3).
3. **Wachttijd 30 minuten, twee mails** (S3 bevestiging + keuze, S4 verhaal + bewijs op dag 4). Geen codebalk.
4. **Geen korting.** Wie "houd me" klikt, toont leesbereidheid, geen koopaarzeling. Een code beloont maanden niet-lezen, leert de lijst dat de sunsetmail korting oplevert, en kost marge op orders die (blijkens S7V4a7) ook zonder komen. De sale en HI10 ziet de lezer gewoon in de volgende campagne.
5. **Twee fouten in de huidige sunset gevonden**: het live segment mist de botklikfilter en de leeftijdsgrens van 120 dagen uit het plan, en de S2-filter telt botklikken als "kept". Fix in 5.

## 1. Data

### 1.1 Omvang nu

| Bron | Waarde |
| --- | --- |
| Segment WuHSm6 "v4 · Sunset · unengaged 120d", profile_count op 8 okt | **78.682** |
| Gekoppelde flow | Vhi3iH "v4 · Sunset", status draft |
| Definitie live | can receive marketing · Received Email > 7 in 120 d · Active on Site 0 in 120 d · Placed Order 0 in 180 d · Clicked Email 0 in 120 d |
| Wijkt af van plan 2.8 | geen "Bot Click is false" op Clicked Email, geen "profiel ouder dan 120 dagen" |
| Ter vergelijking | oud Sunset Segment XY4NVp 17.365 (02-deliverability); "HS // Engaged 90 Days" VKxqyA 89.628 |

Bij de start van v4 · Sunset stromen dus ruim 78.000 profielen in één keer in. 03-voorstel (punt 4) adviseert de inhaalslag in delen van 10.000 per week; dat geldt ook hier, anders komen er in één week honderden kept-klikken en S3-mails tegelijk (geen probleem voor de kept-flow zelf, wel voor de klachtenpiek van S1).

### 1.2 Historische re-permission-klikken: oude sunset S7V4a7

S7V4a7 ("EB | Sunset Flow | 5/15/25", live sinds mei 2025, trigger segment XY4NVp) had **geen "keep me"-knop**: beide mails waren een bestsellerblok (Pan Pro, Cutting Board V2, Wok) met alleen een uitschrijflink. Elke klik daarop is dus een spontane heractivering. Laatste 365 dagen (flowrapport, conversie = Placed Order RSNxYV, accountattributie):

| Mail | Ontvangers | Menselijke klikkers (Bot Click false, som per maand) | Botklikkers | Uitschrijf | Spam | Orders (attributie) | Omzet | AOV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Email #1 "it's been a while" | 34.326 | 143 (0,42%) | 39 | 193 | 17 | 8 | $1.465 | $183 |
| Email #2 "Staying or Going?" | 30.391 | 129 (0,42%) | 28 | 290 | 9 | 2 | $587 | $294 |
| **Totaal** | **64.717** | **272** | **67** (20% van alle klikkers) | **483** | **26** | **10** | **$2.052** | **$205** |

Lezing:
- Orders per menselijke klikker: 10 / 272 = **circa 3,7 procent**. Bovengrens: de accountattributie telt ook open-attributie mee (1 dag), en Klaviyo-klikkers per maand zijn licht dubbel geteld. Ondergrens: kopen na het venster telt niet mee.
- Een op de vijf klikkers is een bot (security-scanners, vooral Outlook). Die moeten nooit als "kept" tellen.
- Geklikte pagina's: `/collections/all` (meeste), productpagina's van Pan Pro, cutting board en wok, en de homepage.
- Wat deze kopers daarna (na 5 dagen) deden, kan niet per profiel worden nagegaan zonder export van profiel-ID's (de MCP filtert events niet op flow). Proxy uit eigen data: `research/lijst/01-cohorten.md` sectie 5: niet-kopers die in week 1 klikken kopen in dag 7 tot 90 in **5,71 procent** van de gevallen, niet-klikkers in 2,48 procent (2,3 keer). Na 60 dagen zonder signaal is het 0,36 procent. Eén klik verplaatst iemand dus van de dode staart naar de klikkersgroep.

### 1.3 Benchmarks (extern, met bron)

| Bewering | Bron | Gewicht |
| --- | --- | --- |
| Flowconversie van lapsed ontvangers meestal 2 tot 5 procent, top 5 tot 10 procent; definities verschillen sterk | [eightx.co, win-back benchmarks](https://eightx.co/blog/average-win-back-reactivation-rate-benchmarks) | agency-blog |
| Omnisend lapsed-purchase-automatisering 0,52 procent conversie; OpenSend meldt 10,34 procent | samengevat in [opensend.com](https://opensend.com/post/win-back-campaign-success-rate-statistics) | vendor, ongelijke definities |
| Klaviyo Academy: sunset-profielen "have churned" en zijn "highly unlikely to purchase or engage again"; doel is bevestigen of afmelden | [Klaviyo Academy](https://academy.klaviyo.com/en-us/courses/automating-the-customer-journey-with-flows/lessons/say-goodbye-to-unengaged-customers), [Klaviyo glossary](https://www.klaviyo.com/glossary/what-is-sunsetting) | officieel |
| Korting aan koude profielen: meestal afgeraden ("not going to purchase anything if you are not interested, even with a discount"); tegenstem: grotere promo want ze gaan toch weg | [Klaviyo Community 3522](https://community.klaviyo.com/marketing-30/best-practice-for-sunset-flow-3522), [fether.app](https://fether.app/blogs/fether-blog/from-send-all-to-smart-a-klaviyo-guide-to-engagement-segments-and-sunset-flows) | meningen |

De eigen 3,7 procent per klikker valt in de externe 2 tot 5 procent, zonder korting.

## 2. Meten: hoe weten we dat iemand "keep me" klikte?

### 2.1 URL met "keep" werkt niet

Live Clicked Email-events (W247h8) bevatten `URL` zonder querystring: een campagnelink met UTM komt binnen als `https://siraatskitchen.com/`, de klikken van S7V4a7 als `/collections/all`. Een `utm_content=s1-keep` is dus onzichtbaar voor segmenten en triggerfilters. Alleen het **pad** telt.

### 2.2 Keuze: elke menselijke klik op S1 of S2 is "keep" (fase 1)

- Trigger: metric **Clicked Email (W247h8)** met triggerfilter **$flow = v4 · Sunset (Vhi3iH)** EN **Bot Click = false**.
- Dat sluit aan op het bestaande plan: S1 zegt "one tap keeps you on the list" en de stap-3-split in 2.8 telt elke klik als kept. Wie in S1 op de logo-link of de hero klikt, wil ook blijven.
- Terugval als Klaviyo `$flow` niet als triggerfilter accepteert: `Campaign Name contains "SUNSET · S"` (flowberichten hebben hun berichtnaam als Campaign Name, zie het live event "Post Purchase Flow | IT'S ON ITS WAY"). Daarom heten de nieuwe mails `SUNSET-KEPT · S3/S4`, zodat ze niet zelf in die filter vallen.
- Klik op uitschrijven of "Choose fewer emails" is geen Clicked Email naar de site (Klaviyo-links); wie uitschrijft, kan niet meer mailen en valt door de mail-filters.

### 2.3 Optioneel (fase 2): eigen bevestigingspagina

Een Shopify-pagina `/pages/still-on-the-list` ("You're staying. Thank you.", met de vier keuzes uit S3) als doel van de S1/S2-knop. Voordelen: de lezer ziet direct bevestiging, en `URL contains still-on-the-list` onderscheidt "keep" van productklikken. Nodig: akkoord Floris om een pagina aan te maken (geen product, maar wel een sitewijziging). Tot dan fase 1.

### 2.4 Segmenten (geen update-profile, les uit de checkout-bouw)

| Segment (nieuw) | Definitie | Gebruik |
| --- | --- | --- |
| `v4 · Sunset · kept` | Clicked Email where $flow = v4 · Sunset AND Bot Click = false, at least once in the last 180 days | rapportage (% kept), uitsluiting van een nieuwe sunset-instap binnen 180 dagen (flowfilter dekt dat al) |
| `v4 · Sunset · kept · pan` / `set` / `gift` / `proof` | Clicked Email where Campaign Name contains "SUNSET-KEPT · S3" AND URL contains `/collections/pans` / `/collections/bundles` / `/products/e-gift-card` / `/pages/third-party-testing`, in 180 days | campagnes met het juiste product (03-voorstel punt 1, zelfde vraag als in de pop-up) |

Kanttekening: de footer linkt ook naar `/collections/pans`, `/collections/bundles` en de labpagina. De Campaign Name-filter beperkt de ruis tot S3; een footerklik in S3 telt mee als keuze. Acceptabel; de gift-keuze is uniek.

## 3. Flow `v4 · Sunset · kept`

| Stap | Wachttijd | Mail / actie | Verzendfilter |
| --- | --- | --- | --- |
| trigger | | Clicked Email, $flow = v4 · Sunset, Bot Click = false | flowfilter: niet in deze flow in de laatste 365 dagen |
| 1 | **30 minuten** | **s3-kept.html** "You're staying. Thank you." (Benjamin, tekstmail, vier keuzelinks) | Placed Order 0 sinds flowstart |
| 2 | 4 dagen, tot 09:00 | **s4-kept.html** "The pan we started with" (Benjamin, verhaal + rapport 25895 + 75 jaar, knop naar pannen) | Placed Order 0 sinds flowstart · geen checkout- of cartmail in 3 dagen |
| einde | | terug in normale campagnes | |

Waarom zo:
- **30 minuten** (Floris' voorstel) en niet direct: de bevestiging komt terwijl de lezer nog weet dat hij klikte, maar niet als botreactie binnen seconden. Botklikken zijn er dan al uitgefilterd. Geen quiet hours nodig: de klik is van de lezer zelf, net als C1/K1 realtime gaan.
- **Twee mails, niet meer**: deze groep las maanden niets. S3 bevestigt en vraagt één ding (commitment, liking), S4 geeft het ene verhaal dat alleen Siraat kan vertellen (authority: rapport 25895; social proof: 100,000+). Daarna neemt de campagnestroom het over; een lange reeks zou precies het volume terugbrengen dat de sunset wilde weghalen.
- **Afzender Benjamin**, zoals S2 (de lezer antwoordde op een vraag van Benjamin).
- **Internationaal**: de sunsetgroep is gemengd US/INT. Daarom geen dollarbedragen, geen inch-maten, geen gift-blok met USD-waarden en een friction reducer die overal klopt ("30-day returns. 75-year warranty. 100,000+ happy customers.").
- Verhouding tot andere flows: een kept-profiel kan meteen in browse/cart/checkout vallen (klik naar de site). Die gaan voor; S4 wacht als er in 3 dagen een checkout- of cartmail was (dan valt S4 weg, de verkoopflow doet het werk).

## 4. Korting: nee (advies met reden)

| Argument | Uitleg |
| --- | --- |
| Marge | Wie klikt, koopt al in circa 3,7 procent zonder code (S7V4a7), AOV $205. 10 procent op die orders is circa $20 per order weggegeven op omzet die er ook zonder was; de sale (compare-at) en HI10 bestaan al. Floris zei bij checkout zelf: "korting is er al via compare-at". |
| Gedrag | Een code na "keep me" beloont maanden niet lezen. Actieve lezers krijgen dat niet. Als het rondgaat (codes lekken, 3.22), leert de lijst: negeer de mails, wacht op de sunset. |
| Eerlijkheid | S1 belooft "Nothing to fill in, nothing to buy" en "you'll get what we send everyone". Een cadeau achteraf is niet oneerlijk, maar wel een ander verhaal dan de mail vertelde. |
| Deliverability | De klik zelf is het gewenste signaal; een korting voegt daar niets aan toe. Wat helpt is dat S3 en S4 gelezen en aangeklikt worden; een tweede klik (keuze in S3) versterkt het. |
| Wat wel | Het bestaande aanbod: de lopende sale, gifts en HI10 in de eerstvolgende campagne; checkout/cart-flows met hun eigen ladder (plan 1.4) als iemand verder gaat. |
| Test (optioneel, na 8 weken) | Als Floris toch wil weten of een code loont: in S4 een 50/50-split S4 tegen S4 met HI10-regel (geen unieke code, geen nieuwe pool), meten op omzet per ontvanger over 30 dagen. Bij circa 1.000 tot 2.000 kept-profielen per maand is het verschil pas na 2 tot 3 maanden leesbaar. |

## 5. Daarna: terug in campagnes, en wie niet klikt

**Wie klikt (kept)**
- Valt direct uit WuHSm6 (Clicked Email 0 in 120 d klopt niet meer) en komt in "HS // Engaged 90 Days" (VKxqyA, menselijke klik), dus in de standaard campagnedoelgroep (03-voorstel punt 3).
- Krijgt S2 niet (verzendfilter Clicked Email 0 sinds flowstart) en komt in de stap-3-split van v4 · Sunset op JA.
- Nieuwe sunset-instap pas na 180 dagen (flowfilter v4 · Sunset) en alleen bij opnieuw 120 dagen zonder signaal. Kept-flow nogmaals pas na 365 dagen.
- Frequentie: het campagneplafond (3 per 7 dagen) geldt. Advies: de eerste 14 dagen na kept maximaal 2 campagnes, via het bestaande segment-mechanisme (`v4 · Sunset · kept` met klik in de laatste 14 dagen toevoegen aan de uitsluiting bij de derde campagne van de week). Laag gewicht; mag ook weg.

**Wie niet klikt** (blijft zoals in plan 2.8)
- S2 op dag 5, daarna 3 dagen wachten, dan segment `v4 · Sunset · suppressed` (S2 ontvangen, geen klik, geen sitebezoek, geen order), wekelijks bulk-suppressen na akkoord. Geen derde mail, geen korting als laatste redmiddel.

**Fixes die nodig zijn in de bestaande sunset (gevonden bij dit onderzoek)**

| # | Wat | Waarom |
| --- | --- | --- |
| 1 | Segment WuHSm6: Clicked Email-voorwaarde met `Bot Click = false` (zoals plan 2.8 en VKxqyA). | Nu sluit één botklik iemand voor 120 dagen uit van de sunset, terwijl die nooit echt klikte (20 procent van de klikkers in S7V4a7 was bot). |
| 2 | Segment WuHSm6: "profiel aangemaakt meer dan 120 dagen geleden" toevoegen (plan 2.8). | Ontbreekt live. Met "Received Email > 7 in 120 dagen" is het effect klein, maar het plan en het segment moeten gelijk zijn. |
| 3 | `build_sunset` S2-filter en de stap-3/suppressed-logica: Clicked Email met `Bot Click = false`. | Anders slaat een scanner S2 over en telt het profiel als kept. |
| 4 | S7V4a7 uitzetten op het moment dat v4 · Sunset live gaat (plan 1.1 "vervangt S7V4a7"). | Twee sunsets tegelijk geven 4 afscheidsmails. |

## 6. Flowsectie-voorstel voor `scripts/build_flows.py`

Niet in het script gezet (opdracht: voorstel). Getest in een kopie (`--offline`, uitvoer naar de scratchpad): 4 acties, 2 mails, 0 fouten, strikt lineair, geen update-profile, alleen de twee nieuwe templates ontbreken nog (export).

```python
# ---------------------------------------------------------------- 2.8b Sunset · kept (research/v5/06-sunset-kept.md)
# Ook toevoegen: FLOW_NAMES["sunsetkept"] = "v4 · Sunset · kept"; UTM["sunsetkept"] = "v4-sunset-kept";
# FLOWMAP["sunsetkept"] = "sunset"; BUILDERS["sunsetkept"] = build_sunset_kept; in PREFERRED direct na "sunset".
KEPT = "SUNSET-KEPT ·"  # berichtnamen: bevat bewust niet "SUNSET · S" (suppressed-segment) en niet "CODE ·" (cooldown)


def kept_prop(field, ftype, op, value):
    return {"type": "metric-property", "metric_id": CLICKED_EMAIL, "field": field,
            "filter": {"type": ftype, "operator": op, "value": value}}


def build_sunset_kept(f):
    """Instap: menselijke klik (Bot Click false) op S1 of S2 van v4 · Sunset. 30 minuten later S3, dag 4 S4.
    Geen samenkomende takken (lineair), geen update-profile, geen coupon."""
    trig = groups([kept_prop("$flow", "string", "equals", f.flow_ref("sunset"))],
                  [kept_prop("Bot Click", "boolean", "equals", False)])
    s4f = [[NO_ORDER_SINCE_START], [f.received_from("checkout", days=3)], [f.received_from("cart", days=3)]]
    entry = f.chain([
        lambda n: f.delay("minutes", 30, None, n),
        lambda n: f.mail("s3-kept", f"{KEPT} S3", n, [[NO_ORDER_SINCE_START]], label=FROM_BENJAMIN),
        lambda n: f.delay("days", 4, "09:00:00", n),
        lambda n: f.mail("s4-kept", f"{KEPT} S4", n, s4f, label=FROM_BENJAMIN),
    ])
    f.notes += ["'Kept' zonder update-profile: segment 'v4 · Sunset · kept' = Clicked Email (Bot Click false) where $flow = "
                "v4 · Sunset, minstens 1 keer in de laatste 180 dagen. Keuze in S3: Clicked Email waarvan URL het pad bevat.",
                "Geen korting en geen coupon (06-sunset-kept, 4). Klik op S1 én S2 geeft één instap (flowfilter 365 dagen).",
                "Terugval als de triggerfilter $flow weigert: Campaign Name contains 'SUNSET · S'."]
    return f.definition([mtrig(CLICKED_EMAIL, trig)], groups([not_in_flow(last_days(365))]), entry)
```

Dry-run-uitvoer (OVERZICHT): trigger "Clicked Email · triggerfilter: event.$flow equals Vhi3iH EN event.Bot Click equals False"; S4-filter verwijst naar v4 · Checkout abandonment (SNwQWU) en v4 · Cart abandonment (UshtNX).

Bouwvolgorde: na v4 · Sunset (heeft het flow-ID nodig). Voor de bouw: (a) `s3-kept` en `s4-kept` in de v4-inventaris (v4-flow-system sectie 5) en `exports/manifest.csv` zetten, anders slaat `qa_render.py` ze over en leest `build_flows.py` het onderwerp uit de topcomment; (b) templates exporteren (`v4 · Sunset · kept · s3-kept`, `... · s4-kept`); (c) bij de eerste bouw controleren dat Klaviyo een tijdsvertraging van 30 minuten en `$flow` als triggerfilter op Clicked Email accepteert.

## 7. QA en copy

- `qa_render.py` op beide mails: **0 FOUT** (2 groen, statisch, Django-render en browser op 600 en 390 px). Omdat de mails nog niet in de v4-inventaris staan, gedraaid via een kopie van het script met de inventarisfilter verruimd; geen wijziging aan het origineel. Screenshots: `exports/qa/shots/sunset-s3-kept-*.jpg`, `sunset-s4-kept-*.jpg`.
- Vaste header en footer uit `partials/`, knop in S4 via `{{BLOCK:cta}}` (VML), preheader met `mso-hide:all`, grijs #6E6E6E (fix 4 uit 01-inbox-check), friction reducer op 14 px.
- Claims alleen uit claims.csv: pure titanium cooking surface + no coatings, Light Labs ISO/IEC 17025, report no. 25895, 31 PFAS below the detection limit, 75 jaar ("covered for 75 years"), 30-day returns, 100,000+ happy customers, eerste orders 20 december 2024, look-alikes zonder naam. Geen em dash (grep 0).
- Onderwerpen (vijf types, A/B gekozen):

| Type | S3 | S4 |
| --- | --- | --- |
| Curiosity + benefit | One tap, then only what you came for | Why I'd still pick the first pan today |
| Specificity | **A: You're staying. Thank you.** | **B: December 20, 2024** |
| Question | What are you here for? | Read the report before you buy? |
| Story | **B: Got it, you're still on the list** | **A: The pan we started with** |
| Offer | n.v.t. (geen aanbod) | n.v.t. (geen aanbod) |

Geen A/B in fase 1 (plan 3.19): onderwerp A.

## 8. Verwachting en meten

- Kept-ratio: de oude sunset haalde 0,42 procent klikkers per mail zonder knop. Met een expliciete knop schat ik 1 tot 3 procent over S1 en S2 samen: **800 tot 2.400 profielen** uit de huidige 78.682, daarna circa 100 tot 400 per maand. Drempel uit 03-voorstel (monitoring 19): kept onder 3 procent is oranje, maar die drempel was gemaakt voor de snelle 60-dagen-sunset; voor de 120-dagengroep is 1 procent realistischer.
- Omzet: 800 tot 2.400 kept maal circa 3,7 procent maal $205 = **$6.000 tot $18.000 eenmalig** (bovengrens, accountattributie), zonder kortingskosten.
- Meten per week: kept (segment), keuze in S3 per optie, S3/S4-klik, orders per kept-profiel in 30 dagen, uitschrijving en spam per mail. Rood: spam > 0,08 procent op S3 of S4 (deze groep klaagt het meest, 01-cohorten 3).

## Open voor Floris

1. Akkoord op "geen korting" voor kept-profielen (of de optionele HI10-test in S4 na 8 weken).
2. Mag er een Shopify-pagina `/pages/still-on-the-list` komen (fase 2, 2.3)?
3. Akkoord op de vier fixes in sectie 5 (segment WuHSm6 en S2-filter: botklikken; S7V4a7 uit bij livegang).
