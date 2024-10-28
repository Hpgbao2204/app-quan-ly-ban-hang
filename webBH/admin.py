from django.contrib import admin
from .models import Product, Brand, Categories, Profile


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'price', 'description', 'brand', 'category')
    list_filter = ('price',)
    search_fields = ('name', 'description')
    ordering = ('price',)
    readonly_fields = ('code', 'id')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone', 'get_email')  # Thêm phương thức get_email

    def get_email(self, obj):
        return obj.user.email  # Lấy email từ User
    get_email.short_description = 'Email'  # Đặt tiêu đề cho cột


admin.site.register(Profile, ProfileAdmin)