"""Prototype dark mode (13-darkmode.md). Werkt alleen op kopieën in research/v6-golive/darkmode/, nooit op de echte templates.
Gebruik (vanuit /tmp): python3 -I research/v6-golive/darkmode/make_after.py
  before/<mail>.html  gerenderde mail zoals hij nu is (qa_render-route, Django op een testevent)
  after/<mail>.html   variant A (advies): light only + Outlook-herstelregels
  after/c1-B.html     variant B (NIET doen): A plus crème/wit vastgezet met background-image (Gmail-truc), ter vergelijking
De functie light_only() is precies wat build_template.py als laatste stap zou doen (zie diff in 13-darkmode.md)."""
import re, os, sys
D = os.path.dirname(os.path.abspath(__file__))

def light_only(k):
    # 1. color-scheme: 'light' wordt 'light only' (meta's) plus :root (CSS). Spec-grammatica staat 'light only' en 'only light' toe.
    k = re.sub(r'<meta name="color-scheme" content="[^"]*">', '<meta name="color-scheme" content="light only">', k)
    k = re.sub(r'<meta name="supported-color-schemes" content="[^"]*">', '<meta name="supported-color-schemes" content="light only">', k)
    # eigen <style>-blok: als een client :root niet snapt en het blok weggooit, blijft de layout-CSS staan
    k = k.replace('</head>', '<style>:root{color-scheme:light only;}</style>\n</head>', 1)
    # 2. Outlook.com en Outlook-apps: elk element met een vaste kleur krijgt een klasse per kleur (ob-xxxxxx achtergrond, oc-xxxxxx tekst).
    #    Outlook zet data-ogsb/data-ogsc op elementen waarvan het de kleur omzet; regels '[data-ogsb] .ob-xxxxxx' zetten de originele kleur terug.
    used_b, used_c = set(), set()
    def tag(m):
        t = m.group(0)
        st = re.search(r'style="([^"]*)"', t); sv = st.group(1) if st else ''
        b = re.search(r'(?:^|;)\s*background(?:-color)?\s*:\s*(#[0-9A-Fa-f]{6})\b', sv) or re.search(r'\bbgcolor="(#[0-9A-Fa-f]{6})"', t)
        c = re.search(r'(?:^|;)\s*color\s*:\s*(#[0-9A-Fa-f]{6})\b', sv)
        cls = []
        if b: cls.append('ob-' + b.group(1)[1:].lower()); used_b.add(b.group(1).upper())
        if c: cls.append('oc-' + c.group(1)[1:].lower()); used_c.add(c.group(1).upper())
        if not cls: return t
        if re.search(r'\sclass="', t): return re.sub(r'\sclass="([^"]*)"', lambda x: ' class="%s %s"' % (x.group(1), ' '.join(cls)), t, count=1)
        return re.sub(r'^<(\w+)', lambda x: '<%s class="%s"' % (x.group(1), ' '.join(cls)), t, count=1)
    head, body = k.split('<body', 1)
    body = re.sub(r'<(?:td|th|table|tr|div|p|span|a|b|strong|i|em|h\d|font)\b[^>]*>', tag, body)
    k = head + '<body' + body
    rules = ['[data-ogsb] .ob-%s{background-color:%s!important;}' % (x[1:].lower(), x) for x in sorted(used_b)]
    rules += ['[data-ogsb] .oc-%s,[data-ogsc] .oc-%s{color:%s!important;}' % (x[1:].lower(), x[1:].lower(), x) for x in sorted(used_c)]
    # Aparte <style>: clients die attribuutselectoren niet snappen (o.a. Gmail) gooien dan alleen dit blok weg, niet de layout-CSS.
    k = k.replace('</head>', '<style>\n/* Outlook.com/Outlook-apps: originele kleuren terug na hun dark mode */\n%s\n</style>\n</head>' % '\n'.join(rules), 1)
    return k

def gradient_lock(k):
    # Variant B: lichte vlakken vastzetten met background-image. Gmail-apps en Outlook laten background-image staan,
    # maar keren de TEKST erop wel om: lichte tekst op crème. Alleen ter illustratie.
    def rep(m):
        col = m.group(2)
        return '%s;background-image:linear-gradient(%s,%s)' % (m.group(0), col, col)
    return re.sub(r'(background(?:-color)?\s*:\s*)(#(?:F8F7F2|FFFFFF|ECE8E1|ECE7DD))', rep, k, flags=re.I)

if __name__ == '__main__':
    os.makedirs(os.path.join(D, 'after'), exist_ok=True)
    for f in sorted(os.listdir(os.path.join(D, 'before'))):
        if not f.endswith('.html'): continue
        k = light_only(open(os.path.join(D, 'before', f)).read())
        open(os.path.join(D, 'after', f), 'w').write(k); print('A', f, len(k))
        if f == 'c1.html':
            open(os.path.join(D, 'after', 'c1-B.html'), 'w').write(gradient_lock(k)); print('B c1')
