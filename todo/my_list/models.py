from django.db import models


class MyList(models.Model):
    text = models.CharField(max_length=255, verbose_name="Texto")
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Minha Lista"
        verbose_name_plural = "Minhas Listas"
