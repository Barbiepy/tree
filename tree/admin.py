from django.contrib import admin

from tree.models import Item


class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    readonly_fields = ["depth_level"]  # TODO убрать


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]
    readonly_fields = ["depth_level"]  # TODO убрать

