# A/B Q4 · 08 · Stijl- en contentaudit van alle live flowmails (28 okt 2026)

Vraag Floris: vóór Black Friday ook stijl en content van de live flowmails verbeteren. Dit is alleen een audit. Er is niets aangepast in Klaviyo, Shopify, Figma of in de mailbronnen. Er staat geen klantdata in dit document.

Regels waartegen getoetst is: CLAUDE.md (lockup, vaste header en footer behalve affiliate en Mystery, Benjamin, 30 dagen retour, 75 jaar garantie, 100,000+, geen gedachtestreepje), DECISIONS.md, PLAYBOOK.md (10, 11, 12), de skills siraat-direct-response en siraat-flash-style, en de plannen in 00 tot en met 05.

---

## 0. Samenvatting voor Floris

1. **Het v4-systeem staat er goed.** Elke v4-mail heeft dezelfde knop, dezelfde kleuren, de lockup in de header, een friction reducer onder de knop, echte reviews en geen gedachtestreepje. Live en repo zijn gelijk (sectie 2). Het merk is herkenbaar en de claims kloppen.
2. **De grootste schade zit buiten v4.** Drie oude flows versturen nog elke dag. Het gaat om de oude winback `UEfh4h` (ongeveer 470 mails per dag), vier live mails in Failure to launch `T2SmtR` en de FREE E-GUIDE `YyaMjx`. Daarin staan "100-DAY TRIAL", "FREE RETURNS", "Lifetime Guarantee", "Heat safe up to 548C/1000F", "45% off", "Your 10% Off Ends Tonight" met code GOODFOOD (onwaar) en een microplastics-angsthook. Dat zijn precies de zinnen die DECISIONS (1 okt) verbiedt.
3. **Over drie dagen is de copy in ongeveer 45 live varianten onwaar.** In checkout, cart, browse, post-purchase P3, winback, VIP en anniversary staat "Your 4 gifts end when the fall sale ends". De gifts lopen in november door (DECISIONS 19 okt). Daarnaast staan "This month" en "THE FALL SALE" in C3-P, en "Buy 2, get 4 free" voor $299 in welcome, site en checkout. Ook de setprijs voor november is nog open.
4. **Op mobiel staat de knop in checkout, cart en browse net onder de vouw.** Dit is gemeten op 375 x 667 px. Op de mobiele kop gaat 168 px aan merkchroom op (codebalk 44, header 79, aanbodbalk 45). Daarna komen een hero van 281 px en de cartkaart. De knop begint daardoor op 694 tot 896 px. K1, de mail met 55% van de cartomzet, is het ergst: de knop begint op 972 px, omdat de cartkaart een productfoto van 300 px toont.
5. **De mails zijn lang voor wat ze moeten doen.** Checkout- en cartmails hebben 250 tot 345 woorden en 3,5 tot 4,6 schermen. De skill vraagt voor most-aware lezers 60 tot 180 woorden. Een gifts-blok staat er vaak twee keer in, plus drie reviews, een vergelijking en een aanbodblok. Ter vergelijking: Our Place gebruikt gemiddeld 44 woorden per mail en Made In 153 (Email Love).
6. **Er zijn drie kleine directe fixes.** De affiliate-aankondiging zegt nog "15% off their first order", terwijl het besluit van 22 okt zegt dat de korting voor alle klanten geldt. Er zijn vier verschillende afzendernamen. De review-flows gebruiken "SiraatsKitchen", zonder apostrof. De grijze hulptekst #727272 op crème haalt 4,48:1, net onder de AA-norm.

---

## 1. Hoe gemeten

- **Live versies.** Ik heb de definities van alle 29 live flows en de 137 gekoppelde templates alleen lezend opgehaald met de Klaviyo-helper. De API-key is niet geprint. Opslag: scratchpad `audit08/live/`.
- **Rendering.** Elke unieke live template is gerenderd met Django (`research/tailoring/test/render.py`) op een US-voorbeeldevent: `co_x_standard` (checkout), `atc_x_standard` (cart), `vp_x_standard` (browse en TP), `po_x_standard` (post-purchase, winback, VIP, anniversary, review, Mystery, affiliate), en zonder event voor welcome, site, sunset, UGC en FTL. Daarna volgde Chromium op **375 x 667 px**, net als de route van 23 okt (networkidle, volle pagina).
  - 667 px is ongeveer wat iOS Mail en de Gmail-app op een iPhone van 6,1 inch tonen, na de app-balken.
  - De oude templates gaven een Django-fout op de Klaviyo-filter `index`. Die zijn gerenderd met de tags weggehaald. Lege productbeelden in de oude winback zijn dus een artefact van die render.
- **Woorden.** Ik heb alle zichtbare woorden boven de footer geteld, dus inclusief reviews, labels, cartregels en friction reducers. De eigenlijke copy is ongeveer 60 tot 70% daarvan.
- **Schermen.** De hoogte tot de footer gedeeld door 667.
- **Contrast.** Berekend op de berekende kleur tegen de achtergrondcel.
- **Footer-links.** Unsubscribe, voorkeuren en webversie zijn #111111 op #282828. Dat is een bewuste keuze van Floris en telt niet mee.
- **Vergelijking met concurrenten.** De inbox-tijdlijn (`research/concurrenten/overzicht.md`, dag 16), plus Email Love. Our Place en Made In heb ik met brand insights en recente mails bekeken ("Double Major", "One Less Worry", "What Our Co-Founder, Jake, Actually Cooks With", "The Easiest Way to Keep Your Pans Looking New"). Van Caraway en HexClad staan alleen oudere mails in Email Love; voor die twee leunt dit document op de eigen inbox. WebSearch leverde geen e-mailteardowns op. Wel vond ik een teardown van de HexClad-landingspagina: daar werd het onderscheidende punt onder de korting begraven, en dat is hier ook een les.

---

## 2. Live tegenover repo

| Groep | Aantal live templates | Uitkomst |
|---|---|---|
| v4-flows (welcome, checkout, cart, browse, TP, site, post-purchase, levering, winback, sunset, kept, VIP, anniversary, UGC), affiliate (S1, S5a, S5b), Mystery (M1 tot M3), review (XzHrez A/B, TvfJYU) | 112 acties, 63 unieke bronnen | **Gelijk aan de repo.** Zichtbare tekst, `src`, `href`, `alt` en `bgcolor` zijn identiek aan `klaviyo/templates/v3/**/*.klaviyo.html`. Het enige verschil is de CSS-opmaak in `<style>`: Klaviyo herschrijft spaties, de volgorde en `#FFFFFF` naar `#FFF`. De regels zelf zijn gelijk. |
| Welke bron live staat | | K1 gebruikt `cart/k1-v2.klaviyo.html`, niet `k1.html`. W1-variant B gebruikt `welcome/w1-v3`. Niet live staan `welcome/w1-b`, `w1-v2`, `cart/k1`, `checkout/c4-int*`, `c4-us*` en Mystery M4 (Draft). |
| Live zonder bron in de repo | 10 mails | De oude winback `UEfh4h` (4 mails), FTL `T2SmtR` (4 mails live, 6 op Draft sinds 28 okt), FREE E-GUIDE `S2EMYW` en Pan Flash Buyers `Wn2tsq` mail 2 (service, niet beoordeeld). Daarnaast versturen de Old-armen in welcome nog tot ongeveer 30 okt (Old Welcome 6 tot 8). |
| Previews in de repo | | Een paar `-preview.html` en PNG's zijn ouder dan de `.klaviyo.html` (voorbeeld: `checkout/c1-preview.html` 9 okt 15:09 tegenover `c1.klaviyo.html` 16:36). Voor deze audit heb ik daarom de live HTML zelf gerenderd. |

Geen verschil in content tussen live en repo. Wel draaien er 10 live mails waarvan de bron alleen in Klaviyo bestaat. Daar zitten de grootste overtredingen.

---

## 3. Meetwerk per mail (375 x 667 px, US)

Knop boven de vouw betekent dat de onderkant van de eerste primaire knop op of boven 667 px ligt.

| Mail | Hoogte tot footer (px) | Schermen | Woorden | Hero-hoogte | Eerste knop (px) | Boven vouw |
|---|---|---|---|---|---|---|
| W0 | 2.726 | 4,1 | 286 | 375 | 474-530 | ja |
| W1 (A) | 2.899 | 4,3 | 315 | 375 | 518-574 | ja |
| W1 (B, v3) | 3.066 | 4,6 | 327 | 248 (lager) | 471-527 | ja |
| W2 | 2.045 | 3,1 | 371 | geen | geen (P.S.-link) | n.v.t. |
| W3 | 2.975 | 4,5 | 322 | 375 | 518-574 | ja |
| W4-US / INT | 3.047 / 2.714 | 4,6 / 4,1 | 294 / 273 | 375 | 518-574 | ja |
| W5 | 2.955 | 4,4 | 349 | 375 | 518-574 | ja |
| C1 | 2.923 | 4,4 | 344 | 281 | 694-750 | nee |
| C2 | 2.660 | 4,0 | 303 | 281 | 694-750 | nee |
| C2-ACC | 2.314 | 3,5 | 253 | 281 | 694-750 | nee |
| C3-P / S / ACC | 2.625 / 2.336 / 2.575 | 3,9 / 3,5 / 3,9 | 334 / 265 / 263 | 281 | 674-768 | nee |
| C4 (code) | 3.050 | 4,6 | 336 | 281 | 732-788 | nee |
| K1 | 2.476 | 3,7 | 256 | 281 | **972-1028** | nee |
| K1-ACC | 2.099 | 3,1 | 216 | 281 | 689-745 | nee |
| K2-NEW / RETURNING | 2.482 / 2.851 | 3,7 / 4,3 | 282 / 272 | 281 | 670-726 | nee |
| K3 (code) | 3.064 | 4,6 | 336 | 281 | 708-764 | nee |
| B1 / B1-ACC | 2.309 / 1.908 | 3,5 / 2,9 | 287 / 197 | 281 | 707-763 | nee |
| B2-NOTCLICKED | 2.764 | 4,1 | 296 | 281 | 707-763 | nee |
| B2-CLICKED (code) | 2.899 | 4,3 | 336 | 281 | 707-763 | nee |
| TP · B1 | 3.036 | 4,6 | **380** | 329 (productfoto) | 840-896 | nee |
| TP · B2-NOTCLICKED | 2.792 | 4,2 | 335 | 248 | 823-879 | nee |
| A1 | 2.709 | 4,1 | 297 | 281 | 427-483 | ja |
| A2 | 2.706 | 4,1 | 273 | 281 | 827-883 | nee |
| P1-FIRST / REPEAT | 3.547 / 2.541 | 5,3 / 3,8 | 414 / 267 | 375 | 474-530 | ja |
| P2 / P2-SAFE | 3.585 / 3.286 | 5,4 / 4,9 | 463 / 467 | 375 | 474-530 | ja |
| P3 (code, 5 soorten) | 2.900-2.976 | 4,3-4,5 | 339-361 | 375 | 518-574 | ja |
| Mystery M1 / M2 / M3 | 1.517 / 1.599 / 1.425 | 2,3 / 2,4 / 2,1 | 211 / 227 / 183 | 248 | **1161 / 1249 / 950** | nee |
| Review (XzHrez, TvfJYU) | 1.301 | 2,0 | 73 | 319 | sterren op 351+ | ja (sterren) |
| R1 (SET, PAN, ACC) | 2.429-2.919 | 3,6-4,4 | 287-321 | 375 | 518-574 | ja |
| R2 / R2-VIP (code) | 2.957 / 2.984 | 4,4 / 4,5 | 361 / 365 | 375 | 518-574 | ja |
| S1 / S2 | 1.227 / 921 | 1,8 / 1,4 | 137 / 137 | 281 / geen | 631-687 / 441-497 | net niet / ja |
| S3 / S4 kept | 1.260 / 1.131 | 1,9 / 1,7 | 191 / 177 | geen | geen / 653-709 | n.v.t. / nee |
| AFF A1 / A2 / payout / sale | ~950-1.100 totaal | 1,4-1,7 | 114 / 104 / 112 / 103 | 249-414 | 624-830 | A1 ja, rest nee |
| VIP V1 (code) / V2 | 3.019 / 763 | 4,5 / 1,1 | 332 / 101 | 375 / geen | 518-574 / 627-683 | ja / nee |
| Anniversary N1 / N2 | 2.563 / 2.943 | 3,8 / 4,4 | 311 / 329 | 375 | 518-574 | ja |
| UGC U1 | 2.516 | 3,8 | 313 | 375 | 476-532 | ja |
| Oude winback UEfh4h #1-#3 | 1.120-1.570 | 1,7-2,3 | vrijwel alleen beeld | volle breedte | 688-796 of geen | nee |
| FTL (4 live) | 1.440-2.220 | 2,2-3,3 | vrijwel alleen beeld | volle breedte | geen live knop | nee |
| FREE E-GUIDE | 1.250 | 1,9 | vrijwel alleen beeld | volle breedte | geen live knop | nee |

Vaste bovenkant v4 op mobiel:

- Codebalk: 44 px. In P1, P2, W0, W2 en de tekstmails is er geen codebalk.
- Header met lockup: 79 px.
- Hero: 375 px (1:1) of 281 px (4:3).
- Aanbodbalk: 45 px.

Pas daarna begint de cartkaart of de knop. In welcome, post-purchase en winback valt de knop daardoor net binnen het eerste scherm, in de 4:3-flows net erbuiten.

---

## 4. Per mail: score, de 3 grootste problemen en één verbetering

Scores van 1 tot 10 op stijl en content samen: eerste scherm, lengte, copy volgens de regels, beeld en consistentie. Varianten die alleen in het aanbod verschillen (code of nocode) staan samen.

### Welcome `T4a5Mk`

**W0 (al klant) · 7/10**
1. In het eerste scherm staan hero, knop en friction reducer. Goed. De mail is wel 4,1 schermen lang voor een bedankje met één tip.
2. Er zijn 9 kleine beelden zonder alt. Die zijn decoratief, maar het zijn er veel.
3. De ondertekening is "Founder, Siraat's Kitchen". Floris koos op 15 okt voor "Siraat"; dat is nog niet doorgevoerd.

Verbetering: inkorten tot de eerste-ei-stappen en één knop, ongeveer 2 schermen.

**W1 A (lopende arm) · 7/10**
1. De belofte staat in het eerste scherm ("No PFAS. Here's the paper."), met de knop op 518 px. Goed. Alleen staat het aanbod drie keer in dat eerste scherm: in de codebalk, de aanbodbalk en het knoplabel.
2. 4,3 schermen. Het gifts-blok staat er twee keer in. Vergelijking, aanbodblok en drie reviews: dat zijn vier grote onderdelen, en PLAYBOOK 12 staat er maximaal twee toe.
3. De Card Game-regel ("Your Card Game entry is in") staat in grijs, 14 px op crème, met een contrast van 4,48:1.

Verbetering: het tweede gifts-blok weg, en de vergelijking of het aanbodblok weg. Dan ongeveer 3,3 schermen, met dezelfde boodschap.

**W1 B (v3, "Welcome to Siraat.") · 6/10**
1. Het eerste scherm is een begroeting met code. Er is geen hero-beeld en het product staat pas op 651 px. De belofte is generiek ("The original hammered titanium pan").
2. "FALL SALE / Buy 2, get 4 free / $299" is na 31 okt verouderd.
3. 4,6 schermen. Dit is de langste welcome-mail.

Verbetering: als T04 dichtgaat met A (01-welcome, 29 okt), deze arm ook in de bron als archief markeren. Komt hij terug, dan zonder het setblok.

**W2 (brief van Benjamin) · 8/10**
1. Een echte tekstbrief, zoals HexClad het niet doet (die zet de brief in een afbeelding). Er is geen knop, wel een P.S.-link. Bewust zo.
2. 371 woorden. Dat past bij een problem-aware lezer, maar de hoogste afmelding van de flow zit hier (1,98%).
3. De afzender is "Benjamin at Siraat's Kitchen", ondertekend als "Siraat's Kitchen". Dat is niet in lijn met het merknaambesluit.

Verbetering: de eerste alinea inkorten tot de reden waarom hij schrijft. Het PFAS-verhaal mag een alinea later. Dit is een test (T17 staat al gepland op 7 dec).

**W3 ("Don't take our word for it.") · 7/10**
1. Sterk bewijs met zes controleerbare punten en het certificaat in beeld. Het eerste scherm is goed.
2. 4,5 schermen met 7 icoontjes zonder alt (decoratief).
3. Het gifts-blok herhaalt zich. Na de zes bewijspunten zakt de hiërarchie weg.

Verbetering: de zes punten worden drie (rapport, nummer, garantie, conform DECISIONS 1 okt) en het tweede gifts-blok gaat weg.

**W4-US / W4-INT ("Who are you cooking for?") · 6/10**
1. "FALL SALE / Buy 2, get 4 free" plus de setprijs. De datum en de novemberprijs zijn open.
2. W4-INT verkoopt nul (0 orders op 1.880). De opbouw is gelijk aan US zonder een sterker INT-argument.
3. De hero (pasta lift, AI-flash) is mooi, maar de pan zelf is klein in beeld.

Verbetering: het setblok onder een macro voor de saleperiode zetten (één plek wijzigen per sale). In W4-INT bovenaan de maatkeuze en "duties paid".

**W5 ("Tammy is on her fourth pan") · 7/10**
1. Goede verhaalopbouw: voor, test, nu. Het onderwerp is een specifiek citaat.
2. Nul orders op 2.243 mails. De laatste welcome-mail sluit het aanbod niet echt af ("last time we mention HI10" staat alleen in de preview).
3. Twee reviews noemen "non-stick". Dat is letterlijk en toegestaan, maar het botst met de regel "non-stick niet als kop".

Verbetering: dit wordt de BF-vroege-toegang-mail (Q2 in 01-welcome). Stijl: één aanbod, één deadline met reden, korter.

### Checkout `QUBUQV`

**C1 ("Your cart + 4 gifts are still pending") · 6/10**
1. **De knop staat onder de vouw (694 px).** In het eerste scherm staan codebalk, header, hero 4:3, aanbodbalk en de cartkaart. De knop komt net niet in beeld.
2. "Your 4 gifts end when the fall sale ends" is vanaf 1 nov onwaar.
3. 344 woorden en 4,4 schermen voor een most-aware lezer (norm 60 tot 180). Gifts-strook, vergelijking, 3 reviews en een P.S.

Verbetering: op mobiel de header (79 px) of de aanbodbalk (45 px) laten vallen, zodat de knop op ongeveer 610 px begint. Daarnaast de vergelijking weg. Dit is een test (eerste scherm compact tegenover nu).

**C2 ("Has the pan in your cart been tested?") · 6/10**
1. Dezelfde vouw (694 px). De belofte ("Non-toxic is easy to say") is sterk, maar staat ver weg van het cartproduct.
2. De hoogste afmelding van de flow (2,38%). De mail is lang (4,0 schermen) voor de derde mail in 26 uur.
3. Verouderde gifts-regel. De ondertekening noemt "Siraat's Kitchen" twee keer.

Verbetering: kort houden. Rapportnummer, certificaatbeeld, één knop, ongeveer 150 woorden. Hiervoor zijn geen extra tests nodig, het past naast R4 (48 uur).

**C2-ACC · 6/10**: zelfde vouw, verouderde gifts-regel, het accessoire verdwijnt achter het blok over de pan. Verbetering: het accessoire bovenaan en de pan als tweede stap.

**C3-P ("One pan, or three?") · 5/10**
1. "THE FALL SALE" en "FALL SALE · SIX PIECES" staan ingebakken in de hero en in de codebalk. "This month, buy 2" staat in de copy. Op 1 nov is dat verouderd, en een nieuwe export van het beeld is nodig.
2. De eerste knop "Upgrade to the 6-piece set" wordt op mobiel twee regels (74 px hoog).
3. 334 woorden, gifts twee keer.

Verbetering: label en balk zonder seizoensnaam ("THE 6-PIECE SET"), en de prijs uit de macro. Directe fix bij de saleomzetting.

**C3-S / C3-ACC · 6/10**: zelfde vouw en gifts-regel. C3-ACC verhaalt goed ("we started with cutting boards"). Verbetering: in C3-S de doos-inhoud bovenaan in plaats van na de cart.

**C4 code / nocode ("We're removing your discount in 48 hours") · 7/10**
1. Echte deadline met datum in de codebalk ("FRI OCT 30" uit de coupon). De twee beloftes staan erin. Goed.
2. 4,6 schermen en de knop op 732 px. De codebalk is hier twee regels hoog.
3. De nocode-variant draagt de verouderde gifts-regel.

Verbetering: de deadline-regel als eerste zin onder de hero in plaats van na de cart.

### Cart `TZG9Mx`

**K1 ("The hammered pattern: an easy wipe") · 4/10**
1. **De knop staat op 972 px, het slechtste eerste scherm van alle verkoopmails.** De cartkaart van k1-v2 toont een productfoto van ongeveer 300 px, terwijl C1 een compacte regel heeft. K1 maakt 55% van de cartomzet.
2. De hero is een close-up van een hand die veegt. Het product en het gevoel van "jouw cart" ontbreken in het eerste scherm.
3. Verouderde gifts-regel en 256 woorden.

Verbetering: dezelfde compacte cartregel als C1 (beeld 76 px) en de knop direct eronder. Dit is een directe fix volgens PLAYBOOK 11 ("cart en knop boven de vouw").

**K1-ACC · 6/10**: knop op 689 px, 2,9% afmelding (5 op 174). Verbetering: compacte kaart en korter.

**K2-NEW ("15 coated pans, or one") · 7/10**
1. Sterke rekensom die het prijsbezwaar beantwoordt. Precies de nummer-1-twijfel uit de enquête.
2. "Nothing to wear off" en varianten komen drie keer voor. Dat is een eigen tic die de skill wil rantsoeneren.
3. Knop op 670 px (net onder) en de verouderde gifts-regel.

Verbetering: de rekensom als eerste blok onder de hero, de cart compacter.

**K2-RETURNING · 7/10**: kort en passend ("you know how it works"). Verouderde gifts-regel. Verbetering: 4,3 schermen naar 3.

**K3 code / nocode · 6/10**: echte deadline, maar 4,6 schermen. De nocode-variant "What if it's not for you?" is een goede risicoomkering. Verbetering: K3 nocode tot 2,5 schermen, alleen de twee beloftes en de cart.

### Browse `WdRz5k` en Triple Pixel `QNZyEb`

**B1 ("Get this pan with 10% off") · 6/10**
1. Knop op 707 px. Het eerste scherm toont de hero met "This pan, 10% off." en de productregel.
2. In de copy staat "the sale" zonder getal, terwijl de site 50% en straks 70% toont (zie BR1).
3. De ondertekening noemt "Siraat's Kitchen" twee keer.

Verbetering: de productregel en de knop boven de reviews, de saleregel in de aanbodbalk. Dit is test BR1.

**B1-ACC · 7/10**: compact (197 woorden), goed beeld (Moss-schort, Shopify). Verbetering: knop omhoog.

**B2-NOTCLICKED ("Skeptical? So were they.") · 7/10**: goede verhaalhook en echte reviews. 4,1 schermen. Verbetering: de reviewcase bovenaan, gifts weg.

**B2-CLICKED code / nocode · 6/10**: deadline klopt, nocode draagt de verouderde gifts-regel. Verbetering: zoals K3.

**TP · B1 ("Here it is again.") · 6/10**
1. De beste omzet per ontvanger van browse ($1,20), maar de knop staat op 840 px. Eerst komen een kop in live tekst en een grote productfoto.
2. 380 woorden. Dat is de langste browsemail.
3. Er is geen vaste hero met aanbodbalk, dus de opbouw wijkt af van de andere flows. Dat is bewust (product eerst, BR2).

Verbetering: de knop direct onder de productfoto (ongeveer 610 px) en de tekst naar 230 woorden.

**TP · B2-NOTCLICKED ("Why we can cover this pan for 75 years") · 5/10**: 0,50% spam, knop op 823 px, 335 woorden. Verbetering: halveren of op holdout (BR5, R5).

**TP · B2-CLICKED · 6/10**: verouderde gifts-regel. Verbetering: zoals K3.

### Site `VLGhbR`

**A1 ("Four eggs or five?") · 8/10**: de beste mobiele opbouw van alle verkoopmails. De knop staat op 427 px, met een concrete keuzehulp. Probleem: "Buy 2, get 4 free" en $299 in de copy (verouderingsrisico), 4,1 schermen. Verbetering: het setblok onder de salemacro.

**A2 ("Where 100,000+ customers started") · 6/10**: de knop staat op 827 px, omdat er eerst een productkaart met "BEST SELLER"-sticker komt. Verbetering: knop onder de hero, zoals A1.

### Post-purchase `X3ySuU` en levering `VQ93sx`

**P1-FIRST ("Good call. Here's what's next.") · 7/10**
1. Het eerste scherm is goed: hero, e-book-knop op 474 px.
2. 5,3 schermen en 414 woorden. Tijdlijn, gifts, tip, reviews en de e-book-knop twee keer.
3. "Delivery then takes 6 to 10 days" is een levertijd. In een servicemail mag dat, maar in BFCM moet het kloppen. Mediaan nu: 77 uur tot fulfillment.

Verbetering: de tijdlijn compacter, en ruimte voor de dekselkaart (T15) door het tweede gifts-blok te schrappen.

**P1-REPEAT · 7/10**: kort en warm. Maar 20 eerste kopers per week krijgen deze mail ten onrechte (05-herinstap). Verbetering: buiten stijl, wel de copy-regel "Same 4 gifts" laten kloppen als de gifts wijzigen.

**P2 / P2-SAFE (eerste ei) · 8/10**: inhoudelijk de sterkste mail. De chef-stappen met beeld, de reden ("Cold metal grabs your food"), de knop in het eerste scherm. 5,4 schermen mag hier (PLAYBOOK 12). Probleem: twee reviews met "non stick" en 4 beelden zonder alt. Verbetering: de stapbeelden een alt geven ("Water drop beads on a hot pan").

**P3 (SET, NEXT, PAN, ACCESSORY, APRON; code en nocode) · 6/10**
1. Verouderde gifts-regel in alle 12 varianten, en de setprijs van $299.
2. 4,3 tot 4,5 schermen voor één cross-sell.
3. De heroes verschillen sterk van stijl: AI-flash (crêpe), Shopify-daglicht (P3-NEXT, P3-APRON) en studio. De flow oogt daardoor niet als één reeks.

Verbetering: één productkaart en één knop, de reviews naar 2. Dit staat gepland met het saleblok (3 tot 6 nov).

### Mystery Gift `YwsKcf` (zonder header, conform besluit 23 okt)

**M1 ("Let's reveal your mystery gift") · 7/10**
1. Het eerste scherm is goed. Het label en de kop staan in live tekst, de foto toont het echte pak (v3, letter voor letter gecontroleerd).
2. De knop staat op 1.161 px, na de brief en "What's in the pack".
3. De kop staat in Instrument Serif als webfont. In Gmail valt die terug op Times New Roman, en dan wijkt hij af van de TT Ramillas-PNG's in de rest.

Verbetering: een kleine tekstlink of knop direct onder de foto ("See my gift up close").

**M2 · 7/10**: duidelijke instructie in drie stappen. De knop staat op 1.249 px. Verbetering: zoals M1.

**M3 ("Alright, here's the offer") · 6/10**: dit is de verkoopmail van de flow, maar de knop ("Get 20% every month") staat op 950 px en de prijs komt pas na de uitleg. Verbetering: aanbod en prijs direct onder de hero. Kleine directe fix, kan vóór BFCM.

### Review `XzHrez` en vangnet `TvfJYU`

**Review · 8/10**: de sterren staan meteen in het eerste scherm, met 73 woorden. De witte lockup staat in de hero (besluit 12 okt). Problemen: de afzender is "SiraatsKitchen" (zonder apostrof, anders dan de rest) en de hero is geen link. Verbetering: de afzendernaam gelijktrekken met de andere flows. Het nadenken over de A/B-uitslag (half jan) laat ik hier buiten.

### Winback v4 `UyFc78`

**R1 (SET, PAN, ACC) · 6/10**: goed eerste scherm (knop op 518 px). Problemen: verouderde gifts-regel en $299, 3,6 tot 4,4 schermen, en de knop "Shop with my 10%" zegt niets over de pan. Verbetering: de knop naar het voordeel ("Add the lid that fits"), het saleblok erin (3 tot 6 nov).

**R2 / R2-VIP code en nocode · 6/10**: de deadline is echt ("72 hours"), maar 4,4 schermen en 361 woorden. De hero toont een echte shootfoto met het monogram op het handvat. Verbetering: inkorten tot ongeveer 200 woorden. Krijgt pas eind december volume.

### Oude winback `UEfh4h` (live, loopt tot 14 dec, ongeveer 470 mails per dag)

**Email #1 tot #3 · 2/10**
1. **De claims zijn in strijd met DECISIONS**: in de topbalk staan "FREE SHIPPING | FREE RETURNS | 100-DAY TRIAL". De alt zegt "PRIME TIME SALE | UP TO 56% OFF". De vergelijking noemt "Lifetime Guarantee".
2. **Onware urgentie**: "Your 10% Off Ends Tonight" en het onderwerp "10% Off Expires Tonight". Code GOODFOOD is de affiliatecode. Ook staat er "Workers Day" in een mail die in november landt.
3. De oude header (zwart, menu), niet de vaste header en footer. De knoppen zijn klein en afgerond, er is geen friction reducer.

Verbetering: direct op Draft (PLAYBOOK 7) of de drie mails vervangen door een v4-R1-kloon tot 14 dec. Het oordeel van 04-postpurchase ($0,09 per ontvanger) komt daar nog bij.

### Sunset `TbYQmX` en kept `Wzz6xC`

**S1 · 7/10**: eerlijk en kort (137 woorden). De knop staat op 631 tot 687 px, dus net niet. Verbetering: de knop direct onder de hero.

**S2 · 8/10**: een brief van Benjamin met de knop in het eerste scherm. "nothing to fill in, nothing to buy" is een eigen tic. Verbetering: geen.

**S3 / S4 kept · 7/10**: kort. S3 heeft geen knop, maar dat is bewust (voorkeurlink). Verbetering: geen voor BFCM.

### Affiliate (S1 `R22pzb`, S5a `Yp6sKv`, S5b `TkV5DY`; platte brief, besluit 21 okt)

**A1 announce · 7/10**
1. **"Friends get 15% off their first order"** staat in de preview en in de copy. Volgens het besluit van 22 okt geldt de korting voor alle klanten.
2. De rekensom ("8 friends: a whole Duo back") is sterk, maar staat vóór de knop en vult het eerste scherm.
3. De afzender is "Benjamin from Siraat". Dat is een vierde variant.

Verbetering: "first order" eruit. Een directe fix van één regel.

**A2 nudge-1 · 7/10**: goede tip ("save your link in your notes"). De knop staat op 666 tot 722 px. Verbetering: de rekensom korter.

**Payout / sale · 7/10**: 103 tot 112 woorden, in lijn met de skill. De knop staat net onder de vouw. Het contrast in de minimale footer is 3,0:1 (#9A948B, 11 tot 12 px). Verbetering: de footertekst #727272 of donkerder.

### Overige live v4 (kort)

- **VIP V1 · 6/10.** Verouderde gifts-regel. De hero is een echte Shopify-schortfoto met de echte opdruk, dus geen AI-tekst. 4,5 schermen. **V2 · 8/10**: korte vraag van Benjamin.
- **Anniversary N1 / N2 · 6/10.** Verouderde gifts-regel en de setprijs.
- **UGC U1 · 7/10.** Duidelijke vraag, knop op 476 px.

### Failure to launch `T2SmtR` (4 live) en FREE E-GUIDE `YyaMjx`

**FTL Titanium vs Non-Stick, Store + Care, vs Stainless, Micro-Plastic Free · 2/10**
1. In beeld staan "100-DAY TRIAL", "Lifetime Warranty", "Get a Lifetime of Use", "Heat Safe up to 548C/1000F" (een oventemperatuur, verboden) en "Naturally Non-Stick".
2. "5g Should Be Causing You Anxiety" is een microplastics-angsthook. Die is niet onze claim en is een gezondheidsclaim.
3. Ze zijn bijna alleen beeld en hebben geen live tekst. Afzender "SiraatsKitchen", oude header en footer.

Verbetering: de 4 overige mails ook op Draft zetten, of de afmeldings- en claimsrisico's laten wegen tegen de $0,012 per ontvanger. Dit hoort vóór 1 nov bij R7.

**FREE E-GUIDE · 3/10**: "100-DAY TRIAL" in de topbalk en "45% off on our bestselling ... Set Pro" (een oud aanbod). Op 28 okt een afmeldalarm van 1,63%. Verbetering: de topbalk en de 45%-regel eruit, en daarna de mail op de vaste opmaak met de lockup zetten. Kan ook simpel: een v4-P1-achtige brief van Benjamin met de downloadknop.

---

## 5. Consistentie tussen flows

| Onderdeel | Stand | Oordeel |
|---|---|---|
| Knop | Alle v4-mails: brick #AC3B19, wit, Inter 16 px in kapitalen met letterspatiëring, pijl, 331 x 56 px, geen afronding, ik-vorm. | Consistent. Oude flows: kleine afgeronde oranje of zwarte knoppen. |
| Kleuren | crème #F8F7F2 kolom, ink #282828, brick, espresso aanbodblok, donkere footer. | Consistent in v4. |
| Letters | Koppen als TT Ramillas-PNG; body Inter (Arial in Gmail); Mystery-koppen live in Instrument Serif (Times in Gmail). | Mystery wijkt zichtbaar af in Gmail. |
| Logo | Lockup op crème in de header, wit in de footer. Review: witte lockup in de hero. Affiliate en Mystery: zonder header (besluiten). | Klopt met CLAUDE.md. Oude flows: eigen witte lockup in een zwarte balk. |
| Afzender | "Siraat's Kitchen", "Benjamin at Siraat's Kitchen", "Benjamin from Siraat", "SiraatsKitchen" (review, FTL, oude winback, e-guide). | **Vier varianten.** De review-flows krijgen in BFCM veel volume met de vreemdste variant. |
| Ondertekening | "Founder, Siraat's Kitchen" in vrijwel alles, "Founder, Siraat" in TP B1, W1 en Mystery. | Wacht op het merknaambesluit (DECISIONS 15 okt: Siraat). |
| Beeld | Vier bronnen: AI-flash v5 (goedgekeurd), hp-shoot (donker, studio), Shopify-lifestyle (daglicht), en Mystery v3 (flash met echt pak). Alle heroes hebben een donkere overlay voor de ingebakken kop. | De overlay maakt de flash-look grauw en de pan grijs. Binnen één flow (P3, checkout) springt de stijl van mail naar mail. Geen zwarte coating in v4 gezien. Geen AI-tekst gezien; logo's in V1 en R2 komen uit echte foto's. Vergelijkingsbeeld "Titanium vs Traditional" (FTL) toont bewust een zwarte pan. |
| Aanbod | Codebalk + aanbodbalk + knoplabel + aanbodblok zeggen hetzelfde. | Vier keer hetzelfde aanbod per mail. Het idee van de mail moet daartegen opboksen. |
| Afsluiter | "Reply and our team will help." in 22 templates. | Klopt met PLAYBOOK 12. |

---

## 6. Toegankelijkheid en dark mode

- **Contrast.** Grijs #727272 op crème #F8F7F2 = 4,48:1. Dat geldt voor de friction reducers (12 px), "Founder, ..." (15 px), "Join 100,000+ happy customers" (13 px), P.S.-regels en Card Game-regels, in 60+ mails. Het zit net onder AA (4,5:1); op 12 px telt dat. Met #6B6B6B wordt het 5,0:1, met #666666 5,4:1. Doorgestreepte prijzen in #9A948B = 3,0:1. De affiliate-footer in #9A948B (11 px) = 3,0:1. Footer-links #111111 op #282828 zijn bewust (Floris) en niet meegeteld.
- **Alt-teksten.** Elke hero-alt noemt kop, subregel en aanbod letterlijk. Goed. Er zijn 2 tot 9 decoratieve beelden per mail met `alt=""` (iconen, reviewavatars, het pannetje boven de vergelijking). Dat is correct. Wel ontbreekt een beschrijvende alt bij de stapbeelden in P2. De oude flows zijn bijna alleen beeld: met beelden uit blijft er niets over.
- **Dark mode.** `color-scheme: light only` staat in elke v4-mail. Apple Mail respecteert dat, de Gmail-app op iOS kleurt toch om. Wat daar goed gaat:
  - De lockup staat in de header als PNG met een crème vlak, dus geen zwart logo op zwart.
  - De kop staat ingebakken in de hero.
  - Vlakken zijn bgcolor plus inline (QA 10 okt).

  Risico: de grijze hulpteksten worden in geïnverteerde modus nog zwakker. Mystery-koppen in live serif zijn het meest gevoelig.
- **Tikdoelen.** Knoppen van 56 px hoog over de volle breedte. Goed. Tekstlinks in de friction reducer en de P.S. zijn 12 tot 15 px.

---

## 7. Wat de beste DTC-kookmerken anders doen

| Merk | Wat ze doen (bron) | Wat Siraat ervan kan leren |
|---|---|---|
| Our Place | Gemiddeld **44 woorden** en 21 beelden per mail, onderwerpen van 23 tekens (Email Love brand insights). "Double Major": één grote productfoto, een kop met woordgrap, een anatomie-callout met 3 feiten, één knop. "One Less Worry": geruststelling ("Made without PFAS, lead, or microplastics") zonder angst. Geen codebalk, geen aanbodbalk. | Eén idee per scherm. Het product groot en scherp, zonder overlay. De specificatierij (idee 29) in plaats van drie lagen aanbod. |
| Made In | Gemiddeld **153 woorden**, 12 beelden, een eenvoudige witte header met woordmerk, één rode knop per blok. "Jake's Buyer's Guide": de oprichter als gids, met per materiaal "benefits / considerations" naast elkaar. "Keep Your Pans Looking New": educatie met één product en één knop. | De oprichter als gids werkt ook in post-purchase (P2 doet dit al goed). Eerlijke "considerations" passen bij de skill ("one honest limitation"). |
| HexClad (eigen inbox) | Cartmails met 7 dagen ertussen, elke mail één bezwaar (garantie, dan prijs via Affirm). De brief van de oprichter staat in een afbeelding. Refer-a-friend in elke footer. | Eén bezwaar per mail (T23, T24). Brieven blijven live tekst (W2 en S2 doen dat al). |
| Caraway (eigen inbox, Email Love 2023-2025) | Georganiseerde productlayout, rustig palet, reviews als blok. Opt-out van feestdagmails (Father's Day). "Not ready for a full set?" onder de set. | Een kleinere stap onder de set (idee 10). Een opt-out vóór BFCM-drukte kan afmeldingen in welcome en sunset drukken. |

Samengevat: de concurrenten winnen op **rust in het eerste scherm**. Ze tonen één product groot en één zin, en hebben veel minder herhaling. Siraat wint op **bewijs** (rapportnummer, 75 jaar, echte reviews, Benjamin als tekst) en mag dat niet inleveren. Het gaat erom het bewijs minder te stapelen, niet om minder bewijs.

---

## 8. Top 10 stijl- en contentverbeteringen

Impact is een inschatting, geen bewezen effect. "Vóór BFCM" betekent live vóór de bevriezing van 20 nov (00-plan).

| # | Verbetering | Waar | Verwachte impact | Test of fix | Vóór BFCM | Moeite |
|---|---|---|---|---|---|---|
| 1 | Oude flows met verboden claims en valse deadline stoppen of vervangen: oude winback (100-day, free returns, GOODFOOD, "Ends Tonight"), FTL (4 live: 100-day, lifetime, 1000°F, microplastics-angst), FREE E-GUIDE (100-day, 45% off) | `UEfh4h`, `T2SmtR`, `YyaMjx` | Hoog op merk- en claimrisico; omzet nu $0,01 tot $0,09 per ontvanger, dus weinig te verliezen. E-guide-afmelding 1,63% omlaag | Directe fix (Draft of v4-kloon), akkoord Floris | Ja, vóór 1 nov | Laag |
| 2 | "Your 4 gifts end when the fall sale ends", "This month", "THE FALL SALE" en de $299-set omzetten naar november-waar (gifts lopen door; prijs en datum van Floris). Eén keer in `v5lib`/`gifts5 urgency`, daarna herbouwen en exporteren; C3-P-hero en -codebalk opnieuw | ~45 live varianten in checkout, cart, browse, TP, P3, R1/R2, VIP, N, plus W1-B, W4, A1/A2, C3 | Voorkomt onware copy in alle verkoopflows vanaf 1 nov | Directe fix | Ja, vóór 1 nov | Middel (één macro, ~45 templates patchen via export) |
| 3 | K1: compacte cartregel zoals C1 en de knop direct onder de cart (nu 972 px) | `cart/k1-v2` | K1 = 55% van cartomzet; knop in het eerste scherm. Schatting +10 tot 20% klik op K1, $100 tot $250 per week | Directe fix (PLAYBOOK 11), uitslag volgen op klik | Ja | Laag |
| 4 | Eerste scherm in checkout, cart, browse en TP compacter: op mobiel de header of de aanbodbalk weg, zodat de knop rond 600 px staat (nu 670 tot 896) | C1-C4, K2-K3, B1/B2, TP B1/B2, A2 | Meer kliks op de mails met de hoogste omzet per ontvanger; ongeveer +5 tot 15% klik | Test (C1 compact tegen nu; T14 staat nog niet live, dus slot vrij) | Start 1 nov, beslissen in dec | Middel |
| 5 | Verkoopmails inkorten naar ~2,5 schermen en de skillnorm (most aware 60 tot 180 woorden): het tweede gifts-blok weg, 2 reviews in plaats van 3, maximaal 2 grote onderdelen | Checkout, cart, browse, P3, R2, W1/W3 | Minder afmelding (C2 2,38%, W1 1,81%); klik gelijk of hoger | C2 direct (past bij R4), de rest als test na BFCM | C2 ja, rest dec | Middel |
| 6 | Affiliate A1: "15% off their first order" naar "15% off" (besluit 22 okt) | `R22pzb` A1, preview en body | Klopt weer met het aanbod; voorkomt klachten van bestaande klanten | Directe fix | Ja | Laag |
| 7 | Afzender en ondertekening gelijk: één naam (Floris kiest Siraat of Siraat's Kitchen, DECISIONS 15 okt), en "SiraatsKitchen" uit review, FTL en e-guide | Alle flows | Herkenbaarheid in de inbox; review-flows krijgen in BFCM de Fulfilled-golf | Directe fix (afzendernaam in Klaviyo, ondertekening via partial) | Ja | Laag |
| 8 | Eén aanbodregel per mail: codebalk en aanbodbalk niet allebei hetzelfde laten zeggen, en tijdens de sale de salemelding plus HI10 in één regel (sluit aan op BR1 en Q1) | Alle v4-verkoopmails | Ruimte voor het idee van de mail in het eerste scherm; duidelijker aanbod in BFCM | Test (BR1 en Q1 lopen al; dit is hun stijluitvoering) | Ja, met BR1 op 1 nov | Middel |
| 9 | Grijs #727272 naar #666666 (5,4:1) voor friction reducers, ondertekening en P.S.; affiliate-footer #9A948B donkerder | `partials/blocks/_style` en inline blokken | Leesbaar op mobiel en in dark mode; AA gehaald | Directe fix, meenemen in de export van punt 2 | Ja | Laag |
| 10 | Beeld: product groter en zonder donkere overlay; de kop als live tekst of op een effen vlak boven het beeld (zoals Mystery en review); per flow één beeldbron (flash) | Heroes van checkout, cart, P3, W3 | Herkenbaar echt product (gehamerd titanium) in het eerste scherm; aansluiting op Our Place en Made In; Mystery M1 haalt 3,35% klik met deze opbouw | Test (W3-hero T07 en C1 als eerste) | Nee, na BFCM (dec) | Hoog (nieuwe heroes en exports) |

Kleine directe fixes die buiten de top 10 vallen:
- Mystery M3: aanbod en knop direct onder de hero (nu 950 px).
- P2: alt-teksten voor de stapbeelden.
- P1: de levertijdregel "6 to 10 days" voor BFCM laten checken.
- W1-B: archiveren als T04 met A sluit.
- Old Welcome 6 tot 8 op Draft zodra ze leeg zijn (rond 30 okt).
