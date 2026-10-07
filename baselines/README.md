# Baselines e-mailprestaties Siraat's Kitchen

**Snapshotdatum:** 7 oktober 2026. Alleen gelezen uit Klaviyo (Reporting API, Metric Aggregates API, REST revision 2025-10-15). Account-tijdzone US/Eastern, valuta USD. Conversiemetric: Placed Order (Shopify, `RSNxYV`), Klaviyo-standaard attributievenster.

Doel: elke herbouwde flow en elke nieuwe campagne meten tegen deze "voor"-situatie.

## Bestanden

| Bestand | Inhoud |
|---|---|
| `flows-30d.csv` | Per live flow, Klaviyo-timeframe `last_30_days` (7 sep t/m 6 okt 2026) |
| `flows-90d.csv` | Per live flow, `last_90_days` (9 jul t/m 6 okt 2026) |
| `flow-messages-90d.csv` | Per flow-e-mail binnen live flows, `last_90_days`, met berichtnaam en onderwerpregel |
| `campaigns-90d.csv` | Per e-mailcampagne verzonden in `last_90_days` (87 campagnes; SMS uitgesloten), met classificatie |
| `account-weekly.csv` | 13 volledige weken (ma t/m zo, ET), week van 6 jul t/m week van 28 sep 2026 |
| `README.md` | Dit document |

## Kopcijfers om te verslaan

Bron per cijfer: **[K]** = direct door Klaviyo gerapporteerd; **[B]** = door ons berekend uit Klaviyo-data (formule erbij).

| # | Baseline | 90 dagen | 30 dagen | Hoe |
|---|---|---|---|---|
| 1 | Flow-omzetaandeel van totale omzet | **10.8%** ($416,090 / $3,865,201) | 10.5% ($115,961 / $1,101,999) | [B] som `conversion_value` live flows (flow report) / som Placed Order value (metric aggregates, zelfde dagen) |
| 2 | Omzet per ontvanger: Welcome (SiaNLu) | **$0.696** ($147,013 / 211,126 delivered) | $0.515 | [B] som conversion_value / som delivered van de flows in de groep (Klaviyo-definitie RPR = waarde / delivered) |
| 3 | Omzet per ontvanger: Checkout abandonment (Tsg2tV + Y2TmNB) | **$2.359** ($64,291 / 27,249 delivered) | $2.082 | [B] som conversion_value / som delivered van de flows in de groep (Klaviyo-definitie RPR = waarde / delivered) |
| 4 | Omzet per ontvanger: Cart abandonment (SwkMyn + TBWngE) | **$1.472** ($49,267 / 33,472 delivered) | $1.767 | [B] som conversion_value / som delivered van de flows in de groep (Klaviyo-definitie RPR = waarde / delivered) |
| 5 | Omzet per ontvanger: Browse abandonment (TyEjuQ + Wj6x6V) | **$0.968** ($74,859 / 77,326 delivered) | $0.864 | [B] som conversion_value / som delivered van de flows in de groep (Klaviyo-definitie RPR = waarde / delivered) |
| 6 | Omzet per ontvanger: Post-purchase (RL3TU6) | **$0.309** ($20,550 / 66,527 delivered) | $0.190 | [B] som conversion_value / som delivered van de flows in de groep (Klaviyo-definitie RPR = waarde / delivered) |
| 7 | Omzet per ontvanger: Winback (UEfh4h) | **$0.198** ($9,459 / 47,842 delivered) | $0.136 | [B] som conversion_value / som delivered van de flows in de groep (Klaviyo-definitie RPR = waarde / delivered) |
| 8 | Welcome-omzet per nieuwe abonnee | **$2.53** ($147,013 / 58,097) | $1.95 ($36,066 / 18,458) | [B] conversion_value Welcome-flow / aantal 'Subscribed to List' events voor Email List `Uw8eZG` in hetzelfde venster |
| 9 | Checkout-herstelratio | **0.97%** (252 orders / 26,049 starters) | 0.70% (62 / 8,872) | [B] attributed orders (`conversions`) uit beide checkout-flows / som van dagelijkse unieke 'Checkout Started' (Shopify, `RfMvni`) |
| 10 | Campagne-omzet per ontvanger: image-only | **$0.080** (74 campagnes, $234,956) | n.v.t. | [B] som conversion_value / som delivered per klasse |
| 11 | Campagne-omzet per ontvanger: tekst/founder note | **$0.118** (13 campagnes, $70,458) | n.v.t. | idem |
| 12 | Unsubscribe-ratio alle e-mail (flows + campagnes) | **0.54%** | n.v.t. | [B] som unsubscribe_uniques / som delivered (flows 0.94%, campagnes 0.44%) |
| 13 | Spamklachtratio alle e-mail | **0.042%** | n.v.t. | [B] som spam_complaints / som delivered (flows 0.076%, campagnes 0.033%) |

### Context

- Totale e-mail-geattribueerde omzet 90d (metric aggregates, `$attributed_channel` = email): $721,410 = 18.7% van de totale omzet. Flows $418,569 (10.8%) en campagnes in het campagnerapport $305,413.
- Campagnes 90d totaal: 87 e-mailcampagnes, 3,550,566 delivered, open rate 39.9%, click rate 0.62%, omzet per ontvanger $0.086.
- Flows 90d totaal (live): 922,239 delivered, omzet per ontvanger $0.451, bounce 0.52%.
- Tekst/founder-campagnes: open 39.8%, click 0.81%, conversie 0.055%; image-only: open 40.0%, click 0.58%, conversie 0.036%.

## Definities

- **Vensters.** `last_30_days` en `last_90_days` zijn Klaviyo-reporttimeframes: de 30/90 volledige dagen tot en met gisteren in account-tijdzone (dus 7 sep t/m 6 okt en 9 jul t/m 6 okt 2026). Account-aggregaten voor de kopcijfers zijn dagelijks opgehaald over exact die dagen. De weekbestanden gebruiken kalenderweken maandag t/m zondag (ET); de lopende week van 5 okt is weggelaten.
- **Live flows.** Flows met status `live` op 7 okt 2026 (24 flows, waaronder transactionele CS-notificaties en lead-magnetflows). Flows met een andere status zijn uitgesloten; in deze vensters had geen enkele niet-live flow verzendingen. Kanaal: alle rapportregels waren e-mail.
- **recipients / delivered.** Klaviyo: ontvangers en afgeleverde e-mails (recipients minus bounces).
- **open_rate, click_rate, conversion_rate, unsubscribe_rate, spam_complaint_rate.** Unieke opens / clicks / converters / afmeldingen en spamklachten gedeeld door delivered. **bounce_rate** = bounced / recipients. Open rates zijn opgeblazen door Apple Mail Privacy Protection; gebruik click rate en omzet per ontvanger als primaire vergelijking.
- **conversion_uniques** = unieke profielen met een geattribueerde Placed Order; **conversions** (extra kolom) = aantal geattribueerde orders; **conversion_value** = geattribueerde orderwaarde in USD.
- **revenue_per_recipient** = conversion_value / delivered (geverifieerd tegen Klaviyo's eigen waarde). Per flow en per categorie herberekend als som waarde / som delivered over de berichten; per bericht is het Klaviyo's eigen cijfer.
- **Flowcategorieen** (kolom `category`): welcome = SiaNLu; checkout = Tsg2tV + Y2TmNB; cart = SwkMyn + TBWngE; browse = TyEjuQ + Wj6x6V; post-purchase = RL3TU6; winback = UEfh4h; overige flows = `other`.
- **Campagneclassificatie.** Op naam: bevat `Founder`, `Note`, `Benjamin`, `Plain Text` of `Text Based` (hoofdletterongevoelig) = `text/founder note`, anders `image-only`. Let op: `image-only` betekent hier "geen tekstmarker in de naam", niet geverifieerd op template-inhoud. Twijfelgevallen zoals "09/05 September is hard" (persoonlijke onderwerpregel) staan als image-only. Campagnes met meerdere edities (per land) zijn aparte regels.
- **Campagnevenster.** Klaviyo `last_90_days` campaign values report; send_date in UTC.
- **account-weekly.csv.** `placed_order_*` = alle Shopify-orders. `email_attributed_*` = orders met `$attributed_channel` = email. `flow_attributed_*_all_channels` = orders met een `$attributed_flow` (vrijwel volledig e-mail; SMS-flows apart nihil). `campaign_email_attributed_value_est` = email-attributed min flow-attributed (schatting). `checkout_started_unique` en `added_to_cart_unique` = unieke profielen per week (Shopify-metrics `RfMvni`, `QXcV8K`; Triple Pixel-varianten niet gebruikt). `subscribed_email_list_Uw8eZG` = aantal 'Subscribed to List' events voor Email List. `unsubscribed_email_marketing_unique` = metric 'Unsubscribed from Email Marketing' (`YcWddQ`). `marked_spam_unique` = 'Marked Email as Spam' (`VQMAAk`).
- **Checkout-herstelratio.** Noemer = alle checkout-starters (ook wie direct kocht), opgeteld als som van dagelijkse unieke starters, dus een persoon die op twee dagen start telt twee keer. Teller = orders toegeschreven aan de twee checkout-flows. Dit is een herstelratio op alle starters, niet op alleen de flow-instromers.
- **Welcome per nieuwe abonnee.** Noemer = 'Subscribed to List' events op Email List in het venster; welcome-omzet kan ook komen van abonnees die voor het venster instroomden, dus dit is een stroomverhouding, geen cohortcijfer.
- **Attributie.** Klaviyo-attributie (last touch binnen het accountvenster). Flowrapport-omzet en metric-aggregate-omzet verschillen licht (90d: $416,090 vs $418,569) door verschil in datering (rapport op verzenddatum vs order op orderdatum).

## Herhalen

Draai dezelfde rapporten (flow-values-reports, campaign-values-reports met `conversion_metric_id` RSNxYV; metric-aggregates met `timezone` US/Eastern) en vergelijk per flow-id en flow-message-id. Vergelijk een herbouwde flow alleen met een venster van gelijke lengte en bij voorkeur zonder grote saleperiodes (augustus jubileumsale, september Labor Day/Warehouse Clearance en oktober Prime Sale vallen in deze baseline).
