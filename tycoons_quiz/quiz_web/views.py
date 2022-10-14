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
    form = QuizForm()
    return render(response, 'quiz_web/add_quizes.html',{"form":form})