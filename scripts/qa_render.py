"""QA-poort voor elke Klaviyo-export: bouwt per mail de Klaviyo-versie (zelfde route als export_klaviyo.py) en controleert
dat de mail er altijd normaal uitziet, zonder fouten en op de juiste grootte. Moet groen zijn voor elke export (PLAYBOOK 12).

Gebruik (vanuit /tmp, met -I):
  python3 -I scripts/qa_render.py                     alles: statisch + Django-render + browser (screenshots)
  python3 -I scripts/qa_render.py --only=checkout/c1  een of meer mails (komma's)
  python3 -I scripts/qa_render.py --static            zonder browser (tags, filters, Django-render, ruwe HTML-structuur)
Uitvoer: exports/qa/render-report.md, exports/qa/shots/<flow>-<id>-<desktop|mobile>-<rendered|raw>.jpg. Exitcode 1 bij FOUT.

Controles per mail:
 a. tags alleen uit de Klaviyo-allowlist (KL_TAGS + DJANGO_TAGS), filters uit DJANGO_FILTERS + KL_FILTERS (TWIJFEL = waarschuwing)
 b. Django-render op realistische events per trigger (VARIANTS); rendering mag niet falen; met en zonder <!--{% %}--> identiek
 c. na rendering geen {% %} {{ }} meer, geen lege productregels, geen $0, geen lege src/href, geen 'None'
 d. browser op 600 en 390 px (gerenderd): geen horizontale overflow, hoofdtabel 600 px, rijen en hero op volle breedte,
    alle beelden laden, hoogte op 390 px <= 3.600 px (P2 en P2-safe uitgezonderd)
 e. ruwe HTML (zoals de Klaviyo-code-editor hem toont, zonder Django): geen tekst in tabelcontext (foster-parenting),
    geen zichtbare {% buiten de hoofdtabel of vlak voor een tabel, hoofdtabel 600 px, hero op volle breedte
"""
import sys,os,re,glob,json,subprocess,tempfile,shutil,html as H
from html.parser import HTMLParser
ROOT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
V=os.path.join(ROOT,'klaviyo','templates','v3'); SH=os.path.join(ROOT,'klaviyo','templates','partials','shared')
BT=os.path.join(ROOT,'scripts','build_template.py'); TEST=os.path.join(ROOT,'research','tailoring','test')
QA=os.path.join(ROOT,'exports','qa'); SHOTS=os.path.join(QA,'shots')
OPT={a.split('=',1)[0]:(a.split('=',1)[1] if '=' in a else '1') for a in sys.argv[1:] if a.startswith('--')}
FLOWS=['anniversary','browse','cart','checkout','post-purchase','site','sunset','ugc','vip','welcome','winback']

# ---------- a. allowlists ----------
# Klaviyo-tags (Klaviyo-documentatie "template tags"). Alles daarbuiten geeft in de editor "Invalid template tag".
KL_TAGS={'coupon_code','unsubscribe','unsubscribe_link','manage_preferences','manage_preferences_link','web_view','web_view_link'}
# Ingebouwde Django-tags die Klaviyo verwerkt. Niet: load, include, extends, block, url, csrf_token, debug (bestaan niet in Klaviyo).
DJANGO_TAGS={'if','elif','else','endif','for','empty','endfor','with','endwith','firstof','cycle','resetcycle','now','comment','endcomment',
 'spaceless','endspaceless','autoescape','endautoescape','filter','endfilter','ifchanged','endifchanged','regroup','templatetag',
 'verbatim','endverbatim','widthratio','lorem'}
DJANGO_FILTERS={'add','addslashes','capfirst','center','cut','date','default','default_if_none','dictsort','dictsortreversed','divisibleby',
 'escape','escapejs','filesizeformat','first','floatformat','force_escape','get_digit','iriencode','join','json_script','last','length',
 'length_is','linebreaks','linebreaksbr','linenumbers','ljust','lower','make_list','phone2numeric','pluralize','pprint','random','rjust',
 'safe','safeseq','slice','slugify','stringformat','striptags','time','timesince','timeuntil','title','truncatechars','truncatechars_html',
 'truncatewords','truncatewords_html','unordered_list','upper','urlencode','urlize','urlizetrunc','wordcount','wordwrap','yesno'}
KL_FILTERS={'lookup','currency_format','missing_product_image','trim_slash','days_since','format_date_string','base64_encode','hash_md5',
 'hash_sha1','hash_sha256','titlecase','split','multiply','divide','round','percentage','ceil','floor','strip'}
# Django-filters die we gebruiken maar waarvan Klaviyo-ondersteuning niet in de eigen documentatie is bevestigd: waarschuwing, geen fout.
TWIJFEL={'cut':'Django-filter; in Klaviyo niet zelf bevestigd (browse: event.URL|cut). Controleer één keer met Preview in Klaviyo.',
 'slice':'Django-filter; in Klaviyo niet zelf bevestigd (browse: event.Price|slice). Controleer één keer met Preview in Klaviyo.'}

# ---------- b. contexten per trigger (research/tailoring/test/samples) ----------
PO=[('po_pan_us','kookgerei US'),('po_set6','set, niet-US'),('po_apron_us','accessoire US'),('po_deep','kookgerei internationaal')]
VARIANTS={'checkout':[('co_pan','kookgerei'),('co_set6','set'),('co_apron','accessoire'),('co_pan_eur','internationaal EUR')],
 'cart':[('atc_pan','kookgerei'),('atc_apron','accessoire'),('atc_lid_eur','internationaal EUR')],
 'browse':[('vp_pan','kookgerei'),('vp_set6','set'),('vp_apron','accessoire')],
 'post-purchase':PO,'winback':PO,'anniversary':PO,
 'vip':PO+[('po_pan_us+pool','kookgerei US, person.last_flow_code_pool=SK_REGULARS15_14D')],
 'welcome':[('none','geen event')],'site':[('none','geen event')],'sunset':[('none','geen event')],'ugc':[('none','geen event')]}
LONG_OK=re.compile(r'^(p2(-safe)?|p1-.*|w0|w2)$')   # PLAYBOOK 12: lengtegrens geldt voor verkoopmails; P2/P2-safe mogen langer, P1, W0, W2 zijn geen verkoopmail (h11)
MAXH=3600; MAXH_HARD=3780            # "ruwweg" 3.600: boven 3.600 waarschuwing, boven 3.780 fout

def mails():
    out=[]
    for f in FLOWS:
        for s in sorted(glob.glob(os.path.join(V,f,'*.html'))):
            if re.search(r'-preview|\.klaviyo\.html$',s): continue
            out.append((f,os.path.basename(s)[:-5],s))
    if OPT.get('--only'):
        want=set(OPT['--only'].split(',')); out=[m for m in out if m[0]+'/'+m[1] in want]
    return out

def build(flow,src,tmp):
    """Klaviyo-versie via build_template.py --out --no-preview; beelden als file:// zodat de browser ze laadt (CDN = zelfde bestand)."""
    ad=os.path.join(V,flow,'assets')
    tu=os.path.join(tmp,'u.txt'); ts=os.path.join(tmp,'s.txt')
    open(tu,'w').write(''.join('%s file://%s\n'%(n,os.path.join(os.path.realpath(ad),n)) for n in sorted(os.listdir(ad)) if os.path.isfile(os.path.join(ad,n))))
    open(ts,'w').write(''.join('%s file://%s\n'%(n,os.path.join(os.path.realpath(SH),n)) for n in sorted(os.listdir(SH)) if os.path.isfile(os.path.join(SH,n))))
    out=os.path.join(tmp,'%s-%s.raw.html'%(flow,os.path.basename(src)[:-5]))
    r=subprocess.run([sys.executable,'-I',BT,src,ad,tu,'--out='+out,'--shared-urls='+ts,'--no-preview'],capture_output=True,text=True)
    if r.returncode: raise RuntimeError('build: '+(r.stderr or r.stdout).strip()[-300:])
    return out,open(out).read()

def tags_filters(k):
    F=[];W=[];used=set()
    for m in re.finditer(r'\{%-?\s*(\w+)',k):
        t=m.group(1)
        if t not in KL_TAGS|DJANGO_TAGS:
            F.append('tag {%% %s %%} bestaat niet in Klaviyo (regel %d)'%(t,k.count('\n',0,m.start())+1))
    for expr in re.findall(r'\{\{.*?\}\}|\{%.*?%\}',k,re.S):
        expr=re.sub(r"'[^']*'|\"[^\"]*\"",'""',expr)
        for f in re.findall(r'\|\s*(\w+)',expr):
            used.add(f)
            if f in TWIJFEL: W.append('filter |%s: %s'%(f,TWIJFEL[f]))
            elif f not in DJANGO_FILTERS|KL_FILTERS: F.append('filter |%s onbekend in Klaviyo'%f)
    return F,W,used

class Foster(HTMLParser):
    """Volgt de open elementen; tekst direct in table/tbody/thead/tfoot/tr wordt door de browser boven de tabel gezet."""
    VOID={'img','br','meta','link','hr','input','col','source','area','wbr','base'}
    TCTX={'table','tbody','thead','tfoot','tr'}
    def __init__(s): super().__init__(convert_charrefs=True); s.st=[]; s.bad=[]
    def handle_starttag(s,tag,a):
        if tag in s.VOID: return
        if tag in ('td','th','tr') and s.st and s.st[-1] in ('td','th'): s.st.pop()
        if tag=='tr' and s.st and s.st[-1]=='tr': s.st.pop()
        s.st.append(tag)
    def handle_startendtag(s,tag,a): pass
    def handle_endtag(s,tag):
        if tag in s.st:
            while s.st and s.st.pop()!=tag: pass
    def handle_data(s,d):
        if s.st and s.st[-1] in s.TCTX and d.strip(): s.bad.append('regel %d: %s'%(s.getpos()[0],re.sub(r'\s+',' ',d.strip())[:90]))

def foster(x):
    p=Foster(); p.feed(x); p.close(); return p.bad

_ENG=None
def engine():
    global _ENG
    if _ENG: return _ENG
    sys.path.insert(0,os.path.join(TEST,'pylib')); sys.path.insert(0,TEST)
    import django
    from django.conf import settings
    settings.configure(TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','OPTIONS':{'libraries':{'kl':'kltags'},'builtins':['kltags']}}])
    django.setup()
    from django.template import engines
    _ENG=engines['django']; return _ENG

def context(var):
    name,_,extra=var.partition('+')
    ev={} if name=='none' else json.load(open(os.path.join(TEST,'samples',name+'.json')))
    person={'last_flow_code_pool':'SK_REGULARS15_14D'} if extra=='pool' else {}
    return {'event':ev,'first_name':'Sarah','person':person,'organization':{'name':"Siraat's Kitchen",'full_address':'[address]'}}

def unwrap(x): return re.sub(r'<!--(\{%.*?%\})-->',r'\1',x,flags=re.S)

def after_render(r):
    F=[]
    body=re.sub(r'<style.*?</style>','',r,flags=re.S)
    for t in ('{%','%}','{{','}}'):
        if t in body: F.append('restant %s na rendering: %s'%(t,re.sub(r'\s+',' ',body[max(0,body.find(t)-40):body.find(t)+40])))
    text=H.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<!--.*?-->','',body,flags=re.S)))
    if re.search(r'\$\s*0(?:\.0+)?(?![\d.,])',text): F.append('$0 in de tekst')
    if re.search(r'\$(?!\s*\d)',text): F.append('lege prijs ($ zonder bedrag)')
    if re.search(r'\bNone\b',text): F.append("'None' in de tekst")
    for m in re.finditer(r'<tr>\s*<td width="104".*?</tr>',body,re.S):   # cart-regels (blocks/cart.html)
        row=m.group(0); title=re.search(r'font-weight:600;color:#282828;[^"]*">(.*?)</div>',row,re.S); qty=re.search(r'Qty\s*(\S*)\s*<',row)
        if not title or not title.group(1).strip(): F.append('lege productregel (geen titel)')
        if qty and not re.match(r'\d',qty.group(1)): F.append('productregel zonder aantal')
    for a in ('src','href'):
        if re.search(r'\b%s="\s*"'%a,body): F.append('lege %s'%a)
    return F

def norm(x): return re.sub(r'\s+',' ',x.replace('<!---->','')).strip()

def main():
    ms=mails()
    if not ms: sys.exit('geen mails gevonden')
    tmp=tempfile.mkdtemp(prefix='qa-render-'); browser='--static' not in OPT
    if browser: os.makedirs(SHOTS,exist_ok=True)
    R={}; jobs=[]; used_all={}
    for flow,mid,src in ms:
        key=flow+'/'+mid; e=R[key]={'F':[],'W':[],'variants':[]}
        try: rawp,k=build(flow,src,tmp)
        except Exception as ex: e['F'].append(str(ex)); continue
        F,W,used=tags_filters(k); e['F']+=F; e['W']+=W
        for f in used: used_all.setdefault(f,set()).add(key)
        e['F']+=['ruwe HTML, tekst in tabelcontext (foster-parenting): '+b for b in foster(k)]
        if F: continue
        for i,(var,label) in enumerate(VARIANTS[flow]):
            try:
                ctx=context(var); r=engine().from_string(k).render(ctx)
                r0=engine().from_string(unwrap(k)).render(context(var))
                if norm(r)!=norm(r0): e['F'].append('%s: gerenderde uitkomst wijkt af met <!--{%% %%}--> (moet identiek zijn)'%var)
            except Exception as ex: e['F'].append('%s: rendering faalt: %s'%(var,str(ex)[:200])); continue
            e['variants'].append(var)
            e['F']+=['%s: %s'%(var,x) for x in after_render(r)]
            e['F']+=['%s: gerenderd, tekst in tabelcontext: %s'%(var,b) for b in foster(r)]
            rp=os.path.join(tmp,'%s-%s-%s.html'%(flow,mid,var)); open(rp,'w').write(r)
            for w,dev in ((600,'desktop'),(390,'mobile')):
                shot=os.path.join(SHOTS,'%s-%s-%s-rendered.jpg'%(flow,mid,dev)) if i==0 else None
                jobs.append(dict(key='%s|%s|%d|r'%(key,var,w),html=rp,width=w,shot=shot,raw=False))
        for w,dev in ((600,'desktop'),(390,'mobile')):
            jobs.append(dict(key='%s|raw|%d|x'%(key,w),html=rawp,width=w,shot=os.path.join(SHOTS,'%s-%s-%s-raw.jpg'%(flow,mid,dev)),raw=True))
        print('%-14s %-22s statisch %s'%(flow,mid,'ok' if not e['F'] else '%d FOUT'%len(e['F'])),flush=True)
    M={}
    if browser and jobs:
        jf=os.path.join(tmp,'jobs.json'); rf=os.path.join(tmp,'res.json'); json.dump(jobs,open(jf,'w'))
        r=subprocess.run(['node',os.path.join(ROOT,'scripts','qa_shots.js'),jf,rf],capture_output=True,text=True)
        if r.returncode or not os.path.exists(rf): sys.exit('browser faalt: '+(r.stderr or r.stdout)[-500:])
        M=json.load(open(rf))
    heights={}
    for jk,m in M.items():
        key,var,w,mode=jk.split('|'); w=int(w); e=R[key]; tag='%s %d px'%(var,w)
        if 'error' in m: e['F'].append('%s: browser: %s'%(tag,m['error'])); continue
        # ruwe weergave op 390 px: lange Django-expressies ({{ item.line_price|floatformat:2 }}, {% coupon_code '...' %}) zijn
        # onbreekbaar en verbreden de tabel; de echte mail (gerenderd) is maatgevend, dus daar alleen een waarschuwing
        if mode=='x' and w==390:
            if m['scrollWidth']>m['vw']: e['W'].append('ruw 390 px (code-editor mobiel): tabel %d px breed door lange Django-expressies; gerenderd in orde'%m['scrollWidth'])
            m=dict(m,scrollWidth=0,mainWidth=390,wideImgs=[],narrow=[])
        if m['scrollWidth']>m['vw']: e['F'].append('%s: horizontale overflow (%d > %d)'%(tag,m['scrollWidth'],m['vw']))
        if m['mainWidth'] is None: e['F'].append('%s: geen hoofdtabel (table.w)'%tag)
        elif w==600 and m['mainWidth']!=600: e['F'].append('%s: hoofdtabel %d px (moet 600)'%(tag,m['mainWidth']))
        elif w==390 and m['mainWidth']!=390: e['F'].append('%s: hoofdtabel %d px op mobiel (moet 390)'%(tag,m['mainWidth']))
        for x in m['narrow']: e['F'].append('%s: blok niet op volle breedte: %s'%(tag,x))
        for x in m['wideImgs']: e['F'].append('%s: breed beeld niet op volle breedte: %s'%(tag,x))
        for x in m['badImgs']: e['F'].append('%s: beeld laadt niet: %s'%(tag,x))
        if mode=='x':
            for x in m['raw']['outside']: e['F'].append('ruw %d px: Django-tekst buiten de hoofdtabel (foster-parenting): %s'%(w,x))
            for x in m['raw']['beforeTable']: e['F'].append('ruw %d px: Django-tekst vlak boven een tabel (foster-parenting): %s'%(w,x))
            e['rawvisible']=m['raw']['visible']
        elif w==390: heights.setdefault(key,{})[var]=m['height']
    for key,hs in heights.items():
        e=R[key]; mid=key.split('/')[1]; h=max(hs.values()); e['h']=h
        if h>MAXH and LONG_OK.match(mid): e['W'].append('hoogte %d px op 390 px bij %s (geen verkoopmail of P2: langer toegestaan)'%(h,max(hs,key=hs.get)))
        elif h>MAXH: (e['F'] if h>MAXH_HARD else e['W']).append('hoogte %d px op 390 px (max ~%d) bij %s'%(h,MAXH,max(hs,key=hs.get)))
    shutil.rmtree(tmp,ignore_errors=True)
    # ---------- rapport ----------
    ok=[k for k in R if not R[k]['F']]; bad=[k for k in R if R[k]['F']]
    L=['# QA-render rapport','','Gegenereerd door `scripts/qa_render.py`%s. %d mails: **%d groen**, %d met FOUT, %d met waarschuwing.'%(
        '' if browser else ' --static (zonder browser)',len(R),len(ok),len(bad),sum(1 for k in R if R[k]['W'])),'',
       'Tag-allowlist: Django `%s` plus Klaviyo `%s`.'%(', '.join(sorted(DJANGO_TAGS)),', '.join(sorted(KL_TAGS))),'',
       '## Gebruikte filters','','| filter | status | mails |','|---|---|---|']
    for f in sorted(used_all):
        st='TWIJFEL' if f in TWIJFEL else ('Klaviyo' if f in KL_FILTERS else ('Django' if f in DJANGO_FILTERS else 'ONBEKEND'))
        L.append('| `%s` | %s | %d |'%(f,st,len(used_all[f])))
    L+=['','## Per mail','','| mail | status | varianten | hoogte 390 px | zichtbare `{%`/`{{` in ruwe weergave |','|---|---|---|---|---|']
    for k in R:
        e=R[k]; L.append('| %s | %s | %s | %s | %s |'%(k,'FOUT' if e['F'] else ('let op' if e['W'] else 'groen'),', '.join(e['variants']),e.get('h','-'),e.get('rawvisible','-')))
    L+=['','## Fouten en waarschuwingen','']
    for k in R:
        for x in R[k]['F']: L.append('- FOUT %s: %s'%(k,x))
        for x in sorted(set(R[k]['W'])): L.append('- let op %s: %s'%(k,x))
    if browser: L+=['','Screenshots: `exports/qa/shots/<flow>-<id>-<desktop|mobile>-<rendered|raw>.jpg` (gerenderd = eerste variant).']
    os.makedirs(QA,exist_ok=True)
    if not OPT.get('--only') and browser: open(os.path.join(QA,'render-report.md'),'w').write('\n'.join(L)+'\n')
    for k in bad:
        for x in R[k]['F'][:6]: print('FOUT',k,x)
    print('\nQA-render: %d mails, %d groen, %d met FOUT.%s'%(len(R),len(ok),len(bad),' Rapport: exports/qa/render-report.md' if browser and not OPT.get('--only') else ''))
    sys.exit(1 if bad else 0)

if __name__=='__main__': main()
