"""US vr 27 nov 18:00 (vervangt HS Email 17 US): korte brief 'Before midnight', set $499 via automatische korting (US-markt).
Vaste header/footer. Gebruik: python3 -I build_us_1800_499.py"""
import os, re
T = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(T)
src = open(os.path.join(T, 'build.py')).read().split("os.makedirs(os.path.join(T, '.preview')")[0]
g = {'__file__': os.path.join(T, 'build.py')}; exec(src, g)
p, a, row, signoff, shell, FIRST, MUTED = (g[k] for k in ('p','a','row','signoff','shell','FIRST','MUTED'))
def L(path, c): return f'https://siraatskitchen.com/discount/BF499?redirect={path}&utm_source=klaviyo&utm_medium=email&utm_campaign=bf-1127-us-1800&utm_content={c}'
SET = '/products/titanium-hammered-cookware-set'
body = (p(f'Hey {FIRST},') +
    p('Quick one. At midnight ET I switch off this morning&rsquo;s prices. My team was not thrilled I turned them on in the first place.') +
    p(f'Until then the 12-piece set is <b>$499</b> instead of $649. That&rsquo;s 3 pans, 3 pots and 6 lids, and the only way to get our hammered titanium pots. Already applied (code BF499): {a("get the 12-piece set for $499", L(SET,"letter-link"))}.') +
    p('If it&rsquo;s been sitting in your cart all week, tonight is the night.') +
    signoff() +
    p(f'P.S. 30-day returns and a 75-year warranty. {a("The $499 price ends at midnight", L(SET,"ps-link"))}.', 15, 23, MUTED, '18px 0 0 0'))
h = shell('Before midnight', 'At midnight the $499 set is gone.', row(body, '32px 40px 36px 40px'))
assert '—' not in h
open(os.path.join(C, 'us-1800-499.html'), 'w').write(h)
print('ok', len(h))
