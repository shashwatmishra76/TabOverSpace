from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name = 'custom_url')
@stringfilter
def get_custom_url(value):
    if ' ' in str(value):
        sections = value.split(' ')
        y = ""
        for i in sections:
            y += i.lower() + "_"
        y = y[:-1]
        return y
