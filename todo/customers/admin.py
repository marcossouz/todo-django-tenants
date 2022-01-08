from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from django.contrib.auth.admin import UserAdmin

from customers.models import Client, Domain, TenantUser
from customers.forms import TenantUserChangeForm, TenantUserCreationForm


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'paid_until')


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant')


@admin.register(TenantUser)
class TenantUserAdmin(UserAdmin):
    add_form = TenantUserCreationForm
    form = TenantUserChangeForm

    list_display = ('username', 'email', 'client', 'is_active',)
    list_display_links = list_display
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'is_active',)}),
        ('Permissões', {'fields': ('client',)}),
        ('Datas importantes', {'fields': ('date_joined', 'last_login')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'client', 'password1', 'password2',)}),
    )
    search_fields = ('email', 'client__name', 'client__schema_name')
    ordering = ('email',)
    filter_horizontal = ['user_permissions']
    list_per_page = 30
