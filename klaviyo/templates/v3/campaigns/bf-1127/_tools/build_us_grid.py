"""US za 28 nov 14:00 lokaal: productgrid, bovenaan 12-pc $499 (BF499, vandaag), raster tegen saleprijzen zonder code.
Vaste header/footer. Gebruik: python3 -I build_intl_sat.py"""
import os, re
T = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(T)
src = open(os.path.join(T, 'build.py')).read().split("os.makedirs(os.path.join(T, '.preview')")[0]
g = {'__file__': os.path.join(T, 'build.py')}; exec(src, g)
p, btn, row, shell, FIRST, MUTED, SANS, SERIF, INK, RED = (g[k] for k in ('p','btn','row','shell','FIRST','MUTED','SANS','SERIF','INK','RED'))
SITE='https://siraatskitchen.com'; GOLD='#F2C14E'
def L(path,c):
    pre=f'{SITE}/discount/BF499?redirect={path}&' if 'cookware-set' in path else f'{SITE}{path}?'
    return f'{pre}utm_source=klaviyo&utm_medium=email&utm_campaign=bf-1128-us-grid&utm_content={c}'
IMG12S='https://cdn.shopify.com/s/files/1/0907/0877/1156/files/12pcsset.webp'
IMG=lambda u: u.split('?')[0]+'?width=560&height=560&crop=center&format=pjpg'
P=[('Pan Pro Standard','The pan Siraat started with. Eggs to steak.','/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern','https://cdn.shopify.com/s/files/1/0907/0877/1156/files/Titanium_hammered_pan_pro_standard_b69d1fc5-43d8-40a5-9ad7-523bdddc54d4.webp'),
   ('Pan Pro Large','Big enough for a crowd. Even heat edge to edge.','/products/titanium-hammered-pan-pro-large','https://cdn.shopify.com/s/files/1/0907/0877/1156/files/Titanium_hammered_pan_pro_large_6d4ce352-c4ff-48c9-b4d1-170232007e4f.webp'),
   ('Wok Pan Pro','High sides, fast heat. Stir-fry night, sorted.','/products/titanium-hammered-wok-pan-pro','https://cdn.shopify.com/s/files/1/0907/0877/1156/files/siraat-wok-real-side.jpg'),
   ('Deep Pan Pro','For braises, sauces and Sunday stews.','/products/titanium-hammered-deep-pan-pro','https://cdn.shopify.com/s/files/1/0907/0877/1156/files/DeepHammeredPan.webp'),
   ('Roasting Pan','Rack included. Ready for the holiday table.','/products/titanium-hammered-roasting-pan','https://cdn.shopify.com/s/files/1/0907/0877/1156/files/Roastingpanwithrack.webp'),
   ('Titanium Cutting Board','Anti-microbial titanium. No plastic in your food prep.','/products/titanium-cutting-board-v2','https://cdn.shopify.com/s/files/1/0907/0877/1156/files/Titanium_Cutting_Board_08.jpg')]
def card(t,d,path,img,i):
    k=re.sub(r'\W+','-',t.lower())
    return (f'<td class="gcol" width="50%" valign="top" style="width:50%;padding:0 6px 14px 6px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#F1EEE7" style="background:#F1EEE7;border-radius:8px;">'
            f'<tr><td style="padding:10px 10px 0 10px;"><a href="{L(path,k+"-img")}"><img src="{IMG(img)}" width="250" alt="{t}" style="display:block;width:100%;max-width:250px;height:auto;border:0;border-radius:6px;"></a></td></tr>'
            f'<tr><td align="center" style="padding:10px 12px 0 12px;"><span style="display:inline-block;background:{RED};color:#FFFFFF;font-family:{SANS};font-size:11px;line-height:13px;font-weight:800;letter-spacing:1px;padding:5px 8px;border-radius:4px;">UP TO 70% OFF</span></td></tr>'
            f'<tr><td align="center" style="padding:8px 12px 0 12px;font-family:{SANS};font-size:17px;line-height:22px;font-weight:800;color:{INK};">{t}</td></tr>'
            f'<tr><td align="center" style="padding:4px 12px 0 12px;font-family:{SANS};font-size:13px;line-height:19px;color:{MUTED};">{d}</td></tr>'
            f'<tr><td align="center" style="padding:12px 12px 16px 12px;"><a href="{L(path,k+"-btn")}" style="display:inline-block;background:{INK};color:#FFFFFF;font-family:{SANS};font-size:12px;line-height:14px;font-weight:800;letter-spacing:1px;text-decoration:none;padding:11px 14px;border-radius:4px;">SHOP THE SALE</a></td></tr>'
            f'</table></td>')
grid=''.join('<tr>'+card(*P[i],i)+card(*P[i+1],i+1)+'</tr>' for i in range(0,6,2))
grid=f'<tr><td style="padding:22px 14px 6px 14px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{grid}</table></td></tr>\n'
SALE='/collections/black-friday-sale'; SET='/products/titanium-hammered-cookware-set'
hero=(f'<tr><td bgcolor="#111111" style="background-color:#111111;padding:36px 30px 34px 30px;text-align:center;font-family:{SANS};">'
      f'<div style="font-size:13px;line-height:18px;letter-spacing:2.5px;font-weight:800;color:{GOLD};">BLACK FRIDAY WEEKEND &middot; TODAY ONLY</div>'
      f'<div class="h2" style="font-size:44px;line-height:48px;font-weight:900;color:#FFFFFF;padding-top:12px;">THE 12-PIECE SET<br>$499</div>'
      f'<div style="font-family:{SERIF};font-size:22px;line-height:28px;color:#FFFFFF;padding-top:12px;"><s style="color:#BDB8B0;">$649</s> &middot; ends tonight at midnight ET</div>'
      f'<div style="padding:18px 30px 0 30px;"><a href="{L(SET,"hero-img")}"><img src="{IMG(IMG12S)}" width="480" alt="The 12-Piece Titanium Hammered Set" style="display:block;width:100%;max-width:480px;height:auto;border:0;border-radius:6px;"></a></div>'
      f'<div style="padding:22px 20px 0 20px;">'+btn('Get my 12-piece set for $499',L(SET,'hero'))+'</div>'
      f'<div style="font-size:13px;line-height:19px;color:#BDB8B0;padding-top:12px;">Already applied &middot; Free shipping &middot; 30-day returns &middot; 100,000+ happy customers</div></td></tr>\n')
intro=row(p(f'Hey {FIRST},')+p('These are the pans people picked up most this week. All still up to 70% off, with 5 free gifts on every order. And the 12-piece set above is $499 until midnight ET tonight.'),'28px 40px 0 40px')
outro=row('<div style="padding:6px 0 10px 0;">'+btn('Shop the Black Friday sale',L(SALE,'bottom'))+'</div>'+
          p('Free shipping. 30-day returns. 100,000+ happy customers.',13,19,MUTED,'0 0 6px 0','center'),'10px 40px 34px 40px')
h=shell('What everyone picked up this week','Up to 70% off + the 12-piece set at $499 until midnight ET.',hero+intro+grid+outro)
h=h.replace('@media only screen and (max-width:620px){','@media only screen and (max-width:620px){.gcol{display:block!important;width:100%!important;padding:0 0 14px 0!important}')
assert '—' not in h
open(os.path.join(C,'us-1128-grid.html'),'w').write(h)
pv=h.replace(FIRST,'Sarah')
for t in ['{% unsubscribe_link %}','{% manage_preferences_link %}','{% web_view_link %}']: pv=pv.replace(t,'#')
pv=re.sub(r'\{%.*?%\}','',pv).replace('{{ organization.name }}','Siraats Kitchen').replace('{{ organization.full_address }}','Address').replace('{{ sk_ref }}','')
os.makedirs(os.path.join(T,'.preview'),exist_ok=True); open(os.path.join(T,'.preview','us-1128-grid.html'),'w').write(pv); print('ok',len(h))
