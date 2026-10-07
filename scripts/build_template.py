"""Bouwt Klaviyo-HTML en een lokale preview uit een bron-template met {{IMG}}.
Gebruik: python3 -I scripts/build_template.py <bron.html> <assets-map> <urls.txt>
Schrijft <bron>.klaviyo.html (CDN-links) en <bron-zonder-.html>-preview.html (lokale beelden, voorbeelddata).
Opties (voor scripts/export_klaviyo.py): --out=<pad> (Klaviyo-versie elders), --shared-urls=<bestand> (extra 'bestand url' voor {{SHARED}}), --no-preview.
De Klaviyo-versie krijgt UTM's op elke siraatskitchen.com-link zonder UTM (header, footer): utm_content=<mail>-logo|nav-*|ft-*, campaign uit de mail zelf (04-utm.md 5.2)."""
import sys,re,os
OPT={a.split('=',1)[0]:(a.split('=',1)[1] if '=' in a else '1') for a in sys.argv[1:] if a.startswith('--')}
src,assets,urls=[a for a in sys.argv[1:] if not a.startswith('--')][:3]
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
if OPT.get('--shared-urls'): su.update(dict(l.split() for l in open(OPT['--shared-urls']) if l.strip()))
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
# UTM op siraatskitchen.com-links zonder UTM (header/footer-partials); prefix en campaign uit de eigen links van de mail
def add_utm(x):
    camp=re.findall(r'utm_campaign(?:=|%3D)([\w-]+)',x); cont=re.findall(r'utm_content(?:=|%3D)([a-z0-9]+)-',x)
    if not camp or not cont: return x
    camp=max(set(camp),key=camp.count); mid=max(set(cont),key=cont.count)
    ft=re.sub(r'<!--(?![\[<>]).*?-->\n?','',open(os.path.join(P,'footer.html')).read(),flags=re.S).strip()[:80]
    fpos=x.find(ft) if ft else -1
    def fix(m):
        url=m.group(2)
        if 'utm_' in url or not re.match(r'https://(www\.)?siraatskitchen\.com',url): return m.group(0)
        path=re.sub(r'https://(www\.)?siraatskitchen\.com','',url).strip('/')
        blk='logo' if not path else re.sub(r'[^a-z0-9]+','-',path.split('/')[-1].lower())
        blk=('ft-' if 0<=fpos<=m.start() else ('' if blk=='logo' else 'nav-'))+blk
        u=url if path else url.rstrip('/')+'/'
        return '%s%s%sutm_source=klaviyo&utm_medium=email&utm_campaign=%s&utm_content=%s-%s"'%(m.group(1),u,'&' if '?' in u else '?',camp,mid,blk)
    return re.sub(r'(href=")([^"{}]+)"',fix,x)
k=add_utm(k)
# QA-poort 2026-10-07 (qa_render.py): Django-logica in HTML-tekst (tussen <table>/<tr>/<td>) in een HTML-commentaar,
# <!--{% if ... %}-->. Django/Klaviyo verwerkt tags ook binnen commentaar (gerenderd blijft alleen <!----> over),
# de browser en de Klaviyo-code-editor tonen ze niet en "foster-parenten" ze dus niet boven de tabel.
# Alleen besturingstags; uitvoertags (coupon_code, unsubscribe, web_view ...) en tags in attributen, <title>, <style> en bestaande commentaren blijven staan.
CTRL=('if','elif','else','endif','for','empty','endfor','with','endwith','comment','endcomment','ifchanged','endifchanged','spaceless','endspaceless','autoescape','endautoescape','filter','endfilter')
def wrap_ctrl(x):
    toks=[]
    x=re.sub(r'\{%.*?%\}|\{\{.*?\}\}',lambda m:(toks.append(m.group(0)),'\x00%d\x00'%(len(toks)-1))[1],x,flags=re.S)
    out=[]; raw=None; pos=0
    for m in re.finditer(r'<!--.*?-->|<(/?)([a-zA-Z][\w:-]*)[^>]*>|<![^>]*>',x,re.S):
        text=x[pos:m.start()]; pos=m.end()
        if raw is None: text=re.sub(r'\x00(\d+)\x00',lambda t:'<!--%s-->'%toks[int(t.group(1))] if re.match(r'\{%-?\s*('+'|'.join(CTRL)+r')\b',toks[int(t.group(1))]) and '--' not in toks[int(t.group(1))] else t.group(0),text)
        out.append(text); out.append(m.group(0))
        tag=(m.group(2) or '').lower()
        if tag in ('style','title','script','textarea'): raw=None if m.group(1) else tag
    out.append(x[pos:])
    return re.sub(r'\x00(\d+)\x00',lambda t:toks[int(t.group(1))],''.join(out))
k=wrap_ctrl(k)
if '{{IMG}}' not in k and '{{SHARED}}' not in k: open(OPT.get('--out',base+'.klaviyo.html'),'w').write(k)
elif OPT.get('--out'): sys.exit('nog {{IMG}}/{{SHARED}} zonder URL: '+', '.join(sorted(set(re.findall(r'\{\{(?:IMG|SHARED)\}\}/([\w.-]+)',k)))))
if OPT.get('--no-preview'): sys.exit(0)
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
p=p.replace("{% web_view 'View in browser' %}",'<a href="#" style="color:#BDB8B0;">View in browser</a>').replace("{% unsubscribe 'Unsubscribe' %}",'<a href="#" style="color:#BDB8B0;">Unsubscribe</a>').replace('{% manage_preferences_link %}','#').replace('{{ organization.name }}',"Siraat's Kitchen").replace('{{ organization.full_address }}','[address]')
open(base+'-preview.html','w').write(p); print('ok',base)
