from django.contrib import admin
from django.db import models
from django.forms import Textarea

from quiz.models import Lesson, Variant, Question, VariantQuestions, Answer, TestType, TestTypeLesson


@admin.register(TestType)
class TestTypeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'duration',
        'has_by_lesson'
    )


@admin.register(TestTypeLesson)
class TestTypeLessonAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'test_type',
        'lesson',
        'order',
        'duration',
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name_kz',
    )


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'test_type',
        'language',
        'is_active',
    )
    list_filter = ['test_type', ]


@admin.register(VariantQuestions)
class VariantQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'variant',
        'question',
        'order',
    )
    list_filter = ['variant', ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'answer',
        'is_correct',
        'order',
    )


class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ('pk', 'order', 'is_correct', 'answer')
    readonly_fields = ('pk',)
    extra = 0
    # max_num = 4
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 80})},
    }


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = (
        'pk',
        'lesson',
        'point',
        'choice',
        'question'
    )
    list_filter = ['lesson', ]
    readonly_fields = ('pk', 'created', 'modified',)
    # list_filter = ['topic__lesson__test_type', 'topic__lesson', 'topic']
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 180})},
    }
