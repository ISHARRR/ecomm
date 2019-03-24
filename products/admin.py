from django.contrib import admin

# Register your models here.
from . models import ProductModel


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    search_fields = ['title', 'slug']

    list_filter = ['id']

    ordering = ('id',)

    class Meta:
        model = ProductModel


admin.site.register(ProductModel, ProductModelAdmin)