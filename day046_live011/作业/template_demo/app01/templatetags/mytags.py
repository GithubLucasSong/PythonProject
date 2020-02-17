from django import template

register = template.Library()


@register.filter
def subtract(value, arg):
    return value - arg


@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def divide(value, arg):
    return value / arg


@register.filter
def show_a(value, arg):
    return '<a href="https://{}">{}</a>'.format(arg,value)
