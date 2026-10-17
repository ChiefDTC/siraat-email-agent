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
