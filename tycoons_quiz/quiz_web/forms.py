from django import forms
from .models import Quiz, Question, Answer
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name', 'desc', 'number_of_questions', 'time')

    
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('content', 'quiz')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields ={"username", "email", "password1", "password2"}
