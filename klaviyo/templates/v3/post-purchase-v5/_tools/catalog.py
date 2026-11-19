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
CARDS = {
    'e34': ('e34', 0, 900, 440), 'fhp': ('fhp', 0, 940, 400), 'kn8': ('kn8', 0, 760, 450), 'cmp': ('cmp', 0, 860, 450),
    'csp': ('csp', 0, 900, 440), 's06': ('s06', -4, 640, 450), 'rst': ('rst', -3, 640, 430), 'p22': ('p22', 0, 680, 450),
    'lrg': ('lrg', -10, 560, 450), 'piz': ('piz', -4, 600, 440), 'ute': ('ute', 0, 620, 450), 'std': ('std', -10, 540, 450),
    'crp': ('crp', -4, 980, 360), 'sml': ('sml', -10, 520, 430), 'min': ('min', -10, 480, 410), 'dep': ('dep', -3, 960, 430),
    'wok': ('wok', -3, 960, 440), 'brd': ('brd', -6, 520, 450), 'lid': ('lid', -3, 560, 420),
}
_T = ['#F3E3D3', '#E4E7DF', '#E8E1EA', '#E2E8EC', '#EFE6D6']
TINT = {k: _T[i % len(_T)] for i, k in enumerate(CARDS)}
