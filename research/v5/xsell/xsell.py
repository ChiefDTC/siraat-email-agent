import json, collections, statistics, datetime as dt
P='/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/data/orders.jsonl'
GIFT=('🎁','Gift','100% off','100% OFF','FREE','E-Guide','E-Book','Giveaway','Draw','Shipping Protection','Free Shipping','Win Your Order')
def cat(t):
    if any(g in t for g in GIFT): return None
    if '12PC' in t or '(Copy)' in t: return None  # componentregels van bundels
    m=[('12-Pcs','set12'),('34-Pcs','setall'),('Pot Set','potset'),('6-Pcs','set6'),('Litre','pot'),('Cookware Set Pro','setpro'),('Complete Edition','setpro'),('Full Hammered','setpro'),
       ('Pan Pro Duo','duo'),('2 Pans','duo'),('& Utensil Set','std+ut'),('With Lid','std+lid'),
       ('Pan Pro Standard','standard'),('Pan Pro-Standard','standard'),('Frying Pan, 11','standard'),('Pan Pro Large','large'),('Pan Pro-Large','large'),('Pan Pro Small','small'),('Pan Pro-Small','small'),('Pan Pro Mini','mini'),
       ('Titanium Pan Pro','standard'),('Hammered Pan Pro','standard'),
       ('Deep Pan','deep'),('Wok','wok'),('pe Pan','crepe'),('Pizza Steel','pizza'),('Roasting','roast'),
       ('Lid','lid'),('Utensil Set Bundle','utset'),('Titanium Utensil','utensil'),('Chopsticks','utensil'),
       ('Cutting Board','board'),('Prep Board','board'),('Non Slip Mat','mat'),('Salt Mill','mill'),('Pepper Mill','mill'),('Mill Set','mill'),('Apron','apron'),
       ('Dishwasher Sheets','sheets'),('Detergent','sheets'),('Pizza Wheel','pizzawheel'),('Knife Sharpener','sharpener'),('Trivet','trivet'),('Water Bottle','bottle'),('Gift Card','giftcard'),('Grill Press','grillpress')]
    for k,v in m:
        if k in t: return v
    return 'other'
orders=collections.defaultdict(list)
with open(P) as f:
    for l in f:
        d=json.loads(l)
        cs={cat(t) for t in (d['p'].get('Items') or [])}; cs.discard(None)
        if not cs: continue
        ts=dt.datetime.fromisoformat(d['ts'])
        orders[d['pid']].append((ts,cs,(d.get('loc') or {}).get('c')))
for p in orders: orders[p].sort(key=lambda x:x[0])
import sys
END=dt.datetime(2026,10,7,16,tzinfo=dt.timezone.utc); FU=int(sys.argv[1]) if len(sys.argv)>1 else 180
CUT=END-dt.timedelta(days=FU)
base=collections.Counter(); rep=collections.Counter(); nxt=collections.defaultdict(collections.Counter); nxtnew=collections.defaultdict(collections.Counter); days=collections.defaultdict(list); daysy=collections.defaultdict(lambda: collections.defaultdict(list))
same=collections.defaultdict(collections.Counter); nall=collections.Counter()
for p,os_ in orders.items():
    owned=set()
    for i,(ts,cs,c) in enumerate(os_):
        for x in cs:
            nall[x]+=1
            for y in cs:
                if y!=x: same[x][y]+=1
        if ts<=CUT:
            # volgende order > 1 uur later
            j=next((j for j in range(i+1,len(os_)) if (os_[j][0]-ts).total_seconds()>3600),None)
            for x in cs:
                base[x]+=1
                if j is not None and (os_[j][0]-ts).days<=FU:
                    rep[x]+=1; dd=(os_[j][0]-ts).days; days[x].append(dd)
                    allown=owned|cs
                    for y in os_[j][1]:
                        nxt[x][y]+=1; daysy[x][y].append(dd)
                        if y not in allown: nxtnew[x][y]+=1
        owned|=cs
print('profielen',len(orders),'orders',sum(len(v) for v in orders.values()))
for x,n in nall.most_common():
    if n<40: continue
    b=base[x]; r=rep[x]
    top=nxt[x].most_common(5); topn=nxtnew[x].most_common(4)
    md=statistics.median(days[x]) if days[x] else None
    s=' · '.join(f'{y} {100*k/b:.1f}% ({100*k/max(r,1):.0f}% v. herh., med {statistics.median(daysy[x][y]):.0f}d)' for y,k in top)
    sn=' · '.join(f'{y} {100*k/b:.1f}%' for y,k in topn)
    sm=' · '.join(f'{y} {100*k/nall[x]:.1f}%' for y,k in same[x].most_common(6))
    print(f'\n## {x}: orders {n}, cohort {b}, herhaal 180d {100*r/max(b,1):.1f}% (med {md}d)\n  next: {s}\n  next NIEUW: {sn}\n  zelfde order: {sm}')
