# Tegoed-systeem: "You have $12 in your account"

Voor: Floris. Van: flow builder, 8 nov 2026. Klaviyo-account TdtTzz.
Status: ontwerp plus DRAFT in Klaviyo. Niets live, geen coupon of Shopify-korting gemaakt, geen bestaande flow aangeraakt.

| Wat | ID |
|---|---|
| Flow | **Ubi9m5** `v4 · Tegoed ($12 in your account) · DRAFT` (status draft, alle 4 mails draft) |
| Trigger (placeholder) | lijst **TvEQxz** `Tegoed uitgegeven` (nieuw, leeg) |
| Templates (bibliotheek) | T1 **VaRdvM**, T2 **V6dXap**, T3 **W6nhmt**, T4 **Xb9RTV** (flowkopieën: X98RKq, Ww7P8M, U6ESZF, X4vBq2) |
| Bron | `klaviyo/templates/v3/tegoed/t1..t4.html` (generator `_tools/make_tegoed.py`, render `_tools/render_tegoed.py`, screenshots `previews/`, flowscript `_tools/build_flow_tegoed.py`) |
| Coupon (placeholder) | `{% coupon_code 'SIRAAT_CREDIT_12' %}` in T1. **Bestaat nog niet**: Floris maakt hem aan. |

Het tegoed is een gewone unieke kortingscode, geen Rise.ai. Eerlijk betekent hier: de klant heeft echt een code van $12, die echt vervalt op de datum in de mail. Nooit "we added yesterday", "extended", "support team just checked" of een tweede verlenging.

---

## 1. Wie krijgt tegoed, en wanneer

Wat er nu al met kopers gebeurt (gelezen, niet aangepast): Post-purchase X3ySuU (Placed Order: P1 na 1 uur, P2 dag 17, P3 dag 21 met unieke code in de CODE-armen) en Winback UyFc78 (Placed Order: R1 dag 45, R2 dag 75 met code). Na dag 75 krijgt een koper geen flowmail meer, alleen campagnes.

| | Trigger | Geldig | Voor | Tegen |
|---|---|---|---|---|
| **a) Bedankt-tegoed na eerste bezorgde order** | Delivered Shipment (VcUF33), eerste order, + 5 dagen | 30 dagen | Klant is net tevreden, kent het product; tweede aankoop is de grootste hefboom | Botst met P3-code (dag 21) en reviewverzoek (bezorging + 14 dagen). Drie codes in 75 dagen. Hoogste kannibalisatie: veel van deze klanten kopen toch al |
| **b) Winback-tegoed na 120 dagen zonder order** | Lijst `Tegoed uitgegeven`, gevuld uit segment "laatste order 120 tot 127 dagen geleden" | 30 dagen | Begint waar UyFc78 ophoudt (dag 75), dus geen overlap met flowcodes. "In your account" past bij iemand die al klant is. Lage basiskans, dus weinig weggegeven aan wie toch al kocht | Lagere respons dan a |
| **c) Beloning voor review of verwijzing** | Review ingediend (Trustpilot stuurt geen events, dus nu niet te triggeren) of Snowball-verkoop | 60 dagen | Voelt het meest verdiend | Trustpilot-incentive is al een risico (DECISIONS 7 okt); Snowball heeft al 15% commissie. Geen trigger beschikbaar |

**Advies: begin met b (120 dagen zonder order).** Hij vult een gat in plaats van een derde code naast P3 en R2 te leggen, de holdout meet zuiver, en de boodschap is waar zonder uitleg ("you ordered from Siraat before, so I made you a $12 code"). a kan daarna als test tegen P3, c pas als er een review-event is.

Cohort voor de start: US (`person.Country` US of leeg), want de copy zegt $12 en een vaste Shopify-korting wordt buiten de US omgerekend. Uitsluiten: refund of annulering in de laatste order, open Gorgias-ticket in 14 dagen, wie al in de flow zat (filter staat).

Vullen van de lijst: wekelijks (bijv. maandag) de nieuwe instromers uit het 120-127-dagen-segment toevoegen. Dat kan Floris handmatig of een klein script (`POST /api/lists/TvEQxz/relationships/profiles`). Later desgewenst een segment-trigger in de UI in plaats van de lijst.

## 2. Bedrag en marge

$12 vast, één keer per klant, voorstel minimum besteding $50 (beschermt losse accessoires zoals vaatwasstrips; Floris kiest).

Rekenvoorbeeld bij 60% brutomarge (aanname uit `research/giftcard/02-bedrag-of-korting.md`, Floris bevestigt):
- Tweede pan van $144: marge $86. Met tegoed $74.
- Elke verzilvering kost $12, ook bij wie toch al zou kopen. Break-even als minstens 12 / 86 = **14% van de verzilverde orders echt extra** is (extra marge 74 per extra order tegen 12 weggegeven op de rest).
- Bij 120 dagen zonder order is de basiskans op een order binnen 30 dagen laag, dus de kans dat we boven 14% komen is goed. Bij trigger a is dat juist het risico.
- In de Black Friday-sale (tot 70% korting) is de marge per order veel lager en eet $12 een groter deel op. Zie 6.

## 3. Mechanisme in Klaviyo

### 3.1 De code
- Klaviyo-coupon `SIRAAT_CREDIT_12` (Shopify-gekoppeld, unieke codes): vast bedrag $12, één gebruik per klant, eventueel minimum $50.
- Vervaltijd: **"29 dagen na aanmaak"**. Klaviyo telt bij dagen-vervaldatum 24 uur marge erbij, dus de code werkt in werkelijkheid 30 dagen na aanmaak (aanpak-urgentie-flows.md 2.2). Controleer dit één keer met een testprofiel.
- De code wordt gemaakt in T1 (`{% coupon_code 'SIRAAT_CREDIT_12' %}`, ook in de knoplink; binnen één mail hergebruikt Klaviyo dezelfde code).

### 3.2 Waarom T2 tot T4 géén coupon-tag hebben
Elke mail met een coupon-tag maakt een **nieuwe** code met een **nieuwe** vervaldatum. Dan zou de herinnering een andere code tonen en klopt "expires in 3 days" niet. Daarom:
- Bij uitgifte vuurt Klaviyo **Coupon Assigned** (XUMYt7) met `UniqueCode` en `CouponExpirationDate`.
- Een kleine hulpflow (door Floris te maken, trigger Coupon Assigned, triggerfilter `CouponKey = SIRAAT_CREDIT_12`) schrijft met een **webhook-actie** naar `https://a.klaviyo.com/api/profile-import` drie profieleigenschappen:
  - `siraat_credit_code` = `{{ event.UniqueCode }}`
  - `siraat_credit_value` = `12`
  - `siraat_credit_expires_at` = `{{ event.CouponExpirationDate }}` (formaat `YYYY-MM-DDTHH:MM:SS`, UTC)
  - Header met een private key die alleen `profiles:write` mag (geen volledige sleutel in een webhook).
- T2, T3 en T4 tonen `{{ person.siraat_credit_code }}` en `{{ person.siraat_credit_expires_at|format_date_string|date:'l, F j' }}`. Een split vóór T2 laat alleen profielen door waar `siraat_credit_code` gezet is; zonder code geen herinnering (liever niets dan een verkeerde datum).
- Deze eigenschappen kunnen ook campagnes gebruiken ("You have $12 in your account" in een blok, alleen als `siraat_credit_expires_at` in de toekomst ligt).

Alternatief (optie B, later): een script maakt de code zelf in Shopify met `ends_at` 23:59 ET op dag 30, schrijft de drie eigenschappen en zet het profiel op de lijst. Dan kan T1 ook de profielwaarden gebruiken en mag T4 echt "tonight" zeggen.

### 3.3 Waarom de datums kloppen
Alle mails gaan om 09:00 lokale tijd. De code ontstaat bij T1 (dag 0, 09:00) of tot ongeveer 10 uur eerder (Klaviyo maakt codes in batches). Werkelijke einde dus tussen dag 29 23:00 en dag 30 09:00.
- T1 toont "Expires: vandaag + 29 dagen" (via `{% today %}|days_later:29`). Conservatief: de code werkt zeker tot het eind van die dag. T1 kan de echte tijd niet tonen, omdat de code in dezelfde mail ontstaat.
- T3 op dag 27: nog 2,6 tot 3 dagen. "Expires in 3 days" klopt.
- T4 op dag 29: nog 14 tot 24 uur. Onderwerp "Last day for your $12", tekst "less than 24 hours". **Niet "tonight"**: het einde ligt tussen 23:00 en 09:00, dus "tonight" is niet altijd waar. Wil Floris "Your $12 expires tonight", dan optie B (vast einde 23:59 ET).
- T2 tot T4 tonen de echte datum van het profiel. Die kan een dag later zijn dan T1 noemde (nooit eerder). Dat is eerlijk, maar check in de test of de datum in UTC of profieltijd rendert.

## 4. Flowopbouw (zoals gebouwd in Ubi9m5)

| Stap | Wanneer | Inhoud | Smart Sending |
|---|---|---|---|
| Holdout-split | instap | 10% (`profile-sample`) stopt hier: geen code, geen mail | |
| T1 | dag 0, 09:00 | "You have $12 in your account": korte Benjamin-brief, kaart Account / Credit / Expires / Code, knop "Use my $12" (code al toegepast via `/discount/CODE`) | aan |
| Split | dag 14 | alleen door als `siraat_credit_code` gezet is | |
| T2 | dag 14, 09:00 | "Your $12 is still in your account": zelfde code, zelfde datum, Tammy-review (R138, letterlijk) | aan |
| T3 | dag 27, 09:00 | "Your $12 expires in 3 days" | uit (echte deadline) |
| T4 | dag 29, 09:00 | "Last day for your $12": laatste mail, twee beloftes (30-day returns, beschadigd of defect: vervangen of terugbetalen), 75-year warranty | uit |

Uitstap: flowfilter (bij elke stap opnieuw gecontroleerd) **Placed Order sinds flowstart = 0**, **Coupon Used met CouponKey = SIRAAT_CREDIT_12 sinds flowstart = 0**, en **nooit eerder in deze flow** (één tegoed per klant, ooit). Wie bestelt, valt direct uit de flow.

Mails: vaste header en footer uit `partials/` (lockup monogram + SIRAAT), afzender "Benjamin from Siraat", geen geel, geen gedachtestreepjes, geen BF-code, friction reducer "One use, already applied. 30-day returns. 100,000+ happy customers." Elke mail heeft vijf onderwerpregels in de bronkop. Kleine regel onderaan: één code per klant, één order, niet in te wisselen voor geld, vervalt na de getoonde datum, en waarom de klant hem krijgt.

Over "in your account": de code hoort bij het e-mailadres in de mail, niet bij een saldo in het Shopify-klantaccount. Floris koos dit formaat; wie het letterlijk wil, kan later Shopify-store credit gebruiken. Veilige B-onderwerpregel staat klaar ("$12 for your next order, from Benjamin").

## 5. Overlap met andere flows

- **Winback UyFc78**: eindigt op dag 75 (R2). Bij trigger b start het tegoed op dag 120, dus geen overlap. Toch voorstel: bij het vullen van de lijst uitsluiten wie in de laatste 14 dagen een mail uit UyFc78 kreeg.
- **Post-purchase X3ySuU**: start opnieuw bij een nieuwe order; wie bestelt, valt al uit het tegoed. Geen overlap.
- **Sunset TbYQmX** (120 dagen niet actief): kan dezelfde mensen raken. Voorstel: wie in Sunset zit, eerst het tegoed geven en Sunset 30 dagen later laten starten, of Sunset-profielen uitsluiten bij het vullen. Floris kiest.
- **Campagnes**: T1 en T2 met Smart Sending aan (geen duw op een drukke campagnedag), T3 en T4 uit, want die horen bij een echte datum.

## 6. Stapelen met de sale (besluit Floris)

DECISIONS 19 okt staat HI10 en flowcodes toe op de sale. Voor het tegoed drie opties:
1. **Stapelt wel** (combineren met productkortingen aan in Shopify). Sterkst voor conversie, laagste marge. Copy mag dan "It works on sale prices too."
2. **Stapelt niet**: dan moet de mail dat zeggen, anders voelt het als een truc in de kassa.
3. **Starten na BFCM** (advies): eerste lijstvulling op 1 december, of in januari. Dan meet de holdout schoon, botst het niet met de 70%-sale en is er in december een echte reden ("for the new year in your kitchen").

De huidige copy zegt niets over stapelen; die regel gaat erin zodra Floris kiest.

## 7. Meten

- 10% holdout via de split bij instap. Holdout = profielen op de lijst die T1 niet kregen.
- Hoofdmaat: orders en omzet per profiel binnen 35 dagen na instap, tegoedgroep tegen holdout (incrementeel, niet de verzilverde orders).
- Plus: verzilveringsgraad (Coupon Used), marge na tegoed, uitschrijvingen per mail.
- Beslissen na minstens 4 cohorten of 1.500 profielen in de tegoedgroep. Doorgaan als de extra marge per profiel positief is (break-even in 2).

## 8. Wat Floris moet doen vóór livegang

1. **Coupon** `SIRAAT_CREDIT_12` in Klaviyo (Shopify, unieke codes): $12 vast, 1x per klant, vervalt 29 dagen na aanmaak, minimum besteding kiezen, stapelen kiezen. Heet hij anders, dan de tagnaam in T1 (twee plekken) en het CouponKey-filter in de flow aanpassen.
2. **Hulpflow Coupon Assigned → webhook** die de drie profieleigenschappen schrijft (3.2), met een sleutel die alleen profielen mag schrijven. Daarna één testprofiel door de hele flow sturen en de datum in T2 tot T4 controleren.
3. **Trigger kiezen**: advies b. Segment "laatste order 120 tot 127 dagen geleden, US" maken en wekelijks naar lijst TvEQxz, of de lijst vervangen door een segment-trigger in de UI.
4. **Besluiten**: stapelen met de sale (6), startmoment (advies 1 december of later), Sunset-overlap (5), minimum besteding.
5. **Testmails** van T1 tot T4 bekijken (PLAYBOOK: livegang pas na ontvangen testmails), dan zelf de flow en de mails op live zetten. Claude zet niets live.
