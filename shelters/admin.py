from django.contrib import admin
from .models import Shelter

# Shelter Admin
class ShelterAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state')
    search_fields = ('name', 'city', 'state')
    list_filter = ('city', 'state')
    ordering = ('name',)

# Shelter Model
admin.site.register(Shelter, ShelterAdmin)

