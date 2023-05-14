from django.db import models

from core.abstract.NameModel import NameModel
from core.constants.LanguagesChoices import LANGUAGE_CHOICES
from core.constants.TestTypesChoices import TEST_TYPES


class Lesson(NameModel):
    test_type = models.CharField(
        max_length=10,
        choices=TEST_TYPES.choices(),
        null=False,
        blank=False,
        verbose_name="Тип Теста"
    )
    order = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Очередь"
    )
    duration = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Длительность в минутах"
    )
    icon = models.ImageField(
        upload_to='lessons/',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'lesson'
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
        unique_together = ['test_type', 'order']
        ordering = ["order"]

    def __str__(self):
        return f"{self.name_kz}"


class Variant(models.Model):
    test_type = models.CharField(
        max_length=10,
        choices=TEST_TYPES.choices(),
        null=False,
        blank=False,
        verbose_name="Тип Теста"
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="Название"
    )
    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES.choices(),
        null=False,
        blank=False,
        verbose_name="Язык варианта"
    )
    icon = models.ImageField(
        upload_to='variants/',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )

    class Meta:
        db_table = 'variant'
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"
        unique_together = ['test_type', 'name']
        ordering = ["id"]

    def __str__(self):
        return f"{self.test_type} -> {self.name} -> {self.language}"


class Question(models.Model):
    question = models.TextField(
        null=False,
        blank=False,
        verbose_name="Вопрос"
    )

    point = models.IntegerField(default=1)

    class Meta:
        db_table = 'questions'
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["id"]

    def __str__(self):
        return f"{self.question}"


class VariantQuestions(models.Model):
    variant = models.ForeignKey(
        Variant,
        on_delete=models.CASCADE,
        related_name='variant_questions',
        null=False,
        blank=False,
        verbose_name="Вариант"
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='variant_questions',
        null=False,
        blank=False,
        verbose_name="Предмет"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='variant_questions',
        null=False,
        blank=False,
        verbose_name="Предмет"
    )

    order = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Очередь"
    )

    class Meta:
        db_table = 'variant_questions'
        verbose_name = "Вопросы варианта"
        verbose_name_plural = "Вопросы варианта"
        unique_together = ['variant', 'lesson', 'question']
        ordering = ["id"]

    def __str__(self):
        return f"{self.test_type} + {self.name}"
