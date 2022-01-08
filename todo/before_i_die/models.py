from django.db import models


class BeforeIDie(models.Model):
    text = models.CharField(max_length=255, verbose_name="Texto")
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Coisa a fazer antes de morrer'
        verbose_name_plural = 'Coisas a fazer antes de morrer'
