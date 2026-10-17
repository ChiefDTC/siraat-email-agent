# Site niet bereikbaar vanuit mails (17 okt 2026)

Aanleiding: Gorgias-ticket 96260668 (UK-klant, campagne "Is your cutting board non-toxic?"). Links werken niet, en ook de directe URL siraatskitchen.com werkt niet bij haar.

## Bevindingen
- Gorgias, laatste 30 dagen: 3 duidelijke meldingen.
  - 95125499 (12 okt): screenshot met ERR_SSL_PROTOCOL_ERROR op de site zelf, "Your site is not secure".
  - 95500612 (13 okt, VS): "website appears to be down for months".
  - 96260668 (17 okt, UK): links en directe URL werken allebei niet.
- Het probleem zit dus op domein- of SSL-niveau, niet in de Klaviyo-links. Ook de directe URL faalt.
- Klaviyo, 10 sep t/m 17 okt: kliks per dag en Viewed Product zijn normaal, en de orders blijven op 150 tot 265 per dag. Er is geen algemene storing; het gaat om een deel van de bezoekers.
- Shopify: het primaire domein is siraatskitchen.com en volgens Shopify staat SSL aan.
- Vanuit deze omgeving kan ik DNS niet zelf controleren, omdat DoH en DNS-tools door de proxy worden geblokkeerd.

## Meest waarschijnlijke oorzaak
Een verkeerd of verouderd DNS-record naast het Shopify-record. Bijvoorbeeld een AAAA-record (IPv6) of een tweede A-record dat naar een oude host wijst. Wie op dat adres uitkomt, krijgt een SSL-fout. Dat verklaart waarom het "bij sommigen" misgaat, ook bij de directe URL. Klanten met IPv6, zoals veel UK- en Comcast-aansluitingen, raakt het het eerst.

Tweede kandidaat: een ISP- of beveiligingsfilter (bijv. UK-ISP-filters) dat het domein blokkeert.

## Check (Floris, 5 min)
1. Shopify Admin > Settings > Domains: staat er bij siraatskitchen.com of www een waarschuwing over SSL of DNS?
2. dnschecker.org: zoek siraatskitchen.com op als A en als AAAA, en www.siraatskitchen.com als CNAME.
   - Juist: A = 23.227.38.65 (alleen dit), www CNAME = shops.myshopify.com, en geen andere AAAA dan die van Shopify.
   - Elk ander IP-adres of een oud AAAA-record verwijderen bij de DNS-provider.
3. Daarna: Shopify Domains > "Verify connection", zodat het certificaat opnieuw wordt uitgegeven.

## Update 12:41 (Floris, dnschecker.org)
- A siraatskitchen.com = 23.227.38.65 wereldwijd, overal resolved.
- AAAA = 2620:127:f00f:5:: wereldwijd. Dat is het officiële Shopify IPv6-adres.
- Conclusie: de DNS van het hoofddomein is schoon. De hypothese van een oud of verkeerd record vervalt.
- Volgende kandidaat: het domein wordt door beveiligingsfilters geblokkeerd (ISP-filter, antivirus, bedrijfsnetwerk, Safe Browsing-achtige lijsten). Nog te checken: www-CNAME, Google Transparency Report, VirusTotal (siraatskitchen.com en ctrk.klclick1.com), en de UK-ISP-filters.
- www.siraatskitchen.com CNAME = shops.myshopify.com wereldwijd (12:48). Volledige DNS in orde. Oorzaak ligt buiten onze DNS: volgende stap reputatie (Safe Browsing, VirusTotal, Sky Shield) + klanten vragen naar provider/4G.

## Oorzaak gevonden (12:50)
- Google Safe Browsing: geen onveilige content.
- VirusTotal siraatskitchen.com: 2/92 malicious (Chong Lua Dao: Malicious, VIPRE: Malware) en 2 suspicious (alphaMountain.ai, Gridinsoft).
- VIPRE is consumenten-antivirus met webfilter dat HTTPS onderschept. Dat geeft precies ERR_SSL_PROTOCOL_ERROR en blokkeert ook de directe URL. alphaMountain.ai levert URL-categorieën aan andere filters (o.a. DNS- en routerfilters), dus die melding kan verder doorwerken.
- Actie: false-positive aanvragen bij alle vier. Nog checken: ctrk.klclick1.com op VirusTotal.
- ctrk.klclick1.com op VirusTotal: 0/92, schoon (12:55). Klaviyo-linkdomein is niet de oorzaak; probleem zit alleen bij siraatskitchen.com. Contacten: docs.virustotal.com/docs/false-positive-contacts.

## Grootste bron gevonden: Spectrum Security Shield (13:05)
- Ticket 91338121 (Owen, Californië): na weken bevestigd: "Spectrum security shield had your site blocked". Shield uit = kon bestellen. Hij heeft zelf bij Spectrum een unblock aangevraagd (13 okt, "tot 5 dagen").
- Eerste melding van dezelfde klant: ticket 78311285, 11 aug 2026 ("Safari can't open the page"). Probleem bestaat dus minstens sinds 11 aug 2026. John (13 okt) schreef "down for months".
- Spectrum is een van de grootste internetproviders in de VS. Dat verklaart "honderden".
- Actie: aanvraag via https://www.spectrum.net/support/forms/verify_url_security (siraatskitchen.com, www, en account.siraatskitchen.com).
- Leerpunt CS: "het ligt aan je browser" was 2 maanden lang het antwoord. Dat moet stoppen.
- 13:01: Spectrum-formulier voor alle 3 URLs: 'Security Shield Is Not Blocking This Site'. Waarschijnlijk opgeheven na Owens aanvraag van 13 okt. Let op: andere sites meldden dat het formulier 'vrij' zei terwijl de blokkade nog deels bestond. Verifiëren via eerstvolgende Spectrum-klant.
- 13:10: case Timothy Hess (#SIRAAT109321, Elkhart IN). Besteld 15 okt op desktop via IP 130.41.14.100 = Palo Alto Networks (Prisma Access, zakelijke VPN, Denver). Thuis op telefoon via wifi ERR_CONNECTION_REFUSED. Bevestigt: filter op thuisnetwerk. Kwam via AppLovin-advertentie: probleem raakt ook betaald verkeer, niet alleen mail.

## Checkers (13:20, Floris)
| Checker | Resultaat | Actie |
|---|---|---|
| Spectrum Security Shield | niet geblokkeerd | geen |
| Cisco Talos/OpenDNS | Neutral, Shopping, niet op blocklist | optioneel reputatieticket |
| OpenText/BrightCloud | Low Risk 64/100, foutief "1 month old" | change request ingediend/te doen |
| Zvelo | Online Shopping, geen phishing | geen |
| Norton Safe Web | Safe | geen |
| Trend Micro | Untested | reclassify request (Shopping) |
| McAfee | trustedsource.org 403 | via sitelookup.mcafee.com |
| VIPRE, alphaMountain, Gridinsoft, Chong Lua Dao | gemarkeerd | false-positive mails verstuurd 17 okt |
