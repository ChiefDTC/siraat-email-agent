"""Rendert de huidige Klaviyo-templates (lokaal opgehaald, alleen GET) naar HTML met voorbeeldprofiel (US).
Gebruik: python3 render_current.py <map met {templateid}.html> <uitvoermap> <templateid> ...
Echte BF-code wordt vervangen door BFCODE vóór het renderen (publieke repo)."""
import sys, re, os
import django
from django.conf import settings
settings.configure(TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','OPTIONS':{'builtins':[__name__]}}])
django.setup()
from django import template
from django.template import Template, Context, Engine
register = template.Library()

@register.filter
def lookup(d, k):
    try: return d.get(k, '')
    except Exception: return ''
@register.filter
def multiply(a, b):
    try: return float(a) * float(b)
    except Exception: return ''
@register.filter
def divide(a, b):
    try: return float(a) / float(b)
    except Exception: return ''
@register.filter
def ceil(a):
    import math
    try: return math.ceil(float(a))
    except Exception: return ''
@register.filter
def index(a, i):
    try: return a[int(i)]
    except Exception: return ''
@register.filter
def format_date_string(a, f=''): return 'Nov 30'
@register.filter
def days_later(a, n=0): return 'Nov 30'
for t, val in [('today', 'Nov 8'), ('manage_preferences_link', '#'), ('unsubscribe_link', '#'),
               ('web_view_link', '#'), ('unsubscribe', '#'), ('coupon_code', 'K3X7-SAMPLE')]:
    register.simple_tag(name=t, func=(lambda v: (lambda *a, **k: v))(val))

ENG = Engine(builtins=[__name__], libraries={}, string_if_invalid='', autoescape=False)
CTX = {'first_name': 'there',
       'person': {'first_name': 'there', 'email': 'sample@example.com', '$country': 'United States',
                  'Country': 'United States', 'country': 'United States'},
       'organization': {'name': 'Siraat', 'url': 'https://siraatskitchen.com'}, 'event': {}}

def clean(h):
    h = re.sub(r'BF-[A-Z0-9]{4,8}', 'BFCODE', h)          # echte BF-code nooit in uitvoer
    h = re.sub(r'{%\s*catalog.*?%}.*?{%\s*endcatalog\s*%}', '', h, flags=re.S)
    h = re.sub(r'{%\s*(today|coupon_code)[^%]*%}', lambda m: '{% ' + m.group(1) + ' %}', h)
    return h

def main():
    src, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    for tid in sys.argv[3:]:
        h = open(os.path.join(src, tid + '.html')).read()
        h = clean(h)
        try:
            r = ENG.from_string(h).render(Context(CTX))
        except Exception as e:
            print('FOUT', tid, str(e)[:120]); r = re.sub(r'{[{%].*?[%}]}', '', h, flags=re.S)
        r = re.sub(r'BF-[A-Z0-9]{4,8}', 'BFCODE', r)
        open(os.path.join(out, tid + '.html'), 'w').write(r)
main()
