"""Prototype (scratch) van het xsell-blok: genereert Django en test het op voorbeeldorders. Niet in templates."""
import sys, re
OWN = [  # token, substrings in trigger-Items die bezit betekenen
 ('mini',  ['Pan Pro Mini','Pan Set With Lids','12-Pcs','Full Hammered']),
 ('small', ['Pan Pro Small','Pan Set With Lids','12-Pcs','Pan Pro Duo','Full Hammered']),
 ('std',   ['Pan Pro Standard','Titanium Pan Pro','Frying Pan','Cookware Set Pro','Pan Pro Duo','Full Hammered','Pan Pro With Lid','& Utensil Set']),
 ('large', ['Pan Pro Large','Pan Set With Lids','12-Pcs','Full Hammered']),
 ('deep',  ['Deep Pan','Cookware Set Pro','Complete Edition']),
 ('wok',   ['Wok','Cookware Set Pro','Complete Edition']),
 ('crepe', ['pe Pan','Complete Edition']),
 ('lid20', ['Pan Set With Lids','12-Pcs','Full Hammered','Pan Pro Mini&Lid']),
 ('lid26', ['Pan Set With Lids','12-Pcs','Full Hammered','Pan Pro Small&Lid']),
 ('lid28', ['Full Hammered','Pan Pro Standard&Lid','Pan Pro With Lid']),
 ('lid30', ['Pan Set With Lids','12-Pcs','Full Hammered','Pan Pro Large&Lid']),
 ('board', ['Cutting Board','Prep Board']),
 ('utset', ['Utensil Set','Full Hammered']),
 ('apron', ['Apron']), ('mill', ['Mill']), ('pizza', ['Pizza Steel']),
]
CAT = [  # categorie, triggertokens (eerste match wint), 4 kandidaten
 ('set12', ['12-Pcs'], ['std','utset','board','crepe']),
 ('setbig',['Cookware Set Pro','Complete Edition','Full Hammered','Pan Pro Duo','2 Pans'], ['lid28','board','crepe','mini']),
 ('pot',   ['Pot'], ['set6','std','board','utset']),
 ('set6',  ['Pan Set With Lids'], ['std','utset','board','deep']),
 ('std',   ['Pan Pro Standard','Titanium Pan Pro','Frying Pan','Pan Pro With Lid'], ['lid28','mini','board','deep']),
 ('large', ['Pan Pro Large'], ['lid30','small','std','board']),
 ('small', ['Pan Pro Small'], ['mini','lid26','board','wok']),
 ('mini',  ['Pan Pro Mini'], ['std','lid20','board','wok']),
 ('deep',  ['Deep Pan'], ['wok','mini','board','utset']),
 ('wok',   ['Wok'], ['deep','mini','board','utset']),
 ('crepe', ['pe Pan'], ['std','board','utset','wok']),
 ('pizza', ['Pizza Steel'], ['board','std','crepe','utset']),
 ('roast', ['Roasting'], ['board','large','utset','std']),
 ('board', ['Cutting Board','Prep Board'], ['std','mini','utset','deep']),
 ('lid',   ['Lid'], ['mini','small','board','deep']),
 ('utensil',['Utensil','Chopsticks'], ['board','mini','deep','wok']),
 ('mill',  ['Mill'], ['board','apron','std','utset']),
 ('apron', ['Apron'], ['mill','board','std','mini']),
 ('sheets',['Dishwasher Sheets','Detergent'], ['std','board','mini','deep']),
]
ITEM = {  # token: naam, regel, handle, beeld
 'mini':('Pan Pro Mini 8&Prime;','The breakfast pan: eggs and small portions.','titanium-hammered-pan-pro-mini','pc-mini'),
 'small':('Pan Pro Small 10&Prime;','Dinner for two.','titanium-hammered-pan-pro-small','pc-small'),
 'std':('Pan Pro 11&Prime;','The size most kitchens start with.','original-siraat-100-pure-titanium-pan-with-hammered-pattern','pc-standard'),
 'large':('Pan Pro Large 12&Prime;','Room for the whole family.','titanium-hammered-pan-pro-large','pc-large'),
 'deep':('Deep Pan Pro','Higher sides for sauces, pasta and one-pan dinners.','titanium-hammered-deep-pan-pro','pc-deep'),
 'wok':('Wok Pan Pro','Up to 3.5&Prime; deep, to toss without spilling.','titanium-hammered-wok-pan-pro','pc-wok'),
 'crepe':('Cr&ecirc;pe Pan Pro','Flat and wide: cr&ecirc;pes, pancakes, tortillas.','titanium-hammered-crepe-pan-pro','pc-crepe'),
 'lid20':('Stainless Steel Lid, 20 cm','Fits your 8&Prime; Mini.','stainless-steel-lid?variant=53294486421844','pc-lid'),
 'lid26':('Stainless Steel Lid, 26 cm','Fits your 10&Prime; Small.','stainless-steel-lid?variant=52401107206484','pc-lid'),
 'lid28':('Stainless Steel Lid, 28 cm','Fits your 11&Prime; Pan Pro.','stainless-steel-lid?variant=52401107239252','pc-lid'),
 'lid30':('Stainless Steel Lid, 30 cm','Fits your 12&Prime; Large.','stainless-steel-lid?variant=52401107272020','pc-lid'),
 'board':('Titanium Cutting Board','Non-porous titanium. Nothing soaks in.','titanium-cutting-board-v2','pc-board'),
 'utset':('Titanium Utensil Set','Metal on titanium is fine: no coating to scrape.','siraat-pure-titanium-utensils-bundle','pc-utensil'),
 'apron':('Siraat Signature Apron','16-oz canvas, adjustable, four colors.','siraat-signature-apron-moss','pc-apron'),
 'mill':('Salt &amp; Pepper Mill Set','All-metal, 12 grind settings.','salt-pepper-mill-set','pc-mill'),
 'set6':('3 pans + 3 lids','Mini, Small and Large, each with its lid.','titanium-hammered-pan-set-with-lids-6-pcs','pc-set6'),
}
def cond(toks, var='s'):
    one=lambda x:' and '.join("'%s' in %s"%(y,var) for y in x.split('&'))
    return ' or '.join(one(x) for x in toks)
def gen():
    o=[]
    o.append("{% with s=event.Items|join:',' t=person|lookup:'Shopify Tags'|default:''|join:',' %}")
    # 1. bezit (trigger-order of profieltag)
    for tok,subs in OWN:
        o.append("{%% if %s or 'own-%s' in t %%}{%% firstof 'y' as o_%s %%}{%% endif %%}"%(cond(subs),tok,tok))
    # 2. categorie (eerste match)
    o.append(''.join(('{%% if %s %%}' if i==0 else '{%% elif %s %%}')%cond(t)+"{%% firstof '%s' as k %%}"%c for i,(c,t,_) in enumerate(CAT))+'{% endif %}')
    # 3. beschikbare kandidaten a1..a4 per categorie (alleen niet in bezit)
    def free(tok):
        if tok=='set6': return 'not o_mini and not o_small and not o_large'
        return 'not o_%s'%tok
    parts=[]
    for i,(c,t,cands) in enumerate(CAT):
        body=''.join("{%% if %s %%}{%% firstof '%s' as a%d %%}{%% endif %%}"%(free(x),x,j+1) for j,x in enumerate(cands))
        parts.append(('{%% if k == \'%s\' %%}' if i==0 else '{%% elif k == \'%s\' %%}')%c+body)
    o.append(''.join(parts)+'{% endif %}')
    # 4. eerste en tweede vrije kandidaat
    o.append("{% firstof a1 a2 a3 a4 as c1 %}{% if a1 %}{% firstof a2 a3 a4 as c2 %}{% elif a2 %}{% firstof a3 a4 as c2 %}{% elif a3 %}{% firstof a4 as c2 %}{% endif %}")
    # 5. renderer per rij
    def chain(var, f):
        return ''.join(('{%% if %s == \'%s\' %%}' if i==0 else '{%% elif %s == \'%s\' %%}')%(var,k)+f(v) for i,(k,v) in enumerate(ITEM.items()))+'{% endif %}'
    for var in ('c1','c2'):
        o.append("{%% if %s %%}<tr data-xs=\"{{ %s }}\"><td><img src=\"{{SHARED}}/%s.jpg\" width=\"64\" alt=\"\"></td><td><a href=\"[[pre]]%s[[post]]\"><b>%s</b><br>%s</a></td></tr>{%% endif %%}"%(
            var,var,chain(var,lambda v:v[3]),chain(var,lambda v:v[2]),chain(var,lambda v:v[0]),chain(var,lambda v:v[1])))
    o.append("{% if not c1 %}<tr data-xs=\"fallback\"><td>FALLBACK: The care guide, plus our bestsellers</td></tr>{% endif %}")
    o.append("{% endwith %}")
    return '\n'.join(o)
if __name__=='__main__':
    h=gen(); print(len(h),'bytes', file=sys.stderr)
    open(sys.argv[1],'w').write(h)
