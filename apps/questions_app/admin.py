from django.contrib import admin
from apps.questions_app.models import (
                                        Question,
                                        Choice
                                        )
from django.contrib.auth.models import Group


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    # list_display = ['id', 'username', 'points']


class ChoiceAdmin(admin.ModelAdmin):
    model = Choice


admin.site.unregister(Group)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
