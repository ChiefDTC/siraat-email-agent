import csv,re,sys
rev={r['id']:r for r in csv.DictReader(open('content/reviews/reviews.csv'))}
txt=open('research/copy/04-rewrites.md').read()
errs=0; pairs={}
cur=None
for i,line in enumerate(txt.split('\n')):
    if line.startswith('## '): cur=line
    m=re.match(r'- (q[12]) \((R\d+)[^)]*\): "(.*)"\s*(\(.*\))?$',line.strip())
    if not m: continue
    q,rid,ex=m.group(1),m.group(2),m.group(3)
    orig=rev[rid]['quote']; stars=rev[rid]['stars']
    parts=[p.strip() for p in ex.split('...') if p.strip()]
    pos=0; ok=True
    for p in parts:
        j=orig.find(p,pos)
        if j<0: ok=False; break
        pos=j+len(p)
    L=len(ex)
    pairs.setdefault(cur,{})[q]=L
    flag=[]
    if not ok: flag.append('NOT VERBATIM')
    if L>120: flag.append('TOO LONG %d'%L)
    if stars!='5': flag.append('STARS '+stars)
    if flag: errs+=1; print(cur,q,rid,flag,ex)
for k,v in pairs.items():
    if 'q1' in v and 'q2' in v and abs(v['q1']-v['q2'])>30: print('DIFF',k,v); errs+=1
print('errors',errs, 'checked', sum(len(v) for v in pairs.values()))
