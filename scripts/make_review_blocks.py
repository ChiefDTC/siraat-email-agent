"""Reviewsets voor het v5-blok {{BLOCK:reviews3 set="c1"}} (drie pijlers: kwaliteit, levering, service).

Leest content/reviews/top.md (selectie van de review-curator, 8 okt 2026):
  - tabel "Alle gebruikte snippets" (ref, klant, datum, pijlers, snippet)
  - per mail de tabellen "Per mail: voorgestelde set" (q1, q2, q3)
Controleert elke snippet tegen content/reviews/library.csv: Trustpilot, 5 sterren, bruikbaar in mail, letterlijk
(elk stuk tussen "..." moet in de volledige tekst staan), max 120 tekens, geen gedachtestreepje, en R017 (Marilyn B.) nooit.
Schrijft content/reviews/sets.json (wordt gelezen door scripts/v5lib.py). Extra sets: zie EXTRA hieronder.

Gebruik: python3 -I scripts/make_review_blocks.py        (exit 1 bij een fout)
"""
import os, re, csv, json, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
TOP = os.path.join(ROOT, 'content', 'reviews', 'top.md')
LIB = os.path.join(ROOT, 'content', 'reviews', 'library.csv')
OUT = os.path.join(ROOT, 'content', 'reviews', 'sets.json')
BANNED = {'R017': 'Marilyn B., zwak volgens Floris (8 okt 2026)'}
# Extra sets (zelfde regels), voor blokken die niet aan één mail hangen. Volgorde = kwaliteit, levering, service.
EXTRA = {
    'kls-pan': ['R577', 'R516', 'R240'],          # standaardmix Pan Pro
    'kls-set': ['R398', 'R157', 'R530'],          # set: hele collectie, pannen en deksels snel binnen, service bij de set
    'kls-int': ['R554', 'R399', 'R407-M'],        # internationaal: 30 cm, Melbourne, UK-klant geholpen met de maat
    'kls-acc': ['R490', 'R158', 'R148'],          # accessoire
    'kls-owner': ['R547', 'R082', 'R101'],        # bestaande klant: tweede aankoop, levering, service
}

def rows(md, start):
    i = md.index(start); out = []
    for line in md[i:].split('\n')[2:]:
        if not line.startswith('|'):
            if out: break
            continue
        if set(line.replace('|', '').strip()) <= set('-'): continue
        out.append([c.strip() for c in line.strip().strip('|').split('|')])
    return out

def main():
    md = open(TOP).read()
    lib = {r['review_id']: r for r in csv.DictReader(open(LIB))}
    revs = {}
    for c in rows(md, '## Alle gebruikte snippets'):
        if c[0] == 'Ref': continue
        ref, name, date, pil, snip = c[0], c[1], c[2], c[3], c[4]
        snip = snip.strip()
        if snip.startswith('"') and snip.endswith('"'): snip = snip[1:-1]
        revs[ref] = {'name': name, 'date': date, 'pillars': [p for p in pil.split('/') if p in ('K', 'L', 'S')], 'snippet': snip}
    sets = {}
    for sec in re.findall(r'^### (\w[\w-]*)\n', md, re.M):
        for c in rows(md, '### %s\n' % sec):
            if c[0] == 'Mail' or len(c) < 5: continue
            refs = [re.match(r'(R\d+(?:-[A-Z])?)', x).group(1) for x in c[2:5] if re.match(r'R\d+', x)]
            sets[c[0]] = refs
    for k, v in EXTRA.items(): sets[k] = v
    bad = []
    for ref, r in revs.items():
        base = ref.split('-')[0]; L = lib.get(base)
        if base in BANNED: bad.append('%s staat in de snippetlijst maar is verboden' % ref)
        if not L: bad.append('%s niet in library.csv' % ref); continue
        if L['bron'] != 'Trustpilot' or L['sterren'] != '5': bad.append('%s: geen Trustpilot 5 sterren' % ref)
        if not L['bruikbaar_in_mail'].startswith('ja'): bad.append('%s: niet bruikbaar in mail' % ref)
        tekst = re.sub(r'\s+', ' ', L['tekst'])
        for piece in [p.strip() for p in r['snippet'].split('...') if p.strip()]:
            if re.sub(r'\s+', ' ', piece) not in tekst: bad.append('%s: niet letterlijk: %r' % (ref, piece[:60]))
        if len(r['snippet']) > 120: bad.append('%s: %d tekens' % (ref, len(r['snippet'])))
        if '—' in r['snippet']: bad.append('%s: gedachtestreepje' % ref)
        if not r['pillars']: bad.append('%s: geen pijler' % ref)
    for s, refs in sets.items():
        for ref in refs:
            if ref.split('-')[0] in BANNED: bad.append('set %s bevat verboden %s' % (s, ref))
            elif ref not in revs: bad.append('set %s: %s heeft geen gecontroleerde snippet' % (s, ref))
        if len(refs) < 2: bad.append('set %s: minder dan 2 reviews' % s)
    if bad:
        print('\n'.join(bad)); sys.exit(1)
    json.dump({'generated_from': 'content/reviews/top.md + library.csv (scripts/make_review_blocks.py)', 'banned': BANNED,
               'reviews': revs, 'sets': sets}, open(OUT, 'w'), indent=1, ensure_ascii=False)
    print('ok: %d reviews, %d sets -> %s' % (len(revs), len(sets), os.path.relpath(OUT, ROOT)))

if __name__ == '__main__': main()
