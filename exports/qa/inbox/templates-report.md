# Inbox-QA op alle templates (automatisch)

Gegenereerd door `python3 -I scripts/qa_inbox.py templates --markets=US,UK`. Controles uit `scripts/mail_checks.py`; renders met Django op het eerste testevent per flow, markt via `v5checks.market_ctx`.

## Systematisch (in vrijwel elke mail)

- FOUT Beelden: 13 beelden, 292 KB totaal (122 van 122 renders)
- FOUT Beelden: CDN-versie ontbreekt of laadt niet: logo-black-cream.png (niet in klaviyo-urls.txt), logo-white-dark.png (niet in klaviyo-urls.txt) (122 van 122 renders)
- LET OP Dark mode: forced 375 px: lichte blokken op donkere achtergrond (beeld met witte rand): pc-lid.jpg, pc-mini.jpg, pc-board.jpg, gift-shipping.jpg (+3) (106 van 122 renders)

## Overzicht

| mail | US FOUT / LET OP | UK FOUT / LET OP |
|---|---|---|
| anniversary/n1 | Beelden / Dark mode | Beelden / Dark mode |
| anniversary/n2-nocode | Beelden / Dark mode | Beelden / Dark mode |
| anniversary/n2 | Beelden / Dark mode | Beelden / Dark mode |
| browse/b1-acc | Beelden / Dark mode | Beelden / Dark mode |
| browse/b1 | Beelden / Dark mode | Beelden / Dark mode |
| browse/b2-clicked-nocode | Beelden / Dark mode | Beelden / Dark mode |
| browse/b2-clicked | Beelden / Dark mode | Beelden / Dark mode |
| browse/b2-notclicked | Beelden / Dark mode | Beelden / Dark mode |
| cart/k1-acc | Linktekst past bij bestemming, Beelden / Dark mode | Linktekst past bij bestemming, Beelden / Dark mode |
| cart/k1 | Linktekst past bij bestemming, Beelden / Dark mode | Linktekst past bij bestemming, Beelden / Dark mode |
| cart/k2-new | Linktekst past bij bestemming, Beelden / Dark mode | Linktekst past bij bestemming, Beelden / Dark mode |
| cart/k2-returning | Linktekst past bij bestemming, Beelden / Dark mode | Linktekst past bij bestemming, Beelden / Dark mode |
| cart/k3-nocode | Linktekst past bij bestemming, Beelden / Dark mode | Linktekst past bij bestemming, Beelden / Dark mode |
| cart/k3 | Beelden / Dark mode | Beelden / Dark mode |
| checkout/c1 | Beelden / Dark mode | Beelden / Dark mode |
| checkout/c2-acc | Beelden / Dark mode | Beelden / Dark mode |
| checkout/c2 | Beelden / Dark mode | Beelden / Dark mode |
| checkout/c3-acc | Beelden / Dark mode | Beelden / Dark mode |
| checkout/c3-p | Beelden / Dark mode | Beelden / Dark mode |
| checkout/c3-s | Beelden / Dark mode | Beelden / Dark mode |
| checkout/c4-nocode | Beelden / Dark mode | Beelden / Dark mode |
| checkout/c4 | Beelden / Dark mode | Beelden / Dark mode |
| post-purchase/p1-first | Beelden / Dark mode | Beelden / Dark mode |
| post-purchase/p1-repeat | Beelden / Dark mode | Beelden / Dark mode |
| post-purchase/p2-safe | Beelden / - | Beelden / - |
| post-purchase/p2 | Beelden / - | Beelden / - |
| post-purchase/p3-accessory-nocode | Beelden / Dark mode | Beelden / Dark mode |
| post-purchase/p3-accessory | Beelden / Dark mode | Beelden / Dark mode |
| post-purchase/p3-apron-nocode | Beelden / Dark mode | Beelden / Dark mode |
| post-purchase/p3-apron | Beelden / Dark mode | Beelden / Dark mode |
| post-purchase/p3-next-nocode | Beelden / Dark mode | Beelden / Dark mode |
| post-purchase/p3-next | Beelden / Dark mode | Beelden / Dark mode |
| post-purchase/p3-pan-nocode | Beelden / Dark mode | Beelden / Dark mode |
| post-purchase/p3-pan | Beelden / Dark mode | Beelden / Dark mode |
| post-purchase/p3-set-nocode | Beelden / Dark mode | Beelden / Dark mode |
| post-purchase/p3-set | Beelden / Dark mode | Beelden / Dark mode |
| site/a1 | Beelden / Dark mode | Beelden / Dark mode |
| site/a2 | Beelden / Dark mode | Beelden / Dark mode |
| sunset/s1 | Beelden / - | Beelden / - |
| sunset/s2 | Beelden / - | Beelden / - |
| sunset/s3-kept | Beelden / - | Beelden / - |
| sunset/s4-kept | Beelden / - | Beelden / - |
| ugc/u1 | Beelden / - | Beelden / - |
| vip/v1-nocode | Beelden / Dark mode | Beelden / Dark mode |
| vip/v1 | Beelden / Links (status 200), Dark mode | Beelden / Links (status 200), Dark mode |
| vip/v2 | Beelden / - | Beelden / - |
| welcome/w0 | Beelden / Dark mode | Beelden / Dark mode |
| welcome/w1-a | Beelden / Dark mode | Beelden / Dark mode |
| welcome/w1-b | Beelden / Dark mode | Beelden / Dark mode |
| welcome/w2 | Beelden / Dark mode | Beelden / Dark mode |
| welcome/w3 | Beelden / Dark mode | Beelden / Dark mode |
| welcome/w4-int | Beelden / Valuta en maat, Dark mode | Beelden / Dark mode |
| welcome/w4-us | Beelden / Dark mode | Beelden / Dark mode |
| welcome/w5 | Beelden / Dark mode | Beelden / Dark mode |
| winback/r1-acc | Beelden / Dark mode | Beelden / Dark mode |
| winback/r1-pan | Beelden / Dark mode | Beelden / Dark mode |
| winback/r1-set | Beelden / Dark mode | Beelden / Dark mode |
| winback/r2-nocode | Beelden / Dark mode | Beelden / Dark mode |
| winback/r2-vip-nocode | Beelden / Dark mode | Beelden / Dark mode |
| winback/r2-vip | Beelden / Links (status 200), Dark mode | Beelden / Links (status 200), Dark mode |
| winback/r2 | Beelden / Dark mode | Beelden / Dark mode |

## Details per mail (zonder de systematische punten)

### cart/k1-acc

- US FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- UK FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x

### cart/k1

- US FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- UK FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x

### cart/k2-new

- US FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- UK FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x

### cart/k2-returning

- US FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- UK FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x

### cart/k3-nocode

- US FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- UK FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x

### post-purchase/p2-safe

- US FOUT Beelden: zwaar (>300 KB): egg-slide-lite.gif 559 KB
- UK FOUT Beelden: zwaar (>300 KB): egg-slide-lite.gif 559 KB

### post-purchase/p2

- US FOUT Beelden: zwaar (>300 KB): egg-slide-lite.gif 559 KB
- UK FOUT Beelden: zwaar (>300 KB): egg-slide-lite.gif 559 KB

### vip/v1

- US LET OP Links (status 200): sociale links niet te openen vanuit deze omgeving: Facebook (www.facebook.com), Instagram (www.instagram.com). Niet gecontroleerd: Get my 15% now → (rate limit van de shop, later opnieuw)
- UK LET OP Links (status 200): sociale links niet te openen vanuit deze omgeving: Facebook (www.facebook.com), Instagram (www.instagram.com). Niet gecontroleerd: Get my 15% now → (rate limit van de shop, later opnieuw)

### welcome/w0

- US FOUT Beelden: zwaar (>300 KB): gif-water-test.gif 396 KB, gif-egg-slide.gif 664 KB
- UK FOUT Beelden: zwaar (>300 KB): gif-water-test.gif 396 KB, gif-egg-slide.gif 664 KB

### welcome/w4-int

- US LET OP Valuta en maat: markt US. "duties paid" in een US-mail; cm in een US-mail: "★★★★ “Purchased the 30cm Tita"

### winback/r2-vip

- US LET OP Links (status 200): sociale links niet te openen vanuit deze omgeving: Facebook (www.facebook.com), Instagram (www.instagram.com). Niet gecontroleerd:  (rate limit van de shop, later opnieuw), For VIPs, 72 hours. You came b (rate limit van de shop, later opnieuw), The 6-piece set Mini, Small an (rate limit van de shop, later opnieuw)
- UK LET OP Links (status 200): sociale links niet te openen vanuit deze omgeving: Facebook (www.facebook.com), Instagram (www.instagram.com). Niet gecontroleerd:  (rate limit van de shop, later opnieuw), For VIPs, 72 hours. You came b (rate limit van de shop, later opnieuw), The 6-piece set Mini, Small an (rate limit van de shop, later opnieuw)

