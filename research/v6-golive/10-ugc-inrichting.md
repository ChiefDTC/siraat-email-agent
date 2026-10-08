# 10 · UGC-inrichting (U1 "Show us your first egg?")

Ingericht op 8 oktober 2026 met toestemming van Floris. Geen klantberichten verstuurd, geen bestaande macro's, regels of AI-agent-instellingen aangepast, geen producten aangeraakt.

## Wat er staat

### Shopify
| Onderdeel | Waarde |
| --- | --- |
| Korting | "UGC15 · foto first egg (Gorgias)" |
| ID | `gid://shopify/DiscountCodeNode/2359038640468` |
| Type | Basiskorting met code, 15% op de hele bestelling (alle producten) |
| Codes | 300 unieke codes, formaat `UGC15-XXXXXX` (6 tekens uit 32 tekens zonder 0/O/1/I, cryptografisch willekeurig: ruim 1 miljard combinaties). 1 aangemaakt met de korting, 299 via `discountRedeemCodeBulkAdd` (250 + 49, 0 mislukt). |
| Gebruik | Usage limit 1 (geldt per code bij een korting met meerdere codes), één keer per klant |
| Minimum | Geen |
| Combineert met | Productkortingen: ja (FREE GIFT BXGY blijft werken). Verzendkortingen: ja (gratis verzending blijft). Orderkortingen: nee (niet stapelen met HI10 of andere codes). |
| Looptijd | Start 8 okt 2026, einddatum 31 dec 2027 23:59 UTC |
| Status | Actief |

**Waarom een einddatum van 31 dec 2027 en geen open einde.** Shopify kent geen geldigheidsduur per code: alle codes delen de start- en einddatum van de korting. De 60 dagen per klant zijn dus hoe dan ook handwerk. Een lange einddatum is een vangnet: als het proces stilvalt of codes uitlekken, verlopen ze vanzelf in plaats van eeuwig geldig te blijven. Vóór december 2027 een nieuwe pool aanmaken (zie "Onderhoud").

**Hoe we de 60 dagen handhaven.** De CSV houdt per code `uitgegeven_op` en `verloopt_op` bij. Eens per maand: codes met `verloopt_op` in het verleden die niet gebruikt zijn, verwijderen uit de korting in Shopify (Kortingen, UGC15, codelijst, code verwijderen). Daarmee is de belofte "60 dagen" echt, ook al staat er technisch een langere einddatum op de korting.

### Codelijst
- Bestand: `research/v6-golive/ugc15-codes.csv` (kolommen: `code`, `status` vrij/uitgegeven, `uitgegeven_op`, `ticket`, `verloopt_op`). 300 regels, alle op `vrij`.
- **Let op: deze repo is publiek op GitHub.** Het bestand staat daarom in `.gitignore` en gaat niet mee in een commit. Support moet de lijst ergens privé kunnen bewerken (zie "Wat Floris nog moet doen").

### Gorgias
| Onderdeel | Waarde |
| --- | --- |
| Tag | `ugc-photo` (id 1937596), nieuw aangemaakt |
| Macro | "UGC · first egg foto (UGC15)" (id 404432), https://siraatskitchen.gorgias.com/app/settings/macros/404432 |
| Macro doet | Antwoordtekst (Engels) met placeholder `[UGC15-CODE]`, tag `ugc-photo`, interne notitie voor de supportmedewerker |

Tekst van de macro (ondertekend "The Siraat team"):

> Hi {{firstname}},
> Thank you for the photo. We love it. This is exactly why we make these pans: real food, in real kitchens.
> Here's your thank you: **[UGC15-CODE]**
> It gives you 15% off your next order. Use it once, within 60 days. It works together with the free gifts on your order, so you keep those too.
> One small question: may we share your photo on siraatskitchen.com and on our social channels, with your first name only? Just reply "yes". Rather keep it private? That's completely fine, the code is yours either way.
> Happy cooking, The Siraat team

De code hangt niet af van toestemming (zo belooft U1 het ook: "You still get your code"). Controleer bij het eerste gebruik of de Gorgias-e-mailhandtekening van support@ geen tweede ondertekening toevoegt.

### Kan een macro zelf een Shopify-code maken of uit een pool halen?
- Via de API/MCP niet: de beschikbare macro-acties zijn tekst, tags, status, toewijzen, notitie, e-mail, custom field en een andere macro. Er is geen actie "maak Shopify-korting" of "pak code uit pool".
- In de Gorgias-interface heeft de Shopify-integratie (gekoppeld: winkel 2d0add-d6) wel een kortingsknop in het antwoordvenster waarmee een medewerker een Shopify-kortingscode invoegt of een unieke code genereert op basis van een bestaande korting. **Optie:** als die knop codes op de UGC15-korting kan genereren, vervalt de handmatige lijst (Shopify telt dan zelf). Niet ingesteld: eerst in de UI testen op één testticket, en dan beslissen. Tot die tijd geldt de lijst.

### Regel voor automatisch taggen (beschreven, niet aangemaakt)
Een Gorgias-regel kan antwoorden op U1 met een foto vooraf taggen, zodat ze in een eigen view komen:
- **Trigger:** ticket created (en message created op een bestaand ticket).
- **Voorwaarden:** kanaal = e-mail, ontvanger = support@siraatskitchen.com, onderwerp bevat "first egg" (de knop in U1 zet "My first egg" als onderwerp; bij "reply" begint het onderwerp met "Re: Show us your first egg?"), en het bericht heeft een bijlage (afbeelding).
- **Acties:** tag `ugc-incoming` (of direct `ugc-photo`), eventueel toewijzen aan het supportteam. Geen automatisch antwoord: de code moet handmatig uit de lijst.
- Zonder bijlage maar met onderwerp "first egg": alleen taggen `ugc-question`, want dat is vaak een kookvraag ("egg stuck").
- Let op: de AI Agent staat op e-mail uit (email_enabled = false), dus deze tickets komen bij mensen terecht. Zo houden.

## Werkproces voor support (5 stappen)
1. **Foto komt binnen.** Een klant antwoordt op U1 (onderwerp "My first egg" of "Re: Show us your first egg?") met een foto. Controleer kort: is het een eigen foto van iets gekookt in een Siraat-pan? Alleen een vraag of een probleem (ei plakt)? Dan eerst helpen, macro pas als er een foto is.
2. **Macro toepassen.** Kies "UGC · first egg foto (UGC15)". De tag `ugc-photo` en een interne notitie worden toegevoegd.
3. **Code invullen en markeren.** Pak de bovenste code met status `vrij` uit de UGC15-lijst, vervang `[UGC15-CODE]` in het antwoord, en zet in de lijst: status `uitgegeven`, `uitgegeven_op` = vandaag, `ticket` = ticketnummer, `verloopt_op` = vandaag + 60 dagen. Eén code per klant: zoek eerst in de lijst of de klant al een code kreeg. Verstuur.
4. **Toestemming afwachten.** Antwoordt de klant "yes" (of iets vergelijkbaars), dan mag de foto gebruikt worden. Schreef de klant "private", of geen reactie: foto niet hergebruiken.
5. **Foto opslaan met toestemming.** Alleen bij "yes": foto downloaden en opslaan in de gedeelde UGC-map met bestandsnaam `JJJJMMDD_voornaam_ticketnummer`, en in de map/het overzicht noteren: voornaam, ticketnummer, datum toestemming. Trekt een klant later toestemming in, foto verwijderen en overal offline halen.

## Wat Floris nog moet doen
1. **Codelijst privé neerzetten.** Bijvoorbeeld een Google Sheet die alleen het supportteam kan bewerken, gevuld uit `ugc15-codes.csv` (lokaal bestand, niet in GitHub). Daarna is de sheet de enige bron; het CSV-bestand alleen als back-up.
2. **Supportteam uitleggen:** de 5 stappen hierboven, waar de lijst staat, en dat de code nooit afhangt van toestemming.
3. **Gedeelde UGC-map aanwijzen** (Drive of Shopify Files met prefix `ugc-`) voor foto's met toestemming.
4. **Beslissen over de kortingsknop in Gorgias** (testen op één testticket) en over de autotag-regel hierboven.
5. **Maandelijks onderhoud toewijzen:** verlopen, ongebruikte codes uit Shopify verwijderen; bij minder dan 50 vrije codes een nieuwe batch toevoegen; vóór december 2027 een nieuwe pool met nieuwe einddatum.
6. **Eén testronde:** een code uit de lijst gebruiken in een testcheckout om te bevestigen dat 15% plus FREE GIFT samen werken en dat de code daarna niet opnieuw werkt.
