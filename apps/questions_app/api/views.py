from rest_framework import generics

from apps.questions_app.api.serializers import (QuestionSerializer)
from apps.questions_app.models import Question

import random


class QuestionsListAPIView(generics.ListAPIView):
    """this endpoint randomly returns a list of 10 questions"""
    serializer_class = QuestionSerializer

    def get_queryset(self):
        pool = list(Question.objects.all())
        random.shuffle(pool)
        object_list = pool[:3]
        return object_list
