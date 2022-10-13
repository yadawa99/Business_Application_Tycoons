from django.shortcuts import render
from . models import *
# Create your views here.

def home(response):
    return render(response, 'quiz_web/home.html')
