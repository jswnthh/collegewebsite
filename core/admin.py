from django.contrib import admin
from .models import CallForAction

@admin.register(CallForAction)
class CallForActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
