import django_filters
from quiz.models import Lesson


class LessonFilter(django_filters.FilterSet):

    class Meta:
        model = Lesson
        fields = ['test_type', ]
