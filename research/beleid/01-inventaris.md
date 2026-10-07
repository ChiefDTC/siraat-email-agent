# 01 · Inventaris: wat Siraat belooft over retour, trial en garantie

Datum: 7 oktober 2026. Alleen gelezen in Shopify, Gorgias en de repo. Niets gewijzigd, niets gepubliceerd. Geen persoonsgegevens: ticketcijfers zijn aggregaten, citaten zonder naam of ordernummer.

Volledige tabel (71 plekken, met bron, zichtbaarheid en prioriteit): `research/beleid/inventaris.csv`.

## In het kort

1. **De site belooft iets anders dan service doet.** Alle actieve pan-, set-, pizza-, roasting- en snijplank-PDP's (thema `ecomspace/prime-sale`, bijgewerkt 7 okt) hebben een blok "Risk-free purchase": *"Cook on your pan at home for 30 days, and if it isn't the best pan you've owned, return it for a full refund."* Het beleid (Shopify refund policy, AI-guidance 5302114) zegt: alleen ongebruikt retour, plakken is geen defect. De site belooft dus in feite variant (c) uit `02-leer-garantie.md`; service voert variant (a) uit. Dat is de kern van het vertrouwensprobleem, en in de VS een risico onder de FTC-gidsen voor garanties (16 CFR 239: een "satisfaction or your money back"-belofte moet je nakomen).
2. **Wie betaalt de retourzending is nergens hetzelfde.** Shopify refund policy en help center: klant betaalt. AI-guidances 5302114, 8566447, 5831674, PDP-iconen en v3-mails W2, W5, S2: gratis. Macro's 247094 en 247095: klant betaalt, met 10 procent, 20 procent tegoed of 50/50 als goodwill. In tickets zeggen agenten het allebei (98 tickets "klant betaalt", 108 "gratis", 180 dagen), en "klant betaalt" stijgt: 2 in april naar 41 in september.
3. **"Lifetime" leeft nog op de plek waar DECISIONS naar verwijst.** `/pages/warranty` zegt "lifetime warranty ... as long as you own it". Daarnaast "lifetime" in PDP-beschrijvingen, het PDP-kopblok ("for a lifetime, not a season"), de snijplank-PDP en de PLAYBOOK (hfst. 1 en 8: "levenslange garantie en 100 dagen proef").
4. **Macro 249761 (213 keer gebruikt) zegt dat de pan een coating heeft**: "properly activating the non-stick layer, as this ensures the coating works as intended". Dat ondermijnt de kernclaim "no coatings" precies op het moment dat een klant twijfelt.
5. **Wat al goed is:** de 31+9 v3-mails, footer en icoonblok noemen "30-day returns" en "75-year warranty" correct; geen enkele v3-mail noemt nog een trial. De announcement bar toont geen 100-DAY TRIAL meer (content/facts is op dat punt verouderd), maar ook geen retourbelofte: alleen een sale-teller zonder einddatum.

## Wat is "het beleid"?

Er is geen één bron. Voor deze inventaris geldt als beleid:

| Onderwerp | Bron die leidend is | Tekst |
|---|---|---|
| Retourtermijn | DECISIONS 2026-10-01 en Shopify refund policy | 30 dagen na bezorging, alleen ongebruikt, originele verpakking, vooraf goedgekeurd |
| Gebruikt product | Shopify refund policy, guidance 5302114 | Geen refund, tenzij defect. "Food sticking to the pan is not a defect" |
| Garantie | DECISIONS 2026-10-01, guidance 5831676 | 75-year warranty tegen defecten (deuk, kromme bodem, losse steel, klinknagels, deksel past niet). Niet: plakken, verkleuring, slijtage |
| Schade bij aankomst of defect binnen 30 dagen | Shopify refund policy | Klant kiest refund of vervanging, Siraat betaalt verzending |
| Retourzending ongebruikt product | **Onbeslist** | Shopify-beleid: klant betaalt. Guidance: gratis. Moet Floris kiezen |
| Trial | Guidance 5302114 | Bestaat niet meer sinds 15 september 2026; oudere orders per geval |

## Tabel: plek, exacte tekst, klopt, fix

Tekens als gedachtestreepjes in brontekst zijn vervangen door [gedachtestreepje]. "Onbeslist" = klopt met de ene beleidsbron en niet met de andere.

### Announcement bar en PDP's (Shopify-thema, live)

| Plek | Exacte tekst | Klopt | Fix |
|---|---|---|---|
| Announcement bar, actief blok | "PRIME SALE · Up to 70% off · ends in" + teller 2h 43m in een lus (geen einddatum ingevuld) | n.v.t. | Echte einddatum of teller uit. Retourbelofte terug als tweede blok |
| Announcement bar, uitgeschakeld | "FREE SHIPPING \| 30-DAY RETURNS \| 75-YEAR WARRANTY" | ja | Aanzetten |
| Pan-PDP's (Standard, Small, Large, Mini, Duo, Kit, Set Pro, Full Pro, Complete Edition, Deep, Wok, Crepe, Pan met deksel) | "Risk-free purchase. Cook on your pan at home for 30 days, and if it isn't the best pan you've owned, return it for a full refund. Your 75-year warranty covers it from there." | **nee** | Kritiek. Tekst gelijk aan de gekozen variant uit 02 |
| Zelfde PDP's, FAQ | "Cook on it for 30 days; if it isn't the best pan you've owned, return it for a full refund." | **nee** | Idem |
| Zelfde PDP's, iconen | "30-Day Returns · free returns · 75-Year Warranty · covered for 75 years" | deels | "free returns" na besluit retourkosten |
| Pan-PDP's, kopblok | "A coating-free surface that sears clean and releases naturally [gedachtestreepje] for a lifetime, not a season." | nee | "...releases naturally, year after year." |
| Sets (6-Pcs, 12-Pcs, potten) | "Try your set at home for 30 days, cook everything you love in it, and if it isn't the best cookware you've owned, return it for a full refund." / "The whole set is returnable within 30 days for a full refund." | **nee** | Idem pan-PDP |
| Sets en Roasting Pan, trust-regel | "Free Express Shipping from the US · 30-Day Returns · free returns" | nee | "Free shipping" (verzendbeleid: 6 tot 10 dagen, geen express) |
| Pizza Steel | "Bake on it for 30 days, and if it isn't the best pizza surface you've owned, return it for a full refund." | nee | Idem pan-PDP |
| Roasting Pan | "Roast at home for 30 days, and if it isn't the best roasting pan you've owned, return it for a full refund." + "for a lifetime, not a season" | nee | Idem, plus metafields nalopen op het oude "100-day trial" |
| Snijplank V2 en bundel | "Use your board at home for 30 days, and if it isn't the cleanest, safest board you've owned, return it for a full refund." + 4x "built to last a lifetime" | nee | Idem |
| product.json en testing-templ (Pan Pro "-copy"-listings) | "We want you to be sure. Try your pan at home for 30 days ... return it for a full refund." + "Lifetime Durability", "sturdy for life" | nee | Idem; copy-listings archiveren |
| Deksel | "75-Year Warranty · 30-Day Returns" | ja | Geen |
| Productbeschrijvingen (Admin) | "a lifetime of reliable use", "practically indestructible", "for a lifetime of performance", "scratch-proof ... the last cookware set you'll ever need" | deels | "built to last, with a 75-year warranty against defects" |

### Beleidspagina's (Shopify)

| Plek | Exacte tekst | Klopt | Fix |
|---|---|---|---|
| Refund policy, kop | "You can return any unused Siraat product within 30 days of delivery for a full refund. Every product is also protected by our 75-Year Warranty against defects, for as long as you own it." | ja | "for 75 years" i.p.v. "for as long as you own it" |
| Refund policy, gebruikt | "Products that have been used cannot be returned for a refund, unless they have a defect. Food sticking to the pan is not a defect" | ja (is het beleid) | Leidend tot Floris kiest |
| Refund policy, kosten | "Return shipping for unused products is the customer's responsibility." | onbeslist | Besluit retourkosten |
| Refund policy, reactietijd | "Our team responds within 1 hour with return instructions" | deels | Eén belofte; warranty-pagina en help center zeggen 24 uur |
| /pages/warranty | "Every Siraat product is covered by a lifetime warranty against manufacturing defects ... a warranty that lasts as long as you own it." | **nee** | "75-year warranty" |
| /pages/warranty, uitsluiting | "The warranty does not cover: ... Damage from accidents, drops, or impacts" | deels | Guidance en mail N1 noemen "a dent" gedekt. Eén definitie |
| Shipping policy | "free worldwide shipping on all orders", VS 6 tot 10 kalenderdagen | ja | PDP "Express" weg |
| /pages/our-responsibility, better-for-the-world | "built to last a lifetime" (snijplank) | deels | "built to last" + 75 jaar |

### Help center (Gorgias 124366, staat "deactivated", artikelen wel gepubliceerd en public)

| Artikel | Exacte tekst | Klopt | Fix |
|---|---|---|---|
| 5326409 Refund policy | "every order comes with a 100-day trial period ... Use it, cook with it ... If it's not for you, we'll take it back. No complicated process." | nee | Herschrijven of unpublishen voordat iemand het help center aanzet |
| 5326415 How to Return | "All returns must be requested within 100 days of delivery" / "respond within 24 hours" | nee | 30 dagen, portal |
| 5326416 Unused Products | "Changed your mind before using it? ... we'll issue a full refund." | ja | Termijn erbij |
| 5326418 Used Products | "We encourage you to actually cook with your Siraat, that's the whole point of the trial." | nee | Bij variant (b): hier "Learn it in 30 days" |
| 5326419 Refund Timeline | "Confirmation email within 3 business days ... Allow 5-10 business days" | deels | Eén tijdlijn met guidance (tot 10 werkdagen + 5 tot 7) |
| 5326421 Shipping Costs | "Return shipping is the customer's responsibility." | onbeslist | Besluit retourkosten |
| 5326444 Why titanium | "built to last a lifetime" | nee | Herschrijven |

### Macro's (Gorgias)

| Macro (gebruik) | Exacte tekst | Klopt | Fix |
|---|---|---|---|
| 247063 Return Template (893) | "Once submitted, we will review and approve your submission, and then send you a return label." | deels | Voorwaarden (ongebruikt, 30 dagen) en kosten toevoegen. Let op: deze macro zegt níet dat de klant betaalt, anders dan content/facts stelt |
| 247094 Return fee too high (15) | "return shipping fees for international orders ... are the responsibility of the customer ... A 10% partial refund, or A 20% store credit" | onbeslist | Na besluit retourkosten; goodwill-ladder vastleggen |
| 247095 Final option (0) | "we would cover 50% of the return shipping cost" | onbeslist | Idem |
| 247061 Return - Used (2) | "unable to accept returns of used items ... happy to offer you an 80% refund, as a gesture of goodwill" | nee | Vervangen door de macro van de gekozen variant |
| 247068 Maximum offer (0) | "a 30% refund for your purchase ... no need to return the item" | nee | Archiveren of in goodwill-ladder |
| 249761 Non-stick Troubleshooting (213) | "properly activating the non-stick layer, as this ensures the coating works as intended" | **nee** | Kritiek: "There is no coating, so the release comes from heat control" |
| 247048 Non-stick pan (269) | "your nonstick cookware ... Titanium Hammerhead Pan" | deels | "your titanium pan", juiste productnaam |
| 246881 Return Instructions (5) | "Since your order was delivered on [datum] we're happy to process a return for you." | deels | Voorwaarden toevoegen of archiveren |
| 247078 Refund Processed (901) | "approximately 5-7 business days" | ja | Geen |
| 246886 Damaged Items (1) | "send us a photo of the broken/damaged item(s) ... we'll do our best to resolve this" | ja | Keuze refund of vervanging noemen |

### AI-guidances (Gorgias, AI-agent "Noah")

| Guidance | Exacte tekst | Klopt | Fix |
|---|---|---|---|
| 5302114 returns (aan) | "Siraat no longer offers a 100-day trial, free trial, or money-back guarantee ... can be returned free of charge within 30 days of delivery" | deels | "free of charge" na besluit retourkosten |
| 5302114, gebruikt | "used products cannot be returned for a refund, and that sticking is a technique issue rather than a defect ... Do not offer partial refunds" | ja | Botst met PDP; menselijke agenten bieden wel goodwill |
| 5831676 warranty (aan) | "75-year warranty against defects, such as a dent, a warped base, a loose or broken handle ... does not cover food sticking" | ja | "dent" afstemmen met warranty-pagina |
| 8566447 product advice (aan) | "free 30-day returns on unused products, and the 75-year warranty against defects ... Never call it a lifetime warranty" | deels | Retourkosten |
| 5302143 quality issue (aan) | "sticking and discolouration are not defects ... used products cannot be returned for a refund" | ja | Botst met PDP |
| 5831672 refund request (gepubliceerd, AI uit) | "refunds are only available within 60 days of purchase ... return shipping costs are their responsibility" | nee | Archiveren |
| 5831674 exchange (aan) | "the return is free of charge" | deels | Retourkosten |

### v3-mails (klaviyo/templates/v3, nog niet live)

| Mail | Exacte tekst | Klopt | Fix |
|---|---|---|---|
| Footer (alle) | "Free shipping on all orders · 30-day returns · 75-year warranty" | ja | Geen |
| Icoonblok (verkoopmails) | "FREE SHIPPING · 30-DAY RETURNS · 75-YEAR WARRANTY" | ja | Geen |
| K3 | "No risk on your side." / "Unused? Full refund within 30 days of delivery." | deels | Kop past niet bij beleid (plakken na gebruik niet gedekt) |
| W2 | "Not for you? Free 30-day returns." | deels | "unused" toevoegen; "free" na besluit |
| W5 | "Free 30-day returns on unused pans, and a 75-year warranty on every one." | deels | "free" na besluit |
| S2 | "every order ships with $70 in gifts and free 30-day returns." | deels | "unused", "free" na besluit |
| B1-acc, K1-acc, C2-acc, C3-acc, P3-apron, P3-next, R1-acc | "Free shipping. 30-day returns. 100,000+ happy customers." | ja | Geen |
| W4-US, W4-INT, C3-P | "Plus 30-day returns." | ja | Geen |
| W3, C2 | "A warranty that outlasts you? Yes. 75 years. No coating to fail." | ja | Geen |
| K2-new | "A $134 Siraat pan, covered for 75 years · $1.79 a year" | deels | "against defects" |
| N1 | "A dent, a warp, a loose handle? That is what the 75-year warranty is for." | deels | Na besluit over deuken |
| N2, S2, K2-returning, R1-pan, C3-S | "Your 75-year warranty has 74 to go." en varianten | ja | Geen |
| V1 (reviewquote) | "made to last a lifetime" | deels | Ander citaat |
| Oktober-draft founder note | "30-day returns from the day the box arrives. If the pan isn't for you, send it back." | deels | "send it back unused" |

### Ads-claims in de repo

| Plek | Exacte tekst | Klopt | Fix |
|---|---|---|---|
| content/hooks/hooks.csv (ROAS 2,49 op $11.323) | "Try it risk free for 100 days" | nee | In Meta controleren; vervangen |
| content/hooks/angles.md | "Subject 'Try it risk free for 100 days'" (advies voor cart 3) | nee | Advies aanpassen |
| Statics W33, W36 (aug) | "100 DAYS TO DECIDE" | nee | Controleren of nog live |
| Statics W40 (26 sep, na de wijziging) | "Zero Risk Guarantee", "Try It Keep It Or Send Back" | waarschijnlijk nee | Beeldtekst bekijken |
| 10 video's | "...-LIFETIMEGUARANTEE-..." in bestandsnaam | waarschijnlijk nee | Transcript checken |
| Notion W41 | "We lied. It carries a 75-year warranty." | ja | Geen |

### Repo-documenten die agents sturen

| Plek | Tekst | Klopt | Fix |
|---|---|---|---|
| PLAYBOOK hfst. 1 en 8 | "met levenslange garantie en 100 dagen proef", goedgekeurde claims "Lifetime warranty", "100-day trial" | nee | Bijwerken naar DECISIONS (niet gedaan, buiten opdracht) |
| content/reviews/summary.md | "approved claim: lifetime warranty", "covered by the lifetime warranty" | nee | Bijwerken |
| content/facts | balk "100-DAY TRIAL", macro 247063 "klant betaalt" | nee (verouderd) | Bijwerken; PDP-risk-free-blokken toevoegen |

**Telling over 71 plekken:** 26 nee of waarschijnlijk nee, 20 deels, 4 onbeslist (retourkosten), 19 ja, 2 n.v.t.

## Gorgias: hoe vaak, en waarom

Bron: Gorgias analytics, tickets 10 april t/m 7 oktober 2026 (180 dagen), spam uitgesloten, drie intents: Return/Request 1.795, Order/Refund 979, Warranty/Claim 270, samen 3.044. Reden per ticket via trefwoorden in de klanttekst (onderwerp plus klantberichten, geciteerde eerdere mails eruit). Eén hoofdreden per ticket, in deze volgorde: trial-verwachting, schade/defect/verkeerd product, plakken, verkleuring, maat/gewicht, retourkosten, annuleren, verandering van gedachten, levering. Grof, maar richtinggevend; 966 tickets (32 procent) hebben geen herkenbare reden of geen klanttekst (vaak "I'd like to return my order" of een portal-melding).

### Hoofdreden, aandeel van tickets met een herkenbare reden

| Reden | Return/Request | Order/Refund | Warranty/Claim | Samen | Aandeel (van 2.078) |
|---|---|---|---|---|---|
| Trial-verwachting (trial, 100 day, money back, risk-free, guarantee) | 322 | 193 | 39 | 554 | 26,7% |
| Plakken of "werkt niet" (incl. verkleuring 47) | 329 | 142 | 47 | 518 | 24,9% |
| Schade, defect, verkeerd product | 161 | 91 | 105 | 357 | 17,2% |
| Verandering van gedachten (incl. "ongebruikt, geen reden" 56) | 184 | 54 | 9 | 247 | 11,9% |
| Maat of gewicht (te groot, te zwaar, deksel past niet) | 128 | 20 | 3 | 151 | 7,3% |
| Retourkosten of retourlabel | 95 | 6 | 0 | 101 | 4,9% |
| Annuleren vóór levering | 43 | 43 | 0 | 86 | 4,1% |
| Levering | 17 | 45 | 2 | 64 | 3,1% |
| Geen of onduidelijke reden | 516 | 385 | 65 | 966 | (buiten noemer) |

Niet-exclusief (een ticket kan meer raken): **plakken in 893 van 3.044 tickets (29 procent)**, trial in 502 (16,5 procent), en 338 tickets noemen beide. Twee derde van de trial-tickets gaat dus over één vraag: "ik heb hem gebruikt, hij plakt, mag hij terug?". Dat is precies het gat dat een leer-garantie dicht.

Voor Return/Request alleen (1.279 met herkenbare reden): trial 25 procent, plakken 26 procent, verandering van gedachten 14 procent, schade 13 procent, maat 10 procent, retourkosten 7 procent. In Order/Refund weegt trial zwaarder (33 procent).

### Conflict tussen belofte en beleid

| Signaal | Tickets (van 3.044) | Toelichting |
|---|---|---|
| Klant beroept zich op een belofte (trial, money back, risk-free, free returns, full refund, "your ad says", lifetime) | 1.013 (33%) | Ruim: "full refund" telt mee |
| **Klant beroept zich op een belofte én krijgt een weigering op beleidsgronden** (gebruikt, niet eligible, geen defect) | **519 (17%)** | De kernmaat voor "conflict". Return/Request 345, Order/Refund 151, Warranty 23 |
| Agent zegt "klant betaalt retour" | 98 | Stijgt per maand: apr 2, mei 9, jun 10, jul 11, aug 23, sep 41 |
| Agent of AI zegt "gratis retour" | 108 | Beide standpunten lopen naast elkaar |
| Agent biedt gedeeltelijke refund of tegoed | tot 1.161 | Bovengrens (trefwoordmatch). Goodwill is praktijk, staat nergens in beleid; guidance verbiedt het de AI |
| Klant noemt chargeback, dispuut of review | 455 (15%) | Escalatiedruk |

Na 15 september (nieuwe beleid) noemen nog 40 tickets in de drie intents een trial; de PDP-belofte "cook on it for 30 days ... full refund" kan de volgende golf worden, nu met een termijn die korter is maar dezelfde botsing.

### Trustpilot (content/reviews, 180 dagen)

Van 154 lage reviews (1 tot 3 sterren) noemen er 97 tot 100 retour, refund of de trial; 47 noemen Siraat "scam" of "fake" (summary.md; eigen telling op de geciteerde tekst: 97 en 29). Lage reviews over retour liepen per maand: apr 13, mei 22, jun 31, jul 12, aug 10, sep 9. Het probleem bestond dus al onder de 100-day trial: ook toen kregen gebruikte pannen geen volledige refund (80 procent goodwill-macro). Typerende zin, geanonimiseerd: *"The company noted a 100-day guarantee on their product. Then, when I inquired about returning the items, they told me that I could not return them because I had tried them."*

## Wat niet gecontroleerd is

- Wat het retourportaal (return.siraatskitchen.com) zelf belooft en of het retourlabels gratis aanmaakt.
- Of de ads uit de repo (D1 tot D5 in de CSV) nog live staan in Meta; alleen bestandsnamen en hooks gezien.
- Klaviyo live flows (opdracht: alleen v3-bronnen). De live welcome- en post-purchase-mails kunnen nog oude claims bevatten.
- PDP-metafields en apps (Okendo-widget, Alia-pop-up) buiten de thema-templates.
- Juridische toets: EU- en UK-klanten hebben een wettelijk herroepingsrecht van 14 dagen; een "used = geen refund"-regel mag daar hooguit waardevermindering verrekenen, niet de hele refund weigeren. Retourkosten mogen alleen bij de klant liggen als dat vooraf duidelijk is gemeld. In Australië geldt de ACL. Laten toetsen; dit is geen juridisch advies.
