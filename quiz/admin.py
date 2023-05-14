from django.contrib import admin
from django.db import models
from django.forms import Textarea

from quiz.models import Lesson, Variant, Question, VariantQuestions, Answer

admin.site.register(Lesson)
admin.site.register(Answer)
admin.site.register(Variant)
admin.site.register(VariantQuestions)


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
        'question',
    )
    readonly_fields = ('pk', 'created', 'modified',)
    # list_filter = ['topic__lesson__test_type', 'topic__lesson', 'topic']
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 180})},
    }
