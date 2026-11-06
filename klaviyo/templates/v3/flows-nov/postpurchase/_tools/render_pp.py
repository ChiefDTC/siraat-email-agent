"""Post-purchase nov 2026: build (build_template) + Django-render op echte Placed Order-voorbeelden + checks.
Gebruik (vanuit /tmp): python3 -I render_pp.py <uitmap> [id,id]. Schrijft <uitmap>/<id>-<variant>.html; screenshots daarna met shot_pp.js.
Varianten: us = Pan Pro Standard-koper US, us-set = 6-delige set, int = Deep Pan-koper Duitsland, int-set = 6-delige set Duitsland."""
import sys, os, subprocess, re
sys.path.insert(0, '/home/user/siraat-email-agent/scripts'); import qa_render as Q
N = '/home/user/siraat-email-agent/klaviyo/templates/v3/flows-nov/postpurchase'
AD = '/home/user/siraat-email-agent/klaviyo/templates/v3/bfcm/november-v2/assets'
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
tu = os.path.join(OUT, 'u.txt'); ts = os.path.join(OUT, 's.txt')
open(tu, 'w').write(''.join('%s file://%s\n' % (n, os.path.join(AD, n)) for n in sorted(os.listdir(AD)) if os.path.isfile(os.path.join(AD, n))))
open(ts, 'w').write(''.join('%s file://%s\n' % (n, os.path.join(Q.SH, n)) for n in sorted(os.listdir(Q.SH)) if os.path.isfile(os.path.join(Q.SH, n))))
VAR = {'us': [('us', 'po_pan_us', 'United States'), ('us-set', 'po_set6', 'United States')],
       'int': [('int', 'po_deep', 'Germany'), ('int-set', 'po_x_set6', 'Germany')]}
ids = sys.argv[2].split(',') if len(sys.argv) > 2 else sorted(f[:-5] for f in os.listdir(N) if f.startswith('pp-') and f.endswith('.html') and not f.endswith(('-preview.html', '.klaviyo.html')))
for mid in ids:
    src = os.path.join(N, mid + '.html')
    r = subprocess.run([sys.executable, '-I', Q.BT, src, AD, os.path.join(AD, 'klaviyo-urls.txt')], capture_output=True, text=True, cwd='/tmp')
    if r.returncode: print(mid, 'BUILD', r.stderr[-500:], r.stdout[-300:]); continue
    raw = os.path.join(OUT, mid + '.raw.html')
    r = subprocess.run([sys.executable, '-I', Q.BT, src, AD, tu, '--out=' + raw, '--shared-urls=' + ts, '--no-preview'], capture_output=True, text=True, cwd='/tmp')
    if r.returncode: print(mid, 'RAW', r.stderr[-500:]); continue
    k = open(raw).read(); F, W, _ = Q.tags_filters(k)
    fo = Q.foster(k)
    for tag, sample, country in VAR['us' if '-us' in mid else 'int']:
        if 'twopans' in mid and tag.endswith('-set'): continue
        c = Q.context(sample); c['person']['Country'] = country
        h = Q.engine().from_string(k).render(c)
        probs = Q.after_render(h) + fo
        open(os.path.join(OUT, '%s-%s.html' % (mid, tag)), 'w').write(h)
        t = re.sub(r'<[^>]+>', ' ', re.sub(r'<style.*?</style>|<!--.*?-->', '', h, flags=re.S))
        cards = re.findall(r'alt="Siraat ([^"]+)" style="display:block;width:100%;max-width:118px', h) + re.findall(r'alt="Siraat ([^"]+)" style="display:block;width:92px', h)
        print(mid, tag, 'tagsF:%d' % len(F), probs[:3] or 'ok', '| dash:%d' % (h.count('—') + h.count('–')), '| lockup:%s' % ('logo-black-cream' in h or 'logo-white' in h),
              '| footer:%s' % ('unsubscribe' in h.lower()), '| $:%d' % t.count('$'), '| kaarten:%s' % cards, '| KB %.0f' % (len(h.encode()) / 1024))
