# Klaviyo-stubs voor de Django-tests. Registreer hier ALLEEN tags en filters die Klaviyo echt kent
# (zelfde lijst als KL_TAGS in scripts/qa_render.py). Een foute naam hier (bijv. manage_preferences_url) laat de test
# een tag accepteren die Klaviyo weigert ("Invalid template tag"), daarom geen extra's toevoegen.
from django import template
from django.utils.safestring import mark_safe
register = template.Library()
@register.filter
def lookup(d, k):
    try: return d.get(k, '')
    except Exception: return ''
@register.simple_tag
def coupon_code(name): return 'SRT-K7Q2M'
@register.simple_tag
def unsubscribe(label='Unsubscribe'): return mark_safe('<a href="#" style="color:#BDB8B0;">%s</a>' % label)
@register.simple_tag
def unsubscribe_link(): return '#unsubscribe'
@register.simple_tag
def manage_preferences(label='Manage preferences'): return mark_safe('<a href="#" style="color:#BDB8B0;">%s</a>' % label)
@register.simple_tag
def manage_preferences_link(): return '#preferences'
@register.simple_tag
def web_view(label='View in browser'): return mark_safe('<a href="#" style="color:#BDB8B0;">%s</a>' % label)
@register.simple_tag
def web_view_link(): return '#webview'
# Klaviyo-datumtag en -filters (help.klaviyo.com "Date variables in templates reference"; urgency-upgrade 7 okt 2026):
# {% today '%Y-%m-%d' as today %}{{ today|days_later:2|format_date_string|date:'D' }}
import datetime as _dt
@register.simple_tag
def today(fmt='%Y-%m-%d'): return _dt.datetime.now().strftime(fmt)
@register.filter
def days_later(v, n):
    for f in ('%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%m-%d-%Y'):
        try: return (_dt.datetime.strptime(str(v), f) + _dt.timedelta(days=int(n))).strftime(f)
        except ValueError: pass
    return ''
@register.filter
def format_date_string(v):
    for f in ('%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%m-%d-%Y'):
        try: return _dt.datetime.strptime(str(v), f)
        except ValueError: pass
    return ''
