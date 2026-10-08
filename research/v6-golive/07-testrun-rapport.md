LIVE: JA, NA DEZE 5 FIXES

# Testrun v5-flows · 8 oktober 2026 (avond)

Testrun-agent. Echte mails uit TEST-kopieën van de flows naar lolagroothuis+<alias>@gmail.com, gecontroleerd door de monitor-agent (`08-monitor-log.csv`, Slack #claude-mail). Wat niet echt kon, is getest als PREVIEW: de template is in Klaviyo gerenderd met realistische eventdata (template-render API, niets verzonden) en daarna gecontroleerd met `scripts/qa_inbox.py mail` (rapporten in `previews/`).

Testopzet: `test-flows.csv` (13 + 1 kopieën, allemaal live, alleen voor profielen met `siraat_test = true` en "lolagroothuis" in het e-mailadres; wachttijden 3 tot 4 minuten). De 13 echte v5-flows staan nog op Draft (gecontroleerd). Er is geen enkele mail uit een TEST-flow naar een ander adres gegaan (watcher op Received Email, 0 lekken). Scenario's per alias: `test-scenarios.csv`. Testcode: `test-code.md`.

## 1. Scenario, verwachte mail, ontvangen, checks

Checks (monitor-agent, 15 controles per mail): elke echte mail heeft dezelfde vijf systeemfouten uit de header en footer (zie fix 1). In de tabel staat "OK" als er verder niets mis is.

| Scenario (alias) | Verwachte mail | Ontvangen | Checks |
| --- | --- | --- | --- |
| Eerste order, pan, US (+order) | P1-FIRST | ja 19:40 | systeemfouten; deksel-notitie ontbreekt (siraat_owned leeg) |
| idem | P2-SAFE | ja 19:45 | systeemfouten; GIF 559 KB (let op) |
| idem | CODE · P3-PAN | ja 19:56 | systeemfouten; cross-sell leeg; dekselknop zonder 28 cm-variant; code THX- werkt (10%) |
| idem | R1, R2 (winback), N1, N2 (anniversary) | NEE | order viel vlak na het aanmaken van de flows (zie 4.1); opnieuw met +order2 |
| Order 1, Crêpe Pan Pro (+vip) | P1-FIRST, P2-SAFE, N1, R1-PAN · kook | ja | systeemfouten; cross-sell leeg in N1 en R1 |
| idem, na order 2 | P3 en N2 stoppen, winback start opnieuw | ja (P3/N2 niet verstuurd, tweede R1 19:54) | gedrag klopt |
| Order 2 met code (+vip) | CODE · V1, V2 | ja 19:59 | systeemfouten; REG-code vervalt 8 okt 2027 i.p.v. na 14 dagen; V2 kwam vóór V1 (testartefact); P.S. in V2 noemt HI10 na de 15%-code |
| idem | CODE · R2-VIP | ja 20:06 | systeemfouten; code heeft in Shopify geen einddatum, mail zegt "ends Oct 11"; cooldown niet te toetsen (testartefact) |
| Sunset (+sunset, trigger via testlijst) | S1, S2 | ja | systeemfouten |
| Sunset kept (+sunsetkept, testlijst) | S3, S4 | ja | systeemfouten |
| Welcome US variant A (+welcome, testlijst) | W1-A, W2, W3, W4-US, W5 | W1 t/m W4-US ja, W5 onderweg | systeemfouten; codebalk W1 toont "10%%"; W2 "our The Green Clean E-Guide" |
| Welcome US variant B (+welcomeabtb) | W1-B, W2, W3, W4-US, W5 | W1 t/m W3 ja, rest onderweg | systeemfouten |
| Welcome UK (+welcomeint) | W1-A, W2, W3, W4-INT, W5 | W1 t/m W4-INT ja | systeemfouten; W4-INT doorgestreepte £498 bij de set (let op) |
| Checkout per product (pan, set, schort, plank, gift card, US-only, eigenaar met deksel) en land (UK, AU, CA, EU, SG, NZ, HK, onbekend) | C1 t/m C4 | GEBLOKKEERD, PREVIEW | zie 3 |
| Cart (pan, accessoire, nocode, UK) | K1/K1-ACC, K2, K3 | GEBLOKKEERD, PREVIEW | zie 3 |
| Browse (pan A/B, accessoire, nocode) | B1 A/B, B1-ACC, B2 | GEBLOKKEERD, PREVIEW | zie 3, plus fix 3 |
| Site abandonment | A1, A2 | GEBLOKKEERD, PREVIEW | zie 3 |
| Levering, UGC | P2, U1 | geen Delivered-event, PREVIEW | zie 3 |

## 2. Blokkerende fouten en de fix

1. **Header en footer in alle Klaviyo-templates zijn de oude versie** (elke mail): ABOUT linkt naar /pages/faq, oude Facebook-URL, footer toont "SIRAATSKITCHEN", lockup onzichtbaar in geforceerde dark mode, afmeld- en webversielink 2.4:1 contrast (brick op #282828). De partials in de repo zijn al aangepast (nog niet gecommit). Fix: templates opnieuw bouwen en exporteren (`export_klaviyo.py --live`) en in elke flow de mails opnieuw aan de template koppelen (flowmails zijn kopieën), daarna één mail per flow controleren.
2. **Coupon-vervaltijden kloppen niet met de mailtekst**: SK_REGULARS15_14D (V1) gaf een code die pas op 8 okt 2027 vervalt; R2_VIP_15_72H gaf een code zonder einddatum in Shopify terwijl de mail "ends Oct 11" zegt. Fix (Floris, Klaviyo > Coupons): bij alle 9 pools "expires after N hours/days after assignment" zetten. Zonder dit is de deadline in de mail niet waar.
3. **Browse: B2-CLICKED wordt nooit verstuurd.** De klik-split zoekt Campaign Name "B1 · T05a", maar Klaviyo heeft de A/B-varianten hernoemd naar "B1 Test #1 October 08, 2026 Variation A/B" (in WdRz5k en in de kopie). Campaign Name = berichtnaam (bevestigd: "CODE · V1", "CODE · P3-PAN" komen zo door). Fix: varianten in de UI hernoemen naar "B1 · T05a-A" en "B1 · T05a-B", of de split op "B1 Test #1" laten zoeken.
4. **W1 codebalk toont "YOUR WELCOME 10%%"** (beide varianten; W2 en later tonen 10%). Fix: in de W1-bron het dubbele procentteken weghalen, opnieuw exporteren.
5. **Checkout, cart, browse en site zijn niet echt doorlopen.** Vanuit deze omgeving weigert het netwerk static.klaviyo.com (onsite-tracking) en www.google.com (captcha in de Shopify-checkout); Shopify registreerde geen checkout met e-mail en Klaviyo kreeg geen events. Synthetische events via de API waren niet toegestaan. Fix: één echte ronde in een gewone browser (Floris of iemand met de aliassen uit `test-scenarios.csv`), of static.klaviyo.com en www.google.com toevoegen aan Allowed domains van de omgeving en dan draai ik de scenario's automatisch. De TEST-kopieën staan klaar.

## 3. Alleen als PREVIEW getest (template gerenderd, niets verzonden)

44 mails gerenderd met realistische data per markt (`previews/`): C1 voor pan, set, schort, plank, gift card, US-only set, eigenaar met deksel, UK, AU, CA, EU, SG, NZ, HK en onbekend; C2, C2-ACC, C3-S (US, UK), C3-P, C3-ACC, C4 nocode; K1 (US, UK), K1-ACC, K2-NEW, K2-RETURNING, K3 nocode; B1 A en B (US, UK), B1-ACC, B2-NOTCLICKED, B2 nocode; A1 (US, AU), A2; P2 (levering), U1; P1-REPEAT, P3-PAN nocode; R1-SET, R1-ACC.

- Bij alle 44: dezelfde systeemfouten als fix 1. Geen ongerenderde tags, geen em dash, grootte onder 102 KB, layout 375/600/1200 goed, valuta en verzendregel per markt goed (US, UK, AU, CA, EU, SG, NZ, HK).
- Let op: checkout met USD maar zonder profielland (bijv. Noorwegen, dat in USD afrekent) krijgt de US-versie ("Free shipping from the US", $70 in gifts). Zo ontworpen, maar fout voor die klanten.
- Let op: deksel- en maatregels tonen cm in US-mails (C1 eigenaar, P1-REPEAT, P3-PAN).
- Niet te renderen zonder echt profiel (coupon-tag): CODE · C4, CODE · K3, CODE · B2, alle CODE · P3 behalve PAN, CODE · R2, CODE · N2, V1 nocode, W0. Die zijn alleen lokaal getest (`exports/qa/inbox/templates-report.md`).
- Echte previewmails (create_template_preview_send_job) vragen een expliciete bevestiging van de gebruiker en zijn daarom niet verstuurd.

## 4. Wat verder opviel (niet blokkerend)

1. Een nieuwe flow pakt events in de eerste ongeveer 30 seconden na aanmaken of livezetten niet op (Winback en Anniversary misten de order van +order om 19:35:04). Bij livegang: nieuwe flow eerst aan, oude flow pas een paar minuten later uit.
2. Cross-sell is leeg zolang `siraat_owned` niet gevuld is (alle testprofielen, want de bezit-sync draait pas vannacht). Na de sync van 03:27 controleren of +order en +vip een gevulde lijst hebben; bij echte klanten op dag 21 (P3) en 45 (R1) is de sync allang gedraaid.
3. P3-PAN: knop "add the lid" opent de deksel zonder de 28 cm-variant.
4. Klaviyo's verzendwachtrij liep op tot 15 minuten (W4-US kwam 16 minuten na W3). Geen fout.
5. Testorders en de testcode niet annuleren of refunden; code LOLATEST na de testrun uitzetten; testkopieën, testlijsten (SpVeTG, XMcTr9, TFD68Z) en testprofielen opruimen na de post-purchase-ronde.
