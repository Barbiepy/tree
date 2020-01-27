from django.urls import path

from tree.views import MenuListView, DetailedMenuView

urlpatterns = [
    path('', MenuListView.as_view()),
    path('menus/<int:pk>/', DetailedMenuView.as_view(), name='detailed-menu')
]
