import datetime

from django.shortcuts import render, redirect
from django.views import generic

from quiz.models import Quiz, Question, Answer

now = datetime.datetime.now()


class QuizListView(generic.ListView):
    model = Quiz
    template_name = 'list_active_quizzes.html'
    context_object_name = 'quizzes'

    def get(self, request, *args, **kwargs):
        active_quizzes = Quiz.objects.filter(start_date__lte=now,
                                             end_date__gte=now).only('pk', 'title')
        all_quizzes = Quiz.objects.filter(passage_user_id=request.user.id)
        return render(request, self.template_name,
                      {self.context_object_name: active_quizzes, 'all_quizzes': all_quizzes})


class QuizDetailView(generic.DetailView):
    model = Quiz
    template_name = 'detail_quiz.html'
    context_object_name = 'quiz'

    def post(self, request, *args, **kwargs):
        quiz = self.get_object(self.queryset)
        for question in quiz.questions.all():
            self.create_answer(question=question, request=request, quiz=quiz)
        quiz.passage_date = datetime.datetime.now()
        quiz.passage_user_id = request.user.id
        quiz.save()
        return redirect(f'/results/{quiz.pk}/')

    def create_answer(self, question, request, quiz):
        if question.type == 'один вариант':
            user_answer = request.POST[f'one_answer {question}']
            Answer.objects.update_or_create(question=question, user=request.user,
                                            defaults={'quiz': quiz, 'title': user_answer})
        elif question.type == 'несколько вариантов':
            user_answers = request.POST.getlist(f'several_answers {question}')
            cur_answers = Answer.objects.filter(question=question)
            for cur_answer in cur_answers:
                cur_answer.delete()
            for user_answer in user_answers:
                Answer.objects.create(question=question, quiz=quiz, title=user_answer,
                                      user=request.user)
        else:
            user_answer = request.POST[f'{question}']
            Answer.objects.update_or_create(question=question, user=request.user,
                                            defaults={'quiz': quiz, 'title': user_answer})


class ResultsView(generic.DetailView):
    model = Quiz
    template_name = 'results.html'
    context_object_name = 'results'


class AnswerView(generic.CreateView):
    model = Question
    template_name = 'answer.html'
    context_object_name = 'question'
