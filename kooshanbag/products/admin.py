from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    

admin.site.register(models.Color)

admin.site.register(models.Size)

admin.site.register(models.ProductImage)

admin.site.register(models.Price)



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'size', 'slug', 'price',
                     'quantity', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['colors']
    

admin.site.register(models.Comment)


admin.site.register(models.ProductDescription)


