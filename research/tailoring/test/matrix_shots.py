"""Screenshots en hoogtes per productcel (productmatrix). Bouwt de mail zoals de export (scripts/qa_render.py build),
rendert hem met Django op samples/<trig>_x_<cat>.json en meet in Chromium op 390 en 600 px.
Gebruik (vanuit /tmp): python3 -I <repo>/research/tailoring/test/matrix_shots.py checkout/c1:apron,pizza,set12 cart/k1-acc:board ...
Uitvoer: exports/qa/matrix/<flow>-<mail>-<cat>-<mobile|desktop>.jpg en een regel per cel met de hoogte op 390 px."""
import sys, os, json, subprocess, tempfile
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
sys.argv = [sys.argv[0]] + sys.argv[1:]
args = [a for a in sys.argv[1:] if not a.startswith('--')]; sys.argv = sys.argv[:1]
import qa_render as Q
TRIG = {'checkout': 'co', 'cart': 'atc', 'browse': 'vp', 'post-purchase': 'po', 'winback': 'po', 'vip': 'po', 'anniversary': 'po'}
OUT = os.path.join(ROOT, 'exports', 'qa', 'matrix'); os.makedirs(OUT, exist_ok=True)
tmp = tempfile.mkdtemp(prefix='mx-'); jobs = []; F = 0
for a in args:
    fm, cats = a.split(':'); flow, mail = fm.split('/')
    src = os.path.join(Q.V, flow, mail + '.html'); rawp, k = Q.build(flow, src, tmp)
    for c in cats.split(','):
        r = Q.engine().from_string(k).render(Q.context('%s_x_%s' % (TRIG[flow], c)))
        bad = Q.after_render(r)
        if bad: print('FOUT', flow, mail, c, bad); F = 1
        p = os.path.join(tmp, '%s-%s-%s.html' % (flow, mail, c)); open(p, 'w').write(r)
        for w, dev in ((390, 'mobile'), (600, 'desktop')):
            jobs.append(dict(key='%s|%s|%s|%d' % (flow, mail, c, w), html=p, width=w, shot=os.path.join(OUT, '%s-%s-%s-%s.jpg' % (flow, mail, c, dev)), raw=False))
jf = os.path.join(tmp, 'j.json'); rf = os.path.join(tmp, 'r.json'); json.dump(jobs, open(jf, 'w'))
subprocess.run(['node', os.path.join(ROOT, 'scripts', 'qa_shots.js'), jf, rf], check=True)
for key, m in sorted(json.load(open(rf)).items()):
    flow, mail, c, w = key.split('|')
    if 'error' in m: print('FOUT', key, m['error']); F = 1; continue
    probs = m['narrow'] + m['wideImgs'] + m['badImgs'] + (['overflow %d' % m['scrollWidth']] if m['scrollWidth'] > m['vw'] else [])
    if w == '390': print('%-14s %-16s %-9s hoogte %5d px %s' % (flow, mail, c, m['height'], ' '.join(probs)))
    if probs: F = 1
sys.exit(F)
