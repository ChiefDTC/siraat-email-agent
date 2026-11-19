"""Scenario's voor PP viewed tailored: context voor Klaviyo template-render + verwachte uitkomst."""
S = [
 dict(id='s01', title='VS · kocht Pan Pro Standard · bekeek Wok (gisteren) en Deep Pan (vorige week)',
      cc='US', items=['Titanium Hammered Pan Pro Standard', 'Mystery Gift'], vr={'std': 9, 'wok': 1, 'dep': 2}, so=[],
      expect_hero='12-Pcs', expect=['wok', 'dep']),
 dict(id='s02', title='VS · kocht 12-Pcs · bekeek Pan Pro Large (zit in de set), Pizza Steel en de Damascus-messenset',
      cc='US', items=['Titanium Hammered Cookware Set | 12-Pcs'], vr={'s12': 9, 's06': 9, 'min': 9, 'sml': 9, 'lrg': 9, 'piz': 1, 'kn8': 2}, so=[],
      expect_hero=None, expect=['piz', 'kn8']),
 dict(id='s03', title='VS · kocht 12-Pcs · bekeek Pan Pro Standard 11" (zit NIET in de set), Pizza Steel',
      cc='US', items=['Titanium Hammered Cookware Set | 12-Pcs'], vr={'s12': 9, 's06': 9, 'min': 9, 'sml': 9, 'lrg': 9, 'std': 1, 'piz': 1}, so=[],
      expect_hero=None, expect=['piz', 'std']),
 dict(id='s04', title='VS · kocht Pan Pro Mini · niets bekeken',
      cc='US', items=['Titanium Hammered Pan Pro Mini'], vr={'min': 9}, so=[], expect_hero='12-Pcs', expect=[]),
 dict(id='s05', title='VS · kocht 6-Pcs · bekeek alleen Mini en Large (al in bezit)',
      cc='US', items=['Titanium Hammered Pan Set With Lids | 6-Pcs'], vr={'s06': 9, 'min': 9, 'sml': 9, 'lrg': 9}, so=[], expect_hero='12-Pcs', expect=[]),
 dict(id='s06', title='VS · kocht Pan Pro Standard · bekeek 5 producten (Wok en Deep gisteren, Pizza Steel vorige week, Crêpe en Board 3 weken terug)',
      cc='US', items=['Titanium Hammered Pan Pro Standard'], vr={'std': 9, 'wok': 1, 'dep': 1, 'piz': 2, 'crp': 3, 'brd': 3}, so=[],
      expect_hero='12-Pcs', expect=['dep', 'wok', 'piz']),
 dict(id='s07', title='VK · kocht Pan Pro Standard · bekeek Wok, 2 Pans + 2 Lids (alleen VS) en 12-Pcs (alleen VS)',
      cc='GB', items=['Titanium Hammered Pan Pro Standard'], vr={'std': 9, 'wok': 2, 'p22': 1, 's12': 1}, so=[], expect_hero='6-Pcs', expect=['wok']),
 dict(id='s08', title='VS · kocht The Just Everything Bundle 34-Pcs · bekeek Wok (in bezit), Pan Pro Standard en messenset',
      cc='US', items=['The Just Everything Bundle | 34-Pcs'],
      vr={k: 9 for k in ['e34', 's12', 's06', 'min', 'sml', 'lrg', 'rst', 'wok', 'dep', 'crp', 'piz', 'brd', 'ute']} | {'std': 1, 'kn8': 3}, so=[],
      expect_hero=None, expect=['std', 'kn8']),
 dict(id='s09', title='VS · kocht Pan Pro Standard, nam via Aftersell de 12-Pcs erbij · bekeek Deep Pan en Pan Pro Large',
      cc='US', items=['Titanium Hammered Pan Pro Standard', 'Mystery Gift'],  # Placed Order mist de Aftersell-regel
      vr={'std': 9, 's12': 9, 's06': 9, 'min': 9, 'sml': 9, 'lrg': 9, 'dep': 1}, so=[], expect_hero=None, expect=['dep']),
 dict(id='s10', title='Land onbekend · kocht Pan Pro Standard · bekeek de 6-Pcs en de Roasting Pan (alleen VS)',
      cc=None, items=['Titanium Hammered Pan Pro Standard'], vr={'std': 9, 's06': 1, 'rst': 1}, so=[], expect_hero='6-Pcs', expect=[]),
 dict(id='s11', title='VS · kocht Wok, had eerder al de 12-Pcs (alleen in siraat_owned) · bekeek alleen de Wok',
      cc='US', items=['Titanium Hammered Wok Pan Pro'], vr={'wok': 9}, so=['set12', 'panpro', 'panpro_mini'], expect_hero=None, expect=[]),
 dict(id='s12', title='VS · tracker gemist: kocht Deep Pan in deze order, ppv_vr_dep staat nog op 1 · bekeek ook Wok',
      cc='US', items=['Titanium Hammered Deep Pan Pro'], vr={'dep': 1, 'wok': 2}, so=[], expect_hero='12-Pcs', expect=['wok']),
]
def ctx(s):
    person = {'first_name': 'Sam', 'email': 'sam@example.com', 'siraat_owned': s['so']}
    for k, v in s['vr'].items(): person['ppv_vr_' + k] = v
    ev = {'Items': s['items'], 'extra': {'shipping_address': ({'country_code': s['cc']} if s['cc'] else {})}}
    return {'person': person, 'event': ev}
