# Cohortanalyse aanmelding/browse tot eerste order. Invoer: JSONL uit research/timing/scripts/fetch_events.py (sub.jsonl SCvkku, po.jsonl RSNxYV, vp.jsonl XNtYMB) in de werkmap. Geen ruwe data in de repo.
import json,collections,bisect,statistics as st
from datetime import datetime,timedelta
P=lambda s:datetime.fromisoformat(s.replace('Z','+00:00'))
sub={}
for l in open('sub.jsonl'):
    e=json.loads(l)
    if e['p'].get('list_id')!='Uw8eZG':continue
    t=P(e['ts']);
    if e['pid'] not in sub or t<sub[e['pid']]: sub[e['pid']]=t
po=collections.defaultdict(list)
for l in open('po.jsonl'):
    e=json.loads(l);po[e['pid']].append((P(e['ts']),float(e['p'].get('$value') or 0)))
vp=collections.defaultdict(list)
for l in open('vp.jsonl'):
    e=json.loads(l);vp[e['pid']].append(P(e['ts']))
for d in (po,vp):
    for k in d: d[k].sort()
end=P('2026-11-18T00:00:00Z')
A=P('2026-10-20T00:00:00Z');B=P('2026-11-10T00:00:00Z')
coh=[(p,t) for p,t in sub.items() if A<=t<B]
prior=sum(1 for p,t in coh if any(o[0]<t-timedelta(minutes=1) for o in po.get(p,[])))
pros=[(p,t) for p,t in coh if not any(o[0]<t-timedelta(minutes=1) for o in po.get(p,[]))]
print('cohort',len(coh),'prior buyers',prior,'prospects',len(pros))
W=[('2min',timedelta(minutes=2)),('10min',timedelta(minutes=10)),('1h',timedelta(hours=1)),('24h',timedelta(days=1)),('2d',timedelta(days=2)),('3d',timedelta(days=3)),('5d',timedelta(days=5)),('7d',timedelta(days=7))]
def first_order(p,t):
    for o in po.get(p,[]):
        if o[0]>=t-timedelta(minutes=1): return o
    return None
fo={p:first_order(p,t) for p,t in pros}
for n,w in W:
    c=sum(1 for p,t in pros if fo[p] and fo[p][0]-t<=w)
    print(n,c,'%.1f%%'%(100*c/len(pros)))
# non buyers after 1h
nb=[(p,t) for p,t in pros if not(fo[p] and fo[p][0]-t<=timedelta(hours=1))]
print('nonbuyer 1h',len(nb))
buy7=[ (p,t) for p,t in nb if fo[p] and fo[p][0]-t<=timedelta(days=7)]
print('buy 1h-7d',len(buy7),'%.2f%%'%(100*len(buy7)/len(nb)))
# hazard per day among nonbuyers
for d0,d1 in [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7)]:
    lo=timedelta(hours=1) if d0==0 else timedelta(days=d0)
    c=sum(1 for p,t in nb if fo[p] and lo<fo[p][0]-t<=timedelta(days=d1))
    print('day',d0,'-',d1,c,'%.2f%%'%(100*c/len(nb)))
# return visit: product view > 1h after signup within 7 days (before order)
def ret(p,t):
    for v in vp.get(p,[]):
        if timedelta(hours=1)<v-t<=timedelta(days=7):
            o=fo[p]
            if o and o[0]<v: return None
            return v
    return None
R=[(p,t,ret(p,t)) for p,t in nb]
rr=[x for x in R if x[2]]
print('returned to view product 1h-7d',len(rr),'%.1f%%'%(100*len(rr)/len(nb)))
cb_r=sum(1 for p,t,v in rr if fo[p] and fo[p][0]-t<=timedelta(days=7))
cb_n=sum(1 for p,t,v in R if not v and fo[p] and fo[p][0]-t<=timedelta(days=7))
print('conv7d returners %.2f%% (%d) vs non-returners %.2f%% (%d)'%(100*cb_r/len(rr),cb_r,100*cb_n/(len(nb)-len(rr)),cb_n))
# share of 1h-7d buyers that returned first
print('of buyers 1h-7d, viewed product again before buying', sum(1 for p,t,v in rr if fo[p] and fo[p][0]-t<=timedelta(days=7)),'/',len(buy7))
gaps=sorted((v-t).total_seconds()/3600 for p,t,v in rr)
q=lambda a,x:a[int(len(a)*x)]
print('first return visit hours after signup p25/p50/p75',q(gaps,.25),q(gaps,.5),q(gaps,.75))
# multi-day viewers
md=[]
for p,t in nb:
    days={(v-t).days for v in vp.get(p,[]) if timedelta(0)<=v-t<=timedelta(days=7) and not(fo[p] and fo[p][0]<v)}
    md.append((p,len(days)))
for k in (1,2,3):
    g=[p for p,n in md if (n>=k if k==3 else n==k)]
    c=sum(1 for p in g if fo[p] and fo[p][0]-sub[p]<=timedelta(days=7))
    print('distinct view days',k if k<3 else '3+',len(g),'conv7d %.2f%%'%(100*c/max(1,len(g))))
# time-to-order distribution among buyers within 7d (all prospects)
bt=sorted((fo[p][0]-t).total_seconds()/3600 for p,t in pros if fo[p] and fo[p][0]-t<=timedelta(days=7))
print('buyers 7d',len(bt),'share in 1h %.1f%%'%(100*sum(1 for x in bt if x<=1)/len(bt)),'1-24h %.1f%%'%(100*sum(1 for x in bt if 1<x<=24)/len(bt)),'1-3d %.1f%%'%(100*sum(1 for x in bt if 24<x<=72)/len(bt)),'3-7d %.1f%%'%(100*sum(1 for x in bt if x>72)/len(bt)))
late=[x for x in bt if x>1]; print('late buyers median hours',st.median(late))
