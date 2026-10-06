# Routines (automatische taken)

## Dagelijks e-mailrapport in Slack

- Kanaal: #claude-mail (C0C7A159Q6M)
- Tijd: elke dag 08:52 Europe/Amsterdam
- Connectors nodig: Klaviyo, Slack
- Status: aangemaakt op 6 oktober 2026 als trig_016oK1qoS7fm5vy3oK7aMe2S, maar zonder connectors (sessies kunnen die niet doorgeven). Opnieuw aanmaken in de claude.ai Routines-UI met onderstaande prompt en beide connectors aangevinkt, daarna de oude routine verwijderen.

### Prompt

```
Je bent de e-mailmarketing-agent van Siraat's Kitchen (Klaviyo-account TdtTzz). Maak het dagelijkse performance-rapport en post het in Slack-kanaal #claude-mail (channel_id C0C7A159Q6M). Schrijf in het Nederlands, gebruik nooit een gedachtestreepje (em dash).

Haal op via de Klaviyo-tools (conversion metric = Placed Order, id RSNxYV):
1. get_flow_report voor "yesterday" en voor "last_7_days", gegroepeerd op flow_id en flow_name, statistieken: recipients, open_rate, click_rate, conversion_rate, unsubscribe_rate, plus value_statistics conversion_value en revenue_per_recipient. Het resultaat is groot; sla het op en verwerk het met jq of python. Toon de 8 flows met de meeste ontvangers.
2. get_campaign_report voor "last_7_days" (send_channel email), gegroepeerd op campaign_id en campaign_message_name, zelfde statistieken. Toon alle campagnes die in die periode verstuurd zijn.
3. De review-flow "Review request · Delivered +14d (Siraat DS)" (flow id XzHrez): recipients, click_rate en unsubscribe_rate per variatie (group_by variation_name) sinds livegang op 6 oktober 2026. Benoem of er al een verschil zichtbaar is tussen variant A (onderwerp "Win your purchase amount back") en variant B (onderwerp "How was your experience?"), en waarschuw dat onder 1.000 ontvangers per variant geen conclusie mogelijk is.
4. De oude review-flow "Trustpilot 4 emojis FLOW - 7JAN" (Vixr6X): recipients gisteren. Als de datum 12 oktober 2026 of later is en deze flow nog verstuurt, meld dan expliciet dat de e-mailstap in die flow op Draft gezet moet worden.

Post daarna één Slack-bericht (slack_send_message) met deze opbouw:
- Kop: "E-mail update <datum>"
- Blok "Gisteren": totaal ontvangers flows, gemiddelde open/klik, omzet uit flows, en de opvallendste afwijking ten opzichte van het 7-daags gemiddelde (alleen noemen als de afwijking groter is dan 20 procent).
- Tabel "Flows, laatste 7 dagen": flow, ontvangers, open %, klik %, omzet, omzet per ontvanger.
- Tabel "Campagnes, laatste 7 dagen": campagne, ontvangers, open %, klik %, omzet. Als er geen campagnes zijn, zeg dat.
- Blok "Review flow A/B": de cijfers uit stap 3.
- Blok "Signalen": maximaal drie concrete observaties die aandacht verdienen (bijvoorbeeld uitschrijfratio boven 0,5 procent, klikratio die daalt, een flow zonder ontvangers). Geen algemene adviezen, alleen wat in de data staat.
- Afsluiten met één voorgestelde actie voor vandaag, in één zin.

Regels: alleen cijfers uit de tool-resultaten, nooit schatten. Percentages met één decimaal, bedragen in USD zonder decimalen. Als een tool faalt, vermeld dat in het bericht en post de rest. Stuur niets naar andere kanalen.
```

## Eenmalige herinnering

- 12 oktober 2026, 22:37 UTC: oude reviewflow Vixr6X uitzetten en eerste A/B-cijfers bekijken (trig_01EtdedR1TsAYdgmTwrAu85g, gebonden aan sessie van 6 oktober).
