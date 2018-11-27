from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def filter_multi(v1,v2):
    return v1 * v2

@register.simple_tag
def simple_tag_multi(v1,v2):
    return v1 * v2

@register.simple_tag
def my_input(id,arg):
    result = "<input type='text' id='%s' class='%s' />" %(id,arg,)
    return mark_safe(result)