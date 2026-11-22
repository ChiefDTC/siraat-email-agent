# Brief: BFCM-week extra mails (US only), 27 nov t/m 4 dec 2026

Opdracht Floris (22 nov): mails voor de komende week, **alleen USA**, met de **12-Pcs set** en de **gratis Titanium Hammered Pizza Steel** centraal, met de **Homestead-banner** (rode aankondigingsbalk bovenaan, zie HS Email 13 US: `klaviyo/hs-previews/2026-11-bfcm/hs-email13-us-nov25.html`, maar dan met 5 gifts). Mooie Black Friday-beelden als achtergrond/hero.

Niets naar klanten sturen, niets inplannen. Alleen bouwen + tests naar lolagroothuis@gmail.com na akkoord Floris.

## De 4 mails

| # | Map | Datum (lokaal) | Doelgroep | Rol |
|---|---|---|---|---|
| M1 | `m1-buyers-bf` | vr 27 nov 10:00 ET | US bestaande kopers (worden uitgesloten van HS Email 16) | kopers 2: "Black Friday, for the kitchen you started". Upgrade naar de volledige set, Pizza Steel gratis. Bestaand concept: Klaviyo campagne 01M62ECEGWRPHFA2HQPAM6WE22, template VhZvzh (lezen, niet wijzigen). |
| M2 | `m2-abandoners-sat` | za 28 nov 14:00 | US winkelwagen/checkout laatste 30 dagen, geen order | Benjamin, kort, persoonlijk, "something stopped you?", 12-Pcs + Pizza Steel + 5 gifts. Vorig jaar de best renderende send van de piek ($0,77/ontvanger). |
| M3 | `m3-buyers-cm` | ma 30 nov 10:00 ET | US bestaande kopers (uit HS Email 20) | kopers 3: Cyber Monday. Bestaand concept: 01M62ECJ5ER9F0GNV8GJMKJPCV, template UAmcBg. Extra korting **nog niet besloten**: maak variant A zonder extra korting en variant B met `$100 off orders $700+` (en $50 off $400+), placeholder code `[CODE]`. |
| M4 | `m4-24h-left` | vr 4 dec 18:00 | US Engaged 30 + afhakers | "24 hours left". Einddatum sale = **5 dec** (Email 11 footer "11/01 to 12/05"), nog te bevestigen door Floris; schrijf `[END: Sat, Dec 5]` als markering. |

## Vaste feiten (check claims.csv / DECISIONS.md)
- 12-Pcs set: `$649`, compare-at `$2,047` (68% off). URL https://siraatskitchen.com/products/titanium-hammered-cookware-set
- Gratis Titanium Hammered Pizza Steel, alleen bij de 12-Pcs set, alleen tijdens de sale. URL https://siraatskitchen.com/products/titanium-hammered-pizza-steel
- 5 free gifts with every order ($555 value, alleen in US): Free shipping, A mystery gift, The Plastic-Free Cooking e-book, The Favorites Cookbook e-book, A chance to win a PFAS water filter ($450 value). Nooit "purifier", nooit "4 gifts".
- Collectie: https://siraatskitchen.com/collections/black-friday-sale
- Bewijs: Light Labs report no. 25895 (https://siraatskitchen.com/pages/third-party-testing), 75-year warranty, 30-day returns, 100,000+ happy customers.
- Oprichter = Benjamin. Nooit een em dash.

## Merkregels (CLAUDE.md, altijd)
- Vaste header en footer uit `klaviyo/templates/partials/` (header.html, footer.html). Logo = lockup monogram + SIRAAT (`brand/logo/lockup/`), nooit nagebouwd.
- HS-banner = rode balk bovenaan ín de mail, boven/onder onze header (design kiest), tekst bv. "5 FREE gifts with every order + a FREE Pizza Steel with the 12-piece set".
- Copy-skill: `.claude/skills/siraat-direct-response/SKILL.md`. Beeldstijl: siraat-flash-style skill (flitsfoto, nacht, mensen lachen) of donkere BF-productshots; nooit AI-logo's of tekst in beeld.

## Uitvoer per map
- `copy.md` (copy-agent): 5 onderwerpregels + keuze, preview, hero (label / regel1|regel2 / subline), body, knoppen, friction reducer, P.S.
- `images/` + `images/README.md` (image-agent): bestanden + gehoste URL (Klaviyo upload), welke mail, welke plek.
- `email.html` + `preview.png` (design-agent).
