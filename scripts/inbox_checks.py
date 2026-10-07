"""Inbox- en deliverability-controles zonder browser (research/deliverability/01-inbox-check.md).
Gebruikt door scripts/qa_render.py (alleen waarschuwingen, nooit FOUT) en scripts/qa_inbox.py (volledig rapport).

  warnings(src, k, renders)  lijst met waarschuwingen voor één mail
    src      bron-template (topcomment met SUBJECT_A, SUBJECT_B, PREVIEW)
    k        Klaviyo-versie zoals build_template.py hem maakt (ruw, met Django-tags)
    renders  dezelfde mail na Django-rendering, één string per event-variant

Aannames (zie het onderzoeksrapport):
- Gmail knipt een bericht af als de HTML-part groter is dan ~102 KB. We meten de quoted-printable-gecodeerde grootte
  (elke '=' in de HTML wordt '=3D', plus zachte regeleinden) en tellen per link TRK_BYTES op, omdat Klaviyo elke href
  bij verzending vervangt door een eigen klik-redirect. Waarschuwing vanaf WARN_KB, ernstig vanaf HARD_KB.
- Klaviyo maakt bij CODE-templates zonder tekstversie zelf een plain-text-part uit de HTML. CSS telt daarbij niet:
  inhoud met display:none (mobiele of desktop-varianten) komt dus dubbel in de tekstversie.
"""
import os, re, quopri, html as H
from urllib.parse import urlparse, unquote

GMAIL_CLIP_KB = 102
WARN_KB = 80
HARD_KB = 95
TRK_BYTES = 600      # conservatief: lengte van een Klaviyo-kliktracking-URL (ouder formaat trk.klclick.com/ls/click?upn=... is 400-900 tekens)
PIXEL_BYTES = 500    # open-pixel en wat Klaviyo verder toevoegt

SHORTENERS = ('bit.ly', 'tinyurl.com', 't.co', 'goo.gl', 'ow.ly', 'rebrand.ly', 'cutt.ly', 'is.gd', 'buff.ly', 'shorturl.at',
              'tiny.cc', 'rb.gy', 'lnkd.in', 'bl.ink', 'short.io', 'linktr.ee')
# Klassieke spamtriggers. Niet elk woord is een probleem; samen met beeldzwaarte en klachten telt het mee (SpamAssassin-achtig).
SPAM_I = [r'\bact now\b', r'\bbuy now\b', r'\border now\b', r'\bclick here\b', r'\blimited time\b', r'\bonce in a lifetime\b',
          r'\brisk[- ]free\b', r'\b100% free\b', r'\bno cost\b', r'\bcash\b', r'\bwinner\b', r"\byou(?:'ve| have) won\b",
          r'\bcongratulations\b', r'\burgent\b', r'\bspecial promotion\b', r"\bdon'?t miss\b", r'\bexpires? (?:today|tonight)\b',
          r'\bfree gift\b', r'\bcheap\b', r'\bbest price\b', r'\bdouble your\b', r'\bmiracle\b', r'\bno obligation\b',
          r'\bapply now\b', r'\bget it now\b', r'\blast chance\b', r'\bfinal (?:call|notice)\b', r'\bguarantee[ds]?\b']
SPAM_CS = [r'\bFREE\b', r'\$\$+', r'!!+']


def meta(src):
    """SUBJECT_A, SUBJECT_B, PREVIEW uit de topcomment (zelfde regel als export_klaviyo.py)."""
    try: top = open(src).read().split('\n', 1)[0]
    except Exception: return '', '', ''
    def g(k):
        m = re.search(r'(?:<!--|\|)\s*' + k + r':\s*(.*?)\s*(?:\||-->)', top)
        return re.sub(r'\s*\((?:reserve|niet gebruiken|phase|fase)[^)]*\)\s*$', '', H.unescape(m.group(1)).strip()) if m else ''
    return g('SUBJECT_A'), g('SUBJECT_B'), g('PREVIEW')


def hrefs(x):
    return [h for h in re.findall(r'\bhref="([^"]*)"', x) if h.strip() and not h.startswith('#')]


def domain(u):
    try:
        n = urlparse(H.unescape(u).strip()).netloc.lower()
        return n[4:] if n.startswith('www.') else n
    except Exception:
        return ''


def sizes(r):
    """(ruw KB, quoted-printable KB, geschat verzonden KB, aantal links) voor één gerenderde mail."""
    b = r.encode('utf-8'); qp = len(quopri.encodestring(b)); n = len(hrefs(r))
    return len(b) / 1024, qp / 1024, (qp + n * TRK_BYTES + PIXEL_BYTES) / 1024, n


def visible_text(r):
    """Tekst zoals een lezer hem ziet: zonder head/style/commentaar, zonder display:none-blokken en zonder preheader."""
    x = re.sub(r'<head.*?</head>|<style.*?</style>|<!--.*?-->', '', r, flags=re.S)
    x = strip_hidden(x)
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', x))).strip()


def strip_hidden(x):
    """Verwijdert elementen met display:none in de inline-stijl (mobiele varianten, preheader)."""
    out = x
    for _ in range(30):
        m = re.search(r'<(div|table|tr|td|span|p|a)\b[^>]*style="[^"]*display:\s*none[^"]*"[^>]*>', out, re.S)
        if not m: break
        tag = m.group(1); depth = 0; pos = m.start(); end = None
        for t in re.finditer(r'<(/?)%s\b[^>]*>' % tag, out[pos:], re.S):
            if t.group(0).endswith('/>'): continue
            depth += -1 if t.group(1) else 1
            if depth == 0: end = pos + t.end(); break
        if end is None: break
        out = out[:m.start()] + out[end:]
    return out


def plain_text(r):
    """Benadering van Klaviyo's automatische tekstversie (html2text-achtig): CSS telt niet, links als 'tekst (url)', beelden weg."""
    x = re.sub(r'<head.*?</head>|<style.*?</style>', '', r, flags=re.S)
    x = re.sub(r'<!--\[if mso\]>.*?<!\[endif\]-->', '', x, flags=re.S)
    x = re.sub(r'<!--.*?-->', '', x, flags=re.S)
    def a(m):
        t = re.sub(r'<[^>]+>', '', m.group(2)).strip(); u = m.group(1)
        if not t: return ''
        return '%s (%s)' % (t, u) if u.startswith('http') else t
    x = re.sub(r'<a\b[^>]*href="([^"]*)"[^>]*>(.*?)</a>', a, x, flags=re.S)
    x = re.sub(r'<br\s*/?>', '\n', x)
    x = re.sub(r'</(p|div|tr|h\d|li|table)>', '\n', x)
    x = re.sub(r'</td>', ' ', x)
    x = H.unescape(re.sub(r'<[^>]+>', '', x)).replace('‌', '').replace('\xa0', ' ')
    lines = [re.sub(r'[ \t]+', ' ', l).strip() for l in x.split('\n')]
    out = []
    for l in lines:
        if l or (out and out[-1]): out.append(l)
    return '\n'.join(out).strip()


def plain_dupes(pt):
    """Regels (langer dan 25 tekens, geen link) die meer dan één keer in de tekstversie staan."""
    seen = {}
    for l in pt.split('\n'):
        k = re.sub(r'\s*\(https?://[^)]*\)', '', l).strip()
        if len(k) > 25: seen[k] = seen.get(k, 0) + 1
    return {k: v for k, v in seen.items() if v > 1}


def spam_hits(text, where):
    hits = []
    for p in SPAM_I:
        for m in re.finditer(p, text, re.I): hits.append('%s: "%s"' % (where, m.group(0)))
    for p in SPAM_CS:
        for m in re.finditer(p, text): hits.append('%s: "%s"' % (where, m.group(0)))
    return hits


def caps_words(s):
    return [w for w in re.findall(r"\b[A-Z][A-Z']{3,}\b", s) if w not in ('PFAS', 'PFOA', 'HI10', 'USD', 'BPA')]


_IMGCACHE = {}
def png_info(path):
    """Voor dark mode: (heeft transparantie, gemiddelde luminantie van de zichtbare pixels, aandeel lichte dekkende randpixels)."""
    if path in _IMGCACHE: return _IMGCACHE[path]
    res = None
    try:
        from PIL import Image
        im = Image.open(path); im.seek(0); im = im.convert('RGBA')
        im.thumbnail((200, 200))
        px = list(im.getdata()) if not hasattr(im, 'get_flattened_data') else list(im.get_flattened_data())
        w, h = im.size
        alpha = any(p[3] < 250 for p in px)
        vis = [p for p in px if p[3] > 128]
        L = lambda p: (0.2126 * p[0] + 0.7152 * p[1] + 0.0722 * p[2]) / 255
        lum = sum(L(p) for p in vis) / len(vis) if vis else 1.0
        border = [px[i] for i in range(w)] + [px[(h - 1) * w + i] for i in range(w)] + [px[j * w] for j in range(h)] + [px[j * w + w - 1] for j in range(h)]
        light = sum(1 for p in border if p[3] > 200 and L(p) > 0.85) / max(1, len(border))
        res = (alpha, lum, light)
    except Exception:
        res = None
    _IMGCACHE[path] = res
    return res


def warnings(src, k, renders):
    W = []
    r = max(renders, key=len) if renders else k
    # 1. Gmail-clipping
    raw, qp, est, n = sizes(r)
    if est > HARD_KB: W.append('inbox: geschatte verzonden HTML %.0f KB (QP %.0f KB + %d links met Klaviyo-tracking): Gmail knipt boven ~%d KB' % (est, qp, n, GMAIL_CLIP_KB))
    elif est > WARN_KB: W.append('inbox: geschatte verzonden HTML %.0f KB (marge naar Gmail-clipping ~%d KB is klein)' % (est, GMAIL_CLIP_KB))
    # 2. spamsignalen in onderwerp en preview
    sa, sb, pv = meta(src)
    for nm, s in (('onderwerp A', sa), ('onderwerp B', sb), ('preview', pv)):
        if not s: continue
        for h in spam_hits(s, nm): W.append('inbox: spamsignaal in ' + h)
        if '!' in s: W.append('inbox: uitroepteken in %s (flows zijn kalm, PLAYBOOK 1)' % nm)
        cw = caps_words(s)
        if cw: W.append('inbox: woord in hoofdletters in %s: %s' % (nm, ', '.join(cw)))
    body = visible_text(r)
    bh = spam_hits(body, 'body')
    if bh:
        cnt = {}
        for h in bh: cnt[h] = cnt.get(h, 0) + 1
        W.append('inbox: spamsignalen in de body: ' + ', '.join('%s%s' % (h.split(': ', 1)[1], ' x%d' % c if c > 1 else '') for h, c in sorted(cnt.items())))
    ex = body.count('!')
    if ex > 2: W.append('inbox: %d uitroeptekens in de body' % ex)
    # tekst tegenover beeld
    imgs = re.findall(r'<img\b[^>]*>', strip_hidden(re.sub(r'<head.*?</head>', '', r, flags=re.S)), re.S)
    if len(body) < 500 and imgs: W.append('inbox: weinig live tekst (%d tekens) tegenover %d beelden' % (len(body), len(imgs)))
    # links
    hs = hrefs(r); doms = sorted({domain(h) for h in hs if h.startswith('http')} - {''})
    for h in hs:
        d = domain(h)
        if d in SHORTENERS or any(d.endswith('.' + s) for s in SHORTENERS): W.append('inbox: linkverkorter %s' % d)
        if h.startswith('http://'): W.append('inbox: link zonder https: %s' % h[:70])
    if len(hs) > 40: W.append('inbox: %d links (veel; elk wordt een Klaviyo-redirect en telt mee in de grootte)' % len(hs))
    if len(doms) > 6: W.append('inbox: %d verschillende linkdomeinen: %s' % (len(doms), ', '.join(doms)))
    for m in re.finditer(r'<a\b[^>]*href="(https?://[^"]*)"[^>]*>([^<]{4,80})</a>', r):
        t = m.group(2).strip()
        if re.match(r'^(https?://)?([\w-]+\.)+[a-z]{2,}(/\S*)?$', t, re.I) and domain(t if '://' in t else 'http://' + t) != domain(m.group(1)):
            W.append('inbox: linktekst %s wijst naar een ander domein (%s)' % (t, domain(m.group(1))))
    # alt-teksten en beeldbreedte (Outlook)
    for tag in re.findall(r'<img\b[^>]*>', k, re.S):
        s = re.search(r'src="([^"]*)"', tag); s = os.path.basename(s.group(1)) if s else '?'
        if not re.search(r'\balt="', tag): W.append('inbox: beeld zonder alt: %s' % s[:50])
        elif re.search(r'\balt="[^"]*\.(?:png|jpe?g|gif)"', tag, re.I): W.append('inbox: alt-tekst is een bestandsnaam: %s' % s[:50])
        if not re.search(r'\bwidth="\d+"', tag) and '{%' not in tag: W.append('outlook: beeld zonder width-attribuut (Outlook toont de ware grootte): %s' % s[:50])
    # 4. Outlook (Windows, Word-engine)
    nohide = [m.group(0)[:80] for m in re.finditer(r'<(?!div style="display:none;font-size:1px)[a-z]+\b[^>]*style="[^"]*display:\s*none(?![^"]*mso-hide:\s*all)[^"]*"[^>]*>', k)]
    if nohide: W.append('outlook: %d verborgen element(en) zonder mso-hide:all (Outlook kan ze tonen): %s' % (len(nohide), nohide[0]))
    if re.search(r'<div style="display:none;font-size:1px(?![^"]*mso-hide)', k): W.append('outlook: preheader zonder mso-hide:all')
    btn = 0
    for m in re.finditer(r'<a\b[^>]*style="[^"]*display:\s*block[^"]*padding[^"]*"[^>]*>', k):
        td = k.rfind('<td', 0, m.start())
        if 'v:roundrect' not in k[td:m.start()] and re.search(r'bgcolor="#|background:#', k[td:m.start()]): btn += 1
    if btn: W.append('outlook: %d knop(pen) zonder VML-fallback (padding op <a> valt weg in Outlook: lage knop, alleen de tekst klikbaar)' % btn)
    if re.search(r'background-image|\bbackground="', k) and 'v:rect' not in k: W.append('outlook: achtergrondafbeelding zonder VML (v:rect)')
    for m in re.finditer(r'<(div|table)\b[^>]*style="[^"]*max-width:\s*(\d+)px[^"]*"[^>]*>', k):
        if m.group(1) == 'div' or not re.search(r'\bwidth="\d+%?"', m.group(0)):
            W.append('outlook: %s met max-width:%spx zonder width-attribuut of ghost table (Outlook negeert max-width)' % (m.group(1), m.group(2))); break
    # 3. dark mode (statisch): zwart logo op transparant, geen dark-mode-regels
    dm = 'prefers-color-scheme' in k or 'data-ogsc' in k
    for m in re.finditer(r'<img\b[^>]*src="file://([^"]+\.png)"[^>]*>', k):
        p = m.group(1); info = png_info(p)
        if info and info[0] and info[1] < 0.25 and not dm:
            W.append('dark mode: %s is donker op transparant en heeft geen dark-mode-variant (onleesbaar op donkere achtergrond)' % os.path.basename(p))
    # plain-text
    dup = plain_dupes(plain_text(r))
    if dup: W.append('plain-text: %d regel(s) dubbel in Klaviyo\'s automatische tekstversie (verborgen desk/mob-varianten), bijv. "%s"' % (len(dup), list(dup)[0][:60]))
    return sorted(set(W))
