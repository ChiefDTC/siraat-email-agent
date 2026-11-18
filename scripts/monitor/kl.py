import subprocess,json,time
def api(m,p,b=None,rev='2025-10-15'):
    c=['curl','-sS','-g','-X',m,'https://a.klaviyo.com'+p,'-H','revision: '+rev,'-H','accept: application/vnd.api+json','-H','content-type: application/vnd.api+json']
    if b is not None: c+=['--data-binary',json.dumps(b)]
    for i in range(6):
        r=subprocess.run(c,capture_output=True,text=True)
        o=r.stdout.strip()
        if not o: return {}
        try: d=json.loads(o)
        except Exception: d={'raw':o[:300]}
        if isinstance(d,dict) and any(str(e.get('status'))=='429' for e in d.get('errors',[]) if isinstance(e,dict)):
            time.sleep(2*(i+1)); continue
        return d
    return d
