from django.views.generic import ListView, TemplateView

from tree.models import Item


class MenuListView(TemplateView):
    """
    View для получение всех  списка всех меню
    """
    template_name = 'menus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'menus': Item.objects.filter(depth_level=0).values_list('name', flat=True)
        })
        return context


class DetailedMenuView(TemplateView):
    """
    View для получение отрендеренного меню на уровне переданного pk
    """
    template_name = "detailed_menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu = Item.objects.get_detailed_menu(kwargs.get("pk"))
        context.update({
            "detailed_menu": menu
        })
        return context
