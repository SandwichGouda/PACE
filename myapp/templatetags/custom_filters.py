from django import template

register = template.Library()

@register.filter
def author(value, delimiter="-"):
    return value.split(delimiter)[0]

@register.filter
def title(value, delimiter="-"):
    return value.split(delimiter)[1][:-4]
