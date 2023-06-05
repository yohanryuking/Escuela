from django.shortcuts import render, redirect
from .models import Curso

# Create your views here.


def home(request):
    cursos = Curso.objects.all()
    return render(request, "gestion.html", {"cursos": cursos})


def registar(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)

    return redirect('/')

def eliminar(request, codigo):
    
    curso= Curso.objects.get(codigo=codigo)
    curso.delete()
    
    return redirect('/')

def edicion(request, codigo):
    curso= Curso.objects.get(codigo=codigo)
    return render(request, "edicion.html", {"curso":curso})

def editar(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    
    return redirect('/')
    
