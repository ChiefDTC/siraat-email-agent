# 19 · Reviewmail: kortere hero (12 okt 2026)

Vraag Floris: in de reviewmail van flow XzHrez ("Review request · Delivered +14d (Siraat DS)", live) is de hero te hoog; op mobiel moet je te ver scrollen voor je bij de sterren komt.

Live niets gewijzigd. Nieuw los testtemplate in Klaviyo: **WK8WLv** ("TEST · Review hero kort [T1]").

## Wat er live staat

Flow XzHrez, actie 119577637 (ab-test). Drie berichten, alle drie met exact dezelfde HTML (md5 408b5635...), bron `klaviyo/templates/review-request.html`:

| Bericht | Actie | Template |
|---|---|---|
| Review request · Win your purchase back (main) | 119577631 | UxfsuQ |
| A · Subject: Win your purchase amount back | 119577632 | SVpzGN |
| B · Subject: How was your experience? | 119577635 | WTnCid |

De live mail is nog van vóór de vaste opbouw (6 okt): geen vaste header en footer, hero 1200x1200 PNG van 1,3 MB met logo, eyebrow, kop en subregel in het beeld, daarna intro, drie stappen en pas dan de sterren.

## Wat er veranderd is (T1)

- **Hero**: nieuw beeld 1200x1020 (was 1200x1200), JPG 127 KB (was PNG 1,3 MB). Uitsnede y 50 tot 1070 uit dezelfde flitsfoto (`klaviyo/figma/ai/review-hero-dark-1200.jpg`): beide gezichten, de lepel en de pan met handvat en saus blijven in beeld. Retina 2x op 600 px. Generator: `scripts/make_review_hero.py`, beeld in `klaviyo/templates/v3/review/assets/review-hero-short.jpg`, in Klaviyo als image 382450658.
- **Tekst in het beeld**: alleen eyebrow "THANK YOU FOR YOUR ORDER" en kop "Win your purchase amount back" (TT Ramillas). De kop staat groter in beeld en de eyebrow is beter leesbaar op 375 px.
- **Subregel** "Tell us honestly how your titanium pan is treating you. Every month one reviewer gets their full order refunded." staat nu als live tekst onder "Two minutes. One honest review." (was 9 px tekst in het beeld).
- **Sterren direct onder de intro** (PLAYBOOK 10: knop direct onder de hero). De drie stappen staan nu onder de sterren; stap 1 zegt daarom "Tap the stars above ...". "Good or bad, we read every word ..." sluit af. Sterrenrijen 16 px padding (was 18).
- **Vaste header en footer** uit `partials/` (CLAUDE.md). Het logo staat daardoor in de header (lockup), niet meer in het beeld. De oude legal-regels zijn vervangen door de footer.
- **Gmail**: bgcolor plus inline background-color op elke gekleurde cel, light-only, preheader-fix via `build_template.py`. UTM's op de your-experience-links (`utm_campaign=v4-review`, `utm_content=r1-stars3/2/1`), header en footer krijgen ze automatisch. Trustpilot-links ongewijzigd. Sterren-routing ongewijzigd (5 en 4 naar Trustpilot, 3 tot 1 naar your-experience met rating en ordernummer).

Bron: `klaviyo/templates/v3/review/r1-short.html`, gebouwd met `scripts/build_template.py` naar `r1-short.klaviyo.html` en `r1-short-preview.html`.

## Metingen op 375 px (Chromium, scherm 667 px hoog)

| | Voor (live) | Na (T1) |
|---|---|---|
| Hero (beeld) hoog, Apple Mail | 375 px | 319 px |
| Bovenkant hero | 8 | 79 (header 71 px erboven) |
| "Two minutes. One honest review." | y 411 | y 422 |
| Eerste sterrenrij (5 sterren), Apple Mail | y 903 tot 970, onder de vouw | **y 559 tot 622, boven de vouw** |
| Eerste sterrenrij, Gmail iOS strikt (geschaald 0,625) | y 671 tot 713, net onder de vouw | **y 465 tot 505**; ook 4 sterren (tot 544) boven de vouw |
| Totale lengte, Apple Mail | 1.461 px | 1.968 px (door de vaste footer) |

De eerste knop staat op Apple Mail 344 px hoger en op Gmail iOS 206 px hoger, in beide gevallen ruim boven de vouw.

Screenshots (375 px): `img/19-review-voor-na-375.jpg` (Apple Mail, vouwlijn), `img/19-review-voor-na-gmailios-375.jpg` (Gmail iOS strikt), los per modus `img/19-review-{voor,na}-{apple,gmailios,gmailtrim}.jpg`.

## Controles

- `mail_checks.preview_problems` en `bg_problems` op T1: 0 en 0. Op de live HTML: 1 preview-fout (maar 10 opvulposities, de inbox-preview toont daarna de alt-tekst van de hero) en 5 bg-fouten (cellen met alleen CSS-achtergrond).
- `qa_mail_shots.js` (apple, gmailios, gmailtrim): geen horizontaal scrollen, geen afgesneden beelden, geen lege cellen, geen laag contrast. In gmailtrim melden fb.png en ig.png "broken": dat doet de footer van elke mail in deze simulatie (ook P2), geen fout van T1.
- Opvallend: in de apple-modus wordt de **live** mail donker (crème kolom donker, "Two minutes"-kop bijna onleesbaar). T1 blijft licht. Nog een reden om te vervangen.
- Klaviyo-render van WK8WLv met ordernummer 12345: geen ongerenderde tags, links correct.

## Bij akkoord

De drie live templates UxfsuQ, SVpzGN en WTnCid krijgen de HTML van `r1-short.klaviyo.html` (alle drie dezelfde, het A/B-verschil zit alleen in het onderwerp). Daarna PLAYBOOK 7 punt 4: links in de live HTML controleren. Niet gedaan in deze sessie.

Open: image 382449764 (eerste uitsnede 1200x1000) staat ongebruikt in de Klaviyo-bibliotheek.
