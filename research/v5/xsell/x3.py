import runpy,io,contextlib,collections
buf=io.StringIO()
with contextlib.redirect_stdout(buf): g=runpy.run_path('/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/xs/xsell.py')
orders=g['orders']; c=collections.Counter(); multi=0; rep=0
for p,os_ in orders.items():
    own=set().union(*[cs for _,cs,_ in os_]); c.update(own)
    if len(os_)>1: rep+=1
print('profielen',len(orders),'met 2+ orders',rep); print(c.most_common(25))
