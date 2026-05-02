from django import template
register = template.Library()

@register.simple_tag(name='multiply')

def multiply(value1, value2):
    return value1*value2





