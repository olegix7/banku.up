from django.contrib import admin
from .models import Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('icon', 'name', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('name',)
    search_fields = ('name', 'url')
    list_filter = ('is_active',)
    ordering = ('order', 'name')
