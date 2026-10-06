#!/usr/bin/env python3
"""Generates the Klaviyo flow specs (markdown) and the HTML email examples.

Run:  python3 klaviyo/build.py
Output: klaviyo/flows/*.md, klaviyo/emails/<flow>/*.html, klaviyo/index.html

All content lives in FLOWS below. Klaviyo template tags are left intact
({{ first_name|default:'' }}, {% coupon_code 'GIFT25' %}, event.* variables),
so each HTML file can be pasted into a Klaviyo HTML template as-is.
"""
from __future__ import annotations

import html
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://siraatskitchen.com"
SHOP_ALL = f"{SITE}/collections/all"
GIFT_CARD = f"{SITE}/products/e-gift-card"

# ----------------------------------------------------------------------------
# Image assets (Klaviyo CDN = already in the account's image library,
# Shopify CDN = live product photos). All load in email clients.
# ----------------------------------------------------------------------------
KL = "https://d3k81ch9hvuctc.cloudfront.net/company/TdtTzz/images/"
SH = "https://cdn.shopify.com/s/files/1/0907/0877/1156/files/"
IMG = {
    # existing Klaviyo assets
    "logo": KL + "14eadd25-c23b-41d6-8b65-01416cbd1bc4.png",
    "nav_shop": KL + "8690236c-2516-446e-baa2-e7d17ee52b9a.png",
    "nav_about": KL + "b3bdcf9e-1580-4c73-a540-d2af11f4a34e.png",
    "nav_faq": KL + "aaddd65f-9ff2-4a31-ba5b-20c8a20b1ee1.png",
    "rated": KL + "867d8f8f-41ef-4ea2-a9c9-f8fb1f72ea7e.png",
    "trust_gif": KL + "d4bfbbdb-461e-442e-bf99-37821d3ba2fa.gif",
    "follow": KL + "061bca1b-5ce2-4bcb-9b9b-c18bca64a612.png",
    "ig": KL + "bc0bc9bd-8958-4522-83cb-8e21359cf6f8.png",
    "fb": KL + "962e2830-e81d-47e6-b049-c8eed2458a84.png",
    "siraat_footer": KL + "fd9170e4-b937-4d64-9c9d-d6e720f1ad22.png",
    "privacy": KL + "ff5e61a2-c093-4383-a0f9-39d110a84f16.png",
    "terms": KL + "78600673-0f5e-431a-8365-a64a5065bc0c.png",
    "kept_safe": KL + "a095ecf3-4fb6-4cd0-8314-559f2c8ff5c4.png",
    "feel_difference": KL + "b0d19ead-3640-4e9e-9502-6aaa3cf87b4e.png",
    "welcome_banner": KL + "8ed8fc2c-8d34-4762-9f96-4282534c4f29.png",
    "inside": KL + "819acdf3-7285-405c-ab75-5efc9ce07404.png",
    "from_kitchen": KL + "906fe5b7-3f9d-4d0e-b37e-75245eb91f19.png",
    "safe_kitchenware": KL + "5d1d0065-3899-4c24-be99-338522aa97e3.png",
    "cook10_banner": KL + "2d94fd5e-7b32-48d0-bc8c-07bbe663418f.png",
    # Shopify product photos
    "standard": SH + "Titanium_hammered_pan_pro_standard_b69d1fc5-43d8-40a5-9ad7-523bdddc54d4.webp?v=1781682831",
    "large": SH + "Titanium_hammered_pan_pro_large_6d4ce352-c4ff-48c9-b4d1-170232007e4f.webp?v=1781682831",
    "small": SH + "Titanium_hammered_pan_pro_small_76f7b49e-60cd-4e03-a90e-e72411c244d4.webp?v=1781682830",
    "wok": SH + "WokHammedPan_3.webp?v=1780301994",
    "deep": SH + "DeepHammeredPan.webp?v=1780301640",
    "crepe": SH + "Crepepan01.jpg?v=1751891713",
    "duo_flipper": SH + "HammeredPanProWithFlipper.webp?v=1780126830",
    "set_pro": SH + "cookwaresetpro.webp?v=1777628114",
    "four_pcs": SH + "TitaniumPan4PCS2.jpg?v=1774026132",
    "full_pro": SH + "FullHammeredProEdition_3.webp?v=1776602877",
    "kit": SH + "SIRAAT_53.png?v=1759447172",
    "utensil_set": SH + "TitaniumHammeredPanPro_UtensilSet.jpg?v=1758400325",
    "pizza": SH + "TitaniumHammeredPizzaSteel.webp?v=1765805736",
    "pots": SH + "6PCSSet09.webp?v=1780225733",
    "utensils": SH + "Utensils05-V2_1.webp?v=1780300209",
    "board": SH + "TitaniumCuttingBoard08_9c3268c8-b730-405a-8253-b9d7c6ab24e5.jpg?v=1757699471",
    "lid": SH + "Regular_Hammered_Panttern_Pan_with_lid_02_e1b2d9bb-75a9-41ee-ae7a-f88f008157e1.jpg?v=1759445618",
    "giftcard": SH + "b9d997d2-ff4c-424d-ab23-bc0949ff0c18.jpg?v=1764890312",
}


def shop_img(key: str, width: int = 1200) -> str:
    """Shopify CDN resize parameter; Klaviyo assets are returned untouched."""
    url = IMG[key]
    return f"{url}&width={width}" if url.startswith(SH) else url


# Hero image per email file (top of the mail, full width, links to the CTA)
HERO = {
    "w1-welcome-10": "welcome_banner", "w2-note-from-benjamin": "duo_flipper", "w3-why-titanium": "standard",
    "w4-social-proof": "set_pro", "w5-expires-tonight": "large",
    "c1-left-on-the-stove": "kept_safe", "c2a-25-in-your-account": "giftcard", "c2b-10-off-to-finish": "cook10_banner",
    "c3-still-deciding": "feel_difference", "c4a-25-expires-tonight": "giftcard", "c4b-10-expires-tonight": "kit",
    "k1-we-saved-these": "kept_safe", "k2-questions": "safe_kitchenware", "k3-cook10": "cook10_banner", "k4-last-call": "standard",
    "b1-still-looking": "{{ event.ImageURL }}", "b2-what-cooks-say": "four_pcs",
    "f1-titanium-vs-nonstick": "standard", "f2-care-faq": "wok", "f3-real-reviews": "set_pro",
    "s1-staying-or-going": "duo_flipper", "s2-last-email": "large",
    "p1-weve-got-your-order": "utensil_set", "p2-founder-note": "from_kitchen", "p3-get-ready-to-cook": "standard",
    "p4-your-25-for-january": "giftcard", "r1-welcome-back": "set_pro",
    "wb1-whats-new": "full_pro", "wb2-winback10": "deep", "wb3-expires": "crepe",
    "g1-thanks-for-gifting": "giftcard", "g2-opened-yet": "giftcard", "gc1-too-late-to-ship": "giftcard",
    "gc2-arrives-today": "giftcard", "gc3-christmas-eve": "giftcard",
}
# A second, smaller image under the body text (optional)
FEATURE = {
    "w1-welcome-10": "inside", }

# ----------------------------------------------------------------------------
# Shared layout
# ----------------------------------------------------------------------------

BASE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  body {{ margin:0; padding:0; background:#f7f7f7; -webkit-font-smoothing:antialiased; }}
  table {{ border-collapse:collapse; }}
  img {{ border:0; display:block; max-width:100%; height:auto; }}
  a {{ color:#1e1e1e; }}
  .btn a {{ display:inline-block; background:#1e1e1e; color:#ffffff !important; text-decoration:none; padding:16px 36px; border-radius:4px; font-weight:700; font-size:15px; letter-spacing:1px; text-transform:uppercase; font-family:Helvetica,Arial,sans-serif; }}
  .code {{ display:inline-block; background:#fff8e6; border:1px dashed #c9a24b; padding:10px 18px; font-size:22px; letter-spacing:2px; font-weight:700; font-family:Helvetica,Arial,sans-serif; }}
  @media (max-width:620px) {{ .wrap {{ width:100% !important; }} .pad {{ padding-left:18px !important; padding-right:18px !important; }} }}
</style>
</head>
<body>
<div style="display:none;max-height:0;overflow:hidden;font-size:1px;color:#f7f7f7;">{preview}&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;</div>
<table role="presentation" width="100%" bgcolor="#f7f7f7">
<tr><td align="center" style="padding:24px 0;">
<table role="presentation" class="wrap" width="600" bgcolor="#ffffff" style="width:600px; font-family:Helvetica,Arial,sans-serif; color:#1e1e1e;">

  <!-- header: existing Klaviyo assets (logo + nav) -->
  <tr><td><a href="{site}"><img src="{logo}" width="600" alt="Siraat's Kitchen"></a></td></tr>
  <tr><td>
    <table role="presentation" width="100%"><tr>
      <td width="33%"><a href="{site}"><img src="{nav_shop}" width="200" alt="SHOP"></a></td>
      <td width="33%"><a href="{site}/pages/about-us"><img src="{nav_about}" width="200" alt="ABOUT US"></a></td>
      <td width="33%"><a href="{site}/pages/faq"><img src="{nav_faq}" width="200" alt="FAQ"></a></td>
    </tr></table>
  </td></tr>

  <!-- hero -->
  <tr><td><a href="{cta_url}"><img src="{hero}" width="600" alt="{headline_alt}" style="width:100%;"></a></td></tr>

  <!-- body -->
  <tr><td class="pad" style="padding:32px 40px 8px 40px;">
    <h1 style="margin:0 0 14px 0; font-size:26px; line-height:1.25; font-weight:700; text-align:center;">{headline}</h1>
    {body}
  </td></tr>

  {product}

  {cta}

  {feature}

  {proof}

  <!-- trust bar (text, replaces the outdated 30,000 gif) -->
  <tr><td style="padding:16px 20px; background:#f2f2f2;">
    <table role="presentation" width="100%" style="font-family:Helvetica,Arial,sans-serif; font-size:11px; letter-spacing:1px; text-transform:uppercase; color:#2b2929; font-weight:700;">
      <tr><td align="center">100K+ customers</td><td align="center">75-year warranty</td><td align="center">Tested PFAS-free</td><td align="center">100-day trial</td></tr>
    </table>
  </td></tr>

  <!-- footer: existing Klaviyo assets -->
  <tr><td><img src="{follow}" width="600" alt="FOLLOW US"></td></tr>
  <tr><td><table role="presentation" width="100%"><tr>
    <td width="50%"><a href="https://www.instagram.com/siraatskitchen/"><img src="{ig}" width="300" alt="Instagram"></a></td>
    <td width="50%"><a href="https://www.facebook.com/profile.php?id=61567176126958"><img src="{fb}" width="300" alt="Facebook"></a></td>
  </tr></table></td></tr>
  <tr><td><a href="{site}"><img src="{siraat_footer}" width="600" alt="SIRAAT"></a></td></tr>
  <tr><td bgcolor="#272727"><table role="presentation" width="100%"><tr>
    <td width="50%"><a href="{site}/policies/privacy-policy"><img src="{privacy}" width="300" alt="Privacy Policy"></a></td>
    <td width="50%"><a href="{site}/policies/terms-of-service"><img src="{terms}" width="300" alt="Terms of Service"></a></td>
  </tr></table></td></tr>
  <tr><td bgcolor="#272727" align="center" style="padding:10px 0 14px 0; font-size:11px; color:#ffffff;">
    {signoff}{{{{ organization.name }}}} &middot; {{{{ organization.full_address }}}}<br>
    No longer want to receive these emails? <a href="{{{{ unsubscribe_link }}}}" style="color:#ffffff;">Unsubscribe</a> &middot; <a href="{{{{ manage_preferences_link }}}}" style="color:#ffffff;">Preferences</a>
  </td></tr>

</table>
</td></tr>
</table>
</body>
</html>
"""


def p(text: str) -> str:
    return f'<p style="margin:0 0 14px 0; font-size:15px; line-height:1.6; text-align:center;">{text}</p>'


def cta(label: str, url: str, ghost: bool = False) -> str:
    cls = "btn-ghost" if ghost else "btn"
    return f"""  <tr><td class="pad" align="center" style="padding:8px 40px 28px 40px;">
    <span class="{cls}"><a href="{url}">{label}</a></span>
  </td></tr>
"""


def code_block(code_tag: str, label: str) -> str:
    return f"""<table role="presentation" width="100%" style="margin:8px 0 20px 0;"><tr><td align="center" style="padding:18px; background:#fbfaf7; border:1px solid #e8e3da; border-radius:8px; font-family:Helvetica,Arial,sans-serif;">
      <div style="font-size:12px; letter-spacing:1px; text-transform:uppercase; color:#6b6b6b; margin-bottom:8px;">{label}</div>
      <span class="code">{code_tag}</span>
    </td></tr></table>"""


# Dynamic product blocks (Klaviyo event variables)
CHECKOUT_ITEMS = """  <tr><td class="pad" style="padding:0 40px 8px 40px;">
    <table role="presentation" width="100%" style="border:1px solid #e8e3da; background:#fcfaf7;">
      {% for item in event.extra.line_items %}
      <tr>
        <td width="150" align="center" style="padding:12px;"><img src="{{ item.product.images.0.src|default:'' }}" width="130" alt="{{ item.product.title }}" style="margin:0 auto;"></td>
        <td style="padding:12px; font-size:16px;">{{ item.product.title }}<br><span style="color:#6b6b6b; font-size:14px;">Qty {{ item.quantity }} &middot; {{ event.extra.currency }} {{ item.line_price|floatformat:2 }}</span></td>
      </tr>
      {% endfor %}
    </table>
  </td></tr>
"""

SINGLE_PRODUCT = """  <tr><td class="pad" align="center" style="padding:0 40px 8px 40px;">
    <table role="presentation" width="100%" style="border:1px solid #e8e3da;">
      <tr>
        <td align="center" style="padding:16px;"><a href="{{ event.URL }}"><img src="{{ event.ImageURL }}" width="320" alt="{{ event.ProductName }}" style="margin:0 auto;"></a></td>
      </tr>
      <tr>
        <td align="center" style="padding:0 16px 16px 16px; font-size:16px;"><a href="{{ event.URL }}" style="text-decoration:none; color:#1e1e1e;">{{ event.ProductName }}</a><br><span style="color:#6b6b6b; font-size:13px;">Free shipping &middot; 100-day trial</span></td>
      </tr>
    </table>
  </td></tr>
"""

BESTSELLERS = f"""  <tr><td class="pad" style="padding:0 28px 8px 28px;">
    <table role="presentation" width="100%" style="font-family:Helvetica,Arial,sans-serif; font-size:13px; text-align:center;">
      <tr>
        <td width="33%" style="padding:8px;"><a href="{SITE}/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern" style="text-decoration:none; color:#1e1e1e;"><img src="{shop_img('standard', 400)}" width="170" alt="Pan Pro Standard" style="margin:0 auto 8px auto;">Pan Pro Standard<br><b>$134</b></a></td>
        <td width="33%" style="padding:8px;"><a href="{SITE}/products/titanium-hammered-pan-pro-large" style="text-decoration:none; color:#1e1e1e;"><img src="{shop_img('large', 400)}" width="170" alt="Pan Pro Large" style="margin:0 auto 8px auto;">Pan Pro Large<br><b>$139</b></a></td>
        <td width="33%" style="padding:8px;"><a href="{SITE}/products/titanium-hammered-wok-pan-pro" style="text-decoration:none; color:#1e1e1e;"><img src="{shop_img('wok', 400)}" width="170" alt="Wok Pan Pro" style="margin:0 auto 8px auto;">Wok Pan Pro<br><b>from $119</b></a></td>
      </tr>
    </table>
  </td></tr>
"""

REVIEWS = """  <tr><td class="pad" style="padding:0 36px 24px 36px;">
    <table role="presentation" width="100%" style="font-size:14px; line-height:1.5;">
      <tr><td style="padding:12px 0; border-top:1px solid #e8e3da;">&#9733;&#9733;&#9733;&#9733;&#9733; &ldquo;Eggs slide off with no oil. I threw out three non-stick pans the week this arrived.&rdquo; <span style="color:#6b6b6b;">&mdash; Dana R.</span></td></tr>
      <tr><td style="padding:12px 0; border-top:1px solid #e8e3da;">&#9733;&#9733;&#9733;&#9733;&#9733; &ldquo;Metal spatula, dishwasher, high heat. Nothing to scratch off because there is no coating.&rdquo; <span style="color:#6b6b6b;">&mdash; Marcus T.</span></td></tr>
      <tr><td style="padding:12px 0; border-top:1px solid #e8e3da; border-bottom:1px solid #e8e3da;">&#9733;&#9733;&#9733;&#9733;&#9733; &ldquo;Half the weight of my cast iron and heats faster. Bought a second one for my mum.&rdquo; <span style="color:#6b6b6b;">&mdash; Priya K.</span></td></tr>
    </table>
      </td></tr>
"""

FOUNDER_SIGNOFF = "Benjamin, founder<br>"

# ----------------------------------------------------------------------------
# Flow definitions
# ----------------------------------------------------------------------------
# email keys: file, subject, preview, tag, headline, body (list of paragraphs or raw html),
#             product (optional block), cta (label, url), proof (optional), signoff, delay,
#             filters, smart_sending, incentive, notes

FLOWS = [
    # ------------------------------------------------------------------ 1
    dict(
        slug="01-welcome",
        name="Welcome Flow (nieuw)",
        replaces="EB | Welcome Flow | Updated 02.03.26 (SiaNLu)",
        trigger="Added to List: Email List (Uw8eZG)",
        trigger_filters="Geen",
        profile_filters=[
            "Placed Order = 0 times since starting this flow (op elke mail)",
            "Email not contains test@example.com",
        ],
        settings=[
            "Smart sending UIT op mail 1, AAN op mail 2 tot 5",
            "Re-entry: nooit (een profiel doorloopt de welcome flow eenmaal)",
            "Alle mails van send@siraatskitchen.com, reply-to support@",
        ],
        tree="""Trigger: Added to List "Email List"
│
├─ [5 min] ─ W1  Welcome + 10% (HI10 uniek)
├─ [1 dag, 10:00] ─ W2  Note from Benjamin
├─ [2 dagen, 10:00] ─ W3  Why titanium, not coating
├─ [2 dagen, 10:00] ─ W4  100,000 kitchens (bestsellers)
├─ [2 dagen, 10:00] ─ W5  Your 10% expires tonight
│
└─ Conditional split: Placed Order > 0 since start?
     ├─ YES → exit (Post Purchase flow neemt over)
     └─ NO  → exit (Failure to launch pakt ze op dag 14 op)""",
        emails=[
            dict(file="w1-welcome-10", delay="5 min na trigger", subject="{{ first_name|default:'Welcome' }}, here's your 10% off",
                 preview="One code, one cookware upgrade. Valid 7 days.", tag="Welcome 1 of 5",
                 headline="Welcome to the kitchen that doesn't need a coating.",
                 body=[p("You're in. Here is your welcome code, good for 10% off anything in the shop for the next 7 days."),
                       code_block("{% coupon_code 'HI10' %}", "Your welcome code, 10% off, 7 days"),
                       p("Every Siraat pan is hand-hammered titanium. No PFAS, no ceramic layer that wears off, nothing to re-season. Cook on it for 100 days. If it isn't the best pan you own, send it back.")],
                 product=BESTSELLERS, cta=("Shop with 10% off", SHOP_ALL), proof="", signoff="",
                 incentive="HI10 uniek, 10%, 7 dagen", smart="UIT", filters="Placed Order = 0 since start",
                 notes="Zet de code als tekst, niet alleen in een afbeelding (huidige fout)."),
            dict(file="w2-note-from-benjamin", delay="1 dag, 10:00", subject="A note from Benjamin",
                 preview="Why I started making pans out of titanium.", tag="Welcome 2 of 5",
                 headline="I was tired of replacing pans every two years.",
                 body=[p("Hi {{ first_name|default:'there' }},"),
                       p("Every non-stick pan I owned went the same way: slick for a year, then flaking, then in the bin. The 'healthy' ceramic ones were worse. So I went looking for a surface that doesn't have a coating to lose."),
                       p("Titanium was the answer. Hammered by hand so the surface has thousands of tiny dimples that keep oil where it belongs. It takes a few cooks to learn (we'll show you how), and then it outlasts everything else in your drawer."),
                       p("That's the whole company. One material, done properly, backed by 100 days to try it.")],
                 product="", cta=("See how it's made", f"{SITE}/pages/about"), proof="", signoff=FOUNDER_SIGNOFF,
                 incentive="Geen", smart="AAN", filters="Placed Order = 0 since start", notes=""),
            dict(file="w3-why-titanium", delay="2 dagen, 10:00", subject="Why food sticks (and why it won't on titanium)",
                 preview="The 3-step method that makes a titanium pan release like non-stick.", tag="Welcome 3 of 5",
                 headline="Coatings wear off. Titanium doesn't.",
                 body=[p("Non-stick works because of a layer on top of the metal. Titanium works because of the metal itself. That changes three things:"),
                       "<ol style='font-size:16px; line-height:1.7; margin:0 0 16px 20px; padding:0;'><li><b>Heat first, then oil, then food.</b> Medium heat for 60 seconds, a thin film of oil, then the egg. It slides.</li><li><b>Metal utensils are fine.</b> There is nothing to scratch.</li><li><b>Dishwasher is fine.</b> No coating to protect.</li></ol>",
                       p("Your 10% code is still active for 4 more days.")],
                 product="", cta=("Read the care guide", f"{SITE}/pages/care"), proof="", signoff="",
                 incentive="Verwijst naar HI10", smart="AAN", filters="Placed Order = 0 since start", notes=""),
            dict(file="w4-social-proof", delay="2 dagen, 10:00", subject="What 100,000 kitchens figured out",
                 preview="The three pans people buy first.", tag="Welcome 4 of 5",
                 headline="Start with the pan you'll use every night.",
                 body=[p("Most people start with the Pan Pro Standard. It fits a two-person dinner, goes from stove to oven, and is the one our customers reorder for family."),],
                 product=BESTSELLERS, cta=("Shop bestsellers", SHOP_ALL), proof=REVIEWS, signoff="",
                 incentive="Verwijst naar HI10", smart="AAN", filters="Placed Order = 0 since start AND Opened Email ≥ 1 since start", notes=""),
            dict(file="w5-expires-tonight", delay="2 dagen, 10:00", subject="Your 10% ends tonight",
                 preview="After midnight the code stops working.", tag="Welcome 5 of 5",
                 headline="Last day for your welcome code.",
                 body=[p("Hi {{ first_name|default:'there' }}, your 10% welcome code expires at midnight. After that it's gone, and we don't resend it."),
                       code_block("{% coupon_code 'HI10' %}", "10% off, ends tonight"),
                       p("Free shipping, 100 days to try it, and nothing to re-season. If you've been waiting, this is the moment.")],
                 product="", cta=("Use my 10% now", SHOP_ALL), proof="", signoff="",
                 incentive="HI10", smart="AAN", filters="Placed Order = 0 since start", notes="Daarna conditional split op Placed Order; beide takken eindigen."),
        ],
    ),
    # ------------------------------------------------------------------ 2
    dict(
        slug="02-checkout-abandonment",
        name="Checkout Abandonment (samengevoegd, A/B gift card vs 10%)",
        replaces="EB | DEC 25 | Checkout Abandonment (Y2TmNB) + Triple Pixel variant (Tsg2tV)",
        trigger="Checkout Started (Shopify, RfMvni)",
        trigger_filters="Geen",
        profile_filters=[
            "Placed Order = 0 times since starting this flow",
            "Has not been in this flow in the last 7 days",
            "Received Email from flow 'Checkout Abandonment Triple Pixel' = 0 since start (of zet die flow uit)",
            "Email not contains test@example.com",
        ],
        settings=[
            "Smart sending UIT op C1 en de sms, AAN op C2 tot C4",
            "Sms alleen bij SMS consent, quiet hours aan (21:00 tot 09:00 lokale tijd), Texas-segment uitsluiten",
            "Eén 50% random sample split direct na de trigger: tak A = $25 gift card, tak B = 10% code. Na 4 weken winnaar kiezen en de split verwijderen",
            "Geen geneste splits meer",
        ],
        tree="""Trigger: Checkout Started (Shopify)
│
├─ [1 uur] ─ C1  You left something on the stove (cart, geen korting)
│
├─ Conditional split: SMS consent?
│    └─ YES → [1 uur] SMS-1  "Your cart is saved: {{ checkout_url }}"
│
└─ Random sample split 50%
     ├─ A (gift card)
     │    ├─ [1 dag, 09:00] ─ C2a  $25 is waiting in your account (GIFT25)
     │    ├─ [1 dag, 09:00] ─ C3   Still deciding? 100 days to try it
     │    └─ [1 dag, 09:00] ─ C4a  Your $25 expires tonight
     └─ B (10%)
          ├─ [1 dag, 09:00] ─ C2b  10% off to finish your order (CHECKOUT10)
          ├─ [1 dag, 09:00] ─ C3   Still deciding? 100 days to try it
          └─ [1 dag, 09:00] ─ C4b  Your 10% expires tonight""",
        sms=[
            ("SMS-1", "1 uur na C1, alleen met SMS consent",
             "Siraat's Kitchen: your cart is saved and ships free. Finish here: {{ event.extra.checkout_url }} Reply STOP to opt out."),
        ],
        emails=[
            dict(file="c1-left-on-the-stove", delay="1 uur na trigger", subject="You left something on the stove",
                 preview="Your cart is saved. Free shipping, 100-day trial.", tag="Checkout 1 of 4",
                 headline="Your cart is still here.",
                 body=[p("Hi {{ first_name|default:'there' }}, you were one step from checkout. We've kept everything in your cart, and shipping is on us.")],
                 product=CHECKOUT_ITEMS, cta=("Finish my order", "{{ event.extra.checkout_url }}"), proof="", signoff="",
                 incentive="Geen (bewust: eerst de twijfelaars zonder korting laten converteren)", smart="UIT", filters="Placed Order = 0 since start", notes=""),
            dict(file="c2a-25-in-your-account", delay="1 dag, 09:00 (tak A)", subject="{{ first_name|default:'Hey' }}, there's $25 in your account",
                 preview="A $25 gift card toward your cart. Valid 72 hours.", tag="Checkout 2 of 4 · A",
                 headline="We put $25 on your account.",
                 body=[p("Still thinking about it? We've added a $25 gift card to your account. It comes off your cart at checkout, no minimum fuss (orders over $99), and it's valid for 72 hours."),
                       code_block("{% coupon_code 'GIFT25' %}", "Your $25 gift card code"),
                       p("Add it in the discount field at checkout. Free shipping and the 100-day trial still apply.")],
                 product=CHECKOUT_ITEMS, cta=("Use my $25", "{{ event.extra.checkout_url }}?discount={% coupon_code 'GIFT25' %}"), proof="", signoff="",
                 incentive="GIFT25 uniek, $25 vast, min. $99, 72 uur", smart="AAN", filters="Placed Order = 0 since start", notes="Test-tak A."),
            dict(file="c2b-10-off-to-finish", delay="1 dag, 09:00 (tak B)", subject="{{ first_name|default:'Hey' }}, 10% off to finish your order",
                 preview="Your cart plus 10% off. Valid 72 hours.", tag="Checkout 2 of 4 · B",
                 headline="10% off, just for this cart.",
                 body=[p("Still thinking about it? Here's 10% off everything in your cart, valid for 72 hours."),
                       code_block("{% coupon_code 'CHECKOUT10' %}", "Your 10% code"),
                       p("Add it in the discount field at checkout. Free shipping and the 100-day trial still apply.")],
                 product=CHECKOUT_ITEMS, cta=("Use my 10%", "{{ event.extra.checkout_url }}?discount={% coupon_code 'CHECKOUT10' %}"), proof="", signoff="",
                 incentive="CHECKOUT10 uniek, 10%, 72 uur", smart="AAN", filters="Placed Order = 0 since start", notes="Test-tak B."),
            dict(file="c3-still-deciding", delay="1 dag, 09:00 (beide takken)", subject="Still deciding? Here's what actually matters",
                 preview="100 days to try it. Free returns. No coating to wear off.", tag="Checkout 3 of 4",
                 headline="Three questions people ask before they order.",
                 body=["<p style='margin:0 0 12px 0; font-size:16px; line-height:1.6;'><b>Does food really not stick?</b> Yes, once the pan is hot and lightly oiled. We send a 3-step guide with every order.</p>",
                       "<p style='margin:0 0 12px 0; font-size:16px; line-height:1.6;'><b>What if I don't like it?</b> 100 days to cook on it. Send it back for a full refund, no questions.</p>",
                       "<p style='margin:0 0 16px 0; font-size:16px; line-height:1.6;'><b>Will it last?</b> There is no coating to fail. Metal utensils, dishwasher, high heat, all fine.</p>",
                       p("Your code from yesterday is still active until tomorrow night.")],
                 product="", cta=("Back to my cart", "{{ event.extra.checkout_url }}"), proof=REVIEWS, signoff="",
                 incentive="Verwijst naar code van C2", smart="AAN", filters="Placed Order = 0 since start", notes=""),
            dict(file="c4a-25-expires-tonight", delay="1 dag, 09:00 (tak A)", subject="Your $25 expires tonight",
                 preview="After midnight the gift card is gone.", tag="Checkout 4 of 4 · A",
                 headline="Last call for your $25.",
                 body=[p("Your $25 gift card expires at midnight. We can't extend it, and your cart will clear soon after."),
                       code_block("{% coupon_code 'GIFT25' %}", "$25 off, ends tonight")],
                 product=CHECKOUT_ITEMS, cta=("Finish with $25 off", "{{ event.extra.checkout_url }}?discount={% coupon_code 'GIFT25' %}"), proof="", signoff="",
                 incentive="GIFT25", smart="AAN", filters="Placed Order = 0 since start", notes=""),
            dict(file="c4b-10-expires-tonight", delay="1 dag, 09:00 (tak B)", subject="Your 10% expires tonight",
                 preview="After midnight the code is gone.", tag="Checkout 4 of 4 · B",
                 headline="Last call for your 10%.",
                 body=[p("Your 10% code expires at midnight. We can't extend it, and your cart will clear soon after."),
                       code_block("{% coupon_code 'CHECKOUT10' %}", "10% off, ends tonight")],
                 product=CHECKOUT_ITEMS, cta=("Finish with 10% off", "{{ event.extra.checkout_url }}?discount={% coupon_code 'CHECKOUT10' %}"), proof="", signoff="",
                 incentive="CHECKOUT10", smart="AAN", filters="Placed Order = 0 since start", notes=""),
        ],
    ),
    # ------------------------------------------------------------------ 3
    dict(
        slug="03-cart-abandonment",
        name="Cart Abandonment (nieuw)",
        replaces="EB | Cart Abandonment | 2/03/26 (SwkMyn) + Triple Pixel variant (TBWngE)",
        trigger="Added to Cart (Shopify, QXcV8K)",
        trigger_filters="Geen",
        profile_filters=[
            "Checkout Started = 0 times since starting this flow",
            "Placed Order = 0 times since starting this flow",
            "Has not been in this flow in the last 7 days",
            "Received Email from flow 'Checkout Abandonment' = 0 in the last 3 days",
        ],
        settings=[
            "Smart sending UIT op K1, AAN op K2 tot K4",
            "Geen random sample split. Eén tak.",
            "first_name altijd met |default:'' (huidige mails tonen 'Hi ,')",
        ],
        tree="""Trigger: Added to Cart (Shopify)
│
├─ [1 uur] ─ K1  We saved these for you (geen korting)
├─ [1 dag, 09:00] ─ K2  Questions before you decide? (trial, care)
├─ [1 dag, 09:00] ─ K3  Get cooking with 10% off (COOK10)
└─ [1 dag, 09:00] ─ K4  Last call for 10%
     (K3 en K4 alleen als Checkout Started = 0 in laatste 3 dagen)""",
        emails=[
            dict(file="k1-we-saved-these", delay="1 uur na trigger", subject="{{ first_name|default:'Hey' }}, we saved these for you",
                 preview="Your cart is waiting. Free shipping on every order.", tag="Cart 1 of 4",
                 headline="Still in your cart.",
                 body=[p("Hi {{ first_name|default:'there' }}, you added this to your cart and left before checkout. It's still there, and shipping is free.")],
                 product=SINGLE_PRODUCT, cta=("Back to my cart", f"{SITE}/cart"), proof="", signoff="",
                 incentive="Geen", smart="UIT", filters="Checkout Started = 0 AND Placed Order = 0 since start", notes=""),
            dict(file="k2-questions", delay="1 dag, 09:00", subject="Questions before you decide?",
                 preview="100 days to try it. Here's how the first cook goes.", tag="Cart 2 of 4",
                 headline="Try it for 100 days. Here's what the first week looks like.",
                 body=[p("Day 1: heat the pan on medium for a minute, add a little oil, cook an egg. It releases. Day 2 onward: whatever you like, metal spatula included. Day 100: if it's not the pan you reach for, send it back."),
                       p("No coating, so no learning when it 'wears out'. It doesn't.")],
                 product=SINGLE_PRODUCT, cta=("Back to my cart", f"{SITE}/cart"), proof=REVIEWS, signoff="",
                 incentive="Geen", smart="AAN", filters="Checkout Started = 0 AND Placed Order = 0 since start", notes=""),
            dict(file="k3-cook10", delay="1 dag, 09:00", subject="{{ first_name|default:'Hey' }}, get cooking with 10% off",
                 preview="Your cart plus 10% off, valid 48 hours.", tag="Cart 3 of 4",
                 headline="10% off what's in your cart.",
                 body=[p("Here's a nudge: 10% off your cart for the next 48 hours."),
                       code_block("{% coupon_code 'COOK10' %}", "Your 10% code, 48 hours")],
                 product=SINGLE_PRODUCT, cta=("Use my 10%", f"{SITE}/cart?discount={{% coupon_code 'COOK10' %}}"), proof="", signoff="",
                 incentive="COOK10 uniek, 10%, 48 uur", smart="AAN", filters="Checkout Started = 0 in last 3 days AND Placed Order = 0 since start", notes=""),
            dict(file="k4-last-call", delay="1 dag, 09:00", subject="Last call for 10% off",
                 preview="Your code ends tonight.", tag="Cart 4 of 4",
                 headline="Your 10% ends tonight.",
                 body=[p("The code expires at midnight and your cart clears shortly after."),
                       code_block("{% coupon_code 'COOK10' %}", "10% off, ends tonight")],
                 product=SINGLE_PRODUCT, cta=("Finish my order", f"{SITE}/cart?discount={{% coupon_code 'COOK10' %}}"), proof="", signoff="",
                 incentive="COOK10", smart="AAN", filters="Checkout Started = 0 in last 3 days AND Placed Order = 0 since start AND Opened Email ≥ 1 since start", notes=""),
        ],
    ),
    # ------------------------------------------------------------------ 4
    dict(
        slug="04-browse-abandonment",
        name="Browse Abandonment (samengevoegd)",
        replaces="EB | DEC 25 | Browse Abandonment (Wj6x6V) + Triple Pixel variant (TyEjuQ)",
        trigger="Viewed Product (Klaviyo onsite, XNtYMB)",
        trigger_filters="Geen",
        profile_filters=[
            "Added to Cart = 0, Checkout Started = 0, Placed Order = 0 since starting this flow",
            "Has not been in this flow in the last 7 days (beide varianten gelijk, nu 2 en 30 dagen)",
            "Received Email from flow 'Browse Abandonment Triple Pixel' = 0 in the last 7 days (of zet die flow uit)",
            "Received Email from flow 'Cart Abandonment' = 0 in the last 3 days",
        ],
        settings=[
            "Smart sending UIT op B1, AAN op B2",
            "Afzender send@ (nu support@, inconsistent met de rest)",
        ],
        tree="""Trigger: Viewed Product
│
├─ [2 uur] ─ B1  Still looking at {{ event.ProductName }}?
└─ Conditional split: Added to Cart since start?
     ├─ YES → exit (Cart flow neemt over)
     └─ NO  → [2 dagen, 09:00] ─ B2  What 100,000 cooks say""",
        emails=[
            dict(file="b1-still-looking", delay="2 uur na trigger", subject="Still looking at {{ event.ProductName|default:'this' }}?",
                 preview="Free shipping and 100 days to try it.", tag="Browse 1 of 2",
                 headline="We saw you looking.",
                 body=[p("Hi {{ first_name|default:'there' }}, you had a look at this earlier. If it helps: shipping is free, you get 100 days to try it, and there's no coating to wear off.")],
                 product=SINGLE_PRODUCT, cta=("Take another look", "{{ event.URL }}"), proof="", signoff="",
                 incentive="Geen", smart="UIT", filters="Added to Cart = 0, Checkout Started = 0, Placed Order = 0 since start", notes=""),
            dict(file="b2-what-cooks-say", delay="2 dagen, 09:00", subject="What 100,000 cooks say about it",
                 preview="Real reviews, and the 100-day trial if they're wrong.", tag="Browse 2 of 2",
                 headline="Don't take our word for it.",
                 body=[p("Here is what people wrote after a few weeks with the pan you looked at.")],
                 product=SINGLE_PRODUCT, cta=("Try it for 100 days", "{{ event.URL }}"), proof=REVIEWS, signoff="",
                 incentive="Geen", smart="AAN", filters="Added to Cart = 0 AND Placed Order = 0 since start", notes="Geen korting in browse: de incentive bewaren voor cart en checkout."),
        ],
    ),
    # ------------------------------------------------------------------ 5
    dict(
        slug="05-failure-to-launch",
        name="Failure to launch (ingekort tot 3 mails)",
        replaces="EB | Failure to launch (T2SmtR, 10 mails, 105.835 verzendingen per maand)",
        trigger="Added to List: Email List (Uw8eZG)",
        trigger_filters="Geen",
        profile_filters=[
            "Placed Order = 0 times since starting this flow",
            "Opened Email ≥ 1 in the last 14 days (alleen wie de welcome flow heeft geopend)",
        ],
        settings=[
            "Eerste wachtstap 14 dagen (nu 30), daarna 3 mails in 7 dagen",
            "Smart sending AAN op alles",
            "Na de laatste mail: niet geopend → Update profile property FTL_unopened = true (input voor sunset)",
        ],
        tree="""Trigger: Added to List "Email List"
│
└─ [14 dagen, 09:00]
    └─ Conditional split: Placed Order = 0 AND Opened Email ≥ 1 (last 14 d)?
         ├─ NO  → exit
         └─ YES
              ├─ F1  Titanium vs non-stick
              ├─ [3 dagen, 09:00] ─ F2  Care FAQ
              └─ [4 dagen, 09:00] ─ F3  What customers really think
                   └─ split: Opened Email = 0 since F1? → YES: property FTL_unopened = true""",
        emails=[
            dict(file="f1-titanium-vs-nonstick", delay="14 dagen na trigger, 09:00", subject="Us vs the pan in your drawer",
                 preview="Why titanium hits differently.", tag="Education 1 of 3",
                 headline="Non-stick vs titanium, honestly.",
                 body=["<table role='presentation' width='100%' style='font-size:15px; line-height:1.5; margin-bottom:16px;'><tr><td style='padding:8px; border-bottom:1px solid #e8e3da;'></td><td style='padding:8px; border-bottom:1px solid #e8e3da;'><b>Non-stick</b></td><td style='padding:8px; border-bottom:1px solid #e8e3da;'><b>Siraat titanium</b></td></tr><tr><td style='padding:8px;'>Surface</td><td style='padding:8px;'>Coating that wears off</td><td style='padding:8px;'>The metal itself</td></tr><tr><td style='padding:8px;'>Metal utensils</td><td style='padding:8px;'>No</td><td style='padding:8px;'>Yes</td></tr><tr><td style='padding:8px;'>Lifespan</td><td style='padding:8px;'>1 to 2 years</td><td style='padding:8px;'>Decades</td></tr><tr><td style='padding:8px;'>Chemicals</td><td style='padding:8px;'>PFAS or ceramic sol-gel</td><td style='padding:8px;'>None</td></tr></table>",
                       p("Cook on it for 100 days. If it loses, send it back.")],
                 product="", cta=("See the pans", SHOP_ALL), proof="", signoff="",
                 incentive="Geen", smart="AAN", filters="Placed Order = 0 since start", notes=""),
            dict(file="f2-care-faq", delay="3 dagen, 09:00", subject="Unlocking the non-stick effect",
                 preview="Stick-free every time, in three steps.", tag="Education 2 of 3",
                 headline="Three steps. That's the whole technique.",
                 body=["<ol style='font-size:16px; line-height:1.7; margin:0 0 16px 20px; padding:0;'><li>Heat the dry pan on medium for about a minute.</li><li>Add a thin film of oil and let it shimmer.</li><li>Add food. Don't move it for the first 30 seconds.</li></ol>",
                       p("Clean it in the dishwasher or with a sponge. No seasoning, no special brushes.")],
                 product="", cta=("Read the full care guide", f"{SITE}/pages/care"), proof="", signoff="",
                 incentive="Geen", smart="AAN", filters="Placed Order = 0 since start", notes=""),
            dict(file="f3-real-reviews", delay="4 dagen, 09:00", subject="What our customers really think",
                 preview="Real reviews inside.", tag="Education 3 of 3",
                 headline="100,000 customers. Here is what they say.",
                 body=[p("We could tell you it's the last pan you'll buy. These people already did.")],
                 product=BESTSELLERS, cta=("Shop the pans", SHOP_ALL), proof=REVIEWS, signoff="",
                 incentive="Geen", smart="AAN", filters="Placed Order = 0 since start", notes="Laatste mail. Daarna property-update voor sunset."),
        ],
    ),
    # ------------------------------------------------------------------ 6
    dict(
        slug="06-sunset",
        name="Sunset Flow (met echte suppressie)",
        replaces="EB | Sunset Flow | 5/15/25 (S7V4a7, zet alleen een property)",
        trigger="Added to Segment: Sunset Segment (XY4NVp)",
        trigger_filters="Segment aanpassen: opens met machine_open = false, 90 dagen geen klik, geen non-machine open, geen Active on Site, geen order",
        profile_filters=["Placed Order = 0 in the last 90 days"],
        settings=[
            "Smart sending AAN",
            "Laatste stap is 'Unsubscribe profile from email' (Klaviyo flow action), niet alleen een property",
            "Wie opent of klikt: property Re_engaged = true en exit",
        ],
        tree="""Trigger: Added to Segment "Sunset Segment"
│
├─ S1  Should we keep emailing you?
├─ [5 dagen, 09:00]
│    └─ split: Opened or Clicked since start?
│         ├─ YES → property Re_engaged = true → exit
│         └─ NO  → S2  This is our last email
└─ [5 dagen]
     └─ split: Opened or Clicked since start?
          ├─ YES → property Re_engaged = true → exit
          └─ NO  → Unsubscribe profile from email marketing""",
        emails=[
            dict(file="s1-staying-or-going", delay="Direct", subject="Should we keep emailing you?",
                 preview="One click keeps you on the list. No click and we stop.", tag="Sunset 1 of 2",
                 headline="We'd rather ask than keep guessing.",
                 body=[p("Hi {{ first_name|default:'there' }}, you haven't opened our emails in a while. That's fine. Click below to stay on the list, or do nothing and we'll stop emailing you in 10 days.")],
                 product="", cta=("Keep me on the list", f"{SITE}/?utm_source=klaviyo&utm_campaign=sunset"), proof="", signoff="",
                 incentive="Geen", smart="AAN", filters="Placed Order = 0 in last 90 days", notes=""),
            dict(file="s2-last-email", delay="5 dagen, 09:00", subject="This is our last email",
                 preview="Unless you click, we'll stop here.", tag="Sunset 2 of 2",
                 headline="Last one from us.",
                 body=[p("No hard feelings. If you want to keep hearing from us (new pans, the occasional sale), click once. Otherwise this is goodbye, and you can always come back at siraatskitchen.com.")],
                 product="", cta=("Keep me on the list", f"{SITE}/?utm_source=klaviyo&utm_campaign=sunset-last"), proof="", signoff="",
                 incentive="Geen", smart="AAN", filters="Opened Email = 0 AND Clicked Email = 0 since start", notes="Daarna: niet geopend → unsubscribe."),
        ],
    ),
    # ------------------------------------------------------------------ 7
    dict(
        slug="07-post-purchase",
        name="Post Purchase (met holiday next-purchase gift card)",
        replaces="EB | Post Purchase Flow | 4/6/2026 (RL3TU6)",
        trigger="Placed Order (Shopify, RSNxYV)",
        trigger_filters="Geen",
        profile_filters=["Geen (iedere order)"],
        settings=[
            "Smart sending UIT (transactioneel karakter)",
            "'On its way' hoort in de Pan Education / shipping flow op het event Shipment In Transit, niet op een vaste dag",
            "Holiday-tak: trigger filter op orderdatum tussen 20 nov en 31 dec (of gebruik een tijdelijke conditional split op 'Placed Order in last 1 day' tijdens die periode)",
        ],
        tree="""Trigger: Placed Order
│
└─ Conditional split: Placed Order count > 1 (all time)?
     ├─ YES (repeat) ─ [2 min] ─ R1  Welcome back
     └─ NO (first order)
          ├─ [2 min] ─ P1  We've got your order
          ├─ [1 dag, 09:30] ─ P2  A note from Benjamin
          ├─ [2 dagen, 09:30] ─ P3  Get ready to cook (3-step method, 100-day trial)
          └─ Conditional split: order placed between 20 Nov and 31 Dec?
               ├─ NO  → exit
               └─ YES ─ [7 dagen] ─ P4  Your $25 for January (JAN25, 1 to 15 Jan)
                              (JAN50 voor orders > $400 via extra split)""",
        emails=[
            dict(file="p1-weve-got-your-order", delay="2 min na order", subject="We've got your order",
                 preview="Order {{ event.extra.order_number|default:'' }} is confirmed. Here's what happens next.", tag="Order 1 of 4",
                 headline="Thank you. Your order is in.",
                 body=[p("Hi {{ first_name|default:'there' }}, your order is confirmed and heading to the warehouse. You'll get a tracking email the moment it ships, usually within 1 to 2 business days."),
                       p("While you wait: the first cook on titanium is different from non-stick. Mail 3 shows you exactly how.")],
                 product=CHECKOUT_ITEMS, cta=("View my order", "{{ event.extra.order_status_url|default:'https://siraatskitchen.com/account' }}"), proof="", signoff="",
                 incentive="Geen", smart="UIT", filters="Geen", notes="Order-items blok werkt met event.extra.line_items van Placed Order."),
            dict(file="p2-founder-note", delay="1 dag, 09:30", subject="A note from Benjamin",
                 preview="Why your pan has dents in it.", tag="Order 2 of 4",
                 headline="Those dimples are the point.",
                 body=[p("Every Siraat pan is hammered by hand. The dimples aren't decoration: they hold a thin film of oil exactly where the food sits, which is why a bare titanium surface releases like a coated one, without the coating."),
                       p("If anything about your order isn't right, reply to this email. It lands with a human.")],
                 product="", cta=("See how it's made", f"{SITE}/pages/about"), proof="", signoff=FOUNDER_SIGNOFF,
                 incentive="Geen", smart="UIT", filters="Geen", notes=""),
            dict(file="p3-get-ready-to-cook", delay="2 dagen, 09:30", subject="Get ready to cook: the 3-step method",
                 preview="Heat, oil, food. In that order.", tag="Order 3 of 4",
                 headline="Before the first egg, read this.",
                 body=["<ol style='font-size:16px; line-height:1.7; margin:0 0 16px 20px; padding:0;'><li>Heat the dry pan on medium for about a minute.</li><li>Add a thin film of oil and let it shimmer.</li><li>Add food. Don't move it for the first 30 seconds.</li></ol>",
                       p("Metal utensils and the dishwasher are fine. And you have 100 days: if it's not the best pan you own, send it back.")],
                 product="", cta=("Read the full care guide", f"{SITE}/pages/care"), proof="", signoff="",
                 incentive="Geen", smart="UIT", filters="Geen", notes=""),
            dict(file="p4-your-25-for-january", delay="7 dagen (alleen orders 20 nov tot 31 dec)", subject="{{ first_name|default:'Hey' }}, we set aside $25 for you in January",
                 preview="A $25 gift card, valid 1 to 15 January.", tag="Order 4 of 4 · Holiday",
                 headline="$25 for your next order, in January.",
                 body=[p("Thanks for ordering with us this season. We've put a $25 gift card on your account for your next order. It works from 1 to 15 January, on anything in the shop, with no minimum beyond $99."),
                       code_block("{% coupon_code 'JAN25' %}", "Your January gift card, valid 1 to 15 Jan"),
                       p("Save this email. We'll remind you once on 2 January, and that's it.")],
                 product=BESTSELLERS, cta=("See what's new", SHOP_ALL), proof="", signoff="",
                 incentive="JAN25 uniek, $25 vast, min. $99, geldig 1 tot 15 jan (JAN50 bij order > $400)", smart="UIT", filters="Placed Order between 20 Nov and 31 Dec", notes="Campagne op 2 januari naar segment 'Holiday buyers zonder herhaalorder' als herinnering."),
            dict(file="r1-welcome-back", delay="2 min na order (repeat buyers)", subject="Welcome back",
                 preview="Thank you for ordering again.", tag="Repeat order",
                 headline="Good to see you again.",
                 body=[p("Hi {{ first_name|default:'there' }}, your order is confirmed. You know the drill by now, so we'll keep this short: tracking follows as soon as it ships."),
                       p("Reply to this email if you'd like us to add anything to the box.")],
                 product=CHECKOUT_ITEMS, cta=("View my order", "{{ event.extra.order_status_url|default:'https://siraatskitchen.com/account' }}"), proof="", signoff="",
                 incentive="Geen", smart="UIT", filters="Placed Order count > 1", notes=""),
        ],
    ),
    # ------------------------------------------------------------------ 8
    dict(
        slug="08-winback",
        name="Customer Winback (met herhaalcheck)",
        replaces="EB | Customer Winback | 5/8/25 (UEfh4h)",
        trigger="Placed Order (Shopify)",
        trigger_filters="Geen",
        profile_filters=[
            "Placed Order = 0 times in the last 60 days (gecontroleerd op elke mail, ontbreekt nu)",
            "Has not been in this flow in the last 90 days",
        ],
        settings=["Smart sending AAN", "Geen random sample split"],
        tree="""Trigger: Placed Order
│
└─ [60 dagen, 09:00]
    └─ split: Placed Order = 0 in last 60 days?
         ├─ NO  → exit
         └─ YES
              ├─ WB1  What's new since your last order
              ├─ [3 dagen, 09:00] ─ WB2  10% off your next pan (WINBACK10)
              └─ [2 dagen, 09:00] ─ WB3  10% expires tonight""",
        emails=[
            dict(file="wb1-whats-new", delay="60 dagen na order, 09:00", subject="What's new since your last order",
                 preview="The pieces customers add second.", tag="Winback 1 of 3",
                 headline="Two months in. How's the pan?",
                 body=[p("Hi {{ first_name|default:'there' }}, it's been about two months since your order. By now the pan should be the one you reach for. Here's what people add next.")],
                 product=BESTSELLERS, cta=("See what's new", SHOP_ALL), proof="", signoff="",
                 incentive="Geen", smart="AAN", filters="Placed Order = 0 in last 60 days", notes=""),
            dict(file="wb2-winback10", delay="3 dagen, 09:00", subject="10% off your next pan",
                 preview="A thank-you for being a customer. Valid 5 days.", tag="Winback 2 of 3",
                 headline="10% off, because you've cooked with us before.",
                 body=[p("Here's 10% off your next order, valid for 5 days. Most customers go for a second size or the wok."),
                       code_block("{% coupon_code 'WINBACK10' %}", "Your 10% code, 5 days")],
                 product=BESTSELLERS, cta=("Use my 10%", SHOP_ALL), proof="", signoff="",
                 incentive="WINBACK10 uniek, 10%, 5 dagen", smart="AAN", filters="Placed Order = 0 in last 60 days", notes=""),
            dict(file="wb3-expires", delay="2 dagen, 09:00", subject="Your 10% expires tonight",
                 preview="Last chance for the returning-customer code.", tag="Winback 3 of 3",
                 headline="Last day for your 10%.",
                 body=[p("Your returning-customer code ends at midnight."), code_block("{% coupon_code 'WINBACK10' %}", "10% off, ends tonight")],
                 product="", cta=("Shop now", SHOP_ALL), proof="", signoff="",
                 incentive="WINBACK10", smart="AAN", filters="Placed Order = 0 in last 60 days AND Opened Email ≥ 1 since start", notes=""),
        ],
    ),
    # ------------------------------------------------------------------ 9
    dict(
        slug="09-gift-card",
        name="Gift Card flows en december-campagnes",
        replaces="EB - E-Gift Card (UYALJ8, 1 transactionele mail)",
        trigger="Flow A: Placed Order where Items contains 'E-Gift Card'. Campagnes: engaged 90 dagen, 15 tot 24 december",
        trigger_filters="Flow A: Ordered Product ProductID = 12245272494420",
        profile_filters=["Flow A: geen"],
        settings=[
            "Flow A is transactioneel (G1) plus één marketingmail (G2) met smart sending AAN",
            "Campagnes GC1 tot GC3: audience Engaged 90 Days, exclusies Unengaged 180, Sunset, For Suppression, bought in last 7 days",
            "Shopify stuurt de gift card zelf naar de ontvanger; Klaviyo mailt alleen de koper",
        ],
        tree="""Flow A: Placed Order with E-Gift Card
│
├─ [2 min] ─ G1  Thanks for gifting Siraat's Kitchen (hoe het werkt)
└─ [14 dagen, 09:00] ─ G2  Has it been opened yet? (herinnering + pan-tips om door te sturen)

Campagnes (geen flow):
├─ 15 dec ─ GC1  Too late to ship? A gift card arrives in a minute
├─ 20 dec ─ GC2  The gift that arrives today (last ship date voorbij)
└─ 23 dec ─ GC3  Christmas Eve: still time for a Siraat gift card""",
        emails=[
            dict(file="g1-thanks-for-gifting", delay="2 min na order (transactioneel)", subject="Thanks for gifting Siraat's Kitchen",
                 preview="Here's how your gift card works.", tag="Gift card · buyer",
                 headline="Your gift card is on its way.",
                 body=[p("Hi {{ first_name|default:'there' }}, thank you. The gift card is sent by email to the recipient you entered at checkout (or to you, if you'd rather hand it over yourself). It never expires and works on anything in the shop."),
                       p("Tip: forward them our 3-step guide when they pick a pan. The first egg is the moment they get it.")],
                 product="", cta=("Read the care guide", f"{SITE}/pages/care"), proof="", signoff="",
                 incentive="Geen", smart="UIT (transactioneel)", filters="Geen", notes=""),
            dict(file="g2-opened-yet", delay="14 dagen, 09:00", subject="Has your gift been opened yet?",
                 preview="A gentle reminder, plus the pan most people choose.", tag="Gift card · reminder",
                 headline="Two weeks in. Have they picked a pan?",
                 body=[p("Gift cards get lost in inboxes. If yours hasn't been used yet, a quick nudge usually does it. Most recipients choose the Pan Pro Standard, so we've put it below in case it helps.")],
                 product=BESTSELLERS, cta=("Resend my gift card", f"{SITE}/account"), proof="", signoff="",
                 incentive="Geen", smart="AAN", filters="Geen (Klaviyo ziet verzilvering niet)", notes="'Resend' linkt naar het account; Shopify kan een gift card opnieuw mailen vanuit de admin."),
            dict(file="gc1-too-late-to-ship", delay="Campagne 15 dec", subject="Too late to ship? A gift card arrives in a minute",
                 preview="$25 to $200, delivered by email, never expires.", tag="Campaign · 15 Dec",
                 headline="The gift that arrives in a minute.",
                 body=[p("Shipping cut-offs are closing in. A Siraat gift card is emailed straight to them (or to you) the moment you order, and they pick the pan they actually want."),
                       p("Available from $25 to $200. Add a message, choose the delivery date, done.")],
                 product="", cta=("Send a gift card", GIFT_CARD), proof=REVIEWS, signoff="",
                 incentive="Geen", smart="AAN", filters="Engaged 90 Days, excl. bought in last 7 days", notes="Voeg een $150-variant toe met de framing 'Gift a pan'."),
            dict(file="gc2-arrives-today", delay="Campagne 20 dec", subject="The gift that arrives today",
                 preview="Last ship date has passed. This one is instant.", tag="Campaign · 20 Dec",
                 headline="Missed the shipping cut-off? This one is instant.",
                 body=[p("Orders placed now won't make it under the tree, but a gift card will. Pick an amount, write a note, and it lands in their inbox today, or on the date you choose.")],
                 product="", cta=("Send a gift card", GIFT_CARD), proof="", signoff="",
                 incentive="Geen", smart="AAN", filters="Engaged 90 Days, excl. bought gift card in last 7 days", notes=""),
            dict(file="gc3-christmas-eve", delay="Campagne 23 dec", subject="Christmas Eve plan: a Siraat gift card",
                 preview="Delivered by email in a minute. Schedule it for the morning.", tag="Campaign · 23 Dec",
                 headline="Still time. Just.",
                 body=[p("A Siraat gift card is delivered by email in under a minute, or scheduled for Christmas morning. $25 to $200, never expires, and they choose the pan."),],
                 product="", cta=("Send it now", GIFT_CARD), proof="", signoff="",
                 incentive="Geen", smart="AAN", filters="Engaged 30 Days", notes="Korte mail, mobiel eerst."),
        ],
    ),
]

# ----------------------------------------------------------------------------
# Rendering
# ----------------------------------------------------------------------------


def render_email(flow: dict, e: dict) -> str:
    body = "".join(e["body"])
    cta_html = cta(*e["cta"]) if e.get("cta") else ""
    hero_key = HERO.get(e["file"], "standard")
    hero = hero_key if hero_key.startswith("{{") else shop_img(hero_key)
    feat_key = FEATURE.get(e["file"])
    feature = ""
    if feat_key:
        feature = f'  <tr><td><a href="{e["cta"][1]}"><img src="{shop_img(feat_key)}" width="600" alt=""></a></td></tr>\n'
    return BASE.format(
        title=html.escape(re.sub(r"{{.*?}}", "", e["subject"]).strip(" ,") or flow["name"]),
        preview=e["preview"],
        headline=e["headline"],
        headline_alt=html.escape(e["headline"], quote=True),
        body=body,
        product=e.get("product", ""),
        cta=cta_html,
        cta_url=e["cta"][1] if e.get("cta") else SITE,
        feature=feature,
        proof=e.get("proof", ""),
        signoff=e.get("signoff", ""),
        hero=hero,
        site=SITE,
        logo=IMG["logo"], nav_shop=IMG["nav_shop"], nav_about=IMG["nav_about"], nav_faq=IMG["nav_faq"],
        trust_gif=IMG["trust_gif"], follow=IMG["follow"], ig=IMG["ig"], fb=IMG["fb"],
        siraat_footer=IMG["siraat_footer"], privacy=IMG["privacy"], terms=IMG["terms"],
    )


def render_flow_md(flow: dict) -> str:
    out = [f"# {flow['name']}", ""]
    out.append(f"Vervangt: {flow['replaces']}")
    out.append("")
    out.append(f"**Trigger:** {flow['trigger']}  ")
    out.append(f"**Trigger filters:** {flow['trigger_filters']}  ")
    out.append("**Profile filters:**")
    for f in flow["profile_filters"]:
        out.append(f"- {f}")
    out.append("")
    out.append("**Instellingen:**")
    for s in flow["settings"]:
        out.append(f"- {s}")
    out.append("")
    out.append("## Vertakking")
    out.append("")
    out.append("```")
    out.append(flow["tree"])
    out.append("```")
    out.append("")
    out.append("## Berichten")
    out.append("")
    out.append("| # | Bestand | Wanneer | Onderwerp | Preview | Incentive | Filter op bericht | Smart sending | Notities |")
    out.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for i, e in enumerate(flow["emails"], 1):
        rel = f"../emails/{flow['slug']}/{e['file']}.html"
        out.append(
            f"| {i} | [{e['file']}.html]({rel}) | {e['delay']} | {e['subject']} | {e['preview']} | {e['incentive']} | {e['filters']} | {e['smart']} | {e.get('notes','')} |"
        )
    if flow.get("sms"):
        out.append("")
        out.append("## Sms")
        out.append("")
        for name, when, text in flow["sms"]:
            out.append(f"- **{name}** ({when}): `{text}`")
    out.append("")
    return "\n".join(out)


def render_index(flows: list[dict]) -> str:
    cards = []
    for fl in flows:
        rows = "".join(
            f"<li><a href='emails/{fl['slug']}/{e['file']}.html' target='preview'>{html.escape(e['file'])}</a> "
            f"<span class='muted'>{html.escape(e['delay'])}</span><br><span class='subj'>{html.escape(e['subject'])}</span></li>"
            for e in fl["emails"]
        )
        cards.append(
            f"<section class='flow'><h2>{html.escape(fl['name'])}</h2>"
            f"<p class='muted'>Trigger: {html.escape(fl['trigger'])} &middot; <a href='flows/{fl['slug']}.md'>spec</a></p>"
            f"<pre>{html.escape(fl['tree'])}</pre><ul>{rows}</ul></section>"
        )
    return f"""<!DOCTYPE html><html lang="nl"><head><meta charset="utf-8"><title>Siraat's Kitchen · Klaviyo flows</title>
<style>
body{{margin:0;font-family:Helvetica,Arial,sans-serif;color:#1f1f1f;background:#f4f1ec;display:grid;grid-template-columns:460px 1fr;height:100vh}}
nav{{overflow:auto;padding:20px;border-right:1px solid #ddd;background:#fff}}
iframe{{width:100%;height:100%;border:0;background:#f4f1ec}}
h1{{font-size:18px;letter-spacing:2px}} h2{{font-size:15px;margin:24px 0 4px}}
pre{{font-size:11px;line-height:1.35;background:#f9f7f3;padding:10px;border-radius:6px;overflow:auto}}
ul{{list-style:none;padding:0;margin:0}} li{{padding:6px 0;border-top:1px solid #eee;font-size:13px}}
.muted{{color:#777;font-size:11px}} .subj{{color:#444;font-size:12px}}
a{{color:#1f1f1f}}
</style></head><body>
<nav><h1>KLAVIYO FLOWS</h1><p class="muted">Klik een mail om hem rechts te bekijken. Specs per flow staan in <code>flows/</code>.</p>{''.join(cards)}</nav>
<iframe name="preview" src="emails/{flows[0]['slug']}/{flows[0]['emails'][0]['file']}.html"></iframe>
</body></html>"""


def main() -> None:
    (ROOT / "flows").mkdir(exist_ok=True)
    (ROOT / "emails").mkdir(exist_ok=True)
    n = 0
    for fl in FLOWS:
        (ROOT / "flows" / f"{fl['slug']}.md").write_text(render_flow_md(fl), encoding="utf-8")
        d = ROOT / "emails" / fl["slug"]
        d.mkdir(exist_ok=True)
        for e in fl["emails"]:
            (d / f"{e['file']}.html").write_text(render_email(fl, e), encoding="utf-8")
            n += 1
    (ROOT / "index.html").write_text(render_index(FLOWS), encoding="utf-8")
    print(f"{len(FLOWS)} flows, {n} emails written under {ROOT}")


if __name__ == "__main__":
    main()
