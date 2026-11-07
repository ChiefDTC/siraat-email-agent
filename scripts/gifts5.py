"""gifts5.py: van 4 naar 5 gratis gifts in bestaande Klaviyo-templates (HTML in, HTML uit).

Sinds november 2026 op de site: Mystery gift ($35), Free shipping ($15), Plastic-free e-book ($30),
Favorites Cookbook ($25, nieuw) plus een wekelijkse kans om een PFAS water filter te winnen ($450). Samen "$555 value".

Besluiten Floris (7 nov 2026): tegel blijft "Free shipping"; filter altijd "win / chance to win a PFAS water filter";
totaal is "$555 value", alleen in US-takken en US-mails, en alleen waar al een totaal stond of in de kop van het
gift-blok. Buiten de US geen valuta in het totaal.

Wat het script doet, per template:
  1. Telwoord in zichtbare copy: "4 gifts", "4 free gifts", "four gifts" (ook hoofdletters) wordt 5/five.
     Alleen in tekst en alt/title, ook in Outlook-blokken (<!--[if mso]>); nooit in URL's, <style> of Django-code.
  2. Totaal (--no-values zet dit uit): "$70 in gifts" (US-tak) wordt "5 free gifts ($555 value)",
     "$70 in gifts, on us" wordt "5 free gifts, on us ($555 value)"; de andere markten (C$95, £55 ...) worden
     "5 free gifts" zonder bedrag. Mystery-tegel US $25 wordt $35; mystery buiten de US blijft zoals hij is.
  3. Cookbook als vijfde tegel in elk herkend gift-blok, vlak voor de filter (filter blijft de laatste tegel):
       row   (data-gifts5="row", 4 naast elkaar)  -> 5 naast elkaar, tegels 20 procent, beeld 64 -> 56 px
       grid  (data-gifts5="grid", 2x2 / 4 breed)   -> cookbook op de filterplek, filter gecentreerd in een extra rij (2+2+1 mobiel, 4+1 desktop)
       cards (pp-complete, kaarten 270 px, 2x2)    -> cookbook op de filterplek, filterkaart gecentreerd in een derde rij
     De nieuwe tegel kopieert de e-book-tegel (zelfde opmaak, link, marktketen); waarde US "$25 value", elders "Included".
     In een US-kaartenmail wordt de kop "5 free gifts with every order ($555 value)".

Idempotent: een blok met het cookbook-beeld wordt overgeslagen en de tellingen matchen na de eerste ronde niet meer.
Het script draait elke template zelf twee keer en weigert als de tweede ronde iets verandert.

Gebruik (alleen lokaal, schrijft niets naar Klaviyo):
  python3 -I scripts/gifts5.py IN_DIR OUT_DIR --cookbook-img https://cdn.klaviyomail.com/... [--no-values] [--report r.json]
Templates die het script niet veilig aankan komen in het rapport onder "manual" en worden NIET geschreven.
"""
import argparse, json, os, re, sys

MARKETS = ['US', 'CA', 'UK', 'EU', 'AU', 'NZ', 'SG']
CUR = {'US': '$', 'CA': 'C$', 'UK': '£', 'EU': '€', 'AU': 'A$', 'NZ': 'NZ$', 'SG': 'S$'}
OLD = {  # (ship, ebook, mystery, filter, totaal) zoals live (v5lib.GIFT, 8 okt)
    'US': (15, 30, 25, 450, 70), 'CA': (20, 40, 35, 620, 95), 'UK': (10, 25, 20, 350, 55), 'EU': (15, 30, 25, 410, 70),
    'AU': (20, 45, 35, 660, 100), 'NZ': (25, 50, 45, 820, 120), 'SG': (20, 40, 35, 590, 95)}
MYSTERY_US, COOKBOOK_US, TOTAL_US = 35, 25, '$555&nbsp;value'   # 35 + 15 + 30 + 25 + 450; nbsp: nooit '($555' los van 'value)'

def amt(m, v): return '%s%d' % (CUR[m], v)
def amt_re(m, v):  # bedrag als los token: "$70" niet in "C$70" of "$700"
    return r'(?<![A-Za-z$])' + re.escape(amt(m, v)) + r'(?!\d)'

# ------------------------------------------------------------------ segmenten
DJ = re.compile(r'(\{%.*?%\}|\{\{.*?\}\})', re.S)
SEG = re.compile(r'(<!--.*?-->|<style\b.*?</style>|<script\b.*?</script>|<[^>]+>)', re.S)

def map_text(h, fn_text, fn_alt):
    """Past fn_text toe op tekst, fn_alt op alt/title; mso-blokken recursief; Django-commentaar en style overslaan."""
    out = []
    for part in SEG.split(h):
        if not part: continue
        if part.startswith('<!--'):
            if part.startswith('<!--[if') and part.endswith('<![endif]-->'):
                i = part.index(']>') + 2; j = len(part) - len('<![endif]-->')
                out.append(part[:i] + map_text(part[i:j], fn_text, fn_alt) + part[j:])
            else:
                out.append(part)
        elif part.startswith('<style') or part.startswith('<script'):
            out.append(part)
        elif part.startswith('<'):
            out.append(re.sub(r'(\s(?:alt|title)=")([^"]*)(")', lambda m: m.group(1) + fn_alt(m.group(2)) + m.group(3), part))
        else:
            # Django-code in platte tekst ({% ... %}, {{ ... }}) blijft ongemoeid
            out.append(''.join(x if x.startswith(('{%', '{{')) else fn_text(x) for x in DJ.split(part) if x))
    return ''.join(out)

SP = r'(?:\s|&nbsp;| )+'
COUNT = re.compile(r'\b(4|four|Four|FOUR)(' + SP + r')((?:free|Free|FREE)' + SP + r')?(gifts|Gifts|GIFTS)\b')
def five(m):
    n = {'4': '5', 'four': 'five', 'Four': 'Five', 'FOUR': 'FIVE'}[m.group(1)]
    return n + m.group(2) + (m.group(3) or '') + m.group(4)

def totals(s):
    """US: "$70 in gifts[, on us]" -> "5 free gifts[, on us] ($555 value)"; andere markten zonder bedrag."""
    for m in MARKETS:
        pat = amt_re(m, OLD[m][4]) + SP + r'(in|IN)' + SP + r'(gifts|GIFTS)((?:,' + SP + r'(?:on|ON)' + SP + r'(?:us|US))?)'
        def rep(mo, m=m):
            up = mo.group(1) == 'IN'
            base = ('5 FREE GIFTS' if up else '5 free gifts') + mo.group(3)
            return base + ((' (%s)' % (TOTAL_US.replace('value', 'VALUE') if up else TOTAL_US)) if m == 'US' else '')
        s = re.sub(pat, rep, s)
    return s

# ------------------------------------------------------------------ element helpers
def elem_end(h, start, tag):
    """Eindindex (na </tag>) van het element dat op start begint; telt nesting."""
    pat = re.compile(r'<(/?)%s\b[^>]*>' % tag, re.I)
    depth = 0
    for m in pat.finditer(h, start):
        depth += -1 if m.group(1) else 1
        if depth == 0: return m.end()
    raise ValueError('geen sluittag')

def enclosing_start(h, idx, tag):
    """Start van het binnenste <tag> dat idx omsluit."""
    pat = re.compile(r'<(/?)%s\b[^>]*>' % tag, re.I)
    stack = []
    for m in pat.finditer(h, 0, idx):
        if m.group(1):
            if stack: stack.pop()
        else: stack.append(m.start())
    if not stack: raise ValueError('geen omsluitend element')
    return stack[-1]

def ebook_to_cookbook_values(s):
    s = re.sub(amt_re('US', OLD['US'][1]) + r'(' + SP + r'value)', amt('US', COOKBOOK_US) + r'\1', s)
    for m in MARKETS[1:]:   # geen afgeleide bedragen buiten de US
        s = re.sub(amt_re(m, OLD[m][1]) + SP + r'value', 'Included', s)
    return s

def mystery_values(s):
    return re.sub(amt_re('US', OLD['US'][2]) + r'(' + SP + r'value)', amt('US', MYSTERY_US) + r'\1', s)

def make_tile(ebook_td, img):
    t = re.sub(r'data-gift="[^"]*"', 'data-gift="gift-cookbook.jpg"', ebook_td)
    t = re.sub(r'(<img[^>]*?\salt=")[^"]*(")', r'\1Favorites Cookbook\2', t)
    t = re.sub(r'(<img[^>]*?\ssrc=")[^"]*(")', lambda m: m.group(1) + img + m.group(2), t)
    t = re.sub(r'The Green Clean(<br\s*/?>|\s)E-Guide', r'Favorites\1Cookbook', t)
    t = re.sub(r'Plastic-Free Home e(?:‑|-| )book', 'Favorites Cookbook', t)
    if 'Favorites' not in re.sub(r'alt="[^"]*"', '', t): raise ValueError('e-book-label niet herkend')
    return ebook_to_cookbook_values(t)

def tile_td(block, key):
    i = block.find('data-gift="%s"' % key)
    if i < 0: raise ValueError('tegel %s ontbreekt' % key)
    s = block.rfind('<td', 0, i)   # data-gift staat op de <td> zelf
    return s, elem_end(block, s, 'td')

# ------------------------------------------------------------------ blokken
def do_row(block, img, opt):
    if 'gift-cookbook.jpg' in block: return block
    keys = re.findall(r'data-gift="([^"]+)"', block)
    if keys != ['gift-shipping.jpg', 'gift-ebook.jpg', 'gift-mystery.jpg', 'gift-filter.jpg']: raise ValueError('row: onverwachte tegels %s' % keys)
    es, ee = tile_td(block, 'gift-ebook.jpg'); new = make_tile(block[es:ee], img)
    fs, _ = tile_td(block, 'gift-filter.jpg')
    block = block[:fs] + new + '\n' + block[fs:]
    block = block.replace('colspan="4"', 'colspan="5"')
    block = re.sub(r'(data-gift="[^"]+"[^>]*?)width="25%"', r'\1width="20%"', block)
    block = re.sub(r'(<td[^>]*?)width="25%"([^>]*data-gift=)', r'\1width="20%"\2', block)
    block = block.replace('style="width:64px;height:64px;margin:0 auto;" width="64"', 'style="width:56px;height:56px;margin:0 auto;" width="56"')
    block = block.replace('padding:8px 4px 14px 4px;', 'padding:8px 2px 14px 2px;')
    if block.count('width="20%"') != 5: raise ValueError('row: breedtes niet omgezet')
    return block

def do_grid(block, img, opt):
    if 'gift-cookbook.jpg' in block: return block
    keys = re.findall(r'data-gift="([^"]+)"', block)
    if keys != ['gift-shipping.jpg', 'gift-ebook.jpg', 'gift-mystery.jpg', 'gift-filter.jpg']: raise ValueError('grid: onverwachte tegels %s' % keys)
    # 7 nov (Floris): de vier vaste gifts in het raster, de filter (kans) gecentreerd eronder.
    es, ee = tile_td(block, 'gift-ebook.jpg')
    cook = make_tile(block[es:ee], img)
    fs, fe = tile_td(block, 'gift-filter.jpg')
    ftile = block[fs:fe].replace('width="50%"', 'width="140"', 1)
    ftile = ftile.replace('font-family:Inter,Arial,Helvetica,sans-serif;"', 'font-family:Inter,Arial,Helvetica,sans-serif;width:126px;"', 1)
    block = block[:fs] + cook + block[fe:]
    # buitenste rastertabel: de <table> die de eerste g2-cel omsluit
    g = block.find('class="g2"')
    ts = enclosing_start(block, g, 'table'); te = elem_end(block, ts, 'table')
    row = ('\n<table role="presentation" align="center" cellpadding="0" cellspacing="0" border="0" data-gift5row="1" style="margin:10px auto 0 auto;"><tr>\n'
           + ftile + '\n</tr></table>')
    return block[:te] + row + block[te:]

def do_cards(h, img, opt):
    """pp-complete: 2x2 kaarten met beelden van 270 px. Derde rij met de cookbook-kaart, 50 procent, gecentreerd."""
    if 'alt="Favorites Cookbook"' in h: return h, 0
    fi = h.find('alt="Chance to win a PFAS water filter"')
    eb = re.search(r'alt="Plastic-Free Home e book"|alt="The Green Clean E-Guide"', h)
    if fi < 0 or not eb: raise ValueError('cards: filter- of e-book-kaart niet gevonden')
    # kaart = <td width=50%> die de kaarttabel omsluit
    def card_td(idx):
        t = enclosing_start(h, idx, 'table')   # kaarttabel rond het beeld
        s = enclosing_start(h, t, 'td'); return s, elem_end(h, s, 'td')
    es, ee = card_td(eb.start())
    card = h[es:ee]
    card = re.sub(r'(<img[^>]*?\salt=")[^"]*(")', r'\1Favorites Cookbook\2', card)
    card = re.sub(r'(<img[^>]*?\ssrc=")[^"]*(")', lambda m: m.group(1) + img + m.group(2), card)
    card = re.sub(r'Plastic-Free Home e(?:‑|-| )book|The Green Clean E-Guide', 'Favorites Cookbook', card)
    card = card.replace('width="50%"', 'width="50%" align="center"', 1)
    fs, fe = card_td(fi)
    # 7 nov (Floris): cookbook op de plek van de filter, filterkaart gecentreerd in de derde rij
    fcard = h[fs:fe].replace('width="50%"', 'width="50%" align="center"', 1)
    h = h[:fs] + card.replace('width="50%" align="center"', 'width="50%"', 1) + h[fe:]
    card = fcard
    grid = enclosing_start(h, fs, 'table'); ge = elem_end(h, grid, 'table')
    if h[ge - len('</tr></table>'):ge] != '</tr></table>': raise ValueError('cards: raster eindigt anders')
    ins = ('<tr><td colspan="2" align="center" style="padding:0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
           '<td width="25%" style="font-size:0;line-height:0;">&nbsp;</td>' + card + '<td width="25%" style="font-size:0;line-height:0;">&nbsp;</td></tr></table></td></tr>')
    pos = ge - len('</table>')
    head = h[:grid]
    if opt and 'alt="Free shipping"' in h[grid:pos]:   # US-mail (INT-variant heet "Free shipping, duties paid"): totaal in de kop
        k = head.rfind('4 gifts with every order</div>')
        if k > 0 and grid - k < 400:
            head = head[:k] + '5 free gifts with every order (%s)</div>' % TOTAL_US + head[k + len('4 gifts with every order</div>'):]
    return head + h[grid:pos] + ins + h[pos:], 1

def transform(h, img, values=True):
    notes = []
    # 1. blokken
    n_blocks = 0
    for kind, fn in (('row', do_row), ('grid', do_grid)):
        while True:
            ms = [m for m in re.finditer(r'data-gifts5="%s"' % kind, h)]
            todo = None
            for m in ms:
                s = h.rfind('<td', 0, m.start()); e = elem_end(h, s, 'td')
                if 'gift-cookbook.jpg' not in h[s:e]: todo = (s, e); break
            if not todo: break
            s, e = todo; b = fn(h[s:e], img, None)
            if values: b = re.sub(r'(data-gift="gift-mystery.jpg".*?</td>)', lambda m: mystery_values(m.group(1)), b, flags=re.S)
            b = b.replace('data-gifts5="%s"' % kind, 'data-gifts5="%s" data-gifts-n="5"' % kind, 1)
            h = h[:s] + b + h[e:]; n_blocks += 1; notes.append(kind)
    if 'max-width:270px' in h and 'alt="Chance to win a PFAS water filter"' in h and 'data-gifts5' not in h:
        h, k = do_cards(h, img, values)
        if k: n_blocks += 1; notes.append('cards')
    # 2. telwoord en totalen in zichtbare copy
    def ft(s):
        s = COUNT.sub(five, s)
        return totals(s) if values else s
    h = map_text(h, ft, ft)
    return h, n_blocks, notes

def audit(before, after):
    """Restpunten: wat het script niet kon of wat met de hand moet."""
    issues = []
    vis = []
    map_text(after, lambda s: vis.append(s) or s, lambda s: vis.append(s) or s)
    vis = ' '.join(vis)
    if re.search(r'(?i)\b(4|four)\b(?:\s|&nbsp;|\u00a0)+(?:free(?:\s|&nbsp;)+)?gifts', vis): issues.append('telwoord 4 nog zichtbaar')
    if re.search(r'(?i)purifier|free filter', vis) and not re.search(r'(?i)purifier|free filter', before): issues.append('verboden filterwoord')
    for d in ('\u2013', '\u2014'):
        if after.count(d) > before.count(d): issues.append('streepje toegevoegd')
    n_filter = after.count('alt="Chance to win a PFAS water filter"')
    n_cook = after.count('alt="Favorites Cookbook"')
    if n_cook < n_filter: issues.append('gift-blok zonder cookbook (%d filter, %d cookbook)' % (n_filter, n_cook))
    hrefs_b = sorted(set(re.findall(r'href="([^"]*)"', before))); hrefs_a = sorted(set(re.findall(r'href="([^"]*)"', after)))
    if hrefs_b != hrefs_a: issues.append('links gewijzigd')
    return issues

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('indir'); ap.add_argument('outdir')
    ap.add_argument('--cookbook-img', required=True, help='Klaviyo-gehoste URL van gift-cookbook.jpg (320x320)')
    ap.add_argument('--no-values', action='store_true', help='totaal en mystery-bedrag niet aanpassen')
    ap.add_argument('--report', default=None)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    rep = {'ok': {}, 'unchanged': [], 'manual': {}}
    for f in sorted(os.listdir(a.indir)):
        if not f.endswith('.html'): continue
        h = open(os.path.join(a.indir, f), encoding='utf-8').read(); t = f[:-5]
        try:
            out, nb, notes = transform(h, a.cookbook_img, not a.no_values)
            again, _, _ = transform(out, a.cookbook_img, not a.no_values)
            if again != out: raise ValueError('niet idempotent')
            iss = audit(h, out)
            if iss: raise ValueError('; '.join(iss))
        except Exception as e:
            rep['manual'][t] = str(e); continue
        if out == h: rep['unchanged'].append(t); continue
        open(os.path.join(a.outdir, f), 'w', encoding='utf-8').write(out)
        rep['ok'][t] = {'blocks': notes, 'count_edits': len(COUNT.findall(' '.join(re.findall(r'>([^<]*)<', h))))}
    s = json.dumps(rep, indent=1, ensure_ascii=False)
    if a.report: open(a.report, 'w').write(s)
    print('ok %d, ongewijzigd %d, handwerk %d' % (len(rep['ok']), len(rep['unchanged']), len(rep['manual'])))
    for t, e in rep['manual'].items(): print('  HANDWERK', t, e)

if __name__ == '__main__':
    main()
