# Siraat's Kitchen · Flow System v4 · Review brief for Homestead

Version 7 October 2026. Status: fully specified, all emails designed and built as templates. **Nothing is live in Klaviyo yet.** Designs: Figma v4, https://www.figma.com/design/ahGP2wWoVIif8ETXcBq1Dj (one page per flow, every email with subject A/B and preview text).

---

## 1. Why we rebuilt

**Baseline (last 90 days, 9 Jul to 6 Oct 2026, Klaviyo attribution):** flows earned $416,090, **10.8% of total revenue** ($3.87M). All email together: 18.7%.

| Flow | Siraat RPR now | Klaviyo average | Klaviyo top 10% |
| --- | --- | --- | --- |
| Welcome | $0.70 | $2.65 | $21.18 |
| Checkout abandonment | $2.36 | $3.65 (cart benchmark) | $28.89 |
| Cart abandonment | $1.47 | $3.65 | $28.89 |
| Browse abandonment | $0.97 | $0.95 to $1.07 | $7.05 |
| Post-purchase | $0.31 | $0.38 | $5.27 |
| Winback | $0.20 | n/a | n/a |

Checkout recovery: 0.97% of all checkout starters. Our target is the Klaviyo average, not the top 10% (high AOV, giveaway-driven list). Base scenario: flows from 10.8% to about 17% of revenue.

**The biggest issues we found in the current flows**

| # | Issue | Evidence |
| --- | --- | --- |
| 1 | Cart block showed free gifts instead of the product | In 40 of 100 real checkouts the paid product fell outside the three items shown; $0 gift lines came first. 47% of Added to Cart events are auto-added gifts. |
| 2 | No tailoring by product category | Apron, board, pot, deep pan and pizza steel buyers all got pan emails (15% of checkouts, 9.5% of orders have no pan). |
| 3 | Offer and cart at the bottom | Offer missing from the hero in 27 of 31 emails; cart block 1 to 2.5 screens down (C2: at 2,800 of 3,919 px). |
| 4 | Timing not based on data | Welcome split at minute zero sent buyers into the prospect path; "now your pan is here" emails sent before delivery (median 11.7 days); welcome plus failure-to-launch meant 18 emails. |
| 5 | Overlap between flows | Two triggers per abandonment flow (Shopify and Triple Pixel); welcome and browse overlap raised unsubscribes (7.24% vs 5.14%). |

---

## 2. The system at a glance

| # | Flow | Trigger | Goal | Emails per person (variants) | Key splits | Runtime | Replaces |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Checkout abandonment | Checkout Started, value > 0 | Recover checkout | 4 (10) | Category, existing customer, cart value/set, country, code router | 7 days | Both checkout flows |
| 2 | Cart abandonment | Added to Cart (gifts excluded) | Recover cart | 3 (6) | Category, existing customer, code router | 5 days | Both cart flows |
| 3 | Browse abandonment | Viewed Product (Klaviyo onsite) | Turn a view into a cart | 2 (5) | Category, clicked B1, code router | 3 days | Both browse flows |
| 4 | Welcome | Added to pop-up list | First order | 5 (8) | Bought since start, ever bought, T04, country | 14 days | Welcome + Failure to launch |
| 5 | Post-purchase | Placed Order | Use, trust, second order | 3 (13) | First/repeat, cookware, delivery known, category router, code router | 20 days | Post-purchase |
| 5b | Post-purchase · delivery (helper) | Delivered Shipment | First-egg email on delivery | 1 | none | 1 day | |
| 6 | Winback | Placed Order, then wait | Second order | 2 (7) | Category, VIP, code router | 90 days | Winback 60d |
| 7 | Site abandonment (new) | Active on Site | Catch visits without a product view | 2 | none | 2 days | |
| 8 | Sunset (new) | Segment "unengaged 120d" | Re-permission or suppress | 2 | Engaged since start | 8 days | Old sunset |
| 9 | VIP (new) | Placed Order, 2nd order | Third order, loyalty | 2 (3) | Code router | 40 days | |
| 10 | Anniversary (new) | First order with cookware | Service at 6 months, offer at 12 | 2 (3) | Code router | 365 days | |
| 11 | UGC first egg (new) | Delivered Shipment, 1st order | Customer photos | 1 | none | delivery + 4 days | |
| | Review request | unchanged, live | | | | | |

---

## 3. Flow by flow

Notation: TS = trigger split, CS = conditional split. "Until 09:00" = Klaviyo delay "X days, until 09:00" in the profile's time zone. Every sales email has a send filter "Placed Order zero times since starting this flow". Category lists: **COOKWARE** = exact product titles of all pans, pots, pizza steel, roasting pan and bundles; **SET** = exact set titles; **COOK WORDS** (substring OR on product name) = Hammer, Pan, Pot, ookware, Everything, fanne, Prep Bundle. Code = see the code router in section 4.

### 3.1 Checkout abandonment
Filters: no order since start, not in this flow for 14 days, no post-purchase email in 7 days. Re-entry 14 days.

| Step | Wait (why) | Split / router (exact condition) | Email | Subject A | Code |
| --- | --- | --- | --- | --- | --- |
| 0 | none | CS random sample 50%: v4 path or best old path (T01) | | | |
| 1 | 30 min (14.3% buy on their own within 15 min, only +2.5 pp by 30 min) | none | c1 | Something stop you at checkout? | HI10 shown |
| 2 | none | TS `Items` contains any of COOKWARE + SET | yes: cookware path, no: accessory path | | |
| 3 | 1 day, no time (77% of C1's effect lands within 24 h) | CS Placed Order at least once ever: yes skip, no send | c2 / c2-acc (accessory) | Has the pan in your cart actually been tested? / Yours, or a gift? Both work. | HI10 |
| 4 | 2 days until 09:00, day 3 (recovery 8.7% at 24 h, 10.6% at day 3) | TS `Items` any of SET, else `$value` >= 300: c3-s. Else Pan Pro titles AND `$value` < 250: c3-p. Else none. Accessory path: existing customer skip, else c3-acc | c3-s / c3-p / c3-acc | $70 in gifts ship with your set / One pan, or three for $349? / Most kitchens start with the pan | HI10 |
| 5 | 2 days until 09:00, day 5 (day 3 to 7 still +1.7 pp; a 48 h code fits that window) | CS Country = US; else TS Customer Locale = en-US and no country; else INT | | | |
| 6 | none | Code router, pool C4_10_48H | c4-us / c4-int (or -nocode) | 10% off your cart, for 48 hours / Last reminder: your cart and 4 gifts | unique 10%, 48 h |

Exit day 7 (after that, under 0.3% chance per day).

### 3.2 Cart abandonment
Trigger filters: Price > 0; product name excludes Mystery Gift, E-Book, Free Shipping, Giveaway. Filters: no Checkout Started or order since start, no checkout email in 7 days, not in flow 14 days.

| Step | Wait (why) | Split / router | Email | Subject A | Code |
| --- | --- | --- | --- | --- | --- |
| 0 | none | T01 50% | | | |
| 1 | 30 min (only +1.0 pp buy on their own between 30 and 60 min; old 15-min arm $2.90 vs $2.27) | CS Added to Cart where Product Name contains COOK WORDS, last 1 day | k1 / k1-acc | One pass with a damp cloth. / Picked it out? It's still here. | HI10 |
| 2 | 1 day (cart orders come slower, median 9.5 h) | CS Placed Order at least once ever (cookware path only) | k2-returning / k2-new | Adding to your Siraat kitchen? / The pan you keep replacing is the expensive one | HI10 |
| 3 | 2 days until 09:00, day 3 (recovery 5.8% at 24 h, 7.2% at day 3); accessory path waits 3 days, no K2 | Code router, pool K3_10_48H | k3 (or -nocode) | Your own 10% code, for 48 hours / What if it's not for you? | unique 10%, 48 h |

End day 5. No value split in cart (carts >= $300 do not recover better).

### 3.3 Browse abandonment
Filters: no Added to Cart, Checkout Started or order since start; no cart, checkout or welcome email in 7 days; not in flow 7 days.

| Step | Wait (why) | Split / router | Email | Subject A | Code |
| --- | --- | --- | --- | --- | --- |
| 0 | none | T01 50% | | | |
| 1 | 1 hour (after 15 min only 1.9% buy within the hour; cart and checkout fire first) | TS Viewed Product `Name` contains COOK WORDS | b1 (T05a) / b1-acc | Lab-tested: nothing on this pan to scratch off / Looked twice? Here's the detail. | HI10 |
| 2 | 2 days until 09:00 (78% of orders after a browse email land within 48 h) | CS Clicked Email where message = B1 (or B1-acc) since start. Yes: code router, pool B2_10_48H. No: b2-notclicked (accessory path: end) | b2-clicked (or -nocode) / b2-notclicked | Your own 10%, for the next 48 hours / Week one, in their words | unique 10%, 48 h |

End day 3.

### 3.4 Welcome
Trigger: added to the pop-up list (Alia giveaway). Never re-enter. Every W email is **skipped** (not ended) if there is an order since start or a checkout or cart email in the last day.

| Step | Wait (why) | Split / router | Email | Subject A | Code |
| --- | --- | --- | --- | --- | --- |
| 0 | none | T01 50% (old path keeps failure-to-launch until 20 Nov) | | | |
| 1 | 20 min (20.3% buy within 10 min of signing up) | CS Placed Order since start: yes end (post-purchase takes over) | | | |
| 2 | none | CS Placed Order at least once ever: yes w0, then end | w0 | Thank you. Now the first egg. | none |
| 3 | none (1.3% still buy on day 0 after the first hour) | A/B T04 50/50, no auto winner | w1-a (code block) / w1-b (gift card) | The pan with nothing on it (and your 10%) | HI10 |
| 4 | 1 day until 09:00 (first-order chance 0.50% on day 1) | | w2 (plain text, Benjamin) | The pan nobody else was making | HI10 in P.S. |
| 5 | 2 days until 09:00, day 3 (0.24%) | | w3 | Has your cookware actually been tested? | HI10 |
| 6 | 3 days until 09:00, day 6 (0.13%) | CS Country = US | w4-us / w4-int | Who are you cooking for? | HI10 |
| 7 | 4 days until 09:00, day 10 (0.09%; old day-10 last call earned $0.26 per recipient) | | w5 | Tammy is on her fourth pan | HI10 |

End day 14, then campaigns (new subscribers get no campaigns for 14 days).

### 3.5 Post-purchase (plus 5b delivery helper)
Filter: not in flow for 30 days. No T01 (before/after against the same weeks last period).

| Step | Wait (why) | Split / router | Email | Subject A | Code |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 hour (confirmation; 72 to 78% of clicks go to care and use) | CS Placed Order = 1 ever | p1-first / p1-repeat | Good call. Here's what's coming. / Good to see you again | none |
| 2 | 16 days until 09:00 (delivery median 11.7 days, p75 14.7; only 36% get a Delivered Shipment event) | TS `Items` any of COOKWARE + SET, no: skip. Yes: CS Delivered Shipment since start: yes skip (5b sent it), no p2-safe | p2-safe | When your pan arrives: the first egg | none |
| 3 | 4 days until 09:00, day 20 (about delivery + 8 at median; 12.4% of repeat orders land in days 14 to 21) | CS Placed Order = 2 ever: end (VIP takes over). Cookware: SET or `$value` >= 300 → p3-set; lid titles → p3-next; Pan Pro or shape pans → p3-pan; else p3-accessory. Non-cookware: e-gift card → end; owns cookware → p3-next; apron → p3-apron; else p3-accessory. Each via code router | p3-set / p3-next / p3-pan / p3-apron / p3-accessory | The pan your set is missing / What goes next to your pan / Which lid fits your pan? / An apron deserves a pan / Now meet the pan | unique 10%, 14 days |
| 4 | delivery + 14 | existing review flow, unchanged | review | | |
| 5b | trigger Delivered Shipment, 1 day until 09:00 ("now your pan is here" must wait for delivery) | Filters: cookware order in last 30 days, no p2-safe in 30 days, no refund | p2 | If you can do an egg, you can do anything | none |

### 3.6 Winback
Trigger Placed Order, then wait. No re-entry limit: every new order restarts the clock, the old run stops on the send filter.

| Step | Wait (why) | Split / router | Email | Subject A | Code |
| --- | --- | --- | --- | --- | --- |
| 1 | 45 days until 09:00 (median time to 2nd order 35 days; 57% of repeat orders within 45 days) | Cookware + (SET or `$value` >= 300) → r1-set; cookware → r1-pan; no cookware now but owns cookware → r1-pan; else r1-acc. Skip if a post-purchase or VIP email in 7 days | r1-set / r1-pan / r1-acc | The shapes a set leaves out / How's your pan doing? / Ready for the pan? | HI10 in email |
| 2 | 30 days until 09:00, day 75 (day 60 to 90 still about 1%) | CS Placed Order at least 2 ever: code router R2_VIP_15_72H, else R2_10_72H | r2-vip / r2 (or -nocode) | For our regulars: 15% for 72 hours / 10% off your next piece, for 72 hours | unique 15% / 10%, 72 h |

End day 90 (after that 0.6% per 30 days: campaign territory).

### 3.7 New flows

| Flow | Step | Wait (why) | Split / filter | Email | Subject A | Code |
| --- | --- | --- | --- | --- | --- | --- |
| Site abandonment | 1 | 2 hours (low intent, no own timing data yet) | No product view, cart, checkout or order since start; no order in 30 days; no browse/cart/checkout/post-purchase email in 7 days, no welcome in 10 | a1 | Not sure which pan? Start here. | HI10 |
| | 2 | 2 days until 09:00 | same | a2 | Where 100,000+ people started | HI10 |
| Sunset | entry | Segment: profile older than 120 days, no human click 120 days, no site activity 120 days, no order 180 days, at least 8 emails received in 120 days. Opens ignored (Apple MPP) | not in welcome or post-purchase in 30 days | | | |
| | 1 | 1 day until 09:00 | | s1 | Should we keep writing to you? | none |
| | 2 | 4 days until 09:00 | no click, site activity or order since start | s2 (plain text, Benjamin) | Last email from me (unless you tap) | none |
| | 3 | 3 days | CS click OR active on site OR order since start: `sunset_status = kept`, else `suppressed` + `sunset_at`; weekly bulk suppression | | | |
| VIP | 1 | 30 days until 09:00 after 2nd order | Code router SK_REGULARS15_14D (first 4 weeks 100% code); no refund, no order in 14 days; sets `siraat_regular = true` | v1 (or -nocode) | Twice is a habit. Here's 15% off. | unique 15%, 14 days |
| | 2 | 10 days until 09:00 | | v2 (plain text, Benjamin) | A question from Benjamin | none |
| Anniversary | 1 | 182 days until 09:00 | First order with cookware; no refund; no VIP/winback email or support ticket in 14 days | n1 (service) | How's your pan at six months? | none |
| | 2 | 183 days until 09:00 (day 365) | Code router SK_ANNIV10_7D; no order in 14 days | n2 (or -nocode) | One year ago this week | unique 10%, 7 days |
| UGC first egg | 1 | Delivery + 4 days until 09:00 (so it does not land next to P3) | First order, owns cookware; no ticket since start, no refund | u1 (reply-to support) | Show us your first egg? | 15% after a photo, via helpdesk macro |

Sequence for a median first-time cookware buyer: P1 day 0, P2 day 13, U1 day 16, P3 day 20, review day 26, R1 day 45, R2 day 75.

---

## 4. Global rules

| Rule | Setting |
| --- | --- |
| Priority between flows | Nobody is in two sales flows at once. 1 Post-purchase > 2 Checkout > 3 Cart > 4 Browse > 5 Welcome > 6 Winback > 7 Site. Each lower flow does not start (or skips) if a higher flow sent an email in the last 7 days. Welcome emails are skipped, not ended, after a checkout or cart email in 24 h. |
| Exclusion mechanism | Klaviyo only checks "has been in *this* flow". For other flows: `Received Email where Flow = <exact flow name> zero times in the last N days`. Fallback if the Flow dimension is not available: one segment per flow ("received email from flow X in 7 days") and "is not in segment". |
| Smart Sending | Off in all flows (priority rules handle overlap). |
| Quiet hours | 22:00 to 07:00 local for follow-ups, implemented as "wait X days, until 09:00". First emails (C1, K1, B1, P1, A1) go real-time, also in the evening (21 to 22 h converts as well as daytime). |
| Send time | 09:00 profile time zone for all follow-ups (orders peak 09 to 12 h). Exception: C2 and K2 "wait 1 day" without time. No weekday filter (weekend is the strongest buying day). Profiles without time zone fall back to US/Eastern. |
| Frequency cap | Max 3 campaigns per profile per 7 days (segment excluded on every campaign); flow emails do not count. New subscribers: no campaigns for 14 days. |
| Code cooldown | One unique code per person per 30 days, see router below. Discount ladder: sale + 4 gifts in every email; 10% (public HI10 or a unique code) only in the last email; 15% only VIP; never 20%+ in flows. One discount per order, so a unique code replaces HI10. |
| UTM | `utm_source=klaviyo`, `utm_medium=email`, `utm_campaign` = flow slug (`v4-checkout` etc., old path `old-<flow>`), `utm_content` = `<mailid>-<block>`, `utm_term` = test arm (`t02-b`). Never a code or personal data in a UTM. |
| Attribution | Account window unchanged during tests (5 days click, 1 day open). |
| Triggers | No Triple Pixel triggers; one trigger per flow. |

**Code router** (before every unique-code email: C4, K3, B2-clicked, P3, R2, R2-VIP, V1, N2):

```
CS "Cooldown?"  Properties about someone · last_flow_code_at · is in the last 30 days
  YES → <email>-nocode (gift stack, risk reversal; not counted in T02)
  NO  → A/B T02 50/50, no auto winner
          A → <email> with {% coupon_code 'POOL' %}
              → Update profile property: last_flow_code_at = today, last_flow_code_pool = POOL
          B → <email>-nocode
```
Fallback if Update Profile cannot set "today": code emails get a message name starting with "CODE ·" and the cooldown becomes "Received Email where Message Name starts with CODE · at least once in 30 days".

---

## 5. Tests and measurement

| Test | Where | Design | Primary metric | Decision |
| --- | --- | --- | --- | --- |
| T01 old vs new | Checkout, cart, browse, welcome | Random sample 50% right after the trigger; profile property `v3_arm = new/old` + flow + date. Old path = best current path, same templates and delays | Revenue per entrant, 7-day cohort (welcome 14) | v4 to 100% on 20 Nov unless clearly worse (upper bound of 90% interval below 0) or a guardrail breaks |
| T02 code vs no code | Last email in checkout, cart, browse, post-purchase, winback (VIP and anniversary join after 4 weeks) | Pooled A/B 50/50 per email, strata per email; after the decision a **permanent 10% holdout** | Margin contribution per recipient | Code stays only if P(lift > breakeven) >= 80%. Breakeven at 60% margin: +20% buyers for 10%, +33% for 15% |
| T04 W1 framing | Welcome W1 | HI10 as code block vs as "welcome gift card" | Unique click rate W1 (RPR as check) | B wins only at P(B > A) >= 90% and RPR not worse |
| T05a subject principle | Browse B1 | Authority "Lab-tested: nothing on this pan to scratch off" vs social proof "100,000+ happy customers cook on this pan" | Unique click rate | |

Phasing: phase 1 launch to 19 Nov; **BFCM freeze 20 Nov to 6 Dec** (old path off, T02 100% code, no new tests); phase 2 from 7 Dec (HI10 in early emails vs none, W1 subject, W3 hero, B2 length). Max 2 tests per flow.

Guardrails per arm (from 1,000 delivered): unsubscribe > 1.0% or > 1.5x control; spam > 0.10% or > 2x control (account never above 0.3%); bounce > 2%; refund rate +2 pp; sample ratio mismatch p < 0.01. Opens are never a metric (Apple MPP).

---

## 6. Email standard (see Figma for every email)

| Element | Standard |
| --- | --- |
| Code bar | Above the header in every sales email: offer and code (or "4 gifts · 30-day returns" in no-code variants). |
| Hero with offer bar | The headline carries the idea; the offer sits in a bar on the hero image, readable on mobile. |
| Above the fold | Checkout and cart: hero, cart block (paid items only, no $0 gifts), button. Browse: viewed product with price. |
| Buttons | First-person with benefit ("Complete my order", "Claim my 10% + gifts"), full width on mobile, max 3 identical primary buttons; links apply the code. |
| Friction reducer | Under every primary button: "Free shipping. 30-day returns. 100,000+ happy customers." (code and INT variants exist). |
| Real reviews | Selected and shortened only, never edited; one line of proof near the top, review block later; each sales email has one customer and one authority (lab report no. 25895). |
| Closer look / comparison | Max two big modules per email (comparison, closer look, value stack, size picker); max ~3,600 px on mobile. |
| Brand | Fixed header and footer with the SIRAAT lockup; founder voice is Benjamin; claims: 30-day returns, 75-year warranty, 100,000+ customers. Flows are calm, no em dashes, no hype words. |

---

## 7. Before go-live

**Build list (in order):** decisions below → close leaking public codes → coupons → profile properties → segments → upload images and templates → flows on Draft → test sends → live per group.

| Item | What |
| --- | --- |
| Coupons (Shopify unique, 1 use, 1 per customer, expiry after assignment) | C4_10_48H, K3_10_48H, B2_10_48H (10%, 48 h); P3_THANKYOU_10_14D (10%, 14 days); R2_10_72H (10%), R2_VIP_15_72H (15%, 72 h); SK_REGULARS15_14D (15%, 14 days); SK_ANNIV10_7D (10%, 7 days). UGC15 as a separate bulk pool for the helpdesk. |
| Profile properties | `v3_arm`, `v3_arm_flow`, `v3_arm_at`, `last_flow_code_at`, `last_flow_code_pool`, `siraat_regular`, `sunset_status`, `sunset_at` |
| Segments | Sunset unengaged 120d, Sunset suppressed, Welcome protection (14 days), Campaign cap, Has cookware, VIP, US, T01 cohorts (4 flows x 2 arms), optional "email from flow X in 7 days" |
| Templates | 61 emails built (all no-code variants included). Still to do: upload images to Klaviyo, UTM build, shorten 5 subject/preview lines, create templates named `v4 · <flow> · <email>` |
| Test sends | Test profile through every branch (pan, set, apron, board, gift card; US and INT; new and existing), coupon preview (same code everywhere in the email), `/discount/` links with UTM, reply-to, sender name |
| Go-live groups | A: checkout, cart, browse, welcome (old flows to Draft, old path lives inside v4). B: post-purchase + helper, winback. C: sunset, site, VIP, UGC, anniversary. Nothing archived. |

**Open decisions that affect the build**

| Decision | Current choice in v4 |
| --- | --- |
| C1 and K1 at 30 min instead of 1 hour | 30 min |
| C2/K2 "1 day" (can land at night) or always "until 09:00" | 1 day, no time |
| Keep HI10 in early emails at launch, test removal in phase 2 | Keep, test later |
| No separate HI10 branch for list members in last emails | No branch (otherwise almost no unique codes go out) |
| Gross margin to confirm (all code breakevens depend on it) | 60% assumed |
| Does Shopify already send a shipping email with tracking? | If not, add a tracking email |
| How long the $349 six-piece listing stays live | Eight emails link to it |
| Close leaking public codes before T02 | Required |
| Official rules page for the weekly filter draw | Needed before "draw closes Sunday" urgency |

---

## 8. Questions for Homestead

1. **Routers on `Items`.** We route on `Items contains any of <exact titles>` in trigger splits (checkout, post-purchase, winback) and on product-name substrings for Added to Cart and Viewed Product. Is this reliable in Klaviyo (title changes, variants, multi-line orders), or would you use a catalog category, tags or a profile property instead? Does a trigger split support OR, or do we chain splits?
2. **Code cooldown.** Can an Update Profile action reliably write "today" into `last_flow_code_at` for a relative-date split, or should we go with the message-name fallback? Any experience with `{% coupon_code %}` appearing several times in one email?
3. **50/50 old against new in the same flow.** Random sample split right after the trigger, with the best old path rebuilt inside the v4 flow and a profile property per arm. Sound, or would you run old and new as separate flows? Is a 7-day cohort per entrant the right read?
4. **Quiet hours.** "Wait X days, until 09:00" in the profile's time zone, with real-time first emails. Pitfalls with time zones, the day-count rule, or very long delays (182 days)?
5. **Exclusions, sunset and suppression.** Cross-flow exclusion via "Received Email where Flow = X", sunset at 120 days with click/site activity as the only signals, weekly bulk suppression of `sunset_status = suppressed`. Anything you would change, including a faster sunset (45 to 60 days) for new subscribers?
6. **Deliverability.** Outlook spam rate is 0.31% (limit 0.3%), campaigns went to the full list with Smart Sending off, DMARC is p=none. What risks do you see when v4 adds flows and volume, and what should change first on the campaign side?
7. **Launch order and gaps.** What would you put live first, what is missing for us to build and launch this ourselves in Klaviyo, and where do you see the biggest risk of something breaking silently?
