# Livegang v4-flowmails in Klaviyo (account TdtTzz)

Stand 7 oktober 2026. Alles staat klaar om te exporteren, er is **niets** naar Klaviyo gestuurd. Bindend plan: `klaviyo/flows/v4-flow-system.md`. Per mail onderwerp, preview, beelden en status: `manifest.csv`. Proefbouw van elke Klaviyo-HTML (met placeholder-URL's voor beelden die nog niet geüpload zijn): `dry-run/<flow>/<id>.html`.

Uitkomst dry-run: **61 mails, 61 klaar, 0 blokkades**. 101 unieke beelden moeten nog naar de Klaviyo-bibliotheek (hero's, productbeelden, GIF's, certificaat); de gedeelde beelden (`partials/shared`) en logo's staan er al.

## 0. Eerst beslissen (Floris, OVERZICHT-FLORIS.md)

Zonder deze antwoorden niet live zetten:

| Nr | Vraag | Waarom het de livegang raakt |
| --- | --- | --- |
| 1, 2 | Lekkende publieke codes dicht (BFEXTRA10, NYEXTRA10, 100%-codes enz.) | Voorwaarde voor test T02 (unieke code tegen geen code) |
| 24 | Regels en "No purchase necessary" voor de PFAS-filtertrekking | Bijna elke verkoopmail noemt "chance to win" |
| 39 | Akkoord op de AI-flitsbeelden | 18 hero's (16 verschillende beelden) zijn AI-flitsbeelden (hero-registers) |
| 41 tot 46 | Timing C1/K1 30 min, C2/K2 09:00, HI10 in vroege mails, geen HI10-tak, BDAY-listing $349, verzendmail | Bepalen de flowinstellingen in stap 6 |
| 6 | Marge per pan en set | Breakeven van de 10/15%-codes (v4 3.14) |
| 22, 23 | Garantie bij deuken, en op schort en molen | N1 en K3 beloven dit |
| 33 | E-book-link (`/products/e` of gratis variant) | P1-first |
| 36 | UGC: 15% voor een foto | Flow UGC first egg |
| 38 | Roasting Pan-pagina zonder "Lifetime" en "100-day" | Kaart met NEW-sticker linkt erheen |
| 30 | Leest Benjamin de replies? | W2, S2, V2 als "Benjamin at Siraat's Kitchen" |

Plus de voorwaarden uit v4 4.1: reply-to support@siraatskitchen.com in Gorgias bevestigd, Gorgias-macro en tag `ugc-photo`.

## 1. API-key

De huidige key heeft `templates:read` (PLAYBOOK 9). Voor stap 5 is een key nodig met **images:write** en **templates:write** (flows full blijft nodig voor stap 6). Het script gebruikt de proxy-credential van de sessie, of `KLAVIYO_API_KEY` als die gezet is.

## 2. Coupons (Klaviyo UI: Coupons, Shopify, unique codes)

Elke pool: unieke codes, 1 gebruik, 1 per klant, alleen one-time purchase products, vervalt na toewijzing, geen einddatum op de pool. Namen exact zoals in de templates (het script controleert ze).

| Pool | Prefix | Korting | Vervalt na | Mails |
| --- | --- | --- | --- | --- |
| C4_10_48H | CO- | 10% | 48 uur | c4-us, c4-int |
| K3_10_48H | CART- | 10% | 48 uur | k3 |
| B2_10_48H | VIEW- | 10% | 48 uur | b2-clicked |
| P3_THANKYOU_10_14D | THX- | 10% | 14 dagen | p3-pan, p3-set, p3-next, p3-apron, p3-accessory |
| R2_10_72H | BACK- | 10% | 72 uur | r2 |
| R2_VIP_15_72H | VIP- | 15% | 72 uur | r2-vip |
| SK_REGULARS15_14D | REG- | 15% | 14 dagen | v1 |
| SK_ANNIV10_7D | YEAR- | 10% | 7 dagen | n2 |

UGC15 is een Shopify-bulkcode voor de Gorgias-macro, niet in Klaviyo.

## 3. Segmenten (v4 4.3)

`v4 · Sunset · unengaged 120d`, `v4 · Sunset · suppressed`, `v4 · Welcome-bescherming`, `v4 · Campagne-cap`, `v4 · Heeft kookgerei`, `v4 · VIP`, `v4 · US`, de 8 T01-cohortsegmenten (`v3_arm` new/old x checkout, cart, browse, welcome). Alleen als de Flow-dimensie in de Received Email-filter niet werkt: per flow "Mail uit flow X in 7 dagen".

## 4. Profieleigenschappen (v4 4.2)

`v3_arm`, `v3_arm_flow`, `v3_arm_at`, `last_flow_code_at`, `last_flow_code_pool`, `siraat_regular`, `sunset_status`, `sunset_at` (fase 2: `test_t03`). Ze ontstaan via "Update profile property" in de flows. Zet ze één keer op een testprofiel (siraatskitchen@gmail.com) zodat ze in de split-condities te kiezen zijn. Kan "Update profile property" geen datum van vandaag zetten: berichtnamen van codemails laten beginnen met `CODE ·` (terugval v4 1.4).

## 5. Beelden en templates

```
cd /home/user/siraat-email-agent
python3 -I scripts/export_klaviyo.py                       # dry-run: moet 61 klaar geven
python3 -I scripts/export_klaviyo.py --live --i-am-sure    # pas na stap 0 tot 4
```

`--live` doet per mail: alleen de beelden uploaden die de mail echt gebruikt en nog geen URL hebben (zelfde call als `upload_images.py`, naam `siraat-<map>-<bestand>`), de URL in `<map>/assets/klaviyo-urls.txt` of `partials/shared/klaviyo-urls.txt` schrijven, `<id>.klaviyo.html` naast de bron bouwen, opnieuw valideren en de template `v4 · <flow> · <id>` aanmaken (editor CODE). Bestaat die naam al, dan slaat hij hem over. Template-ID's komen in `exports/live/templates.csv`. Mails met een blokkade gaan niet mee. Na de run: dry-run opnieuw en `klaviyo-urls.txt` + `.klaviyo.html` committen.

Gecontroleerd per mail (dry-run en live): geen `{{IMG}}`, `{{SHARED}}`, `[[` of `{{BLOCK`, geen lokale paden, `{% if %}`/`{% for %}` in balans, coupon-pool bestaat, HTML onder 100 KB (grootste 35 KB), interne comments weg, onderwerp A en B max 50 en preview 40 tot 90 tekens (uit de topcomment), alt op elk beeld, UTM op elke siraatskitchen.com-link (header en footer krijgen `<mail>-logo`, `-nav-*`, `-ft-*`), geen gedachtestreepje.

## 6. Flows bouwen (v4 sectie 2, volgorde 4.6, alles eerst op Draft)

Groep A: Checkout, Cart, Browse, Welcome. Groep B: Post-purchase plus Post-purchase · levering, Winback. Groep C: Sunset, Site, VIP, UGC first egg, Anniversary.
Per flow: trigger, filters, splits en wachttijden exact uit sectie 2; template per bericht uit stap 5 (Klaviyo maakt bij koppelen een kopie); onderwerp A en preview uit `manifest.csv`; onderwerp B alleen bij T04 (w1-a/w1-b) en T05a (b1); afzender en reply-to volgens 1.3; smart sending uit; `add_tracking_params` aan met source, medium, campaign.

## 7. Testsends naar siraatskitchen@gmail.com

Per flow elke tak met een testprofiel (v4 4.7): cart met pan, set, schort, plank, gift card; US en INT; nieuw en bestaand. Controleer per mail: beelden laden van cdn.klaviyomail.com, code verschijnt en is overal dezelfde, `/discount/<code>`-links met UTM werken, preheader, afzender, reply-to, mobiel (Gmail-app) en Outlook.

## 8. Live en 50/50

Per groep in één moment: flows op Live, T01-split 50/50 (oud/nieuw) en T02-A/B 50/50 (code/geen code) zetten en in de editor op "Start test" klikken (de API kan dat niet). Oude flows uit tabel 4.6 tegelijk op Draft (niet archiveren). Eerste twee weken dagelijks uitschrijving per mail volgen (signaal boven 0,5%, probleem boven 1%).

## Beeldkwaliteit (retina-ronde 7 okt)

Elk beeld is minimaal 2x zijn weergavebreedte en is gemaakt zonder opschalen boven de bron. Gewicht: hero's 127 tot 286 KB, productkaarten onder 60 KB, GIF's 396 tot 664 KB, zwaarste mail W0 1,28 MB (twee GIF's), dan P2-safe 0,89 MB en P2 0,82 MB. Scripts: `scripts/make_chef_media.py` (GIF's en stills uit de chef-video, 1080p), `scripts/make_hero.py`.
