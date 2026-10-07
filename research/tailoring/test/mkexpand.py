import re
src=open('/home/user/siraat-email-agent/scripts/build_template.py').read().split('\n')
out=['# Automatisch afgeleid van scripts/build_template.py (blokexpansie). Opnieuw maken: python3 <scratch>/mkexpand.py (kopieert build_template t/m de _style.css-regel)']
for l in src:
    if l.startswith("P=os.path.join(d,'partials'); R="): l="P=os.path.join(d,'partials'); R='/home/user/siraat-email-agent/klaviyo/templates/partials'"
    out.append(l)
    if '_style.css' in l and l.startswith('h=h.replace'): break
out.append("open(sys.argv[4],'w').write(h)")
open('/home/user/siraat-email-agent/research/tailoring/test/expand.py','w').write('\n'.join(out)+'\n')
