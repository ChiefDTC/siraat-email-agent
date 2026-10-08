# 11 · Overstapplan oude live flows bij de v5-livegang

Opgesteld 8 oktober 2026 (avond). Alleen gelezen: Klaviyo-API (flowdefinities, templates, Received Email per flow en per bericht, 9 sept t/m 8 okt), Shopify Admin (ordertijdlijn, fulfilments, kortingscodes) en de repo. Niets gewijzigd in Klaviyo, Shopify of de templates. Berichtnamen uit Klaviyo met een lang streepje zijn hier met een punt of dubbele punt geschreven.

---

## 0. Samenvatting voor Floris

1. Verzending is veilig: Shopify stuurt elke klant de orderbevestiging en de 3PL (Ecomflow, ShipBob) stuurt via Shopify de verzendmail met trackingnummer (27 van 28 gecontroleerde orders). Die blijven altijd; geen enkele oude Klaviyo-mail heeft echte tracking.
2. Het echte gat zit in het **gratis e-book**: v5 P1 linkt naar de productpagina `/products/e` (oude Green Clean E-Guide), niet naar een download. Alleen FREE E-GUIDE (YyaMjx) en E-Book (TSUnLs) hebben een echte downloadlink. **YyaMjx blijft live tot de P1-knop naar de echte download wijst** (tekst in 3.2).
3. P1 zegt niets over verwerkingstijd en levertijd. Data: mediaan 3,2 dagen tot verzending, 80% binnen 8 dagen (het beleid zegt "1 business day"). Voorgestelde Engelse regel in 3.2.
4. Middle East delay (SxN86d) uit: AE-orders worden gewoon verzonden en de beloofde code THANKYOU10 bestaat niet in Shopify.
5. Mystery Gift Reveal (WvRupU) verstuurt sinds 21 september niets meer (trigger op een verwijderd product). Laten liggen of op Draft; niemand mist iets dat nu nog aankomt.
6. Pan Education: pan-tak uit (dubbel met P1, P2, P2-SAFE, U1). Cutting Board-tak blijft, na het weghalen van twee verouderde beeldblokken ("100-DAY TRIAL", "UP TO 56% OFF").
7. Winback UEfh4h blijft tot 14 december live met twee flowfilters, zodat kopers van vóór de livegang hun winback nog krijgen. Daarvoor moet code GOODFOOD tot dan actief blijven (staat op de lijst met lekcodes).
8. Triple Pixel-flows uit bij groep A (verouderde claims: 30,000, 100-DAY TRIAL, COOK10). Daarna binnen een week een v5-vangnet-kloon met de Triple Pixel-trigger (zie 7).
9. Blijven ongewijzigd: E-Gift Card, Back in Stock, de drie CS-meldingen, Pan Flash Buyers, Review request XzHrez. Trustpilot Vixr6X gaat 12 oktober uit zoals gepland.

---

## 1. Wat Shopify en de 3PL zelf sturen (blijft altijd)

Bewijs: tijdlijn van 28 recente verzonden orders (GraphQL `order.events`), 25 van vóór 6 okt plus de 3 nieuwste.

| Mail | Afzender | Wanneer | Bereik in de steekproef | Inhoud |
|---|---|---|---|---|
| Order confirmation | Shopify | direct na bestelling | 27 van 28 (de missende: Apple Pay-order #SIRAAT107808, geen e-mailevent) | regels, totaal, adres. In Europa staat er een zin over mogelijke VAT en invoerrechten (zie `research/cro/03-checkout-audit.md`) |
| Order edited | Shopify | na een Aftersell-upsell | waar van toepassing | gewijzigde order |
| Shipping confirmation | Ecomflow-Siraatkitchen of ShipBob Fulfillment, via Shopify | bij de fulfilment met trackingnummer | 27 van 28 | vervoerder, trackingnummer, link (USPS, GOFO, YTO, NZ Couriers enz.) |
| Out for delivery, Delivered | ShipBob Fulfillment | onderweg en bij aflevering | alleen ShipBob-orders (in de steekproef 1 keer gezien) | status |

Belangrijk om te weten:
- De gratis digitale regels (Plastic-Free Home E-Book, Giveaway entry, Free Shipping) worden als aparte fulfilment zonder tracking afgesloten. Shopify stuurt daarvoor **geen** aparte mail met de download. De download komt nu alleen uit Klaviyo (YyaMjx, TSUnLs).
- Alle Klaviyo-mails hier, ook P1 en YyaMjx, zijn marketingmails (`transactional: false`). Uitgeschreven kopers krijgen ze niet. YyaMjx bereikte 4.436 mails tegen 5.261 orders in 30 dagen. Robuuster (optioneel, Shopify): de downloadlink ook in Shopify > Settings > Notifications > Order confirmation zetten.

---

## 2. Cijfers: Received Email laatste 30 dagen (9 sept t/m 8 okt)

| Flow | Mails 30 d | Flow | Mails 30 d |
|---|---|---|---|
| T2SmtR Failure to launch | 112.637 | SwkMyn Cart | 9.357 |
| SiaNLu Welcome | 70.902 | S7V4a7 Sunset | 7.600 |
| RL3TU6 Post Purchase | 18.960 | Y2TmNB Checkout | 5.321 |
| UEfh4h Winback | 15.283 | YyaMjx FREE E-GUIDE | 4.436 |
| TyEjuQ Browse Triple Pixel | 14.181 | TSUnLs E-Book | 4.407 |
| Wj6x6V Browse | 13.713 | Tsg2tV Checkout Triple Pixel | 3.263 |
| YcXbHx Pan Education | 11.771 | Vixr6X Trustpilot | 2.666 |
| WvRupU Mystery Gift Reveal | 9.777 (sinds 21 sept 0 nieuwe instromers) | TBWngE Cart Triple Pixel | 1.278 |
| WsQDYu Back in Stock | 56 | SxN86d Middle East delay | 39 |
| UYALJ8 E-Gift Card, Wn2tsq Pan Flash, XzHrez Review | 0 | TLHht3, UcGzaL, Y4a7fJ | alleen interne meldingen |

Placed Order in dezelfde 30 dagen: 5.261.

Verzendsnelheid (Fulfilled Order, `FulfillmentHours`, orders met pan of set, 2.164 fulfilments sinds 8 sept):

| Markt | n | Mediaan | 80% binnen | 95% binnen |
|---|---|---|---|---|
| Alle | 2.164 | 77 uur | 197 uur | 278 uur |
| US | 1.319 | 77 | 200 | 277 |
| AU | 315 | 75 | 202 | 276 |
| SG | 120 | 69 | 169 | 269 |
| CA | 103 | 120 | 231 | 284 |
| GB | 89 | 72 | 175 | 240 |
| AE | 56 | 149 | 290 | 353 |

Het verzendbeleid (`content/facts/site-pages-and-policies.md`) zegt "processed within 1 business day"; Gorgias-macro 246877 zegt 3 tot 5 dagen. De data passen bij de macro, niet bij het beleid. Levertijd volgens beleid: 6 tot 10 dagen (Singapore 6 tot 8, Ierland en Denemarken 8 tot 14).

---

## 3. (a) Verzend-, vertraging- en gratis-productinformatie: wat moet blijven en waar komt het vandaan

### 3.1 Per soort informatie

| Informatie | Nu (oud) | Straks | Oordeel |
|---|---|---|---|
| Orderbevestiging | Shopify + RL3TU6 "We've Got Your Order" (alleen beelden) | Shopify + v5 P1 (1 uur) | gedekt |
| Tracking / verzonden | 3PL-verzendmail + RL3TU6 "Your Package Is On Its Way" (vaste wachttijd dag 3 of 4, géén trackingnummer, knop naar /apps/parcelpanel, zegt "We've packed and wrapped it" terwijl de helft dan nog niet verzonden is) | 3PL-verzendmail; P1 zegt "Tracking link by email as soon as it ships" | gedekt; de oude mail is niet nodig en deels onwaar |
| Onderweg / bijna daar | YcXbHx Email 1 "about to arrive" (trigger Postflows In Transit, inhoud = verzorgingstips) | 3PL-verzendmail; ShipBob "out for delivery" | gedekt voor de status; tips zitten in P1 en P2 |
| Verwerkingstijd en levertijd per markt | nergens (ook niet in de oude mails) | **ontbreekt in P1** | toevoegen aan P1 (tekst 3.2) |
| Vertraging | SxN86d (Midden-Oosten, onjuist geworden) | P2-SAFE dag 17 "Has your order not arrived yet ... reply with your order number" | gedekt voor de lange staart; SxN86d uit |
| Levering, eerste gebruik | RL3TU6 "Unlocking the Non-Stick" (na Fulfilled Order), YcXbHx | v5 P2 (levering +1 dag), P2-SAFE, U1 | gedekt |
| Zendingsproblemen (exception, mislukte bezorging, afhaalpunt) | TLHht3, UcGzaL, Y4a7fJ: interne melding naar CS | ongewijzigd | blijven live |
| E-book (Plastic-Free Home E-Book) | YyaMjx (download via Shopify Digital Downloads), TSUnLs (download `/a/downloads/...`) | **P1 linkt naar productpagina `/products/e`** (oude "The Green Clean E-Guide", verkoopbaar product, geen download) | **gat**: YyaMjx blijft tot P1 is aangepast |
| Mystery Gift (dishwasher sheets) | WvRupU onthulde het; sinds 21 sept dood | P1: "The mystery gift travels in the box" | geen regressie; optionele regel in 3.2 |
| Giveaway entry (PFAS-waterfilter) | niet in oude mails | P1 gift-blok: "your order is entered for a chance to win" | gedekt |
| Cadeaubon | Shopify stuurt de bon; UYALJ8 bedankt de koper | ongewijzigd | blijft |
| Back in stock | WsQDYu | ongewijzigd | blijft |

### 3.2 Wat er in v5 P1 bij moet (concrete Engelse tekst; templates niet gewijzigd)

**1. E-book-knop naar de echte download.** In `klaviyo/templates/v3/post-purchase/p1-first.html` (2 knoppen) en `p1-repeat.html` (2 knoppen) de url `https://siraatskitchen.com/products/e?...` vervangen door de echte downloadlink, met dezelfde utm-parameters. Kandidaten die nu in de live mails staan:
- `https://delivery.shopifyapps.com/-/396da74b7735ff7f/6d8678add81ad2ad` (YyaMjx, Shopify Digital Downloads)
- `https://siraatskitchen.com/a/downloads/-/c3223546db2107ef/49618d950a4222f5` (TSUnLs)

Floris controleert eerst welke link het **Plastic-Free Home E-Book** opent (de huidige gift; de oude titel "The Green Clean E-Guide" hoort bij `/products/e`). Via de proxy kon ik de bestanden niet openen. Knoptekst mag blijven: "Download your e-book". Gift-blok-notitie blijft: "The e-book is yours today."

**2. Blok "When to expect it"** (onder "WHAT HAPPENS NEXT", vervangt de regel "We pack and check it"):

US:
> **When to expect it.** Most orders leave our warehouse within 3 to 6 business days. Delivery then takes 6 to 10 days. Your tracking link arrives by email the moment it ships, and the first tracking update can take 24 to 72 hours to show. Free shipping from the US.

Buiten de US:
> **When to expect it.** Most orders leave our warehouse within 3 to 6 business days. Delivery then takes 6 to 10 days in most countries, 8 to 14 to Ireland and Denmark. Your tracking link arrives by email the moment it ships, and the first tracking update can take 24 to 72 hours to show. Free shipping, duties paid.

Als macro: `{{IF:US}}...{{ELSE}}...{{ENDIF}}` (de marktlogica bestaat al via `{{SHIP}}`). Floris bevestigt "3 to 6 business days" (data: mediaan 3,2 dagen, 80% binnen 8 kalenderdagen) of past het beleid aan; dan beleid, macro en mail gelijk.

**3. Optioneel, tegen "I got sheets, not a gift"-tickets (34 van 400)**, als P.S. in P2 en P2-SAFE (niet in P1, daar is het bewust een verrassing):
> P.S. The mystery gift in your box is a pack of our plastic-free dishwasher sheets. Your pan is dishwasher safe, so they have a job from day one.

**4. Bekend gat in de v5-opbouw** (geen tekst, wel melden): X3ySuU heeft herinstap 30 dagen. Wie binnen 30 dagen twee keer bestelt, krijgt bij de tweede order geen P1 en dus geen e-booklink. Shopify-bevestiging en 3PL-tracking komen wel. Acceptabel, omdat het e-book hetzelfde is.

### 3.3 Volgorde e-book

| Moment | YyaMjx FREE E-GUIDE | TSUnLs E-Book |
|---|---|---|
| Groep B live, P1 nog met `/products/e` | **BLIJFT LIVE** (enige echte download). Wel twee beeldblokken weghalen: "SIRAAT PRIME TIME SALE \| UP TO 56% OFF" en "45% off on our bestselling Titanium Hammered Cookware Set Pro" | UIT (Draft). Dubbel met YyaMjx en noemt het e-book "mystery gift", terwijl de echte mystery gift sheets zijn |
| P1 aangepast en live (link getest) | UIT (Draft) | blijft uit |

---

## 4. Tabel per flow

Groepen en tijden volgen `03-golive-draaiboek.md` (vrijdag 9 okt: A 14:00, B 15:15, C 16:15 of maandag).

| Flow | Trigger | Advies | Wanneer | Reden |
|---|---|---|---|---|
| SiaNLu EB Welcome | lijst Uw8eZG | UIT BIJ LIVEGANG GROEP A | 14:00 | v5 Welcome T4a5Mk (T01-oud pad zit daarin) |
| Y2TmNB EB Checkout | Checkout Started | UIT BIJ LIVEGANG GROEP A | 14:00 | v5 Checkout QUBUQV |
| SwkMyn EB Cart | Added to Cart | UIT BIJ LIVEGANG GROEP A | 14:00 | v5 Cart TZG9Mx |
| Wj6x6V EB Browse | Viewed Product | UIT BIJ LIVEGANG GROEP A | 14:00 | v5 Browse WdRz5k |
| Tsg2tV Checkout Triple Pixel | Checkout Started TP | UIT BIJ LIVEGANG GROEP A | 14:00 | verouderde claims (30,000+, 100-DAY TRIAL, 56% OFF); vangnet volgt (sectie 7) |
| TBWngE Cart Triple Pixel | Added to Cart TP | UIT BIJ LIVEGANG GROEP A | 14:00 | idem, plus code COOK10 (lekcode) en filter op SwkMyn |
| TyEjuQ Browse Triple Pixel | Viewed Product TP | UIT BIJ LIVEGANG GROEP A | 14:00 | ~75% overlapt al met Wj6x6V (zelfde mail twee keer); verouderde claims |
| T2SmtR Failure to launch | lijst Uw8eZG | FILTER TOEVOEGEN, blijft live | vóór 14:00 | voorwaarde uit `01-segmenten-audit.md` bevinding 2 (zie 6.4) |
| RL3TU6 EB Post Purchase | Placed Order | UIT BIJ LIVEGANG GROEP B | 15:15 | v5 P1 + 3PL-tracking dekken alles; oude mails noemen "100 Days to Try Us Out" en "100-DAY TRIAL" |
| YyaMjx FREE E-GUIDE | Placed Order | BLIJFT LIVE tot P1 is aangepast, dan uit | eerst blokken weghalen (vóór 15:15) | enige echte e-bookdownload |
| TSUnLs EB E-Book | Placed Order met Mystery Gift / E-Guide | UIT BIJ LIVEGANG GROEP B | 15:15 | dubbel met YyaMjx; verwarrende "mystery gift"-naam |
| YcXbHx EB Pan Education | Postflows Shipment In Transit | ALLEEN DEZE BERICHTEN UIT (pan-tak); Cutting Board-tak BLIJFT na opschonen | 15:15 | zie 6.1 |
| WvRupU Mystery Gift Reveal | Ordered Product ProductID 15675410415956 (product bestaat niet meer) | UIT BIJ LIVEGANG GROEP B (Draft, administratief) | 15:15 | stuurt sinds 21 sept niets; huidige Mystery Gift heeft ID 15785445622100. Herstel alleen als apart besluit (6.2) |
| SxN86d Middle East delay | Placed Order, split op profielland | UIT BIJ LIVEGANG GROEP B (mag nu al) | 15:15 | zegt "outbound shipments are briefly paused"; 62 AE-orders zijn sinds 8 sept verzonden. Code THANKYOU10 bestaat niet in Shopify |
| UEfh4h EB Customer Winback | Placed Order | FILTER TOEVOEGEN, blijft live tot 14 dec, dan Draft | 15:15 | zie 6.3 |
| S7V4a7 EB Sunset | segment XY4NVp | UIT BIJ LIVEGANG GROEP C | met TbYQmX | anders vier afscheidsmails |
| UYALJ8 E-Gift Card | Placed Order met E-Gift Card | BLIJFT LIVE | | bedankmail koper; Shopify stuurt de bon. v5 heeft niets eigens |
| WsQDYu Back in Stock | Subscribed to Back in Stock | BLIJFT LIVE | | v5 heeft geen BIS; geen overlap |
| TLHht3 Shipment Exception (CS) | Postflows 6 | BLIJFT LIVE | | interne melding naar biggunservice123@gmail.com |
| UcGzaL Delivery Attempt Failed (CS) | Postflows 7 | BLIJFT LIVE | | idem |
| Y4a7fJ Ready for Pickup (CS) | Postflows 8 | BLIJFT LIVE | | idem; de klantmail erin staat op Draft en blijft zo |
| Wn2tsq Pan Flash Buyers | segment YbCB68, alleen US | BLIJFT LIVE | | 0 mails in 30 dagen, eenmalige CS-flow; geen overlap |
| XzHrez Review request | Delivered Shipment +14 d | BLIJFT LIVE | | onderdeel van het nieuwe systeem |
| Vixr6X Trustpilot | segment Yx4ain | gaat 12 okt uit (gepland) | 12 okt | niet vervroegen |

---

## 5. Tabel per bericht

Mails = Received Email in 30 dagen. "Uit met flow" = de flow gaat op Draft, berichten hoeven niet apart.

| Flow | Bericht-ID | Naam (onderwerp) | Status | Mails | Advies | Reden |
|---|---|---|---|---|---|---|
| RL3TU6 | SPaYdU | 1st time buyer, Multiple (We've Got Your Order) | live | 2.373 | uit met flow, groep B | v5 P1 |
| RL3TU6 | Vp4qSX | 1st time buyer, Single (We've Got Your Order) | live | 974 | uit met flow | v5 P1 |
| RL3TU6 | UwgBb7 | Purchased other collection (We've Got Your Order) | live | 870 | uit met flow | v5 P1 |
| RL3TU6 | U98PFG | 2nd time buyers (Welcome Back) | live | 490 | uit met flow | v5 P1-REPEAT |
| RL3TU6 | QUeA2U, X6wxL3 | Founder's Note (A note from Benjamin) | live | 3.380 / 842 | uit met flow | Benjamin-verhaal zit in P1 en welcome |
| RL3TU6 | Y6xS2a | 100 Day-Trial (100 Days to Try Us Out) | live | 3.334 | uit met flow | in strijd met DECISIONS (30-day returns) |
| RL3TU6 | Y8Nn9B, Tse2up, Xg94tJ | IT'S ON ITS WAY (Your Package Is On Its Way) | live | 3.319 / 805 / 481 | uit met flow | vaste wachttijd, geen tracking; 3PL-verzendmail is de echte |
| RL3TU6 | XaMN6w | GET READY TO COOK (Unlocking the Non-Stick) | live | 2.093 | uit met flow | v5 P2 / P2-SAFE |
| YyaMjx | XtYsPr | E-Guide Flow (Your E-Guide Is Ready) | live | 4.436 | BLIJFT LIVE tot P1-fix; twee beeldblokken weg | enige echte download |
| TSUnLs | SvpV7D | Your Mystery Gift Is Here | live | 3.160 | uit met flow, groep B | dubbel met YyaMjx |
| TSUnLs | XtL9Mq | Open Your Mystery Gift | live | 842 | uit met flow | idem |
| TSUnLs | YjAsnx | Don't Forget Your Gift | live | 407 | uit met flow | idem |
| YcXbHx | VVxZpH | Pan Education 1 (about to arrive) | live | 3.381 | ALLEEN DIT BERICHT UIT | P1 heat-tip, 3PL-tracking; "100-DAY TRIAL" |
| YcXbHx | X4Pk75 | Pan Education 2 (The #1 mistake that makes titanium stick) | live | 1.653 | ALLEEN DIT BERICHT UIT | zelfde boodschap en bijna zelfde onderwerp als v5 P2 |
| YcXbHx | XXRDsv | Pan Education 5 (5 things that will shorten your pan's life) | live | 1.557 | ALLEEN DIT BERICHT UIT | P2 "looking after it", U1 |
| YcXbHx | RzJb6Z | Pan Education 3 (changing color) | live | 1.548 | ALLEEN DIT BERICHT UIT | P2 "heat tint" |
| YcXbHx | TiT2Ni | Pan Education 6 (over a week cooking) | live | 1.622 | ALLEEN DIT BERICHT UIT | U1 en review XzHrez |
| YcXbHx | XtJ7me | Pan Education 4 (right way to clean) | live | 1.676 | ALLEEN DIT BERICHT UIT | P2 |
| YcXbHx | W8quz8 | Pan Education 7 | draft | 0 | laten | |
| YcXbHx | UJMq2j | Cutting Board Education 1 (Almost Here) | live | 173 | BLIJFT LIVE na opschonen | v5 heeft geen plankverzorging |
| YcXbHx | QTNBVJ | Cutting Board Education 2 (FAQs) | live | 171 | BLIJFT LIVE na opschonen | idem |
| WvRupU | Y3G6Km, U6yi6c, SynbCN, SpGUYn | Mystery Gift 1/4 t/m 4/4 | live | 1.576 / 2.042 / 2.703 / 3.456 (laatste instromer 20 sept) | uit met flow (Draft) | trigger dood; verkoopmails abonnement |
| SxN86d | TT4XEG | Shipping Update Regarding Your Order | live | 39 | uit met flow | onjuist en code bestaat niet |
| UEfh4h | Wrnas5 | Email 1 (Serving Up New Must-Haves) | live | 5.117 | FILTER TOEVOEGEN (op flow), banner weg | lopende kopers afmaken |
| UEfh4h | XWQLLB, WW78hc | Email 2 en kopie (We Cut a Deal for You, code GOODFOOD) | live | 2.594 / 2.501 | idem | GOODFOOD tot 14 dec actief laten |
| UEfh4h | WC4V9Y | Email 3 (10% Off Expires Tonight) | live | 5.071 | idem | idem |
| UYALJ8 | VmBygA | Thanks for Gifting | live | 0 | BLIJFT LIVE | |
| WsQDYu | Scuk9u | You're On The List | live | 54 | BLIJFT LIVE | |
| WsQDYu | Rrh2Qh | It's Back | live | 2 | BLIJFT LIVE | |
| TLHht3 | VP9FZa | intern: Shipment Exception | live | | BLIJFT LIVE | |
| UcGzaL | UasiYN | intern: Delivery Attempt Failed | live | | BLIJFT LIVE | |
| Y4a7fJ | S3Rq7E / R245LY | intern: Ready for Pickup / klantmail | live / draft | | BLIJFT zoals het is | |
| Wn2tsq | QQyigU / XT8PNy | Credit or Refund? / Email 1 | live / draft | 0 | BLIJFT zoals het is | |
| XzHrez | WWGnBW | Review request (A/B) | live | 0 (nieuw) | BLIJFT LIVE | |
| Vixr6X | SfeWhr | How was your experience? | live | 2.666 | 12 okt uit | gepland |
| Y2TmNB | R4g5Wr, RpzC3U, RZ4Urm, XWU6HU, Yjpp3E, U3byfW, SRuuaP, SZuXUJ, S9QbcN, Xbtxpg | checkout 1 t/m 5 (A/B) | live | 5.321 samen | uit met flow, groep A | v5 Checkout |
| Tsg2tV | X37MuT, VGsrUf, XjBNHW, TE8MmA, VYWt9i | TP checkout 1 t/m 4 | live | 3.263 samen | uit met flow, groep A | sectie 7 |
| SwkMyn | W7cyzk, URatk6, SY7jud, STu58P, UBgGhU | cart 1 t/m 3 | live | 9.357 samen | uit met flow, groep A | v5 Cart |
| TBWngE | VWL44n, SUi5iD, SYVjE3, Shh2G2, REfY5p | TP cart 1 t/m 3 | live | 1.278 samen | uit met flow, groep A | sectie 7 |
| Wj6x6V | Y7wqBq, WUsPxr | browse 1 (A/B) | live | 13.713 samen | uit met flow, groep A | v5 Browse |
| TyEjuQ | Vm6cZj, Wwv3Tb | TP browse 1 (A/B) | live | 14.181 samen | uit met flow, groep A | sectie 7 |
| SiaNLu | U473Qm, V427ZY, Rs6ATL, SrZF5p, XUgzX9, RxYqFv, X99646, VW5f2C | welcome 1 t/m 5 en Additional 1 t/m 3 | live | 70.902 samen | uit met flow, groep A | v5 Welcome |
| T2SmtR | S6wMyn, U6PsqR, RifeeX, WFwksy, WFZ9ka, RA3fUx, RgzVJY, WwCjFD, S5P3Wn, SmQwfi | FTL 1 t/m 10 | live | 112.637 samen | BLIJFT, met voorwaarde | alleen het oude welcome-pad (6.4) |
| S7V4a7 | TdxnHR, UyjuhX | sunset 1 en 2 | live | 7.600 samen | uit met flow, groep C | v5 Sunset |

---

## 6. Speciale gevallen

### 6.1 (b) Pan Education YcXbHx: pan-tak tegen Cutting Board-tak

Opbouw: trigger "Postflows · Shipment In Transit". Split 1: Placed Order in 30 dagen met een pan in Items. JA = pan-tak (6 live mails over ~15 dagen). NEE = split 2: Collections bevat Cutting Board. JA = board-tak (2 mails). Iemand met pan en plank zit dus altijd in de pan-tak.

- **Pan-tak uit**: alle zes onderwerpen (verwarmen, de "#1 mistake", kleurverandering, schoonmaken, levensduur) staan in v5 P1 (heat first), P2 en P2-SAFE (vijf stappen, heat tint, baking soda, vaatwasser) en U1. Mail 2 heeft bijna hetzelfde onderwerp als v5 P2. Alle pan-mails dragen de balk "FREE SHIPPING | 100-DAY TRIAL" en "PRIME TIME SALE | UP TO 56% OFF".
- **Board-tak blijft**: ~170 mails per maand, alleen plankkopers zonder pan. v5 geeft hen alleen P1 (algemeen) en P3-ACCESSORY op dag 21. Inhoud is gebruik en schoonmaak, geen verkoop. Voorwaarde: twee beeldblokken weg.

Klikstappen (groep B, 15:15):
1. Flows > zoek "EB | Pan Education" > open.
2. Klik op de mailkaart "Pan Education | Email 1" > in het linkerpaneel bij **Status** (Live) kies **Draft** > bevestig. Herhaal voor Email 2, 5, 3, 6 en 4 (Email 7 staat al op Draft). Profielen in de pan-tak slaan deze mails over; de flow zelf blijft **Live**.
3. Klik op "FLOW: Cutting Board Education | Email 1" > **Edit email** (of Edit content) > klik op het bovenste beeld "SIRAAT PRIME TIME SALE | UP TO 56% OFF" > prullenbak (Delete block). Scroll naar onder > beeld "FREE SHIPPING | FREE SHIPPING | 100-DAY TRIAL | MADE WITH LOVE" > Delete block > **Save** > terug naar de flow. Zelfde voor "Cutting Board Education | Email 2".
4. Preview van beide board-mails met een echt profiel (Preview > profiel zoeken) en controleren dat er nergens "100-day" of "56%" staat.

### 6.2 Mystery Gift Reveal WvRupU

Trigger is Ordered Product met ProductID `15675410415956`; dat product bestaat niet meer in Shopify. De huidige "Mystery Gift" in elke order heeft ID `15785445622100`. Reveal-mail 1 had 1.066 tot 1.070 verzendingen per week tot half september en 0 sinds de week van 21 september; de laatste vervolgmails liepen uit tot 4 oktober. Er gaat dus nu al niets meer uit.

Advies: bij groep B op **Draft** (statusmenu rechtsboven > Draft), zodat niemand per ongeluk de trigger herstelt naast v5. Wil Floris de onthulling terug: dan alleen mail 1 (reveal) met trigger-ID 15785445622100 en een verzendfilter "Received Email where Flow equals X3ySuU zero times in the last 2 days", en mail 2 t/m 4 (abonnementsverkoop) op Draft. Beter nog: de P.S.-regel uit 3.2 punt 3 in P2 en P2-SAFE.

### 6.3 (c) Winback-gat UEfh4h

Probleem: v5 Winback UyFc78 start alleen bij orders na de livegang (R1 op dag 45). Kopers van ~26 juli t/m 9 oktober zitten nu in de 60-dagenwacht van UEfh4h. Gaat UEfh4h uit, dan krijgen zij geen winback (~5.100 mensen per maand).

Advies: UEfh4h **live laten met twee flowfilters** en op **14 december** naar Draft (laatste instromer 9 okt + 60 + 3 dagen = ~11 december).

- Filter 1: Placed Order zero times **after 9 oktober 2026**. Wie na de livegangsdag nog eens bestelt, valt uit de oude flow (die zit in v5). Gekozen "na 9 okt" en niet "na 8 okt", zodat kopers van vrijdagochtend (vóór 15:15, nog niet in v5) hun winback houden.
- Filter 2: Received Email where Flow equals **UyFc78** zero times over all time. Vangt de kopers van vrijdagmiddag (na 15:15 in zowel oud als v5): zij krijgen v5 R1 op dag 45 en vallen daarna uit de oude flow.

Voorwaarden:
- **GOODFOOD blijft actief tot 14 december.** Mail 2 en 3 noemen die code in het beeld. GOODFOOD staat in `exports/GO-LIVE.md` stap 0 op de lijst van lekcodes. Kies: GOODFOOD pas op 14 dec uit, of mail 2, kopie en 3 op Draft en alleen mail 1 (bestsellers, geen code) laten lopen.
- In alle vier de mails het beeld "SIRAAT PRIME TIME SALE | UP TO 56% OFF" verwijderen (Edit email > blok > Delete > Save).
- Weet dat deze mails deels in BFCM (20 nov t/m 6 dec) vallen, naast de campagnes. Acceptabel bij dit volume; anders bij de BFCM-bevriezing UEfh4h al op Draft.

Klikstappen (groep B, 15:15, in plaats van UEfh4h op Draft):
1. Flows > "EB | Customer Winback | 5/8/25" > open > klik op de **Trigger**-kaart > **Flow filters** > **Add a filter** (of Edit filters).
2. Definition: **What someone has done (or not done)** > **Placed Order** > **zero times** > tijdvak **after** > datum **Oct 9, 2026** (staat er geen "after": **between** Oct 10, 2026 en Dec 31, 2027).
3. **AND** > **What someone has done (or not done)** > **Received Email** > **zero times** > **over all time** > **Add filter** (where) > **Flow** > **equals** > "v4 · Winback" (UyFc78).
4. **Save**. Flow blijft Live. Agenda: 14 december statusmenu > Draft.
5. Claude controleert na het opslaan via de API dat beide filters in `profile_filter` staan.

Alternatief bekeken en afgeraden: v5 Winback met "Add past profiles" vullen. De v5-mails lezen het verzendland en de items uit de order van het triggerevent; bij terugwerkende instroom krijgt iedereen tegelijk R1, zonder de 45-dagenlogica.

### 6.4 T2SmtR Failure to launch (blijft live)

Gebruik de voorwaarde uit `01-segmenten-audit.md` bevinding 2, niet die uit GO-LIVE stap 8: die laatste sluit ook alle huidige inschrijvers uit (SiaNLu-berichten heten "EB [DG] | Email #..", niet "Old · Welcome").
1. Flows > "EB | Failure to launch" > split direct na "Wait 30 days" > Edit.
2. **AND** > **What someone has done** > **Received Email** > **zero times** > **in the last 60 days** > where **Flow equals "v4 · Welcome"** (T4a5Mk) **and Campaign Name doesn't contain "Old ·"** > Save. Vóór 14:00.

Let op (los van de livegang): 6 van de 10 FTL-mails dragen nog de balk "100-DAY TRIAL" of "Lifetime", en alle 10 "UP TO 56% OFF". Die blokken verwijderen hoort bij dezelfde schoonmaak.

---

## 7. (d) Triple Pixel-flows: bereik zonder Shopify-event

Feiten:
- TyEjuQ (browse TP) is met 14.181 mails groter dan Wj6x6V (13.713). Het heeft geen filter op het Shopify-event Viewed Product, dus ~75% van de ontvangers krijgt dezelfde "we saw you looking"-mail ook uit Wj6x6V. Na groep A dekt v5 Browse die 75%.
- Echt extra bereik (audit 01, 36 uur): 182 cart-profielen zonder Shopify Added to Cart, 32 checkout-profielen zonder Shopify Checkout Started, ~25% van de TP-viewers zonder Viewed Product. Grofweg 120 cart, 20 checkout en 100 tot 150 browse per dag.
- Inhoud van de drie TP-flows: "SIRAAT PRIME TIME SALE | UP TO 56% OFF", "Rated 4.9/5 by 30,000+ Customers", "FREE SHIPPING | 30,000 HAPPY CUSTOMERS | 100-DAY TRIAL", code COOK10 (lekcode). Laten lopen betekent dus verouderde en onjuiste claims naast v5.
- Het Triple Pixel-event "Checkout Started" heeft dezelfde vorm als het Shopify-event (Items, extra, line_items). "Viewed Product - TP" lijkt op het klaviyo.js-event (Name, ProductID, ImageURL, URL, Price). "Added to Cart - TP" heeft een eigen vorm (Product Name, items) en vuurt ook op de automatisch toegevoegde Mystery Gift.

Advies:
1. **Groep A: alle drie uit** (Draft), in dezelfde minuut als de rest.
2. **Binnen een week een v5-vangnet**, na "ga" van Floris, door Claude via de API als Draft:
   - "v5 · Checkout · TP-vangnet": kopie van QUBUQV zonder T01-split (100% v5), trigger Checkout Started - Triple Pixel (RtgBgs), flowfilters: Checkout Started (RfMvni) zero times since starting this flow; Received Email where Flow equals QUBUQV zero times in the last 3 days; Placed Order zero times since starting this flow. Templates zijn dezelfde (vorm gelijk).
   - "v5 · Browse · TP-vangnet": kopie van WdRz5k, trigger Viewed Product - TP (V48nhq), filters: Viewed Product (XNtYMB) zero times in the last 1 day; Received Email where Flow equals WdRz5k zero times in the last 7 days; plus de triggerfilter tegen Giveaway, E-Guide, E-Book, Mystery Gift (`02-segmenten-foutenjacht.md` bevinding 14). Eerst met een testprofiel de productblokken controleren.
   - Cart TP pas als de Added to Cart-TP-vorm in de cart-templates getest is (andere eigenschapnamen); tot die tijd geen vangnet voor cart.
   - De T01-meting blijft zuiver: beide armen van de A/B-test zijn Shopify-getriggerd, het vangnet raakt alleen de rest.
3. Alternatief als Floris liever niets nieuws bouwt: TP-flows uit en het verlies accepteren (orde 15 cart-mails per dag die nu echt verstuurd worden; TBWngE haalde 1.278 mails in 30 dagen).

---

## 8. Klikstappen per type actie (Klaviyo-UI)

**Hele flow uit (UIT BIJ LIVEGANG GROEP X)**: Flows > zoek de naam > open > statusmenu rechtsboven (Live) > **Draft** > bevestigen. Niet archiveren (PLAYBOOK §7). Lopende profielen krijgen geen mails meer.

**Alleen dit bericht uit**: flow openen > klik op de mailkaart > linkerpaneel **Status** > **Draft** > bevestigen. De flow blijft Live; profielen slaan de mail over en lopen door.

**Filter toevoegen (flowfilter)**: flow openen > klik op de **Trigger**-kaart > **Flow filters** > **Add a filter** of **Edit** > voorwaarde > **Save**. Een flowfilter wordt bij instap en vóór elke stap opnieuw gecontroleerd.

**Beeldblok weghalen**: mailkaart > **Edit email** (of Edit content) > klik op het beeld > prullenbak > **Save**. Daarna **Preview** met een echt profiel.

### Volgorde op vrijdag 9 oktober

| Tijd | Actie |
|---|---|
| vóór 14:00 | T2SmtR-voorwaarde (6.4). YyaMjx: twee beeldblokken weg. Cutting Board-mails: twee beeldblokken weg. UEfh4h: banner weg in vier mails |
| 14:00 groep A | Draft: SiaNLu, Y2TmNB, Tsg2tV, SwkMyn, TBWngE, Wj6x6V, TyEjuQ |
| 15:15 groep B | Draft: RL3TU6, TSUnLs, WvRupU, SxN86d. Pan Education: 6 pan-mails op Draft (flow blijft Live). UEfh4h: twee flowfilters (blijft Live). YyaMjx blijft Live |
| 16:15 of ma 12 okt, groep C | Draft: S7V4a7 (zelfde minuut als TbYQmX en Wzz6xC live) |
| zodra P1 de echte downloadlink heeft (getest) | Draft: YyaMjx |
| 12 okt | Vixr6X uit (gepland) |
| 14 dec | UEfh4h Draft; GOODFOOD uit |

Rollback groep B (aanvulling op `03-golive-draaiboek.md` 5.4): RL3TU6 en TSUnLs weer Live; de pan-mails in YcXbHx weer Live; UEfh4h-filters weghalen. SxN86d en WvRupU niet terugzetten.

---

## 9. Controle na livegang (Claude, alleen lezen)

- Na 1 uur en na 24 uur: Received Email per `$flow` voor RL3TU6, TSUnLs, YcXbHx (alleen UJMq2j en QTNBVJ mogen nog), WvRupU, SxN86d = 0; YyaMjx > 0 tot de P1-fix.
- Vijf verse kopers: per koper Shopify-bevestiging, P1, YyaMjx (tot de fix) en verder geen oude naflow.
- UEfh4h: na 24 uur nog verzendingen voor oude kopers, geen enkele ontvanger met een order na 9 okt.
- Na de P1-fix: klik op de e-bookknop in een testmail opent het Plastic-Free Home E-Book als download.

## 10. Open punten voor Floris

1. Welke downloadlink hoort bij het Plastic-Free Home E-Book (3.2 punt 1)?
2. "3 to 6 business days" akkoord, of het verzendbeleid ("1 business day") aanpassen?
3. GOODFOOD tot 14 dec laten staan, of winback-mail 2 en 3 nu al uit?
4. "Ga" voor de twee TP-vangnetflows (checkout en browse) na de eerste testweek?
5. Optioneel: e-booklink ook in de Shopify-orderbevestiging, zodat uitgeschreven kopers het ook krijgen.
