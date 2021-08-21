from rest_framework import serializers

from .models import Quiz, Question


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    passage_user_id = serializers.ReadOnlyField()

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'start_date', 'end_date', 'description', 'passage_user_id']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    quizzes = serializers.HyperlinkedRelatedField(many=True, queryset=Quiz.objects.all(), view_name='quizzes-detail')

    class Meta:
        model = Question
        fields = ['id', 'text', 'type', 'all_answers', 'quizzes']
