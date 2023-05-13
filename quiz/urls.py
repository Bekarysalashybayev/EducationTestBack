from django.urls import path, include

from quiz.views import TestApi

urlpatterns = [
    path('', TestApi.as_view()),
]
