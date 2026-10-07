"""Bouwt Klaviyo-HTML en een lokale preview uit een bron-template met {{IMG}}.
Gebruik: python3 -I scripts/build_template.py <bron.html> <assets-map> <urls.txt>
Schrijft <bron>.klaviyo.html (CDN-links) en <bron-zonder-.html>-preview.html (lokale beelden, voorbeelddata)."""
import sys,re,os
src,assets,urls=sys.argv[1:4]
u=dict(l.split() for l in open(urls) if l.strip()) if os.path.exists(urls) else {}
h=open(src).read()
P=os.path.join(os.path.dirname(os.path.abspath(src)),'partials')
h=h.replace('{{HEADER}}',open(os.path.join(P,'header.html')).read()).replace('{{FOOTER}}',open(os.path.join(P,'footer.html')).read())
k=h
for a,b in sorted(u.items(),key=lambda x:-len(x[0])): k=k.replace('{{IMG}}/'+a,b)
base=src[:-5]
if '{{IMG}}' not in k: open(base+'.klaviyo.html','w').write(k)
p=h.replace('{{IMG}}',os.path.basename(assets.rstrip('/')))
m=re.search(r'\{% for item in event.extra.line_items %\}\{% if forloop.counter <= 3 %\}(.*?)\{% endif %\}\{% endfor %\}',p,re.S)
if m:
    r=re.sub(r"\{\{ item.product.images.0.src[^}]*\}\}",os.path.basename(assets.rstrip('/'))+'/cart-fallback.jpg',m.group(1)).replace('{{ item.title }}','Titanium Hammered Pan Pro, 11"').replace('{{ item.quantity|floatformat:0 }}','1').replace('{{ item.line_price|floatformat:2 }}','134.00')
    p=p[:m.start()]+r+p[m.end():]
p=re.sub(r"\{\{ first_name[^}]*\}\}",'Sarah',p);p=re.sub(r"\{\{ event[^}]*\}\}",'#',p)
p=p.replace("{% web_view 'View in browser' %}",'<a href="#" style="color:#BDB8B0;">View in browser</a>').replace("{% unsubscribe 'Unsubscribe' %}",'<a href="#" style="color:#BDB8B0;">Unsubscribe</a>').replace('{% manage_preferences_url %}','#').replace('{{ organization.name }}',"Siraat's Kitchen").replace('{{ organization.full_address }}','[address]')
open(base+'-preview.html','w').write(p); print('ok',base)
