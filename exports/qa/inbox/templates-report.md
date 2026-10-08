# Inbox-QA op alle templates (automatisch)

Gegenereerd door `python3 -I scripts/qa_inbox.py templates --markets=US,UK`. Controles uit `scripts/mail_checks.py`; renders met Django op het eerste testevent per flow, markt via `v5checks.market_ctx`.

## Systematisch (in vrijwel elke mail)


## Overzicht

| mail | US FOUT / LET OP | UK FOUT / LET OP |
|---|---|---|
| anniversary/n1 | - / Valuta en maat | - / - |
| anniversary/n2-nocode | - / Valuta en maat | - / - |
| anniversary/n2 | - / Valuta en maat | - / - |
| browse/b1-acc | - / - | - / - |
| browse/b1 | - / - | - / - |
| browse/b2-clicked-nocode | - / - | - / - |
| browse/b2-clicked | - / - | - / - |
| browse/b2-notclicked | - / Dark mode | - / Dark mode |
| cart/k1-acc | Linktekst past bij bestemming / - | Linktekst past bij bestemming / - |
| cart/k1 | Linktekst past bij bestemming / - | Linktekst past bij bestemming / - |
| cart/k2-new | Linktekst past bij bestemming / - | Linktekst past bij bestemming / - |
| cart/k2-returning | Linktekst past bij bestemming / - | Linktekst past bij bestemming / - |
| cart/k3-nocode | Linktekst past bij bestemming / - | Linktekst past bij bestemming / - |
| cart/k3 | - / - | - / - |
| checkout/c1 | - / Dark mode | - / Dark mode |
| checkout/c2-acc | - / - | - / - |
| checkout/c2 | - / - | - / - |
| checkout/c3-acc | - / - | - / - |
| checkout/c3-p | - / Linktekst past bij bestemming | - / Linktekst past bij bestemming |
| checkout/c3-s | - / - | - / - |
| checkout/c4-nocode | - / - | - / - |
| checkout/c4 | - / - | - / - |
| post-purchase/p1-first | - / Valuta en maat | - / - |
| post-purchase/p1-repeat | - / Valuta en maat | - / - |
| post-purchase/p2-safe | - / Beelden, Valuta en maat | - / Beelden |
| post-purchase/p2 | - / Beelden | - / Beelden |
| post-purchase/p3-accessory-nocode | - / Valuta en maat | - / - |
| post-purchase/p3-accessory | - / Valuta en maat | - / - |
| post-purchase/p3-apron-nocode | - / Valuta en maat | - / - |
| post-purchase/p3-apron | - / Valuta en maat | - / - |
| post-purchase/p3-next-nocode | - / Valuta en maat | - / - |
| post-purchase/p3-next | - / Valuta en maat | - / - |
| post-purchase/p3-pan-nocode | - / Valuta en maat | - / - |
| post-purchase/p3-pan | - / Valuta en maat | - / - |
| post-purchase/p3-set-nocode | - / Valuta en maat | - / - |
| post-purchase/p3-set | - / Valuta en maat | - / - |
| site/a1 | - / Valuta en maat | - / - |
| site/a2 | - / - | - / - |
| sunset/s1 | - / - | - / - |
| sunset/s2 | - / - | - / - |
| sunset/s3-kept | - / - | - / - |
| sunset/s4-kept | - / - | - / - |
| ugc/u1 | - / - | - / - |
| vip/v1-nocode | - / Valuta en maat | - / - |
| vip/v1 | - / Valuta en maat | - / - |
| vip/v2 | - / - | - / - |
| welcome/w0 | - / Beelden | - / Beelden |
| welcome/w1-a | - / Dark mode | - / Dark mode |
| welcome/w1-b | - / Dark mode | - / Dark mode |
| welcome/w2 | - / - | - / - |
| welcome/w3 | - / - | - / - |
| welcome/w4-int | - / Valuta en maat | - / - |
| welcome/w4-us | - / Valuta en maat | - / - |
| welcome/w5 | - / - | - / - |
| winback/r1-acc | - / Valuta en maat, Dark mode | - / Dark mode |
| winback/r1-pan | - / Valuta en maat | - / - |
| winback/r1-set | - / Valuta en maat | - / - |
| winback/r2-nocode | - / Valuta en maat | - / - |
| winback/r2-vip-nocode | - / Valuta en maat | - / - |
| winback/r2-vip | - / Valuta en maat | - / - |
| winback/r2 | - / Valuta en maat | - / - |

## Details per mail (zonder de systematische punten)

### anniversary/n1

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### anniversary/n2-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### anniversary/n2

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### browse/b2-notclicked

- US LET OP Dark mode: tekst met laag contrast: dark 375 px: "Preheat on medium for 2 to 3 m" 2.8:1
- UK LET OP Dark mode: tekst met laag contrast: dark 375 px: "Preheat on medium for 2 to 3 m" 2.8:1

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

- US LET OP Dark mode: tekst met laag contrast: dark 375 px: "Light Labs report no. 25895: 3" 2.8:1
- UK LET OP Dark mode: tekst met laag contrast: dark 375 px: "Light Labs report no. 25895: 3" 2.8:1

### checkout/c3-p

- US LET OP Linktekst past bij bestemming: [LET OP] "Keep my one pan and check out" -> /checkouts/sample/recover
- UK LET OP Linktekst past bij bestemming: [LET OP] "Keep my one pan and check out" -> /checkouts/sample/recover

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

### site/a1

- US LET OP Valuta en maat: markt US. cm in een US-mail: "ELLER Standard 11″ (28 cm) Fiv"; cm in een US-mail: "Pan Pro Large, 12″ (30 cm) The"; cm in een US-mail: "Pan Pro Small, 10″ (26 cm) Tit"; cm in een US-mail: "Pro Standard, 11″ (28 cm) Tit"

### vip/v1-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### vip/v1

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### welcome/w0

- US LET OP Beelden: zwaar (>300 KB): gif-water-test.gif 396 KB, gif-egg-slide.gif 664 KB
- UK LET OP Beelden: zwaar (>300 KB): gif-water-test.gif 396 KB, gif-egg-slide.gif 664 KB

### welcome/w1-a

- US LET OP Dark mode: tekst met laag contrast: dark 375 px: "Light Labs report no. 25895: 3" 2.8:1
- UK LET OP Dark mode: tekst met laag contrast: dark 375 px: "Light Labs report no. 25895: 3" 2.8:1

### welcome/w1-b

- US LET OP Dark mode: tekst met laag contrast: dark 375 px: "Light Labs report no. 25895: 3" 2.8:1
- UK LET OP Dark mode: tekst met laag contrast: dark 375 px: "Light Labs report no. 25895: 3" 2.8:1

### welcome/w4-int

- US LET OP Valuta en maat: markt US. "duties paid" in een US-mail; cm in een US-mail: "ELLER Standard 11″ (28 cm) Eve"; cm in een US-mail: "Pan Pro Large, 12″ (30 cm) The"; cm in een US-mail: "Pan Pro Small, 10″ (26 cm) Tit"

### welcome/w4-us

- US LET OP Valuta en maat: markt US. cm in een US-mail: "ELLER Standard 11″ (28 cm) Eve"; cm in een US-mail: "Pan Pro Large, 12″ (30 cm) The"; cm in een US-mail: "Pan Pro Small, 10″ (26 cm) Tit"; cm in een US-mail: "Pro Standard, 11″ (28 cm) Tit"

### winback/r1-acc

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US LET OP Dark mode: tekst met laag contrast: dark 375 px: "Light Labs report no. 25895: 3" 2.8:1
- UK LET OP Dark mode: tekst met laag contrast: dark 375 px: "Light Labs report no. 25895: 3" 2.8:1

### winback/r1-pan

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### winback/r1-set

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### winback/r2-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### winback/r2-vip-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### winback/r2-vip

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

### winback/r2

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"

