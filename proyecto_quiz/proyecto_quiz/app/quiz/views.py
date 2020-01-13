from django.shortcuts import render,redirect
from proyecto_quiz.app.quiz.models import *
# Create your views here.

def index(request):
    lista_examenes= Examen.objects.filter()
    return render(request,'index.html',{'examenes':lista_examenes})

def agregar_examen(request):
    if request.method == 'POST':
        nom_usuario = request.POST.get('nom_usuario')
        nom_examen = request.POST.get('nom_examen')
        Examen.objects.create(nombre=request.POST.get('nom_examen'),nombre_usuario=nom_usuario)
        """
        Pregunta.objects.create(pregunta=request.POST.get('pregunta'),
                                opcion1=request.POST.get('opcion1'),
                                opcion2=request.POST.get('opcion2'),
                                opcion3=request.POST.get('opcion3'),
                                answer=request.POST.get('respuesta'))"""
        return redirect('quiz:index')
    return render(request,'crear_examen.html')
