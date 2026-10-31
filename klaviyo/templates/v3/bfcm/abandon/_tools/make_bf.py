"""Maakt BF 2026-varianten van de live abandonment-mails in klaviyo/templates/v3/bfcm/abandon/ (bronnen blijven ongewijzigd)."""
import re, os, sys
R = '/home/user/siraat-email-agent/klaviyo/templates/v3'
OUT = R + '/bfcm/abandon'
SRC = {  # naam: (map, signaal, code-pool of None, subject A, subject B, preview)
 'c1': ('checkout', 'checkout', None, 'Your cart, at Black Friday prices', 'Black Friday is live. Your cart is saved.', 'An extra 10% on top of the sale, applied with the button. Your 4 gifts are still pending.'),
 'c2': ('checkout', 'checkout', None, 'Tested, and now priced for Black Friday', 'Report no. 25895, at Black Friday prices', 'Why I had our pan lab-tested. Plus an extra 10% on top of the sale.'),
 'c2-acc': ('checkout', 'checkout', None, 'Yours, or a gift? Priced for Black Friday.', 'A Black Friday gift? It is still in your cart.', 'An extra 10% on top of Black Friday prices, applied with the button.'),
 'c3-s': ('checkout', 'checkout', None, 'Your set, priced for Black Friday', 'The complete collection, plus an extra 10%', 'Every piece, the same tested titanium surface. An extra 10% on top of the sale.'),
 'c3-p': ('checkout', 'checkout', None, 'One pan, or three? Black Friday is live.', 'Built to last. Priced for Black Friday.', 'Most of our 100,000+ customers start with one. An extra 10% on top of the sale.'),
 'c3-acc': ('checkout', 'checkout', None, 'The pan we made after the board, priced for Black Friday', 'Still cooking on a coated pan?', 'We started with cutting boards too. Black Friday is live, plus an extra 10%.'),
 'c4': ('checkout', 'checkout', 'C4_10_48H', 'Your own 10%, on top of Black Friday prices', '48 hours: your 10% on top of the sale', 'Already applied to your cart. In 48 hours we remove it, then the regular sale price applies.'),
 'c4-nocode': ('checkout', 'checkout', None, 'Last email about your Black Friday cart', '"They honored the warranty"', 'Black Friday prices, an extra 10% with the button, and then we stop reminding you.'),
 'k1-v2': ('cart', 'cart', None, 'Your cart, at Black Friday prices', 'Black Friday is live. We saved your cart.', 'An extra 10% on top of the sale, applied with the button.'),
 'k1-acc': ('cart', 'cart', None, 'Picked it out? Black Friday is live.', 'Your cart and an extra 10%, saved', 'An extra 10% on top of Black Friday prices, applied with the button.'),
 'k2-new': ('cart', 'cart', None, '15 coated pans, or one. Priced for Black Friday.', 'The pan you keep replacing, priced for Black Friday', 'Our warranty runs 75 years. Here is the math, with an extra 10% on top of the sale.'),
 'k2-returning': ('cart', 'cart', None, 'Adding to your Siraat kitchen? Black Friday is live.', 'Same pan, Black Friday price, an extra 10%', 'You know how it works. Your cart is saved, with an extra 10% on top of the sale.'),
 'k3': ('cart', 'cart', 'K3_10_48H', 'Your own 10%, on top of the sale, for 48 hours', "We're removing your cart's 10% in 48 hours", 'Already applied, on top of Black Friday prices. In 48 hours we remove the code.'),
 'k3-nocode': ('cart', 'cart', None, "What if it's not for you?", 'Last email about your Black Friday cart', 'Then it goes back unused within 30 days. An extra 10% on top of the sale, with the button.'),
 'b1': ('browse', 'browse', None, 'The pan you looked at, priced for Black Friday', 'Lab-tested, plus an extra 10% off', 'Report no. 25895. Plus an extra 10% on top of Black Friday prices.'),
 'b1-acc': ('browse', 'browse', None, 'Looked twice? Black Friday is live.', "What it's made of, plus an extra 10%", 'An extra 10% on top of Black Friday prices, applied with the button.'),
 'b2-clicked': ('browse', 'browse', 'B2_10_48H', 'Your own 10%, on top of Black Friday prices', '48 hours: your 10% on the pan you went back to', 'Already applied. In 48 hours we remove it, then the regular sale price applies.'),
 'b2-clicked-nocode': ('browse', 'browse', None, '"I ordered one pan to try it out"', '100,000+ people started with one. Black Friday is live.', 'Sunny C. started with one. An extra 10% on top of the sale, with the button.'),
 'b2-notclicked': ('browse', 'browse', None, 'Skeptical? So were they.', 'Week one, in their words. Priced for Black Friday.', 'One thought it was a scam. One is on her fourth pan. An extra 10% on top of the sale.'),
 'a1': ('site', 'profile', None, 'Four eggs or five? Black Friday is live.', 'Which pan? Priced for Black Friday.', 'Four sizes, one titanium surface. An extra 10% on top of Black Friday prices.'),
 'a2': ('site', 'profile', None, 'Where 100,000+ customers started, priced for Black Friday', 'The first pan, priced for Black Friday', 'Most people start with one pan. An extra 10% on top of Black Friday prices.'),
 'tp-b1': ('browse-tp', None, None, 'The pan you looked at, priced for Black Friday', 'Three questions to ask before Black Friday', 'Here it is again, with the lab report, the 75-year warranty and an extra 10% on top of the sale.'),
 'tp-b1-acc': ('browse-tp', None, None, 'Looked twice? Black Friday is live.', 'We started with the cutting board', "Here it is again. What it's made of, and an extra 10% on top of the sale."),
 'tp-b2-clicked': ('browse-tp', None, 'B2_10_48H', 'Your own 10%, on top of Black Friday prices', '48 hours: your 10% on the one you went back to', 'Already applied with the button. In 48 hours we remove it, then the regular sale price applies.'),
 'tp-b2-clicked-nocode': ('browse-tp', None, None, '"I ordered one pan to try it out"', 'Two promises, before Black Friday ends', 'If you change your mind, or if something is wrong. Both are covered. Extra 10% on top of the sale.'),
 'tp-b2-notclicked': ('browse-tp', None, None, 'Why we can cover this pan for 75 years', 'Built to last. Priced for Black Friday.', "Nothing on it to wear off. That's why the warranty is this long. Extra 10% on top of the sale."),
}
TOPBAR = '{{BLOCK:bf-topbar text="BLACK FRIDAY SALE IS LIVE"}}'
DEAL = '{{BLOCK:bf-deal pad="22px 44px 0 44px" headline="Extra 10%% off" detail="%s"}}'
ANCH = [r'\{\{BLOCK:cart\b', r'<!-- PRODUCTKAART', r'<!-- PRODUCT \(', r'<!-- MAATKIEZER', r'\{\{BLOCK:productcard\b']
ENC = lambda q: q.replace('%', '%25').replace('&', '%26').replace('=', '%3D')
report = []
for name, (d, sig, pool, sa, sb, pv) in SRC.items():
    h = open('%s/%s/%s.html' % (R, d, name)).read()
    log = []
    # 1 kopcommentaar
    first = h.split('\n', 1)[0]
    assert first.startswith('<!--'), name
    assum = 'Aanbod Floris 31 okt: Black Friday Sale up to 70% off (collectie black-friday-sale) plus extra 10% met code BFCODE (placeholder, echte code pas bij upload); oude publieke code vervangen door BFCODE; 4 gifts nog geldig aangenomen; vaste prijzen uit de v5-prijslijst weggelaten (kloppen niet met BF-prijzen)'
    if pool:
        assum += '; codemail: unieke code %s (ook 10%%, echt 48 uur) blijft in plaats van BFCODE, een code per order; besluit Floris' % pool
    elif '-nocode' in name:
        assum += '; nocode-mail krijgt nu BFCODE (abandonment krijgt de extra 10%%), weghalen als cooldown codevrij moet blijven'
    newc = '<!-- BF 2026 VARIANT (voorbeeld, niet live, 31 okt 2026) | BRON: klaviyo/templates/v3/%s/%s.html | SUBJECT_A: %s | SUBJECT_B: %s | PREVIEW: %s | AANNAMES: %s | WIJZIGINGEN: zie bfcm/abandon/NOTES.md -->' % (d, name, sa, sb, pv, assum)
    h = newc + '\n' + h.split('\n', 1)[1]  # originele bronkop weg (noemde HI10); zie de bron voor de oude onderwerpen
    # 2 marktsignaal (de map 'abandon' kent de builder niet)
    if sig and 'MARKET-SIGNAL' not in h:
        h = h.replace('<!DOCTYPE html>', '<!-- MARKET-SIGNAL: %s -->\n<!DOCTYPE html>' % sig, 1)
    # 3 preheader
    h, n = re.subn(r'(<body\b[^>]*>\s*<div style="display:\s*none;[^"]*">)(.*?)(</div>)', lambda m: m.group(1) + pv + m.group(3), h, count=1, flags=re.S)
    assert n == 1, name
    # 4 topbar in plaats van codebar
    h, n = re.subn(r'^\{\{BLOCK:codebar\b.*\}\}[ \t]*$', TOPBAR, h, count=1, flags=re.M)
    if n: log.append('codebar vervangen door bf-topbar')
    else:
        h = h.replace('{{HEADER}}', TOPBAR + '\n{{HEADER}}', 1); log.append('bf-topbar boven {{HEADER}} (had geen codebar)')
    # 5 offer-blok weg in codemails (deal neemt het over)
    if pool:
        h, n = re.subn(r'^\{\{BLOCK:offer\b.*\}\}[ \t]*\n', '', h, count=1, flags=re.M)
        assert n == 1, name
        log.append('offer-blok (eigen code + deadline) vervangen door bf-deal')
        detail = "On top of Black Friday prices, up to 70%% off. Applied with the button, or use your own code {%% coupon_code '%s' %%} at checkout, until {{DATE:2:l, F j}}." % pool
    else:
        detail = 'On top of Black Friday prices, up to 70% off. Applied with the button, or use code BFCODE at checkout.'
    # 6 deal boven het product/cart-blok
    pos = None
    for a in ANCH:
        m = re.search(a, h)
        if m: pos = m.start(); log.append('bf-deal boven ' + a.replace('\\', '')); break
    assert pos is not None, name
    h = h[:pos] + DEAL % detail + '\n' + h[pos:]
    # 7 knoppen: rust cta -> bf-cta geel op cream
    h, n = re.subn(r'\{\{BLOCK:cta ', '{{BLOCK:bf-cta bg="#F8F7F2" ', h)
    log.append('%d rust-knoppen naar bf-cta' % n)
    # 8 links naar /discount/HI10?redirect=<doel> (alleen winkel-links zonder code; /pages/ en checkout-links blijven)
    cnt = [0]
    def fix(m):
        attr, path, q = m.group(1), m.group(2), m.group(3)
        if path.startswith('/discount/') or path.startswith('/pages/') or 'checkout' in path: return m.group(0)
        cnt[0] += 1
        return '%s="https://siraatskitchen.com/discount/BFCODE?redirect=%s%s"' % (attr, path or '/', ('%3F' + ENC(q)) if q else '')
    if not pool:
        body_start = h.find('{{HEADER}}'); foot = h.find('{{FOOTER}}')
        mid = re.sub(r'\b(href|url)="https://siraatskitchen\.com([^"?]*)(?:\?([^"]*))?"', fix, h[body_start:foot])
        h = h[:body_start] + mid + h[foot:]
    log.append('%d winkel-links via /discount/BFCODE?redirect=' % cnt[0])
    # 9 HI10 overal in de body naar BFCODE (links, &discount=, tekst); bronkop blijft
    top, body = h.split('<!DOCTYPE html>', 1)
    n = body.count('HI10'); body = body.replace('HI10', 'BFCODE'); h = top + '<!DOCTYPE html>' + body
    log.append('%d keer HI10 -> BFCODE' % n)
    # 9b checkout-links zonder code (nocode-mails) krijgen &discount=BFCODE
    if not pool:
        h, n = re.subn(r"(responsive_checkout_url\|default:'[^']*' \}\})&(?!discount=)", r"\1&discount=BFCODE&", h)
        if n: log.append('%d checkout-links kregen &discount=BFCODE' % n)
    # 10 vaste catalogusprijzen (v5-prijslijst) weg: kloppen niet met de BF-saleprijzen
    n0 = len(re.findall(r'\{\{(?:PRICE|WAS|FROM):', h))
    h = re.sub(r'\{\{IF:PRICED\}\}(.*?)(?:\{\{ELSE\}\}(.*?))?\{\{ENDIF\}\}', lambda m: m.group(2) or '', h, flags=re.S)
    h = re.sub(r'\b(now|was)="[^"]*\{\{(?:PRICE|WAS|FROM):[^"]*"', r'\1=""', h)
    left = re.findall(r'.{0,60}\{\{(?:PRICE|WAS|FROM):.{0,30}', h)
    assert not left, (name, left)
    if n0: log.append('%d prijsmacro\'s weggelaten' % n0)
    # 11 fall-sale-taal past niet bij BF: gifts5-urgentie ('Your 4 gifts end when the fall sale ends.') uit, c3-p tekst neutraal
    n = len(re.findall(r'(\{\{BLOCK:gifts5\b[^}]*?) urgency="1"', h))
    h = re.sub(r'(\{\{BLOCK:gifts5\b[^}]*?) urgency="1"', r'\1', h)
    if n: log.append('%d gifts5-urgentieregel (fall sale) uit' % n)
    top, body = h.split('<!DOCTYPE html>', 1)
    b2 = body.replace('alt="The fall sale. ', 'alt="').replace('{{IMG}}/c3p-hero-v5.jpg', '{{IMG}}/c3p-hero-bf.jpg').replace('eyebrow="THE FALL SALE SET"', 'eyebrow="THE 6-PIECE SET"').replace('label="Upgrade to the 6-piece set"', 'label="Get the 6-piece set"').replace('In the fall sale set you pay', 'In the 6-piece set you pay')
    for hh in ('a1-hero', 'a2-hero', 'b1-hero', 'b1acc-hero', 'b2-notclicked-hero'):
        if '{{IMG}}/%s-v5.jpg' % hh in b2:
            b2 = b2.replace('{{IMG}}/%s-v5.jpg' % hh, '{{IMG}}/%s-bf.jpg' % hh); log.append('hero %s-bf.jpg (balk zonder HI10)' % hh)
    if b2 != body: log.append('fall-sale-tekst in body geneutraliseerd')
    h = top + '<!DOCTYPE html>' + b2
    assert chr(0x2014) not in h, name
    open('%s/%s-bf.html' % (OUT, name), 'w').write(h)
    report.append('%s: %s' % (name, '; '.join(log)))
print('\n'.join(report))
