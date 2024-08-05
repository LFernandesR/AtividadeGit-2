from django.contrib import admin
from django.urls import path
from .views import index, lucas

urlpatterns = [
    path('', index, name = 'index'),
    path('lucas', lucas, name = 'lucas')
]
