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
