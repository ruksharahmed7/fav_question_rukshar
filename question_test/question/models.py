from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    option5 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    explain = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class FavoriteQuestion(models.Model):
    user = models.ForeignKey(User, related_name='favquestions', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='favquestions', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username + '+' + self.question.question

class ReadQuestion(models.Model):
    user = models.ForeignKey(User, related_name='readquestions', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='readquestions', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username + '+' + self.question.question
