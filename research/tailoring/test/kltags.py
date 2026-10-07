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
def web_view(label='View in browser'): return mark_safe('<a href="#" style="color:#BDB8B0;">%s</a>' % label)
@register.simple_tag
def manage_preferences_url(): return '#'
@register.simple_tag
def unsubscribe_url(): return '#'
