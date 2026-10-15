# 02 · Bedrag of korting? Gift card, credit of "10% off"

Datum: 15 oktober 2026. Vraag van Floris: tonen we een aanbod als gift card met een bedrag ("$25 gift card", "$30 credit") of als korting ("10% off")? Voor welcome, referral (vriend en verwijzer), winback en cadeau-momenten. Floris maakte het beeld `research/giftcard/floris-giftcard-goud.webp` (goudkleurige kaart met strik, monogram, SIRAAT en de woorden GIFT CARD, zonder bedrag).

Bronnen: eigen Klaviyo-data (alleen gelezen: flow T4a5Mk, flow- en campaign-values-reports, Placed Order-events 15 juli tot 15 oktober 2026), DECISIONS, PLAYBOOK, `research/copy/06-offer-design.md`, `research/deep/04-siraat-diagnose.md`, `.agents/product-marketing.md`, `research/concurrenten/`, `content/facts/claims.csv`, plus webonderzoek (bronnen onderaan). Niets aangemaakt of gewijzigd in Klaviyo of Shopify. Codes behalve HI10 staan hier als XXXXXXXX.

## Kort antwoord

1. **"Gift card" alleen voor een echte gift card.** Een kortingscode met minimumbedrag, einddatum of "niet stapelbaar" is geen gift card. Noem die "$25 off" of "your $25 welcome offer". Floris' gouden kaart hoort bij echte gift cards: de verwijzer-beloning, de verkoop van e-gift cards (flow 09) en december.
2. **Welcome: HI10 (10%) blijft de controle.** De enige eigen test (T04, 9 tot 15 okt: HI10 als code tegen HI10 als "welcome gift card") gaf de gift-card-variant niets extra: 3,8 tegen 4,5 procent kopers, $9.72 tegen $12.02 per ontvanger (niet significant, kans dat B beter is 22 procent). De volgende test is niet de verpakking, maar de mechaniek: **10% zonder minimum tegen "$25 off $150+"**.
3. **Referral: dollars aan beide kanten.** Vriend: "$25 off your first order of $150+" (kortingscode). Verwijzer: een **echte $25 Siraat gift card** na de retourtermijn van de vriend. Daar past het gouden beeld eerlijk.
4. **Winback: dollars, laag minimum.** "$20 off your next order of $100+" tegen de huidige 10%. Het vervolgproduct (deksel-pan $154, pot $149, utensils $149) ligt net boven $100, waar een bedrag groter voelt.
5. **BFCM: procent als kop (sitebreed, compare-at), dollars als trap voor sets.** Historisch zijn de best verdienende campagnes van het jaar "62% off". Daaronder een extra laag in dollars ("extra $30 off $299+, $75 off $599+") tegen "extra 10%", gelijke kosten bij $299.

## 1. Eigen data

### 1.1 Is HI10 ooit getest als code tegen als gift card? Ja: T04

DECISIONS 7 okt noemde het plan ("A/B in W1: A = HI10 als code-blok, B = zelfde 10 procent als 'welcome gift card' met gift-card-visual"). Het is gebouwd en gedraaid:

- Flow T4a5Mk (v4 · Welcome), A/B-actie 119850659, experiment `01M4E3EWS7W4DCBYCZ8VSB2WP4`, 50/50, winnaar handmatig.
- A = variatie VnXKz4 (template w1-a, HI10 als codekaart). B = variatie SXwPrW (template w1-b, zelfde HI10 als "welcome gift card"-beeld, alt "Your Siraat welcome gift card: 10% on top of the sale with code HI10"). Zelfde onderwerp ("No PFAS. Here's the paper. And 10%."), preview, hero en blokvolgorde.
- Gestart door Floris op 9 okt 00:40 UTC. Op 15 okt 00:33 UTC is variant B vervangen door W1 v3 (LOG). T04 is dus na 6 dagen gestopt, met te weinig volume voor een besluit.

Resultaat 9 okt 00:40 tot 15 okt 00:33 UTC:

| | A · HI10 als code | B · HI10 als "gift card" |
| --- | --- | --- |
| Ontvangers | 882 | 793 |
| Unieke klik (van afgeleverd) | 27 (3,1%) | 20 (2,6%) |
| Klaviyo-toegeschreven orders / omzet | 10 / $3,051 | 4 / $1,067 |
| Toegeschreven omzet per ontvanger | $3.46 | $1.35 |
| Cohort: kopers na W1 (alle orders tot 15 okt 15:35) | 40 (4,5%) | 30 (3,8%) |
| Cohort: omzet / per ontvanger | $10,601 / $12.02 | $7,710 / $9.72 |
| Waarvan binnen 1 uur na W1 (al aan het winkelen) | 22 | 18 |
| Kopers met HI10 | 8 | 5 |
| Gemiddelde order | $265 | $257 |
| Uitschrijvingen | 21 | 21 |

Methode cohort: alle profielen die tussen 9 en 15 okt op de Alia-lijst (Uw8eZG) kwamen, hun Placed Order (RSNxYV) na de eerste W1, variant via `$variation` op Received Email. Fisher exact op kopers p = 0,47, op klik p = 0,55, op toegeschreven orders p = 0,19. Bayesiaans P(B > A) op kopers = 22 procent.

Wat we eruit halen:
- **Geen bewijs dat de gift-card-verpakking helpt**; de richting is zelfs negatief. Dat past bij de theorie (§2): "10%" in een gift-card-jasje is nog steeds 10%, en het woord belooft iets wat het niet is.
- De variant had een claimprobleem: een publieke procentcode als "gift card" tonen is geen gift card (§3). Dat probleem is sinds 15 okt weg, omdat B nu W1 v3 is (beide HI10 als code).
- Twee derde van de welcome-kopers bestelt binnen een uur na W1 (zie ook `research/v6-golive/20-welcome-analyse.md`). Een aanbodtest in W1 meet dus voor een groot deel mensen die al kochten. Het meetplan (§5) houdt daar rekening mee.

### 1.2 Welke codes en aanbiedingen presteerden het best? (90 dagen, 15 juli tot 15 okt 2026)

18,697 orders, omzet $3,96 mln, gemiddelde order $212 (mediaan $149, kwart onder $134, kwart boven $208). 52,7 procent van de orders ligt onder $150 (gemiddeld $127), 47,3 procent op of boven $150 (gemiddeld $314).

| Groep (eerste code op de order) | Orders | Aandeel | Gem. order | Korting per order |
| --- | --- | --- | --- | --- |
| Geen code | 11,286 | 60,4% | $222 | $2 |
| Publieke 10%-codes (verjaardag, sale, merk, 10 codes XXXXXXXX) | 3,405 | 18,2% | $208 | $24 |
| Creator-codes (14 codes XXXXXXXX) | 2,197 | 11,8% | $189 | $32 |
| Overig (handmatig, vervanging, samples) | 584 | 3,1% | $108 | $93 |
| Merkcode 15% (XXXXXXXX) | 369 | 2,0% | $176 | $31 |
| **HI10** | **341** | **1,8%** | **$260** | **$29** |
| Merkcode 5% (XXXXXXXX) | 297 | 1,6% | $253 | $13 |
| Merkcode 25% (XXXXXXXX) | 145 | 0,8% | $204 | $68 |
| Unieke flowcodes (sinds 9 okt) | 73 | 0,4% | $233 | $34 |

- **HI10 heeft de hoogste gemiddelde order van alle 10%-codes** ($260 tegen $208 voor de andere publieke 10%-codes en $222 zonder code). Dat is selectie (welkomstinschrijvers kopen vaker een set), geen bewijs dat 10% de order groter maakt, maar het laat zien dat HI10 geen koopjescode is.
- Diepere codes trekken kleinere orders (15%: $176, creator: $189). Meer procent koopt dus geen grotere mand.
- **Er is in 90 dagen geen enkele dollarcode gebruikt** en in 365 dagen geen enkele campagne met een dollarbedrag, "credit" of "gift card" in naam, onderwerp of preview (236 campagnes met 2,000+ ontvangers). Een dollaraanbod is voor Siraat dus nooit getest; de geplande checkout-test met een $25-code tegen 10% (`klaviyo/flows/02-checkout-abandonment.md`, BACKLOG 2) is nooit gebouwd.
- Campagnes per aanbod (365 dagen, omzet per ontvanger): procentaanbod in onderwerp of preview $0.152 (40 campagnes), geen aanbod $0.120 (169), gift/free $0.120 (27). De beste campagnes van het jaar zijn BFCM 2025 met "62% off" ($0.59 tot $0.64 per ontvanger) en een "gifts for you"-campagne ($0.72). Procent werkt als sitebrede sale-kop.

## 2. Wat het onderzoek zegt

**Rule of 100 (Berger, *Contagious*; Chen, Monroe en Lou 1998).** Onder ~$100 voelt een procent groter, erboven een bedrag. Chen et al. vonden in *Journal of Retailing* dat bij een duur product een korting in dollars als groter werd ervaren dan dezelfde korting in procenten, en omgekeerd bij een goedkoop product. Siraat zit precies op de grens: een pan kost $129 tot $149, dus 10% is $13 tot $15. Dat is klein in beide vormen. Bij sets ($299 tot $599) wint het bedrag duidelijk: "$30 off" klinkt groter dan "10%", "$75 off" groter dan "12,5%".

**Gift card en mental accounting (Helion en Gilovich 2014; Reinholtz, Bartels en Parker 2015).** Geld op een gift card wordt als "vrij geld" geboekt en makkelijker aan iets leuks uitgegeven; met een winkelspecifieke kaart kiezen mensen sterker voor wat typisch is voor die winkel. Dat effect hoort bij **echt opgeslagen tegoed** dat al van jou is (eigendom, verliesaversie bij laten verlopen). Een code die 10% van de prijs haalt, geeft dat gevoel niet; het beeld van een kaart verandert de rekensom niet. Dat verklaart waarom T04-B niets deed.

**Premium-perceptie.** Retailers kiezen beloningen boven korting om niet "altijd in de aanbieding" te lijken (Aberdeen/Hawk-onderzoek: 43 procent noemt dat als reden). Bij Siraat staat er al een permanente compare-at ($439 bij $134), dus nog een procent erbovenop leert vooral dat de prijs onderhandelbaar is. Een bedrag met drempel ("$25 off $150+") of een gift voelt als beloning, niet als prijsverlaging. Klantdata wijst dezelfde kant op: prijs is het grootste bezwaar (27 procent bijna-stop, 47 procent "overpriced"), maar korting in cart-mails trok nauwelijks omzet ($0.79 per ontvanger); prijs rechtvaardigen werkt beter dan prijs verlagen (`.agents/product-marketing.md`, diagnose §6).

**Breakage.** Bij betaalde gift cards blijft 3 tot 12 procent onbesteed (na de CARD Act van 2009 rond 3 tot 5 procent, digitale kaarten minder). Over promotionele tegoeden vonden we geen betrouwbare cijfers; verwacht meer onbesteed dan bij betaalde kaarten, omdat de klant er zelf niets voor betaalde. Reken voor de marge niet op breakage, behandel het als meevaller.

**Concurrenten (eigen inschrijvingen 12 tot 15 okt, plus openbare bronnen).**

| Merk | Welkom | Referral | Wat we leren |
| --- | --- | --- | --- |
| HexClad | Geen code, toegang tot lopende sale ("You're In!"); welkomstmail noemt refer-a-friend | Vriend **$100 off** eerste order (drempel volgens bronnen $300 of $400); verwijzer krijgt **een product** (mengkommen, waarde ~$129), betere gifts bij meer verwijzingen (Rivo). Rivo meldt $450K in 90 dagen en +17% orderwaarde bij verwezen klanten (leveranciersclaim) | Dollar aan de vriend met hoge drempel, product aan de verwijzer. Prijsbezwaar in browse 3 met Affirm, niet met korting |
| Our Place | Geen code, Prime Deals-sale; campagne met cadeau bij $300+ | Volgens openbare bronnen **$20 / $20** met $100 minimum (niet op de eigen site bevestigd) | Kleine dollars, drempel net boven de instapprijs |
| Caraway | **Geen welkomstkorting**; in welkom 2 **$50 off een tweede aankoop van $300+**; sets met vaste dollarbedragen ($95 tot $190 off) zonder code | Bronnen spreken elkaar tegen (15/15 procent, of $100 voor de vriend plus producten voor de verwijzer) | Dollars op sets, beloning voor de tweede aankoop in plaats van korting op de eerste |
| Made In | Inschrijving bevestigd, na dagen nog geen mail; welkomstcode volgens eigen pagina een procent, minimum $149, niet op sets | Geen programma gevonden | Procent met drempel en uitsluitingen |

De officiële referral-pagina's waren vanuit deze omgeving niet bereikbaar; de bedragen hierboven komen uit eigen inbox-registraties (`research/concurrenten/tijdlijn.csv`) en derde bronnen, dus behandelen als indicatie.

## 3. Juridisch en praktisch (US): wat mag "gift card" heten?

**Twee verschillende dingen in Shopify.**

| | Shopify gift card / store credit | Kortingscode (vast bedrag of procent) |
| --- | --- | --- |
| Wat het is | Opgeslagen tegoed, een betaalmiddel | Prijsverlaging op een order |
| Minimumbedrag | Niet mogelijk | Mogelijk |
| Productuitsluiting (geen sets, geen gift cards) | Niet mogelijk | Mogelijk |
| Stapelen | Werkt naast elke kortingscode, dus ook naast HI10 of een creator-code | Instelbaar (`combinesWith`) |
| Verloopdatum | Instelbaar, maar wettelijk beperkt (zie onder) | Vrij |
| Boekhouding | Verplichting op de balans tot besteding of verval; betaalde kaarten zijn omzet pas bij besteding | Geen verplichting; lagere omzet |
| Klaviyo | Geen native unieke gift cards; app of Shopify-flow nodig | Unieke codes via `{% coupon_code %}` (bestaat al) |
| Store credit | Shopify store credit vereist de nieuwe klantaccounts en kan met of zonder einddatum worden uitgegeven | n.v.t. |

**Wetgeving.**
- Federaal (CARD Act, Regulation E 12 CFR 1005.20): betaalde gift cards mogen niet binnen 5 jaar verlopen. Een **promotionele** kaart ("loyalty, award or promotional") is uitgezonderd, mits op de kaart zelf staat dat hij promotioneel is en wanneer het tegoed verloopt.
- Staten: veel staten verbieden verval bij betaalde kaarten. Californië (Civil Code 1749.5) verbiedt verval en fees bij verkochte gift certificates, met een uitzondering voor kaarten die gratis worden gegeven in een award-, loyalty- of promotieprogramma, mits de vervaldatum in hoofdletters en minimaal 10 punt op de voorkant staat. De wijziging SB 22 (in werking 1 april 2026) zet elektronische gift cards expliciet onder de wet; of de promotie-uitzondering ongewijzigd is gebleven, hebben we niet in de geconsolideerde tekst kunnen nalezen. Laat dit bevestigen voordat we promotionele gift cards met einddatum uitgeven.
- FTC (sectie 5, "net impression", en de gids voor het woord "free"): als een "gift card" alleen werkt boven een bedrag, niet op sets of niet naast andere aanbiedingen, dan wekt het woord een verkeerde indruk. Dat levert ook supporttickets op ("my gift card doesn't work"); die zien we nu al bij codes ("the discounts were never applied", CRO-audit).

**Onze claimregels** (`content/facts/claims.csv`): HI10 staat als "owner-override" met de omschrijving "10% off on top of the current sale". "Gift card" staat nergens als goedgekeurde claim; de regels vragen echte cijfers, echte deadlines en nooit een asterisk. Een "gift card" met kleine lettertjes is precies de asterisk die we niet willen. De oude welcome-v3-spec (7 okt) stelde een "$25 gift card" voor die in werkelijkheid een unieke code met $149 minimum en 14 dagen was; die naam klopt dus niet. Hetzelfde geldt voor de geplande checkout-mail "there's $25 in your account" met een code van 72 uur: een code staat niet "in your account".

**Naamgeving, voorstel voor DECISIONS:**

| Wat het technisch is | Mag heten | Mag niet heten |
| --- | --- | --- |
| Echte Shopify gift card (gekocht, of door ons uitgegeven als tegoed zonder minimum) | "Siraat gift card", "$25 gift card", gouden kaartbeeld | |
| Shopify store credit op het klantaccount | "$25 store credit", "$25 in your account" | "gift card" als het een einddatum heeft en dat niet op de kaart staat |
| Kortingscode met vast bedrag | "$25 off", "$25 off your first order of $150+", "your $25 welcome offer" | "gift card", "credit", "in your account", "cash" |
| Kortingscode met procent | "10% off on top of the sale", "extra 10%" | "gift card", "gift" |
| Gratis product bij de order | "gift", "free gift" (filter: "chance to win") | |

**Gouden kaart van Floris:** inzetten op echte gift cards (verwijzer, flow 09, december). Voor een welkomst- of winback-aanbod in dollars een kopie laten maken met "$25 OFF" of "WELCOME" in plaats van "GIFT CARD" (origineel niet aanpassen, DECISIONS 7 okt). Check vóór gebruik dat monogram en woordmerk op de kaart overeenkomen met `brand/logo/lockup/` (het beeld is gegenereerd, het logo erop is dus nagebouwd).

## 4. Advies per moment

Aannames voor de marge (Floris bevestigt): brutomarge 60 procent van de verkoopprijs, dus kostprijs plus verzending 40 procent. Bij 65 procent (beleid/02) verschuiven de getallen licht maar niet de volgorde. Prijzen: Pan Pro Standard $134, pan met deksel $154, 6-delige fall-set $299, 12-delig $599.

### 4.1 Welcome (W1 en verder)

| | Advies |
| --- | --- |
| Vorm | **Procent blijft de controle** (HI10, 10% bovenop de sale, geen minimum). Testen tegen **vast bedrag met drempel** |
| Hoogte | B: $25 off |
| Minimum | $150 (net boven de losse pan; pan met deksel $154 haalt het) |
| Naam | "Your $25 welcome offer" / "$25 off your first order of $150+". Niet "gift card" |
| Code | Unieke code per profiel (XXXXXXXX), 14 dagen, eenmalig, niet combineerbaar. Echte deadline, dus W5 mag "expires" zeggen |
| Waarom niet direct overstappen | 52,7 procent van de orders ligt onder $150. Voor de losse-pankoper is "$25 off $150+" een drempel, geen cadeau; dat kan conversie kosten. Alleen een test laat zien of de hogere mand en de grotere set-korting dat goedmaken |

Rekenvoorbeeld per order:

| Mand | Met HI10 | Met $25 off $150+ |
| --- | --- | --- |
| Losse pan $134 | betaalt $120.60, marge $67.00 | geen korting: betaalt $134, marge $80.40, of haakt af |
| Pan met deksel $154 | betaalt $138.60, marge $77.00 | betaalt $129, marge $67.40 |
| 6-delige set $299 | betaalt $269.10, marge $149.50 | betaalt $274, marge $154.40 |
| 12-delige set $599 | betaalt $539.10, marge $299.50 | betaalt $574, marge $334.40 |

Marge = betaald min 40 procent van de prijs vóór code. B verliest $9.60 per pan met deksel en wint bij sets ($4.90 tot $34.90). De grote post is de losse pan (52,7 procent van de orders): wie in B toch koopt, betaalt de volle $134 en levert $13.40 meer marge op; wie door de drempel afhaakt, kost $67. Breakeven: B is gelijk zolang **minder dan ongeveer 17 procent van de losse-pankopers afhaakt** (53 × (1 - x) × $80.40 = 53 × $67). Elke losse-pankoper die naar een set gaat, levert daarbovenop ongeveer $87 extra op. De test moet dus vooral meten hoeveel losse-pankopers B verliest. Een **echte** $25 gift card zonder minimum voor iedereen raden we af: stapelbaar met HI10 en creator-codes (losse pan: $134 → $95.60, marge $42), verplichting op de balans, staatsregels voor verval, en Klaviyo kan hem niet zelf maken.

### 4.2 Referral, vriend

| | Advies |
| --- | --- |
| Vorm | Vast bedrag |
| Hoogte | $25 off |
| Minimum | $150 |
| Naam | "$25 off your first Siraat order of $150+, from {naam}" |
| Code | Unieke code per verwijzing, eenmalig, alleen nieuwe klanten, niet combineerbaar met andere codes |

Rekenvoorbeeld: gemiddelde order boven $150 is $314 na korting; neem een fall-set van $299: vriend betaalt $274, marge $154. Ter vergelijking: een nieuwe klant via betaalde ads kost bij NC-ROAS 1,62 en een order van $212 ongeveer $131 aan advertenties, terwijl de order $127 marge oplevert (bijna nul na ads). Een verwezen klant met $25 korting plus $25 verwijzerbeloning kost hooguit $50. **Referral is per nieuwe klant ruim twee keer goedkoper dan betaald verkeer.** Our Place ($20 bij $100+) en HexClad ($100 bij $300+, 25 tot 33 procent) zitten aan weerszijden; $25 bij $150 is 17 procent bij de drempel en rond 8 procent bij een set.

### 4.3 Referral, verwijzer

| | Advies |
| --- | --- |
| Vorm | **Echte Siraat gift card** (Shopify gift card of store credit), hier mag het woord en het gouden beeld |
| Hoogte | $25 per geslaagde verwijzing; eventueel trap (3 verwijzingen = product, zoals HexClad) |
| Minimum | Geen (het is tegoed) |
| Wanneer | Na de 30-dagen-retourtermijn van de vriend, zodat een retour geen beloning oplevert |
| Verval | Bij voorkeur geen. Wil Floris een einddatum, dan "promotional" en de datum op de kaart zelf, in hoofdletters (Californië, Reg E) en eerst juridisch laten bevestigen |
| Naam | "Your $25 Siraat gift card. Thank you for sharing." |

Kosten: $25 aan tegoed kost bij besteding aan producten met 60 procent marge ongeveer $10 aan inkoop, of $25 als het een aankoop vervangt die de klant toch zou doen. Breakage is een meevaller, geen plan. Let op: er is nog geen referral-programma (product-marketing, backlog A13); niets beloven in mails tot Floris een app kiest (Rivo, Smile, Okendo of vergelijkbaar) en de voorwaarden vastlegt.

### 4.4 Winback (R2, R2-VIP)

| | Advies |
| --- | --- |
| Vorm | Vast bedrag tegen de huidige 10% (unieke code, 72 uur) |
| Hoogte | $20 off (VIP: $30 off tegen de huidige 15%) |
| Minimum | $100 |
| Naam | "$20 off your next piece". Alleen "store credit" of "in your account" als we echt Shopify store credit uitgeven |
| Waarom | De tweede aankoop is een deksel-pan ($154), pot ($149), utensils ($149) of tweede pan ($129 tot $139): net boven $100, waar een bedrag groter voelt dan 10% ($13 tot $15) |

Rekenvoorbeeld pan met deksel $154: met 10% betaalt de klant $138.60, marge $77.00; met $20 betaalt hij $134, marge $72.40. B moet **6,4 procent meer kopers** halen om gelijk te spelen. VIP met set $299: 15% geeft marge $134.55, $30 off geeft $149.40; daar wint het bedrag zelfs zonder extra kopers. Wacht met deze test tot T02 (code tegen geen code) een besluit geeft: als winback zonder code even goed verkoopt, vervalt de vraag.

### 4.5 BFCM

| | Advies |
| --- | --- |
| Kop | **Procent, sitebreed** ("up to 50% off", gebaseerd op echte compare-at). Dat is de vorm die historisch het best verdiende (62% off, $0.59 tot $0.64 per ontvanger) |
| Extra laag | **Dollartrap voor sets**: "extra $30 off $299+, extra $75 off $599+" tegen "extra 10%". Bij $299 gelijke kosten ($30 tegen $29.90), bij $599 kost de trap $15 meer maar voelt veel groter |
| Minimum | Per trede |
| Naam | "Extra $75 off the 12-piece set". Geen "gift card" |
| HI10 | Eenmalig per klant; tijdens BFCM niet stapelen met de trap |
| Gift card verkopen | Flow 09 (GC1 tot GC3, 15 tot 23 december): echte e-gift cards, het gouden beeld hoort hier. Bonus ("buy a $150 gift card, get $25 off in January") als **kortingscode met januari-einddatum**, niet als tweede gift card: dan geen staatsregels voor verval en geen verplichting op de balans |

Rekenvoorbeeld 12-delig $599 (sale) met trap: betaalt $524, marge $284.40; met extra 10%: betaalt $539.10, marge $299.50. De trap kost $15 marge per set en moet dus 5 procent meer sets verkopen. Bij de 6-delige set zijn ze gelijk.

### 4.6 Andere cadeau-momenten

- **Kerst en Moederdag:** echte gift cards verkopen (flow 09). De koper krijgt de G1/G2-mails; Shopify mailt de ontvanger. Gouden beeld plus bedragen $25 tot $200; "never expires" mag alleen als de kaarten zo zijn ingesteld (nu te controleren in Shopify).
- **Review- of Trustpilot-beloning:** als dit een gift card is (DECISIONS 7 okt: Floris accepteert het risico), dan een echte gift card zonder minimum, anders "$X off".
- **Giveaway "Win your order":** de prijs is een terugbetaling, geen gift card. Niet mengen in beeld of tekst.

## 5. Voorgestelde test: T06 · W1, 10% tegen $25 off $150+

**Hypothese.** Een vast bedrag met drempel ($25 off $150+) levert per W1-ontvanger meer marge op dan HI10, omdat het de mand naar pan met deksel en sets duwt en bij sets groter voelt, ook als iets minder mensen kopen.

**Opzet.**
- Plek: W1 in v4 · Welcome (T4a5Mk), na afloop van de lopende v2/v3-test. Winnende W1-template als basis; alleen het aanbodblok, de codebalk, de hero-aanbodbalk en één regel in W5 verschillen.
- A: HI10, 10% bovenop de sale, geen minimum (huidig).
- B: unieke code (XXXXXXXX), $25 off bij $150+, 14 dagen, eenmalig, niet combineerbaar; W5 noemt de echte vervaldatum. Beeld: kopie van het gouden beeld met "$25 OFF" of "WELCOME", niet "GIFT CARD".
- Toewijzing: willekeurige 50/50-split bovenaan de prospect-tak (niet de A/B-kaart op één mail), zodat W1 tot en met W5 per arm consistent zijn. Arm op het profiel vastleggen (`offer_arm`).
- Alleen US (beide aanbiedingen in dollars); INT blijft HI10.
- Wat B-ontvangers met HI10 doen (staat op couponsites) wordt gemeten, niet geblokkeerd: dat is de echte wereld.

**Meetplan.**

| | Metric | Bron |
| --- | --- | --- |
| Primair | **Marge per ontvanger binnen 14 dagen na W1** = (omzet na korting min 40% van de omzet vóór korting) / ontvangers, over **alle** orders, niet alleen toegeschreven | Placed Order per profiel (cohort zoals §1.1), korting uit `Total Discounts` |
| Secundair | Koperspercentage; gemiddelde order; aandeel orders >= $150; aandeel orders met set; gebruik van de eigen code per arm | idem |
| Uitsplitsing | Kopers binnen 1 uur na W1 apart (waren al aan het winkelen) tegen na 1 uur; daar hoort het effect te zitten | idem |
| Guardrails | Uitschrijving W1 tot W5 (niet meer dan +20% relatief), spam, refunds binnen 30 dagen per arm, Gorgias-tickets met "code"/"gift card"/"doesn't work" | Klaviyo, Gorgias YzvjGf |
| SRM-check | Verhouding ontvangers 50/50 binnen 3 procentpunt | flow-values-report per pad |

**Omvang en duur.** Basis 4,5 procent kopers per W1-ontvanger (T04-A). Om een verschil van 20 procent relatief in koperspercentage te zien (80 procent power, 5 procent significantie) zijn ruim 8,000 ontvangers per arm nodig; W1 haalt ongeveer 1,900 per week in totaal (US iets minder). Dat is 9 tot 10 weken. Daarom beslissen op de marge per ontvanger met een Bayesiaanse regel, zoals in `research/testing/05-beslisregels.md`: **B wint als P(B beter op marge per ontvanger) >= 90 procent en de guardrails groen zijn**; A blijft bij P(A beter) >= 80 procent of op 31 januari 2027. BFCM-weken (23 nov tot 2 dec) tellen niet mee, de test loopt wel door.

**Vóór de start (door Floris, niet door de agent):** Shopify-korting met vast bedrag $25, minimum $150, eenmalig per klant, niet combineerbaar, als Klaviyo coupon voor unieke codes; kopie van het gouden beeld met "$25 OFF"; akkoord op de naam "$25 welcome offer" in DECISIONS.

**Volgende tests, in volgorde:** (1) winback $20 off $100+ tegen 10% na T02; (2) BFCM-campagnesplit extra 10% tegen dollartrap (een campagne, 50/50, primair omzet en marge per ontvanger, secundair aandeel sets); (3) referral pas als het programma bestaat: vriend $25 tegen $20, verwijzer gift card tegen product.

## 6. Open voor Floris

1. Brutomarge per pan en per set (alle rekenvoorbeelden gaan uit van 60 procent).
2. Akkoord op de naamgevingstabel (§3) als DECISIONS-regel: "gift card" alleen voor echte gift cards.
3. Staan de verkochte e-gift cards in Shopify op "never expires"? (GC1 belooft dat.)
4. Referral-app en voorwaarden (wie, hoeveel, na hoeveel dagen).
5. Kopie van het gouden beeld met "$25 OFF" of "WELCOME" voor dollaraanbiedingen die geen gift card zijn.
6. Juridische check Californië na SB 22 als we ooit promotionele gift cards met einddatum willen uitgeven.

## Bronnen

- Berger, J., *Contagious* (2013), Rule of 100: [shortform.com/blog/rule-of-100](https://www.shortform.com/blog/rule-of-100/), [jonahberger.com](https://jonahberger.com/fuzzy-math-what-makes-something-seem-like-a-good-deal/)
- Chen, S.-F. S., Monroe, K. B. en Lou, Y.-C. (1998), The effects of framing price promotion messages on consumers' perceptions and purchase intentions, *Journal of Retailing* 74(3), 353-372: [experts.illinois.edu](https://experts.illinois.edu/en/publications/the-effects-of-framing-price-promotion-messages-on-consumers-perc/)
- Helion, C. en Gilovich, T. (2014), Gift cards and mental accounting: green-lighting hedonic spending, *Journal of Behavioral Decision Making* 27(4), 386-393: [metatoc.com](https://metatoc.com/papers/26968-gift-cards-and-mental-accounting-green-lighting-hedonic-spending)
- Reinholtz, N., Bartels, D. M. en Parker, J. R. (2015), *Journal of Consumer Research*: [PDF](https://home.uchicago.edu/~bartels/papers/Reinholtz-Bartels-Parker-2015-JCR.pdf)
- Aberdeen/Hawk Incentives over beloning tegen korting: [emarketer.com](https://www.emarketer.com/content/why-some-retailers-prefer-reward-based-promotions)
- Breakage: [Kroll](https://www.kroll.com/-/media/assets/pdfs/news/tax-services/unclaimed-property-the-votes-are-in.pdf), [beancount.io](https://beancount.io/blog/2026/05/17/gift-card-breakage-revenue-accounting-asc-606-retailers-restaurants-liability-redemption-proportionate-method-escheatment-guide)
- Regulation E 12 CFR 1005.20: [eCFR](https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-A/section-1005.20), [CFPB interpretatie](https://www.consumerfinance.gov/rules-policy/regulations/1005/interp-20/), [Pillsbury](https://www.pillsburylaw.com/en/news-and-insights/card-act-loyalty-award-and-promotional-card-code-and-other.html)
- Californië Civil Code 1749.5 en SB 22 (2025): [california.public.law](https://california.public.law/codes/ca_civ_code_section_1749.5), [legiscan SB22](https://legiscan.com/CA/text/SB22/2025)
- Shopify: [Issuing free gift cards](https://help.shopify.com/en/manual/products/gift-card-products/issue-gift-card), [Store credit](https://help.shopify.com/en/manual/customers/store-credit), [Gift card terms](https://www.shopify.com/legal/terms-gift-cards)
- HexClad referral: [Rivo case study](https://www.rivo.io/case-studies/hexclad), [coupons.com](https://www.coupons.com/coupon-codes/hexclad)
- Our Place, Caraway, Made In: [coupons.com Our Place](https://www.coupons.com/coupon-codes/our-place), [Tom's Guide Caraway](https://www.tomsguide.com/home/home-appliances/kitchen-dining/caraway-home-coupon-codes), [TechRadar Caraway](https://www.techradar.com/coupons/caraway), [Made In discount page](https://madeincookware.com/pages/discount-code)
- Eigen: `research/concurrenten/tijdlijn.csv` en `overzicht.md` (inschrijvingen 12 tot 15 okt), `research/v6-golive/20-welcome-analyse.md`, `research/cro/01-funnel.md` en `03-checkout-audit.md`
