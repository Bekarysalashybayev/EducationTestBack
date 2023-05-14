from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from quiz.filter import LessonFilter
from quiz.models import Lesson
from quiz.serializers import LessonSerializer


class LessonViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """ Предметы """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filterset_class = LessonFilter
