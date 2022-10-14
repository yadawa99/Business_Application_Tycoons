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

def main(response):
    return render(response, 'quiz_web/main.html')

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

def add_question(request):
    questions = Question.objects.all()
    questions = Question.objects.filter().order_by('-id')
    if request.method=="POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "add_question.html")
    else:
        form=QuestionForm()
    return render(request, "add_question.html", {'form':form, 'questions':questions})

def delete_question(request, myid):
    question = Question.objects.get(id=myid)
    if request.method == "POST":
        question.delete()
        return redirect('/add_question')
    return render(request, "delete_question.html", {'question':question})

def add_options(request, myid):
    question = Question.objects.get(id=myid)
    QuestionFormSet = inlineformset_factory(Question, Answer, fields=('content','correct', 'question'), extra=4)
    if request.method=="POST":
        formset = QuestionFormSet(request.POST, instance=question)
        if formset.is_valid():
            formset.save()
            alert = True
            return render(request, "add_options.html", {'alert':alert})
        else:
            formset=QuestionFormSet(instance=question)
        return render(request, "add_options.html", {'formset':formset, 'question':question})

def results(request):
    marks = Marks_Of_User.objects.all()
    return render(request, "results.html", {'marks':marks})

def delete_result(request, myid):
    marks = Marks_Of_User.objects.get(id=myid)
    if request.method == "POST":
        marks.delete()
        return redirect('/results')
    return render(request, "delete_result.html", {'marks':marks})
def main(request):
    quiz = Quiz.objects.all()
    para = {'quiz' : quiz}
    return render(request, 'quiz_web/main.html', para )
def about_us(request):
    return render(request, 'quiz_web/about_us.html')

