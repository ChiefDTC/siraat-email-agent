# UX-spec urgentie-sprint (6 mails)

Datum: 8 november 2026. Rol: UX. Alleen gelezen en geschreven, niets in Klaviyo of Shopify gewijzigd, geen testmails.

Bronnen: `../BRIEF.md`, PLAYBOOK §1, §2, §10 tot §12, DECISIONS (BF 31 okt, geel alleen voor sale-tags 5 nov, alles klikbaar 6 nov, 5 gifts 7 nov), `research/plannen/2026-11-urgentie.md`, `research/plannen/2026-11-punten-store-credit.md`, `research/homestead/2026-11-e5-e6/ux.md`, `research/cro/01-funnel.md` (PDP-timer), de previews van `klaviyo/templates/v3/campaigns/win-order-back-1104/` (wb-us-c2, wb-us-b-letter) en `klaviyo/templates/v3/flows-nov/signup/` (bfw3), en de blokken in `klaviyo/templates/partials/blocks/` (deadline, deadline-line, codebar, bf-topbar, bf-cta, gifts5).

Voor de designer: elk blok hieronder bestaat al als partial of is een kleine variant ervan. Maten zijn CSS-pixels op 375 px breed (iPhone SE/mini, Gmail- en Apple Mail-app). Waar "ET" staat: zie §2.4 over tijdzones.

---

## 0. Diagnose: waarom wel opens en geen kliks

Cijfers (urgentie.md, 14 dagen): opens 36 tot 49 procent, kliks 0,24 tot 1,13 procent. De twee beste mails hadden een echte deadline ("Win your order back (today only)" US $0,171 per ontvanger, "The October sale ENDS TONIGHT" $0,166).

Wat we zien in de bestaande ontwerpen op 375 px:

1. **De deadline staat niet in het eerste scherm.** In wb-us-c2 (de winnaar) staat "today" alleen in de onderwerpregel en in de eyebrow "FLASH DEAL". Het woord "tonight" of een tijd staat nergens boven de vouw. De lezer opent omdat het onderwerp urgent is, ziet dan een algemene salemail en sluit.
2. **Lange mails.** bfw3 is 5.294 px hoog, bijna 1,5 keer de grens van 3.600 px (PLAYBOOK §12). Hoe langer de mail, hoe meer de knop een van de vele dingen wordt.
3. **Het grootste vlak is niet klikbaar.** Hero-tekst als achtergrondbeeld met live tekst erover (c2) is alleen klikbaar op de knop. Wie op de kop of de pan tikt, gebeurt niets. Besluit 6 nov (alles klikbaar) is nog niet overal doorgevoerd.
4. **Te veel verschillende doelen.** Raster van 6 producten plus gifts plus reviews plus knop: elke tegel is een andere bestemming, niemand klikt. Een urgentiemail heeft één actie.
5. **Wat de klik oplevert is onduidelijk.** "Shop VIP Black Friday" zegt niet wat er na de tik gebeurt (is de korting al toegepast, waar kom ik, krijg ik de gifts).

Daarom: elke mail in deze set beantwoordt binnen het eerste scherm drie vragen, in deze volgorde: **wat eindigt wanneer** (deadline), **wat krijg ik** (aanbod met getal), **waar tik ik** (knop, en het hele hero-vlak).

---

## 1. Algemene regels (alle 6 mails)

### 1.1 Het eerste scherm: 560 px

Ontwerp voor een **harde vouw op 560 px**. Reden: iPhone SE/mini heeft 667 px viewport; Gmail-app en Apple Mail nemen 90 tot 110 px voor de kop met afzender en onderwerp. Grotere telefoons (844 px) zien dan meer, nooit minder.

Vaste volgorde en pixelbudget (verkoopmails 1, 2, 3, 5, 6):

| # | Blok | Hoogte op 375 | Eindigt op | Inhoud |
|---|---|---|---|---|
| 1 | Deadline-topbalk (`bf-topbar`, ink) | 40 | 40 | Deadline in caps, bv. "ENDS TONIGHT 11:59 PM ET". Hele balk is een link. |
| 2 | Vaste header (lockup, nav verborgen op mobiel) | 70 | 110 | `partials/header.html`, niets aan veranderen. |
| 3 | Eyebrow | 30 | 140 | Wat voor deal: "24-HOUR FLASH DEAL", "VIP ONLY", "YOUR STORE CREDIT". |
| 4 | Kop (live tekst, 2 regels) | 100 | 240 | Het aanbod als getal: "$249 for 2 pans + 2 lids", "Your $12 expires tonight". |
| 5 | Deadline-regel of deadline-tegels | 50 tot 90 | 290 tot 330 | Zie §2. Altijd live tekst. |
| 6 | Productbeeld of aanbodvisual (optioneel) | 0 tot 150 | max 440 | Alleen als het product het aanbod is (flash, gifts, draw). Uitsnede 2:1 of 16:9, niet vierkant. |
| 7 | Knop 1 | 56 | max 500 | Zie §1.3. |
| 8 | Friction reducer | 30 | max 530 | 13/18 px, één regel. |

Harde eisen, ook als het budget knelt:
- **Knop 1 eindigt uiterlijk op 520 px.** Past het niet, dan gaat eerst het beeld (blok 6) onder de knop, niet de deadline.
- **Deadline en aanbod staan als live tekst in het eerste scherm**, ook als ze in de hero-afbeelding staan. Beelden worden geblokkeerd (Outlook zakelijk, sommige Gmail-instellingen) en zijn niet leesbaar voor schermlezers.
- **Geen vierkante hero van 375 px hoog boven de knop.** Dat duwt de knop altijd onder de vouw (1:1 op 375 = 375 px beeld alleen). Een vierkant productbeeld mag, maar dan onder knop 1.
- Kop live, niet als PNG in TT Ramillas: in deze set weegt leesbaarheid en dark mode zwaarder dan het font. Inter 800, 36/40 px op mobiel (40/44 op desktop), ink of wit op ink. Wil Floris de TT Ramillas-kop, dan als PNG naast een live kop met dezelfde tekst in de alt en een `display:none`-vrije fallback, en dan telt het beeld als blok 6.

### 1.2 Stijl van het eerste scherm: licht of donker

Twee varianten, kies per mail (zie §3):

- **Donker vlak** (zoals wb-us-c2, de winnaar): hero-vlak ink #272727 of espresso #321E1D, tekst wit, eyebrow goud #B8862B (alleen als decoratie, 4,6:1 op ink), knop wit met ink tekst (DECISIONS 5 nov). Voordeel: overleeft dark mode zonder schade, voelt als "event". Voor FLASH, VIP en GIFTS.
- **Licht vlak** (crème #F8F7F2 kolom, wit vlak): kop ink, knop ink met witte tekst. Voor CREDIT (persoonlijk, briefachtig) en DRAW.

Geel #FFB800 alleen op sale-tags ("-63%", "70% OFF") met ink tekst (8,6:1). Nooit als knop, balk of tekst op wit (1,7:1). Let op: wb-us-c2 heeft nog een gele topbalk en gele knop; dat is van voor het besluit van 5 nov en wordt in deze set ink.

### 1.3 Knoppen: aantal, plaats, vorm

- **Eén actie per mail, één bestemming.** Elke link in de mail (topbalk, hero, beeld, knoppen, P.S.) gaat naar dezelfde URL, met eigen `utm_content`. Uitzondering: de link "Official rules" in DRAW en de voorwaardenregel in CREDIT.
- **Aantal knoppen**: 2 in mails tot ~2.400 px, 3 in mails boven 2.400 px. Knop 1 boven de vouw, knop 2 direct na het bewijs (reviews of gifts), knop 3 onderaan voor de footer. Altijd dezelfde tekst, of knop 3 met de deadline erin ("Before 11:59 PM tonight").
- **Maat**: volle breedte min 2 x 24 px gutter = 327 px op 375 (desktop 360 px, zoals `bf-cta`), hoogte 56 px, radius 28 px (pil). Minimaal 48 px tikhoogte, minimaal 16 px verticale ruimte tot de volgende link.
- **Kleur**: op licht ink #272727 met witte tekst (14,9:1); op donker wit met ink tekst. Een nieuwe variant van `bf-cta` met `btnbg` en `btncolor` (nu hard geel); VML-roundrect voor Outlook met dezelfde kleuren.
- **Tekst**: Inter 16 px, 800, letter-spacing 1 px, caps, max 26 tekens zodat hij op 327 px op één regel past. Ik-vorm met het voordeel: "GET MY 2 PANS FOR $249", "USE MY EXTRA 10%", "USE MY $12 NOW", "CLAIM MY 5 GIFTS", "ORDER AND ENTER THE DRAW". Geen "Shop now" (alleen receptmails, DECISIONS 9 okt).
- **Pijl** "→" als HTML-entiteit `&rarr;` achter de tekst; niet in de VML-versie.
- Onder elke knop de friction reducer (PLAYBOOK §12): bij een code `{{FRICTION:code}}`, anders `{{FRICTION}}`.

### 1.4 Tikvlakken: het hele hero-vlak is klikbaar

DECISIONS 6 nov: elk beeld en elk beeldblok is klikbaar. Voor deze set strenger: **alles in blok 1 tot 8 linkt naar dezelfde URL.**

Bouwwijze (geen `<a>` om een `<table>`, dat breekt in Outlook en sommige Gmail-versies):
- Topbalk: de tekst in de `<td>` als `<a style="display:block;color:inherit;text-decoration:none">` met padding 11px 20px op de `<a>`, niet op de `<td>`, zodat de hele balk tikbaar is.
- Eyebrow, kop, deadline-regel: elk een eigen `<a style="display:block;...">` met dezelfde href. Geen onderstreping, kleur inherit.
- Beeld: `<a><img style="display:block;width:100%"></a>` (link_all in build doet dit al).
- Deadline-tegels: de buitenste `<td>` krijgt per tegel een `<a style="display:block">` om de inhoud.
- Achtergrondbeeld met tekst erover (zoals c2): niet gebruiken in deze set. Het achtergrondbeeld zelf is niet klikbaar en Outlook toont het alleen via VML. Gebruik een gewoon `<img>` en daaronder een effen ink-vlak met live tekst.
- UTM per vlak: `utm_content=topbar`, `hero-kop`, `hero-deadline`, `hero-img`, `cta1`, `cta2`, `cta3`, `ps`. Dan zien we na de verzending welk vlak klikt (PLAYBOOK, research/testing/04-utm.md).

### 1.5 Maximale hoogte

- Grens: **3.600 px op 375 px breed inclusief footer** (~550 px). Doel per mail staat in §3; de meeste mails horen rond 2.200 tot 2.800 px.
- Maximaal 2 grote onderdelen per mail (productraster, gifts-raster, vergelijking, value stack).
- Gmail knipt mails boven 102 KB HTML af ("[Message clipped]"); de deadline in de footer-zone wordt dan niet gezien en de afmeldlink valt weg. Doel: gerenderde Klaviyo-HTML onder 80 KB. Geen `xsell` (35 KB) in deze set.
- Totaal beeldgewicht onder 800 KB, hero onder 300 KB, countdown-GIF onder 150 KB.

### 1.6 Typografie en contrast

| Element | Maat mobiel | Kleur | Contrast |
|---|---|---|---|
| Kop | Inter 800, 36/40 px | ink op licht, wit op ink | 14,9:1 |
| Bodytekst | Inter 400, 16/24 px (nooit kleiner) | ink #272727 | 13,9:1 op crème |
| Deadline-regel | Inter 700, 16/22 px | brick #AC3B19 op wit/crème, of wit op ink | 5,8:1 en 14,9:1 |
| Eyebrow | Inter 700, 12/16 px, spatiëring 2 px | brick op licht, goud #B8862B op ink | 6,2:1 en 4,6:1 |
| Friction reducer | 13/18 px | #727272 op wit | 4,8:1 (op crème 4,5:1, net AA) |
| Juridische regel (CREDIT, DRAW) | 12/17 px | #727272 op licht | 4,8:1 |
| Topbalk | 12/16 px, 800, caps | wit op ink | 14,9:1 |

Niet doen:
- Legal-grijs #9A948B op wit of crème: 3,0:1, haalt AA niet. Alleen op de donkere footer (4,9:1).
- Goud #B8862B als tekst op wit (3,2:1). Alleen op ink.
- Deadline alleen via kleur (rood) laten opvallen: de tekst moet zelf "tonight" of de tijd noemen.
- Tekst kleiner dan 12 px. iOS vergroot tekst onder 13 px soms zelf en breekt dan de regel.

### 1.7 Dark mode

Onze templates zetten `color-scheme: light`. Apple Mail respecteert dat (blijft licht); Gmail-app iOS en Android en Outlook-app negeren het en keren lichte vlakken om. Regels:

- **Donkere vlakken blijven donker** in alle clients. Daarom donker eerste scherm voor FLASH, VIP en GIFTS.
- **Kleur altijd als `bgcolor` plus inline `background-color`** op `<td>` en `<table>` (PLAYBOOK §6). Gmail keert dan consequent om; een gekleurde div niet.
- **Logo**: de vaste lockup staat in de header op lichte achtergrond. Gmail dark maakt de achtergrond donker, het zwarte PNG blijft zwart en verdwijnt bijna. Header niet aanpassen (CLAUDE.md), maar wel testen in Gmail iOS dark; als het lockup onleesbaar is, een PNG met 1 px lichte rand of een lichte plaat erachter vragen aan Floris. Dit geldt voor alle mails, niet alleen deze set.
- **Beelden met transparantie** (gift-tegels, sticker, sale-tag als PNG): altijd met eigen achtergrond geëxporteerd, nooit transparant op crème.
- **Countdown-GIF**: met ingebakken ink-achtergrond en witte cijfers, dan ziet hij er in licht en donker hetzelfde uit.
- **Knop op licht vlak** (ink met wit): Gmail dark keert ink naar lichtgrijs met donkere tekst; dat blijft leesbaar. Niet zelf proberen te sturen met `[data-ogsc]`-hacks.
- Test op: Apple Mail iOS licht en dark, Gmail iOS dark, Gmail Android dark, Outlook iOS dark (`qa_mail_shots.js` modus `gmailios` en een handmatige preview-send naar een interne inbox op akkoord van Floris).

### 1.8 Overige toegankelijkheid

- `lang="en"` op `<html>`, `role="presentation"` op alle layouttabellen (staat al in de basis).
- Kop als `<h1>` met inline reset (margin 0, zelfde font), zodat schermlezers de kop vinden.
- Alt-tekst noemt het aanbod en de deadline letterlijk: `alt="Titanium Hammered Pan Pro, 2 pans and 2 lids, $249, deal ends tonight at 11:59 PM ET"`. Countdown-GIF: `alt="Deal ends tonight at 11:59 PM ET"`.
- Linktekst zonder "click here". Topbalk-link leest als zin.
- Preheader direct na `<body>` (verborgen div, zoals nu), max 90 tekens, met de deadline als die niet in het onderwerp staat.
- Animatie: een countdown tikt 1 keer per seconde; geen knipperende elementen, niets sneller dan 3 keer per seconde (WCAG 2.3.1).
- Klaviyo genereert de platte-tekstversie: na het bouwen controleren dat de deadline en de link erin staan (vooral bij de Benjamin-brief).

---

## 2. Countdown: hoe tonen we de deadline

### 2.1 Opties

| | A. Statische deadline-regel (live tekst) | B. Live countdown-GIF (Sendtric, NiftyImages, MotionMail, Countdownmail) | C. Deadline in het hero-beeld gebakken |
|---|---|---|---|
| Wat | "Ends tonight at 11:59 PM ET" als HTML-tekst, of de bestaande tegels uit `deadline` (TONIGHT · 11:59 PM · SUN) | Een beeld-URL op de server van de dienst; bij elke open rekent de server de resterende tijd uit en stuurt een GIF van ~60 frames | Tekst in de PNG/JPG |
| Altijd juist | Ja, mits de tekst de echte backend-tijd noemt | Bij openen ja; daarna verouderd tot de mail opnieuw geopend wordt | Ja, maar onleesbaar als beelden uit staan |
| Beelden uit / Outlook zakelijk | Werkt | Niets te zien, alleen alt | Niets te zien |
| Outlook Windows desktop | Werkt | Toont alleen het eerste frame (statisch); de dienst moet frame 1 juist zetten | Werkt |
| Apple Mail Privacy Protection | Werkt | Apple haalt beelden vooraf op via een proxy bij aflevering; bij heropenen kan de klok de stand van dat moment tonen in plaats van nu. Bekend probleem, niet volledig te sturen | n.v.t. |
| Gmail | Werkt | Gmail haalt beelden via de eigen proxy; werkt meestal per open, kan bij snel heropenen gecachet zijn | Werkt |
| Dark mode | Volgt de mail | Vast beeld, kies ink-achtergrond | Vast beeld |
| Schermlezer | Leest de tekst | Alleen alt | Alleen alt |
| Na de deadline | Blijft "tonight" zeggen (oud bericht) | Toont 00:00:00 of een eigen "verlopen"-beeld, dat is eerlijker voor wie later opent | Blijft staan |
| Per ontvanger een eigen eindtijd | Ja, via Klaviyo-variabele | Sendtric en MotionMail: één vaste eindtijd per timer. NiftyImages en Countdownmail: eindtijd via een parameter in de URL, dus te vullen met een Klaviyo-variabele (volgens hun documentatie; eerst in een proefaccount controleren) | Nee |
| Bezorgbaarheid | Geen risico | Extra beeldhost in de mail, ~50 tot 150 KB. Op zich geen spamsignaal; wel: beeld nooit linken naar het domein van de dienst, altijd naar siraatskitchen.com, en nooit als enig beeld in een tekstmail | Zwaarder beeld |
| Klikeffect | Basis | Smooche gebruikt het ("Final hours", countdownmail.com). Branchecijfers wijzen op meer kliks, maar we hebben geen eigen meting | Basis |
| Kosten en werk | Geen | Sendtric: gratis versie met eigen merk in de GIF, betaalde versie zonder. MotionMail en NiftyImages: gratis instap, betaald voor meer opens of personalisatie. Prijzen nog te checken. Extra account voor Floris | Per mail een nieuw beeld |

### 2.2 Aanbeveling (veilige standaard)

1. **Standaard in alle 6 mails: optie A, de deadline als live tekst op drie plekken**: in de topbalk, in de hero (regel of tegels, direct boven knop 1) en in of onder de laatste knop. Altijd juist, werkt overal, geen derde partij.
2. **Live countdown-GIF alleen als extra laag, en alleen waar de deadline één vast moment is voor de hele verzending**: FLASH (mail 1) en GIFTS (mail 5) op de echte einddag. Niet in de Benjamin-brief (mail 4: daar breekt elk beeld het briefgevoel), niet in CREDIT zolang de vervaltijd per profiel verschilt (dan alleen NiftyImages met URL-parameter, na een proef).
3. **Eerst testen, niet meteen standaard**: in FLASH een A/B met en zonder GIF (de rest gelijk), winnaar op unieke kliks en omzet per ontvanger, nooit op opens. Urgentie.md vraagt Floris al of een aftelklok mag (open vraag 3); zonder zijn ja geen GIF.
4. **Keuze dienst**: Sendtric (betaalde versie, zonder merk) voor vaste eindtijden: eenvoudigste, één URL in een Klaviyo-beeldblok of `<img>`. NiftyImages als we persoonlijke vervaltijden willen (VIP-code, tegoed). Countdownmail.com is wat Smooche gebruikt, functioneel gelijk.
5. **Eisen aan de GIF als hij erin komt**:
   - Formaat 600 x 140 (geleverd 1200 x 280), ink #272727-achtergrond, cijfers wit Inter 600 of systeemfont van de dienst, labels HRS / MIN / SEC in #C9C6C0 (8,8:1). Geen dagen-veld op de einddag.
   - Plaats: direct onder de kop, op de plek van de deadline-tegels, met de statische regel ("Ends tonight at 11:59 PM ET") er live onder. De GIF vervangt de tekst nooit.
   - Frame 1 (Outlook) toont de juiste tijd bij openen; dat doet de dienst standaard, controleren.
   - Verlopen-beeld instellen: "This deal has ended. Black Friday prices are still on." (op ink), zodat late openers niet 00:00:00 zien en toch kunnen klikken naar de sale.
   - Eindtijd exact gelijk aan de backend (Shopify-code, Rise-vervaldatum). Eerst de backend, dan de timer.
   - Linken naar dezelfde URL als knop 1, `utm_content=countdown`.
   - Onder 150 KB; testen of hij in Gmail iOS, Apple Mail en Outlook web laadt.

### 2.3 Deadline-formuleringen (live tekst, als variabele)

Alle tijden komen uit één variabele zodat Floris ze in één keer vervangt (BRIEF: `{{DEADLINE}}`). In de bron als bouwmacro, niet als Klaviyo-tag, zodat er nooit een lege deadline naar een klant gaat:

| Plek | Patroon | Voorbeeld |
|---|---|---|
| Topbalk | `ENDS {{DEADLINE_CAPS}}` | ENDS TONIGHT 11:59 PM ET |
| Hero-regel | `Ends {{DEADLINE}}.` | Ends tonight at 11:59 PM ET. |
| Tegels (`deadline`-blok) | label, dag, tijd | ENDS · TONIGHT · 11:59 PM ET |
| Knop 3 | `Before {{DEADLINE_SHORT}}` | BEFORE 11:59 PM TONIGHT |
| Alt | `deal ends {{DEADLINE}}` | |

Build-regel: staat `{{DEADLINE}}` nog als placeholder in de bron, dan weigert de export (QA-FOUT). Dit is een kleine uitbreiding van `qa_render.py`, door de bouwrol.

### 2.4 Tijdzones (beslissing nodig van Floris)

De BRIEF schrijft "tonight at 11:59 PM, tijd van de ontvanger". De backend kent echter één absoluut moment: een Shopify-kortingscode eindigt op één tijdstip, een Rise-vervaldatum ook. Klaviyo kan de tijdzone van de ontvanger niet betrouwbaar in de tekst zetten. UX-regel: **de tekst noemt het moment dat de backend afdwingt, met tijdzone.**

- US-verzending: één eindtijd in ET, verzonden in de ochtend ET, tekst "tonight at 11:59 PM ET". Voor de westkust is dat 8:59 PM PT; desgewenst in de hero-regel "(8:59 PM PT)" erachter, niet in de topbalk.
- INT-verzending: eigen verzending, eigen backend-moment, tekst in de tijd van de grootste markt (bv. "tonight at 11:59 PM GMT") of een unieke code per ontvanger met een vaste looptijd ("Your code works for 24 hours from this email"); dat is eerlijk omdat Klaviyo de code bij verzending toewijst en de pool de looptijd afdwingt (zelfde redenering als het `deadline`-blok uit oktober).
- Wil Floris echt "middernacht lokaal" per ontvanger, dan moet de backend dat ook doen (Klaviyo-verzending in lokale tijd plus unieke codes met relatieve looptijd). Anders niet zo formuleren.

---

## 3. Spec per mail

Legenda posities: px vanaf de bovenkant op 375 px. "Bestemming" verwijst naar §4.

### Mail 1 · FLASH: "24-hour flash deal ends tonight"

Doel: één product (Pan Pro Standard $144, of 2 Pans + 2 Lids $249 met MSRP $664) extra scherp voor 24 uur. Eén product = één beslissing, dus de mail is kort.

Eerste scherm (donker vlak):

| # | Blok | px | Inhoud |
|---|---|---|---|
| 1 | Topbalk ink, wit | 0 tot 40 | 24-HOUR FLASH DEAL · ENDS TONIGHT 11:59 PM ET |
| 2 | Header | 40 tot 110 | Lockup |
| 3 | Productbeeld, uitsnede 2:1, op donker | 110 tot 298 | Echte productfoto (packshot op donker of shoot), geen tekst in het beeld; gele sale-tag "-63%" als live `<td>` linksboven, niet in het beeld |
| 4 | Kop (h1, wit op ink) | 310 tot 385 | "2 pans + 2 lids. $249." (of "The Pan Pro. $X today.") |
| 5 | Prijsregel | 385 tot 410 | `{{WAS:duo2}}` doorgestreept #C9C6C0 naast "today only", alleen bevestigd anker (PLAYBOOK §12) |
| 6 | Deadline-regel of countdown-GIF | 415 tot 445 | Regel wit 16 px: "Flash deal ends tonight at 11:59 PM ET." In de GIF-variant: GIF 327 x 76 px (415 tot 491) met de regel eronder, dan schuift alles 70 px op en gaat de prijsregel (5) de kop in |
| 7 | Knop 1, wit met ink | 455 tot 511 | GET MY 2 PANS FOR $249 → |
| 8 | Friction reducer | 515 tot 540 | One use, already applied. 30-day returns. (bij code) |

Knop 1 eindigt zonder GIF op 511, met GIF rond 520 als de prijsregel in de kop opgaat. Past het niet, dan het beeld (3) onder de knop, nooit de deadline.

Rest van de mail (licht vlak):
- Wat zit erin (2 regels plus kleine foto per item, of bestaand `bundle`-blok, max 400 px).
- Drie iconregels (`features`, max 220 px): pure titanium cooking surface, no coatings; 75-year warranty; 30-day returns.
- 2 reviews (`reviews3 n="2"`, set kls-pan of kls-set).
- Knop 2 (ink op licht), friction reducer.
- Gifts-strook `gifts5 style="row"` ("+ 5 free gifts with this order", US "$555 value").
- Knop 3 "BEFORE 11:59 PM TONIGHT →".
- Footer.

Doelhoogte: ~2.500 px. Aantal knoppen: 3. Bestemming: productpagina met code (§4). INT: zelfde opbouw, prijzen via macro, alleen als het product in die markt verkocht wordt (2 Pans + 2 Lids is US-only: INT krijgt Pan Pro Standard).

### Mail 2 · VIP-WEEKEND: "VIP only: extra 10% on top, ends Sunday midnight"

Doel: persoonlijke code, extra 10 procent bovenop de sale, verloopt zondag 23:59. De code moet zichtbaar zijn (bewijs dat het persoonlijk is) maar de lezer hoeft hem niet over te typen.

Eerste scherm (donker vlak):

| # | Blok | px | Inhoud |
|---|---|---|---|
| 1 | Topbalk | 0 tot 40 | VIP ONLY · EXTRA 10% ENDS SUNDAY 11:59 PM ET |
| 2 | Header | 40 tot 110 | |
| 3 | Eyebrow (goud op ink) | 130 tot 150 | VIP BLACK FRIDAY WEEKEND |
| 4 | Kop | 155 tot 245 | "Extra 10% off. On top of up to 70% off." |
| 5 | Codevak | 255 tot 325 | Wit vak met stippelrand, code `{% coupon_code 'VIPWKND' %}` in 24 px, spatiëring 3 px, eronder 12 px "Your personal code · already applied when you tap below". `white-space:nowrap`, valt op 320 px terug naar 20 px (bestaande `.offer-code`-regels) |
| 6 | Deadline-tegels | 335 tot 420 | ENDS · SUN · 11:59 PM ET (bestaand `deadline`-blok, ink-variant) |
| 7 | Knop 1 | 435 tot 491 | USE MY EXTRA 10% → |
| 8 | Friction reducer | 495 tot 520 | One use, already applied. 30-day returns. 100,000+ happy customers. |

Rest:
- "What your 10% looks like": 2 x 2 productkaarten (`productcard`), per kaart sale-prijs met `note="$X with your code"`; nooit de eigen verkoopprijs doorstrepen voor de codeprijs (PLAYBOOK §12). Max 2 rijen. Elke kaart linkt naar dezelfde codelink met eigen redirect naar dat product (uitzondering op "één bestemming": zelfde actie, code blijft gelijk).
- Gifts-strook.
- Knop 2, friction reducer.
- Footer.

Doelhoogte: ~2.700 px. Knoppen: 2 (plus kaarten). Bestemming: sale-collectie met code (§4).

Let op:
- "On top" alleen als de code in Shopify echt combineert met de sale-prijzen (combinaties aan, of sale-prijzen zijn compare-at-prijzen en de code werkt erop). Controleer vóór de copy.
- Gebruik dezelfde `coupon_code`-tag in het codevak en in alle links; Klaviyo wijst per ontvanger per bericht één code toe. Controleer in een Klaviyo-preview dat codevak en link dezelfde code tonen.
- Unieke code en het eerste scherm: de codebalk boven de header (`codebar`) niet ook nog gebruiken; één plek voor de code.

### Mail 3 · CREDIT: "Your $X store credit expires tonight"

Doel: het persoonlijke bedrag is het hele verhaal. Het moet groot, juist en nergens anders verwarrend zijn.

Eerste scherm (licht vlak, persoonlijk):

| # | Blok | px | Inhoud |
|---|---|---|---|
| 1 | Topbalk | 0 tot 40 | YOUR CREDIT EXPIRES TONIGHT 11:59 PM ET |
| 2 | Header | 40 tot 110 | |
| 3 | Aanhef | 130 tot 155 | "Hi {{ first_name\|default:'there' }}," (16 px) |
| 4 | Tegoedkaart | 165 tot 345 | Wit vak, 1 px rand #ECE7DD, radius 8. Klein label "YOUR STORE CREDIT" (brick, 12 px). Bedrag live tekst Inter 800, 56/60 px, ink: "$12". Eronder "= 1,200 points" (14 px, #727272) alleen als het puntenmodel live is. Eronder deadline-regel brick 16 px "Expires tonight at 11:59 PM ET". Hele kaart is een link |
| 5 | Eén zin | 355 tot 405 | "That's $12 off anything in the Black Friday Sale, on top of up to 70% off." (alleen "on top" als het stapelt, zie onder) |
| 6 | Knop 1, ink | 420 tot 476 | USE MY $12 NOW → |
| 7 | Friction reducer | 480 tot 505 | Applied at checkout. 30-day returns. 100,000+ happy customers. |

Rest:
- "How it works", drie korte regels (pick anything, credit at checkout, 5 gifts ship with it), max 200 px.
- 4 producten in 2 x 2, met "Your price with credit" alleen als het bedrag het verschil echt maakt; anders gewone sale-prijzen.
- Knop 2.
- Juridische regel boven de footer, 12 px #727272 op wit: "Promotional store credit, no purchase needed to receive it. Expires {{CREDIT_EXPIRY_LONG}}. Not redeemable for cash." (tekst uit het store-credit-plan).
- Footer.

Doelhoogte: ~2.300 px. Knoppen: 2.

Bedrag en vervaltijd tonen (regels voor de bouwrol):
- Bron: `rise_wallet_balance` en `rise_wallet_next_expiration_date` (Rise-koppeling) of de eigen import `siraat_points` / `siraat_credit_expires` (zie store-credit-plan). Nooit een vast bedrag in de copy.
- **Niet verzenden zonder saldo**: segmentfilter saldo > 0 op het moment van verzenden. In de template als tweede vangnet: `{% if bal > 0 %}...{% else %}` een versie zonder bedrag ("Your Black Friday prices end soon") en zonder "expires". Nooit "$0", nooit een lege plek, nooit `default:12`.
- Opmaak: hele dollars zonder decimalen ("$12"), anders twee ("$12.50"): Django `floatformat:"-2"` (in een Klaviyo-preview bevestigen, PLAYBOOK zet `floatformat:0` alleen als voorbeeld). Duizendtallen met komma.
- Valuta: Rise-tegoed staat in de valuta van de winkel; buiten de US geen "$" tonen (PLAYBOOK v5). INT: bedrag in punten of in lokale valuta alleen als Rise dat per markt levert; anders INT niet in deze mail of zonder bedrag. Beslissing Floris.
- Vervaltijd: alleen "tonight" als de vervaldatum van dat profiel vandaag is. Veiligst: de campagne alleen naar het segment "vervalt vandaag" sturen en de tijd als vaste tekst. Als de datum uit het profiel komt: `{{ person|lookup:'rise_wallet_next_expiration_date'|format_date_string|date:'M j' }}` en dan "Expires Nov 30 at 11:59 PM ET" in plaats van "tonight".
- Geen punten tonen zolang het puntenmodel (100 points = $1) niet live is; dan alleen dollars.
- Subject en preview mogen het bedrag noemen; test in de Klaviyo-preview op een profiel met en zonder saldo.

### Mail 4 · LAST-HOURS resend: brief van Benjamin in platte tekst

Naar openers zonder klik en zonder order (urgentie.md, resendregel R-b). Doel: voelt als een persoonlijk bericht, niet als de vijfde salemail. Eén nieuwe reden, één link.

Opmaakregels:
- **Geen header, geen hero, geen beeld, geen topbalk.** Minimale footer: afmelden, voorkeuren, adres (BRIEF: uitzondering voor platte brieven van Benjamin). Let op: CLAUDE.md noemt deze uitzondering nog alleen voor affiliate- en Mystery Gift-mails; Floris laten bevestigen en in DECISIONS zetten vóór verzending.
- Witte achtergrond over de hele breedte, tekstkolom max 560 px, links uitgelijnd, padding 24 px opzij op mobiel.
- Font: systeemfont-stack (`-apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif`), 17/26 px, ink #272727. Geen Inter-import: een brief van een persoon ziet eruit als de mailapp zelf.
- Afzender "Benjamin from Siraat" (of "Benjamin, Siraat's Kitchen"), antwoordadres een echte, gelezen inbox. Geen "A real person reads every email" (PLAYBOOK §12); wel "Reply and our team will help."
- Lengte: 70 tot 130 woorden. Op 375 px is dat ~700 tot 1.100 px inclusief footer. Ver onder de grens.

Opbouw:

| # | Regel | Positie |
|---|---|---|
| 1 | "Hi {{ first_name\|default:'there' }}," | ~20 px |
| 2 | Eerste zin = de deadline: "Quick one: the {{DEAL}} ends tonight at 11:59 PM ET." | ~60 px |
| 3 | Eén of twee zinnen met de nieuwe reden (gifts, prijs, review) | ~100 tot 200 px |
| 4 | **Link 1 op een eigen regel**, 18 px, 700, brick #AC3B19, onderstreept, met `display:inline-block;padding:12px 0` zodat het tikvlak 44 px hoog is: "→ See the deal before midnight" | ~230 px, ruim in het eerste scherm |
| 5 | Eén zin bezwaar weg ("30 days to send it back.") | |
| 6 | "Benjamin" / "Founder, Siraat's Kitchen" | |
| 7 | P.S. met dezelfde link in de zin: "P.S. Your 5 free gifts ship with it." | |
| 8 | Minimale footer, 12 px #727272 | |

Regels:
- Maximaal 2 links naar hetzelfde doel (regel 4 en P.S.), plus de footerlinks. Geen knop: de brief van 4 nov (wb-us-b-letter) had wel een pilknop en die mag als B-variant in een test, maar de standaard is platte tekst omdat founder-notes 1,3 procent klikken tegen 0,3 tot 0,6 procent voor beeldmails (PLAYBOOK §1).
- Geen vet behalve de deadline-zin (mag), geen kleurvlakken, geen emoji.
- Onderwerp in zinskapitalen, kort, zonder caps of uitroeptekens ("A few hours left", "Before midnight").
- Verzendmoment: minimaal 4 uur vóór het backend-einde, liefst 6 tot 8 uur, zodat "last hours" waar is en er tijd is om te kopen.
- Platte-tekstversie in Klaviyo handmatig nalopen: de link staat als volledige URL op een eigen regel, niet als "[link]".
- Bestemming: dezelfde als de mail waarop hij de resend is.

### Mail 5 · GIFTS: "Your 5 free gifts end tonight"

Doel: de gifts zijn het aanbod. Ze moeten in het eerste scherm te zien zijn, maar het raster van 5 tegels is te hoog (~600 px). Dus een compacte strook boven de vouw, het raster lager.

Eerste scherm (donker vlak):

| # | Blok | px | Inhoud |
|---|---|---|---|
| 1 | Topbalk | 0 tot 40 | YOUR 5 FREE GIFTS END TONIGHT 11:59 PM ET |
| 2 | Header | 40 tot 110 | |
| 3 | Kop (wit op ink) | 130 tot 215 | "5 free gifts. Last day." |
| 4 | Waarde-regel | 215 tot 245 | US: "$555 value, with every order." INT: "With every order." (geen bedrag, DECISIONS 7 nov) |
| 5 | Gifts-strook | 255 tot 355 | 5 kleine echte gift-beelden op één rij (`gifts5 style="row"` aangepast naar 5 x 60 px, of 4 + filter met "Chance to win"-label), labels 11 px wit eronder. Hele strook is een link |
| 6 | Deadline-regel of GIF | 365 tot 425 | "Gifts end tonight at 11:59 PM ET." Op de echte laatste dag eventueel de countdown-GIF |
| 7 | Knop 1, wit met ink | 440 tot 496 | CLAIM MY 5 GIFTS → |
| 8 | Friction reducer | 500 tot 525 | Added automatically. Free shipping. 30-day returns. (alleen "added automatically" als dat zo is, zie onder) |

Rest:
- Gifts-raster (`gifts5`) met per gift één regel uitleg, max 650 px. Filter altijd "Chance to win a PFAS water filter", nooit gratis of "purifier".
- "Pick anything" met 2 x 2 bestsellers (licht vlak).
- Knop 2, knop 3 met de deadline.
- Footer.

Doelhoogte: ~3.000 px. Knoppen: 3.

Let op: DECISIONS zegt "gifts eindigen als BF eindigt". "Your 5 free gifts end tonight" is dus alleen waar op de laatste dag van de sale (30 nov), tenzij Floris een eerdere gifts-deadline in de backend zet. Ook nagaan hoe de gifts in de bestelling komen (automatisch toegevoegd door een app of zelf toevoegen); daar hangt de friction reducer en de bestemming van af.

### Mail 6 · DRAW: "Order by Sunday midnight to enter this week's filter draw"

Doel: een wekelijkse trekking als deadline. Juridisch de gevoeligste mail: in de VS hoort bij een trekking "No purchase necessary" en officiële regels met een gratis manier van meedoen (urgentie.md, actiepunt 4). Pas verzenden als die regels online staan.

Eerste scherm (licht vlak):

| # | Blok | px | Inhoud |
|---|---|---|---|
| 1 | Topbalk | 0 tot 40 | THIS WEEK'S FILTER DRAW CLOSES SUNDAY 11:59 PM ET |
| 2 | Header | 40 tot 110 | |
| 3 | Beeld filter, uitsnede 2:1 | 110 tot 298 | Echte productfoto van de PFAS water filter (`gift-filter`), geen AI, geen tekst in het beeld |
| 4 | Kop (h1, ink) | 310 tot 390 | "Order by Sunday. You're in this week's draw." |
| 5 | Deadline-tegels | 400 tot 470 | DRAW CLOSES · SUN · 11:59 PM ET |
| 6 | Knop 1, ink | 480 tot 536 | ORDER AND ENTER THE DRAW → |
| 7 | Juridische regel | 540 tot 575 | 12/17 px #727272: "No purchase necessary. Open to US residents 18+. Official rules." met "Official rules" als aparte, onderstreepte link (eigen tikvlak, 8 px ruimte tot de knop) |

Hier mag de juridische regel net onder de vouw vallen, maar niet verder dan 600 px: hij hoort bij de deadline. Knop 1 eindigt op 536; om op 520 te komen het beeld naar 16:7 (164 px).

Rest:
- "How it works" in drie regels: every order this week is an entry; winner drawn Monday and emailed; or enter free (link naar de regels).
- Prijswaarde: US "a $450 PFAS water filter" (`{{GIFTS:filterline}}`), INT zonder bedrag of uitgesloten als de regels alleen US toestaan.
- Bestsellers 2 x 2.
- Gifts-strook ("plus 5 free gifts with every order").
- Knop 2.
- Footer.

Doelhoogte: ~2.600 px. Knoppen: 2. Bestemming: sale-collectie.

---

## 4. Bestemming per mail

Regel: de klik moet landen op een pagina waar de lezer het aanbod uit de mail meteen terugziet, met de korting al toegepast waar dat kan. Nooit landen op een pagina met een andere (of nep-)timer.

| Mail | Bestemming | URL-patroon | Waarom |
|---|---|---|---|
| 1 FLASH (met code) | Productpagina, korting toegepast | `https://siraatskitchen.com/discount/FLASHCODE?redirect=/products/2-pans-and-2-lids%3Futm_source%3Dklaviyo%26utm_medium%3Demail%26utm_campaign%3Dflash-1108%26utm_content%3Dcta1` | Eén product: geen tussenstap. Code wordt in de sessie gezet en staat in de kassa |
| 1 FLASH (prijs in Shopify, geen code) | Productpagina | `https://siraatskitchen.com/products/2-pans-and-2-lids?utm_...` | |
| 2 VIP-WEEKEND | Sale-collectie, code toegepast | `https://siraatskitchen.com/discount/{% coupon_code 'VIPWKND' %}?redirect=/collections/black-friday-sale%3Futm_...` | Extra 10% geldt op alles; de lezer kiest zelf |
| 3 CREDIT | Sale-collectie | `https://siraatskitchen.com/collections/black-friday-sale?utm_...` | Rise-tegoed is een gift card, geen kortingscode: de `/discount/`-link werkt er niet voor. Of Rise het tegoed zelf in de kassa toepast (wallet herkend op e-mail) moet getest worden; zo niet, dan de walletcode in het tegoedvak met "Enter at checkout" |
| 4 LAST-HOURS | Zelfde als de oorspronkelijke mail | | Continuïteit: hetzelfde aanbod |
| 5 GIFTS | Sale-collectie | `/collections/black-friday-sale?utm_...` | Gifts gelden op elke order. Als gifts handmatig moeten worden toegevoegd: liever naar een pagina die dat uitlegt of de cart met gifts (`/cart/add?id=...` alleen als Floris bevestigt dat de gift-varianten zo werken) |
| 6 DRAW | Sale-collectie | `/collections/black-friday-sale?utm_...` | Elke order telt mee. Regels-link naar de officiële regelspagina |

Technische regels voor links:
- `/discount/CODE?redirect=` alleen met een echte Shopify-kortingscode. De `redirect` is een pad op de eigen site; UTM-parameters erachter URL-gecodeerd (`%3F`, `%26`), zoals de `xsell`-macro dat al doet. Echte BF-codes nooit in de repo: placeholders FLASHCODE, BFCODE, VIPWKND.
- Product met maten (Pan Pro Standard): deep link naar de juiste variant met `?variant=<id>` binnen de redirect, anders kiest de pagina de eerste maat (Mini).
- **PDP-timer**: research/cro/01-funnel.md vond op de productpagina een countdown die per bezoeker op 02:42 begint ("PRIME SALE ends in 02 HRS 42 MIN"). Als die nog live staat en de mail zegt "ends tonight at 11:59 PM ET", ziet de lezer twee verschillende deadlines en gelooft geen van beide. Vóór mail 1 controleren en die timer uitzetten, of mail 1 naar de collectie laten landen.
- Na de deadline: de code werkt niet meer. De collectie blijft werken; een productpagina ook, maar dan zonder flashprijs. Geen aparte "verlopen"-pagina nodig, wel het verlopen-beeld in de GIF (§2.2).
- Klaviyo-klikmeting staat aan; geen eigen link-shorteners.

---

## 5. Meten

- Per vlak `utm_content` (§1.4). Na elke verzending: aandeel kliks uit het eerste scherm (topbar, hero-*, cta1, countdown) tegen de rest. Verwachting bij deze opbouw: meer dan de helft van de kliks boven 560 px.
- Doel per mail: klik boven 1,5 procent (nu 0,24 tot 1,13), omzet per ontvanger boven $0,17 (de deadline-mails van okt/nov).
- Tests, één variabele per test (PLAYBOOK §6), winnaar op unieke kliks en omzet per ontvanger, nooit op opens:
  1. FLASH: met of zonder countdown-GIF.
  2. LAST-HOURS: platte tekstlink tegen één pilknop.
  3. VIP: codevak boven de knop tegen codevak eronder.
- Bewaking: afmelden boven 1,5 procent of spam boven 0,15 procent vanaf 1.000 ontvangers = stoppen (vangrail urgentie.md, 0,3 procent spam voor de hele reeks).

---

## 6. QA-lijst voor de designer (per mail, vóór oplevering)

- [ ] Op 375 px: deadline, aanbod met getal en knop 1 eindigen boven 560 px (knop 1 uiterlijk op 520 px).
- [ ] Topbalk, eyebrow, kop, deadline, beeld en knoppen linken allemaal naar dezelfde URL met eigen `utm_content`.
- [ ] Knoppen ink met wit (licht) of wit met ink (donker), 56 px hoog, volle breedte, VML voor Outlook. Geen gele knop of balk.
- [ ] Geel alleen op sale-tags met ink tekst.
- [ ] Deadline staat 3 keer als live tekst (topbalk, hero, laatste knop of eronder), uit één variabele, met tijdzone.
- [ ] Geen `{{DEADLINE}}`, `FLASHCODE`, `BFCODE` of lege Klaviyo-variabele meer in de export; geen "$0" in CREDIT.
- [ ] Hoogte inclusief footer onder 3.600 px (doelen per mail in §3), HTML onder 80 KB, beelden onder 800 KB.
- [ ] Contrast volgens §1.6; geen #9A948B of goud als tekst op licht.
- [ ] Dark mode gecontroleerd in Gmail iOS (lockup, knoppen, gift-tegels).
- [ ] Alt-teksten noemen aanbod en deadline; kop als `<h1>`.
- [ ] Vaste header en footer (behalve mail 4: minimale footer, na bevestiging Floris).
- [ ] Merkregels: Benjamin, 30-day returns, 75-year warranty, 100,000+ customers, "5 free gifts", "chance to win a PFAS water filter", geen verboden woorden uit de BRIEF, geen gedachtestreepjes.
- [ ] `qa_render.py` groen; previews 375 en 600 in `klaviyo/templates/v3/campaigns/urgency-1108/` en als rij in Figma (DECISIONS 4 nov).

---

## 7. Open vragen voor Floris

1. Mag er een live countdown-GIF in FLASH en GIFTS (als A/B), en met welke dienst (voorstel Sendtric betaald, of NiftyImages als er persoonlijke vervaltijden komen)?
2. Tijdzone van de deadlines: één moment in ET voor de US-verzending, en wat voor INT (§2.4)?
3. Stapelt de VIP-code in Shopify echt bovenop de sale-prijzen, en stapelt het Rise-tegoed met BFCODE?
4. Past Rise het tegoed automatisch toe in de kassa, of moet de klant een walletcode invullen?
5. Staat de PDP-timer (02:42 per bezoeker) nog aan? Zo ja: uit vóór de flash-mail.
6. Hoe komen de 5 gifts in de bestelling (automatisch of zelf toevoegen)?
7. Officiële regels en gratis deelname voor de filtertrekking: wanneer online, en alleen US?
8. Benjamin-brief zonder header (mail 4): uitzondering bevestigen en in DECISIONS zetten.
9. Lockup in Gmail dark mode: als het zwarte logo wegvalt, mag er een variant met lichte rand of plaat komen?
