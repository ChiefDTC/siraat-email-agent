"""Lokale preview: rendert out/<mail>.html met Django + Klaviyo-tags (research/tailoring/test/kltags.py) per CASES -> previews/<mail>--<id>.html"""
import os, sys, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')); REPO = os.path.abspath(os.path.join(ROOT, '../../../..'))
T = os.path.join(REPO, 'research/tailoring/test'); sys.path.insert(0, T); sys.path.insert(0, os.path.join(T, 'pylib')); sys.path.insert(0, os.path.dirname(__file__))
import django
from django.conf import settings
settings.configure(TEMPLATES=[{'BACKEND': 'django.template.backends.django.DjangoTemplates', 'OPTIONS': {'libraries': {'kl': 'kltags'}, 'builtins': ['kltags']}}]); django.setup()
from django.template import engines
from ctx import CASES
os.makedirs(os.path.join(ROOT, 'previews'), exist_ok=True)
only = sys.argv[1:]
for mail, cid, title, c in CASES:
    if only and mail not in only: continue
    h = open(os.path.join(ROOT, 'out', mail + '.html')).read()
    ctx = dict(c, first_name='Sam', organization={'name': "Siraat's Kitchen", 'full_address': '[address]'})
    out = engines['django'].from_string(h).render(ctx)
    assert '{%' not in out and '{{' not in out, (mail, cid)
    open(os.path.join(ROOT, 'previews', f'{mail}--{cid}.html'), 'w').write(out)
    print('ok', mail, cid)
