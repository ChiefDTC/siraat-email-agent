# Honest urgency in our flows: how to do it better than the current plan

For: Lucas (email specialist). From: lifecycle strategy, 8 Nov 2026. Klaviyo account TdtTzz.
Status: research and plan only. Nothing was changed in Klaviyo, Shopify, Ecomflow or the site. Klaviyo was read with GET calls only.

Read with: `../BRIEF.md`, `BRIEF-copy-per-flow.md`, `../black-hat/black-hat-referentie.md`, `../psychologie/koop-psychologie.md`, `../flows-ontwerp/flows-ontwerp.md`, `../scheduling/kalender.md`, `../segmentation/segmenten.md`, `research/voc/2026-11-synthese.md`.

House rules that apply to every line below: founder is Benjamin; 30-day returns (unused items); 75-year warranty; 100,000+ customers; 2 Pans + 2 Lids is $249 (not $199); BF code is always the placeholder BFCODE; header and footer from `klaviyo/templates/partials/`; yellow only on sale tags.

---

## 0. The short version

The current plan is right in direction (real deadlines, real counters, Benjamin letter last). What it misses is that three of its deadlines are not yet true in the backend, and that the best honest urgency we have after Nov 30 (Christmas delivery) is not in it at all.

**Top 5 improvements, ranked by expected impact**

| # | Improvement | Why it matters | Effort |
|---|---|---|---|
| 1 | **Make the existing "48 hours" codes actually expire, then remind on the real expiry.** C4, K3 and B2 codes are set to expire one year after creation (checked today in the Coupon Assigned events). Fix the expiry window, then add a reminder step triggered by Coupon Assigned that prints `CouponExpirationDate`. | Cart and checkout are $25k a week of flow revenue and their strongest subject lines ("Your own 10% ... for 48 hours", "we're removing your discount") are currently not true. Fixing it turns them from a legal risk into our best real deadline. | Small (coupon settings plus one flow step each) |
| 2 | **Christmas ship-by deadline (US) from Dec 1 to the cutoff, then an e-gift card fallback.** Ecomflow shows US delivery 6 to 13 days (p90, 90 days) plus about 3 days to fulfillment. A real "order by Dec {{SHIPBY_US}} for Dec 24" date carries urgency through December, when the BF deadline is gone. | Gift is 18.5% of the buying reason in Nov and Dec (VoC). It is the only true deadline left after Nov 30. | Medium (one block, one date per market, ops sign-off) |
| 3 | **Trigger-based real scarcity: a Low Inventory flow plus an upgraded Back in Stock flow.** Ecomflow shows real low runway today on Pan Pro Small (2.8 days), Standard (5.3), Large (2.4) and Mini (0 on hand). | Scarcity that the system detects is true by construction. Back in Stock is already our highest RPR flow ($21.69) on tiny volume. | Medium |
| 4 | **Date-switched blocks inside every flow: "ends tonight" only on Nov 30, "It ended" automatically from Dec 1.** One code block with a date condition, used in all BF flows, plus a fixed (not evergreen) countdown in the last-day versions only. | Flows keep sending after the sale; without the switch they would keep saying "Black Friday is live". The switch makes every deadline end on time without anyone touching templates on Dec 1. | Small |
| 5 | **Protect the gift promise and make it an honest scarcity line.** Mystery Gift stock in Ecomflow is 1,992 units at 257 a day (about 7.7 days). Every flow promises "5 free gifts with every order" until Nov 30. | If the gift runs out on Nov 16 the promise becomes false in 24 flows at once. If it is counted, "We packed N mystery gifts. When they're gone, orders ship without one" is true and strong. | Small (confirm total stock across all warehouses) |

Everything else (orders counter via web feed, Rise credit redeem, SMS, timing tests) is in sections 3 and 5.

---

## 1. What I checked in Klaviyo and the backends today (facts)

| Check | Result | What it means for us |
|---|---|---|
| Live flows by trigger type | 37 live flows. **None** use the Date Based, Low Inventory or Price Drop trigger (also none in draft). | Section 3 items 3 and 6 are net new. Date logic today only lives in delays (`delay_until_time`) and in time frames of filters. |
| Conditional splits in the urgency flows | Checkout QUBUQV: 3 splits (profile-sample 100%, Received Email in the last N). Cart TZG9Mx: 6 (sample, Added to Cart again, Received Email). Browse WdRz5k: 8 plus 1 A/B (sample 50/50 for the T02 code test). Welcome T4a5Mk: 4 (buyer splits, US vs INT). Winback UyFc78: 5 (2+ orders, Received Email, sample 50/50). Post-purchase X3ySuU: 3. Sunset TbYQmX, Site VLGhbR, BFCM Welcome Rn556d: none or a 100% sample. | The 50/50 `profile-sample` split already works through the API (PLAYBOOK 12, 30 Oct). We can use it for holdouts without new tooling. No split uses a date or inventory condition yet. |
| Purchase filters | Checkout, cart, browse: flow filter "Placed Order since flow start = 0" plus per-email filters on Placed Order. Welcome splits out buyers. Winback emails filter Placed Order. **Back in Stock WsQDYu has no filters at all**, Rn556d only "not in flow before". | Good base. Add the missing filters in section 2.7 before any urgency copy goes into BIS or Rn556d. |
| Smart Sending | **Off** on every email in checkout, cart, browse, site, welcome, winback, post-purchase and sunset. **On** only in YqKCmH (BF follow-up, test list). | Flows will never be suppressed by campaigns, but flows also suppress nothing. With 3 to 4 campaigns a day from Nov 27, low-intent flows need their own volume cap (section 2.6). |
| Coupon codes (Coupon Assigned, metric XUMYt7, since 25 Oct) | `K3_10_48H` 361 codes, `C4_10_48H` 127, `B2_10_48H` 12. **Every one expires one year after it was created** (codes assigned 8 Nov 2026 expire 7 or 8 Nov 2027). | The copy says 48 hours. The backend says one year. This is the first thing to fix (section 2.2). |
| Coupons API | `GET /api/coupons` returns nothing: Shopify dynamic coupons are not exposed there. | Read expiry from the Coupon Assigned event (`CouponExpirationDate`), not from the coupons API. |
| Catalog API | `GET /api/catalog-items` returns nothing: the endpoint only covers custom catalogs, not the Shopify sync. | Inventory is synced (the BIS flow works on it), but confirm the `inventory_quantity` field in a template preview (section 2.4). |
| Universal Content | 27 saved blocks, all legacy Homestead: "FREE SHIPPING \| 30,000 HAPPY CUSTOMERS \| 100-DAY TRIAL", "Life Warranty \| Free Shipping \| 100 Day-Trial", "30,000+ Customers" (3 versions). | These break DECISIONS (30-day, 75-year, 100,000+). Never drop them into a new email; archive after checking no live template uses them. Our v4 templates are code templates built from partials, so new "UC" blocks are partials in `partials/blocks/` (names in section 5.2). |
| Old arms in live flows | Still attached at 0% traffic: checkout "We Can't Keep these Forever", cart "Last Call for 10% Off!", welcome "Save 10% On a Lifetime of Use". | 0% since 19 Oct (T01 stopped), so no sends. Do not reactivate them as a rollback during BFCM: all three are fake-scarcity or banned-claim subjects. |
| Flow timing | Checkout C1 at 10 minutes, then next day 08:30, then +2 days 09:00. Cart K1 at 15 minutes, K2 +2 days 08:00. Browse B1 at 1 hour, B2 +2 days 09:00. | First touch is already fast. The timing gains are in the expiry reminder and the Nov 30 evening, not in the first email. |
| Ecomflow stock (8 Nov, 14:07 UTC) | 12 SKUs critical. Pan Pro Mini 0 on hand, Small 131 (2.8 days runway), Standard 485 (5.3 days), Large 198 (2.4 days), Mystery Gift 1,992 (7.7 days at 257 a day), Dishwasher Sheets 0, Stainless Steel Lid Small 58 and Large 88 (2 to 3 days). | Real low stock exists. Ecomflow may not be the only location (ShipBob also ships): Floris confirms total stock before any stock line goes live. |
| Ecomflow delivery, United States | Average 8.7 days (30 d), 9.4 (90 d); range 6 to 12 (30 d), 6 to 13 (90 d). Plus fulfillment: median 77 hours in October (DECISIONS 8 Oct). | Basis for a real Christmas cutoff (section 3, item 2). |

---

## 2. Klaviyo mechanics per format, with exact implementation

### 2.1 Date-based conditional blocks (show and hide)

Use one code block that compares the send moment with a fixed cutoff. In our code templates the tag `now` is on the allowlist (PLAYBOOK 12), so:

```django
{% now "YmdHi" as t %}
<!--{% if t >= "202612010500" %}-->
  {{BLOCK:ended}}            {# from Dec 1 05:00 UTC = Nov 30 11:59 PM ET + 1 min #}
<!--{% elif t >= "202611300500" %}-->
  {{BLOCK:deadline day="last"}}   {# Nov 30 00:00 ET until the end #}
<!--{% else %}-->
  {{BLOCK:deadline day="normal"}} {# "Black Friday ends Nov 30, 11:59 PM ET" #}
<!--{% endif %}-->
```

Rules:
- Compare fixed-length strings (`YmdHi`) so the string compare is also a time compare.
- Verify once which timezone `now` renders in (account timezone or UTC): seed send at a known minute, read the rendered value. Write cutoffs in UTC in the code and in ET in the copy.
- Subjects cannot carry this logic safely. For subjects use two flow emails behind a conditional split, or keep the subject date-neutral ("Black Friday ends Nov 30") and let the body switch. Never let a subject say "tonight" on a day when it is not.
- `qa_render.py` must render each branch: add sample events with fixed `now` overrides (Nov 20, Nov 30 20:00 ET, Dec 1 09:00 ET).

### 2.2 Unique coupon codes with a real expiry

Today: `{% coupon_code 'C4_10_48H' %}`, `'K3_10_48H'`, `'B2_10_48H'` render a fresh Shopify code per profile, but the coupon is set to the 1-year expiry option.

How Klaviyo's Shopify unique coupons work (Klaviyo help center, see sources):
- Expiry choices: a fixed date, a number of days or hours after the code is generated, or 1 year. The days or hours option is only available for flows, not campaigns.
- Klaviyo adds a 24-hour grace period to days or hours expiry. A "48 hours" code is valid for about 72 hours.
- Codes are generated in batches ahead of use, so the clock can start a few hours before the email (we saw codes assigned up to 10 hours after creation with the same expiry).
- Shopify shows the expiry in the store timezone.

Implementation:
1. Change C4, K3 and B2 coupons from "1 year" to "48 hours after generation" (Floris, in the Klaviyo coupon settings; also check in Shopify that the discount behind it has no other end date or usage rule that conflicts).
2. Copy in the email that issues the code: "Your own 10%, good for at least 2 days." That is always true (48 h plus 24 h grace minus batch time is at least 62 hours). Do not print a precise hour in the issuing email: Klaviyo cannot show the exact expiry of a code rendered in the same email.
3. Add the precise reminder as a small new flow per pool, triggered by **Coupon Assigned** (XUMYt7) with trigger filter `CouponKey = C4_10_48H` (and K3, B2). Klaviyo has no delay "until an event date minus N hours", so use a fixed wait of 40 hours and print the real time: `Your code {{ event.UniqueCode }} stops working {{ event.CouponExpirationDate|format_date_string|date:"l, M j \a\t g:i A" }}` (test the filter chain in preview; fallback: print the date only).
4. Filters on that reminder: Coupon Used with `CouponKey` equals this pool since flow start = 0, Placed Order since flow start = 0.
5. "We're removing your discount" is only allowed in an email that goes out before `CouponExpirationDate` and names that date.
6. During Nov 27 to 30, a fixed-date pool (one per region, ends Nov 30 23:59 local) is simpler than hours: then "ends tonight" is true for everyone on Nov 30 (`flows-ontwerp.md` 2.2).

### 2.3 Countdown timers in flows

| Type | How it works | Honest when | Use in our flows |
|---|---|---|---|
| Fixed end date (Sendtric fixed deadline, NiftyImages fixed timer) | One image URL counts down to one moment for everyone; after the moment it shows an expired image. | The moment equals the real backend end (Nov 30 23:59 ET sale end, or the fixed-date pool end). | Yes, only in the last-day branch of 2.1 (Nov 30). Expired image: "BLACK FRIDAY ENDED" in house style, no yellow except the sale tag. |
| Evergreen, open based | Starts counting when the recipient first opens (Sendtric "evergreen"; resets per recipient). | Practically never: it measures the reader, not the offer. A second device or a cleared cookie restarts it. | No. This is black-hat A1/A4. |
| Dynamic, end time passed in the URL | The end time is a merge tag in the image URL (vendors call it dynamic timers; check per vendor). | The tag is the real expiry, e.g. `{{ event.CouponExpirationDate }}` in the Coupon Assigned reminder flow. | Optional in the 2.2 reminder flow, after we verify the vendor reads a per-profile end time. |

Rules: a timer never appears without the same end time written in text next to it (images are blocked in many clients). Sendtric free tier is 10,000 views a month; flows at BFCM volume will pass that, so budget a paid plan or keep the timer only in the Nov 30 branch. A/B the timer against no timer inside the flow (section 5.3), because no independent study shows a reliable lift.

### 2.4 Catalog and inventory-based stock lines

Source: the Shopify catalog sync. Inventory is synced (Back in Stock runs on it), but our API cannot list the Shopify catalog, so confirm the field in a template preview:

```django
{% catalog event.extra.line_items.0.product.id integration='shopify' unpublished='cancel' %}
  {{ catalog_item }}   {# preview once to see the real field names #}
{% endcatalog %}
```

Then the stock line, only with a real, small number:

```django
{% catalog ITEM_ID integration='shopify' unpublished='cancel' %}
<!--{% if catalog_item.variant.inventory_quantity > 0 and catalog_item.variant.inventory_quantity <= 50 %}-->
  Fewer than {{ STOCK_ROUNDED }} left of the {{ catalog_item.title }} right now.
<!--{% endif %}-->
{% endcatalog %}
```

Rules: threshold 50 units or 3 days of runway, whichever is lower; never show a number above the real one; round down ("fewer than 100") is fine, round up is not. Do not show a stock line for products with `inventory_policy = continue` (oversell allowed): there the number does not limit anything. In cart and checkout, the product ID comes from the event (`Items`, `line_items`), so the line is about the reader's own product. Re-check before every BFCM week that Shopify inventory matches Ecomflow plus ShipBob.

### 2.5 "Bought this week" counters

Klaviyo cannot count orders into a template by itself, and the Shopify-synced catalog cannot be given custom fields through the API (custom metadata only works on a custom catalog). Best route:

1. A small daily job (Shopify `run-analytics-query` or the Admin API) writes a JSON file: `{"orders_since_nov1": 21400, "orders_7d": 6210, "as_of": "2026-11-20"}`. Host it on a stable HTTPS URL (Shopify Files or a static page).
2. Add it as a **Web Feed** in Klaviyo (Content, Web feeds) named `siraat_counter`, refresh daily, and attach it in the template's data feeds.
3. In the template: `{% if feeds.siraat_counter.orders_since_nov1 %}{{ feeds.siraat_counter.orders_since_nov1|floatformat:0 }} orders since Nov 1 (as of {{ feeds.siraat_counter.as_of }}){% endif %}`. If the feed fails, the block disappears.

Rules: always a denominator in time ("since Nov 1", "in the last 7 days"), always the "as of" date, numbers rounded down to the hundred. Never per product unless the job counts per product. Never "X people are viewing".

### 2.6 Smart Sending interplay

Klaviyo Smart Sending skips an email if the profile received an email in the window (default 16 hours), counting flows and campaigns together. Today it is off in all our main flows.

- Cart, checkout, the coupon reminder flows and the Nov 30 last-day emails: keep Smart Sending **off**. These are tied to a real personal event or deadline; a campaign at 08:15 must not swallow them.
- Browse, site, welcome W2 and later, failure to launch, sunset, winback: from Nov 20 to Nov 30 add a message filter instead of Smart Sending: `Received Email (YkRM4Q) in the last 1 day < 3` (the pattern from `kalender.md` section 4). Smart Sending would suppress too much on campaign days; the cap is more predictable.
- Campaigns keep Smart Sending off on deadline days, with the exclusions in `kalender.md`.

### 2.7 Filters so urgency never hits someone who already bought

Every urgency email gets these as **message-level filters** (re-checked at send, not only at entry):

| Filter | Klaviyo condition | Where |
|---|---|---|
| Not bought since the flow started | Placed Order (RSNxYV) since flow start = 0 | All flows with an offer (exists in checkout, cart, browse; add to BIS, Rn556d, low-inventory, price-drop, ship-by) |
| Not bought in the last 3 days | Placed Order in the last 3 days = 0 | Welcome, BF follow-up, sunset, winback (people who bought through another path) |
| Code not used | Coupon Used (USRsNP) with `CouponKey` equals the pool since flow start = 0 | Coupon reminder flows, last code email |
| Not in a higher-intent flow | Started Checkout (RfMvni) since flow start = 0 | Browse, site, welcome offer emails |
| Already owns it | `person.siraat_owned` does not contain the product key | Low inventory, price drop, BIS, post-purchase cross-sell |
| Holdout | `siraat_credit_cohort` not equals "holdout" | Credit and redeem flows |

### 2.8 Profile properties we can use

`siraat_owned` (nightly sync, exists), `siraat_goal` (quiz plan, after BFCM), `siraat_credit_balance` and `siraat_credit_expires` or the Rise fields `rise_wallet_balance` and `rise_wallet_next_expiration_date` (redeem flow, `flows-ontwerp.md` 2.1), `person.Country` and `location['country']` for market. New, proposed: `siraat_shipby_market` is not needed: the ship-by date is a lookup on market inside the block.

---

## 3. Better ideas we do not have yet, ranked by expected impact

Impact estimates are ours, based on our own data unless a source is named. Our anchor: real-deadline emails earn $0.165 to $0.171 per recipient against $0.03 to $0.13 without, and 62 to 74% of their orders come within 24 hours (own Klaviyo data, `koop-psychologie.md` 1.3).

| Rank | Idea | Mechanism in Klaviyo | Why it ranks here | Benchmark or evidence |
|---|---|---|---|---|
| 1 | **Real personal code deadlines plus exact-expiry reminders** | 2.2: coupon expiry 48 h, reminder flow on Coupon Assigned | Lives inside our two biggest-RPR flows (checkout $4.77, cart $2.75 per recipient; together about 7,350 recipients a week). Removes the largest current honesty gap. | Inman and McAlister 1994: second redemption peak just before a coupon's expiry. Shu and Gneezy 2010: short validity redeemed far more often than long (about 31% vs 6% in their field study). Own data: deadline emails 1.5 to 5 times the RPR. |
| 2 | **Christmas ship-by deadline, then e-gift card** | Block `{{BLOCK:shipby}}` with a date switch (2.1) and per-market dates; after the cutoff the block swaps to the E-Gift Card ($25 to $200, delivered digitally) | December has no sale deadline. A delivery date is real, personal to the market and matters to the 18.5% who buy as a gift. Also cuts "where is my gift" tickets (69% of gift tickets are about delivery). | VoC synthesis section 9; Ecomflow US delivery p90 13 days; carriers' own last-mile dates (USPS Ground Advantage Dec 17, FedEx Ground Dec 17) are later than ours, so our date is set by our own chain, not by them. |
| 3 | **Low Inventory flow (new) and Back in Stock upgrade** | Low Inventory trigger on the Shopify catalog, threshold in units; audience is people who viewed or carted the item; Klaviyo skips people who bought it. BIS WsQDYu: add filters and a BF price line. | Our stock is really low on three Pan Pro sizes now. Back in Stock already earns $21.69 per recipient. | Third-party Klaviyo benchmark summaries put Back in Stock at about $9 RPR and the highest conversion of common flows (eightx, see sources). Klaviyo: Low Inventory and Price Drop triggers need inventory synced; Price Drop does not send on 0 or negative stock. |
| 4 | **Date-switched "ends tonight" and automatic "It ended"** | 2.1 in every BF flow; "It ended" block from Dec 1 with what really stays (free shipping, 30-day returns on unused items, 75-year warranty) and the ship-by date | Prevents flows from lying on Dec 1 to 3, and gives one honest last-day push in every flow on Nov 30. | Own data: Oct 31 "ENDS TONIGHT" 74% of orders within 24 h. Black-hat A3: never extend; the honest after-mail keeps trust for the next sale. |
| 5 | **Mystery gift: counted, honest scarcity** | Web feed counter (2.5) with gifts left, or a plain line "while they last" if not counted | Protects the "5 free gifts" promise in 24 flows; if counted, adds a real scarcity line that also works in post-purchase ("yours is packed"). | Ecomflow: about 7.7 days of runway today. Worchel 1975: items that become scarce through demand are valued more. |
| 6 | **Price Drop flow, and "price goes back on date X" only when scheduled** | Price Drop trigger (needs price and inventory synced; product level, all variants must drop). After Nov 30 a block "On Dec 1 the price returns to {{PRICE:...}}" only if Floris has scheduled the change in Shopify. | Real by construction; reaches viewers who did not cart. Smaller audience than cart. | Klaviyo help center on Price Drop requirements. FTC 16 CFR 233: a "regular price" claim must be a price we really sold at. |
| 7 | **Real orders counter** | Web feed (2.5) in browse, site, welcome | Social proof that cannot be faked; replaces the "93% sold" bar idea. Moderate lift, mostly on cold readers. | Our own rule (PLAYBOOK 1): real numbers, no asterisk. FTC 16 CFR 465 bans fake social indicators. |
| 8 | **Rise credit redeem flow with real expiry** | `flows-ontwerp.md` 2.1 (C-L, C-X date trigger on `rise_wallet_next_expiration_date`), 10% holdout | Strong (endowment and mental accounting) but depends on Rise going live. Unique $12 code is the fallback; it must use 2.2 expiry, not 1 year. | Helion and Gilovich 2014 (gift cards spent more freely); Shu and Gneezy 2010. |
| 9 | **Abandoned-checkout timing: the evening of Nov 30** | One extra checkout and cart step on Nov 30 only: "Started Checkout in the last 3 days, no order" at 20:00 local via a date-conditioned branch | First touch is already 10 to 15 minutes, so the gain is not there. The gain is the last evening, when 2025's Cyber week peaked at 20:00 to 22:00 (Adobe). | Klaviyo abandoned cart benchmark: average RPR $3.65, top 10% $28.89 (2024 report). Our C1 is already $7.96 to $10.21. |
| 10 | **SMS layer** | Klaviyo SMS for checkout (1 message, +1 h) and the last-day reminder only | High open rates, but needs consent capture (TCPA), number registration and quiet hours; not realistic before Nov 30. Plan for January. | Vendor ranges only (SMS click 19 to 36%, Omnisend abandoned cart SMS $3 to $11 per message); treat as indicative. |
| 11 | **Post-BFCM honesty sequence** | "It ended" (rank 4) plus, in December, a different real reason (ship-by, then gift card, then New Year on Jan 1 to 3) | Keeps December revenue without fake extensions. Fresh-start effect: day 1 to 7 of the month index 108 to 109, January strongest month outside Q4. | `koop-psychologie.md` 1.1 and kaart 17. |

---

## 4. Guardrails: one concrete rule per format

| Format | Rule (must be true before send) | Legal or trust basis |
|---|---|---|
| Deadline text ("ends tonight", "last day") | Only in the date branch where it is true (2.1). One end per mechanism. Never extend after "it ends". Time zone always written ("11:59 PM ET"). | FTC Act section 5 and the FTC dark patterns report (fake deadlines); EU UCPD Annex I point 7; CMA v Emma Sleep. |
| Unique code expiry | The coupon's backend expiry is at or after every time stated in copy. "Good for at least 2 days" in the issuing email; exact time only from `CouponExpirationDate`. | Same; also our own C4/K3/B2 finding. |
| Countdown GIF | Fixed end time equal to the backend end, or a per-profile end time passed in the URL from the event. Never open-based evergreen. Text time next to it. | FTC dark patterns report; Mathur et al. 2019 (157 of 393 timers deceptive). |
| Stock line | Only from live Shopify inventory, at or below 50 units, never rounded up, never on oversell-allowed products. Never "next batch", "reserve", "coming" (DECISIONS 1 Nov). | UCPD Annex I point 7; FTC; CMA (Booking, Emma). |
| Orders counter | From a dated feed, with time denominator and "as of" date; hidden if empty. | FTC 16 CFR 465 (fake social proof indicators). |
| Reviews next to urgency | Verbatim Trustpilot quotes only (PLAYBOOK 12); never a review count or average until the site numbers are fixed (VoC 4.2). Do not add urgency to the review request flow. The current star routing (4 to 5 stars to Trustpilot, 1 to 3 to our own page) is review gating: fix before scaling review asks. | FTC 16 CFR 465 (suppressing negative reviews); Trustpilot guidelines. |
| Subject lines | The subject describes what is in the email and the offer that really applies. No "Re:", "Fwd:", "(1)", "Your order is pending", no fake personal status. "Tonight" only on the night. Preview repeats the real number and deadline. | CAN-SPAM 15 USC 7704(a)(2); FTC v Jumpstart. |
| Returns line next to a deadline | "30-day returns on unused items" (not "30-day returns" alone) in the friction reducer and footer. This touches the footer partial plus the FRICTION macro, which reach all 106 source templates in one rebuild. Never "risk-free", "hassle-free", "free returns". | Refund policy: used items not returnable, sticking is not a defect (VoC 4.1); FTC guides on satisfaction guarantees (16 CFR 239). |
| Product claims in urgency heroes | Never "eggs slide" or "nothing sticks" as an unconditional promise. Use "Eggs slide. With heat." or the 3-minute rule. Our FAQ says "low-stick, not zero-stick". | VoC 4.3; sticking is the top complaint and top return reason. |
| Price anchor ($664 for 2 Pans + 2 Lids) | Show $664 only if Floris confirms with Shopify price history that the bundle was openly offered at $664 for a substantial recent period. Otherwise anchor on the sum of today's single prices ("Bought separately: $X") or no anchor. Confirmed anchors today: Pan Pro Standard $439, 12-piece set $1,186, Roasting Pan $250 (PLAYBOOK 12). EU and UK: percentage off against the lowest price of the last 30 days. | FTC 16 CFR 233.1 (former price comparisons); EU Omnibus Article 6a; HvJ Aldi Sued 2024. |
| Gift promise | "5 free gifts with every order" only while gift stock covers forecast orders to Nov 30; otherwise add "while they last" now. | FTC section 5 (representation that becomes false). |
| Price references in older briefs | `BRIEF-copy-per-flow.md` still has "2 Pans + 2 Lids $199" in a preview: replace with $249 before reuse. | DECISIONS 8 Nov. |

---

## 5. Implementation plan for Lucas

### 5.1 Per flow

| Flow (ID) | Urgency blocks (partials) | Data source | Test design | When |
|---|---|---|---|---|
| Checkout QUBUQV | C1: `deadline` (date switch), `stock` (own product, if low), `counter`. C4: code issue "good for at least 2 days". New reminder flow on Coupon Assigned `C4_10_48H` with exact expiry. Nov 30: last-day branch with fixed `countdown`, then `ended` from Dec 1. Benjamin letter stays last. | Event (line items), Shopify catalog inventory, Coupon Assigned `CouponExpirationDate`, web feed | A/B inside the flow on C1: fixed countdown on Nov 30 branch vs text only (unique clicks, placed order rate). 10% holdout on the reminder step (profile-sample split) to measure its increment. | Before BFCM: coupon expiry fix, reminder flow, filters. Nov 30: last-day branch. Dec 1: `ended` plus `shipby`. |
| Cart TZG9Mx | K1: `deadline`, `stock`. K3: code issue. Reminder flow on `K3_10_48H`. Nov 30 branch, `ended`. | Same as checkout (Added to Cart `Items`) | Same structure as checkout; cart has double the volume, so test the countdown here first. | Same order as checkout. |
| Browse WdRz5k (and QNZyEb, merge planned) | B1: `counter` plus 2 verbatim reviews. B2: code issue, reminder flow on `B2_10_48H`. `stock` only on the viewed product. | Viewed Product event, feed, catalog | Keep the running 50/50 code test (T02); do not add a second test. | Before BFCM: filters and reminder. |
| Site VLGhbR | `counter`, `deadline`. No code. | Feed | None (small volume). | Before BFCM. |
| Welcome T4a5Mk | W1: subject with real numbers ("5 free gifts", "up to 70% off"), `deadline` with date switch, `counter`. Last welcome email: "Last welcome email" is true; `ended` from Dec 1, then `shipby`. | Date switch, feed | A/B subject on W1 only (number subject vs current), winner on placed order rate, no automatic winner. | Before BFCM (W1 first; W1 is about 73% of welcome revenue). |
| BFCM Welcome Rn556d | `deadline` with date switch, `counter`. Add filter Placed Order in last 3 days = 0. | Date switch, feed | None; one email. | Before BFCM. |
| BF follow-up YqKCmH | Same as Rn556d; move from test list to main list only with the date switch in place. Smart Sending stays on here. | Date switch | None. | Before Nov 20. |
| Redeem (new, Rise or unique $12 code) | `codeexp` with real expiry, Benjamin letter as last step, 10% holdout. | Rise profile fields or Coupon Assigned | Holdout 10% for incrementality. | Only when Rise test passes; else post-BFCM. |
| Winback UyFc78 | Code with 2.2 expiry (not 1 year), `deadline` in December replaced by `shipby`. | Coupon Assigned | Keep current 50/50 code test. | Coupon fix before BFCM; `shipby` Dec 1. |
| Sunset TbYQmX | Benjamin letter, "before we stop emailing" (true: the flow suppresses after). No sale deadline in the subject; the real deadline is the unsubscribe-by-silence date. Filter Placed Order in last 120 days = 0. | Flow logic | None. | Before BFCM. |
| Post-purchase X3ySuU | Light $12 next-order code with 2.2 expiry, only after delivery education. No deadline in P1. Gift-packed line if the mystery gift is counted. | Coupon Assigned, feed | None during BFCM. | After BFCM (education first, VoC action 4). |
| Back in Stock WsQDYu | Add filters (Placed Order with that product since flow start = 0). Add BF price line in the date switch, then `ended`. | Shopify catalog | None (50 a week). | Before BFCM. |
| Low Inventory (new) | One email: product, real units (`stock`), BF price, no code. | Low Inventory trigger, Shopify catalog | None; measure RPR vs BIS. | Build before Nov 20 if Floris confirms stock numbers; draft otherwise. |
| Price Drop (new) | One email: old and new price only if both are real, `deadline` switch. | Price Drop trigger | None. | Post-BFCM, when prices change on schedule. |
| Ship-by (block in all flows, Dec 1 to cutoff) | `shipby` per market; after cutoff swaps to e-gift card. | Per-market date confirmed by ops | A/B in cart: `shipby` vs none, Dec 1 to cutoff. | Dec 1. |

### 5.2 Block names

Our templates are code templates built with `scripts/build_template.py`, so the reusable blocks are partials. Names below; if you build a hybrid or drag-and-drop email, create a Universal Content block with the name in the right column.

| Partial | Universal Content name | Content |
|---|---|---|
| `{{BLOCK:deadline}}` | `URG · Deadline · BF end (date switch)` | Normal: "Black Friday ends Nov 30, 11:59 PM ET." Last day: "Ends tonight, 11:59 PM ET." |
| `{{BLOCK:countdown}}` | `URG · Countdown · fixed Nov 30 23:59 ET` | Fixed timer image plus the same time in text. Last-day branch only. |
| `{{BLOCK:ended}}` | `URG · It ended · auto from Dec 1` | "Black Friday ended. Free shipping, 30-day returns on unused items and the 75-year warranty stay." |
| `{{BLOCK:codeexp}}` | `URG · Code expiry · from event` | "Your code {{ event.UniqueCode }} stops working {{ expiry }}." Reminder flows only. |
| `{{BLOCK:stock}}` | `URG · Stock · Shopify catalog` | Catalog lookup line, threshold rules in 2.4. |
| `{{BLOCK:counter}}` | `URG · Orders counter · web feed` | Feed line with "as of" date. |
| `{{BLOCK:shipby}}` | `URG · Ship-by Christmas · per market` | "Order by {{SHIPBY}} to have it by Dec 24 (standard shipping)." After the date: e-gift card line. |
| `{{BLOCK:anchor}}` | `URG · Price anchor · confirmed only` | Confirmed compare-at or "Bought separately" sum. |

Do not use the legacy UC blocks listed in section 1.

### 5.3 Test design

- One variable per test, winner on unique clicks and placed order rate, never opens (PLAYBOOK 6). No automatic winner.
- Volume reality: checkout about 2,400 recipients a week and cart about 4,950. From Nov 9 to Nov 30 that is about 7,000 and 15,000 recipients per flow, so a 50/50 test can only detect large differences (roughly a 25% or bigger change in placed order rate). Run at most one urgency test per flow during BFCM: the countdown test in cart, the W1 subject test in welcome.
- Holdouts: 10% `profile-sample` split before the coupon reminder step and in the redeem flow. That is the only way to know whether the reminder adds orders or only moves them earlier.
- After the deadline, check that sales really drop (Dec 1 vs Nov 30 in the same flows). If they do not drop, nobody believed the deadline (`koop-psychologie.md` kaart 3).
- Guardrails per arm from 1,000 delivered: unsubscribe above 0.5% is a signal, above 1% stop; spam above 0.1% stop.

### 5.4 Order of work

**Before BFCM (Nov 9 to Nov 25)**
1. Floris: coupon expiry on C4, K3, B2 from 1 year to 48 hours (or a fixed-date pool ending Nov 30 23:59 for BFCM). Until then, change the subjects that say "48 hours" to "Your own 10%, on top of the sale".
2. Floris: total stock for Mystery Gift and the three Pan Pro sizes across Ecomflow and ShipBob. If the gift will not last to Nov 30, add "while they last" in the gifts block today.
3. Lucas: message filters from 2.7 on every urgency email; filters on BIS WsQDYu and Rn556d.
4. Lucas: `deadline` and `ended` date switch in checkout, cart, browse, site, welcome, Rn556d, YqKCmH, winback, BIS. Render all three branches in `qa_render.py`.
5. Lucas: coupon reminder flows (C4, K3, B2) on Coupon Assigned, draft, then live after a seed test shows a real expiry.
6. Lucas: web feed counter and `counter` block.
7. Lucas: Low Inventory flow in draft; live only after Floris confirms the stock numbers.
8. Floris: decide $664 (evidence or no anchor) and "30-day returns on unused items" (one partial change plus rebuild).
9. Received Email cap on low-intent flows from Nov 20.

**During BFCM (Nov 26 to Nov 30)**
- No new builds. Nov 30: last-day branches with fixed countdown fire by date; evening checkout and cart step at 20:00 local. Watch spam and unsubscribe per send.

**After BFCM (Dec 1 to Dec 24)**
- Dec 1: `ended` shows automatically; `shipby` block live in all flows with Floris's per-market dates (suggested starting point for the US: order by about Dec 8, from 3 days to fulfillment plus 13 days p90 delivery plus a 1 to 2 day peak buffer; INT earlier).
- After the cutoff: e-gift card line replaces `shipby`.
- Price Drop flow if prices change on a schedule.
- Post-purchase light $12 code (2.2 expiry), after education.

**January**
- SMS layer (consent, registration, checkout plus last-day only), Rise redeem with holdout, quiz-popup test, 14 vs 30-day code windows.

---

## 6. Summary table per flow

| Flow | Current plan | Add or change | Data source | Honest because | Priority |
|---|---|---|---|---|---|
| Checkout QUBUQV | Checkout open, expiring code, stock, social proof, countdown last day, auto "It ended", Benjamin last | Fix 1-year code expiry; Coupon Assigned reminder with exact time; date switch; Nov 30 20:00 step; `shipby` in December | Event, catalog, Coupon Assigned, feed | Every time in copy comes from the backend | 1 |
| Cart TZG9Mx | Stock, social proof, countdown | Same as checkout; countdown A/B here | Same | Same | 1 |
| Browse WdRz5k / QNZyEb | Bought-this-week counter, reviews | Counter via web feed with "as of"; B2 code expiry fix plus reminder | Feed, Coupon Assigned | Dated counter, real expiry | 2 |
| Site VLGhbR | Counter, reviews | Date switch | Feed | Dated counter | 3 |
| Welcome T4a5Mk | Number subjects, countdown with date condition, order counter | W1 subject test; `ended` then `shipby` from Dec 1 | Date switch, feed | Switch ends it on time | 2 |
| BFCM Welcome Rn556d | Same as welcome | Add "no order in 3 days" filter | Date switch | Same | 2 |
| BF follow-up YqKCmH | Same as welcome | Only to main list once the switch is in | Date switch | Same | 2 |
| Redeem (new) | Unique $12 code, real expiry | Use 2.2 expiry (not 1 year), 10% holdout | Rise or Coupon Assigned | Real balance or real code | 3 |
| Winback UyFc78 | Expiring code | Fix code expiry; `shipby` in December | Coupon Assigned | Real expiry | 3 |
| Sunset TbYQmX | Benjamin letter, "before we stop emailing" | Keep; no sale deadline in subject; filter recent buyers | Flow logic | We do stop emailing | 3 |
| Post-purchase X3ySuU | Light $12 next order | After education; 2.2 expiry; gift-packed line if counted | Coupon Assigned | Real expiry | 4 |
| Back in Stock WsQDYu | Not in plan | Filters, BF price switch | Catalog | Restock is a real event | 2 |
| Low Inventory (new) | Not in plan | New one-email flow | Low Inventory trigger | System-detected stock | 2 |
| Price Drop (new) | Not in plan | New, post-BFCM | Price Drop trigger | System-detected price | 4 |
| All flows | Price anchor | Only confirmed compare-at or sum of parts; $249 for 2 Pans + 2 Lids | Shopify, DECISIONS | Former price really charged | 1 |

---

## 7. Open questions for Floris

1. Coupon expiry C4, K3, B2: 48 hours after generation, or a fixed-date pool for Nov 27 to 30? Who changes it, and when?
2. Total stock (Ecomflow plus ShipBob) for Mystery Gift and Pan Pro Mini, Small, Standard, Large. Is Shopify inventory the same number Klaviyo sees?
3. Is $664 a price the 2 Pans + 2 Lids was really sold at? If not, no $664 anywhere.
4. Christmas cutoff per market (US first). Gift receipt or no prices on the packing slip possible?
5. Do prices change on a schedule on Dec 1 (needed for "price goes back on date X" and the Price Drop flow)?
6. "30-day returns on unused items" in footer and friction reducer: yes?
7. Budget for a countdown vendor at flow volume (Sendtric free tier is 10,000 views a month).

---

## 8. Sources

External (searched 8 Nov 2026; help.klaviyo.com could not be opened directly from this session, so Klaviyo help center content comes from search summaries of these pages):
- Klaviyo help center, Unique coupon codes for Shopify (expiry options, 24-hour grace, flows only for variable expiry): https://help.klaviyo.com/hc/en-us/articles/115006155388 ; community thread on flow coupon expiry: https://community.klaviyo.com/marketing-30/expiration-date-of-unique-coupon-code-in-a-flow-setting-5567
- Klaviyo help center, How to create a low inventory flow: https://help.klaviyo.com/hc/en-us/articles/21374913673243 ; Klaviyo blog, low inventory flows: https://www.klaviyo.com/blog/low-inventory-flows
- Klaviyo help center, How to create a price drop flow: https://help.klaviyo.com/hc/en-us/articles/4404249033755
- Klaviyo help center, Catalog lookup: https://help.klaviyo.com/hc/en-us/articles/360004785571 ; show and hide blocks: https://help.klaviyo.com/hc/en-us/articles/115005258208 ; developer docs, message design: https://developers.klaviyo.com/en/docs/django_message_design
- Klaviyo abandoned cart benchmarks (average RPR $3.65, top 10% $28.89): https://www.klaviyo.com/blog/abandoned-cart-benchmarks ; Klaviyo 2024 benchmark report: https://resources.klaviyo.com/2024-benchmark-report
- Back in Stock RPR third-party summary (indicative only): https://eightx.co/blog/average-klaviyo-flow-revenue-contribution-benchmarks
- Countdown types: Sendtric https://sendtric.com ; CountdownMail on fixed vs evergreen vs dynamic: https://countdownmail.com/blog/fixed-vs-evergreen-vs-dynamic-timers
- SMS ranges (vendor data, indicative): https://www.clickminded.com/sms-marketing-benchmarks/ ; Klaviyo SMS benchmarks: https://www.klaviyo.com/uk/marketing-resources/sms-benchmarks-by-industry
- 2026 carrier holiday deadlines: ShipStation https://www.shipstation.com/blog/us-2026-holiday-shipping-deadlines-for-ups-usps-and-fedex.md ; CBS https://www.cbsnews.com/chicago/news/2026-holiday-shipping-deadlines-usps-fedex-ups
- Legal: FTC dark patterns report, FTC 16 CFR 465 (reviews), CAN-SPAM 15 USC 7704, EU UCPD Annex I, Omnibus Article 6a, CMA cases: all with links in `../black-hat/black-hat-referentie.md` section 5. FTC Guides Against Deceptive Pricing, 16 CFR 233: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-233
- Research: Inman and McAlister 1994; Shu and Gneezy 2010; Helion and Gilovich 2014; Worchel, Lee and Adewole 1975; Mathur et al. 2019. Details and links in `../psychologie/koop-psychologie.md` section 7.

Internal (read only, 8 Nov 2026): Klaviyo GET on flows QUBUQV, TZG9Mx, WdRz5k, VLGhbR, T4a5Mk, Rn556d, YqKCmH, UyFc78, TbYQmX, X3ySuU, WsQDYu (definitions, splits, filters, delays, Smart Sending); flows by trigger type; Coupon Assigned events since 25 Oct (CouponKey, CouponExpirationDate); coupons and catalog endpoints; Universal Content list. Ecomflow stock health and United States shipping times (8 Nov). Repo: DECISIONS, PLAYBOOK, `content/facts/facts.csv`, `content/catalog/products.json`, VoC synthesis, sprint folders.
