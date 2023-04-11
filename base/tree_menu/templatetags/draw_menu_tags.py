import json

from django import template
from django.template import RequestContext
from django.urls import reverse

from ..models import MenuItem, Menu

register = template.Library()


def _mark_active_parents(active_item: MenuItem, menu_items):
    while active_item is not None:
        menu_items[active_item.id][2] = True
        if active_item.parent_id:
            active_item = menu_items[active_item.parent_id][0]
        else:
            break


def _mark_active_items(menu_items: dict, context: RequestContext):
    current_path: str = context.request.get_full_path()

    # Searching for active element of the menu
    active_item = None
    for item_data in menu_items.values():
        item = item_data[0]
        item_url = item.get_url()

        if item_url and current_path.startswith(item_url):
            if active_item and len(item_url) > len(active_item.get_url()) or \
                    not active_item:
                active_item = item

        if item.parent_id is not None:
            menu_items[item.parent_id][1].append(item_data)

    # Marking all parent items on higher levels of menu
    _mark_active_parents(active_item, menu_items)

    return menu_items


@register.inclusion_tag('tree_menu/template_tags/menu.html', takes_context=True)
def draw_menu(context: RequestContext, menu_slug: str):
    menu_items_list = list(MenuItem.objects.filter(
        menu__slug=menu_slug).select_related("menu"))

    if menu_items_list:
        # If at least one item available, getting menu_title from queryset
        # to minimize database queries count
        menu_title = menu_items_list[0].menu.title

        # Creating dict for items with additional data:
        # {'item_id': [item_object, children_list, is_active]
        menu_items = {item.id: [item, [], False] for item in menu_items_list}

        menu_items = _mark_active_items(menu_items, context)

        # Deleting all non-zero level items
        menu_items = dict(filter(lambda item: item[1][0].parent_id is None,
                                 menu_items.items()))
    else:
        # If there is no items, do query to get menu_title
        menu_title = Menu.objects.get(slug=menu_slug).title
        menu_items = {}

    return {
        'menu_title': menu_title,
        'menu_items': menu_items,
        'context': context,
    }


@register.inclusion_tag('tree_menu/template_tags/dropdown.html')
def draw_items(items: dict):
    return {'items': items}
