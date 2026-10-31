# BFCM 2026 flowvarianten (voorbeelden, niet live)

Bron: Figma "Siraat · Black Friday 2026 Brand Book" (jY3uex0pCP6rHT97zFiA9B), pagina's 01, 02, 05, 07.

## Stijl
- Signal Yellow #FFB800 (vlakken, tags, knoppen; tekst erop altijd Ink #272727). Ink #272727. Night #0E0E0E (exclusieve donkere vlakken). Cream #F8F7F2 basis. Stock red #C8202A alleen voor een echte voorraadbalk.
- Inter Black koppen (strak), Inter Extra Bold caps voor tags en knoppen, Inter Regular body. Serif (Instrument Serif Italic) alleen als tweede regel op donker beeld.
- Eén groot geel element per sectie. Geen gele tekst op wit/cream. Geen rode knoppen.

## Blokken (klaviyo/templates/partials/blocks, via {{BLOCK:naam key="..."}})
bf-topbar (text, bg, color) · bf-hero (img, alt, tag, line1, line2, sub) · bf-cta (label, url, pad, bg, sub) · bf-sectionbar (text) · bf-tiles2 (pad, img1, name1, url1, img2, name2, url2) · bf-deal (pad, eyebrow, headline, detail) · bf-product (side=left|right, img, url, name, kicker, alt, b1, b2; opties pill, btn, pad, bg, panel): productkaart Smooche-stijl, zie signup/FLOW.md.
Voorbeeld: klaviyo/templates/v3/bfcm/_test/t.html. Vaste {{HEADER}} en {{FOOTER}} blijven (merkregel). bf-topbar staat boven {{HEADER}}.

## Beelden (Shopify CDN, https://cdn.shopify.com/s/files/1/0907/0877/1156/files/)
Exclusive dark (hero, 2400x1000): siraat-collection-exclusive-NN-*-desktop.jpg met NN-* = 01-plinths, 02-gallery-vitrines, 03-velvet-trunk, 03-velvet-trunk-steel-lids, 04-pan-tower, 05-gallery-rail, 06-slate-flatlay, 07-stage-reveal, 08-vault, 09-chefs-table, 10-levitating-pan. Ook siraat-bf-pan-case-hero-desktop-hq.jpg. Voeg ?width=1200 toe.
Yellow studio producttegels (webp, voeg ?width=600&format=pjpg toe): siraat-bf-product-<naam>-yellow(-tag).webp met naam = hammered-pan-pro, hammered-pan-pro-mini, hammered-deep-pan-pro, hammered-wok-pan-pro, hammered-crepe-pan-pro, dishwasher-sheets, bundle-pan-pro-duo, bundle-pan-pro-kit, bundle-pan-pro-utensil-set, bundle-pro-duo-pan-flipper, bundle-cookware-set-pro, bundle-full-hammered-pro-edition, bundle-complete-edition.

## Copy (brand book copy bank)
Koppen: The sale of the year. · Priced for Black Friday. · Built to last. Priced for Black Friday. · Worth locking up. · The complete collection. · Last call.
Tags: BLACK FRIDAY · BLACK FRIDAY DEAL · BLACK FRIDAY IS LIVE · LAST CALL. Knoppen: SHOP THE SALE · SHOP THE SETS · SHOP THE DEAL · SHOP BEFORE IT ENDS.
Bewijs: Pure titanium cooking surface. Zero coating. · Works on all stovetops, including induction · Oven safe to 750°F / 400°C · Dishwasher safe · PFAS-free, PTFE-free, lab tested.

## Regels
- "Non-toxic" mag (Floris, 31 okt, wijkt af van het brand book), net als pure titanium enz. Nooit een gedachtestreepje.
- AANBOD (Floris, 31 okt): Black Friday Sale tot 70% korting, voor iedereen, via de collectie. Gebruik "Up to 70% off" (niet "70% off everything"). EXTRA 10% met een code ALLEEN in abandonment-mails (checkout, cart, browse, site: mensen die niet afrekenden). Nergens anders een extra code. De code staat NIET in de repo (publiek): schrijf in de bron de placeholder BFCODE (dus /discount/BFCODE?redirect=... en tekst "code BFCODE"); die wordt pas bij upload naar Klaviyo vervangen.
- Geen "ends today", aftellers of "sitewide" tenzij waar; "94% Sold" alleen bij echte voorraad (niet gebruiken).
- Geen "you won"; bij reveal "Unlocked". Oprichter Benjamin. Retour 30 dagen, garantie 75 jaar, 100,000+ klanten.
- Collectie: https://siraatskitchen.com/collections/black-friday-sale. Topbar-tekst: "BLACK FRIDAY SALE IS LIVE". Abandonment-knoppen: https://siraatskitchen.com/discount/BFCODE?redirect=<oorspronkelijk doel of /collections/black-friday-sale>.

## Bouwen en renderen
python3 -I scripts/build_template.py <bron.html> <assets-map> <klaviyo-urls.txt> (draaien vanuit /tmp). Kopieer klaviyo/templates/v3/subscription/assets/klaviyo-urls.txt naar je assets-map.
Screenshot 375 px: node /tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/shot375.js <preview.html> <out.png>
