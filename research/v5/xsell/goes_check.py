import sys, os, re
T='/home/user/siraat-email-agent/research/tailoring/test'
sys.path.insert(0, T+'/pylib'); sys.path.insert(0, T)
import django
from django.conf import settings
settings.configure(TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','OPTIONS':{'libraries':{'kl':'kltags'},'builtins':['kltags']}}])
django.setup()
from django.template import engines
B='/home/user/siraat-email-agent/klaviyo/templates/partials/blocks/goes.html'
h=open(B).read().replace('[[src]]','event.Items|join:","').replace('[[pre]]','/p/').replace('[[post]]','').replace('[[pad]]','0').replace('[[note]]','').replace('{{SHARED}}','S')
t=engines['django'].from_string(h)
cases={
 'Standard+Mini':['Titanium Hammered Pan Pro Standard','Titanium Hammered Pan Pro Mini'],
 'Small+Mini':['Titanium Hammered Pan Pro Small','Titanium Hammered Pan Pro Mini'],
 'Large+Small':['Titanium Hammered Pan Pro Large','Titanium Hammered Pan Pro Small'],
 'Deep+Wok':['Titanium Hammered Deep Pan Pro','Titanium Hammered Wok Pan Pro'],
 'Wok+Deep+Crepe':['Titanium Hammered Wok Pan Pro','Titanium Hammered Deep Pan Pro','Titanium Hammered Crêpe Pan Pro'],
 'Standard+Lid+Board':['Titanium Hammered Pan Pro Standard','Stainless Steel Lid','Titanium Cutting Board V2'],
 'Board+Standard':['Titanium Cutting Board V2','Titanium Hammered Pan Pro Standard'],
 'Fall3+3 (Small,Large,Mini,Lid)':['Titanium Hammered Pan Pro Small','Titanium Hammered Pan Pro Large','Titanium Hammered Pan Pro Mini','Stainless Steel Lid'],
 '6pcs+Board':['Titanium Hammered Pan Set With Lids | 6-Pcs','Titanium Cutting Board V2'],
 'Apron+Mill':['Siraat Signature Apron (Oak)','Salt & Pepper Mill Set'],
 'Pizza+Board':['Titanium Hammered Pizza Steel','Titanium Cutting Board V2'],
 'Crepe+Standard':['Titanium Hammered Crêpe Pan Pro','Titanium Hammered Pan Pro Standard'],
}
for k,items in cases.items():
    out=t.render({'event':{'Items':items}})
    names=re.findall(r'font-weight:600;color:#282828;">([^<]+)</span>',out)
    cat=re.findall(r'data-goes="([^"]+)"',out)
    print(f'{k:35s} cat={cat} -> {names}')
