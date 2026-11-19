"""PP v5: productgegevens. Basis = post-purchase-viewed/_tools/ppv_catalog.py (zelfde sleutels, prijzen Shopify 19 nov, bundel-inhoud,
tracker-eigenschappen ppv_vr_<key>), plus het deksel voor PP4 en per kaart de uitsnede, kanteling en tint."""
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../post-purchase-viewed/_tools')))
from ppv_catalog import P, BYKEY, SET12, OWN_MATCH, SO  # noqa: E402,F401

LID = dict(key='lid', t='Z', name='Stainless Steel Lid', handle='stainless-steel-lid', line='Pick the same diameter as your pan. Steams, melts, stops the splatter.',
           price=59, frm=True, us=False)
ALL = {p['key']: p for p in P} | {'lid': LID}
# 6-Pcs-regel zonder inches, want in PP4 staat de kaart ook buiten de VS
ALL['s06'] = dict(ALL['s06'], line='Mini, Small and Large pans, each with a fitted lid.')

# key -> (uitsnede, rotatie in graden, max breedte, max hoogte) op de kaart van 1120 x 540
CARDS = {  # 19 nov avond: product 70 tot 80% van de kaartbreedte (Floris), 3/4-aanzicht waar mogelijk
    'e34': ('e34', 0, 960, 600), 'fhp': ('fhp', 0, 1000, 560), 'kn8': ('kn8', 0, 860, 600), 'cmp': ('cmp', 0, 900, 600),
    'csp': ('csp', 0, 920, 600), 's06': ('s06', -4, 820, 600), 'rst': ('rst', -3, 840, 600), 'p22': ('p22', 0, 820, 600),
    'lrg': ('lrg', -8, 800, 610), 'piz': ('piz', -4, 820, 600), 'ute': ('ute', 0, 800, 600), 'std': ('std', -8, 800, 610),
    'crp': ('crp34', -2, 900, 600), 'sml': ('sml', -8, 780, 600), 'min': ('min', -8, 760, 590), 'dep': ('dep34', -2, 900, 600),
    'wok': ('wok34', -2, 900, 600), 'brd': ('brd', -6, 720, 610), 'lid': ('lid', -3, 820, 590),
}
_T = ['#F3E3D3', '#E4E7DF', '#E8E1EA', '#E2E8EC', '#EFE6D6']
TINT = {k: _T[i % len(_T)] for i, k in enumerate(CARDS)}
