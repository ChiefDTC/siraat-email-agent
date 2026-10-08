import sys, re
T='/home/user/siraat-email-agent/research/tailoring/test'
sys.path.insert(0, T+'/pylib'); sys.path.insert(0, T)
import django
from django.conf import settings
settings.configure(TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','OPTIONS':{'libraries':{'kl':'kltags'},'builtins':['kltags']}}])
django.setup()
from django.template import engines
h=open(sys.argv[1]).read().replace('[[pre]]','/p/').replace('[[post]]','')
t=engines['django'].from_string(h)
cases=[
 ('Standard',['Titanium Hammered Pan Pro Standard'],[]),
 ('Standard+Lid',['Titanium Hammered Pan Pro Standard','Stainless Steel Lid'],[]),
 ('Standard+Mini',['Titanium Hammered Pan Pro Standard','Titanium Hammered Pan Pro Mini'],[]),
 ('Small+Mini',['Titanium Hammered Pan Pro Small','Titanium Hammered Pan Pro Mini'],[]),
 ('Large+Small',['Titanium Hammered Pan Pro Large','Titanium Hammered Pan Pro Small'],[]),
 ('Deep+Wok',['Titanium Hammered Deep Pan Pro','Titanium Hammered Wok Pan Pro'],[]),
 ('Fall sale 6-Pcs',['Titanium Hammered Pan Set With Lids | 6-Pcs'],[]),
 ('6-Pcs+Board',['Titanium Hammered Pan Set With Lids | 6-Pcs','Titanium Cutting Board V2'],[]),
 ('Pot set (US)',['Titanium Hammered Pot Set With Lids | 6-Pcs'],[]),
 ('Apron+Mill',['Siraat Signature Apron (Oak)','Salt & Pepper Mill Set'],[]),
 ('VIP: 2e order Lid, eerder Standard+Mini+Board (tags)',['Stainless Steel Lid'],['own-std','own-mini','own-board','own-lid28']),
 ('VIP: 2e order Mini, eerder Small (tag)',['Titanium Hammered Pan Pro Mini'],['own-small','own-lid26']),
 ('Alles al',['Titanium Hammered Pan Pro Standard'],['own-lid28','own-mini','own-board','own-deep']),
]
for name,items,tags in cases:
    out=t.render({'event':{'Items':items},'person':{'Shopify Tags':tags}})
    print(f"{name:55s} -> {re.findall(r'data-xs=\"([^\"]+)\"',out)}")
