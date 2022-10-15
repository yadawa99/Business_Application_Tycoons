from django.shortcuts import render, redirect
from . models import *
from .forms import QuizForm, QuestionForm, CreateUserForm
from django.http import JsonResponse
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
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
            return render(response, "quiz_web/add_quizes.html", {'obj':obj})
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
            return render(request, "quiz_web/add_question.html")
    else:
        form=QuestionForm()
    return render(request, "quiz_web/add_question.html", {'form':form, 'questions':questions})

def delete_question(request, myid):
    question = Question.objects.get(id=myid)
    if request.method == "POST":
        question.delete()
        return redirect('/add_question')
    return render(request, "quiz_web/delete_question.html", {'question':question})

def add_options(request, myid):
    question = Question.objects.get(id=myid)
    QuestionFormSet = inlineformset_factory(Question, Answer, fields=('content','correct', 'question'), extra=4)
    if request.method=="POST":
        formset = QuestionFormSet(request.POST, instance=question)
        if formset.is_valid():
            formset.save()
            alert = True
            return render(request, "quiz_web/add_answers.html", {'alert':alert})
        else:
            formset=QuestionFormSet(instance=question)
        return render(request, "quiz_web/add_answers.html", {'formset':formset, 'question':question})

def results(request):
    marks = Marks_Of_User.objects.all()
    return render(request, "quiz_web/results.html", {'marks':marks})

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

@login_required(login_url = '/login')
def quiz(request, myid):
    quiz = Quiz.objects.get(id=myid)
    return render(request, "quiz_web/quiz.html", {'quiz':quiz})

def quiz_data_view(request, myid):
    quiz = Quiz.objects.get(id=myid)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.content)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

def save_quiz_view(request, myid):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(content=k)
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(id=myid)

        score = 0
        marks = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.content)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.content:
                        if a.correct:
                            score += 1
                            correct_answer = a.content
                    else:
                        if a.correct:
                            correct_answer = a.content

                marks.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                marks.append({str(q): 'not answered'})
     
        Marks_Of_User.objects.create(quiz=quiz, user=user, score=score)
        
        return JsonResponse({'passed': True, 'score': score, 'marks': marks})

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("quiz_web/main.html")
        else:
            return render(request, "quiz_web/login.html")
    return render(request, "quiz_web/login.html")

def Logout(request):
    logout(request)
    return redirect('quiz_web/login.html')

def Signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password != confirm_password:
            return redirect('/register')

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return render(request, 'quiz_web/login.html')
    return render(request, "quiz_web/signup.html")

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.post)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "quiz_web/register.html", context)
