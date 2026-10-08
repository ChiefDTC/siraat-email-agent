# Beeld-audit v5 (8 okt 2026)

Aanleiding: feedback Floris (`00-feedback-floris.md`): in AI-beelden staat het handvat scheef en zit het hammered pattern aan de buitenkant. Feit (vergeleken met `content/products/titanium-hammered-pan-pro/img/packshot-1..3.jpg`): de hamerslag (kleine hexagon-achtige deukjes) zit ALLEEN op het kookoppervlak binnenin. Binnenwanden en de hele buitenkant zijn glad geborsteld RVS. Handvat recht, gegoten, plat en taps met ophangoog, twee klinknagels aan de binnenwand, logo-reliëf op het handvat. Deksels: massief glad RVS met gestapelde knop, geen glas.

Criteria per beeld: hammered buitenkant, handvat scheef/vervormd/dubbel, verkeerde pan-vorm, coating/zwart oppervlak, verminkte tekst/logo, handen/vingers, product dat niet bestaat.

Bekeken: alle hero's die een mail echt laadt (48 unieke bestanden in `klaviyo/templates/v3/*/assets`, nocode-varianten delen hun basisbeeld met de hoofdvariant), alle beelden in `klaviyo/templates/partials/shared` en alle 16 beelden in `content/media/ai-flash`.

## Uitkomst in het kort

- **16 van 16 AI-flashbeelden fout**: allemaal hamerslag op de buitenwand en/of onderkant. Ze voeden 21 hero's in 16 mails plus 5 nocode-varianten.
- **Alle echte foto's ok** (shoot, Shopify-productfoto's, UGC). Eén kanttekening bij c3-acc (zie onder).
- **partials/shared: ok.** Packshots en productkaarten kloppen. De gift-beelden (e-book, filter, mystery, verzending) tonen geen pan.

## AI-beelden (content/media/ai-flash) en de hero's die ze voeden

| Bronbeeld | Oordeel | Wat is fout | Hero-bestand(en) | Mails |
|---|---|---|---|---|
| pan-trophy-1x1-01.jpg | fout | onderkant/buitenkant van de opgeheven pan volledig gehamerd | post-purchase/assets/p1-first-hero.jpg | p1-first |
| friends-greeting-1x1-01.jpg | fout | steelpan rechtsonder gehamerd aan de buitenkant | post-purchase/assets/p1-repeat-hero.jpg | p1-repeat |
| egg-plate-1x1-01.jpg | fout | buitenwand van de gekantelde pan gehamerd | post-purchase/assets/p2-hero.jpg | p2 |
| lid-steam-1x1-01.jpg | fout | buitenwand pan gehamerd (deksel was al glad) | post-purchase/assets/p3-pan-hero.jpg, p3-pan-nocode-hero.jpg | p3-pan, p3-pan-nocode |
| pan-reflection-1x1-01.jpg | fout | hij kijkt in de gehamerde ONDERKANT van de pan: concept zelf toont de foute buitenkant | post-purchase/assets/p3-accessory-hero.jpg, p3-accessory-nocode-hero.jpg | p3-accessory, p3-accessory-nocode |
| crepe-flip-1x1-01.jpg | fout | onderkant gehamerd; gewone koekenpan i.p.v. platte crêpepan | post-purchase/assets/p3-set-hero.jpg, p3-set-nocode-hero.jpg | p3-set, p3-set-nocode |
| full-stove-1x1-01.jpg | fout | kookpot, steelpan en alle pannen gehamerd aan de buitenkant | winback/assets/r1-set-hero.jpg | r1-set |
| egg-slide-4x3-01.jpg | fout | buitenwand en onderrand gehamerd | browse/assets/b2-clicked-hero.jpg, b2-clicked-nocode-hero.jpg | b2-clicked, b2-clicked-nocode |
| sauce-taste-4x3-01.jpg | fout | buitenwand pan gehamerd | browse/assets/b2-notclicked-hero.jpg | b2-notclicked |
| pan-microphone-4x3-01.jpg | fout | steelpannetjes volledig gehamerd aan de buitenkant | cart/assets/k2-new-hero.jpg | k2-new |
| olive-oil-4x3-01.jpg | fout | beide pannen gehamerd aan de buitenkant | checkout/assets/c2-hero-pfas.jpg | c2 |
| three-pans-4x3-01.jpg | fout | drie pannen gehamerd aan de buitenkant | checkout/assets/c3p-hero.jpg | c3-p |
| steak-sear-4x3-01.jpg | fout | buitenwand gehamerd | cart/assets/k3-hero.jpg, k3-nocode-hero.jpg | k3, k3-nocode |
| egg-crack-1x1-01.jpg | fout | buitenwand gehamerd | welcome/assets/w0-hero.jpg | w0 |
| two-sizes-1x1-01.jpg | fout | beide pannen tonen een gehamerde onderkant | welcome/assets/w4-int-hero.jpg | w4-int |
| pasta-lift-1x1-01.jpg | fout | buitenwand en onderkant gehamerd | welcome/assets/w4-us-hero.jpg | w4-us |

Handvatten in de oude AI-beelden zijn grotendeels recht; het hoofdprobleem is de buitenkant. Handen/vingers en tekst: geen fouten gezien (geen tekst of logo in beeld).

## Hero's uit echte foto's (ok)

| Hero | Mails | Oordeel |
|---|---|---|
| anniversary n1-hero, n2-hero, n2-nocode-hero | n1, n2, n2-nocode | ok (echte foto, UGC) |
| browse b1-hero-pfas, b1acc-hero | b1, b1-acc | ok |
| cart k1-hero-pfas, k1acc-hero, k2-returning-hero | k1, k1-acc, k2-returning | ok |
| checkout c1-hero, c1-hero-set/pot/pizza/apron, c2acc-hero, c3s-hero, c4us(-nocode), c4int(-nocode) | c1, c2-acc, c3-s, c4-us, c4-int (+nocode) | ok |
| checkout c3acc-hero | c3-acc | ok met kanttekening: Shopify-lifestylebeeld (oogt zelf als render), hamerslag loopt binnenin tot in de wanden; buitenkant niet zichtbaar. Geen vervanging nodig, wel niet als productbewijs gebruiken. |
| post-purchase p2-safe-hero, p3-apron(-nocode), p3-next(-nocode) | p2-safe, p3-apron, p3-next (+nocode) | ok |
| site a1-hero, a2-hero | a1, a2 | ok |
| sunset s1-hero, ugc u1-hero, vip v1(-nocode) | s1, u1, v1 | ok |
| welcome w1-hero-pfas, w3-hero, w5-hero | w1-a, w1-b, w3, w5 | ok |
| winback r1-pan, r1-acc, r2(-nocode), r2-vip(-nocode) | r1-pan, r1-acc, r2, r2-vip (+nocode) | ok |

## partials/shared (ok)

card-panpro-*, card-set6, card-set12-save587, card-roast-new, pc-* (alle productkaarten), panpro-desk/mob, set6-desk/mob, roast-desk/mob, ugc-prod-*: echte packshots, kloppen. gift-ebook, gift-filter, gift-mystery, gift-shipping: geen kookgerei. Iconen, pills en stickers: niet relevant voor deze criteria.

## Vervanging

Zie `05-beeld-vervangingen.csv`. Alle 16 AI-beelden zijn opnieuw gemaakt (Higgsfield `gpt_image_2_5`, quality high, 2k) als bewerking van het oude beeld met de echte packshot als referentie (Pan Pro `Titanium_hammered_pan_pro_standard`, 12-delige set `12pcsset` voor pot/steelpan/deksel, `Crepepan01` voor de crêpepan). Compositie, personen en flitsstijl bleven gelijk; alleen het kookgerei is gecorrigeerd. Bestanden naast het origineel: `content/media/ai-flash/<naam>-v5.jpg` (1200 px breed, zelfde ratio) en `<naam>-v5-2k.jpg` (volle resolutie voor nieuwe uitsneden). Hero's met kop en aanbodbalk moeten nog door de bouwronde opnieuw worden opgebouwd; templates zijn niet aangeraakt.

Pogingen: 14 beelden in één keer goed. egg-slide (poging 1: lang rond buisvormig handvat) en pan-microphone (poging 1: vreemde bevestiging handvat) goedgekeurd in poging 2.

Controle: de opdracht vroeg een aparte controleur via de Agent-tool. Die tool was in deze subagent-omgeving niet beschikbaar. De controle is daarom als aparte stap gedaan op de eindbestanden, per beeld naast de packshots, met uitvergrote uitsneden van pan, handvat en handen. Advies: laat vóór implementatie nog een onafhankelijke controleur over `*-v5.jpg` gaan.

Restpunten (geen afkeur): pannen in full-stove, three-pans en lid-steam hebben hamerslag tot hoog in de binnenwand (echt product: vooral bodem); egg-plate toont het handvat niet (hand op de rand); pan-microphone toont steelpannen uit de 12-delige set (US-only), let op bij internationale ontvangers van k2-new.
