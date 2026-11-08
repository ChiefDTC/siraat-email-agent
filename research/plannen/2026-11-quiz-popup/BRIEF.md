# Brief: quiz-popup met angles + welkomflow per angle (Floris, 8 nov 2026)

Idee (Floris, na gesprek met Colin, die de e-mails voor Siraat doet): de popup stelt eerst een vraag zoals "What is your main goal?" met 4 of 5 angles die bewezen zijn in de post-purchase survey. Bijvoorbeeld "Ditch the toxins from my home", "Better performance from my cookware" of "It's a gift". Na de klik volgt een offer en tekst die bij dat antwoord past, zoals "70% of our customers came for the same reason: non-toxic cookware. Here is your offer." Daarna volgt een volledige welkomflow per gekozen angle. Alles moet A/B-testbaar en meetbaar zijn.

## Surveydata (anoniem, geaggregeerd, 22,160 antwoorden, 2025 tot mei 2026)
- Non-toxic / PFAS-free is in elke survey de nummer 1 driver (68 tot 76%). "What matters most": non-toxic 68%. "Most important": toxin-free ~70%, daarna effortless non-stick. "Value most when cooking": health & safety 76%. "Why did they buy": PFAS/microplastics vermijden 44%, plus titanium benefits.
- Pijn: oude coating die afbladdert/slijt 41%, zorgen over toxiciteit 27%.
- Vergeleken met: stainless steel 41%, daarna ceramic en cast iron.
- Voor wie: zelf 69% (7 tot 8 op 10), cadeau ~1 op 5, partner/familie de rest.
- Bezwaren: prijs 55% (open), "almost stopped": prijs 27%, maat/welk product 15%, "werkt titanium echt" 15%. ~47% vindt het "overpriced".
- 60% zocht al actief naar non-toxic/PFAS-free kookgerei (hoge intentie). 38% koopt op de dag van ontdekking.
- Ontdekking: Instagram + Facebook ~80%; in één survey leidt Google (42%).
- Held-product: Hammered Pan Pro (71%). Wens: meer titanium (potten, sets, bakeware) 44%.
- Eerst koken: eieren/ontbijt nummer 1, daarna steak en vis. Chefs: Jamie Oliver, Gordon Ramsay.
- Klanttaal: "Non stick without toxic coating", "You should try this instead of the toxic non-stick", "The peeling of non stick coatings", "Looking for something non toxic but easy to cook with at the same time".

## Context
- Repo: /home/user/siraat-email-agent. Lees eerst README.md, PLAYBOOK.md, DECISIONS.md en CLAUDE.md (merkregels).
- Popup is Alia (alia_popup props in Klaviyo). Er loopt al een trigger-A/B-test: research/popup/2026-11-trigger-test.md. OptiMonk laadt ook op de site.
- Klaviyo account TdtTzz. Huidige welkomflow: research/plannen/2026-11-welcome-audit.md en klaviyo/templates/v3/flows-nov/welcome/.
- Huidig aanbod: 5 gifts ($555 value), free shipping, kans op PFAS waterfilter (US). Retour 30 dagen, garantie 75 jaar, 100,000+ klanten, oprichter Benjamin.
- Vaste regels: nooit een em dash of en dash. Geen verzonnen claims of percentages; alleen surveycijfers die hierboven staan, en die eerlijk formuleren ("7 in 10 of our customers say..."). Geen klantdata, nooit de echte BF-code (gebruik BFCODE). Geen flashprijzen verzinnen. Siraat-skill siraat-direct-response volgen voor copy.
- READ-ONLY: niets aanpassen in Klaviyo, Alia, Shopify of live flows. Niet committen; de hoofdsessie commit.
