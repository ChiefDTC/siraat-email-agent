"""Bouwt Klaviyo-HTML en een lokale preview uit een bron-template met {{IMG}}.
Gebruik: python3 -I scripts/build_template.py <bron.html> <assets-map> <urls.txt>
Schrijft <bron>.klaviyo.html (CDN-links) en <bron-zonder-.html>-preview.html (lokale beelden, voorbeelddata)."""
import sys,re,os
src,assets,urls=sys.argv[1:4]
u=dict(l.split() for l in open(urls) if l.strip()) if os.path.exists(urls) else {}
h=open(src).read()
P=os.path.join(os.path.dirname(os.path.abspath(src)),'partials')
d=os.path.dirname(os.path.abspath(src))
while not os.path.isdir(os.path.join(d,'partials')) and os.path.dirname(d)!=d: d=os.path.dirname(d)
P=os.path.join(d,'partials'); R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','klaviyo','templates','partials')
h=h.replace('{{HEADER}}',open(os.path.join(P,'header.html')).read()).replace('{{FOOTER}}',open(os.path.join(P,'footer.html')).read())
# Blokken uit klaviyo/templates/partials/blocks: {{BLOCK:naam key="waarde"}} met [[key]] in het blok
B=os.path.join(R,'blocks'); SH=os.path.join(R,'shared')
DEF={'codebar':{'text':'EXTRA 10% OFF YOUR ORDER &middot; CODE','code':'HI10'},
 'cta':{'pad':'24px 44px 6px 44px','sub':''},
 'icons':{'pad':'22px 44px 6px 44px','icon4':'pfas-tested','text4':'PFAS<br>LAB TESTED'},
 'icons-int':{'pad':'22px 44px 6px 44px','icon4':'no-duties','text4':'NO IMPORT<br>DUTIES'},
 'gifts':{'pad':'30px 44px 6px 44px','eyebrow':'WITH EVERY ORDER','headline':'$70 in gifts, on us','note':'Plus a chance to win a $450 PFAS water filter. Nothing to add: it all comes with every order.'},
 'offer':{'pad':'26px 44px 6px 44px','eyebrow':'YOUR CODE','headline':'10% off your order','code':'HI10','note':'Applied automatically with the button. Or enter it at checkout.','deadline':''},
 'reviews':{'pad':'28px 44px 6px 44px'},
 'features':{'pad':'30px 44px 6px 44px','eyebrow':'WHY IT LASTS'},
 'compare':{'pad':'34px 44px 6px 44px','eyebrow':'THE DIFFERENCE','headline':'Titanium vs. coated nonstick','cap':'compare-cap-panpro.png','colA':'Siraat Titanium','colB':'Coated nonstick','note':'','ib1':'cross','ib2':'cross','ib3':'cross','ib4':'cross','ib5':'cross'},
 'closerlook':{'pad':'34px 44px 6px 44px','eyebrow':'UP CLOSE','headline':'Take a closer look.'},
 'productcard':{'pad':'0 44px 10px 44px','pill':'','note':'','was':'','link':'Shop now'},
 'cart':{'pad':'24px 44px 6px 44px','title':'STILL IN YOUR CART','line':'<b>HI10</b> takes an extra 10% off, applied with the button below.'}}
# US-voorwaarde per trigger (dezelfde als de bestaande mails): Placed Order = verzendland, Checkout = presentment currency, Added to Cart = $currency, Viewed Product = '$' in prijs
USCOND={'post-purchase':"event.extra.shipping_address.country_code == 'US'",'winback':"event.extra.shipping_address.country_code == 'US'",'vip':"event.extra.shipping_address.country_code == 'US'",'anniversary':"event.extra.shipping_address.country_code == 'US'",
 'checkout':"event.extra.presentment_currency == 'USD' or not event.extra.presentment_currency",'cart':"event|lookup:'$currency' == 'USD'",'browse':"'$' in event.Price"}
def blk(m):
    name=m.group(1); kv=dict(DEF.get(name,{})); kv.update(dict(re.findall(r'(\w+)="([^"]*)"',m.group(2))))
    fn='icons.html' if name=='icons-int' else name+'.html'
    t=open(os.path.join(B,fn)).read()
    if name=='compare':
        row=open(os.path.join(B,'compare-row.html')).read(); rows=[]
        for i in range(1,6):
            last=i==5; ib=kv.pop('ib%d'%i)
            r=row.replace('[[a]]',kv.pop('a%d'%i)).replace('[[b]]',kv.pop('b%d'%i)).replace('[[ib]]',ib).replace('[[ibalt]]','Also yes:' if ib=='same' else 'No:')
            r=r.replace('[[radA]]','border-bottom:0;border-radius:0 0 0 12px;' if last else '').replace('[[radB]]','border-bottom:0;border-radius:0 0 12px 0;' if last else '')
            rows.append(r)
        kv['rows']=''.join(rows)
    if name=='productcard':
        if '/' not in kv.get('img',''): kv['img']='{{SHARED}}/'+kv.get('img','')
        kv['pill']=('<div style="padding-bottom:8px;"><span style="display:inline-block;background:#AC3B19;color:#FFFFFF;font-size:10px;line-height:14px;letter-spacing:1.4px;font-weight:600;padding:3px 9px;border-radius:10px;">%s</span></div>'%kv['pill']) if kv['pill'] else ''
        w=kv.pop('was'); now=kv.pop('now',''); note=kv.pop('note',''); us=kv.pop('us',''); cond=kv.pop('uscond','')
        ph=('<div style="padding-top:10px;font-size:16px;line-height:22px;">%s<b style="color:#AC3B19;font-weight:600;">%s</b></div>'%(('<span style="color:#9A948B;text-decoration:line-through;">%s</span>&nbsp; '%w) if w else '',now)) if (w or now) else ''
        nh=('<div style="font-size:12px;line-height:17px;color:#727272;">%s</div>'%note) if note else ''
        if us:  # us="1": prijsregel en note alleen voor US; us="price": alleen de prijsregel, note altijd zichtbaar
            cond=cond or USCOND.get(os.path.basename(os.path.dirname(os.path.abspath(src))))
            if not cond: sys.exit('productcard us="1": geen US-voorwaarde bekend voor deze flow, geef uscond="..."')
            wrap=lambda x:('{%% if %s %%}%s{%% endif %%}'%(cond,x)) if x else ''
            if us=='price': ph=wrap(ph)
            else: ph,nh=wrap(ph+nh),''
        kv['pricehtml']=ph+nh
    if name=='offer' and kv['deadline']: kv['deadline']=open(os.path.join(B,'deadline.html')).read().replace('[[text]]',kv['deadline'])
    for k,v in kv.items(): t=t.replace('[['+k+']]',v)
    left=re.findall(r'\[\[\w+\]\]',t)
    if left: sys.exit('blok %s mist %s'%(name,left))
    return t
h=re.sub(r'\{\{BLOCK:([\w-]+)((?:\s+\w+="[^"]*")*)\s*\}\}',blk,h)
h=h.replace('</style>',open(os.path.join(B,'_style.css')).read()+'</style>',1)
su=dict(l.split() for l in open(os.path.join(SH,'klaviyo-urls.txt')) if l.strip()) if os.path.exists(os.path.join(SH,'klaviyo-urls.txt')) else {}
k=h
for a,b in sorted(u.items(),key=lambda x:-len(x[0])): k=k.replace('{{IMG}}/'+a,b)
for a,b in su.items(): k=k.replace('{{SHARED}}/'+a,b)
base=src[:-5]
# QA 2026-10-07: Outlook-fontfallback, @import apart (niet-mso), interne comments weg uit de verzendversie
MSO='<!--[if mso]><style>body,table,td,div,p,a,span{font-family:Arial,Helvetica,sans-serif!important;}</style><![endif]-->\n'
def head_fix(x):
    imp=re.search(r"\s*@import url\([^)]*\);",x)
    if imp:
        x=x.replace(imp.group(0),'',1)
        x=x.replace('<style>','<!--[if !mso]><!--><style>'+imp.group(0).strip()+'</style><!--<![endif]-->\n<style>',1)
    return x.replace('</head>',MSO+'</head>',1)
k=head_fix(k)
k=re.sub(r'<!--(?![\[<>]).*?-->\n?','',k,flags=re.S)
if '{{IMG}}' not in k and '{{SHARED}}' not in k: open(base+'.klaviyo.html','w').write(k)
p=h.replace('{{IMG}}',os.path.basename(assets.rstrip('/'))).replace('{{SHARED}}',os.path.relpath(SH,os.path.dirname(os.path.abspath(src))))
p=re.sub(r"\{% coupon_code [^%]*%\}",'SRT-K7Q2M',p)
m=re.search(r'\{% for item in event.extra.line_items %\}\{% if (?:forloop.counter <= 3|item.line_price > 0) %\}(.*?)\{% endif %\}\{% endfor %\}',p,re.S)
if m:
    r=re.sub(r"\{% if item.product.images.0.thumb_src %\}.*?\{% endif %\}|\{\{ item.product.images.0.src[^}]*\}\}",os.path.basename(assets.rstrip('/'))+'/cart-fallback.jpg',m.group(1),flags=re.S)
    r=re.sub(r"\{% if event.extra.presentment_currency[^%]*%\}(.*?)\{% endif %\}",r'\1',r).replace('{{ item.title }}','Titanium Hammered Pan Pro, 11"').replace('{{ item.quantity|floatformat:0 }}','1').replace('{{ item.line_price|floatformat:2 }}','134.00')
    p=p[:m.start()]+r+p[m.end():]
p=re.sub(r"\{\{ event.extra.(?:order_number|name)[^}]*\}\}",'#SIRAAT1042',p)
p=re.sub(r"\{% if event.ImageURL %\}.*?\{% else %\}(.*?)\{% endif %\}",r'\1',p)
p=re.sub(r"\{\{ first_name[^}]*\}\}",'Sarah',p);p=re.sub(r"\{\{ event[^}]*\}\}",'#',p)
p=p.replace("{% web_view 'View in browser' %}",'<a href="#" style="color:#BDB8B0;">View in browser</a>').replace("{% unsubscribe 'Unsubscribe' %}",'<a href="#" style="color:#BDB8B0;">Unsubscribe</a>').replace('{% manage_preferences_url %}','#').replace('{{ organization.name }}',"Siraat's Kitchen").replace('{{ organization.full_address }}','[address]')
open(base+'-preview.html','w').write(p); print('ok',base)
