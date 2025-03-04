from django.contrib import admin
from .models import Cake, Modifications, Order, CustomUser, VariablesOfModification, ShortenedURL


class VariablesOfModificationAdminInline(admin.TabularInline):
    model = VariablesOfModification


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'telegram_username']
    search_fields = ['username', 'telegram_username']


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    search_fields = ['name', 'ingredients']


@admin.register(Modifications)
class ModificationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'cake', 'modification', 'necessary']
    search_fields = ['modification']
    list_filter = ['necessary', 'cake']
    inlines = [VariablesOfModificationAdminInline]


@admin.register(VariablesOfModification)
class VariablesOfModificationAdmin(admin.ModelAdmin):
    list_display = ['modification', 'tier', 'price']
    search_fields = ['modification__modification']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'address', 'cake', 'delivery', 'status', 'total_price_with_currency']
    list_filter = ['delivery', 'status', 'cake']
    list_editable = ['status', 'delivery']
    readonly_fields = ['customer', 'address', 'cake', 'variables_of_modifications', 'phone_number', 'created',
                       'comment', 'total_price']
    search_fields = ['customer__username', 'address', 'cake__name']
    date_hierarchy = 'created'

    def total_price_with_currency(self, obj):
        return f"{obj.total_price} руб."
    total_price_with_currency.short_description = 'Общая стоимость'

    def has_add_permission(self, request):
        return False


@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ['long_url', 'short_url', 'click_count', 'created_at']
    search_fields = ['long_url', 'short_url']
    readonly_fields = ['click_count', 'created_at']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

    actions = ['reset_click_count']

    @admin.action(description='Сбросить счетчик кликов')
    def reset_click_count(self, request, queryset):
        queryset.update(click_count=0)
        self.message_user(request, f"Счетчик кликов сброшен для {queryset.count()} ссылок.")
