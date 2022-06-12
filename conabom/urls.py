from django.contrib import admin
from django.urls import path
from conabom import views


urlpatterns = [
    
    path('index/', views.inicio, name='index'),
    path('user_index/', views.userIndex, name='userIndex'),
    path('register/', views.registro, name='register'),
    path('accounts/user_index/userAplication/', views.userApplication, name='userApplication'),
    
]