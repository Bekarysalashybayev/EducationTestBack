from django.urls import path, include
from rest_framework import routers

from quiz.views import LessonViewSet

quizRouter = routers.DefaultRouter()
quizRouter.register(r'lesson', LessonViewSet, )

urlpatterns = [
    path('', include(quizRouter.urls)),
]
