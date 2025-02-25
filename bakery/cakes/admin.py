from django.contrib import admin

from .models import Cake, Modifications, Order, CustomUser, VariablesOfModification


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'ingredients', 'price']


@admin.register(Modifications)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['modification']


@admin.register(Order)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['address', 'status', 'cake']


@admin.register(VariablesOfModification)
class VariablesOfModificationAdmin(admin.ModelAdmin):
    list_display = ['modification', 'tier']
