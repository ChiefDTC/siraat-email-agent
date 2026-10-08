"""v5-controles (8 okt 2026): testcontexten per markt en de inhoudsregels voor internationale klanten.
Gebruikt door research/tailoring/test/v5_blocks.py (alle v5-bouwstenen, hard) en scripts/qa_render.py (alle mails).

Markten in de tests: US, UK, AU, CA, SG, EU (DE) en onbekend ('XX' = geen enkel signaal).
Per signaal (scripts/v5lib.py FLOWSIG) zet market_ctx het juiste veld: verzendland (order), _ip_country_code (cart),
presentment_currency + profielland (checkout), profielland (browse, profile)."""
import re, copy, html as H

MARKETS = ['US', 'UK', 'AU', 'CA', 'SG', 'EU', 'XX']
ISO = {'US': 'US', 'UK': 'GB', 'AU': 'AU', 'CA': 'CA', 'SG': 'SG', 'EU': 'DE', 'XX': ''}
CUR = {'US': 'USD', 'UK': 'GBP', 'AU': 'AUD', 'CA': 'CAD', 'SG': 'SGD', 'EU': 'EUR', 'XX': ''}
NAME = {'US': 'United States', 'UK': 'United Kingdom', 'AU': 'Australia', 'CA': 'Canada', 'SG': 'Singapore', 'EU': 'Germany', 'XX': ''}
SYM = {'UK': '£', 'AU': 'A$', 'CA': 'C$', 'SG': 'S$', 'EU': '€'}
US_ONLY_WORDS = ['12-piece', '12-Piece', '12-PIECE', '12 pieces', 'Roasting Pan', 'roasting pan', 'saucepan', 'stockpot', 'Just Everything',
                 '2 pans + 2 lids', 'Pro Duo: 2 pans', '34 pieces']

def market_ctx(sig, m, ev=None, person=None):
    """Event en profiel voor markt m bij signaal sig. ev/person: basis (wordt gekopieerd)."""
    ev = copy.deepcopy(ev or {}); p = dict(person or {})
    if sig == 'order':
        ex = ev.setdefault('extra', {}); ex['shipping_address'] = dict(ex.get('shipping_address') or {}, country_code=ISO[m])
        if CUR[m]: ex['presentment_currency'] = CUR[m]
    elif sig == 'cart':
        ev['_ip_country_code'] = ISO[m]; ev['$currency'] = CUR[m] or 'USD'
    elif sig == 'checkout':
        ex = ev.setdefault('extra', {}); ex['presentment_currency'] = CUR[m]
        if m != 'XX': p['Country'] = NAME[m]
    elif sig in ('browse', 'profile'):
        if m != 'XX': p['Country'] = NAME[m]
        if sig == 'browse' and m == 'XX': ev.pop('Price', None)
    return ev, p

def text(h):
    h = re.sub(r'<style.*?</style>|<!--.*?-->', ' ', h, flags=re.S)
    h = re.sub(r'<div style="display:none;[^"]*">.*?</div>', ' ', h, count=1, flags=re.S)   # preheader
    return H.unescape(re.sub(r'<[^>]+>', ' ', h))

USD = re.compile(r'(?<![A-Z])\$\s?\d')
INCH = re.compile(r'\d(?:\.\d)?\s?(?:″|"|”|-inch\b| inch\b|-in\b)')

def market_problems(rendered, m, strict_scope=None):
    """Inhoudsfouten voor markt m in een gerenderde mail. strict_scope: alleen deze HTML-delen controleren (v5-blokken)."""
    F = []
    parts = strict_scope if strict_scope is not None else [rendered]
    for part in parts:
        t = text(part)
        if m != 'US':
            for x in USD.finditer(t): F.append('USD-bedrag buiten de US (%s): %s' % (m, t[max(0, x.start() - 30):x.end() + 10].strip()))
            for w in US_ONLY_WORDS:
                if w in t: F.append('US-only product buiten de US (%s): %s' % (m, w))
        if m not in ('US', 'XX'):
            for x in INCH.finditer(t): F.append('inch buiten de US (%s): %s' % (m, t[max(0, x.start() - 25):x.end() + 5].strip()))
        if m == 'XX':   # onbekend: inch alleen tussen haakjes achter cm, bv. "28 cm (11″)"
            t2 = re.sub(r'\d+ cm \(\d+(?:\.\d)?\u2033\)', ' ', t)
            for x in INCH.finditer(t2): F.append('inch zonder cm bij onbekende markt: %s' % t2[max(0, x.start() - 25):x.end() + 5].strip())
    return F

def v5_parts(rendered):
    """De gerenderde v5-blokken (gifts5, reviews3, bundle, xsell) als losse HTML-stukken."""
    out = []
    for attr in ('data-gifts5', 'data-reviews3', 'data-xsell'):
        for mo in re.finditer(r'<td[^>]*%s=' % attr, rendered):
            out.append(_cell(rendered, mo.start()))
    for mo in re.finditer(r'<td data-bundle=', rendered):
        out.append(rendered[mo.start():rendered.find('</table>', mo.start())])
    return out

def _cell(h, i):
    """Van de <td> op positie i tot de bijbehorende </td> (telt geneste td's)."""
    depth = 0
    for mo in re.finditer(r'<td\b|</td>', h[i:]):
        depth += 1 if mo.group(0) == '<td' else -1
        if depth == 0: return h[i:i + mo.end()]
    return h[i:]

def gifts_problems(rendered):
    F = []
    for mo in re.finditer(r'<td[^>]*data-gifts5="(\w+)"', rendered):
        c = _cell(rendered, mo.start())
        for img in ('gift-shipping.jpg', 'gift-ebook.jpg', 'gift-mystery.jpg', 'gift-filter.jpg'):
            if img not in c: F.append('gifts5 (%s) zonder %s' % (mo.group(1), img))
    if re.search(r'\$\s?70|\$\s?450', text(rendered)) and 'gift-shipping.jpg' not in rendered:
        F.append('gift-bedrag zonder gift-beelden')
    return F

def review_problems(rendered):
    F = []
    if 'data-rev="R017' in rendered or 'Marilyn B.' in rendered or 'I followed your directions' in rendered:
        F.append('R017 (Marilyn B.) in de mail')
    return F

def xsell_shown(rendered):
    return re.findall(r'data-xs="([\w-]+)"', rendered)
