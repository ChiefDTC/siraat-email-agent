# 06 · Offer design voor de flows (Hormozi value equation)

Datum: 7 oktober 2026. Bron: `research/copy/offers-skill.md` (value equation, value stack, garanties, urgentie, prijspresentatie, checklist), plus `content/facts/products.csv`, `site-pages-and-policies.md` (refund policy), `facts.csv`, DECISIONS, `research/ux-2026-10-07/04-offer-strategy.md`.
Door Floris bevestigd (7 okt, via coördinator): Pan Pro Standard 11" $134 met compare-at $439; 6-delige set $349; de 4 gifts gelden bij elke order.
Grenzen: geen nieuwe beloftes, alleen wat het beleid zegt; de PFAS water filter is een kans, nooit opgeteld bij gegarandeerde waarde.

---

## 1. De value equation, toegepast

Offer value = (dream outcome x perceived likelihood) / (time delay x effort and sacrifice)

| Factor | Wat wij hebben (echt) | Hoe sterk het nu in de mails staat | Score 1 tot 5 |
| --- | --- | --- | --- |
| Dream outcome | Koken zonder coating; eieren die glijden; één pan die niet na een paar jaar weg moet (75 jaar garantie); niet meer twijfelen wat er van je pan in je eten komt; "I can't wait to finish work, and go home to cook" (R563). | Zwak uitgedrukt: de hero-koppen gaan over 10 procent, niet over het resultaat. Alleen W0, P2 en B1 tonen het resultaat (het ei, de spatel). | 2 |
| Perceived likelihood | Light Labs rapport 25895 (31 PFAS onder detectiegrens, ISO/IEC 17025), 100,000+ happy customers, 384 vijfsterrenreviews in 180 dagen, 30-day returns, 75-year warranty, de chef-gids. | Sterk in W3 en C2, elders als icoontje. Reviews zijn generiek. Maar: 81 van 154 lage reviews gaan over plakken; wie de techniek niet kent, gelooft het resultaat niet of haalt het niet. | 3 |
| Time delay | Free shipping, verzending binnen 1 werkdag (voorraad), e-book direct, chef-gids direct, levering 6 tot 10 dagen (US). | Zwakste punt van het product: 48 van 154 lage reviews noemen levering of tracking. In marketingmails noemen we bewust geen levertijden (PLAYBOOK 11). Wat we wel kunnen inkorten: de tijd tot het eerste succes (gids vóór de pan aankomt, W0, P1). | 2 |
| Effort and sacrifice | Vaatwasserbestendig, metalen spatels mogen, geen seasoning, één pan voor alles, werkt op elke kookplaat. Wel: voorverwarmen en een beetje olie is nodig ("It takes a bit of getting used to", R040). | Goed in K1 en P2. Maar de leercurve wordt vóór de aankoop zelden eerlijk genoemd, waardoor de moeite na de aankoop als verrassing komt (retouren, 1-sterrenreviews). | 3 |

Waar het offer het zwakst is:
1. **Dream outcome wordt niet verkocht.** Het aanbod (10 procent) verdringt het resultaat. Oplossing: hero-kop = resultaat of bewijs, aanbod in de balk (04-rewrites).
2. **Time delay.** We kunnen de levertijd niet korter maken in copy, wel de tijd tot het eerste resultaat: "Your cook guide arrives today. The pan follows." (P1, W0) en het e-book direct downloadbaar (P1-knop moet echt naar de download, nu /pages/faq).
3. **Perceived likelihood bij de techniek.** De eerlijke beperking vóór de aankoop ("medium heat, a little oil, and the egg slides; skip the heat and it sticks") verhoogt de ervaren kans van slagen en verlaagt teleurstelling. In W2, B1 en C1 opnemen.

---

## 2. Het standaard value stack-blok

Nieuw blok `{{BLOCK:stack}}` (voorstel voor de bouw, zelfde stijl als het offerblok). Tabel met item, waarde, status, en onderaan "Value" tegen "Your price". Alleen prijzen uit products.csv en DECISIONS.

### 2.1 Pan Pro Standard 11" (US, met HI10)

| What you get | Value | |
| --- | --- | --- |
| Titanium Hammered Pan Pro, Standard 11" (28 cm) | $439 | $134 today |
| Free shipping | $15 | Included |
| Plastic-Free Home e-book | $30 | Included |
| Mystery gift in the box | $25 | Included |
| 75-year warranty against defects | | Included |
| 30-day returns on unused products | | Included |
| HI10: extra 10% off | | -$13.40 |
| **Value** | **$509** | |
| **Your price** | | **$120.60** |
| Plus: a chance to win a PFAS water filter ($450 value) with your order | | Chance to win |

Regels:
- $509 = $439 + $15 + $30 + $25. De filter staat onder de streep als "Chance to win" en telt niet mee (DECISIONS: "win", nooit "free").
- Compare-at $439 bestaat alleen voor de Standard 11". Mini ($129), Small ($127) en Large ($139) hebben geen compare-at in Shopify: daar geen doorgestreepte prijs, alleen prijs en prijs na code.
- Met een unieke code (C4, K3, B2-clicked, R2) is de regel `Your code: extra 10% off` en het bedrag hetzelfde. R2-VIP: 15% = -$20.10, prijs $113.90.
- INT: geen dollarbedragen (W4-INT-besluit). Daar het blok zonder kolom "Value": alleen "Included"-regels plus "Duties paid".

### 2.2 6-delige set ($349, bevestigd)

| What you get | Value | |
| --- | --- | --- |
| 3 Titanium Hammered Pans + 3 stainless steel lids | | $349 today |
| Free shipping | $15 | Included |
| Plastic-Free Home e-book | $30 | Included |
| Mystery gift in the box | $25 | Included |
| One 75-year warranty for all six pieces | | Included |
| 30-day returns on unused products | | Included |
| HI10: extra 10% off | | -$34.90 |
| **Your price** | | **$314.10** |
| **About per pan, lid included** | | **$104.70** |
| Plus: a chance to win a PFAS water filter ($450 value) | | Chance to win |

Geen compare-at voor de $349-set: de zichtbare $399-versie heeft compare-at $1,384, de $349-versie heeft er geen in Shopify. [VRAAG FLORIS: welke compare-at hoort bij de $349-set, of geen.] Daarom hier geen "Value"-totaal maar een prijs-per-pan-anker.

### 2.3 12-delige set (US, $599, compare-at $1,186)
Zelfde opbouw. Value $1,186 + $70 = $1,256, your price met HI10 $539.10.

### 2.4 Waar het blok komt

| Mail | Stack | Waarom |
| --- | --- | --- |
| W1-A / W1-B | 2.1, direct onder het aanbodblok | Eerste kennismaking met het offer; laat zien dat de gifts echt zijn. |
| W4-US | 2.1, 2.2 en 2.3 als drie tiers (zie §5) | Keuzemail. |
| W5 | 2.1 | Laatste herinnering, waarde > prijs zichtbaar. |
| C3-P | 2.2 | Upsell-rekensom. |
| C3-S | 2.2 of 2.3 afhankelijk van de cart (of een algemeen "with your set"-stack zonder prijs) | Setkoper twijfelt over de grootte van de uitgave. |
| C4-US | 2.1 met unieke code, dynamisch alleen als de cart een Standard 11" is; anders zonder Value-regel | Laatste mail. |
| K3 | idem C4 | Laatste mail. |
| B2-clicked | 2.1 met unieke code (dynamisch product: alleen Value-regel bij de Standard) | Warmste browse-lezer. |
| R2 / R2-VIP | Korte versie: gifts + garantie + code, geen pan-anker (klant kent de pan) | Herhaalaankoop. |
| Niet in | W0, W2, W3, C1, C2, K1, P1, P2 | Bewijs-, gids- of herinneringsmails: een prijstabel breekt de slide. C1 heeft het cartblok al. |

---

## 3. Garantie en risk reversal: sterker, en precies zoals het beleid zegt

Wat het beleid zegt (refund policy, `site-pages-and-policies.md`, en facts.csv):
- Ongebruikt (niet gekookt, niet gewassen, niet ingevet), originele verpakking, binnen 30 dagen na levering: volledige refund.
- Retourzending van ongebruikte producten: voor de klant.
- Beschadigd of defect binnen 30 dagen: klant kiest refund of gratis vervanging, Siraat betaalt alle verzending. Een paar foto's volstaat.
- Daarna: 75-Year Warranty tegen defecten (deuk, kromgetrokken bodem, loszittend of gebroken handvat, gebroken klinknagels, deksel dat niet meer past), "for as long as you own it".
- Niet gedekt: plakken, kookresultaat, verkleuring, normale slijtage.
- Support antwoordt volgens het beleid "within 1 hour on business days". [VRAAG FLORIS: mag dat in marketingmail? Het is een harde belofte.]

Zwak nu: "30-day returns" en "75-year warranty" als twee icoontjes. Geen uitleg, geen bewijs, "No risk on your side" (K3) is te sterk.

Sterkere formulering (twee beloftes, gewone woorden, specifiek):
> **Two promises.**
> **Changed your mind?** Send it back unused within 30 days of delivery for a full refund.
> **Something wrong with it?** If it arrives damaged or with a defect, you choose: a refund or a new one, and we pay the shipping. After 30 days, the 75-year warranty covers dents, a warped base, a loose handle or rivet, and a lid that no longer fits. A few photos is all it takes.

Korte versie (friction reducer): `30-day returns on unused pans. 75-year warranty. 100,000+ happy customers.`

Eerlijke beperking als vertrouwensbouwer (Sugarman: honesty; skill: "honest limitations"):
> One honest note: sticking is not a defect. A pan with no coating releases with heat and timing. Our chef's 5 steps show you how, and they come with your order.

Bewijs naast de garantie (match proof aan de claim): R240 Brandon W. ("I just sent them the picture and they honored the warranty."), R273 Steven T. ("I returned my pans, unused, and received a refund, no questions asked.").

Nooit: "risk-free", "money-back guarantee", "100-day trial", "lifetime", "free returns", "no questions asked" als eigen belofte (wel als citaat van Steven T.).

Waar: volledige versie in K3 en C4 (laatste mails), korte versie onder elke knop in verkoopmails, eerlijke beperking in W2, B1 en P1.

---

## 4. Urgentie: alleen wat echt is

| Mechaniek | Status | Copy | Waar |
| --- | --- | --- | --- |
| Unieke code, 48 uur na de mail (C4_10_48H, K3_10_48H, B2_10_48H) | Echt | "Your personal code works for 48 hours after this email. It is one code, made for you, so it has an end date. After that, the regular sale price applies." | C4, K3, B2-clicked |
| Unieke code, 72 uur (R2_10_72H, R2_VIP_15_72H) | Echt | idem met 72 uur | R2, R2-VIP |
| Unieke bedankcode, 14 dagen (P3_THANKYOU_10_14D) | Echt | "Your thank-you code works for 14 days after this email." | P3-pan, P3-set, P3-accessory |
| Eén code per order, eenmalig per persoon | Echt (Shopify-regel) | "One code per order." | Onder elke code |
| HI10 | Publiek, geen einddatum | Nooit met deadline. "HI10 still works." | Welcome, browse, cart, R1 |
| Wekelijkse PFAS-filtertrekking | Niet bevestigd (geen actievoorwaarden gevonden) | Niet als deadline gebruiken tot Floris de voorwaarden levert. | Nergens als urgentie |
| Einde reeks | Echt | "This is the last email about your cart." / "The last time we mention it in this series." | C4, K3, W5 |
| Sale-einde oktober, BFCM | Onbekend (DECISIONS) | Geen datum tot Floris die geeft. | Nergens |

Reden noemen (scarcity-framework): elke deadline krijgt één zin waarom ("made for you, so it has an end date") en één zin wat er daarna gebeurt ("the regular sale price applies"). Geen countdown-GIF zonder echte einddatum.

---

## 5. Prijspresentatie

1. **Anker eerst, dan prijs, dan prijs na code, in dollars**: `$439  $134  $120.60 with HI10`. Alleen bij de Standard 11" (enige met compare-at). Besparing in dollars en procent mag: "You save $318.40 (72%)" (1 - 120.60/439 = 72,5 procent, naar beneden afgerond). Veiliger: alleen dollars.
2. **Per jaar garantie**: "$134, covered for 75 years: about $1.79 a year." Alleen als "covered", nooit als gegarandeerde levensduur. Beter nog de eerlijke som uit 01 §1.4 (15 coated pans in 75 years).
3. **Per pan bij sets**: "$349 for three pans and three lids: about $116 a pan, lid included" (zonder code) of "$104.70 with HI10".
4. **Tiers in W4-US** (2 tot 3, niet meer; offers-skill):

| | The Pan Pro | The 6-piece set | The 12-piece set |
| --- | --- | --- | --- |
| For | 1 or 2 people | A busy stovetop | The whole kitchen (US only) |
| What | 1 pan, 4 sizes | 3 pans + 3 lids | 3 pans, 3 pots, 6 lids |
| Price | from $127 | $349 | $599 (was $1,186) |
| With HI10 | from $114.30 | $314.10 | $539.10 |
| Per pan | | about $105 with HI10 | |
| Gifts | 4 gifts | 4 gifts | 4 gifts |
| Warranty | 75 years | 75 years | 75 years |

Middelste tier visueel benadrukken ("Most cooks for two or more pick this", alleen als Floris bevestigt dat de 6-set de populairste set is; anders label "Best value per pan", wat rekenkundig klopt tegenover losse pannen met deksel).
W4-INT: zelfde tiers zonder prijzen en zonder 12-delige set (bestaand besluit).
5. **Geen betaalplannen noemen**: niet gevonden in facts. [VRAAG FLORIS: Shop Pay Installments of Klarna actief? Dan "or 4 payments of $30.15" bij de Pan Pro.]

---

## 6. Offer-checklist per flow

Scores 1 tot 5 op de vier checklistgroepen van de offers-skill. Huidige v3 → na de voorstellen in 04 en dit document.

| Flow | Waarde (droomresultaat, stack) | Risico (garantie, proof) | Urgentie (echt, helder) | Prijs (anker, investering) | Nu | Na |
| --- | --- | --- | --- | --- | --- | --- |
| Checkout | 2 → 4 | 3 → 4 | 4 → 4 | 3 → 4 | 3,0 | 4,0 |
| Cart | 2 → 4 | 3 → 5 | 4 → 4 | 3 → 4 | 3,0 | 4,3 |
| Browse | 2 → 3 | 2 → 4 | 3 → 4 | 2 → 3 | 2,3 | 3,5 |
| Welcome | 2 → 4 | 3 → 4 | 2 → 2 (bij besluit B: 4) | 3 → 4 | 2,5 | 3,5 |
| Post-purchase | 3 → 4 | 3 → 4 | 4 → 4 | 3 → 3 | 3,3 | 3,8 |
| Winback | 2 → 3 | 2 → 3 | 4 → 4 | 2 → 3 | 2,5 | 3,3 |

### Checkout · 3 verbeteringen met de meeste omzetimpact
1. C4: volledige risk reversal ("Two promises") plus value stack met de persoonlijke code. Laatste mail, hoogste RPR-flow ($2,36 per ontvanger, baselines).
2. C3-P: value stack 2.2 met "$104.70 per pan with HI10" en Sunny C. als bewijs. Verhoogt AOV; $349 is nu bevestigd.
3. C1: value stack niet, wel één review direct onder de cart en de friction reducer onder de knop. C1 is al de beste mail van het account; alleen frictie weghalen.

### Cart · 3 verbeteringen
1. K2-new: eerlijke pijnsom (15 pans or one) met de stack 2.1 eronder. Prijs-twijfel is het grootste pre-sale bezwaar (22 van 58 prijstickets pre-sale).
2. K3: "What protects you" met de twee beloftes en R240/R273; "No risk on your side" eruit.
3. K2-returning: HI10 niet meer als "thank-you" framen (onwaar), wel "same 4 gifts, same warranty".

### Browse · 3 verbeteringen
1. B2-clicked: reden voor de code + wat daarna + stack met code. Nu alleen scarcity.
2. B1: dream outcome in de kop ("Nothing on it to scratch off") in plaats van 10 procent; eerlijke beperking blijft.
3. B2-notclicked: twee zwakke kaarten vervangen door de verhalen van James en Sunny (perceived likelihood).

### Welcome · 3 verbeteringen
1. W1: stack 2.1 direct onder het aanbodblok, gifts-eyebrow naar "WITH EVERY ORDER" (bevestigd). Hoogste volume (16.805 ontvangers per week).
2. W4-US: tier-tabel met prijs na HI10 en prijs per pan; maatkeuze als commitment-stap.
3. Besluit B (unieke 10-dagen-code) beslissen: zonder echte deadline heeft W5 geen urgentie. Tot dan W5 eerlijk "last email in this series" laten zeggen.

### Post-purchase · 3 verbeteringen
1. P1: e-book-knop naar de echte download (tijd tot resultaat) en de chef-tip; spijt voorkomen houdt retouren laag.
2. P3: per product de prijs na bedankcode in dollars (staat er al) plus één review die bij het product hoort (deksel-review ontbreekt nog).
3. P2: niets verkopen behalve het eerste succes; deksel-upsell onderaan.

### Winback · 3 verbeteringen
1. R2-VIP: reden voor 15 procent ("you have ordered more than once"), Tammy als bewijs, korte stack.
2. R1: "new" alleen waar het waar is; social proof van wat andere eigenaren erbij kochten.
3. R2: reden voor de code ("if one pan is always busy") plus wat er na 72 uur gebeurt.

---

## 7. Open voor Floris
1. Compare-at voor de $349-set (of geen).
2. Mag "Our team responds within 1 hour on business days" (uit het beleid) in mails?
3. Betaalplannen actief (Shop Pay Installments, Klarna)?
4. Is de 6-delige set de meest gekochte set? (voor een "most picked"-label in W4)
5. Actievoorwaarden wekelijkse filtertrekking.
6. Besluit B: unieke welkomstcode met 10 dagen looptijd.
