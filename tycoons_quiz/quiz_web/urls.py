from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("", views.home, name="home"),
    path("addq/", views.add_quizes, name="addq"),
    path("main/",views.main, name="main"),
    path("about_us/", views.about_us, name="about_us"),

    path("<int:myid>/", views.quiz, name="quiz"), 
    path('<int:myid>/data/', views.quiz_data_view, name='quiz-data'),
    path('<int:myid>/save/', views.save_quiz_view, name='quiz-save'),
    
    path("signup/", views.signup, name="signup"),
    path("login/", LoginView.as_view(template_name='quiz_web/login.html'), name="login"),
    path("logout/", views.logout, name="logout"),
    
  
    path('add_question/', views.add_question, name='add_question'),  
    path('add_options/<int:myid>/', views.add_options, name='add_options'), 
    path('results/', views.results, name='results'),    
    path('delete_question/<int:myid>/', views.delete_question, name='delete_question'),  
    path('delete_result/<int:myid>/', views.delete_result, name='delete_result'),    

]