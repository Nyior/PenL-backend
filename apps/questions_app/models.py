from django.db import models


class Choice(models.Model):
    """ This class models an answer object
    """
    body = models.CharField(max_length=100)

    def __str__(self):
        return self.body


class Question(models.Model):
    """ This class models a question object
    """
    body = models.CharField(max_length=500)
    answer = models.ForeignKey(
                                     Choice,
                                     on_delete=models.SET_NULL,
                                     related_name='question_answer_to',
                                     null=True,
                                     blank=True
                                     )
    choices = models.ManyToManyField(
                                     Choice,
                                     )
    answer_explanation = models.TextField(
                                            null=True,
                                            blank=True
                                        )

    def __str__(self):
        return self.body
