from django import template
from django.urls import reverse

from tree.models import Item

register = template.Library()


@register.simple_tag
def draw_menu(name: str):
    """
    Отрисовать главный пункт меню по названию
    :param name: название главного пункта меню
    :return:
    """

    pk = Item.objects.filter(name=name, depth_level=0).first().pk
    url = reverse('detailed-menu', kwargs={"pk": pk})

    return f"<a href={url}>{name}</a>"


@register.simple_tag
def multiply(string: str, count: int) -> str:
    """
    Тэг для перемножения строк
    :param string:
    :param count:
    :return:
    """
    return string * count
