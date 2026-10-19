# Figma: Siraat · Alle e-mails (okt 2026)

Link: https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=1-2

Doel: overzicht voor een nieuwe designer (statics/ads). Elke rij is één flow, mails van links naar rechts in de volgorde waarin een klant ze krijgt; onderaan campagnes en merk-bouwstenen. Stand 12 oktober 2026, alleen wat live is in Klaviyo (status read-only gecontroleerd via de API, alle 14 flows `live`).

Werkwijze: live template-HTML per flow-actie via GET /api/templates/{id}, lokaal gerenderd met de Django-engine uit qa_render (research/tailoring/test, kltags) en voorbeelddata (Sarah, US; samples co_/atc_/vp_/po_; K1 v2 met golive k1v2-event; W4-INT met UK-profiel), beelden lokaal gecachet, screenshot 600 px breed, volle lengte, modus light via scripts/qa_mail_shots.js. Identieke templates (bijv. nocode · cooldown en nocode · T02-B) zijn samengevoegd tot één render met de andere namen in het label. Oude 'Old ·'-mails (50/50- en 90/10-tests) niet opgenomen. Kortingscodes in tekst gemaskeerd als XXXXXXXX; codes die in een herobeeld zijn gebakken (welkomstcode in de heroband) staan er nog wel in.

Screenshot van het geheel: `research/figma/alle-emails-overzicht.png` (verkleind, origineel canvas 9664 x 48009 px).

## Rijen

### Rij 1 · v4 · Welcome (T4a5Mk), 8 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=2-2) · Trigger: Inschrijving op de lijst (Alia-pop-up "Card Game"). 50/50 tegen de oude welcome. Nieuw: W1 bewijs + welkomstcode (A/B), W2 Benjamin, W3 test, W4 per markt, W5 reviews.

- **W0 · al klant (vertakking)**: na 5 min. Onderwerp: Thank you. Now the first egg.
- **W1 · A/B variant A**: na 5 min. Onderwerp: No PFAS. Here's the paper. And 10%.
- **W1 · A/B variant B**: na 5 min. Onderwerp: No PFAS. Here's the paper. And 10%.
- **W2**: na 5 min + 1 d (10:00). Onderwerp: The pan nobody else was making
- **W3**: na 5 min + 1 d (10:00) + 2 d (09:00). Onderwerp: Has your cookware been tested?
- **W4-US**: na 5 min + 1 d (10:00) + 2 d (09:00) + 3 d (09:00). Onderwerp: Who are you cooking for?
- **W4-INT**: na 5 min + 1 d (10:00) + 2 d (09:00) + 3 d (09:00). Onderwerp: Who are you cooking for?
- **W5**: na 5 min + 1 d (10:00) + 2 d (09:00) + 3 d (09:00) + 4 d (09:00). Onderwerp: Tammy is on her fourth pan

### Rij 1b · W1 v2 voorstel (13 okt)
[Naar het voorstel](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=25-2) · Frame "W1 v2 proposal (Oct 13)" direct onder rij 1 (node 25:2). Voor Floris: drie keer welkomstmail 1 naast elkaar, labels met timing, onderwerp, preview en twee regels "what changed" (uit research/v6-golive/20-welcome-analyse.md). Niet in Klaviyo.

- **W1 · current (variant A)**: kopie van de render uit rij 1. Onderwerp: No PFAS. Here's the paper. And 10%.
- **Old · Welcome 1** (template YrrJiM): live template via GET /api/templates en Klaviyo template-render (Sarah), 600 px 2x. Onderwerp: `{{ first_name }}`, Thanks For Joining Us. Code zit in de beelden.
- **W1 v2 · proposal**: klaviyo/templates/v3/welcome/w1-v2-preview.html, 600 px 2x, volle lengte, code in tekst gemaskeerd. Onderwerp: `{{ first_name }}`, here's your 10%.

### Rij 2 · v4 · Browse abandonment (WdRz5k), 5 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=2-66) · Trigger: Product bekeken, niet in cart. 90% nieuw sinds 12 okt. B1 A/B op onderwerp, B2 alleen wie in B1 klikte krijgt een eigen code (code/nocode-test T02).

- **B1 · A/B (A en B)**: na 1 u. Onderwerp: Get this pan with 10% off | Why I started making this pan
- **B1-ACC**: na 1 u. Onderwerp: Looked twice? Here's the detail.
- **B2-CLICKED · pan nocode · cooldown** (ook: B2-CLICKED · pan nocode · T02-B, B2-CLICKED · acc nocode · cooldown, B2-CLICKED · acc nocode · T02-B): na 1 u + 2 d (09:00). Onderwerp: "I ordered one pan to try it out"
- **CODE · B2-CLICKED · pan** (ook: CODE · B2-CLICKED · acc): na 1 u + 2 d (09:00). Onderwerp: Your own 10% expires in 48 hours
- **B2-NOTCLICKED**: na 1 u + 2 d (09:00). Onderwerp: Skeptical? So were they.

### Rij 3 · v4 · Cart abandonment (TZG9Mx), 6 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=2-111) · Trigger: Added to Cart, geen checkout. 90% nieuw sinds 12 okt. K1 v2 (cartpagina, sinds 10 okt). Eerste korting pas in K3 (eigen 10%, 48 uur).

- **K1 v2 (cartpagina)**: na 15 min. Onderwerp: The hammered pattern: an easy wipe
- **K1-ACC**: na 15 min. Onderwerp: Picked it out? It's still here.
- **K2-RETURNING**: na 15 min + 2 d (08:00). Onderwerp: Adding to your Siraat kitchen?
- **K2-NEW**: na 15 min + 2 d (08:00). Onderwerp: 15 coated pans, or one
- **K3 · pan nocode · cooldown** (ook: K3 · pan nocode · T02-B, K3 · acc nocode · cooldown, K3 · acc nocode · T02-B): na 15 min + 2 d (08:00) + 2 d (09:00). Onderwerp: What if it's not for you?
- **CODE · K3 · pan** (ook: CODE · K3 · acc): na 15 min + 2 d (08:00) + 2 d (09:00). Onderwerp: We're removing your discount

### Rij 4 · v4 · Checkout abandonment (QUBUQV), 8 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=2-163) · Trigger: Checkout gestart, niet betaald. 90% nieuw sinds 12 okt. Gifts vooraan, welkomstcode automatisch in C1 t/m C3, C4 eigen code of geen code.

- **C1**: na 10 min. Onderwerp: Your cart + 4 gifts are still pending
- **C2**: na 10 min + 1 d (08:30). Onderwerp: Has the pan in your cart been tested?
- **C2-ACC**: na 10 min + 1 d (08:30). Onderwerp: Yours, or a gift? Both work.
- **C3-S**: na 10 min + 1 d (08:30) + 2 d (09:00). Onderwerp: What's in the box with your set
- **C3-P**: na 10 min + 1 d (08:30) + 2 d (09:00). Onderwerp: One pan, or three?
- **C3-ACC**: na 10 min + 1 d (08:30) + 2 d (09:00). Onderwerp: The pan we made after the board
- **C4 nocode · cooldown** (ook: C4 nocode · T02-B): na 10 min + 1 d (08:30) + 2 d (09:00) + 2 d (09:00). Onderwerp: Last email about your cart
- **CODE · C4**: na 10 min + 1 d (08:30) + 2 d (09:00) + 2 d (09:00). Onderwerp: We're removing your discount in 48 hours

### Rij 5 · v4 · Site abandonment (VLGhbR), 2 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=2-228) · Trigger: Op de site geweest, niets bekeken. Twee mails, geen korting: eerst het idee, dan bewijs van 100,000+ klanten.

- **A1**: na 2 u. Onderwerp: Four eggs or five?
- **A2**: na 2 u + 2 d (09:00). Onderwerp: Where 100,000+ customers started

### Rij 6 · v4 · Post-purchase + levering (X3ySuU · VQ93sx), 14 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=3-2) · Trigger: Placed Order (X3ySuU) en Delivered Shipment (VQ93sx). P1 na 1 uur, P2 de dag na levering, P2-safe dag 17 als nog niet geleverd, P3 dag 21 cross-sell per product (code/nocode).

- **P1-FIRST**: na 1 u. Onderwerp: Good call. Here's what's coming.
- **P1-REPEAT**: na 1 u. Onderwerp: Good to see you again
- **P2 · levering (flow VQ93sx)**: 1 dag na levering (09:00). Onderwerp: The mistake that makes titanium stick
- **P2-SAFE**: na 1 u + 16 d (09:00). Onderwerp: When your pan arrives: the first egg
- **P3-SET nocode · cooldown** (ook: P3-SET nocode · T02-B): na 1 u + 16 d (09:00) + 4 d (09:00). Onderwerp: The pan your set is missing
- **P3-NEXT · deksel nocode · cooldown** (ook: P3-NEXT · eigenaar nocode · cooldown, P3-NEXT · deksel nocode · T02-B, P3-NEXT · eigenaar nocode · T02-B): na 1 u + 16 d (09:00) + 4 d (09:00). Onderwerp: How is the pan treating you?
- **P3-PAN nocode · cooldown** (ook: P3-PAN nocode · T02-B): na 1 u + 16 d (09:00) + 4 d (09:00). Onderwerp: Which lid fits your pan?
- **P3-ACCESSORY · kook nocode · cooldown** (ook: P3-ACCESSORY · acc nocode · cooldown, P3-ACCESSORY · kook nocode · T02-B, P3-ACCESSORY · acc nocode · T02-B): na 1 u + 16 d (09:00) + 4 d (09:00). Onderwerp: Now meet the pan
- **P3-APRON nocode · cooldown** (ook: P3-APRON nocode · T02-B): na 1 u + 16 d (09:00) + 4 d (09:00). Onderwerp: An apron deserves a pan
- **CODE · P3-SET**: na 1 u + 16 d (09:00) + 4 d (09:00). Onderwerp: The pan your set is missing
- **CODE · P3-NEXT · deksel** (ook: CODE · P3-NEXT · eigenaar): na 1 u + 16 d (09:00) + 4 d (09:00). Onderwerp: How is the pan treating you?
- **CODE · P3-PAN**: na 1 u + 16 d (09:00) + 4 d (09:00). Onderwerp: Which lid fits your pan?
- **CODE · P3-ACCESSORY · kook** (ook: CODE · P3-ACCESSORY · acc): na 1 u + 16 d (09:00) + 4 d (09:00). Onderwerp: Now meet the pan
- **CODE · P3-APRON**: na 1 u + 16 d (09:00) + 4 d (09:00). Onderwerp: An apron deserves a pan

### Rij 7 · UGC + Review request (VPixnJ · XzHrez), 2 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=3-115) · Trigger: Delivered Shipment (Shopify). U1 vraagt een foto van het eerste ei. Reviewmail zonder vaste header (logo in de hero), A/B op onderwerp, 4-5 sterren naar Trustpilot.

- **U1 · UGC first egg (VPixnJ)**: 4 dagen na levering (09:00). Onderwerp: Show us your first egg?
- **Review R1 kort, zonder header (A/B onderwerp)**: 14 dagen na levering (09:30). Onderwerp: Win your purchase amount back | How was your experience?

### Rij 7b · Mystery Gift v3 (concept, 19 okt), 4 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=39-2) · Frame "Mystery Gift v3 (concept, 19 okt)" direct onder rij 7 (node 39:2). Trigger: Ordered Product, ProductID 15785445622100 (OF ProductName equals "Mystery Gift"); vervangt WvRupU (Draft, dode trigger). Filters: rc_active_subscriber false of niet gezet, geen order met Dishwasher Sheets sinds start, nooit eerder in deze flow, nooit WvRupU ontvangen, geen refund in 30 dagen; elke mail slaat over als er in de laatste 2 dagen een X3ySuU-mail ging. Status: concept, niet in Klaviyo. Beelden: klaviyo/templates/v3/mystery/previews/m1 t/m m4-mobile-375.png (375 px, 2x). Spec: klaviyo/flows/mystery-gift-v3.md.

- **M1 reveal**: dag 3, 10:00. Onderwerp A: Let's reveal your mystery gift | B: What's in the small box in your order. Preview: It's not overstock. It's the other half of a no-coating kitchen.
- **M2 gebruik**: dag 12, 10:00. Onderwerp: The ten-second way to use your gift. Preview: One sheet where the pod goes. Half a sheet for a light load.
- **M3 aanbod**: dag 23, 10:00. Onderwerp A: Alright, here's the offer | B: 20% off every delivery, not just the first. Preview: Including the part most brands would leave out.
- **M4 laatste, optioneel**: dag 30, 10:00. Onderwerp: Last one from me about the dishwasher sheets. Preview: The price isn't going anywhere. These emails are.

### Rij 8a · v4 · Winback (UyFc78), 7 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=4-2) · Trigger: Bestelling, daarna 45 dagen stilte. R1 per product (set, pan, accessoire), R2 dag 75: 10% of 15% voor terugkerende klanten (code/nocode).

- **R1-SET**: na 45 d (09:00). Onderwerp: The shapes a set leaves out
- **R1-PAN · kook** (ook: R1-PAN · eigenaar): na 45 d (09:00). Onderwerp: How's your pan doing?
- **R1-ACC**: na 45 d (09:00). Onderwerp: Ready for the pan?
- **R2-VIP nocode · cooldown** (ook: R2-VIP nocode · T02-B): na 45 d (09:00) + 30 d (09:00). Onderwerp: You came back. Thank you.
- **CODE · R2-VIP**: na 45 d (09:00) + 30 d (09:00). Onderwerp: 15% exclusive discount, 72 hours
- **R2 nocode · cooldown** (ook: R2 nocode · T02-B): na 45 d (09:00) + 30 d (09:00). Onderwerp: Ready for pan number two?
- **CODE · R2**: na 45 d (09:00) + 30 d (09:00). Onderwerp: Your 10% expires in 72 hours

### Rij 8b · v4 · VIP (VTkxFL), 3 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=4-62) · Trigger: Tweede bestelling. V1 dag 30 (15% exclusive of zonder code), V2 dag 40: een vraag van Benjamin.

- **V1 nocode · cooldown**: na 30 d (09:00). Onderwerp: You're a VIP. Thank you.
- **CODE · V1**: na 30 d (09:00). Onderwerp: You're a VIP. Here's 15% off.
- **V2**: na 30 d (09:00) + 10 d (09:00). Onderwerp: A question from Benjamin

### Rij 8c · v4 · Anniversary (XbYT7T), 3 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=4-91) · Trigger: Eerste bestelling met kookgerei. N1 na 6 maanden, N2 na 1 jaar (15% of zonder code).

- **N1**: na 182 d (09:00). Onderwerp: Six months in. Anything worn off?
- **N2 nocode · cooldown**: na 182 d (09:00) + 183 d (09:00). Onderwerp: One year ago this week
- **CODE · N2**: na 182 d (09:00) + 183 d (09:00). Onderwerp: One year in. Here's 15% off.

### Rij 8d · v4 · Sunset + Sunset · kept (TbYQmX · Wzz6xC), 4 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=4-120) · Trigger: 120 dagen geen klik, bezoek of order. S1 en S2 vragen of we mogen blijven schrijven. Wie klikt, gaat naar Sunset · kept (S3, S4).

- **SUNSET · S1**: na 1 d (09:00). Onderwerp: Should we keep writing to you?
- **SUNSET · S2**: na 1 d (09:00) + 4 d (09:00). Onderwerp: Last email from me (unless you tap)
- **SUNSET-KEPT · S3 (Sunset · kept, Wzz6xC)**: na klik in sunset: na 30 min. Onderwerp: You're staying. Thank you.
- **SUNSET-KEPT · S4 (Sunset · kept, Wzz6xC)**: na klik in sunset: na 30 min + 4 d (09:00). Onderwerp: The pan we started with

### Rij 9 · Campagnes (recept-01), 2 mails
[Naar de rij](https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=4-156) · Trigger: Receptcampagne (Floris, 9 okt). Concept B: steak met brown butter mushroom pan sauce, Pan Pro Standard. Knoppen "Shop now" en "Shop the pan".

- **Recept 01 · Steak night · US**: US: verstuurd 9 okt. Onderwerp: Friday steak night, sauce included
- **Recept 01 · Steak night · INT**: INT: gepland 10 okt, geannuleerd (niet verstuurd). Onderwerp: Weekend steak night recipe, sauce included

### Rij 10 · Merk-bouwstenen

- Logo-lockups (brand/logo/lockup/): zwart op crème, wit op donker, e-mailformaten.
- Kleuren: paper #FFFFFF, cream #F8F7F2, sand #ECE7DD, hairline #E4DED3, ink #282828, charcoal #2B2929, espresso #321E1D, brick #AC3B19, titanium #C9C6C0, grijs #727272, legal #9A948B.
- Lettertypes: TT Ramillas Light Italic (koppen, altijd als PNG; niet in Figma geïnstalleerd, voorbeeld in fallback Instrument Serif Italic), Inter (lopende tekst), eyebrow en knopstijl.
- Header, footer, codebalk, knop, productkaart (K1 v2), gifts-blok, reviewkaart, vergelijking met PFAS-pan, codeblok, deadline-tegels, twee beloftes (uitsnedes uit de renders, 2x).
- Zes goedgekeurde flitsstijl-foto's uit content/media/ai-flash/ (v5, zonder de drie afgekeurde).

## Kanttekeningen

- Rij 8 (overige v5-flows) is opgesplitst in 8a Winback, 8b VIP (VTkxFL, dus niet site abandonment), 8c Anniversary, 8d Sunset + Sunset · kept. Site abandonment is VLGhbR (rij 5).
- Varianten met dezelfde HTML maar een ander voorbeeldproduct (bijv. pan of accessoire in K3, B2) zijn één keer gerenderd, met het panvoorbeeld.
- INT-receptcampagne is nooit verstuurd (geannuleerd 9 okt), staat er voor de volledigheid in.
- Renders zijn lokaal (Django), niet via Klaviyo's eigen template-render; kleine verschillen in Klaviyo-tags (unsubscribe-links, webview) zijn mogelijk.
