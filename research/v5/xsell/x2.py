import runpy,sys,collections,statistics
sys.argv=['x','180']
import io,contextlib
buf=io.StringIO()
with contextlib.redirect_stdout(buf): g=runpy.run_path(sys.argv[0] if False else '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/xs/xsell.py')
orders=g['orders']
nrep=0; nown=0; nonly=0; c3=collections.Counter(); c3new=collections.Counter(); n3=0; d23=[]
for p,os_ in orders.items():
    owned=set()
    prev=None
    for i,(ts,cs,c) in enumerate(os_):
        if i>0 and (ts-os_[i-1][0]).total_seconds()>3600:
            nrep+=1
            if cs&owned: nown+=1
            if cs<=owned: nonly+=1
        if i==2:
            n3+=1; d23.append((ts-os_[1][0]).days)
            for y in cs: c3[y]+=1
            for y in cs-owned: c3new[y]+=1
        owned|=cs
print('herhaalorders',nrep,'met al-bezeten categorie %.0f%%'%(100*nown/nrep),'alleen al-bezeten %.0f%%'%(100*nonly/nrep))
print('3e orders',n3,'mediaan dagen 2->3',statistics.median(d23))
print('3e order top',[(k,round(100*v/n3)) for k,v in c3.most_common(8)])
print('3e order nieuw',[(k,round(100*v/n3)) for k,v in c3new.most_common(8)])
# US-only: aandeel niet-US bij set12, pot, potset, roast
cc=collections.defaultdict(collections.Counter)
for p,os_ in orders.items():
    for ts,cs,c in os_:
        for x in cs: cc[x]['US' if c=='United States' else 'INT' if c else 'onbekend']+=1
for x in ['set12','potset','pot','roast','set6','standard']: print(x,dict(cc[x]))
