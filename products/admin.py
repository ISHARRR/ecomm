from django.contrib import admin

# Register your models here.
from . models import ProductModel


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = ProductModel


admin.site.register(ProductModel, ProductModelAdmin)