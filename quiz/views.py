from rest_framework import permissions, generics, status
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.pagination.pagination import StandardPagination
from core.permissions.permissionList import TeacherPermission
from quiz.filter import LessonFilter, VariantFilter
from quiz.models import Lesson, Variant, VariantQuestions, Question
from quiz.serializers import LessonSerializer, VariantSerializer, QuestionVariantSerializer, \
    VariantQuestionCreateSerializer, QuestionCreationSerializer, ImageUploadSerializer


class LessonViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """ Предметы """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filterset_class = LessonFilter


class VariantViewSet(ListModelMixin, RetrieveModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet):
    """ Варианты """

    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    permission_classes = [TeacherPermission]
    pagination_class = StandardPagination

    filterset_class = VariantFilter


class QuestionVariantView(generics.ListAPIView):
    """ Вопросы Варианта """

    queryset = VariantQuestions.objects.all().select_related('variant', 'question')
    serializer_class = QuestionVariantSerializer
    permission_classes = [TeacherPermission]
    lookup_field = None

    def get_queryset(self):
        variant = self.kwargs.get('variant')
        lesson = self.kwargs.get('lesson')
        queryset = super().get_queryset().filter(variant=variant, question__lesson=lesson)
        return queryset


class CreateQuestionView(generics.CreateAPIView):
    """ Добавление Вопроса к Варианту """

    queryset = VariantQuestions.objects.all()
    serializer_class = VariantQuestionCreateSerializer
    permission_classes = [TeacherPermission]


class QuestionViewSet(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """ Вопросы """

    queryset = Question.objects.all()
    serializer_class = QuestionCreationSerializer
    permission_classes = [TeacherPermission]


class SaveImageView(CreateAPIView):
    serializer_class = ImageUploadSerializer

    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs).data
        return Response({"url": data.get('upload')},
                        status=status.HTTP_201_CREATED)
