from django.urls import re_path
from django.urls import path
from . import views



urlpatterns = [
    path('', views.phonebook, name='phonebook'),
    path('login/', views.authorization, name='authorization'),
    path('index/', views.index, name='index'),
]