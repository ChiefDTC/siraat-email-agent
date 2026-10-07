# 03 · Voorstel: selecteren, doseren, afscheid nemen en bewaken

Datum: 7 oktober 2026. Bouwt op 01-cohorten, 02-deliverability, `klaviyo/flows/v3-new-flows.md` (Sunset v3 met S1 en S2) en DECISIONS (pop-up blijft de Alia-giveaway). Niets is aangemaakt of gewijzigd; dit is een voorstel. Alle bedragen zijn schattingen met de aannames erbij.

## Waarom

- Bijna alle klachten komen van niet-klikkers: 82 procent van de spamklachten en 75 procent van de uitschrijvingen sinds 1 juli komen van profielen zonder menselijke klik in de 90 dagen ervoor; de helft van de spamklachten van aanmelders jonger dan 60 dagen.
- Juist die groep krijgt sinds september de meeste extra mail: campagnes naar de volledige lijst, tot 4,1 campagnes per ontvanger in de week van 28 september, Smart Sending uit bij 10 van 33 campagnes.
- Bij providers die klachten terugmelden staat Siraat op 0,18 procent, bij Outlook op 0,31 procent. Gmail (56 procent van de mail) is niet zichtbaar zonder Postmaster Tools.
- Tegelijk leveren niet-klikkers nog steeds ongeveer 80 procent van de latere orders (via alle kanalen). Afsnijden in week 1 kost omzet; minder vaak mailen en na 45 tot 60 dagen zonder enig signaal stoppen niet.

## 1. Eén segmentatievraag in de pop-up

**Keuze: doel, niet kookplaat.** Het doel stuurt meteen product, prijsniveau en toon (pan $134 tot $199, set $349 tot $799, cadeau in Q4), en "just looking" is zelf een intentiesignaal. De kookplaatvraag (inductie en kookplaat: 24 pre-sale vragen in 90 dagen) is kleiner en kan als één-klik-vraag in welcome-mail 2.

| | Voorstel |
|---|---|
| Plaats | Stap 2 van de Alia-pop-up, ná het e-mailadres (de aanmelding is dan al binnen, dus geen verlies aan opt-ins). Optioneel, één tik. |
| Vraag (Engels) | "What brings you here?" |
| Antwoorden | "My first titanium pan" · "A full set" · "A gift for someone" · "Just looking" |
| Opslag | Profieleigenschap `shopping_for` = `pan` / `set` / `gift` / `browsing` (via Alia-integratie naar Klaviyo). |
| Gebruik | Welcome v3: W2 tot W4 vertakken op `shopping_for` (pan: maatkeuze en sticking; set: 6 tegen 12, prijs per stuk; gift: levering vóór de feestdagen en 30 dagen retour; browsing: lichte reeks, zie 2). Campagnes: set-aanbiedingen alleen aan `set` plus klanten. |
| Tweede vraag | Kookplaat (Gas / Electric / Induction) als drie knoppen in W2, elke knop zet `cooktop` via een link met UTM of een Klaviyo-voorkeurenpagina. |
| Kanttekening | De giveaway-belofte ("kans op order refund") blijft ongewijzigd. Alia moet een tweede stap met een vraag ondersteunen en het antwoord naar Klaviyo sturen: te bevestigen door Floris. |

**Verwacht effect.** Aanname: 50 tot 70 procent beantwoordt de vraag; gepersonaliseerde W2 tot W4 verhogen de conversie dag 1 tot 90 van wie niet direct koopt met 5 tot 10 procent relatief (van 4,2 naar 4,4 tot 4,6 procent). Basis: circa 17.000 aanmelders per maand die niet binnen 24 uur kopen, $9,78 omzet per zo'n aanmelder in dag 1 tot 90. Dat is $166.000 per maand aan latere omzet (alle kanalen); 5 tot 10 procent op het beantwoorde deel geeft **circa $4.000 tot $11.000 per maand** (alle kanalen, niet allemaal incrementeel). Risico: klein, mits de vraag na het e-mailadres komt.

## 2. Intentiescore in de eerste 7 dagen

Doel: niemand afsnijden, wel bepalen wie de volle verkoopreeks en de campagnestroom krijgt.

| Signaal (dag 0 tot 7, sinds aanmelding) | Punten | Klaviyo-metric |
|---|---|---|
| Menselijke klik in een mail | 2 | Clicked Email `W247h8`, Bot Click = false |
| Product bekeken | 2 | Viewed Product `XNtYMB` |
| Added to Cart | 3 | `QXcV8K` |
| Checkout Started | 4 | `RfMvni` |
| Sitebezoek zonder productview | 1 | Active on Site `UdCdLD` |
| Antwoord `set` of `gift` in de pop-up | 1 | profieleigenschap |
| Order | uit de score, naar Post-purchase | `RSNxYV` |

**Uitvoering.** Op dag 7 in Welcome v3 een conditional split: score 2 of hoger = **hoog**, anders **laag**. Klaviyo kan geen punten optellen, dus in de praktijk een split met "OF"-voorwaarden: klik, productview, ATC of checkout sinds flow-start, of sitebezoek plus antwoord `set`/`gift`. Profiel krijgt `intent_7d = high/low` via een update-profile-actie.

| Pad | Welcome | Campagnes dag 7 tot 60 | Opnieuw beoordelen |
|---|---|---|---|
| Hoog | Volledige reeks met aanbod | Normaal, binnen het plafond (zie 3) | Niet nodig |
| Laag | Twee mails: bewijs (Light Labs, 75 jaar garantie) en bestsellers met HI10; daarna geen Failure to launch-reeks van 10 mails | Maximaal 1 campagne per week, alleen de sterkste (founder note, grote sale) | Dag 30: alsnog een signaal, dan naar hoog. Dag 60 zonder signaal: Sunset (zie 4) |

**Data.** Slechts 8,5 procent van de niet-kopers klikt in week 1; zij kopen daarna in 5,7 procent van de gevallen, de rest in 2,5 procent. Met productviews en sitebezoek erbij verwacht ik 20 tot 30 procent "hoog" (productview per profiel is niet gemeten in deze analyse: eerste meting na livegang).

**Verwacht effect.** Volume: het lage pad krijgt in dag 7 tot 60 circa 6 tot 10 mails in plaats van 20 tot 30 (Failure to launch plus 2 tot 4 campagnes per week). Bij 12.000 tot 14.000 lage profielen per maand is dat **150.000 tot 250.000 mails per maand minder** (circa 8 tot 12 procent van het huidige volume). Omzet: het lage pad levert in dag 7 tot 90 nu $5,71 per profiel (alle kanalen) en is goed voor 82 procent van alle latere omzet van aanmelders. Als e-mail daar 20 tot 30 procent van verdient en 10 tot 20 procent dáárvan wegvalt door minder mail, kost het **$1.500 tot $5.000 per maand**. Daarom krijgt het lage pad nog wel mail, alleen minder. Daartegenover minder uitschrijvingen (in het eerste kwartaal na aanmelding 25 procent nu) en minder klachten bij precies de groep die de helft van de spamklachten maakt.

## 3. Frequentieplafond over alle flows en campagnes

| Regel | Waarde |
|---|---|
| Plafond marketingmail per profiel | Maximaal **4 per 7 dagen** (flows en campagnes samen) voor hoog en klant; **2 per 7 dagen** voor laag en voor profielen zonder klik in 90 dagen |
| Voorrang | Checkout, cart, browse en post-purchase gaan altijd voor; campagnes wijken. Transactionele mail telt niet mee. |
| Smart Sending | Altijd aan op campagnes (venster minstens 16 uur). Uitzetten alleen met reden in LOG.md. |
| Uitvoering in Klaviyo | Segment "Frequentieplafond bereikt": Received Email (`YkRM4Q`) minstens 4 keer in de laatste 7 dagen, of minstens 2 keer voor `intent_7d = low` en profielen zonder klik in 90 dagen. Dit segment staat als uitsluiting op elke campagne. In flows (behalve de abandonment-flows) een filter "Received Email minder dan 4 keer in 7 dagen". |
| Doelgroep campagnes | Standaard "Engaged 90 Days" (bestaand segment `VKxqyA`, 89.759) plus klanten van de laatste 180 dagen. De volledige Email List of "US Subscribers" alleen bij de 4 tot 6 grootste momenten per jaar (BFCM, jubileumsale), en dan met uitsluiting van Unengaged 180 en Sunset. |

**Verwacht effect.** In een normale week (2 tot 2,5 campagnes per ontvanger) raakt het plafond vooral de lage groep: 10 tot 15 procent minder campagnemail. In een piekweek zoals 28 september (4,4 mails per ontvanger) 30 tot 40 procent minder. Omzet: campagnes leveren circa $100.000 per maand; ik schat dat 3 tot 6 procent daarvan komt van mails boven het plafond aan niet-klikkers: **$3.000 tot $6.000 per maand risico**, grotendeels terug te verdienen via betere inboxplaatsing (zie 6).

## 4. Sunset na 45 tot 60 dagen zonder klik

Aanvulling op Sunset v3 (`klaviyo/flows/v3-new-flows.md`, S1 "Still want to hear from us?" en S2 "Last email from me"). De v3-trigger (120 dagen zonder klik, sitebezoek en order) blijft voor bestaande profielen; voor nieuwe aanmelders komt er een snellere ingang.

| | Nieuwe aanmelders (nieuw) | Bestaande profielen (v3) |
|---|---|---|
| Instap | 60 dagen na aanmelding: geen menselijke klik, geen Active on Site, geen order sinds aanmelding, en minstens 8 mails ontvangen | 120 dagen zonder klik, sitebezoek of order, minstens 8 mails in 120 dagen |
| Vroege variant | `intent_7d = low` én geen enkel signaal na 45 dagen: instap al op dag 45 | n.v.t. |
| Mails | S1, na 4 dagen S2 | S1, S2 |
| Uitkomst | Signaal: `sunset_status = kept`. Geen signaal: `sunset_status = suppressed`, wekelijks bulk-suppressen of uitsluiten van alle marketing | idem |
| Opens | Tellen niet als signaal (Apple Mail Privacy) | idem |

**Waarom 60 en niet 30 dagen.** Wie na 45 dagen nog niet klikte en niet kocht, koopt in dag 45 tot 90 nog in 0,64 procent ($1,47 per profiel, alle kanalen); na 60 dagen 0,36 procent ($0,85 per profiel in 30 dagen). Na 60 dagen is de restwaarde klein genoeg om te stoppen; op 30 dagen laat je te veel liggen.

**Omvang.** Circa 20.000 aanmelders per maand, waarvan 70 tot 75 procent op dag 60 geen klik en geen order heeft; na aftrek van sitebezoekers schat ik **10.000 tot 13.000 profielen per maand** in de snelle sunset. Eenmalige inhaalslag: het bestaande niet-betrokken deel (77.000 op Klaviyo's eigen definitie) via v3 in delen van 10.000 per week, zodat er geen piek in klachten ontstaat.

**Verwacht effect.**
- Volume: elk onderdrukt profiel kreeg 10 tot 17 marketingmails per maand. Na drie maanden ingroei **350.000 tot 600.000 mails per maand minder** (15 tot 25 procent van het huidige volume), na de inhaalslag meer.
- Omzet die wegvalt: 10.000 tot 13.000 profielen maal $0,85 (alle kanalen, 30 dagen) is $8.500 tot $11.000, waarvan ik 20 tot 30 procent aan e-mail toeschrijf: **$2.000 tot $3.500 per maand**, dalend omdat de restwaarde per maand verder afneemt. S1 en S2 houden een deel ("kept"; aanname 5 tot 10 procent).
- Klachten: bij uitsluiten van niet-klikkers verwacht ik **35 tot 50 procent minder spamklachten** (82 procent komt nu van niet-klikkers, niet allemaal in de sunset). De ratio bij providers die terugmelden daalt dan van 0,18 naar circa 0,09 tot 0,12 procent; Outlook van 0,22 tot 0,31 naar onder 0,15.
- Klaviyo-kosten: onderdrukte profielen tellen niet als actief profiel. Bij 50.000 tot 80.000 minder actieve profielen scheelt dat waarschijnlijk een prijstrede; te controleren op de factuur.

## 5. Samen: verwachte omzet- en risico-effecten per maand

| Onderdeel | Omzet erbij | Omzet risico | Volume | Klachten en uitschrijving |
|---|---|---|---|---|
| Segmentatievraag | +$4.000 tot +$11.000 (alle kanalen) | klein | gelijk | iets lager (relevantere mail) |
| Intentiescore | | -$1.500 tot -$5.000 | -150.000 tot -250.000 mails | lager in dag 7 tot 60, waar de helft van de spamklachten valt |
| Frequentieplafond plus engaged-doelgroepen | | -$3.000 tot -$6.000 | -10 tot -40 procent campagnemail | uitschrijvingen per week terug naar 1.500 tot 2.000 (nu tot 3.340) |
| Sunset 45 tot 60 dagen | | -$2.000 tot -$3.500 | -350.000 tot -600.000 mails na 3 maanden | spam -35 tot -50 procent |
| Betere inboxplaatsing (gevolg van alles) | **+$5.000 tot +$12.000**: aanname 2 tot 5 procent meer inbox bij Outlook en Yahoo/AOL (31 procent van de mail) en stabiel bij Gmail, op circa $240.000 e-mailomzet per maand | | | |
| **Netto** | **tussen -$5.000 en +$16.000 per maand**; midden van de ranges circa +$5.000. De directe rekensom is dus bescheiden; de echte reden is het vermeden staartrisico hieronder | | **-30 tot -45 procent mail** | |

Het grootste effect staat niet in de tabel: het vermijden van een Gmail- of Microsoft-blokkade. Bij een spamratio boven 0,3 procent gaat ook de checkout-mail ($2,36 per ontvanger) naar spam. Eén maand met 30 procent minder inboxplaatsing kost $50.000 tot $70.000.

**Meten.** Holdout van 10 procent op de intentiescore (laag pad zonder ingreep) en op de snelle sunset (niet onderdrukken), 8 weken. Primaire maat: omzet per aanmelder (alle kanalen) en klachten per 1.000 verzonden mails per provider.

## 6. Monitoring: drempels voor het dagelijkse rapport

Aanvulling op het bestaande Slack-rapport (#claude-mail, BACKLOG 13). Groen, oranje en rood; rood betekent dezelfde dag actie (campagnes pauzeren of doelgroep versmallen).

| # | Maat | Bron | Venster | Oranje | Rood |
|---|---|---|---|---|---|
| 1 | Spamratio Outlook/Hotmail | Marked as Spam ÷ Received, per Inbox Provider | rollend 7 d | > 0,10% | > 0,20% |
| 2 | Spamratio Yahoo/AOL (Verizon Media) | idem | rollend 7 d | > 0,08% | > 0,15% |
| 3 | Spamratio alle terugmeldende providers samen (Outlook, Yahoo, Comcast) | idem | rollend 7 d | > 0,10% | > 0,20% |
| 4 | Gmail-spamratio | Google Postmaster Tools (handmatig of via API zodra gekoppeld) | dagelijks | > 0,10% | > 0,20% |
| 5 | Spamratio per campagne (alle providers) | campagnerapport | per verzending | > 0,05% | > 0,08% |
| 6 | Uitschrijving per campagne | campagnerapport | per verzending | > 0,40% | > 0,60% |
| 7 | Uitschrijving per flow-mail | flowrapport | rollend 7 d | > 0,5% | > 1,0% (PLAYBOOK 6) |
| 8 | Hard bounce | Bounced Email, Bounce Type = Hard | per verzending | > 0,3% | > 0,5% |
| 9 | Soft bounce | idem, Soft | dag | > 2 keer het 4-wekengemiddelde | > 4 keer (throttling) |
| 10 | Mails per unieke ontvanger | Received count ÷ unique | rollend 7 d | > 3,5 | > 4,5 |
| 11 | Verzendvolume | Received count | week | > 1,5 keer gemiddelde 8 weken | > 2 keer |
| 12 | Menselijke klikkers per unieke ontvanger | Clicked (Bot Click = false) uniek ÷ Received uniek | week | < 2,0% | < 1,5% |
| 13 | Bot-klikaandeel | Clicked, Bot Click = true | week | > 30% | > 40% (klikcijfers onbetrouwbaar) |
| 14 | Campagne zonder Smart Sending of met de volledige lijst / US Subscribers zonder engagementfilter | Campaigns API | per verzending | elke keer melden | > 2 per week |
| 15 | Nieuw cohort, eerste 7 dagen | Subscribed to List en vervolg-events | per weekcohort | uitschrijving > 12% of spam > 5 per 1.000 | uitschrijving > 15% of spam > 8 per 1.000 |
| 16 | Aandeel campagnemail naar profielen niet betrokken in 90 dagen | campagne-doelgroep tegen `VKxqyA` | per verzending | > 30% | > 45% |
| 17 | Dropped Email | `RCULWK` | dag | > 50 | > 150 |
| 18 | DMARC-doorgang (zodra eigen rapporten binnenkomen) | DMARC-aggregaatrapporten | week | < 98% | < 95% |
| 19 | Sunset-voortgang | `sunset_status` kept / suppressed | week | kept < 3% (S1 werkt niet) | n.v.t. |

## 7. Volgorde van invoeren

1. Deze week, zonder bouwwerk: Smart Sending altijd aan; geen campagnes meer naar de volledige lijst of "US Subscribers" zonder engagementfilter; Google Postmaster Tools en Microsoft SNDS koppelen; eigen DMARC-rapportadres.
2. Frequentieplafond-segment en uitsluiting op elke campagne.
3. Sunset v3 live (S1, S2, segment 120 dagen), daarna de snelle ingang op 60 dagen en de inhaalslag in delen.
4. Intentiescore als dag-7-split in Welcome v3, met holdout.
5. Segmentatievraag in Alia (hangt af van wat Alia kan) en vertakking in W2 tot W4.
6. Na 4 weken: DMARC naar `p=quarantine` als alle bronnen aligned zijn.
