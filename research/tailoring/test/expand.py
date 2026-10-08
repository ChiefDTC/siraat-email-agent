# Automatisch afgeleid van scripts/build_template.py (blokexpansie). Opnieuw maken: python3 <scratch>/mkexpand.py (kopieert build_template t/m de _style.css-regel)
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
P=os.path.join(d,'partials'); R='/home/user/siraat-email-agent/klaviyo/templates/partials'
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
 'cart':{'pad':'24px 44px 6px 44px','title':'STILL IN YOUR CART','line':'<b>HI10</b> takes an extra 10% off, and your <b>$70 in gifts</b> are still attached to this cart.'},
 'deadline':{'pad':'18px 44px 6px 44px','label':'YOUR OWN CODE RUNS OUT','amount':'48','unit':'HOURS','note':''},
 'ugc':{'pad':'28px 44px 6px 44px','eyebrow':'IN THEIR WORDS','headline':'From their kitchens','foot':'Verified reviews. Join 100,000+ happy customers.'}}
DEF['offer'].update({'days':'','amount':'','unit':'HOURS'})
# Persoonlijke deadline (urgency-upgrade 7 okt 2026): {{DATE:<dagen>:<Django-datumformaat>[:upper]}} wordt de Klaviyo-tag
# {% today '%Y-%m-%d' as today %}{{ today|days_later:N|format_date_string|date:'FMT' }} (help.klaviyo.com, date variables reference).
# Alleen gebruiken bij een unieke code die echt vervalt (C4/K3/B2 48 uur, R2 72 uur, P3 en V1 14 dagen, N2 7 dagen).
def date_macro(x):
    def rep(m):
        n,fmt,up=m.group(1),m.group(2),m.group(3)
        return "{%% today '%%Y-%%m-%%d' as today %%}{{ today|days_later:%s|format_date_string|date:'%s'%s }}"%(n,fmt,'|upper' if up else '')
    return re.sub(r"\{\{DATE:(\d+):([^:}']+)(:upper)?\}\}",rep,x)
# v5-bouwstenen (8 okt 2026): markt-helper, macro's en generator-blokken staan in scripts/v5lib.py (PLAYBOOK h12 "v5-bouwstenen").
# De flow volgt uit de map van de bron; een bron buiten v3/<flow>/ kan <!-- MARKET-SIGNAL: order|cart|checkout|browse|profile --> zetten.
sys.path.insert(0,os.path.abspath(os.path.join(R,'..','..','..','scripts'))); import v5lib
FLOW=os.path.basename(os.path.dirname(os.path.abspath(src)))
_ms=re.search(r'<!-- MARKET-SIGNAL: (\w+) -->',h)
if _ms: FLOW=_ms.group(1)
# US-voorwaarde voor productcard us="1": dezelfde centrale markt-helper (checkout: presentment currency + profielland, cart: _ip_country_code,
# browse: profielland met prijsnotatie als terugval, order: verzendland; de oude regel '$' in event.Price was ook waar voor AUD/CAD/SGD).
def blk(m):
    name=m.group(1); kv=dict(DEF.get(name,{})); kv.update(dict(re.findall(r'(\w+)="([^"]*)"',m.group(2))))
    if name=='vs': name='compare'; kv=dict(DEF['compare'],**v5lib.vs(kv))
    elif name in v5lib.BLOCKS:
        try: return v5lib.block(name,kv,FLOW)
        except ValueError as e: sys.exit('blok %s: %s'%(name,e))
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
            if cond: wrap=lambda x:('{%% if %s %%}%s{%% endif %%}'%(cond,x)) if x else ''
            else:
                if FLOW not in v5lib.FLOWSIG or v5lib.FLOWSIG[FLOW]=='profile': sys.exit('productcard us="1": geen event-signaal in deze flow, geef uscond="..."')
                wo,c,wc=v5lib.us_cond(FLOW); wrap=lambda x:('%s{%% if %s %%}%s{%% endif %%}%s'%(wo,c,x,wc)) if x else ''
            if us=='price': ph=wrap(ph)
            else: ph,nh=wrap(ph+nh),''
        kv['pricehtml']=ph+nh
    if name in ('deadline','offer') and kv.get('days'):
        d=kv['days']; kv['dday']='{{DATE:%s:D:upper}}'%d; kv['ddate']='{{DATE:%s:M j:upper}}'%d
    if name=='offer':
        if kv['deadline'] and kv['days']: kv['deadline']=open(os.path.join(B,'deadline-offer.html')).read().replace('[[text]]',kv['deadline'])
        elif kv['deadline']: kv['deadline']=open(os.path.join(B,'deadline-line.html')).read().replace('[[text]]',kv['deadline'])
        for x in ('days','amount','unit','dday','ddate'): kv.setdefault(x,'')
    for k,v in kv.items(): t=t.replace('[['+k+']]',v)
    left=re.findall(r'\[\[\w+\]\]',t)
    if left: sys.exit('blok %s mist %s'%(name,left))
    return t
h=re.sub(r'\{\{BLOCK:([\w-]+)((?:\s+\w+="[^"]*")*)\s*\}\}',blk,h)
try: h=v5lib.expand(h,FLOW)
except ValueError as e: sys.exit('v5-macro: %s'%e)
h=date_macro(h)
h=h.replace('</style>',open(os.path.join(B,'_style.css')).read()+'</style>',1)
open(sys.argv[4],'w').write(h)
