from django.contrib import admin
from .models import Products, Brand, Category, SubCategory

# Register your models here.
admin.site.site_header = 'Dashboard'


class ProductsAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


class SubCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'category_name')


class BrandAdmin(admin.ModelAdmin):
    fields = ('name', 'category_name', 'sub_category_name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Products, ProductsAdmin)
