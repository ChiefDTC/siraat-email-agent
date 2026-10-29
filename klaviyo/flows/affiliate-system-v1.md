# Affiliate-systeem v1 (Social Snowball) in Klaviyo, als concept · 22 okt 2026

Status: **alles staat als Draft in Klaviyo. Niets is live gezet, ingepland of verstuurd.** Geen bestaande live flow, template of campagne is gewijzigd (alleen gelezen). De 6 Snowball-standaardflows zijn niet aangeraakt.

Bronnen: `klaviyo/flows/affiliate-v1.md` (copy v2), `research/snowball/02-klaviyo-audit.md`, `03-flowstructuur.md`, `05-aanbod-besluit.md`, DECISIONS 21 okt. Wijzigingen van Floris op 22 okt (link snel na aankoop, refer-a-friend in elke flow, deelkit weg) zijn hierin verwerkt.

## 1. Wat er in Klaviyo staat

| Wat | Naam | ID | Link |
| --- | --- | --- | --- |
| Flow S1 | AFF S1 · Activatie na bezorging | **R22pzb** | https://www.klaviyo.com/flow/R22pzb/edit |
| Flow S5a | AFF S5a · Verkoopmelding | **Yp6sKv** | https://www.klaviyo.com/flow/Yp6sKv/edit |
| Flow S5b | AFF S5b · Uitbetaling | **TkV5DY** | https://www.klaviyo.com/flow/TkV5DY/edit |
| Segment | AFF · bestaande affiliates | **TZ8Cmj** | https://www.klaviyo.com/list/TZ8Cmj |
| Campagne (Draft, niet ingepland) | AFF · Aankondiging bestaande affiliates | **01M5HJXNW21DZ91Q7G8P1N10D0** (bericht 01M5HJXNWCBAGB18A74NA9EYJD, template-kopie UaYp6t) | Klaviyo > Campaigns > Drafts |
| Bibliotheektemplate | AFF · announce | X4LBgN | bron `klaviyo/templates/v3/affiliate/aff-announce.klaviyo.html` |
| Bibliotheektemplate | AFF · nudge-1 | VNJw3y | `aff-nudge-1.klaviyo.html` |
| Bibliotheektemplate | AFF · sale | TphzUs | `aff-sale.klaviyo.html` |
| Bibliotheektemplate | AFF · payout | UyGqNi | `aff-payout.klaviyo.html` |
| Bibliotheektemplate (voorbereid, niet gekoppeld) | AFF · P1-FIRST + link | TVFnbF | kopie live XhZ3Xr + `aff-block-p1.klaviyo.html` |
| Bibliotheektemplate (voorbereid, niet gekoppeld) | AFF · P1-REPEAT + link | Rwes4z | kopie live UCEkN9 + `aff-block-p1.klaviyo.html` |

Alle mails: afzender "Benjamin from Siraat" <send@siraatskitchen.com>, reply-to = hetzelfde adres (geen support), niet transactioneel, UTM `utm_source=klaviyo`, `utm_medium=email`, `utm_campaign=aff-<mail>` (aff-announce, aff-nudge-1, aff-sale, aff-payout; ook in de dashboardlink van de template). Smart sending aan in S1 en de campagne, uit in S5a en S5b.

22 okt middag: S1 opnieuw gebouwd op de bezorg-trigger (R22pzb, sectie 3). De eerste versie VX4gA3 (trigger inschrijving, lineair met slots) is verwijderd; die was door ons gemaakt en nooit live.

Bouwscript: `scripts/build_aff_flows.py` (POST /api/flows met definition en temporary_id, weigert als de flownaam al bestaat). P1-blok: `scripts/aff_p1_block.py`.

## 2. Tijdlijn per klant

| Moment | Wat de klant krijgt | Bron |
| --- | --- | --- |
| Minuut 0 | Shopify-orderbevestiging en de pop-up met de referral-link | Shopify, Snowball |
| Minuut 3 | E-Guide | YyaMjx (live, ongewijzigd) |
| Minuut ~20 | Snowball schrijft in (XzrVJZ), link staat op het profiel | Snowball |
| 1 uur | P1-FIRST of P1-REPEAT **met het blok "Give 15%, get 15%" onder de eerste alinea** (na de swap, sectie 6) | X3ySuU (live, swap voorbereid) |
| Bezorging | S1 start (Postflows UabgWz), 10% holdout | S1 |
| Bezorging + 1 en + 4 dagen | P2 (VQ93sx) en U1 (VPixnJ), met de refer-a-friend-footerregel (na toepassen, sectie 7) | live flows |
| Bezorging + 3 dagen, 10:00 | **A1 = aff-announce** ("Your order can pay for itself"); + 5 dagen als er in de 2 dagen ervoor een reviewmail was | S1 |
| A1 + 3 dagen | **A2 = aff-nudge-1**, alleen als A1 geopend en niet geklikt | S1 |
| Bezorging + 14 dagen | Reviewverzoek | XzHrez (live) |
| Bij een referral-sale | aff-sale, direct (max 1 per 3 dagen) | S5a |
| Bij een uitbetaling | aff-payout, direct (max 1 per 14 dagen) | S5b |

Maximaal 2 activatiemails per persoon (A1, A2). Clickers en niet-openers krijgen na A1 niets meer. Zonder bezorgbewijs geen A1 (de vangnet-cap op dag 21 uit VX4gA3 is vervallen).

## 3. Structuur S1 (R22pzb)

Trigger: **Postflows - 4. Shipment Delivered (UabgWz)**. Vuurt voor bijna elke order (week van 15 okt: 1.678 events op 1.437 orders), dus de trigger is zelf het bezorgbewijs.

Flowfilters (alle moeten gelden, op elk moment in de flow):
1. Profieleigenschap `Referral Link - SocialSnowball` is gezet (alleen affiliates).
2. Has not been in this flow over all time (geen tweede mail bij een tweede pakket of een herhaald Postflows-event).
3. Refunded Order (Xg6cwn) zero times in the last 60 days.
4. Cancelled Order (TFervq) zero times in the last 60 days.
5. Opened Ticket (Gorgias, YzvjGf) zero times in the last 21 days.
6. New referral sale (Xqbr4d) zero times over all time (wie al verkoopt, heeft de uitleg niet nodig).

```
UabgWz (bezorgd)
  └ Split: random 10%  ── JA → einde (holdout, geen mail)
                        └ NEE
      wacht 3 d (10:00 profieltijd)
      Split: reviewmail XzHrez of TvfJYU ontvangen in de laatste 2 dagen?
        ├ NEE → A1 announce ──────────── wacht 3 d ── Split: A1 geopend en niet geklikt? ── JA → A2 nudge-1
        │                                                                              └ NEE → einde
        └ JA  → wacht 2 d (10:00) → A1 announce · na review ── wacht 3 d ── zelfde split ── JA → A2 nudge-1 · na review
```

Takken lopen niet samen (editorregel v4 2.1), daarom staat de staart A1, wacht, split, A2 twee keer. Mailnamen: `AFF S1 · A1 · announce`, `AFF S1 · A1 · announce · na review`, `AFF S1 · A2 · nudge-1`, `AFF S1 · A2 · nudge-1 · na review`; de A2-split werkt op de naam (`Campaign Name contains 'AFF S1 · A1'`, Opened Email WyrTym > 0 en Clicked Email W247h8 = 0 sinds start flow), dus rapporteren kan per naam-prefix. Geen verzendfilters op de mails nodig.

| Actie | Type | Wat |
| --- | --- | --- |
| 121654812 | split | random 10% holdout |
| 121654813 | wacht | 3 dagen, 10:00 profieltijd |
| 121654814 | split | Received Email (YkRM4Q) uit XzHrez of TvfJYU in de laatste 2 dagen |
| 121654815 | wacht | 2 dagen, 10:00 |
| 121654816 / 121654817 | mail | A1 (template-kopie VLgZtZ / RyqbQq) |
| 121654818 / 121654819 | wacht | 3 dagen, 10:00 |
| 121654820 / 121654821 | split | A1 geopend en niet geklikt |
| 121654822 / 121654823 | mail | A2 (template-kopie TTdRC8 / QQKSSp) |

Onderwerpen: A1 "Your order can pay for itself" / preview "Friends get 15% off their first order. You get 15% of what they pay." A2 "Has anyone asked about your pan?" / "That is the moment your link pays. Give 15%, get 15%." (uit de topcomment van de bron). A/B-tests (onderwerpen B in de topcomment) kunnen alleen in de editor worden toegevoegd.

Bekende randen:
- U1 (VPixnJ) gaat op bezorging + 4, A1 op bezorging + 3. Smart sending (accountinstelling) kan A1 overslaan als er net een andere mail was; er is geen tweede slot meer, dus wie wordt overgeslagen krijgt geen A1. Na de eerste week meten hoeveel A1's smart sending overslaat.
- De reviewcheck kijkt naar de 2 dagen vóór het A1-moment. XzHrez gaat op bezorging + 14, dus in de gewone tak speelt hij zelden; hij vangt vooral TvfJYU (fallback) en late Postflows-events.
- Holdout: Klaviyo kan via de API geen "Update profile property" plaatsen. Om de holdout later te kunnen meten: in de editor op de JA-tak van de 10%-split een Update profile property `snow_pilot = holdout` zetten vóór livegang. Zonder die stap is de holdout alleen te benaderen als "in flow S1, geen AFF S1-mail ontvangen".
- De linkeigenschap moet er bij bezorging al staan. Inschrijving gebeurt 17 tot 22 minuten na de order, bezorging dagen later, dus dat klopt voor kopers sinds 20 okt.

## 4. S5a en S5b

| Flow | Trigger | Flowfilter | Mail | Smart sending |
| --- | --- | --- | --- | --- |
| Yp6sKv AFF S5a · Verkoopmelding | New referral sale (Xqbr4d) | not in this flow in the last 3 days | direct `AFF S5 · SALE · aff-sale`, "A friend just ordered with your link" / "Here is your commission, and how your order can pay for itself." | uit |
| TkV5DY AFF S5b · Uitbetaling | Payout sent (WManrA) | not in this flow in the last 14 days | direct `AFF S5 · PAY · aff-payout`, "Your payout is on its way" / "Look for an email from Tremendous to choose PayPal, bank, Visa or a gift card." | uit |

Bedragen: event, dan profiel, anders "in your dashboard" (zie affiliate-v1.md). Snowball zet de bedragen als profieleigenschap; bij twee sales kort na elkaar kan het profielbedrag bij de verkeerde horen (daarom max 1 per 3 dagen).

## 5. Campagne en segment

Segment **TZ8Cmj "AFF · bestaande affiliates"** (via de API aangemaakt):
- Enrolled in SocialSnowball through purchase (XzrVJZ) at least once **before 22 okt 2026 00:00 UTC**;
- Delivered Shipment (VcUF33) of Postflows Shipment Delivered (UabgWz) at least once in the last 60 days;
- Refunded Order zero times in the last 60 days; Cancelled Order zero times in the last 60 days;
- can receive email marketing.

**Grootte op 22 okt 10:40 UTC: 56 profielen.** Van de ~437 ingeschrevenen zijn de meeste orders (13 tot 21 okt) nog niet bezorgd; het segment groeit vanzelf zodra bezorgbewijzen binnenkomen. Verzendmoment daarom pas als het segment rond de 300 zit (voorstel uit v1: rond 29 okt), en vóór verzending opnieuw de grootte bekijken.

Campagne **"AFF · Aankondiging bestaande affiliates"**: Draft, audience TZ8Cmj, template AFF · announce (kopie UaYp6t), onderwerp "Your order can pay for itself", smart sending aan, UTM aff-announce. De API zet bij een draft een standaard verzendstrategie (static, tijdstip van aanmaken); dat is geen inplanning, er is geen send job. **Niet op "Schedule" of "Send" klikken voordat de checklist rond is**; dan eerst het verzendtijdstip zetten.

Overlap: het segment telt inschrijvingen vóór 22 okt. S1 start nu op bezorging, dus een bestaande affiliate die na livegang van S1 (opnieuw) een bezorgevent krijgt, kan ook S1 krijgen. Oplossing vóór livegang: de campagne eerst versturen en in S1 een flowfilter toevoegen "Received Email where Campaign Name = AFF · Aankondiging bestaande affiliates zero times", of bewust accepteren (S1 telt per persoon maar één keer).

## 6. Link binnen het uur: P1 met blok (voorbereid, niet gekoppeld)

Floris 22 okt: geen extra mail op 1 uur (er gaan al bevestiging, E-Guide en P1), maar het blok in P1.

- Blok: `klaviyo/templates/v3/affiliate/aff-block-p1.klaviyo.html` (gegenereerd door `scripts/aff_p1_block.py` uit `aff-block.klaviyo.html`). Kop "Give 15%, get 15%" uit de profielvariabelen, rekensom op de waarde van **deze** order (`event $value`, alleen bij USD; anders het Pan Pro Duo-voorbeeld per verzendland), knop "Share my link". Toont alleen als `Referral Link - SocialSnowball` gevuld is en `snow_pilot != 'out'`. Inschrijving gebeurt 17 tot 22 minuten na de order, P1 gaat na 1 uur, dus de link staat er.
- Plaats: direct onder de eerste alinea ("Hi {first_name}, your order is in..."), boven het orderblok.
- Templates klaar in de bibliotheek: **TVFnbF** (P1-FIRST) en **Rwes4z** (P1-REPEAT), byte-kopie van de live templates van 22 okt 10:20 UTC plus het blok. Gerenderd (template-render) met US $214, UK zonder orderwaarde, profiel 20/10 en zonder link: geen restanten, geen em dash, zonder link geen blok.

Swap later (zelfde methode als de footerwijziging van 19 okt, `scratchpad golive/footer_apply.py`):

| Flow | Actie-ID | Bericht | Template nu | Nieuw |
| --- | --- | --- | --- | --- |
| X3ySuU v4 · Post-purchase | **119850551** | R3gbkQ P1-FIRST | XhZ3Xr | TVFnbF |
| X3ySuU v4 · Post-purchase | **119850552** | WqxPSh P1-REPEAT | UCEkN9 | Rwes4z |

Stappen: (1) controleer of XhZ3Xr/UCEkN9 sinds 22 okt niet gewijzigd zijn; zo ja, opnieuw bouwen met `python3 -I scripts/aff_p1_block.py --insert <live.html> <uit.html>` en de bibliotheektemplate bijwerken; (2) `PATCH /api/flow-actions/<id>` met `definition` (id, type send-email, data.message met nieuwe `template_id`, overige velden ongewijzigd); (3) GET ter controle: status ongewijzigd, nieuwe template-kopie bevat "Give {{", footer en links kloppen; (4) oude template-ID bewaren voor terugdraaien. Vereist een sessie die live flows mag wijzigen (PLAYBOOK 9: niet in Auto-modus).

Het branded blok in de bezorgmails (opdracht punt 4, ook later):

| Flow | Actie-ID | Bericht | Template nu | Wat |
| --- | --- | --- | --- | --- |
| VQ93sx v4 · Post-purchase · levering | **119850581** | RCgdNW P2 | UKxRjv | rijen uit `aff-block.klaviyo.html` direct boven de vaste footer (vóór `<tr><td class="pad" bgcolor="#282828"`) |
| X3ySuU | **119850552** | WqxPSh P1-REPEAT | UCEkN9 | vervalt: P1-REPEAT krijgt het P1-blok hoog in de mail (Rwes4z), niet nog een tweede onderaan |
| X3ySuU | **119850554** | TZ6TKb P2-SAFE | SvHrU6 | rijen uit `aff-block.klaviyo.html` boven de vaste footer |

Werkwijze: bibliotheekkopie van de huidige live HTML met het blok erin, template-render-test, dan PATCH flow-action. Let op: `aff-block.klaviyo.html` leest de markt uit `event.extra.shipping_address` (Placed Order). In VQ93sx is het event Delivered Shipment; daar valt het blok zonder orderwaarde terug op de percentageregel, tenzij `Siraat Last Order Value` op het profiel staat. Eerst in een render op een echt Delivered Shipment-event controleren.

## 7. Refer-a-friend in elke flow (voorgesteld, niet toegepast)

Snippet: `klaviyo/templates/partials/footer-refer-row.html`, één regel in de donkere footer, direct boven "Free shipping on all orders ... Unsubscribe | Manage preferences": "Give friends 15% off their first order. You get 15%. **Share your link →**". Alleen zichtbaar met een Snowball-link (dus kopers sinds 20 okt) en niet in de holdout; percentages uit het profiel.

Toepassen: snippet invoegen in `partials/footer.html`, alle templates opnieuw bouwen (`build_template.py`), `qa_render.py` groen, dan per flowactie bibliotheekkopie + PATCH template_id (zoals de footerwijziging van 19 okt, 89 mails). Scan op 22 okt (alleen GET): 25 live flows, 140 flowmails, **102 met de vaste footer**:

| Flow | ID | Met vaste footer | Zonder (oude arm of andere opmaak) | Acties met vaste footer (template) |
| --- | --- | --- | --- | --- |
| v4 · Browse abandonment · Triple Pixel | QNZyEb | 9 | 0 | 121177227 (TY9hCH), 121177228 (SVXXh8), 121177242 (XmHxNn), 121177244 (SPjGMd), 121177247 (W5EsqB), 121177250 (QQdytM), 121177251 (QPCirr), en 2 meer |
| v4 · Checkout abandonment | QUBUQV | 9 | 5 | 119850587 (Udgz6f), 119850597, 119850599, 119850603, 119850606, 119850613, 119850618, 119850620, en 1 meer |
| v4 · Welcome | T4a5Mk | 10 | 8 | 119850655 tot 119850674 e.v. |
| v4 · Cart abandonment | TZG9Mx | 10 | 3 | 119850627 tot 119850644 e.v. |
| v4 · Sunset | TbYQmX | 2 | 0 | 119850754, 119850756 |
| Review request · fallback | TvfJYU | 1 | 0 | 121192022 (UEEzSL) |
| v4 · Winback | UyFc78 | 10 | 0 | 119850720 tot 119850735 |
| v4 · Site abandonment | VLGhbR | 2 | 0 | 119850748, 119850750 |
| v4 · UGC first egg | VPixnJ | 1 | 0 | 119850759 (SRZXtf) |
| v4 · Post-purchase · levering | VQ93sx | 1 | 0 | 119850581 (UKxRjv) |
| v4 · VIP | VTkxFL | 4 | 0 | 119850713, 119850714, 119850717, 119850718 |
| v4 · Browse abandonment | WdRz5k | 11 | 1 | 119850690 tot 119850706 e.v. |
| v4 · Sunset · kept | Wzz6xC | 2 | 0 | 119850775, 119850777 |
| v4 · Post-purchase | X3ySuU | 24 | 0 | 119850551 tot 119850579 |
| v4 · Anniversary | XbYT7T | 3 | 0 | 119850738, 119850741, 119850742 |
| Review request · Delivered +14d | XzHrez | 3 | 0 | 119577631 (R4bgQf), 119577632 (Wc9HjH), 119577635 (UGdR4h) |
| EB Failure to launch, EB Winback UEfh4h, EB E-Gift Card, EB Pan Flash Buyers, BIS Waitlist, Ready for Pickup, FREE E-GUIDE | div. | 0 | 21 | andere footer, niet meenemen |

Volledige lijst per actie met template-ID: scratchpad `aff/footer-scan.json` (alleen ID's, geen klantdata); bij het toepassen opnieuw scannen, want templates wisselen. Overweeg de regel **niet** in de reviewmails (XzHrez, TvfJYU) en P3-codemails te zetten (één doel per mail, 03-flowstructuur sectie 4); dan 102 min 3 min 1 min 22 = 76 mails. Besluit Floris.

## 8. Copy-wijziging 22 okt (Floris: "te moeilijk, houd het helder")

- In elke affiliate-mail is de grijze kleine-letterregel ("Sharing? Tell friends it's your referral link (and use #ad...)", plafond $50, Tremendous-zin) vervangen door één regel: "Your sales and payouts are in your dashboard." (dashboardlink met UTM). Minimale wettelijke footer blijft.
- In het blok is "Sharing? Say it's your referral link." weggehaald (alleen "Friends get 15% off their first order.").
- aff-welcome-kit is gearchiveerd (`archive/welcome-kit/`): zonder deelkit was hij gelijk aan aff-announce. S1 is nu A1 = announce, A2 = nudge-1 alleen voor openers zonder klik.
- Bugfix: de regel "Or copy it:" had enkele aanhalingstekens rond een attribuut met `{{ ...|lookup:'...' }}`. Klaviyo weigerde de hele template te renderen (template-render 400). In de `.klaviyo.html` staan nu dubbele aanhalingstekens. De bron `.html` gebruikt de CTA-macro (sub="...") en heeft dezelfde vorm; na een herbouw met `build_template.py` deze regel opnieuw corrigeren (of de macro aanpassen). De generator in de scratchpad (`gen_aff_v2.py`) is verouderd ten opzichte van de repo: de repo-bestanden zijn de bron.
- Figma-rij 85:2 (oaxnBkz3MAbePRnorCrQwz) bijgewerkt: nieuwe 375 px US-screenshots, kolom welcome-kit weg, kolommen P1-FIRST + link, P1-REPEAT + link en de footerregel erbij.

**Open punt Floris (FTC):** de mails noemen de disclosure niet meer. De regel "zeg dat het je referral-link is, #ad in openbare posts" moet in het Snowball-portaal en de voorwaarden staan; affiliates moeten in openbare posts nog steeds melden dat ze commissie krijgen. Graag bevestigen dat het daar staat.

## 9. Verificatie (22 okt, na aanmaken)

- GET op de drie flows: status draft, alle 18 mails status draft, triggers XzrVJZ / Xqbr4d / WManrA, flowfilters zoals in sectie 3 en 4, verzendfilters per mail (6 bij A1 dag 6 tot 18, 5 bij A1 vanaf dag 21, 4 bij A2), alle links verwijzen naar bestaande acties, afzender, reply-to, smart sending en UTM per mail gecontroleerd.
- Template-render (Klaviyo `POST /api/template-render`) op de bibliotheektemplates, de flowkopieën (A1 d6 TxBksV, A1 d27 WHiPJV, A2 d9 SUAhQi, sale RKLGYN, payout WiKN4j) en de campagnekopie UaYp6t, met een testprofiel (Referral-eigenschappen 15%/15%, link, Siraat Last Order Value 214 USD) en UK zonder orderwaarde, plus 20/10 en zonder link voor de bibliotheektemplates: geen `{{`/`{%`-restanten, geen em dash. Uitkomsten: US "Your last order was $214 ... about $27. 8 friends: your whole order back.", UK "Pan Pro Duo at £177 ... you get £22.57", 20/10 alleen de percentageregel. Sale: "Your commission: $27.29", zonder bedrag "in your dashboard". `multiply`, `divide` en `ceil` werken in Klaviyo (render bevestigd).
- `scripts/check_previews.py affiliate`: 0 problemen. Screenshots 375 en 600 px: geen overflow, alle beelden laden.

Verificatie S1 R22pzb (22 okt middag, GET met definition): flow status draft, trigger UabgWz, 6 flowfilters zoals sectie 3, 12 acties, alle links verwijzen naar bestaande acties, 4 mails status draft, afzender "Benjamin from Siraat" <send@siraatskitchen.com> (reply-to zelfde adres), smart sending aan, UTM aff-announce / aff-nudge-1, wachttijden 3/2/3 dagen tot 10:00 profieltijd. Template-render op X4LBgN, VNJw3y en de flowkopieën VLgZtZ, RyqbQq, TTdRC8, QQKSSp (US $214 en UK zonder orderwaarde): geen `{{`/`{%`-restanten, geen em dash, link TESTER12345 5 keer, afmelden en voorkeuren aanwezig. VX4gA3 daarna verwijderd (GET geeft 404).

## 10. Launch-checklist (blokkerend)

1. **Snowball op 15/15**: vriend 15% op de eerste order, affiliate 15% van wat de vriend betaalt (zonder verzending en tax), max $50 per order. **SafeLink** aan (unieke code per klik).
2. **Alleen nieuwe klanten** voor de vriendenkorting; niet stapelen met HI10 of flowcodes.
3. **Self-referral-blokkade** (zelfde e-mail, adres, betaalmiddel, IP) aan.
4. **Uitbetaling 45 dagen** na verzending (wachttijd tegen retouren), via Tremendous; minimum bevestigen.
5. **Profielen tonen 15%**: `Referral Reward - SocialSnowball` en `Referral Friend Offer - SocialSnowball` = `15%` op een steekproef van ingeschreven kopers (nu nog 20%/10%; dan tonen de mails alleen de percentageregel en de kop "Give 10%, get 20%").
6. Snowball's eigen klantmails uit (behalve wat we bewust laten), zodat niemand dubbel mail krijgt (03 sectie 5.1, B1).
7. Referral-link getest: opent siraatskitchen.com, code wordt toegepast, domein schoon (VirusTotal).
8. Testmails van A1, A2, sale, payout en P1 + blok ontvangen en bekeken (DECISIONS 8 okt), op een echt profiel met link.
9. Holdout-tag in de editor op de 10%-tak (sectie 3), of bewust zonder.
10. FTC-tekst in het Snowball-portaal en de voorwaarden (sectie 8).

## 11. Go-live-stappen (na akkoord Floris, in deze volgorde)

1. Checklist 1 tot 10 afvinken.
2. S5a (Yp6sKv) en S5b (TkV5DY): mail op Live, dan flow op Live.
3. S1 (R22pzb): alle 4 mails op Live (of eerst Manual voor een droge week), dan flow op Live. Eerste A1 valt 3 dagen na de eerste bezorging.
4. P1-swap (sectie 6, acties 119850551 en 119850552), alleen in een sessie die live flows mag wijzigen.
5. Campagne: segment TZ8Cmj opnieuw bekijken (doel ~300), verzendtijd zetten (10:00 ET), smart sending aan laten, versturen.
6. Daarna de bezorgblokken (sectie 6) en de footerregel (sectie 7), elk na een eigen akkoord.
7. Bewaken met de drempels uit 03-flowstructuur 5.2 (uitschrijving per mail < 0,4%, stop > 1%).

## Wijzigingen 28 okt 2026 (A/B Q4)

- Verzendfilter $0 (28 okt 2026, A/B Q4): elke mail heeft een extra conditiegroep "Placed Order met $value > 0, minstens 1 keer in de laatste N dagen" (N = wachttijd + buffer). TikTok-samples, seeding en gratis vervangingen krijgen zo geen mails; een betaalde order valt altijd binnen het venster. Details en terugdraaien: research/ab-tests-q4/07-uitgevoerd.md, exports/rollback/2026-10-28-abq4/.
- Nieuw, live: **YhQJdb** "AFF S1 vangnet · Fulfilled +12d (geen Postflows)". Zelfde opbouw als R22pzb (10% holdout, A1 met review-split, A2 alleen bij open zonder klik), trigger Fulfilled Order, eerste wachttijd 12 dagen tot 10:00. Profielfilter van R22pzb plus: nooit een R22pzb-mail, geen Postflows-event sinds de start. Templates zijn kopieën (VfnKts, UCmGQP, XAcrfa, VaKv84).
- R22pzb A1/A2 (121654816, 121654817, 121654822, 121654823): extra filter "nooit een mail uit YhQJdb".
- Restpunt: de 10%-holdout van R22pzb is niet herkenbaar; een klein deel kan een vangnetmail krijgen.
