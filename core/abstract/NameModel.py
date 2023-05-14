from django.db import models


class NameModel(models.Model):
    name_kz = models.CharField(
        max_length=55,
        null=False,
        blank=False,
        verbose_name="Название KZ"
    )
    name_ru = models.CharField(
        max_length=55,
        null=False,
        blank=False,
        verbose_name="Название RU"
    )

    class Meta:
        abstract = True
