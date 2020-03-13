from django.db import models
from quiz.models import Quiz

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    question = models.TextField(verbose_name='question', null=True)
    choice1 = models.TextField(verbose_name='choice1', null=True)
    choice2 = models.TextField(verbose_name='choice2', null=True)
    choice3 = models.TextField(verbose_name='choice3', null=True)
    choice4 = models.TextField(verbose_name='choice4', null=True)
    answer = models.CharField(max_length=200)
