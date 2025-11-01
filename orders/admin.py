from django.contrib import admin

from .models import Combo, Extra, MenuItem, Order


class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "full_name",
        "menu_item",
        "quantity",
        "delivery_method",
    )
    readonly_fields = (
        "full_name",
        "email",
        "menu_item",
        "quantity",
        "extras",
        "delivery_method",
        "address",
    )


admin.site.register(Combo)
admin.site.register(Extra)
admin.site.register(MenuItem)
admin.site.register(Order, CustomerOrderAdmin)
