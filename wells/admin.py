from django.contrib import admin
from .models import Well

@admin.register(Well)
class WellAdmin(admin.ModelAdmin):
    list_display  = ['name', 'pressure', 'status', 'active', 'engineer']
    list_filter   = ['status', 'active']
    search_fields = ['name', 'engineer']