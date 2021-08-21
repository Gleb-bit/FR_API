from django.urls import path

from quiz.views import *

urlpatterns = [
    path('quizzes/', QuizListView.as_view(), name='quizzes'),
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz_detail'),
    path('answer/<int:pk>/', AnswerView.as_view(), name='answer'),
    path('results/<int:pk>/', ResultsView.as_view(), name='results'),
]
