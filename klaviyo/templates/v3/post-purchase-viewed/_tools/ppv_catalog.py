"""PP viewed tailored (19 nov 2026, draft). Eén bron voor template, tracker-flows en SCENARIOS.md.

Elke aanbiedbare product heeft een letter (token) en een profieleigenschap ppv_vr_<key> (getal):
  0 of leeg = niet bekeken in 30 dagen, 1 = bekeken in de laatste ~3 dagen, 2 = 3 tot 10 dagen, 3 = 10 tot 30 dagen,
  9 = in bezit (gekocht, los of in een bundel). 9 wordt nooit overschreven door de view-tracker.
Prijzen: Shopify Admin 19 nov 2026 (US). Compare-at alleen bij bevestigde ankers (12-Pcs $2,047, 6-Pcs $997).
"""
CDN = 'https://cdn.shopify.com/s/files/1/0907/0877/1156/files/'
def img(f): return CDN + f + ('&' if '?' in f else '?') + 'width=480&format=jpg'

# key, token, naam in de mail, handle, beeld, regel, US-prijs, 'from'-prijs?, alleen VS?
# volgorde = prioriteit binnen een recentheidsemmer (hoogste orderwaarde eerst)
P = [
 dict(key='e34', t='A', name='The Just Everything Bundle', handle='the-just-everything-bundle-34-pcs', img=img('TitaniumHammeredPanPro_18.webp?v=1791211498'),
      line='34 pieces: the 12-piece set, five specialty pans, boards, utensils and more.', price=1499, frm=False, us=True),
 dict(key='fhp', t='B', name='Full Hammered Pro Edition', handle='full-hammered-pro-edition', img=img('FullHammeredProEdition_3.webp?v=1776602877'),
      line='All four Pan Pro sizes, each with a lid, plus four titanium utensils.', price=799, frm=False, us=False),
 dict(key='kn8', t='C', name='Damascus 67 Layer Knife Set', handle='damascus-67-layer-knife-set-8-piece', img=img('dk67-knife-set-01-lineup-packshot.jpg?v=1794501795'),
      line='Eight knives, made from 67 layers of Damascus steel.', price=499, frm=False, us=True),  # INT-verzending/prijs messen onbekend: [VRAAG FLORIS],
 dict(key='cmp', t='D', name='Titanium Hammered Complete Edition', handle='the-hammered-collection', img=img('TitaniumPan4PCS2.jpg?v=1774026132'),
      line='Pan Pro 11&Prime;, Wok, Deep Pan and Cr&ecirc;pe Pan.', price=495, frm=False, us=False),
 dict(key='csp', t='E', name='Titanium Hammered Cookware Set Pro', handle='titanium-hammered-cookware-set-pro', img=img('cookwaresetpro.webp?v=1777628114'),
      line='Pan Pro 11&Prime;, Wok and Deep Pan, with a titanium flipper and ladle.', price=479, frm=False, us=False),
 dict(key='s06', t='F', name='Titanium Hammered Pan Set With Lids', handle='titanium-hammered-pan-set-with-lids-6-pcs', img=img('6pcscookwareset.webp?v=1783062518'),
      line='Three pans, Mini 8&Prime;, Small 10&Prime; and Large 12&Prime;, each with a fitted lid.', price=299, was=997, frm=False, us=True),  # buiten de VS is dit de hero, geen kaart
 dict(key='rst', t='G', name='Titanium Hammered Roasting Pan', handle='titanium-hammered-roasting-pan', img=img('Roastingpanwithrack.webp?v=1786086806'),
      line='Comes with a fitted roasting rack.', price=199, frm=False, us=True),
 dict(key='p22', t='H', name='2 Pans + 2 Lids', handle='2-pans-and-2-lids', img=img('Titanium_Hammered_Pan_Pro_15.webp?v=1791108749'),
      line='Mini 8&Prime; and Standard 11&Prime;, each with a fitted lid.', price=199, frm=False, us=True),
 dict(key='lrg', t='I', name='Titanium Hammered Pan Pro Large', handle='titanium-hammered-pan-pro-large', img=img('Titanium_hammered_pan_pro_large_6d4ce352-c4ff-48c9-b4d1-170232007e4f.webp?v=1781682831'),
      line='12&Prime;. Room for a family dinner.', price=149, frm=False, us=False),
 dict(key='piz', t='J', name='Titanium Hammered Pizza Steel', handle='titanium-hammered-pizza-steel', img=img('SK_PIZZA_HERO_01_2048_031126.jpg?v=1793715479'),
      line='For pizza night from your own oven.', price=149, frm=False, us=False),
 dict(key='ute', t='K', name='Titanium Utensil Set', handle='siraat-pure-titanium-utensils-bundle', img=img('SK_UTENSIL_SET_HERO_01_v3_2048_031126.jpg?v=1793749122'),
      line='Flipper, spatula, ladle and scooper, all titanium.', price=149, frm=False, us=False),
 dict(key='std', t='L', name='Titanium Hammered Pan Pro Standard', handle='original-siraat-100-pure-titanium-pan-with-hammered-pattern', img=img('Titanium_hammered_pan_pro_standard_b69d1fc5-43d8-40a5-9ad7-523bdddc54d4.webp?v=1781682831'),
      line='11&Prime;. The pan Siraat started with.', price=144, frm=False, us=False),
 dict(key='crp', t='M', name='Titanium Hammered Cr&ecirc;pe Pan Pro', handle='titanium-hammered-crepe-pan-pro', img=img('Crepepan01.jpg?v=1751891713'),
      line='A low edge and a wide base. Cr&ecirc;pes, pancakes, tortillas.', price=139, frm=False, us=False),
 dict(key='sml', t='N', name='Titanium Hammered Pan Pro Small', handle='titanium-hammered-pan-pro-small', img=img('Titanium_hammered_pan_pro_small_76f7b49e-60cd-4e03-a90e-e72411c244d4.webp?v=1781682830'),
      line='10&Prime;. The in-between size.', price=137, frm=False, us=False),
 dict(key='min', t='O', name='Titanium Hammered Pan Pro Mini', handle='titanium-hammered-pan-pro-mini', img=img('Titanium_hammered_pan_pro_mini_65b75fe4-5d77-49af-80a0-eb0b3a78e303.webp?v=1781682830'),
      line='8&Prime;. Eggs, sauces and sides.', price=129, frm=False, us=False),
 dict(key='dep', t='P', name='Titanium Hammered Deep Pan Pro', handle='titanium-hammered-deep-pan-pro', img=img('DeepHammeredPan.webp?v=1780301640'),
      line='Higher sides for sauces, braises and one-pan dinners.', price=119, frm=True, us=False),
 dict(key='wok', t='Q', name='Titanium Hammered Wok Pan Pro', handle='titanium-hammered-wok-pan-pro', img=img('siraat-wok-real-side.jpg?v=1793570219'),
      line='Tall sides and a wide base for stir-fries.', price=119, frm=True, us=False),
 dict(key='brd', t='R', name='Titanium Cutting Board', handle='titanium-cutting-board-v2', img=img('Titanium_Cutting_Board_08.jpg?v=1749556968'),
      line='Anti-microbial titanium. Knife-friendly, no plastic.', price=99, frm=True, us=False),
]
BYKEY = {p['key']: p for p in P}
# Hero's (geen kaart): 12-Pcs in de VS, 6-Pcs buiten de VS.
SET12 = dict(key='s12', name='Titanium Hammered Cookware Set', handle='titanium-hammered-cookware-set', price=649, was=2047)

# ---- Viewed Product (XNtYMB) Name -> key. 'contains' tenzij ('equals', ...). Volgorde telt (eerste treffer wint).
VIEW_MATCH = [
 ('s12', [('contains', '12-Pcs')]),
 ('e34', [('contains', '34-Pcs')]),
 ('s06', [('contains', '6-Pcs')]),
 ('fhp', [('contains', 'Full Hammered Pro')]),
 ('kn8', [('contains', 'Knife Set (8-Piece)')]),
 ('cmp', [('contains', 'Complete Edition')]),
 ('csp', [('contains', 'Cookware Set Pro')]),
 ('rst', [('contains', 'Roasting Pan')]),
 ('p22', [('contains', '2 Pans + 2 Lids')]),
 ('lrg', [('equals', 'Titanium Hammered Pan Pro Large')]),
 ('piz', [('equals', 'Titanium Hammered Pizza Steel')]),
 ('ute', [('equals', 'Titanium Utensil Set Bundle')]),
 ('std', [('equals', 'Titanium Hammered Pan Pro Standard')]),
 ('crp', [('contains', 'Crêpe Pan Pro')]),
 ('sml', [('equals', 'Titanium Hammered Pan Pro Small')]),
 ('min', [('equals', 'Titanium Hammered Pan Pro Mini')]),
 ('dep', [('equals', 'Titanium Hammered Deep Pan Pro')]),
 ('wok', [('equals', 'Titanium Hammered Wok Pan Pro')]),
 ('brd', [('equals', 'Titanium Cutting Board (Anti-Microbial)'), ('equals', 'Titanium Cutting Board')]),
]

# ---- Ordered Product (XT7f8Z, ook Aftersell-regels) Name bevat -> keys die op 9 (in bezit) gaan.
# Bundel-inhoud: PDP "What's in the box" (content/catalog/products.json) en scripts/sync_owned.py.
_S6 = ['s06', 'min', 'sml', 'lrg']
_S12 = ['s12'] + _S6
OWN_MATCH = [
 ('34-Pcs', ['e34'] + _S12 + ['rst', 'wok', 'dep', 'crp', 'piz', 'brd', 'ute']),
 ('FREE PIZZA STEEL', _S12 + ['piz']),
 ('12-Pcs', _S12),
 ('6-Pcs', _S6),
 ('Full Hammered Pro', ['fhp', 'min', 'sml', 'std', 'lrg', 'ute', 's06', 'p22']),
 ('Complete Edition', ['cmp', 'std', 'wok', 'dep', 'crp']),
 ('Cookware Set Pro', ['csp', 'std', 'wok', 'dep']),
 ('2 Pans + 2 Lids', ['p22', 'min', 'std']),
 ('Pan Pro Duo', ['min', 'sml', 'std']),      # catalogus: Mini + Standard; Shopify-tekst: Small + Standard. Beide uitgesloten (veilig).
 ('Pro Duo', ['std']),
 ('Pan Pro Kit', ['sml']),
 ('Cook & Prep', ['std', 'brd']),
 ('Pan Pro & Utensil', ['std', 'ute']),
 ('Wok & Deep', ['wok', 'dep']),
 ('Knife Set (8-Piece)', ['kn8']),
 ('Roasting Pan', ['rst']),
 ('Utensil Set Bundle', ['ute']),
 ('Titanium Cutting Board', ['brd']),
 ('Pizza Steel', ['piz']),
 ('Pan Pro Standard', ['std']),
 ('Pan Pro Large', ['lrg']),
 ('Pan Pro Small', ['sml']),
 ('Pan Pro Mini', ['min']),
 ('Crêpe Pan Pro', ['crp']),
 ('Deep Pan Pro', ['dep']),
 ('Wok Pan Pro', ['wok']),
]
# siraat_owned-sleutels (scripts/sync_owned.py, historie tot de laatste sync) -> keys
SO = {'everything': ['e34'], 'set12': ['s12'], 'set6': ['s06'], 'complete': ['cmp'], 'panpro_standard': ['std'], 'panpro_large': ['lrg'],
      'panpro_small': ['sml'], 'panpro_mini': ['min'], 'deep': ['dep'], 'wok': ['wok'], 'crepe': ['crp'], 'pizza': ['piz'], 'roasting': ['rst'],
      'board': ['brd'], 'utensils': ['ute']}

def owned_keys_for_title(title):
    for frag, keys in OWN_MATCH:
        if frag in title:
            return keys
    return []

def keys_owned(titles, so=()):
    out = set()
    for t in titles: out |= set(owned_keys_for_title(t))
    for s in so: out |= set(SO.get(s, []))
    return out
