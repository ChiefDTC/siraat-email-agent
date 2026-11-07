# Urgentiesysteem Black Friday 2026 (7 nov 2026)

Vraag: de mails moeten tijdens de VIP Black Friday (tot 70% off + 5 free gifts, tot en met 30 nov) veel meer urgentie hebben, zoals Smooche. Wat doet Smooche precies, wat doen Our Place en HexClad, wat doen wij nu, en hoe bouwen we urgentie die waar is.

Alleen gelezen. Niets gewijzigd in Klaviyo, Shopify of Gmail, niets verstuurd. Geen klantdata en geen echte BF-code in dit stuk (placeholder BFCODE).

Bronnen:
- Gmail lolagroothuis@gmail.com: `from:smooche` in de laatste 45 dagen geeft **0 directe Smooche-mails**. Het enige Smooche-materiaal in dit account is de doorgestuurde thread "lukje" van Floris (1 nov 17:08 UTC) met 13 Smooche-mails als .eml-bijlage. Tijden komen uit `research/smooche/04-meer-output-november.md` (Klaviyo-afmeldtoken, klopt op minuten). Zoektermen `SMOOCHEVIP`, `"VIP ONLY"`, `hey@smooche.com`, `"You missed this"`: geen treffers. De voorbeelden "VIP ONLY: An Extra 20% Off This Weekend, YOUR PASSWORD: SMOOCHEVIP" en "You missed this" komen dus uit de opdracht, niet uit deze mailbox; ze staan hieronder als patroon, niet als gemeten mail.
- Gmail plus-adressen (concurrententest): HexClad, Our Place, Made In; vastgelegd in `research/concurrenten/tijdlijn.csv` en `overzicht.md`.
- Klaviyo (read-only, `GET /api/campaigns` en `POST /api/campaign-values-reports`, conversie RSNxYV): alle e-mailcampagnes 24 okt tot 8 nov.
- DECISIONS.md, PLAYBOOK.md, skill siraat-direct-response, `research/smooche/06-volume-plan-smooche.md`, `research/homestead/kalender-november-2026.md`.

---

## 0. Kort

- Smooche verkoopt niet met één deadline maar met een **ketting van steeds nieuwe, persoonlijke deadlines**: "sale ends tonight", "credit expires today", "credit extended 24 hours, cannot be extended again", "final hours" met aftelklok, "pending order canceled within 24 hours". Bijna geen daarvan is echt (de sale liep door, het "tegoed" is een kortingscode, de "pending order" bestaat niet).
- Siraat heeft in november **nul echte deadlines in campagnes** behalve de eendaagse trekking op 4 nov. Juist die mail ("Win your order back (today only)") had de beste RPR van november in de US: **$0,171**, tegen $0,03 tot $0,12 voor de rest. De laatste echte deadline-mail ("The October sale ENDS TONIGHT", 31 okt) deed $0,166. Deadlines werken bij ons ook, we gebruiken ze alleen niet.
- Grootste gaten: (1) geen echte tussendeadlines tussen 1 en 30 nov, (2) resends bestaan pas sinds 8 nov en alleen op niet-openers met hetzelfde onderwerp, (3) geen "extra bovenop" voor VIP/kopers in het weekend, (4) de wekelijkse filtertrekking mag nog geen deadline zijn (geen officiële regels), (5) klikratio's zijn laag (0,4 tot 1,1%), dus de mails openen wel maar geven geen reden om nu te klikken.
- Voorstel: **elke week een echte, kleine deadline** (weekend-extra met eigen code 48 uur, flash-product 24 uur, trekking zodra de regels er zijn), resends naar niet-openers én niet-klikkers met een nieuw onderwerp, en de harde eindpush 28 tot 30 nov die al gepland is.

---

## 1. Smooche-tijdlijn (gemeten, uit de .eml's)

Aanmelding 30 okt rond 23:27 UTC, cart en checkout gestart ~31 okt 14:30 UTC. Uren na aanmelding. Bedrag en code van het "tegoed" weggelaten.

| # | UTC | Uur | Afzender | Onderwerp | Preview / kern | Urgentiemiddel |
|---|---|---|---|---|---|---|
| 1 | 30 okt 23:28 | 0,0 | Smooche | You joined at the right time 👻 | "Our Halloween sale takes up to 60% off everything, no code needed" | thema (Halloween), "no code needed" |
| 2 | 30 okt 23:58 | 0,5 | Chloe from Smooche | Found your new make-up? | "the sale we're running right now ends tonight at midnight" | **deadline vanavond**, "No extensions this time" (sale liep door: onwaar) |
| 3 | 31 okt 01:29 | 2,0 | Chloe from Smooche | No tricks, just a treat | "Everything is up to 60% off, and it's already applied" | **voorraadclaim** "running pretty low on stock", "limited time" |
| 4 | 31 okt 12:57 | 13,5 | Smooche | Happy Halloween 🎃 | "You have [bedrag] store credit left. Expires Today" | **nep-tegoed** (kortingscode met $30 minimum), zegel "Expires Today", "support team just checked" |
| 5 | 31 okt 14:41 | 15,2 | Chloe from Smooche | Still want your foundation? | "This exclusive sale is set to end very soon, and only available while current stock lasts" | vage deadline + voorraad |
| 6 | 31 okt 15:42 | 16,3 | Smooche | Foundation that adapts to you | "3 reasons", "selling out fast, but the deal's still live" | **voorraadclaim**, "60% Off + Free Gifts" |
| 7 | 31 okt 15:56 | 16,5 | Chloe from Smooche | Your order is pending. | "pricing is tied to today's flash sale and will expire SOON", "pending orders not completed within 24 hours will be marked as canceled" | **nep-order**, flash-sale, gratis verzending "activated" |
| 8 | 1 nov 01:30 | 26,0 | Smooche | What the right foundation actually does | reviews, "97% said it matched" | geen (bewijs) |
| 9 | 1 nov 13:57 | 38,5 | Chloe from Smooche | (1) Your store credit is updated. | "I extended your credit with just 24 hours (until tonight)... cannot be extended again" | **verlengde deadline**, "(1)" in onderwerp als notificatie |
| 10 | 1 nov 14:42 | 39,2 | Chloe from Smooche | Your foundation order is pending. | checkoutlink | nep-order, tweede ronde (+24 u) |
| 11 | 1 nov 15:43 | 40,3 | Smooche | A photo of me went viral for the wrong reason | brief van "Jen", "60% off right now" | verhaal, geen deadline |
| 12 | 1 nov 15:57 | 40,5 | Chloe from Smooche | #1 Korean Foundation is waiting for you. | "Now available at 58% off" | cart wacht |
| 13 | 1 nov 16:46 | 41,3 | Smooche | Your [bedrag] is about to disappear | "Final hours", "ends tonight", aftelklok (countdownmail.com), "use it or lose it" | **live aftelklok**, verlies-framing |
| (opdracht) | n.v.t. | | Smooche | VIP ONLY: An Extra 20% Off This Weekend, YOUR PASSWORD: SMOOCHEVIP | (niet in deze mailbox) | **VIP + wachtwoord + extra % bovenop + weekend-deadline** |
| (opdracht) | n.v.t. | | Smooche | You missed this | (niet in deze mailbox) | **resend naar niet-openers/niet-klikkers** |

Cadans:
- 13 mails in 41 uur; 5 in de eerste 3 uur; drukste dag 6 mails.
- Cart/checkout in blokken van drie (+10 min, +1 u, +1 u 15) en precies 24 uur later nog eens drie.
- Welkom op 0, +2 en +26 uur. "Tegoed"-reeks: dag 0 "expires today", dag 1 "verlengd", dag 1 avond aftelklok.
- Bijna elke mail heeft een eigen, nieuwe reden om vandaag te kopen. Geen mail herhaalt dezelfde deadline.

### Our Place en HexClad (zelfde periode, plus-adressen)

| UTC | Merk | Onderwerp | Urgentiemiddel |
|---|---|---|---|
| 18 okt 19:01 | HexClad | 2x entries ends today 🍕 | dubbele winkansen, deadline vandaag, geen korting |
| 25 okt 16:30 | HexClad | Ends soon: 2x entries on accessories | dubbele punten, echte einddatum (2 nov) |
| 1 nov 08:15 | Our Place | Last Call for Mystery Rewards (preview "Don't miss out!") | loyaliteitsbeloning, "Ends Tonight" 23:59 PT, persoonlijke code |
| 1 nov 18:00 | HexClad | You. Italy. $10K. Need we say more? (preview "LAST CHANCE to enter giveaway!") | einde winactie (2 nov), echt |
| 4 nov 06:15 | Our Place | Black Friday's (Almost) Here | aankondiging |
| 5 nov 05:15 | Our Place | BLACK FRIDAY AT OUR PLACE | start, "biggest sale of the year" |
| 5 nov 20:30 | HexClad | Thanksgiving VIP Sale starts now 🦃 | **"VIP"-label**, alleen naar hello@-segment (b en c, niet w) |
| 5 nov 21:17 | HexClad | Your kitchen needs this! | tweede mail 47 min later (browse) |
| 5 nov 21:38 | Our Place | A Note to Start Black Friday ("Morgan here") | persona-brief op de startdag |

Lessen: de kookgerei-concurrenten gebruiken **echte** deadlines, maar vaak op iets anders dan de prijs (winkansen, punten, beloningen). HexClad noemt de pre-sale "VIP" en stuurt hem alleen naar een betrokken segment. Our Place stuurt elke campagne gespreid in drie golven (06:15, 12:15, 14:15 UTC per segment).

---

## 2. De mechanieken die ertoe doen (8)

| # | Mechaniek | Smooche-vorm | Werkt omdat | Eerlijke Siraat-vorm |
|---|---|---|---|---|
| 1 | **Echte einddatum, hard aan het eind** | "ends tonight at midnight", aftelklok | verliesaversie, beslismoment | 30 nov: "Black Friday ends tomorrow", "Last day", "Final hours" + aftelklok tot de echte eindtijd (alleen campagnes, niet in flows) |
| 2 | **Tussendeadlines (ketting)** | elke dag een nieuw "expires today" | elke mail een nieuwe lus | wekelijks één echte kleine deadline: weekend-extra (48 u), flash-product (24 u), trekking (zondag 23:59 ET, zodra regels er zijn) |
| 3 | **VIP / wachtwoord / extra bovenop** | "VIP ONLY, extra 20%, password SMOOCHEVIP, this weekend" | exclusiviteit + reden + einde | "VIP weekend: your own extra X% on top, until Sunday 23:59 ET" met **unieke Klaviyo-code** per profiel (`{% coupon_code %}`), alleen naar kopers + E30. Geen vaste "password"-code (lekt naar couponsites) |
| 4 | **Resend naar niet-openers én niet-klikkers** | "You missed this" | 30 tot 50% van de oorspronkelijke opens erbij voor weinig moeite | resend +24 tot 48 u met **nieuw onderwerp** naar niet-openers; aparte korte brief naar openers zonder klik |
| 5 | **Gift-ontgrendeling** | "60% Off + Free Gifts" | gratis dingen wegen zwaarder dan % | "5 free gifts with every order. They end when Black Friday ends." Alleen waar (gifts lopen tot 30 nov) |
| 6 | **Voorraadclaim** | "running pretty low", "selling out fast" | schaarste | alleen "Just arrived and selling fast" voor 6-Pcs en 12-Pcs zolang Floris dat in de backend bevestigt; concreet getal alleen met echte data |
| 7 | **Cadans en verdichting** | 13 mails in 41 u, blokken van 3 | aanwezigheid op het beslismoment | volumeplan v2 (13 in 40,5 u), daarna dagelijkse campagne en 3 à 5 per dag op 28 tot 30 nov |
| 8 | **Persoonlijke afzender bij de deadline** | "Chloe": "I extended your credit" | voelt als een mens die iets regelt | Benjamin bij echte momenten ("The sale ends tonight. One honest note first."), nooit een verzonnen handeling |

Bewust niet: nep-tegoed, "your order is pending", "we extended" (verlengen na "cannot be extended"), aftelklok zonder echt einde, "(1)" in het onderwerp als nep-notificatie, verzonnen klantverhalen.

---

## 3. Siraat nu tegenover Smooche

### Campagnes laatste 14 dagen (Klaviyo, verzendtijd UTC)

| Verzonden | Campagne | Onderwerp | Preview | Ontv. | Open | Klik | RPR | Deadline / resend |
|---|---|---|---|---|---|---|---|---|
| 27 okt 08:15 | Oct E11 plain text | The October sale ends this week | | 83.306 | 41,4% | 0,69% | $0,155 | echte deadline (week) |
| 31 okt 08:15 | Oct E12 Halloween | The October sale ENDS TONIGHT ⏰ | Up to 70% off + 4 free gifts | 84.564 | 40,9% | 0,80% | **$0,166** | echte deadline vandaag |
| 1 nov 08:15 | Nov E1 INTL | Black Friday Savings Start Today | Up to 70% off. FREE gifts too. | 75.034 | 38,0% | 0,87% | $0,097 | geen |
| 1 nov 08:15 | Nov E1 US (Pizza Steel) | Black Friday Savings Start Today | Up to 70% off. FREE gifts too. | 74.434 | 35,8% | 0,58% | $0,102 | geen |
| 2 nov 09:00 | Roasting Pan INT launch | New in. Already 70% off. | The titanium roasting pan just landed in our warehouse. | 73.390 | 38,6% | 0,78% | $0,088 | "just landed" (waar) |
| 3 nov 08:15 | Nov E2 recept US | What I cooked last Tuesday | | 67.688 | 41,1% | 0,24% | $0,087 | geen |
| 3 nov 08:15 | Nov E2 recept INTL | What I cooked last Tuesday | | 52.831 | 45,5% | 0,34% | $0,093 | geen |
| 4 nov 09:00 | Win Your Order Back US | Win your order back (today only) | Order anything today and it could be on us. Everything is already up to 70% off. | 74.697 | 42,4% | 0,78% | **$0,171** | **echte dagdeadline (trekking)** |
| 4 nov 09:00 | Win Your Order Back INTL | Win your order back (today only) | idem | 52.047 | 49,3% | 1,13% | $0,077 | idem |
| 5 nov 08:15 | Nov E3 US | Replace the whole drawer in one order! | FREE gifts with the PFAS-free set | 72.533 | 43,8% | 0,50% | $0,109 | geen |
| 5 nov 08:15 | Nov E3 INTL | Replace the whole drawer in one order! | FREE gifts with the PFAS-free set | 49.206 | 48,5% | 0,57% | $0,095 | geen |
| 6 nov 18:07 | Benjamin-brief 2 Pans + 2 Lids US | I need to show you something | One pan is $144. For $105 more you get all four pieces. | 76.794 | 43,4% | 0,55% | $0,124 | geen |
| 7 nov 08:15 | Nov E4 US | Up to 70% OFF pans for Thanksgiving | The pans that do the work on the day | 73.288 | 26,5% | 0,37% | $0,068 | geen (Thanksgiving impliciet) |
| 7 nov 08:15 | Nov E4 INTL | Up to 70% OFF pans for Thanksgiving | idem | 51.371 | 37,3% | 0,50% | $0,031 | geen |
| 8 nov 10:00 (gepland) | Resend 1 Nov E1 US en INTL | Still cooking on coated pans? | Up to 70% OFF + FREE gifts | segment "Ressend 1 / November 2026" | | | | **eerste resend**, nieuw onderwerp |

(Testcampagnes `[TEST] AB Q4` van 28 okt en de review-catch-up weggelaten.)

Lezing:
- De twee mails met een echte deadline vandaag (31 okt en 4 nov US) zijn de twee beste van de periode. Zonder deadline zakt de US-RPR naar $0,07 à $0,11.
- Klikratio's zijn overal laag (0,24 tot 1,13%). Opens zijn goed (36 tot 49%, wel opgeblazen door Apple MPP). Probleem zit dus in "waarom nu klikken".
- 7 nov US: opens vallen naar 26,5%. Vijfde campagne in 7 dagen naar E90 zonder nieuwe reden; "Up to 70% OFF" in het onderwerp is na een week geen nieuws meer.
- Spam 0,01 tot 0,03%, afmelden 0,22 tot 0,56%: ruim binnen de vangrail (0,3% spam). Er is ruimte voor meer druk.
- Resend: de eerste resend komt pas op 8 nov (E1, een week na verzending, nieuw onderwerp). Geen resend naar niet-klikkers.

### Naast elkaar

| | Smooche | Siraat nu | Gat |
|---|---|---|---|
| Deadlines per week | elke dag een nieuwe | 1 (trekking 4 nov) | groot |
| Einddatum sale in mail | ja, steeds "tonight" | bewust niet in flows (besluit 1 nov); campagnes ook niet | klein in flows (goed zo), groot in campagnes vóór 28 nov |
| VIP / extra bovenop | "extra 20% this weekend" | BFCODE alleen in abandonment-flows; VIP 15% (okt) niet in de BF-campagnes | groot |
| Resend niet-openers | "You missed this" | vanaf 8 nov, 3 gepland (Homestead) | middel |
| Resend niet-klikkers | waarschijnlijk | geen | groot |
| Gift als deadline | "+ Free Gifts" | "5 free gifts" staat in de mails, maar zonder "end with the sale" in de meeste campagnes | middel |
| Voorraad | vaag, onwaar | "Just arrived and selling fast" mag, nog nauwelijks gebruikt in campagnes | middel |
| Aftelklok | ja (countdownmail.com) | nee | pas op 29 en 30 nov |
| Persona bij deadline | Chloe | Benjamin-brieven bestaan (beste niet-deadline RPR, $0,124) | klein |

---

## 4. Welke deadlines Siraat echt heeft

| Deadline | Echt? | Wat mag in de mail | Voorwaarde |
|---|---|---|---|
| **Einde Black Friday Sale 30 nov** | ja | "Black Friday ends tomorrow / today / tonight", aftelklok in campagnes 29 en 30 nov | eindtijd en tijdzone van Floris (open vraag uit 06, punt 1); niet in flowmails (besluit 1 nov) |
| **5 free gifts** | ja, lopen met de sale | "Your 5 free gifts end when Black Friday ends." | alleen tot 30 nov; INT zonder bedrag, US "$555 value" |
| **Wekelijkse PFAS-filtertrekking** | nog niet als deadline | nu alleen "a chance to win a PFAS water filter (weekly draw)" | officiële regels met sluitmoment (bijv. zondag 23:59 ET) en "no purchase necessary"; daarna "Order by Sunday to be in this week's filter draw" |
| **Dagtrekking "Win your order back"** | ja, als eenmalige actie | "(today only)" zoals 4 nov | ook hier regels/AMOE; herhalen alleen als het weer echt één dag is |
| **Unieke code met vervaldatum** | ja | "Your own extra 10%, until Sunday 23:59 ET. Then the Black Friday price still applies." | Klaviyo `{% coupon_code %}`, Shopify dynamic coupon, one use, stapelt op sale (besluit 19 okt); marge checken bij 70% |
| **Flash-product 24 u** (bijv. Wok of Deep Pan een dag lager, of gratis deksel) | alleen als Floris het echt instelt | "Today only: the Wok Pan Pro at $X. Tomorrow back to $Y." | prijs gaat na 24 u echt terug; EU-laagste-prijs-30-dagen check |
| **Pizza Steel gratis bij 12-Pcs (US)** | zolang de actie loopt | "+ FREE Pizza Steel ($664 value) with this set" | einde alleen noemen als het een echt einde heeft |
| **"Just arrived and selling fast"** (6-Pcs, 12-Pcs) | ja, zolang voorraad | "Just arrived and selling fast" | elke maandag en op 20 en 27 tot 30 nov in de backend checken; uitverkocht = regel weg |
| **Laatste mail van een reeks** | ja | "This is the last email about Black Friday." | alleen op 30 nov 20:00 |

### Wat we niet zeggen

- "next batch", "reserve", "coming", "arriving", "reserved for you", "price held" (DECISIONS 1 nov).
- Een einddatum van de sale in flowmails (besluit 1 nov avond); flows krijgen urgentie via de unieke code en de gifts, niet via 30 nov.
- "Only X left", "almost gone", "low stock" zonder echte voorraaddata per markt.
- "Ends tonight" of een aftelklok vóór 29 nov (de sale loopt door), "No extensions", "cannot be extended again" als we verlengen.
- "Your order is pending", "we added credit to your account", "our team noticed", "(1)" in het onderwerp.
- "Last chance" behalve in de echte laatste mails op 30 nov.
- "Free filter", "purifier"; "lifetime warranty", "100-day trial", "risk-free", "free returns".
- Een vaste VIP-"password"-code in de mail (lekt, en dan is "VIP only" niet meer waar). Nooit de echte BF-code in repo of plan.
- "Prices go back up" zolang de prijs na 30 nov niet vaststaat (open vraag 06, punt 2).

---

## 5. Urgentiekalender 8 tot 30 november

Uitgangspunt: Homestead-kalender (E5 tot E20, resends 1 tot 3) blijft staan; dit voegt de **urgentielaag** toe. Tijden in UTC tenzij "lokaal". Uitsluitingen overal: Basis, P7 (P3 in BF-week), wie in de laatste 1 uur een cart/checkout-flowmail kreeg. Vangrail: spam boven 0,3% op een verzending van 1.000+ = stoppen.

Resend-regel (nieuw, voor elke verkoopcampagne van Homestead en ons):
- **R-a niet-openers**: +24 u (weekend) of +48 u, nieuw onderwerp, zelfde mail. Segment: ontvangen campagne X, niet geopend, geen order sinds verzending.
- **R-b openers zonder klik**: +24 u, korte Benjamin-brief (platte tekst, één knop) met één nieuwe reden (gift, deadline, review). Segment: geopend X, niet geklikt, geen order. Let op: Apple MPP maakt "geopend" onbetrouwbaar; daarom R-b alleen als de mail een echte nieuwe reden heeft.

| Dag | Tijd | Wat | Segment | Urgentiemiddel | Onderwerp A / B |
|---|---|---|---|---|---|
| zo 8 nov | 10:00 | Resend 1 (E1, gepland) | Ressend 1 US/INTL | resend | Still cooking on coated pans? (staat) |
| ma 9 nov | 17:00 | **R-b op E4** (Thanksgiving) | openers E4 zonder klik | gift-einde | 5 free gifts, one order / The gifts end with Black Friday |
| di 10 nov | 08:15 | E5 recept (Homestead) | E30 | geen, BF-band | (Homestead) |
| wo 11 nov | 08:00 | E6 founder-brief (Homestead) | E90 | Benjamin | (Homestead) |
| do 12 nov | 16:00 | **Flash 1** (alleen als Floris een echt 24-uursaanbod zet, bijv. Wok of Deep Pan Pro) | E90 + Product Viewers L30 | 24 u, echt | Today only: the Wok Pan Pro at $X / 24 hours. One pan. |
| vr 13 nov | 16:00 | **VIP weekend 1** aankondiging | kopers (alle) + E30 | unieke code, extra X% bovenop, tot zo 23:59 ET | VIP weekend: an extra X% on top / Your own code, until Sunday |
| za 14 nov | 08:15 | E7 Free Gifts (Homestead) | All buyers + E90 | gifts | (Homestead) |
| zo 15 nov | 10:00 | Resend 2 (E7, gepland) | niet-openers E7 | resend | You missed this: 5 free gifts / The gifts are still on |
| zo 15 nov | 18:00 | **VIP weekend 1 laatste uren** | VIP-ontvangers zonder order, niet geklikt | echte einde code | Your extra X% ends tonight / Benjamin here, before your code ends |
| di 17 nov | 08:15 | E8 recept (Homestead) | E30 | | (Homestead) |
| wo 18 nov | 08:00 | E9 Before the Rush (Homestead) | E90 | Benjamin | (Homestead) |
| do 19 nov | 16:00 | **Flash 2** (als echt) of v2-proof | E90 | 24 u | Today only: ... / "The last pans we ever have to purchase" |
| vr 20 nov | 08:15 | v2-w2 "selling fast" (volumeplan, alleen als op voorraad) | E90 | voorraad, echt | The sets are selling fast / Just arrived: the 6 and 12-piece sets |
| za 21 nov | 08:15 | E10 Gift Guide (Homestead) | E90 | | (Homestead) |
| zo 22 nov | 10:00 | v2-pricelist + **R-a op E10** | E30 + abandoners L30 / niet-openers E10 | eerste echte telling naar 30 nov in een campagne (8 dagen) | 8 days left: the price list / Every price, before the last week |
| ma 23 nov | 08:15 | E11 BF Week Is Here (Homestead) | Lijst | start BF-week | (Homestead) |
| di 24 nov | 08:15 | E12 Bon Appetit (Homestead) | E90 | autoriteit | (Homestead) |
| wo 25 nov | 10:00 | E13 Still Deciding (Homestead) | abandoners L30 | | (Homestead) |
| do 26 nov | 16:00 | **VIP weekend 2** aankondiging (Thanksgiving-weekend) | kopers + E30 | unieke code tot zo 29 nov 23:59 ET | VIP: an extra X% for the last weekend / Your own code, Thursday to Sunday |
| vr 27 nov | 08:00 / 13:00 / 18:00 / 21:00 | E15, E16, E17 (Homestead) + v2-pricelist | volgens 06 sectie 5 | "Black Friday is here", gifts | (zie 06) |
| za 28 nov | 08:15 / 10:00 / 19:00 | v2-sat28, E18, v2-proof | volgens 06 | "3 days left" | The last weekend of Black Friday / 3 days left: up to 70% off |
| zo 29 nov | 09:00 | v2-sun29 | Lijst | **aftelklok tot echt einde**, "ends tomorrow" | Black Friday ends tomorrow / Tomorrow it is over |
| zo 29 nov | 10:00 | Resend 3 (E16) | niet-openers E16 | resend | You missed this: Black Friday bestsellers |
| zo 29 nov | 18:00 | **VIP weekend 2 laatste uren** | VIP-ontvangers zonder order | einde code | Your extra X% ends tonight |
| zo 29 nov | 19:00 | v2-sun29 resend | niet-openers v2-sun29 + abandoners L30 | resend | Tomorrow it is over |
| ma 30 nov | 07:00 / 10:00 / 13:00 / 17:00 / 20:00 | v2-mon-am, E19, v2-mon-pm (Benjamin), E20, v2-mon-late | volgens 06 | "Last day", "Final hours", aftelklok, "Last email" | Last day: up to 70% off / Final hours / Last email: Black Friday ends tonight |

Flows (geen sale-einddatum, besluit 1 nov): urgentie via BFCODE (cart/checkout), "5 free gifts with every order", "Just arrived and selling fast" en de cadans uit 06 (C1b +1 u, C1c +3 u, C2 +24 u ...). Op 29 en 30 nov C2 tijdelijk naar +6 u (06 sectie 5).

### Onderwerpregels per mechaniek (5 types, skill §5)

VIP weekend (extra bovenop, unieke code):
1. Offer: "VIP weekend: an extra 10% on top"
2. Specificiteit: "Your own code, until Sunday 11:59 PM ET"
3. Vraag: "Want the Black Friday price, minus 10%?"
4. Curiosity + benefit: "Why your code is not on the website"
5. Story: "I made a code for people who already cook on titanium"

Resend niet-openers:
1. "You missed this: 5 free gifts with every order"
2. "In case it got buried: up to 70% off"
3. "Still cooking on coated pans?" (staat al)
4. "Report no. 25895, at Black Friday prices"
5. "Benjamin here, one more time"

Flash 24 u (alleen als echt):
1. "Today only: the Wok Pan Pro at $X"
2. "24 hours. One pan."
3. "Tomorrow it goes back to $Y"
4. "Which pan would you cook with tonight?"
5. "The pan for Thanksgiving, today only"

Gifts als deadline:
1. "5 free gifts, one order"
2. "The gifts end with Black Friday"
3. "$555 in gifts with every order" (alleen US)
4. "What comes in the box, besides the pan"
5. "Gift #5 is new this week" (cookbook, alleen als nieuw voor de lezer)

Eindpush (bestaand, 06): "Black Friday ends tomorrow", "Last day: up to 70% off", "Final hours", "Last email: Black Friday ends tonight".

---

## 6. Top 5 deze week (8 tot 14 nov)

1. **Resend-regel invoeren** (Homestead): na elke verkoopcampagne R-a niet-openers met nieuw onderwerp (+24 à 48 u) en vanaf E4 R-b openers zonder klik. Eerste: R-b op E4 op ma 9 nov. Segmenten bouwen: "ontvangen X, niet geopend/geklikt, geen order sinds".
2. **VIP weekend 1 (13 tot 15 nov) laten besluiten door Floris**: percentage (10% voorstel), doelgroep (kopers + E30), unieke Klaviyo-code per profiel met vervaldatum zo 23:59 ET, en of het stapelt met HI10/BFCODE (voorstel: niet). Twee mails: vr aankondiging, zo 18:00 laatste uren.
3. **Gifts als echte deadline in elke campagne**: regel "Your 5 free gifts end when Black Friday ends." in hero-subregel of preview van E5 tot E10. Kost niets, is waar.
4. **Officiële regels voor de wekelijkse filtertrekking** (en de "Win your order back"-trekking) laten publiceren met sluitmoment zondag 23:59 ET en AMOE. Daarna wordt "Order by Sunday to be in this week's filter draw" een wekelijkse echte deadline. 4 nov liet zien dat dit het sterkste haakje is ($0,171 US).
5. **Eindtijd 30 nov en flash-momenten vastleggen**: Floris geeft eindtijd + tijdzone (voor aftelklok 29 en 30 nov) en zegt of er echte 24-uurs flash-deals komen op 12 en 19 nov. Zonder ja: die slots vullen met v2-proof of v2-letter, zonder deadline.

## 7. Besluiten nodig van Floris

1. VIP weekend: ja/nee, percentage, doelgroep, stapelen, twee weekenden (13 tot 15 en 26 tot 29 nov)?
2. Flash-deals 12 en 19 nov: welk product, welke prijs, en gaat de prijs echt terug na 24 uur?
3. Eindtijd en tijdzone 30 nov; mag een aftelklok (bijv. via een gif-dienst) in campagnes van 29 en 30 nov?
4. Regels voor de filtertrekking publiceren (pagina + link in footer)?
5. Mag Homestead de resend-regel (R-a en R-b) op alle verkoopcampagnes toepassen, en wie bouwt de segmenten?
