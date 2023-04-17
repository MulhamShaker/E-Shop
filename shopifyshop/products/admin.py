from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "active", "category"]
    search_fields = ["name"]
    list_filter = ["category", "price"]

admin.site.register(Product,ProductAdmin)
admin.site.site_header = "Mulham Shopify"
admin.site.site_title = "Mulham Shopify"
