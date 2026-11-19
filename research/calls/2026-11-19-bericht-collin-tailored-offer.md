Hey Collin,

I've been working on the tailored offer we discussed today. Don't mind the images of the smaller products for now, some shadows still need fixing.

**Figma:** https://www.figma.com/design/oaxnBkz3MAbePRnorCrQwz?node-id=376-106

**Trigger**
Placed Order, 5 minutes later. It's the first post-purchase email, before the order confirmation, while the customer is still warm.

**The offer**
- 15% off with code VIP15-PICKS, one use, valid until Nov 30.
- The top offer is the Cookware Set 12-Pcs for the US and the Pan Set 6-Pcs for every other country, because the 12-Pcs is US only. It's left out if they already own it.
- Below that: up to 3 products they viewed in the last 30 days, most recent first.
- Never a product they already own or anything inside a bundle they own.

**How it knows**
Two small tracker flows:
- One saves every Viewed Product on the profile.
- The other marks products as owned on Ordered Product, so Aftersell purchases count too.

**Scenarios**
- **US, bought the Standard, viewed Wok + Deep:** 12-Pcs on top, Wok and Deep below.
- **US, bought the 12-Pcs, viewed Large, Pizza Steel and knives:** no top offer, only Pizza Steel and knives. The Large is hidden because it's in the set.
- **US, bought the 12-Pcs, viewed the Standard 11":** the Standard is shown, because it's not in the 12-Pcs.
- **Viewed 5 products:** max 3 cards, most recent first.
- **UK, viewed Wok, 2+2 and 12-Pcs:** 6-Pcs on top, Wok only. US-only products are hidden.
- **US, bought the 34-Pcs:** no top offer, only items not in the set.
- **Bought the Standard, then added the 12-Pcs via Aftersell:** the tracker catches it, so no top offer.
- **Country unknown:** treated as non-US, so 6-Pcs on top.

**Status**
Built and tested, still in draft. As agreed, the plan is to run it as a 50/50 split against the current post-purchase. Before go-live I still need to:
- turn on the two trackers and backfill them,
- activate the code.
