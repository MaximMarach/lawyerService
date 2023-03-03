from django.contrib import admin

from api.models import Contact
# Register your models here.

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    model = Contact