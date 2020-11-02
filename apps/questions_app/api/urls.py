from django.urls import path
from apps.questions_app.api.views import (QuestionsListAPIView)

urlpatterns = [
    path('questions', QuestionsListAPIView.as_view(), name='questions'),
]
