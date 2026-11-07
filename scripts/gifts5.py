"""gifts5.py: van 4 naar 5 gratis gifts in bestaande Klaviyo-templates (HTML in, HTML uit).

Nieuw sinds november 2026 op de site: Mystery gift ($35), Express shipping ($15), Plastic-free e-book ($30),
Favorites Cookbook ($25, nieuw) plus een wekelijkse kans op een PFAS water filter ($450).

Wat het script doet, per template:
  1. Telwoord in zichtbare copy: "4 gifts", "4 free gifts", "four gifts" (ook hoofdletters) wordt 5/five.
     Alleen in tekst en in alt/title-attributen, ook in Outlook-blokken (<!--[if mso]>); nooit in URL's,
     <style>, of Django-code (<!--{% ... %}-->).
  2. Waarden (--values, standaard AAN): mystery $25 -> $35 en totaal "$70 in gifts" -> "$105 in gifts",
     per markt (zie VALUES; buiten de US afgeleid volgens research/v5/01-markten.md sectie 6: USD x koers, afgerond op 5).
  3. Cookbook als vijfde tegel in elk herkend gift-blok, vlak voor de filter (de filter blijft de laatste tegel):
       row   (data-gifts5="row", 4 naast elkaar)  -> 5 naast elkaar, tegels 20 procent, beeld 64 -> 56 px
       grid  (data-gifts5="grid", 2x2 / 4 breed)   -> extra gecentreerde rij met 1 tegel (2+2+1 mobiel, 4+1 desktop)
       cards (pp-complete, kaarten 270 px, 2x2)    -> derde rij met 1 kaart van 50 procent, gecentreerd
     De nieuwe tegel kopieert de e-book-tegel ernaast (zelfde opmaak, zelfde link, zelfde marktketen).
  4. --express (standaard AAN): tegel "Free shipping" heet "Express shipping" (alleen in de shipping-tegel zelf).

Idempotent: een blok met data-gifts-n="5" of het cookbook-beeld wordt overgeslagen; tellingen en bedragen
matchen na de eerste ronde niet meer. Draai het twee keer en vergelijk (--check doet dat zelf).

Gebruik (alleen lokaal, schrijft niets naar Klaviyo):
  python3 -I scripts/gifts5.py IN_DIR OUT_DIR --cookbook-img https://cdn.klaviyomail.com/... [--no-values] [--no-express] [--report r.json]
Templates die het script niet veilig aankan komen in het rapport onder "manual" en worden NIET geschreven.
"""
import argparse, json, os, re, sys

MARKETS = ['US', 'CA', 'UK', 'EU', 'AU', 'NZ', 'SG']
CUR = {'US': '$', 'CA': 'C$', 'UK': '£', 'EU': '€', 'AU': 'A$', 'NZ': 'NZ$', 'SG': 'S$'}
OLD = {  # (ship, ebook, mystery, filter, totaal) zoals live (v5lib.GIFT, 8 okt)
    'US': (15, 30, 25, 450, 70), 'CA': (20, 40, 35, 620, 95), 'UK': (10, 25, 20, 350, 55), 'EU': (15, 30, 25, 410, 70),
    'AU': (20, 45, 35, 660, 100), 'NZ': (25, 50, 45, 820, 120), 'SG': (20, 40, 35, 590, 95)}
# Nieuw: mystery $35 en cookbook $25 (site, nov 2026). Buiten de US: USD x koers (GBP .773, EUR .912, AUD 1.469,
# NZD 1.816, SGD 1.301, CAD 1.374), afgerond op 5. Cookbook $25 = zelfde bedrag als het oude mystery-bedrag.
# AFGELEID, niet uit een Shopify-prijslijst: laten bevestigen door Floris.
MYSTERY = {'US': 35, 'CA': 50, 'UK': 25, 'EU': 30, 'AU': 50, 'NZ': 65, 'SG': 45}
COOKBOOK = {'US': 25, 'CA': 35, 'UK': 20, 'EU': 25, 'AU': 35, 'NZ': 45, 'SG': 35}
TOTAL = {m: OLD[m][0] + OLD[m][1] + MYSTERY[m] + COOKBOOK[m] for m in MARKETS}   # US 105

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
    for m in MARKETS:
        s = re.sub(amt_re(m, OLD[m][4]) + r'(' + SP + r'(?i:in' + SP + r'gifts))', amt(m, TOTAL[m]) + r'\1', s)
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
    for m in MARKETS:
        s = re.sub(amt_re(m, OLD[m][1]) + r'(' + SP + r'value)', amt(m, COOKBOOK[m]) + r'\1', s)
    return s

def mystery_values(s):
    for m in MARKETS:
        s = re.sub(amt_re(m, OLD[m][2]) + r'(' + SP + r'value)', amt(m, MYSTERY[m]) + r'\1', s)
    return s

def express(s):
    s = re.sub(r'Free(<br\s*/?>|\s)shipping', r'Express\1shipping', s)
    return re.sub(r'(alt=")Free shipping', r'\1Express shipping', s)

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
    es, ee = tile_td(block, 'gift-ebook.jpg')
    new = make_tile(block[es:ee], img).replace('width="50%"', 'width="140"', 1)
    new = new.replace('font-family:Inter,Arial,Helvetica,sans-serif;"', 'font-family:Inter,Arial,Helvetica,sans-serif;width:126px;"', 1)
    # buitenste rastertabel: de <table> die de eerste g2-cel omsluit
    g = block.find('class="g2"')
    ts = enclosing_start(block, g, 'table'); te = elem_end(block, ts, 'table')
    row = ('\n<table role="presentation" align="center" cellpadding="0" cellspacing="0" border="0" data-gift5row="1" style="margin:10px auto 0 auto;"><tr>\n'
           + new + '\n</tr></table>')
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
    grid = enclosing_start(h, fs, 'table'); ge = elem_end(h, grid, 'table')
    if h[ge - len('</tr></table>'):ge] != '</tr></table>': raise ValueError('cards: raster eindigt anders')
    ins = ('<tr><td colspan="2" align="center" style="padding:0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
           '<td width="25%" style="font-size:0;line-height:0;">&nbsp;</td>' + card + '<td width="25%" style="font-size:0;line-height:0;">&nbsp;</td></tr></table></td></tr>')
    pos = ge - len('</table>')
    region = h[grid:pos] + ins
    if opt:
        region = re.sub(r'(alt=")Free shipping', r'\1Express shipping', region)
        region = re.sub(r'(font-weight:600;text-align:center;">)Free shipping', r'\1Express shipping', region)
    return h[:grid] + region + h[pos:], 1

def transform(h, img, values=True, exp=True):
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
            if exp:
                ss, se = tile_td(b, 'gift-shipping.jpg'); b = b[:ss] + express(b[ss:se]) + b[se:]
            b = b.replace('data-gifts5="%s"' % kind, 'data-gifts5="%s" data-gifts-n="5"' % kind, 1)
            h = h[:s] + b + h[e:]; n_blocks += 1; notes.append(kind)
    if 'max-width:270px' in h and 'alt="Chance to win a PFAS water filter"' in h and 'data-gifts5' not in h:
        h, k = do_cards(h, img, exp)
        if k: n_blocks += 1; notes.append('cards')
    # 2. telwoord en totalen in zichtbare copy
    def ft(s):
        s = COUNT.sub(five, s)
        return totals(s) if values else s
    h = map_text(h, ft, ft)
    return h, n_blocks, notes

GIFT_IMG = re.compile(r'(?i)alt="[^"]*(PFAS water filter|Mystery gift)[^"]*"')

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
    ap.add_argument('--no-values', action='store_true', help='mystery- en totaalbedragen niet aanpassen')
    ap.add_argument('--no-express', action='store_true', help='"Free shipping"-tegel niet hernoemen')
    ap.add_argument('--report', default=None)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    rep = {'ok': {}, 'unchanged': [], 'manual': {}}
    for f in sorted(os.listdir(a.indir)):
        if not f.endswith('.html'): continue
        h = open(os.path.join(a.indir, f), encoding='utf-8').read(); t = f[:-5]
        try:
            out, nb, notes = transform(h, a.cookbook_img, not a.no_values, not a.no_express)
            again, _, _ = transform(out, a.cookbook_img, not a.no_values, not a.no_express)
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
