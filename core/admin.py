from django.contrib import admin
from .models import Contact, Partner, PartnerCategory

# Register your models here.

admin.site.register (Contact)

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name','partner', 'created_at', 'updated_at')
    list_filter = ('name','partner', 'created_at', 'updated_at')
    search_fields = ('name','partner', 'created_at', 'updated_at')

admin.site.register (Partner, PartnerAdmin)

admin.site.register (PartnerCategory)