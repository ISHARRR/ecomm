from django.contrib import admin

# Register your models here.
from . models import ProductModel


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    # define search columns list, then a search box will be added at the top of Department list page.
    search_fields = ['title', 'slug']

    # define filter columns list, then a filter widget will be shown at right side of Department list page.
    list_filter = ['id']

    ordering = ('id',)

    class Meta:
        model = ProductModel


admin.site.register(ProductModel, ProductModelAdmin)