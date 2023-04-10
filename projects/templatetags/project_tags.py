from django import template

register = template.Library()

@register.filter
def capitalize(value):
    return value.capitalize()

@register.filter
def two_decimals(value):
    value = f'{value:.2f}'
    if str(value).endswith('.00'):
        value = int(value.replace('.00', ''))
    return str(value)
