"""Vernieuwt content/catalog/products.json uit siraatskitchen.com (alleen lezen).
Gebruik (vanuit /tmp):  python3 -I <repo>/scripts/refresh_catalog.py <repo>/content/catalog/products.json [rawdir] [--no-fetch]
- Haalt per handle en per land /products/<handle>.js op met de cookie localization=<LAND> (zo toont Shopify de marktprijs),
  plus de US-PDP-HTML voor secties en FAQ. Ruwe pagina's gaan naar rawdir (standaard /tmp/siraat-catalog-raw), nooit in git.
- HANDLES en US_ONLY komen uit Shopify Admin (products status:active, publishedInContext per land, 8 okt 2026).
  Nieuw product of nieuwe markt: eerst die twee lijsten bijwerken (zie content/catalog/README.md).
"""
import json,os,re,sys,html,time,subprocess
ARGS=[a for a in sys.argv[1:] if not a.startswith('--')]
OUT=ARGS[0]; RAW=ARGS[1] if len(ARGS)>1 else '/tmp/siraat-catalog-raw'
os.makedirs(RAW+'/js',exist_ok=True); os.makedirs(RAW+'/html',exist_ok=True)
HANDLES=["original-siraat-100-pure-titanium-pan", "original-siraat-100-pure-titanium-pan-with-hammered-pattern", "siraat-titanium-ice-cubes", "siraat-pure-titanium-utensils-bundle", "siraat-non-slip-mat-for-board-premium-silicone", "siraat-pure-titanium-utensils", "titanium-pro-duo", "titanium-hammered-wok-pan-pro", "titanium-hammered-deep-pan-pro", "titanium-hammered-cookware-set-pro", "titanium-straws", "titanium-hammered-pan-pro-kit", "titanium-cutting-board-v2", "diatomite-mat-anthracite-ultra-hygienic-fast-drying-mold-resistant", "titanium-hammered-crepe-pan-pro", "titanium-hammered-pro-prep-cook-set", "titanium-hammered-pan-pro-mini", "rolling-knife-sharpener-diamond-ceramic", "titanium-cutting-board-v2-bundle", "the-hammered-collection", "titanium-water-bottle", "titanium-hammered-pan-pro-incl-lid", "stainless-steel-lid", "titanium-chopsticks", "cherrywood-mini-trivet", "e-gift-card", "titanium-hammered-pan-pro-utensil-set", "e", "full-hammered-pro-edition", "titanium-hammered-pan-pro-duo", "titanium-hammered-pan-pro-large", "titanium-hammered-pan-pro-small", "e-sca_clone_freegift", "titanium-hammered-pizza-steel", "titanium-cutting-board-v2-gold-edition", "siraat-signature-apron-azure", "siraat-signature-apron-moss", "siraat-signature-apron-ember", "siraat-signature-apron-oak", "the-green-e-guide-free", "pizza-wheel", "magnetic-cherry-wood-trivet", "siraat-non-slip-mat-for-board-premium-silicone-sca_clone_freegift", "salt-mill", "pepper-mill", "salt-pepper-mill-set", "grill-press", "tote-bag", "2-litre-titanium-hammered-pot-with-lid", "3-litre-titanium-hammered-pot-with-lid", "7-5-litre-titanium-hammered-pot-with-lid", "titanium-hammered-pan-set-with-lids-6-pcs", "dishwashing-detergent-sheets-fresh-lemon", "titanium-hammered-cookware-set", "titanium-hammered-pan-pro-standard-copy", "stainless-steel-lid-copy", "titanium-hammered-pan-pro-large-copy", "titanium-hammered-pan-pro-mini-copy", "titanium-hammered-roasting-pan", "titanium-hammered-pan-pro-standard-copy-1", "free-shipping-sca_clone_freegift", "entry-to-win-your-order-sca_clone_freegift", "the-green-clean-e-guide-sca_clone_freegift", "dishwashing-detergent-sheets-fresh-lemon-sca_clone_freegift", "2-pans-and-2-lids", "the-just-everything-bundle-34-pcs"]
C=['US','CA','GB','DE','NL','FR','AU','NZ','SG','HK','AE','CH','NO','SE','JP']
def get(url,c,o):
    r=subprocess.run(['curl','-sS','-b','localization='+c,'-o',o,'-w','%{http_code}',url],capture_output=True,text=True)
    return r.stdout
if '--no-fetch' not in sys.argv:
    for h in HANDLES:
        for c in C:
            get(f'https://siraatskitchen.com/products/{h}.js',c,f'{RAW}/js/{h}__{c}.json'); time.sleep(0.15)
        get(f'https://siraatskitchen.com/products/{h}','US',f'{RAW}/html/{h}.html'); print('ok',h,flush=True)
raw=RAW
C=['US','CA','GB','DE','NL','FR','AU','NZ','SG','HK','AE','CH','NO','SE','JP']
CUR={'US':'USD','CA':'CAD','GB':'GBP','DE':'EUR','NL':'EUR','FR':'EUR','AU':'AUD','NZ':'NZD','SG':'SGD','HK':'HKD','AE':'AED','CH':'CHF','NO':'USD','SE':'SEK','JP':'JPY'}
MARKET={'US':'USA','CA':'Canada','GB':'United Kingdom','DE':'Germany (EUR)','NL':'Netherlands (EUR)','FR':'EURO','AU':'Australia','NZ':'New Zealand','SG':'Singapore','HK':'RoW (local currency)','AE':'MIDDLE EAST / RoW','CH':'RoW (local currency)','NO':'Norway (USD)','SE':'RoW (local currency)','JP':'RoW (local currency)'}
# Admin publishedInContext (8 okt 2026): alleen US gepubliceerd
US_ONLY={'2-litre-titanium-hammered-pot-with-lid','3-litre-titanium-hammered-pot-with-lid','7-5-litre-titanium-hammered-pot-with-lid','titanium-hammered-cookware-set','titanium-hammered-pan-pro-standard-copy','stainless-steel-lid-copy','titanium-hammered-pan-pro-large-copy','titanium-hammered-pan-pro-mini-copy','titanium-hammered-roasting-pan','2-pans-and-2-lids','the-just-everything-bundle-34-pcs'}
GIFT_HANDLES={'free-shipping-sca_clone_freegift','entry-to-win-your-order-sca_clone_freegift','the-green-clean-e-guide-sca_clone_freegift','dishwashing-detergent-sheets-fresh-lemon-sca_clone_freegift','e-sca_clone_freegift','siraat-non-slip-mat-for-board-premium-silicone-sca_clone_freegift','the-green-e-guide-free'}
DUP_HANDLES={'titanium-hammered-pan-pro-standard-copy':'original-siraat-100-pure-titanium-pan-with-hammered-pattern','titanium-hammered-pan-pro-standard-copy-1':'original-siraat-100-pure-titanium-pan-with-hammered-pattern','titanium-hammered-pan-pro-large-copy':'titanium-hammered-pan-pro-large','titanium-hammered-pan-pro-mini-copy':'titanium-hammered-pan-pro-mini','stainless-steel-lid-copy':'stainless-steel-lid'}
NOMINAL_IN={20:'8',24:'9.5',26:'10',28:'11',30:'12'}
def strip(t):
    t=re.sub(r'(?is)<(script|style|svg|noscript)[^>]*>.*?</\1>',' ',t)
    t=re.sub(r'(?i)<br\s*/?>|</(p|div|li|h\d|tr|summary|details)>','\n',t)
    t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t)
    out=[];prev=None
    for l in t.split('\n'):
        l=re.sub(r'\s+',' ',l).strip()
        if l and l!=prev: out.append(l)
        prev=l
    return out
HDR=["OVERVIEW","NON TOXIC MATERIALS","DETAILS","CONSTRUCTION","WHAT'S INCLUDED","CARE & USE","SPECIFICATIONS","DIMENSIONS","FEATURES","HOW TO USE","MATERIALS"]
def sections(lines,title):
    out={};cur=None
    # start bij eerste OVERVIEW
    idx=[i for i,l in enumerate(lines) if l in HDR and i>400]
    if not idx: return out
    start=idx[0]
    for l in lines[start:start+120]:
        if l in HDR: cur=l; out[cur]=[]; continue
        if l==title or l.startswith('Sale price') or l=='ADD TO CART' or l.startswith('🍁'): break
        if cur and l not in ('Tested PFAS-Free','·','See Lab Results'): out[cur].append(l)
    return {k:v for k,v in out.items() if v}
def faq(lines):
    qs=[]
    for i,l in enumerate(lines):
        if l.endswith('?') and i+2<len(lines) and lines[i+1]=='›' and not lines[i+2].endswith('?'):
            q=(l,lines[i+2])
            if q not in qs: qs.append(q)
    for k,l in enumerate(lines):
        if l in ('FAQS','FAQs') and k>400:
            j=k+1
            while j+1<len(lines) and lines[j].endswith('?') and not lines[j+1].endswith('?'):
                q=(lines[j],lines[j+1]); 
                if q not in qs: qs.append(q)
                j+=2
    return [{'q':a,'a':b} for a,b in qs]
def misc(lines,title):
    d={}
    for i,l in enumerate(lines):
        if l==title and i>0 and re.match(r'^[\d.]+ · [\d,]+ reviews$',lines[i-1]) and i+1<len(lines) and 'tagline' not in d and not lines[i+1].startswith(('Sale price','$','Regular')):
            d['tagline']=lines[i+1]
        if l=='Important notice!' and i+1<len(lines): d['important_notice']=lines[i+1]
        m=re.match(r'^([\d.]+) · ([\d,]+) reviews$',l)
        if m and 'rating' not in d: d['rating']=float(m.group(1)); d['reviews']=int(m.group(2).replace(',',''))
        if l.startswith('Free Express Shipping') or l=='from the US': d['site_shipping_line']='Free Express Shipping from the US (staat op elke PDP, ook voor niet-US bezoekers)'
    # badge boven galerij
    for i,l in enumerate(lines):
        if ('FALL SALE' in l or 'OFF' in l or 'NON-TOXIC' in l) and i+1<len(lines) and lines[i+1]=='Zoom':
            d['badge']=l; break
    return d
def cm_in(s):
    r=[]
    for m in re.finditer(r'(\d+(?:[.,]\d+)?)\s?cm\s?/\s?([\d.]+)\s?(?:″|"|”|in)',s,re.I): r.append({'cm':float(m.group(1).replace(',','.')),'in':float(m.group(2))})
    return r
products=[]
for h in HANDLES:
    js={}
    for c in C:
        f=f'{raw}/js/{h}__{c}.json'
        try: js[c]=json.load(open(f))
        except Exception: js[c]=None
    us=js['US']
    if not us: print('geen US-data',h); continue
    lines=strip(open(f'{raw}/html/{h}.html',encoding='utf-8',errors='replace').read()) if os.path.exists(f'{raw}/html/{h}.html') else []
    title=us['title']
    sec=sections(lines,title)
    variants=[]
    for v in us['variants']:
        opts=[o for o in (v.get('options') or []) if o]
        txt=' '.join(opts+[v.get('title') or ''])
        m=re.search(r'(\d+(?:\.\d+)?)\s?CM',txt,re.I)
        cm=float(m.group(1)) if m else None
        OV={'titanium-hammered-wok-pan-pro':{'Mini':24.0,'Small':26.0,'Standard':28.0,'Large':30.0},'titanium-hammered-deep-pan-pro':{'Mini':20.0,'Standard':24.0,'Large':26.0}}
        if cm is None and h in OV: cm=OV[h].get(txt.split()[0])
        mi=re.search(r'\((\d+)(?:"|″|”)\)',txt)
        if cm is None and mi: cm={'8':20.0,'10':26.0,'11':28.0,'12':30.0}.get(mi.group(1))
        if cm is None and len(us['variants'])==1 and not re.search(r'Set|Edition|Bundle|Duo|Kit|Pans|Collection',title):
            md=re.search(r'Diameter:\s*(\d+(?:\.\d+)?)\s?cm',' '.join(sec.get('DETAILS',[])),re.I)
            if md: cm=float(md.group(1))
        prices={}; avail={}
        for c in C:
            j=js[c]
            if not j: prices[c]=None; avail[c]=False; continue
            vv=next((x for x in j['variants'] if x['id']==v['id']),None)
            if not vv: prices[c]=None; avail[c]=False; continue
            prices[c]={'price':vv['price']/100,'compare_at':(vv['compare_at_price']/100 if vv.get('compare_at_price') else None),'currency':CUR[c]}
            avail[c]=bool(vv.get('available'))
        variants.append({'id':v['id'],'title':v['title'],'options':opts,'sku':v.get('sku'),'weight_g':v.get('weight'),
            'size_cm':cm,'size_in_exact':round(cm/2.54,1) if cm else None,'size_in_nominal':NOMINAL_IN.get(int(cm)) if cm else None,
            'available':avail,'prices':prices})
    published={c:bool(js[c]) for c in C}
    imgs=['https:'+i if i.startswith('//') else i for i in us.get('images',[])]
    inc=sec.get("WHAT'S INCLUDED",[])
    fq=faq(lines)
    box=[x['a'] for x in fq if any(k in x['q'].lower() for k in ('included','in the box','come with','what do i get',"what's in",'what is in'))]
    dims=cm_in(' '.join(sec.get('DETAILS',[])+inc))
    p={'handle':h,'title':title,'url':f'https://siraatskitchen.com/products/{h}','tags':us.get('tags',[]),
       'role':'gift (gratis, auto-add)' if h in GIFT_HANDLES else ('duplicaat-listing van '+DUP_HANDLES[h] if h in DUP_HANDLES else 'verkoop'),
       'us_only': h in US_ONLY,'published_storefront':published,
       'variants':variants,'images':imgs[:10],'images_total':len(imgs),
       'pdp':{**misc(lines,title),'sections':sec,'whats_in_the_box':inc or box,'whats_in_the_box_faq':box,'dimensions':dims,'faq':fq},
       'description_html_len':len(us.get('description') or '')}
    if us.get('description'): p['pdp']['description_text']=' '.join(strip(us['description']))[:2000]
    products.append(p)
json.dump({'generated':'2026-10-08','source':'siraatskitchen.com /products/<handle>.js per land (cookie localization=<CC>) + PDP-HTML (US) + Shopify Admin publishedInContext','countries':C,'currency_by_country':CUR,'market_by_country':MARKET,'products':products},open(OUT,'w'),indent=1,ensure_ascii=False)
print(len(products),'producten')
