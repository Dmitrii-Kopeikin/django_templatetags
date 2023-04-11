from django.contrib import admin

from .models import Menu, MenuItem


class MenuItemInLine(admin.TabularInline):
    model = MenuItem
    extra = 3
    readonly_fields = ['id']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    list_display_links = ['id', 'title']
    readonly_fields = ['id']

    inlines = [MenuItemInLine, ]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'menu', 'title', 'parent', 'url', 'named_url',
                    'named_url_kwargs']
    readonly_fields = ['id']
    list_editable = ['title', 'parent', 'url', 'named_url', 'named_url_kwargs']
