# Quiz-popup met angles: samenvattend advies (8 nov 2026)

Bronnen: strategie.md, copy.md/copy.json, meten-ab.md, welkomflow-per-angle.md. Niets is aangepast in Klaviyo, Alia of Shopify.

## Advies
Doen, maar in stappen.
1. Popup: eerst één vraag die je alleen aantikt, dan het e-mailveld. Favoriete vraag: "What made you look today?". Vier angles: PFAS-free, een non-stick die niet afbladdert, makkelijker dan rvs/gietijzer, en cadeau. Plus "Just looking" om over te slaan. Family safety valt af, want dat is hetzelfde motief als PFAS-free.
2. Aanbod: voor iedereen gelijk (5 gifts, $555 value, free shipping, kans op de filter). Per angle veranderen de kop, de bewijsregel en welk gift voorop staat. Geen code op het bedankscherm (besluit 31 okt).
3. Bewijsregel: "7 in 10 of our customers told us toxin-free cookware mattered most" (71% van 3,358 antwoorden). Niet "70% kwam daarvoor" en niet "#1 reason".
4. Meten: Alia A/B, controle tegenover quiz, 50/50, 21 dagen plus 14 dagen uitrijpen. Hoofdmetric is de omzet binnen 14 dagen per bezoeker die de popup zag; het aantal inschrijvingen is een vangrail. Start na de triggertest en na BFCM (2 dec), in januari met 10% holdout.
5. Profielveld: `siraat_goal` (non_toxic, performance, replace_coating, gift, other), plus `siraat_goal_first`, `siraat_goal_at` en `siraat_goal_source`.
6. Welkomflow: één flow met een split op `siraat_goal` en een fallback voor "geen antwoord" (de huidige flow). Mails per tak: non-toxic 6, performance 7 (de switch-tak gebruikt dezelfde mails), cadeau 5. Eerst live: alleen W1 per angle (ongeveer 80% van de omzet van de reis).

## Verwachting (schatting)
- Popup: tussen min 10% en plus 15% omzet per bezoeker. De betrouwbare data laat weinig verschil zien tussen een popup met één stap en een met meerdere stappen.
- Welkomflow per angle: plus 14 tot 28% omzet per subscriber, ongeveer $3,500 tot $7,000 per week.

## Open punten voor Floris
- Checken in de Alia-editor of elk antwoord een eigen vervolgscherm kan krijgen. Zo niet, kan Klaviyo-forms met vertakking de uitwijk zijn (nog checken).
- Officiële voorwaarden voor de winactie met de filter.
- Verzenddeadline voor de cadeau-tak; cadeauverpakking bestaat niet op de site.
