from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    return render(response,"quiz_web/home.html",{})
