from django.contrib import admin

# Register your models here.
from . models import ContactModel


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['first_name']

    search_fields = ['id',]

    list_filter = ['id']

    ordering = ('id',)

    class Meta:
        model = ContactModel


admin.site.register(ContactModel)
