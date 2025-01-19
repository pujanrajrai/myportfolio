from django.contrib import admin
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home, name="home"),
    path('create-education/', views.education_create, name="education_create"),

]
