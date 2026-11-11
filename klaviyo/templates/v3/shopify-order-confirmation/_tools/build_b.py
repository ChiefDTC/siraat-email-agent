#!/usr/bin/env python3
"""Bouwt de drie herontwerpen van variant B (11 nov 2026): b2 Editorial, b3 Steps, b4 Cards.

Gebruik: python3 -I _tools/build_b.py   (vanuit de map shopify-order-confirmation)
Daarna:  VARIANTS=b2,b3,b4 LIQUIDJS=<pad>/node_modules/liquidjs node _tools/render.js

Hergebruikt de Liquid-logica en blokken van build.py (settings, subtotal_line_items-lus,
selling_plan_allocation, presentment currency, gifts-detectie, abonnementskader, pakketten,
giftslijst, hulpblok, footer). Nieuw: hero met live tekst op het beeld (achtergrond + VML),
welkomst-samenvatting, verwachtingstijdlijn, vier pijlers, eerste week, in drie vormen.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B  # noqa: E402

HERE = B.HERE
F, SERIF = B.F, B.SERIF
INK, CREAM, SAND, BRICK, GREY, PAPER = B.INK, B.CREAM, B.SAND, B.BRICK, B.GREY, B.PAPER
K, S, IMG = B.K, B.S, B.IMG
SOFT = "#4A4744"

HERO_IMG = "https://cdn.shopify.com/s/files/1/0907/0877/1156/files/siraat-titanium-hammered-deep-pan-10-family-dinner.webp?width=1200&height=904&crop=center&format=pjpg"  # familiediner Deep Pan (Floris, 11 nov); was AI-flash 5d0622a1   # Higgsfield flash, 1168x880, ocimg/hero1 (11 nov)
HERO_BG = "#1C1510"

def shop(f, w=1200, h=800):
    return f"{S}{f}?width={w}&height={h}&crop=center&format=pjpg"

PIL = {  # echte shootfoto's (hp-shoot), Shopify-CDN
    "nontoxic": "P11-E_Hammered_1920w_q82.webp",
    "perf": "P04-A_Stovetop_Pan_1920w_q82.webp",
    "life": "P11-C_Edge_2560w_q76.webp",
    "oven": "P07-A_OvenSafe_1920w_q82.webp",
    "egg": "P09-B_Pan_Lid_1920w_q82.webp",
}
ICON = {
    "nocoat": IMG["icon_nocoat"], "pfas": IMG["icon_pfas"], "warranty": IMG["icon_warranty"],
    "customers": IMG["icon_customers"], "returns": IMG["icon_returns"],
    "oven": K + "32fc5491-ecc0-4ed3-914c-a9162fa5e01e.png",
    "utensil": K + "aa65fb02-298b-4520-bd71-a95a4c29f438.png",
    "truck": K + "97d97db1-3ff1-4112-b062-fc0af390ce4b.png",
    "check": K + "6d715e47-cf75-4606-a1d2-63d4dd4717c7.png",
    "clock": K + "b7e73206-d320-43bf-a098-a7c7f3cb0b10.png",
    "gift": K + "13fbb106-5f86-4d07-8046-ad1a9f5b74a1.png",
    "original": K + "f809f5c9-53fe-471c-bf61-5383ae8c1d4c.png",
}
LAB_URL = "https://siraatskitchen.com/pages/third-party-testing"
PORTAL = "https://siraatskitchen.com/tools/recurring/login"

# ------------------------------------------------------------ settings + extra Liquid
SETUP = (B.SETUP
    .replace("'https://siraatskitchen.com/a/loop_subscriptions/customer' -%}{%- comment -%} subscription portal: Loop (LOG 30 Oct) or Recharge customer portal link. One click, no login if possible. {%- endcomment -%}",
             f"'{PORTAL}' -%}}{{%- comment -%}} subscription portal: Recharge (11 Nov 2026) {{%- endcomment -%}}")
    .replace("{%- assign sk_cancel_window = '1 hour' -%}",
             "{%- assign sk_pack = 'within 1 business day' -%}{%- comment -%} packing promise. Policy page and help center: processed within 1 business day. Floris wants 'within a few hours'; only switch when the warehouse really does that (8 Oct data: median 77 h to fulfillment). {%- endcomment -%}\n{%- assign sk_cancel_window = '1 hour' -%}"))
assert PORTAL in SETUP and "sk_pack" in SETUP
SETUP += """{%- assign sk_where = shipping_address.country | default: '' -%}{%- case sk_country -%}{%- when 'US' -%}{%- assign sk_where = 'the US' -%}{%- when 'GB' -%}{%- assign sk_where = 'the UK' -%}{%- when 'NL' -%}{%- assign sk_where = 'the Netherlands' -%}{%- when 'AE' -%}{%- assign sk_where = 'the UAE' -%}{%- when 'PH' -%}{%- assign sk_where = 'the Philippines' -%}{%- endcase -%}
{%- comment -%} sk_kind: pan (any cookware in the order), board (cutting board, no cookware) or other (accessories only). Drives the intro, the pillars and the first-week block. {%- endcomment -%}
{%- assign sk_kind = 'other' -%}
{%- for line in subtotal_line_items -%}{%- if line.final_line_price > 0 and line.selling_plan_allocation == nil -%}
  {%- assign t = line.title | downcase -%}
  {%- if t contains 'pan' or t contains 'wok' or t contains 'pot' or t contains 'cookware' or t contains 'duo' or t contains 'complete edition' or t contains 'braiser' or t contains 'skillet' or t contains 'pizza steel' -%}{%- assign sk_kind = 'pan' -%}
  {%- elsif t contains 'board' and sk_kind != 'pan' -%}{%- assign sk_kind = 'board' -%}{%- endif -%}
{%- endif -%}{%- endfor -%}
{%- assign sk_first_img = '' -%}{%- assign sk_first_var = '' -%}{%- assign sk_first_qty = 1 -%}{%- assign sk_rest = '' -%}{%- assign sk_n = 0 -%}
{%- for line in subtotal_line_items -%}
  {%- if line.final_line_price > 0 and line.selling_plan_allocation == nil -%}
    {%- assign sk_n = sk_n | plus: 1 -%}
    {%- if sk_n == 1 -%}
      {%- if line.image -%}{%- assign sk_first_img = line.image | img_url: '480x480', crop: 'center' -%}{%- endif -%}
      {%- if line.variant.title != 'Default Title' -%}{%- assign sk_first_var = line.variant.title -%}{%- endif -%}
      {%- assign sk_first_qty = line.quantity -%}
    {%- else -%}
      {%- if sk_rest != '' -%}{%- assign sk_rest = sk_rest | append: ', ' -%}{%- endif -%}
      {%- assign sk_rest = sk_rest | append: line.title -%}{%- if line.quantity > 1 -%}{%- assign sk_rest = sk_rest | append: ' x ' | append: line.quantity -%}{%- endif -%}
    {%- endif -%}
  {%- endif -%}
{%- endfor -%}
"""

EXTRA_CSS = """
  .herotxt{text-shadow:0 1px 12px rgba(0,0,0,0.45);}
  @media only screen and (max-width:620px){
    .bign{font-size:44px!important;line-height:46px!important;}
  }
  @media only screen and (max-width:480px){
    .stack{display:block!important;width:100%!important;max-width:100%!important;}
    .stackimg{padding:0 0 18px 0!important;}
    .stackimg img{width:100%!important;height:auto!important;}
    .stacktxt{padding:0!important;}
    .g2{display:block!important;width:100%!important;padding:0 0 12px 0!important;}
    .t4{display:inline-block!important;width:48%!important;padding:0 0 16px 0!important;vertical-align:top!important;}
    .sumimg{width:96px!important;}
    .sumimg img{width:96px!important;height:96px!important;}
    .wkc{height:auto!important;padding:14px 16px!important;}
    .c2{padding:0 4px 8px 4px!important;}
    .c2in{padding:12px 12px 14px 12px!important;}
    .c2t{font-size:15px!important;line-height:20px!important;}
    .c2img{height:120px!important;}
    .c2big{font-size:26px!important;line-height:30px!important;}
    .heropad{padding:214px 22px 26px 22px!important;}
    .heroh1{font-size:34px!important;line-height:38px!important;}
  }
"""
HEAD = B.HEAD.replace("</style>", EXTRA_CSS + "</style>")

# ------------------------------------------------------------ shared new blocks
def h2i(txt, pad="8px 44px 0 44px", align="left", size=28):
    """Kop in Inter (b3, b4)."""
    return f"""<tr><td class="pad h2" align="{align}" style="padding:{pad};{F}font-size:{size}px;line-height:{size+6}px;font-weight:600;letter-spacing:-0.5px;color:{INK};text-align:{align};">{txt}</td></tr>\n"""

def hero(sub):
    txt = f"""<div style="{F}font-size:12px;line-height:16px;letter-spacing:2.4px;font-weight:600;color:#F1D7C9;">THANK YOU{{% if customer.first_name != blank %}}, {{{{ customer.first_name | upcase }}}}{{% endif %}}</div>
<div class="heroh1" style="{F}font-size:44px;line-height:48px;font-weight:700;letter-spacing:-1.2px;color:#FFFFFF;padding-top:10px;">Your order is confirmed.</div>
<div style="{F}font-size:16px;line-height:24px;font-weight:500;color:#F1EEE8;padding-top:10px;">{sub}</div>"""
    return f"""<!-- HERO: live tekst op het beeld. Achtergrondbeeld (background-attribuut + CSS) met VML voor Outlook; bgcolor als beelden uit staan. -->
<tr><td align="left" valign="bottom" bgcolor="{HERO_BG}" background="{HERO_IMG}" style="background-color:{HERO_BG};background-image:url('{HERO_IMG}');background-size:cover;background-position:center top;background-repeat:no-repeat;"><!--[if gte mso 9]><v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width:600px;height:452px;"><v:fill type="frame" src="{HERO_IMG}" color="{HERO_BG}" /><v:textbox inset="0,0,0,0"><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="heropad herotxt" align="left" valign="bottom" style="padding:262px 40px 34px 40px;background-image:linear-gradient(180deg,rgba(18,12,8,0) 0%,rgba(18,12,8,0.55) 38%,rgba(18,12,8,0.92) 100%);">
{txt}
</td></tr></table>
<!--[if gte mso 9]></v:textbox></v:rect><![endif]--></td></tr>
"""

def welcome(serif=False, pad_top="34px"):
    head = (f"""<tr><td class="pad h2" style="padding:{pad_top} 44px 0 44px;{SERIF}font-size:34px;line-height:38px;color:{INK};">Welcome to Siraat.</td></tr>\n"""
            if serif else h2i("Welcome to Siraat.", pad=f"{pad_top} 44px 0 44px", size=30))
    intro = B.para("{% if sk_kind == 'pan' %}You chose a pan with a pure titanium cooking surface and no coatings, so there is nothing on it to wear off.{% elsif sk_kind == 'board' %}You chose a pure titanium board. No plastic, no wood, nothing to shave off into your food.{% endif %} Here is your order.", pad="10px 44px 0 44px", color=SOFT)
    # Alle betaalde regels (max 4 zichtbaar), daarna een regel voor de rest, abonnement en gifts.
    rows = f"""{{%- assign sk_row = 0 -%}}
{{%- for line in subtotal_line_items -%}}{{%- if line.final_line_price > 0 and line.selling_plan_allocation == nil -%}}
{{%- assign sk_row = sk_row | plus: 1 -%}}{{%- if sk_row <= 4 -%}}
<tr>
  <td width="64" valign="top" style="width:64px;padding:{{% if sk_row == 1 %}}0{{% else %}}12px{{% endif %}} 0 12px 0;border-bottom:1px solid {SAND};">{{%- if line.image -%}}<img src="{{{{ line.image | img_url: '160x160', crop: 'center' }}}}" width="64" height="64" alt="{{{{ line.title | escape }}}}" style="display:block;width:64px;height:64px;border-radius:6px;border:1px solid {SAND};">{{%- else -%}}<div style="width:64px;height:64px;background:{SAND};border-radius:6px;"></div>{{%- endif -%}}</td>
  <td valign="top" style="padding:{{% if sk_row == 1 %}}2px{{% else %}}14px{{% endif %}} 10px 12px 14px;border-bottom:1px solid {SAND};{F}color:{INK};">
    <div style="font-size:15px;line-height:20px;font-weight:600;">{{{{ line.title }}}}</div>
    <div style="font-size:13px;line-height:18px;color:{GREY};padding-top:2px;">{{% if line.variant.title != 'Default Title' %}}{{{{ line.variant.title }}}} &middot; {{% endif %}}Qty {{{{ line.quantity }}}}</div>
  </td>
  <td valign="top" align="right" style="padding:{{% if sk_row == 1 %}}2px{{% else %}}14px{{% endif %}} 0 12px 0;border-bottom:1px solid {SAND};{F}font-size:15px;line-height:20px;color:{INK};font-weight:600;white-space:nowrap;">{{{{ line.final_line_price | money }}}}</td>
</tr>
{{%- endif -%}}{{%- endif -%}}{{%- endfor -%}}
{{%- assign sk_extra = sk_row | minus: 4 -%}}
{{%- if sk_extra > 0 or sk_subs > 0 or sk_gifts > 0 -%}}
<tr><td colspan="3" style="padding:12px 0 0 0;{F}font-size:13px;line-height:19px;color:{SOFT};">{{% if sk_extra > 0 %}}+ {{{{ sk_extra }}}} more item{{% if sk_extra > 1 %}}s{{% endif %}}{{% if sk_subs > 0 or sk_gifts > 0 %}}, {{% endif %}}{{% else %}}+ {{% endif %}}{{% if sk_subs > 0 %}}a subscription{{% if sk_gifts > 0 %}} and {{% endif %}}{{% endif %}}{{% if sk_gifts > 0 %}}{{{{ sk_gifts }}}} free gifts{{% endif %}}. Full receipt below.</td></tr>
{{%- endif -%}}
<tr><td colspan="3" style="padding-top:14px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr><td style="padding:10px 0 0 0;border-top:1px solid {SAND};{F}font-size:13px;line-height:19px;color:{GREY};">Order</td><td align="right" style="padding:10px 0 0 0;border-top:1px solid {SAND};{F}font-size:14px;line-height:19px;color:{INK};font-weight:600;">{{{{ order_name }}}}</td></tr>
  <tr><td style="padding:6px 0 0 0;{F}font-size:13px;line-height:19px;color:{GREY};">Total charged today</td><td align="right" style="padding:6px 0 0 0;{F}font-size:16px;line-height:20px;color:{INK};font-weight:600;white-space:nowrap;">{{{{ total_price | money_with_currency }}}}</td></tr>
</table></td></tr>
"""
    card = B.card_open(pad="20px 44px 0 44px", inner="18px 18px") + rows + B.CARD_CLOSE
    track = f"""<tr><td class="pad" style="padding:18px 44px 0 44px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{PAPER}" style="background-color:{PAPER};border-left:3px solid {BRICK};border-radius:3px;"><tr>
  <td width="44" valign="top" style="width:44px;padding:16px 0 16px 16px;"><img src="{ICON['truck']}" width="28" height="28" alt="" style="display:block;width:28px;height:28px;"></td>
  <td valign="top" style="padding:14px 18px 14px 12px;{F}color:{INK};">
    <div style="font-size:17px;line-height:23px;font-weight:600;">You&rsquo;ll receive tracking once it ships.</div>
    <div style="font-size:13px;line-height:19px;color:{SOFT};padding-top:3px;">{{% if sk_ship > 1 %}}One email per parcel, each with its own tracking link.{{% else %}}We email you the tracking link the moment your box leaves us.{{% endif %}}</div>
  </td></tr></table></td></tr>
"""
    return head + intro + card + track

PACK_T = "Packed {{ sk_pack }}"
SHIP_T = "Shipped, tracking by email"
DELIV_T = "Delivered in {{ sk_days }} days"
STEPS_EXPECT = [
    ("Order confirmed", "That is this email. Want to change the address? Reply within {{ sk_cancel_window }}.", "check"),
    (PACK_T, "We check every piece before it goes in the box.", "clock"),
    (SHIP_T, "{% if sk_ship > 1 %}One email per parcel, each with its own tracking link.{% else %}You get an email with your tracking link.{% endif %} It can take 24 to 72 hours to show movement.", "truck"),
    (DELIV_T, "Counted from the day it ships{% if sk_where != '' %}, within {{ sk_where }}{% endif %}. Peak weeks can add a few days.", "gift"),
]
PARCEL_NOTE = ("{% if sk_ship > 1 %}{% if sk_sep_text != '' %}{{ sk_sep_text }} {% if sk_sep_list.size > 1 %}often ship on their own{% else %}often ships on its own{% endif %}"
               "{% else %}Some items ship on their own{% endif %}, so your order may arrive in more than one parcel. Nothing is missing, it is on its way.{%- endif -%}")

def chain_row(n, title, body, last=False, dot_bg=BRICK, dot_fg="#FFFFFF", line=SAND, icon=None, pills=""):
    """Verticale stap met genummerde stip en doorlopende lijn (CSS-gradient; zonder gradient blijven de stippen)."""
    bg = "" if last else f"background-image:linear-gradient({line},{line});background-size:2px 100%;background-repeat:no-repeat;background-position:17px 0;"
    dot = (f"""<img src="{icon}" width="20" height="20" alt="" style="display:block;width:20px;height:20px;margin:8px auto 0 auto;">""" if icon else
           f"""<div style="{F}font-size:14px;line-height:36px;font-weight:700;color:{dot_fg};text-align:center;">{n}</div>""")
    return f"""<tr>
  <td width="36" valign="top" style="width:36px;{bg}"><div style="width:36px;height:36px;border-radius:18px;background-color:{dot_bg};{'border:1px solid '+SAND+';box-sizing:border-box;' if icon else ''}">{dot}</div></td>
  <td valign="top" style="padding:6px 0 {0 if last else 22}px 16px;{F}font-size:16px;line-height:22px;color:{INK};"><div style="font-weight:600;">{title}</div><div style="padding-top:4px;font-size:14px;line-height:21px;color:{SOFT};">{body}</div>{pills}</td>
</tr>\n"""

def pill(t, bg=PAPER, fg=INK, border=SAND):
    return f"""<span class="pill" style="display:inline-block;margin:0 4px 8px 0;padding:6px 12px;background-color:{bg};border:1px solid {border};border-radius:20px;{F}font-size:12px;line-height:16px;font-weight:600;color:{fg};white-space:nowrap;">{t}</span>"""

def parcel_box(pad="18px 44px 0 44px"):
    return ("{%- if sk_ship > 1 -%}" + f"""<tr><td class="pad" style="padding:{pad};"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FBF3EF" style="background-color:#FBF3EF;border-radius:6px;border:1px solid #E3C9BE;"><tr><td style="padding:14px 18px;{F}font-size:14px;line-height:21px;color:{INK};"><span style="font-weight:600;color:{BRICK};">May arrive in more than one parcel.</span> {PARCEL_NOTE}</td></tr></table></td></tr>
""" + "{%- endif -%}\n")

def expect_chain(serif=False):
    head = B.eyebrow("WHAT HAPPENS NEXT") + (B.h2("Here&rsquo;s what to expect") if serif else h2i("Here&rsquo;s what to expect"))
    rows = "".join(chain_row(i + 1, t, b, last=(i == 3), dot_bg=(BRICK if i == 0 else PAPER), dot_fg=("#FFFFFF" if i == 0 else BRICK))
                   .replace("background-color:#FFFFFF;\">", "background-color:#FFFFFF;border:2px solid " + BRICK + ";box-sizing:border-box;\">")
                   for i, (t, b, _) in enumerate(STEPS_EXPECT))
    rows = rows.replace("line-height:36px;font-weight:700;color:" + BRICK, "line-height:32px;font-weight:700;color:" + BRICK)
    return head + f"""<tr><td class="pad" style="padding:22px 44px 0 44px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table></td></tr>\n""" + parcel_box()

def expect_row4():
    """Compacte 4-stappenrij (b4): 4 kolommen op desktop, 2x2 op mobiel."""
    def cell(i, t, b, ic):
        return f"""<td class="t4" width="25%" valign="top" align="center" style="width:25%;padding:0 4px;text-align:center;">
<div style="width:52px;height:52px;margin:0 auto;border-radius:26px;background-color:{PAPER};border:{'1px solid '+SAND if i else '2px solid '+BRICK};box-sizing:border-box;"><img src="{ic}" width="24" height="24" alt="" style="display:block;width:24px;height:24px;margin:{13 if i else 12}px auto 0 auto;"></div>
<div style="padding-top:10px;{F}font-size:11px;line-height:14px;letter-spacing:1.5px;font-weight:600;color:{BRICK};">STEP {i+1}</div>
<div style="padding-top:4px;{F}font-size:14px;line-height:19px;font-weight:600;color:{INK};">{t}</div></td>"""
    short = [("Order confirmed", "check"), ("Packed {{ sk_pack }}", "clock"), ("Shipped with tracking", "truck"), ("Delivered in {{ sk_days }} days", "gift")]
    cells = "".join(cell(i, t, "", ICON[ic]) for i, (t, ic) in enumerate(short))
    notes = B.para("Tracking comes by email{% if sk_ship > 1 %}, one email per parcel{% endif %}. Delivery is counted from the day it ships; peak weeks can add a few days. Want to change the address? Reply within {{ sk_cancel_window }}.", pad="10px 44px 0 44px", size=13, color=GREY, align="center")
    return (B.eyebrow("WHAT HAPPENS NEXT", align="center") + h2i("Here&rsquo;s what to expect", align="center")
            + f"""<tr><td class="pad" style="padding:22px 36px 0 36px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cells}</tr></table></td></tr>\n"""
            + notes + parcel_box())

# --- de vier pijlers (alleen goedgekeurde claims; DECISIONS 1 okt, 7 okt; skill sectie 3)
PILLARS = [
    dict(key="nontoxic", label="NON-TOXIC", title="No coating. Nothing to peel or flake.",
         body="A pure titanium cooking surface with no coatings. No PFAS, PFOA, or BPA, and no layer that can scratch off in a year.",
         short="No PFAS, PFOA, or BPA. No layer to scratch off.", icon="nocoat", pills=["No coatings", "No PFAS, PFOA, or BPA"]),
    dict(key="perf", label="PERFORMANCE", title="A real sear, then straight into the oven.",
         body="Heat it right and steak browns the way it should. Oven safe, metal utensil safe, dishwasher safe, works on every stovetop.",
         short="Oven safe, metal utensil safe, dishwasher safe.", icon="utensil", pills=["Oven safe", "Metal utensil safe", "Dishwasher safe"]),
    dict(key="life", label="TITANIUM", title="Built for life. Covered for 75 years.",
         body="There is nothing on it to wear out, so we cover it for 75 years against defects: a dent, a warped base, a loose handle.",
         short="Nothing to wear out, so we cover it against defects.", icon="warranty", pills=["75-year warranty", "The original hammered pan"]),
    dict(key="lab", label="LAB REPORTS", title="Tested PFAS-free. Read the report yourself.",
         body="Light Labs, an ISO/IEC 17025-accredited lab, tested for 31 PFAS compounds. Every one came back below the detection limit. Report no. 25895.",
         short="Light Labs tested 31 PFAS compounds. All below detection.", icon="pfas", pills=["Report no. 25895", "31 PFAS tested"]),
]
PILLARS_BOARD = [
    dict(key="nontoxic", label="NON-TOXIC", title="No plastic. No wood. No coating.",
         body="Pure titanium all the way through. Nothing to shave off into your food and nothing to soak up raw juices.",
         icon="nocoat", pills=["No plastic", "No coating"]),
    dict(key="perf", label="EVERY DAY", title="Rinse, wipe, done.",
         body="No oiling, no sanding, no stains that stay. Rinse it after raw meat and wipe it dry.",
         icon="utensil", pills=["Easy to clean", "Nothing to oil"]),
    dict(key="life", label="TITANIUM", title="Built for life. Covered for 75 years.",
         body="There is nothing on it to wear out, so we cover it for 75 years against defects.",
         icon="warranty", pills=["75-year warranty"]),
    dict(key="try", label="RISK FREE", title="Try it for 30 days.",
         body="Not for you? Send it back within 30 days of delivery. Join 100,000+ happy customers.",
         icon="returns", pills=["30-day returns", "100,000+ customers"]),
]
PILLARS_OTHER = [
    dict(key="nontoxic", label="NON-TOXIC", title="Pure titanium. No coating.",
         body="Nothing to peel, flake or wear off into your food or drink.",
         icon="nocoat", pills=["No coating"]),
    dict(key="life", label="TITANIUM", title="Built for life. Covered for 75 years.",
         body="Titanium does not rust or wear out, so we cover it for 75 years against defects.",
         icon="warranty", pills=["75-year warranty"]),
    dict(key="try", label="RISK FREE", title="Try it for 30 days.",
         body="Not for you? Send it back within 30 days of delivery. Join 100,000+ happy customers.",
         icon="returns", pills=["30-day returns", "100,000+ customers"]),
]
PILLAR_HEAD_EB = "WHY YOU CHOSE THIS PAN"
PILLAR_HEAD = "You picked the pan with<br>nothing to wear off."
LAB_LINK = f"""<a href="{LAB_URL}" style="{F}font-size:14px;line-height:20px;font-weight:600;color:{BRICK};text-decoration:underline;">Read the lab report&nbsp;&rarr;</a>"""

def lab_card(pad="0", big=True):
    """Donkere 'wat je krijgt is wat we testten'-kaart met badges (geen verzonnen certificaten: alleen eigen feiten)."""
    def badge(ic, t):
        return f"""<td class="g2" width="50%" valign="top" style="width:50%;padding:0 6px 12px 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#353231" style="background-color:#353231;border-radius:30px;"><tr><td width="40" style="width:40px;padding:6px 0 6px 8px;"><div style="width:30px;height:30px;border-radius:15px;background-color:#F8F7F2;"><img src="{ic}" width="18" height="18" alt="" style="display:block;width:18px;height:18px;margin:0 auto;padding-top:6px;"></div></td><td style="padding:6px 12px 6px 8px;{F}font-size:13px;line-height:17px;font-weight:600;color:#FFFFFF;">{t}</td></tr></table></td>"""
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{INK}" style="background-color:{INK};border-radius:8px;"><tr><td bgcolor="{INK}" style="background-color:{INK};padding:28px 26px 18px 26px;">
<div style="{F}font-size:11px;line-height:16px;letter-spacing:2px;font-weight:600;color:#E3A28C;">THIRD-PARTY TESTED</div>
<div class="{'bign' if big else ''}" style="{F}font-size:{'56px' if big else '28px'};line-height:{'58px' if big else '32px'};font-weight:700;letter-spacing:-1.5px;color:#FFFFFF;padding-top:8px;">{'No. 25895' if big else 'What you get is exactly what we tested.'}</div>
<div style="{F}font-size:15px;line-height:23px;color:#DAD6CF;padding-top:10px;">{'What you get is exactly what we tested. ' if big else ''}Light Labs, an ISO/IEC 17025-accredited lab, tested our titanium cooking surface for 31 PFAS compounds. Every one came back below the detection limit.</div>
<div style="padding-top:14px;"><a href="{LAB_URL}" style="{F}font-size:14px;line-height:20px;font-weight:600;color:#FFFFFF;text-decoration:underline;">Read the report yourself &rarr;</a></div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:20px;"><tr>{badge(ICON['pfas'], 'Tested PFAS-free')}{badge(ICON['nocoat'], 'No coatings')}</tr><tr>{badge(ICON['warranty'], '75-year warranty')}{badge(ICON['customers'], '100,000+ customers')}</tr></table>
</td></tr></table>"""

def first_week(variant):
    """Eerste week met titanium: hitte, olie, eten. Benjamin als oprichter."""
    steps = [("Heat", "Medium heat for 2 to 3 minutes. A drop of water should bead up and glide."),
             ("Oil", "A teaspoon of oil. Swirl it around."),
             ("Food", "Lay it in and leave it until it lets go on its own. Start with eggs.")]
    serif = variant == "b2"
    head = B.eyebrow("YOUR FIRST WEEK WITH TITANIUM") + (B.h2("Heat, oil, food. In that order.") if serif else h2i("Heat, oil, food. In that order."))
    note = B.para("One tip from me before it arrives. Titanium has no coating, so food lets go because of heat, not chemistry. Cold metal grabs your food, hot metal lets it go. Skip the heat and it sticks; give it one more minute next time.", pad="10px 44px 0 44px", color=SOFT)
    if variant == "b3":
        rows = "".join(chain_row(i + 1, t, b, last=(i == 2)) for i, (t, b) in enumerate(steps))
        body = f"""<tr><td class="pad" style="padding:20px 44px 0 44px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table></td></tr>\n"""
    else:
        def cell(i, t, b):
            return f"""<td class="g2" width="33%" valign="top" style="width:33%;padding:0 6px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{PAPER}" style="background-color:{PAPER};border:1px solid {SAND};border-radius:8px;"><tr><td class="wkc" valign="top" height="112" style="height:112px;padding:16px 16px 16px 16px;"><div style="{F}font-size:15px;line-height:22px;font-weight:600;color:{INK};"><span style="display:inline-block;width:22px;height:22px;border-radius:11px;background-color:{BRICK};color:#FFFFFF;font-size:12px;line-height:22px;text-align:center;margin-right:8px;">{i+1}</span>{t}</div><div style="padding-top:4px;{F}font-size:13px;line-height:19px;color:{SOFT};">{b}</div></td></tr></table></td>"""
        cells = "".join(cell(i, t, b) for i, (t, b) in enumerate(steps))
        body = f"""<tr><td class="pad" style="padding:20px 38px 0 38px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{cells}</tr></table></td></tr>\n"""
        if variant == "b2":
            body = (f"""<tr><td class="pad" style="padding:22px 44px 0 44px;"><img src="{shop(PIL['egg'], 1024, 640)}" width="512" alt="A fried egg in a hammered titanium pan" style="display:block;width:100%;max-width:512px;height:auto;border-radius:6px;"></td></tr>\n""" + body)
    sign = B.para("Questions on your first cook? Reply to this email and our team will help.<br><br>Benjamin<br><span style=\"color:#727272;\">Founder, Siraat</span>", pad="20px 44px 0 44px", size=15)
    return head + note + body + sign

def stars_line(pad="0 44px 34px 44px"):
    return f"""<tr><td class="pad" align="center" style="padding:{pad};text-align:center;"><div style="{F}font-size:18px;line-height:22px;letter-spacing:3px;color:{BRICK};">&#9733;&#9733;&#9733;&#9733;&#9733;</div><div style="padding-top:4px;{F}font-size:13px;line-height:19px;color:{SOFT};">You are in good company.</div></td></tr>\n"""

def practical(serif):
    head = B.eyebrow("THE PRACTICAL PART") + (B.h2("Everything else, in one place") if serif else h2i("Everything else, in one place"))
    help_ = (B.eyebrow("HELP", pad="34px 44px 0 44px") + (B.h2("Need to change something?") if serif else h2i("Need to change something?", size=24))
        + B.para("Reply to this email or write to <a href=\"mailto:{{ sk_support }}\" style=\"color:#AC3B19;\">{{ sk_support }}</a>. Our team answers within 1 hour on business days.")
        + B.para("<span style=\"font-weight:600;\">Change the address or cancel:</span> ask within {{ sk_cancel_window }} of ordering. After that your order may already be packed. Write anyway and we will tell you honestly what is still possible.", pad="10px 44px 0 44px")
        + B.icons3(pad="28px 44px 18px 44px") + stars_line())
    blocks = B.SUB + B.gifts() + B.items("Your receipt")
    if not serif:
        blocks = blocks.replace(SERIF, F + "font-weight:600;letter-spacing:-0.5px;").replace("font-size:32px;line-height:36px", "font-size:24px;line-height:30px").replace("font-size:26px;line-height:30px", "font-size:20px;line-height:26px")
    return (B.rule("38px 44px 0 44px") + head + blocks + B.address() + help_)

def section_head(serif, align="left"):
    return (B.eyebrow(PILLAR_HEAD_EB, pad="42px 44px 0 44px", align=align)
            + (B.h2(PILLAR_HEAD, align=align) if serif else h2i(PILLAR_HEAD, align=align)))

# ------------------------------------------------------------ B2 Editorial
def pillars_editorial():
    out = section_head(True)
    for i, p in enumerate(PILLARS):
        rtl = i % 2 == 1
        if p["key"] == "lab":
            out += f"""<tr><td class="pad" style="padding:30px 44px 0 44px;">{lab_card(big=True)}</td></tr>\n"""
            continue
        img = f"""<td class="stack stackimg" width="256" valign="top" dir="ltr" style="width:256px;padding:0;"><img src="{shop(PIL[p['key']], 600, 500)}" width="256" alt="" style="display:block;width:256px;height:auto;border-radius:6px;"></td>"""
        pad_t = "0 0 0 24px" if not rtl else "0 24px 0 0"
        txt = f"""<td class="stack stacktxt" valign="middle" dir="ltr" style="padding:{pad_t};">
<div style="{F}font-size:11px;line-height:16px;letter-spacing:2px;font-weight:600;color:{BRICK};">{i+1:02d} &middot; {p['label']}</div>
<div class="h2" style="{SERIF}font-size:28px;line-height:32px;color:{INK};padding-top:8px;">{p['title']}</div>
<div style="{F}font-size:15px;line-height:23px;color:{SOFT};padding-top:10px;">{p['body']}</div></td>"""
        out += f"""<tr><td class="pad" style="padding:30px 44px 0 44px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" dir="{'rtl' if rtl else 'ltr'}"><tr>{img}{txt}</tr></table></td></tr>\n"""
    return out

def variant_b2():
    body = (hero("Order {{ order_name }} is in. Here is exactly what happens next.")
        + welcome(serif=True) + B.rule("36px 44px 0 44px") + expect_chain(serif=True)
        + pillars_editorial() + B.rule("40px 44px 0 44px") + first_week("b2") + practical(True))
    return body, "B2 Editorial", "Your order is confirmed. Here is exactly what happens next, and how to cook your first egg in titanium."

# ------------------------------------------------------------ B3 Steps (Create-achtig)
def _steps(pillars, eyebrow, head, lab):
    out = B.eyebrow(eyebrow, pad="42px 44px 0 44px") + h2i(head)
    rows = ""
    for i, p in enumerate(pillars):
        pills = '<div style="padding-top:10px;">' + "".join(pill(t, bg=CREAM) for t in p["pills"]) + "</div>"
        body = (p["short"] + " Details just below.") if p["key"] == "lab" else p["body"]
        rows += chain_row(i + 1, f"<span style=\"{F}font-size:11px;letter-spacing:2px;color:{BRICK};\">{p['label']}</span><br>{p['title']}", body,
                          last=(i == len(pillars) - 1), dot_bg=PAPER, icon=ICON[p["icon"]], pills=pills)
    out += f"""<tr><td class="pad" style="padding:24px 44px 0 44px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table></td></tr>\n"""
    if lab:
        out += f"""<tr><td class="pad" style="padding:26px 44px 0 44px;">{lab_card(big=False)}</td></tr>\n"""
    return out

def pillars_steps():
    return ("{% if sk_kind == 'pan' %}" + _steps(PILLARS, PILLAR_HEAD_EB, PILLAR_HEAD, True) + benefit_pills()
            + "{% elsif sk_kind == 'board' %}" + _steps(PILLARS_BOARD, "WHY YOU CHOSE THIS BOARD", "You picked the board<br>that stays clean.", False)
            + "{% endif %}")

def benefit_pills():
    return f"""<tr><td class="pad" align="center" style="padding:20px 44px 0 44px;text-align:center;">{pill('Dishwasher safe')}{pill('Metal utensil safe')}{pill('Oven safe')}{pill('Induction ready')}{pill('No seasoning')}</td></tr>\n"""

def variant_b3():
    body = (hero("Order {{ order_name }} is in. Here is exactly what happens next.")
        + welcome(serif=False) + B.rule("36px 44px 0 44px") + expect_chain(serif=False)
        + pillars_steps() + "{% if sk_kind == 'pan' %}" + B.rule("36px 44px 0 44px") + first_week("b3") + "{% endif %}" + practical(False))
    return body, "B3 Steps", "Your order is confirmed. Four steps until it is in your kitchen, and three for your first cook."

# ------------------------------------------------------------ B4 Cards
def pillars_cards():
    def card(i, p):
        if p["key"] == "lab":
            top = f"""<td bgcolor="{INK}" style="background-color:{INK};border-radius:8px 8px 0 0;height:150px;" height="150" align="center" valign="middle"><div style="{F}font-size:11px;line-height:16px;letter-spacing:2px;font-weight:600;color:#E3A28C;">REPORT</div><div class="c2big" style="{F}font-size:34px;line-height:38px;font-weight:700;letter-spacing:-1px;color:#FFFFFF;">No. 25895</div><div style="{F}font-size:12px;line-height:16px;color:#DAD6CF;padding-top:4px;">Light Labs &middot; 31 PFAS tested</div></td>"""
        else:
            top = f"""<td style="padding:0;border-radius:8px 8px 0 0;overflow:hidden;"><img src="{shop(PIL[p['key']], 520, 300)}" width="260" height="150" alt="" class="c2img" style="display:block;width:100%;max-width:260px;height:150px;object-fit:cover;border-radius:8px 8px 0 0;"></td>"""
        link = f"<div style=\"padding-top:8px;\">{LAB_LINK}</div>" if p["key"] == "lab" else ""
        return f"""<td class="c2" width="50%" valign="top" style="width:50%;padding:0 6px 12px 6px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{PAPER}" style="background-color:{PAPER};border:1px solid {SAND};border-radius:8px;">
<tr>{top}</tr>
<tr><td class="c2in" style="padding:14px 16px 18px 16px;"><table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td width="22" valign="middle" style="width:22px;"><img src="{ICON[p['icon']]}" width="18" height="18" alt="" style="display:block;width:18px;height:18px;"></td><td valign="middle" style="padding-left:6px;{F}font-size:11px;line-height:16px;letter-spacing:2px;font-weight:600;color:{BRICK};">{p['label']}</td></tr></table>
<div class="c2t" style="padding-top:8px;{F}font-size:16px;line-height:21px;font-weight:600;color:{INK};">{p['title']}</div>
<div style="padding-top:6px;{F}font-size:13px;line-height:19px;color:{SOFT};">{p['short']}</div>{link}</td></tr></table></td>"""
    grid = (f"<tr>{card(0, PILLARS[0])}{card(1, PILLARS[1])}</tr><tr>{card(2, PILLARS[2])}{card(3, PILLARS[3])}</tr>")
    return (section_head(False, align="center")
            + f"""<tr><td class="pad" style="padding:22px 38px 0 38px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{grid}</table></td></tr>\n"""
            + benefit_pills())

def variant_b4():
    body = (hero("Order {{ order_name }} is in. Here is exactly what happens next.")
        + welcome(serif=False) + B.rule("34px 44px 0 44px") + expect_row4()
        + pillars_cards() + B.rule("34px 44px 0 44px") + first_week("b4") + practical(False))
    return body, "B4 Cards", "Your order is confirmed. What happens next, why titanium, and your first cook, at a glance."

def build():
    for key, fn in (("b2", variant_b2), ("b3", variant_b3), ("b4", variant_b4)):
        body, name, pre = fn()
        html = (SETUP.replace("VARIANT_NAME", f"variant {key.upper()} ({name})")
                + HEAD.replace("PREHEADER", pre) + B.HEADER + body + B.FOOTER)
        assert "—" not in html and "–" not in html, f"dash in {key}"
        assert "loop_subscriptions" not in html
        out = os.path.join(HERE, f"variant-{key}.liquid")
        open(out, "w").write(html)
        print("written", out, len(html))

if __name__ == "__main__":
    build()
