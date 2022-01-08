from django.contrib import admin

from .models import MyList


@admin.register(MyList)
class MyListAdmin(admin.ModelAdmin):
    list_display = ('text', 'checkbox',)
