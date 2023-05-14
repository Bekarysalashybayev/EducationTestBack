import django_filters
from quiz.models import Lesson, Variant


class LessonFilter(django_filters.FilterSet):

    class Meta:
        model = Lesson
        fields = ['test_type', ]


class VariantFilter(django_filters.FilterSet):

    class Meta:
        model = Variant
        fields = ['test_type', ]