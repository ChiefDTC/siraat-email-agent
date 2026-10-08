# 03 · Copyspec v5: direct response, urgentie en verhaallijn (59 mails)

Datum: 8 oktober 2026. Rol: direct-response-, urgentie- en verhaallijn-agent, fase 1. Alleen gelezen en geschreven in dit bestand: geen templates gewijzigd, niets naar Klaviyo of Shopify, niet gecommit.
Bronnen: `research/v5/00-feedback-floris.md` (leidend voor de richting), DECISIONS.md (bindend), `.claude/skills/siraat-direct-response/SKILL.md`, `.agents/product-marketing.md`, `research/copy/*` (vooral 06-offer-design §4), `research/survey/01-klantbegrip.md`, `research/onderwerpen/01-lab.md`, `research/history/01-beste-mails.md`, `research/inspiratie/01-concurrenten.md`, `research/build-v4/urgency-upgrade.md`, `content/facts/*`, en de topcomment plus tekst van alle 59 mails in `exports/manifest.csv` (de oude c4-us, c4-int en hun nocode-varianten staan nog in de map maar niet in de inventaris en zijn niet meegenomen).

Leeswijzer per mail: **Onderwerp** A en B (tekens tussen haken, zichtbaar, max 40) · **Preview** · **Hero** (LABEL / `Regel1|Regel2` / subline) · **Verhaalstap** (de ene stap uit de flowlijn) · **Urgentie** (en waarom waar) · **CTA** · **P.S.** · **Blokken** (weg / terug of nieuw). `{day}` = de bestaande Klaviyo-datummacro (`{{DATE:n:l, F j}}`), alleen in mails met een unieke code.

Markeringen: **[BESLISSING EIGENAAR]** = urgentie of aanbod wordt pas waar na een besluit van Floris. **[VRAAG]** = feit onzeker, eerst controleren.

---

## 0. Wat is echt? De urgentie-toets

Floris wil urgentie op wat de klant verliest. Hieronder per mechaniek of het waar is, en zo niet, hoe het waar te maken is.

| # | Mechaniek | Waar? | Bewijs | Hoe we het zeggen | Wat we niet zeggen |
| --- | --- | --- | --- | --- | --- |
| U1 | **Unieke code verloopt** (C4_10_48H, K3_10_48H, B2_10_48H, R2_10_72H, R2_VIP_15_72H, SK_REGULARS15_14D, SK_ANNIV10_7D, P3_THANKYOU_10_14D) | **Ja** | Shopify unique coupon, verloopt X uur na toewijzing (topcomments, DECISIONS 2026-10-07). Codemails gaan om 09:00 lokaal; de datumtag rekent in US/Eastern en toont dus nooit een latere dag dan de echte vervaldag, hooguit een dag eerder (AU/Azië). Marge: tot 24 uur in ons nadeel, nooit in dat van de klant. | "Your 10% expires on the morning of {day}." / "Already applied. After that it comes off your cart." / "Made for you, so it has an end date." | Uren in de tegels, "tonight", "midnight" |
| U2 | **Code verdwijnt uit de cart** | **Ja** | Na de vervaldag werkt de code niet meer; de knop met `&discount=CODE` past niets meer toe. | "Your 10% comes off this cart on {day}." / "Your cart link keeps working. Your 10% doesn't." | |
| U3 | **"We're removing your cart"** | **Nee** | Shopify bewaart de winkelwagen (cart-cookie, circa 14 dagen [VRAAG: in Shopify-cookiedocumentatie bevestigen]) en de abandoned-checkout-link blijft werken. Wij verwijderen niets. | Waar alternatief: "This is the last email about your cart." + U2. | "We're removing your cart", "your cart expires", "reserved", "held" |
| U4 | **4 gifts "pending"** | **Ja** | De gifts zitten als eigen artikelen in de cart: de cartflow-trigger sluit "Mystery Gift, E-Book, Free Shipping, Giveaway" uit (k1-topcomment), en `claims.csv` noemt de Shopify-giftproducten. Ze worden pas geleverd als de order geplaatst is. [VRAAG: één testcheckout maken om te zien dat de vier regels ook in de checkout staan.] | "Your cart is waiting, with 4 gifts still pending." / "They ship the moment you place the order." | |
| U5 | **Gifts lopen af** | **Nu niet** | DECISIONS 2026-10-07: gifts gelden voor elke order; einddatum oktober-actie onbekend. `claims.csv` registreert de gift-stack als "October 2026 campaign offer". | Tot er een datum is: "pending", nooit "expiring". | "Your gifts expire", "gifts run out" |
| U5b | Gifts lopen af, waar gemaakt | **[BESLISSING EIGENAAR]** | Optie 1: einddatum van de gift-stack vastleggen (bv. einde fall sale). Optie 2: mystery gift "while stock lasts" alleen met echte voorraadteller. | Met datum, in Klaviyo met `{% today %}`-vergelijking zodat de regel na de datum vanzelf verdwijnt: "The 4 gifts are part of our fall offer. It ends {einddatum}." | |
| U6 | **Fall sale (3+3, "buy 2 get 4 free", $299) loopt af** | **Onbekend** | Feedback Floris 8 okt: fall sale vanaf vandaag. Geen einddatum. Let op: DECISIONS zegt 6-delige set = $349; feedback zegt $299 voor de fall-set. **[BESLISSING EIGENAAR]**: welke prijs is live, welk product (handle) en tot wanneer. | Met datum: "Fall sale: pay for 2 pans, the Mini and 3 lids are free. Until {einddatum}." | Sale-einde zonder datum |
| U7 | **Wekelijkse filtertrekking** | **Nog niet als deadline** | facts.csv: wekelijks, 5 winnaars. Skill §6: geen deadline zonder officiële actievoorwaarden. | **[BESLISSING EIGENAAR]**: voorwaarden publiceren met sluitmoment (bv. zondag 23:59 ET). Daarna waar: "Order by Sunday to be in this week's filter draw." | "Last chance to win" |
| U8 | **Laatste mail van een reeks** | **Ja** | C4, K3, W5, S2 zijn de laatste stap van hun flow. | "This is the last email about your cart." | "Final notice" bij mails die niet de laatste zijn |
| U9 | **HI10 verloopt** | **Nee** | HI10 actief zonder einddatum (claims.csv). | Nooit een deadline. Welcome: "the last time we mention it in this series" (waar). | "Your 10% expires" bij HI10 |
| U10 | **Lage voorraad** | **Nee** | Geen voorraaddata in mails. | | "Selling fast", "only X left" |

Twee voorstellen om meer urgentie echt te maken, beide **[BESLISSING EIGENAAR]**:
1. **Einddatum voor fall sale en gift-stack** (U5b, U6). Grootste hefboom: geeft C1 t/m C3, K1, K2 en de setmails een echte "loopt af" zonder code.
2. **Unieke welkomstcode met 10 dagen looptijd** (besluit B uit 06-offer-design §6). Pas dan heeft W5 een echte "your 10% expires". Tot die tijd blijft HI10 zonder deadline.

Kortingstiming (Floris: "10% in K1, waarom niet pas na een dag?"): in deze spec staat HI10 niet meer in onderwerp, preview of hero van C1, K1, K2 en B2-notclicked. De auto-toegepaste HI10 in de C1 t/m C3-links blijft (DECISIONS 2026-10-08). Of HI10 helemaal uit K1 gaat is voor de kortingstiming-agent.

---

## 1. Verhaallijn per flow

De waar-gebeurde tijdlijn (alleen uit W2, goedgekeurd door Floris op 8 oktober, DECISIONS en claims.csv):

| Stap | Feit | Bron |
| --- | --- | --- |
| S1 | Twee jaar geleden begon Benjamin te lezen over PFAS, de "forever chemicals" in veel coated cookware. Het zat hem dwars hoe normaal ze waren geworden. | W2 |
| S2 | Eerst titanium snijplanken. Daarna de pan, "because in the end you cook in a pan". | W2 |
| S3 | Het idee: een titanium kookoppervlak, een hammered pattern zodat minder eten het metaal raakt, niets om af te slijten. RVS was makkelijker geweest, maar kookt niet zo. | W2 |
| S4 | Zes maanden testen voor het goed was. | W2 |
| S5 | Eerste orders 20 december 2024. De look-alikes kwamen daarna. | DECISIONS 2026-10-01 |
| S6 | Light Labs, ISO/IEC 17025, rapport 25895, 30 oktober 2025: 31 PFAS, allemaal onder de detectiegrens. Getest: Pan Pro; alle pannen hetzelfde oppervlak. | claims.csv, DECISIONS 2026-10-07 |
| S7 | 100,000+ happy customers, in iets meer dan een jaar. | DECISIONS, claims.csv |
| S8 | 75 jaar garantie, omdat er niets is dat kan afslijten. | DECISIONS, skill §2 |
| S9 | De eerlijke noot: koud metaal grijpt, heet metaal laat los. | skill §2 |
| S10 | Klanten: Tammy (vierde pan), Sunny (één pan, toen de set), James (dacht dat het oplichting was), Marilyn ("I only need the new one"), Scott (de laatste pannen). | reviews, letterlijk |

Regel: één stap per mail, één vergelijking per flow, en geen stap twee keer in dezelfde flow. [VRAAG] "Two years ago" (W2) plus zes maanden testen plus snijplanken vóór de pan betekent dat het lezen uiterlijk begin 2024 begon; als dat eerder was, overal "a little over two years ago".

| Flow | Lijn (één zin) | Mail 1 | Mail 2 | Mail 3 | Mail 4 | Vergelijking (één per flow) |
| --- | --- | --- | --- | --- | --- | --- |
| **Checkout** | Je stond bij de laatste stap; waarom deze pan bestaat; wat 100,000+ mensen deden; wat je beschermt, en je code verloopt. | C1: bezit. Cart + 4 gifts pending, één regel "your next pan vs your coated one" | C2: S1 + S6. Benjamin las over PFAS, dus liet hij testen. C2-acc: S2 (wij begonnen ook met een accessoire) | C3-p: S7 (100,000+, de meesten beginnen met één, Sunny). C3-s: S4 (zes maanden testen, elk stuk hetzelfde oppervlak). C3-acc: S2 (van plank naar pan) | C4: S8 + U1/U2 (twee beloftes, je 10% verloopt) | Coated non-stick, alleen in C1 |
| **Cart** | Hoe hij werkt; wat hij echt kost; wat je beschermt, en je code gaat eraf. | K1: S3, hammered pattern, easy wipe. K1-acc: S2 | K2-new: S8, 15 pannen of één. K2-returning: S10 (Tammy) | K3: twee beloftes + U1/U2 | | RVS (schrobben), alleen in K1. K2 houdt de som, zonder tabel |
| **Browse** | Waarom Benjamin begon; wat het origineel is; wat sceptici ervan vonden. | B1: S1, "get this pan with 10%". B1-acc: S2 | B2-clicked: S5 + S7, je eigen code verloopt. B2-clicked-nocode: S7. B2-notclicked: S10 (sceptici) | | | Gietijzer (Tammy: lichter), alleen in B2-notclicked |
| **Site** | Welke maat; waar 100,000+ mensen begonnen. | A1: maat (tel je eieren) | A2: S5 + S7 (sinds 20 december 2024) | | | Geen |
| **Welcome** | Het idee; Benjamins verhaal; bewijs voor de scepticus; jouw maat; drie klanten en twee beloftes. | W1: S6 (no PFAS, here's the paper) | W2: S1 t/m S5 (blijft) | W3: S6 + S8, "skeptical first": zes bewijzen | W4: maatkeuze (commitment). W5: S10 + twee beloftes | Coated non-stick in W1 (één zin); andere titaniummerken in W3 (de drie vragen) |
| **Post-purchase** | Je koos goed; de eerste kook; wat eigenaren erbij nemen. | P1: bevestig de keuze (no PFAS), S9 als tip | P2: S9 in vijf stappen | P3: S10, wat eigenaren als tweede kopen, code 14 dagen | | Geen |
| **VIP** | Twee orders = VIP, 15% exclusief; daarna Benjamins vraag. | V1: VIP, 15% | V2: wat maken we hierna | | | Geen |
| **Winback** | Hoe gaat het met je pan; pan nummer twee, code verloopt. | R1: check-in + wat eigenaren toevoegen | R2: eigen code 72 uur, VIP 15% exclusive | | | Coated non-stick alleen in R1-acc (zij hebben nog geen pan) |
| **Anniversary** | Zes maanden: niets afgesleten; een jaar: 15%. | N1: S8 als bewijs uit hun eigen keuken | N2: één jaar, 15% voor 7 dagen | | | Geen |
| **Sunset, UGC** | Ongewijzigd van lijn; zie mails. | | | | | |

---

## 2. Herhalingen die nu in de mails zitten

Geteld in de huidige tekst van de 59 mails. Wie in één week checkout, cart en browse krijgt, ziet dit allemaal meerdere keren.

| # | Herhaling | Waar nu | Voorstel |
| --- | --- | --- | --- |
| 1 | Gifts-grid "$70 in gifts, included / in the box" | ~45 mails, vaak naast codebalk "$70 IN GIFTS" én de cartregel "your $70 in gifts are still attached" (3x per mail) | Eén keer per mail, als gift-iconen (Floris' free-shipping-icoon) direct onder cart of product. INT: "4 gifts", nooit "$70" |
| 2 | Friction reducer "Free shipping. 30-day returns. 100,000+ happy customers." | Onder elke knop, 3 tot 4x per mail | Alleen onder de eerste en laatste knop |
| 3 | "Every pan says non-toxic. Few can show you the paper." | C2, W1, W3 (W1 en W3 in dezelfde week) | Alleen C2. W1 en W3 krijgen een eigen opener |
| 4 | De drie vragen (rapport, nummer, 75 jaar) | C2 en W3 identiek | Alleen W3 (welcome); C2 vertelt het als Benjamins reden |
| 5 | Vergelijkingstabel coated non-stick | K2-new en A2 identiek; B1 tegen RVS | Tabellen weg uit A2 en B1; zie vergelijking per flow in §1 |
| 6 | "Cold metal grabs your food, hot metal lets it go" | W0, P1-first, P2, P2-safe, U1 (P1, P2 en U1 binnen 3 weken) | Alleen P2/P2-safe; P1 één zin "heat first", U1 verwijst naar P2 |
| 7 | "Heat it on medium 2 to 3 minutes... Skip the heat, and it sticks." | W1 en W2 (opeenvolgend), P1, K2-returning, P3-next, P3-set | W2 houdt hem; uit W1 |
| 8 | "Nothing on it to wear off" | W0, W1, W2, C3-acc, K1, K2-new, N2, A1, P3-accessory | Max één keer per flow; Floris vraagt directer: "no coating, so nothing to wear off" alleen waar S8 de verhaalstap is |
| 9 | Tammy "I am on my 4th pan" | 16 mails (C3-acc, B2-notclicked, K2-returning, W4-us, W4-int, W5, A2, P1-repeat, P3-apron, V1, V1-nocode, R1-acc, R2, R2-nocode, R2-vip, N2) | Alleen K2-returning, W5, R2-vip, B2-notclicked (gietijzer). V1 en R2-vip gaan naar dezelfde mensen: in V1 een andere review |
| 10 | James "another scam" | C2, W3, B2-clicked, B2-clicked-nocode, B2-notclicked | Alleen W3 en B2-notclicked |
| 11 | Sunny C. "ordered one pan to try it out" | C3-p, B2-clicked (body + B-onderwerp), B2-clicked-nocode (A-onderwerp), B2-notclicked, P3-accessory | C3-p, B2-clicked-nocode en P3-accessory; uit B2-clicked en B2-notclicked |
| 12 | Marilyn B. "I only need the new one" | W1, A2, B2-notclicked, P1-first, P3-accessory | W1 en P1-first |
| 13 | "Two promises" met Steven T. en Brandon W. | C4, C4-nocode, K3, K3-nocode, R2, R2-nocode, R2-vip, R2-vip-nocode | Blijft in C4/K3 (laatste mail); in R2 alleen de korte regel zonder reviews |
| 14 | "HERE IS YOUR 10%" + "Last chance for your code" | C4 en K3 identiek | Eigen koppen, zie mails |
| 15 | "If one pan is always busy" | R2, R2-nocode, C3-p, P3-next | Alleen R2 |
| 16 | "Here is what owners add next" | R1-pan, P3-next, N1 | P3 en R1 houden het, N1 krijgt een eigen invalshoek |
| 17 | "Most kitchens start with the pan" | C3-acc, R1-acc, P3-accessory, A2 | C3-acc en P3-accessory krijgen S2 (van plank naar pan) |
| 18 | Closerlook met dezelfde vier labels | K1, P3-accessory, R1-acc | Alleen K1 (daar is het de verhaalstap) |
| 19 | "Your Card Game entry is in" | W0, W1 (preview + body) | Eén regel in W1, niet in de preview |
| 20 | "15 pans, or one" | K2-new, C3-p | Alleen K2-new |
| 21 | Report 25895 als hero-idee | W1, W3, C2, B1, K1 (5 hero's) | Hero-idee alleen in W1 (wat) en W3 (bewijs) en C2; elders als bewijsregel |
| 22 | "Reply and our team will help" | ~50 mails | Varieer; max 3 per flow (skill §9) |
| 23 | Onderwerpen "One pan, or three?" | C3-p én A2-B (en hero A2) | A2 krijgt eigen onderwerp en hero |
| 24 | "Thank you for a year of cooking with us" | N2 twee keer in één mail | Eén keer |

---

## 3. Checkout (C1 tot C4)

### C1 · 30 min na Checkout Started
- **Onderwerp:** A "Your cart + 4 gifts are still pending" (37) · B "We kept your cart (and 4 gifts)" (31). A/B: verlies (pending) tegen bezit (kept, historische winnaar "We kept these safe").
- **Preview:** "They ship the moment you place the order. One tap left."
- **Hero:** STILL PENDING / `Your cart,|plus 4 gifts` / "Saved at the last step. One tap left."
- **Verhaalstap:** bezit. Opener: "You got to the last step. Your cart is saved, and four gifts are attached to it: free shipping, the e-book, a mystery gift and a chance to win a PFAS water filter. They ship the moment you place the order." Daarna één directe regel (Floris): "Your next pan, next to your coated one: no coating to wear off, and no PFAS. Light Labs, report no. 25895."
- **Urgentie:** gifts pending (U4, waar). Geen vervaldatum (U5). Met fall-sale-datum: "Fall sale prices until {einddatum}" **[BESLISSING EIGENAAR]**. HI10 niet vooraan (Floris): alleen één regel onder de cart, "Your extra 10% is already applied."
- **CTA:** "Complete my order"
- **P.S.:** "Cooking for 2 to 4? The 11-inch is the one most people pick. Between two sizes, reply and we'll tell you."
- **Blokken:** weg: aanbodbalk "Extra 10% off with code HI10" in de hero-afbeelding, HI10-codebalk (wordt "4 GIFTS PENDING · FREE SHIPPING"), goes-blok (cross-sell in mail 1 leidt af), tweede en derde friction reducer. Terug/nieuw: gift-iconen direct onder de cart, reviewrij met de drie pijlers (kwaliteit, levering, service; reviews-agent).

### C2 · dag 1, kookgerei, nieuwe klanten
- **Onderwerp:** A "Has the pan in your cart been tested?" (37) · B "Why I had our pan lab-tested" (28). A/B: autoriteit tegen oprichter.
- **Preview:** "Two years ago I started reading about PFAS. Report no. 25895 is the answer."
- **Hero:** blijft (Floris: goed): TESTED, NOT CLAIMED / `Non-toxic is|easy to say` / "Here's the paper: report no. 25895"
- **Verhaalstap:** S1 + S6. "Two years ago I started reading about PFAS, the forever chemicals in a lot of coated cookware. When we made the pan, I didn't want you to take my word for it. So we sent it to Light Labs." Daarna het rapport: 31 PFAS, allemaal onder de detectiegrens, ISO/IEC 17025, 30 oktober 2025. Geen drie-vragen-blok meer (zit in W3).
- **Urgentie:** cartregel "your 4 gifts are still pending on this cart" (U4). Geen deadline.
- **CTA:** "Complete my order"
- **P.S.:** "Want the full report as a PDF? Reply and we'll send it. Your 4 gifts are still pending on this cart."
- **Blokken:** weg: drie-vragen-blok, gifts-grid (cartregel en iconen volstaan), James (zit in W3 en B2-notclicked). Terug: één review met dezelfde reden (Gwen "peace of mind") + één service/levering-review.

### C2-acc · dag 1, accessoire
- **Onderwerp:** A "Yours, or a gift? Both work." (28) · B "Your 4 gifts are still pending" (30).
- **Preview:** "Free shipping, 30 days to return it unused, and 4 gifts that ship with it."
- **Hero:** blijft: STILL IN YOUR CART / `Yours, or a gift?|Both work.` / subline zonder HI10: "4 gifts ship with it, either way."
- **Verhaalstap:** S2, kort: "Siraat started with a titanium cutting board, before there was a pan. The small things get the same care." (per accessoire tailored door de tailoring-agent).
- **Urgentie:** gifts pending (U4).
- **CTA:** "Complete my order"
- **P.S.:** "Not sure about a size or color? Reply with who it's for."
- **Blokken:** weg: dubbele iconenrij (FREE SHIPPING / 30-DAY RETURNS staat ook in de friction reducer), "10% off with HI10" uit de preview. Terug: gift-iconen onder de cart.

### C3-p · dag 3, één Pan Pro in de cart
- **Onderwerp:** A "One pan, or three?" (18) · B "\"I ordered one pan to try it out\"" (33).
- **Preview:** "Most of our 100,000+ customers start with one. Here's when three makes sense."
- **Hero:** THE MATH / `One pan,|or three?` / met fall-set: "Pay for 2 pans. The Mini and 3 lids are free." Zonder bevestiging: "Three pans, three lids, about $116 a pan."
- **Verhaalstap:** S7. "In a little over a year, 100,000+ people have cooked on our pans. Most started with one. Many came back for the rest." Sunny C. als bewijs.
- **Urgentie:** fall sale tot {einddatum} **[BESLISSING EIGENAAR]** (U6; ook: $299 of $349, en welke handle). Zonder datum: geen deadline, alleen gifts pending.
- **CTA:** "Upgrade to the 6-piece set" · tweede link "Keep my one pan and check out"
- **P.S.:** "Cooking for 2 to 4? Then one 11-inch pan is the right call, and your cart stays exactly as it is."
- **Blokken:** weg: de "15 pans"-som (alleen K2-new), M. A.-review. Blijft: value stack (met fall-prijs als bevestigd). INT: geen dollars, "about X a pan" alleen in lokale valuta (valuta-agent).

### C3-s · dag 3, set in de cart
- **Onderwerp:** A "What's in the box with your set" (31) · B "\"I've replaced all the pans...\"" (31).
- **Preview:** "Every piece, the same tested titanium surface. Plus 4 gifts pending."
- **Hero:** WHAT'S IN THE BOX / `Every pan,|one decision` / "One 75-year warranty for every piece."
- **Verhaalstap:** S4. "We tested the pan for six months before the first one shipped. Every piece in your set has that same titanium cooking surface." Daarna "what's in the box" per bundel (C3-S routeert op product, bundel-agent).
- **Urgentie:** gifts pending; bij de fall-set de echte einddatum **[BESLISSING EIGENAAR]**.
- **CTA:** "Complete my order"
- **P.S.:** "Not sure which pieces you need? Reply with what you cook in a normal week."
- **Blokken:** weg: generieke features-fallback (wordt per bundel een eigen box-blok), HI10 uit de hero-subline. Terug: gift-iconen.

### C3-acc · dag 3, accessoire, nieuwe klanten
- **Onderwerp:** A "The pan we made after the board" (31) · B "Still cooking on a coated pan?" (30).
- **Preview:** "We started with cutting boards too. Then the pan, because you cook in a pan."
- **Hero:** WHERE WE STARTED / `From the board|to the pan` / "No coating. Covered for 75 years."
- **Verhaalstap:** S2, als Benjamin: "We started with titanium cutting boards. Then we made the pan. A board is nice, but in the end you cook in a pan." Geen coated-vergelijking (zit in C1).
- **Urgentie:** cart en gifts pending. Geen deadline.
- **CTA:** "Complete my order" · productkaart "Add the Pan Pro"
- **P.S.:** "Happy with what's in your cart? Then that's all you need."
- **Blokken:** weg: Tammy (zie herhaling 9), tweede iconenrij. Blijft: productkaart Pan Pro (US met prijs, INT zonder).

### C4 · dag 5, unieke code 48 uur (T02-A)
- **Onderwerp:** A "Your 10% expires in 48 hours" (28) · B "Last email: your 10% and 4 gifts" (32).
- **Preview:** "Already applied to your cart. On {day} morning it comes off."
- **Hero:** EXPIRES IN 48 HOURS / `Your 10%|runs out` / "Already on your cart. Then it's gone."
- **Verhaalstap:** S8, afsluiting: "No coating, so nothing to wear off. That's why we can cover it for 75 years." Dan de twee beloftes.
- **Urgentie:** C4_10_48H verloopt 48 uur na toewijzing (U1, waar), code gaat van de cart af (U2, waar), laatste mail (U8, waar), gifts pending (U4). Codebalk: "YOUR 10% EXPIRES {DAG} {DATUM}". Niet: "we're removing your cart" (U3).
- **CTA:** "Use my 10% now"
- **P.S.:** "Your 10% expires on the morning of {day}. After that it comes off this cart, the regular sale price applies, and this was our last email about it."
- **Blokken:** weg: offer-kop "Last chance for your code" (zelfde als K3) wordt "Your 10% runs out {day}"; tweede gifts-grid. Blijft: twee beloftes met Steven T. en Brandon W., deadline-tegels. INT: "Duties paid" blijft.

### C4-nocode · dag 5, geen code (T02-B of cooldown)
- **Onderwerp:** A "Last email about your cart" (26) · B "\"They honored the warranty\"" (27).
- **Preview:** "4 gifts still pending, two promises, and then we stop reminding you."
- **Hero:** LAST EMAIL / `Still yours,|if you want it` / "4 gifts pending. 30 days to change your mind."
- **Verhaalstap:** S8 (zoals C4), zonder code.
- **Urgentie:** laatste mail (U8), gifts pending (U4). Met fall-datum: einde sale **[BESLISSING EIGENAAR]**.
- **CTA:** "Complete my order"
- **P.S.:** vervangt "there is no rush on our side" (haalt alle urgentie weg): "This is our last reminder. Your cart link keeps working, but we won't bring it up again."
- **Blokken:** weg: 12-delige-setkaart (laatste mail, één keuze). Blijft: twee beloftes.

---

## 4. Cart (K1 tot K3)

### K1 · 30 min na Added to Cart, kookgerei
- **Onderwerp:** A "The hammered pattern: an easy wipe" (34) · B "We saved your cart (and 4 gifts)" (32). A/B: mechanisme tegen bezit (historische cart-1-winnaar).
- **Preview:** "Less food touches the metal, so cleanup is a quick wipe. Your cart is saved."
- **Hero:** STILL IN YOUR CART / `Hammered for|an easy wipe` / "Less food touches the metal. No coating."
- **Verhaalstap:** S3, direct (Floris: "easy wipe met het hammered pattern"): "The hammered pattern is the point. Less food touches the metal, so it lets go, and cleanup is a quick wipe with a soft sponge. No coating, so no PFAS and nothing to peel off. Dishwasher? That works too." Vergelijking RVS (één zin): "Stainless steel often needs a soak. This needs a sponge." (bron: B1-tabel, Thomas H. "cleanup in 30 seconds").
- **Urgentie:** gifts pending (U4). Geen 10% in onderwerp, preview of hero (kortingstiming-agent beslist over HI10 in de body).
- **CTA:** "Finish my order"
- **P.S.:** "A rainbow tint can show up over time. That's heat patina, normal on titanium, and baking soda lifts it."
- **Blokken:** weg: aanbodbalk HI10 in de hero, gifts-grid (wordt iconen). Blijft: closerlook (hier is hij de verhaalstap), Graham C. Nieuw: één bezorg-review (pijler snelheid).

### K1-acc · 30 min, accessoire
- **Onderwerp:** A "Picked it out? It's still here." (31) · B "Your cart + 4 gifts, saved" (26).
- **Preview:** "What it's made of, in two lines. 4 gifts are pending with it."
- **Hero:** blijft: STILL IN YOUR CART / `Picked it out?|It is still here.` / subline zonder HI10: "4 gifts ship with it."
- **Verhaalstap:** S2 kort ("We started with a titanium board, before the pan."), daarna het about-blok per accessoire.
- **Urgentie:** gifts pending.
- **CTA:** "Finish my order"
- **P.S.:** "Buying it as a gift? Reply with who it's for."
- **Blokken:** weg: HI10 uit preview en codebalk, dubbele iconenrij.

### K2-new · dag 1, nieuwe klant
- **Onderwerp:** A "15 coated pans, or one" (22) · B "The pan you keep replacing" (26).
- **Preview:** "Say a coated pan lasts 5 years. Our warranty runs 75. Here's the math."
- **Hero:** THE REAL PRICE / `15 coated pans,|or one` / "Covered for 75 years. Nothing to wear off."
- **Verhaalstap:** S8. De som blijft; de vergelijking is hier de som zelf, dus de coated-tabel gaat eruit.
- **Urgentie:** gifts pending. Geen deadline. US: termijnregel blijft (akkoord Floris: alleen profielland US).
- **CTA:** "Finish my order"
- **P.S.:** US: "Prefer to pay over time? Shop Pay Installments and Affirm are at checkout." INT: "Free shipping, duties paid."
- **Blokken:** weg: vergelijkingstabel coated non-stick (herhaling 5), HI10 uit preview. Blijft: Scott Y.

### K2-returning · dag 1, bestaande klant
- **Onderwerp:** A "Adding to your Siraat kitchen?" (30) · B "Same pan, same 4 gifts, saved" (29).
- **Preview:** "You know how it works. Your cart is saved, with 4 gifts pending."
- **Hero:** blijft: WELCOME BACK / `You know|this pan` / "Same titanium, same 4 gifts."
- **Verhaalstap:** S10 (Tammy, vierde pan). Tailoring: niet de deksel of pan aanbieden die ze al hebben (tailoring-agent).
- **Urgentie:** gifts pending.
- **CTA:** "Finish my order"
- **P.S.:** "Which pan do you reach for most? Reply and tell me. It shapes what we make next."
- **Blokken:** weg: "medium heat, the water test" (kennen ze), tweede gifts-grid.

### K3 · laatste cartmail, unieke code 48 uur
- **Onderwerp:** A "Your cart's 10% ends in 48 hours" (32) · B "Last email: your cart and 10%" (29).
- **Preview:** "Already applied. On {day} morning the code comes off your cart."
- **Hero:** LAST EMAIL · 48 HOURS / `Your 10% comes|off on {dag}` is dynamisch, dus in het beeld statisch: `Your 10%|comes off soon` / "Already applied. Then it's gone."
- **Verhaalstap:** de twee beloftes (wat je beschermt), zonder S8 te herhalen als C4 al kwam.
- **Urgentie:** K3_10_48H (U1), code gaat van de cart af (U2), laatste mail (U8). Floris' "we're removing your cart and your discount": de korting klopt, de cart niet (U3). Eerlijke vorm: "We're taking your 10% off this cart on {day}." **[BESLISSING EIGENAAR]** akkoord op deze formulering in plaats van "removing your cart".
- **CTA:** "Use my 10% now"
- **P.S.:** "On the morning of {day} your code comes off this cart and the regular sale price applies. Your cart link keeps working. Your 10% doesn't."
- **Blokken:** weg: offer-kop "Last chance for your code" (zelfde als C4) wordt "Your 10% comes off {day}". Blijft: twee beloftes, tegels.

### K3-nocode · laatste cartmail, geen code
- **Onderwerp:** A "What if it's not for you?" (25) · B "Last email about your cart" (26).
- **Preview:** "Then it goes back unused within 30 days. Your 4 gifts are still pending."
- **Hero:** blijft: LAST EMAIL / `What if it's|not for you?` / "30 days to change your mind."
- **Verhaalstap:** twee beloftes.
- **Urgentie:** laatste mail (U8), gifts pending.
- **CTA:** "Finish my order"
- **P.S.:** "This is our last reminder about this cart. After this, it's yours to come back to."
- **Blokken:** weg: tweede gifts-grid, tweede iconenrij.

---

## 5. Browse (B1, B2)

### B1 · 1 uur na Viewed Product, kookgerei
- **Onderwerp:** A "Get this pan with 10% off" (25) · B "Why I started making this pan" (29). A/B: aanbod (Floris) tegen oprichter. Vervangt T05a (autoriteit tegen social proof) **[BESLISSING EIGENAAR]** of T05a blijft en dit wordt fase 2.
- **Preview:** "Two years ago I read about PFAS. This pan is what came out of it."
- **Hero:** THE PAN YOU VIEWED / `This pan,|10% off` / "No PFAS. Light Labs report no. 25895."
- **Verhaalstap:** S1, in Benjamins stem (3 zinnen): "Two years ago I started reading about PFAS. It bothered me how normal they had become in our pans. So we made one with nothing on it: a pure titanium cooking surface, no coatings." Dan CTA.
- **Urgentie:** geen deadline (HI10, U9). Wel: "HI10 works on top of the sale."
- **CTA:** "Get 10% off this pan"
- **P.S.:** "Works on induction, gas, electric and ceramic. Not sure about your stove? Reply."
- **Blokken:** weg: vergelijkingstabel tegen RVS (Floris: variatie; RVS zit nu in K1), tweede reviewpaar. Nieuw: korte Benjamin-noot met handtekening, onder het productblok.

### B1-acc · 1 uur, accessoire
- **Onderwerp:** A "Looked twice? Here's the detail." (32) · B "10% off the piece you looked at" (31).
- **Preview:** "What it's made of, in two lines. And how Siraat started."
- **Hero:** blijft: YOU HAD A LOOK / `Looked twice?|Here is the detail.`
- **Verhaalstap:** S2: "We started with titanium cutting boards, before we made a single pan."
- **Urgentie:** geen.
- **CTA:** "Get 10% off this piece"
- **P.S.:** "Buying for someone else? Reply with who it's for."
- **Blokken:** weg: dubbele iconenrij.

### B2-clicked · 2 dagen na B1, klikte, unieke code 48 uur
- **Onderwerp:** A "Your own 10% runs out in 48 hours" (33) · B "A code for the pan you went back to" (35).
- **Preview:** "Already applied to the pan you looked at. Gone on {day} morning."
- **Hero:** YOUR CODE · 48 HOURS / `Your own 10%|runs out soon` / "Then the regular sale price is back."
- **Verhaalstap:** S5 + S7: "We shipped the first one on December 20, 2024. A little over a year later, 100,000+ people cook on them."
- **Urgentie:** B2_10_48H (U1, waar). Codebalk met datum, tegels, P.S.
- **CTA:** "Use my 10% now"
- **P.S.:** "Your code expires on the morning of {day}. After that, the regular sale price applies."
- **Blokken:** weg: Sunny en James (herhaling 10, 11); in plaats daarvan één kwaliteit- en één leveringsreview. INT (AU, HK): geen dollars in stack en productblok (valuta-agent).

### B2-clicked-nocode · zelfde plek, geen code
- **Onderwerp:** A "\"I ordered one pan to try it out\"" (33) · B "100,000+ people started with one" (32).
- **Preview:** "Sunny C. started with one. Your order comes with 4 gifts too."
- **Hero:** blijft: IN THEIR WORDS / Sunny C.
- **Verhaalstap:** S7 via Sunny.
- **Urgentie:** geen (eerlijk).
- **CTA:** "Get my pan + 4 gifts"
- **P.S.:** "A question before you decide? Reply."
- **Blokken:** weg: James (herhaling 10).

### B2-notclicked · 2 dagen na B1, niet geklikt
- **Onderwerp:** A "Skeptical? So were they." (24) · B "Week one, in their words" (24).
- **Preview:** "One thought it was a scam. One is on her fourth pan."
- **Hero:** IN THEIR WORDS / `Skeptical?|So were they.` / "From the first doubt to the fourth pan."
- **Verhaalstap:** S10, twee kaarten in plaats van vier: James (de twijfel) en Tammy (gietijzer: "so much lighter than my old cast iron pans", de vergelijking van deze flow).
- **Urgentie:** geen. HI10 uit de preview.
- **CTA:** "Get 10% off this pan"
- **P.S.:** "Still deciding? Reply with what you cook most."
- **Blokken:** weg: Marilyn en Sunny (herhaling 11, 12), tweede gifts-CTA.

---

## 6. Site (A1, A2)

### A1 · 2 uur na Active on Site
- **Onderwerp:** A "Four eggs or five?" (18) · B "Not sure which pan? Start here." (31). (Vraag als A: onderwerplab +57% klik.)
- **Preview:** "Four sizes, one titanium surface. Pick yours in 30 seconds."
- **Hero:** blijft: WHICH SIZE? / `Four eggs|or five?`
- **Verhaalstap:** de maatregel (tel je eieren). Maten in cm buiten de US (maten-agent).
- **Urgentie:** geen.
- **CTA:** "Get 10% off my pan"
- **P.S.:** "Between two sizes? Reply with what you cook and for how many."
- **Blokken:** weg: "no coating to wear off" (herhaling 8). Blijft: maattabel.

### A2 · dag 2
- **Onderwerp:** A "Where 100,000+ customers started" (32) · B "December 20, 2024" (17).
- **Preview:** "The first pan shipped on December 20, 2024. Most people still start there."
- **Hero:** SINCE DECEMBER 20, 2024 / `100,000+ kitchens|started here` / "Most with the 11-inch pan."
- **Verhaalstap:** S5 + S7.
- **Urgentie:** geen.
- **CTA:** "Claim my 10% + gifts"
- **P.S.:** "Not sure yet? Reply with what you cook in a normal week."
- **Blokken:** weg: vergelijkingstabel coated (herhaling 5), "One pan, or three?"-hero (herhaling 23), Tammy.

---

## 7. Welcome (W0 tot W5)

### W0 · bestaande klant meldt zich aan
- **Onderwerp:** A "Thank you. Now the first egg." (29) · B "2 to 3 minutes on medium. Then the egg." (39).
- **Preview:** "Cold metal grabs your food, hot metal lets it go."
- **Hero:** blijft.
- **Verhaalstap:** S9. (Klant, geen verkoop.)
- **Urgentie:** geen.
- **CTA:** "Watch the cook guide"
- **P.S.:** "Simmering or steaming? The lid for your pan size is $59 (US)."
- **Blokken:** weg: "nothing on it to wear off" in de opener.

### W1-A · direct na aanmelding, HI10 als code (T04-A)
- **Onderwerp:** A "No PFAS. Here's the paper. And 10%." (35) · B "Your 10% is inside (plus 4 gifts)" (33). (Huidige A is 43 tekens.)
- **Preview:** "Light Labs report no. 25895. HI10 takes 10% off the sale price."
- **Hero:** THE IDEA / `No PFAS.|Here's the paper.` / "Report no. 25895, read it yourself."
- **Verhaalstap:** S6 (het wat). Eigen opener in plaats van "Every pan says non-toxic": "Plenty of pans say non-toxic. Ours went to a lab: 31 PFAS compounds tested, every one below the detection limit." Coated non-stick in één zin: "A coated pan is made to slide until the coating wears. Ours has no coating to wear." De oorsprong (20 december 2024) en "Skip the heat" gaan naar W2.
- **Urgentie:** geen (HI10, U9). Card Game-regel één keer in de body.
- **CTA:** "Claim my 10% + gifts"
- **P.S.:** "Tomorrow: why I started making this pan."
- **Blokken:** weg: Card Game uit de preview, Scott Y. (blijft in K2-new). Blijft: offer, gifts, Marilyn B.

### W1-B · idem, HI10 als welcome gift card (T04-B)
- Gelijk aan W1-A (zelfde onderwerp, preview, hero, verhaal, P.S.); alleen de offerkaart verschilt (T04). CTA "Claim my 10% + gifts".

### W2 · dag 1, Benjamin (tekst)
- **Onderwerp:** A "The pan nobody else was making" (30) · B "A note from Benjamin" (20) (historie: welcome-tekstmail "A Note from Benjamin" won).
- **Preview:** "It's Benjamin. I wanted to write to you myself. (Your 10% is in the P.S.)"
- **Hero:** geen (tekstmail).
- **Verhaalstap:** S1 tot S5, blijft zoals Floris het goedkeurde.
- **Urgentie:** geen.
- **CTA:** "Claim my 10% + gifts"
- **P.S.:** blijft.
- **Blokken:** ongewijzigd. Eventueel de laatste alinea (rapport) inkorten tot één zin, want W3 is de bewijsmail.

### W3 · dag 3, "skeptical first": veel meer zekerheid
- **Onderwerp:** A "Has your cookware been tested?" (30) · B "Skeptical? Good. Here's the proof." (34).
- **Preview:** "Six things you can check yourself, before you spend a dollar."
- **Hero:** SKEPTICAL FIRST / `Don't take|our word for it` / "Report no. 25895. Read it yourself."
- **Verhaalstap:** S6 + S8, als bewijsladder (Floris: veel meer zekerheid). Zes regels, elk met iets om zelf te controleren: (1) a lab report: Light Labs, ISO/IEC 17025; (2) a report number: no. 25895, October 30, 2025, link; (3) 31 PFAS tested, every one below the detection limit; (4) a warranty that outlasts you: 75 years, because there is no coating to wear off; (5) 30 days to send it back unused; (6) 100,000+ happy customers since December 20, 2024. Daarna James: "I honestly thought this might be another scam. But it's real titanium." Andere titaniummerken: "Ask any titanium brand these questions. Us included."
- **Urgentie:** geen.
- **CTA:** "Claim my 10% + gifts" · tekstlink "Read the report first"
- **P.S.:** "Want the full report as a PDF? Reply and we'll send it."
- **Blokken:** weg: opener "Every pan says non-toxic" (herhaling 3). Nieuw: bewijsladder (zes regels met vinkjes, een linkt naar het rapport). Blijft: certificaatbeeld (T07 test later pan-in-gebruik).

### W4-US · dag 6, US
- **Onderwerp:** A "Who are you cooking for?" (24) · B "Count your eggs, pick your pan" (30).
- **Preview:** "One, two, or a family? Pick your pan by that. Your 10% is already off."
- **Hero:** blijft: WHICH SIZE? / `Who are you|cooking for?`
- **Verhaalstap:** commitment: de maatkeuze. Met fall-set (indien bevestigd) als middelste tier.
- **Urgentie:** geen; met fall-datum: "Fall sale until {einddatum}" alleen bij de fall-set **[BESLISSING EIGENAAR]**.
- **CTA:** "Claim my 10% + gifts"
- **P.S.:** "Still not sure? Reply with what you cook most and who for."
- **Blokken:** weg: Tammy (herhaling 9). Blijft: Emma ("pass down to my son").

### W4-INT · dag 6, buiten de US
- Zoals W4-US. Preview: "One, two, or a family? Pick your pan by that. Free shipping, duties paid." Geen dollars, geen 12-delige set, maten in cm eerst (maten-agent). "4 gifts", niet "$70".

### W5 · dag 10, laatste welcome
- **Onderwerp:** A "Tammy is on her fourth pan" (26) · B "The last note about your 10%" (28).
- **Preview:** "Three customers, two promises, and the last time we mention HI10."
- **Hero:** SKEPTICAL FIRST / `Then the egg.|Then the fourth pan.` / "Three customers, in their own words."
- **Verhaalstap:** S10 + de twee beloftes. Zekerheid (Floris): na de drie verhalen het volledige "Two promises"-blok (nu staat het alleen klein onderaan).
- **Urgentie:** laatste welcome-mail (U8, waar). HI10 zonder deadline (U9). Met besluit B (unieke 10-dagencode) wordt dit: "Your welcome 10% expires {day}" **[BESLISSING EIGENAAR]**.
- **CTA:** "Claim my 10% + gifts"
- **P.S.:** "This is the last welcome email. HI10 keeps working, but we won't bring it up again."
- **Blokken:** nieuw: twee beloftes als blok met Steven T. Blijft: Michael G., Fran G., Tammy. Weg: tweede gifts-grid.

---

## 8. Post-purchase (P1 tot P3)

### P1-first · 1 uur na eerste order
- **Onderwerp:** A "Good call. Here's what's coming." (32) · B "The first egg will tell you" (27).
- **Preview:** "Order confirmed. Your 4 gifts, your e-book and the one tip that matters."
- **Hero:** blijft.
- **Verhaalstap:** bevestig de keuze in hun woorden (S6): "You chose no PFAS and nothing to peel off." S9 als één zin ("heat first"), de rest in P2.
- **Urgentie:** geen (servicemail).
- **CTA:** "Download your e-book"
- **P.S.:** "If something sticks in your first week, reply before you give up on it."
- **Blokken:** weg: "Cold metal grabs..." (herhaling 6). Cross-sell: niet in P1 (cross-sell-agent, P3).

### P1-repeat · 1 uur na herhaalorder
- **Onderwerp:** A "Good to see you again" (21) · B "Round two. Here's what's coming." (32).
- **Preview:** "Your order is in. Same careful packing, same 4 gifts."
- **Hero/verhaal:** blijft. Tammy eruit (herhaling 9), Don J. blijft.
- **Urgentie:** geen. **CTA:** "Read the care guide". **P.S.:** "New size in this order? Reply and we'll tell you which lid fits."

### P2-safe · 16 dagen na order (geen leverdata)
- **Onderwerp:** A "When your pan arrives: the first egg" (36) · B "Is your pan on the stove yet?" (29).
- **Preview:** "Heat first, then oil, then the egg. Keep this for your first cook."
- **Hero/verhaal:** blijft; S9 is hier de stap. Steak als tweede kook toevoegen (zoals P2).
- **Urgentie:** geen. **CTA:** "Watch the chef video". **P.S.:** "Made your first egg? Send us a photo."

### P2 · 1 dag na levering
- **Onderwerp:** A "The mistake that makes titanium stick" (37) · B "Can you do an egg? Then anything." (33). (Historie: "The #1 mistake that makes titanium stick" 6,9% klik; daarom als A.)
- **Preview:** "Medium on titanium works like high on a normal pan. The chef's five steps."
- **Hero/verhaal:** blijft (S9).
- **Urgentie:** geen. **CTA:** "Watch the chef video". **P.S.:** "After the egg, a steak. Heat the pan first, then let it release on its own."
- **Blokken:** ongewijzigd (Floris: goed).

### P3-pan · dag 20, pan gekocht, code 14 dagen
- **Onderwerp:** A "Which lid fits your pan?" (24) · B "Your thank-you 10% ends in 14 days" (34).
- **Preview:** "The lid in your pan's size. Your code expires on {day}."
- **Hero:** FITS YOUR PAN / `The lid|that fits` / "Your 10% thank-you code, for 14 days."
- **Verhaalstap:** S10: wat eigenaren als tweede kopen (de deksel).
- **Urgentie:** P3_THANKYOU_10_14D (U1, waar).
- **CTA:** "Add the lid, 10% off"
- **P.S.:** "Your code expires on the morning of {day}. It works on the whole order."
- **Blokken:** tailoring: geen deksel aanbieden als ze er al een hebben (cross-sell-agent).

### P3-pan-nocode
- Zelfde als P3-pan zonder code. Onderwerp B "The lid that fits your pan" (26). Preview: "The lid in your pan's size, plus 4 gifts with every order." Urgentie: geen. CTA "Add the lid that fits". P.S. "Not sure which size your pan is? Reply with your order number."

### P3-set · dag 20, set gekocht, code 14 dagen
- **Onderwerp:** A "The pan your set is missing" (27) · B "Crepe or wok, 10% for 14 days" (29).
- **Preview:** "The flat one and the deep one. Your code expires on {day}."
- **Hero:** blijft: FOR SET OWNERS / `The pan your|set is missing`
- **Verhaalstap:** S10 (wat sethouders erbij namen: Chetan, Pam).
- **Urgentie:** code 14 dagen (U1). **CTA:** "Add the crêpe pan, 10% off". **P.S.:** "Your code expires on the morning of {day}."
- **Blokken:** weg: "medium heat, the water test" (kennen ze).

### P3-set-nocode
- Zonder code. Onderwerp B "Flat for crepes, deep for stir-fry" (34) (huidige B is 48 tekens). CTA "Add the crêpe pan". P.S. "Already have both? Reply with what you cook most."

### P3-next · dag 20, overige pankopers, code 14 dagen
- **Onderwerp:** A "How is the pan treating you?" (28) · B "What goes next to your pan" (26). (Historie: check-in-vraag wint in post-purchase; nu A en B gewisseld.)
- **Preview:** "The board or the lid that matches your order. Your code expires on {day}."
- **Hero:** blijft.
- **Verhaalstap:** S10, matched aan wat ze hebben.
- **Urgentie:** code 14 dagen. **CTA:** "Use my 10% code". **P.S.:** "Your code expires on the morning of {day}."
- **Blokken:** weg: "A second Pan Pro... so one pan is never busy" (herhaling 15).

### P3-next-nocode
- Zonder code, zelfde onderwerpen. Preview: "The board or the lid that matches your order. 4 gifts with every order." CTA "See what fits my pan".

### P3-accessory · dag 20, alleen accessoire, code 14 dagen
- **Onderwerp:** A "Now meet the pan" (16) · B "From the board to the pan" (25).
- **Preview:** "We started with cutting boards too. Your 10% on the pan expires {day}."
- **Hero:** FOR SIRAAT OWNERS / `Now meet|the pan` / "Your 10% thank-you code, for 14 days."
- **Verhaalstap:** S2 (Benjamin begon zelf met snijplanken). Directe vergelijking (Floris): "Your next pan vs. your coated one: no coating to wear off, no PFAS, report no. 25895."
- **Urgentie:** code 14 dagen. **CTA:** "Get the Pan Pro, 10% off". **P.S.:** "Your code expires on the morning of {day}."
- **Blokken:** weg: closerlook (herhaling 18), Marilyn (herhaling 12). Blijft: Sunny.

### P3-accessory-nocode
- Zonder code. Preview: "We started with cutting boards too. Then the pan. 4 gifts with every order." CTA "Get the Pan Pro".

### P3-apron · dag 20, schort, code 14 dagen
- **Onderwerp:** A "An apron deserves a pan" (23) · B "Was the apron a gift?" (21).
- **Preview:** "10% off the pan it was made for. Your code expires on {day}."
- **Hero/verhaal:** blijft (cadeauperspectief). Tammy eruit (herhaling 9).
- **Urgentie:** code 14 dagen. **CTA:** "Get the Pan Pro, 10% off". **P.S.:** "Your code expires on the morning of {day}. A gift card works too, if they'd rather pick."

### P3-apron-nocode
- Zonder code. Preview: "The pan it was made for, for you or for them. 4 gifts with every order." CTA "Get the Pan Pro".

---

## 9. UGC (U1)

### U1 · 4 dagen na levering
- **Onderwerp:** A "Show us your first egg?" (23) · B "One photo, 15% off your next order" (34).
- **Preview:** blijft.
- **Hero/verhaal:** blijft (Floris: goed). Kleine wijziging: "Cold metal grabs..." vervangen door "Not there yet? Here's the 3-step guide" met link (herhaling 6).
- **Urgentie:** geen deadline in de mail; de 15%-code geldt 60 dagen na verzending door support (echt, maar pas na de foto). **CTA:** "Send my photo". **P.S.:** "After the egg: a steak. Pan hot first, lay it down, leave it until it lets go."

---

## 10. VIP (V1, V2)

### V1 · 30 dagen na tweede order, unieke code 14 dagen
- **Onderwerp:** A "You're a VIP. Here's 15% off." (29) · B "15% off, exclusive to VIPs" (26).
- **Preview:** "Two orders makes you a VIP. Your own 15% code, until {day}."
- **Hero:** VIP · 15% EXCLUSIVE / `You're a VIP.|Here's 15%.` / "Your own code. Gone in 14 days."
- **Verhaalstap:** S7 (Floris: "You're a VIP customer, 15% off, exclusive, get it now"): "Out of 100,000+ customers, you're one of the people who came back. That makes you a VIP, and VIPs get 15%." [VRAAG] "Most people stop at one order" staat nu in de mail; laat Floris bevestigen dat dat klopt (repeat-omzet 12%).
- **Urgentie:** SK_REGULARS15_14D (U1, waar). "Exclusive" is waar: de pool gaat alleen naar klanten met 2+ orders.
- **CTA:** "Get my 15% now"
- **P.S.:** "Your 15% expires on the morning of {day}. One use, on your whole order."
- **Blokken:** weg: "Twice is a habit" overal (Floris: slecht), Tammy (zelfde mensen krijgen haar in R2-vip). Tailoring: goes-blok mag niet tonen wat ze al hebben (deksel, plank, wok; tailoring-agent).

### V1-nocode · zelfde plek, cooldown (code in laatste 30 dagen)
- **Onderwerp:** A "You're a VIP. Thank you." (24) · B "For our VIPs: a note from Benjamin" (34).
- **Preview:** "Two orders makes you a VIP. A thank you, and 4 gifts with every order."
- **Hero:** VIP / `You're a VIP.|Thank you.` / "4 gifts with every order."
- **Verhaalstap:** als V1, zonder code.
- **Urgentie:** geen. Floris wil VIP = 15%. **[BESLISSING EIGENAAR]**: VIP uitzonderen van de code-cooldown (dan vervalt deze variant), of deze variant houden met HI10.
- **CTA:** "Shop with my 4 gifts". **P.S.:** "Which pan do you reach for most? Reply and tell me."

### V2 · 10 dagen na V1, Benjamin vraagt
- **Onderwerp:** A "A question from Benjamin" (24) · B "What should we make next?" (25).
- **Preview/verhaal:** blijft.
- **Urgentie:** P.S. bij code: "Your VIP 15% expires on {day}" (datum van V1 + 14 dagen, dus nog 4 dagen; tag `{{DATE:4:l, F j}}` alleen als V2 exact 10 dagen na V1 valt). Zoekterm in de P.S. wordt "You're a VIP" in plaats van "Twice is a habit".
- **CTA:** "Take me to the shop".

---

## 11. Winback (R1, R2)

### R1-pan · dag 45, pan gekocht
- **Onderwerp:** A "How's your pan doing?" (21) · B "What pan owners add next" (24).
- **Preview:** "Six weeks in. Here's what owners of the same pan add next."
- **Hero:** blijft.
- **Verhaalstap:** check-in + S10. Roasting pan alleen US: [VRAAG] Floris wil het zeker weten; tot dan alleen tonen bij `country_code == 'US'` (staat al zo).
- **Urgentie:** geen (HI10).
- **CTA:** "Shop with my 10%". **P.S.:** "Honestly, how is it doing? Reply, good or bad."
- **Blokken:** weg: HI10 uit de preview.

### R1-set · dag 45, set gekocht
- **Onderwerp:** A "The shapes a set leaves out" (27) · B "Which pan do you reach for most?" (32).
- **Preview:** "The flat one, the deep one, the board and the tools."
- **Verhaal/hero:** blijft. **Urgentie:** geen. **CTA:** "Shop with my 10%". **P.S.:** "Reply with the pan you grab first. It shapes what we make next."

### R1-acc · dag 45, alleen accessoire
- **Onderwerp:** A "Ready for the pan?" (18) · B "Still cooking on a coated pan?" (30).
- **Preview:** "You started the way we did, with the board. Here's the pan."
- **Hero:** blijft.
- **Verhaalstap:** S2 + de directe vergelijking (enige in winback): "Your next pan vs. your coated one: no coating to wear off, no PFAS (report no. 25895)."
- **Urgentie:** geen. **CTA:** "Get 10% off the pan". **P.S.:** "Not sure which size? Reply with what you cook most."
- **Blokken:** weg: closerlook (herhaling 18), Tammy.

### R2 · dag 75, unieke code 72 uur
- **Onderwerp:** A "Your 10% expires in 72 hours" (28) · B "Ready for pan number two?" (25).
- **Preview:** "Your own code, already applied. Gone on {day} morning."
- **Hero:** YOUR CODE · 72 HOURS / `Pan number two,|10% off` / "Your own code. Gone in 72 hours."
- **Verhaalstap:** "If one pan is always busy" (enige plek, herhaling 15) + S10 (Don J., Beverly G. steak).
- **Urgentie:** R2_10_72H (U1). Floris: meer urgentie. Codebalk, tegels en P.S. met datum; offer-kop "Your 10% runs out {day}".
- **CTA:** "Use my 10% now"
- **P.S.:** "Your code expires on the morning of {day}. After that, the regular sale price applies. Your 4 gifts come with the order either way."
- **Blokken:** twee beloftes alleen als korte regel, zonder reviews. Tammy uit de ugc-rij (herhaling 9).

### R2-nocode · dag 75, geen code
- **Onderwerp:** A "Ready for pan number two?" (25) · B "Your next piece comes with 4 gifts" (34).
- **Preview:** blijft. **Urgentie:** geen. **CTA:** "Shop with my 4 gifts". **P.S.:** "Reply with the pan you own, we'll tell you which size goes next."
- **Blokken:** weg: Tammy.

### R2-vip · dag 75, 2+ orders, unieke code 72 uur
- **Onderwerp:** A "15% exclusive discount, 72 hours" (32) · B "You came back. Here's 15%." (26).
- **Preview:** "For VIPs only. Already applied. Gone on {day} morning."
- **Hero:** FOR VIPs · 72 HOURS / `You came back.|Here's 15%.` / "Exclusive discount. Gone in 72 hours."
- **Verhaalstap:** S10 (Tammy, hier wel: zelfde soort klant).
- **Urgentie:** R2_VIP_15_72H (U1). Floris: "15% exclusive discount" (waar: alleen 2+ orders).
- **CTA:** "Get my 15% now"
- **P.S.:** "Your 15% expires on the morning of {day}. A thank you has an end date, so it stays a thank you."

### R2-vip-nocode · dag 75, 2+ orders, cooldown
- **Onderwerp:** A "You came back. Thank you." (25) · B "What should we make next?" (25).
- **Preview/verhaal:** blijft. **Urgentie:** geen; zie V1-nocode **[BESLISSING EIGENAAR]** over VIP en cooldown. **CTA:** "Shop with my 4 gifts".

---

## 12. Anniversary (N1, N2)

### N1 · 6 maanden na eerste (en enige) order
- **Onderwerp:** A "Six months in. Anything worn off?" (33) · B "How's your pan at six months?" (29).
- **Preview:** "There was nothing on it to wear off. Here's what owners add at six months."
- **Hero:** SIX MONTHS IN / `Nothing|worn off` / "Half a year of cooking, no coating."
- **Verhaalstap:** S8 als bewijs uit hun eigen keuken: "Six months of cooking, and there's nothing worn off, because there was nothing on it to wear off."
- **Urgentie:** geen.
- **CTA:** "Find my second piece" (Floris: geen care video als hoofdknop voor iemand die een half jaar geleden kocht).
- **P.S.:** "A brown tint, more sticking, a loose handle? Reply with a photo. The tint is carbonized oil, sticking is the heat, and a loose handle is what the 75-year warranty is for."
- **Blokken:** weg: care-video-CTA (2x), "Three short answers" als hoofdblok (wordt de P.S.). Blijft: second-piece-blok (tailored: niet wat ze al hebben).

### N2 · 1 jaar, unieke code 7 dagen
- **Onderwerp:** A "One year in. Here's 15% off." (28) · B "A year on titanium. 74 to go." (29).
- **Preview:** "A year ago you placed your first order. Your own 15%, until {day}."
- **Hero:** ONE YEAR · 15% FOR 7 DAYS / `A year on|titanium` / "74 years left on your warranty."
- **Verhaalstap:** S8: "A year of cooking. Nothing has worn off. Your 75-year warranty has 74 to go."
- **Urgentie:** code 7 dagen (U1). Floris: 15%. **[BESLISSING EIGENAAR]**: nieuwe pool SK_ANNIV15_7D aanmaken (nu SK_ANNIV10_7D = 10%). Tot die er is: copy niet live zetten.
- **CTA:** "Get my 15% now"
- **P.S.:** "Your 15% expires on the morning of {day}. One week, like the week you ordered."
- **Blokken:** weg: dubbele "Thank you for a year" (herhaling 24), Tammy (herhaling 9).

### N2-nocode · 1 jaar, cooldown
- **Onderwerp:** A "One year ago this week" (22) · B "A year on titanium. 74 to go." (29).
- **Preview:** blijft. **Urgentie:** geen. **CTA:** "Shop with my 4 gifts". **Blokken:** zoals N2.

---

## 13. Sunset (S1, S2)

### S1 · re-permission
- **Onderwerp:** A "Should we keep writing to you?" (30) · B "Still want our emails? One tap." (31).
- Rest blijft (Floris: goed). **Urgentie:** "we'll stop writing in about a week" is waar (S2 + split na 3 dagen). **CTA:** "Yes, keep me on the list".

### S2 · laatste
- **Onderwerp:** A "Last email from me (unless you tap)" (35) · B "Should I stop writing?" (22).
- Rest blijft. **Urgentie:** laatste mail (U8, waar). **CTA:** "Keep me on the list". De "keep me on the list"-vervolgflow is voor de sunset-agent.

---

## 14. Open voor Floris

1. **Einddatum fall sale en gift-stack** (U5b, U6). Zonder datum blijft "pending" de sterkste eerlijke urgentie in C1 tot C3, K1, K2.
2. **Fall-set: $299 of $349**, welke handle, en mag "pay for 2 pans, the Mini and 3 lids are free" letterlijk zo (C3-p, C3-s, W4).
3. **K3/C4-formulering**: akkoord op "we're taking your 10% off this cart on {day}" in plaats van "we're removing your cart" (U3 is niet waar).
4. **Filtertrekking**: officiële voorwaarden met wekelijks sluitmoment, dan wordt U7 een echte deadline.
5. **Anniversary 15%**: nieuwe pool SK_ANNIV15_7D.
6. **VIP en code-cooldown**: VIP altijd 15% (dan vervallen V1-nocode en R2-vip-nocode als variant) of de cooldown houden.
7. **B1-test**: T05a (autoriteit tegen social proof) vervangen door aanbod tegen oprichter, of later.
8. **Unieke welkomstcode** (besluit B): pas dan een echte deadline in W5.
9. **Claim "PFAS-pannen"**: Floris noemt coated pans "PFAS-pannen". Waar is: PTFE (de meeste non-stick coatings) valt onder de OECD-definitie van PFAS, maar dat staat niet in claims.csv. Tot akkoord schrijven we "a coated non-stick pan" naast "ours: no PFAS, report no. 25895" en laten de lezer de conclusie trekken.
10. **Testcheckout**: bevestigen dat de 4 gift-regels in de checkout staan (U4), en de Shopify-cart-levensduur (U3).
