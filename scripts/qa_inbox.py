"""Inbox- en deliverability-wachter voor alle v4-mails (research/deliverability/01-inbox-check.md).
Bouwt elke mail zoals scripts/qa_render.py (build_template.py, Django-render op de eerste event-variant) en meet:
 1. Gmail-clipping: HTML-grootte ruw, quoted-printable en geschat na Klaviyo-linktracking (alle varianten, de grootste telt)
 2. spamsignalen (onderwerp, preview, body), tekst tegenover beeld, links en domeinen, linkverkorters, alt-teksten, plain-text
 3. dark mode: light, prefers-color-scheme dark, gedeeltelijke en volledige inversie (simulatie); logo, lichte randen, contrast
 4. Outlook (Windows): VML-knoppen, verborgen elementen, beelden zonder width, max-width zonder ghost table
 5. toegankelijkheid op 390 px: tekst < 14 px, tap targets < 44 px, contrast WCAG AA
Gebruik (vanuit /tmp): python3 -I scripts/qa_inbox.py [--only=checkout/c1,...]
Uitvoer: exports/qa/inbox-report.md, exports/qa/inbox-data.json, exports/qa/darkmode/<flow>-<id>.jpg (6 representatieve mails).
Alleen meten; wijzigt geen templates. Exitcode altijd 0 (de poort is qa_render.py; deze checks staan daar als waarschuwing).

Inbox-QA per ontvangen mail (testcheckouts, research/v6-golive/04-inbox-qa.md), controles in scripts/mail_checks.py:
  python3 -I scripts/qa_inbox.py mail <bestand.json|.eml|.html> [--market=UK] [--alias=pan] [--out=map] [--no-net] [--no-browser]
      bestand.json = uitvoer van mcp__Gmail__get_message (FULL_CONTENT). Schrijft <out>/report.md, result.json, slack.txt en
      screenshots (375/600/1200 px licht, 375/600 px dark, 375 px geforceerd donker). Exitcode 1 bij FOUT.
  python3 -I scripts/qa_inbox.py templates [--markets=US,UK] [--only=checkout/c1,...] [--shots=map]
      alle mails uit de repo, gerenderd per markt (zelfde route als qa_render.py), dezelfde controles.
      Uitvoer: exports/qa/inbox/templates-report.md en templates-data.json.
  python3 -I scripts/qa_inbox.py pending <id,id,...>     welke Gmail-ID's nog niet gecontroleerd zijn (exports/qa/inbox/seen.tsv)
  python3 -I scripts/qa_inbox.py slack <result.json>     print het Slack-bericht (niet versturen; dat doet de sessie na akkoord)"""
import sys, os, re, json, csv, subprocess, tempfile, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qa_render as Q
import inbox_checks as I
import mail_checks as MC

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
        pt = I.plain_text(r0); e['plain_chars'] = len(pt); e['plain_dupes'] = I.plain_dupes(r0)
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


# ------------------------------------------------------------------ inbox-QA per mail (mail, templates, slack)
ICON = {MC.OK: ':white_check_mark:', MC.FOUT: ':x:', MC.LETOP: ':warning:', MC.NVT: ':heavy_minus_sign:'}
LABEL = {'onderwerp': 'Onderwerp', 'preheader': 'Preheader', 'afzender': 'Afzender', 'grootte': 'Grootte (Gmail-clip 102 KB)',
         'links': 'Links (status 200)', 'utm': 'UTM', 'linktekst': 'Linktekst past bij bestemming', 'beelden': 'Beelden',
         'tags': 'Ongerenderde tags', 'markt': 'Valuta en maat', 'header-footer': 'Header, footer, logo', 'afmelden': 'Afmelden en voorkeuren',
         'em-dash': 'Em dash', 'layout': 'Layout 375/600/1200 px', 'dark-mode': 'Dark mode'}
AMS = None


def opts(args):
    o = {}; pos = []
    for a in args:
        if a.startswith('--'): k, _, v = a[2:].partition('='); o[k] = v or '1'
        else: pos.append(a)
    return o, pos


def manifest():
    try: return {r['flow'] + '/' + r['id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'exports', 'manifest.csv')))}
    except Exception: return {}


def which_mail(subject):
    """flow/id uit de manifest op onderwerp (A of B); None als onbekend (bijv. campagne of oude flow)."""
    n = MC._norm(subject)
    for k, r in manifest().items():
        if n and n in (MC._norm(r.get('onderwerp_a')), MC._norm(r.get('onderwerp_b'))): return k
    return None


def amsterdam(iso):
    try:
        from datetime import datetime
        from zoneinfo import ZoneInfo
        d = datetime.fromisoformat(iso.replace('Z', '+00:00')).astimezone(ZoneInfo('Europe/Amsterdam'))
        return '%d %s %s' % (d.day, 'jan feb mrt apr mei jun jul aug sep okt nov dec'.split()[d.month - 1], d.strftime('%H:%M'))
    except Exception: return iso or '?'


def browser_run(jobs):
    if not jobs: return {}
    tmp = tempfile.mkdtemp(prefix='qa-mail-'); jf = os.path.join(tmp, 'jobs.json'); rf = os.path.join(tmp, 'res.json')
    json.dump(jobs, open(jf, 'w'))
    r = subprocess.run(['node', os.path.join(ROOT, 'scripts', 'qa_mail_shots.js'), jf, rf], capture_output=True, text=True)
    if r.returncode or not os.path.exists(rf): print('browser faalt: ' + (r.stderr or r.stdout)[-400:]); return {}
    res = json.load(open(rf)); shutil.rmtree(tmp, ignore_errors=True); return res


MAIL_VIEWS = [(375, 'light'), (600, 'light'), (1200, 'light'), (375, 'dark'), (600, 'dark'), (375, 'forced')]


def md_report(res, meta):
    L = ['# Inbox-QA: %s' % meta['title'], '', '- Alias: %s (markt %s)' % (meta.get('alias') or '-', meta.get('market') or '?'),
         '- Ontvangen: %s · afzender %s' % (meta.get('when') or '-', meta.get('sender') or '-'),
         '- Gmail: %s' % (meta.get('url') or '-'), '', '| controle | status | details |', '|---|---|---|']
    for k in MC.CHECKS:
        if k in res: L.append('| %s | %s | %s |' % (LABEL[k], res[k]['status'], res[k]['detail'].replace('|', '/')))
    L += ['', '## Links', '', '| tekst | bestemming | via | status |', '|---|---|---|---|']
    for r in res.get('_links', []):
        L.append('| %s | %s | %s | %s |' % ((r['text'] or '')[:50].replace('|', '/'), (r['dest'] or r['href'])[:110], r['via'], r['status']))
    if meta.get('shots'): L += ['', '## Screenshots', ''] + ['- %s' % x for x in meta['shots']]
    return '\n'.join(L) + '\n'


def slack_text(res, meta):
    c = MC.summary(res)
    who = ('lolagroothuis+%s' % meta['alias']) if meta.get('alias') else (meta.get('to') or '?')
    L = [':envelope_with_arrow: *Nieuwe e-mail ontvangen:* %s, %s (%s), %s' % (meta.get('mail') or meta['title'].split(' "')[0], who, meta.get('market') or '?', meta.get('when') or '?'),
         'Onderwerp: "%s"%s' % (meta.get('subject') or '', ' · <%s|open in Gmail>' % meta['url'] if meta.get('url') else ''),
         '*%d OK · %d FOUT · %d LET OP*' % (c[MC.OK], c[MC.FOUT], c[MC.LETOP]), '']
    for st in (MC.FOUT, MC.LETOP):
        for k in MC.CHECKS:
            if k in res and res[k]['status'] == st: L.append('%s *%s*: %s' % (ICON[st], LABEL[k], res[k]['detail'][:260]))
    oks = [LABEL[k] for k in MC.CHECKS if k in res and res[k]['status'] == MC.OK]
    if oks: L.append('%s %s' % (ICON[MC.OK], ', '.join(oks)))
    nv = [LABEL[k] for k in MC.CHECKS if k in res and res[k]['status'] == MC.NVT]
    if nv: L.append('%s niet van toepassing: %s' % (ICON[MC.NVT], ', '.join(nv)))
    if meta.get('shots'): L += ['', 'Screenshots (375 licht, 375 dark, 600 licht) als bijlage in de thread; volledig rapport: `%s`' % meta.get('report', '')]
    return '\n'.join(L).replace('\u2014', ',')


def rel(p):
    p = os.path.abspath(p); return os.path.relpath(p, ROOT) if p.startswith(ROOT + os.sep) else p


def cmd_mail(args):
    o, pos = opts(args)
    if not pos: sys.exit('gebruik: qa_inbox.py mail <bestand> [--market=..] [--alias=..]')
    m = MC.load(pos[0])
    alias = o.get('alias') or MC.alias_of(m['to']); market = o.get('market') or MC.market_of_alias(alias)
    fm = o.get('flow') or which_mail(m.get('subject') or '')
    title = '%s "%s"' % (fm or 'onbekende mail (geen v5-onderwerp)', m.get('subject') or '')
    stamp = (m.get('id') or os.path.basename(pos[0]).rsplit('.', 1)[0])
    out = o.get('out') or os.path.join(QA, 'inbox', '%s-%s' % ((alias or 'mail'), stamp))
    os.makedirs(os.path.join(out, 'shots'), exist_ok=True)
    hp = os.path.join(out, 'mail.html'); open(hp, 'w').write(m['html'])
    jobs = [] if 'no-browser' in o else [dict(key='%s|%d' % (md, w), html=hp, width=w, mode=md, net='no-net' not in o,
                                              shot=os.path.join(out, 'shots', '%s-%d.jpg' % (md, w))) for w, md in MAIL_VIEWS]
    B = browser_run(jobs)
    for j in jobs:
        if j['key'] in B: B[j['key']]['shot'] = j['shot']
    res = MC.run_checks(m, market, kind='mail', browser={'jobs': list(B.values()), 'unsubContrast': sum((b.get('unsubContrast', []) for b in B.values()), [])} if B else None,
                        skip_net='no-net' in o)
    if fm and res['header-footer']['status'] == MC.FOUT and 'header mist' in res['header-footer']['detail']:
        title = 'geen v5-mail (onderwerp gelijk aan %s, maar zonder vaste header) "%s"' % (fm, m.get('subject') or '')
    meta = dict(title=title, mail=title.split(' "')[0], subject=m.get('subject'), alias=alias, market=market, when=amsterdam(m.get('date') or ''), sender=m.get('sender'), url=m.get('url'),
                to=', '.join(m['to']), shots=sorted(rel(j['shot']) for j in jobs), report=rel(os.path.join(out, 'report.md')))
    json.dump({'meta': meta, 'result': res}, open(os.path.join(out, 'result.json'), 'w'), indent=1, default=str)
    open(os.path.join(out, 'report.md'), 'w').write(md_report(res, meta))
    st = slack_text(res, meta); open(os.path.join(out, 'slack.txt'), 'w').write(st)
    print(st); print('\nRapport: %s' % rel(out))
    if m.get('id'):
        with open(SEEN, 'a') as f: f.write('%s\t%s\t%s\t%s\n' % (m['id'], alias or '-', m.get('subject') or '', rel(out)))
    sys.exit(1 if any(res[k]['status'] == MC.FOUT for k in MC.CHECKS if k in res) else 0)


SEEN = os.path.join(QA, 'inbox', 'seen.tsv')


def cmd_pending(args):
    """Welke Gmail-ID's (komma's) zijn nog niet gecontroleerd? Voor de loop: alleen nieuwe mails ophalen en checken."""
    seen = {l.split('\t')[0] for l in open(SEEN)} if os.path.exists(SEEN) else set()
    ids = [x for a in args for x in a.split(',') if x and not x.startswith('--')]
    print(' '.join(i for i in ids if i not in seen) or '(niets nieuw)')


def cmd_slack(args):
    o, pos = opts(args); d = json.load(open(pos[0])); print(slack_text(d['result'], d['meta']))


def cdn_map(flow):
    mp = {}
    for f in (os.path.join(Q.V, flow, 'assets', 'klaviyo-urls.txt'), os.path.join(Q.SH, 'klaviyo-urls.txt')):
        if os.path.exists(f):
            for line in open(f):
                parts = line.split()
                if len(parts) >= 2: mp.setdefault(parts[0], parts[1])
    return mp


def cmd_templates(args):
    import v5lib
    sys.path.insert(0, os.path.join(ROOT, 'research', 'tailoring', 'test')); import v5checks as V5C
    o, pos = opts(args)
    markets = (o.get('markets') or 'US,UK').split(',')
    ms = Q.mails(); tmp = tempfile.mkdtemp(prefix='qa-inbox-tpl-'); man = manifest()
    shots = o.get('shots') or os.path.join(tmp, 'shots')   # zonder --shots: tijdelijk (nodig voor de pixelcontrole in dark mode)
    os.makedirs(shots, exist_ok=True)
    D = {}; jobs = []; cdn_todo = {}
    for flow, mid, src in ms:
        key = flow + '/' + mid
        try: rawp, k = Q.build(flow, src, tmp)
        except Exception as ex: D[key] = {'err': str(ex)[:200]}; continue
        sa, sb, pv = I.meta(src); mf = man.get(key, {})
        base = Q.VARIANTS[flow][0][0].partition('+')[0]
        bev = {} if base == 'none' else json.load(open(os.path.join(Q.TEST, 'samples', base + '.json')))
        cm = cdn_map(flow)
        for mk in markets:
            ev, person = V5C.market_ctx(v5lib.sig_of(flow), mk, bev)
            ctx = {'event': ev, 'first_name': 'Sarah', 'person': person, 'organization': {'name': "Siraat's Kitchen", 'full_address': MC.REAL_ADDRESS}}
            e = D.setdefault(key, {})[mk] = {}
            try: r = Q.engine().from_string(k).render(ctx)
            except Exception as ex: e['err'] = 'rendering faalt: %s' % str(ex)[:160]; continue
            rp = os.path.join(tmp, '%s-%s-%s.html' % (flow, mid, mk)); open(rp, 'w').write(r)
            e.update(html=rp, raw=k, subject=sa or mf.get('onderwerp_a', ''), preview=pv or mf.get('preview', ''))
            for w, md in [(375, 'light'), (600, 'light'), (1200, 'light'), (375, 'dark'), (375, 'forced')]:
                sh = os.path.join(shots, '%s-%s-%s-%s-%d.jpg' % (mk, flow, mid, md, w)) if (w, md) in ((375, 'light'), (600, 'light'), (375, 'dark'), (375, 'forced')) else None
                jobs.append(dict(key='%s|%s|%s|%d' % (key, mk, md, w), html=rp, width=w, mode=md, net=False, shot=sh))
        for nm in set(re.findall(r'src="file://[^"]*/([^"/]+)"', k)):
            cdn_todo[nm] = cm.get(nm)
        print('%-14s %-22s gebouwd' % (flow, mid), flush=True)
    print('browser: %d metingen' % len(jobs), flush=True)
    B = browser_run(jobs)
    for j in jobs:
        if j['key'] in B: B[j['key']]['shot'] = j['shot']
    # CDN: staat elk beeld in de Klaviyo-bibliotheek en laadt het?
    MC.prefetch([u for u in cdn_todo.values() if u], head=True)
    cdn_bad = {nm: (MC.curl(u, head=True)[0] if u else 'niet in klaviyo-urls.txt') for nm, u in cdn_todo.items()}
    cdn_bad = {nm: st for nm, st in cdn_bad.items() if st != 200}
    R = {}
    for key, per in D.items():
        for mk, e in per.items() if isinstance(per, dict) and 'err' not in per else []:
            if 'err' in e: R.setdefault(key, {})[mk] = {'tags': {'status': MC.FOUT, 'detail': e['err']}}; continue
            html = open(e['html']).read()
            bj = [B[j] for j in B if j.startswith('%s|%s|' % (key, mk))]
            m = {'html': html, 'subject': e['subject'], 'preheader': MC.preheader(html) or e['preview'], 'plain': ''}
            res = MC.run_checks(m, mk, kind='template', raw=e['raw'],
                                browser={'jobs': bj, 'unsubContrast': sum((b.get('unsubContrast', []) for b in bj), [])})
            used = set(re.findall(r'src="file://[^"]*/([^"/]+)"', html)); cb = {nm: cdn_bad[nm] for nm in used if nm in cdn_bad}
            if cb:
                res['beelden']['status'] = MC.FOUT
                res['beelden']['detail'] += '; CDN-versie ontbreekt of laadt niet: ' + ', '.join('%s (%s)' % kv for kv in sorted(cb.items())[:5])
            res.pop('_images', None)
            res['_links'] = [{k2: v for k2, v in r.items() if k2 in ('text', 'dest', 'status')} for r in res['_links']]
            R.setdefault(key, {})[mk] = res
        if isinstance(per, dict) and 'err' in per: R[key] = {mk: {'tags': {'status': MC.FOUT, 'detail': per['err']}} for mk in markets}
    shutil.rmtree(tmp, ignore_errors=True)
    od = os.path.join(QA, 'inbox'); os.makedirs(od, exist_ok=True)
    suf = '-only' if Q.OPT.get('--only') else ''   # een deelrun overschrijft het volledige rapport niet
    json.dump(R, open(os.path.join(od, 'templates-data%s.json' % suf), 'w'), indent=1, default=str)
    open(os.path.join(od, 'templates-report%s.md' % suf), 'w').write(tpl_report(R, markets))
    tot = sum(1 for k in R for mk in R[k] if any(R[k][mk].get(c, {}).get('status') == MC.FOUT for c in MC.CHECKS))
    print('Templates: %d mails x %d markten, %d renders met FOUT. Rapport: exports/qa/inbox/templates-report%s.md' % (len(R), len(markets), tot, suf))


def sysnorm(part):
    """Detailregel zonder getallen en beeldlijsten, om dezelfde fout in veel mails als één systematisch punt te tellen."""
    part = re.sub(r'(lichte blokken[^:]*):.*', r'\1', part)
    return re.sub(r'\d+(?:\.\d+)?', '#', part)


def tpl_report(R, markets):
    # systematische punten: dezelfde detailregel in >= 80% van de renders
    from collections import Counter
    cnt = Counter(); n = 0; ex = {}
    for k in R:
        for mk in R[k]:
            n += 1
            for c in MC.CHECKS:
                x = R[k][mk].get(c)
                if x and x['status'] in (MC.FOUT, MC.LETOP):
                    for part in x['detail'].split('; '): cnt[(c, x['status'], sysnorm(part))] += 1; ex.setdefault((c, x['status'], sysnorm(part)), part)
    common = {key for key, v in cnt.items() if v >= 0.6 * n and n > 2}
    L = ['# Inbox-QA op alle templates (automatisch)', '', 'Gegenereerd door `python3 -I scripts/qa_inbox.py templates --markets=%s`. '
         'Controles uit `scripts/mail_checks.py`; renders met Django op het eerste testevent per flow, markt via `v5checks.market_ctx`.' % ','.join(markets), '',
         '## Systematisch (in vrijwel elke mail)', '']
    for key in sorted(common): L.append('- %s %s: %s (%d van %d renders)' % (key[1], LABEL[key[0]], ex[key], cnt[key], n))
    L += ['', '## Overzicht', '', '| mail | ' + ' | '.join('%s FOUT / LET OP' % mk for mk in markets) + ' |', '|---|' + '---|' * len(markets)]
    for k in R:
        cells = []
        for mk in markets:
            x = R[k].get(mk, {})
            f = [LABEL[c] for c in MC.CHECKS if x.get(c, {}).get('status') == MC.FOUT]
            w = [LABEL[c] for c in MC.CHECKS if x.get(c, {}).get('status') == MC.LETOP]
            cells.append('%s / %s' % (', '.join(f) or '-', ', '.join(w) or '-'))
        L.append('| %s | %s |' % (k, ' | '.join(cells)))
    L += ['', '## Details per mail (zonder de systematische punten)', '']
    for k in R:
        lines = []
        for mk in markets:
            x = R[k].get(mk, {})
            for c in MC.CHECKS:
                y = x.get(c)
                if not y or y['status'] not in (MC.FOUT, MC.LETOP): continue
                parts = [p for p in y['detail'].split('; ') if (c, y['status'], sysnorm(p)) not in common]
                parts = [p for p in parts if not re.match(r'^\d+ (links|beelden)', p)] or ([] if not parts else parts)
                if parts: lines.append('- %s %s %s: %s' % (mk, y['status'], LABEL[c], '; '.join(parts)[:400]))
        if lines: L += ['### ' + k, ''] + lines + ['']
    return '\n'.join(L) + '\n'


def dispatch():
    if len(sys.argv) > 1 and sys.argv[1] in ('mail', 'templates', 'slack', 'pending'):
        cmd, args = sys.argv[1], sys.argv[2:]
        {'mail': cmd_mail, 'templates': cmd_templates, 'slack': cmd_slack, 'pending': cmd_pending}[cmd](args)
    else:
        main()


if __name__ == '__main__': dispatch()
