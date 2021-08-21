from django import forms

from quiz.models import Answer


class AnswerForm(forms.Form):
    answer = forms.CharField(max_length=255)
    # class Meta:
    #     model = Answer
    #     fields = ['title', 'question', 'vote', 'choice']

