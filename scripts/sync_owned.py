"""Nachtelijke sync: wat bezit een klant? Shopify-orders (via Klaviyo-events) naar profielvelden.

Besluit 8 okt 2026 (DECISIONS.md): het script `siraat_owned` mag, dagelijks draaien en controleren.
Handleiding: research/v5/07-sync-owned.md

Gebruik (altijd vanuit /tmp, met python3 -I):
  python3 -I scripts/sync_owned.py                         dry-run: incrementeel sinds de cursor (eerste keer: volledige historie)
  python3 -I scripts/sync_owned.py --since=2026-09-08      dry-run vanaf een datum
  python3 -I scripts/sync_owned.py --live                  schrijven (bulk import), cursor en ledger bijwerken
  python3 -I scripts/sync_owned.py --live --limit=50       proef: maximaal 50 profielen schrijven (PATCH), daarna GET-controle
  python3 -I scripts/sync_owned.py --check                 controle: exit 1 als de laatste geslaagde live run ouder is dan 36 uur
Opties: --examples=N (aantal voorbeelden in dry-run, standaard 20), --bulk / --patch (schrijfmethode forceren).

Bron: Klaviyo-events van de Shopify-integratie
  Placed Order   RSNxYV  (regels met handle, titel, variant, line_item_id)
  Cancelled Order TFervq (hele order vervalt)
  Refunded Order Xg6cwn  (volledig terugbetaald: order vervalt; deels: terugbetaalde regels vervallen)
Schrijft per profiel alleen: siraat_owned, siraat_owned_cats, siraat_first_order_at, siraat_last_order_at, siraat_orders.
Geen consent, geen andere velden.

Staat: exports/live/sync_owned_state.json (cursor, laatste runs) en exports/live/sync_owned_ledger.json.gz
(per order: profiel, datum, regels met sleutels, status). Zonder volledige ledger (vóór de eerste volledige run)
haalt het script voor elk te schrijven profiel eerst diens volledige orderhistorie op, zodat de velden kloppen.
"""
import sys, os, re, json, gzip, time, subprocess, urllib.parse, datetime as DT, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
LIVEDIR = os.path.join(ROOT, 'exports', 'live')
STATE = os.path.join(LIVEDIR, 'sync_owned_state.json')
LEDGER = os.environ.get('SYNC_OWNED_LEDGER') or os.path.join(LIVEDIR, 'sync_owned_ledger.json.gz')  # bevat profiel-ID's: in .gitignore
M_PLACED, M_CANCEL, M_REFUND = 'RSNxYV', 'TFervq', 'Xg6cwn'
OVERLAP_H = 48           # incrementeel: zoveel uur terug vanaf de cursor (late events), ledger ontdubbelt
MAX_AGE_H = 36           # --check
API = 'https://a.klaviyo.com'

OPT = {a.split('=', 1)[0]: (a.split('=', 1)[1] if '=' in a else '1') for a in sys.argv[1:] if a.startswith('--')}
LIVE = '--live' in OPT
LIMIT = int(OPT['--limit']) if '--limit' in OPT else None
SINCE = OPT.get('--since')
NEX = int(OPT.get('--examples', 20))

# ---------------------------------------------------------------- mapping
# Sleutels en categorie. 'panpro' en 'lid' zijn verzamelsleutels (komen er altijd bij naast de maat).
CAT = {}
for k in ('panpro', 'panpro_mini', 'panpro_small', 'panpro_standard', 'panpro_large', 'pan_original',
          'deep', 'wok', 'crepe', 'roasting'):
    CAT[k] = 'pan'
for k in ('set6', 'set12', 'complete', 'everything'):
    CAT[k] = 'set'
for k in ('pot_2l', 'pot_3l', 'pot_75l'):
    CAT[k] = 'pot'
SIZE_CM = {'mini': 20, 'small': 26, 'standard': 28, 'large': 30}
UTENSILS = ['utensil_flipper', 'utensil_spatula', 'utensil_ladle', 'utensil_scooper']

def pan(size): return ['panpro', 'panpro_' + size] if size else ['panpro']
def lid(size): return ['lid', 'lid_%d' % SIZE_CM[size]] if size else ['lid']

# Bundels uitgepakt volgens content/catalog/products.json ("whats_in_the_box"). bundle=True geeft categorie 'set'.
SET6 = ['set6'] + pan('mini') + pan('small') + pan('large') + lid('mini') + lid('small') + lid('large')
SET12 = ['set12'] + SET6[1:] + ['pot_2l', 'pot_3l', 'pot_75l']
BUNDLES = [  # (regex op titel+handle, sleutels); volgorde = prioriteit
    (r'just everything|34-pcs', ['everything'] + SET12[1:] + ['set12', 'roasting', 'wok', 'deep', 'crepe', 'pizza',
        'board', 'utensils'] + UTENSILS + ['pizza_wheel', 'grill_press', 'trivet', 'mill', 'apron']),
    (r'cookware set pro|cookware-set-pro', pan('standard') + ['wok', 'deep', 'utensil_flipper', 'utensil_ladle']),
    (r'12 ?-?pcs|hammered cookware set\b|hammered-cookware-set$', SET12),
    (r'pot set|pot-set', ['pot_2l', 'pot_3l', 'pot_75l']),
    (r'pan set with lids|pan-set-with-lids', SET6),
    (r'complete edition|hammered-collection', ['complete'] + pan('standard') + ['wok', 'deep', 'crepe']),
    (r'full hammered pro edition|full-hammered-pro', pan('mini') + pan('small') + pan('standard') + pan('large')
        + lid('mini') + lid('small') + lid('standard') + lid('large') + ['utensils'] + UTENSILS),
    (r'2 pans \+ 2 lids|2-pans-and-2-lids', pan('mini') + pan('standard') + lid('mini') + lid('standard')),
    (r'pan pro duo|pan-pro-duo', pan('mini') + pan('standard')),
    (r'hammered pro duo|titanium-pro-duo', pan('standard') + ['utensil_flipper']),
    (r'pan pro kit|pan-pro-kit', pan('small') + lid('small') + ['utensil_flipper']),
    (r'cook & prep|prep-cook', pan('standard') + ['board']),
    (r'pan pro & utensil|pan-pro-utensil', pan('standard') + ['utensils'] + UTENSILS),
    (r'wok & deep|wok-deep', ['wok', 'deep']),
]
IGNORE = r'mystery gift|e-guide|e-book|ebook|\bguide\b|giveaway|weekly draw|win your order|free shipping|' \
         r'shipping protection|shipping-insurance|gift card|e-gift'
SIMPLE = [  # (regex, sleutel)
    (r'salt|pepper|\bmill\b', 'mill'), (r'apron', 'apron'), (r'pizza wheel|pizza-wheel', 'pizza_wheel'),
    (r'pizza', 'pizza'), (r'roasting', 'roasting'), (r'cr[eê]pe', 'crepe'), (r'\bwok\b', 'wok'),
    (r'deep pan|deep-pan', 'deep'), (r'diatomite', 'diatomite_mat'), (r'non[- ]slip mat', 'mat'),
    (r'cutting board|snijplank|prep board|cutting-board', 'board'), (r'bottle', 'bottle'), (r'ice cube', 'ice_cubes'),
    (r'straw', 'straws'), (r'trivet', 'trivet'), (r'sharpener', 'sharpener'), (r'chopstick', 'chopsticks'),
    (r'grill press', 'grill_press'), (r'\btote\b', 'tote'), (r'tea filter', 'tea_filter'),
    (r'dishwasher|detergent|sheets', 'sheets'),
]

def size_of(s):
    """Pan Pro/deksel-maat uit tekst: cm, woorden, inches. None als onbekend."""
    s = s.lower()
    m = re.search(r'(\d{2})\s*cm', s)
    if m:
        return {20: 'mini', 26: 'small', 28: 'standard', 30: 'large'}.get(int(m.group(1)))
    for w, k in (('mini', 'mini'), ('small', 'small'), ('medium', 'small'), ('standard', 'standard'),
                 ('standrd', 'standard'), ('large', 'large')):
        if re.search(r'\b' + w + r'\b', s):
            return k
    m = re.search(r'(\d{1,2}(?:[.,]\d)?)\s*(?:"|″|”|in\b)', s)
    if m:
        v = float(m.group(1).replace(',', '.'))
        return 'mini' if v < 9 else 'small' if v < 10.6 else 'standard' if v < 11.4 else 'large'
    return None

def classify(title, variant, handle):
    """-> (sleutels, bundel?) ; ([], False) voor te negeren regels ; None als onbekend."""
    t = ('%s | %s' % (title or '', handle or '')).lower()
    v = (variant or '').lower()
    if v in ('default title', 'none', 'free'):
        v = ''
    if re.search(IGNORE, t):
        return [], False
    for rx, keys in BUNDLES:
        if re.search(rx, t):
            if 'pizza steel' in t:  # bv. "Cookware Set | 12-Pcs | + FREE PIZZA STEEL"
                keys = keys + ['pizza']
            return sorted(set(keys)), True
    if re.search(r'pot with lid|saucepan|stockpot|litre|-qt|\bqt\b', t):
        if re.search(r'7[,.-]?5|8-qt|8 qt', t): return ['pot_75l'], False
        if re.search(r'\b3[ -]litre|3-qt|3 qt|^3-', t): return ['pot_3l'], False
        if re.search(r'\b2[ -]litre|2-qt|2 qt|^2-', t): return ['pot_2l'], False
        return None
    if re.search(r'utensil', t):
        if re.search(r'bundle|set', t) or not v:
            return ['utensils'] + UTENSILS, False
        for u in ('flipper', 'spatula', 'ladle', 'scooper'):
            if u in v: return ['utensil_' + u], False
        return None
    if re.search(r'\bgift\b', (title or '').lower()):  # fysieke cadeaus met een variant (bv. "Birthday Sale Gift | Spatula")
        for u in ('flipper', 'spatula', 'ladle', 'scooper'):
            if u in v: return ['utensil_' + u], False
        return [], False
    if re.search(r'\blid\b', t) and not re.search(r'with lid|incl-lid|with-lid', t):
        return lid(size_of(v) or size_of(t)), False
    for rx, k in SIMPLE:
        if re.search(rx, t):
            return [k], False
    if 'hammered' not in t and re.search(r'titanium pan|pure titanium pan', t):
        return ['pan_original'], False  # eerste, niet-gehamerde pan (24/26/28 cm)
    if re.search(r'hammered|pan pro|frying pan', t):
        keys = pan(size_of(v) or size_of(t))
        if re.search(r'with lid|incl-lid|with-lid', t):
            keys += lid(size_of(v) or size_of(t))
        return sorted(set(keys)), False
    return None

def cats_of(keys, bundle):
    c = {CAT.get(k, 'accessory') for k in keys}
    if bundle:
        c.add('set')
    return sorted(c)

# ---------------------------------------------------------------- API
def api(method, url, body=None):
    if url.startswith('/'):
        url = API + url
    cmd = ['curl', '-sS', '-w', '\n%{http_code}', '-X', method, url, '-H', 'revision: 2025-10-15',
           '-H', 'accept: application/vnd.api+json']
    if os.environ.get('KLAVIYO_API_KEY'):
        cmd += ['-H', 'Authorization: Klaviyo-API-Key ' + os.environ['KLAVIYO_API_KEY']]
    if body is not None:
        cmd += ['-H', 'content-type: application/vnd.api+json', '--data-binary', '@-']
    for attempt in range(8):
        r = subprocess.run(cmd, input=json.dumps(body) if body is not None else None, capture_output=True, text=True)
        out, _, code = r.stdout.rpartition('\n')
        code = int(code or 0)
        if code == 429 or code >= 500 or code == 0:
            time.sleep(min(60, 2 * (attempt + 1) ** 2))
            continue
        try:
            return code, (json.loads(out) if out.strip() else {})
        except ValueError:
            return code, out
    return code, 'opgegeven na herhaalde 429/5xx'

def events(metric, since=None, profile=None, until=None):
    f = ['equals(metric_id,"%s")' % metric]
    if since: f.append('greater-or-equal(datetime,%s)' % since)
    if until: f.append('less-than(datetime,%s)' % until)
    if profile: f.append('equals(profile_id,"%s")' % profile)
    q = {'filter': 'and(%s)' % ','.join(f) if len(f) > 1 else f[0], 'page[size]': '200', 'sort': 'datetime',
         'fields[event]': 'datetime,event_properties'}
    url = API + '/api/events/?' + urllib.parse.urlencode(q)
    n = 0
    while url:
        code, d = api('GET', url)
        if code != 200:
            sys.exit('events %s: HTTP %s %s' % (metric, code, str(d)[:300]))
        for e in d.get('data', []):
            yield e
        n += 1
        if n % 25 == 0:
            print('  .. %s: %d pagina\'s, t/m %s' % (metric, n, d['data'][-1]['attributes']['datetime'] if d.get('data') else '?'),
                  file=sys.stderr, flush=True)
        url = (d.get('links') or {}).get('next')

# ---------------------------------------------------------------- ledger
def load_json(p, default):
    try:
        if p.endswith('.gz'):
            with gzip.open(p, 'rt') as f: return json.load(f)
        with open(p) as f: return json.load(f)
    except (OSError, ValueError):
        return default

def save_json(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + '.tmp'
    if p.endswith('.gz'):
        with gzip.open(tmp, 'wt') as f: json.dump(obj, f, separators=(',', ':'))
    else:
        with open(tmp, 'w') as f: json.dump(obj, f, indent=1, ensure_ascii=False)
    os.replace(tmp, p)

UNKNOWN = collections.Counter()

def ingest_placed(L, e):
    """Placed Order -> ledger-order {p, at, lines:{line_id:[qty, keys, bundle]}, st}. Geeft profiel-id terug."""
    p = e['attributes']['event_properties']; x = p.get('$extra') or {}
    prof = (((e.get('relationships') or {}).get('profile') or {}).get('data') or {}).get('id')
    oid = str(p.get('$event_id') or x.get('id') or e['id'])
    if not prof:
        return None
    o = L.setdefault(oid, {'st': 'ok', 'ref': {}})
    o['p'] = prof
    o['at'] = e['attributes']['datetime']
    if x.get('test'):
        o['st'] = 'test'
    lines = {}
    items = x.get('line_items')
    if items is None:  # zonder $extra: alleen Items-namen
        items = [{'id': 'i%d' % i, 'title': n, 'quantity': 1} for i, n in enumerate(p.get('Items') or [])]
    for li in items:
        prod = li.get('product') or {}
        title = li.get('title') or li.get('name') or prod.get('title')
        variant = li.get('variant_title') or ((prod.get('variant') or {}).get('title'))
        r = classify(title, variant, prod.get('handle'))
        if r is None:
            UNKNOWN[(title, variant, prod.get('handle'))] += 1
            continue
        keys, bundle = r
        if keys:
            lines[str(li.get('id'))] = [li.get('quantity') or 1, keys, bundle]
    o['lines'] = lines
    return prof

def ingest_status(L, e, kind):
    """Cancelled / Refunded Order: status bijwerken; ook als de Placed Order nog niet in de ledger staat."""
    p = e['attributes']['event_properties']; x = p.get('$extra') or {}
    oid = str(p.get('$event_id') or x.get('id'))
    prof = (((e.get('relationships') or {}).get('profile') or {}).get('data') or {}).get('id')
    o = L.setdefault(oid, {'st': 'ok', 'ref': {}, 'lines': None, 'p': prof, 'at': e['attributes']['datetime']})
    if kind == 'cancel' or x.get('cancelled_at'):
        o['st'] = 'cancelled'
    elif x.get('financial_status') == 'refunded':
        o['st'] = 'refunded'
    # het event bevat de volledige refundlijst van de order: per regel optellen en vervangen
    tot = collections.Counter()
    for rf in x.get('refunds') or []:
        for rl in rf.get('refund_line_items') or []:
            tot[str(rl.get('line_item_id'))] += rl.get('quantity') or 0
    o['ref'] = dict(tot)
    return o.get('p')

def profile_view(L, oids):
    keys, cats, dates, n = set(), set(), [], 0
    for oid in oids:
        o = L[oid]
        if o['st'] != 'ok' or o.get('lines') is None:
            continue
        got = False
        for lid_, (qty, k, bundle) in o['lines'].items():
            if o['ref'].get(lid_, 0) >= qty:
                continue
            keys.update(k); cats.update(cats_of(k, bundle)); got = True
        n += 1
        dates.append(o['at'])
    return {'siraat_owned': sorted(keys), 'siraat_owned_cats': sorted(cats),
            'siraat_first_order_at': min(dates) if dates else None,
            'siraat_last_order_at': max(dates) if dates else None, 'siraat_orders': n}

def backfill(L, prof):
    """Volledige historie van één profiel (als de ledger nog niet compleet is)."""
    for e in events(M_PLACED, profile=prof):
        ingest_placed(L, e)
    for e in events(M_CANCEL, profile=prof):
        ingest_status(L, e, 'cancel')
    for e in events(M_REFUND, profile=prof):
        ingest_status(L, e, 'refund')

# ---------------------------------------------------------------- schrijven
def props(v):
    out = {k: v[k] for k in ('siraat_owned', 'siraat_owned_cats', 'siraat_orders')}
    for k in ('siraat_first_order_at', 'siraat_last_order_at'):
        if v[k]: out[k] = v[k]
    return out

def write_patch(rows):
    bad = []
    for prof, v in rows:
        code, d = api('PATCH', '/api/profiles/%s/' % prof,
                      {'data': {'type': 'profile', 'id': prof, 'attributes': {'properties': props(v)}}})
        if code != 200:
            bad.append((prof, code, str(d)[:200]))
        time.sleep(0.1)
    return bad

def write_bulk(rows):
    bad, jobs = [], []
    for i in range(0, len(rows), 5000):
        chunk = rows[i:i + 5000]
        body = {'data': {'type': 'profile-bulk-import-job', 'attributes': {'profiles': {'data': [
            {'type': 'profile', 'id': prof, 'attributes': {'properties': props(v)}} for prof, v in chunk]}}}}
        code, d = api('POST', '/api/profile-bulk-import-jobs/', body)
        if code not in (200, 201, 202):
            bad.append(('job %d' % i, code, str(d)[:300])); continue
        jobs.append(d['data']['id']); time.sleep(1)
    for j in jobs:
        for _ in range(240):
            code, d = api('GET', '/api/profile-bulk-import-jobs/%s/' % j)
            a = (d.get('data') or {}).get('attributes', {}) if isinstance(d, dict) else {}
            if a.get('status') in ('complete', 'failed', 'cancelled'):
                print('  bulk job %s: %s, %s/%s verwerkt, %s fouten' % (j, a.get('status'), a.get('completed_count'),
                      a.get('total_count'), a.get('failed_count')))
                if a.get('failed_count'):
                    c2, er = api('GET', '/api/profile-bulk-import-jobs/%s/import-errors/' % j)
                    for x in (er.get('data') or [])[:20] if isinstance(er, dict) else []:
                        bad.append((j, 'import-error', json.dumps(x.get('attributes'))[:200]))
                if a.get('status') != 'complete':
                    bad.append((j, a.get('status'), ''))
                break
            time.sleep(5)
        else:
            bad.append((j, 'timeout', 'job nog niet klaar na 20 min'))
    return bad

def verify(rows):
    fails = 0
    for prof, v in rows:
        code, d = api('GET', '/api/profiles/%s/?fields%%5Bprofile%%5D=properties' % prof)
        pr = ((d.get('data') or {}).get('attributes') or {}).get('properties') or {} if isinstance(d, dict) else {}
        want = props(v)
        diff = {k: (pr.get(k), w) for k, w in want.items() if pr.get(k) != w}
        if diff:
            fails += 1
            print('  CONTROLE FOUT %s: %s' % (prof, json.dumps(diff)[:300]))
        time.sleep(0.1)
    return fails

# ---------------------------------------------------------------- main
def iso(d): return d.strftime('%Y-%m-%dT%H:%M:%S+00:00')

def check():
    st = load_json(STATE, {})
    last = st.get('last_success_at')
    if not last:
        print('WAARSCHUWING sync_owned: nog nooit een geslaagde live run.'); sys.exit(1)
    age = (DT.datetime.now(DT.timezone.utc) - DT.datetime.fromisoformat(last)).total_seconds() / 3600
    if age > MAX_AGE_H:
        print('WAARSCHUWING sync_owned: laatste geslaagde run %s (%.0f uur geleden, grens %d).' % (last, age, MAX_AGE_H))
        sys.exit(1)
    print('OK sync_owned: laatste geslaagde run %s (%.1f uur geleden), %s profielen geschreven.'
          % (last, age, st.get('last_run', {}).get('written')))

def main():
    if '--check' in OPT:
        return check()
    t0 = time.time()
    now = DT.datetime.now(DT.timezone.utc)
    st = load_json(STATE, {})
    # zonder ledger-bestand (bv. verse checkout) valt het script terug op ophalen per profiel
    complete = bool(st.get('full_history_done')) and os.path.exists(LEDGER)
    L = load_json(LEDGER, {}) if complete else {}
    if SINCE:
        start = SINCE + 'T00:00:00Z'
    elif st.get('cursor'):
        start = iso(DT.datetime.fromisoformat(st['cursor']) - DT.timedelta(hours=OVERLAP_H)).replace('+00:00', 'Z')
    else:
        start = None  # volledige historie
    print('sync_owned %s | bron vanaf %s | ledger %s (%d orders)' % ('LIVE' if LIVE else 'DRY-RUN', start or 'begin (volledige historie)',
          'compleet' if complete else 'nog niet compleet', len(L)))
    if start is None and not complete:
        complete_after = True
    else:
        complete_after = complete

    dirty, cursor = set(), st.get('cursor')
    nev = collections.Counter()
    for metric, kind in ((M_PLACED, 'placed'), (M_CANCEL, 'cancel'), (M_REFUND, 'refund')):
        for e in events(metric, since=start):
            nev[kind] += 1
            prof = ingest_placed(L, e) if kind == 'placed' else ingest_status(L, e, kind)
            if prof: dirty.add(prof)
            dt = e['attributes']['datetime']
            if kind == 'placed' and (not cursor or dt > cursor): cursor = dt
    print('events: %d Placed, %d Cancelled, %d Refunded | %d profielen geraakt (%.0f s)'
          % (nev['placed'], nev['cancel'], nev['refund'], len(dirty), time.time() - t0))

    by_prof = collections.defaultdict(list)
    for oid, o in L.items():
        if o.get('p'): by_prof[o['p']].append(oid)
    targets = sorted(dirty)
    if LIMIT:
        targets = targets[:LIMIT]
    if not complete_after:
        # volledige historie per profiel ophalen voor wie we schrijven of als voorbeeld tonen
        need = targets if LIVE else targets[:NEX]
        print('ledger niet compleet: volledige historie ophalen voor %d profielen ...' % len(need), flush=True)
        for prof in need:
            backfill(L, prof)
        by_prof = collections.defaultdict(list)
        for oid, o in L.items():
            if o.get('p'): by_prof[o['p']].append(oid)
    rows = [(p, profile_view(L, by_prof[p])) for p in targets]

    # rapport
    keyc, catc = collections.Counter(), collections.Counter()
    for _, v in rows:
        keyc.update(v['siraat_owned']); catc.update(v['siraat_owned_cats'])
    st_c = collections.Counter(L[o]['st'] for p in targets for o in by_prof[p])
    print('profielen te schrijven: %d | orders per status: %s' % (len(rows), dict(st_c)))
    print('categorieën: %s' % dict(catc.most_common()))
    print('sleutels: %s' % ', '.join('%s %d' % kv for kv in keyc.most_common()))
    print('leeg (alleen gifts/terugbetaald): %d' % sum(1 for _, v in rows if not v['siraat_owned']))
    if UNKNOWN:
        print('ONBEKENDE producttitels (niet gemapt, %d regels):' % sum(UNKNOWN.values()))
        for (t, v, h), c in UNKNOWN.most_common(30):
            print('  %4d  %s | %s | %s' % (c, t, v, h))
    print('\nvoorbeelden%s:' % ('' if complete_after or LIVE else ' (volledige historie per profiel opgehaald)'))
    for p, v in rows[:NEX]:
        print('  %s  orders=%d  %s..%s  cats=%s  owned=%s' % (p, v['siraat_orders'], (v['siraat_first_order_at'] or '-')[:10],
              (v['siraat_last_order_at'] or '-')[:10], ','.join(v['siraat_owned_cats']), ','.join(v['siraat_owned'])))

    if not LIVE:
        print('\nDRY-RUN: niets geschreven (Klaviyo en staat ongewijzigd). %.0f s' % (time.time() - t0))
        return
    use_bulk = ('--bulk' in OPT) or (len(rows) > 100 and '--patch' not in OPT)
    print('\nschrijven: %d profielen via %s ...' % (len(rows), 'bulk import' if use_bulk else 'PATCH'), flush=True)
    bad = write_bulk(rows) if use_bulk else write_patch(rows)
    for b in bad[:20]:
        print('  FOUT', b)
    fails = None
    if LIMIT and len(rows) <= 200:
        print('controle met GET ...', flush=True)
        fails = verify(rows)
        print('controle: %d van %d profielen afwijkend' % (fails, len(rows)))
    run = {'at': iso(now), 'mode': 'live', 'since': start, 'limit': LIMIT, 'events': dict(nev), 'written': len(rows),
           'errors': len(bad), 'verify_fails': fails, 'seconds': round(time.time() - t0)}
    st.setdefault('runs', []).append(run); st['runs'] = st['runs'][-30:]
    st['last_run'] = run
    if not LIMIT and not SINCE and not bad:
        # alleen een volledige of reguliere incrementele run zet de cursor en telt als geslaagd
        st['cursor'] = cursor
        st['full_history_done'] = complete_after
        st['last_success_at'] = iso(now)
        save_json(LEDGER, L)
    save_json(STATE, st)
    print('klaar in %.0f s; %d fouten.' % (time.time() - t0, len(bad)))
    if bad:
        sys.exit(1)

if __name__ == '__main__':
    main()
