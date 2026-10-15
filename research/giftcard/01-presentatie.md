# Gift cards in mails: waar en hoe (15 okt 2026)

Vraag van Floris: hoe laten we gift cards het slimst zien in mails en waar, en past zijn nieuwe gouden kaart (`floris-giftcard-goud.webp`) bij het merk? Alles hieronder is alleen gelezen in Klaviyo (GET plus rapport-queries), niets gewijzigd in Klaviyo of Shopify. Codes staan hier als XXXXXXXX.

## Kort

1. Floris' kaart is een sterk cadeau-object (strik, metaal, transparante achtergrond), maar **het logo erop is door AI nagebouwd en klopt niet**. Het monogram wijkt zichtbaar af van het officiële lockup. Zo mag het niet in een mail (PLAYBOOK §2 en §3, CLAUDE.md).
2. **Goud is geen merkkleur.** Ons materiaal en palet is titanium (#C9C6C0), espresso en brick. Goud kan hooguit als feestversie in december.
3. **Toon een gift card alleen waar het echt om een gift card gaat** (cadeau-campagnes in december, de koper-flow, P3, browse op de gift-card-pagina). De 10%-welkomstcode als "welcome gift card" verpakken heeft in de W1-test niets opgeleverd: evenveel kliks, minder orders.
4. Advies: **variant B (Floris' kaart in titanium met het echte lockup) als sfeerbeeld in campagnes** en **variant C (vlakke titanium kaart, bedrag in het beeld) als functionele kaart**. Naam, afzender en uitleg altijd als live tekst onder het beeld, nooit over een beeld heen.

## 1. Inventaris: waar tonen we nu een gift card

| Plek | Pad | Hoe het eruitziet | Werkt het? |
|---|---|---|---|
| W1 variant B "welcome gift card" (test T04) | `klaviyo/templates/v3/welcome/w1-b.html`, beeld `klaviyo/templates/v3/welcome/assets/gift-card.jpg` (gemaakt met `scripts/make_giftcard.py`) | Espresso kaart, officieel wit logo, "Welcome gift" in TT Ramillas, "10% on top of the sale", code in een gestippeld kader. 512 px breed, klikbaar. | Live van 9 tot 15 okt, toen vervangen door W1 v3. Cijfers hieronder: geen winst. |
| Flow EB · E-Gift Card (UYALJ8, live) | Klaviyo, 1 transactionele mail | Oude Homestead-stijl | 7 ontvangers in 365 dagen, 0 kliks. Gift cards worden nauwelijks gekocht. |
| Nieuwe gift-card-flow en decembercampagnes G1, G2, GC1 tot GC3 | `klaviyo/flows/09-gift-card.md`, `klaviyo/emails/09-gift-card/*.html` | Shopify-productfoto (kaart op kersttafel, met logo en kersttekst in het beeld), oude header-beelden, nog niet in v3/v5-stijl | Nog niet gebouwd in de nieuwe stijl, nog niet verstuurd. Hier hoort de nieuwe kaart. |
| Productblokken browse, cart, checkout | `klaviyo/templates/partials/blocks/about.html`, `label.html`, `noun.html`, `pick.html`; `v3/browse/b1*.html`, `b2*.html` | Alleen tekst ("GIFT CARD", "Delivered by email", "Can it be combined with a code?"), geen beeld | Werkt; mist een kaartbeeld als iemand de gift card bekeek. |
| P3 schort | `klaviyo/templates/v3/post-purchase/p3-apron*.html` | P.S. "A gift card works too, if they'd rather pick." | Alleen tekst. |
| Sunset S3 | `klaviyo/templates/v3/sunset/s3-kept.html` | Segmentregel op /products/e-gift-card | Geen beeld. |
| Shopify-product | `content/products/e-gift-card/` | Labels in euro bij dollarprijzen ($25, $50, $100, $200), badge "SALE" zonder korting | Eerst repareren: een mail die "$50" toont en een pagina die "€50,00" toont, wekt wantrouwen. |

### W1-test T04: welkomstcode als code tegen als gift card

Bron: Klaviyo metric-aggregates op `$variation` binnen W1-bericht RN7Yy6 (flow T4a5Mk), 9 okt 00:40 tot 15 okt 00:30 UTC, orders toegeschreven tot 15 okt 12:00 UTC. Zelfde onderwerp en preview in beide armen; alleen de aanbodkaart verschilde.

| Arm | Ontvangers | Unieke kliks | Klik | Orders | Omzet | Per ontvanger |
|---|---|---|---|---|---|---|
| A, code als codeblok (VnXKz4) | 851 | 23 | 2,70% | 10 | $2,666 | $3.13 |
| B, zelfde code als "welcome gift card" (SXwPrW) | 774 | 22 | 2,84% | 4 | $1,067 | $1.38 |

Kans dat B beter is: klik 57 procent (gelijk), conversie 8 procent. De steekproef is klein (gepland was 5 weken, gestopt na 6 dagen), dus geen hard bewijs, maar er is geen enkel signaal dat de gift-card-verpakking helpt. Uitschrijvingen zijn niet per variant te splitsen (het event draagt geen variatie). Inhoudelijk speelt ook mee: een gift card is een betaalmiddel en een code is een korting (`content/products/e-gift-card/product.md` waarschuwt hier al voor). Wie "gift card" leest en een code krijgt, voelt zich misleid. **Advies: de welkomstcode niet meer als gift card verpakken.**

## 2. Floris' beeld eerlijk beoordeeld

Bestanden: `floris-giftcard-goud.webp` (origineel), `logo-vergelijking.png` (monogram naast het officiële lockup en als overlay).

**Wat goed is**
- Het voelt meteen als een cadeau: strik, zwaar metaal, licht schuin. Dat is precies wat een gift card in een mail moet doen.
- Transparante achtergrond (alfa-kanaal), dus het werkt op crème, wit en donker zonder vlak eromheen.
- Geborsteld metaal past bij een metaalmerk; het verhaal "een kaart van metaal" sluit aan op titanium.

**Wat niet kan of niet past**
- **Logo nagebouwd door AI.** Visueel vergeleken met `brand/logo/lockup/siraat-lockup-black.png` (rechtgezet en op gelijke grootte gelegd): de lijnen van het monogram zijn dunner en als groeven met een opstaande rand getekend, de tegenvormen kloppen niet (vooral het "7"-deel rechtsboven met de schuine afsnijding en de middelste balk onderaan), en de verhouding monogram tot woordmerk is anders (woordmerk relatief groter en zwaarder dan in het lockup). De overlap van de vormen is 0,56 (1,0 is identiek). Het woordmerk SIRAAT lijkt er sterk op, maar is ook gerenderd en niet het bestand. Regel: logo altijd het echte lockup, nooit door AI. Ook "GIFT CARD" is door het model gezet.
- **Goud is geen merkkleur.** Palet: titanium #C9C6C0, espresso #321E1D, brick #AC3B19, crème. Goud leest als "luxe creditcard" en botst met de belofte van één eerlijk materiaal (titanium). De pannen zelf zijn zilvergrijs. Goud kan als feestversie in december, niet als standaard.
- **Geen flash-fotostijl.** Het is een glanzende 3D-render. Voor een object (kaart) is dat aanvaardbaar, maar het is geen hero: in de hero blijft een echte flash-foto van mensen of product.
- **Leesbaarheid op mobiel.** Op 375 px is de kaart ongeveer 335 px breed; het logo wordt dan ongeveer 160 px en "GIFT CARD" ongeveer 6 px hoog: onleesbaar. Bedrag, naam en afzender moeten dus live tekst zijn, onder het beeld.
- **Formaat.** WebP werkt niet in Outlook voor Windows. Voor mail: PNG met transparantie (1100 px, 8-bit: 164 KB goud, 100 KB titanium) of JPG op crème (95 KB). Met JPG op crème verschijnt in geforceerd donker een crème rechthoek (zie `demo/v1-375-forced.png`); met PNG niet. Norm voor een kaartbeeld is onder 120 KB, dus titanium PNG past, goud net niet.

## 3. Benchmarks

Beperking: de sites van HexClad, Our Place, Caraway en Made In zijn vanuit deze omgeving niet bereikbaar (proxy 403), en de concurrenten-inbox (`research/concurrenten/`, sinds 12 okt) bevat nog geen gift-card-mails; die komen meestal pas vanaf eind november. Wat wel bekeken is:

- **Costa Nova** (Email Love, 25 sep 2026, "A COSTA NOVA Gift Card for Thanksgiving"): de kaart als fysiek object in een sfeerfoto, in de eigen merkkleur, met logo en "Gift card". Kop "Give the gift of choice". Geen bedrag op de kaart; het bedrag en de uitleg staan in de tekst.
- **Cariloha** (Email Love, 29 aug 2026, "A $50 Gift Card is Yours!"): geen kaartbeeld maar het bedrag zeer groot in typografie ("$50 GIFT CARD"), daaronder de voorwaarden en de geldigheid, dan een knop.
- **Made In** (reseller-pagina's): e-gift card, alleen online in te wisselen, geen vervaldatum volgens die pagina's. Niet bij Made In zelf geverifieerd.
- Uit eigen kennis, niet in deze sessie geverifieerd: de grote kookgerei-merken tonen in december een vlakke kaart in merkkleur met het logo, vaak met de vier bedragen als keuzeknoppen, en de hoofdboodschap "arrives instantly by email".

Wat werkt (en wat wij overnemen):
- **Bedrag groot en concreet** ($50), niet "a gift card".
- **Voor wie en van wie**: "For Anna" en "From Benjamin" (of de koper). In de transactionele mail aan de koper komt de naam uit het order-event; in campagnes laten we de naam weg of gebruiken we de voornaam van de lezer.
- **Hoe besteden en wanneer het aankomt**: "Delivered by email. Spend it on anything in the shop."
- **Geldigheid alleen als die vaststaat.** Voor ons is de vervaldatum onbekend (`content/products/e-gift-card/claims.md`: nooit "never expires" zonder bron). Eerst bij Floris of in Shopify vastleggen.

## 4. Advies en varianten

Alle mockups gebruiken het echte lockup uit `brand/logo/lockup/` (script `make_mockups.py`), niets is nagetekend.

| Variant | Bestand | Wat | Wanneer |
|---|---|---|---|
| A | `v1-goud-echt-lockup.png` | Floris' kaart, AI-logo en AI-tekst weggepoetst, echt lockup als gravure erop, "GIFT CARD" in Inter | Alleen als feestversie (kerst) als Floris goud wil houden |
| B | `v2-titanium.png` | Dezelfde kaart en strik in titanium-tint, echt lockup | **Aanbevolen sfeerbeeld** in GC1 tot GC3 en G1: cadeaugevoel van Floris' strik, in ons materiaal |
| C | `v3-titanium-plat.jpg`, `v3-titanium-50.jpg` | Vlakke geborstelde titanium kaart (eigen render, geen AI), brick lint, lockup, bedrag in TT Ramillas in het beeld | **Aanbevolen functionele kaart**: vier beelden ($25, $50, $100, $200), gekozen met een if op het order-item; in G1 (koper), browse op de gift-card-pagina en P3 |

Mobiele screenshots 375 px (licht en geforceerd donker) in `demo/`, met vaste header en footer uit `klaviyo/templates/partials/` (`make_demo.py`, gerenderd met `scripts/qa_mail_shots.js`). Overzicht: `overzicht-375.png`.

- `demo/v1-375-light.png`, `demo/v2-375-light.png`: kaartbeeld plus live strook "FOR ANNA / $50 / From Benjamin..." en knop. De strook heeft een eigen `bgcolor`, dus blijft leesbaar in elke modus.
- `demo/v3s-375-light.png`: variant C met het bedrag in het beeld; geen live tekst nodig, werkt ook zonder naam.
- `demo/v3-375-light.png` en `demo/v3-375-forced.png`: bedrag en naam als live tekst over het kaartbeeld (achtergrondbeeld met VML). In geforceerd donker (Gmail-app, Outlook) wordt de tekst wit op een lichte kaart en is hij onleesbaar. **Daarom nooit live tekst over een beeld.**

Waar wel, waar niet:
- **Wel**: decembercampagnes GC1 tot GC3 (variant B boven, variant C bij de bedragen), G1 aan de koper (variant C met het gekochte bedrag plus live strook met ontvanger), G2 herinnering, browse-mail als iemand /products/e-gift-card bekeek, P3 als alternatief voor wie een cadeau zoekt.
- **Niet**: de welkomstcode als "welcome gift card" (T04), checkout en cart (afleiding van de kar), hero's (die blijven flash-foto's).

## 5. Open punten voor Floris

1. Kies: goud als feestversie houden (A) of alles in titanium (B en C).
2. Shopify-product: labels van euro naar dollar, badge "SALE" weg, vervaldatum vastleggen.
3. Na de keuze: blok `{{BLOCK:giftcard amount=".." name=".."}}` in `partials/blocks/` plus ondersteuning in `scripts/build_template.py`, de G- en GC-mails herbouwen in v5-stijl, beelden via `scripts/export_klaviyo.py` naar de bibliotheek. Niets hiervan is gedaan of live.
