"""Inbox- en deliverability-wachter voor alle v4-mails (research/deliverability/01-inbox-check.md).
Bouwt elke mail zoals scripts/qa_render.py (build_template.py, Django-render op de eerste event-variant) en meet:
 1. Gmail-clipping: HTML-grootte ruw, quoted-printable en geschat na Klaviyo-linktracking (alle varianten, de grootste telt)
 2. spamsignalen (onderwerp, preview, body), tekst tegenover beeld, links en domeinen, linkverkorters, alt-teksten, plain-text
 3. dark mode: light, prefers-color-scheme dark, gedeeltelijke en volledige inversie (simulatie); logo, lichte randen, contrast
 4. Outlook (Windows): VML-knoppen, verborgen elementen, beelden zonder width, max-width zonder ghost table
 5. toegankelijkheid op 390 px: tekst < 14 px, tap targets < 44 px, contrast WCAG AA
Gebruik (vanuit /tmp): python3 -I scripts/qa_inbox.py [--only=checkout/c1,...]
Uitvoer: exports/qa/inbox-report.md, exports/qa/inbox-data.json, exports/qa/darkmode/<flow>-<id>.jpg (6 representatieve mails).
Alleen meten; wijzigt geen templates. Exitcode altijd 0 (de poort is qa_render.py; deze checks staan daar als waarschuwing)."""
import sys, os, re, json, csv, subprocess, tempfile, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qa_render as Q
import inbox_checks as I

ROOT = Q.ROOT; QA = Q.QA; DM = os.path.join(QA, 'darkmode')
REPR = ['checkout/c1', 'browse/b1', 'welcome/w1-a', 'welcome/w2', 'post-purchase/p2', 'winback/r2-vip']
MODES = ['light', 'dark', 'partial', 'full']


def lin(v):
    v = v / 255; return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4


def rel(rgb): return 0.2126 * lin(rgb[0]) + 0.7152 * lin(rgb[1]) + 0.0722 * lin(rgb[2])


def ratio(a, b): x, y = sorted([a, b]); return (y + 0.05) / (x + 0.05)


def rgbv(s): return [int(x) for x in re.findall(r'\d+', s)[:3]]


def img_mean_rel(path):
    """Relatieve luminantie van de zichtbare pixels van een beeld (voor contrast tegen de achtergrond)."""
    try:
        from PIL import Image
        im = Image.open(path); im.seek(0); im = im.convert('RGBA'); im.thumbnail((160, 160))
        px = [p for p in (im.get_flattened_data() if hasattr(im, 'get_flattened_data') else im.getdata()) if p[3] > 128]
        if not px: return None
        return sum(rel(p) for p in px) / len(px)
    except Exception:
        return None


def main():
    ms = Q.mails(); tmp = tempfile.mkdtemp(prefix='qa-inbox-'); os.makedirs(DM, exist_ok=True)
    man = {r['flow'] + '/' + r['id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'exports', 'manifest.csv')))}
    D = {}; jobs = []
    for flow, mid, src in ms:
        key = flow + '/' + mid; e = D[key] = {'flow': flow, 'id': mid}
        rawp, k = Q.build(flow, src, tmp)
        rs = []
        for var, _ in Q.VARIANTS[flow]:
            try: rs.append((var, Q.engine().from_string(k).render(Q.context(var))))
            except Exception as ex: e.setdefault('err', []).append('%s: %s' % (var, str(ex)[:120]))
        if not rs: continue
        var0, r0 = rs[0]
        big = max(rs, key=lambda x: len(x[1]))
        raw, qp, est, nl = I.sizes(big[1])
        e.update(size_raw=round(raw, 1), size_qp=round(qp, 1), size_est=round(est, 1), size_var=big[0], links=nl,
                 domains=sorted({I.domain(h) for h in I.hrefs(r0) if h.startswith('http')} - {''}))
        sa, sb, pv = I.meta(src)
        m = man.get(key, {})
        e.update(subj_a=sa or m.get('onderwerp_a', ''), subj_b=sb or m.get('onderwerp_b', ''), preview=pv or m.get('preview', ''))
        e['warn'] = I.warnings(src, k, [x[1] for x in rs])
        body = I.visible_text(r0); e['body_chars'] = len(body); e['body_excl'] = body.count('!')
        pt = I.plain_text(r0); e['plain_chars'] = len(pt); e['plain_dupes'] = I.plain_dupes(pt)
        e['plain_django'] = bool(re.search(r'\{[%{]', pt))
        if key == 'checkout/c1' or key == 'welcome/w2': e['plain_sample'] = pt[:1800]
        e['imgs_tag'] = len(re.findall(r'<img\b', I.strip_hidden(re.sub(r'<head.*?</head>', '', r0, flags=re.S))))
        rp = os.path.join(tmp, '%s-%s.html' % (flow, mid)); open(rp, 'w').write(r0)
        for mode in MODES:
            shot = os.path.join(tmp, '%s-%s-%s.jpg' % (flow, mid, mode)) if key in REPR else None
            jobs.append(dict(key='%s|%s|390' % (key, mode), html=rp, width=390, mode=mode, shot=shot))
        jobs.append(dict(key='%s|light|600' % key, html=rp, width=600, mode='light', shot=None))
        print('%-14s %-22s %.1f KB est.' % (flow, mid, est), flush=True)
    jf = os.path.join(tmp, 'jobs.json'); rf = os.path.join(tmp, 'res.json'); json.dump(jobs, open(jf, 'w'))
    r = subprocess.run(['node', os.path.join(ROOT, 'scripts', 'qa_inbox.js'), jf, rf], capture_output=True, text=True)
    if r.returncode or not os.path.exists(rf): sys.exit('browser faalt: ' + (r.stderr or r.stdout)[-600:])
    M = json.load(open(rf))
    for jk, m in M.items():
        key, mode, w = jk.split('|'); e = D[key]
        if 'error' in m: e.setdefault('err', []).append('%s %s: %s' % (mode, w, m['error'])); continue
        if w == '600':
            e['img_area_pct'] = round(100 * m['imgArea'] / max(1, m['mainArea'])); continue
        e.setdefault('modes', {})[mode] = {'contrast_fail': m['contrastFail'], 'n_text': m['nText']}
        if mode == 'light':
            e['small'] = [x for x in m['small']]
            e['tap'] = m['tap']; e['height390'] = m['height']
        # beelden in dark mode: transparante donkere beelden en lichte randen
        if mode in ('partial', 'full', 'dark', 'light'):
            bad = []; frames = []; logo = {}
            for im in m['imgs']:
                p = im['src']; nm = os.path.basename(p); info = I.png_info(p) if os.path.exists(p) else None
                if not info: continue
                bg = rgbv(im['bg']); bgl = rel(bg)
                if info[0]:
                    fl = img_mean_rel(p)
                    if fl is not None:
                        cr = ratio(fl, bgl)
                        if nm.startswith('logo-'): logo[nm] = round(cr, 2)
                        if cr < 3 and im['w'] >= 20: bad.append('%s (%.1f:1 op %s)' % (nm, cr, im['bg']))
                elif info[2] > 0.5 and bgl < 0.2 and im['w'] < 380: frames.append(nm)
            e['modes'][mode].update(img_bad=sorted(set(bad)), frames=sorted(set(frames)), logo=logo)
    # screenshots: 4 panelen naast elkaar
    from PIL import Image, ImageDraw
    for key in REPR:
        if key not in D: continue
        flow, mid = key.split('/')
        ims = [Image.open(os.path.join(tmp, '%s-%s-%s.jpg' % (flow, mid, md))) for md in MODES if os.path.exists(os.path.join(tmp, '%s-%s-%s.jpg' % (flow, mid, md)))]
        if len(ims) != 4: continue
        h = max(i.height for i in ims) + 34; W = sum(i.width for i in ims) + 3 * 12
        c = Image.new('RGB', (W, h), (128, 128, 128)); d = ImageDraw.Draw(c); x = 0
        lab = {'light': 'licht', 'dark': 'prefers-color-scheme: dark', 'partial': 'gedeeltelijke inversie (Gmail Android, Outlook.com)', 'full': 'volledige inversie (Gmail iOS, Outlook Win)'}
        for md, im in zip(MODES, ims):
            d.text((x + 6, 10), lab[md], fill=(255, 255, 255)); c.paste(im, (x, 34)); x += im.width + 12
        c.save(os.path.join(DM, '%s-%s.jpg' % (flow, mid)), quality=62)
    shutil.rmtree(tmp, ignore_errors=True)
    json.dump(D, open(os.path.join(QA, 'inbox-data.json'), 'w'), indent=1, default=list)
    report(D)


def report(D):
    L = ['# Inbox-rapport (automatisch)', '', 'Gegenereerd door `scripts/qa_inbox.py`. Analyse en fixes: `research/deliverability/01-inbox-check.md`.', '',
         '| mail | KB ruw / QP / geschat | links | domeinen | live tekst | beeld % | spam | contrast licht / part. / vol | logo part. / vol | <14 px | tap < 44 | Outlook | plain-text dubbel |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for k, e in D.items():
        md = e.get('modes', {})
        cf = ' / '.join(str(len([x for x in md.get(mm, {}).get('contrast_fail', []) if not x['foot']])) for mm in ('light', 'partial', 'full'))
        lg = ' / '.join(str(md.get(mm, {}).get('logo', {}).get('logo-black.png', '-')) for mm in ('partial', 'full'))
        sm = len([x for x in e.get('small', []) if x['len'] > 40 and not x['foot']])
        tp = len([x for x in e.get('tap', []) if not x['foot']]); tpf = len([x for x in e.get('tap', []) if x['foot']])
        spam = len([w for w in e['warn'] if w.startswith('inbox: spam') or 'uitroep' in w or 'hoofdletters' in w])
        ol = len([w for w in e['warn'] if w.startswith('outlook')])
        L.append('| %s | %s / %s / %s | %d | %d | %d | %s | %d | %s | %s | %d | %d (+%d footer) | %d | %d |' % (
            k, e['size_raw'], e['size_qp'], e['size_est'], e['links'], len(e['domains']), e['body_chars'], e.get('img_area_pct', '-'),
            spam, cf, lg, sm, tp, tpf, ol, len(e['plain_dupes'])))
    L += ['', '## Waarschuwingen per mail', '']
    for k, e in D.items():
        L.append('### ' + k); L.append('')
        L.append('- Onderwerp A: "%s" · B: "%s" · preview: "%s"' % (e['subj_a'], e['subj_b'], e['preview']))
        for w in e['warn']: L.append('- ' + w)
        md = e.get('modes', {})
        for mm in ('light', 'partial', 'full'):
            x = md.get(mm, {})
            fails = [f for f in x.get('contrast_fail', []) if not f['foot']]
            if fails: L.append('- contrast %s: %d tekst(en) onder AA, bijv. "%s" %.2f:1 (%s op %s)' % (mm, len(fails), fails[0]['t'], fails[0]['r'], fails[0]['fg'], fails[0]['bg']))
            if x.get('img_bad'): L.append('- dark mode %s: beeld slecht zichtbaar: %s' % (mm, ', '.join(x['img_bad'][:4])))
            if x.get('frames'): L.append('- dark mode %s: lichte rand zichtbaar: %s' % (mm, ', '.join(x['frames'][:6])))
        sm = [s for s in e.get('small', []) if s['len'] > 40 and not s['foot']]
        if sm: L.append('- lopende tekst < 14 px op 390 px: %d, bijv. "%s" (%s px)' % (len(sm), sm[0]['t'], sm[0]['fs']))
        tp = [t for t in e.get('tap', []) if not t['foot']]
        if tp: L.append('- tap targets < 44 px (buiten footer): ' + ', '.join('"%s" %dx%d' % (t['t'], t['w'], t['h']) for t in tp[:5]))
        if e.get('err'): L.append('- meetfout: ' + '; '.join(e['err']))
        L.append('')
    open(os.path.join(QA, 'inbox-report.md'), 'w').write('\n'.join(L) + '\n')
    print('Rapport: exports/qa/inbox-report.md, data: exports/qa/inbox-data.json, screenshots: exports/qa/darkmode/')


if __name__ == '__main__': main()
