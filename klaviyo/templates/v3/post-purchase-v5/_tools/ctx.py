"""Contexten voor previews (lokaal Django) en de Klaviyo template-render API. Zelfde vorm als post-purchase-viewed/_tools/scenarios.py."""
def ev(items, cc='US', name='#SK104512', lines=None):
    return {'Items': items, 'extra': {'name': name, 'shipping_address': ({'country_code': cc} if cc else {}),
            'line_items': lines or [{'title': t, 'quantity': 1} for t in items]}}
def person(vr=None, so=None):
    p = {'first_name': 'Sam', 'email': 'sam@example.com', 'siraat_owned': so or []}
    for k, v in (vr or {}).items(): p['ppv_vr_' + k] = v
    return p
STD = ['Titanium Hammered Pan Pro Standard', 'Mystery Gift', 'Plastic-Free Guide E-Book']
S12 = ['Titanium Hammered Cookware Set | 12-Pcs', 'Mystery Gift']
# (mail, scenario-id, titel, context)
CASES = [
 ('pp1-first', 'us', 'VS, eerste order, Pan Pro Standard', {'event': ev(STD), 'person': person()}),
 ('pp1-repeat', 'us', 'VS, herhaalorder, Wok', {'event': ev(['Titanium Hammered Wok Pan Pro', 'Mystery Gift']), 'person': person()}),
 ('pp2-upsell', 'std-wok-deep', 'VS, kocht Standard, bekeek Wok (1) en Deep (2)', {'event': ev(STD), 'person': person({'std': 9, 'wok': 1, 'dep': 2})}),
 ('pp2-upsell', 's12-pizza-knives', 'VS, kocht 12-Pcs, bekeek Pizza Steel (1) en messen (2), Large in set', {'event': ev(S12), 'person': person({'s12': 9, 's06': 9, 'min': 9, 'sml': 9, 'lrg': 9, 'piz': 1, 'kn8': 2})}),
 ('pp2-upsell', 'uk-std-wok', 'VK, kocht Standard, bekeek Wok (2), 2+2 en 12-Pcs (alleen VS)', {'event': ev(STD, 'GB'), 'person': person({'std': 9, 'wok': 2, 'p22': 1, 's12': 1})}),
 ('pp3-delivered', 'us-std', 'VS, Standard bezorgd (dekselkaart 11")', {'event': ev(STD), 'person': person()}),
 ('pp3-safe', 'uk-std', 'VK, Standard, nog niet bevestigd bezorgd (deksel 28 cm)', {'event': ev(STD, 'GB'), 'person': person()}),
 ('pp4-code', 'us-std', 'VS, pankoper Standard', {'event': ev(STD), 'person': person({'std': 9})}),
 ('pp4-code', 'us-s12', 'VS, setkoper 12-Pcs', {'event': ev(S12), 'person': person({'s12': 9, 's06': 9, 'min': 9, 'sml': 9, 'lrg': 9})}),
 ('pp4-nocode', 'de-acc', 'Duitsland, accessoirekoper (snijplank)', {'event': ev(['Titanium Cutting Board'], 'DE'), 'person': person({'brd': 9})}),
]
