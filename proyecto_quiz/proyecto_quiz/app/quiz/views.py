from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from proyecto_quiz.app.quiz.models import *
# Create your views here.

def index(request):
    lista_examenes = Examen.objects.filter()
    if 'usuario' in request.session:
       mis_examenes = Examen.objects.filter(usuario=request.session['usuario'])
       return render(request,'inicio.html',{'examenes':mis_examenes})

    return render(request,'index.html',{'examenes':lista_examenes})

def agregar_examen(request):
    if request.method == 'POST':
        usuario =Usuario.objects.get(id_autor=request.session['usuario'])
        Examen.objects.create(nombre=request.POST.get('nom_examen'),usuario=usuario)
        return redirect('quiz:index')
    return render(request,'crear_examen.html')

def crear_usuario(request):
    if request.method == 'POST':
        Usuario.objects.create(nombre=request.POST.get('nombre'),
                               apellido=request.POST.get('apellido'),
                               nombre_usuario=request.POST.get('usuario'),
                               clave=request.POST.get('clave'))
        return redirect('quiz:index')
    return render(request,'crear_usuario.html')

def login(request):
    if request.method=='POST':
        usuario = Usuario.objects.filter(nombre_usuario=request.POST.get('usuario'), clave=request.POST.get('clave'))
        for u in usuario:
           print(u.nombre_usuario)
           if u:
              request.session['usuario'] = u.id_autor
              return redirect('quiz:index')
           break
    return render(request,'login.html')

def cerrar_sesion(request):
    del request.session['usuario']
    return HttpResponseRedirect('../')