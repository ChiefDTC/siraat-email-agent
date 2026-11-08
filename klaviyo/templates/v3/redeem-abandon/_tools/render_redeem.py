"""Redeem 13.78 (8 nov 2026): build (build_template: .klaviyo.html met CDN-links) + Django-render op een checkout- en cart-voorbeeld + checks.
R2 wordt twee keer gerenderd: met en zonder person.siraat_redeem_code.
Gebruik (vanuit /tmp): python3 -I render_redeem.py <uitmap>; daarna node shot_redeem.js <uitmap> <previewmap>."""
import sys, os, subprocess
sys.path.insert(0, '/home/user/siraat-email-agent/scripts'); import qa_render as Q
N = '/home/user/siraat-email-agent/klaviyo/templates/v3/redeem-abandon'; SH = Q.SH; AD = '/home/user/siraat-email-agent/klaviyo/templates/partials/assets'
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
ts = os.path.join(OUT, 's.txt'); tu = os.path.join(OUT, 'u.txt')
open(tu, 'w').write(''.join('%s file://%s\n' % (n, os.path.join(AD, n)) for n in sorted(os.listdir(AD)) if os.path.isfile(os.path.join(AD, n))))
open(ts, 'w').write(''.join('%s file://%s\n' % (n, os.path.join(SH, n)) for n in sorted(os.listdir(SH)) if os.path.isfile(os.path.join(SH, n))))
SAMPLE = {'checkout': 'co_pan', 'cart': 'atc_pan'}
for mid in ('r1-checkout', 'r2-checkout', 'r1-cart', 'r2-cart'):
    src = os.path.join(N, mid + '.html')
    r = subprocess.run([sys.executable, '-I', Q.BT, src, AD, os.path.join(AD, 'klaviyo-urls.txt'), '--shared-urls=' + os.path.join(SH, 'klaviyo-urls.txt'), '--no-preview'], capture_output=True, text=True, cwd='/tmp')
    if r.returncode: print(mid, 'BUILD', r.stderr[-500:], r.stdout[-300:]); continue
    raw = os.path.join(OUT, mid + '.raw.html')
    r = subprocess.run([sys.executable, '-I', Q.BT, src, AD, tu, '--out=' + raw, '--shared-urls=' + ts, '--no-preview'], capture_output=True, text=True, cwd='/tmp')
    if r.returncode: print(mid, 'RAW', r.stderr[-500:]); continue
    k = open(raw).read()
    for var in (('', {}), ('-withcode', {'siraat_redeem_code': 'SRT-K7Q2M'})) if mid.startswith('r2') else (('', {}),):
        c = Q.context(SAMPLE[mid.split('-')[1]]); c['email'] = 'you@example.com'
        c['person'].update({'Country': 'United States'}); c['person'].update(var[1])
        h = Q.engine().from_string(k).render(c)
        probs = Q.after_render(h) + Q.foster(h)
        open(os.path.join(OUT, mid + var[0] + '.html'), 'w').write(h)
        kv = open(os.path.join(N, mid + '.klaviyo.html')).read()
        hrefs = sorted(set(x.split('"')[0][:150] for x in h.split('href="')[1:] if 'discount' in x[:120] or '/cart' in x[:60] or 'checkouts' in x[:60]))
        print(mid + var[0], probs[:3] or 'ok', '| emdash:%d' % (kv.count('—') + kv.count('–')), '| footer-unsub:%s' % ('unsubscribe' in kv.lower()),
              '| coupon-tags:%d' % kv.count('coupon_code'), '| KB %.0f' % (len(kv.encode()) / 1024))
        for x in hrefs: print('    ', x)
