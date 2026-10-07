# Go-live v4-flows · checklist voor 8 oktober 2026

Doel: alle v4-flows tegelijk live, met A/B (T01 oud tegen nieuw in checkout, cart, browse en welcome; T02 code tegen geen code; T04 W1; T05a B1). Bindend plan: `klaviyo/flows/v4-flow-system.md`. Flowdefinities: `exports/live/flows/<slug>.json`, leesbare boom per flow: `exports/live/flows/OVERZICHT.md`. Script: `scripts/build_flows.py`.

**Wie**: E = eigenaar in de Klaviyo-UI (of Shopify, Gorgias). C = Claude via de API (pas na een uitdrukkelijk "ga" van de eigenaar).

Stand van vandaag (GET, 7 okt 20:59): alle 12 metrics en lijst Uw8eZG bestaan. Er zijn **geen** v4-segmenten, **geen** coupons en maar 10 van de 63 benodigde templates (alleen checkout, en c4/c4-nocode nog niet). De enige v4-flow is de oude checkout-draft Y6yj2z.

---

## Stap 0 · Vooraf beslissen (E)

Zonder deze punten liever niet live:

- [ ] Publieke lekcodes dicht of met einddatum (BFEXTRA10, NYEXTRA10, NTWDHPKL5C, EXTRA30, COOK10, COOKHAPPY, GOODFOOD, de drie 100%-codes). Anders meet T02 niets (plan 3.22).
- [ ] Bday-sale-listing 6-delige set $349 blijft live tijdens de test (3.20).
- [ ] R2 alleen als "up to 50% off" echt live is (2.6).
- [ ] Gorgias: reply-to support@siraatskitchen.com komt binnen; macro en tag `ugc-photo` voor UGC15 (alleen nodig voor UGC first egg).
- [ ] Exacte schorttitels uit een echte order (het script gebruikt nu `Siraat Signature Apron - Azure/Moss/Ember/Oak`, aangenomen). Klopt het niet: titels in `SCHORT_TITELS` aanpassen en het script opnieuw draaien.

## Stap 1 · API-key (E)

- [ ] Key met **templates:write**, **images:write** en **flows:write** (plus de read-scopes). Nodig voor stap 4 en 6.

## Stap 2 · Coupons (E, Klaviyo > Coupons > Shopify > unique codes)

Elke pool: unieke codes, 1 gebruik, 1 per klant, alleen one-time purchase products, vervaltijd na toewijzing, geen einddatum op de pool. De naam moet exact zo, want de templates gebruiken `{% coupon_code '<naam>' %}`.

| Pool | Prefix | Korting | Vervalt na | Flow · mail |
| --- | --- | --- | --- | --- |
| C4_10_48H | CO- | 10% | 48 uur | Checkout · c4 |
| K3_10_48H | CART- | 10% | 48 uur | Cart · k3 |
| B2_10_48H | VIEW- | 10% | 48 uur | Browse · b2-clicked |
| P3_THANKYOU_10_14D | THX- | 10% | 14 dagen | Post-purchase · p3-* |
| R2_10_72H | BACK- | 10% | 72 uur | Winback · r2 |
| R2_VIP_15_72H | VIP- | 15% | 72 uur | Winback · r2-vip |
| SK_REGULARS15_14D | REG- | 15% | 14 dagen | VIP · v1 |
| SK_ANNIV10_7D | YEAR- | 10% | 7 dagen | Anniversary · n2 |

UGC15 is een Shopify-bulkpool voor de Gorgias-macro, niet in Klaviyo.

## Stap 3 · Segmenten (E in de UI, of C via POST /api/segments na akkoord)

Nodig voor de flows:

- [ ] **v4 · Sunset · unengaged 120d** (trigger van de Sunset-flow; zonder dit segment weigert het script die flow): can receive email marketing · profiel aangemaakt meer dan 120 dagen geleden · Clicked Email (Bot Click is false) 0 keer in 120 dagen · Active on Site 0 keer in 120 dagen · Placed Order 0 keer in 180 dagen · Received Email minstens 8 keer in 120 dagen.
- [ ] **v4 · Sunset · suppressed** (nieuwe definitie, want "update profile" kan niet via de API): in segment "v4 · Sunset · unengaged 120d" · Received Email waarvan Campaign Name "SUNSET · S2" bevat, minstens 1 keer in de laatste 60 dagen · en 0 keer in de laatste 3 dagen. Wekelijks bulk-suppressen (handmatig of routine, na akkoord).

Nodig voor campagnes (geen flow hangt ervan af, wel vóór de eerste campagne na livegang):

- [ ] **v4 · Welcome-bescherming**: Uw8eZG-lid sinds minder dan 14 dagen en Placed Order 0 keer in 14 dagen. Uitsluiten bij elke campagne.
- [ ] **v4 · Campagne-cap**: Received Email waarvan Flow niet gezet is, minstens 3 keer in 7 dagen. Uitsluiten bij elke campagne.

Rapportage (mag later): v4 · Heeft kookgerei, v4 · VIP, v4 · US. T01-cohorten kunnen niet op `v3_arm` (wordt niet gezet); gebruik per flow "Received Email waarvan $flow = <v4-flow> en Campaign Name bevat 'Old ·'" (oud pad) tegen "... bevat niet 'Old ·'" (nieuw pad), plus Placed Order in 7 dagen (welcome 14).

## Stap 4 · Templates exporteren (C)

- [ ] Wachten tot c4.html en c4-nocode.html (samengevoegde C4, andere agent) klaar zijn en in `exports/manifest.csv` staan. Kiezen: W4 als landsplit (w4-us, w4-int; standaard) of één `w4` (dan `--w4=template` in stap 6).
- [ ] `python3 -I scripts/export_klaviyo.py` (dry-run, moet alles "klaar" geven), daarna `--live --i-am-sure`. Logt in `exports/live/templates.csv`.
- [ ] `python3 -I scripts/build_flows.py` opnieuw: in `OVERZICHT.md` moet "0 templates ontbreken" staan. Nu ontbreken er 53 (lijst in OVERZICHT.md).

## Stap 5 · Oude checkout-draft weg (E, of C met DELETE na akkoord)

- [ ] Flow **Y6yj2z** ("v4 · Checkout abandonment", Draft, landsplit) verwijderen of hernoemen. Het script weigert de nieuwe checkout zolang die naam bestaat. Y6yj2z is nooit live geweest.

## Stap 6 · Flows aanmaken, alles Draft (C)

Vanuit /tmp, in deze volgorde (latere flows filteren op "Received Email where $flow = <ID van een eerdere v4-flow>", het script leest die ID's uit `exports/live/flows.csv`):

```
cd /tmp
S=/home/user/siraat-email-agent/scripts/build_flows.py
for f in postpurchase levering checkout cart welcome browse vip winback anniversary site sunset ugc; do
  python3 -I $S --live --only=$f || break
done
```

Welcome staat vóór browse (browse filtert op welcome-mails). Elke flow komt als Draft met alle mails op draft. Weigert Klaviyo iets:
- de A/B-actie (T04, T05a): opnieuw met `--ab=split` (50/50 random split, vervolg per tak gekopieerd);
- de wachttijd van 182/183 dagen (anniversary): opnieuw met `--max-delay=91`.

## Stap 7 · Nalopen en testen (E en C)

- [ ] Per flow de boom in Klaviyo naast `OVERZICHT.md` leggen: trigger, flowfilters, herinstap, splits, wachttijden "tot 09:00", afzender (W2, S2, V2: Benjamin at Siraat's Kitchen), reply-to support@, smart sending uit.
- [ ] Checkout, cart, browse, welcome: in de split "random 50%" bovenaan is JA = v4, NEE = oud pad (berichten "Old · ...", utm_campaign `old-<flow>`).
- [ ] Received Email-filters: tonen ze de juiste flow? Klik-split browse: werkt "Campaign Name bevat 'B1 · T05a'"?
- [ ] Testprofiel door elke tak (cart met pan, set, schort, plank, gift card; US en INT; nieuw en bestaand), preview met echt event, linkcheck incl. `/discount/`-redirect, coupon-preview (code verschijnt, overal dezelfde), GA4 DebugView. Testmails sturen kan C via de template-preview (create_template_preview_send_job) naar siraatskitchen@gmail.com.
- [ ] Coupons per codemail in de preview zien (stap 2 moet klaar zijn).

## Stap 8 · Failure to launch T2SmtR (E, vóór groep A)

Plan: T2SmtR blijft tot 20 november alleen voor het oude welcome-pad. `v3_arm` bestaat niet (update-profile kan niet via de API). Oplossing: in T2SmtR, in de bestaande split na de 30 dagen wachten, een voorwaarde toevoegen: **Received Email waarvan Campaign Name "Old · Welcome" bevat, minstens 1 keer in de laatste 60 dagen** (alleen dan door naar de mails). Niet als flowfilter: die wordt bij de instap gecontroleerd, vóór Old · Welcome 1 verstuurd is. Zonder deze stap krijgt ook het nieuwe pad de FTL-mails en is T01 in welcome vervuild.

## Stap 9 · Live zetten, per groep in één moment (E)

Per v4-flow: alle mails op Live (Klaviyo: flow openen, "Update all actions" > Live) en de flow op Live. **In dezelfde minuut** de oude flows op Draft (niet archiveren, PLAYBOOK §7). C kan de flowstatus met `PATCH /api/flows/<id>` omzetten, maar de mails moeten ook op Live; dat gaat het veiligst in de UI.

| Groep | v4-flows live | Oude flows naar Draft |
| --- | --- | --- |
| A | Checkout, Cart, Browse, Welcome | **Y2TmNB** (checkout), **Tsg2tV** (checkout Triple Pixel), **SwkMyn** (cart), **TBWngE** (cart Triple Pixel), **Wj6x6V** (browse), **TyEjuQ** (browse Triple Pixel), **SiaNLu** (welcome). T2SmtR blijft live met de filter uit stap 8. |
| B | Post-purchase, Post-purchase · levering, Winback | **RL3TU6** (post-purchase), **UEfh4h** (winback) |
| C | Sunset, Site abandonment, VIP, Anniversary, UGC first egg (alleen na de Gorgias-macro) | **S7V4a7** (sunset). UEqeEm (oud site-draft) blijft Draft. |

Groep A en B mogen tegelijk. Blijven ongewijzigd live: XzHrez (review), WsQDYu, WvRupU, UYALJ8, TSUnLs, YyaMjx, YcXbHx, Wn2tsq, SxN86d, TLHht3, UcGzaL, Y4a7fJ. Vixr6X gaat zoals gepland op 12 oktober uit.

## Stap 10 · Na livegang (C)

- [ ] Na 1 uur en na 24 uur: instroom per flow, verzonden per bericht, geen mails uit oude flows meer (behalve T2SmtR), uitschrijving per mail (browse extra volgen, 3.4).
- [ ] LOG.md bijwerken met de flow-ID's (staan in `exports/live/flows.csv`).

## BFCM-bevriezing 20 november t/m 6 december (E)

- [ ] 20 nov: in checkout, cart, browse en welcome de bovenste split "random 50%" naar **100%** (iedereen v4). T2SmtR op Draft.
- [ ] 20 nov: elke T02-split (de "random 50%" direct onder de cooldown-split) naar **100%** = iedereen zonder cooldown krijgt de code. V1 en N2 hebben nu al geen T02.
- [ ] T04 (W1) mag doorlopen, apart rapporteren.
- [ ] 7 dec: T02-splits terug naar 50%. V1 en N2 in T02 opnemen: script met `--t02-new` (nieuwe flow) of in de UI een random-split toevoegen.

## Wat via de API niet kon (en hoe het nu werkt)

- **Update profile property** (v3_arm, last_flow_code_at, siraat_regular, sunset_status): weggelaten. Cooldown via berichtnamen "CODE · ..." (Received Email, Campaign Name bevat "CODE ·", 30 dagen). T01-arm leesbaar aan "Old · ..."-berichtnamen. Sunset-suppressie via het segment uit stap 3.
- **Samenkomende takken**: niet toegestaan, dus categorie-routing als verzendfilter op de mail (per stap komt hoogstens één mail door) en een gedeeld vervolg per tak gekopieerd.
- **Trigger split op Items**: niet gebruikt (vorm niet bewezen); dezelfde keuze via profiel-metric-filters op het event in de laatste N dagen.
- **"Can receive email marketing"** als filter: weggelaten; marketingmails gaan nooit naar uitgeschreven profielen.
