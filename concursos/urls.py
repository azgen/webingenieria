from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.concursos, name='concursos'),
    path('concursos/', views.concursos, name='concursos'),
    path('pdf/', views.concursos, name='pdf'),
]