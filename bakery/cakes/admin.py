from django.contrib import admin

from .models import Cake, Modifications, Order, CustomUser, VariablesOfModification


class VariablesOfModificationAdminInline(admin.TabularInline):
    model = VariablesOfModification


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'telegram_username', ]


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', ]
    search_fields = ['name', 'ingredients', ]


@admin.register(Modifications)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['id', 'cake', 'modification', 'necessary']
    search_fields = ['modification', ]
    list_filter = ['necessary', 'cake', ]
    inlines = [VariablesOfModificationAdminInline]


@admin.register(VariablesOfModification)
class VariablesOfModificationAdmin(admin.ModelAdmin):
    list_display = ['modification', 'tier', 'price']
    search_fields = ['modification__modification', ]


@admin.register(Order)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'address', 'cake', 'delivery', 'status', ]
    list_filter = ['delivery', 'status', ]
    raw_id_fields = ['variables_of_modifications', ]
    list_editable = ['status', ]
    readonly_fields = ['customer', 'address', 'cake', 'variables_of_modifications', 'phone_number', 'created',
                       'comment', ]
