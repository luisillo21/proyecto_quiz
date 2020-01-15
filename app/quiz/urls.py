from django.urls import path
from proyecto_quiz.app.quiz.views import *

urlpatterns = [
    path('',index,name='index'),
    path('agregar_examen/',agregar_examen, name='agregar_examen'),
    path('crear_usuario/',crear_usuario, name='crear_usuario'),
    path('login/',login, name='iniciar_sesion'),
    path('cerrar/',cerrar_sesion, name='cerrar_sesion'),
]