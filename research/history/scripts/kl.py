import json, subprocess, time, sys
H = ["-H","revision: 2025-10-15","-H","accept: application/vnd.api+json","-H","content-type: application/vnd.api+json"]
def req(url, body=None, tries=12):
    for i in range(tries):
        cmd = ["curl","-s","-g","-w","\n%{http_code}",url]+H
        if body is not None:
            cmd += ["-X","POST","-d",json.dumps(body)]
        out = subprocess.run(cmd,capture_output=True,text=True).stdout
        txt, code = out.rsplit("\n",1)
        if code == "429" or "throttled" in txt[:300]:
            wait = 5
            try:
                d=json.loads(txt); det=d["errors"][0]["detail"]
                import re; m=re.search(r"(\d+) second",det); wait=int(m.group(1))+1 if m else 5
            except Exception: pass
            print("429, wait",wait,file=sys.stderr); time.sleep(min(wait,90)); continue
        if code.startswith("5"):
            time.sleep(5); continue
        try: return json.loads(txt)
        except Exception: return {"raw":txt,"code":code}
    raise RuntimeError("too many retries "+url)
def pages(url):
    out=[]; inc=[]
    while url:
        d=req(url); out+=d.get("data",[]); inc+=d.get("included",[]) or []
        url=(d.get("links") or {}).get("next")
    return out, inc
