"""QA van de .klaviyo.html (urgentie-sprint 8 nov): voorbeeldwaarden invullen, Django-render zoals Klaviyo (qa_render.engine), dan de checks.
Gebruik: python3 -I render_urg.py <uitmap>. Schrijft <uitmap>/<id>.html (gerenderd). Meldt per mail: renderfouten, open tokens (BLOKKEREND voor live),
hero nog niet geupload, links zonder eigen utm_content, platte tekst zonder deadline/link, streepjes, verboden woorden, KB."""
import sys, os, re, html, collections
sys.path.insert(0, '/home/user/siraat-email-agent/scripts'); import qa_render as Q
T = os.path.dirname(os.path.abspath(__file__)); N = os.path.dirname(T); OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
G = {'__file__': os.path.join(T, 'make_urg.py'), '__name__': 'x'}; exec(open(os.path.join(T, 'make_urg.py')).read(), G)
for f in sorted(x for x in os.listdir(N) if x.endswith('.klaviyo.html')):
    mid = f[:-13]; k = open(os.path.join(N, f)).read()
    open_tokens = sorted(set(re.findall(r'\[\[(\w+)\]\]', k)))
    pending = sorted(set(re.findall(r'UPLOAD-PENDING:([\w.-]+)', k)))
    c = Q.context('none'); c['person']['Country'] = 'United States' if mid.endswith('-us') else 'Germany'
    h = Q.engine().from_string(G['fill'](k, G['caps'](G['SAMPLE']))).render(c)
    probs = Q.after_render(h) + Q.foster(h)
    open(os.path.join(OUT, mid + '.html'), 'w').write(h)
    body = h.split('<body', 1)[1]
    links = re.findall(r'href="([^"]+)"', body)
    own = [l for l in links if 'utm_campaign=urgency-1108' in l or 'utm_campaign%3Durgency-1108' in l]
    ct = collections.Counter(re.search(r'utm_content(?:=|%3D)([\w-]+)', l).group(1) for l in own)
    dests = set(re.sub(r'[?%].*', '', l) for l in own)
    nolink = [l[:60] for l in links if 'siraatskitchen.com' in l and 'utm_' not in l]
    text = html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<style.*?</style>|<!--.*?-->', '', body, flags=re.S)))
    main = text.split('NON-TOXIC COOKWARE')[0]   # vaste footer ('BUILT FOR LIFE') niet meetellen
    bad = [b for b in G['BAD'] if re.search(r'\b%s\b' % re.escape(b), main.lower())]
    dl = text.lower().count('11:59 pm')
    print(mid, '| render:', probs[:3] or 'ok', '| KB %.0f' % (len(k.encode()) / 1024), '| deadline x%d' % dl, '| utm_content:', dict(ct),
          '| bestemmingen:', len(dests), '| zonder utm:', nolink or 0, '| streepje:', bool(re.search('[–—]', h)), '| verboden:', bad or 0,
          '| hero niet geupload:', pending or 0, '| BLOKKEREND tokens:', open_tokens or 0)
