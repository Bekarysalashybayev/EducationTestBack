from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from quiz.models import Lesson, Variant, VariantQuestions, Question, Answer


class LessonSerializer(serializers.ModelSerializer):
    """ Предметы """

    class Meta:
        model = Lesson
        fields = ('id', 'name_ru', 'icon')


class AnswerSerializer(serializers.ModelSerializer):
    """ Ответы """

    class Meta:
        model = Answer
        fields = ('pk', 'answer', 'order')


class AnswerCreationSerializer(serializers.ModelSerializer):
    """ Добавление Ответа """

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'order', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):
    """ Вопросы """

    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question', 'point', 'answers')


class QuestionCreationSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    """ Добавление Вопроса """

    answers = AnswerCreationSerializer(many=True, required=True)

    class Meta:
        model = Question
        fields = ('id', 'question', 'point', 'lesson', 'answers')


class QuestionVariantSerializer(serializers.ModelSerializer):
    """ Вопросы варианта """
    question = QuestionSerializer(read_only=True, )

    class Meta:
        model = VariantQuestions
        fields = ('question',)


class VariantQuestionCreateSerializer(WritableNestedModelSerializer, ):
    """ Добавление Вопроса к варианту """
    question = QuestionCreationSerializer(required=True)

    class Meta:
        model = VariantQuestions
        fields = ('variant', 'question', 'order')


class VariantSerializer(serializers.ModelSerializer):
    """ Варианты """

    class Meta:
        model = Variant
        fields = "__all__"


class VariantQuestionSerializer(serializers.ModelSerializer):
    """ Вопросы с Вариантами """

    class Meta:
        model = VariantQuestions
        fields = "__all__"
