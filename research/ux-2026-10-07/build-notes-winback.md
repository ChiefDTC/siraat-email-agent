# Build notes winback (R1-pan, R1-set, R2, R2-VIP)

Datum: 7 oktober 2026. Herbouw volgens PLAYBOOK 10 en 11, referentie checkout C1. Bronnen: `klaviyo/templates/v3/winback/*.html`, previews in `previews/`, hero-register `content/media/hero-register/winback.csv`.

## Per mail

| Mail | Hero (kop / subregel / label / aanbodbalk) | Aanbod | Mobiel | Desktop |
| --- | --- | --- | --- | --- |
| R1-pan | "New pans, 10% off for you" / "Same titanium. Same 75-year warranty." / NEW SINCE YOUR LAST ORDER / EXTRA 10% OFF WITH HI10 · $70 IN GIFTS | HI10 (codebalk, hero, knoppen via /discount/HI10) | 3.362 px | 3.311 px |
| R1-set | "Your set, one step further" / "What's new, with 10% off for you." / FOR SET OWNERS / idem | HI10 | 3.414 px | 3.281 px |
| R2 | "10% off your next piece" / "Plus $70 in gifts with every order." / YOUR CODE · 72 HOURS / YOUR 10% CODE EXPIRES IN 72 HOURS | unieke code R2_10_72H, offerblok met deadline | 3.457 px | 3.371 px |
| R2-VIP | "A thank you: 15% off" / "Because you ordered more than once." / FOR OUR REGULARS · 72 HOURS / YOUR 15% CODE EXPIRES IN 72 HOURS | unieke code R2_VIP_15_72H, offerblok met deadline | 3.464 px | 3.377 px |

Blokvolgorde R1: codebalk · header · hero · knop · korte intro · productlijst (4, prijs en prijs met HI10) · knop · gifts · reviews · iconen · knop · Benjamin.
Blokvolgorde R2/R2-VIP: codebalk (unieke code) · header · hero · knop · offerblok (code, deadline, knop) · gifts · productlijst (3, prijs met code) · reviews · iconen · knop · Benjamin.
Knop en aanbod staan in alle vier binnen de eerste ~600 px op mobiel. Drie keer dezelfde primaire knop ("Shop with my 10%" / "Claim my 15%").

Productkaarten zijn een eigen inline lijst (beeld links, tekst rechts, prijs plus prijs na code in brick); op mobiel verdwijnt de omschrijving (`.pcd`) en wordt het beeld 88 px. Dit is inline in de mails geschreven, geen nieuw blok in partials.

## Coupons die nodig zijn (niet aangemaakt)

| Klaviyo-coupon | Korting | Geldig | Instellingen |
| --- | --- | --- | --- |
| `R2_10_72H` | 10% | 3 dagen na toewijzing | Shopify unique codes, prefix bijv. BACK-, 1 gebruik, 1 per klant, one-time purchase products |
| `R2_VIP_15_72H` | 15% | 3 dagen na toewijzing | idem, prefix bijv. VIP- |

(In 04-offer-strategy heten deze pools SK_WINBACK10_72H en SK_VIP15_72H; de mails gebruiken de namen uit de opdracht. Kies één naam en pas de tag aan als de pool anders heet.)

Let op: de coupon-tag staat 12 keer in elke R2-mail (codebalk, offerblok, alle knoppen, hero-link, productlinks), ook in de URL `/discount/{% coupon_code '...' %}?redirect=...`. Klaviyo hoort per ontvanger per bericht één code te geven; controleer in een test-send dat overal dezelfde code staat en dat er niet 12 codes per profiel uit de pool gaan. Zo niet: één keer de tag en de rest via een variabele, of alleen codeblok plus knoppen.

## Open punten voor Floris

1. **Prijs Pan Pro (R2):** Shopify zegt $134 met compare-at $439 (69 procent), de oude hero beloofde "Up to 50% off". De nieuwe R2 en R2-VIP noemen geen salepercentage en geen doorgestreepte prijs meer, alleen de prijs en de prijs met de code. Graag besluiten: klopt compare-at $439, of moet die naar een echte vorige prijs? Daarna kan de doorgestreepte prijs terug.
2. **6-delige set:** mails tonen $349 (besluit), Shopify-listing `titanium-hammered-pan-set-with-lids-6-pcs` staat op $399; $349 is de ongelijste BDAY SALE-variant. De link gaat naar de $399-listing. Floris beslist $349 of $399 in Shopify.
3. **"New" in R1:** alleen 2 Pans + 2 Lids is echt nieuw (okt 2026). Wok, crepe en deksel staan er als "what pan owners add next". R1 loopt 60 dagen na de order, dus "new" moet bij elke productlancering bijgewerkt worden.
4. **SEND-regel R2:** de oude regel "alleen versturen zolang up to 50% off live is" is vervallen, omdat de mail geen sale meer belooft. Wel: alleen versturen zolang de gift-stack ($70 + kans op de filter) loopt.
5. **Gift-waardes** ($15, $30, $25, $450) en de wekelijkse trekking: nog te bevestigen (zoals in de hele UX-ronde).
6. **HI10 aan bestaande klanten in R1:** volgens opdracht. Als de holdout-test (R2 met/zonder code) loopt, R1 eventueel zonder HI10 testen.
7. **Iconenrij US:** winback gaat naar alle markten; nu de US-rij (4e icoon PFAS lab tested). Bij een INT-split kan `{{BLOCK:icons-int}}`.
8. **Nieuwe beelden uploaden:** r1-pan-hero, r1-set-hero, r2-hero, r2-vip-hero, p-lid.jpg en de bestaande p-*.jpg staan nog niet in `assets/klaviyo-urls.txt`, dus er is nog geen `*.klaviyo.html` gebouwd. Na upload: urls toevoegen en opnieuw bouwen.

## Beelden

- R1-pan: Shopify Files `IMG_1253.jpg` (penne in de Pan Pro met deksel; deksel past bij de lid-upsell).
- R1-set: Shopify Files `Pan_LF_13.jpg` (pannen, planken en utensils op marmer; laat zien wat een set aanvult).
- R2: hp-shoot `P05-A_Stovetop_Pot`.
- R2-VIP: Shopify Files `26742171-...jpg` (utensils, deksel en trivet op zwart).
- Productbeeld deksel: Shopify-productfoto Stainless Steel Lid, kopie in `assets/src/stainless-steel-lid-packshot.jpg`, vierkant gemaakt als `assets/p-lid.jpg`.
Geen van deze beelden staat in hp-shoot P02-P12 of in chef-video. `content/assets/index.csv` kolom used_in niet bijgewerkt (buiten mijn grenzen).

## Reviews (5 sterren, max 120 tekens)

R1-pan Chetan G. + Marlene · R1-set Pam B. + David I. · R2 Tyrone B. + Virginie M. · R2-VIP Olwen T. + David F. (herhaalkopers). Alleen spaties voor een punt weggehaald.
