from django.urls import path, include
from rest_framework import routers

from quiz.views import LessonViewSet, VariantViewSet, QuestionVariantView, CreateQuestionView, QuestionViewSet, \
    SaveImageView

quizRouter = routers.DefaultRouter()
quizRouter.register(r'lesson', LessonViewSet, )
quizRouter.register(r'variant', VariantViewSet, )
quizRouter.register(r'question', QuestionViewSet, )

urlpatterns = [
    path('', include(quizRouter.urls)),
    path('variant-questions/<int:variant>/<int:lesson>/', QuestionVariantView.as_view(), name='variant-questions'),
    path('add-question/', CreateQuestionView.as_view(), name='add-question'),
    path('question-image/', SaveImageView.as_view(), name='add-image'),
]
