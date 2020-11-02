from rest_framework import serializers
from apps.questions_app.models import (
                                    Choice,
                                    Question
                                    )


class ChoiceSerializer(serializers.ModelSerializer):
    """ This serialiazes a choice object"""

    class Meta:
        model = Choice
        fields = ['body']


class QuestionSerializer(serializers.ModelSerializer):
    answer = serializers.StringRelatedField()
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'body', 'answer', 'choices', 'answer_explanation']

    def get_choices(self, object):
        return object.choices.all()
