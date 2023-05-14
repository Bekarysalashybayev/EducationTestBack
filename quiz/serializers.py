from rest_framework import serializers

from quiz.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """ Предметы """

    class Meta:
        model = Lesson
        fields = "__all__"
