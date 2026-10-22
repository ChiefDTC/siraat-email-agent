# Affiliate-systeem v1 (Social Snowball) in Klaviyo, als concept · 22 okt 2026

Status: **alles staat als Draft in Klaviyo. Niets is live gezet, ingepland of verstuurd.** Geen bestaande live flow, template of campagne is gewijzigd (alleen gelezen). De 6 Snowball-standaardflows zijn niet aangeraakt.

Bronnen: `klaviyo/flows/affiliate-v1.md` (copy v2), `research/snowball/02-klaviyo-audit.md`, `03-flowstructuur.md`, `05-aanbod-besluit.md`, DECISIONS 21 okt. Wijzigingen van Floris op 22 okt (link snel na aankoop, refer-a-friend in elke flow, deelkit weg) zijn hierin verwerkt.

## 1. Wat er in Klaviyo staat

| Wat | Naam | ID | Link |
| --- | --- | --- | --- |
| Flow S1 | AFF S1 · Activatie nieuwe kopers | **VX4gA3** | https://www.klaviyo.com/flow/VX4gA3/edit |
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

Bouwscript: `scripts/build_aff_flows.py` (POST /api/flows met definition en temporary_id, weigert als de flownaam al bestaat). P1-blok: `scripts/aff_p1_block.py`.

## 2. Tijdlijn per klant

| Moment | Wat de klant krijgt | Bron |
| --- | --- | --- |
| Minuut 0 | Shopify-orderbevestiging | Shopify |
| Minuut 3 | E-Guide | YyaMjx (live, ongewijzigd) |
| Minuut ~20 | Snowball schrijft in (XzrVJZ), link staat op het profiel; S1 start (10% holdout) | Snowball, S1 |
| 1 uur | P1-FIRST of P1-REPEAT **met het blok "Give 15%, get 15%" onder de eerste alinea** (na de swap, sectie 6) | X3ySuU (live, swap voorbereid) |
| Bezorging + 1 en + 4 dagen | P2 (VQ93sx) en U1 (VPixnJ), met de refer-a-friend-footerregel (na toepassen, sectie 7) | live flows |
| Bezorging + 3 tot 6 dagen | **A1 = aff-announce** ("Your order can pay for itself") | S1 |
| A1 + 3 dagen | **A2 = aff-nudge-1**, alleen als A1 geopend en niet geklikt | S1 |
| Bezorging + 14 dagen | Reviewverzoek | XzHrez (live) |
| Geen bezorgbewijs | A1 op dag 21 (of het eerstvolgende slot) | S1 |
| Bij een referral-sale | aff-sale, direct (max 1 per 3 dagen) | S5a |
| Bij een uitbetaling | aff-payout, direct (max 1 per 14 dagen) | S5b |

Maximaal 2 activatiemails per persoon (A1, A2). Clickers en niet-openers krijgen na A1 niets meer.

## 3. Structuur S1 (VX4gA3)

Trigger: Enrolled in SocialSnowball through purchase (XzrVJZ).

Flowfilters (alle moeten gelden, op elk moment in de flow):
1. Has not been in this flow over all time.
2. Refunded Order (Xg6cwn) zero times since starting this flow.
3. Cancelled Order (TFervq) zero times since starting this flow.
4. Opened Ticket (Gorgias, YzvjGf) zero times in the last 21 days. (Er is ook "Ticket Created" S2Aax7 van Klaviyo zelf; niet gebruikt.)
5. New referral sale (Xqbr4d) zero times since starting this flow.

```
XzrVJZ
  └ Split: random 10%  ── JA → einde (holdout, geen mail)
                        └ NEE
      wacht 6 d (09:00) ── A1·d6
      wacht 3 d ── A2·d9  ── A1·d9
      wacht 3 d ── A2·d12 ── A1·d12
      wacht 3 d ── A2·d15 ── A1·d15
      wacht 3 d ── A2·d18 ── A1·d18
      wacht 3 d ── A2·d21 ── A1·d21 (cap: ook zonder bezorgbewijs)
      wacht 3 d ── A2·d24 ── A1·d24
      wacht 3 d ── A2·d27 ── A1·d27
      wacht 3 d ── A2·d30 ── einde
```

Waarom lineair: Klaviyo-flows mogen in de editor geen samenkomende takken hebben (v4 2.1). Een API-test op 22 okt (testflow SB92xY, meteen weer verwijderd) liet zien dat de API een samenkomende link wel accepteert, maar de editor is daar niet op getest; daarom de bewezen vorm. Elke A1- en A2-kopie heeft verzendfilters die bepalen of het profiel nu aan de beurt is. Wie wordt overgeslagen (nog niet bezorgd, reviewmail net gehad, smart sending), komt bij het volgende slot terug. Alle A1-kopieën heten `AFF S1 · A1 · announce · d<dag>`, alle A2-kopieën `AFF S1 · A2 · nudge-1 · d<dag>`; filters werken op de naam (`Campaign Name contains 'AFF S1 · A1'`), dus rapporteren kan per naam-prefix.

Verzendfilters A1 (dag 6 tot 18):
- Received Email where Campaign Name contains `AFF S1 · A1` zero times since starting this flow (één A1 per persoon).
- Delivered Shipment (VcUF33) **of** Postflows 4. Shipment Delivered (UabgWz) at least once since starting this flow (bezorgbewijs).
- VcUF33 zero times in the last 3 days en UabgWz zero times in the last 3 days (bezorging minstens 3 dagen geleden).
- Received Email where $flow = XzHrez zero times in the last 3 days, idem TvfJYU (3 dagen afstand tot de reviewmail; anders volgend slot).

A1 vanaf dag 21 (cap): dezelfde filters zonder de regel "bezorgbewijs". Wie op dag 19 tot 21 is bezorgd, wacht nog tot het slot daarna (dag 24).

Verzendfilters A2:
- Received Email where Campaign Name contains `AFF S1 · A1` at least once in the last 4 days (A1 in het vorige slot, dus precies 3 dagen geleden).
- Opened Email (WyrTym) where Campaign Name contains `AFF S1 · A1` at least once since starting this flow.
- Clicked Email (W247h8) where Campaign Name contains `AFF S1 · A1` zero times since starting this flow.
- Received Email where Campaign Name contains `AFF S1 · A2` zero times since starting this flow.
- Plus flowfilter 5 (geen sale sinds start).

Onderwerpen: A1 "Your order can pay for itself" / preview "Friends get 15% off their first order. You get 15% of what they pay." A2 "Has anyone asked about your pan?" / "That is the moment your link pays. Give 15%, get 15%." A/B-tests (onderwerpen B in de topcomment van de bron) kunnen alleen in de editor worden toegevoegd.

Bekende randen:
- U1 (VPixnJ) gaat op bezorging + 4. A1 kan op bezorging + 3 tot 6 vallen, dus soms binnen een dag van U1. Smart sending (accountinstelling) kan A1 dan overslaan; het volgende slot vangt hem op. Alternatief na de eerste week: de 3-dagenregel ook op VQ93sx en VPixnJ zetten (zelfde filter als de reviewflows).
- Holdout: Klaviyo kan via de API geen "Update profile property" plaatsen. Om de holdout later te kunnen meten: in de editor op de JA-tak van de 10%-split een Update profile property `snow_pilot = holdout` zetten vóór livegang. Zonder die stap is de holdout alleen te benaderen als "in flow S1, geen AFF S1-mail ontvangen, wel bezorgd".
- Postflows vuurt ca. 2,5 keer per zending; een late herhaling schuift A1 hooguit één slot op.

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

Overlap: het segment telt alleen inschrijvingen vóór 22 okt, S1 alleen nieuwe triggers na livegang. Niemand krijgt beide.

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
3. S1 (VX4gA3): alle 16 mails op Live (of eerst Manual voor een droge week), dan flow op Live. Eerste A1 valt pas 6 dagen later.
4. P1-swap (sectie 6, acties 119850551 en 119850552), alleen in een sessie die live flows mag wijzigen.
5. Campagne: segment TZ8Cmj opnieuw bekijken (doel ~300), verzendtijd zetten (10:00 ET), smart sending aan laten, versturen.
6. Daarna de bezorgblokken (sectie 6) en de footerregel (sectie 7), elk na een eigen akkoord.
7. Bewaken met de drempels uit 03-flowstructuur 5.2 (uitschrijving per mail < 0,4%, stop > 1%).
