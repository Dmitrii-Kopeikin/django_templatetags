import django.urls
from django.urls import path
from django.views.generic import RedirectView

from .views import (
    MenuDetailView, MenuListView, MenuItemDetailView
)

app_name = 'tree_menu'
urlpatterns = [
    path('', RedirectView.as_view(url='/menus')),
    path('menus', MenuListView.as_view(), name='menus'),
    path('menu/<int:pk>', MenuDetailView.as_view(), name='menu'),
    path('menu/<int:menu_id>/item/<int:item_id>', MenuItemDetailView.as_view(), name='menu_item'),
]
