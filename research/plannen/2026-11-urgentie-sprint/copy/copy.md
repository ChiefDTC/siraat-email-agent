# Copy urgentie-sprint (8 nov 2026)

Rol: copywriter. Bron: `../BRIEF.md`, `research/plannen/2026-11-urgentie.md`, `research/plannen/2026-11-punten-store-credit.md`, DECISIONS.md, PLAYBOOK.md, skill siraat-direct-response, `content/reviews/top.md`. Machineleesbaar: `copy.json` (zelfde inhoud, voor de design-agent).

## Spelregels voor deze set

- Elke deadline staat als variabele: `{{DEADLINE}}` (volledig, bv. "tonight at 11:59 PM") en `{{DEADLINE_SHORT}}` (onderwerp en hero, bv. "tonight"). Baseline vanavond 23:59 ontvangerstijd. Geen mail live voordat Floris de echte deadline in Shopify, Klaviyo of Rise.ai heeft gezet.
- Deadline staat in het eerste scherm (hero of subline plus countdown-regel) en nog een keer vlak boven de laatste knop (`final_cta_line`).
- Elke deadline heeft een reden en zegt wat er daarna gebeurt ("then the regular Black Friday price applies").
- INT: geen valuta, geen bedragen; US-only zinnen zijn herschreven. Friction reducer INT met "duties paid".
- Reviews: alleen letterlijk uit `content/reviews/reviews.csv`, 5 sterren, ingekort met "...", max 120 tekens, door het script gecontroleerd. R017 bewust niet (Floris: zwak).
- Knoppen: ink #272727. Geel alleen op saletags. Vaste header en footer, behalve mail 4 (platte brief, minimale footer).
- Onderwerplengte gemeten met voorbeeldwaarden: `{{DEADLINE}}` = tonight at 11:59 PM, `{{DEADLINE_SHORT}}` = tonight, `{{FLASH_PRICE}}` = $199, `{{FLASH_PERCENT}}` = 20%, `{{CREDIT}}` = 12, `{{POINTS}}` = 1,200, `{{VIP_CODE}}` = VIP-7KQ2.

## Placeholders

| Placeholder | Betekenis |
| --- | --- |
| `{{DEADLINE}}` | Volledige deadline, bv. 'tonight at 11:59 PM' of 'Sunday at 11:59 PM ET'. Baseline: vanavond 23:59 ontvangerstijd. Pas live als de deadline echt in de backend staat. |
| `{{DEADLINE_SHORT}}` | Korte vorm voor onderwerp en hero, bv. 'tonight' of 'Sunday'. Moet altijd hetzelfde moment zijn als {{DEADLINE}}. |
| `{{DEADLINE_DATE}}` | Juridische vorm, bv. 'November 15, 2026 at 11:59 PM ET'. |
| `{{FLASH_PRICE}}` | US flashprijs 2 Pans + 2 Lids (Floris zet die in Shopify). Alleen US. |
| `{{FLASH_PERCENT}}` | INT: extra korting in procent op de flashset, bv. '20%'. Geen valuta in INT. |
| `{{VIP_CODE}}` | Unieke Klaviyo-code per profiel ({% coupon_code 'VIPWEEKEND' %}), one use, vervalt op {{DEADLINE}}. |
| `{{CREDIT}}` | Rise.ai-saldo per profiel in USD zonder $-teken (bv. 12). Alleen US. Bestaat nog niet: mail 3 pas live als Rise live is. |
| `{{POINTS}}` | Rise.ai-punten per profiel (100 points = $1). |
| `{{PAN_AFTER_CREDIT}}` | 144 min {{CREDIT}}, berekend in Klaviyo. |
| `{{WHAT_ENDS}} / {{WHAT_ENDS_SHORT}} / {{AFTER}}` | Mail 4: wat er afloopt en wat er daarna gebeurt, gekozen per bronmail (tabel in copy.md). |
| `{{DRAW_RULES_URL}}` | Link naar de officiele trekkingsregels. Mail 6 mag niet live zonder. |
| `{{LINK}}` | Doel-URL (BF-collectie of codelink). |
| `BFCODE` | Echte BF-code nooit in bestanden. |

## Mail 1-flash: 24-hour flash deal ends tonight

Afzender: Siraat. Doelgroep: E90 + Product Viewers L30 (US en INT apart).

### US

- Subject A: "24-hour flash: 2 pans + 2 lids" (30 tekens)
- Subject B: "Flash price ends {{DEADLINE_SHORT}}" (24 tekens, deadline, **gekozen**)
- Subject C: "4 pieces for {{FLASH_PRICE}}, today only" (29 tekens)
- Preview: "The 2 Pans + 2 Lids set is {{FLASH_PRICE}} for 24 hours. Then it goes back to $249."
- Resend niet-openers: "Last hours: 2 pans + 2 lids, {{FLASH_PRICE}}" (33 tekens), preview "The flash price ends {{DEADLINE}}. After that it's $249 again."
- Eyebrow: 24-HOUR FLASH DEAL
- Hero: `Two pans, two lids.|One day at this price.`
- Subline: {{FLASH_PRICE}} until {{DEADLINE}}
- Countdown-regel (eerste scherm): Flash price ends {{DEADLINE}}. Then $249.

Body:

> For the next 24 hours, the 2 Pans + 2 Lids set is {{FLASH_PRICE}}. Its Black Friday price is $249, and before the sale it was $664.
>
> Two hammered titanium pans, each with its own lid. A pure titanium cooking surface with no coatings, so there's nothing on them to wear off. That's why every piece is covered for 75 years.
>
> This is a flash price, so it has an end. It goes back to $249 {{DEADLINE}}. Same set, same 5 free gifts, just not this price.
>
> Your 5 free gifts ship with it. $555 value.
>
> "...I thought it was just marketing hype... I ended up buying the whole collection." (Fatima, verified buyer, R398)
>
> Light Labs tested our titanium for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895, read it yourself.
>
> [ Get both pans for {{FLASH_PRICE}} ]
> Free shipping. 30-day returns. 100,000+ happy customers.
>
> This price is gone {{DEADLINE}}. The set stays, at $249.
> [ Get both pans for {{FLASH_PRICE}} ]
>
> P.S. Two pans means one can be a gift. Tammy, a verified buyer, is on her 4th pan and gave one to her son.

### INT

- Subject A: "24-hour flash: 2 pans + 2 lids" (30 tekens)
- Subject B: "Flash price ends {{DEADLINE_SHORT}}" (24 tekens, deadline, **gekozen**)
- Subject C: "An extra {{FLASH_PERCENT}} off, today only" (28 tekens)
- Preview: "An extra {{FLASH_PERCENT}} off the 2 Pans + 2 Lids set, for 24 hours. Then it's the Black Friday price again."
- Resend niet-openers: "Last hours: the 2-pan flash deal" (32 tekens), preview "The extra {{FLASH_PERCENT}} ends {{DEADLINE}}."
- Eyebrow: 24-HOUR FLASH DEAL
- Hero: `Two pans, two lids.|One day at this price.`
- Subline: Extra {{FLASH_PERCENT}} off until {{DEADLINE}}
- Countdown-regel (eerste scherm): Flash price ends {{DEADLINE}}. Then the Black Friday price.

Body:

> For the next 24 hours, the 2 Pans + 2 Lids set has an extra {{FLASH_PERCENT}} off its Black Friday price.
>
> Two hammered titanium pans, each with its own lid. A pure titanium cooking surface with no coatings, so there's nothing on them to wear off. That's why every piece is covered for 75 years.
>
> This is a flash price, so it has an end. The extra {{FLASH_PERCENT}} stops {{DEADLINE}}. Same set, same 5 free gifts, just not this price.
>
> Your 5 free gifts ship with it.
>
> "...I thought it was just marketing hype... I ended up buying the whole collection." (Fatima, verified buyer, R398)
>
> Light Labs tested our titanium for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895, read it yourself.
>
> [ Get both pans, {{FLASH_PERCENT}} extra off ]
> Free shipping, duties paid. 30-day returns. 100,000+ happy customers.
>
> The extra {{FLASH_PERCENT}} is gone {{DEADLINE}}. The set stays.
> [ Get both pans, {{FLASH_PERCENT}} extra off ]
>
> P.S. Two pans means one can be a gift. Tammy, a verified buyer, is on her 4th pan and gave one to her son.

Notities:

- Alleen versturen als Floris echt een 24-uursprijs in Shopify zet en die daarna echt teruggaat naar $249 (EU: laagste-prijs-30-dagen check).
- Product gekozen: 2 Pans + 2 Lids (beste RPR zonder deadline, Benjamin-brief 6 nov, $0,124). Ander product: alleen naam, prijzen en de review wisselen.
- 'before the sale it was $664' alleen als $664 de echte compare-at in Shopify is (brief: MSRP $664). Anders die zin schrappen.
- R398 is gekozen omdat het over 'the whole collection' gaat (set). PS gebruikt R138 (Tammy) als parafrase, geen citaat: 'is on her 4th pan and gave one to her son' staat letterlijk in haar review.

## Mail 2-vip-weekend: VIP only: extra 10% on top, ends Sunday midnight

Afzender: Benjamin from Siraat. Doelgroep: Kopers (alle) + E30, unieke code per profiel.

### US

- Subject A: "VIP only: an extra 10% on top" (29 tekens, **gekozen**)
- Subject B: "Your extra 10% ends {{DEADLINE_SHORT}}" (27 tekens, deadline)
- Subject C: "Want 10% off the Black Friday price?" (36 tekens)
- Preview: "Your own code, on top of up to 70% off. One use. It stops working {{DEADLINE}}."
- Resend niet-openers: "Your extra 10% is still unused" (30 tekens), preview "Your own code ends {{DEADLINE}}. After that it's the regular Black Friday price."
- Eyebrow: VIP WEEKEND
- Hero: `An extra 10%|on top of Black Friday`
- Subline: Your own code. Ends {{DEADLINE_SHORT}}.
- Countdown-regel (eerste scherm): Your code {{VIP_CODE}} works until {{DEADLINE}}.

Body:

> Hi {{ first_name|default:'there' }},
>
> Benjamin here. This weekend I made a code for the people on this list. It's not on the website, and it only works once: {{VIP_CODE}}.
>
> It takes an extra 10% off the Black Friday price. So the Pan Pro goes from $144 to $129.60, and the 2 Pans + 2 Lids from $249 to $224.10.
>
> It's made for this weekend, so it has an end. The code stops working {{DEADLINE}}, and then the regular Black Friday price applies again.
>
> Your 5 free gifts come with it. $555 value.
>
> "These hammered Titanium pans from Siraat have been the best we have owned yet... the last pans we ever have to purchase." (Scott Y., verified buyer, R583)
>
> Light Labs tested our titanium for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895, read it yourself.
>
> [ Use my extra 10% ]
> One use, already applied. 30-day returns. 100,000+ happy customers.
>
> One order, one code, until {{DEADLINE}}.
> [ Use my extra 10% ]
>
> P.S. The code covers one order, so put everything you want in that one. The 5 gifts come with it either way.

### INT

- Subject A: "VIP only: an extra 10% on top" (29 tekens, **gekozen**)
- Subject B: "Your extra 10% ends {{DEADLINE_SHORT}}" (27 tekens, deadline)
- Subject C: "Want 10% off the Black Friday price?" (36 tekens)
- Preview: "Your own code, on top of up to 70% off. One use. It stops working {{DEADLINE}}."
- Resend niet-openers: "Your extra 10% is still unused" (30 tekens), preview "Your own code ends {{DEADLINE}}. After that it's the regular Black Friday price."
- Eyebrow: VIP WEEKEND
- Hero: `An extra 10%|on top of Black Friday`
- Subline: Your own code. Ends {{DEADLINE_SHORT}}.
- Countdown-regel (eerste scherm): Your code {{VIP_CODE}} works until {{DEADLINE}}.

Body:

> Hi {{ first_name|default:'there' }},
>
> Benjamin here. This weekend I made a code for the people on this list. It's not on the website, and it only works once: {{VIP_CODE}}.
>
> It takes an extra 10% off the Black Friday price, which is already up to 70% off. One code, any pan or set in the sale.
>
> It's made for this weekend, so it has an end. The code stops working {{DEADLINE}}, and then the regular Black Friday price applies again.
>
> Your 5 free gifts come with it.
>
> "These hammered Titanium pans from Siraat have been the best we have owned yet... the last pans we ever have to purchase." (Scott Y., verified buyer, R583)
>
> Light Labs tested our titanium for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895, read it yourself.
>
> [ Use my extra 10% ]
> One use, already applied. Duties paid. 30-day returns.
>
> One order, one code, until {{DEADLINE}}.
> [ Use my extra 10% ]
>
> P.S. The code covers one order, so put everything you want in that one. The 5 gifts come with it either way.

Notities:

- Besluit Floris nodig: 10% ja, doelgroep kopers + E30, stapelt op de sale maar niet met HI10/BFCODE, twee weekenden (13 tot 15 en 26 tot 29 nov)?
- 'VIP only' is alleen waar met een unieke code per profiel naar dit segment. Nooit een vaste wachtwoordcode.
- Resend 'still unused' alleen naar profielen zonder order sinds verzending (dan is het waar).

## Mail 3-credit: Your $X store credit expires tonight

Afzender: Benjamin from Siraat. Doelgroep: Rise-saldo > 0 (segment Points · balance > 0 · bf26).

### US

- Subject A: "Your ${{CREDIT}} expires {{DEADLINE_SHORT}}" (24 tekens, deadline, **gekozen**)
- Subject B: "${{CREDIT}} from your past orders" (25 tekens)
- Subject C: "{{POINTS}} points, still unused" (26 tekens)
- Preview: "Earned by your past orders, applied at checkout. After {{DEADLINE}}, the balance is gone."
- Resend niet-openers: "${{CREDIT}}, last hours" (15 tekens), preview "Your store credit expires {{DEADLINE}}. It's applied at checkout."
- Eyebrow: YOUR STORE CREDIT
- Hero: `Your ${{CREDIT}}|expires {{DEADLINE_SHORT}}`
- Subline: {{POINTS}} points, ready to use now
- Countdown-regel (eerste scherm): ${{CREDIT}} left. Expires {{DEADLINE}}.

Body:

> Hi {{ first_name|default:'there' }},
>
> Benjamin here. Your past orders earned you {{POINTS}} points. That's ${{CREDIT}} in store credit, and it's already on your account.
>
> Use it on anything in the Black Friday Sale. It comes off at checkout, after the sale price. A Pan Pro is $144 right now. With your credit, you pay ${{PAN_AFTER_CREDIT}}.
>
> It's a thank-you for ordering from us before, made for this sale, so it has an end date. The balance goes to zero {{DEADLINE}}. Nothing else changes.
>
> Your 5 free gifts ship with this order too. $555 value.
>
> "I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns." (Tammy, verified buyer, R138)
>
> And the pan you already own? Still covered for 75 years.
>
> [ Use my ${{CREDIT}} ]
> Applied at checkout. 30-day returns. 100,000+ happy customers.
>
> Your ${{CREDIT}} is gone {{DEADLINE}}. Use it or let it go.
> [ Use my ${{CREDIT}} ]
>
> P.S. Already have one of our pans? This is a good moment for a second size. Tammy is on her 4th.
>
> <small>Promotional store credit, no purchase needed to receive it. Expires {{DEADLINE_DATE}}. 100 points = $1. Not redeemable for cash.</small>

### INT

- Subject A: "Your store credit expires {{DEADLINE_SHORT}}" (33 tekens, deadline, **gekozen**)
- Subject B: "Credit from your past orders" (28 tekens)
- Subject C: "{{POINTS}} points, still unused" (26 tekens)
- Preview: "Earned by your past orders, applied at checkout in your currency. After {{DEADLINE}}, it's gone."
- Resend niet-openers: "Your store credit, last hours" (29 tekens), preview "It expires {{DEADLINE}}. It's applied at checkout."
- Eyebrow: YOUR STORE CREDIT
- Hero: `Your store credit|expires {{DEADLINE_SHORT}}`
- Subline: {{POINTS}} points, ready to use now
- Countdown-regel (eerste scherm): {{POINTS}} points left. Expires {{DEADLINE}}.

Body:

> Hi {{ first_name|default:'there' }},
>
> Benjamin here. Your past orders earned you {{POINTS}} points. That's store credit, and it's already on your account.
>
> Use it on anything in the Black Friday Sale. It comes off at checkout, in your own currency, after the sale price.
>
> It's a thank-you for ordering from us before, made for this sale, so it has an end date. The balance goes to zero {{DEADLINE}}. Nothing else changes.
>
> Your 5 free gifts ship with this order too.
>
> "I am on my 4th pan from Siraat... I even gifted one to my son, and he says it's the best pan he owns." (Tammy, verified buyer, R138)
>
> And the pan you already own? Still covered for 75 years.
>
> [ Use my store credit ]
> Applied at checkout, in your currency. Duties paid. 30-day returns.
>
> Your credit is gone {{DEADLINE}}. Use it or let it go.
> [ Use my store credit ]
>
> P.S. Already have one of our pans? This is a good moment for a second size. Tammy is on her 4th.
>
> <small>Promotional store credit, no purchase needed to receive it. Expires {{DEADLINE_DATE}}. 100 points = 1 USD, converted at checkout. Not redeemable for cash.</small>

Notities:

- Mag pas live als Rise.ai echt tegoed met vervaldatum op elk profiel zet (BRIEF: nooit verzonnen tegoed). {{CREDIT}} en {{POINTS}} uit rise_wallet_balance / siraat_points.
- Open in het creditplan: stapelt het tegoed met de sale (copy zegt 'after the sale price') en doet INT mee? INT-versie noemt geen bedrag; de legal-regel noemt 1 USD alleen omdat dat de rekenregel is, schrappen als Floris dat niet wil.
- Juridische regel (Californie) laten lezen, zie creditplan vraag 7.
- 'Use it or let it go' is verlies-framing zonder druk; alternatief: 'After that, it's the regular Black Friday price.'

## Mail 4-last-hours: Last hours resend to openers without a click (plain text, Benjamin)

Afzender: Benjamin from Siraat. Doelgroep: Openers van mail 1, 2, 3, 5 of 6 zonder klik en zonder order, ca. 4 tot 6 uur voor {{DEADLINE}}.

### US

- Subject A: "Last hours" (10 tekens, **gekozen**)
- Subject B: "It ends {{DEADLINE}}" (27 tekens, deadline)
- Subject C: "Benjamin here, before it ends" (29 tekens)
- Preview: "A short note from me, then I'll leave you alone."
- Resend niet-openers: "Benjamin here, one last time" (28 tekens), preview "{{WHAT_ENDS_SHORT}} ends {{DEADLINE}}."
- Countdown-regel (eerste scherm): {{WHAT_ENDS}} ends {{DEADLINE}}.

Platte tekst (Benjamin):

```
Hi {{ first_name|default:'there' }},

A quick follow-up to my last email, before it ends.

{{WHAT_ENDS}} ends {{DEADLINE}}.

{{AFTER}} That's the whole change, but it's a real one.

If it's the price that's holding you back, here's how I think about it. Say a good coated pan lasts a few years before it starts to peel, and then you buy another. Ours has a pure titanium cooking surface, no coatings, nothing on it to wear off. That's why we cover it for 75 years.

And if it's not for you, send it back unused within 30 days. One customer, Steven, put it like this: "I returned my pans, unused, and received a refund, no questions asked."

Here's the link, it ends {{DEADLINE}}:
{{LINK}}

Benjamin
Founder, Siraat

P.S. If something else is stopping you, a size question or anything, just reply. I read these.
```

### INT

- Subject A: "Last hours" (10 tekens, **gekozen**)
- Subject B: "It ends {{DEADLINE}}" (27 tekens, deadline)
- Subject C: "Benjamin here, before it ends" (29 tekens)
- Preview: "A short note from me, then I'll leave you alone."
- Resend niet-openers: "Benjamin here, one last time" (28 tekens), preview "{{WHAT_ENDS_SHORT}} ends {{DEADLINE}}."
- Countdown-regel (eerste scherm): {{WHAT_ENDS}} ends {{DEADLINE}}.

Platte tekst (Benjamin):

```
Hi {{ first_name|default:'there' }},

A quick follow-up to my last email, before it ends.

{{WHAT_ENDS}} ends {{DEADLINE}}.

{{AFTER}} That's the whole change, but it's a real one.

If it's the price that's holding you back, here's how I think about it. Say a good coated pan lasts a few years before it starts to peel, and then you buy another. Ours has a pure titanium cooking surface, no coatings, nothing on it to wear off. That's why we cover it for 75 years.

And if it's not for you, send it back unused within 30 days. One customer, Steven, put it like this: "I returned my pans, unused, and received a refund, no questions asked."

Here's the link, it ends {{DEADLINE}}:
{{LINK}}

Benjamin
Founder, Siraat

P.S. If something else is stopping you, a size question or anything, just reply. I read these.
```

`{{WHAT_ENDS}}` per bronmail:

| Bronmail | {{WHAT_ENDS}} US | {{WHAT_ENDS}} INT | {{WHAT_ENDS_SHORT}} | {{AFTER}} US | {{AFTER}} INT |
| --- | --- | --- | --- | --- | --- |
| 1-flash | The flash price on the 2 Pans + 2 Lids ({{FLASH_PRICE}}) | The extra {{FLASH_PERCENT}} off the 2 Pans + 2 Lids | The flash price | After that the set goes back to $249. | After that it's the regular Black Friday price. |
| 2-vip-weekend | Your own extra 10% code, {{VIP_CODE}}, | Your own extra 10% code, {{VIP_CODE}}, | Your extra 10% | After that the code stops working and it's the regular Black Friday price. | After that the code stops working and it's the regular Black Friday price. |
| 3-credit | Your ${{CREDIT}} store credit | Your store credit | Your ${{CREDIT}} | After that the balance goes to zero. | After that the balance goes to zero. |
| 5-gifts | The free gifts with every order (mystery gift, two books and the filter draw) | The free gifts with every order (mystery gift, two books and the filter draw) | The free gifts | After that orders ship without them. Free shipping stays. | After that orders ship without them. Free shipping stays. |
| 6-draw | This week's PFAS water filter draw | This week's PFAS water filter draw | This week's draw | After that your order goes into next week's draw instead. | After that your order goes into next week's draw instead. |

Notities:

- Platte brief: geen header en geen logo, minimale footer (afmelden, voorkeuren, adres), zoals de BRIEF toestaat.
- Bewust 'A quick follow-up to my last email' en niet 'You opened my email but didn't click': Apple MPP maakt opens onbetrouwbaar, dus dat zou niet altijd waar zijn.
- INT is gelijk aan US: de brief noemt geen bedrag. Bij 3-credit de INT-regel uit what_ends gebruiken.
- Mag alleen als de bronmail een echte deadline heeft die nog niet voorbij is. 'Last hours' alleen in de laatste 6 uur.
- 'I read these' in plaats van de standaardregel 'A real person reads every email' (die is gerantsoeneerd).

## Mail 5-gifts: Your 5 free gifts end tonight

Afzender: Siraat. Doelgroep: Lijst (E90 + kopers), alleen op de dag dat de gifts echt stoppen.

### US

- Subject A: "Your free gifts end {{DEADLINE_SHORT}}" (27 tekens, deadline, **gekozen**)
- Subject B: "$555 in gifts, with any order" (29 tekens)
- Subject C: "What comes in the box besides the pan" (37 tekens)
- Preview: "Mystery gift, two books and a shot at a PFAS water filter. They stop when Black Friday does."
- Resend niet-openers: "Last hours for the 5 free gifts" (31 tekens), preview "They end {{DEADLINE}}, with Black Friday."
- Eyebrow: 5 FREE GIFTS
- Hero: `The gifts end|{{DEADLINE_SHORT}}`
- Subline: With every order. $555 value.
- Countdown-regel (eerste scherm): Gifts end {{DEADLINE}}.

Body:

> Every order in the Black Friday Sale ships with 5 free gifts. One pan or the whole set, you get the same five.
>
> Mystery gift · Free shipping · Plastic-free ebook · Favorites cookbook · A chance to win a PFAS water filter (weekly draw)  (blok `{{BLOCK:gifts5}}`)
>
> They end with Black Friday, {{DEADLINE}}. After that, the mystery gift, both books and the draw entry are gone. Free shipping stays.
>
> So it's $555 in gifts on a $144 pan. That math only works until {{DEADLINE_SHORT}}.
>
> "A gift for my daughter who loves to cook... I can't wait to finish work, and go home to cook." (Louise T., verified buyer, R563)
>
> Light Labs tested our titanium for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895, read it yourself.
>
> [ Claim my 5 gifts ]
> Free shipping. 30-day returns. 100,000+ happy customers.
>
> Order before {{DEADLINE}} and all five ship with it.
> [ Claim my 5 gifts ]
>
> P.S. The gifts come per order, not per pan. If a second pan is on your list, this is the order to put it in.

### INT

- Subject A: "Your free gifts end {{DEADLINE_SHORT}}" (27 tekens, deadline, **gekozen**)
- Subject B: "5 free gifts, with any order" (28 tekens)
- Subject C: "What comes in the box besides the pan" (37 tekens)
- Preview: "Mystery gift, two books and a shot at a PFAS water filter. They stop when Black Friday does."
- Resend niet-openers: "Last hours for the 5 free gifts" (31 tekens), preview "They end {{DEADLINE}}, with Black Friday."
- Eyebrow: 5 FREE GIFTS
- Hero: `The gifts end|{{DEADLINE_SHORT}}`
- Subline: With every order, any size.
- Countdown-regel (eerste scherm): Gifts end {{DEADLINE}}.

Body:

> Every order in the Black Friday Sale ships with 5 free gifts. One pan or the whole set, you get the same five.
>
> Mystery gift · Free shipping, duties paid · Plastic-free ebook · Favorites cookbook · A chance to win a PFAS water filter (weekly draw)  (blok `{{BLOCK:gifts5}}`)
>
> They end with Black Friday, {{DEADLINE}}. After that, the mystery gift, both books and the draw entry are gone. Free shipping, duties paid, stays.
>
> One order, five extras, and the pan underneath it all is covered for 75 years.
>
> "A gift for my daughter who loves to cook... I can't wait to finish work, and go home to cook." (Louise T., verified buyer, R563)
>
> Light Labs tested our titanium for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895, read it yourself.
>
> [ Claim my 5 gifts ]
> Free shipping, duties paid. 30-day returns. 100,000+ happy customers.
>
> Order before {{DEADLINE}} and all five ship with it.
> [ Claim my 5 gifts ]
>
> P.S. The gifts come per order, not per pan. If a second pan is on your list, this is the order to put it in.

Notities:

- De gifts lopen tot het einde van Black Friday (30 nov). 'End tonight' is dus alleen waar op de laatste dag, tenzij Floris een eerdere gift-deadline in de backend zet. [BESLUIT FLORIS]
- Onderwerp bewust 'Your free gifts end' en niet 'Your 5 free gifts end': gratis verzending blijft na de sale (staande claim), dus niet alle vijf stoppen. Body zegt dat eerlijk.
- Mystery gift niet onthullen. Waarde $555 alleen US (besluit 7 nov). Gift-beelden via {{BLOCK:gifts5}}.
- Rekensom '$555 in gifts on a $144 pan' is letterlijk de besluitwaarde tegen de US-saleprijs.

## Mail 6-draw: Order by Sunday midnight to enter this week's filter draw

Afzender: Siraat. Doelgroep: E90 + abandoners L30.

### US

- Subject A: "Order by {{DEADLINE_SHORT}} for this week's draw" (37 tekens, deadline, **gekozen**)
- Subject B: "Win a PFAS water filter this week" (33 tekens)
- Subject C: "This week's filter draw: who's in?" (34 tekens)
- Preview: "Every order this week is an entry. The draw closes {{DEADLINE}}. No purchase necessary, see the rules."
- Resend niet-openers: "Last hours to enter this week's draw" (36 tekens), preview "It closes {{DEADLINE}}. One order, one entry."
- Eyebrow: WEEKLY FILTER DRAW
- Hero: `This week's draw|closes {{DEADLINE_SHORT}}`
- Subline: Order by then for a chance at a PFAS filter
- Countdown-regel (eerste scherm): This week's draw closes {{DEADLINE}}.

Body:

> Every week, one person who ordered that week wins a PFAS water filter. This week's draw closes {{DEADLINE}}.
>
> Order before then and you're in this week's draw. One pan counts the same as the whole set.
>
> It fits the pan. Light Labs tested our titanium for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895, read it yourself. The filter is for the water you cook with.
>
> And the order itself is still up to 70% off, with the other 4 gifts included.
>
> Plus 4 more gifts with every order. $555 value in total.
>
> "Awesome pan and peace of mind that I am not ingesting bits of toxins when I cook." (Gwen, verified buyer, R555)
>
> [ Order and enter this week ]
> Free shipping. 30-day returns. 100,000+ happy customers.
>
> The draw closes {{DEADLINE}}. Orders after that go into next week's.
> [ Order and enter this week ]
>
> P.S. You don't need a big order to be in. One pan, one entry.
>
> <small>No purchase necessary. One winner per weekly draw, picked at random from entries received by {{DEADLINE_DATE}}. Full rules: {{DRAW_RULES_URL}}</small>

### INT

- Subject A: "Order by {{DEADLINE_SHORT}} for this week's draw" (37 tekens, deadline, **gekozen**)
- Subject B: "Win a PFAS water filter this week" (33 tekens)
- Subject C: "This week's filter draw: who's in?" (34 tekens)
- Preview: "Every order this week is an entry. The draw closes {{DEADLINE}}. No purchase necessary, see the rules."
- Resend niet-openers: "Last hours to enter this week's draw" (36 tekens), preview "It closes {{DEADLINE}}. One order, one entry."
- Eyebrow: WEEKLY FILTER DRAW
- Hero: `This week's draw|closes {{DEADLINE_SHORT}}`
- Subline: Order by then for a chance at a PFAS filter
- Countdown-regel (eerste scherm): This week's draw closes {{DEADLINE}}.

Body:

> Every week, one person who ordered that week wins a PFAS water filter. This week's draw closes {{DEADLINE}}.
>
> Order before then and you're in this week's draw. One pan counts the same as the whole set.
>
> It fits the pan. Light Labs tested our titanium for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895, read it yourself. The filter is for the water you cook with.
>
> And the order itself is still up to 70% off, with the other 4 gifts included.
>
> Plus 4 more gifts with every order.
>
> "Awesome pan and peace of mind that I am not ingesting bits of toxins when I cook." (Gwen, verified buyer, R555)
>
> [ Order and enter this week ]
> Free shipping, duties paid. 30-day returns. 100,000+ happy customers.
>
> The draw closes {{DEADLINE}}. Orders after that go into next week's.
> [ Order and enter this week ]
>
> P.S. You don't need a big order to be in. One pan, one entry.
>
> <small>No purchase necessary. One winner per weekly draw, picked at random from entries received by {{DEADLINE_DATE}}. Full rules: {{DRAW_RULES_URL}}</small>

Notities:

- BLOKKEREND: de trekking is volgens skill en urgentieplan pas een deadline als er officiele regels zijn (sluitmoment, AMOE/'no purchase necessary', 1 winnaar per week, landen). Zonder {{DRAW_RULES_URL}} niet versturen.
- 'One pan, one entry' en 'One pan counts the same as the whole set' veronderstellen 1 entry per order. Als de regels anders zijn, aanpassen.
- Na de laatste BF-week (30 nov) is er geen 'next week's draw' meer, tenzij de trekking doorloopt: final_cta_line dan aanpassen.
- Gwen (R555) zegt 'toxins': klantwoorden, geen claim van ons. Geen gezondheidsclaim over het filter ('for the water you cook with').

## Besluiten nodig van Floris

1. Flash (mail 1): welk product (voorstel 2 Pans + 2 Lids), welke prijs ({{FLASH_PRICE}} US, {{FLASH_PERCENT}} INT), en gaat de prijs echt terug naar $249 na 24 uur? Is $664 de echte compare-at?
2. VIP-weekend (mail 2): 10%, doelgroep kopers + E30, unieke code per profiel, stapelt op de sale maar niet met HI10/BFCODE, welke weekenden?
3. Credit (mail 3): pas als Rise.ai live is met echt saldo en vervaldatum per profiel. Stapelt het met de sale, doet INT mee, juridische regel akkoord?
4. Gifts (mail 5): alleen op de echte laatste dag (30 nov), tenzij er een eerdere gift-deadline in de backend komt.
5. Trekking (mail 6): officiele regels met sluitmoment, AMOE en 1 entry per order publiceren; zonder regelslink niet versturen.
6. Tijdzone: {{DEADLINE}} in ontvangerstijd (Klaviyo local time) of vast ET? De copy werkt met beide, maar de backend-deadline moet hetzelfde moment zijn als wat er in de mail staat.

## Controle

- Reviewcheck (letterlijk, 5 sterren, max 120 tekens): ok
- Geen em dash, geen en dash, geen verboden woorden (purifier, lifetime, reserved, price held, next batch, pending order, no extensions, Shop now): ok
- INT zonder valuta (behalve de rekenregel in de credit-legal, zie notitie): ok
