# Content mapping per flow and email (7 October 2026)

> Let op: gemaakt vóór Floris' antwoorden van 7 oktober. DECISIONS.md gaat voor: 6-delige set = $349, 12-pcs levertijd een paar dagen (geen backorder), oprichter Benjamin, 100,000+ klanten, Light Labs geldt voor alle pannen, HI10 blijft (A/B met gift-card-weergave), giveaway-pop-up blijft.

Read-only mapping of hero photo, headline, reviews, claims, product and GIF per email. Full fields in mapping.csv (same folder). Rules applied: one hero photo per email, never reused inside a flow (and in fact never reused at all), reviews unique per flow, only approved or owner-override claims, Light Labs only for the Pan Pro, no giveaway framing, no 'You're in'. Headlines are six words or fewer and render in TT Ramillas.

Emails mapped: 22 (20 with a hero photo, W2 is plain text, P4 is live and noted only). Distinct hero photos: 20.


## Welcome (W0 buyers, W1 to W5)

| email | day | hero image (id, title) | headline | reviews | main claim | product | GIF |
|---|---|---|---|---|---|---|---|
| W0 | 0 (buyers path, 10 min after signup) | 63225744752980: Preheating Pan Pro over gas flame (pre_heating_titanium_hammered_pan_pro.webp, 2048) | First heat, then oil, then patience | Aggie M. | No coatings | none (buyer already ordered) | gif-egg-slide.gif (hero below headline); gif-water-test.gif inline |
| W1 | 0 (10 min after signup) | 63501616283988: Woman eating an egg from the pan (Lifestyle_image_egg.jpg, 2048) | The original hammered titanium pan | Thomas D. | The original hammered titanium pan | original-siraat-100-pure-titanium-pan-with-hammered-pattern ($134, compare-at $439) | none |
| W2 | 1 (10:00) | none | none (plain text) | Fran G. | The original hammered titanium pan | original-siraat-100-pure-titanium-pan-with-hammered-pattern ($134, compare-at $439) | none |
| W3 | 3 (10:00) | 70573756547412: Hammered Pan Pro, pure titanium surface, studio (Regular_Hammered_Panttern_Pan_02, 3000) | Tested. Not claimed. | Jonathan D.; Gwen | Tested free from PFAS by Light Labs, an ISO/IEC 17025-accredited lab. Report no. 25895, released 30 October 2025. | original-siraat-100-pure-titanium-pan-with-hammered-pattern ($134, compare-at $439) | none |
| W4-US | 6 (10:00, US segment) | 69653576515924: Three pans with vegetables on the stove (Photo_Three_Pans_with_Vegetables_on_Stove_Pro.jpg, 4037x2691) | Three ways to start | Deb; David; Chetan G. | Free shipping on all orders | dishwashing-detergent-sheets-fresh-lemon ($25, compare-at $60) | none |
| W4-INT | 6 (10:00, non-US segment) | 64589539115348: Bundle of three hammered pans with fresh vegetables (bundle_set_hammered_pans.webp, 1080) | Three ways to start | Mrs J.; Graham C.; Caliann | Free shipping on all orders | dishwashing-detergent-sheets-fresh-lemon (link, no price) | none |
| W5 | 9 (10:00) | 62816122601812: Couple cooking dinner in Siraat aprons (Apron_Ember.webp, 2048) | In their words | Tammy; Marilyn B.; Sandi R. | 100K+ happy customers | original-siraat-100-pure-titanium-pan-with-hammered-pattern ($134, compare-at $439) | none |

## Checkout abandonment (C1 to C4)

| email | day | hero image (id, title) | headline | reviews | main claim | product | GIF |
|---|---|---|---|---|---|---|---|
| C1 | 0 (1 hour after Checkout Started) | 70885778555220: Single hammered pan with seafood on a gas range, lid lifted (P06-A_Stovetop, 1920x1280) | Your pan is still here | Susan M. | No coatings | dynamic cart block ({{ event.extra.line_items }}) | none |
| C2 | 2 (09:00 local) | 59266431975764: Folding a vegetable omelet in a titanium pan (gempages d2a399da, 4608x3072) | Three questions, one answer | Jason M.; Beverley S. | Tested free from PFAS by Light Labs, an ISO/IEC 17025-accredited lab. Report no. 25895, released 30 October 2025. | dynamic cart block (small) | none |
| C3 | 3 | 61213082714452: Flipping a crispy quesadilla with the titanium turner (A7406247_1, 2485) | Reserved at today's price | Jardier M.; Helenor S.; Lorraine | 3-ply | dynamic cart block | none |
| C4 | 4 (last) | 64589616873812: T-bone steak searing in a hammered pan on gas (steak_in_titanium_hammered_pan.webp, 1890) | Final call, gifts included | Chris B.; Deborah G. | Up to 50% off + 4 free gifts (October 2026 campaign offer) | dynamic cart block | none |

## Cart abandonment (K1 to K3)

| email | day | hero image (id, title) | headline | reviews | main claim | product | GIF |
|---|---|---|---|---|---|---|---|
| K1 | 0 (1 hour after Added to Cart, no Checkout Started) | 71715411001684: Wiping a Pan Pro Large clean with a cloth (9.webp, 1080) | One wipe. No scrubbing. | Carol E.; Tracey C. | Cleanup is 30 seconds | dynamic cart block | none (one-pass wipe GIF to be cut, see gaps) |
| K2 | 2 | 71326802510164: Basting steak in a hammered pan on induction (sv2-pan-basting.webp, 1920x1280) | Built to outlast you | Peter; Mrs H. | 75-year warranty | dynamic cart block | none |
| K3 | 3 (last) | 69725067542868: Woman eating a fried egg straight from the pan at the table (Lifestyle_image_egg_fbcf2a8f, 2048) | Covered for 75 years | Jack; D. C. | 75-year warranty | dynamic cart block | none |

## Browse abandonment (B1, B2)

| email | day | hero image (id, title) | headline | reviews | main claim | product | GIF |
|---|---|---|---|---|---|---|---|
| B1 | 0 (same day, 4 hours after Viewed Product) | 63960186650964: Close-up of the hammered titanium surface (Regular_Hammered_Panttern_Pan_05, 3000) | No coating to scratch off | Chris C.; Stevens W. | No coatings | dynamic: {{ event.ProductURL }} viewed product | none (scratch-test GIF to be cut, see gaps) |
| B2 | 2 | 62815908659540: Home cook tasting dinner in the Azure apron (ApronAzureEating.webp, 2048) | Week one, in their words | Stacey K.; Carlos C.; Cynthia | No coatings | dynamic: {{ event.ProductURL }} | none |

## Post-purchase (P1 to P4)

| email | day | hero image (id, title) | headline | reviews | main claim | product | GIF |
|---|---|---|---|---|---|---|---|
| P1 | 0 (order confirmed, 1 hour after Placed Order) | 56801963344212: Happy home cook holding the titanium turner and a frying pan (IMG_6175.jpg, 2316) | Good call. Here's what's coming. | Anne L.; Galit W. | Free shipping on all orders | dynamic order line items | none |
| P2 | delivered (Shipment Delivered + 1 day) | 63507278004564: Couple cooking a crepe in a titanium pan on gas (1.5.png, 2048) | If you can do an egg | Kathy; Cherry | No seasoning required | none (how-to) | gif-water-test.gif; gif-oil-shimmer.gif; gif-egg-slide.gif (in that order, one per step); gif-rainbow-tint.gif optional for the patina note |
| P3 | 14 | 58852686856532: Titanium pan with lid going into a hot oven (10_8858e586, 1890) | What goes with your pan | Joseph G.; Victoria; Mel | Anti-microbial | Pan buyers: stainless-steel-lid ($59), 2-pans-and-2-lids ($199), titanium-hammered-pan-pro-duo ($229, compare-at $570) | none |
| P4 | 30 | none | (live, unchanged) | Carlos C. | No coatings | none | none |

## Winback (R1, R2)

| email | day | hero image (id, title) | headline | reviews | main claim | product | GIF |
|---|---|---|---|---|---|---|---|
| R1 | 60 (no order in 60 days) | 72111681110356: Roast chicken with vegetables in the Roasting Pan (hammeredroastingpan.webp, 1024) | New since your last order | Pam B.; Jim M. | The original hammered titanium pan | US: titanium-hammered-roasting-pan ($199, compare-at $250, US only) | none |
| R2 | 90 (no order in 90 days) | 71326802477396: Roast chicken in a hammered pan in the oven, rivets visible (sv2-oven-rivets.webp, 1920x1280) | Half off. Here's the catch. | Martin M.; Gladys; Denise H. | Up to 50% off + 4 free gifts (October 2026 campaign offer) | titanium-hammered-pan-set-with-lids-6-pcs ($399, compare-at $1,384) | none |

## Gaps, grouped by what Siraat must supply

### Clean video (re-export without captions)
- All 5 chef-video GIFs (egg-slide, water-test, oil-shimmer, steak-sear, rainbow-tint) and all 11 stills have burned-in subtitles. Used in W0 and P2 (GIFs), W0 and P2 (stills). Re-export from the 2:34 master (cdn.shopify.com/videos/c/o/v/59e8423c235b4e71a38a64910b48faac.mp4) without the caption track, then re-cut at 600 px, 12 fps, under 1.5 MB (hero) and under 600 KB (inline).
- One-pass wipe GIF for K1: cut 3 seconds from Drive 1WCr_8xqsuY44n64f5_P1vh-n7yuJ-IDe (real-time wipe after salmon).
- Scratch-test GIF for B1: Drive 1nlzfCIswJnOr1IKIigkNAiB09T_oCn1T shows a named competitor; cut only the Siraat half or skip.
- Founder line to camera (optional for W2 as a still): nothing exists.

### Cut-out PNGs (transparent, for tiles)
- Stainless Steel Lid, Dishwasher Sheets pack, Pan Pro Standard, 6-Pcs set, Cookware Set Pro, 2 Pans + 2 Lids: only packshots on white exist, no transparent cut-outs. Needed for the three-tile rows in W4-US, W4-INT, P3, R1, R2. The Cutting Board V2 is the only clean cut-out (71161458065748).
- Light Labs certificate: render page 1 of brand/proof/light-labs-certificate-of-analysis-2025-10-30.pdf as a 600 px PNG for W3 and C2.

### Photos to shoot (no real photo exists)
- Unboxing / what's in the box (P1): pan, sheets pack, e-book card, apron or spatula on a table.
- Founder portrait (W2): confirm whether 73260580569428 (smiling man hugging a pan, about-us page) is the founder; otherwise shoot one.
- Old peeling nonstick pan from Siraat's own kitchen (B1, K2 comparison): the adv-chef-nonstick/stainless/castiron files (72615701414228, 72615701446996, 72615701479764) are advertorial material of unknown origin, verify before use.
- Drawer of dead pans (K2, replacement fatigue): nothing exists.
- Lid on the pan in use, in a kitchen (P3): only a studio packshot exists.
- Three Shopify files labelled Nano Banana, OpenArt or ChatGPT (70573346685268, 72196035510612, 73782159606100) are AI and were excluded from every hero slot.

### Missing reviews (no verified quote under 45 words)
- 12-Pcs set: none (W4-US tile has no proof).
- Lids: no 5-star quote (Joanna C. 4 stars only) and none about pots (P3).
- Durability beyond the first weeks: nothing at 6 or 12 months (B2 diary stops at week one; K2 must not imply long-term release).
- Induction and glass-top: Mrs J. and Adam T. only; no glass-top electric proof (W4-INT, P2).
- Australia, Canada, New Zealand: no usable quote about currency or shipping (W4-INT).
- Cool handle: Nina G. only, not a claim.
- 30-day returns: no customer proof; Jack (R414) praises the old 100-day policy, quote only next to the plain 30-day wording (K3).
- Named chef: none (the Michelin chef photos 59270929547604 and 59283084476756 name 'Allessandro D.' in alt text only; not used).

### Decisions still open (block copy, not assets)
- HI10 in flows (W1, W2, W5, R2) vs the $25 gift card (welcome-v3 decision 5; checkout research wants the 10% codes out).
- Founder name, reply-to inbox, footer address (W2).
- 12-Pcs lead time (W4-US, C4 variant).
- Which 6-Pcs listing and price to link: $399 active or $349 unlisted bday-sale (W4-US, R2).
- October campaign end date (C4 'final call', R2) and whether the Roasting Pan may be recommended (R1).
- Customer count 100K+ vs 30,000 (W1, W5) and Trustpilot score 3.7 shown or not (W5, C3).


## Photo usage (each hero id used once)

| hero id | title | source | used in |
|---|---|---|---|
| 63225744752980 | Preheating Pan Pro over gas flame (pre_heating_titanium_hammered_pan_pro.webp, 2048) | shopify-file | welcome W0 |
| 63501616283988 | Woman eating an egg from the pan (Lifestyle_image_egg.jpg, 2048) | shopify-file | welcome W1 |
| 70573756547412 | Hammered Pan Pro, pure titanium surface, studio (Regular_Hammered_Panttern_Pan_02, 3000) | shopify-file | welcome W3 |
| 69653576515924 | Three pans with vegetables on the stove (Photo_Three_Pans_with_Vegetables_on_Stove_Pro.jpg, 4037x2691) | shopify-file | welcome W4-US |
| 64589539115348 | Bundle of three hammered pans with fresh vegetables (bundle_set_hammered_pans.webp, 1080) | shopify-file | welcome W4-INT |
| 62816122601812 | Couple cooking dinner in Siraat aprons (Apron_Ember.webp, 2048) | shopify-file | welcome W5 |
| 70885778555220 | Single hammered pan with seafood on a gas range, lid lifted (P06-A_Stovetop, 1920x1280) | shopify-file | checkout C1 |
| 59266431975764 | Folding a vegetable omelet in a titanium pan (gempages d2a399da, 4608x3072) | shopify-file | checkout C2 |
| 61213082714452 | Flipping a crispy quesadilla with the titanium turner (A7406247_1, 2485) | shopify-file | checkout C3 |
| 64589616873812 | T-bone steak searing in a hammered pan on gas (steak_in_titanium_hammered_pan.webp, 1890) | shopify-file | checkout C4 |
| 71715411001684 | Wiping a Pan Pro Large clean with a cloth (9.webp, 1080) | shopify-file | cart K1 |
| 71326802510164 | Basting steak in a hammered pan on induction (sv2-pan-basting.webp, 1920x1280) | shopify-file | cart K2 |
| 69725067542868 | Woman eating a fried egg straight from the pan at the table (Lifestyle_image_egg_fbcf2a8f, 2048) | shopify-file | cart K3 |
| 63960186650964 | Close-up of the hammered titanium surface (Regular_Hammered_Panttern_Pan_05, 3000) | shopify-file | browse B1 |
| 62815908659540 | Home cook tasting dinner in the Azure apron (ApronAzureEating.webp, 2048) | shopify-file | browse B2 |
| 56801963344212 | Happy home cook holding the titanium turner and a frying pan (IMG_6175.jpg, 2316) | shopify-file | post-purchase P1 |
| 63507278004564 | Couple cooking a crepe in a titanium pan on gas (1.5.png, 2048) | shopify-file | post-purchase P2 |
| 58852686856532 | Titanium pan with lid going into a hot oven (10_8858e586, 1890) | shopify-file | post-purchase P3 |
| 72111681110356 | Roast chicken with vegetables in the Roasting Pan (hammeredroastingpan.webp, 1024) | shopify-file | winback R1 |
| 71326802477396 | Roast chicken in a hammered pan in the oven, rivets visible (sv2-oven-rivets.webp, 1920x1280) | shopify-file | winback R2 |

Second images (may repeat across flows, never inside one): 87886656536916 Pan Pro packshot (W1); certificate page 1 (W3, C2); 70885778358612 12-Pcs on the stove (W4-US); 85742472790356 Cookware Set Pro (W4-INT); 90331671953748 Dishwasher Sheets packshot (C4, P1); 72615701414228 scratched nonstick, verify (B1); still-water-test.jpg (P2, needs clean version); still-egg-in-pan.jpg (W0, needs clean version); 71161458065748 Cutting Board cut-out (P3); 92274752946516 2 Pans + 2 Lids packshot (R1); 89082455720276 6-Pcs packshot (R2); 73260580569428 about-us photo, verify founder (W2 optional).
