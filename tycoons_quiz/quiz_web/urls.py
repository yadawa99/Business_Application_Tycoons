from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("addq/", views.add_quizes, name="addq"),
    path("main/",views.main, name="main"),
    path("about_us/", views.about_us, name="about_us")

]