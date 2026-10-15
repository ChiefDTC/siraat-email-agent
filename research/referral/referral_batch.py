"""Wekelijkse referral-batch (route A, research/referral/01-ontwerp.md en 02-livegang-stappen.md stap 7).

Zoekt orders die met een vrienden-code uit de Klaviyo-pool zijn betaald, koppelt elke code aan de klant die hem kreeg
(Coupon Assigned, metric XUMYt7) en beoordeelt per order of de verwijzer zijn beloning krijgt.

Standaard ALLEEN LEZEN (GET op de Klaviyo-API). Schrijft een CSV met profiel-id's (geen e-mailadressen) BUITEN de repo.
Met --apply --i-am-sure stuurt het script per goedgekeurde order een eigen event 'Referral Reward Earned' naar het profiel van de
verwijzer; dat event start de beloningsflow (v4 · Referral · beloning). Een event vuurt elke keer opnieuw (een lijst niet: wie
al op de lijst staat, start de flow niet nog een keer). Schrijfactie: alleen na akkoord Floris en met een sleutel met events:write.

Gebruik:
  python3 -I research/referral/referral_batch.py --pool=REF_FRIEND_25 [--days=120] [--min-age=40] [--cap=10]
         [--out=~/referral-batch.csv] [--state=~/referral-rewarded.txt] [--apply --i-am-sure]

Regels (01-ontwerp.md sectie 5):
  1. code komt uit de pool (CouponKey == --pool), verwijzer = profiel van Coupon Assigned
  2. vriend is niet de verwijzer (ander profiel, ander e-mailadres, ander verzendadres dan alle orders van de verwijzer)
  3. vriend had voor deze order nog nooit een Placed Order (eerste order)
  4. geen Refunded Order en geen Cancelled Order op deze order
  5. order is minstens --min-age dagen oud (30-day returns vanaf levering; mediaan levering 12 dagen, dus standaard 40)
  6. maximaal --cap beloningen per verwijzer per 365 dagen; elke order maar een keer (state-bestand)
"""
import sys, os, json, csv, time, subprocess, datetime as dt, re

OPT = {a.split('=', 1)[0]: (a.split('=', 1)[1] if '=' in a else '1') for a in sys.argv[1:] if a.startswith('--')}
POOL = OPT.get('--pool', 'REF_FRIEND_25')
DAYS = int(OPT.get('--days', '120')); MINAGE = int(OPT.get('--min-age', '40')); CAP = int(OPT.get('--cap', '10'))
OUT = os.path.expanduser(OPT.get('--out', '~/referral-batch.csv'))
STATE = os.path.expanduser(OPT.get('--state', '~/referral-rewarded.txt'))
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
if os.path.abspath(OUT).startswith(REPO) or os.path.abspath(STATE).startswith(REPO):
    sys.exit('uitvoer met profiel-id\'s hoort niet in de (publieke) repo: kies een pad buiten ' + REPO)

M_ORDER, M_ASSIGNED, M_REFUND, M_CANCEL = 'RSNxYV', 'XUMYt7', 'Xg6cwn', 'TFervq'


def api(method, path, body=None):
    """Klaviyo-API via curl; de sleutel komt uit de omgeving (proxy of KLAVIYO_API_KEY)."""
    url = path if path.startswith('http') else 'https://a.klaviyo.com' + path
    c = ['curl', '-sS', '-g', '-X', method, url, '-H', 'revision: 2025-10-15', '-H', 'accept: application/vnd.api+json',
         '-H', 'content-type: application/vnd.api+json']
    if os.environ.get('KLAVIYO_API_KEY'): c += ['-H', 'Authorization: Klaviyo-API-Key ' + os.environ['KLAVIYO_API_KEY']]
    if body is not None: c += ['-d', json.dumps(body)]
    for _ in range(6):
        out = subprocess.run(c, capture_output=True, text=True).stdout
        try:
            r = json.loads(out) if out.strip() else {}
        except ValueError:
            time.sleep(2); continue
        if any(e.get('status') == 429 for e in r.get('errors', [])): time.sleep(2); continue
        return r
    return {'errors': [{'detail': 'geen antwoord'}]}


def events(metric, since, extra=''):
    url = '/api/events/?filter=equals(metric_id,"%s"),greater-than(datetime,%s)%s&page[size]=200&fields[event]=event_properties,datetime' % (
        metric, since.strftime('%Y-%m-%dT%H:%M:%SZ'), extra)
    while url:
        r = api('GET', url)
        if r.get('errors'): sys.exit('API-fout: %s' % r['errors'][:1])
        for e in r.get('data', []): yield e
        url = (r.get('links') or {}).get('next')


def profile_email(pid, cache={}):
    if pid not in cache:
        r = api('GET', '/api/profiles/%s/?fields[profile]=email' % pid)
        cache[pid] = ((r.get('data') or {}).get('attributes') or {}).get('email') or ''
    return cache[pid]


def addr(ev):
    a = ((ev['attributes']['event_properties'].get('$extra') or {}).get('shipping_address') or {})
    return re.sub(r'\W', '', ('%s%s' % (a.get('address1') or '', a.get('zip') or '')).lower())


def order_id(ev):
    p = ev['attributes']['event_properties']
    return str((p.get('$extra') or {}).get('id') or p.get('$event_id') or ev['id'])


def main():
    now = dt.datetime.now(dt.timezone.utc).replace(tzinfo=None); since = now - dt.timedelta(days=DAYS)
    # 1. code -> verwijzer (Coupon Assigned van deze pool; codes kunnen al voor 'since' zijn toegewezen: 60 dagen geldig, dus +60)
    owner = {}
    for e in events(M_ASSIGNED, since - dt.timedelta(days=60)):
        p = e['attributes']['event_properties']
        if p.get('CouponKey') == POOL and p.get('UniqueCode'):
            owner[p['UniqueCode'].upper()] = e['relationships']['profile']['data']['id']
    # 2. orders met zo'n code
    hits = []
    for e in events(M_ORDER, since):
        codes = [c.upper() for c in (e['attributes']['event_properties'].get('Discount Codes') or [])]
        for c in codes:
            if c in owner: hits.append((c, e))
    refunded = {order_id(e) for e in events(M_REFUND, since)} | {order_id(e) for e in events(M_CANCEL, since)}
    done = set(open(STATE).read().split()) if os.path.exists(STATE) else set()
    per_ref = {}
    rows = []
    for code, e in hits:
        friend = e['relationships']['profile']['data']['id']; ref = owner[code]; oid = order_id(e)
        t = dt.datetime.fromisoformat(e['attributes']['datetime'].replace('Z', '+00:00')).replace(tzinfo=None)
        status, why = 'OK', ''
        if oid in done: status, why = 'AL_BELOOND', 'order staat in state-bestand'
        elif friend == ref: status, why = 'NEE', 'eigen code (zelfde profiel)'
        elif profile_email(friend).lower() == profile_email(ref).lower() and profile_email(ref): status, why = 'NEE', 'zelfde e-mailadres'
        elif oid in refunded: status, why = 'NEE', 'refund of annulering'
        else:
            prior = [x for x in events(M_ORDER, dt.datetime(2020, 1, 1), ',equals(profile_id,"%s")' % friend)
                     if x['attributes']['datetime'] < e['attributes']['datetime']]
            ref_addrs = {addr(x) for x in events(M_ORDER, dt.datetime(2020, 1, 1), ',equals(profile_id,"%s")' % ref)}
            if prior: status, why = 'NEE', 'vriend had al een order (geen nieuwe klant)'
            elif addr(e) and addr(e) in ref_addrs: status, why = 'NEE', 'zelfde verzendadres als verwijzer'
            elif (now - t).days < MINAGE: status, why = 'WACHT', 'order jonger dan %d dagen (retourtermijn)' % MINAGE
            elif per_ref.get(ref, 0) >= CAP: status, why = 'NEE', 'plafond %d per verwijzer bereikt' % CAP
        if status == 'OK': per_ref[ref] = per_ref.get(ref, 0) + 1
        rows.append({'order_id': oid, 'order_datum': e['attributes']['datetime'][:10], 'order_waarde': e['attributes']['event_properties'].get('$value'),
                     'vriend_profiel': friend, 'verwijzer_profiel': ref, 'status': status, 'reden': why})
    with open(OUT, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['order_id', 'order_datum', 'order_waarde', 'vriend_profiel', 'verwijzer_profiel', 'status', 'reden'])
        w.writeheader(); w.writerows(rows)
    tel = {}
    for r in rows: tel[r['status']] = tel.get(r['status'], 0) + 1
    omzet = sum(float(r['order_waarde'] or 0) for r in rows if r['status'] in ('OK', 'WACHT', 'AL_BELOOND'))
    print('pool %s: %d codes toegewezen, %d orders met code, status %s, omzet vrienden $%.0f' % (POOL, len(owner), len(rows), tel, omzet))
    print('CSV (profiel-id\'s, niet in de repo): ' + OUT)
    if OPT.get('--apply'):
        if not OPT.get('--i-am-sure'): sys.exit('--apply vraagt ook --i-am-sure')
        ok = [r for r in rows if r['status'] == 'OK']
        for r in ok:
            body = {'data': {'type': 'event', 'attributes': {
                'properties': {'friend_order_id': r['order_id'], 'friend_order_value': r['order_waarde'], 'pool': POOL},
                'unique_id': 'ref-reward-' + r['order_id'],
                'metric': {'data': {'type': 'metric', 'attributes': {'name': 'Referral Reward Earned'}}},
                'profile': {'data': {'type': 'profile', 'id': r['verwijzer_profiel']}}}}}
            res = api('POST', '/api/events/', body)
            if res.get('errors'): sys.exit('fout bij %s: %s' % (r['order_id'], res['errors'][:1]))
            with open(STATE, 'a') as f: f.write(r['order_id'] + '\n')
        print('%d beloningsevents verstuurd, state bijgewerkt' % len(ok))


if __name__ == '__main__':
    main()
