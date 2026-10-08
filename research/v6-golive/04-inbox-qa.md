# 04 · Inbox-QA: elke testmail automatisch gecontroleerd

Stand: 8 oktober 2026, kwaliteitsagent. Doel: morgen doen Floris en Lola testcheckouts; elke mail die op lolagroothuis+…@gmail.com binnenkomt wordt binnen een paar minuten gecontroleerd, en per mail staat er een kort OK/FOUT-bericht klaar voor Slack. Vandaag al gedraaid op alle 61 templates (US en UK) en op echte mails uit de inbox. Er is niets naar Slack gestuurd en er is geen template gewijzigd.

## 1. In het kort

- **Gmail-connector werkt.** Het gekoppelde account is lolagroothuis@gmail.com. Er staan oude Siraat-campagnes in (van send@siraatskitchen.com) en sinds 21:31 vanavond ook echte v5-testmails op +order, +vip, +sunset en +sunsetkept.
- **De pijplijn draait:** `scripts/qa_inbox.py mail <bestand>` controleert één mail op 15 punten (zie §3), maakt screenshots op 375, 600 en 1200 px (licht, dark, geforceerd donker) en schrijft `report.md`, `result.json` en `slack.txt`. Een eerste echte P1 (+order) is er al doorheen gegaan.
- **Templates vandaag (61 mails x US en UK = 122 renders):** layout, grootte, UTM, tags, em dash, header/footer en lockup zijn overal in orde. Wat er wel uitkomt:
  1. **Hoog, staat live in Klaviyo:** in alle 65 geëxporteerde `*.klaviyo.html` gaat ABOUT nog naar `/pages/faq`. De bron is door de link-agent al verbeterd (`/pages/about-us`), maar zolang er niet opnieuw geëxporteerd is, krijgt elke testmail van morgen deze fout. De echte P1 van vanavond bevestigt het.
  2. **Hoog, alle mails:** de afmeldlink is in de echte mail brick (#AC3B19) op de donkere footer (#282828), contrast 2,4:1, nauwelijks leesbaar. Gezien in de echte P1. Oorzaak: `{% unsubscribe %}` en `{% web_view %}` maken zelf een link zonder kleur, dus geldt de algemene linkkleur. De templatecheck ziet dit niet, omdat de nep-tag in de test al een grijze kleur meegeeft (zie §6).
  3. **Hoog, alle mails:** het headerlogo (zwarte lockup op transparant) is bijna onzichtbaar in geforceerde donkere modus (Gmail-app, Outlook), contrast 2,8 tot 3,0:1. Bekend uit `research/deliverability/01-inbox-check.md` (advies 1, nog niet uitgevoerd).
  4. **Middel, 5 cartmails:** de knop "Finish my order" gaat naar de productpagina (`event.URL`), niet naar de cart. Dat is k1, k1-acc, k2-new, k2-returning en k3-nocode. Keuze voor Floris staat al in `05-links.md`.
  5. **Laag:** in US-mails staat hier en daar "cm" (cross-sell "Stainless Steel Lid, 28 cm", "the 28 cm lid", "20, 26, 28 or 30 cm"), wat lage contrasten in dark mode, en drie GIF's boven de 300 KB.
- **Slack:** het kanaal is **#claude-mail** (C0C7A159Q6M), bevestigd door Floris. Conceptbericht in §5.
- **Morgen:** een loop in deze sessie, elke 5 minuten (Gmail is alleen via de connector in de sessie bereikbaar). Het commando staat in §7.

## 2. Opzet van de pijplijn

```
Gmail (connector, in de sessie)                         repo (scripts)
1. search_threads  from:send@siraatskitchen.com          
   newer_than:1d  -> ID's met toRecipients lolagroothuis+…
2. qa_inbox.py pending <ID's>  -> alleen nieuwe ID's      exports/qa/inbox/seen.tsv
3. get_message FULL_CONTENT -> opslaan als <id>.json
4. qa_inbox.py mail <id>.json                             scripts/mail_checks.py   (15 controles)
                                                         scripts/qa_mail_shots.js (Chromium: screenshots, layout, dark)
   -> report.md, result.json, slack.txt, shots/*.jpg
5. slack.txt laten zien; posten in #claude-mail pas na akkoord (Floris post zelf)
```

Bestanden:

| Bestand | Wat |
|---|---|
| `scripts/mail_checks.py` | Nieuw. Alle controles per mail, los van de bron: neemt een Gmail-JSON (uitvoer van `mcp__Gmail__get_message`), een `.eml` of een `.html` (met optioneel `<naam>.meta.json`). |
| `scripts/qa_mail_shots.js` | Nieuw. Playwright/Chromium: 375/600/1200 px licht, 375/600 px `prefers-color-scheme: dark`, 375 px geforceerd donker (`WebContentsForceDark`, benadering van Gmail-app en Outlook). Meet horizontaal scrollen, beelden buiten het scherm, afgesneden (overflow) en vervormde beelden, beelden die niet laden, contrast van de afmeldlink en in dark mode tekst onder 3:1. Plus een pixelcontrole op de screenshot: logo nog zichtbaar, lichte blokken op donker. |
| `scripts/qa_inbox.py` | Uitgebreid met subcommando's `mail`, `templates`, `pending` en `slack`. Zonder subcommando doet het script precies wat het al deed (deliverability-rapport). |
| `exports/qa/inbox/templates-report.md` en `templates-data.json` | Resultaat van vandaag op alle templates. |

Commando's (altijd vanuit /tmp, met `-I`):

```
python3 -I /home/user/siraat-email-agent/scripts/qa_inbox.py mail <id>.json [--market=UK] [--out=map]
python3 -I /home/user/siraat-email-agent/scripts/qa_inbox.py templates --markets=US,UK [--only=checkout/c1] [--shots=map]
python3 -I /home/user/siraat-email-agent/scripts/qa_inbox.py pending <id,id,...>
python3 -I /home/user/siraat-email-agent/scripts/qa_inbox.py slack <map>/result.json
```

Markt per alias: een landcode in de alias wint (`+uk-pan`, `+au-set`, `+us-schort`); anders `+pan`, `+set`, `+schort` = US en `+int` = EU. `+order`, `+vip` en `+sunset` hebben geen land: dan `--market=` meegeven, anders staat de marktcheck op N.V.T. **Advies voor morgen:** gebruik aliassen met land, zoals `lolagroothuis+uk-pan@gmail.com`, dan klopt de valutacheck vanzelf.

De flow en mail worden herkend aan het onderwerp (A of B uit `exports/manifest.csv`). Een mail met een v5-onderwerp maar zonder vaste header heet "geen v5-mail" (zie de testmail hieronder).

## 3. De controles

| # | Controle | FOUT als | LET OP als |
|---|---|---|---|
| 1 | Onderwerp | leeg of placeholder | langer dan 70 tekens |
| 2 | Preheader | geen verborgen preheader | gelijk aan het onderwerp |
| 3 | Afzender | niet @siraatskitchen.com | |
| 4 | Grootte | HTML-part (quoted-printable) boven 102 KB (Gmail knipt) | boven 90 KB |
| 5 | Links | bestemming geeft geen 200, of een productlink komt uit op de homepage | link niet te controleren |
| 6 | UTM | geen enkele shoplink heeft utm_source, utm_medium en utm_campaign (ook binnen `/discount/?redirect=`) | een deel mist |
| 7 | Linktekst | ABOUT niet naar about, FAQ niet naar faq, lab results, unsubscribe, preferences, socials, cart/checkout-knop niet naar cart of checkout | pan/set/apron/lid/board/accessories niet naar een passende pagina |
| 8 | Beelden | laadt niet, geen alt, ontbreekt in de Klaviyo-bibliotheek (templates) | beeld boven 300 KB, totaal boven 1,5 MB |
| 9 | Tags | `{{`, `{%`, `[VRAAG`, placeholder, "YOUR … TEXT", lorem, None, `[address]` in tekst, alt, href of src | |
| 10 | Valuta en maat | bedrag in de valuta van een andere markt, "from the US" of inch buiten de US, US-only product buiten de US | cm in een US-mail (behalve "11″ (28 cm)"), "duties paid" in een US-mail |
| 11 | Header, footer, logo | ankerteksten uit `partials/header.html` en `footer.html` ontbreken, logo is niet byte-gelijk aan `brand/logo/lockup/*`, header niet zwart of footer niet wit | |
| 12 | Afmelden | geen afmeld- of voorkeurenlink, placeholdertekst, link geeft 4xx, contrast onder 3:1 | link niet te openen vanuit deze omgeving |
| 13 | Em dash | een gedachtestreepje in onderwerp, preheader, tekst of alt | |
| 14 | Layout | horizontaal scrollen op 375/600/1200 px, beeld buiten het scherm, afgesneden of vervormd | |
| 15 | Dark mode | logo onzichtbaar in donkere modus (contrast onder 3:1 op de screenshot) | tekst onder 3:1, lichte blokken op donker |

**Beperking in deze omgeving:** de netwerkregels van deze cloudomgeving blokkeren `ctrk.klclick1.com` (Klaviyo-kliktracking), `manage.kmail-lists.com` (afmelden, voorkeuren, web view), facebook.com, instagram.com en trustpilot.com. `curl -sSIL --max-redirs 10` geeft daar 000. Het script valt dan terug op Klaviyo's tekstversie van dezelfde mail, waarin elke link met zijn echte bestemming staat; die bestemming wordt wel gevolgd (siraatskitchen.com en de beeld-CDN's zijn bereikbaar). Het rapport zegt per mail hoeveel links via deze terugval zijn gecontroleerd. Wil je dat de trackinglinks zelf gevolgd worden: in de omgevingsinstellingen (Network access, Allowed domains) `ctrk.klclick1.com`, `manage.kmail-lists.com`, `www.trustpilot.com` toevoegen. De afmeldlink zelf even met de hand aanklikken in de eerste testmail.

## 4. Gmail-test en testcase van vandaag

- `search_threads` en `get_message` werken. Zoekvraag die werkt: `from:siraatskitchen.com newer_than:1d`, daarna filteren op `toRecipients` met `lolagroothuis+`. Let op: Shopify-bevestigingen komen van `support@siraatskitchen.com` en hebben geen Klaviyo-header; die horen niet in deze check, dus zoek op `from:send@siraatskitchen.com`.
- Testcase 1 (echte mail, 8 okt 09:15, naar het hoofdadres): "The pan nobody else was making", een campagne (Prime Sale, "now 70% off"). Uitkomst 9 OK, 4 FOUT, 2 LET OP: geen preheader, geen UTM op beide links, geen vaste header en footer, geen voorkeurenlink; "See the pan" gaat naar de homepage. Neveneffect: **de v5-W2 heeft precies hetzelfde onderwerp** als deze campagne van vandaag. Wie beide krijgt, ziet een herhaling. Voor de copy-agent.
- Testcase 2 (echte v5-mail, 8 okt 21:40, +order, P1-first, gedraaid door de coördinator met deze pijplijn): 11 OK, 3 FOUT, 1 LET OP. FOUT: ABOUT naar `/pages/faq` (oude export in Klaviyo), afmeldlink 2,4:1, logo en "View in browser" in dark mode. Alle 16 trackinglinks via de tekstversie gevolgd: UTM overal goed, 289 KB beeld, 26 KB HTML.
- Handmatig gezien in een oudere campagne (26 sep, "What everyone's buying this week", niet door mij gemaakt, alleen ter illustratie van wat de check vangt): de afmeldlink heet letterlijk "YOUR UNSUBSCRIBE TEXT" en is #111 op #2B2929, "Win a PFAS Water Purifyer" (tikfout en verboden woord), em dashes in alt-teksten, drie lege links in de footer. De placeholder- en contrastcheck vangen dit.

## 5. Slack-bericht

**Kanaal: #claude-mail** (C0C7A159Q6M, privé, workspace SiraatsKitchen). Daar post Floris al de dagrapporten. Andere kanalen die in aanmerking kwamen: #email-marketing (C08E5PU34AF) en #homestead (C0BMMQ28W3S); die zijn voor gesprekken met mensen, niet voor automatische meldingen. Per mail één bericht, screenshots als bijlage in de thread (Slack-upload via `slack_get_file_upload_url` en `slack_complete_file_upload`): 375 licht, 375 geforceerd donker, 600 licht. Niets verstuurd.

Concept op basis van testcase 1 (zoals `slack.txt` het geeft):

```
:envelope_with_arrow: *Nieuwe e-mail ontvangen:* geen v5-mail (onderwerp gelijk aan welcome/w2, maar zonder vaste header), lolagroothuis@gmail.com (US), 8 okt 09:15
Onderwerp: "The pan nobody else was making" · <Gmail-link|open in Gmail>
*9 OK · 4 FOUT · 2 LET OP*

:x: *Preheader*: geen preheader (Gmail toont dan de eerste tekst uit de mail)
:x: *UTM*: 2 van 2 shoplinks zonder UTM: "See the pan →" (/) en "Shop what we built, now 70% off →" (/) missen utm_source, utm_medium, utm_campaign
:x: *Header, footer, logo*: geen logo gevonden; header mist COOKWARE, SETS; footer mist TITANIUM COOKWARE, BUNDLES & SETS, ACCESSORIES, LAB RESULTS, Manage preferences
:x: *Afmelden en voorkeuren*: geen voorkeurenlink
:warning: *Links (status 200)*: 3 links; 2 Klaviyo-trackinglinks gevolgd via de tekstversie; afmeldlink niet te openen vanuit deze omgeving
:warning: *Linktekst past bij bestemming*: "See the pan →" gaat naar de homepage
:white_check_mark: Onderwerp, Afzender, Grootte, Beelden, Ongerenderde tags, Valuta en maat, Em dash, Layout 375/600/1200 px, Dark mode
Screenshots (375 licht, 375 donker, 600 licht) in de thread
```

Zo ziet hij eruit voor een v5-mail die goed gaat (gesimuleerde C1 op +uk-pan, gerenderd uit de repo):

```
:envelope_with_arrow: *Nieuwe e-mail ontvangen:* checkout/c1, lolagroothuis+uk-pan (UK), 9 okt 12:42
Onderwerp: "Your cart + 4 gifts are still pending"
*14 OK · 1 FOUT · 0 LET OP*

:x: *Dark mode*: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1); lichte blokken op donker: packshot-1.jpg; dark 375 px: "Light Labs report no. 25895" 2.8:1
:white_check_mark: Onderwerp, Preheader, Afzender, Grootte, Links (status 200), UTM, Linktekst, Beelden, Ongerenderde tags, Valuta en maat, Header, footer, logo, Afmelden en voorkeuren, Em dash, Layout 375/600/1200 px
```

## 6. Resultaten van vandaag: alle 61 templates, US en UK

Gerenderd zoals `qa_render.py` doet (build_template, Django op het eerste testevent per flow), markt via `v5checks.market_ctx`. 122 renders, 610 browsermetingen, 2 min 50 s. Volledig: `exports/qa/inbox/templates-report.md`.

**Overal in orde (122 van 122):** onderwerp en preheader aanwezig; grootte 14 tot 37 KB inclusief geschatte tracking (ruim onder 102 KB); alle shoplinks 200 en met UTM; geen ongerenderde tags of placeholders; geen em dash; header en footer uit de partials, logo byte-gelijk aan de lockup (zwart boven, wit onder); afmeld- en voorkeurentag aanwezig; geen horizontaal scrollen, geen afgesneden of vervormde beelden op 375, 600 en 1200 px; alle beelden laden lokaal en staan in de Klaviyo-bibliotheek.

**Fouten per mail, met ernst**

| Ernst | Wat | Mails | Markt | Waar op te lossen |
|---|---|---|---|---|
| Hoog | ABOUT gaat naar `/pages/faq` in wat nu in Klaviyo staat | alle 61 (65 `*.klaviyo.html`) | alle | Bron is al goed (`/pages/about-us`, link-agent). Opnieuw exporteren vóór de testcheckouts. |
| Hoog | Afmeldlink en "View in browser" brick op #282828, 2,4:1 | alle (gezien in de echte P1) | alle | `partials/footer.html`: de `{% unsubscribe %}`/`{% web_view %}`-link krijgt de algemene linkkleur. Oplossing: `<a href="{% unsubscribe_link %}" style="color:#BDB8B0;">Unsubscribe</a>` (en `{% web_view_link %}`), net als bij Manage preferences. Template-agent. |
| Hoog | Headerlogo onzichtbaar in geforceerde donkere modus (Gmail-app, Outlook), 2,8 tot 3,0:1 | alle 61 | alle | Advies 1 uit `research/deliverability/01-inbox-check.md`: lockup geplat op crème (#F8F7F2) via script uit het officiële bestand. |
| Middel | "Finish my order" gaat naar de productpagina, niet naar de cart | cart/k1, k1-acc, k2-new, k2-returning, k3-nocode | alle | Keuze Floris (`05-links.md`): knoptekst aanpassen ("Back to my pan") of cart-permalink. |
| Laag | "cm" in een US-mail: cross-sell-regel "Stainless Steel Lid, 28 cm" | anniversary/n1, n2, n2-nocode; post-purchase/p3-accessory(-nocode), p3-apron(-nocode), p3-next(-nocode), p3-set(-nocode), p3-pan(-nocode); vip/v1(-nocode); winback/r1-acc, r1-pan, r1-set, r2, r2-nocode, r2-vip, r2-vip-nocode | US | Productnaam in de xsell-generator via `{{SIZE:28}}`. |
| Laag | "Add the 28 cm lid" / "Pan Pro takes the 28 cm lid" in US | post-purchase/p1-first, p1-repeat, p2-safe, p3-pan, p3-pan-nocode | US | `{{SIZE:28}}` |
| Laag | "20, 26, 28 or 30 cm" in US | post-purchase/p3-pan, p3-pan-nocode | US | `{{SIZE:..}}` per maat |
| Laag | Grijze tekst 2,8:1 in `prefers-color-scheme: dark` ("Light Labs report no. 25895", "Preheat on medium…") | checkout/c1, welcome/w1-a, w1-b, winback/r1-acc; browse/b2-notclicked | alle | Dark-modekleur van die regel lichter. |
| Info | GIF boven 300 KB (binnen de PLAYBOOK-grens van 1 MB) | post-purchase/p2, p2-safe (egg-slide-lite 559 KB); welcome/w0 (gif-egg-slide 664 KB, gif-water-test 396 KB) | alle | Geen actie nodig. |
| Info | Productfoto's en gift-beelden met witte achtergrond worden lichte blokken in geforceerd donker | 53 van 61 | alle | Geaccepteerd in `01-inbox-check.md`. |
| Geen fout | "duties paid" en "30cm" in welcome/w4-int bij US | welcome/w4-int | US | w4-int gaat alleen naar internationale profielen. |

Voorbeeld (checkout/c1, 375 px, links licht, rechts geforceerd donker): `research/v6-golive/img/04-c1-licht-vs-geforceerd-donker.jpg`. Het logo linksboven verdwijnt bijna.

**Wat de templatecheck niet kan zien** (en de inboxcheck morgen wel): de echte Klaviyo-uitvoer van `{% unsubscribe %}` (in de test is dat een nep-link met grijze kleur; daarom vond alleen de echte P1 de 2,4:1), het echte afzenderadres, de werkelijke trackinglinks en de echte productdata uit het event (de testevents gebruiken `/products/x`, die tellen als voorbeeld en niet als fout).

## 7. Hoe het morgen draait

**Advies: een loop in deze sessie, elke 5 minuten, tijdens het testvenster.** De Gmail-connector is alleen in een sessie bereikbaar; een geplande Routine krijgt geen connectors mee (PLAYBOOK 9). Per nieuwe mail kost het ongeveer 20 seconden plus het ophalen.

Start (één regel in deze sessie):

```
/loop 5m Inbox-QA testronde Siraat. 1) mcp__Gmail__search_threads query "from:send@siraatskitchen.com newer_than:1d" (pageSize 50, THREAD_VIEW_METADATA_ONLY); neem alle bericht-ID's met een toRecipient lolagroothuis+…. 2) Draai vanuit /tmp: python3 -I /home/user/siraat-email-agent/scripts/qa_inbox.py pending <ID's met komma's>. 3) Voor elk nieuw ID: mcp__Gmail__get_message FULL_CONTENT, sla de volledige JSON op als <scratchpad>/gmail/<id>.json en draai python3 -I /home/user/siraat-email-agent/scripts/qa_inbox.py mail <scratchpad>/gmail/<id>.json --out=<scratchpad>/inbox/<id> (bij +order/+vip zonder land: --market=US of het land van de testcheckout). 4) Toon per mail de inhoud van slack.txt en zet een regel in research/v6-golive/08-monitor-log.csv. Niets naar Slack sturen; Floris post zelf in #claude-mail. Stop met de loop als er 30 minuten niets nieuws binnenkomt.
```

**Handmatig per testronde** kan ook: dezelfde vier stappen één keer, bijvoorbeeld na elke checkout ("draai de inbox-QA"). Werkt net zo, alleen zonder wachten.

Afspraken voor morgen:
- Testaliassen met land: `+us-pan`, `+uk-set`, `+au-schort`, `+eu-int`. Dan klopt de valuta- en maatcheck zonder extra werk.
- Vóór de eerste checkout opnieuw exporteren naar Klaviyo, anders geeft elke mail de ABOUT-fout (al opgelost in de bron).
- De ruwe Gmail-JSON en `mail.html` bevatten persoonlijke afmeldlinks; die horen in de scratchpad, niet in git. Alleen `report.md` en `slack.txt` gaan mee.
- De afmeldlink in de eerste testmail één keer met de hand aanklikken (domein is vanuit de sessie geblokkeerd).
