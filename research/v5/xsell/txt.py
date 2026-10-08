import re,sys,html
for p in sys.argv[1:]:
    s=open(p).read()
    s=re.sub(r'<style.*?</style>','',s,flags=re.S)
    s=re.sub(r'<!--(\{%.*?%\})-->',r'\1',s,flags=re.S)
    s=re.sub(r'<(br|/tr|/p|/div|/h\d)[^>]*>','\n',s)
    s=re.sub(r'<a [^>]*href="([^"]*)"[^>]*>',lambda m:' [→'+m.group(1)[:110]+'] ',s)
    s=re.sub(r'<img [^>]*src="([^"]*)"[^>]*>',lambda m:' [IMG '+m.group(1)[-50:]+'] ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    print('=====',p); print(s.strip())
