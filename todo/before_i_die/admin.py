from django.contrib import admin

from .models import BeforeIDie


@admin.register(BeforeIDie)
class BeforeIDieAdmin(admin.ModelAdmin):
    list_display = ('text', 'checkbox',)
