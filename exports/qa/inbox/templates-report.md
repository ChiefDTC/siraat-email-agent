# Inbox-QA op alle templates (automatisch)

Gegenereerd door `python3 -I scripts/qa_inbox.py templates --markets=US,UK`. Controles uit `scripts/mail_checks.py`; renders met Django op het eerste testevent per flow, markt via `v5checks.market_ctx`.

## Systematisch (in vrijwel elke mail)


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
| winback/r1-set | Dark mode / Valuta en maat | Dark mode / - |
| winback/r2-nocode | Dark mode / Valuta en maat | Dark mode / - |
| winback/r2-vip-nocode | Dark mode / Valuta en maat | Dark mode / - |
| winback/r2-vip | Dark mode / Valuta en maat | Dark mode / - |
| winback/r2 | Dark mode / Valuta en maat | Dark mode / - |

## Details per mail (zonder de systematische punten)

### anniversary/n1

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### anniversary/n2-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg

### anniversary/n2

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg

### browse/b1-acc

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### browse/b1

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### browse/b2-clicked-nocode

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### browse/b2-clicked

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### browse/b2-notclicked

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: dark 375 px: tekst met laag contrast "Preheat on medium for 2 to 3 m" 2.8:1; forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg

### cart/k1-acc

- US FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### cart/k1

- US FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### cart/k2-new

- US FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### cart/k2-returning

- US FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### cart/k3-nocode

- US FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Linktekst past bij bestemming: [FOUT] "Finish my order →" -> /products/x
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### cart/k3

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### checkout/c1

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### checkout/c2-acc

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### checkout/c2

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### checkout/c3-acc

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: card-panpro-bestseller.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: card-panpro-bestseller.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg

### checkout/c3-p

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### checkout/c3-s

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### checkout/c4-nocode

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### checkout/c4

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### post-purchase/p1-first

- US LET OP Valuta en maat: markt US. cm in een US-mail: "e splatter. Add the 28 cm lid"; cm in een US-mail: "″ Pan Pro takes the 28 cm lid."
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### post-purchase/p1-repeat

- US LET OP Valuta en maat: markt US. cm in een US-mail: "e splatter. Add the 28 cm lid"; cm in een US-mail: "″ Pan Pro takes the 28 cm lid."
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: packshot-1.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### post-purchase/p2-safe

- US LET OP Beelden: zwaar (>300 KB): egg-slide-lite.gif 559 KB
- US LET OP Valuta en maat: markt US (geen bedrag in eigen valuta gezien). cm in een US-mail: "e splatter. Add the 28 cm lid"; cm in een US-mail: "″ Pan Pro takes the 28 cm lid."
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)
- UK LET OP Beelden: zwaar (>300 KB): egg-slide-lite.gif 559 KB
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)

### post-purchase/p2

- US LET OP Beelden: zwaar (>300 KB): egg-slide-lite.gif 559 KB
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)
- UK LET OP Beelden: zwaar (>300 KB): egg-slide-lite.gif 559 KB
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)

### post-purchase/p3-accessory-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### post-purchase/p3-accessory

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### post-purchase/p3-apron-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### post-purchase/p3-apron

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### post-purchase/p3-next-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### post-purchase/p3-next

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### post-purchase/p3-pan-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "pan: 20, 26, 28 or 30 cm. The"; cm in een US-mail: "tainless Steel Lid, 28 cm Fits"; cm in een US-mail: "″ Pan Pro takes the 28 cm lid."
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### post-purchase/p3-pan

- US LET OP Valuta en maat: markt US. cm in een US-mail: "pan: 20, 26, 28 or 30 cm. The"; cm in een US-mail: "tainless Steel Lid, 28 cm Fits"; cm in een US-mail: "″ Pan Pro takes the 28 cm lid."
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### post-purchase/p3-set-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### post-purchase/p3-set

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### site/a1

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: size-small.jpg; forced 375 px: licht blok op donkere achtergrond: size-standard.jpg; forced 375 px: licht blok op donkere achtergrond: pc-large.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: size-small.jpg; forced 375 px: licht blok op donkere achtergrond: size-standard.jpg; forced 375 px: licht blok op donkere achtergrond: pc-large.jpg

### site/a2

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: card-panpro-bestseller.jpg; forced 375 px: licht blok op donkere achtergrond: card-set6.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: card-panpro-bestseller.jpg; forced 375 px: licht blok op donkere achtergrond: card-set6.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg

### sunset/s1

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)

### sunset/s2

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)

### sunset/s3-kept

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)

### sunset/s4-kept

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)

### ugc/u1

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)

### vip/v1-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg

### vip/v1

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg

### vip/v2

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond)

### welcome/w0

- US LET OP Beelden: zwaar (>300 KB): gif-water-test.gif 396 KB, gif-egg-slide.gif 664 KB
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg; forced 375 px: licht blok op donkere achtergrond: gift-filter.jpg
- UK LET OP Beelden: zwaar (>300 KB): gif-water-test.gif 396 KB, gif-egg-slide.gif 664 KB
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg; forced 375 px: licht blok op donkere achtergrond: gift-filter.jpg

### welcome/w1-a

- US FOUT Dark mode: dark 375 px: tekst met laag contrast "Light Labs report no. 25895: 3" 2.8:1; forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: compare-cap-panpro.png; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: compare-cap-panpro.png; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg

### welcome/w1-b

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: compare-cap-panpro.png; forced 375 px: licht blok op donkere achtergrond: gift-card.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: compare-cap-panpro.png; forced 375 px: licht blok op donkere achtergrond: gift-card.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg

### welcome/w2

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg; forced 375 px: licht blok op donkere achtergrond: gift-filter.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg; forced 375 px: licht blok op donkere achtergrond: gift-filter.jpg

### welcome/w3

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg; forced 375 px: licht blok op donkere achtergrond: gift-filter.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg; forced 375 px: licht blok op donkere achtergrond: gift-filter.jpg

### welcome/w4-int

- US LET OP Valuta en maat: markt US. "duties paid" in een US-mail; cm in een US-mail: "★★★★ “Purchased the 30cm Tita"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-small.jpg; forced 375 px: licht blok op donkere achtergrond: pc-standard.jpg; forced 375 px: licht blok op donkere achtergrond: pc-large.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-small.jpg; forced 375 px: licht blok op donkere achtergrond: pc-standard.jpg; forced 375 px: licht blok op donkere achtergrond: pc-large.jpg

### welcome/w4-us

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-small.jpg; forced 375 px: licht blok op donkere achtergrond: pc-standard.jpg; forced 375 px: licht blok op donkere achtergrond: pc-large.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-small.jpg; forced 375 px: licht blok op donkere achtergrond: pc-standard.jpg; forced 375 px: licht blok op donkere achtergrond: pc-large.jpg

### welcome/w5

- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg; forced 375 px: licht blok op donkere achtergrond: gift-filter.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg; forced 375 px: licht blok op donkere achtergrond: gift-ebook.jpg; forced 375 px: licht blok op donkere achtergrond: gift-mystery.jpg; forced 375 px: licht blok op donkere achtergrond: gift-filter.jpg

### winback/r1-acc

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: compare-cap-panpro.png; forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: compare-cap-panpro.png; forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg

### winback/r1-pan

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### winback/r1-set

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg; forced 375 px: licht blok op donkere achtergrond: gift-shipping.jpg

### winback/r2-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg

### winback/r2-vip-nocode

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 2.8:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg

### winback/r2-vip

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg

### winback/r2

- US LET OP Valuta en maat: markt US. cm in een US-mail: "tainless Steel Lid, 28 cm Fits"
- US FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg
- UK FOUT Dark mode: forced 375 px: logo logo-black.png onzichtbaar (contrast 3.0:1 tussen logo en achtergrond); forced 375 px: licht blok op donkere achtergrond: pc-lid.jpg; forced 375 px: licht blok op donkere achtergrond: pc-mini.jpg; forced 375 px: licht blok op donkere achtergrond: pc-set6.jpg; forced 375 px: licht blok op donkere achtergrond: pc-board.jpg

