from rest_framework import viewsets, permissions

from .models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer


class QuizViewSet(viewsets.ModelViewSet):
    '''Information about quizzes'''

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionViewSet(viewsets.ModelViewSet):
    '''Information about questions'''

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]
