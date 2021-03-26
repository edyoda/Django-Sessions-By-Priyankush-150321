from django import template

register = template.Library()

@register.filter(name='rep_space')
def rep_space(value):
    return value.replace(' ', '@#$%^!')