from django.contrib import admin
from .models import Email


class EmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'e_mail', 'message',)
    list_display_links = ('name',)
    search_fields = ('name', 'e_mail',)

admin.site.register(Email, EmailAdmin)