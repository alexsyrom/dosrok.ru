import os
from django import template

register = template.Library()

@register.filter
def extension(value): 
    name, ext = os.path.splitext(value)
    if ext:
        return ext[1:]
    else:
        return "unknown"
