"""BF-W1 A · 12pcs top (US) · TEST (19 nov 2026). NIET LIVE.
Bron: live template Y8QqZB (Floris' ontwerp, opgeslagen als Y8QqZB-bron.html). Alleen het 2 Pans + 2 Lids aanbodblok
is vervangen door een blok in dezelfde stijl: VS = Cookware Set 12-Pcs ($649, was $2,047, 68% off), rest = Pan Set 6-Pcs
($299, was $997, 70% off). Geen nep-urgentie in het nieuwe blok ('today only', 'back to ... at midnight' en 'Claim before
it's gone' zijn weggelaten). De lagere kaart van hetzelfde product staat in die tak niet meer in de mail.
Landconditie zoals scripts/v5lib.py (profiel): person.Country, terugval person|lookup:'country_code'; onbekend = niet-VS.
Gebruik: python3 -I build.py -> bf-w1-a-12pcs-top.html (Klaviyo) + preview-us.html / preview-int.html (conditie opgelost)
"""
import os, re
D = os.path.dirname(os.path.abspath(__file__))
h = open(os.path.join(D, 'Y8QqZB-bron.html')).read()
W = "{% with mpc=person.Country mpcc=person|lookup:'country_code' %}{% if mpc == 'United States' or mpc == 'US' or not mpc and mpcc == 'US' %}"
IFUS = '<!--' + W + '-->'; ELSE = '<!--{% else %}-->'; END = '<!--{% endif %}{% endwith %}-->'
# ---- 1. aanbodblok
i = h.find('62% off today only'); s = h.rfind('<tr>', 0, h.rfind('<tr>', 0, i))
j = h.find("Claim before it's gone"); e = h.find('</tr>', h.find('</table>', j)) + 5
blk = h[s:e]
assert blk.count('$664') == 2 and '2-pans-and-2-lids' in blk
def offer(badge, name, was, now, sub, label, handle):
    b = blk.replace('62% off today only', badge).replace('2 Pans + 2 Lids', name)
    b = b.replace('$664\n', was + '\n', 1).replace('$249', now)
    b = b.replace('Price goes back to $664 at midnight', sub)
    b = b.replace("Claim before it's gone", label).replace('/products/2-pans-and-2-lids', '/products/' + handle)
    assert '$664' not in b and 'midnight' not in b
    return b
B12 = offer('68% off', 'Cookware Set, 12\u00a0Pcs', '$2,047', '$649', '3 pans, 3 pots, 6 lids', 'Get the 12-piece set', 'titanium-hammered-cookware-set')
B6 = offer('70% off', 'Pan Set, 6\u00a0Pcs', '$997', '$299', '3 pans and 3 fitted lids', 'Get the 6-piece set', 'titanium-hammered-pan-set-with-lids-6-pcs')
h = h[:s] + IFUS + '\n' + B12 + ELSE + '\n' + B6 + END + '\n' + h[e:]
# ---- 2. kaarten: rij met de 6-Pcs kaart en rij met de 12-Pcs kaart
def row(key):
    k = h.find(key); a = h.rfind('<tr>\n<td class="cp"', 0, k)
    # einde: de </tr> die de buitenste cp-rij sluit = eerste '</table>\n</td>\n</tr>' na de laatste img van de kaart
    im = h.find('<img', h.find('class="ii"', k)); z = h.find('</table>\n</td>\n</tr>', im) + len('</table>\n</td>\n</tr>')
    return a, z
a6, z6 = row('>Pan Set, 6\u00a0Pcs</a>'); r6 = h[a6:z6]
a12, z12 = row('>Cookware Set, 12\u00a0Pcs</a>'); r12 = h[a12:z12]
assert r6.count('class="cp"') == 1 and r12.count('class="cp"') == 1 and '12\u00a0Pcs' not in r6 and '6-pcs' not in r12
# 12-Pcs kaart alleen buiten de VS (in de VS staat hij al bovenaan), 6-Pcs kaart alleen in de VS
h = h[:a12] + IFUS + ELSE + r12 + END + h[z12:]
h = h[:a6] + IFUS + r6 + END + h[z6:]
assert h.count(IFUS) == 3 and h.count(END) == 3 and '\u2014' not in h
open(os.path.join(D, 'bf-w1-a-12pcs-top.html'), 'w').write(h)
# previews met opgeloste conditie
def solve(x, us):
    pat = re.escape(IFUS) + r'(.*?)(?:' + re.escape(ELSE) + r'(.*?))?' + re.escape(END)
    return re.sub(pat, lambda m: (m.group(1) if us else (m.group(2) or '')), x, flags=re.S)
for nm, us in (('us', True), ('int', False)):
    x = solve(h, us); assert '{% if' not in x and '{% with' not in x
    x = re.sub(r'\{%.*?%\}', '#', x)
    open(os.path.join(D, f'preview-{nm}.html'), 'w').write(x)
print('ok', len(h))
