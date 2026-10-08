"""Inbox-QA per ontvangen mail (research/v6-golive/04-inbox-qa.md). Gebruikt door scripts/qa_inbox.py (subcommando's mail,
templates en slack). Neemt één mail (HTML-bestand, Gmail-JSON van mcp__Gmail__get_message of .eml) en geeft per controle
OK, FOUT, LET OP of N.V.T. met details. Wijzigt niets aan templates.

Controles (naam = sleutel in het rapport en het Slack-bericht):
  onderwerp      onderwerp aanwezig, geen em dash, geen placeholder
  preheader      verborgen preheader-tekst aanwezig en niet gelijk aan het onderwerp
  afzender       adres op siraatskitchen.com (alleen bij echte mails)
  grootte        HTML-part < 102 KB (Gmail knipt daarboven), let op vanaf 90 KB
  links          elke link volgen (Klaviyo-tracking via curl -sSIL --max-redirs 10, anders via de tekstversie) tot status 200
  utm            utm_source, utm_medium en utm_campaign op elke siraatskitchen.com-bestemming (ook binnen /discount/?redirect=)
  linktekst      ankertekst past bij de bestemming (ABOUT niet naar /faq, cart-knop naar cart/checkout, enz.)
  beelden        elk beeld laadt (200), heeft alt (lege alt alleen bij decoratie), gewicht per beeld en totaal
  tags           geen ongerenderde {{ / {% / [VRAAG / placeholder / YOUR ... TEXT / None
  markt          valuta, maat en verzendregel passend bij de markt van de alias (US, UK, AU, CA, SG, EU, XX)
  header-footer  vaste header- en footerpartial aanwezig, logo is de officiële lockup (zwart op licht, wit op donker)
  afmelden       unsubscribe- en voorkeurenlink aanwezig, echte tekst, bereikbaar
  em-dash        geen gedachtestreepje in onderwerp, preheader, tekst of alt
  layout         (browser) geen horizontaal scrollen op 375/600/1200 px, geen afgesneden of vervormde beelden
  dark-mode      (browser) prefers-color-scheme dark en geforceerde donkere modus: leesbaar, afmeldlink zichtbaar
"""
import os, re, json, csv, hashlib, subprocess, quopri, email, html as H
from email import policy
from urllib.parse import urlparse, parse_qs, unquote, urlencode, urlunparse
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
PARTIALS = os.path.join(ROOT, 'klaviyo', 'templates', 'partials')
LOCKUP_DIR = os.path.join(ROOT, 'brand', 'logo', 'lockup')
OK, FOUT, LETOP, NVT = 'OK', 'FOUT', 'LET OP', 'N.V.T.'
CHECKS = ['onderwerp', 'preheader', 'afzender', 'grootte', 'links', 'utm', 'linktekst', 'beelden', 'tags', 'markt',
          'header-footer', 'afmelden', 'em-dash', 'layout', 'dark-mode']
GMAIL_CLIP_KB = 102
SENDER_DOMAIN = 'siraatskitchen.com'
TRACK_HOSTS = re.compile(r'(^|\.)(klclick\d?\.com|klaviyomail\.com|kmail-lists\.com|klaviyo\.com)$')
SOCIAL = re.compile(r'facebook\.com|instagram\.com|tiktok\.com|trustpilot\.com|youtube\.com')
REAL_ADDRESS = "2803 Philadelphia Pike Suite B #1567, Claymont, DE 19703"

# Alias -> markt. Plus-adres lolagroothuis+<tag>@gmail.com. Een landcode in de tag wint (+uk-pan, +au, +us-set).
# +pan/+set/+schort zijn volgens OVERZICHT-V5 de US-checkouts, +int de internationale (land vooraf afspreken; standaard EU/NL).
ALIAS_MARKET = {'pan': 'US', 'set': 'US', 'schort': 'US', 'apron': 'US', 'int': 'EU'}
CC_MARKET = {'us': 'US', 'uk': 'UK', 'gb': 'UK', 'au': 'AU', 'ca': 'CA', 'sg': 'SG', 'eu': 'EU', 'nl': 'EU', 'de': 'EU', 'nz': 'NZ', 'xx': 'XX'}
SYMS = {'US': [r'(?<![A-Z])\$'], 'UK': ['£'], 'EU': ['€'], 'AU': [r'A\$'], 'CA': [r'C\$'], 'SG': [r'S\$'], 'NZ': [r'NZ\$']}

PLACEHOLDER = re.compile(r'\{\{|\{%|%\}|\}\}|\[VRAAG|placeholder|YOUR [A-Z ]{2,30} TEXT|lorem ipsum|\bTODO\b|\bTBD\b|\bXXX\b|'
                         r'\[address\]|\bNone\b|\bundefined\b|\bNaN\b|\[\[|\]\]|\{\{IMG\}\}|\{\{SHARED\}\}', re.I)
FILLER = '͏­‌​‍⁠﻿  ⁣'

# Ankertekst -> toegestane bestemming (regex op host+pad+query, gedecodeerd, incl. redirect-parameter).
# Alleen toegepast op korte ankers (<= 50 tekens); lange alt-teksten van beeldlinks bevatten te veel woorden.
ANCHOR_RULES = [
    (r'\babout\b|our story', r'/pages/(about|our-story)', FOUT),
    (r'\bfaq\b|questions', r'/pages/faq|/faq', FOUT),
    (r'lab result|test result|light labs|third.party', r'third-party-testing|lab', FOUT),
    (r'unsubscribe', r'unsubscribe|^#$|^#unsub', FOUT),
    (r'preferences', r'subscriptions/update|preferences|^#$|^#pref', FOUT),
    (r'view in (your )?browser|web ?view', r'web-view|^#$|^#webview|klclick', FOUT),
    (r'facebook', r'facebook\.com', FOUT), (r'instagram', r'instagram\.com', FOUT), (r'tiktok', r'tiktok\.com', FOUT),
    (r'trustpilot|leave a review|write a review|rate', r'trustpilot\.com|/pages/your-experience|review', FOUT),
    (r'return to (my )?cart|my cart|complete (my )?order|check ?out|finish (my )?order', r'/cart|/checkouts?\b|checkout|recover', FOUT),
    (r'accessor', r'/collections/accessor|/products/', LETOP),
    (r'bundles?|\bsets?\b', r'/collections/(bundles|sets)|set|bundle|/collections/', LETOP),
    (r'^(titanium )?cookware|\bpans\b', r'/collections/|/products/', LETOP),
    (r'\bpan\b', r'/products/|/collections/', LETOP),
    (r'apron', r'apron', LETOP), (r'\blid\b', r'lid', LETOP), (r'board', r'board', LETOP),
    (r'track (my )?order|order status', r'/account|/orders|track|status', LETOP),
]


# ------------------------------------------------------------------ invoer
def load(path, meta=None):
    """Leest een mail. .json = uitvoer van mcp__Gmail__get_message (FULL_CONTENT) of {html, subject, ...};
    .eml = ruwe MIME; .html = alleen HTML (meta via een .meta.json ernaast of het argument meta)."""
    m = {'path': path, 'html': '', 'plain': '', 'subject': None, 'sender': None, 'to': [], 'date': None, 'id': None, 'url': None, 'size_estimate': None}
    if path.endswith('.json'):
        d = json.load(open(path))
        if 'messages' in d and d['messages']: d = d['messages'][-1]
        m.update(html=d.get('htmlBody') or d.get('html') or '', plain=d.get('plaintextBody') or d.get('plain') or '',
                 subject=d.get('subject'), sender=d.get('sender'), to=d.get('toRecipients') or d.get('to') or [],
                 date=d.get('date'), id=d.get('id'), url=d.get('viewUrl'), size_estimate=d.get('sizeEstimate'))
    elif path.endswith('.eml'):
        msg = email.message_from_bytes(open(path, 'rb').read(), policy=policy.default)
        for part in msg.walk():
            ct = part.get_content_type()
            if ct == 'text/html' and not m['html']: m['html'] = part.get_content()
            elif ct == 'text/plain' and not m['plain']: m['plain'] = part.get_content()
        m.update(subject=str(msg['subject'] or ''), sender=email.utils.parseaddr(str(msg['from'] or ''))[1], to=[str(msg['to'] or '')], date=str(msg['date'] or ''))
    else:
        m['html'] = open(path, encoding='utf-8', errors='replace').read()
        side = path[:-5] + '.meta.json'
        if os.path.exists(side): m.update(json.load(open(side)))
    if meta: m.update({k: v for k, v in meta.items() if v is not None})
    if isinstance(m['to'], str): m['to'] = [m['to']]
    return m


def alias_of(to):
    for t in to or []:
        mm = re.search(r'lolagroothuis\+([\w.-]+)@', t or '', re.I)
        if mm: return mm.group(1).lower()
    return None


def market_of_alias(alias):
    if not alias: return None
    parts = re.split(r'[-_.]', alias)
    for p in parts:
        if p in CC_MARKET: return CC_MARKET[p]
    for p in parts:
        if p in ALIAS_MARKET: return ALIAS_MARKET[p]
    return None


# ------------------------------------------------------------------ html-hulp
def strip_comments(x):
    return re.sub(r'<!--(?!\[if).*?-->', '', x, flags=re.S)


def visible_text(x):
    x = re.sub(r'<head.*?</head>|<style.*?</style>|<script.*?</script>|<!--.*?-->', ' ', x, flags=re.S | re.I)
    x = _strip_hidden(x)
    t = H.unescape(re.sub(r'<[^>]+>', ' ', x))
    for c in FILLER: t = t.replace(c, ' ')
    return re.sub(r'\s+', ' ', t).strip()


def _strip_hidden(x):
    out = x
    for _ in range(40):
        mm = re.search(r'<(div|table|tr|td|span|p|a)\b[^>]*style="[^"]*display:\s*none[^"]*"[^>]*>', out, re.S | re.I)
        if not mm: break
        tag = mm.group(1); depth = 0; end = None
        for t in re.finditer(r'<(/?)%s\b[^>]*>' % tag, out[mm.start():], re.S | re.I):
            if t.group(0).endswith('/>'): continue
            depth += -1 if t.group(1) else 1
            if depth == 0: end = mm.start() + t.end(); break
        if end is None: break
        out = out[:mm.start()] + ' ' + out[end:]
    return out


def preheader(x):
    body = re.sub(r'^.*?<body[^>]*>', '', x, flags=re.S | re.I)
    mm = re.search(r'<(div|span)\b[^>]*style="[^"]*display:\s*none[^"]*"[^>]*>(.*?)</\1>', body[:6000], re.S | re.I)
    if not mm: return ''
    t = H.unescape(re.sub(r'<[^>]+>', ' ', mm.group(2)))
    for c in FILLER: t = t.replace(c, ' ')
    return re.sub(r'\s+', ' ', t).strip()


def links(x):
    """[(href, ankertekst, index)] in documentvolgorde. Ankertekst = zichtbare tekst, anders alt van het beeld."""
    out = []
    for i, mm in enumerate(re.finditer(r'<a\b([^>]*)>(.*?)</a>', x, re.S | re.I)):
        h = re.search(r'\bhref\s*=\s*"([^"]*)"', mm.group(1)) or re.search(r"\bhref\s*=\s*'([^']*)'", mm.group(1))
        if not h: continue
        href = H.unescape(h.group(1)).strip()
        t = re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', mm.group(2)))).strip()
        if not t:
            alt = re.search(r'\balt="([^"]*)"', mm.group(2)); t = H.unescape(alt.group(1)).strip() if alt else ''
        out.append((href, t, i))
    return out


def images(x):
    out = []
    for mm in re.finditer(r'<img\b[^>]*>', strip_comments(x), re.S | re.I):
        tag = mm.group(0); s = re.search(r'\bsrc="([^"]*)"', tag)
        if not s: continue
        alt = re.search(r'\balt="([^"]*)"', tag); w = re.search(r'\bwidth="(\d+)"', tag); hgt = re.search(r'\bheight="(\d+)"', tag)
        out.append({'src': H.unescape(s.group(1)), 'alt': H.unescape(alt.group(1)) if alt else None,
                    'w': int(w.group(1)) if w else None, 'h': int(hgt.group(1)) if hgt else None})
    return out


def is_pixel(im):
    return (im['w'] == 1 and im['h'] in (1, None)) or '/o/' in im['src'] and 'klclick' in im['src']


def decoded(u):
    """URL plus gedecodeerde redirect-parameter (Shopify /discount/CODE?redirect=/pad%3Futm_...)."""
    u = H.unescape(u); x = u
    try:
        q = parse_qs(urlparse(u).query)
        for k in ('redirect', 'return_to', 'url'):
            if k in q: x += ' ' + unquote(q[k][0])
    except Exception: pass
    return unquote(x)


def strip_utm(u):
    p = urlparse(u); q = [(k, v) for k, v in [kv.split('=', 1) if '=' in kv else (kv, '') for kv in p.query.split('&') if kv] if not k.startswith('utm_')]
    return urlunparse(p._replace(query='&'.join('%s=%s' % kv for kv in q)))


def is_sample(u):
    """URL uit een testevent (research/tailoring/test/samples): bestaat niet in de shop, dus geen linkfout."""
    return bool(re.search(r'/checkouts/sample/|/products/x(?:$|[?&#%]|\b)', decoded(u)))


def is_tracking(u):
    try: return bool(TRACK_HOSTS.search(urlparse(u).netloc.lower())) and 'subscriptions/' not in u
    except Exception: return False


# ------------------------------------------------------------------ netwerk
_NET = {}
def curl(u, head=False):
    """(status, eind-URL, redirects, bytes). status 0 = niet bereikbaar vanuit deze omgeving (proxy/egress)."""
    key = (u, head)
    if key in _NET: return _NET[key]
    if u.startswith('file://') or u.startswith('/'):
        p = unquote(u[7:]) if u.startswith('file://') else u; p = p.split('?')[0]; r = (200, u, 0, os.path.getsize(p)) if os.path.exists(p) else (404, u, 0, 0)
        _NET[key] = r; return r
    cmd = ['curl', '-sS', '-L', '--max-redirs', '10', '-o', '/dev/null', '--max-time', '25', '-A',
           'Mozilla/5.0 (Siraat inbox-QA)', '-w', '%{http_code} %{num_redirects} %{size_download} %{url_effective}']
    if head: cmd.insert(1, '-I')
    try:
        o = subprocess.run(cmd + [u], capture_output=True, text=True, timeout=40).stdout.strip().split(' ', 3)
        r = (int(o[0]), o[3] if len(o) > 3 else u, int(o[1]), int(float(o[2])))
    except Exception:
        r = (0, u, 0, 0)
    if r[0] in (429, 500, 502, 503, 504):   # Shopify knijpt bij veel verzoeken: twee keer opnieuw
        import time
        for wait in (3, 8):
            time.sleep(wait)
            o = subprocess.run(cmd + [u], capture_output=True, text=True, timeout=40).stdout.strip().split(' ', 3)
            try: r = (int(o[0]), o[3] if len(o) > 3 else u, int(o[1]), int(float(o[2])))
            except Exception: pass
            if r[0] not in (429, 500, 502, 503, 504): break
    if head and r[0] in (403, 405, 400): r = curl(u, head=False)
    _NET[key] = r; return r


def prefetch(urls, head=False):
    urls = sorted({u for u in urls if u and (u, head) not in _NET})
    with ThreadPoolExecutor(4) as ex: list(ex.map(lambda u: curl(u, head), urls))


def plain_links(plain):
    """[(tekst, url)] uit Klaviyo's tekstversie: markdown [tekst](url) of 'tekst (url)'."""
    out = [(re.sub(r'\s+', ' ', t).strip(), u) for t, u in re.findall(r'\[([^\]]*)\]\((https?://[^)\s]+)\)', plain or '')]
    if not out: out = [(re.sub(r'\s+', ' ', t).strip(), u) for t, u in re.findall(r'([^\n()]{2,80}?)\s*\((https?://[^)\s]+)\)', plain or '')]
    return out


def _norm(t): return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()


# ------------------------------------------------------------------ lockup
_LOCK = None
def lockups():
    global _LOCK
    if _LOCK is None:
        _LOCK = {}
        for f in os.listdir(LOCKUP_DIR):
            if f.endswith('.png'): _LOCK[hashlib.md5(open(os.path.join(LOCKUP_DIR, f), 'rb').read()).hexdigest()] = f
    return _LOCK


def file_md5(src):
    if src.startswith('file://'):
        p = unquote(src[7:]); return hashlib.md5(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    try:
        b = subprocess.run(['curl', '-sS', '-L', '--max-time', '20', src], capture_output=True, timeout=30).stdout
        return hashlib.md5(b).hexdigest() if b else None
    except Exception: return None


def partial_tokens():
    """Vaste ankerteksten uit header.html en footer.html (zo blijft de check gelijk met de partials)."""
    toks = {}
    for nm in ('header', 'footer'):
        x = open(os.path.join(PARTIALS, nm + '.html')).read()
        ts = [re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', '', t))).replace('→', '').strip() for t in re.findall(r'<a\b[^>]*>(.*?)</a>', x, re.S)]
        ts = [t for t in ts if t and '{' not in t]
        if nm == 'footer': ts += ['NON-TOXIC COOKWARE', 'BUILT FOR LIFE']
        toks[nm] = ts
    return toks


# ------------------------------------------------------------------ controles
def R(status, detail=''): return {'status': status, 'detail': detail}


def run_checks(m, market=None, kind='mail', raw=None, browser=None, skip_net=False):
    """m: dict uit load() (of een template-render met html/subject/preheader). kind: 'mail' (echte ontvangen mail) of 'template'.
    raw: Klaviyo-versie met Django-tags (template-modus, voor afmeldtags). browser: resultaat van qa_mail_shots.js voor deze mail.
    Geeft {check: {'status', 'detail'}} plus '_links' en '_images' met de ruwe meetgegevens."""
    x = m['html']; out = {}
    vis = visible_text(x)
    subj = (m.get('subject') or '').strip(); pre = (m.get('preheader') or preheader(x) or '').strip()
    # onderwerp
    if not subj: out['onderwerp'] = R(FOUT, 'geen onderwerp')
    elif PLACEHOLDER.search(subj): out['onderwerp'] = R(FOUT, 'placeholder in onderwerp: "%s"' % subj)
    else: out['onderwerp'] = R(OK if len(subj) <= 70 else LETOP, '"%s"%s' % (subj, '' if len(subj) <= 70 else ' (%d tekens, mobiel knipt na ~40)' % len(subj)))
    # preheader
    if not pre: out['preheader'] = R(FOUT, 'geen preheader (Gmail toont dan de eerste tekst uit de mail)')
    elif _norm(pre) == _norm(subj): out['preheader'] = R(LETOP, 'preheader gelijk aan onderwerp')
    elif PLACEHOLDER.search(pre): out['preheader'] = R(FOUT, 'placeholder in preheader: "%s"' % pre[:90])
    else: out['preheader'] = R(OK, '"%s"' % pre[:110])
    # afzender
    if kind != 'mail': out['afzender'] = R(NVT, 'flow-instelling in Klaviyo, niet in de template')
    else:
        s = (m.get('sender') or '').lower()
        out['afzender'] = R(OK, s) if s.endswith('@' + SENDER_DOMAIN) else R(FOUT, 'afzender %s is niet @%s' % (s or '(leeg)', SENDER_DOMAIN))
    # grootte
    b = x.encode('utf-8'); qp = len(quopri.encodestring(b)) / 1024; rawkb = len(b) / 1024
    est = qp
    if kind != 'mail':   # template: Klaviyo vervangt elke href door een tracking-URL van ~90 tekens (ctrk.klclick1.com/l/<id>_<n>)
        est = qp + sum(1 for l in links(x) if l[0].startswith('http')) * 0.09 + 0.5
    det = '%.1f KB HTML (%.1f KB quoted-printable%s)' % (rawkb, qp, '' if kind == 'mail' else ', na tracking ~%.0f KB' % est)
    out['grootte'] = R(FOUT if est > GMAIL_CLIP_KB else (LETOP if est > 90 else OK), det)
    # links
    L = links(x); pl = plain_links(m.get('plain')); pool = {}
    for t, u in pl: pool.setdefault(_norm(t), []).append(u)
    order = [u for t, u in pl]
    rows = []; blocked = 0
    track_urls = [h for h, t, i in L if h.startswith('http') and is_tracking(h)]
    if not skip_net: prefetch(track_urls, head=True)
    ti = 0
    for href, txt, i in L:
        row = {'href': href, 'text': txt[:80], 'dest': None, 'status': None, 'via': None, 'final': None}
        if href.startswith('mailto:') or href.startswith('tel:'): row.update(dest=href, status=200, via='mailto'); rows.append(row); continue
        if href in ('#', '') or href.startswith('#'):
            row.update(dest=href, via='tag'); rows.append(row); continue
        if is_tracking(href):
            st, fin, nr, _ = (0, href, 0, 0) if skip_net else curl(href, head=True)
            if st:
                row.update(dest=fin, via='redirect (%d)' % nr)
            else:
                blocked += 1
                cand = pool.get(_norm(txt)) or []
                if cand: row.update(dest=cand.pop(0), via='tekstversie (anker)')
                else:
                    mm = re.search(r'_(\d+)$', href)
                    if mm and int(mm.group(1)) < len(order): row.update(dest=order[int(mm.group(1))], via='tekstversie (volgorde, onzeker)')
                    else: row.update(dest=None, via='tracking niet te volgen')
            ti += 1
        else:
            row.update(dest=href, via='direct')
        rows.append(row)
    dests = [r['dest'] for r in rows if r['dest'] and r['dest'].startswith('http') and not is_sample(r['dest'])]
    if not skip_net: prefetch([strip_utm(d) for d in dests])
    bad = []; unknown = []; social = []
    for r in rows:
        d = r['dest']
        if not d or not d.startswith('http'):
            if r['via'] == 'tracking niet te volgen': unknown.append(r['text'] or r['href'][:60])
            continue
        if is_sample(d): r['status'] = 'voorbeeld'; continue
        if skip_net: continue
        st, fin, nr, _ = curl(strip_utm(d)); r['status'] = st; r['final'] = fin
        if st == 429: unknown.append('%s (rate limit van de shop, later opnieuw)' % r['text'][:30]); continue
        if st == 0:
            (social if SOCIAL.search(urlparse(d).netloc) else unknown).append('%s (%s)' % (r['text'][:30], urlparse(d).netloc))
        elif st != 200: bad.append('"%s" -> %s geeft %d' % (r['text'][:40], d[:90], st))
        elif urlparse(fin).path.rstrip('/') in ('', '/') and urlparse(d).path.strip('/') not in ('',) and 'siraatskitchen' in fin and not urlparse(d).path.startswith('/discount'):
            bad.append('"%s" -> %s komt uit op de homepage' % (r['text'][:40], d[:90]))
    det = '%d links, %d unieke bestemmingen' % (len(rows), len({strip_utm(d) for d in dests}))
    if blocked: det += '; %d Klaviyo-trackinglinks niet te volgen vanuit deze omgeving (egress), bestemming uit de tekstversie' % blocked
    if social: det += '; sociale links niet te openen vanuit deze omgeving: ' + ', '.join(sorted(set(social)))
    if bad: out['links'] = R(FOUT, det + '. ' + '; '.join(bad[:8]))
    elif unknown: out['links'] = R(LETOP, det + '. Niet gecontroleerd: ' + ', '.join(sorted(set(unknown))[:8]))
    else: out['links'] = R(OK if not skip_net else NVT, det)
    # utm
    miss = []
    for r in rows:
        d = r['dest']
        if not d or not d.startswith('http') or 'siraatskitchen.com' not in urlparse(d).netloc: continue
        dd = decoded(d)
        need = [k for k in ('utm_source', 'utm_medium', 'utm_campaign') if k + '=' not in dd]
        if need: miss.append('"%s" (%s) mist %s' % (r['text'][:35], urlparse(d).path[:40] or '/', ','.join(need)))
    shop = [r for r in rows if r['dest'] and 'siraatskitchen.com' in (urlparse(r['dest']).netloc if r['dest'].startswith('http') else '')]
    if not shop: out['utm'] = R(NVT, 'geen links naar siraatskitchen.com')
    elif miss: out['utm'] = R(FOUT if len(miss) == len(shop) else LETOP, '%d van %d shoplinks zonder UTM: %s' % (len(miss), len(shop), '; '.join(miss[:6])))
    else: out['utm'] = R(OK, '%d shoplinks met UTM' % len(shop))
    # linktekst
    mism = []; worst = OK
    for r in rows:
        t = (r['text'] or '').strip(); d = r['dest'] or r['href']
        if not t or len(t) > 50 or not d: continue
        tl = t.lower(); dd = decoded(d).lower()
        for pat, ok_pat, sev in ANCHOR_RULES:
            if re.search(pat, tl):
                if not re.search(ok_pat, dd):
                    mism.append('[%s] "%s" -> %s' % (sev, t[:40], (urlparse(d).path or d)[:60] if d.startswith('http') else d[:40]))
                    if sev == FOUT: worst = FOUT
                    elif worst == OK: worst = LETOP
                break
    out['linktekst'] = R(worst, '; '.join(sorted(set(mism))[:10]) if mism else 'ankerteksten passen bij hun bestemming')
    # beelden
    ims = [im for im in images(x) if not is_pixel(im)]
    if not skip_net: prefetch([im['src'] for im in ims if im['src'].startswith('http')])
    bad = []; noalt = []; heavy = []; total = 0; seen = set()
    for im in ims:
        st, _, _, size = curl(im['src']) if (not skip_net or im['src'].startswith('file://')) else (None, 0, 0, 0)
        if st is not None and st != 200: bad.append('%s (%s)' % (os.path.basename(urlparse(im['src']).path)[:40], st or 'niet bereikbaar'))
        if im['src'] not in seen: total += size or 0; seen.add(im['src'])
        if im['alt'] is None: noalt.append(os.path.basename(urlparse(im['src']).path)[:40])
        if size and size > 300 * 1024: heavy.append('%s %d KB' % (os.path.basename(urlparse(im['src']).path)[:40], size // 1024))
    det = '%d beelden, %d KB totaal' % (len(ims), total // 1024)
    if heavy: det += '; zwaar (>300 KB): ' + ', '.join(heavy[:5])
    if noalt: det += '; zonder alt: ' + ', '.join(noalt[:5])
    if bad: det += '; laadt niet: ' + ', '.join(bad[:6])
    out['beelden'] = R(FOUT if bad or noalt else (LETOP if heavy or total > 1536 * 1024 else OK), det)
    # tags en placeholders (zichtbare tekst, alt, href, src)
    hits = []
    for mm in PLACEHOLDER.finditer(vis): hits.append(vis[max(0, mm.start() - 25):mm.end() + 25])
    for im in ims:
        if im['alt'] and PLACEHOLDER.search(im['alt']): hits.append('alt: ' + im['alt'][:60])
        if PLACEHOLDER.search(im['src']): hits.append('src: ' + im['src'][-60:])
    for href, t, i in L:
        if re.search(r'\{\{|\{%|%7B%7B|%7B%25|\[\[', href): hits.append('href: ' + href[:70])
    out['tags'] = R(FOUT, '; '.join('"%s"' % h for h in hits[:6])) if hits else R(OK, 'geen ongerenderde tags of placeholders')
    # markt
    out['markt'] = market_check(vis + ' ' + ' '.join(im['alt'] or '' for im in ims), market)
    # header en footer
    out['header-footer'] = header_footer(x, vis, ims, L, skip_net)
    # afmelden
    out['afmelden'] = unsub_check(x, L, rows, raw, kind, skip_net, browser)
    # em dash
    ed = []
    for nm, s in (('onderwerp', subj), ('preheader', pre), ('tekst', vis)):
        for mm in re.finditer('—', s or ''): ed.append('%s: "%s"' % (nm, s[max(0, mm.start() - 30):mm.end() + 20].strip()))
    for im in ims:
        if '—' in (im['alt'] or ''): ed.append('alt: "%s"' % im['alt'][:60])
    out['em-dash'] = R(FOUT, '%d keer; %s' % (len(ed), '; '.join(ed[:4]))) if ed else R(OK, 'geen em dash')
    # layout en dark mode (browser)
    out['layout'], out['dark-mode'] = browser_checks(browser)
    out['_links'] = rows; out['_images'] = ims
    return out


def market_check(text, market):
    if not market: return R(NVT, 'markt onbekend (geef --market of gebruik een alias als +uk-pan)')
    F = []; W = []
    t = text
    for mk, pats in SYMS.items():
        if mk == market: continue
        for p in pats:
            for mm in re.finditer(p + r'\s?\d', t):
                if mk == 'US' and re.match(r'[ACSNZ]', t[max(0, mm.start() - 2):mm.start()][-1:] or ' '): continue
                F.append('%s-bedrag in een %s-mail: "%s"' % (mk, market, t[max(0, mm.start() - 25):mm.end() + 8].strip()))
    if market == 'US':
        for mm in re.finditer(r'(?<![(\d])(?<!\(\d)(?<!\(\d\d)\d+\s?cm\b(?!\s*\()(?!\))', t):   # "11″ (28 cm)" mag
            W.append('cm in een US-mail: "%s"' % t[max(0, mm.start() - 20):mm.end() + 5].strip())
        if re.search(r'duties paid', t, re.I): W.append('"duties paid" in een US-mail')
    else:
        if re.search(r'from the US\b', t): F.append('"Free shipping from the US" in een %s-mail' % market)
        for mm in re.finditer(r'\d(?:\.\d)?\s?(?:″|”|"|-inch\b| inch\b)', t):
            if market != 'XX': F.append('inch in een %s-mail: "%s"' % (market, t[max(0, mm.start() - 20):mm.end() + 5].strip()))
        for w in ('12-piece', '12-Piece', 'Roasting Pan', 'roasting pan', 'stockpot', 'saucepan'):
            if w in t: F.append('US-only product in een %s-mail: %s' % (market, w))
    syms = [p for p in SYMS.get(market, [])]
    has_own = any(re.search(p + r'\s?\d', t) for p in syms)
    det = 'markt %s%s' % (market, '' if has_own or market == 'XX' else ' (geen bedrag in eigen valuta gezien)')
    if F: return R(FOUT, det + '. ' + '; '.join(sorted(set(F))[:6]))
    if W: return R(LETOP, det + '. ' + '; '.join(sorted(set(W))[:4]))
    return R(OK, det)


def header_footer(x, vis, ims, L, skip_net):
    toks = partial_tokens(); up = vis.upper(); anchors = {(_norm(t)) for h, t, i in L}
    miss = {nm: [t for t in ts if _norm(t) not in anchors and t.upper() not in up] for nm, ts in toks.items()}
    logos = [im for im in ims if re.search(r'logo|lockup', im['src'], re.I) or (im['alt'] or '').strip().lower() in ('siraat', "siraat's kitchen", 'siraat logo')]
    lk = lockups(); probs = []
    if not logos: probs.append('geen logo gevonden')
    else:
        names = []
        for im in logos:
            h = file_md5(im['src']) if (not skip_net or im['src'].startswith('file://')) else None
            names.append(lk.get(h, '?' if h is None else 'GEEN lockup'))
        if any(n == 'GEEN lockup' for n in names): probs.append('logo is niet de officiële lockup: ' + ', '.join(os.path.basename(urlparse(i['src']).path) for i, n in zip(logos, names) if n == 'GEEN lockup'))
        if names and 'black' not in names[0] and names[0] not in ('?',): probs.append('headerlogo is niet de zwarte lockup (%s)' % names[0])
        if len(names) > 1 and 'white' not in names[-1] and names[-1] not in ('?',): probs.append('footerlogo is niet de witte lockup (%s)' % names[-1])
    if miss['header']: probs.append('header mist: ' + ', '.join(miss['header']))
    if miss['footer']: probs.append('footer mist: ' + ', '.join(miss['footer']))
    if probs: return R(FOUT, '; '.join(probs))
    return R(OK, 'header en footer uit de partials, logo = lockup (%d)' % len(logos))


def unsub_check(x, L, rows, raw, kind, skip_net, browser):
    probs = []; info = []
    if kind != 'mail':
        k = raw or x
        if not re.search(r'\{%\s*unsubscribe', k): probs.append('geen {% unsubscribe %}')
        if not re.search(r'\{%\s*manage_preferences', k): probs.append('geen {% manage_preferences(_link) %}')
        info.append('Klaviyo-tags aanwezig' if not probs else '')
    else:
        un = [(h, t) for h, t, i in L if 'unsubscribe' in h.lower() or re.search(r'unsubscribe', t, re.I)]
        pr = [(h, t) for h, t, i in L if 'subscriptions/update' in h or re.search(r'preferences', t, re.I)]
        if not un: probs.append('geen afmeldlink')
        if not pr: probs.append('geen voorkeurenlink')
        for h, t in un + pr:
            if PLACEHOLDER.search(t) or not t.strip(): probs.append('linktekst is placeholder of leeg: "%s"' % t)
        for h, t in un + pr:
            if not h.startswith('http') or skip_net: continue
            st = curl(h)[0]
            if st == 0: info.append('%s niet te openen vanuit deze omgeving (egress), handmatig klikken' % urlparse(h).netloc)
            elif st >= 400: probs.append('"%s" geeft %d' % (t[:30], st))
    if browser:
        low = [c for c in browser.get('unsubContrast', []) if c['ratio'] < 3]
        if low: probs.append('afmeldlink nauwelijks zichtbaar: ' + ', '.join('"%s" %.1f:1 (%s op %s, %s)' % (c['t'][:25], c['ratio'], c['fg'], c['bg'], c['mode']) for c in low[:3]))
    if probs: return R(FOUT, '; '.join(probs))
    return R(LETOP if info and kind == 'mail' else OK, '; '.join(sorted(set(i for i in info if i))) or 'afmeld- en voorkeurenlink aanwezig')


def browser_checks(b):
    if not b: return R(NVT, 'geen browsermeting'), R(NVT, 'geen browsermeting')
    lay = []; dm = []
    for job in b.get('jobs', []):
        tag = '%s %d px' % (job['mode'], job['width'])
        if job.get('error'): lay.append('%s: %s' % (tag, job['error'][:80])); continue
        if job['scrollWidth'] > job['vw'] + 1: lay.append('%s: horizontaal scrollen (%d > %d)' % (tag, job['scrollWidth'], job['vw']))
        for c in job.get('cut', [])[:3]: lay.append('%s: %s' % (tag, c))
        for c in job.get('broken', [])[:3]: lay.append('%s: beeld laadt niet %s' % (tag, c))
        if job['mode'] != 'light':
            for c in job.get('lowContrast', [])[:2]: dm.append('%s: tekst met laag contrast "%s" %.1f:1' % (tag, c['t'][:30], c['ratio']))
        if job['mode'] != 'light' and job.get('shot') and os.path.exists(job['shot']):
            for issue in shot_dark_issues(job['shot'], job.get('imgRects', [])): dm.append('%s: %s' % (tag, issue))
    lay = sorted(set(lay), key=lay.index); dm = sorted(set(dm), key=dm.index)
    widths = sorted({j['width'] for j in b.get('jobs', [])})
    L = R(FOUT, '; '.join(lay[:6])) if lay else R(OK, 'geen horizontaal scrollen of afgesneden beelden op %s px' % '/'.join(map(str, widths)))
    hard = [x for x in dm if 'logo' in x and 'onzichtbaar' in x]
    D = R(FOUT if hard else LETOP, '; '.join(dm[:5])) if dm else R(OK, 'leesbaar in prefers-color-scheme dark en geforceerde donkere modus')
    return L, D


def _lum(p): return (0.2126 * p[0] + 0.7152 * p[1] + 0.0722 * p[2]) / 255


def shot_dark_issues(shot, rects):
    """Pixelcontrole op een screenshot in donkere modus: is het logo nog te zien, en staan er lichte blokken (beeld met witte
    achtergrond) op een donkere pagina? Werkt ook voor geforceerde donkere modus, waar de DOM-kleuren niet veranderen."""
    try:
        from PIL import Image
        im = Image.open(shot).convert('RGB')
    except Exception: return []
    out = []; blocks = []; W, Hh = im.size
    for r in rects:
        x0, y0, x1, y1 = max(0, r['x']), max(0, r['y']), min(W, r['x'] + r['w']), min(Hh, r['y'] + r['h'])
        if x1 - x0 < 10 or y1 - y0 < 10: continue
        crop = im.crop((x0, y0, x1, y1)); crop.thumbnail((200, 200)); px = list(crop.getdata()); L = sorted(_lum(p) for p in px)
        if r['logo']:
            lo, hi = L[len(L) // 20], L[-len(L) // 20 - 1]
            cr = (hi + 0.05) / (lo + 0.05)
            if cr < 3: out.append('logo %s onzichtbaar (contrast %.1f:1 tussen logo en achtergrond)' % (r['name'], cr))
            continue
        cw, ch = crop.size
        edge = [crop.getpixel((i, 0)) for i in range(cw)] + [crop.getpixel((i, ch - 1)) for i in range(cw)] + [crop.getpixel((0, j)) for j in range(ch)] + [crop.getpixel((cw - 1, j)) for j in range(ch)]
        el = sum(_lum(p) for p in edge) / len(edge)
        ring = [im.getpixel((max(0, x0 - 6), min(Hh - 1, (y0 + y1) // 2))), im.getpixel((min(W - 1, x1 + 5), min(Hh - 1, (y0 + y1) // 2)))]
        if el > 0.85 and sum(_lum(p) for p in ring) / 2 < 0.25: blocks.append(r['name'])
    if blocks: out.append('lichte blokken op donkere achtergrond (beeld met witte rand): %s%s' % (', '.join(blocks[:4]), ' (+%d)' % (len(blocks) - 4) if len(blocks) > 4 else ''))
    return out


def summary(res):
    c = {OK: 0, FOUT: 0, LETOP: 0, NVT: 0}
    for k in CHECKS:
        if k in res: c[res[k]['status']] += 1
    return c
