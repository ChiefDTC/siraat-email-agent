# Welcome v6b · Sealed envelope, direct response (concept, 17 nov 2026)

Status: **concept**. Niet in Klaviyo als template of flow; live welcome T4a5Mk niet aangeraakt. Welcome-tests starten na Cyber Monday (2 dec).

Waarom: feedback Floris op v6 (`welcome-v6-envelope.md`): "veel meer direct response, ook met upsells. Te esthetisch." v6b verkoopt eerst; de envelop is alleen nog een lichte draad (zegel op de codekaart, één zandlijnbeeld in E2).

- HTML: `klaviyo/templates/v3/welcome/v6b-envelope-dr/` (`e1..e5.html` Klaviyo, `-preview.html`). Bouwen `python3 -I _tools/build.py`, renders `node _tools/shot.js`.
- Renders 600 en 390 px (DSF 2): `klaviyo/templates/v3/welcome/v6b-envelope-dr/renders/`.
- Beelden: 9 productfoto's uit Shopify (featured image, 600x600 JPG) in de Klaviyo-bibliotheek als `v6b-*.jpg`; envelopbeelden uit v6. URL's in `assets/klaviyo-urls.txt`.
- Figma: oaxnBkz3MAbePRnorCrQwz, All emails, "Row 1f · v6b · Welcome · Direct response (concept, 17 nov)" (node 333:106), direct onder Row 1e (v6).

## Aanbod en code (Shopify, 17 nov)

- **HI10** (DiscountCodeNode 1737555870036): ACTIVE, 10% op alle producten, 1x per klant, geen einddatum, geen minimum. `combinesWith`: order, product en verzending allemaal **false**.
- Links: `/discount/HI10?redirect=<URL-encoded pad + UTM>` (patroon F13/ROAST15). Getest op E1 kaart Pan Pro Standard: 302 naar de PDP met UTM, `set-cookie: discount_code=HI10`, PDP 200.
- Gifts: `GIFTS = "5 free gifts with every order"` als één constante in build.py. Is het na BF "during Black Friday" of stopt het, dan alleen die regel aanpassen.

## Prijzen (Shopify variants.price, US, 17 nov)

| Product | Prijs | Met HI10 |
| --- | --- | --- |
| Pan Pro Mini 8″ | $129 | $116.10 |
| Pan Pro Small 10″ | $137 | $123.30 |
| Pan Pro Standard 11″ | $144 | $129.60 |
| Pan Pro Large 12″ | $149 | $134.10 |
| Stainless Steel Lid | $59 | $53.10 |
| 6-Piece Set (Mini, Small, Large + 3 lids) | $299 | $269.10 |
| 12-Piece Set (US only) | $649 | $584.10 |
| 2 Pans + 2 Lids | $199 | $179.10 |
| Roasting Pan | $199 | $179.10 |

Let op: Shopify zegt Pan Pro Standard **$144** (DECISIONS 8 nov zei $149) en 2 Pans + 2 Lids **$199** (DECISIONS 8 nov zei $249). Mails gebruiken de Shopify-prijs.

Geen doorgestreepte compare-at. Shopify heeft wel compareAtPrice ($480 bij $144, $997 bij $299, $2,047 bij $649), maar PLAYBOOK 12 staat alleen bevestigde ankers toe en die wijken hier af van DECISIONS ($439, $1,186). Besparing wordt alleen getoond als echte som van losse prijzen.

## Upsell-mechanieken

1. **Bundelblok "Most people pick the 6-piece set"**: Mini $129 + Small $137 + Large $149 + 3 lids $177 = $592 los, set $299, **save $293**; met HI10 $269.10, ongeveer $90 per pan, lid included (E1, E3).
2. **Add the lid**: rij met $59 / $53.10 (E1, E2).
3. **Complete the set**: rij naar de 6-piece set met de besparing (E4).
4. **Maatkiezer** Mini/Small/Standard/Large met prijs en HI10-prijs, Standard gemarkeerd "most picked" (E2). Teksten per maat uit W4.
5. **Value stack**: Pan Pro Standard $144 + 5 free gifts ($555 value) + 75-year warranty + 30-day returns, "Your price $129.60 with HI10" (E2). Geen opgeteld totaal.
6. **Productkaarten** 2 per rij, elk met prijs, HI10-prijs en eigen knop met code (E1, E3, E4); recap met drie producten en knoppen (E5).

## Reeks

Timing en filters als v4 (T4a5Mk). Elke mail heeft boven de vouw: harde aanbodregel, codekaart HI10, grote knop, sterren plus "100,000+ happy customers".

| # | Timing | Rol | Onderwerp A / B | Preview |
| --- | --- | --- | --- | --- |
| E1 | 5 min | Aanbod + 4 bestsellers (Standard, 6-pc, 2 Pans + 2 Lids, Roasting) + bundel + lid + 2 reviews (Tammy, Sunny C.) + cartlink. Test tegen W1 ($2.96 per ontvanger). | Your 10% is inside (plus 5 free gifts) / HI10: 10% off everything, sets included | HI10 takes 10% off everything, sets included. Plus 5 free gifts with every order. |
| E2 | +1 d 10:00 | Verhaal kort (origineel, 20 dec 2024, sirat = path, geen coating, 75 jaar) en daarna maatkiezer, value stack, lid, 2 reviews (Carole, Graham C.). | Which size is yours? / The pan nobody else was making | First orders shipped December 20, 2024. Pick your size, 10% off with HI10. |
| E3 | +2 d 09:00 | Bewijs: 31 / 0 / 75, rapport 25895, tabel Siraat tegen "a PFAS-coated pan" (geen merk, geen gezondheidsclaim), 2 reviews (Michael G., Thomas D.), kaarten Standard en Large, bundel. | Report no. 25895 / Has your cookware been tested? | 31 PFAS compounds tested, every one below detection. Your 10% is still here. |
| E4 | +3 d 09:00 | "Still sealed": code nog ongebruikt (kopers zijn uit de flow). Vier kaarten (Standard, 6-pc, 12-pc US, Large), drie bezwaren (Will food stick? / Induction? / What if I don't like it?), complete the set, 2 reviews (Fatima, Brandon W.). | Your 10% is still unused / "I ended up buying the whole collection" | Your 10% is unused. Where most people start, with your price, plus 5 free gifts. |
| E5 | +4 d 09:00 | Korte brief Benjamin (geen druk, twee beloftes, reply), dan een hard recap-blok: code, gifts, garantie, retour, drie producten met prijs en knop. Vaste header en footer. | Last note about your 10% / Two promises, and your 10% | No end date, no pressure. Two promises, and your 10% in one place. |

## Eerlijkheid

Geen VIP of handpicked, geen variabel bedrag, geen deadline of countdown (HI10 verloopt niet), geen nep-compare-at. Reviews letterlijk uit `content/reviews/reviews.csv` (5 sterren, alleen ingekort met "..."). Claims uit de skill: pure titanium cooking surface + no coatings, rapport 25895 (31 PFAS, ISO/IEC 17025), 75-year warranty, 30-day returns, 100,000+, eerste orders 20 dec 2024, induction/gas/electric/ceramic, dishwasher en metal utensil safe, oven safe zonder temperatuur.

## QA (17 nov)

| Mail | 600 px | 390 px | Overloop | Kapotte beelden | Em dash |
| --- | --- | --- | --- | --- | --- |
| E1 | 3,240 | 3,397 | nee | 0 | 0 |
| E2 | 2,957 | 3,101 | nee | 0 | 0 |
| E3 | 2,888 | 3,154 | nee | 0 | 0 |
| E4 | 3,071 | 3,112 | nee | 0 | 0 |
| E5 | 1,559 | 1,698 | nee | 0 | 0 |

Alleen US (USD, 12-pc US only). Voor INT: prijzen via de PRICE-macro's en `{{FRICTION}}`.

## Open vragen voor Floris

1. **HI10 combineert met niets** (ook niet met productkortingen). Blijven de 5 gratis gifts (automatische korting?) staan als iemand HI10 gebruikt? Zo niet, dan klopt "10% + 5 gifts" niet en moet de combinatie in Shopify aan of moet de copy anders.
2. Blijven de 5 gifts na 30 nov, of worden ze "during Black Friday"?
3. Prijzen na BF: geldt $144 of $149 voor de Standard, en $199 of $249 voor 2 Pans + 2 Lids?
4. Mag de echte Shopify compare-at doorgestreept worden ($480, $997, $2,047)? Die wijkt af van de ankers in DECISIONS.
5. Is er een Trustpilot-score die we als getal mogen noemen?
