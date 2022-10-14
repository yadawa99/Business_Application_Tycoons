from django.shortcuts import render, redirect
from . models import *
from .forms import QuizForm, QuestionForm
from django.http import JsonResponse
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
# Create your views here.

def home(response):
    return render(response, 'quiz_web/home.html')

def add_quizes(response):
    if response.method=="POST":
        form = QuizForm(data=response.POST)
        
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()
            obj = form.instance
            return render(response, "add_quizes.html", {'obj':obj})
    else:
        form=QuizForm()
    return render(response, 'quiz_web/add_quizes.html',{"form":form})