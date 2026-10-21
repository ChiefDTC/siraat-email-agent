# Social Snowball · hoe het werkt bij Siraat (21 okt 2026)

Vragen: werkt de affiliatecode ook als een vriend hem intypt, hoe staat de korting in Shopify, welke portal zien affiliates, hoe werken uitbetalingen en welke regels (tiers, plafond, alleen nieuwe klanten, zelfverwijzing, attributievenster) bestaan er.

Werkwijze: alles alleen gelezen. Shopify via read-only GraphQL, Klaviyo via GET op events van XzrVJZ (alleen om drie voorbeeldcodes te vinden; geen persoonsgegevens in dit bestand). help.socialsnowball.io en socialsnowball.io waren via de proxy niet bereikbaar (DNS-fout), net als apps.shopify.com; webinformatie komt daarom uit zoekresultaten (snippets) van die pagina's. Markering: **[Shopify]** = zelf gezien in de winkel, **[SS-help]** = uit zoeksnippet van het Snowball-helpcenter of -blog, **[derden]** = review of concurrent, **[niet geverifieerd]** = niet bevestigd.

## Kort antwoord

1. **Intypen werkt.** Elke affiliatecode (voornaam + 5 cijfers) bestaat als echte kortingscode in Shopify. Een vriend die de code met de hand invoert krijgt dezelfde 10%. De link doet hetzelfde automatisch. [Shopify] Of Snowball de handmatig getypte code ook als verwijzing telt: volgens de docs wel (codegebruik is de basis van code-tracking), maar met een testorder bevestigen. [SS-help, niet geverifieerd voor Siraat]
2. **Eén gedeelde korting voor het hele programma**, aangemaakt op 12 okt 2026: "Default program - DO NOT DELETE", 10% op de hele order, voor iedereen (ook bestaande klanten), onbeperkt herbruikbaar, combineert met niets. Per affiliate komt er een code bij in die korting (nu 460 codes, 0 keer gebruikt). [Shopify]
3. **Portal:** standaard `affiliates.socialsnowball.io/auth/affiliate/login`. Geen bewijs voor een eigen portal-domein (zoals affiliates.siraatskitchen.com). Wel draaien de affiliatelinks al op siraatskitchen.com. Niet nodig.
4. **Uitbetaling:** wachttijd instelbaar in dagen na plaatsing of na verzending (blog noemt ook levering); schema bepaalt het merk; Tremendous mailt de affiliate een claimlink, die kiest zelf uit de methodes die Siraat in de Tremendous-campagne aanzet.
5. **Regels:** zelfverwijzing blokkeren (zelfde e-mail of IP) bestaat, alleen-gefulfilde-orders bestaat, attributievenster 1 tot 365 dagen, alleen nieuwe klanten via een klantsegment op de korting, automatische tiers op prestatie genoemd; een plafond per order niet gevonden.

## 1. Codetype "tracking link"

### Wat de bronnen zeggen

- Snowball kent drie manieren van tracken: **discount code** (affiliate deelt een code), **UTM/tracking link** (link zonder korting, alleen cookie) en **discount link** (link die een korting toepast). Sinds juni 2024 kan het samen: toggle "Apply discount code with the tracking links" onder Tracking Settings, met een vaste of procentuele korting. [SS-help, blog: [generate both discount codes and UTM links](https://www.socialsnowball.io/post/generate-both-discount-codes-and-utm-links-for-affiliates), [UTM links](https://help.socialsnowball.io/en/articles/6457463-tracking-affiliate-sales-with-utm-links), [both codes and links](https://help.socialsnowball.io/en/articles/6846640-how-to-provide-affiliates-with-both-discount-codes-and-utm-links)]
- **Safelinks**: een variant van de tracking link die bij elke klik een unieke code voor eenmalig gebruik maakt, in een cookie bewaart en in de checkout toepast. Gebruikt de klant de code niet, dan telt de cookie nog. Alleen Shopify. [SS-help: [Safelinks: everything you need to know](https://help.socialsnowball.io/en/articles/7953430-safelinks-everything-you-need-to-know), [BusinessWire juni 2023](https://www.businesswire.com/news/home/20230612005071/en/Social-Snowball-Launches-Safelinks-A-Leap-in-E-commerce-Affiliate-Marketing---Solving-Coupon-Code-Leakage-Problem); derden: [Modash](https://www.modash.io/blog/ecommerce-affiliate-software-tools)]
- Attributie is volgens een concurrent vooral last-click binnen Shopify. [derden: [Tapfiliate](https://tapfiliate.com/blog/social-snowball-review/)] Wat wint als op één order een code van affiliate A en een cookie van affiliate B zitten: niet gevonden. [niet geverifieerd]

### Wat er in de winkel staat [Shopify]

| Kenmerk | Waarde |
| --- | --- |
| Korting | `Default program - DO NOT DELETE` (DiscountCodeBasic), actief sinds 12 okt 2026, geen einddatum |
| Waarde | 10% op alle producten, klasse ORDER |
| Wie mag hem gebruiken | iedereen (`DiscountBuyerSelectionAll`), dus **ook bestaande klanten** |
| Eén keer per klant | nee (`appliesOncePerCustomer = false`) |
| Gebruikslimiet | geen |
| Minimum orderbedrag | geen |
| Combineert met | **niets** (order-, product- en verzendkortingen allemaal `false`): stapelt dus niet met HI10, flowcodes of andere codes |
| Aantal codes | 460 (ongeveer gelijk aan de 437 inschrijvingen via aankoop, XzrVJZ), waarvan in de eerste 50 tien in het patroon `DISC` + 6 cijfers, de rest voornaam + 5 cijfers |
| Gebruik | 0 (geen enkele order met een programmacode tot nu) |

- Drie willekeurige affiliatecodes uit Klaviyo-profielen: alle drie **gevonden** in Shopify, alle drie in deze ene korting.
- De link `https://www.siraatskitchen.com/<CODE>` is een **Shopify URL-redirect** (pad `/<code>` in kleine letters) naar `https://www.siraatskitchen.com/?snowball=<CODE>`. Het Snowball-script op de site leest die parameter, zet de cookie en past de korting toe. Het domein is dus gewoon siraatskitchen.com (dit beantwoordt B5 uit 03-flowstructuur: ja).
- **Hoe Snowball de korting maakt:** niet één korting per affiliate en niet per klik, maar één programmakorting ("discount folder", genoemd naar het programma) waaraan Snowball bij elke nieuwe affiliate een code toevoegt. Dat klopt met de helpcenter-tekst over de "program's discount folder". [SS-help: [stacking](https://help.socialsnowball.io/en/articles/8456197-stacking-affiliate-discount-codes-with-other-discount-codes-from-shopify)]
- **Safelinks bij Siraat:** onze Klaviyo-template zegt dat de link bij elke klik een unieke code maakt. De tien `DISC`-codes kunnen zulke klikcodes of testcodes zijn; aparte per-klik-kortingen zien we niet (geen nieuwe kortingen met een Snowball-titel). Met 0 gebruik valt niet vast te stellen of de link de eigen code van de affiliate of een unieke klikcode toepast. [niet geverifieerd: testklik plus testorder]

### Gevolgen

- **Code in mails tonen kan**: Klaviyo-profieleigenschap `Referral Code - SocialSnowball` (naast `Referral Link - SocialSnowball`). Omdat de code ook handmatig werkt, is "Or tell them your code: {{ code }}" eerlijk. Nadeel: een getypte code kan op couponsites lekken (de korting heeft geen beperking per klant). Advies: in mails de link voorop, code als tweede regel.
- **Alleen nieuwe klanten staat nu uit.** Bestaande klanten kunnen elkaars code gebruiken, ook herhaald. Instellen kan in Snowball onder Advanced Settings, veld "Discount codes apply to", met een segment van klanten zonder eerdere aankoop. [SS-help: [restrict code usage to segments](https://help.socialsnowball.io/en/articles/6846628-how-to-restrict-affiliate-code-usage-to-specific-customer-segments)] Niet in Shopify zelf wijzigen; Snowball beheert deze korting ("DO NOT DELETE").
- **Stapelen staat uit**, conform het advies in 04-commissie-economie. Let op: de sale zit in de productprijs (geen korting), dus de 10% komt bovenop de saleprijs. De automatische Aftersell-korting kan niet samen met de programmacode gebruikt worden (combinesWith false); niet getest wat de klant dan ziet. [niet geverifieerd]

## 2. Affiliateportal

- **Standaard login:** `https://affiliates.socialsnowball.io/auth/affiliate/login` (aanmelden: `/auth/affiliate/signup`). Affiliates verifiëren eerst hun e-mail. [SS-help: [setting up your affiliate account](https://help.socialsnowball.io/en/articles/5325092-setting-up-your-affiliate-account), [how do affiliates get access](https://help.socialsnowball.io/en/articles/5325081-how-do-affiliates-get-access-to-their-dashboard)]
- **Wat affiliates zien:** hun sales en payouts, plus een tab **Payout Methods** waar ze, afhankelijk van wat het merk aanzet, gegevens invullen. Voor Tremendous en store credit hoeven ze niets in te vullen. Link en code staan in het dashboard [niet geverifieerd in detail; clicks per link niet bevestigd]. [SS-help: [payout credentials](https://help.socialsnowball.io/en/articles/5325079-an-affiliate-hasn-t-input-their-payout-credentials-yet-what-should-i-do)]
- **Eigen portal of domein:** geen bron gevonden voor een white-label portal op een eigen (sub)domein, op geen enkel plan. Wat wel bestaat: "custom affiliate link subdomains" in de prijsvergelijking (plan niet zichtbaar in de snippet), en de affiliatelinks gebruiken standaard het primaire Shopify-domein. [SS-help: [change subdomain of affiliate links](https://help.socialsnowball.io/en/articles/6656287-how-to-change-the-subdomain-of-your-affiliate-links), [pricing](https://www.socialsnowball.io/pricing)] Branding gaat over aanmeldformulier (kleuren, afbeelding, CSS), bedankpagina en mails; een betaald plan verwijdert Snowball-branding. Dashboard-branding is volgens een concurrent beperkt tot een logo. [SS-help: [sign-up form](https://help.socialsnowball.io/en/articles/5535127-customizing-the-affiliate-sign-up-form); derden: [Tapfiliate](https://tapfiliate.com/blog/social-snowball-review/), [Influencer Marketing Hub](https://influencermarketinghub.com/social-snowball/)]
- **Nodig?** Nee. De links staan al op siraatskitchen.com; de portal is alleen voor wie zijn verdiensten wil bekijken. De mails moeten wel naar de **login**-URL linken, niet naar signup of de oude `socialsnowball.io/login-form` (zie 02-klaviyo-audit).
- Achtergrond: Snowball is in juni 2025 overgenomen door Dotdigital. [derden, niet geverifieerd]

## 3. Uitbetaling

| Onderdeel | Wat bestaat | Bron |
| --- | --- | --- |
| Wachttijd | Commission filter **Custom Delay** (Settings > Commission Filters): elk aantal dagen na **plaatsing** of na **verzending** van de order; het blog noemt ook **levering**. Status "Pending custom delay", daarna "Ready". Bedoeld om de retourtermijn te overbruggen: geretourneerde orders vervallen vóór uitbetaling | [SS-help custom delay](https://help.socialsnowball.io/en/articles/6878881-setting-up-custom-delay-commission-filters-to-create-a-maturation-period-for-payouts), [blog filters](https://www.socialsnowball.io/post/use-filters-to-automate-when-affiliate-commissions-are-sent), [pending custom delay](https://help.socialsnowball.io/en/articles/5864095-a-commission-status-is-pending-custom-delay-what-does-this-mean) |
| Alleen gefulfilde orders | Aparte filter: commissie pas na fulfilment ("Pending order fulfillment") | [SS-help fraud guide](https://help.socialsnowball.io/en/articles/5382070-protecting-against-fraud-a-complete-guide) |
| Minimum | Alleen gevonden voor Trolley (bankoverschrijving): "Payment Minimums" in de Snowball-instellingen. Algemeen minimum voor Tremendous niet gevonden | [SS-help Trolley](https://help.socialsnowball.io/en/articles/8680105-setting-up-trolley-integration-to-send-payouts-to-your-affiliates), [niet geverifieerd] |
| Schema | Het merk bepaalt het ritme (wekelijks, tweewekelijks, maandelijks). Een vaste maanddatum als instelling niet gevonden; uitbetalen gebeurt vanuit de Payouts-tab (in bulk). Of automatisch op een datum kan: niet bevestigd | [SS-help Tremendous ontvangen](https://help.socialsnowball.io/en/articles/5551709-receiving-payouts-to-your-email-via-tremendous), [niet geverifieerd] |
| Methodes | Quick cash (Tremendous, Trolley, nieuw: Snowpay), quick store credit, handmatig | [SS-help how do I pay](https://help.socialsnowball.io/en/articles/5325094-how-do-i-pay-an-affiliate-their-commission), [Snowpay](https://help.socialsnowball.io/en/articles/15886485-receiving-payouts-via-snowpay) |
| Tremendous-flow | Siraat maakt een Tremendous-account, vult het saldo en maakt een campagne die bepaalt welke methodes de affiliate mag kiezen (goedkeuring tot enkele dagen). Bij uitbetaling mailt Tremendous de affiliate (afzender `rewards@reward.tremendous.com`) met een Redeem-knop; de affiliate heeft geen account nodig en kiest op de claimpagina zelf: PayPal, bankoverschrijving, gift cards (o.a. Amazon), Visa prepaid, Venmo (alleen als aangezet, via telefoonnummer). Gift cards direct, PayPal en bank een paar dagen. Vanaf $600 per jaar op hetzelfde e-mailadres vraagt Tremendous een W-9 | [SS-help Tremendous setup](https://help.socialsnowball.io/en/articles/5544038-setting-up-the-tremendous-integration-for-quick-and-easy-commission-payouts), [SS-help ontvangen](https://help.socialsnowball.io/en/articles/5551709-receiving-payouts-to-your-email-via-tremendous), [Tremendous Venmo](https://help.tremendous.com/hc/en-us/articles/39976727588115-Venmo-payouts) |
| Status zonder methode | "Pending enabled payout methods" zolang Siraat geen methode aanzet | [SS-help](https://help.socialsnowball.io/en/articles/5864671-a-commission-status-is-pending-enabled-payout-methods-what-does-this-mean) |

Aansluiting op het besluit (05-aanbod-besluit): 45 dagen wachttijd na plaatsing, of 30 dagen na verzending, past in Custom Delay. Een minimum van $50 voor Tremendous is als instelling niet bevestigd; zonder minimum kan Siraat het in de maandelijkse batch zelf handhaven (alleen "Ready" boven $50 uitbetalen). [niet geverifieerd]

## 4. Programmaregels

| Regel | Bestaat? | Hoe | Bron |
| --- | --- | --- | --- |
| Tiers | Ja, volgens het blog: affiliates automatisch naar hogere commissie op basis van prestatie; daarnaast meerdere programma's (aparte commissie per groep). Drempels en werking niet gevonden | [blog How ecommerce brands use SS](https://www.socialsnowball.io/post/how-ecommerce-brands-use-social-snowball-affiliate-marketing-customer-referrals), [niet geverifieerd] |
| Plafond per order | Niet gevonden | [niet geverifieerd] |
| Alleen nieuwe klanten | Op de korting: segment "nog geen aankoop" in "Discount codes apply to". Een aparte commissieregel niet gevonden (helpcenter heeft een artikel "How to restrict affiliate purchases to new customers only", inhoud niet gelezen). Nu bij Siraat **uit** | [SS-help segments](https://help.socialsnowball.io/en/articles/6846628-how-to-restrict-affiliate-code-usage-to-specific-customer-segments), [Shopify] |
| Zelfverwijzing blokkeren | Ja: geen commissie als klant en affiliate hetzelfde e-mailadres of IP-adres hebben | [SS-help fraud guide](https://help.socialsnowball.io/en/articles/5382070-protecting-against-fraud-a-complete-guide) |
| Attributievenster | Ja: cookieduur 1 tot 365 dagen bij linkprogramma's; merken gebruiken 14 of 30 dagen | [SS-help UTM links](https://help.socialsnowball.io/en/articles/6457463-tracking-affiliate-sales-with-utm-links), [derden: merkvoorwaarden](https://badbirdiegolf.com/pages/affiliate-terms) |
| Eerste vs herhaalorder | Alleen voor abonnementen (Skio) apart in te stellen | [SS-help Skio](https://help.socialsnowball.io/en/articles/10421729-integrating-social-snowball-with-skio-to-create-recurring-commissions) |
| Stapelen | Via Shopify Combinations op de programmakorting; nu uit | [SS-help stacking](https://help.socialsnowball.io/en/articles/8456197-stacking-affiliate-discount-codes-with-other-discount-codes-from-shopify), [Shopify] |

## 5. Wat Floris kan doen (in het Snowball-dashboard)

1. **Portal:** niets bouwen. Wel in Settings kijken of er een logo voor de portal in te stellen is en daar het Siraat-lockup zetten. Voor de mails: bevestigen dat `affiliates.socialsnowball.io/auth/affiliate/login` de juiste login is (of welke URL het dashboard zelf toont).
2. **Advanced Settings > Discount codes apply to:** segment "geen eerdere aankoop" als de vriendenkorting alleen voor nieuwe klanten moet gelden (advies uit 04).
3. **Commission Filters:** Custom Delay aan (45 dagen na plaatsing of 30 dagen na verzending), zelfverwijzing blokkeren aan, eventueel alleen gefulfilde orders.
4. **Tracking Settings:** cookieduur noteren (advies 30 dagen) en of Safelinks aan staat.
5. **Eén testorder** via een eigen testaffiliate: eenmaal via de link, eenmaal met de code getypt, om te zien welke code in de checkout komt en of beide als verwijzing tellen.
