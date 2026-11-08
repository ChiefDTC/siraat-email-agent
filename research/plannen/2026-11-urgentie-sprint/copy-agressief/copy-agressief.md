# Agressieve copy urgentie-sprint (8 nov 2026)

Rol: AGGRESSIVE COPY (edge-finder). Floris wil een maximale baseline, zo hard als Smooche, die hij per mail met de hand afzwakt. Dit is geen vervanging van `../copy/copy.md` (de rustige versie), maar een laag erboven: zelfde 6 mails, zelfde producten en reviews, harder geformuleerd, plus een final-hour-mini-mail en een 'you missed this / last call'-mail.

Bronnen: `../BRIEF.md`, `../copy/copy.md` en `copy.json`, `research/plannen/2026-11-urgentie.md` (Smooche-tijdlijn uit de 13 .eml's), `research/smooche/01` tot `06`, DECISIONS.md, PLAYBOOK.md. Gmail (lolagroothuis@gmail.com, laatste 10 dagen): alleen de doorgestuurde thread 'lukje' (1 nov), al volledig uitgewerkt in 04; niets nieuws. 'VIP ONLY ... SMOOCHEVIP' en 'You missed this' staan niet in deze mailbox, ze komen uit de opdracht en staan hier als patroon.

Alleen geschreven. Niets in Klaviyo of Shopify gewijzigd, niets verstuurd. Machineleesbaar: `copy-agressief.json` (mail, markt, veld, elk item met `waar_als` en `risico`).

**Hoofdregel:** elke regel hieronder mag alleen live als de kolom 'waar als' in de backend klopt op het moment van verzenden. Is één voorwaarde niet waar, dan valt de regel terug op de rustige versie uit copy.md.

## 1. Smooche-mechaniek en woordpatronen

| Onderdeel | Patroon (gemeten uit de 13 mails, tenzij anders vermeld) |
| --- | --- |
| Onderwerp-formules | [DEADLINE IN CAPS]: [aanbod] ('The sale ENDS TONIGHT'); persoonlijk bedrag + verlies ('Your [bedrag] is about to disappear'); status-imitatie ('Your order is pending.', '(1) Your store credit is updated.'); productnaam + 'is waiting for you'; thema + emoji ('Happy Halloween 🎃', 'You joined at the right time 👻'). |
| Preview-formules | Deadline in de eerste zin ('the sale we're running right now ends tonight at midnight'); 'no code needed / already applied'; 'Expires Today'; aanbod + gifts ('60% Off + Free Gifts'). |
| Hero-regels | Kort, bedrag of deadline centraal: 'Your Halloween Surprise' + 'You have [bedrag] store credit left' + zegel 'Expires Today'; 'Final hours'; 'Use it or lose it'. |
| Countdown | Live aftelklok (countdownmail.com) alleen in de slotmail van de kredietreeks (+41 u); verder tekstdeadlines ('tonight', 'within 24 hours', 'SOON' in caps). |
| Slotreeks | Kredietketting: dag 0 'expires today' (13,5 u), dag 1 'extended 24 hours, cannot be extended again' (38,5 u), dag 1 avond 'about to disappear' + klok (41,3 u). Cart/checkout in blokken van 3 (+10 min, +1 u, +1 u 15) en 24 u later nog eens 3. |
| Resend-onderwerpen | '(1) Your ... is updated', 'Your foundation order is pending.' (tweede ronde), 'You missed this' en 'Final hours' (laatste twee uit de opdracht, niet in deze mailbox gemeten). |
| Emoji | Alleen in merkmails (👻 🎃), niet in de Chloe-brieven; max 1 per onderwerp, aan het eind. |
| Caps | Eén woord of frase in caps ('SOON', 'ENDS TONIGHT', 'VIP ONLY', 'YOUR PASSWORD'), nooit het hele onderwerp. |
| Getallen | Oneven, persoonlijk ogend bedrag ($12.24), percentages (60%, 58%, 97% said it matched), 100,000+ women, 24 hours. |
| Cadans | 13 mails in 41 uur, 5 in de eerste 3 uur, elke mail een nieuwe reden; persona (Chloe, platte tekst) bij de 'persoonlijke' momenten, merk (beeldmail) bij aanbod. |

### Wat we eerlijk kunnen overnemen

- Deadline in onderwerp, preview, hero en vlak boven de laatste knop (zelfde moment overal).
- Relatieve tijd ('6 hours left', '60 minutes left', 'Final hour') op echte verzend-offsets T-24h, T-6h, T-1h; waar voor elke tijdzone tegelijk.
- Eén woord in caps plus één emoji ('ENDS TONIGHT ... ⏰').
- Persoonlijk bedrag in het onderwerp ('Your ${{CREDIT}} is about to disappear'), mits echt Rise-saldo met echte vervaldatum.
- 'VIP ONLY' + code in het onderwerp, met unieke one-use code per profiel in plaats van een wachtwoord.
- Verlies-framing ('use it or lose it', 'goes to $0') als het saldo echt vervalt.
- Resend naar niet-openers met nieuw onderwerp ('You missed this: ...'), en een platte Benjamin-brief naar niet-klikkers.
- Live countdown-GIF naar de echte backend-tijd, die na afloop 'ENDED' toont.
- Na de deadline: 'It ended. Here's what's still on.' Geen verlenging, wel de volgende echte reden.
- 'No code needed / already applied' alleen via /discount/CODE?redirect= of automatische korting, getest per markt.

### Risico-legenda

| Risico | Betekenis |
| --- | --- |
| groen | Waar zodra de backend-voorwaarde klopt; geen spamwoorden, geen caps-onderwerp. |
| oranje | Waar onder een strikte extra voorwaarde (verzendtijd, segment, tijdzone, regels) of met caps/emoji/'free'/verlies-framing. Floris checkt per verzending. |
| rood | Alleen met extra techniek (live GIF, AMOE in Klaviyo) of hoog deliverability-risico (caps-onderwerp). Standaard niet versturen; staat erin als maximale stand om af te zwakken. |

FTC-kader: fake countdowns, valse schaarste en nep-orderstatus zijn misleidend (FTC Act sectie 5; FTC-rapport 'Bringing Dark Patterns to Light', 2022); misleidende onderwerpregels vallen onder CAN-SPAM. EU: UCPD bijlage I punt 7 (vals 'maar heel kort beschikbaar'). Deliverability: hele onderwerp in caps, 'FREE' in caps, meerdere emoji en '!!!' verhogen spamplaatsing; onze vangrail blijft spam onder 0,1%, stop boven 0,15% per nieuwe stap.

## 2. Tijdzone- en verzendregels (gelden voor alle mails)

- Shopify-prijzen, codes en Rise-vervaldata hebben één eindtijd, geen eindtijd per ontvanger. 'Tonight' of 'midnight' is dus alleen waar voor de tijdzone die je noemt. US: schrijf 'midnight ET' of splits de US-lijst per tijdzone met elk een eigen code-einde. INT: gebruik uren/minuten of {{DEADLINE}} met tijdzone.
- Klaviyo 'send in recipient's local time' verschuift de verzending, niet de deadline: niet gebruiken voor T-1h en T-15min.
- Statische '60 minutes left' veroudert in de inbox. Daarom: absolute tijd in de body ('ends at 11:59 PM ET') en bij T-15min alleen met live GIF.
- Grote verzendingen (75k) kunnen 10 tot 30 min duren. T-1h en T-15min alleen naar kleine segmenten (klikkers zonder order, < 10k), zodat de mail vóór de deadline aankomt.
- Volume: max 3 mails per 24 u per profiel (4 op BF/CM, volumeplan 06). De volledige reeks T-24h + T-6h + T-1h + T-15min gaat dus nooit naar hetzelfde profiel: T-6h alleen niet-openers, T-1h alleen niet-klikkers, T-15min alleen klikkers zonder order.
- Stopregel blijft: spam boven 0,15% op een nieuwe stap (1.000+ ontvangers) of 0,3% op een verzending = terug naar de rustige versie uit copy.md.

Placeholders (aanvullend op copy.md):

| Placeholder | Betekenis |
| --- | --- |
| `{{DEADLINE}}` | Volledig moment met tijdzone, bv. 'tonight at 11:59 PM ET'. Moet exact de backend-eindtijd zijn. |
| `{{DEADLINE_SHORT}}` | Kort, bv. 'tonight' of 'Sunday'. Zelfde moment als {{DEADLINE}}. |
| `{{DEADLINE_PAST}}` | Mail 8B: moment waarop het echt eindigde, bv. 'last night at 11:59 PM ET'. |
| `{{HOURS_LEFT}}` | Echte uren tot {{DEADLINE}} op het verzendmoment (afronden naar beneden). Nieuw t.o.v. copy.md. |
| `{{MINUTES_LEFT}}` | Echte minuten tot {{DEADLINE}} op het verzendmoment; bij T-15min alleen naast een live GIF. |
| `{{FLASH_PRICE}} / {{FLASH_PERCENT}}` | Zie copy.md (US prijs, INT procent). |
| `{{VIP_CODE}}` | Unieke Klaviyo-code per profiel, one use, einde {{DEADLINE}}. |
| `{{CREDIT}} / {{POINTS}} / {{PAN_AFTER_CREDIT}}` | Rise.ai-saldo per profiel (US zonder $-teken), punten, 144 min credit. |
| `{{WHAT_ENDS}} / {{WHAT_ENDS_SHORT}} / {{AFTER}} / {{AFTER_SHORT}}` | Mail 4, 7, 8: per bronmail uit de tabel in copy.md. |
| `{{DRAW_RULES_URL}}` | Officiële trekkingsregels; zonder deze link geen trekkingsmail. |
| `{{LINK}}` | Doel-URL (codelink of BF-collectie). |
| `BFCODE` | Echte BF-code nooit in bestanden; alleen in abandonment-flows, niet in deze campagnes. |

## 3. De mails

In de tabellen staan terugkerende voorwaarden als code tussen haken; de volledige tekst staat hier (en voluit in de JSON).

| Code | Voorwaarde |
| --- | --- |
| [FLASH-US] | Shopify: 2 Pans + 2 Lids staat op {{FLASH_PRICE}} en gaat op {{DEADLINE}} echt terug naar $249 (geplande prijswijziging of app, getest) |
| [FLASH-INT] | Shopify/Markets: extra {{FLASH_PERCENT}} op de 2 Pans + 2 Lids stopt op {{DEADLINE}} (automatische korting met einddatum) |
| [VIP] | unieke Klaviyo-code per profiel ({% coupon_code %}), one use, Shopify-einddatum = {{DEADLINE}}, alleen naar kopers + E30, niet op de site of couponsites |
| [CREDIT-US] | Rise.ai heeft echt saldo ${{CREDIT}} op dit profiel gezet met vervaldatum = {{DEADLINE}}; segment rise_wallet_balance > 0 |
| [CREDIT-INT] | Rise.ai-saldo > 0 op dit profiel met vervaldatum = {{DEADLINE}}; INT-tegoed werkt in checkout in lokale valuta (getest) |
| [GIFTS-US] | gifts (mystery gift, ebook, cookbook, trekkingsdeelname) worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app/automatisering uit); in de praktijk alleen 30 nov tenzij Floris een eerdere gift-deadline zet; $555 value alleen US |
| [GIFTS] | gifts (mystery gift, ebook, cookbook, trekkingsdeelname) worden op {{DEADLINE}} echt uit nieuwe orders gehaald (gift-app/automatisering uit); in de praktijk alleen 30 nov tenzij Floris een eerdere gift-deadline zet |
| [DRAW] | officiële trekkingsregels gepubliceerd ({{DRAW_RULES_URL}}) met sluitmoment = {{DEADLINE}}, AMOE ('no purchase necessary'), 1 entry per order |
| [DRAW-NIET-IN] | profiel heeft deze week geen order (Klaviyo: Placed Order sinds start trekking = 0) EN AMOE-deelnames staan als event in Klaviyo; anders niet waar |
| [FH] | [FH] |
| [LH] | [LH] |
| [T-15] | [T-15] |
| [T-60] | [T-60] |
| [T-6] | verzendtijd = {{DEADLINE}} min 6 uur (marge 30 min) |
| [T-24] | verzendtijd = {{DEADLINE}} min 24 uur of minder |
| [NIET-OPENERS] | segment: ontvangen bronmail, niet geopend, geen order sinds verzending; deadline nog niet voorbij |
| [NIET-KLIKKERS] | segment: geopend of ontvangen bronmail, niet geklikt, geen order sinds verzending |
| [TONIGHT-ET] | {{DEADLINE}} valt vandaag om 23:59 in de tijdzone die genoemd wordt (ET); bij een US-brede lijst ET noemen, want voor Pacific is 23:59 ET 20:59 |
| [MIDNIGHT-ET] | de backend-deadline is precies 23:59 ET (Shopify-prijs, code of Rise-vervaldatum), niet later |
| [INT-TZ] | INT: geen 'tonight' of 'midnight' zonder tijdzone; relatieve tijd (uren/minuten) is waar voor elke tijdzone tegelijk |
| [NOW] | verzending direct (niet 'local time'), zodat iedereen hem op hetzelfde moment krijgt |

### 1-flash: FLASH: 24-hour flash deal ends tonight

Afzender: Siraat.

Voorwaarde voor de hele mail: [FLASH-US] / INT: [FLASH-INT]

#### US

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | ENDS TONIGHT: 2 pans + 2 lids for {{FLASH_PRICE}} ⏰ | [FLASH-US]; [TONIGHT-ET] | oranje Noot: Twee caps-woorden plus één emoji: Smooche-stijl, binnen de grens. Hele onderwerp in caps zou rood zijn. |
| Subject 2 | 24 hours. 4 pieces. {{FLASH_PRICE}}. | [FLASH-US]; [T-24] | groen |
| Subject 3 | 6 hours left on the flash price | [FLASH-US]; [T-6] | groen |
| Subject 4 | Order now: 60 minutes left | [FLASH-US]; [T-60] | oranje Noot: Statische tekst veroudert: wie om 01:00 opent leest nog '60 minutes'. Body moet het absolute tijdstip noemen. |
| Subject 5 | It's gone at midnight ET | [FLASH-US]; [MIDNIGHT-ET] | groen |
| Preview 1 | Then the set goes back to $249. No code, the price is already on the page. | [FLASH-US]; flashprijs staat zonder code op de PDP | groen |
| Preview 2 | {{FLASH_PRICE}} for 2 pans + 2 lids until {{DEADLINE}}. After that, $249. | [FLASH-US] | groen |
| Preview 3 | 5 free gifts ship with it. This price does not. | [FLASH-US]; gifts lopen door na de flash (tot 30 nov) | groen |
| Hero 1 | 24 hours.\|Then it's $249. | [FLASH-US]; [T-24] | groen |
| Hero 2 | {{FLASH_PRICE}}\|until midnight ET | [FLASH-US]; [MIDNIGHT-ET] | groen |
| Hero 3 | 2 pans. 2 lids.\|Gone tonight. | [FLASH-US]; [TONIGHT-ET] | groen |
| Countdown T-24h | 24 hours at {{FLASH_PRICE}}. Ends {{DEADLINE}}. | [FLASH-US]; [T-24] | groen |
| Countdown T-6h | 6 hours left. At {{DEADLINE}} it's $249 again. | [FLASH-US]; [T-6] | groen |
| Countdown T-1h | Final hour. {{FLASH_PRICE}} until {{DEADLINE}}. | [FLASH-US]; [T-60] | oranje |
| Countdown T-15min | {{MINUTES_LEFT}} minutes left at {{FLASH_PRICE}}. | [FLASH-US]; [T-15] | rood Noot: Alleen met live GIF. Als tekst: op Gmail-tijdstip geopend kan hij al voorbij zijn. Zonder GIF niet sturen. |
| Button 1 | Get both pans for {{FLASH_PRICE}} | [FLASH-US] | groen |
| Button 2 | Lock in {{FLASH_PRICE}} now | [FLASH-US]; prijs staat vast zodra de order geplaatst is (niet bij winkelwagen) | oranje Noot: 'Lock in' alleen als het om de order gaat; nooit suggereren dat de winkelwagen de prijs vasthoudt (= 'price held', verboden). |
| Button 3 | Order before midnight ET | [FLASH-US]; [MIDNIGHT-ET] | groen |
| Body | For 24 hours the 2 Pans + 2 Lids set is {{FLASH_PRICE}}, already on the page, no code. At {{DEADLINE}} it goes back to $249, the same set with the same 5 free gifts, just not this price. If you've been waiting for the moment, this is it. | [FLASH-US]; $664 compare-at niet genoemd tenzij bevestigd | groen |
| Resend niet-openers | You missed this: {{FLASH_PRICE}} for 4 pieces | [FLASH-US]; [NIET-OPENERS]; [T-6] | oranje Noot: 'You missed this' kan lezen als 'voorbij'. Preview moet zeggen dat het nog loopt: 'Still on until {{DEADLINE}}.' |

#### INT

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | ENDS IN 24 HOURS: an extra {{FLASH_PERCENT}} off 2 pans ⏰ | [FLASH-INT]; [T-24] | oranje |
| Subject 2 | 24 hours. 4 pieces. {{FLASH_PERCENT}} extra off. | [FLASH-INT]; [T-24] | groen |
| Subject 3 | {{HOURS_LEFT}} hours left on the flash price | [FLASH-INT]; {{HOURS_LEFT}} = echte uren tot {{DEADLINE}} op verzendmoment, [NOW] | groen |
| Subject 4 | Order now: 60 minutes left | [FLASH-INT]; [T-60] | oranje |
| Subject 5 | Final hour: the 2-pan flash deal | [FLASH-INT]; [T-60] | groen |
| Preview 1 | Then it's the regular Black Friday price again. Already applied, no code. | [FLASH-INT]; automatische korting zonder code | groen |
| Preview 2 | An extra {{FLASH_PERCENT}} on top of Black Friday, for 24 hours only. | [FLASH-INT]; [T-24] | groen |
| Preview 3 | 5 free gifts ship with it. The extra {{FLASH_PERCENT}} does not stay. | [FLASH-INT] | groen |
| Hero 1 | 24 hours.\|Then it's gone. | [FLASH-INT]; [T-24] | groen |
| Hero 2 | Extra {{FLASH_PERCENT}} off\|for {{HOURS_LEFT}} more hours | [FLASH-INT]; [INT-TZ] | groen |
| Hero 3 | 2 pans. 2 lids.\|One day only. | [FLASH-INT]; looptijd is echt maximaal 24 uur | groen |
| Countdown T-24h | 24 hours at an extra {{FLASH_PERCENT}} off. Ends {{DEADLINE}}. | [FLASH-INT]; {{DEADLINE}} met tijdzone of per markt ingevuld | groen |
| Countdown T-6h | 6 hours left. Then it's the regular Black Friday price. | [FLASH-INT]; [T-6] | groen |
| Countdown T-1h | Final hour on the extra {{FLASH_PERCENT}}. | [FLASH-INT]; [T-60] | oranje |
| Countdown T-15min | {{MINUTES_LEFT}} minutes left on the extra {{FLASH_PERCENT}}. | [FLASH-INT]; [T-15] | rood Noot: Alleen met live GIF. |
| Button 1 | Get both pans, {{FLASH_PERCENT}} extra off | [FLASH-INT] | groen |
| Button 2 | Order before it ends | [FLASH-INT] | groen |
| Button 3 | Use the flash price | [FLASH-INT] | groen |
| Body | For 24 hours the 2 Pans + 2 Lids set has an extra {{FLASH_PERCENT}} off its Black Friday price, already applied. When the {{HOURS_LEFT}} hours are up, the extra {{FLASH_PERCENT}} stops and the regular Black Friday price is back. Same set, same 5 free gifts, duties paid. | [FLASH-INT]; [INT-TZ] | groen |
| Resend niet-openers | You missed this: {{FLASH_PERCENT}} extra off 2 pans | [FLASH-INT]; [NIET-OPENERS] | oranje |

### 2-vip-weekend: VIP-WEEKEND: VIP only, extra 10% on top, ends Sunday midnight

Afzender: Benjamin from Siraat.

Voorwaarde voor de hele mail: [VIP]

#### US

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | VIP ONLY: an extra 10% off this weekend | [VIP] | oranje Noot: Smooche-formule zonder vast wachtwoord. 'VIP ONLY' is waar zolang de code uniek is en alleen naar dit segment gaat. |
| Subject 2 | YOUR CODE: {{VIP_CODE}} (extra 10%, ends Sunday) | [VIP]; code is per profiel, dus doorsturen maakt hem niet publiek (one use) | oranje Noot: Eerlijke versie van 'YOUR PASSWORD: SMOOCHEVIP'. Caps op twee woorden. |
| Subject 3 | Your extra 10% ends at midnight ET | [VIP]; [MIDNIGHT-ET]; verzending op zondag | groen |
| Subject 4 | Final hours: your extra 10% on top | [VIP]; [T-6]; profiel heeft code nog niet gebruikt | groen |
| Subject 5 | 60 minutes left on your code | [VIP]; [T-60]; code nog ongebruikt | oranje |
| Preview 1 | On top of up to 70% off. One use, not on the website. | [VIP] | groen |
| Preview 2 | It stops working Sunday at 11:59 PM ET. Then it's the regular Black Friday price. | [VIP]; [MIDNIGHT-ET] | groen |
| Preview 3 | The Pan Pro goes from $144 to $129.60 with it. | [VIP]; code werkt bovenop de saleprijs en stapelt niet met BFCODE/HI10 | groen |
| Hero 1 | VIP only.\|Extra 10% off. | [VIP] | groen |
| Hero 2 | Your code ends\|Sunday at midnight | [VIP]; [MIDNIGHT-ET]; in de subline 'ET' toevoegen | groen |
| Hero 3 | 10% on top\|of Black Friday | [VIP] | groen |
| Countdown T-24h | Your code {{VIP_CODE}} works until {{DEADLINE}}. | [VIP]; [T-24] | groen |
| Countdown T-6h | 6 hours left on {{VIP_CODE}}. | [VIP]; [T-6] | groen |
| Countdown T-1h | Final hour. {{VIP_CODE}} stops at {{DEADLINE}}. | [VIP]; [T-60] | oranje |
| Countdown T-15min | {{MINUTES_LEFT}} minutes left on your extra 10%. | [VIP]; [T-15] | rood |
| Button 1 | Use my extra 10% | [VIP]; knop zet de code via /discount/{{VIP_CODE}}?redirect= in de sessie | groen |
| Button 2 | Apply {{VIP_CODE}} now | [VIP] | groen |
| Button 3 | Use it before midnight ET | [VIP]; [MIDNIGHT-ET] | groen |
| Body | Benjamin here. I made you a code that takes an extra 10% off the Black Friday price: {{VIP_CODE}}, one use, already applied through the button. It stops working {{DEADLINE}}, and there's no second one this weekend. | [VIP]; er komt dit weekend echt geen tweede VIP-code naar dit profiel | oranje Noot: 'no second one this weekend' alleen als Floris VIP-weekend 2 pas op 26 nov doet. Anders schrappen. |
| Resend niet-openers | You missed this: your own extra 10% | [VIP]; [NIET-OPENERS] | oranje |

#### INT

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | VIP ONLY: an extra 10% off this weekend | [VIP] | oranje |
| Subject 2 | YOUR CODE: {{VIP_CODE}} (extra 10%, ends Sunday) | [VIP]; [INT-TZ]: 'Sunday' klopt alleen als de code in de tijdzone van de ontvanger nog op zondag eindigt | oranje |
| Subject 3 | Your extra 10% ends in {{HOURS_LEFT}} hours | [VIP]; {{HOURS_LEFT}} echt op verzendmoment; [NOW] | groen |
| Subject 4 | Final hours: your extra 10% on top | [VIP]; [T-6] | groen |
| Subject 5 | 60 minutes left on your code | [VIP]; [T-60] | oranje |
| Preview 1 | On top of up to 70% off. One use, not on the website. | [VIP] | groen |
| Preview 2 | It stops working {{DEADLINE}}. Then it's the regular Black Friday price. | [VIP]; {{DEADLINE}} met tijdzone | groen |
| Preview 3 | Any pan or set in the sale. Duties paid. | [VIP]; code geldig in alle Markets | groen |
| Hero 1 | VIP only.\|Extra 10% off. | [VIP] | groen |
| Hero 2 | Your code ends\|in {{HOURS_LEFT}} hours | [VIP]; [INT-TZ] | groen |
| Hero 3 | 10% on top\|of Black Friday | [VIP] | groen |
| Countdown T-24h | Your code {{VIP_CODE}} works until {{DEADLINE}}. | [VIP]; [T-24] | groen |
| Countdown T-6h | 6 hours left on {{VIP_CODE}}. | [VIP]; [T-6] | groen |
| Countdown T-1h | Final hour on {{VIP_CODE}}. | [VIP]; [T-60] | oranje |
| Countdown T-15min | {{MINUTES_LEFT}} minutes left on your extra 10%. | [VIP]; [T-15] | rood |
| Button 1 | Use my extra 10% | [VIP] | groen |
| Button 2 | Apply {{VIP_CODE}} now | [VIP] | groen |
| Button 3 | Use it before it ends | [VIP] | groen |
| Body | Benjamin here. I made you a code that takes an extra 10% off the Black Friday price: {{VIP_CODE}}, one use, already applied through the button. It stops working {{DEADLINE}}, then it's the regular Black Friday price again. | [VIP] | groen |
| Resend niet-openers | You missed this: your own extra 10% | [VIP]; [NIET-OPENERS] | oranje |

### 3-credit: CREDIT: Your $X store credit expires tonight

Afzender: Benjamin from Siraat.

Voorwaarde voor de hele mail: [CREDIT-US] (US) / [CREDIT-INT] (INT). Mail bestaat pas als Rise.ai live is.

#### US

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your ${{CREDIT}} expires at midnight ET | [CREDIT-US]; [MIDNIGHT-ET] | groen |
| Subject 2 | Your ${{CREDIT}} is about to disappear | [CREDIT-US]; [T-6] | oranje Noot: Letterlijk Smooche (mail 13). Waar omdat het saldo echt naar nul gaat. |
| Subject 3 | Expires today: ${{CREDIT}} in store credit | [CREDIT-US]; vervaldatum valt op de verzenddag (ET) | groen |
| Subject 4 | Use it or lose it: ${{CREDIT}}, {{HOURS_LEFT}} hours left | [CREDIT-US]; {{HOURS_LEFT}} echt op verzendmoment | oranje |
| Subject 5 | Final hour: your ${{CREDIT}} goes to $0 | [CREDIT-US]; [T-60] | oranje |
| Preview 1 | Earned by your past orders. Applied at checkout, after the sale price. | [CREDIT-US]; tegoed stapelt echt op de saleprijs (Rise gift card) | groen |
| Preview 2 | At {{DEADLINE}} the balance goes to zero. Nothing else changes. | [CREDIT-US] | groen |
| Preview 3 | That's a ${{PAN_AFTER_CREDIT}} Pan Pro, for {{HOURS_LEFT}} more hours. | [CREDIT-US]; {{PAN_AFTER_CREDIT}} = 144 min {{CREDIT}} berekend in Klaviyo; saldo dekt niet meer dan de pan | groen |
| Hero 1 | ${{CREDIT}}\|expires tonight | [CREDIT-US]; [TONIGHT-ET] | groen |
| Hero 2 | Use it\|or lose it | [CREDIT-US] | oranje Noot: Verlies-framing; mag omdat het waar is, maar niet combineren met 'Final hour' in dezelfde mail (te zwaar). |
| Hero 3 | Your ${{CREDIT}}\|ends at midnight ET | [CREDIT-US]; [MIDNIGHT-ET] | groen |
| Countdown T-24h | ${{CREDIT}} left. Expires {{DEADLINE}}. | [CREDIT-US]; [T-24] | groen |
| Countdown T-6h | 6 hours left on your ${{CREDIT}}. | [CREDIT-US]; [T-6] | groen |
| Countdown T-1h | Final hour. Your ${{CREDIT}} goes to $0 at {{DEADLINE}}. | [CREDIT-US]; [T-60] | oranje |
| Countdown T-15min | {{MINUTES_LEFT}} minutes left to use ${{CREDIT}}. | [CREDIT-US]; [T-15] | rood |
| Button 1 | Use my ${{CREDIT}} | [CREDIT-US]; knop opent de shop met het Rise-saldo zichtbaar in checkout | groen |
| Button 2 | Spend it before midnight ET | [CREDIT-US]; [MIDNIGHT-ET] | groen |
| Button 3 | Don't let ${{CREDIT}} expire | [CREDIT-US] | oranje |
| Body | Benjamin here. Your past orders earned you ${{CREDIT}} in store credit, and it's already on your account. At {{DEADLINE}} the balance goes to zero, and I'd rather you cooked with it. It comes off at checkout, on top of the Black Friday price. | [CREDIT-US]; promotionele tegoed, gratis gegeven, vervaldatum in de kleine lettertekst (CA Civil Code 1749.5) | oranje Noot: Juridische regel uit copy.md verplicht onderaan. |
| Resend niet-openers | Your ${{CREDIT}}, last hours | [CREDIT-US]; [NIET-OPENERS]; [T-6] | groen |

#### INT

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your store credit expires in {{HOURS_LEFT}} hours | [CREDIT-INT]; [INT-TZ] | groen |
| Subject 2 | Your store credit is about to disappear | [CREDIT-INT]; [T-6] | oranje |
| Subject 3 | Expires today: your store credit | [CREDIT-INT]; vervaldatum valt op de verzenddag in de tijdzone van de grootste INT-markt (anders 'in {{HOURS_LEFT}} hours') | oranje |
| Subject 4 | Use it or lose it: {{POINTS}} points | [CREDIT-INT]; {{POINTS}} uit Rise | oranje |
| Subject 5 | Final hour: your store credit goes to zero | [CREDIT-INT]; [T-60] | oranje |
| Preview 1 | Earned by your past orders. Applied at checkout, in your currency. | [CREDIT-INT] | groen |
| Preview 2 | When it expires, the balance goes to zero. Nothing else changes. | [CREDIT-INT] | groen |
| Preview 3 | {{POINTS}} points, ready to use for {{HOURS_LEFT}} more hours. | [CREDIT-INT] | groen |
| Hero 1 | Your credit\|expires in {{HOURS_LEFT}} hours | [CREDIT-INT] | groen |
| Hero 2 | Use it\|or lose it | [CREDIT-INT] | oranje |
| Hero 3 | {{POINTS}} points\|gone at {{DEADLINE_SHORT}} | [CREDIT-INT]; {{DEADLINE_SHORT}} met tijdzone | groen |
| Countdown T-24h | {{POINTS}} points left. Expires {{DEADLINE}}. | [CREDIT-INT]; [T-24] | groen |
| Countdown T-6h | 6 hours left on your store credit. | [CREDIT-INT]; [T-6] | groen |
| Countdown T-1h | Final hour. Your credit goes to zero at {{DEADLINE}}. | [CREDIT-INT]; [T-60] | oranje |
| Countdown T-15min | {{MINUTES_LEFT}} minutes left to use your credit. | [CREDIT-INT]; [T-15] | rood |
| Button 1 | Use my store credit | [CREDIT-INT] | groen |
| Button 2 | Spend it before it expires | [CREDIT-INT] | groen |
| Button 3 | Don't let it expire | [CREDIT-INT] | oranje |
| Body | Benjamin here. Your past orders earned you {{POINTS}} points in store credit, already on your account. In {{HOURS_LEFT}} hours the balance goes to zero, and I'd rather you cooked with it. It comes off at checkout in your currency, on top of the Black Friday price. | [CREDIT-INT]; [INT-TZ] | oranje |
| Resend niet-openers | Your store credit, last hours | [CREDIT-INT]; [NIET-OPENERS]; [T-6] | groen |

### 4-last-hours: LAST-HOURS: resend naar openers zonder klik (platte brief Benjamin)

Afzender: Benjamin from Siraat.

Voorwaarde voor de hele mail: [LH]

#### US

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Last hours | [LH]; [T-6] | groen |
| Subject 2 | {{HOURS_LEFT}} hours left | [LH]; {{HOURS_LEFT}} echt op verzendmoment, [NOW] | groen |
| Subject 3 | Benjamin here: it ends in {{HOURS_LEFT}} hours | [LH] | groen |
| Subject 4 | Before it's gone | [LH] | groen |
| Subject 5 | Final hour | [LH]; [T-60] | oranje Noot: Dan is dit de T-1h-mail; niet ook nog de losse final-hour-mail naar hetzelfde profiel. |
| Preview 1 | One short note from me, then I'll leave you alone. | [LH]; dit is echt de laatste mail over deze deadline | groen |
| Preview 2 | {{WHAT_ENDS_SHORT}} ends {{DEADLINE}}. | [LH] | groen |
| Preview 3 | After this, it's the regular Black Friday price. | [LH]; geldt voor flash, VIP en credit; bij gifts/draw de {{AFTER}}-regel uit copy.md | groen |
| Hero 1 | (geen hero: platte tekst) | n.v.t. | groen |
| Hero 2 | Eerste regel: {{WHAT_ENDS}} ends {{DEADLINE}}. | [LH] | groen |
| Hero 3 | Eerste regel: Last hours. Then it's over. | [LH]; [T-6] | groen |
| Countdown T-24h | (niet gebruiken: 'last hours' is pas waar in de laatste 6 uur) | n.v.t. | groen |
| Countdown T-6h | {{WHAT_ENDS}} ends in 6 hours. | [LH]; [T-6] | groen |
| Countdown T-1h | One hour left. {{WHAT_ENDS}} ends {{DEADLINE}}. | [LH]; [T-60] | oranje |
| Countdown T-15min | (niet als platte brief: geen GIF mogelijk, statische minuten verouderen) | n.v.t. | groen |
| Button 1 | Kale link: {{LINK}} | [LH] | groen |
| Button 2 | Here's the link, it ends {{DEADLINE}}: | [LH] | groen |
| Button 3 | Use it here before it ends: | [LH] | groen |
| Body | {{WHAT_ENDS}} ends {{DEADLINE}}. {{AFTER}} If it's for you, this is the moment, and if it isn't, send it back unused within 30 days. | [LH] | groen |
| Resend niet-openers | One more time, then it's over | [LH]; [NIET-OPENERS]; dit is echt de laatste mail over deze deadline | oranje |

#### INT

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Last hours | [LH]; [T-6] | groen |
| Subject 2 | {{HOURS_LEFT}} hours left | [LH]; {{HOURS_LEFT}} echt op verzendmoment, [NOW] | groen |
| Subject 3 | Benjamin here: it ends in {{HOURS_LEFT}} hours | [LH] | groen |
| Subject 4 | Before it's gone | [LH] | groen |
| Subject 5 | Final hour | [LH]; [T-60] | oranje Noot: Dan is dit de T-1h-mail; niet ook nog de losse final-hour-mail naar hetzelfde profiel. |
| Preview 1 | One short note from me, then I'll leave you alone. | [LH]; dit is echt de laatste mail over deze deadline | groen |
| Preview 2 | {{WHAT_ENDS_SHORT}} ends {{DEADLINE}}. | [LH] | groen |
| Preview 3 | After this, it's the regular Black Friday price. | [LH]; geldt voor flash, VIP en credit; bij gifts/draw de {{AFTER}}-regel uit copy.md | groen |
| Hero 1 | (geen hero: platte tekst) | n.v.t. | groen |
| Hero 2 | Eerste regel: {{WHAT_ENDS}} ends {{DEADLINE}}. | [LH] | groen |
| Hero 3 | Eerste regel: Last hours. Then it's over. | [LH]; [T-6] | groen |
| Countdown T-24h | (niet gebruiken: 'last hours' is pas waar in de laatste 6 uur) | n.v.t. | groen |
| Countdown T-6h | {{WHAT_ENDS}} ends in 6 hours. | [LH]; [T-6] | groen |
| Countdown T-1h | One hour left. {{WHAT_ENDS}} ends {{DEADLINE}}. | [LH]; [T-60] | oranje |
| Countdown T-15min | (niet als platte brief: geen GIF mogelijk, statische minuten verouderen) | n.v.t. | groen |
| Button 1 | Kale link: {{LINK}} | [LH] | groen |
| Button 2 | Here's the link, it ends {{DEADLINE}}: | [LH] | groen |
| Button 3 | Use it here before it ends: | [LH] | groen |
| Body | {{WHAT_ENDS}} ends {{DEADLINE}}. {{AFTER}} If it's for you, this is the moment, and if it isn't, send it back unused within 30 days. | [LH] | groen |
| Resend niet-openers | One more time, then it's over | [LH]; [NIET-OPENERS]; dit is echt de laatste mail over deze deadline | oranje |

### 5-gifts: GIFTS: Your 5 free gifts end tonight

Afzender: Siraat.

Voorwaarde voor de hele mail: [GIFTS]. Gratis verzending blijft na de sale, dus nooit 'all 5 gifts end'; zeg 'free gifts' of 'the 4 gifts'.

#### US

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your free gifts end tonight 🎁 | [GIFTS-US]; [TONIGHT-ET] | oranje Noot: 'free' plus emoji: let op promotietab, geen spamtrigger op zich. Nooit 'FREE' in caps. |
| Subject 2 | $555 in gifts, gone at midnight ET | [GIFTS-US]; [MIDNIGHT-ET] | oranje Noot: $555 telt gratis verzending mee, die blijft. Alleen gebruiken als Floris akkoord is dat de waarde als geheel 'gone' heet; anders 'The gifts are gone at midnight ET'. |
| Subject 3 | 6 hours left: 4 free gifts with every order | [GIFTS-US]; [T-6] | groen |
| Subject 4 | Final hour for your free gifts | [GIFTS-US]; [T-60] | oranje |
| Subject 5 | Order in the next 60 minutes, get the gifts | [GIFTS-US]; [T-60] | oranje |
| Preview 1 | Mystery gift, two books and a draw entry. Tomorrow orders ship without them. | [GIFTS-US]; na {{DEADLINE}} echt geen gifts meer | groen |
| Preview 2 | One pan or the whole set, same gifts. Until {{DEADLINE}}. | [GIFTS-US] | groen |
| Preview 3 | The pan stays up to 70% off a little longer. The gifts don't. | [GIFTS-US]; de sale loopt echt langer dan de gifts | rood Noot: Alleen waar bij een gift-deadline vóór 30 nov. Op 30 nov eindigen sale en gifts tegelijk: dan schrappen. |
| Hero 1 | The gifts end\|tonight | [GIFTS-US]; [TONIGHT-ET] | groen |
| Hero 2 | $555 in gifts.\|Gone at midnight ET. | [GIFTS-US]; [MIDNIGHT-ET] | oranje |
| Hero 3 | Last day\|for the free gifts | [GIFTS-US]; verzenddag = laatste giftdag | groen |
| Countdown T-24h | Free gifts end {{DEADLINE}}. | [GIFTS-US]; [T-24] | groen |
| Countdown T-6h | 6 hours left for the free gifts. | [GIFTS-US]; [T-6] | groen |
| Countdown T-1h | Final hour. Order by {{DEADLINE}} and the gifts ship with it. | [GIFTS-US]; [T-60] | oranje |
| Countdown T-15min | {{MINUTES_LEFT}} minutes left for the free gifts. | [GIFTS-US]; [T-15] | rood |
| Button 1 | Claim my free gifts | [GIFTS-US]; gifts worden automatisch toegevoegd (geen code nodig) | groen |
| Button 2 | Order before midnight ET | [GIFTS-US]; [MIDNIGHT-ET] | groen |
| Button 3 | Get the pan + the gifts | [GIFTS-US] | groen |
| Body | Every order placed before {{DEADLINE}} ships with a mystery gift, two books and an entry in the PFAS water filter draw. After that, orders ship without them; free shipping stays. One pan or the whole set, the gifts are the same, so tonight is the night to order. | [GIFTS-US]; [DRAW] (voor de trekkingsregel) | oranje |
| Resend niet-openers | You missed this: the free gifts end tonight | [GIFTS-US]; [NIET-OPENERS]; [TONIGHT-ET] | oranje |

#### INT

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Your free gifts end in {{HOURS_LEFT}} hours 🎁 | [GIFTS]; [INT-TZ] | oranje |
| Subject 2 | The free gifts are gone in {{HOURS_LEFT}} hours | [GIFTS]; [INT-TZ] | groen |
| Subject 3 | 6 hours left: 4 free gifts with every order | [GIFTS]; [T-6] | groen |
| Subject 4 | Final hour for your free gifts | [GIFTS]; [T-60] | oranje |
| Subject 5 | Order in the next 60 minutes, get the gifts | [GIFTS]; [T-60] | oranje |
| Preview 1 | Mystery gift, two books and a draw entry. After that, orders ship without them. | [GIFTS] | groen |
| Preview 2 | One pan or the whole set, same gifts. Until {{DEADLINE}}. | [GIFTS]; {{DEADLINE}} met tijdzone | groen |
| Preview 3 | Free shipping, duties paid, stays. The gifts don't. | [GIFTS] | groen |
| Hero 1 | The gifts end\|in {{HOURS_LEFT}} hours | [GIFTS]; [INT-TZ] | groen |
| Hero 2 | 4 free gifts.\|Last hours. | [GIFTS]; [T-6] | groen |
| Hero 3 | Last day\|for the free gifts | [GIFTS]; laatste giftdag in de tijdzone van de ontvanger | oranje |
| Countdown T-24h | Free gifts end {{DEADLINE}}. | [GIFTS]; [T-24] | groen |
| Countdown T-6h | 6 hours left for the free gifts. | [GIFTS]; [T-6] | groen |
| Countdown T-1h | Final hour for the free gifts. | [GIFTS]; [T-60] | oranje |
| Countdown T-15min | {{MINUTES_LEFT}} minutes left for the free gifts. | [GIFTS]; [T-15] | rood |
| Button 1 | Claim my free gifts | [GIFTS] | groen |
| Button 2 | Order before it ends | [GIFTS] | groen |
| Button 3 | Get the pan + the gifts | [GIFTS] | groen |
| Body | Every order placed before {{DEADLINE}} ships with a mystery gift, two books and an entry in the PFAS water filter draw. After that, orders ship without them; free shipping, duties paid, stays. One pan or the whole set, the gifts are the same. | [GIFTS]; [DRAW] (voor de trekkingsregel) | oranje |
| Resend niet-openers | You missed this: the free gifts end soon | [GIFTS]; [NIET-OPENERS] | oranje |

### 6-draw: DRAW: Order by Sunday midnight to enter this week's filter draw

Afzender: Siraat.

Voorwaarde voor de hele mail: [DRAW]. Elke trekkingsmail draagt 'No purchase necessary' en de regelslink.

#### US

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | This week's draw closes at midnight ET ⏰ | [DRAW]; [MIDNIGHT-ET] | groen |
| Subject 2 | 6 hours left to enter this week's filter draw | [DRAW]; [T-6] | groen |
| Subject 3 | Order in the next hour: you're in this week's draw | [DRAW]; [T-60] | oranje Noot: Nooit 'win a PFAS water filter' zonder 'chance'. 'You're in' klopt alleen met 1 entry per order. |
| Subject 4 | Final hour: this week's PFAS water filter draw | [DRAW]; [T-60] | oranje |
| Subject 5 | You're not in this week's draw yet | [DRAW]; [DRAW-NIET-IN] | rood Noot: Rood tot AMOE-deelnames in Klaviyo zichtbaar zijn: wie via AMOE meedeed krijgt anders een onware mail. |
| Preview 1 | One order, one entry. No purchase necessary, rules inside. | [DRAW] | groen |
| Preview 2 | After {{DEADLINE}}, your order counts for next week's draw instead. | [DRAW]; er IS een volgende wekelijkse trekking (niet in de laatste BF-week) | oranje |
| Preview 3 | And the pan is still up to 70% off, with 4 more gifts. | [DRAW] | groen |
| Hero 1 | This week's draw\|closes tonight | [DRAW]; [TONIGHT-ET] | groen |
| Hero 2 | 6 hours\|to get in | [DRAW]; [T-6] | groen |
| Hero 3 | One order.\|One entry. | [DRAW]; 1 entry per order in de regels | groen |
| Countdown T-24h | This week's draw closes {{DEADLINE}}. | [DRAW]; [T-24] | groen |
| Countdown T-6h | 6 hours left to enter this week's draw. | [DRAW]; [T-6] | groen |
| Countdown T-1h | Final hour. The draw closes at {{DEADLINE}}. | [DRAW]; [T-60] | oranje |
| Countdown T-15min | {{MINUTES_LEFT}} minutes until this week's draw closes. | [DRAW]; [T-15] | rood |
| Button 1 | Order and enter this week | [DRAW] | groen |
| Button 2 | Get in before midnight ET | [DRAW]; [MIDNIGHT-ET] | groen |
| Button 3 | Enter with one pan | [DRAW] | groen |
| Body | Every order placed before {{DEADLINE}} is an entry in this week's PFAS water filter draw. One pan counts the same as the whole set, and the pan itself is still up to 70% off. No purchase necessary, see the rules: {{DRAW_RULES_URL}}. | [DRAW] | oranje Noot: Oranje vanwege kansspelrecht: regels, AMOE en landen moeten kloppen. |
| Resend niet-openers | Last hours to enter this week's draw | [DRAW]; [NIET-OPENERS]; [T-6] | groen |

#### INT

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | This week's draw closes in {{HOURS_LEFT}} hours ⏰ | [DRAW]; [INT-TZ]; INT-landen staan in de regels als toegestaan | groen |
| Subject 2 | 6 hours left to enter this week's filter draw | [DRAW]; [T-6] | groen |
| Subject 3 | Order in the next hour: you're in this week's draw | [DRAW]; [T-60] | oranje |
| Subject 4 | Final hour: this week's PFAS water filter draw | [DRAW]; [T-60] | oranje |
| Subject 5 | You're not in this week's draw yet | [DRAW]; [DRAW-NIET-IN] | rood |
| Preview 1 | One order, one entry. No purchase necessary, rules inside. | [DRAW] | groen |
| Preview 2 | After {{DEADLINE}}, your order counts for next week's draw instead. | [DRAW]; er is een volgende trekking | oranje |
| Preview 3 | And the pan is still up to 70% off, duties paid. | [DRAW] | groen |
| Hero 1 | This week's draw\|closes in {{HOURS_LEFT}} hours | [DRAW]; [INT-TZ] | groen |
| Hero 2 | 6 hours\|to get in | [DRAW]; [T-6] | groen |
| Hero 3 | One order.\|One entry. | [DRAW] | groen |
| Countdown T-24h | This week's draw closes {{DEADLINE}}. | [DRAW]; [T-24] | groen |
| Countdown T-6h | 6 hours left to enter this week's draw. | [DRAW]; [T-6] | groen |
| Countdown T-1h | Final hour before this week's draw closes. | [DRAW]; [T-60] | oranje |
| Countdown T-15min | {{MINUTES_LEFT}} minutes until this week's draw closes. | [DRAW]; [T-15] | rood |
| Button 1 | Order and enter this week | [DRAW] | groen |
| Button 2 | Get in before it closes | [DRAW] | groen |
| Button 3 | Enter with one pan | [DRAW] | groen |
| Body | Every order placed before {{DEADLINE}} is an entry in this week's PFAS water filter draw. One pan counts the same as the whole set, and the pan itself is still up to 70% off, duties paid. No purchase necessary, see the rules: {{DRAW_RULES_URL}}. | [DRAW] | oranje |
| Resend niet-openers | Last hours to enter this week's draw | [DRAW]; [NIET-OPENERS]; [T-6] | groen |

### 7-final-hour: FINAL HOUR mini-mail (generiek, vult {{WHAT_ENDS}} per deadline)

Afzender: Siraat (of Benjamin from Siraat bij VIP/credit).

Voorwaarde voor de hele mail: [FH]

#### US

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Final hour | [FH] | groen |
| Subject 2 | Order now: 60 minutes left | [FH] | oranje |
| Subject 3 | It's gone at midnight ET | [FH]; [MIDNIGHT-ET] | groen |
| Subject 4 | {{MINUTES_LEFT}} minutes left: {{WHAT_ENDS_SHORT}} | [FH]; {{MINUTES_LEFT}} = echte minuten op verzendmoment | oranje |
| Subject 5 | FINAL HOUR ⏰ {{WHAT_ENDS_SHORT}} ends at {{DEADLINE_SHORT}} | [FH] | rood Noot: Maximale Smooche-stand: caps plus emoji. Deliverability rood; Floris kiest. Nooit vaker dan één keer per deadline. |
| Preview 1 | {{WHAT_ENDS}} ends {{DEADLINE}}. One button, that's it. | [FH] | groen |
| Preview 2 | {{AFTER}} | [FH] | groen |
| Preview 3 | Last email about this. Promise. | [FH]; er komt over deze deadline echt geen mail meer | groen |
| Hero 1 | Final hour. | [FH] | groen |
| Hero 2 | 60 minutes.\|Then it's over. | [FH] | groen |
| Hero 3 | Live countdown-GIF + '{{WHAT_ENDS_SHORT}} ends at {{DEADLINE}}' | [FH]; GIF telt af naar exact {{DEADLINE}} en toont daarna 'ENDED' | oranje |
| Countdown T-24h | (n.v.t.: dit is de T-1h-mail) | n.v.t. | groen |
| Countdown T-6h | (n.v.t.) | n.v.t. | groen |
| Countdown T-1h | {{WHAT_ENDS}} ends at {{DEADLINE}}. | [FH] | groen |
| Countdown T-15min | Variant T-15: '15 minutes left. Then {{AFTER_SHORT}}.' | er loopt een echte deadline {{DEADLINE}} (één van mail 1, 2, 3, 5, 6); [T-15]; [NIET-KLIKKERS]; max 3 mails per 24 u per profiel (4 op BF/CM) inclusief deze | rood Noot: Alleen naar klikkers zonder order, alleen met GIF. |
| Button 1 | Order before {{DEADLINE_SHORT}} | [FH] | groen |
| Button 2 | Use it now | [FH] | groen |
| Button 3 | Finish my order | [FH]; alleen naar profielen met Started Checkout in de laatste 48 u (er is een checkout, geen order) | oranje Noot: Nooit 'complete your pending order'. |
| Body | {{WHAT_ENDS}} ends at {{DEADLINE}}, about an hour from now. {{AFTER}} This is the last email about it. | [FH] | groen |
| Resend niet-openers | (geen resend: na de deadline is er niets meer om te resenden; zie mail 8B) | n.v.t. | groen |

#### INT

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | Final hour | [FH] | groen |
| Subject 2 | Order now: 60 minutes left | [FH] | oranje |
| Subject 3 | It's gone in 60 minutes | [FH]; [INT-TZ] | groen |
| Subject 4 | {{MINUTES_LEFT}} minutes left: {{WHAT_ENDS_SHORT}} | [FH]; {{MINUTES_LEFT}} = echte minuten op verzendmoment | oranje |
| Subject 5 | FINAL HOUR ⏰ {{WHAT_ENDS_SHORT}} ends in 60 minutes | [FH] | rood |
| Preview 1 | {{WHAT_ENDS}} ends {{DEADLINE}}. One button, that's it. | [FH] | groen |
| Preview 2 | {{AFTER}} | [FH] | groen |
| Preview 3 | Last email about this. Promise. | [FH]; er komt over deze deadline echt geen mail meer | groen |
| Hero 1 | Final hour. | [FH] | groen |
| Hero 2 | 60 minutes.\|Then it's over. | [FH] | groen |
| Hero 3 | Live countdown-GIF + '{{WHAT_ENDS_SHORT}} ends at {{DEADLINE}}' | [FH]; GIF telt af naar exact {{DEADLINE}} en toont daarna 'ENDED' | oranje |
| Countdown T-24h | (n.v.t.: dit is de T-1h-mail) | n.v.t. | groen |
| Countdown T-6h | (n.v.t.) | n.v.t. | groen |
| Countdown T-1h | {{WHAT_ENDS}} ends at {{DEADLINE}}. | [FH] | groen |
| Countdown T-15min | Variant T-15: '15 minutes left. Then {{AFTER_SHORT}}.' | er loopt een echte deadline {{DEADLINE}} (één van mail 1, 2, 3, 5, 6); [T-15]; [NIET-KLIKKERS]; max 3 mails per 24 u per profiel (4 op BF/CM) inclusief deze | rood Noot: Alleen naar klikkers zonder order, alleen met GIF. |
| Button 1 | Order before it ends | [FH] | groen |
| Button 2 | Use it now | [FH] | groen |
| Button 3 | Finish my order | [FH]; alleen naar profielen met Started Checkout in de laatste 48 u (er is een checkout, geen order) | oranje Noot: Nooit 'complete your pending order'. |
| Body | {{WHAT_ENDS}} ends at {{DEADLINE}}, about an hour from now. {{AFTER}} This is the last email about it. | [FH] | groen |
| Resend niet-openers | (geen resend: na de deadline is er niets meer om te resenden; zie mail 8B) | n.v.t. | groen |

### 8-missed-last-call: YOU MISSED THIS / LAST CALL (8A vóór de deadline naar niet-openers, 8B ná de deadline)

Afzender: Siraat.

Voorwaarde voor de hele mail: 8A vóór de deadline: [NIET-OPENERS]; [T-6] \| 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline)

#### US

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | You missed this | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | oranje Noot: Smooche-resend. Alleen als 8A (nog niet voorbij); preview moet het nog-lopen zeggen. |
| Subject 2 | You missed this: {{WHAT_ENDS_SHORT}}, {{HOURS_LEFT}} hours left | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Subject 3 | Last call: {{WHAT_ENDS_SHORT}} ends at midnight ET | 8A vóór de deadline: [NIET-OPENERS]; [T-6]; [MIDNIGHT-ET]; dit is echt de laatste mail over deze deadline | oranje Noot: 'Last call' alleen in de laatste mail over die specifieke deadline; 'Last chance' alleen op 30 nov. |
| Subject 4 | It ended. Here's what's still on. | 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline) | groen Noot: Eerlijke Smooche-truc ná de deadline: geen nep-verlenging, wel een volgende reden. |
| Subject 5 | You missed the flash price. The gifts are still here. | 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline); gifts lopen echt nog | groen |
| Preview 1 | Still on until {{DEADLINE}}. Then it's gone. | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Preview 2 | {{WHAT_ENDS}} ended {{DEADLINE_PAST}}. Black Friday is still up to 70% off. | 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline); {{DEADLINE_PAST}} = moment dat het echt eindigde | groen |
| Preview 3 | That one is done for good. This is still live: | 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline); er komt voor deze actie echt geen herhaling (Floris bevestigt vooraf) | oranje Noot: Achteraf feitelijk, geen belofte vooraf. Schrappen als de actie later toch terugkomt. |
| Hero 1 | You missed this.\|It's still on. | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Hero 2 | {{HOURS_LEFT}} hours left. | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Hero 3 | It's over.\|This isn't. | 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline) | groen |
| Countdown T-24h | (8A) Still on until {{DEADLINE}}. | 8A vóór de deadline: [NIET-OPENERS]; [T-24] | groen |
| Countdown T-6h | (8A) 6 hours left. Then it's gone. | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Countdown T-1h | (8A) Final hour. Use the final-hour mini-mail (7) instead. | n.v.t. | groen |
| Countdown T-15min | (n.v.t.) | n.v.t. | groen |
| Button 1 | See what I missed | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Button 2 | Use it before midnight ET | 8A vóór de deadline: [NIET-OPENERS]; [T-6]; [MIDNIGHT-ET] | groen |
| Button 3 | Shop what's still on | 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline) | groen |
| Body | 8A: In case it got buried: {{WHAT_ENDS}} ends {{DEADLINE}}, and you haven't opened it yet. Here it is again, one button. / 8B: {{WHAT_ENDS}} ended {{DEADLINE_PAST}}, and it won't return. What is still on: up to 70% off and the free gifts until the end of Black Friday. | 8A vóór de deadline: [NIET-OPENERS]; [T-6] / 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline) | oranje Noot: 8B alleen als de actie echt niet terugkomt. 'won't return' in plaats van 'coming back' (BRIEF verbiedt 'coming'). |
| Resend niet-openers | (dit is zelf de resend) | n.v.t. | groen |

#### INT

| Veld | Copy (English) | Waar als | Risico |
| --- | --- | --- | --- |
| Subject 1 | You missed this | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | oranje Noot: Smooche-resend. Alleen als 8A (nog niet voorbij); preview moet het nog-lopen zeggen. |
| Subject 2 | You missed this: {{WHAT_ENDS_SHORT}}, {{HOURS_LEFT}} hours left | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Subject 3 | Last call: {{WHAT_ENDS_SHORT}} ends in {{HOURS_LEFT}} hours | 8A vóór de deadline: [NIET-OPENERS]; [T-6]; [INT-TZ]; laatste mail over deze deadline | oranje |
| Subject 4 | It ended. Here's what's still on. | 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline) | groen Noot: Eerlijke Smooche-truc ná de deadline: geen nep-verlenging, wel een volgende reden. |
| Subject 5 | You missed the flash price. The gifts are still here. | 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline); gifts lopen echt nog | groen |
| Preview 1 | Still on until {{DEADLINE}}. Then it's gone. | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Preview 2 | {{WHAT_ENDS}} ended {{DEADLINE_PAST}}. Black Friday is still up to 70% off. | 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline); {{DEADLINE_PAST}} = moment dat het echt eindigde | groen |
| Preview 3 | That one is done for good. This is still live: | 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline); er komt voor deze actie echt geen herhaling (Floris bevestigt vooraf) | oranje Noot: Achteraf feitelijk, geen belofte vooraf. Schrappen als de actie later toch terugkomt. |
| Hero 1 | You missed this.\|It's still on. | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Hero 2 | {{HOURS_LEFT}} hours left. | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Hero 3 | It's over.\|This isn't. | 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline) | groen |
| Countdown T-24h | (8A) Still on until {{DEADLINE}}. | 8A vóór de deadline: [NIET-OPENERS]; [T-24] | groen |
| Countdown T-6h | (8A) 6 hours left. Then it's gone. | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Countdown T-1h | (8A) Final hour. Use the final-hour mini-mail (7) instead. | n.v.t. | groen |
| Countdown T-15min | (n.v.t.) | n.v.t. | groen |
| Button 1 | See what I missed | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Button 2 | Use it before it ends | 8A vóór de deadline: [NIET-OPENERS]; [T-6] | groen |
| Button 3 | Shop what's still on | 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline) | groen |
| Body | 8A: In case it got buried: {{WHAT_ENDS}} ends {{DEADLINE}}, and you haven't opened it yet. Here it is again, one button. / 8B: {{WHAT_ENDS}} ended {{DEADLINE_PAST}}, and it won't return. What is still on: up to 70% off and the free gifts until the end of Black Friday. | 8A vóór de deadline: [NIET-OPENERS]; [T-6] / 8B ná de deadline: deadline {{DEADLINE}} is echt voorbij en het aanbod is echt weg; ontvangers = kregen bronmail, geen order; er loopt nog iets anders echts (sale tot 30 nov of een volgende deadline) | oranje Noot: 8B alleen als de actie echt niet terugkomt. 'won't return' in plaats van 'coming back' (BRIEF verbiedt 'coming'). |
| Resend niet-openers | (dit is zelf de resend) | n.v.t. | groen |

## 4. Smooche doet dit, wij niet

| Smooche | Waarom niet |
| --- | --- |
| Your order is pending. / Pending orders not completed within 24 hours will be marked as canceled. | Er bestaat geen order; misleidend onderwerp (CAN-SPAM 15 USC 7704(a)(2)) en nep-orderstatus (FTC Act sectie 5). Wel: 'Your checkout is still open' naar echte Started Checkout. |
| (1) Your store credit is updated. | '(1)' doet zich voor als ongelezen notificatie en er is niets bijgewerkt; misleidend onderwerp. |
| I extended your credit by 24 hours (until tonight). It cannot be extended again. | Verzonnen handeling en geplande nep-verlenging; maakt de eerste 'expires today' achteraf vals. BRIEF verbiedt 'no extensions' en verzonnen tegoed. |
| The sale ends tonight at midnight. No extensions this time. | Hun sale liep door; bij ons loopt BF tot 30 nov, dus 'sale ends tonight' vóór 30 nov is een valse deadline (FTC dark patterns-rapport 2022, EU UCPD bijlage I punt 7). |
| Running pretty low on stock / selling out fast / only while current stock lasts | Zonder echte voorraaddata per markt is dit valse schaarste. Ook bij ons de 12-delige set niet pushen (0 bij ShipBob). |
| Yesterday we added $12.24 to your account. Our customer support team just checked and noticed you haven't used it. | Verzonnen tegoed (eigenlijk een kortingscode met $30 minimum) en verzonnen supportcheck. Wij alleen echt Rise-saldo, en geen nep-handeling. |
| Expires Today-zegel op een code die morgen gewoon weer werkt / aftelklok die reset | Nep-countdown: FTC noemt dit expliciet misleidend. Onze GIF telt naar de echte backend-tijd en toont daarna 'ENDED'. |
| VIP ONLY ... YOUR PASSWORD: SMOOCHEVIP (vaste code) | Een vaste code lekt naar couponsites; dan is 'VIP only' niet meer waar. Wij: unieke {{VIP_CODE}} per profiel, one use. |
| Free shipping has been activated for you | Gratis verzending geldt voor iedereen; 'activated for you' suggereert een persoonlijke handeling die niet bestaat. |
| Try your luck... see what you win (iedereen wint hetzelfde) | Valse indruk van winst (EU UCPD bijlage I punt 31); bij ons geen 'win' zonder 'chance' en regels. |
| Final hours / about to disappear terwijl er niets eindigt | Smooche gebruikt 'final hours' als stijl; bij ons alleen in de laatste 6 uur van een echte deadline. |
| Your cart is reserved / price held / next batch | Expliciet verboden in DECISIONS (1 nov); de winkelwagen houdt geen prijs vast. |
| Persona die verzonnen dingen doet ('Chloe: I extended...') | Benjamin bestaat; hij zegt alleen wat echt gebeurd is ('I made you a code' alleen als de code echt voor dit segment is gemaakt). |
| Sterren zonder bron of aantal | FTC-regel nepreviews (2024); wij alleen letterlijke geverifieerde reviews met naam en ID. |

## 5. Controle

- Geen em dash of en dash in het hele bestand (script-check).
- Geen verboden woorden in de copy: next batch, reserve, coming, price held, pending order, no extensions, purifier, lifetime, free filter, shop now (script-check; 'pending' en 'no extensions' staan alleen in sectie 4 als citaat van Smooche).
- INT-copy zonder valutateken (script-check).
- Geen echte BF-code; {{VIP_CODE}} en BFCODE zijn placeholders.

## 6. Besluiten Floris

1. Tijdzone per deadline: één ET-eindtijd met 'midnight ET' in de copy, of de US-lijst per tijdzone splitsen met eigen code-einde?
2. Live countdown-GIF (Sendtric/NiftyImages) ja of nee? Zonder GIF vallen alle T-15min-regels af.
3. Mag de reeks T-24h / T-6h / T-1h per deadline, met de segmentering hierboven (max 3 per 24 u)?
4. '$555 in gifts, gone at midnight' (gratis verzending blijft) of liever 'The gifts are gone at midnight ET'?
5. Trekking: AMOE-deelnames als event in Klaviyo, zodat 'You're not in this week's draw yet' waar kan zijn?
6. Mail 8B (na de deadline 'It ended. Here's what's still on.'): toevoegen aan de kalender na elke flash en VIP-weekend?
