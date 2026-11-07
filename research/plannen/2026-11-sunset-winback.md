# Sunset en winback in de Black Friday-sale (7 nov 2026)

Vraag: Sunset TbYQmX mailt ~9.500 per week voor $0, Winback UyFc78 staat live maar had 0 ontvangers, de oude winback UEfh4h verdient wel iets. Doel: één sterke VIP Black Friday-mail in de sunset (doel $0,25 per ontvanger) en een BF-winback voor eerdere kopers (doel $0,60 per ontvanger). Alleen gelezen in Klaviyo (GET plus flow-values-reports en metric-aggregates), niets gewijzigd, geen testmails.

## 1. Audit (flow-values-report 24 okt tot 7 nov 2026, conversie Placed Order RSNxYV)

| Flow | Mail (actie) | Wachttijd | Status | Ontv. | Opens | Kliks | Orders | Omzet | RPR | Uitschr. | Spam |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TbYQmX Sunset | S1 'Should we keep writing to you?' (119850754) | 1 d, 09:00 | live | 9.017 | 3.428 (38%) | 27 (0,30%) | 2 | $153,95 | $0,017 | 45 (0,50%) | 0 |
| TbYQmX Sunset | S2 'Last email from me (unless you tap)' (119850756) | +4 d, 09:00 | live | 7.743 | 2.554 (33%) | 33 (0,43%) | 0 | $0 | $0 | 25 (0,32%) | 1 |
| Wzz6xC Sunset kept | S3 'You're staying. Thank you.' (119850775) | 30 min | live | 60 | 34 | 5 | 0 | $0 | $0 | 0 | 0 |
| Wzz6xC Sunset kept | S4 'The pan we started with' (119850777) | +4 d, 09:00 | live | 46 | 26 | 2 | 1 | $373,99 | $8,13 | 0 | 0 |
| UyFc78 Winback v4 | R1-SET / R1-PAN kook / R1-PAN eigenaar / R1-ACC (119850720 tot 723), daarna 30 d en splits naar 6 R2-varianten | 45 d, 09:00 | alle live | 0 | 0 | 0 | 0 | $0 | n.v.t. | 0 | 0 |
| UEfh4h oude winback | Email #1 'Serving Up New Must-Haves' (81010377) | 60 d, 08:00 | live | 2.192 | 862 | 9 | 1 | $31,80 | $0,015 | 5 | 0 |
| UEfh4h | Email #2 A 'We Cut a Deal for You' (81011317) | +2 d | live | 1.090 | 442 | 9 | 1 | $144,91 | $0,133 | 3 | 0 |
| UEfh4h | Email #2 B kopie (104289065) | +1 d | live | 1.107 | 459 | 6 | 0 | $0 | $0 | 7 | 0 |
| UEfh4h | Email #3 '10% Off Expires Tonight' (81011677) | +1 d | live | 2.209 | 904 | 4 | 2 | $259,32 | $0,117 | 17 (0,77%) | 1 |

Totalen 14 dagen: Sunset 16.760 ontvangers, $154 ($0,009 per ontvanger). Kept 106, $374. UEfh4h 6.598, $436 ($0,066). UyFc78 0.

Triggers en filters:
- TbYQmX: segment WuHSm6 'v4 · Sunset · unengaged 120d' (nu 88.640 leden), vuurt alleen bij nieuwe instroom. Flowfilter: niet in deze flow in 180 d, geen mail uit Welcome T4a5Mk en Post-purchase X3ySuU in 30 d. S2 alleen zonder klik (Bot Click = false), zonder UdCdLD en zonder order sinds flowstart. Smart sending uit. **Er is geen onderdrukkingsstap**: wie na S2 niet klikt, krijgt gewoon weer campagnes (zie LOG 15 en 24 okt).
- Wzz6xC: segment YxfuJT 'kept (klik 7d)' (36 leden), filter niet in flow in 365 d. S3 en S4 alleen zonder order sinds flowstart; S4 ook zonder checkout-/cartmail in 3 d.
- UyFc78: zie sectie 2.
- UEfh4h: trigger Placed Order, 60 d, sinds 8 okt per mail: Placed Order = 0 na 2026-10-09, nooit een mail uit UyFc78, order in de laatste 63 tot 66 d. Bedient dus alleen orders van vóór 9 okt en droogt rond 8 dec op (Floris: loopt door tot 14 dec).

## 2. Waarom UyFc78 niemand krijgt

Het is geen kapotte filter, het is de klok.

1. UyFc78 ging live op 8 okt 22:29 UTC (LOG, livegang v5). Trigger Placed Order (RSNxYV), geen triggerfilter, geen flowfilter, geen herinstapregel.
2. De eerste stap is een wachttijd van 45 dagen tot 09:00 profieltijd (actie 119850719). Een metric-flow neemt alleen orders op die na de livegang binnenkomen, geen historie.
3. De eerste order die de flow kon vangen is dus van 8 okt 22:29 UTC. 45 dagen later is 22 nov 22:29 UTC; de eerste R1 gaat op **23 nov 09:00 lokale tijd**.
4. Bewijs dat de wachtrij gevuld is: metric-aggregates Placed Order 9 okt tot 7 nov: 8.143 orders (~7.900 profielen per maandvak), allemaal in de wachttijd. Het flow-values-report 24 okt tot 7 nov geeft voor UyFc78 geen enkele rij (0 ontvangers), UEfh4h wel 6.598.
5. De R1-filters sluiten niemand uit op dag 45: ze vragen een order in de laatste 46 of 48 dagen, geen nieuwe order sinds flowstart en geen post-purchase/VIP-mail in 7 dagen.

Gevolg voor Black Friday: UyFc78 bereikt vanaf 23 nov alleen kopers van na 9 okt (45 d terug), UEfh4h alleen kopers van ongeveer 9 aug tot 8 okt (op dag 60). **Wie zijn laatste order vóór ~9 aug plaatste (nov 2025 tot aug 2026: ~83.000 orders) krijgt in de hele sale geen winback.** Dat is het echte gat.

Tweede fout (komt op 23 nov boven): set-kopers met een orderwaarde onder $300 krijgen geen R1. R1-SET vraagt een set én $value >= 300 in 46 d; R1-PAN kook vraagt set = 0; R1-PAN eigenaar vraagt 0 orders uit de pannenlijst in 46 d, en die lijst bevat ook de settitels; R1-ACC vraagt 0 keer de pannenlijst ooit. De 6-delige set kost in de sale minder dan $300, dus die kopers vallen door alle vier de takken.

### De fix (Floris in de UI, of API met akkoord; niets gedaan)

1. UyFc78 niet ombouwen: de flow werkt, hij is alleen jong. Wel in actie 119850720 (R1-SET) de conditie '$value greater-than-or-equal 300 in de laatste 46 dagen' verwijderen, zodat elke set-koper R1-SET krijgt.
2. Nieuw segment 'v4 · Winback BF · eerdere kopers': Placed Order minstens 1 keer ooit, Placed Order 0 keer in de laatste 45 dagen, kan e-mailmarketing ontvangen. (De 45 dagen sluit iedereen uit die nu in de UyFc78-wachttijd zit.)
3. Nieuwe flow 'v4 · Winback BF' als Draft: trigger dat segment; flowfilter geen mail uit UEfh4h, UyFc78 of X3ySuU in 7 dagen; herinstap 1 keer ooit. Acties: conditional split op person.Country (US of leeg naar wbf-us, anders wbf-int), elke tak direct de mail om 10:00 lokale tijd, smart sending aan, verzendfilter 'Placed Order 0 sinds flowstart'.
4. Bij het live zetten 'Add past profiles' kiezen, anders vangt ook deze segmentflow alleen nieuwe instroom en hebben we hetzelfde probleem als UyFc78. Gespreid over 2 tot 3 dagen (deliverability) als de UI dat aanbiedt.
5. Uit op 1 dec (mail naar Draft), dan neemt UyFc78 het weer alleen over.

## 3. Nieuwe mails (klaviyo/templates/v3/flows-nov/sunset-winback/)

Bron `_tools/make_sw.py` (helpers van signup/make_bfw.py, vaste header en footer via build_template.py), render `_tools/render_sw.py`, screenshots `_tools/shot_sw.js`. Per mail .html, .klaviyo.html, -preview.html en `previews/<id>-<markt>-375.png` en `-600.png`. Gecontroleerd: 375 en 600 px zonder overloop, alle beelden laden, elk beeld en het hele herobeeld klikbaar, 0 gedachtestreepjes, geen bedragen, geen code, geen einddatum, label VIP Black Friday, alleen de sale-tags geel (topbalk oranje zoals de rest van flows-nov sinds 7 nov), knoppen ink.

### sbf-us / sbf-int · Sunset 'One last look at 70% off'
- Afzender Benjamin from Siraat. A/B onderwerp (schaarste tegen vraag): A 'Before I stop writing: your 70% off', B 'Still cooking on a coated pan?'. Preview: 'Up to 70% off, 4 gifts with every order, no code needed. The last sale email you will get from me.'
- Opbouw: korte opener van Benjamin, herobeeld ei uit de pan met glaspaneel, knop 'Get my Black Friday price' met friction reducer, één alinea sale, één alinea Light Labs 25895, kaarten Pan Pro Standard en 6-delige set, review Scott Y. (R583), de ware schaarste ('This is the last sale email you'll get from me ... Unless you tap anything in this email'), ondertekening, BF-band.
- Plaats in TbYQmX: S1 (dag 1) → 2 dagen tot 09:00 → **conditional split person.Country → sbf-us / sbf-int** → 2 dagen tot 09:00 → S2 (de wachttijd van S2 gaat van 4 naar 2 dagen, S2 blijft op dag 5) → 3 dagen → **nieuwe onderdrukkingsstap**: profieleigenschap `sunset_suppressed = true` (of naar een lijst 'Sunset · suppressed') voor wie geen klik en geen order heeft sinds flowstart, en dat segment uitsluiten van alle campagnes.
- Filters op sbf: geen klik sinds flowstart (Bot Click = false), geen order sinds flowstart. Wie klikt, gaat via YxfuJT de kept-flow in en krijgt S2 niet.
- Voorwaarde: zonder onderdrukkingsstap klopt 'last sale email' niet (ze krijgen daarna gewoon campagnes). Dus sbf pas live samen met die stap.
- Wzz6xC (kept): geen extra mail. 36 leden per week, S4 verdient al. Hooguit S4 later in BF-stijl.

### wbf-us / wbf-int · Winback 'Your next pan, up to 70% off'
- Afzender Benjamin from Siraat. A/B onderwerp (aanbod tegen sociaal bewijs): A 'Up to 70% off your second pan', B '"I am on my 4th pan from Siraat"'. Preview: '4 gifts with every order, no code needed. Here is where I would go next.'
- Opbouw: herobeeld feesttafel met twee pannen, knop 'Get my VIP price', opener ('You've had a Siraat box on your doorstep before, so I'll skip the pitch'), waarom een tweede pan, review Tammy (R138, 4e pan, cadeau aan haar zoon), kaarten Pan Pro Standard, Deep Pan Pro, 6-delige set (US ook 12-delige set), cadeauregel plus 75-year warranty en 30-day returns, ondertekening, BF-band.
- Plaats: de nieuwe flow 'v4 · Winback BF' uit sectie 2. Niet in UyFc78: R1 daar is al in BF-stijl en start vanzelf op 23 nov.

## 4. Verwacht effect (schatting, geen meting)

Rekenbasis: gemiddelde orderwaarde sinds 9 okt $235 (Placed Order $1.914.701 / 8.143).

- Sunset sbf: ~4.400 ontvangers per week (S1 min klikkers). Bij 0,8% klik en 6% conversie: ~$0,11 per ontvanger, ~$500 per week. De $0,25 vraagt ~1,2% klik en 9% conversie; mogelijk in de BF-week zelf, niet als gemiddelde. Belangrijker voor de omzet: de onderdrukkingsstap haalt ~4.000 stille profielen per week uit de campagnes (LOG 24 okt: WuHSm6 kreeg 786.556 campagnemails in 30 dagen), wat de inbox-plaatsing voor de rest verbetert.
- Winback wbf: geschat 40.000 tot 60.000 mailbare eerdere kopers (gecontroleerd zodra het segment bestaat). Bij 2% klik en 10% conversie ~$0,47 per ontvanger; $0,60 bij 2,5% klik. Eenmalig $19.000 tot $28.000 in de sale. Ter vergelijking: UEfh4h haalt nu $0,066 met oude copy en 10%-codes.
- UyFc78 levert vanaf 23 nov vanzelf; met de R1-SET-fix krijgen ook de set-kopers onder $300 hun mail.

## 5. Open voor Floris

1. Akkoord op de onderdrukkingsstap in TbYQmX (zonder die stap geen sbf).
2. Akkoord op segment en flow 'v4 · Winback BF' plus 'Add past profiles', en op de R1-SET-fix in UyFc78.
3. Beelden: IM_EGG (sunset) en IM_TABLE (winback) staan al in Klaviyo; geen nieuwe uploads nodig.
4. Figma-rij (DECISIONS 4 nov) nog niet gemaakt.
