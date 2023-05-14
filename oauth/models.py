from django.contrib.auth.models import AbstractUser
from django.db import models

from core.abstract.TimeStampedModel import TimeStampedModel
from core.constants.RoleChoices import ROLES


class Role(models.Model):
    name = models.CharField(max_length=11, choices=ROLES.choices(), unique=True, default=ROLES.STUDENT)

    class Meta:
        db_table = 'user_role'

    def __str__(self):
        return f"{self.name}"


class User(AbstractUser, TimeStampedModel):
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='users',
        null=True,
        blank=True,
        verbose_name="Роль"
    )

    middle_name = models.CharField(
        max_length=150,
        default='',
        blank=True,
        verbose_name="Отчество"
    )

    is_active = models.BooleanField(null=False, blank=False, default=True)
    is_staff = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        db_table = 'user'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователеи"

    def __str__(self):
        return self.username
