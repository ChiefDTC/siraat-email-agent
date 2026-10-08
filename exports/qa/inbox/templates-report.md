# Inbox-QA op alle templates (automatisch)

Gegenereerd door `python3 -I scripts/qa_inbox.py templates --markets=US,UK`. Controles uit `scripts/mail_checks.py`; renders met Django op het eerste testevent per flow, markt via `v5checks.market_ctx`.

## Systematisch (in vrijwel elke mail)

- FOUT Dark mode: forced 375 px: lichte blokken op donkere achtergrond (beeld met witte rand): pc-lid.jpg, pc-mini.jpg, pc-board.jpg, gift-shipping.jpg (+3) (106 van 122 renders)
- FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond) (122 van 122 renders)

## Overzicht

| mail | US FOUT / LET OP | UK FOUT / LET OP |
|---|---|---|
| anniversary/n1 | Dark mode / Valuta en maat | Dark mode / - |
| anniversary/n2-nocode | Dark mode / Valuta en maat | Dark mode / - |
| anniversary/n2 | Dark mode / Valuta en maat | Dark mode / - |
| browse/b1-acc | Dark mode / - | Dark mode / - |
| browse/b1 | Dark mode / - | Dark mode / - |
| browse/b2-clicked-nocode | Dark mode / - | Dark mode / - |
| browse/b2-clicked | Dark mode / - | Dark mode / - |
| browse/b2-notclicked | Dark mode / - | Dark mode / - |
| cart/k1-acc | Linktekst past bij bestemming, Dark mode / - | Linktekst past bij bestemming, Dark mode / - |
| cart/k1 | Linktekst past bij bestemming, Dark mode / - | Linktekst past bij bestemming, Dark mode / - |
| cart/k2-new | Linktekst past bij bestemming, Dark mode / - | Linktekst past bij bestemming, Dark mode / - |
| cart/k2-returning | Linktekst past bij bestemming, Dark mode / - | Linktekst past bij bestemming, Dark mode / - |
| cart/k3-nocode | Linktekst past bij bestemming, Dark mode / - | Linktekst past bij bestemming, Dark mode / - |
| cart/k3 | Dark mode / - | Dark mode / - |
| checkout/c1 | Dark mode / - | Dark mode / - |
| checkout/c2-acc | Dark mode / - | Dark mode / - |
| checkout/c2 | Dark mode / - | Dark mode / - |
| checkout/c3-acc | Dark mode / - | Dark mode / - |
| checkout/c3-p | Dark mode / - | Dark mode / - |
| checkout/c3-s | Dark mode / - | Dark mode / - |
| checkout/c4-nocode | Dark mode / - | Dark mode / - |
| checkout/c4 | Dark mode / - | Dark mode / - |
| post-purchase/p1-first | Dark mode / Valuta en maat | Dark mode / - |
| post-purchase/p1-repeat | Dark mode / Valuta en maat | Dark mode / - |
| post-purchase/p2-safe | Dark mode / Beelden, Valuta en maat | Dark mode / Beelden |
| post-purchase/p2 | Dark mode / Beelden | Dark mode / Beelden |
| post-purchase/p3-accessory-nocode | Dark mode / Valuta en maat | Dark mode / - |
| post-purchase/p3-accessory | Dark mode / Valuta en maat | Dark mode / - |
| post-purchase/p3-apron-nocode | Dark mode / Valuta en maat | Dark mode / - |
| post-purchase/p3-apron | Dark mode / Valuta en maat | Dark mode / - |
| post-purchase/p3-next-nocode | Dark mode / Valuta en maat | Dark mode / - |
| post-purchase/p3-next | Dark mode / Valuta en maat | Dark mode / - |
| post-purchase/p3-pan-nocode | Dark mode / Valuta en maat | Dark mode / - |
| post-purchase/p3-pan | Dark mode / Valuta en maat | Dark mode / - |
| post-purchase/p3-set-nocode | Dark mode / Valuta en maat | Dark mode / - |
| post-purchase/p3-set | Dark mode / Valuta en maat | Dark mode / - |
| site/a1 | Dark mode / - | Dark mode / - |
| site/a2 | Dark mode / - | Dark mode / - |
| sunset/s1 | Dark mode / - | Dark mode / - |
| sunset/s2 | Dark mode / - | Dark mode / - |
| sunset/s3-kept | Dark mode / - | Dark mode / - |
| sunset/s4-kept | Dark mode / - | Dark mode / - |
| ugc/u1 | Dark mode / - | Dark mode / - |
| vip/v1-nocode | Dark mode / Valuta en maat | Dark mode / - |
| vip/v1 | Dark mode / Valuta en maat | Dark mode / - |
| vip/v2 | Dark mode / - | Dark mode / - |
| welcome/w0 | Dark mode / Beelden | Dark mode / Beelden |
| welcome/w1-a | Dark mode / - | Dark mode / - |
| welcome/w1-b | Dark mode / - | Dark mode / - |
| welcome/w2 | Dark mode / - | Dark mode / - |
| welcome/w3 | Dark mode / - | Dark mode / - |
| welcome/w4-int | Dark mode / Valuta en maat | Dark mode / - |
| welcome/w4-us | Dark mode / - | Dark mode / - |
| welcome/w5 | Dark mode / - | Dark mode / - |
| winback/r1-acc | Dark mode / Valuta en maat | Dark mode / - |
| winback/r1-pan | Dark mode / Valuta en maat | Dark mode / - |
| winback/r1-set | Links (status 200), Dark mode / Valuta en maat | Links (status 200), Dark mode / - |
| winback/r2-nocode | Dark mode / Valuta en maat | Dark mode / - |
| winback/r2-vip-nocode | Dark mode / Valuta en maat | Dark mode / - |
| winback/r2-vip | Dark mode / Valuta en maat | Dark mode / - |
| winback/r2 | Dark mode / Valuta en maat | Dark mode / - |

## Details per mail (zonder de systematische punten)

### anniversary/n1

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### anniversary/n2-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### anniversary/n2

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### browse/b2-notclicked

- US FOUT Dark mode: dark 375 px: tekst met laag contrast "Preheat on medium for 2 to 3 m" 2.8:1
- UK FOUT Dark mode: dark 375 px: tekst met laag contrast "Preheat on medium for 2 to 3 m" 2.8:1

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

### checkout/c1

- US FOUT Dark mode: dark 375 px: tekst met laag contrast "Light Labs report no. 25895: 3" 2.8:1
- UK FOUT Dark mode: dark 375 px: tekst met laag contrast "Light Labs report no. 25895: 3" 2.8:1

### post-purchase/p1-first

- US LET OP Valuta en maat: markt US. cm in een US-mail: "e splatter. Add the 28 cm lid"; cm in een US-mail: "″ Pan Pro takes the 28 cm lid."

### post-purchase/p1-repeat

- US LET OP Valuta en maat: markt US. cm in een US-mail: "e splatter. Add the 28 cm lid"; cm in een US-mail: "″ Pan Pro takes the 28 cm lid."

### post-purchase/p2-safe

- US LET OP Beelden: zwaar (>300 KB): egg-slide-lite.gif 559 KB
- US LET OP Valuta en maat: markt US (geen bedrag in eigen valuta gezien). cm in een US-mail: "e splatter. Add the 28 cm lid"; cm in een US-mail: "″ Pan Pro takes the 28 cm lid."
- UK LET OP Beelden: zwaar (>300 KB): egg-slide-lite.gif 559 KB

### post-purchase/p2

- US LET OP Beelden: zwaar (>300 KB): egg-slide-lite.gif 559 KB
- UK LET OP Beelden: zwaar (>300 KB): egg-slide-lite.gif 559 KB

### post-purchase/p3-accessory-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### post-purchase/p3-accessory

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### post-purchase/p3-apron-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### post-purchase/p3-apron

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### post-purchase/p3-next-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### post-purchase/p3-next

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### post-purchase/p3-pan-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "pan: 20, 26, 28 or 30 cm. The"; cm in een US-mail: "tainless Steel Lid, 28 cm Fits"; cm in een US-mail: "″ Pan Pro takes the 28 cm lid."

### post-purchase/p3-pan

- US LET OP Valuta en maat: markt US. cm in een US-mail: "pan: 20, 26, 28 or 30 cm. The"; cm in een US-mail: "tainless Steel Lid, 28 cm Fits"; cm in een US-mail: "″ Pan Pro takes the 28 cm lid."

### post-purchase/p3-set-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### post-purchase/p3-set

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### vip/v1-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### vip/v1

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### welcome/w0

- US LET OP Beelden: zwaar (>300 KB): gif-water-test.gif 396 KB, gif-egg-slide.gif 664 KB
- UK LET OP Beelden: zwaar (>300 KB): gif-water-test.gif 396 KB, gif-egg-slide.gif 664 KB

### welcome/w1-a

- US FOUT Dark mode: dark 375 px: tekst met laag contrast "Light Labs report no. 25895: 3" 2.8:1
- UK FOUT Dark mode: dark 375 px: tekst met laag contrast "Light Labs report no. 25895: 3" 2.8:1

### welcome/w1-b

- US FOUT Dark mode: dark 375 px: tekst met laag contrast "Light Labs report no. 25895: 3" 2.8:1
- UK FOUT Dark mode: dark 375 px: tekst met laag contrast "Light Labs report no. 25895: 3" 2.8:1

### welcome/w4-int

- US LET OP Valuta en maat: markt US. "duties paid" in een US-mail; cm in een US-mail: "★★★★ “Purchased the 30cm Tita"

### winback/r1-acc

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: dark 375 px: tekst met laag contrast "Light Labs report no. 25895: 3" 2.8:1
- UK FOUT Dark mode: dark 375 px: tekst met laag contrast "Light Labs report no. 25895: 3" 2.8:1

### winback/r1-pan

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### winback/r1-set

- US FOUT Links (status 200): sociale links niet te openen vanuit deze omgeving: Facebook (www.facebook.com), Instagram (www.instagram.com). "Shop with my 10% →" -> https://siraatskitchen.com/discount/HI10?redirect=/collections/all%3Futm_source%3Dklaviyo% geeft 429
- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- UK FOUT Links (status 200): sociale links niet te openen vanuit deze omgeving: Facebook (www.facebook.com), Instagram (www.instagram.com). "Shop with my 10% →" -> https://siraatskitchen.com/discount/HI10?redirect=/collections/all%3Futm_source%3Dklaviyo% geeft 429

### winback/r2-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### winback/r2-vip-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### winback/r2-vip

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### winback/r2

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

