#!/usr/bin/env python3
"""Bouwt de drie Shopify-orderbevestigingen (variant-a/b/c.liquid).

Gebruik: python3 -I _tools/build.py   (vanuit de map shopify-order-confirmation)
Daarna:  node _tools/render.js        (previews + PNG's)

De .liquid-bestanden zijn de bron die in Shopify geplakt wordt
(Settings > Notifications > Order confirmation > Edit code).
Alles wat Floris moet invullen staat bovenaan elke .liquid als assign.
"""
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

K = "https://cdn.klaviyomail.com/company/TdtTzz/images/"
S = "https://cdn.shopify.com/s/files/1/0907/0877/1156/files/"
IMG = {
    "logo_black": K + "ae4dfc27-1e05-481a-90b6-f6467bc3db78.png",   # brand/logo/lockup/siraat-lockup-black-email.png
    "logo_white": K + "c8e347f7-34c0-42d9-8ddc-32949f48155e.png",   # lockup wit op #282828 (vaste footer)
    "fb": K + "17c00632-f9db-4dcd-a27e-bf0adc4987da.png",
    "ig": K + "6b905e47-7bf9-4aec-a63b-0538ecc6bd60.png",
    "gift_mystery": K + "c97cf7a9-cccf-4472-a592-d49747b6d6a7.jpeg",
    "gift_shipping": K + "fc1878e8-1cc0-4699-8f62-1110afb1750e.jpeg",
    "gift_ebook": K + "3fab7ff2-1993-48d2-8567-d9f3d0ce04dd.jpeg",
    "gift_cookbook": K + "dabf0446-a5d7-49ae-87f8-672e5692bf5b.jpeg",
    "gift_filter": K + "a6aec8e7-f289-424e-ab60-689f1ae85c39.jpeg",
    "icon_returns": K + "543e925f-fed4-4f3b-a811-a70761a13542.png",
    "icon_warranty": K + "e39ac58c-e419-47b6-ab84-b2cd8185e946.png",
    "icon_customers": K + "c2ae0306-f0fa-48e5-817c-6b41e95f16aa.png",
    "icon_pfas": K + "454277c9-b6fc-4d54-974d-8cebc9112ec1.png",
    "icon_nocoat": K + "2638aa47-083f-4985-a610-4d5c72b7429c.png",
    "hero_b": S + "siraat-titanium-hammered-deep-pan-10-family-dinner.webp?width=1200&height=800&crop=center&format=pjpg",
}

INK = "#282828"; CREAM = "#F8F7F2"; SAND = "#ECE7DD"; BRICK = "#AC3B19"
GREY = "#727272"; LEGAL = "#9A948B"; PAPER = "#FFFFFF"
F = "font-family:Inter,Arial,Helvetica,sans-serif;"
SERIF = "font-family:'Instrument Serif','Times New Roman',Times,serif;font-style:italic;font-weight:400;"

# ---------------------------------------------------------------- setup
SETUP = """{%- comment -%}
  Siraat order confirmation, VARIANT_NAME.
  Source: klaviyo/templates/v3/shopify-order-confirmation (built by _tools/build.py). Do not edit in Shopify only:
  change the source, rebuild, paste again.
  ===== FLORIS: fill in or confirm these values =====
{%- endcomment -%}
{%- assign sk_portal_url = 'https://siraatskitchen.com/a/loop_subscriptions/customer' -%}{%- comment -%} subscription portal: Loop (LOG 30 Oct) or Recharge customer portal link. One click, no login if possible. {%- endcomment -%}
{%- assign sk_support = 'support@siraatskitchen.com' -%}
{%- assign sk_ebook_url = 'https://delivery.shopifyapps.com/-/396da74b7735ff7f/6d8678add81ad2ad' -%}
{%- assign sk_cookbook_url = '' -%}{%- comment -%} empty = 'link arrives by email' {%- endcomment -%}
{%- assign sk_days_us = '3 to 10' -%}{%- comment -%} Fulfilled to Delivered, US: median 7.1 d, p90 12.5 d (Klaviyo), Ecomflow US 9.1 d {%- endcomment -%}
{%- assign sk_days_int = '6 to 14' -%}{%- comment -%} shipping policy: 6-10 days, Ireland/Denmark 8-14 {%- endcomment -%}
{%- assign sk_cancel_window = '1 hour' -%}{%- comment -%} shipping policy: cancellation request within 1 hour {%- endcomment -%}
{%- comment -%} ===== end of settings ===== {%- endcomment -%}
{%- assign sk_cur = presentment_currency | default: currency | default: 'USD' | upcase -%}
{%- assign sk_country = shipping_address.country_code | default: billing_address.country_code | default: 'US' -%}
{%- if sk_country == 'US' -%}{%- assign sk_days = sk_days_us -%}{%- else -%}{%- assign sk_days = sk_days_int -%}{%- endif -%}
{%- assign sk_paid = 0 -%}{%- assign sk_gifts = 0 -%}{%- assign sk_subs = 0 -%}{%- assign sk_ship = 0 -%}
{%- assign sk_first = '' -%}{%- assign sk_sep = '' -%}
{%- for line in subtotal_line_items -%}
  {%- assign t = line.title | downcase -%}
  {%- assign kind = 'item' -%}
  {%- if line.selling_plan_allocation -%}{%- assign kind = 'sub' -%}
  {%- elsif line.final_line_price == 0 -%}
    {%- if t contains 'mystery' -%}{%- assign kind = 'mystery' -%}
    {%- elsif t contains 'shipping' -%}{%- assign kind = 'shipping' -%}
    {%- elsif t contains 'cookbook' -%}{%- assign kind = 'cookbook' -%}
    {%- elsif t contains 'book' or t contains 'guide' -%}{%- assign kind = 'ebook' -%}
    {%- elsif t contains 'filter' or t contains 'draw' -%}{%- assign kind = 'filter' -%}
    {%- else -%}{%- assign kind = 'freebie' -%}{%- endif -%}
  {%- endif -%}
  {%- if kind == 'sub' -%}{%- assign sk_subs = sk_subs | plus: 1 -%}
  {%- elsif kind == 'item' -%}{%- assign sk_paid = sk_paid | plus: 1 -%}{%- if sk_first == '' -%}{%- assign sk_first = line.title -%}{%- endif -%}
  {%- else -%}{%- assign sk_gifts = sk_gifts | plus: 1 -%}{%- endif -%}
  {%- if line.requires_shipping and kind != 'shipping' and kind != 'ebook' and kind != 'cookbook' and kind != 'filter' -%}
    {%- assign sk_ship = sk_ship | plus: 1 -%}
    {%- if kind != 'item' -%}{%- assign sk_short = line.title -%}
      {%- if kind == 'sub' -%}{%- assign sk_short = 'dishwasher sheets' -%}{%- if t contains 'sheet' -%}{%- else -%}{%- assign sk_short = line.title -%}{%- endif -%}{%- endif -%}
      {%- if kind == 'mystery' -%}{%- assign sk_short = 'mystery gift' -%}{%- endif -%}
      {%- assign sk_sep = sk_sep | append: '|' | append: sk_short -%}
    {%- elsif t contains 'lid' -%}{%- assign sk_sep = sk_sep | append: '|lid' -%}{%- endif -%}
  {%- endif -%}
{%- endfor -%}
{%- assign sk_sep_list = sk_sep | remove_first: '|' | split: '|' -%}
{%- assign sk_sep_text = '' -%}
{%- for s in sk_sep_list -%}
  {%- if forloop.first -%}{%- assign sk_sep_text = s | capitalize -%}
  {%- elsif forloop.last -%}{%- assign sk_sep_text = sk_sep_text | append: ' and ' | append: s -%}
  {%- else -%}{%- assign sk_sep_text = sk_sep_text | append: ', ' | append: s -%}{%- endif -%}
{%- endfor -%}
{%- assign sk_more = sk_paid | minus: 1 -%}
"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light only">
<meta name="supported-color-schemes" content="light only">
<title>Order {{ order_name }} confirmed</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&family=Inter:wght@400;500;600&display=swap');
  body{margin:0;padding:0;background:#FFFFFF;-webkit-text-size-adjust:100%;}
  table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0;}
  img{border:0;display:block;line-height:100%;outline:none;text-decoration:none;}
  a{color:#AC3B19;}
  @media only screen and (max-width:620px){
    .w{width:100%!important;}
    .pad{padding-left:22px!important;padding-right:22px!important;}
    .h1{font-size:36px!important;line-height:40px!important;}
    .h2{font-size:28px!important;line-height:32px!important;}
    .btnw{width:100%!important;}
    .hidem{display:none!important;}
    .cardin{padding-left:16px!important;padding-right:16px!important;}
    .ck-l{width:92px!important;}
  }
  @media only screen and (max-width:480px){
    .ic3{display:block!important;width:100%!important;padding:0 0 14px 0!important;}
    .pill{display:inline-block!important;margin:0 4px 8px 0!important;}
  }
</style>
</head>
<body style="margin:0;padding:0;background:#FFFFFF;">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:#FFFFFF;">PREHEADER&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;&#8204;&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;"><tr><td align="center" style="padding:8px 0 0 0;">
<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="#F8F7F2" style="width:600px;background-color:#F8F7F2;">
"""

HEADER = f"""<!-- HEADER (look van partials/header.html, lockup zwart op licht) -->
<tr><td bgcolor="{CREAM}" class="pad" style="padding:18px 36px;background-color:{CREAM};border-bottom:1px solid {SAND};">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
    <td valign="middle"><a href="https://siraatskitchen.com"><img src="{IMG['logo_black']}" width="150" alt="Siraat" style="display:block;width:150px;height:auto;border:0;"></a></td>
    <td valign="middle" align="right" style="{F}font-size:11px;line-height:18px;letter-spacing:1.5px;font-weight:600;color:{INK};">ORDER {{{{ order_name }}}}</td>
  </tr></table>
</td></tr>
"""

FOOTER = f"""<!-- FOOTER (look van partials/footer.html; transactioneel, dus zonder afmeldlinks) -->
<tr><td class="pad" bgcolor="{INK}" style="padding:38px 40px 30px 40px;background-color:{INK};">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{INK}" style="background-color:{INK};">
  <tr><td bgcolor="{INK}" style="background-color:{INK};"><a href="https://siraatskitchen.com"><img src="{IMG['logo_white']}" width="190" alt="Siraat" style="display:block;width:190px;height:auto;border:0;"></a></td></tr>
  <tr><td bgcolor="{INK}" style="background-color:{INK};{F}font-size:13px;line-height:18px;letter-spacing:2px;font-weight:600;color:#BDB8B0;padding-top:14px;">NON-TOXIC COOKWARE &middot; BUILT FOR LIFE</td></tr>
  <tr><td bgcolor="{INK}" style="background-color:{INK};padding-top:28px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{INK}" style="background-color:{INK};">
    <tr><td bgcolor="{INK}" style="background-color:{INK};border-top:1px solid #5A5856;padding:15px 4px;"><a href="{{{{ order_status_url }}}}" style="{F}font-size:14px;letter-spacing:2px;font-weight:600;color:#F2F2F2;text-decoration:none;">MY ORDER &amp; TRACKING &nbsp;&rarr;</a></td></tr>
    <tr><td bgcolor="{INK}" style="background-color:{INK};border-top:1px solid #5A5856;padding:15px 4px;"><a href="https://siraatskitchen.com/pages/warranty" style="{F}font-size:14px;letter-spacing:2px;font-weight:600;color:#F2F2F2;text-decoration:none;">RETURNS &amp; WARRANTY &nbsp;&rarr;</a></td></tr>
    <tr><td bgcolor="{INK}" style="background-color:{INK};border-top:1px solid #5A5856;border-bottom:1px solid #5A5856;padding:15px 4px;"><a href="https://siraatskitchen.com/pages/third-party-testing" style="{F}font-size:14px;letter-spacing:2px;font-weight:600;color:#F2F2F2;text-decoration:none;">LAB RESULTS &nbsp;&rarr;</a></td></tr>
  </table>
  </td></tr>
  <tr><td align="center" bgcolor="{INK}" style="background-color:{INK};padding:28px 0 22px 0;">
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" bgcolor="{INK}" style="background-color:{INK};margin:0 auto;"><tr>
    <td bgcolor="{INK}" style="background-color:{INK};padding:0 16px;"><a href="https://www.facebook.com/people/SiraatsKitchen/61567176126958/"><img src="{IMG['fb']}" width="32" alt="Facebook" style="width:32px;height:32px;"></a></td>
    <td bgcolor="{INK}" style="background-color:{INK};padding:0 16px;"><a href="https://www.instagram.com/siraatskitchen"><img src="{IMG['ig']}" width="32" alt="Instagram" style="width:32px;height:32px;"></a></td>
  </tr></table>
  </td></tr>
  <tr><td align="center" bgcolor="{INK}" style="background-color:{INK};{F}font-size:12px;line-height:19px;color:#BDB8B0;text-align:center;">
    Free shipping on all orders &middot; 30-day returns &middot; 75-year warranty<br><br>
    Questions? Reply to this email or write to <a href="mailto:{{{{ sk_support }}}}" style="color:#F2F2F2;">{{{{ sk_support }}}}</a><br>
    {{{{ shop.name }}}} &middot; siraatskitchen.com
  </td></tr>
</table>
</td></tr>
</table>
</td></tr></table>
</body>
</html>
"""

def eyebrow(txt, pad="36px 44px 0 44px", align="left"):
    return f"""<tr><td class="pad" align="{align}" style="padding:{pad};{F}font-size:11px;line-height:16px;letter-spacing:2px;font-weight:600;color:{BRICK};text-align:{align};">{txt}</td></tr>\n"""

def h2(txt, pad="8px 44px 0 44px", align="left"):
    return f"""<tr><td class="pad h2" align="{align}" style="padding:{pad};{SERIF}font-size:32px;line-height:36px;color:{INK};text-align:{align};">{txt}</td></tr>\n"""

def para(txt, pad="12px 44px 0 44px", size=15, color=INK, align="left"):
    lh = int(size * 1.6)
    return f"""<tr><td class="pad" align="{align}" style="padding:{pad};{F}font-size:{size}px;line-height:{lh}px;color:{color};text-align:{align};">{txt}</td></tr>\n"""

def button(label, url, pad="24px 44px 0 44px", sub=None):
    s = f"""<tr><td class="pad" align="center" style="padding:{pad};">
  <table role="presentation" class="btnw" width="340" cellpadding="0" cellspacing="0" border="0" style="width:340px;"><tr><td align="center" bgcolor="{INK}" style="background-color:{INK};border-radius:3px;">
    <a href="{url}" style="display:block;padding:18px 20px;{F}font-size:15px;line-height:18px;font-weight:600;letter-spacing:1.5px;color:#FFFFFF;text-decoration:none;text-transform:uppercase;">{label} &rarr;</a>
  </td></tr></table>
</td></tr>\n"""
    if sub:
        s += f"""<tr><td class="pad" align="center" style="padding:10px 44px 0 44px;{F}font-size:12px;line-height:18px;color:{GREY};text-align:center;">{sub}</td></tr>\n"""
    return s

def rule(pad="32px 44px 0 44px"):
    return f"""<tr><td class="pad" style="padding:{pad};"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-top:1px solid {SAND};font-size:0;line-height:0;height:1px;">&nbsp;</td></tr></table></td></tr>\n"""

def card_open(pad="20px 44px 0 44px", border=SAND, bg=PAPER, inner="22px 22px"):
    return f"""<tr><td class="pad" style="padding:{pad};">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="background-color:{bg};border:1px solid {border};border-radius:4px;"><tr><td class="cardin" style="padding:{inner};">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">\n"""

CARD_CLOSE = "</table>\n</td></tr></table>\n</td></tr>\n"

# ---------------------------------------------------------------- blocks
LINE_IMG = """{%- if line.image -%}<img src="{{ line.image | img_url: 'compact_cropped' }}" width="64" height="64" alt="{{ line.title | escape }}" style="display:block;width:64px;height:64px;border-radius:3px;border:1px solid #ECE7DD;object-fit:cover;">{%- else -%}<div style="width:64px;height:64px;background:#ECE7DD;border-radius:3px;"></div>{%- endif -%}"""

def items_block(title="What you ordered", show_head=True):
    head = (eyebrow("YOUR ORDER {{ order_name }}") + h2(title)) if show_head else ""
    return head + card_open() + f"""{{%- for line in subtotal_line_items -%}}
{{%- if line.final_line_price > 0 or line.selling_plan_allocation -%}}
<tr>
  <td width="64" valign="top" style="width:64px;padding:{{% if forloop.first %}}0{{% else %}}14px{{% endif %}} 0 14px 0;border-bottom:1px solid {SAND};">{LINE_IMG}</td>
  <td valign="top" style="padding:{{% if forloop.first %}}0{{% else %}}14px{{% endif %}} 10px 14px 14px;border-bottom:1px solid {SAND};{F}font-size:15px;line-height:21px;color:{INK};">
    <span style="font-weight:600;">{{{{ line.title }}}}</span>
    {{%- if line.variant.title and line.variant.title != 'Default Title' -%}}<br><span style="font-size:13px;color:{GREY};">{{{{ line.variant.title }}}}</span>{{%- endif -%}}
    <br><span style="font-size:13px;color:{GREY};">Qty {{{{ line.quantity }}}}</span>
    {{%- if line.selling_plan_allocation -%}}<br><span style="display:inline-block;margin-top:6px;padding:3px 8px;background-color:#F6E7E1;color:{BRICK};font-size:11px;line-height:15px;letter-spacing:1px;font-weight:600;border-radius:2px;">SUBSCRIPTION</span><br><span style="font-size:13px;line-height:19px;color:{INK};">{{{{ line.selling_plan_allocation.selling_plan.name }}}}</span>{{%- endif -%}}
  </td>
  <td valign="top" align="right" style="padding:{{% if forloop.first %}}0{{% else %}}14px{{% endif %}} 0 14px 0;border-bottom:1px solid {SAND};{F}font-size:15px;line-height:21px;color:{INK};white-space:nowrap;">{{% if line.final_line_price == 0 %}}Free{{% else %}}{{{{ line.final_line_price | money }}}}{{% endif %}}</td>
</tr>
{{%- endif -%}}
{{%- endfor -%}}
{{%- if sk_gifts > 0 -%}}
<tr><td colspan="3" style="padding:14px 0 14px 0;border-bottom:1px solid {SAND};{F}font-size:15px;line-height:21px;color:{INK};">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
    <td style="{F}font-size:15px;line-height:21px;color:{INK};"><span style="font-weight:600;">{{{{ sk_gifts }}}} free gifts</span><br><span style="font-size:13px;color:{GREY};">Details below</span></td>
    <td align="right" style="{F}font-size:15px;line-height:21px;color:{INK};white-space:nowrap;">{{{{ 0 | money }}}}</td>
  </tr></table>
</td></tr>
{{%- endif -%}}
{TOTALS}""" + CARD_CLOSE

def trow(label, value, bold=False, size=14, pad="4px"):
    w = "600" if bold else "400"
    return f"""<tr><td colspan="2" style="padding:{pad} 0 0 0;{F}font-size:{size}px;line-height:{int(size*1.5)}px;color:{INK};font-weight:{w};">{label}</td><td align="right" style="padding:{pad} 0 0 0;{F}font-size:{size}px;line-height:{int(size*1.5)}px;color:{INK};font-weight:{w};white-space:nowrap;">{value}</td></tr>\n"""

TOTALS = (trow("Subtotal", "{{ subtotal_price | money }}", pad="14px")
    + "{%- if total_discounts > 0 -%}" + trow("Discount", "-{{ total_discounts | money }}") + "{%- endif -%}\n"
    + trow("Shipping", "{% if shipping_price == 0 %}Free{% else %}{{ shipping_price | money }}{% endif %}")
    + "{%- if tax_price > 0 -%}" + trow("Tax", "{{ tax_price | money }}") + "{%- endif -%}\n"
    + trow("Total charged today", "{{ total_price | money_with_currency }}", bold=True, size=16, pad="10px")
    + f"""{{%- if sk_cur != 'USD' -%}}<tr><td colspan="3" style="padding:10px 0 0 0;{F}font-size:13px;line-height:19px;color:{GREY};">You were charged in {{{{ sk_cur }}}}, the currency you saw at checkout. If your card uses another currency, your bank converts it and may add its own fee.</td></tr>{{%- endif -%}}\n""")

def items(title="What you ordered", show_head=True):
    return items_block(title, show_head).replace("{TOTALS}", TOTALS)

def step(n_label, title, body, last=False, done=False):
    dot_bg = BRICK if done else PAPER
    dot_fg = "#FFFFFF" if done else BRICK
    return f"""<tr>
  <td width="30" valign="top" style="width:30px;padding:0 0 {0 if last else 18}px 0;"><span style="display:inline-block;width:26px;height:26px;background-color:{dot_bg};border:2px solid {BRICK};border-radius:50%;{F}font-size:12px;line-height:26px;font-weight:600;color:{dot_fg};text-align:center;">{n_label}</span></td>
  <td valign="top" style="padding:4px 0 {0 if last else 18}px 14px;{F}font-size:15px;line-height:22px;color:{INK};"><span style="font-weight:600;">{title}</span><br><span style="font-size:14px;line-height:21px;color:#4A4744;">{body}</span></td>
</tr>\n"""

def timeline(head_eyebrow="WHAT HAPPENS NEXT", head="From our shelf to your stove"):
    rows = (step("1", "Today: order received",
                 "You are reading the proof. Need to change the address or cancel? Reply within {{ sk_cancel_window }} of ordering.", done=True)
        + step("2", "Within 1 business day: packed",
               "We check every piece before it goes in the box.")
        + step("3", "Shipped: tracking by email",
               "{% if sk_ship > 1 %}One email per parcel, each with its own tracking link. {% else %}You get an email with your tracking link. {% endif %}Tracking can take 24 to 72 hours to show movement.")
        + step("4", "Delivered: usually {{ sk_days }} days after it ships",
               "{% if sk_country == 'US' %}That is the US average. Holidays and peak weeks can add a few days.{% else %}That is our average outside the US. Customs and peak weeks can add a few days.{% endif %}", last=True))
    return eyebrow(head_eyebrow) + h2(head) + card_open() + rows + CARD_CLOSE

def shipments(pad_top="20px"):
    return f"""{{%- if sk_ship > 1 -%}}
""" + card_open(pad=f"{pad_top} 44px 0 44px", border="#E3C9BE", bg="#FBF3EF") + f"""<tr><td style="{F}font-size:11px;line-height:16px;letter-spacing:2px;font-weight:600;color:{BRICK};">YOUR ORDER MAY COME IN MORE THAN ONE PARCEL</td></tr>
<tr><td style="padding-top:8px;{F}font-size:15px;line-height:23px;color:{INK};">
{{%- if sk_sep_text != '' -%}}{{{{ sk_sep_text }}}} {{% if sk_sep_list.size > 1 %}}often ship on their own{{% else %}}often ships on its own{{% endif %}} and can arrive first.{{%- else -%}}Some items ship on their own and can arrive first.{{%- endif %}} So if one box arrives and the rest is not there yet, nothing is missing. It is on its way.</td></tr>
<tr><td style="padding-top:12px;{F}font-size:14px;line-height:22px;color:#4A4744;">
&bull;&nbsp; Every parcel gets its own tracking email.<br>
&bull;&nbsp; A &ldquo;delivered&rdquo; notice can be for one parcel only.<br>
&bull;&nbsp; Check all tracking emails, or see every parcel on <a href="{{{{ order_status_url }}}}" style="color:{BRICK};">your order page</a>.<br>
&bull;&nbsp; No movement 14 days after a parcel shipped? Email us and we will trace it.</td></tr>
""" + CARD_CLOSE + "{%- endif -%}\n"

SUB = f"""{{%- for line in subtotal_line_items -%}}{{%- if line.selling_plan_allocation -%}}
{{%- assign sp_name = line.selling_plan_allocation.selling_plan.name -%}}
{{%- assign sp_days = sp_name | split: 'every ' | last | split: ' ' | first | plus: 0 -%}}
""" + card_open(pad="20px 44px 0 44px", border=INK, bg=PAPER) + f"""<tr><td style="{F}font-size:11px;line-height:16px;letter-spacing:2px;font-weight:600;color:{BRICK};">YOU STARTED A SUBSCRIPTION</td></tr>
<tr><td style="padding-top:6px;{SERIF}font-size:26px;line-height:30px;color:{INK};">{{{{ line.title }}}}</td></tr>
<tr><td style="padding-top:12px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr><td width="112" valign="top" style="width:112px;padding:6px 0;border-top:1px solid {SAND};{F}font-size:13px;line-height:20px;color:{GREY};">Plan</td><td valign="top" style="padding:6px 0;border-top:1px solid {SAND};{F}font-size:14px;line-height:20px;color:{INK};font-weight:600;">{{{{ sp_name }}}}</td></tr>
    <tr><td valign="top" style="padding:6px 0;border-top:1px solid {SAND};{F}font-size:13px;line-height:20px;color:{GREY};">Today</td><td valign="top" style="padding:6px 0;border-top:1px solid {SAND};{F}font-size:14px;line-height:20px;color:{INK};">{{% if line.final_line_price == 0 %}}Free, nothing charged for this item{{% else %}}{{{{ line.final_line_price | money }}}}{{% endif %}}</td></tr>
    {{%- if sp_days > 0 -%}}{{%- assign sp_secs = sp_days | times: 86400 -%}}<tr><td valign="top" style="padding:6px 0;border-top:1px solid {SAND};{F}font-size:13px;line-height:20px;color:{GREY};">First charge</td><td valign="top" style="padding:6px 0;border-top:1px solid {SAND};{F}font-size:14px;line-height:20px;color:{INK};">Around {{{{ created_at | date: '%s' | plus: sp_secs | date: '%B %-d, %Y' }}}}, then every {{{{ sp_days }}}} days</td></tr>{{%- endif -%}}
    <tr><td valign="top" style="padding:6px 0;border-top:1px solid {SAND};border-bottom:1px solid {SAND};{F}font-size:13px;line-height:20px;color:{GREY};">Cancel</td><td valign="top" style="padding:6px 0;border-top:1px solid {SAND};border-bottom:1px solid {SAND};{F}font-size:14px;line-height:20px;color:{INK};">Any time before a charge, in one click</td></tr>
  </table>
</td></tr>
<tr><td style="padding-top:12px;{F}font-size:14px;line-height:22px;color:#4A4744;">Didn&rsquo;t mean to subscribe, or want to skip or pause? It takes one click{{% if line.final_line_price == 0 %}}, and nothing has been charged yet{{% endif %}}.</td></tr>
<tr><td align="center" style="padding-top:16px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" bgcolor="{PAPER}" style="background-color:{PAPER};border:2px solid {INK};border-radius:3px;">
    <a href="{{{{ sk_portal_url }}}}" style="display:block;padding:14px 16px;{F}font-size:14px;line-height:18px;font-weight:600;letter-spacing:1.2px;color:{INK};text-decoration:none;text-transform:uppercase;">Manage or cancel my subscription &rarr;</a>
  </td></tr></table>
</td></tr>
""" + CARD_CLOSE + "{%- endif -%}{%- endfor -%}\n"

def gift_row(img, title, tag, body, last=False):
    bb = "" if last else f"border-bottom:1px solid {SAND};"
    return f"""<tr>
  <td width="56" valign="top" style="width:56px;padding:12px 0;{bb}"><img src="{img}" width="56" height="56" alt="" style="display:block;width:56px;height:56px;border-radius:3px;object-fit:cover;"></td>
  <td valign="top" style="padding:12px 0 12px 14px;{bb}{F}font-size:15px;line-height:21px;color:{INK};"><span style="font-weight:600;">{title}</span> &nbsp;<span style="display:inline-block;padding:2px 7px;background-color:{CREAM};border:1px solid {SAND};color:{GREY};font-size:10px;line-height:14px;letter-spacing:1px;font-weight:600;border-radius:2px;white-space:nowrap;">{tag}</span><br><span style="font-size:13px;line-height:19px;color:#4A4744;">{body}</span></td>
</tr>\n"""

def gifts():
    loop = f"""{{%- for line in subtotal_line_items -%}}
{{%- assign t = line.title | downcase -%}}
{{%- unless line.selling_plan_allocation -%}}{{%- if line.final_line_price == 0 -%}}
{{%- if t contains 'mystery' -%}}{gift_row(IMG['gift_mystery'], '{{ line.title }}', 'SHIPS', 'A surprise in a box of its own. It often ships separately, so it may arrive before or after your cookware.')}
{{%- elsif t contains 'shipping' -%}}{gift_row(IMG['gift_shipping'], '{{ line.title }}', 'APPLIED', 'Already taken off this order. Nothing to do.')}
{{%- elsif t contains 'cookbook' -%}}{gift_row(IMG['gift_cookbook'], '{{ line.title }}', 'DIGITAL', '{% if sk_cookbook_url != blank %}Nothing ships. <a href="{{ sk_cookbook_url }}" style="color:#AC3B19;">Download it here</a>.{% else %}Nothing ships. Your download link arrives in a separate email.{% endif %}')}
{{%- elsif t contains 'book' or t contains 'guide' -%}}{gift_row(IMG['gift_ebook'], '{{ line.title }}', 'DIGITAL', 'Nothing ships. <a href="{{ sk_ebook_url }}" style="color:#AC3B19;">Download it here</a>, the link also comes by email.')}
{{%- elsif t contains 'filter' or t contains 'draw' -%}}{gift_row(IMG['gift_filter'], '{{ line.title }}', 'DRAW', 'You are entered in the weekly draw for a PFAS water filter. Winners hear from us by email.')}
{{%- else -%}}{gift_row(IMG['gift_mystery'], '{{ line.title }}', 'INCLUDED', 'Included with your order.')}
{{%- endif -%}}
{{%- endif -%}}{{%- endunless -%}}
{{%- endfor -%}}"""
    return ("{%- if sk_gifts > 0 -%}\n" + eyebrow("INCLUDED WITH EVERY ORDER") + h2("Your {{ sk_gifts }} free gifts")
            + para("What ships, what is digital, and what you are entered in.", pad="8px 44px 0 44px", size=14, color=GREY)
            + card_open(inner="6px 22px") + loop + CARD_CLOSE + "{%- endif -%}\n")

def address():
    return f"""{{%- if shipping_address -%}}
{para('<span style="font-weight:600;">Shipping to</span><br>{{ shipping_address.name }}<br>{{ shipping_address.address1 }}{% if shipping_address.address2 != blank %}, {{ shipping_address.address2 }}{% endif %}<br>{{ shipping_address.city }}{% if shipping_address.province_code != blank %}, {{ shipping_address.province_code }}{% endif %} {{ shipping_address.zip }}<br>{{ shipping_address.country }}<br><span style="font-size:13px;color:#727272;">Something wrong? Reply within {{ sk_cancel_window }} and we fix it before it ships.</span>', pad='16px 44px 0 44px', size=14)}
{{%- endif -%}}
"""

def help_block(head="Need to change something?"):
    return (eyebrow("HELP") + h2(head)
        + para("Reply to this email or write to <a href=\"mailto:{{ sk_support }}\" style=\"color:#AC3B19;\">{{ sk_support }}</a>. Our team answers within 1 hour on business days.")
        + para("<span style=\"font-weight:600;\">Change or cancel:</span> ask within {{ sk_cancel_window }} of ordering. After that your order may already be packed. Write anyway, we will tell you honestly what is still possible.", pad="10px 44px 0 44px")
        + button("View my order", "{{ order_status_url }}", pad="22px 44px 0 44px")
        + icons3())

def icons3(pad="30px 44px 36px 44px"):
    def cell(img, t1, t2):
        return f"""<td class="ic3" width="33%" valign="top" align="center" style="width:33%;padding:0 6px;text-align:center;"><img src="{img}" width="44" height="44" alt="" style="display:block;margin:0 auto;width:44px;height:44px;"><div style="padding-top:8px;{F}font-size:13px;line-height:18px;font-weight:600;color:{INK};">{t1}</div><div style="{F}font-size:12px;line-height:17px;color:{GREY};">{t2}</div></td>"""
    return f"""<tr><td class="pad" style="padding:{pad};"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
{cell(IMG['icon_returns'], '30-day returns', 'Unused, within 30 days of delivery')}
{cell(IMG['icon_warranty'], '75-year warranty', 'Against defects, as long as you own it')}
{cell(IMG['icon_customers'], '100,000+', 'happy customers')}
</tr></table></td></tr>\n"""

def hero_text(eb, title, sub, pad_top="40px"):
    return (eyebrow(eb, pad=f"{pad_top} 44px 0 44px", align="center")
        + f"""<tr><td class="pad h1" align="center" style="padding:10px 44px 0 44px;{SERIF}font-size:44px;line-height:48px;color:{INK};text-align:center;">{title}</td></tr>\n"""
        + para(sub, pad="12px 60px 0 60px", size=16, color="#4A4744", align="center"))

# ---------------------------------------------------------------- variants
def variant_a():
    body = (hero_text("ORDER CONFIRMED", "Thank you, {{ customer.first_name | default: 'friend' }}.",
                      "Order {{ order_name }} is in. Below: what you ordered, what it cost, and exactly what happens next.")
        + button("View my order", "{{ order_status_url }}", pad="24px 44px 0 44px", sub="Tracking appears here as soon as each parcel ships.")
        + items_head_spacer() + items("What you ordered") + address()
        + timeline() + shipments() + SUB + gifts() + rule() + help_block())
    return body, "Calm receipt", "Order {{ order_name }} is confirmed. What you ordered, what ships when, and how to change anything."

def items_head_spacer():
    return "<tr><td style=\"font-size:0;line-height:0;height:8px;\">&nbsp;</td></tr>\n"

def week_step(n, title, body, last=False):
    return step(n, title, body, last=last)

def variant_b():
    hero = f"""<tr><td style="padding:0;"><a href="https://siraatskitchen.com"><img src="{IMG['hero_b']}" width="600" alt="Friends around a dinner table, sharing food from a hammered titanium pan" style="display:block;width:100%;max-width:600px;height:auto;"></a></td></tr>\n"""
    first_week = (eyebrow("YOUR FIRST WEEK WITH TITANIUM") + h2("What to expect, step by step")
        + card_open() + week_step("1", "The day it arrives", "Unbox, wash once with warm soapy water, dry. No seasoning needed.")
        + week_step("2", "First cook: heat, oil, food", "Medium heat for 2 to 3 minutes. A drop of water should bead up and glide. Then a teaspoon of oil, then the food. Cold metal grabs your food, hot metal lets it go.")
        + week_step("3", "Week 1", "Start with eggs. Let food sit until it lets go on its own. If it sticks, the pan was not hot enough yet. Give it another minute next time.")
        + week_step("4", "Month 1", "You stop thinking about it. Metal spatula, dishwasher, oven: all fine. There is no coating to protect.", last=True)
        + CARD_CLOSE)
    def pill(t):
        return f"""<span class="pill" style="display:inline-block;margin:0 4px 8px 0;padding:7px 12px;background-color:{PAPER};border:1px solid {SAND};border-radius:20px;{F}font-size:12px;line-height:16px;font-weight:600;color:{INK};white-space:nowrap;">{t}</span>"""
    pills = f"""<tr><td class="pad" align="center" style="padding:20px 44px 0 44px;text-align:center;">{pill('Dishwasher safe')}{pill('Metal utensil safe')}{pill('Oven safe')}{pill('Induction ready')}{pill('No seasoning')}</td></tr>\n"""
    trust = (f"""<tr><td class="pad" style="padding:36px 44px 0 44px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{INK}" style="background-color:{INK};border-radius:4px;"><tr><td style="padding:30px 28px;" bgcolor="{INK}">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
<tr><td bgcolor="{INK}" style="background-color:{INK};{F}font-size:11px;line-height:16px;letter-spacing:2px;font-weight:600;color:#E3A28C;">THIRD-PARTY TESTED</td></tr>
<tr><td bgcolor="{INK}" class="h2" style="background-color:{INK};padding-top:8px;{SERIF}font-size:30px;line-height:34px;color:#FFFFFF;">What you get is exactly what we tested.</td></tr>
<tr><td bgcolor="{INK}" style="background-color:{INK};padding-top:12px;{F}font-size:15px;line-height:23px;color:#DAD6CF;">A pure titanium cooking surface with no coatings. Tested free from PFAS by Light Labs, an ISO/IEC 17025-accredited lab: report no. 25895, 31 PFAS compounds, every one below the detection limit.</td></tr>
<tr><td bgcolor="{INK}" style="background-color:{INK};padding-top:14px;{F}font-size:14px;line-height:20px;"><a href="https://siraatskitchen.com/pages/third-party-testing" style="color:#FFFFFF;font-weight:600;">Read the report yourself &rarr;</a></td></tr>
<tr><td bgcolor="{INK}" style="background-color:{INK};padding-top:22px;border-bottom:1px solid #5A5856;font-size:0;line-height:0;">&nbsp;</td></tr>
<tr><td bgcolor="{INK}" style="background-color:{INK};padding-top:18px;{F}font-size:18px;line-height:22px;letter-spacing:3px;color:#E3A28C;">&#9733;&#9733;&#9733;&#9733;&#9733;</td></tr>
<tr><td bgcolor="{INK}" style="background-color:{INK};padding-top:4px;{F}font-size:14px;line-height:21px;color:#DAD6CF;"><span style="color:#FFFFFF;font-weight:600;">100,000+ happy customers.</span> Covered for 75 years against defects.</td></tr>
</table></td></tr></table></td></tr>\n""")
    body = (hero + hero_text("ORDER {{ order_name }}", "Your order is confirmed.",
                             "Thank you, {{ customer.first_name | default: 'friend' }}. Here is what you ordered, and what your first week with titanium looks like.", pad_top="34px")
        + items_head_spacer() + items("Order details", show_head=False)
        + button("View my order", "{{ order_status_url }}", pad="22px 44px 0 44px", sub="Tracking appears here as soon as each parcel ships.")
        + rule("34px 44px 0 44px") + first_week + pills + trust
        + timeline("THE PRACTICAL PART", "When it arrives") + shipments() + SUB + gifts() + address() + rule() + help_block())
    return body, "Experience", "Your order is confirmed. Here is your first week with titanium, plus when each parcel ships."

def variant_c():
    def ck(label, value, last=False):
        bb = "" if last else f"border-bottom:1px solid {SAND};"
        return f"""<tr><td width="24" valign="top" style="width:24px;padding:13px 0 12px 0;{bb}"><span style="display:inline-block;width:16px;height:16px;line-height:16px;text-align:center;background-color:{BRICK};color:#FFFFFF;border-radius:50%;{F}font-size:10px;font-weight:600;">&#10003;</span></td>
<td class="ck-l" width="124" valign="top" style="width:124px;padding:12px 10px 12px 0;{bb}{F}font-size:11px;line-height:18px;letter-spacing:1px;font-weight:600;color:{BRICK};">{label}</td>
<td valign="top" style="padding:12px 0;{bb}{F}font-size:14px;line-height:21px;color:{INK};">{value}</td></tr>\n"""
    checklist = (card_open(pad="24px 44px 0 44px", border=INK, inner="8px 20px")
        + ck("WHAT YOU ORDERED", "{{ sk_first }}{% if sk_more > 0 %} and {{ sk_more }} more item{% if sk_more > 1 %}s{% endif %}{% endif %}{% if sk_subs > 0 %}, plus a subscription{% endif %}{% if sk_gifts > 0 %}, plus {{ sk_gifts }} free gifts{% endif %}.")
        + ck("WHAT IT COSTS", "<span style=\"font-weight:600;\">{{ total_price | money_with_currency }}</span>, charged today.{% if sk_cur != 'USD' %} Charged in {{ sk_cur }}, the currency you saw at checkout.{% endif %}{% if sk_subs > 0 %} The subscription costs nothing today.{% endif %}")
        + ck("WHEN IT ARRIVES", "Packed within 1 business day. Delivered usually {{ sk_days }} days after it ships. Tracking comes by email.")
        + ck("WHAT ARRIVES SEPARATELY", "{% if sk_ship > 1 %}{% if sk_sep_text != '' %}{{ sk_sep_text }} {% if sk_sep_list.size > 1 %}can each come in their own parcel{% else %}can come in its own parcel{% endif %}{% else %}Some items can come in their own parcel{% endif %}, each with its own tracking. A &ldquo;delivered&rdquo; notice may be for one parcel only.{% else %}Nothing. Your order ships in one parcel.{% endif %}")
        + ck("YOUR SUBSCRIPTION", "{% if sk_subs > 0 %}{% for line in subtotal_line_items %}{% if line.selling_plan_allocation %}<span style=\"font-weight:600;\">{{ line.title }}:</span> {{ line.selling_plan_allocation.selling_plan.name }}. <a href=\"{{ sk_portal_url }}\" style=\"color:#AC3B19;\">Manage or cancel</a>.<br>{% endif %}{% endfor %}{% else %}None. Nothing in this order renews.{% endif %}")
        + ck("HOW TO CHANGE IT", "Reply to this email within {{ sk_cancel_window }} to change the address or cancel.{% if sk_subs > 0 %} The subscription you can change or cancel any time, in one click.{% endif %}", last=True)
        + CARD_CLOSE)
    body = (hero_text("ORDER {{ order_name }} CONFIRMED", "No surprises.",
                      "{{ customer.first_name | default: 'Hi' }}, here is everything about your order on one screen. Details below.", pad_top="36px")
        + checklist
        + button("View my order", "{{ order_status_url }}", pad="22px 44px 0 44px", sub="Tracking appears here as soon as each parcel ships.")
        + rule("34px 44px 0 44px") + SUB + items("The details") + address()
        + shipments("24px") + timeline() + gifts() + rule() + help_block())
    return body, "No surprises", "Order {{ order_name }}: what you ordered, what it costs, when it arrives, and what comes separately."

def build():
    for key, fn in (("a", variant_a), ("b", variant_b), ("c", variant_c)):
        body, name, pre = fn()
        html = (SETUP.replace("VARIANT_NAME", f"variant {key.upper()} ({name})")
                + HEAD.replace("PREHEADER", pre) + HEADER + body + FOOTER)
        assert "—" not in html and "–" not in html, f"dash in variant {key}"
        out = os.path.join(HERE, f"variant-{key}.liquid")
        open(out, "w").write(html)
        print("written", out, len(html))

if __name__ == "__main__":
    build()
