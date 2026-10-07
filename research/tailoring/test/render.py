"""Rendert een uitgevouwen Klaviyo-template met Django (Klaviyo-achtige syntax) op een voorbeeld-event.
Gebruik: python3 render.py <expanded.html> <event.json> <uit.html> <img-map> <shared-map> [profiel.json]"""
import sys, json, re, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pylib'))  # pip install --target research/tailoring/test/pylib django==4.2
import django
from django.conf import settings
settings.configure(TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','OPTIONS':{'libraries':{'kl':'kltags'},'builtins':['kltags']}}])
django.setup()
from django.template import engines
src, evf, out, img, shared = sys.argv[1:6]
h = open(src).read()
h = h.replace('{{IMG}}', img).replace('{{SHARED}}', shared)
ev = json.load(open(evf))
ctx = {'event': ev, 'first_name': 'Sarah', 'organization': {'name': "Siraat's Kitchen", 'full_address': '[address]'}, 'person': {}}
t = engines['django'].from_string(h)
open(out, 'w').write(t.render(ctx))
print('ok', out)
