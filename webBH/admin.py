from django.contrib import admin
from .models import Product, Brand, Categories


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'price', 'description', 'brand', 'category')
    list_filter = ('price',)
    search_fields = ('name', 'description')
    ordering = ('price',)
    readonly_fields = ('code',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)



