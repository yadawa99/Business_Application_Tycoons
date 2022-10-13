from django.shortcuts import render
from . models import *
from .forms import QuizForm, QuestionForm
# Create your views here.

def home(response):
    return render(response, 'quiz_web/home.html')

def add_quizes(response):
    if response.method == "POST":
        form = QuizForm(data=response.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()
            obj = form.instance
            return render(response, "add_quizes.html", {'obj': obj})
    else:
        form = QuizForm()
    return render(response, 'quiz_web/add_quizes.html')