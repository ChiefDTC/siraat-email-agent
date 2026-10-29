# Terugdraaien A/B Q4-wijzigingen (28 okt 2026)

- `voor0/<actie-id>.json`: definitie van elke flow-actie vóór de wijzigingen van 28 okt ($0-filter, TP B2 manual, W1-variatie B, B1-variatie B).
- `voor1/<actie-id>.json`: definitie na het $0-filter, vóór de dedupe-filters en het P2-SAFE-filter.
- Terugzetten van één actie: `PATCH /api/flow-actions/<id>` met `{"data":{"type":"flow-action","id":"<id>","attributes":{"definition": <inhoud van het bestand>}}}`.
- `patch0.py` en `patch1.py` zijn de scripts die de filters zetten (idempotent; draaien vanuit de scratchpad met kl.py).
