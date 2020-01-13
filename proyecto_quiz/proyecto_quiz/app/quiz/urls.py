from django.urls import path
from proyecto_quiz.app.quiz.views import *

urlpatterns = [
    path('',index,name='index'),
    path('agregar_examen/', agregar_examen, name='agregar_examen'),
]