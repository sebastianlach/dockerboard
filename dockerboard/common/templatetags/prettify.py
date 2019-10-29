from django import template
from yaml import dump

register = template.Library()


@register.filter
def pretty_yaml(value):
    return dump(value)
