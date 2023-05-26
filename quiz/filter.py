import django_filters
from quiz.models import Lesson, Variant


class LessonFilter(django_filters.FilterSet):
    test_type = django_filters.CharFilter(field_name='test_type_lessons__test_type__name', lookup_expr='iexact')

    class Meta:
        model = Lesson
        fields = ['test_type', ]


class VariantFilter(django_filters.FilterSet):
    test_type = django_filters.CharFilter(field_name='test_type__name', lookup_expr='iexact')

    class Meta:
        model = Variant
        fields = ['test_type', ]
