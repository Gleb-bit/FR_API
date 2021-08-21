from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    '''Model for questions'''
    title = models.CharField(max_length=255, default='')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    description = models.TextField(default='')
    questions = models.ManyToManyField('Question', related_name='quizzes')
    passage_date = models.DateField(null=True)
    passage_user_id = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    '''Model for questions'''

    CHOICES = [
        ('текст', 'ответ текстом'),
        ('один вариант', 'ответ с выбором одного варианта'),
        ('несколько вариантов', 'ответ с выбором нескольких вариантов'),
    ]

    text = models.TextField(default='')
    type = models.CharField(max_length=255, choices=CHOICES, default='текст')
    all_answers = models.CharField(max_length=255, default='')

    def split_all_answers(self):
        return self.all_answers.split(', ')

    def __str__(self):
        return self.text


class Answer(models.Model):
    '''Model for answers'''

    title = models.CharField(max_length=128, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
