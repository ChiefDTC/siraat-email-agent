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
P=os.path.join(d,'partials'); R='/home/user/siraat-email-agent/klaviyo/templates/partials'
h=h.replace('{{HEADER}}',open(os.path.join(P,'header.html')).read()).replace('{{FOOTER}}',open(os.path.join(P,'footer.html')).read())
# Blokken uit klaviyo/templates/partials/blocks: {{BLOCK:naam key="waarde"}} met [[key]] in het blok
B=os.path.join(R,'blocks'); SH=os.path.join(R,'shared')
DEF={'codebar':{'text':'EXTRA 10% OFF YOUR ORDER &middot; CODE','code':'HI10'},
 'cta':{'pad':'24px 44px 6px 44px','sub':''},
 'icons':{'pad':'22px 44px 6px 44px','icon4':'pfas-tested','text4':'PFAS<br>LAB TESTED'},
 'icons-int':{'pad':'22px 44px 6px 44px','icon4':'no-duties','text4':'NO IMPORT<br>DUTIES'},
 'gifts':{'pad':'30px 44px 6px 44px','eyebrow':'WITH EVERY ORDER','headline':'$70 in gifts, on us','note':'Plus a chance to win a $450 PFAS water filter. Nothing to add: it all comes with your order.'},
 'offer':{'pad':'26px 44px 6px 44px','eyebrow':'YOUR CODE','headline':'10% off your order','code':'HI10','note':'Applied automatically with the button. Or enter it at checkout.','deadline':''},
 'reviews':{'pad':'28px 44px 6px 44px'},
 'features':{'pad':'30px 44px 6px 44px','eyebrow':'WHY IT LASTS'},
 'cart':{'pad':'24px 44px 6px 44px','title':'STILL IN YOUR CART','line':'<b>HI10</b> takes an extra 10% off, applied with the button below.'}}
def blk(m):
    name=m.group(1); kv=dict(DEF.get(name,{})); kv.update(dict(re.findall(r'(\w+)="([^"]*)"',m.group(2))))
    fn='icons.html' if name=='icons-int' else name+'.html'
    t=open(os.path.join(B,fn)).read()
    if name=='offer' and kv['deadline']: kv['deadline']=open(os.path.join(B,'deadline.html')).read().replace('[[text]]',kv['deadline'])
    for k,v in kv.items(): t=t.replace('[['+k+']]',v)
    left=re.findall(r'\[\[\w+\]\]',t)
    if left: sys.exit('blok %s mist %s'%(name,left))
    return t
h=re.sub(r'\{\{BLOCK:([\w-]+)((?:\s+\w+="[^"]*")*)\s*\}\}',blk,h)
h=h.replace('</style>',open(os.path.join(B,'_style.css')).read()+'</style>',1)
open(sys.argv[4],'w').write(h)
