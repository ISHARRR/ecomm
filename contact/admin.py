from django.contrib import admin

# Register your models here.
from . models import ContactModel


class ContactModelAdmin(admin.ModelAdmin):
    list_display = [ 'first_name']

    class Meta:
        model = ContactModel


admin.site.register(ContactModel)
