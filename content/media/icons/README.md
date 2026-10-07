# Siraat lijn-iconen

Zelf getekende set, 16 iconen. 24px grid, stroke 1.75px, ronde caps en joins, geen vulling. Twee kleuren: brick #AC3B19 en ink #282828. Overzicht: `preview.png`.

| Bestand | Betekenis |
|---|---|
| free-shipping | truck, gratis verzending |
| returns-30-day | cirkelpijl met retourpijl, 30 dagen retour |
| warranty-75-year | schild met vinkje, 75 jaar garantie |
| pfas-tested | laboratoriumkolf, PFAS getest |
| no-coating | pan van boven met hamerslag-puntjes, geen coating |
| metal-utensil-safe | spatel, metalen keukengerei mag |
| dishwasher-safe | vaatwasser |
| induction-ready | inductiespoel tussen twee platen |
| oven-safe | oven |
| gift | cadeau met strik |
| mystery-gift | doos met vraagteken |
| e-book | open boek |
| water-filter | druppel |
| secure-checkout | slot |
| customers-100k | twee personen, 100,000+ klanten |
| original-since-2024 | rozet met ster, the original since 2024 |

## Bestanden

- `svg/brick/*.svg`, `svg/ink/*.svg`: 24x24 viewBox, kleur hard in `stroke`.
- `png/<kleur>/<naam>-48.png` (48px) en `<naam>-96.png` (96px, de 2x voor weergave op 48px). Transparant.
- In e-mail: `<img src="...-96.png" width="48" height="48">`. Klaviyo-mail ondersteunt geen inline SVG betrouwbaar, dus altijd PNG.

## Opnieuw bouwen

```
python3 -I build_icons.py   # schrijft svg/
node render_icons.js        # schrijft png/ en preview.png (playwright, chromium /opt/pw-browsers/chromium)
```

Nieuw icoon: voeg een regel toe aan `ICONS` in `build_icons.py`, zelfde regels (1.75 stroke, binnen 2.75 tot 21.25 blijven).

## Let op

- Brick op charcoal (#282828, footer) heeft weinig contrast, zie onderste rij van `preview.png`. Voor de footer een witte of titanium (#C9C6C0) variant toevoegen in `COLORS`.
- Geen tekst in de iconen ("30", "75") zodat ze in elke taal werken; het getal staat in het label ernaast.
