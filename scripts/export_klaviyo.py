"""Export van de v4-flowmails naar Klaviyo: eerst een dry-run, pas na akkoord live.

Gebruik:
  python3 -I scripts/export_klaviyo.py                      dry-run (standaard), alle mails
  python3 -I scripts/export_klaviyo.py --only=checkout/c1   dry-run voor een of meer mails (komma's)
  (--update: bestaande templates krijgen de nieuwe HTML via PATCH)
  python3 -I scripts/export_klaviyo.py --live --i-am-sure   live: beelden uploaden, klaviyo-urls.txt aanvullen,
                                                            .klaviyo.html bouwen, templates aanmaken (POST /api/templates)

Dry-run (schrijft niets in Klaviyo):
  - per mail uit klaviyo/templates/v3/<flow>/<id>.html (de v4-inventaris, v4-flow-system.md sectie 5):
    welke lokale beelden nog geen CDN-URL hebben (dat zou --live uploaden),
  - bouwt de Klaviyo-HTML met tijdelijke placeholder-URL's in exports/dry-run/<flow>/<id>.html,
  - valideert (zie check()) en schrijft exports/manifest.csv.
Live (alleen met --i-am-sure, na akkoord Floris; API-key met scopes images:write en templates:write):
  1. uploadt alleen de beelden die een mail echt gebruikt en die nog geen URL hebben (zelfde call als upload_images.py),
     en vult <assets>/klaviyo-urls.txt of partials/shared/klaviyo-urls.txt aan,
  2. bouwt <id>.klaviyo.html naast de bron (build_template.py) en valideert opnieuw,
  3. maakt per mail een template "v4 · <flow> · <id>" aan (editor_type CODE), slaat namen over die al bestaan,
     en logt naam en template-ID in exports/live/templates.csv.
Mails met een blokkade worden in live overgeslagen.
QA-poort: --live draait eerst scripts/qa_render.py en weigert alles bij een FOUT (exitcode != 0).
"""
import sys,os,re,csv,json,glob,hashlib,subprocess,tempfile,time,html as H
ROOT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
V=os.path.join(ROOT,'klaviyo','templates','v3'); PA=os.path.join(ROOT,'klaviyo','templates','partials')
SH=os.path.join(PA,'shared'); PASSETS=os.path.join(PA,'assets')
EXP=os.path.join(ROOT,'exports'); DRY=os.path.join(EXP,'dry-run')
BT=os.path.join(ROOT,'scripts','build_template.py')
PLAN=os.path.join(ROOT,'klaviyo','flows','v4-flow-system.md')
OPT={a.split('=',1)[0]:(a.split('=',1)[1] if '=' in a else '1') for a in sys.argv[1:] if a.startswith('--')}
LIVE='--live' in OPT
if LIVE and '--i-am-sure' not in OPT: sys.exit('--live vraagt ook --i-am-sure (eerst akkoord Floris, zie exports/README.md).')

# map -> (flownaam in Klaviyo, utm_campaign) volgens v4-flow-system.md 1.1
FLOWS={'checkout':('Checkout abandonment','v4-checkout'),'cart':('Cart abandonment','v4-cart'),'browse':('Browse abandonment','v4-browse'),
 'welcome':('Welcome','v4-welcome'),'post-purchase':('Post-purchase','v4-postpurchase'),'winback':('Winback','v4-winback'),
 'site':('Site abandonment','v4-site'),'sunset':('Sunset','v4-sunset'),'vip':('VIP','v4-vip'),'anniversary':('Anniversary','v4-anniversary'),'ugc':('UGC first egg','v4-ugc')}
FLOWNAME_OVERRIDE={('post-purchase','p2'):'Post-purchase · levering'}
POOLS={'C4_10_48H','K3_10_48H','B2_10_48H','P3_THANKYOU_10_14D','R2_10_72H','R2_VIP_15_72H','SK_REGULARS15_14D','SK_ANNIV10_7D'}  # v4 4.4
PLACEHOLDER='https://cdn.klaviyomail.com/company/TdtTzz/images/DRYRUN-%s-%s'
MAXKB=100

def urlfile(p): return dict(l.split() for l in open(p) if l.strip()) if os.path.exists(p) else {}
def md5(p): return hashlib.md5(open(p,'rb').read()).hexdigest()

def inventory():
    """Mail-ID's uit de tabel in sectie 5 van het v4-plan (ook de varianten die toen nog 'te bouwen' waren)."""
    t=open(PLAN).read(); t=t[t.index('## 5. Mail-inventaris'):]
    ids=[]
    for line in t.split('\n'):
        if not line.startswith('| '): continue
        c=line.split('|')[1].strip()
        if c in ('Mail','---'): continue
        if c.startswith('p3-*-nocode'): ids+=['p3-%s-nocode'%x for x in ('set','pan','next','apron','accessory')]; continue
        ids+=[x.strip() for x in c.split(',')]
    return ids

def mails():
    out=[]
    for f in sorted(FLOWS):
        for s in sorted(glob.glob(os.path.join(V,f,'*.html'))):
            if re.search(r'-preview|\.klaviyo\.html$',s): continue
            out.append((f,os.path.basename(s)[:-5],s))
    if OPT.get('--only'):
        want=set(OPT['--only'].split(',')); out=[m for m in out if m[0]+'/'+m[1] in want]
    return out

def meta(src):
    top=open(src).read().split('\n',1)[0]
    def g(k):
        m=re.search(r'(?:<!--|\|)\s*'+k+r':\s*(.*?)\s*(?:\||-->)',top)
        # werknotities achter een onderwerp, bijv. '(reserve; ...)', horen niet bij de onderwerpregel
        return re.sub(r'\s*\((?:reserve|niet gebruiken|phase|fase)[^)]*\)\s*$','',H.unescape(m.group(1)).strip()) if m else ''
    return g('SUBJECT_A'),g('SUBJECT_B'),g('PREVIEW')

def expanded(src):
    """Bron na blokexpansie (zelfde code als build_template.py, via research/tailoring/test/expand.py)."""
    tmp=tempfile.mktemp(suffix='.html')
    r=subprocess.run([sys.executable,'-I',os.path.join(ROOT,'research','tailoring','test','expand.py'),src,os.path.join(os.path.dirname(src),'assets'),'/dev/null',tmp],capture_output=True,text=True)
    if r.returncode: raise RuntimeError('expand: '+(r.stderr or r.stdout).strip()[-300:])
    h=open(tmp).read(); os.remove(tmp); return h

PURL=urlfile(os.path.join(PASSETS,'klaviyo-urls.txt'))
PMD5={md5(os.path.join(PASSETS,f)):u for f,u in PURL.items() if os.path.exists(os.path.join(PASSETS,f))}

def images(flow,src,h):
    """Alle lokale beelden van een mail: (soort, bestand, pad, url of None, bron van de url)."""
    ad=os.path.join(V,flow,'assets'); fu=urlfile(os.path.join(ad,'klaviyo-urls.txt')); su=urlfile(os.path.join(SH,'klaviyo-urls.txt'))
    res=[]
    for kind,name in sorted(set(re.findall(r'\{\{(IMG|SHARED)\}\}/([\w.@-]+\.(?:png|jpe?g|gif))',h))):
        if kind=='IMG':
            p=os.path.join(ad,name); u=fu.get(name); how='flow'
            if not u and os.path.exists(p) and md5(p) in PMD5: u=PMD5[md5(p)]; how='partials/assets'
        else: p=os.path.join(SH,name); u=su.get(name); how='shared'
        res.append((kind,name,p,u,how if u else None))
    return res

def build(src,flow,imgs,out,placeholder):
    """Bouwt de Klaviyo-HTML via build_template.py --out (geen preview) met echte of placeholder-URL's."""
    ad=os.path.join(V,flow,'assets')
    fu=urlfile(os.path.join(ad,'klaviyo-urls.txt')); su={}
    for kind,name,p,u,how in imgs:
        url=u or (PLACEHOLDER%(flow,name) if placeholder else None)
        if not url: continue
        (fu if kind=='IMG' else su)[name]=url
    tu=tempfile.mktemp(suffix='.txt'); ts=tempfile.mktemp(suffix='.txt')
    open(tu,'w').write(''.join('%s %s\n'%kv for kv in fu.items())); open(ts,'w').write(''.join('%s %s\n'%kv for kv in su.items()))
    os.makedirs(os.path.dirname(out),exist_ok=True)
    r=subprocess.run([sys.executable,'-I',BT,src,ad,tu,'--out='+out,'--shared-urls='+ts,'--no-preview'],capture_output=True,text=True)
    os.remove(tu); os.remove(ts)
    if r.returncode: raise RuntimeError('build: '+(r.stderr or r.stdout).strip()[-300:])
    return open(out).read()

def check(k,subj_a,subj_b,prev):
    """Validatie van de Klaviyo-HTML. Geeft (blokkades, waarschuwingen)."""
    B=[];W=[]
    for t in ('{{IMG}}','{{SHARED}}','[[','{{BLOCK','{{HEADER}}','{{FOOTER}}'):
        if t in k: B.append('restant %s'%t)
    for s in re.findall(r'\bsrc="([^"]*)"',k):
        for part in re.split(r'\{%[^%]*%\}',s):
            part=part.strip()
            if part and not re.match(r'(https://|\{\{)',part): B.append('lokaal pad in src: %s'%part[:60])
    for a in re.findall(r'\bhref="([^"]*)"',k):
        if re.match(r'(assets/|\.\./|/|file:)',a) or re.search(r'\.(jpe?g|png|gif)$',a) and not a.startswith('http'): B.append('lokaal pad in href: %s'%a[:60])
    stack=[]
    for m in re.finditer(r'\{%\s*(\w+)',k):
        tag=m.group(1)
        if tag in ('if','for'): stack.append(tag)
        elif tag in ('endif','endfor'):
            want=tag[3:]
            if not stack or stack[-1]!=want: B.append('Klaviyo-tags niet in balans bij {%% %s %%}'%tag); break
            stack.pop()
    if stack: B.append('Klaviyo-tags niet gesloten: %s'%','.join(stack))
    if k.count('{{')!=k.count('}}'): B.append('{{ }} niet in balans')
    for p in re.findall(r"\{%\s*coupon_code\s+'([^']+)'",k):
        if p not in POOLS: B.append('onbekende coupon-pool %s'%p)
    kb=len(k.encode())/1024
    if kb>=MAXKB: B.append('HTML %.1f KB (Gmail knipt rond 102 KB)'%kb)
    com=[c for c in re.findall(r'<!--.*?-->',k,re.S) if not re.match(r'<!--\[if|<!--<!\[endif\]|<!\[endif\]',c) and not c.startswith('<!--[if')]
    com=[c for c in com if c not in ('<!--<![endif]-->',) and not c.startswith('<!--[if !mso]><!-->')]
    com=[c for c in com if not re.match(r'<!--\{%.*%\}-->$',c,re.S)]  # Django-logica in commentaar (build_template wrap_ctrl, qa_render.py)
    if com: B.append('interne HTML-comments: %d'%len(com))
    if not subj_a: B.append('geen SUBJECT_A in topcomment')
    elif len(subj_a)>50: B.append('onderwerp A %d tekens (max 50)'%len(subj_a))
    if subj_b and len(subj_b)>50: B.append('onderwerp B %d tekens (max 50)'%len(subj_b))
    if not prev: B.append('geen PREVIEW in topcomment')
    elif not 40<=len(prev)<=90: B.append('preview %d tekens (40 tot 90)'%len(prev))
    ph=re.search(r'<div style="display:none;[^"]*">(.*?)(?:&nbsp;|&zwnj;|</div>)',k,re.S)
    norm=lambda x:re.sub(r'\s+',' ',x.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).strip()
    if prev and ph and norm(H.unescape(ph.group(1)))!=norm(prev): W.append('preheader in de HTML wijkt af van PREVIEW')
    for tag in re.findall(r'<img\b[^>]*>',k,re.S):
        if not re.search(r'\balt="',tag): B.append('beeld zonder alt: %s'%re.search(r'src="([^"]{0,60})',tag).group(1)); continue
        w=re.search(r'\bwidth="(\d+)"',tag)
        if re.search(r'\balt=""',tag) and w and int(w.group(1))>40: W.append('lege alt op beeld van %s px'%w.group(1))
    for a in re.findall(r'\bhref="([^"]*)"',k):
        if re.search(r'siraatskitchen\.com',a) and 'utm_source' not in a and not a.startswith('mailto'):
            B.append('link zonder UTM: %s'%a[:80])
    if '\u2014' in k or '&mdash;' in k: B.append('gedachtestreepje (em dash)')
    return sorted(set(B)),sorted(set(W))

# ---------- live (alleen met --live --i-am-sure) ----------
def api(method,path,body=None,form=None):
    h=['-H','revision: 2025-10-15','-H','accept: application/vnd.api+json']
    if os.environ.get('KLAVIYO_API_KEY'): h+=['-H','Authorization: Klaviyo-API-Key '+os.environ['KLAVIYO_API_KEY']]
    cmd=['curl','-sS','-w','\n%{http_code}','-X',method,'https://a.klaviyo.com'+path]+h
    if body is not None: cmd+=['-H','content-type: application/vnd.api+json','--data-binary','@-']
    for k_,v in (form or []): cmd+=['-F','%s=%s'%(k_,v)]
    for attempt in range(5):
        r=subprocess.run(cmd,input=json.dumps(body) if body is not None else None,capture_output=True,text=True)
        out,_,code=r.stdout.rpartition('\n')
        if code=='429': time.sleep(2+attempt*2); continue
        time.sleep(1.2)  # PLAYBOOK 4: rate limit
        return int(code or 0),(json.loads(out) if out.strip().startswith('{') else out)
    return 429,'rate limit'

def upload(kind,flow,name,path):
    """Zelfde call als scripts/upload_images.py; naam in Klaviyo siraat-<map>-<bestand>."""
    pre='shared' if kind=='SHARED' else flow
    code,res=api('POST','/api/image-upload',form=[('file','@'+path),('name','siraat-%s-%s'%(pre,name))])
    try: url=res['data']['attributes']['image_url']
    except Exception: raise RuntimeError('upload %s: %s %s'%(name,code,str(res)[:200]))
    uf=os.path.join(SH if kind=='SHARED' else os.path.join(V,flow,'assets'),'klaviyo-urls.txt')
    open(uf,'a').write('%s %s\n'%(name,url)); return url

def remember(flow,name,url):
    """URL die al bestaat (logo's uit partials/assets) in de klaviyo-urls.txt van de flow zetten."""
    uf=os.path.join(V,flow,'assets','klaviyo-urls.txt')
    if name not in urlfile(uf): open(uf,'a').write('%s %s\n'%(name,url))

def template_exists(name):
    code,res=api('GET','/api/templates?filter='+__import__('urllib.parse').parse.quote('equals(name,"%s")'%name))
    if code!=200: raise RuntimeError('templates lezen: %s %s'%(code,str(res)[:200]))
    d=res.get('data') or []; return d[0]['id'] if d else None

def create_template(name,k,subj,prev):
    body={'data':{'type':'template','attributes':{'name':name,'editor_type':'CODE','html':k}}}
    code,res=api('POST','/api/templates',body=body)
    if code not in (200,201): raise RuntimeError('template %s: %s %s'%(name,code,str(res)[:300]))
    return res['data']['id']

# ---------- hoofdlus ----------
def qa_gate():
    """QA-poort (PLAYBOOK 12): scripts/qa_render.py moet groen zijn, anders weigert --live."""
    cmd=[sys.executable,'-I',os.path.join(ROOT,'scripts','qa_render.py')]+(['--only='+OPT['--only']] if OPT.get('--only') else [])
    r=subprocess.run(cmd,cwd=tempfile.gettempdir())
    if r.returncode: sys.exit('QA-poort rood (scripts/qa_render.py, zie exports/qa/render-report.md): --live geweigerd, niets naar Klaviyo gestuurd.')

def main():
    if LIVE: qa_gate()
    inv=inventory(); ms=mails(); have={m[1] for m in ms}
    rows=[]; up_total=set()
    if LIVE: os.makedirs(os.path.join(EXP,'live'),exist_ok=True); tlog=open(os.path.join(EXP,'live','templates.csv'),'a')
    for flow,mid,src in ms:
        fname=FLOWNAME_OVERRIDE.get((flow,mid),FLOWS[flow][0]); tname='v4 · %s · %s'%(fname,mid)
        a,b,p=meta(src); B=[];W=[]; imgs=[]; kb=0
        if mid not in inv: W.append('niet in de v4-inventaris (sectie 5)')
        try:
            h=expanded(src); imgs=images(flow,src,h)
            missing=[i for i in imgs if not os.path.exists(i[2])]
            if missing: B.append('beeld ontbreekt lokaal: %s'%', '.join(i[1] for i in missing))
            if LIVE and not B:
                for kind,name,path,u,how in imgs:
                    if not u: upload(kind,flow,name,path)
                    elif how=='partials/assets': remember(flow,name,u)
                imgs=images(flow,src,h)
                out=src[:-5]+'.klaviyo.html'; k=build(src,flow,imgs,out,False)
            else:
                out=os.path.join(DRY,flow,mid+'.html'); k=build(src,flow,imgs,out,True)
            kb=len(k.encode())/1024
            b2,w2=check(k,a,b,p); B+=b2; W+=w2
        except Exception as e: B.append(str(e))
        todo=[('shared/' if i[0]=='SHARED' else flow+'/assets/')+i[1] for i in imgs if not i[3]]
        up_total.update(todo)
        status='klaar' if not B else 'blokkade: '+'; '.join(B)
        if LIVE and not B:
            try:
                tid=template_exists(tname)
                if tid and '--update' in OPT:
                    code,res=api('PATCH','/api/templates/'+tid,body={'data':{'type':'template','id':tid,'attributes':{'html':k}}})
                    if code!=200: raise RuntimeError('update %s: %s %s'%(tid,code,str(res)[:200]))
                tid=tid or create_template(tname,k,a,p)
                tlog.write('%s,%s,%s\n'%(time.strftime('%Y-%m-%d %H:%M'),tname,tid)); tlog.flush(); status='klaar · template %s'%tid
            except Exception as e: status='blokkade: '+str(e)
        rows.append(dict(flow=flow,id=mid,templatenaam=tname,onderwerp_a=a,onderwerp_b=b,preview=p,aantal_beelden=len(imgs),
            te_uploaden=len(todo),te_uploaden_bestanden=' '.join(todo),html_kb='%.1f'%kb,status=status,waarschuwingen='; '.join(W)))
        print('%-14s %-22s %5.1f KB  beelden %2d  upload %2d  %s'%(flow,mid,kb,len(imgs),len(todo),status[:110]))
    missing_inv=[i for i in inv if i not in have and not re.search(r'nohi10',i)]
    for i in missing_inv:
        rows.append(dict(flow='',id=i,templatenaam='',onderwerp_a='',onderwerp_b='',preview='',aantal_beelden=0,te_uploaden=0,te_uploaden_bestanden='',html_kb='',status='blokkade: staat in de v4-inventaris maar er is geen bronbestand',waarschuwingen=''))
    if not OPT.get('--only'):
        os.makedirs(EXP,exist_ok=True)
        with open(os.path.join(EXP,'manifest.csv'),'w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    ok=sum(1 for r in rows if r['status'].startswith('klaar'))
    print('\n%s: %d mails, %d klaar, %d met blokkade. Unieke beelden te uploaden: %d.%s'%('LIVE' if LIVE else 'DRY-RUN',len(rows),ok,len(rows)-ok,len(up_total),
          '' if LIVE else ' Niets naar Klaviyo gestuurd. Uitvoer: exports/dry-run/, exports/manifest.csv'))

if __name__=='__main__': main()
