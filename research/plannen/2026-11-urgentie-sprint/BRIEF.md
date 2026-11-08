# Urgentie-sprint (8 nov 2026), gezamenlijke brief voor alle agents

Doel (Floris): de meest urgente BF-salemails maken, met deadlines die echt eindigen ("ends tonight", "last hours", "expires at midnight"). Baseline: we schrijven alsof de deadline vanavond om 23:59 (tijd van de ontvanger) afloopt; Floris zet de echte deadline later in de backend (Shopify/Klaviyo-code of Rise.ai-vervaldatum). Elke deadline in de copy moet dus als variabele te vervangen zijn en mag pas live als hij echt bestaat.

## Feiten
- Sale: VIP Black Friday, tot 70% korting, 5 free gifts bij elke bestelling ($555 value in USD-mails): Mystery gift, Free shipping, Plastic-free ebook, Favorites cookbook, plus kans op een PFAS water filter (wekelijkse trekking). Nooit "purifier".
- Oprichter Benjamin. 30 dagen retour, 75 jaar garantie, 100,000+ klanten. Hero: Titanium Hammered Pan Pro (US $144), 2 Pans + 2 Lids $249 (MSRP $664), sets.
- Bewezen: campagnes met echte deadline deden $0,17 per ontvanger tegen $0,03 tot $0,12 zonder ("Win your order back (today only)", "The October sale ENDS TONIGHT"). Opens 36 tot 49%, kliks onder 1%: klikprobleem.
- Lopende plannen: research/plannen/2026-11-urgentie.md (Smooche-analyse, kalender), research/plannen/2026-11-punten-store-credit.md (persoonlijk tegoed "Your $12 expires tonight", Rise.ai, nog niet live), research/popup/2026-11-trigger-test.md.
- Deadline-mechanieken die we mogen gebruiken (eerlijk, als Floris ze in de backend zet): flash deal 24 u, VIP-weekend extra 10% met persoonlijke code die zondag 23:59 verloopt, persoonlijk tegoed dat verloopt, wekelijkse filtertrekking "order by Sunday", gifts eindigen als BF eindigt, einde sale 30 nov.

## Regels (verplicht)
- Lees CLAUDE.md, PLAYBOOK.md, DECISIONS.md. Nooit een gedachtestreepje (em dash of en dash).
- Verboden: next batch, reserve, coming, price held, nepvoorraad, "pending order", verzonnen tegoed, "no extensions".
- Echte BF-code nooit in bestanden: placeholder BFCODE. Deadline-placeholder: {{DEADLINE}} (bv. "tonight at 11:59 PM").
- Kleuren: geel #FFB800 alleen op saletags; knoppen ink #272727; vaste header en footer uit klaviyo/templates/partials/ (uitzondering: platte brieven van Benjamin mogen zonder header, met minimale footer).
- Publieke repo: geen klantdata. Niets in Klaviyo/Shopify wijzigen, geen testmails.
- Werk alleen in je eigen submap: research/plannen/2026-11-urgentie-sprint/<rol>/ (designbestanden in klaviyo/templates/v3/campaigns/urgency-1108/). Commit met Nederlandse LOG.md-regel, git pull --rebase, push naar main. Trailers:
  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01HjCaDE95ohEXY6DPZTSH67
- Klaviyo alleen lezen: /tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive/kl.py, api(m,p,b) (GET en report-endpoints).

## De mailset (alle rollen werken op deze 6)
1. FLASH: "24-hour flash deal ends tonight" (één heldenproduct of set extra scherp).
2. VIP-WEEKEND: "VIP only: extra 10% on top, ends Sunday midnight" (persoonlijke code).
3. CREDIT: "Your $X store credit expires tonight" (Rise.ai-tegoed, bedrag per profiel).
4. LAST-HOURS resend: "Last hours" naar openers zonder klik (korte brief van Benjamin, platte tekst).
5. GIFTS: "Your 5 free gifts end tonight" (gifts-deadline).
6. DRAW: "Order by Sunday midnight to enter this week's filter draw".
