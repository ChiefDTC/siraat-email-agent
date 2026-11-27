"""Strategist-mails VERBATIM (Floris 27 nov: alles uit de docs houden, alleen Ali -> Benjamin; Lucas past aan).
Enige andere wijziging: gedachtestreepjes (huisregel) vervangen door ':' of '·'. Knoppen linken met SET30 (30% op 12-pc, US).
Gebruik: python3 -I build_verbatim.py"""
import os, re
H = os.path.dirname(os.path.abspath(__file__))
BT = os.path.join(os.path.dirname(H), 'bf-1127', '_tools')
src = open(os.path.join(BT, 'build.py')).read().split("os.makedirs(os.path.join(T, '.preview')")[0]
g = {'__file__': os.path.join(BT, 'build.py')}; exec(src, g)
p, btn, row, shell, MUTED, SANS, INK, RED, IMG12, LINE, PANEL = (g[k] for k in ('p','btn','row','shell','MUTED','SANS','INK','RED','IMG12','LINE','PANEL'))
SITE='https://siraatskitchen.com'; SET='/products/titanium-hammered-cookware-set'
def L(camp,c): return f'{SITE}/discount/SET30?redirect={SET}&utm_source=klaviyo&utm_medium=email&utm_campaign={camp}&utm_content={c}'
def C(t,size=16,w='400',color=INK,pad='0 0 10px 0'): return f'<div style="font-family:{SANS};font-size:{size}px;line-height:{int(size*1.45)}px;font-weight:{w};color:{color};text-align:center;padding:{pad};">{t}</div>'
def Hd(t): return f'<div style="font-family:{SANS};font-size:24px;line-height:30px;font-weight:900;color:{INK};padding:6px 0 12px 0;">{t}</div>'
def ul(items): return '<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 12px 0;">'+''.join(f'<tr><td valign="top" style="font-family:{SANS};font-size:16px;line-height:24px;color:{INK};padding:0 8px 6px 0;">&bull;</td><td style="font-family:{SANS};font-size:16px;line-height:24px;color:{INK};padding-bottom:6px;">{i}</td></tr>' for i in items)+'</table>'
def table(head,rows):
    h=''.join(f'<td style="padding:10px 8px;font-family:{SANS};font-size:12px;font-weight:800;color:#FFFFFF;background:{RED if i==1 else INK};">{x}</td>' for i,x in enumerate(head))
    b=''.join('<tr>'+''.join(f'<td style="padding:10px 8px;font-family:{SANS};font-size:14px;line-height:20px;color:{INK};background:{"#FFFFFF" if j%2==0 else PANEL};">{x}</td>' for x in r)+'</tr>' for j,r in enumerate(rows))
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid {LINE};margin-bottom:14px;"><tr>{h}</tr>{b}</table>'
def bt(camp,label,c): return '<div style="padding:8px 0 18px 0;">'+btn(label,L(camp,c))+'</div>'
IMG=lambda camp: f'<a href="{L(camp,"img")}"><img src="{IMG12}" width="520" alt="The 12-Piece Titanium Hammered Set" style="display:block;width:100%;max-width:520px;height:auto;border:0;margin:6px 0 14px 0;"></a>'
# ---------- doc 1 ----------
A='bf-verbatim-a'
a=(row(C('BLACK FRIDAY JUST WENT LIVE!',15,'800',RED,'6px 0 6px 0')+C('30% OFF',56,'900')+C('The 12-Piece Titanium Hammered Set',22,'600')+C('+',22,'400')+C('5 FREE GIFTS',30,'900')+
       C('Worth $555, Including a Mystery Gift and More!',16,'400',MUTED)+IMG(A)+bt(A,'GRAB YOUR SET','hero'),'30px 40px 10px 40px')+
   row(Hd('EVERYTHING INSIDE OUR 12-PIECE TITANIUM SET')+p('3 pans &middot; 3 pots &middot; 6 fitted lids. A complete kitchen in one decision.')+
       ul(['<b>8" Mini Pan + Lid:</b> Eggs, single portions, quick sauces.','<b>10" Small Pan + Lid:</b> Everyday saut&eacute;ing, veggies, and weeknight dinners.',
           '<b>12" Large Pan + Lid:</b> Steaks, family-size meals, and big one-pan dishes.','<b>2-Qt Saucepan + Lid:</b> Sauces, grains, and reheating.',
           '<b>3-Qt Saucepan + Lid:</b> Pasta, soups, and sides.','<b>8-Qt Stockpot + Lid:</b> Stocks, stews, chili, and batch cooking.'])+
       p('Every piece has a pure, hand-hammered titanium cooking surface. No coating, third-party tested PFAS-free, and covered by a 75-year warranty.')+bt(A,'SHOP THE SET','inside'),'20px 40px 10px 40px')+
   row(Hd('SIRAAT VS. COATED COOKWARE')+table(['FEATURE','Siraat','Coated / PFAS Pans'],[['PFAS &amp; PTFE free','&#10003;','&#10007;'],['No coating to scratch or flake','&#10003;','&#10007;'],
       ['Safe with metal utensils','&#10003;','&#10007;'],['Oven safe to 1000&deg;F','&#10003;','Limited'],['Induction compatible','&#10003;','Varies'],['Dishwasher safe','&#10003;','Degrades'],['Lasts','75-year warranty','1&ndash;2 years']]),'20px 40px 10px 40px')+
   row(Hd('WARNING: THIS DEAL WON&rsquo;T LAST')+p('On this exact deal we are not making any profit, so it won&rsquo;t be around for much longer. Take advantage now and upgrade your cookware for a lifetime!')+
       bt(A,'CLAIM 30% OFF + 5 FREE GIFTS','deal')+C('&#10003; Tested PFAS-Free &middot; &#10003; 75-Year Warranty &middot; &#10003; 30-Day Returns &middot; &#10003; Free Shipping From the USA',13,'400',MUTED,'0 0 10px 0'),'20px 40px 30px 40px'))
# ---------- doc 2 ----------
B='bf-verbatim-b'
P=lambda *xs: ''.join(p(x) for x in xs)
b=(row(C('BLACK FRIDAY &middot; BIGGEST SALE IN SIRAAT HISTORY',14,'800',RED,'6px 0 4px 0')+C('THIS IS THE ONE.',26,'900')+C('30% OFF',56,'900',RED)+C('THE 12-PIECE TITANIUM HAMMERED SET',20,'800')+
       C('+ 5 FREE GIFTS WORTH $555',18,'800')+C('Including a Mystery Gift You Won&rsquo;t See Coming',15,'400',MUTED)+IMG(B)+bt(B,'&#128293; GRAB YOUR SET &middot; BLACK FRIDAY PRICE &rarr;','hero')+
       C('&#10022; Free gifts added automatically at checkout<br>&#10022; Free express shipping to the US<br>&#10022; This price has NEVER been offered before. It won&rsquo;t be offered again.',14,'400',MUTED,'0 0 10px 0'),'30px 40px 10px 40px')+
   row(Hd('YOUR KITCHEN HAS A SECRET.')+P('Go to your kitchen right now.','Pull out your frying pan. The one you use every morning. The one you cook the kids&rsquo; eggs on. The one you&rsquo;ve had for 3, 5, maybe 8 years.',
       'Hold it under the light.','Run your thumb across the surface. Slowly.','<b>Feel the scratches?</b>','<b>Feel the rough patches where the smooth black used to be?</b>','<b>Feel the bare metal underneath?</b>',
       'That&rsquo;s not normal wear. That&rsquo;s the coating leaving your pan. And it didn&rsquo;t evaporate. It went somewhere. It went into your food.','Last month. Last year. Every meal. Every plate. Every person at your table.',
       'The coating on non-stick pans is made with PFAS: per- and polyfluoroalkyl substances. They call them forever chemicals because once they&rsquo;re inside you, they don&rsquo;t leave. Not in a week. Not in a year. Not ever. They just build up.',
       'A clinic in Phoenix studied 47 women with unexplained fatigue, thyroid problems, joint pain, and brain fog. Ages 45-67. No common medication. No common diet.','One common factor: all 47 were cooking on non-stick pans with degraded coatings.',
       'Every single one had PFAS levels between 4x and 11x the national median.','The source wasn&rsquo;t their water. Wasn&rsquo;t their food packaging. It was the pan sitting on their stove. Their pans look exactly like yours.'),'26px 40px 6px 40px')+
   row(Hd('WE BUILT THE PAN THAT ENDS THE CYCLE.')+P('The Siraat 12 Piece Titanium Hammered Set is not coated. Not sprayed. Not infused. Not &ldquo;titanium-reinforced.&rdquo; Not &ldquo;titanium-ceramic.&rdquo; Not any of the 14 made-up compound words the industry invented to hide a coating behind a metal name.',
       '<b>It is pure titanium.</b>','The cooking surface is titanium. The metal. Element number 22 on the periodic table. There is nothing on top of it. There is nothing between it and your food. There is nothing to scratch, flake, chip, degrade, or end up in your bloodstream.',
       'We sent all 12 pieces to Light Labs for independent testing. Not a sample. Not the flagship pan. All 12.','Every single piece came back ZERO PFAS detected.','Not low. Not &ldquo;within safe limits.&rdquo; Not &ldquo;below the threshold.&rdquo; Zero.',
       'The full lab report is published on our website. We show what other brands bury.'),'20px 40px 6px 40px')+
   row(Hd('12 PIECES. ALL PURE TITANIUM. ALL TESTED. ALL ZERO.')+ul(['&#127859; <b>8" Mini Pan + Lid:</b> Eggs, single portions, quick sauces. The one you&rsquo;ll reach for first.','&#127859; <b>10" Small Pan + Lid:</b> Everyday saut&eacute;ing, veggies, weeknight dinners. The workhorse.',
       '&#127859; <b>12" Large Pan + Lid:</b> Steaks, family meals, one-pan dishes. Replaces three coated pans.','&#129752; <b>2-Qt Saucepan + Lid:</b> Sauces, grains, reheating. No coating to flake into the soup.',
       '&#129752; <b>3-Qt Saucepan + Lid:</b> Pasta, soups, sides. The one your mother should&rsquo;ve had.','&#129752; <b>8-Qt Stockpot + Lid:</b> Stocks, stews, chili, batch cooking. Feeds the whole family. For 75 years.'])+
       p('Every piece: hand-hammered titanium surface. Light Labs tested. Zero PFAS. 75-year warranty.')+bt(B,'&#128293; SHOP THE 12-PIECE SET &middot; 30% OFF &rarr;','inside'),'20px 40px 6px 40px')+
   row(Hd('SIRAAT vs. EVERYTHING ELSE IN YOUR KITCHEN')+table(['FEATURE','SIRAAT','YOUR &ldquo;NON-TOXIC&rdquo; PANS'],[['PFAS &amp; PTFE','&#9989; Zero. Tested. Published.','&#10060; Tested on new pans only.'],
       ['Coating','&#9989; No coating. Nothing to scratch.','&#10060; Degrades in 14 months.'],['Metal Utensils','&#9989; Use whatever you want.','&#10060; &ldquo;Wooden only&rdquo; = fragile coating.'],['Oven Safe','&#9989; 1000&deg;F.','&#9888;&#65039; Coating breaks down at heat.'],
       ['Dishwasher','&#9989; Titanium doesn&rsquo;t care.','&#10060; &ldquo;Hand wash&rdquo; = can&rsquo;t take it.'],['Lifespan','&#9989; 75-year warranty.','&#10060; 1-2 years. Buy another.'],['What You Pay For','&#9989; The last set you&rsquo;ll ever buy.','&#10060; A subscription to poison.']]),'20px 40px 6px 40px')+
   row(Hd('&#9888;&#65039; THIS DEAL IS COSTING US MONEY. THAT&rsquo;S THE POINT.')+P('Let&rsquo;s be honest.','The 12 piece set at 30% off. Plus 5 free gifts worth $555. Plus free express shipping.','We are not making a single dollar on this order.',
       'Benjamin, our founder, made the call himself. He said: &ldquo;Black Friday isn&rsquo;t about margin. It&rsquo;s about getting pure titanium into as many kitchens as possible before another year of coated pans goes by.&rdquo;',
       'This is the lowest price in Siraat history.','It has never been offered before. It will not be offered again.','When Black Friday ends, this page goes dark. The free gifts go away. The 30% disappears. And the next time you think about your pans, another 6 months of coating will be in your food.',
       'Don&rsquo;t wait 6 months. Don&rsquo;t wait 6 days. This is the moment.'),'20px 40px 6px 40px')+
   row(C('30% OFF + 5 FREE GIFTS WORTH $555',22,'900',RED,'6px 0 4px 0')+C('THE LAST COOKWARE SET YOUR KITCHEN WILL EVER NEED.',16,'800')+bt(B,'&#128293; CLAIM BLACK FRIDAY DEAL &rarr;','deal')+
       ul(['&#9989; Light Labs Tested &rarr; Zero PFAS Across All 12 Pieces','&#9989; 75-Year Warranty &rarr; Every Pan, Every Pot, Every Lid','&#9989; 30-Day Money-Back Guarantee &rarr; No Questions, No Hassle','&#9989; Free Express Shipping &rarr; Anywhere in the USA','&#9989; 100,000+ Families Already Switched']),'20px 40px 6px 40px')+
   row(Hd('P.S.')+P('Tonight, after dinner, do one thing. Pick up your frying pan. Turn it over. Look at the surface under the kitchen light.','If you see scratches &rarr; the coating is in your food.','If you see bare metal &rarr; the coating has been in your food for years.',
       'If the pan looks fine &rarr; flip it over and check again. It&rsquo;s never fine.','The 47 women in Phoenix didn&rsquo;t know either. They thought the fatigue was just aging. They thought the thyroid problems ran in the family. They thought brain fog was stress.',
       'It was the pan. It&rsquo;s always the pan.','<b>30% off. 5 free gifts. 75 year warranty. This week only.</b>')+bt(B,'SHOP NOW &rarr;','ps'),'20px 40px 30px 40px'))
for n,body,title,pre in [('verbatim-a-doc1',a,'Black Friday Is Live','Upgrade your whole cookware for 30% OFF!'),
                         ('verbatim-b-doc2',b,"Black Friday: We're giving away $555 worth of free gifts. Here's why.",'30% off the only cookware set with zero coating. Zero PFAS. Zero lies. + $555 in free gifts.')]:
    h=shell(title,pre,body); assert '—' not in h and 'Ali' not in h
    open(os.path.join(H,n+'.html'),'w').write(h)
    pv=h
    for t in ['{% unsubscribe_link %}','{% manage_preferences_link %}','{% web_view_link %}']: pv=pv.replace(t,'#')
    pv=re.sub(r'\{%.*?%\}','',pv).replace('{{ organization.name }}','Siraats Kitchen').replace('{{ organization.full_address }}','Address').replace('{{ sk_ref }}','')
    open(os.path.join(H,n+'.preview.html'),'w').write(pv); print(n,len(h))
