# Affiliate-mails v2 (Social Snowball), concept 21 okt 2026

Status: **concept, niets in Klaviyo aangemaakt, gewijzigd of verstuurd.** v2 vervangt de v1-copy hieronder (v1 blijft als achtergrond staan). Aanleiding: Floris, "too much text" en "someone who ordered $200 should see they can earn that back". Aanbod volgens DECISIONS 21 okt (15/15).

## Wat er veranderd is

- **Platte brief is de versie om te gebruiken** (Floris, 21 okt): `aff-announce`, `aff-welcome-kit`, `aff-nudge-1`, `aff-sale`, `aff-payout` zijn brieven van Benjamin op wit, zonder header en logo: één beeld, korte tekst, één knop met de referral-link, "Benjamin, founder of Siraat", kleine lettertjes (FTC en voorwaarden) en een minimale wettelijke footer (afmelden en voorkeuren in #111111, `{{ organization.name }} · {{ organization.full_address }}`). Dit is een uitzondering op de vaste header/footer-regel; Floris legt die zelf vast in DECISIONS.md en CLAUDE.md.
- De branded v2 (vaste header, footer, hero met kop) staat in `archive/v2-branded/` (bron, .klaviyo.html, US-screenshots 375 px), alleen ter vergelijking.
- **Het blok `aff-block` blijft branded**: het staat binnen bestaande branded mails. Wel v2-copy en de rekensom; markt = verzendland van de order (`MARKET-SIGNAL: order`).
- `aff-nudge-2` vervalt: `archive/` (bron, Klaviyo-versie, preview, screenshots). `aff-nudge-1` is nu de laatste activatiemail en gaat **alleen naar wie de welcome-kit opende of erop klikte** (flowfilter), en alleen bij 0 keer New referral sale (Xqbr4d) sinds flowstart.
- Geen codevak meer (SafeLinks: alleen de link delen). De link staat als knop plus "Or copy it:".
- **Afzender**: from-label "Benjamin from Siraat", **geen reply-to naar support**. Daarom ook geen "Reply and our team will help" meer in de copy.
- UTM: `utm_campaign=aff-v2` alleen op de dashboardlink (de referral-link blijft schoon).

## Aanbod en rekensom ("Your order can pay for itself")

- Vriend 15% op de eerste order; jij 15% van wat de vriend betaalt; uitbetaling in USD via Tremendous (PayPal, bank, Visa of gift card) na de retourtermijn. Het plafond van $50 per order staat alleen in de kleine lettertjes.
- Percentages uit de profielvariabelen met default `'15%'` (`Referral Reward - SocialSnowball`, `Referral Friend Offer - SocialSnowball`). **De rekensom verschijnt alleen als beide 15% zijn**; staat het profiel nog op 20%/10% (nu zo in Snowball), dan toont de mail alleen "Every friend who orders with your link: 20% of what they pay, for you." Zo klopt de som nooit met een ander percentage.
- Persoonlijk (profiel `Siraat Last Order Value` + `Siraat Last Order Currency`, numeriek, in de valuta van de klant): verdienste per vriend = waarde x 0,85 x 0,15 = waarde x 0,1275 (`ov|multiply:0.1275|floatformat:0`, "about"). Aantal vrienden = ceil(1 / 0,1275) = **altijd 8** zolang het plafond niet raakt (8 x 12,75% = 102% van de order). Boven $392.16 (USD): "$50, the most per order" en `ov|divide:50|ceil` vrienden. Andere valuta ($, £, €, C$, A$, NZ$, S$) alleen onder een veilige grens (GBP 290, EUR 330, CAD 530, AUD 590, NZD 650, SGD 490; ca. $50 omgerekend, okt 2026), daarboven het marktvoorbeeld. Onbekende valuta of een tekst-waarde: marktvoorbeeld.
- Zonder orderwaarde: Pan Pro Duo per markt via `{{PRICE:panproduo}}`, `*0.85`, `*0.1275`, `*1.02` (profielland, `person.Country`). Onbekende markt: alleen de percentageregel.
- Formulering als rekensom, nooit als belofte: "A friend who orders the same pays 15% less, and you get about $27. 8 friends: your whole order back."
- **Uitgewerkt, US (order $214)**: vriend betaalt $181.90, jij $27.29 (mail: "about $27"); 8 x $27.29 = $218.28, dus de hele $214 terug (7 vrienden = $191, niet genoeg).
- **Uitgewerkt, UK (geen orderwaarde)**: Pan Pro Duo £177 (catalogus), vriend betaalt £150.45, jij £22.57; 8 vrienden = £180.54, een hele Duo terug.
- Getest: plafond (US $599: "$50 ... 12 friends"), GBP £160 ("about £20", 8 vrienden), profiel 20/10 (alleen percentageregel), orderwaarde als tekst (marktvoorbeeld).
- [CONTROLEREN in een Klaviyo-preview op een echt profiel] de filters `multiply`, `divide`, `ceil` (staan in de Klaviyo-lijst van qa_render; in de Django-test nagebootst in `research/tailoring/test/kltags.py`) en dat `Siraat Last Order Value` als getal op het profiel staat.
- **Let op prijzen**: `content/catalog/products.json` (8 okt) wijkt af van de site (21 okt) voor de Pan Pro Duo: US $249 klopt, maar UK £172 (catalogus £177), EU €209 (199), CA C$329 (314), AU A$327 (337), NZ NZ$410 (416), SG S$297 (298). Catalogus verversen en de mails opnieuw bouwen vóór livegang. De briefing noemde $229 (oud, `content/facts/products.csv`).

## Mails v2

| Bestand | Plaats | Onderwerp A / B (5 types in de topcomment) | Preview |
| --- | --- | --- | --- |
| `aff-announce` | Eenmalige campagne aan de ~420 auto-ingeschreven kopers (zie v1) | A: Your order can pay for itself · B: Give 15%, get 15% | Friends get 15% off their first order. You get 15% of what they pay. |
| `aff-welcome-kit` | Flow mail 1 na bezorging; 3 korte deelteksten (sms, Instagram met #ad, e-mailregel), elk met disclosure | A: Ready to paste: give 15%, get 15% · B: 3 texts that can pay for your pan | Your order can pay for itself. Three texts, ready to paste. |
| `aff-nudge-1` | Welcome-kit + 7 dagen, alleen openers/klikkers van de welcome-kit, 0 sales | A: Has anyone asked about your pan? · B: Your order can pay for itself | That is the moment your link pays. Give 15%, get 15%. |
| `aff-sale` | New referral sale (Xqbr4d), 15 min, max 1 per 3 dagen | A: A friend just ordered with your link · B: Thank you for passing it on | Here is your commission, and how your order can pay for itself. |
| `aff-payout` | Payout sent (WManrA), direct, max 1 per 14 dagen | A: Your payout is on its way · B: Paid: your 15% from friends | Look for an email from Tremendous to choose PayPal, bank, Visa or a gift card. |
| `aff-block` | Blok in VQ93sx, X3ySuU, bedankmail na review (branded) | n.v.t. | n.v.t. |

Lengte body copy (platte brief, US-render, zonder aanhef-beeld, knop, ondertekening en kleine lettertjes): announce 75, welcome-kit 70 (plus 3 deelteksten), nudge-1 62, sale 58, payout 66 woorden. v1 had 170 tot 430 woorden boven de footer.

## Bouwen, previews, QA

- Generator en bouwscript in de scratchpad van de sessie (`gen_aff_v2.py`, `build_v2.sh`); bronnen met `{{IMG}}`, `.klaviyo.html` met CDN-beelden (assets/klaviyo-urls.txt, v2-beelden).
- Drie testprofielen: US met Siraat Last Order Value 214 (USD), UK zonder orderwaarde, onbekend land; alle 15%/15%. Previews `*-preview.html` (US), `*-preview-uk.html`, `*-preview-unknown.html`; screenshots `previews/<mail>-<us|uk|unknown>-<mobile-375|desktop-600>.png`.
- Gecontroleerd: geen em dash, geen `{{`/`{%` in gerenderde previews, geen horizontale scroll op 375 en 600, alle beelden laden, `scripts/check_previews.py affiliate` 0 problemen.
- Figma: rij node 85-2 in oaxnBkz3MAbePRnorCrQwz bijgewerkt met de 375 px US-screenshots (platte brieven + blok), nudge 2 eruit.

---

# Affiliate-mails v1 (Social Snowball), concept 21 okt 2026

Status: **concept, niets in Klaviyo aangemaakt of gewijzigd.** De 6 Snowball-standaardflows blijven Draft (DECISIONS 21 okt). Bronnen, Klaviyo-versies en previews in `klaviyo/templates/v3/affiliate/`. Achtergrond: `research/snowball/01-case-studies-en-copy.md` (copy, FTC, deliverability), `02-klaviyo-audit.md` (profielvelden, events), `03-flowstructuur.md` (flows S0 t/m S7, frequentiebudget), `04-commissie-economie.md`.

## Uitgangspunten

- Afzender Benjamin, merknaam Siraat, kalm flowregister, vaste header en footer (lockup), geen em dash.
- **Commissie en vriendenkorting komen uit profielvariabelen**, zodat een ander percentage geen templatewijziging vraagt:
  - `{{ person|lookup:'Referral Reward - SocialSnowball'|default:'20%' }}` (nu 20%)
  - `{{ person|lookup:'Referral Friend Offer - SocialSnowball'|default:'10%' }}` (nu 10%)
  - `{{ person|lookup:'Referral Link - SocialSnowball'|default:'https://siraatskitchen.com' }}`
  - `{{ person|lookup:'Referral Code - SocialSnowball'|default:'' }}` (codevak verdwijnt als leeg)
  - `{{ person|lookup:'Referral Currency - SocialSnowball'|default:'$' }}` (alleen in sale en payout)
- **Vaste bedragen staan alleen in het rekenvoorbeeld** (aff-announce) en in onderwerp/preview: Pan Pro Duo $229, vriend betaalt $206.10, jij krijgt 20% daarvan = $41.22. In de bron gemarkeerd met `UPDATE IF COMMISSION CHANGES`. Als Snowball de commissie over het bedrag vóór de vriendenkorting rekent, wordt het $45.80. In dezelfde comment staan de getallen voor het advies 15%/15% (research/snowball/05-aanbod-besluit.md, nog niet akkoord): Pan Pro Duo $229, vriend betaalt $194.65, commissie $29.20; Pan Pro Standard $144: commissie ca. $18.36.
- Eerlijke verdienclaims: geen inkomensbeloftes, geen verzonnen verhalen, alleen het rekenvoorbeeld per order en "No target and no posting schedule. What you earn depends only on how many friends order." Geen "no minimum" (advies: minimum $10).
- FTC: in elke mail de regel "One rule when you share: let friends know you earn a commission. 'It's my referral link' is enough." In de deelkit staat de disclosure in elke kant-en-klare tekst (#ad vooraan in de Instagram-caption).
- Uitbetaling: cash via Tremendous (Visa virtual card, Amazon gift card, PayPal, Venmo, bank). Copy noemt geen wachttijd (Floris 21 okt: "return window"-zin weg), alleen "Paid in USD through Tremendous", volgens advies 05-aanbod-besluit (45 dagen na verzending, minimum $10; nog niet akkoord Floris). Geen bedrag voor het minimum in de copy.
- Beelden: AI (flash-stijl, verzonnen personen). Nooit presenteren als klant, affiliate of reviewer; alt-teksten beschrijven alleen de scène.
- UTM op eigen links: `utm_campaign=aff-v1`. De referral-link zelf zonder UTM (die moet schoon gedeeld worden).

## Mails

| Bestand | Doel | Trigger / plaats (voorstel, sluit aan op 03-flowstructuur) | Onderwerp A / B | Preview |
| --- | --- | --- | --- | --- |
| `aff-announce` | Eenmalig uitleggen aan de 437 automatisch ingeschreven kopers (13 t/m 21 okt) dat ze al een link hebben. Wat het is, wat vrienden krijgen, wat jij verdient, rekenvoorbeeld, link + code, uitbetaling, 3 deelideeën, FTC. | Campagne. Segment: Enrolled in SocialSnowball through purchase (XzrVJZ) vóór de start van S1, kan e-mailmarketing ontvangen (~420), geen Refunded Order, geen Opened Ticket in 30 dagen, niet in holdout (`snow_pilot` != out). Smart sending aan. Verzenden als de meesten bezorgd zijn (voorstel: 29 okt, 10:00 ET). | A: You already have your own Siraat link · B: A quick note from Benjamin | Friends get 10% off with it. You earn 20% of what they pay. |
| `aff-block` | Herbruikbaar blok (geen mail): beeld, één regel, vriendenkorting, verdienregel, link, knop, FTC-regel. Alleen zichtbaar met een link en niet in de holdout. | VQ93sx levering (P2, actie 119850581, onderaan vóór de footer), "How is the pan treating you?" (X3ySuU), bedankmail na review (REV1 / S4). Codetemplates: rijen uit `aff-block.html` (bron, `{{IMG}}`) of `aff-block.klaviyo.html` (CDN). Drag-and-drop: `aff-block.universal.html` als universal content. | n.v.t. | n.v.t. |
| `aff-welcome-kit` | Welkom + deelkit: link, hoe het werkt, drie kant-en-klare teksten (sms/WhatsApp, Instagram-caption, e-mail aan een vriend), elk met disclosure, drie eerlijke regels. | Flow "Affiliate · welkom + nudges" mail 1 = S1-A1 in 03-flowstructuur: trigger XzrVJZ, wachten tot na bezorging (S1: 31 dagen, of Delivered Shipment + 5 dagen), verzendfilter F-BEZORGD, geen aff-announce ontvangen, smart sending aan. | A: Your link is ready · B: 3 messages you can copy and send | Text, Instagram or email. Each one ready to paste. |
| `aff-nudge-1` | Activatie, hoek "de makkelijkste manier": niet posten maar antwoorden als iemand vraagt; link opslaan. Tekstmail zonder hero. | Welcome-kit + 7 dagen, alleen als New referral sale (Xqbr4d) 0 keer sinds flowstart. | A: The easiest way to share your link · B: Has anyone asked about your pan yet? | Not a post. Just an answer when someone asks what pan that is. |
| `aff-nudge-2` | Activatie, hoek "wat je vrienden krijgen": 10% off, titanium zonder coating, PFAS-rapport 25895, 75 jaar garantie, gratis verzending, 30 dagen retour. Laatste herinnering ("last reminder", moet waar blijven). | Nudge-1 + 7 dagen, zelfde voorwaarde. Daarna geen affiliate-nudge meer. | A: What your friends get with your link · B: 10% off, plus everything you got | The same pan, the same 75-year warranty, and 10% off from you. |
| `aff-sale` | Melding "een vriend bestelde met je link": orderwaarde en commissie, wat er nu gebeurt, link opnieuw delen. Geen naam van de vriend. | Flow "Affiliate · verkoop" (S5a, vervangt draft VnWwqJ): trigger New referral sale (Xqbr4d), 15 min, max 1 per 3 dagen, smart sending uit. | A: A friend just ordered with your link · B: Thank you for passing it on | Here's what you earned, and what happens next. |
| `aff-payout` | Uitbetaling verstuurd: bedrag, Tremendous-mail claimen (5 opties), dashboard, blijven delen. | Flow "Affiliate · uitbetaling" (S5b, vervangt draft VdNKHq): trigger Payout sent (WManrA), direct, max 1 per 14 dagen, smart sending uit. | A: Your payout is on its way · B: Thank you. Here's your commission. | Look for an email from Tremendous to choose how you get paid. |

Per mail staan de vijf onderwerpregels (één per type) en de keuze voor de A/B in de topcomment van de bron. A/B telkens één variabele, winnaar op unieke kliks (bij nudges en welcome liever op referral-sales per ontvanger zodra er volume is).

## Bedragen in sale en payout

Volgens de audit dragen de events bijna niets: New referral sale heeft alleen `Social Snowball - Conversion ID` en `$value`, Payout sent alleen de Conversion ID. De bedragen staan als profieleigenschap. De templates lezen daarom in deze volgorde, en vallen netjes terug:

- Orderwaarde: `event|lookup:'Social Snowball: Affiliate Order Value'` → `event|lookup:'$value'` → `person|lookup:'Social Snowball: Affiliate Order Value'` → "in your dashboard".
- Commissie / uitbetaling: `event|lookup:'Social Snowball: Payout amount'` → `person|lookup:'Social Snowball: Payout amount'` → "in your dashboard" (sale) of een zin zonder bedrag (payout).
- Risico (audit 3.5): bij twee sales kort na elkaar kan het profielbedrag bij de verkeerde sale horen. Daarom 15 minuten wachten en max 1 verkoopmail per 3 dagen.

## Previews en QA

- Previews (Django-render met voorbeeldprofiel Sarah, link `SARAH48213`, 20%/10%; sale $206.10/$41.22; payout $82.44): `*-preview.html`. Screenshots 375 en 600 px (2x) in `previews/`.
- Gecontroleerd: geen horizontale scroll (375 en 600), geen kapotte beelden, geen restanten `{{ }}`/`{% %}`, geen em dash, `scripts/check_previews.py affiliate` 0 problemen. Klaviyo-versies ook gerenderd met een leeg profiel: defaults werken, het blok verdwijnt.
- `qa_render.py` kent de map affiliate nog niet (FLOWS-lijst); toevoegen met een sample voor Xqbr4d/WManrA vóór een export.
- `aff-block-demo.html` is alleen een preview-omgeving voor het blok, niet versturen.

## Open punten voor Floris

1. **Commissie definitief?** Nu 20% / 10% op het profiel; advies 05-aanbod-besluit is 15% commissie (netto, max $50) en 15% vriendenkorting alleen op een eerste order. De mails volgen het profiel vanzelf, maar het rekenvoorbeeld in aff-announce en de percentages in onderwerp en preview staan vast (UPDATE IF COMMISSION CHANGES).
2. **Rekenbasis**: commissie over wat de vriend betaalt (na 10%) of over de prijs vóór korting? Copy zegt "20% of what they pay" ($41.22). Anders wordt het $45.80 en de tekst "20% of the order".
3. **Portal-URL**: nu `https://affiliates.socialsnowball.io/auth/affiliate/login` (uit de drafts). Is er een Siraat-portal of een andere login-URL?
4. **Werkt de Referral Code bij het afrekenen?** Codetype is "tracking link" (Safelinks maakt per klik een unieke code). Als de code zelf niet in de checkout werkt, het codevak weghalen.
5. **Wachttijd en minimum uitbetaling**: copy zegt nu "monthly, once the return window has passed" (advies: 45 dagen na verzending, minimum $10). Klopt dat met de Snowball-instelling? Anders die zin aanpassen in announce, welcome-kit en sale.
6. **Alleen nieuwe klanten / alleen eerste order** voor de vriendenkorting: niet in de copy tot het in Snowball zo staat.
7. **Tremendous-mail**: klopt het dat Tremendous zelf een claimmail stuurt met de vijf opties (Visa virtual card, Amazon, PayPal, Venmo, bank)? Bevestigen welke opties echt aanstaan.
8. **Timing aff-announce**: voorstel 29 okt (meeste orders van 13 t/m 21 okt dan bezorgd). Of samenvoegen met S1 zodat de 437 gewoon in S1 lopen.
9. **Frequentiebudget**: 03-flowstructuur gaat uit van maximaal 2 activatiemails (A1, A2 alleen klikkers). Deze set heeft welcome-kit + 2 nudges. Voorstel: nudge-1 alleen naar wie de welcome-kit opende of klikte, nudge-2 alleen naar klikkers zonder sale; of nudge-2 schrappen.
10. **Afzender**: "Benjamin at Siraat" met reply-to support? De drafts gebruiken "SiraatsKitchen" zonder reply-to.
11. **Holdout/pilot**: het blok toont niet bij `snow_pilot == 'out'`. De nachtelijke `snow_block_ok`-vlag (03, sectie 4) is nog niet gebouwd; tot dan blok alleen in de pilot.
12. Sale en payout zijn meldingen: als marketing versturen (alleen wie mag) of transactioneel? Advies: marketing, omdat er een deeloproep in staat.
