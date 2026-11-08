# Te agressieve copy voor alle live flows (urgentie-sprint, 8 nov 2026)

Rol: FLOWS-AGRESSIEF. Floris wil per flow een bewust te harde baseline ('ends tonight', 'last chance', 'order now', minuten, use it or lose it) die hij per flow met de hand afzwakt. Doel: de klant denkt 'ik moet nu kopen'. Alles alleen gelezen en geschreven: niets in Klaviyo of Shopify gewijzigd, niets verstuurd, geen testmails. Echte BF-code nergens in deze map (placeholder BFCODE); de code in de live templates is bij het uitlezen vervangen.

Bronnen: BRIEF.md, copy-agressief/copy-agressief.md (methode 'waar als' + risico, lijst 'Smooche doet dit, wij niet'), research/plannen/2026-11-urgentie.md, CLAUDE.md, DECISIONS.md, PLAYBOOK.md. Klaviyo read-only via kl.py: `GET /api/flows?filter=equals(status,"live")` (37 live flows), per flow `additional-fields[flow]=definition` (alle stappen, vertragingen, takken, onderwerp, preview, template), `GET /api/templates/{id}` (133 templates, hero-alt en knoppen), `POST /api/flow-values-reports` 25 okt tot 8 nov 2026 gegroepeerd op flow_id en flow_message_id, conversie RSNxYV.

Omvang: 26 flows, 87 mails (varianten met dezelfde copy samengenomen, oude armen met 0% instroom niet; 5 voorstellen voor nieuwe herinneringsstappen), 784 regels copy, elk met 'waar als' en risico: 614 groen, 141 oranje, 29 rood. In de hero-regels staat '|' voor de regelbreuk tussen kop en subregel. Per flow een bestand `<flowid>-<naam>.md`; alles machineleesbaar in `flows-agressief.json` (voorwaarden voluit per regel).

## 1. Welke flows winnen het meest bij urgentie

Rangorde op omzet per week (ontvangers per week x RPR, laatste 14 dagen), gecorrigeerd voor de hefboom: is er in die flow een deadline die vandaag al echt is (unieke 48-uurscode, echte open checkout) of alleen het BF-einde op 30 nov.

| # | Flow | Ontvangers per week | RPR 14 d | Omzet per week | Klik | Hefboom | Waarom | Bestand |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | T4a5Mk v4 · Welcome | 23.935 | $1,04 | $24.960 | 2,0% | hoog | grootste volume; alleen BF-einde 30 nov en gifts, datumblok 28 tot 30 nov | [T4a5Mk-welcome.md](T4a5Mk-welcome.md) |
| 2 | TZG9Mx v4 · Cart abandonment | 4.949 | $2,75 | $13.628 | 3,7% | hoog | echte 48-uurscode K3 + echte cart; nieuwe +44 u-herinnering | [TZG9Mx-cart.md](TZG9Mx-cart.md) |
| 3 | Rn556d v4 · BFCM Welcome · direct A/B (hoofdlijst) | 3.584 | $3,49 | $12.495 | 4,1% | hoog | BF-einde en gifts; datumblok 30 nov | [Rn556d-bf-direct.md](Rn556d-bf-direct.md) |
| 4 | QUBUQV v4 · Checkout abandonment | 2.404 | $4,77 | $11.461 | 3,7% | hoog | echte 48-uurscode C4 + echte open checkout; nieuwe +44 u-herinnering | [QUBUQV-checkout.md](QUBUQV-checkout.md) |
| 5 | WdRz5k v4 · Browse abandonment | 6.338 | $0,88 | $5.548 | 2,9% | midden | echte 48-uurscode B2; lage RPR, klikprobleem | [WdRz5k-browse.md](WdRz5k-browse.md) |
| 6 | X3ySuU v4 · Post-purchase | 4.008 | $0,55 | $2.219 | 5,7% | midden | BF-einde; 'before it ships' pas na order-edit-besluit | [X3ySuU-post-purchase.md](X3ySuU-post-purchase.md) |
| 7 | YyaMjx FREE E - GUIDE | 2.224 | $0,64 | $1.417 | 7,4% | laag | hoge klik, geen eigen deadline | [YyaMjx-e-guide.md](YyaMjx-e-guide.md) |
| 8 | WsQDYu BIS / Back in Stock Waitlist | 50 | $21,69 | $1.095 | 5,9% | midden | hoogste RPR, klein volume; echte restock + BF-prijs | [WsQDYu-back-in-stock.md](WsQDYu-back-in-stock.md) |
| 9 | VLGhbR v4 · Site abandonment | 1.389 | $0,53 | $740 | 1,9% | laag | BF-einde; klein volume | [VLGhbR-site.md](VLGhbR-site.md) |
| 10 | T2SmtR EB / Failure to launch | 13.763 | $0,03 | $418 | 0,4% | midden | groot volume, $0,03; hero zegt nog Prime Time 56%: eerst die claim vervangen | [T2SmtR-failure-to-launch.md](T2SmtR-failure-to-launch.md) |
| 11 | QNZyEb v4 · Browse abandonment · Triple Pixel | 959 | $0,34 | $324 | 3,1% | laag | zelfde als WdRz5k, klein volume | [QNZyEb-browse-triple-pixel.md](QNZyEb-browse-triple-pixel.md) |
| 12 | UEfh4h EB / Customer Winback / 5/8/25 | 3.246 | $0,07 | $218 | 0,4% | laag | oude flow tot 14 dec; nep-risico Email #3 eerst controleren | [UEfh4h-winback-oud.md](UEfh4h-winback-oud.md) |
| 13 | R22pzb AFF S1 · Activatie na bezorging | 242 | $0,81 | $196 | 0,4% | laag | geen eigen deadline; alleen BF-einde | [R22pzb-affiliate-activatie.md](R22pzb-affiliate-activatie.md) |
| 14 | Wzz6xC v4 · Sunset · kept | 54 | $3,46 | $187 | 6,5% | laag | geen eigen deadline; alleen BF-einde | [Wzz6xC-sunset-kept.md](Wzz6xC-sunset-kept.md) |
| 15 | YwsKcf v4 · Mystery Gift | 631 | $0,13 | $85 | 4,0% | laag | geen eigen deadline; alleen BF-einde | [YwsKcf-mystery-gift.md](YwsKcf-mystery-gift.md) |
| 16 | TbYQmX v4 · Sunset | 8.517 | $0,01 | $77 | 0,4% | laag | afscheid is de enige echte deadline; $0,009 | [TbYQmX-sunset.md](TbYQmX-sunset.md) |
| 17 | VPixnJ v4 · UGC first egg | 214 | $0,36 | $77 | 0,0% | laag | geen eigen deadline; alleen BF-einde | [VPixnJ-ugc-first-egg.md](VPixnJ-ugc-first-egg.md) |
| 18 | VQ93sx v4 · Post-purchase · levering | 339 | $0,18 | $62 | 6,0% | laag | geen eigen deadline; alleen BF-einde | [VQ93sx-post-purchase-levering.md](VQ93sx-post-purchase-levering.md) |
| 19 | YqKCmH v4 · BF follow-up BF-W2/BF-W3 · TEST (draft) | 0 | $0,00 | $0 | 0,0% | midden | 0 ontvangers (testlijst); klaar voor hoofdlijst | [YqKCmH-bf-follow-up.md](YqKCmH-bf-follow-up.md) |
| 20 | Vd38Vc v4 · Post-purchase upsell 50% test · TEST (draft) | 0 | $0,00 | $0 | 0,0% | midden | 0 ontvangers (test); pp-addon is de enige plek waar 'before your order ships' kan kloppen | [Vd38Vc-post-purchase-upsell.md](Vd38Vc-post-purchase-upsell.md) |
| 21 | R9dcdY v4 · P2 vangnet · Fulfilled +12d (geen Delivered) | 0 | $0,00 | $0 | 0,0% | laag | geen eigen deadline; alleen BF-einde | [R9dcdY-p2-vangnet.md](R9dcdY-p2-vangnet.md) |
| 22 | UyFc78 v4 · Winback | 0 | $0,00 | $0 | 0,0% | laag | nog geen ontvangers (45 en 75 dagen); BF-einde | [UyFc78-winback.md](UyFc78-winback.md) |
| 23 | XbYT7T v4 · Anniversary | 0 | $0,00 | $0 | 0,0% | laag | echte 7-dagen-code, maar bijna geen ontvangers vóór 30 nov | [XbYT7T-anniversary.md](XbYT7T-anniversary.md) |
| 24 | VTkxFL v4 · VIP | 3 | $0,00 | $0 | 0,0% | laag | geen eigen deadline; alleen BF-einde | [VTkxFL-vip.md](VTkxFL-vip.md) |
| 25 | YhQJdb AFF S1 vangnet · Fulfilled +12d (geen Postflows) | 0 | $0,00 | $0 | 0,0% | laag | geen eigen deadline; alleen BF-einde | [YhQJdb-affiliate-vangnet.md](YhQJdb-affiliate-vangnet.md) |
| 26 | WTY94m v4 · Abonnement S1 (Loop, test 20%) | 130 | $0,00 | $0 | 10,4% | laag | echte volgende afschrijfdatum uit Loop ({{NEXT_CHARGE}}) is de enige deadline | [WTY94m-abonnement-s1.md](WTY94m-abonnement-s1.md) |

## 2. Eerst veranderen (volgorde)

1. **Checkout QUBUQV** ($4,77 per ontvanger, C1 zelfs $10,21). CODE · C4 nu al: 'Your own 10% expires in 48 hours' (groen, code vervalt echt). Nieuwe stap C4-REM op +44 uur ('Your 10% expires in {{HOURS_LEFT}} hours'). C1-onderwerp 'Your checkout is still open: extra 10% applied'. Op 30 nov het datumblok 'Your checkout prices go up at MIDNIGHT ⏰'.
2. **Cart TZG9Mx** ($2,75, 4.949 per week). Zelfde opbouw: K1 'Your cart is still open: extra 10% + 5 free gifts', CODE · K3 '48 hours', nieuwe K3-REM, en K2-NEW 'Our warranty runs 75 years. Your extra 10% runs out {{DEADLINE_SHORT}}.'
3. **Welcome T4a5Mk + BF-direct Rn556d** (samen 27.500 per week, grootste omzetbron). Vandaag alle [BFEND]-regels ('ends Nov 30', '5 free gifts end Nov 30'); vanaf 28 nov de [BF48]/[BF30]-onderwerpen via datumblok of handmatige omzetting. W5 is echt de laatste welkomstmail: 'Last welcome email: up to 70% off ends {{DEADLINE_SHORT}}'.
4. **Browse WdRz5k** (6.338 per week, $0,88). CODE · B2 met '48 hours' plus B2-REM; B1 'The pan you looked at: extra 10% until {{DEADLINE_SHORT}}'. QNZyEb meteen dezelfde copy (samenvoegen staat op BACKLOG 3).
5. **Failure to launch T2SmtR** (13.763 per week, $0,03): eerst de onware hero 'SIRAAT PRIME TIME SALE | UP TO 56% OFF' vervangen door BF met einddatum; dat is geen afzwakking maar een correctie.
6. Pas daarna: post-purchase (X3ySuU P1, Vd38Vc pp-addon) met 'add it before your order ships', alleen als Floris een order-edit-link of samenvoegen via support bevestigt; tot die tijd de groene variant.

## 3. De 8 sterkste onderwerpen

| # | Flow | Mail | Onderwerp | Risico | Waar als |
| --- | --- | --- | --- | --- | --- |
| 1 | QUBUQV | CODE · C4 | Your own 10% expires in 48 hours | groen | [CODE48]: de code vervalt echt 48 uur na uitgifte |
| 2 | QUBUQV | C1 | Your checkout prices go up at MIDNIGHT ⏰ | oranje | [BF30] + [PRICEUP]: alleen op 30 nov |
| 3 | TZG9Mx | K1 | Your cart is still open: extra 10% + 5 free gifts | groen | [CART] + [BFCODE] + [GIFTS5] |
| 4 | TZG9Mx | NIEUW · K3-REM | Your 10% expires in {{HOURS_LEFT}} hours | groen | [CODEREM]: nieuwe stap op +44 uur |
| 5 | T4a5Mk | W1 | Up to 70% off + 5 free gifts. ENDS {{DEADLINE_SHORT}} ⏰ | oranje | [SALE70] + [GIFTS5] + [BFEND] |
| 6 | Rn556d | BF-W1 direct | ENDS TONIGHT: up to 70% off, no code needed ⏰ | oranje | [BF30] |
| 7 | TZG9Mx | K2-NEW | Our warranty runs 75 years. Your extra 10% runs out {{DEADLINE_SHORT}}. | groen | [W75] + [BFCODE] + [BFEND] |
| 8 | TbYQmX | SUNSET · S2 | Last email from me, and the last one at this price | groen | [LASTFLOW] + [SUNSET]: na onderdrukking echt de laatste |

## 4. Zo maak je 'tonight' waar in een flow

- Een flowmail gaat op elk uur van elke dag uit; 'ends tonight' is dus alleen waar op de dag dat er echt iets eindigt. Voor BF is dat 30 nov (eindtijd per regio, zie scheduling/kalender.md).
- Twee manieren: (a) datumblok in onderwerp, preview en hero (`{% today %}`-vergelijking; per markt testen, ook in het onderwerp), of (b) Floris zet op 30 nov 00:00 de onderwerpen van de abandonment- en welkomstmails om (PATCH flow-action) en op 1 dec terug. Optie (b) is eenvoudiger en goed te controleren.
- De enige deadlines die vandaag al per profiel echt zijn: de unieke codes K3_10_48H, C4_10_48H, B2_10_48H (48 uur) en SK_ANNIV15_7D (7 dagen). Daar mag 'expires in 48 hours' vandaag live. 'Expires tonight' pas in een herinneringsstap vlak voor het einde (nieuwe stappen K3-REM, C4-REM, B2-REM, N2-REM).
- {{MINUTES_LEFT}} en 'Order now: 60 minutes left' zijn in flows altijd rood: alleen met een live countdown-GIF die naar de echte eindtijd telt.

## 5. Bevindingen in de live flows (los van de nieuwe copy)

- **'4 gifts' staat nog in bijna alle v4-flows** (cart, checkout, browse, post-purchase, anniversary, BF follow-up). Sinds 7 nov zijn het 5 gifts; elke regel hierboven gaat uit van 5 ([GIFTS5]).
- **Failure to launch T2SmtR en oude winback UEfh4h**: hero 'SIRAAT PRIME TIME SALE | UP TO 56% OFF' is verouderd en nu onwaar.
- **UEfh4h Email #3** heeft een beeld 'Your 10% Off Ends Tonight' zonder zichtbare code in de HTML. Controleren of de 10% uit Email #2 echt na een dag vervalt; zo niet, dan is dit nu een nep-deadline live.
- **Back in stock WsQDYu BIS 2**: preview 'You're first in line, limited restock' (met gedachtestreepje in Klaviyo) is een schaarsteclaim zonder getal.
- **Anniversary XbYT7T N2**: 'Your 4 gifts end when the fall sale ends' is achterhaald.
- **Checkout C1 tot C4**: 'Your 4 gifts are still pending' ligt tegen het verboden 'pending order' aan; voorstel '5 free gifts are on this checkout'.
- **P1-FIRST** onderwerp 'Good call. Here's what's coming.' gebruikt 'coming' (verboden in deze sprint).
- **YqKCmH en Vd38Vc** staan live maar hadden 0 ontvangers in 14 dagen (test); **UyFc78 winback** en **XbYT7T anniversary** nog geen (delays 45 tot 365 dagen).
- CODE · R2, CODE · R2-VIP, CODE · P3 en CODE · V1 hebben geen coupon in de template: daar bestaat nu geen code-deadline.

## 6. Verleidelijk, maar nooit waar voor Siraat

Deze regels staan bewust niet in de flowbestanden als bruikbare copy (ook niet als rood), omdat ze zonder verzonnen feiten nooit kloppen. Per flow staat de lijst ook onderaan het bestand.

| Regel | Waarom niet |
| --- | --- |
| Your cart is reserved / we're holding your cart / price held | Verboden (DECISIONS 1 nov, BRIEF). De Shopify-cart houdt geen prijs vast. |
| Your cart expires at midnight | De cart vervalt niet. Wel waar op 30 nov: 'Your cart prices go up at midnight' ([BF30] + [PRICEUP]). |
| Your order is pending / will be canceled | Er bestaat geen order; nep-orderstatus (FTC Act sectie 5, CAN-SPAM). |
| Only 3 left / almost sold out | Geen echte voorraaddata per variant in de flow; valse schaarste. |
| We extended your discount 24 hours, it cannot be extended again | Verzonnen verlenging; BRIEF verbiedt 'no extensions'. |
| Your code expires tonight (in een 48-uurs codemail op het moment van uitgifte) | Op het uitgiftemoment zijn het nog 48 uur. Alleen waar in de nieuwe herinneringsstap [CODEREM]. |
| Your order is on hold until you add the lid | Verzonnen orderstatus. |
| Add it to your order (zonder order-edit of samenvoegen) | Wordt een tweede order; alleen waar met [UNSHIP]. |
| Last chance before your box is sealed | Nep-procesclaim. |
| VIP ONLY: up to 70% off | De sale is voor iedereen; alleen met unieke VIP-code [VIPCODE]. |
| HI10 expires tonight / welcome price today only | HI10 heeft geen einddatum; er is geen welkomstprijs per profiel. |
| You won! / You're a winner | Alia geeft een kans, geen winst. |
| FINAL NOTICE / account closure | Klinkt als phishing; er sluit niets. |
| Only {{N}} left / selling out in hours (zonder echte voorraadvariabele) | Valse schaarste. |
| Your link expires tonight / double commission ends tonight (affiliate) | Bestaat niet. |
| Your warranty is expiring / register or lose your warranty | Verzonnen. |
| Up to 56% off (Prime Time) | Verlopen actie. |

## 7. Voorwaarden (codes in de kolom 'waar als')

- **[AFF]** Snowball-link en 15/15 zijn actief voor dit profiel
- **[AFFDL]** NIEUW: Floris zet een echte tijdsgebonden affiliate-actie in Snowball (bv. hogere commissie tot {{DEADLINE}}); bestaat nu niet
- **[AFFSTACK]** de 15% vriendenkorting stapelt in Shopify echt op de BF-saleprijs (combinatie-instelling controleren); anders niet zeggen
- **[ANNIV7]** SK_ANNIV15_7D (one use) vervalt echt 7 dagen na uitgifte; template toont 'ENDS' met days_later:7, {{DEADLINE}} = die datum
- **[BF30]** de mail gaat uit op 30 nov (laatste BF-dag) en saleprijs, BFCODE en gifts stoppen echt op {{DEADLINE}}. In een flow alleen via een datumblok in onderwerp en hero ({% today %}-vergelijking, getest) of doordat Floris op 30 nov de onderwerpen omzet (PATCH flow-action) en op 1 dec terugzet; andere dagen valt de regel terug op de [BFEND]-versie
- **[BF48]** de mail gaat uit op 29 of 30 nov (laatste 48 uur van BF), zelfde datumblok als [BF30]; 'last chance' en 'final hours' alleen dan
- **[BFCODE]** BFCODE (extra 10% bovenop de sale, alleen abandonment) staat in de knoplink en werkt op het verzendmoment; BFCODE stopt met BF, dus de einddatum is [BFEND]
- **[BFEND]** Black Friday eindigt echt op 30 nov 23:59 (eindtijd per regio uit scheduling/kalender.md: US 23:59 PT of ET zoals genoemd, INT CET/AEDT); {{DEADLINE}} = die datum met tijdzone ('Nov 30 at 11:59 PM ET'), {{DEADLINE_SHORT}} = 'Nov 30'. Nooit 'tonight' of 'midnight' behalve samen met [BF30]
- **[BIS]** het product staat op het verzendmoment echt weer op voorraad (BIS-trigger, catalog unpublished=cancel)
- **[BISFIRST]** de waitlist-mail gaat echt uit vóór een campagne of algemene aankondiging van deze restock
- **[CART]** echte Added to Cart van dit profiel en geen order sinds flowstart (flowfilter RSNxYV = 0 staat erin); de knop herstelt de cart
- **[CHECKOUT]** echte Started Checkout van dit profiel en geen order sinds flowstart (flowfilter staat erin); knop gaat naar de checkout-URL
- **[CODE48]** unieke Klaviyo-code (K3_10_48H, C4_10_48H of B2_10_48H, one use) vervalt in Shopify echt 48 uur na uitgifte; {{DEADLINE}} = days_later:2 met het uur van de coupon-instelling (template zegt nu 'expires on the morning of', dus uur controleren); {{DEADLINE_SHORT}} = weekdag
- **[CODEREM]** NIEUWE flowstap (bestaat nu niet): herinnering op uitgifte + 44 tot 46 uur, alleen als de code ongebruikt is (Placed Order = 0 sinds flowstart); {{HOURS_LEFT}} = echte uren tot de coupon-einde
- **[GIFTS5]** de gift-app voegt nu echt 5 gifts toe aan elke order (mystery gift, free shipping, plastic-free e-book, Favorites cookbook, kans op een PFAS water filter); '$555 value' alleen in US-mails; huidige flowtemplates zeggen nog '4 gifts' en moeten mee
- **[GIFTSEND]** de 5 gifts worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app uit); nu is dat 30 nov, dus zelfde datum als [BFEND]
- **[HI10]** HI10 werkt bovenop de sale, one use per klant; HI10 heeft geen einddatum, dus nooit 'HI10 expires'
- **[LASTFLOW]** dit is echt de laatste mail van deze flow voor dit profiel (geen stap meer erna)
- **[LASTPRICE]** na deze mail krijgt dit profiel geen mail meer met deze prijs: alleen waar op 30 nov ([BF30]) of als het profiel tot 30 nov uit alle BF-campagnes is gesloten. Anders misleidend, want campagnes lopen door
- **[MINS]** {{MINUTES_LEFT}} alleen naast een live countdown-GIF (Sendtric/NiftyImages) die naar de echte backend-eindtijd telt en daarna ENDED toont; als statische tekst nooit
- **[NOW]** de flowmail gaat uit op het moment dat de trigger valt (geen 'local time'-verschuiving), dus relatieve tijd klopt
- **[PRICE144]** Pan Pro Standard staat in de BF-sale echt op $144 (US, Shopify)
- **[PRICEUP]** de producten in deze cart/checkout gaan op {{DEADLINE}} echt terug naar de normale prijs (einde BF). De Shopify-cart zelf vervalt niet en houdt geen prijs vast; de regel gaat over de prijs, nooit over de cart
- **[RETURN30]** 30 dagen retour vanaf bezorging, ongebruikt (DECISIONS 1 okt)
- **[REVIEW]** de geciteerde review staat letterlijk en geverifieerd in de huidige template (naam en ID)
- **[SALE70]** de BF-sale (tot 70% off, zonder code op de site) staat live op het verzendmoment; 'up to', want niet elk product heeft 70%
- **[SHIPSEP]** een tweede order wordt los verzonden en krijgt zelf gratis verzending en de gifts; de copy belooft niet dat het in hetzelfde pakket zit
- **[STOCK6]** Floris bevestigt in de backend dat de nieuwe voorraad 6-pcs en/of 12-pcs net binnen is ('Just arrived and selling fast', DECISIONS 1 nov); nooit een getal zonder echte voorraaddata
- **[STOCKNUM]** echte voorraad van deze variant op het verzendmoment staat als variabele {{UNITS}} in de mail (catalogusfeed of Shopify-voorraad); een verzonnen getal of 'selling out' zonder data is nepschaarste
- **[SUB]** Loop-abonnement met 20% op elke levering is actief
- **[SUBNEXT]** {{NEXT_CHARGE}} = echte volgende afschrijfdatum uit Loop voor dit profiel; overslaan of opzeggen kan echt tot die datum
- **[SUNSET]** het profiel wordt na S2 zonder klik echt onderdrukt of uit de marketinglijst gehaald (flow-actie of segmentregel, controleren)
- **[SUPPORTMERGE]** support (Gorgias) kan een tweede order echt samenvoegen met een nog niet verzonden eerste order; Floris bevestigt
- **[UGC15]** de 15% wordt echt na een foto-reply gestuurd; een einddatum op de 15% bestaat nu niet, dus deadline alleen via de sale [BFEND]
- **[UNSHIP]** de order van dit profiel staat op het verzendmoment nog op unfulfilled (verzendfilter Fulfilled Order = 0 sinds flowstart) EN er bestaat een echte manier om toe te voegen aan dezelfde zending (order-edit-link of supportteam voegt samen vóór fulfillment, getest). Zonder dat mechanisme niet waar
- **[VIP2]** profiel heeft echt 2 of meer orders (flowtrigger VIP)
- **[VIPCODE]** NIEUW: unieke VIP-code per profiel (DECISIONS 8 okt: VIP krijgt 15%) met echte einddatum {{DEADLINE}}, alleen naar dit segment; CODE V1 heeft nu geen coupon in de template
- **[W75]** 75 jaar garantie (DECISIONS 1 okt)

## 8. Overgeslagen flows

| Flow | Naam | Reden |
| --- | --- | --- |
| TLHht3 | Shipment Exception Notification (to CS) | interne melding |
| UcGzaL | Delivery Attempt Failed Notification (to CS) | interne melding |
| Y4a7fJ | Ready for Pickup Notification (to CS) | interne melding, draft |
| TkV5DY | AFF S5b · Uitbetaling | service: uitbetaling aan affiliate |
| Yp6sKv | AFF S5a · Verkoopmelding | service: verkoopmelding aan affiliate |
| UYALJ8 | EB - E-Gift Card | transactioneel: levering cadeaubon |
| Wn2tsq | EB | Pan Flash Buyers | service: 'Credit or Refund?' voor flash-kopers |
| T5riz5 | Review request · Delivered +14d (Postflows) | reviewverzoek; urgentie past niet en kan FTC-reviewregels raken |
| TF2B5x | Review request · Delivered +14d (ShipBob) | reviewverzoek |
| TvfJYU | Review request · fallback Fulfilled +21d | reviewverzoek |
| XzHrez | Review request · Delivered +14d (Siraat DS) | reviewverzoek |

## 9. Controle

- Geen em dash of en dash in deze map (script-check); gedachtestreepjes uit Klaviyo-namen bij het uitlezen vervangen.
- Geen 'next batch', 'reserve', 'coming', 'pending', 'purifier', 'lifetime', 'shop now', 'free filter', 'price held' of 'no extensions' in de nieuwe copy (script-check; alleen in citaten van huidige copy en in de lijst hierboven).
- INT-mails zonder valutateken; '$555 value' en '$144' alleen in US-mails.
- Merkfeiten: 5 free gifts, oprichter Benjamin, 30-day returns, 75-year warranty, 100,000+ customers.
