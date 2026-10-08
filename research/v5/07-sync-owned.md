# 07 · `siraat_owned`: wat een klant al bezit (nachtelijke sync)

Stand 8 oktober 2026. Besluit Floris 8 okt (DECISIONS.md): het script mag, moet dagelijks draaien en gecontroleerd worden. Script: `scripts/sync_owned.py`. Achtergrond: `02-bundels-korting-klanten.md`, sectie 3.

## 1. Wat het doet

1. Leest uit Klaviyo de Shopify-events **Placed Order** (RSNxYV), **Cancelled Order** (TFervq) en **Refunded Order** (Xg6cwn). Placed Order bevat per regel handle, titel, variant en `line_item_id`; dat is preciezer dan Ordered Product (XT7f8Z, geen handle).
2. Zet elke orderregel om naar vaste sleutels (functie `classify`). Bundels worden uitgepakt naar hun inhoud volgens `content/catalog/products.json` ("whats_in_the_box").
3. Sluit uit: testorders, geannuleerde orders, volledig terugbetaalde orders, en per regel wat in een deelrefund is teruggegeven.
4. Schrijft per profiel alleen deze vijf velden (geen consent, niets anders):

| Veld | Type | Voorbeeld |
|---|---|---|
| `siraat_owned` | lijst | `["lid","lid_28","panpro","panpro_standard","sheets"]` |
| `siraat_owned_cats` | lijst | `["accessory","pan"]` (pan, set, pot, accessory) |
| `siraat_first_order_at` | datum (ISO, UTC) | `2026-09-08T19:23:14+00:00` |
| `siraat_last_order_at` | datum (ISO, UTC) | idem |
| `siraat_orders` | getal | aantal geldige orders (niet test, niet geannuleerd, niet volledig terugbetaald) |

### Sleutels

- Pannen: `panpro_mini` (20 cm, 8″), `panpro_small` (26 cm, 10″, ook "Medium" in de Full Edition), `panpro_standard` (28 cm, 11″), `panpro_large` (30 cm, 12″), plus altijd de verzamelsleutel `panpro`. Oude niet-gehamerde pan: `pan_original`. Verder `deep`, `wok`, `crepe`, `roasting` (geen maat).
- Deksels: `lid_20`, `lid_26`, `lid_28`, `lid_30` (cm, zelfde maat als de pan) plus altijd `lid`. Pan "With Lid" geeft pan en deksel.
- Potten: `pot_2l`, `pot_3l`, `pot_75l`.
- Sets (bundelsleutel plus de inhoud): `set6` (Mini, Small, Large + 3 deksels), `set12` (set6 + 3 potten), `complete` (Standard, wok, deep, crêpe), `everything` (34-delig). Andere bundels (Duo, Pro Duo, 2+2, Kit, Cookware Set Pro, Full Edition, Cook & Prep, Pan + Utensils, Wok & Deep) krijgen alleen hun inhoud en categorie `set`.
- Accessoires: `utensils` (de hele set van 4) en per stuk `utensil_flipper`, `utensil_spatula`, `utensil_ladle`, `utensil_scooper`; `board`, `apron`, `mill`, `sheets`, `pizza` (pizza steel), `pizza_wheel`, `grill_press`, `trivet`, `mat`, `diatomite_mat`, `bottle`, `ice_cubes`, `straws`, `chopsticks`, `sharpener`, `tea_filter`, `tote`.
- Genegeerd: Mystery Gift (ook "Father's Day Mystery Gift"), E-Guide/E-Book, Free Shipping, Shipping Protection, Giveaway/Weekly Draw, E-Gift Card. **Wel** meegeteld: fysieke gratis items met een duidelijke inhoud (bv. "🎁 FREE Lid", "🎁 Titanium Utensil (100% off) / Spatula", "Birthday Sale Gift / Spatula"), want die heeft de klant echt.

## 2. Gebruik in een mail

Klaviyo-templates (Django-achtig) kunnen met `in` controleren of een lijst een waarde bevat. Gebruik de `lookup`-filter; die werkt ook als het veld ontbreekt (dan leeg, dus `in` is onwaar en `not in` is waar):

```
{% if 'wok' not in person|lookup:'siraat_owned' %}  ...wokkaart...  {% endif %}
{% if 'lid_28' in person|lookup:'siraat_owned' %}  "A second 28 cm lid?"  {% endif %}
{% if 'pan' in person|lookup:'siraat_owned_cats' %}  "Adding to your Siraat kitchen"  {% endif %}
{% if person|lookup:'siraat_orders' >= 2 %} ... {% endif %}
```

`person.siraat_owned` werkt ook (de naam heeft geen spaties), maar `lookup` is de vaste vorm in onze templates. Let op: `in` op een lijst is een exacte match. Gebruik dus de verzamelsleutels `panpro` en `lid` voor "heeft een Pan Pro / een deksel", niet `'pan' in ...` op `siraat_owned` (dat is alleen goed op `siraat_owned_cats`). Test in de preview met een profiel dat de velden heeft; Klaviyo toont bij een onbekend profiel lege velden.

In segmenten en flowfilters: "Properties about someone" > `siraat_owned` > *contains* > `wok`. `siraat_orders` is een getal, de twee datums worden als datum herkend.

## 3. Draaien

Altijd vanuit `/tmp` met `python3 -I`. Standaard is dry-run (alleen tellen, 20 voorbeelden, niets schrijven).

```
python3 -I scripts/sync_owned.py                      # dry-run, incrementeel (eerste keer: volledige historie)
python3 -I scripts/sync_owned.py --since=2026-09-08   # dry-run vanaf een datum
python3 -I scripts/sync_owned.py --live               # schrijven (bulk import), cursor en ledger bijwerken
python3 -I scripts/sync_owned.py --live --limit=50    # proef, met GET-controle per profiel
python3 -I scripts/sync_owned.py --check              # exit 1 + WAARSCHUWING als de laatste geslaagde run > 36 uur oud is
```

Staat: `exports/live/sync_owned_state.json` (cursor = laatste Placed Order-tijdstip, laatste 30 runs, `last_success_at`) en `exports/live/sync_owned_ledger.json.gz` (per order: profiel, datum, sleutels per regel, status). De ledger bevat profiel-ID's en staat daarom in `.gitignore`; pad aan te passen met `SYNC_OWNED_LEDGER`. Een incrementele run leest vanaf cursor min 48 uur (late events), ontdubbelt via order-ID en schrijft alleen de geraakte profielen, berekend over hun volledige historie in de ledger. Zonder ledger (bv. een verse checkout) haalt het script per geraakt profiel de volledige historie op (3 calls per profiel), dus de velden kloppen ook dan, alleen trager.

Alleen een live run zonder `--limit` en zonder `--since`, zonder fouten, zet de cursor en `last_success_at`. Schrijven: tot 100 profielen via `PATCH /api/profiles/{id}`, daarboven via `POST /api/profile-bulk-import-jobs` (5.000 per job, het script wacht op elke job en toont importfouten). Rate limits: bij 429 of 5xx wacht het script oplopend en probeert opnieuw.

## 4. Dagelijkse run en controle

- **Run:** elke nacht `--live`, rond 03:50 Amsterdam (na de dag, voor de ochtendflows). Daarna direct `--check`.
- **Controle:** `--check` (exitcode 1 en een regel `WAARSCHUWING sync_owned: ...` als de laatste geslaagde run ouder is dan 36 uur, of nooit). Draai het bij de start van elke sessie en na de nachtelijke run; bij een waarschuwing: `last_run` in de state lezen (errors, events, seconds) en handmatig `--live` draaien.
- **Steekproef wekelijks:** `--live --limit=20 --since=<7 dagen terug>` doet een GET-controle per profiel; en de dry-run toont "ONBEKENDE producttitels": nieuwe producten toevoegen aan `BUNDLES` of `SIMPLE` in het script.
- Waar het draait (Claude Routine, GitHub Action of eigen server) beslist de hoofdsessie. Buiten deze omgeving is `KLAVIYO_API_KEY` nodig met scopes `events:read`, `profiles:read`, `profiles:write`, en moet de state (en bij voorkeur de ledger) tussen runs bewaard blijven.

## 5. Beperkingen

- **Tot 24 uur vertraging.** De trigger-order van een flow zelf moet uit het event blijven komen (`event.Items`), niet uit `siraat_owned`.
- **Alleen Shopify-orders sinds de Klaviyo-koppeling** (eerste events oktober 2024; oktober 2024 bevat testorders, die worden overgeslagen). Oudere orders of verkoop buiten Shopify (Amazon, retail) ontbreken.
- **Cadeaus en doorverkoop:** wie voor een ander kocht, "bezit" het volgens het veld toch. Mystery Gifts zijn onbekend van inhoud en tellen niet mee.
- **Refunds:** volledige refund = order telt niet; deelrefund = alleen de terugbetaalde regels vervallen. Een refund zonder regels (bv. prijscorrectie, chargeback-alert) laat de producten staan. Retour zonder refund in Shopify ziet het script niet.
- **Maten:** wok, deep en crêpe zonder maat (de varianten zijn wisselend benoemd). Oude pannen van 24 cm worden `pan_original`. Een product zonder herkenbare maat krijgt alleen `panpro` of `lid`.
- **Samengevoegde profielen:** orders van een samengevoegd profiel blijven aan het oude profiel-ID hangen tot een nieuw event komt; schrijven naar een verdwenen ID geeft een importfout (staat in de output).
- Een profiel dat alles heeft teruggestuurd krijgt `siraat_owned = []` en `siraat_orders = 0`; de datums blijven dan staan van de vorige keer.

## 6. Stand 8 okt 2026

- Dry-run laatste 30 dagen (`--since=2026-09-08`): 5.208 Placed, 60 Cancelled, 116 Refunded; 5.056 profielen geraakt; 112 profielen zonder sleutel (alleen gifts of alles terug); 2 onbekende titels ("12pcs cookware set"), daarna toegevoegd. Duur 73 s.
- Proef live `--live --limit=50 --since=2026-09-08 --bulk`: 50 profielen met volledige historie, één bulk job (50/50, 0 fouten), GET-controle 0 afwijkingen. Cursor niet gezet (proef).
- Volledige historie **nog niet live gedraaid** (beslissing hoofdsessie). Schatting: ca. 109.000 Placed Order-events (2024: 1,5k, 2025: 41k, 2026: 67k) = ca. 550 pagina's van 200 à 1,5 tot 3,5 s = 15 tot 30 min ophalen; daarna ca. 80.000 tot 100.000 profielen in 16 tot 20 bulk jobs (5.000 per job), enkele minuten per job. Totaal naar schatting 45 tot 75 minuten, één keer. Daarna dagelijks een paar honderd orders: minder dan een minuut.
