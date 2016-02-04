from questionnaire.models import *
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'text', 'q_type', 'options', 'answer')
        depth = 1

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'check', 'number', 'yesno', 'question', 'user')
