from django import template
register = template.Library()

@register.filter
def cut(value, arg):
    return value.replace(arg, '')

@register.filter
def lower(value):
    return value.lower()

