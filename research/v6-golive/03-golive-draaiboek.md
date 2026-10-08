# 03 · Go-live-draaiboek v5-flows · vrijdag 9 oktober 2026

Voor Floris en Lola, om letterlijk af te vinken. Opgesteld 8 oktober 2026 (avond) door de go-live-planner. Alleen gelezen: repo, Klaviyo (GET). Niets gewijzigd in Klaviyo of Shopify.

**Wie**: **F** = Floris (Klaviyo-UI, Shopify, besluiten, de knoppen voor live en rollback) · **L** = Lola (testkoper, inbox, matrix invullen) · **C** = Claude (alleen lezen via API: profielen, events, flowstatus, rapporten; schrijft in Klaviyo of Shopify alleen na een uitdrukkelijk "ga" van Floris).

Alle tijden zijn Amsterdam (CEST). Labels in Klaviyo staan in het Engels zoals in de UI; een label kan iets afwijken, de plek klopt.

---

## 0. Stand vanavond (GET, 8 okt 19:30)

| Wat | Stand | Gevolg voor morgen |
|---|---|---|
| 13 v5-flows | alle **draft**: Checkout QUBUQV, Cart TZG9Mx, Browse WdRz5k, Welcome T4a5Mk, Post-purchase X3ySuU, Levering VQ93sx, Winback UyFc78, VIP VTkxFL, Anniversary XbYT7T, Site VLGhbR, Sunset TbYQmX, Sunset kept Wzz6xC, UGC VPixnJ | klaar om te testen |
| Oude flows | **live**: Y2TmNB, Tsg2tV (checkout), SwkMyn, TBWngE (cart), Wj6x6V, TyEjuQ (browse), SiaNLu (welcome), T2SmtR (failure to launch), RL3TU6 (post-purchase), UEfh4h (winback), S7V4a7 (sunset), naflows YyaMjx (FREE E-GUIDE), TSUnLs (E-Book), YcXbHx (Pan Education), WvRupU (Mystery Gift Reveal) | uitzetten per groep (sectie 5) |
| Coupons | `GET /api/coupons` geeft **0 coupons** terug | Floris controleert in de UI dat alle pools bestaan. Zonder pool kan een codemail niet renderen. **Blokkerend** voor elke codemail |
| Segmenten | aanwezig: WuHSm6 (Sunset unengaged), YxfuJT (Sunset kept, trigger). **Ontbreken**: Sunset suppressed, Welcome-bescherming, Campagne-cap | Welcome-bescherming en Campagne-cap zijn nodig vóór de eerste campagne van Homestead na livegang |
| Templates | 61 bijgewerkt, QA 61/61 groen (8 okt) | ochtendcheck herhaalt dit |

---

## 1. De dag in één oogopslag

| Tijd | Wat | Wie |
|---|---|---|
| **Vanavond 8 okt, vóór 22:00** | Voorbereiding A (sectie 2.1): testorders voor de eigenaar- en VIP-profielen, zodat de nachtelijke bezit-sync van 03:27 `siraat_owned` vult | F |
| 08:00 | Ochtendcheck door Claude (sectie 2.3): QA-poort, flowstatus, coupons, sync, segmenten. Status naar Floris | C |
| 08:00 tot 09:00 | Vooraf-checklist (sectie 2.2) afronden: coupons, lekcodes, T2SmtR, Homestead | F |
| 09:00 tot 10:00 | Testclones maken en live zetten alleen voor Lola's adressen (sectie 3.1) | F, C controleert via API |
| 10:00 | **Go/no-go 1**: vooraf-checklist volledig groen? Zo niet: niet testen met codemails | F |
| 10:00 tot 12:30 | Testronde: scenariomatrix (sectie 4). Lola voert uit en vult in, Claude volgt elk alias in Klaviyo en Shopify | L, C, F (testorders) |
| 12:30 tot 13:30 | Triage: elke FOUT krijgt eigenaar en besluit (fixen, accepteren, of groep later) | F, C, L |
| 13:30 | **Go/no-go 2** per groep (A, B, C) | F |
| **14:00** | **Groep A live**: Checkout, Cart, Browse, Welcome; oude 7 flows in dezelfde minuut uit; A/B-tests starten | F (klikt), L (leest mee), C (controleert) |
| 14:15 tot 15:00 | Rooktest op de echte live flows (scenario 37) | L, C |
| 15:00 | 1-uurscontrole groep A (sectie 6.1) | C |
| **15:15** | **Groep B live**: Post-purchase, Levering, Winback; oude post-purchase, winback en de vier naflows in dezelfde minuut uit | F |
| **16:15** | **Groep C live** (alleen bij go): Site, VIP, Anniversary, Sunset + Sunset kept (oude sunset S7V4a7 in dezelfde minuut uit), UGC alleen als de Gorgias-macro klaar is | F |
| 16:30 | Testclones op Draft (sectie 3.4) | F |
| 17:15 | 1-uurscontrole B en C | C |
| 21:00 | Avondcontrole alle groepen, kort bericht aan Floris | C |
| **Za 10 okt 14:00** | 24-uurscontrole (sectie 6.2) | C, F beslist |
| Zo 11 okt 14:00 | 48-uurscontrole (sectie 6.3); testorders annuleren | C, F |
| Ma 12 okt | Eerste testrapport (`test_report.py`), Vixr6X gaat zoals gepland uit | C, F |

Wie bij een probleem beslist: **Floris**. Wie de rollback uitvoert: **Floris** (UI), Claude levert binnen 10 minuten het bewijs (welke mails, hoeveel ontvangers).

---

## 2. Vooraf

### 2.1 Vanavond (8 okt), Floris

- [ ] **Testorder eigenaar**: in Shopify Admin > Orders > Create order: klant `lolagroothuis+x-eig@gmail.com`, product Titanium Hammered Pan Pro Standard, US-verzendadres (een openbaar adres, bv. een hotel), **Collect payment > Mark as paid**. Tag `TEST-GOLIVE`. Direct daarna fulfilment op hold (Order > More actions > Hold fulfillment) en in ShipBob op hold. **Niet annuleren of terugbetalen tot zondag** (een terugbetaling maakt een Refunded Order-event, en dat blokkeert P2, P3, V1, N1 en N2 in de tests).
- [ ] **Testorder VIP, order 1**: zelfde werkwijze, klant `lolagroothuis+vip-1@gmail.com`, Pan Pro Standard, US-adres.
- [ ] Morgenochtend controleert Claude dat beide profielen `siraat_owned` bevatten (`panpro`, `panpro_standard`). Zo niet: Floris zet het veld in het profiel (Audience > Profiles > alias > Properties > Add property `siraat_owned`).

### 2.2 Vooraf-checklist (vóór go/no-go 1 om 10:00)

**Coupons in Klaviyo** (F, Content > Coupons; zoek op naam). Elke pool: Shopify, unieke codes, 1 gebruik, 1 per klant, alleen one-time purchase, geen einddatum op de pool, vervaltijd na toewijzing zoals hieronder. Bij **Combinations** "**Product and collection coupons**" aanvinken, zodat de code samen met de automatische FREE GIFT (de 4 gifts) werkt. De naam moet exact kloppen; de templates zoeken op naam.

| # | Pool | Prefix | Korting | Vervalt na | Mail | OK |
|---|---|---|---|---|---|---|
| 1 | C4_10_48H | CO- | 10% | 48 uur | Checkout C4 | [ ] |
| 2 | K3_10_48H | CART- | 10% | 48 uur | Cart K3 | [ ] |
| 3 | B2_10_48H | VIEW- | 10% | 48 uur | Browse B2-clicked | [ ] |
| 4 | P3_THANKYOU_10_14D | THX- | 10% | 14 dagen | Post-purchase P3 | [ ] |
| 5 | R2_10_72H | BACK- | 10% | 72 uur | Winback R2 | [ ] |
| 6 | R2_VIP_15_72H | VIP- | 15% | 72 uur | Winback R2-VIP | [ ] |
| 7 | SK_REGULARS15_14D | REG- | 15% | 14 dagen | VIP V1 | [ ] |
| 8 | SK_ANNIV15_7D | YEAR- | 15% | 7 dagen | Anniversary N2 (door Floris aangemaakt) | [ ] |
| 9 | UGC15 (Shopify-bulkpool, niet in Klaviyo) | | 15% | | Gorgias-macro na U1 | [ ] |

- [ ] Kan Klaviyo de vervaltijd alleen in dagen? Dan 2 dagen (48 uur) en 3 dagen (72 uur). De mail toont "48 HOURS" en een datum = verzenddag plus 2 dagen; dat klopt dan.
- [ ] SK_ANNIV10_7D (oud) wordt door geen mail meer gebruikt; laten staan of verwijderen, maakt niet uit.

**Shopify, lekcodes uit** (F, Shopify Admin > Discounts > zoeken > Deactivate, of einddatum vandaag):
- [ ] 99%- en 100%-codes: `98347983474334593`, `SRJACEP6YNN1` (en de kopie), `SJHNDFJNSAD934`, `9MJ85MRZDE17`
- [ ] BFEXTRA10, NTWDHPKL5C, NYEXTRA10, EXTRA30
- [ ] (advies audit) HI10 op "once per customer" zetten. Besluit 8 okt: HI10 blijft automatisch in C1 tot C3. Alleen de limiet per klant is nieuw; Floris beslist.

**Klaviyo, oude naflows** (F): de vier gaan in dezelfde minuut als groep B uit (sectie 5.2). Vooraf alleen nakijken dat je ze kunt vinden:
- [ ] YyaMjx FREE E - GUIDE · [ ] TSUnLs EB | E-Book · [ ] YcXbHx EB | Pan Education · [ ] WvRupU Mystery Gift Reveal

**T2SmtR (Failure to launch)** (F, vóór groep A, GO-LIVE stap 8):
- [ ] Flows > "EB | Failure to launch" > in de bestaande split na de 30 dagen wachten een voorwaarde toevoegen: **What someone has done > Received Email > where Campaign Name contains "Old · Welcome" > at least once > in the last 60 days**. Alleen JA gaat door naar de mails. Niet als flowfilter. Opslaan. De flow blijft live.

**Sunset-segment** (F):
- [ ] Lists & Segments > "v4 · Sunset · unengaged 120d" (WuHSm6) > Edit > groep toevoegen: **Properties about someone > Created > is at least 120 days ago**. Opslaan. (De API weigerde dit.)

**Homestead-afspraak** (F, vóór 14:00):
- [ ] Wie verstuurt de campagnes vanaf vandaag? Afspraak schriftelijk (mail of Slack).
- [ ] Homestead sluit bij elke campagne uit: "v4 · Welcome protection" (in welcomelijst sinds minder dan 14 dagen, geen order) en "v4 · Campagne-cap" (minstens 3 niet-flowmails in 7 dagen). Deze twee segmenten bestaan nog niet: Floris maakt ze, of geeft Claude het "ga" om ze via de API te maken (definities in `exports/GO-LIVE.md` stap 3).
- [ ] Homestead plant tussen 9 en 12 oktober geen campagne met een eigen 10%-code die de T02-meting vervuilt.

**Open vraag compare-at $288** (F beslist, zie sectie 8):
- [ ] Mag de Pan Pro Standard in mails doorgestreept $288 tonen naast $144? Nu tonen de mails geen doorgestreepte prijs. Zonder besluit blijft dat zo; de livegang wacht hier niet op.

### 2.3 Ochtendcheck (C, 08:00, alleen lezen)

- [ ] `cd /tmp && python3 -I /home/user/siraat-email-agent/scripts/qa_render.py`: 61/61 groen
- [ ] `python3 -I .../scripts/build_flows.py` (GET-dry-run): 13 flows, 0 fouten, 0 ontbrekend; alle 13 nog draft
- [ ] `python3 -I .../scripts/sync_owned.py --check`: laatste run minder dan 36 uur oud; profielen `+x-eig` en `+vip-1` hebben `siraat_owned`
- [ ] Flowstatus van alle oude flows (lijst sectie 0) nog live, niets onverwachts aan of uit
- [ ] Coupons in de API (ter info; de UI is leidend)
- [ ] `python3 -I .../scripts/qa_inbox.py`: geen ernstige Gmail-clipping (>95 KB) en dark-mode-logo zichtbaar
- [ ] Kort statusbericht aan Floris: groen, of welke punten blokkeren

---

## 3. Testopzet

### 3.1 Waarom clones, en hoe (F, 09:00 tot 10:00)

De echte wachttijden (1 dag, 3 dagen tot 09:00, 45 dagen) passen niet in een testdag, en een flow op **Manual** laat ook echte klanten in de wachtrij lopen zodra de trigger komt. Daarom testen we op **kopieën** die alleen Lola's adressen binnenlaten, met wachttijden in minuten. De originele v5-flows blijven onaangeroerd op Draft; zo kan niemand vergeten een wachttijd terug te zetten.

Per testclone (9 stuks, zie tabel):

1. Flows > rij van de v5-flow > menu **⋯ > Clone** > naam `TEST · <flow>` (nooit met "v4 ·" ervoor, anders telt `test_report.py` mee) > **Clone flow**.
2. Triggerkaart > **Flow filters** > Add: **Properties about someone > Email > contains > `lolagroothuis+<prefix>`** (met OR voor een tweede prefix). De bestaande flowfilters laten staan.
3. Elke **Time delay**-kaart: eenheid Minutes, waarde uit de tabel, "Delay until a specific time" uit.
4. Elke split **Random sample 50%** voor T01 (bovenaan) en T02 (onder de cooldown-split): op **100%** zodat het testprofiel het v5-pad en de codemail krijgt. De T02-B-tekst (nocode) bekijken we via preview. A/B-acties T04 (W1) en T05a (B1) blijven 50/50.
5. Alleen in TEST · VIP en TEST · Anniversary: de verzendfilter "Placed Order = 0 in the last 14 days" op V1 en N2 vervangen door "Placed Order = 0 since starting this flow" (anders slaat de testorder van vandaag de mail over).
6. Status rechtsboven: **Live**, en in de pop-up kiezen voor alle acties Live.
7. Claude leest de clone via de API en bevestigt: filter aanwezig, wachttijden in minuten, splits 100%.

| Clone | Filter: Email contains | Wachttijden in de test |
|---|---|---|
| TEST · Checkout | `lolagroothuis+c-` OR `lolagroothuis+x-` | C1 2 min · C2 +4 · C3 +4 · C4 +4 |
| TEST · Cart | `lolagroothuis+k-` OR `lolagroothuis+x-` | K1/K1-ACC 2 min · K2 +4 · K3 +4 (acc: K3 +4 na K1-ACC) |
| TEST · Browse | `lolagroothuis+b-` OR `lolagroothuis+x-` | B1 2 min · klikvenster +8 · B2 |
| TEST · Welcome | `lolagroothuis+w-` | W1 2 min · W2, W3, W4, W5 elk +3 |
| TEST · Post-purchase | `lolagroothuis+pp-` | P1 2 min · P2-SAFE +3 · P3 +3 |
| TEST · Winback | `lolagroothuis+wb-` | R1 3 min · R2 +4 |
| TEST · VIP | `lolagroothuis+vip-` | V1 3 min · V2 +3 |
| TEST · Anniversary | `lolagroothuis+wb-` | N1 3 min · N2 +3 |
| TEST · Site | `lolagroothuis+s-` | A1 2 min · A2 +3 |

Niet als clone (trigger niet na te bootsen op een testdag): **Levering** (Delivered Shipment), **UGC** (Delivered Shipment), **Sunset** en **Sunset kept** (segment van 120 dagen inactief). Die gaan via preview met een echt event (3.3) en via de monitoring na livegang.

**Bekende beperking van clones**: de voorrangsfilters ("Received Email waarvan $flow = QUBUQV ...") wijzen naar de originele flows, niet naar de clones. Voorrang tussen flows testen we daarom pas op de echte live flows (scenario 37 en de 24-uurscontrole). De cooldown werkt wel in clones, want die kijkt naar de berichtnaam "CODE ·", die bij het klonen meegaat (Claude controleert de berichtnamen in de clone).

**Plan B als klonen niet lukt**: de originele flow op **Manual** (alle mails Manual). Profielen lopen dan tot elke mail en wachten in de handmatige wachtrij; per mail in Analytics de wachtrij openen en alleen Lola's adressen versturen. Nadeel: de echte wachttijden blijven staan (alleen de eerste mail is vandaag te testen) en echte klanten komen ook in de wachtrij. Vóór Live moet die wachtrij leeg (alle wachtende mails overslaan), anders krijgen klanten oude mails. Alleen gebruiken als plan A faalt.

### 3.2 Testprofielen en browsers (L)

- Alle mails komen binnen in **lolagroothuis@gmail.com** (plus-truc). Elk alias is een eigen Klaviyo-profiel. Een herhaling krijgt een nieuw alias (bv. `+c-uk2`), want flows laten iemand niet twee keer binnen.
- **Elk alias een eigen, schoon browservenster** (nieuw incognitovenster of een eigen Chrome-profiel). Klaviyo koppelt bezoek aan een cookie; in één venster lopen de events van twee aliassen door elkaar.
- **Checkout** (scenario's met `+c-`): geen identificatie nodig. Shopify geeft het e-mailadres uit de checkout door. Lola vult e-mail en adres in en gaat door tot de **betaalstap** (de stap waar de kaart gevraagd wordt), en sluit dan het venster. Nooit betalen.
- **Cart, browse en site** (`+k-`, `+b-`, `+s-`, `+x-`): de browser moet eerst bekend zijn bij Klaviyo. Werkwijze: in het nieuwe venster siraatskitchen.com openen (met de juiste VPN), de **Alia-pop-up** invullen met het alias, en dan pas het product bekijken of in de cart leggen. Claude bevestigt binnen 2 minuten dat het profiel een "Active on Site"-event heeft. Geen event: Lola logt in via siraatskitchen.com/account met het alias (inlogcode komt in Gmail) en probeert opnieuw.
- **Land**: checkout volgt de **valuta** (VPN of de landkiezer onderaan de site); cart volgt het **IP-land** (alleen VPN werkt); browse, welcome en site volgen het **profielland** (komt uit het IP bij de Alia-aanmelding; Claude controleert het veld en Floris corrigeert het in het profiel als het leeg is).
- **Adressen**: gebruik openbare adressen (hotel of station) in het juiste land, nooit een klantadres.
- **Ruis**: de oude flows zijn tot 14:00 live. Lola's aliassen krijgen dus ook oude mails ("Don't leave these hanging", "Hi ..., we saved these for you", de oude welkomstmails). Die negeren; in de matrix tellen alleen de mails die in de kolom "Verwacht" staan. Claude kan per alias de lijst Received Email (met flow) geven.

### 3.3 Preview met echt event (C, F)

Voor mails die niet live te testen zijn: flow openen > mail > **Preview & test** > profiel kiezen (het alias of een bestaand klantprofiel in het juiste land) en een **echt event** kiezen > **Send test email** naar het alias. Een test-send vult de mail met dat profiel en event, maar maakt **geen** Received Email-event en toont geen echte unieke code (code en vervaldatum controleren we alleen in de live clone-mails).

### 3.4 Na de testronde (F, 16:30)

- [ ] Alle TEST-clones op **Draft** (status rechtsboven). Niet verwijderen tot na de 48-uurscontrole (bewijs), daarna verwijderen.
- [ ] Testorders: fulfilment blijft op hold; **zondag 11 okt** annuleren met terugbetaling en restock (F).

---

## 4. Testscenario-matrix

### 4.1 Referentie per markt (wat in elke mail moet kloppen)

| Markt (signaal) | Valuta | Gifts | Pan Pro Standard | Fall-set (6 stuks) | Maat Standard | Verzendregel | Termijnen (Shop Pay, Affirm) |
|---|---|---|---|---|---|---|---|
| US (USD, land US) | $ | $70 | $144 | $299 | 11″ | Free shipping from the US | ja |
| Canada (CAD) | C$ (nooit kale "$") | C$95 | C$224 | C$449 | 28 cm | Free shipping, duties paid | nee |
| VK (GBP) | £ | £55 | £124 | £249 | 28 cm | Free shipping, duties paid | nee |
| Europa (EUR) | € | €70 | €139 | €279 | 28 cm | Free shipping, duties paid | nee |
| Australië (AUD) | A$ | A$100 | A$224 | A$449 | 28 cm | Free shipping, duties paid | nee |
| Nieuw-Zeeland (NZD) | NZ$ | NZ$120 | NZ$274 (geen doorgestreepte prijs) | NZ$549 | 28 cm | Free shipping, duties paid | nee |
| Singapore (SGD) | S$ | S$95 | S$204 | S$409 | 28 cm | Free shipping, duties paid | nee |
| Hongkong, Midden-Oosten, Zwitserland, rest | geen bedragen | "4 free gifts" | geen bedrag | geen bedrag | 28 cm | Free shipping, duties paid | nee |
| Onbekend (geen signaal) | geen bedragen | "4 free gifts" | geen bedrag | geen bedrag | 28 cm (11″) | Free shipping | nee |

Overal: geen US-only producten buiten de US (12-delige set, potten, roasting pan, 2 Pans + 2 Lids, 34-Pcs); in checkoutmails staan regelprijzen in het cart-blok alleen bij USD.

**Basischeck bij elke mail** (niet per regel herhaald; een fout hier is altijd FOUT):
- Header: monogram plus woordmerk SIRAAT naast elkaar (lockup), in licht en donker zichtbaar. Footer aanwezig met adres, Unsubscribe en Manage preferences.
- Afzender "Siraat's Kitchen", bij W2, S2, S3, S4 en V2 "Benjamin at Siraat's Kitchen". Reply gaat naar support@siraatskitchen.com.
- Geen `{{`, `{%`, `[VRAAG`, lege beelden of Engelse/Nederlandse mengtekst. Geen gedachtestreepje in onderwerp of tekst.
- Feiten: 30-day returns, 75-year warranty, 100,000+ customers, oprichter Benjamin. Nooit "100-day trial" of "lifetime".
- Elke knop werkt, opent de juiste pagina (PDP of checkout met de cart erin), UTM `utm_campaign=v4-<flow>`; geen 404 (vooral de fall-set-link: `titanium-hammered-pan-set-with-lids-6-pcs`).
- Codemail: code in tekst en knop gelijk, prefix klopt, datumtegels = verzenddag plus 2 dagen (48 uur) / 3 dagen (72 uur) / 7 of 14 dagen; in Shopify Admin > Discounts bestaat de code met 10% of 15%, 1 gebruik en dezelfde einddatum.

**Invullen**: kolom Resultaat = wat er echt kwam (onderwerp, tijd, afwijking). OK/FOUT = OK of FOUT plus één woord.

### 4.2 Checkout abandonment (TEST · Checkout)

Gemeenschappelijk: Lola legt het product in de cart, gaat naar de checkout, vult het alias, naam en een adres in het land in, klikt door tot de betaalstap en sluit het venster. Verwacht in de test: C1 binnen 5 min, daarna C2, C3 en C4 elk binnen 5 min na de vorige (hele reeks binnen 20 min). In C1 tot C3 staat HI10 al in de checkoutlink (`discount=HI10`), C4 heeft de eigen CO-code.

| # | Alias | Lola doet | Verwacht | Wat moet kloppen | Resultaat | OK/FOUT |
|---|---|---|---|---|---|---|
| 1 | +c-us-pan | VPN US. Pan Pro Standard 11″ in cart, checkout tot betaalstap | C1 "Your cart + 4 gifts are still pending" · C2 "Has the pan in your cart been tested?" · C3-P "One pan, or three?" · CODE · C4 "We're removing your discount in 48 hours" | $144, $70 gifts, 11″, "Free shipping from the US", termijnregel aanwezig; C2 PFAS-vergelijking en Light Labs 25895; C3-P biedt de fall-set $299 aan met werkende link; C4 code CO-..., tegels verzenddag + 2; knop opent de checkout mét de pan | | |
| 2 | +c-us-set | VPN US. Fall-set 6-Pcs in cart, checkout tot betaalstap | C1 · C2 · C3-S "What's in the box with your set" · C4 | "Buy 2, get 4 free. Six pieces for $299", what's in the box (Mini, Small, Large, drie deksels), nergens een Small of Mini als extra aanbod; geen doorgestreepte $598 zolang 2.2 open is | | |
| 3 | +c-us-schort | VPN US. Siraat Signature Apron (Azure) | C1 · C2-ACC "Yours, or a gift? Both work." · C3-ACC "The pan we made after the board" · C4 | Schortverhaal (canvas, verstelbaar, cadeau), geen panuitleg in C1 en C2; de pan pas als tweede stap in C3-ACC | | |
| 4 | +c-us-acc | VPN US. Titanium Cutting Board (Medium) | C1 · C2-ACC · C3-ACC · C4 | Plankverhaal, juiste productfoto en titel; geen dekselmaat of panmaat in C1/C2 | | |
| 5 | +c-us-gc | VPN US. E-Gift Card $50 | C1 · C2-ACC · C3-ACC · C4 | Gift-card-regel "$25 to $200", geen maten; **noteren**: werkt de CO-code in de Shopify-checkout op een gift card? (verwacht: nee; open punt 8.5) | | |
| 6 | +c-uk | VPN VK of landkiezer United Kingdom (GBP). Pan Pro Standard | C1 tot C4 als #1 | £124, £55 gifts, 28 cm, nergens inch, "duties paid", geen termijnregel, C3-P met £249-set, geen $ in de hele mail | | |
| 7 | +c-au | VPN AU (AUD). Fall-set | C1 · C2 · C3-S · C4 | A$449, A$100 gifts, 28 cm, geen "from the US" | | |
| 8 | +c-ca | VPN CA (CAD). Pan Pro Large 12″ | C1 · C2 · C3-P · C4 | C$ (nooit kale "$"), C$95 gifts, 30 cm, "duties paid" | | |
| 9 | +c-eu | VPN Duitsland of Nederland (EUR). Pan Pro Small 10″ | C1 · C2 · C3-P · C4 | €, €70 gifts, 26 cm | | |
| 10 | +c-sg | VPN SG (SGD). Pan Pro Mini 8″ | C1 · C2 · C3-P · C4 | S$95 gifts, 20 cm | | |
| 11 | +c-nz | VPN NZ (NZD). Pan Pro Standard | C1 · C2 · C3-P · C4 | NZ$120 gifts, NZ$549-set, geen doorgestreepte prijs, 28 cm | | |
| 12 | +c-hk | VPN HK (HKD). Pan Pro Standard | C1 · C2 · C3-P · C4 | "4 free gifts" zonder bedrag, geen HK$ of $-bedragen, 28 cm, geen US-only product | | |
| 13 | +c-ch | VPN Zwitserland (CHF), het "rest/onbekend"-geval. Pan Pro Standard | C1 · C2 · C3-P · C4 | Geen enkel bedrag, "4 free gifts", 28 cm. **Extra**: herhaal met +c-no (Noorwegen, rekent in USD, profiel zonder land): verwacht volgens de regel de US-versie; Floris beslist of dat acceptabel is (8.6) | | |
| 14 | +c-stop | VPN US. Pan Pro Standard, checkout tot betaalstap. **Na C1**: Lola meldt het, Floris maakt direct een order voor dit alias (draft order, Mark as paid, hold) | Alleen C1. C2, C3, C4 komen **niet** | In Klaviyo bij C2 "Skipped" voor dit profiel (Claude bevestigt). Bonus: aanmelden voor een nieuw C1 binnen 14 dagen kan niet (herinstap) | | |

### 4.3 Cart abandonment (TEST · Cart)

Gemeenschappelijk: nieuw venster met VPN, Alia-aanmelding met het alias (3.2), product in de cart, **niet** naar de checkout, venster sluiten.

| # | Alias | Lola doet | Verwacht | Wat moet kloppen | Resultaat | OK/FOUT |
|---|---|---|---|---|---|---|
| 15 | +k-us-pan | VPN US. Pan Pro Standard in cart | K1 "The hammered pattern: an easy wipe" (≤5 min) · K2-NEW "15 coated pans, or one" (+5) · CODE · K3 "We're removing your cart's 10%" (+5) | **K1 en K2 zonder HI10 en zonder code**; K3 code CART-..., tegels + 2 dagen; knoppen naar de PDP (niet naar /cart); $, 11″, $70 | | |
| 16 | +k-au-schort | VPN AU. Signature Apron (Moss) | K1-ACC "Picked it out? It's still here." · CODE · K3 (acc) | A$, IP-land AU herkend (geen $-bedragen), schortverhaal; geen K2 in de acc-tak | | |

### 4.4 Browse abandonment (TEST · Browse)

| # | Alias | Lola doet | Verwacht | Wat moet kloppen | Resultaat | OK/FOUT |
|---|---|---|---|---|---|---|
| 17 | +b-us-klik | VPN US, Alia-aanmelding, Pan Pro Large twee keer bekijken, niets in de cart. **In B1 op een knop klikken** binnen 5 min na ontvangst | B1 (één van de twee onderwerpen: "Get this pan with 10% off" of "Why I started making this pan") ≤5 min · CODE · B2-CLICKED "Your own 10% expires in 48 hours" (+8 tot 10 min) | B1 zonder code (verhaal en bewijs), B2 code VIEW-..., 12″, $149, tegels + 2 dagen. Claude bevestigt dat de klik-split op "B1 · T05a" werkte | | |
| 18 | +b-uk-geen | VPN VK, Alia-aanmelding, Pan Pro Standard bekijken, **niet** klikken in B1 | B1 · B2-NOTCLICKED "Skeptical? So were they." | Geen code in B2, £, 28 cm, profielland VK gebruikt | | |
| 19 | +b-us-acc | VPN US, Alia-aanmelding, Salt & Pepper Mill Set bekijken, in B1-ACC klikken | B1-ACC "Looked twice? Here's the detail." · CODE · B2-CLICKED (acc) | Molenverhaal, geen pan-PFAS-pitch in B1-ACC | | |

### 4.5 Welcome (TEST · Welcome, trigger lijst Uw8eZG via Alia)

| # | Alias | Lola doet | Verwacht | Wat moet kloppen | Resultaat | OK/FOUT |
|---|---|---|---|---|---|---|
| 20 | +w-us | VPN US, nieuw venster, Alia-pop-up (Card Game) invullen | W1 (T04-A of T04-B) "No PFAS. Here's the paper. And 10%." ≤5 min · W2 "The pan nobody else was making" · W3 "Has your cookware been tested?" · W4-US "Who are you cooking for?" · W5 "Tammy is on her fourth pan" (elk +3 tot 5 min) | W1: één regel over de Card Game-deelname, daarna verkoop, HI10 (A: codeblok, B: gift-card-beeld). W2 van "Benjamin at Siraat's Kitchen", verhaal PFAS, snijplank, zes maanden. W4-US mag de 12-delige set tonen; fall-set $299 | | |
| 21 | +w-uk | VPN VK, Alia-pop-up | W1 · W2 · W3 · W4-INT · W5 | W4-INT zonder 12-delige set, potten of roasting pan; £249-set; 28 cm | | |
| 22 | +w-a / +w-b | Twee extra aanmeldingen (VPN US) om beide W1-varianten te zien | W1 · T04-A bij de ene, T04-B bij de andere (niet gegarandeerd, 50/50) | Beide varianten één keer gezien; anders preview van de ontbrekende variant (3.3) | | |

### 4.6 Post-purchase en levering

Testorders maakt Floris (draft order, Mark as paid, tag TEST-GOLIVE, hold) op het moment dat Lola zegt "nu".

| # | Alias | Wat er gebeurt | Verwacht | Wat moet kloppen | Resultaat | OK/FOUT |
|---|---|---|---|---|---|---|
| 23 | +pp-us-pan | F: order Pan Pro Standard, US-adres | P1-FIRST "Good call. Here's what's coming." ≤5 min · P2-SAFE "When your pan arrives: the first egg" (+3) · CODE · P3-PAN "Which lid fits your pan?" (+3) | P1: e-booklink naar /products/e (The Green Clean E-Guide). P3 biedt het **28 cm / 11″-deksel** aan, nooit nog een Standard; code THX-..., 14 dagen | | |
| 24 | +pp-uk-set | F: order fall-set, VK-adres | P1-FIRST · P2-SAFE · CODE · P3-SET "The pan your set is missing" | Markt uit het verzendland: £, 28 cm; P3-SET biedt de Standard 28 cm aan (zit niet in de set), geen Small/Mini/deksel uit de set | | |
| 25 | +lev (preview) | C/F: preview van P2 (levering) en U1 (UGC) met een echt Delivered Shipment-event van een US- en een AU-klant, Send test naar +lev | P2 "The mistake that makes titanium stick" · U1 "Show us your first egg?" | P2: juiste maat per land; U1: "reply with a photo, 15% on your next order", reply-to support@ | | |

### 4.7 Bestaande klant, US-only, stoppen, cooldown

| # | Alias | Lola doet | Verwacht | Wat moet kloppen | Resultaat | OK/FOUT |
|---|---|---|---|---|---|---|
| 26 | +x-eig (heeft order van gisteren en `siraat_owned`) | VPN US, Alia-aanmelding of inloggen, **Stainless Steel Lid 28 cm** in cart, niet naar de checkout. Na K2: zelfde venster naar de checkout tot betaalstap | Cart: K1 · **K2-RETURNING "Adding to your Siraat kitchen?"**. Daarna checkout: C1 (eigenaarsversie) · C2-ACC · **geen C3-ACC** · C4 | Geen "first egg", geen PFAS-pitch voor nieuwe kopers, geen pan aangeboden die al in `siraat_owned` staat; deksel in de juiste maat. Na de checkout stopt de cart-reeks (geen K3) | | |
| 27 | +x-usonly | F of C (na "ga"): profielland op **United Kingdom** zetten. Lola: VPN **US**, Alia-aanmelding, 12-Pcs set bekijken (alleen in de US te koop) | TEST · Browse: B1 · B2 | De 12-delige set, $599 en potten komen **niet** in beeld; in plaats daarvan de 6-delige set in £249 (alternatief) | | |
| 28 | +x-cool | VPN US. Eerst cart (Pan Pro Standard, geen checkout) en wachten op **CODE · K3**. Dan in hetzelfde venster checkout tot betaalstap | Cart K1 · K2-NEW · CODE · K3. Checkout C1 · C2 · C3-P · **C4 nocode · cooldown "Last email about your cart"** | De C4 zonder code (cooldown: code in de laatste 30 dagen), geen tweede kortingscode | | |
| 29 | +c-us-pan (opnieuw, binnen 14 dagen) | VPN US, zelfde alias als #1 opnieuw een checkout tot betaalstap | **Niets** uit TEST · Checkout | Herinstap 14 dagen werkt (geen dubbele reeks) | | |

### 4.8 VIP, winback, anniversary, site

| # | Alias | Wat er gebeurt | Verwacht | Wat moet kloppen | Resultaat | OK/FOUT |
|---|---|---|---|---|---|---|
| 30 | +vip-1 (order 1 van gisteren) | F: **order 2**, Stainless Steel Lid 28 cm, US-adres | TEST · VIP: CODE · V1 "You're a VIP. Here's 15% off." (≤5 min) · V2 "A question from Benjamin" (+3) | Code REG-..., 15%, 14 dagen; geen 28 cm-deksel en geen Standard aangeboden; V2 van Benjamin | | |
| 31 | +wb-us | F: order Pan Pro Standard, US-adres (eerste order van dit alias) | TEST · Winback: R1-PAN "How's your pan doing?" · CODE · R2 "Your 10% expires in 72 hours". TEST · Anniversary: N1 "Six months in. Anything worn off?" · CODE · N2 "One year in. Here's 15% off." | R2: BACK-..., 10%, 72 uur, geen 404-setlink ($299); N2: YEAR-..., 15%, 7 dagen; nergens de Standard aangeboden die net gekocht is | | |
| 32 | +wb-vip (preview) | C/F: preview R2-VIP met een klant met twee orders, Send test | "15% exclusive discount, 72 hours" | 15%, VIP-toon, geen dubbele korting genoemd | | |
| 33 | +s-us | VPN US, nieuw venster, Alia-aanmelding, **alleen** de homepage en een collectiepagina, geen product openen | TEST · Site: A1 "Four eggs or five?" (≤5 min) · A2 "Where 100,000+ customers started" (+3) | Geen productevent; als Lola per ongeluk een product opent, komt er niets (correct) | | |

### 4.9 Sunset, sunset kept (preview, live-controle na groep C)

| # | Alias | Wat er gebeurt | Verwacht | Wat moet kloppen | Resultaat | OK/FOUT |
|---|---|---|---|---|---|---|
| 34 | +sunset (preview) | C/F: Send test van S1, S2 (TbYQmX) en S3, S4 (Wzz6xC) met een profiel uit WuHSm6 | S1 "Should we keep writing to you?" · S2 "Last email from me (unless you tap)" · S3 "You're staying. Thank you." · S4 "The pan we started with" | S2, S3, S4 van Benjamin; de "keep me"-knop werkt; geen korting in S3/S4. Na livegang (24 uur): instroom WuHSm6, aantal in YxfuJT groeit alleen door echte (geen bot) klikken | | |

### 4.10 Uitschrijven, voorkeuren, inbox en apparaten

| # | Alias / mail | Lola doet | Verwacht | Wat moet kloppen | Resultaat | OK/FOUT |
|---|---|---|---|---|---|---|
| 35 | +w-unsub | Aanmelden zoals #20; in W1 onderaan **Unsubscribe** klikken. In een andere mail (bv. +w-uk W2) **Manage preferences** openen | Bevestigingspagina in huisstijl; geen W2 tot W5 meer voor +w-unsub | Klaviyo-profiel: email marketing "Unsubscribed" (Claude bevestigt); voorkeurspagina laadt; in Gmail staat bovenaan de mail de link "Unsubscribe" naast de afzender (one-click) | | |
| 36a | C1 (#1), W1 (#20), K3 (#15), P3 (#23) | **Gmail web** (Chrome) en **Gmail-app** (iOS of Android) | Volledig zichtbaar | Geen "[Message clipped]", beelden laden, knoppen klikbaar, header-lockup scherp | | |
| 36b | zelfde vier | **Apple Mail** op iPhone (Gmail-account toegevoegd), licht en **donkere modus** | Leesbaar in beide | Logo zichtbaar in dark mode, tekst niet donker op donker, knoppen zichtbaar | | |
| 36c | zelfde vier | **Outlook** (outlook.com in de browser en, als beschikbaar, Outlook voor Windows met het Gmail-account) | Layout 600 px intact | Knoppen als knop (niet als blauwe link), geen verschoven tabellen, beelden met juiste breedte | | |
| 36d | zelfde vier | **Mobiel** (telefoon, ca. 390 px breed) | Eén kolom | Tekst leesbaar zonder zoomen, knoppen groot genoeg voor een duim, productkaarten onder elkaar | | |
| 37 | +live-1 t/m +live-4 (rooktest na 14:00, **echte** flows) | VPN US. Vier verse aliassen, elk een checkout met Pan Pro Standard tot betaalstap, kort na elkaar | Per alias óf v5 C1 na ca. 30 min, óf "Old · Checkout 1" na ca. 10 min | De echte live flow werkt; Claude ziet in Klaviyo de T01-split (beide paden mogelijk); geen mail uit de oude, uitgezette checkoutflows Y2TmNB/Tsg2tV | | |

**Totaal**: 37 scenario's (plus 36a tot d). Elke FOUT direct in de Slack-thread of aan Floris met alias en mail.

---

## 5. Livegang per groep (Klaviyo-UI)

### 5.0 Klikpaden (gelden voor elke flow)

- **Flow openen**: linkermenu **Flows** > zoekveld > naam (bv. `v4 · Checkout abandonment`) > klik op de naam (de builder opent).
- **Mailstatus controleren**: in de builder op een mailkaart klikken > rechts paneel > status **Draft / Manual / Live**.
- **Smart Sending**: mailkaart > **Settings** (of Sending settings) > **Smart Sending** staat **uit** in alle v5-mails (zo ontworpen: de voorrangsfilters regelen overlap). Controleer steekproefsgewijs één mail per flow.
- **T01-split**: in Checkout, Cart, Browse en Welcome de bovenste conditional split: **Random sample 50%**, JA = v5-pad, NEE = "Old · ..."-pad. Niets aan veranderen, alleen controleren.
- **Flow live zetten**: rechtsboven het statusmenu (**Draft**) of de knop **Review and turn on** > **Live** > in de pop-up kiezen voor **alle acties op Live** (Update all actions) > bevestigen. Daarna een paar mailkaarten openen: groen "Live".
- **Oude flow uit**: oude flow openen > statusmenu > **Draft** > bevestigen. **Niet archiveren** (PLAYBOOK §7, de cijfers blijven nodig).
- **A/B-test starten** (W1 T04, B1 T05a): op de A/B-kaart klikken > **Test settings**: verdeling 50/50, winnaar **handmatig** (geen automatische winnaar), metriek unieke kliks > **Start test** / Save. De API kon de test aanmaken maar niet starten.

"In dezelfde minuut": Floris heeft twee tabbladen open, het nieuwe flow-tabblad en de oude flows. Eerst nieuw op Live, dan direct de oude op Draft. Lola noteert de tijden. Gevolg om te weten: wie nu midden in een oude reeks zit, krijgt de rest van die oude mails niet meer (bewust geaccepteerd in GO-LIVE).

### 5.1 Groep A · 14:00 · Checkout, Cart, Browse, Welcome

Vooraf (13:50):
- [ ] Go/no-go 2 voor A is "go"; geen open FOUT in scenario 1 tot 22, 26 tot 29, 35 tot 36
- [ ] T2SmtR-voorwaarde staat (2.2)
- [ ] Coupons C4, K3, B2 bestaan
- [ ] Per flow: T01-split 50%, Smart Sending uit, alle mails Draft (worden nu Live)

Live (14:00), noteer de minuut:

| v5-flow live | Tijd | Oude flows in dezelfde minuut op Draft | Tijd |
|---|---|---|---|
| [ ] v4 · Checkout abandonment (QUBUQV) | | [ ] Y2TmNB EB Checkout · [ ] Tsg2tV Checkout Triple Pixel | |
| [ ] v4 · Cart abandonment (TZG9Mx) | | [ ] SwkMyn EB Cart · [ ] TBWngE Cart Triple Pixel | |
| [ ] v4 · Browse abandonment (WdRz5k) | | [ ] Wj6x6V EB Browse · [ ] TyEjuQ Browse Triple Pixel | |
| [ ] v4 · Welcome (T4a5Mk) | | [ ] SiaNLu EB Welcome Flow | |

Direct erna (14:05):
- [ ] A/B-test **T04** in Welcome (W1) gestart
- [ ] A/B-test **T05a** in Browse (B1) gestart
- [ ] T2SmtR blijft **live** (met de nieuwe voorwaarde)
- [ ] Claude: GET flowstatus van alle 11 betrokken flows, bericht "A staat" aan Floris
- [ ] 14:15 rooktest scenario 37

### 5.2 Groep B · 15:15 · Post-purchase, Levering, Winback

Vooraf: go voor B, coupons P3, R2 en R2-VIP bestaan, scenario 23 tot 25 en 30 tot 32 zonder open FOUT.

| v5-flow live | Tijd | Oude flows in dezelfde minuut op Draft | Tijd |
|---|---|---|---|
| [ ] v4 · Post-purchase (X3ySuU) | | [ ] RL3TU6 EB Post Purchase Flow · [ ] YyaMjx FREE E - GUIDE · [ ] TSUnLs EB E-Book · [ ] YcXbHx EB Pan Education · [ ] WvRupU Mystery Gift Reveal | |
| [ ] v4 · Post-purchase · levering (VQ93sx) | | (geen) | |
| [ ] v4 · Winback (UyFc78) | | [ ] UEfh4h EB Customer Winback | |

Blijven ongewijzigd live: XzHrez (review request), WsQDYu, UYALJ8, TLHht3, UcGzaL, Y4a7fJ, Wn2tsq, SxN86d, Vixr6X (gaat 12 okt uit zoals gepland).

### 5.3 Groep C · 16:15 · Site, VIP, Anniversary, Sunset, Sunset kept, UGC

Vooraf: go voor C, coupons REG en YEAR bestaan, segment WuHSm6 met de "Created"-groep (2.2), scenario 30, 31, 33, 34 zonder open FOUT.

| v5-flow live | Tijd | Oude flows in dezelfde minuut op Draft | Tijd |
|---|---|---|---|
| [ ] v4 · Site abandonment (VLGhbR) | | (UEqeEm is al Draft) | |
| [ ] v4 · VIP (VTkxFL) | | (geen) | |
| [ ] v4 · Anniversary (XbYT7T) | | (geen) | |
| [ ] v4 · Sunset (TbYQmX) **en** v4 · Sunset · kept (Wzz6xC) | | [ ] S7V4a7 EB Sunset Flow (twee sunsets tegelijk = vier afscheidsmails) | |
| [ ] v4 · UGC first egg (VPixnJ), **alleen** als de Gorgias-macro en tag `ugc-photo` en de UGC15-pool klaar zijn | | (geen) | |

Advies: als de testronde uitloopt, groep C naar maandag 12 oktober. Sunset en anniversary verliezen niets aan een paar dagen later.

### 5.4 Wat te doen bij een fout (rollback)

**Stopcriteria (direct ingrijpen)**: een mail met zichtbare code-tags of lege velden; een codemail zonder code of met een code die niet werkt; verkeerde valuta of US-only product bij een buitenlandse klant; een klant krijgt dezelfde soort mail uit oud en nieuw; Klaviyo toont "Skipped" door renderfouten; drempels uit sectie 6 overschreden.

| Ernst | Wat | Hoe (UI) | Wie |
|---|---|---|---|
| Eén mail fout | Alleen die mail uit | Mailkaart > status **Draft** (profielen slaan de mail over en gaan door) of **Manual** (ze wachten; later bewust versturen of overslaan). Voor een codemail: liever de codemail op Draft en de nocode-mail ernaast laten lopen | F, C levert het aantal geraakte ontvangers |
| Fout in een tak of split | Flow terug, oude aan | v5-flow statusmenu > **Draft**. Oude flow(s) van die rij statusmenu > **Live** en controleren dat de mailkaarten Live zijn | F |
| Groep breed (bv. coupons kapot, deliverability) | Hele groep terug | Alle v5-flows van de groep op Draft; de oude flows uit dezelfde tabel weer Live (A: Y2TmNB, Tsg2tV, SwkMyn, TBWngE, Wj6x6V, TyEjuQ, SiaNLu; B: RL3TU6, UEfh4h, en de vier naflows; C: S7V4a7). T2SmtR blijft live, maar bij een rollback van Welcome de nieuwe voorwaarde weer weghalen: SiaNLu verstuurt geen mails met de naam "Old · Welcome", dus anders krijgt niemand meer FTL-mails | F |
| Template-fout die snel te fixen is | Fixen en opnieuw | Claude past de bron aan, draait de QA-poort en, na "ga" van Floris, `export_klaviyo.py --live --i-am-sure --update` voor die ene template. Mail daarna weer Live | C, F |

Na elke rollback: tijd en reden in LOG.md (Claude), en bij klantimpact een kort bericht aan support (Gorgias) met wat klanten kunnen hebben gekregen.

---

## 6. Monitoring

Claude leest alles via de API (flow-values-report en Received Email, Bounced Email, Marked Email as Spam, Unsubscribed, Placed Order) en Shopify (kortingscodes, alleen lezen). Rapport aan Floris op de tijden uit sectie 1.

Verwachte instroom per dag (oude flows, gemiddelde 8 weken; per T01-arm de helft): checkout ca. 85, cart ca. 140, browse ca. 880, welcome ca. 580. Post-purchase volgt het aantal orders (ca. 250 per dag).

### 6.1 Na 1 uur per groep

- [ ] Elke v5-flow van de groep heeft instroom (behalve VIP, anniversary, sunset: daar kan het uur leeg zijn)
- [ ] Geen enkele verzending meer uit de uitgezette oude flows en naflows
- [ ] Geen "Skipped" door renderfouten of ontbrekende coupon
- [ ] Eerste echte mails: steekproef van 3 profielen per flow (land, valuta, product) klopt met 4.1

### 6.2 Na 24 uur (za 10 okt 14:00)

| Cijfer | Waar | Normaal | Ingrijpen als | Actie |
|---|---|---|---|---|
| Hard bounce per mail | Flow-analytics per mail | C1 16 tot 17% (typfouten in de checkout, bekend); W1 ca. 2,3%; overige < 1% | C1 > 20%, W1 > 4%, andere mail > 2% | Mail op Manual, oorzaak zoeken (lijstbron, typo's) |
| Spamklachten per mail | idem | < 0,05% | > 0,1% signaal; **> 0,3% stoppen** (Gmail/Yahoo-grens; Outlook staat al op 0,31% accountbreed) | Signaal: onderwerp en frequentie bekijken; stoppen: mail op Draft |
| Uitschrijving per mail | idem | < 0,5% (browse en welcome hoger: 1,4 tot 1,7%) | > 1% (browse en welcome > 2%) | Mail en onderwerp bekijken; bij > 3% mail op Draft |
| Instroom per flow | Flow-analytics | zie hierboven | < 50% of > 200% van normaal | Trigger, flowfilters en voorrang nakijken |
| T01-verdeling | instromers per pad (eerste mail v5 tegen "Old · ...") | 50/50 | buiten 40/60 bij > 100 instromers | Split nakijken |
| T02, T04, T05a | verzendingen per arm | beide armen > 0 | een arm 0 terwijl de andere > 20 | Split of A/B-test (gestart?) nakijken |
| Codes | Shopify Discounts, zoeken op CO-, CART-, VIEW-, THX-, BACK-, VIP-, REG-, YEAR- | elke code hoogstens 1 keer gebruikt; orders met code tonen ook de 4 gifts | een code 2 keer, gebruik na de vervaldatum, of een order met code zonder gifts | Coupon-instelling (Combinations, 1 per klant) aanpassen |
| Lekcodes | Shopify, gebruik BFEXTRA10, NYEXTRA10, NTWDHPKL5C, EXTRA30, 99/100%-codes | 0 nieuw gebruik | > 0 | Code alsnog uit |
| Conversie en omzet | flow-values-report per pad | eerste 14 dagen **niets beslissen** (beslisregels) | v5-pad 0 orders na 48 uur terwijl het oude pad in dezelfde flow ≥ 5 heeft; of flowomzet totaal > 30% onder dezelfde weekdag vorige week | Eerst techniek nakijken (links, checkout-restore, codes), geen inhoudelijke winnaar kiezen |
| Mails per nieuwe koper | 5 verse kopers, Received Email in 24 uur | P1 plus Shopify-bevestiging, geen naflowmails | > 3 marketingmails in 24 uur | Naflows en voorrang nakijken |
| Bezit-sync | `sync_owned.py --check` | laatste run < 36 uur | ouder | Routine nakijken (`trig_01WF2aAEzd6Ekb7AeW2kVvcd`) |

### 6.3 Na 48 uur (zo 11 okt 14:00)

- [ ] Alle cijfers van 6.2 opnieuw, nu met de eerste C2, K2, W2, W3 en B2-mails
- [ ] Eerste CO-, CART- en VIEW-codes zijn verlopen: in Shopify einddatum gepasseerd, geen gebruik erna
- [ ] Sunset (als groep C live is): S1 verstuurd aan het segment, S2 alleen aan wie niet klikte, YxfuJT groeit alleen door echte klikken
- [ ] Testorders (TEST-GOLIVE) annuleren met terugbetaling (F); TEST-clones verwijderen (F)
- [ ] `test_report.py` draaien met `--since=2026-10-09` (de constante GO_LIVE in het script staat op 8 oktober) en klaarzetten voor maandag
- [ ] Logregel in LOG.md met tijden van de livegang per groep en de uitkomst van 6.2 en 6.3 (C)

---

## 7. Volledige checklist (afvinken op de dag)

**Vanavond 8 okt (F)**
- [ ] Testorder `+x-eig` (Pan Pro Standard, US, Mark as paid, hold, tag TEST-GOLIVE)
- [ ] Testorder `+vip-1` order 1 (idem)

**08:00 tot 10:00**
- [ ] C: ochtendcheck (2.3) en statusbericht
- [ ] F: 9 coupons gecontroleerd (vervaltijd, Combinations "Product and collection coupons")
- [ ] F: lekcodes uit in Shopify
- [ ] F: T2SmtR-voorwaarde
- [ ] F: Sunset-segment "Created at least 120 days ago"
- [ ] F: Homestead-afspraak en segmenten Welcome-bescherming en Campagne-cap (zelf of "ga" aan Claude)
- [ ] F: besluit compare-at $288 (of bewust open laten)
- [ ] F: 9 TEST-clones met filter, korte wachttijden, splits 100%, Live
- [ ] C: clones gecontroleerd via API
- [ ] F: **go/no-go 1**

**10:00 tot 12:30 testronde**
- [ ] L: checkout #1 tot #14
- [ ] L: cart #15, #16
- [ ] L: browse #17 tot #19
- [ ] L: welcome #20 tot #22
- [ ] F: testorders #23, #24, #30, #31 en op afroep #14
- [ ] C/F: previews #25, #32, #34
- [ ] L: bestaande klant, US-only, cooldown, herinstap #26 tot #29
- [ ] L: site #33
- [ ] L: uitschrijven en voorkeuren #35
- [ ] L: Gmail, Apple Mail, Outlook, dark mode, mobiel #36a tot d
- [ ] C: per alias de Received Email-lijst en de codes in Shopify naast de matrix gelegd

**12:30 tot 13:30**
- [ ] Alle FOUT-regels: eigenaar en besluit
- [ ] F: **go/no-go 2** voor A, B en C apart

**Livegang**
- [ ] 14:00 Groep A live, 7 oude flows uit, T04 en T05a gestart
- [ ] 14:15 Rooktest #37
- [ ] 15:00 1-uurscontrole A
- [ ] 15:15 Groep B live, RL3TU6, UEfh4h en 4 naflows uit
- [ ] 16:15 Groep C live (of naar maandag), S7V4a7 uit; UGC alleen met Gorgias-macro
- [ ] 16:30 TEST-clones op Draft
- [ ] 17:15 1-uurscontrole B en C
- [ ] 21:00 avondcontrole

**Daarna**
- [ ] Za 14:00 24-uurscontrole (6.2)
- [ ] Zo 14:00 48-uurscontrole (6.3), testorders annuleren, clones verwijderen
- [ ] Ma 12 okt eerste testrapport, Vixr6X uit

---

## 8. Open beslissingen voor Floris

1. **Compare-at $288**: Pan Pro Standard doorgestreept $288 naast $144 in mails? Nu niet getoond. Advies: pas tonen als de $288 een echte eerdere verkoopprijs is (een verzonnen anker is een juridisch en vertrouwensrisico); de livegang wacht er niet op.
2. **Testorders**: draft order met "Mark as paid" en fulfilment op hold (advies), of een echte bestelling van een goedkoop product die gewoon verzonden wordt. Annuleren pas zondag, anders blokkeert de terugbetaling de tests.
3. **Alles op één dag?** Advies: A om 14:00, B om 15:15 alleen als de vier naflows in dezelfde minuut uitgaan, C mag naar maandag (de audit adviseerde gefaseerd).
4. **Naflows**: helemaal uit (zoals OVERZICHT-V5) of Mystery Gift Reveal na P3 laten starten? Het e-book zit nu in P1. Advies: alle vier uit.
5. **Gift card in checkout**: krijgt iemand met alleen een gift card in C4 een code die in Shopify niet werkt? Uitkomst van scenario 5 bepaalt of C4 een extra filter krijgt.
6. **Noorwegen en andere USD-landen zonder profielland** krijgen in checkout de US-versie (dollars, inch). Acceptabel voor nu, of liever de neutrale versie?
7. **HI10 op "once per customer"** zetten (advies audit), los van het besluit dat HI10 in C1 tot C3 blijft.
8. **Segmenten Welcome-bescherming en Campagne-cap**: Floris maakt ze of geeft Claude het "ga" (API). Nodig vóór de eerste Homestead-campagne.
9. **UGC first egg** pas live als Gorgias-macro, tag `ugc-photo` en de UGC15-pool er zijn.
