# 01 · De beste mails ooit: wat won, waarom, en wat terug moet in v4

Datum: 7 oktober 2026. Alleen gelezen uit Klaviyo (account TdtTzz, REST revision 2025-10-15, conversiemetric Placed Order RSNxYV, Klaviyo-attributie). Niets aangemaakt of gewijzigd, geen templates in de repo aangeraakt.

## Kort

- **Bereik.** Alle 384 e-mailcampagnes die de Reporting API kent (eerste verzending 22 januari 2025, laatste 6 oktober 2026): 9,61 mln delivered, $1,30 mln toegeschreven omzet. Alle 160 flowberichten met verzendingen sinds 8 oktober 2024 (live, draft en verwijderde flows): 3,02 mln delivered, $2,11 mln. Daarvan hebben 350 campagnes en 120 flowberichten minstens 1.000 ontvangers; alleen die tellen in de ranglijsten.
- **Grootste les campagnes.** Het verschil tussen campagnes komt vooral van publiek en moment (Black Friday, warehouse sale, kleine "highly engaged"-segmenten), niet van onderwerpformules. Na correctie voor de maand (RPR-index = RPR gedeeld door de mediaan van die maand) zijn de duidelijkste winnaars: **een nieuw product aan bestaande kopers** (deksels aan pankopers, index 6,9), **praktische kookhulp** ("Why Food Sticks", 7,18% klik, hoogste ooit), **tekstmails van de oprichter** (mediaan index 1,22, minder uitschrijving) en **een echte deadline of gift** (index 1,10 tot 1,15). Seizoensverhalen, vergelijkingen en algemene educatie verliezen (0,70 tot 0,92).
- **Grootste les flows.** Mail 1 doet het werk: checkout 1 ($2,17 tot $7,83 per ontvanger), welcome 1 ($2,73 op 199.479 ontvangers, $535.843, de best verdienende mail ooit), cart 1 ($2,43 tot $2,66). Op dezelfde positie wint **gift/bonus** van **merk/community** (checkout 3 "Special Extra Bonus" tegenover checkout 2 "Join the Happy Chef Club"), wint **een deadline op de code** van **een kale code** (cart 3 tegenover cart 2), en wint **een check-in-vraag** in post-purchase ("We've got a quick question for you!", $0,77, 8,2% klik).
- **v4 klopt grotendeels met de data.** K3/C4 (deadline op eigen code), P2 ("The one mistake that makes titanium stick"), P3-pan (deksel), P1 (bevestiging zonder founder note) volgen historische winnaars. De gaten: v4 gebruikt nergens de voornaam of de historische "saved/kept for you"-formule in de onderwerpen van mail 1, zet PFAS-vragen op plekken waar gift-framing historisch won, en heeft geen tekstmail van Benjamin buiten W2. Zie sectie 6: 15 iteraties.

## 0. Methode en datakwaliteit

| Bron | Call | Venster |
| --- | --- | --- |
| Campagnes en berichten (onderwerp, preview, afzender, template-ID, verzendtijd) | `GET /api/campaigns?filter=and(equals(messages.channel,'email'),equals(archived,false) en ook true)&include=campaign-messages` | alles (413 campagnes, waarvan 376 verzonden) |
| Campagnecijfers | `POST /api/campaign-values-reports`, group_by campaign_id, statistieken recipients, delivered, opens_unique, clicks_unique, conversion_uniques, conversions, conversion_value, unsubscribe_uniques, spam_complaints, bounced | 2025-01-01 t/m 2025-12-31 en 2026-01-01 t/m 2026-10-08 (max 1 jaar per call) |
| Flowcijfers per bericht | `POST /api/flow-values-reports`, group_by flow_id, flow_message_id | 2024-10-08 t/m 2025-10-07 en 2025-10-07 t/m 2026-10-07, per bericht opgeteld |
| Flowberichten en flows | `GET /api/flow-messages/{id}`, `GET /api/flows` (ook archived) | stand 7 okt |
| HTML | `GET /api/templates/{id}?fields[template]=html,...` voor alle 560 templates | stand 7 okt |
| Visuele check top 10 | Chromium-render op 600 px van 25 templates (contactsheets niet in de repo) | |

Afspraken:
- **RPR** = toegeschreven omzet / delivered (Klaviyo-definitie). Rates = uniek / delivered.
- **RPR-index campagnes** = RPR / mediaan-RPR van alle campagnes (>= 1.000 ontvangers) in dezelfde kalendermaand. Corrigeert voor sale-maanden, niet voor publiek. **Index flows** = RPR / mediaan van dezelfde flowgroep (checkout, cart, welcome, ...).
- Kenmerken (onderwerptype, aanbod, product, formaat) zijn met regex uit onderwerp, preview, zichtbare tekst en alt-teksten gehaald (`scripts/features.py`), na het weghalen van standaard header/footer-alts. Formaat: `image-only` = minder dan 60 woorden live tekst, `text` = 60+ woorden en hoogstens 2 inhoudsbeelden.

Beperkingen (belangrijk bij het lezen):
1. **Attributie, geen incrementaliteit.** Klaviyo schrijft een order toe aan de laatste mail binnen het venster. Mail 1 van checkout krijgt veel orders die ook zonder mail gekomen waren (research/timing 1a).
2. **Templates leven.** Flowtemplates zijn sinds verzending soms aangepast, en universal content (de rode sale-balk "SIRAAT PRIME TIME SALE, UP TO 56% OFF") staat nu in 415 templates. De HTML is dus de huidige versie, niet altijd wat er toen verstuurd werd. Campagnetemplates zijn na verzending bevroren, op die balk na.
3. **A/B per variant ontbreekt.** Het campagnerapport geeft één regel per campagne; bij 16 A/B-campagnes staan beide onderwerpen in de CSV (gescheiden door `||`).
4. **Publieksgrootte.** Kleine "highly engaged"-segmenten (1.940 tot 3.801) halen hoge RPR. Ze staan in de lijsten, maar het patroon telt pas als het ook bij grote segmenten terugkomt.
5. **Verwijderde flowberichten** van vóór oktober 2024 zitten niet in het rapport. De oudste campagne is van januari 2025.
6. **Positie-effect in flows.** Mail 1 wint altijd. Flowpatronen zijn daarom per positie vergeleken (sectie 3), niet over flows heen.
7. Vier van de top-RPR checkout-regels (New AB Checkout 1, Email #1, Copy of Email #1, de Triple Pixel-variant) gebruiken **dezelfde template** (UD7QXp en kopieën). Het verschil ($2,75 tot $7,83) is timing en cohort (10 tegen 30 minuten, periode juli 2026 tegenover december 2025), geen creatie.
8. Verzenddag en -uur: al in research/timing (3b, 3c). Hier alleen de RPR-aanvulling: donderdag (index 1,06) en vrijdag (1,14) het sterkst, dinsdag en woensdag het zwakst (0,91 tot 0,97); 291 van 326 niet-BFCM-campagnes gingen vóór 10:00 ET, dus geen zinnige uurvergelijking.

## 1. Ranglijsten (>= 1.000 ontvangers)

Volledige kolommen (preview, template-ID, publiek, formaat, producten) in de CSV's in deze map.

#### Top 20 campagnes op omzet per ontvanger

| # | Datum | Campagne (publiek) | Onderwerp | Ontv. | Open | Klik | Conv. | Omzet | RPR | RPR-index | Uitschr. | Spam |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-07-21 | 7/21 How to Cook More Without Spending More Time | Get Out of the Kitchen Quicker | 1940 | 53.3% | 3.14% | 0.36% | $2137 | $1.10 | 10.51 | 0.88% | 0.103% |
| 2 | 2025-11-29 | 11/29 Last Push for Abandoned Orders / 30 Days A | I Just Got Fired for Doing This | 12069 | 57.1% | 1.53% | 0.48% | $9286 | $0.77 | 2.13 | 1.21% | 0.050% |
| 3 | 2025-11-06 | 11/6 Special Offer / 30 Days Engaged | Hey {first_name}, We’ve got gifts for yo | 7545 | 58.2% | 2.52% | 0.32% | $5395 | $0.72 | 1.98 | 0.78% | 0.093% |
| 4 | 2025-08-14 | 8/2 Lid Launch / Titanium Hammered Pan Buyers | Put a lid on it | 3270 | 48.6% | 3.45% | 0.74% | $2229 | $0.69 | 6.94 | 1.14% | 0.000% |
| 5 | 2025-11-28 | 11/28 [6 PM] Plain text reminder / Engaged 90 Da | Don’t Iet this burn | 28491 | 60.9% | 1.83% | 0.29% | $18507 | $0.65 | 1.8 | 1.09% | 0.060% |
| 6 | 2025-11-28 | 11/28 [1 PM] Highlight Bestsellers / 90 Days Eng | 62% Off these BestseIIers | 27011 | 57.0% | 2.34% | 0.27% | $17222 | $0.64 | 1.77 | 0.95% | 0.119% |
| 7 | 2025-11-11 | 11/11 Black Friday Sale / 30 Days Engaged | Black Friday Sale On Now | 9015 | 60.9% | 3.95% | 0.32% | $5726 | $0.64 | 1.76 | 0.88% | 0.078% |
| 8 | 2025-04-21 | EB / TARIFF CAMPAIGN | From the Founder: A Note I Never Wanted to Write 💔 | 2739 | 65.2% | 3.36% | 0.33% | $1709 | $0.62 | 2.1 | 1.17% | 0.146% |
| 9 | 2025-07-11 | 7/11 Product Launch / 30 Days Engaged | Bonjour, New Arrival! 🇫🇷 | 7339 | 59.5% | 2.02% | 0.36% | $4520 | $0.62 | 2.87 | 1.46% | 0.055% |
| 10 | 2025-11-28 | 11/28 [8 AM] Black Friday + 62% Off Sitewide / 1 | 62% 0ff Cookware! | 30704 | 40.1% | 2.84% | 0.28% | $18059 | $0.59 | 1.63 | 0.73% | 0.124% |
| 11 | 2025-05-29 | 5/29 Memorial Day Email 2 / 30 Days Engaged | Last Call to Use COOK10 | 4163 | 60.3% | 1.49% | 0.29% | $2444 | $0.59 | 2.4 | 0.91% | 0.024% |
| 12 | 2025-11-30 | 11/30 [5 PM] 8 Hours Left (Plain text) / Engaged | Time’s ticking | 11045 | 60.4% | 1.76% | 0.29% | $6399 | $0.58 | 1.61 | 1.42% | 0.036% |
| 13 | 2025-11-30 | 11/30 Black Friday Weekend Extension 120 Days En | The Timer’s Started | 28132 | 57.2% | 1.33% | 0.25% | $15714 | $0.56 | 1.55 | 1.03% | 0.039% |
| 14 | 2025-11-24 | 11/24 48 Hours Left [Plain text] / Engaged 180 D | A note from James, | 12920 | 52.4% | 1.51% | 0.26% | $6876 | $0.53 | 1.48 | 1.24% | 0.016% |
| 15 | 2026-02-12 | 2/12 Warehouse Clearance Sale Launch / 30 Days E | Warehouse Sale Alert | 38026 | 53.2% | 3.58% | 0.40% | $20239 | $0.53 | 3.87 | 0.70% | 0.071% |
| 16 | 2025-11-22 | 11/22 Low in Stock Items / 30 Days Engaged | Warehouse Update | 17326 | 55.9% | 2.07% | 0.23% | $8885 | $0.51 | 1.42 | 1.21% | 0.029% |
| 17 | 2025-11-29 | 11/29 [10 AM]: Black Friday Sale Extension / 30  | Black Weekends | 26325 | 59.6% | 1.80% | 0.23% | $13376 | $0.51 | 1.41 | 1.03% | 0.034% |
| 18 | 2025-05-30 | 5/30 Titanium Wok / 30 Days Engaged & Viewers | One Wok to Rule Them All, | 3510 | 65.1% | 0.71% | 0.20% | $1772 | $0.51 | 2.06 | 0.71% | 0.000% |
| 19 | 2026-07-17 | 7/17 Why Food Sticks (And How to Fix It) / Highl | Why Food Sticks | 3801 | 61.5% | 7.18% | 0.26% | $1738 | $0.46 | 4.36 | 1.03% | 0.079% |
| 20 | 2025-05-25 | 5/25 Micro-Plastic Free / 30 Days Engaged | Cook Better = Feel Better | 3791 | 58.0% | 0.87% | 0.18% | $1671 | $0.44 | 1.8 | 0.98% | 0.026% |

#### Top 20 campagnes op klikratio

| # | Datum | Campagne (publiek) | Onderwerp | Ontv. | Open | Klik | Conv. | Omzet | RPR | RPR-index | Uitschr. | Spam |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-07-17 | 7/17 Why Food Sticks (And How to Fix It) / Highl | Why Food Sticks | 3801 | 61.5% | 7.18% | 0.26% | $1738 | $0.46 | 4.36 | 1.03% | 0.079% |
| 2 | 2025-08-04 | 8/4 Review Email / Fulfilled Orders | How was your experience? 😁 😃 😔 😫 | 2021 | 53.1% | 5.92% | 0.10% | $320 | $0.16 | 1.61 | 1.34% | 0.000% |
| 3 | 2025-12-28 | Review Email / Placed Order in the Last 3 Months | How was your experience?  😁 😃 😔 😫 | 11926 | 57.5% | 4.24% | 0.13% | $4577 | $0.39 | 2.67 | 1.09% | 0.042% |
| 4 | 2025-12-03 | 12/4 Slight Delay On Carriers / Buyers in BFCM | Your cookware is on the move | 6637 | 81.1% | 4.11% | 0.11% | $1072 | $0.16 | 1.13 | 0.29% | 0.015% |
| 5 | 2025-11-11 | 11/11 Black Friday Sale / 30 Days Engaged | Black Friday Sale On Now | 9015 | 60.9% | 3.95% | 0.32% | $5726 | $0.64 | 1.76 | 0.88% | 0.078% |
| 6 | 2025-05-14 | 5/14 Feedback / Placed Order | We’d love hear your honest feedback. | 1284 | 48.3% | 3.68% | 0.08% | $152 | $0.12 | 0.49 | 0.47% | 0.000% |
| 7 | 2026-02-12 | 2/12 Warehouse Clearance Sale Launch / 30 Days E | Warehouse Sale Alert | 38026 | 53.2% | 3.58% | 0.40% | $20239 | $0.53 | 3.87 | 0.70% | 0.071% |
| 8 | 2025-08-14 | 8/2 Lid Launch / Titanium Hammered Pan Buyers | Put a lid on it | 3270 | 48.6% | 3.45% | 0.74% | $2229 | $0.69 | 6.94 | 1.14% | 0.000% |
| 9 | 2025-04-21 | EB / TARIFF CAMPAIGN | From the Founder: A Note I Never Wanted to Write 💔 | 2739 | 65.2% | 3.36% | 0.33% | $1709 | $0.62 | 2.1 | 1.17% | 0.146% |
| 10 | 2026-07-21 | 7/21 How to Cook More Without Spending More Time | Get Out of the Kitchen Quicker | 1940 | 53.3% | 3.14% | 0.36% | $2137 | $1.10 | 10.51 | 0.88% | 0.103% |
| 11 | 2025-07-21 | 7/21 Advertorial Landing Page / 30 Days Engaged | {first_name}, this concerns you. | 6471 | 56.3% | 2.89% | 0.19% | $2648 | $0.41 | 1.91 | 1.56% | 0.031% |
| 12 | 2026-02-16 | 2/16 Product Review / Engaged 30 Days | Hello 80% Off! | 31066 | 53.0% | 2.88% | 0.19% | $7028 | $0.23 | 1.64 | 0.53% | 0.071% |
| 13 | 2025-11-28 | 11/28 [8 AM] Black Friday + 62% Off Sitewide / 1 | 62% 0ff Cookware! | 30704 | 40.1% | 2.84% | 0.28% | $18059 | $0.59 | 1.63 | 0.73% | 0.124% |
| 14 | 2025-11-06 | 11/6 Special Offer / 30 Days Engaged | Hey {first_name}, We’ve got gifts for yo | 7545 | 58.2% | 2.52% | 0.32% | $5395 | $0.72 | 1.98 | 0.78% | 0.093% |
| 15 | 2025-11-28 | 11/28 [1 PM] Highlight Bestsellers / 90 Days Eng | 62% Off these BestseIIers | 27011 | 57.0% | 2.34% | 0.27% | $17222 | $0.64 | 1.77 | 0.95% | 0.119% |
| 16 | 2025-06-27 | 6/27 Pay Day Pick / 30 Days Engaged | PayYay! | 5386 | 60.5% | 2.33% | 0.13% | $1859 | $0.35 | 2.08 | 1.62% | 0.112% |
| 17 | 2025-11-04 | 11/4 VIP Early Access - 42% off sitewide / 90 Da | Hey {first_name}, Your Savings Start Now | 12388 | 54.9% | 2.25% | 0.19% | $4815 | $0.39 | 1.08 | 0.76% | 0.137% |
| 18 | 2025-09-18 | 9/18 Anniversary Campaign / 90 Days Engaged | It’s Our Anniversary! 🎉 | 8171 | 63.2% | 2.22% | 0.17% | $2553 | $0.31 | 1.99 | 0.78% | 0.012% |
| 19 | 2025-11-07 | [Follow-up] 11/4 VIP Early Access - 42% off site | VIP Black Friday Savings Start Now | 4562 | 36.9% | 2.08% | 0.11% | $1085 | $0.24 | 0.66 | 0.35% | 0.022% |
| 20 | 2025-11-22 | 11/22 Low in Stock Items / 30 Days Engaged | Warehouse Update | 17326 | 55.9% | 2.07% | 0.23% | $8885 | $0.51 | 1.42 | 1.21% | 0.029% |

#### Slechtste 10 campagnes op uitschrijving

| # | Datum | Campagne (publiek) | Onderwerp | Ontv. | Open | Klik | Conv. | Omzet | RPR | RPR-index | Uitschr. | Spam |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2025-09-07 | 9/7 Father's Day / AU and NZ Subscribers | Happy Father’s Day | 1209 | 43.9% | 1.91% | 0.25% | $490 | $0.41 | 2.59 | 2.24% | 0.083% |
| 2 | 2025-07-13 | 7/13 Prime Day Last Call / 30 Days Engaged | Hey {first_name}, Ending Tonight, | 5649 | 72.1% | 1.70% | 0.18% | $1475 | $0.26 | 1.22 | 1.98% | 0.035% |
| 3 | 2025-08-21 | 8/21 Bestsellers + Product Review / 30 Days Enga | Kitchen Confidential | 7338 | 67.5% | 1.34% | 0.23% | $2774 | $0.38 | 3.83 | 1.94% | 0.068% |
| 4 | 2025-11-30 | Clone 11/30 [5 PM] 8 Hours Left (Plain text) / E | Time’s ticking | 25526 | 61.0% | 1.50% | 0.16% | $10191 | $0.40 | 1.11 | 1.82% | 0.051% |
| 5 | 2025-03-16 | Email Campaign - Mar 14, 2025, 5:28 PM (clone) | Ultimate Cutting Board: Last Stock Alert! | 2953 | 48.4% | 1.09% | 0.03% | $60 | $0.02 | 0.16 | 1.77% | 0.136% |
| 6 | 2025-08-03 | 8/3 Cooking with Family + Product Feature / 30 D | Quality Time = Cooking Time | 6601 | 64.3% | 0.94% | 0.08% | $939 | $0.14 | 1.44 | 1.72% | 0.015% |
| 7 | 2025-03-14 | Email Campaign - Mar 14, 2025, 5:28 PM | Hurry! Ultimate Cutting Board Selling Fast! ⏳ | 2781 | 46.7% | 0.98% | 0.18% | $1011 | $0.37 | 2.83 | 1.67% | 0.217% |
| 8 | 2025-06-27 | 6/27 Pay Day Pick / 30 Days Engaged | PayYay! | 5386 | 60.5% | 2.33% | 0.13% | $1859 | $0.35 | 2.08 | 1.62% | 0.112% |
| 9 | 2025-07-15 | [Follow-up] 7/13 Meal Prep Hacks + Crepe Pan Fol | Time to Save: Your Sanity Matters! | 1806 | 29.9% | 1.05% | 0.11% | $306 | $0.17 | 0.79 | 1.61% | 0.055% |
| 10 | 2025-08-05 | [Follow-up] 8/3 Cooking with Family + Product Fe | Unlock Quality Cooking Moments! | 1621 | 34.3% | 0.43% | 0.00% | $0 | $0.00 | 0.0 | 1.61% | 0.000% |

#### Top 20 flowberichten op omzet per ontvanger

| # | Flow (status) | Bericht | Onderwerp | Ontv. | Open | Klik | Conv. | Omzet | RPR | Index in groep | Uitschr. | Spam |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EB / DEC 25 / Checkout Abandonment (live) | New AB Checkout 1 | Don’t leave these hanging | 2394 | 46.7% | 4.03% | 2.35% | $17307 | $7.83 | 5.91 (checkout) | 1.04% | 0.000% |
| 2 | Welcome Series Flow - HKT (draft) | Welcome Series, Email #1 | Welcome to Siraat Kitchen , Your 10% Off Awaits! | 1004 | 51.6% | 7.29% | 2.84% | $6492 | $6.58 | 12.29 (welcome) | 2.63% | 0.000% |
| 3 | EB / DEC 25 / Checkout Abandonment (live) | Email #1 | Don’t leave these hanging | 8921 | 45.0% | 3.68% | 2.20% | $46352 | $5.36 | 4.05 (checkout) | 1.38% | 0.092% |
| 4 | EB / DEC 25 / Checkout Abandonment (live) | Copy of Email #1 | Don’t leave these hanging | 8239 | 44.0% | 3.51% | 1.87% | $36788 | $4.59 | 3.47 (checkout) | 1.45% | 0.112% |
| 5 | EB / DEC 25 / Checkout Abandonment (live) | Email #1 | Don’t leave these hanging | 6647 | 50.5% | 4.78% | 1.83% | $28379 | $4.32 | 3.26 (checkout) | 0.73% | 0.122% |
| 6 | EB / Welcome Flow / Updated 02.03. (live) | Welcome Series, Email #1 | Welcome to {org} Family😍 | 6497 | 59.8% | 4.85% | 2.10% | $25762 | $4.01 | 7.5 (welcome) | 1.64% | 0.047% |
| 7 | EB / Checkout Abandonment / 5/13/2 (draft) | Email #1 | Don’t leave these hanging | 9546 | 53.7% | 3.61% | 1.34% | $27889 | $2.95 | 2.23 (checkout) | 1.59% | 0.074% |
| 8 | EB / Browse Abandonment / 4/25/25 (draft) | Email #1 | Hi {first_name}, we saw you looking... | 16301 | 53.6% | 4.18% | 1.39% | $46758 | $2.90 | 2.24 (browse) | 3.05% | 0.081% |
| 9 | EB / DEC 25 / Checkout Abandonment (live) | Copy of Email #1 | Don’t leave these hanging | 6423 | 48.2% | 4.23% | 1.37% | $17475 | $2.75 | 2.08 (checkout) | 1.20% | 0.063% |
| 10 | EB / Welcome Flow / Updated 02.03. (live) | Eb [DG] / Email #1 (FLOW Upd | {first_name}, Thanks For Joining Us | 199479 | 48.5% | 3.08% | 1.22% | $535843 | $2.73 | 5.1 (welcome) | 2.64% | 0.150% |
| 11 | EB / Cart Abandonment / 2/03/26 (live) | Email #1 | Hi {first_name}, we saved these for you | 36198 | 44.8% | 2.87% | 0.97% | $95297 | $2.66 | 2.58 (cart) | 1.61% | 0.084% |
| 12 | EB / Cart Abandonment / 2/03/26 (live) | Copy of Email #1 | Hi {first_name}, we saved these for you | 35219 | 44.4% | 2.82% | 0.92% | $85035 | $2.43 | 2.37 (cart) | 1.61% | 0.077% |
| 13 | EB / DEC 25 / Checkout Abandonment (live) | New AB Checkout 3 | We’ve cooked something for you! | 1441 | 41.2% | 2.44% | 0.91% | $3427 | $2.39 | 1.8 (checkout) | 1.25% | 0.000% |
| 14 | EB / Checkout Abandonment / 5/13/2 (draft) | Copy of Email #1 | Don’t leave these hanging | 9345 | 52.8% | 3.31% | 1.01% | $20146 | $2.17 | 1.64 (checkout) | 1.68% | 0.043% |
| 15 | EB / Browse Abandonment / 4/25/25 (draft) | Copy of Email #1 | Hi {first_name}, we saw you looking... | 15863 | 52.1% | 3.70% | 0.85% | $32997 | $2.11 | 1.63 (browse) | 2.93% | 0.128% |
| 16 | EB / Checkout Abandonment / 5/13/2 (draft) | Email #2 | Join the Happy Chef Club | 1257 | 49.5% | 3.40% | 0.73% | $2020 | $1.64 | 1.24 (checkout) | 2.27% | 0.081% |
| 17 | EB / DEC 25 / Checkout Abandonment (live) | Email #3 | Your Order with a Special Extra Bonus | 13701 | 42.2% | 2.88% | 0.59% | $19249 | $1.41 | 1.07 (checkout) | 0.92% | 0.103% |
| 18 | EB / Checkout Abandonment / 5/13/2 (draft) | Email #3 | Your Order with a Special Extra Bonus | 1596 | 48.6% | 3.84% | 0.45% | $2191 | $1.40 | 1.06 (checkout) | 0.64% | 0.064% |
| 19 | EB / DEC 25 / Browse Abandonment / (live) | Email #1 | Hi {first_name}, we saw you looking... | 61979 | 39.5% | 3.49% | 0.64% | $82266 | $1.33 | 1.03 (browse) | 1.22% | 0.079% |
| 20 | EB / DEC 25 / Browse Abandonment / (live) | Copy of Email #1 | Hi {first_name}, we saw you looking... | 61024 | 39.0% | 3.24% | 0.58% | $76589 | $1.26 | 0.97 (browse) | 1.32% | 0.084% |

#### Top 20 flowberichten op klikratio

| # | Flow (status) | Bericht | Onderwerp | Ontv. | Open | Klik | Conv. | Omzet | RPR | Index in groep | Uitschr. | Spam |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EB / Post Purchase Flow / 4/6/2026 (live) | Copy of Post Purchase Flow / | Your Package Is On Its Way | 4280 | 72.8% | 33.60% | 0.35% | $2400 | $0.56 | 1.55 (post purchase) | 0.19% | 0.070% |
| 2 | EB / Post Purchase Flow / 4/6/2026 (live) | Post Purchase Flow / IT'S ON | Your Package Is On Its Way | 26209 | 71.0% | 33.10% | 0.18% | $8395 | $0.32 | 0.88 (post purchase) | 0.21% | 0.061% |
| 3 | EB / Post Purchase Flow / 4/6/2026 (live) | Copy of Post Purchase Flow / | Your Package Is On It’s Way | 2353 | 65.9% | 25.85% | 0.34% | $889 | $0.38 | 1.04 (post purchase) | 0.13% | 0.128% |
| 4 | FLOW - UPDATE ORDER - FLORIS 28-03 (draft) | Copy of Copy of Email #1 | Quick update about your oder | 1912 | 76.1% | 22.07% | 0.21% | $806 | $0.43 | 2.19 (other) | 0.16% | 0.000% |
| 5 | FLOW - UPDATE ORDER - FLORIS 28-03 (draft) | Copy of Email #1 | Update about your order | 1188 | 77.1% | 19.78% | 0.17% | $412 | $0.35 | 1.81 (other) | 0.34% | 0.000% |
| 6 | FREE E-GUIDE FLOW (draft) | Email #1 | Your guide is inside | 2428 | 51.2% | 9.41% | 0.42% | $1722 | $0.72 | 10.03 (guide) | 1.17% | 0.208% |
| 7 | EB / Post Purchase Flow / 4/6/2026 (live) | Post Purchase Flow / 1st tim | We’ve Got Your Order | 4803 | 65.3% | 9.13% | 0.40% | $4372 | $0.91 | 2.51 (post purchase) | 0.33% | 0.042% |
| 8 | EB / Post Purchase Flow / 4/6/2026 (live) | Copy of Post Purchase Flow / | A note from Benjamin | 4498 | 62.5% | 9.04% | 0.20% | $1439 | $0.32 | 0.88 (post purchase) | 2.21% | 0.022% |
| 9 | EB / E-Book (live) | Copy of The Green Clean Guid | Your Mystery Gift Is Here | 50040 | 62.0% | 8.71% | 0.21% | $19247 | $0.39 | 2.8 (e-book) | 0.41% | 0.127% |
| 10 | New Customer Thank You Flow - HKT (draft) | New Customer Thank You: Emai | Thank You for Choosing Siraat Kitchen! | 1345 | 65.8% | 8.47% | 0.22% | $312 | $0.23 | 1.21 (other) | 1.50% | 0.000% |
| 11 | EB / Post Purchase Flow / 4/6/2026 (live) | Post Purchase Flow / Founder | A note from Benjamin | 27370 | 59.4% | 8.41% | 0.12% | $5493 | $0.20 | 0.55 (post purchase) | 1.50% | 0.044% |
| 12 | EB / Post Purchase Flow / 5/5/25 (draft) | Email #4 | We’ve got a quick question for you! | 22228 | 63.0% | 8.19% | 0.38% | $17006 | $0.77 | 2.11 (post purchase) | 0.97% | 0.072% |
| 13 | EB / Post Purchase Flow / 5/5/25 (draft) | Email #1 | We’ve got your order! | 6565 | 65.7% | 8.02% | 0.35% | $3405 | $0.52 | 1.43 (post purchase) | 0.50% | 0.015% |
| 14 | EB / Post Purchase Flow / 4/6/2026 (live) | Post Purchase Flow / GET REA | Unlocking the Non-Stick | 19320 | 55.4% | 7.81% | 0.20% | $6448 | $0.33 | 0.92 (post purchase) | 0.80% | 0.026% |
| 15 | EB / Post Purchase Flow / 4/6/2026 (live) | Post Purchase Flow / 1st tim | We’ve Got Your Order | 23080 | 64.0% | 7.80% | 0.20% | $8982 | $0.39 | 1.07 (post purchase) | 0.38% | 0.078% |
| 16 | EB / Pan Education (live) | FLOW: Cutting Board Educatio | Quick Cutting Board FAQs | 1304 | 61.0% | 7.39% | 0.54% | $1447 | $1.11 | 2.84 (education) | 1.62% | 0.000% |
| 17 | FREE E - GUIDE (live) | E-Guide Flow | Your E-Guide Is Ready | 26156 | 60.7% | 7.32% | 0.17% | $7290 | $0.28 | 3.92 (guide) | 0.98% | 0.112% |
| 18 | Welcome Series Flow - HKT (draft) | Welcome Series, Email #1 | Welcome to Siraat Kitchen , Your 10% Off Awaits! | 1004 | 51.6% | 7.29% | 2.84% | $6492 | $6.58 | 12.29 (welcome) | 2.63% | 0.000% |
| 19 | EB / Pan Education (live) | Pan Education / Email 1 | Your Siraat Titanium Pan is about to arrive, | 27757 | 63.2% | 7.15% | 0.25% | $14285 | $0.52 | 1.32 (education) | 0.27% | 0.014% |
| 20 | EB / E-Book (live) | Email 2: E-Book Reminder | Open Your Mystery Gift 🎁 | 12054 | 17.5% | 7.09% | 0.02% | $238 | $0.02 | 0.14 (e-book) | 0.36% | 0.100% |

#### Slechtste 10 flowberichten op uitschrijving

| # | Flow (status) | Bericht | Onderwerp | Ontv. | Open | Klik | Conv. | Omzet | RPR | Index in groep | Uitschr. | Spam |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  (weg) | Customer Winback : Email 1 | Hey, it’s been some time since we saw you. | 2157 | 54.1% | 2.45% | 0.28% | $776 | $0.37 | 1.88 (other) | 4.56% | 0.141% |
| 2 | EB / Browse Abandonment / 4/25/25 (draft) | Email #1 | Hi {first_name}, we saw you looking... | 16301 | 53.6% | 4.18% | 1.39% | $46758 | $2.90 | 2.24 (browse) | 3.05% | 0.081% |
| 3 | EB / Browse Abandonment / 4/25/25 (draft) | Copy of Email #1 | Hi {first_name}, we saw you looking... | 15863 | 52.1% | 3.70% | 0.85% | $32997 | $2.11 | 1.63 (browse) | 2.93% | 0.128% |
| 4 | EB / Welcome Flow / Updated 02.03. (live) | Eb [DG] / Email #1 (FLOW Upd | {first_name}, Thanks For Joining Us | 199479 | 48.5% | 3.08% | 1.22% | $535843 | $2.73 | 5.1 (welcome) | 2.64% | 0.150% |
| 5 | Welcome Series Flow - HKT (draft) | Welcome Series, Email #1 | Welcome to Siraat Kitchen , Your 10% Off Awaits! | 1004 | 51.6% | 7.29% | 2.84% | $6492 | $6.58 | 12.29 (welcome) | 2.63% | 0.000% |
| 6 |  (weg) | Customer Winback: Email 2 | A special gift - Just for you | 1919 | 51.4% | 1.54% | 0.21% | $290 | $0.15 | 0.79 (other) | 2.54% | 0.106% |
| 7 | EB / Post Purchase Flow / 5/5/25 (draft) | Email #2 | Cooking just got healthier | 42411 | 60.4% | 3.33% | 0.22% | $12718 | $0.30 | 0.83 (post purchase) | 2.39% | 0.040% |
| 8 | EB / Welcome Flow / Updated 02.03. (live) | Welcome Series, Email #2 | Stay Connected: Follow us on Social Media! | 6053 | 52.7% | 1.58% | 0.15% | $1082 | $0.18 | 0.34 (welcome) | 2.31% | 0.033% |
| 9 | X Farooq / Customer Thank You Flow (draft) | New Customer Thank You: Emai | You're what makes us great | 2719 | 58.9% | 3.03% | 0.11% | $306 | $0.11 | 0.58 (other) | 2.29% | 0.000% |
| 10 | EB / Checkout Abandonment / 5/13/2 (draft) | Email #2 | Join the Happy Chef Club | 1257 | 49.5% | 3.40% | 0.73% | $2020 | $1.64 | 1.24 (checkout) | 2.27% | 0.081% |

## 2. Patronen in campagnes (346 campagnes met maandindex)

"Mediaan-index" is de typische campagne met dat kenmerk ten opzichte van de maand. "Gewogen" is alle omzet gedeeld door alle delivered. Bij kleine n (onder 15) is het een aanwijzing, geen bewijs. Bron: `patterns-campaigns.csv`.

### 2a. Onderwerpregel

| Kenmerk | n | Mediaan RPR-index | Mediaan klikindex | Klik (gewogen) | Uitschr. (gewogen) | Lezing |
| --- | --- | --- | --- | --- | --- | --- |
| Geen kenmerk (basis) | | 1,00 | 1,00 | 0,76% | 0,64% | |
| Voornaam in onderwerp | 21 | 1,08 | **1,17** | **1,08%** | 0,77% | Meer klik, iets meer uitschrijving |
| Getal | 40 | 1,08 | 1,10 | 0,87% | **0,49%** | Getallen helpen en kosten niets |
| Korting/sale in onderwerp | 36 | 1,04 | 1,15 | 1,05% | 0,48% | Werkt, maar het aanbod zelf doet het werk |
| Urgentie (last, ends, hours left) | 40 | **1,17** | 1,10 | 0,75% | 0,57% | Alleen met echte deadline |
| PFAS / non-toxic / healthy | 13 | 1,19 | 1,17 | 0,88% | 0,72% | Licht positief, kleine n |
| Social proof (bestsellers, reviews, #1) | 22 | 1,00 | 0,97 | 0,66% | 0,63% | Geen effect in het onderwerp |
| Vraag (?) | 13 | **0,84** | 0,99 | 1,02% | 0,78% | Meer klik (gewogen +34%), minder omzet |
| Nieuwsgierigheid zonder aanbod | 41 | 1,00 | 1,00 | 0,83% | 0,70% | Neutraal |
| Nieuw / launch | 13 | 0,84 | 1,09 | 0,77% | 0,72% | Woord "new" alleen helpt niet; het nieuwe product wel (2b) |
| Emoji | 36 | 0,98 | 0,98 | **0,56%** | 0,46% | Gewogen RPR $0,086 tegen $0,141 zonder: niet gebruiken |
| Lengte 0 tot 2 woorden | 33 | 1,11 | 1,10 | 0,77% | 0,68% | Kort mag ("Put a lid on it", "Why Food Sticks") |
| Lengte 6 tot 8 woorden | 90 | 0,92 | 0,99 | 0,71% | 0,55% | |
| Lengte 9+ woorden | 19 | 1,11 | 1,05 | 0,79% | 0,40% | Founder-onderwerpen zijn lang en doen het goed |

Vergelijk met `research/onderwerpen/01-lab.md` (zelfde dag, 365 dagen, regressie met publiek x maand, maat klik): vraag +57% klik (n=7), emoji -25% klik, voornaam opent beter, getallen generiek. Deze analyse (21 maanden, maat RPR) bevestigt emoji en de klikwinst van voornaam en vraag, maar ziet bij vragen geen omzetwinst. Conclusie voor v4: een vraag mag om klik te halen, alleen niet als de omzetmail van een reeks op een vraag leunt zonder test.

### 2b. Invalshoek (thema uit naam, onderwerp en preview, zonder Black Friday)

| Thema | n | Mediaan RPR-index | Mediaan klikindex | RPR (gewogen) | Uitschr. | Voorbeelden |
| --- | --- | --- | --- | --- | --- | --- |
| Nieuw product / launch | 25 | **1,15** | **1,24** | $0,131 | 0,55% | Lid Launch (6,94), Crêpe launch (2,87), Wok (2,06) |
| Gift / bonus | 21 | 1,10 | 1,06 | $0,145 | 0,72% | "We've got gifts for you!" (1,98), Labor Day free gift |
| Deadline van een lopende sale | 18 | 1,10 | 1,05 | $0,108 | 0,52% | "Last Call to Use COOK10" (2,40) |
| Founder / tekstmail | 20 | 1,03 | **1,21** | $0,107 | 0,58% | 7/24 Benjamin "63% off" (2,22, uitschr. 0,34%), tariff note (2,10) |
| PFAS / gezondheid | 19 | 1,00 | 0,88 | $0,121 | 0,70% | "Cook Better = Feel Better" (1,80) |
| Reviews / bestsellers | 35 | 1,00 | 1,09 | $0,121 | 0,65% | "Kitchen Confidential" (3,83, maar 1,94% uitschr.) |
| Sale-lancering | 35 | 0,98 | 1,00 | $0,116 | 0,53% | Warehouse sale 80% (3,87) |
| Vergelijking (vs) | 12 | 0,92 | 0,91 | $0,116 | 0,54% | "Titanium VS Non-Stick" (2,60) is de uitzondering |
| Educatie / how-to | 55 | 0,91 | 0,84 | $0,112 | 0,62% | Algemeen zwak, **behalve** concrete kookhulp: "Why Food Sticks" (4,36, 7,18% klik), "Get out of the kitchen quicker" (10,51) |
| Seizoen / verhaal | 8 | **0,70** | 0,89 | $0,069 | 0,55% | Father's Day, "Cooking with family" |

### 2c. Aanbod, formaat, product, lengte

| Kenmerk | n | Mediaan RPR-index | Klik (gewogen) | Uitschr. | Lezing |
| --- | --- | --- | --- | --- | --- |
| Geen % in de mail | 251 | 0,97 | 0,70% | 0,68% | |
| Tot 20% | 15 | 1,00 | 0,65% | 0,61% | Een kale 10% doet in campagnes niets extra |
| 21 tot 49% | 33 | 1,04 | 0,97% | 0,85% | |
| 50% of meer | 47 | 1,15 | 0,93% | 0,50% | Diepe sitewide sale verkoopt, maar is een moment, geen flowtactiek |
| Code in de mail genoemd | 15 | **1,52** | 1,07% | 0,78% | Een eigen code met naam (COOK10, VIP62, EXTRA30) verkoopt |
| Gift genoemd | 33 | 1,01 | 0,72% | **0,48%** | Gift verlaagt uitschrijving |
| Formaat tekst | 39 | **1,22** | 0,87% | **0,56%** | Zie ook PLAYBOOK 1 (founder-notes klikken beter) |
| Formaat image-only | 305 | 0,99 | 0,74% | 0,65% | 88% van alle campagnes |
| Hoofdproduct wok / crêpe | 13 | 1,00 tot 1,48 | 1,0% | 1,1% | Hoge RPR, hoge uitschrijving |
| Hoofdproduct pan / set | 177 | 1,00 | 0,81% | 0,62% | |
| Hoofdproduct utensils / deep pan / steamer | 22 | 0,47 tot 0,87 | 0,3 tot 0,6% | | Niet als hoofdonderwerp |
| Aantal inhoudsbeelden 0-3 / 4-6 / 7-10 / 11+ | 131 / 99 / 87 / 29 | 1,01 / 1,00 / 0,98 / 1,01 | | 0,62 / 0,66 / 0,69 / 0,54% | Lengte van de mail maakt geen verschil |
| Black Friday-week | 20 | 1,42 | 1,54% | 1,16% | Het seizoen, niet de mail |
| Publiek engaged 30 dagen | 179 | 1,05 | 0,93% | 0,81% | |
| Publiek engaged 60 tot 90 dagen | 61 | 0,91 | 0,64% | 0,64% | |

## 3. Patronen in flows, per positie

Bron: `flow-messages-all.csv`. RPR per ontvanger, klik, uitschrijving.

| Flow | Positie | Variant (onderwerp) | RPR | Klik | Uitschr. | Les |
| --- | --- | --- | --- | --- | --- | --- |
| Checkout | 1 (10 tot 30 min) | "Don't leave these hanging" / preview "You're a click away from better kitchen tools"; hero "We Kept These Safe Just For You", cart en knop boven de vouw, **geen code** | $2,17 tot $7,83 | 3,3 tot 4,8% | 0,7 tot 1,7% | De sterkste mail in het account, zonder korting |
| Checkout | 2 (dag 1) | "Join the Happy Chef Club" (merk, community) | $0,78 tot $0,94 | 1,5 tot 2,2% | 1,2 tot **2,3%** | Merkmail zonder reden om terug te komen: zwakste stap |
| Checkout | 3 | "Your Order with a Special Extra Bonus" / "See Inside for Details" | $0,81 tot $1,41 | **2,9 tot 3,8%** | 0,6 tot 1,2% | Gift-framing verslaat merkmail, ook later in de reeks |
| Checkout | 3 (AB-arm) | "We've cooked something for you!" + 10% COOKHAPPY | **$2,39** | 2,4% | 1,25% | Gift-woorden plus eigen code |
| Checkout | 4 | "We Can't Keep these Forever" / "Cart & Discount Expires Tonight" | $0,70 tot $1,25 | 1,7 tot 2,5% | 0,7 tot 1,4% | Deadline werkt, maar "tonight" zonder echte deadline mag niet meer |
| Checkout | 4 (AB-arm) | "One Click to Cooking Better for Life" | $0,44 | 1,3% | 0,85% | Vaag merkonderwerp: laagste |
| Cart | 1 (15/30 min) | "Hi {first_name}, we saved these for you" / "Get Cooking Now" | $2,43 tot $2,66 | 2,8 tot 2,9% | 1,6% | Voornaam + "saved for you" |
| Cart | 2 | "Hi {first_name}, getting cooking with 10% off" | $0,63 tot $1,11 | 1,5 tot 2,4% | 0,9 tot 1,3% | Kale 10% zonder deadline: zwak |
| Cart | 3 | "Last Call for 10% Off!" / "Your discount ends in 48 hours" | $0,88 tot $1,05 | 1,5 tot 1,9% | 0,7 tot 1,0% | Zelfde 10% met deadline: +40 tot 65% RPR tegenover mail 2 in de hoofdflow; in de kleine Triple Pixel-flow geen verschil ($1,01 tegen $1,11) |
| Browse | 1 | "Hi {first_name}, we saw you looking..." / "Upgrade your kitchen kit" | $0,69 tot $2,90 | 2,6 tot 4,2% | 1,2 tot **3,0%** | "We saw you" wint omzet, kost uitschrijving (oude 4/25-versie 3%) |
| Welcome | 1 | "{first_name}, Thanks For Joining Us" / "It's great to have you here", HI10 in hero | **$2,73** (199.479 ontv.) | 3,1% | 2,6% | Best verdienende mail ooit; eerste contact geeft altijd hoge uitschrijving |
| Welcome | 1 (oud HKT) | "Welcome to Siraat Kitchen, Your 10% Off Awaits!" | $6,58 (1.004 ontv.) | 7,3% | 2,6% | Aanbod in het onderwerp, kleine oude n |
| Welcome | 2 | "A Note from Benjamin" (tekst, 324 woorden) | $0,72 | 2,6% | 2,1% | Tekstmail op dag 1 verslaat de beeldmails van dag 3 tot 10 (positie speelt mee) |
| Welcome | 3 tot 5 | "Straight from the kitchen", "Cook with the Best", "The ultimate showdown" | $0,39 tot $0,65 | 1,4 tot 2,1% | 1,4 tot 2,0% | Vergelijking (showdown) $0,54 |
| Welcome | extra | "See Why We Are Top Rated" / "Last Call for an Extra 10% Off" | $0,17 / $0,25 | 0,9% | 0,7 tot 0,9% | Social proof als onderwerp: zwakste |
| Welcome / FTL | quiz | "Hey {first_name}, We've got questions" / "How well will you be?" | $0,59 (welcome) / $0,22 (FTL) | 1,9% / 0,7% | 1,0% / 0,8% | In failure-to-launch 3 tot 5 keer de RPR van de andere 10 mails ($0,04 tot $0,08) |
| Post-purchase | 1 | "We've Got Your Order" / "Thank You For Cooking with Us" | $0,39 tot $0,91 | 6,8 tot 9,1% | 0,3 tot 0,6% | |
| Post-purchase | founder | "A note from Benjamin" / "Cooking just got healthier, A note from James" | $0,20 tot $0,32 | 3,3 tot 9,0% | **1,5 tot 2,4%** | Founder note vlak na aankoop jaagt kopers weg |
| Post-purchase | check-in | "We've got a quick question for you!" / "How's it going?" | **$0,77** | **8,2%** | 0,97% | Beste niet-transactionele PP-mail |
| Post-purchase | garantie | "100 Days to Try Us Out" | $0,13 | 3,2% | 1,0% | |
| Pan education | 1 | "Your Siraat Titanium Pan is about to arrive" / "The 3-step method for perfect non-stick cooking" | $0,52 | 7,2% | **0,27%** | Stappenplan met foto's |
| Pan education | 2 | "The #1 mistake that makes titanium stick 🔥" / "It's simpler than you think" | $0,42 | 6,9% | 0,59% | Zelfde idee als v4 P2-B |
| Pan education | 3 tot 6 | kleur, schoonmaken, "5 things", "a week cooking" | $0,25 tot $0,39 | 2,1 tot 4,0% | 0,5 tot 0,7% | Afnemend |
| Review (Trustpilot) | | "How was your experience?" (tekst) | $0,60 | 4,2% | 0,9% | |
| E-guide | 1 | "Your guide is inside" / "50+ recipes. One surprise..." | $0,72 | 9,4% | 1,2% | Beloofde gift leveren = klik |
| Winback | 1 tot 3 | "Serving Up New Must-Haves" / "We Cut a Deal for You" (10%) / "10% Off Expires Tonight" | $0,24 / $0,11 tot $0,24 / $0,22 | 0,6 tot 0,8% | 0,9 tot 1,0% | Nieuw-invalshoek even goed als korting |
| Sunset | 1, 2 | "Hi {first_name}, it's been a while" / "are you Staying or Going?" | $0,06 | 0,45% | 0,6 tot 1,0% | |

## 4. Wat de top 10 gemeen hebben (HTML bekeken)

Gerenderd en bekeken: de 10 campagnes met de hoogste RPR (QSxH3X, Si6st2, TuFtP3, RRHn5w, R4he9x, URTniy, VFgC7p, XWXeub, SnhBzN, Wr9eRc), plus 5 campagnes met hoge maandindex (UVr2ct, QWGLEC, W4ZFxc, XDCge5, W9MieH) en 11 winnende flowmails (UD7QXp, YdWRjr, TicuGn, XTCs5P, Xm8ZHM, X9w6vN, UDUmFi, VPBrLr, VEttPt, VAJ4SU, WQ5Px5).

| Template | Campagne | Hero | Kop in de hero | Aanbod | Hoogte op 600 px |
| --- | --- | --- | --- | --- | --- |
| QSxH3X | 7/21 Get Out of the Kitchen Quicker | lifestyle: hand schrobt pan in de gootsteen | "GET CLEANED UP QUICKER" | geen | 2.447 |
| Si6st2 | 11/29 Last push (abandoned) | geen, tekstmail van "Ali" | | EXTRA30 bovenop 42% | 1.825 |
| TuFtP3 | 11/6 Special offer | product in gebruik: pasta in pan, deksel, onderzetter | "Check Out These Two Incredible Offers" | gratis deksel, onderzetter en spatel bij Pan Pro | 2.796 |
| RRHn5w | 8/2 Lid launch (pankopers) | product: deksel, donker hout | "LIDS HAVE LANDED" | geen | 2.182 |
| R4he9x | 11/28 plain text | geen, 4 regels tekst | | VIP62, 62% | 856 |
| URTniy | 11/28 bestsellers | product op het fornuis | "Whip Up Extra Savings" | 42% + 20% met VIP62 | 3.086 |
| VFgC7p | 11/11 Black Friday | sfeerbeeld goud | "42% Off Is Here" | 42% | 4.140 |
| XWXeub | Tariff note | geen, tekstmail | | SIRAAT25 | 900 |
| SnhBzN | 7/11 crêpe launch | lifestyle: pannenkoeken op de crêpepan | "Flip Breakfast Flawlessly" | geen, "limited stock" | 2.251 |
| Wr9eRc | 11/28 62% off | lifestyle: wokgerecht in de pan | "62% OFF Sitewide" | 62% met VIP62 | 3.093 |
| UVr2ct | 7/17 Why Food Sticks | lifestyle: handen, crêpe in pan | "GET UN-STUCK" | geen | 4.258 |
| W9MieH | 7/24 Founder (Benjamin) | geen, tekstmail | | 63%, al op de pagina | 1.146 |

Gemeen:
1. **Eén idee, groot in de hero, met de knop er direct onder.** Elke beeldmail in de top opent met een kop van 2 tot 5 woorden die het idee of het aanbod draagt ("LIDS HAVE LANDED", "GET UN-STUCK", "62% OFF Sitewide") en een knop boven de vouw. Dat is al PLAYBOOK 10/11.
2. **De pan in gebruik, met eten of handen.** 4 van de 7 beeld-hero's in de top 10 tonen de pan tijdens het koken of schoonmaken (pasta, pannenkoeken, wok, schrobben), en ook de klikkampioen UVr2ct (handen, crêpe). Losse packshots alleen bij een productlancering (deksel). Abstracte sfeerbeelden (goud, merkpatroon) alleen in sale-mails.
3. **Drie van de tien zijn kale tekstmails** van 4 tot 20 zinnen, met een persoon als afzender en één code of één link. Geen header-beeld. Hoogte 856 tot 1.825 px.
4. **Eén product of één belofte**, niet de catalogus. De productgrids zitten alleen in Black Friday-mails, waar de sale het werk deed.
5. **Kort.** Mediaan ongeveer 2.350 px op 600 px breed. Geen relatie tussen lengte en RPR (2c).
6. **Sterrenbalk of klantenaantal direct onder de hero** in 5 van de 10 ("Rated 4.9/5 by 30,000+ Customers", "100K+ Happy customers" met een korte quote).
7. **Flowmail 1 (checkout, cart, browse)** heeft overal dezelfde bouw: begroeting met voornaam, korte kop ("We Kept These Safe For You", "You've Got Great Taste", "Make Your Kitchen a Cut Above"), het product uit de cart met prijs en knop, dan een raster met vier tot zes voordelen (no toxins/PFAS, antibacterial, knife-friendly, lifetime). Geen korting in mail 1.
8. **Pan education 1 en "Why Food Sticks"** gebruiken genummerde stappen met een eigen foto per stap (verwarmen, waterdruppel, olie). Dat is precies de bouw van v4 P2.

## 5. Niet herhalen

- **Si6st2 "I Just Got Fired for Doing This"** (nr. 2 op RPR, $9.286): een verzonnen verhaal van "Ali, former Customer Satisfaction Manager" met code EXTRA30. Misleidend, en botst met DECISIONS (oprichter is Benjamin, nooit Ali of Floris). De RPR komt van het publiek (30 dagen verlaten carts) en de BFCM-week.
- **"A note from James"** en "Floris, Founder" (tariff note, 11/24): verkeerde oprichtersnaam. Het tekstformat wel overnemen, de naam niet.
- **"30,000+ customers", "100-day trial", "lifetime warranty"** in vrijwel alle oude templates: vervangen door 100,000+, 30-day returns, 75-year warranty (DECISIONS).
- **Nep-deadlines** ("Expires Tonight", "We Can't Keep these Forever") werkten, maar mogen alleen nog met een unieke verlopende code (PLAYBOOK 11).
- **Social-follow-mail** ("Stay Connected: Follow us", 2,31% uitschrijving, $0,18) en **founder note direct na aankoop** (1,5 tot 2,4% uitschrijving): v4 heeft ze al niet.
- **Seizoensverhalen** (Father's Day AU 2,24% uitschrijving, "Cooking with Family" 1,72%) en **utensils/deep pan als hoofdproduct**.
- **Emoji in het onderwerp**: geen meetbare winst, gewogen RPR $0,086 tegenover $0,141.

## 6. Vertaling naar v4: 15 iteraties, gerangschikt op verwachte impact

Impact = volume van de mail × grootte van het historische verschil × hoe zeker dat verschil is. Testplekken volgen v4-flow-system 1.6 (maximaal 2 tests per flow, T01 en T02 eerst). "Vast" = zonder test doorvoeren, want het historische bewijs is sterk en v4 wijkt er zonder reden van af. Onderwerpen in het Engels, volgens skill siraat-direct-response.

| # | v4-mail | Soort | Wat | Historisch bewijs | Wanneer |
| --- | --- | --- | --- | --- | --- |
| 1 | **C1** (checkout 1) | A/B onderwerp | B = "Don't leave these hanging" (of "We kept your cart safe") tegen v4-A. Let op: manifest zegt "Something stop you at checkout?", v4-flow-system 2.1 zegt "Forgetting something?"; eerst één A kiezen. | Dit onderwerp stond op alle zeven checkout-1-varianten met 1.000+ ontvangers ($2,17 tot $7,83, 3,3 tot 4,8% klik), samen $194.000 omzet. Een vraagonderwerp zakte in campagnes naar index 0,84. | Fase 2, na T01 (T01 vergelijkt het hele pad, niet het onderwerp) |
| 2 | **C1** | Vast / T03-controle | Geen HI10 in preview en hero van C1 als controlearm van T03. | Alle historische checkout-1-mails hadden geen code en zijn de best verdienende flowmails; kortingen pas vanaf mail 3. 74% van de checkout-starters koopt toch al (timing 1a), korting in mail 1 geeft vooral marge weg. | T03 (fase 2) zo inrichten |
| 3 | **W1-A/B** | A/B onderwerp (T05b) | B = "{first_name}, thanks for joining. Your 10% is inside" (voornaam + dank + aanbod) tegen "No PFAS, nothing to wear off, and your 10%". | Oude welcome 1 "{first_name}, Thanks For Joining Us" haalde $2,73 op 199.479 ontvangers ($535.843), de HKT-versie met het aanbod in het onderwerp $6,58 (1.004 ontvangers). Voornaam in campagne-onderwerpen: klikindex 1,17. | T05b, fase 2 |
| 4 | **K1** (cart 1, kookgerei) | A/B onderwerp | B = "{first_name}, we saved your cart (and 4 gifts)" tegen "Nothing on it to peel off". | Oude cart 1 "Hi {first_name}, we saved these for you": $2,43 tot $2,66, 2,8% klik op 71.417 ontvangers. Een productvoordeel als onderwerp van cart 1 is nooit getest. | Na T02 in cart (fase 2) |
| 5 | **C2** | A/B onderwerp | B = gift-framing: "Your order, with 4 gifts inside" tegen de PFAS-vraag "Has the pan in your cart actually been tested?". Body blijft het bewijs (rapport 25895). | Checkout 3 "Your Order with a Special Extra Bonus" klikte 2,9 tot 3,8% tegen 1,5 tot 2,2% voor de merkmail op dag 1; "We've cooked something for you!" $2,39. PFAS-onderwerpen in flows: $0,14 gewogen (n=3), in campagnes klikindex 0,88 als thema. | Fase 3 (checkout heeft in fase 1 en 2 al T01, T02, T03) |
| 6 | **P2** | Vast | Wissel A en B: "The one mistake that makes titanium stick" wordt A, "If you can do an egg, you can do anything" wordt B (of laat de test vallen). | Pan education 2 "The #1 mistake that makes titanium stick" 6,9% klik; campagne "Why Food Sticks" 7,18% klik, hoogste campagne ooit, RPR-index 4,36. | Bij export |
| 7 | **W2** | Vast + A/B | Afzendernaam "Benjamin from Siraat's Kitchen" (vast). A/B onderwerp: B = "A note from Benjamin" tegen "The pan nobody else was making". | Welcome 2 "A Note from Benjamin" (tekst) $0,72 en 2,6% klik, beter dan alle beeldmails op dag 3 tot 10 ($0,17 tot $0,65). Campagnes met afzender "Benjamin from Siraat": klikindex 2,04 (n=4). | Afzender bij export; onderwerp fase 3 (welcome heeft T01, T04) |
| 8 | **P3-pan** | A/B onderwerp + hero | B = "Put a lid on it" tegen "Which lid fits your pan?". Hero: deksel óp de pan, productfoto op hout (zoals RRHn5w). | Lid Launch aan pankopers: RPR $0,69, maandindex 6,94, 3,45% klik, 0,74% conversie, de beste cross-sell ooit. | T02 loopt op P3; onderwerp als tweede test in fase 2 |
| 9 | **P3-next, N1, R1-pan** | Vast | Check-in-vraag als A-onderwerp: "How is the pan treating you?" (P3-next nu B), "How's your pan at six months?" (N1, al A), "How's your pan doing?" (R1-pan, al A). | Post-purchase "We've got a quick question for you!" / "How's it going?": $0,77 en 8,2% klik, beste niet-transactionele PP-mail; Trustpilot "How was your experience?" 4,2% klik. Hier werkt de vraagvorm wél, omdat de vraag over hun eigen pan gaat. | Bij export (P3-next) |
| 10 | **W4-us/int** | Vast blok | "Who are you cooking for?" als klikbare quiz: drie knoppen (1 tot 2, 3 tot 4, family) die elk naar de juiste maat linken, in plaats van één knop. | Quizmail "We've got questions / How well will you be?": $0,22 in failure-to-launch tegen $0,04 tot $0,08 voor de 10 andere FTL-mails, $0,59 in welcome. Maatkeuze is het bezwaar van 15% (S8). | Bij volgende templateronde |
| 11 | **B2-notclicked** | A/B onderwerp + blok | B = "Why food sticks (and the 2-minute fix)" met het 3-stappenblok uit P2 (verwarmen, waterdruppel, olie) tegen "Week one, in their words". | "Why Food Sticks" 7,18% klik / index 4,36; Pan education 1 7,2% klik bij 0,27% uitschrijving. "Werkt titanium echt?" is het bezwaar van 15% (S8). Social proof als onderwerp: index 1,00 in campagnes, $0,17 in welcome. | T08 (lengte) loopt al op B2-notclicked; dit wordt fase 3 |
| 12 | **W3 (T07 hero)** | Variant voor de geplande hero-test | Hero B = pan in gebruik met eten en handen (flash-stijl), tegen het certificaatbeeld. | 4 van de 7 beeld-hero's in de top 10 plus de klikkampioen "Why Food Sticks" tonen de pan tijdens het koken; abstracte of documentbeelden alleen bij sales. | T07, fase 2 |
| 13 | **V1 / R2-VIP** | A/B formaat | B = kale tekstmail van Benjamin (4 tot 8 zinnen, één link met de code al toegepast), zelfde aanbod. | Tekstcampagnes: mediaan RPR-index 1,22 en minder uitschrijving (0,56% tegen 0,65%); 7/24 Benjamin-tekstmail aan de US: index 2,22 bij 0,34% uitschrijving; tariff note index 2,10 en 3,4% klik. | V1/N2 zijn stratum in T02; formaattest pas fase 3 |
| 14 | **R1-pan / R1-set** | Voorwaardelijk | Alleen als er echt iets nieuws is: onderwerp B "New since your last order: ..." met het nieuwe product als hero. | Winback "Serving Up New Must-Haves" $0,24 tegen $0,11 tot $0,24 voor "We Cut a Deal for You" (10%); launch-campagnes mediaan index 1,15, klikindex 1,24; crêpe-, wok- en deksellancering index 2,1 tot 6,9. | Bij de eerstvolgende productlancering |
| 15 | **Alle v4-onderwerpen** | Vaste regels | (a) Geen emoji. (b) Getal waar het kan ("4 gifts", "$70", "2 minutes", "75 years"). (c) Vraag vooral als die over hun eigen pan of cart gaat (#9); een algemene nieuwsgierigheidsvraag wint klik maar historisch geen omzet. (e) Geen tekenvervanging ("0ff", "BIack", "BestseIIers" uit de BFCM-mails). (d) Kort mag: 1 tot 3 woorden. | Emoji: RPR $0,086 tegen $0,141 (onderwerplab: -25% klik). Getal: klikindex 1,10 en uitschrijving 0,49% tegen 0,67%. Vraag: RPR-index 0,84 (n=13), klik wel hoger. Onderwerpen van 0 tot 2 woorden: index 1,11 (onderwerplab: kort +19% klik). | Toetsen in qa bij elke nieuwe mail |

Bevestigd zonder wijziging (v4 volgt de historische winnaar al):
- **K3 / C4**: "Last chance: your own 10% ends in 48 hours". Oude cart 3 "Last Call for 10% Off! / ends in 48 hours" verslaat de kale 10% van cart 2 in de hoofdflow met 40 tot 65% RPR (in de kleine Triple Pixel-variant gelijk) en heeft de laagste uitschrijving van de reeks.
- **P1-first**: bevestiging zonder founder note (oude founder-mails na aankoop 1,5 tot 2,4% uitschrijving).
- **P2-safe**: "When your pan arrives: the first egg" volgt Pan education 1 "Your Siraat Titanium Pan is about to arrive" (7,2% klik, 0,27% uitschrijving).
- **C3-s**: "$70 in gifts ship with your set" volgt de gift-framing van checkout 3.
- **Geen social-follow-mail, geen "community"-mail in checkout** (Happy Chef Club was de zwakste stap).

## Bestanden

| Bestand | Inhoud |
| --- | --- |
| `campaigns-all.csv` | Alle 384 campagnes: cijfers, onderwerp(en), preview, afzender, template-ID, kenmerken, thema, maandindex |
| `flow-messages-all.csv` | Alle 160 flowberichten: cijfers over beide vensters, onderwerp, preview, template-ID, status, groep, groepsindex |
| `top20-campaigns-rpr.csv`, `top20-campaigns-click.csv`, `worst10-campaigns-unsub.csv` | Ranglijsten campagnes (>= 1.000 ontvangers) |
| `top20-flowmessages-rpr.csv`, `top20-flowmessages-click.csv`, `worst10-flowmessages-unsub.csv` | Ranglijsten flowberichten |
| `patterns-campaigns.csv`, `patterns-flows.csv` | Groepsvergelijkingen per kenmerk |
| `scripts/` | Ophalen (`kl.py`, `campaigns.py`, `camp_report.py`, `flow_report.py`, `flow_meta.py`, `templates.py`), tabellen (`camp_table.py`, `flow_table.py`), kenmerken (`features.py`, `build_feat.py`, `themes.py`), patronen (`patterns.py`), render (`shot.js`). Draaien vanuit /tmp met `python3 -I`; schrijven naar /tmp/hist. |
