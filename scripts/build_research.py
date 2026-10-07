"""Bouwt een demo-mail met de nieuwe research-blokken (research/ux-round2/blocks) en daarna build_template.py.
Raakt klaviyo/templates niet aan: blokken uit research/ux-round2/blocks worden eerst ingevuld,
de rest ({{BLOCK:...}}, {{HEADER}}, {{FOOTER}}) doet het bestaande build_template.py.

Gebruik:
  python3 -I scripts/build_research.py <bron.html> <uit.html>
  bron: mag {{RBLOCK:naam key="waarde"}} bevatten (compare, closerlook, productcard)
  uit:  het ingevulde bestand; build_template.py maakt daarnaast <uit>-preview.html
        (assets-map = map 'assets' naast <uit>, partials via de bovenliggende map 'partials').
"""
import sys, os, re, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
RB = os.path.join(ROOT, 'research', 'ux-round2', 'blocks')
DEF = {
    'compare': {'pad': '34px 44px 6px 44px', 'eyebrow': 'THE DIFFERENCE', 'headline': 'Titanium vs. coated nonstick',
                'cap': 'compare-cap-panpro.png', 'colA': 'Siraat Titanium', 'colB': 'Coated nonstick', 'note': '',
                'ib1': 'cross', 'ib2': 'cross', 'ib3': 'cross', 'ib4': 'cross', 'ib5': 'cross'},
    'closerlook': {'pad': '34px 44px 6px 44px', 'eyebrow': 'UP CLOSE', 'headline': 'Take a closer look.'},
    'productcard': {'pad': '0 44px 10px 44px', 'pill': '', 'note': '', 'was': '', 'link': 'Shop now'},
}
PILL = ('<div style="padding-bottom:8px;"><span style="display:inline-block;background:#AC3B19;color:#FFFFFF;'
        'font-size:10px;line-height:14px;letter-spacing:1.4px;font-weight:600;padding:3px 9px;border-radius:10px;">%s</span></div>')


def rblock(m):
    name = m.group(1); kv = dict(DEF.get(name, {}))
    kv.update(dict(re.findall(r'(\w+)="([^"]*)"', m.group(2))))
    t = open(os.path.join(RB, name + '.html')).read()
    if name == 'compare':
        row = open(os.path.join(RB, 'compare-row.html')).read(); rows = []
        for i in range(1, 6):
            last = i == 5
            r = row.replace('[[a]]', kv.pop('a%d' % i)).replace('[[b]]', kv.pop('b%d' % i))
            ib = kv.pop('ib%d' % i)
            r = r.replace('[[ib]]', ib).replace('[[ibalt]]', 'Also yes:' if ib == 'same' else 'No:')
            r = r.replace('[[radA]]', 'border-bottom:0;border-radius:0 0 0 12px;' if last else '')
            r = r.replace('[[radB]]', 'border-bottom:0;border-radius:0 0 12px 0;' if last else '')
            rows.append(r)
        kv['rows'] = ''.join(rows)
    if name == 'productcard': kv['pill'] = PILL % kv['pill'] if kv['pill'] else ''
    if name == 'productcard':
        w = kv.pop('was'); kv['washtml'] = ('<span style="color:#9A948B;text-decoration:line-through;">%s</span>&nbsp; ' % w) if w else ''
    for k, v in kv.items(): t = t.replace('[[' + k + ']]', v)
    left = re.findall(r'\[\[\w+\]\]', t)
    if left: sys.exit('blok %s mist %s' % (name, left))
    return t


def main():
    if len(sys.argv) != 3: sys.exit(__doc__)
    src, out = sys.argv[1:]
    h = open(src).read()
    h = re.sub(r'\{\{RBLOCK:([\w-]+)((?:\s+\w+="[^"]*")*)\s*\}\}', rblock, h)
    h = h.replace('</style>', open(os.path.join(RB, '_style.css')).read() + '</style>', 1)
    open(out, 'w').write(h)
    d = os.path.dirname(os.path.abspath(out))
    subprocess.run([sys.executable, '-I', os.path.join(ROOT, 'scripts', 'build_template.py'), out,
                    os.path.join(d, 'assets'), os.path.join(d, 'assets', 'klaviyo-urls.txt')], check=True)


if __name__ == '__main__':
    main()
