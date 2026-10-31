# Backup vóór de BFCM-omzetting (31 okt 2026)

- backup/: per flow de definitie (flow-<id>.json), per mail de oude template-html (template-<id>.html) en map.json.
- rollback.py: zet alle 88 templates en 62 onderwerpen/previews terug. Standaard dry-run, `--apply` om uit te voeren, flow-id als argument om te beperken. Draaien vanuit deze map (gebruikt ./kl.py en ./backup).
- Draft-duplicaten in Klaviyo (nooit live zetten): checkout SaE7Eg, cart RvC4T8, browse RCRzrp, browse TP R4sLZD, site R3ggUV, welcome X7mJkA, post-purchase RzqPaH, winback VX9pxs, VIP VCCn9S.
- Na de sale ook content/catalog/products.json opnieuw verversen (prijzen staan op BF-niveau).
- Handmatig na de agent (31 okt): B1-variatie B template Ye4tQy naar b1-bf (oude html in backup/template-Ye4tQy.html, niet in rollback.py: zelf terugzetten). Onderwerpen/previews van A/B-variaties W1 (119850657, 119850658) en B1 (119850691, 119850692) aangepast; oude waarden in backup/ab-variation-subjects.json (ook zelf terugzetten).
