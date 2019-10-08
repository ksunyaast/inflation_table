from django import template

register = template.Library()

@register.filter
def inf_color(num: str) -> str:
    color = ''
    if num:
        num = float(num)
        if num < 0:
            color = '#008000'
        if 1 <= num and num < 2:
            color = '#FCD3D3'
        if 2 <= num and num < 5:
            color = '#FA8C8C'
        if num >= 5:
            print(num)
            color = '#FF0000'
    return color

@register.filter
def first_column(list: list) -> int:
    return list[0]

@register.filter
def last_column(list: list) -> int:
    return list[len(list) - 1]