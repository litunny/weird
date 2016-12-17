from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'active', 'created_date')

admin.site.register(Contact, ContactAdmin)