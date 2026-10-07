# Overzicht voor Floris · geldlekken en open vragen

Stand 7 oktober 2026. Samengevoegd uit alle agent-rapporten in research/ (cro, payments, beleid, lijst, reviews-okendo, deep, timing, tailoring, testing, potentie, copy, qa). Bedragen zijn schattingen per maand; ze overlappen deels en zijn niet op te tellen.

---

## Deel 1 · Vandaag doen (risico, geen keuze)

| # | Wat | Waarom | Wie |
|---|---|---|---|
| 1 | Kortingscodes uitzetten: `98347983474334593` (99%, geen limiet, sinds 6 okt 5x gebruikt, $1.656 weg), `SRJACEP6YNN1` + kopie (100%), `SJHNDFJNSAD934` (100%) | Iedereen die ze vindt krijgt gratis producten | Floris (of Claude na jouw "ja") |
| 2 | Ook dicht: EXTRA30, SK25, B2B25, LABOR20, BFEXTRA10 (7.626x gebruikt), NYEXTRA10, NTWDHPKL5C | Lekken korting en verstoren de codetests | Floris / Claude na akkoord |
| 3 | "Risk-free purchase"-blok op alle PDP's ("cook 30 days, full refund, free returns") gelijktrekken met het beleid, of het beleid aanpassen | Belofte die service weigert: 519 tickets in 180 dagen, FTC-risico (16 CFR 239) | Floris / developer |
| 4 | Nep-urgentie van de PDP: countdown die elke sessie op 02:42 begint, "few units left" bij 1.098 op voorraad, "Local warehouse / Express from the US" | Refunds, chargebacks ("merchant misrepresentation"), FTC | Developer |
| 5 | Campagnes niet meer naar de hele lijst, Smart Sending altijd aan | Spam bij Outlook 0,31% (juli 0,50%), grens is 0,3%; blokkade kost $50k tot $70k per maand | Wie de campagnes verstuurt (Homestead?) |

---

## Deel 2 · Waar we geld missen (geschat per maand)

### Site en checkout (bron: research/cro)
| Lek | Geschat | Kern |
|---|---|---|
| PDP naar winkelwagen | $55k tot $110k | Pan Pro Standard: 155k sessies, 76% bounce, 5,3% add-to-cart. Plakken (grootste bezwaar) niet beantwoord boven de vouw |
| Checkout naar betaald | $40k tot $70k | 3.739 onbetaalde checkouts per maand, $867k cartwaarde |
| Winkelwagen naar checkout | $35k tot $68k | 53,5% van de carts wordt geen checkout; ticket: set $499 werd $699 in checkout |
| Nep-urgentie en onware beloftes | $20k tot $45k | Minder refunds en chargebacks als het eerlijk is |
| Europa | $25k tot $50k (of minder verspilde ads) | Italië 0,15%, Duitsland 0,27% conversie; orderbevestiging noemt btw/invoerrechten terwijl de site "free shipping worldwide" zegt |
| Paid search op blogpagina's | $20k tot $40k | 24.463 sessies landen op blog/content; `/cfv6` (4.281 sessies) geeft 404 |
| Kortingslek | $10k tot $20k marge | Zie deel 1 |
| Post-purchase upsell (Aftersell) | $15k tot $25k | Aanbod bij maar 44% van de orders, één funnel |
| Pot Set 6-Pcs op draft | onbekend | Verkocht $32k in 30 dagen, pagina geeft nu 404 |

### Betalen (bron: research/payments)
Aanwezig: Shop Pay, Apple Pay, Google Pay, Shop Pay Installments (US, sinds maart, 5% van US-omzet), Affirm, Klarna (UK/EU), PayPal.
| Lek | Geschat | Kern |
|---|---|---|
| Australië zonder termijnbetaling | $3,4k tot $9,1k | Checkout afgerond 45% (US 53%); carts boven A$350 kopen 13% (US 33%); 18% betaalt met PayPal. Advies: Afterpay via Cross Border, en PayPal Pay Later-messaging (gratis) |
| Canada zonder termijnbetaling | kleiner dan AU | Afgerond 38%. Zelfde stap, 4 weken na AU |
| UK: Klarna toont niets op de PDP | klein | Script staat in theme maar rendert niet |
| US: termijnregel te weinig zichtbaar | +0,5 tot +2% US | Ook in cart drawer en mails tonen |
| Android Chrome, Samsung Internet, iOS Chrome | onderdeel van checkout-lek | 34 tot 39% afgerond; Google Pay bijna ongebruikt (19 orders tegen 431 Apple Pay) |
| Klarna-omzet zakte | onbekend | $35.755 in januari naar $1.158 in september |

### Beleid en vertrouwen (bron: research/beleid, research/deep)
| Lek | Geschat | Kern |
|---|---|---|
| Koprisico (plakken) niet afgedekt | $30k tot $80k (deep) | 25% van retourredenen is plakken, 27% trial-verwachting; 47 Trustpilot-reviews noemen "scam" |
| Tegenstrijdige beloftes | zit in bovenstaande | "lifetime" op /pages/warranty en PDP's, "100 days" en "Zero Risk" in ads, retourkosten: 98x "klant betaalt" en 108x "gratis" in tickets |
| Macro 249761 zegt "coating" | vertrouwen | 213x gebruikt, ondermijnt "no coatings" |

### Reviews (bron: research/reviews-okendo)
| Lek | Geschat | Kern |
|---|---|---|
| Reviews met twijfelachtige herkomst | risico | Loox: 19 dubbele teksten onder andere namen; snijplank: 4 van 5 reviews om exact 00:00 met namen die nergens bestaan. FTC 16 CFR 465 |
| Scores tegenstrijdig | conversie | Okendo 4,80, Loox 4,2 (die ziet Google), Trustpilot 3,93; Google-data bevat nog "lifetime", "scratch-resistant", "nutrients" |
| Reviews beantwoorden de vragen niet | conversie | Kopers vragen materiaal, maat, herkomst, schoonmaken, deksels; 0 reviews over potten, 0 over de sets bij naam |

### E-mail en lijst (bron: research/lijst, research/potentie, research/tailoring)
| Lek | Geschat | Kern |
|---|---|---|
| Flows onder benchmark | +$1M per jaar (basis) | Flows 10,8% van omzet; welcome $0,70 per ontvanger tegen $2,65 gemiddeld |
| Mails niet op maat | onderdeel van flows | Schort-, plank-, potten-, deep pan- en pizza steel-kopers kregen pan-mails (~95 tot 360 mensen per week per fout) |
| Deliverability | $50k tot $70k bij blokkade | Frequentie verdubbeld sinds september, 82% van spamklachten van niet-klikkers, DMARC p=none met rapporten naar mijndomein |
| Pop-up-lijst | lage opbrengst | 21% koopt binnen 24 uur, daarna nog maar 2,8% in 30 dagen; 16% schrijft zich binnen 30 dagen uit |

---

## Deel 3 · Open vragen (op volgorde van belang)

### A. Nu beslissen
1. Mag ik de kortingscodes uit deel 1 (punt 1 en 2) uitzetten in Shopify? Ja of nee.
2. Retourbeleid: kies (a) huidig beleid helder, (b) "Learn it in 30 days" (coaching, daarna vervanging of terugbetaling, ~$6.300 per maand extra kosten, quitte bij +0,7% conversie), of (c) 30 dagen ook gebruikt retour (~$22.500 per maand, quitte bij +2,6%). Advies: (b), eerst als 50/50-test.
3. Retourzending ongebruikt product: betaalt de klant of is het gratis?
4. Mag de standaard-doelgroep voor campagnes "Engaged 90 Days" plus recente kopers worden, maximaal 4 marketingmails per 7 dagen?
5. Mogen de ~77.000 nooit-betrokken profielen in delen van 10.000 per week onderdrukt worden?

### B. Geld en betalen
6. Wat zijn de echte marge en landed cost per pan en per set? (Alle breakevens hangen hiervan af; nu aangenomen 65 tot 83%.)
7. Mag er een Afterpay-account (US, Cross Border voor AU en CA) worden aangevraagd, en wie tekent?
8. Wat zijn je Shopify Plus-tarieven (kaart, internationaal, valutaconversie) en het tarief van Shop Pay Installments?
9. Waarom draait de Affirm-app naast Shop Pay Installments (dat ook door Affirm loopt)? Is er een contract met minimum?
10. Mag "or 4 interest-free payments of $33.50" in de mails, alleen in markten waar het kan?
11. Klarna zakte van $35.755 (jan) naar $1.158 (sep): minder EU-verkeer of een instelling?

### C. Site en producten
12. Welke 6-delige set-listing blijft ($349 BDAY, $399/$349 hoofdlisting, $449 SB met 510 orders)?
13. Pot Set 6-Pcs staat op draft maar verkoopt $32k per maand: weer actief zetten?
14. De Mini kost nu $99 en de Small $127: klopt dat?
15. Mag de Loox-score uit de Google structured data, en de oude productbeschrijvingen met "lifetime", "scratch-resistant", "nutrients", "naturally non-stick" eraf?
16. bestpansreviewed.com: van wie is die site en mag die zonder vermelding blijven?
17. Live chat-test (+12%, 92% kans beter): laten lopen tot 14 dagen en dan uitrollen? En de "Upgrade & Save"-test (-16%) stoppen?

### D. Vertrouwen en bewijs
18. Heb je een materiaalcertificaat van het kookoppervlak? (Een review met XRF-meting zegt RVS 321.)
19. Waar komen de Okendo- en Loox-reviews vandaan (import, migratie)? Stuur een Okendo CSV-export en een Loox-export, of zet `api.okendo.io` in de toegestane domeinen.
20. Mag support op elke review van 1 tot 3 sterren antwoorden?
21. Staan de ads met "100 days", "Zero Risk" en "lifetime" nog live in Meta?
22. Valt een deuk door een val onder de garantie? (Warranty-pagina zegt nee, guidance en mail N1 zeggen ja.)
23. Geldt de 75-year warranty ook voor schort en molen?
24. De wekelijkse filtertrekking: zijn er actievoorwaarden en "No purchase necessary"? Zonder die voorwaarden gebruiken we de trekking niet in mails.
25. Is de Forbes-vermelding echt (artikel, datum)?

### E. Deliverability en lijst
26. Wie beheert de DNS bij mijndomein? Mogen we een eigen DMARC-rapportadres instellen en Google Postmaster Tools en Microsoft SNDS koppelen?
27. Mailen Shopify-notificaties en Gorgias als @siraatskitchen.com?
28. Kan Alia een tweede stap met één vraag tonen ("What brings you here?") en het antwoord naar Klaviyo sturen? Kunnen we Alia-leestoegang krijgen?
29. Wie stuurt de campagnes met Smart Sending uit naar de hele lijst (Homestead "HS"-campagnes)?

### F. Flows en copy
30. Benjamins echte verhaal: één moment uit het begin, waarom van snijplank naar pan, liefst met foto. Leest hij de replies echt?
31. De chef uit de video: naam, functie, en mogen we hem citeren?
32. "Pure titanium cooking surface" of "titanium cooking surface"?
33. E-book-knop: `/products/e` (product van $50) of `/products/the-green-e-guide-free` (gratis)?
34. Aparte tracking-mail bij verzending (de oude had 29,8% klik)?
35. Review-verzoek na 14 of 30 dagen na levering? (Advies 14.)
36. Akkoord op de UGC-oproep "first egg" in P2 (15% voor een foto)?
37. Gewicht van de Pan Pro Standard (voor de rij "lichter dan gietijzer" in de vergelijking)?
38. Roasting Pan-pagina zegt nog "Lifetime warranty" en "100-day trial": eerst aanpassen voordat we er met een NEW-sticker naartoe linken.
39. De AI-flitsbeelden voor 16 hero's: akkoord? Dan mag PLAYBOOK ook AI-beelden in deze stijl toestaan.
40. Unieke codes aanmaken in Klaviyo (C4, K3, B2, P3, R2, R2-VIP, V1, N2): gedaan of zal ik je erdoorheen loodsen?

### G. Definitief flowplan v4 (klaviyo/flows/v4-flow-system.md)
41. C1 en K1 na 30 minuten in plaats van 1 uur (data: na 15 minuten koopt bijna niemand meer vanzelf). Akkoord?
42. C2 en K2: "1 dag later" (kan 's nachts vallen) of altijd "wacht tot 09:00"? Advies: 09:00.
43. HI10 in de vroege mails laten staan bij livegang en in fase 2 testen met en zonder HI10 (test T03)? Advies: ja.
44. Geen aparte HI10-tak voor lijstleden in de laatste mails (anders gaat er bijna geen unieke code meer uit). Akkoord?
45. Hoe lang blijft de $349 BDAY-listing van de 6-delige set live? Acht mails linken ernaar.
46. Stuurt Shopify al een verzendmail met tracking? Zo niet, dan voegen we P1b toe.
47. Anniversary-flow: ook een eenmalige mail voor klanten die hun eerste jaar al voorbij zijn?
48. Welcome in fase 3: holdout-test en een unieke welkomstcode van 10 dagen testen?

### Al beantwoord (7 okt)
6-delige set in mails $349 · gifts "with every order" · e-book link /products/e · compare-at Pan Pro $439 klopt · unieke codes akkoord, max 1 keer per persoon · Affirm en Shop Pay zijn actief.
