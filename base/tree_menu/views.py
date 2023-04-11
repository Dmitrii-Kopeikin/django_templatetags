from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, ListView
from django.views import View
from django.http import HttpResponse

from .models import Menu, MenuItem


class MenuDetailView(DetailView):
    model = Menu
    context_object_name = 'menu'


class MenuListView(ListView):
    model = Menu
    context_object_name = 'menus'


class MenuItemDetailView(View):
    template_name = 'tree_menu/menu_item_detail.html'

    def get(self, request, **kwargs):
        menu = Menu.objects.get(pk=kwargs['menu_id'])
        menu_item = MenuItem.objects.get(pk=kwargs['item_id'])
        context = {
            'menu': menu,
            'menu_item': menu_item,
        }
        return render(request, self.template_name, context)
