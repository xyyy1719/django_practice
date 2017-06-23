from django import template
register = template.Library()

@register.simple_tag
def minus2(value):
    return value - 2
