from django.contrib import admin
from .models import Product, Client, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    ordering = ['name']
    list_filter = ['name', 'date']
    search_fields = ['name']
    search_help_text = 'Search by name'

    readonly_fields = ['date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'email'],
            },
        ),
        (
            'Contacts for communication',
            {
                'fields': ['phone', 'address'],
            }
        ),
        (
            'Date',
            {
                'fields': ['date'],
            },
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['name', 'price']
    list_filter = ['name', 'date']
    search_fields = ['name', 'price']
    search_help_text = 'Search by name and price'

    readonly_fields = ['date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Description',
            {
                'classes': ['collapse'],
                'fields': ['description', 'price', 'quantity'],
            }
        ),
        (
            'Date',
            {
                'fields': ['date'],
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'price']
    ordering = ['date', 'price']
    list_filter = ['client', 'product', 'date']
    search_fields = ['client', 'product', 'price', 'date']
    search_help_text = 'Search'

    readonly_fields = ['date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client', 'product', 'price', 'date'],
            },
        ),
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
