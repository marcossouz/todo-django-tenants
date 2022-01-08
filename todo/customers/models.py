from django.db import models
from django.contrib.auth import get_user_model
from django_tenants.models import TenantMixin, DomainMixin

User = get_user_model()


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Domain(DomainMixin):
    pass

    def __str__(self):
        return self.domain

    class Meta:
        verbose_name = 'Domain'
        verbose_name_plural = 'Domains'


class TenantUser(User):
    client = models.ForeignKey(
        Client, verbose_name='Client', on_delete=models.PROTECT)

    class Meta(User.Meta):
        verbose_name = 'Tenant User'
        verbose_name_plural = 'Tenants User'
