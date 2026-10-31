import json,subprocess,time
def api(m,p,b=None,rev='2025-10-15'):
    c=['curl','-sS','-g','-X',m,'https://a.klaviyo.com'+p,'-H','revision: '+rev,'-H','accept: application/vnd.api+json','-H','content-type: application/vnd.api+json']
    inp=None
    if b: c+=['--data-binary','@-']; inp=json.dumps(b)
    for k in range(5):
        out=subprocess.run(c,capture_output=True,text=True,input=inp).stdout
        try:
            r=json.loads(out)
            if any(e.get('status')==429 for e in r.get('errors',[])): time.sleep(2); continue
            return r
        except Exception: time.sleep(2)
    return {'errors':[{'detail':'geen antwoord'}]}
def status(fid): 
    r=api('GET',f'/api/flows/{fid}?fields[flow]=name,status'); return r['data']['attributes']['status'],r['data']['attributes']['name']
def setstatus(fid,s):
    r=api('PATCH',f'/api/flows/{fid}',{'data':{'type':'flow','id':fid,'attributes':{'status':s}}})
    return 'FOUT '+json.dumps(r['errors'])[:200] if 'errors' in r else r['data']['attributes']['status']
