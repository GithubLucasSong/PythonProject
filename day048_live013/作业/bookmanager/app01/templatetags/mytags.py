from django import template

register = template.Library()


@register.inclusion_tag('page.html')
def pagination(num):
    return {'num': range(1, num + 1)}

@register.inclusion_tag('dropdown.html')
def sqr_list(num):
    return {'num':range(1,num+1)}

@register.filter
def multiply(value, arg):
    return value * arg