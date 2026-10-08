# Rendert alle v5-mails (US-context, testcontext per flowtype) naar previews/<flow>-<id>.png, 600 px breed. Gebruik: cd /tmp && python3 -I <repo>/klaviyo/figma/v5/render.py
import sys,os,json,re,tempfile,subprocess
sys.argv=['x']; sys.path.insert(0,'/home/user/siraat-email-agent/scripts')
import qa_render as Q
ROOT=Q.ROOT; OUT=os.path.join(ROOT,'klaviyo','figma','v5','previews'); os.makedirs(OUT,exist_ok=True)
SPECIAL={'checkout/c3-s':'co_set6','checkout/c2-acc':'co_apron','checkout/c3-acc':'co_apron','cart/k1-acc':'atc_apron','browse/b1-acc':'vp_apron',
 'post-purchase/p3-set':'po_set6','post-purchase/p3-set-nocode':'po_set6','post-purchase/p3-apron':'po_apron_us','post-purchase/p3-apron-nocode':'po_apron_us',
 'post-purchase/p3-accessory':'po_board_us','post-purchase/p3-accessory-nocode':'po_board_us','winback/r1-set':'po_set6','winback/r1-acc':'po_apron_us'}
tmp=tempfile.mkdtemp(prefix='v5fig-'); jobs=[]; meta={}
for flow,mid,src in Q.mails():
    key=flow+'/'+mid
    rawp,k=Q.build(flow,src,tmp)
    var=SPECIAL.get(key,Q.VARIANTS[flow][0][0]).partition('+')[0]
    bev={} if var=='none' else json.load(open(os.path.join(Q.TEST,'samples',var+'.json')))
    ev,person=Q.V5C.market_ctx(Q.v5lib.sig_of(flow),'US',bev)
    r=Q.engine().from_string(k).render({'event':ev,'first_name':'Sarah','person':person,'organization':{'name':"Siraat's Kitchen",'full_address':'[address]'}})
    p=os.path.join(tmp,'%s-%s.html'%(flow,mid)); open(p,'w').write(r)
    jobs.append({'html':p,'png':os.path.join(OUT,'%s-%s.png'%(flow,mid))})
    m=re.match(r'\s*<!--(.*?)-->',open(src).read(),re.S)
    d={a.strip():b.strip() for a,b in (x.split(':',1) for x in (m.group(1).split(' | ') if m else []) if ':' in x)}
    meta[key]={'a':d.get('SUBJECT_A',''),'b':d.get('SUBJECT_B',''),'p':d.get('PREVIEW',''),'var':var}
    print(key,var,flush=True)
json.dump(jobs,open(os.path.join(tmp,'jobs.json'),'w'))
json.dump(meta,open(os.path.join(ROOT,'klaviyo','figma','v5','meta.json'),'w'),indent=1)
r=subprocess.run(['node',os.path.join(ROOT,'klaviyo','figma','v5','shot.js'),os.path.join(tmp,'jobs.json')],capture_output=True,text=True)
print(r.stdout[-2000:],r.stderr[-2000:])
