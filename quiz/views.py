from django.shortcuts import redirect, render, get_list_or_404
from quiz.forms import *
from quiz.models import *
import random

from django.shortcuts import render
from .models import Question


def quiz_home(request, id):
    questions = Question.objects.filter(category_id=id).order_by('?')[:5]
    total = len(questions)

    if request.method == 'POST':
        # Get all the questions of the specified category
        score = sum(10 for q in questions if q.answer == request.POST.get(q.question))
        correct = sum(1 for q in questions if q.answer == request.POST.get(q.question))
        wrong = total - correct
        percent = (score / (total * 10)) * 100
        context = {
            'questions': questions,
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'Quiz/result.html', context)
    else:
        # questions = get_list_or_404(Question, category_id=id)
        context = {
            'questions': questions
        }
        return render(request, 'Quiz/home.html', context)


def add_question(request):
    if request.user.is_staff:
        form = AddQuestionForm()
        if request.method == 'POST':
            form = AddQuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'Quiz/addQuestion.html', context)
    else:
        return redirect('home')


def quiz_categories(request):
    quiz_category = QuestionCategory.objects.all()
    context = {
        'quiz_categroy': quiz_category
    }
    return render(request, 'Quiz/quiz_category.html', context)
